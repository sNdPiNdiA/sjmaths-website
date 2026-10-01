#!/usr/bin/env node
/**
 * ============================================================================
 * SJ Maths — English Generator (Chemistry/Topic-Page Standard)
 * Styled with /assets/css/topic-page.min.css & Earth Emerald Palette
 * ============================================================================
 */

import fs from 'fs';
import path from 'path';
import 'dotenv/config';
import { GoogleGenAI } from '@google/genai';
import { jsonrepair } from 'jsonrepair';
import { compileTopicHtml } from './lib/english-compiler.mjs';

// Single-key mode using another API key
const apiKeys = [process.env.GEMINI_API_KEY_1].filter(Boolean);

if (apiKeys.length === 0) {
  console.error('CRITICAL ERROR: No GEMINI_API_KEY_1 defined in .env');
  process.exit(1);
}

console.log(`Loaded ${apiKeys.length} Gemini API keys for round-robin rotation.`);
const aiClients = apiKeys.map((key, i) => ({
  id: i + 1,
  preview: key.substring(0, 10) + '...' + key.slice(-6),
  client: new GoogleGenAI({ apiKey: key })
}));
let clientIndex = 0;

// Parse CLI Arguments
const args = process.argv.slice(2);
function getArg(flag) {
  const idx = args.indexOf(flag);
  return idx !== -1 && args[idx + 1] ? args[idx + 1] : null;
}
const hasFlag = (flag) => args.includes(flag);

const TARGET_TOPIC = getArg('--topic');
const TARGET_SECTION = getArg('--section');
const LIMIT = getArg('--limit') ? parseInt(getArg('--limit'), 10) : null;
const FORCE = hasFlag('--force');
const GAP_MS = getArg('--gap') ? parseInt(getArg('--gap'), 10) * 1000 : 0;

const MODELS = ['gemini-3.5-flash-lite'];
const STATUS_FILE = 'content-generation-status-english.json';

function loadStatus() {
  if (fs.existsSync(STATUS_FILE)) {
    try {
      return JSON.parse(fs.readFileSync(STATUS_FILE, 'utf8'));
    } catch (e) {
      return {};
    }
  }
  return {};
}

function saveStatus(status) {
  fs.writeFileSync(STATUS_FILE, JSON.stringify(status, null, 2), 'utf8');
}

const statusMap = loadStatus();

// --- Subtopic Extraction ---
function getUrlToTopicsMap() {
  const urlToTopics = {};
  if (fs.existsSync('up-pgt-english/index.html')) {
    const pgtHtml = fs.readFileSync('up-pgt-english/index.html', 'utf8');
    const pgtRegex = /<div class="topic"[^>]*data-search="([^"]+)"[\s\S]*?<a class="topic-link" href="([^"]+)">([^<]+)<\/a>/g;
    let match;
    while ((match = pgtRegex.exec(pgtHtml)) !== null) {
      const [_, dataSearch, url, title] = match;
      if (!urlToTopics[url]) urlToTopics[url] = new Set();
      urlToTopics[url].add(title.trim());
    }
  }
  if (fs.existsSync('up-tgt-english/index.html')) {
    const tgtHtml = fs.readFileSync('up-tgt-english/index.html', 'utf8');
    const tgtRegex = /<div class="topic"[^>]*data-search="([^"]+)"[\s\S]*?<a class="topic-link" href="([^"]+)">([^<]+)<\/a>/g;
    let match;
    while ((match = tgtRegex.exec(tgtHtml)) !== null) {
      const [_, dataSearch, url, title] = match;
      if (url.includes('/english/')) {
        if (!urlToTopics[url]) urlToTopics[url] = new Set();
        urlToTopics[url].add(title.trim());
      }
    }
  }
  const result = {};
  for (const [url, set] of Object.entries(urlToTopics)) {
    result[url] = Array.from(set);
  }
  return result;
}
const globalUrlToTopics = getUrlToTopicsMap();

function getAllEnglishPages(dir = 'english') {
  let pages = [];
  if (!fs.existsSync(dir)) return pages;
  const list = fs.readdirSync(dir, { withFileTypes: true });
  for (const item of list) {
    const full = path.join(dir, item.name);
    if (item.isDirectory()) {
      pages = pages.concat(getAllEnglishPages(full));
    } else if (item.name === 'index.html') {
      let rel = full.replace(/\\/g, '/');
      if (!rel.startsWith('/')) rel = '/' + rel;
      rel = rel.replace(/index\.html$/, '');
      pages.push(rel);
    }
  }
  return pages;
}

