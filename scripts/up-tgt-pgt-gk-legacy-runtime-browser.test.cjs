const test = require('node:test');
const assert = require('node:assert/strict');
const crypto = require('node:crypto');
const fs = require('node:fs');
const path = require('node:path');
const { execFileSync } = require('node:child_process');
const { chromium } = require('playwright');
const { ROOT } = require('./seo-html.cjs');
const { fixtureFiles, routeRepositoryFixtures } = require('./lib/browser-fixture.cjs');

const baseline = 'afb5a3473445d7609eb3004b999c66b9d0215c70';
const pages = [
  ['history', 'up-tgt-pgt-gk/indian-history/vijayanagara/index.html'],
  ['polity', 'up-tgt-pgt-gk/indian-polity/constitutional-bodies/index.html'],
];
const fixtureRoot = path.resolve(ROOT, process.env.SJ_REFACTOR_FIXTURE_ROOT || '.');

test('shared GK runtime preserves legacy English-only history and polity learning flows', { timeout: 180000 }, async () => {
  const browser = await chromium.launch({ headless: true });
  const files = fixtureFiles(fixtureRoot);
  const evidenceRoot = path.join(ROOT, 'scratch/refactor/up-tgt-pgt-gk-legacy-runtime', path.basename(fixtureRoot));
  fs.mkdirSync(evidenceRoot, { recursive: true });
  const report = [];
  try {
    for (const [id, file] of pages) for (const width of [390, 1280]) {
      const originalHtml = execFileSync('git', ['show', `${baseline}:${file}`], { cwd: ROOT, encoding: 'utf8', maxBuffer: 20e6 });
      const sharedHtml = fs.readFileSync(path.join(fixtureRoot, file), 'utf8');
      assert.doesNotMatch(originalHtml, /id="bilingual-data"/);
      assert.match(sharedHtml, /data-up-tgt-pgt-gk-runtime="topic"/);
      const results = [];

      for (const [mode, html] of [['inline', originalHtml], ['shared', sharedHtml]]) {
        const context = await browser.newContext({ viewport: { width, height: 900 }, reducedMotion: 'reduce', serviceWorkers: 'block' });
        try {
          const page = await context.newPage();
          const evidence = await routeRepositoryFixtures(page, { root: fixtureRoot, files });
          await page.addInitScript(() => {
            localStorage.setItem('sjmaths_language', 'hi');
            localStorage.setItem('sjmaths_theme', 'light');
            localStorage.setItem('sj_theme', 'light');
          });
          await page.route('**/assets/js/require-auth.min.js*', route => route.fulfill({ contentType: 'text/javascript', body: '' }));
          const url = `https://sjmaths.com/${file}`;
          await page.route(url, route => route.fulfill({ contentType: 'text/html', body: html }));
          await page.goto(url, { waitUntil: 'load', timeout: 30000 });
          await page.evaluate(() => document.fonts.ready);
          await page.waitForTimeout(400);
          assert.deepEqual(evidence.errors, [], `${id}/${mode} runtime errors`);
          assert.deepEqual(evidence.missing, [], `${id}/${mode} missing local requests`);
          const initial = await page.evaluate(() => ({
            language: document.documentElement.lang,
            heading: document.querySelector('h1')?.textContent.trim(),
            visibleText: document.querySelector('main')?.innerText.slice(0, 600),
            quizCount: document.querySelectorAll('#tab-quiz [data-quiz], #tab-quiz [data-fill], #tab-quiz [data-short]').length,
            testCount: document.querySelectorAll('#tab-test [data-test]').length,
            overflow: Math.max(0, document.documentElement.scrollWidth - innerWidth),
          }));
          assert.equal(initial.language, 'en', 'legacy English-only page remains English when stored Hindi is unavailable');
          assert.ok(initial.quizCount > 0);
          assert.ok(initial.testCount > 0);
          const screenshot = path.join(evidenceRoot, `${id}-${width}-${mode}.png`);
          await page.screenshot({ path: screenshot, animations: 'disabled' });

          await page.locator('#tab-btn-quiz').focus();
          await page.keyboard.press('Enter');
          const quizAnswer = await page.evaluate(() => JSON.parse(document.getElementById('quiz-data').textContent)[0].correct_index);
          await page.locator(`#quiz-card-0 [data-quiz="0"][data-option="${quizAnswer}"]`).click();
          const quizResult = {
            feedback: await page.locator('#quiz-feedback-0').innerText(),
            score: await page.locator('#quiz-score').innerText(),
            optionsDisabled: await page.locator('#quiz-card-0 button').evaluateAll(buttons => buttons.every(button => button.disabled)),
          };

          await page.locator('#tab-btn-test').focus();
          await page.keyboard.press('Enter');
          const testAnswer = await page.evaluate(() => JSON.parse(document.getElementById('test-data').textContent)[0].correct_index);
          await page.locator(`#test-card-0 [data-test="0"][data-option="${testAnswer}"]`).click();
          await page.locator('#btn-submit-test').click();
          const testResult = {
            score: await page.locator('#test-score').innerText(),
            resultVisible: await page.locator('#test-result').evaluate(element => !element.classList.contains('hidden')),
            submitHidden: await page.locator('#btn-submit-test').evaluate(element => element.classList.contains('hidden')),
          };
          results.push({ mode, initial, quizResult, testResult, screenshot, errors: evidence.errors, missing: evidence.missing });
        } finally { await context.close(); }
      }

      assert.deepEqual(results[1].initial, results[0].initial, `${id}/${width} initial view parity`);
      assert.deepEqual(results[1].quizResult, results[0].quizResult, `${id}/${width} quiz keyboard/feedback parity`);
      assert.deepEqual(results[1].testResult, results[0].testResult, `${id}/${width} test submission parity`);
      assert.equal(results[1].quizResult.optionsDisabled, true);
      assert.equal(results[1].testResult.resultVisible, true);
      assert.equal(results[1].testResult.submitHidden, true);
      const digest = filePath => crypto.createHash('sha256').update(fs.readFileSync(filePath)).digest('hex');
      assert.equal(digest(results[1].screenshot), digest(results[0].screenshot), `${id}/${width} initial screenshot parity`);
      report.push({ id, width, initial: results[0].initial, quizResult: results[0].quizResult, testResult: results[0].testResult });
    }
    fs.writeFileSync(path.join(evidenceRoot, 'report.json'), `${JSON.stringify(report, null, 2)}\n`);
  } finally { await browser.close(); }
});
