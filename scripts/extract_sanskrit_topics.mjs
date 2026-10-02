import fs from 'fs';

const html = fs.readFileSync('up-upper-primary-teacher/sanskrit/index.html', 'utf8');

// Parse accordions
const accordionRegex = /<details class="module-accordion"[^>]*data-sec-idx="([^"]+)"[\s\S]*?<h3 class="module-title">\s*<span class="lang-hi">([^<]+)<\/span>[\s\S]*?<ul class="module-list">([\s\S]*?)<\/ul>/g;

let accMatch;
const allTopics = [];

while ((accMatch = accordionRegex.exec(html)) !== null) {
  const secIdx = accMatch[1];
  const secTitle = accMatch[2].trim();
  const listHtml = accMatch[3];

  const rowRegex = /<li class="topic-row">[\s\S]*?<input[^>]*id="([^"]+)"[\s\S]*?<a\s+href="\/up-upper-primary-teacher\/sanskrit\/([^"\/]+)\/?"[\s\S]*?<span class="topic-num">([^<]+)<\/span>\s*<span class="lang-hi">([^<]+)<\/span>[\s\S]*?<span class="topic-tag">([^<]+)<\/span>/g;

  let rowMatch;
  while ((rowMatch = rowRegex.exec(listHtml)) !== null) {
    allTopics.push({
      secIdx: Number(secIdx),
      secTitle,
      chkId: rowMatch[1].trim(),
      slug: rowMatch[2].trim(),
      numStr: rowMatch[3].trim(),
      title: rowMatch[4].trim(),
      tag: rowMatch[5].trim()
    });
  }
}

console.log(`Extracted ${allTopics.length} Sanskrit topics:`);
console.table(allTopics);

fs.writeFileSync('scripts/sanskrit_topics_list.json', JSON.stringify(allTopics, null, 2), 'utf8');
