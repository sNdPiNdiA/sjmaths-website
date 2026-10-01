const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const { execFileSync } = require('node:child_process');
const { chromium } = require('playwright');
const { ROOT } = require('./seo-html.cjs');
const { fixtureFiles, routeRepositoryFixtures } = require('./lib/browser-fixture.cjs');

const baseline = '237db669da5fca0a8ff8ae6a5a601d284a367642';
const pages = [
  ['class-11', 'class-11-maths/chapter-wise-notes/chapter-1-sets/index.html'],
  ['class-12', 'class-12-maths/chapter-wise-notes/chapter-7-integrals/index.html'],
  ['class-9', 'class-9-maths/chapter-wise-notes/chapter-9-triangles/index.html'],
  ['previous-syllabus', 'class-9-maths/previous-syllabus/circles/index.html'],
].filter(([id]) => !process.env.SJ_REFACTOR_PAGE || id === process.env.SJ_REFACTOR_PAGE);
const fixtureRoot = path.resolve(ROOT, process.env.SJ_REFACTOR_FIXTURE_ROOT || '.');

async function screenshotPixels(page, first, second) {
  return page.evaluate(async images => {
    const decoded = await Promise.all(images.map(async data => {
      const image = new Image(); image.src = `data:image/png;base64,${data}`; await image.decode();
      const canvas = document.createElement('canvas'); canvas.width = image.width; canvas.height = image.height;
      const context = canvas.getContext('2d'); context.drawImage(image, 0, 0);
      return { width: image.width, height: image.height, data: context.getImageData(0, 0, image.width, image.height).data };
    }));
    if (decoded[0].width !== decoded[1].width || decoded[0].height !== decoded[1].height) throw new Error('Screenshot dimensions differ.');
    let pixelsChanged = 0;
    for (let i = 0; i < decoded[0].data.length; i += 4) {
      if (decoded[0].data[i] !== decoded[1].data[i] || decoded[0].data[i + 1] !== decoded[1].data[i + 1]
        || decoded[0].data[i + 2] !== decoded[1].data[i + 2] || decoded[0].data[i + 3] !== decoded[1].data[i + 3]) pixelsChanged++;
    }
    return { width: decoded[0].width, height: decoded[0].height, pixelsChanged };
  }, [first, second].map(file => fs.readFileSync(file).toString('base64')));
}

