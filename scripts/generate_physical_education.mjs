#!/usr/bin/env node
/**
 * ============================================================================
 * SJ Maths — Physical Education Content & Study Notes Generator Pipeline
 * Powered by Google Gemini API via @google/genai SDK
 * Generates canonical, high-yield study notes, theory, tables, mnemonics,
 * and practice MCQs for all 308 UP TGT & PGT Physical Education topics.
 * ============================================================================
 */

import fs from 'node:fs';
import path from 'node:path';
import 'dotenv/config';
import { GoogleGenAI } from '@google/genai';
import { jsonrepair } from 'jsonrepair';

const ROOT = process.cwd();
const DOMAIN = 'https://sjmaths.com';
const STATUS_FILE = path.join(ROOT, 'content-generation-status-physical-education.json');

// 1. Parse command line arguments
const args = process.argv.slice(2);
const DRY_RUN = args.includes('--dry-run');
const FORCE = args.includes('--force');
const TEMPLATE_ONLY = args.includes('--template-only'); // generate quick structured shell without AI
const LIMIT = (() => {
  const idx = args.indexOf('--limit');
  return idx !== -1 && args[idx + 1] ? parseInt(args[idx + 1], 10) : null;
})();
const TARGET_TOPIC = (() => {
  const idx = args.indexOf('--topic');
  return idx !== -1 && args[idx + 1] ? args[idx + 1] : null;
})();
const TARGET_BRANCH = (() => {
  const idx = args.indexOf('--branch');
  return idx !== -1 && args[idx + 1] ? args[idx + 1] : null;
})();
const MODEL_NAME = (() => {
  const idx = args.indexOf('--model');
  return idx !== -1 && args[idx + 1] ? args[idx + 1] : 'gemini-3.5-flash-lite';
})();
const FALLBACK_MODELS = [MODEL_NAME, 'gemini-2.5-flash-lite'];

// Load all available API Keys for multi-key rotation
const apiKeys = [...new Set([
  process.env.GEMINI_API_KEY_1,
  process.env.GEMINI_API_KEY_2,
  process.env.GEMINI_API_KEY
].filter(Boolean))];

if (!TEMPLATE_ONLY && apiKeys.length === 0) {
  console.error('ERROR: No GEMINI_API_KEY found in .env. Run with --template-only or configure .env.');
  process.exit(1);
}

const aiClients = apiKeys.map((key, i) => ({
  id: i + 1,
  preview: key.substring(0, 10) + '...' + key.slice(-6),
  client: new GoogleGenAI({ apiKey: key })
}));
let clientIndex = 0;

function getAiClient() {
  if (aiClients.length === 0) return null;
  const clientObj = aiClients[clientIndex % aiClients.length];
  clientIndex++;
  return clientObj;
}

// Load generation status tracking
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

// 2. Extract syllabus definitions from tracker files
function extractSyllabus(filePath) {
  const full = path.join(ROOT, filePath);
  if (!fs.existsSync(full)) {
    console.error(`Tracker file not found: ${full}`);
    return [];
  }
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

// 3. Aggregate unique topics
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
          inPgt: false,
          coverage: 'full'
        });
      } else {
        const item = topicsMap.get(cleanHref);
        item.inTgt = true;
        item.tgtUnit = unit.unit;
        item.tgtUnitTitle = unit.title;
      }
    }
  }
}

for (const unit of pgtSyllabus) {
  for (const [groupTitle, items] of unit.groups) {
    for (const [name, href, coverage, tgtUnitRef] of items) {
      const cleanHref = href.startsWith('/') ? href : '/' + href;
      if (!topicsMap.has(cleanHref)) {
        topicsMap.set(cleanHref, {
          name,
          href: cleanHref,
          pgtUnit: unit.unit,
          pgtUnitTitle: unit.title,
          groupTitle,
          inTgt: coverage === 'full',
          inPgt: true,
          coverage: coverage || 'pgt',
          tgtUnitRef: tgtUnitRef || ''
        });
      } else {
        const item = topicsMap.get(cleanHref);
        item.inPgt = true;
        item.pgtUnit = unit.unit;
        item.pgtUnitTitle = unit.title;
        item.coverage = coverage || 'full';
        item.tgtUnitRef = tgtUnitRef || '';
      }
    }
  }
}

const topics = Array.from(topicsMap.values());

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

function getSectionName(slug) {
  return SECTION_TITLES[slug] || slug.split('-').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' ');
}

