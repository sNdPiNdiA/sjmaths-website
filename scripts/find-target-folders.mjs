import fs from 'fs';
import path from 'path';
import crypto from 'crypto';

const rootDir = process.cwd();

function walk(dir, fileList = []) {
  const files = fs.readdirSync(dir);
  for (const file of files) {
    if (file === 'node_modules' || file === '.git' || file === '.gemini' || file === 'dist') continue;
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

const htmlFiles = walk(rootDir);

function normalizeCss(css) {
  return css.replace(/\r\n/g, '\n').split('\n').map(l => l.trim()).filter(Boolean).join('\n');
}

const targetHashes = {
  '33d4260a3be2': [],
  '5e3e56c3b4f7': [],
  'ec398f50c9e0': [],
  '34bbd6deca78': [],
  '8786125ad489': []
};

for (const file of htmlFiles) {
  const content = fs.readFileSync(file, 'utf8');
  const styleRegex = /<style\b[^>]*>([\s\S]*?)<\/style>/gi;
  let match;
  while ((match = styleRegex.exec(content)) !== null) {
    const raw = match[1];
    const norm = normalizeCss(raw);
    const hash = crypto.createHash('sha256').update(norm).digest('hex').slice(0, 12);
    if (targetHashes[hash]) {
      targetHashes[hash].push(path.relative(rootDir, file).replace(/\\/g, '/'));
    }
  }
}

for (const [hash, fileList] of Object.entries(targetHashes)) {
  console.log(`\nHash ${hash}: ${fileList.length} files`);
  const folderCounts = {};
  fileList.forEach(f => {
    const prefix = f.split('/').slice(0, 2).join('/');
    folderCounts[prefix] = (folderCounts[prefix] || 0) + 1;
  });
  console.log('Folder breakdown:', folderCounts);
}
