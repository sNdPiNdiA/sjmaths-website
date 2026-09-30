// Repository fixtures: Firebase authentication, global chrome and analytics excluded.
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const cheerio = require('cheerio');
const { chromium } = require('playwright');
const { ROOT, siteFiles } = require('./seo-html.cjs');
const { createResolver } = require('./seo-routes.cjs');
const { routeRepositoryFixtures } = require('./lib/browser-fixture.cjs');
const { worksheets } = require('./data/class-9-worksheets.cjs');
const files = siteFiles();
const resolve = createResolver(files);
async function prepare(page) {
  const evidence = await routeRepositoryFixtures(page, { root: ROOT, files });
  await page.route('**/*', async route => {
    const url = new URL(route.request().url());
    if (url.hostname !== 'sjmaths.com') return route.fulfill({ status: 200, body: '', contentType: route.request().resourceType() === 'stylesheet' ? 'text/css' : 'text/javascript' });
    const result = resolve(url.href);
    if (!result.file?.endsWith('.html')) return route.fallback();
    const $ = cheerio.load(fs.readFileSync(path.join(ROOT, result.file), 'utf8'));
    $('script[type="module"], script[src*="googlesyndication"], script[src*="global-header"], script[src*="global-footer"], script[src*="main.min.js"]').remove();
    return route.fulfill({ contentType: 'text/html', body: $.html() });
  });
  return evidence;
}
test('worksheet answers, chapter links and print choices work on mobile, tablet and desktop', { timeout: 180000 }, async () => {
  const browser = await chromium.launch({ headless: true });
  try {
    for (const width of [390, 768, 1366]) {
      const context = await browser.newContext({ viewport: { width, height: 850 }, reducedMotion: 'reduce', serviceWorkers: 'block' });
      try {
        const page = await context.newPage();
        const evidence = await prepare(page);
        await page.goto('https://sjmaths.com/class-9-maths/worksheets/');
        assert.equal(await page.locator('.worksheet-entry').count(), 15);
        assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1));
        await page.locator('#earlier-worksheets summary').click();
        assert.equal(await page.locator('#earlier-worksheets a').count(), files.filter(file => /^class-9-maths\/worksheets\/chapter-[^/]+\/[^/]+\.html$/.test(file)).length);
        for (const sheet of worksheets) {
          const url = 'https://sjmaths.com/class-9-maths/worksheets/current-syllabus/' + sheet.folder + '/';
          await page.goto(url);
          assert.equal(await page.locator('.worksheet-question').count(), sheet.questions.length);
          assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1));
          await page.locator('.worksheet-solution summary').first().click();
          assert.ok(await page.locator('.worksheet-solution > ol').first().isVisible());
          await page.locator('#toggle-sheet-answers').click();
          assert.equal(await page.locator('.worksheet-solution[open]').count(), sheet.questions.length);
          assert.equal(await page.locator('#toggle-sheet-answers').getAttribute('aria-pressed'), 'true');
          await page.locator('#toggle-sheet-answers').click();
          assert.equal(await page.locator('.worksheet-solution[open]').count(), 0);
          await page.locator('.sheet-level-links a[href="#challenge"]').click();
          assert.equal(new URL(page.url()).hash, '#challenge');
          const heading = await page.locator('#challenge h2').boundingBox();
          assert.ok(heading && heading.y >= 0 && heading.y < 850);
          if (sheet.number === 1) {
            await page.locator('.worksheet-solution summary').first().click();
            await page.evaluate(() => { window.print = () => { window.__printCalls = (window.__printCalls || 0) + 1; }; });
            await page.locator('#print-sheet').click();
            await page.emulateMedia({ media: 'print' });
            assert.equal(await page.locator('.worksheet-solution[open]').count(), 0);
            assert.equal(await page.locator('.worksheet-solution').first().isVisible(), false);
            await page.evaluate(() => window.dispatchEvent(new Event('afterprint')));
            await page.emulateMedia({ media: null });
            assert.equal(await page.locator('.worksheet-solution[open]').count(), 1);
            await page.locator('#print-sheet-answers').check();
            await page.locator('#print-sheet').click();
            await page.emulateMedia({ media: 'print' });
            assert.ok(await page.locator('.worksheet-solution > ol').last().isVisible());
            assert.equal(await page.evaluate(() => window.__printCalls), 2);
            await page.evaluate(() => window.dispatchEvent(new Event('afterprint')));
            await page.emulateMedia({ media: null });
            assert.equal(await page.locator('.worksheet-solution[open]').count(), 1);
          }
          if (width === 390 && sheet.number === 10) {
            await page.locator('#toggle-sheet-answers').click();
            await page.locator('#question-ws-10-new-3').scrollIntoViewIfNeeded();
            fs.mkdirSync(path.join(ROOT, 'scratch'), { recursive: true });
            await page.screenshot({ path: path.join(ROOT, 'scratch/class-9-current-worksheet-mobile.png') });
          }
        }
        assert.deepEqual(evidence.missing, []);
        assert.deepEqual(evidence.errors, []);
      } finally { await context.close(); }
    }
    const context = await browser.newContext({ javaScriptEnabled: false, viewport: { width: 390, height: 850 } });
    try {
      const page = await context.newPage();
      await prepare(page);
      await page.goto('https://sjmaths.com/class-9-maths/worksheets/');
      assert.equal(await page.locator('.worksheet-entry').count(), 15);
      await page.locator('.worksheet-entry a').first().click();
      await page.locator('.worksheet-solution summary').first().click();
      assert.ok(await page.locator('.worksheet-solution > ol').first().isVisible());
    } finally { await context.close(); }
  } finally { await browser.close(); }
});
