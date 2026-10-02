import fs from 'node:fs';
import path from 'node:path';

function walk(dir) {
  let results = [];
  const list = fs.readdirSync(dir);
  for (const file of list) {
    const full = path.join(dir, file);
    const stat = fs.statSync(full);
    if (stat.isDirectory()) {
      results = results.concat(walk(full));
    } else if (file === 'index.html') {
      results.push(full);
    }
  }
  return results;
}

const allFiles = walk(path.join(process.cwd(), 'up-upper-primary-teacher'));
const suspectPatterns = {
  'as an ai': /as an ai/i,
  'here is a': /here is a/i,
  'certainly': /certainly/i,
  'in conclusion': /in conclusion/i
};

for (const [name, pat] of Object.entries(suspectPatterns)) {
  for (const f of allFiles) {
    const txt = fs.readFileSync(f, 'utf8');
    const m = txt.match(pat);
    if (m) {
      const idx = txt.indexOf(m[0]);
      const snippet = txt.slice(Math.max(0, idx - 40), Math.min(txt.length, idx + 80)).replace(/\n/g, ' ');
      console.log(`[${name}] ${path.relative(process.cwd(), f)}:\n  "...${snippet}..."\n`);
    }
  }
}
