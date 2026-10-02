import fs from 'node:fs';
import path from 'node:path';

const base = path.join(process.cwd(), 'up-upper-primary-teacher', 'english');
const dirs = fs.readdirSync(base).filter(d => fs.statSync(path.join(base, d)).isDirectory());
for (const d of dirs) {
  const f = path.join(base, d, 'index.html');
  if (!fs.existsSync(f)) continue;
  const content = fs.readFileSync(f, 'utf8');
  const m = content.match(/<p class="lead-desc">\s*<span>([\s\S]*?)<\/span>\s*<\/p>/);
  if (m) console.log(`[${d}]\n${m[1].trim()}\n`);
}
