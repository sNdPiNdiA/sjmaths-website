#!/usr/bin/env node
/**
 * SJ Maths History Topic Content Generator
 * Generates point-wise, high-yield study notes, key concepts, quick revision,
 * self-assessment checklist, and exam PYQ facts for history pages using Gemini 3.5 Flash Lite.
 *
 * Usage:
 *   node scripts/generate_history.mjs --dry-run
 *   node scripts/generate_history.mjs --topic ancient-india/religious-movements/bhagvatism
 *   node scripts/generate_history.mjs --limit 5
 *   node scripts/generate_history.mjs --all
 *   node scripts/generate_history.mjs --concurrency 2 --max-attempts 1 --gap 0
 */

import fs from 'node:fs';
import path from 'node:path';
import 'dotenv/config';
import { GoogleGenAI } from '@google/genai';
import { jsonrepair } from 'jsonrepair';
import * as cheerio from 'cheerio';

const ROOT = process.cwd();
const HISTORY_ROOT = path.join(ROOT, 'history');
const STATUS_PATH = path.join(ROOT, 'content-generation-status-history.json');
const MODEL = process.env.GEMINI_MODEL || 'gemini-3.5-flash-lite';
const TAB_VERSION = 'history-tabs-v1';
const QUESTION_TYPES = ['mcq', 'assertion_reason', 'true_false', 'fill_blank', 'match_following', 'case_based', 'short_answer'];

// API Key rotation / fallback support
const API_KEYS = [
  process.env.GEMINI_API_KEY_1,
  process.env.GEMINI_API_KEY_2,
  process.env.GEMINI_API_KEY
].filter(Boolean);

let keyIndex = 0;
function getAIClient() {
  const key = API_KEYS[keyIndex++ % API_KEYS.length];
  return new GoogleGenAI({ apiKey: key });
}

function rotateKey() {
  console.log(`Rotating API key after a quota/rate-limit response (next request index: ${keyIndex})`);
}

const args = process.argv.slice(2);
const hasFlag = (f) => args.includes(f);
function getArg(flag) {
  const i = args.indexOf(flag);
  return i >= 0 ? args[i + 1] : null;
}

const requestedTopic = getArg('--topic');
const requestedLimit = getArg('--limit') ? parseInt(getArg('--limit'), 10) : 0;
const dryRun = hasFlag('--dry-run');
const force = hasFlag('--force');
const allFlag = hasFlag('--all');
const gapMs = Math.max(0, parseInt(getArg('--gap') || '0', 10)) * 1000;
const concurrency = Math.max(1, parseInt(getArg('--concurrency') || '2', 10));
const retryAttempts = Math.max(1, parseInt(getArg('--max-attempts') || '1', 10));
const retryDelayMs = Math.max(0, parseInt(getArg('--retry-delay') || '1000', 10));

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

function formatApiError(error) {
  const causes = Array.isArray(error?.cause?.errors)
    ? error.cause.errors.map((item) => item?.code).filter(Boolean).join(', ')
    : '';
  return causes ? `${error.message} (${causes})` : error.message;
}

async function assertGeminiReachable() {
  try {
    await fetch('https://generativelanguage.googleapis.com', {
      method: 'HEAD',
      signal: AbortSignal.timeout(5000)
    });
  } catch (error) {
    throw new Error(`Cannot reach generativelanguage.googleapis.com from this terminal: ${formatApiError(error)}. Check network/firewall permissions or run the command outside the restricted terminal.`);
  }
}

function readStatus() {
  if (!fs.existsSync(STATUS_PATH)) return {};
  try {
    return JSON.parse(fs.readFileSync(STATUS_PATH, 'utf8'));
  } catch {
    return {};
  }
}

function writeStatus(status) {
  try {
    fs.writeFileSync(STATUS_PATH, JSON.stringify(status, null, 2) + '\n', 'utf8');
  } catch (err) {
    console.warn('Warning: Could not update status log:', err.message);
  }
}

function escapeHtml(str) {
  return String(str || '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

function discoverHistoryPages(dir) {
  let results = [];
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      results = results.concat(discoverHistoryPages(fullPath));
    } else if (entry.name === 'index.html') {
      const relPath = path.relative(HISTORY_ROOT, fullPath).replace(/\\/g, '/');
      results.push({
        fullPath,
        relPath, // e.g. "ancient-india/religious-movements/bhagvatism/index.html"
        topicDir: path.dirname(relPath)
      });
    }
  }
  return results;
}

function isPlaceholderContent(html) {
  return !html.includes(`data-history-tabs="${TAB_VERSION}"`);
}

