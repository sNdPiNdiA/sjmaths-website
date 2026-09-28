import test from 'node:test';
import assert from 'node:assert/strict';
import { createReferenceUpdater } from './lib/build-references.mjs';
import { legacyReferenceUpdater } from './fixtures/build-references-legacy.mjs';
const mapping = {
  'assets/js/example.js': 'assets/js/example.min.js',
  'assets/js/example-long.js': 'assets/js/example-long.min.js',
  'assets/js/example.js-extra.js': 'assets/js/example.js-extra.min.js',
  'assets/css/example.css': 'assets/css/example.min.css',
  './assets/vendor/fontawesome/css/all.min.css': './assets/vendor/fontawesome/css/all.min.css',
  'assets/vendor/fontawesome/css/all.min.css': 'assets/vendor/fontawesome/css/all.min.css',
};
const hashes = Object.fromEntries(Object.values(mapping).map(file => [file, '1234abcd']));
test('reference preselection preserves existing prefix, alias, query and ordering semantics', () => {
  const update = createReferenceUpdater(mapping, hashes), old = legacyReferenceUpdater(mapping, hashes);
  for (const source of [
    '<script src="/assets/js/example.js"></script>',
    '<link href="./assets/css/example.min.css?v=old.1">',
    '../assets/js/example-long.js ../../assets/js/example.js',
    'assets/js/example.min.js?v=old&mode=test#part',
    'https://sjmaths.com/assets/css/example.css?v=old',
    './assets/vendor/fontawesome/css/all.min.css?v=old /assets/vendor/fontawesome/css/all.min.css',
    '<p>Do not edit original concepts or formulas.</p>',
    'assets/js/example-long.js assets/js/example.js assets/css/example.css',
    'assets/js/example.js-extra.js',
  ]) assert.equal(update(source), old(source), source);
  assert.equal(createReferenceUpdater({}, {})('Unchanged'), 'Unchanged');
});
