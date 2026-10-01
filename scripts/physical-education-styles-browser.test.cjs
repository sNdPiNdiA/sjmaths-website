const test = require('node:test');
const assert = require('node:assert/strict');
const crypto = require('node:crypto');
const fs = require('node:fs');
const path = require('node:path');
const { chromium } = require('playwright');
const { ROOT } = require('./seo-html.cjs');
const { fixtureFiles, routeRepositoryFixtures } = require('./lib/browser-fixture.cjs');

test('Physical Education shared stylesheet preserves bilingual lesson rendering and controls', { timeout: 180000 }, async () => {
  const file = 'physical-education/anatomy-and-physiology/cells-tissues-and-organs/index.html';
  const route = '/physical-education/anatomy-and-physiology/cells-tissues-and-organs/';
  const fixtureRoot = path.resolve(ROOT, process.env.SJ_REFACTOR_FIXTURE_ROOT || '.');
  const files = fixtureFiles(fixtureRoot);
  const { hydratePhysicalEducationStyles } = await import('./lib/physical-education-styles.mjs');
  const externalHtml = fs.readFileSync(path.join(fixtureRoot, file), 'utf8');
  const inlineHtml = hydratePhysicalEducationStyles(externalHtml);
  assert.notEqual(inlineHtml, externalHtml, 'fixture must exercise the extracted stylesheet');
  const browser = await chromium.launch({ headless: true });
  const evidenceRoot = path.join(ROOT, 'scratch/refactor/physical-education-styles');
  fs.mkdirSync(evidenceRoot, { recursive: true });
  try {
    for (const width of [390, 1280]) {
      const screenshots = new Map();
      const overflow = [];
      for (const [kind, html] of [['inline', inlineHtml], ['external', externalHtml]]) {
        const context = await browser.newContext({ viewport: { width, height: 900 }, reducedMotion: 'reduce' });
        try {
          const page = await context.newPage();
          const evidence = await routeRepositoryFixtures(page, { root: fixtureRoot, files });
          await page.addInitScript(() => localStorage.setItem('sjmaths_pe_lang', 'en'));
          await page.route(`https://sjmaths.com${route}`, request => request.fulfill({ contentType: 'text/html', body: html }));
          await page.goto(`https://sjmaths.com${route}`, { waitUntil: 'networkidle' });
          await page.addStyleTag({ content: 'html { scroll-behavior: auto !important; }' });
          await page.evaluate(() => document.fonts.ready);
          assert.deepEqual(evidence.errors, [], `${kind} runtime errors`);
          assert.deepEqual(evidence.missing, [], `${kind} missing local requests`);
          if (kind === 'external') {
            const link = page.locator('link[data-pe-topic-style="topic"]');
            assert.equal(await link.count(), 1);
            assert.equal(await link.evaluate(element => element.sheet !== null), true);
          }
          overflow.push(await page.evaluate(() => Math.max(0, document.documentElement.scrollWidth - innerWidth)));

          const capture = async state => {
            const capturePath = path.join(evidenceRoot, `${width}-${state}-${kind}.png`);
            await page.screenshot({ path: capturePath, fullPage: false, animations: 'disabled' });
            screenshots.set(`${kind}-${state}`, capturePath);
          };
          await capture('english');
          await page.locator('#btn-hi').focus();
          await page.keyboard.press('Enter');
          assert.equal(await page.locator('html').getAttribute('data-pe-lang'), 'hi');
          assert.equal(await page.locator('.content-hi').isVisible(), true);
          await page.evaluate(() => window.scrollTo({ top: 0, behavior: 'instant' }));
          await page.waitForTimeout(100);
          await capture('hindi');
          const answer = page.locator('.content-hi .btn-reveal').first();
          const explanationId = await answer.getAttribute('onclick').then(value => value.match(/toggleExp\('([^']+)'\)/)?.[1]);
          assert.ok(explanationId, 'Hindi reveal button should reference its explanation');
          await answer.focus();
          await page.keyboard.press('Enter');
          assert.notEqual(await page.locator(`#${explanationId}`).evaluate(element => getComputedStyle(element).display), 'none');
          await page.evaluate(() => window.scrollTo({ top: 0, behavior: 'instant' }));
          await page.waitForTimeout(100);
          await capture('answer');
        } finally { await context.close(); }
      }
      assert.equal(overflow[1], overflow[0], `${width}px horizontal overflow parity`);
      for (const state of ['english', 'hindi', 'answer']) {
        const inline = fs.readFileSync(screenshots.get(`inline-${state}`));
        const external = fs.readFileSync(screenshots.get(`external-${state}`));
        const digest = buffer => crypto.createHash('sha256').update(buffer).digest('hex');
        assert.equal(digest(external), digest(inline), `${width}px ${state} inline/external pixels`);
      }
    }
  } finally { await browser.close(); }
});
