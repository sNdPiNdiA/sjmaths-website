import fs from 'fs';
import path from 'path';
import crypto from 'crypto';

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

const dir = path.join(rootDir, 'music-instrumental');
const files = walk(dir);

function normalizeCss(css) {
  return css.replace(/\r\n/g, '\n').split('\n').map(l => l.trim()).filter(Boolean).join('\n');
}

const targetHash = 'e8bf2eed0cd4';
const matched = [];
const other = [];

for (const f of files) {
  const content = fs.readFileSync(f, 'utf8');
  const styleMatch = content.match(/<style\b[^>]*>([\s\S]*?)<\/style>/i);
  const rel = path.relative(rootDir, f).replace(/\\/g, '/');
  if (styleMatch) {
    const norm = normalizeCss(styleMatch[1]);
    const hash = crypto.createHash('sha256').update(norm).digest('hex').slice(0, 12);
    if (hash === targetHash) {
      matched.push(rel);
    } else {
      other.push({ file: rel, hash, len: styleMatch[1].length });
    }
  } else {
    other.push({ file: rel, reason: 'no style' });
  }
}

console.log(`Total HTML files in music-instrumental/: ${files.length}`);
console.log(`Matched target hash (${targetHash}): ${matched.length}`);
console.log(`Other files: ${other.length}`);
if (matched.length > 0) {
  console.log('Sample matched files:', matched.slice(0, 3));
}
if (other.length > 0) {
  console.log('Sample other files:', other.slice(0, 3));
}
