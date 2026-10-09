const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { execFileSync } = require('node:child_process');
const { chromium } = require('playwright');
const cheerio = require('cheerio');
const root = path.resolve(__dirname, '..');
const chapters = fs.readdirSync(path.join(root, 'class-10-science')).filter(d => /^chapter-(9|10|11|12)-/.test(d));

test('Physics cleanup preserves questions, solutions, year tags and valid scripts', () => {
  for (const chapter of chapters) {
    const file = `class-10-science/${chapter}/index.html`;
    const before = cheerio.load(execFileSync('git', ['show', `HEAD:${file}`], { cwd: root, encoding: 'utf8' }));
    const after = cheerio.load(fs.readFileSync(path.join(root, file), 'utf8'));
    for (const selector of ['.pyq-card h3', '.pyq-card .question', '.pyq-card > p', '.question-card .question', '.question-card .answer', '.answer-toggle', '.pyq-opt']) {
      assert.deepEqual(after(selector).map((i, e) => after(e).text()).get(), before(selector).map((i, e) => before(e).text()).get(), `${chapter}: ${selector}`);
    }
    const years = dom => dom('.pyq-year,.pyq-tag').map((i, e) => (dom(e).text().match(/\d{4}/g) || []).join(',')).get();
    assert.deepEqual(years(after), years(before));
    const ids = after('[id]').map((i, e) => after(e).attr('id')).get();
    assert.equal(new Set(ids).size, ids.length, `${chapter}: duplicate IDs`);
    after('script:not([src]):not([type="application/ld+json"])').each((i, e) => new vm.Script(after(e).html(), { filename: file }));
    assert.doesNotMatch(after('.pyq-year,.pyq-tag').text(), /byju|cbseguidance|thestudypath|oswal\.io|diagnosticassessment|cbse\.online|educart|\bMTG\b/i);
  }
});

