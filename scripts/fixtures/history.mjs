// Synthetic test material only; never written into student pages.
export const metadata = { title: 'Fixture & <Topic>', breadcrumb: 'Fixture', kicker: 'Test' };
const points = count => Array.from({ length: count }, (_, i) => `Point ${i + 1}: & <tag>\nSecond line`);
export const content = {
  introduction_points: points(4),
  concepts: Array.from({ length: 6 }, (_, i) => ({
    id: `concept-${i}`, title: `Concept ${i}`, lead: 'Lead & <text>',
    explanation_points: points(5), key_points: points(4), examples: points(2),
    comparison_points: points(2), common_misconceptions: points(2), exam_focus_points: points(3),
  })),
};
content.revision = {
  concept_revisions: content.concepts.map(concept => ({
    concept_id: concept.id, title: concept.title, pointwise_summary: points(4),
    mnemonics: points(1), tips: points(1), tricks: points(1), common_traps: points(1),
  })),
  quick_facts: points(8), mnemonics: points(3), tips: points(4), tricks: points(4), exam_traps: points(5),
  comparisons: [{ left: 'Left', right: 'Right', difference_points: points(3) }],
};
const types = ['mcq', 'assertion_reason', 'true_false', 'fill_blank', 'match_following', 'case_based', 'short_answer'];
function question(index, type) {
  return {
    id: `question-${index}`, concept_id: content.concepts[index % 6].id, type,
    question: `Question ${index}: <script>alert("test")</script> & details`, explanation: 'Explanation & <tag>',
    ...(type === 'fill_blank' ? { accepted_answers: ['Answer'] }
      : type === 'short_answer' ? { expected_answer: 'Expected answer' }
      : { options: ['A & <tag>', 'B'], correct_index: 0 }),
  };
}
export const questions = {
  quiz_questions: Array.from({ length: 35 }, (_, i) => question(i, types[i % types.length])),
  topic_test: Array.from({ length: 10 }, (_, i) => question(i, 'mcq')),
};
export const legacyContent = {
  syllabus_focus_points: ['<strong>Focus:</strong> Original wording'],
  study_sections: [{ heading: 'Heading & <tag>', points: ['<strong>Concept:</strong> Original point'] }],
  key_facts_revision: ['Original fact'], exam_traps_and_distinctions: ['Original trap'],
  interactive_checklist: ['Original checklist'],
};
export function originalHtml(styleLink) {
  return `<!doctype html><html lang="en"><head><title>Fixture</title>${styleLink}</head><body>
<header class="site-header"><div class="header-inner"><a class="back-btn" href="/history/">Back</a></div></header>
<section class="hero"><h1>Fixture</h1><div class="exam-badges"></div></section>
<div class="main-grid"><div class="content-col"><p>Old content</p></div><aside>Unchanged</aside></div>
</body></html>`;
}
