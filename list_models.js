import fs from 'fs';

let apiKey = '';
const env = fs.readFileSync('.env', 'utf8');
for (const line of env.split('\n')) {
  if (line.startsWith('GEMINI_API_KEY=')) apiKey = line.split('=')[1].trim();
}

const res = await fetch(`https://generativelanguage.googleapis.com/v1beta/models?key=${apiKey}`);
const data = await res.json();
const flashModels = data.models ? data.models.map(m => m.name.replace('models/', '')).filter(m => m.includes('flash') || m.includes('lite') || m.includes('gemini')) : [];
console.log('Available models:', flashModels);
