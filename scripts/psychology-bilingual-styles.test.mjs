import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import crypto from 'node:crypto';
import {
  assertPsychologyBilingualTemplateStyle,
  externalizePsychologyBilingualStyle,
  hydratePsychologyBilingualStyle,
  psychologyBilingualStyleLink,
} from './lib/psychology-bilingual-styles.mjs';

const style = fs.readFileSync(new URL('../assets/css/psychology-bilingual-topic.css', import.meta.url), 'utf8').trim();
const digest = value => crypto.createHash('sha256').update(value).digest('hex');

test('Psychology bilingual stylesheet equals the audited 200-page source', () => {
  assert.equal(Buffer.byteLength(style), 10215);
  assert.equal(digest(style), 'd878a378c68a7f7035a93976d149c54077bb40743db000e6c602d1ecc3b4b9e7');
});

test('exact extraction is idempotent and preserves nonmatching style variants', () => {
  const html = `<head><style>\n${style}\n</style><style media="print">.print{display:block}</style></head><main>Psychology learning content</main>`;
  const expected = `<head>${psychologyBilingualStyleLink}<style media="print">.print{display:block}</style></head><main>Psychology learning content</main>`;
  const external = externalizePsychologyBilingualStyle(html, style, { strict: true });
  assert.equal(external, expected);
  assert.equal(externalizePsychologyBilingualStyle(external, style), external);
  assert.throws(() => externalizePsychologyBilingualStyle('<style>.edited{}</style>', style, { strict: true }), /found 0/);
});

test('hydration recognizes minified and cache-busted shared stylesheet links', () => {
  const html = psychologyBilingualStyleLink.replace('psychology-bilingual-topic.css', 'psychology-bilingual-topic.min.css?v=abc');
  assert.equal(hydratePsychologyBilingualStyle(html), `<style>${style}</style>`);
});

test('Hindi translator externalizes its exact template before writing translated pages', () => {
  const translator = fs.readFileSync(new URL('./translate_psychology_hindi.mjs', import.meta.url), 'utf8');
  assert.doesNotThrow(() => assertPsychologyBilingualTemplateStyle(translator));
  assert.throws(() => assertPsychologyBilingualTemplateStyle(translator.replace('--bg: #f8f9fc;', '--bg: #ffffff;')), /no longer matches/);
  assert.match(translator, /externalizePsychologyBilingualStyle/);
  assert.match(translator, /strict:\s*true/);
});
