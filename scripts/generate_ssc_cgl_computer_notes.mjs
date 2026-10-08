#!/usr/bin/env node
/**
 * Generate Comprehensive Bilingual Study Notes (Tab 1: Concepts & Theory)
 * for SSC CGL Computer Knowledge Topics.
 *
 * Uses Gemini API (gemini-3.5-flash-lite) to generate in-depth, curriculum-aligned,
 * exam-targeted study notes tailored specifically for SSC CGL Tier-2 Computer Proficiency.
 *
 * Usage:
 *   node scripts/generate_ssc_cgl_computer_notes.mjs
 *   node scripts/generate_ssc_cgl_computer_notes.mjs --topic backup-devices
 *   node scripts/generate_ssc_cgl_computer_notes.mjs --limit 1
 *   node scripts/generate_ssc_cgl_computer_notes.mjs --dry-run
 *   node scripts/generate_ssc_cgl_computer_notes.mjs --force
 */

import fs from 'node:fs';
import path from 'node:path';
import 'dotenv/config';
import { GoogleGenAI } from '@google/genai';
import { jsonrepair } from 'jsonrepair';

const ROOT_DIR = process.cwd();
const COMPUTER_DIR = path.join(ROOT_DIR, 'ssc-cgl', 'computer-knowledge');
const STATUS_FILE = path.join(ROOT_DIR, 'ssc-cgl-computer-status.json');

// CLI Arguments parsing
function parseCliArgs(args) {
  const flags = {};
  const positionals = [];
  for (let i = 0; i < args.length; i++) {
    const arg = args[i];
    if (arg.startsWith('--')) {
      if (arg.includes('=')) {
        const [k, ...v] = arg.slice(2).split('=');
        flags[k] = v.join('=');
      } else {
        const next = args[i + 1];
        if (next !== undefined && !next.startsWith('--')) {
          flags[arg.slice(2)] = next;
          i++;
        } else {
          flags[arg.slice(2)] = true;
        }
      }
    } else {
      positionals.push(arg);
    }
  }
  return { flags, positionals };
}

const { flags } = parseCliArgs(process.argv.slice(2));

const TARGET_MODEL = flags.model || process.env.GEMINI_MODEL || 'gemini-3.5-flash-lite';
const LIMIT = flags.limit ? parseInt(flags.limit, 10) : 0;
const TOPIC_FILTER = flags.topic || null;
const FORCE = Boolean(flags.force);
const DRY_RUN = Boolean(flags['dry-run']);
const GAP_MS = (parseInt(flags.gap || '1', 10)) * 1000;
const MAX_ATTEMPTS = parseInt(flags.attempts || '3', 10);

// API Keys setup with rotation
const apiKeys = [
  process.env.GEMINI_API_KEY,
  process.env.GEMINI_API_KEY_1,
  process.env.GEMINI_API_KEY_2,
  process.env.GOOGLE_API_KEY
].filter(Boolean);

if (apiKeys.length === 0) {
  console.error('❌ Error: No Gemini API Key found in .env');
  process.exit(1);
}

let currentKeyIndex = 0;
function getGenAIClient() {
  const apiKey = apiKeys[currentKeyIndex % apiKeys.length];
  return new GoogleGenAI({ apiKey });
}

function rotateApiKey() {
  if (apiKeys.length > 1) {
    currentKeyIndex = (currentKeyIndex + 1) % apiKeys.length;
    console.log(`🔄 Rotated to Gemini API key #${currentKeyIndex + 1}`);
  }
}

// Status file handling
function readStatus() {
  if (fs.existsSync(STATUS_FILE)) {
    try {
      return JSON.parse(fs.readFileSync(STATUS_FILE, 'utf8'));
    } catch {
      return {};
    }
  }
  return {};
}

function writeStatus(status) {
  try {
    fs.writeFileSync(STATUS_FILE, JSON.stringify(status, null, 2), 'utf8');
  } catch (err) {
    console.warn('Warning: Could not save status file:', err.message);
  }
}

// Discover all 17 computer knowledge topic directories
function getTopicDirs() {
  if (!fs.existsSync(COMPUTER_DIR)) return [];
  const entries = fs.readdirSync(COMPUTER_DIR, { withFileTypes: true });
  return entries
    .filter(e => e.isDirectory())
    .map(e => ({
      slug: e.name,
      dirPath: path.join(COMPUTER_DIR, e.name),
      htmlPath: path.join(COMPUTER_DIR, e.name, 'index.html')
    }))
    .filter(t => fs.existsSync(t.htmlPath));
}

