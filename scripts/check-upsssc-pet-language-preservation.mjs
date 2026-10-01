import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { readGitBaseline } from './lib/git-baseline.mjs';
import { externalizeUpssscPetLanguage } from './lib/upsssc-pet-language.mjs';

const require = createRequire(import.meta.url);
const { ROOT, siteFiles } = require('./seo-html.cjs');
const baseline = process.argv.find(value => value.startsWith('--baseline='))?.slice('--baseline='.length)
  || '237db669da5fca0a8ff8ae6a5a601d284a367642';
const pages = siteFiles().filter(file => file.startsWith('upsssc-pet/') && file.endsWith('/index.html'));
let migrated = 0;
for await (const [file, bytes] of readGitBaseline(pages, { root: ROOT, baseline })) {
  const original = bytes.toString('utf8');
  const expected = externalizeUpssscPetLanguage(original);
  const current = fs.readFileSync(path.join(ROOT, file), 'utf8');
  if (expected !== original) migrated++;
  if (current !== expected) throw new Error(`Unexpected page/content change: ${file}`);
}
if (migrated !== 87) throw new Error(`Expected 87 exact language-bootstrap replacements; found ${migrated}.`);
console.log(JSON.stringify({ baseline, pages: pages.length, exactReplacements: migrated, untouched: pages.length - migrated }, null, 2));
