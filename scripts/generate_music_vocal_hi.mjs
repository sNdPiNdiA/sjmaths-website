#!/usr/bin/env node
/**
 * SJ Maths — Hindi Music Vocal topic-page generator.
 *
 * Generates static, crawlable pages with four tabs:
 * 1. अध्ययन नोट्स  2. अवधारणा क्विज़  3. पुनरावृत्ति सारांश  4. विषय परीक्षा
 *
 * Default API key: GEMINI_API_KEY_1. Use --key 1, --topic, --all or --dry-run.
 */

import fs from 'node:fs';
import path from 'node:path';
import 'dotenv/config';
import { GoogleGenAI } from '@google/genai';
import { parseMusicJson as parseJson } from './lib/music-json-parser.mjs';
import { musicVocalTopicScript } from './lib/music-vocal-runtime.mjs';
import { musicVocalTopicStyleLink } from './lib/music-vocal-styles.mjs';
import { compileMusicVocalHtml } from './lib/music-vocal-renderer.mjs';
import { QUESTION_TYPES, validateContent, validateQuestions } from './lib/music-vocal-schema.mjs';
import { generateMusicJson } from './lib/music-json-request.mjs';

const ROOT = process.cwd();
const SUBJECT_ROOT = path.join(ROOT, 'music-vocal');
const TRACKER_PATH = path.join(ROOT, 'up-pgt-music-vocal', 'index.html');
const STATUS_PATH = path.join(ROOT, 'content-generation-status-music-vocal-hi.json');
const MODEL = process.env.GEMINI_MODEL || 'gemini-3.5-flash-lite';

const args = process.argv.slice(2);
const hasFlag = (flag) => args.includes(flag);
function argValue(flag) { const index = args.indexOf(flag); return index >= 0 ? args[index + 1] : null; }
const requestedTopic = argValue('--topic');
const dryRun = hasFlag('--dry-run');
const allFlag = hasFlag('--all');
const force = hasFlag('--force');
const limit = Number.parseInt(argValue('--limit') || '0', 10) || 0;
const gapMs = Math.max(0, Number.parseInt(argValue('--gap') || '10', 10) || 0) * 1000;
const keySelector = argValue('--key') || '1';

