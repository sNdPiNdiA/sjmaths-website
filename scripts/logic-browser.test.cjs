const assert = require('node:assert/strict');
const { chromium } = require('playwright');

(async () => {
  try {
    const browser = await chromium.launch({ headless: true });
    for (const width of [1280, 390]) {
      console.log(`\n=== Testing Logic Study Guide at Viewport Width: ${width}px ===`);
      const context = await browser.newContext({ viewport: { width, height: 800 }, reducedMotion: 'reduce' });
      const page = await context.newPage();

      await page.addInitScript(() => {
        sessionStorage.setItem('sj_auth_gate_skipped', 'true');
        localStorage.setItem('sj_user_logged_in', 'true');
      });

      const errors = [];
      page.on('console', msg => { if (msg.type() === 'error') errors.push(msg.text()); });
      page.on('pageerror', err => errors.push(err.message));

      const testUrl = 'http://localhost:8082/logic/deductive-arguments/categorical-syllogism/fallacies/';
      const res = await page.goto(testUrl, { waitUntil: 'domcontentloaded' });
      assert.equal(res.status(), 200, 'Page returned HTTP 200');

      await page.waitForTimeout(400);

      // Verify external stylesheet is linked and loaded
      await page.waitForFunction(() => {
        const link = document.querySelector('link[data-study-guide-style="logic"]');
        return link && link.sheet !== null;
      });
      const isSheetLoaded = await page.evaluate(() => {
        const link = document.querySelector('link[data-study-guide-style="logic"]');
        return link && link.sheet !== null;
      });
      assert.equal(isSheetLoaded, true, 'Logic Topic CSS stylesheet is loaded into document');

      // Verify no remaining inline style elements
      const inlineStyleCount = await page.evaluate(() => {
        return document.querySelectorAll('style').length;
      });
      assert.equal(inlineStyleCount, 0, 'No inline style tags remain in head/body');

      // Verify computed kicker color matches --accent (#6366f1 -> rgb(99, 102, 241))
      const kickerColor = await page.locator('.kicker').evaluate(el => window.getComputedStyle(el).color);
      assert.equal(kickerColor, 'rgb(99, 102, 241)', 'Kicker color matches accent indigo');

      // Verify card styling
      const cardRadius = await page.locator('.card').first().evaluate(el => window.getComputedStyle(el).borderRadius);
      assert.equal(cardRadius, '18px', 'Card border radius is 18px');

      // Verify responsive layout
      const gridCols = await page.locator('.main-grid').evaluate(el => window.getComputedStyle(el).gridTemplateColumns);
      const sidebarPos = await page.locator('.sidebar-card').evaluate(el => window.getComputedStyle(el).position);

      if (width === 1280) {
        assert.ok(gridCols.includes('340px'), 'Main grid has 340px sidebar column on desktop');
        assert.equal(sidebarPos, 'sticky', 'Sidebar card is sticky on desktop');
      } else {
        assert.equal(sidebarPos, 'static', 'Sidebar card is static on mobile');
      }

      // Verify zero fatal console errors
      const fatalErrors = errors.filter(e => !e.includes('favicon') && !e.includes('adsbygoogle') && !e.includes('pagead') && !e.includes('footer-container'));
      assert.deepEqual(fatalErrors, [], 'No fatal runtime errors');

      console.log(`Passed all tests at ${width}px!`);
      await context.close();
    }
    await browser.close();
    console.log('\n🎉 ALL LOGIC VIEWPORT TESTS PASSED PERFECTLY!');
  } catch (err) {
    console.error('LOGIC TEST ERROR:', err);
    process.exit(1);
  }
})();