test('Physics pages and separate animation fixtures work on mobile and desktop', { timeout: 600000 }, async () => {
  const browser = await chromium.launch({ headless: true });
  try {
    for (const width of [390, 1280]) {
      const context = await browser.newContext({ viewport: { width, height: 900 }, reducedMotion: width === 390 ? 'reduce' : 'no-preference', serviceWorkers: 'block' });
      const page = await context.newPage();
      await page.route('https://sjmaths.com/**', async route => {
        const url = new URL(route.request().url());
        let file = path.join(root, decodeURIComponent(url.pathname));
        if (fs.existsSync(file) && fs.statSync(file).isDirectory()) file = path.join(file, 'index.html');
        if (!fs.existsSync(file)) return route.fulfill({ status: 404, body: url.pathname });
        const mime = { '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.svg': 'image/svg+xml' };
        await route.fulfill({ contentType: mime[path.extname(file)] || 'application/octet-stream', body: fs.readFileSync(file) });
      });
      for (const chapter of chapters) {
        const errors = [];
        const onError = e => errors.push(e.message);
        page.on('pageerror', onError);
        const url = `https://sjmaths.com/class-10-science/${chapter}/`;
        await page.goto(url + '#pyqs', { waitUntil: 'networkidle' });
        assert.equal(await page.locator('#tab-pyqs').evaluate(el => el.classList.contains('active')), true, `${chapter}: hash tab`);
        const topic = page.locator(".pyq-tab-btn[onclick*=\"'t1'\"]").first();
        await topic.click();
        await page.reload({ waitUntil: 'networkidle' });
        assert.equal(await page.locator('.pyq-tab-btn.active').count(), 1, `${chapter}: restored topic`);
        assert.notEqual(await page.locator('.pyq-tab-btn.active').textContent(), 'All Topics');
        const reveal = page.locator('#tab-pyqs .reveal-btn:visible').first();
        await reveal.click();
        assert.equal(await reveal.evaluate(btn => btn.nextElementSibling.classList.contains('show')), true);
        assert.equal(await reveal.evaluate(btn => btn.nextElementSibling.getBoundingClientRect().height > 0), true);
        await reveal.click();
        assert.equal(await reveal.evaluate(btn => btn.nextElementSibling.classList.contains('show')), false);
        const option = page.locator('#tab-pyqs .pyq-opt:visible').first();
        await option.click();
        assert.equal(await option.isDisabled(), true);
        for (const tab of ['concepts', 'ncert', 'revision', 'test', 'pyqs', 'concepts']) {
          await page.evaluate(name => openTab(name), tab);
          assert.equal(await page.locator('.tab-panel.active').count(), 1);
          assert.equal(await page.locator(`#tab-${tab}`).evaluate(el => el.classList.contains('active')), true);
          const navStates = await page.locator(`.nav-btn[onclick*="'${tab}'"]`).evaluateAll(buttons => buttons.every(btn => btn.classList.contains('active')));
          assert.equal(navStates, true, `${chapter}: navigation selection sync`);
          if (tab === 'ncert') {
            // Exercise every NCERT reveal handler, including in-text questions.
            // A class toggle alone is insufficient: the answer must be visible.
            const buttons = page.locator('#tab-ncert button[onclick*="toggle"]');
            assert.ok(await buttons.count() > 0, `${chapter}: NCERT answer buttons`);
            for (let i = 0; i < await buttons.count(); i++) {
              const button = buttons.nth(i);
              const answer = button.locator('xpath=following-sibling::*[1]');
              assert.equal(await answer.isVisible(), false, `${chapter}: NCERT ${i + 1} initially hidden`);
              await button.click();
              assert.equal(await answer.isVisible(), true, `${chapter}: NCERT ${i + 1} revealed`);
              assert.match(await button.textContent(), /hide/i);
              await button.click();
              assert.equal(await answer.isVisible(), false, `${chapter}: NCERT ${i + 1} hidden again`);
              assert.match(await button.textContent(), /show/i);
              // Rapid clicks must leave the answer in its original closed state.
              await button.evaluate(btn => { btn.click(); btn.click(); });
              assert.equal(await answer.isVisible(), false, `${chapter}: NCERT ${i + 1} rapid toggle`);
            }
          }
          await page.evaluate(() => Promise.all(document.getAnimations().map(animation => animation.finished.catch(() => {}))));
          const overflow = await page.evaluate(() => ({ width: document.documentElement.scrollWidth, elements: [...document.querySelectorAll('body *')].filter(el => el.getBoundingClientRect().right > innerWidth + 1 && el.getBoundingClientRect().width > 0 && !(() => { for(let p=el.parentElement;p&&p!==document.body;p=p.parentElement) if(["auto","scroll","hidden"].includes(getComputedStyle(p).overflowX)) return true; return false; })()).slice(0, 8).map(el => ({ tag: el.tagName, cls: el.className, parent: el.parentElement.className, parentWidth: getComputedStyle(el.parentElement).width, parentOverflow: getComputedStyle(el.parentElement).overflowX, text: el.textContent.slice(0, 80) })) }));
          assert.ok(overflow.width <= width + 1, `${chapter}: ${tab} overflow at ${width}: ${JSON.stringify(overflow)}`);
        }
        const scenes = await page.locator('[data-three-animation],[data-three-anim]').count();
        assert.equal(await page.locator('[data-three-animation] canvas,[data-three-anim] canvas').count(), scenes, `${chapter}: WebGL initialization`);
        await page.evaluate(() => { for (const action of ['reverse', 'toggle', 'toggle']) window.SJThree?.[action]('motor'); });
        await page.evaluate(() => openTab('test'));
        assert.ok(await page.locator('#test1 .option,#test1 .test-option').count() > 0);
        await page.locator('#test1 .option,#test1 .test-option').first().click();
        await page.evaluate(() => submitTest(1));
        assert.match(await page.locator('#result1,#score1').textContent(), /\d+\s*\/\s*\d+/);
        // The production HTML currently has no mounts. Exercise retained engines
        // in explicit fixtures without adding animations to educational content.
        const types = {
          '9': ['reflection-laws', 'concave-mirror', 'convex-mirror', 'glass-slab', 'convex-lens', 'concave-lens', 'power-comparison'],
          '10': ['eye-anatomy', 'accommodation', 'defects-correction', 'prism-dispersion', 'rainbow-drop', 'twinkling-star'],
          '11': ['current-flow', 'ohms-law', 'resistance-factors', 'series-parallel', 'heating-effect'],
          '12': ['magnetic-wire', 'solenoid', 'motor', 'generator']
        }[chapter.match(/^chapter-(\d+)/)[1]];
        await page.evaluate(({ types, circuit }) => {
          const fixture = document.createElement('section');
          fixture.id = 'animation-fixture';
          for (const type of types) {
            const mount = document.createElement('div');
            mount.setAttribute(circuit ? 'data-three-anim' : 'data-three-animation', type);
            mount.style.cssText = 'height:300px;width:100%;position:relative';
            fixture.appendChild(mount);
          }
          document.body.appendChild(fixture);
        }, { types, circuit: chapter.startsWith('chapter-11-') });
        await page.addScriptTag({ content: fs.readFileSync(path.join(root, 'class-10-science', chapter, 'three-animations.js'), 'utf8') });
        assert.equal(await page.locator('#animation-fixture canvas').count(), types.length, `${chapter}: fixture WebGL scenes`);
        await page.evaluate(() => {
          document.querySelector('#animation-fixture').scrollIntoView();
          for (const el of document.querySelectorAll('#animation-fixture [data-three-animation],#animation-fixture [data-three-anim]')) {
            const instance = el._opticsLabInstance || el._eyeOpticsInstance || el.__circuitSimulation;
            instance?.nextStep?.();
            instance?.prevStep?.();
            instance?.togglePlay?.();
          }
          window.SJThree?.reverse('motor');
          window.SJThree?.toggle('motor');
          dispatchEvent(new Event('resize'));
        });
        await page.evaluate(() => new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve))));
        await page.evaluate(() => { document.querySelector('#animation-fixture').style.display = 'none'; });
        await page.evaluate(() => new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve))));
        const stopped = await page.evaluate(() => [...document.querySelectorAll('#animation-fixture [data-three-animation],#animation-fixture [data-three-anim]')].every(el => {
          const instance = el._opticsLabInstance || el.__circuitSimulation;
          return !instance || !instance.rafId;
        }));
        assert.equal(stopped, true, `${chapter}: hidden fixture RAF stops`);
        assert.deepEqual(errors, [], `${chapter}: runtime errors`);
        page.off('pageerror', onError);
        console.log(`${chapter} ${width}px: tabs, persistence, answers, test scoring passed; ${scenes} animation mounts`);
      }
      await context.close();
    }
  } finally { await browser.close(); }
});
