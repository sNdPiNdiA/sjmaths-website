const fs = require('fs');

const topicsV2 = JSON.parse(fs.readFileSync('upsc-aso/topics_v2.json', 'utf8'));
console.log('topics_v2 count:', topicsV2.length);

const html = fs.readFileSync('upsc-aso/index.html', 'utf8');
const dayRegex = /Day\s+(\d+)\s+•\s+STUDY[\s\S]*?<ul class="syllabus-list"[^>]*>([\s\S]*?)<\/ul>/gi;
let match;
const indexList = [];
while ((match = dayRegex.exec(html)) !== null) {
  const day = parseInt(match[1]);
  const listHtml = match[2];
  const linkRegex = /href="([^"]+)"[^>]*class="microtopic-link"[^>]*>([^<]+)<\/a>/gi;
  let lMatch;
  while ((lMatch = linkRegex.exec(listHtml)) !== null) {
    let href = lMatch[1];
    if (href.startsWith('/')) href = href.slice(1);
    indexList.push({ day, title: lMatch[2].replace(/&amp;/g, '&'), href });
  }
}
console.log('index.html microtopics count:', indexList.length);

// Compare hrefs and paths
let matched = 0;
let unmatched = 0;
topicsV2.forEach(t => {
  const expectedHref = `upsc-aso/${t.subject_slug}/${t.slug}/`;
  const found = indexList.find(i => i.href === expectedHref);
  if (found) matched++;
  else unmatched++;
});
console.log(`Matched between topics_v2 and index.html: ${matched}, unmatched: ${unmatched}`);
