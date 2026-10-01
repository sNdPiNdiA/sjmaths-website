#!/usr/bin/env node
/**
 * ============================================================================
 * SJ Maths — Chemistry Content Generator Pipeline (Concise Competitive Prep)
 * Target: UP PGT Chemistry (Subject Code 02) & Advanced Competitive Standards
 * 5 Modular Tabs:
 *   1. 📖 Study Notes (Concise Bullets, Formulas, Exceptions & Mnemonics)
 *   2. ⚡ Revision Summary (Glossary, Must-Remember, Confusions)
 *   3. ❓ Practice Quiz (18-20 Interactive MCQs with Live Score)
 *   4. 🏛️ Previous Years Questions (PYQs & Exam Trends)
 *   5. ⏱️ Timed Topic Test (10-Minute Countdown Test & Modal)
 *
 * Rotating sequence: gemini-3.5-flash, gemini-3.6-flash, gemini-3.7-flash, gemini-3.8-flash
 * Multi-API key rotation supported
 * ============================================================================
 */

import fs from 'fs';
import path from 'path';
import 'dotenv/config';
import { GoogleGenAI } from '@google/genai';
import { jsonrepair } from 'jsonrepair';
import { renderTopicHtml } from './lib/chemistry-renderer.mjs';

// Load API Keys for multi-key rotation
const apiKeys = [...new Set([
  process.env.GEMINI_API_KEY_2,
  process.env.GEMINI_API_KEY_1,
  process.env.GEMINI_API_KEY
].filter(Boolean))];

if (apiKeys.length === 0) {
  console.error('CRITICAL ERROR: No GEMINI_API_KEY defined in .env');
  process.exit(1);
}

console.log(`Loaded ${apiKeys.length} Gemini API keys for round-robin rotation.`);
const aiClients = apiKeys.map((key, i) => ({
  id: i + 1,
  preview: key.substring(0, 10) + '...' + key.slice(-6),
  client: new GoogleGenAI({ apiKey: key })
}));
let clientIndex = 0;

// Parse Command Line Arguments
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
const DRY_RUN = hasFlag('--dry-run');
const GAP_MS = getArg('--gap') ? parseInt(getArg('--gap'), 10) * 1000 : 0; // 0s default (no delay)

const MODELS = [
  'gemini-3.7-flash',
  'gemini-3.8-flash',
  'gemini-3.1-flash-lite',
  'gemini-3.5-flash'
];
let modelIndex = 0;

const modelCallCounts = {
  'gemini-3.7-flash': 0,
  'gemini-3.8-flash': 0,
  'gemini-3.1-flash-lite': 0,
  'gemini-3.5-flash': 0
};

// Status Tracking File
const STATUS_FILE = 'content-generation-status-chemistry.json';
let statusMap = {};
if (fs.existsSync(STATUS_FILE)) {
  try {
    statusMap = JSON.parse(fs.readFileSync(STATUS_FILE, 'utf8'));
  } catch (e) {
    statusMap = {};
  }
}

function saveStatus() {
  fs.writeFileSync(STATUS_FILE, JSON.stringify(statusMap, null, 2), 'utf8');
}

// Load Inventory & Tracker Sequences
const INVENTORY_FILE = 'scratch/chemistry_inventory.json';
if (!fs.existsSync(INVENTORY_FILE)) {
  console.error(`Inventory file not found at ${INVENTORY_FILE}. Run scratch/analyze_chemistry_topics.mjs first.`);
  process.exit(1);
}
const inventory = JSON.parse(fs.readFileSync(INVENTORY_FILE, 'utf8'));

const pgtSequence = fs.existsSync('scratch/pgt_chemistry_parsed.json')
  ? JSON.parse(fs.readFileSync('scratch/pgt_chemistry_parsed.json'))
  : [];

// Map section folders to clean titles
const SECTION_NAMES = {
  'physical-chemistry': { en: 'Physical Chemistry', code: '01' },
  'inorganic-chemistry': { en: 'Inorganic Chemistry', code: '02' },
  'organic-chemistry': { en: 'Organic Chemistry', code: '03' },
  'chemistry-in-everyday-life': { en: 'Chemistry in Everyday Life', code: '04' },
  'atomic-structure': { en: 'Atomic Structure and Quantum Mechanics', code: '05' },
  'chemical-bonding': { en: 'Chemical Bonding and Molecular Structure', code: '06' },
  'chemical-reactions': { en: 'Chemical Reactions and Stoichiometry', code: '07' },
  'electrochemistry': { en: 'Electrochemistry and Redox Processes', code: '08' },
  'foundations': { en: 'Basic Principles and Foundations of Chemistry', code: '09' },
  'nuclear-chemistry': { en: 'Nuclear Chemistry and Radioactivity', code: '10' },
  'periodic-table': { en: 'Periodic Classification and Periodicity', code: '11' }
};

