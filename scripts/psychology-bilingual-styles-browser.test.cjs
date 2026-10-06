const test = require('node:test');
const assert = require('node:assert/strict');
const crypto = require('node:crypto');
const fs = require('node:fs');
const path = require('node:path');
const { chromium } = require('playwright');
const { ROOT } = require('./seo-html.cjs');
const { fixtureFiles, routeRepositoryFixtures } = require('./lib/browser-fixture.cjs');

const pages = [
  ['bilingual', 'psychology/abnormal-psychology/abnormal-behavior/contemporary-perspectives/index.html', '/psychology/abnormal-psychology/abnormal-behavior/contemporary-perspectives/'],
  ['english-variant', 'psychology/application-of-psychology/guidance-and-counselling/counselling-processes/index.html', '/psychology/application-of-psychology/guidance-and-counselling/counselling-processes/'],
];
const fixtureRoot = path.resolve(ROOT, process.env.SJ_REFACTOR_FIXTURE_ROOT || '.');

test('Psychology bilingual CSS preserves mobile/desktop rendering, language switch and answer controls', { timeout: 120000 }, async () => {
  const browser = await chromium.launch({ headless: true });
  const evidenceRoot = path.join(ROOT, 'scratch/refactor/psychology-bilingual-style', path.basename(fixtureRoot));
  fs.mkdirSync(evidenceRoot, { recursive: true });
  const summaries = [];

  try {
    for (const [id, file, route] of pages) for (const width of [390, 1280]) {
      const externalHtml = fs.readFileSync(path.join(fixtureRoot, file), 'utf8');
      const migrated = externalHtml.includes('data-psychology-bilingual-style="shared"');
      const sharedStyle = externalHtml.match(/<link\b(?=[^>]*data-psychology-bilingual-style="shared")[^>]*href="([^"]+)"[^>]*>/i);
      const inlineHtml = sharedStyle
        ? externalHtml.replace(sharedStyle[0], () => {
            const stylePath = new URL(sharedStyle[1], 'https://sjmaths.com').pathname;
            const css = fs.readFileSync(path.join(ROOT, stylePath.replace(/^\//, '')), 'utf8');
            return `<style>${css}</style>`;
          })
        : externalHtml;
      const screenshots = [];

      for (const [kind, html] of [['inline', inlineHtml], ['external', externalHtml]]) {
        const context = await browser.newContext({ viewport: { width, height: 900 }, reducedMotion: 'reduce', serviceWorkers: 'block' });
        try {
          const page = await context.newPage();
          const evidence = await routeRepositoryFixtures(page, { root: fixtureRoot, files: fixtureFiles(fixtureRoot) });
          await page.addInitScript(() => localStorage.setItem('sjmaths_psych_lang', 'en'));
          await page.route(`https://sjmaths.com${route}`, request => request.fulfill({ contentType: 'text/html', body: html }));
          await page.goto(`https://sjmaths.com${route}`, { waitUntil: 'networkidle' });
          const skip = page.locator('#sj-skip-gate-btn');
          if (await page.locator('script[src*="require-auth"]').count()) {
            await skip.waitFor({ state: 'visible', timeout: 15000 });
            await skip.click();
            await page.locator('#sj-auth-overlay').waitFor({ state: 'hidden' });
          }
          await page.evaluate(() => document.fonts.ready);
          if (kind === 'external' && migrated) {
            const style = page.locator('link[data-psychology-bilingual-style="shared"]');
            assert.equal(await style.count(), 1);
            assert.match(await style.getAttribute('href'), /\/assets\/css\/psychology-bilingual-topic(?:\.min)?\.css(?:\?[^" ]*)?$/);
          }
          const state = await page.evaluate(() => ({
            overflow: Math.max(0, document.documentElement.scrollWidth - innerWidth),
            title: document.querySelector('h1')?.getBoundingClientRect().toJSON(),
            hero: document.querySelector('.topic-hero')?.getBoundingClientRect().toJSON(),
            language: document.documentElement.dataset.psychLang,
          }));
          assert.equal(state.overflow, 0, `${id}/${kind}/${width} horizontal overflow`);
          const screenshotPath = path.join(evidenceRoot, `${id}-${width}-${kind}.png`);
          await page.screenshot({ path: screenshotPath, animations: 'disabled' });
          screenshots.push({ kind, screenshotPath, state, errors: evidence.errors, missing: evidence.missing });

          if (id === 'bilingual' && kind === 'external' && width === 390) {
            const hindiButton = page.locator('.lang-btn[data-lang="hi"]').first();
            await hindiButton.focus();
            await page.keyboard.press('Enter');
            assert.equal(await page.locator('html').getAttribute('data-psych-lang'), 'hi');
            assert.equal(await page.locator('.lang-pane-hi').isVisible(), true);
            assert.equal(await page.locator('.lang-pane-en').isVisible(), false);
            const reveal = page.locator('#hi-exp-0').locator('..').locator('.btn-reveal');
            await reveal.focus();
            await page.keyboard.press('Enter');
            assert.equal(await page.locator('#hi-exp-0').isVisible(), true);
            summaries.push({ id, width, languageKeyboardSwitch: 'Hindi pane visible; English pane hidden', answerKeyboardReveal: true });
          }
        } finally { await context.close(); }
      }

      assert.equal(screenshots[1].state.overflow, screenshots[0].state.overflow, `${id}/${width} overflow parity`);
      assert.deepEqual(screenshots[1].state.title, screenshots[0].state.title, `${id}/${width} title geometry`);
      assert.deepEqual(screenshots[1].state.hero, screenshots[0].state.hero, `${id}/${width} hero geometry`);
      assert.deepEqual(screenshots[1].errors, screenshots[0].errors);
      assert.deepEqual(screenshots[1].missing, screenshots[0].missing);
      const digest = filePath => crypto.createHash('sha256').update(fs.readFileSync(filePath)).digest('hex');
      assert.equal(digest(screenshots[1].screenshotPath), digest(screenshots[0].screenshotPath), `${id}/${width} initial screenshot`);
      summaries.push({ id, width, state: screenshots[1].state, screenshot: 'pixel-identical' });
    }
    fs.writeFileSync(path.join(evidenceRoot, 'results.json'), JSON.stringify({ fixtureRoot: path.relative(ROOT, fixtureRoot) || '.', summaries }, null, 2) + '\n');
  } finally { await browser.close(); }
});
