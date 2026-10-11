import crypto from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';
import { createRequire } from 'node:module';

const require = createRequire(import.meta.url);
const { parse } = require('./seo-html.cjs');
const ROOT = process.cwd();
const HUB_PATH = path.join(ROOT, 'up-assistant-teacher/index.html');
const ENGLISH_MODEL = 'gemini-3.5-flash-lite';
const HINDI_MODEL = 'gemini-3.1-flash-lite';
const REQUEST_GAP_MS = 13000;
const MAX_RETRY_DELAY_MS = 60000;
const START_RETRY_DELAY_MS = 5000;
const PRERENDER_SCRIPT = path.join(ROOT, 'scripts/prerender-seo-content.cjs');
const KEY_NAMES = ['GEMINI_API_KEY_1', 'GEMINI_API_KEY_2', 'GEMINI_API_KEY', 'GOOGLE_API_KEY'];
const lastRequestAt = new Map();
let nextKey = 0;

function loadDotEnv() {
  const envPath = path.join(ROOT, '.env');
  if (!fs.existsSync(envPath)) return;
  for (const line of fs.readFileSync(envPath, 'utf8').split(/\r?\n/)) {
    const match = line.match(/^\s*([\w.-]+)\s*=\s*(.*)?\s*$/);
    if (!match || process.env[match[1]]) continue;
    let value = (match[2] || '').trim();
    if ((value.startsWith('"') && value.endsWith('"')) || (value.startsWith("'") && value.endsWith("'"))) value = value.slice(1, -1);
    process.env[match[1]] = value;
  }
}

function getApiKeys() {
  const seen = new Set();
  return KEY_NAMES.flatMap(name => {
    const value = process.env[name]?.trim();
    if (!value || seen.has(value)) return [];
    seen.add(value);
    return [{ name, value }];
  });
}

function getOptions() {
  const dryRun = process.argv.includes('--dry-run');
  const limitArg = process.argv.find(arg => /^--limit=\d+$/.test(arg));
  return { dryRun, limit: limitArg ? Number(limitArg.split('=')[1]) : Infinity };
}

