const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { chromium } = require('playwright');
const { ROOT } = require('./seo-html.cjs');
const { fixtureFiles, routeRepositoryFixtures } = require('./lib/browser-fixture.cjs');

test('Agriculture authored and regenerated variants preserve five tabs, quiz, theme and test lifecycle', { timeout: 180000 }, async () => {
  const runtime = await import('./lib/agriculture-runtime.mjs');
  const { renderTopicHtml } = await import('./lib/agriculture-renderer.mjs');
  const { transformHtml } = await import('./lib/agriculture-redesign.mjs');
  const fixture = await import('./fixtures/agriculture.mjs');
  const root = path.resolve(ROOT, process.env.SJ_REFACTOR_FIXTURE_ROOT || '.');
  const files = fixtureFiles(root);
  const generated = renderTopicHtml(fixture.item, fixture.context, fixture.data);
  const cases = [
    ...['agriculture/natural-farming/concept/index.html', 'agriculture/water-management/irrigation-frequency/index.html'].map(file => ({ file, html: runtime.externalizeAgricultureRuntime(fs.readFileSync(path.join(root, file), 'utf8')), widths: [390, 1280], expiry: false })),
    { file: fixture.item.url.slice(1) + 'index.html', html: generated, widths: [390], expiry: true },
    { file: fixture.item.url.slice(1) + 'index.html', html: transformHtml(generated), widths: [390], expiry: true },
  ];
  const browser = await chromium.launch({ headless: true });
  try {
    for (const item of cases) for (const width of item.widths) {
      const url = 'https://sjmaths.com/' + item.file.replace(/index\.html$/, '');
      const before = runtime.hydrateAgricultureRuntime(item.html);
      assert.notEqual(before, item.html, 'exercise actual inline versus shared runtime');
      const outcomes = [];
      for (const html of [before, item.html]) {
        const context = await browser.newContext({ viewport: { width, height: 900 }, reducedMotion: 'reduce', serviceWorkers: 'block' });
        try {
          const page = await context.newPage();
          const evidence = await routeRepositoryFixtures(page, { root, files });
          await page.route(url, route => route.fulfill({ contentType: 'text/html', body: html }));
          await page.addInitScript(() => localStorage.setItem('sjmaths-theme', 'green'));
          await page.clock.install();
          await page.goto(url);
          const tabs = page.locator('.tab-btn');
          assert.equal(await tabs.count(), 5);
          const states = [];
          for (let i = 0; i < 5; i++) {
            await tabs.nth(i).focus(); await page.keyboard.press('Enter');
            assert.equal(await tabs.nth(i).getAttribute('aria-selected'), 'true');
            assert.equal(await page.locator('.tab-panel.active').count(), 1);
            states.push(await page.locator('.tab-panel.active').innerText());
          }
          await page.locator('#btn-theme-toggle').click();
          assert.equal(await page.locator('html').evaluate(el => el.classList.contains('dark')), true);
          assert.equal(await page.locator('html').getAttribute('data-theme'), 'dark');
          assert.equal(await page.locator('#btn-theme-toggle').getAttribute('aria-pressed'), 'true');
          assert.equal(await page.evaluate(() => localStorage.getItem('sjmaths.theme.preference')), 'dark');
          assert.equal(await page.evaluate(() => localStorage.getItem('sjmaths-theme')), 'green');
          await page.locator('#btn-theme-toggle').click();
          assert.equal(await page.locator('html').getAttribute('data-theme'), 'light');
          assert.equal(await page.evaluate(() => localStorage.getItem('sjmaths-theme')), 'green');
          await page.locator('[data-tab="tab-quiz"]').click();
          const card = page.locator('#q-card-0');
          const options = card.locator('.quiz-option-btn, .quiz-opt');
          const correct = Number(await card.getAttribute('data-correct'));
          await options.nth(correct).click();
          assert.equal(await options.first().isDisabled(), true);
          const quizScore = await page.locator('#quizScore, #quizScoreText').innerText();
          assert.match(quizScore, /(?:^1$|Score: 1 \/)/);
          const feedback = await page.locator('#feedback-0, #q-feedback-0').innerText();
          assert.match(feedback, /Correct Answer/);
          await page.locator('#btnResetQuiz').click();
          assert.equal(await options.first().isDisabled(), false);
          assert.match(await page.locator('#quizScore, #quizScoreText').innerText(), /(?:^0$|Score: 0 \/)/);
          await page.locator('[data-tab="tab-test"]').click();
          await page.locator('#btnStartTest').click();
          const timer = page.locator('#timerDisplay, #testTimerDisplay');
          await page.clock.runFor(1000);
          assert.equal(await timer.innerText(), '09:59');
          const testCards = page.locator('.test-question-card');
          assert.equal(await testCards.count(), 10);
          if (item.expiry) await page.clock.runFor(599000);
          else {
            for (let i = 0; i < await testCards.count(); i++) {
              const question = testCards.nth(i);
              await question.locator('.test-option-btn').nth(Number(await question.getAttribute('data-correct'))).click();
            }
            await page.locator('#btnSubmitTest').click();
          }
          assert.equal(await page.locator('#testResultModal').isVisible(), true);
          assert.equal(await page.locator('#resFinalScore').innerText(), item.expiry ? '0' : '10');
          if (item.expiry) assert.equal(await timer.innerText(), '00:00');
          const stopped = await timer.innerText();
          await page.clock.runFor(3000);
          assert.equal(await timer.innerText(), stopped);
          await page.locator('#btnRetakeTest').click();
          await page.waitForLoadState('load');
          assert.equal(await page.locator('#testResultModal').isVisible(), false);
          assert.equal(await timer.innerText(), '10:00');
          assert.deepEqual(evidence.errors, []);
          assert.deepEqual(evidence.missing, []);
          outcomes.push({ states, quizScore, feedback });
        } finally { await context.close(); }
      }
      assert.deepEqual(outcomes[1], outcomes[0], `${item.file} ${width}px parity`);
    }
  } finally { await browser.close(); }
});
