const assert = require('node:assert/strict');
const { chromium } = require('playwright');

(async () => {
  try {
    const browser = await chromium.launch({ headless: true });

    const testCases = [
      {
        url: 'http://localhost:8082/civics/district-administration/district-magistrate/index.html',
        selector: 'link[data-civics-style="topic"]',
        name: 'Civics Topic (District Magistrate)'
      },
      {
        url: 'http://localhost:8082/civics/challenges-of-indian-democracy/index.html',
        selector: 'link[data-civics-style="hub"]',
        name: 'Civics Hub (Challenges of Indian Democracy)'
      }
    ];

    for (const testCase of testCases) {
      for (const width of [1280, 390]) {
        console.log(`\n=== Testing ${testCase.name} at Viewport: ${width}px ===`);
        const context = await browser.newContext({ viewport: { width, height: 800 }, reducedMotion: 'reduce' });
        const page = await context.newPage();

        await page.addInitScript(() => {
          sessionStorage.setItem('sj_auth_gate_skipped', 'true');
          localStorage.setItem('sj_user_logged_in', 'true');
        });

        const errors = [];
        page.on('console', msg => { if (msg.type() === 'error') errors.push(msg.text()); });
        page.on('pageerror', err => errors.push(err.message));

        const res = await page.goto(testCase.url, { waitUntil: 'domcontentloaded' });
        assert.equal(res.status(), 200, 'Page returned HTTP 200');

        await page.waitForTimeout(300);

        // Verify external stylesheet is linked and loaded
        await page.waitForFunction((sel) => {
          const link = document.querySelector(sel);
          return link && link.sheet !== null;
        }, testCase.selector);
        const isSheetLoaded = await page.evaluate((sel) => {
          const link = document.querySelector(sel);
          return link && link.sheet !== null;
        }, testCase.selector);
        assert.equal(isSheetLoaded, true, 'Civics CSS stylesheet is loaded into document');

        // Verify no remaining inline styles in document matching the block
        const hasInlineTopicStyle = await page.evaluate(() => {
          const styles = Array.from(document.querySelectorAll('style'));
          return styles.some(s => s.textContent.includes('--accent:#4338ca') || s.textContent.includes('--accent: #4338ca'));
        });
        assert.equal(hasInlineTopicStyle, false, 'No inline civics style tag remains');

        // Verify CSS variable values resolved
        const brand = await page.evaluate(() => {
          return window.getComputedStyle(document.documentElement).getPropertyValue('--brand').trim();
        });
        assert.equal(brand, '#16324f', 'CSS variable --brand is active and resolved');

        // Verify hero section exists
        const hero = page.locator('.hero');
        assert.ok(await hero.count() > 0, 'Hero element exists');

        // Verify zero fatal console errors
        const fatalErrors = errors.filter(e => !e.includes('favicon') && !e.includes('adsbygoogle') && !e.includes('pagead') && !e.includes('footer-container') && !e.includes('status of 409'));
        assert.deepEqual(fatalErrors, [], 'No fatal runtime errors');

        console.log(`Passed all tests for ${testCase.name} at ${width}px!`);
        await context.close();
      }
    }

    await browser.close();
    console.log('\n🎉 ALL CIVICS VIEWPORT TESTS PASSED PERFECTLY!');
    process.exit(0);
  } catch (err) {
    console.error('CIVICS TEST ERROR:', err);
    process.exit(1);
  }
})();
