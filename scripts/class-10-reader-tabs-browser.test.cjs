const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { execFileSync } = require('node:child_process');
const { chromium } = require('playwright');
const { ROOT } = require('./seo-html.cjs');
const { fixtureFiles, routeRepositoryFixtures } = require('./lib/browser-fixture.cjs');

const baseline = 'afb5a3473445d7609eb3004b999c66b9d0215c70';
const file = 'class-10-maths/chapter-wise-notes/chapter-1-real-numbers/index.html';
const fixtureRoot = path.resolve(ROOT, process.env.SJ_REFACTOR_FIXTURE_ROOT || '.');

async function comparePixels(page, firstPath, secondPath) {
  return page.evaluate(async images => {
    const decoded = await Promise.all(images.map(async data => {
      const image = new Image();
      image.src = `data:image/png;base64,${data}`;
      await image.decode();
      const canvas = document.createElement('canvas');
      canvas.width = image.width;
      canvas.height = image.height;
      const context = canvas.getContext('2d');
      context.drawImage(image, 0, 0);
      return { width: image.width, height: image.height, data: context.getImageData(0, 0, image.width, image.height).data };
    }));
    if (decoded[0].width !== decoded[1].width || decoded[0].height !== decoded[1].height) throw new Error('Screenshot dimensions differ.');
    let pixelsChanged = 0;
    for (let index = 0; index < decoded[0].data.length; index += 4) {
      if (decoded[0].data[index] !== decoded[1].data[index]
        || decoded[0].data[index + 1] !== decoded[1].data[index + 1]
        || decoded[0].data[index + 2] !== decoded[1].data[index + 2]
        || decoded[0].data[index + 3] !== decoded[1].data[index + 3]) pixelsChanged++;
    }
    return { width: decoded[0].width, height: decoded[0].height, pixelsChanged };
  }, [firstPath, secondPath].map(imagePath => fs.readFileSync(imagePath).toString('base64')));
}

