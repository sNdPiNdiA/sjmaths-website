// Migrate only the exact shared runtime in English and Geography pages.
import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { externalizeExamTopicRuntime } from './lib/exam-topic-runtime.mjs';
import { commitBuildWrites } from './lib/build-transaction.mjs';
const require = createRequire(import.meta.url);
const { ROOT, siteFiles } = require('./seo-html.cjs');
const apply = process.argv.includes('--apply');
const changes = [], writes = new Map();
for (const file of siteFiles().filter(file => /^(english|geography)\//.test(file) && file.endsWith('.html'))) {
  const absolute = path.join(ROOT, file);
  const before = fs.readFileSync(absolute, 'utf8');
  const after = externalizeExamTopicRuntime(before);
  if (before === after) continue;
  if ((after.match(/data-exam-topic-runtime=/g) || []).length !== 1) throw new Error(`Unexpected runtime count: ${file}`);
  changes.push(file);
  writes.set(absolute, Buffer.from(after, 'utf8'));
}
if (apply) commitBuildWrites(writes);
console.log(JSON.stringify({ mode: apply ? 'apply' : 'dry-run', changed: changes.length, files: changes }, null, 2));
