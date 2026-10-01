#!/usr/bin/env node
/**
 * ============================================================================
 * SJ Maths — Chemistry Hindi Translation & Bilingual Pipeline
 * Powered by Google Gemini 3.1 Flash Lite via @google/genai SDK
 * Translates and compiles full dual-language (EN / HI) UP PGT/TGT Chemistry Pages
 * Block-based container compiler ensuring 100% tag balance and zero layout leaks
 * ============================================================================
 */

import fs from 'fs';
import path from 'path';
import 'dotenv/config';
import { GoogleGenAI } from '@google/genai';
import { jsonrepair } from 'jsonrepair';
import { cleanMathHtml, buildCompleteBilingualHtml } from './lib/chemistry-bilingual.mjs';

// Multi-key rotation
const rawKeys = [
  process.env.GEMINI_API_KEY_2,
  process.env.GEMINI_API_KEY_1,
  process.env.GEMINI_API_KEY
].filter(Boolean);

const apiKeys = [...new Set(rawKeys)];
if (apiKeys.length === 0) {
  console.error('CRITICAL ERROR: No GEMINI_API_KEY found in environment.');
  process.exit(1);
}

console.log(`Loaded ${apiKeys.length} API keys for round-robin rotation.`);
const clients = apiKeys.map((key, i) => ({
  id: i + 1,
  preview: key.substring(0, 10) + '...' + key.slice(-6),
  client: new GoogleGenAI({ apiKey: key })
}));
let clientIdx = 0;

function getNextClient() {
  const c = clients[clientIdx];
  clientIdx = (clientIdx + 1) % clients.length;
  return c;
}

// CLI Flags
const args = process.argv.slice(2);
function getArg(flag) {
  const idx = args.indexOf(flag);
  return idx !== -1 && args[idx + 1] ? args[idx + 1] : null;
}
const hasFlag = (f) => args.includes(f);

const TARGET_TOPIC = getArg('--topic');
const LIMIT = getArg('--limit') ? parseInt(getArg('--limit'), 10) : null;
const FORCE = hasFlag('--force');

const MODEL_NAME = 'gemini-3.1-flash-lite';
const STATUS_FILE = 'content-generation-status-chemistry-hi.json';

