#!/usr/bin/env node
/**
 * scripts/generate_ahc_ro_aro_notes.mjs
 *
 * Subject-Wise Pointwise Study Notes Generator for Allahabad High Court RO/ARO
 * (Review Officer / Assistant Review Officer) Examination.
 *
 * Generates:
 * 1. Deep-dive pointwise study notes directly rendered inside index.html (#deep-dive-section)
 * 2. Embedded JSON study guide data (<script id="embedded-study-guide-data"> and -hi)
 * 3. Standalone theory.json data file for runtime and offline consistency
 * 4. Rich noscript SEO block
 *
 * Usage:
 *   node scripts/generate_ahc_ro_aro_notes.mjs --subject history-of-india
 *   node scripts/generate_ahc_ro_aro_notes.mjs --subject general-science --topic biotechnology
 *   node scripts/generate_ahc_ro_aro_notes.mjs --all
 *   node scripts/generate_ahc_ro_aro_notes.mjs --subject computer-knowledge --limit 3
 *   node scripts/generate_ahc_ro_aro_notes.mjs --list
 *   node scripts/generate_ahc_ro_aro_notes.mjs --dry-run
 *   node scripts/generate_ahc_ro_aro_notes.mjs --force
 */

import fs from 'node:fs';
import path from 'node:path';
import 'dotenv/config';
import { GoogleGenAI } from '@google/genai';
import { jsonrepair } from 'jsonrepair';

const ROOT_DIR = process.cwd();
const AHC_DIR = path.join(ROOT_DIR, 'ahc-ro-aro');
const STATUS_FILE = path.join(ROOT_DIR, 'scripts', '.ahc-notes-status.json');

