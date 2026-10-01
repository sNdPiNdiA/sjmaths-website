// Replace only the two fingerprinted classic scripts in ASO topic pages.
import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { externalizeAsoTopicRuntimes } from './lib/aso-topic-runtime.mjs';
import { commitBuildWrites } from './lib/build-transaction.mjs';

const require = createRequire(import.meta.url);
const { ROOT, siteFiles } = require('./seo-html.cjs');
const apply = process.argv.includes('--apply');
const changed = [], writes = new Map();
const files = siteFiles().filter(file => file.startsWith('upsc-aso/') && file.endsWith('.html'));
for (const file of files) {
  const absolute = path.join(ROOT, file);
  const before = fs.readFileSync(absolute, 'utf8');
  const after = externalizeAsoTopicRuntimes(before);
  if (before === after) continue;
  if ((after.match(/data-aso-topic-runtime=/g) || []).length !== 2) throw new Error(`Unexpected shared runtime count: ${file}`);
  changed.push(file);
  writes.set(absolute, Buffer.from(after, 'utf8'));
}
if (apply) commitBuildWrites(writes);
console.log(JSON.stringify({ mode: apply ? 'apply' : 'dry-run', scanned: files.length, changed: changed.length, files: changed }, null, 2));
