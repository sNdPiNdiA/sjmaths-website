const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const { execFileSync } = require('node:child_process');
const { chromium } = require('playwright');
const { ROOT } = require('./seo-html.cjs');
const { fixtureFiles, routeRepositoryFixtures } = require('./lib/browser-fixture.cjs');

const baseline = '237db669da5fca0a8ff8ae6a5a601d284a367642';
const pages = [
  ['child-psychology', 'up-assistant-teacher/child-psychology/creating-conducive-learning-environment/index.html'],
  ['english', 'up-assistant-teacher/english/adjectives-comparative-superlative/index.html'],
  ['environmental-social-studies', 'up-assistant-teacher/environmental-social-studies/latitudes-longitudes/index.html'],
  ['hindi', 'up-assistant-teacher/hindi/alankaara-bhaeda-va-udaaharana/index.html'],
  ['information-technology', 'up-assistant-teacher/information-technology/computers-fundamentals-applications/index.html'],
  ['life-skill-management', 'up-assistant-teacher/life-skill-management/constitutional-human-values/index.html'],
  ['sanskrit', 'up-assistant-teacher/sanskrit/alankaara-upamaa-raoopaka-utaparaekashaa-aadai/index.html'],
  ['science', 'up-assistant-teacher/science/distance/index.html'],
  ['teaching-skills', 'up-assistant-teacher/teaching-skills/current-indian-society-elementary-education/index.html'],
];
const fixtureRoot = path.resolve(ROOT, process.env.SJ_REFACTOR_FIXTURE_ROOT || '.');
const fixtures = fixtureFiles(fixtureRoot);

test('removing the duplicated helper preserves nine subject tab and keyboard flows', { timeout: 180000 }, async () => {
  const browser = await chromium.launch({ headless: true });
  const evidenceRoot = path.join(ROOT, 'scratch/refactor/up-assistant-renderer-dedupe', path.basename(fixtureRoot));
  fs.mkdirSync(evidenceRoot, { recursive: true });
  const results = [];

  try {
    for (const width of [390, 1280]) {
      const context = await browser.newContext({ viewport: { width, height: 900 }, reducedMotion: 'reduce', serviceWorkers: 'block' });
      try {
        const page = await context.newPage();
        const evidence = await routeRepositoryFixtures(page, { root: fixtureRoot, files: fixtures });
        await page.addInitScript(() => {
          try { localStorage.clear(); } catch {}
          try { sessionStorage.clear(); } catch {}
        });

        for (const [id, file] of pages) {
          const url = `https://sjmaths.com/${file.replace(/index\.html$/, '')}`;
          const originalHtml = execFileSync('git', ['show', `${baseline}:${file}`], { cwd: ROOT, encoding: 'utf8', maxBuffer: 20e6 });
          const currentHtml = fs.readFileSync(path.join(fixtureRoot, file), 'utf8');
          assert.doesNotMatch(currentHtml, /data-up-assistant-tabs-runtime="shared"/);
          let activeHtml = originalHtml;
          await page.route(url, route => route.fulfill({ contentType: 'text/html', body: activeHtml }));
          const captures = [];

          for (const [kind, html] of [['baseline', originalHtml], ['deduplicated', currentHtml]]) {
            activeHtml = html;
            const errorStart = evidence.errors.length;
            const missingStart = evidence.missing.length;
            await page.goto(url, { waitUntil: 'load', timeout: 20000 });
            const overlay = page.locator('#sj-auth-overlay');
            await overlay.waitFor({ state: 'visible', timeout: 5000 }).catch(() => {});
            const skip = page.locator('#sj-skip-gate-btn');
            if (await overlay.isVisible().catch(() => false)) {
              await skip.click();
              await overlay.waitFor({ state: 'hidden' });
            }
            await page.evaluate(() => document.fonts.ready);
            const runtimeErrors = evidence.errors.slice(errorStart).filter(error => !error.startsWith('Service Worker registration failed'));
            const missing = evidence.missing.slice(missingStart);
            assert.deepEqual(runtimeErrors, [], `${id}/${kind} unexpected page errors`);
            assert.deepEqual(missing, [], `${id}/${kind} missing local requests`);
            assert.equal(await page.locator('script[src*="upsc-renderer"]').count(), 1, `${id} loads the shared renderer`);
            assert.equal(await page.locator('#upsc-page-data').count(), 1, `${id} has renderer page data`);

            const state = await page.evaluate(() => ({
              overflow: Math.max(0, document.documentElement.scrollWidth - innerWidth),
              h1: document.querySelector('h1')?.getBoundingClientRect().toJSON(),
              tabCount: document.querySelectorAll('.tab-btn').length,
              activeTabs: document.querySelectorAll('.tab-btn.active').length,
              content: document.querySelector('#topic-content')?.innerText.slice(0, 180),
            }));
            assert.ok(state.tabCount >= 2, `${id} tab controls exist`);
            assert.equal(state.activeTabs, 1, `${id}/${kind} one selected tab`);
            const screenshotPath = path.join(evidenceRoot, `${id}-${width}-${kind}.png`);
            await page.screenshot({ path: screenshotPath, animations: 'disabled' });
            const flow = [];

            if (width === 1280) {
              const tabs = page.locator('.tab-btn');
              for (let i = 0; i < await tabs.count(); i++) {
                const tab = tabs.nth(i);
                await tab.focus();
                await page.keyboard.press('Enter');
                assert.equal(await tab.getAttribute('aria-selected'), 'true', `${id} selected tab ${i}`);
                flow.push({
                  selected: await tab.getAttribute('data-tab'),
                  activeCount: await page.locator('.tab-btn.active').count(),
                  content: await page.locator('#topic-content').innerText(),
                });
              }
              const testTab = page.locator('.tab-btn[data-tab="tab-test"]');
              if (await testTab.count()) {
                await testTab.focus();
                await page.keyboard.press('Enter');
                const submit = page.locator('.btn-submit-test').first();
                if (await submit.count()) {
                  const radio = page.locator('.test-question-card input[type="radio"]').first();
                  if (await radio.count()) await radio.check();
                  await submit.click();
                  flow.push({ submitted: await page.locator('.mock-test-result').first().innerText(), button: await submit.innerText(), disabled: await submit.isDisabled() });
                }
              }
            }
            captures.push({ kind, screenshotPath, state, flow, errors: runtimeErrors, missing });
          }

          assert.deepEqual(captures[1].state, captures[0].state, `${id}/${width} layout and initial render parity`);
          assert.deepEqual(captures[1].errors, captures[0].errors);
          assert.deepEqual(captures[1].missing, captures[0].missing);
          if (width === 1280) assert.deepEqual(captures[1].flow, captures[0].flow, `${id} renderer-owned interactions parity`);
          const digest = filePath => crypto.createHash('sha256').update(fs.readFileSync(filePath)).digest('hex');
          assert.equal(digest(captures[1].screenshotPath), digest(captures[0].screenshotPath), `${id}/${width} screenshot parity`);
          results.push({ id, width, state: captures[1].state, flowVerified: width === 1280, screenshot: 'pixel-identical' });
        }
      } finally { await context.close(); }
    }
    fs.writeFileSync(path.join(evidenceRoot, 'results.json'), JSON.stringify({ fixtureRoot: path.relative(ROOT, fixtureRoot) || '.', baseline, results }, null, 2) + '\n');
  } finally { await browser.close(); }
});