// Extract human topic title from index.html
function getTopicTitle(htmlPath) {
  try {
    const content = fs.readFileSync(htmlPath, 'utf8');
    const h1Match = content.match(/<h1[^>]*>([\s\S]*?)<\/h1>/i);
    if (h1Match) {
      return h1Match[1].replace(/<[^>]+>/g, '').trim();
    }
  } catch {}
  return path.basename(path.dirname(htmlPath)).replace(/-/g, ' ');
}

// Build generation prompt for Gemini
function buildPrompt(topicTitle, slug) {
  return `You are a premier senior computer science educator and exam question setter for SSC CGL Tier 2 (Computer Proficiency / Computer Knowledge Module).

TOPIC: "${topicTitle}" (Slug: ${slug})
EXAM CONTEXT: SSC CGL Tier-2 Computer Knowledge is a qualifying but mandatory 60-mark section (20 questions, 3 marks each, 1 negative mark). Questions test practical concepts, protocols, technical specifications, keyboard shortcuts, hardware architectures, security threats, and MS Office nuances.

TASK:
Generate comprehensive, authentic, high-yield bilingual (English and Hindi) Study Notes & Theory for this topic.

REQUIREMENTS:
1. STRICT BILINGUAL FORMAT:
   Every single title, paragraph, bullet point, table cell, and callout MUST be in both English ("en") and standardized Hindi ("hi") using standard official examination terminology.

2. STRUCTURED SECTIONS:
   - "overview": Concise summary explaining what the topic is, why it matters, and how SSC CGL tests it.
   - "learningObjectives": 4-5 focused learning targets for SSC CGL aspirants.
   - "conceptIntro": Foundational explanation with real-world analogies.
   - "coreSections": 3 to 4 detailed technical sections breaking down every essential sub-concept, component, protocol, architecture, or mechanism. Include structured subpoints with labels and explanations.
   - "comparisonTable": A high-yield reference comparison table (e.g. types, speeds, ports, protocols, or differences) with title, 3-4 headers, and 4-6 rows of exact facts.
   - "callouts": 3 to 4 strategic exam callouts:
     * "exam-tip": Past SSC CGL question patterns & high-yield areas.
     * "remember-this": Memory aids, golden rules, or acronyms.
     * "common-mistake": Subtle confusions or traps students often make.
   - "keyTakeaways": 5 to 7 bullet points summarizing critical facts for rapid pre-exam revision.

OUTPUT FORMAT:
Return strictly a valid JSON object matching this schema without any preamble, markdown code blocks, or extra text:

{
  "topicTitle": { "en": "...", "hi": "..." },
  "overview": { "en": "...", "hi": "..." },
  "learningObjectives": [
    { "en": "...", "hi": "..." }
  ],
  "conceptIntro": { "en": "...", "hi": "..." },
  "coreSections": [
    {
      "heading": { "en": "...", "hi": "..." },
      "paragraphs": [
        { "en": "...", "hi": "..." }
      ],
      "bulletPoints": [
        {
          "label": { "en": "...", "hi": "..." },
          "detail": { "en": "...", "hi": "..." }
        }
      ]
    }
  ],
  "comparisonTable": {
    "title": { "en": "...", "hi": "..." },
    "headers": [
      { "en": "...", "hi": "..." }
    ],
    "rows": [
      [
        { "en": "...", "hi": "..." }
      ]
    ]
  },
  "callouts": [
    {
      "type": "exam-tip",
      "title": { "en": "...", "hi": "..." },
      "text": { "en": "...", "hi": "..." }
    },
    {
      "type": "remember-this",
      "title": { "en": "...", "hi": "..." },
      "text": { "en": "...", "hi": "..." }
    },
    {
      "type": "common-mistake",
      "title": { "en": "...", "hi": "..." },
      "text": { "en": "...", "hi": "..." }
    }
  ],
  "keyTakeaways": [
    { "en": "...", "hi": "..." }
  ]
}`;
}

