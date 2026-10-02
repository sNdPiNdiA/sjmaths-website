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

test('CPU lesson reference deduplication initializes once and preserves content, language switching and pixels', { timeout: 180000 }, async () => {
  const file = 'ahc-ro-aro/computer-knowledge/cpu-architecture-registers/index.html';
  const url = `https://sjmaths.com/${file.slice(0, -10)}`;
  const original = execFileSync('git', ['show', `5d341a929ac7484c0c9c6e84486dab4e33a95995:${file}`], { cwd: ROOT, encoding: 'utf8', maxBuffer: 5e6 });
  const current = fs.readFileSync(path.join(fixtureRoot, file), 'utf8');
  const evidenceRoot = path.join(ROOT, 'scratch/refactor/ahc-language-dedupe', path.basename(fixtureRoot));
  fs.mkdirSync(evidenceRoot, { recursive: true });
  const browser = await chromium.launch({ headless: true });
  const results = [];
  try {
    for (const width of widths) {
      const outcomes = [];
      for (const [mode, html] of [['before', original], ['after', current]]) {
        const context = await browser.newContext({ viewport: { width, height: 900 }, reducedMotion: 'reduce', serviceWorkers: 'block' });
        try {
          const page = await context.newPage();
          const evidence = await routeRepositoryFixtures(page, { root: fixtureRoot, files: fixtureFiles(fixtureRoot) });
          const localErrors = [], externalErrors = [];
          page.on('pageerror', error => localErrors.push(error.message));
          page.on('console', message => {
            if (message.type() !== 'error' || message.text().startsWith('Service Worker registration failed')) return;
            let location;
            try { location = new URL(message.location().url); } catch { /* Unknown provenance remains a local failure. */ }
            if (location && !['sjmaths.com', 'www.sjmaths.com'].includes(location.hostname)) {
              externalErrors.push({ resource: location.origin + location.pathname, message: message.text() });
            } else localErrors.push(message.text());
          });
          await page.addInitScript(() => {
            if (!sessionStorage.getItem('__cpu_language_fixture')) {
              localStorage.setItem('sjmaths_preferred_language', 'hi');
              sessionStorage.setItem('__cpu_language_fixture', 'yes');
            }
            window.__cpuLanguageInitializers = 0;
            const add = EventTarget.prototype.addEventListener;
            EventTarget.prototype.addEventListener = function(type, listener, ...options) {
              if (this === document && type === 'DOMContentLoaded' && document.currentScript?.getAttribute('data-ahc-ro-aro-language') === 'shared') {
                window.__cpuLanguageInitializers++;
              }
              return add.call(this, type, listener, ...options);
            };
          });
          await page.route(url, route => route.fulfill({ contentType: 'text/html', body: html }));
          await page.goto(url, { waitUntil: 'networkidle' });
          if (await page.locator('script[src*="require-auth"]').count()) {
            const skip = page.locator('#sj-skip-gate-btn').first();
            await skip.waitFor({ state: 'visible', timeout: 15000 });
            await skip.click();
            await page.locator('#sj-auth-overlay').first().waitFor({ state: 'hidden' });
          }
          await page.evaluate(() => document.fonts.ready);
          assert.equal(await page.evaluate(() => window.__cpuLanguageInitializers), mode === 'before' ? 3 : 1);
          const read = () => page.evaluate(() => ({
            lang: document.documentElement.lang,
            pref: localStorage.getItem('sjmaths_preferred_language'),
            bodyHindi: document.body.classList.contains('lang-mode-hi'),
            labels: [...document.querySelectorAll('#langBtnText, #mobileLangBtnText, #navLangText')].map(node => node.textContent),
            notes: [...document.querySelectorAll('main')].map(node => node.innerText),
            overflow: Math.max(0, document.documentElement.scrollWidth - innerWidth),
          }));
          const hindi = await read();
          assert.equal(hindi.lang, 'hi');
          assert.equal(hindi.bodyHindi, true);
          const image = path.join(evidenceRoot, `${width}-${mode}.png`);
          await page.screenshot({ path: image, animations: 'disabled' });
          const toggle = page.locator('#headerLangToggleBtn').first();
          await toggle.waitFor({ state: 'visible' });
          await toggle.press('Enter');
          await page.reload({ waitUntil: 'networkidle' });
          const english = await read();
          assert.equal(english.lang, 'en');
          assert.equal(english.bodyHindi, false);
          outcomes.push({ hindi, english, image, errors: localErrors, externalErrors, missing: evidence.missing });
        } finally { await context.close(); }
      }
      fs.writeFileSync(path.join(evidenceRoot, `${width}-errors.json`), JSON.stringify(outcomes.map(({ errors, externalErrors }) => ({ errors, externalErrors })), null, 2) + '\n');
      for (const key of ['hindi', 'english', 'errors', 'missing']) assert.deepEqual(outcomes[1][key], outcomes[0][key], `${width}px ${key} parity`);
      const pixelPage = await browser.newPage();
      const pixels = await screenshotPixels(pixelPage, outcomes[0].image, outcomes[1].image);
      await pixelPage.close();
      assert.equal(pixels.pixelsChanged, 0, `${width}px visual parity`);
      results.push({ width, initializersBefore: 3, initializersAfter: 1, pixels, errors: outcomes[1].errors, externalErrors: outcomes[1].externalErrors, missing: outcomes[1].missing });
    }
    fs.writeFileSync(path.join(evidenceRoot, 'results.json'), JSON.stringify(results, null, 2) + '\n');
  } finally { await browser.close(); }
});

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
          await page.addInitScript(() => {
            const fixtureKey = '__sjmaths_ahc_language_fixture_initialized';
            if (sessionStorage.getItem(fixtureKey) !== 'yes') {
              localStorage.removeItem('sjmaths_preferred_language');
              sessionStorage.setItem(fixtureKey, 'yes');
            }
          });
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
          const hindiSelection = await readState();
          assert.equal(hindiSelection.language, 'hi');
          assert.equal(hindiSelection.buttonText, 'English');
          await page.reload({ waitUntil: 'networkidle' });
          const hindi = await readState();
          assert.equal(hindi.htmlLang, 'hi');
          assert.equal(hindi.bodyHindi, true);
          assert.equal(hindi.buttonText, 'English');

          await page.locator('#headerLangToggleBtn').press('Enter');
          const restoredEnglish = await readState();
          assert.equal(restoredEnglish.language, 'en');
          assert.equal(restoredEnglish.buttonText, english.buttonText);
          await page.reload({ waitUntil: 'networkidle' });
          const restoredEnglishAfterReload = await readState();
          assert.equal(restoredEnglishAfterReload.htmlLang, 'en');
          assert.equal(restoredEnglishAfterReload.bodyHindi, false);
          assert.equal(restoredEnglishAfterReload.language, 'en');
          const runtimeErrors = evidence.errors.filter(error => !error.startsWith('Service Worker registration failed'));
          outcomes.push({ mode, screenshotPath, english, hindi, restoredEnglish: restoredEnglishAfterReload, errors: runtimeErrors, missing: evidence.missing });
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

