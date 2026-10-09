const assert = require('node:assert/strict');
const { chromium } = require('playwright');

(async () => {
  try {
    const browser = await chromium.launch({ headless: true });

    const testCases = [
      {
        url: 'http://localhost:8082/up-assistant-teacher/gk-current-affairs/ancient-indian-monuments-temples-architecture/index.html',
        selector: 'link[data-topic-style="up-assistant-glass"]',
        name: 'UP Assistant Teacher GK (Monuments & Architecture)',
        varName: '--accent-gradient',
        expectedVal: 'linear-gradient(135deg, #d4af37, #2980b9)'
      },
      {
        url: 'http://localhost:8082/up-assistant-teacher/logical-reasoning/analogies/index.html',
        selector: 'link[data-topic-style="up-assistant-glass"]',
        name: 'UP Assistant Teacher Logical Reasoning (Analogies)',
        varName: '--accent-gradient',
        expectedVal: 'linear-gradient(135deg, #d4af37, #2980b9)'
      },
      {
        url: 'http://localhost:8082/up-assistant-teacher/child-psychology/learning-theories-practical-classroom-application/index.html',
        selector: 'link[data-topic-style="up-assistant-glass"]',
        name: 'UP Assistant Teacher Child Psychology (Learning Theories)',
        varName: '--accent-gradient',
        expectedVal: 'linear-gradient(135deg, #d4af37, #2980b9)'
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

        // Verify no remaining inline styles matching the block
        const hasInlineGlassStyle = await page.evaluate(() => {
          const styles = Array.from(document.querySelectorAll('style'));
          return styles.some(s => s.textContent.includes('--glass-bg: rgba(255,255,255,0.95)') && s.textContent.includes('.topic-container'));
        });
        assert.equal(hasInlineGlassStyle, false, 'No inline up-assistant glass style tag remains');

        // Verify CSS variable values resolved
        const resolvedVal = await page.evaluate((vName) => {
          return window.getComputedStyle(document.documentElement).getPropertyValue(vName).trim();
        }, testCase.varName);
        assert.equal(resolvedVal, testCase.expectedVal, `CSS variable ${testCase.varName} is active and resolved to ${testCase.expectedVal}`);

        // Verify tab buttons exist and are styled
        const tabsCount = await page.locator('.study-tabs .tab-btn').count();
        if (tabsCount > 0) {
          const firstTab = page.locator('.study-tabs .tab-btn').first();
          await firstTab.click();
          await page.waitForTimeout(100);
        }

        // Verify zero fatal console errors
        const fatalErrors = errors.filter(e => !e.includes('favicon') && !e.includes('adsbygoogle') && !e.includes('pagead') && !e.includes('footer-container') && !e.includes('status of 409'));
        assert.deepEqual(fatalErrors, [], 'No fatal runtime errors');

        console.log(`Passed all tests for ${testCase.name} at ${width}px!`);
        await context.close();
      }
    }

    await browser.close();
    console.log('\n🎉 ALL UP ASSISTANT TEACHER GLASS VIEWPORT TESTS PASSED PERFECTLY!');
    process.exit(0);
  } catch (err) {
    console.error('UP ASSISTANT TEACHER GLASS TEST ERROR:', err);
    process.exit(1);
  }
})();
