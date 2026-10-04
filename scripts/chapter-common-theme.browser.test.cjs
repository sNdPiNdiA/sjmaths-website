const test = require('node:test');
const assert = require('node:assert/strict');
const { chromium } = require('playwright');
const path = require('node:path');

test('chapter-common fallback follows canonical theme preference without consuming palette values', { timeout: 30000 }, async () => {
  const browser = await chromium.launch({ headless: true });
  try {
    const page = await browser.newPage({ viewport: { width: 390, height: 844 } });
    await page.addInitScript(() => {
      localStorage.setItem('sjmaths.theme.preference', 'light');
      localStorage.setItem('sjmaths-theme', 'green');
    });
    await page.route('https://sjmaths.com/theme-test', route => route.fulfill({ contentType: 'text/html', body: '<!doctype html><html><body></body></html>' }));
    await page.goto('https://sjmaths.com/theme-test');
    await page.setContent('<button id="theme-toggle"><i class="fa-moon"></i></button><div id="progressBar"></div>');
    await page.addScriptTag({ path: path.join(process.cwd(), 'assets/js/chapter-common.js') });
    const theme = page.locator('#theme-toggle');
    assert.equal(await page.locator('html').getAttribute('data-theme'), 'light');
    assert.equal(await theme.getAttribute('aria-pressed'), 'false');
    await theme.focus();
    await page.keyboard.press('Enter');
    assert.equal(await page.locator('html').getAttribute('data-theme'), 'dark');
    assert.equal(await page.locator('html').getAttribute('data-theme-preference'), 'dark');
    assert.equal(await theme.getAttribute('aria-pressed'), 'true');
    assert.equal(await page.evaluate(() => localStorage.getItem('sjmaths.theme.preference')), 'dark');
    assert.equal(await page.evaluate(() => localStorage.getItem('sjmaths-theme')), 'green');
    await page.evaluate(() => window.dispatchEvent(new StorageEvent('storage', { key: 'sjmaths.theme.preference', newValue: 'light' })));
    assert.equal(await page.locator('html').getAttribute('data-theme'), 'light');
    assert.equal(await theme.getAttribute('aria-pressed'), 'false');
  } finally { await browser.close(); }
});
