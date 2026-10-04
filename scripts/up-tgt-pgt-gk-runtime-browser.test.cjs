const test = require('node:test');
const assert = require('node:assert/strict');
const crypto = require('node:crypto');
const fs = require('node:fs');
const path = require('node:path');
const { execFileSync } = require('node:child_process');
const { chromium } = require('playwright');
const { ROOT } = require('./seo-html.cjs');
const { fixtureFiles, routeRepositoryFixtures } = require('./lib/browser-fixture.cjs');

const baseline = '6be921178f2787101ae755971253e564df0c85f2';

test('GK external topic runtime preserves bilingual quiz, test, theme and keyboard flows', { timeout: 180000 }, async () => {
  const file = 'up-tgt-pgt-gk/art-culture/classical-dances/index.html';
  const route = '/up-tgt-pgt-gk/art-culture/classical-dances/';
  const originalHtml = execFileSync('git', ['show', `${baseline}:${file}`], { cwd: ROOT, encoding: 'utf8', maxBuffer: 20e6 });
  const fixtureRoot = path.resolve(ROOT, process.env.SJ_REFACTOR_FIXTURE_ROOT || '.');
  const externalHtml = fs.readFileSync(path.join(fixtureRoot, file), 'utf8');
  assert.match(externalHtml, /data-up-tgt-pgt-gk-runtime="topic"/);
  assert.match(originalHtml, /id="bilingual-data"/);
  const files = fixtureFiles(fixtureRoot);
  const browser = await chromium.launch({ headless: true });
  const evidenceRoot = path.join(ROOT, 'scratch/refactor/up-tgt-pgt-gk-runtime');
  fs.mkdirSync(evidenceRoot, { recursive: true });
  try {
    for (const width of [390, 1280]) {
      const results = [];
      for (const [kind, html] of [['inline', originalHtml], ['external', externalHtml]]) {
        const context = await browser.newContext({ viewport: { width, height: 900 }, reducedMotion: 'reduce' });
        try {
          const page = await context.newPage();
          const evidence = await routeRepositoryFixtures(page, { root: fixtureRoot, files });
          await page.addInitScript(() => {
            if (!sessionStorage.getItem('sj-gk-initial-state-set')) {
              localStorage.setItem('sjmaths_language', 'hi');
              localStorage.setItem('sjmaths_theme', 'light');
              localStorage.setItem('sj_theme', 'light');
            localStorage.setItem('sjmaths-theme', 'green');
              sessionStorage.setItem('sj-gk-initial-state-set', 'true');
            }
          });
          await page.route(`https://sjmaths.com${route}`, request => request.fulfill({ contentType: 'text/html', body: html }));
          await page.goto(`https://sjmaths.com${route}`, { waitUntil: 'networkidle' });
          await page.addStyleTag({ content: 'html { scroll-behavior: auto !important; }' });
          await page.evaluate(() => document.fonts.ready);
          assert.deepEqual(evidence.errors, [], `${kind} runtime errors`);
          assert.deepEqual(evidence.missing, [], `${kind} missing local requests`);
          if (kind === 'external') {
            const runtime = page.locator('script[data-up-tgt-pgt-gk-runtime="topic"]');
            assert.equal(await runtime.count(), 1);
            assert.equal(await runtime.evaluate(element => /\/assets\/js\/up-tgt-pgt-gk-topic(?:\.min)?\.js(?:\?|$)/.test(element.src)), true);
            const languageRuntime = page.locator('script[data-up-tgt-pgt-gk-runtime="language"]');
            assert.equal(await languageRuntime.count(), 1);
            assert.equal(await languageRuntime.evaluate(element => /\/assets\/js\/up-tgt-pgt-gk-language(?:\.min)?\.js(?:\?|$)/.test(element.src)), true);
          }
          assert.equal(await page.locator('html').getAttribute('lang'), 'hi');
          const screenshotPath = path.join(evidenceRoot, `${width}-${kind}-hindi.png`);
          await page.screenshot({ path: screenshotPath, fullPage: false, animations: 'disabled' });
          const overflow = await page.evaluate(() => Math.max(0, document.documentElement.scrollWidth - innerWidth));

          await Promise.all([
            page.waitForNavigation({ waitUntil: 'networkidle' }),
            page.locator('#btn-language-toggle').focus().then(() => page.keyboard.press('Enter')),
          ]);
          assert.equal(await page.locator('html').getAttribute('lang'), 'en');
          const languageControl = {
            text: (await page.locator('#btn-language-toggle').textContent()).trim(),
            ariaLabel: await page.locator('#btn-language-toggle').getAttribute('aria-label'),
          };

          await page.locator('#tab-btn-quiz').focus();
          await page.keyboard.press('Enter');
          const correctQuiz = await page.evaluate(() => JSON.parse(document.getElementById('quiz-data').textContent)[0].correct_index);
          await page.locator(`#quiz-card-0 [data-quiz="0"][data-option="${correctQuiz}"]`).click();
          assert.equal(await page.locator('#quiz-feedback-0 .correct').count(), 1);

          await page.locator('#tab-btn-test').focus();
          await page.keyboard.press('Enter');
          const correctTest = await page.evaluate(() => JSON.parse(document.getElementById('test-data').textContent)[0].correct_index);
          await page.locator(`#test-card-0 [data-test="0"][data-option="${correctTest}"]`).click();
          await page.locator('#btn-submit-test').click();
          const score = await page.locator('#test-score').textContent();
          assert.ok(Number(score) >= 1, `${kind} test score should include the correct first answer`);

          await page.locator('#btn-theme-toggle').focus();
          await page.keyboard.press('Enter');
          assert.equal(await page.locator('body').evaluate(element => element.classList.contains('dark-mode')), true);
          if (kind === 'external') {
            assert.equal(await page.locator('html').getAttribute('data-theme'), 'dark');
            assert.equal(await page.locator('#btn-theme-toggle').getAttribute('aria-pressed'), 'true');
            assert.equal(await page.evaluate(() => localStorage.getItem('sjmaths-theme')), 'green');
          }
          results.push({ kind, screenshotPath, overflow, score: Number(score), languageControl, errors: evidence.errors, missing: evidence.missing });
        } finally { await context.close(); }
      }
      assert.equal(results[1].overflow, results[0].overflow, `${width}px overflow parity`);
      assert.equal(results[1].score, results[0].score, `${width}px test score parity`);
      assert.deepEqual(results[1].languageControl, results[0].languageControl, `${width}px language-toggle state parity`);
      assert.deepEqual(results[1].errors, results[0].errors);
      assert.deepEqual(results[1].missing, results[0].missing);
      const digest = filePath => crypto.createHash('sha256').update(fs.readFileSync(filePath)).digest('hex');
      assert.equal(digest(results[1].screenshotPath), digest(results[0].screenshotPath), `${width}px initial Hindi pixels`);
    }
  } finally { await browser.close(); }
});

