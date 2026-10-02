import fs from 'fs';

const html = fs.readFileSync('up-upper-primary-teacher/index.html', 'utf8');
const regex = /href=["']([^"']*\/english\/[^"']*)["']/gi;
let m;
const links = new Set();
while ((m = regex.exec(html)) !== null) {
  links.add(m[1]);
}
console.log('English links in root index.html count:', links.size);
Array.from(links).forEach((l, i) => console.log(`${i + 1}. ${l}`));
