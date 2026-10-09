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

const dir = path.join(rootDir, 'up-assistant-teacher');
const files = walk(dir);

function normalizeCss(css) {
  return css.replace(/\r\n/g, '\n').split('\n').map(l => l.trim()).filter(Boolean).join('\n');
}

const targetHashA = 'ec398f50c9e0';
const matchedA = [];
const other = [];

for (const f of files) {
  const content = fs.readFileSync(f, 'utf8');
  const styleMatch = content.match(/<style\b[^>]*>([\s\S]*?)<\/style>/i);
  if (styleMatch) {
    const norm = normalizeCss(styleMatch[1]);
    const hash = crypto.createHash('sha256').update(norm).digest('hex').slice(0, 12);
    const rel = path.relative(rootDir, f).replace(/\\/g, '/');
    if (hash === targetHashA) {
      matchedA.push(rel);
    } else {
      other.push({ file: rel, hash, len: styleMatch[1].length });
    }
  }
}

console.log(`Matched Cluster A (${targetHashA}): ${matchedA.length}`);
console.log(`Other files: ${other.length}`);
