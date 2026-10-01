// Offline preservation fixture, never a production lesson.
export const context = { topicUrl: '/english/language/grammar/narration/', sectionTitle: 'Grammar', topicName: 'Narration' };
const questions = (count, label) => Array.from({ length: count }, (_, i) => ({ question: label + ' question ' + (i + 1), options: ['First', 'Second', 'Third', 'Fourth'], correct_index: i % 4, explanation: label + ' explanation ' + (i + 1), exam_year: i === 0 ? '2020, 2023' : '2023' }));
export const call1 = { title: 'Narration', short_intro: 'Original introduction', academic_synopsis: 'Original synopsis',
  conceptual_pillars: [{ pillar_title: 'Concept A', lead_concept: 'Original concept', detailed_analysis_points: ['Original point A', 'Original point B'], comparative_insights: 'Original comparison', key_takeaways: ['Original takeaway'] }, { pillar_title: 'Concept B', lead_concept: 'Original concept B', detailed_analysis_points: ['Original point C'] }],
  formulas_and_scales: [{ name: 'Original rule', equation: 'Original expression', parameters: 'Original parameters', exam_significance: 'Original significance' }],
  spatial_and_regional_distribution: { global_patterns: 'Original historical context', indian_context: 'Original Indian context' },
  tricks_and_mnemonics: [{ title: 'Original mnemonic', mnemonic: 'Original shortcut', explanation: 'Original rationale', exam_pitfall_warning: 'Original pitfall' }],
};
export const call2 = { quick_revision: { glossary_terms: [{ term: 'Original term', definition: 'Original definition', exam_tag: 'PGT' }], high_yield_laws_and_theories: [{ theorist_or_law: 'Original rule', year_or_period: '2023', core_postulate: 'Original postulate' }] }, practice_quiz: questions(20, 'Practice'), pyqs: questions(6, 'PYQ'), topic_test: questions(10, 'Test') };

