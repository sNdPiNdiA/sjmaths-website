#!/usr/bin/env node
/**
 * SJ Maths — Hindi Music Instrumental topic-page generator.
 *
 * Generates static, crawlable four-tab pages:
 *   1. अध्ययन नोट्स
 *   2. अवधारणा क्विज़
 *   3. पुनरावृत्ति सारांश
 *   4. विषय परीक्षा
 *
 * The default key is GEMINI_API_KEY. Use --key GEMINI_API_KEY_1/2, --topic, --all or --dry-run.
 */

import fs from 'node:fs';
import path from 'node:path';
import 'dotenv/config';
import { GoogleGenAI } from '@google/genai';
import { jsonrepair } from 'jsonrepair';

const ROOT = process.cwd();
const SUBJECT_ROOT = path.join(ROOT, 'music-instrumental');
const TRACKER_PATH = path.join(ROOT, 'up-pgt-music-instrumental', 'index.html');
const STATUS_PATH = path.join(ROOT, 'content-generation-status-music-instrumental-hi.json');
const MODEL = process.env.GEMINI_MODEL || 'gemini-3.6-flash';
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
const keySelector = argValue('--key') || 'GEMINI_API_KEY';

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
    const sectionTitle = stripTags(sectionHtml.match(/<span class="section-title">([\s\S]*?)<\/span>/i)?.[1] || 'Music Instrumental');
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
  else throw new Error('Choose --topic /music-instrumental/.../, --all, or --dry-run.');
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
      item[field].forEach((point, index) => requireText(point, `revision ${item.concept_id}.${field}[${index}]`));
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
  } else {
    if (!Array.isArray(question.options) || question.options.length < 2 || !Number.isInteger(question.correct_index) || question.correct_index < 0 || question.correct_index >= question.options.length) throw new Error(`${label} needs valid options and correct_index`);
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
  return `आप UP PGT Music Instrumental (Sangeet Vadan) के वरिष्ठ अध्यापक और परीक्षा-विशेषज्ञ हैं।
इस विषय के लिए अत्यंत सटीक, परीक्षा-उपयोगी सामग्री तैयार करें:
विषय: "${context.topicName}"
पाठ्यक्रम खंड: "${context.sectionTitle}"

कठोर नियम:
- पूरा उत्तर केवल वैध JSON में दें; Markdown या HTML न दें।
- विद्यार्थी को दिखाई देने वाली सामग्री मानक, स्वाभाविक हिन्दी (देवनागरी) में हो। आवश्यक तकनीकी शब्द के बाद English term को कोष्ठक में दे सकते हैं।
- अध्ययन नोट्स में लंबे अनुच्छेद बिल्कुल न लिखें। हर व्याख्या छोटे, स्वतंत्र, बिंदुवार वाक्यों में हो।
- प्रत्येक अवधारणा अलग हो और विषय के सभी उप-विषयों को कवर करे।
- ताल, मात्रा, लय, layakari, bol, swar-lipi, वाद्य और संगीत-इतिहास से जुड़े तथ्य संगीतशास्त्रीय रूप से सही हों। मनगढ़ंत रचनाएँ, कलाकार, तिथियाँ या परंपराएँ न जोड़ें।
- revision में हर अवधारणा का अलग, सूक्ष्म, बिंदुवार entry अनिवार्य है।

यह exact JSON shape लौटाएँ:
{
  "title":"हिन्दी SEO शीर्षक",
  "section_title_hi":"पाठ्यक्रम खंड का हिन्दी शीर्षक",
  "short_title":"छोटा हिन्दी शीर्षक",
  "introduction_points":["कम-से-कम 4 संक्षिप्त बिंदु"],
  "concepts":[{
    "id":"stable-kebab-case-id",
    "title":"अवधारणा का हिन्दी शीर्षक",
    "lead":"एक वाक्य का सार",
    "explanation_points":["कम-से-कम 5 छोटे व्याख्यात्मक बिंदु"],
    "key_points":["कम-से-कम 4 मुख्य बिंदु"],
    "examples":["कम-से-कम 2 सही उदाहरण या अनुप्रयोग"],
    "comparison_points":["कम-से-कम 2 तुलनात्मक बिंदु"],
    "common_misconceptions":["कम-से-कम 2 सामान्य भ्रांतियाँ"],
    "exam_focus_points":["कम-से-कम 3 परीक्षा-केंद्रित बिंदु"]
  }],
  "revision":{
    "concept_revisions":[{"concept_id":"exact concept id","title":"अवधारणा शीर्षक","definition_points":["कम-से-कम 3 परिभाषात्मक बिंदु"],"must_remember":["कम-से-कम 5 सूक्ष्म स्मरण बिंदु"],"exam_traps":["कम-से-कम 2 अवधारणा-विशिष्ट परीक्षा जाल"]}],
    "quick_facts":["कम-से-कम 5 तथ्य"],
    "glossary":[{"term":"शब्द","definition":"हिन्दी परिभाषा"}],
    "comparisons":[{"left":"A","right":"B","difference_points":["कम-से-कम 2 अंतर"]}],
    "memory_hooks":["कम-से-कम 3 स्मृति-सहायक बिंदु"],
    "exam_traps":["कम-से-कम 4 सावधानियाँ"]
  }
}
4–8 अलग-अलग अवधारणाएँ दें।`;
}

