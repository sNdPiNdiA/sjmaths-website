import test from 'node:test';
import assert from 'node:assert/strict';
import crypto from 'node:crypto';
import { externalizeHindiGenerator, externalizeHindiTopicRuntime, hindiTopicRuntime, hindiTopicScript, hydrateHindiTopicRuntime, normalizeHindiGenerator } from './lib/hindi-topic-runtime.mjs';

const expected = 'cf45d429afa1506bd6f27fe0f0057531ea2c6bba67e780446ebcfdfc41c56d49';

test('Hindi topic runtime is fingerprinted and exact extraction round-trips', () => {
  assert.equal(Buffer.byteLength(hindiTopicRuntime), 8210);
  assert.equal(crypto.createHash('sha256').update(hindiTopicRuntime).digest('hex'), expected);
  const source = `<head><title>हिन्दी</title></head><body><p>अनुच्छेद</p><script>${hindiTopicRuntime}</script><footer>अंत</footer></body>`;
  const external = externalizeHindiTopicRuntime(source);
  assert.equal((external.match(/data-hindi-topic-runtime=/g) || []).length, 1);
  assert.ok(external.indexOf('<p>अनुच्छेद</p>') < external.indexOf(hindiTopicScript));
  assert.ok(external.indexOf(hindiTopicScript) < external.indexOf('<footer>'));
  assert.equal(externalizeHindiTopicRuntime(external), external);
  assert.equal(hydrateHindiTopicRuntime(external), source);
  assert.equal(hydrateHindiTopicRuntime(external.replace('.js"', '.min.js"')), source);
});

test('Hindi generator externalization changes only its owned runtime and import', () => {
  const source = `import { jsonrepair } from 'jsonrepair';\nconst prompt = 'keep prompt byte-for-byte';\nconst html = \`<script>${hindiTopicRuntime}</script>\`;`;
  const after = externalizeHindiGenerator(source);
  assert.equal(normalizeHindiGenerator(source), normalizeHindiGenerator(after));
  assert.ok(after.includes("import { hindiTopicScript } from './lib/hindi-topic-runtime.mjs';"));
  assert.ok(after.includes('${hindiTopicScript}'));
  assert.ok(after.includes("const prompt = 'keep prompt byte-for-byte';"));
  assert.equal(externalizeHindiGenerator(after), after);
});

test('Hindi runtime extraction preserves modified and attributed variants', () => {
  const variant = `<script defer>${hindiTopicRuntime}</script>`;
  const modified = `<script>${hindiTopicRuntime}\n// local variant</script>`;
  assert.equal(externalizeHindiTopicRuntime(variant + modified), variant + modified);
});
