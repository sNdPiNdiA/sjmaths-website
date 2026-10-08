'use strict';

const fs = require('node:fs');
const path = require('node:path');
const { spawnSync } = require('node:child_process');
const {
  assertSameShape,
  buildHindiCleanupPrompt,
  buildHindiTranslationPrompt,
  extractEnglishValues,
  extractHindiValues,
  isBilingualConcepts,
  numericTokenDifferences,
  pairTranslatedValues,
  untranslatedLatinPaths,
} = require('./lib/up-assistant-bilingual.cjs');

const ROOT = path.resolve(__dirname, '..');
const MODEL = process.env.GEMINI_MODEL || 'gemini-3.1-flash-lite';
const REQUEST_DELAY_MS = 3000;
const MAX_RETRIES = 5;

function loadEnv() {
  const envPath = path.join(ROOT, '.env');
  if (!fs.existsSync(envPath)) return;
  for (const line of fs.readFileSync(envPath, 'utf8').split(/\r?\n/)) {
    const match = line.match(/^\s*([\w.-]+)\s*=\s*(.*?)\s*$/);
    if (!match || process.env[match[1]]) continue;
    process.env[match[1]] = match[2].replace(/^(?:"([\s\S]*)"|'([\s\S]*)')$/, (_, doubleQuoted, singleQuoted) => doubleQuoted ?? singleQuoted);
  }
}

function parseResponse(text) {
  const cleaned = String(text || '').trim().replace(/^```(?:json)?\s*/i, '').replace(/\s*```$/, '');
  const start = cleaned.search(/[\[{]/);
  if (start < 0) throw new Error('Translation response did not contain JSON.');
  const opening = cleaned[start];
  const closing = opening === '{' ? '}' : ']';
  let depth = 0;
  let quoted = false;
  let escaped = false;
  for (let index = start; index < cleaned.length; index++) {
    const char = cleaned[index];
    if (escaped) { escaped = false; continue; }
    if (char === '\\') { escaped = true; continue; }
    if (char === '"') { quoted = !quoted; continue; }
    if (quoted) continue;
    if (char === opening || char === (opening === '{' ? '[' : '{')) depth++;
    if (char === closing || char === (closing === '}' ? ']' : '}')) depth--;
    if (depth === 0) return JSON.parse(cleaned.slice(start, index + 1));
  }
  throw new Error('Translation response contained incomplete JSON.');
}

function sleep(ms) { return new Promise(resolve => setTimeout(resolve, ms)); }

async function translate(concepts, subject, apiKey) {
  const url = `https://generativelanguage.googleapis.com/v1beta/models/${MODEL}:generateContent?key=${apiKey}`;
  const requestJson = async prompt => {
    let lastError;
    for (let attempt = 1; attempt <= MAX_RETRIES; attempt++) {
    try {
      const response = await fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          contents: [{ parts: [{ text: prompt }] }],
          generationConfig: { temperature: 0.1, maxOutputTokens: 65536, responseMimeType: 'application/json' },
        }),
      });
      if (response.status === 429 || response.status === 503) {
        const wait = response.status === 429 ? Math.min(60000, 5000 * (2 ** (attempt - 1))) : 15000;
        lastError = new Error(`Gemini API rate/service response ${response.status}`);
        if (attempt < MAX_RETRIES) { await sleep(wait); continue; }
      }
      if (!response.ok) throw new Error(`Gemini API error ${response.status}: ${(await response.text()).slice(0, 220)}`);
      const payload = await response.json();
      const text = payload?.candidates?.[0]?.content?.parts?.map(part => part.text || '').join('') || '';
      if (!text) throw new Error('Gemini returned no translated text.');
      return parseResponse(text);
    } catch (error) {
      lastError = error;
      if (attempt === MAX_RETRIES) break;
      if (!/rate\/service response/.test(error.message)) await sleep(2500 * attempt);
    }
    }
    throw lastError || new Error('Translation failed after retries.');
  };
  const translateSmaller = async (source, key = '') => {
    if (key === 'type' || source === null || typeof source !== 'object' && typeof source !== 'string') return source;
    try {
      const wrapper = { value: source };
      const result = await requestJson(buildHindiTranslationPrompt(wrapper, subject));
      assertSameShape(wrapper, result);
      return result.value;
    } catch (error) {
      if (!/shape|keys|value type|JSON|Unexpected token|Unexpected end/.test(error.message)) throw error;
      if (Array.isArray(source)) {
        const values = [];
        for (const item of source) values.push(await translateSmaller(item));
        return values;
      }
      if (source && typeof source === 'object') {
        const values = {};
        for (const [childKey, childValue] of Object.entries(source)) {
          values[childKey] = childKey === 'type' ? childValue : await translateSmaller(childValue, childKey);
        }
        return values;
      }
      throw error;
    }
  };
  let translated;
  try {
    translated = await requestJson(buildHindiTranslationPrompt(concepts, subject));
    assertSameShape(concepts, translated);
  } catch (error) {
    if (!/shape|keys|value type|JSON|Unexpected token|Unexpected end/.test(error.message)) throw error;
    console.log('  Retrying translation in smaller blocks to preserve the source structure.');
    translated = {};
    for (const [key, value] of Object.entries(concepts)) {
      translated[key] = key === 'type' ? value : await translateSmaller(value, key);
    }
    assertSameShape(concepts, translated);
  }
  for (let pass = 0; pass < 4; pass++) {
    const issues = [
      ...untranslatedLatinPaths(translated),
      ...numericTokenDifferences(concepts, translated, subject),
    ];
    if (!issues.length) break;
    console.log(`  Refining ${issues.length} script/number issues (pass ${pass + 1}).`);
    translated = await requestJson(buildHindiCleanupPrompt(translated, subject, issues.slice(0, 20)));
    assertSameShape(concepts, translated);
  }
  const remainingLatin = untranslatedLatinPaths(translated);
  if (remainingLatin.length) throw new Error(`Hindi layer still contains Latin prose: ${remainingLatin.slice(0, 3).join('; ')}`);
  const remainingNumbers = numericTokenDifferences(concepts, translated, subject);
  if (remainingNumbers.length) throw new Error(`Translation changed numeric facts: ${remainingNumbers.slice(0, 3).join('; ')}`);
  return translated;
}

