import test from 'node:test';
import assert from 'node:assert/strict';
import crypto from 'node:crypto';
import { externalizeMusicVocalGenerator, externalizeMusicVocalTopicRuntime, hydrateMusicVocalTopicRuntime, musicVocalTopicRuntime, musicVocalTopicScript, normalizeMusicVocalGenerator } from './lib/music-vocal-runtime.mjs';

const expected = '26d8db13a02c69d92cd43f052385bb14179cbc99ff348c46d37b59b1cf226125';

test('Music Vocal runtime is fingerprinted and exact extraction round-trips', () => {
  assert.equal(Buffer.byteLength(musicVocalTopicRuntime), 3790);
  assert.equal(crypto.createHash('sha256').update(musicVocalTopicRuntime).digest('hex'), expected);
  const source = `<head><title>संगीत</title></head><body><p>अध्याय</p><script>${musicVocalTopicRuntime}</script><footer>अंत</footer></body>`;
  const external = externalizeMusicVocalTopicRuntime(source);
  assert.equal((external.match(/data-music-vocal-topic-runtime=/g) || []).length, 1);
  assert.ok(external.indexOf('<p>अध्याय</p>') < external.indexOf(musicVocalTopicScript));
  assert.ok(external.indexOf(musicVocalTopicScript) < external.indexOf('<footer>'));
  assert.equal(externalizeMusicVocalTopicRuntime(external), external);
  assert.equal(hydrateMusicVocalTopicRuntime(external), source);
  assert.equal(hydrateMusicVocalTopicRuntime(external.replace('.js"', '.min.js"')), source);
});

test('Music Vocal generator externalization changes only its owned controller and import', () => {
  const source = `import { jsonrepair } from 'jsonrepair';\nconst prompt = 'preserve content prompt';\nconst html = \`<script>${musicVocalTopicRuntime}</script>\`;`;
  const after = externalizeMusicVocalGenerator(source);
  assert.equal(normalizeMusicVocalGenerator(source), normalizeMusicVocalGenerator(after));
  assert.ok(after.includes("import { musicVocalTopicScript } from './lib/music-vocal-runtime.mjs';"));
  assert.ok(after.includes('${musicVocalTopicScript}'));
  assert.ok(after.includes("const prompt = 'preserve content prompt';"));
  assert.equal(externalizeMusicVocalGenerator(after), after);
});

test('Music Vocal extraction leaves attributed and edited script variants untouched', () => {
  assert.equal(externalizeMusicVocalTopicRuntime(`<script defer>${musicVocalTopicRuntime}</script>`), `<script defer>${musicVocalTopicRuntime}</script>`);
  assert.equal(externalizeMusicVocalTopicRuntime(`<script>${musicVocalTopicRuntime}\n// local variant</script>`), `<script>${musicVocalTopicRuntime}\n// local variant</script>`);
});