function buildLegacyPrompt(metadata) {
  return `You are a distinguished Professor of History and Subject Expert for Indian competitive exams (UP TGT Social Science, UP PGT History, UPSC, State PCS, UGC NET).

Create comprehensive, accurate, high-yield STUDY NOTES for the following topic:
- Topic Title: "${metadata.title}"
- Breadcrumb / Section: "${metadata.breadcrumb}"
- Hierarchy Context: "${metadata.kicker}"
- Target Exam Audience: UP TGT Social Science / UP PGT History / Competitive Exams

IMPORTANT FORMATTING RULES:
1. All study notes MUST be POINT-WISE (bullet points). NEVER produce long walls of text or paragraphs.
2. Every point should begin with a bold keyword or sub-concept (e.g., "• <strong>Origins & Sources:</strong> ...").
3. Include specific names, dates, archaeological sites, literary sources, inscriptions, rulers, and architectural or socio-economic facts.
4. Keep the content academically rigorous and verified.
5. Provide the output in RAW JSON format only (no markdown fencing, no preamble).

JSON SCHEMA REQUIRED:
{
  "syllabus_focus_points": [
    "High-yield syllabus focus point 1",
    "High-yield syllabus focus point 2",
    "High-yield syllabus focus point 3",
    "High-yield syllabus focus point 4"
  ],
  "study_sections": [
    {
      "heading": "Section Heading (e.g., Historical Background & Sources)",
      "points": [
        "Point 1 with <strong>Bold Keyword</strong>: Clear, factual note",
        "Point 2 with <strong>Bold Keyword</strong>: Clear, factual note",
        "Point 3 with <strong>Bold Keyword</strong>: Clear, factual note",
        "Point 4 with <strong>Bold Keyword</strong>: Clear, factual note"
      ]
    },
    {
      "heading": "Section Heading (e.g., Core Principles, Beliefs & Developments)",
      "points": [
        "Point 1 with <strong>Bold Keyword</strong>: Detailed factual point",
        "Point 2 with <strong>Bold Keyword</strong>: Detailed factual point",
        "Point 3 with <strong>Bold Keyword</strong>: Detailed factual point",
        "Point 4 with <strong>Bold Keyword</strong>: Detailed factual point"
      ]
    },
    {
      "heading": "Section Heading (e.g., Significant Figures, Sites & Chronology)",
      "points": [
        "Point 1 with <strong>Bold Keyword</strong>: Specific names, sites, or dates",
        "Point 2 with <strong>Bold Keyword</strong>: Specific names, sites, or dates",
        "Point 3 with <strong>Bold Keyword</strong>: Specific names, sites, or dates",
        "Point 4 with <strong>Bold Keyword</strong>: Specific names, sites, or dates"
      ]
    },
    {
      "heading": "Section Heading (e.g., Impact, Legacy & Historiography)",
      "points": [
        "Point 1 with <strong>Bold Keyword</strong>: Analysis, legacy, or historical significance",
        "Point 2 with <strong>Bold Keyword</strong>: Analysis, legacy, or historical significance",
        "Point 3 with <strong>Bold Keyword</strong>: Analysis, legacy, or historical significance",
        "Point 4 with <strong>Bold Keyword</strong>: Analysis, legacy, or historical significance"
      ]
    }
  ],
  "key_facts_revision": [
    "Essential fact 1 frequently asked in exam papers",
    "Essential fact 2 frequently asked in exam papers",
    "Essential fact 3 frequently asked in exam papers",
    "Essential fact 4 frequently asked in exam papers",
    "Essential fact 5 frequently asked in exam papers",
    "Essential fact 6 frequently asked in exam papers"
  ],
  "exam_traps_and_distinctions": [
    "Common misconception or exam trap to avoid 1",
    "Common misconception or exam trap to avoid 2",
    "Common misconception or exam trap to avoid 3"
  ],
  "interactive_checklist": [
    "Checklist item 1 specific to this topic",
    "Checklist item 2 specific to this topic",
    "Checklist item 3 specific to this topic",
    "Checklist item 4 specific to this topic",
    "Checklist item 5 specific to this topic"
  ]
}`;
}

function buildContentPrompt(metadata) {
  return `You are a distinguished Professor of Indian History and an examiner for UP TGT Social Science, UP PGT History, UPSC, State PCS and UGC NET.

Create accurate, comprehensive and exam-oriented study material for:
- Topic title: "${metadata.title}"
- Breadcrumb / section: "${metadata.breadcrumb}"
- Curriculum context: "${metadata.kicker}"

The first tab is detailed study notes. Keep every explanation point-wise: use short standalone points, one idea per point, and never write long prose paragraphs. Include names, dates, sources, inscriptions, sites, rulers, movements, causes, chronology, impact and historiographical distinctions wherever relevant. Do not invent facts.

Return ONLY valid JSON. Do not use Markdown fences, HTML tags, citations or a preamble. Use plain text strings and normal Unicode.

Return exactly this shape:
{
  "introduction_points": ["at least 4 point-wise overview points"],
  "concepts": [
    {
      "id": "stable-kebab-case-id",
      "title": "Concept heading",
      "lead": "One concise central idea",
      "explanation_points": ["at least 5 detailed point-wise explanations"],
      "key_points": ["at least 4 precise facts or relationships"],
      "examples": ["at least 2 specific historical examples"],
      "comparison_points": ["at least 2 point-wise comparisons or distinctions"],
      "common_misconceptions": ["at least 2 exam misconceptions"],
      "exam_focus_points": ["at least 3 likely exam targets"]
    }
  ]
}

Generate 5 to 7 materially different concepts. Every concept must be covered in detail; do not merge concepts.`;
}

function buildQuestionsPrompt(metadata, content) {
  const conceptList = content.concepts.map((concept) => `- ${concept.id}: ${concept.title} — ${concept.lead}`).join('\n');
  return `You are the chief examiner for Indian History competitive examinations.
Create the concept quiz for:
- Topic: "${metadata.title}"
- Section: "${metadata.breadcrumb}"

The detailed study-note concepts are:
${conceptList}

Quiz rules:
- Return ONLY valid JSON, with no Markdown fences, HTML or preamble.
- Create exactly 35 quiz questions, covering every concept at least 4 times.
- Use all seven question types at least once: ${QUESTION_TYPES.join(', ')}.
- Every question must use one of the exact concept ids above.
- Use original, exam-relevant questions with plausible distractors and a useful explanation.
- For assertion_reason, include assertion and reason in the question and use four answer choices.
- For match_following, include the lists and code choices in the question.
- For fill_blank, provide accepted_answers and no options or correct_index.
- For short_answer, provide expected_answer and no options or correct_index.

Return exactly:
{
  "quiz_questions": [{
    "id":"q-001",
    "concept_id":"one-of-the-concept-ids",
    "type":"mcq|assertion_reason|true_false|fill_blank|match_following|case_based|short_answer",
    "question":"question text",
    "options":["option 1","option 2","option 3","option 4"],
    "correct_index":0,
    "accepted_answers":["answer"],
    "expected_answer":"answer",
    "explanation":"why this is correct"
  }]
}
Include only fields appropriate to each question type. Do not return topic_test or any other fields.`;
}

function buildRevisionTestPrompt(metadata, content) {
  const conceptList = content.concepts.map((concept) => `- ${concept.id}: ${concept.title} — ${concept.lead}`).join('\n');
  return `You are an expert revision coach and examiner for Indian History competitive examinations.
Create the revision summary and 10-question mini test for:
- Topic: "${metadata.title}"
- Section: "${metadata.breadcrumb}"

Base the response only on these study-note concepts:
${conceptList}

Return ONLY valid JSON, with no Markdown fences, HTML or preamble.
Revision rules:
- Create one concept_revisions entry for every concept id, with exact matching concept_id values.
- Keep every revision item point-wise and useful for rapid recall.
- Include mnemonics, tips, tricks, comparisons and exam traps.

Mini-test rules:
- Create exactly 10 objective questions in topic_test.
- Use only mcq, assertion_reason, true_false, match_following or case_based.
- Each test question must include options, correct_index and explanation.
- Do not copy quiz wording; make the test application-oriented.

Return exactly:
{
  "revision": {
    "concept_revisions": [{
      "concept_id":"exact-concept-id",
      "title":"concept title",
      "pointwise_summary":["at least 4 rapid-recall points"],
      "mnemonics":["at least 1 useful mnemonic"],
      "tips":["at least 1 study or recall tip"],
      "tricks":["at least 1 exam-solving trick"],
      "common_traps":["at least 1 concept-specific trap"]
    }],
    "quick_facts":["at least 8 rapid-recall facts"],
    "mnemonics":["at least 3 topic-level mnemonics"],
    "tips":["at least 4 revision tips"],
    "tricks":["at least 4 exam tricks"],
    "comparisons":[{"left":"concept A","right":"concept B","difference_points":["at least 3 distinctions"]}],
    "exam_traps":["at least 5 common traps or cautions"]
  },
  "topic_test":[{"id":"t-001","concept_id":"concept-id","type":"mcq","question":"...","options":["...","...","...","..."],"correct_index":0,"explanation":"..."}]
}
Return exactly one revision object and ten test questions.`;
}

