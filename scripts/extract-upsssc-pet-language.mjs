import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { commitBuildWrites } from './lib/build-transaction.mjs';
import { externalizeUpssscPetLanguage } from './lib/upsssc-pet-language.mjs';

const require = createRequire(import.meta.url);
const { ROOT, siteFiles } = require('./seo-html.cjs');
const apply = process.argv.includes('--apply');
const pages = siteFiles().filter(file => file.startsWith('upsssc-pet/') && file.endsWith('/index.html'));
const writes = new Map();
const changedPages = [];

for (const file of pages) {
  const absolute = path.join(ROOT, file);
  const before = fs.readFileSync(absolute, 'utf8');
  const hasLegacyBootstrap = [...before.matchAll(/<script>([\s\S]*?)<\/script>/gi)]
    .some(match => match[1].includes('sj_pref_lang') && match[1].includes('langEn'));
  if (!hasLegacyBootstrap) continue;
  if (!/id=["']langEn["']/.test(before) || !/id=["']langHi["']/.test(before)
      || !/class=["'][^"']*\blang-en\b/.test(before) || !/class=["'][^"']*\blang-hi\b/.test(before)) {
    throw new Error(`Language bootstrap controls or content classes are missing in ${file}.`);
  }
  if (/data-upsc-shared-script=["']language["']/.test(before)) throw new Error(`Duplicate shared language script already present in ${file}.`);
  const after = externalizeUpssscPetLanguage(before, { strict: true });
  if (before === after) throw new Error(`Expected language bootstrap replacement did not change ${file}.`);
  changedPages.push(file);
  writes.set(absolute, Buffer.from(after, 'utf8'));
}

if (![0, 87].includes(changedPages.length)) throw new Error(`Expected 0 or 87 exact replacements; found ${changedPages.length}.`);
if (apply) commitBuildWrites(writes);
console.log(JSON.stringify({ mode: apply ? 'apply' : 'dry-run', scannedPages: pages.length, exactReplacements: changedPages.length, untouchedPages: pages.length - changedPages.length, writes: writes.size }, null, 2));
