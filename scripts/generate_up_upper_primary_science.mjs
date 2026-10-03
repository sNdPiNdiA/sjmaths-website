#!/usr/bin/env node
/**
 * ============================================================================
 * SJ Maths — UP Upper Primary Assistant Teacher (Class 6-8) Science Generator
 * Pointwise Concept Notes, Memory Mnemonics, Tips, Tricks & 10 Interactive MCQs
 * Powered by Google Gemini API via @google/genai SDK
 *
 * Examination: UP Upper Primary Assistant Teacher Recruitment 2026 (Super TET Junior)
 * Subject: Science (Part 2C: Science & Mathematics Teacher | -1 Negative Marking)
 * Covers all 34 Modular Micro-Topics across 4 Sections:
 *   1. Biology & Life Sciences (Topics 1 to 14)
 *   2. Human Body, Health & Nutrition (Topics 15 to 20)
 *   3. Physics, Energy & Measurements (Topics 21 to 26)
 *   4. Chemistry & Materials (Topics 27 to 34)
 *
 * Uses common CSS: /assets/css/up-upper-primary-topic.min.css
 * Uses common JS:  /assets/js/up-upper-primary-topic.min.js
 * No footer included (as requested).
 * ============================================================================
 */

import fs from 'node:fs';
import path from 'node:path';
import 'dotenv/config';
import { GoogleGenAI } from '@google/genai';
import { jsonrepair } from 'jsonrepair';

const ROOT = process.cwd();
const DOMAIN = 'https://sjmaths.com';
const TRACKER_PATH = path.join(ROOT, 'up-upper-primary-teacher', 'science', 'index.html');
const STATUS_FILE = path.join(ROOT, 'content-generation-status-upper-primary-science.json');
const OUTPUT_DIR = path.join(ROOT, 'up-upper-primary-teacher', 'science');

// 1. API Key & Multi-Model Rotation Configuration
const KEY_CONFIGS = [
  { key: process.env.GEMINI_API_KEY_1, name: 'KEY_1', models: ['gemini-2.5-flash', 'gemini-3.5-flash-lite'] },
  { key: process.env.GEMINI_API_KEY_2, name: 'KEY_2', models: ['gemini-3.5-flash-lite', 'gemini-3.5-flash'] },
  { key: process.env.GEMINI_API_KEY,   name: 'KEY_3', models: ['gemini-3.5-flash-lite', 'gemini-3.5-flash'] }
].filter(c => Boolean(c.key));

if (KEY_CONFIGS.length === 0) {
  console.error('ERROR: No valid GEMINI_API_KEY found in environment. Please configure .env file.');
  process.exit(1);
}

let keyIndex = 0;
function getActiveConfig() {
  return KEY_CONFIGS[keyIndex % KEY_CONFIGS.length];
}

function rotateKey() {
  keyIndex++;
  const next = getActiveConfig();
  console.log(`  [Key Rotation] Rotating to next API key (${next.name})...`);
}

// 2. Parse CLI arguments
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

// 3. Status Tracking
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

// 4. Extract Syllabus from Science Tracker Hub
function decodeHtml(str) {
  return String(str || '')
    .replace(/&amp;/g, '&')
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'");
}

