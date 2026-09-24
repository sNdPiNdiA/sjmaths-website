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
import { jsonrepair } from 'jsonrepair';

const ROOT = process.cwd();
const SUBJECT_ROOT = path.join(ROOT, 'music-vocal');
const TRACKER_PATH = path.join(ROOT, 'up-pgt-music-vocal', 'index.html');
const STATUS_PATH = path.join(ROOT, 'content-generation-status-music-vocal-hi.json');
const MODEL = process.env.GEMINI_MODEL || 'gemini-3.5-flash-lite';
const QUESTION_TYPES = ['mcq', 'assertion_reason', 'true_false', 'fill_blank', 'match_following', 'case_based', 'short_answer'];

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

function writeStatus(status) { fs.writeFileSync(STATUS_PATH, `${JSON.stringify(status, null, 2)}\n`, 'utf8'); }

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

function parseJson(raw) {
  const cleaned = String(raw || '').trim().replace(/^```(?:json)?\s*/i, '').replace(/\s*```$/i, '').trim();
  try { return JSON.parse(cleaned); }
  catch (error) { try { return JSON.parse(jsonrepair(cleaned)); } catch { throw new Error(`Gemini JSON parse failed: ${error.message}`); } }
}

function requireText(value, label) { if (typeof value !== 'string' || !value.trim()) throw new Error(`${label} must be a non-empty string`); }

function validateContent(data) {
  if (!data || !Array.isArray(data.concepts) || data.concepts.length < 4 || data.concepts.length > 8) throw new Error('Content must contain 4–8 concepts');
  requireText(data.title, 'title'); requireText(data.section_title_hi, 'section_title_hi');
  if (!Array.isArray(data.introduction_points) || data.introduction_points.length < 4) throw new Error('Introduction needs at least 4 point-wise items');
  const ids = new Set();
  for (const [index, concept] of data.concepts.entries()) {
    requireText(concept.id, `concept ${index + 1} id`); requireText(concept.title, `concept ${index + 1} title`); requireText(concept.lead, `concept ${concept.id} lead`);
    if (ids.has(concept.id)) throw new Error(`Duplicate concept id: ${concept.id}`); ids.add(concept.id);
    for (const [field, minimum] of [['explanation_points', 5], ['key_points', 4], ['examples', 2], ['comparison_points', 2], ['common_misconceptions', 2], ['exam_focus_points', 3]]) {
      if (!Array.isArray(concept[field]) || concept[field].length < minimum) throw new Error(`Concept ${concept.id} needs ${minimum} ${field}`);
      concept[field].forEach((item, itemIndex) => requireText(item, `${concept.id}.${field}[${itemIndex}]`));
    }
  }
  const revision = data.revision;
  if (!revision || !Array.isArray(revision.concept_revisions) || revision.concept_revisions.length !== data.concepts.length) throw new Error('Revision needs one detailed entry for every concept');
  const revisionIds = new Set();
  revision.concept_revisions.forEach((item) => {
    requireText(item.concept_id, 'revision concept_id'); requireText(item.title, `revision ${item.concept_id} title`);
    if (!ids.has(item.concept_id) || revisionIds.has(item.concept_id)) throw new Error(`Invalid or duplicate revision concept: ${item.concept_id}`);
    revisionIds.add(item.concept_id);
    for (const [field, minimum] of [['definition_points', 3], ['must_remember', 5], ['exam_traps', 2]]) {
      if (!Array.isArray(item[field]) || item[field].length < minimum) throw new Error(`Revision ${item.concept_id} needs ${minimum} ${field}`);
      item[field].forEach((point, pointIndex) => requireText(point, `revision ${item.concept_id}.${field}[${pointIndex}]`));
    }
  });
  if (!Array.isArray(revision.quick_facts) || revision.quick_facts.length < 5) throw new Error('Revision needs 5 quick facts');
  if (!Array.isArray(revision.glossary) || revision.glossary.length < 4) throw new Error('Revision needs 4 glossary items');
  if (!Array.isArray(revision.comparisons) || revision.comparisons.length < 1) throw new Error('Revision needs comparisons');
  if (!Array.isArray(revision.memory_hooks) || revision.memory_hooks.length < 3) throw new Error('Revision needs memory hooks');
  if (!Array.isArray(revision.exam_traps) || revision.exam_traps.length < 4) throw new Error('Revision needs exam traps');
  return data;
}

