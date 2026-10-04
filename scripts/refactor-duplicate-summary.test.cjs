const test = require('node:test');
const assert = require('node:assert/strict');
const { summarizeDuplicateBlocks } = require('./lib/refactor-duplicate-summary.cjs');

test('inventory separates within-page repetition from cross-page sharing without changing totals', () => {
  const map = new Map([
    ['single', { bytes: 1000, occurrences: 3, files: ['a.html'] }],
    ['cross', { bytes: 100, occurrences: 2, files: ['b.html', 'c.html'] }],
    ['mixed', { bytes: 10, occurrences: 5, files: ['d.html', 'e.html', 'f.html'] }],
    ['unique', { bytes: 9999, occurrences: 1, files: ['g.html'] }],
  ]);
  const before = JSON.stringify([...map]);
  const summary = summarizeDuplicateBlocks(map);
  assert.equal(summary.extraBytes, 2140);
  assert.equal(summary.withinPageRepeatedBytes, 2020);
  assert.equal(summary.crossPageRepeatedBytes, 120);
  assert.equal(summary.extraBytes, summary.withinPageRepeatedBytes + summary.crossPageRepeatedBytes);
  assert.equal(summary.withinPageGroups, 2);
  assert.equal(summary.crossPageGroups, 2);
  assert.deepEqual(summary.groups.map(group => group.files[0]), ['a.html', 'b.html', 'd.html']);
  assert.equal(JSON.stringify([...map]), before);
});
test('empty and unique-only inventories have no duplication candidates', () => {
  for (const map of [new Map(), new Map([['unique', { bytes: 100, occurrences: 1, files: ['a.html'] }]])]) {
    assert.equal(summarizeDuplicateBlocks(map).extraBytes, 0);
    assert.deepEqual(summarizeDuplicateBlocks(map).groups, []);
  }
});

test('exact duplicate page shells and scripts are removed once without touching unique content', async () => {
  const { removeExactDuplicates } = await import('./dedupe-exact-page-duplicates.mjs');
  const source = '<!doctype html><html><body>' +
    '<header><a href="/">Home</a></header><main><h1>Lesson</h1><p>Keep this lesson.</p></main>' +
    '<script>window.lessonReady = true;</script><footer>Footer</footer>' +
    '<header><a href="/">Home</a></header><main><h1>Lesson</h1><p>Keep this lesson.</p></main>' +
    '<script>window.lessonReady = true;</script><footer>Footer</footer>' +
    '</body></html>';
  const result = removeExactDuplicates(source);
  const { load } = require('cheerio');
  const $ = load(result.source);
  assert.equal($('header').length, 1);
  assert.equal($('main').length, 1);
  assert.equal($('footer').length, 1);
  assert.equal($('script').length, 1);
  assert.equal($('main').text(), 'LessonKeep this lesson.');
  assert.deepEqual(removeExactDuplicates(result.source).ranges, []);
});

test('distinct lesson sections and scripts are retained', async () => {
  const { removeExactDuplicates } = await import('./dedupe-exact-page-duplicates.mjs');
  const source = '<!doctype html><html><body><main><h1>One</h1></main>' +
    '<main><h1>Two</h1></main><script>window.first = 1;</script>' +
    '<script>window.second = 2;</script></body></html>';
  const result = removeExactDuplicates(source);
  const { load } = require('cheerio');
  const $ = load(result.source);
  assert.equal($('main').length, 2);
  assert.equal($('script').length, 2);
  assert.deepEqual(result.ranges, []);
});

test('removing an indented duplicate also removes its empty indentation line', async () => {
  const { removeExactDuplicates } = await import('./dedupe-exact-page-duplicates.mjs');
  const source = '<!doctype html>\n<body>\n  <main><p>Keep</p></main>\n  <main><p>Keep</p></main>\n</body>';
  const result = removeExactDuplicates(source);
  assert.equal(result.source, '<!doctype html>\n<body>\n  <main><p>Keep</p></main>\n</body>');
  assert.deepEqual(removeExactDuplicates(result.source).ranges, []);
});
