const fs = require('fs');
const path = require('path');
const root = process.cwd();

function walk(dir, out = []) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    if (['node_modules', '.git', 'scripts', '.vscode'].includes(e.name)) continue;
    const fp = path.join(dir, e.name);
    if (e.isDirectory()) walk(fp, out);
    else if (e.name.toLowerCase().endsWith('.html')) out.push(fp);
  }
  return out;
}

const files = walk(root);
const MATH_RE = /\$\$|\\\(|\\\[|\\\(/;
const orderBad = [];
const noConfig = [];
const cdnVariants = {};
const unsafeTypeset = [];
const mathNoMj = [];
let mjCount = 0;

for (const fp of files) {
  const rel = path.relative(root, fp);
  let c;
  try { c = fs.readFileSync(fp, 'utf8'); } catch { continue; }
  const hasMj = /<script[^>]*mathjax/i.test(c) || /window\.MathJax/.test(c);
  const hasMath = /\$\$/.test(c) || /\\\(/.test(c) || /\\\[\s*\n/.test(c) || /<mjx|katex/i.test(c);
  if (hasMj) {
    mjCount++;
    const scriptIdx = c.search(/<script[^>]+mathjax/i);
    const cfgIdx = c.indexOf('window.MathJax');
    if (cfgIdx === -1) noConfig.push(rel);
    else if (cfgIdx > scriptIdx) orderBad.push(rel);
    const m = c.match(/<script[^>]*src=["']([^"']*mathjax[^"']*)["']/i);
    if (m) {
      const key = m[1].replace(/\?.*$/, '');
      cdnVariants[key] = (cdnVariants[key] || 0) + 1;
    }
    if (/MathJax\.typesetPromise\(\)/.test(c)) unsafeTypeset.push(rel);
  } else if (hasMath) {
    mathNoMj.push(rel);
  }
}

console.log('HTML files scanned:', files.length);
console.log('pages with MathJax:', mjCount);
console.log('=== config AFTER script tag:', orderBad.length);
orderBad.slice(0, 15).forEach(p => console.log('   ', p));
console.log('=== no window.MathJax config:', noConfig.length);
noConfig.slice(0, 15).forEach(p => console.log('   ', p));
console.log('=== CDN variants:');
Object.entries(cdnVariants).forEach(([k, v]) => console.log('   ', v, k));
console.log('=== pages calling MathJax.typesetPromise():', unsafeTypeset.length);
unsafeTypeset.slice(0, 15).forEach(p => console.log('   ', p));
console.log('=== math content but NO MathJax:', mathNoMj.length);
mathNoMj.slice(0, 25).forEach(p => console.log('   ', p));

