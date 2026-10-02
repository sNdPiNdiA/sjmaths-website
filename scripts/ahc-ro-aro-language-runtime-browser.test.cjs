const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { execFileSync } = require('node:child_process');
const { chromium } = require('playwright');
const { ROOT } = require('./seo-html.cjs');
const { fixtureFiles, routeRepositoryFixtures } = require('./lib/browser-fixture.cjs');

const baseline = '9dd18d6c9c2c8b8bc252757a2cd10d404d3e2773';
const pages = [
  ['agriculture', 'ahc-ro-aro/agriculture-commerce-trade/major-crops/index.html'],
  ['science', 'ahc-ro-aro/general-science/atomic-structure/index.html'],
];
const fixtureRoot = path.resolve(ROOT, process.env.SJ_REFACTOR_FIXTURE_ROOT || '.');
const widths = process.env.SJ_REFACTOR_WIDTH ? [Number(process.env.SJ_REFACTOR_WIDTH)] : [390, 1280];

async function screenshotPixels(page, first, second) {
  return page.evaluate(async images => {
    const decoded = await Promise.all(images.map(async data => {
      const image = new Image(); image.src = `data:image/png;base64,${data}`; await image.decode();
      const canvas = document.createElement('canvas'); canvas.width = image.width; canvas.height = image.height;
      const context = canvas.getContext('2d'); context.drawImage(image, 0, 0);
      return { width: image.width, height: image.height, data: context.getImageData(0, 0, image.width, image.height).data };
    }));
    if (decoded[0].width !== decoded[1].width || decoded[0].height !== decoded[1].height) throw new Error('Screenshot dimensions differ.');
    let pixelsChanged = 0, maxChannelDelta = 0;
    for (let index = 0; index < decoded[0].data.length; index += 4) {
      let changed = false;
      for (let channel = 0; channel < 4; channel++) {
        const delta = Math.abs(decoded[0].data[index + channel] - decoded[1].data[index + channel]);
        maxChannelDelta = Math.max(maxChannelDelta, delta);
        changed ||= delta !== 0;
      }
      if (changed) pixelsChanged++;
    }
    return { width: decoded[0].width, height: decoded[0].height, pixelsChanged, maxChannelDelta };
  }, [first, second].map(file => fs.readFileSync(file).toString('base64')));
}

