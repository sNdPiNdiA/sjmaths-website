import test from 'node:test';
import assert from 'node:assert/strict';
import * as cheerio from 'cheerio';
import { historyStyles, historyTopicCss, historyStyleLink, hydrateHistoryStyles, externalizeHistoryStyles } from './lib/history-styles.mjs';
import { historyTabCss } from './lib/history-renderer.mjs';

test('exact stylesheet extraction preserves surrounding content and cascade position', () => {
  const prefix = '<head><link href="prior.css" rel="stylesheet">';
  const suffix = '<style>.later{color:red}</style></head><body><h1>Original question</h1><script type="application/json">{"answer":42}</script></body>';
  const original = prefix + `<style>\n${historyTopicCss}\n</style>` + suffix;
  const extracted = externalizeHistoryStyles(original);
  assert.equal(extracted, prefix + historyStyleLink + suffix);
  assert.equal(externalizeHistoryStyles(extracted), extracted);
  assert.equal(externalizeHistoryStyles(hydrateHistoryStyles(extracted)), extracted);
});

test('generator serialization preserves the marker and regeneration can recover CSS', () => {
  const serialized = cheerio.load('<head>' + historyStyleLink + '</head><body>Content</body>').html();
  const hydrated = hydrateHistoryStyles(serialized);
  assert.ok(hydrated.includes(`<style>${historyTopicCss}</style>`));
  assert.equal(externalizeHistoryStyles(hydrated), serialized);
  const built = '<link data-history-shared-style="topic" href="/assets/css/history-topic.min.css?v=1234" rel="stylesheet">';
  assert.equal(hydrateHistoryStyles(built), `<style>${historyTopicCss}</style>`);
  const unrelated = '<link data-history-shared-style="topic" href="other.css">';
  assert.equal(hydrateHistoryStyles(unrelated), unrelated);
});

test('modified rules and style attributes are not silently discarded', () => {
  for (const original of [
    `<style>${historyTopicCss}\n.new-rule{color:red}</style>`,
    `<style media="print">${historyTopicCss}</style>`,
    `<style nonce="nonce">${historyTopicCss}</style>`,
  ]) assert.equal(externalizeHistoryStyles(original), original);
  assert.equal(externalizeHistoryStyles(`<style>${historyTopicCss.replace(/\n/g, '\r\n')}</style>`), historyStyleLink);
});

test('current generator tab styles already exist in the shared stylesheet', () => {
  const css = historyTabCss();
  assert.ok(historyTopicCss.replace(/\r\n/g, '\n').includes(css.replace(/\r\n/g, '\n')));
});

test('all three variants round-trip without merging different cascades', () => {
  for (const variant of historyStyles) {
    assert.equal(externalizeHistoryStyles(`<style>${variant.css}</style>`), variant.link);
    assert.equal(hydrateHistoryStyles(variant.link), `<style>${variant.css}</style>`);
    const built = variant.link.replace(`${variant.name}.css`, `${variant.name}.min.css?v=abcd`);
    assert.equal(hydrateHistoryStyles(built), `<style>${variant.css}</style>`);
  }
});
