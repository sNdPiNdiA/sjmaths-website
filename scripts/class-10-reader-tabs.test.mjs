import test from 'node:test';
import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import { ROOT } from './seo-html.cjs';
import {
  class10ReaderTabsTag,
  externalizeClass10ReaderTabs,
  hydrateClass10ReaderTabs,
  validateClass10ReaderTabs,
} from './lib/class-10-reader-tabs.mjs';

const sample = 'class-10-maths/chapter-wise-notes/chapter-1-real-numbers/index.html';
const baseline = execFileSync('git', ['show', `afb5a3473445d7609eb3004b999c66b9d0215c70:${sample}`], { cwd: ROOT, encoding: 'utf8', maxBuffer: 20e6 });
const runtime = [...baseline.matchAll(/<script>([\s\S]*?)<\/script>/gi)].map(match => match[1]).find(source => source.includes('openMobileDockDrawer'));

test('Class 10 chapter resource-tab controller is pinned and retains its iframe lifecycle behavior', () => {
  const checked = validateClass10ReaderTabs(runtime);
  assert.equal(Buffer.byteLength(checked), 5124);
  for (const name of ['toggleNavTabDropdown', 'openMobileDockDrawer', 'closeMobileDockDrawer', 'switchTab']) {
    assert.ok(checked.includes(`function ${name}(`), `${name} handler exists`);
  }
  assert.ok(checked.includes('iframe.onload = function()'));
  assert.ok(checked.includes('embeddedHeight'));
  assert.ok(checked.includes("document.querySelector('main')"));
});

test('exact Class 10 extraction preserves script position and hydration', () => {
  const before = `<body><main>notes</main><script>\n${runtime}\n</script><script defer>later()</script></body>`;
  const after = `<body><main>notes</main>${class10ReaderTabsTag}<script defer>later()</script></body>`;
  assert.equal(externalizeClass10ReaderTabs(before, runtime, { strict: true }), after);
  assert.equal(hydrateClass10ReaderTabs(after, runtime), before.replace(`<script>\n${runtime}\n</script>`, `<script>${runtime.trim()}</script>`));
  assert.equal(externalizeClass10ReaderTabs(after, runtime), after, 'repeat extraction is idempotent');
  assert.throws(() => externalizeClass10ReaderTabs('<script>changed()</script>', runtime, { strict: true }), /found 0/);
});
