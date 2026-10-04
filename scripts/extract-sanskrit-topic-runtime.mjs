import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { createRequire } from 'node:module';
import { commitBuildWrites } from './lib/build-transaction.mjs';
import { externalizeSanskritTopicRuntime } from './lib/sanskrit-topic-runtime.mjs';

const require = createRequire(import.meta.url);
const { ROOT, siteFiles } = require('./seo-html.cjs');
const apply = process.argv.includes('--apply');
const expected = { bytes: 10985, sha256: 'f7104355c14439f003bc13412513d2357af53468c006a0885741f9d8068385a6' };
const fingerprint = source => ({ bytes: Buffer.byteLength(source), sha256: crypto.createHash('sha256').update(source).digest('hex') });
const generatorPath = path.join(ROOT, 'scripts/generate_sanskrit.mjs');
const generator = fs.readFileSync(generatorPath, 'utf8');
const generatedScripts = [...generator.matchAll(/<script>([\s\S]*?)<\/script>/gi)].map(match => match[1].trim());
const assetPath = path.join(ROOT, 'assets/js/sanskrit-topic.js');
const existingAsset = fs.existsSync(assetPath) ? fs.readFileSync(assetPath, 'utf8').trim() : null;
const runtime = generatedScripts.find(source => JSON.stringify(fingerprint(source)) === JSON.stringify(expected))
  || existingAsset;
if (!runtime || JSON.stringify(fingerprint(runtime)) !== JSON.stringify(expected)) {
  throw new Error(`Unexpected Sanskrit generator runtime: ${JSON.stringify(runtime ? fingerprint(runtime) : null)}`);
}

const pages = siteFiles().filter(file => file.startsWith('sanskrit/') && file.endsWith('/index.html'));
const writes = new Map();
const changedPages = [];
for (const file of pages) {
  const absolute = path.join(ROOT, file);
  const before = fs.readFileSync(absolute, 'utf8');
  const inlineCount = [...before.matchAll(/<script>([\s\S]*?)<\/script>/gi)].filter(match => match[1].trim() === runtime).length;
  const referenceCount = (before.match(/data-sanskrit-topic-runtime="shared"/g) || []).length;
  if (inlineCount + referenceCount === 0) continue;
  if (inlineCount + referenceCount !== 1) throw new Error(`Partial or duplicate Sanskrit runtime in ${file}.`);
  const after = externalizeSanskritTopicRuntime(before, runtime);
  if ((after.match(/data-sanskrit-topic-runtime="shared"/g) || []).length !== 1) {
    throw new Error(`Expected one shared Sanskrit runtime reference in ${file}.`);
  }
  if (before !== after) {
    changedPages.push(file);
    writes.set(absolute, Buffer.from(after, 'utf8'));
  }
}
if (![0, 26].includes(changedPages.length)) throw new Error(`Expected 0 or 26 exact page replacements; found ${changedPages.length}.`);
if (existingAsset !== null && existingAsset !== runtime) throw new Error('Existing Sanskrit runtime asset differs from the audited generator source.');
if (existingAsset === null) writes.set(assetPath, Buffer.from(`${runtime}\n`, 'utf8'));

if (apply) commitBuildWrites(writes);
console.log(JSON.stringify({ mode: apply ? 'apply' : 'dry-run', scannedPages: pages.length, changedPages: changedPages.length, untouchedPages: pages.length - changedPages.length, writes: writes.size }, null, 2));
