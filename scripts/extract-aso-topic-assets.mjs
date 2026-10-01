// One-time exact extraction of the shared ASO topic-page controllers.
// This script is intentionally separate from page migration so assets are
// created only after every candidate page proves to contain the same scripts.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { createRequire } from 'node:module';
import { commitBuildWrites } from './lib/build-transaction.mjs';

const require = createRequire(import.meta.url);
const { ROOT } = require('./seo-html.cjs');
const sample = 'upsc-aso/aerodynamics-performance-stability/aeronautics-aerodynamics-mega-test/index.html';
const expected = new Map([
  ['universal-quiz-feedback', { name: 'aso-topic-feedback', bytes: 13134, sha256: 'f9bc9daa8e6bae4f484dca929ecdaaa0077de88034c60be6bd7e33bdd91c5511' }],
  ['universal-tab-engine', { name: 'aso-topic-tabs', bytes: 5611, sha256: 'a3294b7f42bb498bc33bf30cde89c7561720e73100215c32975ed242e7fa2a4f' }],
]);
const html = fs.readFileSync(path.join(ROOT, sample), 'utf8');
const scripts = new Map();
for (const match of html.matchAll(/<script\s+id="([^"]+)">([\s\S]*?)<\/script>/gi)) {
  if (!expected.has(match[1])) continue;
  const source = match[2].trim();
  const fingerprint = { bytes: Buffer.byteLength(source), sha256: crypto.createHash('sha256').update(source).digest('hex') };
  const definition = expected.get(match[1]);
  if (fingerprint.bytes !== definition.bytes || fingerprint.sha256 !== definition.sha256) {
    throw new Error(`Unexpected source fingerprint for ${match[1]}: ${JSON.stringify(fingerprint)}`);
  }
  scripts.set(match[1], source);
}
if (scripts.size !== expected.size) throw new Error(`Expected ${expected.size} shared scripts; found ${scripts.size}`);

const writes = new Map();
for (const [id, definition] of expected) {
  const target = path.join(ROOT, 'assets/js', `${definition.name}.js`);
  if (fs.existsSync(target)) {
    if (fs.readFileSync(target, 'utf8').trim() !== scripts.get(id)) throw new Error(`Existing asset differs: ${target}`);
    continue;
  }
  writes.set(target, Buffer.from(`${scripts.get(id)}\n`, 'utf8'));
}
if (!writes.size) throw new Error('Both shared ASO topic runtime assets already exist and match.');
commitBuildWrites(writes);
console.log(JSON.stringify({ extracted: [...writes.keys()].map(file => path.relative(ROOT, file)), fingerprints: Object.fromEntries([...expected].map(([id, definition]) => [id, definition])) }, null, 2));
