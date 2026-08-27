/**
 * stage-controller.test.js
 * 
 * Comprehensive test suite for the generic, topic-agnostic Stage Controller.
 * Tests all 22 required behavioral contracts across FTA and synthetic topics.
 */

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import {
  StageController,
  createStageController,
  normalizeStage,
  getStudentStageLabel,
  getStudentFacingTitle,
  INTERNAL_STAGES,
  STUDENT_TO_INTERNAL_STAGE,
  INTERNAL_TO_STUDENT_STAGE
} from './stage-controller.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const ftaPath = path.join(__dirname, '../data/class-10/mathematics/chapter-1-real-numbers/fta.json');
const ftaData = JSON.parse(fs.readFileSync(ftaPath, 'utf8'));

let totalTests = 0;
let passedTests = 0;
let failedTests = 0;

function assert(condition, message) {
  totalTests += 1;
  if (condition) {
    passedTests += 1;
    console.log(`  [PASS] ${message}`);
  } else {
    failedTests += 1;
    console.error(`  [FAIL] ${message}`);
  }
}

console.log('====================================================');
console.log('GENERIC STAGE CONTROLLER TEST SUITE');
console.log('====================================================\n');

// ----------------------------------------------------------------------------
// 1. FTA Try stage starts correctly.
// ----------------------------------------------------------------------------
console.log('Test 1: FTA Try stage initialization');
const tryController = createStageController({
  topicData: ftaData,
  studentState: {},
  currentStage: 'try'
});
assert(tryController.getCurrentStage() === 'guided_practice', '1. FTA Try stage starts as internal guided_practice');
assert(tryController.getStudentFacingStage() === 'try', '1b. Student facing stage is "try"');
assert(tryController.getStudentFacingTitle() === 'Try', '1c. Student facing title is "Try"');

// ----------------------------------------------------------------------------
// 2. Try requires divisor choice.
// 3. Try requires learner quotient calculation.
// ----------------------------------------------------------------------------
console.log('\nTest 2 & 3: Try stage interaction contracts in topicData');
const tryUnit = ftaData.units.guided_practice;
assert(tryUnit.support.ask_for_divisor === true && tryUnit.support.divisor_input === 'options', '2. Try provides divisor options / choices for student decision');
assert(tryUnit.support.ask_for_quotient === true && tryUnit.support.quotient_input === 'numeric', '3. Try requires learner quotient calculation');
assert(tryUnit.support.do_not_calculate_for_learner === true, '3b. System does NOT calculate quotient for learner');

// ----------------------------------------------------------------------------
// 4. Think requires learner divisor selection.
// 5. Think has lower support than Try.
// ----------------------------------------------------------------------------
console.log('\nTest 4 & 5: Think stage contracts');
const thinkUnit = ftaData.units.faded_guidance;
assert(thinkUnit.support.ask_for_divisor === true && thinkUnit.support.divisor_input === 'numeric', '4. Think requires learner divisor input as numeric');
assert(thinkUnit.support.next_step_prompt === false, '4b. Think removes next_step_prompt (learner decides next step)');
assert(thinkUnit.support_level < tryUnit.support_level, '5. Think (support_level 2) has lower support than Try (support_level 3)');

// ----------------------------------------------------------------------------
// 6. Build removes most scaffolding.
// ----------------------------------------------------------------------------
console.log('\nTest 6: Build stage contracts');
const buildUnit = ftaData.units.constructed_solution;
assert(buildUnit.support_level === 1, '6. Build support level is 1 (minimal scaffold)');
assert(buildUnit.support.solution_framework === 'minimal', '6b. Build uses minimal framework');
assert(buildUnit.support.student_creates_steps === true && buildUnit.support.final_answer_required === true, '6c. Student constructs complete solution and final answer');

