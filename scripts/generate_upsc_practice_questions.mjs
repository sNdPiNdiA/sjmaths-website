#!/usr/bin/env node
/**
 * UPSC Microtopic Practice Question Generator
 * Generates 30 high-yield, authentic UPSC Prelims & Mains practice questions per microtopic
 * using Gemini 3.5 Flash Lite with 1 API call per page and rotating API keys.
 *
 * Supported subjects:
 *   ancient-history, medieval-history, modern-history, art-and-culture, polity, economy
 *
 * Usage:
 *   node scripts/generate_upsc_practice_questions.mjs --dry-run
 *   node scripts/generate_upsc_practice_questions.mjs --subject ancient-history --limit 1
 *   node scripts/generate_upsc_practice_questions.mjs --topic upsc/ancient-history/Age-of-Mahajanapadas/Administrative-Setup
 *   node scripts/generate_upsc_practice_questions.mjs --limit 6 (1 from each subject)
 */

import fs from 'node:fs';
import path from 'node:path';
import 'dotenv/config';
import { GoogleGenAI } from '@google/genai';
import { jsonrepair } from 'jsonrepair';

const ROOT = process.cwd();
const MODEL = process.env.GEMINI_MODEL || 'gemini-3.1-flash-lite';
const FALLBACK_MODEL = 'gemini-2.5-flash';

// API Key rotation
const API_KEYS = [
  process.env.GEMINI_API_KEY_1,
  process.env.GEMINI_API_KEY_2,
  process.env.GEMINI_API_KEY_3 || process.env.GEMINI_API_KEY
].filter(Boolean);

if (API_KEYS.length === 0) {
  console.error('❌ No GEMINI_API_KEY found in environment or .env');
  process.exit(1);
}

let keyIndex = 0;
function getNextAIClient() {
  const currentKey = API_KEYS[keyIndex % API_KEYS.length];
  const keyId = (keyIndex % API_KEYS.length) + 1;
  keyIndex++;
  return {
    client: new GoogleGenAI({ apiKey: currentKey }),
    keyId: `KEY_${keyId}`
  };
}

// Target subject directories
const SUBJECT_MAP = {
  'ancient': 'ancient-history',
  'ancient-history': 'ancient-history',
  'medieval': 'medieval-history',
  'medieval-history': 'medieval-history',
  'modern': 'modern-history',
  'moden': 'modern-history',
  'modern-history': 'modern-history',
  'art': 'art-and-culture',
  'culture': 'art-and-culture',
  'art-and-culture': 'art-and-culture',
  'polity': 'polity',
  'economy': 'economy'
};

const args = process.argv.slice(2);
const hasFlag = (f) => args.includes(f);
function getArg(flag) {
  const i = args.indexOf(flag);
  return i >= 0 ? args[i + 1] : null;
}

const dryRun = hasFlag('--dry-run');
const force = hasFlag('--force');
const requestedSubject = getArg('--subject');
const requestedTopic = getArg('--topic');
const requestedLimit = getArg('--limit') ? parseInt(getArg('--limit'), 10) : 0;
const perSubjectLimit = getArg('--per-subject') ? parseInt(getArg('--per-subject'), 10) : 0;
const requestedConcurrency = getArg('--concurrency') ? parseInt(getArg('--concurrency'), 10) : 1;

// Resolve target subjects
let targetSubjectDirs = Object.values(SUBJECT_MAP);
targetSubjectDirs = [...new Set(targetSubjectDirs)];

if (requestedSubject) {
  const matched = [];
  for (const s of requestedSubject.split(',')) {
    const clean = s.trim().toLowerCase();
    if (SUBJECT_MAP[clean]) matched.push(SUBJECT_MAP[clean]);
  }
  if (matched.length > 0) targetSubjectDirs = [...new Set(matched)];
}

