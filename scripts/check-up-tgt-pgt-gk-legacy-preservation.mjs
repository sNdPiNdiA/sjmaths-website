import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { readGitBaseline } from './lib/git-baseline.mjs';
import { externalizeUpTgtPgtGkTopicRuntime, legacyEnglishOnlyUpTgtPgtGkRuntimeHash } from './lib/up-tgt-pgt-gk-runtime.mjs';

const require = createRequire(import.meta.url);
const { ROOT, siteFiles } = require('./seo-html.cjs');
const baseline = process.argv.find(value => value.startsWith('--baseline='))?.slice('--baseline='.length)
  || 'afb5a3473445d7609eb3004b999c66b9d0215c70';
const pages = siteFiles().filter(file => file.startsWith('up-tgt-pgt-gk/') && file.endsWith('/index.html'));
let migrated = 0;
for await (const [file, bytes] of readGitBaseline(pages, { root: ROOT, baseline })) {
  const original = bytes.toString('utf8');
  let expected = original;
  try { expected = externalizeUpTgtPgtGkTopicRuntime(original, legacyEnglishOnlyUpTgtPgtGkRuntimeHash); }
  catch (error) {
    if (error.message !== 'Expected an exact legacy GK runtime or its shared reference.') throw error;
  }
  const current = fs.readFileSync(path.join(ROOT, file), 'utf8');
  if (expected !== original) migrated++;
  if (current !== expected) throw new Error(`Unexpected page/content change: ${file}`);
}
if (migrated !== 13) throw new Error(`Expected 13 exact English-only GK runtime substitutions; found ${migrated}.`);
console.log(JSON.stringify({ baseline, pages: pages.length, exactReplacements: migrated, untouched: pages.length - migrated }, null, 2));
