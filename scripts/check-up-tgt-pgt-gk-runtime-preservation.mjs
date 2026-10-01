import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';
import { createRequire } from 'node:module';
import {
  externalizeUpTgtPgtGkGenerator,
  externalizeUpTgtPgtGkTopicRuntime,
} from './lib/up-tgt-pgt-gk-runtime.mjs';

const require = createRequire(import.meta.url);
const { ROOT, siteFiles } = require('./seo-html.cjs');
const baseline = process.argv.find(value => value.startsWith('--baseline='))?.slice('--baseline='.length) || '6be921178f2787101ae755971253e564df0c85f2';
const pages = siteFiles().filter(file => file.startsWith('up-tgt-pgt-gk/') && file.endsWith('/index.html'));
let migrated = 0;
let untouched = 0;

for (const file of pages) {
  const original = execFileSync('git', ['show', `${baseline}:${file}`], { cwd: ROOT, encoding: 'utf8', maxBuffer: 20e6 });
  const expected = original.includes('id="bilingual-data"')
    ? externalizeUpTgtPgtGkTopicRuntime(original)
    : original;
  const current = fs.readFileSync(path.join(ROOT, file), 'utf8');
  if (expected !== original) migrated++;
  else untouched++;
  if (current !== expected) throw new Error(`Unexpected content or markup change: ${file}`);
}

const generatorPath = 'scripts/generate_up_tgt_pgt_gk.mjs';
const generatorOriginal = execFileSync('git', ['show', `${baseline}:${generatorPath}`], { cwd: ROOT, encoding: 'utf8', maxBuffer: 20e6 });
if (fs.readFileSync(path.join(ROOT, generatorPath), 'utf8') !== externalizeUpTgtPgtGkGenerator(generatorOriginal)) {
  throw new Error('Unexpected GK generator change.');
}
if (migrated !== 55 || untouched !== pages.length - 55) {
  throw new Error(`Expected 55 exact runtime replacements; found ${migrated} changes and ${untouched} untouched pages.`);
}

console.log(JSON.stringify({ baseline, pages: pages.length, migrated, untouched, generator: 'runtime reference only' }, null, 2));
