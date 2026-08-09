/**
 * Generate all UPSC Economy microtopic pages using upsc-microtopic-template.js.
 * English-only mode: Hindi fields mirror English so the existing renderer stays compatible.
 *
 * Usage:
 *   node upsc/generate-economy.js
 *   node upsc/generate-economy.js --limit 5
 *   node upsc/generate-economy.js --force --tabs overview,concepts,practice,test
 */

import fs from 'fs';
import path from 'path';
import { jsonrepair } from 'jsonrepair';
import {
  validateMetadata,
  GeminiClient,
  assemblePage,
  createManifest,
  TabCache,
  generatePrompt,
  parseResponse,
  normalizeContent,
  generateSha256Hash,
} from './upsc-microtopic-template.js';

const ROOT = process.cwd();
const SUBJECT_DIR = 'economy';
const ECONOMY_ROOT = path.join(ROOT, 'upsc', SUBJECT_DIR);
const DEFAULT_TABS = ['overview', 'concepts', 'visual', 'comparisons', 'practice', 'mains', 'revision', 'test'];
const TAB_GROUPS = [
  ['overview', 'concepts', 'visual'],
  ['comparisons', 'practice', 'mains'],
  ['revision', 'test'],
];

function loadDotEnv() {
  const envPath = path.join(ROOT, '.env');
  if (!fs.existsSync(envPath)) return;
  for (const line of fs.readFileSync(envPath, 'utf8').split(/\r?\n/)) {
    const match = line.match(/^\s*([\w.-]+)\s*=\s*(.*?)\s*$/);
    if (!match || process.env[match[1]]) continue;
    process.env[match[1]] = match[2].replace(/^['"]|['"]$/g, '');
  }
}

function titleFromDir(value) {
  return value
    .replace(/[-_]+/g, ' ')
    .replace(/\bGDP\b|\bGNP\b|\bGST\b|\bNITI\b|\bFDI\b|\bMSME\b/gi, token => token.toUpperCase())
    .replace(/\b\w/g, char => char.toUpperCase());
}

function readTopicName(topicDir, fallback) {
  const candidates = ['content.json', 'page-data.json'];
  for (const filename of candidates) {
    const file = path.join(topicDir, filename);
    if (!fs.existsSync(file)) continue;
    try {
      const data = JSON.parse(fs.readFileSync(file, 'utf8'));
      const title = data.hero?.title || data.title || data.metadata?.title;
      const description = data.hero?.description || data.description || data.metadata?.description;
      if (title || description) return { name: title || fallback, description: description || '' };
    } catch {
      // Fall back to the directory name.
    }
  }
  return { name: fallback, description: '' };
}

function discoverTopics() {
  const parents = fs.readdirSync(ECONOMY_ROOT)
    .filter(name => fs.statSync(path.join(ECONOMY_ROOT, name)).isDirectory());
  const topics = [];
  for (const parentDir of parents) {
    const parentPath = path.join(ECONOMY_ROOT, parentDir);
    const children = fs.readdirSync(parentPath)
      .filter(name => fs.statSync(path.join(parentPath, name)).isDirectory());
    for (const dir of children) {
      const fallback = titleFromDir(dir);
      const source = readTopicName(path.join(parentPath, dir), fallback);
      topics.push({ parentDir, parentTopic: titleFromDir(parentDir), dir, ...source });
    }
  }
  return topics;
}

function buildMeta(topic, previous, next) {
  const description = topic.description || `Comprehensive UPSC Economy study guide covering ${topic.name}, its concepts, Indian context, current relevance, and Prelims and Mains applications.`;
  return {
    name: topic.name,
    hindiName: topic.name,
    dir: topic.dir,
    subject: 'Economy',
    subjectDir: SUBJECT_DIR,
    parentTopic: topic.parentTopic,
    parentDir: topic.parentDir,
    previousTopic: previous?.name || '',
    previousDir: previous?.dir || '',
    previousTopicHi: previous?.name || '',
    nextTopic: next?.name || '',
    nextDir: next?.dir || '',
    nextTopicHi: next?.name || '',
    parentTopicHi: topic.parentTopic,
    childTopics: [], childDirs: [], childTopicsHi: [],
    similarTopics: [], similarDirs: [], similarTopicsHi: [],
    confusedTopics: [], confusedDirs: [], confusedTopicsHi: [],
    canonicalUrl: `https://sjmaths.com/upsc/economy/${topic.parentDir}/${topic.dir}/`,
    description,
    hindiDescription: description,
    category: 'GS-3',
    supportsMains: true,
    topicId: `economy.${topic.parentDir}.${topic.dir}`.toLowerCase().replace(/[^a-z0-9.-]/g, '-'),
    practiceTypes: ['basic', 'conceptual', 'statement', 'advanced'],
    difficulty: 'medium',
    studyTime: { concepts: 20, practice: 15, revision: 10 },
    learningObjectives: [
      `Explain the core economic concepts related to ${topic.name}`,
      `Connect ${topic.name} with the Indian economy and UPSC GS-3`,
      `Apply the topic in UPSC Prelims and Mains answers`,
    ],
    scope: {
      mustExplain: [topic.name, 'Indian Economy', 'UPSC GS-3'],
      mayMention: ['RBI', 'Union Budget', 'Economic Survey', 'NITI Aayog', 'constitutional and statutory institutions'],
      neverExplain: ['unrelated school-level mathematics', 'unrelated history narratives', 'unsupported current statistics'],
      relatedTopics: [topic.name],
      keywords: ['UPSC Economy', 'Indian Economy', topic.name],
    },
    related: {
      prerequisite: previous ? [previous.name] : [],
      recommendedNext: next ? [next.name] : [],
      advancedTopics: [topic.name],
    },
  };
}

function parseArgs() {
  const args = process.argv.slice(2);
  const tabsArg = args.find(arg => arg.startsWith('--tabs='));
  const limitArg = args.find(arg => arg.startsWith('--limit='));
  return {
    force: args.includes('--force'),
    limit: limitArg ? Number(limitArg.split('=')[1]) : Infinity,
    tabs: tabsArg ? tabsArg.split('=')[1].split(',').filter(Boolean) : DEFAULT_TABS,
  };
}

function groupsForTabs(tabs) {
  return TAB_GROUPS.map(group => group.filter(tab => tabs.includes(tab))).filter(group => group.length);
}

function combinedPrompt(meta, tabs) {
  const prompts = tabs.map(tab => `\n--- ${tab.toUpperCase()} TAB ---\n${generatePrompt(tab, meta)}`).join('\n');
  return `You are generating multiple UPSC Economy page tabs in one response.\nIMPORTANT LANGUAGE RULE: Generate ONLY English content in this API response. Do NOT translate anything into Hindi. Do NOT create {"en": ..., "hi": ...} objects. Every title, paragraph, label, explanation, question, option, and table cell must be a plain English string.\nReturn ONLY valid JSON, with exactly these top-level keys: ${tabs.join(', ')}. Each key must contain the complete JSON object required for that tab. Do not use markdown fences. Follow the requested tab structures, but ignore any bilingual-output instruction inside the tab requirements.\n\nTOPIC METADATA:\n${JSON.stringify({ ...meta, hindiName: undefined, hindiDescription: undefined, parentTopicHi: undefined })}\n\nTAB REQUIREMENTS:\n${prompts}\n\nFINAL OUTPUT RULE: Return plain English strings only. Never return Hindi text and never return bilingual en/hi wrappers in the API JSON.`;
}

async function generateTabGroup(client, meta, tabs, cache) {
  const raw = await client.generate(combinedPrompt(meta, tabs));
  let parsed;
  try {
    parsed = parseResponse(raw);
  } catch (firstError) {
    try {
      const repaired = jsonrepair(raw.replace(/^```(?:json)?\s*/i, '').replace(/\s*```$/i, '').trim());
      parsed = JSON.parse(repaired);
      console.warn(`  JSON repair applied for group: ${tabs.join(', ')}`);
    } catch {
      throw firstError;
    }
  }
  if (!parsed || typeof parsed !== 'object' || Array.isArray(parsed)) throw new Error(`Combined response did not contain tab keys: ${tabs.join(', ')}`);
  const result = {};
  for (const tab of tabs) {
    if (!parsed[tab]) throw new Error(`Combined response missing tab: ${tab}`);
    const normalized = normalizeContent(parsed[tab]);
    const bilingual = await (async value => {
      const wrap = item => typeof item === 'string' ? { en: item, hi: item } : item;
      const walk = item => {
        if (typeof item === 'string') return wrap(item);
        if (Array.isArray(item)) return item.map(walk);
        if (!item || typeof item !== 'object') return item;
        if (typeof item.en === 'string' && typeof item.hi === 'string') {
          return { en: item.en, hi: item.en };
        }
        return Object.fromEntries(Object.entries(item).map(([key, value]) => [key, walk(value)]));
      };
      return walk(value);
    })(normalized);
    const hash = await generateSha256Hash(bilingual);
    await cache.set(tab, bilingual, 0, hash);
    result[tab] = bilingual;
  }
  return result;
}

async function main() {
  loadDotEnv();
  const apiKey = process.env.GEMINI_API_KEY;
  if (!apiKey) throw new Error('GEMINI_API_KEY is not set in .env or the environment.');

  const options = parseArgs();
  const topics = discoverTopics().slice(0, options.limit);
  const client = new GeminiClient(apiKey, {
    model: 'gemini-3.5-flash-lite',
    temperature: 0.1,
    requestDelay: 10000,
    requestTimeout: 90000,
    responseMimeType: 'application/json',
    maxRetries: 5,
  });
  let calls = 0;

  console.log(`Discovered ${topics.length} Economy microtopics.`);
  console.log(`Model: gemini-3.5-flash-lite | Tabs: ${options.tabs.join(', ')}`);
  console.log('English-only mode: Hindi fields mirror English.');

  for (let index = 0; index < topics.length; index++) {
    const topic = topics[index];
    const previous = topics[index - 1];
    const next = topics[index + 1];
    const meta = buildMeta(topic, previous, next);
    const validation = validateMetadata(meta);
    if (!validation.passed) {
      console.error(`[${index + 1}/${topics.length}] Skipping ${topic.name}: ${validation.errors.join('; ')}`);
      continue;
    }

    console.log(`\n[${index + 1}/${topics.length}] ${topic.parentTopic} -> ${topic.name}`);
    const cache = new TabCache(fs, path, ROOT, meta);
    const tabResults = {};
    const bilingualData = {};
    let topicCalls = 0;
    const staleTabs = options.force ? options.tabs : await cache.getStaleTabs(options.tabs);
    const groups = groupsForTabs(staleTabs);
    const cachedTabs = options.tabs.length - staleTabs.length;
    if (options.force) {
      console.log(`  Force mode: regenerating all ${options.tabs.length} tabs.`);
    } else if (staleTabs.length === 0) {
      console.log(`  Cache hit: all ${cachedTabs}/${options.tabs.length} tabs cached; skipping API calls.`);
    } else {
      console.log(`  Cache status: ${cachedTabs}/${options.tabs.length} cached; generating ${staleTabs.length} stale tab(s) in ${groups.length} API group(s).`);
    }

    for (const group of groups) {
      try {
        calls++;
        topicCalls++;
        console.log(`  Generating ${group.join(', ')} (API call ${topicCalls}/3)...`);
        const generated = await generateTabGroup(client, meta, group, cache);
        for (const tabName of group) {
          bilingualData[tabName] = generated[tabName];
          tabResults[tabName] = { score: { overall: 0 } };
        }
        console.log(`  Completed group: ${group.join(', ')}`);
      } catch (error) {
        console.error(`  Group ${group.join(', ')} failed: ${error.message}`);
      }
    }

    for (const tabName of options.tabs) {
      if (bilingualData[tabName]) continue;
      const cached = await cache.get(tabName);
      if (cached) {
        bilingualData[tabName] = cached.data;
        tabResults[tabName] = { score: { overall: cached.score }, contentHash: cached.hash };
      }
    }

    const outputDir = path.join(ECONOMY_ROOT, topic.parentDir, topic.dir);
    fs.mkdirSync(outputDir, { recursive: true });
    fs.writeFileSync(path.join(outputDir, 'index.html'), assemblePage(meta, bilingualData), 'utf8');
    fs.writeFileSync(path.join(outputDir, 'page.manifest.json'), JSON.stringify(createManifest(meta, tabResults), null, 2), 'utf8');
    const tabsDir = path.join(outputDir, 'tabs');
    fs.mkdirSync(tabsDir, { recursive: true });
    for (const [tabName, data] of Object.entries(bilingualData)) {
      fs.writeFileSync(path.join(tabsDir, `${tabName}.json`), JSON.stringify(data, null, 2), 'utf8');
    }
    console.log(`  Written: ${path.relative(ROOT, outputDir)}`);
  }
  console.log(`\nCompleted Economy batch. API calls: ${calls}`);
}

main().catch(error => {
  console.error('Fatal:', error.stack || error.message);
  process.exitCode = 1;
});