console.log('====================================================');
console.log('   UPSC Practice Question Generator (30 Qs/page)   ');
console.log('====================================================');
console.log(`Model:         ${MODEL} (fallback: ${FALLBACK_MODEL})`);
console.log(`API Keys:      ${API_KEYS.length} available (rotating 1 call/page)`);
console.log(`Subjects:      ${targetSubjectDirs.join(', ')}`);
console.log(`Dry Run:       ${dryRun}`);
console.log(`Force:         ${force}`);
if (requestedLimit) console.log(`Total Limit:   ${requestedLimit}`);
if (perSubjectLimit) console.log(`Per-Subject:   ${perSubjectLimit}`);
console.log('====================================================\n');

// Discover topic pages
function discoverTopicFiles() {
  const files = [];
  for (const subj of targetSubjectDirs) {
    const subjDir = path.join(ROOT, 'upsc', subj);
    if (!fs.existsSync(subjDir)) continue;

    function walk(dir) {
      for (const item of fs.readdirSync(dir, { withFileTypes: true })) {
        const full = path.join(dir, item.name);
        if (item.isDirectory()) {
          walk(full);
        } else if (item.name === 'index.html') {
          // Check if it's an actual topic page with a practice tab
          try {
            const text = fs.readFileSync(full, 'utf8');
            if (text.includes('tab-practice') || text.includes('practice-panel')) {
              files.push({ subject: subj, file: full });
            }
          } catch {}
        }
      }
    }
    walk(subjDir);
  }
  return files;
}

const allDiscovered = discoverTopicFiles();

// Filter topics that lack practice questions (unless --force)
const candidates = [];
for (const item of allDiscovered) {
  if (requestedTopic && !item.file.replace(/\\/g, '/').includes(requestedTopic.replace(/\\/g, '/'))) {
    continue;
  }

  if (force) {
    candidates.push(item);
    continue;
  }

  const content = fs.readFileSync(item.file, 'utf8');
  let hasQuestions = false;

  // Check upsc-page-data
  const pageMatch = content.match(/<script id="upsc-page-data" type="application\/json">([\s\S]*?)<\/script>/);
  if (pageMatch) {
    try {
      const d = JSON.parse(pageMatch[1]);
      if (d.practice && d.practice.levels) {
        for (const l of Object.values(d.practice.levels)) {
          if (Array.isArray(l) && l.length > 0) { hasQuestions = true; break; }
        }
      }
    } catch {}
  }

  // Check embedded-study-guide-data
  if (!hasQuestions) {
    const guideMatch = content.match(/<script type="application\/json" id="embedded-study-guide-data">([\s\S]*?)<\/script>/);
    if (guideMatch) {
      try {
        const d = JSON.parse(guideMatch[1]);
        if (Array.isArray(d.practiceQuestions) && d.practiceQuestions.length > 0) {
          hasQuestions = true;
        }
      } catch {}
    }
  }

  // Check tabs/practice.json
  if (!hasQuestions) {
    const tabsPj = path.join(path.dirname(item.file), 'tabs', 'practice.json');
    if (fs.existsSync(tabsPj)) {
      try {
        const d = JSON.parse(fs.readFileSync(tabsPj, 'utf8'));
        if (d.levels) {
          for (const l of Object.values(d.levels)) {
            if (Array.isArray(l) && l.length > 0) { hasQuestions = true; break; }
          }
        }
      } catch {}
    }
  }

  if (!hasQuestions) {
    candidates.push(item);
  }
}

console.log(`Found ${candidates.length} candidate microtopics missing practice questions.`);

// Group and apply limits
let selectedTopics = [];
if (perSubjectLimit > 0) {
  const bySubj = {};
  for (const c of candidates) {
    if (!bySubj[c.subject]) bySubj[c.subject] = [];
    if (bySubj[c.subject].length < perSubjectLimit) bySubj[c.subject].push(c);
  }
  selectedTopics = Object.values(bySubj).flat();
} else if (requestedLimit > 0) {
  // Balanced selection across subjects
  const bySubj = {};
  for (const c of candidates) {
    if (!bySubj[c.subject]) bySubj[c.subject] = [];
    bySubj[c.subject].push(c);
  }
  const keys = Object.keys(bySubj);
  let idx = 0;
  while (selectedTopics.length < requestedLimit && selectedTopics.length < candidates.length) {
    const subj = keys[idx % keys.length];
    if (bySubj[subj] && bySubj[subj].length > 0) {
      selectedTopics.push(bySubj[subj].shift());
    }
    idx++;
  }
} else {
  selectedTopics = candidates;
}

