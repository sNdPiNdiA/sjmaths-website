#!/usr/bin/env node
/**
 * SJ Maths Military Science topic-page generator.
 *
 * Each generated topic contains four tabs:
 *   1. Study Notes
 *   2. Concept Quiz (all supported question types for every concept)
 *   3. Revision Summary
 *   4. Timed Topic Test
 *
 * Examples:
 *   node scripts/generate_military_science.mjs --dry-run
 *   node scripts/generate_military_science.mjs --topic /military-science/war/meaning/ --force
 *   node scripts/generate_military_science.mjs --all --gap 15
 */

import fs from 'node:fs';
import path from 'node:path';
import 'dotenv/config';
import { GoogleGenAI } from '@google/genai';
import { jsonrepair } from 'jsonrepair';

const ROOT = process.cwd();
const MILITARY_ROOT = path.join(ROOT, 'military-science');
const TRACKER_PATH = path.join(ROOT, 'up-pgt-military-science', 'index.html');
const STATUS_PATH = path.join(ROOT, 'content-generation-status-military-science.json');
const MODEL = process.env.GEMINI_MODEL || 'gemini-3.5-flash-lite';
const QUESTION_TYPES = [
  'mcq',
  'assertion_reason',
  'true_false',
  'fill_blank',
  'match_following',
  'case_based',
  'short_answer'
];

const args = process.argv.slice(2);
const hasFlag = (flag) => args.includes(flag);
function argValue(flag) {
  const index = args.indexOf(flag);
  return index >= 0 ? args[index + 1] : null;
}

const requestedTopic = argValue('--topic');
const dryRun = hasFlag('--dry-run');
const force = hasFlag('--force');
const allFlag = hasFlag('--all');
const gapMs = Math.max(0, Number.parseInt(argValue('--gap') || '0', 10) || 0) * 1000;

