const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { execFileSync } = require('node:child_process');
const cheerio = require('cheerio');
const { chromium } = require('playwright');
const { fixtureFiles, routeRepositoryFixtures } = require('./lib/browser-fixture.cjs');
const { createResolver } = require('./seo-routes.cjs');
const root = path.resolve(__dirname, '..');
const files = fixtureFiles(root);
const pages = files.filter(f => f.startsWith('class-11-physics/') && f.endsWith('.html'));
const trackedPages = new Set(execFileSync('git', ['ls-tree', '-r', '--name-only', 'HEAD', 'class-11-physics'], { cwd: root, encoding: 'utf8' }).trim().split(/\r?\n/));

test('Class 11 Physics preserves content, script syntax, IDs and local references', async () => {
  const { normalizePhysicsMath } = await import('./lib/class11-physics-math.mjs');
  const resolve = createResolver(files);
  for (const file of pages) {
    const html = fs.readFileSync(path.join(root, file), 'utf8');
    const $ = cheerio.load(html);
    const ids = new Set();
    $('[id]').each((_, e) => { const id = $(e).attr('id'); assert.ok(!ids.has(id), `${file}: duplicate ${id}`); ids.add(id); });
    $('script:not([src])').each((_, e) => {
      if ($(e).attr('type') === 'application/ld+json') JSON.parse($(e).html());
      else new vm.Script($(e).html(), { filename: file });
    });
    $('[href], [src]').each((_, e) => {
      const ref = $(e).attr('href') || $(e).attr('src');
      if (!ref || /^(mailto:|tel:|javascript:|data:)/.test(ref)) return;
      const url = new URL(ref, 'https://sjmaths.com/' + file);
      if (url.hostname !== 'sjmaths.com') return;
      const target = resolve(url.href);
      assert.ok(target.file || target.redirect, `${file}: missing ${ref}`);
      if (ref.startsWith('#') && ref.length > 1) assert.ok(ids.has(ref.slice(1)), `${file}: missing anchor ${ref}`);
    });
    if (!trackedPages.has(file)) continue;
    const baseline = cheerio.load(normalizePhysicsMath(execFileSync('git', ['show', `HEAD:${file}`], { cwd: root, encoding: 'utf8' })));
    if (file === 'class-11-physics/index.html') {
      // Chapter 8 activation is intentional; every other hub card is preserved.
      baseline('[data-keywords^="Mechanical Properties of Solids"]').remove();
      $('[data-keywords^="Mechanical Properties of Solids"]').remove();
    }
    baseline('script').remove(); $('script').remove();
    assert.equal($('body').html(), baseline('body').html(), `${file}: student content changed`);
  }
});

