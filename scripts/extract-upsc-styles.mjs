// Exact stylesheet migration with whole-body preservation and rollback.
import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { externalizeUpscStyles } from './lib/upsc-styles.mjs';
import { commitBuildWrites } from './lib/build-transaction.mjs';
const require = createRequire(import.meta.url);
const { ROOT, siteFiles } = require('./seo-html.cjs');
const apply = process.argv.includes('--apply');
const changes = [], writes = new Map();
for (const file of siteFiles().filter(file => file.startsWith('upsc/') && file.endsWith('.html'))) {
  const absolute = path.join(ROOT, file);
  const before = fs.readFileSync(absolute, 'utf8');
  const after = externalizeUpscStyles(before);
  if (before === after) continue;
  const bodyAt = before.search(/<body\b/i);
  if (bodyAt < 0 || before.slice(bodyAt) !== after.slice(after.search(/<body\b/i))) throw new Error(`Body changed: ${file}`);
  changes.push(file);
  writes.set(absolute, Buffer.from(after, 'utf8'));
}
if (apply) commitBuildWrites(writes);
console.log(JSON.stringify({ mode: apply ? 'apply' : 'dry-run', changed: changes.length, bodyUnchanged: true, files: changes }, null, 2));
