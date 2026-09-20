#!/usr/bin/env node
/**
 * ============================================================================
 * SJ Maths — Art (चित्रकला) Content Generator Pipeline
 * Powered by Google Gemini API via @google/genai SDK
 * Generates canonical, high-quality Devanagari Hindi study pages for UP TGT/PGT Art
 * ============================================================================
 */

import fs from 'fs';
import path from 'path';
import 'dotenv/config';
import { GoogleGenAI } from '@google/genai';
import { jsonrepair } from 'jsonrepair';

// Verify API Key existence
const apiKey = process.env.GEMINI_API_KEY;
if (!apiKey) {
  console.error('CRITICAL ERROR: GEMINI_API_KEY environment variable is not defined.');
  console.error('Please set GEMINI_API_KEY in your .env file or environment.');
  process.exit(1);
}

// Initialize Gemini Client
const ai = new GoogleGenAI({ apiKey });

// Parse Command Line Arguments
const args = process.argv.slice(2);
function getArg(flag) {
  const idx = args.indexOf(flag);
  return idx !== -1 && args[idx + 1] ? args[idx + 1] : null;
}
const hasFlag = (flag) => args.includes(flag);

const TARGET_TOPIC = getArg('--topic');     // e.g. /art/aesthetics/rasa-theory/
const TARGET_SECTION = getArg('--section'); // e.g. rajasthani-painting
const TARGET_MODEL = getArg('--model') || 'gemini-3.5-flash-lite'; // Default model
const LIMIT = getArg('--limit') ? parseInt(getArg('--limit'), 10) : null;
const FORCE = hasFlag('--force');
const DRY_RUN = hasFlag('--dry-run');

// Status Tracking File
const STATUS_FILE = 'content-generation-status-art.json';
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
const INVENTORY_FILE = 'scratch/art_inventory.json';
if (!fs.existsSync(INVENTORY_FILE)) {
  console.error(`Inventory file not found at ${INVENTORY_FILE}. Run scratch/analyze_art_topics.mjs first.`);
  process.exit(1);
}
const inventory = JSON.parse(fs.readFileSync(INVENTORY_FILE, 'utf8'));

const tgtSequence = fs.existsSync('scratch/tgt_art_parsed.json')
  ? JSON.parse(fs.readFileSync('scratch/tgt_art_parsed.json'))
  : [];
const pgtSequence = fs.existsSync('scratch/pgt_art_parsed.json')
  ? JSON.parse(fs.readFileSync('scratch/pgt_art_parsed.json'))
  : [];

