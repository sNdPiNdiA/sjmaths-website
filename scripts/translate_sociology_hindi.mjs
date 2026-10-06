#!/usr/bin/env node
/**
 * ============================================================================
 * SJ Maths — UP PGT Sociology 1:1 Full-Fidelity Hindi Translation Pipeline
 * Powered by Google Gemini API via @google/genai SDK
 * Translates English Sociology study notes and MCQs into academic Hindi (हिन्दी)
 * with zero shortening, retaining all sociological theorists, classical paradigms,
 * Indian sociological pioneers, comparison tables, mnemonics, and 10 MCQs with
 * comprehensive explanations.
 *
 * Configured with a persistent zero-flicker bilingual toggle (English | हिन्दी).
 * Key: GEMINI_API_KEY_1 (with automatic fallback to GEMINI_API_KEY_2).
 * Model: gemini-3.1-flash-lite (with fallback to gemini-3.5-flash-lite on 503).
 * ============================================================================
 */

import fs from 'node:fs';
import path from 'node:path';
import 'dotenv/config';
import { GoogleGenAI } from '@google/genai';
import { jsonrepair } from 'jsonrepair';
import { externalizeSociologyBilingualStyle, sociologyBilingualCss } from './lib/sociology-bilingual-styles.mjs';

const ROOT = process.cwd();
const DOMAIN = 'https://sjmaths.com';
const STATUS_FILE = path.join(ROOT, 'content-translation-status-sociology-hindi.json');

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
const TARGET_SECTION = (() => {
  const idx = args.indexOf('--section');
  return idx !== -1 && args[idx + 1] ? args[idx + 1] : null;
})();
const MODEL_NAME = (() => {
  const idx = args.indexOf('--model');
  return idx !== -1 && args[idx + 1] ? args[idx + 1] : 'gemini-3.1-flash-lite';
})();

const FALLBACK_MODELS = [MODEL_NAME, 'gemini-3.5-flash-lite'];

// Key setup: Default GEMINI_API_KEY_1 with fallback to GEMINI_API_KEY_2
const availableKeys = [
  { name: 'GEMINI_API_KEY_1', key: process.env.GEMINI_API_KEY_1 },
  { name: 'GEMINI_API_KEY_2', key: process.env.GEMINI_API_KEY_2 },
  { name: 'GEMINI_API_KEY', key: process.env.GEMINI_API_KEY }
].filter(k => Boolean(k.key));

if (availableKeys.length === 0) {
  console.error('ERROR: No valid Gemini API key found in .env.');
  process.exit(1);
}

const customKeyIdx = args.indexOf('--key');
let activeKeyObj = customKeyIdx !== -1 && args[customKeyIdx + 1]
  ? availableKeys.find(k => k.name === args[customKeyIdx + 1]) || availableKeys[0]
  : availableKeys[0];

let ai = new GoogleGenAI({ apiKey: activeKeyObj.key });

function switchKeyIfAvailable() {
  const other = availableKeys.find(k => k.name !== activeKeyObj.name);
  if (other) {
    console.log(`  Switching API key: ${activeKeyObj.name} -> ${other.name}`);
    activeKeyObj = other;
    ai = new GoogleGenAI({ apiKey: activeKeyObj.key });
    return true;
  }
  return false;
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

// 3. Extract syllabus definitions from UP PGT Sociology tracker
function decodeHtml(str) {
  return str
    .replace(/&amp;/g, '&')
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'");
}

function extractSyllabus() {
  const trackerPath = path.join(ROOT, 'up-pgt-sociology', 'index.html');
  if (!fs.existsSync(trackerPath)) {
    console.error(`Tracker file not found: ${trackerPath}`);
    return [];
  }
  const html = fs.readFileSync(trackerPath, 'utf8');

  const sectionRegex = /<article class="section-card[^"]*" id="([^"]+)"[\s\S]*?>([\s\S]*?)<\/article>/g;
  let sMatch;
  const topicList = [];

  while ((sMatch = sectionRegex.exec(html)) !== null) {
    const [_, sId, sBody] = sMatch;
    const titleMatch = sBody.match(/<span class="section-title">([^<]+)<\/span>/);
    const rawTitle = titleMatch ? titleMatch[1].trim() : sId;
    const sTitle = decodeHtml(rawTitle);

    const numMatch = sBody.match(/<span class="section-no">[^<]*<strong>([^<]+)<\/strong><\/span>/);
    const sNum = numMatch ? numMatch[1].trim() : '';

    const topicRegex = /<a class="topic-link" href="([^"]+)">([^<]+)<\/a>/g;
    let tMatch;
    while ((tMatch = topicRegex.exec(sBody)) !== null) {
      const href = tMatch[1].startsWith('/') ? tMatch[1] : '/' + tMatch[1];
      topicList.push({
        href: href.endsWith('/') ? href : href + '/',
        name: decodeHtml(tMatch[2].trim()),
        sectionTitle: sTitle,
        sectionId: sId,
        sectionNo: sNum
      });
    }
  }

  return topicList;
}

const allTopics = extractSyllabus();

