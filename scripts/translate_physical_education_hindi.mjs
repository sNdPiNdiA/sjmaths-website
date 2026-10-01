#!/usr/bin/env node
/**
 * ============================================================================
 * SJ Maths — Physical Education Hindi Translation & Bilingual Pipeline
 * Powered by Google Gemini API via @google/genai SDK
 * Model: gemini-3.1-flash-lite (with fallback to gemini-3.5-flash-lite)
 *
 * Performs FULL-FIDELITY, unshortened 1:1 translation of English study notes
 * into academic Hindi, and embeds a persistent language toggle (English / हिन्दी)
 * with zero-flicker localStorage state.
 * ============================================================================
 */

import fs from 'node:fs';
import path from 'node:path';
import 'dotenv/config';
import { GoogleGenAI } from '@google/genai';
import { jsonrepair } from 'jsonrepair';

const ROOT = process.cwd();
const DOMAIN = 'https://sjmaths.com';
const STATUS_FILE = path.join(ROOT, 'content-translation-status-pe-hindi.json');

// 1. Parse command line arguments
const args = process.argv.slice(2);
const DRY_RUN = args.includes('--dry-run');
const FORCE = args.includes('--force');
const LIMIT = (() => {
  const idx = args.indexOf('--limit');
  return idx !== -1 && args[idx + 1] ? parseInt(args[idx + 1], 10) : null;
})();
const TARGET_TOPIC = (() => {
  const idx = args.indexOf('--topic');
  return idx !== -1 && args[idx + 1] ? args[idx + 1] : null;
})();
const MODEL_NAME = (() => {
  const idx = args.indexOf('--model');
  return idx !== -1 && args[idx + 1] ? args[idx + 1] : 'gemini-3.1-flash-lite';
})();

const FALLBACK_MODELS = [MODEL_NAME, 'gemini-3.5-flash-lite'];

const apiKeys = [...new Set([
  process.env.GEMINI_API_KEY_1,
  process.env.GEMINI_API_KEY_2,
  process.env.GEMINI_API_KEY
].filter(Boolean))];

if (apiKeys.length === 0) {
  console.error('ERROR: No GEMINI API key found in .env.');
  process.exit(1);
}

const aiClients = apiKeys.map((key, i) => ({
  id: i + 1,
  preview: key.substring(0, 8) + '...' + key.slice(-4),
  client: new GoogleGenAI({ apiKey: key })
}));
let clientIndex = 0;
function getAiClient() {
  const c = aiClients[clientIndex % aiClients.length];
  clientIndex++;
  return c;
}

// 2. Load translation status tracking
let statusMap = {};
if (fs.existsSync(STATUS_FILE)) {
  try {
    statusMap = JSON.parse(fs.readFileSync(STATUS_FILE, 'utf8'));
  } catch {
    statusMap = {};
  }
}
function saveStatus() {
  fs.writeFileSync(STATUS_FILE, JSON.stringify(statusMap, null, 2), 'utf8');
}

// 3. Extract syllabus topics
function extractSyllabus(filePath) {
  const full = path.join(ROOT, filePath);
  if (!fs.existsSync(full)) return [];
  const content = fs.readFileSync(full, 'utf8');
  const match = content.match(/const syllabus = (\[[\s\S]*?\]);/);
  if (!match) return [];
  try {
    return JSON.parse(match[1]);
  } catch {
    return [];
  }
}

const tgtSyllabus = extractSyllabus('up-tgt-physical-education/index.html');
const pgtSyllabus = extractSyllabus('up-pgt-physical-education/index.html');

const topicsMap = new Map();

for (const unit of tgtSyllabus) {
  for (const [groupTitle, items] of unit.groups) {
    for (const [name, href] of items) {
      const cleanHref = href.startsWith('/') ? href : '/' + href;
      if (!topicsMap.has(cleanHref)) {
        topicsMap.set(cleanHref, {
          name,
          href: cleanHref,
          tgtUnit: unit.unit,
          tgtUnitTitle: unit.title,
          groupTitle,
          inTgt: true,
          inPgt: false
        });
      }
    }
  }
}

for (const unit of pgtSyllabus) {
  for (const [groupTitle, items] of unit.groups) {
    for (const [name, href, coverage] of items) {
      const cleanHref = href.startsWith('/') ? href : '/' + href;
      if (!topicsMap.has(cleanHref)) {
        topicsMap.set(cleanHref, {
          name,
          href: cleanHref,
          pgtUnit: unit.unit,
          pgtUnitTitle: unit.title,
          groupTitle,
          inTgt: coverage === 'full',
          inPgt: true
        });
      } else {
        const item = topicsMap.get(cleanHref);
        item.inPgt = true;
        item.pgtUnit = unit.unit;
        item.pgtUnitTitle = unit.title;
      }
    }
  }
}

const allTopics = Array.from(topicsMap.values());

const SECTION_TITLES = {
  'foundations-history-and-philosophy': 'Foundations, History & Philosophy of Physical Education',
  'teaching-organization-and-administration': 'Methods, Organization & Administration in Physical Education',
  'anatomy-and-physiology': 'Human Anatomy & Exercise Physiology',
  'kinesiology-and-biomechanics': 'Kinesiology & Biomechanics of Human Movement',
  'sports-psychology-and-sociology': 'Sports Psychology & Sports Sociology',
  'sports-injuries-and-rehabilitation': 'Sports Injuries, First Aid & Athletic Rehabilitation',
  'health-and-nutrition': 'Health Education, Lifestyle Diseases & Sports Nutrition',
  'sports-training-and-fitness': 'Principles of Sports Training & Physical Fitness',
  'tests-measurement-and-evaluation': 'Tests, Measurement & Evaluation in Physical Education',
  'yoga': 'Yoga Education, Asanas & Wellness',
  'sports-rules-measurements-and-equipment': 'Rules, Dimensions & Equipment of Major Sports',
  'sports-general-knowledge': 'Sports General Knowledge, Awards & Personalities',
  'growth-and-development': 'Human Growth, Motor Development & Age Characteristics',
  'research-methods-and-statistics': 'Research Methods & Applied Statistics in Physical Education'
};

