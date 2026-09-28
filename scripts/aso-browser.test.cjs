const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { execFileSync } = require('node:child_process');
const { chromium } = require('playwright');
const { ROOT, siteFiles } = require('./seo-html.cjs');
const { routeRepositoryFixtures } = require('./lib/browser-fixture.cjs');

test('ASO style extraction preserves keyboard tabs, quiz, scoring and completion', { timeout: 120000 }, async () => {
  const file = 'upsc-aso/aerodynamics-performance-stability/absolute-and-service-ceiling/index.html';
  const url = 'https://sjmaths.com/' + file.replace(/index\.html$/, '');
  const before = execFileSync('git', ['show', `HEAD:${file}`], { cwd: ROOT, encoding: 'utf8', maxBuffer: 10e6 });
  const after = fs.readFileSync(path.join(ROOT, file), 'utf8');
  const files = siteFiles();
  const browser = await chromium.launch({ headless: true });
  try {
    for (const width of [390, 1280]) {
      const outcomes = [];
      for (const html of [before, after]) {
        const context = await browser.newContext({ viewport: { width, height: 900 }, reducedMotion: 'reduce', serviceWorkers: 'block' });
        try {
          const page = await context.newPage();
          const evidence = await routeRepositoryFixtures(page, { root: ROOT, files });
          await page.route(url, route => route.fulfill({ contentType: 'text/html', body: html }));
          await page.goto(url);
          await page.clock.install();
          const tabs = page.locator('.tab-strip .tab-btn');
          const states = [];
          for (let i = 0; i < await tabs.count(); i++) {
            await tabs.nth(i).focus();
            await page.keyboard.press('Enter');
            assert.equal(await tabs.nth(i).getAttribute('aria-selected'), 'true');
            // Navigation time is intentionally variable. Exclude only the live
            // clock from content parity; timer cleanup is asserted separately.
            const panel = page.locator('.tab-panel.active');
            let text = await panel.innerText();
            const clock = panel.locator('#test-timer-display');
            if (await clock.count()) text = text.replace(await clock.innerText(), '[countdown]');
            states.push(text);
          }
          await tabs.nth(1).click();
          await page.locator('.quiz-option').first().click();
          const feedback = await page.locator('#practice-exp-1').innerText();
          assert.equal(await page.locator('#practice-exp-1').isVisible(), true);
          await tabs.nth(2).click();
          const questions = page.locator('.test-question-item');
          assert.equal(await questions.count(), 10);
          for (let i = 0; i < await questions.count(); i++) {
            const question = questions.nth(i);
            const correct = Number(await question.getAttribute('data-correct'));
            await question.locator('.test-option').nth(correct).click();
          }
          await page.locator('#submit-test-btn').click();
          const score = await page.locator('#test-score-display').innerText();
          assert.equal(score, '30 / 30');
          const timer = await page.locator('#test-timer-display').innerText();
          await page.clock.runFor(3000);
          assert.equal(await page.locator('#test-timer-display').innerText(), timer);
          await page.locator('[onclick="reviewTestAnswers()"]').click();
          assert.equal(await page.locator('.test-explanation:visible').count(), 10);
          await tabs.nth(3).click();
          const mark = page.locator('#mark-topic-btn');
          await mark.click();
          assert.equal(await mark.evaluate(button => button.classList.contains('marked')), true);
          const key = 'aso_topic_done_absolute-and-service-ceiling';
          assert.equal(await page.evaluate(key => localStorage.getItem(key), key), 'true');
          await mark.click();
          assert.equal(await page.evaluate(key => localStorage.getItem(key), key), null);
          assert.deepEqual(evidence.missing, []);
          assert.deepEqual(evidence.errors.filter(error => !error.startsWith('Service Worker registration failed')), []);
          outcomes.push({ states, feedback, score });
        } finally { await context.close(); }
      }
      assert.deepEqual(outcomes[1], outcomes[0], `${width}px flow parity`);
    }
  } finally { await browser.close(); }
});
