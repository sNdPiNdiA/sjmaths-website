import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { createRequire } from 'node:module';
import { commitBuildWrites } from './lib/build-transaction.mjs';

const require = createRequire(import.meta.url);
const { ROOT, siteFiles } = require('./seo-html.cjs');
const apply = process.argv.includes('--apply');
const expected = { bytes: 10169, sha256: '21aaa88b15d81fffda23da5d03c80fc7312166c522dfd00f48efb8bc3509d27d' };
const styleLink = '<link rel="stylesheet" href="/assets/css/sociology-bilingual-topic.css" data-sociology-bilingual-style="shared">';
const fingerprint = source => ({ bytes: Buffer.byteLength(source), sha256: crypto.createHash('sha256').update(source).digest('hex') });
const normalize = source => source.replace(/\r\n/g, '\n').trim();
const externalize = (html, style) => html.replace(/<style>([\s\S]*?)<\/style>/gi, (tag, source) => normalize(source) === style ? styleLink : tag);
const pages = siteFiles().filter(file => file.startsWith('up-pgt-sociology/') && file.endsWith('/index.html'));
const assetPath = path.join(ROOT, 'assets/css/sociology-bilingual-topic.css');
const sourcePage = pages.find(file => fs.existsSync(path.join(ROOT, file)) && /<style>[\s\S]*?<\/style>/i.test(fs.readFileSync(path.join(ROOT, file), 'utf8')));
const sampleHtml = sourcePage ? fs.readFileSync(path.join(ROOT, sourcePage), 'utf8') : '';
const sampleStyle = sampleHtml.match(/<style>([\s\S]*?)<\/style>/i)?.[1]?.trim();
const style = sampleStyle && fingerprint(sampleStyle).sha256 === expected.sha256
  ? sampleStyle
  : fs.existsSync(assetPath) ? fs.readFileSync(assetPath, 'utf8').trim() : '';
if (!style || JSON.stringify(fingerprint(style)) !== JSON.stringify(expected)) {
  throw new Error(`Unexpected Sociology bilingual stylesheet: ${JSON.stringify(fingerprint(style))}`);
}

const writes = new Map();
const changedPages = [];
for (const file of pages) {
  const absolute = path.join(ROOT, file);
  const before = fs.readFileSync(absolute, 'utf8');
  const inlineCount = [...before.matchAll(/<style>([\s\S]*?)<\/style>/gi)].filter(match => match[1].trim() === style).length;
  const referenceCount = (before.match(/data-sociology-bilingual-style="shared"/g) || []).length;
  if (inlineCount + referenceCount === 0) continue;
  if (inlineCount + referenceCount !== 1) throw new Error(`Partial or duplicate shared stylesheet in ${file}.`);
  const after = externalize(before, style);
  if ((after.match(/data-sociology-bilingual-style="shared"/g) || []).length !== 1) {
    throw new Error(`Expected one shared stylesheet reference in ${file}.`);
  }
  if (before !== after) {
    changedPages.push(file);
    writes.set(absolute, Buffer.from(after, 'utf8'));
  }
}
if (![0, 88].includes(changedPages.length)) throw new Error(`Expected 0 or 88 exact page replacements; found ${changedPages.length}.`);
const existingAsset = fs.existsSync(assetPath) ? fs.readFileSync(assetPath, 'utf8').trim() : null;
if (existingAsset !== null && existingAsset !== style) throw new Error('Existing Sociology bilingual CSS asset differs from the audited source.');
if (existingAsset === null) writes.set(assetPath, Buffer.from(`${style}\n`, 'utf8'));

if (apply) commitBuildWrites(writes);
console.log(JSON.stringify({ mode: apply ? 'apply' : 'dry-run', scannedPages: pages.length, changedPages: changedPages.length, untouchedPages: pages.length - changedPages.length, writes: writes.size }, null, 2));
