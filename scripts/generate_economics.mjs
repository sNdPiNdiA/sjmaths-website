#!/usr/bin/env node
/**
 * ============================================================================
 * SJ Maths — Economics Content Generator Pipeline
 * Target: UP PGT Economics (Subject Code 11), UP TGT Social Science & UGC-NET
 * 5 Modular Tabs:
 *   1. 📖 Theoretical Notes (Theorists, Assumptions, Pillars, Formulations, Paradoxes)
 *   2. ⚡ Revision Summary (Glossary, Must-Remember Laws, Confusions, Policy Matrix)
 *   3. ❓ Practice Quiz (18-20 Interactive MCQs with Live Feedback)
 *   4. 🏛️ Previous Years Questions (PYQs & Exam Trends)
 *   5. ⏱️ Timed Topic Test (10-Minute Countdown Test & Scoring)
 *
 * Multi-API key rotation & model fallback supported
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
const GAP_MS = getArg('--gap') ? parseInt(getArg('--gap'), 10) * 1000 : 10000; // 10s default gap

const MODELS = [
  'gemini-3.5-flash-lite'
];
const CALLS_PER_MODEL = 20;
let currentModelIndex = 0;
let currentModelCalls = 0;

const modelCallCounts = {
  'gemini-3.5-flash-lite': 0
};

// Status Tracking File
const STATUS_FILE = 'content-generation-status-economics.json';
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

// Load Inventory
const INVENTORY_FILE = 'scratch/economics_inventory.json';
if (!fs.existsSync(INVENTORY_FILE)) {
  console.error(`Inventory file not found at ${INVENTORY_FILE}. Run script to generate inventory first.`);
  process.exit(1);
}
const inventory = JSON.parse(fs.readFileSync(INVENTORY_FILE, 'utf8'));

// Section Titles
const SECTION_NAMES = {
  'micro-economics': 'Micro Economics',
  'macro-economics': 'Macro Economics',
  'money-and-banking': 'Money and Banking',
  'public-finance': 'Public Finance',
  'international-trade': 'International Trade',
  'indian-economy': 'Indian Economy',
  'growth-and-development': 'Growth and Development',
  'elementary-statistics': 'Elementary Statistics',
  'economic-systems': 'Economic Systems',
  'economic-theory': 'Economic Theory',
  'population-theory': 'Population Theory'
};

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

function getTopicContext(item) {
  const parts = item.url.split('/').filter(Boolean);
  const sectionKey = parts[1] || 'general';
  const sectionTitle = SECTION_NAMES[sectionKey] || sectionKey.replace(/-/g, ' ').replace(/\b\w/g, c => c.toUpperCase());
  return {
    sectionKey,
    sectionTitle,
    topicSlug: parts[parts.length - 1],
    title: item.title
  };
}

function buildPromptStudyNotes(item, context) {
  return `You are an elite Professor of Economics and Senior Exam Specialist for competitive examinations (UP PGT Economics Subject Code 11, UP TGT Social Science, UGC-NET, and State Assistant Professor).

Generate the AUTHORITATIVE THEORETICAL STUDY NOTES (Part 1 of 2) for the following syllabus topic:

TOPIC: "${item.title}"
CANONICAL URL: "${item.url}"
AREA / BRANCH: "${context.sectionTitle}"

CRITICAL PEDAGOGICAL REQUIREMENTS FOR STUDY NOTES:
1. EXHAUSTIVE SUBTOPIC COVERAGE: The syllabus title contains multiple distinct concepts separated by colons/commas (e.g. "Indifference Curve Analysis: Consumer Equilibrium, Price, Income, and Substitution Effects"). You MUST provide exhaustive coverage for EVERY subtopic and concept named in the title so NO concept is missed. Provide 4 to 6 comprehensive conceptual pillars covering all nuances.
2. ECONOMISTS, PUBLICATIONS & CHRONOLOGY: Focus heavily on pioneering economists, publication years, landmark books/treatises (e.g., Adam Smith 1776, Ricardo 1817, Marshall 1890, Keynes 1936, Hicks & Allen 1934, Samuelson 1947, Schumpeter, Nurkse, etc.).
3. UNDERLYING ASSUMPTIONS: State 5 to 7 vital ceteris paribus assumptions (rationality, transitivity, diminishing MRS, convexity, homogeneous factors, closed economy, etc.) with brief economic rationale.
4. MATHEMATICAL & ELASTICITY FORMULAS: Provide 4 to 6 exact equilibrium conditions (e.g. MR = MC, MRS_{xy} = P_x / P_y), mathematical equations, derivatives, and elasticities. Use clean mathematical notation compatible with visual rendering (e.g. MRS_{xy} = - \\frac{dY}{dX} = \\frac{MU_x}{MU_y}, or Slutsky decomposition \\frac{\\partial X}{\\partial P_x} = \\frac{\\partial X^h}{\\partial P_x} - X \\frac{\\partial X}{\\partial M}).
5. ECONOMIC PARADOXES & BOUNDARY CASES: Detail 3 to 5 key paradoxes, boundary conditions, and exceptions (e.g. Giffen goods, corner solutions, backward-bending labor supply, liquidity trap, Leontief paradox, stagflation, neutral goods).
6. COMPARISON MATRIX: Include a detailed comparative matrix with 4 to 6 dimensions comparing competing doctrines/methods/goods (e.g. Cardinal vs Ordinal Utility, Hicksian vs Slutsky Decomposition, or Classical vs Keynesian).
7. TIPS, TRICKS, SHORTCUTS & MNEMONICS: Provide 4 to 6 high-yield exam shortcuts, memory acronyms/mnemonics, rule-of-thumb tricks, and fast calculation shortcuts specifically designed for UP PGT & UGC NET aspirants.

OUTPUT MUST BE A SINGLE, VALID, PARSABLE JSON OBJECT WITH NO SURROUNDING MARKDOWN OR COMMENTS:

{
  "title": "${item.title}",
  "short_intro": "2-3 sentences concise summary defining the topic, its importance in economic theory, and relevance in teacher recruitment exams.",
  
  "theorists_and_origins": [
    {
      "theorist": "Name of Economist",
      "year_or_treatise": "Year & famous book/treatise title",
      "contribution": "Specific doctrine, law, formulation, or analytical tool introduced"
    }
  ],

  "core_assumptions": [
    "Assumption 1 with economic rationale",
    "Assumption 2 with economic rationale",
    "Assumption 3 with economic rationale",
    "Assumption 4 with economic rationale",
    "Assumption 5 with economic rationale"
  ],

  "conceptual_pillars": [
    {
      "pillar_title": "1. First Major Subtopic / Dimension from Title",
      "explanation": "Thorough, authoritative explanation of theoretical mechanisms, diagrams, slopes, and behavior.",
      "exam_takeaways": [
        "High-yield factual exam point 1",
        "High-yield factual exam point 2",
        "High-yield factual exam point 3"
      ]
    },
    {
      "pillar_title": "2. Second Major Subtopic / Dimension from Title",
      "explanation": "Detailed explanation of curves, equilibrium conditions, and shifts.",
      "exam_takeaways": [
        "High-yield factual exam point 1",
        "High-yield factual exam point 2",
        "High-yield factual exam point 3"
      ]
    },
    {
      "pillar_title": "3. Third Major Subtopic / Dimension from Title",
      "explanation": "Comprehensive theoretical analysis and institutional context.",
      "exam_takeaways": [
        "High-yield factual exam point 1",
        "High-yield factual exam point 2",
        "High-yield factual exam point 3"
      ]
    },
    {
      "pillar_title": "4. Fourth Major Subtopic / Dimension from Title",
      "explanation": "Advanced analytical mechanisms, decomposition, or policy implications.",
      "exam_takeaways": [
        "High-yield factual exam point 1",
        "High-yield factual exam point 2",
        "High-yield factual exam point 3"
      ]
    }
  ],

  "mathematical_formulations": [
    {
      "concept": "Name of Formula / Equilibrium Condition",
      "equation": "Mathematical formula (e.g. MRS_{xy} = \\frac{MU_x}{MU_y} = \\frac{P_x}{P_y})",
      "economic_significance": "What the formula measures, conditions of validity, and interpretation of parameters"
    }
  ],

  "economic_paradoxes_and_exceptions": [
    {
      "name": "Name of Paradox or Exception (e.g. Giffen Paradox, Corner Solution)",
      "condition": "Underlying conditions under which normal economic laws fail or produce counter-intuitive results",
      "diagrammatic_behavior": "How the curve behaves graphically (e.g. upward sloping, horizontal, L-shaped, touches axes)"
    }
  ],

  "comparison_matrix": {
    "title": "Title of Matrix (e.g. Hicksian vs Slutsky Decomposition)",
    "headers": ["Dimension / Parameter", "Approach A", "Approach B"],
    "rows": [
      ["Dimension 1", "State A", "State B"],
      ["Dimension 2", "State A", "State B"],
      ["Dimension 3", "State A", "State B"],
      ["Dimension 4", "State A", "State B"]
    ]
  },

  "tips_and_mnemonics": [
    {
      "title": "Title of Shortcut / Trick / Rule",
      "mnemonic_or_tag": "Acronym / Memory Keyword (e.g. COMP-SUB, SE-IE-PE)",
      "shortcut_rule": "The exact quick-solving rule or formula shortcut to remember in exam hall",
      "exam_application": "How to apply this instantly to solve tricky UP PGT / NET exam questions in 10 seconds"
    }
  ]
}

REQUIRED COUNTS:
- 'theorists_and_origins': 4 to 6 landmark theorists with treatises/dates.
- 'core_assumptions': 5 to 7 assumptions.
- 'conceptual_pillars': 4 to 6 comprehensive pillars covering EVERY subtopic in the title.
- 'mathematical_formulations': 4 to 6 exact equations/formulas.
- 'economic_paradoxes_and_exceptions': 3 to 5 exceptions/paradoxes.
- 'tips_and_mnemonics': 4 to 6 tips, tricks, shortcuts, or mnemonics.
`;
}

function buildPromptRevisionAndTesting(item, context, studyNotesData) {
  const pillarsList = (studyNotesData.conceptual_pillars || []).map(p => p.pillar_title).join(', ');
  return `You are an elite Professor of Economics and Senior Exam Specialist for competitive examinations (UP PGT Economics Subject Code 11, UP TGT Social Science, UGC-NET, and State Assistant Professor).

Generate the EXHAUSTIVE QUICK REVISION, PRACTICE QUIZ, PYQs, AND TOPIC TEST (Part 2 of 2) for the following syllabus topic:

TOPIC: "${item.title}"
CANONICAL URL: "${item.url}"
AREA / BRANCH: "${context.sectionTitle}"
COVERED CONCEPTUAL PILLARS IN NOTES: "${pillarsList}"

CRITICAL REQUIREMENTS FOR REVISION & TESTING:
1. QUICK REVISION MUST INCLUDE EVERY SINGLE CONCEPT:
   - Exhaustive Terms Glossary: Include 12 to 18 definitions covering EVERY concept, variable, curve, law, and effect in this topic without omitting anything.
   - Must-Remember Laws & Identities: 6 to 8 crucial mathematical identities, equilibrium rules, or economic laws frequently tested in exams.
   - Common Analytical Confusions Contrast Table: 4 to 6 confusing pairs (e.g. Change in Demand vs Change in Quantity Demanded, Hicks Substitution vs Slutsky Substitution, Normal Good vs Inferior Good vs Giffen Good) clearly disambiguated.
2. PRACTICE QUIZ: Exactly 18 to 20 high-quality multiple choice questions (MCQs) spanning conceptual, mathematical, assertion-reason, and matching types with detailed step-by-step explanations.
3. PREVIOUS YEAR QUESTIONS (PYQs): Exactly 5 to 6 realistic PYQ pattern questions based on UP PGT Economics and UGC NET exam trends with complete step-by-step solutions.
4. TIMED TOPIC TEST: Exactly 10 rigorous test MCQs suitable for a 10-minute countdown challenge with comprehensive derivations or rationales.

OUTPUT MUST BE A SINGLE, VALID, PARSABLE JSON OBJECT WITH NO SURROUNDING MARKDOWN OR COMMENTS:

{
  "quick_revision": {
    "terms_glossary": [
      { "term": "Economic Concept / Term 1", "definition": "Crisp, precise textbook definition covering its mechanism and significance" }
    ],
    "must_remember_laws": [
      "Crucial economic rule, formula condition, or identity 1",
      "Crucial economic rule, formula condition, or identity 2",
      "Crucial economic rule, formula condition, or identity 3"
    ],
    "common_confusions": [
      {
        "concept_a": "First Confusing Term / Concept",
        "concept_b": "Second Confusing Term / Concept",
        "difference": "Crisp distinction highlighting differences in assumptions, slopes, shifts vs movements, or real income definitions"
      }
    ]
  },

  "quiz": [
    {
      "question": "Question text testing deep conceptual or mathematical understanding?",
      "options": ["Option A text", "Option B text", "Option C text", "Option D text"],
      "correct_index": 0,
      "explanation": "Detailed analytical explanation proving why option A is correct and why other options fail."
    }
  ],

  "pyq_patterns": [
    {
      "question": "Standard UP PGT / UGC NET pattern question?",
      "options": ["Option A", "Option B", "Option C", "Option D"],
      "correct_index": 1,
      "explanation": "Step-by-step solution referencing previous exam trends and theoretical proof."
    }
  ],

  "topic_test": [
    {
      "question": "Rigorous timed test question testing numerical, assertion-reason, or matching pairs?",
      "options": ["Option A", "Option B", "Option C", "Option D"],
      "correct_index": 2,
      "explanation": "Comprehensive derivation or conceptual justification."
    }
  ]
}

REQUIRED COUNTS:
- 'terms_glossary': 12 to 18 terms covering EVERY single sub-concept of the topic.
- 'must_remember_laws': 6 to 8 essential identities/laws.
- 'common_confusions': 4 to 6 contrast pairs.
- 'quiz': Exactly 18 to 20 practice questions.
- 'pyq_patterns': Exactly 5 to 6 questions.
- 'topic_test': Exactly 10 questions.
`;
}

function cleanRawJson(text) {
  let cleaned = text.trim();
  if (cleaned.startsWith('```json')) cleaned = cleaned.slice(7);
  else if (cleaned.startsWith('```')) cleaned = cleaned.slice(3);
  if (cleaned.endsWith('```')) cleaned = cleaned.slice(0, -3);
  return cleaned.trim();
}

function validateStudyNotes(data) {
  if (!data.title || typeof data.title !== 'string') throw new Error('Missing title');
  if (!data.short_intro || typeof data.short_intro !== 'string') throw new Error('Missing short_intro');
  if (!Array.isArray(data.conceptual_pillars) || data.conceptual_pillars.length < 3) {
    throw new Error(`Pillars insufficient: expected >=3, got ${data.conceptual_pillars ? data.conceptual_pillars.length : 0}`);
  }
}

function validateRevisionAndTesting(data) {
  if (!data.quick_revision || !Array.isArray(data.quick_revision.terms_glossary) || data.quick_revision.terms_glossary.length < 8) {
    throw new Error(`Terms glossary insufficient: expected >=8, got ${data.quick_revision?.terms_glossary?.length || 0}`);
  }
  if (!Array.isArray(data.quiz) || data.quiz.length < 15) {
    throw new Error(`Quiz array insufficient: expected >=15, got ${data.quiz ? data.quiz.length : 0}`);
  }
  if (!Array.isArray(data.topic_test) || data.topic_test.length < 8) {
    throw new Error(`Topic test array insufficient: expected >=8, got ${data.topic_test ? data.topic_test.length : 0}`);
  }
}

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
    if (!q.explanation) q.explanation = 'Direct application of governing economic principle.';
  });
}

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

function renderTopicHtml(item, context, data) {
  const canonicalUrl = `https://sjmaths.com${item.url}`;
  const title = `${data.title} — Economics Lecture Notes & Quiz | SJ Maths`;
  const metaDesc = `${data.title}: Core theories, mathematical formulas, theorists, shortcuts, paradoxes, PYQs, and interactive mock test for UP PGT Economics & TGT Social Science.`;

  // 1. THEORISTS & ORIGINS
  let theoristsHtml = '';
  if (Array.isArray(data.theorists_and_origins) && data.theorists_and_origins.length > 0) {
    const cards = data.theorists_and_origins.map(t => `
      <div class="theorist-card">
        <div class="theorist-name">${t.theorist}</div>
        <div class="theorist-year">${t.year_or_treatise}</div>
        <p class="theorist-desc">${t.contribution}</p>
      </div>
    `).join('');
    theoristsHtml = `
      <div class="card">
        <h2>🏛️ Key Economists &amp; Landmark Publications</h2>
        <div class="theorist-grid">${cards}</div>
      </div>
    `;
  }

  // 2. CORE ASSUMPTIONS
  let assumptionsHtml = '';
  if (Array.isArray(data.core_assumptions) && data.core_assumptions.length > 0) {
    assumptionsHtml = `
      <div class="card">
        <h2>⚖️ Fundamental Assumptions &amp; Hypotheses</h2>
        <ul class="assumptions-list">
          ${data.core_assumptions.map(a => `<li>${a}</li>`).join('')}
        </ul>
      </div>
    `;
  }

  // 3. CONCEPTUAL PILLARS
  let pillarsHtml = '';
  if (Array.isArray(data.conceptual_pillars) && data.conceptual_pillars.length > 0) {
    pillarsHtml = data.conceptual_pillars.map((p, idx) => `
      <section class="card" id="pillar-sec-${idx + 1}">
        <h2>${p.pillar_title}</h2>
        <div class="prose-content">
          <p>${p.explanation}</p>
          <div class="takeaways-box">
            <strong>Key Exam Takeaways:</strong>
            <ul>
              ${(p.exam_takeaways || []).map(t => `<li>${t}</li>`).join('')}
            </ul>
          </div>
        </div>
      </section>
    `).join('');
  }

  // 4. MATHEMATICAL FORMULATIONS & EQUILIBRIUM CONDITIONS
  function formatMathHtml(str) {
    if (!str) return '';
    let out = str;
    
    // Clean raw LaTeX formatting and dollar delimiters if generated
    out = out.replace(/\$/g, '')
             .replace(/\\left[.|(\[]/g, '')
             .replace(/\\right[.|)\]]/g, '')
             .replace(/\\quad/g, ' &nbsp; ')
             .replace(/\\implies/g, ' &rArr; ')
             .replace(/\\iff/g, ' &hArr; ')
             .replace(/\\min/g, 'min')
             .replace(/\\max/g, 'max')
             .replace(/\\text\{([^{}]+)\}/g, '$1');

    // Replace Greek and Math symbols
    const symbolMap = {
      '\\\\partial': '&part;',
      '\\\\Delta': '&Delta;',
      '\\\\lambda': '&lambda;',
      '\\\\mu': '&mu;',
      '\\\\pi': '&pi;',
      '\\\\sigma': '&sigma;',
      '\\\\alpha': '&alpha;',
      '\\\\beta': '&beta;',
      '\\\\infty': '&infin;',
      '\\\\approx': '&asymp;',
      '\\\\times': '&times;',
      '\\\\cdot': '&middot;',
      '\\\\rightarrow': '&rarr;',
      '\\\\le': '&le;',
      '\\\\ge': '&ge;',
      '\\\\neq': '&ne;'
    };
    for (const [pattern, rep] of Object.entries(symbolMap)) {
      out = out.replace(new RegExp(pattern, 'g'), rep);
    }

    // Convert \frac{A}{B} to visual fraction
    let changed = true;
    let safety = 0;
    while (changed && safety < 8) {
      changed = false;
      safety++;
      out = out.replace(/(?:&frac|\\frac)\{([^{}]+)\}\{([^{}]+)\}/g, (_, num, denom) => {
        changed = true;
        return `<span class="math-frac"><span class="math-num">${num}</span><span class="math-denom">${denom}</span></span>`;
      });
    }

    // Subscripts & Superscripts
    out = out.replace(/_\{([^{}]+)\}/g, '<span class="math-sub">$1</span>');
    out = out.replace(/_([a-zA-Z0-9]+)/g, '<span class="math-sub">$1</span>');
    out = out.replace(/\^\{([^{}]+)\}/g, '<span class="math-sup">$1</span>');
    out = out.replace(/\^([a-zA-Z0-9]+)/g, '<span class="math-sup">$1</span>');

    return out;
  }

  let formulasHtml = '';
  if (Array.isArray(data.mathematical_formulations) && data.mathematical_formulations.length > 0) {
    const cards = data.mathematical_formulations.map(f => `
      <div class="formula-card">
        <div class="formula-name">${f.concept}</div>
        <div class="formula-eq">${formatMathHtml(f.equation)}</div>
        <p class="formula-sig">${f.economic_significance}</p>
      </div>
    `).join('');
    formulasHtml = `
      <div class="card">
        <h2>📐 Mathematical Formulations &amp; Equilibrium Conditions</h2>
        <div class="formula-grid">${cards}</div>
      </div>
    `;
  }

  // 5. TIPS, TRICKS & MNEMONICS
  let tricksHtml = '';
  if (Array.isArray(data.tips_and_mnemonics) && data.tips_and_mnemonics.length > 0) {
    const cards = data.tips_and_mnemonics.map(t => `
      <div class="trick-card">
        <div class="trick-title">
          <span>💡 ${t.title}</span>
          ${t.mnemonic_or_tag ? `<span class="mnemonic-tag">${t.mnemonic_or_tag}</span>` : ''}
        </div>
        <div class="trick-shortcut">${t.shortcut_rule}</div>
        <p class="trick-app"><strong>Exam Application:</strong> ${t.exam_application}</p>
      </div>
    `).join('');
    tricksHtml = `
      <div class="card">
        <h2>🧠 Exam Tips, Tricks &amp; Mnemonics (10-Second Shortcuts)</h2>
        <div class="trick-grid">${cards}</div>
      </div>
    `;
  }

  // 6. PARADOXES & EXCEPTIONS
  let paradoxesHtml = '';
  if (Array.isArray(data.economic_paradoxes_and_exceptions) && data.economic_paradoxes_and_exceptions.length > 0) {
    const list = data.economic_paradoxes_and_exceptions.map(p => `
      <div class="paradox-card">
        <div class="paradox-head">
          <span class="badge badge-warn">Exception / Paradox</span>
          <strong>${p.name}</strong>
        </div>
        <p><strong>Conditions:</strong> ${p.condition}</p>
        <p><strong>Diagrammatic Behavior:</strong> <em>${p.diagrammatic_behavior}</em></p>
      </div>
    `).join('');
    paradoxesHtml = `
      <div class="card">
        <h2>⚠️ Economic Paradoxes &amp; Boundary Exceptions</h2>
        <div class="paradox-list">${list}</div>
      </div>
    `;
  }

  // 7. COMPARISON MATRIX
  let matrixHtml = '';
  if (data.comparison_matrix && Array.isArray(data.comparison_matrix.headers) && Array.isArray(data.comparison_matrix.rows)) {
    const ths = data.comparison_matrix.headers.map(h => `<th>${h}</th>`).join('');
    const trs = data.comparison_matrix.rows.map(row => `
      <tr>${row.map(c => `<td>${c}</td>`).join('')}</tr>
    `).join('');
    matrixHtml = `
      <div class="card">
        <h2>📊 ${data.comparison_matrix.title}</h2>
        <div class="table-wrap">
          <table class="matrix-table">
            <thead><tr>${ths}</tr></thead>
            <tbody>${trs}</tbody>
          </table>
        </div>
      </div>
    `;
  }

  // 8. GLOSSARY & CONFUSIONS (Quick Revision)
  const qr = data.quick_revision || {};
  let glossaryHtml = '';
  if (Array.isArray(qr.terms_glossary) && qr.terms_glossary.length > 0) {
    glossaryHtml = qr.terms_glossary.map(t => `
      <div class="glossary-item">
        <strong>${t.term}:</strong> <span>${t.definition}</span>
      </div>
    `).join('');
  }

  let confusionsHtml = '';
  if (Array.isArray(qr.common_confusions) && qr.common_confusions.length > 0) {
    confusionsHtml = qr.common_confusions.map(c => `
      <div class="confusion-card">
        <div class="conf-terms">
          <span class="conf-badge-a">${c.concept_a}</span>
          <span class="conf-vs">VS</span>
          <span class="conf-badge-b">${c.concept_b}</span>
        </div>
        <p>${c.difference}</p>
      </div>
    `).join('');
  }

  // 9. PRACTICE QUIZ (18-20 MCQs)
  const letters = ['A', 'B', 'C', 'D'];
  let quizCardsHtml = '';
  (data.quiz || []).forEach((q, idx) => {
    let opts = q.options.map((opt, oIdx) => `
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
        <h3 class="q-text">${q.question}</h3>
        <div class="quiz-options-group">${opts}</div>
        <div class="q-feedback hidden" id="feedback-${idx}">
          <p class="feedback-explanation"><strong>Explanation:</strong> ${q.explanation}</p>
        </div>
      </div>
    `;
  });

  // 10. PYQ PATTERNS
  let pyqCardsHtml = '';
  (data.pyq_patterns || []).forEach((q, idx) => {
    let opts = q.options.map((opt, oIdx) => `
      <div class="pyq-opt ${oIdx === q.correct_index ? 'correct-pyq-opt' : ''}">
        <strong>${letters[oIdx]}.</strong> ${opt}
      </div>
    `).join('');

    pyqCardsHtml += `
      <div class="pyq-card">
        <div class="pyq-tag">Previous Year Pattern • Q${idx + 1}</div>
        <h4>${q.question}</h4>
        <div class="pyq-opts">${opts}</div>
        <div class="pyq-sol"><strong>Solution:</strong> ${q.explanation}</div>
      </div>
    `;
  });

  // 11. TOPIC TEST
  let topicTestCardsHtml = '';
  (data.topic_test || []).forEach((q, idx) => {
    let opts = q.options.map((opt, oIdx) => `
      <button type="button" class="test-option-btn" data-qindex="${idx}" data-optindex="${oIdx}">
        <span class="option-letter">${letters[oIdx]}</span>
        <span class="option-text">${opt}</span>
      </button>
    `).join('');

    topicTestCardsHtml += `
      <div class="test-question-card" id="test-q-${idx}" data-correct="${q.correct_index ?? 0}">
        <div class="q-header"><span class="q-number">Test Item ${idx + 1} of 10</span></div>
        <h3 class="q-text">${q.question}</h3>
        <div class="quiz-options-group">${opts}</div>
        <div class="test-feedback hidden" id="test-feedback-${idx}">
          <p><strong>Rationale:</strong> ${q.explanation}</p>
        </div>
      </div>
    `;
  });

  return `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>${title}</title>
<meta name="description" content="${metaDesc}">
<link rel="canonical" href="${canonicalUrl}">
<link rel="icon" type="image/png" href="/favicon.png">

<!-- Common Economics Module Stylesheet -->
<link rel="stylesheet" href="/assets/css/economics.css">
</head>
<body>

<header class="site-header">
  <a class="brand" href="/">
    SJ Maths <span class="sub">Economics</span>
  </a>
  <div class="header-actions">
    <button type="button" class="theme-toggle-btn" id="theme-toggle-btn" aria-label="Toggle Dark Mode">🌙 Dark</button>
    <a class="back-btn" href="/up-pgt-economics/">← UP PGT Economics</a>
  </div>
</header>

<div class="container">
  <section class="hero">
    <div class="breadcrumb">
      <a href="/">Home</a> › <a href="/up-pgt-economics/">Economics</a> › <span>${context.sectionTitle}</span>
    </div>
    <div class="kicker">${context.sectionTitle}</div>
    <h1>${data.title}</h1>
    <p class="lead">${data.short_intro}</p>
  </section>

  <!-- 5 Modular Tabs Navigation -->
  <nav class="tabs-nav">
    <button class="tab-btn active" data-tab="tab-theory">📖 Study Notes</button>
    <button class="tab-btn" data-tab="tab-summary">⚡ Quick Revision</button>
    <button class="tab-btn" data-tab="tab-quiz">❓ Practice Quiz (${(data.quiz || []).length} MCQs)</button>
    <button class="tab-btn" data-tab="tab-pyq">🏛️ Previous Year Questions</button>
    <button class="tab-btn" data-tab="tab-test">⏱️ Timed Test (10 Min)</button>
  </nav>

  <!-- TAB 1: STUDY NOTES -->
  <div class="tab-pane active" id="tab-theory">
    ${theoristsHtml}
    ${assumptionsHtml}
    ${pillarsHtml}
    ${formulasHtml}
    ${tricksHtml}
    ${paradoxesHtml}
    ${matrixHtml}
  </div>

  <!-- TAB 2: REVISION SUMMARY -->
  <div class="tab-pane" id="tab-summary">
    <div class="card">
      <h2>⚡ Must-Remember Economic Identities &amp; Laws</h2>
      <ul class="assumptions-list">
        ${(qr.must_remember_laws || []).map(l => `<li>${formatMathHtml(l)}</li>`).join('')}
      </ul>
    </div>
    <div class="card">
      <h2>🚫 Common Analytical Confusions (Contrast Table)</h2>
      ${confusionsHtml}
    </div>
    <div class="card">
      <h2>📚 Complete Concept-by-Concept Glossary</h2>
      <p style="font-size:0.9rem;color:var(--muted);margin-bottom:14px">Every fundamental term, curve, and mechanism covered in this chapter.</p>
      ${glossaryHtml}
    </div>
  </div>

  <!-- TAB 3: PRACTICE QUIZ -->
  <div class="tab-pane" id="tab-quiz">
    <div class="card">
      <h2>❓ Interactive Practice Quiz</h2>
      <p style="font-size:0.9rem;color:var(--muted);margin-bottom:16px">Select an answer to see instant feedback and complete analytical explanation.</p>
      ${quizCardsHtml}
    </div>
  </div>

  <!-- TAB 4: PREVIOUS YEARS QUESTIONS -->
  <div class="tab-pane" id="tab-pyq">
    <div class="card">
      <h2>🏛️ Previous Years Questions &amp; Recurring Patterns</h2>
      <p style="font-size:0.9rem;color:var(--muted);margin-bottom:16px">Exam patterns from UP PGT Economics, UP TGT Social Science, and UGC NET.</p>
      ${pyqCardsHtml}
    </div>
  </div>

  <!-- TAB 5: TIMED TOPIC TEST -->
  <div class="tab-pane" id="tab-test">
    <div class="test-bar">
      <span>10 Questions • 10 Minutes Challenge</span>
      <div class="test-timer" id="test-timer">10:00</div>
      <button class="submit-btn" id="finish-test-btn">Submit Test</button>
    </div>
    <div id="test-cards-container">
      ${topicTestCardsHtml}
    </div>
    <div class="card hidden" id="test-score-card">
      <h2>Test Result: <span id="test-score-text">0/10</span></h2>
      <p id="test-feedback-summary">Test submitted successfully. Detailed explanations are now visible below each question.</p>
    </div>
  </div>
</div>

<footer>
  <span>SJ Maths • Master Economics Library • ${data.title}</span><br>
  <a href="/up-pgt-economics/" style="color:var(--primary)">UP PGT Economics Tracker</a> • 
  <a href="/up-tgt-social-science/" style="color:var(--primary)">UP TGT Social Science</a>
</footer>

<!-- Common Economics Interactive Engine -->
<script src="/assets/js/economics.js" defer></script>
</body>
</html>
`;
}

async function callGeminiApi(prompt, model, attempt) {
  const activeClientObj = aiClients[clientIndex % aiClients.length];
  clientIndex++;

  console.log(`Calling Gemini API [Model: ${model} | Key: #${activeClientObj.id} (${activeClientObj.preview})] (Attempt ${attempt})...`);
  const response = await activeClientObj.client.models.generateContent({
    model: model,
    contents: prompt,
    config: {
      responseMimeType: 'application/json',
      temperature: 0.3,
      maxOutputTokens: 32768
    }
  });

  const rawJsonText = cleanRawJson(response.text);
  let parsed = null;
  try {
    parsed = JSON.parse(rawJsonText);
  } catch (jsonErr) {
    console.warn('Initial JSON.parse failed, attempting jsonrepair...');
    parsed = JSON.parse(jsonrepair(rawJsonText));
  }
  return parsed;
}

async function processTopic(item) {
  const context = getTopicContext(item);
  console.log(`\n========================================`);
  console.log(`Processing Topic: ${item.url}`);
  console.log(`Branch: ${context.sectionTitle} | Target: UP PGT Economics`);

  if (DRY_RUN) {
    console.log(`[DRY RUN] Would generate: ${item.url}`);
    return true;
  }

  statusMap[item.url] = {
    status: 'generating',
    startedAt: new Date().toISOString()
  };
  saveStatus();

  const maxRetries = 6;
  const currentModel = MODELS[0]; // gemini-3.5-flash-lite
  let studyNotesData = null;
  let revisionAndTestingData = null;

  // CALL 1: STUDY NOTES
  console.log(`\n--- [CALL 1/2] Generating Theoretical Study Notes, Pillars, Formulas, Tricks & Mnemonics ---`);
  const promptNotes = buildPromptStudyNotes(item, context);
  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try {
      studyNotesData = await callGeminiApi(promptNotes, currentModel, attempt);
      studyNotesData = cleanMarkdownStars(studyNotesData);
      validateStudyNotes(studyNotesData);
      console.log(`✓ Call 1 (Study Notes) validated successfully (${(studyNotesData.conceptual_pillars || []).length} pillars, ${(studyNotesData.tips_and_mnemonics || []).length} tricks/mnemonics)`);
      break;
    } catch (err) {
      console.error(`Call 1 attempt ${attempt} failed:`, err.message);
      if (attempt === maxRetries) {
        statusMap[item.url] = { status: 'notes_call_failed', error: err.message, failedAt: new Date().toISOString() };
        saveStatus();
        return false;
      }
      const waitTime = err.message.includes('503') ? Math.max(GAP_MS, 15000) : GAP_MS;
      console.log(`Waiting ${waitTime / 1000}s before retrying Call 1...`);
      await new Promise(r => setTimeout(r, waitTime));
    }
  }

  // Small pause between calls
  console.log(`Pausing ${Math.round(GAP_MS / 1000)}s between Call 1 and Call 2...`);
  await new Promise(r => setTimeout(r, GAP_MS));

  // CALL 2: QUICK REVISION & TESTING
  console.log(`\n--- [CALL 2/2] Generating Quick Revision (All Concepts), Practice Quiz, PYQs & Timed Test ---`);
  const promptRev = buildPromptRevisionAndTesting(item, context, studyNotesData);
  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try {
      revisionAndTestingData = await callGeminiApi(promptRev, currentModel, attempt);
      normalizeQuestions(revisionAndTestingData.quiz);
      normalizeQuestions(revisionAndTestingData.pyq_patterns);
      normalizeQuestions(revisionAndTestingData.topic_test);
      revisionAndTestingData = cleanMarkdownStars(revisionAndTestingData);
      validateRevisionAndTesting(revisionAndTestingData);
      console.log(`✓ Call 2 (Revision & Testing) validated successfully (${revisionAndTestingData.quick_revision.terms_glossary.length} glossary terms, ${revisionAndTestingData.quiz.length} quiz MCQs, ${revisionAndTestingData.topic_test.length} test items)`);
      break;
    } catch (err) {
      console.error(`Call 2 attempt ${attempt} failed:`, err.message);
      if (attempt === maxRetries) {
        statusMap[item.url] = { status: 'revision_call_failed', error: err.message, failedAt: new Date().toISOString() };
        saveStatus();
        return false;
      }
      const waitTime = err.message.includes('503') ? Math.max(GAP_MS, 15000) : GAP_MS;
      console.log(`Waiting ${waitTime / 1000}s before retrying Call 2...`);
      await new Promise(r => setTimeout(r, waitTime));
    }
  }

  // Combine both parts
  const parsedData = {
    ...studyNotesData,
    quick_revision: revisionAndTestingData.quick_revision,
    quiz: revisionAndTestingData.quiz,
    pyq_patterns: revisionAndTestingData.pyq_patterns,
    topic_test: revisionAndTestingData.topic_test
  };

  // Target directory
  const targetDir = path.resolve(item.path);
  fs.mkdirSync(targetDir, { recursive: true });

  // Save Quiz & Test JSONs
  fs.writeFileSync(path.join(targetDir, 'quiz.json'), JSON.stringify(parsedData.quiz, null, 2), 'utf8');
  fs.writeFileSync(path.join(targetDir, 'topic-test.json'), JSON.stringify(parsedData.topic_test, null, 2), 'utf8');
  if (parsedData.pyq_patterns) {
    fs.writeFileSync(path.join(targetDir, 'pyq.json'), JSON.stringify(parsedData.pyq_patterns, null, 2), 'utf8');
  }

  // Render & Write HTML
  const targetHtmlPath = path.join(targetDir, 'index.html');
  const finalHtml = renderTopicHtml(item, context, parsedData);
  fs.writeFileSync(targetHtmlPath, finalHtml, 'utf8');
  console.log(`✓ Successfully saved: ${targetHtmlPath}`);

  const wordCount = (finalHtml.match(/\b\w+\b/g) || []).length;
  statusMap[item.url] = {
    status: 'completed',
    title: parsedData.title,
    wordCount,
    glossaryCount: parsedData.quick_revision?.terms_glossary?.length || 0,
    tricksCount: parsedData.tips_and_mnemonics?.length || 0,
    quizCount: parsedData.quiz.length,
    testCount: parsedData.topic_test.length,
    completedAt: new Date().toISOString()
  };
  saveStatus();

  return true;
}

async function main() {
  console.log(`\n======================================================`);
  console.log(`SJ Maths — Economics Pipeline Starting`);
  console.log(`Models in rotation: ${MODELS.join(', ')}`);
  console.log(`======================================================\n`);

  const eligible = getEligibleTopics();
  console.log(`Found ${eligible.length} eligible Economics topics to process.`);

  const toProcess = LIMIT ? eligible.slice(0, LIMIT) : eligible;
  let successCount = 0;
  let failCount = 0;

  for (let i = 0; i < toProcess.length; i++) {
    const item = toProcess[i];
    console.log(`\n[${i + 1}/${toProcess.length}] Progress: ${Math.round(((i + 1) / toProcess.length) * 100)}%`);
    const success = await processTopic(item);
    if (success) successCount++;
    else failCount++;

    if (GAP_MS > 0 && i < toProcess.length - 1) {
      await new Promise(r => setTimeout(r, GAP_MS));
    }
  }

  console.log(`\n======================================================`);
  console.log(`Economics Generation Complete!`);
  console.log(`Success: ${successCount} | Failed: ${failCount}`);
  console.log(`======================================================\n`);
}

main().catch(err => {
  console.error('FATAL ERROR:', err);
  process.exit(1);
});
