const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { chromium } = require('playwright');
const { ROOT } = require('./seo-html.cjs');
const { fixtureFiles, routeRepositoryFixtures } = require('./lib/browser-fixture.cjs');

test('Chemistry unified runtime preserves English/Hindi tabs, quiz/PYQ, theme and timed-test lifecycle', { timeout: 120000 }, async () => {
  const { externalizeChemistryRuntime, hydrateChemistryRuntime } = await import('./lib/chemistry-runtime.mjs');
  const root = path.resolve(ROOT, process.env.SJ_REFACTOR_FIXTURE_ROOT || '.');
  const files = fixtureFiles(root);
  const browser = await chromium.launch({ headless: true });
  try {
    for (const [file, bilingual] of [
      ['chemistry/chemistry-in-everyday-life/chemicals-in-food/artificial-sweeteners/index.html', true],
      ['chemistry/chemistry-in-everyday-life/index.html', false],
    ]) {
      const url = 'https://sjmaths.com/' + file.replace(/index\.html$/, '');
      const after = externalizeChemistryRuntime(fs.readFileSync(path.join(root, file), 'utf8'));
      const before = hydrateChemistryRuntime(after);
      assert.notEqual(before, after);
      for (const width of [390, 1280]) {
        const outcomes = [];
        for (const html of [before, after]) {
          const context = await browser.newContext({ viewport: { width, height: 900 }, reducedMotion: 'reduce', serviceWorkers: 'block' });
          try {
            const page = await context.newPage();
            await page.addInitScript(() => {
              localStorage.removeItem('sjmaths.theme.preference');
              localStorage.setItem('sjmaths-theme', 'green');
            });
            const evidence = await routeRepositoryFixtures(page, { root, files });
            await page.route(url, route => route.fulfill({ contentType: 'text/html', body: html }));
            await page.goto(url);
            await page.clock.install();
            const tabs = page.locator('.tab-btn');
            assert.equal(await tabs.count(), 5);
            const states = [];
            for (let i = 0; i < 5; i++) {
              await tabs.nth(i).focus(); await page.keyboard.press('Enter');
              assert.equal(await tabs.nth(i).getAttribute('aria-selected'), 'true');
              states.push(await page.locator('.tab-panel.active').innerText());
            }
            let hindi;
            if (bilingual) {
              assert.equal(await page.locator('html').getAttribute('data-lang'), 'en');
              await page.locator('#btn-lang-toggle').click();
              assert.equal(await page.locator('html').getAttribute('data-lang'), 'hi');
              await tabs.nth(0).click(); hindi = await page.locator('#tab-notes').innerText();
              await page.locator('#btn-lang-toggle').click();
              assert.equal(await page.locator('html').getAttribute('data-lang'), 'en');
            }
            await page.locator('#btn-theme-toggle').click();
            assert.equal(await page.locator('html').evaluate(html => html.classList.contains('dark')), true);
            if (html === after) {
              assert.equal(await page.locator('html').getAttribute('data-theme'), 'dark');
              assert.equal(await page.locator('#btn-theme-toggle').getAttribute('aria-pressed'), 'true');
              assert.equal(await page.evaluate(() => localStorage.getItem('sjmaths-theme')), 'green');
            }
            await page.locator('#btn-theme-toggle').click();
            await tabs.nth(2).click();
            const correct = Number(await page.locator('#q-card-0').getAttribute('data-correct'));
            await page.locator('#q-card-0 .quiz-option-btn').nth(correct).click();
            assert.equal(await page.locator('#quizScore').innerText(), '1');
            assert.equal(await page.locator('#feedback-0').isVisible(), true);
            await page.locator('#btnResetQuiz').click();
            assert.equal(await page.locator('#quizScore').innerText(), '0');
            assert.equal(await page.locator('#q-card-0 .quiz-option-btn').first().isDisabled(), false);
            await tabs.nth(3).click();
            await page.locator('#pyq-card-0 .quiz-option-btn').first().click();
            assert.equal(await page.locator('#pyq-expl-0').isVisible(), true);
            await tabs.nth(4).click();
            await page.locator('#btnStartTest').click();
            await page.clock.runFor(1000);
            assert.equal(await page.locator('#timerDisplay').innerText(), '09:59');
            const questions = page.locator('.test-question-card');
            const count = await questions.count();
            for (let i = 0; i < count; i++) {
              const question = questions.nth(i);
              const index = Number(await question.getAttribute('data-correct'));
              await question.locator('.test-option-btn').nth(index).click();
            }
            await page.locator('#btnSubmitTest').click();
            assert.equal(await page.locator('#resFinalScore').innerText(), String(count));
            const timer = await page.locator('#timerDisplay').innerText();
            await page.clock.runFor(3000);
            assert.equal(await page.locator('#timerDisplay').innerText(), timer);
            await page.locator('#btnRetakeTest').click();
            assert.equal(await page.locator('#timerDisplay').innerText(), '10:00');
            assert.equal(await page.locator('#btnStartTest').isVisible(), false); // Test panel resets hidden.
            assert.deepEqual(evidence.missing, []);
            assert.deepEqual(evidence.errors, []);
            outcomes.push({ states, hindi, count });
          } finally { await context.close(); }
        }
        assert.deepEqual(outcomes[1], outcomes[0], `${file} at ${width}px`);
      }
    }
  } finally { await browser.close(); }
});
