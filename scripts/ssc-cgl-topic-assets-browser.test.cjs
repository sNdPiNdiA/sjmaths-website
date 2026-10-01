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
const pages = [
  ['computer', 'ssc-cgl/computer-knowledge/backup-devices/index.html', '/ssc-cgl/computer-knowledge/backup-devices/'],
  ['english', 'ssc-cgl/english/active-and-passive-voice/active-and-passive-voice-narrations/index.html', '/ssc-cgl/english/active-and-passive-voice/active-and-passive-voice-narrations/'],
  ['finance', 'ssc-cgl/finance-economics/balance-sheet/index.html', '/ssc-cgl/finance-economics/balance-sheet/'],
  ['general-awareness', 'ssc-cgl/general-awareness/basic-science-awareness/biology-human-physiology-digestive-respiratory-circulatory/index.html', '/ssc-cgl/general-awareness/basic-science-awareness/biology-human-physiology-digestive-respiratory-circulatory/'],
  ['reasoning', 'ssc-cgl/reasoning/analytical-reasoning/index.html', '/ssc-cgl/reasoning/analytical-reasoning/'],
];
const fixtureRoot = path.resolve(ROOT, process.env.SJ_REFACTOR_FIXTURE_ROOT || '.');

test('SSC-CGL shared assets preserve cross-subject appearance, nav scroll and keyboard navigation', { timeout: 180000 }, async () => {
  const browser = await chromium.launch({ headless: true });
  const evidenceRoot = path.join(ROOT, 'scratch/refactor/ssc-cgl-topic-assets', path.basename(fixtureRoot));
  fs.mkdirSync(evidenceRoot, { recursive: true });
  const digest = file => crypto.createHash('sha256').update(fs.readFileSync(file)).digest('hex');
  const summaries = [];

  try {
    for (const [id, file, route] of pages) for (const width of [390, 1280]) {
      const originalHtml = execFileSync('git', ['show', `${baseline}:${file}`], { cwd: ROOT, encoding: 'utf8', maxBuffer: 20e6 });
      const externalHtml = fs.readFileSync(path.join(fixtureRoot, file), 'utf8');
      const migrated = externalHtml.includes('data-ssc-cgl-topic-style="shared"');
      const outcomes = [];

      for (const [kind, html] of [['inline', originalHtml], ['external', externalHtml]]) {
        const context = await browser.newContext({ viewport: { width, height: 900 }, reducedMotion: 'reduce' });
        try {
          const page = await context.newPage();
          const evidence = await routeRepositoryFixtures(page, { root: fixtureRoot, files: fixtureFiles(fixtureRoot) });
          await page.addInitScript(() => {
            localStorage.removeItem('ssc-cgl-prep-checklist');
          });
          await page.route(`https://sjmaths.com${route}`, request => request.fulfill({ contentType: 'text/html', body: html }));
          await page.goto(`https://sjmaths.com${route}`, { waitUntil: 'networkidle' });
          const skip = page.locator('#sj-skip-gate-btn');
          if (await page.locator('script[src*="require-auth"]').count()) await skip.waitFor({ state: 'visible', timeout: 15000 });
          if (await skip.isVisible()) await skip.click();
          await page.waitForTimeout(400);
          await page.evaluate(() => document.fonts.ready);
          await page.waitForTimeout(180);
          if (kind === 'external' && migrated) {
            const style = page.locator('link[data-ssc-cgl-topic-style="shared"]');
            assert.equal(await style.count(), 1);
            assert.match(await style.getAttribute('href'), /\/assets\/css\/ssc-cgl-topic(?:\.min)?\.css(?:\?|$)/);
            const runtime = page.locator('script[data-ssc-cgl-topic-runtime="shared"]');
            assert.equal(await runtime.count(), 1);
            assert.match(await runtime.getAttribute('src'), /\/assets\/js\/ssc-cgl-topic(?:\.min)?\.js(?:\?|$)/);
          }

          const navState = await page.locator('.subject-nav').evaluate(nav => {
            const active = nav.querySelector('.sub-nav-item.active');
            if (!active) return { activeFound: false };
            const outer = nav.getBoundingClientRect();
            const inner = active.getBoundingClientRect();
            return {
              activeFound: true,
              activeVisible: inner.left >= outer.left - 1 && inner.right <= outer.right + 1,
              activeText: active.textContent.trim(),
              scrollLeft: Math.round(nav.scrollLeft),
              checklistElements: document.querySelectorAll('.checklist-checkbox').length,
              overflow: Math.max(0, document.documentElement.scrollWidth - innerWidth),
            };
          });
          assert.equal(navState.activeFound, true, `${id}/${kind} active subject link exists`);
          const screenshotPath = path.join(evidenceRoot, `${id}-${width}-${kind}.png`);
          await page.screenshot({ path: screenshotPath, animations: 'disabled' });

          const link = page.locator('.sub-nav-item:not(.active)').first();
          const targetPath = new URL(await link.getAttribute('href'), 'https://sjmaths.com').pathname;
          await link.focus();
          await Promise.all([
            page.waitForURL(url => url.pathname === targetPath, { timeout: 15000 }),
            page.keyboard.press('Enter'),
          ]);
          outcomes.push({ kind, screenshotPath, navState, targetPath, errors: evidence.errors, missing: evidence.missing });
        } finally { await context.close(); }
      }

      assert.equal(outcomes[1].navState.overflow, outcomes[0].navState.overflow, `${id}/${width} overflow parity`);
      assert.equal(outcomes[1].navState.activeText, outcomes[0].navState.activeText, `${id}/${width} active nav parity`);
      assert.equal(outcomes[1].navState.activeVisible, outcomes[0].navState.activeVisible, `${id}/${width} active link visibility parity`);
      assert.equal(outcomes[1].navState.scrollLeft, outcomes[0].navState.scrollLeft, `${id}/${width} nav scroll parity`);
      assert.equal(outcomes[1].navState.checklistElements, outcomes[0].navState.checklistElements, `${id}/${width} checklist markup parity`);
      assert.equal(outcomes[1].targetPath, outcomes[0].targetPath, `${id}/${width} keyboard destination parity`);
      assert.deepEqual(outcomes[1].errors, outcomes[0].errors);
      assert.deepEqual(outcomes[1].missing, outcomes[0].missing);
      assert.equal(digest(outcomes[1].screenshotPath), digest(outcomes[0].screenshotPath), `${id}/${width} initial pixels`);
      summaries.push({ id, width, inline: { navState: outcomes[0].navState, targetPath: outcomes[0].targetPath }, external: { navState: outcomes[1].navState, targetPath: outcomes[1].targetPath } });
    }
    fs.writeFileSync(path.join(evidenceRoot, 'results.json'), JSON.stringify({ fixtureRoot: path.relative(ROOT, fixtureRoot) || '.', baseline, summaries }, null, 2) + '\n');
  } finally { await browser.close(); }
});
