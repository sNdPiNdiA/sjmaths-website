const test = require('node:test');
const assert = require('node:assert/strict');
const crypto = require('node:crypto');
const fs = require('node:fs');
const path = require('node:path');
const { execFileSync } = require('node:child_process');
const { chromium } = require('playwright');
const { ROOT } = require('./seo-html.cjs');
const { fixtureFiles, routeRepositoryFixtures } = require('./lib/browser-fixture.cjs');

const baseline = '237db669da5fca0a8ff8ae6a5a601d284a367642';
const file = 'sanskrit/anuvad/hindi-vakyon-ka-sanskrit-anuvad/index.html';
const route = '/sanskrit/anuvad/hindi-vakyon-ka-sanskrit-anuvad/';
const fixtureRoot = path.resolve(ROOT, process.env.SJ_REFACTOR_FIXTURE_ROOT || '.');

test('Sanskrit shared runtime preserves screenshots and complete keyboard learning flows', { timeout: 120000 }, async () => {
  const originalHtml = execFileSync('git', ['show', `${baseline}:${file}`], { cwd: ROOT, encoding: 'utf8', maxBuffer: 20e6 });
  const externalHtml = fs.readFileSync(path.join(fixtureRoot, file), 'utf8');
  const migrated = externalHtml.includes('data-sanskrit-topic-runtime="shared"');
  const browser = await chromium.launch({ headless: true });
  const evidenceRoot = path.join(ROOT, 'scratch/refactor/sanskrit-topic-runtime', path.basename(fixtureRoot));
  fs.mkdirSync(evidenceRoot, { recursive: true });
  const screenshots = [];

  try {
    for (const width of [390, 1280]) for (const [kind, html] of [['inline', originalHtml], ['external', externalHtml]]) {
      const context = await browser.newContext({ viewport: { width, height: 900 }, reducedMotion: 'reduce', serviceWorkers: 'block' });
      try {
        const page = await context.newPage();
        const evidence = await routeRepositoryFixtures(page, { root: fixtureRoot, files: fixtureFiles(fixtureRoot) });
        await page.addInitScript(() => {
          localStorage.removeItem('sjmaths.theme.preference');
          localStorage.removeItem('sjmaths_theme');
          localStorage.removeItem('sj_theme');
          localStorage.setItem('sjmaths-theme', 'green');
        });
        await page.route(`https://sjmaths.com${route}`, request => request.fulfill({ contentType: 'text/html', body: html }));
        await page.goto(`https://sjmaths.com${route}`, { waitUntil: 'networkidle' });
        const skip = page.locator('#sj-skip-gate-btn');
        if (await page.locator('script[src*="require-auth"]').count()) {
          await skip.waitFor({ state: 'visible', timeout: 15000 });
          await skip.click();
          await page.locator('#sj-auth-overlay').waitFor({ state: 'hidden' });
        }
        await page.evaluate(() => document.fonts.ready);
        assert.deepEqual(evidence.errors, [], `${kind} page errors`);
        assert.deepEqual(evidence.missing, [], `${kind} missing local requests`);
        if (kind === 'external' && migrated) {
          const runtime = page.locator('script[data-sanskrit-topic-runtime="shared"]');
          assert.equal(await runtime.count(), 1);
          assert.match(await runtime.getAttribute('src'), /\/assets\/js\/sanskrit-topic(?:\.min)?\.js(?:\?[^" ]*)?$/);
        }
        const state = await page.evaluate(() => ({
          overflow: Math.max(0, document.documentElement.scrollWidth - innerWidth),
          h1: document.querySelector('h1')?.getBoundingClientRect().toJSON(),
          tabs: [...document.querySelectorAll('.tab-btn')].map(button => button.textContent.trim()),
          quizQuestions: document.querySelectorAll('#tab-quiz .quiz-question-card').length,
          pyqs: document.querySelectorAll('#tab-pyqs .pyq-card').length,
          testQuestions: document.querySelectorAll('#tab-test .test-question-card').length,
        }));
        assert.equal(state.overflow, 0, `${kind}/${width} horizontal overflow`);
        assert.ok(state.quizQuestions > 0);
        assert.ok(state.pyqs > 0);
        assert.ok(state.testQuestions > 0);
        const screenshotPath = path.join(evidenceRoot, `${width}-${kind}.png`);
        await page.screenshot({ path: screenshotPath, animations: 'disabled' });
        screenshots.push({ kind, width, screenshotPath, state });

        if (kind === 'external' && width === 1280) {
          const theme = page.locator('#btn-theme-toggle');
          await theme.focus();
          await page.keyboard.press('Enter');
          assert.equal(await page.locator('body').evaluate(element => element.classList.contains('dark-mode')), true);
          assert.equal(await page.locator('html').getAttribute('data-theme'), 'dark');
          assert.equal(await theme.getAttribute('aria-pressed'), 'true');
          assert.equal(await page.evaluate(() => localStorage.getItem('sjmaths-theme')), 'green');
          await theme.focus();
          await page.keyboard.press('Enter');
          assert.equal(await page.locator('body').evaluate(element => element.classList.contains('dark-mode')), false);
          assert.equal(await page.locator('html').getAttribute('data-theme'), 'light');
          assert.equal(await theme.getAttribute('aria-pressed'), 'false');

          const quizTab = page.locator('.tab-btn[data-tab="tab-quiz"]');
          await quizTab.focus();
          await page.keyboard.press('Enter');
          assert.equal(await page.locator('#tab-quiz').evaluate(element => element.classList.contains('active')), true);
          const quizCard = page.locator('#tab-quiz .quiz-question-card').first();
          const quizCorrect = await quizCard.getAttribute('data-correct');
          const quizAnswer = quizCard.locator(`.quiz-option-btn[data-optindex="${quizCorrect}"]`);
          await quizAnswer.focus();
          await page.keyboard.press('Enter');
          assert.equal(await quizAnswer.isDisabled(), true);
          assert.equal(await quizCard.locator('.q-feedback').isVisible(), true);
          assert.equal(await page.locator('#quizScore').textContent(), '1');
          await page.locator('#btnResetQuiz').focus();
          await page.keyboard.press('Enter');
          assert.equal(await page.locator('#quizScore').textContent(), '0');
          assert.equal(await quizAnswer.isDisabled(), false);

          const pyqTab = page.locator('.tab-btn[data-tab="tab-pyqs"]');
          await pyqTab.focus();
          await page.keyboard.press('Enter');
          const pyqAnswer = page.locator('#tab-pyqs .quiz-option-btn[data-pyqindex]').first();
          await pyqAnswer.focus();
          await page.keyboard.press('Enter');
          assert.equal(await pyqAnswer.isDisabled(), true);

          const testTab = page.locator('.tab-btn[data-tab="tab-test"]');
          await testTab.focus();
          await page.keyboard.press('Enter');
          const start = page.locator('#btnStartTest');
          await start.dblclick();
          assert.equal(await page.locator('#testActiveWrap').isVisible(), true);
          assert.equal(await page.locator('#testStartWrap').isVisible(), false);
          await page.waitForTimeout(1250);
          const [minutes, seconds] = (await page.locator('#timerDisplay').textContent()).split(':').map(Number);
          const secondsLeft = minutes * 60 + seconds;
          assert.ok(secondsLeft >= 599 && secondsLeft <= 600, `repeated start input left ${secondsLeft} seconds`);
          const testOption = page.locator('#tab-test .test-option-btn[data-tindex="0"]').first();
          await testOption.focus();
          await page.keyboard.press('Enter');
          assert.equal(await testOption.evaluate(element => element.classList.contains('selected')), true);
          const submit = page.locator('#btnSubmitTest');
          await submit.focus();
          await page.keyboard.press('Enter');
          assert.equal(await page.locator('#testResultModal').isVisible(), true);
          const reload = page.waitForLoadState('domcontentloaded');
          await page.locator('#btnRetakeTest').click();
          await reload;
          assert.equal(await page.locator('#timerDisplay').textContent(), '10:00');
        }
      } finally { await context.close(); }
    }

    for (const width of [390, 1280]) {
      const inline = screenshots.find(item => item.width === width && item.kind === 'inline');
      const external = screenshots.find(item => item.width === width && item.kind === 'external');
      assert.deepEqual(external.state, inline.state, `${width}px state parity`);
      const digest = filePath => crypto.createHash('sha256').update(fs.readFileSync(filePath)).digest('hex');
      assert.equal(digest(external.screenshotPath), digest(inline.screenshotPath), `${width}px initial screenshot`);
    }
    fs.writeFileSync(path.join(evidenceRoot, 'results.json'), JSON.stringify({ fixtureRoot: path.relative(ROOT, fixtureRoot) || '.', baseline, screenshots: screenshots.map(({ screenshotPath, ...item }) => item) }, null, 2) + '\n');
  } finally { await browser.close(); }
});
