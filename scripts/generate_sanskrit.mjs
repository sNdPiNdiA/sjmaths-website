#!/usr/bin/env node
/**
 * ============================================================================
 * SJ Maths — Sanskrit Content Generator Pipeline (UP PGT / TGT Sanskrit)
 * Target: UP PGT Sanskrit (Subject Code 05), UP TGT Sanskrit, UGC-NET
 * Model: gemini-3.5-flash-lite only
 * Language: High-Standard Academic Sanskrit & Hindi (देवनागरी लिपि / शास्त्रीय संस्कृत)
 * Architecture:
 *   - Two API Calls per Topic:
 *       Call 1: Exhaustive Study Notes (Dynamic conceptual modules /
 *               विशिष्ट प्रतिपाद्य विषय, पाणिनीय सूत्राणि / कारिका,
 *               अपवादाः / विशेषाः, स्मरणसूत्राणि / युक्ति-प्रणाल्यः).
 *       Call 2: Quick Revision Summary (पारिभाषिक शब्दावली, मुख्य स्मरणीय बिन्दवः),
 *               Practice Quiz (18-20 MCQs with instant Sanskrit/Hindi feedback),
 *               PYQs (5-6 MCQs), and Timed Test (10 MCQs).
 * ============================================================================
 */

import fs from 'fs';
import path from 'path';
import 'dotenv/config';
import { GoogleGenAI } from '@google/genai';
import { jsonrepair } from 'jsonrepair';

// Parse CLI arguments early
const args = process.argv.slice(2);
function getArg(flag) {
  const idx = args.indexOf(flag);
  return idx !== -1 && args[idx + 1] ? args[idx + 1] : null;
}
const hasFlag = (flag) => args.includes(flag);

// Determine keys to use
const SPECIFIC_KEY = getArg('--key');

let rawKeys = [];
if (SPECIFIC_KEY) {
  // If user passed a number (e.g. 1, 2, 3) or key name (e.g. GEMINI_API_KEY_3) or direct key string
  if (process.env[`GEMINI_API_KEY_${SPECIFIC_KEY}`]) {
    rawKeys = [process.env[`GEMINI_API_KEY_${SPECIFIC_KEY}`]];
  } else if (process.env[SPECIFIC_KEY]) {
    rawKeys = [process.env[SPECIFIC_KEY]];
  } else if (SPECIFIC_KEY.startsWith('AIza') || SPECIFIC_KEY.startsWith('AQ.')) {
    rawKeys = [SPECIFIC_KEY];
  } else {
    rawKeys = [process.env.GEMINI_API_KEY_1 || process.env.GEMINI_API_KEY_2 || process.env.GEMINI_API_KEY];
  }
} else {
  // Collect all available GEMINI_API_KEY* variables from environment
  const envKeys = Object.keys(process.env)
    .filter(k => k.startsWith('GEMINI_API_KEY'))
    .sort()
    .map(k => process.env[k]);
  rawKeys = envKeys;
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
  return c;
}

function rotateClient() {
  clientIndex++;
  const c = aiClients[clientIndex % aiClients.length];
  console.log(`🔄 Switching active API key -> Key #${c.id} (${c.preview})`);
  return c;
}

const TARGET_TOPIC = getArg('--topic');
const TARGET_SECTION = getArg('--section');
const LIMIT = getArg('--limit') ? parseInt(getArg('--limit'), 10) : null;
const FORCE = hasFlag('--force');
const DRY_RUN = hasFlag('--dry-run');
const GAP_MS = getArg('--gap') ? parseInt(getArg('--gap'), 10) * 1000 : 1500; // 1.5s default

// Strictly use gemini-3.5-flash-lite
const MODEL_NAME = 'gemini-3.5-flash-lite';

// Status Tracking File
const STATUS_FILE = 'content-generation-status-sanskrit.json';
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

// Section Sanskrit metadata mapping
const SECTION_NAMES = {
  'vaidika-sahitya': { sa: 'वैदिक साहित्यम्', hi: 'वैदिक साहित्य', en: 'Vedic Literature', code: '01' },
  'bharatiya-darshana': { sa: 'भारतीयदर्शनम्', hi: 'भारतीय दर्शन', en: 'Indian Philosophy', code: '02' },
  'sanskrit-vyakarana': { sa: 'संस्कृतव्याकरणम् (पाणिनीय)', hi: 'संस्कृत व्याकरण', en: 'Sanskrit Grammar', code: '03' },
  'bhashavigyana': { sa: 'भाषाविज्ञानम्', hi: 'भाषाविज्ञान', en: 'Linguistics', code: '04' },
  'sahityashastra': { sa: 'संस्कृत-साहित्यशास्त्रम् (काव्यशास्त्रम्)', hi: 'संस्कृत साहित्यशास्त्र एवं काव्यशास्त्र', en: 'Poetics and Literary Criticism', code: '05' },
  'laukika-sahitya': { sa: 'लौकिक-संस्कृत-साहित्यम्', hi: 'लौकिक संस्कृत साहित्य', en: 'Classical Sanskrit Literature', code: '06' },
  'sahitya': { sa: 'संस्कृत-साहित्यम् (काव्य-नाटक-गद्यम्)', hi: 'संस्कृत साहित्य', en: 'Sanskrit Literature', code: '07' },
  'subhashita-evam-sukti': { sa: 'सूक्तयः एवं सुभाषितानि', hi: 'सूक्तियाँ एवं सुभाषित', en: 'Epigrams and Wise Sayings', code: '08' },
  'anuvad': { sa: 'अनुवाद-कौशलम् एवं रचना', hi: 'अनुवाद एवं वाक्य रचना', en: 'Translation and Composition', code: '09' },
  'pratiyogitatmaka-sanskrit': { sa: 'प्रतियोगितात्मक-संस्कृतम्', hi: 'प्रतियोगितात्मक संस्कृत', en: 'Competitive Sanskrit Essentials', code: '10' }
};

