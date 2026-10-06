const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const cheerio = require('cheerio');
const { chromium } = require('playwright');
const { fixtureFiles, routeRepositoryFixtures } = require('./lib/browser-fixture.cjs');

const root = path.resolve(__dirname, '..');
const route = '/class-11-physics/chapter-10-thermal-properties-of-matter/';
const file = path.join(root, route, 'index.html');
const html = fs.readFileSync(file, 'utf8');
const $ = cheerio.load(html);
const close = (actual, expected, tolerance = 0.015) => assert.ok(Math.abs(actual - expected) <= Math.abs(expected) * tolerance, `${actual} differs from ${expected}`);

test('Chapter 10 keeps the supplied concept sequence and places all eight worked examples with their topics', () => {
  assert.equal($('h1').length, 1);
  assert.equal($('.tab').length, 5);
  assert.equal($('#learn [data-concept]').length, 12);
  assert.deepEqual($('[data-example^="NCERT Example"]').map((_, el) => $(el).attr('data-example').match(/10\.\d/)[0]).get().sort(), ['10.1','10.2','10.3','10.4','10.5','10.6','10.7','10.8']);
  assert.equal($('[data-example="NCERT Example 10.3 · Solved"]').closest('[data-concept]').attr('data-concept'), 'sec-10-7');
  assert.equal($('[data-example="NCERT Example 10.4 · Solved"]').closest('[data-concept]').attr('data-concept'), 'sec-10-8');
  for (const id of ['sec-10-4','sec-10-5','sec-10-6','sec-10-7','sec-10-8','sec-10-8-pressure','sec-10-9','sec-10-9-radiation','sec-10-10']) assert.ok($('#' + id).length, `missing concept ${id}`);
  for (const phrase of ['β≈2α','γ≈3α','γ=1/T','Yα|ΔT|','Wien','Stefan','Newton','triple point','regelation','convection','blackbody']) assert.ok($('#learn').text().toLowerCase().includes(phrase.toLowerCase()), `missing ${phrase}`);
});

test('All 20 NCERT exercise prompts, solutions and concept links remain present', () => {
  const cards = $('#exercise [data-exercise]');
  assert.equal(cards.length, 20);
  for (let n = 1; n <= 20; n++) {
    const card = $('[data-exercise="10.' + n + '"]');
    assert.equal(card.length, 1, `missing Exercise 10.${n}`);
    assert.ok(card.find('.ex-question').text().length > 70, `Exercise 10.${n} prompt is incomplete`);
    assert.ok(card.find('.step-item').length >= 2, `Exercise 10.${n} solution is incomplete`);
    const target = card.find('.ex-prereq a').attr('href');
    assert.ok(target && $(target).length, `Exercise 10.${n} concept link is broken`);
    assert.equal(card.find('.sol-toggle-btn').attr('aria-expanded'), 'false');
    assert.ok($('#' + card.find('.sol-toggle-btn').attr('aria-controls')).length);
  }
  assert.match($('[data-exercise="10.19"] .ex-question').text(), /optical pyrometer/i);
  assert.match($('[data-exercise="10.20"] .ex-question').text(), /surroundings is 20 °C/i);
});

test('Quiz and revision cover every concept and every answer is structurally valid', () => {
  assert.equal($('#quiz .mcq-card').length, 36);
  assert.equal($('#quiz .quiz-topic-group').length, 12);
  $('#quiz .quiz-topic-group').each((_, group) => {
    assert.equal($(group).find('.mcq-card').length, 3);
    assert.ok($(group).find('.quiz-topic-heading a').attr('href'));
  });
  $('#quiz .mcq-card').each((_, card) => {
    const options = $(card).find('.mcq-option-btn');
    assert.equal(options.length, 4);
    assert.equal(options.filter('[data-correct="true"]').length, 1);
  });
  assert.equal($('#revision .rev-card').length, 12);
  $('#revision .rev-card').each((_, card) => assert.equal($(card).find('li').length, 3));
});

