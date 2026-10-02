// Music Vocal content contract, kept independent of API calls and file writes.
export const QUESTION_TYPES = ['mcq', 'assertion_reason', 'true_false', 'fill_blank', 'match_following', 'case_based', 'short_answer'];

function requireText(value, label) { if (typeof value !== 'string' || !value.trim()) throw new Error(`${label} must be a non-empty string`); }

export function validateContent(data) {
  if (!data || !Array.isArray(data.concepts) || data.concepts.length < 4 || data.concepts.length > 8) throw new Error('Content must contain 4–8 concepts');
  requireText(data.title, 'title'); requireText(data.section_title_hi, 'section_title_hi');
  if (!Array.isArray(data.introduction_points) || data.introduction_points.length < 4) throw new Error('Introduction needs at least 4 point-wise items');
  const ids = new Set();
  for (const [index, concept] of data.concepts.entries()) {
    requireText(concept.id, `concept ${index + 1} id`); requireText(concept.title, `concept ${index + 1} title`); requireText(concept.lead, `concept ${concept.id} lead`);
    if (ids.has(concept.id)) throw new Error(`Duplicate concept id: ${concept.id}`); ids.add(concept.id);
    for (const [field, minimum] of [['explanation_points', 5], ['key_points', 4], ['examples', 2], ['comparison_points', 2], ['common_misconceptions', 2], ['exam_focus_points', 3]]) {
      if (!Array.isArray(concept[field]) || concept[field].length < minimum) throw new Error(`Concept ${concept.id} needs ${minimum} ${field}`);
      concept[field].forEach((item, itemIndex) => requireText(item, `${concept.id}.${field}[${itemIndex}]`));
    }
  }
  const revision = data.revision;
  if (!revision || !Array.isArray(revision.concept_revisions) || revision.concept_revisions.length !== data.concepts.length) throw new Error('Revision needs one detailed entry for every concept');
  const revisionIds = new Set();
  revision.concept_revisions.forEach((item) => {
    requireText(item.concept_id, 'revision concept_id'); requireText(item.title, `revision ${item.concept_id} title`);
    if (!ids.has(item.concept_id) || revisionIds.has(item.concept_id)) throw new Error(`Invalid or duplicate revision concept: ${item.concept_id}`);
    revisionIds.add(item.concept_id);
    for (const [field, minimum] of [['definition_points', 3], ['must_remember', 5], ['exam_traps', 2]]) {
      if (!Array.isArray(item[field]) || item[field].length < minimum) throw new Error(`Revision ${item.concept_id} needs ${minimum} ${field}`);
      item[field].forEach((point, pointIndex) => requireText(point, `revision ${item.concept_id}.${field}[${pointIndex}]`));
    }
  });
  if (!Array.isArray(revision.quick_facts) || revision.quick_facts.length < 5) throw new Error('Revision needs 5 quick facts');
  if (!Array.isArray(revision.glossary) || revision.glossary.length < 4) throw new Error('Revision needs 4 glossary items');
  if (!Array.isArray(revision.comparisons) || revision.comparisons.length < 1) throw new Error('Revision needs comparisons');
  if (!Array.isArray(revision.memory_hooks) || revision.memory_hooks.length < 3) throw new Error('Revision needs memory hooks');
  if (!Array.isArray(revision.exam_traps) || revision.exam_traps.length < 4) throw new Error('Revision needs exam traps');
  return data;
}

function validateQuestion(question, label, allowShort = true) {
  requireText(question.id, `${label}.id`); requireText(question.concept_id, `${label}.concept_id`); requireText(question.type, `${label}.type`); requireText(question.question, `${label}.question`); requireText(question.explanation, `${label}.explanation`);
  if (!QUESTION_TYPES.includes(question.type)) throw new Error(`${label} has invalid type ${question.type}`);
  if (question.type === 'fill_blank') {
    if (!Array.isArray(question.accepted_answers) || !question.accepted_answers.length) throw new Error(`${label} needs accepted_answers`);
  } else if (question.type === 'short_answer') {
    if (!allowShort) throw new Error(`${label} cannot be short_answer`); requireText(question.expected_answer, `${label}.expected_answer`);
  } else if (!Array.isArray(question.options) || question.options.length < 2 || !Number.isInteger(question.correct_index) || question.correct_index < 0 || question.correct_index >= question.options.length) {
    throw new Error(`${label} needs valid options and correct_index`);
  }
}

export function validateQuestions(data, conceptIds) {
  if (!data || !Array.isArray(data.quiz_questions) || data.quiz_questions.length < conceptIds.length * QUESTION_TYPES.length) throw new Error('Quiz does not cover every question type for every concept');
  if (!Array.isArray(data.topic_test) || data.topic_test.length !== 10) throw new Error('Topic test must contain exactly 10 questions');
  const coverage = new Map(conceptIds.map((id) => [id, new Set()]));
  data.quiz_questions.forEach((question, index) => { validateQuestion(question, `quiz ${index + 1}`); if (!coverage.has(question.concept_id)) throw new Error(`Quiz references unknown concept ${question.concept_id}`); coverage.get(question.concept_id).add(question.type); });
  for (const [id, types] of coverage) { const missing = QUESTION_TYPES.filter((type) => !types.has(type)); if (missing.length) throw new Error(`Concept ${id} is missing: ${missing.join(', ')}`); }
  data.topic_test.forEach((question, index) => { if (!['mcq', 'assertion_reason', 'match_following', 'case_based'].includes(question.type)) throw new Error(`Test ${index + 1} must be objective`); validateQuestion(question, `test ${index + 1}`, false); if (!conceptIds.includes(question.concept_id)) throw new Error(`Test references unknown concept ${question.concept_id}`); });
  return data;
}