function getTopicContext(topicUrl) {
  const parts = topicUrl.split('/').filter(Boolean);
  const branch = parts[1] || 'general';
  const subBranch = parts[2] || '';
  const slug = parts[parts.length - 1];

  const formatTitle = (s) => s.split('-').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' ');

  let sectionTitle = formatTitle(branch);
  if (subBranch && subBranch !== slug) {
    sectionTitle += ` — ${formatTitle(subBranch)}`;
  }

  const topicName = formatTitle(slug);
  const subtopics = globalUrlToTopics[topicUrl] || [];

  return {
    branch,
    subBranch,
    slug,
    sectionTitle,
    topicName,
    topicUrl,
    subtopics
  };
}

// ----------------------------------------------------------------------------
// PROMPT BUILDERS (2-Call Architecture)
// ----------------------------------------------------------------------------

function buildCall1Prompt(context) {
  const subtopicsText = context.subtopics && context.subtopics.length > 0 
    ? `\nSubtopics to Cover:\n${context.subtopics.map(t => `- ${t}`).join('\n')}` 
    : '';

  return `You are a distinguished Professor of English Literature and Linguistics, and Chief Academic Examiner for UP TGT/PGT English.
Produce deep, rigorous, exhaustive, academic-grade Study Notes for the topic:
Topic: "${context.topicName}"
Section/Branch: "${context.sectionTitle}"${subtopicsText}
Exam Targets: UP PGT English (Subject Code 02), UP TGT English, UGC-NET.

Return ONLY a valid, parseable JSON object matching this structure:
{
  "title": "${context.topicName}: Comprehensive Literary & Grammatical Analysis",
  "short_intro": "High-yield conceptual breakdown and foundational study notes of ${context.topicName} tailored for competitive exam mastery.",
  "academic_synopsis": "Exhaustive 2-3 paragraph academic overview detailing the foundational definitions, historical context, major works/rules, and exam relevance.",
  "conceptual_pillars": [
    {
      "pillar_title": "Title of Major Conceptual Pillar (e.g. Author Biography / Plot Summary / Grammatical Rules / Themes)",
      "lead_concept": "Key literary movement, character analysis, or grammatical principle.",
      "detailed_analysis_points": [
        "DO NOT use long explanations or paragraphs.",
        "STRICTLY use short, high-yield bullet points.",
        "Ensure ALL subtopics provided are comprehensively covered."
      ],
      "comparative_insights": "Direct comparison with related works, authors, or competing grammatical theories (e.g., Shakespeare vs Marlowe, Active vs Passive voice).",
      "key_takeaways": [
        "Concise core takeaways and factual benchmarks."
      ]
    }
  ],
  "spatial_and_regional_distribution": {
    "global_patterns": "Major literary movements globally or historical eras (e.g., Renaissance, Victorian Era).",
    "indian_context": "Impact or context related to Indian Writing in English or local adaptations, if applicable."
  },
  "formulas_and_scales": [
    {
      "name": "Literary Device or Grammar Rule Name (e.g., Sonnet Structure, Subject-Verb Agreement)",
      "equation": "Definition or structure (e.g. ABBA ABBA CDE CDE for Petrarchan Sonnet)",
      "parameters": "Explanation of the components (meter, syllables, clauses)",
      "exam_significance": "Why this appears in competitive exams and typical questions"
    }
  ],
  "tricks_and_mnemonics": [
    {
      "title": "High-Yield Mnemonic / Memory Shortcut",
      "type": "Mnemonic",
      "mnemonic": "Memorable acronym or phonetic phrase to remember works or rules",
      "explanation": "Clear breakdown of what each letter/word stands for",
      "exam_pitfall_warning": "Common mistake or distractor trap set by examiners (e.g. commonly misspelled words)"
    }
  ]
}

CRITICAL RULES:
1. Include at least 3-4 deep conceptual pillars with thorough academic analysis.
2. Ensure ALL subtopics provided are comprehensively covered across the conceptual pillars.
3. STRICTLY use short bullet points in 'detailed_analysis_points'. DO NOT WRITE LONG PARAGRAPHS.
4. Include at least 2 literary forms, grammatical rules, or structures in 'formulas_and_scales'.
5. Include at least 2-3 practical memory mnemonics or exam tips.
6. Output pure JSON without markdown code fences or conversational prose.`;
}

