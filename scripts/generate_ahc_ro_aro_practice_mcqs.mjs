#!/usr/bin/env node
/**
 * scripts/generate_ahc_ro_aro_practice_mcqs.mjs
 *
 * Subject-Wise Practice Zone (50 MCQs) & Live Mock Test (15 MCQs) Generator
 * for Allahabad High Court RO/ARO (Review Officer / Assistant Review Officer) Exam.
 *
 * Outputs:
 * 1. practice.json - Standalone file containing 50 Practice MCQs and 15 Mock Test MCQs with full bilingual support.
 * 2. index.html - Injects practiceQuestions & mockTestQuestions into:
 *    - <script id="embedded-study-guide-data" type="application/json"> (English)
 *    - <script id="embedded-study-guide-data-hi" type="application/json"> (Hindi)
 *
 * Usage:
 *   node scripts/generate_ahc_ro_aro_practice_mcqs.mjs --topic major-rivers-lakes
 *   node scripts/generate_ahc_ro_aro_practice_mcqs.mjs --subject geography --limit 2
 *   node scripts/generate_ahc_ro_aro_practice_mcqs.mjs --subject agriculture-commerce-trade
 *   node scripts/generate_ahc_ro_aro_practice_mcqs.mjs --all
 *   node scripts/generate_ahc_ro_aro_practice_mcqs.mjs --dry-run --topic major-rivers-lakes
 *   node scripts/generate_ahc_ro_aro_practice_mcqs.mjs --force --topic major-crops
 */

import fs from 'node:fs';
import path from 'node:path';
import 'dotenv/config';
import { GoogleGenAI } from '@google/genai';
import { jsonrepair } from 'jsonrepair';

const ROOT_DIR = process.cwd();
const AHC_DIR = path.join(ROOT_DIR, 'ahc-ro-aro');
const STATUS_FILE = path.join(ROOT_DIR, 'scripts', '.ahc-mcq-status.json');

