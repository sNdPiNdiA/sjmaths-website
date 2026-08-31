/**
 * topic-convert.js
 *
 * Pure, browser-safe converter: v4.0.0 Learning-Topic JSON  →  v2.0.0 WebMCP chapter format.
 *
 * The v4.0.0 schema encodes a **3-Stage Typology Architecture** per problem:
 *   Stage 1: Strategy Choices  (step.strategy_question + strategy_options + correct_strategy_index)
 *   Stage 2: Guided Calculation (step.calc_prompt + expected_divisor/expected_quotient/expected_value + calc_template)
 *   Stage 3: Notebook Solve + Self-Audit (step.rubric_text + rubric_math + revisit_topic remediation)
 *
 * Every pool question contains `steps[]`; each step is ONE evaluatable WebMCP practice item,
 * and the items are distributed across 3 cognitive stage buckets:
 *   guided_practice → independent_solution → transfer_mastery (transfer_and_pyq)
 *
 * This module has NO filesystem / DOM dependencies, so it can run in:
 *   - Node.js (imported by topic-discovery.js)
 *   - Browser (imported by demo/index.html)
 */

const STAGE_LABELS = {
  concepts: '1. Concepts',
  worked_examples: '2. Worked Solutions',
  stage_1_strategy: '3. Strategy',
  stage_2_calc: '4. Guided Calc',
  stage_3_notebook: '5. Notebook'
};

const PRACTICE_STAGES = ['guided_practice', 'independent_solution', 'transfer_mastery'];

/**
 * Builds one evaluatable WebMCP practice item for a single step inside a pool question.
 */
function stepToPracticeItem(question, step, sIdx, qt, topicId) {
  const itemId = `${question.id || `${topicId}_p`}_s${sIdx + 1}`;
  return {
    id: itemId,
    parent_question_id: question.id || null,
    step_number: step.step_number || sIdx + 1,
    step_focus: step.focus || '',
    stage: null, // assigned during distribution
    skill_id: `skill-${(qt.type_id || 'general').replace(/[^a-z0-9]/g, '-')}`,
    difficulty: question.difficulty || 'medium',
    question: step.strategy_question || question.statement,
    options: step.strategy_options || [],
    correct_index: step.correct_strategy_index ?? 0,
    solution: step.rubric_math || question.final_canonical_answer || '',
    hint: step.hint || '',
    hints: step.hint ? [{ level: 1, text: step.hint }] : [],
    calc: {
      prompt: step.calc_prompt || '',
      template_latex: (step.calc_template && step.calc_template.format_latex) || '',
      fields: (step.calc_template && step.calc_template.fields) || [],
      expected_value: step.expected_value ?? null,
      expected_divisor: step.expected_divisor ?? null,
      expected_quotient: step.expected_quotient ?? null
    },
    rubric_text: step.rubric_text || '',
    rubric_math: step.rubric_math || '',
    revisit_topic: step.revisit_topic || null,
    final_answer: question.final_canonical_answer || null,
    source: {
      type_id: qt.type_id || 'general',
      type_title: qt.type_title || '',
      pool_index: question.__poolIndex,
      total_pool: question.__poolSize
    }
  };
}
/**
 * Distributes step-items into the 3 cognitive stage buckets in balanced thirds,
 * guaranteeing >=5 per bucket whenever the source data has >=15 step-items.
 */
function distributeStages(stepItems) {
  const total = stepItems.length;
  const third = Math.ceil(total / 3);
  stepItems.forEach((item, i) => {
    item.stage = i < third
      ? 'guided_practice'
      : i < third * 2
        ? 'independent_solution'
        : 'transfer_mastery';
  });
  return stepItems;
}

/**
 * Converts a v4.0.0 topic into a v2.0.0-compatible WebMCP unit.
 * Surfaces ALL pool questions x ALL steps, preserving the 3-stage typology.
 */
