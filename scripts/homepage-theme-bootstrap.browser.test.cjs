const test = require('node:test');
const assert = require('node:assert/strict');
const path = require('node:path');
const { chromium } = require('playwright');
const { ROOT } = require('./seo-html.cjs');
const { fixtureFiles, routeRepositoryFixtures } = require('./lib/browser-fixture.cjs');

const fixtureRoot = path.resolve(ROOT, process.env.SJ_REFACTOR_FIXTURE_ROOT || '.');
const pages = ['index.html', 'pages/index.html', 'competitive-exams/index.html'];

test('homepage theme bootstraps follow the canonical setting and preserve palettes', { timeout: 90000 }, async t => {
  const browser = await chromium.launch({ headless: true });
  t.after(() => browser.close());
  for (const file of pages) for (const width of [390, 1280]) {
    const context = await browser.newContext({ viewport: { width, height: 900 }, reducedMotion: 'reduce' });
    try {
      const page = await context.newPage();
      const evidence = await routeRepositoryFixtures(page, { root: fixtureRoot, files: fixtureFiles(fixtureRoot) });
      await page.route('**/assets/js/require-auth.min.js*', route => route.fulfill({ contentType: 'text/javascript', body: '' }));
      await page.addInitScript(() => {
        localStorage.setItem('sjmaths.theme.preference', 'dark');
        localStorage.setItem('sjmaths-theme', 'green');
      });
      await page.goto(`https://sjmaths.com/${file}`, { waitUntil: 'domcontentloaded' });
      assert.equal(await page.locator('html').getAttribute('data-theme'), 'dark', file);
      assert.equal(await page.locator('html').getAttribute('data-theme-preference'), 'dark', file);
      assert.equal(await page.locator('body').evaluate(body => body.classList.contains('dark-mode')), true, file);
      assert.equal(await page.evaluate(() => localStorage.getItem('sjmaths-theme')), 'green', `${file} palette`);

      if (width === 390) {
        const mobileMenuButton = page.locator('.mobile-toggle');
        await mobileMenuButton.waitFor({ state: 'visible' });
        await mobileMenuButton.click();
        await page.waitForFunction(() => document.querySelector('#primary-navigation')?.classList.contains('active'));
        assert.equal(await page.locator('#primary-navigation').evaluate(nav => getComputedStyle(nav).position), 'fixed', `${file} mobile menu overlays the viewport`);
        assert.equal(await page.locator('#primary-navigation').isVisible(), true, `${file} mobile menu is visible`);
        await page.keyboard.press('Escape');
        await page.waitForFunction(() => !document.querySelector('#primary-navigation')?.classList.contains('active'));
      }

      const toggle = page.locator('#darkToggle');
      await toggle.waitFor({ state: 'visible' });
      await page.waitForFunction(() => window.SJMathsTheme?.getPreference() === 'dark'
        && document.querySelector('#darkToggle')?.getAttribute('aria-pressed') === 'true');
      await toggle.click();
      assert.equal(await page.locator('html').getAttribute('data-theme'), 'light', `${file} pointer toggle`);
      assert.equal(await toggle.getAttribute('aria-pressed'), 'false', `${file} accessible toggle state`);
      assert.equal(await page.evaluate(() => localStorage.getItem('sjmaths-theme')), 'green', `${file} keeps palette on toggle`);
      assert.deepEqual(evidence.missing, [], `${file} local assets`);
      assert.equal(await page.evaluate(() => Math.max(0, document.documentElement.scrollWidth - innerWidth)), 0, `${file} overflow at ${width}px`);
    } finally { await context.close(); }
  }
});
