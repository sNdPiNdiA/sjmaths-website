import test from 'node:test';
import assert from 'node:assert/strict';
import crypto from 'node:crypto';
import { externalizeMusicInstrumentalGenerator, externalizeMusicInstrumentalTopicRuntime, hydrateMusicInstrumentalTopicRuntime, musicInstrumentalTopicRuntime, musicInstrumentalTopicScript, normalizeMusicInstrumentalGenerator } from './lib/music-instrumental-runtime.mjs';

const expected = '9e29b5dab0c143db9766a7f4391960ab25f1155d783fc346709b6636aecd9d3a';

test('Music Instrumental runtime is fingerprinted and exact extraction round-trips', () => {
  assert.equal(Buffer.byteLength(musicInstrumentalTopicRuntime), 7670);
  assert.equal(crypto.createHash('sha256').update(musicInstrumentalTopicRuntime).digest('hex'), expected);
  assert.ok(musicInstrumentalTopicRuntime.includes('quiz-feedback show'));
  const source = `<head><title>वाद्य संगीत</title></head><body><p>ताल</p><script>${musicInstrumentalTopicRuntime}</script><footer>समाप्त</footer></body>`;
  const external = externalizeMusicInstrumentalTopicRuntime(source);
  assert.equal((external.match(/data-music-instrumental-topic-runtime=/g) || []).length, 1);
  assert.ok(external.indexOf('<p>ताल</p>') < external.indexOf(musicInstrumentalTopicScript));
  assert.ok(external.indexOf(musicInstrumentalTopicScript) < external.indexOf('<footer>'));
  assert.equal(externalizeMusicInstrumentalTopicRuntime(external), external);
  assert.equal(hydrateMusicInstrumentalTopicRuntime(external), source);
  assert.equal(hydrateMusicInstrumentalTopicRuntime(external.replace('.js"', '.min.js"')), source);
});

test('Music Instrumental generator externalization changes only its owned controller and import', () => {
  const source = `import { jsonrepair } from 'jsonrepair';\nconst prompt = 'preserve curriculum prompt';\nconst html = \`<script>${musicInstrumentalTopicRuntime}</script>\`;`;
  const after = externalizeMusicInstrumentalGenerator(source);
  assert.equal(normalizeMusicInstrumentalGenerator(source), normalizeMusicInstrumentalGenerator(after));
  assert.ok(after.includes("import { musicInstrumentalTopicScript } from './lib/music-instrumental-runtime.mjs';"));
  assert.ok(after.includes('${musicInstrumentalTopicScript}'));
  assert.ok(after.includes("const prompt = 'preserve curriculum prompt';"));
  assert.equal(externalizeMusicInstrumentalGenerator(after), after);
});

test('Music Instrumental extraction leaves attributed and edited script variants untouched', () => {
  assert.equal(externalizeMusicInstrumentalTopicRuntime(`<script defer>${musicInstrumentalTopicRuntime}</script>`), `<script defer>${musicInstrumentalTopicRuntime}</script>`);
  assert.equal(externalizeMusicInstrumentalTopicRuntime(`<script>${musicInstrumentalTopicRuntime}\n// local variant</script>`), `<script>${musicInstrumentalTopicRuntime}\n// local variant</script>`);
});
