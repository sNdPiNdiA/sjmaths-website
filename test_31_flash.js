import fs from 'fs';

let apiKey = '';
const env = fs.readFileSync('.env', 'utf8');
for (const line of env.split('\n')) {
  if (line.startsWith('GEMINI_API_KEY=')) apiKey = line.split('=')[1].trim();
}

async function test() {
  const url = `https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-lite:generateContent?key=${apiKey}`;
  const payload = {
    contents: [{ parts: [{ text: 'Return JSON: {"status": "ok", "model": "gemini-3.1-flash-lite"}' }] }],
    generationConfig: { responseMimeType: 'application/json' }
  };
  const res = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  });
  const data = await res.json();
  console.log('Tested gemini-3.1-flash-lite:', data.candidates ? data.candidates[0].content.parts[0].text : data);
}

test();
