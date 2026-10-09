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
const matches = [];

for (const file of htmlFiles) {
  const content = fs.readFileSync(file, 'utf8');
  const styleRegex = /<style\b[^>]*>([\s\S]*?)<\/style>/gi;
  let m;
  while ((m = styleRegex.exec(content)) !== null) {
    if (m[1].includes(':root{--bg:#f6f8fb;--paper:#fff;--ink:#182238;--ink2:#4c576b')) {
      matches.push({
        file: path.relative(rootDir, file).replace(/\\/g, '/'),
        len: m[1].length,
        styleContent: m[1]
      });
      break;
    }
  }
}

console.log(`Found ${matches.length} files matching the shared theme style (:root{--bg:#f6f8fb;--paper:#fff;--ink:#182238)!`);
const lengthCounts = {};
matches.forEach(m => {
  lengthCounts[m.len] = (lengthCounts[m.len] || 0) + 1;
});
console.log('Length distribution:', lengthCounts);

// Check folders
const folderCounts = {};
matches.forEach(m => {
  const topFolder = m.file.split('/')[0];
  folderCounts[topFolder] = (folderCounts[topFolder] || 0) + 1;
});
console.log('Folder distribution:', folderCounts);

// Check if all style contents are identical when normalized
const firstNormalized = matches[0].styleContent.replace(/\r\n/g, '\n').trim();
let exactMatches = 0;
let diffFiles = [];
for (const m of matches) {
  const norm = m.styleContent.replace(/\r\n/g, '\n').trim();
  if (norm === firstNormalized) {
    exactMatches++;
  } else {
    diffFiles.push({ file: m.file, len: norm.length });
  }
}
console.log(`Exact matches to sample 1: ${exactMatches} / ${matches.length}`);
if (diffFiles.length > 0) {
  console.log('Sample non-exact matches:', diffFiles.slice(0, 5));
}