const SECTION_TITLES_HI = {
  'foundations-history-and-philosophy': 'शारीरिक शिक्षा के आधार, इतिहास एवं दर्शन',
  'teaching-organization-and-administration': 'शिक्षण विधियां, संगठन एवं प्रशासन',
  'anatomy-and-physiology': 'मानव शरीर रचना एवं व्यायाम कार्यिकी',
  'kinesiology-and-biomechanics': 'किनेसियोलॉजी एवं जैव-यांत्रिकी',
  'sports-psychology-and-sociology': 'खेल मनोविज्ञान एवं खेल समाजशास्त्र',
  'sports-injuries-and-rehabilitation': 'खेल चोटें, प्राथमिक उपचार एवं पुनर्वास',
  'health-and-nutrition': 'स्वास्थ्य शिक्षा, जीवनशैली रोग एवं खेल पोषण',
  'sports-training-and-fitness': 'खेल प्रशिक्षण के सिद्धांत एवं शारीरिक दक्षता',
  'tests-measurement-and-evaluation': 'परीक्षण, मापन एवं मूल्यांकन',
  'yoga': 'योग शिक्षा, आसन एवं प्राणायाम',
  'sports-rules-measurements-and-equipment': 'प्रमुख खेलों के नियम, माप एवं उपकरण',
  'sports-general-knowledge': 'खेल सामान्य ज्ञान, पुरस्कार एवं व्यक्तित्व',
  'growth-and-development': 'मानव वृद्धि एवं विकास',
  'research-methods-and-statistics': 'अनुसंधान विधियां एवं व्यावहारिक सांख्यिकी'
};

function getSectionName(slug) {
  return SECTION_TITLES[slug] || slug.split('-').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' ');
}

function getSectionNameHi(slug) {
  return SECTION_TITLES_HI[slug] || getSectionName(slug);
}

// 4. Build Full-Fidelity Translation Prompt
function buildTranslationPrompt(topic, enPayload) {
  const parts = topic.href.split('/').filter(Boolean);
  const branchSlug = parts[1] || 'general';
  const branchTitleEn = getSectionName(branchSlug);
  const branchTitleHi = getSectionNameHi(branchSlug);

  return `You are a Senior Professor of Physical Education and master translator for Uttar Pradesh TGT/PGT physical education teacher examinations.
Provide an exhaustive, master-level 1:1 Hindi (हिन्दी) translation of the following English Physical Education study content.

STRICT FULL-FIDELITY RULES:
1. DO NOT summarize, abridge, or skip ANY concepts. The Hindi version must have the exact same depth, nuance, and completeness as the English version.
2. Every cited scholar, publication year, formula, constant density, measurement number, and technical term MUST be retained and clearly translated into Hindi (with English technical terms in parentheses where helpful for exam clarity).
3. In each section, preserve every sub-bullet and list item in semantic HTML (<p>, <ul>, <li>, <strong>, <em>, <code>).
4. Translate all 10 practice questions and their rationales completely into Hindi.
5. Provide a comparative table, mnemonic, 6 high-yield exam points, 2 common misconceptions, and 4 FAQs in Hindi.

SOURCE ENGLISH CONTENT TO TRANSLATE:
${JSON.stringify(enPayload, null, 2)}

OUTPUT FORMAT:
Respond with ONLY a raw valid JSON object (no markdown \`\`\`json wrappers, no preamble) adhering strictly to this schema:
{
  "title_hi": "पूर्ण प्रामाणिक हिन्दी शीर्षक (उदा. शरीर संघटन: Body Composition)",
  "short_intro_hi": "पूर्ण हिन्दी अनुवाद...",
  "notes_sections_hi": [
    {
      "heading": "1. सैद्धांतिक आधार एवं शास्त्रीय परिभाषाएं (Definitional Framework)",
      "content_html": "<p>पूर्ण अनुवाद जिसमें सभी विद्वानों, वर्षों, मॉडलों और सिद्धांतों का संपूर्ण विस्तृत विवरण हो...</p>"
    },
    {
      "heading": "2. शारीरिक एवं जैव-यांत्रिकीय सिद्धांत तथा मापन तकनीकें",
      "content_html": "<p>पूर्ण अनुवाद जिसमें सभी मापन विधियों, सूत्रों, अनुपातों और तालिकाओं का संपूर्ण विवरण हो...</p>"
    },
    {
      "heading": "3. खेल प्रदर्शन, कोचिंग एवं शिक्षण में अनुप्रयोग",
      "content_html": "<p>पूर्ण अनुवाद जिसमें प्रदर्शन, प्रशिक्षण, चोट रोकथाम, स्वास्थ्य और शिक्षण अनुप्रयोगों का संपूर्ण विवरण हो...</p>"
    }
  ],
  "comparison_tables_hi": [
    {
      "title": "तुलनात्मक तालिका शीर्षक",
      "headers": ["मानदंड", "श्रेणी अ", "श्रेणी ब"],
      "rows": [
        ["बिंदु 1", "विवरण", "विवरण"]
      ]
    }
  ],
  "mnemonics_hi": [
    {
      "title": "स्मृति सूत्र / Mnemonic",
      "trick": "सूत्र",
      "explanation": "विस्तृत व्याख्या"
    }
  ],
  "exam_points_hi": [
    "परीक्षा तथ्य 1",
    "परीक्षा तथ्य 2",
    "परीक्षा तथ्य 3",
    "परीक्षा तथ्य 4",
    "परीक्षा तथ्य 5",
    "परीक्षा तथ्य 6"
  ],
  "common_errors_hi": [
    "भ्रांति 1: परीक्षा की सामान्य गलतफहमी बनाम वैज्ञानिक सत्य।",
    "भ्रांति 2: सामान्य भूल एवं सही समाधान।"
  ],
  "practice_questions_hi": [
    {
      "question": "हिन्दी में अनुवादित बहुविकल्पीय प्रश्न?",
      "options": ["विकल्प क", "विकल्प ख", "विकल्प ग", "विकल्प घ"],
      "correct_index": 0,
      "explanation": "सही उत्तर का विस्तृत वैज्ञानिक एवं प्रामाणिक कारण।"
    }
  ],
  "faqs_hi": [
    {
      "q": "हिन्दी प्रश्न?",
      "a": "सटीक उत्तर"
    }
  ]
}`;
}

