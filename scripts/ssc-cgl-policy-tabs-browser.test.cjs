const test = require('node:test');
const assert = require('node:assert/strict');
const crypto = require('node:crypto');
const fs = require('node:fs');
const path = require('node:path');
const { execFileSync } = require('node:child_process');
const { chromium } = require('playwright');
const { ROOT } = require('./seo-html.cjs');
const { fixtureFiles, routeRepositoryFixtures } = require('./lib/browser-fixture.cjs');

const baseline = 'aec62244f2281ab9fa115837f315ffd91e3faa6c';
const pages = [
  ['citizenship', 'ssc-cgl/general-awareness/general-policy-polity/citizenship-articles-5-11-and-caa/index.html'],
  ['parliament', 'ssc-cgl/general-awareness/general-policy-polity/parliament-lok-sabha-rajya-sabha-and-officers/index.html'],
];
const fixtureRoot = path.resolve(ROOT, process.env.SJ_REFACTOR_FIXTURE_ROOT || '.');

async function tabState(page) {
  return page.evaluate(() => ({
    activePanel: document.querySelector('.tab-panel.active')?.id || null,
    activeButtonIndex: [...document.querySelectorAll('.main-tabs-nav .tab-btn')].findIndex(button => button.classList.contains('active')),
    activePanelCount: document.querySelectorAll('.tab-panel.active').length,
    overflow: Math.max(0, document.documentElement.scrollWidth - innerWidth),
  }));
}

test('SSC-CGL policy tab runtime preserves deep links, keyboard switching and pageshow restoration', { timeout: 180000 }, async () => {
  const browser = await chromium.launch({ headless: true });
  const evidenceRoot = path.join(ROOT, 'scratch/refactor/ssc-cgl-policy-tabs', path.basename(fixtureRoot));
  fs.mkdirSync(evidenceRoot, { recursive: true });
  const summaries = [];

  try {
    for (const [id, file] of pages) for (const width of [390, 1280]) {
      const route = `/${file.slice(0, file.lastIndexOf('/'))}/`;
      const url = `https://sjmaths.com${route}#tab-mini-test`;
      const originalHtml = execFileSync('git', ['show', `${baseline}:${file}`], { cwd: ROOT, encoding: 'utf8', maxBuffer: 20e6 });
      const sharedHtml = fs.readFileSync(path.join(fixtureRoot, file), 'utf8');
      assert.match(sharedHtml, /data-ssc-cgl-policy-tabs="shared"/);
      const outcomes = [];

      for (const [kind, html] of [['inline', originalHtml], ['shared', sharedHtml]]) {
        const context = await browser.newContext({ viewport: { width, height: 900 }, reducedMotion: 'reduce', serviceWorkers: 'block' });
        try {
          const page = await context.newPage();
          const evidence = await routeRepositoryFixtures(page, { root: fixtureRoot, files: fixtureFiles(fixtureRoot) });
          await page.addInitScript(() => sessionStorage.setItem('sj_auth_gate_skipped', 'true'));
          await page.route(url.split('#')[0], routeHandler => routeHandler.fulfill({ contentType: 'text/html', body: html }));
          await page.goto(url, { waitUntil: 'networkidle' });
          await page.evaluate(async () => {
            if (window.MathJax?.startup?.promise) await window.MathJax.startup.promise;
            await document.fonts.ready;
          });
          const initial = await tabState(page);
          assert.deepEqual(initial, { activePanel: 'tab-mini-test', activeButtonIndex: 3, activePanelCount: 1, overflow: 0 }, `${id}/${width}/${kind} hash-selected initial tab`);

          const screenshotPath = path.join(evidenceRoot, `${id}-${width}-${kind}.png`);
          await page.screenshot({ path: screenshotPath, animations: 'disabled' });

          const practiceButton = page.locator('.main-tabs-nav .tab-btn').nth(1);
          await practiceButton.focus();
          await page.keyboard.press('Enter');
          await page.waitForFunction(() => document.querySelector('.tab-panel.active')?.id === 'tab-practice');
          const keyboardPractice = await tabState(page);
          assert.equal(keyboardPractice.activeButtonIndex, 1, `${id}/${width}/${kind} keyboard practice activation`);

          await page.evaluate(() => window.dispatchEvent(new Event('pageshow')));
          const restored = await tabState(page);
          assert.equal(restored.activePanel, 'tab-mini-test', `${id}/${width}/${kind} pageshow restores hash-selected tab`);
          assert.equal(restored.activeButtonIndex, 3, `${id}/${width}/${kind} pageshow restores active button`);
          outcomes.push({ kind, screenshotPath, initial, keyboardPractice, restored, errors: evidence.errors.filter(error => !error.startsWith('Service Worker registration failed')), missing: evidence.missing });
        } finally { await context.close(); }
      }

      assert.deepEqual(outcomes[1].initial, outcomes[0].initial, `${id}/${width} initial state parity`);
      assert.deepEqual(outcomes[1].keyboardPractice, outcomes[0].keyboardPractice, `${id}/${width} keyboard flow parity`);
      assert.deepEqual(outcomes[1].restored, outcomes[0].restored, `${id}/${width} pageshow flow parity`);
      assert.deepEqual(outcomes[1].errors, outcomes[0].errors, `${id}/${width} browser error parity`);
      assert.deepEqual(outcomes[1].missing, outcomes[0].missing, `${id}/${width} local asset parity`);
      assert.deepEqual(outcomes[1].missing, [], `${id}/${width} all local assets resolve`);
      const digest = filePath => crypto.createHash('sha256').update(fs.readFileSync(filePath)).digest('hex');
      assert.equal(digest(outcomes[1].screenshotPath), digest(outcomes[0].screenshotPath), `${id}/${width} initial screenshot parity`);
      summaries.push({ id, width, initial: outcomes[1].initial, keyboardPractice: outcomes[1].keyboardPractice, restored: outcomes[1].restored, errors: outcomes[1].errors, missing: outcomes[1].missing });
    }
    fs.writeFileSync(path.join(evidenceRoot, 'results.json'), JSON.stringify({ fixtureRoot: path.relative(ROOT, fixtureRoot) || '.', baseline, summaries }, null, 2) + '\n');
  } finally { await browser.close(); }
});