console.log(`Selected ${selectedTopics.length} microtopics to process.\n`);

// Extract topic metadata from index.html / content.json
function extractTopicInfo(filePath) {
  const content = fs.readFileSync(filePath, 'utf8');
  const dir = path.dirname(filePath);

  let topicName = path.basename(dir).replace(/-/g, ' ');
  let subjectName = path.relative(path.join(ROOT, 'upsc'), dir).split(path.sep)[0];
  let overviewText = '';

  // Try upsc-page-data
  const pageMatch = content.match(/<script id="upsc-page-data" type="application\/json">([\s\S]*?)<\/script>/);
  if (pageMatch) {
    try {
      const d = JSON.parse(pageMatch[1]);
      if (d.topicName) topicName = d.topicName;
      if (d.subject) subjectName = d.subject;
      if (d.overview && d.overview.definition) {
        overviewText += `Definition: ${typeof d.overview.definition === 'string' ? d.overview.definition : d.overview.definition.en || ''}\n`;
      }
      if (d.concepts && Array.isArray(d.concepts.sections)) {
        for (const s of d.concepts.sections.slice(0, 4)) {
          const title = typeof s.title === 'string' ? s.title : s.title?.en || '';
          overviewText += `- ${title}\n`;
        }
      }
    } catch {}
  }

  // Try embedded-study-guide-data
  const guideMatch = content.match(/<script type="application\/json" id="embedded-study-guide-data">([\s\S]*?)<\/script>/);
  if (guideMatch) {
    try {
      const d = JSON.parse(guideMatch[1]);
      if (d.hero?.title) topicName = d.hero.title;
      if (d.hero?.description) overviewText += `${d.hero.description}\n`;
      if (d.deepDive?.sections) {
        for (const s of d.deepDive.sections.slice(0, 3)) {
          overviewText += `- ${s.title}\n`;
        }
      }
    } catch {}
  }

  // Fallback to content.json
  const cjPath = path.join(dir, 'content.json');
  if (fs.existsSync(cjPath) && !overviewText) {
    try {
      const cj = JSON.parse(fs.readFileSync(cjPath, 'utf8'));
      if (cj.hero?.title) topicName = cj.hero.title;
      if (cj.hero?.description) overviewText += cj.hero.description;
    } catch {}
  }

  return { topicName, subjectName, overviewText, template: pageMatch ? 'upsc-renderer' : 'competitive-exam-guide' };
}

