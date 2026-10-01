import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';
import { createRequire } from 'node:module';
import {
  externalizePhysicalEducationStyles,
  externalizePhysicalEducationTranslator,
} from './lib/physical-education-styles.mjs';

const require = createRequire(import.meta.url);
const { ROOT, siteFiles } = require('./seo-html.cjs');
const baseline = process.argv.find(value => value.startsWith('--baseline='))?.slice('--baseline='.length) || '6be921178f2787101ae755971253e564df0c85f2';
const pages = siteFiles().filter(file => file.startsWith('physical-education/') && file.endsWith('/index.html'));
let migrated = 0;
let unchanged = 0;

for (const file of pages) {
  const original = execFileSync('git', ['show', `${baseline}:${file}`], { cwd: ROOT, encoding: 'utf8', maxBuffer: 20e6 });
  const expected = externalizePhysicalEducationStyles(original);
  const current = fs.readFileSync(path.join(ROOT, file), 'utf8');
  if (expected !== original) migrated++;
  else unchanged++;
  if (current !== expected) throw new Error(`Unexpected generated-page change: ${file}`);
}

const translatorPath = 'scripts/translate_physical_education_hindi.mjs';
const translatorOriginal = execFileSync('git', ['show', `${baseline}:${translatorPath}`], { cwd: ROOT, encoding: 'utf8', maxBuffer: 20e6 });
const translatorExpected = externalizePhysicalEducationTranslator(translatorOriginal);
const translatorCurrent = fs.readFileSync(path.join(ROOT, translatorPath), 'utf8');
if (translatorCurrent !== translatorExpected) throw new Error('Unexpected change in the maintained Hindi translator.');
if (migrated !== 307 || unchanged !== 16) throw new Error(`Expected 307 extracted and 16 untouched page variants; got ${migrated} and ${unchanged}.`);

console.log(JSON.stringify({ baseline, pages: pages.length, extracted: migrated, untouchedVariants: unchanged, translator: 'exact stylesheet/import change only' }, null, 2));