// ----------------------------------------------------------------------------
// 7. Confidence bridge exists internally but is not student-visible.
// ----------------------------------------------------------------------------
console.log('\nTest 7: Hidden internal confidence bridge');
const bridgeController = createStageController({
  topicData: ftaData,
  studentState: {
    attempts: [
      { question_id: 'c_01', correct: true, hints_used: 0, stage: 'constructed_solution', skill_ids: ['prime_factorisation', 'division_calculation', 'completion_condition', 'expanded_form', 'exponential_form', 'error_analysis'] },
      { question_id: 'c_02', correct: true, hints_used: 0, stage: 'constructed_solution', skill_ids: ['prime_factorisation', 'division_calculation', 'completion_condition', 'expanded_form', 'exponential_form', 'error_analysis'] },
      { question_id: 'c_03', correct: true, hints_used: 0, stage: 'constructed_solution', skill_ids: ['prime_factorisation', 'division_calculation', 'completion_condition', 'expanded_form', 'exponential_form', 'error_analysis'] }
    ]
  },
  currentStage: 'constructed_solution'
});
const bridgeDecision = bridgeController.getNextDecision();
assert(bridgeDecision.to_stage === 'independence_bridge' || bridgeDecision.to_stage === 'confidence_bridge', '7. Internal transition advances to confidence/independence bridge');
assert(bridgeDecision.student_stage === 'build', '7b. Confidence bridge is NOT exposed to student; label remains "build"');
assert(ftaData.sequence.internal_only_units.includes('independence_bridge'), '7c. Topic data marks independence_bridge as internal_only');

// ----------------------------------------------------------------------------
// 8. Correct answer with Hint 1 still provides evidence.
// ----------------------------------------------------------------------------
console.log('\nTest 8: Hint 1 evidence weight');
const hint1State = {
  attempts: [
    { question_id: 'q_h1', correct: true, hints_used: 1, stage: 'guided_practice', skill_ids: ['prime_factorisation'] }
  ]
};
const hint1Controller = createStageController({ topicData: ftaData, studentState: hint1State, currentStage: 'guided_practice' });
const hint1Evidence = hint1Controller.evaluateStage('guided_practice');
assert(hint1Evidence.distinctCorrect === 1, '8. Correct answer with Hint 1 counts as distinct correct');
assert(hint1Evidence.distinctLowHintCorrect === 1, '8b. Hint 1 counts towards low-hint evidence');

// ----------------------------------------------------------------------------
// 9. Hint 3 does not count as full mastery evidence.
// ----------------------------------------------------------------------------
console.log('\nTest 9: Hint 3 evidence weight');
const hint3State = {
  attempts: [
    { question_id: 'q_h3', correct: true, hints_used: 3, stage: 'independent_solution', support_level: 0, skill_ids: ['prime_factorisation'] }
  ]
};
const hint3Controller = createStageController({ topicData: ftaData, studentState: hint3State, currentStage: 'independent_solution' });
const hint3Skills = hint3Controller.evaluateSkills();
assert(hint3Skills.skills['prime_factorisation'].lowSupportCount === 0, '9. Hint 3 is practice evidence and does not count as qualifying low-support unassisted mastery');
assert(hint3Skills.skills['prime_factorisation'].mastered === false, '9b. Skill is NOT mastered from Hint 3 attempt alone');

// ----------------------------------------------------------------------------
// 10. One wrong answer does not regress the stage.
// ----------------------------------------------------------------------------
console.log('\nTest 10: Single error handling');
const singleErrorState = {
  error_streak: 1,
  attempts: [
    { question_id: 'g_01', correct: true, stage: 'guided_practice', skill_ids: ['prime_factorisation'] },
    { question_id: 'g_02', correct: false, stage: 'guided_practice', skill_ids: ['divisor_selection'] }
  ]
};
const singleErrorController = createStageController({ topicData: ftaData, studentState: singleErrorState, currentStage: 'guided_practice' });
const singleErrorDecision = singleErrorController.getNextDecision({ lastAttemptCorrect: false });
assert(singleErrorDecision.decision === 'retry', '10. Single error returns decision "retry"');
assert(singleErrorDecision.to_stage === 'guided_practice', '10b. Learner remains in current stage without regression');

