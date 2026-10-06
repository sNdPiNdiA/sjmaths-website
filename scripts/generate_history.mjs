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
 *   node scripts/generate_history.mjs --remaining
 *   node scripts/generate_history.mjs --concurrency 2 --max-attempts 1 --gap 0
 *   node scripts/generate_history.mjs --force
 */

import fs from 'node:fs';
import path from 'node:path';
import 'dotenv/config';
import { GoogleGenAI } from '@google/genai';
import { jsonrepair } from 'jsonrepair';
import * as cheerio from 'cheerio';
import { renderHistoryHtml as renderHtml, TAB_VERSION } from './lib/history-renderer.mjs';
import { QUESTION_TYPES, validateContent, validateQuestions, validateRevisionAndTest } from './lib/history-schema.mjs';

const ROOT = process.cwd();
const HISTORY_ROOT = path.join(ROOT, 'history');
const STATUS_PATH = path.join(ROOT, 'content-generation-status-history.json');
const MODEL = process.env.GEMINI_MODEL || 'gemini-3.5-flash-lite';

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
const remainingFlag = hasFlag('--remaining');
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
5. Write in direct, natural textbook language. Avoid promotional introductions, study advice, repeated summaries, and phrases such as "it is important to note".
6. Keep each point concise and do not restate the same fact across concepts, examples, revision notes, or exam tips.
7. Provide the output in RAW JSON format only (no markdown fencing, no preamble).

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
    // Target only remaining files: not completed in status log OR still containing placeholder content
    targets = allPages.filter((p) => {
      const isCompletedInStatus = status[p.relPath]?.status === 'completed';
      if (isCompletedInStatus) {
        // Also verify the file on disk is actually rendered, not reverted to placeholder
        const html = fs.readFileSync(p.fullPath, 'utf8');
        return isPlaceholderContent(html);
      }
      return true;
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
