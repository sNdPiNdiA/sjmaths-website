const test = require('node:test');
const assert = require('node:assert/strict');
const crypto = require('node:crypto');
const fs = require('node:fs');
const path = require('node:path');
const { execFileSync } = require('node:child_process');
const { chromium } = require('playwright');
const { ROOT } = require('./seo-html.cjs');
const { fixtureFiles, routeRepositoryFixtures } = require('./lib/browser-fixture.cjs');

const baseline = '4a81ff7b7c9adce1ae0eba3f7243c9d722ad400a';
const file = 'physics/electricity-and-magnetism/alternating-current/ac-bridges/index.html';
const route = '/physics/electricity-and-magnetism/alternating-current/ac-bridges/';
const fixtureRoot = path.resolve(ROOT, process.env.SJ_REFACTOR_FIXTURE_ROOT || '.');

test('Physics shared assets preserve mobile/desktop appearance and keyboard learning flows', { timeout: 120000 }, async () => {
  const inlineHtml = execFileSync('git', ['show', `${baseline}:${file}`], { cwd: ROOT, encoding: 'utf8', maxBuffer: 20e6 });
  const externalHtml = fs.readFileSync(path.join(fixtureRoot, file), 'utf8');
  const browser = await chromium.launch({ headless: true });
  const evidenceRoot = path.join(ROOT, 'scratch/refactor/physics-topic-browser', path.basename(fixtureRoot));
  fs.mkdirSync(evidenceRoot, { recursive: true });

  try {
    for (const width of [390, 1280]) {
      const results = [];
      for (const [kind, html] of [['inline', inlineHtml], ['external', externalHtml]]) {
        const context = await browser.newContext({ viewport: { width, height: 900 }, reducedMotion: 'reduce' });
        try {
          const page = await context.newPage();
          const evidence = await routeRepositoryFixtures(page, { root: fixtureRoot, files: fixtureFiles(fixtureRoot) });
          await page.route(`https://sjmaths.com${route}`, request => request.fulfill({ contentType: 'text/html', body: html }));
          await page.goto(`https://sjmaths.com${route}`, { waitUntil: 'networkidle' });
          await page.evaluate(() => document.fonts.ready);
          assert.deepEqual(evidence.errors, [], `${kind} page errors`);
          assert.deepEqual(evidence.missing, [], `${kind} missing local requests`);

          if (kind === 'external') {
            assert.equal(await page.locator('link[data-physics-topic-style="lesson"]').count(), 1);
            const styleHref = await page.locator('link[data-physics-topic-style="lesson"]').getAttribute('href');
            assert.match(styleHref, /\/assets\/css\/physics-topic(?:\.min)?\.css(?:\?|$)/);
            assert.equal(await page.locator('script[data-physics-topic-runtime="lesson"]').count(), 1);
            const runtimeSrc = await page.locator('script[data-physics-topic-runtime="lesson"]').getAttribute('src');
            assert.match(runtimeSrc, /\/assets\/js\/physics-topic(?:\.min)?\.js(?:\?|$)/);
          }

          const screenshotPath = path.join(evidenceRoot, `${width}-${kind}.png`);
          await page.screenshot({ path: screenshotPath, animations: 'disabled' });
          const overflow = await page.evaluate(() => Math.max(0, document.documentElement.scrollWidth - innerWidth));

          const quizTab = page.locator('.tab[data-panel="quiz"]');
          await quizTab.focus();
          await page.keyboard.press('Enter');
          assert.equal(await page.locator('#quiz').evaluate(element => element.classList.contains('active')), true);
          const quizQuestion = page.locator('#quiz .question').first();
          const quizCorrect = await quizQuestion.getAttribute('data-correct');
          const correctQuizOption = quizQuestion.locator(`.option[data-index="${quizCorrect}"]`);
          await correctQuizOption.focus();
          await page.keyboard.press('Enter');
          assert.equal(await quizQuestion.locator('.answer').isVisible(), true);
          assert.equal(await correctQuizOption.isDisabled(), true);

          const testTab = page.locator('.tab[data-panel="test"]');
          await testTab.focus();
          await page.keyboard.press('Enter');
          assert.equal(await page.locator('#test').evaluate(element => element.classList.contains('active')), true);
          const testQuestion = page.locator('#test .question').first();
          const testCorrect = await testQuestion.getAttribute('data-correct');
          await testQuestion.locator(`.option[data-index="${testCorrect}"]`).click();
          assert.equal(await testQuestion.locator('.answer').isVisible(), true);

          results.push({ kind, screenshotPath, overflow, errors: evidence.errors, missing: evidence.missing });
        } finally { await context.close(); }
      }
      assert.equal(results[1].overflow, results[0].overflow, `${width}px overflow parity`);
      assert.deepEqual(results[1].errors, results[0].errors);
      assert.deepEqual(results[1].missing, results[0].missing);
      const digest = filePath => crypto.createHash('sha256').update(fs.readFileSync(filePath)).digest('hex');
      assert.equal(digest(results[1].screenshotPath), digest(results[0].screenshotPath), `${width}px initial pixels`);
    }
  } finally { await browser.close(); }
});
