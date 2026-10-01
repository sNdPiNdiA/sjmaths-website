import fs from 'node:fs';

const html = fs.readFileSync('up-tgt-pgt-gk/indian-history/index.html', 'utf8');
console.log('Includes indus-valley link:', html.includes('indus-valley/'));
const topicMatch = html.match(/<div class="topic"[\s\S]*?<\/div>\s*<\/div>/);
if (topicMatch) {
  console.log('Sample topic HTML:\n', topicMatch[0]);
}
