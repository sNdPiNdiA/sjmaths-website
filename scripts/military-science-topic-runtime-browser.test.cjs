const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { chromium } = require('playwright');
const { ROOT } = require('./seo-html.cjs');
const { fixtureFiles, routeRepositoryFixtures } = require('./lib/browser-fixture.cjs');

test('Military Science shared runtime preserves all seven quiz types and timed test', { timeout: 180000 }, async () => {
  const file = 'military-science/contemporary-security/cyber-security/challenges/index.html';
  const route = '/military-science/contemporary-security/cyber-security/challenges/';
  const fixtureRoot = path.resolve(ROOT, process.env.SJ_REFACTOR_FIXTURE_ROOT || '.');
  const files = fixtureFiles(fixtureRoot);
  const { hydrateMilitaryScienceTopicRuntime } = await import('./lib/military-science-runtime.mjs');
  const externalHtml = fs.readFileSync(path.join(fixtureRoot, file), 'utf8');
  const inlineHtml = hydrateMilitaryScienceTopicRuntime(externalHtml);
  assert.notEqual(inlineHtml, externalHtml, 'fixture must exercise shared-runtime hydration');
  const browser = await chromium.launch({ headless: true });
  try {
    for (const width of [390, 1280]) {
      const outcomes = [];
      for (const html of [inlineHtml, externalHtml]) {
        const context = await browser.newContext({ viewport: { width, height: 900 }, reducedMotion: 'reduce', serviceWorkers: 'block' });
        try {
          const page = await context.newPage();
          await page.addInitScript(() => {
            localStorage.removeItem('sjmaths.theme.preference');
            localStorage.setItem('sjmaths-theme', 'green');
          });
          const pageErrors = [];
          page.on('pageerror', error => pageErrors.push(error.message));
          const evidence = await routeRepositoryFixtures(page, { root: fixtureRoot, files });
          await page.route(`https://sjmaths.com${route}`, request => request.fulfill({ contentType: 'text/html', body: html }));
          await page.clock.install();
          await page.goto(`https://sjmaths.com${route}`);
          const quiz = JSON.parse(await page.locator('#quiz-data').textContent());
          const exam = JSON.parse(await page.locator('#test-data').textContent());
          const expectedTypes = ['mcq', 'assertion_reason', 'true_false', 'fill_blank', 'match_following', 'case_based', 'short_answer'];
          assert.deepEqual([...new Set(quiz.map(item => item.type))].sort(), expectedTypes.slice().sort());
          const tabs = page.locator('.tab-btn');
          assert.equal(await tabs.count(), 4);
          const panelText = [];
          for (let index = 0; index < 4; index++) {
            const tab = tabs.nth(index);
            await tab.focus();
            await page.keyboard.press('Enter');
            assert.equal(await tab.getAttribute('aria-selected'), 'true');
            const id = await tab.getAttribute('data-tab');
            assert.equal(await page.locator(`#${id}`).isVisible(), true);
            panelText.push((await page.locator(`#${id}`).innerText()).slice(0, 300));
          }

          await page.locator('#btn-theme-toggle').click();
          const darkMode = await page.locator('body').evaluate(body => body.classList.contains('dark-mode'));
          assert.equal(darkMode, true);
          assert.equal(await page.locator('html').getAttribute('data-theme'), 'dark');
          assert.equal(await page.locator('#btn-theme-toggle').getAttribute('aria-pressed'), 'true');
          assert.equal(await page.evaluate(() => localStorage.getItem('sjmaths-theme')), 'green');
          await tabs.nth(1).click();
          for (const type of expectedTypes) {
            const index = quiz.findIndex(item => item.type === type);
            assert.notEqual(index, -1, `fixture needs ${type}`);
            const feedback = page.locator(`#quiz-feedback-${index} .quiz-feedback.show`);
            if (type === 'fill_blank') {
              await page.locator(`#quiz-input-${index}`).fill(String(quiz[index].accepted_answers[0]));
              await page.locator(`[data-fill="${index}"]`).click();
              assert.ok((await feedback.textContent()).includes('Accepted answer(s)'));
            } else if (type === 'short_answer') {
              await page.locator(`[data-short="${index}"]`).click();
              assert.ok((await feedback.textContent()).includes('Expected answer'));
            } else {
              await page.locator(`#quiz-card-${index} [data-option="${quiz[index].correct_index}"]`).click();
              assert.ok((await feedback.textContent()).includes('Correct'));
            }
            assert.equal(await feedback.isVisible(), true, `${type} feedback must be visible`);
          }
          assert.equal(await page.locator('#quiz-score').innerText(), `Score: 6 / ${quiz.length}`);

          await tabs.nth(3).click();
          await page.locator(`#test-card-0 [data-option="${exam[0].correct_index}"]`).click();
          await page.locator('#btn-submit-test').click();
          assert.equal(await page.locator('#test-score').innerText(), '1');
          assert.equal(await page.locator('#test-result').isVisible(), true);
          assert.equal(await page.locator('#test-feedback-0 .quiz-feedback.show').isVisible(), true);
          await Promise.all([page.waitForNavigation(), page.locator('#btn-retake-test').click()]);
          assert.equal(await page.locator('#test-result').isVisible(), false);
          await page.locator('.tab-btn[data-tab="tab-test"]').click();
          await page.clock.runFor(600000);
          assert.equal(await page.locator('#test-score').innerText(), '0');
          assert.equal(await page.locator('#test-result').isVisible(), true);

          assert.equal(await page.evaluate(() => Math.max(0, document.documentElement.scrollWidth - innerWidth)), 0, `${width}px horizontal overflow`);
          assert.deepEqual(pageErrors, []);
          assert.deepEqual(evidence.missing, []);
          outcomes.push({ panelText, darkMode, quizScore: await page.locator('#quiz-score').innerText(), timerResult: await page.locator('#test-score').innerText(), errors: pageErrors });
        } finally { await context.close(); }
      }
      assert.deepEqual(outcomes[1], outcomes[0], `${width}px inline/external runtime parity`);
    }
  } finally { await browser.close(); }
});
