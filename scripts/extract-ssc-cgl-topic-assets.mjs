import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { createRequire } from 'node:module';
import { commitBuildWrites } from './lib/build-transaction.mjs';
import { externalizeSscCglTopicAssets } from './lib/ssc-cgl-topic-assets.mjs';

const require = createRequire(import.meta.url);
const { ROOT, siteFiles } = require('./seo-html.cjs');
const apply = process.argv.includes('--apply');
const sample = 'ssc-cgl/computer-knowledge/backup-devices/index.html';
const expected = {
  style: { bytes: 6082, sha256: 'd39350137fcac64dc47c7464d4d16c99a53c92844b702cec96e211bc75e95fc2' },
  runtime: { bytes: 1784, sha256: '17dbf59ea9a0a18e4c4f49f87c1d30bb71bb1cdc6f41368d9b7bbe27c6814360' },
};
const fingerprint = source => ({ bytes: Buffer.byteLength(source), sha256: crypto.createHash('sha256').update(source).digest('hex') });
const sampleHtml = fs.readFileSync(path.join(ROOT, sample), 'utf8');
const styleMatch = sampleHtml.match(/<style>([\s\S]*?)<\/style>/i);
const scriptMatches = [...sampleHtml.matchAll(/<script>([\s\S]*?)<\/script>/gi)];
const styleAsset = path.join(ROOT, 'assets/css/ssc-cgl-topic.css');
const runtimeAsset = path.join(ROOT, 'assets/js/ssc-cgl-topic.js');
const style = (styleMatch?.[1] ?? (fs.existsSync(styleAsset) ? fs.readFileSync(styleAsset, 'utf8') : '')).trim();
const runtime = scriptMatches.map(match => match[1].trim()).find(source => fingerprint(source).sha256 === expected.runtime.sha256)
  || (fs.existsSync(runtimeAsset) ? fs.readFileSync(runtimeAsset, 'utf8').trim() : '');
if (!style || !runtime) throw new Error('Canonical SSC-CGL page is missing its exact shared style or runtime.');
for (const [name, source] of [['style', style], ['runtime', runtime]]) {
  const actual = fingerprint(source);
  if (actual.bytes !== expected[name].bytes || actual.sha256 !== expected[name].sha256) {
    throw new Error(`Unexpected SSC-CGL ${name} fingerprint: ${JSON.stringify(actual)}`);
  }
}

const pages = siteFiles().filter(file => file.startsWith('ssc-cgl/') && file.endsWith('/index.html'));
const writes = new Map();
const changedPages = [];
for (const file of pages) {
  const absolute = path.join(ROOT, file);
  const before = fs.readFileSync(absolute, 'utf8');
  const inlineStyleCount = [...before.matchAll(/<style>([\s\S]*?)<\/style>/gi)].filter(match => match[1].trim() === style).length;
  const inlineRuntimeCount = [...before.matchAll(/<script>([\s\S]*?)<\/script>/gi)].filter(match => match[1].trim() === runtime).length;
  const styleRefCount = (before.match(/data-ssc-cgl-topic-style="shared"/g) || []).length;
  const runtimeRefCount = (before.match(/data-ssc-cgl-topic-runtime="shared"/g) || []).length;
  if (inlineStyleCount + styleRefCount === 0 && inlineRuntimeCount + runtimeRefCount === 0) continue;
  if (inlineStyleCount + styleRefCount !== 1 || inlineRuntimeCount + runtimeRefCount !== 1) {
    throw new Error(`Partial or duplicate shared asset implementation in ${file}.`);
  }
  const after = externalizeSscCglTopicAssets(before, style, runtime);
  if ((after.match(/data-ssc-cgl-topic-style="shared"/g) || []).length !== 1
    || (after.match(/data-ssc-cgl-topic-runtime="shared"/g) || []).length !== 1) {
    throw new Error(`Expected exactly one shared CSS and JS reference in ${file}.`);
  }
  if (before !== after) {
    changedPages.push(file);
    writes.set(absolute, Buffer.from(after, 'utf8'));
  }
}
if (![0, 152].includes(changedPages.length)) throw new Error(`Expected 0 or 152 exact page replacements; found ${changedPages.length}.`);

for (const [relative, content] of [
  ['assets/css/ssc-cgl-topic.css', `${style}\n`],
  ['assets/js/ssc-cgl-topic.js', `${runtime}\n`],
]) {
  const absolute = path.join(ROOT, relative);
  if (fs.existsSync(absolute)) {
    if (fs.readFileSync(absolute, 'utf8').trim() !== content.trim()) throw new Error(`Existing asset differs: ${relative}`);
  } else writes.set(absolute, Buffer.from(content, 'utf8'));
}

if (apply) commitBuildWrites(writes);
console.log(JSON.stringify({ mode: apply ? 'apply' : 'dry-run', scannedPages: pages.length, changedPages: changedPages.length, untouchedPages: pages.length - changedPages.length, writes: writes.size }, null, 2));
