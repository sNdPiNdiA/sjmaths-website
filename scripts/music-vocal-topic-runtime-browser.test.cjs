const test = require('node:test');
const assert = require('node:assert/strict');
const crypto = require('node:crypto');
const fs = require('node:fs');
const path = require('node:path');
const { chromium } = require('playwright');
const { ROOT } = require('./seo-html.cjs');
const { fixtureFiles, routeRepositoryFixtures } = require('./lib/browser-fixture.cjs');

test('Music Vocal shared style and runtime preserve rendering, four-tab quiz and timed-test flows', { timeout: 150000 }, async () => {
  const file = 'music-vocal/acoustics/resonance/index.html';
  const fixtureRoot = path.resolve(ROOT, process.env.SJ_REFACTOR_FIXTURE_ROOT || '.');
  const files = fixtureFiles(fixtureRoot);
  const { hydrateMusicVocalTopicRuntime } = await import('./lib/music-vocal-runtime.mjs');
  const { hydrateMusicVocalStyles } = await import('./lib/music-vocal-styles.mjs');
  let externalHtml = fs.readFileSync(path.join(fixtureRoot, file), 'utf8');
  if (process.env.SJ_MUSIC_RENDERER_FIXTURE === '1') {
    const { compileMusicVocalHtml } = await import('./lib/music-vocal-renderer.mjs');
    const { musicVocalRendererFixture } = await import('./lib/music-vocal-renderer-fixture.mjs');
    const { musicVocalTopicScript } = await import('./lib/music-vocal-runtime.mjs');
    const { musicVocalTopicStyleLink } = await import('./lib/music-vocal-styles.mjs');
    const { content, questions, context } = musicVocalRendererFixture();
    externalHtml = compileMusicVocalHtml(content, questions, context, { musicVocalTopicScript, musicVocalTopicStyleLink });
  }
  const inlineHtml = hydrateMusicVocalStyles(hydrateMusicVocalTopicRuntime(externalHtml));
  assert.notEqual(inlineHtml, externalHtml, 'fixture must exercise shared-script hydration');
  assert.match(externalHtml, /data-music-vocal-topic-style="topic"/);
  assert.doesNotMatch(inlineHtml, /data-music-vocal-topic-style="topic"/);
  const evidenceRoot = path.join(ROOT, 'scratch/refactor', process.env.SJ_MUSIC_RENDERER_FIXTURE === '1' ? 'music-vocal-renderer' : 'music-vocal-styles', path.basename(fixtureRoot));
  fs.mkdirSync(evidenceRoot, { recursive: true });
  const summaries = [];
  const browser = await chromium.launch({ headless: true });
  try {
    for (const width of [390, 1280]) {
      const outcomes = [];
      for (const [kind, html] of [['inline', inlineHtml], ['external', externalHtml]]) {
        const context = await browser.newContext({ viewport: { width, height: 900 }, reducedMotion: 'reduce', serviceWorkers: 'block' });
        try {
          const page = await context.newPage();
          const evidence = await routeRepositoryFixtures(page, { root: fixtureRoot, files });
          await page.route('https://sjmaths.com/music-vocal/acoustics/resonance/', route => route.fulfill({ contentType: 'text/html', body: html }));
          await page.clock.install();
          await page.goto('https://sjmaths.com/music-vocal/acoustics/resonance/');
          await page.evaluate(() => document.fonts.ready);
          const tabs = page.locator('.tab');
          assert.equal(await tabs.count(), 4);
          const panelText = [];
          const screenshots = [];
          for (const tab of await tabs.all()) {
            await tab.focus();
            await page.keyboard.press('Enter');
            assert.equal(await tab.getAttribute('class').then(value => value.includes('active')), true);
            const id = await tab.getAttribute('data-tab');
            assert.equal(await page.locator(`#${id}`).isVisible(), true);
            panelText.push((await page.locator(`#${id}`).innerText()).slice(0, 300));
            const image = await page.screenshot({ path: path.join(evidenceRoot, `${width}-${kind}-${id}.png`), animations: 'disabled' });
            screenshots.push(crypto.createHash('sha256').update(image).digest('hex'));
          }

          await tabs.nth(1).click();
          const mcq = page.locator('[data-quiz]').first();
          const mcqCard = mcq.locator('xpath=ancestor::*[contains(@class,"question")][1]');
          await mcq.click();
          assert.equal(await mcq.isDisabled(), true);
          assert.ok(await mcqCard.innerText().then(text => text.includes('सही') || text.includes('पुनः देखें')));

          const fillButton = page.locator('[data-fill]').first();
          const fillCard = fillButton.locator('xpath=ancestor::*[contains(@class,"question")][1]');
          const fillIndex = await fillCard.getAttribute('data-index');
          const accepted = (await fillCard.locator('.accepted-answer').first().innerText()).trim();
          await page.locator(`#quiz-input-${fillIndex}`).fill(accepted);
          await fillButton.click();
          assert.ok(await fillCard.innerText().then(text => text.includes('स्वीकृत उत्तर')));

          const shortButton = page.locator('[data-short]').first();
          const shortCard = shortButton.locator('xpath=ancestor::*[contains(@class,"question")][1]');
          await shortButton.click();
          assert.ok(await shortCard.innerText().then(text => text.includes('अपेक्षित उत्तर')));

          await tabs.nth(3).click();
          await page.locator('[data-test]').first().click();
          await page.locator('#submit-test').click();
          const manualResult = await page.locator('#test-result').innerText();
          assert.match(manualResult, /आपका परिणाम: \d+ \/ 10/);
          assert.equal(await page.locator('[data-test]').first().isDisabled(), true);

          await page.reload();
          await page.locator('.tab[data-tab="test"]').click();
          await page.clock.runFor(600000);
          const timedResult = await page.locator('#test-result').innerText();
          assert.equal(timedResult, 'आपका परिणाम: 0 / 10');

          assert.equal(await page.evaluate(() => Math.max(0, document.documentElement.scrollWidth - innerWidth)), 0, `${width}px overflow`);
          assert.deepEqual(evidence.missing, []);
          if (process.env.SJ_MUSIC_RENDERER_FIXTURE === '1') assert.deepEqual(evidence.errors, [], 'offline renderer fixture must have no runtime errors');
          outcomes.push({ panelText, screenshots, manualResult, timedResult, errors: evidence.errors });
        } finally { await context.close(); }
      }
      assert.deepEqual(outcomes[1], outcomes[0], `${width}px inline/external parity`);
      summaries.push({ width, screenshots: 'pixel-identical across all four tabs', manualResult: outcomes[1].manualResult, timedResult: outcomes[1].timedResult, errors: outcomes[1].errors });
    }
    fs.writeFileSync(path.join(evidenceRoot, 'results.json'), JSON.stringify({ fixtureRoot, summaries }, null, 2) + '\n');
  } finally { await browser.close(); }
});
