const test = require('node:test');
const assert = require('node:assert/strict');
const path = require('node:path');
const fs = require('node:fs');
const { chromium } = require('playwright');
const { ROOT } = require('./seo-html.cjs');
const { fixtureFiles, routeRepositoryFixtures } = require('./lib/browser-fixture.cjs');

const pages = [
  ['class-9', 'class-9-maths/previous-syllabus/circles/index.html'],
  ['class-10', 'class-10-maths/chapter-wise-notes/chapter-2-polynomials/index.html'],
  ['class-11', 'class-11-maths/chapter-wise-notes/chapter-1-sets/index.html'],
  ['class-12', 'class-12-maths/chapter-wise-notes/chapter-13-probability/index.html'],
];
const fixtureRoot = path.resolve(ROOT, process.env.SJ_REFACTOR_FIXTURE_ROOT || '.');

test('chapter reader semantic dark tokens preserve light mode and avoid viewport overflow', { timeout: 120000 }, async t => {
  const browser = await chromium.launch({ headless: true });
  t.after(() => browser.close());

  for (const [grade, file] of pages) for (const width of [390, 1280]) {
    const context = await browser.newContext({ viewport: { width, height: 900 }, reducedMotion: 'reduce', serviceWorkers: 'block' });
    try {
      const page = await context.newPage();
      const evidence = await routeRepositoryFixtures(page, { root: fixtureRoot, files: fixtureFiles(fixtureRoot) });
      await page.route('**/assets/js/require-auth.min.js*', route => route.fulfill({ contentType: 'text/javascript', body: '' }));
      const failedResponses = [];
      page.on('response', response => {
        if (response.status() >= 400) failedResponses.push(`${response.status()} ${response.url()}`);
      });
      await page.goto(`https://sjmaths.com/${file}`, { waitUntil: 'load', timeout: 25000 });
      await page.waitForTimeout(1000);
      const errorsBeforeThemeSwitch = [...evidence.errors];
      await page.evaluate(() => window.SJMathsTheme.setPreference('light'));
      const light = await page.evaluate(() => ({
        theme: document.documentElement.dataset.theme,
        overflow: Math.max(0, document.documentElement.scrollWidth - innerWidth),
        slideBackground: getComputedStyle(document.body).getPropertyValue('--slide-bg').trim(),
        chapterHeading: document.querySelector('h1')?.textContent.trim(),
      }));
      assert.equal(light.theme, 'light', `${grade} remains in light mode`);
      assert.equal(light.overflow, 0, `${grade} light mode fits ${width}px`);
      assert.equal(light.slideBackground, '#ffffff', `${grade} light slide palette is unchanged`);
      assert.ok(light.chapterHeading, `${grade} chapter heading is present`);

      const toggle = page.locator('#notebookThemeToggle');
      await toggle.click();
      assert.equal(await toggle.getAttribute('aria-pressed'), 'true');
      assert.equal(await page.evaluate(() => localStorage.getItem('sjmaths.theme.preference')), 'dark');
      const dark = await page.evaluate(() => ({
        theme: document.documentElement.dataset.theme,
        overflow: Math.max(0, document.documentElement.scrollWidth - innerWidth),
        slideBackground: getComputedStyle(document.body).getPropertyValue('--slide-bg').trim(),
        noteSurface: getComputedStyle(document.body).getPropertyValue('--card-bg').trim(),
        slideText: getComputedStyle(document.body).getPropertyValue('--slide-text').trim(),
        pageColor: getComputedStyle(document.documentElement).getPropertyValue('--sj-color-page').trim(),
        noteCard: (() => {
          const card = document.querySelector('.sj-card, .note-section');
          if (!card) return null;
          const style = getComputedStyle(card);
          const rgb = value => value.match(/[\d.]+/g).slice(0, 3).map(Number).map(channel => channel / 255);
          const luminance = value => rgb(value).map(channel => channel <= 0.04045 ? channel / 12.92 : ((channel + 0.055) / 1.055) ** 2.4)
            .reduce((sum, channel, index) => sum + channel * [0.2126, 0.7152, 0.0722][index], 0);
          const background = style.backgroundColor;
          const color = style.color;
          const values = [luminance(background), luminance(color)].sort((a, b) => b - a);
          return { background, color, luminance: luminance(background), contrast: (values[0] + 0.05) / (values[1] + 0.05) };
        })(),
      }));
      assert.equal(dark.theme, 'dark');
      assert.equal(dark.overflow, 0, `${grade} dark mode fits ${width}px`);
      assert.equal(dark.slideBackground, '#182635', `${grade} uses shared semantic surface token`);
      assert.equal(dark.noteSurface, '#182635', `${grade} note cards use the shared semantic surface token`);
      assert.equal(dark.slideText, '#f1f5f9', `${grade} uses shared semantic ink token`);
      assert.equal(dark.pageColor, '#101a27');
      assert.ok(dark.noteCard, `${grade} renders a styled note card`);
      assert.ok(dark.noteCard.luminance < 0.25, `${grade} note card uses a dark surface`);
      assert.ok(dark.noteCard.contrast >= 4.5, `${grade} note-card text contrast is ${dark.noteCard.contrast}`);
      if (process.env.SJ_THEME_SCREENSHOTS) {
        const directory = path.join(ROOT, 'scratch', 'theme-screenshots', process.env.SJ_THEME_SCREENSHOTS);
        fs.mkdirSync(directory, { recursive: true });
        await page.screenshot({ path: path.join(directory, `${grade}-${width}-dark.png`) });
      }
      await toggle.focus();
      await page.keyboard.press('Enter');
      assert.equal(await page.locator('html').getAttribute('data-theme'), 'light', `${grade} keyboard toggle restores light mode`);
      assert.equal(await toggle.getAttribute('aria-pressed'), 'false');
      assert.deepEqual(evidence.missing, [], `${grade} has no missing local assets`);
      assert.deepEqual(failedResponses, [], `${grade} has no failed local requests`);
      await page.waitForTimeout(250);
      assert.deepEqual(evidence.errors, errorsBeforeThemeSwitch, `${grade} theme switch introduces no browser errors`);
    } finally {
      await context.close();
    }
  }
});