test('shared GK runtime keeps English generator output working without bilingual data', { timeout: 30000 }, async () => {
  const pageHtml = `<!doctype html><html lang="en"><head><title>GK Runtime Fixture</title></head><body>
    <script type="application/json" id="quiz-data">[{"correct_index":0,"explanation":"Correct English explanation."}]</script>
    <script type="application/json" id="test-data">[{"correct_index":0,"explanation":"Correct English test explanation."}]</script>
    <div class="study-tabs-sticky-wrapper">
      <button type="button" class="tab-btn" data-tab="tab-quiz" id="tab-btn-quiz">Quiz</button>
      <button type="button" class="tab-btn" data-tab="tab-test" id="tab-btn-test">Test</button>
    </div>
    <div id="tab-quiz" class="tab-panel"><div id="quiz-card-0"><button type="button" data-quiz="0" data-option="0">Correct option</button><div id="quiz-feedback-0"></div></div><p id="quiz-score"></p><button id="btn-reset-quiz">Reset</button></div>
    <div id="tab-test" class="tab-panel hidden"><p id="test-timer"></p><div id="test-card-0"><button type="button" data-test="0" data-option="0">Correct test option</button><div id="test-feedback-0"></div></div><p id="test-score"></p><div id="test-result" class="hidden"></div><button id="btn-submit-test">Submit</button><button id="btn-retake-test">Retake</button></div>
    <button id="btn-theme-toggle">Dark Mode</button>
    <script src="/assets/js/up-tgt-pgt-gk-topic.js" data-up-tgt-pgt-gk-runtime="topic"></script>
  </body></html>`;
  const runtimeSource = fs.readFileSync(path.join(ROOT, 'assets/js/up-tgt-pgt-gk-topic.js'), 'utf8');
  const browser = await chromium.launch({ headless: true });
  try {
    const page = await browser.newPage();
    const errors = [];
    page.on('pageerror', error => errors.push(error.message));
    page.on('console', message => { if (message.type() === 'error') errors.push(message.text()); });
    await page.addInitScript(() => localStorage.setItem('sjmaths_language', 'hi'));
    await page.route('https://sjmaths.com/gk-runtime-fixture.html', route => route.fulfill({ contentType: 'text/html', body: pageHtml }));
    await page.route('https://sjmaths.com/assets/js/up-tgt-pgt-gk-topic.js', route => route.fulfill({ contentType: 'text/javascript', body: runtimeSource }));
    await page.goto('https://sjmaths.com/gk-runtime-fixture.html', { waitUntil: 'networkidle' });
    assert.equal(await page.locator('html').getAttribute('lang'), 'en');
    assert.equal(await page.locator('#btn-language-toggle').count(), 0);
    await page.locator('#quiz-card-0 [data-quiz]').click();
    assert.equal(await page.locator('#quiz-feedback-0 .correct').count(), 1);
    assert.match(await page.locator('#quiz-feedback-0').innerText(), /Correct/);
    await page.locator('#tab-btn-test').click();
    await page.locator('#test-card-0 [data-test]').click();
    await page.locator('#btn-submit-test').click();
    assert.equal(await page.locator('#test-score').textContent(), '1');
    await page.locator('#btn-theme-toggle').click();
    assert.equal(await page.locator('body').evaluate(element => element.classList.contains('dark-mode')), true);
    assert.deepEqual(errors, []);
  } finally { await browser.close(); }
});
