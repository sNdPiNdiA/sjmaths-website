#!/usr/bin/env node
/**
 * Generate 30 Practice MCQs (Tab 2, 3 Sub-tabs) & 15-Question Timed Mini Test (Tab 4)
 * for SSC CGL Topics (Computer Knowledge, Finance & Economics, General Awareness).
 *
 * Pre-rendered directly into each topic's index.html for maximum SEO and interactivity.
 * Zero detached JSON files created.
 *
 * Usage:
 *   node scripts/generate_ssc_cgl_tabs_2_and_4.mjs --topic backup-devices
 *   node scripts/generate_ssc_cgl_tabs_2_and_4.mjs --subject computer
 *   node scripts/generate_ssc_cgl_tabs_2_and_4.mjs --subject finance
 *   node scripts/generate_ssc_cgl_tabs_2_and_4.mjs --subject ga
 *   node scripts/generate_ssc_cgl_tabs_2_and_4.mjs --all
 *   node scripts/generate_ssc_cgl_tabs_2_and_4.mjs --dry-run
 *   node scripts/generate_ssc_cgl_tabs_2_and_4.mjs --force
 */

import fs from 'node:fs';
import path from 'node:path';
import 'dotenv/config';
import { GoogleGenAI } from '@google/genai';
import { jsonrepair } from 'jsonrepair';

