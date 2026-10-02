import fs from 'node:fs';
import path from 'node:path';

const ROOT = process.cwd();
const HINDI_DIR = path.join(ROOT, 'up-upper-primary-teacher', 'hindi');
const HINDI_HUB = path.join(HINDI_DIR, 'index.html');

const html = fs.readFileSync(HINDI_HUB, 'utf8');

// Find all hrefs inside hindi/index.html
const linkRegex = /href="([^"]+)"/g;
const links = new Set();
let m;
while ((m = linkRegex.exec(html)) !== null) {
  if (m[1].includes('/up-upper-primary-teacher/hindi/')) {
    links.add(m[1]);
  }
}

console.log('--- ALL LINKS in hindi/index.html ---');
for (const l of [...links].sort()) {
  console.log(l);
}

// Find modules/accordions
console.log('\n--- MODULES in hindi/index.html ---');
const moduleRegex = /<h3 class="module-title">[\s\S]*?<span class="lang-hi">([^<]+)<\/span>/g;
while ((m = moduleRegex.exec(html)) !== null) {
  console.log(m[1]);
}