function requireText(value, label) {
  if (typeof value !== 'string' || !value.trim()) throw new Error(`${label} must be a non-empty string`);
}

function requireTextArray(value, label, minimum) {
  if (!Array.isArray(value) || value.length < minimum) throw new Error(`${label} needs at least ${minimum} items`);
  value.forEach((item, index) => requireText(item, `${label}[${index}]`));
}

function validateContent(data) {
  if (!data || !Array.isArray(data.concepts) || data.concepts.length < 5 || data.concepts.length > 7) {
    throw new Error('Content must contain 5 to 7 concepts');
  }
  requireTextArray(data.introduction_points, 'introduction_points', 4);
  const ids = new Set();
  for (const [index, concept] of data.concepts.entries()) {
    requireText(concept.id, `concept ${index + 1} id`);
    requireText(concept.title, `concept ${index + 1} title`);
    requireText(concept.lead, `concept ${concept.id} lead`);
    if (ids.has(concept.id)) throw new Error(`Duplicate concept id: ${concept.id}`);
    ids.add(concept.id);
    requireTextArray(concept.explanation_points, `concept ${concept.id} explanation_points`, 5);
    requireTextArray(concept.key_points, `concept ${concept.id} key_points`, 4);
    requireTextArray(concept.examples, `concept ${concept.id} examples`, 2);
    requireTextArray(concept.comparison_points, `concept ${concept.id} comparison_points`, 2);
    requireTextArray(concept.common_misconceptions, `concept ${concept.id} common_misconceptions`, 2);
    requireTextArray(concept.exam_focus_points, `concept ${concept.id} exam_focus_points`, 3);
  }
  return data;
}

function validateRevision(revision, conceptIds) {
  if (!revision || !Array.isArray(revision.concept_revisions) || revision.concept_revisions.length !== conceptIds.length) {
    throw new Error('Revision must contain one entry for every concept');
  }
  const revisionIds = new Set();
  for (const revisionItem of revision.concept_revisions) {
    requireText(revisionItem.concept_id, 'revision concept_id');
    if (!conceptIds.includes(revisionItem.concept_id)) throw new Error(`Revision references unknown concept ${revisionItem.concept_id}`);
    if (revisionIds.has(revisionItem.concept_id)) throw new Error(`Duplicate revision concept ${revisionItem.concept_id}`);
    revisionIds.add(revisionItem.concept_id);
    requireText(revisionItem.title, `revision ${revisionItem.concept_id} title`);
    requireTextArray(revisionItem.pointwise_summary, `revision ${revisionItem.concept_id} pointwise_summary`, 4);
    requireTextArray(revisionItem.mnemonics, `revision ${revisionItem.concept_id} mnemonics`, 1);
    requireTextArray(revisionItem.tips, `revision ${revisionItem.concept_id} tips`, 1);
    requireTextArray(revisionItem.tricks, `revision ${revisionItem.concept_id} tricks`, 1);
    requireTextArray(revisionItem.common_traps, `revision ${revisionItem.concept_id} common_traps`, 1);
  }
  requireTextArray(revision.quick_facts, 'revision.quick_facts', 8);
  requireTextArray(revision.mnemonics, 'revision.mnemonics', 3);
  requireTextArray(revision.tips, 'revision.tips', 4);
  requireTextArray(revision.tricks, 'revision.tricks', 4);
  requireTextArray(revision.exam_traps, 'revision.exam_traps', 5);
  if (!Array.isArray(revision.comparisons) || revision.comparisons.length < 1) throw new Error('Revision comparisons are incomplete');
  revision.comparisons.forEach((comparison, index) => {
    requireText(comparison.left, `revision comparison ${index + 1} left`);
    requireText(comparison.right, `revision comparison ${index + 1} right`);
    requireTextArray(comparison.difference_points, `revision comparison ${index + 1} difference_points`, 3);
  });
  return revision;
}

function validateQuestion(question, label, allowShortAnswer = true) {
  requireText(question.id, `${label} id`);
  requireText(question.concept_id, `${label} concept_id`);
  requireText(question.type, `${label} type`);
  if (!QUESTION_TYPES.includes(question.type)) throw new Error(`${label} has unsupported type ${question.type}`);
  requireText(question.question, `${label} question`);
  requireText(question.explanation, `${label} explanation`);
  if (question.type === 'fill_blank') {
    requireTextArray(question.accepted_answers, `${label} accepted_answers`, 1);
  } else if (question.type === 'short_answer') {
    if (!allowShortAnswer) throw new Error(`${label} cannot be short_answer`);
    requireText(question.expected_answer, `${label} expected_answer`);
  } else {
    requireTextArray(question.options, `${label} options`, 2);
    if (!Number.isInteger(question.correct_index) || question.correct_index < 0 || question.correct_index >= question.options.length) {
      throw new Error(`${label} has an invalid correct_index`);
    }
  }
}

function validateQuestions(data, conceptIds) {
  if (!data || !Array.isArray(data.quiz_questions) || data.quiz_questions.length < 30 || data.quiz_questions.length > 35) {
    throw new Error('Quiz must contain 30 to 35 questions');
  }
  const coverage = new Map(conceptIds.map((id) => [id, 0]));
  const types = new Set();
  data.quiz_questions.forEach((question, index) => {
    validateQuestion(question, `quiz question ${index + 1}`);
    if (!coverage.has(question.concept_id)) throw new Error(`Quiz question ${question.id} references an unknown concept`);
    coverage.set(question.concept_id, coverage.get(question.concept_id) + 1);
    types.add(question.type);
  });
  for (const [conceptId, count] of coverage) if (count < 4) throw new Error(`Concept ${conceptId} needs at least 4 quiz questions`);
  const missingTypes = QUESTION_TYPES.filter((type) => !types.has(type));
  if (missingTypes.length) throw new Error(`Quiz is missing question types: ${missingTypes.join(', ')}`);
  return data;
}

