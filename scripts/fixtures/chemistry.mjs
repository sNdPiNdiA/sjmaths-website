// Synthetic offline preservation fixture, never a production lesson.
export const item = { url: '/chemistry/physical-chemistry/chemical-kinetics/activation-energy/', titleGuess: 'Kinetics' };
export const context = { sectionMeta: { en: 'Physical Chemistry' }, sectionKey: 'physical-chemistry', related: [{ url: '/chemistry/', title: 'Chemistry' }], prevTopic: { href: '/chemistry/', title: 'Previous' }, nextTopic: { href: '/chemistry/', title: 'Next' } };
const questions = (count, label) => Array.from({ length: count }, (_, i) => ({ question: `${label} question ${i + 1}`, options: ['First option', 'Second option', 'Third option', 'Fourth option'], correct_index: i % 4, explanation: `${label} explanation ${i + 1}`, year_tag: i === 0 ? '2020, 2023' : '2023' }));
export const data = {
  title: 'Kinetics', topic_intro: 'Original introductory text',
  concise_notes: [{ module_title: 'Concept A', bullets: ['Original point A', '$r=k[A]$'] }, { module_title: 'Concept B', bullets: ['Original point B', 'Original point C'] }],
  formula_sheet: [{ name: 'Rate law', equation_html: '<span>r=k[A]</span>', conditions: 'First order', units: 'mol L^-1 s^-1' }],
  critical_exceptions: [{ rule: 'Original rule', exception: 'Original exception', reason: 'Original reason' }],
  tips_and_tricks: [{ trick_title: 'Original shortcut', shortcut_formula: '$r=k[A]$', application: 'Original application' }],
  comparison_matrix: { title: 'Original comparison', headers: ['First', 'Second'], rows: [['Cell A', 'Cell B']] },
  exam_points: ['Original exam point'], common_pitfalls: ['Original pitfall'],
  chapter_summary_concepts: [{ concept_title: 'Concept A', concept_body_html: '<p>Original revision point A</p>' }],
  quick_revision: { terms_glossary: [{ term: 'Rate', definition: 'Original definition' }], must_remember: ['Original takeaway'], summary: ['Original recall'], common_confusions: [{ term_a: 'First', term_b: 'Second', difference: 'Original distinction' }] },
  quiz: questions(20, 'Practice'), pyq_patterns: questions(6, 'PYQ'), topic_test: questions(10, 'Test'),
};
export const enData = {
  title: data.title, lead: data.topic_intro, kicker: 'Chemistry',
  sections: data.concise_notes.map(n => ({ heading: n.module_title, bullets: n.bullets })),
  formulas: [{ name: 'Rate law', eq: '<span>r=k[A]</span>', conditions: 'First order', units: 'mol L^-1 s^-1' }],
  exceptions: [{ rule: 'Original rule', observation: 'Original exception' }],
  tricks: [{ title: 'Original shortcut', shortcut: '$r=k[A]$', application: 'Original application' }],
  comparison: data.comparison_matrix, exam_points: data.exam_points, common_errors: data.common_pitfalls,
  summary_concepts: [{ title: 'Concept A', body: '<p>Original revision point A</p>' }],
  glossary: data.quick_revision.terms_glossary, key_takeaways: data.quick_revision.must_remember,
  quick_recall: data.quick_revision.summary, key_differences: data.quick_revision.common_confusions,
};
export const hiData = {
  title_hi: 'रासायनिक गतिकी', lead_hi: 'मूल परिचय', kicker_hi: 'रसायन विज्ञान',
  sections_hi: [{ heading_hi: 'अवधारणा A', bullets_hi: ['मूल बिंदु A', '$r=k[A]$'] }, { heading_hi: 'अवधारणा B', bullets_hi: ['मूल बिंदु B', 'मूल बिंदु C'] }],
  formula_meta_hi: [{ name_hi: 'वेग नियम', conditions_hi: 'प्रथम कोटि', units_hi: 'mol L^-1 s^-1' }],
  exceptions_hi: [{ rule_hi: 'मूल नियम', observation_hi: 'मूल अपवाद' }],
  tricks_hi: [{ title_hi: 'मूल सूत्र', application_hi: 'मूल उपयोग' }],
  comparison_hi: { title_hi: 'मूल तुलना', headers_hi: ['पहला', 'दूसरा'], rows_hi: [['A', 'B']] },
  exam_points_hi: ['मूल परीक्षा बिंदु'], common_errors_hi: ['मूल त्रुटि'],
  summary_concepts_hi: [{ title_hi: 'अवधारणा A', body_hi: 'मूल पुनरावृत्ति बिंदु' }],
  glossary_hi: [{ term_hi: 'वेग', definition_hi: 'मूल परिभाषा' }],
  key_takeaways_hi: ['मूल निष्कर्ष'], quick_recall_hi: ['मूल स्मरण'],
  key_differences_hi: [{ term_a_hi: 'पहला', term_b_hi: 'दूसरा', difference_hi: 'मूल अंतर' }],
};
export const translatedQuestions = questions => questions.map((q, i) => ({ ...q, question_hi: `प्रश्न ${i + 1}`, options_hi: ['पहला', 'दूसरा', 'तीसरा', 'चौथा'], explanation_hi: `व्याख्या ${i + 1}` }));