function validateQuestion(question, label, allowShort = true) {
  requireText(question.id, `${label}.id`); requireText(question.concept_id, `${label}.concept_id`); requireText(question.type, `${label}.type`); requireText(question.question, `${label}.question`); requireText(question.explanation, `${label}.explanation`);
  if (!QUESTION_TYPES.includes(question.type)) throw new Error(`${label} has invalid type ${question.type}`);
  if (question.type === 'fill_blank') {
    if (!Array.isArray(question.accepted_answers) || !question.accepted_answers.length) throw new Error(`${label} needs accepted_answers`);
  } else if (question.type === 'short_answer') {
    if (!allowShort) throw new Error(`${label} cannot be short_answer`); requireText(question.expected_answer, `${label}.expected_answer`);
  } else if (!Array.isArray(question.options) || question.options.length < 2 || !Number.isInteger(question.correct_index) || question.correct_index < 0 || question.correct_index >= question.options.length) {
    throw new Error(`${label} needs valid options and correct_index`);
  }
}

function validateQuestions(data, conceptIds) {
  if (!data || !Array.isArray(data.quiz_questions) || data.quiz_questions.length < conceptIds.length * QUESTION_TYPES.length) throw new Error('Quiz does not cover every question type for every concept');
  if (!Array.isArray(data.topic_test) || data.topic_test.length !== 10) throw new Error('Topic test must contain exactly 10 questions');
  const coverage = new Map(conceptIds.map((id) => [id, new Set()]));
  data.quiz_questions.forEach((question, index) => { validateQuestion(question, `quiz ${index + 1}`); if (!coverage.has(question.concept_id)) throw new Error(`Quiz references unknown concept ${question.concept_id}`); coverage.get(question.concept_id).add(question.type); });
  for (const [id, types] of coverage) { const missing = QUESTION_TYPES.filter((type) => !types.has(type)); if (missing.length) throw new Error(`Concept ${id} is missing: ${missing.join(', ')}`); }
  data.topic_test.forEach((question, index) => { if (!['mcq', 'assertion_reason', 'match_following', 'case_based'].includes(question.type)) throw new Error(`Test ${index + 1} must be objective`); validateQuestion(question, `test ${index + 1}`, false); if (!conceptIds.includes(question.concept_id)) throw new Error(`Test references unknown concept ${question.concept_id}`); });
  return data;
}

