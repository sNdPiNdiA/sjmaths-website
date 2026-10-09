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

const hashMap = {};

for (const f of files) {
  const content = fs.readFileSync(f, 'utf8');
  const styleMatch = content.match(/<style\b[^>]*>([\s\S]*?)<\/style>/i);
  const rel = path.relative(rootDir, f).replace(/\\/g, '/');
  if (styleMatch) {
    const norm = normalizeCss(styleMatch[1]);
    const hash = crypto.createHash('sha256').update(norm).digest('hex').slice(0, 12);
    if (!hashMap[hash]) hashMap[hash] = { count: 0, len: styleMatch[1].length, samples: [] };
    hashMap[hash].count++;
    if (hashMap[hash].samples.length < 2) hashMap[hash].samples.push(rel);
  } else {
    if (!hashMap['NO_STYLE']) hashMap['NO_STYLE'] = { count: 0, len: 0, samples: [] };
    hashMap['NO_STYLE'].count++;
  }
}

for (const [hash, data] of Object.entries(hashMap)) {
  console.log(`Hash: ${hash} | Count: ${data.count} | Size: ${data.len}B | Samples: ${data.samples.slice(0, 2).join(', ')}`);
}
