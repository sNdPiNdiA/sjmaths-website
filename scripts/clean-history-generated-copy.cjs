const fs = require('node:fs');
const path = require('node:path');
const { ROOT } = require('./seo-html.cjs');

const historyRoot = path.join(ROOT, 'history');
function collect(dir) {
  return fs.readdirSync(dir, { withFileTypes: true }).flatMap(entry => {
    const file = path.join(dir, entry.name);
    return entry.isDirectory() ? collect(file) : entry.name === 'index.html' ? [file] : [];
  });
}

const replacements = [
  [/<p class="lead">Core study module, theoretical overview, and exam revision checklist for <strong>[\s\S]*?<\/p>\s*/gi, ''],
  [/<span class="exam-chip history-generated-badge">[\s\S]*?<\/span>/gi, ''],
  [/<p>Practice across every concept with mixed question formats\.<\/p>/gi, ''],
  [/<p>Use this tab after completing the detailed notes and before attempting the mini test\.<\/p>/gi, ''],
  [/<p>Attempt the objective questions and submit when finished\.<\/p>/gi, ''],
  [/<p>Check off each item as you master the factual and analytical aspects of <strong>[\s\S]*?<\/p>\s*/gi, ''],
  [/<h2>\d+\. Syllabus Overview &(?:amp;)? Exam Focus<\/h2>/gi, '<h2>1. Topic outline</h2>'],
  [/<h2>\d+\. High-Yield Key Facts &amp; Exam Memory Points<\/h2>/gi, '<h2>Key facts</h2>'],
  [/<h2>\d+\. Common Exam Pitfalls &(?:amp;)? Confusions to Avoid<\/h2>/gi, '<h2>Common confusions</h2>'],
  [/<h2>\d+\. Self-Assessment &amp; Topic Checklist<\/h2>/gi, '<h2>Check yourself</h2>'],
  [/<strong>Key Fact:<\/strong>\s*/gi, ''],
  [/<h3>Detailed explanation<\/h3>/gi, '<h3>Details</h3>'],
  [/<h3>Key points<\/h3>/gi, '<h3>Remember</h3>'],
  [/<strong>Examples and evidence<\/strong>/gi, '<strong>Examples &amp; sources</strong>'],
  [/<strong>Important distinctions<\/strong>/gi, '<strong>Compare</strong>'],
  [/<strong>Common misconceptions<\/strong>/gi, '<strong>Common confusions</strong>'],
  [/<strong>Exam focus<\/strong>/gi, '<strong>Exam points</strong>'],
  [/<h3>Point-wise rapid recall<\/h3>/gi, '<h3>Quick recall</h3>'],
  [/<h3>Mnemonic<\/h3>/gi, '<h3>Memory aid</h3>'],
  [/<h3>Tips<\/h3>/gi, '<h3>Review tips</h3>'],
  [/<h3>Exam tricks<\/h3>/gi, '<h3>Quick checks</h3>'],
  [/<h3>Common traps<\/h3>/gi, '<h3>Watch for</h3>'],
  [/<h2>Topic mnemonics<\/h2>/gi, '<h2>Memory aids</h2>'],
  [/<h2>Revision tips<\/h2>/gi, '<h2>Review tips</h2>'],
  [/<h2>Exam tricks<\/h2>/gi, '<h2>Question cues</h2>'],
  [/<h2>Important comparisons<\/h2>/gi, '<h2>Compare</h2>'],
  [/<h2>Exam traps and cautions<\/h2>/gi, '<h2>Watch for</h2>'],
  [/<h2>Self-assessment checklist<\/h2>/gi, '<h2>Check yourself</h2>'],
  [/(<label class="check-item"><input type="checkbox"><span>)I can explain ([^<]+?) with its key dates, terms and exam distinctions\.(<\/span><\/label>)/gi, '$1Explain $2 from memory.$3']
];

let changed = 0;
for (const file of collect(historyRoot)) {
  const before = fs.readFileSync(file, 'utf8');
  let after = before;
  for (const [pattern, replacement] of replacements) after = after.replace(pattern, replacement);
  if (after !== before) {
    fs.writeFileSync(file, after, 'utf8');
    changed += 1;
  }
}
console.log(`Removed repeated filler and simplified labels in ${changed} History pages.`);
