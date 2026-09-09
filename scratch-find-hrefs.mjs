import fs from 'fs';

const html = fs.readFileSync('index.html', 'utf8');
const regex = /href=["']([^"']+)["']/g;
let m;
const hrefs = [];
while ((m = regex.exec(html)) !== null) {
    hrefs.push(m[1]);
}

console.log('--- Unique hrefs directly in index.html ---');
const unique = [...new Set(hrefs)];
unique.forEach(h => console.log(h));
