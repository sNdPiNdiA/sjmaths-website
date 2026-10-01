// Exact-block extraction for generated Mathematics topic pages.
import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { commitBuildWrites } from './lib/build-transaction.mjs';
import {
  externalizeMathematicsGenerator,
  externalizeMathematicsStyles,
  normalizeMathematicsGenerator,
} from './lib/mathematics-styles.mjs';

const require = createRequire(import.meta.url);
const { ROOT, siteFiles } = require('./seo-html.cjs');
const apply = process.argv.includes('--apply');
const files = siteFiles().filter(file => file.startsWith('mathematics/') && file.endsWith('/index.html'));
const writes = new Map();
const changedPages = [];

for (const file of files) {
  const absolute = path.join(ROOT, file);
  const before = fs.readFileSync(absolute, 'utf8');
  const after = externalizeMathematicsStyles(before);
  if (before === after) continue;
  const body = html => html.slice(html.search(/<body\b/i));
  if (!/<body\b/i.test(before) || body(before) !== body(after)) throw new Error(`Body changed: ${file}`);
  changedPages.push(file);
  writes.set(absolute, Buffer.from(after, 'utf8'));
}

const generatorPath = path.join(ROOT, 'scripts/generate_mathematics.mjs');
const generatorBefore = fs.readFileSync(generatorPath, 'utf8');
const generatorAfter = externalizeMathematicsGenerator(generatorBefore);
if (normalizeMathematicsGenerator(generatorBefore) !== normalizeMathematicsGenerator(generatorAfter)) {
  throw new Error('Mathematics generator change exceeded the exact stylesheet/import allowance.');
}
if (generatorBefore !== generatorAfter) writes.set(generatorPath, Buffer.from(generatorAfter, 'utf8'));
if (![0, 299].includes(changedPages.length)) throw new Error(`Expected 0 or 299 inline Mathematics styles; found ${changedPages.length}.`);
if ((generatorAfter.match(/\$\{mathematicsTopicStyleLink\}/g) || []).length !== 1) {
  throw new Error('Expected exactly one shared stylesheet interpolation in the Mathematics generator.');
}

if (apply) commitBuildWrites(writes);
console.log(JSON.stringify({ mode: apply ? 'apply' : 'dry-run', scannedPages: files.length, changedPages: changedPages.length, bodyUnchanged: true, generatorChanged: generatorBefore !== generatorAfter }, null, 2));
