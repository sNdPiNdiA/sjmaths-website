const assert = require('node:assert/strict');
const { chromium } = require('playwright');

(async () => {
  try {
    const browser = await chromium.launch({ headless: true });
    for (const width of [1280, 390]) {
      console.log(`\n=== Testing Music Instrumental Topic at Viewport Width: ${width}px ===`);
      const context = await browser.newContext({ viewport: { width, height: 800 }, reducedMotion: 'reduce' });
      const page = await context.newPage();

      await page.addInitScript(() => {
        sessionStorage.setItem('sj_auth_gate_skipped', 'true');
        localStorage.setItem('sj_user_logged_in', 'true');
      });

      const errors = [];
      page.on('console', msg => { if (msg.type() === 'error') errors.push(msg.text()); });
      page.on('pageerror', err => errors.push(err.message));

      const testUrl = 'http://localhost:8082/music-instrumental/avanaddh-vadya/bol-notation/kathin-layakari/index.html';
      const res = await page.goto(testUrl, { waitUntil: 'domcontentloaded' });
      assert.equal(res.status(), 200, 'Page returned HTTP 200');

      await page.waitForTimeout(400);

      // Verify external stylesheet is linked and loaded
      await page.waitForFunction(() => {
        const link = document.querySelector('link[data-music-style="instrumental"]');
        return link && link.sheet !== null;
      });
      const isSheetLoaded = await page.evaluate(() => {
        const link = document.querySelector('link[data-music-style="instrumental"]');
        return link && link.sheet !== null;
      });
      assert.equal(isSheetLoaded, true, 'Music Instrumental Topic CSS stylesheet is loaded into document');

      // Verify no remaining inline topic styles in document
      const hasInlineTopicStyle = await page.evaluate(() => {
        const styles = Array.from(document.querySelectorAll('style'));
        return styles.some(s => s.textContent.includes('--brand:#7c2d12'));
      });
      assert.equal(hasInlineTopicStyle, false, 'No inline topic style tag remains');

      // Verify study tabs exist
      const tabs = page.locator('.study-tabs');
      const tabsCount = await tabs.count();
      assert.ok(tabsCount > 0, 'Study tabs element exists');

      // Verify responsive tabs grid
      const cols = await tabs.first().evaluate(el => window.getComputedStyle(el).gridTemplateColumns);
      if (width === 1280) {
        assert.ok(cols.includes('repeat(4') || cols.split(' ').length === 4, 'Tabs have 4 columns on desktop');
      } else {
        assert.ok(cols.includes('repeat(2') || cols.split(' ').length === 2, 'Tabs have 2 columns on mobile');
      }

      // Verify tab-btn min-height
      const minHeight = await page.locator('.tab-btn').first().evaluate(el => window.getComputedStyle(el).minHeight);
      const expectedMinHeight = width === 1280 ? '54px' : '44px';
      assert.equal(minHeight, expectedMinHeight, `Tab button min-height is ${expectedMinHeight}`);

      // Verify zero fatal console errors
      const fatalErrors = errors.filter(e => !e.includes('favicon') && !e.includes('adsbygoogle') && !e.includes('pagead') && !e.includes('footer-container') && !e.includes('status of 409'));
      assert.deepEqual(fatalErrors, [], 'No fatal runtime errors');

      console.log(`Passed all tests at ${width}px!`);
      await context.close();
    }
    await browser.close();
    console.log('\n🎉 ALL MUSIC INSTRUMENTAL VIEWPORT TESTS PASSED PERFECTLY!');
    process.exit(0);
  } catch (err) {
    console.error('MUSIC INSTRUMENTAL TEST ERROR:', err);
    process.exit(1);
  }
})();
