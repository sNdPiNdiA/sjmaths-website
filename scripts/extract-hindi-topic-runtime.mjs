// Exact-only Hindi topic-page migration, including its maintained generator.
import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { externalizeHindiGenerator, externalizeHindiTopicRuntime, normalizeHindiGenerator } from './lib/hindi-topic-runtime.mjs';
import { commitBuildWrites } from './lib/build-transaction.mjs';

const require = createRequire(import.meta.url);
const { ROOT, siteFiles } = require('./seo-html.cjs');
const apply = process.argv.includes('--apply');
const files = siteFiles().filter(file => file.startsWith('hindi/') && file.endsWith('.html'));
const changedPages = [], writes = new Map();
let legacyPages = 0;
for (const file of files) {
  const absolute = path.join(ROOT, file);
  const before = fs.readFileSync(absolute, 'utf8');
  const after = externalizeHindiTopicRuntime(before);
  if (before !== after) legacyPages++;
  if (before === after) continue;
  if ((after.match(/data-hindi-topic-runtime=/g) || []).length !== 1) throw new Error(`Unexpected shared runtime count: ${file}`);
  changedPages.push(file);
  writes.set(absolute, Buffer.from(after, 'utf8'));
}
const generatorPath = path.join(ROOT, 'scripts/generate_hindi.mjs');
const generatorBefore = fs.readFileSync(generatorPath, 'utf8');
const generatorAfter = externalizeHindiGenerator(generatorBefore);
if (normalizeHindiGenerator(generatorBefore) !== normalizeHindiGenerator(generatorAfter)) {
  throw new Error('Hindi generator change exceeded its exact controller/import allowance.');
}
if (generatorBefore !== generatorAfter) writes.set(generatorPath, Buffer.from(generatorAfter, 'utf8'));
if (legacyPages && legacyPages !== 102) throw new Error(`Expected exactly 102 legacy Hindi runtimes; found ${legacyPages}`);
if ((generatorAfter.match(/\$\{hindiTopicScript\}/g) || []).length !== 1) throw new Error('Expected exactly one shared controller interpolation in Hindi generator.');
if (apply) commitBuildWrites(writes);
console.log(JSON.stringify({ mode: apply ? 'apply' : 'dry-run', scannedPages: files.length, legacyPages, changedPages: changedPages.length, generatorChanged: generatorBefore !== generatorAfter, files: changedPages }, null, 2));
