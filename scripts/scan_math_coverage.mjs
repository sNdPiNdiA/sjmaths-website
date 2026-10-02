import fs from 'fs';
import path from 'path';

const ROOT = process.cwd();
const IGNORE_DIRS = new Set(['node_modules', '.git', '.gemini', 'dist', 'build', '.cache']);

function findHtmlFiles(dir) {
  let results = [];
  try {
    const list = fs.readdirSync(dir, { withFileTypes: true });
    for (const item of list) {
      if (item.isDirectory()) {
        if (!IGNORE_DIRS.has(item.name)) {
          results.push(...findHtmlFiles(path.join(dir, item.name)));
        }
      } else if (item.isFile() && item.name.endsWith('.html')) {
        results.push(path.join(dir, item.name));
      }
    }
  } catch (e) {}
  return results;
}

const allHtmls = findHtmlFiles(ROOT);
console.log(`Total HTML files found: ${allHtmls.length}`);

// Patterns that indicate math formulas that need KaTeX/MathJax
const mathPatterns = [
  /\\\([^\)]+\\\)/,           // \( ... \)
  /\\\[[^\]]+\\\]/,           // \[ ... \]
  /\$\$[^\$]+\$\$/,           // $$ ... $$
  /(?<!\$)\$(?!\$)[^\$\n\r]+(?<!\$)\$(?!\$)/, // $ ... $
  /\\frac\{[^\}]+\}\{[^\}]+\}/, // \frac{}{}
  /\\sqrt\{[^\}]+\}/,         // \sqrt{}
  /\\times/,
  /\\approx/,
  /\\degree/,
  /\\pi/,
  /\\theta/,
  /\\alpha/,
  /\\beta/,
  /\\sum_/,
  /\\int_/
];

const filesWithMath = [];
const missingMathEngine = [];

for (const file of allHtmls) {
  const content = fs.readFileSync(file, 'utf8');
  let hasMath = false;
  for (const pat of mathPatterns) {
    if (pat.test(content)) {
      hasMath = true;
      break;
    }
  }

  if (hasMath) {
    filesWithMath.push(file);
    const hasKatex = content.includes('katex.min.js') || content.includes('katex.min.css') || content.includes('up-upper-primary-topic.min.js') || content.includes('up-upper-primary-topic.js');
    const hasMathJax = content.includes('mathjax') || content.includes('MathJax');
    if (!hasKatex && !hasMathJax) {
      missingMathEngine.push(file);
    }
  }
}

console.log(`Files with Math expressions: ${filesWithMath.length}`);
console.log(`Files missing Math engine: ${missingMathEngine.length}`);
if (missingMathEngine.length > 0) {
  console.log('Sample missing files:', missingMathEngine.slice(0, 15));
}