// Map section folders to clean Hindi and English titles
const SECTION_NAMES = {
  'aesthetics': { en: 'Aesthetics and Rasa Theory', hi: 'सौंदर्यशास्त्र एवं रस सिद्धांत' },
  'art-techniques-and-media': { en: 'Art Techniques and Media', hi: 'कला तकनीक, माध्यम एवं विधियां' },
  'bengal-school': { en: 'Bengal School of Art', hi: 'बंगाल शैली एवं पुनरुत्थान काल' },
  'colour-theory': { en: 'Colour Theory', hi: 'रंग सिद्धांत एवं वर्ण चक्र' },
  'company-school': { en: 'Company School (Patna Kalam)', hi: 'कंपनी शैली (पटना कलम)' },
  'contemporary-indian-art': { en: 'Contemporary Indian Art', hi: 'समकालीन भारतीय कला एवं प्रवृत्तियां' },
  'drawing-and-composition': { en: 'Drawing and Composition', hi: 'रेखांकन एवं संयोजन' },
  'elements-of-art': { en: 'Elements of Art (Shadanga)', hi: 'कला के छह मूलभूत तत्व' },
  'important-artists': { en: 'Prominent Artists and Masters', hi: 'प्रमुख भारतीय एवं पाश्चात्य चित्रकार' },
  'important-paintings-and-artworks': { en: 'Masterpieces and Artworks', hi: 'प्रसिद्ध चित्र एवं कलाकृतियां' },
  'indian-miniature-painting': { en: 'Indian Miniature Painting', hi: 'भारतीय लघुचित्रकला शैलियां' },
  'indian-mural-painting': { en: 'Indian Mural Painting (Ajanta, Ellora, Bagh)', hi: 'भारतीय भित्ति चित्रकला (अजंता, एलोरा, बाघ)' },
  'indian-painting-foundations': { en: 'Foundations of Indian Painting', hi: 'भारतीय चित्रकला की आधारशिला एवं षडांग' },
  'indus-valley-art': { en: 'Indus Valley Art and Civilization', hi: 'सिंधु घाटी सभ्यता की कला एवं शिल्प' },
  'modern-indian-art': { en: 'Modern Indian Art', hi: 'आधुनिक भारतीय चित्रकला' },
  'mughal-painting': { en: 'Mughal School of Painting', hi: 'मुगल चित्रकला शैली एवं दरबारी कला' },
  'pahari-painting': { en: 'Pahari School of Painting', hi: 'पहाड़ी चित्रकला शैली (कांगड़ा, बसोहली)' },
  'prehistoric-art': { en: 'Prehistoric Indian Rock Art', hi: 'प्रागैतिहासिक भारतीय शैलचित्रकला' },
  'principles-of-art-and-composition': { en: 'Principles of Art and Composition', hi: 'कला एवं संयोजन के सिद्धांत' },
  'rajasthani-painting': { en: 'Rajasthani School of Painting', hi: 'राजस्थानी चित्रकला शैली' },
  'western-art-history': { en: 'Western Art History', hi: 'पाश्चात्य कला का इतिहास' },
  'western-art-movements': { en: 'Western Art Movements', hi: 'पाश्चात्य कला आंदोलन एवं आधुनिक वाद' }
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
  // parts[0] is 'art', parts[1] is section
  const sectionKey = parts[1] || 'general';
  const sectionMeta = SECTION_NAMES[sectionKey] || { en: sectionKey, hi: sectionKey };

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
  const sectionPrefix = `/art/${sectionKey}/`;
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
 * Construct Gemini Prompt for Art (चित्रकला / रूपांकन)
 */
function buildPrompt(item, context) {
  const segs = item.url.split('/').filter(Boolean);
  const topicSlug = segs[segs.length - 1];
  const topicTitleGuess = topicSlug.split('-').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' ');

  return `
You are an eminent Professor of Fine Arts (चित्रकला), Art Historian, and Master Educator creating high-level, production-ready study material for UP TGT Art (प्रवक्ता/सहायक अध्यापक चित्रकला) and UP PGT Art competitive examinations in Uttar Pradesh.

Topic Details:
- Subject: Art / Drawing & Painting (चित्रकला)
- Section: ${context.sectionMeta.en} (${context.sectionMeta.hi})
- Topic Slug: ${topicSlug}
- Reference English Title: ${topicTitleGuess}
- Canonical URL: ${item.url}
- Exam Relevance: ${item.examRelevance} (UP TGT / UP PGT Art)

CRITICAL LANGUAGE GUIDELINES:
1. All core educational content MUST be in natural, academically rigorous, authentic Devanagari Hindi (शुद्ध, प्रामाणिक एवं मानक हिंदी).
2. Do NOT use Romanized Hindi (Hinglish).
3. Technical and art history English terms MUST appear in parentheses following the Hindi term where appropriate.
   Example: रूपभेद (Differentiation of Forms), भित्ति चित्रण (Mural Painting), टेम्परा (Tempera), जलरंग (Water Colour), वास पद्धति (Wash Technique), अंतराल (Space), स्वर्णिम विभाजन (Golden Section).
4. Terminology must strictly adhere to standard Indian Fine Arts curricula: NCERT, Lalit Kala Akademi, UGC NET Visual Arts, and Uttar Pradesh Secondary Education Service Selection Board (UPSESSB) TGT/PGT Art standards.
5. Provide rich depth: historical timeline, patron kings/dynasties (आश्रयदाता), stylistic characteristics (शैलीगत विशेषताएं), human figure proportions (मानव आकृतियों का अंकन), color schemes (रंग योजना), prominent paintings with their current museum locations (उदा. राष्ट्रीय संग्रहालय नई दिल्ली, भारत कला भवन वाराणसी, विक्टोरिया मेमोरियल कोलकाता), and exam traps.
6. NO FABRICATED PYQs: Do not include or invent any "Previous Year Questions".

OUTPUT FORMAT:
Respond with ONLY a valid, raw JSON object (no Markdown code block wrappers, no preamble) adhering to this schema:
{
  "title_hi": "पूर्ण हिंदी शीर्षक (English Title in Parentheses)",
  "short_intro": "विषय का 2-3 वाक्यों में सारगर्भित, परीक्षा-उन्मुख हिंदी परिचय।",
  "notes_sections": [
    {
      "heading": "H2 स्तर का हिंदी शीर्षक",
      "content_html": "<p>विस्तृत, प्रामाणिक व्याख्या...</p><ul><li>महत्वपूर्ण बिंदु...</li></ul>"
    }
  ],
  "comparison_tables": [
    {
      "title": "तालिका का शीर्षक (उदा. शैलियों / कलाकारों / माध्यमों की तुलना)",
      "headers": ["स्तंभ 1", "स्तंभ 2", "स्तंभ 3"],
      "rows": [
        ["डेटा 1", "डेटा 2", "डेटा 3"]
      ]
    }
  ],
  "mnemonics": [
    {
      "title": "स्मरण सूत्र / याद रखने की ट्रिक (उदा. शैलियों के क्रम या षडांग का सूत्र)",
      "trick": "सरल व रोचक याद रखने की ट्रिक / एक्रोनिम / तुकबंदी (Devanagari Hindi)",
      "explanation": "ट्रिक के प्रत्येक अक्षर/शब्द का विस्तृत अर्थ और परीक्षा में उपयोग"
    }
  ],
  "exam_points": [
    "परीक्षा के लिए अति-महत्वपूर्ण तथ्य 1 (सन, स्थान, संग्रहालय, खोजकर्ता आदि)",
    "परीक्षा के लिए अति-महत्वपूर्ण तथ्य 2"
  ],
  "common_errors": [
    "विद्यार्थियों द्वारा की जाने वाली सामान्य गलती एवं उसका सही ऐतिहासिक/कलात्मक तथ्य"
  ],
  "chapter_summary_concepts": [
    {
      "concept_num": "संकल्पना 1",
      "concept_title": "संकल्पना का शीर्षक (English Title in Parentheses)",
      "concept_body_html": "<p>गहन सैद्धांतिक सार...</p><ul><li><span class=\"summary-highlight-pill\">मुख्य शब्द</span>: स्पष्टीकरण व मानक...</li></ul>"
    }
  ],
  "quick_revision": {
    "terms_glossary": [
      {
        "term": "मुख्य कला पद / शब्दावली",
        "term_en": "English Term",
        "definition": "1-2 वाक्यों में अत्यंत सटीक, प्रामाणिक परिभाषा जो संपूर्ण अवधारणा स्पष्ट करे।"
      }
    ],
    "summary": [
      "त्वरित सारांश बिंदु 1",
      "त्वरित सारांश बिंदु 2"
    ],
    "must_remember": [
      "परीक्षा के लिए अनिवार्य बिंदु 1",
      "परीक्षा के लिए अनिवार्य बिंदु 2"
    ],
    "common_confusions": [
      {
        "term_a": "पद A (उदा. कांगड़ा शैली)",
        "term_b": "पद B (उदा. बसोहली शैली)",
        "difference": "दोनों के मध्य स्पष्ट अंतर"
      }
    ]
  },
  "quiz": [
    {
      "question": "अवधारणात्मक एवं ट्रिकी बहुविकल्पीय प्रश्न (हिंदी में)?",
      "options": ["विकल्प A", "विकल्प B", "विकल्प C", "विकल्प D"],
      "correct_index": 0,
      "hint": "संकेत जो गहरी कलात्मक समझ विकसित करे",
      "explanation": "विस्तृत एवं प्रामाणिक हिंदी व्याख्या जिसमें यह भी स्पष्ट हो कि अन्य विकल्प क्यों अनुचित हैं।"
    }
  ],
  "topic_test": [
    {
      "question": "परीक्षा स्तरीय बहुविकल्पीय प्रश्न (हिंदी में)?",
      "options": ["विकल्प A", "विकल्प B", "विकल्प C", "विकल्प D"],
      "correct_index": 0,
      "explanation": "विस्तृत परीक्षा-उन्मुख समाधान एवं व्याख्या।",
      "difficulty": "TGT"
    }
  ],
  "pyq_pattern_practice": [
    {
      "question": "विगत वर्षों के पैटर्न पर आधारित अभ्यास प्रश्न?",
      "options": ["विकल्प A", "विकल्प B", "विकल्प C", "विकल्प D"],
      "correct_index": 0,
      "explanation": "विस्तृत समाधान।",
      "note": "अभ्यास प्रश्न — यह वास्तविक PYQ नहीं है"
    }
  ]
}

REQUIREMENTS:
- 'notes_sections': Provide 4 to 6 substantial sections covering historical context, techniques, mediums, styles, major paintings, and examination questions.
- 'mnemonics': Provide 1 to 3 memorable memory tricks in Hindi to easily remember complex artistic classifications, artist lineages, or techniques.
- 'chapter_summary_concepts': Provide 4 to 6 comprehensive, point-by-point concept blocks (संकल्पना 1, संकल्पना 2...) formatted exactly as found in standard academic Art textbook end-of-chapter master summaries. Include all definitions, classifications, techniques, color palettes, and comparison points.
- 'terms_glossary': Under 'quick_revision', provide 10 to 12 concise technical art terms defining EVERY vital concept of this topic.
- 'quiz': Provide exactly 18 to 20 TRICKY, high-yield conceptual MCQs covering EVERY single major concept in the notes. Design the quiz such that by solving these questions alone, the student's entire notes and concepts are 100% revised and learned.
- 'topic_test': Provide exactly 10 unique, challenging MCQs with TGT/PGT difficulty.
- 'pyq_pattern_practice': Provide exactly 4 to 5 pattern practice MCQs.
- All MCQ arrays MUST have exactly 4 options per question, with 'correct_index' an integer from 0 to 3.
`;
}