// 4. Build Full-Fidelity Translation Prompt for Sociology
function buildTranslationPrompt(topic, enPayload) {
  return `You are a distinguished Professor of Sociology (समाजशास्त्र के प्राध्यापक), Senior Hindi Translator & Subject Expert for Uttar Pradesh Secondary Education Service Selection Board (UPSESSB / UPESSC) PGT Sociology (Post Graduate Teacher, Subject Code 16) and UGC NET Sociology examinations.
Provide an exhaustive, master-level 1:1 Hindi (हिन्दी) translation of the following English Sociology study notes and examination content.

STRICT FULL-FIDELITY RULES:
1. DO NOT summarize, abridge, or skip ANY concepts. The Hindi version must have the exact same depth, nuance, and completeness as the English version.
2. Every cited sociologist/theorist (e.g. Auguste Comte, Herbert Spencer, Émile Durkheim, Max Weber, Karl Marx, Vilfredo Pareto, Pitirim Sorokin, Talcott Parsons, Robert K. Merton, C. Wright Mills, Ferdinand Tönnies, Georg Simmel, Charles Horton Cooley, George Herbert Mead, G.S. Ghurye, M.N. Srinivas, D.P. Mukerji, Radhakamal Mukerjee, Irawati Karve, Andre Beteille, S.C. Dube, B.R. Ambedkar, Yogendra Singh, K.M. Kapadia, P.N. Prabhu, A.R. Desai), publication title, publication year, seminal concept, Greek/Latin etymological root, field study, and constitutional article MUST be retained and accurately translated into Hindi (with English technical terms in parentheses where helpful for exam clarity, e.g. "संस्कृतिकरण (Sanskritization)", "यांत्रिक एवं सावयवी एकता (Mechanical & Organic Solidarity)", "सामाजिक तथ्य (Social Facts)", "आदर्श प्रारूप (Ideal Types)").
3. In each section, preserve every sub-bullet and list item in semantic HTML (<p>, <ul>, <li>, <strong>, <em>, <code>).
4. Translate all 10 practice questions and their rationales completely into Hindi.
5. Provide a comparative table, mnemonic, 6 high-yield exam points, 2 common misconceptions, and 4 FAQs in Hindi.

SOURCE ENGLISH CONTENT TO TRANSLATE:
${JSON.stringify(enPayload, null, 2)}

OUTPUT FORMAT:
Respond with ONLY a raw valid JSON object (no markdown \`\`\`json wrappers, no chat preamble) adhering strictly to this schema:
{
  "title_hi": "पूर्ण प्रामाणिक हिन्दी शीर्षक (उदा. समिति (Association))",
  "short_intro_hi": "अंग्रेज़ी परिचय का संक्षिप्त, सटीक हिन्दी अनुवाद; इसमें परीक्षा-प्रचार न जोड़ें...",
  "notes_sections_hi": [
    {
      "heading": "1. सैद्धांतिक एवं शास्त्रीय आधार (Definitional & Classical Framework)",
      "content_html": "<p>पूर्ण अनुवाद जिसमें सभी प्रमुख समाजशास्त्रियों, सिद्धांतों और परिभाषाओं का विस्तृत विवरण हो...</p><ul><li><strong>मुख्य सैद्धांतिक सूत्र:</strong> विवरण...</li></ul>"
    },
    {
      "heading": "2. संरचनात्मक अवधारणाएं, आनुभविक प्रक्रियाएं एवं भारतीय समाजशास्त्रीय परिप्रेक्ष्य (Structural Dynamics & Indian Context)",
      "content_html": "<p>पूर्ण अनुवाद जिसमें प्रक्रियाओं, भारतीय समाजशास्त्रियों के अध्ययनों एवं अवधारणाओं का पूर्ण विवरण हो...</p>"
    },
    {
      "heading": "3. समकालीन गतिशीलता, सामाजिक नीतियां एवं व्यावहारिक आयाम (Contemporary Dynamics & Applied Dimensions)",
      "content_html": "<p>पूर्ण अनुवाद जिसमें समकालीन समाज, संवैधानिक प्रावधानों एवं व्यावहारिक अनुप्रयोगों का पूर्ण विवरण हो...</p>"
    }
  ],
  "comparison_tables_hi": [
    {
      "title": "तुलनात्मक समाजशास्त्रीय विश्लेषण",
      "headers": ["मानदंड / आयाम", "श्रेणी अ", "श्रेणी ब"],
      "rows": [
        ["बिंदु 1", "विवरण", "विवरण"]
      ]
    }
  ],
  "mnemonics_hi": [
    {
      "title": "स्मृति सूत्र / Mnemonic",
      "trick": "सूत्र / Acronym",
      "explanation": "विस्तृत व्याख्या जो परीक्षा में चरणों या वर्गीकरण को याद रखने में सहायक हो।"
    }
  ],
  "exam_points_hi": [
    "परीक्षा तथ्य 1 (समाजशास्त्री का नाम, पुस्तक का नाम व वर्ष, या प्रमुख परिभाषा)",
    "परीक्षा तथ्य 2",
    "परीक्षा तथ्य 3",
    "परीक्षा तथ्य 4",
    "परीक्षा तथ्य 5",
    "परीक्षा तथ्य 6"
  ],
  "common_errors_hi": [
    "भ्रांति 1: परीक्षा की सामान्य गलतफहमी बनाम प्रामाणिक समाजशास्त्रीय सिद्धांत।",
    "भ्रांति 2: परीक्षा का प्रमुख जाल एवं सही उत्तर का चयन कैसे करें।"
  ],
  "practice_questions_hi": [
    {
      "question": "स्पष्ट UP PGT परीक्षा-स्तरीय बहुविकल्पीय प्रश्न हिन्दी में?",
      "options": ["विकल्प क", "विकल्प ख", "विकल्प ग", "विकल्प घ"],
      "correct_index": 0,
      "explanation": "विस्तृत समाजशास्त्रीय व्याख्या जिसमें सही विकल्प और अन्य विकल्पों के संदर्भ का स्पष्ट विश्लेषण हो।"
    }
  ],
  "faqs_hi": [
    {
      "q": "इस समाजशास्त्रीय विषय पर महत्वपूर्ण परीक्षा प्रश्न?",
      "a": "प्रामाणिक एवं स्पष्ट समाजशास्त्रीय उत्तर।"
    }
  ]
}`;
}