function validateRevisionAndTest(data, conceptIds) {
  validateRevision(data?.revision, conceptIds);
  if (!Array.isArray(data?.topic_test) || data.topic_test.length !== 10) throw new Error('Mini test must contain exactly 10 questions');
  data.topic_test.forEach((question, index) => {
    if (!['mcq', 'assertion_reason', 'true_false', 'match_following', 'case_based'].includes(question.type)) {
      throw new Error(`Mini-test question ${index + 1} must be objective`);
    }
    validateQuestion(question, `mini-test question ${index + 1}`, false);
    if (!conceptIds.includes(question.concept_id)) throw new Error(`Mini-test question ${question.id} references an unknown concept`);
  });
  return data;
}

async function generateContentWithRetry(prompt, validator = null, label = 'Content', maxAttempts = retryAttempts) {
  let attempt = 0;
  let activePrompt = prompt;
  while (attempt < maxAttempts) {
    attempt++;
    try {
      const client = getAIClient();
      const response = await client.models.generateContent({
        model: MODEL,
        contents: activePrompt,
        config: { temperature: 0.25, responseMimeType: 'application/json' }
      });

      let text = response.text || '';
      text = text.trim().replace(/^```(?:json)?\s*/i, '').replace(/\s*```$/i, '').trim();

      let parsed;
      try {
        parsed = JSON.parse(text);
      } catch (parseError) {
        parsed = JSON.parse(jsonrepair(text));
      }
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
    } catch (err) {
      console.warn(`${label} attempt ${attempt} failed: ${formatApiError(err)}`);
      if (err.message?.includes('429') || err.message?.includes('quota') || err.message?.includes('ResourceExhausted')) {
        rotateKey();
        await sleep(Math.max(1500, retryDelayMs * 2) * attempt);
      } else {
        await sleep(retryDelayMs * attempt);
      }
      if (err.isValidationError) {
        activePrompt = `${prompt}\n\nYour previous response failed validation with this error: ${err.message}\nReturn a complete replacement JSON response and satisfy every minimum count exactly.`;
      }
      if (attempt >= maxAttempts) throw err;
    }
  }
}

function renderLegacyHtml(originalHtml, data, metadata) {
  const $ = cheerio.load(originalHtml);

  // Update lead text if suitable
  if (metadata.title) {
    $('.hero h1').text(metadata.title);
  }

  // Build the new point-wise cards inside .content-col
  const contentCol = $('.main-grid .content-col');
  contentCol.empty();

  // Card 1: Syllabus Overview & Exam Focus (Point-wise)
  let card1Html = `<article class="card">
    <h2>1. Syllabus Overview & Exam Focus</h2>
    <p>In competitive examinations (UP TGT Social Science / UP PGT History / UGC NET), <strong>${escapeHtml(metadata.title)}</strong> is a key tested topic. Focus your preparation on the following high-priority points:</p>
    <ul class="point-notes">`;
  for (const pt of (data.syllabus_focus_points || [])) {
    card1Html += `<li>${pt}</li>`;
  }
  card1Html += `</ul>
  </article>`;
  contentCol.append(card1Html);

  // Card 2+: Study Notes Sections (Point-wise notes)
  let sectionIndex = 2;
  for (const section of (data.study_sections || [])) {
    let secHtml = `<article class="card">
      <h2>${sectionIndex}. ${escapeHtml(section.heading)}</h2>
      <ul class="point-notes">`;
    for (const pt of (section.points || [])) {
      secHtml += `<li>${pt}</li>`;
    }
    secHtml += `</ul>
    </article>`;
    contentCol.append(secHtml);
    sectionIndex++;
  }

  // Card: High-Yield Key Facts & Chronology
  if (Array.isArray(data.key_facts_revision) && data.key_facts_revision.length > 0) {
    let factsHtml = `<article class="card">
      <h2>${sectionIndex}. High-Yield Key Facts & Exam Memory Points</h2>
      <div class="quick-facts-box">
        <ul class="point-notes">`;
    for (const fact of data.key_facts_revision) {
      factsHtml += `<li><strong>Key Fact:</strong> ${fact}</li>`;
    }
    factsHtml += `</ul>
      </div>
    </article>`;
    contentCol.append(factsHtml);
    sectionIndex++;
  }

  // Card: Common Misconceptions & Exam Traps
  if (Array.isArray(data.exam_traps_and_distinctions) && data.exam_traps_and_distinctions.length > 0) {
    let trapsHtml = `<article class="card">
      <h2>${sectionIndex}. Common Exam Pitfalls & Confusions to Avoid</h2>
      <ul class="point-notes warning-points">`;
    for (const trap of data.exam_traps_and_distinctions) {
      trapsHtml += `<li>${trap}</li>`;
    }
    trapsHtml += `</ul>
    </article>`;
    contentCol.append(trapsHtml);
    sectionIndex++;
  }

  // Card: Topic Self-Assessment Checklist
  const checklistItems = Array.isArray(data.interactive_checklist) && data.interactive_checklist.length > 0
    ? data.interactive_checklist
    : [
        `Master fundamental chronology and sources for ${metadata.title}`,
        `Understand key terms, inscriptions, and archaeological findings`,
        `Review major rulers, thinkers, or socio-economic dynamics`,
        `Solve minimum 20 previous years' questions (PYQ)`,
        `Mark complete on the main syllabus tracker`
      ];

  let checkHtml = `<article class="card">
    <h2>${sectionIndex}. Self-Assessment & Topic Checklist</h2>
    <p>Check off each item as you master the factual and analytical aspects of <strong>${escapeHtml(metadata.title)}</strong>:</p>
    <div class="checklist">`;
  for (const item of checklistItems) {
    checkHtml += `<label class="check-item"><input type="checkbox"> <span>${item}</span></label>`;
  }
  checkHtml += `</div>
  </article>`;
  contentCol.append(checkHtml);

  // Ensure styling for point-notes is present in <style>
  if (!$('style').text().includes('.point-notes')) {
    const additionalCss = `
.point-notes{margin:8px 0 16px 20px;padding:0;display:grid;gap:10px}
.point-notes li{color:var(--ink2);line-height:1.65;font-size:.92rem}
.point-notes li strong{color:var(--ink)}
.quick-facts-box{background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;padding:14px 16px}
.warning-points li{color:#92400e}
.warning-points li strong{color:#78350f}
`;
    $('style').append(additionalCss);
  }

  return $.html();
}

