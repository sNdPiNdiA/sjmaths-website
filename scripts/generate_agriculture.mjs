#!/usr/bin/env node
/**
 * ============================================================================
 * SJ Maths — Agriculture Content Generator Pipeline (English Only)
 * Powered by Google Gemini API via @google/genai SDK
 * Generates canonical, high-quality English study pages for UP TGT/PGT Agriculture
 * ============================================================================
 */

import fs from 'fs';
import path from 'path';
import 'dotenv/config';
import { GoogleGenAI } from '@google/genai';
import { jsonrepair } from 'jsonrepair';

// Load all available API Keys for multi-key rotation
const apiKeys = [...new Set([
  process.env.GEMINI_API_KEY_2,
  process.env.GEMINI_API_KEY_1,
  process.env.GEMINI_API_KEY
].filter(Boolean))];

if (apiKeys.length === 0) {
  console.error('CRITICAL ERROR: No GEMINI_API_KEY defined in .env');
  process.exit(1);
}

console.log(`Loaded ${apiKeys.length} Gemini API keys for dual-key round-robin rotation.`);
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

const TARGET_TOPIC = getArg('--topic');     // e.g. /agriculture/agronomy/cereal-crops/wheat/
const TARGET_SECTION = getArg('--section'); // e.g. agronomy
const TARGET_MODEL = getArg('--model') || 'gemini-3.5-flash-lite';
const LIMIT = getArg('--limit') ? parseInt(getArg('--limit'), 10) : null;
const FORCE = hasFlag('--force');
const DRY_RUN = hasFlag('--dry-run');
const GAP_MS = getArg('--gap') ? parseInt(getArg('--gap'), 10) * 1000 : 0; // 0s buffer as requested

// Allowed models with gemini-3.5-flash-lite exclusively
const MODELS = [
  'gemini-3.5-flash-lite'
];

const modelCallCounts = {
  'gemini-3.5-flash-lite': 0
};

// Status Tracking File
const STATUS_FILE = 'content-generation-status-agriculture.json';
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
const INVENTORY_FILE = 'scratch/agriculture_inventory.json';
if (!fs.existsSync(INVENTORY_FILE)) {
  console.error(`Inventory file not found at ${INVENTORY_FILE}. Run scratch/analyze_agriculture_topics.mjs first.`);
  process.exit(1);
}
const inventory = JSON.parse(fs.readFileSync(INVENTORY_FILE, 'utf8'));

const tgtSequence = fs.existsSync('scratch/tgt_agriculture_parsed.json')
  ? JSON.parse(fs.readFileSync('scratch/tgt_agriculture_parsed.json'))
  : [];
const pgtSequence = fs.existsSync('scratch/pgt_agriculture_parsed.json')
  ? JSON.parse(fs.readFileSync('scratch/pgt_agriculture_parsed.json'))
  : [];

// Map section folders to clean titles
const SECTION_NAMES = {
  'agronomy': { en: 'Agronomy and Field Crops', code: '01' },
  'soil-science': { en: 'Soil Science and Agricultural Chemistry', code: '02' },
  'water-management': { en: 'Water Management and Irrigation Systems', code: '03' },
  'agricultural-botany': { en: 'Agricultural Botany, Genetics and Plant Breeding', code: '04' },
  'plant-physiology-and-seed-science': { en: 'Plant Physiology and Seed Science', code: '05' },
  'horticulture': { en: 'Horticulture, Olericulture & Pomology', code: '06' },
  'crop-protection': { en: 'Crop Protection, Entomology & Plant Pathology', code: '07' },
  'agricultural-economics': { en: 'Agricultural Economics and Farm Management', code: '08' },
  'agricultural-extension-and-rural-development': { en: 'Agricultural Extension and Rural Development', code: '09' },
  'animal-science': { en: 'Animal Husbandry, Dairying & Veterinary Science', code: '10' },
  'agricultural-engineering': { en: 'Agricultural Engineering and Implements', code: '11' },
  'agricultural-meteorology': { en: 'Agricultural Meteorology and Climate Adaptation', code: '12' },
  'natural-farming': { en: 'Natural and Organic Farming Systems', code: '13' }
};

/**
 * Filter topics to process
 */
function getEligibleTopics() {
  return inventory.filter(item => {
    // If specific topic requested
    if (TARGET_TOPIC) {
      const cleanTarget = TARGET_TOPIC.endsWith('/') ? TARGET_TOPIC : TARGET_TOPIC + '/';
      return item.url === cleanTarget;
    }
    // If specific section requested
    if (TARGET_SECTION) {
      if (!item.url.includes(`/${TARGET_SECTION}/`)) return false;
    }

    // Check status
    if (!FORCE && statusMap[item.url] && statusMap[item.url].status === 'completed') {
      return false;
    }
    return true;
  });
}

/**
 * Build context for a topic (previous, next, related, exam relevance)
 */