test('Class 10 resource tabs preserve page state and desktop/mobile handlers', { timeout: 120000 }, async () => {
  const browser = await chromium.launch({ headless: true });
  const evidenceRoot = path.join(ROOT, 'scratch/refactor/class-10-reader-tabs', path.basename(fixtureRoot));
  fs.mkdirSync(evidenceRoot, { recursive: true });
  const screenshots = {};
  const reports = [];
  try {
    const inlineHtml = execFileSync('git', ['show', `${baseline}:${file}`], { cwd: ROOT, encoding: 'utf8', maxBuffer: 20e6 });
    const sharedHtml = fs.readFileSync(path.join(fixtureRoot, file), 'utf8');
    assert.match(sharedHtml, /data-class-10-reader-tabs="shared"/);

    for (const width of [390, 1280]) {
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
        let activeHtml = inlineHtml;
        await page.route(url, route => route.fulfill({ contentType: 'text/html', body: activeHtml }));
        const captures = {};

        for (const [mode, html] of [['inline', inlineHtml], ['shared', sharedHtml]]) {
          activeHtml = html;
          const errorsAt = evidence.errors.length;
          const missingAt = evidence.missing.length;
          await page.goto('about:blank');
          await page.goto(url, { waitUntil: 'load', timeout: 20000 });
          await page.evaluate(async () => {
            await document.fonts.ready;
            if (window.MathJax?.startup?.promise) await window.MathJax.startup.promise.catch(() => {});
          });
          await page.waitForTimeout(1500);
          const state = await page.evaluate(() => {
            const rect = selector => {
              const element = document.querySelector(selector);
              if (!element) return null;
              const { x, y, width: w, height } = element.getBoundingClientRect();
              return [x, y, w, height].map(value => Math.round(value * 10) / 10);
            };
            return {
              overflow: Math.max(0, document.documentElement.scrollWidth - innerWidth),
              pageHeight: document.documentElement.scrollHeight,
              heading: document.querySelector('h1')?.textContent.trim(),
              contentLength: document.querySelector('main')?.innerText.length,
              contentExcerpt: document.querySelector('main')?.innerText.slice(0, 500),
              headingRect: rect('h1'),
              contentRect: rect('main'),
              navHidden: getComputedStyle(document.querySelector('.chapter-nav-wrapper')).display === 'none',
              dockHidden: getComputedStyle(document.querySelector('.mobile-floating-dock')).display === 'none',
              iframeHidden: getComputedStyle(document.querySelector('#iframe-tab-content')).display === 'none',
              activePills: document.querySelectorAll('.nav-tab-pill.active').length,
            };
          });
          assert.equal(state.navHidden, true, 'notes-first desktop resource navigation remains hidden');
          assert.equal(state.dockHidden, true, 'notes-first mobile resource dock remains hidden');
          assert.equal(state.iframeHidden, true, 'notes-first iframe remains hidden');
          assert.equal(state.activePills, 1);
          const errors = evidence.errors.slice(errorsAt).filter(error => !error.startsWith('Service Worker registration failed'));
          const missing = evidence.missing.slice(missingAt);
          assert.deepEqual(errors, [], `${mode} browser errors; HTTP failures: ${JSON.stringify(failedResponses.slice(-8))}`);
          assert.deepEqual(missing, [], `${mode} missing local assets`);
          const shotPath = path.join(evidenceRoot, `${width}-${mode}.png`);
          await page.evaluate(() => document.activeElement?.blur());
          await page.screenshot({ path: shotPath, animations: 'disabled' });
          captures[mode] = { state, shotPath };

          if (width === 1280) {
            const pill = page.locator('.nav-tab-pill.ncert-tab').first();
            const navItem = pill.locator('xpath=..');
            await pill.evaluate(element => element.click());
            assert.equal(await navItem.evaluate(element => element.classList.contains('active-open')), true);
            await page.evaluate(() => document.body.dispatchEvent(new MouseEvent('click', { bubbles: true })));
            assert.equal(await navItem.evaluate(element => element.classList.contains('active-open')), false);
            await pill.evaluate(element => element.click());
            await navItem.locator('a.nav-dropdown-item').first().evaluate(element => element.click());
            await page.waitForFunction(() => {
              const frame = document.getElementById('tab-iframe');
              return frame?.contentDocument?.readyState === 'complete'
                && frame.contentDocument.location.href === frame.src
                && frame.contentDocument.head;
            }, null, { timeout: 20000 });
            const desktopFlow = await page.evaluate(() => ({
              iframeDisplay: document.getElementById('iframe-tab-content').style.display,
              iframePath: new URL(document.getElementById('tab-iframe').src).pathname,
              breadcrumbDisplay: document.querySelector('.breadcrumb').style.display,
              navDisplay: document.querySelector('.nav-buttons').style.display,
              mainDisplay: document.querySelector('main').style.display,
              embeddedHeaderDisplay: document.getElementById('tab-iframe').contentDocument.getElementById('header-container')?.style.display ?? null,
              embeddedFooterDisplay: document.getElementById('tab-iframe').contentDocument.getElementById('footer-container')?.style.display ?? null,
              embeddedOverridesPresent: [...document.getElementById('tab-iframe').contentDocument.head.querySelectorAll('style')]
                .some(style => style.textContent.includes('#themeToggle, .question-nav.bottom')),
              iframeHeightStyle: document.getElementById('tab-iframe').style.height,
              iframePanelHeightStyle: document.getElementById('iframe-tab-content').style.height,
            }));
            assert.equal(desktopFlow.iframeDisplay, 'block');
            assert.equal(desktopFlow.breadcrumbDisplay, 'none');
            assert.equal(desktopFlow.navDisplay, 'none');
            assert.equal(desktopFlow.mainDisplay, 'none');
            assert.ok([null, 'none'].includes(desktopFlow.embeddedHeaderDisplay));
            assert.ok([null, 'none'].includes(desktopFlow.embeddedFooterDisplay));
            assert.equal(desktopFlow.embeddedOverridesPresent, true);
            assert.ok(parseFloat(desktopFlow.iframeHeightStyle) > 0);
            assert.ok(parseFloat(desktopFlow.iframePanelHeightStyle) > 0);
            await page.locator('.nav-tab-pill.notes-tab').evaluate(element => element.click());
            assert.equal(await page.locator('main').evaluate(element => element.style.display), '');
            assert.equal(await page.locator('#iframe-tab-content').evaluate(element => element.style.display), 'none');
          } else {
            await page.locator('.mobile-dock-btn[onclick^="openMobileDockDrawer"]').first().evaluate(element => element.click());
            const drawer = page.locator('#dockDrawerOverlay');
            assert.equal(await drawer.evaluate(element => element.classList.contains('active')), true);
            assert.ok(await page.locator('#dockDrawerContent a.nav-dropdown-item').count() > 0);
            await page.locator('#dockDrawerContent a.nav-dropdown-item').first().evaluate(element => element.click());
            await page.waitForFunction(() => {
              const frame = document.getElementById('tab-iframe');
              return frame?.contentDocument?.readyState === 'complete'
                && frame.contentDocument.location.href === frame.src
                && frame.contentDocument.head;
            }, null, { timeout: 20000 });
            const mobileFlow = await page.evaluate(() => ({
              iframeDisplay: document.getElementById('iframe-tab-content').style.display,
              iframePath: new URL(document.getElementById('tab-iframe').src).pathname,
              drawerActive: document.getElementById('dockDrawerOverlay').classList.contains('active'),
              mainDisplay: document.querySelector('main').style.display,
            }));
            assert.equal(mobileFlow.iframeDisplay, 'block');
            assert.equal(mobileFlow.drawerActive, false);
            assert.equal(mobileFlow.mainDisplay, 'none');
          }
        }

        assert.deepEqual(captures.shared.state, captures.inline.state, `${width}px initial page state parity`);
        reports.push({ width, pixels: await comparePixels(page, captures.inline.shotPath, captures.shared.shotPath) });
      } finally {
        await context.close();
      }
    }
    fs.writeFileSync(path.join(evidenceRoot, 'screenshot-diffs.json'), `${JSON.stringify(reports, null, 2)}\n`);
    console.log(`Class 10 reader tab screenshots: ${JSON.stringify(reports)}`);
  } finally {
    await browser.close();
  }
});
