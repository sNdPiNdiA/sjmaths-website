const assert = require('node:assert/strict');
const { chromium } = require('playwright');

(async () => {
  try {
    const browser = await chromium.launch({ headless: true });
    
    const testPages = [
      'http://localhost:8082/up-pgt-biology/botany/angiosperms/index.html',
      'http://localhost:8082/up-pgt-civics/section-a/introduction-to-civics/index.html',
      'http://localhost:8082/up-pgt-education/educational-technology/index.html'
    ];

    for (const testUrl of testPages) {
      for (const width of [1280, 390]) {
        console.log(`\n=== Testing UP PGT Page (${testUrl.split('/').slice(-3).join('/')}) at Viewport: ${width}px ===`);
        const context = await browser.newContext({ viewport: { width, height: 800 }, reducedMotion: 'reduce' });
        const page = await context.newPage();

        await page.addInitScript(() => {
          sessionStorage.setItem('sj_auth_gate_skipped', 'true');
          localStorage.setItem('sj_user_logged_in', 'true');
        });

        const errors = [];
        page.on('console', msg => { if (msg.type() === 'error') errors.push(msg.text()); });
        page.on('pageerror', err => errors.push(err.message));

        const res = await page.goto(testUrl, { waitUntil: 'domcontentloaded' });
        assert.equal(res.status(), 200, 'Page returned HTTP 200');

        await page.waitForTimeout(300);

        // Verify external stylesheet is linked and loaded
        await page.waitForFunction(() => {
          const link = document.querySelector('link[data-up-pgt-style="topic"]');
          return link && link.sheet !== null;
        });
        const isSheetLoaded = await page.evaluate(() => {
          const link = document.querySelector('link[data-up-pgt-style="topic"]');
          return link && link.sheet !== null;
        });
        assert.equal(isSheetLoaded, true, 'UP PGT Topic CSS stylesheet is loaded into document');

        // Verify no remaining inline topic styles in document
        const hasInlineTopicStyle = await page.evaluate(() => {
          const styles = Array.from(document.querySelectorAll('style'));
          return styles.some(s => s.textContent.includes('--brand:#12324a') || s.textContent.includes('--brand: #12324a'));
        });
        assert.equal(hasInlineTopicStyle, false, 'No inline topic style tag remains');

        // Verify CSS variable value resolved
        const brand = await page.evaluate(() => {
          return window.getComputedStyle(document.documentElement).getPropertyValue('--brand').trim();
        });
        assert.equal(brand, '#12324a', 'CSS variable --brand is active and resolved');

        // Verify site header exists and is styled
        const siteHeader = page.locator('.site-header');
        assert.ok(await siteHeader.count() > 0, 'Site header element exists');

        // Verify zero fatal console errors
        const fatalErrors = errors.filter(e => !e.includes('favicon') && !e.includes('adsbygoogle') && !e.includes('pagead') && !e.includes('footer-container') && !e.includes('status of 409'));
        assert.deepEqual(fatalErrors, [], 'No fatal runtime errors');

        console.log(`Passed all tests at ${width}px!`);
        await context.close();
      }
    }
    await browser.close();
    console.log('\n🎉 ALL UP PGT VIEWPORT TESTS PASSED PERFECTLY!');
    process.exit(0);
  } catch (err) {
    console.error('UP PGT TEST ERROR:', err);
    process.exit(1);
  }
})();
