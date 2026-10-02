import test from 'node:test';
import assert from 'node:assert/strict';
import vm from 'node:vm';
import { execFileSync } from 'node:child_process';
import { QUESTION_TYPES, validateContent, validateQuestions } from './lib/music-vocal-schema.mjs';

const original = execFileSync('git', ['show', '150c071b46:scripts/generate_music_vocal_hi.mjs'], { encoding: 'utf8' }).replace(/\r\n/g, '\n');
const frozen = { QUESTION_TYPES };
vm.runInNewContext(original.slice(original.indexOf('function requireText('), original.indexOf('function buildContentPrompt(')) + '\nthis.content = validateContent; this.questions = validateQuestions;', frozen);
const points = count => Array.from({ length: count }, (_, i) => `बिंदु ${i + 1}`);
function fixture() {
  const concepts = Array.from({ length: 4 }, (_, i) => ({ id: `c${i}`, title: 'अवधारणा', lead: 'परिचय', explanation_points: points(5), key_points: points(4), examples: points(2), comparison_points: points(2), common_misconceptions: points(2), exam_focus_points: points(3) }));
  const content = { title: 'संगीत', section_title_hi: 'नाद', introduction_points: points(4), concepts, revision: { concept_revisions: concepts.map(c => ({ concept_id: c.id, title: c.title, definition_points: points(3), must_remember: points(5), exam_traps: points(2) })), quick_facts: points(5), glossary: points(4).map(term => ({ term, definition: 'अर्थ' })), comparisons: [{ left: 'नाद', right: 'श्रुति', difference_points: points(2) }], memory_hooks: points(3), exam_traps: points(4) } };
  const question = (concept_id, type, id) => ({ id, concept_id, type, question: 'प्रश्न', explanation: 'व्याख्या', options: ['स्वर', 'लय'], correct_index: 0, accepted_answers: ['स्वर'], expected_answer: 'स्वर' });
  return { content, questions: { quiz_questions: concepts.flatMap(c => QUESTION_TYPES.map((type, i) => question(c.id, type, `${c.id}-${i}`))), topic_test: Array.from({ length: 10 }, (_, i) => question(`c${i % 4}`, ['mcq', 'assertion_reason', 'match_following', 'case_based'][i % 4], `t${i}`)) } };
}
function outcome(fn, value, ids) {
  try { return { accepted: fn(value, ids) === value }; }
  catch (error) { return { error: error.message }; }
}

test('schema accepts complete four-concept notes and all required quiz/test types without mutation', () => {
  const { content, questions } = fixture();
  const before = JSON.stringify({ content, questions });
  assert.equal(validateContent(content), content);
  assert.equal(validateQuestions(questions, content.concepts.map(c => c.id)), questions);
  assert.equal(JSON.stringify({ content, questions }), before);
  assert.deepEqual(outcome(validateContent, content), outcome(frozen.content, content));
});

test('incomplete educational sections retain the original rejection behavior', () => {
  const mutations = [
    value => { value.concepts.pop(); }, value => { value.title = ''; },
    value => { value.section_title_hi = null; }, value => { value.introduction_points.pop(); },
    value => { value.concepts[1].id = value.concepts[0].id; },
    value => { value.revision.concept_revisions.pop(); },
    value => { value.revision.concept_revisions[0].concept_id = 'unknown'; },
    ...['explanation_points', 'key_points', 'examples', 'comparison_points', 'common_misconceptions', 'exam_focus_points'].flatMap(field => [
      value => { value.concepts[0][field].pop(); }, value => { value.concepts[0][field][0] = ''; }
    ]),
    ...['definition_points', 'must_remember', 'exam_traps'].flatMap(field => [
      value => { value.revision.concept_revisions[0][field].pop(); }, value => { value.revision.concept_revisions[0][field][0] = ''; }
    ]),
    ...['quick_facts', 'glossary', 'comparisons', 'memory_hooks', 'exam_traps'].map(field => value => { value.revision[field].pop(); })
  ];
  for (const mutate of mutations) {
    const { content } = fixture(); mutate(content);
    const current = outcome(validateContent, content);
    assert.ok(current.error);
    assert.deepEqual(current, outcome(frozen.content, content));
  }
});

test('missing quiz coverage, unknown concepts and invalid answers retain original rejection behavior', () => {
  const mutations = [
    q => { q.quiz_questions.pop(); }, q => { q.topic_test.pop(); },
    q => { q.quiz_questions[0].concept_id = 'unknown'; },
    q => { q.topic_test[0].concept_id = 'unknown'; },
    q => { q.quiz_questions[0].type = 'other'; },
    q => { q.quiz_questions[1].type = 'mcq'; },
    q => { q.quiz_questions[0].correct_index = 2; },
    q => { q.quiz_questions[0].correct_index = -1; },
    q => { q.quiz_questions[0].options = ['one']; },
    q => { q.quiz_questions[3].accepted_answers = []; },
    q => { q.quiz_questions[6].expected_answer = ''; },
    q => { q.topic_test[0].type = 'short_answer'; },
    ...['id', 'concept_id', 'type', 'question', 'explanation'].map(field => q => { q.quiz_questions[0][field] = ''; })
  ];
  const ids = ['c0', 'c1', 'c2', 'c3'];
  for (const mutate of mutations) {
    const { questions } = fixture(); mutate(questions);
    const current = outcome(validateQuestions, questions, ids);
    assert.ok(current.error);
    assert.deepEqual(current, outcome(frozen.questions, questions, ids));
  }
});
