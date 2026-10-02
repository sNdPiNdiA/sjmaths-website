import fs from 'fs';
import path from 'path';

const ROOT = process.cwd();
const EXCLUDE = new Set(['.git', 'node_modules', '.gemini', 'scratch', 'outputs', '.vscode', '.idea', 'dist', 'build']);

const topDirs = fs.readdirSync(ROOT, { withFileTypes: true })
  .filter(d => d.isDirectory() && !EXCLUDE.has(d.name) && !d.name.startsWith('.'))
  .map(d => d.name);

console.log('Top dirs to scan:', topDirs.length);

let totalHtml = 0;
let filesWithMath = 0;
let filesWithKatex = 0;
let filesMissingKatex = [];

function checkDir(dir) {
  let entries;
  try {
    entries = fs.readdirSync(dir, { withFileTypes: true });
  } catch(e) {
    return;
  }
  for (const entry of entries) {
    if (EXCLUDE.has(entry.name) || entry.name.startsWith('.')) continue;
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      checkDir(full);
    } else if (entry.isFile() && entry.name.endsWith('.html')) {
      totalHtml++;
      const content = fs.readFileSync(full, 'utf8');
      const hasMath = /\$[a-zA-Z0-9\\(+\-\^_\s\.\/]{2,}\$/.test(content) ||
                      content.includes('\\frac{') ||
                      content.includes('\\sqrt{') ||
                      content.includes('\\Delta') ||
                      content.includes('\\times') ||
                      content.includes('\\sum') ||
                      content.includes('\\int');
      if (hasMath) {
        filesWithMath++;
        const hasK = content.includes('katex.min.js') || 
                     content.includes('up-upper-primary-topic.min.js') ||
                     content.includes('mathjax') ||
                     content.includes('MathJax');
        if (hasK) {
          filesWithKatex++;
        } else {
          filesMissingKatex.push(full);
        }
      }
    }
  }
}

for (const d of topDirs) {
  const start = Date.now();
  checkDir(path.join(ROOT, d));
  // console.log(`Scanned ${d} in ${Date.now() - start}ms`);
}

console.log(`ALL REPO - Total HTML files scanned: ${totalHtml}`);
console.log(`Files with Math expressions: ${filesWithMath}`);
console.log(`Files with KaTeX/MathJax: ${filesWithKatex}`);
console.log(`Files missing KaTeX/MathJax: ${filesMissingKatex.length}`);
if (filesMissingKatex.length > 0) {
  console.log('Sample missing files (first 25):', filesMissingKatex.slice(0, 25).map(f => path.relative(ROOT, f)));
}
