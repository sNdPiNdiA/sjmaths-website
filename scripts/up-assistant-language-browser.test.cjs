const assert = require('node:assert/strict');
const { chromium } = require('playwright');

(async () => {
  try {
    const browser = await chromium.launch({ headless: true });
    for (const width of [1280, 390]) {
      console.log(`\n=== Testing UP Assistant Language Topic at Viewport Width: ${width}px ===`);
      const context = await browser.newContext({ viewport: { width, height: 800 }, reducedMotion: 'reduce' });
      const page = await context.newPage();

      await page.addInitScript(() => {
        sessionStorage.setItem('sj_auth_gate_skipped', 'true');
        localStorage.setItem('sj_user_logged_in', 'true');
      });

      const errors = [];
      page.on('console', msg => { if (msg.type() === 'error') errors.push(msg.text()); });
      page.on('pageerror', err => errors.push(err.message));

      const testUrl = 'http://localhost:8082/up-assistant-teacher/hindi/alankaara-bhaeda-va-udaaharana/index.html';
      const res = await page.goto(testUrl, { waitUntil: 'domcontentloaded' });
      assert.equal(res.status(), 200, 'Page returned HTTP 200');

      await page.waitForTimeout(800);

      // Verify external stylesheet is linked and loaded
      await page.waitForFunction(() => {
        const link = document.querySelector('link[data-topic-style="up-assistant-language"]');
        return link && link.sheet !== null;
      });
      const isSheetLoaded = await page.evaluate(() => {
        const link = document.querySelector('link[data-topic-style="up-assistant-language"]');
        return link && link.sheet !== null;
      });
      assert.equal(isSheetLoaded, true, 'UP Assistant Language Topic CSS stylesheet is loaded into document');

      // Verify no remaining inline topic styles in document
      const hasInlineTopicStyle = await page.evaluate(() => {
        const styles = Array.from(document.querySelectorAll('style'));
        return styles.some(s => s.textContent.includes('--accent-gradient: linear-gradient(135deg, #d4af37, #c0392b)'));
      });
      assert.equal(hasInlineTopicStyle, false, 'No inline topic style tag remains');

      // Verify study tabs exist and interact
      const tabButtons = page.locator('.study-tabs .tab-btn');
      const tabCount = await tabButtons.count();
      assert.ok(tabCount > 0, 'Study tab buttons are present');

      // Verify tabs styling and responsiveness
      const tabsWrap = await page.locator('.study-tabs').evaluate(el => window.getComputedStyle(el).flexWrap);
      if (width === 1280) {
        assert.equal(tabsWrap, 'wrap', 'Tabs wrap on desktop');
      } else {
        assert.equal(tabsWrap, 'nowrap', 'Tabs nowrap on mobile scroll row');
      }

      // Verify active tab styling
      const activeTab = page.locator('.tab-btn.active').first();
      const activeBg = await activeTab.evaluate(el => window.getComputedStyle(el).backgroundColor);
      assert.equal(activeBg, 'rgb(15, 118, 110)', 'Active tab button has styled background');

      // Verify clicking tab 2 activates tab panel 2
      if (tabCount > 1) {
        await tabButtons.nth(1).click();
        const tab2Active = await tabButtons.nth(1).evaluate(el => el.classList.contains('active'));
        assert.equal(tab2Active, true, 'Second tab becomes active upon click');
      }

      // Verify zero fatal console errors
      const fatalErrors = errors.filter(e => !e.includes('favicon') && !e.includes('adsbygoogle') && !e.includes('pagead') && !e.includes('footer-container') && !e.includes('status of 409'));
      assert.deepEqual(fatalErrors, [], 'No fatal runtime errors');

      console.log(`Passed all tests at ${width}px!`);
      await context.close();
    }
    await browser.close();
    console.log('\n🎉 ALL UP ASSISTANT LANGUAGE VIEWPORT TESTS PASSED PERFECTLY!');
    process.exit(0);
  } catch (err) {
    console.error('UP ASSISTANT LANGUAGE TEST ERROR:', err);
    process.exit(1);
  }
})();
