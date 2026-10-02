import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { createRequire } from 'node:module';
import { commitBuildWrites } from './lib/build-transaction.mjs';
import { externalizeSscCglPolicyMiniTest, sscCglPolicyMiniTestRuntime } from './lib/ssc-cgl-policy-mini-test.mjs';

const require = createRequire(import.meta.url);
const { ROOT, siteFiles } = require('./seo-html.cjs');
const apply = process.argv.includes('--apply');
const pages = siteFiles().filter(file => file.startsWith('ssc-cgl/general-awareness/general-policy-polity/') && file.endsWith('/index.html'));
const writes = new Map();
let changedPages = 0;
let inlinePages = 0;
let sharedPages = 0;
let runtimeSource = '';

for (const file of pages) {
  const absolute = path.join(ROOT, file);
  const before = fs.readFileSync(absolute, 'utf8');
  const inlineMatch = [...before.matchAll(/<script\b([^>]*)>([\s\S]*?)<\/script>/gi)]
    .find(item => !/\bsrc\s*=/i.test(item[1]) && crypto.createHash('sha256').update(item[2].trim()).digest('hex') === sscCglPolicyMiniTestRuntime.sha256);
  if (inlineMatch) {
    inlinePages++;
    const source = inlineMatch[2].trim();
    if (runtimeSource && runtimeSource !== source) throw new Error(`Mini-test controller variants differ in ${file}.`);
    runtimeSource = source;
  }
  if (before.includes(sscCglPolicyMiniTestRuntime.attribute)) sharedPages++;
  const after = externalizeSscCglPolicyMiniTest(before);
  if (after !== before) {
    changedPages++;
    writes.set(absolute, Buffer.from(after, 'utf8'));
  }
}

if (!((inlinePages === 18 && sharedPages === 0) || (inlinePages === 0 && sharedPages === 18))) {
  throw new Error(`Partial or mixed mini-test migration: ${inlinePages} inline, ${sharedPages} shared.`);
}
if (![0, 18].includes(changedPages)) throw new Error(`Expected 0 or 18 exact replacements; found ${changedPages}.`);

const assetPath = path.join(ROOT, 'assets/js/ssc-cgl-policy-mini-test.js');
if (!runtimeSource && fs.existsSync(assetPath)) runtimeSource = fs.readFileSync(assetPath, 'utf8').trim();
if (!runtimeSource) throw new Error('Canonical SSC-CGL mini-test source and asset are missing.');
const actual = { bytes: Buffer.byteLength(runtimeSource), sha256: crypto.createHash('sha256').update(runtimeSource).digest('hex') };
if (actual.bytes !== sscCglPolicyMiniTestRuntime.bytes || actual.sha256 !== sscCglPolicyMiniTestRuntime.sha256) {
  throw new Error(`Unexpected mini-test runtime fingerprint: ${JSON.stringify(actual)}`);
}
const asset = `${runtimeSource}\n`;
if (fs.existsSync(assetPath)) {
  if (fs.readFileSync(assetPath, 'utf8') !== asset) throw new Error('Existing policy mini-test asset differs from the exact source.');
} else writes.set(assetPath, Buffer.from(asset, 'utf8'));

if (apply) commitBuildWrites(writes);
console.log(JSON.stringify({ mode: apply ? 'apply' : 'dry-run', scannedPages: pages.length, exactReplacements: changedPages, inlinePages, sharedPages, asset: 'assets/js/ssc-cgl-policy-mini-test.js', writes: writes.size }, null, 2));

