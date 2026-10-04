import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { commitBuildWrites } from './lib/build-transaction.mjs';
import { migrateUpUpperPrimaryThemeBootstraps } from './lib/up-upper-primary-theme-bootstrap.mjs';

const require = createRequire(import.meta.url);
const { ROOT, siteFiles } = require('./seo-html.cjs');
const apply = process.argv.includes('--apply');
const expected = { englishSanskritHead: 55, englishSanskritBody: 55, hindiHead: 34, hindiBody: 34 };
const writes = new Map();
const totals = { englishSanskritHead: 0, englishSanskritBody: 0, hindiHead: 0, hindiBody: 0 };

for (const file of siteFiles().filter(file => file.startsWith('up-upper-primary-teacher/') && file.endsWith('.html'))) {
    const absolute = path.join(ROOT, file);
    const before = fs.readFileSync(absolute, 'utf8');
    const result = migrateUpUpperPrimaryThemeBootstraps(before);
    for (const key of Object.keys(totals)) totals[key] += result.counts[key];
    if (before !== result.html) writes.set(absolute, Buffer.from(result.html, 'utf8'));
}

for (const [key, count] of Object.entries(expected)) {
    if (totals[key] !== count) throw new Error(`Expected ${count} ${key} bootstraps, found ${totals[key]}.`);
}
if (writes.size !== 89) throw new Error(`Expected exactly 89 UP Upper Primary pages to update, found ${writes.size}.`);
if (apply) commitBuildWrites(writes);
console.log(JSON.stringify({ mode: apply ? 'apply' : 'dry-run', updatedPages: writes.size, replacements: totals }, null, 2));