// ----------------------------------------------------------------------------
// 11. Two related errors trigger diagnosis.
// ----------------------------------------------------------------------------
console.log('\nTest 11: Two consecutive errors diagnosis');
const twoErrorState = {
  error_streak: 2,
  attempts: [
    { question_id: 'g_01', correct: false, stage: 'guided_practice', skill_ids: ['divisor_selection'] },
    { question_id: 'g_02', correct: false, stage: 'guided_practice', skill_ids: ['divisor_selection'] }
  ]
};
const twoErrorController = createStageController({ topicData: ftaData, studentState: twoErrorState, currentStage: 'guided_practice' });
const twoErrorDecision = twoErrorController.getNextDecision({ lastAttemptCorrect: false, failedStepSkillId: 'divisor_selection' });
assert(twoErrorDecision.decision === 'targeted_remediation', '11. Two related errors trigger targeted_remediation');
assert(twoErrorDecision.diagnosed_skill_id === 'divisor_selection', '11b. Diagnosed skill is correctly identified');
assert(twoErrorDecision.allow_retry === true, '11c. Allows retry at current stage');

// ----------------------------------------------------------------------------
// 12. Three+ related errors trigger targeted remediation.
// ----------------------------------------------------------------------------
console.log('\nTest 12: Three or more errors remediation');
const threeErrorState = {
  error_streak: 3,
  attempts: [
    { question_id: 'g_01', correct: false, stage: 'guided_practice', skill_ids: ['division_calculation'] },
    { question_id: 'g_02', correct: false, stage: 'guided_practice', skill_ids: ['division_calculation'] },
    { question_id: 'g_03', correct: false, stage: 'guided_practice', skill_ids: ['division_calculation'] }
  ]
};
const threeErrorController = createStageController({ topicData: ftaData, studentState: threeErrorState, currentStage: 'guided_practice' });
const threeErrorDecision = threeErrorController.getNextDecision({ lastAttemptCorrect: false, failedStepSkillId: 'division_calculation' });
assert(threeErrorDecision.decision === 'targeted_remediation', '12. Three errors trigger targeted_remediation micro-practice');
assert(threeErrorDecision.remediation_type === 'targeted_micro_practice', '12b. Remediation type is targeted_micro_practice');

// ----------------------------------------------------------------------------
// 13. Input error is not treated as conceptual failure.
// ----------------------------------------------------------------------------
console.log('\nTest 13: Input / format error policy');
const inputErrorController = createStageController({ topicData: ftaData, studentState: {}, currentStage: 'guided_practice' });
const inputErrorDecision = inputErrorController.getNextDecision({ isFormatError: true, reason_type: 'input_error' });
assert(inputErrorDecision.decision === 'retry', '13. Malformed input returns decision "retry"');
assert(inputErrorDecision.reason_type === 'input_error', '13b. Reason type is classified as input_error (not math misconception)');

// ----------------------------------------------------------------------------
// 14. Duplicate skill IDs are normalized.
// 15. One question can contribute evidence to multiple skills.
// ----------------------------------------------------------------------------
console.log('\nTest 14 & 15: Skill deduplication and multi-skill evidence');
const multiSkillState = {
  attempts: [
    {
      question_id: 'multi_q1',
      correct: true,
      hints_used: 0,
      stage: 'guided_practice',
      support_level: 1,
      // Duplicate skill IDs included in raw array
      skill_ids: ['prime_factorisation', 'divisor_selection', 'prime_factorisation', 'division_calculation']
    }
  ]
};
const multiSkillController = createStageController({ topicData: ftaData, studentState: multiSkillState, currentStage: 'guided_practice' });
const multiSkillEvidence = multiSkillController.evaluateStage('guided_practice');
assert(multiSkillEvidence.coreSkillsEvidenced['prime_factorisation'] === 1, '14. Duplicate skill IDs normalized (counted once per question)');
assert(multiSkillEvidence.coreSkillsEvidenced['divisor_selection'] === 1, '15. Question contributed evidence to divisor_selection');
assert(multiSkillEvidence.coreSkillsEvidenced['division_calculation'] === 1, '15b. Same question contributed evidence to division_calculation');

