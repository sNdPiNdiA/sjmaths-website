import test from 'node:test';
import assert from 'node:assert/strict';
import {
  extractUpAssistantDuplicateRuntime,
  removeUpAssistantDuplicateRuntime,
} from './lib/up-assistant-renderer-dedupe.mjs';
import { execFileSync } from 'node:child_process';
import { ROOT } from './seo-html.cjs';

const sample = 'up-assistant-teacher/child-psychology/creating-conducive-learning-environment/index.html';
const baselineHtml = execFileSync('git', ['show', `237db669da5fca0a8ff8ae6a5a601d284a367642:${sample}`], { cwd: ROOT, encoding: 'utf8', maxBuffer: 20e6 });
const runtime = extractUpAssistantDuplicateRuntime(baselineHtml);

test('baseline duplicate is fingerprinted and contains only legacy tab-panel handling', () => {
  assert.equal(Buffer.byteLength(runtime), 1031);
  assert.match(runtime, /tabPanels\.forEach/);
  assert.match(runtime, /aria-selected/);
});

test('removes only the exact inline or tagged external duplicate', () => {
  const inline = `<head><script type="application/ld+json">{"@type":"Thing"}</script></head><main>Notes</main><script>\n${runtime}\n</script><script defer>keep()</script>`;
  const inlineExpected = `<head><script type="application/ld+json">{"@type":"Thing"}</script></head><main>Notes</main><script defer>keep()</script>`;
  assert.equal(removeUpAssistantDuplicateRuntime(inline, runtime, { strict: true }), inlineExpected);

  const external = '<main>Notes</main><script src="/assets/js/up-assistant-tabs.js" data-up-assistant-tabs-runtime="shared"></script><script defer>keep()</script>';
  assert.equal(removeUpAssistantDuplicateRuntime(external, runtime, { strict: true }), '<main>Notes</main><script defer>keep()</script>');
  assert.equal(removeUpAssistantDuplicateRuntime(inlineExpected, runtime), inlineExpected, 'repeat is idempotent');
  assert.throws(() => removeUpAssistantDuplicateRuntime('<script>changed()</script>', runtime, { strict: true }), /found 0/);
});
