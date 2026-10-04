const test = require('node:test');
const assert = require('node:assert/strict');
const { chromium } = require('playwright');
const path = require('node:path');
const http = require('node:http');
const { ROOT } = require('./seo-html.cjs');

async function createPage(t, browser, html) {
  const server = http.createServer((request, response) => {
    response.writeHead(200, { 'content-type': 'text/html; charset=utf-8' });
    response.end(html);
  });
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  t.after(() => new Promise(resolve => server.close(resolve)));
  const page = await browser.newPage();
  await page.goto(`http://127.0.0.1:${server.address().port}/`);
  return page;
}

test('shared theme controller migrates preferences, preserves palette state and updates compatibly', { timeout: 60000 }, async t => {
  const browser = await chromium.launch({ headless: true });
  t.after(() => browser.close());
  const page = await createPage(t, browser, '<!doctype html><html><head></head><body><button id="themeToggle" type="button"><i class="fa-moon"></i></button></body></html>');
  await page.emulateMedia({ colorScheme: 'light' });
  await page.evaluate(() => {
    localStorage.setItem('sjmaths-dark', 'off');
    localStorage.setItem('theme', 'dark');
    localStorage.setItem('sjmaths-theme', 'green');
  });
  await page.addScriptTag({ path: path.join(ROOT, 'assets/js/main.min.js') });

  assert.deepEqual(await page.evaluate(() => ({
    preference: window.SJMathsTheme.getPreference(),
    resolved: window.SJMathsTheme.getResolvedTheme(),
    dataTheme: document.documentElement.dataset.theme,
    preferenceAttribute: document.documentElement.dataset.themePreference,
    migrated: localStorage.getItem('sjmaths.theme.preference'),
    palette: localStorage.getItem('sjmaths-theme')
  })), {
    preference: 'light', resolved: 'light', dataTheme: 'light',
    preferenceAttribute: 'light', migrated: 'light', palette: 'green'
  });

  const events = await page.evaluate(() => {
    const received = [];
    window.addEventListener('sjmaths:themechange', event => received.push(event.detail));
    window.addEventListener('themeChanged', event => received.push({ legacy: event.detail.isDark }));
    window.setTheme('orange');
    const palette = localStorage.getItem('sjmaths-theme');
    window.setDarkMode(true);
    return { palette, preference: window.SJMathsTheme.getPreference(), theme: document.documentElement.dataset.theme, events: received };
  });
  assert.equal(events.palette, 'orange');
  assert.equal(events.preference, 'dark');
  assert.equal(events.theme, 'dark');
  assert.deepEqual(events.events.map(event => event.legacy ?? event.theme), ['dark', true]);

  await page.evaluate(() => document.dispatchEvent(new Event('DOMContentLoaded')));
  const toggle = page.locator('#themeToggle');
  assert.equal(await page.locator('#darkToggle').count(), 0, 'do not inject a second global toggle');
  assert.equal(await toggle.getAttribute('aria-pressed'), 'true');
  assert.equal(await toggle.getAttribute('aria-label'), 'Switch to light theme');
  await toggle.click();
  assert.equal(await page.locator('html').getAttribute('data-theme'), 'light');
  assert.equal(await toggle.getAttribute('aria-pressed'), 'false');

  await page.evaluate(() => window.dispatchEvent(new StorageEvent('storage', {
    key: 'sjmaths.theme.preference', newValue: 'dark'
  })));
  assert.equal(await page.locator('html').getAttribute('data-theme'), 'dark');
  await page.evaluate(() => window.SJMathsTheme.setPreference('system'));
  await page.emulateMedia({ colorScheme: 'dark' });
  await page.waitForFunction(() => document.documentElement.dataset.theme === 'dark');
  assert.equal(await page.locator('html').getAttribute('data-theme'), 'dark');
  assert.equal(await page.locator('html').getAttribute('data-theme-preference'), 'system');
  assert.equal(await page.evaluate(() => localStorage.getItem('sjmaths-dark')), 'on');
});

test('local chapter and test controls toggle exactly once alongside the shared controller', { timeout: 60000 }, async t => {
  const browser = await chromium.launch({ headless: true });
  t.after(() => browser.close());
  for (const [script, id] of [['chapter-common.js', 'theme-toggle'], ['test-dark-mode.js', 'testThemeToggle']]) {
    const page = await createPage(t, browser, `<!doctype html><html><head></head><body><button id="${id}" type="button"><i class="fa-moon"></i></button></body></html>`);
    await page.emulateMedia({ colorScheme: 'light' });
    await page.addScriptTag({ path: path.join(ROOT, 'assets/js/main.min.js') });
    await page.addScriptTag({ path: path.join(ROOT, 'assets/js', script) });
    await page.evaluate(() => document.dispatchEvent(new Event('DOMContentLoaded')));
    await page.locator(`#${id}`).click();
    assert.equal(await page.locator('html').getAttribute('data-theme'), 'dark', `${script}: one click changes theme once`);
    await page.locator(`#${id}`).focus();
    await page.keyboard.press('Enter');
    assert.equal(await page.locator('html').getAttribute('data-theme'), 'light', `${script}: keyboard toggles once`);
    await page.close();
  }
});