function stripTags(value) {
  return String(value || '').replace(/<[^>]*>/g, ' ')
    .replace(/&amp;/g, '&').replace(/&quot;/g, '"').replace(/&#39;/g, "'")
    .replace(/&ndash;/g, '–').replace(/&mdash;/g, '—').replace(/&rsquo;/g, '’')
    .replace(/&ldquo;/g, '“').replace(/&rdquo;/g, '”').replace(/&nbsp;/g, ' ')
    .replace(/&#(\d+);/g, (_, code) => String.fromCodePoint(Number(code)))
    .replace(/&#x([\da-f]+);/gi, (_, code) => String.fromCodePoint(Number.parseInt(code, 16)))
    .replace(/\s+/g, ' ').trim();
}

function normalizeUrl(value) {
  let url = String(value || '').trim().replace(/\\/g, '/');
  if (!url.startsWith('/')) url = `/${url}`;
  if (!url.endsWith('/')) url += '/';
  return url.replace(/\/index\.html\/$/, '/');
}

function urlToDir(url) { return path.join(ROOT, url.replace(/^\//, '').replace(/\/$/, '')); }

function titleFromSlug(value) {
  return String(value || 'Music Vocal').split('-').filter(Boolean).map((word) => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
}

function getContext(url, contexts) {
  const listed = contexts.get(url);
  if (listed) return listed;
  const parts = url.split('/').filter(Boolean);
  const fallback = { url, topicName: titleFromSlug(parts.at(-1)), sectionTitle: titleFromSlug(parts[1] || 'Music Vocal'), key: parts.slice(1).join('/') };
  const indexPath = path.join(urlToDir(url), 'index.html');
  if (!fs.existsSync(indexPath)) return fallback;
  const html = fs.readFileSync(indexPath, 'utf8');
  const heading = html.match(/<h1[^>]*>([\s\S]*?)<\/h1>/i)?.[1];
  const oldTitle = html.match(/<title>([\s\S]*?)<\/title>/i)?.[1];
  const pageTitle = stripTags(heading || oldTitle || '').replace(/\s*[|—–-]\s*(Music Vocal|Music Vocal Study Guide|SJ Maths).*$/i, '').trim();
  if (pageTitle) fallback.topicName = pageTitle;
  return fallback;
}

function isHindiGeneratedPage(indexPath) {
  if (!fs.existsSync(indexPath)) return false;
  const html = fs.readFileSync(indexPath, 'utf8');
  return html.includes('<html lang="hi"') && html.includes('id="quiz-data"') && html.includes('id="test-data"');
}

function readStatus() {
  if (!fs.existsSync(STATUS_PATH)) return {};
  try { return JSON.parse(fs.readFileSync(STATUS_PATH, 'utf8')); } catch { return {}; }
}

function writeStatus(status) {
  try { fs.writeFileSync(STATUS_PATH, `${JSON.stringify(status, null, 2)}\n`, 'utf8'); }
  catch (error) { console.warn(`Warning: could not update status log (${error.code || error.message}); generation will continue.`); }
}

function readTrackerContexts() {
  if (!fs.existsSync(TRACKER_PATH)) return new Map();
  const html = fs.readFileSync(TRACKER_PATH, 'utf8');
  const contexts = new Map();
  const sectionRegex = /<article[^>]*class="section-card"[^>]*id="[^"]+"[^>]*>([\s\S]*?)(?=<article[^>]*class="section-card"|<\/section>)/gi;
  let sectionMatch;
  while ((sectionMatch = sectionRegex.exec(html))) {
    const sectionHtml = sectionMatch[1];
    const sectionTitle = stripTags(sectionHtml.match(/<span class="section-title">([\s\S]*?)<\/span>/i)?.[1] || 'Music Vocal');
    const topicRegex = /<div class="topic"[^>]*data-key="([^"]+)"[\s\S]*?<a class="topic-link" href="([^"]+)">([\s\S]*?)<\/a>/gi;
    let topicMatch;
    while ((topicMatch = topicRegex.exec(sectionHtml))) {
      const url = normalizeUrl(topicMatch[2]);
      contexts.set(url, { url, topicName: stripTags(topicMatch[3]), sectionTitle, key: topicMatch[1] });
    }
  }
  return contexts;
}

function discoverTopicUrls() {
  const urls = [];
  function walk(dir) {
    if (!fs.existsSync(dir)) return;
    for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
      const full = path.join(dir, entry.name);
      if (entry.isDirectory()) walk(full);
      else if (entry.name === 'index.html') urls.push(normalizeUrl(`/${path.relative(ROOT, full).replace(/\\/g, '/')}`));
    }
  }
  walk(SUBJECT_ROOT);
  return urls.sort();
}

function resolveTargets(contexts) {
  const all = discoverTopicUrls();
  let targets;
  if (requestedTopic) {
    const url = normalizeUrl(requestedTopic);
    if (!all.includes(url)) throw new Error(`Topic page not found: ${url}`);
    targets = [url];
  } else if (allFlag || dryRun) targets = all;
  else throw new Error('Choose --topic /music-vocal/.../, --all, or --dry-run.');
  return limit > 0 ? targets.slice(0, limit) : targets;
}


function buildContentPrompt(context) {
  return `आप UP PGT Music Vocal (Sangeet Gayan) के वरिष्ठ शिक्षक और परीक्षा-विशेषज्ञ हैं।
विषय: "${context.topicName}"
पाठ्यक्रम खंड: "${context.sectionTitle}"

इस विषय पर सटीक, point-wise हिन्दी (देवनागरी) सामग्री तैयार करें। संगीत के आवश्यक technical terms के बाद English term कोष्ठक में दे सकते हैं। लंबे अनुच्छेद न लिखें। हर concept को अलग रखें और विषय के सभी उप-विषयों को कवर करें। कलाकार, राग, ग्रंथ, काल या ऐतिहासिक तथ्य तभी दें जब वे विश्वसनीय और विषय से सीधे संबंधित हों। परिचय के बिंदु सीधे संगीत-विषय समझाएँ; परीक्षा, पाठ्यक्रम, तैयारी या अभ्यर्थियों के बारे में प्रचारात्मक वाक्य न लिखें। परीक्षा-संबंधी तथ्य केवल संबंधित अवधारणा के परीक्षा-केंद्रित बिंदुओं में रखें।

अनिवार्य JSON संरचना:
{
  "title":"हिन्दी SEO शीर्षक",
  "section_title_hi":"पाठ्यक्रम खंड का हिन्दी शीर्षक",
  "short_title":"छोटा हिन्दी शीर्षक",
  "introduction_points":["कम-से-कम 4 छोटे बिंदु"],
  "concepts":[{
    "id":"stable-kebab-case-id",
    "title":"अवधारणा का हिन्दी शीर्षक",
    "lead":"एक वाक्य का सार",
    "explanation_points":["कम-से-कम 5 बिंदु"],
    "key_points":["कम-से-कम 4 मुख्य बिंदु"],
    "examples":["कम-से-कम 2 सही संगीत उदाहरण"],
    "comparison_points":["कम-से-कम 2 तुलना बिंदु"],
    "common_misconceptions":["कम-से-कम 2 सामान्य भ्रांतियाँ"],
    "exam_focus_points":["कम-से-कम 3 परीक्षा-केंद्रित बिंदु"]
  }],
  "revision":{
    "concept_revisions":[{"concept_id":"exact concept id","title":"अवधारणा शीर्षक","definition_points":["कम-से-कम 3 परिभाषात्मक बिंदु"],"must_remember":["कम-से-कम 5 सूक्ष्म स्मरण बिंदु"],"exam_traps":["कम-से-कम 2 परीक्षा-जाल"]}],
    "quick_facts":["कम-से-कम 5 तथ्य"],
    "glossary":[{"term":"शब्द","definition":"हिन्दी परिभाषा"}],
    "comparisons":[{"left":"A","right":"B","difference_points":["कम-से-कम 2 अंतर"]}],
    "memory_hooks":["कम-से-कम 3 स्मृति-सहायक बिंदु"],
    "exam_traps":["कम-से-कम 4 सावधानियाँ"]
  }
}
4 से 8 अलग-अलग अवधारणाएँ दें। केवल वैध JSON लौटाएँ।`;
}

function buildQuestionsPrompt(context, content) {
  const concepts = content.concepts.map((item) => `- ${item.id}: ${item.title} — ${item.lead}`).join('\n');
  return `आप UP PGT Music Vocal के परीक्षा-विशेषज्ञ हैं। नीचे दिए गए हिन्दी अध्ययन-नोट्स के आधार पर interactive quiz और timed test बनाइए।
विषय: "${context.topicName}"
अवधारणाएँ:
${concepts}

नियम:
- पूरा उत्तर केवल वैध JSON में दें। सभी प्रश्न, विकल्प और explanations हिन्दी देवनागरी में हों; आवश्यक music terms English में रख सकते हैं।
- हर concept_id के लिए इन सातों प्रकारों में कम-से-कम एक प्रश्न दें: ${QUESTION_TYPES.join(', ')}.
- प्रश्नों में स्वर, श्रुति, राग, ताल, लय, गायन-शैली, वाद्य-संगत, notation, संगीत-इतिहास और दिए गए विषय के लागू उप-विषय शामिल करें; केवल शीर्षक दोहराने वाले प्रश्न न बनाएं।
- assertion_reason में assertion, reason और चार मानक विकल्प दें। match_following में दोनों सूचियाँ और चार coded options दें। case_based में छोटा संगीत-अभ्यास या performance scenario दें। fill_blank में accepted_answers और short_answer में expected_answer दें।
- topic_test में ठीक 10 objective questions हों; type केवल mcq, assertion_reason, match_following या case_based हो।
- कोई तथ्य, कलाकार, रचना या ऐतिहासिक attribution न गढ़ें।

यह exact JSON shape लौटाएँ:
{"quiz_questions":[{"id":"q-001","concept_id":"concept-id","type":"mcq|assertion_reason|true_false|fill_blank|match_following|case_based|short_answer","question":"हिन्दी प्रश्न","options":["विकल्प 1","विकल्प 2","विकल्प 3","विकल्प 4"],"correct_index":0,"accepted_answers":["उत्तर"],"expected_answer":"उत्तर","explanation":"हिन्दी व्याख्या"}],"topic_test":[{"id":"t-001","concept_id":"concept-id","type":"mcq","question":"हिन्दी प्रश्न","options":["...","...","...","..."],"correct_index":0,"explanation":"हिन्दी व्याख्या"}]}`;
}

async function generateJson(prompt, ai, validator, label, maxAttempts = 3) {
  return generateMusicJson(prompt, ai, validator, label, { model: MODEL, parseJson, maxAttempts });
}

function compileHtml(content, questions, context) {
  return compileMusicVocalHtml(content, questions, context, { musicVocalTopicScript, musicVocalTopicStyleLink });
}

function chooseApiKey() {
  const names = { '1': 'GEMINI_API_KEY_1', '2': 'GEMINI_API_KEY_2', GEMINI_API_KEY: 'GEMINI_API_KEY', GEMINI_API_KEY_1: 'GEMINI_API_KEY_1', GEMINI_API_KEY_2: 'GEMINI_API_KEY_2' };
  const name = names[keySelector] || 'GEMINI_API_KEY_1'; const key = process.env[name];
  if (!key) throw new Error(`Set ${name} in .env before running the Hindi music vocal generator.`);
  return { name, key };
}

async function processTopic(url, contexts, ai, status) {
  const context = getContext(url, contexts); const targetDir = urlToDir(url); const indexPath = path.join(targetDir, 'index.html');
  if (!force && isHindiGeneratedPage(indexPath)) { console.log(`Skipped ${url} (Hindi page already generated; use --force to regenerate)`); return; }
  console.log(`\nGenerating Hindi page: ${url} — ${context.topicName}`); status[url] = { status: 'generating', model: MODEL, key: keySelector, language: 'hi', startedAt: new Date().toISOString() }; writeStatus(status);
  const content = await generateJson(buildContentPrompt(context), ai, validateContent, 'Study notes'); context.sectionTitle = content.section_title_hi; console.log(`  ✓ notes: ${content.concepts.length} अवधारणाएँ`);
  if (gapMs) await new Promise((resolve) => setTimeout(resolve, gapMs));
  const questions = await generateJson(buildQuestionsPrompt(context, content), ai, (data) => validateQuestions(data, content.concepts.map((item) => item.id)), 'Quiz and test');
  console.log(`  ✓ quiz: ${questions.quiz_questions.length}; test: ${questions.topic_test.length}`);
  // Write the page after the final generation attempt. If validation still
  // fails, generateJson returns that last response intentionally for saving.
  const html = compileHtml(content, questions, context);
  fs.mkdirSync(targetDir, { recursive: true });
  fs.writeFileSync(indexPath, html, 'utf8');
  status[url] = { status: 'completed', model: MODEL, key: keySelector, language: 'hi', title: content.title, concepts: content.concepts.length, quizQuestions: questions.quiz_questions.length, testQuestions: 10, completedAt: new Date().toISOString() }; writeStatus(status);
  console.log(`  ✓ wrote ${indexPath}`);
}

async function main() {
  const contexts = readTrackerContexts(); const targets = resolveTargets(contexts); console.log(`Discovered ${targets.length} Music Vocal page(s). Language: Hindi. Model: ${MODEL}. Key: GEMINI_API_KEY_${keySelector === '1' ? '1' : keySelector}`);
  if (dryRun) { targets.forEach((url) => console.log(`${url} — ${getContext(url, contexts).topicName}`)); return; }
  const selected = chooseApiKey(); const ai = new GoogleGenAI({ apiKey: selected.key }); const status = readStatus();
  for (const url of targets) { try { await processTopic(url, contexts, ai, status); } catch (error) { status[url] = { status: 'failed', model: MODEL, key: selected.name, language: 'hi', error: error.message, failedAt: new Date().toISOString() }; writeStatus(status); console.error(`  ✗ ${url}: ${error.message}`); if (requestedTopic) throw error; } }
}

main().catch((error) => { console.error(`Generation failed: ${error.message}`); process.exitCode = 1; });
