const fs = require('fs');
const path = require('path');

function safeWrite(filePath, content) {
  const dir = path.dirname(filePath);
  if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
  fs.writeFileSync(filePath, content, 'utf8');
}

// Check Topic 1 template header CSS and body
const topic1Path = path.join(process.cwd(), 'up-upper-primary-teacher', 'mathematics', 'natural-and-whole-numbers', 'index.html');
const t1Content = fs.readFileSync(topic1Path, 'utf8');

// Notice in Topic 1:
// Hero container is <div class="topic-hero-panel">
// In main.min.css:
// .topic-hero-panel { background: ...; }
// And KaTeX is loaded cleanly with:
// <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css"/>
// <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
// <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]});"></script>

console.log('Topic 1 length:', t1Content.length);
console.log('Ready to build Topic 2, 3, 4 with exact precision.');
