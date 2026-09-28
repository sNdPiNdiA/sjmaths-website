/* Add the shared favicon to managed curriculum pages that do not declare one. */
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const TARGET_DIRS = process.argv.filter(arg => arg.startsWith('--scope='))
  .flatMap(arg => arg.slice(8).split(','))
  .map(value => value.trim())
  .filter(Boolean);
const DRY_RUN = process.argv.includes('--dry-run');
const DEFAULT_DIRS = ['class-9-maths', 'class-10-maths', 'class-11-maths', 'class-12-maths'];
const scopes = TARGET_DIRS.length ? TARGET_DIRS : DEFAULT_DIRS;
let inspected = 0;
let modified = 0;

function walk(directory) {
  if (!fs.existsSync(directory)) return;
  for (const entry of fs.readdirSync(directory, { withFileTypes: true })) {
    const absolute = path.join(directory, entry.name);
    if (entry.isDirectory()) walk(absolute);
    else if (entry.isFile() && entry.name.endsWith('.html')) repair(absolute);
  }
}

function repair(absolute) {
  inspected++;
  const original = fs.readFileSync(absolute, 'utf8');
  if (!/<head\b/i.test(original) || /<link\b[^>]*\brel\s*=\s*["'][^"']*\bicon\b/i.test(original)) return;
  const favicon = '    <link rel="icon" type="image/png" href="/favicon.png">';
  const next = original.replace(/(<title\b[^>]*>[\s\S]*?<\/title>)/i, `$1\n${favicon}`);
  if (next === original) return;
  if (!DRY_RUN) fs.writeFileSync(absolute, next, 'utf8');
  modified++;
}

for (const scope of scopes) walk(path.join(ROOT, scope));
console.log(JSON.stringify({ dryRun: DRY_RUN, scopes, inspected, modified }));