function buildCall2Prompt(context, call1Data) {
  return `You are a Senior Question Setter for UP PGT English, UP TGT, and UGC-NET.
Based on the topic "${context.topicName}" under "${context.sectionTitle}", generate high-yield quick revision concepts and assessment items.

Return ONLY a valid, parseable JSON object matching this structure:
{
  "quick_revision": {
    "glossary_terms": [
      {
        "term": "Key Literary or Grammatical Term",
        "definition": "Precise, exam-standard 1-2 sentence definition",
        "exam_tag": "Term Tag"
      }
    ],
    "high_yield_laws_and_theories": [
      {
        "theorist_or_law": "Name of Author, Critic, or Rule (e.g. T.S. Eliot, Chomsky, Noam)",
        "year_or_period": "Year/Period (e.g. 1922, Elizabethan Age)",
        "core_postulate": "Core postulate, famous quote, or summary of their major contribution"
      }
    ]
  },
  "practice_quiz": [
    {
      "question": "Clear, rigorous MCQ testing conceptual understanding (e.g. identifying a quote, grammar rule, or author)",
      "options": ["Option A", "Option B", "Option C", "Option D"],
      "correct_index": 0,
      "explanation": "Detailed explanation explaining why the correct option is right and others are incorrect."
    }
  ],
  "pyqs": [
    {
      "exam_year": "UP PGT English (Previous Year Pattern)",
      "question": "Authentic competitive exam level question",
      "options": ["Option A", "Option B", "Option C", "Option D"],
      "correct_index": 1,
      "explanation": "Complete solution with examiner notes and context."
    }
  ],
  "topic_test": [
    {
      "question": "Rigorous timed test question testing analytical/factual mastery",
      "options": ["Option A", "Option B", "Option C", "Option D"],
      "correct_index": 2,
      "explanation": "In-depth rationale and correct solution."
    }
  ]
}

CRITICAL RULES:
1. Provide 12-15 glossary terms and 3-5 author/critic/rule models.
2. Provide 18-20 Practice Quiz MCQs with diverse cognitive difficulty.
3. Provide 5-6 PYQs representing real UP TGT/PGT/NET patterns.
4. Provide exactly 10 Timed Topic Test questions.
5. Output pure JSON without markdown code fences.`;
}

// ----------------------------------------------------------------------------
// HTML COMPILER (Chemistry topic-page.min.css & JS Standard)
// ----------------------------------------------------------------------------


// ----------------------------------------------------------------------------
// API CALL EXECUTION
// ----------------------------------------------------------------------------

async function callGeminiApi(prompt, model, attempt) {
  const activeClientObj = aiClients[clientIndex % aiClients.length];
  clientIndex++;

  console.log(`Calling Gemini API [Model: ${model} | Key: #${activeClientObj.id} (${activeClientObj.preview})] (Attempt ${attempt})...`);
  const response = await activeClientObj.client.models.generateContent({
    model: model,
    contents: prompt,
    config: {
      temperature: 0.35,
      responseMimeType: 'application/json'
    }
  });

  if (!response || !response.text) {
    throw new Error('Empty response from Gemini API');
  }

  return response.text;
}

function parseGeminiJson(rawText) {
  let cleaned = rawText.trim();
  cleaned = cleaned.replace(/^```(?:json)?\s*/i, '').replace(/\s*```$/i, '').trim();

  try {
    return JSON.parse(cleaned);
  } catch (err1) {
    try {
      const repaired = jsonrepair(cleaned);
      return JSON.parse(repaired);
    } catch (err2) {
      throw new Error(`JSON parse & repair failed: ${err1.message}`);
    }
  }
}

async function generateWithRetry(prompt, model, validatorFn, maxRetries = 4) {
  let lastError = null;
  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try {
      const text = await callGeminiApi(prompt, model, attempt);
      const parsed = parseGeminiJson(text);
      if (validatorFn(parsed)) {
        return parsed;
      }
      throw new Error('Response failed validation check');
    } catch (err) {
      lastError = err;
      console.warn(`[Attempt ${attempt}/${maxRetries} failed]: ${err.message}`);
      if (attempt < maxRetries) {
        const delay = attempt * 3000;
        console.log(`Waiting ${delay / 1000}s before retry...`);
        await new Promise(r => setTimeout(r, delay));
      }
    }
  }
  throw lastError;
}

// ----------------------------------------------------------------------------
// MAIN ORCHESTRATOR
// ----------------------------------------------------------------------------