// ----------------------------------------------------------------------------
// 16. Strong learner can advance early.
// 17. Weak learner receives additional practice.
// ----------------------------------------------------------------------------
console.log('\nTest 16 & 17: Adaptive pacing (strong vs struggling learner)');
const strongState = {
  attempts: [
    { question_id: 'g_01', correct: true, hints_used: 0, stage: 'guided_practice', skill_ids: ['prime_factorisation', 'divisor_selection'] },
    { question_id: 'g_02', correct: true, hints_used: 0, stage: 'guided_practice', skill_ids: ['prime_factorisation', 'division_calculation'] },
    { question_id: 'g_03', correct: true, hints_used: 0, stage: 'guided_practice', skill_ids: ['prime_factorisation', 'completion_condition', 'expanded_form'] }
  ]
};
const strongController = createStageController({ topicData: ftaData, studentState: strongState, currentStage: 'guided_practice' });
assert(strongController.canAdvance('guided_practice') === true, '16. Strong learner with sufficient distinct evidence can advance early');
const strongDecision = strongController.getNextDecision();
assert(strongDecision.decision === 'advance' && strongDecision.to_stage === 'faded_guidance', '16b. Strong learner advances to faded_guidance (Think)');

const strugglingState = {
  attempts: [
    { question_id: 'g_01', correct: true, hints_used: 0, stage: 'guided_practice', skill_ids: ['prime_factorisation'] },
    { question_id: 'g_02', correct: false, hints_used: 2, stage: 'guided_practice', skill_ids: ['divisor_selection'] },
    { question_id: 'g_03', correct: false, hints_used: 2, stage: 'guided_practice', skill_ids: ['division_calculation'] }
  ]
};
const strugglingController = createStageController({ topicData: ftaData, studentState: strugglingState, currentStage: 'guided_practice' });
assert(strugglingController.canAdvance('guided_practice') === false, '17. Struggling learner cannot advance with low accuracy/coverage');
const strugglingDecision = strugglingController.getNextDecision();
assert(strugglingDecision.decision === 'extend_practice' || strugglingDecision.decision === 'stay', '17b. Struggling learner receives extended practice in current stage');

// ----------------------------------------------------------------------------
// 18. Difficulty does not automatically increase when support decreases.
// ----------------------------------------------------------------------------
console.log('\nTest 18: Dimension separation (difficulty vs support)');
const safeDims = tryController.safelyAdjustDimensions(
  { difficulty: 'medium', support_level: 3 },
  { accuracy: 1.0, consecutiveSuccesses: 2, unassisted: true }
);
assert(safeDims.support_level === 2, '18. Support level decreased from 3 to 2');
assert(safeDims.difficulty === 'medium', '18b. Difficulty remained unchanged at "medium"');
assert(safeDims.applied_rule === 'safe_support_reduction', '18c. Applied rule is safe_support_reduction');

// ----------------------------------------------------------------------------
// 19. Transfer task types come from topicData.
// ----------------------------------------------------------------------------
console.log('\nTest 19: Transfer task types dynamic resolution');
const applyController = createStageController({ topicData: ftaData, studentState: {}, currentStage: 'transfer_mastery' });
const recTypes = applyController._getRecommendedTaskTypes('transfer_mastery');
assert(recTypes.length > 0, '19. Transfer task types dynamically extracted from topicData');
assert(recTypes.includes('divisibility_reasoning') || recTypes.includes('uniqueness_reasoning') || recTypes.includes('direct_factorisation'), '19b. Topic-defined transfer task types present');

// ----------------------------------------------------------------------------
// 20. Mastery is controlled by topicData rather than FTA constants.
// ----------------------------------------------------------------------------
console.log('\nTest 20: Mastery requirements from topicData');
const fullMasteryState = {
  attempts: [
    { question_id: 'i_01', correct: true, hints_used: 0, stage: 'independent_solution', support_level: 0, skill_ids: ['prime_factorisation', 'completion_condition'] },
    { question_id: 'i_02', correct: true, hints_used: 0, stage: 'independent_solution', support_level: 0, skill_ids: ['prime_factorisation', 'divisor_selection'] },
    { question_id: 'i_03', correct: true, hints_used: 0, stage: 'independent_solution', support_level: 0, skill_ids: ['division_calculation', 'expanded_form'] },
    { question_id: 'i_04', correct: true, hints_used: 0, stage: 'independent_solution', support_level: 0, skill_ids: ['exponential_form', 'uniqueness'] },
    { question_id: 'i_05', correct: true, hints_used: 0, stage: 'independent_solution', support_level: 0, skill_ids: ['incomplete_factorisation', 'error_analysis', 'reverse_factorisation', 'divisibility_reasoning'] },
    { question_id: 't_01', correct: true, hints_used: 0, stage: 'transfer_mastery', support_level: 0, skill_ids: ['prime_factorisation', 'divisor_selection', 'division_calculation', 'completion_condition', 'expanded_form', 'exponential_form', 'uniqueness', 'incomplete_factorisation', 'error_analysis', 'reverse_factorisation', 'divisibility_reasoning'] }
  ]
};
const fullMasteryController = createStageController({ topicData: ftaData, studentState: fullMasteryState, currentStage: 'transfer_mastery' });
const skillsEvaluation = fullMasteryController.evaluateSkills();
assert(skillsEvaluation.allCoreMastered === true, '20. Core skills mastery evaluated according to topicData criteria');