/**
 * Filter topics to process
 */
function getEligibleTopics() {
  return inventory.filter(item => {
    if (TARGET_TOPIC) {
      const cleanTarget = TARGET_TOPIC.endsWith('/') ? TARGET_TOPIC : TARGET_TOPIC + '/';
      return item.url === cleanTarget;
    }
    if (TARGET_SECTION) {
      if (!item.url.includes(`/${TARGET_SECTION}/`)) return false;
    }
    if (!FORCE && statusMap[item.url] && statusMap[item.url].status === 'completed') {
      return false;
    }
    return true;
  });
}

/**
 * Build context for a topic
 */
function getTopicContext(item) {
  const parts = item.url.split('/').filter(Boolean);
  const sectionKey = parts[1] || 'general';
  const sectionMeta = SECTION_NAMES[sectionKey] || { en: sectionKey.replace(/-/g, ' ').replace(/\b\w/g, c => c.toUpperCase()), code: '00' };

  let prevTopic = null;
  let nextTopic = null;

  const inPgtIdx = pgtSequence.findIndex(t => t.href === item.url);
  if (inPgtIdx !== -1) {
    if (inPgtIdx > 0) prevTopic = pgtSequence[inPgtIdx - 1];
    if (inPgtIdx < pgtSequence.length - 1) nextTopic = pgtSequence[inPgtIdx + 1];
  }

  const sectionPrefix = `/chemistry/${sectionKey}/`;
  const related = inventory
    .filter(other => other.url.startsWith(sectionPrefix) && other.url !== item.url)
    .slice(0, 6)
    .map(r => {
      const segs = r.url.split('/').filter(Boolean);
      const slug = segs[segs.length - 1];
      const titleClean = slug.split('-').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' ');
      return { url: r.url, title: titleClean };
    });

  return {
    sectionKey,
    sectionMeta,
    prevTopic,
    nextTopic,
    related
  };
}

/**
 * Construct Gemini Prompt for Concise Competitive Chemistry Notes
 */
