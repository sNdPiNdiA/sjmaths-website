'use strict';

const fs = require('node:fs');
const path = require('node:path');
const test = require('node:test');
const assert = require('node:assert/strict');
const { parse, ROOT } = require('./seo-html.cjs');
const {
  extractEnglishValues,
  extractHindiValues,
  isBilingualConcepts,
  numericTokenDifferences,
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

test('every Hindi and Sanskrit topic keeps paired English and Devanagari notes in its data and rendered HTML', () => {
  assert.equal(topicPages.length, 87, 'update the expected audit count when topics are added or removed');
  for (const { subject, topic, dir } of topicPages) {
    const label = `${subject}/${topic}`;
    const concepts = JSON.parse(fs.readFileSync(path.join(dir, 'tabs', 'concepts.json'), 'utf8'));
    const pageData = JSON.parse(fs.readFileSync(path.join(dir, 'data.json'), 'utf8'));
    assert.equal(isBilingualConcepts(concepts), true, `${label} concepts must keep both language layers`);
    assert.deepEqual(untranslatedLatinPaths(concepts), [], `${label} Hindi layer must not contain Latin-script prose`);
    assert.deepEqual(
      numericTokenDifferences(extractEnglishValues(concepts), extractHindiValues(concepts), subject),
      [],
      `${label} Hindi layer must preserve source number tokens`,
    );
    assert.deepEqual(pageData.concepts, concepts, `${label} data.json must match tabs/concepts.json`);

    const html = fs.readFileSync(path.join(dir, 'index.html'), 'utf8');
    const open = '<script id="upsc-page-data" type="application/json">';
    const start = html.indexOf(open);
    const end = start < 0 ? -1 : html.indexOf('</script>', start + open.length);
    assert.ok(start >= 0 && end > start, `${label} must contain inline topic data`);
    const inlineData = JSON.parse(html.slice(start + open.length, end).trim());
    assert.deepEqual(inlineData.concepts, concepts, `${label} inline data must match its authored concepts`);

    const $ = parse(html);
    assert.ok($('#topic-content .lang-en').length, `${label} needs English in crawlable rendered HTML`);
    assert.ok($('#topic-content .lang-hi').length, `${label} needs Devanagari in crawlable rendered HTML`);
    assert.match($('#topic-content .lang-hi').text(), /[\u0900-\u097F]/, `${label} Hindi layer should contain Devanagari script`);
  }
});
