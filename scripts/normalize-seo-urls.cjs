const fs = require('fs');
const path = require('path');

const ROOT = __dirname.replace(/\\scripts$/, '');
const SKIP = new Set(['.git', '.firebase', '.vscode', 'assets', 'node_modules']);
const DOMAIN_URL = /https:\/\/sjmaths\.com\/[^"'<>\s)]+/g;

function walk(dir) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (entry.isDirectory()) {
      if (!SKIP.has(entry.name)) walk(path.join(dir, entry.name));
      continue;
    }
    if (!entry.isFile() || !entry.name.endsWith('.html')) continue;

    const file = path.join(dir, entry.name);
    const original = fs.readFileSync(file, 'utf8');
    const updated = original.replace(DOMAIN_URL, (url) => {
      const match = url.match(/^(.*?)(\/index\.html|\.html)([?#].*)?$/);
      if (!match) return url;
      const [, base, suffix, tail = ''] = match;
      return `${base}${suffix === '/index.html' ? '/' : ''}${tail}`;
    });
    if (updated !== original) {
      fs.writeFileSync(file, updated, 'utf8');
      console.log(path.relative(ROOT, file));
    }
  }
}

walk(ROOT);
