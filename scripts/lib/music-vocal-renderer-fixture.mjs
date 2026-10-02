// Offline educational fixture; never sent to Gemini or written to a lesson URL.
export function musicVocalRendererFixture() {
  const marker = 'हिन्दी <script>alert(1)</script> & "स्वर"\nदूसरी पंक्ति';
  const points = [marker, 'नाद और श्रुति'];
  const concept = { id: 'c1', title: marker, lead: marker, explanation_points: points, key_points: points, examples: points, comparison_points: points, common_misconceptions: points, exam_focus_points: points };
  const revision = { concept_revisions: [{ title: marker, definition_points: points, must_remember: points, exam_traps: points }], glossary: [{ term: marker, definition: marker }], comparisons: [{ left: marker, right: marker, difference_points: points }], quick_facts: points, memory_hooks: points, exam_traps: points };
  const types = ['mcq', 'assertion_reason', 'true_false', 'fill_blank', 'match_following', 'case_based', 'short_answer'];
  const quiz_questions = types.map(type => ({ type, question: marker, options: points, correct_index: 0, accepted_answers: ['स्वर'], expected_answer: marker, explanation: marker }));
  return {
    content: { title: marker, short_title: marker, introduction_points: points, concepts: [concept, { ...concept, id: 'c2' }], revision },
    questions: { quiz_questions, topic_test: Array.from({ length: 10 }, () => ({ ...quiz_questions[0] })) },
    context: { url: '/music-vocal/acoustics/resonance/', topicName: marker, sectionTitle: marker }
  };
}
