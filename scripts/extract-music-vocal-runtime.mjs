// Exact-only controller migration for generated Hindi Music Vocal topic pages.
import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { externalizeMusicVocalGenerator, externalizeMusicVocalTopicRuntime, musicVocalTopicRuntime, normalizeMusicVocalGenerator } from './lib/music-vocal-runtime.mjs';
import { commitBuildWrites } from './lib/build-transaction.mjs';
import { hasMusicVocalRendererWiring } from './lib/music-vocal-renderer-wiring.mjs';

const require = createRequire(import.meta.url);
const { ROOT, siteFiles } = require('./seo-html.cjs');
const apply = process.argv.includes('--apply');
const files = siteFiles().filter(file => file.startsWith('music-vocal/') && file.endsWith('/index.html'));
const changedPages = [], writes = new Map();
let legacyPages = 0;
for (const file of files) {
  const absolute = path.join(ROOT, file);
  const before = fs.readFileSync(absolute, 'utf8');
  const after = externalizeMusicVocalTopicRuntime(before);
  if (before !== after) legacyPages++;
  if (before === after) continue;
  if ((after.match(/data-music-vocal-topic-runtime=/g) || []).length !== 1) throw new Error(`Unexpected shared runtime count: ${file}`);
  changedPages.push(file);
  writes.set(absolute, Buffer.from(after, 'utf8'));
}
const generatorPath = path.join(ROOT, 'scripts/generate_music_vocal_hi.mjs');
const generatorBefore = fs.readFileSync(generatorPath, 'utf8');
const generatorAfter = externalizeMusicVocalGenerator(generatorBefore);
if (normalizeMusicVocalGenerator(generatorBefore) !== normalizeMusicVocalGenerator(generatorAfter)) {
  throw new Error('Music Vocal generator change exceeded its exact controller/import allowance.');
}
if (generatorBefore !== generatorAfter) writes.set(generatorPath, Buffer.from(generatorAfter, 'utf8'));
if (legacyPages && legacyPages !== 201) throw new Error(`Expected exactly 201 legacy Music Vocal runtimes; found ${legacyPages}`);
if ((generatorAfter.match(/\$\{musicVocalTopicScript\}/g) || []).length !== 1 && !hasMusicVocalRendererWiring(generatorAfter.replace(/\r\n/g, '\n'))) throw new Error('Expected exactly one shared controller interpolation or maintained renderer wiring in Music Vocal generator.');
if (apply) commitBuildWrites(writes);
console.log(JSON.stringify({ mode: apply ? 'apply' : 'dry-run', controllerBytes: Buffer.byteLength(musicVocalTopicRuntime), scannedPages: files.length, legacyPages, changedPages: changedPages.length, generatorChanged: generatorBefore !== generatorAfter }, null, 2));
