#!/usr/bin/env node
/**
 * ============================================================================
 * SJ Maths — UP Upper Primary Assistant Teacher (Class 6-8) Social Studies
 * Pointwise Concept Notes, Memory Mnemonics, Tips, Tricks & 10 Interactive MCQs
 * Powered by Google Gemini API via @google/genai SDK
 *
 * Examination: UP Upper Primary Assistant Teacher Recruitment 2026 (Super TET Junior)
 * Subject: Social Studies (Part 2B: 90 Questions | 270 Marks | -1 Negative Marking)
 * Covers all 48 Modular Micro-Topics across 5 Sections:
 *   1. Ancient Indian History (Topics 1 to 9)
 *   2. Medieval & Modern Indian History (Topics 10 to 22)
 *   3. Civics, Society, Governance & Safety (Topics 23 to 30)
 *   4. Geography & Uttar Pradesh Special (Topics 31 to 40)
 *   5. Atmosphere, Economy, Environment & Disaster Management (Topics 41 to 48)
 *
 * Uses common CSS: /assets/css/up-upper-primary-topic.min.css
 * Uses common JS:  /assets/js/up-upper-primary-topic.min.js
 * ============================================================================
 */

import fs from 'node:fs';
import path from 'node:path';
import 'dotenv/config';
import { GoogleGenAI } from '@google/genai';
import { jsonrepair } from 'jsonrepair';

const ROOT = process.cwd();
const DOMAIN = 'https://sjmaths.com';
const TRACKER_PATH = path.join(ROOT, 'up-upper-primary-teacher', 'social-studies', 'index.html');
const STATUS_FILE = path.join(ROOT, 'content-generation-status-upper-primary-social-studies.json');
const OUTPUT_DIR = path.join(ROOT, 'up-upper-primary-teacher', 'social-studies');

// 1. API Key & Model Configuration
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
const ALL = args.includes('--all');
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
  return idx !== -1 && args[idx + 1] ? args[idx + 1] : 'gemini-3.8-flash';
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

