const test = require('node:test');
const assert = require('node:assert/strict');
const path = require('node:path');
const { chromium } = require('playwright');
const { ROOT } = require('./seo-html.cjs');
const { fixtureFiles, routeRepositoryFixtures } = require('./lib/browser-fixture.cjs');

const fixtureRoot = path.resolve(ROOT, process.env.SJ_REFACTOR_FIXTURE_ROOT || '.');
const hubs = [
  'ib/index.html',
  'ib/myp-mathematics/index.html',
  'ib/dp-mathematics/index.html',
  'ib/command-terms/index.html',
];
const interactive = [
  'ib/dp-mathematics/analysis-and-approaches-sl/index.html',
  'ib/myp-mathematics/algebra/index.html',
  'ib/myp-mathematics/geometry-and-trigonometry/index.html',
  'ib/myp-mathematics/statistics-and-probability/index.html',
];

test('IB hubs resolve canonical theme settings across mobile and desktop', { timeout: 90000 }, async t => {
  const browser = await chromium.launch({ headless: true });
  t.after(() => browser.close());
  for (const file of hubs) for (const width of [390, 1280]) {
    const context = await browser.newContext({ viewport: { width, height: 900 }, reducedMotion: 'reduce' });
    try {
      const page = await context.newPage();
      const evidence = await routeRepositoryFixtures(page, { root: fixtureRoot, files: fixtureFiles(fixtureRoot) });
      await page.addInitScript(() => {
        localStorage.setItem('sjmaths.theme.preference', 'dark');
        localStorage.setItem('sjmaths-theme', 'green');
      });
      await page.goto(`https://sjmaths.com/${file}`, { waitUntil: 'domcontentloaded' });
      assert.equal(await page.locator('html').getAttribute('data-theme'), 'dark', file);
      assert.equal(await page.locator('body').evaluate(body => body.classList.contains('dark-mode')), true, file);
      assert.equal(await page.evaluate(() => localStorage.getItem('sjmaths-theme')), 'green', 'palette remains independent');
      assert.deepEqual(evidence.missing, [], `${file} local asset requests resolve`);
    } finally { await context.close(); }
  }
});

test('IB topic theme controls toggle once by pointer and keyboard without palette changes', { timeout: 90000 }, async t => {
  const browser = await chromium.launch({ headless: true });
  t.after(() => browser.close());
  for (const file of interactive) {
    const context = await browser.newContext({ viewport: { width: 390, height: 900 }, reducedMotion: 'reduce' });
    try {
      const page = await context.newPage();
      const evidence = await routeRepositoryFixtures(page, { root: fixtureRoot, files: fixtureFiles(fixtureRoot) });
      await page.addInitScript(() => {
        localStorage.setItem('sjmaths.theme.preference', 'light');
        localStorage.setItem('sjmaths-theme', 'green');
      });
      await page.goto(`https://sjmaths.com/${file}`, { waitUntil: 'domcontentloaded' });
      const toggle = page.locator('#theme-toggle');
      await toggle.waitFor({ state: 'visible' });
      assert.equal(await page.locator('html').getAttribute('data-theme'), 'light', file);
      await toggle.click();
      assert.equal(await page.locator('html').getAttribute('data-theme'), 'dark', `${file} pointer`);
      assert.equal(await toggle.getAttribute('aria-pressed'), 'true', file);
      await toggle.focus();
      await page.keyboard.press('Enter');
      assert.equal(await page.locator('html').getAttribute('data-theme'), 'light', `${file} keyboard`);
      assert.equal(await toggle.getAttribute('aria-pressed'), 'false', file);
      assert.equal(await page.evaluate(() => localStorage.getItem('sjmaths-theme')), 'green', 'palette remains independent');
      await page.evaluate(() => {
        localStorage.setItem('sjmaths.theme.preference', 'system');
        window.dispatchEvent(new StorageEvent('storage', { key: 'sjmaths.theme.preference', newValue: 'system' }));
      });
      await page.emulateMedia({ colorScheme: 'dark' });
      await page.waitForFunction(() => document.documentElement.dataset.theme === 'dark');
      assert.equal(await page.evaluate(() => localStorage.getItem('sjmaths-dark')), 'on', `${file} keeps legacy consumers in sync`);
      assert.equal(await page.evaluate(() => localStorage.getItem('sjmaths-theme')), 'green', 'system changes do not replace the palette');
      assert.deepEqual(evidence.missing, [], `${file} local asset requests resolve`);
    } finally { await context.close(); }
  }
});
