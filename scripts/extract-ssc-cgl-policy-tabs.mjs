import crypto from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { commitBuildWrites } from './lib/build-transaction.mjs';
import { externalizeSscCglPolicyTabs, sscCglPolicyTabsRuntime } from './lib/ssc-cgl-policy-tabs.mjs';

const require = createRequire(import.meta.url);
const { ROOT, siteFiles } = require('./seo-html.cjs');
const apply = process.argv.includes('--apply');
const pages = siteFiles().filter(file => file.startsWith('ssc-cgl/general-awareness/general-policy-polity/') && file.endsWith('/index.html'));
const writes = new Map();
let inlinePages = 0, sharedPages = 0, replacements = 0, runtimeSource = '';

for (const file of pages) {
  const absolute = path.join(ROOT, file);
  const before = fs.readFileSync(absolute, 'utf8');
  const inline = [...before.matchAll(/<script\b([^>]*)>([\s\S]*?)<\/script>/gi)]
    .filter(match => !/\bsrc\s*=/i.test(match[1]))
    .filter(match => crypto.createHash('sha256').update(match[2].trim()).digest('hex') === sscCglPolicyTabsRuntime.sha256);
  const references = (before.match(new RegExp(sscCglPolicyTabsRuntime.attribute, 'g')) || []).length;
  if (inline.length > 1 || references > 1 || (inline.length && references)) {
    throw new Error(`Duplicate or mixed SSC-CGL policy tab runtime in ${file}.`);
  }
  if (inline.length) {
    inlinePages++;
    const source = inline[0][2].trim();
    if (runtimeSource && source !== runtimeSource) throw new Error(`Policy tab runtime variants differ in ${file}.`);
    runtimeSource = source;
  }
  if (references) sharedPages++;
  const after = externalizeSscCglPolicyTabs(before);
  if (after !== before) {
    replacements++;
    writes.set(absolute, Buffer.from(after, 'utf8'));
  }
}

if (!((inlinePages === 18 && sharedPages === 0) || (inlinePages === 0 && sharedPages === 18))) {
  throw new Error(`Unexpected SSC-CGL policy tab coverage: ${pages.length} pages, ${inlinePages} inline, ${sharedPages} shared.`);
}
if (![0, 18].includes(replacements)) throw new Error(`Expected 0 or 18 exact replacements; found ${replacements}.`);

const assetPath = path.join(ROOT, sscCglPolicyTabsRuntime.asset.slice(1));
if (!runtimeSource && fs.existsSync(assetPath)) runtimeSource = fs.readFileSync(assetPath, 'utf8').trim();
if (!runtimeSource) throw new Error('Canonical SSC-CGL policy tab runtime and asset are missing.');
const actual = { bytes: Buffer.byteLength(runtimeSource), sha256: crypto.createHash('sha256').update(runtimeSource).digest('hex') };
if (actual.bytes !== sscCglPolicyTabsRuntime.bytes || actual.sha256 !== sscCglPolicyTabsRuntime.sha256) {
  throw new Error(`Unexpected policy tab runtime fingerprint: ${JSON.stringify(actual)}`);
}
const asset = `${runtimeSource}\n`;
if (fs.existsSync(assetPath)) {
  if (fs.readFileSync(assetPath, 'utf8') !== asset) throw new Error('Existing policy tab runtime asset differs from the exact source.');
} else writes.set(assetPath, Buffer.from(asset, 'utf8'));

if (apply) commitBuildWrites(writes);
console.log(JSON.stringify({ mode: apply ? 'apply' : 'dry-run', scannedPages: pages.length, exactReplacements: replacements, inlinePages, sharedPages, asset: 'assets/js/ssc-cgl-policy-tabs.js', writes: writes.size }, null, 2));
