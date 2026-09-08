const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const SKIP = new Set(['.git', '.firebase', '.vscode', 'assets', 'node_modules', 'scratch']);

let fixedCount = 0;

function walk(dir) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (entry.isDirectory()) {
      if (!SKIP.has(entry.name)) walk(path.join(dir, entry.name));
      continue;
    }
    if (!entry.isFile() || !entry.name.endsWith('.html')) continue;

    const file = path.join(dir, entry.name);
    let html = fs.readFileSync(file, 'utf8');

    let modified = false;
    html = html.replace(/<img\s+([^>]+)>/gi, (fullTag, attrs) => {
      let updatedAttrs = attrs;
      if (!/loading=/i.test(attrs) && !/fetchpriority=["']high["']/i.test(attrs)) {
        updatedAttrs += ' loading="lazy"';
        modified = true;
      }
      if (!/decoding=/i.test(attrs)) {
        updatedAttrs += ' decoding="async"';
        modified = true;
      }
      return `<img ${updatedAttrs}>`;
    });

    if (modified) {
      fs.writeFileSync(file, html, 'utf8');
      fixedCount++;
    }
  }
}

walk(ROOT);
console.log(`Updated images with lazy-loading & async decoding across ${fixedCount} HTML files.`);
