import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { createRequire } from 'node:module';
import { commitBuildWrites } from './lib/build-transaction.mjs';
import { externalizeAhcRoAroLanguageRuntime, deduplicateAhcRoAroLanguageReferences, ahcRoAroLanguageRuntime } from './lib/ahc-ro-aro-language-runtime.mjs';

const require = createRequire(import.meta.url);
const { ROOT, siteFiles } = require('./seo-html.cjs');
const apply = process.argv.includes('--apply');
const deduplicate = process.argv.includes('--dedupe-references');
const pages = siteFiles().filter(file => file.startsWith('ahc-ro-aro/') && file.endsWith('/index.html'));
const writes = new Map();
let changedPages = 0, inlinePages = 0, sharedPages = 0, runtimeSource = '';
let deduplicatedPages = 0;

for (const file of pages) {
  const absolute = path.join(ROOT, file);
  const before = fs.readFileSync(absolute, 'utf8');
  const inlineMatch = [...before.matchAll(/<script\b([^>]*)>([\s\S]*?)<\/script>/gi)]
    .find(item => !/\bsrc\s*=/i.test(item[1]) && crypto.createHash('sha256').update(item[2].trim()).digest('hex') === ahcRoAroLanguageRuntime.sha256);
  if (inlineMatch) {
    inlinePages++;
    const source = inlineMatch[2].trim();
    if (runtimeSource && runtimeSource !== source) throw new Error(`Language runtime variants differ in ${file}.`);
    runtimeSource = source;
  }
  if (before.includes(ahcRoAroLanguageRuntime.attribute)) sharedPages++;
  const deduplicated = deduplicate ? deduplicateAhcRoAroLanguageReferences(before) : before;
  if (deduplicated !== before) deduplicatedPages++;
  const after = externalizeAhcRoAroLanguageRuntime(deduplicated);
  if (after !== before) {
    changedPages++;
    writes.set(absolute, Buffer.from(after, 'utf8'));
  }
}

if (!((inlinePages === 32 && sharedPages === 0) || (inlinePages === 0 && sharedPages === 32))) {
  throw new Error(`Partial or mixed language migration: ${inlinePages} inline, ${sharedPages} shared.`);
}
if (![0, 32].includes(changedPages) && !(deduplicate && inlinePages === 0 && changedPages === deduplicatedPages)) throw new Error(`Expected 0 or 32 exact replacements, or explicit reference deduplication; found ${changedPages}.`);

const assetPath = path.join(ROOT, 'assets/js/ahc-ro-aro-language.js');
if (!runtimeSource && fs.existsSync(assetPath)) runtimeSource = fs.readFileSync(assetPath, 'utf8').trim();
if (!runtimeSource) throw new Error('Canonical AHC RO/ARO language runtime and asset are missing.');
const actual = { bytes: Buffer.byteLength(runtimeSource), sha256: crypto.createHash('sha256').update(runtimeSource).digest('hex') };
if (actual.bytes !== ahcRoAroLanguageRuntime.bytes || actual.sha256 !== ahcRoAroLanguageRuntime.sha256) {
  throw new Error(`Unexpected AHC RO/ARO language fingerprint: ${JSON.stringify(actual)}`);
}
const asset = `${runtimeSource}\n`;
if (fs.existsSync(assetPath)) {
  if (fs.readFileSync(assetPath, 'utf8') !== asset) throw new Error('Existing AHC RO/ARO language asset differs from the exact source.');
} else writes.set(assetPath, Buffer.from(asset, 'utf8'));

if (apply) commitBuildWrites(writes);
console.log(JSON.stringify({ mode: apply ? 'apply' : 'dry-run', scannedPages: pages.length, exactReplacements: changedPages, deduplicatedPages, inlinePages, sharedPages, asset: 'assets/js/ahc-ro-aro-language.js', writes: writes.size }, null, 2));

