// Exact migration of the bilingual GK topic runtime and its maintained generators.
import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { commitBuildWrites } from './lib/build-transaction.mjs';
import {
  externalizeUpTgtPgtGkGenerator,
  externalizeUpTgtPgtGkTopicRuntime,
  normalizeUpTgtPgtGkGeneratorForParity,
  upTgtPgtGkRuntimeTag,
} from './lib/up-tgt-pgt-gk-runtime.mjs';

const require = createRequire(import.meta.url);
const { ROOT, siteFiles } = require('./seo-html.cjs');
const apply = process.argv.includes('--apply');
const candidates = siteFiles().filter(file => file.startsWith('up-tgt-pgt-gk/') && file.endsWith('/index.html'));
const writes = new Map();
let changedPages = 0;
let bilingualPages = 0;

for (const file of candidates) {
  const absolute = path.join(ROOT, file);
  const before = fs.readFileSync(absolute, 'utf8');
  if (!before.includes('id="bilingual-data"')) continue;
  bilingualPages++;
  const after = externalizeUpTgtPgtGkTopicRuntime(before);
  if (after === before) continue;
  if ((after.match(/data-up-tgt-pgt-gk-runtime="topic"/g) || []).length !== 1) {
    throw new Error(`Expected exactly one shared GK runtime link in ${file}`);
  }
  if ((after.match(/data-up-tgt-pgt-gk-runtime="language"/g) || []).length !== 1) {
    throw new Error(`Expected exactly one shared GK language runtime link in ${file}`);
  }
  changedPages++;
  writes.set(absolute, Buffer.from(after, 'utf8'));
}

if (![0, 55].includes(changedPages) || bilingualPages !== 55) {
  throw new Error(`Expected 55 bilingual pages and either 0 or 55 exact runtime replacements; found ${bilingualPages} and ${changedPages}.`);
}

const generatorPath = path.join(ROOT, 'scripts/generate_up_tgt_pgt_gk.mjs');
const generatorBefore = fs.readFileSync(generatorPath, 'utf8');
const generatorAfter = externalizeUpTgtPgtGkGenerator(generatorBefore);
if (normalizeUpTgtPgtGkGeneratorForParity(generatorBefore) !== normalizeUpTgtPgtGkGeneratorForParity(generatorAfter)) {
  throw new Error('GK generator change exceeded the shared-runtime import/reference replacement.');
}
if ((generatorAfter.match(/\$\{upTgtPgtGkRuntimeTag\}/g) || []).length !== 1) {
  throw new Error('Expected one shared GK runtime in the generator template.');
}
if (generatorBefore !== generatorAfter) writes.set(generatorPath, Buffer.from(generatorAfter, 'utf8'));

if (apply) commitBuildWrites(writes);
console.log(JSON.stringify({
  mode: apply ? 'apply' : 'dry-run',
  candidatePages: candidates.length,
  bilingualPages,
  changedPages,
  generatorChanged: generatorBefore !== generatorAfter,
  runtimeTag: upTgtPgtGkRuntimeTag,
}, null, 2));
