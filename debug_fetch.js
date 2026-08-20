import fs from 'fs';

let apiKey = '';
const env = fs.readFileSync('.env', 'utf8');
for (const line of env.split('\n')) {
  if (line.startsWith('GEMINI_API_KEY=')) apiKey = line.split('=')[1].trim();
}

const prompt = `You are a premier UPSC CSE faculty. Write high-yield concepts & theory notes for the microtopic: "Antimatter Dark Matter".
Subject: Science and Tech | Parent: Physics Cosmic Physics

STRICT CONSTRAINTS:
1. ONLY English language strings.
2. NO long descriptive paragraphs. Keep explanations bulleted, crisp, analytical.
3. Return valid JSON.`;

const url = `https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-lite:generateContent?key=${apiKey}`;
const payload = {
  contents: [{ parts: [{ text: prompt }] }],
  generationConfig: { responseMimeType: 'application/json', temperature: 0.1 }
};

console.log('Sending request to gemini-3.1-flash-lite...');
const start = Date.now();
try {
  const res = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  });
  console.log('HTTP Status:', res.status, 'Time taken:', (Date.now() - start), 'ms');
  const data = await res.json();
  console.log('Response preview:', JSON.stringify(data).slice(0, 300));
} catch (e) {
  console.error('Fetch error:', e);
}
