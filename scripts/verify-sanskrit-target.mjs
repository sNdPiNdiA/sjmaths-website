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

const sanskritFiles = walk(path.join(rootDir, 'sanskrit'));
console.log(`Total HTML files in sanskrit/: ${sanskritFiles.length}`);

function normalizeCss(css) {
  return css.replace(/\r\n/g, '\n').split('\n').map(l => l.trim()).filter(Boolean).join('\n');
}

const targetHash = '33d4260a3be2';
const matchedFiles = [];
const otherStyleFiles = [];

for (const file of sanskritFiles) {
  const content = fs.readFileSync(file, 'utf8');
  const styleMatch = content.match(/<style\b[^>]*>([\s\S]*?)<\/style>/i);
  if (styleMatch) {
    const norm = normalizeCss(styleMatch[1]);
    const hash = crypto.createHash('sha256').update(norm).digest('hex').slice(0, 12);
    const rel = path.relative(rootDir, file).replace(/\\/g, '/');
    if (hash === targetHash) {
      matchedFiles.push(rel);
    } else {
      otherStyleFiles.push({ file: rel, hash, len: styleMatch[1].length });
    }
  }
}

console.log(`Matched files with hash ${targetHash}: ${matchedFiles.length}`);
console.log(`Other style files in sanskrit/: ${otherStyleFiles.length}`);
if (otherStyleFiles.length > 0) {
  console.log('Sample other style files:', otherStyleFiles.slice(0, 5));
}
