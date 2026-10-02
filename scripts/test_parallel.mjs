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
  const name = `KEY_${(keyIdx % API_KEYS.length) + 1}`;
  keyIdx++;
  return { client: new GoogleGenAI({ apiKey: key }), name };
}

async function callGemini(prompt, taskName = 'translate') {
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
      console.warn(`  [${taskName} Attempt ${attempt}/4] Error on ${name}: ${e.message?.slice(0, 100)}`);
      await new Promise(r => setTimeout(r, attempt * 1500));
    }
  }
  throw new Error(`${taskName} failed after 4 attempts`);
}

async function testParallel() {
  const t0 = Date.now();
  console.log('Testing parallel translation for Part 1 & Part 2...');
  const prompt1 = `Translate to Hindi: {"greeting": "Welcome to Indus Valley Civilisation study module"}`;
  const prompt2 = `Translate to Hindi: {"question": "What is the standard Harappan brick ratio?"}`;

  const [r1, r2] = await Promise.all([
    callGemini(prompt1, 'Part1'),
    callGemini(prompt2, 'Part2')
  ]);

  console.log(`Both completed in ${((Date.now() - t0)/1000).toFixed(2)}s!`);
  console.log('R1:', r1);
  console.log('R2:', r2);
}

testParallel().catch(console.error);