// 5. Render Bilingual Page HTML with Persistent Toggle
function renderBilingualPage(topic, enData, hiData) {
  const canonicalUrl = `${DOMAIN}${topic.href}`;
  const pageTitle = `${enData.title} | Sociology | SJ Maths`;
  const metaDesc = `Study ${enData.title} with bilingual sociology notes, key theories, practice questions and answers for UP PGT Sociology.`;

  // --- ENGLISH PANE RENDERING ---
  let enNotesHtml = '';
  (enData.notes_sections || []).forEach((sec, idx) => {
    enNotesHtml += `
      <section class="card content-card" id="en-section-${idx + 1}">
        <h2>${sec.heading}</h2>
        <div class="prose-content">${sec.content_html}</div>
      </section>
    `;
  });

  let enTablesHtml = '';
  if (enData.comparison_tables && enData.comparison_tables.length > 0) {
    enData.comparison_tables.forEach(table => {
      const headers = (table.headers || []).map(h => `<th>${h}</th>`).join('');
      const rows = (table.rows || []).map(r => `<tr>${(r || []).map(c => `<td>${c}</td>`).join('')}</tr>`).join('');
      enTablesHtml += `
        <div class="comparison-card">
          <div class="table-title">${table.title || 'Comparative Sociological Analysis'}</div>
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
  if (enData.mnemonics && enData.mnemonics.length > 0) {
    enData.mnemonics.forEach(m => {
      enMnemonicsHtml += `
        <div class="mnemonic-card">
          <div class="mnemonic-badge">Memory Shortcut / Mnemonic</div>
          <div class="mnemonic-title">${m.title || 'Sociological Mnemonic'}</div>
          <div class="mnemonic-formula">${m.trick || ''}</div>
          <p class="mnemonic-desc">${m.explanation || ''}</p>
        </div>
      `;
    });
  }

  let enPointsHtml = '';
  if (enData.exam_points && enData.exam_points.length > 0) {
    enPointsHtml = `
      <section class="card points-card" id="en-points">
        <h2>High-Yield Exam Points for UP PGT Sociology</h2>
        <ul class="points-list">
          ${enData.exam_points.map(pt => `<li>${pt}</li>`).join('\n          ')}
        </ul>
      </section>
    `;
  }

  let enErrorsHtml = '';
  if (enData.common_errors && enData.common_errors.length > 0) {
    enErrorsHtml = `
      <section class="card errors-card" id="en-traps">
        <h2>Common Misconceptions &amp; Exam Traps</h2>
        <ul class="errors-list">
          ${enData.common_errors.map(err => `<li>${err}</li>`).join('\n          ')}
        </ul>
      </section>
    `;
  }

  let enQuestionsHtml = '';
  if (enData.practice_questions && enData.practice_questions.length > 0) {
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
          <ul class="mcq-options">${optionsHtml}</ul>
          <div class="mcq-reveal">
            <button type="button" class="btn-reveal" onclick="toggleExp('en-exp-${i}')">Show Answer &amp; Explanation</button>
            <div class="mcq-explanation" id="en-exp-${i}" style="display:none;">
              <strong>Correct Option: ${correctLetter}${correctText ? ' (' + correctText + ')' : ''}</strong>
              <p>${q.explanation || 'Refer to theoretical notes above.'}</p>
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
        <div class="mcq-container">${qList}</div>
      </section>
    `;
  }

  let enFaqsHtml = '';
  if (enData.faqs && enData.faqs.length > 0) {
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

  // --- HINDI PANE RENDERING ---
  let hiNotesHtml = '';
  (hiData.notes_sections_hi || []).forEach((sec, idx) => {
    hiNotesHtml += `
      <section class="card content-card" id="hi-section-${idx + 1}">
        <h2>${sec.heading}</h2>
        <div class="prose-content">${sec.content_html}</div>
      </section>
    `;
  });

  let hiTablesHtml = '';
  if (hiData.comparison_tables_hi && hiData.comparison_tables_hi.length > 0) {
    hiData.comparison_tables_hi.forEach(table => {
      const headers = (table.headers || []).map(h => `<th>${h}</th>`).join('');
      const rows = (table.rows || []).map(r => `<tr>${(r || []).map(c => `<td>${c}</td>`).join('')}</tr>`).join('');
      hiTablesHtml += `
        <div class="comparison-card">
          <div class="table-title">${table.title || 'तुलनात्मक समाजशास्त्रीय विश्लेषण'}</div>
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
  if (hiData.mnemonics_hi && hiData.mnemonics_hi.length > 0) {
    hiData.mnemonics_hi.forEach(m => {
      hiMnemonicsHtml += `
        <div class="mnemonic-card">
          <div class="mnemonic-badge">स्मृति सूत्र / Mnemonic</div>
          <div class="mnemonic-title">${m.title || 'समाजशास्त्रीय स्मृति सूत्र'}</div>
          <div class="mnemonic-formula">${m.trick || ''}</div>
          <p class="mnemonic-desc">${m.explanation || ''}</p>
        </div>
      `;
    });
  }

  let hiPointsHtml = '';
  if (hiData.exam_points_hi && hiData.exam_points_hi.length > 0) {
    hiPointsHtml = `
      <section class="card points-card" id="hi-points">
        <h2>UP PGT समाजशास्त्र परीक्षा के लिए महत्वपूर्ण तथ्य</h2>
        <ul class="points-list">
          ${hiData.exam_points_hi.map(pt => `<li>${pt}</li>`).join('\n          ')}
        </ul>
      </section>
    `;
  }

  let hiErrorsHtml = '';
  if (hiData.common_errors_hi && hiData.common_errors_hi.length > 0) {
    hiErrorsHtml = `
      <section class="card errors-card" id="hi-traps">
        <h2>सामान्य भ्रांतियां एवं परीक्षा के जाल (Common Traps)</h2>
        <ul class="errors-list">
          ${hiData.common_errors_hi.map(err => `<li>${err}</li>`).join('\n          ')}
        </ul>
      </section>
    `;
  }

  let hiQuestionsHtml = '';
  if (hiData.practice_questions_hi && hiData.practice_questions_hi.length > 0) {
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
          <ul class="mcq-options">${optionsHtml}</ul>
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
        <div class="mcq-container">${qList}</div>
      </section>
    `;
  }

  let hiFaqsHtml = '';
  if (hiData.faqs_hi && hiData.faqs_hi.length > 0) {
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

  // Combined Schema for FAQs
  const allFaqEntities = [
    ...(enData.faqs || []).map(f => ({
      "@type": "Question",
      "name": f.q,
      "acceptedAnswer": { "@type": "Answer", "text": f.a }
    })),
    ...(hiData.faqs_hi || []).map(f => ({
      "@type": "Question",
      "name": f.q,
      "acceptedAnswer": { "@type": "Answer", "text": f.a }
    }))
  ];

  const faqSchema = allFaqEntities.length > 0 ? `
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": ${JSON.stringify(allFaqEntities, null, 2)}
  }
  </script>` : '';

  return `<!doctype html>
<html lang="en" data-soc-lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>${pageTitle}</title>
  <meta name="description" content="${metaDesc}">
  <meta name="robots" content="index,follow,max-image-preview:large">
  <meta name="author" content="SJ Maths">
  <meta name="theme-color" content="#0f766e">
  <link rel="canonical" href="${canonicalUrl}">
  <link rel="icon" type="image/png" href="/favicon.png">

  <!-- Open Graph -->
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="SJ Maths">
  <meta property="og:title" content="${pageTitle}">
  <meta property="og:description" content="${metaDesc}">
  <meta property="og:url" content="${canonicalUrl}">
  <meta property="og:image" content="https://sjmaths.com/assets/images/og-default.jpg">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="${pageTitle}">
  <meta name="twitter:description" content="${metaDesc}">
  <meta name="twitter:image" content="https://sjmaths.com/assets/images/og-default.jpg">

  <!-- Pre-render anti-flicker language check -->
  <script>
    (function() {
      try {
        var savedLang = localStorage.getItem('sjmaths_soc_lang');
        if (savedLang === 'hi' || savedLang === 'en') {
          document.documentElement.setAttribute('data-soc-lang', savedLang);
          document.documentElement.lang = savedLang;
        } else {
          document.documentElement.setAttribute('data-soc-lang', 'en');
          document.documentElement.lang = 'en';
        }
      } catch (e) {}
    })();
  </script>

  <!-- Structured Data (JSON-LD) -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "LearningResource",
    "name": "${enData.title} | ${hiData.title_hi}",
    "headline": "${enData.title} — Bilingual Study Notes & MCQs",
    "description": "${metaDesc}",
    "url": "${canonicalUrl}",
    "inLanguage": ["en", "hi"],
    "learningResourceType": "Study Guide / Quiz",
    "educationalLevel": "Post Graduate Teacher (UP PGT Subject Code 16)",
    "isPartOf": {
      "@type": "WebSite",
      "name": "SJ Maths",
      "url": "https://sjmaths.com/"
    },
    "breadcrumb": {
      "@type": "BreadcrumbList",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://sjmaths.com/" },
        { "@type": "ListItem", "position": 2, "name": "UP PGT Sociology", "item": "https://sjmaths.com/up-pgt-sociology/" },
        { "@type": "ListItem", "position": 3, "name": "${topic.sectionTitle}", "item": "${canonicalUrl}" },
        { "@type": "ListItem", "position": 4, "name": "${enData.title}", "item": "${canonicalUrl}" }
      ]
    }
  }
  </script>${faqSchema}

  <style>
    :root {
      --bg: #f6f8fb;
      --card-bg: #ffffff;
      --ink: #18212f;
      --ink-muted: #536174;
      --line: #e1e6ed;
      --soft-line: #eff3f7;
      --brand: #0f766e;
      --brand-dark: #115e59;
      --brand-soft: #eaf8f5;
      --accent: #0d9488;
      --accent-soft: #f0fdfa;
      --success: #15803d;
      --success-soft: #f0fdf4;
      --shadow: 0 12px 34px rgba(15,118,110,.07);
      --radius: 16px;
      --header-h: 66px;
    }
    * { box-sizing: border-box; }
    html { scroll-behavior: smooth; }
    body {
      margin: 0; color: var(--ink);
      background: radial-gradient(circle at 100% 0,rgba(15,118,110,.05),transparent 28rem), var(--bg);
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

    /* Language Switcher Button */
    .lang-switcher-wrap {
      display: inline-flex; align-items: center; background: #eaf8f5; border-radius: 999px;
      padding: 3px; border: 1px solid #cce9e4;
    }
    .lang-btn {
      border: 0; background: transparent; padding: 6px 14px; border-radius: 999px;
      font-size: .78rem; font-weight: 800; color: #0f766e; cursor: pointer; transition: all .15s ease;
    }
    .lang-btn:hover { color: #115e59; }

    /* Language-dependent visibility */
    html[data-soc-lang="en"] .lang-pane-hi { display: none !important; }
    html[data-soc-lang="hi"] .lang-pane-en { display: none !important; }
    html[data-soc-lang="en"] .lang-btn[data-lang="en"] {
      background: var(--brand); color: #fff; box-shadow: 0 2px 6px rgba(15,118,110,.25);
    }
    html[data-soc-lang="hi"] .lang-btn[data-lang="hi"] {
      background: var(--brand); color: #fff; box-shadow: 0 2px 6px rgba(15,118,110,.25);
    }

    /* Breadcrumbs */
    .breadcrumb {
      display: flex; gap: 8px; align-items: center; font-size: .78rem; color: var(--ink-muted);
      margin: 24px 0 16px; flex-wrap: wrap;
    }
    .breadcrumb a { color: var(--ink-muted); }
    .breadcrumb a:hover { color: var(--brand); }
    .breadcrumb span.sep { color: #94a3b8; }

    /* Topic Hero */
    .topic-hero {
      background: var(--card-bg); border: 1px solid var(--line); border-radius: var(--radius);
      padding: 32px 36px; box-shadow: var(--shadow); position: relative; overflow: hidden; margin-bottom: 24px;
    }
    .topic-hero::before {
      content: ""; position: absolute; left: 0; top: 0; bottom: 0; width: 6px;
      background: linear-gradient(180deg, #0f766e, #115e59);
    }
    .hero-top-row { display: flex; justify-content: space-between; align-items: center; gap: 12px; margin-bottom: 8px; }
    .kicker { font-size: .75rem; text-transform: uppercase; font-weight: 800; letter-spacing: .08em; color: var(--brand); }
    h1, .topic-page-title { margin: 0 0 12px; font-size: clamp(1.6rem, 3.2vw, 2.3rem); line-height: 1.22; color: var(--ink); letter-spacing: -.02em; font-weight: 700; }
    .lead { margin: 0 0 16px; color: var(--ink-muted); font-size: .98rem; line-height: 1.6; }
    .topic-chips { display: flex; gap: 8px; flex-wrap: wrap; }
    .chip { padding: 4px 11px; border-radius: 999px; font-size: .7rem; font-weight: 750; border: 1px solid transparent; }
    .chip-pgt { background: #eaf8f5; color: #0f766e; border-color: #cce9e4; }
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
    .prose-content p { font-size: .96rem; line-height: 1.75; color: #283542; margin-bottom: 14px; }
    .prose-content ul { margin: 10px 0 18px 22px; padding: 0; }
    .prose-content li { font-size: .94rem; line-height: 1.7; color: #283542; margin-bottom: 8px; }
    .prose-content strong { color: #0f766e; }

    /* Comparison Table */
    .comparison-card {
      background: var(--card-bg); border: 1px solid var(--line); border-radius: var(--radius);
      padding: 24px 28px; box-shadow: var(--shadow); margin-bottom: 24px; overflow: hidden;
    }
    .table-title { font-weight: 800; font-size: 1.08rem; color: var(--ink); margin-bottom: 14px; }
    .table-responsive { overflow-x: auto; -webkit-overflow-scrolling: touch; }
    .styled-table { width: 100%; border-collapse: collapse; font-size: .88rem; text-align: left; }
    .styled-table th { background: var(--brand-soft); color: var(--brand); padding: 11px 14px; font-weight: 750; border: 1px solid var(--line); }
    .styled-table td { padding: 10px 14px; border: 1px solid var(--line); vertical-align: top; }
    .styled-table tr:nth-child(even) { background: #fafbfd; }

    /* Mnemonic Card */
    .mnemonic-card {
      background: linear-gradient(135deg, #f0fdfa, #ccfbf1); border: 1px solid #99f6e4;
      border-radius: var(--radius); padding: 22px 26px; margin-bottom: 24px;
    }
    .mnemonic-badge {
      display: inline-block; background: #0f766e; color: white; font-size: .68rem;
      text-transform: uppercase; font-weight: 800; letter-spacing: .06em; padding: 3px 9px; border-radius: 6px; margin-bottom: 8px;
    }
    .mnemonic-title { font-size: 1.05rem; font-weight: 800; color: #115e59; margin-bottom: 6px; }
    .mnemonic-formula {
      font-size: 1.15rem; font-weight: 900; color: #0f766e; font-family: monospace;
      background: rgba(255,255,255,.9); padding: 6px 12px; border-radius: 8px; display: inline-block; margin-bottom: 8px;
    }
    .mnemonic-desc { font-size: .9rem; color: #134e4a; margin: 0; line-height: 1.55; }

    /* Points & Errors List */
    .points-card h2 { color: #0f766e; }
    .points-list { margin: 0; padding-left: 20px; }
    .points-list li { margin-bottom: 9px; font-size: .92rem; color: #283542; line-height: 1.6; }
    .errors-card { background: #fffbf5; border-color: #fed7aa; }
    .errors-card h2 { color: #9a3412; border-bottom-color: #ffedd5; }
    .errors-list { margin: 0; padding-left: 20px; }
    .errors-list li { margin-bottom: 9px; font-size: .92rem; color: #7c2d12; line-height: 1.6; }

    /* Practice MCQs */
    .mcq-card h2 { color: var(--brand); }
    .mcq-item {
      background: #fafbfd; border: 1px solid var(--line); border-radius: 12px;
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
      background: var(--brand-soft); border: 1px solid #cce9e4; color: var(--brand);
      padding: 7px 14px; border-radius: 8px; font-size: .8rem; font-weight: 750; cursor: pointer;
    }
    .btn-reveal:hover { background: #daf3ef; }
    .mcq-explanation {
      margin-top: 12px; padding: 12px 16px; background: var(--success-soft);
      border: 1px solid #bbf7d0; border-radius: 8px; font-size: .86rem; color: #166534;
    }
    .mcq-explanation p { margin: 6px 0 0; }

    /* FAQs */
    .faq-item { margin-bottom: 16px; padding-bottom: 14px; border-bottom: 1px solid var(--soft-line); }
    .faq-item:last-child { border-bottom: none; margin-bottom: 0; padding-bottom: 0; }
    .faq-q { font-size: .98rem; font-weight: 750; color: var(--brand); margin: 0 0 6px; }
    .faq-a { font-size: .9rem; color: #334155; margin: 0; line-height: 1.6; }

    /* Cross navigation bar */
    .cross-nav { margin: 32px 0 48px; }
    .cross-nav-card {
      background: var(--card-bg); border: 1px solid var(--line); border-radius: var(--radius);
      padding: 20px 24px; display: flex; align-items: center; justify-content: space-between;
      gap: 12px; transition: border-color .2s; text-decoration: none;
    }
    .cross-nav-card:hover { border-color: var(--accent); }
    .cross-nav-card strong { display: block; font-size: .98rem; color: var(--ink); }
    .cross-nav-card span { font-size: .8rem; color: var(--ink-muted); }

    /* Footer */
    .site-footer {
      padding: 32px 0; border-top: 1px solid var(--line); background: #ffffff;
      font-size: .8rem; color: var(--ink-muted); text-align: center; margin-top: 48px;
    }
    @media(max-width: 640px) {
      .topic-hero { padding: 22px 20px; }
      .card { padding: 20px 18px; }
    }
  </style>
  <script>
    function toggleExp(id) {
      const exp = document.getElementById(id);
      if (exp) {
        exp.style.display = exp.style.display === 'none' ? 'block' : 'none';
      }
    }
    function switchSocLang(lang) {
      document.documentElement.setAttribute('data-soc-lang', lang);
      document.documentElement.lang = lang;
      try {
        localStorage.setItem('sjmaths_soc_lang', lang);
      } catch (e) {}
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
        <span class="brand-sub">Sociology Study Portal</span>
      </span>
    </a>
    <div style="display:flex;align-items:center;gap:12px;">
      <div class="lang-switcher-wrap" role="group" aria-label="Language Switcher">
        <button type="button" class="lang-btn" data-lang="en" onclick="switchSocLang('en')">English</button>
        <button type="button" class="lang-btn" data-lang="hi" onclick="switchSocLang('hi')">हिन्दी</button>
      </div>
      <a href="/up-pgt-sociology/" style="font-size:.82rem;font-weight:700;color:var(--brand);">← Syllabus</a>
    </div>
  </div>
</header>

<main class="wrap">
  <!-- ENGLISH VERSION -->
  <div class="lang-pane-en">
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="/">Home</a>
      <span class="sep">›</span>
      <a href="/up-pgt-sociology/">Sociology</a>
      <span class="sep">›</span>
      <span>${topic.sectionTitle}</span>
      <span class="sep">›</span>
      <span>${enData.title}</span>
    </nav>

    <article class="topic-hero">
      <div class="hero-top-row">
        <div class="kicker">Section ${topic.sectionNo} • ${topic.sectionTitle}</div>
        <div class="lang-switcher-wrap">
          <button type="button" class="lang-btn" data-lang="en" onclick="switchSocLang('en')">English</button>
          <button type="button" class="lang-btn" data-lang="hi" onclick="switchSocLang('hi')">हिन्दी</button>
        </div>
      </div>
      <h1 lang="en">${enData.title}</h1>
      <p class="lead">${enData.short_intro}</p>
      <div class="topic-chips">
        <span class="chip chip-pgt">UP PGT Sociology • Code 16</span>
        <span class="chip chip-unit">${topic.sectionTitle}</span>
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

  <!-- HINDI VERSION -->
  <div class="lang-pane-hi" lang="hi">
    <nav class="breadcrumb" aria-label="ब्रेडक्रम्ब">
      <a href="/">होम</a>
      <span class="sep">›</span>
      <a href="/up-pgt-sociology/">समाजशास्त्र (Sociology)</a>
      <span class="sep">›</span>
      <span>${topic.sectionTitle}</span>
      <span class="sep">›</span>
      <span>${hiData.title_hi}</span>
    </nav>

    <article class="topic-hero">
      <div class="hero-top-row">
        <div class="kicker">अनुभाग ${topic.sectionNo} • ${topic.sectionTitle}</div>
        <div class="lang-switcher-wrap">
          <button type="button" class="lang-btn" data-lang="en" onclick="switchSocLang('en')">English</button>
          <button type="button" class="lang-btn" data-lang="hi" onclick="switchSocLang('hi')">हिन्दी</button>
        </div>
      </div>
      <div class="topic-page-title" role="heading" aria-level="1" lang="hi">${hiData.title_hi}</div>
      <p class="lead">${hiData.short_intro_hi}</p>
      <div class="topic-chips">
        <span class="chip chip-pgt">UP PGT समाजशास्त्र • कोड 16</span>
        <span class="chip chip-unit">${topic.sectionTitle}</span>
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
    <a class="cross-nav-card" href="/up-pgt-sociology/">
      <div>
        <strong>UP PGT Sociology Study Tracker</strong>
        <span>Track all 11 sections &amp; 88 curriculum topics</span>
      </div>
      <span aria-hidden="true" style="font-size:1.3rem;font-weight:bold;color:var(--brand);">→</span>
    </a>
  </section>
</main>

<footer class="site-footer">
  <div class="wrap">
    <p>© SJ Maths</p>
    <p><a href="/privacy-policy/">Privacy Policy</a> • <a href="/up-pgt-sociology/">UP PGT Sociology Directory</a> • <a href="/">Home</a></p>
  </div>
</footer>

</body>
</html>`;
}

// 6. Main Execution Pipeline
async function run() {
  console.log('================================================================');
  console.log('SJ Maths — UP PGT Sociology 1:1 Full Hindi Translation Pipeline');
  console.log(`Model: ${MODEL_NAME} (Fallback: ${FALLBACK_MODELS.join(', ')})`);
  console.log(`Key:   ${activeKeyObj.name} (${activeKeyObj.key ? activeKeyObj.key.substring(0, 8) + '...' + activeKeyObj.key.slice(-4) : 'NONE'})`);
  console.log(`Total Topics: ${allTopics.length}`);
  console.log('================================================================');

  let eligibleTopics = allTopics;

  if (TARGET_SECTION) {
    eligibleTopics = eligibleTopics.filter(t => t.sectionId === TARGET_SECTION || t.sectionNo === TARGET_SECTION);
    console.log(`Filtering for section: ${TARGET_SECTION} (${eligibleTopics.length} topics)`);
  }

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
      console.log(`[${i + 1}/${eligibleTopics.length}] Waiting for file to be generated: ${relativePath}/index.html. Skipping.`);
      skippedCount++;
      continue;
    }

    const existingHtml = fs.readFileSync(targetFile, 'utf8');

    // Skip if already translated with full fidelity
    if (statusMap[topic.href]?.translated === true && statusMap[topic.href]?.fullFidelity === true && !FORCE) {
      if (existingHtml.includes('lang-pane-hi') && existingHtml.includes('data-soc-lang')) {
        skippedCount++;
        continue;
      }
    }

    console.log(`\n[${i + 1}/${eligibleTopics.length}] Translating 1:1 to Hindi: ${topic.name}`);
    console.log(`  Path: ${topic.href} (Section ${topic.sectionNo} • ${topic.sectionTitle})`);

    // Extract English content from existing HTML
    const h1Match = existingHtml.match(/<h1>([^<]+)<\/h1>/);
    const leadMatch = existingHtml.match(/<p class="lead">([\s\S]*?)<\/p>/);

    // Extract English notes sections
    const secRegex = /<section class="card content-card"[^>]*>[\s\S]*?<h2>([^<]+)<\/h2>[\s\S]*?<div class="prose-content">([\s\S]*?)<\/div>[\s\S]*?<\/section>/g;
    let sMatch;
    const extractedSections = [];
    while ((sMatch = secRegex.exec(existingHtml)) !== null) {
      extractedSections.push({
        heading: sMatch[1].trim(),
        content_html: sMatch[2].trim()
      });
    }

    // Extract English comparison tables
    const tableRegex = /<div class="comparison-card">[\s\S]*?<div class="table-title">([^<]+)<\/div>[\s\S]*?<table[^>]*>([\s\S]*?)<\/table>[\s\S]*?<\/div>/g;
    let tMatch;
    const extractedTables = [];
    while ((tMatch = tableRegex.exec(existingHtml)) !== null) {
      const tableTitle = tMatch[1].trim();
      const tableBody = tMatch[2];
      const thMatches = [...tableBody.matchAll(/<th>([^<]+)<\/th>/g)].map(m => m[1].trim());
      const trMatches = [...tableBody.matchAll(/<tr>([\s\S]*?)<\/tr>/g)];
      const rows = [];
      trMatches.forEach(tr => {
        const tds = [...tr[1].matchAll(/<td>([\s\S]*?)<\/td>/g)].map(m => m[1].trim());
        if (tds.length > 0) rows.push(tds);
      });
      extractedTables.push({ title: tableTitle, headers: thMatches, rows });
    }

    // Extract English mnemonics
    const mnemRegex = /<div class="mnemonic-card">[\s\S]*?<div class="mnemonic-title">([^<]+)<\/div>[\s\S]*?<div class="mnemonic-formula">([^<]+)<\/div>[\s\S]*?<p class="mnemonic-desc">([^<]+)<\/p>[\s\S]*?<\/div>/g;
    let mMatch;
    const extractedMnemonics = [];
    while ((mMatch = mnemRegex.exec(existingHtml)) !== null) {
      extractedMnemonics.push({
        title: mMatch[1].trim(),
        trick: mMatch[2].trim(),
        explanation: mMatch[3].trim()
      });
    }

    // Extract English exam points
    const ptsMatch = existingHtml.match(/<section class="card points-card"[^>]*>[\s\S]*?<ul class="points-list">([\s\S]*?)<\/ul>[\s\S]*?<\/section>/);
    const extractedPoints = ptsMatch ? [...ptsMatch[1].matchAll(/<li>([^<]+)<\/li>/g)].map(m => m[1].trim()) : [];

    // Extract English common traps
    const errMatch = existingHtml.match(/<section class="card errors-card"[^>]*>[\s\S]*?<ul class="errors-list">([\s\S]*?)<\/ul>[\s\S]*?<\/section>/);
    const extractedErrors = errMatch ? [...errMatch[1].matchAll(/<li>([^<]+)<\/li>/g)].map(m => m[1].trim()) : [];

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

    // Extract English FAQs
    const faqRegex = /<div class="faq-item">[\s\S]*?<h3 class="faq-q">([^<]+)<\/h3>[\s\S]*?<p class="faq-a">([^<]+)<\/p>[\s\S]*?<\/div>/g;
    let fMatch;
    const extractedFaqs = [];
    while ((fMatch = faqRegex.exec(existingHtml)) !== null) {
      extractedFaqs.push({
        q: fMatch[1].trim(),
        a: fMatch[2].trim()
      });
    }

    const enPayload = {
      title: h1Match ? h1Match[1].trim() : topic.name,
      short_intro: leadMatch ? leadMatch[1].trim() : '',
      notes_sections: extractedSections,
      comparison_tables: extractedTables,
      mnemonics: extractedMnemonics,
      exam_points: extractedPoints,
      common_errors: extractedErrors,
      practice_questions: extractedQuestions,
      faqs: extractedFaqs
    };

    const prompt = buildTranslationPrompt(topic, enPayload);
    let hiData = null;

    // Retry loop with model fallback (gemini-3.1-flash-lite -> gemini-3.5-flash-lite)
    for (let attempt = 0; attempt < 4 && !hiData; attempt++) {
      const currentModel = FALLBACK_MODELS[Math.floor(attempt / 2) % FALLBACK_MODELS.length];
      try {
        console.log(`  Calling Gemini (${currentModel}) using ${activeKeyObj.name} [Attempt ${attempt + 1}]...`);
        const response = await ai.models.generateContent({
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
        if (err.message.includes('429') || err.message.includes('Quota') || err.message.includes('ResourceExhausted')) {
          switchKeyIfAvailable();
        }
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
    const renderedHtml = externalizeSociologyBilingualStyle(
      renderBilingualPage(topic, enPayload, hiData),
      sociologyBilingualCss,
      { strict: true },
    );

    if (!DRY_RUN) {
      fs.writeFileSync(targetFile, renderedHtml, 'utf8');

      statusMap[topic.href] = {
        translated: true,
        fullFidelity: true,
        titleEn: enPayload.title,
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
  console.log(`Sociology 1:1 Hindi Translation Finished!`);
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