// 5. Render Bilingual Study Page
function renderBilingualPage(topic, enData, hiData) {
  const canonicalUrl = `${DOMAIN}${topic.href}`;
  const parts = topic.href.split('/').filter(Boolean);
  const branchSlug = parts[1] || 'general';
  const branchTitleEn = getSectionName(branchSlug);
  const branchTitleHi = getSectionNameHi(branchSlug);
  const branchUrl = `/physical-education/${branchSlug}/`;

  const examBadgesEn = [];
  const examBadgesHi = [];
  if (topic.inTgt) {
    examBadgesEn.push('<span class="chip chip-tgt">UP TGT Physical Education</span>');
    examBadgesHi.push('<span class="chip chip-tgt">यूपी टीजीटी शारीरिक शिक्षा</span>');
  }
  if (topic.inPgt) {
    examBadgesEn.push('<span class="chip chip-pgt">UP PGT Physical Education</span>');
    examBadgesHi.push('<span class="chip chip-pgt">यूपी पीजीटी शारीरिक शिक्षा</span>');
  }
  if (topic.tgtUnit) {
    examBadgesEn.push(`<span class="chip chip-unit">TGT Unit ${topic.tgtUnit}</span>`);
    examBadgesHi.push(`<span class="chip chip-unit">टीजीटी इकाई ${topic.tgtUnit}</span>`);
  }
  if (topic.pgtUnit) {
    examBadgesEn.push(`<span class="chip chip-unit">PGT Unit ${topic.pgtUnit}</span>`);
    examBadgesHi.push(`<span class="chip chip-unit">पीजीटी इकाई ${topic.pgtUnit}</span>`);
  }

  const pageTitle = `${enData.title} (${hiData.title_hi}) — Study Notes & MCQs | Physical Education | SJ Maths`;
  const metaDesc = `Master ${enData.title} / ${hiData.title_hi} for UP TGT/PGT Physical Education. Bilingual study notes, theory, tables, mnemonics, and practice MCQs.`;

  // Render English Sections
  let enNotesHtml = '';
  (enData.notes_sections || []).forEach((sec, idx) => {
    enNotesHtml += `
      <section class="card content-card" id="en-sec-${idx + 1}">
        <h2>${sec.heading}</h2>
        <div class="prose-content">${sec.content_html}</div>
      </section>
    `;
  });

  let enTablesHtml = '';
  if (enData.comparison_tables && Array.isArray(enData.comparison_tables) && enData.comparison_tables.length > 0) {
    enData.comparison_tables.forEach(table => {
      const headers = (table.headers || []).map(h => `<th>${h}</th>`).join('');
      const rows = (table.rows || []).map(r => `<tr>${(r || []).map(c => `<td>${c}</td>`).join('')}</tr>`).join('');
      enTablesHtml += `
        <div class="comparison-card">
          <div class="table-title">${table.title}</div>
          <div class="table-responsive">
            <table class="styled-table">
              <thead><tr>${headers}</tr></thead>
              <tbody>${rows}</tbody>
            </table>
          </div>
        </div>
      `;
    });
  }

  let enMnemonicsHtml = '';
  if (enData.mnemonics && Array.isArray(enData.mnemonics) && enData.mnemonics.length > 0) {
    enData.mnemonics.forEach(m => {
      enMnemonicsHtml += `
        <div class="mnemonic-card">
          <div class="mnemonic-badge">Memory Trick / Mnemonic</div>
          <div class="mnemonic-title">${m.title}</div>
          <div class="mnemonic-formula">${m.trick}</div>
          <p class="mnemonic-desc">${m.explanation}</p>
        </div>
      `;
    });
  }

  let enPointsHtml = '';
  if (enData.exam_points && Array.isArray(enData.exam_points) && enData.exam_points.length > 0) {
    enPointsHtml = `
      <section class="card points-card" id="en-points">
        <h2>High-Yield Exam Points for UP TGT &amp; PGT</h2>
        <ul class="points-list">
          ${enData.exam_points.map(pt => `<li>${pt}</li>`).join('\n          ')}
        </ul>
      </section>
    `;
  }

  let enErrorsHtml = '';
  if (enData.common_errors && Array.isArray(enData.common_errors) && enData.common_errors.length > 0) {
    enErrorsHtml = `
      <section class="card errors-card" id="en-errors">
        <h2>Common Misconceptions &amp; Exam Traps</h2>
        <ul class="errors-list">
          ${enData.common_errors.map(err => `<li>${err}</li>`).join('\n          ')}
        </ul>
      </section>
    `;
  }

  let enQuestionsHtml = '';
  if (enData.practice_questions && Array.isArray(enData.practice_questions) && enData.practice_questions.length > 0) {
    const letters = ['A', 'B', 'C', 'D'];
    const validQuestions = enData.practice_questions.filter(q => q && q.question);
    const qList = validQuestions.map((q, i) => {
      const opts = Array.isArray(q.options) ? q.options : (Array.isArray(q.choices) ? q.choices : []);
      const optionsHtml = opts.map((opt, oIdx) => `
        <li class="mcq-option" data-idx="${oIdx}">
          <span class="opt-letter">${letters[oIdx] || String.fromCharCode(65 + oIdx)}</span>
          <span class="opt-text">${opt}</span>
        </li>
      `).join('');

      const correctIdx = typeof q.correct_index === 'number' && q.correct_index >= 0 ? q.correct_index : 0;
      const correctLetter = letters[correctIdx] || 'A';
      const correctText = opts[correctIdx] || '';

      return `
        <div class="mcq-item" id="en-q-${i + 1}" data-correct="${correctIdx}">
          <div class="mcq-header">
            <span class="q-num">Q${i + 1}</span>
            <span class="q-text">${q.question}</span>
          </div>
          <ul class="mcq-options">
            ${optionsHtml}
          </ul>
          <div class="mcq-reveal">
            <button type="button" class="btn-reveal" onclick="toggleExp('en-exp-${i}')">Show Answer &amp; Explanation</button>
            <div class="mcq-explanation" id="en-exp-${i}" style="display:none;">
              <strong>Correct Option: ${correctLetter}${correctText ? ' (' + correctText + ')' : ''}</strong>
              <p>${q.explanation || 'Refer to the conceptual notes above.'}</p>
            </div>
          </div>
        </div>
      `;
    }).join('\n');

    enQuestionsHtml = `
      <section class="card mcq-card" id="en-mcqs">
        <h2>Practice Examination Questions (${validQuestions.length} MCQs)</h2>
        <p style="color:var(--ink-muted);font-size:.9rem;margin-bottom:20px;">
          Test your conceptual understanding. Select an answer and check the detailed pedagogical rationale.
        </p>
        <div class="mcq-container">
          ${qList}
        </div>
      </section>
    `;
  }

  let enFaqsHtml = '';
  if (enData.faqs && Array.isArray(enData.faqs) && enData.faqs.length > 0) {
    enFaqsHtml = `
      <section class="card faq-card" id="en-faqs">
        <h2>Frequently Asked Questions</h2>
        <div class="faq-list">
          ${enData.faqs.map(f => `
            <div class="faq-item">
              <h3 class="faq-q">${f.q}</h3>
              <p class="faq-a">${f.a}</p>
            </div>
          `).join('\n          ')}
        </div>
      </section>
    `;
  }

  // Render Hindi Sections
  let hiNotesHtml = '';
  (hiData.notes_sections_hi || []).forEach((sec, idx) => {
    hiNotesHtml += `
      <section class="card content-card" id="hi-sec-${idx + 1}">
        <h2>${sec.heading}</h2>
        <div class="prose-content">${sec.content_html}</div>
      </section>
    `;
  });

  let hiTablesHtml = '';
  if (hiData.comparison_tables_hi && Array.isArray(hiData.comparison_tables_hi) && hiData.comparison_tables_hi.length > 0) {
    hiData.comparison_tables_hi.forEach(table => {
      const headers = (table.headers || []).map(h => `<th>${h}</th>`).join('');
      const rows = (table.rows || []).map(r => `<tr>${(r || []).map(c => `<td>${c}</td>`).join('')}</tr>`).join('');
      hiTablesHtml += `
        <div class="comparison-card">
          <div class="table-title">${table.title}</div>
          <div class="table-responsive">
            <table class="styled-table">
              <thead><tr>${headers}</tr></thead>
              <tbody>${rows}</tbody>
            </table>
          </div>
        </div>
      `;
    });
  }

  let hiMnemonicsHtml = '';
  if (hiData.mnemonics_hi && Array.isArray(hiData.mnemonics_hi) && hiData.mnemonics_hi.length > 0) {
    hiData.mnemonics_hi.forEach(m => {
      hiMnemonicsHtml += `
        <div class="mnemonic-card">
          <div class="mnemonic-badge">स्मरण सूत्र / Mnemonic</div>
          <div class="mnemonic-title">${m.title}</div>
          <div class="mnemonic-formula">${m.trick}</div>
          <p class="mnemonic-desc">${m.explanation}</p>
        </div>
      `;
    });
  }

  let hiPointsHtml = '';
  if (hiData.exam_points_hi && Array.isArray(hiData.exam_points_hi) && hiData.exam_points_hi.length > 0) {
    hiPointsHtml = `
      <section class="card points-card" id="hi-points">
        <h2>यूपी टीजीटी एवं पीजीटी हेतु मुख्य परीक्षा बिंदु</h2>
        <ul class="points-list">
          ${hiData.exam_points_hi.map(pt => `<li>${pt}</li>`).join('\n          ')}
        </ul>
      </section>
    `;
  }

  let hiErrorsHtml = '';
  if (hiData.common_errors_hi && Array.isArray(hiData.common_errors_hi) && hiData.common_errors_hi.length > 0) {
    hiErrorsHtml = `
      <section class="card errors-card" id="hi-errors">
        <h2>सामान्य भ्रांतियां एवं परीक्षा के जाल (Exam Traps)</h2>
        <ul class="errors-list">
          ${hiData.common_errors_hi.map(err => `<li>${err}</li>`).join('\n          ')}
        </ul>
      </section>
    `;
  }

  let hiQuestionsHtml = '';
  if (hiData.practice_questions_hi && Array.isArray(hiData.practice_questions_hi) && hiData.practice_questions_hi.length > 0) {
    const letters = ['क', 'ख', 'ग', 'घ'];
    const validQuestions = hiData.practice_questions_hi.filter(q => q && q.question);
    const qList = validQuestions.map((q, i) => {
      const opts = Array.isArray(q.options) ? q.options : (Array.isArray(q.choices) ? q.choices : []);
      const optionsHtml = opts.map((opt, oIdx) => `
        <li class="mcq-option" data-idx="${oIdx}">
          <span class="opt-letter">${letters[oIdx] || String.fromCharCode(65 + oIdx)}</span>
          <span class="opt-text">${opt}</span>
        </li>
      `).join('');

      const correctIdx = typeof q.correct_index === 'number' && q.correct_index >= 0 ? q.correct_index : 0;
      const correctLetter = letters[correctIdx] || 'क';
      const correctText = opts[correctIdx] || '';

      return `
        <div class="mcq-item" id="hi-q-${i + 1}" data-correct="${correctIdx}">
          <div class="mcq-header">
            <span class="q-num">प्रश्न ${i + 1}</span>
            <span class="q-text">${q.question}</span>
          </div>
          <ul class="mcq-options">
            ${optionsHtml}
          </ul>
          <div class="mcq-reveal">
            <button type="button" class="btn-reveal" onclick="toggleExp('hi-exp-${i}')">उत्तर एवं व्याख्या देखें</button>
            <div class="mcq-explanation" id="hi-exp-${i}" style="display:none;">
              <strong>सही उत्तर: विकल्प ${correctLetter}${correctText ? ' (' + correctText + ')' : ''}</strong>
              <p>${q.explanation || 'सैद्धांतिक नोट्स का अध्ययन करें।'}</p>
            </div>
          </div>
        </div>
      `;
    }).join('\n');

    hiQuestionsHtml = `
      <section class="card mcq-card" id="hi-mcqs">
        <h2>अभ्यास परीक्षा प्रश्न (${validQuestions.length} बहुविकल्पीय प्रश्न)</h2>
        <p style="color:var(--ink-muted);font-size:.9rem;margin-bottom:20px;">
          अपनी अवधारणात्मक समझ का परीक्षण करें। उत्तर चुनें और विस्तृत शैक्षणिक व्याख्या देखें।
        </p>
        <div class="mcq-container">
          ${qList}
        </div>
      </section>
    `;
  }

  let hiFaqsHtml = '';
  if (hiData.faqs_hi && Array.isArray(hiData.faqs_hi) && hiData.faqs_hi.length > 0) {
    hiFaqsHtml = `
      <section class="card faq-card" id="hi-faqs">
        <h2>अक्सर पूछे जाने वाले प्रश्न (FAQs)</h2>
        <div class="faq-list">
          ${hiData.faqs_hi.map(f => `
            <div class="faq-item">
              <h3 class="faq-q">${f.q}</h3>
              <p class="faq-a">${f.a}</p>
            </div>
          `).join('\n          ')}
        </div>
      </section>
    `;
  }

  return `<!doctype html>
<html lang="en" data-pe-lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>${pageTitle}</title>
  <meta name="description" content="${metaDesc}">
  <meta name="robots" content="index,follow,max-image-preview:large">
  <meta name="author" content="SJ Maths">
  <meta name="theme-color" content="#0F766E">
  <link rel="canonical" href="${canonicalUrl}">
  <link rel="icon" type="image/png" href="/favicon.png">

  <!-- Open Graph -->
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="SJ Maths">
  <meta property="og:title" content="${pageTitle}">
  <meta property="og:description" content="${metaDesc}">
  <meta property="og:url" content="${canonicalUrl}">
  <meta property="og:image" content="https://sjmaths.com/assets/icons/icon-512x512.png">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="${pageTitle}">
  <meta name="twitter:description" content="${metaDesc}">
  <meta name="twitter:image" content="https://sjmaths.com/assets/icons/icon-512x512.png">

  <!-- Immediate Language Initialization (No Flicker) -->
  <script>
    (function() {
      try {
        const saved = localStorage.getItem('sjmaths_pe_lang') || 'en';
        document.documentElement.setAttribute('data-pe-lang', saved);
      } catch (e) {}
    })();
  </script>

  <!-- Structured Data (JSON-LD) -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "LearningResource",
    "name": "${enData.title}",
    "headline": "${enData.title} (${hiData.title_hi}) — Study Notes & MCQs",
    "description": "${metaDesc}",
    "url": "${canonicalUrl}",
    "inLanguage": ["en", "hi"],
    "learningResourceType": "Study Guide / Quiz",
    "educationalLevel": "Teacher Eligibility Examination (TGT / PGT)",
    "isPartOf": {
      "@type": "WebSite",
      "name": "SJ Maths",
      "url": "https://sjmaths.com/"
    },
    "breadcrumb": {
      "@type": "BreadcrumbList",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://sjmaths.com/" },
        { "@type": "ListItem", "position": 2, "name": "Physical Education", "item": "https://sjmaths.com/physical-education/" },
        { "@type": "ListItem", "position": 3, "name": "${branchTitleEn}", "item": "https://sjmaths.com${branchUrl}" },
        { "@type": "ListItem", "position": 4, "name": "${enData.title}", "item": "${canonicalUrl}" }
      ]
    }
  }
  </script>

  <style>
    :root {
      --bg: #f6faf8;
      --card-bg: #ffffff;
      --ink: #16211f;
      --ink-muted: #566762;
      --line: #dde8e4;
      --soft-line: #edf3f1;
      --brand: #0f766e;
      --brand-dark: #115e59;
      --brand-soft: #eaf8f5;
      --success: #15803d;
      --success-soft: #f0fdf4;
      --shadow: 0 12px 34px rgba(21,74,65,.07);
      --radius: 16px;
      --header-h: 66px;
    }
    * { box-sizing: border-box; }
    html { scroll-behavior: smooth; }
    body {
      margin: 0; color: var(--ink);
      background: radial-gradient(circle at 100% 0,rgba(20,184,166,.07),transparent 28rem), var(--bg);
      font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
      line-height: 1.65; -webkit-font-smoothing: antialiased;
    }
    a { color: var(--brand); text-decoration: none; }
    a:hover { text-decoration: underline; }
    .wrap { width: min(1080px, calc(100% - 32px)); margin: auto; }
    
    /* Header */
    .site-header {
      height: var(--header-h); position: sticky; top: 0; z-index: 60;
      background: rgba(255,255,255,.96); backdrop-filter: blur(12px); border-bottom: 1px solid var(--line);
    }
    .header-inner { height: 100%; display: flex; align-items: center; justify-content: space-between; gap: 16px; }
    .brand { display: flex; align-items: center; gap: 11px; text-decoration: none; color: inherit; }
    .brand-mark {
      width: 38px; height: 38px; border-radius: 11px; display: grid; place-items: center;
      background: linear-gradient(145deg, #0f766e, #0d9488); color: white;
      font-weight: 900; font-family: 'Times New Roman', serif; font-size: 1.6rem; font-style: italic; line-height: 1;
    }
    .brand-name { font-weight: 850; letter-spacing: -.02em; display: block; }
    .brand-sub { font-size: .7rem; color: var(--ink-muted); display: block; margin-top: 1px; }

    /* Header Nav & Language Switcher */
    .header-nav { display: flex; align-items: center; gap: 12px; }
    
    .lang-toggle-wrap {
      display: inline-flex;
      align-items: center;
      background: #edf3f1;
      border: 1px solid var(--line);
      border-radius: 999px;
      padding: 2px;
      gap: 2px;
    }
    .lang-btn {
      border: none;
      background: transparent;
      color: var(--ink-muted);
      font-size: .78rem;
      font-weight: 750;
      padding: 5px 12px;
      border-radius: 999px;
      cursor: pointer;
      transition: all .2s ease;
      line-height: 1;
    }
    .lang-btn:hover { color: var(--ink); }

    /* Persistent Language Display Rules */
    html[data-pe-lang="en"] .content-hi { display: none !important; }
    html[data-pe-lang="en"] .content-en { display: block !important; }
    html[data-pe-lang="en"] #btn-en { background: var(--brand); color: #ffffff; box-shadow: 0 2px 6px rgba(15,118,110,.25); }
    html[data-pe-lang="en"] #btn-hi { background: transparent; color: var(--ink-muted); }

    html[data-pe-lang="hi"] .content-en { display: none !important; }
    html[data-pe-lang="hi"] .content-hi { display: block !important; }
    html[data-pe-lang="hi"] #btn-hi { background: var(--brand); color: #ffffff; box-shadow: 0 2px 6px rgba(15,118,110,.25); }
    html[data-pe-lang="hi"] #btn-en { background: transparent; color: var(--ink-muted); }

    /* Breadcrumbs */
    .breadcrumb {
      display: flex; gap: 8px; align-items: center; font-size: .78rem; color: var(--ink-muted);
      margin: 24px 0 16px; flex-wrap: wrap;
    }
    .breadcrumb a { color: var(--ink-muted); }
    .breadcrumb a:hover { color: var(--brand); }
    .breadcrumb span.sep { color: #9aa8a4; }

    /* Topic Hero */
    .topic-hero {
      background: var(--card-bg); border: 1px solid var(--line); border-radius: var(--radius);
      padding: 32px 36px; box-shadow: var(--shadow); position: relative; overflow: hidden; margin-bottom: 24px;
    }
    .topic-hero::before {
      content: ""; position: absolute; left: 0; top: 0; bottom: 0; width: 6px;
      background: linear-gradient(180deg, var(--brand), #0d9488);
    }
    .kicker { font-size: .75rem; text-transform: uppercase; font-weight: 800; letter-spacing: .08em; color: var(--brand); margin-bottom: 8px; }
    h1 { margin: 0 0 12px; font-size: clamp(1.6rem, 3.2vw, 2.3rem); line-height: 1.22; color: var(--ink); letter-spacing: -.02em; }
    .lead { margin: 0 0 16px; color: var(--ink-muted); font-size: .98rem; line-height: 1.6; }
    .topic-chips { display: flex; gap: 8px; flex-wrap: wrap; }
    .chip { padding: 4px 11px; border-radius: 999px; font-size: .7rem; font-weight: 750; border: 1px solid transparent; }
    .chip-tgt { background: #e0f2fe; color: #0369a1; border-color: #bae6fd; }
    .chip-pgt { background: #f3e8ff; color: #7e22ce; border-color: #e9d5ff; }
    .chip-unit { background: #f0fdf4; color: #15803d; border-color: #bbf7d0; }

    /* Cards */
    .card {
      background: var(--card-bg); border: 1px solid var(--line); border-radius: var(--radius);
      padding: 28px 34px; box-shadow: var(--shadow); margin-bottom: 24px;
    }
    .card h2 {
      margin: 0 0 16px; font-size: 1.28rem; font-weight: 800; color: var(--ink);
      border-bottom: 2px solid var(--soft-line); padding-bottom: 9px;
    }
    .prose-content p { font-size: .96rem; line-height: 1.75; color: #283632; margin-bottom: 14px; }
    .prose-content ul { margin: 10px 0 18px 22px; padding: 0; }
    .prose-content li { font-size: .94rem; line-height: 1.7; color: #283632; margin-bottom: 8px; }
    .prose-content strong { color: #16211f; }

    /* Comparison Table */
    .comparison-card {
      background: var(--card-bg); border: 1px solid var(--line); border-radius: var(--radius);
      padding: 24px 28px; box-shadow: var(--shadow); margin-bottom: 24px; overflow: hidden;
    }
    .table-title { font-weight: 800; font-size: 1.08rem; color: var(--ink); margin-bottom: 14px; }
    .table-responsive { overflow-x: auto; -webkit-overflow-scrolling: touch; }
    .styled-table { width: 100%; border-collapse: collapse; font-size: .88rem; text-align: left; }
    .styled-table th { background: var(--brand-soft); color: var(--brand-dark); padding: 11px 14px; font-weight: 750; border: 1px solid var(--line); }
    .styled-table td { padding: 10px 14px; border: 1px solid var(--line); vertical-align: top; }
    .styled-table tr:nth-child(even) { background: #fbfdfc; }

    /* Mnemonic Card */
    .mnemonic-card {
      background: linear-gradient(135deg, #f0fdf4, #dcfce7); border: 1px solid #86efac;
      border-radius: var(--radius); padding: 22px 26px; margin-bottom: 24px;
    }
    .mnemonic-badge {
      display: inline-block; background: #16a34a; color: white; font-size: .68rem;
      text-transform: uppercase; font-weight: 800; letter-spacing: .06em; padding: 3px 9px; border-radius: 6px; margin-bottom: 8px;
    }
    .mnemonic-title { font-size: 1.05rem; font-weight: 800; color: #14532d; margin-bottom: 6px; }
    .mnemonic-formula {
      font-size: 1.15rem; font-weight: 900; color: #15803d; font-family: monospace;
      background: rgba(255,255,255,.8); padding: 6px 12px; border-radius: 8px; display: inline-block; margin-bottom: 8px;
    }
    .mnemonic-desc { font-size: .9rem; color: #166534; margin: 0; line-height: 1.55; }

    /* Points & Errors List */
    .points-card h2 { color: var(--brand-dark); }
    .points-list { margin: 0; padding-left: 20px; }
    .points-list li { margin-bottom: 9px; font-size: .92rem; color: #23332f; line-height: 1.6; }
    .errors-card { background: #fffcf8; border-color: #fed7aa; }
    .errors-card h2 { color: #9a3412; border-bottom-color: #ffedd5; }
    .errors-list { margin: 0; padding-left: 20px; }
    .errors-list li { margin-bottom: 9px; font-size: .92rem; color: #7c2d12; line-height: 1.6; }

    /* Practice MCQs */
    .mcq-card h2 { color: var(--brand-dark); }
    .mcq-item {
      background: #fafcfb; border: 1px solid var(--line); border-radius: 12px;
      padding: 18px 20px; margin-bottom: 16px;
    }
    .mcq-header { display: flex; gap: 12px; align-items: baseline; margin-bottom: 12px; }
    .q-num {
      background: var(--brand); color: white; font-size: .75rem; font-weight: 850;
      padding: 3px 8px; border-radius: 6px; flex-shrink: 0;
    }
    .q-text { font-size: .95rem; font-weight: 700; color: var(--ink); line-height: 1.5; }
    .mcq-options { list-style: none; margin: 0 0 12px; padding: 0; display: grid; gap: 8px; }
    .mcq-option {
      padding: 9px 14px; border: 1px solid var(--line); border-radius: 8px;
      font-size: .88rem; display: flex; align-items: center; gap: 10px; background: #fff;
    }
    .opt-letter {
      width: 24px; height: 24px; border-radius: 6px; background: var(--soft-line);
      display: grid; place-items: center; font-size: .75rem; font-weight: 800; color: var(--ink-muted);
    }
    .btn-reveal {
      background: var(--brand-soft); border: 1px solid #cdeae5; color: var(--brand-dark);
      padding: 7px 14px; border-radius: 8px; font-size: .8rem; font-weight: 750; cursor: pointer;
    }
    .btn-reveal:hover { background: #d7f1ec; }
    .mcq-explanation {
      margin-top: 12px; padding: 12px 16px; background: var(--success-soft);
      border: 1px solid #bbf7d0; border-radius: 8px; font-size: .86rem; color: #166534;
    }
    .mcq-explanation p { margin: 6px 0 0; }

    /* FAQs */
    .faq-item { margin-bottom: 16px; padding-bottom: 14px; border-bottom: 1px solid var(--soft-line); }
    .faq-item:last-child { border-bottom: none; margin-bottom: 0; padding-bottom: 0; }
    .faq-q { font-size: .98rem; font-weight: 750; color: var(--brand-dark); margin: 0 0 6px; }
    .faq-a { font-size: .9rem; color: #374744; margin: 0; line-height: 1.6; }

    /* Cross navigation bar */
    .cross-nav {
      display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px;
      margin: 32px 0 48px;
    }
    .cross-nav-card {
      background: var(--card-bg); border: 1px solid var(--line); border-radius: var(--radius);
      padding: 18px 20px; display: flex; align-items: center; justify-content: space-between;
      gap: 12px; transition: border-color .2s; text-decoration: none;
    }
    .cross-nav-card:hover { border-color: var(--brand); }
    .cross-nav-card strong { display: block; font-size: .9rem; color: var(--ink); }
    .cross-nav-card span { font-size: .76rem; color: var(--ink-muted); }

    /* Footer */
    .site-footer {
      padding: 32px 0; border-top: 1px solid var(--line); background: #ffffff;
      font-size: .8rem; color: var(--ink-muted); text-align: center; margin-top: 48px;
    }
    @media(max-width: 640px) {
      .topic-hero { padding: 22px 20px; }
      .card { padding: 20px 18px; }
      .header-inner { flex-wrap: wrap; height: auto; padding: 10px 0; }
    }
  </style>

  <script>
    function setLanguage(lang) {
      try {
        localStorage.setItem('sjmaths_pe_lang', lang);
      } catch (e) {}
      document.documentElement.setAttribute('data-pe-lang', lang);
    }
    function toggleExp(id) {
      const el = document.getElementById(id);
      if (el) {
        el.style.display = el.style.display === 'none' ? 'block' : 'none';
      }
    }
  </script>
</head>
<body>

<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="/" aria-label="SJ Maths Home">
      <span class="brand-mark" aria-hidden="true">&int;</span>
      <span>
        <span class="brand-name">SJ Maths</span>
        <span class="brand-sub">Physical Education Portal</span>
      </span>
    </a>
    
    <div class="header-nav">
      <!-- Persistent Language Switcher -->
      <div class="lang-toggle-wrap" role="group" aria-label="Language Toggle">
        <button type="button" id="btn-en" class="lang-btn" onclick="setLanguage('en')">English</button>
        <button type="button" id="btn-hi" class="lang-btn" onclick="setLanguage('hi')">हिन्दी</button>
      </div>

      <a href="/up-tgt-physical-education/" style="font-size:.82rem;font-weight:700;">UP TGT</a>
      <a href="/up-pgt-physical-education/" style="font-size:.82rem;font-weight:700;">UP PGT</a>
    </div>
  </div>
</header>

<main class="wrap">
  <!-- ENGLISH CONTENT BLOCK -->
  <div class="content-en">
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="/">Home</a>
      <span class="sep">›</span>
      <a href="/physical-education/">Physical Education</a>
      <span class="sep">›</span>
      <a href="${branchUrl}">${branchTitleEn}</a>
      <span class="sep">›</span>
      <span>${enData.title}</span>
    </nav>

    <article class="topic-hero">
      <div class="kicker">${branchTitleEn} • ${topic.groupTitle}</div>
      <h1>${enData.title}</h1>
      <p class="lead">${enData.short_intro}</p>
      <div class="topic-chips">
        ${examBadgesEn.join('\n        ')}
      </div>
    </article>

    ${enNotesHtml}
    ${enTablesHtml}
    ${enMnemonicsHtml}
    ${enPointsHtml}
    ${enErrorsHtml}
    ${enQuestionsHtml}
    ${enFaqsHtml}
  </div>

  <!-- HINDI CONTENT BLOCK -->
  <div class="content-hi">
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="/">होम</a>
      <span class="sep">›</span>
      <a href="/physical-education/">शारीरिक शिक्षा</a>
      <span class="sep">›</span>
      <a href="${branchUrl}">${branchTitleHi}</a>
      <span class="sep">›</span>
      <span>${hiData.title_hi}</span>
    </nav>

    <article class="topic-hero">
      <div class="kicker">${branchTitleHi} • ${topic.groupTitle}</div>
      <h1>${hiData.title_hi}</h1>
      <p class="lead">${hiData.short_intro_hi}</p>
      <div class="topic-chips">
        ${examBadgesHi.join('\n        ')}
      </div>
    </article>

    ${hiNotesHtml}
    ${hiTablesHtml}
    ${hiMnemonicsHtml}
    ${hiPointsHtml}
    ${hiErrorsHtml}
    ${hiQuestionsHtml}
    ${hiFaqsHtml}
  </div>

  <section class="cross-nav" aria-label="Syllabus Navigation">
    <a class="cross-nav-card" href="/up-tgt-physical-education/">
      <div>
        <strong>UP TGT Physical Education Tracker</strong>
        <span>Track all 8 units &amp; 149 curriculum topics</span>
      </div>
      <span aria-hidden="true">→</span>
    </a>
    <a class="cross-nav-card" href="/up-pgt-physical-education/">
      <div>
        <strong>UP PGT Physical Education Tracker</strong>
        <span>Check 211 topics with TGT/PGT overlap tags</span>
      </div>
      <span aria-hidden="true">→</span>
    </a>
  </section>
</main>

<footer class="site-footer">
  <div class="wrap">
    <p>© SJ Maths • Dedicated preparation portal for teacher examinations and physical education.</p>
    <p><a href="/privacy-policy/">Privacy Policy</a> • <a href="/physical-education/">Physical Education Directory</a> • <a href="/">Home</a></p>
  </div>
</footer>

</body>
</html>`;
}

