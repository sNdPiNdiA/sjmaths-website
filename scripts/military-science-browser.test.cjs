const assert = require('node:assert/strict');
const { chromium } = require('playwright');

(async () => {
  try {
    const browser = await chromium.launch({ headless: true });

    const testCases = [
      {
        url: 'http://localhost:8082/military-science/contemporary-security/21st-century-security-scenario/index.html',
        selector: 'link[data-military-science-style="topic"]',
        name: 'Military Science Topic (21st Century Security Scenario)',
        varName: '--brand',
        expectedVal: '#16324f'
      },
      {
        url: 'http://localhost:8082/military-science/contemporary-security/cyber-security/challenges/index.html',
        selector: 'link[data-military-science-style="topic"]',
        name: 'Military Science Topic (Cyber Security Challenges)',
        varName: '--accent',
        expectedVal: '#b45309'
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
          return styles.some(s => s.textContent.includes('--brand:#16324f') && s.textContent.includes('--brand-dark:#0f2439'));
        });
        assert.equal(hasInlineTopicStyle, false, 'No inline military science topic style tag remains');

        // Verify CSS variable values resolved
        const resolvedVal = await page.evaluate((vName) => {
          return window.getComputedStyle(document.documentElement).getPropertyValue(vName).trim();
        }, testCase.varName);
        assert.equal(resolvedVal, testCase.expectedVal, `CSS variable ${testCase.varName} is active and resolved to ${testCase.expectedVal}`);

        // Verify tab switching
        const quizTabBtn = page.locator('#tab-btn-quiz');
        if (await quizTabBtn.count() > 0) {
          await quizTabBtn.click();
          await page.waitForTimeout(150);
          const isQuizVisible = await page.locator('#tab-quiz').isVisible();
          assert.equal(isQuizVisible, true, 'Quiz tab panel became visible upon click');
        }

        // Verify zero fatal console errors
        const fatalErrors = errors.filter(e => !e.includes('favicon') && !e.includes('adsbygoogle') && !e.includes('pagead') && !e.includes('footer-container') && !e.includes('status of 409'));
        assert.deepEqual(fatalErrors, [], 'No fatal runtime errors');

        console.log(`Passed all tests for ${testCase.name} at ${width}px!`);
        await context.close();
      }
    }

    await browser.close();
    console.log('\n🎉 ALL MILITARY SCIENCE VIEWPORT TESTS PASSED PERFECTLY!');
    process.exit(0);
  } catch (err) {
    console.error('MILITARY SCIENCE TEST ERROR:', err);
    process.exit(1);
  }
})();
