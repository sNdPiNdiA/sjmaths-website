#!/usr/bin/env node
/**
 * generate_upsssc_intermediate_gemini.mjs
 *
 * Automated generator script for UPSSSC Intermediate Level Mains Micro-Topic Pages.
 * Generates all subject files (except Current Affairs and Data Interpretation as requested).
 *
 * Architecture:
 * - Tab 1 (Pointwise Study Notes): 1 API call with gemini-3.5-flash-lite
 * - Tab 2 (30 Revision Practice MCQs): 1 API call with gemini-3.5-flash-lite
 * - Tab 3 (15-Question Timed Mini Test): 1 API call with gemini-3.5-flash-lite
 * - Translation: Dedicated calls with gemini-3.1-flash-lite to translate generated content into Hindi
 * - Assembly: Integrates into the UPSSSC Intermediate UI/UX design system with 100% bilingual parity
 *
 * Usage:
 *   node scripts/generate_upsssc_intermediate_gemini.mjs --list
 *   node scripts/generate_upsssc_intermediate_gemini.mjs --topic polity-mt-1-1
 *   node scripts/generate_upsssc_intermediate_gemini.mjs --subject polity --limit 1
 *   node scripts/generate_upsssc_intermediate_gemini.mjs --subject geography
 *   node scripts/generate_upsssc_intermediate_gemini.mjs --all
 *   node scripts/generate_upsssc_intermediate_gemini.mjs --update-hub
 *   node scripts/generate_upsssc_intermediate_gemini.mjs --force
 *   node scripts/generate_upsssc_intermediate_gemini.mjs --dry-run
 */

import fs from 'node:fs';
import path from 'node:path';
import 'dotenv/config';
import { GoogleGenAI } from '@google/genai';
import { jsonrepair } from 'jsonrepair';
import { UPSSSC_INTERMEDIATE_TOPICS } from './lib/upsssc-intermediate-topics.mjs';

const ROOT_DIR = process.cwd();
const INTERMEDIATE_DIR = path.join(ROOT_DIR, 'upsssc-intermediate-level');
const STATUS_FILE = path.join(ROOT_DIR, 'upsssc-intermediate-status.json');
const HUB_INDEX_FILE = path.join(INTERMEDIATE_DIR, 'index.html');

// CLI Arguments parsing
function parseCliArgs(args) {
  const flags = {};
  const positionals = [];
  for (let i = 0; i < args.length; i++) {
    const arg = args[i];
    if (arg.startsWith('--')) {
      if (arg.includes('=')) {
        const [k, ...v] = arg.slice(2).split('=');
        flags[k] = v.join('=');
      } else {
        const next = args[i + 1];
        if (next !== undefined && !next.startsWith('--')) {
          flags[arg.slice(2)] = next;
          i++;
        } else {
          flags[arg.slice(2)] = true;
        }
      }
    } else {
      positionals.push(arg);
    }
  }
  return { flags, positionals };
}

const { flags } = parseCliArgs(process.argv.slice(2));

const MODEL_GEN = flags['model-gen'] || process.env.GEMINI_MODEL_GEN || 'gemini-3.5-flash-lite';
const MODEL_TRANS = flags['model-trans'] || process.env.GEMINI_MODEL_TRANS || 'gemini-3.1-flash-lite';
const SUBJECT_FILTER = flags.subject || null;
const TOPIC_FILTER = flags.topic || null;
const LIMIT = flags.limit ? parseInt(flags.limit, 10) : 0;
const FORCE = Boolean(flags.force);
const ENRICH_NOTES = Boolean(flags['enrich-notes']);
const DRY_RUN = Boolean(flags['dry-run']);
const LIST_ONLY = Boolean(flags.list);
const UPDATE_HUB = Boolean(flags['update-hub']);
const GAP_MS = (parseInt(flags.gap || '2', 10)) * 1000;
const MAX_ATTEMPTS = parseInt(flags.attempts || '3', 10);

// API Keys setup with rotation
const apiKeys = [
  process.env.GEMINI_API_KEY,
  process.env.GEMINI_API_KEY_1,
  process.env.GEMINI_API_KEY_2,
  process.env.GOOGLE_API_KEY
].filter(Boolean);

if (apiKeys.length === 0 && !LIST_ONLY && !UPDATE_HUB) {
  console.error('❌ Error: No Gemini API Key found in .env (GEMINI_API_KEY, GEMINI_API_KEY_1, or GOOGLE_API_KEY)');
  process.exit(1);
}

let currentKeyIndex = 0;
function getGenAIClient() {
  const apiKey = apiKeys[currentKeyIndex % apiKeys.length];
  return new GoogleGenAI({ apiKey });
}

function rotateApiKey() {
  if (apiKeys.length > 1) {
    currentKeyIndex = (currentKeyIndex + 1) % apiKeys.length;
    console.log(`🔄 Rotated to Gemini API key #${currentKeyIndex + 1}`);
  }
}

const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms));

// Status tracking
function readStatus() {
  if (fs.existsSync(STATUS_FILE)) {
    try {
      return JSON.parse(fs.readFileSync(STATUS_FILE, 'utf8'));
    } catch {
      return {};
    }
  }
  return {};
}

function writeStatus(status) {
  try {
    fs.writeFileSync(STATUS_FILE, JSON.stringify(status, null, 2), 'utf8');
  } catch (err) {
    console.warn('Warning: Could not save status file:', err.message);
  }
}