test('shared Art and Home Science topic controls keep dark mode separate from named palettes', { timeout: 60000 }, async t => {
  const browser = await chromium.launch({ headless: true });
  t.after(() => browser.close());
  const page = await createPage(t, browser, '<!doctype html><html><head></head><body><button id="btn-theme-toggle" type="button">🌙 रात्रि मोड</button></body></html>');
  await page.emulateMedia({ colorScheme: 'light' });
  await page.evaluate(() => localStorage.setItem('sjmaths-theme', 'green'));
  await page.addScriptTag({ path: path.join(ROOT, 'assets/js/topic-page.min.js') });
  await page.evaluate(() => document.dispatchEvent(new Event('DOMContentLoaded')));
  const toggle = page.locator('#btn-theme-toggle');
  assert.equal(await page.locator('html').getAttribute('data-theme'), 'light');
  await toggle.click();
  assert.equal(await page.locator('html').getAttribute('data-theme'), 'dark');
  assert.equal(await toggle.getAttribute('aria-pressed'), 'true');
  assert.equal(await page.evaluate(() => localStorage.getItem('sjmaths.theme.preference')), 'dark');
  assert.equal(await page.evaluate(() => localStorage.getItem('sjmaths-theme')), 'green');
  await toggle.focus();
  await page.keyboard.press('Enter');
  assert.equal(await page.locator('html').getAttribute('data-theme'), 'light');
  assert.equal(await toggle.getAttribute('aria-pressed'), 'false');
  assert.equal(await page.evaluate(() => localStorage.getItem('sjmaths-theme')), 'green');
});

test('theme controller adds one accessible fallback toggle only when the page has none', { timeout: 60000 }, async t => {
  const browser = await chromium.launch({ headless: true });
  t.after(() => browser.close());
  const page = await createPage(t, browser, '<!doctype html><html><head></head><body><main>Content</main></body></html>');
  await page.addScriptTag({ path: path.join(ROOT, 'assets/js/main.min.js') });
  await page.evaluate(() => document.dispatchEvent(new Event('DOMContentLoaded')));
  const toggle = page.locator('#darkToggle');
  assert.equal(await toggle.count(), 1);
  assert.equal(await toggle.getAttribute('type'), 'button');
  assert.match(await toggle.getAttribute('aria-label'), /^Switch to (light|dark) theme$/);
  await toggle.focus();
  await page.keyboard.press('Enter');
  assert.equal(await page.locator('html').getAttribute('data-theme'), 'dark');
});

test('shared design tokens resolve readable light and dark surfaces', { timeout: 60000 }, async t => {
  const browser = await chromium.launch({ headless: true });
  t.after(() => browser.close());
  const page = await createPage(t, browser, `<!doctype html><html data-theme="light"><head></head><body>
    <main id="preview"><p id="body-text">Study content</p><p id="muted-text">Supporting details</p><button id="focus-control">Continue</button></main>
    <style>#preview{background:var(--sj-color-surface);color:var(--sj-color-ink);border:1px solid var(--sj-color-border)}#muted-text{color:var(--sj-color-muted)}button:focus-visible{outline:3px solid color-mix(in srgb,var(--sj-color-focus) 72%,transparent);outline-offset:3px}</style>
  </body></html>`);
  await page.addStyleTag({ path: path.join(ROOT, 'assets/css/design-system.min.css') });

  const light = await page.evaluate(() => {
    const root = getComputedStyle(document.documentElement);
    const preview = getComputedStyle(document.querySelector('#preview'));
    return {
      page: root.getPropertyValue('--sj-color-page').trim(),
      background: preview.backgroundColor,
      color: preview.color,
      colorScheme: root.colorScheme
    };
  });
  assert.deepEqual(light, { page: '#eef3f3', background: 'rgb(255, 255, 255)', color: 'rgb(23, 32, 51)', colorScheme: 'normal' });

  await page.locator('html').evaluate(element => element.dataset.theme = 'dark');
  const dark = await page.evaluate(() => {
    const root = getComputedStyle(document.documentElement);
    const preview = getComputedStyle(document.querySelector('#preview'));
    const rgb = value => value.startsWith('#') ? value.slice(1).match(/../g).map(channel => parseInt(channel, 16)) : value.match(/[\d.]+/g).slice(0, 3).map(Number);
    const luminance = value => rgb(value).map(channel => channel / 255).map(channel => channel <= 0.04045 ? channel / 12.92 : ((channel + 0.055) / 1.055) ** 2.4).reduce((sum, channel, index) => sum + channel * [0.2126, 0.7152, 0.0722][index], 0);
    const contrast = (first, second) => { const values = [luminance(first), luminance(second)].sort((a, b) => b - a); return (values[0] + 0.05) / (values[1] + 0.05); };
    return {
      page: root.getPropertyValue('--sj-color-page').trim(),
      background: preview.backgroundColor,
      color: preview.color,
      muted: getComputedStyle(document.querySelector('#muted-text')).color,
      primary: root.getPropertyValue('--sj-color-primary').trim(),
      colorScheme: root.colorScheme,
      textContrast: contrast(preview.color, preview.backgroundColor),
      mutedContrast: contrast(getComputedStyle(document.querySelector('#muted-text')).color, root.getPropertyValue('--sj-color-page').trim()),
      primaryContrast: contrast(root.getPropertyValue('--sj-color-primary').trim(), preview.backgroundColor)
    };
  });
  assert.equal(dark.page, '#101a27');
  assert.equal(dark.background, 'rgb(24, 38, 53)');
  assert.equal(dark.color, 'rgb(241, 245, 249)');
  assert.equal(dark.colorScheme, 'dark');
  assert.ok(dark.textContrast >= 4.5, `body text contrast ${dark.textContrast}`);
  assert.ok(dark.mutedContrast >= 4.5, `muted text contrast ${dark.mutedContrast}`);
  assert.ok(dark.primaryContrast >= 4.5, `primary color contrast ${dark.primaryContrast}`);

  await page.locator('#focus-control').focus();
  assert.notEqual(await page.locator('#focus-control').evaluate(el => getComputedStyle(el).outlineStyle), 'none');
});
