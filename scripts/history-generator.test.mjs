import test from 'node:test';
import assert from 'node:assert/strict';
import crypto from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';
import * as cheerio from 'cheerio';
import { renderHistoryHtml, renderLegacyHtml } from './lib/history-renderer.mjs';
import { validateContent, validateQuestions, validateRevisionAndTest } from './lib/history-schema.mjs';
import { historyStyles } from './lib/history-styles.mjs';
import { content, questions, legacyContent, metadata, originalHtml } from './fixtures/history.mjs';

// Captured from the pre-extraction functions using this synthetic fixture.
const golden = {
  topic: ['d03779062b5f03220730e11f77d71f5a29dc63a1a82145379efe4d4e6f892fab', '0aae7820b946c2496a10d2ffa3af3eacdf77d50c7b5d04f9f525f795efb7962d'],
  expanded: ['6804b51a32defa4fa673830bbff0ae0354ef358c72c167cead4611f1c49f6997', '9ef464f87ef8847c47a0f74e80707bfb5c56b51f69f512be7a3064accd88ae7b'],
  legacy: ['279e1d3f0fb865763a4ec530578c9ad0218412e90e0ac65f5f5f6bce6bf72ec5', '753435fbbfd960328605dec45a9a5613ab801e66298ca0035b9f7d4f162c7934'],
};
const hash = html => crypto.createHash('sha256').update(html).digest('hex');
for (const style of historyStyles) {
  test(`renderer extraction preserves exact ${style.id} output`, () => {
    assert.equal(hash(renderHistoryHtml(originalHtml(style.link), content, questions, metadata)), golden[style.id][0]);
    assert.equal(hash(renderLegacyHtml(originalHtml(style.link), legacyContent, metadata)), golden[style.id][1]);
  });
}

test('renderer preserves all concepts, seven question types, revision and data', () => {
  const $ = cheerio.load(renderHistoryHtml(originalHtml(historyStyles[0].link), content, questions, metadata));
  assert.equal($('.tab-panel').length, 4);
  assert.equal($('.notes-section').length, content.concepts.length);
  assert.equal($('.quiz-question-card').length, questions.quiz_questions.length);
  assert.equal($('.test-question-card').length, questions.topic_test.length);
  for (const concept of content.concepts) assert.ok($(`#concept-${concept.id}`).text().includes(concept.title));
  assert.deepEqual(JSON.parse($('#history-quiz-data').text()), questions.quiz_questions);
  assert.deepEqual(JSON.parse($('#history-test-data').text()), questions.topic_test);
  assert.equal($('#tab-quiz .q-text script').length, 0, 'question text is escaped, not executable');
  assert.equal($('aside').text(), 'Unchanged');
  const visibleText = $('body').text();
  assert.doesNotMatch(visibleText, /Core study module, theoretical overview|Practice across every concept with mixed question formats|Use this tab after completing the detailed notes|Attempt the objective questions and submit when finished/i);
  assert.equal($('.history-generated-badge').length, 0);
  assert.equal($('.revision-card-box h2').filter((_, el) => /Exam tricks|Topic mnemonics|Important comparisons/.test($(el).text())).length, 0);
});

test('validator extraction retains complete content and question coverage requirements', () => {
  const ids = content.concepts.map(concept => concept.id);
  assert.equal(validateContent(content), content);
  assert.equal(validateQuestions(questions, ids), questions);
  const revisionTest = { revision: content.revision, topic_test: questions.topic_test };
  assert.equal(validateRevisionAndTest(revisionTest, ids), revisionTest);
  const incomplete = structuredClone(content);
  incomplete.concepts[0].examples = [];
  assert.throws(() => validateContent(incomplete), /examples/);
  const unknown = structuredClone(questions);
  unknown.quiz_questions[0].concept_id = 'missing';
  assert.throws(() => validateQuestions(unknown, ids), /unknown concept/);
  const shortTest = structuredClone(revisionTest);
  shortTest.topic_test[0] = questions.quiz_questions.find(question => question.type === 'short_answer');
  assert.throws(() => validateRevisionAndTest(shortTest, ids), /must be objective/);
  const duplicateRevision = structuredClone(revisionTest);
  duplicateRevision.revision.concept_revisions[1].concept_id = ids[0];
  assert.throws(() => validateRevisionAndTest(duplicateRevision, ids), /Duplicate revision concept/);
});

test('regenerating built pages does not duplicate versioned shared styles or navigation', () => {
  const source = originalHtml(historyStyles[0].link)
    .replace('</head>', '<link rel="stylesheet" href="/assets/css/design-system.min.css?v=1234"></head>')
    .replace('</body>', '<script src="/assets/js/topic-mobile-nav.min.js?v=1234" defer></script></body>');
  const once = renderHistoryHtml(source, content, questions, metadata);
  const twice = renderHistoryHtml(once, content, questions, metadata);
  for (const result of [once, twice]) {
    const $ = cheerio.load(result);
    assert.equal($('link[href*="design-system"]').length, 1);
    assert.equal($('script[src*="topic-mobile-nav"]').length, 1);
    assert.equal($('#history-runtime').length, 1);
    assert.equal($('#history-quiz-data').length, 1);
    assert.equal($('.history-tab-shell').length, 1);
    assert.equal($('link[data-history-shared-style]').length, 1);
    assert.deepEqual(JSON.parse($('#history-quiz-data').text()), questions.quiz_questions);
  }
});

test('published History pages omit repeated generated filler while retaining lesson content', () => {
  const historyRoot = path.resolve('history');
  const collect = dir => fs.readdirSync(dir, { withFileTypes: true }).flatMap(entry => {
    const file = path.join(dir, entry.name);
    return entry.isDirectory() ? collect(file) : entry.name === 'index.html' ? [file] : [];
  });
  const pages = collect(historyRoot);
  assert.equal(pages.length, 144);
  for (const file of pages) {
    const html = fs.readFileSync(file, 'utf8');
    assert.doesNotMatch(html, /Core study module, theoretical overview|Practice across every concept with mixed question formats|Use this tab after completing the detailed notes|Attempt the objective questions and submit when finished|history-generated-badge/i, file);
    assert.match(html, /<h1\b/i, `${file} should retain its topic heading`);
  }
});
