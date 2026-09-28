// Plan the whole migration before replacing any page. Ordinary write failure
// rolls back through the existing build transaction.
import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { externalizeUpscLanguage } from './lib/upsc-language.mjs';
import { commitBuildWrites } from './lib/build-transaction.mjs';
const require = createRequire(import.meta.url);
const { ROOT, siteFiles } = require('./seo-html.cjs');
const apply = process.argv.includes('--apply');
const changes = [], writes = new Map();
for (const file of siteFiles().filter(file => file.startsWith('upsc/') && file.endsWith('.html'))) {
  const absolute = path.join(ROOT, file);
  const before = fs.readFileSync(absolute, 'utf8');
  const after = externalizeUpscLanguage(before);
  if (before === after) continue;
  // The exact matcher leaves every other byte intact. Require precisely one
  // replacement per page to reject ambiguous ownership before any writes.
  const tag = 'data-upsc-shared-script="language"';
  if (after.split(tag).length - before.split(tag).length !== 1) throw new Error(`Ambiguous script: ${file}`);
  changes.push(file);
  writes.set(absolute, Buffer.from(after, 'utf8'));
}
if (apply) commitBuildWrites(writes);
console.log(JSON.stringify({ mode: apply ? 'apply' : 'dry-run', changed: changes.length, files: changes }, null, 2));
