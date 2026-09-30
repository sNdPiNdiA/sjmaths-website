// Local navigation/layout fixtures; shared authentication and analytics are not exercised.
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const cheerio = require('cheerio');
const { chromium } = require('playwright');
const { ROOT, siteFiles } = require('./seo-html.cjs');
const { createResolver } = require('./seo-routes.cjs');
const { routeRepositoryFixtures } = require('./lib/browser-fixture.cjs');

const files = siteFiles();
const resolve = createResolver(files);

async function prepare(page) {
  const evidence = await routeRepositoryFixtures(page, { root: ROOT, files });
  await page.route('https://sjmaths.com/**', async route => {
    const resolved = resolve(route.request().url());
    if (resolved.redirect || !resolved.file?.endsWith('.html')) return route.fallback();
    const dom = cheerio.load(fs.readFileSync(path.join(ROOT, resolved.file), 'utf8'));
    dom('script[type="module"], script[src^="/assets/js/"], script[src*="googlesyndication"]').remove();
    return route.fulfill({ contentType: 'text/html', body: dom.html() });
  });
  return evidence;
}

async function noOverflow(page) {
  assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1), page.url() + ' overflows');
}

test('current hubs, native exercise disclosures and deep-linked tabs work on mobile/tablet/desktop', { timeout: 120000 }, async () => {
  const browser = await chromium.launch({ headless: true });
  try {
    for (const width of [390, 768, 1440]) {
      const context = await browser.newContext({ viewport: { width, height: 900 }, reducedMotion: 'reduce', serviceWorkers: 'block' });
      try {
        const page = await context.newPage();
        const evidence = await prepare(page);
        await page.goto('https://sjmaths.com/class-9-maths/', { waitUntil: 'domcontentloaded' });
        assert.equal(await page.locator('#chapters-grid .ch-card-item').count(), 14);
        await noOverflow(page);
        if (width === 390) {
          fs.mkdirSync(path.join(ROOT, 'scratch'), { recursive: true });
          await page.screenshot({ path: path.join(ROOT, 'scratch/class-9-hub-mobile.png'), fullPage: true });
        }
        await page.locator('#search-input').fill('Ch 13');
        await page.locator('#search-input').press('ArrowRight');
        assert.equal(await page.locator('#chapters-grid .ch-card-item:visible').count(), 1);
        assert.match(await page.locator('#chapters-grid .ch-card-item:visible').innerText(), /Two Variables/);
        await page.locator('#search-input').fill('');
        await page.locator('#unit-filter').selectOption('logic');
        assert.equal(await page.locator('#chapters-grid .ch-card-item:visible').count(), 1);
        assert.match(await page.locator('#chapters-grid .ch-card-item:visible').innerText(), /Propositions/);
        await page.goto('https://sjmaths.com/class-9-maths/chapter-wise-notes/');
        assert.equal(await page.locator('main .chapter-card').count(), 14);
        await noOverflow(page);
        await page.goto('https://sjmaths.com/class-9-maths/ncert-exercise-practice/');
        await noOverflow(page);
        const chapter = page.locator('#chapter-grid > details').nth(11);
        await chapter.locator('summary').focus();
        await page.keyboard.press('Enter');
        assert.ok(await chapter.getAttribute('open') !== null);
        await chapter.locator('a[href$="#exercise-12-3"]').click();
        await page.waitForURL('**/#exercise-12-3');
        assert.ok(await page.locator('#exercise-12-3').isVisible());
        assert.equal(await page.locator('#p-notes').isVisible(), false);
        assert.equal(await page.locator('.subpanel:visible').count(), 1);
        await noOverflow(page);
        await page.locator('#exercise-12-3 .exercise-stepper-next').click();
        assert.ok(await page.locator('#exercise-12-4').isVisible());
        await page.locator('#tab-notes').click();
        assert.ok(await page.locator('#p-notes').isVisible());
        assert.equal(await page.locator('#p-exercises').isVisible(), false);
        await page.goto('https://sjmaths.com/class-9-maths/previous-syllabus/');
        await noOverflow(page);
        assert.equal(await page.locator('.archive-topic').count(), 5);
        assert.equal(await page.locator('.archive-page nav').evaluate(el => getComputedStyle(el).position), 'static');
        const breadcrumb = await page.locator('.archive-page nav').boundingBox();
        const heading = await page.locator('.archive-page h1').boundingBox();
        assert.ok(breadcrumb.y + breadcrumb.height <= heading.y, 'breadcrumbs must not overlap the heading');
        if (width === 390) {
          fs.mkdirSync(path.join(ROOT, 'scratch'), { recursive: true });
          await page.screenshot({ path: path.join(ROOT, 'scratch/class-9-archive-mobile.png'), fullPage: true });
        }
        // Routing fixtures cannot prove deployed HTTP redirects. Those rules are
        // checked separately; load the local destination to check its interface.
        await page.goto('https://sjmaths.com/class-9-ganita-manjari-part-2/chapter-14-surface-area-and-volume/');
        assert.equal(new URL(page.url()).pathname, '/class-9-ganita-manjari-part-2/chapter-14-surface-area-and-volume/');
        assert.deepEqual(evidence.missing, []);
        assert.deepEqual(evidence.errors, []);
      } finally { await context.close(); }
    }
    const context = await browser.newContext({ javaScriptEnabled: false, viewport: { width: 390, height: 900 } });
    try {
      const page = await context.newPage();
      await prepare(page);
      await page.goto('https://sjmaths.com/class-9-maths/ncert-exercise-practice/');
      await page.locator('#chapter-grid > details').nth(13).locator('summary').click();
      assert.ok(await page.locator('#chapter-grid a[href$="#exercise-14-1"]').isVisible());
      assert.ok(await page.locator('#chapter-grid a[href$="#exercise-eoc"]').last().isVisible());
    } finally { await context.close(); }
  } finally { await browser.close(); }
});
