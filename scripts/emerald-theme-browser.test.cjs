const assert = require('node:assert/strict');
const { chromium } = require('playwright');

(async () => {
  try {
    const browser = await chromium.launch({ headless: true });

    const testPages = [
      {
        url: 'http://localhost:8082/geography/cartography/geographic-information-system/index.html',
        name: 'Geography Topic (GIS)'
      },
      {
        url: 'http://localhost:8082/english/language/grammar/narration/index.html',
        name: 'English Topic (Narration)'
      }
    ];

    for (const testPage of testPages) {
      for (const width of [1280, 390]) {
        console.log(`\n=== Testing ${testPage.name} at Viewport: ${width}px ===`);
        const context = await browser.newContext({ viewport: { width, height: 800 }, reducedMotion: 'reduce' });
        const page = await context.newPage();

        await page.addInitScript(() => {
          sessionStorage.setItem('sj_auth_gate_skipped', 'true');
          localStorage.setItem('sj_user_logged_in', 'true');
        });

        const errors = [];
        page.on('console', msg => { if (msg.type() === 'error') errors.push(msg.text()); });
        page.on('pageerror', err => errors.push(err.message));

        const res = await page.goto(testPage.url, { waitUntil: 'domcontentloaded' });
        assert.equal(res.status(), 200, 'Page returned HTTP 200');

        await page.waitForTimeout(300);

        // Verify external theme stylesheet is linked and loaded
        await page.waitForFunction(() => {
          const link = document.querySelector('link[data-topic-theme="emerald"]');
          return link && link.sheet !== null;
        });
        const isSheetLoaded = await page.evaluate(() => {
          const link = document.querySelector('link[data-topic-theme="emerald"]');
          return link && link.sheet !== null;
        });
        assert.equal(isSheetLoaded, true, 'Emerald Theme CSS stylesheet is loaded into document');

        // Verify no remaining inline topic styles in document
        const hasInlineTopicStyle = await page.evaluate(() => {
          const styles = Array.from(document.querySelectorAll('style'));
          return styles.some(s => s.textContent.includes('--brand: #064e3b') || s.textContent.includes('--brand:#064e3b'));
        });
        assert.equal(hasInlineTopicStyle, false, 'No inline emerald style tag remains');

        // Verify CSS variable values resolved
        const brand = await page.evaluate(() => {
          return window.getComputedStyle(document.documentElement).getPropertyValue('--brand').trim();
        });
        assert.equal(brand, '#064e3b', 'CSS variable --brand is active and resolved');

        // Verify zero fatal console errors
        const fatalErrors = errors.filter(e => !e.includes('favicon') && !e.includes('adsbygoogle') && !e.includes('pagead') && !e.includes('footer-container') && !e.includes('status of 409'));
        assert.deepEqual(fatalErrors, [], 'No fatal runtime errors');

        console.log(`Passed all tests for ${testPage.name} at ${width}px!`);
        await context.close();
      }
    }

    await browser.close();
    console.log('\n🎉 ALL EMERALD THEME VIEWPORT TESTS PASSED PERFECTLY!');
    process.exit(0);
  } catch (err) {
    console.error('EMERALD THEME TEST ERROR:', err);
    process.exit(1);
  }
})();
