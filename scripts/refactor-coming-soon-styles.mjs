import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { commitBuildWrites } from './lib/build-transaction.mjs';
import { externalizeComingSoonStyle } from './lib/coming-soon-styles.mjs';

const require = createRequire(import.meta.url);
const { ROOT, siteFiles } = require('./seo-html.cjs');
const apply = process.argv.includes('--apply');
const expectedByRoot = new Map([
  ['art', 4],
  ['up-pgt-biology', 226],
  ['up-pgt-civics', 163],
  ['up-pgt-education', 197],
]);
const writes = new Map();
const countsByRoot = new Map();

for (const file of siteFiles().filter(file => file.endsWith('.html'))) {
  const absolute = path.join(ROOT, file);
  const before = fs.readFileSync(absolute, 'utf8');
  const after = externalizeComingSoonStyle(before);
  if (before === after) continue;

  const root = file.split('/')[0];
  if (!expectedByRoot.has(root)) throw new Error(`Unexpected page root contains the shared style: ${file}`);
  if (!/<section\b[^>]*class=["'][^"']*\bcoming-soon\b/i.test(before)) {
    throw new Error(`Matching stylesheet found outside the placeholder template: ${file}`);
  }
  const body = html => html.slice(html.search(/<body\b/i));
  if (!/<body\b/i.test(before) || body(before) !== body(after)) throw new Error(`Body changed: ${file}`);

  countsByRoot.set(root, (countsByRoot.get(root) || 0) + 1);
  writes.set(absolute, Buffer.from(after, 'utf8'));
}

for (const [root, expected] of expectedByRoot) {
  const actual = countsByRoot.get(root) || 0;
  if (![0, expected].includes(actual)) throw new Error(`Expected 0 or ${expected} pages for ${root}; found ${actual}.`);
}
const changedPages = [...countsByRoot.values()].reduce((sum, count) => sum + count, 0);
if (![0, 590].includes(changedPages)) throw new Error(`Expected 0 or 590 pages; found ${changedPages}.`);

if (apply) commitBuildWrites(writes);
console.log(JSON.stringify({
  mode: apply ? 'apply' : 'dry-run',
  changedPages,
  countsByRoot: Object.fromEntries(countsByRoot),
  bodyUnchanged: true,
}, null, 2));