// ----------------------------------------------------------------------------
// 21. Retrieval does not undo mastery.
// ----------------------------------------------------------------------------
console.log('\nTest 21: Delayed retrieval maintains mastery state');
const retrievalState = {
  mastery_gate_passed: true,
  attempts: fullMasteryState.attempts
};
const retrievalController = createStageController({ topicData: ftaData, studentState: retrievalState, currentStage: 'delayed_retrieval' });
const progressState = retrievalController.getProgressState();
assert(progressState.is_topic_mastered === true, '21. Progress reports topic is mastered during delayed retrieval');
const retrievalDecision = retrievalController.getNextDecision({ isRetrievalDue: true });
assert(retrievalDecision.decision === 'retrieval_due', '21b. Decision is retrieval_due');
assert(retrievalDecision.message === "Let's wake this skill up.", '21c. Retrieval message is supportive maintenance');

// ----------------------------------------------------------------------------
// 22. Controller can instantiate using a synthetic non-FTA topic.
// ----------------------------------------------------------------------------
console.log('\nTest 22: Synthetic non-FTA topic operation');
const syntheticTopic = {
  schema_version: '3.3.0',
  topic: {
    id: 'synthetic-linear-equations',
    title: 'Solving Linear Equations',
    student_journey: 'Understand → See → Try → Think → Build → Solve → Apply → Master → Retain'
  },
  skills: {
    isolate_variable: {
      id: 'isolate_variable',
      name: 'Isolating Variable',
      importance: 'core',
      mastery_evidence: {
        minimum_distinct_correct: 2,
        minimum_low_support_correct: 1,
        low_support_levels: [0, 1]
      }
    }
  },
  sequence: {
    ordered_units: ['concept_learning', 'guided_practice', 'independent_solution', 'mastery_gate']
  },
  units: {
    guided_practice: {
      support_level: 3,
      advancement_requirements: {
        minimum_questions: 2,
        accuracy: 0.8,
        minimum_evidence_per_core_skill: 1
      },
      questions: [
        { id: 'synth_01', task_type: 'balance_method', skill_ids: ['isolate_variable'], support_level: 3 },
        { id: 'synth_02', task_type: 'balance_method', skill_ids: ['isolate_variable'], support_level: 3 }
      ]
    }
  }
};

const syntheticStudentState = {
  attempts: [
    { question_id: 'synth_01', correct: true, hints_used: 0, stage: 'guided_practice', skill_ids: ['isolate_variable'] },
    { question_id: 'synth_02', correct: true, hints_used: 0, stage: 'guided_practice', skill_ids: ['isolate_variable'] }
  ]
};

const synthController = createStageController({
  topicData: syntheticTopic,
  studentState: syntheticStudentState,
  currentStage: 'guided_practice'
});

assert(synthController.getCurrentStage() === 'guided_practice', '22. Synthetic controller instantiates with generic topic');
assert(synthController.canAdvance('guided_practice') === true, '22b. Synthetic topic canAdvance evaluates correctly');
const synthDecision = synthController.getNextDecision();
assert(synthDecision.decision === 'advance' && synthDecision.to_stage === 'independent_solution', '22c. Synthetic controller advances to next configured unit');

// ----------------------------------------------------------------------------
// Summary
// ----------------------------------------------------------------------------
console.log('\n====================================================');
console.log(`TOTAL TESTS: ${totalTests}`);
console.log(`PASSED:      ${passedTests}`);
console.log(`FAILED:      ${failedTests}`);
console.log('====================================================');

if (failedTests > 0) {
  process.exit(1);
}