// Convert generated JSON into accessible, responsive HTML
function renderTheoryHtml(data) {
  let html = `<div class="theory-content-wrapper">
    <div class="theory-section-header">
        <h2><span class="lang-en">${escapeHtml(data.topicTitle.en)}: Complete Study Notes</span><span class="lang-hi">${escapeHtml(data.topicTitle.hi)}: संपूर्ण अध्ययन नोट्स</span></h2>
    </div>

    <!-- Quick Overview -->
    <div class="theory-block">
        <h3 class="theory-subheading"><i class="fas fa-info-circle"></i> <span class="lang-en">Quick Overview</span><span class="lang-hi">त्वरित अवलोकन</span></h3>
        <p class="lang-en">${escapeHtml(data.overview.en)}</p>
        <p class="lang-hi">${escapeHtml(data.overview.hi)}</p>
    </div>

    <!-- Learning Objectives -->
    <div class="theory-block">
        <h3 class="theory-subheading"><i class="fas fa-bullseye"></i> <span class="lang-en">Learning Objectives for SSC CGL</span><span class="lang-hi">एसएससी सीजीएल के लिए अध्ययन उद्देश्य</span></h3>
        <ul class="learning-list">
`;

  data.learningObjectives.forEach(obj => {
    html += `            <li><span class="lang-en">${escapeHtml(obj.en)}</span><span class="lang-hi">${escapeHtml(obj.hi)}</span></li>\n`;
  });

  html += `        </ul>
    </div>

    <!-- Concept Introduction -->
    <div class="theory-block">
        <h3 class="theory-subheading"><i class="fas fa-lightbulb"></i> <span class="lang-en">Concept Introduction</span><span class="lang-hi">मूल अवधारणा परिचय</span></h3>
        <p class="lang-en">${escapeHtml(data.conceptIntro.en)}</p>
        <p class="lang-hi">${escapeHtml(data.conceptIntro.hi)}</p>
    </div>
`;

  // Core Technical Sections
  if (Array.isArray(data.coreSections)) {
    data.coreSections.forEach((sec, idx) => {
      html += `    <!-- Core Section ${idx + 1} -->
    <div class="theory-block">
        <h3 class="theory-subheading"><i class="fas fa-layer-group"></i> <span class="lang-en">${escapeHtml(sec.heading.en)}</span><span class="lang-hi">${escapeHtml(sec.heading.hi)}</span></h3>
`;
      if (Array.isArray(sec.paragraphs)) {
        sec.paragraphs.forEach(p => {
          html += `        <p class="lang-en">${escapeHtml(p.en)}</p>\n        <p class="lang-hi">${escapeHtml(p.hi)}</p>\n`;
        });
      }
      if (Array.isArray(sec.bulletPoints) && sec.bulletPoints.length > 0) {
        html += `        <div class="feature-bullet-grid">\n`;
        sec.bulletPoints.forEach(bp => {
          html += `            <div class="feature-bullet-item">
                <div class="bullet-tag"><strong><span class="lang-en">${escapeHtml(bp.label.en)}</span><span class="lang-hi">${escapeHtml(bp.label.hi)}</span></strong></div>
                <div class="bullet-desc"><span class="lang-en">${escapeHtml(bp.detail.en)}</span><span class="lang-hi">${escapeHtml(bp.detail.hi)}</span></div>
            </div>\n`;
        });
        html += `        </div>\n`;
      }
      html += `    </div>\n`;
    });
  }

  // Comparison Table
  if (data.comparisonTable && Array.isArray(data.comparisonTable.headers) && Array.isArray(data.comparisonTable.rows)) {
    html += `    <!-- Reference Comparison Table -->
    <div class="theory-block">
        <h3 class="theory-subheading"><i class="fas fa-table"></i> <span class="lang-en">${escapeHtml(data.comparisonTable.title.en)}</span><span class="lang-hi">${escapeHtml(data.comparisonTable.title.hi)}</span></h3>
        <div class="premium-table-container">
            <table class="premium-table">
                <thead>
                    <tr>
`;
    data.comparisonTable.headers.forEach(h => {
      html += `                        <th><span class="lang-en">${escapeHtml(h.en)}</span><span class="lang-hi">${escapeHtml(h.hi)}</span></th>\n`;
    });
    html += `                    </tr>
                </thead>
                <tbody>
`;
    data.comparisonTable.rows.forEach(row => {
      html += `                    <tr>\n`;
      row.forEach(cell => {
        html += `                        <td><span class="lang-en">${escapeHtml(cell.en)}</span><span class="lang-hi">${escapeHtml(cell.hi)}</span></td>\n`;
      });
      html += `                    </tr>\n`;
    });
    html += `                </tbody>
            </table>
        </div>
    </div>
`;
  }

  // Callouts
  if (Array.isArray(data.callouts)) {
    data.callouts.forEach(c => {
      const calloutClass = c.type === 'remember-this' ? 'remember-this' : (c.type === 'common-mistake' ? 'common-mistake' : 'exam-tip');
      const defaultIcon = c.type === 'remember-this' ? 'fa-bookmark' : (c.type === 'common-mistake' ? 'fa-exclamation-triangle' : 'fa-lightbulb');
      html += `    <div class="${calloutClass}">
        <p><strong><i class="fas ${defaultIcon}"></i> <span class="lang-en">${escapeHtml(c.title?.en || 'Exam Note')}:</span><span class="lang-hi">${escapeHtml(c.title?.hi || 'परीक्षा ध्यान दें')}:</span></strong>
        <span class="lang-en">${escapeHtml(c.text.en)}</span>
        <span class="lang-hi">${escapeHtml(c.text.hi)}</span></p>
    </div>\n`;
    });
  }

  // Key Takeaways
  if (Array.isArray(data.keyTakeaways) && data.keyTakeaways.length > 0) {
    html += `    <!-- Key Takeaways & Exam Checklist -->
    <div class="theory-block takeaways-block">
        <h3 class="theory-subheading"><i class="fas fa-clipboard-check"></i> <span class="lang-en">Key Takeaways (High-Yield Summary)</span><span class="lang-hi">मुख्य निष्कर्ष (त्वरित पुनरीक्षण)</span></h3>
        <ul class="takeaway-list">
`;
    data.keyTakeaways.forEach(tk => {
      html += `            <li><i class="fas fa-check-circle" style="color: #10b981; margin-right: 0.5rem;"></i><span class="lang-en">${escapeHtml(tk.en)}</span><span class="lang-hi">${escapeHtml(tk.hi)}</span></li>\n`;
    });
    html += `        </ul>
    </div>
</div>`;
  }

  return html;
}