function buildPrompt(item, context) {
  const segs = item.url.split('/').filter(Boolean);
  const topicSlug = segs[segs.length - 1];
  const topicTitleGuess = item.titleGuess || topicSlug.split('-').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' ');

  return `
You are an expert Chemistry Professor preparing exam revision material for UP PGT Chemistry (Subject Code 02).

Topic Details:
- Subject: Chemistry
- Branch: ${context.sectionMeta.en}
- Topic Slug: ${topicSlug}
- Reference Topic: ${topicTitleGuess}
- Canonical URL: ${item.url}

CRITICAL RULES TO AVOID AI-GENERATED TONE:
1. STRICTLY NO PROMOTIONAL FILLER OR SELF-REFERENTIAL TEXT: NEVER write phrases like "In this module, we will explore...", "This is a high-yield topic", "Crucial for competitive exams", "Students must master this", "Important for UP PGT", "Here is a breakdown", or "Let's dive in". State the pure scientific facts and formulas directly.
2. CLEAN SCIENTIFIC TOPIC TITLE: The "title" property MUST be just the clean, academic topic name (e.g. "First Law of Thermodynamics", "Aldol Condensation", "Crystal Field Theory"). Do NOT append subtitles like "- High-Yield Study Notes" or "for UP PGT".
3. CONCISE 1-2 LINE BULLETS ONLY: No long narrative paragraphs anywhere.
4. AUTHENTIC TOPIC-SPECIFIC HEADINGS: In "concise_notes", use 3 authentic headings describing the actual chemistry concepts of this topic. Do NOT use generic template titles like "Module 1: Core Principles".
5. CLEAN CHEMICAL NOTATION: Use proper HTML tags (H<sub>2</sub>SO<sub>4</sub>, [Co(NH<sub>3</sub>)<sub>6</sub>]<sup>3+</sup>, Fe<sup>2+</sup>, &Delta;H&deg;, sp<sup>3</sup>d<sup>2</sup>, &rarr;).
6. CLEAN PYQ TAGS: In "pyq_patterns", set "year_tag" to authentic labels like "UP PGT 2021", "UP PGT 2016", "UP PGT 2013", or "Model Question".

REQUIRED JSON OUTPUT SCHEMA:
{
  "title": "Clean academic topic name only (e.g. 'First Law of Thermodynamics')",
  "short_intro": "Strictly 2 direct, factual sentences defining the governing physical or chemical principle. Absolutely no promotional or introductory filler.",
  
  "formula_sheet": [
    {
      "name": "Exact Name of Formula / Law",
      "equation_html": "Equation with sub/sup (e.g. &Delta;U = q + w)",
      "conditions": "When it applies (e.g. Closed system, ideal gas)",
      "units": "Units for variables (e.g. &Delta;U, q, w in Joules)"
    }
  ],

  "concise_notes": [
    {
      "module_title": "Authentic Topic-Specific Heading 1",
      "bullets": [
        "Crisp 1-2 line factual point with key terms bolded.",
        "Specific equation, boundary condition, or IUPAC convention."
      ]
    },
    {
      "module_title": "Authentic Topic-Specific Heading 2",
      "bullets": [
        "Crisp 1-2 line factual point with key terms bolded.",
        "Specific quantitative relation, reaction path, or mechanism detail."
      ]
    },
    {
      "module_title": "Authentic Topic-Specific Heading 3",
      "bullets": [
        "Crisp 1-2 line factual point with key terms bolded.",
        "Specific property, experimental observation, or trend."
      ]
    }
  ],

  "critical_exceptions": [
    {
      "rule": "Expected General Trend or Rule",
      "exception": "Specific Chemical Anomaly",
      "reason": "Scientific rationale (e.g. inert pair effect, half-filled d-subshell stability)"
    }
  ],

  "tips_and_tricks": [
    {
      "trick_title": "Shortcut or Mnemonic Name",
      "shortcut_formula": "Quick formula or mnemonic rule",
      "application": "How to quickly apply it to solve MCQs or numericals"
    }
  ],

  "comparison_matrix": {
    "title": "Comparison Title (e.g. Reversible vs Irreversible Expansion)",
    "headers": ["Parameter", "Class A", "Class B"],
    "rows": [
      ["Condition", "State A description", "State B description"],
      ["Work Equation", "Equation A", "Equation B"]
    ]
  },

  "exam_points": [
    "Factual takeaway 1 with numerical value or formula",
    "Factual takeaway 2",
    "Factual takeaway 3",
    "Factual takeaway 4",
    "Factual takeaway 5",
    "Factual takeaway 6"
  ],

  "common_pitfalls": [
    "Common mistake 1 and the correct scientific rule",
    "Common mistake 2 regarding units or signs",
    "Common mistake 3 regarding conditions or reagents",
    "Common mistake 4"
  ],

  "chapter_summary_concepts": [
    {
      "concept_title": "Core Concept 1",
      "concept_body_html": "<p>2-line factual summary of governing equations and principles.</p>"
    },
    {
      "concept_title": "Core Concept 2",
      "concept_body_html": "<p>2-line factual summary.</p>"
    },
    {
      "concept_title": "Core Concept 3",
      "concept_body_html": "<p>2-line factual summary.</p>"
    },
    {
      "concept_title": "Core Concept 4",
      "concept_body_html": "<p>2-line factual summary.</p>"
    }
  ],

  "quick_revision": {
    "terms_glossary": [
      { "term": "Term 1", "term_en": "Symbol / Formula", "definition": "Direct definition with SI unit." },
      { "term": "Term 2", "term_en": "Symbol / Formula", "definition": "Direct definition." },
      { "term": "Term 3", "term_en": "Symbol / Formula", "definition": "Direct definition." },
      { "term": "Term 4", "term_en": "Symbol / Formula", "definition": "Direct definition." },
      { "term": "Term 5", "term_en": "Symbol / Formula", "definition": "Direct definition." },
      { "term": "Term 6", "term_en": "Symbol / Formula", "definition": "Direct definition." }
    ],
    "must_remember": [
      "Key equation or constant 1",
      "Key equation or constant 2",
      "Key equation or constant 3",
      "Key equation or constant 4",
      "Key equation or constant 5"
    ],
    "summary": [
      "Key recap point 1",
      "Key recap point 2",
      "Key recap point 3",
      "Key recap point 4"
    ],
    "common_confusions": [
      {
        "term_a": "Concept A",
        "term_b": "Concept B",
        "difference": "Direct distinguishing criteria."
      }
    ]
  },

  "quiz": [
    {
      "question": "Conceptual multiple-choice question?",
      "options": ["Option A", "Option B", "Option C", "Option D"],
      "correct_index": 0,
      "explanation": "Clear step-by-step scientific explanation of why this option is correct."
    }
  ],

  "pyq_patterns": [
    {
      "year_tag": "UP PGT 2021",
      "question": "Exam-level multiple-choice question?",
      "options": ["Option A", "Option B", "Option C", "Option D"],
      "correct_index": 0,
      "explanation": "Direct scientific solution."
    }
  ],

  "topic_test": [
    {
      "question": "Timed test multiple choice question?",
      "options": ["Option A", "Option B", "Option C", "Option D"],
      "correct_index": 0,
      "explanation": "Direct solution and derivation."
    }
  ]
}

COUNTS:
- 'formula_sheet': 4 to 6 formulas.
- 'concise_notes': Exactly 3 modules with 3 to 5 crisp bullet points each.
- 'critical_exceptions': 3 to 4 anomalies.
- 'tips_and_tricks': 3 shortcuts/mnemonics.
- 'quiz': 18 to 20 practice questions.
- 'pyq_patterns': 5 to 6 questions.
- 'topic_test': Exactly 10 questions.
`;
}

