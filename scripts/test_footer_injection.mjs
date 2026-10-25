import fs from 'node:fs';
import path from 'node:path';

const ROOT = process.cwd();

const EXCLUDE_DIRS = new Set([
  'node_modules',
  '.git',
  '.pages-dist',
  '.agents',
  '.gemini',
  'tmp',
  'scratch',
  'components'
]);

let scanned = 0;
let alreadyCompliant = 0;
let replacedEmptyContainer = 0;
let replacedOldFooter = 0;
let appendedNoFooter = 0;
let unhandled = 0;
const unhandledList = [];

function checkFile(fullPath) {
  scanned++;
  const c = fs.readFileSync(fullPath, 'utf8');

  // Check if already has complete compliant footer
  if (c.includes('id="site-footer"') && c.includes('/pages/privacy-policy.html')) {
    alreadyCompliant++;
    return;
  }

  // 1. Empty footer-container
  if (/<div id=["']footer-container["']>\s*<\/div>/i.test(c)) {
    replacedEmptyContainer++;
    return;
  }

  // 2. Old footer tag
  if (/<footer[\s>]/i.test(c)) {
    replacedOldFooter++;
    return;
  }

  // 3. No footer at all
  if (c.includes('</main>') || c.includes('</body>')) {
    appendedNoFooter++;
    return;
  }

  unhandled++;
  if (unhandledList.length < 10) unhandledList.push(fullPath);
}

function walk(dir) {
  for (const item of fs.readdirSync(dir, { withFileTypes: true })) {
    if (EXCLUDE_DIRS.has(item.name)) continue;
    const full = path.join(dir, item.name);
    if (item.isDirectory()) {
      walk(full);
    } else if (item.name.endsWith('.html')) {
      checkFile(full);
    }
  }
}

walk(ROOT);

console.log('DRY RUN AUDIT RESULTS:');
console.log({
  scanned,
  alreadyCompliant,
  replacedEmptyContainer,
  replacedOldFooter,
  appendedNoFooter,
  unhandled
});
if (unhandledList.length > 0) {
  console.log('Sample unhandled:', unhandledList);
}

