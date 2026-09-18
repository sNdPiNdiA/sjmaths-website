const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const dir = path.join(ROOT, 'commerce');

function scan(d) {
  let res = [];
  for (const ent of fs.readdirSync(d, { withFileTypes: true })) {
    const full = path.join(d, ent.name);
    if (ent.isDirectory()) {
      res = res.concat(scan(full));
    } else if (ent.name === 'index.html') {
      const rel = path.relative(ROOT, path.dirname(full)).replace(/\\/g, '/');
      const stat = fs.statSync(full);
      res.push({ path: rel, sizeKb: (stat.size / 1024).toFixed(1) });
    }
  }
  return res;
}

const files = scan(dir);
console.log(`Total commerce pages: ${files.length}`);
// Print hierarchy grouped by top 2 levels
const groups = {};
for (const f of files) {
  const parts = f.path.split('/');
  const prefix = parts.slice(0, 2).join('/');
  if (!groups[prefix]) groups[prefix] = [];
  groups[prefix].push(f);
}

for (const [prefix, list] of Object.entries(groups)) {
  console.log(`\n=== ${prefix} (${list.length} pages) ===`);
  list.forEach(p => console.log(`  ${p.path} [${p.sizeKb} KB]`));
}