// Subject metadata registry
const SUBJECT_MAP = {
  'agriculture-commerce-trade': {
    name: 'Agriculture, Commerce & Trade',
    nameHi: 'कृषि, वाणिज्य एवं व्यापार',
    examFocus: 'Agricultural systems, cropping seasons (Kharif/Rabi/Zaid), Green & Allied Revolutions, soil types, irrigation, agro-climatic zones, domestic trade, MSMEs, SEZs, export-import policies, and balance of payments.'
  },
  'computer-knowledge': {
    name: 'Computer Knowledge & Typing',
    nameHi: 'कंप्यूटर ज्ञान एवं टाइपिंग',
    examFocus: 'Computer architecture, CPU registers, memory hierarchy (RAM/ROM/Cache), operating systems, MS Office Suite (Word, Excel, PowerPoint shortcuts & formulas), networking (LAN/WAN, topologies, IP addressing), Internet protocols (SMTP/POP/IMAP/HTTP), cyber security & viruses.'
  },
  'current-affairs': {
    name: 'Current Affairs (National & International)',
    nameHi: 'समसामयिक घटनाएं (राष्ट्रीय एवं अंतर्राष्ट्रीय)',
    examFocus: 'National & international events, government flagship schemes, bilateral summits, bills & acts, constitutional appointments (CAG, CEC, CJI), international bodies (UN, G20, BRICS), sports tournaments, awards, and Nobel prizes.'
  },
  'english': {
    name: 'General English & Hindi',
    nameHi: 'सामान्य अंग्रेजी एवं हिंदी',
    examFocus: 'High-court standard English grammar: parts of speech, tenses, active/passive voice, direct/indirect narration, vocabulary (synonyms, antonyms, idioms, one-word substitution), sentence correction, cloze tests, and Hindi grammar fundamentals (Varnamala, Sandhi, Samas, Karak).'
  },
  'general-aptitude': {
    name: 'General Aptitude & Reasoning',
    nameHi: 'सामान्य योग्यता एवं तर्कशक्ति',
    examFocus: 'Verbal and non-verbal reasoning: number & alphabet series, coding-decoding, blood relations, direction sense, syllogisms, seating arrangements, statement-assumptions, Venn diagrams, time & work, speed-distance-time, profit & loss, and data sufficiency.'
  },
  'general-science': {
    name: 'General Science & Technology',
    nameHi: 'सामान्य विज्ञान एवं प्रौद्योगिकी',
    examFocus: 'Physics (mechanics, electricity, optics, thermodynamics), Chemistry (atomic structure, periodic table, acids-bases-salts, carbon compounds, everyday chemistry), Biology (cell biology, genetics, human anatomy & physiology, diseases, plant physiology), and Modern Tech (biotech, space, defense).'
  },
  'geography': {
    name: 'Geography of India & World',
    nameHi: 'भारत एवं विश्व का भूगोल',
    examFocus: 'Physical geography, geomorphology, climatology, oceans, physiographic divisions of India (Himalayas, Northern Plains, Peninsular Plateau, Coastal Plains), drainage systems & major river valley projects, mineral & energy resources, and water conservation schemes.'
  },
  'history-of-india': {
    name: 'History of India',
    nameHi: 'भारत का इतिहास',
    examFocus: 'Ancient India (Pre-history, Indus Valley, Vedic Age, Buddhism, Jainism, Mauryas, Guptas), Medieval India (Delhi Sultanate, Vijayanagara, Bhakti-Sufi movements, Mughals), and Early Modern India (Advent of Europeans, British Expansion, 1857 Revolt, Socio-religious reforms, Land revenue systems).'
  },
  'indian-national-movement': {
    name: 'Indian National Movement',
    nameHi: 'भारतीय राष्ट्रीय आंदोलन',
    examFocus: 'Rise of nationalism, INC formation, Moderate & Extremist phases, Swadeshi movement, Home Rule, Gandhian era (Non-Cooperation, Civil Disobedience, Quit India), revolutionary leaders (Bhagat Singh, Subhash Chandra Bose, Ambedkar, Patel), INA, and Transfer of Power.'
  },
  'polity-economy-culture': {
    name: 'Polity, Economy & Culture',
    nameHi: 'भारतीय राजव्यवस्था, अर्थव्यवस्था एवं संस्कृति',
    examFocus: 'Indian Constitution (Preamble, Fundamental Rights, DPSP, Judiciary, Parliament, Amendments), Indian Economy (Planning Commission, NITI Aayog, Banking, RBI, Poverty alleviation), and Indian Culture (Classical & folk dances, music, temple architecture, UNESCO heritage).'
  },
  'population-ecology-urbanisation': {
    name: 'Population, Ecology & Urbanisation',
    nameHi: 'जनसंख्या, पर्यावरण एवं शहरीकरण',
    examFocus: 'Demographic dividend, Census trends, sex ratio, ecosystems, food webs, biodiversity hotspots, climate change, global warming, international environmental treaties, national parks, solid waste management, and urbanization challenges in India.'
  },
  'up-special-knowledge': {
    name: 'UP Special General Knowledge',
    nameHi: 'उत्तर प्रदेश विशेष सामान्य ज्ञान',
    examFocus: 'Specific knowledge of Uttar Pradesh: geography, rivers, irrigation, soil profiles, agricultural output, ODOP scheme, MSME hubs, major festivals (Kumbh, Taj Mahotsav), folk dances, historical monuments, demographics, literacy rate, and UP state budget.'
  },
  'mains-comprehension': {
    name: 'Mains Reading Comprehension',
    nameHi: 'मुख्य परीक्षा - गद्यांश बोध',
    examFocus: 'High Court descriptive paper: passage analysis, context extraction, analytical question answering, title formulation, and vocabulary in context.'
  },
  'mains-essay': {
    name: 'Mains Essay Writing',
    nameHi: 'मुख्य परीक्षा - निबंध लेखन',
    examFocus: 'Descriptive essay writing: constitutional issues, judicial reforms, socio-economic challenges, science & technology, and national issues.'
  },
  'mains-precis': {
    name: 'Mains Précis Writing',
    nameHi: 'मुख्य परीक्षा - संक्षेपण',
    examFocus: 'Précis writing rules: central theme extraction, 1/3rd length reduction, elimination of redundancy, title formulation, and logical cohesion.'
  },
  'mains-translation': {
    name: 'Mains Administrative Translation',
    nameHi: 'मुख्य परीक्षा - प्रशासनिक अनुवाद',
    examFocus: 'Official administrative and legal bilingual translation: English to Hindi and Hindi to English, formal court phraseology, and official notifications.'
  }
};

