'use strict';
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const cheerio = require('cheerio');
const policy = require('./seo-policy.cjs');
const root = path.resolve(__dirname, '..');
const scope = 'class-9-ganita-manjari-part-2';
const pages = [scope + '/index.html', ...fs.readdirSync(path.join(root, scope), { withFileTypes: true }).filter(d => d.isDirectory()).map(d => scope + '/' + d.name + '/index.html')];
const titles = new Set();
for (const file of pages) test(file + ' has consistent SEO and crawlable resources', () => {
  const $ = cheerio.load(fs.readFileSync(path.join(root, file), 'utf8'));
  // SVG title elements describe diagrams; they are not document title tags.
  assert.equal($('head > title').length, 1);
  assert.equal($('h1').length, 1);
  const title = $('head > title').text();
  assert.ok(!titles.has(title), 'duplicate page title'); titles.add(title);
  const description = $('meta[name="description"]').attr('content');
  assert.ok(description.includes('Part 2') && description.includes('Class 9'));
  for (const [attr, prefix] of [['property', 'og'], ['name', 'twitter']]) {
    assert.equal($(`meta[${attr}="${prefix}:title"]`).attr('content'), title);
    assert.equal($(`meta[${attr}="${prefix}:description"]`).attr('content'), description);
  }
  const canonical = $('link[rel="canonical"]').attr('href');
  assert.equal(canonical, policy.toUrl(file));
  assert.ok(fs.readFileSync(path.join(root, 'llms.txt'), 'utf8').includes(canonical), 'missing AI index link');
  assert.equal(policy.getSitemapName(file), 'sitemap-class-9.xml');
  assert.ok(fs.readFileSync(path.join(root, 'sitemap-class-9.xml'), 'utf8').includes('<loc>' + canonical + '</loc>'));
  const schema = JSON.parse($('script[type="application/ld+json"]').first().text());
  assert.equal(schema.name, title); assert.equal(schema.description, description); assert.equal(schema.url, canonical);
  const ids = $('[id]').map((i, e) => e.attribs.id).get();
  assert.equal(new Set(ids).size, ids.length, 'duplicate IDs');
  $('a[href]').each((i, link) => {
    const href = $(link).attr('href');
    if (href.startsWith('#')) assert.ok(ids.includes(href.slice(1)), 'missing fragment: ' + href);
    else if (!/^(https?:|mailto:|tel:)/.test(href)) {
      let target = href.startsWith('/') ? path.join(root, href) : path.resolve(root, path.dirname(file), href);
      if (href.endsWith('/')) target = path.join(target, 'index.html');
      assert.ok(fs.existsSync(target), 'missing link: ' + href);
    }
  });
  if (file === scope + '/index.html') {
    assert.equal($('.chapter').length, 6);
    assert.equal($('.hero-meta').length, 0);
    assert.match($('.hero-intro').text(), /six chapters/i);
    return;
  }
  assert.equal($('[role="tablist"], [role="tab"], [role="tabpanel"]').length, 0);
  assert.equal($('.tabs a[href^="#"]').length, $('.tabs .tabbtn').length);
  assert.equal($('.chapter-guide').length, 0);
  assert.equal($('.top .sub').text().trim(), 'Class 9 Ganita Manjari Part 2 · notes, exercises and mini test.');
  assert.ok($('.chapter-neighbours a').length >= 2);
  const answers = JSON.parse($('#exercise-answers').text() || '[]');
  assert.equal($('#p-exercises .answer-text').length, answers.length);
  $('#p-exercises .answer-text').each((i, e) => assert.equal($(e).text(), answers[i].answer));
  const quiz = JSON.parse($('#quiz-data').text());
  assert.equal($('#quiz .mc').length, quiz.length);
  $('#quiz .mc').each((i, e) => {
    assert.equal($(e).find('h4').text(), 'Q' + (i + 1) + '. ' + quiz[i].q);
    assert.deepEqual($(e).find('.op').map((j, o) => $(o).text()).get(), quiz[i].o);
  });
});
test('Class 9 hub links directly to Part 2', () => {
  const $ = cheerio.load(fs.readFileSync(path.join(root, 'class-9-maths/index.html'), 'utf8'));
  assert.equal($('a[href="/class-9-ganita-manjari-part-2/"]').length, 1);
});
