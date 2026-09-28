const test = require('node:test');
const assert = require('node:assert/strict');
const { comparePixels } = require('./inspect-screenshot-diffs.cjs');
test('pixel inspection reports real deltas and bounds without accepting differences', () => {
  const before = new Uint8Array(16), after = new Uint8Array(16);
  assert.equal(comparePixels(before, after, 2, 2).bounds, null);
  after[12] = 10; after[15] = 255;
  const result = comparePixels(before, after, 2, 2);
  assert.equal(result.pixelsChanged, 1);
  assert.equal(result.maxChannelDelta, 255);
  assert.deepEqual(result.bounds, { left: 1, top: 1, right: 1, bottom: 1 });
  assert.throws(() => comparePixels(before, after, 3, 3), /dimensions differ/);
});
