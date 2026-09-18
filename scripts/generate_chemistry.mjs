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

/**
 * Render Complete Topic HTML with 5 Tabs
 */
function renderTopicHtml(item, context, data) {
  const segs = item.url.split('/').filter(Boolean);
  const topicSlug = segs[segs.length - 1];
  const topicTitleGuess = item.titleGuess || topicSlug.split('-').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' ');

  // Clean topic title: strip any AI artifacts like "High-Yield", "Study Notes", "UP PGT", etc.
  const rawTitle = data.title || topicTitleGuess;
  const cleanTitle = rawTitle
    .replace(/\s*[-–—:]\s*(High-Yield|Study Notes|UP PGT|Notes|Chemistry|Rasayan|Comprehensive|Master|Ultimate|Guide).*$/i, '')
    .trim() || topicTitleGuess;

  const canonicalUrl = `https://sjmaths.com${item.url}`;
  const title = `${cleanTitle} | UP PGT Chemistry`;
  const metaDesc = `${cleanTitle}: Key formulas, concise theory, critical exceptions, shortcuts, PYQs, and practice test for UP PGT Chemistry.`;

  // Schema.org Structured Data
  const schemaJsonLd = {
    "@context": "https://schema.org",
    "@type": "LearningResource",
    "name": cleanTitle,
    "headline": `${cleanTitle} — UP PGT Chemistry`,
    "description": metaDesc,
    "url": canonicalUrl,
    "inLanguage": "en",
    "learningResourceType": "Study Guide / Quiz",
    "educationalLevel": "Postgraduate Teacher Recruitment / B.Sc. & M.Sc.",
    "isPartOf": {
      "@type": "WebSite",
      "name": "SJ Maths",
      "url": "https://sjmaths.com/"
    },
    "breadcrumb": {
      "@type": "BreadcrumbList",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://sjmaths.com/" },
        { "@type": "ListItem", "position": 2, "name": "Chemistry", "item": "https://sjmaths.com/chemistry/" },
        { "@type": "ListItem", "position": 3, "name": context.sectionMeta.en, "item": `https://sjmaths.com/chemistry/${context.sectionKey}/` },
        { "@type": "ListItem", "position": 4, "name": cleanTitle, "item": canonicalUrl }
      ]
    }
  };

  // Exam Chips
  const examBadgesHtml = `
    <a class="exam-chip pgt" href="/up-pgt-chemistry/">UP PGT Chemistry</a>
    <span class="exam-chip both">Subject Code 02</span>
    <span class="exam-chip both">B.Sc. / M.Sc. Level</span>
  `;

  // TAB 1: FORMULA SHEET
  function formatMathHtml(str) {
    if (!str) return '';
    const symbolMap = {
      '\\\\hbar': '&#x210f;',
      '\\\\times': '&times;',
      '\\\\cdot': '&middot;',
      '\\\\pm': '&plusmn;',
      '\\\\approx': '&asymp;',
      '\\\\propto': '&prop;',
      '\\\\infty': '&infin;',
      '\\\\Delta': '&Delta;',
      '\\\\pi': '&pi;',
      '\\\\mu': '&mu;',
      '\\\\nu': '&nu;',
      '\\\\alpha': '&alpha;',
      '\\\\beta': '&beta;',
      '\\\\gamma': '&gamma;',
      '\\\\theta': '&theta;',
      '\\\\lambda': '&lambda;',
      '\\\\sigma': '&sigma;',
      '\\\\rho': '&rho;',
      '\\\\epsilon': '&epsilon;',
      '\\\\tau': '&tau;',
      '\\\\omega': '&omega;',
      '\\\\phi': '&phi;',
      '\\\\psi': '&psi;',
      '\\\\partial': '&part;',
      '\\\\sum': '&sum;',
      '\\\\int': '&int;',
      '\\\\rightarrow': '&rarr;',
      '\\\\rightleftharpoons': '&#8652;'
    };
    for (const [pattern, rep] of Object.entries(symbolMap)) {
      str = str.replace(new RegExp(pattern, 'g'), rep);
    }
    str = str.replace(/\\sqrt\{([^{}]+)\}/g, '<span class="math-sqrt">&radic;<span class="math-radicand">$1</span></span>');
    let changed = true;
    let safety = 0;
    while (changed && safety < 10) {
      changed = false;
      safety++;
      str = str.replace(/(?:&frac|\\frac)\{([^{}]+)\}\{([^{}]+)\}/g, (_, num, denom) => {
        changed = true;
        return `<span class="math-frac"><span class="math-num">${num}</span><span class="math-denom">${denom}</span></span>`;
      });
    }
    return str;
  }

  let formulaSheetHtml = '';
  if (Array.isArray(data.formula_sheet) && data.formula_sheet.length > 0) {
    const cards = data.formula_sheet.map(f => `
      <div class="formula-card">
        <div class="formula-name">${f.name}</div>
        <div class="formula-eq">${formatMathHtml(f.equation_html || f.equation)}</div>
        <div class="formula-meta">
          ${f.conditions ? `<div><strong>Conditions:</strong> ${f.conditions}</div>` : ''}
          ${f.units ? `<div><strong>Units:</strong> ${f.units}</div>` : ''}
        </div>
      </div>
    `).join('');

    formulaSheetHtml = `
      <div class="formula-sheet-box">
        <div class="formula-sheet-title">📐 Key Formulas & Equations</div>
        <div class="formula-grid">${cards}</div>
      </div>
    `;
  }

  // TAB 1: CONCISE BULLET NOTES
  let bulletNotesHtml = '';
  if (Array.isArray(data.concise_notes) && data.concise_notes.length > 0) {
    bulletNotesHtml = data.concise_notes.map((m, idx) => `
      <section class="notes-section" id="note-sec-${idx + 1}">
        <h2>${m.module_title}</h2>
        <div class="prose-content">
          <ul class="notes-bullet-list">
            ${m.bullets.map(b => `<li>${b}</li>`).join('')}
          </ul>
        </div>
      </section>
    `).join('');
  }

  // TAB 1: CRITICAL ANOMALIES & EXCEPTIONS
  let exceptionsHtml = '';
  if (Array.isArray(data.critical_exceptions) && data.critical_exceptions.length > 0) {
    const list = data.critical_exceptions.map(e => `
      <div class="exception-card">
        <div class="exception-head">
          <span class="exception-badge">Exception</span>
          <span class="exception-rule">${e.rule}</span>
        </div>
        <p class="exception-detail"><strong>Observation:</strong> ${e.exception} — <em>${e.reason}</em></p>
      </div>
    `).join('');

    exceptionsHtml = `
      <div class="exception-alert-box">
        <div class="exception-alert-title">⚠️ Important Exceptions & Anomalies</div>
        <div class="exception-list">${list}</div>
      </div>
    `;
  }

  // TAB 1: TIPS & MNEMONICS
  let tricksHtml = '';
  if (Array.isArray(data.tips_and_tricks) && data.tips_and_tricks.length > 0) {
    const list = data.tips_and_tricks.map(t => `
      <div class="trick-card">
        <div class="trick-title">${t.trick_title.replace(/^⚡\s*/, '')}</div>
        <div class="trick-shortcut">${t.shortcut_formula}</div>
        <p class="trick-app"><strong>Application:</strong> ${t.application}</p>
      </div>
    `).join('');

    tricksHtml = `
      <div class="trick-box">
        <div class="trick-box-title">💡 Shortcuts & Memory Aids</div>
        <div class="tricks-grid">${list}</div>
      </div>
    `;
  }

  // TAB 1: COMPARISON MATRIX
  let comparisonHtml = '';
  if (data.comparison_matrix && Array.isArray(data.comparison_matrix.headers)) {
    const m = data.comparison_matrix;
    const ths = m.headers.map(h => `<th>${h}</th>`).join('');
    const trs = m.rows.map(r => `<tr>${r.map(c => `<td>${c}</td>`).join('')}</tr>`).join('');

    comparisonHtml = `
      <div class="comparison-card">
        <div class="comparison-title">${m.title || 'Key Differences'}</div>
        <div class="table-responsive">
          <table class="styled-table">
            <thead><tr>${ths}</tr></thead>
            <tbody>${trs}</tbody>
          </table>
        </div>
      </div>
    `;
  }

  // TAB 1: EXAM POINTS & COMMON ERRORS
  let examPointsHtml = '';
  if (Array.isArray(data.exam_points) && data.exam_points.length > 0) {
    examPointsHtml = `
      <div class="exam-points-card">
        <div class="exam-points-title">🎯 Key Exam Points</div>
        <ul class="exam-points-list">
          ${data.exam_points.map(p => `<li>${p}</li>`).join('')}
        </ul>
      </div>
    `;
  }

  let pitfallsHtml = '';
  const pitfallsList = data.common_pitfalls || data.common_errors;
  if (Array.isArray(pitfallsList) && pitfallsList.length > 0) {
    pitfallsHtml = `
      <div class="common-errors-card">
        <div class="common-errors-title">🚫 Common Errors & Confusions</div>
        <ul class="common-errors-list">
          ${pitfallsList.map(e => `<li>${e}</li>`).join('')}
        </ul>
      </div>
    `;
  }

  // TAB 2: REVISION SUMMARY & GLOSSARY
  let summaryConceptsHtml = '';
  if (Array.isArray(data.chapter_summary_concepts) && data.chapter_summary_concepts.length > 0) {
    summaryConceptsHtml = data.chapter_summary_concepts.map(c => `
      <div class="summary-concept-card">
        <div class="summary-concept-header">
          <h3 class="summary-concept-title">${c.concept_title}</h3>
        </div>
        <div class="summary-concept-body prose-content">
          ${c.concept_body_html}
        </div>
      </div>
    `).join('');
  }

  const qr = data.quick_revision || {};
  let glossaryHtml = '';
  if (Array.isArray(qr.terms_glossary) && qr.terms_glossary.length > 0) {
    glossaryHtml = qr.terms_glossary.map(t => `
      <div class="glossary-item">
        <div class="glossary-term-wrap">
          <span class="glossary-term">${t.term}</span>
          ${t.term_en ? `<span class="glossary-term-en">(${t.term_en})</span>` : ''}
        </div>
        <div class="glossary-def">${t.definition}</div>
      </div>
    `).join('');
  }

  let mustRememberHtml = '';
  if (Array.isArray(qr.must_remember) && qr.must_remember.length > 0) {
    mustRememberHtml = qr.must_remember.map(item => `<li>${item}</li>`).join('');
  }

  let recapBulletsHtml = '';
  if (Array.isArray(qr.summary) && qr.summary.length > 0) {
    recapBulletsHtml = qr.summary.map(item => `<li>${item}</li>`).join('');
  }

  let confusionsHtml = '';
  if (Array.isArray(qr.common_confusions) && qr.common_confusions.length > 0) {
    confusionsHtml = qr.common_confusions.map(cf => `
      <div class="confusion-item">
        <div class="confusion-terms">
          <span class="conf-badge-a">${cf.term_a}</span>
          <span class="conf-vs">VS</span>
          <span class="conf-badge-b">${cf.term_b}</span>
        </div>
        <p class="confusion-diff">${cf.difference}</p>
      </div>
    `).join('');
  }

  // TAB 3: PRACTICE QUIZ (18-20 MCQs)
  const letters = ['A', 'B', 'C', 'D'];
  let quizCardsHtml = '';
  (data.quiz || []).forEach((q, idx) => {
    const optsList = Array.isArray(q.options) && q.options.length === 4 ? q.options : ['Option A', 'Option B', 'Option C', 'Option D'];
    let opts = optsList.map((opt, oIdx) => `
      <button type="button" class="quiz-option-btn" data-qindex="${idx}" data-optindex="${oIdx}">
        <span class="option-letter">${letters[oIdx]}</span>
        <span class="option-text">${opt}</span>
      </button>
    `).join('');

    quizCardsHtml += `
      <div class="quiz-question-card" id="q-card-${idx}" data-correct="${q.correct_index ?? 0}">
        <div class="q-header">
          <span class="q-number">Question ${idx + 1} of ${data.quiz.length}</span>
        </div>
        <h3 class="q-text">${q.question || 'Practice Question'}</h3>
        <div class="quiz-options-group">${opts}</div>
        <div class="q-feedback hidden" id="feedback-${idx}">
          <div class="feedback-indicator"></div>
          <p class="feedback-explanation"><strong>Explanation:</strong> ${q.explanation || 'See solution above.'}</p>
        </div>
      </div>
    `;
  });

  // TAB 4: PREVIOUS YEARS QUESTIONS (PYQs & Exam Trends)
  let pyqCardsHtml = '';
  const pyqList = Array.isArray(data.pyq_patterns) && data.pyq_patterns.length > 0
    ? data.pyq_patterns
    : (data.quiz || []).slice(0, 6);

  pyqList.forEach((q, idx) => {
    const optsList = Array.isArray(q.options) && q.options.length === 4 ? q.options : ['Option A', 'Option B', 'Option C', 'Option D'];
    let opts = optsList.map((opt, oIdx) => `
      <button type="button" class="quiz-option-btn" data-pyqindex="${idx}" data-optindex="${oIdx}">
        <span class="option-letter">${letters[oIdx]}</span>
        <span class="option-text">${opt}</span>
      </button>
    `).join('');

    const correctIdx = (typeof q.correct_index === 'number' && q.correct_index >= 0 && q.correct_index < 4) ? q.correct_index : 0;
    const correctOptText = optsList[correctIdx] || '';

    pyqCardsHtml += `
      <div class="pyq-card" id="pyq-card-${idx}" data-correct="${correctIdx}">
        <div class="pyq-header-meta">
          <span class="pyq-badge">${q.year_tag || 'UP PGT'}</span>
        </div>
        <div class="pyq-question-text">${q.question || 'PYQ Question'}</div>
        <div class="quiz-options-group">${opts}</div>
        <div class="pyq-expl-box hidden" id="pyq-expl-${idx}">
          <strong>Answer: Option ${letters[correctIdx]} (${correctOptText})</strong>
          <span>${q.explanation || ''}</span>
        </div>
      </div>
    `;
  });

  // TAB 5: TIMED TOPIC TEST (10 MCQs)
  let testCardsHtml = '';
  (data.topic_test || []).forEach((t, idx) => {
    const optsList = Array.isArray(t.options) && t.options.length === 4 ? t.options : ['Option A', 'Option B', 'Option C', 'Option D'];
    let opts = optsList.map((opt, oIdx) => `
      <button type="button" class="test-option-btn" data-tindex="${idx}" data-optindex="${oIdx}">
        <span class="option-letter">${letters[oIdx]}</span>
        <span class="option-text">${opt}</span>
      </button>
    `).join('');

    testCardsHtml += `
      <div class="test-question-card" id="t-card-${idx}" data-correct="${t.correct_index ?? 0}">
        <div class="test-q-header">
          <span class="t-badge">Question ${idx + 1} of ${(data.topic_test || []).length}</span>
        </div>
        <div class="test-question-text">${t.question || 'Test Question'}</div>
        <div class="test-options-grid">${opts}</div>
        <div class="t-feedback hidden" id="t-feedback-${idx}">
          <p class="feedback-explanation"><strong>Solution:</strong> ${t.explanation || 'See solution above.'}</p>
        </div>
      </div>
    `;
  });

  // Navigation Links
  const prevHtml = context.prevTopic
    ? `<a class="topic-nav-btn prev" href="${context.prevTopic.href}"><span>← Previous:</span> <strong>${context.prevTopic.rawText || context.prevTopic.title || 'Previous'}</strong></a>`
    : `<div class="topic-nav-btn disabled"><span>← Start of Branch</span></div>`;

  const nextHtml = context.nextTopic
    ? `<a class="topic-nav-btn next" href="${context.nextTopic.href}"><span>Next:</span> <strong>${context.nextTopic.rawText || context.nextTopic.title || 'Next'} →</strong></a>`
    : `<a class="topic-nav-btn next" href="/up-pgt-chemistry/"><span>Exam Tracker →</span> <strong>UP PGT Chemistry</strong></a>`;

  // Sidebar Links
  let relatedHtml = '';
  if (context.related && context.related.length > 0) {
    relatedHtml = context.related.map(r => `
      <a href="${r.url}">
        <span>${r.title}</span>
        <span>→</span>
      </a>
    `).join('');
  }

  return `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>${title}</title>
<meta name="description" content="${metaDesc}">
<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1">
<meta name="author" content="SJ Maths">
<meta name="theme-color" content="#1e3a8a">
<link rel="canonical" href="${canonicalUrl}">
<link rel="icon" type="image/png" href="/favicon.png">

<!-- OpenGraph Metadata -->
<meta property="og:type" content="article">
<meta property="og:site_name" content="SJ Maths">
<meta property="og:title" content="${cleanTitle} | Chemistry Notes & Test">
<meta property="og:description" content="${metaDesc}">
<meta property="og:url" content="${canonicalUrl}">

<!-- Twitter Card Metadata -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="${cleanTitle} | UP PGT Chemistry">
<meta name="twitter:description" content="${metaDesc}">

<!-- JSON-LD Structured Data -->
<script type="application/ld+json">
${JSON.stringify(schemaJsonLd, null, 2)}
</script>

<link rel="stylesheet" href="/assets/css/topic-page.css">
<style>
:root {
  --brand: #1e3a8a;
  --brand-dark: #0f172a;
  --brand-light: #2563eb;
  --accent: #2563eb;
  --accent-hover: #1d4ed8;
  --accent-soft: rgba(37, 99, 235, 0.08);
  --accent-border: rgba(37, 99, 235, 0.24);
}
html.dark, body.dark-mode {
  --brand: #93c5fd;
  --brand-dark: #bfdbfe;
  --brand-light: #60a5fa;
  --accent: #60a5fa;
  --accent-hover: #93c5fd;
  --accent-soft: rgba(96, 165, 250, 0.14);
  --accent-border: rgba(96, 165, 250, 0.35);
}
.desk-only { display: none; }
@media (min-width: 640px) {
  .desk-only { display: inline; }
}
</style>
</head>
<body>

<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="https://sjmaths.com/">
      <span class="brand-mark" style="background: linear-gradient(145deg, #1e3a8a, #2563eb); font-family: serif; font-size: 1.35rem; font-style: italic; display: flex; align-items: center; justify-content: center;">&int;</span>
      <span>
        <span class="brand-name">SJ Maths</span>
        <span class="brand-sub">Chemistry</span>
      </span>
    </a>
    <div class="header-actions">
      <button type="button" class="theme-toggle-btn" id="btn-theme-toggle" aria-label="Toggle Dark Mode">🌙 Dark Mode</button>
      <a class="back-btn" href="/up-pgt-chemistry/" title="UP PGT Chemistry Tracker">← UP PGT<span class="desk-only"> Chemistry</span></a>
    </div>
  </div>
</header>

<main class="wrap">
  <!-- Hero Section -->
  <section class="hero">
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="https://sjmaths.com/">Home</a>
      <span class="breadcrumb-sep">›</span>
      <a href="/chemistry/">Chemistry</a>
      <span class="breadcrumb-sep">›</span>
      <a href="/chemistry/${context.sectionKey}/">${context.sectionMeta.en}</a>
      <span class="breadcrumb-sep">›</span>
      <span aria-current="page">${cleanTitle}</span>
    </nav>
    <div class="kicker" style="color: #2563eb; font-weight: 800;">${context.sectionMeta.en}</div>
    <h1>${cleanTitle}</h1>
    <p class="lead">${data.short_intro}</p>

    <div class="exam-badges">
      ${examBadgesHtml}
    </div>
  </section>

  <!-- Interactive Learning Navigation Tabs (5 Tabs) -->
  <div class="study-tabs-sticky-wrapper">
    <div class="study-tabs" role="tablist" aria-label="Study Module Tabs">
      <button type="button" class="tab-btn active" role="tab" aria-selected="true" data-tab="tab-notes" id="tab-btn-notes">
        <span>📖</span> <span>Study Notes</span>
      </button>
      <button type="button" class="tab-btn" role="tab" aria-selected="false" data-tab="tab-summary" id="tab-btn-summary">
        <span>⚡</span> <span>Revision Summary</span>
      </button>
      <button type="button" class="tab-btn" role="tab" aria-selected="false" data-tab="tab-quiz" id="tab-btn-quiz">
        <span>❓</span> <span>Practice Quiz</span> <span class="tab-badge">${data.quiz.length}Q</span>
      </button>
      <button type="button" class="tab-btn" role="tab" aria-selected="false" data-tab="tab-pyqs" id="tab-btn-pyqs">
        <span>🏛️</span> <span>PYQs & Trends</span>
      </button>
      <button type="button" class="tab-btn" role="tab" aria-selected="false" data-tab="tab-test" id="tab-btn-test">
        <span>⏱️</span> <span>Topic Test</span> <span class="tab-badge">${data.topic_test.length}Q</span>
      </button>
    </div>
  </div>

  <!-- Tab Panels & Main Grid Layout -->
  <div class="main-grid">
    <div class="content-col">

      <!-- TAB 1: CONCISE EXAM-RELEVANT NOTES & CHEAT SHEET -->
      <article class="tab-panel active" id="tab-notes" role="tabpanel" aria-labelledby="tab-btn-notes">
        ${bulletNotesHtml}
        ${formulaSheetHtml}
        ${exceptionsHtml}
        ${tricksHtml}
        ${comparisonHtml}
        ${examPointsHtml}
        ${pitfallsHtml}
      </article>

      <!-- TAB 2: REVISION SUMMARY & FLASHCARDS -->
      <article class="tab-panel hidden" id="tab-summary" role="tabpanel" aria-labelledby="tab-btn-summary">
        <div class="summary-container">
          <div class="summary-hero-box" style="background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%);">
            <h2>⚡ Quick Revision: ${cleanTitle}</h2>
            <p>Core formulas, rapid recall points, and distinguishing criteria at a glance.</p>
          </div>
          ${summaryConceptsHtml}
        </div>

        <div class="revision-container" style="margin-top: 24px;">
          <div class="revision-card-box">
            <h2>📚 Terms & Units Glossary</h2>
            <div class="glossary-grid">
              ${glossaryHtml}
            </div>
          </div>

          ${mustRememberHtml ? `
          <div class="revision-card-box highlight">
            <h2>🎯 Key Takeaways</h2>
            <ul class="must-remember-list">
              ${mustRememberHtml}
            </ul>
          </div>` : ''}

          ${recapBulletsHtml ? `
          <div class="revision-card-box">
            <h2>📌 Quick Recall</h2>
            <ul class="recap-list">
              ${recapBulletsHtml}
            </ul>
          </div>` : ''}

          ${confusionsHtml ? `
          <div class="revision-card-box diff">
            <h2>⚖️ Key Differences</h2>
            <div class="confusions-grid">
              ${confusionsHtml}
            </div>
          </div>` : ''}
        </div>
      </article>

      <!-- TAB 3: PRACTICE QUIZ (18-20 MCQs) -->
      <article class="tab-panel hidden" id="tab-quiz" role="tabpanel" aria-labelledby="tab-btn-quiz">
        <div class="quiz-panel-header">
          <div class="quiz-panel-title">
            <h2>❓ Practice Questions (${data.quiz.length} MCQs)</h2>
            <p>Select an option to test your understanding with instant verification and explanations.</p>
          </div>
          <div class="quiz-live-scoreboard">
            <div class="score-pill">Score: <span id="quizScore">0</span> / ${data.quiz.length}</div>
            <button type="button" class="btn-reset-quiz" id="btnResetQuiz">Restart Quiz</button>
          </div>
        </div>

        <div class="quiz-questions-list">
          ${quizCardsHtml}
        </div>
      </article>

      <!-- TAB 4: PREVIOUS YEARS QUESTIONS (PYQs & Exam Trends) -->
      <article class="tab-panel hidden" id="tab-pyqs" role="tabpanel" aria-labelledby="tab-btn-pyqs">
        <div class="pyq-trend-card">
          <h2>🏛️ Exam Trends & Question Pattern</h2>
          <p>Historical question weightage and patterns for <strong>${cleanTitle}</strong> in UP PGT Chemistry.</p>
          <div class="pyq-trend-grid">
            <div class="pyq-stat-item">
              <span class="pyq-stat-val">2–4</span>
              <span class="pyq-stat-label">Expected Questions</span>
            </div>
            <div class="pyq-stat-item">
              <span class="pyq-stat-val">8–12%</span>
              <span class="pyq-stat-label">Topic Weightage</span>
            </div>
            <div class="pyq-stat-item">
              <span class="pyq-stat-val">Medium</span>
              <span class="pyq-stat-label">Difficulty</span>
            </div>
          </div>
        </div>

        <div class="pyq-questions-list">
          ${pyqCardsHtml}
        </div>
      </article>

      <!-- TAB 5: TIMED TOPIC TEST (10 MCQs / 10 Minutes) -->
      <article class="tab-panel hidden" id="tab-test" role="tabpanel" aria-labelledby="tab-btn-test">
        <div class="test-panel-header">
          <div>
            <h2>⏱️ Timed Topic Test</h2>
            <p>10 questions &bull; 10 minutes &bull; Timed practice</p>
          </div>
          <div class="test-timer-badge" id="testTimerBadge">
            <span class="timer-icon">⏳</span> <span id="timerDisplay">10:00</span>
          </div>
        </div>

        <div class="test-instruction-box" id="testStartWrap">
          <h3>Instructions</h3>
          <ul>
            <li><strong>Questions:</strong> 10 MCQs</li>
            <li><strong>Time Allowed:</strong> 10 Minutes</li>
            <li><strong>Marking:</strong> +1 mark for correct, 0 for unattempted or wrong</li>
          </ul>
          <button type="button" class="btn-start-test" id="btnStartTest" style="background: linear-gradient(135deg, #1e3a8a, #2563eb);">Start Test</button>
        </div>

        <div class="test-active-container hidden" id="testActiveWrap">
          <div class="test-questions-list">
            ${testCardsHtml}
          </div>
          <div class="test-submit-bar">
            <button type="button" class="btn-submit-test" id="btnSubmitTest" style="background: #2563eb;">Submit Test</button>
          </div>
        </div>

        <div class="test-result-modal hidden" id="testResultModal">
          <div class="result-card">
            <h3>Test Result</h3>
            <div class="result-score-circle" style="background: linear-gradient(135deg, #1e3a8a, #2563eb);">
              <span id="resFinalScore">0</span> / 10
            </div>
            <p id="resFeedbackText">Review detailed solutions above for all questions.</p>
            <button type="button" class="btn-retake-test" id="btnRetakeTest" style="background: #2563eb;">Retake Test</button>
          </div>
        </div>
      </article>

      <!-- Bottom Prev / Next Navigation -->
      <nav class="topic-pagination" aria-label="Topic Navigation">
        ${prevHtml}
        ${nextHtml}
      </nav>

    </div>

    <!-- Sticky Sidebar -->
    <aside class="sidebar-col">
      <div class="sidebar-card side-card">
        <div class="side-card-header">
          <span class="side-badge">Syllabus Section</span>
          <h3>${context.sectionMeta.en}</h3>
        </div>
        <p class="side-desc">Branch topics covered under official UP PGT Chemistry curriculum.</p>
        <div class="side-nav-links">
          ${relatedHtml}
        </div>
        <div class="side-action-box">
          <a class="side-action-btn" href="/up-pgt-chemistry/" style="background: #1e3a8a;">Full Chemistry Tracker →</a>
        </div>
      </div>
    </aside>
  </div>
</main>

<footer class="site-footer">
  <div class="wrap footer-inner">
    <div>
      <p><strong>SJ Maths — Chemistry</strong></p>
      <p>Study notes and test prep for UP PGT Chemistry (Subject Code 02).</p>
    </div>
    <div class="footer-links">
      <a href="https://sjmaths.com/">Home</a>
      <a href="/up-pgt-chemistry/">UP PGT Chemistry</a>
      <a href="/privacy-policy/">Privacy Policy</a>
    </div>
  </div>
</footer>

<script>
document.addEventListener('DOMContentLoaded', () => {
  // Dual-Class Theme Toggle
  const themeToggleBtn = document.getElementById('btn-theme-toggle');
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  const savedTheme = localStorage.getItem('sjmaths_theme') || localStorage.getItem('sj_theme');
  if (savedTheme === 'dark' || (!savedTheme && prefersDark)) {
    document.body.classList.add('dark-mode');
    document.documentElement.classList.add('dark');
    if (themeToggleBtn) themeToggleBtn.textContent = '☀️ Light Mode';
  }
  if (themeToggleBtn) {
    themeToggleBtn.addEventListener('click', () => {
      const isDark = document.body.classList.toggle('dark-mode');
      document.documentElement.classList.toggle('dark', isDark);
      localStorage.setItem('sjmaths_theme', isDark ? 'dark' : 'light');
      localStorage.setItem('sj_theme', isDark ? 'dark' : 'light');
      themeToggleBtn.textContent = isDark ? '☀️ Light Mode' : '🌙 Dark Mode';
    });
  }

  // 5-Tab Switching Logic
  const tabBtns = document.querySelectorAll('.tab-btn');
  const tabPanels = document.querySelectorAll('.tab-panel');

  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const targetTab = btn.getAttribute('data-tab');
      tabBtns.forEach(b => {
        b.classList.remove('active');
        b.setAttribute('aria-selected', 'false');
      });
      tabPanels.forEach(p => {
        p.classList.remove('active');
        p.classList.add('hidden');
      });

      btn.classList.add('active');
      btn.setAttribute('aria-selected', 'true');
      const activePanel = document.getElementById(targetTab);
      if (activePanel) {
        activePanel.classList.remove('hidden');
        activePanel.classList.add('active');
      }
      const stickyWrap = document.querySelector('.study-tabs-sticky-wrapper');
      if (stickyWrap) {
        window.scrollTo({ top: stickyWrap.offsetTop - 15, behavior: 'smooth' });
      }
    });
  });

  // Practice Quiz Logic
  let quizScore = 0;
  const answeredQuestions = new Set();
  const quizOptionBtns = document.querySelectorAll('.quiz-option-btn');

  quizOptionBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const qIndex = parseInt(btn.getAttribute('data-qindex'), 10);
      const optIndex = parseInt(btn.getAttribute('data-optindex'), 10);
      const isPyq = btn.hasAttribute('data-pyqindex');
      
      if (isPyq) {
        const pyqIdx = parseInt(btn.getAttribute('data-pyqindex'), 10);
        const card = document.getElementById('pyq-card-' + pyqIdx);
        const correct = parseInt(card.getAttribute('data-correct'), 10);
        const expl = document.getElementById('pyq-expl-' + pyqIdx);
        card.querySelectorAll('.quiz-option-btn').forEach((b, idx) => {
          b.disabled = true;
          if (idx === correct) b.classList.add('correct');
          else if (idx === optIndex && optIndex !== correct) b.classList.add('incorrect');
        });
        if (expl) expl.classList.remove('hidden');
        return;
      }

      const card = document.getElementById('q-card-' + qIndex);
      if (!card) return;
      const correctIndex = parseInt(card.getAttribute('data-correct'), 10);
      const feedback = document.getElementById('feedback-' + qIndex);
      const statusEl = feedback ? feedback.querySelector('.feedback-indicator') : null;

      if (answeredQuestions.has(qIndex)) return;
      answeredQuestions.add(qIndex);

      const allBtns = card.querySelectorAll('.quiz-option-btn');
      allBtns.forEach((b, idx) => {
        b.disabled = true;
        if (idx === correctIndex) b.classList.add('correct');
        else if (idx === optIndex && optIndex !== correctIndex) b.classList.add('incorrect');
      });

      const letters = ['A', 'B', 'C', 'D'];
      if (optIndex === correctIndex) {
        quizScore++;
        if (statusEl) {
          statusEl.textContent = '✓ Correct Answer!';
          statusEl.className = 'feedback-indicator correct';
        }
        if (feedback) feedback.className = 'q-feedback correct';
      } else {
        if (statusEl) {
          statusEl.textContent = '✗ Incorrect. Correct Option: ' + letters[correctIndex];
          statusEl.className = 'feedback-indicator incorrect';
        }
        if (feedback) feedback.className = 'q-feedback incorrect';
      }
      if (feedback) feedback.classList.remove('hidden');
      const scoreEl = document.getElementById('quizScore');
      if (scoreEl) scoreEl.textContent = quizScore;
    });
  });

  const btnResetQuiz = document.getElementById('btnResetQuiz');
  if (btnResetQuiz) {
    btnResetQuiz.addEventListener('click', () => {
      quizScore = 0;
      answeredQuestions.clear();
      const scoreEl = document.getElementById('quizScore');
      if (scoreEl) scoreEl.textContent = '0';
      document.querySelectorAll('.quiz-option-btn').forEach(b => {
        b.disabled = false;
        b.classList.remove('correct', 'incorrect');
      });
      document.querySelectorAll('.q-feedback').forEach(f => {
        f.classList.add('hidden');
        f.classList.remove('correct', 'incorrect');
      });
    });
  }

  // Timed Topic Test Logic
  let testTimer = null;
  let secondsLeft = 600;
  const btnStartTest = document.getElementById('btnStartTest');
  const testStartWrap = document.getElementById('testStartWrap');
  const testActiveWrap = document.getElementById('testActiveWrap');
  const timerDisplay = document.getElementById('timerDisplay');

  if (btnStartTest) {
    btnStartTest.addEventListener('click', () => {
      if (testStartWrap) testStartWrap.classList.add('hidden');
      if (testActiveWrap) testActiveWrap.classList.remove('hidden');
      testTimer = setInterval(() => {
        secondsLeft--;
        const mins = Math.floor(secondsLeft / 60);
        const secs = secondsLeft % 60;
        if (timerDisplay) {
          timerDisplay.textContent = (mins < 10 ? '0' : '') + mins + ':' + (secs < 10 ? '0' : '') + secs;
        }
        if (secondsLeft <= 0) {
          clearInterval(testTimer);
          submitTest();
        }
      }, 1000);
    });
  }

  const selectedTestAnswers = {};
  document.querySelectorAll('.test-option-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const tIndex = parseInt(btn.getAttribute('data-tindex'), 10);
      const optIndex = parseInt(btn.getAttribute('data-optindex'), 10);
      selectedTestAnswers[tIndex] = optIndex;
      const card = document.getElementById('t-card-' + tIndex);
      if (card) {
        card.querySelectorAll('.test-option-btn').forEach(b => b.classList.remove('selected'));
      }
      btn.classList.add('selected');
    });
  });

  function submitTest() {
    if (testTimer) clearInterval(testTimer);
    let score = 0;
    const testCards = document.querySelectorAll('.test-question-card');
    testCards.forEach((card, idx) => {
      const correct = parseInt(card.getAttribute('data-correct'), 10);
      const userAns = selectedTestAnswers[idx];
      const feedback = document.getElementById('t-feedback-' + idx);
      const btns = card.querySelectorAll('.test-option-btn');
      btns.forEach((b, oIdx) => {
        b.disabled = true;
        if (oIdx === correct) b.classList.add('correct');
        else if (oIdx === userAns && userAns !== correct) b.classList.add('incorrect');
      });
      if (userAns === correct) score++;
      if (feedback) feedback.classList.remove('hidden');
    });
    const resScore = document.getElementById('resFinalScore');
    if (resScore) resScore.textContent = score;
    const resModal = document.getElementById('testResultModal');
    if (resModal) resModal.classList.remove('hidden');
    const btnSub = document.getElementById('btnSubmitTest');
    if (btnSub) btnSub.classList.add('hidden');
  }

  const btnSubmitTest = document.getElementById('btnSubmitTest');
  if (btnSubmitTest) btnSubmitTest.addEventListener('click', submitTest);

  const btnRetakeTest = document.getElementById('btnRetakeTest');
  if (btnRetakeTest) {
    btnRetakeTest.addEventListener('click', () => {
      location.reload();
    });
  }
});
</script>
</body>
</html>
`;
}

/**
 * Process single topic through rotating Gemini models
 */
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