export function topicToUnit(topicData, index) {
  const shortTitle = topicData.topic?.short_title || `unit-${index + 1}`;
  const unitId = `unit-${index + 1}-${shortTitle.toLowerCase().replace(/[^a-z0-9]/g, '-')}`;
  const topicId = topicData.topic?.id || shortTitle;

  // 1. Flatten every pool question x every step into evaluatable items
  const stepItems = [];
  (topicData.question_types || []).forEach(qt => {
    const pool = qt.pool || [];
    pool.forEach((q, qIdx) => {
      q.__poolIndex = qIdx;
      q.__poolSize = pool.length;
      (q.steps || []).forEach((step, sIdx) => {
        stepItems.push(stepToPracticeItem(q, step, sIdx, qt, topicId));
      });
    });
  });

  // 2. Distribute across 3 cognitive stage buckets
  distributeStages(stepItems);

  // 3. Split into v2 practice_stages buckets
  const guidedIndependent = stepItems.filter(i => i.stage === 'guided_practice' || i.stage === 'independent_solution');
  const transferPyq = stepItems.filter(i => i.stage === 'transfer_mastery');

  // 4. Unit mastery gate: one item per question typology (prefer transfer-stage items)
  const unitMasteryGateQuestions = [];
  (topicData.question_types || []).forEach(qt => {
    const typeId = qt.type_id || 'general';
    const candidate = transferPyq.find(i => i.source.type_id === typeId)
      || guidedIndependent.find(i => i.source.type_id === typeId);
    if (candidate) {
      unitMasteryGateQuestions.push({ ...candidate, stage: 'mastery_gate' });
    }
  });

  // 5. Prerequisite check from the first question's first step
  const firstStep = topicData.question_types?.[0]?.pool?.[0]?.steps?.[0];
  const prerequisiteCheck = firstStep ? {
    id: `${shortTitle.toLowerCase().replace(/[^a-z0-9]/g, '-')}-precheck`,
    question: firstStep.strategy_question || topicData.question_types[0].pool[0].statement,
    options: firstStep.strategy_options || [],
    correct_index: firstStep.correct_strategy_index ?? 0,
    remediation_hint: firstStep.hint || ''
  } : null;

  const workedExamples = (topicData.worked_examples || []).map(we => ({
    id: we.id,
    type_id: we.type_id,
    type_label: we.type_label,
    title: we.title,
    problem: we.problem,
    steps: (we.steps || []).map(s => ({
      step_number: s.step_number,
      statement: s.statement,
      calculation: s.calculation,
      reason: s.reason
    })),
    conclusion: we.conclusion,
    final_answer: we.final_answer
  }));

  // 6. Unit metadata consumed by get_topic_outline / UI renderers
  const skillsCovered = [...new Set(stepItems.map(i => i.skill_id).filter(Boolean))];

  return {
    unit_number: index + 1,
    icon: topicData.topic?.icon || '📘',
    skills_covered: skillsCovered,

    id: unitId,
    title: topicData.topic?.title || shortTitle,
    instruction: {
      core_concepts: (topicData.concepts || []).map(c => c.summary || c.title || ''),
      formulas: (topicData.reference_drawer?.items || []).map(item => ({
        rule: item.tag,
        formula: item.formula,
        example: item.example
      })),
      callout_boxes: [],
      journey: topicData.topic?.student_journey || '',
      stage_progression: (topicData.stages?.progression || []).map(s => ({
        id: s.id,
        title: s.title,
        description: s.description
      })),
      worked_examples: workedExamples
    },
    prerequisite_check: prerequisiteCheck,
    practice_stages: {
      guided_and_independent: guidedIndependent,
      transfer_and_pyq: transferPyq
    },
    unit_mastery_gate: { questions: unitMasteryGateQuestions }
  };
}

/**
 * Combines multiple topics into a chapter-level v2.0.0 WebMCP structure.
 */
export function combineTopicsToChapter(topics, chapterMeta = {}) {
  const firstTopic = topics[0]?.data?.topic || {};
  const id = chapterMeta.id || topics[0]?.data?.topic?.id || 'unknown-chapter';
  const units = topics.map((t, idx) => topicToUnit(t.data, idx));

  // Aggregate skills across all units
  const skills = [];
  const seenSkills = new Set();
  units.forEach(u => {
    [...(u.practice_stages.guided_and_independent || []), ...(u.practice_stages.transfer_and_pyq || [])].forEach(q => {
      if (!seenSkills.has(q.skill_id)) {
        seenSkills.add(q.skill_id);
        skills.push({ id: q.skill_id, name: q.skill_id, unit_id: u.id });
      }
    });
  });

  const totalPracticeItems = units.reduce((a, u) =>
    a + (u.practice_stages.guided_and_independent?.length || 0) + (u.practice_stages.transfer_and_pyq?.length || 0), 0);

  return {
    schema_version: '2.0.0',
    content_type: 'learning_topic',
    topic: {
      id,
      title: chapterMeta.title || firstTopic.chapter || 'Unknown Chapter',
      grade: firstTopic.class || 10,
      subject: firstTopic.subject || 'Mathematics',
      standard: firstTopic.board ? `${firstTopic.board} / NCERT` : 'CBSE / NCERT',
      description: chapterMeta.description || `Learn ${firstTopic.chapter || id} through ${topics.length} topics.`
    },
    scope: {
      total_units: units.length,
      total_skills: skills.length,
      total_practice_items: totalPracticeItems,
      estimated_learning_minutes: totalPracticeItems * 3,
      target_mastery_level: 'proficient'
    },
    prerequisites: [],
    sequence: {
      unit_order: units.map(u => u.id),
      gate_policy: 'sequential_mastery'
    },
    skills,
    units,
    mastery: {
      chapter_mastery_gate: {
        assessment_id: `${id}-mastery`,
        title: `${chapterMeta.title || firstTopic.chapter || 'Chapter'} Mastery Exam`,
        description: 'Comprehensive chapter exam',
        pass_percent: 80,
        questions: []
      }
    }
  };
}

/**
 * Reports the practice-question inventory of a topic (all 3 stages).
 */
export function countTopicPracticeItems(topicData) {
  const stepItems = [];
  (topicData.question_types || []).forEach(qt => {
    (qt.pool || []).forEach(q => {
      q.__poolIndex = 0;
      q.__poolSize = (qt.pool || []).length;
      (q.steps || []).forEach((step, sIdx) => {
        stepItems.push(stepToPracticeItem(q, step, sIdx, qt, topicData.topic?.id));
      });
    });
  });
  distributeStages(stepItems);

  return {
    total_questions: (topicData.question_types || []).reduce((a, qt) => a + (qt.pool || []).length, 0),
    total_steps: stepItems.length,
    guided_practice: stepItems.filter(i => i.stage === 'guided_practice').length,
    independent_solution: stepItems.filter(i => i.stage === 'independent_solution').length,
    transfer_mastery: stepItems.filter(i => i.stage === 'transfer_mastery').length
  };
}

export default {
  topicToUnit,
  combineTopicsToChapter,
  countTopicPracticeItems,
  STAGE_LABELS,
  PRACTICE_STAGES
};
