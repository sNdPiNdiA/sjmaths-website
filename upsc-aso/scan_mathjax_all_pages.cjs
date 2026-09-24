const fs = require('fs');
const path = require('path');

function getHtmlFiles(dir) {
  let res = [];
  for (const item of fs.readdirSync(dir)) {
    const full = path.join(dir, item);
    const stat = fs.statSync(full);
    if (stat.isDirectory()) {
      if (item !== 'node_modules' && item !== '.git') res = res.concat(getHtmlFiles(full));
    } else if (item.endsWith('.html') && full !== path.resolve('upsc-aso/index.html')) {
      res.push(full);
    }
  }
  return res;
}

const allPages = getHtmlFiles(path.resolve('upsc-aso'));
console.log(`Auditing ${allPages.length} pages for MathJax & UI/UX rendering...\n`);

let missingMathJaxConfig = 0;
let missingMathJaxScript = 0;
let hasPolyfillIo = 0;
let missingTypesetInSwitchTab = 0;
let missingDarkBodyOverride = 0;

const pagesNeedingMathJaxConfig = [];
const pagesWithPolyfillIo = [];
const pagesNeedingTypeset = [];

allPages.forEach(p => {
  const html = fs.readFileSync(p, 'utf8');
  const rel = path.relative(path.resolve('.'), p).replace(/\\/g, '/');

  const hasMathJax = html.includes('mathjax');
  const hasInlineConfig = html.includes("['$', '$']") || html.includes('["$", "$"]');
  const hasPolyfill = html.includes('polyfill.io');
  const hasSwitchTab = html.includes('function switchTab');
  const hasTypeset = html.includes('MathJax.typesetPromise') || html.includes('MathJax.typeset');
  const hasDarkOverride = html.includes('background-color: #060911 !important') || html.includes('background-color:#060911!important');

  if (!hasMathJax) missingMathJaxScript++;
  if (hasMathJax && !hasInlineConfig) {
    missingMathJaxConfig++;
    pagesNeedingMathJaxConfig.push(rel);
  }
  if (hasPolyfill) {
    hasPolyfillIo++;
    pagesWithPolyfillIo.push(rel);
  }
  if (hasSwitchTab && !hasTypeset) {
    missingTypesetInSwitchTab++;
    pagesNeedingTypeset.push(rel);
  }
  if (!hasDarkOverride) {
    missingDarkBodyOverride++;
  }
});

console.log('========================================================================');
console.log('                       MATHJAX & UI/UX AUDIT SUMMARY');
console.log('========================================================================');
console.log(`Total HTML pages inspected: ${allPages.length}`);
console.log(`- Pages with MathJax script: ${allPages.length - missingMathJaxScript} / ${allPages.length}`);
console.log(`- Pages MISSING inline dollar config ($...$ ignored by MathJax): ${missingMathJaxConfig}`);
console.log(`- Pages containing deprecated/compromised polyfill.io: ${hasPolyfillIo}`);
console.log(`- Pages where switchTab() MISSES MathJax.typesetPromise(): ${missingTypesetInSwitchTab}`);
console.log(`- Pages missing !important dark theme body override: ${missingDarkBodyOverride}`);
console.log('========================================================================\n');

if (missingMathJaxConfig > 0) {
  console.log(`Sample pages where MathJax ignores $...$ formulas (${missingMathJaxConfig} total):`);
  pagesNeedingMathJaxConfig.slice(0, 10).forEach(p => console.log('  ' + p));
  console.log('');
}

if (hasPolyfillIo > 0) {
  console.log(`Sample pages with compromised polyfill.io (${hasPolyfillIo} total):`);
  pagesWithPolyfillIo.slice(0, 5).forEach(p => console.log('  ' + p));
  console.log('');
}
