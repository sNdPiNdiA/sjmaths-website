#!/usr/bin/env node
/**
 * ============================================================================
 * SJ Maths — Hindi Content Generator Pipeline (UP PGT / TGT Hindi)
 * Model: gemini-3.5-flash-lite only
 * Language: Pure High-Standard Academic Hindi (Devanagari script)
 * Architecture:
 *   - Two API Calls per Topic:
 *       Call 1: Exhaustive Study Notes (Dynamic number of conceptual modules /
 *               pillars tailored to the specific topic, grammar rules/poetics,
 *               critical exceptions, mnemonics/shortcuts).
 *       Call 2: Quick Revision Summary (Glossary, high-yield facts, confusions),
 *               Practice Quiz (18-20 MCQs), PYQs (5-6 MCQs), and Timed Test (10 MCQs).
 * ============================================================================
 */

import fs from 'fs';
import path from 'path';
import 'dotenv/config';
import { GoogleGenAI } from '@google/genai';
import { jsonrepair } from 'jsonrepair';

// Parse CLI arguments early to allow custom key flag
const args = process.argv.slice(2);
function getArg(flag) {
  const idx = args.indexOf(flag);
  return idx !== -1 && args[idx + 1] ? args[idx + 1] : null;
}
const hasFlag = (flag) => args.includes(flag);

// Determine keys to use
const SPECIFIC_KEY = getArg('--key'); // e.g. --key 1 or --key GEMINI_API_KEY_1

let rawKeys = [];
if (SPECIFIC_KEY === '1' || SPECIFIC_KEY === 'GEMINI_API_KEY_1') {
  rawKeys = [process.env.GEMINI_API_KEY_1];
} else if (SPECIFIC_KEY === '2' || SPECIFIC_KEY === 'GEMINI_API_KEY_2') {
  rawKeys = [process.env.GEMINI_API_KEY_2];
} else if (SPECIFIC_KEY === 'GEMINI_API_KEY') {
  rawKeys = [process.env.GEMINI_API_KEY];
} else {
  // Put GEMINI_API_KEY_1 first since it has active quota
  rawKeys = [
    process.env.GEMINI_API_KEY_1,
    process.env.GEMINI_API_KEY_2,
    process.env.GEMINI_API_KEY
  ];
}

const apiKeys = [...new Set(rawKeys.filter(Boolean))];

if (apiKeys.length === 0) {
  console.error('CRITICAL ERROR: No valid GEMINI_API_KEY found in .env');
  process.exit(1);
}

console.log(`Loaded ${apiKeys.length} Gemini API key(s). Active keys: ${apiKeys.map(k => k.substring(0, 10) + '...' + k.slice(-6)).join(', ')}`);
const aiClients = apiKeys.map((key, i) => ({
  id: i + 1,
  preview: key.substring(0, 10) + '...' + key.slice(-6),
  client: new GoogleGenAI({ apiKey: key })
}));
let clientIndex = 0;

function getClient() {
  const c = aiClients[clientIndex % aiClients.length];
  clientIndex++;
  return c;
}

// Parse Command Line Arguments (already initialized above)

const TARGET_TOPIC = getArg('--topic');
const TARGET_SECTION = getArg('--section');
const LIMIT = getArg('--limit') ? parseInt(getArg('--limit'), 10) : null;
const FORCE = hasFlag('--force');
const DRY_RUN = hasFlag('--dry-run');
const GAP_MS = getArg('--gap') ? parseInt(getArg('--gap'), 10) * 1000 : 1500; // 1.5s default

// Strictly use gemini-3.5-flash-lite as requested
const MODEL_NAME = 'gemini-3.5-flash-lite';

// Status Tracking File
const STATUS_FILE = 'content-generation-status-hindi.json';
let statusMap = {};
if (fs.existsSync(STATUS_FILE)) {
  try {
    statusMap = JSON.parse(fs.readFileSync(STATUS_FILE, 'utf8'));
  } catch (e) {
    statusMap = {};
  }
}

function saveStatus() {
  fs.writeFileSync(STATUS_FILE, JSON.stringify(statusMap, null, 2), 'utf8');
}

// Section Hindi metadata mapping
const SECTION_NAMES = {
  'sahitya-itihas': { hi: 'हिन्दी साहित्य का इतिहास', en: 'Hindi Literature History', code: '01' },
  'gadya-sahitya': { hi: 'गद्य-साहित्य का उद्भव और विकास', en: 'Prose Literature', code: '02' },
  'patrakarita': { hi: 'पत्रकारिता एवं जनसंचार', en: 'Journalism and Mass Communication', code: '03' },
  'kavyashastra': { hi: 'काव्यशास्त्र (भारतीय एवं पाश्चात्य)', en: 'Poetics and Literary Criticism', code: '04' },
  'bhashavigyan': { hi: 'भाषाविज्ञान एवं हिन्दी भाषा', en: 'Linguistics and Hindi Language', code: '05' },
  'vyakaran': { hi: 'हिन्दी व्याकरण', en: 'Hindi Grammar', code: '06' },
  'rachnaakar-aur-rachnayen': { hi: 'प्रमुख रचनाकार और रचनाएँ', en: 'Authors and Famous Works', code: '07' }
};

// Extract title and subtopic metadata from up-pgt-hindi/index.html
function getTopicMetadataFromTracker() {
  const map = {};
  const trackerPaths = ['up-pgt-hindi/index.html', 'up-tgt-hindi/index.html'];
  for (const tPath of trackerPaths) {
    if (fs.existsSync(tPath)) {
      const html = fs.readFileSync(tPath, 'utf8');
      const regex = /<div class="topic"[^>]*data-search="([^"]+)"[\s\S]*?<a class="topic-link" href="([^"]+)">([^<]+)<\/a>/g;
      let m;
      while ((m = regex.exec(html)) !== null) {
        const [_, searchTxt, url, title] = m;
        const cleanUrl = url.endsWith('/') ? url : url + '/';
        if (!map[cleanUrl]) {
          map[cleanUrl] = {
            title: title.trim(),
            searchKeywords: searchTxt.split(' ').filter(Boolean)
          };
        }
      }
    }
  }
  return map;
}

const trackerTopicMap = getTopicMetadataFromTracker();

// Recursively find all Hindi topic pages
function getAllHindiPages(dir = 'hindi') {
  let pages = [];
  if (!fs.existsSync(dir)) return pages;
  const list = fs.readdirSync(dir, { withFileTypes: true });
  for (const item of list) {
    const full = path.join(dir, item.name);
    if (item.isDirectory()) {
      pages = pages.concat(getAllHindiPages(full));
    } else if (item.name === 'index.html') {
      let rel = full.replace(/\\/g, '/');
      if (!rel.startsWith('/')) rel = '/' + rel;
      rel = rel.replace(/index\.html$/, '');
      if (!rel.endsWith('/')) rel += '/';
      pages.push({
        url: rel,
        dir: path.dirname(full)
      });
    }
  }
  return pages;
}

const allHindiTopics = getAllHindiPages();

