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
async function main() {
  const res = await fetch(`https://generativelanguage.googleapis.com/v1beta/models?key=${key}`);
  const data = await res.json();
  if (data.models) {
    console.log('Available models:');
    data.models
      .filter(m => m.supportedGenerationMethods && m.supportedGenerationMethods.includes('generateContent'))
      .forEach(m => console.log(' - ' + m.name.replace('models/', '')));
  } else {
    console.log('Response:', data);
  }
}
main().catch(console.error);
