const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { chromium } = require('playwright');
const { ROOT } = require('./seo-html.cjs');
const { fixtureFiles, routeRepositoryFixtures } = require('./lib/browser-fixture.cjs');

test('Music Instrumental shared runtime preserves four tabs, quiz types, theme and timed test', { timeout: 180000 }, async () => {
  const file = 'music-instrumental/avanaddh-vadya/bol-notation/kathin-layakari/index.html';
  const route = '/music-instrumental/avanaddh-vadya/bol-notation/kathin-layakari/';
  const fixtureRoot = path.resolve(ROOT, process.env.SJ_REFACTOR_FIXTURE_ROOT || '.');
  const files = fixtureFiles(fixtureRoot);
  const { hydrateMusicInstrumentalTopicRuntime } = await import('./lib/music-instrumental-runtime.mjs');
  const externalHtml = fs.readFileSync(path.join(fixtureRoot, file), 'utf8');
  const inlineHtml = hydrateMusicInstrumentalTopicRuntime(externalHtml);
  assert.notEqual(inlineHtml, externalHtml, 'fixture must exercise shared-runtime hydration');
  const browser = await chromium.launch({ headless: true });
  try {
    for (const width of [390, 1280]) {
      const outcomes = [];
      for (const html of [inlineHtml, externalHtml]) {
        const context = await browser.newContext({ viewport: { width, height: 900 }, reducedMotion: 'reduce', serviceWorkers: 'block' });
        try {
          const page = await context.newPage();
          const evidence = await routeRepositoryFixtures(page, { root: fixtureRoot, files });
          await page.route(`https://sjmaths.com${route}`, request => request.fulfill({ contentType: 'text/html', body: html }));
          await page.clock.install();
          await page.goto(`https://sjmaths.com${route}`);
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
          await tabs.nth(1).click();

          const mcq = page.locator('[data-quiz]').first();
          const mcqCard = mcq.locator('xpath=ancestor::*[contains(@class,"quiz-question-card")][1]');
          const correct = Number(await mcqCard.getAttribute('data-correct'));
          await mcqCard.locator(`[data-option="${correct}"]`).click();
          assert.equal(await page.locator('#quiz-score').innerText(), `अंक: 1 / ${await page.locator('.quiz-question-card').count()}`);
          const mcqFeedback = page.locator(`#quiz-feedback-${await mcqCard.getAttribute('data-index')}`);
          assert.equal(await mcqFeedback.isVisible(), true, JSON.stringify(await mcqFeedback.evaluate(el => { const ancestors = []; for (let node = el; node; node = node.parentElement) { const style = getComputedStyle(node), rect = node.getBoundingClientRect(); ancestors.push({ tag: node.tagName, id: node.id, className: node.className, display: style.display, visibility: style.visibility, opacity: style.opacity, height: Math.round(rect.height) }); } return ancestors.slice(0, 8); })));
          assert.ok((await mcqFeedback.textContent()).includes('सही'));

          const fillButton = page.locator('[data-fill]').first();
          const fillCard = fillButton.locator('xpath=ancestor::*[contains(@class,"quiz-question-card")][1]');
          const fillIndex = await fillCard.getAttribute('data-index');
          const accepted = (await fillCard.locator('.accepted-answer').first().innerText()).trim();
          await page.locator(`#quiz-input-${fillIndex}`).fill(accepted);
          await fillButton.click();
          assert.ok((await page.locator(`#quiz-feedback-${fillIndex}`).innerText()).includes('स्वीकृत उत्तर'));

          const shortButton = page.locator('[data-short]').first();
          const shortCard = shortButton.locator('xpath=ancestor::*[contains(@class,"quiz-question-card")][1]');
          const shortIndex = await shortCard.getAttribute('data-index');
          await shortButton.click();
          assert.ok((await page.locator(`#quiz-feedback-${shortIndex}`).innerText()).includes('अपेक्षित उत्तर'));

          await tabs.nth(3).click();
          const testOption = page.locator('[data-test]').first();
          const testCard = testOption.locator('xpath=ancestor::*[contains(@class,"test-question-card")][1]');
          const testCorrect = Number(await testCard.getAttribute('data-correct'));
          await testCard.locator(`[data-option="${testCorrect}"]`).click();
          await page.locator('#btn-submit-test').click();
          assert.equal(await page.locator('#test-score').innerText(), '1');
          assert.equal(await page.locator('#test-result').isVisible(), true);
          await Promise.all([page.waitForNavigation(), page.locator('#btn-retake-test').click()]);
          assert.equal(await page.locator('#test-result').isVisible(), false);

          await page.locator('.tab-btn[data-tab="tab-test"]').click();
          await page.clock.runFor(600000);
          const timedScore = await page.locator('#test-score').innerText();
          assert.equal(timedScore, '0');
          assert.equal(await page.locator('#test-result').isVisible(), true);
          assert.equal(await page.evaluate(() => Math.max(0, document.documentElement.scrollWidth - innerWidth)), 0, `${width}px horizontal overflow`);
          assert.deepEqual(evidence.missing, []);
          outcomes.push({ panelText, darkMode, timedScore, errors: evidence.errors });
        } finally { await context.close(); }
      }
      assert.deepEqual(outcomes[1], outcomes[0], `${width}px inline/external parity`);
    }
  } finally { await browser.close(); }
});
