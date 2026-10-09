const assert = require('node:assert/strict');
const { chromium } = require('playwright');

(async () => {
  try {
    const browser = await chromium.launch({ headless: true });
    for (const width of [1280, 390]) {
      console.log(`\n=== Testing UPSC APFC Lesson at Viewport Width: ${width}px ===`);
      const context = await browser.newContext({ viewport: { width, height: 800 } });
      const page = await context.newPage();

      await page.addInitScript(() => {
        sessionStorage.setItem('sj_auth_gate_skipped', 'true');
        localStorage.setItem('sj_user_logged_in', 'true');
      });

      const errors = [];
      page.on('console', msg => { if (msg.type() === 'error') errors.push(msg.text()); });
      page.on('pageerror', err => errors.push(err.message));

      const testUrl = 'http://localhost:8082/upsc-apfc/accountancy/accounting-concepts-and-principles/';
      const res = await page.goto(testUrl, { waitUntil: 'domcontentloaded' });
      assert.equal(res.status(), 200, 'Page returned HTTP 200');

      await page.waitForTimeout(500);

      // Verify external stylesheet is linked and loaded
      const linkLocator = page.locator('link[data-apfc-style="lesson"]');
      assert.equal(await linkLocator.count(), 1, 'UPSC APFC lesson CSS is linked once');
      const isSheetLoaded = await linkLocator.evaluate(el => el.sheet !== null);
      assert.equal(isSheetLoaded, true, 'CSS stylesheet is loaded into document');

      // Verify computed styles match exact design tokens and responsive breakpoints
      const bookPage = page.locator('.book-page').first();
      const maxWidth = await bookPage.evaluate(el => window.getComputedStyle(el).maxWidth);
      assert.equal(maxWidth, '920px', 'Book page max-width matches 920px');

      const bookIntro = page.locator('.book-intro').first();
      const introPadding = await bookIntro.evaluate(el => window.getComputedStyle(el).padding);
      const expectedPadding = width === 1280 ? '22px 20px' : '18px 15px';
      assert.equal(introPadding, expectedPadding, `Intro padding matches ${expectedPadding} for width ${width}`);

      const bookConcept = page.locator('.book-concept').first();
      const conceptMargin = await bookConcept.evaluate(el => window.getComputedStyle(el).marginBottom);
      assert.equal(conceptMargin, '0px', 'Concept margin is 0px');

      // Verify zero unexpected console errors
      const fatalErrors = errors.filter(e => !e.includes('favicon') && !e.includes('adsbygoogle') && !e.includes('pagead') && !e.includes('footer-container'));
      assert.deepEqual(fatalErrors, [], 'No fatal runtime errors');

      await page.screenshot({ path: `scratch/apfc-after-${width}.png` });
      console.log(`Passed all tests at ${width}px!`);
      await context.close();
    }
    await browser.close();
    console.log('\n🎉 ALL UPSC APFC VIEWPORT TESTS PASSED PERFECTLY!');
  } catch (err) {
    console.error('UPSC APFC TEST ERROR:', err);
    process.exit(1);
  }
})();