// Build generation prompt for exactly 30 UPSC questions
function buildPrompt(topicName, subjectName, overviewText) {
  return `You are a premier UPSC Civil Services Examination question setter and subject expert.
Create exactly 30 unique, rigorous, high-yield practice questions for the following UPSC microtopic:

Topic: "${topicName}"
Subject: ${subjectName}
Context & Key Themes:
${overviewText || 'Comprehensive UPSC General Studies Prelims and Mains coverage.'}

Question Design Guidelines:
1. Divide the 30 questions into three difficulty / style levels (10 questions each):
   - "basic" (Questions 1 to 10): Core factual recall, definitions, key technical terms, dates, acts, and institutional bodies.
   - "conceptual" (Questions 11 to 20): Cause-and-effect, systemic comparisons, evolutionary trends, and policy/governance mechanisms.
   - "statementBased" (Questions 21 to 30): Authentic UPSC multi-statement questions ("Consider the following statements... Which of the statements given above is/are correct?").
2. Cover EVERY important fact, term, article/section, personality, institution, and common exam trap related to "${topicName}".
3. Provide bilingual text for all questions, options, and explanations (en: English, hi: authentic Hindi).
4. For every question, include a comprehensive, insightful explanation clarifying why the correct option is right and why distractors are wrong.
5. GOOGLE PREFERRED SOURCES & CITATIONS (High E-E-A-T Standard):
   - Anchor all facts, provisions, metrics, and trends strictly in primary authoritative sources:
     * For Polity: The Constitution of India (Articles, Amendments), Supreme Court landmarks, India Code statutes.
     * For History & Culture: NCERT (Themes in Indian History, An Introduction to Indian Art), Archaeological Survey of India, standard historical canons (Bipan Chandra, Spectrum).
     * For Economy: Economic Survey of India, Union Budget, Reserve Bank of India reports, NITI Aayog.
   - Conclude EVERY explanation with an explicit primary reference in brackets, for example:
     "[Primary Reference: Article 312, Constitution of India / Official UPSC GS-2 Syllabus Reference]" or
     "[Primary Reference: NCERT Class 11 Themes in Indian History / Archaeological Survey of India]".

CRITICAL: Return ONLY a valid JSON object with NO markdown formatting, NO backticks (\`\`\`json).
Structure:
{
  "levels": {
    "basic": [
      {
        "id": 1,
        "question": { "en": "...", "hi": "..." },
        "options": [
          { "letter": "A", "text": { "en": "...", "hi": "..." }, "correct": false },
          { "letter": "B", "text": { "en": "...", "hi": "..." }, "correct": true },
          { "letter": "C", "text": { "en": "...", "hi": "..." }, "correct": false },
          { "letter": "D", "text": { "en": "...", "hi": "..." }, "correct": false }
        ],
        "explanation": { "en": "...", "hi": "..." }
      }
    ],
    "conceptual": [
      {
        "id": 11,
        "question": { "en": "...", "hi": "..." },
        "options": [ ... ],
        "explanation": { "en": "...", "hi": "..." }
      }
    ],
    "statementBased": [
      {
        "id": 21,
        "question": { "en": "Consider the following statements regarding ...:\\n1. ...\\n2. ...\\nWhich of the statements given above is/are correct?", "hi": "..." },
        "options": [
          { "letter": "A", "text": { "en": "1 only", "hi": "केवल 1" }, "correct": false },
          { "letter": "B", "text": { "en": "2 only", "hi": "केवल 2" }, "correct": false },
          { "letter": "C", "text": { "en": "Both 1 and 2", "hi": "1 और 2 दोनों" }, "correct": true },
          { "letter": "D", "text": { "en": "Neither 1 nor 2", "hi": "न तो 1, न ही 2" }, "correct": false }
        ],
        "explanation": { "en": "...", "hi": "..." }
      }
    ]
  }
}`;
}

// Call Gemini API with 1 call per page and key rotation
async function callGemini(prompt) {
  let modelToUse = MODEL;
  let attempts = 0;
  const maxAttempts = 5;

  while (attempts < maxAttempts) {
    attempts++;
    const { client, keyId } = getNextAIClient();
    try {
      const response = await client.models.generateContent({
        model: modelToUse,
        contents: prompt,
        config: {
          temperature: 0.2,
          responseMimeType: 'application/json'
        }
      });
      const raw = response.text ? response.text.trim() : '';
      if (!raw) throw new Error('Empty response from model');
      const repaired = jsonrepair(raw);
      const parsed = JSON.parse(repaired);
      return { data: parsed, keyId, model: modelToUse };
    } catch (err) {
      console.warn(`    ⚠️  [Attempt ${attempts}/${maxAttempts}] Error on ${keyId} with ${modelToUse}: ${err.message.slice(0, 100)}`);
      if (modelToUse === MODEL) {
        modelToUse = FALLBACK_MODEL;
      }
      if (attempts >= maxAttempts) throw err;
      const backoff = Math.min(10000, 2000 * Math.pow(2, attempts - 1));
      console.log(`    ⏳ Waiting ${backoff / 1000}s before retry...`);
      await new Promise(r => setTimeout(r, backoff));
    }
  }
}