// CLI Arguments parsing
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
const TARGET_MODEL = flags.model || process.env.GEMINI_MODEL || 'gemini-3.5-flash-lite';
const FALLBACK_MODELS = ['gemini-3.5-flash-lite', 'gemini-3.5-flash', 'gemini-3.8-flash'];
const LIMIT = flags.limit ? parseInt(flags.limit, 10) : 0;
const TOPIC_FILTER = flags.topic || null;
const SUBJECT_FILTER = flags.subject || null;
const FORCE = Boolean(flags.force);
const DRY_RUN = Boolean(flags['dry-run']);
const GAP_MS = (parseInt(flags.gap || '2', 10)) * 1000;
const MAX_ATTEMPTS = parseInt(flags.attempts || '5', 10);

// API Keys rotation setup
const apiKeys = [
  process.env.GEMINI_API_KEY,
  process.env.GEMINI_API_KEY_1,
  process.env.GEMINI_API_KEY_2,
  process.env.GOOGLE_API_KEY
].filter(Boolean);

if (apiKeys.length === 0) {
  console.error('❌ Error: No Gemini API Key found in environment or .env');
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

// Discover all topic directories in ahc-ro-aro
function discoverTopics() {
  const topics = [];
  const subjects = fs.readdirSync(AHC_DIR, { withFileTypes: true });

  for (const subjEnt of subjects) {
    if (!subjEnt.isDirectory()) continue;
    const subjName = subjEnt.name;
    if (SUBJECT_FILTER && subjName !== SUBJECT_FILTER) continue;

    const subjDir = path.join(AHC_DIR, subjName);
    const topicEnts = fs.readdirSync(subjDir, { withFileTypes: true });

    for (const topEnt of topicEnts) {
      if (!topEnt.isDirectory()) continue;
      const topicSlug = topEnt.name;
      if (TOPIC_FILTER && topicSlug !== TOPIC_FILTER) continue;

      const topicDir = path.join(subjDir, topicSlug);
      const indexPath = path.join(topicDir, 'index.html');
      if (!fs.existsSync(indexPath)) continue;

      const practiceJsonPath = path.join(topicDir, 'practice.json');
      const theoryJsonPath = path.join(topicDir, 'theory.json');

      let currentPracticeCount = 0;
      let currentMockCount = 0;

      if (fs.existsSync(practiceJsonPath)) {
        try {
          const pj = JSON.parse(fs.readFileSync(practiceJsonPath, 'utf8'));
          if (Array.isArray(pj.practiceQuestions)) currentPracticeCount = pj.practiceQuestions.length;
          if (Array.isArray(pj.mockTestQuestions)) currentMockCount = pj.mockTestQuestions.length;
        } catch {}
      } else {
        try {
          const indexHtml = fs.readFileSync(indexPath, 'utf8');
          const m = indexHtml.match(/<script id="embedded-study-guide-data"[^>]*>([\s\S]*?)<\/script>/i);
          if (m) {
            const parsed = JSON.parse(m[1]);
            if (Array.isArray(parsed.practiceQuestions)) currentPracticeCount = parsed.practiceQuestions.length;
            if (Array.isArray(parsed.mockTestQuestions)) currentMockCount = parsed.mockTestQuestions.length;
          }
        } catch {}
      }

      topics.push({
        subject: subjName,
        topicSlug,
        topicDir,
        indexPath,
        practiceJsonPath,
        theoryJsonPath,
        currentPracticeCount,
        currentMockCount,
        has50MCQs: currentPracticeCount >= 50
      });
    }
  }

  return topics;
}

// Extract rich context from existing theory.json and index.html
function extractTopicContext(topic) {
  let title = topic.topicSlug.replace(/-/g, ' ').replace(/\b\w/g, l => l.toUpperCase());
  let titleHi = '';
  const facts = [];

  // Try reading theory.json
  if (fs.existsSync(topic.theoryJsonPath)) {
    try {
      const theory = JSON.parse(fs.readFileSync(topic.theoryJsonPath, 'utf8'));
      if (theory.hero?.title) title = theory.hero.title;
      if (theory.breadcrumbs?.current) title = theory.breadcrumbs.current;
      if (theory.hero?.description) facts.push(theory.hero.description);

      if (theory.timeline?.cards) {
        for (const card of theory.timeline.cards.slice(0, 5)) {
          facts.push(`Timeline [${card.period || card.date}]: ${card.details}`);
        }
      }

      if (theory.deepDive?.sections) {
        for (const sec of theory.deepDive.sections) {
          facts.push(`Section: ${sec.title}`);
          if (sec.content) {
            const cleanText = sec.content.replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim();
            facts.push(cleanText.slice(0, 500));
          }
        }
      }

      if (theory.traps?.items) {
        for (const trap of theory.traps.items.slice(0, 3)) {
          facts.push(`Exam Trap: ${trap.replace(/<[^>]+>/g, '')}`);
        }
      }
    } catch {}
  }

  // Fallback to index.html regex if theory.json was missing or thin
  if (facts.length === 0 && fs.existsSync(topic.indexPath)) {
    try {
      const html = fs.readFileSync(topic.indexPath, 'utf8');
      const h1Match = html.match(/<h1>(?:<span[^>]*>)?(.*?)(?:<\/span>)?<\/h1>/i);
      if (h1Match) title = h1Match[1].replace(/<[^>]+>/g, '').trim();

      const descMatch = html.match(/<p class="topic-desc">(?:<span[^>]*>)?(.*?)(?:<\/span>)?<\/p>/i);
      if (descMatch) facts.push(descMatch[1].replace(/<[^>]+>/g, '').trim());

      const secMatches = [...html.matchAll(/<h3>(.*?)<\/h3>[\s\S]*?<div class="section-content">([\s\S]*?)<\/div>/gi)];
      for (const m of secMatches.slice(0, 4)) {
        const secTitle = m[1].replace(/<[^>]+>/g, '').trim();
        const secBody = m[2].replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim().slice(0, 400);
        facts.push(`Topic Section: ${secTitle} - ${secBody}`);
      }
    } catch {}
  }

  return {
    title,
    titleHi,
    contextSummary: facts.join('\n\n')
  };
}

// Construct prompts for generation in 2 resilient batches
function buildPromptBatch1(topic, subjectMeta, context) {
  return `You are a senior question setter and subject-matter expert for the Allahabad High Court RO/ARO (Review Officer / Assistant Review Officer) and UPPSC competitive examination.

Topic Details:
- Subject: ${subjectMeta.name} (${subjectMeta.nameHi})
- Topic: ${context.title}
- Exam Focus: ${subjectMeta.examFocus}

Syllabus Core Facts & Concepts:
${context.contextSummary || 'Standard high-court syllabus and questions on this topic.'}

TASK (Batch 1 of 2):
Generate EXACTLY 25 high-quality, exam-standard Bilingual Multiple Choice Questions (Practice Questions 1 to 25).
- Questions 1 to 15: Easy to Moderate difficulty (testing fundamental definitions, direct provisions, key personalities, years, formulas, origins, sections).
- Questions 16 to 25: Moderate to Analytical difficulty (multi-statement analysis, matching pairs, and Allahabad High Court / UPPSC past trend pattern).

STRICT OUTPUT FORMAT:
Output ONLY a single valid JSON object with NO markdown formatting, NO triple backticks, and NO trailing commas:
{
  "practiceQuestions": [
    {
      "q": "English question text here",
      "q_hi": "हिंदी में प्रश्न यहाँ लिखें",
      "opts": ["Option A", "Option B", "Option C", "Option D"],
      "opts_hi": ["विकल्प A", "विकल्प B", "विकल्प C", "विकल्प D"],
      "ans": 0,
      "sol": "Detailed explanation in English explaining why the answer is correct.",
      "sol_hi": "हिंदी में विस्तृत व्याख्या।"
    }
  ]
}

CRITICAL RULES:
1. "ans" MUST be an integer from 0 to 3 representing the index of the correct option.
2. "opts" and "opts_hi" MUST each have EXACTLY 4 options.
3. Every question must be 100% factually accurate and relevant to Uttar Pradesh / Indian competitive exams.
4. Provide both English and pure, accurate Hindi for each question, options, and explanation.
5. Return exactly 25 questions in the "practiceQuestions" array.`;
}

function buildPromptBatch2(topic, subjectMeta, context) {
  return `You are a senior question setter and subject-matter expert for the Allahabad High Court RO/ARO (Review Officer / Assistant Review Officer) and UPPSC competitive examination.

Topic Details:
- Subject: ${subjectMeta.name} (${subjectMeta.nameHi})
- Topic: ${context.title}
- Exam Focus: ${subjectMeta.examFocus}

Syllabus Core Facts & Concepts:
${context.contextSummary || 'Standard high-court syllabus and questions on this topic.'}

TASK (Batch 2 of 2):
Generate:
1. EXACTLY 25 Advanced & PYQ-Pattern Bilingual Multiple Choice Questions (Practice Questions 26 to 50):
   - Questions 26 to 40: Advanced / statement-based / assertion-reasoning questions.
   - Questions 41 to 50: Applied / analytical questions matching recent Allahabad High Court & UPPSC RO/ARO standard.
2. EXACTLY 15 Timed Live Mock Test Questions (Mock Test Questions 1 to 15):
   - High-yield, balanced mixed-difficulty exam simulation questions.

STRICT OUTPUT FORMAT:
Output ONLY a single valid JSON object with NO markdown formatting, NO triple backticks, and NO trailing commas:
{
  "practiceQuestions": [
    {
      "q": "English question text here",
      "q_hi": "हिंदी में प्रश्न यहाँ लिखें",
      "opts": ["Option A", "Option B", "Option C", "Option D"],
      "opts_hi": ["विकल्प A", "विकल्प B", "विकल्प C", "विकल्प D"],
      "ans": 0,
      "sol": "Detailed explanation in English.",
      "sol_hi": "हिंदी में विस्तृत व्याख्या।"
    }
  ],
  "mockTestQuestions": [
    {
      "q": "English mock question text",
      "q_hi": "हिंदी में मॉक प्रश्न",
      "opts": ["Option A", "Option B", "Option C", "Option D"],
      "opts_hi": ["विकल्प A", "विकल्प B", "विकल्प C", "विकल्प D"],
      "ans": 0,
      "sol": "Detailed explanation in English.",
      "sol_hi": "हिंदी में विस्तृत व्याख्या।"
    }
  ]
}

CRITICAL RULES:
1. "ans" MUST be an integer from 0 to 3.
2. "opts" and "opts_hi" MUST have exactly 4 elements.
3. Return exactly 25 items in "practiceQuestions" and exactly 15 items in "mockTestQuestions".
4. Ensure pure and accurate bilingual English & Hindi for all fields.`;
}

// Call Gemini API with retries, model fallback, and key rotation
async function callGemini(prompt) {
  const client = getGenAIClient();
  let currentModel = TARGET_MODEL;
  let attempts = 0;

  while (attempts < MAX_ATTEMPTS) {
    attempts++;
    try {
      const response = await client.models.generateContent({
        model: currentModel,
        contents: prompt
      });

      const text = response.text ? response.text.trim() : '';
      if (!text) throw new Error('Received empty response from Gemini model');

      let cleaned = text;
      if (cleaned.startsWith('```json')) cleaned = cleaned.slice(7);
      else if (cleaned.startsWith('```')) cleaned = cleaned.slice(3);
      if (cleaned.endsWith('```')) cleaned = cleaned.slice(0, -3);
      cleaned = cleaned.trim();

      const repaired = jsonrepair(cleaned);
      const parsed = JSON.parse(repaired);
      return parsed;
    } catch (err) {
      console.warn(`   ⚠️ Attempt ${attempts} failed (${err.message.slice(0, 120)})`);
      rotateApiKey();

      // Fallback model rotation if model error, high demand, or rate limit
      const isOverloadedOrRateLimit = /high demand|503|RESOURCE_EXHAUSTED|429|overloaded/i.test(err.message);
      const isNotFound = /not found|404/i.test(err.message);
      if (isNotFound || isOverloadedOrRateLimit) {
        const nextIdx = (FALLBACK_MODELS.indexOf(currentModel) + 1) % FALLBACK_MODELS.length;
        currentModel = FALLBACK_MODELS[nextIdx];
        console.log(`   🔄 Switched fallback model to: ${currentModel}`);
      }

      if (attempts < MAX_ATTEMPTS) {
        const waitTime = isOverloadedOrRateLimit ? 4000 * attempts : 2000 * attempts;
        console.log(`   ⏳ Waiting ${waitTime / 1000}s before next attempt...`);
        await new Promise(r => setTimeout(r, waitTime));
      }
    }
  }

  throw new Error(`Failed after ${MAX_ATTEMPTS} attempts`);
}

// Flexible array extractor from AI responses
function findQuestionArray(obj, preferredKeys) {
  if (!obj || typeof obj !== 'object') return null;
  for (const k of preferredKeys) {
    if (Array.isArray(obj[k]) && obj[k].length > 0) return obj[k];
  }
  // Case-insensitive key search
  const lowerMap = {};
  for (const k of Object.keys(obj)) {
    lowerMap[k.toLowerCase().replace(/[^a-z0-9]/g, '')] = obj[k];
  }
  for (const k of preferredKeys) {
    const cleanK = k.toLowerCase().replace(/[^a-z0-9]/g, '');
    if (Array.isArray(lowerMap[cleanK]) && lowerMap[cleanK].length > 0) return lowerMap[cleanK];
  }
  // Fallback: check any property that is an array of question-like objects
  for (const k of Object.keys(obj)) {
    if (Array.isArray(obj[k]) && obj[k].length > 0 && typeof obj[k][0] === 'object' && (obj[k][0].q || obj[k][0].question || obj[k][0].title)) {
      return obj[k];
    }
  }
  return null;
}

// Validate Question Array
function validateQuestions(qList, expectedMin, label) {
  if (!Array.isArray(qList)) throw new Error(`${label}: expected an array but received ${typeof qList}`);

  const valid = [];
  for (let i = 0; i < qList.length; i++) {
    const item = qList[i];
    if (!item || typeof item !== 'object') continue;
    const qText = item.q || item.question || item.title;
    const opts = item.opts || item.options || item.choices;
    if (!qText || !Array.isArray(opts) || opts.length !== 4) continue;

    let ansIdx = item.ans !== undefined ? item.ans : item.answer !== undefined ? item.answer : 0;
    if (typeof ansIdx === 'string') {
      if (/^[0-3]$/.test(ansIdx.trim())) ansIdx = parseInt(ansIdx.trim(), 10);
      else if (/^[A-D]$/i.test(ansIdx.trim())) ansIdx = ansIdx.trim().toUpperCase().charCodeAt(0) - 65;
      else ansIdx = 0;
    }
    if (typeof ansIdx !== 'number' || isNaN(ansIdx) || ansIdx < 0 || ansIdx > 3) ansIdx = 0;

    const qHi = item.q_hi || item.question_hi || item.hindi || qText;
    const optsHi = (Array.isArray(item.opts_hi) && item.opts_hi.length === 4)
      ? item.opts_hi
      : (Array.isArray(item.options_hi) && item.options_hi.length === 4)
        ? item.options_hi
        : opts;
    const sol = item.sol || item.explanation || item.solution || '';
    const solHi = item.sol_hi || item.explanation_hi || item.solution_hi || sol;

    valid.push({
      q: String(qText).trim(),
      q_hi: String(qHi).trim(),
      opts: opts.map(o => String(o).trim()),
      opts_hi: optsHi.map(o => String(o).trim()),
      ans: ansIdx,
      sol: String(sol).trim(),
      sol_hi: String(solHi).trim()
    });
  }

  if (valid.length < expectedMin) {
    throw new Error(`${label}: only returned ${valid.length} valid questions (expected at least ${expectedMin})`);
  }

  return valid;
}

// Update index.html with embedded bilingual study guide data
function updateIndexHtml(indexPath, practiceQuestions, mockTestQuestions) {
  let content = fs.readFileSync(indexPath, 'utf8');

  // Prepare English questions
  const enPractice = practiceQuestions.map(q => ({
    q: q.q,
    opts: q.opts,
    ans: q.ans,
    sol: q.sol
  }));

  const enMock = mockTestQuestions.map(q => ({
    q: q.q,
    opts: q.opts,
    ans: q.ans,
    sol: q.sol
  }));

  // Prepare Hindi questions
  const hiPractice = practiceQuestions.map(q => ({
    q: q.q_hi || q.q,
    opts: q.opts_hi || q.opts,
    ans: q.ans,
    sol: q.sol_hi || q.sol
  }));

  const hiMock = mockTestQuestions.map(q => ({
    q: q.q_hi || q.q,
    opts: q.opts_hi || q.opts,
    ans: q.ans,
    sol: q.sol_hi || q.sol
  }));

  // Update English embedded script
  const enScriptMatch = content.match(/<script id="embedded-study-guide-data" type="application\/json">([\s\S]*?)<\/script>/i);
  if (enScriptMatch) {
    try {
      const enData = JSON.parse(enScriptMatch[1]);
      enData.practiceQuestions = enPractice;
      enData.mockTestQuestions = enMock;
      const updatedEnScript = `<script id="embedded-study-guide-data" type="application/json">\n${JSON.stringify(enData, null, 2)}\n</script>`;
      content = content.replace(enScriptMatch[0], updatedEnScript);
    } catch (e) {
      console.warn(`   ⚠️ Warning updating English script: ${e.message}`);
    }
  }

  // Update Hindi embedded script
  const hiScriptMatch = content.match(/<script id="embedded-study-guide-data-hi" type="application\/json">([\s\S]*?)<\/script>/i);
  if (hiScriptMatch) {
    try {
      const hiData = JSON.parse(hiScriptMatch[1]);
      hiData.practiceQuestions = hiPractice;
      hiData.mockTestQuestions = hiMock;
      const updatedHiScript = `<script id="embedded-study-guide-data-hi" type="application/json">\n${JSON.stringify(hiData, null, 2)}\n</script>`;
      content = content.replace(hiScriptMatch[0], updatedHiScript);
    } catch (e) {
      console.warn(`   ⚠️ Warning updating Hindi script: ${e.message}`);
    }
  }

  // Ensure Tab label says "(50 Qs)" and "(15 Qs)"
  content = content.replace(/Practice Zone \([^)]*\)/gi, 'Practice Zone (50 Qs)');
  content = content.replace(/अभ्यास प्रश्न \([^)]*\)/gi, 'अभ्यास प्रश्न (50 Qs)');
  content = content.replace(/Live Mock Test \([^)]*\)/gi, 'Live Mock Test (15 Qs)');
  content = content.replace(/लाइव मॉक टेस्ट \([^)]*\)/gi, 'लाइव मॉक टेस्ट (15 Qs)');

  fs.writeFileSync(indexPath, content, 'utf8');
}

