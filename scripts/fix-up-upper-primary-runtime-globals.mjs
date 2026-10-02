import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { commitBuildWrites } from './lib/build-transaction.mjs';

const require = createRequire(import.meta.url);
const { exposeUpperPrimaryRuntimeGlobals } = require('./lib/up-upper-primary-runtime-globals.cjs');
const { ROOT, siteFiles } = require('./seo-html.cjs');
const apply = process.argv.includes('--apply');
const writes = new Map(), skipped = [];
for (const relative of siteFiles().filter(file => file.startsWith('up-upper-primary-teacher/') && file.endsWith('.html'))) {
  const absolute = path.join(ROOT, relative);
  const before = fs.readFileSync(absolute, 'utf8');
  if (!before.includes('const TOPIC_STORAGE_KEY =')) continue;
  const after = exposeUpperPrimaryRuntimeGlobals(before);
  if (!after) { skipped.push(relative); continue; }
  writes.set(absolute, Buffer.from(after, 'utf8'));
}
if (skipped.length) throw new Error(`Refusing partial runtime-global migration; unexpected template declarations in ${skipped.length} pages.`);
if (apply) commitBuildWrites(writes);
console.log(JSON.stringify({ mode: apply ? 'apply' : 'dry-run', changedPages: writes.size, skipped }, null, 2));