/**
 * Validate Gemini JSON Output
 */
function validateContent(data) {
  if (!data || typeof data !== 'object') throw new Error('Root output is not an object');
  if (!data.title_hi || typeof data.title_hi !== 'string') throw new Error('Missing title_hi');
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
  data.quiz.forEach((q, i) => {
    if (!q.question || !Array.isArray(q.options) || q.options.length !== 4) {
      throw new Error(`Quiz question ${i + 1} has invalid question or options length`);
    }
    if (typeof q.correct_index !== 'number' || q.correct_index < 0 || q.correct_index > 3) {
      throw new Error(`Quiz question ${i + 1} has invalid correct_index: ${q.correct_index}`);
    }
  });

  // Validate topic_test
  if (!data.topic_test || !Array.isArray(data.topic_test) || data.topic_test.length < 8) {
    throw new Error(`topic_test must have at least 8 questions (found: ${data.topic_test?.length || 0})`);
  }
  data.topic_test.forEach((q, i) => {
    if (!q.question || !Array.isArray(q.options) || q.options.length !== 4) {
      throw new Error(`Topic test question ${i + 1} has invalid question or options length`);
    }
    if (typeof q.correct_index !== 'number' || q.correct_index < 0 || q.correct_index > 3) {
      throw new Error(`Topic test question ${i + 1} has invalid correct_index: ${q.correct_index}`);
    }
  });

  return true;
}

