import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import crypto from 'node:crypto';
import { execFileSync } from 'node:child_process';
import { externalizeMusicVocalStyles, hydrateMusicVocalStyles, externalizeMusicVocalStyleGenerator, musicVocalTopicCss, musicVocalTopicStyleLink } from './lib/music-vocal-styles.mjs';

test('Music Vocal style is the frozen source and extraction preserves cascade and variants', () => {
  assert.equal(Buffer.byteLength(musicVocalTopicCss), 3104);
  assert.equal(crypto.createHash('sha256').update(musicVocalTopicCss).digest('hex'), '3cd6b57667f17ee0865df79252dee6fdf4d52e08868cd6180a9b06a5f7699a9b');
  const html = `<head><style>${musicVocalTopicCss}</style><style>.later{color:red}</style></head><main>Notes and questions</main>`;
  const expected = `<head>${musicVocalTopicStyleLink}<style>.later{color:red}</style></head><main>Notes and questions</main>`;
  assert.equal(externalizeMusicVocalStyles(html), expected);
  assert.equal(externalizeMusicVocalStyles(expected), expected);
  const variant = `<style>${musicVocalTopicCss}.edited{}</style>`;
  assert.equal(externalizeMusicVocalStyles(variant), variant);
  assert.equal(hydrateMusicVocalStyles(musicVocalTopicStyleLink.replace('.css', '.min.css?v=abc')), `<style>${musicVocalTopicCss}</style>`);
});

test('Music Vocal generator differs from its checkpoint only by the style reference and import', () => {
  const original = execFileSync('git', ['show', '5d341a929ac7484c0c9c6e84486dab4e33a95995:scripts/generate_music_vocal_hi.mjs'], { encoding: 'utf8' });
  const current = fs.readFileSync(new URL('./generate_music_vocal_hi.mjs', import.meta.url), 'utf8');
  const normalize = source => source.replace(/\r\n/g, '\n');
  assert.equal(normalize(current), normalize(externalizeMusicVocalStyleGenerator(original)));
  assert.equal(externalizeMusicVocalStyleGenerator(current), current);
});
