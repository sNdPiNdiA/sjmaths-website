// One-time exact extraction of the generated Hindi topic-page controller.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { createRequire } from 'node:module';
import { commitBuildWrites } from './lib/build-transaction.mjs';

const require = createRequire(import.meta.url);
const { ROOT, siteFiles } = require('./seo-html.cjs');
const expected = { bytes: 8210, sha256: 'cf45d429afa1506bd6f27fe0f0057531ea2c6bba67e780446ebcfdfc41c56d49' };
const scriptPattern = /<script\s*>([\s\S]*?)<\/script>/gi;
const fingerprint = source => ({
  bytes: Buffer.byteLength(source.trim()),
  sha256: crypto.createHash('sha256').update(source.trim()).digest('hex'),
});
const files = siteFiles().filter(file => file.startsWith('hindi/') && file.endsWith('.html'));
const matchingSources = [];
for (const file of files) {
  const html = fs.readFileSync(path.join(ROOT, file), 'utf8');
  for (const match of html.matchAll(scriptPattern)) {
    const source = match[1].trim();
    if (fingerprint(source).sha256 === expected.sha256) matchingSources.push({ file, source });
  }
}
const generator = fs.readFileSync(path.join(ROOT, 'scripts/generate_hindi.mjs'), 'utf8');
const generatorSources = [...generator.matchAll(scriptPattern)].map(match => match[1].trim()).filter(source => fingerprint(source).sha256 === expected.sha256);
if (generatorSources.length !== 1) throw new Error(`Expected one exact controller in Hindi generator; found ${generatorSources.length}`);
if (Buffer.byteLength(generatorSources[0]) !== expected.bytes) throw new Error('Hindi generator controller byte count changed.');

const assetPath = path.join(ROOT, 'assets/js/hindi-topic.js');
if (fs.existsSync(assetPath)) {
  const existing = fs.readFileSync(assetPath, 'utf8').trim();
  if (fingerprint(existing).sha256 !== expected.sha256 || Buffer.byteLength(existing) !== expected.bytes) throw new Error('Existing Hindi runtime asset has an unexpected fingerprint.');
  console.log(JSON.stringify({ mode: 'verify-existing', pagesWithLegacyRuntime: matchingSources.length, asset: path.relative(ROOT, assetPath) }, null, 2));
} else {
  if (matchingSources.length !== 102) throw new Error(`Expected 102 exact legacy Hindi pages; found ${matchingSources.length}`);
  if (matchingSources.some(item => item.source !== generatorSources[0])) throw new Error('A Hindi page runtime differs from the generator implementation.');
  commitBuildWrites(new Map([[assetPath, Buffer.from(`${generatorSources[0]}\n`, 'utf8')]]));
  console.log(JSON.stringify({ mode: 'extract', pages: matchingSources.length, asset: path.relative(ROOT, assetPath), fingerprint: expected }, null, 2));
}
