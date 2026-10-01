import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { createRequire } from 'node:module';
import { commitBuildWrites } from './lib/build-transaction.mjs';
import { externalizePsychologyBilingualStyle } from './lib/psychology-bilingual-styles.mjs';

const require = createRequire(import.meta.url);
const { ROOT, siteFiles } = require('./seo-html.cjs');
const apply = process.argv.includes('--apply');
const expected = { bytes: 10178, sha256: '700421ecbef32deb9256767a15389557b8e27340f79c50e3d8f10555c6b21ad2' };
const fingerprint = source => ({ bytes: Buffer.byteLength(source), sha256: crypto.createHash('sha256').update(source).digest('hex') });
const pages = siteFiles().filter(file => file.startsWith('psychology/') && file.endsWith('/index.html'));
const assetPath = path.join(ROOT, 'assets/css/psychology-bilingual-topic.css');
const sourcePage = pages.find(file => fs.existsSync(path.join(ROOT, file)));
const sampleHtml = fs.readFileSync(path.join(ROOT, sourcePage), 'utf8');
const sampleStyle = sampleHtml.match(/<style>([\s\S]*?)<\/style>/i)?.[1]?.trim();
const style = sampleStyle && fingerprint(sampleStyle).sha256 === expected.sha256
  ? sampleStyle
  : fs.existsSync(assetPath) ? fs.readFileSync(assetPath, 'utf8').trim() : '';
if (!style || JSON.stringify(fingerprint(style)) !== JSON.stringify(expected)) {
  throw new Error(`Unexpected Psychology bilingual stylesheet: ${JSON.stringify(fingerprint(style))}`);
}

const writes = new Map();
const changedPages = [];
for (const file of pages) {
  const absolute = path.join(ROOT, file);
  const before = fs.readFileSync(absolute, 'utf8');
  const inlineCount = [...before.matchAll(/<style>([\s\S]*?)<\/style>/gi)].filter(match => match[1].trim() === style).length;
  const referenceCount = (before.match(/data-psychology-bilingual-style="shared"/g) || []).length;
  if (inlineCount + referenceCount === 0) continue;
  if (inlineCount + referenceCount !== 1) throw new Error(`Partial or duplicate shared stylesheet in ${file}.`);
  const after = externalizePsychologyBilingualStyle(before, style);
  if ((after.match(/data-psychology-bilingual-style="shared"/g) || []).length !== 1) {
    throw new Error(`Expected one shared stylesheet reference in ${file}.`);
  }
  if (before !== after) {
    changedPages.push(file);
    writes.set(absolute, Buffer.from(after, 'utf8'));
  }
}
if (![0, 200].includes(changedPages.length)) throw new Error(`Expected 0 or 200 exact page replacements; found ${changedPages.length}.`);
const existingAsset = fs.existsSync(assetPath) ? fs.readFileSync(assetPath, 'utf8').trim() : null;
if (existingAsset !== null && existingAsset !== style) throw new Error('Existing Psychology bilingual CSS asset differs from the audited source.');
if (existingAsset === null) writes.set(assetPath, Buffer.from(`${style}\n`, 'utf8'));

if (apply) commitBuildWrites(writes);
console.log(JSON.stringify({ mode: apply ? 'apply' : 'dry-run', scannedPages: pages.length, changedPages: changedPages.length, untouchedPages: pages.length - changedPages.length, writes: writes.size }, null, 2));
