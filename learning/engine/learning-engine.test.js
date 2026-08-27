/**
 * learning-engine.test.js
 * 
 * Comprehensive test suite verifying the integration of Stage Controller
 * into the generic Learning Engine across FTA and Synthetic topics.
 * Tests specifications A through P.
 */

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { createLearningEngine } from './learning-engine.js';
import { createStageController } from './stage-controller.js';

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
console.log('GENERIC LEARNING ENGINE INTEGRATION TEST SUITE');
console.log('====================================================\n');

// ----------------------------------------------------------------------------
// A. Engine loads FTA JSON
// B. Engine instantiates StageController
// ----------------------------------------------------------------------------
console.log('Test A & B: Initialization and StageController instantiation');
const engine = createLearningEngine({
  topicData: ftaData,
  currentStage: 'guided_practice'
});

const initialState = engine.getLearningState();
assert(initialState.topic_id === 'cbse10-real-numbers-fta', 'A. Engine loads FTA JSON topic metadata');
assert(initialState.student_stage === 'try', 'B1. StageController mapping returns student_stage "try"');
assert(initialState.current_stage === 'guided_practice', 'B2. Internal stage is guided_practice');

// ----------------------------------------------------------------------------
// C. Guided interaction produces a retry on wrong input
// K. Step-level input errors are distinguished from conceptual errors
// ----------------------------------------------------------------------------
console.log('\nTest C & K: Step-level input error and incorrect attempt handling');
const inputErrRes = engine.submitInteraction({
  question_id: 'g_01',
  step_id: 0,
  input_type: 'numeric',
  response: 'abc', // Malformed text in numeric input
  is_format_error: true
});
assert(inputErrRes.result === 'input_error', 'K1. Step-level malformed input returns "input_error"');
assert(inputErrRes.decision === 'retry', 'K2. Malformed input triggers retry decision');
assert(inputErrRes.allow_retry === true, 'K3. Allows retry without conceptual penalty');

const wrongRes = engine.submitInteraction({
  question_id: 'g_01',
  step_id: 0,
  divisor: 7, // Wrong divisor for 84
  quotient: 12
});
assert(wrongRes.result === 'incorrect', 'C1. Wrong mathematical step evaluated as incorrect');
assert(wrongRes.decision === 'retry', 'C2. First error produces contextual retry decision');
assert(wrongRes.error_streak === 1, 'C3. Error streak is 1');

// ----------------------------------------------------------------------------
// D. Correct Try interaction produces StageController advancement when evidence is sufficient
// ----------------------------------------------------------------------------
console.log('\nTest D: Try interaction and early advancement on sufficient evidence');
const advanceEngine = createLearningEngine({
  topicData: ftaData,
  currentStage: 'guided_practice'
});

// Submit 3 distinct successful questions covering core skills for guided_practice
advanceEngine.submitInteraction({
  question_id: 'g_01',
  is_correct: true,
  hints_used: 0,
  skill_ids: ['prime_factorisation', 'divisor_selection']
});
advanceEngine.submitInteraction({
  question_id: 'g_02',
  is_correct: true,
  hints_used: 0,
  skill_ids: ['prime_factorisation', 'division_calculation']
});
const advanceRes = advanceEngine.submitInteraction({
  question_id: 'g_03',
  is_correct: true,
  hints_used: 0,
  skill_ids: ['prime_factorisation', 'completion_condition', 'expanded_form']
});

assert(advanceRes.result === 'correct', 'D1. Third distinct question is correct');
assert(advanceRes.decision === 'advance', 'D2. StageController signals advance decision');
assert(advanceRes.current_stage === 'faded_guidance', 'D3. Engine transitioned to faded_guidance (Think)');
assert(advanceRes.student_stage === 'think', 'D4. Student facing stage is "think"');

// ----------------------------------------------------------------------------
// E. Think interaction requires learner divisor + quotient
// ----------------------------------------------------------------------------
console.log('\nTest E: Think (faded_guidance) interaction');
const thinkEngine = createLearningEngine({
  topicData: ftaData,
  currentStage: 'faded_guidance'
});
const thinkQ = thinkEngine.getNextQuestion();
assert(thinkQ.id === 'f_01', 'E1. Next question in Think stage is f_01');
assert(thinkQ.support_level === 2, 'E2. Think question has support_level 2');