function inlineText(value) {
  return escapeHtml(value).replace(/\n/g, '<br>');
}

function list(items, className = '') {
  return `<ul${className ? ` class="${className}"` : ''}>${(items || []).map((item) => `<li>${inlineText(item)}</li>`).join('')}</ul>`;
}

function renderChecklist(items) {
  return `<div class="checklist">${(items || []).map((item) => `<label class="check-item"><input type="checkbox"><span>${inlineText(item)}</span></label>`).join('')}</div>`;
}

function safeJson(value) {
  return JSON.stringify(value).replace(/</g, '\\u003c').replace(/>/g, '\\u003e').replace(/&/g, '\\u0026');
}

function renderHistoryConcepts(content) {
  return content.concepts.map((concept, index) => `<section class="notes-section" id="concept-${escapeHtml(concept.id)}">
    <div class="concept-number">Concept ${index + 1}</div>
    <h2>${escapeHtml(concept.title)}</h2>
    <p class="lead-concept">${inlineText(concept.lead)}</p>
    <h3>Detailed explanation</h3>${list(concept.explanation_points, 'notes-bullet-list')}
    <h3>Key points</h3>${list(concept.key_points, 'notes-bullet-list')}
    <div class="history-callout"><strong>Examples and evidence</strong>${list(concept.examples, 'notes-bullet-list')}</div>
    <div class="comparison-callout"><strong>Important distinctions</strong>${list(concept.comparison_points, 'notes-bullet-list')}</div>
    <div class="trap-callout"><strong>Common misconceptions</strong>${list(concept.common_misconceptions, 'notes-bullet-list')}</div>
    <div class="exam-focus"><strong>Exam focus</strong>${list(concept.exam_focus_points, 'notes-bullet-list')}</div>
  </section>`).join('\n');
}

function renderHistoryRevision(revision) {
  const conceptRevisions = revision.concept_revisions.map((item, index) => `<section class="revision-card-box">
    <div class="concept-number">Concept ${index + 1}</div>
    <h2>${escapeHtml(item.title)}</h2>
    <h3>Point-wise rapid recall</h3>${list(item.pointwise_summary, 'must-remember-list')}
    <h3>Mnemonic</h3>${list(item.mnemonics, 'must-remember-list')}
    <h3>Tips</h3>${list(item.tips, 'must-remember-list')}
    <h3>Exam tricks</h3>${list(item.tricks, 'must-remember-list')}
    <h3>Common traps</h3>${list(item.common_traps, 'must-remember-list')}
  </section>`).join('\n');
  const comparisons = revision.comparisons.map((item) => `<div class="revision-comparison"><div><strong>${escapeHtml(item.left)}</strong><span>vs</span><strong>${escapeHtml(item.right)}</strong></div>${list(item.difference_points, 'must-remember-list')}</div>`).join('');
  return `<div class="summary-hero-box"><h2>Rapid revision</h2><p>Use this tab after completing the detailed notes and before attempting the mini test.</p></div>
    ${conceptRevisions}
    <section class="revision-card-box"><h2>Quick facts</h2>${list(revision.quick_facts, 'must-remember-list')}</section>
    <section class="revision-card-box"><h2>Topic mnemonics</h2>${list(revision.mnemonics, 'must-remember-list')}</section>
    <section class="revision-card-box"><h2>Revision tips</h2>${list(revision.tips, 'must-remember-list')}</section>
    <section class="revision-card-box"><h2>Exam tricks</h2>${list(revision.tricks, 'must-remember-list')}</section>
    <section class="revision-card-box"><h2>Important comparisons</h2><div class="revision-comparisons">${comparisons}</div></section>
    <section class="revision-card-box"><h2>Exam traps and cautions</h2>${list(revision.exam_traps, 'must-remember-list')}</section>`;
}

const questionTypeNames = {
  mcq: 'MCQ',
  assertion_reason: 'Assertion–Reason',
  true_false: 'True / False',
  fill_blank: 'Fill in the blank',
  match_following: 'Match the following',
  case_based: 'Case-based',
  short_answer: 'Short answer'
};

function renderHistoryQuizQuestion(question, index) {
  const letters = ['A', 'B', 'C', 'D', 'E'];
  let answerBody;
  if (question.type === 'fill_blank') {
    answerBody = `<input class="quiz-answer-input" id="quiz-input-${index}" aria-label="Your answer"><button type="button" class="quiz-check-btn" data-fill="${index}">Check answer</button>`;
  } else if (question.type === 'short_answer') {
    answerBody = `<textarea class="quiz-answer-textarea" id="quiz-input-${index}" aria-label="Your answer"></textarea><button type="button" class="quiz-check-btn" data-short="${index}">Show answer</button>`;
  } else {
    answerBody = `<div class="quiz-options-group">${(question.options || []).map((option, optionIndex) => `<button type="button" class="quiz-option-btn" data-quiz="${index}" data-option="${optionIndex}"><span class="option-letter">${letters[optionIndex] || optionIndex + 1}</span><span class="option-text">${inlineText(option)}</span></button>`).join('')}</div>`;
  }
  return `<article class="quiz-question-card" id="quiz-card-${index}" data-index="${index}" data-type="${escapeHtml(question.type)}">
    <div class="q-header"><span class="q-number">Question ${index + 1}</span><span class="question-type">${questionTypeNames[question.type] || escapeHtml(question.type)}</span></div>
    <p class="q-text">${inlineText(question.question)}</p>${answerBody}<div id="quiz-feedback-${index}" role="status" aria-live="polite"></div>
  </article>`;
}

function renderHistoryTestQuestion(question, index) {
  const letters = ['A', 'B', 'C', 'D', 'E'];
  return `<article class="test-question-card" id="test-card-${index}" data-index="${index}">
    <div class="test-q-header"><span class="t-badge">Question ${index + 1}</span><span class="question-type">${questionTypeNames[question.type] || escapeHtml(question.type)}</span></div>
    <p class="test-question-text">${inlineText(question.question)}</p>
    <div class="quiz-options-group">${question.options.map((option, optionIndex) => `<button type="button" class="test-option-btn quiz-option-btn" data-test="${index}" data-option="${optionIndex}"><span class="option-letter">${letters[optionIndex] || optionIndex + 1}</span><span class="option-text">${inlineText(option)}</span></button>`).join('')}</div>
    <div id="test-feedback-${index}" role="status" aria-live="polite"></div>
  </article>`;
}

