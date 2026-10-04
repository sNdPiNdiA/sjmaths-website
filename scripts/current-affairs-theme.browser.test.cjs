const test = require('node:test');
const assert = require('node:assert/strict');
const path = require('node:path');
const { chromium } = require('playwright');
const { ROOT } = require('./seo-html.cjs');
const { fixtureFiles, routeRepositoryFixtures } = require('./lib/browser-fixture.cjs');

const fixtureRoot = path.resolve(ROOT, process.env.SJ_REFACTOR_FIXTURE_ROOT || '.');
const files = fixtureFiles(fixtureRoot);
const pages = [
  ['current-affairs/index.html', 'sjmathsCurrentAffairsHub'],
  ['current-affairs/weekly/index.html', 'sjmathsNewWeeklyLayout'],
  ['current-affairs/monthly/index.html', 'sjmathsMonthlyCurrentAffairsDashboard'],
  ['current-affairs/bimonthly/index.html', 'sjmathsBimonthlyCurrentAffairsDashboard'],
];

test('Current Affairs themes follow the shared preference and persist page state without double toggles', { timeout: 120000 }, async t => {
  const browser = await chromium.launch({ headless: true });
  t.after(() => browser.close());
  for (const [file, stateKey] of pages) for (const width of [390, 1280]) {
    const context = await browser.newContext({ viewport: { width, height: 900 }, reducedMotion: 'reduce' });
    try {
      const page = await context.newPage();
      const evidence = await routeRepositoryFixtures(page, { root: fixtureRoot, files });
      await page.route('**/assets/js/require-auth.min.js*', route => route.fulfill({ contentType: 'text/javascript', body: '' }));
      await page.addInitScript(key => {
        localStorage.setItem('sjmaths.theme.preference', 'light');
        localStorage.setItem('sjmaths-theme', 'green');
        localStorage.setItem(key, JSON.stringify({ theme: 'dark' }));
      }, stateKey);
      await page.goto(`https://sjmaths.com/${file}`, { waitUntil: 'domcontentloaded' });
      await page.waitForFunction(key => {
        try { return JSON.parse(localStorage.getItem(key) || '{}').theme === 'light'; }
        catch { return false; }
      }, stateKey);

      const toggle = page.locator('#themeToggle');
      await toggle.waitFor({ state: 'visible' });
      assert.equal(await page.locator('html').getAttribute('data-theme'), 'light', file);
      assert.equal(await page.evaluate(key => JSON.parse(localStorage.getItem(key)).theme, stateKey), 'light', `${file} saved theme sync`);
      const errorsBeforeToggle = [...evidence.errors];
      if (width === 390) {
        await toggle.scrollIntoViewIfNeeded();
        const hitTarget = await toggle.evaluate(element => {
          const rect = element.getBoundingClientRect();
          const hit = document.elementFromPoint(rect.left + rect.width / 2, rect.top + rect.height / 2);
          return { target: hit?.id || hit?.className || hit?.tagName, isToggle: hit === element || element.contains(hit) };
        });
        assert.equal(hitTarget.isToggle, true, `${file} mobile theme button is covered by ${hitTarget.target}`);
        await toggle.click();
      } else {
        await toggle.click();
      }
      await page.waitForFunction(() => document.documentElement.dataset.theme === 'dark');
      await page.waitForFunction(key => JSON.parse(localStorage.getItem(key) || '{}').theme === 'dark', stateKey);
      assert.equal(await page.evaluate(() => localStorage.getItem('sjmaths.theme.preference')), 'dark', `${file} canonical preference`);
      assert.equal(await page.evaluate(() => localStorage.getItem('sjmaths-theme')), 'green', `${file} palette remains independent`);
      assert.deepEqual(evidence.missing, [], `${file} local assets resolve`);
      assert.deepEqual(evidence.errors, errorsBeforeToggle, `${file} toggle adds no browser errors`);
    } finally { await context.close(); }
  }
});