function extractSyllabus() {
  if (!fs.existsSync(TRACKER_PATH)) {
    console.error(`Tracker file not found: ${TRACKER_PATH}`);
    return [];
  }
  const html = fs.readFileSync(TRACKER_PATH, 'utf8');

  const regex = /<details class="module-accordion" data-sec-idx="([^"]+)"[\s\S]*?<h3 class="module-title">[\s\S]*?<span class="lang-hi">([^<]+)<\/span>[\s\S]*?<span class="lang-en">([^<]+)<\/span>[\s\S]*?<ul class="module-list">([\s\S]*?)<\/ul>/g;

  let sMatch;
  const topicList = [];

  while ((sMatch = regex.exec(html)) !== null) {
    const [_, secIdx, secTitleHi, secTitleEn, secBody] = sMatch;
    const topicRegex = /<li class="topic-row">[\s\S]*?<input[^>]*id="([^"]+)"[\s\S]*?<a href="([^"]+)"[\s\S]*?<span class="topic-num">([^<]+)<\/span>[\s\S]*?<span class="lang-hi">([^<]+)<\/span>[\s\S]*?<span class="lang-en">([^<]+)<\/span>[\s\S]*?<span class="topic-tag">([^<]+)<\/span>/g;
    let tMatch;
    while ((tMatch = topicRegex.exec(secBody)) !== null) {
      const href = tMatch[2].startsWith('/') ? tMatch[2] : '/' + tMatch[2];
      const cleanHref = href.endsWith('/') ? href : href + '/';
      const slug = cleanHref.replace('/up-upper-primary-teacher/science/', '').replace(/\//g, '');
      const numRaw = tMatch[3].trim().replace('#', '');
      const num = parseInt(numRaw, 10);

      topicList.push({
        chkId: tMatch[1],
        href: cleanHref,
        slug,
        num,
        numStr: `#${num}`,
        nameHi: decodeHtml(tMatch[4].trim()),
        nameEn: decodeHtml(tMatch[5].trim().replace(/^\(|\)$/g, '')),
        tag: tMatch[6].trim(),
        secIdx: parseInt(secIdx, 10),
        secTitleHi: decodeHtml(secTitleHi.trim()),
        secTitleEn: decodeHtml(secTitleEn.trim()),
      });
    }
  }

  return topicList;
}

const allTopics = extractSyllabus();

// 5. Pointwise & High-Yield Science Prompt Builder
function buildPrompt(topic) {
  return `You are a Senior Professor of Science, Chief Science Curriculum Advisor for SCERT Uttar Pradesh & NCERT, and Senior Head Question Paper Setter for the Uttar Pradesh Upper Primary Assistant Teacher Recruitment Examination (Super TET Junior — Part 2C Science & Mathematics: 90 Questions | 270 Marks | -1 Negative Marking Penalty).

Create exhaustive, strictly POINTWISE classroom study notes, comparative analysis tables, memory mnemonics, shortcut tricks, exam traps, and 10 high-quality exam practice MCQs in ENGLISH for this exact syllabus topic:
- Examination: UP Upper Primary Assistant Teacher Recruitment (Class 6-8) 2026
- Subject: Science (Part 2C Science & Math: 90 Questions | 270 Marks | -1 Negative Marking)
- Section ${topic.secIdx}: ${topic.secTitleEn}
- Topic #${topic.num}: ${topic.nameEn}
- Official Hindi Reference: ${topic.nameHi}
- Canonical URL: ${DOMAIN}${topic.href}

CRITICAL PEDAGOGICAL & STRUCTURAL RULES (STRICT COMPLIANCE REQUIRED):
1. STRICTLY POINTWISE ARCHITECTURE:
   - ZERO continuous narrative prose or long paragraphs.
   - Every single concept MUST be broken into structured point-cards wrapped in <div class="point-grid"><div class="point-card"><strong>[Scientific Law / Formula / Organelle / Mechanism / Reaction / Application]:</strong> Exhaustive, deep factual detail...</div>...</div>.
   - Each point-card MUST begin with a bold scientific term, SI unit, chemical formula, biological process, or physical law.
   - Do NOT omit ANY scientific facts, formulas, equations, exceptions, or applications. Grounded in SCERT UP Class 6-8 Science textbooks ("Hamara Vigyan", "Paryavaran Adhyayan") and NCERT standards.

2. EMBEDDED COGNITIVE ANCHORS:
   - In Concept 1: Embed at least ONE <div class="tip-box"><i class="fas fa-lightbulb"></i> <strong>Exam Pro-Tip:</strong> ...</div> AND at least ONE <div class="mnemonic-inline-box"><i class="fas fa-brain"></i> <strong>Memory Mnemonic:</strong> <code>ACRONYM</code> — ...</div>.
   - In Concept 2: Embed a structured comparison sub-table <div class="topic-subtable-wrapper"><table class="topic-subtable"><thead><tr><th>Entity / Category</th><th>Core Scientific Properties & Formulas</th><th>High-Yield Exam Takeaway</th></tr></thead><tbody><tr><td><strong>Item 1</strong></td><td>...</td><td>...</td></tr><tr><td><strong>Item 2</strong></td><td>...</td><td>...</td></tr></tbody></table></div> AND at least ONE <div class="trick-box"><i class="fas fa-bolt"></i> <strong>Shortcut Trick / Calculation Rule:</strong> ...</div>.
   - In Concept 3: Provide detailed, exhaustive point-cards focusing on practical experiments, real-world applications, laboratory precautions, and regional UP biological/agricultural/environmental contexts AND at least ONE <div class="tip-box"><i class="fas fa-lightbulb"></i> <strong>UP Exam High-Yield Tip:</strong> ...</div>.
   - In Concept 4: Embed scientific exceptions, common calculation errors, unit conversion traps, and trap prevention tips: <div class="trick-box"><i class="fas fa-bolt"></i> <strong>Trap Prevention Trick:</strong> ...</div> AND <div class="mnemonic-inline-box"><i class="fas fa-brain"></i> <strong>Memory Mnemonic:</strong> <code>KEY</code> — ...</div>.

3. 10 HIGH-QUALITY EXAM MCQs:
   - Exactly 10 MCQs matching the competitive standard of Super TET Junior Part 2C (conceptual depth + numerical problem solving where applicable).
   - 4 plausible options without A/B/C/D letter prefixes.
   - 0-based correct_index (0, 1, 2, 3).
   - In-depth analytical explanation detailing why the correct option is right and explaining why distractors are incorrect.

4. QUICK REVISION & TRAPS VAULT:
   - 8 rapid recall scientific facts/formulas.
   - 2 memory mnemonics with title, acronym, and expansion.
   - 4 negative-marking alerts (-1 penalty avoidance).
   - 4 self-assessment checklist items.

5. CLEAN EDITORIAL VOICE:
   - Strictly NO meta-prompt references, NO phrases like "zero narrative paragraphs", NO "(Pointwise Breakdown)" in titles. Natural, authoritative textbook tone.

JSON SCHEMA TO RETURN (EXACTLY AS DEFINED, RAW JSON ONLY):
{
  "key_focus_summary": "Crisp 2-3 sentence overview of this scientific topic, key examination weightage, and high-yield focus areas for Super TET Junior.",
  "concepts": [
    {
      "heading": "1. Core Principles, Definitions & Fundamental Laws",
      "html_content": "<div class=\"point-grid\"><div class=\"point-card\"><strong>Key Principle 1:</strong> ...</div><div class=\"point-card\"><strong>Key Principle 2:</strong> ...</div><div class=\"point-card\"><strong>Key Principle 3:</strong> ...</div><div class=\"point-card\"><strong>Key Principle 4:</strong> ...</div></div><div class=\"tip-box\"><i class=\"fas fa-lightbulb\"></i> <strong>Exam Pro-Tip:</strong> ...</div><div class=\"mnemonic-inline-box\"><i class=\"fas fa-brain\"></i> <strong>Memory Mnemonic:</strong> <code>KEY</code> — ...</div>"
    },
    {
      "heading": "2. Classifications, Chemical / Physical Mechanisms & Systems",
      "html_content": "<div class=\"topic-subtable-wrapper\"><table class=\"topic-subtable\"><thead><tr><th>Entity / Category</th><th>Core Scientific Properties & Formulas</th><th>High-Yield Exam Takeaway</th></tr></thead><tbody><tr><td><strong>Category 1</strong></td><td>Details...</td><td>Takeaway...</td></tr><tr><td><strong>Category 2</strong></td><td>Details...</td><td>Takeaway...</td></tr></tbody></table></div><div class=\"point-grid\"><div class=\"point-card\"><strong>Mechanism / Process 1:</strong> ...</div><div class=\"point-card\"><strong>Mechanism / Process 2:</strong> ...</div><div class=\"point-card\"><strong>Mechanism / Process 3:</strong> ...</div></div><div class=\"trick-box\"><i class=\"fas fa-bolt\"></i> <strong>Shortcut Trick / Calculation Rule:</strong> ...</div>"
    },
    {
      "heading": "3. Laboratory Methods, Practical Applications & Daily Life",
      "html_content": "<div class=\"point-grid\"><div class=\"point-card\"><strong>Experiment / Application 1:</strong> ...</div><div class=\"point-card\"><strong>Experiment / Application 2:</strong> ...</div><div class=\"point-card\"><strong>Experiment / Application 3:</strong> ...</div><div class=\"point-card\"><strong>Experiment / Application 4:</strong> ...</div></div><div class=\"tip-box\"><i class=\"fas fa-lightbulb\"></i> <strong>UP Exam High-Yield Tip:</strong> ...</div>"
    },
    {
      "heading": "4. Scientific Exceptions, Calculations & Common Pitfalls",
      "html_content": "<div class=\"point-grid\"><div class=\"point-card\"><strong>Critical Distinction / Anomaly:</strong> ...</div><div class=\"point-card\"><strong>Edge Case / Exception:</strong> ...</div><div class=\"point-card\"><strong>Formula Trap / Unit Error:</strong> ...</div></div><div class=\"trick-box\"><i class=\"fas fa-bolt\"></i> <strong>Trap Prevention Trick:</strong> ...</div><div class=\"mnemonic-inline-box\"><i class=\"fas fa-brain\"></i> <strong>Memory Mnemonic:</strong> <code>KEY</code> — ...</div>"
    }
  ],
  "comparative_table": {
    "title": "Comprehensive Scientific Matrix & High-Yield Analysis",
    "headers": ["Parameter / Dimension", "Category / System A", "Category / System B", "Super TET Exam Significance"],
    "rows": [
      ["Parameter 1", "Detailed data A", "Detailed data B", "High-yield exam takeaway"],
      ["Parameter 2", "Detailed data A", "Detailed data B", "High-yield exam takeaway"],
      ["Parameter 3", "Detailed data A", "Detailed data B", "High-yield exam takeaway"],
      ["Parameter 4", "Detailed data A", "Detailed data B", "High-yield exam takeaway"]
    ]
  },
  "mcqs": [
    {
      "question": "Challenging scientific question testing conceptual clarity, application or calculation?",
      "options": [
        "First plausible option without any A/B/C/D letter prefix",
        "Second plausible option without any A/B/C/D letter prefix",
        "Third plausible option without any A/B/C/D letter prefix",
        "Fourth plausible option without any A/B/C/D letter prefix"
      ],
      "correct_index": 0,
      "explanation": "Detailed pedagogical explanation stating why option A is correct and explaining the scientific basis why options B, C, and D are incorrect."
    }
  ],
  "revision_facts": [
    "High-yield factual scientific takeaway 1 with specific formula/unit/process.",
    "High-yield factual scientific takeaway 2 with specific formula/unit/process.",
    "High-yield factual scientific takeaway 3 with specific formula/unit/process.",
    "High-yield factual scientific takeaway 4 with specific formula/unit/process.",
    "High-yield factual scientific takeaway 5 with specific formula/unit/process.",
    "High-yield factual scientific takeaway 6 with specific formula/unit/process.",
    "High-yield factual scientific takeaway 7 with specific formula/unit/process.",
    "High-yield factual scientific takeaway 8 with specific formula/unit/process."
  ],
  "mnemonics": [
    {
      "title": "Scientific Rule / Sequence Acronym",
      "acronym": "CODE",
      "expansion": "C - Component, O - Order, D - Data, E - Effect."
    },
    {
      "title": "Key Property Anchor",
      "acronym": "FAST",
      "expansion": "F - Formula, A - Application, S - SI Unit, T - Trend."
    }
  ],
  "exam_traps": [
    "Negative Marking Trap 1: Unit confusion (e.g., Joules vs Calories, m/s vs km/h).",
    "Negative Marking Trap 2: Confusing similar biological terms or processes.",
    "Negative Marking Trap 3: Sign conventions in optics / chemical oxidation states.",
    "Negative Marking Trap 4: Misreading 'NOT true' or 'INCORRECT' in questions."
  ],
  "checklist_items": [
    "Fundamental definitions, SI units, and scientific laws thoroughly memorized.",
    "Key biological structures, chemical reactions, or physical equations mastered.",
    "All 10 practice MCQs solved with accurate conceptual reasoning.",
    "Achieved 20+ marks in the 5-minute timed exam hall mini-test."
  ]
}
`;
}

// 6. HTML Page Renderer (Using Common CSS & JS Runtime, NO FOOTER)
function renderTopicPage(topic, data, prevTopic, nextTopic) {
  const canonicalUrl = `${DOMAIN}${topic.href}`;
  const pageTitle = `${topic.nameEn} | UP Teacher Science | SJMaths`;
  const metaDesc = `Exhaustive pointwise study notes, comparative analysis, 10 practice MCQs, timed mini test, and revision traps for ${topic.nameEn} (Part 2C Science) for UP Upper Primary Assistant Teacher Exam 2026.`;

  // Escape helper
  const esc = (s) => String(s || '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');

  // Clean MCQ Option Prefix
  function cleanOptionText(opt) {
    if (!opt) return '';
    return String(opt).replace(/^(\([A-D]\)|\[[A-D]\]|[A-D][\).:-]|[A-D]\s*[-–—]\s*|[A-D]\s+)\s*/i, '').trim();
  }

  // Render Concepts
  let conceptsHtml = '';
  (data.concepts || []).forEach(c => {
    const cleanHeading = (c.heading || '').replace(/\s*\(Pointwise Breakdown\)/gi, '');
    conceptsHtml += `
        <div class="prep-card">
            <h2>
                <i class="fas fa-bookmark" style="color: var(--brand-emerald);"></i>
                <span>${esc(cleanHeading)}</span>
            </h2>
            <div class="topic-content-body">
                ${c.html_content || c.content_html || ''}
            </div>
        </div>`;
  });

  // Render Comparative Table
  let compTableHtml = '';
  const tableData = data.comparative_table || data.comparison_table;
  if (tableData && tableData.headers && tableData.rows) {
    let ths = tableData.headers.map(h => `<th>${esc(h)}</th>`).join('');
    let trs = tableData.rows.map(row => {
      let tds = row.map((cell, idx) => {
        if (idx === 0) return `<td><strong>${esc(cell)}</strong></td>`;
        return `<td>${esc(cell)}</td>`;
      }).join('');
      return `<tr>${tds}</tr>`;
    }).join('');

    compTableHtml = `
        <div class="prep-card">
            <h2>
                <i class="fas fa-table-columns" style="color: var(--brand-emerald);"></i>
                <span>${esc(tableData.title || 'Comprehensive Scientific Matrix & High-Yield Analysis')}</span>
            </h2>
            <div class="table-scroll-wrapper">
                <table class="prep-table">
                    <thead>
                        <tr>${ths}</tr>
                    </thead>
                    <tbody>
                        ${trs}
                    </tbody>
                </table>
            </div>
        </div>`;
  }

  // Render Practice Questions (10 MCQs)
  let mcqsHtml = '';
  (data.mcqs || []).forEach((q, idx) => {
    let optionsListHtml = '';
    (q.options || []).forEach((opt, optIdx) => {
      const letter = ['A', 'B', 'C', 'D'][optIdx];
      const isCorrect = optIdx === q.correct_index;
      const cleaned = cleanOptionText(opt);
      optionsListHtml += `
            <button type="button" class="mcq-option-btn" data-correct="${isCorrect ? 'true' : 'false'}" onclick="handleMcqOptionClick(this, ${idx})">
                <span class="opt-label">${letter}</span>
                <span>${esc(cleaned)}</span>
            </button>`;
    });

    mcqsHtml += `
        <div class="mcq-item-card" id="mcq-card-${idx}">
            <div class="mcq-header-meta">
                <span class="mcq-q-pill">Question ${idx + 1} of ${data.mcqs.length}</span>
                <span class="mcq-exam-pill"><i class="fas fa-graduation-cap"></i> Super TET Junior Science</span>
            </div>
            <div class="mcq-question-text">
                <p><strong>${idx + 1}.</strong> ${esc(q.question)}</p>
            </div>
            <div class="mcq-options-group">
                ${optionsListHtml}
            </div>
            <div class="mcq-explanation-box" id="mcq-exp-${idx}">
                <div class="exp-badge"><i class="fas fa-circle-check"></i> Correct Answer: Option ${['A', 'B', 'C', 'D'][q.correct_index]}</div>
                <p style="margin: 0; font-size: 0.93rem; line-height: 1.6;">${esc(q.explanation)}</p>
            </div>
        </div>`;
  });

  // Render Revision Facts
  const revFacts = data.revision_facts || (data.revision_points && data.revision_points.high_yield_facts) || [];
  let factsHtml = '';
  revFacts.forEach((fact, fIdx) => {
    factsHtml += `
        <div class="revision-fact-row">
            <span class="fact-num-badge">#${fIdx + 1}</span>
            <div class="fact-text-col">${fact}</div>
        </div>`;
  });

  // Render Mnemonics
  const mnemonicsList = data.mnemonics || (data.revision_points && data.revision_points.mnemonics) || [];
  let mnemonicsHtml = '';
  mnemonicsList.forEach(m => {
    if (typeof m === 'string') {
      mnemonicsHtml += `
        <div class="mnemonic-card">
            <div class="mnemonic-quote-box">
                <i class="fas fa-lightbulb"></i> ${esc(m)}
            </div>
        </div>`;
    } else {
      mnemonicsHtml += `
        <div class="mnemonic-card">
            <h3 style="font-size: 1.05rem; margin: 0 0 0.5rem 0; color: var(--brand-indigo);">
                <i class="fas fa-lightbulb"></i> ${esc(m.title)}
            </h3>
            <div class="mnemonic-quote-box">
                <strong>Memory Key:</strong> <code>${esc(m.acronym)}</code>
            </div>
            <p style="margin: 0; font-size: 0.92rem; color: var(--text-sub);">${esc(m.expansion)}</p>
        </div>`;
    }
  });

  // Render Negative Marking Traps
  const trapsList = data.exam_traps || (data.revision_points && data.revision_points.exam_traps) || [];
  let trapsHtml = '';
  trapsList.forEach((trap, tIdx) => {
    trapsHtml += `
        <div class="trap-card-item">
            <i class="fas fa-triangle-exclamation" style="color: #dc2626; font-size: 1.15rem; margin-top: 2px;"></i>
            <div>
                <strong>Negative Marking Alert #${tIdx + 1}:</strong>
                <p style="margin: 0.25rem 0 0 0;">${esc(trap)}</p>
            </div>
        </div>`;
  });

  // Render Mastery Checklist
  const checklist = data.checklist_items || [
    'Fundamental definitions, SI units, and scientific laws thoroughly memorized.',
    'Key biological structures, chemical reactions, or physical equations mastered.',
    'All 10 practice MCQs solved with accurate conceptual reasoning.',
    'Achieved 20+ marks in the 5-minute timed exam hall mini-test.'
  ];
  let checklistHtml = '';
  checklist.forEach((item, cIdx) => {
    checklistHtml += `
        <label class="mastery-check-item">
            <input type="checkbox" id="chk-mastery-${cIdx}" class="custom-check" onchange="updateMasteryProgress()">
            <span>${esc(item)}</span>
        </label>`;
  });

  // Prev / Next Navigation Links
  const prevLinkHtml = prevTopic
    ? `<a href="${prevTopic.href}" class="topic-nav-btn prev-btn"><i class="fas fa-chevron-left"></i> <span>Previous: ${esc(prevTopic.nameEn.slice(0, 32))}...</span></a>`
    : `<div class="topic-nav-btn disabled"><i class="fas fa-chevron-left"></i> <span>First Topic</span></div>`;

  const nextLinkHtml = nextTopic
    ? `<a href="${nextTopic.href}" class="topic-nav-btn next-btn"><span>Next: ${esc(nextTopic.nameEn.slice(0, 32))}...</span> <i class="fas fa-chevron-right"></i></a>`
    : `<a href="/up-upper-primary-teacher/science/" class="topic-nav-btn next-btn"><span>Back to Science Hub</span> <i class="fas fa-arrow-up"></i></a>`;

  // Mini Test JSON Data
  const miniTestDataJson = JSON.stringify(data.mcqs || []);

  return `<!DOCTYPE html>
<html lang="en">
<head>
<script async="" crossorigin="anonymous" src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7924751316191829"></script>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>${pageTitle}</title>
<meta content="${esc(topic.nameEn)}, ${esc(topic.nameHi)}, Science UP Upper Primary Teacher, Class 6-8 Teacher Syllabus, Super TET Junior Science Notes, UP Assistant Teacher, SJMaths" name="keywords"/>
<meta content="SJMaths" name="author"/>
<meta content="${metaDesc}" name="description"/>
<meta content="index, follow, max-image-preview:large" name="robots"/>
<link href="${canonicalUrl}" rel="canonical"/>
<link href="/favicon.png" rel="icon" type="image/png"/>

<!-- Open Graph -->
<meta property="og:title" content="${pageTitle}"/>
<meta content="${metaDesc}" property="og:description"/>
<meta content="article" property="og:type"/>
<meta content="${canonicalUrl}" property="og:url"/>
<meta content="${DOMAIN}/assets/icons/icon-512x512.png" property="og:image"/>

<!-- Twitter Card -->
<meta content="summary_large_image" name="twitter:card"/>
<meta name="twitter:title" content="${pageTitle}"/>
<meta content="${metaDesc}" name="twitter:description"/>
<meta content="${DOMAIN}/assets/icons/icon-512x512.png" name="twitter:image"/>

<!-- Fonts and Icons -->
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Outfit:wght@500;600;700;800;900&display=swap" rel="stylesheet"/>
<link as="style" crossorigin="anonymous" href="/assets/vendor/fontawesome/css/all.min.css?v=db73e473" onload="this.onload=null;this.rel='stylesheet'" rel="preload"/>
<noscript>
<link href="/assets/vendor/fontawesome/css/all.min.css?v=db73e473" rel="stylesheet"/>
</noscript>

<!-- Stylesheets -->
<link href="/assets/css/main.min.css?v=a3faaea0" rel="stylesheet"/>
<link href="/assets/css/layout.min.css?v=e4922b08" rel="stylesheet"/>
<link href="/assets/css/component.min.css?v=3fce8e36" rel="stylesheet"/>
<link href="/assets/css/improved-ui.min.css?v=dd2cffe9" rel="stylesheet"/>
<link href="/assets/css/pages.min.css?v=9e3bd560" rel="stylesheet"/>
<link href="/assets/css/up-upper-primary-topic.min.css" rel="stylesheet"/>

<!-- Breadcrumb Schema -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "${DOMAIN}/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "UP Upper Primary Teacher",
      "item": "${DOMAIN}/up-upper-primary-teacher/"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Science",
      "item": "${DOMAIN}/up-upper-primary-teacher/science/"
    },
    {
      "@type": "ListItem",
      "position": 4,
      "name": "${esc(topic.nameEn)}",
      "item": "${canonicalUrl}"
    }
  ]
}
</script>
</head>
<body>
<div id="header-container"></div>

<main class="topic-page-container" id="main-content">

    <!-- Top Action & Breadcrumbs -->
    <div class="top-action-bar">
        <div class="breadcrumb-trail">
            <a href="/"><i class="fas fa-home"></i> Home</a>
            <i class="fas fa-chevron-right" style="font-size: 0.7rem; opacity: 0.5;"></i>
            <a href="/up-upper-primary-teacher/">UP Upper Primary</a>
            <i class="fas fa-chevron-right" style="font-size: 0.7rem; opacity: 0.5;"></i>
            <a href="/up-upper-primary-teacher/science/">Science</a>
            <i class="fas fa-chevron-right" style="font-size: 0.7rem; opacity: 0.5;"></i>
            <span style="color: var(--brand-emerald-dark); font-weight: 700;">Topic #${topic.num}</span>
        </div>
        <a href="/up-upper-primary-teacher/science/" class="back-hub-btn">
            <i class="fas fa-arrow-left"></i>
            <span>Back to Science Hub</span>
        </a>
    </div>

    <!-- Topic Hero Panel -->
    <div class="topic-hero-panel">
        <div class="topic-meta-row">
            <span class="topic-badge-pill">#${topic.num} Compulsory</span>
            <span class="subject-tag-pill">${esc(topic.secTitleEn.replace(/^Module \d+:\s*/, ''))}</span>
            <span class="subject-tag-pill">${topic.tag}</span>
        </div>
        <h1>${esc(topic.nameEn)}</h1>
        <div class="topic-hero-subtitle">${esc(topic.nameHi)}</div>
        <p class="lead-desc">${esc(data.key_focus_summary || metaDesc)}</p>
    </div>

    <!-- Live Completion Toggle -->
    <div class="completion-card">
        <div class="completion-card-left">
            <i class="fas fa-tasks" style="font-size: 1.5rem; color: var(--brand-emerald);"></i>
            <div>
                <strong style="font-size: 1rem; color: var(--text-headline);">Preparation Status</strong>
                <p style="margin: 2px 0 0 0; font-size: 0.85rem; color: var(--text-muted);" id="statusDesc">
                    Mark complete once covered. Progress syncs automatically with the main syllabus hub.
                </p>
            </div>
        </div>
        <button id="topicCompletionBtn" class="toggle-topic-btn" onclick="toggleTopicStatus()">
            <i class="fas fa-check-circle"></i>
            <span id="completionBtnText">Mark as Completed</span>
        </button>
    </div>

    <!-- Study Tabs Strip -->
    <div class="study-tabs-strip" role="tablist">
        <button class="study-tab-btn active" data-tab="concepts">
            <i class="fas fa-book-open"></i>
            <span>1. Concepts &amp; Theory</span>
        </button>
        <button class="study-tab-btn" data-tab="practice">
            <i class="fas fa-list-check"></i>
            <span>2. Practice Questions (10 MCQs)</span>
        </button>
        <button class="study-tab-btn" data-tab="test">
            <i class="fas fa-stopwatch"></i>
            <span>3. Mini Test</span>
        </button>
        <button class="study-tab-btn" data-tab="revision">
            <i class="fas fa-redo"></i>
            <span>4. Quick Revision &amp; Traps</span>
        </button>
    </div>

    <!-- ==================== TAB 1: CONCEPTS & THEORY ==================== -->
    <div class="study-tab-pane active" id="tab-concepts">
        <div style="background: var(--brand-emerald-subtle); border-left: 4px solid var(--brand-emerald); padding: 1rem 1.25rem; border-radius: 8px; margin-bottom: 1.5rem;">
            <p style="margin: 0; font-size: 0.95rem; color: var(--text-headline); line-height: 1.6;">
                <i class="fas fa-compass" style="color: var(--brand-emerald); margin-right: 0.4rem;"></i>
                <strong>Syllabus Focus &amp; High-Yield Strategy:</strong> ${esc(data.key_focus_summary || 'Master all foundational laws, biological systems, chemical reactions, physical concepts, and experimental techniques grounded in SCERT UP & NCERT standards.')}
            </p>
        </div>
        ${conceptsHtml}
        ${compTableHtml}
    </div>

    <!-- ==================== TAB 2: PRACTICE QUESTIONS ==================== -->
    <div class="study-tab-pane" id="tab-practice">
        <div class="practice-summary-bar">
            <div>
                <strong style="color: var(--text-headline);">Practice Progress:</strong>
                <span id="practiceProgressText" style="color: var(--text-sub); margin-left: 0.5rem;">0 of ${data.mcqs.length} Answered</span>
            </div>
            <div class="practice-score-badge" id="practiceScoreBadge">Score: 0 / ${data.mcqs.length}</div>
        </div>

        ${mcqsHtml}
    </div>

    <!-- ==================== TAB 3: TIMED MINI TEST ==================== -->
    <div class="study-tab-pane" id="tab-test">
        <div class="test-rules-card" id="testRulesCard">
            <h2>
                <i class="fas fa-stopwatch" style="color: var(--brand-indigo);"></i>
                <span>5-Minute Exam Simulation Mode</span>
            </h2>
            <p style="font-size: 0.95rem; color: var(--text-sub); line-height: 1.6;">
                Experience the real pressure of Super TET Junior (Part 2C Science). You will face 10 randomized questions with negative marking (-1 for incorrect answers) and a strict 5-minute countdown.
            </p>
            <div class="test-meta-grid">
                <div class="meta-item">
                    <i class="fas fa-clock"></i>
                    <div>
                        <strong>Time Limit:</strong>
                        <p style="margin:0;">5 Minutes (300s)</p>
                    </div>
                </div>
                <div class="meta-item">
                    <i class="fas fa-calculator"></i>
                    <div>
                        <strong>Marking Scheme:</strong>
                        <p style="margin:0;">+3 Marks | -1 Negative</p>
                    </div>
                </div>
                <div class="meta-item">
                    <i class="fas fa-trophy"></i>
                    <div>
                        <strong>Passing Benchmark:</strong>
                        <p style="margin:0;">21+ Marks (70%)</p>
                    </div>
                </div>
            </div>
            <button class="start-test-btn" id="startTestBtn" onclick="startMiniTest()">
                <i class="fas fa-play"></i>
                <span>Start Timed Mini Test</span>
            </button>
        </div>

        <div id="testActiveContainer" style="display: none;">
            <div class="test-countdown-bar">
                <div class="timer-display">
                    <i class="fas fa-stopwatch"></i>
                    <span id="testTimerText">05:00</span>
                </div>
                <button class="finish-test-early-btn" onclick="submitMiniTest()">
                    <i class="fas fa-flag-checkered"></i>
                    <span>Submit Test</span>
                </button>
            </div>
            <div id="testQuestionsTarget"></div>
        </div>

        <div class="test-score-modal" id="testScoreModal" style="display: none;">
            <div class="score-card-inner">
                <div class="score-trophy-icon" id="scoreIcon">
                    <i class="fas fa-award"></i>
                </div>
                <h2 id="scoreTitle">Test Completed!</h2>
                <p id="scoreSubtitle" style="color: var(--text-sub); margin-bottom: 1.5rem;">Here is your performance breakdown under negative marking conditions:</p>
                <div class="score-stats-grid">
                    <div class="stat-box">
                        <span class="stat-num" id="statCorrect">0</span>
                        <span class="stat-lbl">Correct (+3)</span>
                    </div>
                    <div class="stat-box">
                        <span class="stat-num" id="statIncorrect" style="color: #dc2626;">0</span>
                        <span class="stat-lbl">Wrong (-1)</span>
                    </div>
                    <div class="stat-box">
                        <span class="stat-num" id="statSkipped" style="color: #94a3b8;">0</span>
                        <span class="stat-lbl">Skipped</span>
                    </div>
                    <div class="stat-box">
                        <span class="stat-num" id="statFinalScore" style="color: var(--brand-emerald-dark); font-weight: 800;">0</span>
                        <span class="stat-lbl">Final Score (/30)</span>
                    </div>
                </div>
                <button class="retake-test-btn" onclick="resetMiniTest()">
                    <i class="fas fa-rotate-left"></i>
                    <span>Retake Test</span>
                </button>
            </div>
        </div>
    </div>

    <!-- ==================== TAB 4: QUICK REVISION & TRAPS ==================== -->
    <div class="study-tab-pane" id="tab-revision">
        <div class="prep-card">
            <h2>
                <i class="fas fa-bolt" style="color: #eab308;"></i>
                <span>High-Yield Rapid Recall Facts (Must-Remember Pointers)</span>
            </h2>
            <div class="quick-facts-container">
                ${factsHtml}
            </div>
        </div>

        <div class="prep-card">
            <h2>
                <i class="fas fa-brain" style="color: var(--brand-indigo);"></i>
                <span>Memory Mnemonics Vault (Exam Retention Anchors)</span>
            </h2>
            <div class="mnemonics-grid">
                ${mnemonicsHtml}
            </div>
        </div>

        <div class="prep-card">
            <h2>
                <i class="fas fa-shield-halved" style="color: #dc2626;"></i>
                <span>Negative Marking Traps &amp; Common Pitfalls (-1 Penalty Avoidance)</span>
            </h2>
            <div class="traps-container">
                ${trapsHtml}
            </div>
        </div>

        <div class="prep-card">
            <h2>
                <i class="fas fa-circle-check" style="color: var(--brand-emerald);"></i>
                <span>Self-Assessment Checklist</span>
            </h2>
            <div class="topic-mastery-checklist">
                ${checklistHtml}
            </div>
        </div>
    </div>

    <!-- Bottom Sequential Navigation -->
    <div class="bottom-topic-nav">
        ${prevLinkHtml}
        ${nextLinkHtml}
    </div>

</main>

<button aria-label="Back to Top" class="back-to-top-btn" id="backToTopBtn">
    <i class="fas fa-arrow-up"></i>
</button>

<!-- Interactive Logic -->
<script>
    window.TOPIC_STORAGE_KEY = 'up-upper-primary-teacher-checklist-v2';
    window.TOPIC_CHECKBOX_ID = '${topic.chkId}';
    window.testData = ${miniTestDataJson};
</script>
<script data-cfasync="false" defer="" src="/assets/js/up-upper-primary-topic.min.js"></script>
<script data-cfasync="false" defer="" src="/assets/js/search.min.js?v=a16d370a"></script>
<script data-cfasync="false" defer="" src="/assets/js/main.min.js?v=c0d93c8c"></script>
<script data-cfasync="false" defer="" src="/assets/js/global-header.min.js?v=d48c181a"></script>
<script src="/assets/js/require-auth.min.js?v=3060658c" type="module"></script>
</body>
</html>
`;
}