function historyTabCss() {
  return `.history-tab-shell{position:sticky;top:66px;z-index:30;padding:10px 0;background:rgba(246,248,251,.96);backdrop-filter:blur(10px)}
.study-tabs{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:8px;padding:8px;background:#fff;border:1px solid var(--line);border-radius:14px;box-shadow:0 8px 22px rgba(28,39,60,.08)}
.tab-btn{min-height:52px;border:1px solid transparent;border-radius:10px;background:transparent;color:var(--ink2);font:inherit;font-weight:800;cursor:pointer;padding:8px 10px}.tab-btn.active{background:var(--accent-soft);border-color:var(--accent-border);color:var(--accent)}.tab-btn:hover{border-color:var(--accent-border)}.tab-badge{display:inline-block;margin-left:4px;font-size:.7rem;color:var(--muted)}
.tab-panel.hidden,.question-source-data,.hidden{display:none!important}.notes-section h3{margin-top:18px;color:var(--brand);font-size:1rem}.concept-number{display:inline-block;margin-bottom:8px;color:var(--accent);font-size:.74rem;font-weight:900;text-transform:uppercase;letter-spacing:.08em}.lead-concept{font-weight:700;color:var(--brand);font-size:1rem}.history-callout,.comparison-callout,.trap-callout,.exam-focus{padding:14px 16px;border-radius:10px;margin:14px 0;line-height:1.6}.history-callout{background:#eff6ff;border-left:4px solid #2563eb}.comparison-callout{background:#f0fdf4;border-left:4px solid #15803d}.trap-callout{background:#fffbeb;border-left:4px solid #d97706}.exam-focus{background:var(--accent-soft);border-left:4px solid var(--accent)}
.quiz-panel-header,.test-panel-header{display:flex;justify-content:space-between;gap:16px;align-items:center;flex-wrap:wrap}.quiz-live-scoreboard{display:flex;gap:8px;align-items:center}.score-pill,.test-timer-badge{padding:7px 11px;border-radius:999px;background:var(--accent-soft);color:var(--accent);font-weight:800;font-size:.8rem}.btn-reset-quiz,.quiz-check-btn,.btn-submit-test,.btn-retake-test{border:0;border-radius:8px;background:var(--brand);color:#fff;font:inherit;font-weight:800;padding:9px 13px;cursor:pointer}.quiz-questions-list,.test-questions-list{display:grid;gap:14px}.quiz-question-card,.test-question-card,.revision-card-box{background:#fff;border:1px solid var(--line);border-radius:14px;padding:18px}.q-header,.test-q-header{display:flex;justify-content:space-between;gap:10px;align-items:center;flex-wrap:wrap}.q-number,.t-badge{font-size:.76rem;font-weight:900;color:var(--muted);text-transform:uppercase;letter-spacing:.06em}.question-type{display:inline-flex;padding:3px 9px;border-radius:999px;background:var(--accent-soft);color:var(--accent);font-size:.72rem;font-weight:850}.q-text,.test-question-text{font-weight:750;color:var(--ink);line-height:1.6}.quiz-options-group{display:grid;gap:8px}.quiz-option-btn{width:100%;display:flex;gap:10px;align-items:flex-start;text-align:left;border:1px solid var(--line);border-radius:9px;background:#fff;color:var(--ink);padding:10px 12px;font:inherit;cursor:pointer}.quiz-option-btn:hover,.quiz-option-btn.selected{border-color:var(--accent);background:var(--accent-soft)}.quiz-option-btn.correct{border-color:#15803d;background:#f0fdf4}.quiz-option-btn.incorrect{border-color:#b91c1c;background:#fef2f2}.option-letter{font-weight:900;color:var(--accent);min-width:20px}.quiz-answer-input,.quiz-answer-textarea{width:100%;padding:11px 13px;border:1px solid var(--line);border-radius:9px;background:var(--paper);color:var(--ink);font:inherit}.quiz-answer-textarea{min-height:96px;resize:vertical}.quiz-check-btn{margin-top:10px}.quiz-feedback{margin-top:12px}.quiz-feedback.correct{color:#166534}.quiz-feedback.incorrect{color:#991b1b}.test-submit-bar{display:flex;justify-content:flex-end;margin-top:18px}.test-result-modal{margin-top:18px;padding:18px;border:1px solid var(--accent-border);border-radius:14px;background:var(--accent-soft)}.revision-card-box{margin-bottom:14px}.revision-card-box h2{margin-top:0}.revision-card-box h3{color:var(--brand);font-size:.95rem}.must-remember-list{margin-top:8px}.revision-comparisons{display:flex;flex-direction:column;gap:12px}.revision-comparison{padding:14px 16px;border:1px solid var(--line);border-radius:10px;background:var(--paper)}.revision-comparison>div{display:flex;gap:9px;align-items:center;flex-wrap:wrap;color:var(--brand)}.revision-comparison span{color:var(--muted);font-size:.78rem}
@media(max-width:680px){.study-tabs{grid-template-columns:repeat(2,minmax(0,1fr))}.tab-btn{font-size:.78rem}.history-tab-shell{top:58px}}`;
}

