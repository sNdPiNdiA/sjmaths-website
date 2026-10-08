'use strict';

const fs = require('node:fs');
const path = require('node:path');
const test = require('node:test');
const assert = require('node:assert/strict');
const { parse, ROOT } = require('./seo-html.cjs');
const {
  isBilingualConcepts,
  untranslatedLatinPaths,
} = require('./lib/up-assistant-bilingual.cjs');

const subjects = ['hindi', 'sanskrit'];
const topicPages = subjects.flatMap(subject => {
  const root = path.join(ROOT, 'up-assistant-teacher', subject);
  return fs.readdirSync(root, { withFileTypes: true })
    .filter(entry => entry.isDirectory())
    .map(entry => ({ subject, topic: entry.name, dir: path.join(root, entry.name) }))
    .filter(page => fs.existsSync(path.join(page.dir, 'tabs', 'concepts.json')));
});

function hasLanguagePair(value) {
  if (Array.isArray(value)) return value.some(hasLanguagePair);
  if (!value || typeof value !== 'object') return false;
  if (typeof value.en === 'string' || typeof value.hi === 'string') return true;
  return Object.values(value).some(hasLanguagePair);
}

test('every Hindi and Sanskrit topic contains only Devanagari lesson content and no English toggle layer', () => {
  assert.equal(topicPages.length, 87, 'update the expected audit count when topics are added or removed');
  for (const { subject, topic, dir } of topicPages) {
    const label = `${subject}/${topic}`;
    const concepts = JSON.parse(fs.readFileSync(path.join(dir, 'tabs', 'concepts.json'), 'utf8'));
    const pageData = JSON.parse(fs.readFileSync(path.join(dir, 'data.json'), 'utf8'));
    assert.equal(isBilingualConcepts(concepts), false, `${label} must not retain an English toggle layer`);
    assert.equal(hasLanguagePair(concepts), false, `${label} concepts must contain only the Devanagari layer`);
    assert.deepEqual(untranslatedLatinPaths(concepts), [], `${label} content must not contain Latin-script prose`);
    assert.deepEqual(pageData.concepts, concepts, `${label} data.json must match tabs/concepts.json`);

    const html = fs.readFileSync(path.join(dir, 'index.html'), 'utf8');
    const open = '<script id="upsc-page-data" type="application/json">';
    const start = html.indexOf(open);
    const end = start < 0 ? -1 : html.indexOf('</script>', start + open.length);
    assert.ok(start >= 0 && end > start, `${label} must contain inline topic data`);
    const inlineData = JSON.parse(html.slice(start + open.length, end).trim());
    assert.deepEqual(inlineData.concepts, concepts, `${label} inline data must match its authored concepts`);

    const $ = parse(html);
    assert.ok($('#topic-content .lang-hi').length, `${label} needs Devanagari in crawlable rendered HTML`);
    assert.match($('#topic-content .lang-hi').text(), /[\u0900-\u097F]/, `${label} Hindi layer should contain Devanagari script`);
    assert.equal($('.lang-en').length, 0, `${label} must not render English content`);
    assert.equal($('#langEn, #langHi, #headerLangToggleBtn, .lang-toggle').length, 0, `${label} must not render a language toggle`);
    assert.equal($('html').attr('lang'), subject === 'sanskrit' ? 'sa' : 'hi', `${label} document language must match the page language`);
    assert.ok($('body').hasClass('devanagari-only'), `${label} must stay in Devanagari-only mode`);
  }
});

test('Hindi and Sanskrit syllabus pages also render without English labels or language toggles', () => {
  for (const subject of subjects) {
    const file = path.join(ROOT, 'up-assistant-teacher', subject, 'index.html');
    const $ = parse(fs.readFileSync(file, 'utf8'));
    assert.equal($('.lang-en').length, 0, `${subject} syllabus must not retain English spans`);
    assert.equal($('#langEn, #langHi, #headerLangToggleBtn, .lang-toggle').length, 0, `${subject} syllabus must not retain a language toggle`);
    assert.equal($('html').attr('lang'), subject === 'sanskrit' ? 'sa' : 'hi');
    assert.ok($('body').hasClass('devanagari-only'));
    const body = $('body').clone();
    body.find('script, style').remove();
    assert.doesNotMatch(body.text(), /[A-Za-z]{2,}/, `${subject} visible syllabus text must be Devanagari-only`);
  }
});
