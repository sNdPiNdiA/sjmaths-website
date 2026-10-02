import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { readGitBaseline } from './lib/git-baseline.mjs';
import { externalizeSociologyBilingualStyle } from './lib/sociology-bilingual-styles.mjs';

const require = createRequire(import.meta.url);
const { ROOT, siteFiles } = require('./seo-html.cjs');
const baseline = process.argv.find(value => value.startsWith('--baseline='))?.slice('--baseline='.length)
  || '5d341a929ac7484c0c9c6e84486dab4e33a95995';
const pages = siteFiles().filter(file => file.startsWith('up-pgt-sociology/') && file.endsWith('/index.html'));
const normalizeLineEndings = source => source.replace(/\r\n/g, '\n');
let migrated = 0;
for await (const [file, bytes] of readGitBaseline(pages, { root: ROOT, baseline })) {
  const original = bytes.toString('utf8');
  const expected = externalizeSociologyBilingualStyle(original);
  const current = fs.readFileSync(path.join(ROOT, file), 'utf8');
  if (expected !== original) migrated++;
  if (normalizeLineEndings(current) !== normalizeLineEndings(expected)) throw new Error(`Unexpected Sociology page change: ${file}`);
}
if (pages.length !== 106 || migrated !== 88) {
  throw new Error(`Expected 106 Sociology pages with 88 exact substitutions; found ${pages.length} and ${migrated}.`);
}
console.log(JSON.stringify({ baseline, pages: pages.length, exactSubstitutions: migrated, byteIdenticalUntouched: pages.length - migrated }, null, 2));
