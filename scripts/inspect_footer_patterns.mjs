import fs from 'node:fs';
import path from 'node:path';

const footerPatterns = new Map();

function scan(dir) {
  for (const item of fs.readdirSync(dir, { withFileTypes: true })) {
    if (['node_modules', '.git', '.pages-dist'].includes(item.name)) continue;
    const p = path.join(dir, item.name);
    if (item.isDirectory()) scan(p);
    else if (item.name.endsWith('.html')) {
      const c = fs.readFileSync(p, 'utf8');
      if (c.includes('site-footer') || /<div id=["']footer-container["']>\s*<\/div>/i.test(c)) {
        continue;
      }
      const m = c.match(/<footer([\s\S]*?)<\/footer>/i);
      if (m) {
        // extract the class or id of the footer
        const tag = m[0].slice(0, 50).split('>')[0] + '>';
        footerPatterns.set(tag, (footerPatterns.get(tag) || 0) + 1);
      }
    }
  }
}

scan('.');
console.log('Footer tag patterns:');
for (const [tag, count] of footerPatterns.entries()) {
  console.log(`${tag} -> ${count}`);
}

