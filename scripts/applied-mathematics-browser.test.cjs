const assert = require('node:assert/strict');
const { chromium } = require('playwright');

(async () => {
  try {
    const browser = await chromium.launch({ headless: true });
    for (const width of [1280, 390]) {
      console.log(`\n=== Testing Viewport Width: ${width}px ===`);
      const context = await browser.newContext({ viewport: { width, height: 800 }, reducedMotion: 'reduce' });
      const page = await context.newPage();

      // Ensure auth gate does not block test interactions
      await page.addInitScript(() => {
        sessionStorage.setItem('sj_auth_gate_skipped', 'true');
        localStorage.setItem('sj_user_logged_in', 'true');
      });

      const errors = [];
      page.on('console', msg => { if (msg.type() === 'error') errors.push(msg.text()); });
      page.on('pageerror', err => errors.push(err.message));

      const testUrl = 'http://localhost:8082/class-11-applied-mathematics/chapter-1-numbers-and-quantification/1-1-binary-number-system/';
      const res = await page.goto(testUrl, { waitUntil: 'domcontentloaded' });
      assert.equal(res.status(), 200, 'Page returned HTTP 200');

      // Wait for element to be attached in DOM
      await page.waitForSelector('link[data-applied-maths-style="monolith"]', { state: 'attached' });
      await page.waitForTimeout(400);

      // Wait for external stylesheet to be loaded
      await page.waitForFunction(() => {
        const link = document.querySelector('link[data-applied-maths-style="monolith"]');
        return link && link.sheet !== null;
      });
      const isSheetLoaded = await page.evaluate(() => {
        const link = document.querySelector('link[data-applied-maths-style="monolith"]');
        return link && link.sheet !== null;
      });
      assert.equal(isSheetLoaded, true, 'CSS stylesheet is loaded in document');

      // Wait for switchTab script to initialize
      const hasSwitchTab = await page.evaluate(() => typeof switchTab === 'function');
      assert.equal(hasSwitchTab, true, 'switchTab is exposed globally');

      // Verify initial active tab in subject-nav is Learn
      const initialActiveTab = await page.locator('.subject-nav .sub-nav-item.active').getAttribute('data-tab');
      assert.equal(initialActiveTab, 'learn', 'Initial active tab is learn');
      const learnDisplay = await page.locator('#tab-learn').evaluate(el => window.getComputedStyle(el).display);
      assert.equal(learnDisplay, 'block', 'Learn section is visible initially');

      // Click second tab: Check Your Progress
      console.log('Clicking tab 1 (progress)...');
      const progressResult = await page.evaluate(() => {
        window.switchTab('progress');
        const btn = document.querySelector('.subject-nav .sub-nav-item[data-tab="progress"]');
        const content = document.querySelector('#tab-progress');
        return {
          active: btn ? btn.classList.contains('active') : false,
          display: content ? window.getComputedStyle(content).display : 'none'
        };
      });
      assert.equal(progressResult.active, true, 'Progress tab received active class');
      assert.equal(progressResult.display, 'block', 'Progress tab content displayed as block');

      // Click mock test tab
      console.log('Clicking tab 4 (mock)...');
      const mockResult = await page.evaluate(() => {
        window.switchTab('mock');
        const btn = document.querySelector('.subject-nav .sub-nav-item[data-tab="mock"]');
        const content = document.querySelector('#tab-mock');
        return {
          active: btn ? btn.classList.contains('active') : false,
          display: content ? window.getComputedStyle(content).display : 'none'
        };
      });
      assert.equal(mockResult.active, true, 'Mock tab received active class');
      assert.equal(mockResult.display, 'block', 'Mock test tab content displayed as block');

      // Verify zero unexpected console errors
      const fatalErrors = errors.filter(e => !e.includes('favicon') && !e.includes('adsbygoogle') && !e.includes('pagead') && !e.includes('footer-container') && !e.includes('status of 409'));
      assert.deepEqual(fatalErrors, [], 'No uncaught script errors');

      console.log(`Passed all tests at ${width}px!`);
      await context.close();
    }
    await browser.close();
    console.log('\n🎉 ALL VIEWPORT TESTS PASSED PERFECTLY!');
  } catch (err) {
    console.error('TEST ERROR:', err);
    process.exit(1);
  }
})();
