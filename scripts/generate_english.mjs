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

function compileTopicHtml(call1, call2, context) {
  const canonicalUrl = `https://sjmaths.com${context.topicUrl}`;
  const metaDesc = `${call1.title}. Detailed study notes, literary analysis, grammar rules, mnemonics, PYQs, and topic test for UP TGT & PGT English.`;

  // Study Notes HTML
  let pillarsHtml = '';
  (call1.conceptual_pillars || []).forEach((p, idx) => {
    const takeaways = (p.key_takeaways || []).map(t => `<li>${t}</li>`).join('');
    const detailedPoints = (p.detailed_analysis_points || []).map(pt => `<li>${pt}</li>`).join('');
    pillarsHtml += `
      <section class="notes-section" id="pillar-${idx + 1}">
        <h2>${idx + 1}. ${p.pillar_title}</h2>
        <div class="prose-content">
          <p class="lead-concept" style="font-weight:600;color:var(--brand);margin-bottom:0.75rem;">${p.lead_concept}</p>
          ${detailedPoints ? `<ul class="notes-bullet-list" style="margin-bottom:1rem;">${detailedPoints}</ul>` : ''}
          ${p.comparative_insights ? `<div class="info-callout" style="background:var(--accent-soft);border-left:4px solid var(--accent);padding:1rem;margin:1rem 0;border-radius:6px;"><strong>Comparative Analysis:</strong> ${p.comparative_insights}</div>` : ''}
          ${takeaways ? `<ul class="notes-bullet-list" style="margin-top:0.75rem;">${takeaways}</ul>` : ''}
        </div>
      </section>
    `;
  });

  // Formulas / Scales
  let formulasHtml = '';
  if (call1.formulas_and_scales && call1.formulas_and_scales.length > 0) {
    const cards = call1.formulas_and_scales.map(f => `
      <div class="formula-card">
        <div class="formula-name">${f.name}</div>
        <div class="formula-eq">${f.equation}</div>
        <div class="formula-meta">
          <div><strong>Parameters:</strong> ${f.parameters}</div>
          <div><strong>Exam Focus:</strong> ${f.exam_significance}</div>
        </div>
      </div>
    `).join('');

    formulasHtml = `
      <div class="formula-sheet-box">
        <div class="formula-sheet-title">📐 Key Literary Devices & Grammar Rules</div>
        <div class="formula-grid">${cards}</div>
      </div>
    `;
  }

  // Spatial & Regional Distribution
  let spatialHtml = '';
  if (call1.spatial_and_regional_distribution) {
    spatialHtml = `
      <section class="notes-section" id="spatial-distribution">
        <h2>Literary Periods & Regional Context</h2>
        <div class="prose-content">
          <div style="margin-bottom:1rem;">
            <h3 style="font-size:1.1rem;color:var(--brand);margin-bottom:0.4rem;">🌐 Global/Historical Context</h3>
            <p>${call1.spatial_and_regional_distribution.global_patterns || ''}</p>
          </div>
          <div>
            <h3 style="font-size:1.1rem;color:var(--brand);margin-bottom:0.4rem;">🇮🇳 Indian Literature in English</h3>
            <p>${call1.spatial_and_regional_distribution.indian_context || ''}</p>
          </div>
        </div>
      </section>
    `;
  }

  // Tricks & Mnemonics
  let tricksHtml = '';
  if (call1.tricks_and_mnemonics && call1.tricks_and_mnemonics.length > 0) {
    const cards = call1.tricks_and_mnemonics.map(t => `
      <div class="trick-card" style="background:var(--paper-card);border:1px solid var(--accent-border);border-radius:var(--radius);padding:1.25rem;margin-bottom:1rem;">
        <div style="font-weight:700;color:var(--accent);font-size:1.05rem;margin-bottom:0.35rem;">💡 ${t.title}</div>
        <div style="font-size:1.1rem;font-weight:800;letter-spacing:0.5px;color:var(--brand);margin-bottom:0.5rem;background:var(--accent-soft);padding:0.5rem 0.75rem;border-radius:6px;display:inline-block;">${t.mnemonic}</div>
        <p style="margin-bottom:0.5rem;font-size:0.95rem;">${t.explanation}</p>
        <div style="font-size:0.85rem;color:var(--muted);"><strong>⚠️ Exam Trap:</strong> ${t.exam_pitfall_warning}</div>
      </div>
    `).join('');

    tricksHtml = `
      <section class="notes-section" id="mnemonics-section">
        <h2>Mnemonics, Memory Shortcuts & Exam Traps</h2>
        <div>${cards}</div>
      </section>
    `;
  }

  // Quick Revision Summary
  let glossaryHtml = '';
  const glossary = (call2.quick_revision && call2.quick_revision.glossary_terms) || [];
  if (glossary.length > 0) {
    const items = glossary.map(g => `
      <div style="border-bottom:1px solid var(--softline);padding:0.85rem 0;">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.25rem;">
          <strong style="color:var(--brand);font-size:1.05rem;">${g.term}</strong>
          <span style="font-size:0.75rem;background:var(--accent-soft);color:var(--accent);padding:2px 8px;border-radius:12px;font-weight:600;">${g.exam_tag || 'Concept'}</span>
        </div>
        <p style="margin:0;font-size:0.92rem;color:var(--ink2);">${g.definition}</p>
      </div>
    `).join('');

    glossaryHtml = `
      <div class="card" style="margin-bottom:1.5rem;">
        <h3 style="margin-bottom:1rem;color:var(--brand);font-size:1.2rem;">📚 High-Yield Literary & Grammatical Terminology</h3>
        <div>${items}</div>
      </div>
    `;
  }

  let theoriesHtml = '';
  const theories = (call2.quick_revision && call2.quick_revision.high_yield_laws_and_theories) || [];
  if (theories.length > 0) {
    const items = theories.map(th => `
      <div style="border-left:3px solid var(--brand);padding-left:1rem;margin-bottom:1rem;">
        <div style="font-weight:700;color:var(--brand);">${th.theorist_or_law} <span style="font-size:0.8rem;color:var(--muted);font-weight:400;">(${th.year_or_period})</span></div>
        <p style="margin:0.25rem 0 0;font-size:0.92rem;">${th.core_postulate}</p>
      </div>
    `).join('');

    theoriesHtml = `
      <div class="card">
        <h3 style="margin-bottom:1rem;color:var(--brand);font-size:1.2rem;">🧭 Prescribed Authors, Critics & Rules</h3>
        <div>${items}</div>
      </div>
    `;
  }

  // Practice Quiz MCQs
  let quizCardsHtml = '';
  const letters = ['A', 'B', 'C', 'D'];
  (call2.practice_quiz || []).forEach((q, idx) => {
    const opts = (q.options || []).map((opt, oIdx) => `
      <button type="button" class="quiz-option-btn" data-qindex="${idx}" data-optindex="${oIdx}">
        <span class="option-letter">${letters[oIdx]}</span>
        <span class="option-text">${opt}</span>
      </button>
    `).join('');

    quizCardsHtml += `
      <div class="quiz-question-card" id="q-card-${idx}" data-correct="${q.correct_index ?? 0}">
        <div class="quiz-q-header"><span class="q-badge">Question ${idx + 1} of ${(call2.practice_quiz || []).length}</span></div>
        <div class="question-text">${q.question}</div>
        <div class="quiz-options-grid">${opts}</div>
        <div class="quiz-feedback hidden" id="feedback-${idx}">
          <div class="feedback-indicator"></div>
          <p class="feedback-explanation"><strong>Rationale:</strong> ${q.explanation}</p>
        </div>
      </div>
    `;
  });

  // PYQs
  let pyqCardsHtml = '';
  (call2.pyqs || []).forEach((q, idx) => {
    const opts = (q.options || []).map((opt, oIdx) => `
      <button type="button" class="quiz-option-btn" data-pyqindex="${idx}" data-optindex="${oIdx}">
        <span class="option-letter">${letters[oIdx]}</span>
        <span class="option-text">${opt}</span>
      </button>
    `).join('');

    pyqCardsHtml += `
      <div class="pyq-card" id="pyq-card-${idx}" data-correct="${q.correct_index ?? 0}">
        <div class="pyq-header">
          <span class="exam-tag">${q.exam_year || 'UP PGT/TGT English'}</span>
        </div>
        <div class="question-text">${q.question}</div>
        <div class="quiz-options-grid">${opts}</div>
        <div class="pyq-solution hidden" id="pyq-expl-${idx}">
          <p><strong>Official Benchmark Explanation:</strong> ${q.explanation}</p>
        </div>
      </div>
    `;
  });

  // Timed Topic Test (10 Items)
  let topicTestCardsHtml = '';
  (call2.topic_test || []).forEach((q, idx) => {
    const opts = (q.options || []).map((opt, oIdx) => `
      <button type="button" class="test-option-btn" data-tindex="${idx}" data-optindex="${oIdx}">
        <span class="option-letter">${letters[oIdx]}</span>
        <span class="option-text">${opt}</span>
      </button>
    `).join('');

    topicTestCardsHtml += `
      <div class="test-question-card" id="t-card-${idx}" data-correct="${q.correct_index ?? 0}">
        <div class="test-q-header"><span class="t-badge">Question ${idx + 1} of 10</span></div>
        <div class="test-question-text">${q.question}</div>
        <div class="test-options-grid">${opts}</div>
        <div class="t-feedback hidden" id="t-feedback-${idx}">
          <p class="feedback-explanation"><strong>Solution:</strong> ${q.explanation}</p>
        </div>
      </div>
    `;
  });

  return `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>${call1.title} | UP TGT &amp; PGT English</title>
<meta name="description" content="${metaDesc}">
<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1">
<meta name="author" content="SJ Maths">
<meta name="theme-color" content="#064e3b">
<link rel="canonical" href="${canonicalUrl}">
<link rel="icon" type="image/png" href="/favicon.png">

<!-- Unified Topic Page Stylesheet (Chemistry Standard) -->
<link rel="stylesheet" href="/assets/css/topic-page.min.css?v=718ef3ff">

<!-- Theme Override -->
<style>
:root {
  --brand: #064e3b;
  --brand-dark: #022c22;
  --brand-light: #059669;
  --brand-gradient: linear-gradient(135deg, #064e3b 0%, #059669 100%);
  --accent: #059669;
  --accent-hover: #047857;
  --accent-soft: rgba(5, 150, 105, 0.08);
  --accent-border: rgba(5, 150, 105, 0.24);
}
html.dark, body.dark-mode {
  --brand: #6ee7b7;
  --brand-dark: #a7f3d0;
  --brand-light: #34d399;
  --brand-gradient: linear-gradient(135deg, #064e3b 0%, #022c22 100%);
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
      <span class="brand-mark" style="background: linear-gradient(145deg, #064e3b, #059669); font-family: serif; font-size: 1.35rem; font-style: italic; display: flex; align-items: center; justify-content: center;">&int;</span>
      <span>
        <span class="brand-name">SJ Maths</span>
        <span class="brand-sub">English</span>
      </span>
    </a>
    <div class="header-actions">
      <button type="button" class="theme-toggle-btn" id="btn-theme-toggle" aria-label="Toggle Dark Mode">🌙 Dark Mode</button>
      <a class="back-btn" href="/up-pgt-english/" title="UP PGT English Tracker">← UP PGT<span class="desk-only"> English</span></a>
    </div>
  </div>
</header>

<main class="wrap">
  <!-- Hero Section -->
  <section class="hero">
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="https://sjmaths.com/">Home</a>
      <span class="breadcrumb-sep">›</span>
      <a href="/up-pgt-english/">English</a>
      <span class="breadcrumb-sep">›</span>
      <span>${context.sectionTitle}</span>
      <span class="breadcrumb-sep">›</span>
      <span aria-current="page">${context.topicName}</span>
    </nav>
    <div class="kicker" style="color: #059669; font-weight: 800;">${context.sectionTitle}</div>
    <h1>${call1.title}</h1>
    <p class="lead">${call1.short_intro}</p>

    <div class="exam-badges">
      <a class="exam-chip pgt" href="/up-pgt-english/">UP PGT English</a>
      <a class="exam-chip both" href="/up-tgt-english/">UP TGT English</a>
      <span class="exam-chip both">B.A. / M.A. Level</span>
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
        <span>❓</span> <span>Practice Quiz</span> <span class="tab-badge">${(call2.practice_quiz || []).length}Q</span>
      </button>
      <button type="button" class="tab-btn" role="tab" aria-selected="false" data-tab="tab-pyqs" id="tab-btn-pyqs">
        <span>🏛️</span> <span>PYQs &amp; Trends</span>
      </button>
      <button type="button" class="tab-btn" role="tab" aria-selected="false" data-tab="tab-test" id="tab-btn-test">
        <span>⏱️</span> <span>Topic Test</span> <span class="tab-badge">10Q</span>
      </button>
    </div>
  </div>

  <!-- Tab Panels & Main Grid Layout -->
  <div class="main-grid">
    <div class="content-col">

      <!-- TAB 1: STUDY NOTES -->
      <article class="tab-panel active" id="tab-notes" role="tabpanel" aria-labelledby="tab-btn-notes">
        ${call1.academic_synopsis ? `<div class="card" style="margin-bottom:1.5rem;"><p style="font-size:1.05rem;line-height:1.75;margin:0;">${call1.academic_synopsis}</p></div>` : ''}
        ${pillarsHtml}
        ${spatialHtml}
        ${formulasHtml}
        ${tricksHtml}
      </article>

      <!-- TAB 2: REVISION SUMMARY -->
      <article class="tab-panel hidden" id="tab-summary" role="tabpanel" aria-labelledby="tab-btn-summary">
        ${glossaryHtml}
        ${theoriesHtml}
      </article>

      <!-- TAB 3: PRACTICE QUIZ -->
      <article class="tab-panel hidden" id="tab-quiz" role="tabpanel" aria-labelledby="tab-btn-quiz">
        <div class="quiz-summary-card">
          <h3>Interactive Concept Practice</h3>
          <p>Instant evaluation with detailed explanations for each question.</p>
        </div>
        <div id="quiz-container">
          ${quizCardsHtml}
        </div>
      </article>

      <!-- TAB 4: PYQS & TRENDS -->
      <article class="tab-panel hidden" id="tab-pyqs" role="tabpanel" aria-labelledby="tab-btn-pyqs">
        <div class="pyq-header-card">
          <h3>Previous Years Questions &amp; Exam Benchmarks</h3>
          <p>Real and benchmark questions aligned with UP PGT, TGT, and National Eligibility tests.</p>
        </div>
        <div id="pyq-container">
          ${pyqCardsHtml}
        </div>
      </article>

      <!-- TAB 5: TIMED TOPIC TEST -->
      <article class="tab-panel hidden" id="tab-test" role="tabpanel" aria-labelledby="tab-btn-test">
        <div class="test-header-bar">
          <div>
            <h3>Timed Exam Simulator</h3>
            <p>10 Questions • 10 Minutes • Real-time scoring</p>
          </div>
          <div class="timer-display" id="testTimerDisplay">10:00</div>
        </div>

        <div class="test-questions-wrapper">
          ${topicTestCardsHtml}
        </div>

        <div class="test-submit-bar">
          <button type="button" class="btn-submit-test" id="btnSubmitTest" style="background: #059669;">Submit Test</button>
        </div>

        <div class="test-result-modal hidden" id="testResultModal">
          <div class="result-card">
            <h3>Test Result</h3>
            <div class="result-score-circle" style="background: linear-gradient(135deg, #064e3b, #059669);">
              <span id="resFinalScore">0</span> / 10
            </div>
            <p id="resFeedbackText">Review detailed solutions above for all questions.</p>
            <button type="button" class="btn-retake-test" id="btnRetakeTest" style="background: #059669;">Retake Test</button>
          </div>
        </div>
      </article>

      <!-- Bottom Pagination -->
      <nav class="topic-pagination" aria-label="Topic Navigation" style="margin-top:2rem;">
        <a class="topic-nav-btn next" href="/up-pgt-english/"><span>Exam Tracker →</span> <strong>UP PGT English</strong></a>
      </nav>

    </div>

    <!-- Sticky Sidebar -->
    <aside class="sidebar-col">
      <div class="sidebar-card side-card">
        <div class="side-card-header">
          <span class="side-badge">Syllabus Section</span>
          <h3>${context.sectionTitle}</h3>
        </div>
        <p class="side-desc">Official UP PGT English curriculum module.</p>
        <div class="side-action-box" style="margin-top:1.5rem;">
          <a class="side-action-btn" href="/up-pgt-english/" style="background: #064e3b; display:block; text-align:center; padding:10px; color:#fff; border-radius:8px; font-weight:600;">Full English Tracker →</a>
        </div>
      </div>
    </aside>
  </div>
</main>

<footer class="site-footer">
  <div class="wrap footer-inner">
    <div>
      <p><strong>SJ Maths — English</strong></p>
      <p>Master curriculum resources for UP PGT English &amp; UP TGT English.</p>
    </div>
    <div class="footer-links">
      <a href="https://sjmaths.com/">Home</a>
      <a href="/up-pgt-english/">UP PGT English</a>
      <a href="/up-tgt-english/">UP TGT English</a>
    </div>
  </div>
</footer>

<!-- Standard Chemistry/Topic-Page Interactive Controller -->
<script>
document.addEventListener('DOMContentLoaded', () => {
  // Theme Toggle
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

      if (optIndex === correctIndex) {
        quizScore++;
        if (statusEl) {
          statusEl.textContent = '✓ Correct Answer!';
          statusEl.style.color = '#15803d';
        }
      } else {
        if (statusEl) {
          statusEl.textContent = '✗ Incorrect!';
          statusEl.style.color = '#b91c1c';
        }
      }
      if (feedback) feedback.classList.remove('hidden');
    });
  });

  // Timed Topic Test Logic
  let testTimer = null;
  let timeRemaining = 600;
  const timerDisplay = document.getElementById('testTimerDisplay');

  const testTabBtn = document.getElementById('tab-btn-test');
  if (testTabBtn) {
    testTabBtn.addEventListener('click', () => {
      if (testTimer) return;
      testTimer = setInterval(() => {
        timeRemaining--;
        const m = Math.floor(timeRemaining / 60);
        const s = timeRemaining % 60;
        if (timerDisplay) {
          timerDisplay.textContent = String(m).padStart(2, '0') + ':' + String(s).padStart(2, '0');
        }
        if (timeRemaining <= 0) {
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
