const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { execFileSync } = require('node:child_process');
const { chromium } = require('playwright');
const { ROOT } = require('./seo-html.cjs');
const { fixtureFiles, routeRepositoryFixtures } = require('./lib/browser-fixture.cjs');

const baseline = '237db669da5fca0a8ff8ae6a5a601d284a367642';
const pages = [
  ['economy', 'upsssc-pet/economy/agricultural-reforms/index.html'],
  ['history', 'upsssc-pet/history/buddhism-gautam-buddha/index.html'],
  ['english', 'upsssc-pet/english/english-grammar/tenses/index.html'],
  ['general-awareness', 'upsssc-pet/general-awareness/awards-winners/index.html'],
];
const fixtureRoot = path.resolve(ROOT, process.env.SJ_REFACTOR_FIXTURE_ROOT || '.');

async function comparePngPixels(page, firstPath, secondPath) {
  const images = [firstPath, secondPath].map(file => fs.readFileSync(file).toString('base64'));
  return page.evaluate(async encoded => {
    const pixels = await Promise.all(encoded.map(async value => {
      const image = new Image();
      image.src = `data:image/png;base64,${value}`;
      await image.decode();
      const canvas = document.createElement('canvas');
      canvas.width = image.width;
      canvas.height = image.height;
      const context = canvas.getContext('2d');
      context.drawImage(image, 0, 0);
      return { width: image.width, height: image.height, data: context.getImageData(0, 0, image.width, image.height).data };
    }));
    if (pixels[0].width !== pixels[1].width || pixels[0].height !== pixels[1].height) throw new Error('Screenshot dimensions differ.');
    let pixelsChanged = 0;
    let maxChannelDelta = 0;
    let left = pixels[0].width, top = pixels[0].height, right = -1, bottom = -1;
    for (let offset = 0; offset < pixels[0].data.length; offset += 4) {
      let changed = false;
      for (let channel = 0; channel < 4; channel++) {
        const delta = Math.abs(pixels[0].data[offset + channel] - pixels[1].data[offset + channel]);
        maxChannelDelta = Math.max(maxChannelDelta, delta);
        changed ||= delta > 0;
      }
      if (changed) {
        pixelsChanged++;
        const pixel = offset / 4;
        const x = pixel % pixels[0].width, y = Math.floor(pixel / pixels[0].width);
        left = Math.min(left, x); right = Math.max(right, x);
        top = Math.min(top, y); bottom = Math.max(bottom, y);
      }
    }
    return { width: pixels[0].width, height: pixels[0].height, pixelsChanged, maxChannelDelta, bounds: pixelsChanged ? { left, top, right, bottom } : null };
  }, images);
}

