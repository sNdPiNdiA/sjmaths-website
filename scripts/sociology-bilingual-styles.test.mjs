import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import crypto from 'node:crypto';
import {
  externalizeSociologyBilingualStyle,
  hydrateSociologyBilingualStyle,
  sociologyBilingualCss,
  sociologyBilingualStyleLink,
} from './lib/sociology-bilingual-styles.mjs';

const cssHash = '21aaa88b15d81fffda23da5d03c80fc7312166c522dfd00f48efb8bc3509d27d';
const digest = value => crypto.createHash('sha256').update(value).digest('hex');

test('Sociology bilingual stylesheet matches the audited 88-page source block', () => {
  assert.equal(Buffer.byteLength(sociologyBilingualCss), 10169);
  assert.equal(digest(sociologyBilingualCss), cssHash);
  const translator = fs.readFileSync(new URL('./translate_sociology_hindi.mjs', import.meta.url), 'utf8');
  const templateStyles = [...translator.matchAll(/<style>([\s\S]*?)<\/style>/gi)];
  assert.equal(templateStyles.length, 1);
  assert.equal(templateStyles[0][1].trim(), sociologyBilingualCss);
  assert.match(translator, /externalizeSociologyBilingualStyle\([\s\S]*?strict:\s*true/);
});

test('exact extraction is idempotent and preserves later style variants and document bytes', () => {
  const html = `<head><link href="before.css"><style>\n${sociologyBilingualCss}\n</style><style media="print">.print{display:block}</style></head><main>Study content stays intact</main>`;
  const expected = `<head><link href="before.css">${sociologyBilingualStyleLink}<style media="print">.print{display:block}</style></head><main>Study content stays intact</main>`;
  assert.equal(externalizeSociologyBilingualStyle(html, sociologyBilingualCss, { strict: true }), expected);
  assert.equal(externalizeSociologyBilingualStyle(expected, sociologyBilingualCss), expected);
  assert.throws(() => externalizeSociologyBilingualStyle('<style>.changed{}</style>', sociologyBilingualCss, { strict: true }), /found 0/);
});

test('hydration restores the shared stylesheet from minified and versioned references', () => {
  const minifiedLink = sociologyBilingualStyleLink.replace('sociology-bilingual-topic.css', 'sociology-bilingual-topic.min.css?v=abc');
  assert.equal(hydrateSociologyBilingualStyle(minifiedLink), `<style>${sociologyBilingualCss}</style>`);
});
