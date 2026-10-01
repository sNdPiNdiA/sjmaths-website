import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { readGitBaseline } from './lib/git-baseline.mjs';
import { externalizeSanskritTopicRuntime } from './lib/sanskrit-topic-runtime.mjs';

const require = createRequire(import.meta.url);
const { ROOT, siteFiles } = require('./seo-html.cjs');
const baseline = process.argv.find(value => value.startsWith('--baseline='))?.slice('--baseline='.length)
  || '237db669da5fca0a8ff8ae6a5a601d284a367642';
const pages = siteFiles().filter(file => file.startsWith('sanskrit/') && file.endsWith('/index.html'));
let migrated = 0;
for await (const [file, bytes] of readGitBaseline(pages, { root: ROOT, baseline })) {
  const original = bytes.toString('utf8');
  const expected = externalizeSanskritTopicRuntime(original);
  const current = fs.readFileSync(path.join(ROOT, file), 'utf8');
  if (expected !== original) migrated++;
  if (current !== expected) throw new Error(`Unexpected Sanskrit content or markup change: ${file}`);
}
if (pages.length !== 163 || migrated !== 26) {
  throw new Error(`Expected 163 Sanskrit pages with 26 exact substitutions; found ${pages.length} and ${migrated}.`);
}
console.log(JSON.stringify({ baseline, pages: pages.length, exactSubstitutions: migrated, byteIdenticalUntouched: pages.length - migrated }, null, 2));
