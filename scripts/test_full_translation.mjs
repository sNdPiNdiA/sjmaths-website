import fs from 'node:fs';
import path from 'node:path';
import 'dotenv/config';
import { GoogleGenAI } from '@google/genai';
import { jsonrepair } from 'jsonrepair';

const API_KEYS = [
  process.env.GEMINI_API_KEY_1,
  process.env.GEMINI_API_KEY_2,
  process.env.GEMINI_API_KEY
].filter(Boolean);

let keyIdx = 0;
function getAI() {
  const key = API_KEYS[keyIdx % API_KEYS.length];
  return { client: new GoogleGenAI({ apiKey: key }), name: `KEY_${(keyIdx % API_KEYS.length) + 1}` };
}
function rotate() { keyIdx++; }

function extractTopicData(filePath) {
  const html = fs.readFileSync(filePath, 'utf8');

  const leadMatch = html.match(/<p class="lead-desc">([\s\S]*?)<\/p>/);
  const leadDesc = leadMatch ? leadMatch[1].replace(/<[^>]+>/g, '').trim() : '';

  const focusMatch = html.match(/<strong>Syllabus Focus &amp; High-Yield Strategy:<\/strong>([\s\S]*?)<\/p>/);
  const syllabusFocus = focusMatch ? focusMatch[1].replace(/<[^>]+>/g, '').trim() : '';

  const concepts = [];
  const conceptRegex = /<div class="prep-card">\s*<h2>\s*<i class="fas fa-bookmark"[^>]*><\/i>\s*<span>([^<]+)<\/span>\s*<\/h2>\s*<div class="topic-content-body">([\s\S]*?)<\/div>\s*<\/div>/g;
  let cMatch;
  while ((cMatch = conceptRegex.exec(html)) !== null) {
    concepts.push({
      heading: cMatch[1].trim(),
      html_content: cMatch[2].trim()
    });
  }

  let comparativeTable = null;
  const tableTitleMatch = html.match(/<i class="fas fa-table-columns"[^>]*><\/i>\s*<span>([^<]+)<\/span>/);
  const tableMatch = html.match(/<table class="prep-table">([\s\S]*?)<\/table>/);
  if (tableTitleMatch && tableMatch) {
    const tableHtml = tableMatch[1];
    const ths = [...tableHtml.matchAll(/<th>([\s\S]*?)<\/th>/g)].map(m => m[1].replace(/<[^>]+>/g, '').trim());
    const rows = [];
    const trRegex = /<tr>([\s\S]*?)<\/tr>/g;
    let trMatch;
    while ((trMatch = trRegex.exec(tableHtml)) !== null) {
      if (trMatch[1].includes('<th')) continue;
      const tds = [...trMatch[1].matchAll(/<td>([\s\S]*?)<\/td>/g)].map(m => m[1].trim());
      if (tds.length) rows.push(tds);
    }
    comparativeTable = {
      title: tableTitleMatch[1].trim(),
      headers: ths,
      rows: rows
    };
  }

  let testData = [];
  const testDataMatch = html.match(/const testData\s*=\s*(\[[\s\S]*?\]);\s*<\/script>/);
  if (testDataMatch) {
    try {
      testData = JSON.parse(testDataMatch[1]);
    } catch (e) {
      console.warn('Failed to parse testData JSON:', e.message);
    }
  }

  const facts = [];
  const factRegex = /<div class="revision-fact-row">\s*<span class="fact-num-badge">[^<]+<\/span>\s*<div class="fact-text-col">([\s\S]*?)<\/div>\s*<\/div>/g;
  let fMatch;
  while ((fMatch = factRegex.exec(html)) !== null) {
    facts.push(fMatch[1].replace(/<[^>]+>/g, '').trim());
  }

  const mnemonics = [];
  const mnemRegex = /<div class="mnemonic-card">[\s\S]*?<h3[^>]*>[\s\S]*?<i class="fas fa-lightbulb"><\/i>\s*([\s\S]*?)<\/h3>[\s\S]*?<code>([\s\S]*?)<\/code>[\s\S]*?<p[^>]*>([\s\S]*?)<\/p>\s*<\/div>/g;
  let mMatch;
  while ((mMatch = mnemRegex.exec(html)) !== null) {
    mnemonics.push({
      title: mMatch[1].replace(/<[^>]+>/g, '').trim(),
      acronym: mMatch[2].trim(),
      expansion: mMatch[3].trim()
    });
  }

  const traps = [];
  const trapRegex = /<div class="trap-card-item">[\s\S]*?<p[^>]*>([\s\S]*?)<\/p>\s*<\/div>\s*<\/div>/g;
  let tMatch;
  while ((tMatch = trapRegex.exec(html)) !== null) {
    traps.push(tMatch[1].replace(/<[^>]+>/g, '').trim());
  }

  const checklist = [];
  const chkRegex = /<label class="mastery-check-item">[\s\S]*?<span>([\s\S]*?)<\/span>\s*<\/label>/g;
  let chkMatch;
  while ((chkMatch = chkRegex.exec(html)) !== null) {
    checklist.push(chkMatch[1].replace(/<[^>]+>/g, '').trim());
  }

  return {
    leadDesc,
    syllabusFocus,
    concepts,
    comparativeTable,
    testData,
    facts,
    mnemonics,
    traps,
    checklist
  };
}

