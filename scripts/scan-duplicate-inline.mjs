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

console.log('Scanning HTML files...');
const htmlFiles = walk(rootDir);
console.log(`Found ${htmlFiles.length} HTML files.`);

const styleMap = new Map();
const scriptMap = new Map();

function normalizeCss(css) {
  return css.replace(/\r\n/g, '\n').split('\n').map(l => l.trim()).filter(Boolean).join('\n');
}

function normalizeJs(js) {
  return js.replace(/\r\n/g, '\n').split('\n').map(l => l.trim()).filter(Boolean).join('\n');
}

const styleRegex = /<style\b[^>]*>([\s\S]*?)<\/style>/gi;
const scriptRegex = /<script\b(?![^>]*\bsrc=)[^>]*>([\s\S]*?)<\/script>/gi;

for (const file of htmlFiles) {
  const content = fs.readFileSync(file, 'utf8');

  let match;
  while ((match = styleRegex.exec(content)) !== null) {
    const raw = match[1];
    if (raw.length < 300) continue;
    const norm = normalizeCss(raw);
    const hash = crypto.createHash('sha256').update(norm).digest('hex').slice(0, 12);
    if (!styleMap.has(hash)) {
      styleMap.set(hash, {
        type: 'style',
        rawSample: raw.slice(0, 100),
        byteLen: raw.length,
        normLen: norm.length,
        files: []
      });
    }
    styleMap.get(hash).files.push(path.relative(rootDir, file).replace(/\\/g, '/'));
  }

  while ((match = scriptRegex.exec(content)) !== null) {
    const raw = match[1];
    if (raw.length < 300) continue;
    // skip ld+json
    if (match[0].includes('application/ld+json')) continue;
    const norm = normalizeJs(raw);
    const hash = crypto.createHash('sha256').update(norm).digest('hex').slice(0, 12);
    if (!scriptMap.has(hash)) {
      scriptMap.set(hash, {
        type: 'script',
        rawSample: raw.slice(0, 100),
        byteLen: raw.length,
        normLen: norm.length,
        files: []
      });
    }
    scriptMap.get(hash).files.push(path.relative(rootDir, file).replace(/\\/g, '/'));
  }
}

const topStyles = [...styleMap.entries()]
  .map(([hash, data]) => ({ hash, ...data, totalSavings: (data.files.length - 1) * data.byteLen }))
  .filter(d => d.files.length >= 10)
  .sort((a, b) => b.totalSavings - a.totalSavings);

const topScripts = [...scriptMap.entries()]
  .map(([hash, data]) => ({ hash, ...data, totalSavings: (data.files.length - 1) * data.byteLen }))
  .filter(d => d.files.length >= 10)
  .sort((a, b) => b.totalSavings - a.totalSavings);

console.log('\n=== TOP DUPLICATE INLINE STYLES (>=10 files) ===');
for (const s of topStyles.slice(0, 15)) {
  console.log(`\nHash: ${s.hash} | Files: ${s.files.length} | Size: ${s.byteLen}B | Total Savings: ${(s.totalSavings / 1024).toFixed(1)} KB`);
  console.log(`Sample: ${s.rawSample.replace(/\s+/g, ' ').trim()}`);
  console.log(`Path preview: ${s.files.slice(0, 3).join(', ')}`);
}

console.log('\n=== TOP DUPLICATE INLINE SCRIPTS (>=10 files) ===');
for (const s of topScripts.slice(0, 15)) {
  console.log(`\nHash: ${s.hash} | Files: ${s.files.length} | Size: ${s.byteLen}B | Total Savings: ${(s.totalSavings / 1024).toFixed(1)} KB`);
  console.log(`Sample: ${s.rawSample.replace(/\s+/g, ' ').trim()}`);
  console.log(`Path preview: ${s.files.slice(0, 3).join(', ')}`);
}