function buildQuestionsPrompt(context, content) {
  const concepts = content.concepts.map((item) => `- ${item.id}: ${item.title} — ${item.lead}`).join('\n');
  return `आप UP PGT Music Instrumental के मुख्य परीक्षक हैं। नीचे दिए गए हिन्दी अध्ययन-नोट्स के आधार पर interactive quiz और timed test बनाएँ।
विषय: "${context.topicName}"
संकल्पनाएँ:
${concepts}

नियम:
- पूरा उत्तर केवल वैध JSON में दें; सभी question, options और explanation हिन्दी (देवनागरी) में हों।
- हर concept_id के लिए इन सभी सात प्रकारों का कम-से-कम एक प्रश्न दें: ${QUESTION_TYPES.join(', ')}.
- प्रश्न केवल शीर्षक दोहराने वाले न हों; ताल, मात्रा, लय, तिहाई, layakari, बोल, notation, वाद्य या संगीतशास्त्रीय सन्दर्भ पर आधारित हों।
- assertion_reason में assertion/reason और चार मानक विकल्प दें। match_following में दोनों सूचियाँ और चार code विकल्प दें। case_based में छोटा संगीत-अभ्यास/प्रदर्शन scenario दें।
- fill_blank में accepted_answers दें; short_answer में expected_answer दें।
- test में ठीक 10 objective प्रश्न हों; प्रकार केवल mcq, assertion_reason, match_following या case_based हों।
- तथ्य न गढ़ें और किसी कलाकार, रचना या ऐतिहासिक घटना का गलत attribution न करें।

यह exact shape लौटाएँ:
{"quiz_questions":[{"id":"q-001","concept_id":"concept-id","type":"mcq|assertion_reason|true_false|fill_blank|match_following|case_based|short_answer","question":"हिन्दी प्रश्न","options":["विकल्प 1","विकल्प 2","विकल्प 3","विकल्प 4"],"correct_index":0,"accepted_answers":["उत्तर"],"expected_answer":"उत्तर","explanation":"हिन्दी व्याख्या"}],"topic_test":[{"id":"t-001","concept_id":"concept-id","type":"mcq","question":"हिन्दी प्रश्न","options":["...","...","...","..."],"correct_index":0,"explanation":"हिन्दी व्याख्या"}]}
अनुपयुक्त fields को छोड़ सकते हैं, लेकिन सभी quiz questions में id, concept_id, type, question और explanation अनिवार्य हैं।`;
}