// Helpers to safely extract bilingual text and normalize questions
function extractText(val, lang = 'en') {
  if (val == null) return '';
  if (typeof val === 'string') return val.trim();
  if (typeof val === 'object') {
    if (lang === 'hi') {
      return (val.hi || val.hindi || val.en || val.english || val.text || '').trim();
    }
    return (val.en || val.english || val.hi || val.hindi || val.text || '').trim();
  }
  return String(val).trim();
}

function extractOptionText(o, lang = 'en') {
  if (o == null) return '';
  if (typeof o === 'string') return o.trim();
  if (typeof o === 'object') {
    if (o.text != null) return extractText(o.text, lang);
    if (lang === 'hi') return (o.hi || o.hindi || o.en || o.english || o.option || '').trim();
    return (o.en || o.english || o.hi || o.hindi || o.option || '').trim();
  }
  return String(o).trim();
}

function normalizeOption(o, fallbackLetter = 'A') {
  if (typeof o === 'string') {
    return {
      letter: fallbackLetter,
      text: { en: o.trim(), hi: o.trim() },
      correct: false
    };
  }
  const letter = o.letter || fallbackLetter;
  const enText = extractOptionText(o, 'en');
  const hiText = extractOptionText(o, 'hi') || enText;
  const correct = Boolean(o.correct === true || o.isCorrect === true || o.right === true);
  return {
    letter,
    text: { en: enText, hi: hiText },
    correct
  };
}

function normalizeQuestion(q, id = 1) {
  const enQ = extractText(q.question || q.q || q.title, 'en');
  const hiQ = extractText(q.question || q.q || q.title, 'hi') || enQ;

  const rawOptions = Array.isArray(q.options) ? q.options : (Array.isArray(q.opts) ? q.opts : []);
  const letters = ['A', 'B', 'C', 'D'];
  const options = rawOptions.map((opt, idx) => normalizeOption(opt, letters[idx] || String(idx + 1)));

  // Ensure one option is marked correct
  const hasCorrect = options.some(o => o.correct);
  if (!hasCorrect && options.length > 0) {
    if (typeof q.ans === 'number' && options[q.ans]) {
      options[q.ans].correct = true;
    } else if (typeof q.answer === 'string' && ['A', 'B', 'C', 'D'].includes(q.answer.toUpperCase())) {
      const idx = ['A', 'B', 'C', 'D'].indexOf(q.answer.toUpperCase());
      if (options[idx]) options[idx].correct = true;
    } else {
      options[0].correct = true;
    }
  }

  const enSol = extractText(q.explanation || q.sol || q.solution, 'en');
  const hiSol = extractText(q.explanation || q.sol || q.solution, 'hi') || enSol;

  const correctOpt = options.find(o => o.correct) || options[0];
  const correctAnswer = correctOpt ? correctOpt.letter : 'A';

  return {
    id: q.id || id,
    question: { en: enQ, hi: hiQ },
    options,
    correctAnswer,
    explanation: { en: enSol, hi: hiSol }
  };
}

function unwrapQuestionsData(raw) {
  if (!raw) return null;
  if (Array.isArray(raw)) return raw;
  if (typeof raw !== 'object') return null;

  if (raw.levels || raw.basic || raw.conceptual || raw.statementBased) return raw;

  const keys = Object.keys(raw);
  for (const k of keys) {
    const val = raw[k];
    if (val && typeof val === 'object') {
      if (val.levels || val.basic || val.conceptual || val.statementBased || val.practiceQuestions || val.questions || Array.isArray(val)) {
        return val;
      }
    }
  }
  return raw;
}

