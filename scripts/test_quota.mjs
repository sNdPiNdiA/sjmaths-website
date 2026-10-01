import 'dotenv/config';
import { GoogleGenAI } from '@google/genai';

async function testKey(name, key) {
  const ai = new GoogleGenAI({ apiKey: key });
  try {
    const res = await ai.models.generateContent({
      model: 'gemini-3.5-flash-lite',
      contents: 'Respond with JSON: {"status": "ok"}',
      config: { responseMimeType: 'application/json' }
    });
    console.log(`${name} SUCCESS:`, res.text.trim());
  } catch (err) {
    console.log(`${name} ERROR:`, err.message);
  }
}

console.log('Testing GEMINI_API_KEY_2:');
await testKey('GEMINI_API_KEY_2', process.env.GEMINI_API_KEY_2);

console.log('\nTesting GEMINI_API_KEY_1:');
await testKey('GEMINI_API_KEY_1', process.env.GEMINI_API_KEY_1);
