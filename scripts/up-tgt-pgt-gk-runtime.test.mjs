import test from 'node:test';
import assert from 'node:assert/strict';
import crypto from 'node:crypto';
import fs from 'node:fs';
import {
  externalizeUpTgtPgtGkGenerator,
  externalizeUpTgtPgtGkTopicRuntime,
  legacyUpTgtPgtGkRuntimeHash,
  normalizeUpTgtPgtGkGeneratorForParity,
  upTgtPgtGkRuntimeSource,
  upTgtPgtGkLanguageRuntimeTag,
  upTgtPgtGkRuntimeTag,
} from './lib/up-tgt-pgt-gk-runtime.mjs';

test('shared GK runtime supports translated and untranslated generator output', () => {
  assert.match(upTgtPgtGkRuntimeSource, /bilingualDataElement\?\.textContent\|\|'\{\}'/);
  assert.match(upTgtPgtGkRuntimeSource, /bilingualDataElement\?'hi':'en'/);
  assert.match(upTgtPgtGkRuntimeSource, /bilingualData\.quiz\?\.length\?bilingualData\.quiz/);
  assert.match(upTgtPgtGkRuntimeSource, /pageLanguage==='hi'\?'✓ सही':'✓ Correct'/);
  assert.doesNotMatch(upTgtPgtGkRuntimeSource, /typeNames|const letters=/);
  assert.equal(crypto.createHash('sha256').update(upTgtPgtGkRuntimeSource).digest('hex'), 'ad5406ccedd6a4b088b7841249e770623e3f7bb305f7a2ed6bc02f0933e58fcf');
  const languageSource = fs.readFileSync(new URL('../assets/js/up-tgt-pgt-gk-language.js', import.meta.url), 'utf8').trim();
  assert.equal(crypto.createHash('sha256').update(languageSource).digest('hex'), 'a2e070d55937ea5f7485a0755d83e9634706bc88a3142c0c541af61573139471');
});

test('topic runtime extraction is fingerprinted, idempotent and variant-safe', () => {
  const legacy = 'document.addEventListener("DOMContentLoaded",()=>{});';
  const fingerprint = crypto.createHash('sha256').update(legacy).digest('hex');
  const page = `<body><script>${legacy}</script><script>keepThis()</script></body>`;
  assert.equal(
    externalizeUpTgtPgtGkTopicRuntime(page, fingerprint),
    `<body>${upTgtPgtGkRuntimeTag}<script>keepThis()</script></body>`,
  );
  const languageSource = fs.readFileSync(new URL('../assets/js/up-tgt-pgt-gk-language.js', import.meta.url), 'utf8').trim();
  const bilingualPage = `<body><script>${legacy}</script><script id="bilingual-runtime">${languageSource}</script><main>Keep content</main></body>`;
  assert.equal(
    externalizeUpTgtPgtGkTopicRuntime(bilingualPage, fingerprint),
    `<body>${upTgtPgtGkRuntimeTag}${upTgtPgtGkLanguageRuntimeTag}<main>Keep content</main></body>`,
  );
  assert.equal(externalizeUpTgtPgtGkTopicRuntime(upTgtPgtGkRuntimeTag), upTgtPgtGkRuntimeTag);
  assert.throws(() => externalizeUpTgtPgtGkTopicRuntime('<script>differentRuntime()</script>'), /exact legacy GK runtime/);
});

test('generator emits the shared parser-blocking runtime at the original template position', () => {
  const source = fs.readFileSync(new URL('./generate_up_tgt_pgt_gk.mjs', import.meta.url), 'utf8');
  const after = externalizeUpTgtPgtGkGenerator(source);
  assert.equal(normalizeUpTgtPgtGkGeneratorForParity(source), normalizeUpTgtPgtGkGeneratorForParity(after));
  assert.ok(after.includes("import { upTgtPgtGkRuntimeTag } from './lib/up-tgt-pgt-gk-runtime.mjs';"));
  assert.equal(after.split('${upTgtPgtGkRuntimeTag}').length - 1, 1);
  assert.equal(externalizeUpTgtPgtGkGenerator(after), after);
});

test('bilingualizer keeps localization in data and does not rewrite runtime source', () => {
  const source = fs.readFileSync(new URL('./bilingualize_up_tgt_pgt_gk.mjs', import.meta.url), 'utf8');
  assert.ok(source.includes('upTgtPgtGkRuntimeSrc'));
  assert.ok(source.includes('bilingual-data'));
  assert.ok(source.includes('upTgtPgtGkLanguageRuntimeTag'));
  assert.doesNotMatch(source, /function bilingualRuntimeFixed/);
  assert.doesNotMatch(source, /const oldQuiz\s*=|const newQuiz\s*=|Accepted answer\\\(s\\\)/);
});
