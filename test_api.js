import fs from 'fs';
import path from 'path';

let apiKey = process.env.GEMINI_API_KEY;
if (!apiKey && fs.existsSync('.env')) {
  const envContent = fs.readFileSync('.env', 'utf8');
  for (const line of envContent.split('\n')) {
    if (line.startsWith('GEMINI_API_KEY=')) {
      apiKey = line.split('=')[1].trim();
    }
  }
}

async function testModel(model) {
  const url = `https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent?key=${apiKey}`;
  const payload = {
    contents: [{ parts: [{ text: `Return JSON: {"status": "success", "model": "${model}"}` }] }],
    generationConfig: { responseMimeType: 'application/json' }
  };
  try {
    const res = await fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    if (!res.ok) {
      const txt = await res.text();
      console.log(`[FAIL] ${model}: HTTP ${res.status} - ${txt}`);
      return false;
    }
    const data = await res.json();
    console.log(`[OK] ${model} works:`, data.candidates[0].content.parts[0].text);
    return true;
  } catch (err) {
    console.log(`[ERR] ${model}:`, err.message);
    return false;
  }
}

for (const m of ['gemini-2.5-flash', 'gemini-2.0-flash', 'gemini-1.5-flash']) {
  await testModel(m);
}
