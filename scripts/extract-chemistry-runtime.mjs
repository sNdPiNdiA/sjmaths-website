import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { externalizeChemistryRuntime, chemistryEnglishScript, chemistryBilingualScript } from './lib/chemistry-runtime.mjs';
import { commitBuildWrites } from './lib/build-transaction.mjs';
const require = createRequire(import.meta.url);
const { ROOT, siteFiles } = require('./seo-html.cjs');
const apply = process.argv.includes('--apply');
const changes = [], writes = new Map();
const modes = { english: 0, bilingual: 0 }, englishFiles = [];
for (const file of siteFiles().filter(file => file.startsWith('chemistry/') && file.endsWith('.html'))) {
  const absolute = path.join(ROOT, file);
  const before = fs.readFileSync(absolute, 'utf8');
  const after = externalizeChemistryRuntime(before);
  if (before === after) continue;
  if (after.split('data-chemistry-runtime=').length - before.split('data-chemistry-runtime=').length !== 1) throw new Error(`Ambiguous runtime: ${file}`);
  if (after.includes(chemistryEnglishScript)) { modes.english++; englishFiles.push(file); }
  else if (after.includes(chemistryBilingualScript)) modes.bilingual++;
  else throw new Error(`Missing owned runtime: ${file}`);
  changes.push(file); writes.set(absolute, Buffer.from(after, 'utf8'));
}
if (apply) commitBuildWrites(writes);
console.log(JSON.stringify({ mode: apply ? 'apply' : 'dry-run', changed: changes.length, modes, englishFiles, files: changes }, null, 2));