async function processTopic(topicUrl) {
  const context = getTopicContext(topicUrl);
  console.log(`\n========================================`);
  console.log(`Processing English Topic: ${topicUrl}`);
  console.log(`Branch: ${context.sectionTitle} | Topic: ${context.topicName}`);
  console.log(`========================================`);

  statusMap[topicUrl] = { status: 'generating', startedAt: new Date().toISOString() };
  saveStatus(statusMap);

  const model = MODELS[0];

  // CALL 1: Deep Study Notes & Memory Aids
  console.log(`\n--- [CALL 1/2] Generating Study Notes, Pillars, Spatial Models, Formulas & Mnemonics ---`);
  const call1Prompt = buildCall1Prompt(context);
  const call1Data = await generateWithRetry(
    call1Prompt,
    model,
    (res) => res && res.conceptual_pillars && res.conceptual_pillars.length >= 2
  );
  console.log(`✓ Call 1 validated successfully (${call1Data.conceptual_pillars.length} pillars, ${(call1Data.tricks_and_mnemonics || []).length} mnemonics)`);

  console.log(`Pausing ${GAP_MS / 1000}s between Call 1 and Call 2...`);
  if (GAP_MS > 0) await new Promise(r => setTimeout(r, GAP_MS));

  // CALL 2: Quick Revision, Quiz, PYQs & Timed Test
  console.log(`\n--- [CALL 2/2] Generating Quick Revision, Practice Quiz, PYQs & Timed Test ---`);
  const call2Prompt = buildCall2Prompt(context, call1Data);
  const call2Data = await generateWithRetry(
    call2Prompt,
    model,
    (res) => res && res.practice_quiz && res.practice_quiz.length >= 10 && res.topic_test && res.topic_test.length === 10
  );
  console.log(`✓ Call 2 validated successfully (${(call2Data.quick_revision?.glossary_terms || []).length} glossary, ${call2Data.practice_quiz.length} quiz MCQs, ${call2Data.topic_test.length} test items)`);

  // Compile Final HTML
  const finalHtml = compileTopicHtml(call1Data, call2Data, context);
  const targetDir = path.join(process.cwd(), topicUrl.replace(/^\//, '').replace(/\/$/, ''));
  const targetIndexPath = path.join(targetDir, 'index.html');

  if (!fs.existsSync(targetDir)) {
    fs.mkdirSync(targetDir, { recursive: true });
  }

  // Save JSON data artifacts
  fs.writeFileSync(path.join(targetDir, 'quiz.json'), JSON.stringify(call2Data.practice_quiz, null, 2), 'utf8');
  if (call2Data.pyqs && call2Data.pyqs.length > 0) {
    fs.writeFileSync(path.join(targetDir, 'pyq.json'), JSON.stringify(call2Data.pyqs, null, 2), 'utf8');
  }
  fs.writeFileSync(path.join(targetDir, 'topic-test.json'), JSON.stringify(call2Data.topic_test, null, 2), 'utf8');

  // Save HTML
  fs.writeFileSync(targetIndexPath, finalHtml, 'utf8');
  console.log(`✓ Successfully compiled & saved: ${targetIndexPath}`);

  statusMap[topicUrl] = {
    status: 'completed',
    title: call1Data.title,
    wordCount: finalHtml.split(/\s+/).length,
    pillarsCount: call1Data.conceptual_pillars.length,
    quizCount: call2Data.practice_quiz.length,
    testCount: call2Data.topic_test.length,
    completedAt: new Date().toISOString()
  };
  saveStatus(statusMap);
}

async function main() {
  const allPages = getAllEnglishPages();
  console.log(`Discovered ${allPages.length} active English chapter pages on disk.`);

  let queue = allPages;

  if (TARGET_TOPIC) {
    queue = allPages.filter(p => p.includes(TARGET_TOPIC));
    console.log(`Filtered for target topic "${TARGET_TOPIC}": ${queue.length} match(es).`);
  } else if (TARGET_SECTION) {
    queue = allPages.filter(p => p.includes(TARGET_SECTION));
    console.log(`Filtered for section "${TARGET_SECTION}": ${queue.length} match(es).`);
  }

  if (!FORCE) {
    queue = queue.filter(p => !statusMap[p] || statusMap[p].status !== 'completed');
  }

  if (LIMIT && LIMIT > 0) {
    queue = queue.slice(0, LIMIT);
  }

  console.log(`Queue ready: ${queue.length} topic(s) to process.`);

  let successCount = 0;
  let failCount = 0;

  for (let i = 0; i < queue.length; i++) {
    const topicUrl = queue[i];
    console.log(`\\n[${i + 1}/${queue.length}] Progress: ${Math.round(((i) / queue.length) * 100)}%`);

    try {
      await processTopic(topicUrl);
      successCount++;
    } catch (err) {
      console.error(`❌ Failed to process ${topicUrl}: ${err.message}`);
      statusMap[topicUrl] = { status: 'failed', error: err.message, failedAt: new Date().toISOString() };
      saveStatus(statusMap);
      failCount++;
    }

    if (i < queue.length - 1) {
      if (GAP_MS > 0) {
        console.log(`Cooling down ${GAP_MS / 1000}s before next chapter...`);
        await new Promise(r => setTimeout(r, GAP_MS));
      }
    }
  }

  console.log(`\\n========================================`);
  console.log(`Batch finished. Success: ${successCount}, Failed: ${failCount}`);
  console.log(`========================================`);
}

main().catch(err => {
  console.error('Fatal execution error:', err);
  process.exit(1);
});
