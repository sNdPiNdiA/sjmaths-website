const fs = require('fs');
const path = require('path');

const syllabusHtml = fs.readFileSync('c:/Users/sande/Documents/GitHub/sjmaths-website/ssc-cgl/syllabus/index.html', 'utf8');

const lines = syllabusHtml.split('\n').slice(1044, 1264).join('\n');
const linkRegex = /href=["']\.\.\/reasoning\/([^"']+)["']/gi;
let m;
const list = [];
while ((m = linkRegex.exec(lines)) !== null) {
    list.push(m[1].replace(/\/$/, ''));
}

console.log('✅ Found Syllabus Reasoning Topics (' + list.length + ' topics):');
list.forEach((t, i) => console.log(`${i+1}. ${t}`));

fs.writeFileSync('reasoning_topics.json', JSON.stringify(list, null, 2), 'utf8');
