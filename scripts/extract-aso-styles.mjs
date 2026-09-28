import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { externalizeAsoStyles } from './lib/aso-styles.mjs';
import { commitBuildWrites } from './lib/build-transaction.mjs';
const require = createRequire(import.meta.url);
const { ROOT, siteFiles } = require('./seo-html.cjs');
const writes = new Map(), files = [];
for (const file of siteFiles().filter(file => file.startsWith('upsc-aso/') && file.endsWith('.html'))) {
  const absolute = path.join(ROOT, file);
  const before = fs.readFileSync(absolute, 'utf8');
  const after = externalizeAsoStyles(before);
  if (before === after) continue;
  const body = html => html.slice(html.search(/<body\b/i));
  if (!/<body\b/i.test(before) || body(before) !== body(after)) throw new Error(`Body changed: ${file}`);
  files.push(file); writes.set(absolute, Buffer.from(after));
}
const apply = process.argv.includes('--apply');
if (apply) commitBuildWrites(writes);
console.log(JSON.stringify({ mode: apply ? 'apply' : 'dry-run', changed: files.length, bodyUnchanged: true, files }, null, 2));
