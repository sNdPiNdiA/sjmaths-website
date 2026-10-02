import fs from 'fs';

const html = fs.readFileSync('up-upper-primary-teacher/sanskrit/index.html', 'utf8');

// Let's parse out the sections and topics from the syllabus hub HTML
// Look for topic cards, checkboxes, links, badges, titles
const cardRegex = /<div class="topic-card"[\s\S]*?<\/div>\s*<\/div>\s*<\/div>/g;

// Also look for sections
const sectionRegex = /<div class="syllabus-section-card"[\s\S]*?<\/section>/g;

console.log('Hub file length:', html.length);

// Extract all links pointing to /up-upper-primary-teacher/sanskrit/
const topicLinkRegex = /<a\s+href="\/up-upper-primary-teacher\/sanskrit\/([^"\/]+)\/?"\s+class="topic-link-btn">\s*<span>([^<]+)<\/span>/g;
let match;
const topicList = [];
while ((match = topicLinkRegex.exec(html)) !== null) {
  topicList.push({
    slug: match[1],
    title: match[2].trim()
  });
}

console.log(`Found ${topicList.length} topic link buttons:`);
topicList.forEach((t, i) => console.log(`${i + 1}. [${t.slug}] -> ${t.title}`));

// Let's also check all checkboxes to get their IDs and numbers
const chkRegex = /<input\s+type="checkbox"\s+id="([^"]+)"[\s\S]*?<div class="topic-title">([^<]+)<\/div>/g;
let chkMatch;
const chkList = [];
while ((chkMatch = chkRegex.exec(html)) !== null) {
  chkList.push({
    id: chkMatch[1],
    title: chkMatch[2].trim()
  });
}
console.log(`\nFound ${chkList.length} topic checkboxes:`);
chkList.forEach((c, i) => console.log(`${i + 1}. [${c.id}] -> ${c.title}`));
