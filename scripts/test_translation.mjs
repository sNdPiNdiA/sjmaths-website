import 'dotenv/config';
import { GoogleGenAI } from '@google/genai';

const keys = [process.env.GEMINI_API_KEY_1, process.env.GEMINI_API_KEY_2, process.env.GEMINI_API_KEY].filter(Boolean);

for (let i = 0; i < keys.length; i++) {
  const ai = new GoogleGenAI({ apiKey: keys[i] });
  for (const m of ['gemini-3.1-flash-lite', 'gemini-3.5-flash-lite']) {
    try {
      const res = await ai.models.generateContent({
        model: m,
        contents: 'Translate into Hindi for academic exam notes: "The Harappan civilization had an advanced underground drainage system."'
      });
      console.log(`KEY_${i+1} [${m}]:`, res.text?.trim()?.slice(0, 100));
    } catch (e) {
      console.log(`KEY_${i+1} [${m}] ERR:`, e.status || e.message?.slice(0, 60));
    }
  }
}