function getTopicContext(item) {
  const parts = item.url.split('/').filter(Boolean);
  // parts[0] is 'agriculture', parts[1] is section
  const sectionKey = parts[1] || 'general';
  const sectionMeta = SECTION_NAMES[sectionKey] || { en: sectionKey.replace(/-/g, ' ').replace(/\b\w/g, c => c.toUpperCase()), code: '00' };

  // Previous and Next links from trackers
  let prevTopic = null;
  let nextTopic = null;

  const inTgtIdx = tgtSequence.findIndex(t => t.href === item.url);
  const inPgtIdx = pgtSequence.findIndex(t => t.href === item.url);

  if (inTgtIdx !== -1) {
    if (inTgtIdx > 0) prevTopic = tgtSequence[inTgtIdx - 1];
    if (inTgtIdx < tgtSequence.length - 1) nextTopic = tgtSequence[inTgtIdx + 1];
  } else if (inPgtIdx !== -1) {
    if (inPgtIdx > 0) prevTopic = pgtSequence[inPgtIdx - 1];
    if (inPgtIdx < pgtSequence.length - 1) nextTopic = pgtSequence[inPgtIdx + 1];
  }

  // Related topics: other topics in same section
  const sectionPrefix = `/agriculture/${sectionKey}/`;
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
 * Construct Gemini Prompt for Agriculture (English Only)
 */
function buildPrompt(item, context) {
  const segs = item.url.split('/').filter(Boolean);
  const topicSlug = segs[segs.length - 1];
  const topicTitleGuess = topicSlug.split('-').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' ');

  return `
You are an eminent Professor of Agriculture, Agronomist, and Senior Agricultural Scientist creating comprehensive, production-ready study material for UP TGT Agriculture and UP PGT Agriculture competitive examinations in India.

Topic Details:
- Subject: Agriculture (Krishi Vigyan)
- Branch: ${context.sectionMeta.en}
- Topic Slug: ${topicSlug}
- English Topic Reference: ${topicTitleGuess}
- Canonical URL: ${item.url}
- Target Exam: ${item.examRelevance} (UP TGT / UP PGT Agriculture)

CRITICAL LANGUAGE GUIDELINES:
1. All core educational content, notes, tables, mnemonics, glossary, and questions MUST be written ENTIRELY IN ENGLISH.
2. Do NOT use Hindi or Romanized Hindi (Hinglish). Use 100% formal academic English.
3. Botanical, zoological, and causal organisms MUST be given with standard scientific binomial nomenclature in italics format (e.g. <em>Triticum aestivum</em>, <em>Magnaporthe oryzae</em>, <em>Helicoverpa armigera</em>).
4. Strictly align with standards of the Indian Council of Agricultural Research (ICAR), State Agricultural Universities (SAUs), and UPSESSB TGT/PGT Agriculture syllabus.
5. Provide rich agronomic depth:
   - Botanical taxonomy, origin, chromosomal number (ploidy level) where applicable
   - Soil and agro-climatic requirements, temperature thresholds
   - Field preparation, seed rate, seed treatment, and spacing geometry
   - Nutrient management, fertilizer requirement calculations (N:P:K recommendations, urea/DAP dose math)
   - Critical irrigation stages (e.g., CRI in wheat, flowering/pod development)
   - Major weed species, herbicides, dosages, and application timing
   - Major insect pests & diseases: symptoms, vector, causal organism, economic threshold level (ETL), and Integrated Pest Management (IPM)
   - High-yielding varieties (HYVs), hybrid varieties, physiological disorders
   - Harvesting indices, post-harvest technology, storage moisture content, and average yield
6. NO FABRICATED PYQs: Do not label questions as actual past papers.

OUTPUT FORMAT:
Respond with ONLY a valid, raw JSON object (no Markdown code block wrappers, no preamble) adhering to this schema:
{
  "title": "Comprehensive Topic Title in English",
  "short_intro": "2 to 3 concise sentences introducing the topic with strong examination context.",
  "notes_sections": [
    {
      "heading": "H2 Level Section Heading",
      "content_html": "<p>Detailed, rigorous explanation...</p><ul><li>Key agronomic point...</li></ul>"
    }
  ],
  "comparison_tables": [
    {
      "title": "Comparative Analysis Table Title",
      "headers": ["Parameter / Feature", "Category A", "Category B"],
      "rows": [
        ["Row Feature 1", "Value A1", "Value B1"]
      ]
    }
  ],
  "mnemonics": [
    {
      "title": "Mnemonic / Formula Memory Trick Title",
      "trick": "Clever, memorable English acronym, rhyme, or memory shortcut",
      "explanation": "Detailed breakdown of each letter/word and how to recall during the exam"
    }
  ],
  "exam_points": [
    "High-yield factual point 1 (variety, seed rate, critical stage, chemical dosage, or formula)",
    "High-yield factual point 2"
  ],
  "common_errors": [
    "Common student confusion or exam trap and the accurate scientific agronomic fact"
  ],
  "chapter_summary_concepts": [
    {
      "concept_num": "Concept 1",
      "concept_title": "Concept Title in English",
      "concept_body_html": "<p>Comprehensive conceptual overview...</p><ul><li><span class=\"summary-highlight-pill\">Key Term</span>: Clear definition and numerical standard...</li></ul>"
    }
  ],
  "quick_revision": {
    "terms_glossary": [
      {
        "term": "Key Agronomic / Technical Term",
        "term_en": "Standard Scientific Term / Formula",
        "definition": "Precise, 1 to 2 sentence authoritative definition explaining the core principle."
      }
    ],
    "summary": [
      "Quick revision bullet point 1",
      "Quick revision bullet point 2"
    ],
    "must_remember": [
      "Must-remember exam fact 1",
      "Must-remember exam fact 2"
    ],
    "common_confusions": [
      {
        "term_a": "Term A",
        "term_b": "Term B",
        "difference": "Precise scientific distinction between Term A and Term B"
      }
    ]
  },
  "quiz": [
    {
      "question": "Tricky, high-yield conceptual multiple-choice question in English?",
      "options": ["Option A", "Option B", "Option C", "Option D"],
      "correct_index": 0,
      "hint": "Pedagogical hint developing scientific reasoning",
      "explanation": "Thorough explanation clarifying why the correct option is right and why the other options are incorrect."
    }
  ],
  "topic_test": [
    {
      "question": "Exam-standard competitive MCQ in English?",
      "options": ["Option A", "Option B", "Option C", "Option D"],
      "correct_index": 0,
      "explanation": "Detailed step-by-step solution and agronomic explanation.",
      "difficulty": "TGT"
    }
  ],
  "pyq_pattern_practice": [
    {
      "question": "Pattern practice question based on competitive exam trends?",
      "options": ["Option A", "Option B", "Option C", "Option D"],
      "correct_index": 0,
      "explanation": "Detailed solution.",
      "note": "Practice Question — Pattern Based"
    }
  ]
}

REQUIREMENTS:
- 'notes_sections': Provide 4 to 6 substantial sections covering taxonomy, morphology, agronomy, nutrient management, crop protection, and economics.
- 'mnemonics': Provide 1 to 3 practical, memorable memory tricks in English.
- 'chapter_summary_concepts': Provide 4 to 6 comprehensive concept blocks formatted as end-of-chapter textbook master summaries.
- 'terms_glossary': Under 'quick_revision', provide 10 to 12 concise technical terms.
- 'quiz': Provide exactly 18 to 20 TRICKY, conceptual MCQs covering all major concepts in the notes.
- 'topic_test': Provide exactly 10 unique, challenging MCQs with TGT/PGT difficulty.
- 'pyq_pattern_practice': Provide exactly 4 to 5 pattern practice MCQs.
- All MCQ arrays MUST have exactly 4 options per question, with 'correct_index' an integer from 0 to 3.
- Language: 100% English.
`;
}