test('Interactive models, SVG fallbacks, internal links, hashes and discovery entries are valid', () => {
  assert.equal($('.thermal-sim-card').length, 4);
  assert.equal($('.thermal-sim-fallback').length, 4);
  assert.equal($('#learn svg').length >= 6, true);
  assert.equal($('.thermal-sim-card .thermal-play').length, 4);
  assert.equal($('.solved-example .example-solution-box:not(.open)').length, 9);
  const ids = new Set();
  $('[id]').each((_, el) => { const id = $(el).attr('id'); assert.ok(!ids.has(id), 'duplicate ID ' + id); ids.add(id); });
  $('[href^="#"]').each((_, el) => assert.ok(ids.has($(el).attr('href').slice(1)), 'broken anchor ' + $(el).attr('href')));
  const hub = cheerio.load(fs.readFileSync(path.join(root, 'class-11-physics/index.html'), 'utf8'));
  assert.equal(hub('[data-keywords^="Thermal Properties of Matter"] .tag-active').length, 1);
  assert.equal(hub('a[href="chapter-10-thermal-properties-of-matter/"]').length, 1);
  const index = JSON.parse(fs.readFileSync(path.join(root, 'assets/js/search-index.json'), 'utf8'));
  assert.equal(index.filter(item => item.url === route).length, 1);
  const sitemap = fs.readFileSync(path.join(root, 'sitemap-class-11.xml'), 'utf8');
  assert.equal(sitemap.split('https://sjmaths.com' + route).length - 1, 1);
  for (const [selector, asset, attr] of [
    ['link[href*="class11-physics-thermal.min"]', 'assets/css/class11-physics-thermal.min.css', 'href'],
    ['script[src*="class11-thermal-three.min"]', 'assets/js/class11-thermal-three.min.js', 'src']
  ]) {
    const expected = crypto.createHash('sha256').update(fs.readFileSync(path.join(root, asset))).digest('hex').slice(0, 8);
    assert.ok($(selector).attr(attr).endsWith(expected), `${asset} cache hash is stale`);
  }
});

test('Representative worked answers and physics relationships recalculate', () => {
  close(27 + (5.243 / 5.231 - 1) / 1.2e-5, 218.4, 0.005);
  close((0.25 * 4180 + 0.14 * 386) * 3 / (0.047 * 77), 911, 0.01);
  close((0.30 * 4186 * (50 - 6.7) - 0.15 * 4186 * 6.7) / 0.15, 3.34e5, 0.01);
  close(3 * 2100 * 12 + 3 * 3.35e5 + 3 * 4186 * 100 + 3 * 2.256e6, 9.1e6, 0.01);
  close((2 * 50.2 * 300 / 0.15) / (2 * 50.2 / 0.15 + 385 / 0.1), 44.4, 0.01);
  close((79 * 373 + 109 * 273) / 188, 315, 0.005);
  close(2 * 79 * 109 / 188, 91.6, 0.005);
  close(91.6 * 0.02 * 100 / 0.2, 916, 0.005);
  close(0.047, (0.25 * 4180 + 0.14 * 386) * 3 / (911 * 77), 0.01);
  close(6 * 25 / 45, 3.333, 0.002);
});

