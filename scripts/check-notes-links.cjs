const fs = require('fs');

const sample = fs.readFileSync('class-10-maths/chapter-wise-notes/chapter-1-real-numbers/index.html', 'utf8');
const links = [...sample.matchAll(/<link\b[^>]*rel=["']stylesheet["'][^>]*>/gi)].map(m => m[0]);
console.log('Stylesheet links count:', links.length);
links.forEach(l => console.log('  ', l));
