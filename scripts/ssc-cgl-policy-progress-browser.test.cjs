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
  ['standard', 'ssc-cgl/general-awareness/general-policy-polity/citizenship-articles-5-11-and-caa/index.html', false],
  ['with-pyq-details', 'ssc-cgl/general-awareness/general-policy-polity/directive-principles-of-state-policy-dpsp-articles-36-51/index.html', true],
].filter(([, file]) => !process.env.SJ_REFACTOR_PAGE || file.includes(process.env.SJ_REFACTOR_PAGE));
const fixtureRoot = path.resolve(ROOT, process.env.SJ_REFACTOR_FIXTURE_ROOT || '.');
const widths = process.env.SJ_REFACTOR_WIDTH ? [Number(process.env.SJ_REFACTOR_WIDTH)] : [390, 1280];

async function screenshotPixels(page, first, second) {
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

test('SSC-CGL polity progress asset preserves screenshots, level navigation, keyboard use and PYQ behavior', { timeout: 240000 }, async () => {
  const browser = await chromium.launch({ headless: true });
  const evidenceRoot = path.join(ROOT, 'scratch/refactor/ssc-cgl-policy-progress', path.basename(fixtureRoot));
  fs.mkdirSync(evidenceRoot, { recursive: true });
  const results = [];

  try {
    for (const [id, file, hasPyqDetails] of pages) for (const width of widths) {
      const directory = file.slice(0, file.lastIndexOf('/'));
      const url = `https://sjmaths.com/${directory}/#tab-practice`;
      const originalHtml = execFileSync('git', ['show', `${baseline}:${file}`], { cwd: ROOT, encoding: 'utf8', maxBuffer: 20e6 });
      const sharedHtml = fs.readFileSync(path.join(fixtureRoot, file), 'utf8');
      assert.match(sharedHtml, /data-ssc-cgl-policy-progress="shared"/);
      assert.match(sharedHtml, /data-ssc-cgl-policy-mini-test="shared"/);
      const outcomes = [];

      for (const [mode, html] of [['inline', originalHtml], ['shared', sharedHtml]]) {
        const context = await browser.newContext({ viewport: { width, height: 900 }, reducedMotion: 'reduce', serviceWorkers: 'block' });
        try {
          const page = await context.newPage();
          const evidence = await routeRepositoryFixtures(page, { root: fixtureRoot, files: fixtureFiles(fixtureRoot) });
          await page.route('**/assets/js/require-auth.min.js*', route => route.fulfill({ contentType: 'text/javascript', body: '' }));
          await page.route(`https://sjmaths.com/${directory}/`, route => route.fulfill({ contentType: 'text/html', body: html }));
          await page.goto(url, { waitUntil: 'networkidle' });
          await page.evaluate(() => document.fonts.ready);
          await page.waitForTimeout(150);
          if (mode === 'shared') {
            const runtime = page.locator('script[data-ssc-cgl-policy-progress="shared"]');
            assert.equal(await runtime.count(), 1);
            assert.match(await runtime.getAttribute('src'), /^\/assets\/js\/ssc-cgl-policy-progress(?:\.min)?\.js(?:\?v=[a-f0-9]+)?$/);
            const miniTestRuntime = page.locator('script[data-ssc-cgl-policy-mini-test="shared"]');
            assert.equal(await miniTestRuntime.count(), 1);
            assert.match(await miniTestRuntime.getAttribute('src'), /^\/assets\/js\/ssc-cgl-policy-mini-test(?:\.min)?\.js(?:\?v=[a-f0-9]+)?$/);
          }

          const initial = await page.evaluate(() => ({
            dots: document.querySelectorAll('#progressTrack .progress-dot').length,
            practiceQuestions: document.querySelectorAll('#tab-practice .practice-card[data-level]').length,
            visibleLevelQuestions: [...document.querySelectorAll('#tab-practice .practice-card[data-level]')].filter(card => getComputedStyle(card).display !== 'none').length,
            pyqSolutionDetails: document.querySelectorAll('#tab-practice .pyq-card details.solution-details').length,
            visiblePyqSolutionDetails: [...document.querySelectorAll('#tab-practice .pyq-card details.solution-details')].filter(details => details.getClientRects().length > 0).length,
            activeLevel: document.querySelector('#levelNav .level-btn.active')?.dataset.level,
            practiceTabActive: document.getElementById('tab-practice')?.classList.contains('active'),
            overflow: Math.max(0, document.documentElement.scrollWidth - innerWidth),
          }));
      assert.deepEqual(initial, {
        dots: 49,
        practiceQuestions: 49,
        visibleLevelQuestions: 7,
        pyqSolutionDetails: hasPyqDetails ? 16 : 0,
        visiblePyqSolutionDetails: 0,
        activeLevel: '1',
        practiceTabActive: true,
        overflow: 0,
      });
          await page.evaluate(() => { document.activeElement?.blur(); window.scrollTo(0, 0); });
          await page.waitForTimeout(120);
          const screenshotPath = path.join(evidenceRoot, `${id}-${width}-${mode}.png`);
          await page.screenshot({ path: screenshotPath, animations: 'disabled' });

          await page.locator('#levelNav .level-btn[data-level="2"]').focus();
          await page.keyboard.press('Enter');
          assert.equal(await page.locator('#levelNav .level-btn[data-level="2"]').evaluate(button => button.classList.contains('active')), true);
          assert.equal(await page.locator('#tab-practice .practice-card.level-active').count(), 7);
          const answerSummary = page.locator('#tab-practice .practice-card[data-level="2"] details.solution-details summary').first();
          await answerSummary.focus();
          await page.keyboard.press('Enter');
          await page.locator('#dot-8.completed').waitFor({ state: 'attached' });
          assert.equal((await page.locator('#attemptedCount').innerText()).trim(), '1/49');
          assert.equal((await page.locator('#correctCount').innerText()).trim(), '1/49');
          assert.equal((await page.locator('#scoreDisplay').innerText()).trim(), '2%');

          const miniTestTab = page.locator('.main-tabs-nav .tab-btn[onclick*="tab-mini-test"]');
          await miniTestTab.focus();
          await page.keyboard.press('Enter');
          assert.equal(await page.locator('#tab-mini-test').evaluate(panel => panel.classList.contains('active')),
            true, 'keyboard activates the mini-test tab');
          await page.locator('#tab-mini-test').evaluate(async panel => {
            await Promise.all(panel.getAnimations().map(animation => animation.finished.catch(() => {})));
          });
          const questions = page.locator('#tab-mini-test .mini-test-question');
          assert.equal(await questions.count(), 10);
          const firstAnswer = questions.first().locator('input[type="radio"]').first();
          const miniTestVisible = await firstAnswer.isVisible();
          let submitted = null, resetState = null;
          if (miniTestVisible) {
            for (let index = 0; index < await questions.count(); index++) {
              const question = questions.nth(index);
              const answer = await question.getAttribute('data-mini-answer');
              const correctOption = question.locator(`input[type="radio"][value="${answer}"]`);
              assert.equal(await correctOption.count(), 1, `question ${index + 1} has its keyed option`);
              await correctOption.focus();
              await page.keyboard.press('Space');
              assert.equal(await correctOption.isChecked(), true, `question ${index + 1} accepts a keyboard answer`);
            }
            const submit = page.locator('#tab-mini-test .mini-test-submit');
            await submit.focus();
            await page.keyboard.press('Enter');
            submitted = await page.locator('#tab-mini-test').evaluate(test => ({
              score: test.querySelector('.mini-test-score')?.textContent.trim(),
              accuracy: test.querySelector('.mini-test-accuracy')?.textContent.trim(),
              resultsDisplay: getComputedStyle(test.querySelector('.mini-test-results')).display,
              correctCards: test.querySelectorAll('.mini-test-question.mini-correct').length,
              wrongCards: test.querySelectorAll('.mini-test-question.mini-wrong').length,
              openSolutions: test.querySelectorAll('.mini-test-solution[open]').length,
            }));
            assert.deepEqual(submitted, { score: '10/10', accuracy: '100%', resultsDisplay: 'block', correctCards: 10, wrongCards: 0, openSolutions: 10 });
            const reset = page.locator('#tab-mini-test .mini-test-reset');
            await reset.focus();
            await page.keyboard.press('Enter');
            resetState = await page.locator('#tab-mini-test').evaluate(test => ({
              selected: test.querySelectorAll('input[type="radio"]:checked').length,
              resultsDisplay: getComputedStyle(test.querySelector('.mini-test-results')).display,
              correctCards: test.querySelectorAll('.mini-test-question.mini-correct').length,
              wrongCards: test.querySelectorAll('.mini-test-question.mini-wrong').length,
              openSolutions: test.querySelectorAll('.mini-test-solution[open]').length,
              score: test.querySelector('.mini-test-score')?.textContent.trim(),
              accuracy: test.querySelector('.mini-test-accuracy')?.textContent.trim(),
            }));
            assert.equal(resetState.selected, 0);
            assert.equal(resetState.resultsDisplay, 'none');
            assert.equal(resetState.correctCards + resetState.wrongCards, 0);
            assert.equal(resetState.openSolutions, 0);
          } else {
            assert.equal(hasPyqDetails, true, `mini-test is visible on ${id}/${width}`);
          }
          const errors = evidence.errors.filter(error => !error.startsWith('Service Worker registration failed'));
          outcomes.push({ mode, screenshotPath, initial, miniTestVisible, submitted, resetState, errors, missing: evidence.missing });
        } finally { await context.close(); }
      }

      assert.deepEqual(outcomes[1].initial, outcomes[0].initial, `${id}/${width} initial state parity`);
      assert.deepEqual(outcomes[1].errors, outcomes[0].errors, `${id}/${width} runtime error parity`);
      assert.deepEqual(outcomes[1].missing, outcomes[0].missing, `${id}/${width} missing asset parity`);
      assert.equal(outcomes[1].miniTestVisible, outcomes[0].miniTestVisible, `${id}/${width} mini-test visibility parity`);
      assert.deepEqual(outcomes[1].submitted, outcomes[0].submitted, `${id}/${width} mini-test submit parity`);
      assert.deepEqual(outcomes[1].resetState, outcomes[0].resetState, `${id}/${width} mini-test reset parity`);
      const pixelPage = await browser.newPage();
      const pixels = await screenshotPixels(pixelPage, outcomes[0].screenshotPath, outcomes[1].screenshotPath);
      await pixelPage.close();
      assert.equal(pixels.pixelsChanged, 0, `${id}/${width} visual pixel parity: ${JSON.stringify(pixels)}`);
      results.push({ id, width, initial: outcomes[1].initial, submitted: outcomes[1].submitted, resetState: outcomes[1].resetState, pixels });
    }
    fs.writeFileSync(path.join(evidenceRoot, 'results.json'), JSON.stringify({ baseline, fixtureRoot: path.relative(ROOT, fixtureRoot) || '.', results }, null, 2) + '\n');
  } finally { await browser.close(); }
});