// Main execution routine
async function main() {
  console.log('================================================================');
  console.log('  AHC RO/ARO Practice Zone (50 MCQs) & Mock Test Generator');
  console.log('================================================================');
  console.log(`Model: ${TARGET_MODEL} | Force: ${FORCE} | DryRun: ${DRY_RUN}`);

  const status = readStatus();
  const allTopics = discoverTopics();

  console.log(`Discovered ${allTopics.length} total topic pages.`);

  // Filter topics needing generation
  const targetTopics = allTopics.filter(t => {
    if (FORCE) return true;
    return !t.has50MCQs;
  });

  console.log(`Topics requiring MCQ generation (<50 MCQs): ${targetTopics.length}`);

  if (targetTopics.length === 0) {
    console.log('✨ All topics already have >= 50 MCQs! Nothing to generate.');
    return;
  }

  const queue = LIMIT > 0 ? targetTopics.slice(0, LIMIT) : targetTopics;
  console.log(`Processing queue of ${queue.length} topics...\n`);

  let successCount = 0;

  for (let i = 0; i < queue.length; i++) {
    const topic = queue[i];
    const relTopicPath = path.join(topic.subject, topic.topicSlug).replace(/\\/g, '/');
    console.log(`[${i + 1}/${queue.length}] 📚 Topic: ${relTopicPath}`);
    console.log(`   Current: ${topic.currentPracticeCount} practice Qs | ${topic.currentMockCount} mock Qs`);

    if (DRY_RUN) {
      console.log(`   [DRY-RUN] Would generate Batch 1 (25 Qs) and Batch 2 (25 practice + 15 mock).`);
      successCount++;
      continue;
    }

    const subjectMeta = SUBJECT_MAP[topic.subject] || {
      name: topic.subject.replace(/-/g, ' ').toUpperCase(),
      nameHi: topic.subject,
      examFocus: 'Allahabad High Court RO/ARO and UPPSC syllabus.'
    };

    const context = extractTopicContext(topic);

    // --- BATCH 1: Practice Questions 1-25 (Retry until completed) ---
    let batch1Questions = null;
    let b1Attempt = 0;
    while (!batch1Questions) {
      b1Attempt++;
      try {
        console.log(`   ⚡ Generating Batch 1 (Practice Qs 1-25)${b1Attempt > 1 ? ` [Attempt ${b1Attempt}]` : ''}...`);
        const prompt1 = buildPromptBatch1(topic, subjectMeta, context);
        const batch1Res = await callGemini(prompt1);
        const p1Raw = findQuestionArray(batch1Res, ['practiceQuestions', 'questions', 'practice', 'practice_questions']);
        batch1Questions = validateQuestions(p1Raw, 20, 'Batch 1 Practice Qs');
        console.log(`   ✓ Batch 1 generated ${batch1Questions.length} practice MCQs.`);
      } catch (err) {
        console.warn(`   ⚠️ Batch 1 failed: ${err.message}. Retrying Batch 1 until completed...`);
        rotateApiKey();
        await new Promise(r => setTimeout(r, Math.min(25000, 3000 * b1Attempt)));
      }
    }

    await new Promise(r => setTimeout(r, 1500));

    // --- BATCH 2: Practice Questions 26-50 + Mock Questions 1-15 (Retry until completed) ---
    let batch2Data = null;
    let b2Attempt = 0;
    while (!batch2Data) {
      b2Attempt++;
      try {
        console.log(`   ⚡ Generating Batch 2 (Practice Qs 26-50 + Mock Test Qs 1-15)${b2Attempt > 1 ? ` [Attempt ${b2Attempt}]` : ''}...`);
        const prompt2 = buildPromptBatch2(topic, subjectMeta, context);
        const batch2Res = await callGemini(prompt2);

        let p2Raw = findQuestionArray(batch2Res, ['practiceQuestions', 'practice', 'practice_questions', 'questions']);
        let mockRaw = findQuestionArray(batch2Res, ['mockTestQuestions', 'mockQuestions', 'mock_test_questions', 'mockTests', 'mock', 'testQuestions', 'miniTestQuestions']);

        // Fallback: If model bundled all questions into a single array
        if (!mockRaw && p2Raw && p2Raw.length >= 35) {
          mockRaw = p2Raw.slice(25);
          p2Raw = p2Raw.slice(0, 25);
        }

        const p2Questions = validateQuestions(p2Raw, 20, 'Batch 2 Practice Qs');
        const mockQuestions = validateQuestions(mockRaw, 10, 'Batch 2 Mock Test Qs');
        batch2Data = { p2Questions, mockQuestions };
        console.log(`   ✓ Batch 2 generated ${p2Questions.length} practice MCQs and ${mockQuestions.length} mock MCQs.`);
      } catch (err) {
        console.warn(`   ⚠️ Batch 2 failed: ${err.message}. Retrying Batch 2 until completed...`);
        rotateApiKey();
        await new Promise(r => setTimeout(r, Math.min(25000, 3000 * b2Attempt)));
      }
    }

    // Combine Practice Questions
    const allPracticeQuestions = [...batch1Questions, ...batch2Data.p2Questions];
    console.log(`   🎯 Total Combined: ${allPracticeQuestions.length} Practice MCQs | ${batch2Data.mockQuestions.length} Mock Test MCQs`);

    // Write practice.json
    const practiceData = {
      practiceQuestions: allPracticeQuestions,
      mockTestQuestions: batch2Data.mockQuestions
    };
    fs.writeFileSync(topic.practiceJsonPath, JSON.stringify(practiceData, null, 2), 'utf8');
    console.log(`   💾 Saved ${topic.practiceJsonPath}`);

    // Update index.html
    updateIndexHtml(topic.indexPath, allPracticeQuestions, batch2Data.mockQuestions);
    console.log(`   💾 Injected bilingual questions into ${topic.indexPath}`);

    // Update status log
    status[relTopicPath] = {
      completedAt: new Date().toISOString(),
      practiceCount: allPracticeQuestions.length,
      mockCount: batch2Data.mockQuestions.length
    };
    writeStatus(status);

    successCount++;
    console.log(`   ✅ Finished topic: ${relTopicPath}\n`);

    if (i < queue.length - 1) {
      await new Promise(r => setTimeout(r, GAP_MS));
    }
  }

  console.log('================================================================');
  console.log(`🏁 Run Completed: ${successCount} Topics Successfully Finished`);
  console.log('================================================================');
}

main().catch(err => {
  console.error('Fatal error in generator:', err);
  process.exit(1);
});