async function callGemini(prompt) {
  for (let attempt = 1; attempt <= 4; attempt++) {
    const { client, name } = getAI();
    try {
      const response = await client.models.generateContent({
        model: 'gemini-3.1-flash-lite',
        contents: prompt,
        config: {
          responseMimeType: 'application/json',
          temperature: 0.1,
        }
      });
      let raw = response.text?.trim() || '';
      if (raw.startsWith('```')) {
        raw = raw.replace(/^```(?:json)?\s*/i, '').replace(/```\s*$/, '').trim();
      }
      try {
        return JSON.parse(raw);
      } catch {
        return JSON.parse(jsonrepair(raw));
      }
    } catch (e) {
      console.warn(`  [Attempt ${attempt}/4] Error on ${name}: ${e.message?.slice(0, 100)}`);
      rotate();
      await new Promise(r => setTimeout(r, attempt * 2000));
    }
  }
  throw new Error('Gemini API call failed after 4 attempts');
}

async function testFullTopic() {
  const p = 'up-upper-primary-teacher/social-studies/indus-valley-civilisation/index.html';
  console.log('Extracting data from', p);
  const data = extractTopicData(p);

  console.log('Sending translation request for Part 1 (Theory & Concepts)...');
  const t0 = Date.now();
  const promptPart1 = `You are a Senior Bilingual Academic Translation Expert for SCERT Uttar Pradesh.
Translate the following theoretical study notes from English into standard, high-scoring academic Hindi (Devanagari, using authentic terminology from SCERT UP "Hamara Itihas" and NCERT Hindi books).
Preserve all HTML tags (<strong>, <code>, <div class="...">, <table>, <thead>, <tbody>, <tr>, <th>, <td>, <i>) exactly intact, translating only the human-readable text.

TOPIC: Indus Valley Civilisation (सिंधु घाटी सभ्यता)

INPUT JSON:
${JSON.stringify({
  lead_desc: data.leadDesc,
  syllabus_focus: data.syllabusFocus,
  concepts: data.concepts,
  comparative_table: data.comparativeTable
}, null, 2)}

OUTPUT FORMAT (RAW JSON ONLY):
{
  "lead_desc": "...",
  "syllabus_focus": "...",
  "concepts": [
    { "heading": "...", "html_content": "..." }
  ],
  "comparative_table": {
    "title": "...",
    "headers": ["...", "..."],
    "rows": [["...", "..."]]
  }
}`;

  const resPart1 = await callGemini(promptPart1);
  console.log(`Part 1 translated in ${((Date.now() - t0)/1000).toFixed(2)}s`);
  console.log('Sample Concept 1 Heading (Hindi):', resPart1.concepts?.[0]?.heading);

  console.log('Sending translation request for Part 2 (10 MCQs, Facts, Mnemonics, Traps, Checklist)...');
  const t1 = Date.now();
  const promptPart2 = `You are a Senior Bilingual Academic Translation Expert for SCERT Uttar Pradesh.
Translate the following 10 practice MCQs, rapid recall facts, mnemonics, exam traps, and mastery checklist into standard academic Hindi.
1. For MCQs, keep the exact same correct_index (0-based) and ensure options correspond accurately.
2. For mnemonics, translate the title, keep the acronym, and translate the expansion/explanation.
3. Preserve any HTML tags intact.

INPUT JSON:
${JSON.stringify({
  mcqs: data.testData,
  facts: data.facts,
  mnemonics: data.mnemonics,
  traps: data.traps,
  checklist: data.checklist
}, null, 2)}

OUTPUT FORMAT (RAW JSON ONLY):
{
  "mcqs": [
    { "question": "...", "options": ["...", "...", "...", "..."], "correct_index": 0, "explanation": "..." }
  ],
  "facts": ["...", "..."],
  "mnemonics": [
    { "title": "...", "acronym": "...", "expansion": "..." }
  ],
  "traps": ["...", "..."],
  "checklist": ["...", "..."]
}`;

  const resPart2 = await callGemini(promptPart2);
  console.log(`Part 2 translated in ${((Date.now() - t1)/1000).toFixed(2)}s`);
  console.log('Sample MCQ 1 Question (Hindi):', resPart2.mcqs?.[0]?.question);
  console.log('Sample MCQ 1 Options (Hindi):', resPart2.mcqs?.[0]?.options);
  console.log('Sample Fact 1 (Hindi):', resPart2.facts?.[0]);
  console.log('Sample Mnemonic 1 (Hindi):', resPart2.mnemonics?.[0]);
}

testFullTopic().catch(console.error);
