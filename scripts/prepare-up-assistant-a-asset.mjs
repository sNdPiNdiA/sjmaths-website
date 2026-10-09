import fs from 'fs';

const sampleFile = 'up-assistant-teacher/child-psychology/creating-conducive-learning-environment/index.html';
const content = fs.readFileSync(sampleFile, 'utf8');

const match = content.match(/<style\b[^>]*>([\s\S]*?)<\/style>/i);
if (!match) {
  console.error('No style block found in sample file!');
  process.exit(1);
}

const rawCss = match[1];
const cssTargetPath = 'assets/css/up-assistant-teacher-topic.css';
const cleanCss = rawCss.replace(/\r\n/g, '\n').trim() + '\n';
fs.writeFileSync(cssTargetPath, cleanCss, 'utf8');
console.log(`Saved ${cleanCss.length} bytes to ${cssTargetPath}`);