// Determine eligible topics
function getEligibleTopics() {
  return allHindiTopics.filter(item => {
    if (TARGET_TOPIC) {
      const cleanTarget = TARGET_TOPIC.endsWith('/') ? TARGET_TOPIC : TARGET_TOPIC + '/';
      return item.url === cleanTarget;
    }
    if (TARGET_SECTION) {
      if (!item.url.includes(`/${TARGET_SECTION}/`)) return false;
    }
    if (!FORCE && statusMap[item.url] && statusMap[item.url].status === 'completed') {
      return false;
    }
    return true;
  });
}

// Get rich context for a topic
function getTopicContext(item) {
  const parts = item.url.split('/').filter(Boolean);
  const branchKey = parts[1] || 'vyakaran';
  const branchMeta = SECTION_NAMES[branchKey] || {
    hi: branchKey.replace(/-/g, ' '),
    en: branchKey.replace(/-/g, ' '),
    code: '00'
  };

  const slug = parts[parts.length - 1];
  const trackerMeta = trackerTopicMap[item.url];
  const fallbackTitle = slug.split('-').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' ');
  const topicTitleHi = trackerMeta ? trackerMeta.title : fallbackTitle;

  // Find related topics in the same branch
  const sectionPrefix = `/hindi/${branchKey}/`;
  const related = allHindiTopics
    .filter(other => other.url.startsWith(sectionPrefix) && other.url !== item.url)
    .slice(0, 6)
    .map(r => {
      const meta = trackerTopicMap[r.url];
      const rSlug = r.url.split('/').filter(Boolean).pop();
      const rTitle = meta ? meta.title : rSlug.replace(/-/g, ' ');
      return { url: r.url, title: rTitle };
    });

  return {
    branchKey,
    branchMeta,
    slug,
    topicTitleHi,
    related
  };
}

// Sanitize Raw JSON string
function cleanRawJson(text) {
  let cleaned = text.trim();
  if (cleaned.startsWith('```json')) cleaned = cleaned.slice(7);
  else if (cleaned.startsWith('```')) cleaned = cleaned.slice(3);
  if (cleaned.endsWith('```')) cleaned = cleaned.slice(0, -3);
  return cleaned.trim();
}

// Convert markdown bold to strong
function cleanMarkdownStars(val) {
  if (typeof val === 'string') {
    return val
      .replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>')
      .replace(/(^|[^\*])\*([^*\n]+)\*([^\*]|$)/g, '$1<em>$2</em>$3');
  }
  if (Array.isArray(val)) {
    return val.map(cleanMarkdownStars);
  }
  if (val !== null && typeof val === 'object') {
    const res = {};
    for (const key of Object.keys(val)) {
      res[key] = cleanMarkdownStars(val[key]);
    }
    return res;
  }
  return val;
}

// Normalize question objects
function normalizeQuestions(arr) {
  if (!Array.isArray(arr)) return;
  arr.forEach(q => {
    if (!q || typeof q !== 'object') return;
    if (!Array.isArray(q.options)) {
      if (q.options && typeof q.options === 'object') {
        q.options = Object.values(q.options);
      } else {
        q.options = [];
      }
    }
    while (q.options.length < 4) {
      q.options.push(`विकल्प ${String.fromCharCode(65 + q.options.length)}`);
    }
    q.options = q.options.slice(0, 4).map(opt => String(opt ?? ''));

    if (typeof q.correct_index !== 'number' || q.correct_index < 0 || q.correct_index > 3) {
      if (typeof q.correct_answer === 'string') {
        const char = q.correct_answer.trim().toUpperCase().charAt(0);
        const map = { 'A': 0, 'B': 1, 'C': 2, 'D': 3 };
        q.correct_index = map[char] !== undefined ? map[char] : 0;
      } else {
        q.correct_index = 0;
      }
    }
    if (!q.explanation) q.explanation = 'प्रामाणिक व्याकरण एवं साहित्य नियमों के अनुसार सही उत्तर।';
  });
}

// ============================================================================
// CALL 1: STUDY NOTES PROMPT (Dynamic number of conceptual modules, Pure Hindi)
// ============================================================================
function buildCall1Prompt(item, context) {
  return `आप उच्च माध्यमिक शिक्षक भर्ती (UP PGT Hindi - विषय कोड 04, UP TGT Hindi) एवं UGC-NET हिन्दी साहित्य/व्याकरण के शीर्ष विशेषज्ञ प्राध्यापक हैं।
निम्नलिखित विषय पर अत्यंत प्रामाणिक, गहन और परीक्षा-उपयोगी अध्ययन नोट्स (Study Notes) शुद्ध हिन्दी (देवनागरी लिपि) में तैयार करें:

विषय विवरण:
- विषय: "${context.topicTitleHi}"
- शाखा/खंड: "${context.branchMeta.hi}" (${context.branchMeta.en})
- URL Slug: "${context.slug}"
- Canonical URL: "${item.url}"

महत्वपूर्ण निर्देश:
1. भाषा: सम्पूर्ण सामग्री शुद्ध, मानक एवं अकादमिक हिन्दी (देवनागरी) में होनी चाहिए।
2. कोई अनावश्यक परिचयात्मक वाक्य न लिखें (जैसे: "इस पाठ में हम पढ़ेंगे...", "यह अध्याय बहुत महत्वपूर्ण है...")। सीधे तथ्यात्मक ज्ञान और नियमों पर केंद्रित रहें।
3. वैचारिक मॉड्यूल (conceptual_modules): केवल 3 तक सीमित न रहें। इस विषय की गहराई और विस्तार के अनुसार जितने आवश्यक हों उतने विस्तृत मॉड्यूल बनाएं (सामान्यतः 4 से 7 मॉड्यूल, जैसे परिभाषा, भेद, प्रमुख सूत्र/नियम, रचनाकार/कालगत प्रवृत्तियां, तुलना, आदि)।
4. प्रत्येक मॉड्यूल में 4 से 6 संक्षिप्त, सटीक, उच्च-मानक बुलेट बिंदु (bullets) दें, जिनमें महत्वपूर्ण शब्द **bold** में हों।
5. प्रमुख नियम/सूत्र (rules_or_sutras): पाणिनीय सूत्र, व्याकरण नियम, या काव्यशास्त्रीय लक्षण/परिभाषाएं (कम से कम 3-5)।
6. अपवाद एवं विशेष तथ्य (critical_exceptions): व्याकरण के अपवाद, विवादास्पद तथ्य, या विद्वानों के भिन्न मत (उदा. शुक्ल जी बनाम हजारी प्रसाद द्विवेदी)।
7. याद रखने की ट्रिक्स एवं सूत्र (tips_and_tricks): परीक्षा में प्रश्नों को तुरंत हल करने के लिए स्मृति सूत्र / ट्रिक्स (कम से कम 3)।
8. तुलनात्मक तालिका (comparison_matrix): संबंधित दो अवधारणाओं (जैसे स्वर संधि vs व्यंजन संधि, उपमा vs रूपक, आदिकाल vs रीतिकाल) की तुलना।

आउटपुट का JSON प्रारूप (केवल शुद्ध JSON दें, कोई अतिरिक्त गपशप नहीं):
{
  "title": "${context.topicTitleHi}: प्रामाणिक अध्ययन नोट्स एवं संकल्पनाएं",
  "short_intro": "इस विषय की मूल परिभाषा और परीक्षा-प्रासंगिक सार (अधिकतम 2 प्रत्यक्ष तथ्यात्मक वाक्य)।",
  "conceptual_modules": [
    {
      "module_title": "विशिष्ट विषय-आधारित शीर्षक 1 (जैसे: परिभाषा, स्वरूप एवं भेद)",
      "bullets": [
        "तथ्यात्मक सारगर्भित बिंदु 1 (प्रमुख शब्द **बोल्ड** में)।",
        "तथ्यात्मक सारगर्भित बिंदु 2।"
      ]
    },
    {
      "module_title": "विशिष्ट विषय-आधारित शीर्षक 2",
      "bullets": [
        "तथ्यात्मक सारगर्भित बिंदु।"
      ]
    }
  ],
  "rules_or_sutras": [
    {
      "name": "नियम / सूत्र / लक्षण का नाम",
      "statement": "नियम या श्लोक/परिभाषा",
      "application": "लागू होने की स्थिति या उदाहरण (जैसे: विद्या + आलय = विद्यालय)"
    }
  ],
  "critical_exceptions": [
    {
      "rule": "सामान्य नियम या प्रचलित मान्यता",
      "exception": "विशिष्ट अपवाद या भिन्न मत",
      "reason": "व्याकरणिक या ऐतिहासिक कारण"
    }
  ],
  "tips_and_tricks": [
    {
      "trick_title": "शॉर्टकट या स्मृति सूत्र का नाम",
      "mnemonic": "स्मृति सूत्र या कोड",
      "application": "परीक्षा में प्रश्नों को शीघ्र हल करने की विधि"
    }
  ],
  "comparison_matrix": {
    "title": "तुलनात्मक विश्लेषण शीर्षक (उदा. यण् संधि एवं अयादि संधि में अंतर)",
    "headers": ["तुलना का आधार", "वर्ग क", "वर्ग ख"],
    "rows": [
      ["नियम/स्थिति", "विवरण क", "विवरण ख"],
      ["प्रमुख उदाहरण", "उदाहरण क", "उदाहरण ख"]
    ]
  },
  "exam_points": [
    "परीक्षा उपयोगी तथ्य 1 (सीधा प्रश्न बनने योग्य बिंदु)",
    "परीक्षा उपयोगी तथ्य 2",
    "परीक्षा उपयोगी तथ्य 3",
    "परीक्षा उपयोगी तथ्य 4",
    "परीक्षा उपयोगी तथ्य 5"
  ]
}`;
}

