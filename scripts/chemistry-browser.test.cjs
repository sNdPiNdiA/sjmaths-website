const assert = require('node:assert/strict');
const { chromium } = require('playwright');

(async () => {
  try {
    const browser = await chromium.launch({ headless: true });
    for (const width of [1280, 390]) {
      console.log(`\n=== Testing Chemistry Topic at Viewport Width: ${width}px ===`);
      const context = await browser.newContext({ viewport: { width, height: 800 }, reducedMotion: 'reduce' });
      const page = await context.newPage();

      await page.addInitScript(() => {
        sessionStorage.setItem('sj_auth_gate_skipped', 'true');
        localStorage.setItem('sj_user_logged_in', 'true');
      });

      const errors = [];
      page.on('console', msg => { if (msg.type() === 'error') errors.push(msg.text()); });
      page.on('pageerror', err => errors.push(err.message));

      const testUrl = 'http://localhost:8082/chemistry/chemistry-in-everyday-life/chemicals-in-food/artificial-sweeteners/';
      const res = await page.goto(testUrl, { waitUntil: 'domcontentloaded' });
      assert.equal(res.status(), 200, 'Page returned HTTP 200');

      await page.waitForTimeout(400);

      // Verify external stylesheet is linked and loaded
      await page.waitForFunction(() => {
        const link = document.querySelector('link[data-chemistry-style="theme"]');
        return link && link.sheet !== null;
      });
      const isSheetLoaded = await page.evaluate(() => {
        const link = document.querySelector('link[data-chemistry-style="theme"]');
        return link && link.sheet !== null;
      });
      assert.equal(isSheetLoaded, true, 'Chemistry CSS stylesheet is loaded into document');

      // Verify computed CSS root variable
      const brandLight = await page.evaluate(() => getComputedStyle(document.documentElement).getPropertyValue('--brand').trim());
      assert.equal(brandLight, '#1e3a8a', 'Light mode --brand matches #1e3a8a');

      // Verify dark mode variable
      const brandDark = await page.evaluate(() => {
        document.body.classList.add('dark-mode');
        const val = getComputedStyle(document.body).getPropertyValue('--brand').trim();
        document.body.classList.remove('dark-mode');
        return val;
      });
      assert.equal(brandDark, '#93c5fd', 'Dark mode --brand matches #93c5fd');

      // Verify responsive .desk-only display
      const deskOnlyDisplay = await page.evaluate(() => {
        const el = document.querySelector('.desk-only');
        return el ? getComputedStyle(el).display : 'none';
      });
      const expectedDeskOnly = width === 1280 ? 'block' : 'none';
      assert.equal(deskOnlyDisplay, expectedDeskOnly, `.desk-only display is ${expectedDeskOnly} at ${width}px`);

      // Verify zero fatal console errors
      const fatalErrors = errors.filter(e => !e.includes('favicon') && !e.includes('adsbygoogle') && !e.includes('pagead') && !e.includes('footer-container'));
      assert.deepEqual(fatalErrors, [], 'No fatal runtime errors');

      console.log(`Passed all tests at ${width}px!`);
      await context.close();
    }
    await browser.close();
    console.log('\n🎉 ALL CHEMISTRY VIEWPORT TESTS PASSED PERFECTLY!');
  } catch (err) {
    console.error('CHEMISTRY TEST ERROR:', err);
    process.exit(1);
  }
})();
