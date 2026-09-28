import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';
import { historyRuntimeScript, historyRuntimeSource, externalizeHistoryRuntime } from './lib/history-runtime.mjs';

test('extracting the exact runtime preserves data, position and parser-blocking order', () => {
  const prefix = '<script type="application/json" id="history-quiz-data">[{"question":"Original"}]</script>';
  const suffix = '<script>window.afterRuntime=true;</script></body>';
  const before = prefix + `<script id="history-runtime">${historyRuntimeSource}</script>` + suffix;
  assert.equal(externalizeHistoryRuntime(before), prefix + historyRuntimeScript + suffix);
  assert.equal(externalizeHistoryRuntime(externalizeHistoryRuntime(before)), prefix + historyRuntimeScript + suffix);
  assert.doesNotMatch(historyRuntimeScript, /\b(?:async|defer)\b/);
  new vm.Script(historyRuntimeSource);
});

test('different runtime variants and attributed scripts stay intact', () => {
  for (const before of [
    `<script id="history-runtime">${historyRuntimeSource};window.custom=true;</script>`,
    `<script id="history-runtime" nonce="nonce">${historyRuntimeSource}</script>`,
    '<script>window.custom=true;</script>',
  ]) assert.equal(externalizeHistoryRuntime(before), before);
});

test('generator references the maintained shared script rather than duplicating its code', () => {
  const generator = fs.readFileSync(new URL('./lib/history-renderer.mjs', import.meta.url), 'utf8');
  assert.match(generator, /import \{ historyRuntimeScript \} from '\.\/history-runtime\.mjs'/);
  assert.ok(generator.includes('${historyRuntimeScript}'));
  assert.ok(!generator.includes(historyRuntimeSource));
});
