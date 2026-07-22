const fs = require('fs');
const path = require('path');

const syllabusHtml = fs.readFileSync('c:/Users/sande/Documents/GitHub/sjmaths-website/ssc-cgl/syllabus/index.html', 'utf8');

const reasoningBlockMatch = syllabusHtml.match(/General Intelligence & Reasoning[\s\S]*?(?=<div class="subject-card">[\s\S]*?English|$)/i);
if (!reasoningBlockMatch) {
    console.error('Reasoning block not found');
    process.exit(1);
}

const block = reasoningBlockMatch[0];
const hrefRegex = /href=["'](?:\.\.\/reasoning\/|\/ssc-cgl\/reasoning\/)([^"']+)["']/gi;
let match;
const links = [];

while ((match = hrefRegex.exec(block)) !== null) {
    let rawPath = match[1].replace(/\/$/, '');
    if (rawPath && !links.includes(rawPath)) {
        links.push(rawPath);
    }
}

console.log('Total reasoning topics extracted:', links.length);
links.forEach((l, i) => console.log((i+1) + '. ' + l));
