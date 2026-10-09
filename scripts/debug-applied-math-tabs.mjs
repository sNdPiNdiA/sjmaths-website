import { chromium } from 'playwright';

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({ viewport: { width: 390, height: 800 } });
  const page = await context.newPage();
  await page.addInitScript(() => {
    sessionStorage.setItem('sj_auth_gate_skipped', 'true');
    localStorage.setItem('sj_user_logged_in', 'true');
  });
  await page.goto('http://localhost:8082/class-11-applied-mathematics/chapter-1-numbers-and-quantification/1-1-binary-number-system/index.html');
  await page.waitForTimeout(400);

  const items = await page.locator('.subject-nav .sub-nav-item').evaluateAll(els =>
    els.map(e => ({ tab: e.getAttribute('data-tab'), visible: e.offsetParent !== null, cls: e.className }))
  );
  console.log('Nav items at 390px:', items);

  const btn = page.locator('.subject-nav .sub-nav-item[data-tab="progress"]');
  console.log('Clicking progress tab...');
  await btn.click({ force: true });
  await page.waitForTimeout(300);

  const activeTab = await page.locator('.subject-nav .sub-nav-item.active').getAttribute('data-tab');
  console.log('Active tab after click:', activeTab);

  await browser.close();
})();
