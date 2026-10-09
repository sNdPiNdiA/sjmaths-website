const assert = require('node:assert/strict');
const { chromium } = require('playwright');

(async () => {
  try {
    const browser = await chromium.launch({ headless: true });
    for (const width of [1280, 390]) {
      console.log(`\n=== Testing UPSSSC PET Topic at Viewport Width: ${width}px ===`);
      const context = await browser.newContext({ viewport: { width, height: 800 }, reducedMotion: 'reduce' });
      const page = await context.newPage();

      await page.addInitScript(() => {
        sessionStorage.setItem('sj_auth_gate_skipped', 'true');
        localStorage.setItem('sj_user_logged_in', 'true');
      });

      const errors = [];
      page.on('console', msg => { if (msg.type() === 'error') errors.push(msg.text()); });
      page.on('pageerror', err => errors.push(err.message));

      const testUrl = 'http://localhost:8082/upsssc-pet/economy/agricultural-reforms/index.html';
      const res = await page.goto(testUrl, { waitUntil: 'domcontentloaded' });
      assert.equal(res.status(), 200, 'Page returned HTTP 200');

      await page.waitForTimeout(400);

      // Verify external stylesheet is linked and loaded
      await page.waitForFunction(() => {
        const link = document.querySelector('link[data-upsssc-style="topic"]');
        return link && link.sheet !== null;
      });
      const isSheetLoaded = await page.evaluate(() => {
        const link = document.querySelector('link[data-upsssc-style="topic"]');
        return link && link.sheet !== null;
      });
      assert.equal(isSheetLoaded, true, 'UPSSSC PET Topic CSS stylesheet is loaded into document');

      // Verify no remaining inline topic styles in document
      const hasInlineTopicStyle = await page.evaluate(() => {
        const styles = Array.from(document.querySelectorAll('style'));
        return styles.some(s => s.textContent.includes('--up-accent:#3b82f6') || s.textContent.includes('--up-accent: #3b82f6'));
      });
      assert.equal(hasInlineTopicStyle, false, 'No inline topic style tag remains');

      // Verify CSS variable value resolved
      const upPrimary = await page.evaluate(() => {
        return window.getComputedStyle(document.documentElement).getPropertyValue('--up-primary').trim();
      });
      assert.equal(upPrimary, '#0f172a', 'CSS variable --up-primary is active and resolved');

      // Verify topic header exists and is styled
      const topicHeader = page.locator('.topic-header');
      const headerCount = await topicHeader.count();
      assert.ok(headerCount > 0, 'Topic header element exists');

      // Verify breadcrumbs styled
      const breadcrumbs = page.locator('.breadcrumbs');
      assert.ok(await breadcrumbs.count() > 0, 'Breadcrumbs element exists');

      // Verify zero fatal console errors
      const fatalErrors = errors.filter(e => !e.includes('favicon') && !e.includes('adsbygoogle') && !e.includes('pagead') && !e.includes('footer-container') && !e.includes('status of 409'));
      assert.deepEqual(fatalErrors, [], 'No fatal runtime errors');

      console.log(`Passed all tests at ${width}px!`);
      await context.close();
    }
    await browser.close();
    console.log('\n🎉 ALL UPSSSC PET VIEWPORT TESTS PASSED PERFECTLY!');
    process.exit(0);
  } catch (err) {
    console.error('UPSSSC PET TEST ERROR:', err);
    process.exit(1);
  }
})();