test('Physics chapters handle rapid navigation, grading, responsive layouts and WebGL lifecycle', { timeout: 240000 }, async () => {
  const browser = await chromium.launch({ headless: true });
  try {
    for (const file of pages) {
      const context = await browser.newContext({ viewport: { width: 390, height: 844 }, reducedMotion: 'reduce' });
      try {
        const page = await context.newPage();
        const evidence = await routeRepositoryFixtures(page, { root, files });
        // Auth/ads are excluded: this test makes no sign-in or production claim.
        await page.route('**/assets/js/require-auth*.js*', r => r.fulfill({ contentType: 'text/javascript', body: '' }));
        await page.addInitScript(() => {
          window.physicsRenders = 0;
          window.physicsDisposals = 0;
          document.addEventListener('load', e => {
            if (e.target.tagName !== 'SCRIPT' || !e.target.src.includes('/three.min.js')) return;
            const Renderer = THREE.WebGLRenderer;
            THREE.WebGLRenderer = class extends Renderer {
              constructor(...args) {
                super(...args);
                const render = this.render;
                this.render = (...args) => { window.physicsRenders++; return render.apply(this, args); };
                const dispose = this.dispose;
                this.dispose = (...args) => { window.physicsDisposals++; return dispose.apply(this, args); };
              }
            };
          }, true);
        });
        await page.goto('https://sjmaths.com/' + file, { waitUntil: 'networkidle', timeout: 90000 });
        if (!file.includes('/chapter-')) {
          await page.locator('#chapter-search').fill('gravitation');
          assert.equal(await page.locator('.chapter-box:visible').count(), 1);
          await page.locator('#chapter-search').fill('zzzz-no-chapter');
          assert.equal(await page.locator('.chapter-box:visible').count(), 0);
          assert.equal(await page.locator('#no-results-alert').isVisible(), true);
          await page.locator('#chapter-search').fill('');
        } else {
          for (const width of [390, 768, 1280]) {
            await page.setViewportSize({ width, height: 844 });
            for (const tab of ['learn', 'quiz', 'exercise', 'revision', 'tests']) {
              await page.evaluate(tab => switchTab(tab), tab);
              await page.waitForTimeout(120);
              const overflow = await page.evaluate(() => document.documentElement.scrollWidth - innerWidth);
              const wide = overflow > 1 ? await page.evaluate(() => [...document.querySelectorAll('.tab.active table, .tab.active .katex, .tab.active div')].filter(e => e.getBoundingClientRect().right > innerWidth + 2 && !e.closest('.table-container,.math-box')).sort((a,b)=>b.getBoundingClientRect().right-a.getBoundingClientRect().right).slice(0,8).map(e => ({ tag:e.tagName,cls:e.className, width:e.getBoundingClientRect().width, parent:e.parentElement.className, text:e.textContent.slice(0,100) }))) : [];
              assert.ok(overflow <= 1, `${file}: ${tab} overflow ${overflow}px at ${width}px ${JSON.stringify(wide)}`);
            }
          }
          const scrollCalls = await page.evaluate(async () => {
            if (typeof openLearnSec !== 'function') return 0;
            let calls = 0;
            const original = Element.prototype.scrollIntoView;
            Element.prototype.scrollIntoView = function() { calls++; };
            openLearnSec(document.querySelector('#learn [id]').id);
            switchTab('quiz');
            await new Promise(r => setTimeout(r, 150));
            Element.prototype.scrollIntoView = original;
            return calls;
          });
          assert.equal(scrollCalls, 0, `${file}: stale Learn scroll`);
          await page.evaluate(() => switchTab('quiz'));
          const quiz = page.locator('.mcq-card').first();
          await quiz.locator('.mcq-option-btn').first().click();
          assert.equal(await quiz.getAttribute('data-answered'), 'true');
          assert.ok(await quiz.locator('.mcq-option-btn:disabled').count() > 0);
          await page.evaluate(() => switchTab('tests'));
          const answer = page.locator('#testLevel0 .mcq-option-btn').first();
          await answer.click();
          await page.evaluate(() => submitActiveTest());
          assert.equal(await page.locator('#testResultBox').isVisible(), true);
          await answer.click();
          assert.equal(await page.locator('#testResultBox').isVisible(), false);
          assert.equal(await page.locator('#testLevel0 .correct, #testLevel0 .wrong').count(), 0);
          await page.evaluate(() => resetActiveTest());
          assert.equal(await page.locator('#testLevel0 [data-selected]').count(), 0);
          if (await page.locator('canvas').count()) {
            await page.evaluate(() => switchTab('learn'));
            const canvas = page.locator('canvas').first();
            await canvas.scrollIntoViewIfNeeded();
            // Font/layout and intersection observers can request one-off redraws after scrolling.
            // Allow them to settle before checking for a continuing animation loop.
            await page.waitForTimeout(500);
            const stopped = await page.evaluate(() => physicsRenders);
            await page.waitForTimeout(500);
            assert.equal(await page.evaluate(() => physicsRenders), stopped, `${file}: reduced motion RAF keeps running`);
            const slider = page.locator('.sim-3d-card').first().locator('input[type=range]').first();
            if (await slider.count()) {
              await slider.evaluate(el => { el.value = el.max; el.dispatchEvent(new Event('input', { bubbles: true })); });
              await page.waitForTimeout(100);
            assert.ok(await page.evaluate(() => physicsRenders) > stopped, `${file}: reduced motion slider did not redraw ${JSON.stringify(await page.evaluate(() => ({renders:physicsRenders,top:document.querySelector('canvas').getBoundingClientRect().top,bottom:document.querySelector('canvas').getBoundingClientRect().bottom,height:innerHeight,card:document.querySelector('canvas').closest('.sim-3d-card')?.className})))}, before=${stopped}`);
            }
            await page.emulateMedia({ reducedMotion: 'no-preference' });
            await page.waitForTimeout(100);
            const running = await page.evaluate(() => physicsRenders);
            await page.waitForTimeout(100);
            assert.ok(await page.evaluate(() => physicsRenders) > running, `${file}: animation did not resume`);
            await page.evaluate(() => switchTab('quiz'));
            await page.waitForTimeout(100);
            const hidden = await page.evaluate(() => physicsRenders);
            await page.waitForTimeout(100);
            assert.equal(await page.evaluate(() => physicsRenders), hidden, `${file}: hidden tab keeps rendering`);
            await page.evaluate(() => window.dispatchEvent(new PageTransitionEvent('pagehide', { persisted: true })));
            const paused = await page.evaluate(() => physicsDisposals);
            assert.equal(paused, 0, `${file}: bfcache destroyed canvases`);
            await page.evaluate(() => window.dispatchEvent(new PageTransitionEvent('pageshow', { persisted: true })));
            await page.evaluate(() => window.dispatchEvent(new PageTransitionEvent('pagehide', { persisted: false })));
            assert.equal(await page.evaluate(() => physicsDisposals), 4, `${file}: renderers not disposed`);
            assert.equal(await page.locator('canvas').count(), 0);
          }
        }
        assert.deepEqual(evidence.errors, [], `${file}: console/page errors`);
        assert.deepEqual(evidence.missing, [], `${file}: missing assets`);
      } finally { await context.close(); }
    }
  } finally { await browser.close(); }
});
