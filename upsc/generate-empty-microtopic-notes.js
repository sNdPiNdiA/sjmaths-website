/**
 * Generate pointwise bilingual study notes for empty UPSC microtopics.
 * English notes are generated first, then translated from that exact content.
 *
 * The script handles both page formats currently in upsc/:
 * - Legacy guide pages with a placeholder and no embedded study-guide data.
 * - Microtopic pages with an empty concepts section and no other lesson content.
 *
 * Usage:
 *   node upsc/generate-empty-microtopic-notes.js --dry-run
 *   node upsc/generate-empty-microtopic-notes.js --list
 *   node upsc/generate-empty-microtopic-notes.js --limit=5
 *   node upsc/generate-empty-microtopic-notes.js --subject=environment --limit=10
 *
 * Set GEMINI_API_KEY, GEMINI_API_KEY_1, or GEMINI_API_KEY_2 in the environment
 * or repository .env before generation. Configured keys are tried alternate-first
 * and rotated automatically when a key hits quota.
 * Generated study notes are written into each index.html, including semantic
 * page markup for search engines and inline data for the existing renderer.
 */

import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';
import { parseResponse } from './upsc-microtopic-template.js';

const SCRIPT_DIR = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(SCRIPT_DIR, '..');
const UPSC_ROOT = path.join(ROOT, 'upsc');
const CONCEPTS_CACHE_TITLE = 'Pointwise Study Notes';
const PLACEHOLDER_RE = /currently being prepared|check back soon for comprehensive/i;
const LEGACY_RENDERER_RE = /competitive-exam-guide(?:\.min)?\.js/i;
const MODERN_TABS = ['overview', 'concepts', 'visual', 'comparisons', 'practice', 'mains', 'revision', 'test'];

const SUBJECTS = {
  csat: { name: 'CSAT', paper: 'CSAT' },
  economy: { name: 'Economy', paper: 'GS Paper III' },
  environment: { name: 'Environment and Ecology', paper: 'GS Paper III' },
  geography: { name: 'Geography', paper: 'GS Paper I' },
  'medieval-history': { name: 'Medieval History', paper: 'GS Paper I' },
  'modern-history': { name: 'Modern History', paper: 'GS Paper I' },
  'science-and-tech': { name: 'Science and Technology', paper: 'GS Paper III' },
};

const ENGLISH_MODEL = 'gemini-3.5-flash-lite';
const HINDI_MODEL = 'gemini-3.1-flash-lite';
const RETRY_BASE_DELAY_MS = 5000;
const RETRY_MAX_DELAY_MS = 60000;

async function retryUntilSuccess(stage, operation) {
  let attempts = 0;
  let delayMs = RETRY_BASE_DELAY_MS;
  let retryGuidance = '';

  while (true) {
    attempts++;
    try {
      const result = await operation(retryGuidance);
      if (attempts > 1) console.log('  ' + stage + ' succeeded on attempt ' + attempts + '.');
      return result;
    } catch (error) {
      const message = error && error.message ? error.message : String(error);
      if (error && error.retryGuidance) retryGuidance = error.retryGuidance;
      console.error('  ' + stage + ' failed on attempt ' + attempts + ': ' + message);
      console.log('  Retrying in ' + Math.ceil(delayMs / 1000) + ' seconds. Press Ctrl+C to stop.');
      await new Promise(resolve => setTimeout(resolve, delayMs));
      delayMs = Math.min(delayMs * 2, RETRY_MAX_DELAY_MS);
    }
  }
}

function addRetryFeedback(prompt, guidance) {
  if (!guidance) return prompt;
  return prompt + '\n\nRETRY FEEDBACK: ' + guidance + ' Return the full corrected JSON, preserve every requested fact and item, and fix the reported validation issue. Do not add commentary outside the JSON.';
}

function contentResponseError(error, stage) {
  const wrapped = error instanceof Error ? error : new Error(String(error));
  wrapped.retryGuidance = 'The previous ' + stage + ' response was rejected: ' + wrapped.message + '.';
  return wrapped;
}

function isQuotaError(status, message) {
  return status === 429 || /RESOURCE_EXHAUSTED|quota exceeded|rate.?limit/i.test(message);
}

function isKeySpecificError(status, message) {
  return status === 401 || status === 403 || /API_KEY_INVALID|API key not valid|invalid API key/i.test(message);
}

function getConfiguredGeminiApiKeys() {
  const candidates = [
    { name: 'GEMINI_API_KEY_1', value: process.env.GEMINI_API_KEY_1 },
    { name: 'GEMINI_API_KEY_2', value: process.env.GEMINI_API_KEY_2 },
    { name: 'GEMINI_API_KEY', value: process.env.GEMINI_API_KEY },
    { name: 'GOOGLE_API_KEY', value: process.env.GOOGLE_API_KEY },
  ];
  const seenValues = new Set();
  return candidates.filter(({ value }) => {
    if (!value || seenValues.has(value)) return false;
    seenValues.add(value);
    return true;
  });
}

