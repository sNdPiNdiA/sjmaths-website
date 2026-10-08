const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const { chromium } = require('playwright');
const { ROOT, siteFiles } = require('./seo-html.cjs');
const { routeRepositoryFixtures } = require('./lib/browser-fixture.cjs');

test('UPSC shared assets preserve keyboard tabs, bilingual content and test submission', { timeout: 90000 }, async () => {
  const file = 'upsc/ancient-history/HarappanIndus-Valley-Civilisation/Agriculture/index.html';
  const url = 'https://sjmaths.com/' + file.replace(/index\.html$/, '');
  const after = fs.readFileSync(path.join(ROOT, file), 'utf8');
  const { hydrateUpscStyles, upscTopicCss } = await import('./lib/upsc-styles.mjs');
  const { hydrateUpscLanguage, upscLanguageSource } = await import('./lib/upsc-language.mjs');
  // Immutable original fingerprints keep this independent of moving HEAD and
  // shallow clones while retaining current authored content and shared UI fixes.
  const hash = text => crypto.createHash('sha256').update(text).digest('hex');
  assert.equal(hash(upscTopicCss), '785d9448f3e3e7d552ca75a6e07901534e3cc9f8ec47e5bdbff527be8e8f036e');
  assert.equal(hash(upscLanguageSource), '1d69b3c507711fccd9c3a8393332293e142bbf83713e0af277fafb42763299f7');
  const before = hydrateUpscLanguage(hydrateUpscStyles(after));
  assert.notEqual(before, after, 'the comparison must exercise inline versus external assets');
  const browser = await chromium.launch({ headless: true });
  try {
    for (const width of [390, 1280]) {
      const outcomes = [];
      for (const html of [before, after]) {
        const context = await browser.newContext({ viewport: { width, height: 900 }, reducedMotion: 'reduce', serviceWorkers: 'block' });
        try {
          const page = await context.newPage();
          const evidence = await routeRepositoryFixtures(page, { root: ROOT, files: siteFiles() });
          await page.route(url, route => route.fulfill({ contentType: 'text/html', body: html }));
          await page.goto(url);
          const skip = page.locator('#sj-skip-gate-btn');
          await skip.waitFor({ state: 'visible', timeout: 15000 });
          await skip.click();
          await page.locator('#sj-auth-overlay').waitFor({ state: 'hidden' });
          assert.equal(await page.locator('.study-tab-footer').evaluate(nav => getComputedStyle(nav).position), 'static');
          // Practice deliberately shuffles questions; pin randomness only in
          // this isolated comparison so order does not create false differences.
          await page.evaluate(() => { Math.random = () => 0.25; });
          const tabs = await page.locator('.study-tabs .tab-btn').evaluateAll(buttons => buttons.filter(button => button.getClientRects().length).map(button => button.dataset.tab));
          const states = [];
          for (const tab of tabs) {
            const button = page.locator(`.study-tabs [data-tab="${tab}"]`);
            await button.focus();
            await page.keyboard.press('Enter');
            assert.equal(await button.getAttribute('aria-selected'), 'true');
            states.push({ tab, text: await page.locator('#topic-content').innerText() });
          }
          await page.locator('#langHi').click();
          assert.equal(await page.locator('#langHi').getAttribute('aria-pressed'), 'true');
          const hindi = await page.locator('#topic-content').innerText();
          await page.locator('#langEn').click();
          assert.equal(await page.locator('#langEn').getAttribute('aria-pressed'), 'true');
          const submit = page.locator('.btn-submit-test');
          await submit.click();
          assert.equal(await submit.isDisabled(), true);
          const score = await page.locator('.mock-test-result').innerText();
          assert.match(score, /correct.*answered/);
          assert.deepEqual(evidence.missing, []);
          const unexpected = evidence.errors.filter(error => !error.startsWith('Service Worker registration failed'));
          assert.deepEqual(unexpected, []);
          outcomes.push({ tabs: states, hindi, score });
        } finally { await context.close(); }
      }
      assert.deepEqual(outcomes[1], outcomes[0], `before/after outcomes at ${width}px`);
    }
  } finally { await browser.close(); }
});
