// Exact-only controller migration for generated Hindi Music Instrumental pages.
import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { externalizeMusicInstrumentalGenerator, externalizeMusicInstrumentalTopicRuntime, musicInstrumentalTopicRuntime, normalizeMusicInstrumentalGenerator } from './lib/music-instrumental-runtime.mjs';
import { commitBuildWrites } from './lib/build-transaction.mjs';

const require = createRequire(import.meta.url);
const { ROOT, siteFiles } = require('./seo-html.cjs');
const apply = process.argv.includes('--apply');
const files = siteFiles().filter(file => file.startsWith('music-instrumental/') && file.endsWith('/index.html'));
const changedPages = [], writes = new Map();
let legacyPages = 0;
for (const file of files) {
  const absolute = path.join(ROOT, file);
  const before = fs.readFileSync(absolute, 'utf8');
  const after = externalizeMusicInstrumentalTopicRuntime(before);
  if (before !== after) legacyPages++;
  if (before === after) continue;
  if ((after.match(/data-music-instrumental-topic-runtime=/g) || []).length !== 1) throw new Error(`Unexpected shared runtime count: ${file}`);
  changedPages.push(file);
  writes.set(absolute, Buffer.from(after, 'utf8'));
}
const generatorPath = path.join(ROOT, 'scripts/generate_music_instrumental_hi.mjs');
const generatorBefore = fs.readFileSync(generatorPath, 'utf8');
const generatorAfter = externalizeMusicInstrumentalGenerator(generatorBefore);
if (normalizeMusicInstrumentalGenerator(generatorBefore) !== normalizeMusicInstrumentalGenerator(generatorAfter)) {
  throw new Error('Music Instrumental generator change exceeded its exact controller/import allowance.');
}
if (generatorBefore !== generatorAfter) writes.set(generatorPath, Buffer.from(generatorAfter, 'utf8'));
if (legacyPages && legacyPages !== 125) throw new Error(`Expected exactly 125 legacy Music Instrumental runtimes; found ${legacyPages}`);
if ((generatorAfter.match(/\$\{musicInstrumentalTopicScript\}/g) || []).length !== 1) throw new Error('Expected exactly one shared controller interpolation in Music Instrumental generator.');
if (apply) commitBuildWrites(writes);
console.log(JSON.stringify({ mode: apply ? 'apply' : 'dry-run', controllerBytes: Buffer.byteLength(musicInstrumentalTopicRuntime), scannedPages: files.length, legacyPages, changedPages: changedPages.length, generatorChanged: generatorBefore !== generatorAfter }, null, 2));
