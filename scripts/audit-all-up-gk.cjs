const fs = require('fs');
const path = require('path');
const cheerio = require('cheerio');

const baseDir = path.resolve('upsssc-up-gk');
const entries = fs.readdirSync(baseDir, { withFileTypes: true });
const subdirs = entries.filter(e => e.isDirectory()).map(e => e.name).sort();

console.log('=== UP GK TOPIC AUDIT ===\n');

for (const dir of subdirs) {
  const filePath = path.join(baseDir, dir, 'index.html');
  if (!fs.existsSync(filePath)) {
    console.log(`[MISSING] ${dir}/index.html`);
    continue;
  }
  const html = fs.readFileSync(filePath, 'utf8');
  const $ = cheerio.load(html);
  
  const theoryCards = $('#tab-theory .card-premium').length;
  const practiceCards = $('#tab-practice .practice-question-card, #tab-practice .question-card').length;
  const pyqCards = $('#tab-pyqs .pyq-card, #tab-pyqs .practice-question-card, #tab-pyqs .question-card').length;
  const testCards = $('#tab-test .test-question, #tab-test .test-q-box').length;
  
  // Measure theory text size
  const theoryText = $('#tab-theory').text().replace(/\s+/g, ' ').trim();
  const theoryWords = theoryText.split(' ').length;
  
  console.log(`${dir.padEnd(35)} | Theory Cards: ${String(theoryCards).padStart(2)} | Theory Words: ${String(theoryWords).padStart(5)} | Practice: ${String(practiceCards).padStart(2)} | PYQs: ${String(pyqCards).padStart(2)} | Test: ${String(testCards).padStart(2)}`);
}