/**
 * Sanitize raw text to ensure valid JSON parse
 */
function cleanRawJson(text) {
  let cleaned = text.trim();
  if (cleaned.startsWith('```json')) cleaned = cleaned.slice(7);
  else if (cleaned.startsWith('```')) cleaned = cleaned.slice(3);
  if (cleaned.endsWith('```')) cleaned = cleaned.slice(0, -3);
  return cleaned.trim();
}

/**
 * Validate parsed content
 */
function validateContent(data) {
  if (!data.title || typeof data.title !== 'string') throw new Error('Missing title');
  if (!data.short_intro || typeof data.short_intro !== 'string') throw new Error('Missing short_intro');
  if (!Array.isArray(data.quiz) || data.quiz.length < 15) {
    throw new Error(`Quiz array insufficient: expected >=15, got ${data.quiz ? data.quiz.length : 0}`);
  }
  if (!Array.isArray(data.topic_test) || data.topic_test.length < 8) {
    throw new Error(`Topic test array insufficient: expected >=8, got ${data.topic_test ? data.topic_test.length : 0}`);
  }
}

/**
 * Normalize MCQs
 */
function normalizeQuestions(arr) {
  if (!Array.isArray(arr)) return;
  arr.forEach(q => {
    if (!q || typeof q !== 'object') return;
    if (!Array.isArray(q.options)) {
      if (q.options && typeof q.options === 'object') {
        q.options = Object.values(q.options);
      } else {
        q.options = [];
      }
    }
    while (q.options.length < 4) {
      q.options.push(`Option ${String.fromCharCode(65 + q.options.length)}`);
    }
    q.options = q.options.slice(0, 4).map(opt => String(opt ?? ''));

    if (typeof q.correct_index !== 'number' || q.correct_index < 0 || q.correct_index > 3) {
      if (typeof q.correct_answer === 'string') {
        const char = q.correct_answer.trim().toUpperCase().charAt(0);
        const map = { 'A': 0, 'B': 1, 'C': 2, 'D': 3 };
        q.correct_index = map[char] !== undefined ? map[char] : 0;
      } else {
        q.correct_index = 0;
      }
    }
    if (!q.explanation) q.explanation = 'Direct application of the governing principle and formula.';
  });
}

/**
 * Convert markdown bold (**text**) and italics (*text*) to HTML tags
 */
function cleanMarkdownStars(val) {
  if (typeof val === 'string') {
    return val
      .replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>')
      .replace(/(^|[^\*])\*([^*\n]+)\*([^\*]|$)/g, '$1<em>$2</em>$3');
  }
  if (Array.isArray(val)) {
    return val.map(cleanMarkdownStars);
  }
  if (val !== null && typeof val === 'object') {
    const res = {};
    for (const key of Object.keys(val)) {
      res[key] = cleanMarkdownStars(val[key]);
    }
    return res;
  }
  return val;
}


