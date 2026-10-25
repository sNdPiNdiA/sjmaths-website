import fs from 'node:fs';
import path from 'node:path';

let total = 0;
let withSiteFooter = 0;
let withEmptyContainer = 0;
let withNeither = 0;
const neitherList = [];

function scan(dir) {
  for (const item of fs.readdirSync(dir, { withFileTypes: true })) {
    if (['node_modules', '.git', '.pages-dist'].includes(item.name)) continue;
    const p = path.join(dir, item.name);
    if (item.isDirectory()) scan(p);
    else if (item.name.endsWith('.html')) {
      total++;
      const c = fs.readFileSync(p, 'utf8');
      if (c.includes('site-footer')) {
        withSiteFooter++;
      } else if (/<div id=["']footer-container["']>\s*<\/div>/i.test(c)) {
        withEmptyContainer++;
      } else {
        withNeither++;
        if (neitherList.length < 50) neitherList.push(p);
      }
    }
  }
}
scan('.');
console.log({ total, withSiteFooter, withEmptyContainer, withNeither });
console.log('Sample neither:');
for (const f of neitherList) {
  console.log(' -', f);
}
