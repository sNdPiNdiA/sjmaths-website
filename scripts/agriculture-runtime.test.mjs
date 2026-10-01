import test from 'node:test';
import assert from 'node:assert/strict';
import crypto from 'node:crypto';
import { load } from 'cheerio';
import { renderTopicHtml } from './lib/agriculture-renderer.mjs';
import { transformHtml } from './lib/agriculture-redesign.mjs';
import * as runtime from './lib/agriculture-runtime.mjs';
import * as fixture from './fixtures/agriculture.mjs';
const hash = value => crypto.createHash('sha256').update(value).digest('hex');
const golden = [
  ['883e07fb0f42de1ed2e7025bdccee6a65133d6c6239ce92400bd8e4fbb79ffe3', '9a5cc1bddf5546479992fdbac1cfac1404a47049c4303d95d4065dc0aeff7e9a'],
  ['22de10fc1e4fffb61e6d17ad5323f6b150fba5b5e3aa2b2f2694193ce895e950', '74a8cb80a60559e0453414f1e3a20f9b3ab42d5cce16a3e4279f13c1ffd59238'],
];
for (const minimal of [false, true]) {
  test(`Agriculture pure renderer and redesign preserve original outputs (minimal=${minimal})`, () => {
    const data = minimal ? { ...fixture.data, comparison_tables: [], mnemonics: [], exam_points: [], common_errors: [], chapter_summary_concepts: [], quick_revision: {} } : fixture.data;
    const generated = renderTopicHtml(fixture.item, fixture.context, data);
    const redesigned = transformHtml(generated);
    assert.equal(hash(generated), golden[Number(minimal)][0]);
    assert.equal(hash(redesigned), golden[Number(minimal)][1]);
    assert.equal(generated.split(runtime.agricultureGeneratedScript).length - 1, 1);
    assert.equal(redesigned.split(runtime.agricultureRedesignedScript).length - 1, 1);
    assert.equal(transformHtml(redesigned), redesigned, 'repeat redesign must remain idempotent');
    const $ = load(generated);
    assert.equal($('.tab-btn').length, 5);
    assert.equal($('.notes-section').length, 2);
    assert.equal($('.quiz-question-card').length, 20);
    assert.equal($('.test-question-card').length, 10);
    assert.match($('#tab-notes').text(), /Original point A/);
    assert.match($('#tab-notes').text(), /\$2n\$/);
    assert.match($('#tab-notes').text(), /Original point B/);
    assert.equal($('.comparison-card').length, minimal ? 0 : 1);
    assert.equal($('.mnemonic-card').length, minimal ? 0 : 1);
  });
}
test('Agriculture migration is exact and preserves its two established variants', () => {
  assert.equal(hash(runtime.agricultureGeneratedRuntime), '06d46b789cb2022d9236721a21d665b9bf3894b996e4cac3ccf6b59966158cf4');
  assert.equal(hash(runtime.agricultureRedesignedRuntime), '673c8f103713d25346b9dfab7bb5a3fe419873efe2f1f8203aa1c62c3858f289');
  for (const [source, tag] of [[runtime.agricultureGeneratedRuntime, runtime.agricultureGeneratedScript], [runtime.agricultureRedesignedRuntime, runtime.agricultureRedesignedScript]]) {
    const before = '<h1>Original $2n$</h1>';
    const after = '<p>Original questions</p>';
    assert.equal(runtime.externalizeAgricultureRuntime(before + `<script>${source}</script>` + after), before + tag + after);
    assert.equal(runtime.hydrateAgricultureRuntime(tag.replace('.js', '.min.js?v=abc')), `<script>${source}</script>`);
    for (const unknown of [`<script defer>${source}</script>`, `<script>${source}\nwindow.extra=true;</script>`]) assert.equal(runtime.externalizeAgricultureRuntime(unknown), unknown);
  }
});
