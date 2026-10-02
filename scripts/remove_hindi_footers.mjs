import fs from 'node:fs';
import path from 'node:path';

const ROOT = process.cwd();
const HINDI_DIR = path.join(ROOT, 'up-upper-primary-teacher', 'hindi');
const HUB_FILE = path.join(HINDI_DIR, 'index.html');

let count = 0;

function cleanDir(dir) {
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  for (const entry of entries) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      cleanDir(full);
    } else if (entry.name === 'index.html' && full !== HUB_FILE) {
      let content = fs.readFileSync(full, 'utf8');
      let changed = false;

      if (content.includes('global-footer.min.js')) {
        content = content.replace(/<script data-cfasync="false" defer="" src="\/assets\/js\/global-footer\.min\.js\?v=[^"]*"><\/script>\r?\n?/g, '');
        changed = true;
      }
      if (content.includes('<div id="footer-container"></div>')) {
        content = content.replace(/<div id="footer-container"><\/div>\r?\n?/g, '');
        changed = true;
      }

      if (changed) {
        fs.writeFileSync(full, content, 'utf8');
        count++;
        console.log(`[CLEANED] ${path.relative(HINDI_DIR, full)}`);
      }
    }
  }
}

cleanDir(HINDI_DIR);
console.log(`\nCleaned footer references from ${count} topic files.`);
