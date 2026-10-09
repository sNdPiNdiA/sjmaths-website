import fs from 'fs';
import path from 'path';

const sampleFile = 'sanskrit/laukika-sahitya/gadya/nalachampu/prathama-ucchvasa/index.html';
const content = fs.readFileSync(sampleFile, 'utf8');

const match = content.match(/<style\b[^>]*>([\s\S]*?)<\/style>/i);
if (!match) {
  console.error('No style block found in sample file!');
  process.exit(1);
}

const rawCss = match[1];
console.log('Raw CSS length:', rawCss.length);
console.log('Raw CSS snippet:\n', rawCss.slice(0, 300));

// Let's create assets/css/sanskrit-topic.css
const cssTargetPath = 'assets/css/sanskrit-topic.css';
// Ensure clean unix newlines for consistent hashing and minification
const cleanCss = rawCss.replace(/\r\n/g, '\n').trim() + '\n';
fs.writeFileSync(cssTargetPath, cleanCss, 'utf8');
console.log(`Saved ${cleanCss.length} bytes to ${cssTargetPath}`);
