const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { chromium } = require('playwright');
const { ROOT } = require('./seo-html.cjs');

const fixtureRoot = path.resolve(ROOT, process.env.SJ_REFACTOR_FIXTURE_ROOT || '.');
const pages = [
  'class-9-maths/chapter-wise-notes/chapter-9-triangles/index.html',
  'class-9-maths/chapter-wise-notes/chapter-10-herons-formula/index.html',
  'class-10-maths/chapter-wise-notes/chapter-1-real-numbers/index.html',
];

test('legacy Class 9 and 10 chapter pages follow the shared theme preference', { timeout: 120000 }, async t => {
  const browser = await chromium.launch({ headless: true });
  t.after(() => browser.close());
  for (const file of pages) for (const width of [390, 1280]) {
    const context = await browser.newContext({ viewport: { width, height: 900 }, reducedMotion: 'reduce' });
    try {
      const page = await context.newPage();
      const evidence = { missing: [], errors: [] };
      page.on('pageerror', error => evidence.errors.push(error.message));
      page.on('console', message => { if (message.type() === 'error') evidence.errors.push(message.text()); });
      await page.route('**/*', async route => {
        const url = new URL(route.request().url());
        if (!['sjmaths.local', 'sjmaths.com', 'www.sjmaths.com'].includes(url.hostname)) return route.continue();
        if (url.pathname.endsWith('/assets/js/require-auth.min.js')) {
          return route.fulfill({ contentType: 'text/javascript', body: '' });
        }
        const relative = decodeURIComponent(url.pathname).replace(/^\/+/, '') || 'index.html';
        let target = path.resolve(fixtureRoot, relative);
        if (target !== fixtureRoot && !target.startsWith(`${fixtureRoot}${path.sep}`)) {
          evidence.missing.push(url.pathname);
          return route.fulfill({ status: 400, body: 'Invalid fixture path' });
        }
        if (fs.existsSync(target) && fs.statSync(target).isDirectory()) target = path.join(target, 'index.html');
        if (!fs.existsSync(target) || !fs.statSync(target).isFile()) {
          evidence.missing.push(url.pathname);
          return route.fulfill({ status: 404, body: 'Fixture not found' });
        }
        const contentTypes = {
          '.html': 'text/html; charset=utf-8', '.js': 'text/javascript; charset=utf-8',
          '.css': 'text/css; charset=utf-8', '.json': 'application/json', '.svg': 'image/svg+xml',
          '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.webp': 'image/webp',
          '.ico': 'image/x-icon', '.woff': 'font/woff', '.woff2': 'font/woff2',
        };
        return route.fulfill({
          contentType: contentTypes[path.extname(target).toLowerCase()] || 'application/octet-stream',
          body: fs.readFileSync(target),
        });
      });
      await page.addInitScript(() => {
        localStorage.setItem('sjmaths.theme.preference', 'light');
        localStorage.setItem('theme', 'dark');
        localStorage.setItem('sjmaths-theme', 'green');
      });
      await page.goto(`http://sjmaths.local/${file}`, { waitUntil: 'domcontentloaded' });
      await page.waitForFunction(() => window.SJMathsTheme?.getPreference() === 'light');
      assert.equal(await page.locator('html').getAttribute('data-theme'), 'light', file);
      const result = await page.evaluate(() => {
        window.__chapterThemeChanges = 0;
        window.addEventListener('sjmaths:themechange', () => window.__chapterThemeChanges++);
        const accepted = window.SJMathsTheme.setPreference('dark');
        return {
          accepted,
          preference: localStorage.getItem('sjmaths.theme.preference'),
          theme: document.documentElement.dataset.theme,
          events: window.__chapterThemeChanges,
        };
      });
      assert.equal(result.accepted, true, `${file} preference accepted`);
      assert.equal(result.preference, 'dark', `${file} preference persisted immediately`);
      assert.equal(result.theme, 'dark', `${file} theme applied immediately`);
      await page.waitForFunction(() => window.__chapterThemeChanges === 1);
      assert.equal(await page.evaluate(() => window.__chapterThemeChanges), 1, `${file} emits one theme change`);
      assert.equal(await page.evaluate(() => localStorage.getItem('sjmaths-theme')), 'green', `${file} palette`);
      assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth), `${file} no horizontal overflow at ${width}px`);
      assert.deepEqual(evidence.missing, [], `${file} local asset requests resolve`);
      assert.deepEqual(evidence.errors, [], `${file} no browser errors`);
    } finally { await context.close(); }
  }
});
