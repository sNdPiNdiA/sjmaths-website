const fs = require('fs');
const path = require('path');

const content = fs.readFileSync('class-11-applied-mathematics/index.html', 'utf8');

// Match all details blocks containing subsections
const regex = /<details class="syllabus-subsection" data-prefix="([^"]+)" data-grp-idx="([^"]+)"[\s\S]*?<span class="subsection-title">([\s\S]*?)<\/span>[\s\S]*?<ul class="syllabus-list">([\s\S]*?)<\/ul>/g;

let match;
const structure = {};

while ((match = regex.exec(content)) !== null) {
    const prefix = match[1];
    const grp = match[2];
    const title = match[3].trim().replace(/\s+/g, ' ');
    const listHtml = match[4];
    
    // Extract list items
    const itemRegex = /<li class="syllabus-item">[\s\S]*?id="([^"]+)"[\s\S]*?href="([^"]+)"[\s\S]*?class="topic-link syllabus-text">([\s\S]*?)<\/a>/g;
    let itemMatch;
    const items = [];
    while ((itemMatch = itemRegex.exec(listHtml)) !== null) {
        items.push({
            id: itemMatch[1],
            href: itemMatch[2],
            text: itemMatch[3].trim().replace(/\s+/g, ' ')
        });
    }
    
    const unit = grp.split('-')[0];
    if (!structure[unit]) structure[unit] = [];
    structure[unit].push({
        grp,
        title,
        items
    });
}

console.log(JSON.stringify(structure, null, 2));
fs.writeFileSync('scratch_extracted_structure.json', JSON.stringify(structure, null, 2), 'utf8');
