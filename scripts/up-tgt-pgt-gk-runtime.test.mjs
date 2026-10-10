import test from 'node:test';
import assert from 'node:assert/strict';
import crypto from 'node:crypto';
import fs from 'node:fs';
import { execFileSync } from 'node:child_process';
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
  assert.equal(crypto.createHash('sha256').update(upTgtPgtGkRuntimeSource).digest('hex'), 'c6978e403be665108d19cd1bc5c32a3234722f706a4662fb4b511fa724718c73');
  const languageSource = fs.readFileSync(new URL('../assets/js/up-tgt-pgt-gk-language.js', import.meta.url), 'utf8').trim();
  assert.equal(crypto.createHash('sha256').update(languageSource).digest('hex'), 'a88c19120619de7883263307647920244937e72d19efa8d1d9e52aeafdb5ed4e');
});

test('topic runtime extraction is fingerprinted, idempotent and variant-safe', () => {
  const legacy = 'document.addEventListener("DOMContentLoaded",()=>{});';
  const fingerprint = crypto.createHash('sha256').update(legacy).digest('hex');
  const page = `<body><script>${legacy}</script><script>keepThis()</script></body>`;
  assert.equal(
    externalizeUpTgtPgtGkTopicRuntime(page, fingerprint),
    `<body>${upTgtPgtGkRuntimeTag}<script>keepThis()</script></body>`,
  );
  const legacyHtml = execFileSync('git', ['show', '6be921178f2787101ae755971253e564df0c85f2:up-tgt-pgt-gk/art-culture/classical-dances/index.html'], { encoding: 'utf8', maxBuffer: 2e6 });
  const languageSource = [...legacyHtml.matchAll(/<script\b([^>]*)>([\s\S]*?)<\/script>/gi)].find(match => match[1].includes('id="bilingual-runtime"'))[2];
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

test('existing bilingual output keeps localization in data and uses the shared runtimes', () => {
  // The historical bilingualizer was removed; inspect its maintained output.
  const source = fs.readFileSync(new URL('../up-tgt-pgt-gk/art-culture/classical-dances/index.html', import.meta.url), 'utf8');
  assert.ok(source.includes('id="bilingual-data"'));
  assert.ok(source.includes('data-up-tgt-pgt-gk-runtime="language"'));
  assert.ok(source.includes('data-up-tgt-pgt-gk-runtime="topic"'));
  assert.doesNotMatch(source, /function bilingualRuntimeFixed|function markQuiz|function submitTest/);
});
