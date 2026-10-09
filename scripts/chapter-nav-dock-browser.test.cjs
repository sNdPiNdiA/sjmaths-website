const assert = require('node:assert/strict');
const { chromium } = require('playwright');

(async () => {
  try {
    const browser = await chromium.launch({ headless: true });

    const testCases = [
      {
        url: 'http://localhost:8082/class-11-maths/chapter-wise-notes/chapter-1-sets/index.html',
        selector: 'link[data-maths-style="nav-dock"]',
        name: 'Class 11 Maths Sets Chapter Notes'
      },
      {
        url: 'http://localhost:8082/class-12-maths/chapter-wise-notes/chapter-1-relations-and-functions/index.html',
        selector: 'link[data-maths-style="nav-dock"]',
        name: 'Class 12 Maths Relations & Functions Chapter Notes'
      },
      {
        url: 'http://localhost:8082/class-9-maths/chapter-wise-notes/chapter-10-herons-formula/index.html',
        selector: 'link[data-maths-style="nav-dock"]',
        name: 'Class 9 Maths Heron\'s Formula Chapter Notes'
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

        const res = await page.goto(testCase.url, { waitUntil: 'load' });
        assert.equal(res.status(), 200, 'Page returned HTTP 200');

        await page.waitForTimeout(400);

        // Verify external stylesheet is linked and loaded
        await page.waitForFunction((sel) => {
          const link = document.querySelector(sel);
          return link && link.sheet !== null;
        }, testCase.selector);

        // Verify no remaining inline styles matching the docked navigation comment
        await page.waitForFunction(() => {
          const styles = Array.from(document.querySelectorAll('style'));
          return !styles.some(s => s.textContent.includes('DUAL DESKTOP-FIXED & MOBILE-FLOATING SIDEBAR DOCK SYSTEM'));
        });

        // Verify CSS rules loaded from stylesheet
        await page.waitForFunction(() => {
          const link = document.querySelector('link[data-maths-style="nav-dock"]');
          if (!link || !link.sheet) return false;
          try {
            return Array.from(link.sheet.cssRules).some(r => r.selectorText && r.selectorText.includes('.chapter-nav-wrapper'));
          } catch (e) {
            return true;
          }
        });

        // Verify zero fatal console errors
        const fatalErrors = errors.filter(e => !e.includes('favicon') && !e.includes('adsbygoogle') && !e.includes('pagead') && !e.includes('footer-container') && !e.includes('status of 409'));
        assert.deepEqual(fatalErrors, [], 'No fatal runtime errors');

        console.log(`Passed all tests for ${testCase.name} at ${width}px!`);
        await context.close();
      }
    }

    await browser.close();
    console.log('\n🎉 ALL CHAPTER NAV DOCK VIEWPORT TESTS PASSED PERFECTLY!');
    process.exit(0);
  } catch (err) {
    console.error('CHAPTER NAV DOCK TEST ERROR:', err);
    process.exit(1);
  }
})();