// 7. Robust Atomic Writing with Retries on Windows
async function safeWriteFile(filePath, content, attempts = 12) {
  const tmpPath = `${filePath}.tmp.${Date.now()}`;
  for (let i = 0; i < attempts; i++) {
    try {
      await fs.promises.writeFile(tmpPath, content, 'utf8');
      try {
        await fs.promises.rename(tmpPath, filePath);
        return;
      } catch {
        await fs.promises.copyFile(tmpPath, filePath);
        await fs.promises.unlink(tmpPath).catch(() => {});
        return;
      }
    } catch (err) {
      if (fs.existsSync(tmpPath)) {
        await fs.promises.unlink(tmpPath).catch(() => {});
      }
      if (i === attempts - 1) {
        try {
          fs.writeFileSync(filePath, content, 'utf8');
          return;
        } catch {
          throw err;
        }
      }
      await new Promise(r => setTimeout(r, 800));
    }
  }
}

// 8. Gemini Generation Call with Multi-Model Fallback & Rotation
async function callGemini(topic, attempt = 1) {
  const prompt = buildPrompt(topic);
  const cfg = getActiveConfig();
  const client = new GoogleGenAI({ apiKey: cfg.key });

  for (const modelToTry of cfg.models) {
    try {
      const response = await client.models.generateContent({
        model: modelToTry,
        contents: prompt,
        config: {
          responseMimeType: 'application/json',
          temperature: 0.25,
        }
      });

      let rawText = response.text?.trim() || '';
      if (rawText.startsWith('```')) {
        rawText = rawText.replace(/^```(?:json)?\s*/i, '').replace(/```\s*$/, '').trim();
      }

      try {
        return JSON.parse(rawText);
      } catch {
        const repaired = jsonrepair(rawText);
        return JSON.parse(repaired);
      }
    } catch (err) {
      const msg = err.message || '';
      console.warn(`    ⚠️  [Attempt ${attempt}/6] Error on ${cfg.name} (${modelToTry}): ${msg.slice(0, 90)}`);

      if (msg.includes('503') || msg.includes('404') || msg.includes('429')) {
        continue;
      }
    }
  }

  // All models on this key failed or exhausted, rotate to next key
  rotateKey();

  if (attempt < 6) {
    const delay = Math.min(attempt * 4000, 20000);
    console.log(`    ⏳ Retrying in ${delay / 1000}s with next key...`);
    await new Promise(r => setTimeout(r, delay));
    return callGemini(topic, attempt + 1);
  }
  throw new Error(`Failed to generate topic #${topic.num} after ${attempt} attempts across all keys/models.`);
}

