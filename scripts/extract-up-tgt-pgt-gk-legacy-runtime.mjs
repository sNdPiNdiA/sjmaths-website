import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { commitBuildWrites } from './lib/build-transaction.mjs';
import {
  externalizeUpTgtPgtGkTopicRuntime,
  legacyEnglishOnlyUpTgtPgtGkRuntimeHash,
  upTgtPgtGkRuntimeTag,
} from './lib/up-tgt-pgt-gk-runtime.mjs';

const require = createRequire(import.meta.url);
const { ROOT, siteFiles } = require('./seo-html.cjs');
const apply = process.argv.includes('--apply');
const pages = siteFiles().filter(file => file.startsWith('up-tgt-pgt-gk/') && file.endsWith('/index.html'));
const writes = new Map();
const changed = [];

for (const file of pages) {
  const absolute = path.join(ROOT, file);
  const before = fs.readFileSync(absolute, 'utf8');
  if (before.includes('data-up-tgt-pgt-gk-runtime="topic"')) continue;
  let after;
  try { after = externalizeUpTgtPgtGkTopicRuntime(before, legacyEnglishOnlyUpTgtPgtGkRuntimeHash); }
  catch (error) {
    if (error.message === 'Expected an exact legacy GK runtime or its shared reference.') continue;
    throw new Error(`${file}: ${error.message}`);
  }
  if (after === before) continue;
  if ((after.match(/data-up-tgt-pgt-gk-runtime="topic"/g) || []).length !== 1) {
    throw new Error(`Expected exactly one shared GK topic runtime in ${file}.`);
  }
  changed.push(file);
  writes.set(absolute, Buffer.from(after, 'utf8'));
}

if (![0, 13].includes(changed.length)) throw new Error(`Expected 0 or 13 exact English-only GK runtime replacements; found ${changed.length}.`);
if (apply) commitBuildWrites(writes);
console.log(JSON.stringify({ mode: apply ? 'apply' : 'dry-run', scannedPages: pages.length, exactReplacements: changed.length, sharedRuntime: upTgtPgtGkRuntimeTag, writes: writes.size }, null, 2));
