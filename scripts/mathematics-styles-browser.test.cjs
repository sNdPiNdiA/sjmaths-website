const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { chromium } = require('playwright');
const { ROOT } = require('./seo-html.cjs');
const { fixtureFiles, routeRepositoryFixtures } = require('./lib/browser-fixture.cjs');

test('Mathematics external stylesheet matches inline rendering on mobile and desktop', { timeout: 180000 }, async () => {
  const file = 'mathematics/abstract-algebra/fields/field-and-examples/index.html';
  const route = '/mathematics/abstract-algebra/fields/field-and-examples/';
  const fixtureRoot = path.resolve(ROOT, process.env.SJ_REFACTOR_FIXTURE_ROOT || '.');
  const files = fixtureFiles(fixtureRoot);
  const { hydrateMathematicsStyles } = await import('./lib/mathematics-styles.mjs');
  const externalHtml = fs.readFileSync(path.join(fixtureRoot, file), 'utf8');
  const inlineHtml = hydrateMathematicsStyles(externalHtml);
  assert.notEqual(inlineHtml, externalHtml, 'fixture must exercise the extracted stylesheet');
  const browser = await chromium.launch({ headless: true });
  const evidenceRoot = path.join(ROOT, 'scratch/refactor/mathematics-styles');
  fs.mkdirSync(evidenceRoot, { recursive: true });
  try {
    for (const width of [390, 1280]) {
      for (const theme of ['light', 'dark']) {
        const screenshots = [];
        const overflowWidths = [];
        for (const [kind, html] of [['inline', inlineHtml], ['external', externalHtml]]) {
          const context = await browser.newContext({ viewport: { width, height: 900 }, reducedMotion: 'reduce' });
          try {
            const page = await context.newPage();
            const evidence = await routeRepositoryFixtures(page, { root: fixtureRoot, files });
            await page.addInitScript(value => {
              localStorage.setItem('sjmaths_theme', value);
              localStorage.setItem('sj_theme', value);
            }, theme);
            await page.route(`https://sjmaths.com${route}`, request => request.fulfill({ contentType: 'text/html', body: html }));
            await page.goto(`https://sjmaths.com${route}`, { waitUntil: 'networkidle' });
            await page.evaluate(() => document.fonts.ready);
            overflowWidths.push(await page.evaluate(() => Math.max(0, document.documentElement.scrollWidth - innerWidth)));
            assert.deepEqual(evidence.errors, []);
            assert.deepEqual(evidence.missing, []);
            if (kind === 'external') {
              assert.equal(await page.locator('link[data-mathematics-shared-style="topic"]').count(), 1);
              assert.equal(await page.locator('link[data-mathematics-shared-style="topic"]').evaluate(link => link.sheet !== null), true);
            }
            const screenshot = await page.screenshot({ fullPage: true, animations: 'disabled' });
            fs.writeFileSync(path.join(evidenceRoot, `${width}-${theme}-${kind}.png`), screenshot);
            screenshots.push(screenshot);
          } finally { await context.close(); }
        }
        assert.equal(overflowWidths[1], overflowWidths[0], `${width}px ${theme} inline/external overflow parity`);
        assert.deepEqual(screenshots[1], screenshots[0], `${width}px ${theme} inline/external pixels`);
      }
    }
  } finally { await browser.close(); }
});
