const fs = require('fs');
const path = require('path');

const topics = [
  'integers-properties-and-operations',
  'bodmas-rule-simplification',
  'lcm-and-hcf-methods-applications'
];

topics.forEach(t => {
  const p = path.join(process.cwd(), 'up-upper-primary-teacher', 'mathematics', t, 'index.html');
  let c = fs.readFileSync(p, 'utf8');

  console.log(`\n=== Processing ${t} ===`);
  const initialSpades = (c.match(/\x0c/g) || []).length;
  console.log(`Initial form-feeds (0x0c / spade): ${initialSpades}`);

  // 1. Fix header squishing: change <header class="topic-hero-card"> to <div class="topic-hero-card">
  c = c.replace('<header class="topic-hero-card">', '<div class="topic-hero-card">');
  // Replace the closing tag corresponding to hero card (first </header>)
  c = c.replace('</header>', '</div>');

  // 2. Fix Form Feed (0x0c) followed by rac -> \frac
  // Note: in string literals, \x0c is character 12
  c = c.replaceAll('\x0crac', '\\frac');
  c = c.replaceAll('\x0c', '\\f');

  // 3. Fix Tab followed by ext -> \text, and \times
  c = c.replaceAll('\text', '\\text');
  c = c.replaceAll('\times', '\\times');
  c = c.replaceAll('\to', '\\to');

  // 4. Fix Carriage return / ightarrow -> \rightarrow
  c = c.replaceAll('ightarrow', '\\rightarrow');
  c = c.replaceAll('\rightarrow', '\\rightarrow');
  c = c.replaceAll('\right', '\\right');

  // 5. Fix dots -> \dots when it appears as a separate word in math or text
  c = c.replaceAll(' dots ', ' \\dots ');
  c = c.replaceAll(' dots,', ' \\dots,');
  c = c.replaceAll('{dots}', '{\\dots}');
  c = c.replaceAll(', dots', ', \\dots');
  c = c.replaceAll('dots}', '\\dots}');
  c = c.replaceAll('dots\\', '\\dots\\');

  // 6. Fix \mathbb
  c = c.replaceAll('mathbbN', '\\mathbb{N}');
  c = c.replaceAll('mathbbW', '\\mathbb{W}');
  c = c.replaceAll('mathbbZ', '\\mathbb{Z}');
  c = c.replaceAll('mathbbQ', '\\mathbb{Q}');
  c = c.replaceAll('mathbbR', '\\mathbb{R}');

  // 7. Fix division and bold 0
  c = c.replaceAll('7div0', '7 \\div 0');
  c = c.replaceAll('0div7', '0 \\div 7');
  c = c.replaceAll('mathbf0', '\\mathbf{0}');

  // 8. Fix any literal spade character '♠' if present
  c = c.replaceAll('♠rac', '\\frac');
  c = c.replaceAll('♠', '\\f');

  fs.writeFileSync(p, c, 'utf8');

  // Verify
  const verified = fs.readFileSync(p, 'utf8');
  const remSpade = (verified.match(/♠|\x0c/g) || []).length;
  const hasHeaderTag = verified.includes('<header class="topic-hero-card">');
  const remIght = (verified.match(/ightarrow/g) || []).length;
  console.log(`Updated ${t}:`);
  console.log(`  Remaining spades/0x0c: ${remSpade}`);
  console.log(`  Hero is <header>: ${hasHeaderTag} (must be false)`);
  console.log(`  Remaining ightarrow: ${remIght}`);
});

// Sync to bodmas alias
const bodmasCanon = path.join(process.cwd(), 'up-upper-primary-teacher', 'mathematics', 'bodmas-rule-simplification', 'index.html');
const bodmasAlias = path.join(process.cwd(), 'up-upper-primary-teacher', 'mathematics', 'bodmas-rule-and-brackets-simplification', 'index.html');
if (fs.existsSync(bodmasAlias)) {
  fs.copyFileSync(bodmasCanon, bodmasAlias);
  console.log('\nSynced bodmas alias file successfully.');
}
