const assert = require('node:assert/strict');
const { chromium } = require('playwright');

(async () => {
  try {
    const browser = await chromium.launch({ headless: true });
    for (const width of [1280, 390]) {
      console.log(`\n=== Testing AHC RO/ARO Table at Viewport Width: ${width}px ===`);
      const context = await browser.newContext({ viewport: { width, height: 800 }, reducedMotion: 'reduce' });
      const page = await context.newPage();

      await page.addInitScript(() => {
        sessionStorage.setItem('sj_auth_gate_skipped', 'true');
        localStorage.setItem('sj_user_logged_in', 'true');
      });

      const errors = [];
      page.on('console', msg => { if (msg.type() === 'error') errors.push(msg.text()); });
      page.on('pageerror', err => errors.push(err.message));

      const testUrl = 'http://localhost:8082/ahc-ro-aro/agriculture-commerce-trade/types-of-farming/';
      const res = await page.goto(testUrl, { waitUntil: 'domcontentloaded' });
      assert.equal(res.status(), 200, 'Page returned HTTP 200');

      await page.waitForTimeout(400);

      // Verify external stylesheet is linked and loaded
      await page.waitForFunction(() => {
        const link = document.querySelector('link[data-table-style="premium"]');
        return link && link.sheet !== null;
      });
      const isSheetLoaded = await page.evaluate(() => {
        const link = document.querySelector('link[data-table-style="premium"]');
        return link && link.sheet !== null;
      });
      assert.equal(isSheetLoaded, true, 'AHC Table CSS stylesheet is loaded into document');

      // Verify computed border-radius across breakpoints
      const container = page.locator('.premium-table-container').first();
      const radius = await container.evaluate(el => window.getComputedStyle(el).borderRadius);
      const expectedRadius = width === 1280 ? '12px' : '8px';
      assert.equal(radius, expectedRadius, `Container border-radius matches ${expectedRadius} at ${width}px`);

      // Verify computed th color
      const th = page.locator('.premium-table th').first();
      const thColor = await th.evaluate(el => window.getComputedStyle(el).color);
      assert.equal(thColor, 'rgb(46, 125, 107)', 'Table header color matches primary theme');

      // Verify zero fatal console errors
      const fatalErrors = errors.filter(e => !e.includes('favicon') && !e.includes('adsbygoogle') && !e.includes('pagead') && !e.includes('footer-container'));
      assert.deepEqual(fatalErrors, [], 'No fatal runtime errors');

      console.log(`Passed all tests at ${width}px!`);
      await context.close();
    }
    await browser.close();
    console.log('\n🎉 ALL AHC RO/ARO VIEWPORT TESTS PASSED PERFECTLY!');
  } catch (err) {
    console.error('AHC RO/ARO TEST ERROR:', err);
    process.exit(1);
  }
})();
