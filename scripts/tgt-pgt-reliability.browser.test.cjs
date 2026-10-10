const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { chromium } = require('playwright');
const { ROOT, siteFiles } = require('./seo-html.cjs');
const { routeRepositoryFixtures } = require('./lib/browser-fixture.cjs');
const files = siteFiles();
const gk = '/up-tgt-pgt-gk/art-culture/classical-dances/';

async function fixture(context, url) {
  const page = await context.newPage();
  const evidence = await routeRepositoryFixtures(page, { root: ROOT, files });
  await page.goto('https://sjmaths.com' + url, { waitUntil: 'load' });
  return { page, evidence };
}

test('both tracker engines recover invalid progress, synchronize tabs and initialize once', { timeout: 120000 }, async () => {
  const browser = await chromium.launch();
  try {
    for (const [url, engine] of [['/up-tgt-mathematics/', 'tracker'], ['/up-pgt-english/', 'cards']]) {
      const context = await browser.newContext();
      const { page, evidence } = await fixture(context, url);
      const key = await page.locator('[data-tracker-key]').getAttribute('data-tracker-key');
      assert.ok(key);
      for (const invalid of ['null', '[]', '12', '"text"', '{broken']) {
        await page.evaluate(({ key, invalid }) => localStorage.setItem(key, invalid), { key, invalid });
        await page.reload({ waitUntil: 'load' });
        await page.evaluate(() => { const checkbox = document.querySelector('.topic-check'); checkbox.checked = true; checkbox.dispatchEvent(new Event('change')); });
        assert.equal(await page.locator('.topic.done').count(), 1, invalid);
      }
      const other = await fixture(context, url);
      await page.evaluate(() => { const checkbox = document.querySelector('.topic-check'); checkbox.checked = false; checkbox.dispatchEvent(new Event('change')); });
      await other.page.waitForFunction(() => document.querySelectorAll('.topic.done').length === 0);
      await page.addScriptTag({ content: fs.readFileSync(path.join(ROOT, 'assets/js/up-tgt-pgt-' + engine + '.js'), 'utf8') });
      const head = page.locator('.section-head').first();
      const previous = await head.getAttribute('aria-expanded');
      await head.click();
      assert.notEqual(await head.getAttribute('aria-expanded'), previous, 'duplicate initialization must not toggle twice');
      await other.page.evaluate(key => localStorage.removeItem(key), key);
      await page.waitForFunction(() => document.querySelectorAll('.topic.done').length === 0);
      assert.deepEqual(evidence.errors, []);
      assert.deepEqual(other.evidence.errors, []);
      await context.close();
    }
  } finally { await browser.close(); }
});

test('progress remains usable when browser writes are denied', { timeout: 90000 }, async () => {
  const browser = await chromium.launch();
  try {
    for (const url of ['/up-tgt-mathematics/', '/up-pgt-english/']) {
      const context = await browser.newContext();
      await context.addInitScript(() => { Storage.prototype.setItem = () => { throw new DOMException('Quota exceeded', 'QuotaExceededError'); }; });
      const { page, evidence } = await fixture(context, url);
      await page.evaluate(() => { const checkbox = document.querySelector('.topic-check'); checkbox.checked = true; checkbox.dispatchEvent(new Event('change')); });
      assert.equal(await page.locator('.topic.done').count(), 1);
      const counter = page.locator('#doneCount, #completedCount, #doneStat').first();
      assert.equal(await counter.textContent(), '1');
      const filter = page.locator('#progressFilters [data-progress="done"]');
      await filter.click();
      assert.equal(await page.locator('.topic:not([hidden])').count(), 1);
      assert.equal(await filter.getAttribute('aria-pressed'), 'true');
      assert.deepEqual(evidence.errors, []);
      await context.close();
    }
  } finally { await browser.close(); }
});

test('GK submission stops its timer, delayed ticks expire accurately and duplicate quiz clicks score once', { timeout: 90000 }, async () => {
  const browser = await chromium.launch();
  const context = await browser.newContext();
  try {
    const { page, evidence } = await fixture(context, gk);
    await page.clock.install();
    await page.locator('#tab-btn-quiz').click();
    await page.evaluate(() => {
      const quiz = document.documentElement.lang === 'hi' ? JSON.parse(document.getElementById('bilingual-data').textContent).quiz : JSON.parse(document.getElementById('quiz-data').textContent);
      const option = document.querySelector('[data-quiz="0"][data-option="' + quiz[0].correct_index + '"]');
      option.click(); option.dispatchEvent(new Event('click'));
    });
    const score = await page.locator('#quiz-score').textContent();
    assert.match(score, /^(स्कोर|Score): 1 \/ /);
    await page.locator('#tab-btn-test').click();
    await page.clock.runFor(2000);
    await page.locator('#btn-submit-test').click();
    const stopped = await page.locator('#test-timer').textContent();
    await page.clock.runFor(5000);
    assert.equal(await page.locator('#test-timer').textContent(), stopped);
    assert.equal(await page.locator('#quiz-score').textContent(), score);
    await page.reload({ waitUntil: 'load' });
    await page.locator('#tab-btn-test').click();
    await page.clock.fastForward(601000);
    assert.equal(await page.locator('#test-timer').textContent(), '00:00');
    assert.equal(await page.locator('#test-result').evaluate(el => el.classList.contains('hidden')), false);
    assert.deepEqual(evidence.errors, []);
    assert.deepEqual(evidence.missing, []);
  } finally { await browser.close(); }
});

