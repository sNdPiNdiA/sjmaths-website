import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { readGitBaseline } from './lib/git-baseline.mjs';
import { externalizeSscCglTopicAssets } from './lib/ssc-cgl-topic-assets.mjs';

const require = createRequire(import.meta.url);
const { ROOT, siteFiles } = require('./seo-html.cjs');
const baseline = process.argv.find(value => value.startsWith('--baseline='))?.slice('--baseline='.length)
  || '4a81ff7b7c9adce1ae0eba3f7243c9d722ad400a';
const pages = siteFiles().filter(file => file.startsWith('ssc-cgl/') && file.endsWith('/index.html'));
let migrated = 0;

for await (const [file, bytes] of readGitBaseline(pages, { root: ROOT, baseline })) {
  const original = bytes.toString('utf8');
  const expected = externalizeSscCglTopicAssets(original);
  const current = fs.readFileSync(path.join(ROOT, file), 'utf8');
  if (expected !== original) migrated++;
  if (current !== expected) throw new Error(`Unexpected SSC-CGL content or markup change: ${file}`);
}

if (pages.length !== 322 || migrated !== 152) {
  throw new Error(`Expected 322 SSC-CGL pages with 152 exact substitutions; found ${pages.length} and ${migrated}.`);
}
console.log(JSON.stringify({ baseline, pages: pages.length, exactSubstitutions: migrated, byteIdenticalUntouched: pages.length - migrated }, null, 2));
