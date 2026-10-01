import test from 'node:test';
import assert from 'node:assert/strict';
import crypto from 'node:crypto';
import vm from 'node:vm';
import { PAGE_TEMPLATE } from '../upsc/upsc-microtopic-template.js';
import { externalizeUpscLanguage, hydrateUpscLanguage, upscLanguageScript, upscLanguageSource } from './lib/upsc-language.mjs';

test('UPSC shared language source is the exact original bootstrap', () => {
  assert.equal(crypto.createHash('sha256').update(upscLanguageSource).digest('hex'), 'f650a6e0aaa5f5e792ad0f57f50f1410aecfec7e8f16e42c95696f35f645d7e0');
  assert.equal(PAGE_TEMPLATE.split(upscLanguageScript).length - 1, 1);
  assert.equal(PAGE_TEMPLATE.indexOf(upscLanguageScript) > PAGE_TEMPLATE.indexOf('id="langHi"'), true);
  assert.doesNotMatch(upscLanguageScript, /\b(?:async|defer|type)=?/);
});
test('exact script extraction preserves load position, neighbouring data and modified implementations', () => {
  const prefix = '<body><script type="application/json">{"original":true}</script><button id="langHi"></button>';
  const suffix = '<script type="module" src="auth.js"></script></body>';
  assert.equal(externalizeUpscLanguage(prefix + `<script>\n${upscLanguageSource}\n</script>` + suffix), prefix + upscLanguageScript + suffix);
  assert.equal(externalizeUpscLanguage(upscLanguageScript), upscLanguageScript);
  assert.equal(externalizeUpscLanguage(hydrateUpscLanguage(upscLanguageScript)), upscLanguageScript);
  assert.equal(hydrateUpscLanguage(upscLanguageScript.replace('.js', '.min.js?v=1234')), `<script>${upscLanguageSource}</script>`);
  for (const tag of [
    upscLanguageScript.replace(' src=', ' defer src='),
    upscLanguageScript.replace(' src=', ' type="module" src='),
    upscLanguageScript.replace('/assets/js/upsc-language.js', '/unowned.js'),
  ]) assert.equal(hydrateUpscLanguage(tag), tag);
  for (const tag of [
    `<script>${upscLanguageSource}\nwindow.extra=true;</script>`,
    `<script defer>${upscLanguageSource}</script>`,
    `<script type="module">${upscLanguageSource}</script>`,
    `<script id="other">${upscLanguageSource}</script>`,
  ]) assert.equal(externalizeUpscLanguage(tag), tag);
});

for (const initial of [undefined, 'en', 'hi']) {
  test(`language preference ${initial ?? 'unset'} keeps DOM classes, aria and storage in sync`, () => {
    const element = () => ({
      classes: new Set(), attributes: {}, listeners: {},
      classList: { toggle(name, enabled) { if (enabled) this.owner.classes.add(name); else this.owner.classes.delete(name); } },
      setAttribute(name, value) { this.attributes[name] = value; },
      addEventListener(name, handler) { this.listeners[name] = handler; },
    });
    const elements = Object.fromEntries(['html', 'body', 'langEn', 'langHi'].map(name => [name, element()]));
    for (const value of Object.values(elements)) value.classList.owner = value;
    const listeners = {}, storage = new Map(initial ? [['sj_pref_lang', initial]] : []);
    const document = {
      documentElement: elements.html, body: elements.body,
      getElementById: id => elements[id],
      addEventListener: (event, handler) => { listeners[event] = handler; },
    };
    const localStorage = { getItem: key => storage.get(key) ?? null, setItem: (key, value) => storage.set(key, value) };
    vm.runInNewContext(upscLanguageSource, { document, localStorage });
    assert.equal(storage.get('sj_pref_lang'), initial, 'registration does not apply early');
    listeners.DOMContentLoaded();
    const check = lang => {
      for (const name of ['html', 'body']) {
        assert.equal(elements[name].classes.has('lang-hi'), lang === 'hi');
        assert.equal(elements[name].classes.has('lang-en'), lang !== 'hi');
      }
      assert.equal(elements.langHi.attributes['aria-pressed'], String(lang === 'hi'));
      assert.equal(elements.langEn.attributes['aria-pressed'], String(lang !== 'hi'));
      assert.equal(storage.get('sj_pref_lang'), lang);
    };
    check(initial || 'en');
    elements.langHi.listeners.click(); check('hi');
    elements.langEn.listeners.click(); check('en');
  });
}
