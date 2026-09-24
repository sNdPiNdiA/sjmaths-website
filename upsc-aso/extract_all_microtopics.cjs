const fs = require('fs');

const html = fs.readFileSync('upsc-aso/index.html', 'utf8');
const dayRegex = /Day\s+(\d+)\s+•\s+STUDY[\s\S]*?<div class="syllabus-header">\s*<span>([^<]+)<\/span>[\s\S]*?<ul class="syllabus-list"[^>]*>([\s\S]*?)<\/ul>/gi;
let match;
const manifest = [];
let id = 1;

while ((match = dayRegex.exec(html)) !== null) {
  const day = parseInt(match[1]);
  const subjectName = match[2].trim();
  const listHtml = match[3];
  const linkRegex = /href="([^"]+)"[^>]*class="microtopic-link"[^>]*>([^<]+)<\/a>/gi;
  let lMatch;
  while ((lMatch = linkRegex.exec(listHtml)) !== null) {
    let href = lMatch[1];
    if (href.startsWith('/')) href = href.slice(1);
    const title = lMatch[2].replace(/&amp;/g, '&').trim();
    // parse subject_slug and slug from href: upsc-aso/<subject_slug>/<slug>/
    const parts = href.split('/').filter(Boolean);
    const subject_slug = parts[1] || '';
    const slug = parts[2] || '';
    const filePath = href.endsWith('/') ? href + 'index.html' : href;
    const exists = fs.existsSync(filePath);

    manifest.push({
      id: id++,
      day,
      subject: subjectName,
      subject_slug,
      slug,
      title,
      href: '/' + href,
      filePath,
      exists
    });
  }
}

console.log('Total extracted microtopics:', manifest.length);
const subjects = {};
manifest.forEach(m => {
  subjects[m.subject] = (subjects[m.subject] || 0) + 1;
});
console.log('Subject breakdown:', subjects);
console.log('Sample entry #1:', manifest[0]);
console.log('Sample entry #544:', manifest[manifest.length - 1]);
fs.writeFileSync('upsc-aso/all_544_microtopics.json', JSON.stringify(manifest, null, 2));
console.log('Wrote upsc-aso/all_544_microtopics.json successfully!');
