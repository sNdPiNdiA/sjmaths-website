import test from 'node:test';
import assert from 'node:assert/strict';
import crypto from 'node:crypto';
import * as cheerio from 'cheerio';
import { renderHistoryHtml, renderLegacyHtml } from './lib/history-renderer.mjs';
import { validateContent, validateQuestions, validateRevisionAndTest } from './lib/history-schema.mjs';
import { historyStyles } from './lib/history-styles.mjs';
import { content, questions, legacyContent, metadata, originalHtml } from './fixtures/history.mjs';

// Captured from the pre-extraction functions using this synthetic fixture.
const golden = {
  topic: ['79b03577726b9f36c21cd3b87902c96825243cdd6a75b9a44e62d5a150caa7d2', 'd277bc99036d56fd017b0d8b85b3cd46a2ab60c2fe32f44c88f38899ba3acd64'],
  expanded: ['56fa55a8fe96c0b3c7b41e9366751f100e75452c27a569dd7e559f2ccad5dd21', '5280eba50fa9bd0c7f7d23b9a65c3517be7ed66956e8c6bf01e801514cf207c7'],
  legacy: ['6885de37c3678c88f658cc0b805ca1b9a7ff995e2cea3b3e90cf8342f7e87efe', '6d74e0d09e0f61d1aba72fff5e0937aa76ac089fdc9f949c178b42dff8578723'],
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
