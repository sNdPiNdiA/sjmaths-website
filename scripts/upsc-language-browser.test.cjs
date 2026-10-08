const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const { chromium } = require('playwright');
const { ROOT } = require('./seo-html.cjs');

test('parser-blocking UPSC language asset preserves readiness order and preferences across reloads', { timeout: 30000 }, async () => {
  const shared = fs.readFileSync(path.join(ROOT, 'assets/js/upsc-language.js'), 'utf8');
  // Frozen original source fingerprint, not a mutable HEAD lookup. This works
  // after committing extraction and in a shallow checkout.
  const inline = shared.trim();
  assert.equal(crypto.createHash('sha256').update(inline).digest('hex'), '1d69b3c507711fccd9c3a8393332293e142bbf83713e0af277fafb42763299f7');
  const browser = await chromium.launch({ headless: true });
  try {
    for (const pref of ['en', 'hi']) {
      const outcomes = [];
      for (const mode of ['inline', 'shared']) {
        const context = await browser.newContext();
        try {
          const page = await context.newPage();
          await page.addInitScript(pref => {
            window.order = [];
            if (!localStorage.getItem('sj_pref_lang')) localStorage.setItem('sj_pref_lang', pref);
          }, pref);
          await page.route('https://sjmaths.com/deferred.js', route => route.fulfill({ contentType: 'text/javascript', body: `window.order.push('deferred'); document.addEventListener('DOMContentLoaded', () => window.order.push(document.getElementById('langHi').getAttribute('aria-pressed')));` }));
          await page.route('https://sjmaths.com/assets/js/upsc-language.js', async route => {
            // An intentionally slow local asset must still run before deferred
            // neighbours and DOMContentLoaded. This test never calls Firebase.
            await new Promise(resolve => setTimeout(resolve, 100));
            await route.fulfill({ contentType: 'text/javascript', body: shared + '\nwindow.order.push("bootstrap");' });
          });
          const runtime = mode === 'inline'
            ? `<script>${inline}\nwindow.order.push("bootstrap");</script>`
            : '<script src="/assets/js/upsc-language.js" data-upsc-shared-script="language"></script>';
          await page.route('https://sjmaths.com/language-fixture/', route => route.fulfill({ contentType: 'text/html', body: `<!doctype html><html><head><script defer src="/deferred.js"></script></head><body><button id="langEn">EN</button><button id="langHi">Hindi</button>${runtime}</body></html>` }));
          await page.goto('https://sjmaths.com/language-fixture/');
          const snapshot = () => page.evaluate(() => ({ order: window.order, language: localStorage.getItem('sj_pref_lang'), html: document.documentElement.className, body: document.body.className, hi: document.getElementById('langHi').getAttribute('aria-pressed') }));
          const initial = await snapshot();
          assert.deepEqual(initial.order, ['bootstrap', 'deferred', String(pref === 'hi')]);
          assert.equal(initial.language, pref);
          await page.locator('#langHi').click();
          await page.reload();
          const reloaded = await snapshot();
          assert.equal(reloaded.hi, 'true');
          assert.equal(reloaded.language, 'hi');
          await page.locator('#langEn').click();
          assert.equal(await page.locator('#langEn').getAttribute('aria-pressed'), 'true');
          assert.equal(await page.evaluate(() => localStorage.getItem('sj_pref_lang')), 'en');
          outcomes.push({ initial, reloaded });
        } finally { await context.close(); }
      }
      assert.deepEqual(outcomes[1], outcomes[0]);
    }
  } finally { await browser.close(); }
});