function setInlineConcepts(html, concepts) {
  const open = '<script id="upsc-page-data" type="application/json">';
  const start = html.indexOf(open);
  if (start < 0) throw new Error('index.html is missing upsc-page-data.');
  const contentStart = start + open.length;
  const end = html.indexOf('</script>', contentStart);
  if (end < 0) throw new Error('index.html has an unterminated upsc-page-data script.');
  const data = JSON.parse(html.slice(contentStart, end).trim());
  data.concepts = concepts;
  return `${html.slice(0, contentStart)}\n${JSON.stringify(data, null, 2)}\n${html.slice(end)}`;
}

function atomicWrite(file, contents) {
  const temp = `${file}.${process.pid}.tmp`;
  fs.writeFileSync(temp, contents, 'utf8');
  fs.renameSync(temp, file);
}

async function main() {
  loadEnv();
  const apiKey = process.env.GEMINI_API_KEY;
  if (!apiKey) throw new Error('GEMINI_API_KEY is not configured.');
  const args = process.argv.slice(2);
  const subjectArg = args.find(arg => arg.startsWith('--subject='))?.slice('--subject='.length);
  const topicArg = args.find(arg => arg.startsWith('--topic='))?.slice('--topic='.length);
  const concurrencyArg = Number(args.find(arg => arg.startsWith('--concurrency='))?.slice('--concurrency='.length) || 2);
  const concurrency = Number.isInteger(concurrencyArg) ? Math.max(1, Math.min(3, concurrencyArg)) : 2;
  const subjects = subjectArg ? [subjectArg] : ['hindi', 'sanskrit'];
  if (subjects.some(subject => !['hindi', 'sanskrit'].includes(subject))) throw new Error('Subject must be hindi or sanskrit.');
  let total = 0;
  let newlyTranslated = 0;
  let failed = 0;
  const failures = [];
  const changedScopes = new Set();
  const groups = subjects.map(subject => {
    const subjectDir = path.join(ROOT, 'up-assistant-teacher', subject);
    const topics = fs.readdirSync(subjectDir, { withFileTypes: true })
      .filter(entry => entry.isDirectory())
      .map(entry => entry.name)
      .filter(name => fs.existsSync(path.join(subjectDir, name, 'tabs', 'concepts.json')))
      .filter(name => !topicArg || name === topicArg)
      .sort();
    return { subject, topics };
  });
  if (topicArg && !groups.some(group => group.topics.includes(topicArg))) {
    throw new Error(`Topic ${topicArg} was not found under ${subjects.join(' or ')}.`);
  }
  const jobs = groups.flatMap(({ subject, topics }) => topics.map(topic => ({ subject, topic })));
  let cursor = 0;
  const processJob = async ({ subject, topic }, number) => {
    const topicDir = path.join(ROOT, 'up-assistant-teacher', subject, topic);
    const conceptsPath = path.join(topicDir, 'tabs', 'concepts.json');
    const dataPath = path.join(topicDir, 'data.json');
    const htmlPath = path.join(topicDir, 'index.html');
    try {
      const source = JSON.parse(fs.readFileSync(conceptsPath, 'utf8'));
      const english = isBilingualConcepts(source) ? extractEnglishValues(source) : source;
      let bilingual = source;
      const needsTranslation = !isBilingualConcepts(source)
        || untranslatedLatinPaths(source).length > 0
        || numericTokenDifferences(extractEnglishValues(source), extractHindiValues(source), subject).length > 0;
      if (needsTranslation) {
        console.log(`[${number}/${jobs.length}] Translating ${subject}/${topic}`);
        const translated = await translate(english, subject, apiKey);
        bilingual = pairTranslatedValues(english, translated);
        newlyTranslated++;
      } else {
        console.log(`[${number}/${jobs.length}] Syncing existing translation ${subject}/${topic}`);
      }

      const data = JSON.parse(fs.readFileSync(dataPath, 'utf8'));
      data.concepts = bilingual;
      const html = setInlineConcepts(fs.readFileSync(htmlPath, 'utf8'), bilingual);
      atomicWrite(conceptsPath, `${JSON.stringify(bilingual, null, 2)}\n`);
      atomicWrite(dataPath, `${JSON.stringify(data, null, 2)}\n`);
      atomicWrite(htmlPath, html);
      changedScopes.add(`up-assistant-teacher/${subject}`);
    } catch (error) {
      failed++;
      failures.push({ subject, topic, error: error.message });
      console.error(`  Failed ${subject}/${topic}: ${error.message}`);
    }
  };
  const worker = async () => {
    while (cursor < jobs.length) {
      const number = ++total;
      const job = jobs[cursor++];
      await processJob(job, number);
      if (cursor < jobs.length && !topicArg) await sleep(REQUEST_DELAY_MS);
    }
  };
  await Promise.all(Array.from({ length: Math.min(concurrency, jobs.length) }, worker));

  console.log(JSON.stringify({ inspected: total, translated: newlyTranslated, failed, failures }, null, 2));
  if (failed) process.exitCode = 1;
  if (!args.includes('--no-prerender') && changedScopes.size) {
    const command = path.join(ROOT, 'scripts', 'prerender-seo-content.cjs');
    for (const scope of changedScopes) {
      const result = spawnSync(process.execPath, [command, `--scope=${scope}`, '--include-noindex'], { cwd: ROOT, stdio: 'inherit' });
      if (result.status !== 0) process.exitCode = result.status || 1;
    }
  }
}

main().catch(error => { console.error(error.message); process.exitCode = 1; });
