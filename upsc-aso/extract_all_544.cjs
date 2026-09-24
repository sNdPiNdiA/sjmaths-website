const fs = require('fs');

const html = fs.readFileSync('upsc-aso/index.html', 'utf8');
const dayRegex = /Day\s+(\d+)\s+•\s+STUDY[\s\S]*?<ul class="syllabus-list"[^>]*>([\s\S]*?)<\/ul>/gi;
let match;
const microtopics = [];
let id = 1;

while ((match = dayRegex.exec(html)) !== null) {
  const day = parseInt(match[1]);
  const listHtml = match[2];
  const linkRegex = /href="([^"]+)"[^>]*class="microtopic-link"[^>]*>([^<]+)<\/a>/gi;
  let lMatch;
  while ((lMatch = linkRegex.exec(listHtml)) !== null) {
    let href = lMatch[1].trim();
    if (href.startsWith('/')) href = href.slice(1);
    const title = lMatch[2].replace(/&amp;/g, '&').trim();

    const parts = href.split('/').filter(Boolean);
    const subject_slug = parts[1] || '';
    const slug = parts[2] || '';
    const filePath = href.endsWith('/') ? href + 'index.html' : href;
    const exists = fs.existsSync(filePath);

    microtopics.push({
      id: id++,
      day,
      subject_slug,
      slug,
      title,
      href: '/' + href,
      filePath,
      exists
    });
  }
}

console.log('Total extracted microtopics:', microtopics.length);
if (microtopics.length > 0) {
  console.log('Sample #1:', microtopics[0]);
  console.log('Sample #544 (last):', microtopics[microtopics.length - 1]);
}
fs.writeFileSync('upsc-aso/all_544_microtopics.json', JSON.stringify(microtopics, null, 2));
console.log('Saved to upsc-aso/all_544_microtopics.json');