function historyRuntime() {
  return `<script id="history-runtime">document.addEventListener('DOMContentLoaded',()=>{const quiz=JSON.parse(document.getElementById('history-quiz-data').textContent||'[]');const test=JSON.parse(document.getElementById('history-test-data').textContent||'[]');const esc=value=>String(value??'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#39;');const letters=['A','B','C','D','E'];let quizScore=0;const answered=new Set();const feedback=(ok,text)=>'<div class="quiz-feedback '+(ok?'correct':'incorrect')+'"><strong>'+(ok?'Correct':'Review')+'</strong><p>'+esc(text)+'</p></div>';function markQuiz(i,ok,text){if(answered.has(i))return;answered.add(i);if(ok)quizScore++;const card=document.getElementById('quiz-card-'+i);card.dataset.answered='true';card.querySelectorAll('button').forEach(button=>button.disabled=true);document.getElementById('quiz-feedback-'+i).innerHTML=feedback(ok,text);document.getElementById('quiz-score').textContent='Score: '+quizScore+' / '+quiz.length;}document.querySelectorAll('[data-quiz]').forEach(button=>button.addEventListener('click',()=>{const i=Number(button.dataset.quiz),option=Number(button.dataset.option),question=quiz[i];document.querySelectorAll('#quiz-card-'+i+' [data-option]').forEach((item,index)=>{item.disabled=true;if(index===question.correct_index)item.classList.add('correct');if(index===option&&option!==question.correct_index)item.classList.add('incorrect');});markQuiz(i,option===question.correct_index,question.explanation);}));document.querySelectorAll('[data-fill]').forEach(button=>button.addEventListener('click',()=>{const i=Number(button.dataset.fill),question=quiz[i],value=document.getElementById('quiz-input-'+i).value.trim().toLowerCase();markQuiz(i,(question.accepted_answers||[]).some(answer=>value===String(answer).trim().toLowerCase()),'Accepted answer(s): '+(question.accepted_answers||[]).join(', ')+' — '+question.explanation);}));document.querySelectorAll('[data-short]').forEach(button=>button.addEventListener('click',()=>{const i=Number(button.dataset.short),question=quiz[i];markQuiz(i,false,'Expected answer: '+(question.expected_answer||'See the explanation')+' — '+question.explanation);}));document.getElementById('btn-reset-quiz').addEventListener('click',()=>location.reload());const chosen={};let submitted=false;document.querySelectorAll('[data-test]').forEach(button=>button.addEventListener('click',()=>{if(submitted)return;const i=Number(button.dataset.test);chosen[i]=Number(button.dataset.option);document.querySelectorAll('#test-card-'+i+' [data-option]').forEach(item=>item.classList.remove('selected'));button.classList.add('selected');}));function submitTest(){if(submitted)return;submitted=true;let score=0;test.forEach((question,i)=>{const answer=chosen[i];if(answer===question.correct_index)score++;document.querySelectorAll('#test-card-'+i+' [data-option]').forEach((item,index)=>{item.disabled=true;if(index===question.correct_index)item.classList.add('correct');if(index===answer&&answer!==question.correct_index)item.classList.add('incorrect');});document.getElementById('test-feedback-'+i).innerHTML=feedback(answer===question.correct_index,question.explanation);});document.getElementById('test-score').textContent=score;document.getElementById('test-result').classList.remove('hidden');document.getElementById('btn-submit-test').classList.add('hidden');}document.getElementById('btn-submit-test').addEventListener('click',submitTest);document.getElementById('btn-retake-test').addEventListener('click',()=>location.reload());let timer=null,remaining=600;function startTimer(){if(timer||submitted)return;timer=setInterval(()=>{remaining--;document.getElementById('test-timer').textContent=String(Math.floor(remaining/60)).padStart(2,'0')+':'+String(remaining%60).padStart(2,'0');if(remaining<=0){clearInterval(timer);submitTest();}},1000);}const tabs=document.querySelectorAll('.tab-btn'),panels=document.querySelectorAll('.tab-panel');tabs.forEach(button=>button.addEventListener('click',()=>{tabs.forEach(item=>{item.classList.remove('active');item.setAttribute('aria-selected','false');});panels.forEach(panel=>{panel.classList.remove('active');panel.classList.add('hidden');});button.classList.add('active');button.setAttribute('aria-selected','true');document.getElementById(button.dataset.tab).classList.remove('hidden');document.getElementById(button.dataset.tab).classList.add('active');if(button.dataset.tab==='tab-test')startTimer();window.scrollTo({top:document.querySelector('.history-tab-shell').offsetTop-15,behavior:'smooth'});}));});</script>`;
}

function renderHtml(originalHtml, data, questions, metadata) {
  const $ = cheerio.load(originalHtml);
  if (!$('link[href="/assets/css/design-system.css"]').length) {
    $('head').append('<link rel="stylesheet" href="/assets/css/design-system.css">');
  }
  const historyHeader = $('.site-header .header-inner').first();
  const historyBack = historyHeader.find('a.back-btn').first();
  if (historyBack.length && !historyBack.parent().hasClass('header-actions')) {
    historyBack.wrap('<div class="header-actions"></div>');
  }
  const mainGrid = $('.main-grid').first();
  const contentCol = mainGrid.find('.content-col').first();
  if (!mainGrid.length || !contentCol.length) throw new Error('History page is missing .main-grid or .content-col');

  $('.history-tab-shell').remove();
  $('script#history-quiz-data, script#history-test-data, script#history-runtime').remove();
  contentCol.empty();
  mainGrid.before(`<div class="history-tab-shell" data-history-tabs="${TAB_VERSION}"><div class="study-tabs" role="tablist" aria-label="History study tabs">
    <button type="button" class="tab-btn active" role="tab" aria-selected="true" data-tab="tab-notes" id="tab-btn-notes"><span>Study Notes</span></button>
    <button type="button" class="tab-btn" role="tab" aria-selected="false" data-tab="tab-quiz" id="tab-btn-quiz"><span>Concept Quiz</span><span class="tab-badge">${questions.quiz_questions.length}Q</span></button>
    <button type="button" class="tab-btn" role="tab" aria-selected="false" data-tab="tab-summary" id="tab-btn-summary"><span>Revision Summary</span></button>
    <button type="button" class="tab-btn" role="tab" aria-selected="false" data-tab="tab-test" id="tab-btn-test"><span>Mini Test</span><span class="tab-badge">10Q</span></button>
  </div></div>`);

  const checklist = data.concepts.map((concept) => `I can explain ${concept.title} with its key dates, terms and exam distinctions.`);
  contentCol.append(`<article class="tab-panel active" id="tab-notes" role="tabpanel" aria-labelledby="tab-btn-notes"><div class="card"><h2>Topic overview</h2>${list(data.introduction_points, 'notes-bullet-list')}</div>${renderHistoryConcepts(data)}<article class="card"><h2>Self-assessment checklist</h2>${renderChecklist(checklist)}</article></article>`);
  contentCol.append(`<article class="tab-panel hidden" id="tab-quiz" role="tabpanel" aria-labelledby="tab-btn-quiz"><div class="card"><div class="quiz-panel-header"><div><h2>Concept Quiz</h2><p>Practice across every concept with mixed question formats.</p></div><div class="quiz-live-scoreboard"><span class="score-pill" id="quiz-score">Score: 0 / ${questions.quiz_questions.length}</span><button type="button" class="btn-reset-quiz" id="btn-reset-quiz">Reset</button></div></div><div class="quiz-questions-list">${questions.quiz_questions.map(renderHistoryQuizQuestion).join('')}</div></div></article>`);
  contentCol.append(`<article class="tab-panel hidden" id="tab-summary" role="tabpanel" aria-labelledby="tab-btn-summary"><div class="summary-container">${renderHistoryRevision(data.revision)}</div></article>`);
  contentCol.append(`<article class="tab-panel hidden" id="tab-test" role="tabpanel" aria-labelledby="tab-btn-test"><div class="card"><div class="test-panel-header"><div><h2>10-question mini test</h2><p>Attempt the objective questions and submit when finished.</p></div><span class="test-timer-badge" id="test-timer">10:00</span></div><div class="test-questions-list">${questions.topic_test.map(renderHistoryTestQuestion).join('')}</div><div class="test-submit-bar"><button type="button" class="btn-submit-test" id="btn-submit-test">Submit Test</button></div><div class="test-result-modal hidden" id="test-result"><h3>Test result</h3><p><strong><span id="test-score">0</span> / 10</strong></p><button type="button" class="btn-retake-test" id="btn-retake-test">Retake Test</button></div></div></article>`);

  $('style').first().append(historyTabCss());
  $('.exam-badges .history-generated-badge').remove();
  $('.exam-badges').append(`<span class="exam-chip history-generated-badge">${questions.quiz_questions.length} quiz questions</span><span class="exam-chip history-generated-badge">10-question mini test</span>`);
  $('body').append(`<script type="application/json" id="history-quiz-data">${safeJson(questions.quiz_questions)}</script><script type="application/json" id="history-test-data">${safeJson(questions.topic_test)}</script>${historyRuntime()}`);
  if (!$('script[src="/assets/js/topic-mobile-nav.js"]').length) {
    $('body').append('<script src="/assets/js/topic-mobile-nav.js" defer></script>');
  }
  return $.html();
}