test('Chapter 10 works in browser across tabs, filters, solutions, scoring and screen widths', { timeout: 90000 }, async () => {
  const browser = await chromium.launch({ headless: true, args: ['--enable-webgl', '--use-gl=angle', '--use-angle=swiftshader'] });
  const files = fixtureFiles(root);
  const context = await browser.newContext({ viewport: { width: 390, height: 844 }, reducedMotion: 'reduce' });
  try {
    const page = await context.newPage();
    const evidence = await routeRepositoryFixtures(page, { root, files });
    await page.route('**/assets/js/require-auth*.js*', route => route.fulfill({ contentType: 'text/javascript', body: '' }));
    await page.addInitScript(() => {
      window.thermalRenders = 0;
      window.thermalDisposals = 0;
      document.addEventListener('load', event => {
        if (event.target.tagName !== 'SCRIPT' || !event.target.src.includes('/three.min.js') || !window.THREE) return;
        const Renderer = window.THREE.WebGLRenderer;
        window.THREE.WebGLRenderer = class extends Renderer {
          constructor(...args) {
            super(...args);
            const render = this.render.bind(this);
            this.render = (...args) => { window.thermalRenders++; return render(...args); };
            const dispose = this.dispose.bind(this);
            this.dispose = (...args) => { window.thermalDisposals++; return dispose(...args); };
          }
        };
      }, true);
    });
    await page.goto('https://sjmaths.com' + route, { waitUntil: 'domcontentloaded', timeout: 30000 });

    const exampleToggle = page.locator('.solved-example .sol-toggle-btn').first();
    assert.equal(await exampleToggle.getAttribute('aria-expanded'), 'false');
    await exampleToggle.click();
    assert.equal(await exampleToggle.getAttribute('aria-expanded'), 'true');
    await exampleToggle.click();
    assert.equal(await exampleToggle.getAttribute('aria-expanded'), 'false');

    await page.locator('.nav-btn[data-tab="quiz"]').click();
    await page.locator('#quiz .mcq-card').first().locator('[data-correct="true"]').click();
    assert.match(await page.locator('#quizProgressCount').textContent(), /1 \/ 36 Answered/);
    assert.equal(await page.locator('#quiz .mcq-card').first().locator('.opt-explanation.show').count(), 1);

    await page.locator('.nav-btn[data-tab="exercise"]').click();
    const firstExercise = page.locator('[data-exercise="10.1"] .sol-toggle-btn');
    await firstExercise.click();
    assert.equal(await firstExercise.getAttribute('aria-expanded'), 'true');
    await page.locator('.exercise-filter .chip').filter({ hasText: 'Temperature' }).click();
    assert.equal(await page.locator('#exercise .exercise-card:visible').count(), 5);
    await page.locator('.exercise-filter .chip').filter({ hasText: 'Expansion' }).click();
    assert.equal(await page.locator('#exercise .exercise-card:visible').count(), 6);

    await page.locator('.nav-btn[data-tab="revision"]').click();
    assert.equal(await page.locator('#revision .rev-card').count(), 12);
    await page.locator('.nav-btn[data-tab="tests"]').click();
    const testPanel = page.locator('#testLevel0');
    for (const card of await testPanel.locator('.test-card').all()) {
      const answer = await card.getAttribute('data-ans');
      await card.locator('[data-idx="' + answer + '"]').click();
    }
    await page.getByRole('button', { name: 'Submit Test' }).click();
    assert.match(await page.locator('#testResultBox').textContent(), /5 \/ 5/);

    for (const width of [390, 768, 1280]) {
      await page.setViewportSize({ width, height: 844 });
      await page.waitForTimeout(120);
      assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth), `horizontal overflow at ${width}px`);
    }

    await page.locator('.nav-btn[data-tab="learn"]').click();
    await page.locator('#thermal-lab').scrollIntoViewIfNeeded();
    await page.waitForTimeout(900);
    const canvasCount = await page.locator('.thermal-sim-card canvas').count();
    assert.equal(canvasCount, 4, 'software WebGL should initialise all four thermal models');
    {
      const slider = page.locator('.thermal-sim-card').first().locator('input[type="range"]');
      await slider.evaluate(el => { el.value = el.max; el.dispatchEvent(new Event('input', { bubbles: true })); });
      await page.waitForTimeout(80);
      assert.ok(await page.evaluate(() => thermalRenders) > 0, 'range control did not redraw Three.js model');
      assert.equal(await page.locator('.thermal-sim-card [data-thermal-play]').first().isDisabled(), true, 'reduced motion must disable continuous animation');
      await page.emulateMedia({ reducedMotion: 'no-preference' });
      const play = page.locator('.thermal-sim-card [data-thermal-play]').first();
      assert.equal(await play.isDisabled(), false);
      await play.click();
      const started = await page.evaluate(() => thermalRenders);
      await page.waitForTimeout(120);
      assert.ok(await page.evaluate(() => thermalRenders) > started, 'Play did not animate the model');
      await play.click();
      const paused = await page.evaluate(() => thermalRenders);
      await page.waitForTimeout(150);
      assert.equal(await page.evaluate(() => thermalRenders), paused, 'paused model kept rendering');
      await play.click();
      await page.locator('.nav-btn[data-tab="quiz"]').click();
      const hiddenTab = await page.evaluate(() => thermalRenders);
      await page.waitForTimeout(150);
      assert.equal(await page.evaluate(() => thermalRenders), hiddenTab, 'model kept animating while Learn was hidden');
      await page.evaluate(() => window.dispatchEvent(new PageTransitionEvent('pagehide', { persisted: false })));
      assert.equal(await page.evaluate(() => thermalDisposals), 4, 'all four initialized renderers should be disposed');
    }
    assert.deepEqual(evidence.errors, []);
    assert.deepEqual(evidence.missing, []);
  } finally {
    await context.close();
    await browser.close();
  }
});