/**
 * Convert structured data into static, accessible HTML
 */
function renderTopicHtml(item, context, data) {
  const title = `${data.title_hi}: नोट्स, MCQ, PYQ और Topic Test | Art (चित्रकला) | SJ Maths`;
  const metaDesc = `UP TGT और UP PGT कला / चित्रकला (Drawing & Painting) परीक्षा के लिए ${data.title_hi} के विस्तृत नोट्स, अध्याय सारांश, 10-मिनट मॉक टेस्ट और 20 अभ्यास क्विज़ प्रश्न।`;
  const canonicalUrl = `https://sjmaths.com${item.url}`;

  // Exam badges markup
  const isTgt = item.inTgt || item.examRelevance === 'Both' || (item.examRelevance && item.examRelevance.includes('TGT'));
  const isPgt = item.inPgt || item.examRelevance === 'Both' || (item.examRelevance && item.examRelevance.includes('PGT'));

  let examBadgesHtml = '';
  if (isTgt && isPgt) {
    examBadgesHtml = `
      <a class="exam-chip both" href="/up-tgt-art/">UP TGT Art Tracker →</a>
      <a class="exam-chip both" href="/up-pgt-art/">UP PGT Art Tracker →</a>
    `;
  } else if (isTgt) {
    examBadgesHtml = `<a class="exam-chip tgt" href="/up-tgt-art/">UP TGT Art Tracker →</a>`;
  } else if (isPgt) {
    examBadgesHtml = `<a class="exam-chip pgt" href="/up-pgt-art/">UP PGT Art Tracker →</a>`;
  }

  // Comparison Tables HTML
  let tablesHtml = '';
  if (data.comparison_tables && Array.isArray(data.comparison_tables) && data.comparison_tables.length > 0) {
    tablesHtml = data.comparison_tables.map(tbl => `
      <div class="card">
        <h2>📊 ${tbl.title}</h2>
        <div class="concept-table-wrap">
          <table class="concept-table">
            <thead>
              <tr>
                ${tbl.headers.map(h => `<th>${h}</th>`).join('')}
              </tr>
            </thead>
            <tbody>
              ${tbl.rows.map(row => `
                <tr>
                  ${row.map(cell => `<td>${cell}</td>`).join('')}
                </tr>
              `).join('')}
            </tbody>
          </table>
        </div>
      </div>
    `).join('');
  }

  // Notes Sections HTML
  const notesSectionsHtml = data.notes_sections.map(sec => `
    <article class="card">
      <h2>${sec.heading}</h2>
      ${sec.content_html}
    </article>
  `).join('\n');

  // Mnemonics & Memory Tricks HTML
  let mnemonicsHtml = '';
  if (data.mnemonics && Array.isArray(data.mnemonics) && data.mnemonics.length > 0) {
    mnemonicsHtml = `
      <div class="card">
        <h2>💡 स्मरण सूत्र एवं याद रखने की ट्रिक्स (Mnemonics & Memory Tricks)</h2>
        <p style="color:var(--muted);font-size:0.88rem;margin-bottom:14px;">परीक्षा में जटिल शैलियों, चित्रकारों और कला सिद्धांतों को सरलता से याद रखने के लिए विशेष ट्रिक्स:</p>
        ${data.mnemonics.map(m => `
          <div class="mnemonic-box">
            <div class="mnemonic-header">💡 ${m.title}</div>
            <div class="mnemonic-trick">${m.trick}</div>
            <p class="mnemonic-desc">${m.explanation}</p>
          </div>
        `).join('')}
      </div>
    `;
  }

  // Exam tips HTML
  let examTipsHtml = '';
  if (data.exam_points && data.exam_points.length > 0) {
    examTipsHtml = `
      <div class="exam-tips">
        <div class="exam-tips-title">🎯 परीक्षा के लिए महत्वपूर्ण तथ्य (Key Exam Points)</div>
        <ul>
          ${data.exam_points.map(p => `<li>${p}</li>`).join('')}
        </ul>
      </div>
    `;
  }

  // Common errors HTML
  let commonErrorsHtml = '';
  if (data.common_errors && data.common_errors.length > 0) {
    commonErrorsHtml = `
      <div class="common-errors">
        <div class="common-errors-title">⚠️ सामान्य गलतियाँ एवं भ्रांतियाँ (Common Pitfalls)</div>
        <ul>
          ${data.common_errors.map(err => `<li>${err}</li>`).join('')}
        </ul>
      </div>
    `;
  }

  // Chapter Summary Concepts HTML (Textbook End-of-Chapter Summary)
  let chapterSummaryHtml = '';
  if (data.chapter_summary_concepts && Array.isArray(data.chapter_summary_concepts) && data.chapter_summary_concepts.length > 0) {
    chapterSummaryHtml = data.chapter_summary_concepts.map((c, idx) => `
      <div class="summary-concept-block">
        <div class="summary-concept-header">
          <span class="summary-concept-num">${c.concept_num || `संकल्पना ${idx + 1}`}</span>
          <span class="summary-concept-title">${c.concept_title}</span>
        </div>
        <div class="summary-concept-body">
          ${c.concept_body_html}
        </div>
      </div>
    `).join('\n');
  }

  // Quick Revision HTML
  const rev = data.quick_revision || {};
  const revSummaryHtml = (rev.summary || []).map(s => `<li>${s}</li>`).join('');
  const revMustRememberHtml = (rev.must_remember || []).map(m => `<li>${m}</li>`).join('');

  // Terms Glossary HTML
  let termsGlossaryHtml = '';
  if (rev.terms_glossary && Array.isArray(rev.terms_glossary) && rev.terms_glossary.length > 0) {
    termsGlossaryHtml = `
      <div class="card terms-glossary-section">
        <h2>📚 मुख्य कला शब्दावली एवं अवधारणाएं (Core Art Terms & Concepts)</h2>
        <p style="color:var(--muted);font-size:0.86rem;margin-bottom:12px;">इस टॉपिक के समस्त मुख्य कला पदों, माध्यमों एवं शैलियों का त्वरित संक्षिप्त सार:</p>
        <div class="terms-glossary-grid">
          ${rev.terms_glossary.map(t => `
            <div class="term-card">
              <div class="term-card-head">
                <span class="term-card-title">${t.term}</span>
                ${t.term_en ? `<span class="term-card-en">(${t.term_en})</span>` : ''}
              </div>
              <p class="term-card-def">${t.definition}</p>
            </div>
          `).join('')}
        </div>
      </div>
    `;
  }

  let confusionsHtml = '';
  if (rev.common_confusions && rev.common_confusions.length > 0) {
    confusionsHtml = `
      <div class="confusion-card">
        <h3>🔍 इनमें भ्रम न करें (Do Not Confuse)</h3>
        <div class="rev-list">
          ${rev.common_confusions.map(c => `
            <div style="margin-bottom:12px;padding-bottom:10px;border-bottom:1px dashed var(--line);">
              <strong style="color:var(--brand);">${c.term_a} बनाम ${c.term_b}:</strong>
              <p style="margin:4px 0 0;font-size:0.88rem;color:var(--ink2);">${c.difference}</p>
            </div>
          `).join('')}
        </div>
      </div>
    `;
  }

  // PYQ Pattern Practice HTML
  let pyqPatternHtml = '';
  if (data.pyq_pattern_practice && data.pyq_pattern_practice.length > 0) {
    pyqPatternHtml = `
      <div class="pyq-practice-section">
        <div class="pyq-practice-header">
          <div>
            <strong style="color:#854d0e;font-size:1rem;">PYQ पैटर्न अभ्यास प्रश्न (Pattern Practice)</strong>
            <span style="color:#a16207;font-size:0.8rem;display:block;">विगत वर्षों के प्रश्न पत्रों के पैटर्न पर आधारित अभ्यास</span>
          </div>
          <span class="pyq-practice-badge">अभ्यास प्रश्न — यह वास्तविक PYQ नहीं है</span>
        </div>

        ${data.pyq_pattern_practice.map((q, qIdx) => `
          <div class="card" style="margin-bottom:16px;">
            <div style="display:flex;justify-content:space-between;margin-bottom:8px;">
              <span class="quiz-qno">पैटर्न प्रश्न ${qIdx + 1}</span>
              <span style="font-size:0.72rem;background:#fef08a;color:#854d0e;padding:2px 8px;border-radius:4px;font-weight:700;">पैटर्न आधारित</span>
            </div>
            <p style="font-weight:700;color:var(--ink);margin-bottom:14px;">${q.question}</p>
            <div class="quiz-options">
              ${q.options.map((opt, oIdx) => `
                <div class="quiz-opt" style="cursor:default;">
                  <span class="quiz-opt-letter">${['A', 'B', 'C', 'D'][oIdx]}</span>
                  <span>${opt}</span>
                  ${oIdx === q.correct_index ? '<strong style="margin-left:auto;color:var(--success);font-size:0.8rem;">(सही उत्तर)</strong>' : ''}
                </div>
              `).join('')}
            </div>
            <div class="quiz-feedback show correct" style="margin-top:12px;">
              <strong>व्याख्या:</strong> ${q.explanation}
            </div>
          </div>
        `).join('')}
      </div>
    `;
  }

  // Related topics links
  const relatedHtml = context.related.map(r => `
    <a class="related-link" href="${r.url}">
      <span>${r.title}</span>
      <span>→</span>
    </a>
  `).join('');

  // Previous & Next navigation
  const prevNextHtml = `
    <nav class="topic-sequence-nav" aria-label="Topic Sequence">
      ${context.prevTopic ? `
        <a class="seq-card prev" href="${context.prevTopic.href}">
          <span class="seq-label">← पिछला टॉपिक (Previous)</span>
          <span class="seq-title">${context.prevTopic.title}</span>
        </a>
      ` : '<div></div>'}
      ${context.nextTopic ? `
        <a class="seq-card next" href="${context.nextTopic.href}">
          <span class="seq-label">अगला टॉपिक (Next) →</span>
          <span class="seq-title">${context.nextTopic.title}</span>
        </a>
      ` : '<div></div>'}
    </nav>
  `;

  // Inline JSON for instant fallback
  const inlineQuizJson = JSON.stringify(data.quiz).replace(/</g, '\\u003c');
  const inlineTestJson = JSON.stringify(data.topic_test).replace(/</g, '\\u003c');

  return `<!doctype html>
<html lang="hi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>${title}</title>
<meta name="description" content="${metaDesc}">
<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1">
<meta name="author" content="SJ Maths">
<meta name="theme-color" content="#16324f">
<link rel="canonical" href="${canonicalUrl}">
<link rel="icon" type="image/png" href="/favicon.png">

<!-- Open Graph -->
<meta property="og:type" content="article">
<meta property="og:site_name" content="SJ Maths">
<meta property="og:title" content="${title}">
<meta property="og:description" content="${metaDesc}">
<meta property="og:url" content="${canonicalUrl}">
<meta property="og:locale" content="hi_IN">

<!-- Structured Data (JSON-LD) -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LearningResource",
  "name": "${data.title_hi}",
  "headline": "${data.title_hi} — UP TGT/PGT Art Study Notes & Topic Test",
  "description": "${metaDesc}",
  "url": "${canonicalUrl}",
  "inLanguage": "hi",
  "learningResourceType": "Study Guide / Quiz",
  "educationalLevel": "Post-Secondary / Teacher Eligibility Examination",
  "isPartOf": {
    "@type": "WebSite",
    "name": "SJ Maths",
    "url": "https://sjmaths.com/"
  },
  "breadcrumb": {
    "@type": "BreadcrumbList",
    "itemListElement": [
      {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://sjmaths.com/"},
      {"@type": "ListItem", "position": 2, "name": "Art", "item": "https://sjmaths.com/art/"},
      {"@type": "ListItem", "position": 3, "name": "${context.sectionMeta.en}", "item": "https://sjmaths.com/art/${context.sectionKey}/"},
      {"@type": "ListItem", "position": 4, "name": "${data.title_hi}", "item": "${canonicalUrl}"}
    ]
  }
}
</script>

<!-- Stylesheets -->
<link rel="stylesheet" href="/assets/css/topic-page.css">
</head>
<body>

<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="https://sjmaths.com/">
      <span class="brand-mark">&int;</span>
      <span>
        <span class="brand-name">SJ Maths</span>
        <span class="brand-sub">Art (चित्रकला) Master Study System</span>
      </span>
    </a>
    <div class="header-actions">
      <button type="button" class="theme-toggle-btn" id="btn-theme-toggle" aria-label="थीम बदलें">🌙 रात्रि मोड</button>
      ${isTgt ? '<a class="back-btn" href="/up-tgt-art/">← UP TGT Tracker</a>' : ''}
      ${isPgt ? '<a class="back-btn" href="/up-pgt-art/">← UP PGT Tracker</a>' : ''}
    </div>
  </div>
</header>

<main class="wrap">
  <!-- Hero Section -->
  <section class="hero">
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="https://sjmaths.com/">Home</a>
      <span class="breadcrumb-sep">›</span>
      <a href="/art/">Art (चित्रकला)</a>
      <span class="breadcrumb-sep">›</span>
      <a href="/art/${context.sectionKey}/">${context.sectionMeta.en} (${context.sectionMeta.hi})</a>
      <span class="breadcrumb-sep">›</span>
      <span class="breadcrumb-current">${data.title_hi}</span>
    </nav>

    <div class="kicker">${context.sectionMeta.en} • ${context.sectionMeta.hi}</div>
    <h1>${data.title_hi}</h1>
    <p class="lead">${data.short_intro}</p>

    <div class="hero-meta-row">
      <div class="exam-badges">
        <span class="exam-badges-label">संबंधित परीक्षा (Exams):</span>
        ${examBadgesHtml}
      </div>

      <div class="topic-progress-wrap">
        <span class="topic-progress-label">टॉपिक प्रगति:</span>
        <div class="topic-progress-bar">
          <div class="topic-progress-fill"></div>
        </div>
        <span class="topic-progress-pct">0%</span>
      </div>
    </div>
  </section>

  <!-- Accessible Tab Navigation Bar -->
  <div class="tabs-container">
    <div class="topic-tablist" role="tablist" aria-label="Topic Study Sections">
      <button type="button" class="tab-btn" role="tab" id="tab-notes" aria-selected="true" aria-controls="notes" tabindex="0">
        <span>📖</span> <span>नोट्स</span>
      </button>
      <button type="button" class="tab-btn" role="tab" id="tab-revision" aria-selected="false" aria-controls="revision" tabindex="-1">
        <span>📖</span> <span>अध्याय सारांश</span>
      </button>
      <button type="button" class="tab-btn" role="tab" id="tab-quiz" aria-selected="false" aria-controls="quiz" tabindex="-1">
        <span>🎯</span> <span>अभ्यास क्विज़</span> <span class="tab-badge">${data.quiz.length}</span>
      </button>
      <button type="button" class="tab-btn" role="tab" id="tab-pyqs" aria-selected="false" aria-controls="pyqs" tabindex="-1">
        <span>📑</span> <span>पिछले वर्षों के प्रश्न</span>
      </button>
      <button type="button" class="tab-btn" role="tab" id="tab-topic-test" aria-selected="false" aria-controls="topic-test" tabindex="-1">
        <span>⏱️</span> <span>टॉपिक टेस्ट</span> <span class="tab-badge">${data.topic_test.length}Q</span>
      </button>
    </div>
  </div>

  <!-- Tab Panels & Main Grid Layout -->
  <div class="main-grid">
    <div class="content-col">

      <!-- TAB 1: NOTES -->
      <section id="notes" class="tab-panel active" role="tabpanel" aria-labelledby="tab-notes">
        ${notesSectionsHtml}
        ${tablesHtml}
        ${mnemonicsHtml}
        ${examTipsHtml}
        ${commonErrorsHtml}

        <div class="completion-action">
          <div>
            <strong style="color:var(--brand);font-size:0.95rem;display:block;">क्या आपने यह नोट्स पूर्ण पढ़ लिए हैं?</strong>
            <span style="color:var(--muted);font-size:0.8rem;">प्रगति ट्रैक करने के लिए पूर्ण चिह्नित करें।</span>
          </div>
          <button type="button" class="completion-btn" id="btn-mark-notes-complete">
            मार्क नोट्स पूर्ण (Mark Completed)
          </button>
        </div>
      </section>

      <!-- TAB 2: TEXTBOOK CHAPTER SUMMARY -->
      <section id="revision" class="tab-panel" role="tabpanel" aria-labelledby="tab-revision" hidden>
        <div class="summary-banner">
          <div class="summary-banner-badge">📖 पाठ्यपुस्तक अध्याय सारांश • Points to Remember</div>
          <h2>${data.title_hi} — संपूर्ण अध्याय का सार</h2>
          <p>मानक चित्रकला एवं ललित कला पाठ्यपुस्तकों के अंतिम सारांश पृष्ठों के अनुरूप — इस अध्याय के सभी सिद्धांतों, शैलियों, तकनीकों, प्रमुख कलाकृतियों एवं परीक्षा उपयोगी तथ्यों का संपूर्ण संकलन।</p>
        </div>

        ${chapterSummaryHtml ? `
        <div class="card">
          <h2>📌 अध्याय के मुख्य सैद्धांतिक बिंदु (Comprehensive Concept Review)</h2>
          ${chapterSummaryHtml}
        </div>
        ` : ''}

        ${tablesHtml}
        ${termsGlossaryHtml}

        <div class="revision-strip">
          <div class="rev-card">
            <h3>⚡ त्वरित सारांश (Key Takeaways)</h3>
            <ul class="rev-list">
              ${revSummaryHtml}
            </ul>
          </div>

          <div class="must-remember-card">
            <h3>🎯 परीक्षा में याद रखें (Must Remember for Exams)</h3>
            <ul class="rev-list">
              ${revMustRememberHtml}
            </ul>
          </div>

          ${confusionsHtml}
        </div>

        <div class="completion-action">
          <div>
            <strong style="color:var(--brand);font-size:0.95rem;display:block;">अध्याय सारांश पुनरावृत्ति संपन्न?</strong>
            <span style="color:var(--muted);font-size:0.8rem;">अपनी तैयारी की प्रगति को अपडेट करें।</span>
          </div>
          <button type="button" class="completion-btn" id="btn-mark-rev-complete">
            मार्क सारांश पूर्ण (Mark Summary Done)
          </button>
        </div>
      </section>

      <!-- TAB 3: PRACTICE QUIZ -->
      <section id="quiz" class="tab-panel" role="tabpanel" aria-labelledby="tab-quiz" hidden>
        <div id="quiz-container"></div>
      </section>

      <!-- TAB 4: PYQs (Strictly No Fabricated PYQs) -->
      <section id="pyqs" class="tab-panel" role="tabpanel" aria-labelledby="tab-pyqs" hidden>
        <div class="pyq-disclaimer-card">
          <div class="pyq-disclaimer-icon">📑</div>
          <h3>सत्यापित PYQ सूचना</h3>
          <p>इस टॉपिक के लिए सत्यापित पिछले वर्ष का प्रश्न अभी उपलब्ध नहीं है।</p>
          <p style="margin-top:8px;font-size:0.82rem;color:var(--muted);">
            जैसे ही उत्तर प्रदेश माध्यमिक शिक्षा सेवा चयन बोर्ड द्वारा आयोजित UP TGT / UP PGT कला के आधिकारिक प्रमाणित प्रश्न उपलब्ध होंगे, उन्हें यहाँ अद्यतन किया जाएगा।
          </p>
        </div>

        ${pyqPatternHtml}
      </section>

      <!-- TAB 5: TOPIC TEST -->
      <section id="topic-test" class="tab-panel" role="tabpanel" aria-labelledby="tab-topic-test" hidden>
        <div id="topic-test-container"></div>
      </section>

      <!-- Sequence Nav -->
      ${prevNextHtml}

    </div>

    <!-- Sidebar Column -->
    <aside class="sidebar-col">
      <div class="sidebar-card">
        <h3>पाठ्यक्रम ट्रैकर</h3>
        ${isTgt ? `
          <div class="exam-action-box">
            <strong>UP TGT Art (चित्रकला)</strong>
            <p>48 टॉपिकों की व्यवस्थित सिलेबस चेकलिस्ट एवं ट्रैकिंग।</p>
            <a class="exam-action-link" href="/up-tgt-art/">ओपन ट्रैकर →</a>
          </div>
        ` : ''}
        ${isPgt ? `
          <div class="exam-action-box">
            <strong>UP PGT Art (चित्रकला)</strong>
            <p>43 टॉपिकों का संपूर्ण सिलेबस व प्रगति ट्रैकर।</p>
            <a class="exam-action-link" href="/up-pgt-art/">ओपन ट्रैकर →</a>
          </div>
        ` : ''}
      </div>

      <div class="sidebar-card">
        <h3>संबंधित टॉपिक</h3>
        <div class="related-list">
          ${relatedHtml}
        </div>
      </div>
    </aside>
  </div>
</main>

<footer class="site-footer">
  <div class="wrap footer-inner">
    <span>SJ Maths • Master Subject Library • ${data.title_hi}</span>
    <div class="footer-links">
      <a href="https://sjmaths.com/">Home</a>
      <a href="/art/">Art</a>
      <a href="/up-tgt-art/">UP TGT Art</a>
      <a href="/up-pgt-art/">UP PGT Art</a>
    </div>
  </div>
</footer>

<!-- Embedded Question Datasets -->
<script>
window.HOME_SCIENCE_QUIZ_DATA = ${inlineQuizJson};
window.HOME_SCIENCE_TEST_DATA = ${inlineTestJson};
</script>

<!-- Shared Reusable JavaScript Engines -->
<script src="/assets/js/progress.js"></script>
<script src="/assets/js/topic-page.js"></script>
<script src="/assets/js/quiz-engine.js"></script>
<script src="/assets/js/topic-test-engine.js"></script>

</body>
</html>
`;
}

