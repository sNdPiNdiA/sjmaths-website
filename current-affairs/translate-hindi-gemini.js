import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { GoogleGenAI } from '@google/genai';

const root = path.dirname(fileURLToPath(import.meta.url));
const weeklyRoot = path.join(root, 'data', 'weekly');
const model = process.env.GEMINI_MODEL || 'gemini-2.5-flash-lite';
const apiKey = process.env.GEMINI_API_KEY || process.env.GOOGLE_API_KEY;
if (!apiKey) throw new Error('Set GEMINI_API_KEY or GOOGLE_API_KEY before running this script.');
if (/^(your[-_ ]?api[-_ ]?key|replace[-_ ]?me|changeme|AIza\.\.\.)$/i.test(apiKey.trim()) || apiKey.includes('...')) {
  throw new Error('GEMINI_API_KEY is still a placeholder. Set it to a real Google Gemini API key.');
}
const ai = new GoogleGenAI({ apiKey });

function jsonFiles(dir) {
  return fs.readdirSync(dir, { withFileTypes: true }).flatMap(entry => {
    const full = path.join(dir, entry.name);
    return entry.isDirectory() ? jsonFiles(full) : entry.name.endsWith('.json') ? [full] : [];
  }).sort();
}
const requestedFiles = process.argv.slice(2).map(file => path.resolve(process.cwd(), file));
const targetFiles = requestedFiles.length ? requestedFiles : jsonFiles(weeklyRoot);
let lastRequestAt = 0;

function parseJson(text) {
  const clean = text.trim().replace(/^```json\s*/i, '').replace(/```$/i, '').trim();
  return JSON.parse(clean);
}

async function translateBatch(topics, attempt = 1) {
  const elapsed = Date.now() - lastRequestAt;
  if (elapsed < 15000) await new Promise(resolve => setTimeout(resolve, 15000 - elapsed));
  lastRequestAt = Date.now();
  const prompt = `Translate the following English current-affairs topics into accurate, natural Hindi for Indian competitive-exam students. Return ONLY a JSON array in the same order. Translate category and importance too: category and importance must be Hindi, not English. Do not omit facts. Keep proper names, organizations, laws, schemes, acronyms, units, dates, ranges, and numbers accurate; transliterate where natural and retain the English term in parentheses when useful. Do not add facts. Each object must contain exactly: category, title, importance, facts (array), detail, exam, remember.\n\nEnglish topics:\n${JSON.stringify(topics)}`;
  try {
    const response = await ai.models.generateContent({
      model,
      contents: prompt,
      config: { temperature: 0.2, responseMimeType: 'application/json' }
    });
    const result = parseJson(response.text || '');
    if (!Array.isArray(result) || result.length !== topics.length) throw new Error(`Expected ${topics.length} translations, received ${result.length}`);
    for (const item of result) {
      if (!item.category || !item.title || !Array.isArray(item.facts) || !item.detail || !item.exam || !item.remember) throw new Error('Incomplete translation object');
    }
    return result;
  } catch (error) {
    const status = error?.status || error?.error?.code;
    if (status === 400 || status === 401 || status === 403) throw error;
    if (attempt >= 3) throw error;
    const waitMs = status === 429 ? 65000 : attempt * 2500;
    console.warn(`Gemini request failed (${status || 'unknown'}); retrying in ${Math.round(waitMs / 1000)}s.`);
    await new Promise(resolve => setTimeout(resolve, waitMs));
    return translateBatch(topics, attempt + 1);
  }
}

for (const file of targetFiles) {
  const data = JSON.parse(fs.readFileSync(file, 'utf8').replace(/^\uFEFF/, ''));
  const topics = data.topics || [];
  const pending = topics.filter(topic => !topic.hi || !topic.hi.title || !topic.hi.facts?.length || !topic.hi.detail || !topic.hi.exam || !topic.hi.remember);
  if (!pending.length) { console.log(`Skipped ${path.relative(root, file)}: already complete`); continue; }
  const batch = pending.map(({ id, category, title, importance, facts, detail, exam, remember }) => ({ id, category, title, importance, facts, detail, exam, remember }));
  const translations = await translateBatch(batch);
  translations.forEach((hi, index) => { pending[index].hi = hi; });
  fs.writeFileSync(file, `${JSON.stringify(data, null, 2)}\n`, 'utf8');
  console.log(`Translated ${path.relative(root, file)} in one request: ${topics.length}/${topics.length} total`);
}