// 4. Gemini AI Prompt Builder
function buildPrompt(topic) {
  const parts = topic.href.split('/').filter(Boolean);
  const branchSlug = parts[1] || 'general';
  const branchTitle = getSectionName(branchSlug);

  return `You are a distinguished Professor of Physical Education, Sports Scientist, and Senior Examination Expert for Uttar Pradesh Secondary Education Service Selection Board (UPSESSB / UPESSC) TGT and PGT Physical Education examinations.

Generate exhaustive, master-level study notes and practice questions for this exact curriculum topic:
- Subject: Physical Education (Sharirik Shiksha)
- Branch: ${branchTitle}
- Group: ${topic.groupTitle}
- Topic: ${topic.name}
- Canonical URL: ${topic.href}
- Target Examination: UP TGT & UP PGT Physical Education

CONTENT DEPTH & ACADEMIC STANDARDS:
1. Provide rich, highly authoritative academic study material strictly aligned with National Council for Teacher Education (NCTE), Lakshmibai National Institute of Physical Education (LNIPE), and standard Indian university Physical Education curricula.
2. Provide precise terminology, foundational definitions by classic scholars (e.g. Clark, Bucher, Williams, Barrow, Sheldon, etc.), physiological/biomechanical principles, standard rules, measurement numbers (meters, grams, seconds, angles), formulas, and clinical/pedagogical applications.
3. Structure your response with:
   - In-depth, readable notes sections using semantic HTML (<p>, <ul>, <li>, <strong>, <em>, <code>).
   - Comparison tables contrasting related categories, somatotypes, principles, or methods.
   - Memory tricks / mnemonics for memorizing classifications, formulas, or chronological orders.
   - High-yield direct factual takeaways for quick last-minute revision.
   - Common exam traps and misconceptions.
   - Exactly 10 practice multiple-choice questions (MCQs) with 4 options each, correct answer index (0 to 3), and comprehensive rationale explaining why the answer is correct and why other options are incorrect.
   - 4 FAQs addressing top search queries.

OUTPUT FORMAT:
Respond with ONLY a valid, raw JSON object (no markdown \`\`\`json wrappers, no chat preamble) adhering strictly to this schema:
{
  "title": "${topic.name}",
  "short_intro": "2 to 3 sentences introducing the core concept, its academic significance, and why it is critical for UP TGT/PGT Physical Education.",
  "notes_sections": [
    {
      "heading": "1. Definitional Framework and Theoretical Foundations",
      "content_html": "<p>Deep, academic explanation with authoritative definitions...</p><ul><li><strong>Key Principle:</strong> Detail...</li></ul>"
    },
    {
      "heading": "2. Physiological / Biomechanical / Practical Principles",
      "content_html": "<p>Detailed breakdown of scientific mechanisms, rules, classifications, measurement formulas, or procedures...</p>"
    },
    {
      "heading": "3. Application in Sports Performance, Coaching & Pedagogy",
      "content_html": "<p>How this topic applies to athletes, training plans, classroom management, or competition standards...</p>"
    }
  ],
  "comparison_tables": [
    {
      "title": "Comparative Analysis Table",
      "headers": ["Parameter / Feature", "Category A", "Category B"],
      "rows": [
        ["Criterion 1", "Detail A", "Detail B"],
        ["Criterion 2", "Detail A", "Detail B"]
      ]
    }
  ],
  "mnemonics": [
    {
      "title": "Memory Shortcut / Mnemonic",
      "trick": "ACRONYM / Memory phrase",
      "explanation": "Detailed breakdown of the shortcut to remember stages, types, or rules during the exam."
    }
  ],
  "exam_points": [
    "High-yield factual point 1 (date, standard formula, author, dimension, or physiological number)",
    "High-yield factual point 2",
    "High-yield factual point 3",
    "High-yield factual point 4",
    "High-yield factual point 5",
    "High-yield factual point 6"
  ],
  "common_errors": [
    "Misconception 1: What students mistakenly believe vs. the scientifically accurate fact.",
    "Misconception 2: Common exam trap and how to answer accurately."
  ],
  "practice_questions": [
    {
      "question": "Clear examination-style MCQ question text?",
      "options": ["Option A", "Option B", "Option C", "Option D"],
      "correct_index": 0,
      "explanation": "Thorough explanation of the correct answer and examination reference."
    }
  ],
  "faqs": [
    {
      "q": "Common question about this topic?",
      "a": "Authoritative, clear answer summarizing key facts."
    }
  ]
}`;
}

