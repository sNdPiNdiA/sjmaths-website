import fs from 'node:fs';
import path from 'node:path';

const matches = [];
function scan(dir) {
  for (const item of fs.readdirSync(dir, { withFileTypes: true })) {
    if (['node_modules', '.git', '.pages-dist'].includes(item.name)) continue;
    const p = path.join(dir, item.name);
    if (item.isDirectory()) scan(p);
    else if (item.name.endsWith('.html')) {
      const c = fs.readFileSync(p, 'utf8');
      if (c.includes('site-footer') && !c.includes('id="site-footer"')) {
        if (matches.length < 5) matches.push(p);
      }
    }
  }
}
scan('.');
console.log('Sample files with site-footer not as ID:', matches);
if (matches.length > 0) {
  const sample = fs.readFileSync(matches[0], 'utf8');
  const lines = sample.split('\n');
  lines.forEach((l, i) => {
    if (l.includes('site-footer')) console.log(`Line ${i+1}: ${l}`);
  });
}