// 9. Main Controller
async function main() {
  console.log('================================================================');
  console.log('  UP Upper Primary Teacher (Class 6-8) — Science Generator');
  console.log(`  Mode: ${DRY_RUN ? 'DRY RUN' : 'PRODUCTION'}`);
  console.log(`  Loaded ${allTopics.length} micro-topics from Science Tracker Hub`);
  console.log('================================================================\n');

  let queue = allTopics;

  if (TARGET_TOPIC) {
    queue = queue.filter(t => t.slug === TARGET_TOPIC || t.numStr === TARGET_TOPIC || t.num === parseInt(TARGET_TOPIC, 10));
    if (queue.length === 0) {
      console.error(`ERROR: Target topic "${TARGET_TOPIC}" not found.`);
      process.exit(1);
    }
  } else if (TARGET_SECTION) {
    const secNum = parseInt(TARGET_SECTION, 10);
    queue = queue.filter(t => t.secIdx === secNum);
    console.log(`Filtering to Section ${secNum}: ${queue.length} topics found.`);
  }

  if (LIMIT && LIMIT > 0) {
    queue = queue.slice(0, LIMIT);
    console.log(`Limiting execution to first ${LIMIT} topics.`);
  }

  console.log(`Processing queue of ${queue.length} topics...\n`);

  let count = 0;
  for (let i = 0; i < queue.length; i++) {
    const topic = queue[i];
    const prevTopic = allTopics[topic.num - 2] || null;
    const nextTopic = allTopics[topic.num] || null;
    const outDir = path.join(OUTPUT_DIR, topic.slug);
    const outFile = path.join(outDir, 'index.html');

    const alreadyDone = !FORCE && statusMap[topic.slug]?.version === 'v2-pointwise' && fs.existsSync(outFile);
    if (alreadyDone) {
      console.log(`[${i + 1}/${queue.length}] [SKIP] Topic #${topic.num} (${topic.slug}) already completed (v2-pointwise).`);
      continue;
    }

    count++;
    console.log(`[${i + 1}/${queue.length}] [GENERATE] Topic #${topic.num}: ${topic.nameEn}`);
    console.log(`  Target File: ${outFile}`);

    if (DRY_RUN) {
      console.log('  [DRY-RUN] Prompt verified. Skipping API call.\n');
      continue;
    }

    try {
      const data = await callGemini(topic);

      if (!fs.existsSync(outDir)) {
        fs.mkdirSync(outDir, { recursive: true });
      }

      const html = renderTopicPage(topic, data, prevTopic, nextTopic);
      await safeWriteFile(outFile, html);

      const stat = fs.statSync(outFile);
      const sizeKb = (stat.size / 1024).toFixed(1);
      console.log(`  ✅ Successfully written (${sizeKb} KB) with pointwise notes, tables & 10 MCQs!\n`);

      statusMap[topic.slug] = {
        num: topic.num,
        nameEn: topic.nameEn,
        nameHi: topic.nameHi,
        section: topic.secIdx,
        completed: true,
        version: 'v2-pointwise',
        fileSizeKb: sizeKb,
        mcqCount: (data.mcqs || []).length,
        updatedAt: new Date().toISOString(),
      };
      saveStatus();

      // Graceful pacing between topics
      await new Promise(r => setTimeout(r, 1200));
    } catch (err) {
      console.error(`  ❌ Failed Topic #${topic.num} (${topic.slug}): ${err.message}\n`);
    }
  }

  console.log('================================================================');
  console.log(`Generation completed. Processed ${count} topics.`);
  console.log('================================================================\n');
}

main().catch(err => {
  console.error('Fatal execution error:', err);
  process.exit(1);
});
