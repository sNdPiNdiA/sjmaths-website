import test from 'node:test';
import assert from 'node:assert/strict';
import crypto from 'node:crypto';
import { asoTopicRuntimes, externalizeAsoTopicRuntimes, hydrateAsoTopicRuntimes } from './lib/aso-topic-runtime.mjs';

test('ASO topic runtime extraction is exact, ordered, and idempotent', () => {
  const legacyIds = ['universal-quiz-feedback', 'universal-tab-engine'];
  const html = '<head></head><body><script>before()</script>' + asoTopicRuntimes.map((runtime, index) => `<script id="${legacyIds[index]}">${runtime.source}</script>`).join('') + '<script>after()</script></body>';
  const external = externalizeAsoTopicRuntimes(html);
  assert.equal((external.match(/data-aso-topic-runtime=/g) || []).length, 2);
  assert.ok(external.indexOf('before()') < external.indexOf('aso-topic-feedback.js'));
  assert.ok(external.indexOf('aso-topic-feedback.js') < external.indexOf('aso-topic-tabs.js'));
  assert.ok(external.indexOf('aso-topic-tabs.js') < external.indexOf('after()'));
  assert.equal(externalizeAsoTopicRuntimes(external), external);
  const hydrated = hydrateAsoTopicRuntimes(external);
  assert.ok(hydrated.indexOf('before()') < hydrated.indexOf(asoTopicRuntimes[0].source));
  assert.ok(hydrated.indexOf(asoTopicRuntimes[0].source) < hydrated.indexOf(asoTopicRuntimes[1].source));
  assert.ok(hydrated.indexOf(asoTopicRuntimes[1].source) < hydrated.indexOf('after()'));
  const hydratedMin = hydrateAsoTopicRuntimes(external.replaceAll('.js"', '.min.js"'));
  assert.ok(hydratedMin.includes(asoTopicRuntimes[0].source));
  assert.ok(hydratedMin.includes(asoTopicRuntimes[1].source));
  for (const [runtime, expected] of asoTopicRuntimes.map((entry, index) => [entry, [
    ['f9bc9daa8e6bae4f484dca929ecdaaa0077de88034c60be6bd7e33bdd91c5511', 13134],
    ['a3294b7f42bb498bc33bf30cde89c7561720e73100215c32975ed242e7fa2a4f', 5611],
  ][index]])) {
    assert.equal(Buffer.byteLength(runtime.source), expected[1]);
    assert.equal(crypto.createHash('sha256').update(runtime.source).digest('hex'), expected[0]);
  }
});

test('ASO runtime extraction leaves variants and attributed scripts untouched', () => {
  const variant = '<script id="universal-tab-engine" defer>different()</script>';
  const module = '<script type="module">different()</script>';
  assert.equal(externalizeAsoTopicRuntimes(variant + module), variant + module);
});
