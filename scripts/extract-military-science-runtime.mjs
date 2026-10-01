// Exact-only controller migration for generated Military Science topic pages.
import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { externalizeMilitaryScienceGenerator, externalizeMilitaryScienceTopicRuntime, militaryScienceTopicRuntime, normalizeMilitaryScienceGenerator } from './lib/military-science-runtime.mjs';
import { commitBuildWrites } from './lib/build-transaction.mjs';

const require = createRequire(import.meta.url);
const { ROOT, siteFiles } = require('./seo-html.cjs');
const apply = process.argv.includes('--apply');
const files = siteFiles().filter(file => file.startsWith('military-science/') && file.endsWith('/index.html'));
const changedPages = [], writes = new Map();
let legacyPages = 0;
for (const file of files) {
  const absolute = path.join(ROOT, file);
  const before = fs.readFileSync(absolute, 'utf8');
  const after = externalizeMilitaryScienceTopicRuntime(before);
  if (before !== after) legacyPages++;
  if (before === after) continue;
  if ((after.match(/data-military-science-topic-runtime=/g) || []).length !== 1) throw new Error(`Unexpected shared runtime count: ${file}`);
  changedPages.push(file);
  writes.set(absolute, Buffer.from(after, 'utf8'));
}
const generatorPath = path.join(ROOT, 'scripts/generate_military_science.mjs');
const generatorBefore = fs.readFileSync(generatorPath, 'utf8');
const generatorAfter = externalizeMilitaryScienceGenerator(generatorBefore);
if (normalizeMilitaryScienceGenerator(generatorBefore) !== normalizeMilitaryScienceGenerator(generatorAfter)) {
  throw new Error('Military Science generator change exceeded its exact controller/import allowance.');
}
if (generatorBefore !== generatorAfter) writes.set(generatorPath, Buffer.from(generatorAfter, 'utf8'));
if (legacyPages && legacyPages !== 46) throw new Error(`Expected exactly 46 legacy Military Science runtimes; found ${legacyPages}`);
if ((generatorAfter.match(/\$\{militaryScienceTopicScript\}/g) || []).length !== 1) throw new Error('Expected exactly one shared controller interpolation in Military Science generator.');
if (apply) commitBuildWrites(writes);
console.log(JSON.stringify({ mode: apply ? 'apply' : 'dry-run', controllerBytes: Buffer.byteLength(militaryScienceTopicRuntime), scannedPages: files.length, legacyPages, changedPages: changedPages.length, generatorChanged: generatorBefore !== generatorAfter }, null, 2));
