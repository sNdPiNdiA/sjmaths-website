import fs from 'fs';
import path from 'path';

const ROOT = process.cwd();
const EXCLUDE = new Set([
  'scratch', 'node_modules', '.git', '.gemini', 'outputs', 'dist', 'build', '.vscode', '.idea', 'assets'
]);

const KATEX_HEAD_BLOCK = `<!-- KaTeX for High-Fidelity Mathematical & Scientific Typesetting -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css" crossorigin="anonymous"/>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js" crossorigin="anonymous"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js" crossorigin="anonymous"></script>
<script>
    document.addEventListener("DOMContentLoaded", function () {
        if (typeof renderMathInElement === 'function') {
            renderMathInElement(document.body, {
                delimiters: [
                    { left: '$$', right: '$$', display: true },
                    { left: '$', right: '$', display: false },
                    { left: '\\\\(', right: '\\\\)', display: false },
                    { left: '\\\\[', right: '\\\\]', display: true }
                ],
                ignoredTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code', 'option'],
                throwOnError: false
            });
        }
    });
</script>`;

function hasMathExpression(html) {
    return /\$[a-zA-Z0-9\\(+\-\^_\s\.\/]{2,}\$/.test(html) ||
           html.includes('\\frac{') ||
           html.includes('\\sqrt{') ||
           html.includes('\\Delta') ||
           html.includes('\\times') ||
           html.includes('\\pm') ||
           html.includes('\\equiv') ||
           html.includes('\\sum') ||
           html.includes('\\int');
}

let totalHtml = 0;
let filesWithMath = 0;
let filesAlreadyKatex = 0;
let filesUpdated = 0;
const updatedList = [];

function processDir(dir) {
  let entries;
  try {
    entries = fs.readdirSync(dir, { withFileTypes: true });
  } catch(e) { return; }

  for (const entry of entries) {
    if (EXCLUDE.has(entry.name) || entry.name.startsWith('.')) continue;
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      processDir(full);
    } else if (entry.isFile() && entry.name.endsWith('.html')) {
      totalHtml++;
      let html = fs.readFileSync(full, 'utf8');
      if (!hasMathExpression(html)) continue;
      filesWithMath++;

      const hasK = html.includes('katex.min.js') || 
                   html.includes('up-upper-primary-topic.min.js') ||
                   html.includes('MathJax');

      if (hasK) {
        filesAlreadyKatex++;
        continue;
      }

      // Inject KaTeX
      let modified = false;
      if (html.includes('</head>')) {
        html = html.replace('</head>', () => `${KATEX_HEAD_BLOCK}\n</head>`);
        modified = true;
      } else if (/<body[^>]*>/i.test(html)) {
        html = html.replace(/<body[^>]*>/i, (m) => `${KATEX_HEAD_BLOCK}\n${m}`);
        modified = true;
      } else {
        html = `${KATEX_HEAD_BLOCK}\n` + html;
        modified = true;
      }

      if (modified) {
        let written = false;
        for (let attempt = 0; attempt < 3; attempt++) {
          try {
            fs.writeFileSync(full, html, 'utf8');
            written = true;
            break;
          } catch (e) {
            // small sleep and retry
            const wait = Date.now() + 100;
            while (Date.now() < wait) {}
          }
        }
        if (written) {
          filesUpdated++;
          updatedList.push(path.relative(ROOT, full));
        } else {
          console.warn('Could not write to', full);
        }
      }
    }
  }
}

const topDirs = fs.readdirSync(ROOT, { withFileTypes: true })
  .filter(d => d.isDirectory() && !EXCLUDE.has(d.name) && !d.name.startsWith('.'))
  .map(d => d.name);

for (const d of topDirs) {
  processDir(path.join(ROOT, d));
}

console.log('--- SCAN & UPDATE SUMMARY ---');
console.log('Total HTML pages in website:', totalHtml);
console.log('Total pages with math:', filesWithMath);
console.log('Pages already having KaTeX/MathJax:', filesAlreadyKatex);
console.log('Newly updated pages with KaTeX:', filesUpdated);
if (updatedList.length > 0) {
  console.log('Updated pages:', updatedList);
}
