const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { execFileSync } = require('node:child_process');
const cheerio = require('cheerio');
const { ROOT, siteFiles } = require('./seo-html.cjs');
const { createResolver } = require('./seo-routes.cjs');

const read = file => fs.readFileSync(path.join(ROOT, file), 'utf8');
const load = file => cheerio.load(read(file));
const resolve = createResolver(siteFiles());
const retired = [
  ['chapter-9-triangles', 'circles', '/class-9-maths/chapter-wise-notes/chapter-5-circles/'],
  ['chapter-10-herons-formula', 'herons-formula', '/class-9-maths/chapter-wise-notes/chapter-6-perimeter-and-area/'],
  ['chapter-11-surface-areas-and-volumes', 'surface-area-and-volume', '/class-9-ganita-manjari-part-2/chapter-14-surface-area-and-volume/'],
];
const expectedNames = ['The Use of Coordinates', 'Introduction to Linear Polynomials', 'The World of Numbers', 'Exploring Algebraic Identities', 'Circles', 'Measuring Space: Perimeter and Area', 'Introduction to Probability', 'Sequences and Progressions', 'Propositions and Their Converses', 'How Quantities Combine: Understanding Data', 'The World of Algorithms', 'Quadrilaterals', 'Two Variables, One Line', 'Math of Space: Surface Area and Volume'];
const normalize = text => text.replace(/\s+/g, ' ').trim();

test('both chapter hubs show the correct 14 chapters and matching structured lists', () => {
  for (const [file, cards, title] of [
    ['class-9-maths/index.html', '#chapters-grid .ch-card-item', '.ch-card-title'],
    ['class-9-maths/chapter-wise-notes/index.html', 'main .chapter-card', 'h2'],
  ]) {
    const $ = load(file);
    assert.equal($(cards).length, 14, file);
    assert.deepEqual($(cards).map((i, e) => normalize($(e).find(title).text())).get(), expectedNames);
    const schemas = $('script[type="application/ld+json"]').map((i, e) => JSON.parse($(e).text())).get();
    const list = schemas.find(schema => schema['@type'] === 'ItemList');
    assert.equal(list.itemListElement.length, 14);
    assert.deepEqual(list.itemListElement.map(item => item.name), expectedNames);
    assert.equal($('h1').length, 1);
  }
});

test('SVG accessibility titles are distinct from the single document title', () => {
  for (const chapter of ['12-quadrilaterals', '13-two-variables-one-line', '14-surface-area-and-volume']) {
    const $ = load('class-9-ganita-manjari-part-2/chapter-' + chapter + '/index.html');
    assert.equal($('head > title').length, 1);
    assert.ok($('head > title').text().trim());
    $('svg').each((_, diagram) => assert.ok($(diagram).find('title').text().trim(), chapter + ': SVG needs an accessible title'));
  }
});

test('all current chapter and exercise links exist, including their fragment targets', () => {
  for (const [file, selector] of [
    ['class-9-maths/index.html', '#chapters-grid a[href]'],
    ['class-9-maths/chapter-wise-notes/index.html', 'main a[href]'],
    ['class-9-maths/ncert-exercise-practice/index.html', '#chapter-grid a[href]'],
    ['class-9-maths/previous-syllabus/index.html', 'main a[href]'],
  ]) {
    const $ = load(file);
    for (const a of $(selector).get()) {
      const href = $(a).attr('href');
      const result = resolve(href, 'https://sjmaths.com/' + file);
      assert.ok(result.file && !result.loop, `${file}: ${href}`);
      const hash = new URL(href, 'https://sjmaths.com/' + file).hash.slice(1);
      if (hash) assert.ok(load(result.file)(`[id="${decodeURIComponent(hash)}"]`).length, href);
    }
  }
  const $ = load('class-9-maths/ncert-exercise-practice/index.html');
  assert.equal($('#chapter-grid > details').length, 14);
  assert.ok($('#chapter-grid a[href]').length > 50, 'exercise links must be in the source HTML');
  assert.equal($('#chapter-grid [onclick]').length, 0, 'disclosures must be keyboard accessible');
});

