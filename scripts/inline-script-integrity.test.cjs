const test = require('node:test');
const assert = require('node:assert/strict');
const { inspectInlineScripts } = require('./lib/inline-script-integrity.cjs');
const { recoverRepeatedBodyPage } = require('./lib/recover-katex-expanded-pages.cjs');
const { exposeUpperPrimaryRuntimeGlobals } = require('./lib/up-upper-primary-runtime-globals.cjs');
test('checks classic scripts without executing them and excludes data, modules and external scripts', () => {
  const html = '<script>throw new Error("must not run");</script><script type="application/ld+json">{broken}</script><script type="module">import x from "x";</script><script src="x.js"></script><script type="text/javascript">const x = 1;</script>';
  const scripts = inspectInlineScripts(html);
  assert.equal(scripts.length, 2);
  assert.deepEqual(scripts.map(script => script.syntaxError), [null, null]);
});
test('shared Upper Primary runtime receives its checklist and complete test data on window', () => {
  const input = '<script>const TOPIC_STORAGE_KEY = \'checklist\'; const TOPIC_CHECKBOX_ID = \'topic-3\'; const testData = [{"question":"नाद","correct_index":0}];</script>';
  const output = exposeUpperPrimaryRuntimeGlobals(input);
  assert.equal(output, '<script>window.TOPIC_STORAGE_KEY = \'checklist\'; window.TOPIC_CHECKBOX_ID = \'topic-3\'; window.testData = [{"question":"नाद","correct_index":0}];</script>');
  assert.equal(exposeUpperPrimaryRuntimeGlobals(input.replace('const testData =', 'let testData =')), null);
  assert.equal(exposeUpperPrimaryRuntimeGlobals('<script>const testData = [];</script>'), null);
});
test('reports corrupt embedded documents and exact duplicates without rewriting source', () => {
  const html = '<script>const a = "\n<body><main>Lesson</main>";</script><script>const x=1;</script><script>const x=1;</script>';
  const scripts = inspectInlineScripts(html);
  assert.ok(scripts[0].syntaxError);
  assert.equal(scripts[0].nestedDocumentMarkup, true);
  assert.equal(scripts[2].duplicateOf, 1);
  assert.equal(scripts[1].duplicateOf, null);
});
test('KaTeX recovery preserves byte-identical repeated bodies and refuses content variants', () => {
  const head = '<html><head><title>अनुरक्षित</title><script type="application/ld+json">{}</script>';
  const injected = '<script>\n    document.addEventListener("DOMContentLoaded", function () {\n        if (typeof renderMathInElement === \'function\')';
  const body = '<body><main>पूरा पाठ</main><script type="application/json">{"q":1}</script></body>';
  const source = `${head}${injected}${body}${body}</head>${body}</html>`;
  const result = recoverRepeatedBodyPage(source, '<link rel="katex"><script>math();</script>');
  assert.ok(result);
  assert.equal(result.split(body).length - 1, 1);
  assert.ok(result.includes('<title>अनुरक्षित</title>'));
  assert.ok(result.includes('application/json'));
  assert.equal(inspectInlineScripts(result).filter(script => script.syntaxError).length, 0);
  assert.equal(recoverRepeatedBodyPage(source.replace('<main>पूरा पाठ</main>', '<main>बदला हुआ</main>', 1), '<link>'), null);
  assert.equal(recoverRepeatedBodyPage(source, ''), null);
});