// 5. Render Study Notes HTML Page
function renderFullStudyPage(topic, data) {
  const canonicalUrl = `${DOMAIN}${topic.href}`;
  const parts = topic.href.split('/').filter(Boolean);
  const branchSlug = parts[1] || 'general';
  const branchTitle = getSectionName(branchSlug);
  const branchUrl = `/physical-education/${branchSlug}/`;

  const examBadges = [];
  if (topic.inTgt) examBadges.push('<span class="chip chip-tgt">UP TGT Physical Education</span>');
  if (topic.inPgt) examBadges.push('<span class="chip chip-pgt">UP PGT Physical Education</span>');
  if (topic.tgtUnit) examBadges.push(`<span class="chip chip-unit">TGT Unit ${topic.tgtUnit}</span>`);
  if (topic.pgtUnit) examBadges.push(`<span class="chip chip-unit">PGT Unit ${topic.pgtUnit}</span>`);

  const pageTitle = `${data.title} — Study Notes, MCQs & Revision | Physical Education | SJ Maths`;
  const metaDesc = `Master ${data.title} for UP TGT and UP PGT Physical Education. In-depth theory notes, scientific principles, comparison tables, mnemonics, and practice MCQs with explanations.`;

  // Render notes sections
  let notesHtml = '';
  (data.notes_sections || []).forEach((sec, idx) => {
    notesHtml += `
      <section class="card content-card" id="section-${idx + 1}">
        <h2>${sec.heading}</h2>
        <div class="prose-content">
          ${sec.content_html}
        </div>
      </section>
    `;
  });

  // Render comparison tables
  let tablesHtml = '';
  if (data.comparison_tables && data.comparison_tables.length > 0) {
    data.comparison_tables.forEach(table => {
      const headers = table.headers.map(h => `<th>${h}</th>`).join('');
      const rows = table.rows.map(r => `<tr>${r.map(c => `<td>${c}</td>`).join('')}</tr>`).join('');
      tablesHtml += `
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

  // Render mnemonics
  let mnemonicsHtml = '';
  if (data.mnemonics && data.mnemonics.length > 0) {
    data.mnemonics.forEach(m => {
      mnemonicsHtml += `
        <div class="mnemonic-card">
          <div class="mnemonic-badge">Memory Trick / Mnemonic</div>
          <div class="mnemonic-title">${m.title}</div>
          <div class="mnemonic-formula">${m.trick}</div>
          <p class="mnemonic-desc">${m.explanation}</p>
        </div>
      `;
    });
  }

  // Render high-yield points
  let pointsHtml = '';
  if (data.exam_points && data.exam_points.length > 0) {
    pointsHtml = `
      <section class="card points-card" id="exam-points">
        <h2>High-Yield Exam Points for UP TGT &amp; PGT</h2>
        <ul class="points-list">
          ${data.exam_points.map(pt => `<li>${pt}</li>`).join('\n          ')}
        </ul>
      </section>
    `;
  }

  // Render common errors
  let errorsHtml = '';
  if (data.common_errors && data.common_errors.length > 0) {
    errorsHtml = `
      <section class="card errors-card" id="common-traps">
        <h2>Common Misconceptions &amp; Exam Traps</h2>
        <ul class="errors-list">
          ${data.common_errors.map(err => `<li>${err}</li>`).join('\n          ')}
        </ul>
      </section>
    `;
  }

  // Render practice questions
  let questionsHtml = '';
  if (data.practice_questions && Array.isArray(data.practice_questions) && data.practice_questions.length > 0) {
    const letters = ['A', 'B', 'C', 'D'];
    const validQuestions = data.practice_questions.filter(q => q && q.question);
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
        <div class="mcq-item" id="q-${i + 1}" data-correct="${correctIdx}">
          <div class="mcq-header">
            <span class="q-num">Q${i + 1}</span>
            <span class="q-text">${q.question}</span>
          </div>
          <ul class="mcq-options">
            ${optionsHtml}
          </ul>
          <div class="mcq-reveal">
            <button type="button" class="btn-reveal" onclick="toggleExplanation(${i})">Show Answer &amp; Explanation</button>
            <div class="mcq-explanation" id="exp-${i}" style="display:none;">
              <strong>Correct Option: ${correctLetter}${correctText ? ' (' + correctText + ')' : ''}</strong>
              <p>${q.explanation || 'Refer to the conceptual notes above.'}</p>
            </div>
          </div>
        </div>
      `;
    }).join('\n');

    questionsHtml = `
      <section class="card mcq-card" id="practice-mcqs">
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

  // Render FAQs
  let faqsHtml = '';
  if (data.faqs && data.faqs.length > 0) {
    faqsHtml = `
      <section class="card faq-card" id="faqs">
        <h2>Frequently Asked Questions</h2>
        <div class="faq-list">
          ${data.faqs.map(f => `
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
<html lang="en">
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

  <!-- Structured Data (JSON-LD) -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "LearningResource",
    "name": "${data.title}",
    "headline": "${data.title} — Study Notes, MCQs & Syllabus Guide",
    "description": "${metaDesc}",
    "url": "${canonicalUrl}",
    "inLanguage": "en",
    "learningResourceType": "Study Guide / Quiz",
    "educationalLevel": "Teacher Eligibility Examination (TGT / PGT)",
    "isPartOf": {
      "@type": "WebSite",
      "name": "SJ Maths",
      "url": "${DOMAIN}/"
    },
    "breadcrumb": {
      "@type": "BreadcrumbList",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Home", "item": "${DOMAIN}/" },
        { "@type": "ListItem", "position": 2, "name": "Physical Education", "item": "${DOMAIN}/physical-education/" },
        { "@type": "ListItem", "position": 3, "name": "${branchTitle}", "item": "${DOMAIN}${branchUrl}" },
        { "@type": "ListItem", "position": 4, "name": "${data.title}", "item": "${canonicalUrl}" }
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

    /* Tables */
    .comparison-card { margin: 24px 0; border: 1px solid var(--line); border-radius: 12px; overflow: hidden; }
    .table-title { background: #f8fbfa; padding: 12px 18px; font-weight: 800; font-size: .9rem; border-bottom: 1px solid var(--line); color: var(--brand-dark); }
    .table-responsive { overflow-x: auto; }
    .styled-table { width: 100%; border-collapse: collapse; text-align: left; font-size: .88rem; }
    .styled-table th { background: #f1f7f5; padding: 10px 14px; font-weight: 750; color: #2c3e39; border-bottom: 1px solid var(--line); }
    .styled-table td { padding: 10px 14px; border-bottom: 1px solid var(--soft-line); color: #374744; }
    .styled-table tr:nth-child(even) { background: #fafdfc; }

    /* Mnemonic Card */
    .mnemonic-card {
      background: #fffbeb; border: 1px solid #fef3c7; border-left: 5px solid #d97706;
      border-radius: 12px; padding: 18px 22px; margin: 24px 0;
    }
    .mnemonic-badge { font-size: .65rem; text-transform: uppercase; font-weight: 850; letter-spacing: .08em; color: #b45309; }
    .mnemonic-title { font-size: 1.05rem; font-weight: 800; color: #78350f; margin: 4px 0 6px; }
    .mnemonic-formula { font-family: monospace; font-size: 1.15rem; font-weight: 700; color: #92400e; background: #fef3c7; padding: 6px 12px; border-radius: 6px; display: inline-block; margin: 6px 0 10px; }
    .mnemonic-desc { font-size: .88rem; color: #92400e; margin: 0; line-height: 1.6; }

    /* High-yield Points & Traps */
    .points-list, .errors-list { margin: 8px 0 0 20px; padding: 0; }
    .points-list li { margin-bottom: 10px; font-size: .94rem; color: #283632; }
    .errors-list li { margin-bottom: 10px; font-size: .94rem; color: #991b1b; }

    /* MCQs */
    .mcq-item { background: #fdfefe; border: 1px solid var(--line); border-radius: 12px; padding: 18px 20px; margin-bottom: 18px; }
    .mcq-header { display: flex; gap: 10px; align-items: baseline; margin-bottom: 12px; }
    .q-num { font-weight: 900; color: var(--brand); font-size: .95rem; }
    .q-text { font-weight: 700; font-size: .96rem; color: var(--ink); line-height: 1.5; }
    .mcq-options { list-style: none; margin: 0 0 14px; padding: 0; display: grid; gap: 8px; }
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
    }
  </style>
  <script>
    function toggleExplanation(idx) {
      const exp = document.getElementById('exp-' + idx);
      if (exp) {
        exp.style.display = exp.style.display === 'none' ? 'block' : 'none';
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
        <span class="brand-sub">Physical Education Study Portal</span>
      </span>
    </a>
    <div class="header-nav">
      <a href="/up-tgt-physical-education/" style="font-size:.82rem;font-weight:700;margin-right:12px;">UP TGT Tracker</a>
      <a href="/up-pgt-physical-education/" style="font-size:.82rem;font-weight:700;">UP PGT Tracker</a>
    </div>
  </div>
</header>

<main class="wrap">
  <nav class="breadcrumb" aria-label="Breadcrumb">
    <a href="/">Home</a>
    <span class="sep">›</span>
    <a href="/physical-education/">Physical Education</a>
    <span class="sep">›</span>
    <a href="${branchUrl}">${branchTitle}</a>
    <span class="sep">›</span>
    <span>${data.title}</span>
  </nav>

  <article class="topic-hero">
    <div class="kicker">${branchTitle} • ${topic.groupTitle}</div>
    <h1>${data.title}</h1>
    <p class="lead">${data.short_intro}</p>
    <div class="topic-chips">
      ${examBadges.join('\n      ')}
    </div>
  </article>

  ${notesHtml}
  ${tablesHtml}
  ${mnemonicsHtml}
  ${pointsHtml}
  ${errorsHtml}
  ${questionsHtml}
  ${faqsHtml}

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
    <p>© SJ Maths • Dedicated preparation portal for teacher examinations and mathematics education.</p>
    <p><a href="/privacy-policy/">Privacy Policy</a> • <a href="/physical-education/">Physical Education Directory</a> • <a href="/">Home</a></p>
  </div>
</footer>

</body>
</html>`;
}

// 6. Hub page generator
function generateHubHtml(title, description, subtopics) {
  const listItems = subtopics.map(sub => `
    <a class="hub-topic-card" href="${sub.href}">
      <div>
        <div class="hub-topic-name">${sub.name}</div>
        <div class="hub-topic-meta">${sub.groupTitle || 'Physical Education'}</div>
      </div>
      <span class="hub-arrow" aria-hidden="true">→</span>
    </a>
  `).join('\n');

  return `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>${title} | Physical Education | SJ Maths</title>
  <meta name="description" content="${description}">
  <meta name="robots" content="index,follow,max-image-preview:large">
  <meta name="author" content="SJ Maths">
  <meta name="theme-color" content="#0F766E">
  <link rel="icon" type="image/png" href="/favicon.png">

  <style>
    :root {
      --bg: #f6faf8; --card: #ffffff; --ink: #16211f; --muted: #566762;
      --line: #dde8e4; --brand: #0f766e; --radius: 16px;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0; font-family: Inter, sans-serif; background: var(--bg); color: var(--ink); line-height: 1.6;
    }
    .wrap { width: min(1080px, calc(100% - 32px)); margin: auto; }
    .site-header {
      height: 66px; background: rgba(255,255,255,.96); border-bottom: 1px solid var(--line);
      display: flex; align-items: center; padding: 0 16px;
    }
    .brand { font-weight: 850; color: inherit; text-decoration: none; }
    .hero {
      background: var(--card); border: 1px solid var(--line); border-radius: var(--radius);
      padding: 32px; margin: 28px 0; box-shadow: 0 12px 34px rgba(21,74,65,.07);
    }
    h1 { margin: 0 0 10px; font-size: 2rem; color: var(--ink); }
    .grid {
      display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 14px; margin-bottom: 48px;
    }
    .hub-topic-card {
      background: var(--card); border: 1px solid var(--line); border-radius: 12px;
      padding: 16px 18px; text-decoration: none; color: inherit; display: flex;
      align-items: center; justify-content: space-between; gap: 12px; transition: border-color .2s;
    }
    .hub-topic-card:hover { border-color: var(--brand); }
    .hub-topic-name { font-size: .9rem; font-weight: 700; color: var(--ink); }
    .hub-topic-meta { font-size: .74rem; color: var(--muted); margin-top: 3px; }
    .hub-arrow { color: var(--brand); font-weight: 700; }
  </style>
</head>
<body>
<header class="site-header">
  <div class="wrap" style="display:flex;justify-content:space-between;align-items:center;">
    <a class="brand" href="/">SJ Maths</a>
    <div>
      <a href="/up-tgt-physical-education/" style="margin-right:12px;color:var(--brand);font-size:.85rem;font-weight:700;text-decoration:none;">UP TGT Tracker</a>
      <a href="/up-pgt-physical-education/" style="color:var(--brand);font-size:.85rem;font-weight:700;text-decoration:none;">UP PGT Tracker</a>
    </div>
  </div>
</header>
<main class="wrap">
  <div class="hero">
    <h1>${title}</h1>
    <p style="margin:0;color:var(--muted);">${description}</p>
  </div>
  <div class="grid">
    ${listItems}
  </div>
</main>
</body>
</html>`;
}

// 7. Fallback template data (if AI key is absent or template mode requested)
function getTemplateData(topic) {
  const parts = topic.href.split('/').filter(Boolean);
  const branchSlug = parts[1] || 'general';
  const branchTitle = getSectionName(branchSlug);

  return {
    title: topic.name,
    short_intro: `${topic.name} is a core study area in ${branchTitle} for UP TGT and UP PGT Physical Education examinations.`,
    notes_sections: [
      {
        heading: "1. Theoretical Concepts & Definition",
        content_html: `<p>In Physical Education and Sports Sciences, <strong>${topic.name}</strong> provides foundational knowledge for understanding curriculum guidelines, physical training principles, and examination problems.</p>`
      },
      {
        heading: "2. Key Principles, Classifications & Protocols",
        content_html: `<p>The study of <strong>${topic.name}</strong> incorporates standardized measurements, physiological responses, diagnostic criteria, and tactical coaching applications.</p>`
      },
      {
        heading: "3. Pedagogical & Examination Significance",
        content_html: `<p>Direct factual, conceptual, and definition-based questions are frequently tested from this area in competitive recruitment tests conducted by UPESSC / UPSESSB.</p>`
      }
    ],
    comparison_tables: [],
    mnemonics: [],
    exam_points: [
      `Master the standard definitions and formulas associated with ${topic.name}.`,
      `Review key terminology and classifications prescribed in the official syllabus.`
    ],
    common_errors: [],
    practice_questions: [],
    faqs: []
  };
}

// 8. Main Generation Loop
async function run() {
  console.log('--- Physical Education Study Notes Generator Pipeline ---');
  console.log(`Loaded ${tgtSyllabus.length} TGT units and ${pgtSyllabus.length} PGT units.`);
  console.log(`Identified ${topics.length} total unique Physical Education topics.`);

  let eligibleTopics = topics;

  if (TARGET_TOPIC) {
    const clean = TARGET_TOPIC.endsWith('/') ? TARGET_TOPIC : TARGET_TOPIC + '/';
    eligibleTopics = eligibleTopics.filter(t => t.href === clean);
    console.log(`Targeting single topic: ${clean} (${eligibleTopics.length} found)`);
  } else if (TARGET_BRANCH) {
    eligibleTopics = eligibleTopics.filter(t => t.href.includes(`/${TARGET_BRANCH}/`));
    console.log(`Targeting branch: ${TARGET_BRANCH} (${eligibleTopics.length} topics)`);
  }

  if (LIMIT) {
    eligibleTopics = eligibleTopics.slice(0, LIMIT);
    console.log(`Applying limit of ${LIMIT} topics.`);
  }

  let generatedCount = 0;
  let skippedCount = 0;
  let errorCount = 0;

  for (let i = 0; i < eligibleTopics.length; i++) {
    const topic = eligibleTopics[i];
    const relativePath = topic.href.replace(/^\//, '').replace(/\/$/, '');
    const targetDir = path.join(ROOT, relativePath);
    const targetFile = path.join(targetDir, 'index.html');

    // Skip if already generated with AI in statusMap (unless --force)
    if (statusMap[topic.href]?.aiCompleted === true && !FORCE && fs.existsSync(targetFile)) {
      skippedCount++;
      continue;
    }

    console.log(`\n[${i + 1}/${eligibleTopics.length}] Generating notes for: ${topic.name}`);
    console.log(`  Path: ${topic.href}`);

    let data;
    let isAiCompleted = false;

    if (TEMPLATE_ONLY) {
      data = getTemplateData(topic);
    } else {
      const prompt = buildPrompt(topic);

      for (let attempt = 0; attempt < 3 && !isAiCompleted; attempt++) {
        const clientObj = getAiClient();
        const currentModel = FALLBACK_MODELS[attempt % FALLBACK_MODELS.length];
        try {
          console.log(`  Calling Gemini (${currentModel}) using Key #${clientObj.id} [Attempt ${attempt + 1}]...`);
          const response = await clientObj.client.models.generateContent({
            model: currentModel,
            contents: prompt,
            config: {
              temperature: 0.3,
              responseMimeType: 'application/json'
            }
          });

          const rawText = response.text ? response.text.trim() : '';
          const repaired = jsonrepair(rawText);
          data = JSON.parse(repaired);
          console.log(`  Received: ${data.notes_sections?.length || 0} sections, ${data.practice_questions?.length || 0} MCQs.`);
          isAiCompleted = true;
        } catch (err) {
          console.warn(`  Attempt ${attempt + 1} warning: ${err.message}`);
          if (attempt < 2) {
            await new Promise(r => setTimeout(r, 2500));
          }
        }
      }

      if (!isAiCompleted) {
        console.error(`  AI Generation Failed after 3 attempts. Falling back to structured template.`);
        data = getTemplateData(topic);
        errorCount++;
      }
    }

    let fullHtml;
    try {
      fullHtml = renderFullStudyPage(topic, data);
    } catch (renderErr) {
      console.warn(`  Render warning: ${renderErr.message}. Falling back to clean template.`);
      data = getTemplateData(topic);
      fullHtml = renderFullStudyPage(topic, data);
      isAiCompleted = false;
    }

    if (!DRY_RUN) {
      fs.mkdirSync(targetDir, { recursive: true });
      fs.writeFileSync(targetFile, fullHtml, 'utf8');

      statusMap[topic.href] = {
        status: 'completed',
        aiCompleted: isAiCompleted,
        title: data.title || topic.name,
        sectionsCount: data.notes_sections?.length || 0,
        questionsCount: data.practice_questions?.length || 0,
        generatedAt: new Date().toISOString()
      };
      saveStatus();
    }

    generatedCount++;
    console.log(`  ✓ Written to: ${relativePath}/index.html`);

    // Pacing delay between requests to prevent API rate limit bursts
    if (!TEMPLATE_ONLY && i < eligibleTopics.length - 1) {
      await new Promise(r => setTimeout(r, 1200));
    }
  }

  // 9. Generate intermediate hubs
  console.log('\nGenerating branch hubs...');
  const branches = new Map();
  for (const t of topics) {
    const parts = t.href.split('/').filter(Boolean);
    const branchSlug = parts[1];
    if (!branchSlug) continue;
    if (!branches.has(branchSlug)) branches.set(branchSlug, []);
    branches.get(branchSlug).push(t);
  }

  for (const [branchSlug, subtopics] of branches.entries()) {
    const branchDir = path.join(ROOT, 'physical-education', branchSlug);
    const branchFile = path.join(branchDir, 'index.html');
    const branchTitle = getSectionName(branchSlug);
    const branchDesc = `Explore all ${subtopics.length} study topics under ${branchTitle} for UP TGT and UP PGT Physical Education.`;

    if (!DRY_RUN && (!fs.existsSync(branchFile) || FORCE)) {
      fs.mkdirSync(branchDir, { recursive: true });
      fs.writeFileSync(branchFile, generateHubHtml(branchTitle, branchDesc, subtopics), 'utf8');
    }
  }

  // Master root hub
  const rootDir = path.join(ROOT, 'physical-education');
  const rootFile = path.join(rootDir, 'index.html');
  const branchList = Array.from(branches.keys()).map(slug => ({
    name: getSectionName(slug),
    href: `/physical-education/${slug}/`,
    groupTitle: `${branches.get(slug).length} Study Topics`
  }));

  if (!DRY_RUN && (!fs.existsSync(rootFile) || FORCE)) {
    fs.mkdirSync(rootDir, { recursive: true });
    fs.writeFileSync(
      rootFile,
      generateHubHtml(
        'Physical Education Master Study Library',
        'Complete curriculum library for UP TGT & UP PGT Physical Education examinations with all 308 topics across 14 major disciplines.',
        branchList
      ),
      'utf8'
    );
  }

  console.log(`\n========================================`);
  console.log(`Pipeline Finished!`);
  console.log(`Generated: ${generatedCount} topics`);
  console.log(`Skipped:   ${skippedCount} topics`);
  console.log(`Errors:    ${errorCount}`);
  console.log(`Total:     ${eligibleTopics.length} topics`);
  console.log(`Status saved to: ${STATUS_FILE}`);
  console.log(`========================================`);
}

run().catch(err => {
  console.error('Fatal execution error:', err);
  process.exit(1);
});