const thinkStepRes = thinkEngine.submitInteraction({
  question_id: 'f_01',
  step_id: 0,
  divisor: 2,
  quotient: 36
});
assert(thinkStepRes.is_correct === true, 'E3. Learner divisor (2) and quotient (36) accepted and correct');
assert(thinkStepRes.step_completed === true, 'E4. Step completed');

// ----------------------------------------------------------------------------
// F. Build accepts structured steps
// G. Confidence bridge remains student-facing Build
// ----------------------------------------------------------------------------
console.log('\nTest F & G: Build stage and confidence bridge');
const buildEngine = createLearningEngine({
  topicData: ftaData,
  currentStage: 'constructed_solution'
});

buildEngine.submitInteraction({
  question_id: 'c_01',
  is_correct: true,
  hints_used: 0,
  skill_ids: ['prime_factorisation', 'division_calculation', 'completion_condition', 'expanded_form', 'exponential_form', 'error_analysis']
});
buildEngine.submitInteraction({
  question_id: 'c_02',
  is_correct: true,
  hints_used: 0,
  skill_ids: ['prime_factorisation', 'division_calculation', 'completion_condition', 'expanded_form', 'exponential_form', 'error_analysis']
});
const buildRes = buildEngine.submitInteraction({
  question_id: 'c_03',
  is_correct: true,
  hints_used: 0,
  skill_ids: ['prime_factorisation', 'division_calculation', 'completion_condition', 'expanded_form', 'exponential_form', 'error_analysis']
});

assert(buildRes.decision === 'advance', 'F1. Build stage completes with advance decision');
assert(buildRes.current_stage === 'independence_bridge' || buildRes.current_stage === 'confidence_bridge', 'G1. Engine advances to internal confidence bridge');
assert(buildRes.student_stage === 'build', 'G2. Student stage remains "build" (hidden bridge transition)');

// ----------------------------------------------------------------------------
// H. Independent transition works
// I. Transfer transition works
// ----------------------------------------------------------------------------
console.log('\nTest H & I: Independent solution and transfer transitions');
const bridgeEngine = createLearningEngine({
  topicData: ftaData,
  currentStage: 'independence_bridge'
});

const bridgeStep1 = bridgeEngine.submitInteraction({
  question_id: 'b_01',
  is_correct: true,
  hints_used: 0,
  skill_ids: ['prime_factorisation', 'division_calculation']
});
const bridgeStep2 = bridgeEngine.submitInteraction({
  question_id: 'b_02',
  is_correct: true,
  hints_used: 0,
  skill_ids: ['prime_factorisation', 'division_calculation']
});

assert(bridgeStep2.decision === 'advance', 'H1. Bridge advances after unassisted success');
assert(bridgeStep2.current_stage === 'independent_solution', 'H2. Advanced to independent_solution');
assert(bridgeStep2.student_stage === 'solve', 'H3. Student stage is "solve"');

const indepEngine = createLearningEngine({
  topicData: ftaData,
  currentStage: 'independent_solution'
});
indepEngine.submitInteraction({ question_id: 'i_01', is_correct: true, hints_used: 0, skill_ids: ['prime_factorisation', 'completion_condition', 'divisor_selection', 'division_calculation', 'expanded_form', 'exponential_form', 'uniqueness'] });
indepEngine.submitInteraction({ question_id: 'i_02', is_correct: true, hints_used: 0, skill_ids: ['prime_factorisation', 'completion_condition', 'divisor_selection', 'division_calculation', 'expanded_form', 'exponential_form', 'uniqueness'] });
const indepRes = indepEngine.submitInteraction({ question_id: 'i_03', is_correct: true, hints_used: 0, skill_ids: ['prime_factorisation', 'completion_condition', 'divisor_selection', 'division_calculation', 'expanded_form', 'exponential_form', 'uniqueness'] });