test('topic redirects reach their final destinations in one hop on both hosts', () => {
  const firebase = JSON.parse(read('firebase.json')).hosting.redirects;
  for (const [slug, , destination] of retired) {
    for (const suffix of ['', '/', '/index.html']) {
      const source = '/class-9-maths/chapter-wise-notes/' + slug + suffix;
      const result = resolve(source);
      assert.equal(result.redirect, destination, source);
      assert.equal(result.chain.length, 1, source);
      assert.equal(result.chain[0].status, 301);
      assert.ok(result.file);
      const rule = firebase.find(item => item.source === source);
      assert.equal(rule.destination, destination);
      assert.equal(rule.type, 301);
    }
  }
  assert.equal(resolve('/class-9-maths/chapter-wise-notes/chapter-12-statistics/').redirect, undefined);
});

test('the three supplements preserve every original note section and its questions', () => {
  for (const [slug, archive] of retired) {
    const original = load('class-9-maths/chapter-wise-notes/' + slug + '/index.html');
    const archived = load('class-9-maths/previous-syllabus/' + archive + '/index.html');
    const sections = $ => $('.note-section').map((i, e) => normalize($(e).text())).get();
    assert.ok(sections(original).length >= 10);
    assert.deepEqual(sections(archived), sections(original), archive);
    assert.equal(archived('link[rel="canonical"]').attr('href'), 'https://sjmaths.com/class-9-maths/previous-syllabus/' + archive + '/');
    assert.equal(archived('.curriculum-notice').length, 1);
  }
});

test('syllabus notices do not modify legacy questions, answers, or inline runtime data', () => {
  function visit(directory) {
    for (const entry of fs.readdirSync(path.join(ROOT, directory), { withFileTypes: true })) {
      const file = directory + '/' + entry.name;
      if (entry.isDirectory()) visit(file);
      else if (entry.name.endsWith('.html')) {
        const content = read(file);
        if (!content.includes('data-curriculum="previous"')) continue;
        const before = cheerio.load(execFileSync('git', ['show', 'HEAD:' + file], { cwd: ROOT, encoding: 'utf8', maxBuffer: 8 * 1024 * 1024 }));
        const after = cheerio.load(content);
        before('[data-curriculum="previous"]').remove();
        after('[data-curriculum="previous"]').remove();
        assert.equal(normalize(after('body').text()), normalize(before('body').text()), file);
      }
    }
  }
  visit('class-9-maths');
});

test('sitemap and search publish canonical current and supplement URLs, excluding retired notes', () => {
  const sitemap = read('sitemap-class-9.xml');
  const search = JSON.parse(read('assets/js/search-index.json'));
  for (const [slug, archive] of retired) {
    const old = '/class-9-maths/chapter-wise-notes/' + slug + '/';
    assert.ok(!sitemap.includes('<loc>https://sjmaths.com' + old + '</loc>'));
    assert.ok(!search.some(entry => entry.url === old));
    assert.ok(sitemap.includes('<loc>https://sjmaths.com/class-9-maths/previous-syllabus/' + archive + '/</loc>'));
  }
  for (const entry of search.filter(item => item.url.startsWith('/class-9-ganita-manjari-part-2/'))) assert.equal(entry.category, 'Class 9');
  assert.ok(sitemap.includes('<loc>https://sjmaths.com/class-9-maths/chapter-wise-notes/chapter-12-statistics/</loc>'));
});

test('scoped discovery updates preserve unrelated search entries and sitemap blocks', () => {
  const baseline = file => execFileSync('git', ['show', 'HEAD:' + file], { cwd: ROOT, encoding: 'utf8', maxBuffer: 20 * 1024 * 1024 });
  const inScope = url => /\/class-9-(maths|ganita-manjari-part-2)\//.test(url);
  const entries = source => JSON.parse(source).filter(entry => !inScope(entry.url));
  assert.deepEqual(entries(read('assets/js/search-index.json')), entries(baseline('assets/js/search-index.json')));
  const blocks = source => [...source.matchAll(/<url>[\s\S]*?<\/url>/g)].map(match => match[0]).filter(block => !inScope(block));
  assert.deepEqual(blocks(read('sitemap-class-9.xml')), blocks(baseline('sitemap-class-9.xml')));
});
