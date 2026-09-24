const fs = require('fs');

const html = fs.readFileSync('upsc-aso/index.html', 'utf8');
const dayRegex = /Day\s+(\d+)\s+•\s+STUDY[\s\S]*?<ul class="syllabus-list"[^>]*>([\s\S]*?)<\/ul>/gi;
let match;
let count = 0;
let totalMicrotopics = 0;
let existingFiles = 0;
let missingFiles = 0;
const missingList = [];

while ((match = dayRegex.exec(html)) !== null) {
  const day = match[1];
  const listHtml = match[2];
  const linkRegex = /href="([^"]+)"[^>]*class="microtopic-link"[^>]*>([^<]+)<\/a>/gi;
  let lMatch;
  while ((lMatch = linkRegex.exec(listHtml)) !== null) {
    totalMicrotopics++;
    let href = lMatch[1];
    if (href.startsWith('/')) href = href.slice(1);
    let filePath = href;
    if (filePath.endsWith('/')) filePath += 'index.html';
    if (fs.existsSync(filePath)) {
      existingFiles++;
    } else {
      missingFiles++;
      if (missingList.length < 10) missingList.push({ day, title: lMatch[2], filePath });
    }
  }
}
console.log('Total microtopic links in index.html:', totalMicrotopics);
console.log('Existing files on disk:', existingFiles);
console.log('Missing files on disk:', missingFiles);
if (missingList.length > 0) {
  console.log('Sample missing:', missingList);
}
