/**
 * ============================================================================
 * UP Upper Primary Assistant Teacher (Class 6-8) Recruitment 2026
 * Part 1: General Knowledge, Current Affairs & Logical Reasoning
 * Study Notes, Theory, MCQs & Timed Mini-Test Generator (English Edition)
 *
 * Exam Pattern:
 *   - Part 1 Compulsory: 30 Questions | 90 Marks
 *   - Marking Scheme: +3 for Correct, -1 Negative Marking Penalty
 *   - Total 63 Micro-Topics across 6 Modules:
 *       1. History of India & National Movement (Topics 1.1 to 1.14)
 *       2. Geography of India (Topics 2.1 to 2.10)
 *       3. Indian Polity & Governance (Topics 3.1 to 3.13)
 *       4. Economic & Social Development (Topics 4.1 to 4.8)
 *       5. Current Events, Ecology & General Science (Topics 5.1 to 5.8)
 *       6. Logical Reasoning (Topics 6.1 to 6.10)
 *
 * Usage:
 *   node scripts/generate_up_upper_primary_general_knowledge.mjs --dry-run
 *   node scripts/generate_up_upper_primary_general_knowledge.mjs --topic indus-valley-civilisation
 *   node scripts/generate_up_upper_primary_general_knowledge.mjs --module 1
 *   node scripts/generate_up_upper_primary_general_knowledge.mjs --all
 * ============================================================================
 */

import fs from 'node:fs';
import path from 'node:path';
import 'dotenv/config';
import { GoogleGenAI } from '@google/genai';
import { jsonrepair } from 'jsonrepair';

const ROOT = process.cwd();
const DOMAIN = 'https://sjmaths.com';
const TRACKER_PATH = path.join(ROOT, 'up-upper-primary-teacher', 'general-knowledge', 'index.html');
const STATUS_FILE = path.join(ROOT, 'content-generation-status-upper-primary-general-knowledge.json');

// API Key Rotation
const API_KEYS = [
  process.env.GEMINI_API_KEY_1,
  process.env.GEMINI_API_KEY_2,
  process.env.GEMINI_API_KEY,
].filter(Boolean);

if (API_KEYS.length === 0) {
  console.error('ERROR: No valid GEMINI_API_KEY found in environment or .env file!');
  process.exit(1);
}

let currentKeyIndex = 0;
function getAIClient() {
  const apiKey = API_KEYS[currentKeyIndex % API_KEYS.length];
  return {
    client: new GoogleGenAI({ apiKey }),
    keyName: `KEY_${(currentKeyIndex % API_KEYS.length) + 1}`,
  };
}

function rotateKey() {
  currentKeyIndex = (currentKeyIndex + 1) % API_KEYS.length;
  console.log(`  [Key Rotation] Rotating to next API key (${getAIClient().keyName})...`);
}

const MODEL_NAME = 'gemini-3.5-flash-lite';

// CLI Arguments
const args = process.argv.slice(2);
const DRY_RUN = args.includes('--dry-run');
const FORCE = args.includes('--force');
const TARGET_MODULE = args.find((_, i, arr) => arr[i - 1] === '--module' || arr[i - 1] === '-m');
const TARGET_TOPIC = args.find((_, i, arr) => arr[i - 1] === '--topic' || arr[i - 1] === '-t');
const LIMIT_ARG = args.find((_, i, arr) => arr[i - 1] === '--limit' || arr[i - 1] === '-l');
const LIMIT = LIMIT_ARG ? parseInt(LIMIT_ARG, 10) : null;

