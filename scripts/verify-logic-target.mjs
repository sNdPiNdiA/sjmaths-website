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

const logicFiles = walk(path.join(rootDir, 'logic'));
console.log(`Total HTML files in logic/: ${logicFiles.length}`);

function normalizeCss(css) {
  return css.replace(/\r\n/g, '\n').split('\n').map(l => l.trim()).filter(Boolean).join('\n');
}

const targetHash = '5e3e56c3b4f7';
const matchedFiles = [];
const otherFiles = [];

for (const file of logicFiles) {
  const content = fs.readFileSync(file, 'utf8');
  const styleMatch = content.match(/<style\b[^>]*>([\s\S]*?)<\/style>/i);
  if (styleMatch) {
    const norm = normalizeCss(styleMatch[1]);
    const hash = crypto.createHash('sha256').update(norm).digest('hex').slice(0, 12);
    const rel = path.relative(rootDir, file).replace(/\\/g, '/');
    if (hash === targetHash) {
      matchedFiles.push(rel);
    } else {
      otherFiles.push({ file: rel, hash, len: styleMatch[1].length });
    }
  } else {
    otherFiles.push({ file: path.relative(rootDir, file).replace(/\\/g, '/'), reason: 'no style' });
  }
}

console.log(`Matched files with hash ${targetHash}: ${matchedFiles.length} / ${logicFiles.length}`);
if (otherFiles.length > 0) {
  console.log('Other files:', otherFiles);
}