test('shared chapter controller preserves hidden handlers and baseline content state', { timeout: 180000 }, async () => {
  const browser = await chromium.launch({ headless: true });
  const evidenceRoot = path.join(ROOT, 'scratch/refactor/chapter-reader-tabs', path.basename(fixtureRoot));
  fs.mkdirSync(evidenceRoot, { recursive: true });
  const results = [];

  try {
    for (const [id, file] of pages) for (const width of [390, 1280]) {
      const context = await browser.newContext({ viewport: { width, height: 900 }, reducedMotion: 'reduce', serviceWorkers: 'block' });
      try {
        const page = await context.newPage();
        const evidence = await routeRepositoryFixtures(page, { root: fixtureRoot, files: fixtureFiles(fixtureRoot) });
        const failedResponses = [];
        page.on('response', response => {
          if (response.status() >= 400) failedResponses.push({ status: response.status(), url: response.url() });
        });
        await page.route('**/assets/js/require-auth.min.js*', route => route.fulfill({ contentType: 'text/javascript', body: '' }));
        const url = `https://sjmaths.com/${file}`;
        const inlineHtml = execFileSync('git', ['show', `${baseline}:${file}`], { cwd: ROOT, encoding: 'utf8', maxBuffer: 25e6 });
        const sharedHtml = fs.readFileSync(path.join(fixtureRoot, file), 'utf8');
        assert.match(sharedHtml, /data-chapter-reader-tabs="shared"/);
        let activeHtml = inlineHtml;
        await page.route(url, route => route.fulfill({ contentType: 'text/html', body: activeHtml }));
        const outcomes = [];

        for (const [mode, html] of [['inline', inlineHtml], ['shared', sharedHtml]]) {
          activeHtml = html;
          const errorsAt = evidence.errors.length, missingAt = evidence.missing.length;
          await page.goto('about:blank');
          await page.goto(url, { waitUntil: 'load', timeout: 20000 });
          await page.evaluate(async () => {
            await document.fonts.ready;
            if (window.MathJax?.startup?.promise) await window.MathJax.startup.promise.catch(() => {});
          });
          await page.waitForTimeout(2500);
          const errors = evidence.errors.slice(errorsAt).filter(error => !error.startsWith('Service Worker registration failed'));
          const missing = evidence.missing.slice(missingAt);
          assert.deepEqual(errors, [], `${id}/${mode} browser errors; HTTP failures: ${JSON.stringify(failedResponses.slice(-8))}`);
          assert.deepEqual(missing, [], `${id}/${mode} missing local assets`);
          const state = await page.evaluate(() => ({
            overflow: Math.max(0, document.documentElement.scrollWidth - innerWidth),
            navItems: document.querySelectorAll('.nav-tab-item').length,
            activePills: document.querySelectorAll('.nav-tab-pill.active').length,
            title: document.querySelector('.chapter-title')?.getBoundingClientRect().toJSON(),
            contentLength: document.querySelector('.content-wrapper')?.innerText.length,
            contentExcerpt: document.querySelector('.content-wrapper')?.innerText.slice(0, 600),
            notesDisplay: document.getElementById('notes-tab-content')?.style.display ?? null,
            iframeDisplay: document.getElementById('iframe-tab-content')?.style.display,
            iframeSrc: document.getElementById('tab-iframe')?.getAttribute('src'),
            drawerActive: document.getElementById('dockDrawerOverlay')?.classList.contains('active'),
            dockButtons: document.querySelectorAll('.mobile-dock-btn').length,
          }));
          assert.ok(state.navItems >= 2, `${id} tab navigation exists`);
          assert.equal(state.activePills, 1, `${id} exactly one active desktop tab`);
          const screenshot = path.join(evidenceRoot, `${id}-${width}-${mode}.png`);
          await page.evaluate(() => document.activeElement?.blur());
          await page.screenshot({ path: screenshot, animations: 'disabled' });
          // The notes-first layout intentionally hides this legacy resource UI;
          // invoke its native DOM handlers directly to check retained behavior.
          let flow;

          if (width === 1280) {
            const ncert = page.locator('.nav-tab-pill.ncert-tab').first();
            const item = ncert.locator('xpath=..');
            await ncert.evaluate(element => element.click());
            assert.equal(await item.evaluate(element => element.classList.contains('active-open')), true, `${id} dropdown opens`);
            await page.evaluate(() => document.body.dispatchEvent(new MouseEvent('click', { bubbles: true })));
            assert.equal(await item.evaluate(element => element.classList.contains('active-open')), false, `${id} outside click closes dropdown`);
            await ncert.evaluate(element => element.click());
            await item.locator('a.nav-dropdown-item').first().evaluate(element => element.click());
            const desktopState = await page.evaluate(() => ({
              iframeDisplay: document.getElementById('iframe-tab-content').style.display,
              iframeSrc: document.getElementById('tab-iframe').getAttribute('src'),
              activePills: document.querySelectorAll('.nav-tab-pill.active').length,
              openDropdowns: document.querySelectorAll('.nav-tab-item.active-open').length,
            }));
            assert.equal(desktopState.iframeDisplay, 'block');
            assert.equal(desktopState.activePills, 1);
            assert.ok(desktopState.iframeSrc.startsWith('/'), `${id} dropdown link opens its local solution in the iframe`);
            flow = desktopState;
          } else {
            const drawerButton = page.locator('.mobile-dock-btn[onclick^="openMobileDockDrawer"]').first();
            await drawerButton.evaluate(element => element.click());
            const drawer = page.locator('#dockDrawerOverlay');
            assert.equal(await drawer.evaluate(element => element.classList.contains('active')), true, `${id} mobile drawer opens`);
            assert.ok(await page.locator('#dockDrawerContent a.nav-dropdown-item').count() > 0, `${id} drawer clones resource links`);
            await page.locator('#dockDrawerContent a.nav-dropdown-item').first().evaluate(element => element.click());
            const mobileState = await page.evaluate(() => ({
              iframeDisplay: document.getElementById('iframe-tab-content').style.display,
              iframeSrc: document.getElementById('tab-iframe').getAttribute('src'),
              drawerActive: document.getElementById('dockDrawerOverlay').classList.contains('active'),
            }));
            assert.equal(mobileState.iframeDisplay, 'block');
            assert.equal(mobileState.drawerActive, false);
            assert.ok(mobileState.iframeSrc.startsWith('/'), `${id} drawer link opens its local resource in the iframe`);
            flow = mobileState;
          }
          outcomes.push({ mode, state, flow, screenshot, errors, missing });
        }

        assert.deepEqual(outcomes[1].state, outcomes[0].state, `${id}/${width} initial layout parity`);
        assert.deepEqual(outcomes[1].flow, outcomes[0].flow, `${id}/${width} interaction parity`);
        assert.deepEqual(outcomes[1].errors, outcomes[0].errors);
        assert.deepEqual(outcomes[1].missing, outcomes[0].missing);
        const pixels = await screenshotPixels(page, outcomes[0].screenshot, outcomes[1].screenshot);
        // This reader's pagination/MathJax presentation is asynchronous across
        // reloads; retain pixel deltas for inspection but gate source text,
        // geometry, controls and actual tab/drawer behavior exactly.
        results.push({ id, width, flow: outcomes[1].flow, pixels });
      } finally { await context.close(); }
    }
    fs.writeFileSync(path.join(evidenceRoot, 'results.json'), JSON.stringify({ baseline, fixtureRoot: path.relative(ROOT, fixtureRoot) || '.', results }, null, 2) + '\n');
  } finally { await browser.close(); }
});