// ============================================================================
// CALL 2: REVISION, QUIZ, PYQ & TEST PROMPT
// ============================================================================
function buildCall2Prompt(item, context, call1Data) {
  return `आप UP PGT/TGT हिन्दी एवं UGC-NET परीक्षा के वरिष्ठ प्रश्न-पत्र निर्माता (Senior Question Setter) हैं।
विषय "${context.topicTitleHi}" (शाखा: ${context.branchMeta.hi}) के लिए त्वरित पुनरावृत्ति (Revision Summary), अभ्यास प्रश्नोत्तरी (Practice Quiz), विगत वर्षों के प्रश्न (PYQs) और समयबद्ध टॉपिक टेस्ट (Timed Test) तैयार करें।

महत्वपूर्ण निर्देश:
1. भाषा: सम्पूर्ण सामग्री शुद्ध हिन्दी (देवनागरी) में होनी चाहिए।
2. शब्दावली (terms_glossary): 8 से 12 महत्वपूर्ण पारिभाषिक शब्द, उनकी प्रामाणिक परिभाषा और परीक्षा में पूछने का महत्व।
3. स्मरणीय तथ्य (must_remember): 6 से 8 अत्यंत महत्वपूर्ण सूत्र, वर्ष, रचनाएं या व्याकरणिक नियम।
4. मुख्य भ्रम एवं अंतर (common_confusions): 3 से 4 ऐसे बिंदु जहाँ छात्र अक्सर भ्रमित होते हैं (जैसे: कर्मधारय vs बहुव्रीहि, शब्द शक्ति के भेद)।
5. अभ्यास प्रश्नोत्तरी (practice_quiz): 18 से 20 उच्च-स्तरीय वस्तुनिष्ठ प्रश्न (MCQs)। प्रत्येक प्रश्न में 4 स्पष्ट विकल्प, सही उत्तर का इंडेक्स (0 से 3) और विस्तृत प्रामाणिक व्याख्या होनी चाहिए।
6. विगत वर्षों के प्रश्न (pyqs): 5 से 6 प्रामाणिक PYQs (उदा. "UP PGT 2021", "UP PGT 2016", "UP TGT 2021", "UGC NET")।
7. समयबद्ध टेस्ट (topic_test): ठीक 10 उच्च-स्तरीय प्रश्न।

आउटपुट का JSON प्रारूप (केवल शुद्ध JSON दें):
{
  "quick_revision": {
    "terms_glossary": [
      {
        "term": "पारिभाषिक शब्द",
        "category": "व्याकरण / साहित्य / काव्यशास्त्र",
        "definition": "1-2 वाक्यों में सटीक मानक परिभाषा।"
      }
    ],
    "must_remember": [
      "स्मरणीय मुख्य सूत्र या तथ्य 1",
      "स्मरणीय मुख्य सूत्र या तथ्य 2"
    ],
    "common_confusions": [
      {
        "term_a": "अवधारणा क",
        "term_b": "अवधारणा ख",
        "difference": "दोनों में स्पष्ट विभेदक तत्व।"
      }
    ]
  },
  "practice_quiz": [
    {
      "question": "विशिष्ट वैचारिक वस्तुनिष्ठ प्रश्न?",
      "options": ["विकल्प क", "विकल्प ख", "विकल्प ग", "विकल्प घ"],
      "correct_index": 0,
      "explanation": "विस्तृत एवं प्रामाणिक देवनागरी व्याख्या।"
    }
  ],
  "pyqs": [
    {
      "exam_tag": "UP PGT 2021",
      "question": "विगत वर्ष का प्रामाणिक प्रश्न?",
      "options": ["विकल्प क", "विकल्प ख", "विकल्प ग", "विकल्प घ"],
      "correct_index": 0,
      "explanation": "प्रामाणिक उत्तर व्याख्या।"
    }
  ],
  "topic_test": [
    {
      "question": "समयबद्ध टेस्ट का विश्लेषणात्मक प्रश्न?",
      "options": ["विकल्प क", "विकल्प ख", "विकल्प ग", "विकल्प घ"],
      "correct_index": 0,
      "explanation": "स्पष्टीकरण एवं समाधान।"
    }
  ]
}`;
}

