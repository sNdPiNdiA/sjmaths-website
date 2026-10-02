import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { createRequire } from 'node:module';
import { commitBuildWrites } from './lib/build-transaction.mjs';
import { externalizeMusicVocalStyles, externalizeMusicVocalStyleGenerator, musicVocalTopicCss } from './lib/music-vocal-styles.mjs';

const require = createRequire(import.meta.url);
const { ROOT, siteFiles } = require('./seo-html.cjs');
const apply = process.argv.includes('--apply');
const hash = crypto.createHash('sha256').update(musicVocalTopicCss).digest('hex');
if (Buffer.byteLength(musicVocalTopicCss) !== 3104 || hash !== '3cd6b57667f17ee0865df79252dee6fdf4d52e08868cd6180a9b06a5f7699a9b') {
  throw new Error('Music Vocal stylesheet differs from the audited source.');
}
const pages = siteFiles().filter(file => file.startsWith('music-vocal/') && file.endsWith('/index.html'));
if (pages.length !== 201) throw new Error(`Expected 201 Music Vocal pages, found ${pages.length}.`);
const writes = new Map();
let changedPages = 0;
for (const file of pages) {
  const absolute = path.join(ROOT, file);
  const before = fs.readFileSync(absolute, 'utf8');
  const after = externalizeMusicVocalStyles(before);
  if ((after.match(/data-music-vocal-topic-style="topic"/g) || []).length !== 1) throw new Error(`Expected one shared style in ${file}.`);
  if (after !== before) { writes.set(absolute, Buffer.from(after)); changedPages++; }
}
if (![0, 201].includes(changedPages)) throw new Error(`Expected 0 or 201 exact replacements, found ${changedPages}.`);
const generatorPath = path.join(ROOT, 'scripts/generate_music_vocal_hi.mjs');
const generator = fs.readFileSync(generatorPath, 'utf8');
const externalGenerator = externalizeMusicVocalStyleGenerator(generator);
if (externalGenerator !== generator) writes.set(generatorPath, Buffer.from(externalGenerator));
if (apply) commitBuildWrites(writes);
console.log(JSON.stringify({ mode: apply ? 'apply' : 'dry-run', pages: pages.length, changedPages, generatorChanged: externalGenerator !== generator, writes: writes.size }, null, 2));
