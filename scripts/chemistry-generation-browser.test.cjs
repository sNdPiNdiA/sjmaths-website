const test = require('node:test');
const assert = require('node:assert/strict');
const { chromium } = require('playwright');
const { ROOT, siteFiles } = require('./seo-html.cjs');
const { routeRepositoryFixtures } = require('./lib/browser-fixture.cjs');

test('offline Chemistry generation and translation produce working tabs and expiry without an API call', { timeout: 30000 }, async () => {
  const { renderTopicHtml } = await import('./lib/chemistry-renderer.mjs');
  const { buildCompleteBilingualHtml } = await import('./lib/chemistry-bilingual.mjs');
  const fixture = await import('./fixtures/chemistry.mjs');
  const english = renderTopicHtml(fixture.item, fixture.context, fixture.data);
  const bilingual = buildCompleteBilingualHtml(english, fixture.enData, fixture.hiData, ...[fixture.data.quiz, fixture.data.pyq_patterns, fixture.data.topic_test].map(fixture.translatedQuestions));
  const url = 'https://sjmaths.com' + fixture.item.url;
  const files = siteFiles();
  const browser = await chromium.launch({ headless: true });
  try {
    for (const [html, isBilingual] of [[english, false], [bilingual, true]]) {
      const context = await browser.newContext({ viewport: { width: 390, height: 900 }, reducedMotion: 'reduce', serviceWorkers: 'block' });
      try {
        const page = await context.newPage();
        const evidence = await routeRepositoryFixtures(page, { root: ROOT, files });
        await page.route(url, route => route.fulfill({ contentType: 'text/html', body: html }));
        await page.goto(url);
        await page.clock.install();
        assert.equal(await page.locator('.quiz-question-card').count(), 20);
        assert.equal(await page.locator('.pyq-card').count(), 6);
        assert.equal(await page.locator('.test-question-card').count(), 10);
        const tabs = page.locator('.tab-btn');
        for (let i = 0; i < 5; i++) {
          await tabs.nth(i).focus(); await page.keyboard.press('Enter');
          assert.equal(await tabs.nth(i).getAttribute('aria-selected'), 'true');
        }
        if (isBilingual) {
          await page.locator('#btn-lang-toggle').click();
          assert.equal(await page.locator('html').getAttribute('data-lang'), 'hi');
          await tabs.nth(0).click();
          assert.match(await page.locator('#tab-notes').innerText(), /मूल बिंदु A/);
        } else assert.equal(await page.locator('#btn-lang-toggle').count(), 0);
        await tabs.nth(4).click();
        await page.locator('#btnStartTest').click();
        await page.clock.runFor(600000);
        assert.equal(await page.locator('#timerDisplay').innerText(), '00:00');
        assert.equal(await page.locator('#testResultModal').isVisible(), true);
        assert.equal(await page.locator('#resFinalScore').innerText(), '0');
        await page.clock.runFor(1000);
        assert.equal(await page.locator('#timerDisplay').innerText(), '00:00');
        assert.deepEqual(evidence.errors, []);
        assert.deepEqual(evidence.missing, []);
      } finally { await context.close(); }
    }
  } finally { await browser.close(); }
});
