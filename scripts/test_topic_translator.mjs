import fs from 'node:fs';
import path from 'node:path';
import 'dotenv/config';
import { GoogleGenAI } from '@google/genai';
import { jsonrepair } from 'jsonrepair';

const ROOT = process.cwd();
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

function rotate() {
  keyIdx++;
}

async function translateContent(enData, topicNameEn, topicNameHi) {
  const prompt = `You are a Senior Bilingual Translation Expert and Master Question Paper Setter for SCERT Uttar Pradesh.
Translate the following academic study content from English to clean, standard academic Hindi (as used in SCERT UP "Hamara Itihas", "Hamara Vigyan", and NCERT Hindi medium textbooks) for the UP Upper Primary Assistant Teacher Recruitment Examination (Super TET Junior).

Topic: ${topicNameEn} (${topicNameHi})

INPUT JSON TO TRANSLATE INTO HINDI:
${JSON.stringify(enData, null, 2)}

TRANSLATION INSTRUCTIONS:
1. Translate all text values into natural, grammatically flawless, authoritative academic Hindi.
2. Keep technical and standard names in Devanagari with English in parentheses where appropriate (e.g., "सिंधु घाटी सभ्यता (Indus Valley Civilisation)").
3. Preserve all HTML tags (<strong>, <code>, <div class="...">, <table>, <thead>, <tbody>, <tr>, <th>, <td>, <i>) exactly intact, only translating the human-readable text content inside them.
4. For MCQs, keep the exact same correct_index (0-based) and ensure options correspond accurately.
5. Return ONLY a valid JSON object matching the exact input structure.

RESPONSE FORMAT (RAW JSON ONLY):
{
  "key_focus_summary": "...",
  "concepts": [
    { "heading": "...", "html_content": "..." },
    { "heading": "...", "html_content": "..." },
    { "heading": "...", "html_content": "..." },
    { "heading": "...", "html_content": "..." }
  ],
  "comparative_table": {
    "title": "...",
    "headers": ["...", "...", "...", "..."],
    "rows": [ ["...", "...", "...", "..."] ]
  },
  "mcqs": [
    { "question": "...", "options": ["...", "...", "...", "..."], "correct_index": 0, "explanation": "..." }
  ],
  "revision_facts": ["...", "..."],
  "mnemonics": [ { "title": "...", "acronym": "...", "expansion": "..." } ],
  "exam_traps": ["...", "..."],
  "checklist_items": ["...", "..."]
}`;

  for (let attempt = 1; attempt <= 4; attempt++) {
    const { client, name } = getAI();
    try {
      const response = await client.models.generateContent({
        model: 'gemini-3.1-flash-lite',
        contents: prompt,
        config: {
          responseMimeType: 'application/json',
          temperature: 0.2,
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
      console.warn(`  [Attempt ${attempt}/4] Error on ${name}: ${e.message?.slice(0, 90)}`);
      rotate();
      await new Promise(r => setTimeout(r, attempt * 2000));
    }
  }
  throw new Error('Failed to translate topic content.');
}

async function test() {
  console.log('Testing translation of Indus Valley Civilisation...');
  const testInput = {
    key_focus_summary: "The Indus Valley Civilisation is renowned for its grid pattern town planning, advanced underground drainage, and standardized brick ratios.",
    concepts: [
      {
        heading: "1. Core Concepts & Foundational Principles",
        html_content: '<div class="point-grid"><div class="point-card"><strong>Grid System:</strong> Streets intersected at right angles dividing the city into rectangular blocks.</div></div><div class="tip-box"><i class="fas fa-lightbulb"></i> <strong>Exam Pro-Tip:</strong> The brick ratio was standardized at 4:2:1.</div>'
      }
    ],
    comparative_table: {
      title: "Comparison of Harappan Sites",
      headers: ["Site", "River", "Key Finding"],
      rows: [["Harappa", "Ravi", "Six granaries in a row"], ["Mohenjo-daro", "Indus", "Great Bath"]]
    },
    mcqs: [
      {
        question: "Which Harappan site is famous for the Great Bath?",
        options: ["Harappa", "Mohenjo-daro", "Lothal", "Kalibangan"],
        correct_index: 1,
        explanation: "Mohenjo-daro features the Great Bath lined with bitumen."
      }
    ],
    revision_facts: ["Standard brick dimension ratio: 4:2:1."],
    mnemonics: [{ title: "Major Sites", acronym: "HML", expansion: "Harappa, Mohenjo-daro, Lothal" }],
    exam_traps: ["Do not confuse Lothal (Gujarat) with Kalibangan (Rajasthan)."],
    checklist_items: ["Mastered the grid town planning system."]
  };

  const startTime = Date.now();
  const hiData = await translateContent(testInput, "Indus Valley Civilisation", "सिंधु घाटी सभ्यता");
  const elapsed = ((Date.now() - startTime) / 1000).toFixed(2);
  console.log(`Success in ${elapsed}s!`);
  console.log('Translated Summary:', hiData.key_focus_summary);
  console.log('Translated Concept 1 Heading:', hiData.concepts?.[0]?.heading);
  console.log('Translated Concept 1 HTML:', hiData.concepts?.[0]?.html_content?.slice(0, 150));
  console.log('Translated MCQ 1 Question:', hiData.mcqs?.[0]?.question);
}

test().catch(console.error);
