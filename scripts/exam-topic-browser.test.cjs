const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { chromium } = require('playwright');
const { ROOT } = require('./seo-html.cjs');
const { fixtureFiles, routeRepositoryFixtures } = require('./lib/browser-fixture.cjs');

test('English and Geography authored pages preserve five tabs, quiz, PYQ and timed test behavior', { timeout: 180000 }, async () => {
  const { externalizeExamTopicRuntime, hydrateExamTopicRuntime } = await import('./lib/exam-topic-runtime.mjs');
  const root = path.resolve(ROOT, process.env.SJ_REFACTOR_FIXTURE_ROOT || '.');
  const files = fixtureFiles(root);
  const pages = ['english/language/grammar/narration/index.html', 'geography/cartography/topographical-maps-and-contours/index.html'];
  const browser = await chromium.launch({ headless: true });
  try {
    for (const file of pages) for (const width of [390, 1280]) {
      const after = externalizeExamTopicRuntime(fs.readFileSync(path.join(root, file), 'utf8'));
      const before = hydrateExamTopicRuntime(after);
      assert.notEqual(before, after);
      const url = 'https://sjmaths.com/' + file.replace(/index\.html$/, '');
      const outcomes = [];
      for (const html of [before, after]) {
        const context = await browser.newContext({ viewport: { width, height: 900 }, reducedMotion: 'reduce', serviceWorkers: 'block' });
        try {
          const page = await context.newPage();
          const evidence = await routeRepositoryFixtures(page, { root, files });
          await page.route(url, route => route.fulfill({ contentType: 'text/html', body: html }));
          await page.addInitScript(() => localStorage.setItem('sjmaths-theme', 'green'));
          await page.clock.install({ time: new Date('2026-01-01T00:00:00Z') });
          await page.clock.pauseAt(new Date('2026-01-01T00:01:00Z'));
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
          await tabs.nth(2).click();
          const question = page.locator('#q-card-0');
          const correct = Number(await question.getAttribute('data-correct'));
          await question.locator('.quiz-option-btn').nth(correct).click();
          assert.equal(await question.locator('.quiz-option-btn').nth(correct).isDisabled(), true);
          assert.match(await page.locator('#feedback-0').innerText(), /Correct Answer/);
          await tabs.nth(3).click();
          await page.locator('#pyq-card-0 .quiz-option-btn').first().click();
          assert.equal(await page.locator('#pyq-expl-0').isVisible(), true);
          await tabs.nth(4).click();
          await page.clock.runFor(1000);
          assert.equal(await page.locator('#testTimerDisplay').innerText(), '09:59');
          const questions = page.locator('.test-question-card');
          assert.equal(await questions.count(), 10);
          for (let i = 0; i < await questions.count(); i++) {
            const card = questions.nth(i);
            await card.locator('.test-option-btn').nth(Number(await card.getAttribute('data-correct'))).click();
          }
          await page.locator('#btnSubmitTest').click();
          assert.equal(await page.locator('#resFinalScore').innerText(), '10');
          assert.equal(await page.locator('#testResultModal').isVisible(), true);
          const stopped = await page.locator('#testTimerDisplay').innerText();
          await page.clock.runFor(3000);
          assert.equal(await page.locator('#testTimerDisplay').innerText(), stopped);
          await page.locator('#btnRetakeTest').click();
          await page.waitForLoadState('load');
          assert.equal(await page.locator('#testResultModal').isVisible(), false);
          assert.equal(await page.locator('#testTimerDisplay').innerText(), '10:00');
          assert.deepEqual(evidence.errors, []);
          assert.deepEqual(evidence.missing, []);
          outcomes.push(states);
        } finally { await context.close(); }
      }
      assert.deepEqual(outcomes[1], outcomes[0], `${file} ${width}px inline/external parity`);
    }
  } finally { await browser.close(); }
});