function normalizeAllLevels(questionsData) {
  const unwrapped = unwrapQuestionsData(questionsData) || {};

  let rawBasic = [];
  let rawConceptual = [];
  let rawStatement = [];

  if (Array.isArray(unwrapped)) {
    rawBasic = unwrapped.slice(0, 10);
    rawConceptual = unwrapped.slice(10, 20);
    rawStatement = unwrapped.slice(20, 30);
  } else {
    const levels = unwrapped.levels || unwrapped.Levels || unwrapped;
    rawBasic = levels.basic || levels.Basic || levels.easy || levels.Easy || [];
    rawConceptual = levels.conceptual || levels.Conceptual || levels.medium || levels.Medium || [];
    rawStatement = levels.statementBased || levels.statement_based || levels['statement-based'] || levels.StatementBased || levels.hard || levels.Hard || [];

    const allList = unwrapped.questions || unwrapped.practiceQuestions || unwrapped.mcqs || unwrapped.items || unwrapped.practice || [];
    if (rawBasic.length === 0 && rawConceptual.length === 0 && rawStatement.length === 0 && Array.isArray(allList) && allList.length > 0) {
      rawBasic = allList.slice(0, 10);
      rawConceptual = allList.slice(10, 20);
      rawStatement = allList.slice(20, 30);
    }
  }

  const total = rawBasic.length + rawConceptual.length + rawStatement.length;
  if (total === 0) {
    throw new Error('Parsed model data did not contain any valid questions');
  }

  let nextId = 1;
  return {
    basic: rawBasic.map(q => normalizeQuestion(q, nextId++)),
    conceptual: rawConceptual.map(q => normalizeQuestion(q, nextId++)),
    statementBased: rawStatement.map(q => normalizeQuestion(q, nextId++))
  };
}

// Save practice questions to topic
function saveQuestions(filePath, questionsData, template) {
  const dir = path.dirname(filePath);
  let content = fs.readFileSync(filePath, 'utf8');

  // 1. Normalize levels structure
  const levels = questionsData.basic ? questionsData : normalizeAllLevels(questionsData);

  // 2. Save tabs/practice.json (used by upsc-renderer)
  const tabsDir = path.join(dir, 'tabs');
  if (!fs.existsSync(tabsDir)) fs.mkdirSync(tabsDir, { recursive: true });
  fs.writeFileSync(path.join(tabsDir, 'practice.json'), JSON.stringify({ levels }, null, 2), 'utf8');

  // 3. Flatten list for competitive-exam-guide format
  const flatQuestions = [];
  const letters = ['A', 'B', 'C', 'D'];
  let qNum = 1;
  for (const lvl of ['basic', 'conceptual', 'statementBased']) {
    for (const q of (levels[lvl] || [])) {
      const correctIdx = q.options.findIndex(o => o.correct === true);
      const chosenIdx = correctIdx >= 0 ? correctIdx : 0;
      flatQuestions.push({
        id: `p_q_${qNum++}`,
        type: 'MCQ',
        level: lvl,
        q: q.question.en,
        opts: q.options.map(o => o.text.en),
        ans: chosenIdx,
        correctAnswer: letters[chosenIdx] || 'A',
        sol: q.explanation.en
      });
    }
  }

  // 4. Update index.html
  if (template === 'upsc-renderer') {
    content = content.replace(/<script id="upsc-page-data" type="application\/json">([\s\S]*?)<\/script>/, (match, jsonStr) => {
      try {
        const pageData = JSON.parse(jsonStr);
        pageData.practice = { levels };
        if (Array.isArray(pageData.tabs) && !pageData.tabs.includes('practice')) {
          pageData.tabs.push('practice');
        }
        return `<script id="upsc-page-data" type="application/json">${JSON.stringify(pageData)}</script>`;
      } catch {
        return match;
      }
    });
  } else {
    // competitive-exam-guide
    content = content.replace(/<script type="application\/json" id="embedded-study-guide-data">([\s\S]*?)<\/script>/, (match, jsonStr) => {
      try {
        const guideData = JSON.parse(jsonStr);
        guideData.practiceQuestions = flatQuestions;
        return `<script type="application/json" id="embedded-study-guide-data">${JSON.stringify(guideData, null, 2)}</script>`;
      } catch {
        return match;
      }
    });

    // Also update Hindi if present
    content = content.replace(/<script type="application\/json" id="embedded-study-guide-data-hi">([\s\S]*?)<\/script>/, (match, jsonStr) => {
      try {
        const guideDataHi = JSON.parse(jsonStr);
        let qNumHi = 1;
        const flatHi = [];
        for (const lvl of ['basic', 'conceptual', 'statementBased']) {
          for (const q of (levels[lvl] || [])) {
            const correctIdx = q.options.findIndex(o => o.correct === true);
            const chosenIdx = correctIdx >= 0 ? correctIdx : 0;
            flatHi.push({
              id: `p_q_${qNumHi++}`,
              type: 'MCQ',
              level: lvl,
              q: q.question.hi || q.question.en,
              opts: q.options.map(o => o.text.hi || o.text.en),
              ans: chosenIdx,
              correctAnswer: letters[chosenIdx] || 'A',
              sol: q.explanation.hi || q.explanation.en
            });
          }
        }
        guideDataHi.practiceQuestions = flatHi;
        return `<script type="application/json" id="embedded-study-guide-data-hi">${JSON.stringify(guideDataHi, null, 2)}</script>`;
      } catch {
        return match;
      }
    });

  }

  fs.writeFileSync(filePath, content, 'utf8');
}