const ROOT_DIR = process.cwd();
const STATUS_FILE = path.join(ROOT_DIR, 'scripts', '.ssc-tabs-2-4-status.json');

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
const SUBJECT_FILTER = flags.subject || null; // 'computer', 'finance', 'ga'
const ALL_TOPICS = Boolean(flags.all);
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
  try {
    if (fs.existsSync(STATUS_FILE)) {
      return JSON.parse(fs.readFileSync(STATUS_FILE, 'utf8'));
    }
  } catch (err) {
    console.warn('Warning: Could not read status file:', err.message);
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

// Determine marking scheme based on subject directory
function getMarkingScheme(relPath) {
  if (relPath.includes('computer-knowledge')) {
    return {
      examTitle: 'SSC CGL Tier-2 Computer Knowledge Module',
      correctMarks: 3,
      negativeMarks: 1,
      durationMins: 15
    };
  } else if (relPath.includes('finance-economics')) {
    return {
      examTitle: 'SSC CGL Paper-3 (General Studies: Finance & Economics)',
      correctMarks: 2,
      negativeMarks: 0.5,
      durationMins: 15
    };
  } else {
    return {
      examTitle: 'SSC CGL General Awareness Module',
      correctMarks: 2,
      negativeMarks: 0.5,
      durationMins: 15
    };
  }
}

// Scan directories for candidate topic pages
function discoverCandidatePages() {
  const candidates = [];
  const baseDirs = [];

  if (!SUBJECT_FILTER || SUBJECT_FILTER === 'computer' || ALL_TOPICS) {
    baseDirs.push({ dir: path.join(ROOT_DIR, 'ssc-cgl', 'computer-knowledge'), subject: 'computer' });
  }
  if (!SUBJECT_FILTER || SUBJECT_FILTER === 'finance' || ALL_TOPICS) {
    baseDirs.push({ dir: path.join(ROOT_DIR, 'ssc-cgl', 'finance-economics'), subject: 'finance' });
  }
  if (!SUBJECT_FILTER || SUBJECT_FILTER === 'ga' || ALL_TOPICS) {
    baseDirs.push({ dir: path.join(ROOT_DIR, 'ssc-cgl', 'general-awareness'), subject: 'ga' });
  }

  function walk(currentDir, subject) {
    if (!fs.existsSync(currentDir)) return;
    const entries = fs.readdirSync(currentDir, { withFileTypes: true });
    for (const e of entries) {
      if (!e.isDirectory()) continue;
      const sub = path.join(currentDir, e.name);
      const htmlPath = path.join(sub, 'index.html');
      if (fs.existsSync(htmlPath)) {
        const content = fs.readFileSync(htmlPath, 'utf8');
        const isDirectory = content.includes('class="topic-directory"') || content.includes('<!-- SJMaths generated topic directory -->');
        if (!isDirectory && (content.includes('tab-practice') || content.includes('main-tabs-nav'))) {
          const relPath = path.relative(ROOT_DIR, htmlPath).replace(/\\/g, '/');
          const slug = e.name;
          candidates.push({
            subject,
            slug,
            relPath,
            dirPath: sub,
            htmlPath
          });
        }
      }
      walk(sub, subject);
    }
  }

  for (const b of baseDirs) {
    walk(b.dir, b.subject);
  }

  // De-duplicate
  const seen = new Set();
  return candidates.filter(c => {
    if (seen.has(c.htmlPath)) return false;
    seen.add(c.htmlPath);
    return true;
  });
}

// Extract human title from index.html
function getTopicTitle(htmlPath) {
  try {
    const content = fs.readFileSync(htmlPath, 'utf8');
    const h1Match = content.match(/<h1[^>]*>([\s\S]*?)<\/h1>/i);
    if (h1Match) {
      return h1Match[1].replace(/<[^>]+>/g, '').replace(/&amp;/g, '&').trim();
    }
    const titleMatch = content.match(/<title>([^<]+)<\/title>/i);
    if (titleMatch) {
      return titleMatch[1].split('|')[0].split('—')[0].replace(/&amp;/g, '&').trim();
    }
  } catch {}
  return path.basename(path.dirname(htmlPath)).replace(/-/g, ' ');
}

// Prompt for Gemini API
function buildPrompt(topicTitle, slug, markingScheme) {
  return `You are a premier senior examination question setter and curriculum architect for the Staff Selection Commission (SSC CGL).

TOPIC: "${topicTitle}" (Slug: ${slug})
EXAM: ${markingScheme.examTitle}

TASK:
Generate two complete question sets for this topic:
1. PRACTICE QUESTIONS (30 MCQs):
   - Exactly 10 questions in "easy" (IDs 1-10): Foundational concepts, definitions, direct factual questions.
   - Exactly 10 questions in "medium" (IDs 11-20): Analytical matching, multi-statement questions, practical application, standard SSC CGL difficulty.
   - Exactly 10 questions in "hard" (IDs 21-30): In-depth, nuanced exceptions, tricky multi-statement assertions, high-difficulty exam standard.

2. MINI TEST (15 MCQs):
   - Exactly 15 questions (IDs 1-15): A balanced, timed test set (5 easy, 5 medium, 5 hard) strictly different from the practice questions.

REQUIREMENTS:
1. STRICT BILINGUAL FORMAT:
   Every question text, all 4 options, and the explanation MUST be provided in both English ("en") and standardized Hindi ("hi").
2. 4 OPTIONS (A, B, C, D):
   High quality, realistic distractors. Exactly one correct answer.
3. DETAILED EXPLANATIONS:
   Provide educational step-by-step explanations for both English and Hindi.

OUTPUT FORMAT:
Return strictly a valid JSON object matching this schema without any preamble, markdown code blocks, or extra text:

{
  "practiceQuestions": {
    "easy": [
      {
        "id": 1,
        "question": { "en": "...", "hi": "..." },
        "options": [
          { "letter": "A", "text": { "en": "...", "hi": "..." } },
          { "letter": "B", "text": { "en": "...", "hi": "..." } },
          { "letter": "C", "text": { "en": "...", "hi": "..." } },
          { "letter": "D", "text": { "en": "...", "hi": "..." } }
        ],
        "correctAnswer": "A",
        "explanation": { "en": "...", "hi": "..." }
      }
    ],
    "medium": [
      ... 10 questions with IDs 11 to 20 ...
    ],
    "hard": [
      ... 10 questions with IDs 21 to 30 ...
    ]
  },
  "miniTestQuestions": [
    ... 15 questions with IDs 1 to 15 ...
  ]
}`;
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

// Render Tab 2 HTML (30 MCQs in 3 Sub-Tabs)
function renderPracticeQuestionsHtml(practiceData) {
  const levels = [
    { key: 'easy', id: 'p-level-1', titleEn: 'Level 1: Easy (Q1–Q10)', titleHi: 'स्तर 1: सरल (प्रश्न 1–10)', nextId: 'p-level-2', nextEn: 'Proceed to Level 2: Medium Questions ➔', nextHi: 'स्तर 2: मध्यम प्रश्नों पर जाएं ➔' },
    { key: 'medium', id: 'p-level-2', titleEn: 'Level 2: Medium (Q11–Q20)', titleHi: 'स्तर 2: मध्यम (प्रश्न 11–20)', nextId: 'p-level-3', nextEn: 'Proceed to Level 3: Hard Questions ➔', nextHi: 'स्तर 3: कठिन प्रश्नों पर जाएं ➔' },
    { key: 'hard', id: 'p-level-3', titleEn: 'Level 3: Hard (Q21–Q30)', titleHi: 'स्तर 3: कठिन (प्रश्न 21–30)', nextId: null }
  ];

  let html = `<div class="practice-container">
    <div class="practice-header">
        <h2><span class="lang-en">Practice Questions (30 Bilingual MCQs)</span><span class="lang-hi">अभ्यास प्रश्न (30 द्विभाषी बहुविकल्पीय प्रश्न)</span></h2>
        <p><span class="lang-en">Practice 30 topic-specific exam-grade MCQs divided into 3 difficulty tiers. Click any option to reveal instant evaluation and detailed explanations.</span><span class="lang-hi">3 कठिनाई स्तरों में विभाजित 30 परीक्षा-स्तरीय प्रश्नों का अभ्यास करें। तत्काल मूल्यांकन और विस्तृत स्पष्टीकरण देखने के लिए किसी भी विकल्प पर क्लिक करें।</span></p>
    </div>

    <!-- Sub-Tabs Navigation -->
    <div class="practice-subtabs-nav" role="tablist">
        <button class="practice-subtab-btn active" onclick="openPracticeSubTab(event, 'p-level-1')" role="tab">
            <i class="fas fa-layer-group"></i> <span class="lang-en">Level 1: Easy (10)</span><span class="lang-hi">स्तर 1: सरल (10)</span>
        </button>
        <button class="practice-subtab-btn" onclick="openPracticeSubTab(event, 'p-level-2')" role="tab">
            <i class="fas fa-cubes"></i> <span class="lang-en">Level 2: Medium (10)</span><span class="lang-hi">स्तर 2: मध्यम (10)</span>
        </button>
        <button class="practice-subtab-btn" onclick="openPracticeSubTab(event, 'p-level-3')" role="tab">
            <i class="fas fa-brain"></i> <span class="lang-en">Level 3: Hard (10)</span><span class="lang-hi">स्तर 3: कठिन (10)</span>
        </button>
    </div>
`;

  levels.forEach((lvl, idx) => {
    const questions = practiceData[lvl.key] || [];
    const activeClass = idx === 0 ? ' active' : '';

    html += `    <!-- ${lvl.titleEn} -->
    <div class="practice-subtab-panel${activeClass}" id="${lvl.id}" role="tabpanel">
`;

    questions.forEach(q => {
      html += `        <div class="practice-q-card" id="pq-card-${q.id}">
            <div class="q-header">
                <span class="q-badge"><span class="lang-en">Q${q.id}</span><span class="lang-hi">प्रश्न ${q.id}</span></span>
                <span class="q-difficulty diff-${lvl.key}"><span class="lang-en">${lvl.key.toUpperCase()}</span><span class="lang-hi">${lvl.key === 'easy' ? 'सरल' : (lvl.key === 'medium' ? 'मध्यम' : 'कठिन')}</span></span>
            </div>
            <div class="q-text">
                <p class="lang-en">${escapeHtml(q.question.en)}</p>
                <p class="lang-hi">${escapeHtml(q.question.hi)}</p>
            </div>
            <div class="q-options" data-correct="${escapeHtml(q.correctAnswer)}">
`;

      (q.options || []).forEach(opt => {
        html += `                <button type="button" class="q-opt-btn" onclick="checkPracticeOption(this, '${escapeHtml(opt.letter)}', '${escapeHtml(q.correctAnswer)}', 'pq-sol-${q.id}')">
                    <span class="opt-letter">${escapeHtml(opt.letter)}</span>
                    <span class="opt-content">
                        <span class="lang-en">${escapeHtml(opt.text.en)}</span>
                        <span class="lang-hi">${escapeHtml(opt.text.hi)}</span>
                    </span>
                </button>\n`;
      });

      html += `            </div>
            <div class="q-solution-box" id="pq-sol-${q.id}" style="display: none;">
                <div class="sol-header">
                    <i class="fas fa-check-circle correct-icon"></i>
                    <strong><span class="lang-en">Correct Answer: Option ${escapeHtml(q.correctAnswer)}</span><span class="lang-hi">सही उत्तर: विकल्प ${escapeHtml(q.correctAnswer)}</span></strong>
                </div>
                <div class="sol-explanation">
                    <p class="lang-en">${escapeHtml(q.explanation.en)}</p>
                    <p class="lang-hi">${escapeHtml(q.explanation.hi)}</p>
                </div>
            </div>
        </div>\n`;
    });

    if (lvl.nextId) {
      html += `        <div class="subtab-nav-footer">
            <button type="button" class="next-subtab-btn" onclick="openPracticeSubTab(null, '${lvl.nextId}')">
                <span class="lang-en">${lvl.nextEn}</span><span class="lang-hi">${lvl.nextHi}</span>
            </button>
        </div>\n`;
    }

    html += `    </div>\n`;
  });

  html += `</div>`;
  return html;
}

// Render Tab 4 HTML (15-Question Timed Mini Test)
function renderMiniTestHtml(testQuestions, markingScheme) {
  const safeDataJson = JSON.stringify(testQuestions).replace(/</g, '\\u003c').replace(/>/g, '\\u003e');

  return `<div class="mini-test-container" id="mini-test-app">
    <!-- Screen 1: Test Start & Guidelines -->
    <div class="test-start-card" id="test-intro-screen">
        <div class="test-icon-badge"><i class="fas fa-stopwatch"></i></div>
        <h2><span class="lang-en">Timed Topic Mini Test</span><span class="lang-hi">समयबद्ध विषय मिनी टेस्ट</span></h2>
        <p class="test-subtitle"><span class="lang-en">Evaluate your command over this topic under simulated exam conditions.</span><span class="lang-hi">परीक्षा के समान परिस्थितियों में इस विषय पर अपनी तैयारी का मूल्यांकन करें।</span></p>

        <div class="test-rules-grid">
            <div class="rule-box">
                <i class="fas fa-question-circle"></i>
                <div class="rule-val">15</div>
                <div class="rule-lbl"><span class="lang-en">Questions</span><span class="lang-hi">कुल प्रश्न</span></div>
            </div>
            <div class="rule-box">
                <i class="fas fa-clock"></i>
                <div class="rule-val">${markingScheme.durationMins}</div>
                <div class="rule-lbl"><span class="lang-en">Minutes</span><span class="lang-hi">मिनट</span></div>
            </div>
            <div class="rule-box">
                <i class="fas fa-plus-circle"></i>
                <div class="rule-val">+${markingScheme.correctMarks}</div>
                <div class="rule-lbl"><span class="lang-en">Correct Mark</span><span class="lang-hi">सही अंक</span></div>
            </div>
            <div class="rule-box">
                <i class="fas fa-minus-circle"></i>
                <div class="rule-val">-${markingScheme.negativeMarks}</div>
                <div class="rule-lbl"><span class="lang-en">Negative Mark</span><span class="lang-hi">नकारात्मक अंक</span></div>
            </div>
        </div>

        <button type="button" class="btn-start-test" onclick="startMiniTestEngine()">
            <i class="fas fa-play"></i> <span class="lang-en">Start Mini Test Now</span><span class="lang-hi">मिनी टेस्ट अभी शुरू करें</span>
        </button>
    </div>

    <!-- Screen 2: Active Test Interface (Hidden Initially) -->
    <div class="test-active-interface" id="test-active-screen" style="display: none;">
        <div class="test-topbar">
            <div class="test-timer-badge">
                <i class="fas fa-hourglass-half"></i> <span class="lang-en">Time Left:</span><span class="lang-hi">शेष समय:</span> <span id="test-timer-display">${markingScheme.durationMins}:00</span>
            </div>
            <div class="test-progress-counter">
                <span class="lang-en">Question</span><span class="lang-hi">प्रश्न</span> <span id="cur-q-num">1</span> / 15
            </div>
        </div>

        <!-- Question Palette Pager -->
        <div class="test-palette" id="test-palette-strip"></div>

        <!-- Active Question Container -->
        <div class="active-question-card" id="active-question-wrapper"></div>

        <!-- Controls Bar -->
        <div class="test-controls-bar">
            <button type="button" class="test-ctrl-btn" id="btn-prev-q" onclick="navigateTestQuestion(-1)"><i class="fas fa-arrow-left"></i> <span class="lang-en">Prev</span><span class="lang-hi">पिछला</span></button>
            <button type="button" class="test-ctrl-btn" id="btn-next-q" onclick="navigateTestQuestion(1)"><span class="lang-en">Next</span><span class="lang-hi">अगला</span> <i class="fas fa-arrow-right"></i></button>
            <button type="button" class="test-ctrl-btn btn-submit-test" onclick="submitMiniTestEngine()"><i class="fas fa-check-double"></i> <span class="lang-en">Submit Test</span><span class="lang-hi">टेस्ट सबमिट करें</span></button>
        </div>
    </div>

    <!-- Screen 3: Results & Analytics Screen (Hidden Initially) -->
    <div class="test-results-screen" id="test-results-screen" style="display: none;">
        <div class="scorecard-hero">
            <div class="scorecard-badge"><i class="fas fa-trophy"></i></div>
            <h2><span class="lang-en">Test Performance Summary</span><span class="lang-hi">टेस्ट प्रदर्शन सारांश</span></h2>
            <div class="score-display">
                <span id="final-score-val">0</span> / <span id="final-max-val">${15 * markingScheme.correctMarks}</span>
            </div>
            <div class="accuracy-tag"><span class="lang-en">Accuracy:</span><span class="lang-hi">सटीकता:</span> <span id="final-accuracy-val">0%</span></div>
        </div>

        <div class="scorecard-stats-grid">
            <div class="stat-pill stat-correct">
                <i class="fas fa-check"></i> <span class="lang-en">Correct:</span><span class="lang-hi">सही:</span> <span id="count-correct">0</span>
            </div>
            <div class="stat-pill stat-wrong">
                <i class="fas fa-times"></i> <span class="lang-en">Incorrect:</span><span class="lang-hi">गलत:</span> <span id="count-wrong">0</span>
            </div>
            <div class="stat-pill stat-unattempted">
                <i class="fas fa-minus"></i> <span class="lang-en">Unattempted:</span><span class="lang-hi">छोड़े गए:</span> <span id="count-unattempted">15</span>
            </div>
        </div>

        <div class="test-solutions-accordion">
            <h3><span class="lang-en">Detailed Solutions Review</span><span class="lang-hi">विस्तृत हल समीक्षा</span></h3>
            <div id="test-solutions-list"></div>
        </div>

        <div class="test-retake-footer">
            <button type="button" class="btn-retake-test" onclick="retakeMiniTestEngine()"><i class="fas fa-redo"></i> <span class="lang-en">Retake Test</span><span class="lang-hi">पुनः टेस्ट दें</span></button>
        </div>
    </div>

    <script id="mini-test-data" type="application/json">${safeDataJson}</script>
</div>`;
}

// Injected CSS for Tab 2 (Practice Questions) & Tab 4 (Mini Test)
const INJECTED_TABS_2_4_CSS = `
    /* Tab 2: Practice Questions Styles */
    .practice-container { padding: 0.5rem 0; }
    .practice-header { margin-bottom: 1.5rem; }
    .practice-header h2 {
        font-family: 'Outfit', sans-serif;
        font-size: 1.45rem;
        font-weight: 800;
        color: #8e44ad;
        margin-bottom: 0.5rem;
    }
    .practice-header p { color: #64748b; font-size: 0.95rem; line-height: 1.5; }
    
    .practice-subtabs-nav {
        display: flex;
        gap: 0.5rem;
        margin-bottom: 1.5rem;
        border-bottom: 2px solid #e2e8f0;
        padding-bottom: 0.35rem;
        overflow-x: auto;
    }
    .practice-subtab-btn {
        background: transparent;
        border: none;
        border-radius: 8px;
        padding: 0.65rem 1rem;
        font-family: 'Outfit', sans-serif;
        font-size: 0.9rem;
        font-weight: 700;
        color: #64748b;
        cursor: pointer;
        display: flex;
        align-items: center;
        gap: 0.45rem;
        transition: all 0.2s ease;
        white-space: nowrap;
    }
    .practice-subtab-btn:hover { background: rgba(142, 68, 173, 0.05); color: #8e44ad; }
    .practice-subtab-btn.active {
        background: #8e44ad;
        color: #ffffff;
        box-shadow: 0 4px 10px rgba(142, 68, 173, 0.25);
    }
    .practice-subtab-panel { display: none; }
    .practice-subtab-panel.active { display: block; animation: upFadeIn 0.3s ease-out; }

    .practice-q-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 1.25rem;
        margin-bottom: 1.25rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.03);
        transition: border-color 0.2s ease;
    }
    .practice-q-card:hover { border-color: #cbd5e1; }
    .q-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem; }
    .q-badge {
        background: rgba(142, 68, 173, 0.1);
        color: #8e44ad;
        font-weight: 800;
        font-size: 0.82rem;
        padding: 0.25rem 0.65rem;
        border-radius: 6px;
    }
    .q-difficulty {
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        padding: 0.2rem 0.55rem;
        border-radius: 4px;
    }
    .diff-easy { background: rgba(16, 185, 129, 0.12); color: #059669; }
    .diff-medium { background: rgba(245, 158, 11, 0.12); color: #d97706; }
    .diff-hard { background: rgba(239, 68, 68, 0.12); color: #dc2626; }

    .q-text { font-size: 0.98rem; font-weight: 600; color: #1e293b; margin-bottom: 1rem; line-height: 1.6; }
    .q-options { display: grid; grid-template-columns: 1fr; gap: 0.6rem; margin-bottom: 0.75rem; }
    .q-opt-btn {
        background: #f8fafc;
        border: 1.5px solid #e2e8f0;
        border-radius: 8px;
        padding: 0.75rem 1rem;
        text-align: left;
        display: flex;
        align-items: flex-start;
        gap: 0.75rem;
        cursor: pointer;
        transition: all 0.2s ease;
        font-size: 0.92rem;
        color: #334155;
    }
    .q-opt-btn:hover:not(:disabled) { background: #f1f5f9; border-color: #8e44ad; }
    .q-opt-btn .opt-letter {
        font-weight: 800;
        color: #8e44ad;
        min-width: 22px;
        height: 22px;
        background: #ffffff;
        border: 1px solid #cbd5e1;
        border-radius: 50%;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        font-size: 0.8rem;
        flex-shrink: 0;
        margin-top: 1px;
    }
    .q-opt-btn.correct-choice {
        background: #ecfdf5 !important;
        border-color: #10b981 !important;
        color: #065f46 !important;
    }
    .q-opt-btn.correct-choice .opt-letter { background: #10b981; color: #ffffff; border-color: #10b981; }
    .q-opt-btn.wrong-choice {
        background: #fef2f2 !important;
        border-color: #ef4444 !important;
        color: #991b1b !important;
    }
    .q-opt-btn.wrong-choice .opt-letter { background: #ef4444; color: #ffffff; border-color: #ef4444; }

    .q-solution-box {
        background: #f8fafc;
        border-left: 4px solid #10b981;
        border-radius: 0 8px 8px 0;
        padding: 0.85rem 1.1rem;
        margin-top: 0.85rem;
        animation: upFadeIn 0.25s ease-out;
    }
    .sol-header { color: #065f46; font-size: 0.9rem; margin-bottom: 0.35rem; display: flex; align-items: center; gap: 0.4rem; }
    .sol-explanation { font-size: 0.88rem; color: #475569; line-height: 1.55; }
    
    .subtab-nav-footer { text-align: center; margin: 2rem 0 1rem; }
    .next-subtab-btn {
        background: #8e44ad;
        color: #ffffff;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 1.75rem;
        font-family: 'Outfit', sans-serif;
        font-size: 0.95rem;
        font-weight: 700;
        cursor: pointer;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .next-subtab-btn:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(142, 68, 173, 0.3); }

    /* Tab 4: Timed Mini Test Styles */
    .mini-test-container { padding: 0.5rem 0; }
    .test-start-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 2.5rem 2rem;
        text-align: center;
        max-width: 650px;
        margin: 1.5rem auto;
        box-shadow: 0 10px 25px rgba(0,0,0,0.04);
    }
    .test-icon-badge {
        font-size: 2.5rem;
        color: #8e44ad;
        background: rgba(142, 68, 173, 0.08);
        width: 70px;
        height: 70px;
        line-height: 70px;
        border-radius: 50%;
        margin: 0 auto 1.25rem;
    }
    .test-start-card h2 { font-family: 'Outfit', sans-serif; font-size: 1.5rem; color: #1e293b; margin-bottom: 0.4rem; font-weight: 800; }
    .test-subtitle { color: #64748b; font-size: 0.92rem; margin-bottom: 1.75rem; }
    .test-rules-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 0.75rem;
        margin-bottom: 2rem;
    }
    .rule-box {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        padding: 0.85rem 0.5rem;
        text-align: center;
    }
    .rule-box i { color: #8e44ad; font-size: 1.1rem; margin-bottom: 0.35rem; }
    .rule-val { font-size: 1.2rem; font-weight: 800; color: #1e293b; }
    .rule-lbl { font-size: 0.75rem; color: #64748b; font-weight: 600; text-transform: uppercase; }
    .btn-start-test {
        background: linear-gradient(135deg, #8e44ad, #9b59b6);
        color: #ffffff;
        border: none;
        border-radius: 30px;
        padding: 0.85rem 2.25rem;
        font-family: 'Outfit', sans-serif;
        font-size: 1.05rem;
        font-weight: 700;
        cursor: pointer;
        box-shadow: 0 4px 15px rgba(142, 68, 173, 0.35);
        transition: all 0.25s ease;
    }
    .btn-start-test:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(142, 68, 173, 0.45); }

    /* Test Active Interface */
    .test-topbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        padding: 0.75rem 1.25rem;
        margin-bottom: 1.25rem;
    }
    .test-timer-badge { font-weight: 800; color: #dc2626; font-size: 1rem; display: flex; align-items: center; gap: 0.45rem; }
    .test-progress-counter { font-weight: 700; color: #475569; font-size: 0.95rem; }
    
    .test-palette {
        display: flex;
        gap: 0.4rem;
        overflow-x: auto;
        padding-bottom: 0.75rem;
        margin-bottom: 1.25rem;
    }
    .palette-btn {
        min-width: 34px;
        height: 34px;
        border-radius: 6px;
        border: 1px solid #cbd5e1;
        background: #ffffff;
        color: #475569;
        font-weight: 700;
        font-size: 0.82rem;
        cursor: pointer;
        transition: all 0.2s ease;
        flex-shrink: 0;
    }
    .palette-btn.current { border-color: #8e44ad; background: #8e44ad; color: #ffffff; }
    .palette-btn.answered { background: #10b981; border-color: #10b981; color: #ffffff; }

    .active-question-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1.25rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.03);
    }
    .test-controls-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 0.75rem;
    }
    .test-ctrl-btn {
        background: #ffffff;
        border: 1.5px solid #cbd5e1;
        border-radius: 8px;
        padding: 0.65rem 1.25rem;
        font-family: 'Outfit', sans-serif;
        font-size: 0.9rem;
        font-weight: 700;
        color: #475569;
        cursor: pointer;
        transition: all 0.2s ease;
    }
    .test-ctrl-btn:hover { background: #f8fafc; border-color: #8e44ad; color: #8e44ad; }
    .btn-submit-test {
        background: #10b981;
        border-color: #10b981;
        color: #ffffff;
        margin-left: auto;
    }
    .btn-submit-test:hover { background: #059669; border-color: #059669; color: #ffffff; }

    /* Results Screen */
    .scorecard-hero {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 2.25rem 2rem;
        text-align: center;
        margin-bottom: 1.5rem;
    }
    .scorecard-badge {
        font-size: 2.2rem;
        color: #f59e0b;
        margin-bottom: 0.75rem;
    }
    .scorecard-hero h2 { font-family: 'Outfit', sans-serif; font-size: 1.4rem; color: #1e293b; margin-bottom: 0.5rem; }
    .score-display {
        font-size: 2.5rem;
        font-weight: 900;
        color: #8e44ad;
        font-family: 'Outfit', sans-serif;
        margin: 0.5rem 0;
    }
    .accuracy-tag { font-size: 0.95rem; font-weight: 700; color: #64748b; }
    .scorecard-stats-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 0.75rem;
        margin-bottom: 2rem;
    }
    .stat-pill {
        border-radius: 10px;
        padding: 0.85rem;
        text-align: center;
        font-size: 0.9rem;
        font-weight: 700;
    }
    .stat-correct { background: #ecfdf5; color: #065f46; border: 1px solid #a7f3d0; }
    .stat-wrong { background: #fef2f2; color: #991b1b; border: 1px solid #fecaca; }
    .stat-unattempted { background: #f8fafc; color: #475569; border: 1px solid #e2e8f0; }

    .test-solutions-accordion h3 {
        font-family: 'Outfit', sans-serif;
        font-size: 1.25rem;
        font-weight: 800;
        color: #1e293b;
        margin-bottom: 1rem;
    }
    .btn-retake-test {
        background: #8e44ad;
        color: #ffffff;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 2rem;
        font-family: 'Outfit', sans-serif;
        font-size: 0.95rem;
        font-weight: 700;
        cursor: pointer;
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        margin-top: 1rem;
    }
    .test-retake-footer { text-align: center; margin: 2rem 0; }
`;

// Injected Interactive Runner Script
const INJECTED_TABS_2_4_JS = `
<script>
/* Tab 2: Practice Questions Subtab Switcher & Interactive Evaluation */
function openPracticeSubTab(evt, subTabId) {
    document.querySelectorAll('.practice-subtab-panel').forEach(function(p) { p.classList.remove('active'); });
    document.querySelectorAll('.practice-subtabs-nav .practice-subtab-btn').forEach(function(b) { b.classList.remove('active'); });
    var panel = document.getElementById(subTabId);
    if (panel) panel.classList.add('active');
    var btn = evt && evt.currentTarget ? evt.currentTarget : document.querySelector('.practice-subtabs-nav .practice-subtab-btn[onclick*="' + subTabId + '"]');
    if (btn) btn.classList.add('active');
}

function checkPracticeOption(btn, chosenOpt, correctOpt, solBoxId) {
    var parent = btn.closest('.q-options');
    if (parent.dataset.evaluated === 'true') return;
    parent.dataset.evaluated = 'true';

    var allBtns = parent.querySelectorAll('.q-opt-btn');
    allBtns.forEach(function(b) {
        b.disabled = true;
        var opt = b.getAttribute('onclick').match(/checkPracticeOption\\(this,\\s*'([A-D])'/);
        var letter = opt ? opt[1] : '';
        if (letter === correctOpt) {
            b.classList.add('correct-choice');
        } else if (b === btn && chosenOpt !== correctOpt) {
            b.classList.add('wrong-choice');
        }
    });

    var solBox = document.getElementById(solBoxId);
    if (solBox) solBox.style.display = 'block';
}

/* Tab 4: Interactive Timed Mini Test Engine */
var testEngine = {
    questions: [],
    currentIndex: 0,
    answers: {},
    timerSeconds: 900,
    timerInterval: null,
    correctMarks: 3,
    negativeMarks: 1,
    isSubmitted: false
};

function initMiniTestData() {
    var raw = document.getElementById('mini-test-data');
    if (raw) {
        try { testEngine.questions = JSON.parse(raw.textContent); } catch (e) { testEngine.questions = []; }
    }
}

function startMiniTestEngine() {
    initMiniTestData();
    if (!testEngine.questions || testEngine.questions.length === 0) return;
    
    document.getElementById('test-intro-screen').style.display = 'none';
    document.getElementById('test-active-screen').style.display = 'block';
    document.getElementById('test-results-screen').style.display = 'none';

    testEngine.currentIndex = 0;
    testEngine.answers = {};
    testEngine.isSubmitted = false;
    testEngine.timerSeconds = 900;

    renderTestPalette();
    renderActiveQuestion();
    startTestTimer();
}

function startTestTimer() {
    clearInterval(testEngine.timerInterval);
    testEngine.timerInterval = setInterval(function() {
        if (testEngine.timerSeconds <= 0) {
            clearInterval(testEngine.timerInterval);
            submitMiniTestEngine();
            return;
        }
        testEngine.timerSeconds--;
        var mins = Math.floor(testEngine.timerSeconds / 60);
        var secs = testEngine.timerSeconds % 60;
        var disp = (mins < 10 ? '0' : '') + mins + ':' + (secs < 10 ? '0' : '') + secs;
        var el = document.getElementById('test-timer-display');
        if (el) el.textContent = disp;
    }, 1000);
}

function renderTestPalette() {
    var strip = document.getElementById('test-palette-strip');
    if (!strip) return;
    strip.innerHTML = '';
    for (var i = 0; i < testEngine.questions.length; i++) {
        var b = document.createElement('button');
        b.type = 'button';
        b.className = 'palette-btn' + (i === testEngine.currentIndex ? ' current' : '') + (testEngine.answers[i] ? ' answered' : '');
        b.textContent = i + 1;
        b.onclick = (function(idx) { return function() { jumpToTestQuestion(idx); }; })(i);
        strip.appendChild(b);
    }
}

function jumpToTestQuestion(idx) {
    testEngine.currentIndex = idx;
    renderTestPalette();
    renderActiveQuestion();
}

function navigateTestQuestion(step) {
    var next = testEngine.currentIndex + step;
    if (next >= 0 && next < testEngine.questions.length) {
        jumpToTestQuestion(next);
    }
}

function renderActiveQuestion() {
    var q = testEngine.questions[testEngine.currentIndex];
    if (!q) return;

    var curEl = document.getElementById('cur-q-num');
    if (curEl) curEl.textContent = testEngine.currentIndex + 1;

    var prevBtn = document.getElementById('btn-prev-q');
    var nextBtn = document.getElementById('btn-next-q');
    if (prevBtn) prevBtn.disabled = testEngine.currentIndex === 0;
    if (nextBtn) nextBtn.disabled = testEngine.currentIndex === testEngine.questions.length - 1;

    var wrapper = document.getElementById('active-question-wrapper');
    if (!wrapper) return;

    var chosen = testEngine.answers[testEngine.currentIndex];

    var html = '<div class="q-header">' +
        '<span class="q-badge"><span class="lang-en">Question ' + (testEngine.currentIndex + 1) + '</span><span class="lang-hi">प्रश्न ' + (testEngine.currentIndex + 1) + '</span></span>' +
        '</div>' +
        '<div class="q-text">' +
        '<p class="lang-en">' + (q.question.en || '') + '</p>' +
        '<p class="lang-hi">' + (q.question.hi || '') + '</p>' +
        '</div>' +
        '<div class="q-options">';

    (q.options || []).forEach(function(opt) {
        var isSelected = chosen === opt.letter;
        html += '<button type="button" class="q-opt-btn' + (isSelected ? ' selected-test-opt' : '') + '" onclick="selectTestAnswer(\\'' + opt.letter + '\\')">' +
            '<span class="opt-letter">' + opt.letter + '</span>' +
            '<span class="opt-content">' +
            '<span class="lang-en">' + (opt.text.en || '') + '</span>' +
            '<span class="lang-hi">' + (opt.text.hi || '') + '</span>' +
            '</span>' +
            '</button>';
    });

    html += '</div>';
    wrapper.innerHTML = html;
}

function selectTestAnswer(letter) {
    testEngine.answers[testEngine.currentIndex] = letter;
    renderTestPalette();
    renderActiveQuestion();
}

function submitMiniTestEngine() {
    clearInterval(testEngine.timerInterval);
    testEngine.isSubmitted = true;

    var total = testEngine.questions.length;
    var correctCount = 0;
    var wrongCount = 0;
    var unattemptedCount = 0;

    for (var i = 0; i < total; i++) {
        var ans = testEngine.answers[i];
        var correct = testEngine.questions[i].correctAnswer;
        if (!ans) {
            unattemptedCount++;
        } else if (ans === correct) {
            correctCount++;
        } else {
            wrongCount++;
        }
    }

    var score = (correctCount * testEngine.correctMarks) - (wrongCount * testEngine.negativeMarks);
    score = Math.max(0, score);
    var attempted = correctCount + wrongCount;
    var accuracy = attempted > 0 ? Math.round((correctCount / attempted) * 100) : 0;

    document.getElementById('test-active-screen').style.display = 'none';
    document.getElementById('test-results-screen').style.display = 'block';

    document.getElementById('final-score-val').textContent = score;
    document.getElementById('final-accuracy-val').textContent = accuracy + '%';
    document.getElementById('count-correct').textContent = correctCount;
    document.getElementById('count-wrong').textContent = wrongCount;
    document.getElementById('count-unattempted').textContent = unattemptedCount;

    // Render Solutions List
    var solList = document.getElementById('test-solutions-list');
    if (solList) {
        solList.innerHTML = '';
        testEngine.questions.forEach(function(q, idx) {
            var userAns = testEngine.answers[idx] || 'Not Attempted';
            var isRight = userAns === q.correctAnswer;
            var item = document.createElement('div');
            item.className = 'practice-q-card';
            item.innerHTML = '<div class="q-header">' +
                '<span class="q-badge">Q' + (idx + 1) + '</span>' +
                '<span class="q-difficulty ' + (isRight ? 'diff-easy' : 'diff-hard') + '">' + (isRight ? 'CORRECT' : (userAns === 'Not Attempted' ? 'UNATTEMPTED' : 'INCORRECT')) + '</span>' +
                '</div>' +
                '<div class="q-text"><p class="lang-en">' + (q.question.en || '') + '</p><p class="lang-hi">' + (q.question.hi || '') + '</p></div>' +
                '<div class="q-solution-box" style="display:block;">' +
                '<div class="sol-header"><strong><span class="lang-en">Correct: Option ' + q.correctAnswer + ' | Your Answer: ' + userAns + '</span><span class="lang-hi">सही: विकल्प ' + q.correctAnswer + ' | आपका उत्तर: ' + userAns + '</span></strong></div>' +
                '<div class="sol-explanation"><p class="lang-en">' + (q.explanation.en || '') + '</p><p class="lang-hi">' + (q.explanation.hi || '') + '</p></div>' +
                '</div>';
            solList.appendChild(item);
        });
    }
}

function retakeMiniTestEngine() {
    startMiniTestEngine();
}

document.addEventListener('DOMContentLoaded', initMiniTestData);
</script>`;

// Main execution loop
async function main() {
  console.log('======================================================================');
  console.log('🎯 SSC CGL Tab 2 (30 MCQs) & Tab 4 (Mini Test) Generator');
  console.log(`🤖 Model: ${TARGET_MODEL}`);
  console.log(`🔑 Available API Keys: ${apiKeys.length}`);
  if (DRY_RUN) console.log('🔍 Mode: DRY-RUN (no files will be written)');
  console.log('======================================================================\n');

  let candidates = discoverCandidatePages();
  console.log(`Found ${candidates.length} candidate topic pages across SSC CGL.\n`);

  if (TOPIC_FILTER) {
    candidates = candidates.filter(c => c.slug.toLowerCase().includes(TOPIC_FILTER.toLowerCase()));
  }
  if (LIMIT > 0) {
    candidates = candidates.slice(0, LIMIT);
  }

  const status = readStatus();
  let completed = 0;
  let skipped = 0;
  let errors = 0;

  for (let i = 0; i < candidates.length; i++) {
    const topic = candidates[i];
    const topicTitle = getTopicTitle(topic.htmlPath);
    console.log(`[${i + 1}/${candidates.length}] Processing: ${topicTitle} (${topic.relPath})`);

    const existingContent = fs.readFileSync(topic.htmlPath, 'utf8');
    const hasPractice = existingContent.includes('practice-q-card') || existingContent.includes('p-level-1');
    const hasMiniTest = existingContent.includes('mini-test-app') || existingContent.includes('mini-test-data');

    if (!FORCE && hasPractice && hasMiniTest) {
      console.log(`   ✅ [Already Populated with Tab 2 & Tab 4] Skipping.\n`);
      skipped++;
      continue;
    }

    if (DRY_RUN) {
      console.log(`   [DRY-RUN] Would generate Tab 2 & Tab 4 for "${topicTitle}"\n`);
      completed++;
      continue;
    }

    const scheme = getMarkingScheme(topic.relPath);
    let success = false;

    for (let attempt = 1; attempt <= MAX_ATTEMPTS; attempt++) {
      try {
        const client = getGenAIClient();
        const prompt = buildPrompt(topicTitle, topic.slug, scheme);

        const response = await client.models.generateContent({
          model: TARGET_MODEL,
          contents: prompt,
          config: {
            temperature: 0.25,
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

        if (!parsed.practiceQuestions || !parsed.miniTestQuestions) {
          throw new Error('Generated JSON missing practiceQuestions or miniTestQuestions');
        }

        // Render HTML for Tab 2 and Tab 4
        const practiceHtml = renderPracticeQuestionsHtml(parsed.practiceQuestions);
        const miniTestHtml = renderMiniTestHtml(parsed.miniTestQuestions, scheme);

        let updatedHtml = existingContent;

        // 1. Inject Styles if not already present
        if (!updatedHtml.includes('/* Tab 2: Practice Questions Styles */')) {
          if (updatedHtml.includes('</style>')) {
            updatedHtml = updatedHtml.replace('</style>', `${INJECTED_TABS_2_4_CSS}\n    </style>`);
          } else {
            updatedHtml = updatedHtml.replace('</head>', `  <style>${INJECTED_TABS_2_4_CSS}  </style>\n</head>`);
          }
        }

        // 2. Inject or Replace Tab 2 and Tab 4 Panels
        const hasTabPractice = updatedHtml.includes('id="tab-practice"') || updatedHtml.includes("id='tab-practice'");
        const hasTabMiniTest = updatedHtml.includes('id="tab-mini-test"') || updatedHtml.includes("id='tab-mini-test'");

        if (hasTabPractice) {
          const tabPracticeRegex = /<div class="tab-panel"[^>]*id=["']tab-practice["'][^>]*>[\s\S]*?<\/div>\s*(?=<!-- Tab 3|<div class="tab-panel"|$)/i;
          if (tabPracticeRegex.test(updatedHtml)) {
            updatedHtml = updatedHtml.replace(tabPracticeRegex, `<div class="tab-panel" id="tab-practice" role="tabpanel">\n${practiceHtml}\n</div>\n\n`);
          }
        }

        if (hasTabMiniTest) {
          const tabMiniTestRegex = /<div class="tab-panel"[^>]*id=["']tab-mini-test["'][^>]*>[\s\S]*?<\/div>\s*(?=<\/main>|$)/i;
          if (tabMiniTestRegex.test(updatedHtml)) {
            updatedHtml = updatedHtml.replace(tabMiniTestRegex, `<div class="tab-panel" id="tab-mini-test" role="tabpanel">\n${miniTestHtml}\n</div>\n`);
          }
        }

        // If neither was present, inject them before </main>
        if (!hasTabPractice && !hasTabMiniTest && updatedHtml.includes('</main>')) {
          const tabBlock = `\n<!-- Tab 2: Practice Questions -->
<div class="tab-panel" id="tab-practice" role="tabpanel">
${practiceHtml}
</div>

<!-- Tab 3: Previous Year Questions -->
<div class="tab-panel" id="tab-pyqs" role="tabpanel">
<div class="tab-placeholder-card">
    <i class="fas fa-history placeholder-icon"></i>
    <h3><span class="lang-en">Previous Year Questions (PYQs)</span><span class="lang-hi">पिछले वर्ष के प्रश्न</span></h3>
    <p><span class="lang-en">Curated SSC CGL Tier-1 &amp; Tier-2 previous year questions for this topic with step-by-step explanations will be indexed here.</span><span class="lang-hi">विस्तृत स्पष्टीकरण के साथ इस विषय के SSC CGL टियर-1 और टियर-2 के पिछले वर्षों के प्रश्न यहाँ उपलब्ध होंगे।</span></p>
</div>
</div>

<!-- Tab 4: Mini Test -->
<div class="tab-panel" id="tab-mini-test" role="tabpanel">
${miniTestHtml}
</div>\n`;
          updatedHtml = updatedHtml.replace('</main>', `${tabBlock}</main>`);
        } else if (hasTabPractice && !hasTabMiniTest && updatedHtml.includes('</main>')) {
          const miniTestBlock = `\n<!-- Tab 4: Mini Test -->
<div class="tab-panel" id="tab-mini-test" role="tabpanel">
${miniTestHtml}
</div>\n`;
          updatedHtml = updatedHtml.replace('</main>', `${miniTestBlock}</main>`);
        }

        // 4. Inject Interactive Runner JS before </body>
        if (!updatedHtml.includes('function openPracticeSubTab(evt, subTabId)')) {
          updatedHtml = updatedHtml.replace('</body>', `${INJECTED_TABS_2_4_JS}\n</body>`);
        }

        // Write directly to index.html (Zero extra JSON files)
        fs.writeFileSync(topic.htmlPath, updatedHtml, 'utf8');

        // Update status log
        status[topic.relPath] = {
          topicTitle,
          status: 'completed',
          updatedAt: new Date().toISOString(),
          model: TARGET_MODEL
        };
        writeStatus(status);

        console.log(`   🎉 Successfully generated Tab 2 & Tab 4 in ${topic.relPath}!\n`);
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
      console.error(`   ❌ Failed to generate Tab 2 & Tab 4 for ${topic.slug} after ${MAX_ATTEMPTS} attempts\n`);
      errors++;
    }

    if (GAP_MS > 0 && i < candidates.length - 1) {
      await new Promise(r => setTimeout(r, GAP_MS));
    }
  }

  console.log('======================================================================');
  console.log('🏁 Batch Generation Complete for Tab 2 & Tab 4');
  console.log(`✅ Newly Generated: ${completed}`);
  console.log(`⏭️  Already Populated / Skipped: ${skipped}`);
  console.log(`❌ Errors: ${errors}`);
  console.log('======================================================================\n');
}

main().catch(err => {
  console.error('Fatal execution error:', err);
  process.exit(1);
});
