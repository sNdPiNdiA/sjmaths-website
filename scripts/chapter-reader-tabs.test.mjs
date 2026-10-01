import test from 'node:test';
import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import { ROOT } from './seo-html.cjs';
import {
  chapterReaderTabsTag,
  externalizeChapterReaderTabs,
  hydrateChapterReaderTabs,
  validateChapterReaderTabs,
} from './lib/chapter-reader-tabs.mjs';

const sample = 'class-11-maths/chapter-wise-notes/chapter-1-sets/index.html';
const baseline = execFileSync('git', ['show', `237db669da5fca0a8ff8ae6a5a601d284a367642:${sample}`], { cwd: ROOT, encoding: 'utf8', maxBuffer: 20e6 });
const runtime = [...baseline.matchAll(/<script>([\s\S]*?)<\/script>/gi)].map(match => match[1]).find(source => source.includes('openMobileDockDrawer'));

test('chapter tab/drawer controller is fingerprinted and contains all global handlers', () => {
  assert.equal(Buffer.byteLength(validateChapterReaderTabs(runtime)), 3216);
  for (const name of ['toggleNavTabDropdown', 'openMobileDockDrawer', 'closeMobileDockDrawer', 'switchTab']) assert.match(runtime, new RegExp(`function ${name}\\(`));
});

test('exact extraction preserves parser-blocking placement and hydration', () => {
  const before = `<body><button>navigation</button><script>\n${runtime}\n</script><script defer>later()</script></body>`;
  const after = `<body><button>navigation</button>${chapterReaderTabsTag}<script defer>later()</script></body>`;
  assert.equal(externalizeChapterReaderTabs(before, runtime, { strict: true }), after);
  assert.equal(hydrateChapterReaderTabs(after, runtime), before.replace(`<script>\n${runtime}\n</script>`, `<script>${runtime.trim()}</script>`));
  assert.equal(externalizeChapterReaderTabs(after, runtime), after, 'repeat extraction is idempotent');
  assert.throws(() => externalizeChapterReaderTabs('<script>changed()</script>', runtime, { strict: true }), /found 0/);
});
