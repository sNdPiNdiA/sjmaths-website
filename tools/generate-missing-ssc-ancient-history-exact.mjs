import dotenv from 'dotenv';
import fs from 'node:fs/promises';
import path from 'node:path';
import { render } from './reformat-ssc-ancient-history-like-upsssc.mjs';

dotenv.config();

const apiKey = process.env.GEMINI_API_KEY;
if (!apiKey) throw new Error('GEMINI_API_KEY is not set.');

const model = 'gemini-2.5-flash';
const delayMs = 12000;
const baseDir = path.resolve('ssc-cgl/general-awareness/history-and-culture');

const topics = [
  {
    slug: 'post-gupta-period',
    title: 'Post-Gupta Period: Harshavardhana & Southern Dynasties',
    focus: 'Harsha, Pushyabhutis, Banabhatta, Xuanzang, Chalukyas, Pallavas, Rashtrakutas, Sangam linkages, temples, regional powers'
  }
];

const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
const cleanJson = (text) => text.replace(/^```json\s*/i, '').replace(/^```\s*/i, '').replace(/```$/i, '').trim();

function promptFor(topic) {
  return `Create SSC CGL General Awareness study content for "${topic.title}".
Level: SSC CGL Tier 1 and Tier 2. Include high-frequency and previous-year-type facts commonly asked in SSC CGL, CHSL, CPO, MTS and Stenographer. Do not invent exact year/shift labels. Label PYQ section questions by pattern only.
Focus: ${topic.focus}

Return ONLY valid JSON:
{
  "description": "SEO description under 155 chars",
  "theory": [{"heading":"...", "bodyHtml":"HTML using p, ul, li, table, thead, tbody, tr, th, td only"}],
  "practice": [{"q":"...", "options":["...","...","...","..."], "answer":0, "explanation":"..."}],
  "pyqs": [{"q":"...", "options":["...","...","...","..."], "answer":0, "explanation":"..."}],
  "test": [{"q":"...", "options":["...","...","...","..."], "answer":0, "explanation":"..."}]
}
Counts required: theory 7 sections, practice 30 questions, pyqs 30 questions, test 15 questions.`;
}

async function generate(topic) {
  const url = `https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent?key=${apiKey}`;
  const res = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      contents: [{ parts: [{ text: promptFor(topic) }] }],
      generationConfig: { responseMimeType: 'application/json', temperature: 0.3 }
    })
  });
  if (!res.ok) throw new Error(`${res.status} ${res.statusText}: ${await res.text()}`);
  const data = await res.json();
  const text = data.candidates?.[0]?.content?.parts?.map((part) => part.text || '').join('') || '';
  return JSON.parse(cleanJson(text));
}

for (const [index, topic] of topics.entries()) {
  console.log(`[${index + 1}/${topics.length}] Generating ${topic.slug}`);
  const data = await generate(topic);
  data.title = topic.title;
  const filePath = path.join(baseDir, topic.slug, 'index.html');
  await fs.mkdir(path.dirname(filePath), { recursive: true });
  await fs.writeFile(filePath, render(topic.slug, data), 'utf8');
  console.log(`Wrote ${filePath}`);
  if (index < topics.length - 1) await sleep(delayMs);
}
