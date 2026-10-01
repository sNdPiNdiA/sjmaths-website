const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { chromium } = require('playwright');
const { ROOT } = require('./seo-html.cjs');
const { fixtureFiles, routeRepositoryFixtures } = require('./lib/browser-fixture.cjs');

test('Hindi shared runtime preserves five-tab, quiz, PYQ, theme and timed-test flows', { timeout: 150000 }, async () => {
  const cases = [
    'hindi/bhashavigyan/bhashayen/index.html',
    'hindi/vyakaran/sandhi/index.html',
  ];
  const fixtureRoot = path.resolve(ROOT, process.env.SJ_REFACTOR_FIXTURE_ROOT || '.');
  const files = fixtureFiles(fixtureRoot);
  const { hydrateHindiTopicRuntime } = await import('./lib/hindi-topic-runtime.mjs');
  const browser = await chromium.launch({ headless: true });
  try {
    for (const file of cases) for (const width of [390, 1280]) {
      const url = `https://sjmaths.com/${file.replace(/index\.html$/, '')}`;
      const pageAfter = fs.readFileSync(path.join(fixtureRoot, file), 'utf8');
      const pageBefore = hydrateHindiTopicRuntime(pageAfter);
      assert.notEqual(pageBefore, pageAfter, `${file} must exercise shared-runtime hydration`);
      const outcomes = [];
      for (const html of [pageBefore, pageAfter]) {
        const context = await browser.newContext({ viewport: { width, height: 900 }, reducedMotion: 'reduce', serviceWorkers: 'block' });
        try {
          const page = await context.newPage();
          const evidence = await routeRepositoryFixtures(page, { root: fixtureRoot, files });
          await page.route(url, route => route.fulfill({ contentType: 'text/html', body: html }));
          await page.clock.install();
          await page.goto(url);
          const tabs = page.locator('.tab-btn');
          assert.equal(await tabs.count(), 5, `${file} tab count`);
          const panels = [];
          for (let index = 0; index < 5; index++) {
            await tabs.nth(index).focus();
            await page.keyboard.press('Enter');
            assert.equal(await tabs.nth(index).getAttribute('aria-selected'), 'true');
            const target = await tabs.nth(index).getAttribute('data-tab');
            panels.push((await page.locator(`#${target}`).innerText()).slice(0, 300));
          }

          await page.locator('#btn-theme-toggle').click();
          const darkMode = await page.locator('body').evaluate(body => body.classList.contains('dark-mode'));

          await tabs.nth(2).click();
          const quiz = page.locator('#q-card-0');
          await quiz.locator('.quiz-option-btn').first().click();
          const quizFeedback = await page.locator('#feedback-0').innerText();
          assert.equal(await quiz.locator('.quiz-option-btn').first().isDisabled(), true);
          await page.locator('#btnResetQuiz').click();
          assert.equal(await quiz.locator('.quiz-option-btn').first().isDisabled(), false);
          assert.equal(await page.locator('#quizScore').innerText(), '0');

          await tabs.nth(3).click();
          await page.locator('#pyq-card-0 .quiz-option-btn').first().click();
          const pyqFeedbackVisible = await page.locator('#pyq-expl-0').isVisible();
          assert.equal(await page.locator('#pyq-card-0 .quiz-option-btn').first().isDisabled(), true);

          await tabs.nth(4).click();
          await page.locator('#btnStartTest').click();
          await page.clock.runFor(2000);
          const runningTimer = await page.locator('#timerDisplay').innerText();
          assert.notEqual(runningTimer, '10:00');
          await page.locator('.test-option-btn').first().click();
          await page.locator('#btnSubmitTest').click();
          const score = await page.locator('#resFinalScore').innerText();
          assert.equal(await page.locator('#testResultModal').isVisible(), true);
          const stoppedTimer = await page.locator('#timerDisplay').innerText();
          await page.clock.runFor(3000);
          assert.equal(await page.locator('#timerDisplay').innerText(), stoppedTimer);
          await page.locator('#btnRetakeTest').click();
          await page.waitForLoadState('domcontentloaded');
          assert.equal(await page.locator('#timerDisplay').innerText(), '10:00');
          assert.equal(await page.locator('#testResultModal').isVisible(), false);

          const overflow = await page.evaluate(() => Math.max(0, document.documentElement.scrollWidth - innerWidth));
          assert.equal(overflow, 0, `${file} ${width}px horizontal overflow`);
          assert.deepEqual(evidence.missing, []);
          outcomes.push({ panels, darkMode, quizFeedback, pyqFeedbackVisible, runningTimer, score, errors: evidence.errors });
        } finally { await context.close(); }
      }
      assert.deepEqual(outcomes[1], outcomes[0], `${file} ${width}px inline/external browser parity`);
    }
  } finally { await browser.close(); }
});