// Subject Registry with Titles and Curated Exam Contexts
const SUBJECT_MAP = {
  'agriculture-commerce-trade': {
    name: 'Agriculture, Commerce & Trade',
    nameHi: 'कृषि, वाणिज्य एवं व्यापार',
    context: 'Agricultural systems, cropping seasons (Kharif/Rabi/Zaid), Green & Allied Revolutions, soil types, irrigation, agro-climatic zones, domestic trade, MSMEs, SEZs, export-import policies, and balance of payments.'
  },
  'computer-knowledge': {
    name: 'Computer Knowledge & Typing',
    nameHi: 'कंप्यूटर ज्ञान एवं टाइपिंग',
    context: 'Computer architecture, CPU registers, input/output & memory types, operating systems, MS Office Suite (Word, Excel, PowerPoint), networking (LAN/WAN, topologies), Internet, email protocols (SMTP/POP/IMAP), cyber security & viruses, typing accuracy & 25+ WPM standards.'
  },
  'current-affairs': {
    name: 'Current Affairs (National & International)',
    nameHi: 'समसामयिक घटनाएं (राष्ट्रीय एवं अंतर्राष्ट्रीय)',
    context: 'National & international events, government flagship schemes, bilateral summits, bills & acts, constitutional appointments (CAG, CEC, CJI), international bodies (UN, G20, BRICS), sports tournaments, awards, and Nobel prizes.'
  },
  'english': {
    name: 'General English & Hindi',
    nameHi: 'सामान्य अंग्रेजी एवं हिंदी',
    context: 'High-court standard English grammar: parts of speech, tenses & conditionals, voice, narration, vocabulary (synonyms, antonyms, idioms, one-word substitution), sentence correction, cloze tests, and Hindi grammar fundamentals (Varnamala, Sandhi, Samas, Karak).'
  },
  'general-aptitude': {
    name: 'General Aptitude & Reasoning',
    nameHi: 'सामान्य योग्यता एवं तर्कशक्ति',
    context: 'Verbal and non-verbal reasoning: number & alphabet series, coding-decoding, blood relations, direction sense, syllogisms, seating arrangements, statement-assumptions, Venn diagrams, time & work, speed-distance-time, profit & loss, and data sufficiency.'
  },
  'general-science': {
    name: 'General Science & Technology',
    nameHi: 'सामान्य विज्ञान एवं प्रौद्योगिकी',
    context: 'Physics (mechanics, electricity, light, sound, units), Chemistry (atomic structure, periodic table, acids-bases, carbon compounds, metals), Biology (cell biology, genetics, human anatomy, diseases, plant physiology), and Modern Tech (biotechnology, defense, space missions).'
  },
  'geography': {
    name: 'Geography of India & World',
    nameHi: 'भारत एवं विश्व का भूगोल',
    context: 'Physical geography, geomorphology, climatology, oceans, physiographic divisions of India (Himalayas, Northern Plains, Peninsular Plateau, Coastal Plains), drainage & river valley projects, mineral & energy resources, and water conservation schemes.'
  },
  'history-of-india': {
    name: 'History of India',
    nameHi: 'भारत का इतिहास',
    context: 'Ancient India (Pre-history, Indus Valley, Vedic Age, Buddhism, Jainism, Mauryas, Guptas), Medieval India (Delhi Sultanate, Vijayanagara, Bhakti-Sufi movements, Mughals), and Early Modern India (Advent of Europeans, British Expansion, 1857 Revolt, Socio-religious reforms, Land revenue systems).'
  },
  'indian-national-movement': {
    name: 'Indian National Movement',
    nameHi: 'भारतीय राष्ट्रीय आंदोलन',
    context: 'Rise of nationalism, INC formation, Moderate & Extremist phases, Swadeshi movement, Home Rule, Gandhian era (Non-Cooperation, Civil Disobedience, Quit India), revolutionary leaders (Bhagat Singh, Subhash Chandra Bose, Ambedkar, Patel), INA, and Transfer of Power.'
  },
  'mains-comprehension': {
    name: 'Mains Reading Comprehension',
    nameHi: 'मुख्य परीक्षा - गद्यांश बोध',
    context: 'Allahabad High Court descriptive paper: unseen passage analysis, analytical context extraction, precise factual question answering, title formulation, inference identification, and vocabulary in context.'
  },
  'mains-essay': {
    name: 'Mains Essay Writing',
    nameHi: 'मुख्य परीक्षा - निबंध लेखन',
    context: 'Descriptive essay structures: constitutional & legal issues, judicial reforms, socio-economic challenges (poverty, unemployment), science & technology, environmental degradation, and contemporary national & international themes.'
  },
  'mains-precis': {
    name: 'Mains Précis Writing',
    nameHi: 'मुख्य परीक्षा - संक्षेपण',
    context: 'Techniques of précis writing: skimming and identifying central theme, maintaining one-third length proportion, eliminating redundant words and personal opinions, formulating titles, and preserving logical flow.'
  },
  'mains-translation': {
    name: 'Mains Administrative Translation',
    nameHi: 'मुख्य परीक्षा - प्रशासनिक अनुवाद',
    context: 'Official legal and administrative bilingual translation: English to Hindi and Hindi to English, formal administrative vocabulary, drafting official letters/circulars, legal court phraseology, and contextual equivalence.'
  },
  'polity-economy-culture': {
    name: 'Indian Polity, Economy & Culture',
    nameHi: 'भारतीय राज्यव्यवस्था, अर्थव्यवस्था एवं संस्कृति',
    context: 'Constituent Assembly, Preamble, Fundamental Rights & Duties, DPSP, Union & State Executive and Legislature, Judiciary (Supreme Court, High Courts, Judicial Review), Panchayati Raj, NITI Aayog, Five-Year Plans, Banking/RBI, Indian art, temple architecture, and classical dances.'
  },
  'population-ecology-urbanisation': {
    name: 'Population, Ecology & Urbanisation',
    nameHi: 'जनसंख्या, पर्यावरण एवं नगरीकरण',
    context: 'Census 2011 detailed facts (India & UP), demographic dividend, literacy & sex ratio, ecosystems & biomes, biodiversity hotspots in India, food chains, global warming, pollution control laws, National Parks & Wildlife Sanctuaries, Smart Cities, and waste management.'
  },
  'up-special-knowledge': {
    name: 'UP Special Knowledge',
    nameHi: 'उत्तर प्रदेश विशेष ज्ञान',
    context: 'Uttar Pradesh geography, soil profiles, rivers & irrigation canals, major crops & ODOP (One District One Product), MSMEs & industrial corridors, education & universities, historical monuments & tourism, fairs & festivals (Kumbh, Taj Mahotsav), folk arts & dances, and state budget.'
  }
};

// CLI Arguments Parser
function parseCliArgs(args) {
  const flags = {};
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
    }
  }
  return flags;
}

const flags = parseCliArgs(process.argv.slice(2));