test('AHC RO/ARO shared language controller preserves responsive rendering and keyboard language switching', { timeout: 240000 }, async () => {
  const browser = await chromium.launch({ headless: true });
  const evidenceRoot = path.join(ROOT, 'scratch/refactor/ahc-ro-aro-language', path.basename(fixtureRoot));
  fs.mkdirSync(evidenceRoot, { recursive: true });
  const results = [];

  try {
    for (const [id, file] of pages) for (const width of widths) {
      const directory = file.slice(0, file.lastIndexOf('/'));
      const url = `https://sjmaths.com/${directory}/`;
      const originalHtml = execFileSync('git', ['show', `${baseline}:${file}`], { cwd: ROOT, encoding: 'utf8', maxBuffer: 15e6 });
      const sharedHtml = fs.readFileSync(path.join(fixtureRoot, file), 'utf8');
      assert.match(sharedHtml, /data-ahc-ro-aro-language="shared"/);
      const outcomes = [];

      for (const [mode, html] of [['inline', originalHtml], ['shared', sharedHtml]]) {
        const context = await browser.newContext({ viewport: { width, height: 900 }, reducedMotion: 'reduce', serviceWorkers: 'block' });
        try {
          const page = await context.newPage();
          const evidence = await routeRepositoryFixtures(page, { root: fixtureRoot, files: fixtureFiles(fixtureRoot) });
          await page.addInitScript(() => localStorage.removeItem('sjmaths_preferred_language'));
          await page.route(url, route => route.fulfill({ contentType: 'text/html', body: html }));
          await page.goto(url, { waitUntil: 'networkidle' });
          await page.evaluate(() => document.fonts.ready);
          const toggle = page.locator('#headerLangToggleBtn');
          await toggle.waitFor({ state: 'visible' });
          assert.equal(await page.evaluate(() => typeof window.toggleLanguage), 'function', `${id}/${mode} language handler is attached`);
          const readState = () => page.evaluate(() => ({
            htmlLang: document.documentElement.lang,
            language: localStorage.getItem('sjmaths_preferred_language') || 'en',
            bodyEnglish: document.body.classList.contains('lang-mode-en'),
            bodyHindi: document.body.classList.contains('lang-mode-hi'),
            buttonText: document.querySelector('#headerLangToggleBtn')?.innerText.trim(),
            englishVisible: [...document.querySelectorAll('.lang-en')].filter(node => getComputedStyle(node).display !== 'none').length,
            hindiVisible: [...document.querySelectorAll('.lang-hi')].filter(node => getComputedStyle(node).display !== 'none').length,
            overflow: Math.max(0, document.documentElement.scrollWidth - innerWidth),
          }));
          const english = await readState();
          assert.equal(english.htmlLang, 'en');
          assert.equal(english.language, 'en');
          assert.equal(english.overflow, 0, `${id}/${width} horizontal overflow`);
          const screenshotPath = path.join(evidenceRoot, `${id}-${width}-${mode}.png`);
          await page.evaluate(() => { document.activeElement?.blur(); window.scrollTo(0, 0); });
          await page.screenshot({ path: screenshotPath, animations: 'disabled' });

          await toggle.press('Enter');
          const hindi = await readState();
          assert.equal(hindi.htmlLang, 'hi');
          assert.equal(hindi.language, 'hi');
          assert.equal(hindi.bodyHindi, true);
          assert.equal(hindi.buttonText, 'English');
          assert.ok(hindi.hindiVisible > 0);
          await page.reload({ waitUntil: 'networkidle' });
          const hindiAfterReload = await readState();
          assert.deepEqual(hindiAfterReload, hindi, `${id}/${mode} saved Hindi preference survives a reload`);

          await page.locator('#headerLangToggleBtn').press('Enter');
          const restoredEnglish = await readState();
          assert.equal(restoredEnglish.htmlLang, 'en');
          assert.equal(restoredEnglish.language, 'en');
          assert.equal(restoredEnglish.bodyHindi, false);
          assert.ok(restoredEnglish.englishVisible > 0);
          await page.reload({ waitUntil: 'networkidle' });
          const restoredEnglishAfterReload = await readState();
          assert.deepEqual(restoredEnglishAfterReload, restoredEnglish, `${id}/${mode} saved English preference survives a reload`);
          outcomes.push({ mode, screenshotPath, english, hindi, restoredEnglish, errors: evidence.errors, missing: evidence.missing });
        } finally { await context.close(); }
      }

      assert.deepEqual(outcomes[1].english, outcomes[0].english, `${id}/${width} English state parity`);
      assert.deepEqual(outcomes[1].hindi, outcomes[0].hindi, `${id}/${width} Hindi state parity`);
      assert.deepEqual(outcomes[1].restoredEnglish, outcomes[0].restoredEnglish, `${id}/${width} return-to-English parity`);
      assert.deepEqual(outcomes[1].errors, outcomes[0].errors, `${id}/${width} runtime error parity`);
      assert.deepEqual(outcomes[1].missing, outcomes[0].missing, `${id}/${width} asset parity`);
      const pixelPage = await browser.newPage();
      const pixels = await screenshotPixels(pixelPage, outcomes[0].screenshotPath, outcomes[1].screenshotPath);
      await pixelPage.close();
      assert.equal(pixels.pixelsChanged, 0, `${id}/${width} visual parity: ${JSON.stringify(pixels)}`);
      results.push({ id, width, english: outcomes[1].english, hindi: outcomes[1].hindi, pixels });
    }
    fs.writeFileSync(path.join(evidenceRoot, 'results.json'), JSON.stringify({ baseline, fixtureRoot: path.relative(ROOT, fixtureRoot) || '.', results }, null, 2) + '\n');
  } finally { await browser.close(); }
});

