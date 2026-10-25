import fs from 'node:fs';
import path from 'node:path';

let total = 0;
let withComponentCss = 0;
let withoutComponentCss = 0;

function scan(dir) {
  for (const item of fs.readdirSync(dir, { withFileTypes: true })) {
    if (['node_modules', '.git', '.pages-dist'].includes(item.name)) continue;
    const p = path.join(dir, item.name);
    if (item.isDirectory()) scan(p);
    else if (item.name.endsWith('.html')) {
      total++;
      const c = fs.readFileSync(p, 'utf8');
      if (c.includes('component.') || c.includes('home-v2.') || c.includes('slide-notes.')) {
        withComponentCss++;
      } else {
        withoutComponentCss++;
      }
    }
  }
}
scan('.');
console.log({ total, withComponentCss, withoutComponentCss });

