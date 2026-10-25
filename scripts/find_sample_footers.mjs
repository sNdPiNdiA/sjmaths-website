import fs from 'node:fs';
import path from 'node:path';

function findSample(pattern) {
  function scan(dir) {
    for (const item of fs.readdirSync(dir, { withFileTypes: true })) {
      if (['node_modules', '.git', '.pages-dist'].includes(item.name)) continue;
      const p = path.join(dir, item.name);
      if (item.isDirectory()) {
        const found = scan(p);
        if (found) return found;
      } else if (item.name.endsWith('.html')) {
        const c = fs.readFileSync(p, 'utf8');
        if (pattern.test(c)) return { p, m: c.match(pattern)[0] };
      }
    }
  }
  return scan('.');
}

console.log('ib-footer:', JSON.stringify(findSample(/<footer class=["']ib-footer["'][\s\S]*?<\/footer>/i), null, 2));
console.log('micro-footer:', JSON.stringify(findSample(/<footer class=["']micro-footer["'][\s\S]*?<\/footer>/i), null, 2));