// 4. Extract Syllabus from Social Studies Tracker Hub
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
      const slug = cleanHref.replace('/up-upper-primary-teacher/social-studies/', '').replace(/\//g, '');
      const numRaw = tMatch[3].trim().replace('#', '');
      const num = parseInt(numRaw, 10);

      topicList.push({
        chkId: tMatch[1],
        href: cleanHref,
        slug,
        num,
        numStr: `#${num}`,
        nameHi: decodeHtml(tMatch[4].trim()),
        nameEn: decodeHtml(tMatch[5].trim()),
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

// 5. Pointwise & High-Yield English Prompt Builder
function buildPrompt(topic) {
  return `You are a Senior Professor of Social Studies, Chief Curriculum Advisor for SCERT Uttar Pradesh & NCERT, and Senior Head Question Paper Setter for the Uttar Pradesh Upper Primary Assistant Teacher Recruitment Examination (Super TET Junior — Part 2B Social Studies: 90 Questions | 270 Marks | -1 Negative Marking Penalty).

Create exhaustive, strictly POINTWISE classroom study notes, comparative analysis tables, memory mnemonics, shortcut tricks, exam traps, and 10 high-quality exam practice MCQs in ENGLISH for this exact syllabus topic:
- Examination: UP Upper Primary Assistant Teacher Recruitment (Class 6-8) 2026
- Subject: Social Studies (Part 2B Compulsory: 90 Questions | 270 Marks | -1 Negative Marking)
- Section ${topic.secIdx}: ${topic.secTitleEn}
- Topic #${topic.num}: ${topic.nameEn}
- Official Hindi Reference: ${topic.nameHi}
- Canonical URL: ${DOMAIN}${topic.href}

CRITICAL PEDAGOGICAL & STRUCTURAL RULES (STRICT COMPLIANCE REQUIRED):
1. STRICTLY POINTWISE ARCHITECTURE:
   - ZERO continuous narrative prose or long paragraphs.
   - Every single concept MUST be broken into structured point-cards wrapped in <div class="point-grid"><div class="point-card"><strong>[Key Term / Ruler / Event / Treaty / Article / Dynamic]:</strong> Exhaustive, deep factual detail...</div>...</div>.
   - Each point-card MUST begin with a bold key concept, historical year, constitutional article, geographic feature, or legal rule.
   - Do NOT omit ANY facts, dates, sites, treaties, mechanisms, or figures. Grounded in SCERT UP Class 6-8 textbooks ("Hamara Itihas aur Nagrik Jivan", "Prithvi aur Hamara Jivan", "Hamari Arthvyavastha", "Paryavaran Adhyayan") and NCERT standards.

2. EMBEDDED COGNITIVE ANCHORS:
   - In Concept 1: Embed at least ONE <div class="tip-box"><i class="fas fa-lightbulb"></i> <strong>Exam Pro-Tip:</strong> ...</div> AND at least ONE <div class="mnemonic-inline-box"><i class="fas fa-brain"></i> <strong>Memory Mnemonic:</strong> <code>ACRONYM</code> — ...</div>.
   - In Concept 2: Embed a structured comparison sub-table <div class="topic-subtable-wrapper"><table class="topic-subtable"><thead><tr><th>Entity / Category</th><th>Core Features & Data</th><th>High-Yield Exam Takeaway</th></tr></thead><tbody><tr><td><strong>Item 1</strong></td><td>...</td><td>...</td></tr><tr><td><strong>Item 2</strong></td><td>...</td><td>...</td></tr></tbody></table></div> AND at least ONE <div class="trick-box"><i class="fas fa-bolt"></i> <strong>Shortcut Trick:</strong> ...</div>.
   - In Concept 3: Provide detailed, exhaustive point-cards specifically focusing on Uttar Pradesh relevance (UP archaeological sites, UP districts, UP rulers/events, UP rivers/soils/minerals, UP local governance, etc.) AND at least ONE <div class="tip-box"><i class="fas fa-lightbulb"></i> <strong>UP Exam High-Yield Tip:</strong> ...</div>.
   - In Concept 4: Embed edge cases, misconceptions, and trap prevention tips: <div class="trick-box"><i class="fas fa-bolt"></i> <strong>Trap Prevention Trick:</strong> ...</div> AND <div class="mnemonic-inline-box"><i class="fas fa-brain"></i> <strong>Memory Mnemonic:</strong> <code>KEY</code> — ...</div>.

3. 10 HIGH-QUALITY EXAM MCQs:
   - Exactly 10 MCQs matching the competitive standard of Super TET Junior Part 2B.
   - 4 plausible options without A/B/C/D prefixes.
   - 0-based correct_index (0, 1, 2, 3).
   - In-depth analytical explanation detailing why the correct option is right and explaining the distractors.

4. QUICK REVISION & TRAPS VAULT:
   - 8 rapid recall facts.
   - 2 memory mnemonics with title, acronym, and expansion.
   - 4 negative-marking alerts (-1 penalty avoidance).
   - 4 self-assessment checklist items.

5. CLEAN EDITORIAL VOICE:
   - Strictly NO meta-prompt references, NO phrases like "zero narrative paragraphs", NO "(Pointwise Breakdown)" in titles. Natural, authoritative textbook tone.

JSON SCHEMA TO RETURN (EXACTLY AS DEFINED, RAW JSON ONLY):
{
  "key_focus_summary": "Crisp 2-3 sentence overview of this topic, key examination weightage, and high-yield focus areas for Super TET Junior.",
  "concepts": [
    {
      "heading": "1. Core Concepts & Foundational Principles",
      "html_content": "<div class=\"point-grid\"><div class=\"point-card\"><strong>Key Principle 1:</strong> ...</div><div class=\"point-card\"><strong>Key Principle 2:</strong> ...</div><div class=\"point-card\"><strong>Key Principle 3:</strong> ...</div><div class=\"point-card\"><strong>Key Principle 4:</strong> ...</div></div><div class=\"tip-box\"><i class=\"fas fa-lightbulb\"></i> <strong>Exam Pro-Tip:</strong> ...</div><div class=\"mnemonic-inline-box\"><i class=\"fas fa-brain\"></i> <strong>Memory Mnemonic:</strong> <code>KEY</code> — ...</div>"
    },
    {
      "heading": "2. Structural Classifications, Chronology & Key Systems",
      "html_content": "<div class=\"topic-subtable-wrapper\"><table class=\"topic-subtable\"><thead><tr><th>Entity / Category</th><th>Core Features & Data</th><th>High-Yield Exam Takeaway</th></tr></thead><tbody><tr><td><strong>Category 1</strong></td><td>Details...</td><td>Takeaway...</td></tr><tr><td><strong>Category 2</strong></td><td>Details...</td><td>Takeaway...</td></tr></tbody></table></div><div class=\"point-grid\"><div class=\"point-card\"><strong>System / Dynamic 1:</strong> ...</div><div class=\"point-card\"><strong>System / Dynamic 2:</strong> ...</div><div class=\"point-card\"><strong>System / Dynamic 3:</strong> ...</div></div><div class=\"trick-box\"><i class=\"fas fa-bolt\"></i> <strong>Shortcut Trick:</strong> ...</div>"
    },
    {
      "heading": "3. Uttar Pradesh Regional Perspective & Sites",
      "html_content": "<div class=\"point-grid\"><div class=\"point-card\"><strong>UP Landmark / Feature 1:</strong> ...</div><div class=\"point-card\"><strong>UP Landmark / Feature 2:</strong> ...</div><div class=\"point-card\"><strong>UP Landmark / Feature 3:</strong> ...</div><div class=\"point-card\"><strong>UP Landmark / Feature 4:</strong> ...</div></div><div class=\"tip-box\"><i class=\"fas fa-lightbulb\"></i> <strong>UP Exam High-Yield Tip:</strong> ...</div>"
    },
    {
      "heading": "4. Comparative Analysis & Exam Pitfalls",
      "html_content": "<div class=\"point-grid\"><div class=\"point-card\"><strong>Critical Distinction:</strong> ...</div><div class=\"point-card\"><strong>Edge Case / Exception:</strong> ...</div><div class=\"point-card\"><strong>Trap Rule:</strong> ...</div></div><div class=\"trick-box\"><i class=\"fas fa-bolt\"></i> <strong>Trap Prevention Trick:</strong> ...</div><div class=\"mnemonic-inline-box\"><i class=\"fas fa-brain\"></i> <strong>Memory Mnemonic:</strong> <code>KEY</code> — ...</div>"
    }
  ],
  "comparative_table": {
    "title": "Comprehensive Comparative Matrix & High-Yield Analysis",
    "headers": ["Key Dimension / Parameter", "Category / Feature A", "Category / Feature B", "Competitive Exam Significance"],
    "rows": [
      ["Parameter 1", "Detailed data A", "Detailed data B", "High-yield exam takeaway"],
      ["Parameter 2", "Detailed data A", "Detailed data B", "High-yield exam takeaway"],
      ["Parameter 3", "Detailed data A", "Detailed data B", "High-yield exam takeaway"],
      ["Parameter 4", "Detailed data A", "Detailed data B", "High-yield exam takeaway"]
    ]
  },
  "mcqs": [
    {
      "question": "Challenging question testing factual recall or conceptual application?",
      "options": [
        "First plausible option without any A/B/C/D letter prefix",
        "Second plausible option without any A/B/C/D letter prefix",
        "Third plausible option without any A/B/C/D letter prefix",
        "Fourth plausible option without any A/B/C/D letter prefix"
      ],
      "correct_index": 0,
      "explanation": "Detailed pedagogical explanation stating why option A is correct and dissecting why options B, C, and D are incorrect."
    }
  ],
  "revision_facts": [
    "High-yield factual takeaway 1 with specific date/law/location.",
    "High-yield factual takeaway 2 with specific date/law/location.",
    "High-yield factual takeaway 3 with specific date/law/location.",
    "High-yield factual takeaway 4 with specific date/law/location.",
    "High-yield factual takeaway 5 with specific date/law/location.",
    "High-yield factual takeaway 6 with specific date/law/location.",
    "High-yield factual takeaway 7 with specific date/law/location.",
    "High-yield factual takeaway 8 with specific date/law/location."
  ],
  "mnemonics": [
    {
      "title": "Topic Acronym / Rule",
      "acronym": "CODE",
      "expansion": "C - Concept, O - Order, D - Dynasty, E - Era."
    },
    {
      "title": "Key Sequence Anchor",
      "acronym": "FAST",
      "expansion": "F - Feature, A - Area, S - Scheme, T - Territory."
    }
  ],
  "exam_traps": [
    "Negative Marking Trap 1: Common confusion between similar sounding entities.",
    "Negative Marking Trap 2: Chronological inversion mistake in historical events.",
    "Negative Marking Trap 3: Boundary / state jurisdiction misattribution.",
    "Negative Marking Trap 4: Misreading 'NOT true' or 'INCORRECT' in questions."
  ],
  "checklist_items": [
    "Foundational chronology, definitions, and contextual origins thoroughly mastered.",
    "Key dates, administrative structures, treaties, and comparative distinctions memorized.",
    "All 10 practice MCQs solved with accurate conceptual reasoning.",
    "Achieved 20+ marks in the 5-minute timed exam hall mini-test."
  ]
}`;
}

// 6. HTML Page Renderer (Using Common CSS & JS Runtime)
function renderTopicPage(topic, data, prevTopic, nextTopic) {
  const canonicalUrl = `${DOMAIN}${topic.href}`;
  const pageTitle = `${topic.nameEn} | UP Teacher Social Studies | SJMaths`;
  const metaDesc = `Exhaustive pointwise study notes, comparative analysis, 10 practice MCQs, timed mini test, and revision traps for ${topic.nameEn} (Part 2B Social Studies) for UP Upper Primary Assistant Teacher Exam 2026.`;

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
                <span>${esc(tableData.title || 'Comprehensive Comparative Matrix & High-Yield Analysis')}</span>
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
                <span class="mcq-exam-pill"><i class="fas fa-graduation-cap"></i> Super TET Junior Social Studies</span>
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
    'Foundational chronology, definitions, and contextual origins thoroughly mastered.',
    'Key dates, administrative structures, treaties, and comparative distinctions memorized.',
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
    : `<a href="/up-upper-primary-teacher/social-studies/" class="topic-nav-btn next-btn"><span>Back to Social Studies Hub</span> <i class="fas fa-arrow-up"></i></a>`;

  // Mini Test JSON Data
  const miniTestDataJson = JSON.stringify(data.mcqs || []);

  return `<!DOCTYPE html>
<html lang="en">
<head>
<script async="" crossorigin="anonymous" src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7924751316191829"></script>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>${pageTitle}</title>
<meta content="${esc(topic.nameEn)}, ${esc(topic.nameHi)}, Social Studies UP Upper Primary Teacher, Class 6-8 Teacher Syllabus, Super TET Junior Notes, UP Assistant Teacher, SJMaths" name="keywords"/>
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
      "name": "Social Studies",
      "item": "${DOMAIN}/up-upper-primary-teacher/social-studies/"
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

<main class="topic-page-container">

    <!-- Top Action Bar -->
    <div class="top-action-bar">
        <div class="breadcrumb-trail">
            <a href="/"><i class="fas fa-home"></i> Home</a>
            <i class="fas fa-chevron-right" style="font-size: 0.7rem;"></i>
            <a href="/up-upper-primary-teacher/">UP Upper Primary</a>
            <i class="fas fa-chevron-right" style="font-size: 0.7rem;"></i>
            <a href="/up-upper-primary-teacher/social-studies/">Social Studies</a>
            <i class="fas fa-chevron-right" style="font-size: 0.7rem;"></i>
            <span>${esc(topic.numStr)}</span>
        </div>
        <a href="/up-upper-primary-teacher/social-studies/" class="back-hub-btn">
            <i class="fas fa-arrow-left"></i>
            <span>Back to Social Studies Hub</span>
        </a>
    </div>

    <!-- Topic Hero Panel -->
    <div class="topic-hero-panel">
        <div class="topic-meta-row">
            <span class="topic-badge-pill">${esc(topic.numStr)} Compulsory</span>
            <span class="subject-tag-pill">${esc(topic.secTitleEn)}</span>
            <span class="subject-tag-pill">${esc(topic.tag)}</span>
        </div>
        <h1>${esc(topic.nameEn)}</h1>
        <div class="topic-hero-subtitle">${esc(topic.nameHi)}</div>
        <p class="lead-desc">${esc(data.key_focus_summary || 'Comprehensive syllabus study notes, key principles, comparative analysis, and practice material for UP Upper Primary Assistant Teacher Exam.')}</p>
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
                <strong>Syllabus Focus &amp; High-Yield Strategy:</strong> ${esc(data.key_focus_summary || topic.nameEn)}
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

    <!-- ==================== TAB 3: MINI TEST ==================== -->
    <div class="study-tab-pane" id="tab-test">
        <div class="prep-card" id="miniTestContainer">
            <div class="mini-test-intro" id="miniTestIntro">
                <i class="fas fa-stopwatch" style="font-size: 3rem; color: var(--brand-emerald); margin-bottom: 1rem;"></i>
                <h2 style="border: none; justify-content: center; margin-bottom: 0.5rem;">Timed Mini-Test Challenge</h2>
                <p class="test-desc">Simulate the real UP Upper Primary Teacher Social Studies exam environment with this 5-minute timed test containing 10 curated questions. Negative marking (-1 per incorrect answer) is enabled.</p>
                <div class="test-stats-row">
                    <span class="test-stat-chip"><i class="fas fa-clock"></i> 5:00 Minutes</span>
                    <span class="test-stat-chip"><i class="fas fa-list-ol"></i> 10 Questions</span>
                    <span class="test-stat-chip"><i class="fas fa-plus"></i> +3 Marks</span>
                    <span class="test-stat-chip"><i class="fas fa-minus"></i> -1 Negative</span>
                </div>
                <button type="button" class="start-test-btn" onclick="startMiniTest()">
                    <i class="fas fa-play"></i> Start Mini Test Now
                </button>
            </div>

            <div id="miniTestActive" style="display: none;">
                <div class="test-timer-bar">
                    <div>
                        <span style="font-weight: 700; color: var(--text-sub);">Question <span id="testCurrentQ">1</span> of ${data.mcqs.length}</span>
                    </div>
                    <div class="test-countdown" id="testTimer">
                        <i class="fas fa-hourglass-half"></i> <span id="timerDisplay">05:00</span>
                    </div>
                </div>

                <div id="testQuestionContainer"></div>

                <div class="test-nav-controls">
                    <button type="button" class="test-btn-nav" id="testPrevBtn" onclick="navTest(-1)"><i class="fas fa-chevron-left"></i> Previous</button>
                    <button type="button" class="test-btn-nav" id="testNextBtn" onclick="navTest(1)">Next <i class="fas fa-chevron-right"></i></button>
                    <button type="button" class="test-submit-btn" id="testSubmitBtn" style="display: none;" onclick="submitMiniTest()">Submit Test <i class="fas fa-check"></i></button>
                </div>
            </div>

            <div id="miniTestResult" style="display: none; text-align: center; padding: 2rem 1rem;">
                <i class="fas fa-award" style="font-size: 3.5rem; color: #f59e0b; margin-bottom: 1rem;"></i>
                <h2 style="border: none; justify-content: center; margin-bottom: 0.5rem;" id="resultTitle">Test Completed!</h2>
                <div style="font-size: 2.2rem; font-weight: 800; color: var(--brand-emerald-dark); margin-bottom: 1rem;" id="resultScoreBanner">0 / 30</div>
                <div id="resultBreakdownGrid"></div>
                <button type="button" class="retry-test-btn" onclick="resetMiniTest()" style="margin-top: 1.5rem;">
                    <i class="fas fa-redo"></i> Retake Test
                </button>
            </div>
        </div>
    </div>

    <!-- ==================== TAB 4: QUICK REVISION & TRAPS ==================== -->
    <div class="study-tab-pane" id="tab-revision">
        <div class="prep-card">
            <h2>
                <i class="fas fa-bolt" style="color: #f59e0b;"></i>
                <span>High-Yield Rapid Recall Facts</span>
            </h2>
            <div class="revision-facts-grid">
                ${factsHtml}
            </div>
        </div>

        ${mnemonicsHtml ? `
        <div class="prep-card">
            <h2>
                <i class="fas fa-brain" style="color: var(--brand-indigo);"></i>
                <span>Memory Mnemonics &amp; Retention Anchors</span>
            </h2>
            ${mnemonicsHtml}
        </div>` : ''}

        <div class="prep-card">
            <h2>
                <i class="fas fa-triangle-exclamation" style="color: #dc2626;"></i>
                <span>Exam Traps &amp; Negative Marking Pitfalls</span>
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
<script data-cfasync="false" defer="" src="/assets/js/main.min.js?v=1594eda0"></script>
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
        // Fallback: copyFile and unlink
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

      // If rate limited or quota exceeded, check if next model on this key works
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
  console.log('  UP Upper Primary Teacher (Class 6-8) — Social Studies Generator');
  console.log(`  Model: ${MODEL_NAME} | Mode: ${DRY_RUN ? 'DRY RUN' : 'PRODUCTION'}`);
  console.log(`  Loaded ${allTopics.length} micro-topics from Tracker Hub`);
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