function buildContentPrompt(context) {
  return `आप UP PGT Music Vocal (Sangeet Gayan) के वरिष्ठ शिक्षक और परीक्षा-विशेषज्ञ हैं।
विषय: "${context.topicName}"
पाठ्यक्रम खंड: "${context.sectionTitle}"

इस विषय पर सटीक, परीक्षा-उपयोगी, point-wise हिन्दी (देवनागरी) सामग्री तैयार करें। संगीत के आवश्यक technical terms के बाद English term कोष्ठक में दे सकते हैं। लंबे अनुच्छेद न लिखें। हर concept को अलग रखें और विषय के सभी उप-विषयों को कवर करें। कलाकार, राग, ग्रंथ, काल या ऐतिहासिक तथ्य तभी दें जब वे विश्वसनीय और विषय से सीधे संबंधित हों।

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

async function generateJson(prompt, ai, validator, label, maxAttempts = 5) {
  let activePrompt = prompt; let lastError;
  for (let attempt = 1; attempt <= maxAttempts; attempt += 1) {
    try {
      const response = await ai.models.generateContent({ model: MODEL, contents: activePrompt, config: { temperature: 0.25, responseMimeType: 'application/json' } });
      if (!response?.text) throw new Error('Gemini returned an empty response');
      const data = parseJson(response.text);
      try { validator(data); } catch (validationError) { const error = new Error(`${label} validation failed: ${validationError.message}`); error.isValidationError = true; throw error; }
      return data;
    } catch (error) {
      lastError = error;
      const status = Number(error?.status || error?.code || error?.error?.code || error?.response?.status) || null;
      if ([400, 401, 403].includes(status)) throw error;
      if (attempt < maxAttempts) {
        const validation = error.isValidationError === true;
        const waitMs = validation ? Math.min(8000, attempt * 2000) : status === 429 ? 65000 : Math.min(60000, 8000 * (2 ** (attempt - 1)));
        if (validation) activePrompt = `${prompt}\n\nपिछला JSON validation error के कारण अस्वीकार हुआ: ${error.message}\nसभी fields और minimum point counts रखते हुए corrected JSON लौटाएँ।`;
        console.warn(`${label} attempt ${attempt} failed (${status || error.message}); retrying in ${Math.round(waitMs / 1000)}s.`);
        await new Promise((resolve) => setTimeout(resolve, waitMs));
      }
    }
  }
  throw lastError;
}

function escapeHtml(value) { return String(value ?? '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;').replace(/'/g, '&#39;'); }
function inlineText(value) { return escapeHtml(value).replace(/\n/g, '<br>'); }
function list(items, className = '') { return `<ul${className ? ` class="${className}"` : ''}>${(items || []).map((item) => `<li>${inlineText(item)}</li>`).join('')}</ul>`; }
function safeJson(data) { return JSON.stringify(data).replace(/</g, '\\u003c').replace(/>/g, '\\u003e').replace(/&/g, '\\u0026'); }

function renderConcepts(content) {
  return content.concepts.map((concept, index) => `<section class="notes-section" id="concept-${escapeHtml(concept.id)}"><div class="concept-number">अवधारणा ${index + 1}</div><h2>${escapeHtml(concept.title)}</h2><p class="lead-concept">${inlineText(concept.lead)}</p><h3>व्याख्या</h3>${list(concept.explanation_points)}<h3>मुख्य बिंदु</h3>${list(concept.key_points)}<div class="callout example"><strong>उदाहरण / प्रयोग:</strong>${list(concept.examples)}</div><div class="callout comparison"><strong>तुलना:</strong>${list(concept.comparison_points)}</div><div class="callout trap"><strong>सामान्य भ्रांतियाँ:</strong>${list(concept.common_misconceptions)}</div><div class="callout exam"><strong>परीक्षा-केंद्रित बिंदु:</strong>${list(concept.exam_focus_points)}</div></section>`).join('\n');
}

function renderRevision(revision, title) {
  const conceptRevisions = revision.concept_revisions.map((item, index) => `<section class="revision-box"><div class="concept-number">अवधारणा ${index + 1}</div><h2>${escapeHtml(item.title)}</h2><h3>परिभाषा और क्षेत्र</h3>${list(item.definition_points)}<h3>अवश्य याद रखें</h3>${list(item.must_remember)}<h3>परीक्षा-जाल</h3>${list(item.exam_traps)}</section>`).join('');
  const glossary = revision.glossary.map((item) => `<div class="glossary-item"><strong>${escapeHtml(item.term)}</strong><span>${inlineText(item.definition)}</span></div>`).join('');
  const comparisons = revision.comparisons.map((item) => `<div class="comparison-row"><strong>${escapeHtml(item.left)}</strong><span>बनाम</span><strong>${escapeHtml(item.right)}</strong>${list(item.difference_points)}</div>`).join('');
  return `<div class="summary-intro"><h2>${escapeHtml(title)} — त्वरित पुनरावृत्ति</h2><p>हर अवधारणा के सूक्ष्म बिंदु दोहराएँ और फिर विषय परीक्षा दें।</p></div>${conceptRevisions}<section class="revision-box"><h2>त्वरित तथ्य</h2>${list(revision.quick_facts)}</section><section class="revision-box"><h2>शब्दावली</h2><div class="glossary-grid">${glossary}</div></section><section class="revision-box"><h2>महत्वपूर्ण अंतर</h2>${comparisons}</section><section class="revision-box"><h2>स्मृति-सहायक बिंदु</h2>${list(revision.memory_hooks)}</section><section class="revision-box"><h2>परीक्षा सावधानियाँ</h2>${list(revision.exam_traps)}</section>`;
}

function questionData(question) {
  const accepted = (question.accepted_answers || []).map((answer) => `<span class="accepted-answer">${inlineText(answer)}</span>`).join('');
  const expected = question.expected_answer ? `<span class="expected-answer">${inlineText(question.expected_answer)}</span>` : '';
  return `<div class="question-source-data" aria-hidden="true">${accepted}${expected}<p class="question-explanation">${inlineText(question.explanation)}</p></div>`;
}

function renderQuizQuestion(question, index) {
  const typeNames = { mcq: 'बहुविकल्पीय', assertion_reason: 'कथन–कारण', true_false: 'सही / गलत', fill_blank: 'रिक्त स्थान', match_following: 'मिलान', case_based: 'परिस्थिति-आधारित', short_answer: 'लघु उत्तर' };
  const letters = ['A', 'B', 'C', 'D', 'E']; let body;
  if (question.type === 'fill_blank') body = `<input class="answer-input" id="quiz-input-${index}" aria-label="उत्तर लिखें"><button class="check-btn" data-fill="${index}">उत्तर जाँचें</button>`;
  else if (question.type === 'short_answer') body = `<textarea class="answer-input" id="quiz-input-${index}" aria-label="उत्तर लिखें"></textarea><button class="check-btn" data-short="${index}">उत्तर देखें</button>`;
  else body = `<div class="options">${question.options.map((option, optionIndex) => `<button type="button" class="option" data-quiz="${index}" data-option="${optionIndex}"><b>${letters[optionIndex]}</b>${inlineText(option)}</button>`).join('')}</div>`;
  const correct = Number.isInteger(question.correct_index) ? ` data-correct="${question.correct_index}"` : '';
  return `<article class="question" data-index="${index}"${correct}><div><span class="question-number">प्रश्न ${index + 1}</span><span class="question-type">${escapeHtml(typeNames[question.type] || question.type)}</span></div><p>${inlineText(question.question)}</p>${body}${questionData(question)}<div id="quiz-feedback-${index}"></div></article>`;
}

function renderTestQuestion(question, index) {
  const letters = ['A', 'B', 'C', 'D', 'E'];
  return `<article class="question test-question" data-index="${index}" data-correct="${question.correct_index}"><div><span class="question-number">प्रश्न ${index + 1}</span><span class="question-type">विषय परीक्षा</span></div><p>${inlineText(question.question)}</p><div class="options">${question.options.map((option, optionIndex) => `<button type="button" class="option" data-test="${index}" data-option="${optionIndex}"><b>${letters[optionIndex]}</b>${inlineText(option)}</button>`).join('')}</div>${questionData(question)}<div id="test-feedback-${index}"></div></article>`;
}

function compileHtml(content, questions, context) {
  const canonical = `https://sjmaths.com${context.url}`;
  const title = content.short_title || context.topicName;
  const description = `${title}: Music Vocal के लिए हिन्दी अध्ययन नोट्स, अवधारणा क्विज़, पुनरावृत्ति सारांश और विषय परीक्षा।`;
  return `<!doctype html><html lang="hi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>${escapeHtml(content.title)} | संगीत गायन | SJ Maths</title><meta name="description" content="${escapeHtml(description)}"><meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1"><meta name="author" content="SJ Maths"><link rel="canonical" href="${canonical}"><meta property="og:type" content="article"><meta property="og:site_name" content="SJ Maths"><meta property="og:title" content="${escapeHtml(content.title)} | संगीत गायन"><meta property="og:description" content="${escapeHtml(description)}"><meta property="og:url" content="${canonical}"><script type="application/ld+json">${safeJson({ '@context': 'https://schema.org', '@type': 'LearningResource', name: content.title, headline: content.title, description, url: canonical, inLanguage: 'hi', educationalLevel: 'UP TGT', learningResourceType: 'Study guide', isPartOf: { '@type': 'WebSite', name: 'SJ Maths', url: 'https://sjmaths.com/' } })}</script><style>:root{--brand:#16324f;--accent:#0f766e;--soft:#ecfdf5;--ink:#182238;--muted:#64748b;--line:#dbe4ec;--paper:#fff;--bg:#f6f8fb}*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font-family:"Noto Sans Devanagari",Mangal,Arial,sans-serif;line-height:1.65}.wrap{width:min(1160px,calc(100% - 28px));margin:auto}.site-header{position:sticky;top:0;z-index:5;background:#ffffffef;border-bottom:1px solid var(--line);padding:12px 0}.header-inner{display:flex;justify-content:space-between;gap:12px;align-items:center}.brand{font-weight:900;color:var(--brand)}.brand small{display:block;color:var(--muted);font-weight:600}.back{color:var(--brand);font-size:.85rem}.hero{padding:28px 0 20px}.breadcrumb{color:var(--muted);font-size:.8rem}.hero h1{color:var(--brand);line-height:1.3}.lead{color:#475569}.tabs{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;position:sticky;top:65px;z-index:4;background:var(--bg);padding:10px 0}.tab{border:1px solid var(--line);background:var(--paper);padding:12px 8px;border-radius:9px;font-weight:800;color:var(--brand);cursor:pointer}.tab.active{background:var(--brand);color:#fff}.panel{background:var(--paper);border:1px solid var(--line);border-radius:12px;padding:20px;margin:12px 0}.hidden{display:none!important}.notes-section,.revision-box{border-top:3px solid var(--accent);padding:18px 0}.notes-section h2,.revision-box h2{color:var(--brand)}h3{color:var(--accent)}ul{padding-left:24px}.callout{padding:12px 15px;margin:14px 0;border-left:4px solid var(--accent);background:var(--soft);border-radius:6px}.callout.trap{background:#fff7ed;border-color:#c2410c}.callout.exam{background:#eff6ff;border-color:#2563eb}.summary-intro{background:var(--soft);padding:16px;border-radius:9px}.glossary-grid{display:grid;gap:10px}.glossary-item{display:flex;gap:10px;border-bottom:1px solid var(--line);padding:8px 0}.comparison-row{padding:12px;border:1px solid var(--line);border-radius:8px;margin:10px 0}.comparison-row span{margin:0 8px;color:var(--muted)}.question{border:1px solid var(--line);border-radius:10px;padding:16px;margin:14px 0;background:#fff}.question-number,.question-type{display:inline-block;margin-right:8px;color:var(--accent);font-weight:900}.question-type{font-size:.78rem;background:var(--soft);padding:3px 8px;border-radius:999px}.options{display:grid;gap:8px}.option{display:flex;gap:10px;text-align:left;padding:11px;border:1px solid var(--line);border-radius:7px;background:#fff;cursor:pointer;font:inherit}.option:hover{border-color:var(--accent)}.option b{color:var(--accent)}.answer-input{width:100%;padding:11px;border:1px solid var(--line);border-radius:7px;font:inherit;margin:6px 0;min-height:46px}.check-btn,.submit{background:var(--brand);color:#fff;border:0;border-radius:7px;padding:10px 14px;font-weight:800;cursor:pointer}.feedback{margin-top:10px}.source{display:none}.result{padding:16px;background:var(--soft);border-radius:9px;margin-top:14px}@media(max-width:700px){.tabs{grid-template-columns:repeat(2,1fr);top:58px}.tab{font-size:.78rem}.header-inner{align-items:flex-start;flex-direction:column}}</style></head><body><header class="site-header"><div class="wrap header-inner"><div class="brand">SJ Maths <small>संगीत गायन</small></div><a class="back" href="/up-pgt-music-vocal/">← UP TGT Music Vocal</a></div></header><main class="wrap"><section class="hero"><div class="breadcrumb"><a href="https://sjmaths.com/">मुख्य पृष्ठ</a> › <a href="/up-pgt-music-vocal/">संगीत गायन</a> › ${escapeHtml(context.sectionTitle)}</div><h1>${escapeHtml(content.title)}</h1><p class="lead">${escapeHtml(content.introduction_points[0])}</p><p>${content.concepts.length} अवधारणाएँ · ${questions.quiz_questions.length} क्विज़ प्रश्न · 10 विषय परीक्षा प्रश्न</p></section><nav class="tabs" role="tablist"><button class="tab active" data-tab="notes">अध्ययन नोट्स</button><button class="tab" data-tab="quiz">अवधारणा क्विज़</button><button class="tab" data-tab="revision">पुनरावृत्ति सारांश</button><button class="tab" data-tab="test">विषय परीक्षा</button></nav><article class="panel" id="notes"><h2>विषय का संक्षिप्त परिचय</h2>${list(content.introduction_points)}${renderConcepts(content)}</article><article class="panel hidden" id="quiz"><h2>अवधारणा क्विज़</h2><p>हर अवधारणा पर सात प्रकार के हिन्दी प्रश्न।</p>${questions.quiz_questions.map(renderQuizQuestion).join('')}</article><article class="panel hidden" id="revision"><h2>मिनट-रिविज़न</h2>${renderRevision(content.revision,title)}</article><article class="panel hidden" id="test"><h2>10 प्रश्नों की विषय परीक्षा</h2><p>टैब खोलते ही 10 मिनट की समय-सीमा शुरू होगी।</p>${questions.topic_test.map(renderTestQuestion).join('')}<button class="submit" id="submit-test">परीक्षा जमा करें</button><div class="result hidden" id="test-result"></div></article></main><script type="application/json" id="quiz-data">${safeJson(questions.quiz_questions)}</script><script type="application/json" id="test-data">${safeJson(questions.topic_test)}</script><script>document.addEventListener('DOMContentLoaded',()=>{const esc=v=>String(v??'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#39;');const quiz=JSON.parse(document.getElementById('quiz-data').textContent);const test=JSON.parse(document.getElementById('test-data').textContent);let quizScore=0;const answered=new Set();const feedback=(card,ok,text)=>{const box=card.querySelector('[id^="quiz-feedback"], [id^="test-feedback"]');if(box)box.innerHTML='<div class="feedback"><strong>'+(ok?'✓ सही':'✕ पुनः देखें')+'</strong><p>'+esc(text)+'</p></div>'};document.querySelectorAll('[data-quiz]').forEach(btn=>btn.addEventListener('click',()=>{const card=btn.closest('.question');const i=Number(card.dataset.index);if(answered.has('q'+i))return;answered.add('q'+i);const chosen=Number(btn.dataset.option);const correct=Number(card.dataset.correct);card.querySelectorAll('.option').forEach((x,n)=>{x.disabled=true;if(n===correct)x.style.borderColor='#15803d';if(n===chosen&&chosen!==correct)x.style.borderColor='#dc2626'});if(chosen===correct)quizScore++;feedback(card,chosen===correct,card.querySelector('.question-explanation')?.textContent||'');}));document.querySelectorAll('[data-fill]').forEach(btn=>btn.addEventListener('click',()=>{const card=btn.closest('.question');const i=Number(card.dataset.index);if(answered.has('q'+i))return;answered.add('q'+i);const value=document.getElementById('quiz-input-'+i).value.trim().toLowerCase();const accepted=[...card.querySelectorAll('.accepted-answer')].map(x=>x.textContent.trim().toLowerCase());feedback(card,accepted.includes(value),'स्वीकृत उत्तर: '+accepted.join(', ')+'। '+(card.querySelector('.question-explanation')?.textContent||''));}));document.querySelectorAll('[data-short]').forEach(btn=>btn.addEventListener('click',()=>{const card=btn.closest('.question');const i=Number(card.dataset.index);if(answered.has('q'+i))return;answered.add('q'+i);feedback(card,false,'अपेक्षित उत्तर: '+(card.querySelector('.expected-answer')?.textContent||'')+'।');}));let selected={};let submitted=false;document.querySelectorAll('[data-test]').forEach(btn=>btn.addEventListener('click',()=>{if(submitted)return;const card=btn.closest('.test-question');selected[card.dataset.index]=Number(btn.dataset.option);card.querySelectorAll('.option').forEach(x=>x.classList.remove('selected'));btn.classList.add('selected')}));document.getElementById('submit-test').addEventListener('click',()=>{if(submitted)return;submitted=true;let score=0;document.querySelectorAll('.test-question').forEach(card=>{const i=card.dataset.index;const answer=selected[i];const correct=Number(card.dataset.correct);if(answer===correct)score++;card.querySelectorAll('.option').forEach((x,n)=>{x.disabled=true;if(n===correct)x.style.borderColor='#15803d';if(n===answer&&answer!==correct)x.style.borderColor='#dc2626'});feedback(card,answer===correct,card.querySelector('.question-explanation')?.textContent||'')});const result=document.getElementById('test-result');result.classList.remove('hidden');result.textContent='आपका परिणाम: '+score+' / '+test.length;});let timer;let remaining=600;function startTimer(){if(timer)return;timer=setInterval(()=>{remaining--;if(remaining<=0){clearInterval(timer);document.getElementById('submit-test').click()}},1000)};document.querySelectorAll('.tab').forEach(tab=>tab.addEventListener('click',()=>{document.querySelectorAll('.tab').forEach(x=>x.classList.remove('active'));document.querySelectorAll('.panel').forEach(x=>x.classList.add('hidden'));tab.classList.add('active');document.getElementById(tab.dataset.tab).classList.remove('hidden');if(tab.dataset.tab==='test')startTimer()}))});</script></body></html>`;
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
  console.log(`  ✓ quiz: ${questions.quiz_questions.length}; test: ${questions.topic_test.length}`); fs.mkdirSync(targetDir, { recursive: true });
  fs.writeFileSync(indexPath, compileHtml(content, questions, context), 'utf8');
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