assert(indepRes.decision === 'start_transfer' || indepRes.decision === 'advance', 'I1. Independent solution completes and signals transfer');
assert(indepRes.current_stage === 'transfer_mastery', 'I2. Advanced to transfer_mastery');
assert(indepRes.student_stage === 'apply', 'I3. Student stage is "apply"');

// ----------------------------------------------------------------------------
// J. Targeted remediation is returned after repeated errors
// ----------------------------------------------------------------------------
console.log('\nTest J: Error streak and targeted remediation');
const errorEngine = createLearningEngine({
  topicData: ftaData,
  currentStage: 'guided_practice'
});

errorEngine.submitInteraction({ question_id: 'g_01', is_correct: false, response: 'wrong' });
const err2 = errorEngine.submitInteraction({ question_id: 'g_01', is_correct: false, response: 'wrong' });
assert(err2.decision === 'targeted_remediation', 'J1. Two consecutive errors trigger targeted_remediation');
assert(err2.remediation !== null, 'J2. Remediation payload provided');
assert(err2.error_streak === 2, 'J3. Error streak is 2');

// ----------------------------------------------------------------------------
// L. Question selection avoids duplicate completed questions
// M. Question selection considers task_type variation
// ----------------------------------------------------------------------------
console.log('\nTest L & M: Question selection and cognitive variation');
const selectEngine = createLearningEngine({
  topicData: ftaData,
  currentStage: 'guided_practice'
});

const q1 = selectEngine.getNextQuestion();
assert(q1.id === 'g_01', 'L1. First question selected is g_01');

// Mark g_01 as solved
selectEngine.submitInteraction({ question_id: 'g_01', is_correct: true });
const q2 = selectEngine.getNextQuestion();
assert(q2.id !== 'g_01', 'L2. Solved question g_01 is NOT repeated in fresh selection');
assert(q2.id === 'g_02', 'L3. Fresh question g_02 selected next');

// ----------------------------------------------------------------------------
// N. Hints do not invalidate correct evidence
// O. Mastery evidence updates correctly
// ----------------------------------------------------------------------------
console.log('\nTest N & O: Hint handling and mastery evidence updates');
const hintEngine = createLearningEngine({
  topicData: ftaData,
  currentStage: 'independent_solution'
});

const hintRes = hintEngine.requestHint({ question_id: 'i_01', hint_level: 1 });
assert(hintRes.hint_level === 1, 'N1. Level 1 hint retrieved successfully');
assert(hintRes.hint_text.length > 0, 'N2. Hint text provided');

const hintedSolveRes = hintEngine.submitInteraction({
  question_id: 'i_01',
  is_correct: true,
  hints_used: 1,
  skill_ids: ['prime_factorisation']
});
assert(hintedSolveRes.is_correct === true, 'N3. Correct answer with hint is counted as correct');

// Add unassisted second question for prime_factorisation to satisfy mastery criteria
const unassistedSolve = hintEngine.submitInteraction({
  question_id: 'i_02',
  is_correct: true,
  hints_used: 0,
  skill_ids: ['prime_factorisation']
});
const masteryState = hintEngine.getMasteryState();
assert(masteryState.skills['prime_factorisation'].mastered === true, 'O1. Prime factorisation skill marked as mastered');
assert(hintEngine.getLearningState().skills_mastered_count >= 1, 'O2. Learning state reflects mastered skill');

