import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import crypto from 'node:crypto';
import {
  assertSanskritRuntimeTemplate,
  externalizeSanskritTopicRuntime,
  hydrateSanskritTopicRuntime,
  sanskritTopicRuntimeTag,
} from './lib/sanskrit-topic-runtime.mjs';

const runtime = fs.readFileSync(new URL('../assets/js/sanskrit-topic.js', import.meta.url), 'utf8').trim();
const digest = value => crypto.createHash('sha256').update(value).digest('hex');

test('Sanskrit runtime equals the audited 26-page generator source', () => {
  assert.equal(Buffer.byteLength(runtime), 8239);
  assert.equal(digest(runtime), '1cec37eeb9e9a33c2e67e99e5bca320d43e5d5585c84f5266a5973d778e222e4');
  const generator = fs.readFileSync(new URL('./generate_sanskrit.mjs', import.meta.url), 'utf8');
  assert.doesNotThrow(() => assertSanskritRuntimeTemplate(generator));
  assert.throws(() => assertSanskritRuntimeTemplate(generator.replace('const quizOptionBtns', 'const removedQuizOptionBtns')), /no longer contains/);
});

test('exact extraction preserves controller position and unrelated scripts', () => {
  const html = `<head><script type="application/ld+json">{"@type":"Thing"}</script></head><body><main>Notes and PYQs</main><script>\n${runtime}\n</script></body>`;
  const expected = `<head><script type="application/ld+json">{"@type":"Thing"}</script></head><body><main>Notes and PYQs</main>${sanskritTopicRuntimeTag}</body>`;
  const external = externalizeSanskritTopicRuntime(html, runtime, { strict: true });
  assert.equal(external, expected);
  assert.equal(externalizeSanskritTopicRuntime(external, runtime), external);
  assert.throws(() => externalizeSanskritTopicRuntime('<script>changed()</script>', runtime, { strict: true }), /found 0/);
});

test('hydration recognizes the staged minified and cache-busted runtime reference', () => {
  const html = sanskritTopicRuntimeTag.replace('sanskrit-topic.js', 'sanskrit-topic.min.js?v=abc');
  assert.equal(hydrateSanskritTopicRuntime(html), `<script>${runtime}</script>`);
});