function createGeminiCaller(apiKeys, requestDelay) {
  const lastRequestByModel = new Map();
  const nextKeyByModel = new Map();

  return async function callGemini(model, prompt) {
    const firstKeyIndex = nextKeyByModel.get(model) || 0;
    let lastQuotaError = null;
    let lastKeyError = null;

    for (let keyOffset = 0; keyOffset < apiKeys.length; keyOffset++) {
      const keyIndex = (firstKeyIndex + keyOffset) % apiKeys.length;
      const apiKey = apiKeys[keyIndex];
      const elapsed = Date.now() - (lastRequestByModel.get(model) || 0);
      if (elapsed < requestDelay) await new Promise(resolve => setTimeout(resolve, requestDelay - elapsed));

      const controller = new AbortController();
      const timeout = setTimeout(() => controller.abort(), 90000);
      let response;
      try {
        response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent?key=${apiKey.value}`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            contents: [{ parts: [{ text: prompt }] }],
            generationConfig: { temperature: 0.1, responseMimeType: 'application/json' },
          }),
          signal: controller.signal,
        });
      } finally {
        clearTimeout(timeout);
        lastRequestByModel.set(model, Date.now());
      }

      const data = await response.json();
      if (!response.ok || data.error) {
        const detail = data.error?.message || response.statusText;
        if (!isQuotaError(response.status, detail) && !isKeySpecificError(response.status, detail)) {
          throw new Error(`Gemini ${model} request failed (${response.status}) using ${apiKey.name}: ${detail}`);
        }

        const keyError = new Error(`Gemini ${model} request failed using ${apiKey.name} (${response.status}): ${detail}`);
        if (isQuotaError(response.status, detail)) lastQuotaError = keyError;
        else lastKeyError = keyError;
        if (keyOffset + 1 < apiKeys.length) {
          const nextKey = apiKeys[(keyIndex + 1) % apiKeys.length];
          console.warn(`  Gemini ${isQuotaError(response.status, detail) ? 'quota' : 'key access'} issue for ${apiKey.name}; switching to ${nextKey.name}.`);
        }
        continue;
      }

      const generatedText = data.candidates?.[0]?.content?.parts?.[0]?.text;
      if (!generatedText) throw new Error(`Gemini ${model} returned no generated text using ${apiKey.name}.`);
      nextKeyByModel.set(model, keyIndex);
      return generatedText;
    }

    nextKeyByModel.set(model, (firstKeyIndex + 1) % apiKeys.length);
    if (lastQuotaError && !lastKeyError) {
      throw new Error(`All ${apiKeys.length} configured Gemini API keys are quota-limited for ${model}. ${lastQuotaError.message}`);
    }
    throw new Error(`All ${apiKeys.length} configured Gemini API keys failed for ${model}. ${lastKeyError?.message || lastQuotaError?.message || ''}`);
  };
}

function loadDotEnv() {
  const envPath = path.join(ROOT, '.env');
  if (!fs.existsSync(envPath)) return;

  for (const line of fs.readFileSync(envPath, 'utf8').split(/\r?\n/)) {
    const match = line.match(/^\s*([\w.-]+)\s*=\s*(.*?)\s*$/);
    if (!match || process.env[match[1]]) continue;
    process.env[match[1]] = match[2].replace(/^['"]|['"]$/g, '');
  }
}

function parseArgs(argv) {
  const options = { dryRun: false, list: false, limit: Infinity, subject: '' };
  for (const arg of argv) {
    if (arg === '--dry-run') options.dryRun = true;
    else if (arg === '--list') options.list = true;
    else if (arg === '--help' || arg === '-h') options.help = true;
    else if (arg.startsWith('--limit=')) {
      options.limit = Number(arg.slice('--limit='.length));
      if (!Number.isInteger(options.limit) || options.limit < 1) {
        throw new Error('--limit must be a positive integer.');
      }
    } else if (arg.startsWith('--subject=')) {
      options.subject = arg.slice('--subject='.length).trim().toLowerCase();
      if (!options.subject) throw new Error('--subject needs a subject folder name.');
    } else {
      throw new Error(`Unknown option: ${arg}`);
    }
  }
  return options;
}

function printHelp() {
  console.log(`Generate pointwise bilingual notes for empty UPSC microtopics.

Usage:
  node upsc/generate-empty-microtopic-notes.js [options]

Options:
  --dry-run             Count and preview targets without an API key or writes
  --list                Print every target path without an API key or writes
  --limit=N             Process at most N targets (useful for resumable batches)
  --subject=FOLDER      Limit to a subject folder, e.g. environment or csat
  --help                Show this help

Generation reads GEMINI_API_KEY_1, GEMINI_API_KEY_2, GEMINI_API_KEY, and GOOGLE_API_KEY from the environment or repository .env, starting with the first configured alternate key.
UPSC_NOTES_REQUEST_DELAY_MS can set request spacing (default: 13000 ms).
A failed generation, translation, validation or save retries with increasing delays until it succeeds; press Ctrl+C to stop.
Each successful topic normally uses one Gemini 3.5 Flash Lite call for English notes and study aids, followed by one Gemini 3.1 Flash Lite call to translate them into Hindi; a failed stage retries with backoff and validation feedback. Pages include pointwise notes, a mind map, tables, methods, tips and Prelims traps. Generated content is saved only in index.html; no JSON sidecar files are written.`);
}

function walkHtmlFiles(directory) {
  const results = [];
  for (const entry of fs.readdirSync(directory, { withFileTypes: true })) {
    const fullPath = path.join(directory, entry.name);
    if (entry.isDirectory()) results.push(...walkHtmlFiles(fullPath));
    else if (entry.isFile() && entry.name.toLowerCase() === 'index.html') results.push(fullPath);
  }
  return results;
}

function readJson(filePath, required = false) {
  if (!fs.existsSync(filePath)) {
    if (required) throw new Error(`Required data file is missing: ${path.relative(ROOT, filePath)}`);
    return null;
  }
  try {
    return JSON.parse(fs.readFileSync(filePath, 'utf8'));
  } catch (error) {
    throw new Error(`Could not parse ${path.relative(ROOT, filePath)}: ${error.message}`);
  }
}

function extractJsonScript(html, id) {
  const escapedId = id.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  const regex = new RegExp(`<script\\b[^>]*\\bid=["']${escapedId}["'][^>]*>([\\s\\S]*?)<\\/script>`, 'i');
  const match = html.match(regex);
  if (!match) return null;
  try {
    return { data: JSON.parse(match[1]), match: match[0], regex };
  } catch (error) {
    throw new Error(`Invalid JSON in ${id}: ${error.message}`);
  }
}

function plainText(value) {
  if (typeof value === 'string') return value.replace(/<[^>]*>/g, ' ').replace(/\s+/g, ' ').trim();
  if (Array.isArray(value)) return value.map(plainText).filter(Boolean).join(' ');
  if (value && typeof value === 'object') return Object.values(value).map(plainText).filter(Boolean).join(' ');
  return '';
}

function hasMeaningfulConcepts(data) {
  const sections = data?.concepts?.sections;
  if (!Array.isArray(sections) || sections.length === 0) return false;
  const text = plainText(sections).replace(PLACEHOLDER_RE, '').trim();
  return text.length >= 150;
}

function hasOtherLessonContent(data) {
  const overview = data?.overview || {};
  const overviewCore = plainText({
    definition: overview.definition,
    importanceInUpsc: overview.importanceInUpsc,
  });
  if (overviewCore.replace(PLACEHOLDER_RE, '').trim().length >= 120) return true;

  const otherTabs = [
    data?.concepts?.upscNotes,
    data?.concepts?.keyTakeaways,
    data?.visual,
    data?.comparisons,
    data?.practice,
    data?.mains,
    data?.revision,
    data?.test,
  ];
  return otherTabs.some(tab => plainText(tab).replace(PLACEHOLDER_RE, '').trim().length >= 150);
}

function validateLegacyPageStructure(html) {
  const blocks = [...html.matchAll(/<!-- SEO_NOSCRIPT_START -->([\s\S]*?)<!-- SEO_NOSCRIPT_END -->/gi)];
  if (blocks.length === 0 || !/<\/body>/i.test(html)) {
    throw new Error('Legacy page is missing its noscript block or closing body tag.');
  }
  for (const [, block] of blocks) {
    const heading = /<h[1-4]\b[^>]*>[^<]*Core Study Notes[^<]*<\/h[1-4]>/i.exec(block);
    if (!heading || block.lastIndexOf('</div>') < heading.index + heading[0].length) {
      throw new Error('Legacy page has an unexpected noscript study-notes structure.');
    }
  }
}

function findTargets() {
  const targets = [];
  for (const indexPath of walkHtmlFiles(UPSC_ROOT)) {
    const html = fs.readFileSync(indexPath, 'utf8');
    const relative = path.relative(UPSC_ROOT, indexPath);
    const parts = relative.split(path.sep);
    const folder = path.dirname(indexPath);
    const contentPath = path.join(folder, 'content.json');

    if (LEGACY_RENDERER_RE.test(html) && parts.length === 4 && !extractJsonScript(html, 'embedded-study-guide-data')
      && !extractJsonScript(html, 'embedded-study-guide-data-hi') && !/window\.studyGuideData\s*=/.test(html)
      && PLACEHOLDER_RE.test(html)) {
      const sidecar = readJson(contentPath);
      const sidecarSections = sidecar?.deepDive?.sections || [];
      const sidecarStillEmpty = sidecarSections.some(section => PLACEHOLDER_RE.test(section.content || ''));
      const sidecarHasGeneratedNotes = sidecar?.deepDive?.title === CONCEPTS_CACHE_TITLE;
      if (!sidecarStillEmpty && !sidecarHasGeneratedNotes) continue;
      try {
        validateLegacyPageStructure(html);
      } catch (error) {
        throw new Error(`${path.relative(ROOT, indexPath)}: ${error.message}`);
      }
      const subjectDir = parts[0];
      const parentDir = parts[1];
      const topicDir = parts[2];
      const subjectInfo = SUBJECTS[subjectDir] || { name: titleFromSlug(subjectDir), paper: 'UPSC GS' };
      const topicName = sidecar.hero?.title || sidecar.breadcrumbs?.current || titleFromSlug(topicDir);
      targets.push({
        kind: 'legacy', indexPath, contentPath, sidecar,
        subjectDir, subject: subjectInfo.name, paper: subjectInfo.paper,
        parentDir, parentTopic: titleFromSlug(parentDir), topicDir, topicName,
        topicId: `${subjectDir}.${parentDir}.${topicDir}`.toLowerCase(),
      });
      continue;
    }

    const modernScript = extractJsonScript(html, 'upsc-page-data');
    if (!modernScript || hasMeaningfulConcepts(modernScript.data) || hasOtherLessonContent(modernScript.data)) continue;

    const data = modernScript.data;
    targets.push({
      kind: 'modern', indexPath, contentPath,
      subjectDir: data.subjectDir || parts[0],
      subject: data.subject || titleFromSlug(data.subjectDir || parts[0]),
      paper: data.category || 'UPSC GS',
      parentDir: data.parentDir || parts[1] || '',
      parentTopic: data.parentTopic || titleFromSlug(data.parentDir || parts[1] || ''),
      topicDir: parts.at(-2), topicName: data.topicName || titleFromSlug(parts.at(-2)),
      topicId: data.topicId || `${data.subjectDir || parts[0]}.${data.parentDir || parts[1]}.${parts.at(-2)}`.toLowerCase(),
      pageData: data,
      sidecar: null,
    });
  }

  return targets.sort((a, b) => {
    const bySubject = a.subjectDir.localeCompare(b.subjectDir);
    return bySubject || a.indexPath.localeCompare(b.indexPath);
  });
}

function titleFromSlug(value = '') {
  const acronyms = new Set(['csat', 'eia', 'unfccc', 'ipcc', 'iucn', 'cbd', 'cop', 'gef', 'unep', 'wmo', 'wwf', 'cites', 'rbi', 'slr', 'gst', 'msp', 'niti', 'fdi', 'msme']);
  return String(value).replace(/[-_]+/g, ' ').split(' ').filter(Boolean).map(word => {
    const lower = word.toLowerCase();
    if (acronyms.has(lower)) return lower.toUpperCase();
    return word.charAt(0).toUpperCase() + word.slice(1);
  }).join(' ');
}

function buildPrompt(meta) {
  const schema = {
    points: [{ heading: 'Short English heading', explanation: 'Complete explanation, at most 45 words.' }],
    studyAids: {
      mindMap: { center: 'Topic', branches: [{ heading: 'Branch', items: ['Short subtopic'] }] },
      tables: [{ title: 'Table title', columns: ['Aspect', 'Type A'], rows: [['Feature', 'Explanation'], ['Feature', 'Explanation']] }],
      mnemonics: [{ title: 'Mnemonic title', phrase: 'Recall phrase', parts: [{ cue: 'Cue', meaning: 'Fact recalled' }, { cue: 'Cue', meaning: 'Fact recalled' }], use: 'When this helps' }],
      tricks: [{ title: 'Method title', steps: ['Step 1', 'Step 2'], examUse: 'How to apply it' }],
      tips: [{ title: 'Topic-specific tip', advice: 'Concise exam advice.' }],
      prelimsTraps: [{ trap: 'Likely confusion', correction: 'Accurate distinction.' }],
    },
  };
  return [
    'You are an experienced UPSC Civil Services teacher. Create accurate, complete, pointwise English study notes for one UPSC microtopic.',
    '',
    'TOPIC',
    '- Topic: ' + meta.topicName,
    '- Subject: ' + meta.subject,
    '- Parent topic: ' + meta.parentTopic,
    '- Exam/paper context: ' + meta.paper,
    '',
    'COVERAGE AND STYLE',
    '- Privately map all examinable concepts and sub-concepts, then check completeness. Cover relevant scope and definitions, classifications, features, comparisons, mechanisms, stages, actors and institutions, laws and policies, causes and effects, applications and significance, limitations, risks, challenges, and responses or reforms.',
    '- Tailor coverage to the subject: essential chronology and consequences for history; location, distribution and processes for geography; ecological links, threats and safeguards for environment; instruments, institutions and effects for economy or polity; principles and applications for science; and rules, formulas, conditions, methods, traps and compact worked examples for CSAT.',
    '- Stay within this microtopic. Include prerequisites only when needed. Use certain, stable facts and specific examples; never guess statistics, dates or legal provisions.',
    '- Use as many points as full coverage requires. There is no target or maximum. Give each distinct concept its own short heading; keep each explanation at most 45 words, usually one or two short sentences. Never write long paragraphs or merge unrelated concepts.',
    '- Include balanced significance, cause-effect links, Prelims distinctions and Mains dimensions where relevant.',
    '',
    'STUDY AIDS',
    '- Create a useful mind map with a central topic and enough branches/subpoints to cover every major part of the notes. Use short labels, not sentences.',
    '- Include at least one concise table. Choose the best topic-specific comparison, classification, process, timeline, institution-role, cause-effect or feature-impact view. Add another only when it clarifies distinct material; do not repeat facts.',
    '- Include 2–5 specific exam tips and 2–5 likely Prelims traps, each paired with an accurate correction. Avoid generic coaching advice.',
    '- Include 1–4 practical methods or tricks with short steps. For CSAT, include a reliable solving sequence where appropriate. Never suggest shortcuts that sacrifice reasoning or accuracy.',
    '- Include a mnemonic only when natural, accurate and genuinely useful. Do not invent misleading acronyms; an empty mnemonic array is acceptable when none is sound.',
    '- Aids reinforce, but do not replace or contradict, the notes. Keep them concise, specific, non-repetitive and supported by the notes.',
    '',
    'Before returning, confirm every relevant concept is explained in the points and every aid preserves the same facts. Return only valid JSON, without markdown fences, commentary or extra keys, matching this schema exactly:',
    JSON.stringify(schema),
  ].join('\n');
}

function requireText(value, label, maxWords) {
  const text = typeof value === 'string' ? value.trim() : '';
  if (!text) throw new Error(label + ' is missing or empty.');
  if (PLACEHOLDER_RE.test(text)) throw new Error(label + ' contains placeholder text.');
  if (maxWords && wordCount(text) > maxWords) throw new Error(label + ' exceeds ' + maxWords + ' words; keep it concise.');
  return text;
}

function validateEnglishNotes(result, topicName) {
  if (!Array.isArray(result && result.points) || result.points.length === 0) throw new Error('Expected non-empty pointwise English notes for ' + topicName + '.');
  const points = result.points.map((point, index) => ({
    heading: requireText(point && point.heading, 'English point ' + (index + 1) + ' heading', 12),
    explanation: requireText(point && point.explanation, 'English point ' + (index + 1) + ' explanation', 45),
  }));
  const aids = result.studyAids;
  if (!aids || typeof aids !== 'object' || Array.isArray(aids)) throw new Error('Study aids are missing for ' + topicName + '.');
  if (!Array.isArray(aids.mindMap && aids.mindMap.branches) || aids.mindMap.branches.length < 3) throw new Error('Mind map must have at least three branches.');
  const mindMap = {
    center: requireText(aids.mindMap.center, 'Mind map center', 12),
    branches: aids.mindMap.branches.map((branch, index) => {
      if (!Array.isArray(branch && branch.items) || !branch.items.length) throw new Error('Mind map branch ' + (index + 1) + ' needs subtopics.');
      return {
        heading: requireText(branch.heading, 'Mind map branch ' + (index + 1) + ' heading', 10),
        items: branch.items.map((item, itemIndex) => requireText(item, 'Mind map branch ' + (index + 1) + ', item ' + (itemIndex + 1), 16)),
      };
    }),
  };
  if (!Array.isArray(aids.tables) || !aids.tables.length || aids.tables.length > 5) throw new Error('Add 1–5 concise study tables.');
  const tables = aids.tables.map((table, index) => {
    if (!Array.isArray(table && table.columns) || table.columns.length < 2 || table.columns.length > 5) throw new Error('Table ' + (index + 1) + ' must have 2–5 columns.');
    if (!Array.isArray(table && table.rows) || table.rows.length < 2 || table.rows.length > 14) throw new Error('Table ' + (index + 1) + ' must have 2–14 rows.');
    const columns = table.columns.map((cell, cellIndex) => requireText(cell, 'Table ' + (index + 1) + ' column ' + (cellIndex + 1), 10));
    const rows = table.rows.map((row, rowIndex) => {
      if (!Array.isArray(row) || row.length !== columns.length) throw new Error('Table ' + (index + 1) + ' row ' + (rowIndex + 1) + ' has the wrong number of cells.');
      return row.map((cell, cellIndex) => requireText(cell, 'Table ' + (index + 1) + ' row ' + (rowIndex + 1) + ', cell ' + (cellIndex + 1), 24));
    });
    return { title: requireText(table.title, 'Table ' + (index + 1) + ' title', 12), columns, rows };
  });
  if (!Array.isArray(aids.mnemonics) || aids.mnemonics.length > 4) throw new Error('Mnemonics must be an array with at most four entries.');
  const mnemonics = aids.mnemonics.map((item, index) => {
    if (!Array.isArray(item && item.parts) || item.parts.length < 2 || item.parts.length > 10) throw new Error('Mnemonic ' + (index + 1) + ' must explain 2–10 cues.');
    return {
      title: requireText(item.title, 'Mnemonic ' + (index + 1) + ' title', 12),
      phrase: requireText(item.phrase, 'Mnemonic ' + (index + 1) + ' phrase', 15),
      parts: item.parts.map((part, partIndex) => ({
        cue: requireText(part && part.cue, 'Mnemonic ' + (index + 1) + ' cue ' + (partIndex + 1), 8),
        meaning: requireText(part && part.meaning, 'Mnemonic ' + (index + 1) + ' meaning ' + (partIndex + 1), 22),
      })),
      use: requireText(item.use, 'Mnemonic ' + (index + 1) + ' use', 30),
    };
  });
  if (!Array.isArray(aids.tricks) || aids.tricks.length < 1 || aids.tricks.length > 4) throw new Error('Add 1–4 practical topic-specific methods.');
  const tricks = aids.tricks.map((item, index) => {
    if (!Array.isArray(item && item.steps) || item.steps.length < 2 || item.steps.length > 6) throw new Error('Method ' + (index + 1) + ' needs 2–6 steps.');
    return {
      title: requireText(item.title, 'Method ' + (index + 1) + ' title', 12),
      steps: item.steps.map((step, stepIndex) => requireText(step, 'Method ' + (index + 1) + ' step ' + (stepIndex + 1), 20)),
      examUse: requireText(item.examUse, 'Method ' + (index + 1) + ' exam use', 30),
    };
  });
  for (const field of ['tips', 'prelimsTraps']) {
    if (!Array.isArray(aids[field]) || aids[field].length < 2 || aids[field].length > 5) throw new Error(field + ' must contain 2–5 entries.');
  }
  const tips = aids.tips.map((item, index) => ({
    title: requireText(item && item.title, 'Tip ' + (index + 1) + ' title', 12),
    advice: requireText(item && item.advice, 'Tip ' + (index + 1) + ' advice', 32),
  }));
  const prelimsTraps = aids.prelimsTraps.map((item, index) => ({
    trap: requireText(item && item.trap, 'Prelims trap ' + (index + 1), 18),
    correction: requireText(item && item.correction, 'Prelims trap ' + (index + 1) + ' correction', 32),
  }));
  return { points, studyAids: { mindMap, tables, mnemonics, tricks, tips, prelimsTraps } };
}

function wordCount(text) {
  return String(text).trim().split(/\s+/).filter(Boolean).length;
}

function collectTranslationUnits(value, label = '$') {
  if (typeof value === 'string') return [{ label, text: value }];
  if (Array.isArray(value)) {
    return value.flatMap((item, index) => collectTranslationUnits(item, label + '[' + (index + 1) + ']'));
  }
  if (value && typeof value === 'object') {
    return Object.entries(value).flatMap(([key, item]) => collectTranslationUnits(item, label + '.' + key));
  }
  return [];
}

function buildHindiTranslationPrompt(meta, englishNotes) {
  const units = collectTranslationUnits(englishNotes);
  return [
    'You are an expert Hindi translator for UPSC Civil Services study material. Translate all notes and study aids into accurate, natural Hindi in Devanagari.',
    'TOPIC: ' + meta.topicName,
    'SUBJECT: ' + meta.subject,
    'PARENT TOPIC: ' + meta.parentTopic,
    '',
    'Translate each input text unit, preserving every fact, distinction, example, formula, caveat, meaning and level of detail. Keep the exact input order and return exactly ' + units.length + ' translated strings. Do not add, omit, merge, split, summarize or reorder units.',
    'Keep explanations and aids concise; do not add facts. Use natural Hindi in Devanagari and retain standard English technical terms in parentheses only when useful. Keep a mnemonic cue or letter pattern unchanged if translating it would break recall, but translate its explanation and use.',
    'Translate every natural-language mind-map branch and subtopic, table heading and cell, tip, method step and trap into Devanagari. For proper names or technical terms, write a Hindi translation or transliteration first and optionally add the original English in parentheses. Only standalone acronyms, formulas and mnemonic letter cues may remain solely in Latin script.',
    'Return only valid JSON without markdown fences or commentary, with exactly this shape: {"translations":["Hindi text 1","Hindi text 2"]}. Include one non-empty string for every input unit. Do not return the input labels or any extra keys.',
    '',
    'TRANSLATION UNITS (id and path explain position; translate only each text value):',
    JSON.stringify(units.map((unit, index) => ({ id: index + 1, path: unit.label, text: unit.text }))),
  ].join('\n');
}

function isFormulaOrSymbol(value) {
  // The translation prompt preserves formulas, so symbolic expressions must not fail the Devanagari check.
  const text = value.trim();
  const mathCharactersOnly = /^[A-Za-z0-9\s\u0370-\u03FF\u2070-\u209F∞√∑∫=<>≤≥≈≠±−×÷·^_/*+().,%{}\[\]|-]+$/u.test(text);
  if (!mathCharactersOnly) return false;
  const letterTokens = text.match(/[A-Za-z]+/g) || [];
  if (letterTokens.some(token => token.length > 4)) return false;
  const hasMathOperator = /[=<>≤≥≈≠±×÷√∞∑∫^_]/u.test(text)
    || /[A-Za-z0-9]\s*\/\s*[A-Za-z0-9]/.test(text)
    || /\s[+-]\s/.test(text)
    || /[A-Za-z0-9]\s*[+−-]\s*[A-Za-z0-9]/u.test(text)
    || /\d[+-]\d/.test(text);
  const isCompactVariable = /^[A-Za-z](?:[A-Z][A-Za-z0-9]*)?$/.test(text) || /^[ΔδλμΣπ]$/u.test(text);
  const isFunctionNotation = /^[A-Za-z]{1,4}\s*\(\s*[A-Za-z0-9]+\s*\)$/u.test(text);
  return hasMathOperator || isCompactVariable || isFunctionNotation;
}

function stringLeaves(value) {
  if (typeof value === 'string') return [value];
  if (Array.isArray(value)) return value.flatMap(stringLeaves);
  if (value && typeof value === 'object') return Object.values(value).flatMap(stringLeaves);
  return [];
}

function isAcronymOnlyText(value) {
  const text = value.trim();
  if (/^[A-Z0-9][A-Z0-9\s.,/()%:-]*$/.test(text)) return true;
  const tokens = text.split(/[\s/()[\],.:;%+-]+/).filter(Boolean);
  return tokens.length > 0 && tokens.every(token => /^[A-Z][A-Z0-9]{1,}$/.test(token.replace(/(?:s|es)$/, '')));
}

function requireHindiForGroup(value, label, devanagari) {
  const leaves = stringLeaves(value);
  const naturalLanguageLeaves = leaves.filter(text =>
    !isAcronymOnlyText(text) && !isFormulaOrSymbol(text),
  );
  if (naturalLanguageLeaves.length && !naturalLanguageLeaves.some(text => devanagari.test(text))) {
    const sample = naturalLanguageLeaves[0].replace(/\s+/g, ' ').slice(0, 80);
    throw new Error('Hindi ' + label + ' has natural-language text but no Devanagari translation. Untranslated sample: ' + JSON.stringify(sample) + '.');
  }
}

function combineTranslations(englishNotes, result, topicName) {
  const units = collectTranslationUnits(englishNotes);
  const hindiStrings = result && result.translations;
  if (!Array.isArray(hindiStrings)) throw new Error('Hindi translation for ' + topicName + ' must return a translations array.');
  if (hindiStrings.length !== units.length) {
    throw new Error('Hindi translation for ' + topicName + ' must return exactly ' + units.length + ' translated strings in order; received ' + hindiStrings.length + '.');
  }
  const devanagari = /\p{Script=Devanagari}/u;
  let unitIndex = 0;
  function pairTree(source, label = '$') {
    if (typeof source === 'string') {
      const unit = units[unitIndex];
      const value = requireText(hindiStrings[unitIndex], 'Hindi translation for ' + (unit ? unit.label : label));
      unitIndex++;
      const key = label.split(/[.[\]]+/).filter(Boolean).at(-1);
      const limit = ['heading', 'center', 'title', 'phrase', 'cue', 'trap'].includes(key) ? 20 : 65;
      if (wordCount(value) > limit) throw new Error('Hindi ' + label + ' exceeds ' + limit + ' words.');
      return { paired: { en: source, hi: value }, hindi: value };
    }
    if (Array.isArray(source)) {
      const paired = [];
      const hindi = [];
      source.forEach((item, index) => {
        const child = pairTree(item, label + '[' + (index + 1) + ']');
        paired.push(child.paired);
        hindi.push(child.hindi);
      });
      return { paired, hindi };
    }
    if (source && typeof source === 'object') {
      const paired = {};
      const hindi = {};
      for (const [key, item] of Object.entries(source)) {
        const child = pairTree(item, label + '.' + key);
        paired[key] = child.paired;
        hindi[key] = child.hindi;
      }
      return { paired, hindi };
    }
    throw new Error('English ' + label + ' has an unsupported value.');
  }
  const translated = pairTree(englishNotes);
  if (unitIndex !== units.length) throw new Error('Hindi translation for ' + topicName + ' did not consume all ' + units.length + ' text units.');
  const hindiPoints = translated.hindi.points;
  const points = translated.paired.points.map((point, index) => {
    const heading = requireText(hindiPoints[index].heading, 'Hindi point ' + (index + 1) + ' heading', 15);
    const explanation = requireText(hindiPoints[index].explanation, 'Hindi point ' + (index + 1) + ' explanation', 65);
    if (!devanagari.test(heading + explanation)) throw new Error('Hindi point ' + (index + 1) + ' is not written in Devanagari.');
    return point;
  });
  const studyAids = translated.paired.studyAids;
  const hindiAids = translated.hindi.studyAids;
  const mindMap = hindiAids.mindMap;
  requireHindiForGroup(mindMap.center, 'mind map center', devanagari);
  mindMap.branches.forEach((branch, index) => {
    requireHindiForGroup(branch.heading, 'mind map branch ' + (index + 1) + ' heading', devanagari);
    requireHindiForGroup(branch.items, 'mind map branch ' + (index + 1) + ' items', devanagari);
  });
  hindiAids.tables.forEach((table, tableIndex) => {
    requireHindiForGroup(table.title, 'table ' + (tableIndex + 1) + ' title', devanagari);
    table.columns.forEach((column, columnIndex) => requireHindiForGroup(column, 'table ' + (tableIndex + 1) + ' column ' + (columnIndex + 1), devanagari));
    table.rows.forEach((row, rowIndex) => requireHindiForGroup(row, 'table ' + (tableIndex + 1) + ' row ' + (rowIndex + 1), devanagari));
  });
  for (const field of ['mnemonics', 'tricks', 'tips', 'prelimsTraps']) {
    (Array.isArray(hindiAids[field]) ? hindiAids[field] : []).forEach((item, index) => requireHindiForGroup(item, field + ' item ' + (index + 1), devanagari));
  }
  if (!devanagari.test(JSON.stringify(hindiAids))) throw new Error('Hindi study aids for ' + topicName + ' contain no Devanagari text.');
  return { points, studyAids };
}

function makeConcepts(points, studyAids) {
  return {
    sections: [{
      title: { en: CONCEPTS_CACHE_TITLE, hi: 'बिंदुवार अध्ययन नोट्स' },
      type: 'list',
      items: points.map(point => ({ term: point.heading, definition: point.explanation })),
    }],
    studyAids,
  };
}

function extractGeneratedPoints(concepts) {
  const section = concepts && concepts.sections && concepts.sections.find(item => item.title && item.title.en === CONCEPTS_CACHE_TITLE);
  if (!section || section.type !== 'list' || !Array.isArray(section.items) || section.items.length === 0) return null;
  return section.items.map(item => ({ heading: item.term, explanation: item.definition }));
}

function extractGeneratedStudyAids(concepts) {
  const aids = concepts && concepts.studyAids;
  return aids && aids.mindMap && aids.tables ? aids : null;
}

function escapeHtml(value) {
  return String(value).replace(/[&<>"']/g, character => ({
    '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;',
  })[character]);
}

function textFor(value, language) {
  if (language) return escapeHtml(value[language]);
  return '<span class="lang-en">' + escapeHtml(value.en) + '</span><span class="lang-hi">' + escapeHtml(value.hi) + '</span>';
}

function renderLegacyList(points, language) {
  return '<ol class="pointwise-study-notes">' + points.map(point =>
    '<li><strong>' + textFor(point.heading, language) + '</strong>: ' + textFor(point.explanation, language) + '</li>'
  ).join('') + '</ol>';
}

function renderStudyAids(aids, language) {
  const title = (english, hindi) => language
    ? escapeHtml(language === 'hi' ? hindi : english)
    : '<span class="lang-en">' + escapeHtml(english) + '</span><span class="lang-hi">' + escapeHtml(hindi) + '</span>';
  const section = (english, hindi, body, className) =>
    '<section class="upsc-study-aid ' + className + '"><h3>' + title(english, hindi) + '</h3>' + body + '</section>';

  const mindMap = aids.mindMap;
  const mapBody = '<p><strong>' + textFor(mindMap.center, language) + '</strong></p><ul>' + mindMap.branches.map(branch =>
    '<li><strong>' + textFor(branch.heading, language) + '</strong><ul>' + branch.items.map(item => '<li>' + textFor(item, language) + '</li>').join('') + '</ul></li>'
  ).join('') + '</ul>';
  let html = section('Mind Map', 'माइंड मैप', mapBody, 'upsc-study-mind-map');

  html += aids.tables.map(table => {
    const caption = textFor(table.title, language);
    const ariaLabel = language ? (language === 'hi' ? 'अध्ययन तालिका' : 'Study aid table') : 'Study aid table / अध्ययन तालिका';
    const headers = table.columns.map(column => '<th scope="col">' + textFor(column, language) + '</th>').join('');
    const rows = table.rows.map(row => '<tr>' + row.map((cell, index) =>
      index === 0 ? '<th scope="row">' + textFor(cell, language) + '</th>' : '<td>' + textFor(cell, language) + '</td>'
    ).join('') + '</tr>').join('');
    return '<section class="upsc-study-aid upsc-study-table"><div class="upsc-study-table-wrap" role="region" aria-label="' +
      escapeHtml(ariaLabel) + '" tabindex="0" style="max-width:100%;overflow-x:auto"><table><caption>' +
      caption + '</caption><thead><tr>' + headers + '</tr></thead><tbody>' + rows + '</tbody></table></div></section>';
  }).join('');

  if (aids.mnemonics.length) {
    const body = '<ul>' + aids.mnemonics.map(item =>
      '<li><strong>' + textFor(item.title, language) + '</strong><p>' + title('Recall phrase', 'स्मरण वाक्य') + ': ' + textFor(item.phrase, language) + '</p><dl>' +
      item.parts.map(part => '<dt>' + textFor(part.cue, language) + '</dt><dd>' + textFor(part.meaning, language) + '</dd>').join('') +
      '</dl><p><strong>' + title('Use', 'उपयोग') + ':</strong> ' + textFor(item.use, language) + '</p></li>'
    ).join('') + '</ul>';
    html += section('Mnemonics', 'स्मरण सूत्र', body, 'upsc-study-mnemonics');
  }

  const tricksBody = '<ul>' + aids.tricks.map(item =>
    '<li><strong>' + textFor(item.title, language) + '</strong><ol>' +
    item.steps.map(step => '<li>' + textFor(step, language) + '</li>').join('') +
    '</ol><p><strong>' + title('Exam use', 'परीक्षा में उपयोग') + ':</strong> ' + textFor(item.examUse, language) + '</p></li>'
  ).join('') + '</ul>';
  html += section('Methods and Tricks', 'तरीके और उपयोगी युक्तियाँ', tricksBody, 'upsc-study-tricks');

  const tipsBody = '<ul>' + aids.tips.map(item =>
    '<li><strong>' + textFor(item.title, language) + '</strong>: ' + textFor(item.advice, language) + '</li>'
  ).join('') + '</ul>';
  html += section('Exam Tips', 'परीक्षा सुझाव', tipsBody, 'upsc-study-tips');

  const trapsBody = '<ul>' + aids.prelimsTraps.map(item =>
    '<li><strong>' + textFor(item.trap, language) + '</strong>: ' + textFor(item.correction, language) + '</li>'
  ).join('') + '</ul>';
  html += section('Prelims Traps and Corrections', 'प्रारंभिक परीक्षा की भ्रांतियाँ और सही तथ्य', trapsBody, 'upsc-study-traps');
  return '<div class="upsc-study-aids">' + html + '</div>';
}

function renderBilingualNotes(points, aids) {
  return '<section class="upsc-generated-study-notes">' +
    '<h2><span class="lang-en">Pointwise Study Notes</span><span class="lang-hi">बिंदुवार अध्ययन नोट्स</span></h2>' +
    renderLegacyList(points, null) + renderStudyAids(aids, null) + '</section>';
}

function updateLegacyNotes(data, points, aids, language) {
  const copy = JSON.parse(JSON.stringify(data));
  copy.deepDive = copy.deepDive || {};
  copy.deepDive.title = language === 'hi' ? 'बिंदुवार अध्ययन नोट्स' : CONCEPTS_CACHE_TITLE;
  copy.deepDive.description = language === 'hi'
    ? 'इस सूक्ष्म विषय के मुख्य विचारों और पुनरावृत्ति सहायक सामग्री को क्रमबद्ध बिंदुओं में पढ़ें।'
    : 'Study this microtopic through concise notes, a mind map, tables and topic-specific recall aids.';
  copy.deepDive.sections = [{
    title: copy.deepDive.title,
    content: renderLegacyList(points, language) + renderStudyAids(aids, language),
    masteryZone: [],
  }];
  return copy;
}

function safeScriptJson(data) {
  return JSON.stringify(data).replace(/</g, '\\u003c');
}

function updateNoScriptNotes(html, points, aids) {
  const markerRegex = /<!-- SEO_NOSCRIPT_START -->([\s\S]*?)<!-- SEO_NOSCRIPT_END -->/gi;
  let blockCount = 0;
  const updated = html.replace(markerRegex, (_whole, originalBlock) => {
    const language = blockCount++ === 0 ? 'en' : 'hi';
    const heading = /<h[1-4]\b[^>]*>[^<]*Core Study Notes[^<]*<\/h[1-4]>/i.exec(originalBlock);
    const wrapperEnd = originalBlock.lastIndexOf('</div>');
    if (!heading || wrapperEnd < heading.index + heading[0].length) throw new Error('Could not locate the legacy study-notes placeholder in a noscript block.');
    const prefix = originalBlock.slice(0, heading.index + heading[0].length);
    const label = language === 'hi' ? 'बिंदुवार अध्ययन नोट्स' : CONCEPTS_CACHE_TITLE;
    const content = renderLegacyList(points, language) + renderStudyAids(aids, language);
    return '<!-- SEO_NOSCRIPT_START -->' + prefix + '<h4>' + label + '</h4>' + content + '\n' + originalBlock.slice(wrapperEnd) + '<!-- SEO_NOSCRIPT_END -->';
  });
  if (blockCount === 0) throw new Error('Legacy page is missing its SEO noscript markers.');
  return updated;
}

function replaceJsonScript(html, id, data) {
  const escapedId = id.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  const regex = new RegExp(`(<script\\b[^>]*\\bid=["']${escapedId}["'][^>]*>)([\\s\\S]*?)(<\\/script>)`, 'i');
  if (!regex.test(html)) throw new Error(`Could not find the ${id} script tag.`);
  return html.replace(regex, (_all, open, _oldJson, close) => `${open}\n${safeScriptJson(data)}\n${close}`);
}

function hashJson(data) {
  return `sha256-${crypto.createHash('sha256').update(JSON.stringify(data)).digest('hex')}`;
}

function atomicWrite(filePath, contents) {
  fs.mkdirSync(path.dirname(filePath), { recursive: true });
  const tempPath = `${filePath}.${process.pid}.${Date.now()}.tmp`;
  try {
    fs.writeFileSync(tempPath, contents, 'utf8');
    fs.renameSync(tempPath, filePath);
  } catch (error) {
    try { if (fs.existsSync(tempPath)) fs.unlinkSync(tempPath); } catch { /* Keep the original error. */ }
    throw error;
  }
}

function updateLegacyPage(target, html, points, aids, sidecar) {
  const englishData = updateLegacyNotes(sidecar, points, aids, 'en');
  const hindiData = updateLegacyNotes(sidecar, points, aids, 'hi');
  let updatedHtml = updateNoScriptNotes(html, points, aids);
  const embeddedData = '<script type="application/json" id="embedded-study-guide-data">' + safeScriptJson(englishData) + '</script>\n' +
    '<script type="application/json" id="embedded-study-guide-data-hi">' + safeScriptJson(hindiData) + '</script>\n';
  const bodyClose = /<\/body>/i;
  if (!bodyClose.test(updatedHtml)) throw new Error('Legacy page is missing its closing body tag.');
  return updatedHtml.replace(bodyClose, embeddedData + '</body>');
}

function updateModernPage(target, html, concepts, points) {
  const current = extractJsonScript(html, 'upsc-page-data');
  if (!current) throw new Error('Modern page is missing its upsc-page-data script.');
  const data = current.data;
  data.concepts = { ...(data.concepts || {}), ...concepts };
  data.generatedAt = new Date().toISOString();
  const tabData = {};
  for (const tab of MODERN_TABS) {
    if (Object.prototype.hasOwnProperty.call(data, tab)) tabData[tab] = data[tab];
  }
  data.contentHash = hashJson(tabData);
  let updatedHtml = replaceJsonScript(html, 'upsc-page-data', data);
  const placeholder = /<section\b(?=[^>]*\bclass=["'][^"']*\bcontent-status\b[^"']*["'])[^>]*>[\s\S]*?<\/section>/i;
  if (!placeholder.test(updatedHtml)) throw new Error('Modern page is missing its content-status placeholder.');
  updatedHtml = updatedHtml.replace(placeholder, renderBilingualNotes(points, concepts.studyAids));
  return updatedHtml;
}

function isStillEmpty(target, html) {
  if (target.kind === 'legacy') {
    return LEGACY_RENDERER_RE.test(html) && !extractJsonScript(html, 'embedded-study-guide-data')
      && !extractJsonScript(html, 'embedded-study-guide-data-hi') && PLACEHOLDER_RE.test(html);
  }
  const script = extractJsonScript(html, 'upsc-page-data');
  return Boolean(script && !hasMeaningfulConcepts(script.data) && !hasOtherLessonContent(script.data));
}

function writeTarget(target, concepts) {
  const html = fs.readFileSync(target.indexPath, 'utf8');
  if (!isStillEmpty(target, html)) return false;

  const points = extractGeneratedPoints(concepts);
  const aids = extractGeneratedStudyAids(concepts);
  if (!points) throw new Error('Generated concepts did not contain valid pointwise notes.');
  if (!aids) throw new Error('Generated concepts did not contain validated study aids.');

  const updatedHtml = target.kind === 'legacy'
    ? updateLegacyPage(target, html, points, aids, target.sidecar)
    : updateModernPage(target, html, concepts, points);
  atomicWrite(target.indexPath, updatedHtml);
  return true;
}

function summarizeTargets(targets) {
  const counts = new Map();
  for (const target of targets) counts.set(target.subjectDir, (counts.get(target.subjectDir) || 0) + 1);
  for (const [subjectDir, count] of [...counts.entries()].sort(([a], [b]) => a.localeCompare(b))) {
    console.log(`  ${subjectDir}: ${count}`);
  }
}

function filterTargets(targets, options) {
  let selected = targets;
  if (options.subject) selected = selected.filter(target => target.subjectDir.toLowerCase() === options.subject);
  if (Number.isFinite(options.limit)) selected = selected.slice(0, options.limit);
  return selected;
}

async function main() {
  const options = parseArgs(process.argv.slice(2));
  if (options.help) return printHelp();

  const allTargets = findTargets();
  const subjectFiltered = options.subject
    ? allTargets.filter(target => target.subjectDir.toLowerCase() === options.subject)
    : allTargets;
  const targets = filterTargets(allTargets, options);

  console.log(`Empty UPSC microtopics found: ${subjectFiltered.length}${options.subject ? ` (${options.subject})` : ''}`);
  summarizeTargets(subjectFiltered);
  if (options.list) {
    for (const target of targets) console.log(`${target.kind}\t${path.relative(ROOT, target.indexPath)}`);
    return;
  }
  if (options.dryRun) {
    console.log(`Dry run: ${targets.length} target(s) selected; no files were written.`);
    for (const target of targets.slice(0, 20)) console.log(`  ${target.kind}: ${path.relative(ROOT, target.indexPath)}`);
    if (targets.length > 20) console.log(`  ... and ${targets.length - 20} more; use --list to print all paths.`);
    return;
  }
  if (targets.length === 0) {
    console.log('No matching empty microtopics to generate.');
    return;
  }

  loadDotEnv();
  const apiKeys = getConfiguredGeminiApiKeys();
  if (apiKeys.length === 0) throw new Error('No Gemini API key is set in the environment or repository .env. Set GEMINI_API_KEY_1, GEMINI_API_KEY_2, GEMINI_API_KEY, or GOOGLE_API_KEY.');
  const requestDelay = Number(process.env.UPSC_NOTES_REQUEST_DELAY_MS || 13000);
  if (!Number.isFinite(requestDelay) || requestDelay < 1000) {
    throw new Error('UPSC_NOTES_REQUEST_DELAY_MS must be at least 1000.');
  }
  const callGemini = createGeminiCaller(apiKeys, requestDelay);

  console.log(`Generating complete English notes with ${ENGLISH_MODEL}, then translating them with ${HINDI_MODEL}; writing index.html only; request spacing: ${requestDelay} ms per model.`);
  console.log('Configured Gemini keys in fallback order: ' + apiKeys.map(key => key.name).join(', ') + '.');
  let completed = 0;
  let skipped = 0;

  for (let index = 0; index < targets.length; index++) {
    const target = targets[index];
    const label = `${target.parentTopic} → ${target.topicName}`;
    console.log(`[${index + 1}/${targets.length}] Generating English notes: ${label}`);
    const englishNotes = await retryUntilSuccess('English generation and validation', async retryGuidance => {
      const englishResponse = await callGemini(ENGLISH_MODEL, addRetryFeedback(buildPrompt(target), retryGuidance));
      try {
        return validateEnglishNotes(parseResponse(englishResponse), target.topicName);
      } catch (error) {
        throw contentResponseError(error, 'English notes');
      }
    });
    console.log('  Translating ' + englishNotes.points.length + ' points and study aids into Hindi.');
    const translatedNotes = await retryUntilSuccess('Hindi translation and validation', async retryGuidance => {
      let prompt = buildHindiTranslationPrompt(target, englishNotes);
      if (retryGuidance) {
        retryGuidance += ' For mind-map labels and subtopics, translate every natural-language phrase into Devanagari. For proper names or technical terms, give a Hindi translation or transliteration first and keep the English term in parentheses when useful. Only mnemonic letter cues and standard acronyms may remain alone in Latin script.';
        prompt = addRetryFeedback(prompt, retryGuidance);
      }
      const hindiResponse = await callGemini(HINDI_MODEL, prompt);
      try {
        return combineTranslations(englishNotes, parseResponse(hindiResponse), target.topicName);
      } catch (error) {
        throw contentResponseError(error, 'Hindi translation');
      }
    });
    const points = translatedNotes.points;
    const concepts = makeConcepts(points, translatedNotes.studyAids);

    const saved = await retryUntilSuccess('HTML save', async () => writeTarget(target, concepts));
    if (saved) {
      completed++;
        console.log('  Saved ' + points.length + ' bilingual points and study aids in index.html.');
    } else {
      skipped++;
        console.log('  Skipped because the page now contains lesson content.');
    }
  }

  console.log(`\nFinished. Completed: ${completed}; skipped: ${skipped}.`);
}

main().catch(error => {
  console.error(`Fatal: ${error.message}`);
  process.exitCode = 1;
});
