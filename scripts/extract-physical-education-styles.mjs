// Exact-block extraction for the bilingual Physical Education lesson pipeline.
import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { commitBuildWrites } from './lib/build-transaction.mjs';
import {
  externalizePhysicalEducationStyles,
  externalizePhysicalEducationTranslator,
  normalizePhysicalEducationTranslator,
  physicalEducationTopicStyleLink,
} from './lib/physical-education-styles.mjs';

const require = createRequire(import.meta.url);
const { ROOT, siteFiles } = require('./seo-html.cjs');
const apply = process.argv.includes('--apply');
const files = siteFiles().filter(file => file.startsWith('physical-education/') && file.endsWith('/index.html'));
const writes = new Map();
const changedPages = [];
let inlinePages = 0;

for (const file of files) {
  const absolute = path.join(ROOT, file);
  const before = fs.readFileSync(absolute, 'utf8');
  const after = externalizePhysicalEducationStyles(before);
  if (before === after) continue;
  inlinePages++;
  const bodyStart = html => html.search(/<body\b/i);
  if (bodyStart(before) < 0 || before.slice(bodyStart(before)) !== after.slice(bodyStart(after))) {
    throw new Error(`Body changed: ${file}`);
  }
  changedPages.push(file);
  writes.set(absolute, Buffer.from(after, 'utf8'));
}

if (![0, 307].includes(inlinePages)) throw new Error(`Expected 0 or 307 legacy bilingual styles; found ${inlinePages}.`);
if (changedPages.length !== inlinePages) throw new Error(`Expected ${inlinePages} exact style replacements; found ${changedPages.length}.`);

const translatorPath = path.join(ROOT, 'scripts/translate_physical_education_hindi.mjs');
const translatorBefore = fs.readFileSync(translatorPath, 'utf8');
const translatorAfter = externalizePhysicalEducationTranslator(translatorBefore);
if (normalizePhysicalEducationTranslator(translatorBefore) !== normalizePhysicalEducationTranslator(translatorAfter)) {
  throw new Error('Translator change exceeded the exact stylesheet/import allowance.');
}
if ((translatorAfter.match(/\$\{physicalEducationTopicStyleLink\}/g) || []).length !== 1) {
  throw new Error('Expected one shared stylesheet interpolation in the Physical Education translator.');
}
if (translatorBefore !== translatorAfter) writes.set(translatorPath, Buffer.from(translatorAfter, 'utf8'));

if (apply) commitBuildWrites(writes);
console.log(JSON.stringify({
  mode: apply ? 'apply' : 'dry-run',
  scannedPages: files.length,
  inlinePages,
  changedPages: changedPages.length,
  translatorChanged: translatorBefore !== translatorAfter,
  styleLink: physicalEducationTopicStyleLink,
}, null, 2));