function escapeHtml(str) {
  if (!str) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

// Generate the complete tabbed structure to inject into index.html
function generateTabbedHtml(theoryHtml) {
  return `<!-- 4-Tab Navigation Bar -->
<div class="main-tabs-nav" role="tablist">
<button class="tab-btn active" onclick="openTab(event, 'tab-theory')" role="tab">
<i class="fas fa-book-open"></i> <span class="lang-en">1. Concepts &amp; Theory</span><span class="lang-hi">1. अवधारणाएं और सिद्धांत</span>
</button>
<button class="tab-btn" onclick="openTab(event, 'tab-practice')" role="tab">
<i class="fas fa-tasks"></i> <span class="lang-en">2. Practice Questions</span><span class="lang-hi">2. अभ्यास प्रश्न</span>
</button>
<button class="tab-btn" onclick="openTab(event, 'tab-pyqs')" role="tab">
<i class="fas fa-history"></i> <span class="lang-en">3. Previous Year Questions</span><span class="lang-hi">3. पिछले वर्ष के प्रश्न</span>
</button>
<button class="tab-btn" onclick="openTab(event, 'tab-mini-test')" role="tab">
<i class="fas fa-stopwatch"></i> <span class="lang-en">4. Mini Test</span><span class="lang-hi">4. मिनी टेस्ट</span>
</button>
</div>

<!-- Tab 1: Concepts & Theory (Fully Populated) -->
<div class="tab-panel active" id="tab-theory" role="tabpanel">
${theoryHtml}
</div>

<!-- Tab 2: Practice Questions (Coming Soon Placeholder) -->
<div class="tab-panel" id="tab-practice" role="tabpanel">
<div class="tab-placeholder-card">
    <i class="fas fa-tasks placeholder-icon"></i>
    <h3><span class="lang-en">Practice Questions</span><span class="lang-hi">अभ्यास प्रश्न</span></h3>
    <p><span class="lang-en">Exam-standard 3-level practice MCQs (Easy, Medium, Hard) tailored to the SSC CGL Tier-2 computer pattern are currently being prepared. Master the Concepts &amp; Theory tab to prepare!</span><span class="lang-hi">SSC CGL टियर-2 कंप्यूटर पैटर्न के अनुसार 3-स्तरीय अभ्यास प्रश्न (सरल, मध्यम, कठिन) जल्द उपलब्ध होंगे। तैयारी के लिए अवधारणाएं और सिद्धांत टैब का अध्ययन करें!</span></p>
</div>
</div>

<!-- Tab 3: Previous Year Questions (Coming Soon Placeholder) -->
<div class="tab-panel" id="tab-pyqs" role="tabpanel">
<div class="tab-placeholder-card">
    <i class="fas fa-history placeholder-icon"></i>
    <h3><span class="lang-en">Previous Year Questions (PYQs)</span><span class="lang-hi">पिछले वर्ष के प्रश्न</span></h3>
    <p><span class="lang-en">Curated SSC CGL Tier-2 (2022–2024) previous year questions for this topic with step-by-step explanations will be indexed here.</span><span class="lang-hi">विस्तृत स्पष्टीकरण के साथ इस विषय के SSC CGL टियर-2 (2022-2024) के पिछले वर्षों के प्रश्न यहाँ उपलब्ध होंगे।</span></p>
</div>
</div>

<!-- Tab 4: Mini Test (Coming Soon Placeholder) -->
<div class="tab-panel" id="tab-mini-test" role="tabpanel">
<div class="tab-placeholder-card">
    <i class="fas fa-stopwatch placeholder-icon"></i>
    <h3><span class="lang-en">Topic Mini Test</span><span class="lang-hi">मिनी टेस्ट</span></h3>
    <p><span class="lang-en">A timed evaluation test with instant scoring, negative marking calculation, and performance analysis will unlock once you master the theory.</span><span class="lang-hi">सिद्धांत में महारत हासिल करने के बाद तत्काल स्कोरिंग और प्रदर्शन विश्लेषण के साथ समयबद्ध टेस्ट उपलब्ध होगा।</span></p>
</div>
</div>`;
}

// Injected CSS for modern 4-tab styling and bilingual callouts
const INJECTED_STYLES = `
    /* 4-Tab Navigation & Study Notes Styling */
    .main-tabs-nav {
        display: flex;
        gap: 0.5rem;
        margin-bottom: 1.75rem;
        border-bottom: 2px solid #e2e8f0;
        padding-bottom: 0;
        overflow-x: auto;
        -webkit-overflow-scrolling: touch;
        scrollbar-width: none;
    }
    .main-tabs-nav::-webkit-scrollbar { display: none; }
    .tab-btn {
        background: transparent;
        border: none;
        border-bottom: 3px solid transparent;
        outline: none;
        font-family: 'Outfit', -apple-system, sans-serif;
        font-size: 0.88rem;
        font-weight: 700;
        color: #718096;
        padding: 0.75rem 1rem 0.65rem;
        cursor: pointer;
        border-radius: 8px 8px 0 0;
        transition: all 0.25s ease;
        display: flex;
        align-items: center;
        gap: 0.45rem;
        white-space: nowrap;
        flex-shrink: 0;
    }
    .tab-btn:hover { color: #8e44ad; background: rgba(142, 68, 173, 0.05); }
    .tab-btn.active {
        color: #8e44ad;
        background: rgba(142, 68, 173, 0.06);
        border-bottom-color: #8e44ad;
    }
    .tab-panel {
        display: none;
        background: #ffffff;
        border: 1px solid rgba(0, 0, 0, 0.08);
        border-radius: 1.25rem;
        padding: 2rem 1.75rem;
        box-shadow: 0 10px 30px -5px rgba(0, 0, 0, 0.05);
        animation: upFadeIn 0.35s ease-out;
        line-height: 1.7;
        color: #2d3748;
    }
    .tab-panel.active { display: block; }
    
    /* Bilingual Language Toggle Sync */
    .lang-hi { display: none; }
    body.lang-mode-hi .lang-en, html.lang-hi .lang-en, body.lang-hi .lang-en { display: none !important; }
    body.lang-mode-hi .lang-hi, html.lang-hi .lang-hi, body.lang-hi .lang-hi { display: block !important; }
    body.lang-mode-hi span.lang-hi, html.lang-hi span.lang-hi, body.lang-hi span.lang-hi,
    body.lang-mode-hi strong.lang-hi, html.lang-hi strong.lang-hi, body.lang-hi strong.lang-hi,
    body.lang-mode-hi em.lang-hi, html.lang-hi em.lang-hi, body.lang-hi em.lang-hi { display: inline-block !important; }

    /* Theory Block Styling */
    .theory-section-header h2 {
        font-family: 'Outfit', sans-serif;
        font-size: 1.45rem;
        font-weight: 800;
        color: #8e44ad;
        margin-bottom: 1.25rem;
        border-bottom: 2px solid rgba(142, 68, 173, 0.15);
        padding-bottom: 0.5rem;
    }
    .theory-block { margin-bottom: 2rem; }
    .theory-subheading {
        font-family: 'Outfit', sans-serif;
        font-size: 1.18rem;
        font-weight: 700;
        color: #1a202c;
        margin-bottom: 0.75rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    .theory-subheading i { color: #8e44ad; }
    .learning-list, .takeaway-list {
        padding-left: 1.2rem;
        margin-bottom: 1rem;
    }
    .learning-list li, .takeaway-list li {
        margin-bottom: 0.5rem;
        font-size: 0.95rem;
    }

    /* Bullet feature grid */
    .feature-bullet-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 0.85rem;
        margin-top: 1rem;
    }
    .feature-bullet-item {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        padding: 0.85rem 1rem;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .feature-bullet-item:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        border-color: #cbd5e1;
    }
    .bullet-tag {
        font-size: 0.95rem;
        color: #8e44ad;
        margin-bottom: 0.35rem;
    }
    .bullet-desc { font-size: 0.88rem; color: #475569; line-height: 1.5; }

    /* Tables */
    .premium-table-container {
        width: 100%;
        overflow-x: auto;
        margin: 1.25rem 0;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
        background: #ffffff;
    }
    .premium-table {
        width: 100%;
        border-collapse: collapse;
        font-size: 0.9rem;
    }
    .premium-table th {
        background: rgba(142, 68, 173, 0.08);
        color: #8e44ad;
        font-weight: 700;
        padding: 0.75rem 1rem;
        text-align: left;
        border-bottom: 2px solid #e2e8f0;
    }
    .premium-table td {
        padding: 0.75rem 1rem;
        border-bottom: 1px solid #f1f5f9;
        color: #334155;
    }
    .premium-table tr:last-child td { border-bottom: none; }
    .premium-table tr:hover td { background: #f8fafc; }

    /* Callouts */
    .exam-tip, .remember-this, .common-mistake {
        border-left: 4px solid;
        border-radius: 0 10px 10px 0;
        padding: 1rem 1.25rem;
        margin: 1.25rem 0;
        font-size: 0.92rem;
        line-height: 1.6;
    }
    .exam-tip {
        background: rgba(142, 68, 173, 0.05);
        border-left-color: #8e44ad;
    }
    .remember-this {
        background: rgba(59, 130, 246, 0.05);
        border-left-color: #3b82f6;
    }
    .common-mistake {
        background: rgba(239, 68, 68, 0.05);
        border-left-color: #ef4444;
    }
    .takeaways-block {
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.04), rgba(5, 150, 105, 0.04));
        border: 1px solid rgba(16, 185, 129, 0.2);
        border-radius: 12px;
        padding: 1.25rem;
        margin-top: 1.5rem;
    }

    /* Tab Placeholder Cards */
    .tab-placeholder-card {
        text-align: center;
        padding: 3rem 1.5rem;
        background: rgba(142, 68, 173, 0.03);
        border: 1px dashed rgba(142, 68, 173, 0.2);
        border-radius: 1rem;
        margin: 1rem 0;
    }
    .placeholder-icon {
        font-size: 2.2rem;
        color: #8e44ad;
        margin-bottom: 1rem;
        opacity: 0.8;
    }
    .tab-placeholder-card h3 {
        font-family: 'Outfit', sans-serif;
        font-size: 1.25rem;
        font-weight: 700;
        color: #1a202c;
        margin-bottom: 0.5rem;
    }
    .tab-placeholder-card p {
        color: #64748b;
        font-size: 0.95rem;
        max-width: 580px;
        margin: 0 auto;
        line-height: 1.6;
    }

    /* Dark Mode */
    body.dark-mode .tab-panel {
        background: #1e1e2e;
        border-color: rgba(255, 255, 255, 0.08);
        color: #e2e8f0;
    }
    body.dark-mode .theory-subheading { color: #f1f5f9; }
    body.dark-mode .feature-bullet-item {
        background: #27273a;
        border-color: rgba(255, 255, 255, 0.08);
    }
    body.dark-mode .bullet-desc { color: #cbd5e1; }
    body.dark-mode .premium-table-container {
        background: #1e1e2e;
        border-color: rgba(255, 255, 255, 0.08);
    }
    body.dark-mode .premium-table th {
        background: rgba(167, 139, 250, 0.12);
        color: #c084fc;
        border-bottom-color: rgba(255, 255, 255, 0.1);
    }
    body.dark-mode .premium-table td {
        border-bottom-color: rgba(255, 255, 255, 0.05);
        color: #e2e8f0;
    }
    body.dark-mode .premium-table tr:hover td { background: #27273a; }
    body.dark-mode .tab-placeholder-card {
        background: rgba(167, 139, 250, 0.05);
        border-color: rgba(167, 139, 250, 0.2);
    }
    body.dark-mode .tab-placeholder-card h3 { color: #f1f5f9; }
    body.dark-mode .tab-placeholder-card p { color: #94a3b8; }
`;

// Injected Tab Switcher Script
const INJECTED_TAB_SCRIPT = `
<script>
function openTab(evt, tabId) {
    document.querySelectorAll('.tab-panel').forEach(function(p) { p.classList.remove('active'); });
    document.querySelectorAll('.main-tabs-nav .tab-btn').forEach(function(b) { b.classList.remove('active'); });
    var panel = document.getElementById(tabId);
    if (panel) panel.classList.add('active');
    var btn = evt && evt.currentTarget ? evt.currentTarget : document.querySelector('.main-tabs-nav .tab-btn[onclick*="' + tabId + '"]');
    if (btn) btn.classList.add('active');
}
function normalizeInitialTab() {
    var requested = window.location.hash.replace('#', '');
    var allowed = ['tab-theory', 'tab-practice', 'tab-pyqs', 'tab-mini-test'];
    var defaultTab = allowed.indexOf(requested) !== -1 ? requested : 'tab-theory';
    openTab(null, defaultTab);
}
document.addEventListener('DOMContentLoaded', normalizeInitialTab);
window.addEventListener('pageshow', normalizeInitialTab);
</script>`;

// Main runner
async function main() {
  console.log('======================================================================');
  console.log('🎯 SSC CGL Computer Knowledge: Comprehensive Study Notes Generator');
  console.log(`🤖 Model: ${TARGET_MODEL}`);
  console.log(`🔑 Available API Keys: ${apiKeys.length}`);
  if (DRY_RUN) console.log('🔍 Mode: DRY-RUN (no files will be written)');
  console.log('======================================================================\n');

  const topics = getTopicDirs();
  console.log(`Found ${topics.length} topics in ssc-cgl/computer-knowledge:\n`);

  let targetTopics = topics;
  if (TOPIC_FILTER) {
    targetTopics = topics.filter(t => t.slug.toLowerCase().includes(TOPIC_FILTER.toLowerCase()));
  }
  if (LIMIT > 0) {
    targetTopics = targetTopics.slice(0, LIMIT);
  }

  const status = readStatus();
  let completed = 0;
  let skipped = 0;
  let errors = 0;

  for (let i = 0; i < targetTopics.length; i++) {
    const topic = targetTopics[i];
    const topicTitle = getTopicTitle(topic.htmlPath);
    console.log(`[${i + 1}/${targetTopics.length}] Processing: ${topicTitle} (${topic.slug})`);

    // Check if already populated (unless --force)
    const existingContent = fs.readFileSync(topic.htmlPath, 'utf8');
    const isPlaceholder = existingContent.includes('Coming Soon');
    if (!FORCE && !isPlaceholder && status[topic.slug]?.status === 'completed') {
      console.log(`   ✅ [Already Populated] Skipping.\n`);
      skipped++;
      continue;
    }

    if (DRY_RUN) {
      console.log(`   [DRY-RUN] Would generate study notes for "${topicTitle}"\n`);
      completed++;
      continue;
    }

    let success = false;
    for (let attempt = 1; attempt <= MAX_ATTEMPTS; attempt++) {
      try {
        const client = getGenAIClient();
        const prompt = buildPrompt(topicTitle, topic.slug);

        const response = await client.models.generateContent({
          model: TARGET_MODEL,
          contents: prompt,
          config: {
            temperature: 0.3,
            responseMimeType: 'application/json'
          }
        });

        const rawText = response.text || '';
        let parsed;
        try {
          parsed = JSON.parse(rawText);
        } catch {
          const repaired = jsonrepair(rawText);
          parsed = JSON.parse(repaired);
        }

        if (!parsed.topicTitle || !parsed.overview || !parsed.learningObjectives) {
          throw new Error('Generated JSON missing required fields');
        }

        // Render HTML
        const theoryHtml = renderTheoryHtml(parsed);
        const tabsHtml = generateTabbedHtml(theoryHtml);

        // Update topic index.html
        let updatedHtml = existingContent;

        // 1. Ensure injected style is in <head>
        if (!updatedHtml.includes('/* 4-Tab Navigation & Study Notes Styling */')) {
          if (updatedHtml.includes('</style>')) {
            updatedHtml = updatedHtml.replace('</style>', `${INJECTED_STYLES}\n    </style>`);
          } else {
            updatedHtml = updatedHtml.replace('</head>', `  <style>${INJECTED_STYLES}  </style>\n</head>`);
          }
        }

        // 2. Replace the placeholder div with the full tabbed content
        const placeholderRegex = /<!-- Concept & Notes Card -->[\s\S]*?<div style="text-align: center; padding: 3rem; background: rgba\(142, 68, 173, 0\.05\);[\s\S]*?<\/div>/i;
        if (placeholderRegex.test(updatedHtml)) {
          updatedHtml = updatedHtml.replace(placeholderRegex, () => tabsHtml);
        } else {
          // Alternative fallback replacement
          const altRegex = /<div style="text-align: center; padding: 3rem; background: rgba\(142, 68, 173, 0\.05\);[\s\S]*?<\/div>/i;
          if (altRegex.test(updatedHtml)) {
            updatedHtml = updatedHtml.replace(altRegex, () => tabsHtml);
          } else {
            console.warn(`⚠️ Could not find exact placeholder block in ${topic.slug}, appending before </main>`);
            updatedHtml = updatedHtml.replace('</main>', `${tabsHtml}\n</main>`);
          }
        }

        // 3. Inject tab switcher script before </body>
        if (!updatedHtml.includes('function openTab(evt, tabId)')) {
          updatedHtml = updatedHtml.replace('</body>', `${INJECTED_TAB_SCRIPT}\n</body>`);
        }

        // Write updated HTML
        fs.writeFileSync(topic.htmlPath, updatedHtml, 'utf8');

        // Also save pure authored JSON for reference/backup
        fs.writeFileSync(path.join(topic.dirPath, 'study-notes.json'), JSON.stringify(parsed, null, 2), 'utf8');

        // Update status
        status[topic.slug] = {
          topicTitle,
          status: 'completed',
          updatedAt: new Date().toISOString(),
          model: TARGET_MODEL
        };
        writeStatus(status);

        console.log(`   🎉 Successfully generated study notes for ${topic.slug}!\n`);
        success = true;
        completed++;
        break;
      } catch (err) {
        console.warn(`   ⚠️ Attempt ${attempt}/${MAX_ATTEMPTS} failed for ${topic.slug}: ${err.message}`);
        rotateApiKey();
        if (attempt < MAX_ATTEMPTS) {
          await new Promise(r => setTimeout(r, 2000));
        }
      }
    }

    if (!success) {
      console.error(`   ❌ Failed to generate study notes for ${topic.slug} after ${MAX_ATTEMPTS} attempts\n`);
      errors++;
    }

    if (GAP_MS > 0 && i < targetTopics.length - 1) {
      await new Promise(r => setTimeout(r, GAP_MS));
    }
  }

  console.log('======================================================================');
  console.log('🏁 Batch Generation Complete');
  console.log(`✅ Newly Generated: ${completed}`);
  console.log(`⏭️  Already Populated / Skipped: ${skipped}`);
  console.log(`❌ Errors: ${errors}`);
  console.log('======================================================================\n');
}

main().catch(err => {
  console.error('Fatal execution error:', err);
  process.exit(1);
});