// 6. Main Pipeline
async function run() {
  console.log('================================================================');
  console.log('SJ Maths — Physical Education Full-Fidelity Hindi Translation Pipeline');
  console.log(`Models: ${FALLBACK_MODELS.join(', ')}`);
  console.log(`Total Topics: ${allTopics.length}`);
  console.log('================================================================');

  let eligibleTopics = allTopics;

  if (TARGET_TOPIC) {
    const clean = TARGET_TOPIC.endsWith('/') ? TARGET_TOPIC : TARGET_TOPIC + '/';
    eligibleTopics = eligibleTopics.filter(t => t.href === clean);
    console.log(`Targeting single topic: ${clean} (${eligibleTopics.length} found)`);
  }

  if (LIMIT) {
    eligibleTopics = eligibleTopics.slice(0, LIMIT);
    console.log(`Applying limit of ${LIMIT} topics.`);
  }

  let translatedCount = 0;
  let skippedCount = 0;
  let errorCount = 0;

  for (let i = 0; i < eligibleTopics.length; i++) {
    const topic = eligibleTopics[i];
    const relativePath = topic.href.replace(/^\//, '').replace(/\/$/, '');
    const targetDir = path.join(ROOT, relativePath);
    const targetFile = path.join(targetDir, 'index.html');

    if (!fs.existsSync(targetFile)) {
      skippedCount++;
      continue;
    }

    // Skip if already translated with full fidelity in statusMap (unless --force)
    if (statusMap[topic.href]?.fullFidelity === true && !FORCE) {
      skippedCount++;
      continue;
    }

    console.log(`\n[${i + 1}/${eligibleTopics.length}] Translating 1:1 to Hindi: ${topic.name}`);
    console.log(`  Path: ${topic.href}`);

    const existingHtml = fs.readFileSync(targetFile, 'utf8');

    // Extract English title & intro
    const h1Match = existingHtml.match(/<h1>([^<]+)<\/h1>/);
    const leadMatch = existingHtml.match(/<p class="lead">([\s\S]*?)<\/p>/);

    // Extract English content sections
    const secRegex = /<section class="card content-card"[^>]*>[\s\S]*?<h2>([^<]+)<\/h2>[\s\S]*?<div class="prose-content">([\s\S]*?)<\/div>[\s\S]*?<\/section>/g;
    let sMatch;
    const extractedSections = [];
    while ((sMatch = secRegex.exec(existingHtml)) !== null) {
      // Pick up to 3 English sections
      if (extractedSections.length < 3) {
        extractedSections.push({ heading: sMatch[1], content_html: sMatch[2].trim() });
      }
    }

    // Extract English practice questions
    const qRegex = /<div class="mcq-item"[^>]*data-correct="(\d+)">[\s\S]*?<span class="q-text">([\s\S]*?)<\/span>[\s\S]*?<ul class="mcq-options">([\s\S]*?)<\/ul>[\s\S]*?<div class="mcq-explanation"[^>]*>([\s\S]*?)<\/div>/g;
    let qMatch;
    const extractedQuestions = [];
    while ((qMatch = qRegex.exec(existingHtml)) !== null) {
      if (extractedQuestions.length < 10) {
        const qText = qMatch[2].trim();
        const optsHtml = qMatch[3];
        const optRegex = /<span class="opt-text">([\s\S]*?)<\/span>/g;
        const opts = [];
        let oMatch;
        while ((oMatch = optRegex.exec(optsHtml)) !== null) {
          opts.push(oMatch[1].trim());
        }
        const expClean = qMatch[4].replace(/<strong>[\s\S]*?<\/strong>/, '').replace(/<[^>]+>/g, '').trim();
        extractedQuestions.push({
          question: qText,
          options: opts,
          correct_index: parseInt(qMatch[1], 10),
          explanation: expClean
        });
      }
    }

    const enData = {
      title: h1Match ? h1Match[1].trim() : topic.name,
      short_intro: leadMatch ? leadMatch[1].trim() : '',
      notes_sections: extractedSections,
      practice_questions: extractedQuestions
    };

    const prompt = buildTranslationPrompt(topic, enData);
    let hiData = null;

    // Retry loop with model fallback and key rotation
    for (let attempt = 0; attempt < 4 && !hiData; attempt++) {
      const clientObj = getAiClient();
      const currentModel = FALLBACK_MODELS[Math.floor(attempt / 2) % FALLBACK_MODELS.length];
      try {
        console.log(`  Calling Gemini (${currentModel}) using Key #${clientObj.id} [Attempt ${attempt + 1}]...`);
        const response = await clientObj.client.models.generateContent({
          model: currentModel,
          contents: prompt,
          config: {
            temperature: 0.2,
            responseMimeType: 'application/json'
          }
        });

        const rawText = response.text ? response.text.trim() : '';
        const repaired = jsonrepair(rawText);
        hiData = JSON.parse(repaired);
        console.log(`  Received Full Hindi: ${hiData.title_hi}, ${hiData.notes_sections_hi?.length || 0} sections, ${hiData.practice_questions_hi?.length || 0} MCQs.`);
      } catch (err) {
        console.warn(`  Attempt ${attempt + 1} warning: ${err.message}`);
        if (attempt < 3) {
          await new Promise(r => setTimeout(r, 2500));
        }
      }
    }

    if (!hiData) {
      console.error(`  Translation failed after 4 attempts for ${topic.name}. Skipping.`);
      errorCount++;
      continue;
    }

    // Render new bilingual HTML
    const bilingualHtml = renderBilingualPage(topic, enData, hiData);

    if (!DRY_RUN) {
      fs.writeFileSync(targetFile, bilingualHtml, 'utf8');

      statusMap[topic.href] = {
        translated: true,
        fullFidelity: true,
        titleEn: enData.title,
        titleHi: hiData.title_hi,
        sectionsHi: hiData.notes_sections_hi?.length || 0,
        questionsHi: hiData.practice_questions_hi?.length || 0,
        translatedAt: new Date().toISOString()
      };
      saveStatus();
    }

    translatedCount++;
    console.log(`  ✓ Updated bilingual page: ${relativePath}/index.html`);

    if (i < eligibleTopics.length - 1) {
      await new Promise(r => setTimeout(r, 1200));
    }
  }

  console.log(`\n========================================`);
  console.log(`Full-Fidelity Hindi Translation Pipeline Finished!`);
  console.log(`Translated: ${translatedCount} topics`);
  console.log(`Skipped:    ${skippedCount} topics`);
  console.log(`Errors:     ${errorCount}`);
  console.log(`Status saved to: ${STATUS_FILE}`);
  console.log(`========================================`);
}

run().catch(err => {
  console.error('Fatal execution error:', err);
  process.exit(1);
});
