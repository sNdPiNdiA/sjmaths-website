export const QUESTION_TYPES = ['mcq', 'assertion_reason', 'true_false', 'fill_blank', 'match_following', 'case_based', 'short_answer'];

function requireText(value, label) {
  if (typeof value !== 'string' || !value.trim()) throw new Error(`${label} must be a non-empty string`);
}

function requireTextArray(value, label, minimum) {
  if (!Array.isArray(value) || value.length < minimum) throw new Error(`${label} needs at least ${minimum} items`);
  value.forEach((item, index) => requireText(item, `${label}[${index}]`));
}

export function validateContent(data) {
  if (!data || !Array.isArray(data.concepts) || data.concepts.length < 5 || data.concepts.length > 7) {
    throw new Error('Content must contain 5 to 7 concepts');
  }
  requireTextArray(data.introduction_points, 'introduction_points', 4);
  const ids = new Set();
  for (const [index, concept] of data.concepts.entries()) {
    requireText(concept.id, `concept ${index + 1} id`);
    requireText(concept.title, `concept ${index + 1} title`);
    requireText(concept.lead, `concept ${concept.id} lead`);
    if (ids.has(concept.id)) throw new Error(`Duplicate concept id: ${concept.id}`);
    ids.add(concept.id);
    requireTextArray(concept.explanation_points, `concept ${concept.id} explanation_points`, 5);
    requireTextArray(concept.key_points, `concept ${concept.id} key_points`, 4);
    requireTextArray(concept.examples, `concept ${concept.id} examples`, 2);
    requireTextArray(concept.comparison_points, `concept ${concept.id} comparison_points`, 2);
    requireTextArray(concept.common_misconceptions, `concept ${concept.id} common_misconceptions`, 2);
    requireTextArray(concept.exam_focus_points, `concept ${concept.id} exam_focus_points`, 3);
  }
  return data;
}

function validateRevision(revision, conceptIds) {
  if (!revision || !Array.isArray(revision.concept_revisions) || revision.concept_revisions.length !== conceptIds.length) {
    throw new Error('Revision must contain one entry for every concept');
  }
  const revisionIds = new Set();
  for (const revisionItem of revision.concept_revisions) {
    requireText(revisionItem.concept_id, 'revision concept_id');
    if (!conceptIds.includes(revisionItem.concept_id)) throw new Error(`Revision references unknown concept ${revisionItem.concept_id}`);
    if (revisionIds.has(revisionItem.concept_id)) throw new Error(`Duplicate revision concept ${revisionItem.concept_id}`);
    revisionIds.add(revisionItem.concept_id);
    requireText(revisionItem.title, `revision ${revisionItem.concept_id} title`);
    requireTextArray(revisionItem.pointwise_summary, `revision ${revisionItem.concept_id} pointwise_summary`, 4);
    requireTextArray(revisionItem.mnemonics, `revision ${revisionItem.concept_id} mnemonics`, 1);
    requireTextArray(revisionItem.tips, `revision ${revisionItem.concept_id} tips`, 1);
    requireTextArray(revisionItem.tricks, `revision ${revisionItem.concept_id} tricks`, 1);
    requireTextArray(revisionItem.common_traps, `revision ${revisionItem.concept_id} common_traps`, 1);
  }
  requireTextArray(revision.quick_facts, 'revision.quick_facts', 8);
  requireTextArray(revision.mnemonics, 'revision.mnemonics', 3);
  requireTextArray(revision.tips, 'revision.tips', 4);
  requireTextArray(revision.tricks, 'revision.tricks', 4);
  requireTextArray(revision.exam_traps, 'revision.exam_traps', 5);
  if (!Array.isArray(revision.comparisons) || revision.comparisons.length < 1) throw new Error('Revision comparisons are incomplete');
  revision.comparisons.forEach((comparison, index) => {
    requireText(comparison.left, `revision comparison ${index + 1} left`);
    requireText(comparison.right, `revision comparison ${index + 1} right`);
    requireTextArray(comparison.difference_points, `revision comparison ${index + 1} difference_points`, 3);
  });
  return revision;
}

function validateQuestion(question, label, allowShortAnswer = true) {
  requireText(question.id, `${label} id`);
  requireText(question.concept_id, `${label} concept_id`);
  requireText(question.type, `${label} type`);
  if (!QUESTION_TYPES.includes(question.type)) throw new Error(`${label} has unsupported type ${question.type}`);
  requireText(question.question, `${label} question`);
  requireText(question.explanation, `${label} explanation`);
  if (question.type === 'fill_blank') {
    requireTextArray(question.accepted_answers, `${label} accepted_answers`, 1);
  } else if (question.type === 'short_answer') {
    if (!allowShortAnswer) throw new Error(`${label} cannot be short_answer`);
    requireText(question.expected_answer, `${label} expected_answer`);
  } else {
    requireTextArray(question.options, `${label} options`, 2);
    if (!Number.isInteger(question.correct_index) || question.correct_index < 0 || question.correct_index >= question.options.length) {
      throw new Error(`${label} has an invalid correct_index`);
    }
  }
}

export function validateQuestions(data, conceptIds) {
  if (!data || !Array.isArray(data.quiz_questions) || data.quiz_questions.length < 30 || data.quiz_questions.length > 35) {
    throw new Error('Quiz must contain 30 to 35 questions');
  }
  const coverage = new Map(conceptIds.map((id) => [id, 0]));
  const types = new Set();
  data.quiz_questions.forEach((question, index) => {
    validateQuestion(question, `quiz question ${index + 1}`);
    if (!coverage.has(question.concept_id)) throw new Error(`Quiz question ${question.id} references an unknown concept`);
    coverage.set(question.concept_id, coverage.get(question.concept_id) + 1);
    types.add(question.type);
  });
  for (const [conceptId, count] of coverage) if (count < 4) throw new Error(`Concept ${conceptId} needs at least 4 quiz questions`);
  const missingTypes = QUESTION_TYPES.filter((type) => !types.has(type));
  if (missingTypes.length) throw new Error(`Quiz is missing question types: ${missingTypes.join(', ')}`);
  return data;
}

export function validateRevisionAndTest(data, conceptIds) {
  validateRevision(data?.revision, conceptIds);
  if (!Array.isArray(data?.topic_test) || data.topic_test.length !== 10) throw new Error('Mini test must contain exactly 10 questions');
  data.topic_test.forEach((question, index) => {
    if (!['mcq', 'assertion_reason', 'true_false', 'match_following', 'case_based'].includes(question.type)) {
      throw new Error(`Mini-test question ${index + 1} must be objective`);
    }
    validateQuestion(question, `mini-test question ${index + 1}`, false);
    if (!conceptIds.includes(question.concept_id)) throw new Error(`Mini-test question ${question.id} references an unknown concept`);
  });
  return data;
}