test('shared language runtime preserves UPSSSC PET mobile and desktop bilingual UI', { timeout: 150000 }, async () => {
  const browser = await chromium.launch({ headless: true });
  const evidenceRoot = path.join(ROOT, 'scratch/refactor/upsssc-pet-language', path.basename(fixtureRoot));
  fs.mkdirSync(evidenceRoot, { recursive: true });
  const results = [];

  try {
    for (const width of [390, 1280]) {
      const context = await browser.newContext({ viewport: { width, height: 900 }, reducedMotion: 'reduce', serviceWorkers: 'block' });
      try {
        const page = await context.newPage();
        const evidence = await routeRepositoryFixtures(page, { root: fixtureRoot, files: fixtureFiles(fixtureRoot) });
        await page.addInitScript(() => { try { localStorage.setItem('sj_pref_lang', 'en'); } catch {} });
        await page.route('**/assets/js/require-auth.min.js*', route => route.fulfill({ contentType: 'text/javascript', body: '' }));

        for (const [id, file] of pages) {
          const url = `https://sjmaths.com/${file}`;
          const inlineHtml = execFileSync('git', ['show', `${baseline}:${file}`], { cwd: ROOT, encoding: 'utf8', maxBuffer: 20e6 });
          const externalHtml = fs.readFileSync(path.join(fixtureRoot, file), 'utf8');
          let activeHtml = inlineHtml;
          await page.route(url, route => route.fulfill({ contentType: 'text/html', body: activeHtml }));
          const outcomes = [];

          for (const [mode, html] of [['inline', inlineHtml], ['shared', externalHtml]]) {
            activeHtml = html;
            const errorsAt = evidence.errors.length;
            const missingAt = evidence.missing.length;
            await page.goto(url, { waitUntil: 'load', timeout: 20000 });
            await page.evaluate(() => document.fonts.ready);
            const unexpectedErrors = evidence.errors.slice(errorsAt).filter(error => !error.startsWith('Service Worker registration failed'));
            const missing = evidence.missing.slice(missingAt);
            assert.deepEqual(unexpectedErrors, [], `${id}/${mode} browser errors`);
            assert.deepEqual(missing, [], `${id}/${mode} missing local assets`);

            const initial = await page.evaluate(() => ({
              html: document.documentElement.className,
              body: document.body.className,
              en: document.getElementById('langEn')?.getAttribute('aria-pressed'),
              hi: document.getElementById('langHi')?.getAttribute('aria-pressed'),
              overflow: Math.max(0, document.documentElement.scrollWidth - innerWidth),
              geometry: ['h1', '#langEn', '#langHi', '.study-tabs'].map(selector => {
                const rect = document.querySelector(selector)?.getBoundingClientRect();
                return rect ? [rect.x, rect.y, rect.width, rect.height] : null;
              }),
            }));
            assert.equal(initial.en, 'true', `${id} starts in English`);
            assert.equal(initial.hi, 'false', `${id} English state is aria-consistent`);
            const englishShot = path.join(evidenceRoot, `${id}-${width}-${mode}-en.png`);
            await page.evaluate(() => { document.activeElement?.blur(); });
            await page.evaluate(() => new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve))));
            await page.screenshot({ path: englishShot, animations: 'disabled' });

            await page.locator('#langHi').click();
            const hindi = await page.evaluate(() => ({
              html: document.documentElement.className,
              body: document.body.className,
              en: document.getElementById('langEn')?.getAttribute('aria-pressed'),
              hi: document.getElementById('langHi')?.getAttribute('aria-pressed'),
              preference: localStorage.getItem('sj_pref_lang'),
              overflow: Math.max(0, document.documentElement.scrollWidth - innerWidth),
              text: document.body.innerText.slice(0, 240),
            }));
            assert.match(hindi.html, /lang-hi/);
            assert.match(hindi.body, /lang-hi/);
            assert.equal(hindi.en, 'false');
            assert.equal(hindi.hi, 'true');
            assert.equal(hindi.preference, 'hi');
            const hindiShot = path.join(evidenceRoot, `${id}-${width}-${mode}-hi.png`);
            await page.evaluate(() => { document.activeElement?.blur(); });
            await page.evaluate(() => new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve))));
            await page.screenshot({ path: hindiShot, animations: 'disabled' });
            await page.locator('#langEn').click();
            assert.equal(await page.locator('#langEn').getAttribute('aria-pressed'), 'true');
            assert.equal(await page.evaluate(() => localStorage.getItem('sj_pref_lang')), 'en');
          outcomes.push({ initial, hindi, englishShot, hindiShot, errors: unexpectedErrors, missing });
          }

          assert.deepEqual(outcomes[1].initial, outcomes[0].initial, `${id}/${width} English layout/state parity`);
          assert.deepEqual(outcomes[1].hindi, outcomes[0].hindi, `${id}/${width} Hindi layout/state parity`);
          assert.deepEqual(outcomes[1].errors, outcomes[0].errors);
          assert.deepEqual(outcomes[1].missing, outcomes[0].missing);
          const pixelDiffs = {};
          for (const state of ['englishShot', 'hindiShot']) {
            pixelDiffs[state] = await comparePngPixels(page, outcomes[0][state], outcomes[1][state]);
          }
          results.push({ id, width, state: 'English/Hindi toggles, ARIA and geometry verified', pixelDiffs });
        }
      } finally { await context.close(); }
    }
    fs.writeFileSync(path.join(evidenceRoot, 'results.json'), JSON.stringify({ baseline, results }, null, 2) + '\n');
  } finally { await browser.close(); }
});
