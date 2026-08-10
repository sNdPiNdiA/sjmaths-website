const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const SKIP = new Set(['.git', '.firebase', '.vscode', 'assets', 'node_modules']);

function walk(dir) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (entry.isDirectory()) {
      if (!SKIP.has(entry.name)) walk(path.join(dir, entry.name));
      continue;
    }
    if (!entry.isFile() || entry.name !== 'index.html') continue;
    const file = path.join(dir, entry.name);
    const html = fs.readFileSync(file, 'utf8');
    if (!/class="placeholder|<title>Placeholder/i.test(html)) continue;
    if (/name=["']robots["'][^>]*noindex/i.test(html)) continue;
    const updated = html.replace(
      /(<meta\s+name=["']robots["']\s+content=["'])index,\s*follow/i,
      '$1noindex, follow',
    );
    if (updated !== html) {
      fs.writeFileSync(file, updated, 'utf8');
      console.log(path.relative(ROOT, file));
    }
  }
}

walk(ROOT);