async function generateJson(prompt, ai, validator, label, maxAttempts = 2) {
  let activePrompt = prompt; let lastError;
  for (let attempt = 1; attempt <= maxAttempts; attempt += 1) {
    try {
      const response = await ai.models.generateContent({ model: MODEL, contents: activePrompt, config: { temperature: 0.25, responseMimeType: 'application/json' } });
      if (!response?.text) throw new Error('Gemini ने खाली उत्तर लौटाया');
      const data = parseJson(response.text);
      try { validator(data); } catch (validationError) { const error = new Error(`${label} validation failed: ${validationError.message}`); error.isValidationError = true; throw error; }
      return data;
    } catch (error) {
      lastError = error;
      const status = Number(error?.status || error?.code || error?.error?.code || error?.response?.status) || null;
      const quotaError = status === 429 || String(error?.message || '').includes('RESOURCE_EXHAUSTED');
      if ([400, 401, 403].includes(status) || quotaError) throw error;
      if (attempt < maxAttempts) {
        const validation = error.isValidationError === true;
        const waitMs = validation ? Math.min(8000, attempt * 2000) : Math.min(60000, 8000 * (2 ** (attempt - 1)));
        if (validation) activePrompt = `${prompt}\n\nपिछला JSON इस validation error के कारण अस्वीकार हुआ: ${error.message}\nपूरा corrected JSON फिर से दें। कोई field या minimum point count न छोड़ें।`;
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
  return content.concepts.map((concept, index) => `<section class="notes-section" id="concept-${escapeHtml(concept.id)}"><div class="concept-number">अवधारणा ${index + 1}</div><h2>${escapeHtml(concept.title)}</h2><p class="lead-concept">${inlineText(concept.lead)}</p><h3>व्याख्या</h3>${list(concept.explanation_points, 'notes-bullet-list')}<h3>मुख्य बिंदु</h3>${list(concept.key_points, 'notes-bullet-list')}<div class="music-callout"><strong>उदाहरण / अनुप्रयोग:</strong>${list(concept.examples, 'notes-bullet-list')}</div><div class="comparison-callout"><strong>तुलना:</strong>${list(concept.comparison_points, 'notes-bullet-list')}</div><div class="trap-callout"><strong>सामान्य भ्रांतियाँ:</strong>${list(concept.common_misconceptions, 'notes-bullet-list')}</div><div class="exam-focus"><strong>परीक्षा-केंद्रित बिंदु:</strong>${list(concept.exam_focus_points, 'notes-bullet-list')}</div></section>`).join('\n');
}

function renderRevision(revision, title) {
  const conceptRevisions = revision.concept_revisions.map((item, index) => `<section class="revision-card-box highlight"><div class="concept-number">अवधारणा ${index + 1}</div><h2>${escapeHtml(item.title)}</h2><h3>परिभाषा और क्षेत्र</h3>${list(item.definition_points, 'must-remember-list')}<h3>अवश्य याद रखें</h3>${list(item.must_remember, 'must-remember-list')}<h3>अवधारणा-विशिष्ट परीक्षा जाल</h3>${list(item.exam_traps, 'must-remember-list')}</section>`).join('');
  const glossary = revision.glossary.map((item) => `<div class="glossary-item"><strong>${escapeHtml(item.term)}</strong><span>${inlineText(item.definition)}</span></div>`).join('');
  const comparisons = revision.comparisons.map((item) => `<div class="revision-comparison"><div><strong>${escapeHtml(item.left)}</strong><span>बनाम</span><strong>${escapeHtml(item.right)}</strong></div>${list(item.difference_points, 'must-remember-list')}</div>`).join('');
  return `<div class="summary-hero-box"><h2>${escapeHtml(title)} — त्वरित पुनरावृत्ति</h2><p>हर अवधारणा को अलग-अलग दोहराएँ और फिर विषय परीक्षा दें।</p></div>${conceptRevisions}<section class="revision-card-box"><h2>त्वरित तथ्य</h2>${list(revision.quick_facts, 'must-remember-list')}</section><section class="revision-card-box"><h2>शब्दावली</h2><div class="glossary-grid">${glossary}</div></section><section class="revision-card-box"><h2>महत्वपूर्ण अंतर</h2><div class="revision-comparisons">${comparisons}</div></section><section class="revision-card-box"><h2>स्मृति-सहायक बिंदु</h2>${list(revision.memory_hooks, 'must-remember-list')}</section><section class="revision-card-box"><h2>परीक्षा सावधानियाँ</h2>${list(revision.exam_traps, 'must-remember-list')}</section>`;
}

function questionData(question) {
  const accepted = (question.accepted_answers || []).map((answer) => `<span class="accepted-answer">${inlineText(answer)}</span>`).join('');
  const expected = question.expected_answer ? `<span class="expected-answer">${inlineText(question.expected_answer)}</span>` : '';
  return `<div class="question-source-data" aria-hidden="true">${accepted}${expected}<p class="question-explanation">${inlineText(question.explanation)}</p></div>`;
}

function renderQuizQuestion(question, index) {
  const typeNames = { mcq: 'बहुविकल्पीय', assertion_reason: 'कथन–कारण', true_false: 'सही / गलत', fill_blank: 'रिक्त स्थान', match_following: 'मिलान', case_based: 'परिस्थिति-आधारित', short_answer: 'लघु उत्तर' };
  const letters = ['A', 'B', 'C', 'D', 'E']; let body;
  if (question.type === 'fill_blank') body = `<input class="quiz-answer-input" id="quiz-input-${index}" aria-label="उत्तर लिखें"><button class="quiz-check-btn" data-fill="${index}">उत्तर जाँचें</button>`;
  else if (question.type === 'short_answer') body = `<textarea class="quiz-answer-textarea" id="quiz-input-${index}" aria-label="उत्तर लिखें"></textarea><button class="quiz-check-btn" data-short="${index}">उत्तर देखें</button>`;
  else body = `<div class="quiz-options-group">${question.options.map((option, optionIndex) => `<button type="button" class="quiz-option-btn" data-quiz="${index}" data-option="${optionIndex}"><span class="option-letter">${letters[optionIndex]}</span><span class="option-text">${inlineText(option)}</span></button>`).join('')}</div>`;
  const correct = Number.isInteger(question.correct_index) ? ` data-correct="${question.correct_index}"` : '';
  return `<article class="quiz-question-card" id="quiz-card-${index}" data-index="${index}" data-type="${escapeHtml(question.type)}"${correct}><div class="q-header"><span class="q-number">प्रश्न ${index + 1}</span><span class="question-type">${escapeHtml(typeNames[question.type] || question.type)}</span></div><p class="q-text">${inlineText(question.question)}</p>${body}${questionData(question)}<div id="quiz-feedback-${index}"></div></article>`;
}

function renderTestQuestion(question, index) {
  const typeNames = { mcq: 'बहुविकल्पीय', assertion_reason: 'कथन–कारण', match_following: 'मिलान', case_based: 'परिस्थिति-आधारित' }; const letters = ['A', 'B', 'C', 'D', 'E'];
  return `<article class="test-question-card" id="test-card-${index}" data-index="${index}" data-correct="${question.correct_index}"><div class="test-q-header"><span class="t-badge">प्रश्न ${index + 1}</span><span class="question-type">${escapeHtml(typeNames[question.type] || question.type)}</span></div><p class="test-question-text">${inlineText(question.question)}</p><div class="quiz-options-group">${question.options.map((option, optionIndex) => `<button type="button" class="test-option-btn quiz-option-btn" data-test="${index}" data-option="${optionIndex}"><span class="option-letter">${letters[optionIndex]}</span><span class="option-text">${inlineText(option)}</span></button>`).join('')}</div>${questionData(question)}<div id="test-feedback-${index}"></div></article>`;
}

function compileHtml(content, questions, context) {
  const canonical = `https://sjmaths.com${context.url}`; const title = content.short_title || context.topicName; const description = `${title}: Music Instrumental के लिए हिन्दी अध्ययन नोट्स, अवधारणा क्विज़, पुनरावृत्ति सारांश और विषय परीक्षा।`;
  return `<!doctype html><html lang="hi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>${escapeHtml(content.title)} | वाद्य संगीत | SJ Maths</title><meta name="description" content="${escapeHtml(description)}"><meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1"><meta name="author" content="SJ Maths"><meta name="theme-color" content="#7c2d12"><link rel="canonical" href="${canonical}"><link rel="icon" type="image/png" href="/favicon.png"><meta property="og:type" content="article"><meta property="og:site_name" content="SJ Maths"><meta property="og:title" content="${escapeHtml(content.title)} | वाद्य संगीत"><meta property="og:description" content="${escapeHtml(description)}"><meta property="og:url" content="${canonical}"><meta property="og:image" content="https://sjmaths.com/assets/images/og-default.jpg"><meta name="twitter:card" content="summary"><meta name="twitter:title" content="${escapeHtml(content.title)} | वाद्य संगीत"><meta name="twitter:description" content="${escapeHtml(description)}"><script type="application/ld+json">${safeJson({ '@context': 'https://schema.org', '@type': 'LearningResource', name: content.title, headline: content.title, description, url: canonical, inLanguage: 'hi', educationalLevel: 'UP PGT', learningResourceType: 'Study guide', isPartOf: { '@type': 'WebSite', name: 'SJ Maths', url: 'https://sjmaths.com/' } })}</script><link rel="stylesheet" href="/assets/css/topic-page.min.css?v=718ef3ff"><style>:root{--brand:#7c2d12;--brand-dark:#431407;--brand-light:#c2410c;--accent:#c2410c;--accent-hover:#9a3412;--accent-soft:rgba(194,65,12,.09);--accent-border:rgba(194,65,12,.26)}body{font-family:"Noto Sans Devanagari","Mangal",Inter,Arial,sans-serif;background:radial-gradient(circle at 100% 0,rgba(194,65,12,.07),transparent 28rem),var(--bg,#f6f8fb)}.study-tabs{grid-template-columns:repeat(4,minmax(0,1fr))}.tab-btn{min-height:54px}.tab-panel.hidden,.question-source-data,.hidden{display:none!important}.concept-number{display:inline-block;margin-bottom:8px;color:var(--accent);font-size:.74rem;font-weight:900}.lead-concept{font-weight:700;color:var(--brand);font-size:1rem}.notes-section h3{margin-top:18px;color:var(--brand);font-size:1rem}.music-callout,.comparison-callout,.trap-callout,.exam-focus{padding:14px 16px;border-radius:10px;margin:14px 0;line-height:1.7}.music-callout{background:#fff7ed;border-left:4px solid #ea580c}.comparison-callout{background:#f0fdf4;border-left:4px solid #15803d}.trap-callout{background:#fffbeb;border-left:4px solid #d97706}.exam-focus{background:var(--accent-soft);border-left:4px solid var(--accent);color:var(--ink2)}.question-type{display:inline-flex;padding:3px 9px;border-radius:999px;background:var(--accent-soft);color:var(--accent);font-size:.72rem;font-weight:850}.quiz-answer-input,.quiz-answer-textarea{width:100%;padding:11px 13px;border:1px solid var(--line);border-radius:9px;background:var(--paper);color:var(--ink);font:inherit}.quiz-answer-textarea{min-height:96px;resize:vertical}.quiz-check-btn{margin-top:10px;padding:9px 14px;border:0;border-radius:8px;background:var(--brand);color:#fff;font-weight:800;cursor:pointer}.quiz-feedback{margin-top:13px}.revision-comparisons{display:flex;flex-direction:column;gap:12px}.revision-comparison{padding:14px 16px;border:1px solid var(--line);border-radius:10px;background:var(--paper-card)}.revision-comparison>div{display:flex;gap:9px;align-items:center;flex-wrap:wrap;color:var(--brand)}.revision-comparison span{color:var(--muted);font-size:.78rem}.test-question-card .test-option-btn{width:100%;text-align:left}.quiz-question-card[data-answered="true"]{border-color:var(--accent-border)}@media(max-width:680px){.study-tabs{grid-template-columns:repeat(2,minmax(0,1fr))}.tab-btn{font-size:.78rem}.tab-btn span:first-child{display:none}}</style></head><body><header class="site-header"><div class="wrap header-inner"><a class="brand" href="https://sjmaths.com/"><span class="brand-mark" style="background:linear-gradient(145deg,#7c2d12,#c2410c);font-family:serif;font-size:1.35rem;font-style:italic;display:flex;align-items:center;justify-content:center">&int;</span><span><span class="brand-name">SJ Maths</span><span class="brand-sub">वाद्य संगीत</span></span></a><div class="header-actions"><button type="button" class="theme-toggle-btn" id="btn-theme-toggle" aria-label="डार्क मोड बदलें">डार्क मोड</button><a class="back-btn" href="/up-pgt-music-instrumental/">← UP PGT Music Instrumental</a></div></div></header><main class="wrap"><section class="hero"><nav class="breadcrumb" aria-label="ब्रेडक्रंब"><a href="https://sjmaths.com/">मुख्य पृष्ठ</a><span>›</span><a href="/up-pgt-music-instrumental/">वाद्य संगीत</a><span>›</span><span>${escapeHtml(context.sectionTitle)}</span><span>›</span><span aria-current="page">${escapeHtml(title)}</span></nav><div class="kicker">${escapeHtml(context.sectionTitle)}</div><h1>${escapeHtml(content.title)}</h1><p class="lead">${escapeHtml(content.introduction_points[0])}</p><div class="exam-badges"><a class="exam-chip pgt" href="/up-pgt-music-instrumental/">UP PGT Music Instrumental</a><span class="exam-chip both">${content.concepts.length} अवधारणाएँ</span><span class="exam-chip both">${questions.quiz_questions.length} प्रश्न</span><span class="exam-chip both">10 प्रश्नों की परीक्षा</span></div></section><div class="study-tabs-sticky-wrapper"><div class="study-tabs" role="tablist" aria-label="वाद्य संगीत अध्ययन टैब"><button type="button" class="tab-btn active" role="tab" aria-selected="true" data-tab="tab-notes" id="tab-btn-notes"><span>📖</span><span>अध्ययन नोट्स</span></button><button type="button" class="tab-btn" role="tab" aria-selected="false" data-tab="tab-quiz" id="tab-btn-quiz"><span>❓</span><span>अवधारणा क्विज़</span><span class="tab-badge">${questions.quiz_questions.length} प्रश्न</span></button><button type="button" class="tab-btn" role="tab" aria-selected="false" data-tab="tab-summary" id="tab-btn-summary"><span>⚡</span><span>पुनरावृत्ति सारांश</span></button><button type="button" class="tab-btn" role="tab" aria-selected="false" data-tab="tab-test" id="tab-btn-test"><span>⏱️</span><span>विषय परीक्षा</span><span class="tab-badge">10 प्रश्न</span></button></div></div><div class="main-grid"><div class="content-col"><article class="tab-panel active" id="tab-notes" role="tabpanel" aria-labelledby="tab-btn-notes"><div class="card"><h2>विषय का संक्षिप्त परिचय</h2>${list(content.introduction_points, 'notes-bullet-list')}</div>${renderConcepts(content)}<nav class="topic-pagination" aria-label="विषय नेविगेशन"><a class="topic-nav-btn next" href="/up-pgt-music-instrumental/"><span>पाठ्यक्रम ट्रैकर →</span><strong>UP PGT Music Instrumental</strong></a></nav></article><article class="tab-panel hidden" id="tab-quiz" role="tabpanel" aria-labelledby="tab-btn-quiz"><div class="quiz-panel-header"><div class="quiz-panel-title"><h2>अवधारणा क्विज़</h2><p>हर अवधारणा के लिए विभिन्न प्रकार के हिन्दी प्रश्न।</p></div><div class="quiz-live-scoreboard"><span class="score-pill" id="quiz-score">अंक: 0 / ${questions.quiz_questions.length}</span><button type="button" class="btn-reset-quiz" id="btn-reset-quiz">पुनः शुरू करें</button></div></div><div class="quiz-questions-list" id="quiz-container">${questions.quiz_questions.map(renderQuizQuestion).join('')}</div></article><article class="tab-panel hidden" id="tab-summary" role="tabpanel" aria-labelledby="tab-btn-summary"><div class="summary-container">${renderRevision(content.revision, title)}</div></article><article class="tab-panel hidden" id="tab-test" role="tabpanel" aria-labelledby="tab-btn-test"><div class="test-panel-header"><div><h2>समयबद्ध विषय परीक्षा</h2><p>10 वस्तुनिष्ठ प्रश्न। टैब खोलते ही 10 मिनट की घड़ी शुरू होगी।</p></div><span class="test-timer-badge" id="test-timer">10:00</span></div><div class="test-questions-list" id="test-container">${questions.topic_test.map(renderTestQuestion).join('')}</div><div class="test-submit-bar"><button type="button" class="btn-submit-test" id="btn-submit-test">परीक्षा जमा करें</button></div><div class="test-result-modal hidden" id="test-result"><div class="result-card"><h3>परीक्षा परिणाम</h3><div class="result-score-circle"><span id="test-score">0</span> / 10</div><p id="test-feedback">व्याख्याएँ पढ़कर पुनः प्रयास करें।</p><button type="button" class="btn-retake-test" id="btn-retake-test">पुनः प्रयास करें</button></div></div></article></div><aside class="sidebar-col"><div class="sidebar-card side-card"><div class="side-card-header"><span class="side-badge">पाठ्यक्रम खंड</span><h3>${escapeHtml(context.sectionTitle)}</h3></div><p class="side-desc">इस विषय के हिन्दी अध्ययन नोट्स, अवधारणा अभ्यास, पुनरावृत्ति और परीक्षा।</p><div class="side-action-box" style="margin-top:1.5rem"><a class="side-action-btn" href="/up-pgt-music-instrumental/" style="background:#7c2d12;display:block;text-align:center;padding:10px;color:#fff;border-radius:8px;font-weight:600">पूरा पाठ्यक्रम ट्रैकर →</a></div></div></aside></div></main><footer class="site-footer"><div class="wrap footer-inner"><div><p><strong>SJ Maths — वाद्य संगीत</strong></p><p>UP PGT Music Instrumental के लिए हिन्दी अध्ययन सामग्री।</p></div><div class="footer-links"><a href="https://sjmaths.com/">मुख्य पृष्ठ</a><a href="/up-pgt-music-instrumental/">UP PGT Music Instrumental</a></div></div></footer><script type="application/json" id="quiz-data">${safeJson(questions.quiz_questions)}</script><script type="application/json" id="test-data">${safeJson(questions.topic_test)}</script><script>document.addEventListener('DOMContentLoaded',()=>{const esc=(value)=>String(value??'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#39;');const quiz=JSON.parse(document.getElementById('quiz-data').textContent);const test=JSON.parse(document.getElementById('test-data').textContent);let score=0;const answered=new Set();const feedback=(ok,text)=>'<div class="quiz-feedback '+(ok?'correct':'incorrect')+'"><strong>'+(ok?'✓ सही':'✕ पुनः देखें')+'</strong><p>'+esc(text)+'</p></div>';const explanation=(card)=>card.querySelector('.question-explanation')?.textContent||'';function mark(card,ok,extra=''){const index=Number(card.dataset.index);if(answered.has(index))return;answered.add(index);if(ok)score++;card.dataset.answered='true';card.querySelectorAll('button').forEach((button)=>button.disabled=true);document.getElementById('quiz-feedback-'+index).innerHTML=feedback(ok,extra+explanation(card));document.getElementById('quiz-score').textContent='अंक: '+score+' / '+quiz.length;}document.querySelectorAll('[data-quiz]').forEach((button)=>button.addEventListener('click',()=>{const card=button.closest('.quiz-question-card');const chosen=Number(button.dataset.option);const correct=Number(card.dataset.correct);card.querySelectorAll('[data-option]').forEach((item,index)=>{item.disabled=true;if(index===correct)item.classList.add('correct');if(index===chosen&&chosen!==correct)item.classList.add('incorrect');});mark(card,chosen===correct);}));document.querySelectorAll('[data-fill]').forEach((button)=>button.addEventListener('click',()=>{const card=button.closest('.quiz-question-card');const value=document.getElementById('quiz-input-'+card.dataset.index).value.trim().toLowerCase();const answers=[...card.querySelectorAll('.accepted-answer')].map((item)=>item.textContent.trim().toLowerCase());mark(card,answers.includes(value),'स्वीकृत उत्तर: '+answers.join(', ')+'। ');}));document.querySelectorAll('[data-short]').forEach((button)=>button.addEventListener('click',()=>{const card=button.closest('.quiz-question-card');const expected=card.querySelector('.expected-answer')?.textContent||'';mark(card,false,'अपेक्षित उत्तर: '+expected+'। ');}));document.getElementById('btn-reset-quiz').addEventListener('click',()=>location.reload());const chosen={};let submitted=false;document.querySelectorAll('[data-test]').forEach((button)=>button.addEventListener('click',()=>{if(submitted)return;const card=button.closest('.test-question-card');chosen[card.dataset.index]=Number(button.dataset.option);card.querySelectorAll('[data-option]').forEach((item)=>item.classList.remove('selected'));button.classList.add('selected');}));function submitTest(){if(submitted)return;submitted=true;let total=0;document.querySelectorAll('.test-question-card').forEach((card)=>{const index=card.dataset.index;const answer=chosen[index];const correct=Number(card.dataset.correct);if(answer===correct)total++;card.querySelectorAll('[data-option]').forEach((item,optionIndex)=>{item.disabled=true;if(optionIndex===correct)item.classList.add('correct');if(optionIndex===answer&&answer!==correct)item.classList.add('incorrect');});document.getElementById('test-feedback-'+index).innerHTML=feedback(answer===correct,explanation(card));});document.getElementById('test-score').textContent=total;document.getElementById('test-result').classList.remove('hidden');document.getElementById('btn-submit-test').classList.add('hidden');}document.getElementById('btn-submit-test').addEventListener('click',submitTest);document.getElementById('btn-retake-test').addEventListener('click',()=>location.reload());let timer=null,remaining=600;function startTimer(){if(timer||submitted)return;timer=setInterval(()=>{remaining--;document.getElementById('test-timer').textContent=String(Math.floor(remaining/60)).padStart(2,'0')+':'+String(remaining%60).padStart(2,'0');if(remaining<=0){clearInterval(timer);submitTest();}},1000);}const tabs=document.querySelectorAll('.tab-btn'),panels=document.querySelectorAll('.tab-panel');tabs.forEach((button)=>button.addEventListener('click',()=>{tabs.forEach((item)=>{item.classList.remove('active');item.setAttribute('aria-selected','false');});panels.forEach((panel)=>{panel.classList.remove('active');panel.classList.add('hidden');});button.classList.add('active');button.setAttribute('aria-selected','true');document.getElementById(button.dataset.tab).classList.remove('hidden');document.getElementById(button.dataset.tab).classList.add('active');if(button.dataset.tab==='tab-test')startTimer();window.scrollTo({top:document.querySelector('.study-tabs-sticky-wrapper').offsetTop-15,behavior:'smooth'});}));const theme=document.getElementById('btn-theme-toggle');const saved=localStorage.getItem('sjmaths_theme')||localStorage.getItem('sj_theme');if(saved==='dark'){document.body.classList.add('dark-mode');document.documentElement.classList.add('dark');theme.textContent='लाइट मोड';}theme.addEventListener('click',()=>{const dark=document.body.classList.toggle('dark-mode');document.documentElement.classList.toggle('dark',dark);localStorage.setItem('sjmaths_theme',dark?'dark':'light');theme.textContent=dark?'लाइट मोड':'डार्क मोड';});});</script></body></html>`;
}

function chooseApiKey() {
  const names = { '1': 'GEMINI_API_KEY_1', '2': 'GEMINI_API_KEY_2', GEMINI_API_KEY: 'GEMINI_API_KEY', GEMINI_API_KEY_1: 'GEMINI_API_KEY_1', GEMINI_API_KEY_2: 'GEMINI_API_KEY_2' };
  const name = names[keySelector] || 'GEMINI_API_KEY'; const key = process.env[name];
  if (!key) throw new Error(`Set ${name} in .env before running the Hindi music generator.`);
  return { name, key };
}

async function processTopic(url, contexts, ai, status) {
  const parts = url.split('/').filter(Boolean); const fallback = { url, topicName: parts.at(-1).replace(/-/g, ' '), sectionTitle: 'Music Instrumental', key: parts.slice(1).join('/') };
  const context = contexts.get(url) || fallback; const targetDir = urlToDir(url); const indexPath = path.join(targetDir, 'index.html');
  if (!force && isHindiGeneratedPage(indexPath)) { console.log(`Skipped ${url} (Hindi page already generated; use --force to regenerate)`); return; }
  console.log(`\nGenerating Hindi page: ${url} — ${context.topicName}`); status[url] = { status: 'generating', model: MODEL, key: keySelector, startedAt: new Date().toISOString() }; writeStatus(status);
  const content = await generateJson(buildContentPrompt(context), ai, validateContent, 'Study notes'); context.sectionTitle = content.section_title_hi; console.log(`  ✓ notes: ${content.concepts.length} अवधारणाएँ`);
  if (gapMs) await new Promise((resolve) => setTimeout(resolve, gapMs));
  const conceptIds = content.concepts.map((item) => item.id); const questions = await generateJson(buildQuestionsPrompt(context, content), ai, (data) => validateQuestions(data, conceptIds), 'Quiz and test');
  console.log(`  ✓ quiz: ${questions.quiz_questions.length}; test: ${questions.topic_test.length}`); fs.mkdirSync(targetDir, { recursive: true });
  fs.writeFileSync(indexPath, compileHtml(content, questions, context), 'utf8');
  status[url] = { status: 'completed', model: MODEL, key: keySelector, language: 'hi', title: content.title, concepts: content.concepts.length, quizQuestions: questions.quiz_questions.length, testQuestions: 10, completedAt: new Date().toISOString() }; writeStatus(status);
  console.log(`  ✓ wrote ${indexPath}`);
}

async function main() {
  const contexts = readTrackerContexts(); const targets = resolveTargets(contexts); const keyName = { '1': 'GEMINI_API_KEY_1', '2': 'GEMINI_API_KEY_2', GEMINI_API_KEY: 'GEMINI_API_KEY', GEMINI_API_KEY_1: 'GEMINI_API_KEY_1', GEMINI_API_KEY_2: 'GEMINI_API_KEY_2' }[keySelector] || 'GEMINI_API_KEY'; console.log(`Discovered ${targets.length} Music Instrumental page(s). Language: Hindi. Model: ${MODEL}. Key: ${keyName}`);
  if (dryRun) { targets.forEach((url) => console.log(`${url} — ${contexts.get(url)?.topicName || 'title unavailable'}`)); return; }
  const selected = chooseApiKey(); const ai = new GoogleGenAI({ apiKey: selected.key }); const status = readStatus();
  for (const url of targets) { try { await processTopic(url, contexts, ai, status); } catch (error) { status[url] = { status: 'failed', model: MODEL, key: selected.name, language: 'hi', error: error.message, failedAt: new Date().toISOString() }; writeStatus(status); console.error(`  ✗ ${url}: ${error.message}`); if (requestedTopic) throw error; } }
}

main().catch((error) => { console.error(`Generation failed: ${error.message}`); process.exitCode = 1; });