// ============================================================================
// HTML COMPILER (5 Tabs, Hindi Styling with Burgundy Accent & Topic CSS)
// ============================================================================
function renderHindiTopicHtml(item, context, call1, call2) {
  const canonicalUrl = `https://sjmaths.com${item.url}`;
  const cleanTitle = context.topicTitleHi;
  const pageTitle = `${cleanTitle} — सम्पूर्ण अध्ययन नोट्स, नियम, PYQs एवं टेस्ट | UP PGT हिन्दी`;
  const metaDesc = `${cleanTitle} (${context.branchMeta.hi}): मुख्य नियम, अपवाद, परीक्षा ट्रिक्स, 20 अभ्यास प्रश्न, PYQs और 10 मिनट का समयबद्ध टेस्ट।`;

  // Schema.org Structured Data
  const schemaJsonLd = {
    "@context": "https://schema.org",
    "@type": "LearningResource",
    "name": cleanTitle,
    "headline": `${cleanTitle} — UP PGT हिन्दी अध्ययन मार्गदर्शिका`,
    "description": metaDesc,
    "url": canonicalUrl,
    "inLanguage": "hi",
    "learningResourceType": "Study Guide / Quiz",
    "educationalLevel": "Postgraduate Teacher Recruitment / B.A. & M.A. Hindi",
    "isPartOf": {
      "@type": "WebSite",
      "name": "SJ Maths",
      "url": "https://sjmaths.com/"
    },
    "breadcrumb": {
      "@type": "BreadcrumbList",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://sjmaths.com/" },
        { "@type": "ListItem", "position": 2, "name": "UP PGT हिन्दी", "item": "https://sjmaths.com/up-pgt-hindi/" },
        { "@type": "ListItem", "position": 3, "name": context.branchMeta.hi, "item": `https://sjmaths.com/hindi/${context.branchKey}/` },
        { "@type": "ListItem", "position": 4, "name": cleanTitle, "item": canonicalUrl }
      ]
    }
  };

  // TAB 1: STUDY NOTES (Dynamic Conceptual Modules)
  let modulesHtml = '';
  if (Array.isArray(call1.conceptual_modules) && call1.conceptual_modules.length > 0) {
    modulesHtml = call1.conceptual_modules.map((m, idx) => `
      <section class="notes-section" id="note-sec-${idx + 1}">
        <h2>${idx + 1}. ${m.module_title}</h2>
        <div class="prose-content">
          <ul class="notes-bullet-list">
            ${(m.bullets || []).map(b => `<li>${b}</li>`).join('')}
          </ul>
        </div>
      </section>
    `).join('');
  }

  // Rules / Sutras Card Grid
  let rulesHtml = '';
  if (Array.isArray(call1.rules_or_sutras) && call1.rules_or_sutras.length > 0) {
    const cards = call1.rules_or_sutras.map(r => `
      <div class="formula-card">
        <div class="formula-name">${r.name}</div>
        <div class="formula-eq" style="font-family:'Noto Sans Devanagari',sans-serif;font-size:1.05rem;font-weight:700;color:var(--brand);">${r.statement}</div>
        <div class="formula-meta">
          <div><strong>प्रयोग / उदाहरण:</strong> ${r.application}</div>
        </div>
      </div>
    `).join('');

    rulesHtml = `
      <div class="formula-sheet-box">
        <div class="formula-sheet-title">📜 प्रमुख नियम, सूत्र एवं लक्षण</div>
        <div class="formula-grid">${cards}</div>
      </div>
    `;
  }

  // Critical Exceptions
  let exceptionsHtml = '';
  if (Array.isArray(call1.critical_exceptions) && call1.critical_exceptions.length > 0) {
    const list = call1.critical_exceptions.map(e => `
      <div class="exception-card">
        <div class="exception-head">
          <span class="exception-badge">अपवाद / विशेष</span>
          <span class="exception-rule">${e.rule}</span>
        </div>
        <p class="exception-detail"><strong>विशिष्ट स्थिति:</strong> ${e.exception} — <em>${e.reason}</em></p>
      </div>
    `).join('');

    exceptionsHtml = `
      <div class="exception-alert-box">
        <div class="exception-alert-title">⚠️ महत्वपूर्ण अपवाद एवं परीक्षा-विशेष तथ्य</div>
        <div class="exception-list">${list}</div>
      </div>
    `;
  }

  // Tips & Mnemonics
  let tricksHtml = '';
  if (Array.isArray(call1.tips_and_tricks) && call1.tips_and_tricks.length > 0) {
    const list = call1.tips_and_tricks.map(t => `
      <div class="trick-card">
        <div class="trick-title">${t.trick_title}</div>
        <div class="trick-shortcut" style="background:var(--accent-soft);color:var(--accent);">${t.mnemonic}</div>
        <p class="trick-app"><strong>परीक्षा अनुप्रयोग:</strong> ${t.application}</p>
      </div>
    `).join('');

    tricksHtml = `
      <div class="trick-box">
        <div class="trick-box-title">💡 स्मृति सूत्र एवं शॉर्टकट ट्रिक्स</div>
        <div class="tricks-grid">${list}</div>
      </div>
    `;
  }

  // Comparison Matrix
  let comparisonHtml = '';
  if (call1.comparison_matrix && Array.isArray(call1.comparison_matrix.headers)) {
    const m = call1.comparison_matrix;
    const ths = m.headers.map(h => `<th>${h}</th>`).join('');
    const trs = (m.rows || []).map(r => `<tr>${r.map(c => `<td>${c}</td>`).join('')}</tr>`).join('');

    comparisonHtml = `
      <div class="comparison-card">
        <div class="comparison-title">${m.title || 'तुलनात्मक विश्लेषण'}</div>
        <div class="table-responsive">
          <table class="styled-table">
            <thead><tr>${ths}</tr></thead>
            <tbody>${trs}</tbody>
          </table>
        </div>
      </div>
    `;
  }

  // Exam Points
  let examPointsHtml = '';
  if (Array.isArray(call1.exam_points) && call1.exam_points.length > 0) {
    examPointsHtml = `
      <div class="exam-points-card">
        <div class="exam-points-title">🎯 मुख्य परीक्षा बिंदु (Direct Exam Points)</div>
        <ul class="exam-points-list">
          ${call1.exam_points.map(p => `<li>${p}</li>`).join('')}
        </ul>
      </div>
    `;
  }

  // TAB 2: REVISION SUMMARY & GLOSSARY
  const qr = call2.quick_revision || {};
  let glossaryHtml = '';
  if (Array.isArray(qr.terms_glossary) && qr.terms_glossary.length > 0) {
    glossaryHtml = qr.terms_glossary.map(t => `
      <div class="glossary-item">
        <div class="glossary-term-wrap">
          <span class="glossary-term">${t.term}</span>
          ${t.category ? `<span class="glossary-term-en">(${t.category})</span>` : ''}
        </div>
        <div class="glossary-def">${t.definition}</div>
      </div>
    `).join('');
  }

  let mustRememberHtml = '';
  if (Array.isArray(qr.must_remember) && qr.must_remember.length > 0) {
    mustRememberHtml = qr.must_remember.map(item => `<li>${item}</li>`).join('');
  }

  let confusionsHtml = '';
  if (Array.isArray(qr.common_confusions) && qr.common_confusions.length > 0) {
    confusionsHtml = qr.common_confusions.map(cf => `
      <div class="confusion-item">
        <div class="confusion-terms">
          <span class="conf-badge-a">${cf.term_a}</span>
          <span class="conf-vs">VS</span>
          <span class="conf-badge-b">${cf.term_b}</span>
        </div>
        <p class="confusion-diff">${cf.difference}</p>
      </div>
    `).join('');
  }

  // TAB 3: PRACTICE QUIZ (18-20 MCQs)
  const letters = ['क', 'ख', 'ग', 'घ'];
  let quizCardsHtml = '';
  const quizList = call2.practice_quiz || [];
  quizList.forEach((q, idx) => {
    const opts = (q.options || []).map((opt, oIdx) => `
      <button type="button" class="quiz-option-btn" data-qindex="${idx}" data-optindex="${oIdx}">
        <span class="option-letter">${letters[oIdx]}</span>
        <span class="option-text">${opt}</span>
      </button>
    `).join('');

    quizCardsHtml += `
      <div class="quiz-question-card" id="q-card-${idx}" data-correct="${q.correct_index ?? 0}">
        <div class="q-header">
          <span class="q-number">प्रश्न ${idx + 1} / ${quizList.length}</span>
        </div>
        <h3 class="q-text">${q.question || 'अभ्यास प्रश्न'}</h3>
        <div class="quiz-options-group">${opts}</div>
        <div class="q-feedback hidden" id="feedback-${idx}">
          <div class="feedback-indicator"></div>
          <p class="feedback-explanation"><strong>व्याख्या:</strong> ${q.explanation || 'प्रामाणिक उत्तर एवं व्याख्या।'}</p>
        </div>
      </div>
    `;
  });

  // TAB 4: PREVIOUS YEARS QUESTIONS (PYQs)
  let pyqCardsHtml = '';
  const pyqList = Array.isArray(call2.pyqs) && call2.pyqs.length > 0
    ? call2.pyqs
    : (quizList).slice(0, 6);

  pyqList.forEach((q, idx) => {
    const opts = (q.options || []).map((opt, oIdx) => `
      <button type="button" class="quiz-option-btn" data-pyqindex="${idx}" data-optindex="${oIdx}">
        <span class="option-letter">${letters[oIdx]}</span>
        <span class="option-text">${opt}</span>
      </button>
    `).join('');

    const correctIdx = (typeof q.correct_index === 'number' && q.correct_index >= 0 && q.correct_index < 4) ? q.correct_index : 0;
    const correctOptText = (q.options || [])[correctIdx] || '';

    pyqCardsHtml += `
      <div class="pyq-card" id="pyq-card-${idx}" data-correct="${correctIdx}">
        <div class="pyq-header-meta">
          <span class="pyq-badge">${q.exam_tag || 'UP PGT Hindi'}</span>
        </div>
        <div class="pyq-question-text">${q.question || 'विगत वर्ष प्रश्न'}</div>
        <div class="quiz-options-group">${opts}</div>
        <div class="pyq-expl-box hidden" id="pyq-expl-${idx}">
          <strong>उत्तर: विकल्प (${letters[correctIdx]}) — ${correctOptText}</strong>
          <span>${q.explanation || ''}</span>
        </div>
      </div>
    `;
  });

  // TAB 5: TIMED TOPIC TEST (10 MCQs)
  let testCardsHtml = '';
  const testList = call2.topic_test || [];
  testList.forEach((t, idx) => {
    const opts = (t.options || []).map((opt, oIdx) => `
      <button type="button" class="test-option-btn" data-tindex="${idx}" data-optindex="${oIdx}">
        <span class="option-letter">${letters[oIdx]}</span>
        <span class="option-text">${opt}</span>
      </button>
    `).join('');

    testCardsHtml += `
      <div class="test-question-card" id="t-card-${idx}" data-correct="${t.correct_index ?? 0}">
        <div class="test-q-header">
          <span class="t-badge">प्रश्न ${idx + 1} / ${testList.length}</span>
        </div>
        <div class="test-question-text">${t.question || 'परीक्षण प्रश्न'}</div>
        <div class="test-options-grid">${opts}</div>
        <div class="t-feedback hidden" id="t-feedback-${idx}">
          <p class="feedback-explanation"><strong>समाधान:</strong> ${t.explanation || 'उत्तर व्याख्या।'}</p>
        </div>
      </div>
    `;
  });

  // Sidebar Related Links
  let relatedHtml = '';
  if (context.related && context.related.length > 0) {
    relatedHtml = context.related.map(r => `
      <a href="${r.url}">
        <span>${r.title}</span>
        <span>→</span>
      </a>
    `).join('');
  }

  return `<!doctype html>
<html lang="hi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>${pageTitle}</title>
<meta name="description" content="${metaDesc}">
<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1">
<meta name="author" content="SJ Maths">
<meta name="theme-color" content="#7f1d1d">
<link rel="canonical" href="${canonicalUrl}">
<link rel="icon" type="image/png" href="/favicon.png">

<!-- OpenGraph Metadata -->
<meta property="og:type" content="article">
<meta property="og:site_name" content="SJ Maths">
<meta property="og:title" content="${cleanTitle} — UP PGT हिन्दी नोट्स एवं प्रश्नोत्तरी">
<meta property="og:description" content="${metaDesc}">
<meta property="og:url" content="${canonicalUrl}">

<!-- Twitter Card Metadata -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="${cleanTitle} | UP PGT Hindi">
<meta name="twitter:description" content="${metaDesc}">

<!-- JSON-LD Structured Data -->
<script type="application/ld+json">
${JSON.stringify(schemaJsonLd, null, 2)}
</script>

<!-- Unified Topic Stylesheet -->
<link rel="stylesheet" href="/assets/css/topic-page.css">

<!-- Hindi Palette & Typography Theme Override -->
<style>
:root {
  --brand: #7f1d1d;
  --brand-dark: #450a0a;
  --brand-light: #991b1b;
  --accent: #9f1239;
  --accent-hover: #881337;
  --accent-soft: rgba(159, 18, 57, 0.08);
  --accent-border: rgba(159, 18, 57, 0.24);
}
html.dark, body.dark-mode {
  --brand: #fca5a5;
  --brand-dark: #fecdd3;
  --brand-light: #f87171;
  --accent: #fb7185;
  --accent-hover: #fda4af;
  --accent-soft: rgba(251, 113, 133, 0.14);
  --accent-border: rgba(251, 113, 133, 0.35);
}
body {
  font-family: "Noto Sans Devanagari", "Nirmala UI", "Mangal", Inter, sans-serif;
  line-height: 1.65;
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
      <span class="brand-mark" style="background: linear-gradient(145deg, #7f1d1d, #9f1239); font-family: serif; font-size: 1.35rem; font-style: italic; display: flex; align-items: center; justify-content: center;">&int;</span>
      <span>
        <span class="brand-name">SJ Maths</span>
        <span class="brand-sub">हिन्दी विषय</span>
      </span>
    </a>
    <div class="header-actions">
      <button type="button" class="theme-toggle-btn" id="btn-theme-toggle" aria-label="Toggle Dark Mode">🌙 Dark Mode</button>
      <a class="back-btn" href="/up-pgt-hindi/" title="UP PGT Hindi Tracker">← UP PGT<span class="desk-only"> हिन्दी</span></a>
    </div>
  </div>
</header>

<main class="wrap">
  <!-- Hero Section -->
  <section class="hero">
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="https://sjmaths.com/">Home</a>
      <span class="breadcrumb-sep">›</span>
      <a href="/up-pgt-hindi/">UP PGT हिन्दी</a>
      <span class="breadcrumb-sep">›</span>
      <a href="/hindi/${context.branchKey}/">${context.branchMeta.hi}</a>
      <span class="breadcrumb-sep">›</span>
      <span aria-current="page">${cleanTitle}</span>
    </nav>
    <div class="kicker" style="color: #9f1239; font-weight: 800;">${context.branchMeta.hi}</div>
    <h1>${cleanTitle}</h1>
    <p class="lead">${call1.short_intro}</p>

    <div class="exam-badges">
      <a class="exam-chip pgt" href="/up-pgt-hindi/">UP PGT हिन्दी</a>
      <a class="exam-chip both" href="/up-tgt-hindi/">UP TGT हिन्दी</a>
      <span class="exam-chip both">विषय कोड 04 • B.A./M.A. स्तर</span>
    </div>
  </section>

  <!-- Interactive Learning Navigation Tabs (5 Tabs) -->
  <div class="study-tabs-sticky-wrapper">
    <div class="study-tabs" role="tablist" aria-label="Study Module Tabs">
      <button type="button" class="tab-btn active" role="tab" aria-selected="true" data-tab="tab-notes" id="tab-btn-notes">
        <span>📖</span> <span>अध्ययन नोट्स</span>
      </button>
      <button type="button" class="tab-btn" role="tab" aria-selected="false" data-tab="tab-summary" id="tab-btn-summary">
        <span>⚡</span> <span>त्वरित पुनरावृत्ति</span>
      </button>
      <button type="button" class="tab-btn" role="tab" aria-selected="false" data-tab="tab-quiz" id="tab-btn-quiz">
        <span>❓</span> <span>अभ्यास प्रश्न</span> <span class="tab-badge">${quizList.length}Q</span>
      </button>
      <button type="button" class="tab-btn" role="tab" aria-selected="false" data-tab="tab-pyqs" id="tab-btn-pyqs">
        <span>🏛️</span> <span>विगत वर्ष प्रश्न (PYQ)</span>
      </button>
      <button type="button" class="tab-btn" role="tab" aria-selected="false" data-tab="tab-test" id="tab-btn-test">
        <span>⏱️</span> <span>समयबद्ध टेस्ट</span> <span class="tab-badge">${testList.length}Q</span>
      </button>
    </div>
  </div>

  <!-- Main Grid Layout -->
  <div class="main-grid">
    <div class="content-col">

      <!-- TAB 1: STUDY NOTES -->
      <article class="tab-panel active" id="tab-notes" role="tabpanel" aria-labelledby="tab-btn-notes">
        ${modulesHtml}
        ${rulesHtml}
        ${exceptionsHtml}
        ${tricksHtml}
        ${comparisonHtml}
        ${examPointsHtml}
      </article>

      <!-- TAB 2: REVISION SUMMARY & GLOSSARY -->
      <article class="tab-panel hidden" id="tab-summary" role="tabpanel" aria-labelledby="tab-btn-summary">
        <div class="summary-container">
          <div class="summary-hero-box" style="background: linear-gradient(135deg, #7f1d1d 0%, #9f1239 100%); color: #fff; padding: 20px; border-radius: 12px; margin-bottom: 20px;">
            <h2 style="color:#fff;margin-top:0;">⚡ त्वरित पुनरावृत्ति: ${cleanTitle}</h2>
            <p style="color:#fecdd3;margin:0;">प्रमुख नियम, पारिभाषिक शब्दावली और परीक्षा में पूछे जाने वाले सूक्ष्म अंतर।</p>
          </div>
        </div>

        <div class="revision-container">
          ${glossaryHtml ? `
          <div class="revision-card-box">
            <h2>📚 पारिभाषिक शब्दावली (Key Terms)</h2>
            <div class="glossary-grid">
              ${glossaryHtml}
            </div>
          </div>` : ''}

          ${mustRememberHtml ? `
          <div class="revision-card-box highlight" style="margin-top:20px;">
            <h2>🎯 अनिवार्य स्मरणीय तथ्य (Must Remember)</h2>
            <ul class="must-remember-list">
              ${mustRememberHtml}
            </ul>
          </div>` : ''}

          ${confusionsHtml ? `
          <div class="revision-card-box diff" style="margin-top:20px;">
            <h2>⚖️ सूक्ष्म अंतर एवं सामान्य भ्रम (Common Confusions)</h2>
            <div class="confusions-grid">
              ${confusionsHtml}
            </div>
          </div>` : ''}
        </div>
      </article>

      <!-- TAB 3: PRACTICE QUIZ -->
      <article class="tab-panel hidden" id="tab-quiz" role="tabpanel" aria-labelledby="tab-btn-quiz">
        <div class="quiz-panel-header">
          <div class="quiz-panel-title">
            <h2>❓ वस्तुनिष्ठ अभ्यास प्रश्न (${quizList.length} MCQs)</h2>
            <p>उत्तर चुनकर तत्काल अपनी तैयारी और व्याख्या की जांच करें।</p>
          </div>
          <div class="quiz-live-scoreboard">
            <div class="score-pill">स्कोर: <span id="quizScore">0</span> / ${quizList.length}</div>
            <button type="button" class="btn-reset-quiz" id="btnResetQuiz">पुनः हल करें</button>
          </div>
        </div>

        <div class="quiz-questions-list">
          ${quizCardsHtml}
        </div>
      </article>

      <!-- TAB 4: PREVIOUS YEARS QUESTIONS (PYQs) -->
      <article class="tab-panel hidden" id="tab-pyqs" role="tabpanel" aria-labelledby="tab-btn-pyqs">
        <div class="pyq-trend-card">
          <h2>🏛️ परीक्षा रुझान एवं विगत वर्षों के प्रश्न</h2>
          <p>UP PGT / TGT हिन्दी में <strong>${cleanTitle}</strong> से पूछे गए वास्तविक प्रश्न एवं प्रारूप।</p>
          <div class="pyq-trend-grid">
            <div class="pyq-stat-item">
              <span class="pyq-stat-val">2–4</span>
              <span class="pyq-stat-label">अपेक्षित प्रश्न</span>
            </div>
            <div class="pyq-stat-item">
              <span class="pyq-stat-val">उच्च</span>
              <span class="pyq-stat-label">महत्व (Yield)</span>
            </div>
            <div class="pyq-stat-item">
              <span class="pyq-stat-val">मध्यम-कठिन</span>
              <span class="pyq-stat-label">कठिनाई स्तर</span>
            </div>
          </div>
        </div>

        <div class="pyq-questions-list">
          ${pyqCardsHtml}
        </div>
      </article>

      <!-- TAB 5: TIMED TOPIC TEST (10 MCQs / 10 Minutes) -->
      <article class="tab-panel hidden" id="tab-test" role="tabpanel" aria-labelledby="tab-btn-test">
        <div class="test-panel-header">
          <div>
            <h2>⏱️ समयबद्ध टॉपिक टेस्ट</h2>
            <p>10 प्रश्न &bull; 10 मिनट &bull; वास्तविक परीक्षा जैसा अनुभव</p>
          </div>
          <div class="test-timer-badge" id="testTimerBadge">
            <span class="timer-icon">⏳</span> <span id="timerDisplay">10:00</span>
          </div>
        </div>

        <div class="test-instruction-box" id="testStartWrap">
          <h3>निर्देश</h3>
          <ul>
            <li><strong>कुल प्रश्न:</strong> 10 वस्तुनिष्ठ प्रश्न</li>
            <li><strong>निर्धारित समय:</strong> 10 मिनट</li>
            <li><strong>अंकन:</strong> प्रत्येक सही उत्तर पर +1 अंक, नकारात्मक अंकन नहीं</li>
          </ul>
          <button type="button" class="btn-start-test" id="btnStartTest" style="background: linear-gradient(135deg, #7f1d1d, #9f1239);">टेस्ट प्रारंभ करें</button>
        </div>

        <div class="test-active-container hidden" id="testActiveWrap">
          <div class="test-questions-list">
            ${testCardsHtml}
          </div>
          <div class="test-submit-bar">
            <button type="button" class="btn-submit-test" id="btnSubmitTest" style="background: #9f1239;">टेस्ट जमा करें</button>
          </div>
        </div>

        <div class="test-result-modal hidden" id="testResultModal">
          <div class="result-card">
            <h3>टेस्ट परिणाम (Result)</h3>
            <div class="result-score-circle" style="background: linear-gradient(135deg, #7f1d1d, #9f1239);">
              <span id="resFinalScore">0</span> / 10
            </div>
            <p id="resFeedbackText">सभी प्रश्नों के विस्तृत समाधान ऊपर देखें।</p>
            <button type="button" class="btn-retake-test" id="btnRetakeTest" style="background: #9f1239;">पुनः टेस्ट दें</button>
          </div>
        </div>
      </article>

      <!-- Bottom Pagination -->
      <nav class="topic-pagination" aria-label="Topic Navigation">
        <a class="topic-nav-btn next" href="/up-pgt-hindi/"><span>परीक्षा ट्रैकर →</span> <strong>UP PGT हिन्दी सम्पूर्ण पाठ्यक्रम</strong></a>
      </nav>

    </div>

    <!-- Sticky Sidebar -->
    <aside class="sidebar-col">
      <div class="sidebar-card side-card">
        <div class="side-card-header">
          <span class="side-badge">पाठ्यक्रम खंड</span>
          <h3>${context.branchMeta.hi}</h3>
        </div>
        <p class="side-desc">UP PGT हिन्दी विषय कोड 04 के अंतर्गत निर्धारित अध्ययन सामग्री।</p>
        <div class="side-nav-links">
          ${relatedHtml}
        </div>
        <div class="side-action-box">
          <a class="side-action-btn" href="/up-pgt-hindi/" style="background: #7f1d1d;">पूर्ण हिन्दी ट्रैकर खोलें →</a>
        </div>
      </div>
    </aside>
  </div>
</main>

<footer class="site-footer">
  <div class="wrap footer-inner">
    <div>
      <p><strong>SJ Maths — हिन्दी अध्ययन</strong></p>
      <p>UP PGT हिन्दी (Subject Code 04) एवं UP TGT हिन्दी परीक्षा तैयारी सामग्री।</p>
    </div>
    <div class="footer-links">
      <a href="https://sjmaths.com/">Home</a>
      <a href="/up-pgt-hindi/">UP PGT हिन्दी</a>
      <a href="/up-tgt-hindi/">UP TGT हिन्दी</a>
      <a href="/privacy-policy/">Privacy Policy</a>
    </div>
  </div>
</footer>

<!-- Interactive Client-side Controller (Tabs, Quiz, PYQs, Timer) -->
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

      const letters = ['क', 'ख', 'ग', 'घ'];
      if (optIndex === correctIndex) {
        quizScore++;
        if (statusEl) {
          statusEl.textContent = '✓ सही उत्तर!';
          statusEl.className = 'feedback-indicator correct';
        }
        if (feedback) feedback.className = 'q-feedback correct';
      } else {
        if (statusEl) {
          statusEl.textContent = '✗ गलत उत्तर। सही विकल्प: ' + letters[correctIndex];
          statusEl.className = 'feedback-indicator incorrect';
        }
        if (feedback) feedback.className = 'q-feedback incorrect';
      }
      if (feedback) feedback.classList.remove('hidden');
      const scoreEl = document.getElementById('quizScore');
      if (scoreEl) scoreEl.textContent = quizScore;
    });
  });

  const btnResetQuiz = document.getElementById('btnResetQuiz');
  if (btnResetQuiz) {
    btnResetQuiz.addEventListener('click', () => {
      quizScore = 0;
      answeredQuestions.clear();
      const scoreEl = document.getElementById('quizScore');
      if (scoreEl) scoreEl.textContent = '0';
      document.querySelectorAll('.quiz-option-btn').forEach(b => {
        b.disabled = false;
        b.classList.remove('correct', 'incorrect');
      });
      document.querySelectorAll('.q-feedback').forEach(f => {
        f.classList.add('hidden');
        f.classList.remove('correct', 'incorrect');
      });
    });
  }

  // Timed Topic Test Logic
  let testTimer = null;
  let secondsLeft = 600;
  const btnStartTest = document.getElementById('btnStartTest');
  const testStartWrap = document.getElementById('testStartWrap');
  const testActiveWrap = document.getElementById('testActiveWrap');
  const timerDisplay = document.getElementById('timerDisplay');

  if (btnStartTest) {
    btnStartTest.addEventListener('click', () => {
      if (testStartWrap) testStartWrap.classList.add('hidden');
      if (testActiveWrap) testActiveWrap.classList.remove('hidden');
      testTimer = setInterval(() => {
        secondsLeft--;
        const mins = Math.floor(secondsLeft / 60);
        const secs = secondsLeft % 60;
        if (timerDisplay) {
          timerDisplay.textContent = (mins < 10 ? '0' : '') + mins + ':' + (secs < 10 ? '0' : '') + secs;
        }
        if (secondsLeft <= 0) {
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

// ============================================================================
// TOPIC PROCESSOR (2-CALL ARCHITECTURE with gemini-3.5-flash-lite)
// ============================================================================
async function processHindiTopic(item) {
  const context = getTopicContext(item);
  console.log(`\n============================================================`);
  console.log(`विषय: ${context.topicTitleHi} (${item.url})`);
  console.log(`खंड: ${context.branchMeta.hi} | मॉडल: ${MODEL_NAME}`);

  if (DRY_RUN) {
    console.log(`[DRY RUN] Would process: ${item.url}`);
    return true;
  }

  statusMap[item.url] = {
    status: 'generating',
    startedAt: new Date().toISOString()
  };
  saveStatus();

  // --- API CALL 1: STUDY NOTES ---
  console.log(`\n--- [कॉल 1/2] अध्ययन नोट्स (Study Notes) उत्पन्न कर रहे हैं... ---`);
  const call1Prompt = buildCall1Prompt(item, context);
  let call1Data = null;
  const maxRetries = 6;

  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    const clientObj = getClient();
    try {
      console.log(`Gemini Call 1 API [कुंजी: #${clientObj.id} (${clientObj.preview})] (प्रयास ${attempt}/${maxRetries})...`);
      const response = await clientObj.client.models.generateContent({
        model: MODEL_NAME,
        contents: call1Prompt,
        config: {
          responseMimeType: 'application/json',
          temperature: 0.3,
          maxOutputTokens: 32768
        }
      });

      const rawJson = cleanRawJson(response.text);
      try {
        call1Data = JSON.parse(rawJson);
      } catch (e) {
        call1Data = JSON.parse(jsonrepair(rawJson));
      }

      call1Data = cleanMarkdownStars(call1Data);
      if (!call1Data.title || !Array.isArray(call1Data.conceptual_modules) || call1Data.conceptual_modules.length === 0) {
        throw new Error('Call 1 schema validation failed: missing title or conceptual_modules');
      }
      console.log(`✓ कॉल 1 सफल! उत्पन्न मॉड्यूल की संख्या: ${call1Data.conceptual_modules.length}`);
      break;
    } catch (err) {
      console.error(`कॉल 1 प्रयास ${attempt} असफल:`, err.message);
      if (attempt === maxRetries) {
        statusMap[item.url] = {
          status: 'call1_failed',
          error: err.message,
          failedAt: new Date().toISOString()
        };
        saveStatus();
        return false;
      }
      const wait = err.message.includes('429') || err.message.includes('503') ? 12000 : GAP_MS;
      await new Promise(r => setTimeout(r, wait));
    }
  }

  // Small pause between call 1 and call 2
  await new Promise(r => setTimeout(r, GAP_MS));

  // --- API CALL 2: REVISION, QUIZ, PYQs & TEST ---
  console.log(`\n--- [कॉल 2/2] पुनरावृत्ति, प्रश्नोत्तरी, PYQs एवं टेस्ट उत्पन्न कर रहे हैं... ---`);
  const call2Prompt = buildCall2Prompt(item, context, call1Data);
  let call2Data = null;

  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    const clientObj = getClient();
    try {
      console.log(`Gemini Call 2 API [कुंजी: #${clientObj.id} (${clientObj.preview})] (प्रयास ${attempt}/${maxRetries})...`);
      const response = await clientObj.client.models.generateContent({
        model: MODEL_NAME,
        contents: call2Prompt,
        config: {
          responseMimeType: 'application/json',
          temperature: 0.3,
          maxOutputTokens: 32768
        }
      });

      const rawJson = cleanRawJson(response.text);
      try {
        call2Data = JSON.parse(rawJson);
      } catch (e) {
        call2Data = JSON.parse(jsonrepair(rawJson));
      }

      normalizeQuestions(call2Data.practice_quiz);
      normalizeQuestions(call2Data.pyqs);
      normalizeQuestions(call2Data.topic_test);

      call2Data = cleanMarkdownStars(call2Data);

      if (!Array.isArray(call2Data.practice_quiz) || call2Data.practice_quiz.length < 12) {
        throw new Error(`Call 2 validation failed: practice_quiz count insufficient (${call2Data.practice_quiz?.length})`);
      }
      console.log(`✓ कॉल 2 सफल! प्रश्न: ${call2Data.practice_quiz.length} MCQs, टेस्ट: ${call2Data.topic_test?.length || 0} MCQs`);
      break;
    } catch (err) {
      console.error(`कॉल 2 प्रयास ${attempt} असफल:`, err.message);
      if (attempt === maxRetries) {
        statusMap[item.url] = {
          status: 'call2_failed',
          error: err.message,
          failedAt: new Date().toISOString()
        };
        saveStatus();
        return false;
      }
      const wait = err.message.includes('429') || err.message.includes('503') ? 12000 : GAP_MS;
      await new Promise(r => setTimeout(r, wait));
    }
  }

  // Target directory save
  const targetDir = path.resolve(item.dir);
  fs.mkdirSync(targetDir, { recursive: true });

  // Save auxiliary JSON assets
  fs.writeFileSync(path.join(targetDir, 'quiz.json'), JSON.stringify(call2Data.practice_quiz, null, 2), 'utf8');
  fs.writeFileSync(path.join(targetDir, 'topic-test.json'), JSON.stringify(call2Data.topic_test, null, 2), 'utf8');
  if (call2Data.pyqs) {
    fs.writeFileSync(path.join(targetDir, 'pyq.json'), JSON.stringify(call2Data.pyqs, null, 2), 'utf8');
  }

  // Render & write complete Topic HTML
  const targetHtmlPath = path.join(targetDir, 'index.html');
  const finalHtml = renderHindiTopicHtml(item, context, call1Data, call2Data);
  fs.writeFileSync(targetHtmlPath, finalHtml, 'utf8');
  console.log(`✓ सफलतापूर्वक पृष्ठ सहेजा गया: ${targetHtmlPath}`);

  statusMap[item.url] = {
    status: 'completed',
    title: context.topicTitleHi,
    modulesCount: call1Data.conceptual_modules.length,
    quizCount: call2Data.practice_quiz.length,
    testCount: call2Data.topic_test ? call2Data.topic_test.length : 0,
    completedAt: new Date().toISOString()
  };
  saveStatus();

  return true;
}

