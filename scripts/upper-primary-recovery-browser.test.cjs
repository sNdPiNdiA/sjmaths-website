const test = require('node:test');
const assert = require('node:assert/strict');
const path = require('node:path');
const { chromium } = require('playwright');
const { ROOT } = require('./seo-html.cjs');
const { fixtureFiles, routeRepositoryFixtures } = require('./lib/browser-fixture.cjs');

test('recovered Upper Primary pages load cleanly, fit mobile, and keep bilingual quiz/test content', { timeout: 90000 }, async () => {
  const fixtureRoot = path.resolve(ROOT, process.env.SJ_REFACTOR_FIXTURE_ROOT || '.');
  const files = fixtureFiles(fixtureRoot);
  const route = '/up-upper-primary-teacher/science/cell-structure-to-organ-systems/';
  const browser = await chromium.launch({ headless: true });
  try {
    for (const width of [390, 1280]) {
      const context = await browser.newContext({ viewport: { width, height: 900 }, reducedMotion: 'reduce' });
      try {
        const page = await context.newPage();
        const evidence = await routeRepositoryFixtures(page, { root: fixtureRoot, files });
        await page.goto(`https://sjmaths.com${route}`, { waitUntil: 'domcontentloaded' });
        const skip = page.locator('#sj-skip-gate-btn');
        if (await page.locator('script[src*="require-auth"]').count()) {
          await skip.waitFor({ state: 'visible', timeout: 20000 });
          await skip.click();
          await page.locator('#sj-auth-overlay').waitFor({ state: 'hidden' });
        }
        assert.equal(await page.locator('html').count(), 1);
        assert.equal(await page.locator('body').count(), 1);
        assert.equal(await page.locator('h1').count(), 1);
        assert.equal(await page.locator('#mcq-card-0').count(), 1);
        assert.equal(await page.locator('#langToggleBtn').count(), 1);
        assert.equal(await page.locator('#testSubmitBtn').count(), 1);
        assert.ok(await page.evaluate(() => window.TOPIC_STORAGE_KEY && window.TOPIC_CHECKBOX_ID));
        await page.locator('#langToggleBtn').focus();
        await page.keyboard.press('Enter');
        assert.ok(await page.locator('body').evaluate(body => body.classList.contains('lang-mode-hi')));
        await page.locator('.study-tab-btn[data-tab="test"]').click();
        await page.locator('.start-test-btn').click();
        assert.match(await page.locator('#testQuestionContainer').innerText(), /Which|क्या|निम्न/);
        assert.equal(await page.evaluate(() => window.testData.length), 10);
        for (let question = 1; question < 10; question++) await page.locator('#testNextBtn').click();
        await page.locator('#testSubmitBtn').click();
        assert.ok(await page.locator('#miniTestResult').isVisible());
        assert.deepEqual(evidence.errors, []);
        assert.deepEqual(evidence.missing, []);
        assert.equal(await page.evaluate(() => Math.max(0, document.documentElement.scrollWidth - innerWidth)), 0);
      } finally { await context.close(); }
    }
  } finally { await browser.close(); }
});