async function processTopic(item) {
  const context = getTopicContext(item);
  console.log(`\n------------------------------------------------------------`);
  console.log(`Processing Topic: ${item.url}`);
  console.log(`Branch: ${context.sectionMeta.en} | Target: UP PGT Chemistry`);

  if (DRY_RUN) {
    console.log(`[DRY RUN] Would generate: ${item.url}`);
    return true;
  }

  statusMap[item.url] = {
    status: 'generating',
    startedAt: new Date().toISOString()
  };
  saveStatus();

  const prompt = buildPrompt(item, context);

  let rawJsonText = null;
  let parsedData = null;
  const maxRetries = 8;

  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    const currentModel = MODELS[modelIndex % MODELS.length];
    modelIndex++;
    modelCallCounts[currentModel]++;

    const activeClientObj = aiClients[clientIndex % aiClients.length];
    clientIndex++;

    try {
      console.log(`Calling Gemini API [Model: ${currentModel} | Key: #${activeClientObj.id} (${activeClientObj.preview})] (Call #${modelCallCounts[currentModel]} | Attempt ${attempt}/${maxRetries})...`);
      const response = await activeClientObj.client.models.generateContent({
        model: currentModel,
        contents: prompt,
        config: {
          responseMimeType: 'application/json',
          temperature: 0.3,
          maxOutputTokens: 32768
        }
      });

      rawJsonText = cleanRawJson(response.text);
      try {
        parsedData = JSON.parse(rawJsonText);
      } catch (jsonErr) {
        console.warn('Initial JSON.parse failed, attempting jsonrepair...');
        parsedData = JSON.parse(jsonrepair(rawJsonText));
      }

      normalizeQuestions(parsedData.quiz);
      normalizeQuestions(parsedData.pyq_patterns);
      normalizeQuestions(parsedData.topic_test);

      parsedData = cleanMarkdownStars(parsedData);

      validateContent(parsedData);
      console.log(`✓ Content validated successfully using ${currentModel} for: ${parsedData.title}`);
      break;
    } catch (err) {
      console.error(`Attempt ${attempt} on ${currentModel} failed:`, err.message);
      if (attempt === maxRetries) {
        statusMap[item.url] = {
          status: 'validation_failed',
          error: err.message,
          failedAt: new Date().toISOString()
        };
        saveStatus();
        return false;
      }
      const waitTime = err.message.includes('503') ? Math.max(GAP_MS, 15000) : GAP_MS;
      console.log(`Waiting ${waitTime / 1000}s before next attempt...`);
      await new Promise(r => setTimeout(r, waitTime));
    }
  }

  // Target directory
  const targetDir = path.resolve(item.dir);
  fs.mkdirSync(targetDir, { recursive: true });

  // Save JSON files
  fs.writeFileSync(path.join(targetDir, 'quiz.json'), JSON.stringify(parsedData.quiz, null, 2), 'utf8');
  fs.writeFileSync(path.join(targetDir, 'topic-test.json'), JSON.stringify(parsedData.topic_test, null, 2), 'utf8');
  if (parsedData.pyq_patterns) {
    fs.writeFileSync(path.join(targetDir, 'pyq.json'), JSON.stringify(parsedData.pyq_patterns, null, 2), 'utf8');
  }

  // Render & write HTML
  const targetHtmlPath = path.join(targetDir, 'index.html');
  const finalHtml = renderTopicHtml(item, context, parsedData);
  fs.writeFileSync(targetHtmlPath, finalHtml, 'utf8');
  console.log(`✓ Successfully saved: ${targetHtmlPath}`);

  const wordCount = (finalHtml.match(/\b\w+\b/g) || []).length;

  statusMap[item.url] = {
    status: 'completed',
    title: parsedData.title,
    wordCount,
    quizCount: parsedData.quiz.length,
    testCount: parsedData.topic_test.length,
    completedAt: new Date().toISOString(),
    reviewed: false
  };
  saveStatus();

  return true;
}

/**
 * Main Execution Loop
 */
async function main() {
  console.log('=== SJ Maths Chemistry Content Generator Pipeline (Concise Prep Method) ===');
  console.log(`Configured Rotating Models: ${MODELS.join(', ')}`);
  console.log(`Rate-limit buffer: ${GAP_MS / 1000}s gap between every API call`);

  const eligible = getEligibleTopics();
  console.log(`Eligible topics found: ${eligible.length}`);

  const toProcess = LIMIT ? eligible.slice(0, LIMIT) : eligible;
  console.log(`Topics scheduled to process: ${toProcess.length}`);

  let successCount = 0;
  for (let i = 0; i < toProcess.length; i++) {
    const item = toProcess[i];
    console.log(`\n[${i + 1}/${toProcess.length}] Processing: ${item.url}`);
    
    let ok = false;
    try {
      ok = await processTopic(item);
    } catch (err) {
      console.error(`Unexpected error processing ${item.url}:`, err);
      statusMap[item.url] = {
        status: 'error',
        error: err.message,
        failedAt: new Date().toISOString()
      };
      saveStatus();
    }
    if (ok) successCount++;

    if (i < toProcess.length - 1 && !DRY_RUN && GAP_MS > 0) {
      console.log(`Waiting ${GAP_MS / 1000}s before next API call...`);
      await new Promise(r => setTimeout(r, GAP_MS));
    }
  }

  console.log('\n============================================================');
  console.log(`Finished processing. Successfully completed: ${successCount}/${toProcess.length}`);
  console.log('Final Model Call Counts:', modelCallCounts);
}

main().catch(err => {
  console.error('Fatal Generator Error:', err);
  process.exit(1);
});
