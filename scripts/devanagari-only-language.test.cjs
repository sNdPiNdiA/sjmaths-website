'use strict';

const fs = require('node:fs');
const path = require('node:path');
const test = require('node:test');
const assert = require('node:assert/strict');
const vm = require('node:vm');

const source = fs.readFileSync(path.join(__dirname, '../assets/js/upsc-language.js'), 'utf8');

function runPage(pathname, initialPreference = 'en') {
  const listeners = {};
  const makeElement = (initialClasses = []) => {
    const classes = new Set(initialClasses);
    return {
      classes, attributes: {}, listeners: {}, removed: false, textContent: '',
      classList: {
        contains(name) { return classes.has(name); },
        add(name) { classes.add(name); },
        remove(name) { classes.delete(name); },
        toggle(name, enabled) { if (enabled) classes.add(name); else classes.delete(name); },
      },
      closest(selector) {
        return selector.includes('headerLangToggleBtn') && this === elements.headerLangToggleBtn ? this : null;
      },
      setAttribute(name, value) { this.attributes[name] = value; },
      addEventListener(name, handler) { this.listeners[name] = handler; },
      remove() { this.removed = true; },
    };
  };
  const elements = {
    html: makeElement(),
    body: makeElement(['exam-ui']),
    langEn: makeElement(),
    langHi: makeElement(),
    headerLangToggleBtn: makeElement(),
    headerLangText: makeElement(),
  };
  const document = {
    documentElement: elements.html,
    body: elements.body,
    getElementById(id) { return elements[id] || null; },
    querySelectorAll() { return [elements.langEn, elements.langHi, elements.headerLangToggleBtn]; },
    addEventListener(name, handler) { listeners[name] = handler; },
  };
  const storage = new Map([
    ['sj_pref_lang', initialPreference],
    ['sjmaths_preferred_language', initialPreference],
  ]);
  const localStorage = {
    getItem(key) { return storage.get(key) ?? null; },
    setItem(key, value) { storage.set(key, value); },
  };
  vm.runInNewContext(source, { document, window: { location: { pathname } }, localStorage });
  listeners.DOMContentLoaded();
  return { elements, storage, listeners };
}

test('Hindi and Sanskrit routes force Devanagari and remove language controls without changing site preference', () => {
  for (const route of ['/up-assistant-teacher/hindi/', '/up-assistant-teacher/sanskrit/example/']) {
    const { elements, storage } = runPage(route);
    assert.equal(elements.html.lang, route.includes('/sanskrit') ? 'sa' : 'hi');
    assert.equal(elements.html.classes.has('lang-hi'), true);
    assert.equal(elements.html.classes.has('lang-en'), false);
    assert.equal(elements.body.classes.has('devanagari-only'), true);
    assert.equal(elements.body.classes.has('lang-mode-hi'), true);
    assert.equal(elements.langEn.removed, true);
    assert.equal(elements.langHi.removed, true);
    assert.equal(elements.headerLangToggleBtn.removed, true);
    assert.equal(storage.get('sj_pref_lang'), 'en');
    assert.equal(storage.get('sjmaths_preferred_language'), 'en');
  }
});

test('other exam pages continue to honor and persist the selected language', () => {
  const { elements, storage, listeners } = runPage('/upsc/gs-paper-1/', 'en');
  assert.equal(elements.body.classes.has('lang-en'), true);
  assert.equal(elements.body.classes.has('devanagari-only'), false);
  const event = {
    target: elements.langHi,
    preventDefault() {},
    stopImmediatePropagation() {},
  };
  elements.langHi.closest = selector => selector.includes('langHi') ? elements.langHi : null;
  // The shared exam controller uses delegated capture handling.
  const clickHandler = listeners.click;
  assert.equal(typeof clickHandler, 'function');
  clickHandler(event);
  assert.equal(elements.body.classes.has('lang-hi'), true);
  assert.equal(storage.get('sj_pref_lang'), 'hi');
});