async function main() {
  console.log(`Starting History Topic Generator [Model: ${MODEL}]`);
  const allPages = discoverHistoryPages(HISTORY_ROOT);
  console.log(`Found ${allPages.length} total history topic pages.`);

  const status = readStatus();

  // Filter pages
  let targets = allPages;
  if (requestedTopic) {
    const cleanReq = requestedTopic.replace(/\\/g, '/').replace(/\/index\.html$/, '');
    targets = allPages.filter((p) => p.topicDir === cleanReq || p.relPath === `${cleanReq}/index.html`);
    if (targets.length === 0) {
      console.error(`Error: No topic matched '${requestedTopic}'`);
      process.exit(1);
    }
  } else if (!force && !allFlag) {
    // By default target placeholder pages
    targets = allPages.filter((p) => {
      const html = fs.readFileSync(p.fullPath, 'utf8');
      return isPlaceholderContent(html);
    });
  }

  if (requestedLimit > 0) {
    targets = targets.slice(0, requestedLimit);
  }

  console.log(`Targeting ${targets.length} pages for generation.`);

  if (dryRun) {
    console.log('DRY RUN: Targeted pages:');
    targets.forEach((t, idx) => console.log(`  [${idx + 1}] ${t.relPath}`));
    return;
  }

  if (API_KEYS.length === 0) {
    throw new Error('No GEMINI_API_KEY configured in environment or .env');
  }

  await assertGeminiReachable();

  let completed = 0;
  let failed = 0;
  let nextTargetIndex = 0;
  async function processPage(index, page) {
    console.log(`\n[${index + 1}/${targets.length}] Processing: ${page.relPath}`);

    try {
      const originalHtml = fs.readFileSync(page.fullPath, 'utf8');
      const $ = cheerio.load(originalHtml);

      const title = $('h1').text().trim() || path.basename(page.topicDir);
      const kicker = $('.kicker').text().trim();
      const breadcrumb = $('.breadcrumb').text().replace(/\s+/g, ' ').trim();

      const metadata = {
        title,
        kicker,
        breadcrumb,
        relPath: page.relPath
      };

      console.log(`  Generating point-wise content for "${title}"...`);
      const data = await generateContentWithRetry(buildContentPrompt(metadata), validateContent, 'Study notes');
      const conceptIds = data.concepts.map((concept) => concept.id);
      const quiz = await generateContentWithRetry(buildQuestionsPrompt(metadata, data), (result) => validateQuestions(result, conceptIds), 'Quiz');
      const revisionAndTest = await generateContentWithRetry(buildRevisionTestPrompt(metadata, data), (result) => validateRevisionAndTest(result, conceptIds), 'Revision and mini test');
      data.revision = revisionAndTest.revision;
      const questions = {
        quiz_questions: quiz.quiz_questions,
        topic_test: revisionAndTest.topic_test
      };

      console.log(`  Received ${data.concepts.length} concepts, ${questions.quiz_questions.length} quiz questions and ${questions.topic_test.length} mini-test questions. Rendering tabs...`);
      const updatedHtml = renderHtml(originalHtml, data, questions, metadata);

      fs.writeFileSync(page.fullPath, updatedHtml, 'utf8');
      console.log(`  ✓ Successfully updated: ${page.relPath}`);

      status[page.relPath] = {
        updatedAt: new Date().toISOString(),
        model: MODEL,
        status: 'completed',
        tabVersion: TAB_VERSION,
        concepts: data.concepts.length,
        quizQuestions: questions.quiz_questions.length,
        testQuestions: questions.topic_test.length
      };
      writeStatus(status);

      completed++;

      if (gapMs > 0) {
        await sleep(gapMs);
      }
    } catch (err) {
      console.error(`  ✗ Failed to process ${page.relPath}: ${err.message}`);
      status[page.relPath] = {
        updatedAt: new Date().toISOString(),
        model: MODEL,
        status: 'error',
        error: err.message
      };
      writeStatus(status);
      failed++;
    }
  }

  async function worker() {
    while (true) {
      const index = nextTargetIndex++;
      if (index >= targets.length) return;
      await processPage(index, targets[index]);
    }
  }

  const workerCount = Math.min(concurrency, targets.length);
  console.log(`Using ${workerCount} concurrent workers; retry limit ${retryAttempts}; inter-page gap ${gapMs}ms.`);
  await Promise.all(Array.from({ length: workerCount }, () => worker()));

  console.log(`\nFinished! Successfully generated and updated ${completed}/${targets.length} pages; failed ${failed}.`);
}

main().catch((err) => {
  console.error('Fatal error:', err);
  process.exit(1);
});
