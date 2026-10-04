const test = require('node:test');
const assert = require('node:assert/strict');
const { chromium } = require('playwright');
const { ROOT } = require('./seo-html.cjs');
const { fixtureFiles, routeRepositoryFixtures } = require('./lib/browser-fixture.cjs');

test('Economics shared theme preference works by keyboard without changing palette or study tabs', { timeout: 90000 }, async () => {
  const file = 'economics/economic-systems/index.html';
  const browser = await chromium.launch({ headless: true });
  try {
    for (const width of [390, 1280]) {
      const context = await browser.newContext({ viewport: { width, height: 900 }, reducedMotion: 'reduce', serviceWorkers: 'block' });
      try {
        const page = await context.newPage();
        const evidence = await routeRepositoryFixtures(page, { root: ROOT, files: fixtureFiles(ROOT) });
        await page.addInitScript(() => {
          localStorage.removeItem('sjmaths.theme.preference');
          localStorage.setItem('sjmaths-theme', 'green');
        });
        await page.goto(`https://sjmaths.com/${file}`, { waitUntil: 'load' });
        assert.deepEqual(evidence.errors, []);
        assert.deepEqual(evidence.missing, []);
        assert.equal(await page.locator('.tab-btn').count(), 5);
        const theme = page.locator('#theme-toggle-btn');
        await theme.focus();
        await page.keyboard.press('Enter');
        assert.equal(await page.locator('html').getAttribute('data-theme'), 'dark');
        assert.equal(await page.locator('body').evaluate(body => body.classList.contains('dark-mode')), true);
        assert.equal(await theme.getAttribute('aria-pressed'), 'true');
        assert.equal(await page.evaluate(() => localStorage.getItem('sjmaths.theme.preference')), 'dark');
        assert.equal(await page.evaluate(() => localStorage.getItem('sjmaths-theme')), 'green');
        assert.equal(await page.evaluate(() => Math.max(0, document.documentElement.scrollWidth - innerWidth)), 0);
        await page.locator('.tab-btn[data-tab="tab-quiz"]').click();
        assert.equal(await page.locator('#tab-quiz').evaluate(panel => panel.classList.contains('active')), true);
        await theme.click();
        assert.equal(await page.locator('html').getAttribute('data-theme'), 'light');
        assert.equal(await theme.getAttribute('aria-pressed'), 'false');
        assert.deepEqual(evidence.errors, []);
      } finally { await context.close(); }
    }
  } finally { await browser.close(); }
});
