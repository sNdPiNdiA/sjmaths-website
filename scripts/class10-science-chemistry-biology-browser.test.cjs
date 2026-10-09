const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { execFileSync } = require('node:child_process');
const { chromium } = require('playwright');
const cheerio = require('cheerio');
const root = path.resolve(__dirname, '..');
const chapters = fs.readdirSync(path.join(root, 'class-10-science')).filter(d => /^chapter-([1-8]|13)-/.test(d));

test('Chemistry and Biology retain questions, answers, year tags and valid references', () => {
  for (const chapter of chapters) {
    const file = `class-10-science/${chapter}/index.html`;
    const original = cheerio.load(execFileSync('git', ['show', `HEAD:${file}`], { cwd: root, encoding: 'utf8' }));
    const dom = cheerio.load(fs.readFileSync(path.join(root, file), 'utf8'));
    for (const selector of ['.pyq-card h3', '.question-card h3', '.answer-toggle', '.answer', '.ans', '.question-a', '.q h3', '.test-question h3', '.pyq-opt', '.pyq-year', '.pyq-tag', '.year']) {
      assert.deepEqual(dom(selector).map((i, e) => dom(e).text()).get(), original(selector).map((i, e) => original(e).text()).get(), `${chapter}: ${selector}`);
    }
    const ids = dom('[id]').map((i, e) => dom(e).attr('id')).get();
    assert.equal(new Set(ids).size, ids.length, `${chapter}: duplicate IDs`);
    dom('script:not([src]):not([type="application/ld+json"])').each((i, e) => new vm.Script(dom(e).html(), { filename: file }));
    dom('script[src],link[href],img[src]').each((i, e) => {
      const url = dom(e).attr('src') || dom(e).attr('href');
      if (!url || /^(https?:|data:|#)/.test(url)) return;
      const asset = url.split(/[?#]/)[0];
      assert.ok(fs.existsSync(path.resolve(root, asset.startsWith('/') ? asset.slice(1) : path.join(path.dirname(file), asset))), `${chapter}: missing ${url}`);
    });
  }
});

test('Chemistry and Biology tabs, solutions and all test levels work on mobile and desktop', { timeout: 600000 }, async () => {
  const browser = await chromium.launch({ headless: true });
  try {
    for (const width of [390, 1280]) {
      const context = await browser.newContext({ viewport: { width, height: 900 }, reducedMotion: 'reduce', serviceWorkers: 'block' });
      const page = await context.newPage();
      await page.route('https://sjmaths.com/**', async route => {
        let file = path.join(root, decodeURIComponent(new URL(route.request().url()).pathname));
        if (fs.existsSync(file) && fs.statSync(file).isDirectory()) file = path.join(file, 'index.html');
        if (!fs.existsSync(file)) return route.fulfill({ status: 404, body: file });
        const mime = { '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.svg': 'image/svg+xml' };
        await route.fulfill({ contentType: mime[path.extname(file)] || 'application/octet-stream', body: fs.readFileSync(file) });
      });
      const findings = [];
      for (const chapter of chapters) {
        const errors = [];
        const onError = e => errors.push(e.message);
        page.on('pageerror', onError);
        try {
          await page.goto(`https://sjmaths.com/class-10-science/${chapter}/`, { waitUntil: 'networkidle' });
          const nav = page.locator('.nav-btn,nav.nav button');
          const count = await nav.count();
          assert.ok(count >= 5);
          for (let index = 0; index < count; index++) {
            const button = nav.nth(index);
            const name = await button.evaluate(el => (el.dataset.tab || el.getAttribute('onclick').match(/'([^']+)'/)[1]).replace(/^tab-/, ''));
            await button.click();
            const panelId = await page.evaluate(name => (document.getElementById('tab-' + name) || document.getElementById(name)).id, name);
            assert.equal(await page.locator(`#${panelId}`).isVisible(), true, `${chapter}: ${name} visible`);
            assert.equal(await page.locator('.tab-panel:visible,section.tab:visible,.page:visible').count(), 1, `${chapter}: only one panel visible`);
            assert.equal(await page.evaluate(() => location.hash), '#' + name, `${chapter}: persistent ${name}`);
            await page.evaluate(() => Promise.all(document.getAnimations().map(animation => animation.finished.catch(() => {}))));
            const size = await page.evaluate(() => ({ width: innerWidth, content: document.documentElement.scrollWidth }));
            assert.ok(size.content <= size.width + 1, `${chapter}: ${name} overflow ${size.content}/${size.width}`);
            const reveal = page.locator(`#${panelId} button[onclick*="toggle"]:visible`).first();
            if (await reveal.count()) {
              await reveal.click();
              assert.equal(await reveal.evaluate(btn => btn.nextElementSibling.classList.contains('show')), true);
              await reveal.click();
              assert.equal(await reveal.evaluate(btn => btn.nextElementSibling.classList.contains('show')), false);
            }
          }
          await page.reload({ waitUntil: 'networkidle' });
          assert.equal(await page.locator('#test,#tab-test').isVisible(), true, `${chapter}: reload restore`);
          const levels = page.locator('.level-btn,.lev');
          assert.equal(await levels.count(), 3);
          for (let level = 1; level <= 3; level++) {
            await levels.nth(level - 1).click();
            const pane = page.locator(`#test${level},#level${level},#L${level}`).first();
            assert.equal(await pane.isVisible(), true, `${chapter}: level ${level} visible`);
            const questions = await page.evaluate(level => {
              const container = document.getElementById('test' + level) || document.getElementById('level' + level) || document.getElementById('L' + level);
              const questions = [...container.querySelectorAll('.test-question,.q')];
              const key = typeof tests !== 'undefined' ? tests[level].map(q => q.a) : typeof answers !== 'undefined' ? answers[level] : KEY[level];
              questions.forEach((question, index) => {
                const options = [...question.querySelectorAll('.option,.opt')];
                const answer = key[index];
                const button = typeof answer === 'number' ? options[answer] : options.find(option => option.dataset.v === answer || option.textContent.trim().startsWith(answer + '.'));
                if (!button) throw new Error('No answer option for question ' + index);
                button.click();
              });
              return questions.length;
            }, level);
            assert.ok(questions > 0, `${chapter}: questions rendered`);
            const submit = page.locator(`#submit${level},button[onclick="submitTest(${level})"],button[onclick="gradeTest()"],button[onclick="grade()"]`).filter({ visible: true }).first();
            await submit.click();
            await page.evaluate(() => Promise.all(document.getAnimations().map(animation => animation.finished.catch(() => {}))));
            const score = await page.locator(`#result${level},#score${level},#result`).first().textContent();
            assert.match(score.replace(/\s/g, ''), new RegExp(`${questions}/${questions}`), `${chapter}: full score level ${level}`);
            const correct = pane.locator('.option.correct-answer,.option.correct,.opt.good').first();
            assert.equal(await correct.evaluate(el => getComputedStyle(el).backgroundColor), 'rgb(240, 253, 244)', `${chapter}: correct answer colour`);
            const wrong = await pane.locator('.test-question,.q').first().locator('.option:not(.correct-answer):not(.correct),.opt:not(.good)').first().elementHandle();
            await wrong.click();
            await submit.click();
            await page.evaluate(() => Promise.all(document.getAnimations().map(animation => animation.finished.catch(() => {}))));
            assert.match((await page.locator(`#result${level},#score${level},#result`).first().textContent()).replace(/\s/g, ''), new RegExp(`${questions - 1}/${questions}`), `${chapter}: rescore changed answer`);
            assert.equal(await wrong.evaluate(el => getComputedStyle(el).backgroundColor), 'rgb(254, 242, 242)', `${chapter}: wrong answer colour`);
          }
          const mathErrors = await page.locator('.katex-error').evaluateAll(elements => elements.slice(0, 8).map(el => el.textContent));
          assert.deepEqual(mathErrors, [], `${chapter}: math errors`);
          assert.deepEqual(errors, [], `${chapter}: browser exceptions`);
          console.log(`${chapter} ${width}px: tabs, persistence, answers, 3 test levels passed`);
        } catch (error) {
          console.log(`FAILED ${chapter} ${width}px: ${error.message}`);
          findings.push(`${chapter} ${width}px: ${error.message}; browser errors=${JSON.stringify(errors)}`);
        } finally { page.off('pageerror', onError); }
      }
      await context.close();
      assert.deepEqual(findings, []);
    }
  } finally { await browser.close(); }
});
