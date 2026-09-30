// Local test-interface checks; auth, analytics and external MathJax are excluded.
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const cheerio = require('cheerio');
const { chromium } = require('playwright');
const { ROOT, siteFiles } = require('./seo-html.cjs');
const { createResolver } = require('./seo-routes.cjs');
const { routeRepositoryFixtures } = require('./lib/browser-fixture.cjs');
const { units } = require('./data/class-9-unit-tests.cjs');
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
test('all twelve papers score MCQs, label written assessment and review step-wise answers on mobile and desktop', { timeout: 120000 }, async () => {
  const browser = await chromium.launch({ headless: true });
  try {
    for (const width of [390, 1366]) {
      const context = await browser.newContext({ viewport: { width, height: 850 }, serviceWorkers: 'block', reducedMotion: 'reduce' });
      try {
        const page = await context.newPage();
        const evidence = await prepare(page);
        for (const unit of units) for (const paper of unit.tests) {
          await page.goto(`https://sjmaths.com/class-9-maths/tests/unit-wise/${unit.folder}/test-${paper.paper}`);
          await page.waitForFunction(() => document.documentElement.classList.contains('unit-test-ready'));
          assert.equal(await page.locator('#questionPalette button').count(), paper.questions.length);
          assert.equal(await page.locator('#inputArea button').count(), 4);
          assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1));
          const first = paper.questions[0];
          await page.locator('#inputArea button').nth(first.correctOption).focus();
          await page.keyboard.press('Enter');
          assert.equal(await page.locator('#inputArea button').nth(first.correctOption).getAttribute('aria-pressed'), 'true');
          await page.reload();
          await page.waitForFunction(() => document.documentElement.classList.contains('unit-test-ready'));
          assert.equal(await page.locator('#inputArea button.selected').count(), 1);
          if (width <= 768) {
            assert.equal(await page.locator('#paletteBody').isVisible(), false);
            await page.locator('#paletteToggle').click();
            assert.equal(await page.locator('#paletteToggle').getAttribute('aria-expanded'), 'true');
            assert.equal(await page.locator('#paletteBody').isVisible(), true);
          }
          for (let i = 0; i < paper.questions.length; i++) {
            await page.locator('#palette-' + i).click();
            const q = paper.questions[i];
            if (q.type === 'mcq') await page.locator('#inputArea button').nth(q.correctOption).click();
            else await page.locator('#inputArea textarea').fill('Written reasoning for teacher review.');
          }
          await page.locator('#btnNext').click();
          const autoMarks = paper.questions.filter(q => q.type === 'mcq').reduce((n, q) => n + q.marks, 0);
          assert.equal(await page.locator('.score-text').textContent(), `${autoMarks} / ${autoMarks}`);
          assert.match(await page.locator('#resultMessage').textContent(), /Written questions.*teacher assessment/);
          assert.equal(await page.locator('#timerDisplay').textContent(), 'Finished');
          await page.locator('#resultModal button').click();
          assert.equal(await page.locator('#solutionArea ol li').count(), paper.questions.at(-1).solutionSteps.length);
          assert.equal(await page.locator('#inputArea textarea').getAttribute('readonly'), '');
          if (width <= 768) {
            await page.locator('#paletteToggle').click();
            assert.equal(await page.locator('#paletteBody').isVisible(), false);
            assert.ok(await page.locator('#paletteToggle').isVisible());
          }
          if (width === 390 && unit.number === 6 && paper.paper === 2) {
            fs.mkdirSync(path.join(ROOT, 'scratch'), { recursive: true });
            await page.screenshot({ path: path.join(ROOT, 'scratch/class-9-current-unit-test-mobile.png') });
          }
        }
        // Reset is scoped to this versioned paper, and restarts timer/state.
        page.once('dialog', dialog => dialog.accept());
        await Promise.all([page.waitForEvent('load'), page.locator('#btnReset').click()]);
        await page.waitForFunction(() => document.documentElement.classList.contains('unit-test-ready'));
        assert.equal(await page.locator('#inputArea button.selected').count(), 0);
        assert.equal(await page.locator('#resultModal').isVisible(), false);
        assert.equal(await page.locator('#qNumber').textContent(), 'Question 1');
        await page.goto('https://sjmaths.com/class-9-maths/tests/unit-wise/');
        assert.equal(await page.locator('.syllabus-unit').count(), 6);
        assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1));
        await page.goto('https://sjmaths.com/class-9-maths/previous-syllabus/unit-tests/unit-1-number-systems/test-1');
        await page.waitForSelector('.mcq-option');
        assert.match(await page.locator('.test-header .logo').textContent(), /Earlier Paper/);
        assert.deepEqual(evidence.missing, []);
        assert.deepEqual(evidence.errors, []);
      } finally { await context.close(); }
    }
    const context = await browser.newContext({ javaScriptEnabled: false, viewport: { width: 390, height: 850 } });
    try {
      const page = await context.newPage();
      await prepare(page);
      await page.goto('https://sjmaths.com/class-9-maths/tests/unit-wise/unit-4-geometry/test-2');
      assert.ok(await page.locator('#source-paper').isVisible());
      assert.equal(await page.locator('.source-question').count(), units[3].tests[1].questions.length);
      assert.ok(await page.locator('.source-question').last().isVisible());
      await page.locator('.source-question').last().locator('summary').click();
      assert.ok(await page.locator('.source-question').last().locator('details > ol').isVisible());
      assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1));
    } finally { await context.close(); }
  } finally { await browser.close(); }
});
