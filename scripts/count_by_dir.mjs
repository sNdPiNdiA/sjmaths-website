import fs from 'node:fs';
import path from 'node:path';

const dirCounts = {};

function scan(dir, topDir) {
  for (const item of fs.readdirSync(dir, { withFileTypes: true })) {
    if (['node_modules', '.git', '.pages-dist'].includes(item.name)) continue;
    const p = path.join(dir, item.name);
    const currentTop = topDir || item.name;
    if (item.isDirectory()) {
      scan(p, currentTop);
    } else if (item.name.endsWith('.html')) {
      dirCounts[currentTop] = (dirCounts[currentTop] || 0) + 1;
    }
  }
}

scan('.', '');
console.log('Top directory HTML counts:');
const sorted = Object.entries(dirCounts).sort((a, b) => b[1] - a[1]);
for (const [d, c] of sorted) {
  console.log(`  ${d.padEnd(30)}: ${c}`);
}