if (flags.help) {
  console.log(`
AHC RO/ARO Subject-Wise Pointwise Study Notes Generator
-------------------------------------------------------
Options:
  --subject <slug>   Target a specific subject (e.g. history-of-india, general-science)
  --topic <slug>     Target a specific topic slug
  --all              Process all subjects
  --limit <n>        Limit number of topics to process
  --force            Regenerate even if topic is already populated
  --dry-run          Preview topics without calling API or modifying files
  --model <name>     Gemini model to use (default: gemini-3.5-flash)
  --list             List all subjects, topics, and their status
  --help             Show this help message
`);
  process.exit(0);
}

const TARGET_MODEL = flags.model || process.env.GEMINI_MODEL || 'gemini-3.5-flash';
const FALLBACK_MODELS = ['gemini-3.5-flash', 'gemini-3.5-flash-lite', 'gemini-3.8-flash'];
const LIMIT = flags.limit ? parseInt(flags.limit, 10) : 0;
const SUBJECT_FILTER = flags.subject || null;
const TOPIC_FILTER = flags.topic || null;
const FORCE = Boolean(flags.force);
const DRY_RUN = Boolean(flags['dry-run']);
const PROCESS_ALL = Boolean(flags.all);

// API Keys rotation setup
const apiKeys = [
  process.env.GEMINI_API_KEY,
  process.env.GEMINI_API_KEY_1,
  process.env.GEMINI_API_KEY_2,
  process.env.GOOGLE_API_KEY
].filter(Boolean);

