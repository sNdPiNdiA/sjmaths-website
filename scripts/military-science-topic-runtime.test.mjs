import test from 'node:test';
import assert from 'node:assert/strict';
import crypto from 'node:crypto';
import { externalizeMilitaryScienceGenerator, externalizeMilitaryScienceTopicRuntime, hydrateMilitaryScienceTopicRuntime, militaryScienceTopicRuntime, militaryScienceTopicScript, normalizeMilitaryScienceGenerator } from './lib/military-science-runtime.mjs';

const expected = '2c869fe1be1f6c2a7480e9fbc15f7f7d7c1be3059a7ba0f5e133716b08504111';

test('Military Science runtime is fingerprinted and exact extraction round-trips', () => {
  assert.equal(Buffer.byteLength(militaryScienceTopicRuntime), 7229);
  assert.equal(crypto.createHash('sha256').update(militaryScienceTopicRuntime).digest('hex'), expected);
  assert.ok(militaryScienceTopicRuntime.includes('quiz-feedback show'));
  const source = `<head><title>Security</title></head><body><p>Concept</p><script>${militaryScienceTopicRuntime}</script><footer>End</footer></body>`;
  const external = externalizeMilitaryScienceTopicRuntime(source);
  assert.equal((external.match(/data-military-science-topic-runtime=/g) || []).length, 1);
  assert.ok(external.indexOf('<p>Concept</p>') < external.indexOf(militaryScienceTopicScript));
  assert.ok(external.indexOf(militaryScienceTopicScript) < external.indexOf('<footer>'));
  assert.equal(externalizeMilitaryScienceTopicRuntime(external), external);
  assert.equal(hydrateMilitaryScienceTopicRuntime(external), source);
  assert.equal(hydrateMilitaryScienceTopicRuntime(external.replace('.js"', '.min.js"')), source);
});

test('Military Science generator externalization changes only its owned controller and import', () => {
  const source = `import { jsonrepair } from 'jsonrepair';\nconst prompt = 'preserve syllabus and questions';\nconst html = \`<script>${militaryScienceTopicRuntime}</script>\`;`;
  const after = externalizeMilitaryScienceGenerator(source);
  assert.equal(normalizeMilitaryScienceGenerator(source), normalizeMilitaryScienceGenerator(after));
  assert.ok(after.includes("import { militaryScienceTopicScript } from './lib/military-science-runtime.mjs';"));
  assert.ok(after.includes('${militaryScienceTopicScript}'));
  assert.ok(after.includes("const prompt = 'preserve syllabus and questions';"));
  assert.equal(externalizeMilitaryScienceGenerator(after), after);
});

test('Military Science extraction leaves attributed and edited variants untouched', () => {
  assert.equal(externalizeMilitaryScienceTopicRuntime(`<script defer>${militaryScienceTopicRuntime}</script>`), `<script defer>${militaryScienceTopicRuntime}</script>`);
  assert.equal(externalizeMilitaryScienceTopicRuntime(`<script>${militaryScienceTopicRuntime}\n// local variant</script>`), `<script>${militaryScienceTopicRuntime}\n// local variant</script>`);
});
