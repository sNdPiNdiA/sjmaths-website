import fs from 'fs';
import path from 'path';

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
const groups = {};

for (const file of htmlFiles) {
  const content = fs.readFileSync(file, 'utf8');
  const styleMatch = content.match(/<style\b[^>]*>([\s\S]*?)<\/style>/i);
  if (styleMatch && styleMatch[1].includes(':root{--bg:#f6f8fb;--paper:#fff;--ink:#182238;--ink2:#4c576b')) {
    const rootLine = styleMatch[1].split('\n')[0].trim();
    const rel = path.relative(rootDir, file).replace(/\\/g, '/');
    const folder = rel.split('/')[0];
    if (!groups[rootLine]) {
      groups[rootLine] = { count: 0, folders: new Set(), samples: [] };
    }
    groups[rootLine].count++;
    groups[rootLine].folders.add(folder);
    if (groups[rootLine].samples.length < 3) groups[rootLine].samples.push(rel);
  }
}

for (const [rootLine, info] of Object.entries(groups)) {
  console.log(`\nCount: ${info.count}`);
  console.log(`Root: ${rootLine}`);
  console.log(`Folders: ${[...info.folders].join(', ')}`);
  console.log(`Samples: ${info.samples.join(', ')}`);
}