// Topic processing worker
async function processTopic(item, index, total) {
  const info = extractTopicInfo(item.file);
  const relPath = path.relative(ROOT, item.file).replace(/\\/g, '/');

  console.log(`[${index + 1}/${total}] Processing: "${info.topicName}" (${item.subject})`);
  console.log(`   Path: ${relPath} [Template: ${info.template}]`);

  if (dryRun) {
    console.log(`   [DRY-RUN] Would generate 30 questions using ${MODEL} via next rotating API key.`);
    return true;
  }

  const prompt = buildPrompt(info.topicName, info.subjectName, info.overviewText);

  try {
    const start = Date.now();
    const result = await callGemini(prompt);
    const duration = ((Date.now() - start) / 1000).toFixed(1);

    const normalized = normalizeAllLevels(result.data);
    const totalQ = (normalized.basic?.length || 0) + (normalized.conceptual?.length || 0) + (normalized.statementBased?.length || 0);

    console.log(`   ✓ [${info.topicName}] Received ${totalQ} questions in ${duration}s via ${result.keyId} (${result.model})`);

    saveQuestions(item.file, normalized, info.template);
    console.log(`   ✓ [${info.topicName}] Saved 30 questions to index.html and tabs/practice.json\n`);
    return true;
  } catch (err) {
    console.error(`   ❌ [${info.topicName}] Failed to generate questions: ${err.message}\n`);
    return false;
  }
}

// Main execution loop
let successCount = 0;
let failCount = 0;
const concurrency = Math.max(1, Math.min(3, requestedConcurrency || 1));

if (concurrency === 1 || dryRun) {
  for (let i = 0; i < selectedTopics.length; i++) {
    const ok = await processTopic(selectedTopics[i], i, selectedTopics.length);
    if (ok) successCount++; else failCount++;
    if (!dryRun) await new Promise(r => setTimeout(r, 1200));
  }
} else {
  console.log(`🚀 Running with concurrency = ${concurrency} parallel workers across ${API_KEYS.length} rotating keys\n`);
  let currentIndex = 0;
  async function worker() {
    while (currentIndex < selectedTopics.length) {
      const idx = currentIndex++;
      const item = selectedTopics[idx];
      const ok = await processTopic(item, idx, selectedTopics.length);
      if (ok) successCount++; else failCount++;
      await new Promise(r => setTimeout(r, 1500));
    }
  }
  const workers = Array.from({ length: concurrency }, () => worker());
  await Promise.all(workers);
}

console.log('====================================================');
console.log(`Generation complete! Success: ${successCount}, Failed: ${failCount}`);
console.log('====================================================');