test('GK late initialization and language switching work with storage denied', { timeout: 90000 }, async () => {
  const browser = await chromium.launch();
  const context = await browser.newContext();
  try {
    await context.addInitScript(() => {
      Storage.prototype.getItem = () => { throw new DOMException('Storage denied', 'SecurityError'); };
      Storage.prototype.setItem = () => { throw new DOMException('Storage denied', 'SecurityError'); };
    });
    const { page, evidence } = await fixture(context, gk);
    assert.equal(await page.locator('html').getAttribute('lang'), 'hi');
    await Promise.all([page.waitForURL('**?lang=en'), page.locator('#btn-language-toggle').click()]);
    await page.waitForLoadState('load');
    assert.equal(await page.locator('html').getAttribute('lang'), 'en');
    assert.deepEqual(evidence.errors, []);
    const late = await context.newPage();
    const lateEvidence = await routeRepositoryFixtures(late, { root: ROOT, files });
    await late.route(/\/assets\/js\/up-tgt-pgt-gk-(?:language|topic)/, route => route.fulfill({ contentType: 'text/javascript', body: '' }));
    await late.goto('https://sjmaths.com' + gk, { waitUntil: 'load' });
    assert.equal(await late.locator('body').getAttribute('data-gk-topic-ready'), null);
    await late.addScriptTag({ content: fs.readFileSync(path.join(ROOT, 'assets/js/up-tgt-pgt-gk-language.js'), 'utf8') });
    await late.addScriptTag({ content: fs.readFileSync(path.join(ROOT, 'assets/js/up-tgt-pgt-gk-topic.js'), 'utf8') });
    assert.equal(await late.locator('body').getAttribute('data-gk-topic-ready'), 'true');
    await late.locator('#tab-btn-test').click();
    await late.locator('#btn-submit-test').click();
    assert.equal(await late.locator('#test-result').evaluate(el => el.classList.contains('hidden')), false);
    assert.deepEqual(lateEvidence.errors, []);
  } finally { await browser.close(); }
});

test('GK theme toggle follows changes from the shared theme controller', { timeout: 60000 }, async () => {
  const browser = await chromium.launch();
  const context = await browser.newContext();
  try {
    await context.addInitScript(() => {
      let preference = 'light';
      window.SJMathsTheme = {
        getPreference: () => preference,
        setPreference(next) {
          preference = next;
          window.dispatchEvent(new CustomEvent('sjmaths:themechange', { detail: { preference, theme: preference, isDark: preference === 'dark' } }));
        },
      };
    });
    const { page, evidence } = await fixture(context, gk);
    await page.evaluate(() => window.SJMathsTheme.setPreference('dark'));
    await page.locator('#btn-theme-toggle').click();
    assert.equal(await page.evaluate(() => window.SJMathsTheme.getPreference()), 'light');
    assert.equal(await page.locator('#btn-theme-toggle').getAttribute('aria-pressed'), 'false');
    assert.deepEqual(evidence.errors, []);
  } finally { await browser.close(); }
});

test('all specialized tracker filters select the matching syllabus cards', { timeout: 120000 }, async () => {
  const browser = await chromium.launch();
  const context = await browser.newContext({ viewport: { width: 1280, height: 844 } });
  try {
    for (const [subject, filter, cardKey] of [
      ['biology', 'branch', 'branch'], ['chemistry', 'branch', 'branch'],
      ['civics', 'section', 'officialSection'], ['economics', 'area', 'area'],
      ['geography', 'unit', 'unit'], ['physics', 'unit', 'unit'],
      ['psychology', 'unit', 'unit'], ['military-science', 'point', 'point'],
    ]) {
      const { page, evidence } = await fixture(context, '/up-pgt-' + subject + '/');
      const choices = await page.locator('#' + filter + 'Filters button').evaluateAll(buttons => buttons.map(button => ({ value: button.dataset[Object.keys(button.dataset)[0]], label: button.textContent })));
      for (const choice of choices) {
        const button = page.locator('#' + filter + 'Filters [data-' + filter + '="' + choice.value + '"]');
        await button.click();
        const visible = await page.locator('.section-card:not([hidden])').evaluateAll((cards, key) => cards.map(card => card.dataset[key]), cardKey);
        assert.ok(visible.length > 0, subject + ': ' + choice.label);
        assert.ok(choice.value === 'all' || visible.every(value => value === choice.value), subject + ': ' + choice.label);
        assert.equal(await button.getAttribute('aria-pressed'), 'true');
      }
      assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 2), subject + ' overflow');
      assert.deepEqual(evidence.errors, []);
      await page.close();
    }
  } finally { await browser.close(); }
});
