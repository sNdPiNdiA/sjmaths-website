const assert = require('node:assert/strict');
const { chromium } = require('playwright');

(async () => {
  try {
    const browser = await chromium.launch({ headless: true });

    const testCases = [
      {
        url: 'http://localhost:8082/commerce/accounting-fundamentals/books-of-original-entry-and-ledger/index.html',
        selector: 'link[data-commerce-style="accounting"]',
        name: 'Commerce Accounting (Books of Original Entry)',
        varName: '--primary',
        expectedVal: '#0284c7'
      },
      {
        url: 'http://localhost:8082/commerce/accounting-fundamentals/index.html',
        selector: 'link[data-commerce-style="hub"]',
        name: 'Commerce Hub (Accounting Fundamentals)',
        varName: '--brand',
        expectedVal: '#0f766e'
      },
      {
        url: 'http://localhost:8082/commerce/accounting-fundamentals/indian-accounting-standards/index.html',
        selector: 'link[data-commerce-style="topic"]',
        name: 'Commerce Topic (Accounting Standards)',
        varName: '--brand',
        expectedVal: '#16324f'
      },
      {
        url: 'http://localhost:8082/commerce/auditing/valuation-and-verification/index.html',
        selector: 'link[data-commerce-style="auditing"]',
        name: 'Commerce Auditing (Valuation & Verification)',
        varName: '--brand',
        expectedVal: '#0f766e'
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
        assert.equal(isSheetLoaded, true, `${testCase.name} stylesheet is loaded into document`);

        // Verify no remaining inline styles in document matching the block
        const hasInlineTopicStyle = await page.evaluate(() => {
          const styles = Array.from(document.querySelectorAll('style'));
          return styles.some(s => s.textContent.includes('--primary: #0284c7') || s.textContent.includes('--brand:#0f766e') || s.textContent.includes('--brand:#16324f'));
        });
        assert.equal(hasInlineTopicStyle, false, 'No inline commerce style tag remains');

        // Verify CSS variable values resolved
        const resolvedVal = await page.evaluate((vName) => {
          return window.getComputedStyle(document.documentElement).getPropertyValue(vName).trim();
        }, testCase.varName);
        assert.equal(resolvedVal, testCase.expectedVal, `CSS variable ${testCase.varName} is active and resolved to ${testCase.expectedVal}`);

        // Verify zero fatal console errors
        const fatalErrors = errors.filter(e => !e.includes('favicon') && !e.includes('adsbygoogle') && !e.includes('pagead') && !e.includes('footer-container') && !e.includes('status of 409'));
        assert.deepEqual(fatalErrors, [], 'No fatal runtime errors');

        console.log(`Passed all tests for ${testCase.name} at ${width}px!`);
        await context.close();
      }
    }

    await browser.close();
    console.log('\n🎉 ALL COMMERCE VIEWPORT TESTS PASSED PERFECTLY!');
    process.exit(0);
  } catch (err) {
    console.error('COMMERCE TEST ERROR:', err);
    process.exit(1);
  }
})();
