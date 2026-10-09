import fs from 'fs';
import path from 'path';

const rootDir = process.cwd();

function walk(dir, fileList = []) {
  const files = fs.readdirSync(dir);
  for (const file of files) {
    const filePath = path.join(dir, file);
    const stat = fs.statSync(filePath);
    if (stat.isDirectory()) {
      walk(filePath, fileList);
    } else if (file.endsWith('.html')) {
      fileList.push(filePath);
    }
  }
  return fileList;
}

const sanskritDir = path.join(rootDir, 'sanskrit', 'laukika-sahitya');
const files = walk(sanskritDir);
console.log(`Found ${files.length} HTML files in sanskrit/laukika-sahitya.`);

const sample = fs.readFileSync(files[0], 'utf8');
const sampleStyle = sample.match(/<style\b[^>]*>([\s\S]*?)<\/style>/i)?.[1]?.replace(/\r\n/g, '\n').trim();

let identical = 0;
let different = [];

for (const f of files) {
  const content = fs.readFileSync(f, 'utf8');
  const styleMatch = content.match(/<style\b[^>]*>([\s\S]*?)<\/style>/i);
  if (!styleMatch) {
    different.push({ file: f, reason: 'no style' });
    continue;
  }
  const norm = styleMatch[1].replace(/\r\n/g, '\n').trim();
  if (norm === sampleStyle) {
    identical++;
  } else {
    different.push({ file: f, len: norm.length, sampleLen: sampleStyle.length });
  }
}

console.log(`Identical: ${identical} / ${files.length}`);
if (different.length > 0) {
  console.log('Different files:', different);
}
