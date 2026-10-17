const fs = require('fs');
const cheerio = require('cheerio');
const $ = cheerio.load(fs.readFileSync('upsssc-up-gk/agriculture/index.html', 'utf8'));

$('#tab-theory .card-premium').each((i, el) => {
  console.log(`\n=== Card ${i+1}: ${$(el).find('.card-title .lang-en').text().trim()} ===`);
  $(el).find('h3, h4').each((_, h) => {
    console.log(`  [Heading] ${$(h).text().trim()}`);
  });
  const text = $(el).text().replace(/\s+/g, ' ').trim();
  console.log(`  Preview: ${text.slice(0, 180)}...`);
});