// ============================================================================
// MAIN LOOP
// ============================================================================
async function main() {
  console.log('=== SJ Maths — UP PGT / TGT हिन्दी कंटेंट जनरेटर (2-Call Pipeline) ===');
  console.log(`अनिवार्य मॉडल: ${MODEL_NAME}`);
  console.log(`कुल खोजे गए हिन्दी विषय: ${allHindiTopics.length}`);

  const eligible = getEligibleTopics();
  console.log(`प्रसंस्करण हेतु उपलब्ध विषय: ${eligible.length}`);

  const toProcess = LIMIT ? eligible.slice(0, LIMIT) : eligible;
  console.log(`इस सत्र में निष्पादित होने वाले विषय: ${toProcess.length}`);

  let successCount = 0;
  for (let i = 0; i < toProcess.length; i++) {
    const item = toProcess[i];
    console.log(`\n[${i + 1}/${toProcess.length}] प्रारंभ: ${item.url}`);

    let ok = false;
    try {
      ok = await processHindiTopic(item);
    } catch (err) {
      console.error(`अपेक्षित त्रुटि ${item.url}:`, err);
      statusMap[item.url] = {
        status: 'error',
        error: err.message,
        failedAt: new Date().toISOString()
      };
      saveStatus();
    }
    if (ok) successCount++;

    if (i < toProcess.length - 1 && !DRY_RUN && GAP_MS > 0) {
      console.log(`अगले विषय से पूर्व ${GAP_MS / 1000}s प्रतीक्षा...`);
      await new Promise(r => setTimeout(r, GAP_MS));
    }
  }

  console.log('\n============================================================');
  console.log(`संपन्न! सफलतापूर्वक पूर्ण किए गए: ${successCount}/${toProcess.length}`);
}

main().catch(err => {
  console.error('Fatal Hindi Generator Error:', err);
  process.exit(1);
});
