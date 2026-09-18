import 'dotenv/config';
import { GoogleGenAI } from '@google/genai';

async function testKeys() {
  const keys = [
    { name: 'GEMINI_API_KEY_1', val: process.env.GEMINI_API_KEY_1 },
    { name: 'GEMINI_API_KEY_2', val: process.env.GEMINI_API_KEY_2 },
    { name: 'GEMINI_API_KEY', val: process.env.GEMINI_API_KEY }
  ];

  for (const k of keys) {
    if (!k.val) {
      console.log(`${k.name}: NOT SET`);
      continue;
    }
    const preview = `${k.val.slice(0, 8)}...${k.val.slice(-4)}`;
    console.log(`Testing ${k.name} (${preview}):`);
    try {
      const ai = new GoogleGenAI({ apiKey: k.val });
      const response = await ai.models.generateContent({
        model: 'gemini-3.1-flash-lite',
        contents: 'Say OK if you are responding.',
      });
      console.log(`  SUCCESS -> ${response.text.trim()}`);
    } catch (err) {
      console.log(`  FAILED -> ${err.message}`);
    }
  }
}

testKeys();
