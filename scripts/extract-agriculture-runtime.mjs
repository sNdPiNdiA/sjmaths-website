// Exact runtime sharing only: never invoke the content-changing redesign batch.
import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { externalizeAgricultureRuntime } from './lib/agriculture-runtime.mjs';
import { commitBuildWrites } from './lib/build-transaction.mjs';
const require = createRequire(import.meta.url);
const { ROOT, siteFiles } = require('./seo-html.cjs');
const apply = process.argv.includes('--apply');
const changes = [], writes = new Map();
for (const file of siteFiles().filter(file => file.startsWith('agriculture/') && file.endsWith('.html'))) {
  const absolute = path.join(ROOT, file);
  const before = fs.readFileSync(absolute, 'utf8');
  const after = externalizeAgricultureRuntime(before);
  if (before === after) continue;
  if ((after.match(/data-agriculture-runtime=/g) || []).length !== 1) throw new Error(`Unexpected runtime count: ${file}`);
  changes.push(file);
  writes.set(absolute, Buffer.from(after, 'utf8'));
}
if (apply) commitBuildWrites(writes);
console.log(JSON.stringify({ mode: apply ? 'apply' : 'dry-run', changed: changes.length, files: changes }, null, 2));
