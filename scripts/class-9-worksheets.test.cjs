const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { execFileSync } = require('node:child_process');
const cheerio = require('cheerio');
const { worksheets } = require('./data/class-9-worksheets.cjs');
const { units } = require('./data/class-9-unit-tests.cjs');
const { ROOT, siteFiles } = require('./seo-html.cjs');
const { createResolver } = require('./seo-routes.cjs');
const read = file => fs.readFileSync(path.join(ROOT, file), 'utf8');
const base = 'class-9-maths/worksheets/current-syllabus';
const resolve = createResolver(siteFiles());

test('all fourteen current chapters and the supplement cover all 77 mapped syllabus groups', () => {
  assert.deepEqual(worksheets.filter(sheet => sheet.number).map(sheet => sheet.number), Array.from({ length: 14 }, (_, i) => i + 1));
  const coverage = JSON.parse(read(base + '/syllabus-coverage.json'));
  assert.equal(coverage.units.flatMap(unit => unit.topics).length, 77);
  for (const unit of coverage.units) for (const topic of unit.topics) {
    assert.ok(topic.worksheetQuestions.length > 0, unit.number + ': ' + topic.label);
    for (const target of topic.worksheetQuestions) {
      const result = resolve(target.url);
      assert.ok(result.file);
      const $ = cheerio.load(read(result.file));
      assert.equal($('#question-' + target.id).length, 1);
    }
  }
  const ids = new Set(worksheets.flatMap(sheet => sheet.questions.map(q => q.id)));
  assert.equal(ids.size, 169);
  for (const q of units.flatMap(unit => unit.tests.flatMap(paper => paper.questions))) assert.ok(ids.has(q.id));
});

test('questions and complete model steps are crawlable, correctly grouped and accessible without JS', () => {
  for (const sheet of worksheets) {
    const file = base + '/' + sheet.folder + '/index.html';
    const $ = cheerio.load(read(file));
    assert.equal($('head > title').length, 1);
    assert.equal($('h1').length, 1);
    assert.equal($('.worksheet-question').length, sheet.questions.length);
    assert.equal($('link[rel="canonical"]').attr('href'), 'https://sjmaths.com/' + base + '/' + sheet.folder + '/');
    assert.equal($('meta[property="og:title"]').attr('content'), $('head > title').text());
    assert.equal($('meta[property="og:description"]').attr('content'), $('meta[name="description"]').attr('content'));
    assert.equal($('script[src*="require-auth"]').length, 1);
    const ids = $('[id]').map((_, el) => $(el).attr('id')).get();
    assert.equal(new Set(ids).size, ids.length);
    for (const q of sheet.questions) {
      const item = $('#question-' + q.id);
      assert.equal(item.find('.question-text').text(), q.question);
      assert.equal(item.closest('.sheet-section').attr('id'), q.level);
      assert.equal(item.find('.worksheet-solution > p').text(), q.finalAnswer);
      assert.deepEqual(item.find('.worksheet-solution > ol > li').map((_, li) => $(li).text()).get(), q.solutionSteps);
      assert.ok(q.solutionSteps.length >= 2);
      assert.equal(item.find('details').attr('open'), undefined);
      if (q.type === 'mcq') assert.deepEqual(item.find('.question-options > li').map((_, li) => $(li).text()).get(), q.options);
    }
    $('svg').each((_, svg) => { assert.ok($(svg).attr('aria-label')); assert.ok($(svg).find('title').text()); });
    $('a[href]').each((_, link) => {
      const href = $(link).attr('href');
      if (href.startsWith('#')) assert.ok(ids.includes(href.slice(1)));
      else assert.ok(resolve(href, 'https://sjmaths.com/' + file).file, href);
    });
  }
});

test('all dashboard Sheets buttons and current directory links reach the correct chapter', () => {
  const $ = cheerio.load(read('class-9-maths/index.html'));
  const cards = $('#chapters-grid .ch-card-item');
  assert.equal(cards.length, 14);
  for (const sheet of worksheets.filter(sheet => sheet.number)) {
    const button = cards.eq(sheet.number - 1).find('.sheet-tab');
    assert.equal(button.length, 1);
    const links = button.closest('details').find('.quick-tab-menu a');
    assert.equal(links.length, 3);
    assert.deepEqual(links.map((_, link) => $(link).attr('href')).get(), ['foundation', 'practice', 'challenge'].map(level => '/' + base + '/' + sheet.folder + '/#' + level));
  }
  const directory = cheerio.load(read('class-9-maths/worksheets/index.html'));
  assert.equal(directory('.worksheet-entry').length, 15);
  assert.equal(directory('#earlier-worksheets a').length, siteFiles().filter(file => /^class-9-maths\/worksheets\/chapter-[^/]+\/[^/]+\.html$/.test(file)).length);
  directory('#chapter-grid a[href]').each((_, link) => assert.ok(resolve(directory(link).attr('href')).file));
});

test('every earlier worksheet question and solution remains unchanged', () => {
  for (const file of siteFiles().filter(file => /^class-9-maths\/worksheets\/chapter-[^/]+\/[^/]+\.html$/.test(file))) {
    const before = cheerio.load(execFileSync('git', ['show', 'HEAD:' + file], { cwd: ROOT, encoding: 'utf8' }));
    const after = cheerio.load(read(file));
    assert.ok(before('.question-list').length, file);
    assert.equal(after('.question-list').html(), before('.question-list').html(), file);
  }
});

test('worksheet-only calculations have independent numeric checks', () => {
  const q = id => worksheets.flatMap(sheet => sheet.questions).find(q => q.id === id);
  assert.equal(Math.hypot(8 - 2, 5 - (-3)), 10);
  assert.match(q('ws-1-new-2').finalAnswer, /10 units/);
  assert.equal((200 - 120) / (15 - 10), 16);
  assert.match(q('ws-2-new-3').finalAnswer, /16 km/);
  assert.equal(2 * Math.sqrt(13 ** 2 - 5 ** 2), 24);
  assert.match(q('ws-5-new-2').finalAnswer, /24 cm/);
  assert.equal(Math.sqrt(16 * 6 * 6 * 4), 48);
  assert.match(q('ws-6-new-2').finalAnswer, /48 cm²/);
  assert.equal((10 * 50 + 20 * 80) / 30, 70);
  assert.equal(q('ws-10-new-1').correctOption, 1);
  assert.equal(100 * 12 / 3, 400);
  assert.match(q('ws-14-new-3').finalAnswer, /400 cm³/);
});