// Extract title metadata from up-pgt-sanskrit, up-tgt-sanskrit, up-pgt-hindi, up-tgt-hindi
function getTopicMetadataFromTracker() {
  const map = {};
  const trackerPaths = [
    'up-pgt-sanskrit/index.html',
    'up-tgt-sanskrit/index.html',
    'up-pgt-hindi/index.html',
    'up-tgt-hindi/index.html'
  ];
  for (const tPath of trackerPaths) {
    if (fs.existsSync(tPath)) {
      const html = fs.readFileSync(tPath, 'utf8');
      const regex = /<a[^>]*href="([^"]+)"[^>]*>([\s\S]*?)<\/a>/g;
      let m;
      while ((m = regex.exec(html)) !== null) {
        const url = m[1];
        const rawTitle = m[2].replace(/<[^>]+>/g, '').trim();
        if (url.includes('/sanskrit/')) {
          const cleanUrl = url.endsWith('/') ? url : url + '/';
          if (!map[cleanUrl] && /[\u0900-\u097F]/.test(rawTitle)) {
            map[cleanUrl] = {
              title: rawTitle
            };
          }
        }
      }
    }
  }
  return map;
}

const trackerTopicMap = getTopicMetadataFromTracker();

// Recursively find all Sanskrit topic pages
function getAllSanskritPages(dir = 'sanskrit') {
  let pages = [];
  if (!fs.existsSync(dir)) return pages;
  const list = fs.readdirSync(dir, { withFileTypes: true });
  for (const item of list) {
    const full = path.join(dir, item.name);
    if (item.isDirectory()) {
      pages = pages.concat(getAllSanskritPages(full));
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

const allSanskritTopics = getAllSanskritPages();

// Determine eligible topics: by default skip already generated files unless --force is passed
function getEligibleTopics() {
  return allSanskritTopics.filter(item => {
    if (TARGET_TOPIC) {
      const cleanTarget = TARGET_TOPIC.endsWith('/') ? TARGET_TOPIC : TARGET_TOPIC + '/';
      return item.url === cleanTarget;
    }
    if (TARGET_SECTION) {
      if (!item.url.includes(`/${TARGET_SECTION}/`)) return false;
    }
    if (!FORCE) {
      // 1. Check statusMap
      if (statusMap[item.url] && statusMap[item.url].status === 'completed') {
        return false;
      }
      // 2. Check filesystem: if quiz.json and topic-test.json already exist
      const targetDir = path.resolve(item.dir);
      if (fs.existsSync(path.join(targetDir, 'quiz.json')) &&
          fs.existsSync(path.join(targetDir, 'topic-test.json')) &&
          fs.existsSync(path.join(targetDir, 'index.html'))) {
        try {
          const html = fs.readFileSync(path.join(targetDir, 'index.html'), 'utf8');
          // If it already has the 5 modular tabs, skip it
          if (html.includes('study-tabs-sticky-wrapper') || html.includes('tab-notes')) {
            return false;
          }
        } catch (e) {}
      }
    }
    return true;
  });
}

// Get rich context for a topic with pure Devanagari title resolution
function getTopicContext(item) {
  const parts = item.url.split('/').filter(Boolean);
  const branchKey = parts[1] || 'sanskrit-vyakarana';
  const branchMeta = SECTION_NAMES[branchKey] || {
    sa: branchKey.replace(/-/g, ' '),
    hi: branchKey.replace(/-/g, ' '),
    en: branchKey.replace(/-/g, ' '),
    code: '00'
  };

  const slug = parts[parts.length - 1];
  const trackerMeta = trackerTopicMap[item.url];

  // Try multiple fallback sources for pure Devanagari title
  let topicTitleSa = trackerMeta ? trackerMeta.title : '';

  if (!topicTitleSa || !/[\u0900-\u097F]/.test(topicTitleSa)) {
    // Attempt extraction from pre-existing index.html or git
    const htmlPath = path.join(item.dir, 'index.html');
    if (fs.existsSync(htmlPath)) {
      const existingHtml = fs.readFileSync(htmlPath, 'utf8');
      const h1Match = existingHtml.match(/<h1>([^<]+)<\/h1>/i);
      if (h1Match && /[\u0900-\u097F]/.test(h1Match[1])) {
        topicTitleSa = h1Match[1].trim();
      } else {
        const titleMatch = existingHtml.match(/<title>([^<—|]+)/i);
        if (titleMatch && /[\u0900-\u097F]/.test(titleMatch[1])) {
          topicTitleSa = titleMatch[1].trim();
        }
      }
    }
  }

  // Fallback to formatted slug if still not found
  if (!topicTitleSa) {
    topicTitleSa = slug.split('-').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' ');
  }

  // Find related topics in the same branch
  const sectionPrefix = `/sanskrit/${branchKey}/`;
  const related = allSanskritTopics
    .filter(other => other.url.startsWith(sectionPrefix) && other.url !== item.url)
    .slice(0, 6)
    .map(r => {
      const meta = trackerTopicMap[r.url];
      let rTitle = meta ? meta.title : '';
      if (!rTitle || !/[\u0900-\u097F]/.test(rTitle)) {
        const rHtmlPath = path.join(r.dir, 'index.html');
        if (fs.existsSync(rHtmlPath)) {
          const rHtml = fs.readFileSync(rHtmlPath, 'utf8');
          const m = rHtml.match(/<h1>([^<]+)<\/h1>/i);
          if (m && /[\u0900-\u097F]/.test(m[1])) rTitle = m[1].trim();
        }
      }
      if (!rTitle) {
        const rSlug = r.url.split('/').filter(Boolean).pop();
        rTitle = rSlug.replace(/-/g, ' ');
      }
      return { url: r.url, title: rTitle };
    });

  return {
    branchKey,
    branchMeta,
    slug,
    topicTitleSa,
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
      q.options.push(`विकल्पः ${String.fromCharCode(65 + q.options.length)}`);
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
    if (!q.explanation) q.explanation = 'पाणिनीय व्याकरण एवं प्रामाणिक शास्त्रीय ग्रन्थों के अनुसार यह उत्तर शुद्ध एवं प्रामाणिक है।';
  });
}

// ============================================================================
// CALL 1: STUDY NOTES PROMPT (Dynamic Conceptual Modules in Hindi)
// ============================================================================
function buildCall1Prompt(item, context) {
  return `आप UP PGT संस्कृत (विषय कोड 05), UP TGT संस्कृत एवं UGC-NET संस्कृत के वरिष्ठ व्याख्याता एवं विशेषज्ञ हैं।
विषय: "${context.topicTitleSa}" (शाखा: ${context.branchMeta.hi} / ${context.branchMeta.sa}) पर परीक्षोपयोगी, प्रामाणिक एवं विस्तृत अध्ययन नोट्स (Study Notes) तैयार करें।

सर्वोच्च प्राथमिकता निर्देश (भाषा सम्बन्धी):
1. भाषा: सभी वैचारिक व्याख्याएँ (Concepts Explanation), विवेचन, नियमार्थ, अपवाद एवं ट्रिक्स केवल और केवल शुद्ध एवं मानक हिन्दी भाषा (देवनागरी लिपि) में ही लिखें! संस्कृत केवल मूल सूत्रों, श्लोकों, कारिकाओं एवं उदाहरण-पदों तक ही सीमित रखें। वाक्य-रचना, विश्लेषण एवं समझाने की पूरी भाषा हिन्दी होनी चाहिए। (उदा. संस्कृत में "एकस्याः भाषायाः भावान्..." न लिखकर हिन्दी में लिखें: "अनुवाद से तात्पर्य एक भाषा के विचारों अथवा भावों को दूसरी भाषा में शुद्धतापूर्वक रूपांतरित करना है।")
2. अंग्रेजी (English/Roman alphabet) का लेशमात्र भी प्रयोग न करें।
3. वैचारिक मॉड्यूल (conceptual_modules): केवल 3 तक सीमित न रहें। विषय की व्यापकता के अनुसार 4 से 7 विस्तृत मॉड्यूल बनाएं (उदा. परिभाषा एवं मूल स्वरूप, प्रमुख भेद एवं वर्गीकरण, महत्वपूर्ण कारक-विभक्ति नियम, लकार एवं काल-विधान, वाच्य-परिवर्तन एवं शुद्धि-नियम, आदि)।
4. प्रत्येक मॉड्यूल में 4 से 6 स्पष्ट, परीक्षोपयोगी बुलेट बिंदु (bullets) सरल एवं सुबोध हिन्दी में दें, जिनमें महत्वपूर्ण शब्द, सूत्र एवं पद **bold** में हों।
5. प्रमुख सूत्र/नियम (rules_or_sutras): मूल पाणिनीय सूत्र या कारिका संस्कृत में दें, परन्तु उसकी वृत्ति, व्याख्या और उदाहरण-सिद्धि सरल हिन्दी में विस्तारपूर्वक समझाएं।
6. अपवाद एवं विशेष तथ्य (critical_exceptions): वार्तिक जनित अपवाद एवं शास्त्रीय कारण हिन्दी में स्पष्ट करें।
7. याद रखने की ट्रिक्स (tips_and_tricks): परीक्षा में प्रश्नों को तुरंत हल करने के स्मृति-सूत्र एवं शॉर्टकट हिन्दी में समझाएं।
8. तुलनात्मक तालिका (comparison_matrix): दो संबंधित पक्षों (उदा. कर्तृवाच्य बनाम कर्मवाच्य, गुण बनाम वृद्धि आदि) का तुलनात्मक विवेचन हिन्दी में दें।
9. परीक्षा बिंदु (exam_points): परीक्षा में सीधे पूछे जाने वाले 5-6 महत्वपूर्ण तथ्य हिन्दी में लिखें।

आउटपुट का JSON प्रारूप (केवल शुद्ध JSON दें, कोई अतिरिक्त गपशप नहीं):
{
  "title": "${context.topicTitleSa}: प्रामाणिक अध्ययन-टिप्पणी एवं सिद्धान्त",
  "short_intro": "इस विषय की मूल परिभाषा और परीक्षा-प्रासंगिक सार सरल हिन्दी में (अधिकतम 2 प्रत्यक्ष तथ्यात्मक वाक्य)।",
  "conceptual_modules": [
    {
      "module_title": "हिन्दी में विशिष्ट शास्त्रीय शीर्षक (उदा. अनुवाद की परिभाषा एवं मूल स्वरूप)",
      "bullets": [
        "हिन्दी में तथ्यात्मक बुलेट बिंदु 1 (प्रमुख पद/सूत्र **बोल्ड** में)।",
        "हिन्दी में तथ्यात्मक बुलेट बिंदु 2।"
      ]
    }
  ],
  "rules_or_sutras": [
    {
      "name": "पाणिनीय सूत्र / नियम का नाम",
      "statement": "मूल संस्कृत सूत्र या कारिका (उदा. इको यणचि ६।१।७७)",
      "application": "हिन्दी में सरल सूत्रार्थ, नियम का अर्थ एवं उदाहरण-सिद्धि (उदा. सुधी + उपास्यः = सुध्युपास्यः)"
    }
  ],
  "critical_exceptions": [
    {
      "rule": "उत्सर्ग (सामान्य नियम हिन्दी में)",
      "exception": "अपवाद / वार्तिक / विशेष मत (हिन्दी में)",
      "reason": "शास्त्रीय कारण एवं सिद्धि-प्रक्रिया (हिन्दी में)"
    }
  ],
  "tips_and_tricks": [
    {
      "trick_title": "स्मरण-सूत्र अथवा शॉर्टकट ट्रिक (हिन्दी में)",
      "mnemonic": "स्मृति-संकेत अथवा श्लोक-पाद",
      "application": "परीक्षा में त्वरित समाधान की विधि (हिन्दी में)"
    }
  ],
  "comparison_matrix": {
    "title": "तुलनात्मक विवेचन (उदा. कर्तृवाच्य एवं कर्मवाच्य में अन्तर)",
    "headers": ["तुलना का आधार", "प्रथम पक्ष", "द्वितीय पक्ष"],
    "rows": [
      ["नियम / स्वरूप", "विवरण क (हिन्दी में)", "विवरण ख (हिन्दी में)"],
      ["उदाहरण एवं सिद्धि", "उदाहरण क", "उदाहरण ख"]
    ]
  },
  "exam_points": [
    "परीक्षा-दृष्टि से अतिमहत्वपूर्ण तथ्य 1 (हिन्दी में)",
    "परीक्षा-दृष्टि से अतिमहत्वपूर्ण तथ्य 2 (हिन्दी में)",
    "परीक्षा-दृष्टि से अतिमहत्वपूर्ण तथ्य 3 (हिन्दी में)",
    "परीक्षा-दृष्टि से अतिमहत्वपूर्ण तथ्य 4 (हिन्दी में)",
    "परीक्षा-दृष्टि से अतिमहत्वपूर्ण तथ्य 5 (हिन्दी में)"
  ]
}`;
}

// ============================================================================
// CALL 2: REVISION, QUIZ, PYQ & TEST PROMPT (Hindi Explanations)
// ============================================================================
function buildCall2Prompt(item, context, call1Data) {
  return `आप UP PGT/TGT संस्कृत (विषय कोड 05) एवं UGC-NET संस्कृत के वरिष्ठ प्रश्न-पत्र निर्माता हैं।
विषय: "${context.topicTitleSa}" (शाखा: ${context.branchMeta.hi}) के लिए त्वरित पुनरावृत्ति (Revision Summary), अभ्यास प्रश्नोत्तरी (Practice Quiz), विगत वर्षों के प्रश्न (PYQs) और समयबद्ध टॉपिक टेस्ट (Timed Test) तैयार करें।

सर्वोच्च प्राथमिकता निर्देश:
1. भाषा: सभी पारिभाषिक शब्दों की परिभाषाएँ, अंतर, भ्रम-निवारण तथा प्रश्नों की विस्तृत व्याख्याएँ (Explanations) केवल और केवल मानक हिन्दी (देवनागरी) में होनी चाहिए! संस्कृत में व्याख्या न लिखें, व्याख्या विद्यार्थियों के समझने के लिए स्पष्ट हिन्दी में होनी चाहिए।
2. पारिभाषिक शब्दावली (terms_glossary): 8 से 12 महत्वपूर्ण पारिभाषिक शब्द/संज्ञाएँ, उनकी सरल एवं सटीक हिन्दी परिभाषा।
3. स्मरणीय तथ्य (must_remember): 6 से 8 अत्यंत महत्वपूर्ण तथ्य, सूत्र, रूप एवं ग्रन्थकार (हिन्दी में)।
4. मुख्य भ्रम एवं अंतर (common_confusions): 3 से 4 अवधारणाओं का स्पष्ट भेद हिन्दी में समझाएं।
5. अभ्यास प्रश्नोत्तरी (practice_quiz): 18 से 20 वस्तुनिष्ठ प्रश्न (MCQs)। प्रश्न और विकल्प विषय के अनुसार संस्कृत/हिन्दी में हों, परन्तु प्रत्येक प्रश्न की "explanation" (व्याख्या) अनिवार्य रूप से विस्तृत एवं सरल हिन्दी में होनी चाहिए।
6. विगत वर्षों के प्रश्न (pyqs): 5 से 6 प्रामाणिक प्रश्न (UP PGT, TGT, UGC-NET) विस्तृत हिन्दी व्याख्या सहित।
7. समयबद्ध टेस्ट (topic_test): ठीक 10 उच्च-स्तरीय प्रश्न विस्तृत हिन्दी व्याख्या सहित।

आउटपुट का JSON प्रारूप (केवल शुद्ध JSON दें):
{
  "quick_revision": {
    "terms_glossary": [
      {
        "term": "पारिभाषिक पद / संज्ञा",
        "category": "व्याकरण / साहित्य / दर्शन / वेद",
        "definition": "1-2 वाक्यों में सटीक हिन्दी परिभाषा।"
      }
    ],
    "must_remember": [
      "स्मरणीय मुख्य सूत्र अथवा तथ्य 1 (हिन्दी में)",
      "स्मरणीय मुख्य सूत्र अथवा तथ्य 2 (हिन्दी में)"
    ],
    "common_confusions": [
      {
        "term_a": "अवधारणा क",
        "term_b": "अवधारणा ख",
        "difference": "दोनों के बीच स्पष्ट भेद एवं अंतर (हिन्दी में)।"
      }
    ]
  },
  "practice_quiz": [
    {
      "question": "वस्तुनिष्ठ प्रश्न?",
      "options": ["विकल्प क", "विकल्प ख", "विकल्प ग", "विकल्प घ"],
      "correct_index": 0,
      "explanation": "विस्तृत एवं प्रामाणिक हिन्दी व्याख्या जिसमें सही उत्तर का कारण स्पष्ट हो।"
    }
  ],
  "pyqs": [
    {
      "exam_tag": "UP PGT 2021",
      "question": "विगत वर्ष का प्रश्न?",
      "options": ["विकल्प क", "विकल्प ख", "विकल्प ग", "विकल्प घ"],
      "correct_index": 0,
      "explanation": "विस्तृत हिन्दी व्याख्या।"
    }
  ],
  "topic_test": [
    {
      "question": "समयबद्ध टेस्ट का विश्लेषणात्मक प्रश्न?",
      "options": ["विकल्प क", "विकल्प ख", "विकल्प ग", "विकल्प घ"],
      "correct_index": 0,
      "explanation": "विस्तृत हिन्दी समाधान एवं स्पष्टीकरण।"
    }
  ]
}
`;
}

// ============================================================================
// HTML COMPILER (5 Tabs, Sanskrit Styling with Terracotta/Amber & Topic CSS)
// ============================================================================
function renderSanskritTopicHtml(item, context, call1, call2) {
  const canonicalUrl = `https://sjmaths.com${item.url}`;
  const cleanTitle = context.topicTitleSa;
  const pageTitle = `${cleanTitle} — सम्पूर्ण अध्ययन नोट्स, पाणिनीय सूत्राणि, PYQs एवं टेस्ट | UP PGT संस्कृत`;
  const metaDesc = `${cleanTitle} (${context.branchMeta.sa}): पाणिनीय सूत्र, कारिका, व्याकरण नियम, अपवाद, 20 अभ्यास प्रश्न, विगत वर्ष प्रश्न (PYQ) और समयबद्ध टेस्ट।`;

  // Schema.org Structured Data
  const schemaJsonLd = {
    "@context": "https://schema.org",
    "@type": "LearningResource",
    "name": cleanTitle,
    "headline": `${cleanTitle} — UP PGT संस्कृत अध्ययन मार्गदर्शिका`,
    "description": metaDesc,
    "url": canonicalUrl,
    "inLanguage": "sa",
    "learningResourceType": "Study Guide / Quiz",
    "educationalLevel": "Postgraduate Teacher Recruitment / B.A. & M.A. Sanskrit",
    "isPartOf": {
      "@type": "WebSite",
      "name": "SJ Maths",
      "url": "https://sjmaths.com/"
    },
    "breadcrumb": {
      "@type": "BreadcrumbList",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://sjmaths.com/" },
        { "@type": "ListItem", "position": 2, "name": "UP PGT संस्कृत", "item": "https://sjmaths.com/up-pgt-sanskrit/" },
        { "@type": "ListItem", "position": 3, "name": context.branchMeta.sa, "item": `https://sjmaths.com/sanskrit/${context.branchKey}/` },
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
        <div class="formula-eq" style="font-family:'Noto Sans Devanagari',sans-serif;font-size:1.08rem;font-weight:700;color:var(--brand);">${r.statement}</div>
        <div class="formula-meta">
          <div><strong>वृत्तिः / प्रयोगः:</strong> ${r.application}</div>
        </div>
      </div>
    `).join('');

    rulesHtml = `
      <div class="formula-sheet-box">
        <div class="formula-sheet-title">📜 पाणिनीय सूत्राणि, कारिका एवं शास्त्रीय नियमाः</div>
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
          <span class="exception-badge">अपवादः / वार्तिकम्</span>
          <span class="exception-rule">${e.rule}</span>
        </div>
        <p class="exception-detail"><strong>विशेष व्यवस्था:</strong> ${e.exception} — <em>${e.reason}</em></p>
      </div>
    `).join('');

    exceptionsHtml = `
      <div class="exception-alert-box">
        <div class="exception-alert-title">⚠️ विशेषापवादाः एवं परीक्षा-विशिष्ट-तथ्यानि</div>
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
        <p class="trick-app"><strong>परीक्षा-प्रयोगः:</strong> ${t.application}</p>
      </div>
    `).join('');

    tricksHtml = `
      <div class="trick-box">
        <div class="trick-box-title">💡 स्मरण-सूत्राणि एवं शॉर्टकट-प्रणाल्यः</div>
        <div class="tricks-grid">${list}</div>
      </div>
    `;
  }

  // Comparison Matrix
  let comparisonHtml = '';
  if (call1.comparison_matrix && Array.isArray(call1.comparison_matrix.headers)) {
    const m = call1.comparison_matrix;
    const ths = m.headers.map(h => `<th>${h}</th>`).join('');
    const trs = (m.rows || []).map(r => {
      if (Array.isArray(r)) {
        return `<tr>${r.map(c => `<td>${c}</td>`).join('')}</tr>`;
      } else if (typeof r === 'object' && r !== null) {
        return `<tr>${Object.values(r).map(c => `<td>${c}</td>`).join('')}</tr>`;
      }
      return `<tr><td>${r}</td></tr>`;
    }).join('');

    comparisonHtml = `
      <div class="comparison-card">
        <div class="comparison-title">${m.title || 'तुलनात्मकं विवेचनम्'}</div>
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
        <div class="exam-points-title">🎯 परीक्षा-केन्द्रित-तथ्यानि (High-Yield Exam Points)</div>
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
          <span class="q-number">प्रश्नः ${idx + 1} / ${quizList.length}</span>
        </div>
        <h3 class="q-text">${q.question || 'अभ्यास-प्रश्नः'}</h3>
        <div class="quiz-options-group">${opts}</div>
        <div class="q-feedback hidden" id="feedback-${idx}">
          <div class="feedback-indicator"></div>
          <p class="feedback-explanation"><strong>शास्त्रीय व्याख्या:</strong> ${q.explanation || 'प्रामाणिकम् उत्तरम्।'}</p>
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
          <span class="pyq-badge">${q.exam_tag || 'UP PGT Sanskrit'}</span>
        </div>
        <div class="pyq-question-text">${q.question || 'विगत-वर्ष-प्रश्नः'}</div>
        <div class="quiz-options-group">${opts}</div>
        <div class="pyq-expl-box hidden" id="pyq-expl-${idx}">
          <strong>शुद्धोत्तरम्: विकल्पः (${letters[correctIdx]}) — ${correctOptText}</strong>
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
          <span class="t-badge">प्रश्नः ${idx + 1} / ${testList.length}</span>
        </div>
        <div class="test-question-text">${t.question || 'परीक्षण-प्रश्नः'}</div>
        <div class="test-options-grid">${opts}</div>
        <div class="t-feedback hidden" id="t-feedback-${idx}">
          <p class="feedback-explanation"><strong>समाधानम्:</strong> ${t.explanation || 'उत्तर व्याख्या।'}</p>
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
<html lang="sa">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>${pageTitle}</title>
<meta name="description" content="${metaDesc}">
<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1">
<meta name="author" content="SJ Maths">
<meta name="theme-color" content="#9a3412">
<link rel="canonical" href="${canonicalUrl}">
<link rel="icon" type="image/png" href="/favicon.png">

<!-- OpenGraph Metadata -->
<meta property="og:type" content="article">
<meta property="og:site_name" content="SJ Maths">
<meta property="og:title" content="${cleanTitle} — UP PGT संस्कृत नोट्स एवं प्रश्नोत्तरी">
<meta property="og:description" content="${metaDesc}">
<meta property="og:url" content="${canonicalUrl}">

<!-- Twitter Card Metadata -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="${cleanTitle} | UP PGT Sanskrit">
<meta name="twitter:description" content="${metaDesc}">

<!-- JSON-LD Structured Data -->
<script type="application/ld+json">
${JSON.stringify(schemaJsonLd, null, 2)}
</script>

<!-- Unified Topic Stylesheet -->
<link rel="stylesheet" href="/assets/css/topic-page.css">

<!-- Sanskrit Palette (Terracotta & Amber) & Typography Override -->
<style>
:root {
  --brand: #9a3412;
  --brand-dark: #7c2d12;
  --brand-light: #c2410c;
  --accent: #b45309;
  --accent-hover: #92400e;
  --accent-soft: rgba(180, 83, 9, 0.08);
  --accent-border: rgba(180, 83, 9, 0.24);
}
html.dark, body.dark-mode {
  --brand: #fdba74;
  --brand-dark: #fed7aa;
  --brand-light: #fb923c;
  --accent: #f59e0b;
  --accent-hover: #fbbf24;
  --accent-soft: rgba(245, 158, 11, 0.14);
  --accent-border: rgba(245, 158, 11, 0.35);
}
body {
  font-family: "Noto Sans Devanagari", "Mangal", "Nirmala UI", Inter, sans-serif;
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
      <span class="brand-mark" style="background: linear-gradient(145deg, #9a3412, #c2410c); font-family: serif; font-size: 1.35rem; font-style: italic; display: flex; align-items: center; justify-content: center;">&int;</span>
      <span>
        <span class="brand-name">SJ Maths</span>
        <span class="brand-sub">संस्कृत विभागः</span>
      </span>
    </a>
    <div class="header-actions">
      <button type="button" class="theme-toggle-btn" id="btn-theme-toggle" aria-label="Toggle Dark Mode">🌙 Dark Mode</button>
      <a class="back-btn" href="/up-pgt-sanskrit/" title="UP PGT Sanskrit Tracker">← UP PGT<span class="desk-only"> संस्कृतम्</span></a>
    </div>
  </div>
</header>

<main class="wrap">
  <!-- Hero Section -->
  <section class="hero">
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="https://sjmaths.com/">Home</a>
      <span class="breadcrumb-sep">›</span>
      <a href="/up-pgt-sanskrit/">UP PGT संस्कृत</a>
      <span class="breadcrumb-sep">›</span>
      <a href="/sanskrit/${context.branchKey}/">${context.branchMeta.sa}</a>
      <span class="breadcrumb-sep">›</span>
      <span aria-current="page">${cleanTitle}</span>
    </nav>
    <div class="kicker" style="color: #b45309; font-weight: 800;">${context.branchMeta.sa}</div>
    <h1>${cleanTitle}</h1>
    <p class="lead">${call1.short_intro}</p>

    <div class="exam-badges">
      <a class="exam-chip pgt" href="/up-pgt-sanskrit/">UP PGT संस्कृत</a>
      <a class="exam-chip both" href="/up-tgt-sanskrit/">UP TGT संस्कृत</a>
      <span class="exam-chip both">विषय कोड 05 • B.A./M.A. स्तर</span>
    </div>
  </section>

  <!-- Interactive Learning Navigation Tabs (5 Tabs) -->
  <div class="study-tabs-sticky-wrapper">
    <div class="study-tabs" role="tablist" aria-label="Study Module Tabs">
      <button type="button" class="tab-btn active" role="tab" aria-selected="true" data-tab="tab-notes" id="tab-btn-notes">
        <span>📖</span> <span>अध्ययन-टिप्पणी</span>
      </button>
      <button type="button" class="tab-btn" role="tab" aria-selected="false" data-tab="tab-summary" id="tab-btn-summary">
        <span>⚡</span> <span>त्वरित-पुनरावृत्तिः</span>
      </button>
      <button type="button" class="tab-btn" role="tab" aria-selected="false" data-tab="tab-quiz" id="tab-btn-quiz">
        <span>❓</span> <span>अभ्यास-प्रश्नाः</span> <span class="tab-badge">${quizList.length}Q</span>
      </button>
      <button type="button" class="tab-btn" role="tab" aria-selected="false" data-tab="tab-pyqs" id="tab-btn-pyqs">
        <span>🏛️</span> <span>विगत-वर्ष-प्रश्नाः (PYQ)</span>
      </button>
      <button type="button" class="tab-btn" role="tab" aria-selected="false" data-tab="tab-test" id="tab-btn-test">
        <span>⏱️</span> <span>समयबद्ध-परीक्षणम्</span> <span class="tab-badge">${testList.length}Q</span>
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
          <div class="summary-hero-box" style="background: linear-gradient(135deg, #7c2d12 0%, #9a3412 100%); color: #fff; padding: 20px; border-radius: 12px; margin-bottom: 20px;">
            <h2 style="color:#fff;margin-top:0;">⚡ त्वरित-पुनरावृत्तिः: ${cleanTitle}</h2>
            <p style="color:#ffedd5;margin:0;">पाणिनीय संज्ञाः, पारिभाषिक शब्दावली, एवं परीक्षायाम् आगच्छन्तः सूक्ष्माः भेदाः।</p>
          </div>
        </div>

        <div class="revision-container">
          ${glossaryHtml ? `
          <div class="revision-card-box">
            <h2>📚 पारिभाषिक-संज्ञावली (Key Terms)</h2>
            <div class="glossary-grid">
              ${glossaryHtml}
            </div>
          </div>` : ''}

          ${mustRememberHtml ? `
          <div class="revision-card-box highlight" style="margin-top:20px;">
            <h2>🎯 अनिवार्य-स्मरणीय-बिन्दवः (Must Remember)</h2>
            <ul class="must-remember-list">
              ${mustRememberHtml}
            </ul>
          </div>` : ''}

          ${confusionsHtml ? `
          <div class="revision-card-box diff" style="margin-top:20px;">
            <h2>⚖️ सूक्ष्म-भेदाः सामान्य-भ्रमाश्च (Common Confusions)</h2>
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
            <h2>❓ वस्तुनिष्ठ-अभ्यास-प्रश्नाः (${quizList.length} MCQs)</h2>
            <p>उत्तरं चिनुत तथा स्वकीय-प्रगतेः प्रामाणिक-व्याख्यायाश्च समीक्षणं कुरुत।</p>
          </div>
          <div class="quiz-live-scoreboard">
            <div class="score-pill">प्राप्ताङ्काः: <span id="quizScore">0</span> / ${quizList.length}</div>
            <button type="button" class="btn-reset-quiz" id="btnResetQuiz">पुनः आरभ्यताम्</button>
          </div>
        </div>

        <div class="quiz-questions-list">
          ${quizCardsHtml}
        </div>
      </article>

      <!-- TAB 4: PREVIOUS YEARS QUESTIONS (PYQs) -->
      <article class="tab-panel hidden" id="tab-pyqs" role="tabpanel" aria-labelledby="tab-btn-pyqs">
        <div class="pyq-trend-card">
          <h2>🏛️ परीक्षा-प्रवृत्तयः विगत-वर्ष-प्रश्नाश्च</h2>
          <p>UP PGT / TGT संस्कृते <strong>${cleanTitle}</strong> सम्बन्धिताः पूर्वपरीक्षासु पृष्टाः प्रश्नाः।</p>
          <div class="pyq-trend-grid">
            <div class="pyq-stat-item">
              <span class="pyq-stat-val">2–4</span>
              <span class="pyq-stat-label">सम्भाविताः प्रश्नाः</span>
            </div>
            <div class="pyq-stat-item">
              <span class="pyq-stat-val">उच्चतमम्</span>
              <span class="pyq-stat-label">महत्त्वम् (Yield)</span>
            </div>
            <div class="pyq-stat-item">
              <span class="pyq-stat-val">शास्त्रीयम्</span>
              <span class="pyq-stat-label">काठिन्य-स्तरः</span>
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
            <h2>⏱️ समयबद्ध-विषय-परीक्षणम्</h2>
            <p>10 प्रश्नाः &bull; 10 निमेषाः &bull; वास्तविक-परीक्षा-सदृशः अनुभवः</p>
          </div>
          <div class="test-timer-badge" id="testTimerBadge">
            <span class="timer-icon">⏳</span> <span id="timerDisplay">10:00</span>
          </div>
        </div>

        <div class="test-instruction-box" id="testStartWrap">
          <h3>निर्देशाः</h3>
          <ul>
            <li><strong>कुल प्रश्नाः:</strong> 10 वस्तुनिष्ठ प्रश्नाः</li>
            <li><strong>निर्धारितः समयः:</strong> 10 निमेषाः (Minutes)</li>
            <li><strong>अङ्कनम्:</strong> प्रत्येकस्मै शुद्धोत्तराय +1 अङ्कः, ऋणात्मकाङ्कनं नास्ति</li>
          </ul>
          <button type="button" class="btn-start-test" id="btnStartTest" style="background: linear-gradient(135deg, #7c2d12, #9a3412);">परीक्षणं प्रारभ्यताम्</button>
        </div>

        <div class="test-active-container hidden" id="testActiveWrap">
          <div class="test-questions-list">
            ${testCardsHtml}
          </div>
          <div class="test-submit-bar">
            <button type="button" class="btn-submit-test" id="btnSubmitTest" style="background: #9a3412;">परीक्षणं समर्प्यताम् (Submit)</button>
          </div>
        </div>

        <div class="test-result-modal hidden" id="testResultModal">
          <div class="result-card">
            <h3>परीक्षण-परिणामः (Result)</h3>
            <div class="result-score-circle" style="background: linear-gradient(135deg, #7c2d12, #9a3412);">
              <span id="resFinalScore">0</span> / 10
            </div>
            <p id="resFeedbackText">सर्वेषां प्रश्नानां प्रामाणिकानि समाधानानि उपरि अवलोकयन्तु।</p>
            <button type="button" class="btn-retake-test" id="btnRetakeTest" style="background: #9a3412;">पुनः परीक्षणं दीयताम्</button>
          </div>
        </div>
      </article>

      <!-- Bottom Pagination -->
      <nav class="topic-pagination" aria-label="Topic Navigation">
        <a class="topic-nav-btn next" href="/up-pgt-sanskrit/"><span>परीक्षा-ट्रैकर →</span> <strong>UP PGT संस्कृत सम्पूर्ण पाठ्यक्रम</strong></a>
      </nav>

    </div>

    <!-- Sticky Sidebar -->
    <aside class="sidebar-col">
      <div class="sidebar-card side-card">
        <div class="side-card-header">
          <span class="side-badge">पाठ्यक्रम खण्डः</span>
          <h3>${context.branchMeta.sa}</h3>
        </div>
        <p class="side-desc">UP PGT संस्कृत विषय कोड 05 अन्तर्गतं निर्धारितम् अध्ययनम्।</p>
        <div class="side-nav-links">
          ${relatedHtml}
        </div>
        <div class="side-action-box">
          <a class="side-action-btn" href="/up-pgt-sanskrit/" style="background: #7c2d12;">सम्पूर्ण-संस्कृत-ट्रैकरम् उद्घाट्यताम् →</a>
        </div>
      </div>
    </aside>
  </div>
</main>

<footer class="site-footer">
  <div class="wrap footer-inner">
    <div>
      <p><strong>SJ Maths — संस्कृत-विभागः</strong></p>
      <p>UP PGT संस्कृतम् (Subject Code 05) एवं UP TGT संस्कृत-परीक्षा-अध्ययन-सामग्री।</p>
    </div>
    <div class="footer-links">
      <a href="https://sjmaths.com/">Home</a>
      <a href="/up-pgt-sanskrit/">UP PGT संस्कृत</a>
      <a href="/up-tgt-sanskrit/">UP TGT संस्कृत</a>
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
          statusEl.textContent = '✓ शुद्धम् उत्तरम्!';
          statusEl.className = 'feedback-indicator correct';
        }
        if (feedback) feedback.className = 'q-feedback correct';
      } else {
        if (statusEl) {
          statusEl.textContent = '✗ अशुद्धम्। शुद्धं विकल्पः: ' + letters[correctIndex];
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
async function processSanskritTopic(item) {
  const context = getTopicContext(item);
  console.log(`\n============================================================`);
  console.log(`विषयः: ${context.topicTitleSa} (${item.url})`);
  console.log(`शाखा: ${context.branchMeta.sa} | प्रारूपम्: ${MODEL_NAME}`);

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
  console.log(`\n--- [कॉल 1/2] अध्ययन-टिप्पणी (Study Notes) उत्पाद्यते... ---`);
  const call1Prompt = buildCall1Prompt(item, context);
  let call1Data = null;
  const maxRetries = 6;

  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    const clientObj = getClient();
    try {
      console.log(`Gemini Call 1 API [कुंजी: #${clientObj.id} (${clientObj.preview})] (प्रयासः ${attempt}/${maxRetries})...`);
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
      console.log(`✓ कॉल 1 सफलम्! उत्पादिताः मॉडयूल्-सङ्ख्या: ${call1Data.conceptual_modules.length}`);
      break;
    } catch (err) {
      console.error(`कॉल 1 प्रयासः ${attempt} असफलः:`, err.message);
      if (err.message.includes('429') && aiClients.length > 1) {
        rotateClient();
      }
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
  console.log(`\n--- [कॉल 2/2] पुनरावृत्तिः, प्रश्नोत्तरी, PYQs एवं टेस्ट उत्पाद्यते... ---`);
  const call2Prompt = buildCall2Prompt(item, context, call1Data);
  let call2Data = null;

  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    const clientObj = getClient();
    try {
      console.log(`Gemini Call 2 API [कुंजी: #${clientObj.id} (${clientObj.preview})] (प्रयासः ${attempt}/${maxRetries})...`);
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
      console.log(`✓ कॉल 2 सफलम्! प्रश्नाः: ${call2Data.practice_quiz.length} MCQs, परीक्षणम्: ${call2Data.topic_test?.length || 0} MCQs`);
      break;
    } catch (err) {
      console.error(`कॉल 2 प्रयासः ${attempt} असफलः:`, err.message);
      if (err.message.includes('429') && aiClients.length > 1) {
        rotateClient();
      }
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
  const finalHtml = renderSanskritTopicHtml(item, context, call1Data, call2Data);
  fs.writeFileSync(targetHtmlPath, finalHtml, 'utf8');
  console.log(`✓ सफलतापूर्वकं पृष्ठं रक्षितम्: ${targetHtmlPath}`);

  statusMap[item.url] = {
    status: 'completed',
    title: context.topicTitleSa,
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
  console.log('=== SJ Maths — UP PGT / TGT संस्कृत सामग्री जनरेटर (2-Call Pipeline) ===');
  console.log(`अनिवार्य-प्रारूपम्: ${MODEL_NAME}`);
  console.log(`कुल-संस्कृत-विषयाः: ${allSanskritTopics.length}`);

  const eligible = getEligibleTopics();
  console.log(`प्रसंस्करणार्थम् उपलभ्याः विषयाः: ${eligible.length}`);

  const toProcess = LIMIT ? eligible.slice(0, LIMIT) : eligible;
  console.log(`अस्मिन् सत्रे संसाधिताः विषयाः: ${toProcess.length}`);

  let successCount = 0;
  for (let i = 0; i < toProcess.length; i++) {
    const item = toProcess[i];
    console.log(`\n[${i + 1}/${toProcess.length}] आरम्भः: ${item.url}`);

    let ok = false;
    try {
      ok = await processSanskritTopic(item);
    } catch (err) {
      console.error(`अपेक्षित-त्रुटिः ${item.url}:`, err);
      statusMap[item.url] = {
        status: 'error',
        error: err.message,
        failedAt: new Date().toISOString()
      };
      saveStatus();
    }
    if (ok) successCount++;

    if (i < toProcess.length - 1 && !DRY_RUN && GAP_MS > 0) {
      console.log(`अग्रिम-विषयात् पूर्वं ${GAP_MS / 1000}s प्रतीक्षा...`);
      await new Promise(r => setTimeout(r, GAP_MS));
    }
  }

  console.log('\n============================================================');
  console.log(`सम्पन्नम्! साफल्येन पूर्णीकृताः: ${successCount}/${toProcess.length}`);
}

main().catch(err => {
  console.error('Fatal Sanskrit Generator Error:', err);
  process.exit(1);
});