function stripTags(value) {
  return String(value || '')
    .replace(/<[^>]*>/g, ' ')
    .replace(/&amp;/g, '&').replace(/&quot;/g, '"').replace(/&#39;/g, "'")
    .replace(/&ndash;/g, '–').replace(/&mdash;/g, '—').replace(/&rsquo;/g, '’')
    .replace(/&ldquo;/g, '“').replace(/&rdquo;/g, '”').replace(/&nbsp;/g, ' ')
    .replace(/&#(\d+);/g, (_, code) => String.fromCodePoint(Number(code)))
    .replace(/&#x([\da-f]+);/gi, (_, code) => String.fromCodePoint(Number.parseInt(code, 16)))
    .replace(/\s+/g, ' ').trim();
}

function titleFromSlug(slug) {
  return slug.split('-').map((word) => word ? word[0].toUpperCase() + word.slice(1) : word).join(' ');
}

function normalizeUrl(value) {
  let url = String(value || '').trim().replace(/\\/g, '/');
  if (!url.startsWith('/')) url = `/${url}`;
  if (!url.endsWith('/')) url += '/';
  return url.replace(/\/index\.html\/$/, '/');
}

function urlToDir(url) {
  return path.join(ROOT, url.replace(/^\//, '').replace(/\/$/, ''));
}

function readStatus() {
  if (!fs.existsSync(STATUS_PATH)) return {};
  try { return JSON.parse(fs.readFileSync(STATUS_PATH, 'utf8')); } catch { return {}; }
}

function writeStatus(status) {
  fs.writeFileSync(STATUS_PATH, `${JSON.stringify(status, null, 2)}\n`, 'utf8');
}

function readTrackerContexts() {
  if (!fs.existsSync(TRACKER_PATH)) return new Map();
  const html = fs.readFileSync(TRACKER_PATH, 'utf8');
  const contexts = new Map();
  const sectionRegex = /<article[^>]*class="section-card"[^>]*id="point-[^"]+"[^>]*>([\s\S]*?)(?=<article[^>]*class="section-card"|<\/section>)/gi;
  let sectionMatch;
  while ((sectionMatch = sectionRegex.exec(html))) {
    const sectionHtml = sectionMatch[1];
    const heading = stripTags(sectionHtml.match(/<span class="section-title">([\s\S]*?)<\/span>/i)?.[1] || 'Military Science');
    const topicRegex = /<div class="topic"[^>]*data-key="([^"]+)"[\s\S]*?<a class="topic-link" href="([^"]+)">([\s\S]*?)<\/a>/gi;
    let topicMatch;
    while ((topicMatch = topicRegex.exec(sectionHtml))) {
      const url = normalizeUrl(topicMatch[2]);
      contexts.set(url, {
        url,
        topicName: stripTags(topicMatch[3]),
        sectionTitle: heading,
        key: topicMatch[1]
      });
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
      else if (entry.name === 'index.html') {
        const relative = path.relative(ROOT, full).replace(/\\/g, '/');
        urls.push(normalizeUrl(`/${relative}`));
      }
    }
  }
  walk(MILITARY_ROOT);
  return urls.sort();
}

function resolveTargets(contexts) {
  const all = discoverTopicUrls();
  if (requestedTopic) {
    const url = normalizeUrl(requestedTopic);
    if (!all.includes(url)) throw new Error(`Topic page not found on disk: ${url}`);
    return [url];
  }
  if (allFlag || dryRun) return all;
  throw new Error('Choose --topic /military-science/.../, --all, or --dry-run.');
}

function parseJson(raw) {
  const cleaned = String(raw || '').trim()
    .replace(/^```(?:json)?\s*/i, '')
    .replace(/\s*```$/i, '').trim();
  try { return JSON.parse(cleaned); }
  catch (firstError) {
    try { return JSON.parse(jsonrepair(cleaned)); }
    catch { throw new Error(`Gemini returned invalid JSON: ${firstError.message}`); }
  }
}

function requireText(value, label) {
  if (typeof value !== 'string' || !value.trim()) throw new Error(`${label} must be a non-empty string`);
}

function validateContent(data) {
  if (!data || !Array.isArray(data.concepts) || data.concepts.length < 4 || data.concepts.length > 8) {
    throw new Error('Content must contain 4–8 concepts');
  }
  requireText(data.title, 'title');
  if (!Array.isArray(data.introduction_points) || data.introduction_points.length < 4) {
    throw new Error('Introduction must contain at least 4 point-wise items');
  }
  const ids = new Set();
  for (const [index, concept] of data.concepts.entries()) {
    requireText(concept.id, `concept ${index + 1} id`);
    requireText(concept.title, `concept ${index + 1} title`);
    if (ids.has(concept.id)) throw new Error(`Duplicate concept id: ${concept.id}`);
    ids.add(concept.id);
    if (!Array.isArray(concept.explanation_points) || concept.explanation_points.length < 5) throw new Error(`Concept ${concept.id} needs 5 explanation_points`);
    if (!Array.isArray(concept.key_points) || concept.key_points.length < 4) throw new Error(`Concept ${concept.id} needs 4 key_points`);
    if (!Array.isArray(concept.examples) || concept.examples.length < 2) throw new Error(`Concept ${concept.id} needs 2 examples`);
    if (!Array.isArray(concept.comparison_points) || concept.comparison_points.length < 2) throw new Error(`Concept ${concept.id} needs 2 comparison_points`);
    if (!Array.isArray(concept.common_misconceptions) || concept.common_misconceptions.length < 2) throw new Error(`Concept ${concept.id} needs 2 common_misconceptions`);
    if (!Array.isArray(concept.exam_focus_points) || concept.exam_focus_points.length < 3) throw new Error(`Concept ${concept.id} needs 3 exam_focus_points`);
    [...data.introduction_points, ...concept.explanation_points, ...concept.key_points, ...concept.examples, ...concept.comparison_points, ...concept.common_misconceptions, ...concept.exam_focus_points].forEach((item, itemIndex) => requireText(item, `concept ${concept.id} point ${itemIndex + 1}`));
  }
  if (!data.revision || !Array.isArray(data.revision.quick_facts) || data.revision.quick_facts.length < 5) throw new Error('Revision summary is incomplete');
  if (!Array.isArray(data.revision.glossary) || data.revision.glossary.length < 4) throw new Error('Revision glossary is incomplete');
  if (!Array.isArray(data.revision.comparisons) || data.revision.comparisons.length < 1) throw new Error('Revision comparisons are incomplete');
  if (!Array.isArray(data.revision.concept_revisions) || data.revision.concept_revisions.length !== data.concepts.length) throw new Error('Revision must contain one detailed entry for every concept');
  const revisionIds = new Set();
  for (const revision of data.revision.concept_revisions) {
    requireText(revision.concept_id, 'revision concept_id');
    if (!ids.has(revision.concept_id)) throw new Error(`Revision references unknown concept ${revision.concept_id}`);
    if (revisionIds.has(revision.concept_id)) throw new Error(`Duplicate revision concept ${revision.concept_id}`);
    revisionIds.add(revision.concept_id);
    requireText(revision.title, `revision ${revision.concept_id} title`);
    if (!Array.isArray(revision.definition_points) || revision.definition_points.length < 3) throw new Error(`Revision ${revision.concept_id} needs 3 definition_points`);
    if (!Array.isArray(revision.must_remember) || revision.must_remember.length < 5) throw new Error(`Revision ${revision.concept_id} needs 5 must_remember points`);
    if (!Array.isArray(revision.exam_traps) || revision.exam_traps.length < 2) throw new Error(`Revision ${revision.concept_id} needs 2 exam_traps`);
    [...revision.definition_points, ...revision.must_remember, ...revision.exam_traps].forEach((item, itemIndex) => requireText(item, `revision ${revision.concept_id} point ${itemIndex + 1}`));
  }
  for (const comparison of data.revision.comparisons) {
    requireText(comparison.left, 'revision comparison left');
    requireText(comparison.right, 'revision comparison right');
    if (!Array.isArray(comparison.difference_points) || comparison.difference_points.length < 2) throw new Error('Revision comparison needs point-wise difference_points');
  }
  return data;
}

function validateQuestion(question, label, allowShortAnswer = true) {
  requireText(question.id, `${label} id`);
  requireText(question.concept_id, `${label} concept_id`);
  requireText(question.type, `${label} type`);
  if (!QUESTION_TYPES.includes(question.type)) throw new Error(`${label} has unsupported type ${question.type}`);
  requireText(question.question, `${label} question`);
  if (question.type === 'fill_blank') {
    if (!Array.isArray(question.accepted_answers) || question.accepted_answers.length < 1) throw new Error(`${label} needs accepted_answers`);
  } else if (question.type === 'short_answer') {
    if (!allowShortAnswer) throw new Error(`${label} cannot be short_answer`);
    requireText(question.expected_answer, `${label} expected_answer`);
  } else {
    if (!Array.isArray(question.options) || question.options.length < 2) throw new Error(`${label} needs options`);
    if (!Number.isInteger(question.correct_index) || question.correct_index < 0 || question.correct_index >= question.options.length) {
      throw new Error(`${label} has an invalid correct_index`);
    }
  }
  requireText(question.explanation, `${label} explanation`);
}

function validateQuestions(data, conceptIds) {
  if (!data || !Array.isArray(data.quiz_questions) || data.quiz_questions.length < conceptIds.length * QUESTION_TYPES.length) {
    throw new Error(`Quiz needs at least ${conceptIds.length * QUESTION_TYPES.length} questions`);
  }
  if (!Array.isArray(data.topic_test) || data.topic_test.length !== 10) throw new Error('Topic test must contain exactly 10 questions');
  const coverage = new Map(conceptIds.map((id) => [id, new Set()]));
  data.quiz_questions.forEach((question, index) => {
    validateQuestion(question, `quiz question ${index + 1}`);
    if (!coverage.has(question.concept_id)) throw new Error(`Quiz question ${question.id} references an unknown concept`);
    coverage.get(question.concept_id).add(question.type);
  });
  for (const [conceptId, types] of coverage) {
    const missing = QUESTION_TYPES.filter((type) => !types.has(type));
    if (missing.length) throw new Error(`Concept ${conceptId} is missing quiz types: ${missing.join(', ')}`);
  }
  data.topic_test.forEach((question, index) => {
    if (!['mcq', 'assertion_reason', 'match_following', 'case_based'].includes(question.type)) {
      throw new Error(`test question ${index + 1} must be an objective question type`);
    }
    validateQuestion(question, `test question ${index + 1}`, false);
    if (!conceptIds.includes(question.concept_id)) throw new Error(`Test question ${question.id} references an unknown concept`);
  });
  return data;
}

function buildContentPrompt(context) {
  return `You are a senior Military Science professor and UP PGT Subject Code 25 examiner.
Create accurate, exam-oriented study material for this syllabus topic:
Topic: "${context.topicName}"
Syllabus section: "${context.sectionTitle}"
URL key: "${context.key}"
Audience: Indian competitive-exam students preparing UP PGT Military Science.

Requirements:
- Cover the topic comprehensively but keep explanations readable for students.
- Do not write long paragraphs in the study notes. Every explanation must be point-wise.
- Use short standalone bullet points, normally 8–28 words each. Keep one idea per bullet.
- The revision summary must include a detailed point-wise entry for every concept; do not merge concepts.
- Use established military-science, security-studies and Indian national-security terminology.
- Do not invent treaties, dates, operations, institutions or official policy details.
- Distinguish a factual claim from an analytical interpretation where needed.
- Include India-specific relevance where the syllabus topic requires it.
- Return ONLY valid JSON. Do not use Markdown fences and do not include HTML.
- Use plain text strings; use normal punctuation and Unicode safely.

Return exactly this shape:
{
  "title": "SEO-friendly topic title",
  "short_title": "short topic name",
  "introduction_points": ["at least 4 concise overview points"],
  "concepts": [
    {
      "id": "stable-kebab-case-id",
      "title": "Concept heading",
      "lead": "One-sentence central idea",
      "explanation_points": ["at least 5 short explanatory points"],
      "key_points": ["at least 4 precise points"],
      "examples": ["at least 2 relevant examples or applications"],
      "comparison_points": ["at least 2 point-wise comparisons with related ideas"],
      "common_misconceptions": ["at least 2 likely exam misconceptions"],
      "exam_focus_points": ["at least 3 point-wise exam targets"]
    }
  ],
  "revision": {
    "concept_revisions": [
      {
        "concept_id": "exact concept id",
        "title": "concept title",
        "definition_points": ["at least 3 points that define the concept"],
        "must_remember": ["at least 5 minute rapid-recall points"],
        "exam_traps": ["at least 2 concept-specific traps"]
      }
    ],
    "quick_facts": ["at least 5 rapid-recall facts"],
    "glossary": [{"term":"term", "definition":"short accurate definition"}],
    "comparisons": [{"left":"concept A", "right":"concept B", "difference_points":["at least 2 point-wise distinctions"]}],
    "memory_hooks": ["at least 3 useful memory hooks"],
    "exam_traps": ["at least 4 common traps or cautions"]
  }
}
Generate 4–8 concepts. Every concept must be materially different and together they must cover the complete syllabus topic.`;
}

function buildQuestionsPrompt(context, content) {
  const conceptList = content.concepts.map((concept) => `- ${concept.id}: ${concept.title} — ${concept.lead}`).join('\n');
  return `You are the chief examiner for UP PGT Military Science.
Create the interactive question bank and timed test for:
Topic: "${context.topicName}"
Syllabus section: "${context.sectionTitle}"

The generated study-note concepts are:
${conceptList}

Question-bank rules:
- Return ONLY valid JSON, with no Markdown fences or HTML.
- Create exactly one or more questions of EACH of these seven types for EACH concept: ${QUESTION_TYPES.join(', ')}.
- Therefore the quiz must contain at least ${content.concepts.length * QUESTION_TYPES.length} questions.
- Every quiz question must use one of the exact concept ids above in concept_id.
- Questions must test the concept rather than merely repeat its title.
- Use original questions, plausible distractors and a useful explanation.
- For assertion_reason, put the assertion and reason in the question and use the standard four answer choices.
- For match_following, put the two lists and code choices in the question and use four code choices.
- For case_based, include a short realistic security/military scenario in the question and four answer choices.
- For fill_blank, provide accepted_answers as a small array of equivalent answers; do not provide options or correct_index.
- For short_answer, provide expected_answer and a concise marking explanation; do not provide options or correct_index.
- Never use a current event unless it is a stable, well-established fact. Do not invent sources or citations.

Timed-test rules:
- Create exactly 10 objective questions in topic_test.
- Use only mcq, assertion_reason, match_following or case_based.
- Each test question must have options, correct_index and explanation.
- Test questions may overlap the concepts but must not copy quiz wording.

Return exactly:
{
  "quiz_questions": [
    {
      "id":"q-001",
      "concept_id":"one-of-the-concept-ids",
      "type":"mcq|assertion_reason|true_false|fill_blank|match_following|case_based|short_answer",
      "question":"question text",
      "options":["option 1","option 2","option 3","option 4"],
      "correct_index":0,
      "accepted_answers":["answer"],
      "expected_answer":"answer",
      "explanation":"why this is correct"
    }
  ],
  "topic_test": [
    {"id":"t-001","concept_id":"concept-id","type":"mcq","question":"...","options":["...","...","...","..."],"correct_index":0,"explanation":"..."}
  ]
}
For each object, include only fields appropriate to its type, but all quiz questions need id, concept_id, type, question and explanation.`;
}

async function generateJson(prompt, ai, validator = null, label = 'response', maxAttempts = 5) {
  let lastError;
  let activePrompt = prompt;
  for (let attempt = 1; attempt <= maxAttempts; attempt += 1) {
    try {
      const response = await ai.models.generateContent({
        model: MODEL,
        contents: activePrompt,
        config: { temperature: 0.25, responseMimeType: 'application/json' }
      });
      if (!response?.text) throw new Error('Gemini returned an empty response');
      const parsed = parseJson(response.text);
      if (validator) {
        try {
          validator(parsed);
        } catch (validationError) {
          const error = new Error(`${label} validation failed: ${validationError.message}`);
          error.isValidationError = true;
          throw error;
        }
      }
      return parsed;
    } catch (error) {
      lastError = error;
      const status = Number(error?.status || error?.code || error?.error?.code || error?.response?.status) || null;
      if ([400, 401, 403].includes(Number(status))) throw error;
      if (attempt < maxAttempts) {
        const isValidationError = error.isValidationError === true;
        const waitMs = isValidationError
          ? Math.min(8000, attempt * 2000)
          : status === 429
            ? 65000
            : Math.min(60000, 8000 * (2 ** (attempt - 1)));
        if (isValidationError) {
          activePrompt = `${prompt}\n\nYour previous response failed validation with this error: ${error.message}\nReturn a complete replacement JSON response. Do not omit any fields. Satisfy every minimum count and keep all study-note explanations and revision entries point-wise.`;
        }
        console.warn(`${label} attempt ${attempt} failed (${status || error.message}); retrying in ${Math.round(waitMs / 1000)}s.`);
        await new Promise((resolve) => setTimeout(resolve, waitMs));
      }
    }
  }
  throw lastError;
}

function escapeHtml(value) {
  return String(value ?? '')
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
}

function inlineText(value) {
  return escapeHtml(value).replace(/\n/g, '<br>');
}

function paragraphs(value) {
  return String(value || '').split(/\n\s*\n/).filter(Boolean)
    .map((part) => `<p>${inlineText(part)}</p>`).join('');
}

function list(items, className = '') {
  return `<ul${className ? ` class="${className}"` : ''}>${(items || []).map((item) => `<li>${inlineText(item)}</li>`).join('')}</ul>`;
}

function renderConcepts(content) {
  return content.concepts.map((concept, index) => `<section class="notes-section" id="concept-${escapeHtml(concept.id)}">
    <div class="concept-number">Concept ${index + 1}</div>
    <h2>${escapeHtml(concept.title)}</h2>
    <p class="lead-concept">${inlineText(concept.lead)}</p>
    <h3>Explanation</h3>${list(concept.explanation_points, 'notes-bullet-list')}
    <h3>Key points</h3>${list(concept.key_points, 'notes-bullet-list')}
    <div class="military-callout"><strong>Examples / applications:</strong>${list(concept.examples, 'notes-bullet-list')}</div>
    <div class="comparison-callout"><strong>Compare:</strong>${list(concept.comparison_points, 'notes-bullet-list')}</div>
    <div class="trap-callout"><strong>Common misconceptions:</strong>${list(concept.common_misconceptions, 'notes-bullet-list')}</div>
    <div class="exam-focus"><strong>Exam focus:</strong>${list(concept.exam_focus_points, 'notes-bullet-list')}</div>
  </section>`).join('\n');
}

function renderRevision(revision) {
  const glossary = revision.glossary.map((item) => `<div class="glossary-item"><strong>${escapeHtml(item.term)}</strong><span>${inlineText(item.definition)}</span></div>`).join('');
  const conceptRevisions = revision.concept_revisions.map((item, index) => `<section class="revision-card-box highlight"><div class="concept-number">Concept ${index + 1}</div><h2>${escapeHtml(item.title)}</h2><h3>Definition and scope</h3>${list(item.definition_points, 'must-remember-list')}<h3>Must remember</h3>${list(item.must_remember, 'must-remember-list')}<h3>Concept-specific exam traps</h3>${list(item.exam_traps, 'must-remember-list')}</section>`).join('');
  const comparisons = revision.comparisons.map((item) => `<div class="revision-comparison"><div><strong>${escapeHtml(item.left)}</strong><span>vs</span><strong>${escapeHtml(item.right)}</strong></div>${list(item.difference_points, 'must-remember-list')}</div>`).join('');
  return `<div class="summary-hero-box"><h2>Rapid revision for ${escapeHtml(revision.title || 'this topic')}</h2><p>Use these facts after completing the notes and before attempting the timed test.</p></div>
    ${conceptRevisions}
    <section class="revision-card-box"><h2>Quick facts</h2>${list(revision.quick_facts, 'must-remember-list')}</section>
    <section class="revision-card-box"><h2>Glossary</h2><div class="glossary-grid">${glossary}</div></section>
    <section class="revision-card-box"><h2>Important distinctions</h2><div class="revision-comparisons">${comparisons}</div></section>
    <section class="revision-card-box"><h2>Memory hooks</h2>${list(revision.memory_hooks, 'must-remember-list')}</section>
    <section class="revision-card-box"><h2>Exam traps and cautions</h2>${list(revision.exam_traps, 'must-remember-list')}</section>`;
}

function renderQuestionSourceData(question) {
  const accepted = (question.accepted_answers || []).map((answer) => `<span class="accepted-answer">${inlineText(answer)}</span>`).join('');
  const expected = question.expected_answer ? `<span class="expected-answer">${inlineText(question.expected_answer)}</span>` : '';
  return `<div class="question-source-data" aria-hidden="true">${accepted}${expected}<p class="question-explanation">${inlineText(question.explanation)}</p></div>`;
}

function renderQuizQuestion(question, index) {
  const typeNames = { mcq: 'MCQ', assertion_reason: 'Assertion–Reason', true_false: 'True / False', fill_blank: 'Fill in the blank', match_following: 'Match the following', case_based: 'Case-based', short_answer: 'Short answer' };
  const letters = ['A', 'B', 'C', 'D', 'E'];
  let answerBody;
  if (question.type === 'fill_blank') {
    answerBody = `<input class="quiz-answer-input" id="quiz-input-${index}" aria-label="Your answer"><button class="quiz-check-btn" data-fill="${index}">Check answer</button>`;
  } else if (question.type === 'short_answer') {
    answerBody = `<textarea class="quiz-answer-textarea" id="quiz-input-${index}" aria-label="Your answer"></textarea><button class="quiz-check-btn" data-short="${index}">Show answer</button>`;
  } else {
    answerBody = `<div class="quiz-options-group">${question.options.map((option, optionIndex) => `<button type="button" class="quiz-option-btn" data-quiz="${index}" data-option="${optionIndex}"><span class="option-letter">${letters[optionIndex]}</span><span class="option-text">${inlineText(option)}</span></button>`).join('')}</div>`;
  }
  const correct = Number.isInteger(question.correct_index) ? ` data-correct="${question.correct_index}"` : '';
  return `<article class="quiz-question-card" id="quiz-card-${index}" data-index="${index}" data-type="${escapeHtml(question.type)}"${correct}>
    <div class="q-header"><span class="q-number">Question ${index + 1}</span><span class="question-type">${escapeHtml(typeNames[question.type] || question.type)}</span></div>
    <p class="q-text">${inlineText(question.question)}</p>${answerBody}${renderQuestionSourceData(question)}<div id="quiz-feedback-${index}"></div>
  </article>`;
}

function renderTestQuestion(question, index) {
  const typeNames = { mcq: 'MCQ', assertion_reason: 'Assertion–Reason', match_following: 'Match the following', case_based: 'Case-based' };
  const letters = ['A', 'B', 'C', 'D', 'E'];
  return `<article class="test-question-card" id="test-card-${index}" data-index="${index}" data-correct="${question.correct_index}">
    <div class="test-q-header"><span class="t-badge">Question ${index + 1}</span><span class="question-type">${escapeHtml(typeNames[question.type] || question.type)}</span></div>
    <p class="test-question-text">${inlineText(question.question)}</p>
    <div class="quiz-options-group">${question.options.map((option, optionIndex) => `<button type="button" class="test-option-btn quiz-option-btn" data-test="${index}" data-option="${optionIndex}"><span class="option-letter">${letters[optionIndex]}</span><span class="option-text">${inlineText(option)}</span></button>`).join('')}</div>
    ${renderQuestionSourceData(question)}<div id="test-feedback-${index}"></div>
  </article>`;
}

function safeJson(data) {
  return JSON.stringify(data).replace(/</g, '\\u003c').replace(/>/g, '\\u003e').replace(/&/g, '\\u0026');
}

function compileHtml(content, questions, context) {
  const canonical = `https://sjmaths.com${context.url}`;
  const description = `${content.short_title || context.topicName}: structured Military Science study notes, concept quiz, revision summary and timed topic test for UP PGT preparation.`;
  return `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>${escapeHtml(content.title)} | Military Science | SJ Maths</title>
<meta name="description" content="${escapeHtml(description)}">
<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1">
<meta name="author" content="SJ Maths">
<meta name="theme-color" content="#16324f">
<link rel="canonical" href="${canonical}">
<link rel="icon" type="image/png" href="/favicon.png">
<meta property="og:type" content="article">
<meta property="og:site_name" content="SJ Maths">
<meta property="og:title" content="${escapeHtml(content.title)} | Military Science">
<meta property="og:description" content="${escapeHtml(description)}">
<meta property="og:url" content="${canonical}">
<meta property="og:image" content="https://sjmaths.com/assets/images/og-default.jpg">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="${escapeHtml(content.title)} | Military Science">
<meta name="twitter:description" content="${escapeHtml(description)}">
<script type="application/ld+json">${safeJson({
    '@context': 'https://schema.org',
    '@type': 'LearningResource',
    name: content.title,
    headline: content.title,
    description,
    url: canonical,
    educationalLevel: 'UP PGT',
    learningResourceType: 'Study guide',
    isPartOf: { '@type': 'WebSite', name: 'SJ Maths', url: 'https://sjmaths.com/' }
  })}</script>
<link rel="stylesheet" href="/assets/css/topic-page.min.css?v=718ef3ff">
<style>
:root{--brand:#16324f;--brand-dark:#0f2439;--brand-light:#2c587f;--accent:#b45309;--accent-hover:#92400e;--accent-soft:rgba(180,83,9,.09);--accent-border:rgba(180,83,9,.26)}
body{background:radial-gradient(circle at 100% 0,rgba(180,83,9,.06),transparent 28rem),var(--bg,#f6f8fb)}
.study-tabs{grid-template-columns:repeat(4,minmax(0,1fr))}.tab-btn{min-height:54px}.tab-panel.hidden,.question-source-data,.hidden{display:none!important}.concept-number{display:inline-block;margin-bottom:8px;color:var(--accent);font-size:.74rem;font-weight:900;text-transform:uppercase;letter-spacing:.08em}.lead-concept{font-weight:700;color:var(--brand);font-size:1rem}.notes-section h3{margin-top:18px;color:var(--brand);font-size:1rem}.military-callout,.comparison-callout,.trap-callout,.exam-focus{padding:14px 16px;border-radius:10px;margin:14px 0;line-height:1.6}.military-callout{background:#eff6ff;border-left:4px solid #2563eb}.comparison-callout{background:#f0fdf4;border-left:4px solid #15803d}.trap-callout{background:#fffbeb;border-left:4px solid #d97706}.exam-focus{background:var(--accent-soft);border-left:4px solid var(--accent);color:var(--ink2)}.question-type{display:inline-flex;padding:3px 9px;border-radius:999px;background:var(--accent-soft);color:var(--accent);font-size:.72rem;font-weight:850;text-transform:uppercase;letter-spacing:.04em}.quiz-answer-input,.quiz-answer-textarea{width:100%;padding:11px 13px;border:1px solid var(--line);border-radius:9px;background:var(--paper);color:var(--ink);font:inherit}.quiz-answer-textarea{min-height:96px;resize:vertical}.quiz-check-btn{margin-top:10px;padding:9px 14px;border:0;border-radius:8px;background:var(--brand);color:#fff;font-weight:800;cursor:pointer}.quiz-feedback{margin-top:13px}.revision-comparisons{display:flex;flex-direction:column;gap:12px}.revision-comparison{padding:14px 16px;border:1px solid var(--line);border-radius:10px;background:var(--paper-card)}.revision-comparison>div{display:flex;gap:9px;align-items:center;flex-wrap:wrap;color:var(--brand)}.revision-comparison span{color:var(--muted);font-size:.78rem}.revision-comparison p{margin:8px 0 0;color:var(--ink2);line-height:1.55}.test-question-card .test-option-btn{width:100%;text-align:left}.quiz-question-card[data-answered="true"]{border-color:var(--accent-border)}
@media(max-width:680px){.study-tabs{grid-template-columns:repeat(2,minmax(0,1fr))}.tab-btn{font-size:.78rem}.tab-btn span:first-child{display:none}}
</style>
</head>
<body>
<header class="site-header"><div class="wrap header-inner">
  <a class="brand" href="https://sjmaths.com/"><span class="brand-mark" style="background:linear-gradient(145deg,#16324f,#b45309);font-family:serif;font-size:1.35rem;font-style:italic;display:flex;align-items:center;justify-content:center">&int;</span><span><span class="brand-name">SJ Maths</span><span class="brand-sub">Military Science</span></span></a>
  <div class="header-actions"><button type="button" class="theme-toggle-btn" id="btn-theme-toggle" aria-label="Toggle dark mode">Dark Mode</button><a class="back-btn" href="/up-pgt-military-science/">← UP PGT Military Science</a></div>
</div></header>
<main class="wrap">
  <section class="hero"><nav class="breadcrumb" aria-label="Breadcrumb"><a href="https://sjmaths.com/">Home</a><span>›</span><a href="/up-pgt-military-science/">Military Science</a><span>›</span><span>${escapeHtml(context.sectionTitle)}</span><span>›</span><span aria-current="page">${escapeHtml(content.short_title || context.topicName)}</span></nav>
    <div class="kicker">${escapeHtml(context.sectionTitle)}</div><h1>${escapeHtml(content.title)}</h1><p class="lead">${escapeHtml(content.introduction_points[0])}</p>
    <div class="exam-badges"><a class="exam-chip pgt" href="/up-pgt-military-science/">UP PGT Military Science</a><span class="exam-chip both">${content.concepts.length} concepts</span><span class="exam-chip both">${questions.quiz_questions.length} quiz questions</span><span class="exam-chip both">10-question test</span></div>
  </section>
  <div class="study-tabs-sticky-wrapper"><div class="study-tabs" role="tablist" aria-label="Military Science study tabs">
    <button type="button" class="tab-btn active" role="tab" aria-selected="true" data-tab="tab-notes" id="tab-btn-notes"><span>📖</span><span>Study Notes</span></button>
    <button type="button" class="tab-btn" role="tab" aria-selected="false" data-tab="tab-quiz" id="tab-btn-quiz"><span>❓</span><span>Concept Quiz</span><span class="tab-badge">${questions.quiz_questions.length}Q</span></button>
    <button type="button" class="tab-btn" role="tab" aria-selected="false" data-tab="tab-summary" id="tab-btn-summary"><span>⚡</span><span>Revision Summary</span></button>
    <button type="button" class="tab-btn" role="tab" aria-selected="false" data-tab="tab-test" id="tab-btn-test"><span>⏱️</span><span>Topic Test</span><span class="tab-badge">10Q</span></button>
  </div></div>
  <div class="main-grid"><div class="content-col">
    <article class="tab-panel active" id="tab-notes" role="tabpanel" aria-labelledby="tab-btn-notes"><div class="card"><h2>Topic overview</h2>${list(content.introduction_points, 'notes-bullet-list')}</div>${renderConcepts(content)}<nav class="topic-pagination" aria-label="Topic navigation"><a class="topic-nav-btn next" href="/up-pgt-military-science/"><span>Exam Tracker →</span><strong>UP PGT Military Science</strong></a></nav></article>
    <article class="tab-panel hidden" id="tab-quiz" role="tabpanel" aria-labelledby="tab-btn-quiz"><div class="quiz-panel-header"><div class="quiz-panel-title"><h2>Concept Quiz</h2><p>Questions are grouped across every concept and include all seven question formats.</p></div><div class="quiz-live-scoreboard"><span class="score-pill" id="quiz-score">Score: 0 / ${questions.quiz_questions.length}</span><button type="button" class="btn-reset-quiz" id="btn-reset-quiz">Reset</button></div></div><div class="quiz-questions-list" id="quiz-container">${questions.quiz_questions.map(renderQuizQuestion).join('')}</div></article>
    <article class="tab-panel hidden" id="tab-summary" role="tabpanel" aria-labelledby="tab-btn-summary"><div class="summary-container">${renderRevision({ ...content.revision, title: content.short_title || context.topicName })}</div></article>
    <article class="tab-panel hidden" id="tab-test" role="tabpanel" aria-labelledby="tab-btn-test"><div class="test-panel-header"><div><h2>Timed Topic Test</h2><p>Ten objective questions. The timer starts when you open this tab.</p></div><span class="test-timer-badge" id="test-timer">10:00</span></div><div class="test-questions-list" id="test-container">${questions.topic_test.map(renderTestQuestion).join('')}</div><div class="test-submit-bar"><button type="button" class="btn-submit-test" id="btn-submit-test">Submit Test</button></div><div class="test-result-modal hidden" id="test-result"><div class="result-card"><h3>Test Result</h3><div class="result-score-circle"><span id="test-score">0</span> / 10</div><p id="test-feedback">Review the explanations and retry when ready.</p><button type="button" class="btn-retake-test" id="btn-retake-test">Retake Test</button></div></div></article>
  </div><aside class="sidebar-col"><div class="sidebar-card side-card"><div class="side-card-header"><span class="side-badge">Syllabus section</span><h3>${escapeHtml(context.sectionTitle)}</h3></div><p class="side-desc">Study notes, concept coverage, rapid revision and a timed test for this Military Science topic.</p><div class="side-action-box" style="margin-top:1.5rem"><a class="side-action-btn" href="/up-pgt-military-science/" style="background:#16324f;display:block;text-align:center;padding:10px;color:#fff;border-radius:8px;font-weight:600">Full Military Science Tracker →</a></div></div></aside></div>
</main>
<footer class="site-footer"><div class="wrap footer-inner"><div><p><strong>SJ Maths — Military Science</strong></p><p>Structured preparation for UP PGT Military Science.</p></div><div class="footer-links"><a href="https://sjmaths.com/">Home</a><a href="/up-pgt-military-science/">UP PGT Military Science</a></div></div></footer>
<script type="application/json" id="quiz-data">${safeJson(questions.quiz_questions)}</script>
<script type="application/json" id="test-data">${safeJson(questions.topic_test)}</script>
<script>
document.addEventListener('DOMContentLoaded',()=>{
  const esc=(value)=>String(value??'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#39;');
  const quiz=JSON.parse(document.getElementById('quiz-data').textContent); const test=JSON.parse(document.getElementById('test-data').textContent);
  const typeNames={mcq:'MCQ',assertion_reason:'Assertion–Reason',true_false:'True / False',fill_blank:'Fill in the blank',match_following:'Match the following',case_based:'Case-based',short_answer:'Short answer'};
  const letters=['A','B','C','D','E']; let quizScore=0; const answered=new Set();
  const feedback=(correct,explanation)=>'<div class="quiz-feedback '+(correct?'correct':'incorrect')+'"><strong>'+(correct?'✓ Correct':'✕ Review')+'</strong><p>'+esc(explanation)+'</p></div>';
  function quizCard(q,index){
    const options=q.options||[]; let body='';
    if(q.type==='fill_blank') body='<input class="quiz-answer-input" id="quiz-input-'+index+'" aria-label="Your answer"><button class="quiz-check-btn" data-fill="'+index+'">Check answer</button>';
    else if(q.type==='short_answer') body='<textarea class="quiz-answer-textarea" id="quiz-input-'+index+'" aria-label="Your answer"></textarea><button class="quiz-check-btn" data-short="'+index+'">Show answer</button>';
    else body='<div class="quiz-options-group">'+options.map((o,i)=>'<button type="button" class="quiz-option-btn" data-quiz="'+index+'" data-option="'+i+'"><span class="option-letter">'+letters[i]+'</span><span class="option-text">'+esc(o)+'</span></button>').join('')+'</div>';
    return '<article class="quiz-question-card" id="quiz-card-'+index+'"><div class="q-header"><span class="q-number">Question '+(index+1)+'</span><span class="question-type">'+esc(typeNames[q.type]||q.type)+'</span></div><p class="q-text">'+esc(q.question)+'</p>'+body+'<div id="quiz-feedback-'+index+'"></div></article>';
  }
  function renderQuiz(){const container=document.getElementById('quiz-container');if(!container.children.length)container.innerHTML=quiz.map(quizCard).join('');}
  function markQuiz(index,correct,answer){if(answered.has(index))return; answered.add(index); if(correct)quizScore++; const card=document.getElementById('quiz-card-'+index); card.dataset.answered='true'; card.querySelectorAll('button').forEach(b=>b.disabled=true); document.getElementById('quiz-feedback-'+index).innerHTML=feedback(correct,answer); document.getElementById('quiz-score').textContent='Score: '+quizScore+' / '+quiz.length;}
  function bindQuiz(){document.querySelectorAll('[data-quiz]').forEach(btn=>btn.addEventListener('click',()=>{const i=Number(btn.dataset.quiz),o=Number(btn.dataset.option),q=quiz[i]; document.querySelectorAll('#quiz-card-'+i+' [data-option]').forEach((b,n)=>{b.disabled=true;if(n===q.correct_index)b.classList.add('correct');if(n===o&&o!==q.correct_index)b.classList.add('incorrect');});markQuiz(i,o===q.correct_index,q.explanation);})); document.querySelectorAll('[data-fill]').forEach(btn=>btn.addEventListener('click',()=>{const i=Number(btn.dataset.fill),q=quiz[i],value=document.getElementById('quiz-input-'+i).value.trim().toLowerCase();markQuiz(i,q.accepted_answers.some(a=>value===String(a).trim().toLowerCase()),'Accepted answer(s): '+q.accepted_answers.join(', ')+' — '+q.explanation);})); document.querySelectorAll('[data-short]').forEach(btn=>btn.addEventListener('click',()=>{const i=Number(btn.dataset.short),q=quiz[i];markQuiz(i,false,'Expected answer: '+q.expected_answer+' — '+q.explanation);}));}
  function resetQuiz(){location.reload();}
  renderQuiz();bindQuiz();document.getElementById('btn-reset-quiz').addEventListener('click',resetQuiz);
  const testContainer=document.getElementById('test-container'); let chosen={}; let submitted=false;
  if(!testContainer.children.length)testContainer.innerHTML=test.map((q,i)=>'<article class="test-question-card" id="test-card-'+i+'"><div class="test-q-header"><span class="t-badge">Question '+(i+1)+'</span><span class="question-type">'+esc(typeNames[q.type]||q.type)+'</span></div><p class="test-question-text">'+esc(q.question)+'</p><div class="quiz-options-group">'+q.options.map((o,n)=>'<button type="button" class="test-option-btn quiz-option-btn" data-test="'+i+'" data-option="'+n+'"><span class="option-letter">'+letters[n]+'</span><span class="option-text">'+esc(o)+'</span></button>').join('')+'</div><div id="test-feedback-'+i+'"></div></article>').join('');
  document.querySelectorAll('[data-test]').forEach(btn=>btn.addEventListener('click',()=>{if(submitted)return;const i=Number(btn.dataset.test);chosen[i]=Number(btn.dataset.option);document.querySelectorAll('#test-card-'+i+' [data-option]').forEach(b=>b.classList.remove('selected'));btn.classList.add('selected');}));
  function submitTest(){if(submitted)return;submitted=true;let score=0;test.forEach((q,i)=>{const answer=chosen[i];if(answer===q.correct_index)score++;document.querySelectorAll('#test-card-'+i+' [data-option]').forEach((b,n)=>{b.disabled=true;if(n===q.correct_index)b.classList.add('correct');if(n===answer&&answer!==q.correct_index)b.classList.add('incorrect');});document.getElementById('test-feedback-'+i).innerHTML=feedback(answer===q.correct_index,q.explanation);});document.getElementById('test-score').textContent=score;document.getElementById('test-result').classList.remove('hidden');document.getElementById('btn-submit-test').classList.add('hidden');}
  document.getElementById('btn-submit-test').addEventListener('click',submitTest);document.getElementById('btn-retake-test').addEventListener('click',()=>location.reload());
  let timer=null,remaining=600;function startTimer(){if(timer||submitted)return;timer=setInterval(()=>{remaining--;document.getElementById('test-timer').textContent=String(Math.floor(remaining/60)).padStart(2,'0')+':'+String(remaining%60).padStart(2,'0');if(remaining<=0){clearInterval(timer);submitTest();}},1000);}
  const tabs=document.querySelectorAll('.tab-btn'),panels=document.querySelectorAll('.tab-panel');tabs.forEach(btn=>btn.addEventListener('click',()=>{tabs.forEach(b=>{b.classList.remove('active');b.setAttribute('aria-selected','false');});panels.forEach(p=>{p.classList.remove('active');p.classList.add('hidden');});btn.classList.add('active');btn.setAttribute('aria-selected','true');document.getElementById(btn.dataset.tab).classList.remove('hidden');document.getElementById(btn.dataset.tab).classList.add('active');if(btn.dataset.tab==='tab-test')startTimer();window.scrollTo({top:document.querySelector('.study-tabs-sticky-wrapper').offsetTop-15,behavior:'smooth'});}));
  const theme=document.getElementById('btn-theme-toggle');const saved=localStorage.getItem('sjmaths_theme')||localStorage.getItem('sj_theme');if(saved==='dark'){document.body.classList.add('dark-mode');document.documentElement.classList.add('dark');theme.textContent='Light Mode';}theme.addEventListener('click',()=>{const dark=document.body.classList.toggle('dark-mode');document.documentElement.classList.toggle('dark',dark);localStorage.setItem('sjmaths_theme',dark?'dark':'light');localStorage.setItem('sj_theme',dark?'dark':'light');theme.textContent=dark?'Light Mode':'Dark Mode';});
});
</script>
</body></html>`;
}

async function processTopic(url, contexts, ai, status) {
  const context = contexts.get(url) || (() => {
    const parts = url.split('/').filter(Boolean); const slug = parts.at(-1);
    return { url, topicName: titleFromSlug(slug), sectionTitle: titleFromSlug(parts[1] || 'Military Science'), key: parts.slice(1).join('/') };
  })();
  const targetDir = urlToDir(url); const indexPath = path.join(targetDir, 'index.html');
  if (!force && fs.existsSync(indexPath)) {
    console.log(`Skipped ${url} (index.html already generated; use --force to regenerate)`); return;
  }
  console.log(`\nGenerating ${url} — ${context.topicName}`);
  status[url] = { status: 'generating', model: MODEL, startedAt: new Date().toISOString() }; writeStatus(status);
  const content = await generateJson(buildContentPrompt(context), ai, validateContent, 'Study notes');
  console.log(`  ✓ study notes: ${content.concepts.length} concepts`);
  if (gapMs) await new Promise((resolve) => setTimeout(resolve, gapMs));
  const conceptIds = content.concepts.map((concept) => concept.id);
  const questions = await generateJson(buildQuestionsPrompt(context, content), ai, (result) => validateQuestions(result, conceptIds), 'Quiz and test');
  console.log(`  ✓ quiz: ${questions.quiz_questions.length} questions; test: ${questions.topic_test.length} questions`);
  fs.mkdirSync(targetDir, { recursive: true });
  fs.writeFileSync(indexPath, compileHtml(content, questions, context), 'utf8');
  status[url] = { status: 'completed', model: MODEL, title: content.title, concepts: content.concepts.length, quizQuestions: questions.quiz_questions.length, testQuestions: 10, completedAt: new Date().toISOString() }; writeStatus(status);
  console.log(`  ✓ wrote ${indexPath}`);
}

async function main() {
  const contexts = readTrackerContexts(); const targets = resolveTargets(contexts);
  console.log(`Discovered ${targets.length} Military Science topic page(s). Model: ${MODEL}`);
  if (dryRun) { targets.forEach((url) => console.log(`${url} — ${contexts.get(url)?.topicName || 'title not found in tracker'}`)); return; }
  const apiKey = process.env.GEMINI_API_KEY || process.env.GOOGLE_API_KEY;
  if (!apiKey) throw new Error('Set GEMINI_API_KEY or GOOGLE_API_KEY before generation.');
  const ai = new GoogleGenAI({ apiKey }); const status = readStatus();
  for (const url of targets) { try { await processTopic(url, contexts, ai, status); } catch (error) { status[url] = { status: 'failed', model: MODEL, error: error.message, failedAt: new Date().toISOString() }; writeStatus(status); console.error(`  ✗ ${url}: ${error.message}`); if (requestedTopic) throw error; } }
}

main().catch((error) => { console.error(`Generation failed: ${error.message}`); process.exitCode = 1; });