function readPageData(html, file) {
  const match = html.match(/<script\b(?=[^>]*\bid=["']upsc-page-data["'])[^>]*>([\s\S]*?)<\/script>/i);
  if (!match) throw new Error(`Missing upsc-page-data in ${path.relative(ROOT, file)}`);
  return JSON.parse(match[1]);
}

function writePageData(html, data, file) {
  const pattern = /(<script\b(?=[^>]*\bid=["']upsc-page-data["'])[^>]*>)[\s\S]*?(<\/script>)/i;
  if (!pattern.test(html)) throw new Error(`Missing upsc-page-data in ${path.relative(ROOT, file)}`);
  const serialized = JSON.stringify(data, null, 2).replace(/</g, '\\u003c');
  return html.replace(pattern, `$1\n${serialized}\n$2`);
}

function hasPlaceholder(data) {
  return /content under preparation|study resources for this microtopic are being compiled|check back soon for complete concept notes/i
    .test(JSON.stringify(data?.concepts ?? data));
}

function extractTargets() {
  const $ = parse(fs.readFileSync(HUB_PATH, 'utf8'));
  const targets = [];
  $('li.syllabus-item').each((_, item) => {
    const link = $(item).find('a[href]').first();
    const href = link.attr('href');
    if (!href?.startsWith('/up-assistant-teacher/')) return;
    const dir = href.replace(/^\//, '').replace(/\/$/, '');
    const file = path.join(ROOT, dir, 'index.html');
    if (!fs.existsSync(file)) throw new Error(`Tracker link has no page: ${href}`);
    const html = fs.readFileSync(file, 'utf8');
    if (!/<script\b(?=[^>]*\bid=["']upsc-page-data["'])[^>]*>/i.test(html)) {
      if (/content under preparation|check back soon for comprehensive notes/i.test(html)) {
        throw new Error(`Placeholder page uses an unsupported content shell: ${href}`);
      }
      return;
    }
    const data = readPageData(html, file);
    if (hasPlaceholder(data)) {
      targets.push({ dir, file, href, topicName: data.topicName, hindiName: data.hindiName, subject: data.subject });
    }
  });
  return targets;
}

function countTextLeaves(value) {
  if (typeof value === 'string') return 1;
  if (Array.isArray(value)) return value.reduce((sum, item) => sum + countTextLeaves(item), 0);
  if (value && typeof value === 'object') return Object.values(value).reduce((sum, item) => sum + countTextLeaves(item), 0);
  return 0;
}

function validateEnglishNotes(value, topic) {
  if (!value || !Array.isArray(value.sections) || value.sections.length < 6) throw new Error('English response needs at least six structured sections.');
  if (!Array.isArray(value.upscNotes) || value.upscNotes.length < 4) throw new Error('English response needs at least four exam tips or traps.');
  if (!Array.isArray(value.keyTakeaways) || value.keyTakeaways.length < 5) throw new Error('English response needs at least five key takeaways.');
  if (value.sections.some(section => !section || !['table', 'list', 'subcards'].includes(section.type))) throw new Error('English response contains an unsupported or paragraph section.');
  if (!value.sections.some(section => /mind\s*map/i.test(section.title || '') && section.type === 'list')) throw new Error('English response is missing the point-wise mind map.');
  if (!value.sections.some(section => section.type === 'subcards')) throw new Error('English response is missing structured concept notes.');
  if (!value.sections.some(section => section.type === 'table')) throw new Error('English response is missing a comparison or facts table.');
  if (countTextLeaves(value) < 100) throw new Error('English response is too short for complete topic coverage.');
  const serialized = JSON.stringify(value);
  if (hasPlaceholder({ concepts: value })) throw new Error('English response contains placeholder wording.');
  if (serialized.toLowerCase().includes('lorem ipsum')) throw new Error('English response contains filler text.');
  if (!topic.topicName || !topic.subject) throw new Error('Page metadata is missing a topic or subject name.');
}

function validateBilingualShape(english, bilingual, at = '$') {
  if (typeof english === 'string') {
    if (at.endsWith('.type')) {
      if (bilingual !== english) throw new Error(`Structural value changed at ${at}.`);
      return;
    }
    if (!bilingual || typeof bilingual !== 'object' || Array.isArray(bilingual)) throw new Error(`Missing bilingual text object at ${at}.`);
    if (Object.keys(bilingual).sort().join(',') !== 'en,hi') throw new Error(`Unexpected bilingual fields at ${at}.`);
    if (bilingual.en !== english) throw new Error(`English source text changed at ${at}.`);
    if (typeof bilingual.hi !== 'string' || !/[\u0900-\u097f]/.test(bilingual.hi)) throw new Error(`Hindi translation is missing Devanagari text at ${at}.`);
    return;
  }
  if (Array.isArray(english)) {
    if (!Array.isArray(bilingual) || bilingual.length !== english.length) throw new Error(`Array structure changed at ${at}.`);
    english.forEach((item, index) => validateBilingualShape(item, bilingual[index], `${at}[${index}]`));
    return;
  }
  if (english && typeof english === 'object') {
    if (!bilingual || typeof bilingual !== 'object' || Array.isArray(bilingual)) throw new Error(`Object structure changed at ${at}.`);
    const a = Object.keys(english).sort();
    const b = Object.keys(bilingual).sort();
    if (a.join(',') !== b.join(',')) throw new Error(`Object keys changed at ${at}.`);
    for (const key of Object.keys(english)) validateBilingualShape(english[key], bilingual[key], `${at}.${key}`);
  }
}

function parseModelJson(raw) {
  const text = String(raw || '').trim().replace(/^```(?:json)?\s*/i, '').replace(/\s*```$/, '');
  return JSON.parse(text);
}

function makeEnglishPrompt(topic) {
  return `You are an experienced UP Assistant Teacher exam educator. Create comprehensive, point-wise study notes for this syllabus microtopic.

TOPIC: ${topic.topicName} (${topic.hindiName || ''})
SUBJECT: ${topic.subject}
EXAM: UP Assistant Teacher Recruitment Examination, Uttar Pradesh
CURRENT DATE: 11 October 2026

Coverage rules:
- Cover the full topic, its standard subtopics, definitions, classifications, processes, examples, Indian/UP context, and exam-relevant distinctions. Expand or reduce the concept count as the topic requires; never omit a relevant subtopic to meet a fixed number.
- Use short bullets, tables, formulas, and structured subcards. Do not write long paragraphs.
- Include a point-wise mind map, useful mnemonics/tricks, common traps, exam tips, and a final revision list.
- Keep facts, dates, formulas, and terminology accurate. For current-affairs categories, date any time-sensitive examples, do not invent winners or appointments, and separate stable background from facts that need a latest official update.
- Avoid unsupported claims about the exact exam frequency. Keep the level appropriate to the supplied syllabus and D.El.Ed./Class 12 standard.

Return ONLY valid JSON, with English strings only and exactly this shape:
{
  "sections": [
    {"title":"Detailed Brief Overview","type":"table","headers":["Aspect","Key details"],"rows":[["...","..."]] },
    {"title":"Mind Map","type":"list","items":[{"term":"Branch","definition":"Child concepts joined with arrows; concise."}]},
    {"title":"Concepts and Theories","type":"subcards","items":[{"title":"Concept","content":"• Point one\\n• Point two\\n• Example: ..."}]},
    {"title":"Important Facts and Comparisons","type":"table","headers":["Concept","Key point","Exam distinction"],"rows":[["...","...","..."]] },
    {"title":"Tricks to Remember","type":"list","items":[{"term":"Mnemonic or trick","definition":"How it helps recall the correct facts."}]},
    {"title":"Mistakes to Avoid","type":"list","items":[{"term":"Common confusion","definition":"Correct distinction in one or two short points."}]},
    {"title":"Point-wise Detailed Summary","type":"list","items":[{"term":"Key point","definition":"Concise revision fact."}]}
  ],
  "upscNotes": [
    {"type":"tip","content":"Exam strategy tip."},
    {"type":"trap","content":"Common exam trap."}
  ],
  "keyTakeaways": ["High-yield fact"]
}

Make the overview table about 8–12 rows, the mind map broad enough to represent the topic, and the concept cards as many as needed for complete coverage. Use 4–8 trick and mistake items, at least four tips/traps total, and enough summary points to cover the full topic. Include no nulls, placeholders, markdown fences, or prose outside the JSON.`;
}

function makeHindiPrompt(english) {
  return `Translate the learner-facing English text in this JSON into clear, natural Hindi in Devanagari for an Indian exam-preparation page.

Rules:
- Preserve every key, array length, array order, section type, number, formula, date, acronym, and English source string exactly.
- For every learner-facing string, return an object with exactly two fields: {"en":"the exact original string","hi":"its complete Hindi translation"}.
- Keep structural values such as section "type" and note "type" as their original plain strings. Do not translate those values.
- Translate headings, table headers and cells, terms, definitions, bullets, tips, traps, and takeaways. Preserve mnemonics in English and explain their meaning in Hindi.
- Every Hindi value must contain Devanagari text; retain technical terms/formulas in parentheses where useful.
- Return only valid JSON. Do not add or remove content, shorten lists, summarize, or add commentary.

ENGLISH JSON:
${JSON.stringify(english)}`;
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function enforceSpacing(model) {
  const previous = lastRequestAt.get(model);
  if (previous) {
    const remaining = REQUEST_GAP_MS - (Date.now() - previous);
    if (remaining > 0) await sleep(remaining);
  }
  lastRequestAt.set(model, Date.now());
}

async function callModel(model, prompt) {
  const keys = getApiKeys();
  if (!keys.length) throw new Error('No Gemini API key is configured in the environment or .env.');
  await enforceSpacing(model);
  const start = nextKey++ % keys.length;
  const failures = [];
  for (let offset = 0; offset < keys.length; offset++) {
    const key = keys[(start + offset) % keys.length];
    let response;
    try {
      response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent?key=${encodeURIComponent(key.value)}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          contents: [{ parts: [{ text: prompt }] }],
          generationConfig: { responseMimeType: 'application/json', temperature: 0.35, maxOutputTokens: 32768 }
        }),
        signal: AbortSignal.timeout(120000)
      });
    } catch (error) {
      failures.push(`${key.name}: ${error.message}`);
      continue;
    }
    if (response.ok) {
      const payload = await response.json();
      const text = payload?.candidates?.[0]?.content?.parts?.map(part => part.text || '').join('').trim();
      if (!text) throw new Error(`${model} returned no text (finishReason: ${payload?.candidates?.[0]?.finishReason || 'unknown'}).`);
      return text;
    }
    const body = (await response.text()).slice(0, 350);
    failures.push(`${key.name}: HTTP ${response.status} ${body}`);
  }
  const error = new Error(`${model} request failed for all configured keys: ${failures.join(' | ')}`);
  error.retryable = failures.some(item => /HTTP (403|408|429|5\d\d)|fetch failed|timeout|ECONNRESET|ENOTFOUND/i.test(item));
  throw error;
}

async function retryForever(label, operation) {
  let delay = START_RETRY_DELAY_MS;
  let attempt = 0;
  while (true) {
    attempt++;
    try {
      return await operation();
    } catch (error) {
      if (error.retryable === false) throw error;
      console.error(`  ${label} failed on attempt ${attempt}: ${error.message}`);
      console.log(`  Retrying in ${Math.round(delay / 1000)} seconds. Press Ctrl+C to stop.`);
      await sleep(delay);
      delay = Math.min(delay * 2, MAX_RETRY_DELAY_MS);
    }
  }
}

function updateEmbeddedData(html, data) {
  const pattern = /(<script\b(?=[^>]*\bid=["']upsc-page-data["'])[^>]*>)[\s\S]*?(<\/script>)/i;
  if (!pattern.test(html)) throw new Error('Page is missing the embedded upsc-page-data block.');
  const serialized = JSON.stringify(data, null, 2).replace(/</g, '\\u003c');
  return html.replace(pattern, (_, open, close) => `${open}\n${serialized}\n${close}`);
}

function prerenderOne(dir) {
  execFileSync(process.execPath, [PRERENDER_SCRIPT, `--scope=${dir.replace(/\\/g, '/')}`], { cwd: ROOT, stdio: 'inherit' });
  const file = path.join(ROOT, dir, 'index.html');
  const html = fs.readFileSync(file, 'utf8');
  const $ = parse(html);
  const text = $('#topic-content').text().trim();
  if (text.length < 400 || hasPlaceholder({ concepts: text })) throw new Error(`Prerender did not materialize complete notes in ${dir}.`);
}

async function generateTopic(topic) {
  console.log(`  Generating English notes for ${topic.topicName} (${topic.subject}).`);
  const english = await retryForever('English generation', async () => {
    const value = parseModelJson(await callModel(ENGLISH_MODEL, makeEnglishPrompt(topic)));
    validateEnglishNotes(value, topic);
    return value;
  });

  console.log(`  Translating the same notes to Hindi for ${topic.topicName}.`);
  const bilingual = await retryForever('Hindi translation and structure validation', async () => {
    const value = parseModelJson(await callModel(HINDI_MODEL, makeHindiPrompt(english)));
    validateBilingualShape(english, value);
    return value;
  });

  const html = fs.readFileSync(topic.file, 'utf8');
  const data = readPageData(html, topic.file);
  data.concepts = bilingual;
  data.version = { ...(data.version || {}), generator: 'up-assistant-bilingual-html-v1' };
  data.contentHash = `sha256-${crypto.createHash('sha256').update(JSON.stringify(bilingual)).digest('hex')}`;
  data.generatedAt = new Date().toISOString();
  fs.writeFileSync(topic.file, updateEmbeddedData(html, data), 'utf8');
  prerenderOne(topic.dir);
  console.log(`  Saved bilingual, crawlable notes to ${path.relative(ROOT, topic.file)}.`);
}

async function main() {
  loadDotEnv();
  const options = getOptions();
  const allTargets = extractTargets();
  const targets = allTargets.slice(0, options.limit);
  console.log(`Incomplete UP Assistant Teacher pages: ${allTargets.length}`);
  console.log(`Selected: ${targets.length}; English model: ${ENGLISH_MODEL}; Hindi model: ${HINDI_MODEL}; max retry wait: 60s.`);
  if (options.dryRun) {
    for (const topic of targets) console.log(`  [GENERATE] ${topic.subject}: ${topic.topicName} -> ${topic.href}`);
    console.log('Dry run complete; no files changed and no API calls made.');
    return;
  }
  if (!getApiKeys().length && targets.length) throw new Error('No Gemini API key is configured.');
  for (let index = 0; index < targets.length; index++) {
    const topic = targets[index];
    console.log(`[${index + 1}/${targets.length}] ${topic.topicName}`);
    await generateTopic(topic);
  }
  console.log(`Completed selected pages: ${targets.length}.`);
}

main().catch(error => {
  console.error(error.message);
  process.exitCode = 1;
});
