const fs = require('fs');

function loadEnv() {
  for (const p of ['.env', '../.env', 'upsc-aso/.env']) {
    if (fs.existsSync(p)) {
      for (const line of fs.readFileSync(p, 'utf8').split('\n')) {
        const m = line.match(/^\s*GEMINI_API_KEY\s*=\s*(.*)\s*$/);
        if (m) return m[1].trim().replace(/^['"]|['"]$/g, '');
      }
    }
  }
  return null;
}

const key = loadEnv();

async function testModel(modelName) {
  console.log(`\nTesting ${modelName}...`);
  const url = `https://generativelanguage.googleapis.com/v1beta/models/${modelName}:generateContent?key=${key}`;
  const payload = {
    contents: [{ parts: [{ text: 'Return JSON: {"success": true, "model": "' + modelName + '"}' }] }],
    generationConfig: { responseMimeType: 'application/json' }
  };
  const start = Date.now();
  const res = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  });
  const dur = Date.now() - start;
  console.log(`Status: ${res.status} (${dur}ms)`);
  if (!res.ok) {
    console.log('Error:', await res.text());
  } else {
    const data = await res.json();
    console.log('Output:', data.candidates[0].content.parts[0].text);
  }
}

async function main() {
  await testModel('gemini-3.6-flash');
  await testModel('gemini-3.5-flash-lite');
  await testModel('gemini-3.5-flash');
}

main().catch(console.error);
