const fs = require('fs');
let content = fs.readFileSync('class-11-applied-mathematics/index.html', 'utf8');

// Extract all chapters with their data-grp-idx values
// Use proper regex escaping
const chapterPattern = /data-grp-idx="(\d+-c\d+)"[\s\S]*?<span class="subsection-title">([^<]+)<\/span>/g;
let match;
const chapters = [];
while ((match = chapterPattern.exec(content)) !== null) {
    chapters.push({ grpIdx: match[1], title: match[2].trim() });
}

console.log('Current chapter structure:');
chapters.forEach(c => console.log(`  ${c.grpIdx}: ${c.title}`));

fs.writeFileSync('chapter_structure_check.json', JSON.stringify(chapters, null, 2));
console.log('\nChapter structure saved. Total chapters:', chapters.length);