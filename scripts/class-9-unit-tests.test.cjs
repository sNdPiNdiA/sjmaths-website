const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { execFileSync } = require('node:child_process');
const cheerio = require('cheerio');
const { units } = require('./data/class-9-unit-tests.cjs');
const { ROOT, siteFiles } = require('./seo-html.cjs');
const { createResolver } = require('./seo-routes.cjs');
const read = file => fs.readFileSync(path.join(ROOT, file), 'utf8');
const base = 'class-9-maths/tests/unit-wise';
const archive = 'class-9-maths/previous-syllabus/unit-tests';
const resolve = createResolver(siteFiles());

test('six supplied units, period counts and all 77 topic groups are assessed', () => {
  assert.deepEqual(units.map(u => u.periods), [12, 66, 6, 69, 27, 24]);
  assert.equal(units[5].name, 'Statistics and Probability');
  const coverage = JSON.parse(read(base + '/syllabus-coverage.json'));
  assert.equal(coverage.units.length, 6);
  assert.equal(coverage.units.flatMap(u => u.topics).length, 77);
  for (const unit of units) {
    const ids = new Set(unit.tests.flatMap(p => p.questions.map(q => q.id)));
    for (const topic of coverage.units.find(u => u.number === unit.number).topics) {
      assert.ok(topic.questions.length > 0, unit.name + ': ' + topic.label);
      assert.ok(topic.questions.every(id => ids.has(id)));
    }
  }
});
test('all twelve papers have source HTML questions, matching embedded/JSON data, answers and valid options', () => {
  for (const unit of units) for (const paper of unit.tests) {
    const file = `${base}/${unit.folder}/test-${paper.paper}.html`;
    const $ = cheerio.load(read(file));
    const data = JSON.parse(read(`${base}/${unit.folder}/${paper.paper === 1 ? 'test.json' : 'test-2.json'}`));
    assert.deepEqual(data, paper);
    assert.deepEqual(JSON.parse($('#unit-test-data').text()), data);
    assert.equal($('head > title').length, 1);
    assert.equal($('h1').length, 1);
    assert.equal($('.source-question').length, paper.questions.length);
    assert.equal($('.curriculum-notice').length, 0, 'archive label must not leak into a current paper');
    assert.notEqual($('#source-paper').attr('open'), undefined);
    assert.equal($('link[rel="canonical"]').attr('href'), 'https://sjmaths.com/' + file.replace(/\.html$/, ''));
    const ids = $('[id]').map((_, el) => $(el).attr('id')).get();
    assert.equal(new Set(ids).size, ids.length);
    for (const q of data.questions) {
      assert.ok(q.marks > 0 && Number.isInteger(q.marks));
      assert.ok(q.solutionSteps.length >= 2 && q.finalAnswer);
      assert.ok(q.topics.every(topic => Object.hasOwn(unit.topics, topic)));
      assert.equal($('#paper-' + q.id + ' > p').text(), q.question);
      if (q.type === 'mcq') {
        assert.equal(q.options.length, 4);
        assert.equal(new Set(q.options).size, 4);
        assert.ok(q.correctOption >= 0 && q.correctOption < 4);
        assert.equal(q.finalAnswer, '(' + String.fromCharCode(97 + q.correctOption) + ') ' + q.options[q.correctOption]);
      }
    }
  }
});
test('earlier twelve JSON papers and every question are preserved exactly', () => {
  for (const unit of units) for (const number of [1, 2]) {
    const name = number === 1 ? 'test.json' : 'test-2.json';
    let original = JSON.parse(execFileSync('git', ['show', `HEAD:${base}/${unit.folder}/${name}`], { cwd: ROOT, encoding: 'utf8' }));
    if (original.version === unit.tests[0].version) original = JSON.parse(execFileSync('git', ['show', `HEAD:${archive}/${unit.folder}/${name}`], { cwd: ROOT, encoding: 'utf8' }));
    assert.deepEqual(JSON.parse(read(`${archive}/${unit.folder}/${name}`)), original);
    const $ = cheerio.load(read(`${archive}/${unit.folder}/test-${number}.html`));
    assert.equal($('link[rel="canonical"]').attr('href'), `https://sjmaths.com/${archive}/${unit.folder}/test-${number}`);
  }
});
test('hub has six separate unit cards and twelve working current-paper links without exam weightage claims', () => {
  const $ = cheerio.load(read('class-9-maths/index.html'));
  assert.equal($('#unit-tests-section .hub-unit-card').length, 6);
  assert.equal($('#unit-tests-section .unit-action-btn').length, 12);
  assert.deepEqual($('#unit-tests-section .unit-weight-badge').map((_, el) => $(el).text()).get(), units.map(u => u.periods + ' Periods'));
  assert.ok(!$('#unit-tests-section').text().includes('Previous-Syllabus'));
  $('#unit-tests-section .unit-action-btn').each((_, element) => assert.match($(element).attr('href'), /\/test-[12]\.html$/));
  for (const file of ['class-9-maths/index.html', base + '/index.html', archive + '/index.html', ...units.flatMap(u => [base + '/' + u.folder + '/index.html', archive + '/' + u.folder + '/index.html'])]) {
    const dom = cheerio.load(read(file));
    dom('a[href]').each((_, element) => {
      const href = dom(element).attr('href');
      if (/^#/.test(href)) return;
      const result = resolve(href, 'https://sjmaths.com/' + file);
      assert.ok(result.external || result.file, file + ': ' + href);
      if (href.includes('test-') && (href.includes('/unit-wise/') || href.includes('/previous-syllabus/unit-tests/')) && !href.includes('.json')) {
        assert.match(href, /test-[12]\.html$/, file + ': test link must resolve on plain static hosts');
      }
    });
  }
});
test('representative numeric answers are independently verified', () => {
  const q = id => units.flatMap(u => u.tests.flatMap(p => p.questions)).find(item => item.id === id);
  assert.equal((20 * 60 + 30 * 80) / 50, 72);
  assert.ok(q('u6t1q5').finalAnswer.includes('72'));
  assert.equal(Math.sqrt(21 * 8 * 7 * 6), 84);
  assert.ok(q('u5t1q6').finalAnswer.includes('84'));
  assert.equal(50 * 51 / 2, 1275);
  assert.ok(q('u2t1q9').finalAnswer.includes('1275'));
  assert.equal(6 ** 3 / 2 ** 3, 27);
  assert.ok(q('u5t2q8').finalAnswer.includes('27'));
  assert.equal((3 * 2 + 2 * 3) / (5 * 4), 0.6);
  assert.ok(q('u6t2q6').finalAnswer.includes('3/5'));
  assert.equal((1 / 3) * 36 * 4, 48);
  assert.ok(q('u5t1q9').finalAnswer.includes('48'));
});