function fixMissingQuotes(str) {
  return str
    .replace(/^(\s*"[a-zA-Z0-9_]+_hi":\s*)([^"\s][^\n\r]*?)",?$/gm, '$1"$2",')
    .replace(/^(\s*"[a-zA-Z0-9_]+":\s*)([^"\s\[\{0-9\-tfn][^\n\r]*?)",?$/gm, '$1"$2",');
}

// Helper: safe JSON parse with targeted quote repair and jsonrepair fallback
function safeParseJson(raw) {
  let cleaned = raw.trim();
  if (cleaned.startsWith('```json')) cleaned = cleaned.replace(/^```json\s*/, '').replace(/\s*```$/, '');
  else if (cleaned.startsWith('```')) cleaned = cleaned.replace(/^```\s*/, '').replace(/\s*```$/, '');

  // 1. Try standard JSON.parse first
  try {
    return JSON.parse(cleaned);
  } catch (e1) {
    // 2. Targeted line-anchored quote repair on unquoted strings
    const repaired = fixMissingQuotes(cleaned);
    try {
      return JSON.parse(repaired);
    } catch (e2) {
      // 3. Fallback to jsonrepair
      try {
        return JSON.parse(jsonrepair(repaired));
      } catch (e3) {
        return JSON.parse(jsonrepair(cleaned));
      }
    }
  }
}

// Helper: Call Gemini with retries and key rotation
async function callGemini(prompt, systemInstruction, maxRetries = 5) {
  let attempts = 0;
  while (attempts < maxRetries) {
    attempts++;
    const { client, id } = getNextClient();
    try {
      const response = await client.models.generateContent({
        model: MODEL_NAME,
        contents: prompt,
        config: {
          systemInstruction: systemInstruction,
          responseMimeType: 'application/json',
          temperature: 0.2
        }
      });
      return safeParseJson(response.text);
    } catch (err) {
      console.warn(`[Key #${id}] Attempt ${attempts}/${maxRetries} failed: ${err.message}`);
      if (attempts >= maxRetries) throw err;
      const delayMs = Math.min(30000, 2500 * Math.pow(1.5, attempts)) + Math.random() * 1000;
      await new Promise(r => setTimeout(r, delayMs));
    }
  }
}

// SYSTEM INSTRUCTIONS
const SYSTEM_INSTRUCTION_NOTES = `You are a Senior Professor of Chemistry and an expert translator for the UP PGT Chemistry (Subject Code 02) and UP TGT Science competitive exams in India.
Your mission is to translate English Chemistry study notes and summary components into high-standard, academic Hindi (NCERT / UP Madhyamik Education Board standard).

CRITICAL TRANSLATION RULES:
1. Standard Academic Technical Terminology:
   - Translate technical chemistry concepts into standard Devanagari terminology, accompanied by the English term in parentheses on first or principal mention.
   - Examples: "Molarity" -> "मोलरता (Molarity)", "Electronegativity" -> "विद्युत ऋणात्मकता (Electronegativity)", "Homogeneous Mixture" -> "समांगी मिश्रण (Homogeneous Mixture)".
2. Untouched Scientific Elements:
   - KEEP ALL chemical symbols (H2O, NaCl, XeF4, Fe2+), units (mol/L, kJ/mol, g/cm3), mathematical fractions, formulas, and reaction arrows strictly intact in standard scientific Latin/symbolic script.
3. Natural, Formal Tone suitable for postgraduate teacher recruitment candidates.
4. Output must be strict JSON matching the requested schema.`;

const SYSTEM_INSTRUCTION_QUESTIONS = `You are an expert bilingual examiner for UP PGT Chemistry and UP TGT Science exams.
Translate competitive exam questions, options, hints, and explanations into clear, accurate Hindi.
Keep chemical formulas, equations, and math notation intact in standard Latin script.
Output must be strict JSON matching the requested schema.`;

// Extract helper: strip existing bilingual spans to obtain pure English baseline
function getPureEn(str) {
  if (!str) return '';
  const enMatch = str.match(/<span class="lang-en">([\s\S]*?)<\/span>/);
  if (enMatch) return enMatch[1].trim();
  const enDivMatch = str.match(/<div class="lang-en">([\s\S]*?)<\/div>/);
  if (enDivMatch) return enDivMatch[1].replace(/<[^>]+>/g, '').trim();
  return str.replace(/<[^>]+>/g, '').trim();
}

// Extract comprehensive content from index.html
function extractComprehensiveContent(html) {
  const kickerMatch = html.match(/<div class="kicker"[^>]*>([\s\S]*?)<\/div>/);
  const titleMatch = html.match(/<h1>([\s\S]*?)<\/h1>/);
  const leadMatch = html.match(/<p class="lead">([\s\S]*?)<\/p>/);

  const kicker = getPureEn(kickerMatch ? kickerMatch[1] : '');
  const title = getPureEn(titleMatch ? titleMatch[1] : '');
  const lead = getPureEn(leadMatch ? leadMatch[1] : '');

  // Sections
  const sections = [];
  const secRegex = /<section class="notes-section"[^>]*>[\s\S]*?<h2>([\s\S]*?)<\/h2>[\s\S]*?<div class="prose-content">([\s\S]*?)<\/div>\s*<\/section>/g;
  let sMatch;
  while ((sMatch = secRegex.exec(html)) !== null) {
    const heading = getPureEn(sMatch[1]);
    const content = sMatch[2];
    const enBlockMatch = content.match(/<div class="lang-en">([\s\S]*?)<\/div>/);
    const bulletsSource = enBlockMatch ? enBlockMatch[1] : content;
    const bullets = [...bulletsSource.matchAll(/<li>([\s\S]*?)<\/li>/g)].map(m => getPureEn(m[1]));
    sections.push({ heading, bullets });
  }

  // Formulas
  const formulas = [];
  const formRegex = /<div class="formula-card">[\s\S]*?<div class="formula-name">([\s\S]*?)<\/div>[\s\S]*?<div class="formula-eq">([\s\S]*?)<\/div>[\s\S]*?<div class="formula-meta">([\s\S]*?)<\/div>\s*<\/div>/g;
  let fMatch;
  while ((fMatch = formRegex.exec(html)) !== null) {
    const name = getPureEn(fMatch[1]);
    const eq = cleanMathHtml(fMatch[2].trim());
    const metaBlock = fMatch[3];
    const condMatch = metaBlock.match(/Conditions:<\/strong>\s*([\s\S]*?)<\/div>/);
    const unitMatch = metaBlock.match(/Units:<\/strong>\s*([\s\S]*?)<\/div>/);
    formulas.push({
      name,
      eq,
      conditions: condMatch ? cleanMathHtml(getPureEn(condMatch[1])) : '',
      units: unitMatch ? cleanMathHtml(getPureEn(unitMatch[1])) : ''
    });
  }

  // Exceptions
  const exceptions = [];
  const excRegex = /<div class="exception-card">[\s\S]*?<span class="exception-rule">([\s\S]*?)<\/span>[\s\S]*?<p class="exception-detail">([\s\S]*?)<\/p>/g;
  let eMatch;
  while ((eMatch = excRegex.exec(html)) !== null) {
    exceptions.push({
      rule: getPureEn(eMatch[1]),
      observation: getPureEn(eMatch[2].replace(/^<strong>Observation:<\/strong>\s*/, ''))
    });
  }

  // Tricks
  const tricks = [];
  const trkRegex = /<div class="trick-card">[\s\S]*?<div class="trick-title">([\s\S]*?)<\/div>[\s\S]*?<div class="trick-shortcut">([\s\S]*?)<\/div>[\s\S]*?<p class="trick-app">([\s\S]*?)<\/p>/g;
  let tMatch;
  while ((tMatch = trkRegex.exec(html)) !== null) {
    tricks.push({
      title: getPureEn(tMatch[1]),
      shortcut: tMatch[2].trim(),
      application: getPureEn(tMatch[3].replace(/^<strong>Application:<\/strong>\s*/, ''))
    });
  }

  // Comparison Matrix
  let comparison = null;
  const compMatch = html.match(/<div class="comparison-card">[\s\S]*?<div class="comparison-title">([\s\S]*?)<\/div>[\s\S]*?<table class="styled-table">([\s\S]*?)<\/table>/);
  if (compMatch) {
    const cTitle = getPureEn(compMatch[1]);
    const theadMatch = compMatch[2].match(/<thead>[\s\S]*?<tr>([\s\S]*?)<\/tr>[\s\S]*?<\/thead>/);
    const headers = theadMatch ? [...theadMatch[1].matchAll(/<th>([\s\S]*?)<\/th>/g)].map(m => getPureEn(m[1])) : [];
    const tbodyMatch = compMatch[2].match(/<tbody>([\s\S]*?)<\/tbody>/);
    const rows = tbodyMatch ? [...tbodyMatch[1].matchAll(/<tr>([\s\S]*?)<\/tr>/g)].map(tr => {
      return [...tr[1].matchAll(/<td>([\s\S]*?)<\/td>/g)].map(td => getPureEn(td[1]));
    }) : [];
    comparison = { title: cTitle, headers, rows };
  }

  // Exam Points
  let exam_points = [];
  const epMatch = html.match(/<div class="exam-points-card">[\s\S]*?<ul class="exam-points-list">([\s\S]*?)<\/ul>/);
  if (epMatch) {
    exam_points = [...epMatch[1].matchAll(/<li>([\s\S]*?)<\/li>/g)].map(m => getPureEn(m[1]));
  }

  // Common Errors
  let common_errors = [];
  const ceMatch = html.match(/<div class="common-errors-card">[\s\S]*?<ul class="common-errors-list">([\s\S]*?)<\/ul>/);
  if (ceMatch) {
    common_errors = [...ceMatch[1].matchAll(/<li>([\s\S]*?)<\/li>/g)].map(m => getPureEn(m[1]));
  }

  // Tab 2: Summary Concepts
  const summary_concepts = [];
  const conceptRegex = /<div class="summary-concept-card">[\s\S]*?<h3 class="summary-concept-title">([\s\S]*?)<\/h3>[\s\S]*?<div class="summary-concept-body prose-content">([\s\S]*?)<\/div>\s*<\/div>/g;
  let cMatch;
  while ((cMatch = conceptRegex.exec(html)) !== null) {
    summary_concepts.push({
      title: getPureEn(cMatch[1]),
      body: getPureEn(cMatch[2])
    });
  }

  // Tab 2: Glossary
  const glossary = [];
  const gloRegex = /<div class="glossary-item">[\s\S]*?<span class="glossary-term">([\s\S]*?)<\/span>[\s\S]*?<div class="glossary-def">([\s\S]*?)<\/div>/g;
  let gMatch;
  while ((gMatch = gloRegex.exec(html)) !== null) {
    glossary.push({
      term: getPureEn(gMatch[1]),
      definition: getPureEn(gMatch[2])
    });
  }

  // Tab 2: Key Takeaways
  let key_takeaways = [];
  const mustMatch = html.match(/<h2>(?:🎯\s*)?(?:<[^>]+>)?Key Takeaways[\s\S]*?<\/h2>[\s\S]*?<ul[^>]*>([\s\S]*?)<\/ul>/);
  if (mustMatch) {
    key_takeaways = [...mustMatch[1].matchAll(/<li>([\s\S]*?)<\/li>/g)].map(x => getPureEn(x[1]));
  }

  // Tab 2: Quick Recall
  let quick_recall = [];
  const recallMatch = html.match(/<h2>(?:📌\s*)?(?:<[^>]+>)?Quick Recall[\s\S]*?<\/h2>[\s\S]*?<ul[^>]*>([\s\S]*?)<\/ul>/);
  if (recallMatch) {
    quick_recall = [...recallMatch[1].matchAll(/<li>([\s\S]*?)<\/li>/g)].map(x => getPureEn(x[1]));
  }

  // Tab 2: Key Differences
  const key_differences = [];
  const confRegex = /<div class="confusion-item">[\s\S]*?<span class="conf-badge-a">([\s\S]*?)<\/span>[\s\S]*?<span class="conf-badge-b">([\s\S]*?)<\/span>[\s\S]*?<p class="confusion-diff">([\s\S]*?)<\/p>/g;
  let cfMatch;
  while ((cfMatch = confRegex.exec(html)) !== null) {
    key_differences.push({
      term_a: getPureEn(cfMatch[1]),
      term_b: getPureEn(cfMatch[2]),
      difference: getPureEn(cfMatch[3])
    });
  }

  return {
    kicker,
    title,
    lead,
    sections,
    formulas,
    exceptions,
    tricks,
    comparison,
    exam_points,
    common_errors,
    summary_concepts,
    glossary,
    key_takeaways,
    quick_recall,
    key_differences
  };
}

// Translate Study Notes & Theory
async function translateTheory(enData) {
  const prompt = `Translate the following English study notes and revision summary components into academic Hindi according to the rules:

INPUT DATA:
${JSON.stringify(enData, null, 2)}

REQUIRED JSON RESPONSE SCHEMA:
{
  "kicker_hi": "Branch in Hindi (e.g. भौतिक रसायन)",
  "title_hi": "Topic Title in Hindi with English in brackets (e.g. रासायनिक तत्व (Chemical Elements))",
  "lead_hi": "Translated introductory lead paragraph in Hindi",
  "sections_hi": [
    {
      "heading_hi": "Section heading in Hindi",
      "bullets_hi": ["Bullet 1 in Hindi", "Bullet 2 in Hindi"]
    }
  ],
  "formula_meta_hi": [
    {
      "name_hi": "Formula name in Hindi (English in brackets)",
      "conditions_hi": "Translated conditions",
      "units_hi": "Translated units explanation"
    }
  ],
  "exceptions_hi": [
    {
      "rule_hi": "General rule in Hindi",
      "observation_hi": "Observation & explanation in Hindi"
    }
  ],
  "tricks_hi": [
    {
      "title_hi": "Shortcut title in Hindi",
      "shortcut_hi": "Shortcut rule in Hindi",
      "application_hi": "Application tip in Hindi"
    }
  ],
  "comparison_hi": {
    "title_hi": "Comparison table title in Hindi",
    "headers_hi": ["Header 1 in Hindi", "Header 2 in Hindi"],
    "rows_hi": [
      ["Cell 1 in Hindi", "Cell 2 in Hindi"]
    ]
  },
  "exam_points_hi": ["Key point 1 in Hindi", "Key point 2 in Hindi"],
  "common_errors_hi": ["Common error 1 in Hindi", "Common error 2 in Hindi"],
  "summary_concepts_hi": [
    {
      "title_hi": "Core concept title in Hindi",
      "body_hi": "Concise concept explanation in Hindi"
    }
  ],
  "glossary_hi": [
    {
      "term_hi": "Term in Hindi (English in brackets)",
      "definition_hi": "Concise definition in Hindi"
    }
  ],
  "key_takeaways_hi": ["Point 1 in Hindi", "Point 2 in Hindi"],
  "quick_recall_hi": ["Recall point 1 in Hindi", "Recall point 2 in Hindi"],
  "key_differences_hi": [
    {
      "term_a_hi": "Term A in Hindi",
      "term_b_hi": "Term B in Hindi",
      "difference_hi": "Clear distinction in Hindi"
    }
  ]
}`;

  return await callGemini(prompt, SYSTEM_INSTRUCTION_NOTES);
}

// Translate Questions Payload (quiz, topic_test, pyq)
async function translateQuestions(questions) {
  if (!Array.isArray(questions) || questions.length === 0) return [];
  const simplified = questions.map(q => ({
    question: q.question,
    options: q.options,
    hint: q.hint || '',
    explanation: q.explanation || ''
  }));

  const prompt = `Translate the following ${simplified.length} exam questions into Hindi:

INPUT QUESTIONS:
${JSON.stringify(simplified, null, 2)}

REQUIRED JSON RESPONSE SCHEMA:
{
  "translated": [
    {
      "question_hi": "Question in Hindi",
      "options_hi": ["Option A in Hindi", "Option B in Hindi", "Option C in Hindi", "Option D in Hindi"],
      "hint_hi": "Hint in Hindi (or empty string)",
      "explanation_hi": "Detailed rationale in Hindi"
    }
  ]
}`;

  const res = await callGemini(prompt, SYSTEM_INSTRUCTION_QUESTIONS);
  return res.translated || [];
}

// Process a Single Topic Directory
async function processTopic(topicDir) {
  console.log(`\n========================================`);
  console.log(`Processing Topic: ${topicDir}`);
  console.log(`========================================`);

  const htmlPath = path.join(topicDir, 'index.html');
  const quizPath = path.join(topicDir, 'quiz.json');
  const testPath = path.join(topicDir, 'topic-test.json');
  const pyqPath = path.join(topicDir, 'pyq.json');

  if (!fs.existsSync(htmlPath)) {
    console.warn(`Skipping: ${htmlPath} does not exist.`);
    return false;
  }

  const html = fs.readFileSync(htmlPath, 'utf8');

  // Skip if already completely bilingual unless FORCE is true
  if (html.includes('class="lang-hi"') && html.includes('id="btn-lang-toggle"') && !FORCE) {
    const hasQuizHi = html.indexOf('<span class="lang-hi">') !== -1 && html.indexOf('quiz-questions-list') !== -1;
    if (hasQuizHi) {
      console.log(`Already fully bilingual. Skipping.`);
      return true;
    }
  }

  // 1. Extract and Translate Theory & Revision Summary
  console.log(`[1/3] Translating Theory & Revision Summary via ${MODEL_NAME}...`);
  const enData = extractComprehensiveContent(html);
  const hiData = await translateTheory(enData);

  // 2. Translate Quiz Questions
  let quizData = [];
  if (fs.existsSync(quizPath)) {
    console.log(`[2/3] Translating Practice Quiz (${quizPath})...`);
    quizData = JSON.parse(fs.readFileSync(quizPath, 'utf8'));
    if (!quizData[0]?.question_hi || FORCE) {
      const hiQuiz = await translateQuestions(quizData);
      quizData.forEach((q, idx) => {
        if (hiQuiz[idx]) {
          q.question_hi = hiQuiz[idx].question_hi;
          q.options_hi = hiQuiz[idx].options_hi;
          q.hint_hi = hiQuiz[idx].hint_hi;
          q.explanation_hi = hiQuiz[idx].explanation_hi;
        }
      });
      fs.writeFileSync(quizPath, JSON.stringify(quizData, null, 2), 'utf8');
    }
  }

  // 3. Translate PYQs and Topic Test together in 1 API call
  let pyqData = [];
  let testData = [];
  const needsPyq = fs.existsSync(pyqPath);
  const needsTest = fs.existsSync(testPath);

  if (needsPyq) pyqData = JSON.parse(fs.readFileSync(pyqPath, 'utf8'));
  if (needsTest) testData = JSON.parse(fs.readFileSync(testPath, 'utf8'));

  const pyqToTranslate = (needsPyq && (!pyqData[0]?.question_hi || FORCE)) ? pyqData : [];
  const testToTranslate = (needsTest && (!testData[0]?.question_hi || FORCE)) ? testData : [];

  if (pyqToTranslate.length > 0 || testToTranslate.length > 0) {
    console.log(`[3/3] Translating PYQs & Topic Test combined (${pyqToTranslate.length + testToTranslate.length} questions in 1 API call)...`);
    const combinedQueue = [...pyqToTranslate, ...testToTranslate];
    const translatedCombined = await translateQuestions(combinedQueue);

    if (pyqToTranslate.length > 0) {
      const hiPyqs = translatedCombined.slice(0, pyqToTranslate.length);
      pyqData.forEach((q, idx) => {
        if (hiPyqs[idx]) {
          q.question_hi = hiPyqs[idx].question_hi;
          q.options_hi = hiPyqs[idx].options_hi;
          q.hint_hi = hiPyqs[idx].hint_hi || '';
          q.explanation_hi = hiPyqs[idx].explanation_hi;
        }
      });
      fs.writeFileSync(pyqPath, JSON.stringify(pyqData, null, 2), 'utf8');
    }

    if (testToTranslate.length > 0) {
      const hiTest = translatedCombined.slice(pyqToTranslate.length);
      testData.forEach((q, idx) => {
        if (hiTest[idx]) {
          q.question_hi = hiTest[idx].question_hi;
          q.options_hi = hiTest[idx].options_hi;
          q.hint_hi = hiTest[idx].hint_hi || '';
          q.explanation_hi = hiTest[idx].explanation_hi;
        }
      });
      fs.writeFileSync(testPath, JSON.stringify(testData, null, 2), 'utf8');
    }
  }

  // Compile Comprehensive Bilingual HTML
  const bilingualHtml = buildCompleteBilingualHtml(html, enData, hiData, quizData, pyqData, testData);
  fs.writeFileSync(htmlPath, bilingualHtml, 'utf8');

  console.log(`✓ Successfully updated ${topicDir} to Full Bilingual (EN/HI)!`);
  return true;
}

// Main Driver
async function main() {
  if (TARGET_TOPIC) {
    const ok = await processTopic(TARGET_TOPIC);
    if (ok) {
      let completed = {};
      if (fs.existsSync(STATUS_FILE)) {
        try { completed = JSON.parse(fs.readFileSync(STATUS_FILE, 'utf8')); } catch (e) {}
      }
      completed[TARGET_TOPIC] = { translatedAt: new Date().toISOString() };
      fs.writeFileSync(STATUS_FILE, JSON.stringify(completed, null, 2), 'utf8');
    }
    return;
  }

  // Scan all chemistry directories recursively
  function getTopicDirs(dir) {
    let results = [];
    const list = fs.readdirSync(dir, { withFileTypes: true });
    for (const d of list) {
      const p = path.join(dir, d.name);
      if (d.isDirectory()) {
        if (fs.existsSync(path.join(p, 'index.html')) && fs.existsSync(path.join(p, 'quiz.json'))) {
          results.push(p);
        }
        results = results.concat(getTopicDirs(p));
      }
    }
    return [...new Set(results)];
  }

  const allTopics = getTopicDirs('chemistry');
  console.log(`Found ${allTopics.length} Chemistry topic directories.`);

  // Load status checkpoint
  let completed = {};
  if (fs.existsSync(STATUS_FILE)) {
    try {
      completed = JSON.parse(fs.readFileSync(STATUS_FILE, 'utf8'));
    } catch (e) {}
  }

  const isDone = (t) => completed[t] || completed[t.replace(/\\/g, '/')] || completed[t.replace(/\//g, '\\')];
  const topicsToProcess = allTopics.filter(t => !isDone(t) || FORCE);
  const queue = LIMIT ? topicsToProcess.slice(0, LIMIT) : topicsToProcess;
  console.log(`Topics remaining to process: ${queue.length} / ${allTopics.length}`);

  const CONCURRENCY = parseInt(getArg('--concurrency') || '2', 10);
  console.log(`Running with concurrency = ${CONCURRENCY} workers across ${apiKeys.length} API keys.`);

  let cursor = 0;
  let successCount = 0;

  async function worker(workerId) {
    while (cursor < queue.length) {
      const idx = cursor++;
      const topic = queue[idx];
      console.log(`\n[Worker ${workerId}] [${idx + 1}/${queue.length}] (${Math.round((idx / queue.length) * 100)}%) Starting: ${topic}`);
      try {
        const ok = await processTopic(topic);
        if (ok) {
          completed[topic] = { translatedAt: new Date().toISOString() };
          fs.writeFileSync(STATUS_FILE, JSON.stringify(completed, null, 2), 'utf8');
          successCount++;
        }
      } catch (err) {
        console.error(`[Worker ${workerId}] Error processing ${topic}:`, err.message);
      }
    }
  }

  const workers = Array.from({ length: Math.min(CONCURRENCY, queue.length) }, (_, i) => worker(i + 1));
  await Promise.all(workers);

  console.log(`\n========================================`);
  console.log(`Translation run completed: ${successCount} topics processed successfully.`);
  console.log(`========================================\n`);
}

main().catch(err => {
  console.error('FATAL:', err);
  process.exit(1);
});