/**
 * Clean raw JSON string to prevent syntax errors
 */
function cleanRawJson(text) {
  if (!text) return '';
  // Replace \u that is not followed by 4 hex digits with u
  let s = text.replace(/\\u(?![0-9a-fA-F]{4})/gi, 'u');
  // Replace backslash not followed by valid JSON escape char (" \ / b f n r t u) with double backslash
  s = s.replace(/\\([^"\\\/bfnrtu])/gi, '\\\\$1');
  return s;
}

/**
 * Normalize MCQs options and correct_index
 */
function normalizeQuestions(arr) {
  if (!Array.isArray(arr)) return;
  const indexMap = { 'A': 0, 'B': 1, 'C': 2, 'D': 3, 'a': 0, 'b': 1, 'c': 2, 'd': 3, '0': 0, '1': 1, '2': 2, '3': 3 };
  arr.forEach((q, i) => {
    if (!q || typeof q !== 'object') return;
    if (!q.question) q.question = `Conceptual Question ${i + 1}`;
    
    if (!Array.isArray(q.options)) {
      if (Array.isArray(q.choices)) {
        q.options = q.choices;
      } else if (q.options && typeof q.options === 'object') {
        q.options = Object.values(q.options);
      } else {
        q.options = [];
      }
    }
    
    q.options = q.options.map(opt => String(opt ?? ''));

    if (q.options.length < 4) {
      while (q.options.length < 4) {
        q.options.push(`Standard Option ${String.fromCharCode(65 + q.options.length)}`);
      }
    } else if (q.options.length > 4) {
      q.options = q.options.slice(0, 4);
    }
    let idx = q.correct_index ?? q.correct_option ?? q.answer ?? q.correctAnswer;
    if (typeof idx === 'number' && idx >= 0 && idx <= 3) {
      q.correct_index = idx;
    } else if (idx !== undefined && indexMap[String(idx).trim()] !== undefined) {
      q.correct_index = indexMap[String(idx).trim()];
    } else {
      q.correct_index = 0;
    }
    if (!q.explanation) q.explanation = 'Detailed explanation aligned with standard ICAR and UP TGT/PGT Agriculture textbooks.';
  });
}

/**
 * Validate Gemini JSON Output
 */
function validateContent(data) {
  if (!data || typeof data !== 'object') throw new Error('Root output is not an object');
  if (!data.title || typeof data.title !== 'string') throw new Error('Missing title');
  if (!data.notes_sections || !Array.isArray(data.notes_sections) || data.notes_sections.length < 3) {
    throw new Error('notes_sections must have at least 3 sections');
  }

  // Validate chapter_summary_concepts
  if (!data.chapter_summary_concepts || !Array.isArray(data.chapter_summary_concepts) || data.chapter_summary_concepts.length < 3) {
    throw new Error('chapter_summary_concepts must have at least 3 concept blocks');
  }

  // Validate quiz
  if (!data.quiz || !Array.isArray(data.quiz) || data.quiz.length < 15) {
    throw new Error(`quiz must have at least 15 questions (found: ${data.quiz?.length || 0})`);
  }

  // Validate topic_test
  if (!data.topic_test || !Array.isArray(data.topic_test) || data.topic_test.length < 8) {
    throw new Error(`topic_test must have at least 8 questions (found: ${data.topic_test?.length || 0})`);
  }

  return true;
}

/**
 * Convert structured data into static, accessible English HTML
 */
function renderTopicHtml(item, context, data) {
  const title = `${data.title}: Study Notes, MCQs, Revision & Topic Test | Agriculture | SJ Maths`;
  const metaDesc = `Master ${data.title} for UP TGT and UP PGT Agriculture exams. In-depth agronomic notes, scientific principles, chapter summary, and 30 practice MCQs.`;
  const canonicalUrl = `https://sjmaths.com${item.url}`;

  // Exam badges markup
  const isTgt = item.inTgt || item.examRelevance === 'Both' || (item.examRelevance && item.examRelevance.includes('TGT'));
  const isPgt = item.inPgt || item.examRelevance === 'Both' || (item.examRelevance && item.examRelevance.includes('PGT'));

  let examBadgesHtml = '';
  if (isTgt && isPgt) {
    examBadgesHtml = `
      <a class="exam-chip both" href="/up-tgt-agriculture/">UP TGT Agriculture Tracker →</a>
      <a class="exam-chip both" href="/up-pgt-agriculture/">UP PGT Agriculture Tracker →</a>
    `;
  } else if (isTgt) {
    examBadgesHtml = `<a class="exam-chip tgt" href="/up-tgt-agriculture/">UP TGT Agriculture Tracker →</a>`;
  } else if (isPgt) {
    examBadgesHtml = `<a class="exam-chip pgt" href="/up-pgt-agriculture/">UP PGT Agriculture Tracker →</a>`;
  } else {
    examBadgesHtml = `
      <a class="exam-chip both" href="/up-tgt-agriculture/">UP TGT Agriculture Tracker →</a>
      <a class="exam-chip both" href="/up-pgt-agriculture/">UP PGT Agriculture Tracker →</a>
    `;
  }

  // Schema Breadcrumbs
  const breadcrumbElements = [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://sjmaths.com/" },
    { "@type": "ListItem", "position": 2, "name": "Agriculture", "item": "https://sjmaths.com/agriculture/" },
    { "@type": "ListItem", "position": 3, "name": context.sectionMeta.en, "item": `https://sjmaths.com/agriculture/${context.sectionKey}/` },
    { "@type": "ListItem", "position": 4, "name": data.title, "item": canonicalUrl }
  ];

  const schemaJsonLd = {
    "@context": "https://schema.org",
    "@type": "LearningResource",
    "name": data.title,
    "headline": `${data.title} — UP TGT/PGT Agriculture Study Notes & Mock Test`,
    "description": metaDesc,
    "url": canonicalUrl,
    "inLanguage": "en",
    "learningResourceType": "Study Guide / Quiz",
    "educationalLevel": "Post-Secondary / Teacher Eligibility Examination",
    "isPartOf": {
      "@type": "WebSite",
      "name": "SJ Maths",
      "url": "https://sjmaths.com/"
    },
    "breadcrumb": {
      "@type": "BreadcrumbList",
      "itemListElement": breadcrumbElements
    }
  };

  // Render Notes HTML
  let notesHtml = '';
  data.notes_sections.forEach((sec, idx) => {
    notesHtml += `
      <section class="notes-section" id="sec-${idx + 1}">
        <h2>${sec.heading}</h2>
        <div class="prose-content">
          ${sec.content_html}
        </div>
      </section>
    `;
  });

  // Render Comparison Tables
  if (data.comparison_tables && data.comparison_tables.length > 0) {
    data.comparison_tables.forEach(table => {
      let headersHtml = table.headers.map(h => `<th>${h}</th>`).join('');
      let rowsHtml = table.rows.map(row => `<tr>${row.map(cell => `<td>${cell}</td>`).join('')}</tr>`).join('');
      notesHtml += `
        <div class="comparison-card">
          <div class="comparison-title">${table.title}</div>
          <div class="table-responsive">
            <table class="styled-table">
              <thead><tr>${headersHtml}</tr></thead>
              <tbody>${rowsHtml}</tbody>
            </table>
          </div>
        </div>
      `;
    });
  }

  // Render Mnemonics
  if (data.mnemonics && data.mnemonics.length > 0) {
    data.mnemonics.forEach(m => {
      notesHtml += `
        <div class="mnemonic-card">
          <div class="mnemonic-badge">Memory Trick / Mnemonic</div>
          <div class="mnemonic-title">${m.title}</div>
          <div class="mnemonic-formula">${m.trick}</div>
          <p class="mnemonic-desc">${m.explanation}</p>
        </div>
      `;
    });
  }

  // Render Exam Points
  if (data.exam_points && data.exam_points.length > 0) {
    let pts = data.exam_points.map(p => `<li>${p}</li>`).join('');
    notesHtml += `
      <div class="exam-points-card">
        <div class="exam-points-title">⚡ High-Yield Exam Points (UP TGT / PGT Focus)</div>
        <ul class="exam-points-list">${pts}</ul>
      </div>
    `;
  }

  // Render Common Errors
  if (data.common_errors && data.common_errors.length > 0) {
    let errs = data.common_errors.map(e => `<li>${e}</li>`).join('');
    notesHtml += `
      <div class="common-errors-card">
        <div class="common-errors-title">⚠️ Common Mistakes & Exam Pitfalls</div>
        <ul class="common-errors-list">${errs}</ul>
      </div>
    `;
  }

  // Render Chapter Summary Concepts
  let summaryConceptsHtml = '';
  if (data.chapter_summary_concepts && data.chapter_summary_concepts.length > 0) {
    data.chapter_summary_concepts.forEach(c => {
      summaryConceptsHtml += `
        <div class="summary-concept-card">
          <div class="summary-concept-header">
            <span class="summary-concept-pill">${c.concept_num}</span>
            <h3 class="summary-concept-title">${c.concept_title}</h3>
          </div>
          <div class="summary-concept-body prose-content">
            ${c.concept_body_html}
          </div>
        </div>
      `;
    });
  }

  // Render Quick Revision
  const qr = data.quick_revision || {};
  let glossaryHtml = '';
  if (qr.terms_glossary && qr.terms_glossary.length > 0) {
    qr.terms_glossary.forEach(t => {
      glossaryHtml += `
        <div class="glossary-item">
          <div class="glossary-term-wrap">
            <span class="glossary-term">${t.term}</span>
            ${t.term_en ? `<span class="glossary-term-en">(${t.term_en})</span>` : ''}
          </div>
          <div class="glossary-def">${t.definition}</div>
        </div>
      `;
    });
  }

  let mustRememberHtml = '';
  if (qr.must_remember && qr.must_remember.length > 0) {
    mustRememberHtml = qr.must_remember.map(item => `<li>${item}</li>`).join('');
  }

  let summaryBulletsHtml = '';
  if (qr.summary && qr.summary.length > 0) {
    summaryBulletsHtml = qr.summary.map(item => `<li>${item}</li>`).join('');
  }

  let confusionsHtml = '';
  if (qr.common_confusions && qr.common_confusions.length > 0) {
    qr.common_confusions.forEach(cf => {
      confusionsHtml += `
        <div class="confusion-item">
          <div class="confusion-terms">
            <span class="conf-badge-a">${cf.term_a}</span>
            <span class="conf-vs">VS</span>
            <span class="conf-badge-b">${cf.term_b}</span>
          </div>
          <p class="confusion-diff">${cf.difference}</p>
        </div>
      `;
    });
  }

  // Render Quiz Cards (SSR for instant availability & SEO)
  let quizCardsHtml = '';
  data.quiz.forEach((q, idx) => {
    const options = Array.isArray(q.options) && q.options.length >= 4 
      ? q.options 
      : ['Option A', 'Option B', 'Option C', 'Option D'];

    let opts = options.map((opt, oIdx) => `
      <button type="button" class="quiz-option-btn" data-qindex="${idx}" data-optindex="${oIdx}">
        <span class="option-letter">${String.fromCharCode(65 + oIdx)}</span>
        <span class="option-text">${opt}</span>
      </button>
    `).join('');

    quizCardsHtml += `
      <div class="quiz-question-card" id="q-card-${idx}" data-correct="${q.correct_index}">
        <div class="q-header">
          <span class="q-number">Question ${idx + 1} of ${data.quiz.length}</span>
          <span class="q-badge">Conceptual MCQ</span>
        </div>
        <h3 class="q-text">${q.question}</h3>
        <div class="quiz-options-group">
          ${opts}
        </div>
        <div class="q-feedback hidden" id="feedback-${idx}">
          <div class="feedback-indicator"></div>
          <p class="feedback-explanation"><strong>Explanation:</strong> ${q.explanation}</p>
        </div>
      </div>
    `;
  });

  // Render Topic Test Cards (SSR)
  let topicTestCardsHtml = '';
  data.topic_test.forEach((t, idx) => {
    const options = Array.isArray(t.options) && t.options.length >= 4 
      ? t.options 
      : ['Option A', 'Option B', 'Option C', 'Option D'];

    let opts = options.map((opt, oIdx) => `
      <button type="button" class="test-option-btn" data-tindex="${idx}" data-optindex="${oIdx}">
        <span class="option-letter">${String.fromCharCode(65 + oIdx)}</span>
        <span class="option-text">${opt}</span>
      </button>
    `).join('');

    topicTestCardsHtml += `
      <div class="test-question-card" id="t-card-${idx}" data-correct="${t.correct_index}">
        <div class="q-header">
          <span class="q-number">Test Question ${idx + 1} of ${data.topic_test.length}</span>
          <span class="q-badge test">${t.difficulty || 'TGT/PGT'} Standard</span>
        </div>
        <h3 class="q-text">${t.question}</h3>
        <div class="quiz-options-group">
          ${opts}
        </div>
        <div class="t-feedback hidden" id="t-feedback-${idx}">
          <p class="feedback-explanation"><strong>Solution & Rationale:</strong> ${t.explanation}</p>
        </div>
      </div>
    `;
  });

  // Navigation Links
  const prevHtml = context.prevTopic
    ? `<a class="nav-prev" href="${context.prevTopic.href}">← Previous: ${context.prevTopic.title}</a>`
    : `<span class="nav-prev disabled">First Topic</span>`;
  const nextHtml = context.nextTopic
    ? `<a class="nav-next" href="${context.nextTopic.href}">Next: ${context.nextTopic.title} →</a>`
    : `<span class="nav-next disabled">End of Section</span>`;

  // Related Topics
  let relatedHtml = '';
  if (context.related && context.related.length > 0) {
    relatedHtml = context.related.map(r => `<li><a href="${r.url}">${r.title}</a></li>`).join('');
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
<meta name="theme-color" content="#15803d">
<link rel="canonical" href="${canonicalUrl}">
<link rel="icon" type="image/png" href="/favicon.png">

<!-- Open Graph -->
<meta property="og:type" content="article">
<meta property="og:site_name" content="SJ Maths">
<meta property="og:title" content="${title}">
<meta property="og:description" content="${metaDesc}">
<meta property="og:url" content="${canonicalUrl}">
<meta property="og:image" content="https://sjmaths.com/assets/icons/icon-512x512.png">
<meta property="og:locale" content="en_US">

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="${title}">
<meta name="twitter:description" content="${metaDesc}">
<meta name="twitter:image" content="https://sjmaths.com/assets/icons/icon-512x512.png">

<!-- Structured Data (JSON-LD) -->
<script type="application/ld+json">
${JSON.stringify(schemaJsonLd, null, 2)}
</script>

<!-- Stylesheets -->
<link rel="stylesheet" href="/assets/css/topic-page.css">
<style>
:root {
  --brand: #14532d;
  --brand-dark: #052e16;
  --brand-light: #16a34a;
  --accent: #15803d;
  --accent-hover: #166534;
  --accent-soft: rgba(21, 128, 61, 0.08);
  --accent-border: rgba(21, 128, 61, 0.24);
}
html.dark, body.dark-mode {
  --brand: #4ade80;
  --brand-dark: #86efac;
  --brand-light: #22c55e;
  --accent: #34d399;
  --accent-hover: #6ee7b7;
  --accent-soft: rgba(52, 211, 153, 0.14);
  --accent-border: rgba(52, 211, 153, 0.35);
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
      <span class="brand-mark" style="background: linear-gradient(145deg, #14532d, #16a34a); font-family: serif; font-size: 1.35rem; font-style: italic; display: flex; align-items: center; justify-content: center;">&int;</span>
      <span>
        <span class="brand-name">SJ Maths</span>
        <span class="brand-sub">Agriculture Master Study System</span>
      </span>
    </a>
    <div class="header-actions">
      <button type="button" class="theme-toggle-btn" id="btn-theme-toggle" aria-label="Toggle Dark Mode">🌙 Dark Mode</button>
      <a class="back-btn" href="/up-pgt-agriculture/" title="UP PGT Agriculture Tracker">← UP PGT<span class="desk-only"> Agriculture</span></a>
      <a class="back-btn" href="/up-tgt-agriculture/" title="UP TGT Agriculture Tracker">← UP TGT<span class="desk-only"> Agriculture</span></a>
    </div>
  </div>
</header>

<main class="wrap">
  <!-- Hero Section -->
  <section class="hero">
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="https://sjmaths.com/">Home</a>
      <span class="breadcrumb-sep">›</span>
      <a href="/agriculture/">Agriculture</a>
      <span class="breadcrumb-sep">›</span>
      <a href="/agriculture/${context.sectionKey}/">${context.sectionMeta.en}</a>
      <span class="breadcrumb-sep">›</span>
      <span aria-current="page">${data.title}</span>
    </nav>
    <div class="kicker" style="color: #15803d; font-weight: 800;">${context.sectionMeta.en}</div>
    <h1>${data.title}</h1>
    <p class="lead">${data.short_intro}</p>

    <div class="exam-badges">
      ${examBadgesHtml}
    </div>
  </section>

  <!-- Interactive Learning Navigation Tabs -->
  <div class="study-tabs-sticky-wrapper">
    <div class="study-tabs" role="tablist" aria-label="Study Module Tabs">
      <button type="button" class="tab-btn active" role="tab" aria-selected="true" data-tab="tab-notes" id="tab-btn-notes">
        <span>📖</span> <span>Study Notes</span>
      </button>
      <button type="button" class="tab-btn" role="tab" aria-selected="false" data-tab="tab-summary" id="tab-btn-summary">
        <span>⚡</span> <span>Chapter Summary</span>
      </button>
      <button type="button" class="tab-btn" role="tab" aria-selected="false" data-tab="tab-revision" id="tab-btn-revision">
        <span>🔄</span> <span>Quick Revision</span>
      </button>
      <button type="button" class="tab-btn" role="tab" aria-selected="false" data-tab="tab-quiz" id="tab-btn-quiz">
        <span>❓</span> <span>Practice Quiz</span> <span class="tab-badge">${data.quiz.length}Q</span>
      </button>
      <button type="button" class="tab-btn" role="tab" aria-selected="false" data-tab="tab-test" id="tab-btn-test">
        <span>⏱️</span> <span>Topic Test</span> <span class="tab-badge">10Q</span>
      </button>
    </div>
  </div>

  <!-- Tab Panels & Main Grid Layout -->
  <div class="main-grid">
    <div class="content-col">

      <!-- TAB 1: NOTES (Present in Server Static HTML for Search Engines) -->
      <article class="tab-panel active" id="tab-notes" role="tabpanel" aria-labelledby="tab-btn-notes">
        ${notesHtml}
      </article>

      <!-- TAB 2: CHAPTER SUMMARY -->
      <article class="tab-panel hidden" id="tab-summary" role="tabpanel" aria-labelledby="tab-btn-summary">
        <div class="summary-container">
          <div class="summary-hero-box">
            <h2>⚡ Chapter Master Summary: ${data.title}</h2>
            <p>Systematic concept review designed for quick retention and last-minute pre-exam revision.</p>
          </div>
          ${summaryConceptsHtml}
        </div>
      </article>

      <!-- TAB 3: QUICK REVISION & GLOSSARY -->
      <article class="tab-panel hidden" id="tab-revision" role="tabpanel" aria-labelledby="tab-btn-revision">
        <div class="revision-container">
          <div class="revision-card-box">
            <h2>📚 Technical Terms Glossary</h2>
            <div class="glossary-grid">
              ${glossaryHtml}
            </div>
          </div>

          ${mustRememberHtml ? `
          <div class="revision-card-box highlight">
            <h2>🎯 Must-Remember High-Frequency Facts</h2>
            <ul class="must-remember-list">
              ${mustRememberHtml}
            </ul>
          </div>` : ''}

          ${summaryBulletsHtml ? `
          <div class="revision-card-box">
            <h2>📌 Quick Recap Bullet Points</h2>
            <ul class="recap-list">
              ${summaryBulletsHtml}
            </ul>
          </div>` : ''}

          ${confusionsHtml ? `
          <div class="revision-card-box diff">
            <h2>⚖️ Concepts Often Confused in Examinations</h2>
            <div class="confusions-grid">
              ${confusionsHtml}
            </div>
          </div>` : ''}
        </div>
      </article>

      <!-- TAB 4: CONCEPTUAL PRACTICE QUIZ -->
      <article class="tab-panel hidden" id="tab-quiz" role="tabpanel" aria-labelledby="tab-btn-quiz">
        <div class="quiz-panel-header">
          <div class="quiz-panel-title">
            <h2>❓ Conceptual Practice Questions (20 MCQs)</h2>
            <p>Solve each question to test your fundamental conceptual clarity. Click any option to verify your answer with detailed explanation.</p>
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

      <!-- TAB 5: TIMED TOPIC TEST -->
      <article class="tab-panel hidden" id="tab-test" role="tabpanel" aria-labelledby="tab-btn-test">
        <div class="test-panel-header">
          <div>
            <h2>⏱️ 10-Minute Topic Speed Test</h2>
            <p>Simulate exam conditions with 10 challenging competitive questions under a strict countdown timer.</p>
          </div>
          <div class="test-timer-badge" id="testTimerBadge">
            <span class="timer-icon">⏳</span> <span id="timerDisplay">10:00</span>
          </div>
        </div>

        <div class="test-start-wrapper" id="testStartWrap">
          <div class="test-instruction-box">
            <h3>Test Instructions</h3>
            <ul>
              <li><strong>Total Questions:</strong> 10 MCQs</li>
              <li><strong>Time Allowed:</strong> 10 Minutes</li>
              <li><strong>Marking Scheme:</strong> +1 mark for correct, 0 for unattempted</li>
              <li><strong>Exam Level:</strong> UP TGT / PGT Agriculture Standard</li>
            </ul>
            <button type="button" class="btn-start-test" id="btnStartTest">Start Test Now</button>
          </div>
        </div>

        <div class="test-active-container hidden" id="testActiveWrap">
          <div class="test-questions-list">
            ${topicTestCardsHtml}
          </div>
          <div class="test-submit-bar">
            <button type="button" class="btn-submit-test" id="btnSubmitTest">Submit & View Analysis</button>
          </div>
        </div>

        <div class="test-result-modal hidden" id="testResultModal">
          <div class="result-card">
            <h3>Test Results & Performance Summary</h3>
            <div class="result-score-circle">
              <span id="resFinalScore">0</span> / 10
            </div>
            <p id="resFeedbackText">Review detailed solutions below for all questions.</p>
            <button type="button" class="btn-retake-test" id="btnRetakeTest">Retake Test</button>
          </div>
        </div>
      </article>

      <!-- Topic Navigation (Previous & Next) -->
      <nav class="topic-pagination" aria-label="Topic Navigation">
        ${prevHtml}
        ${nextHtml}
      </nav>

    </div>

    <!-- Right Sidebar -->
    <aside class="sidebar-col">
      <div class="sidebar-card">
        <h3>Exam Syllabus Trackers</h3>
        <p>Monitor your study progress across all subjects in the UP competitive exam trackers.</p>
        <div class="action-box">
          <strong>UP TGT Agriculture Tracker</strong>
          <p>95 syllabus microtopics, checklist, and practice sets</p>
          <a class="action-btn" href="/up-tgt-agriculture/">Open TGT Tracker →</a>
        </div>
        <div class="action-box" style="margin-top: 12px;">
          <strong>UP PGT Agriculture Tracker</strong>
          <p>157 detailed syllabus topics with exam weights</p>
          <a class="action-btn" href="/up-pgt-agriculture/">Open PGT Tracker →</a>
        </div>
      </div>

      ${relatedHtml ? `
      <div class="sidebar-card" style="margin-top: 20px;">
        <h3>Related Topics</h3>
        <ul class="related-links">
          ${relatedHtml}
        </ul>
      </div>` : ''}
    </aside>
  </div>
</main>

<footer class="footer">
  <div class="wrap footer-inner">
    <span>SJ Maths • Master Subject Library • ${data.title}</span>
    <div>
      <a href="https://sjmaths.com/">Home</a> &nbsp;•&nbsp;
      <a href="/up-tgt-agriculture/">UP TGT Agriculture</a> &nbsp;•&nbsp;
      <a href="/up-pgt-agriculture/">UP PGT Agriculture</a>
    </div>
  </div>
</footer>

<!-- Interactive Page Scripts -->
<script>
document.addEventListener('DOMContentLoaded', () => {
  // Dual-Class Theme Toggle
  const btnTheme = document.getElementById('btn-theme-toggle');
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  const savedTheme = localStorage.getItem('sjmaths_theme') || localStorage.getItem('sj_theme');
  if (savedTheme === 'dark' || (!savedTheme && prefersDark)) {
    document.body.classList.add('dark-mode');
    document.documentElement.classList.add('dark');
    if (btnTheme) btnTheme.textContent = '☀️ Light Mode';
  }
  if (btnTheme) {
    btnTheme.addEventListener('click', () => {
      const isDark = document.body.classList.toggle('dark-mode');
      document.documentElement.classList.toggle('dark', isDark);
      localStorage.setItem('sjmaths_theme', isDark ? 'dark' : 'light');
      localStorage.setItem('sj_theme', isDark ? 'dark' : 'light');
      btnTheme.textContent = isDark ? '☀️ Light Mode' : '🌙 Dark Mode';
    });
  }

  // Tab Switching
  const tabBtns = document.querySelectorAll('.tab-btn');
  const tabPanels = document.querySelectorAll('.tab-panel');

  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const targetId = btn.getAttribute('data-tab');
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
      const activePanel = document.getElementById(targetId);
      if (activePanel) {
        activePanel.classList.remove('hidden');
        activePanel.classList.add('active');
      }
      window.scrollTo({ top: document.querySelector('.study-tabs-sticky-wrapper').offsetTop - 20, behavior: 'smooth' });
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
      const card = document.getElementById('q-card-' + qIndex);
      const correctIndex = parseInt(card.getAttribute('data-correct'), 10);
      const feedback = document.getElementById('feedback-' + qIndex);

      if (answeredQuestions.has(qIndex)) return;
      answeredQuestions.add(qIndex);

      const allBtnsForQ = card.querySelectorAll('.quiz-option-btn');
      allBtnsForQ.forEach((b, idx) => {
        b.disabled = true;
        if (idx === correctIndex) b.classList.add('correct');
        else if (idx === optIndex && optIndex !== correctIndex) b.classList.add('incorrect');
      });

      const letters = ['A', 'B', 'C', 'D'];
      if (optIndex === correctIndex) {
        quizScore++;
        document.getElementById('quizScore').textContent = quizScore;
        feedback.querySelector('.feedback-indicator').textContent = '✓ Correct Answer!';
        feedback.classList.add('correct');
      } else {
        feedback.querySelector('.feedback-indicator').textContent = '✗ Incorrect. Correct Option: ' + letters[correctIndex];
        feedback.classList.add('incorrect');
      }
      feedback.classList.remove('hidden');
    });
  });

  const btnResetQuiz = document.getElementById('btnResetQuiz');
  if (btnResetQuiz) {
    btnResetQuiz.addEventListener('click', () => {
      quizScore = 0;
      answeredQuestions.clear();
      document.getElementById('quizScore').textContent = '0';
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

  // Topic Test Logic
  const btnStartTest = document.getElementById('btnStartTest');
  const testStartWrap = document.getElementById('testStartWrap');
  const testActiveWrap = document.getElementById('testActiveWrap');
  const timerDisplay = document.getElementById('timerDisplay');
  let testTimer = null;
  let secondsLeft = 600;

  if (btnStartTest) {
    btnStartTest.addEventListener('click', () => {
      testStartWrap.classList.add('hidden');
      testActiveWrap.classList.remove('hidden');
      testTimer = setInterval(() => {
        secondsLeft--;
        const mins = Math.floor(secondsLeft / 60);
        const secs = secondsLeft % 60;
        timerDisplay.textContent = (mins < 10 ? '0' : '') + mins + ':' + (secs < 10 ? '0' : '') + secs;
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
      card.querySelectorAll('.test-option-btn').forEach(b => b.classList.remove('selected'));
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
      feedback.classList.remove('hidden');
    });
    document.getElementById('resFinalScore').textContent = score;
    document.getElementById('testResultModal').classList.remove('hidden');
    document.getElementById('btnSubmitTest').classList.add('hidden');
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
 * Process single topic through Gemini
 */
async function processTopic(item) {
  const context = getTopicContext(item);
  console.log(`\n------------------------------------------------------------`);
  console.log(`Processing Topic: ${item.url}`);
  console.log(`Branch: ${context.sectionMeta.en} | Target: ${item.examRelevance}`);

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
  const maxRetries = 4;

  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    // Pick API client from dual-key pool
    const clientObj = aiClients[clientIndex % aiClients.length];
    clientIndex++;

    // Primary model is gemini-3.5-flash-lite, with fallbacks if retrying
    const currentModel = attempt === 1 ? TARGET_MODEL : (MODELS[attempt - 1] || TARGET_MODEL);
    modelCallCounts[currentModel] = (modelCallCounts[currentModel] || 0) + 1;

    try {
      console.log(`Calling Gemini API [Key #${clientObj.id} (${clientObj.preview}) | Model: ${currentModel}] (Attempt ${attempt}/${maxRetries})...`);
      const response = await clientObj.client.models.generateContent({
        model: currentModel,
        contents: prompt,
        config: {
          responseMimeType: 'application/json',
          temperature: 0.3
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
      normalizeQuestions(parsedData.topic_test);

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
      if (GAP_MS > 0) {
        console.log(`Waiting ${GAP_MS / 1000}s gap before next API call attempt...`);
        await new Promise(r => setTimeout(r, GAP_MS));
      } else {
        await new Promise(r => setTimeout(r, 1000)); // Minimal 1s backoff only on failed attempts
      }
    }
  }

  // Target directory
  const targetDir = path.resolve(item.dir);
  fs.mkdirSync(targetDir, { recursive: true });

  // Write question JSON files
  const quizPath = path.join(targetDir, 'quiz.json');
  fs.writeFileSync(quizPath, JSON.stringify(parsedData.quiz, null, 2), 'utf8');

  const testPath = path.join(targetDir, 'topic-test.json');
  fs.writeFileSync(testPath, JSON.stringify(parsedData.topic_test, null, 2), 'utf8');

  // Render & write HTML
  const targetHtmlPath = path.join(targetDir, 'index.html');
  const finalHtml = renderTopicHtml(item, context, parsedData);
  fs.writeFileSync(targetHtmlPath, finalHtml, 'utf8');
  console.log(`✓ Successfully saved: ${targetHtmlPath}`);

  // Count words
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
 * Main Execution Loop with 10s gap between API calls
 */
async function main() {
  console.log('=== SJ Maths Agriculture Content Generator Pipeline (English Only) ===');
  console.log(`Active API Keys: ${aiClients.length} keys loaded (${aiClients.map(c => `Key #${c.id}`).join(', ')})`);
  console.log(`Primary Model: ${TARGET_MODEL}`);
  console.log(`Rate-limit buffer: ${GAP_MS > 0 ? (GAP_MS / 1000) + 's gap' : 'No buffer (0s gap)'}`);

  const eligible = getEligibleTopics();
  console.log(`Eligible topics found: ${eligible.length}`);

  const toProcess = LIMIT ? eligible.slice(0, LIMIT) : eligible;
  console.log(`Topics scheduled to process: ${toProcess.length}`);

  let successCount = 0;
  for (let i = 0; i < toProcess.length; i++) {
    const item = toProcess[i];
    console.log(`\n[${i + 1}/${toProcess.length}] Processing: ${item.url}`);
    
    try {
      const ok = await processTopic(item);
      if (ok) successCount++;
    } catch (err) {
      console.error(`[CRITICAL] Error generating ${item.url}:`, err.message);
      statusMap[item.url] = {
        status: 'validation_failed',
        error: err.message,
        failedAt: new Date().toISOString()
      };
      saveStatus();
    }

    if (i < toProcess.length - 1 && !DRY_RUN && GAP_MS > 0) {
      console.log(`Applying ${GAP_MS / 1000}s buffer before next API call...`);
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
