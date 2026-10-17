const fs = require('fs');
const path = require('path');
const cheerio = require('cheerio');

const baseDir = path.resolve('upsssc-up-gk');
const entries = fs.readdirSync(baseDir, { withFileTypes: true });
const subdirs = entries.filter(e => e.isDirectory()).map(e => e.name);

console.log('Total micro-topics in upsssc-up-gk:', subdirs.length);
console.log(subdirs.join(', '));

// Inspect the first one: agriculture
const sampleFile = path.join(baseDir, 'agriculture', 'index.html');
const $ = cheerio.load(fs.readFileSync(sampleFile, 'utf8'));

console.log('\n--- Tabs in agriculture/index.html ---');
$('.sub-nav-item').each((i, el) => {
  console.log($(el).attr('data-tab'), ':', $(el).text().trim());
});

console.log('\n--- Tab content containers ---');
$('.tab-content').each((i, el) => {
  console.log('ID:', $(el).attr('id'), '| style:', $(el).attr('style'));
});

console.log('\n--- Cards in Theory Tab ---');
$('#tab-theory .card-premium').each((i, el) => {
  const title = $(el).find('.card-title').text().trim();
  const headings = [];
  $(el).find('h3, h4').each((_, h) => headings.push($(h).text().trim()));
  console.log('Card:', title);
  if (headings.length) console.log('   Headings:', headings.slice(0, 5).join(' | '));
});
