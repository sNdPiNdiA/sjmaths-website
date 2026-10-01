// Offline preservation data; never production educational content.
export const item = { url: '/agriculture/agricultural-botany/cell-biology/biology-of-cell/', inTgt: true, inPgt: true, examRelevance: 'Both' };
export const context = { sectionKey: 'agricultural-botany', sectionMeta: { en: 'Agricultural Botany' }, prevTopic: { href: '/agriculture/', title: 'Previous' }, nextTopic: { href: '/agriculture/', title: 'Next' }, related: [{ url: '/agriculture/', title: 'Related' }] };
const questions = (count, label) => Array.from({ length: count }, (_, i) => ({ question: label + ' question ' + (i + 1), options: ['First', 'Second', 'Third', 'Fourth'], correct_index: i % 4, explanation: label + ' explanation ' + (i + 1), difficulty: 'PGT' }));
export const data = {
  title: 'Cell Biology', short_intro: 'Original introduction',
  notes_sections: [{ heading: 'Concept A', content_html: '<ul><li>Original point A</li><li>$2n$</li></ul>' }, { heading: 'Concept B', content_html: '<p>Original point B</p>' }],
  comparison_tables: [{ title: 'Original comparison', headers: ['First', 'Second'], rows: [['Cell A', 'Cell B']] }],
  mnemonics: [{ title: 'Original mnemonic', trick: 'Original trick', explanation: 'Original rationale' }],
  exam_points: ['Original exam point'], common_errors: ['Original pitfall'],
  chapter_summary_concepts: [{ concept_num: '1', concept_title: 'Concept A', concept_body_html: '<p>Original summary A</p>' }],
  quick_revision: { terms_glossary: [{ term: 'Cell', term_en: 'Cell', definition: 'Original definition' }], must_remember: ['Original takeaway'], summary: ['Original recall'], common_confusions: [{ term_a: 'First', term_b: 'Second', difference: 'Original distinction' }] },
  quiz: questions(20, 'Practice'), topic_test: questions(10, 'Test'),
};
