const test = require('node:test');
const assert = require('node:assert/strict');
const crypto = require('node:crypto');
const fs = require('node:fs');
const path = require('node:path');
const { execFileSync } = require('node:child_process');
const { chromium } = require('playwright');
const { ROOT } = require('./seo-html.cjs');
const { fixtureFiles, routeRepositoryFixtures } = require('./lib/browser-fixture.cjs');

const baseline = '5d341a929ac7484c0c9c6e84486dab4e33a95995';
const pages = [
  ['association', 'up-pgt-sociology/basic-sociological-concepts/association/index.html', '/up-pgt-sociology/basic-sociological-concepts/association/'],
  ['caste-system', 'up-pgt-sociology/caste-class-and-rural-power/caste-system/index.html', '/up-pgt-sociology/caste-class-and-rural-power/caste-system/'],
];
const fixtureRoot = path.resolve(ROOT, process.env.SJ_REFACTOR_FIXTURE_ROOT || '.');

test('Sociology bilingual CSS preserves mobile/desktop rendering, language switch and answer control', { timeout: 120000 }, async () => {
  const browser = await chromium.launch({ headless: true });
  const evidenceRoot = path.join(ROOT, 'scratch/refactor/sociology-bilingual-style', path.basename(fixtureRoot));
  fs.mkdirSync(evidenceRoot, { recursive: true });
  const summaries = [];

  try {
    for (const [id, file, route] of pages) for (const width of [390, 1280]) {
      const originalHtml = execFileSync('git', ['show', `${baseline}:${file}`], { cwd: ROOT, encoding: 'utf8', maxBuffer: 20e6 });
      const externalHtml = fs.readFileSync(path.join(fixtureRoot, file), 'utf8');
      const screenshots = [];

      for (const kind of ['inline', 'external']) {
        const context = await browser.newContext({ viewport: { width, height: 900 }, reducedMotion: 'reduce', serviceWorkers: 'block' });
        try {
          const page = await context.newPage();
          const evidence = await routeRepositoryFixtures(page, { root: fixtureRoot, files: fixtureFiles(fixtureRoot) });
          await page.addInitScript(() => localStorage.setItem('sjmaths_soc_lang', 'en'));
          if (kind === 'inline') {
            await page.route(`https://sjmaths.com${route}`, request => request.fulfill({ contentType: 'text/html', body: originalHtml }));
          }
          await page.goto(`https://sjmaths.com${route}`, { waitUntil: 'networkidle' });
          const skip = page.locator('#sj-skip-gate-btn');
          if (await page.locator('#sj-auth-overlay').count()) {
            await skip.waitFor({ state: 'visible', timeout: 15000 });
            await skip.click();
            await page.locator('#sj-auth-overlay').waitFor({ state: 'hidden' });
          }
          await page.evaluate(() => document.fonts.ready);
          if (kind === 'external') {
            const style = page.locator('link[data-sociology-bilingual-style="shared"]');
            assert.equal(await style.count(), 1);
            assert.match(await style.getAttribute('href'), /\/assets\/css\/sociology-bilingual-topic(?:\.min)?\.css(?:\?[^" ]*)?$/);
          }
          const state = await page.evaluate(() => ({
            overflow: Math.max(0, document.documentElement.scrollWidth - innerWidth),
            title: document.querySelector('h1')?.getBoundingClientRect().toJSON(),
            hero: document.querySelector('.topic-hero')?.getBoundingClientRect().toJSON(),
            language: document.documentElement.dataset.socLang,
          }));
          assert.equal(state.overflow, 0, `${id}/${kind}/${width} horizontal overflow`);
          const screenshotPath = path.join(evidenceRoot, `${id}-${width}-${kind}.png`);
          await page.screenshot({ path: screenshotPath, animations: 'disabled' });
          screenshots.push({ kind, screenshotPath, state, errors: evidence.errors, missing: evidence.missing });

          if (kind === 'external' && width === 390 && id === 'association') {
            const hindiButton = page.locator('.lang-btn[data-lang="hi"]').first();
            await hindiButton.focus();
            await page.keyboard.press('Enter');
            assert.equal(await page.locator('html').getAttribute('data-soc-lang'), 'hi');
            assert.equal(await page.locator('.lang-pane-hi').isVisible(), true);
            assert.equal(await page.locator('.lang-pane-en').isVisible(), false);
            const reveal = page.locator('.lang-pane-hi .btn-reveal').first();
            const explanation = page.locator('#hi-exp-0');
            await reveal.focus();
            await page.keyboard.press('Enter');
            await assert.doesNotReject(() => explanation.waitFor({ state: 'visible' }));
            summaries.push({ id, width, keyboardHindiSwitch: true, keyboardAnswerReveal: true });
          }
        } finally { await context.close(); }
      }

      assert.deepEqual(screenshots[1].state.title, screenshots[0].state.title, `${id}/${width} title geometry`);
      assert.deepEqual(screenshots[1].state.hero, screenshots[0].state.hero, `${id}/${width} hero geometry`);
      assert.equal(screenshots[1].state.overflow, screenshots[0].state.overflow, `${id}/${width} overflow parity`);
      assert.deepEqual(screenshots[1].errors, screenshots[0].errors);
      assert.deepEqual(screenshots[1].missing, screenshots[0].missing);
      const digest = filePath => crypto.createHash('sha256').update(fs.readFileSync(filePath)).digest('hex');
      assert.equal(digest(screenshots[1].screenshotPath), digest(screenshots[0].screenshotPath), `${id}/${width} initial screenshot`);
      summaries.push({ id, width, state: screenshots[1].state, screenshot: 'pixel-identical' });
    }
    fs.writeFileSync(path.join(evidenceRoot, 'results.json'), JSON.stringify({ fixtureRoot: path.relative(ROOT, fixtureRoot) || '.', baseline, summaries }, null, 2) + '\n');
  } finally { await browser.close(); }
});
