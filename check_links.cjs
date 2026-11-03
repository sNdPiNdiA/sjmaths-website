const fs = require('fs');
const path = require('path');

const filePath = 'class-12-maths/previous-years-questions-chapter-wise/index.html';
const content = fs.readFileSync(filePath, 'utf8');

const regex = /href=["']([^"']+)["']/g;
let m;
const links = [];
while ((m = regex.exec(content)) !== null) {
  links.push(m[1]);
}

console.log('Total links found:', links.length);

const baseDir = 'class-12-maths/previous-years-questions-chapter-wise';

const missing = [];
const existing = [];

links.forEach(link => {
  if (link.startsWith('http') || link.startsWith('#') || link.startsWith('mailto:')) return;
  
  // Resolve relative to baseDir if not starting with /
  let resolvedPath = link.startsWith('/') ? link.slice(1) : path.join(baseDir, link);
  
  // Check direct
  let exists = fs.existsSync(resolvedPath);
  let existsWithHtml = fs.existsSync(resolvedPath + '.html');
  let existsWithIndex = fs.existsSync(path.join(resolvedPath, 'index.html'));
  
  if (!exists && !existsWithHtml && !existsWithIndex) {
    missing.push({ link, resolvedPath });
  } else {
    existing.push({ link, resolvedPath, exists, existsWithHtml, existsWithIndex });
  }
});

console.log('Missing links (' + missing.length + '):');
console.log(missing);
console.log('Existing links (' + existing.length + '):');
console.log(existing.slice(0, 20));