// ----------------------------------------------------------------------------
// P. Synthetic non-FTA topic works through the same engine
// ----------------------------------------------------------------------------
console.log('\nTest P: Synthetic topic operation (Solving Linear Equations)');
const syntheticTopic = {
  schema_version: '3.3.0',
  topic: {
    id: 'synthetic-algebra-linear-eq',
    title: 'Solving Linear Equations',
    student_journey: 'Understand → See → Try → Think → Build → Solve → Apply → Master → Retain'
  },
  skills: {
    isolate_variable: {
      id: 'isolate_variable',
      name: 'Isolating the variable',
      importance: 'core',
      mastery_evidence: {
        minimum_distinct_correct: 2,
        minimum_low_support_correct: 1,
        low_support_levels: [0, 1]
      }
    }
  },
  sequence: {
    ordered_units: ['guided_practice', 'independent_solution', 'mastery_gate']
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
        { id: 'synth_01', question: 'Solve 2x + 4 = 10', answer: 'x=3', task_type: 'inverse_operations', skill_ids: ['isolate_variable'], support_level: 3 },
        { id: 'synth_02', question: 'Solve 3x - 6 = 9', answer: 'x=5', task_type: 'inverse_operations', skill_ids: ['isolate_variable'], support_level: 3 }
      ]
    },
    independent_solution: {
      support_level: 0,
      questions: [
        { id: 'synth_indep_01', question: 'Solve 5x - 15 = 20', answer: 'x=7', task_type: 'direct_solve', skill_ids: ['isolate_variable'], support_level: 0 }
      ]
    }
  }
};

const synthEngine = createLearningEngine({
  topicData: syntheticTopic,
  currentStage: 'guided_practice'
});

assert(synthEngine.getLearningState().topic_id === 'synthetic-algebra-linear-eq', 'P1. Synthetic topic loaded');
const synthQ1 = synthEngine.getNextQuestion();
assert(synthQ1.id === 'synth_01', 'P2. Synthetic question 1 loaded');

synthEngine.submitInteraction({ question_id: 'synth_01', is_correct: true, hints_used: 0, skill_ids: ['isolate_variable'] });
const synthAdvance = synthEngine.submitInteraction({ question_id: 'synth_02', is_correct: true, hints_used: 0, skill_ids: ['isolate_variable'] });

// ----------------------------------------------------------------------------
// Q. Safety Hardening: Unsupported Interactions & Missing Response Handling
// ----------------------------------------------------------------------------
console.log('\nTest Q: Hardened Safety against unsupported or malformed interactions');
const safetyEngine = createLearningEngine({
  topicData: ftaData,
  currentStage: 'guided_practice'
});

// Q1. Missing response / invalid payload
const missingResp = safetyEngine.submitInteraction({
  question_id: 'g_01'
  // No response, no selected_index, no step_id
});
assert(missingResp.result === 'unsupported_interaction', 'Q1. Missing response returns result "unsupported_interaction"');
assert(missingResp.is_correct === false, 'Q1b. Unsupported interaction is marked not correct');
assert(safetyEngine.getLearningState().step_progress['g_01'] === undefined, 'Q1c. Unsupported interaction awards zero evidence');

// Q2. Unsupported step index out of bounds
const outOfBoundsStep = safetyEngine.submitInteraction({
  question_id: 'g_01',
  step_id: 999,
  response: '2'
});
assert(outOfBoundsStep.result === 'unsupported_interaction', 'Q2. Out of bounds step returns "unsupported_interaction"');

// Q3. Out of bounds selected_index
const outOfBoundsOption = safetyEngine.submitInteraction({
  question_id: 'g_01',
  selected_index: 99
});
assert(outOfBoundsOption.result === 'unsupported_interaction', 'Q3. Out of bounds selected_index returns "unsupported_interaction"');

// Q4. Question with no recognizable answer model
const dummyQuestionTopic = {
  schema_version: '3.3.0',
  topic: { id: 'dummy-test-topic', title: 'Dummy Topic' },
  skills: { dummy_skill: { id: 'dummy_skill', name: 'Dummy', importance: 'core' } },
  units: {
    guided_practice: {
      questions: [{ id: 'dummy_q_01', question: 'An open-ended untargeted prompt without answer' }]
    }
  }
};
const dummyEngine = createLearningEngine({ topicData: dummyQuestionTopic, currentStage: 'guided_practice' });
const dummyEval = dummyEngine.submitInteraction({ question_id: 'dummy_q_01', response: 'some arbitrary text' });
assert(dummyEval.result === 'unsupported_interaction', 'Q4. Question with no answer definition returns "unsupported_interaction"');

