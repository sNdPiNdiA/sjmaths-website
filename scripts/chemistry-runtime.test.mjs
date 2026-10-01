import test from 'node:test';
import assert from 'node:assert/strict';
import crypto from 'node:crypto';
import fs from 'node:fs';
import { load } from 'cheerio';
import { renderTopicHtml } from './lib/chemistry-renderer.mjs';
import { buildCompleteBilingualHtml } from './lib/chemistry-bilingual.mjs';
import { chemistryEnglishScript, chemistryBilingualScript, externalizeChemistryRuntime, hydrateChemistryRuntime, legacyChemistryEnglish, legacyChemistryBilingual } from './lib/chemistry-runtime.mjs';
import * as fixture from './fixtures/chemistry.mjs';
const hash = value => crypto.createHash('sha256').update(value).digest('hex');
const golden = [
  ['6273aeae3f9e5c9f49c70d4fa1ab5ecd0397c577b785fa1ab889d7504684a7d4', '1731498a2e2cb0016ea84f9d9630d65a5cc8b59af21a788dd8c739620e160803'],
  ['c762a91bb87a9c260fc5030645f737e77ce503a3998e9ec7c98a85713f7354fa', '721adda243691b48596823ca713cd5e55c033c2d295aaf67806bbd99c8a65fa4'],
];

for (const minimal of [false, true]) {
  test(`Chemistry renderer and translator match original output except shared runtime (minimal=${minimal})`, () => {
    const data = minimal ? { ...fixture.data, formula_sheet: [], critical_exceptions: [], tips_and_tricks: [], comparison_matrix: null, chapter_summary_concepts: [], quick_revision: {} } : fixture.data;
    const english = renderTopicHtml(fixture.item, fixture.context, data);
    const bilingual = buildCompleteBilingualHtml(english, fixture.enData, fixture.hiData, ...[data.quiz, data.pyq_patterns, data.topic_test].map(fixture.translatedQuestions));
    assert.equal(hash(english), golden[Number(minimal)][0]);
    assert.equal(hash(bilingual), golden[Number(minimal)][1]);
    assert.equal(english.split(chemistryEnglishScript).length - 1, 1);
    assert.equal(bilingual.split(chemistryBilingualScript).length - 1, 1);
    const $ = load(bilingual);
    assert.equal($('.tab-btn').length, 5);
    assert.equal($('.notes-section').length, 2);
    assert.equal($('.quiz-question-card').length, 20);
    assert.equal($('.pyq-card').length, 6);
    assert.equal($('.test-question-card').length, 10);
    assert.match($('.pyq-badge').first().text(), /2020, 2023/);
    assert.match($('#tab-notes').text(), /Original point A/);
    assert.match($('#tab-notes').text(), /मूल बिंदु A/);
    assert.match($('#tab-notes').text(), /r=k\[A\]/);
    const retranslated = buildCompleteBilingualHtml(bilingual, fixture.enData, fixture.hiData, ...[data.quiz, data.pyq_patterns, data.topic_test].map(fixture.translatedQuestions));
    assert.equal(retranslated.split(chemistryBilingualScript).length - 1, 1);
    assert.equal((hydrateChemistryRuntime(retranslated).match(/function setLanguage\(/g) || []).length, 1);
  });
}

test('Chemistry migration matches frozen implementations and never consumes unknown scripts', () => {
  assert.equal(hash(legacyChemistryBilingual), 'a234922484b3130a41991d2184b7492ab55e25e2a9b51f63af4552100f2db9db');
  for (const [source, tag] of [[legacyChemistryEnglish, chemistryEnglishScript], [legacyChemistryBilingual, chemistryBilingualScript]]) {
    const prefix = '<script type="application/json">{"original":true}</script><h1>Original $x^2$</h1>';
    const suffix = '<p>Original educational content</p>';
    assert.equal(externalizeChemistryRuntime(prefix + `<script>${source}</script>` + suffix), prefix + tag + suffix);
    assert.equal(externalizeChemistryRuntime(hydrateChemistryRuntime(tag)), tag);
    assert.equal(hydrateChemistryRuntime(tag.replace('.js', '.min.js?v=abc')), `<script>${source}</script>`);
    for (const unknown of [`<script defer>${source}</script>`, `<script>${source}\nwindow.extra=true;</script>`]) assert.equal(externalizeChemistryRuntime(unknown), unknown);
  }
});

test('Chemistry CLI entry points reuse the importable offline pure modules', () => {
  const generator = fs.readFileSync(new URL('./generate_chemistry.mjs', import.meta.url), 'utf8');
  const translator = fs.readFileSync(new URL('./translate_chemistry_hindi.mjs', import.meta.url), 'utf8');
  assert.match(generator, /import \{ renderTopicHtml \} from '\.\/lib\/chemistry-renderer\.mjs'/);
  assert.match(translator, /import \{ cleanMathHtml, buildCompleteBilingualHtml \} from '\.\/lib\/chemistry-bilingual\.mjs'/);
  assert.doesNotMatch(generator, /function renderTopicHtml\(/);
  assert.doesNotMatch(translator, /function buildCompleteBilingualHtml\(/);
});