/**
 * Generate one topic
 */
async function processTopic(item) {
  const context = getTopicContext(item);
  console.log(`\n------------------------------------------------------------`);
  console.log(`Processing Topic: ${item.url}`);
  console.log(`Section: ${context.sectionMeta.en} (${context.sectionMeta.hi}) | Relevance: ${item.examRelevance}`);

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
  const maxRetries = 3;

  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try {
      console.log(`Calling Gemini API [Model: ${TARGET_MODEL}] (Attempt ${attempt}/${maxRetries})...`);
      const response = await ai.models.generateContent({
        model: TARGET_MODEL,
        contents: prompt,
        config: {
          responseMimeType: 'application/json',
          temperature: 0.3
        }
      });

      rawJsonText = response.text;
      try {
        parsedData = JSON.parse(rawJsonText);
      } catch (jsonErr) {
        console.warn('Initial JSON.parse failed, attempting jsonrepair...');
        parsedData = JSON.parse(jsonrepair(rawJsonText));
      }

      validateContent(parsedData);
      console.log(`✓ Content validated successfully for: ${parsedData.title_hi}`);
      break;
    } catch (err) {
      console.error(`Attempt ${attempt} failed:`, err.message);
      if (attempt === maxRetries) {
        statusMap[item.url] = {
          status: 'validation_failed',
          error: err.message,
          failedAt: new Date().toISOString()
        };
        saveStatus();
        return false;
      }
      // Wait before retry
      await new Promise(r => setTimeout(r, 2000 * attempt));
    }
  }

  // Backup existing file if exists
  const targetDir = path.resolve(item.dir);
  const targetHtmlPath = path.join(targetDir, 'index.html');

  if (fs.existsSync(targetHtmlPath)) {
    const backupPath = path.join(targetDir, 'index.html.backup-before-content-generation');
    if (!fs.existsSync(backupPath)) {
      fs.copyFileSync(targetHtmlPath, backupPath);
      console.log(`Created backup: ${backupPath}`);
    }
  } else {
    fs.mkdirSync(targetDir, { recursive: true });
  }

  // Write question JSON files
  const quizPath = path.join(targetDir, 'quiz.json');
  fs.writeFileSync(quizPath, JSON.stringify(parsedData.quiz, null, 2), 'utf8');

  const testPath = path.join(targetDir, 'topic-test.json');
  fs.writeFileSync(testPath, JSON.stringify(parsedData.topic_test, null, 2), 'utf8');

  // Render & write HTML
  const finalHtml = renderTopicHtml(item, context, parsedData);
  fs.writeFileSync(targetHtmlPath, finalHtml, 'utf8');
  console.log(`✓ Successfully saved: ${targetHtmlPath}`);

  // Count words
  const wordCount = (finalHtml.match(/[\u0900-\u097F\w]+/g) || []).length;

  statusMap[item.url] = {
    status: 'completed',
    title: parsedData.title_hi,
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
  console.log('=== SJ Maths Art (चित्रकला) Content Generator Pipeline ===');
  const eligible = getEligibleTopics();
  console.log(`Eligible topics found: ${eligible.length}`);

  const toProcess = LIMIT ? eligible.slice(0, LIMIT) : eligible;
  console.log(`Topics scheduled to process: ${toProcess.length}`);

  let successCount = 0;
  for (let i = 0; i < toProcess.length; i++) {
    const item = toProcess[i];
    console.log(`\n[${i + 1}/${toProcess.length}] Starting: ${item.url}`);
    const ok = await processTopic(item);
    if (ok) successCount++;

    // Polite rate limit delay between calls
    if (i < toProcess.length - 1 && !DRY_RUN) {
      console.log('Cooling down 2 seconds...');
      await new Promise(r => setTimeout(r, 2000));
    }
  }

  console.log('\n============================================================');
  console.log(`Finished processing. Successfully completed: ${successCount}/${toProcess.length}`);
}

main().catch(err => {
  console.error('Fatal Generator Error:', err);
  process.exit(1);
});