// ----------------------------------------------------------------------------
// R. Stepwise Dynamic Skill Resolution on Synthetic Topic
// ----------------------------------------------------------------------------
console.log('\nTest R: Stepwise dynamic skill resolution without hardcoded literals');
const stepwiseSynthTopic = {
  schema_version: '3.3.0',
  topic: { id: 'synth-fraction-addition', title: 'Adding Fractions' },
  skills: {
    find_common_denom: { id: 'find_common_denom', name: 'Find Common Denominator', importance: 'core' },
    convert_numerators: { id: 'convert_numerators', name: 'Convert Numerators', importance: 'core' },
    add_numerators: { id: 'add_numerators', name: 'Add Numerators', importance: 'core' }
  },
  sequence: { ordered_units: ['guided_practice', 'independent_solution'] },
  units: {
    guided_practice: {
      support_level: 3,
      questions: [
        {
          id: 'frac_01',
          question: 'Add 1/3 + 1/6',
          steps: [
            {
              current: '1/3 + 1/6',
              correct_divisor: 6, // common denom
              quotient: 2, // converted numerator
              divisor_skill_id: 'find_common_denom',
              quotient_skill_id: 'convert_numerators'
            }
          ]
        }
      ]
    }
  }
};

const fracEngine = createLearningEngine({ topicData: stepwiseSynthTopic, currentStage: 'guided_practice' });
// Step failure on common denom
const fracStepFail = fracEngine.submitInteraction({
  question_id: 'frac_01',
  step_id: 0,
  divisor: 9, // Wrong common denom
  quotient: 2
});
assert(fracStepFail.is_correct === false, 'R1. Wrong common denominator evaluated as incorrect');
assert(fracStepFail.diagnosed_skill_id === 'find_common_denom', 'R2. Diagnosed skill dynamically resolved as "find_common_denom"');

// Step failure on numerator conversion
const fracStepFail2 = fracEngine.submitInteraction({
  question_id: 'frac_01',
  step_id: 0,
  divisor: 6, // Correct common denom
  quotient: 5 // Wrong converted numerator
});
assert(fracStepFail2.is_correct === false, 'R3. Wrong numerator evaluated as incorrect');
assert(fracStepFail2.diagnosed_skill_id === 'convert_numerators', 'R4. Diagnosed skill dynamically resolved as "convert_numerators"');

// ----------------------------------------------------------------------------
// S. Assessment Sanitization Hardening: Zero Answer Leakage
// ----------------------------------------------------------------------------
console.log('\nTest S: Assessment Sanitization Hardening');
const sanitizeCheckEngine = createLearningEngine({ topicData: ftaData, currentStage: 'guided_practice' });
const sanitizedQ = sanitizeCheckEngine.getNextQuestion();
assert(!('correct_index' in sanitizedQ), 'S1. Sanitized question contains NO "correct_index"');
assert(!('solution' in sanitizedQ), 'S2. Sanitized question contains NO "solution"');
assert(!('answer' in sanitizedQ), 'S3. Sanitized question contains NO "answer"');
assert(!('correct_divisor' in (sanitizedQ.steps?.[0] || {})), 'S4. Sanitized step contains NO "correct_divisor"');
assert(!('quotient' in (sanitizedQ.steps?.[0] || {})), 'S5. Sanitized step contains NO "quotient"');

// ----------------------------------------------------------------------------
// T. Deterministic Fresh Question Selector
// ----------------------------------------------------------------------------
console.log('\nTest T: Deterministic Fresh Question Selector');
const deterministicEngine = createLearningEngine({ topicData: ftaData, currentStage: 'guided_practice' });
const detQ1 = deterministicEngine.getNextQuestion();
assert(detQ1.id === 'g_01', 'T1. First question is g_01');

// Mark g_01 completed
deterministicEngine.submitInteraction({ question_id: 'g_01', is_correct: true });
const detQ2 = deterministicEngine.getNextQuestion();
assert(detQ2.id === 'g_02', 'T2. Next fresh question is deterministic g_02');

// Mark g_02 completed
deterministicEngine.submitInteraction({ question_id: 'g_02', is_correct: true });
const detQ3 = deterministicEngine.getNextQuestion();
assert(detQ3.id === 'g_03', 'T3. Next fresh question is deterministic g_03');

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