// HTML Helpers
function esc(str) {
  if (!str) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

function decodeHtml(html) {
  return String(html)
    .replace(/&amp;/g, '&')
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'");
}

// 1. Extract Syllabus Topics from General Knowledge Hub
function extractSyllabus() {
  if (!fs.existsSync(TRACKER_PATH)) {
    console.error(`Tracker file not found: ${TRACKER_PATH}`);
    return [];
  }
  const html = fs.readFileSync(TRACKER_PATH, 'utf8');

  const secRegex = /<details class="module-accordion" data-sec-idx="([^"]+)"[\s\S]*?<h3 class="module-title">[\s\S]*?<span class="lang-hi">([^<]+)<\/span>[\s\S]*?<span class="lang-en">([^<]+)<\/span>[\s\S]*?<ul class="module-list">([\s\S]*?)<\/ul>/g;

  let sMatch;
  const topicList = [];

  while ((sMatch = secRegex.exec(html)) !== null) {
    const [_, secIdx, secTitleHi, secTitleEn, secBody] = sMatch;
    const topicRegex = /<li class="topic-row">[\s\S]*?<input[^>]*id="([^"]+)"[\s\S]*?<a href="([^"]+)"[\s\S]*?<span class="topic-num">([^<]+)<\/span>[\s\S]*?<span class="lang-hi">([^<]+)<\/span>[\s\S]*?<span class="lang-en">([^<]+)<\/span>[\s\S]*?<span class="topic-tag">([^<]+)<\/span>/g;
    let tMatch;
    while ((tMatch = topicRegex.exec(secBody)) !== null) {
      const href = tMatch[2].startsWith('/') ? tMatch[2] : '/' + tMatch[2];
      const cleanHref = href.endsWith('/') ? href : href + '/';
      const slug = cleanHref.replace('/up-upper-primary-teacher/general-knowledge/', '').replace(/\//g, '');
      const numStr = tMatch[3].trim();

      topicList.push({
        chkId: tMatch[1],
        href: cleanHref,
        slug,
        numStr,
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

// 2. Load / Save Generation Status
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

// 3. Prompt Builder for General Knowledge Topics
function buildPrompt(topic) {
  const isReasoning = topic.secIdx === 6 || topic.tag.toLowerCase().includes('reasoning');

  return `You are a Senior Academic Subject Expert, Question Paper Setter, and Pedagogical Author for the Uttar Pradesh Basic Education Department (SCERT UP) and competitive teacher recruitments (UP Upper Primary Assistant Teacher / Super TET Junior 2026 - Part 1 Compulsory: 30 Questions | 90 Marks | -1 Negative Marking Penalty).

Your mission is to generate EXHAUSTIVE, STRICTLY POINTWISE, HIGH-RETENTION study notes and test preparation material for:
- Module ${topic.secIdx}: ${topic.secTitleEn}
- Topic #${topic.numStr}: ${topic.nameEn} (Hindi: ${topic.nameHi})
- Subject Tag: ${topic.tag}

CRITICAL PEDAGOGICAL REQUIREMENTS (MANDATORY):
1. STRICTLY POINTWISE FORMAT — ZERO LONG PARAGRAPHS:
   - DO NOT generate dense walls of prose or narrative paragraphs.
   - Every concept must be broken down into structured, high-impact bullet points inside <div class="point-grid"><div class="point-card"><strong>[Core Concept / Term / Event / Formula / Year]:</strong> Exhaustive explanation, key facts, dates, constitutional articles, or mechanisms...</div>...</div>
   - Provide AT LEAST 4 to 6 detailed, comprehensive point-cards in EACH concept section so that NO fact, theory, or examination angle is missed.
2. EXHAUSTIVE COVERAGE — ZERO OMISSIONS:
   - Ensure that ALL concepts, classifications, formulas, theorems, chronological events, constitutional articles, geographic coordinates/tributaries, economic indicators, or scientific laws related to this syllabus topic are covered in complete depth.
   - Present the full academic syllabus thoroughly, but structured strictly in bullet points and cards rather than paragraphs.
3. EMBEDDED TIPS, TRICKS & MNEMONICS INSIDE CONCEPTS:
   - In each concept section, you MUST embed:
     - <div class="tip-box"><i class="fas fa-lightbulb"></i> <strong>Exam Pro-Tip:</strong> High-yield examination tip, common question angle, or direct scoring advice...</div>
     - <div class="trick-box"><i class="fas fa-bolt"></i> <strong>Speed Trick / Shortcut:</strong> Direct memory rule, elimination trick, or calculation shortcut...</div>
     - <div class="mnemonic-inline-box"><i class="fas fa-brain"></i> <strong>Memory Mnemonic:</strong> <code>KEYWORD</code> — Detailed breakdown of what each letter/part stands for...</div>
4. SUB-TABLES INSIDE CONCEPTS:
   - In Concept 2 and/or Concept 4, embed structured HTML sub-tables comparing parameters, categories, dynasties, articles, formulas, or rules:
     <div class="topic-subtable-wrapper"><table class="topic-subtable"><thead><tr><th>Parameter / Item</th><th>Core Features & Data</th><th>High-Yield Exam Takeaway</th></tr></thead><tbody><tr><td><strong>Item 1</strong></td><td>Details...</td><td>Takeaway...</td></tr><tr><td><strong>Item 2</strong></td><td>Details...</td><td>Takeaway...</td></tr></tbody></table></div>
5. UTTAR PRADESH SPECIFIC APPLICATION:
   - In Concept 3, provide detailed, exhaustive point-cards on UP-specific relevance (UP districts, archaeological sites in UP, state institutions, UP river basins, state policies, census data, etc.).

JSON SCHEMA TO RETURN (EXACTLY AS DEFINED):
{
  "key_focus_summary": "Crisp 2-3 sentence overview of this topic, key examination weightage, and high-yield focus areas for Super TET Junior.",
  "concepts": [
    {
      "heading": "1. Core Concepts & Foundational Principles",
      "html_content": "<div class=\"point-grid\"><div class=\"point-card\"><strong>Key Principle 1:</strong> ...</div><div class=\"point-card\"><strong>Key Principle 2:</strong> ...</div><div class=\"point-card\"><strong>Key Principle 3:</strong> ...</div><div class=\"point-card\"><strong>Key Principle 4:</strong> ...</div></div><div class=\"tip-box\"><i class=\"fas fa-lightbulb\"></i> <strong>Exam Pro-Tip:</strong> ...</div><div class=\"mnemonic-inline-box\"><i class=\"fas fa-brain\"></i> <strong>Memory Mnemonic:</strong> <code>KEY</code> — ...</div>"
    },
    {
      "heading": "2. Structural Classifications & High-Yield Data",
      "html_content": "<div class=\"topic-subtable-wrapper\"><table class=\"topic-subtable\"><thead><tr><th>Classification / Category</th><th>Key Characteristics & Data</th><th>Exam Focus</th></tr></thead><tbody><tr><td><strong>Category 1</strong></td><td>Details...</td><td>Takeaway...</td></tr><tr><td><strong>Category 2</strong></td><td>Details...</td><td>Takeaway...</td></tr></tbody></table></div><div class=\"point-grid\"><div class=\"point-card\"><strong>Mechanism / Rule 1:</strong> ...</div><div class=\"point-card\"><strong>Mechanism / Rule 2:</strong> ...</div><div class=\"point-card\"><strong>Mechanism / Rule 3:</strong> ...</div></div><div class=\"trick-box\"><i class=\"fas fa-bolt\"></i> <strong>Shortcut Trick:</strong> ...</div>"
    },
    {
      "heading": "3. Uttar Pradesh Regional Perspective & Sites",
      "html_content": "<div class=\"point-grid\"><div class=\"point-card\"><strong>UP Landmark / Provision 1:</strong> ...</div><div class=\"point-card\"><strong>UP Landmark / Provision 2:</strong> ...</div><div class=\"point-card\"><strong>UP Landmark / Provision 3:</strong> ...</div><div class=\"point-card\"><strong>UP Landmark / Provision 4:</strong> ...</div></div><div class=\"tip-box\"><i class=\"fas fa-lightbulb\"></i> <strong>UP Exam High-Yield Tip:</strong> ...</div>"
    },
    {
      "heading": "4. Comparative Analysis & Exam Pitfalls",
      "html_content": "<div class=\"point-grid\"><div class=\"point-card\"><strong>Critical Distinction:</strong> ...</div><div class=\"point-card\"><strong>Edge Case / Exception:</strong> ...</div><div class=\"point-card\"><strong>Trap Rule:</strong> ...</div></div><div class=\"trick-box\"><i class=\"fas fa-bolt\"></i> <strong>Trap Prevention Trick:</strong> ...</div><div class=\"mnemonic-inline-box\"><i class=\"fas fa-brain\"></i> <strong>Memory Mnemonic:</strong> <code>KEY</code> — ...</div>"
    }
  ],
  "comparative_table": {
    "title": "Comprehensive Comparative Matrix & Exam High-Yield Summary",
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
      "explanation": "Authoritative explanation of why this answer is correct and why other options are incorrect."
    }
  ],
  "revision_facts": [
    "High-yield fact 1 with bold terms and specific dates, articles, formulas or names",
    "High-yield fact 2",
    "High-yield fact 3",
    "High-yield fact 4",
    "High-yield fact 5",
    "High-yield fact 6",
    "High-yield fact 7",
    "High-yield fact 8"
  ],
  "mnemonics": [
    {
      "title": "Mnemonic Title 1",
      "acronym": "ACRONYM",
      "expansion": "Explanation of how to remember"
    },
    {
      "title": "Mnemonic Title 2",
      "acronym": "ACRONYM",
      "expansion": "Explanation of how to remember"
    }
  ],
  "exam_traps": [
    "Common trap 1: Detail a frequent confusion or deceptive question pattern where students lose -1 marks.",
    "Common trap 2: Subtly similar concepts or overlapping terms.",
    "Common trap 3: Numerical or chronological trap.",
    "Common trap 4: Exceptions or boundary conditions."
  ],
  "checklist_items": [
    "I have thoroughly reviewed all pointwise concepts and definitions of this topic.",
    "I can recall the mnemonics, tips, and shortcut tricks without hesitation.",
    "I have mastered the comparative distinctions and Uttar Pradesh-specific applications.",
    "I scored 8+ in the practice MCQs and timed mini test without negative marking traps."
  ]
}

CRITICAL RULES:
1. Provide EXACTLY 10 MCQs in the "mcqs" array.
2. In "options", DO NOT prepend letter tags like "(A)", "A.", "A)".
3. ZERO paragraphs in concepts. Everything MUST be in .point-card, .tip-box, .trick-box, .mnemonic-inline-box, or .topic-subtable.`;
}

// 4. Specialized Current Affairs Placeholder Renderer
function renderCurrentAffairsPlaceholderPage(topic, prevTopic, nextTopic) {
  const canonicalUrl = `${DOMAIN}${topic.href}`;
  const pageTitle = `${esc(topic.nameEn)} | UP Teacher General Knowledge | SJMaths`;
  const metaDesc = `Monthly Current Affairs, Global Summits, Bilateral Relations & Awards roadmap for UP Upper Primary Assistant Teacher Recruitment Exam 2026.`;

  const prevLinkHtml = prevTopic
    ? `<a href="${prevTopic.href}" class="topic-nav-btn prev-btn"><i class="fas fa-chevron-left"></i> <span>Previous: ${esc(prevTopic.nameEn.slice(0, 32))}...</span></a>`
    : `<div class="topic-nav-btn disabled"><i class="fas fa-chevron-left"></i> <span>First Topic</span></div>`;

  const nextLinkHtml = nextTopic
    ? `<a href="${nextTopic.href}" class="topic-nav-btn next-btn"><span>Next: ${esc(nextTopic.nameEn.slice(0, 32))}...</span> <i class="fas fa-chevron-right"></i></a>`
    : `<a href="/up-upper-primary-teacher/general-knowledge/" class="topic-nav-btn next-btn"><span>Back to GK Hub</span> <i class="fas fa-arrow-up"></i></a>`;

  return `<!DOCTYPE html>
<html lang="en">
<head>
<script async="" crossorigin="anonymous" src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7924751316191829"></script>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>${pageTitle}</title>
<meta content="${esc(topic.nameEn)}, ${esc(topic.nameHi)}, UP Upper Primary Teacher Current Affairs, Super TET Junior, SJMaths" name="keywords"/>
<meta content="SJMaths" name="author"/>
<meta content="${metaDesc}" name="description"/>
<meta content="index, follow, max-image-preview:large" name="robots"/>
<link href="${canonicalUrl}" rel="canonical"/>
<link href="/favicon.png" rel="icon" type="image/png"/>

<!-- Open Graph -->
<meta property="og:title" content="${pageTitle}">
<meta content="${metaDesc}" property="og:description"/>
<meta content="article" property="og:type"/>
<meta content="${canonicalUrl}" property="og:url"/>
<meta content="${DOMAIN}/assets/icons/icon-512x512.png" property="og:image"/>

<!-- Twitter Card -->
<meta content="summary_large_image" name="twitter:card"/>
<meta name="twitter:title" content="${pageTitle}">
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
            <a href="/up-upper-primary-teacher/general-knowledge/">General Knowledge</a>
            <i class="fas fa-chevron-right" style="font-size: 0.7rem;"></i>
            <span>#5.1</span>
        </div>
        <a href="/up-upper-primary-teacher/general-knowledge/" class="back-hub-btn">
            <i class="fas fa-arrow-left"></i>
            <span>Back to GK Hub</span>
        </a>
    </div>

    <!-- Topic Hero Panel -->
    <div class="topic-hero-panel">
        <div class="topic-meta-row" style="display: flex; gap: 0.75rem; align-items: center; margin-bottom: 1rem; flex-wrap: wrap;">
            <span class="topic-badge-pill">#5.1 Compulsory</span>
            <span class="subject-tag-pill">Module 5: Current Events, Ecology &amp; General Science</span>
            <span class="subject-tag-pill">Current Affairs</span>
        </div>
        <h1>National &amp; International Current Affairs, Global Summits &amp; Awards</h1>
        <div class="topic-hero-subtitle">राष्ट्रीय एवं अन्तर्राष्ट्रीय महत्व की समसामयिक घटनाएं, वैश्विक सम्मेलन एवं पुरस्कार</div>
        <p style="color: var(--text-sub); margin: 0; line-height: 1.65;">Dynamic section covering high-yield events of national and international importance, bilateral accords, global summits (G20, BRICS, SCO), major sports milestones, prestigious awards, science &amp; defense missions, and Uttar Pradesh state developments.</p>
    </div>

    <!-- Coming Soon Banner -->
    <div class="coming-soon-banner">
        <div class="coming-soon-icon"><i class="fas fa-satellite-dish"></i></div>
        <div class="status-badge-live"><i class="fas fa-circle-dot" style="color: #10b981;"></i> Dynamic Section — Rolling Monthly Updates</div>
        <h2 class="coming-soon-title" style="margin-top: 1rem;">Current Affairs Section Coming Soon</h2>
        <p class="coming-soon-desc">
            To ensure maximum score accuracy and avoid obsolete facts, Current Affairs notes for the UP Upper Primary Assistant Teacher Exam 2026 are released as <strong>curated monthly capsules covering January 2025 up to the examination month</strong>. Complete monthly PDF roundups, pointwise MCQs, and timed mini tests will be made live closer to the exam schedule.
        </p>
    </div>

    <!-- 6-Pillar Syllabus Blueprint -->
    <div class="prep-card">
        <h2>
            <i class="fas fa-sitemap" style="color: var(--brand-emerald);"></i>
            <span>6-Pillar Strategic Syllabus Blueprint (Upcoming Coverage)</span>
        </h2>
        <div class="point-grid">
            <div class="point-card">
                <strong>Pillar 1: National Events &amp; Initiatives:</strong> Major policy rollouts by the Government of India, new national infrastructure milestones, educational policies, and constitutional appointments.
            </div>
            <div class="point-card">
                <strong>Pillar 2: International Summits &amp; Bilateral Accords:</strong> G20, BRICS, SCO, ASEAN, BIMSTEC, UN Climate Summits (COP), bilateral treaties signed by India, and international heads of state visits.
            </div>
            <div class="point-card">
                <strong>Pillar 3: Sports, Honours &amp; Prestigious Awards:</strong> Bharat Ratna, Padma Awards (Vibhushan, Bhushan, Shri), Sahitya Akademi, Nobel Prizes, Olympic/Paralympic medals, and National Sports Awards (Khel Ratna, Arjuna).
            </div>
            <div class="point-card">
                <strong>Pillar 4: Science, Space &amp; Defense Technology:</strong> ISRO space exploration missions (Gaganyaan, Chandrayaan, Aditya-L1), DRDO missile tests, joint military exercises with partner nations, and AI/supercomputing initiatives.
            </div>
            <div class="point-card">
                <strong>Pillar 5: Uttar Pradesh Special Current Affairs (2025–2026):</strong> UP Global Investors Summit outcomes, new expressways (Ganga Expressway, Bundelkhand extensions), ODOP scheme updates, and state welfare missions.
            </div>
            <div class="point-card">
                <strong>Pillar 6: Union &amp; Uttar Pradesh Budget Key Metrics:</strong> Fiscal deficit targets, key budgetary allocations for primary education, social welfare, agricultural subsidies, and Economic Survey takeaways.
            </div>
        </div>
    </div>

    <!-- Static GK Foundations to Prepare Now -->
    <div class="prep-card">
        <h2>
            <i class="fas fa-compass" style="color: var(--brand-emerald);"></i>
            <span>Static GK Foundations to Master First</span>
        </h2>
        <div class="topic-subtable-wrapper">
            <table class="topic-subtable">
                <thead>
                    <tr>
                        <th>Static Dimension</th>
                        <th>Core Foundation to Master</th>
                        <th>Current Affairs Linkage</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>International Organizations</strong></td>
                        <td>Headquarters, founding years, and member lists of UN, IMF, World Bank, WTO, WHO, BRICS.</td>
                        <td>Summits, new member admissions, and annual global indices (HDI, Happiness, Hunger).</td>
                    </tr>
                    <tr>
                        <td><strong>Indian Polity &amp; Governance</strong></td>
                        <td>Articles relating to President, Governor, Election Commission, and Constitutional Amendments.</td>
                        <td>Recent bills, judicial rulings, and election-related notifications.</td>
                    </tr>
                    <tr>
                        <td><strong>Environment &amp; Ecology</strong></td>
                        <td>Ramsar convention, Tiger reserves, National Parks, and Biodiversity hotspots.</td>
                        <td>Newly declared Ramsar sites in UP, COP summit resolutions, and forest survey updates.</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class="tip-box">
            💡 <strong>Smart Preparation Tip:</strong> Do not waste time memorizing daily political news. Focus exclusively on institutional decisions, international treaties, sports championships, awards, and Uttar Pradesh government initiatives.
        </div>
    </div>

    <!-- Bottom Sequential Navigation -->
    <div class="bottom-topic-nav">
        ${prevLinkHtml}
        ${nextLinkHtml}
    </div>

</main>

<div id="footer-container"></div>
<script data-cfasync="false" defer="" src="/assets/js/up-upper-primary-topic.min.js"></script>
<script src="/assets/js/common.min.js?v=a3faaea0"></script>
</body>
</html>`;
}

// 4. HTML Page Renderer for General Knowledge Topic
function renderTopicPage(topic, data, prevTopic, nextTopic) {
  const canonicalUrl = `${DOMAIN}${topic.href}`;
  const pageTitle = `${esc(topic.nameEn)} | UP Teacher General Knowledge | SJMaths`;
  const metaDesc = `Exhaustive study notes, concepts, 10 practice MCQs, timed mini test, and revision traps for ${esc(topic.nameEn)} (Part 1 Compulsory General Knowledge) for UP Upper Primary Assistant Teacher Exam 2026.`;

  // Render Concepts
  let conceptsHtml = '';
  (data.concepts || []).forEach(c => {
    conceptsHtml += `
        <div class="prep-card">
            <h2>
                <i class="fas fa-bookmark" style="color: var(--brand-emerald);"></i>
                <span>${esc((c.heading || "").replace(/\s*\(Pointwise Breakdown\)/gi, ""))}</span>
            </h2>
            <div class="topic-content-body">
                ${c.html_content}
            </div>
        </div>`;
  });

  // Render Comparative Table
  let compTableHtml = '';
  if (data.comparative_table && data.comparative_table.headers && data.comparative_table.rows) {
    let ths = data.comparative_table.headers.map(h => `<th>${esc(h)}</th>`).join('');
    let trs = data.comparative_table.rows.map(row => {
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
                <span>${esc(data.comparative_table.title || 'Comparative Matrix & Examination Analysis')}</span>
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

  // Clean MCQ Option Prefix
  function cleanOptionText(opt) {
    if (!opt) return '';
    return String(opt).replace(/^(\([A-D]\)|\[[A-D]\]|[A-D][\).:-]|[A-D]\s*[-–—]\s*|[A-D]\s+)\s*/i, '').trim();
  }

  // Render Practice Questions
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
                <span class="mcq-exam-pill"><i class="fas fa-graduation-cap"></i> Super TET Junior Compulsory</span>
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
  let factsHtml = '';
  (data.revision_facts || []).forEach((fact, fIdx) => {
    factsHtml += `
        <div class="revision-fact-row">
            <span class="fact-num-badge">#${fIdx + 1}</span>
            <div class="fact-text-col">${fact}</div>
        </div>`;
  });

  // Render Mnemonics
  let mnemonicsHtml = '';
  (data.mnemonics || []).forEach(m => {
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
  });

  // Render Negative Marking Traps
  let trapsHtml = '';
  (data.exam_traps || []).forEach((trap, tIdx) => {
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
  let checklistHtml = '';
  (data.checklist_items || []).forEach((item, cIdx) => {
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
    : `<a href="/up-upper-primary-teacher/general-knowledge/" class="topic-nav-btn next-btn"><span>Back to GK Hub</span> <i class="fas fa-arrow-up"></i></a>`;

  // Mini Test JSON Data
  const miniTestDataJson = JSON.stringify(data.mcqs || []);

  return `<!DOCTYPE html>
<html lang="en">
<head>
<script async="" crossorigin="anonymous" src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7924751316191829"></script>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>${pageTitle}</title>
<meta content="${esc(topic.nameEn)}, ${esc(topic.nameHi)}, UP Upper Primary Teacher GK, Part 1 Compulsory, Super TET Junior, SJMaths" name="keywords"/>
<meta content="SJMaths" name="author"/>
<meta content="${metaDesc}" name="description"/>
<meta content="index, follow, max-image-preview:large" name="robots"/>
<link href="${canonicalUrl}" rel="canonical"/>
<link href="/favicon.png" rel="icon" type="image/png"/>

<!-- Open Graph -->
<meta property="og:title" content="${pageTitle}">
<meta content="${metaDesc}" property="og:description"/>
<meta content="article" property="og:type"/>
<meta content="${canonicalUrl}" property="og:url"/>
<meta content="${DOMAIN}/assets/icons/icon-512x512.png" property="og:image"/>

<!-- Twitter Card -->
<meta content="summary_large_image" name="twitter:card"/>
<meta name="twitter:title" content="${pageTitle}">
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
      "name": "General Knowledge",
      "item": "${DOMAIN}/up-upper-primary-teacher/general-knowledge/"
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
            <a href="/up-upper-primary-teacher/general-knowledge/">General Knowledge</a>
            <i class="fas fa-chevron-right" style="font-size: 0.7rem;"></i>
            <span>${esc(topic.numStr)}</span>
        </div>
        <a href="/up-upper-primary-teacher/general-knowledge/" class="back-hub-btn">
            <i class="fas fa-arrow-left"></i>
            <span>Back to GK Hub</span>
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
        <p class="lead-desc">${esc(data.key_focus_summary || 'Comprehensive micro-topic curriculum study notes, comparative analysis, and practice material for UP Upper Primary Assistant Teacher Exam.')}</p>
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
                <p class="test-desc">Simulate the real UP Upper Primary Teacher Part 1 exam environment with this 5-minute timed test containing 10 curated questions. Negative marking (-1 per incorrect answer) is enabled.</p>
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
                <span>High-Yield Revision Points</span>
            </h2>
            <div class="revision-facts-grid">
                ${factsHtml}
            </div>
        </div>

        <div class="prep-card">
            <h2>
                <i class="fas fa-brain" style="color: var(--brand-indigo);"></i>
                <span>Memory Mnemonics</span>
            </h2>
            <div style="display: grid; gap: 1rem;">
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
                <i class="fas fa-square-check" style="color: var(--brand-emerald);"></i>
                <span>Topic Mastery Checklist</span>
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

<button aria-label="Back to Top" class="back-to-top" id="backToTop">
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

// 5. Robust Atomic Writing with Retries on Windows
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

// 6. Gemini Generation Call with Retries and Key Rotation
async function callGemini(topic, attempt = 1) {
  const prompt = buildPrompt(topic);
  const { client, keyName } = getAIClient();

  try {
    const response = await client.models.generateContent({
      model: MODEL_NAME,
      contents: prompt,
      config: {
        temperature: 0.3,
        responseMimeType: 'application/json',
      }
    });

    let rawText = response.text ? response.text.trim() : '';
    if (!rawText) {
      throw new Error('Empty response from model');
    }

    if (rawText.startsWith('```')) {
      rawText = rawText.replace(/^```json\s*/, '').replace(/^```\s*/, '').replace(/\s*```$/, '');
    }

    let parsed;
    try {
      parsed = JSON.parse(rawText);
    } catch {
      const repaired = jsonrepair(rawText);
      parsed = JSON.parse(repaired);
    }

    return parsed;
  } catch (err) {
    console.error(`  [Attempt ${attempt} on ${keyName}] Gemini error: ${err.message}`);
    rotateKey();

    if (attempt < 5) {
      const waitTime = attempt * 2500;
      console.log(`  Waiting ${waitTime / 1000}s before retrying with rotated key...`);
      await new Promise(r => setTimeout(r, waitTime));
      return callGemini(topic, attempt + 1);
    }
    throw err;
  }
}

// 7. Main Pipeline Runner
async function main() {
  console.log('================================================================');
  console.log('  UP Upper Primary Teacher: General Knowledge Notes Generator');
  console.log('  Target: Part 1 Compulsory (30 Questions | 90 Marks)');
  console.log(`  Mode: ${DRY_RUN ? 'DRY-RUN' : 'LIVE GENERATION'} | Model: ${MODEL_NAME}`);
  console.log(`  Keys available: ${API_KEYS.length}`);
  console.log('================================================================\n');

  let topicsToProcess = allTopics.slice();

  if (TARGET_MODULE) {
    const modNum = parseInt(TARGET_MODULE, 10);
    topicsToProcess = topicsToProcess.filter(t => t.secIdx === modNum);
    console.log(`Filtering by Module ${modNum}: ${topicsToProcess.length} topics found`);
  }

  if (TARGET_TOPIC) {
    topicsToProcess = topicsToProcess.filter(t => {
      return t.slug === TARGET_TOPIC ||
             t.href.includes(TARGET_TOPIC) ||
             t.numStr === TARGET_TOPIC;
    });
    console.log(`Filtering by Topic "${TARGET_TOPIC}": ${topicsToProcess.length} topics matched`);
  }

  if (!FORCE && !TARGET_TOPIC) {
    topicsToProcess = topicsToProcess.filter(t => !statusMap[t.slug]?.completed);
    console.log(`Remaining ungenerated topics: ${topicsToProcess.length}`);
  }

  if (LIMIT && LIMIT > 0) {
    topicsToProcess = topicsToProcess.slice(0, LIMIT);
    console.log(`Applying limit: processing next ${topicsToProcess.length} topics`);
  }

  if (topicsToProcess.length === 0) {
    console.log('No topics to process. Use --force to regenerate existing topics.');
    return;
  }

  console.log(`\nStarting pipeline for ${topicsToProcess.length} topics...\n`);

  let successCount = 0;
  let failCount = 0;

  for (let i = 0; i < topicsToProcess.length; i++) {
    const topic = topicsToProcess[i];
    const overallIdx = allTopics.findIndex(t => t.slug === topic.slug);
    const prevTopic = overallIdx > 0 ? allTopics[overallIdx - 1] : null;
    const nextTopic = overallIdx < allTopics.length - 1 ? allTopics[overallIdx + 1] : null;

    const relPath = topic.href.replace(/^\//, '').replace(/\/$/, '');
    const topicDir = path.join(ROOT, relPath.split('/').join(path.sep));
    const targetFile = path.join(topicDir, 'index.html');

    console.log(`[${i + 1}/${topicsToProcess.length}] Topic ${topic.numStr}: ${topic.nameEn} (${topic.slug})`);
    console.log(`  Module: ${topic.secIdx} (${topic.secTitleEn})`);
    console.log(`  Target: ${targetFile}`);

    if (DRY_RUN) {
      console.log('  [DRY-RUN] Verified syllabus entry & target file path.');
      successCount++;
      continue;
    }

    // Special Handling: Current Affairs section placeholder (as requested)
    if (topic.slug === 'current-events-national-international' || (topic.secIdx === 5 && topic.numStr.includes('5.1'))) {
      console.log(`  [Special Handling] Current Affairs section - Generating dedicated Coming Soon placeholder...`);
      if (!fs.existsSync(topicDir)) {
        fs.mkdirSync(topicDir, { recursive: true });
      }
      const renderedHtml = renderCurrentAffairsPlaceholderPage(topic, prevTopic, nextTopic);
      await safeWriteFile(targetFile, renderedHtml);
      const fileSizeKb = (fs.statSync(targetFile).size / 1024).toFixed(1);
      console.log(`  Wrote ${fileSizeKb} KB to ${targetFile}`);

      statusMap[topic.slug] = {
        num: topic.numStr,
        nameEn: topic.nameEn,
        nameHi: topic.nameHi,
        module: topic.secIdx,
        completed: true,
        placeholder: true,
        fileSizeKb,
        updatedAt: new Date().toISOString(),
      };
      saveStatus();
      successCount++;
      continue;
    }

    try {
      console.log(`  Generating comprehensive English notes via ${MODEL_NAME}...`);
      const startTime = Date.now();
      const generatedData = await callGemini(topic);
      const elapsed = ((Date.now() - startTime) / 1000).toFixed(1);
      console.log(`  Generated successfully in ${elapsed}s (MCQs: ${generatedData.mcqs?.length || 0}, Concepts: ${generatedData.concepts?.length || 0})`);

      if (!fs.existsSync(topicDir)) {
        fs.mkdirSync(topicDir, { recursive: true });
      }

      const renderedHtml = renderTopicPage(topic, generatedData, prevTopic, nextTopic);

      await safeWriteFile(targetFile, renderedHtml);
      const fileSizeKb = (fs.statSync(targetFile).size / 1024).toFixed(1);
      console.log(`  Wrote ${fileSizeKb} KB to ${targetFile}`);

      statusMap[topic.slug] = {
        num: topic.numStr,
        nameEn: topic.nameEn,
        nameHi: topic.nameHi,
        module: topic.secIdx,
        completed: true,
        fileSizeKb,
        mcqCount: generatedData.mcqs?.length || 0,
        updatedAt: new Date().toISOString(),
      };
      saveStatus();
      successCount++;

      if (i < topicsToProcess.length - 1) {
        await new Promise(r => setTimeout(r, 1200));
      }
    } catch (err) {
      console.error(`  ERROR processing topic ${topic.numStr}: ${err.message}`);
      failCount++;
    }
  }

  console.log('\n================================================================');
  console.log(`  Pipeline Complete: ${successCount} Succeeded, ${failCount} Failed.`);
  console.log(`  Status tracking updated: ${STATUS_FILE}`);
  console.log('================================================================\n');
}

main().catch(err => {
  console.error('Fatal error in generator script:', err);
  process.exit(1);
});
