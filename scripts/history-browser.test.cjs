const test = require('node:test');
const assert = require('node:assert/strict');
const { chromium } = require('playwright');
const { ROOT, siteFiles } = require('./seo-html.cjs');
const { routeRepositoryFixtures } = require('./lib/browser-fixture.cjs');

test('History keyboard quiz, all question types, resets and test lifecycle', { timeout: 90000 }, async () => {
  const browser = await chromium.launch({ headless: true });
  try {
    for (const width of [390, 1280]) {
      const context = await browser.newContext({ viewport: { width, height: 900 }, reducedMotion: 'reduce', serviceWorkers: 'block' });
      try {
        const page = await context.newPage();
        const evidence = await routeRepositoryFixtures(page, { root: ROOT, files: siteFiles() });
        await page.goto('https://sjmaths.com/history/indus-saraswati-valley-civilization/art/');
        await page.clock.install();
        const quiz = await page.locator('#history-quiz-data').evaluate(el => JSON.parse(el.textContent));
        assert.equal(new Set(quiz.map(question => question.type)).size, 7);
        await page.locator('#tab-btn-quiz').focus();
        await page.keyboard.press('Enter');
        assert.equal(await page.locator('#tab-btn-quiz').getAttribute('aria-selected'), 'true');
        assert.equal(await page.locator('#tab-notes').isVisible(), false);
        let expectedScore = 0;
        for (let index = 0; index < quiz.length; index++) {
          const question = quiz[index];
          if (question.type === 'fill_blank') {
            await page.locator(`#quiz-input-${index}`).fill(question.accepted_answers[0]);
            await page.locator(`[data-fill="${index}"]`).click();
            expectedScore++;
          } else if (question.type === 'short_answer') {
            await page.locator(`#quiz-input-${index}`).fill(question.expected_answer || 'Practice answer');
            await page.locator(`[data-short="${index}"]`).click();
          } else {
            await page.locator(`[data-quiz="${index}"][data-option="${question.correct_index}"]`).click();
            expectedScore++;
          }
          assert.equal(await page.locator(`#quiz-card-${index}`).getAttribute('data-answered'), 'true');
          assert.equal(await page.locator(`#quiz-card-${index} button:not(:disabled)`).count(), 0);
          assert.ok((await page.locator(`#quiz-feedback-${index}`).innerText()).length > 0);
        }
        assert.equal(await page.locator('#quiz-score').innerText(), `Score: ${expectedScore} / ${quiz.length}`);
        await Promise.all([page.waitForEvent('load'), page.locator('#btn-reset-quiz').click()]);
        assert.equal(await page.locator('#quiz-score').textContent(), `Score: 0 / ${quiz.length}`);
        assert.equal(await page.locator('[data-answered="true"]').count(), 0);
        await page.locator('#tab-btn-summary').focus();
        await page.keyboard.press('Space');
        assert.equal(await page.locator('#tab-summary').isVisible(), true);
        await page.locator('#tab-btn-test').click();
        await page.clock.runFor(3000);
        assert.equal(await page.locator('#test-timer').innerText(), '09:57');
        await page.locator('#tab-btn-notes').click();
        await page.locator('#tab-btn-test').click();
        await page.clock.runFor(2000);
        assert.equal(await page.locator('#test-timer').innerText(), '09:55');
        const questions = await page.locator('#history-test-data').evaluate(el => JSON.parse(el.textContent));
        for (let index = 0; index < questions.length; index++) {
          await page.locator(`[data-test="${index}"][data-option="${questions[index].correct_index}"]`).click();
        }
        await page.locator('#btn-submit-test').click();
        assert.equal(await page.locator('#test-score').innerText(), '10');
        assert.equal(await page.locator('#test-result').isVisible(), true);
        assert.equal(await page.locator('[data-test]:not(:disabled)').count(), 0);
        const stoppedAt = await page.locator('#test-timer').innerText();
        await page.clock.runFor(5000);
        assert.equal(await page.locator('#test-timer').innerText(), stoppedAt, 'submitted tests must stop their timer');
        await Promise.all([page.waitForEvent('load'), page.locator('#btn-retake-test').click()]);
        await page.locator('#tab-btn-test').click();
        await page.clock.runFor(600000);
        assert.equal(await page.locator('#test-result').isVisible(), true, 'expiry submits unanswered tests');
        assert.equal(await page.locator('#test-score').innerText(), '0');
        assert.equal(await page.locator('#test-timer').innerText(), '00:00');
        assert.deepEqual(evidence.missing, []);
        assert.deepEqual(evidence.errors, []);
      } finally { await context.close(); }
    }
  } finally { await browser.close(); }
});

test('offline regenerated History fixture loads shared assets and four working tabs', { timeout: 30000 }, async () => {
  const { renderHistoryHtml } = await import('./lib/history-renderer.mjs');
  const { historyStyles } = await import('./lib/history-styles.mjs');
  const fixture = await import('./fixtures/history.mjs');
  const browser = await chromium.launch({ headless: true });
  try {
    const page = await browser.newPage({ viewport: { width: 390, height: 900 }, reducedMotion: 'reduce' });
    const evidence = await routeRepositoryFixtures(page, { root: ROOT, files: siteFiles() });
    const html = renderHistoryHtml(fixture.originalHtml(historyStyles[0].link), fixture.content, fixture.questions, fixture.metadata);
    await page.route('https://sjmaths.com/history/refactor-fixture/', route => route.fulfill({ contentType: 'text/html', body: html }));
    await page.goto('https://sjmaths.com/history/refactor-fixture/');
    assert.equal(await page.locator('.notes-section').count(), 6);
    for (const panel of ['quiz', 'summary', 'test', 'notes']) {
      await page.locator(`#tab-btn-${panel}`).click();
      assert.equal(await page.locator(`#tab-${panel}`).isVisible(), true);
      assert.equal(await page.locator('.tab-panel:not(.hidden)').count(), 1);
    }
    await page.locator('#tab-btn-quiz').click();
    await page.locator('[data-quiz="0"][data-option="0"]').click();
    assert.equal(await page.locator('#quiz-score').innerText(), 'Score: 1 / 35');
    await page.locator('#tab-btn-test').click();
    await page.locator('#btn-submit-test').click();
    assert.equal(await page.locator('#test-result').isVisible(), true);
    assert.deepEqual(evidence.errors, []);
    assert.deepEqual(evidence.missing, []);
  } finally { await browser.close(); }
});
