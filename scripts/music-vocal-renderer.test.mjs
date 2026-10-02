import test from 'node:test';
import assert from 'node:assert/strict';
import vm from 'node:vm';
import { execFileSync } from 'node:child_process';
import { compileMusicVocalHtml } from './lib/music-vocal-renderer.mjs';
import { musicVocalTopicScript } from './lib/music-vocal-runtime.mjs';
import { musicVocalTopicStyleLink, externalizeMusicVocalStyles } from './lib/music-vocal-styles.mjs';
import { hasMusicVocalRendererWiring } from './lib/music-vocal-renderer-wiring.mjs';

test('complete offline renderer output matches the frozen compiler for all seven question types', () => {
  const baseline = execFileSync('git', ['show', '5d341a929ac7484c0c9c6e84486dab4e33a95995:scripts/generate_music_vocal_hi.mjs'], { encoding: 'utf8' }).replace(/\r\n/g, '\n');
  const block = baseline.slice(baseline.indexOf('function escapeHtml('), baseline.indexOf('function chooseApiKey('));
  const sandbox = { musicVocalTopicScript };
  vm.runInNewContext(block + '\nthis.render = compileHtml;', sandbox);
  const marker = 'हिन्दी <script>alert(1)</script> & "स्वर"\nदूसरी पंक्ति';
  const points = [marker, 'नाद और श्रुति'];
  const concept = { id: 'c1', title: marker, lead: marker, explanation_points: points, key_points: points, examples: points, comparison_points: points, common_misconceptions: points, exam_focus_points: points };
  const revision = { concept_revisions: [{ title: marker, definition_points: points, must_remember: points, exam_traps: points }], glossary: [{ term: marker, definition: marker }], comparisons: [{ left: marker, right: marker, difference_points: points }], quick_facts: points, memory_hooks: points, exam_traps: points };
  const types = ['mcq', 'assertion_reason', 'true_false', 'fill_blank', 'match_following', 'case_based', 'short_answer'];
  const quiz_questions = types.map(type => ({ type, question: marker, options: points, correct_index: 0, accepted_answers: [marker], expected_answer: marker, explanation: marker }));
  const questions = { quiz_questions, topic_test: Array.from({ length: 10 }, () => ({ ...quiz_questions[0] })) };
  const context = { url: '/music-vocal/acoustics/resonance/', topicName: marker, sectionTitle: marker };
  for (const short_title of [marker, '']) {
    const content = { title: marker, short_title, introduction_points: points, concepts: [concept, { ...concept, id: 'c2' }], revision };
    const expected = externalizeMusicVocalStyles(sandbox.render(content, questions, context));
    const before = JSON.stringify({ content, questions, context });
    const actual = compileMusicVocalHtml(content, questions, context, { musicVocalTopicScript, musicVocalTopicStyleLink });
    assert.equal(actual, expected);
    assert.equal(JSON.stringify({ content, questions, context }), before, 'rendering must not mutate educational data');
    assert.equal((actual.match(/class="tab(?: active)?"/g) || []).length, 4);
    assert.equal((actual.match(/class="question test-question"/g) || []).length, 10);
    for (const [id, data] of [['quiz-data', questions.quiz_questions], ['test-data', questions.topic_test]]) {
      const json = actual.match(new RegExp('<script type="application/json" id="' + id + '">([\\s\\S]*?)</script>'))[1];
      assert.deepEqual(JSON.parse(json), data);
      assert.ok(!json.includes('<script>'));
    }
    assert.ok(actual.includes('&lt;script&gt;alert(1)&lt;/script&gt;'));
  }
});

test('migration wiring rejects incomplete or edited forwarding', () => {
  const valid = "import { compileMusicVocalHtml } from './lib/music-vocal-renderer.mjs';\nfunction compileHtml(content, questions, context) {\n  return compileMusicVocalHtml(content, questions, context, { musicVocalTopicScript, musicVocalTopicStyleLink });\n}";
  assert.equal(hasMusicVocalRendererWiring(valid), true);
  assert.equal(hasMusicVocalRendererWiring(valid.replace(', musicVocalTopicStyleLink', '')), false);
  assert.equal(hasMusicVocalRendererWiring(valid.split('\n').slice(1).join('\n')), false);
});