if (apiKeys.length === 0 && !DRY_RUN && !flags.list) {
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

// Helpers
function escapeHtml(str) {
  if (!str) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

function slugToTitle(slug) {
  return slug
    .split('-')
    .map(w => w.charAt(0).toUpperCase() + w.slice(1))
    .join(' ');
}

function readStatus() {
  try {
    if (fs.existsSync(STATUS_FILE)) {
      return JSON.parse(fs.readFileSync(STATUS_FILE, 'utf8'));
    }
  } catch {}
  return {};
}

function writeStatus(status) {
  try {
    fs.writeFileSync(STATUS_FILE, JSON.stringify(status, null, 2), 'utf8');
  } catch {}
}

// Inspect topic status
function getTopicInfo(subjectSlug, topicSlug) {
  const topicDir = path.join(AHC_DIR, subjectSlug, topicSlug);
  const indexPath = path.join(topicDir, 'index.html');
  const theoryPath = path.join(topicDir, 'theory.json');

  let hasIndex = fs.existsSync(indexPath);
  let hasTheory = fs.existsSync(theoryPath);
  let isPopulated = false;

  if (hasIndex) {
    const content = fs.readFileSync(indexPath, 'utf8');
    const hasDeepDiveContent = !/<div class="card-premium" id="deep-dive-section">\s*<\/div>/i.test(content)
      && content.includes('id="deep-dive-section"');
    if (hasDeepDiveContent && hasTheory) {
      isPopulated = true;
    }
  }

  return {
    subjectSlug,
    topicSlug,
    topicDir,
    indexPath,
    theoryPath,
    hasIndex,
    hasTheory,
    isPopulated
  };
}

// Collect all topics
function collectTopics() {
  const allTopics = [];
  const subjects = Object.keys(SUBJECT_MAP);

  for (const subj of subjects) {
    const subjDir = path.join(AHC_DIR, subj);
    if (!fs.existsSync(subjDir)) continue;

    const entries = fs.readdirSync(subjDir, { withFileTypes: true });
    for (const ent of entries) {
      if (!ent.isDirectory()) continue;
      allTopics.push(getTopicInfo(subj, ent.name));
    }
  }

  return allTopics;
}

// List Mode
if (flags.list) {
  const topics = collectTopics();
  console.log(`\n📋 AHC RO/ARO Topics Catalog (${topics.length} total across 16 subjects):\n`);
  const grouped = {};
  topics.forEach(t => {
    grouped[t.subjectSlug] = grouped[t.subjectSlug] || [];
    grouped[t.subjectSlug].push(t);
  });

  for (const [subj, list] of Object.entries(grouped)) {
    const populated = list.filter(t => t.isPopulated).length;
    console.log(`📁 ${subj} (${populated}/${list.length} populated):`);
    list.forEach(t => {
      const mark = t.isPopulated ? '✅' : '⚪';
      console.log(`   ${mark} ${t.topicSlug}`);
    });
  }
  process.exit(0);
}

// Build Prompt for Gemini
function buildPrompt(subjectSlug, topicSlug, topicTitle) {
  const subj = SUBJECT_MAP[subjectSlug] || { name: slugToTitle(subjectSlug), nameHi: '', context: '' };

  return `You are a premier Examination Authority, senior question setter, and subject matter expert for the Allahabad High Court RO/ARO (Review Officer / Assistant Review Officer) examination and UPPSC.

SUBJECT: "${subj.name}" (${subj.nameHi})
TOPIC: "${topicTitle}" (Slug: ${topicSlug})
CURRICULUM FOCUS: ${subj.context}

TASK:
Generate comprehensive, authentic, high-yielding POINTWISE Study Notes for this topic strictly formatted for Allahabad High Court RO/ARO aspirants.

CRITICAL REQUIREMENTS:
1. STRICT BILINGUAL FORMAT:
   Every heading, paragraph, bullet point, table cell, flashcard, and trap must have English ("en") and standardized Hindi ("hi") counterparts using official Indian administrative and exam terminology.

2. PURE POINTWISE STUDY STRUCTURE:
   - "overview": Concise 2-3 sentence overview of why this topic is vital for AHC RO/ARO.
   - "timeline": 4 to 6 chronological milestones / developmental stages / key phases.
   - "sections": 4 to 6 distinct thematic sections breaking down the entire topic.
     * Each section MUST have 4 to 7 detailed POINTWISE bullets with "label" (bold key concept/term) and "detail" (exhaustive, factual explanation including dates, articles, acts, key personalities, formulas, scientific names, or UP-specific data).
     * At least one section MUST include a "table" with "title", "headers" (3-4 columns), and "rows" (4-6 rows of high-yield facts/comparisons).
   - "flashcards": 4 to 5 active recall flashcard Q&As testing frequent exam questions.
   - "mnemonics": 2 to 3 practical memory acronyms / memory keys with phrases and breakdowns.
   - "traps": 3 to 4 common exam traps / factual confusions that negative-marking questions exploit.

OUTPUT FORMAT:
Return strictly a valid JSON object matching this exact schema without any markdown formatting wrappers, markdown ticks, or preamble:

{
  "topicTitle": { "en": "${topicTitle}", "hi": "..." },
  "overview": { "en": "...", "hi": "..." },
  "timeline": {
    "title": { "en": "...", "hi": "..." },
    "description": { "en": "...", "hi": "..." },
    "cards": [
      {
        "period": { "en": "...", "hi": "..." },
        "date": "...",
        "details": { "en": "...", "hi": "..." }
      }
    ]
  },
  "sections": [
    {
      "title": { "en": "...", "hi": "..." },
      "intro": { "en": "...", "hi": "..." },
      "points": [
        {
          "label": { "en": "...", "hi": "..." },
          "detail": { "en": "...", "hi": "..." }
        }
      ],
      "table": {
        "title": { "en": "...", "hi": "..." },
        "headers": [
          { "en": "...", "hi": "..." }
        ],
        "rows": [
          [
            { "en": "...", "hi": "..." }
          ]
        ]
      }
    }
  ],
  "flashcards": [
    {
      "question": { "en": "...", "hi": "..." },
      "answer": { "en": "...", "hi": "..." },
      "icon": "fa-book"
    }
  ],
  "mnemonics": [
    {
      "title": { "en": "...", "hi": "..." },
      "phrase": "...",
      "decryption": { "en": "...", "hi": "..." }
    }
  ],
  "traps": [
    {
      "title": { "en": "...", "hi": "..." },
      "text": { "en": "...", "hi": "..." }
    }
  ]
}`;
}

// Generate pre-rendered deep-dive HTML
function renderDeepDiveHtml(data, lang = 'en') {
  const isHi = lang === 'hi';
  const getVal = obj => (isHi ? (obj?.hi || obj?.en || '') : (obj?.en || obj?.hi || ''));
  const title = getVal(data.topicTitle) || 'Core';
  const overview = getVal(data.overview);

  let html = `<h2 class="card-title">${escapeHtml(title)} Core Study Notes</h2>\n`;
  if (overview) {
    html += `<p>${escapeHtml(overview)}</p>\n`;
  }
  html += `<div class="study-notes-content">\n`;

  data.sections.forEach((sec, idx) => {
    const secTitle = getVal(sec.title) || `Section ${idx + 1}`;
    const secIntro = getVal(sec.intro);
    html += `  <section class="study-section">\n`;
    html += `    <h3>${escapeHtml(secTitle)}</h3>\n`;
    html += `    <div class="section-content">\n`;

    if (secIntro) {
      html += `      <p>${escapeHtml(secIntro)}</p>\n`;
    }

    if (Array.isArray(sec.points) && sec.points.length > 0) {
      html += `      <ul style="padding-left: 1.25rem; line-height: 1.7; margin-bottom: 1.5rem;">\n`;
      sec.points.forEach(pt => {
        const lbl = getVal(pt.label);
        const dtl = getVal(pt.detail);
        html += `        <li style="margin-bottom: 0.75rem;"><strong>${escapeHtml(lbl)}:</strong> ${escapeHtml(dtl)}</li>\n`;
      });
      html += `      </ul>\n`;
    }

    if (sec.table && Array.isArray(sec.table.headers) && Array.isArray(sec.table.rows)) {
      html += `      <div class="premium-table-container">\n`;
      html += `        <table class="premium-table">\n`;
      html += `          <thead>\n            <tr>\n`;
      sec.table.headers.forEach(h => {
        html += `              <th>${escapeHtml(getVal(h))}</th>\n`;
      });
      html += `            </tr>\n          </thead>\n          <tbody>\n`;
      sec.table.rows.forEach(r => {
        html += `            <tr>\n`;
        r.forEach(c => {
          html += `              <td>${escapeHtml(getVal(c))}</td>\n`;
        });
        html += `            </tr>\n`;
      });
      html += `          </tbody>\n        </table>\n      </div>\n`;
    }

    html += `    </div>\n  </section>\n`;
  });

  html += `</div>`;
  return html;
}

// Convert model output to theory.json format
function buildTheoryJson(data, subjectSlug, topicSlug, lang = 'en') {
  const isHi = lang === 'hi';
  const getVal = obj => (isHi ? (obj?.hi || obj?.en || '') : (obj?.en || obj?.hi || ''));
  const subj = SUBJECT_MAP[subjectSlug] || { name: slugToTitle(subjectSlug), nameHi: '' };
  const parentName = isHi ? (subj.nameHi || subj.name) : subj.name;
  const currentTitle = getVal(data.topicTitle) || slugToTitle(topicSlug);
  const overview = getVal(data.overview);

  return {
    breadcrumbs: {
      parent: parentName,
      parentUrl: "../",
      current: currentTitle
    },
    hero: {
      title: currentTitle,
      description: overview
    },
    labels: {
      clickToExpand: isHi ? "विवरण देखने के लिए क्लिक करें" : "Click to expand details",
      mockIntro: {
        title: isHi ? `इंटरएक्टिव ${currentTitle} मॉक टेस्ट` : `Interactive ${currentTitle} Mock Test`,
        description: isHi ? `${currentTitle} पर अपनी तैयारी का परीक्षण करें।` : `Assess your understanding of ${currentTitle}. This timed test covers essential exam questions.`,
        startBtn: isHi ? "मॉक टेस्ट प्रारंभ करें" : "Start Mock Test"
      },
      mockPlay: {
        prevBtn: isHi ? "पिछला प्रश्न" : "Previous Question",
        nextBtn: isHi ? "अगला प्रश्न" : "Next Question",
        submitBtn: isHi ? "टेस्ट सबमिट करें" : "Submit Test"
      }
    },
    timeline: {
      title: getVal(data.timeline?.title) || (isHi ? "महत्वपूर्ण मील के पत्थर" : "Chronological Evolution"),
      description: getVal(data.timeline?.description) || "",
      cards: (data.timeline?.cards || []).map(c => ({
        period: getVal(c.period),
        date: c.date || "",
        details: getVal(c.details)
      }))
    },
    mnemonics: {
      title: isHi ? `${currentTitle} स्मृति सहायक और ट्रिक्स` : `${currentTitle} Mnemonics & Study Tricks`,
      description: isHi ? "त्वरित स्मरण के लिए ट्रिक्स" : "Quick memory triggers to recall key facts for AHC RO/ARO exams.",
      items: (data.mnemonics || []).map(m => ({
        title: getVal(m.title),
        phrase: m.phrase || "",
        decryption: getVal(m.decryption)
      }))
    },
    flashcards: {
      title: isHi ? "सक्रिय स्मरण फ्लैशकार्ड" : "Active Recall Flashcards",
      description: isHi ? "उत्तर देखने के लिए क्लिक करें" : "Hover or click to reveal the answers. Revisit these cards to build instant recall.",
      items: (data.flashcards || []).map(f => ({
        question: getVal(f.question),
        answer: getVal(f.answer),
        icon: f.icon || "fa-book"
      }))
    },
    traps: {
      title: isHi ? "परीक्षा में सामान्य गलतियाँ" : "Common Exam Traps to Avoid",
      items: (data.traps || []).map(t => {
        const trapTitle = getVal(t.title);
        const trapText = getVal(t.text);
        return `<strong>${escapeHtml(trapTitle)}:</strong> ${escapeHtml(trapText)}`;
      })
    },
    deepDive: {
      title: isHi ? `${currentTitle} मुख्य अध्ययन नोट्स` : `${currentTitle} Core Study Notes`,
      description: overview,
      sections: data.sections.map((sec, idx) => {
        const secTitle = getVal(sec.title) || `Section ${idx + 1}`;
        let content = '';
        if (sec.intro) {
          content += `<p>${escapeHtml(getVal(sec.intro))}</p>\n`;
        }
        if (Array.isArray(sec.points) && sec.points.length > 0) {
          content += `<ul style="padding-left: 1.25rem; line-height: 1.7; margin-bottom: 1.5rem;">\n`;
          sec.points.forEach(pt => {
            content += `<li style="margin-bottom: 0.75rem;"><strong>${escapeHtml(getVal(pt.label))}:</strong> ${escapeHtml(getVal(pt.detail))}</li>\n`;
          });
          content += `</ul>\n`;
        }
        return {
          title: secTitle,
          content
        };
      })
    }
  };
}

// Generate Noscript SEO Block
function renderNoscriptSeo(data) {
  const title = data.topicTitle?.en || 'Topic';
  const overview = data.overview?.en || '';
  let html = `<!-- SEO_NOSCRIPT_START -->\n<noscript>\n<div style="padding:20px;max-width:960px;margin:0 auto;font-family:sans-serif;line-height:1.7">\n`;
  html += `<h1>${escapeHtml(title)}</h1>\n`;
  if (overview) html += `<p>${escapeHtml(overview)}</p>\n`;

  data.sections.forEach(sec => {
    html += `<h3>${escapeHtml(sec.title?.en || '')}</h3>\n`;
    if (sec.intro?.en) html += `<p>${escapeHtml(sec.intro.en)}</p>\n`;
    if (Array.isArray(sec.points)) {
      html += `<ul>\n`;
      sec.points.forEach(pt => {
        html += `  <li><strong>${escapeHtml(pt.label?.en || '')}:</strong> ${escapeHtml(pt.detail?.en || '')}</li>\n`;
      });
      html += `</ul>\n`;
    }
  });

  if (Array.isArray(data.flashcards) && data.flashcards.length > 0) {
    html += `<h3>Key Questions &amp; Answers</h3>\n<dl>\n`;
    data.flashcards.forEach(f => {
      html += `<dt><strong>${escapeHtml(f.question?.en || '')}</strong></dt>\n`;
      html += `<dd>${escapeHtml(f.answer?.en || '')}</dd>\n`;
    });
    html += `</dl>\n`;
  }

  html += `</div>\n</noscript>\n<!-- SEO_NOSCRIPT_END -->`;
  return html;
}

// Inject Generated Notes into index.html
function injectIntoIndexHtml(htmlPath, data, theoryEn, theoryHi) {
  let content = fs.readFileSync(htmlPath, 'utf8');

  // 1. Render and inject deep-dive-section
  const deepDiveHtml = renderDeepDiveHtml(data, 'en');
  const deepDiveRegex = /<div class="card-premium" id="deep-dive-section">[\s\S]*?<\/div>/i;
  const newDeepDive = `<div class="card-premium" id="deep-dive-section">${deepDiveHtml}</div>`;

  if (deepDiveRegex.test(content)) {
    content = content.replace(deepDiveRegex, newDeepDive);
  } else {
    // If not found, insert before flashcards-section or tab end
    content = content.replace(
      /<div class="card-premium" id="flashcards-section">/i,
      `${newDeepDive}\n            <div class="card-premium" id="flashcards-section">`
    );
  }

  // 2. Inject or update noscript SEO block
  const noscriptBlock = renderNoscriptSeo(data);
  const existingNoscriptRegex = /<!-- SEO_NOSCRIPT_START -->[\s\S]*?<!-- SEO_NOSCRIPT_END -->/i;
  if (existingNoscriptRegex.test(content)) {
    content = content.replace(existingNoscriptRegex, noscriptBlock);
  } else {
    // Insert before Next button in Tab 1
    content = content.replace(
      /(<button class="btn-action btn-next" onclick="switchTab\('practice-panel'\)")/i,
      `${noscriptBlock}\n            $1`
    );
  }

  // 3. Inject or update embedded JSON scripts
  const scriptEnTag = `<script id="embedded-study-guide-data" type="application/json">\n${JSON.stringify(theoryEn, null, 2)}\n</script>`;
  const scriptHiTag = `<script id="embedded-study-guide-data-hi" type="application/json">\n${JSON.stringify(theoryHi, null, 2)}\n</script>`;

  const existingEnScript = /<script id="embedded-study-guide-data" type="application\/json">[\s\S]*?<\/script>/i;
  const existingHiScript = /<script id="embedded-study-guide-data-hi" type="application\/json">[\s\S]*?<\/script>/i;

  if (existingEnScript.test(content)) {
    content = content.replace(existingEnScript, scriptEnTag);
  }
  if (existingHiScript.test(content)) {
    content = content.replace(existingHiScript, scriptHiTag);
  }

  if (!existingEnScript.test(content) && !existingHiScript.test(content)) {
    // Insert before closing </body>
    const languageRuntimeTag = `<script data-ahc-ro-aro-language="shared" src="/assets/js/ahc-ro-aro-language.min.js?v=4ddbdb0d"></script>`;
    const bundle = `\n    ${scriptEnTag}\n\n    ${scriptHiTag}\n\n    ${languageRuntimeTag}\n`;
    
    // Check if language runtime already exists
    if (content.includes('data-ahc-ro-aro-language="shared"')) {
      content = content.replace(/<script data-ahc-ro-aro-language="shared"[\s\S]*?<\/script>/i, `${scriptEnTag}\n\n    ${scriptHiTag}\n\n    $&`);
    } else {
      content = content.replace('</body>', `${bundle}</body>`);
    }
  }

  fs.writeFileSync(htmlPath, content, 'utf8');
}

// Generate Notes for a Single Topic
async function processTopic(topicInfo) {
  const { subjectSlug, topicSlug, indexPath, theoryPath } = topicInfo;
  const topicTitle = slugToTitle(topicSlug);

  console.log(`\n------------------------------------------------------------`);
  console.log(`📖 Generating notes for: [${subjectSlug}] -> ${topicSlug} (${topicTitle})`);

  if (DRY_RUN) {
    console.log(`   [DRY-RUN] Would call Gemini (${TARGET_MODEL}) and generate pointwise study notes.`);
    return true;
  }

  const prompt = buildPrompt(subjectSlug, topicSlug, topicTitle);
  let attempts = 0;
  const maxAttempts = 3;

  while (attempts < maxAttempts) {
    const currentModel = FALLBACK_MODELS[attempts % FALLBACK_MODELS.length] || TARGET_MODEL;
    attempts++;
    try {
      const client = getGenAIClient();
      console.log(`   ⚡ Calling Gemini API (attempt ${attempts}/${maxAttempts}, model: ${currentModel})...`);

      const generatePromise = client.models.generateContent({
        model: currentModel,
        contents: prompt,
        config: {
          temperature: 0.3,
          responseMimeType: 'application/json'
        }
      });

      const timeoutPromise = new Promise((_, reject) =>
        setTimeout(() => reject(new Error(`API request timed out after 60s for ${currentModel}`)), 60000)
      );

      const response = await Promise.race([generatePromise, timeoutPromise]);

      const rawText = response.text?.trim() || '';
      let parsed;
      try {
        parsed = JSON.parse(rawText);
      } catch (err) {
        console.log(`   ⚠️ Direct JSON.parse failed, running jsonrepair...`);
        parsed = JSON.parse(jsonrepair(rawText));
      }

      if (!parsed || !Array.isArray(parsed.sections) || parsed.sections.length === 0) {
        throw new Error('Invalid structure returned: sections array missing or empty');
      }

      // Convert to theory formats
      const theoryEn = buildTheoryJson(parsed, subjectSlug, topicSlug, 'en');
      const theoryHi = buildTheoryJson(parsed, subjectSlug, topicSlug, 'hi');

      // Write standalone theory.json
      fs.writeFileSync(theoryPath, JSON.stringify(theoryEn, null, 2), 'utf8');
      console.log(`   💾 Saved ${path.relative(ROOT_DIR, theoryPath)}`);

      // Inject into index.html
      injectIntoIndexHtml(indexPath, parsed, theoryEn, theoryHi);
      console.log(`   💾 Injected pointwise notes into ${path.relative(ROOT_DIR, indexPath)}`);

      return true;
    } catch (err) {
      console.error(`   ❌ Attempt ${attempts} failed: ${err.message}`);
      rotateApiKey();
      if (attempts < maxAttempts) {
        const delay = attempts * 3000;
        console.log(`   ⏳ Waiting ${delay / 1000}s before retry...`);
        await new Promise(r => setTimeout(r, delay));
      }
    }
  }

  return false;
}

// Main Execution Flow
async function main() {
  console.log('🚀 AHC RO/ARO Pointwise Study Notes Generator Initialized');
  console.log(`   Model: ${TARGET_MODEL}`);
  console.log(`   Target Directory: ${AHC_DIR}`);

  let topics = collectTopics();

  // Filter by subject if specified
  if (SUBJECT_FILTER) {
    if (!SUBJECT_MAP[SUBJECT_FILTER]) {
      console.error(`❌ Unknown subject: "${SUBJECT_FILTER}". Valid subjects:`);
      Object.keys(SUBJECT_MAP).forEach(s => console.log(`   - ${s}`));
      process.exit(1);
    }
    topics = topics.filter(t => t.subjectSlug === SUBJECT_FILTER);
    console.log(`   Filtered to subject: ${SUBJECT_FILTER} (${topics.length} topics)`);
  } else if (!PROCESS_ALL && !TOPIC_FILTER) {
    console.log(`\n💡 Tip: Provide --subject <name> (e.g. --subject history-of-india) or --all to process.`);
    console.log(`   Available subjects:`);
    Object.keys(SUBJECT_MAP).forEach(s => console.log(`   - ${s}`));
    console.log(`\n   Run with --help for all options.`);
    process.exit(0);
  }

  // Filter by topic if specified
  if (TOPIC_FILTER) {
    topics = topics.filter(t => t.topicSlug === TOPIC_FILTER);
    console.log(`   Filtered to topic: ${TOPIC_FILTER} (${topics.length} matches)`);
  }

  // Filter by population status unless --force
  if (!FORCE) {
    const totalBefore = topics.length;
    topics = topics.filter(t => !t.isPopulated);
    console.log(`   Skipped ${totalBefore - topics.length} already populated topics. (${topics.length} remaining to generate)`);
  }

  // Apply limit
  if (LIMIT > 0 && topics.length > LIMIT) {
    console.log(`   Applying limit: processing first ${LIMIT} topics`);
    topics = topics.slice(0, LIMIT);
  }

  if (topics.length === 0) {
    console.log('\n✨ All requested topics are already populated! Use --force to regenerate.');
    return;
  }

  console.log(`\n🎯 Queue size: ${topics.length} topics to process.`);

  let successCount = 0;
  let failCount = 0;

  for (const topic of topics) {
    const ok = await processTopic(topic);
    if (ok) {
      successCount++;
    } else {
      failCount++;
    }

    // Gentle rate limit gap between requests
    if (!DRY_RUN) {
      await new Promise(r => setTimeout(r, 1500));
    }
  }

  console.log(`\n============================================================`);
  console.log(`🎉 Batch Run Completed: ${successCount} succeeded, ${failCount} failed.`);
}

main().catch(err => {
  console.error('Fatal execution error:', err);
  process.exit(1);
});