// Check if a topic file is already valid
function isTopicComplete(targetFile) {
  if (!fs.existsSync(targetFile)) return false;
  try {
    const content = fs.readFileSync(targetFile, 'utf8');
    const hasCss = content.includes('upsssc-intermediate') && content.includes('.css');
    const hasJs = content.includes('upsssc-intermediate') && content.includes('.js');
    const qCount = (content.match(/class="question-card"|class="practice-question-card"/g) || []).length;
    const testCount = (content.match(/class="test-q-box"|class="test-qblock"/g) || []).length;
    const hasData = (content.includes('window.upssscTestData = [') || content.includes('window.upssscTestData=[')) && (content.match(/\{\s*"ans"\s*:/g) || []).length === 15;
    return hasCss && hasJs && qCount === 30 && testCount === 15 && hasData;
  } catch {
    return false;
  }
}

// Robust JSON parser with jsonrepair
function parseJsonSafe(text) {
  let cleaned = text.trim();
  // Strip code fences if present
  if (cleaned.startsWith('```')) {
    cleaned = cleaned.replace(/^```[a-zA-Z]*\n?/, '').replace(/```$/, '').trim();
  }
  try {
    return JSON.parse(cleaned);
  } catch {
    return JSON.parse(jsonrepair(cleaned));
  }
}

// Generic Gemini API caller with retry, key rotation, and 503 resilient fallback
async function callGemini(model, prompt, options = {}) {
  let lastError = null;
  let activeModel = model;

  for (let attempt = 1; attempt <= MAX_ATTEMPTS; attempt++) {
    try {
      const ai = getGenAIClient();
      const response = await ai.models.generateContent({
        model: activeModel,
        contents: prompt,
        config: {
          temperature: options.temperature ?? 0.25,
          responseMimeType: 'application/json'
        }
      });

      const text = response?.text;
      if (!text) throw new Error('Empty response from Gemini API');

      return parseJsonSafe(text);
    } catch (err) {
      lastError = err;
      const msg = err.message || '';
      console.warn(`⚠️ [Attempt ${attempt}/${MAX_ATTEMPTS}] Error with model ${activeModel}: ${msg.slice(0, 160)}`);

      if (msg.includes('503') || msg.includes('high demand') || msg.includes('UNAVAILABLE')) {
        if (activeModel === 'gemini-3.1-flash-lite') {
          console.log(`🔀 503 High Demand on gemini-3.1-flash-lite. Auto-falling back to gemini-3.5-flash-lite...`);
          activeModel = 'gemini-3.5-flash-lite';
        }
        rotateApiKey();
        const waitTime = attempt * 3000;
        console.log(`⏳ Waiting ${waitTime / 1000}s before retrying...`);
        await sleep(waitTime);
      } else if (msg.includes('429') || msg.includes('quota') || msg.includes('exhausted') || msg.includes('ResourceExhausted')) {
        rotateApiKey();
        const waitTime = attempt * 4000;
        console.log(`⏳ Waiting ${waitTime / 1000}s before retrying...`);
        await sleep(waitTime);
      } else {
        await sleep(2000);
      }
    }
  }

  throw new Error(`Failed after ${MAX_ATTEMPTS} attempts on model ${activeModel}: ${lastError?.message}`);
}

// ==================== TAB 1 GENERATION (gemini-3.5-flash-lite) ====================
async function generateTab1Notes(topic) {
  const prompt = `You are the foremost expert and textbook author for the Uttar Pradesh Subordinate Services Selection Commission (UPSSSC) Intermediate Level Mains Examination.

Generate EXHAUSTIVE, HIGHEST-YIELD, POINTWISE STUDY REVISION NOTES in ENGLISH for this topic:
SUBJECT: ${topic.subjectTitleEn}
SUBSECTION: ${topic.subSectionEn}
TOPIC: ${topic.titleEn}
CORE EXAM FOCUS:
${topic.focus}

CRITICAL PEDAGOGICAL MANDATE:
Do NOT produce high-level summaries or omit key information. Students rely solely on these notes to crack competitive UPSSSC exams. Every single fact, article number, constitutional clause, legal section, year, landmark Supreme Court judgment, definition, classification, formula, scheme name, exception, quote, and UP-specific relevance related to this topic MUST be included. NOTHING related to the topic must be missed!

STRUCTURE & REQUIREMENTS:
1. You MUST divide the study notes into EXACTLY 6 to 8 exhaustive, logically organized thematic sections (NEVER fewer than 6 sections under any circumstance; minimum 6 required).
2. For each section:
   - "title": Clean, crisp section heading. DO NOT prepend numbering or "Section X" to the title string.
   - "examPointer": A high-yield direct exam fact, memory rule, or mnemonic. DO NOT include prefixes like "Direct Exam Fact:" or "Tip:".
   - "table": Where classifications, comparisons, or multi-item lists exist (e.g., all 12 schedules, all borrowed sources, full list of articles, committee names & heads, historical acts & provisions, parts of Constitution), provide a COMPLETE multi-row table (minimum 4 to 12+ rows, 3 to 5 columns). DO NOT truncate or summarize lists.
   - "points": Exactly 6 to 10 dense, high-yield bullet items.
     - "badge": A crisp 2 to 5 word key concept badge (e.g., 'Article 19(1)(a) Scope', '42nd Amendment Additions', 'Jus Soli Birth Criteria', 'Pashupati Seal Animals', 'Zabti / Dahsala Bandobast').
     - "content": Dense, factual, pointwise information packed with exact dates, names, article numbers, legal acts, statistics, quotes, and UP exam questions. Avoid generic filler.

OUTPUT FORMAT:
Strict valid JSON matching this schema:
{
  "topicTag": "e.g. Constitutional Framework | Micro Topic 1.2",
  "subtitle": "Exhaustive pointwise study notes, 30 bilingual practice questions, and a 15-question interactive timed test for UPSSSC Intermediate Level Mains.",
  "sections": [
    {
      "title": "Clean Section Title",
      "examPointer": "High yield fact or mnemonic rule...",
      "table": {
        "headers": ["Col 1", "Col 2", "Col 3", "Col 4"],
        "rows": [
          ["Val 1", "Val 2", "Val 3", "Val 4"]
        ]
      },
      "points": [
        {
          "badge": "2-5 Word Badge",
          "content": "Dense, factual, specific revision bullet point..."
        }
      ]
    }
  ]
}`;

  for (let attempt = 1; attempt <= 3; attempt++) {
    const activePrompt = attempt === 1 
      ? prompt 
      : prompt + `\n\nCRITICAL REQUIREMENT FOR ATTEMPT ${attempt}: You MUST produce AT LEAST 6 SECTIONS (6 to 8 sections) in the 'sections' array. Do not combine topics into fewer than 6 sections!`;
    const res = await callGemini(MODEL_GEN, activePrompt, { temperature: 0.2 + (attempt * 0.05) });
    if (res.sections && res.sections.length >= 6) {
      return res;
    }
    console.warn(`⚠️ Tab 1 returned ${res.sections ? res.sections.length : 0} sections (minimum 6 required). Retrying (attempt ${attempt}/3)...`);
    await sleep(2000);
  }
  throw new Error(`Tab 1 failed to generate at least 6 sections after 3 attempts`);
}

// ==================== TAB 2 GENERATION (gemini-3.5-flash-lite) ====================
async function generateTab2PracticeMCQs(topic) {
  const prompt = `You are a premier question setter for the Uttar Pradesh Subordinate Services Selection Commission (UPSSSC) Intermediate Level Mains Examination.

Generate EXACTLY 30 high-quality, exam-standard Multiple Choice Questions (MCQs) in ENGLISH for this topic:
SUBJECT: ${topic.subjectTitleEn}
TOPIC: ${topic.titleEn}
SYLLABUS REFERENCE: ${topic.focus}

REQUIREMENTS:
1. Exactly 30 questions numbered 1 to 30 divided into 3 tiers:
   - Questions 1 to 10 ("easy"): Direct factual questions, dates, articles, definitions, key institutions, locations.
   - Questions 11 to 20 ("medium"): Conceptual matching, statements, cause-and-effect, chronological sequences.
   - Questions 21 to 30 ("hard"): In-depth provisions, subtle exceptions, assertions, UP state-level relevance where applicable.
2. Format:
   - Exactly 4 options labeled A, B, C, D with realistic distractors.
   - "correctAnswer" MUST be exactly one of "A", "B", "C", or "D".
   - "explanation" MUST be comprehensive and educational, explaining why the correct option is right and providing revision facts.

OUTPUT FORMAT:
Strict valid JSON matching this schema:
{
  "questions": [
    {
      "id": 1,
      "tag": "e.g. Constitutional Development",
      "question": "Question text in English...",
      "options": {
        "A": "Option text A...",
        "B": "Option text B...",
        "C": "Option text C...",
        "D": "Option text D..."
      },
      "correctAnswer": "A",
      "explanation": "Detailed explanation..."
    }
  ]
}`;

  const res = await callGemini(MODEL_GEN, prompt, { temperature: 0.25 });
  const questions = res.questions || [];
  if (questions.length < 30) {
    throw new Error(`Tab 2 returned only ${questions.length} questions (expected 30)`);
  }
  return questions.slice(0, 30);
}

// ==================== TAB 3 GENERATION (gemini-3.5-flash-lite) ====================
async function generateTab3MiniTest(topic) {
  const prompt = `You are a senior exam controller designing a timed mini-test for UPSSSC Intermediate Level Mains.

Generate EXACTLY 15 FRESH, high-yield Multiple Choice Questions in ENGLISH for a 15-minute timed exam (+1 mark for correct, -0.25 negative marking for incorrect).
SUBJECT: ${topic.subjectTitleEn}
TOPIC: ${topic.titleEn}
CORE FOCUS: ${topic.focus}

REQUIREMENTS:
1. Exactly 15 questions numbered 1 to 15.
2. Do not duplicate questions from previous practice sets. Cover the entire syllabus of this topic evenly.
3. Each question must have:
   - "id": 1 to 15
   - "stem": Authentic exam question stem
   - "options": Object with keys "A", "B", "C", "D"
   - "correctAnswer": Exactly one of "A", "B", "C", or "D"
   - "solution": Crisp, clear solution statement (1-2 sentences) for the review modal.

OUTPUT FORMAT:
Strict valid JSON matching this schema:
{
  "testQuestions": [
    {
      "id": 1,
      "stem": "Question stem in English...",
      "options": {
        "A": "Option A...",
        "B": "Option B...",
        "C": "Option C...",
        "D": "Option D..."
      },
      "correctAnswer": "B",
      "solution": "Crisp solution explanation in English..."
    }
  ]
}`;

  const res = await callGemini(MODEL_GEN, prompt, { temperature: 0.25 });
  const testQuestions = res.testQuestions || [];
  if (testQuestions.length < 15) {
    throw new Error(`Tab 3 returned only ${testQuestions.length} test questions (expected 15)`);
  }
  return testQuestions.slice(0, 15);
}

// ==================== HINDI TRANSLATION (gemini-3.1-flash-lite) ====================
async function translateTab1ToHindi(notesData, topic) {
  const prompt = `You are an expert bilingual translator for UP government competitive examinations (UPSSSC/UPPSC).
Translate the following English study notes into authentic, standard Hindi (शुद्ध एवं मानक प्रशासनिक हिन्दी).

TOPIC: ${topic.titleEn}
HINDI TITLE: ${topic.titleHi}

INPUT JSON:
${JSON.stringify({
  topicTag: notesData.topicTag,
  subtitle: notesData.subtitle,
  sections: notesData.sections
})}

TASK:
Return a JSON object with the exact same structure, translated accurately into Hindi:
- "topicTag": Hindi translation
- "subtitle": Hindi translation
- "sections": Array where each section has:
  - "title": Hindi title (clean, do not add section numbers)
  - "examPointer": Hindi translation of the exam fact (DO NOT add prefix like "सीधा परीक्षा तथ्य:", just translate the statement itself)
  - "table": (if present) "headers" translated to Hindi, "rows" containing translated cell arrays
  - "points": array of items with "badge" in Hindi and "content" in Hindi. Preserve standard terms (e.g. अनुच्छेद 21, दीवान-ए-आरिज, नीति आयोग) along with their standard Hindi script.

Return strictly valid JSON matching this structure without extra commentary.`;

  return await callGemini(MODEL_TRANS, prompt, { temperature: 0.15 });
}

async function translateTab2ToHindi(questions, topic) {
  const chunks = [questions.slice(0, 15), questions.slice(15, 30)];
  const translated = [];

  for (let cIdx = 0; cIdx < chunks.length; cIdx++) {
    const chunk = chunks[cIdx];
    const prompt = `You are an expert translator for UPSSSC exam papers.
Translate the following ${chunk.length} English practice MCQs into authentic standard Hindi (UPSSSC exam Hindi standard).

INPUT QUESTIONS:
${JSON.stringify(chunk.map(q => ({
  id: q.id,
  tag: q.tag,
  question: q.question,
  options: q.options,
  explanation: q.explanation
})))}

TASK:
Return a JSON array of exactly ${chunk.length} translated objects:
[
  {
    "id": ${chunk[0].id},
    "tag": "Hindi tag",
    "question": "Hindi question stem...",
    "options": {
      "A": "Hindi option A...",
      "B": "Hindi option B...",
      "C": "Hindi option C...",
      "D": "Hindi option D..."
    },
    "explanation": "Hindi explanation..."
  }
]
Maintain 1:1 correspondence for all ${chunk.length} questions. Return strictly valid JSON array.`;

    const res = await callGemini(MODEL_TRANS, prompt, { temperature: 0.15 });
    const arr = Array.isArray(res) ? res : (res.questions || res.translated || []);
    translated.push(...arr);
    if (cIdx < chunks.length - 1) await sleep(GAP_MS);
  }

  // Map by id to ensure all 30 questions exist in exact order
  const resultMap = new Map(translated.filter(Boolean).map(item => [item.id, item]));
  return questions.map((q, idx) => {
    const found = resultMap.get(q.id) || translated[idx];
    if (found && found.options && (found.question || found.stem)) {
      return {
        id: q.id,
        tag: found.tag || q.tag,
        question: found.question || found.stem || q.question,
        options: {
          A: found.options?.A || q.options?.A || '',
          B: found.options?.B || q.options?.B || '',
          C: found.options?.C || q.options?.C || '',
          D: found.options?.D || q.options?.D || ''
        },
        explanation: found.explanation || q.explanation
      };
    }
    return {
      id: q.id,
      tag: q.tag,
      question: q.question,
      options: q.options,
      explanation: q.explanation
    };
  });
}

async function translateTab3ToHindi(testQuestions, topic) {
  const prompt = `You are an expert translator for UPSSSC exam papers.
Translate the following 15 English timed test questions into authentic standard Hindi (UPSSSC standard).

INPUT TEST QUESTIONS:
${JSON.stringify(testQuestions.map(q => ({
  id: q.id,
  stem: q.stem,
  options: q.options,
  solution: q.solution
})))}

TASK:
Return a JSON array of 15 translated objects:
[
  {
    "id": 1,
    "stem": "Hindi question stem...",
    "options": {
      "A": "Hindi option A...",
      "B": "Hindi option B...",
      "C": "Hindi option C...",
      "D": "Hindi option D..."
    },
    "solution": "Hindi solution explanation..."
  }
]
Maintain 1:1 correspondence for all 15 questions. Return strictly valid JSON array.`;

  const res = await callGemini(MODEL_TRANS, prompt, { temperature: 0.15 });
  const arr = Array.isArray(res) ? res : (res.testQuestions || res.translated || []);
  const resultMap = new Map(arr.filter(Boolean).map(item => [item.id, item]));
  return testQuestions.map((tq, idx) => {
    const found = resultMap.get(tq.id) || arr[idx];
    if (found && found.options) {
      return {
        id: tq.id,
        stem: found.stem || found.question || tq.stem,
        options: {
          A: found.options?.A || tq.options?.A || '',
          B: found.options?.B || tq.options?.B || '',
          C: found.options?.C || tq.options?.C || '',
          D: found.options?.D || tq.options?.D || ''
        },
        solution: found.solution || tq.solution
      };
    }
    return {
      id: tq.id,
      stem: tq.stem,
      options: tq.options,
      solution: tq.solution
    };
  });
}

// ==================== HTML GENERATOR ====================
function escapeHtml(str) {
  return String(str || '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

function normalizeOptions(options) {
  if (!options) return { A: '', B: '', C: '', D: '' };
  if (Array.isArray(options)) {
    const res = { A: '', B: '', C: '', D: '' };
    options.forEach((opt, idx) => {
      const letter = ['A', 'B', 'C', 'D'][idx];
      if (letter) {
        res[letter] = String(opt).replace(/^[A-D][\.\:\s\-]+/, '').trim();
      }
    });
    return res;
  }
  if (typeof options === 'object') {
    return {
      A: options.A || options.a || '',
      B: options.B || options.b || '',
      C: options.C || options.c || '',
      D: options.D || options.d || ''
    };
  }
  return { A: '', B: '', C: '', D: '' };
}

function assembleNotesHtml(tab1En, tab1Hi, isHindi = false) {
  let notesHtml = '';
  const sectionsEn = tab1En.sections || [];
  const sectionsHi = tab1Hi.sections || [];

  for (let sIdx = 0; sIdx < sectionsEn.length; sIdx++) {
    const sEn = sectionsEn[sIdx];
    const sHi = sectionsHi[sIdx] || sEn;

    // Sanitize title to prevent double-numbering like "1. 1. Title"
    const rawEnTitle = isHindi ? (sHi.title || sEn.title || '') : (sEn.title || '');
    const cleanEnTitle = rawEnTitle.replace(/^(\d+[\.\s\-]+|Section\s*\d+[\:\.\s\-]*)+/i, '').trim();
    const cleanHiTitle = (sHi.title || sEn.title || '').replace(/^(\d+[\.\s\-]+|धारा\s*\d+[\:\.\s\-]*|खंड\s*\d+[\:\.\s\-]*|अनुभाग\s*\d+[\:\.\s\-]*)+/i, '').trim();

    // Sanitize exam pointer to prevent duplicate prefixes like "सीधा परीक्षा तथ्य: सीधा परीक्षा तथ्य:"
    const rawEnPointer = isHindi ? (sHi.examPointer || sEn.examPointer || '') : (sEn.examPointer || '');
    const cleanEnPointer = rawEnPointer.replace(/^(Direct Exam Fact|Exam Fact|Memory Trick|Tip|सीधा परीक्षा तथ्य|परीक्षा तथ्य)[\:\s\-]+/i, '').trim();
    const cleanHiPointer = (sHi.examPointer || sEn.examPointer || '').replace(/^(सीधा परीक्षा तथ्य|परीक्षा तथ्य|स्मृति सूत्र|टिप)[\:\s\-]+/i, '').trim();

    notesHtml += `
        <!-- Section ${sIdx + 1} -->
        <section class="notes-section">
            <h2>
                <span class="lang-en">${sIdx + 1}. ${escapeHtml(cleanEnTitle || cleanHiTitle)}</span>
                <span class="lang-hi">${sIdx + 1}. ${escapeHtml(cleanHiTitle || cleanEnTitle)}</span>
            </h2>`;

    if (cleanEnPointer || cleanHiPointer) {
      notesHtml += `
            <div class="exam-pointer">
                <span class="lang-en"><strong>${isHindi ? 'सीधा परीक्षा तथ्य:' : 'Direct Exam Fact:'}</strong> ${escapeHtml(cleanEnPointer || cleanHiPointer)}</span>
                <span class="lang-hi"><strong>सीधा परीक्षा तथ्य:</strong> ${escapeHtml(cleanHiPointer || cleanEnPointer)}</span>
            </div>`;
    }

    // Table if present
    if (sEn.table && Array.isArray(sEn.table.headers) && Array.isArray(sEn.table.rows) && sEn.table.rows.length > 0) {
      const tHi = sHi.table || sEn.table;
      notesHtml += `
            <table class="fact-table">
                <thead>
                    <tr>`;
      sEn.table.headers.forEach((hEn, hIdx) => {
        const hHi = (tHi.headers && tHi.headers[hIdx]) ? tHi.headers[hIdx] : hEn;
        const finalEnHeader = isHindi ? hHi : hEn;
        notesHtml += `
                        <th><span class="lang-en">${escapeHtml(finalEnHeader)}</span><span class="lang-hi">${escapeHtml(hHi)}</span></th>`;
      });
      notesHtml += `
                    </tr>
                </thead>
                <tbody>`;

      sEn.table.rows.forEach((rEn, rIdx) => {
        const rHi = (tHi.rows && tHi.rows[rIdx]) ? tHi.rows[rIdx] : rEn;
        notesHtml += `
                    <tr>`;
        rEn.forEach((cellEn, cIdx) => {
          const cellHi = (rHi && rHi[cIdx]) ? rHi[cIdx] : cellEn;
          const finalEnCell = isHindi ? cellHi : cellEn;
          notesHtml += `
                        <td><span class="lang-en">${escapeHtml(finalEnCell)}</span><span class="lang-hi">${escapeHtml(cellHi)}</span></td>`;
        });
        notesHtml += `
                    </tr>`;
      });

      notesHtml += `
                </tbody>
            </table>`;
    }

    // Points
    if (Array.isArray(sEn.points) && sEn.points.length > 0) {
      notesHtml += `
            <ul class="point-list">`;
      const ptsHi = sHi.points || sEn.points;
      sEn.points.forEach((pEn, pIdx) => {
        const pHi = ptsHi[pIdx] || pEn;
        const finalEnContent = isHindi ? (pHi.content || pEn.content) : pEn.content;
        notesHtml += `
                <li>
                    <span class="key-badge">${escapeHtml(pEn.badge)}</span>
                    <span class="lang-en">${escapeHtml(finalEnContent)}</span>
                    <span class="lang-hi">${escapeHtml(pHi.content || pEn.content)}</span>
                </li>`;
      });
      notesHtml += `
            </ul>`;
    }

    notesHtml += `
        </section>`;
  }

  return notesHtml;
}

function assembleTopicHtml(topic, tab1En, tab1Hi, tab2En, tab2Hi, tab3En, tab3Hi) {
  const isHindi = (topic.subject === 'hindi');
  const pageCanonical = `https://sjmaths.com/upsssc-intermediate-level/${topic.subject}/${topic.slug}/`;
  const subjectAnchor = `/upsssc-intermediate-level/#subj-${topic.subject === 'rural-development' ? 'rural' : (topic.subject === 'science-tech' ? 'sci' : (topic.subject === 'environment' ? 'env' : (topic.subject === 'hindi' ? 'hin' : (topic.subject === 'economy' ? 'eco' : (topic.subject === 'geography' ? 'geo' : (topic.subject === 'history' ? 'hist' : 'polity'))))))}`;

  // Tab 1 Notes HTML
  const notesHtml = assembleNotesHtml(tab1En, tab1Hi, isHindi);

  // Tab 2 Practice Questions HTML (30 MCQs)
  let quizCardsHtml = '';
  for (let i = 0; i < 30; i++) {
    const qEn = tab2En[i];
    const qHi = tab2Hi[i] || qEn;
    const qNum = i + 1;
    const correctOpt = qEn.correctAnswer || 'A';
    const tagDisplay = isHindi ? (qHi.tag || topic.subjectTitleHi) : (qEn.tag || topic.subjectTitleEn);

    quizCardsHtml += `
            <!-- Question ${qNum} -->
            <div class="question-card" id="q-${qNum}">
                <div class="q-meta">
                    <span class="q-num">Question ${qNum}</span>
                    <span class="q-tag">${escapeHtml(tagDisplay)}</span>
                </div>
                <div class="q-text lang-en">${escapeHtml(isHindi ? (qHi.question || qEn.question) : qEn.question)}</div>
                <div class="q-text lang-hi">${escapeHtml(qHi.question || qEn.question)}</div>
                <div class="options-grid">`;

    const optsEn = normalizeOptions(qEn.options);
    const optsHi = normalizeOptions(qHi.options || qEn.options);

    ['A', 'B', 'C', 'D'].forEach(letter => {
      const optEn = optsEn[letter] || '';
      const optHi = optsHi[letter] || optEn;
      const optLabel = isHindi ? `${letter}. ${escapeHtml(optHi)}` : `${letter}. ${escapeHtml(optEn)} / ${escapeHtml(optHi)}`;
      quizCardsHtml += `
                    <button class="opt-btn" data-opt="${letter}" onclick="checkAnswer(this, '${correctOpt}', ${qNum})">${optLabel}</button>`;
    });

    const solBadgeEn = isHindi ? `सही उत्तर: ${correctOpt}` : `Correct Answer: ${correctOpt}`;
    const solPrefixEn = isHindi ? '<strong>व्याख्या:</strong>' : '<strong>Explanation:</strong>';

    quizCardsHtml += `
                </div>
                <div class="solution-box" id="sol-${qNum}">
                    <div class="sol-badge correct"><i class="fas fa-check-circle"></i> <span class="lang-en">${solBadgeEn}</span><span class="lang-hi">सही उत्तर: ${correctOpt}</span></div>
                    <p class="sol-text lang-en">${solPrefixEn} ${escapeHtml(isHindi ? (qHi.explanation || qEn.explanation) : qEn.explanation)}</p>
                    <p class="sol-text lang-hi"><strong>व्याख्या:</strong> ${escapeHtml(qHi.explanation || qEn.explanation)}</p>
                </div>
            </div>`;
  }

  // Tab 3 Mini Test HTML (15 Qs)
  let testBoxesHtml = '';
  const testDataArray = [];

  for (let i = 0; i < 15; i++) {
    const tqEn = tab3En[i];
    const tqHi = tab3Hi[i] || tqEn;
    const qNum = i + 1;
    const correctOpt = tqEn.correctAnswer || 'A';

    testDataArray.push({
      ans: correctOpt,
      solEn: isHindi ? (tqHi.solution || tqEn.solution || '') : (tqEn.solution || ''),
      solHi: tqHi.solution || tqEn.solution || ''
    });

    const toptsEn = normalizeOptions(tqEn.options);
    const toptsHi = normalizeOptions(tqHi.options || tqEn.options);

    testBoxesHtml += `
            <!-- Test Q${qNum} -->
            <div class="test-q-box" id="tq-${i}" data-ans="${correctOpt}">
                <div class="tq-header">
                    <span class="tq-number">${qNum} / 15</span>
                    <span class="tq-weight">1 Mark</span>
                </div>
                <div class="tq-stem lang-en">${escapeHtml(isHindi ? (tqHi.stem || tqEn.stem) : tqEn.stem)}</div>
                <div class="tq-stem lang-hi">${escapeHtml(tqHi.stem || tqEn.stem)}</div>
                <div class="tq-options">`;

    ['A', 'B', 'C', 'D'].forEach(letter => {
      const optEn = toptsEn[letter] || '';
      const optHi = toptsHi[letter] || optEn;
      const optLabel = isHindi ? `${letter}. ${escapeHtml(optHi)}` : `${letter}. ${escapeHtml(optEn)} / ${escapeHtml(optHi)}`;
      testBoxesHtml += `
                    <label class="tq-opt-label"><input type="radio" name="tq_ans_${i}" value="${letter}"> ${optLabel}</label>`;
    });

    testBoxesHtml += `
                </div>
            </div>`;
  }

  // Full HTML Document
  return `<!DOCTYPE html>
<html lang="en">
<head>
<script async="" crossorigin="anonymous" src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7924751316191829"></script>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>${escapeHtml(topic.titleEn)}: Notes &amp; Practice | UPSSSC Mains | SJMaths</title>
<meta content="Pointwise study notes, 30 practice questions with solutions, and a 15-Q interactive test on ${escapeHtml(topic.titleEn)} for UPSSSC Intermediate Level Mains 2026." name="description"/>
<meta content="index, follow, max-image-preview:large" name="robots"/>
<link href="${pageCanonical}" rel="canonical"/>
<meta content="${escapeHtml(topic.titleEn)} | UPSSSC Mains" property="og:title"/>
<meta content="Pointwise study notes, 30 revision questions, and interactive test on ${escapeHtml(topic.titleEn)} for UPSSSC Intermediate Level Mains." property="og:description"/>
<meta content="${pageCanonical}" property="og:url"/>
<meta content="article" property="og:type"/>
<meta content="SJMaths" property="og:site_name"/>
<meta content="https://sjmaths.com/assets/icons/icon-512x512.png" property="og:image"/>
<meta content="summary_large_image" name="twitter:card"/>
<meta content="${escapeHtml(topic.titleEn)} | UPSSSC Mains" name="twitter:title"/>
<meta content="Pointwise study notes, 30 practice questions, and interactive test on ${escapeHtml(topic.titleEn)}." name="twitter:description"/>
<meta content="https://sjmaths.com/assets/icons/icon-512x512.png" name="twitter:image"/>
<link href="/favicon.png" rel="icon" type="image/png"/>

<!-- Instant Theme & Language Initialization (Prevents FOUC & Double Text) -->
<script>
(function() {
  try {
    var p = localStorage.getItem('sjmaths.theme.preference') || 
            (localStorage.getItem('sjmaths-dark') === 'on' ? 'dark' : 
            (localStorage.getItem('theme') || 'system'));
    var d = p === 'dark' || (p === 'system' && window.matchMedia('(prefers-color-scheme: dark)').matches);
    if (d) {
      document.documentElement.classList.add('dark-mode');
      document.documentElement.setAttribute('data-theme', 'dark');
      document.documentElement.style.colorScheme = 'dark';
    }

    var lang = localStorage.getItem('sjmaths_preferred_language') || localStorage.getItem('sj_pref_lang') || 'en';
    if (lang === 'hi') {
      document.documentElement.classList.add('lang-hi', 'lang-mode-hi');
      document.documentElement.classList.remove('lang-en');
      document.documentElement.lang = 'hi';
    } else {
      document.documentElement.classList.add('lang-en');
      document.documentElement.classList.remove('lang-hi', 'lang-mode-hi');
      document.documentElement.lang = 'en';
    }
  } catch(e) {}
})();
</script>

<!-- Fonts & Icons -->
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400..700;1,9..40,400..700&amp;family=Outfit:wght@400..800&amp;display=swap" rel="stylesheet"/>
<link as="style" crossorigin="anonymous" href="/assets/vendor/fontawesome/css/all.min.css?v=db73e473" onload="this.onload=null;this.rel='stylesheet'" rel="preload"/>
<noscript>
<link href="/assets/vendor/fontawesome/css/all.min.css?v=db73e473" rel="stylesheet"/>
</noscript>

<!-- Stylesheets -->
<link href="/assets/css/main.min.css?v=e4c665a0" rel="stylesheet"/>
<link href="/assets/css/layout.min.css?v=e4922b08" rel="stylesheet"/>
<link href="/assets/css/component.min.css?v=85dbb37c" rel="stylesheet"/>
<!-- Schema.org Data -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Article",
      "headline": "${escapeHtml(topic.titleEn)} - UPSSSC Mains",
      "description": "Pointwise study notes, 30 practice questions with solutions, and a 15-question interactive test on ${escapeHtml(topic.titleEn)}.",
      "url": "${pageCanonical}",
      "inLanguage": ["en", "hi"],
      "publisher": {
        "@type": "Organization",
        "name": "SJMaths",
        "url": "https://sjmaths.com"
      }
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://sjmaths.com/" },
        { "@type": "ListItem", "position": 2, "name": "UPSSSC Intermediate Level", "item": "https://sjmaths.com/upsssc-intermediate-level/" },
        { "@type": "ListItem", "position": 3, "name": "${escapeHtml(topic.subjectTitleEn)}", "item": "https://sjmaths.com${subjectAnchor}" },
        { "@type": "ListItem", "position": 4, "name": "${escapeHtml(topic.titleEn)}", "item": "${pageCanonical}" }
      ]
    }
  ]
}
</script>

<link href="/assets/css/upsssc-intermediate.min.css?v=91ebe014" rel="stylesheet"/>
</head>
<body class="exam-ui">
<div id="header-container"></div>
<main class="topic-page-container" id="main-content">

<!-- Top Bar: Breadcrumbs & Dedicated Bilingual Language Toggle -->
<div class="page-top-bar">
    <div class="breadcrumbs-path">
        <a href="/"><i class="fas fa-home"></i> <span class="lang-en">Home</span><span class="lang-hi">होम</span></a>
        <i class="fas fa-chevron-right"></i>
        <a href="/upsssc-intermediate-level/"><span class="lang-en">UPSSSC Intermediate Level</span><span class="lang-hi">यूपीएसएसएससी इंटरमीडिएट स्तर</span></a>
        <i class="fas fa-chevron-right"></i>
        <a href="${subjectAnchor}"><span class="lang-en">${escapeHtml(isHindi ? topic.subjectTitleHi : topic.subjectTitleEn)}</span><span class="lang-hi">${escapeHtml(topic.subjectTitleHi)}</span></a>
        <i class="fas fa-chevron-right"></i>
        <span class="lang-en">${escapeHtml(isHindi ? topic.titleHi.split(':')[0] : topic.titleEn.split(':')[0])}</span>
        <span class="lang-hi">${escapeHtml(topic.titleHi.split(':')[0])}</span>
    </div>

    <!-- On-Page Language Toggle Button -->
    <button class="lang-toggle-pill" id="pageLangToggle" onclick="toggleLanguageMode()" aria-label="Switch Language / भाषा बदलें">
        <i class="fas fa-language" style="color: #0284c7;"></i>
        <span class="lang-en">हिंदी में पढ़ें</span>
        <span class="lang-hi">Read in English</span>
    </button>
</div>

<!-- Header -->
<div class="topic-header">
    <div class="topic-meta-tag">
        <span class="lang-en">${escapeHtml(isHindi ? (tab1Hi.topicTag || topic.subSectionHi) : (tab1En.topicTag || topic.subSectionEn))}</span>
        <span class="lang-hi">${escapeHtml(tab1Hi.topicTag || topic.subSectionHi)}</span>
    </div>
    <h1>
        <span class="lang-en">${escapeHtml(isHindi ? topic.titleHi : topic.titleEn)}</span>
        <span class="lang-hi">${escapeHtml(topic.titleHi)}</span>
    </h1>
    <p class="topic-subtitle">
        <span class="lang-en">${escapeHtml(isHindi ? (tab1Hi.subtitle || tab1En.subtitle) : (tab1En.subtitle || 'High-yield revision notes, 30 bilingual multiple choice practice questions, and a 15-question interactive timed mini test for UPSSSC Intermediate Level Mains Examination.'))}</span>
        <span class="lang-hi">${escapeHtml(tab1Hi.subtitle || 'यूपीएसएसएससी इंटरमीडिएट स्तरीय मुख्य परीक्षा हेतु बिंदुवार रिवीज़न नोट्स, 30 द्विभाषी बहुविकल्पीय अभ्यास प्रश्न और 15 प्रश्नों का समयबद्ध मिनी टेस्ट।')}</span>
    </p>
</div>

<!-- Tabs Navigation -->
<div class="topic-tabs-bar">
    <button class="topic-tab-btn active" onclick="switchTopicTab('notes')">
        <i class="fas fa-book-open"></i>
        <span class="lang-en">${isHindi ? 'बिंदुवार नोट्स' : 'Pointwise Notes'}</span>
        <span class="lang-hi">बिंदुवार नोट्स</span>
    </button>
    <button class="topic-tab-btn" onclick="switchTopicTab('quiz')">
        <i class="fas fa-question-circle"></i>
        <span class="lang-en">${isHindi ? '30 अभ्यास प्रश्न' : '30 Practice MCQs'}</span>
        <span class="lang-hi">30 अभ्यास प्रश्न</span>
    </button>
    <button class="topic-tab-btn" onclick="switchTopicTab('test')">
        <i class="fas fa-stopwatch"></i>
        <span class="lang-en">${isHindi ? '15 प्रश्न मिनी टेस्ट' : '15-Q Mini Test'}</span>
        <span class="lang-hi">15 प्रश्न मिनी टेस्ट</span>
    </button>
</div>

<!-- Tab 1: Pointwise Revision Notes -->
<div class="topic-tab-pane active" id="pane-notes">
    <div class="study-notes-wrapper">
${notesHtml}
    </div>
</div>

<!-- Tab 2: 30 Practice MCQs -->
<div class="topic-tab-pane" id="pane-quiz" style="display: none;">
    <div class="practice-quiz-wrapper">
        <div class="quiz-instruction-banner">
            <div class="quiz-info-left">
                <i class="fas fa-lightbulb"></i>
                <div>
                    <h3 class="lang-en">30 High-Yield Exam Practice Questions</h3>
                    <h3 class="lang-hi">30 उच्च-प्राथमिकता परीक्षा अभ्यास प्रश्न</h3>
                    <p class="lang-en">Click an option to immediately test your understanding. Instant feedback &amp; comprehensive explanations are revealed.</p>
                    <p class="lang-hi">अपनी समझ का परीक्षण करने के लिए विकल्प चुनें। तुरंत सही उत्तर एवं विस्तृत व्याख्या प्रदर्शित होगी।</p>
                </div>
            </div>
            <div class="quiz-progress-chip">
                <span class="lang-en">Answered:</span>
                <span class="lang-hi">हल किए:</span>
                <strong id="quizAnsweredBadge">0/30</strong>
            </div>
        </div>

        <div class="questions-list">
${quizCardsHtml}
        </div>
    </div>
</div>

<!-- Tab 3: 15-Question Timed Mini Test -->
<div class="topic-tab-pane" id="pane-test" style="display: none;">
    <div class="test-container-wrapper">
        <div class="test-hero-card">
            <div class="test-hero-header">
                <div>
                    <span class="test-badge">UPSSSC Exam Pattern</span>
                    <h2>
                        <span class="lang-en">Timed Mini Test: 15 Questions</span>
                        <span class="lang-hi">समयबद्ध मिनी टेस्ट: 15 प्रश्न</span>
                    </h2>
                    <p class="test-rule-note">
                        <span class="lang-en">15 Minutes | 15 Questions | +1 Mark for Correct | -0.25 Negative Marking for Incorrect</span>
                        <span class="lang-hi">15 मिनट | 15 प्रश्न | सही उत्तर पर +1 अंक | गलत उत्तर पर -0.25 ऋणात्मक अंकन</span>
                    </p>
                </div>
                <div class="test-timer-badge">
                    <i class="fas fa-stopwatch"></i>
                    <span id="testTimer">15:00</span>
                </div>
            </div>

            <!-- 15 Test Questions Box -->
            <div class="test-questions-box">
${testBoxesHtml}
            </div>

            <!-- Submit Button Area -->
            <div class="test-actions-bar">
                <button class="test-submit-btn" id="testSubmitBtn" onclick="submitMiniTest()">
                    <i class="fas fa-paper-plane"></i>
                    <span class="lang-en">Submit Mini Test &amp; View Result</span>
                    <span class="lang-hi">मिनी टेस्ट सबमिट करें व परिणाम देखें</span>
                </button>
            </div>

            <!-- Result Scorecard Container -->
            <div class="test-scorecard" id="testScorecard" style="display: none;">
                <div class="scorecard-header">
                    <div class="score-circle">
                        <span id="scoreValue">0</span>
                        <small>/ 15</small>
                    </div>
                    <div class="score-details">
                        <h4 id="scoreFeedback">Test Completed!</h4>
                        <p id="scoreBreakdown">Correct: 0 | Incorrect: 0 | Unattempted: 15</p>
                    </div>
                </div>
                <div class="scorecard-actions">
                    <button class="review-btn" onclick="reviewTestAnswers()">
                        <i class="fas fa-eye"></i>
                        <span class="lang-en">Review Answers &amp; Explanations</span>
                        <span class="lang-hi">उत्तर एवं व्याख्या देखें</span>
                    </button>
                    <button class="retake-btn" onclick="resetMiniTest()">
                        <i class="fas fa-redo"></i>
                        <span class="lang-en">Retake Test</span>
                        <span class="lang-hi">पुनः टेस्ट दें</span>
                    </button>
                </div>
            </div>

        </div>
    </div>
</div>

</main>
<div id="footer-container"></div>

<script>
// Test Data Configuration for ${escapeHtml(topic.titleEn)}
window.upssscTestData = [
    ${testDataArray.map(item => JSON.stringify(item)).join(',\n    ')}
];
</script>

<!-- JS Scripts -->
<script data-cfasync="false" defer="" src="/assets/js/search.min.js?v=a16d370a"></script>
<script data-cfasync="false" defer="" src="/assets/js/main.min.js?v=b47d6b04"></script>
<script data-cfasync="false" defer="" src="/assets/js/global-header.min.js?v=36197f29"></script>
<script data-cfasync="false" defer="" src="/assets/js/global-footer.min.js?v=ea62137b"></script>
<script defer src="/assets/js/upsssc-intermediate.min.js?v=a2f3fc07"></script>
<script defer src="/assets/js/mobile-tab-dock.min.js?v=71d1adf2-mobile-tab-dock-v7"></script>
</body>
</html>
`;
}

// ==================== HUB INDEX LINK UPDATER ====================
function updateHubIndexLinks() {
  if (!fs.existsSync(HUB_INDEX_FILE)) {
    console.warn('⚠️ Hub index.html not found at:', HUB_INDEX_FILE);
    return;
  }

  let html = fs.readFileSync(HUB_INDEX_FILE, 'utf8');
  let updateCount = 0;

  for (const topic of UPSSSC_INTERMEDIATE_TOPICS) {
    const targetHref = `./${topic.subject}/${topic.slug}/`;
    // Regex matches the input tag with id="<topic.id>" followed by the <a> tag
    const regex = new RegExp(`(<input[^>]*id="${topic.id}"[^>]*>\\s*<a[^>]*href=")([^"]*)(")`, 'g');

    if (regex.test(html)) {
      html = html.replace(regex, (match, p1, oldHref, p3) => {
        if (oldHref !== targetHref) {
          updateCount++;
          return `${p1}${targetHref}${p3}`;
        }
        return match;
      });
    }
  }

  if (updateCount > 0) {
    fs.writeFileSync(HUB_INDEX_FILE, html, 'utf8');
    console.log(`✅ Updated ${updateCount} topic link(s) in upsssc-intermediate-level/index.html`);
  } else {
    console.log('ℹ️ All topic links in upsssc-intermediate-level/index.html are already up-to-date.');
  }
}

// ==================== TOPIC GENERATOR PIPELINE ====================
async function processTopic(topic) {
  const topicDir = path.join(INTERMEDIATE_DIR, topic.subject, topic.slug);
  const targetFile = path.join(topicDir, 'index.html');

  console.log(`\n============================================================`);
  console.log(`🚀 Processing [${topic.id}]: ${topic.titleEn}`);
  console.log(`📁 Target: ${targetFile}`);

  if (ENRICH_NOTES) {
    if (!fs.existsSync(targetFile)) {
      console.log(`⚠️ Target file does not exist for [${topic.id}]. Generating full topic...`);
    } else {
      console.log(`✨ [ENRICH MODE] Regenerating Tab 1 (Exhaustive Study Notes) for [${topic.id}]...`);
      // Step 1: Generate Tab 1 with gemini-3.5-flash-lite
      console.log(`📖 Generating Tab 1 (Exhaustive Pointwise Notes) using ${MODEL_GEN}...`);
      const tab1En = await generateTab1Notes(topic);
      console.log(`   ✓ Tab 1 generated with ${tab1En.sections?.length || 0} exhaustive sections`);
      await sleep(GAP_MS);

      // Step 2: Translate Tab 1 into Hindi using gemini-3.1-flash-lite
      console.log(`🇮🇳 Translating Tab 1 to Hindi using ${MODEL_TRANS}...`);
      const tab1Hi = await translateTab1ToHindi(tab1En, topic);
      await sleep(GAP_MS);

      // Step 3: Replace Tab 1 inside existing targetFile
      console.log(`📄 Updating HTML with enriched study notes...`);
      let existingHtml = fs.readFileSync(targetFile, 'utf8');
      const enrichedNotesHtml = assembleNotesHtml(tab1En, tab1Hi);

      // Replace Tab 1 content supporting all 3 UPSSSC Intermediate template variants
      const p1 = /(<div class="study-notes-wrapper">)[\s\S]*?(<\/div>\s*<\/div>\s*(?:<!--[^\n]*\n)*\s*<!--\s*Tab 2:)/;
      const p2 = /(<div class="topic-tab-pane[^"]*" id="pane-notes"[^>]*>)[\s\S]*?(<\/div>\s*(?:<!--[^\n]*\n)*\s*<div[^>]*id="pane-practice")/;
      const p3 = /(<div class="tab-content[^"]*" id="tab-theory"[^>]*>)[\s\S]*?(<\/div>\s*(?:<!--[^\n]*\n)*\s*<div[^>]*id="tab-practice")/;

      if (p1.test(existingHtml)) {
        existingHtml = existingHtml.replace(p1, `$1\n${enrichedNotesHtml}\n    $2`);
      } else if (p2.test(existingHtml)) {
        existingHtml = existingHtml.replace(p2, `$1\n    <div class="study-notes-wrapper">\n${enrichedNotesHtml}\n    </div>\n$2`);
      } else if (p3.test(existingHtml)) {
        existingHtml = existingHtml.replace(p3, `$1\n    <div class="study-notes-wrapper">\n${enrichedNotesHtml}\n    </div>\n$2`);
      } else {
        console.warn(`⚠️ Could not match study-notes-wrapper or tab container precisely, skipping partial replacement.`);
        return false;
      }

      // Also update meta subtitle and header subtitle if present
      if (tab1En.subtitle && tab1Hi.subtitle) {
        existingHtml = existingHtml.replace(
          /<p class="topic-subtitle">[\s\S]*?<\/p>/,
          `<p class="topic-subtitle">\n        <span class="lang-en">${escapeHtml(tab1En.subtitle)}</span>\n        <span class="lang-hi">${escapeHtml(tab1Hi.subtitle)}</span>\n    </p>`
        );
      }
      if (tab1En.topicTag && tab1Hi.topicTag) {
        existingHtml = existingHtml.replace(
          /<div class="topic-meta-tag">[\s\S]*?<\/div>/,
          `<div class="topic-meta-tag">\n        <span class="lang-en">${escapeHtml(tab1En.topicTag)}</span>\n        <span class="lang-hi">${escapeHtml(tab1Hi.topicTag)}</span>\n    </div>`
        );
      }

      fs.writeFileSync(targetFile, existingHtml, 'utf8');
      const passed = isTopicComplete(targetFile);
      if (passed) {
        console.log(`✅ ENRICHED SUCCESS! Verified [${topic.id}] (${(existingHtml.length / 1024).toFixed(1)} KB)`);
        return true;
      } else {
        console.error(`❌ Validation failed after enriching [${topic.id}]!`);
        return false;
      }
    }
  }

  if (!FORCE && isTopicComplete(targetFile)) {
    console.log(`⏭️  Already complete! Skipping. (Use --force or --enrich-notes)`);
    return true;
  }

  if (DRY_RUN) {
    console.log(`[DRY-RUN] Would generate tabs 1, 2, 3 with ${MODEL_GEN} and translate with ${MODEL_TRANS}`);
    return true;
  }

  // Ensure directory exists
  fs.mkdirSync(topicDir, { recursive: true });

  // Step 1: Generate Tab 1 with gemini-3.5-flash-lite
  console.log(`📖 [1/5] Generating Tab 1 (Pointwise Notes) using ${MODEL_GEN}...`);
  const tab1En = await generateTab1Notes(topic);
  console.log(`   ✓ Tab 1 generated with ${tab1En.sections?.length || 0} sections`);
  await sleep(GAP_MS);

  // Step 2: Generate Tab 2 with gemini-3.5-flash-lite
  console.log(`❓ [2/5] Generating Tab 2 (30 Practice MCQs) using ${MODEL_GEN}...`);
  const tab2En = await generateTab2PracticeMCQs(topic);
  console.log(`   ✓ Tab 2 generated with ${tab2En.length} MCQs`);
  await sleep(GAP_MS);

  // Step 3: Generate Tab 3 with gemini-3.5-flash-lite
  console.log(`⏱️  [3/5] Generating Tab 3 (15-Q Timed Mini Test) using ${MODEL_GEN}...`);
  const tab3En = await generateTab3MiniTest(topic);
  console.log(`   ✓ Tab 3 generated with ${tab3En.length} test questions`);
  await sleep(GAP_MS);

  // Step 4: Translate Tab 1, 2, 3 into Hindi using gemini-3.1-flash-lite
  console.log(`🇮🇳 [4/5] Translating Tabs to Hindi using ${MODEL_TRANS}...`);
  console.log(`   Translating Tab 1 Notes...`);
  const tab1Hi = await translateTab1ToHindi(tab1En, topic);
  await sleep(GAP_MS);

  console.log(`   Translating Tab 2 MCQs (30 questions)...`);
  const tab2Hi = await translateTab2ToHindi(tab2En, topic);
  await sleep(GAP_MS);

  console.log(`   Translating Tab 3 Mini Test (15 questions)...`);
  const tab3Hi = await translateTab3ToHindi(tab3En, topic);
  await sleep(GAP_MS);

  // Step 5: Assemble Full HTML & Write to disk
  console.log(`📄 [5/5] Assembling bilingual HTML page...`);
  const fullHtml = assembleTopicHtml(topic, tab1En, tab1Hi, tab2En, tab2Hi, tab3En, tab3Hi);
  fs.writeFileSync(targetFile, fullHtml, 'utf8');

  // Verify generated file
  const passed = isTopicComplete(targetFile);
  if (passed) {
    console.log(`✅ SUCCESS! Verified [${topic.id}] (${(fullHtml.length / 1024).toFixed(1)} KB)`);
    const status = readStatus();
    status[topic.id] = {
      completedAt: new Date().toISOString(),
      subject: topic.subject,
      slug: topic.slug,
      path: path.relative(ROOT_DIR, targetFile)
    };
    writeStatus(status);
    return true;
  } else {
    console.error(`❌ Validation failed for [${topic.id}] after file write!`);
    return false;
  }
}

// ==================== MAIN EXECUTION ====================
async function main() {
  console.log(`============================================================`);
  console.log(` UPSSSC Intermediate Level Generator (Gemini 3.5 & 3.1)`);
  console.log(` Model Gen:   ${MODEL_GEN}`);
  console.log(` Model Trans: ${MODEL_TRANS}`);
  console.log(` Total Catalog Topics: ${UPSSSC_INTERMEDIATE_TOPICS.length}`);
  console.log(`============================================================`);

  if (LIST_ONLY) {
    console.log('\nCatalog Topics Status:');
    let completedCount = 0;
    UPSSSC_INTERMEDIATE_TOPICS.forEach((t, idx) => {
      const targetFile = path.join(INTERMEDIATE_DIR, t.subject, t.slug, 'index.html');
      const isDone = isTopicComplete(targetFile);
      if (isDone) completedCount++;
      const mark = isDone ? '✅ [DONE]' : '⏳ [TODO]';
      console.log(`${String(idx + 1).padStart(2, ' ')}. ${mark} [${t.subject}] ${t.id} -> ${t.slug}`);
    });
    console.log(`\nSummary: ${completedCount}/${UPSSSC_INTERMEDIATE_TOPICS.length} topics generated.`);
    return;
  }

  if (UPDATE_HUB) {
    updateHubIndexLinks();
    return;
  }

  // Filter topics based on CLI arguments
  let targetTopics = UPSSSC_INTERMEDIATE_TOPICS;

  if (SUBJECT_FILTER) {
    targetTopics = targetTopics.filter(t => t.subject === SUBJECT_FILTER || t.id.startsWith(SUBJECT_FILTER));
    console.log(`Filtering by subject "${SUBJECT_FILTER}": ${targetTopics.length} topics found.`);
  }

  if (TOPIC_FILTER) {
    targetTopics = targetTopics.filter(t => t.id === TOPIC_FILTER || t.slug === TOPIC_FILTER || t.id.includes(TOPIC_FILTER));
    console.log(`Filtering by topic "${TOPIC_FILTER}": ${targetTopics.length} topics found.`);
  }

  if (LIMIT > 0) {
    targetTopics = targetTopics.slice(0, LIMIT);
    console.log(`Applying limit of ${LIMIT} topics.`);
  }

  if (targetTopics.length === 0) {
    console.log('No topics matched the criteria.');
    return;
  }

  console.log(`\nWill process ${targetTopics.length} topic(s).`);

  let successCount = 0;
  let failureCount = 0;

  for (let i = 0; i < targetTopics.length; i++) {
    const topic = targetTopics[i];
    console.log(`\n[Progress: ${i + 1}/${targetTopics.length}]`);
    try {
      const ok = await processTopic(topic);
      if (ok) successCount++;
      else failureCount++;
    } catch (err) {
      console.error(`❌ Fatal error processing [${topic.id}]:`, err.message);
      failureCount++;
    }
  }

  // Update hub index links
  console.log(`\nUpdating Hub Index links in upsssc-intermediate-level/index.html...`);
  updateHubIndexLinks();

  console.log(`\n============================================================`);
  console.log(` Execution Summary:`);
  console.log(`   Success: ${successCount}`);
  console.log(`   Failed:  ${failureCount}`);
  console.log(`============================================================\n`);
}

main().catch(err => {
  console.error('Fatal crash in main():', err);
  process.exit(1);
});
