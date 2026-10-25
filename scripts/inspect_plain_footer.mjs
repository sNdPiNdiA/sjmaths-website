import fs from 'node:fs';
import path from 'node:path';

const samples = [];
function scan(dir) {
  for (const item of fs.readdirSync(dir, { withFileTypes: true })) {
    if (['node_modules', '.git', '.pages-dist'].includes(item.name)) continue;
    const p = path.join(dir, item.name);
    if (item.isDirectory()) scan(p);
    else if (item.name.endsWith('.html')) {
      const c = fs.readFileSync(p, 'utf8');
      if (c.includes('site-footer') || /<div id=["']footer-container["']>\s*<\/div>/i.test(c)) continue;
      const m = c.match(/<footer>([\s\S]*?)<\/footer>/i);
      if (m && samples.length < 5) {
        samples.push({ path: p, content: m[0] });
      }
    }
  }
}
scan('.');
console.log(JSON.stringify(samples, null, 2));

