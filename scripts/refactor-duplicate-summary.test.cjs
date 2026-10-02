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
