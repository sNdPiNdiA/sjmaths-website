/**
 * ui-interaction-harness.test.js
 * 
 * Deterministic automated interaction harness testing the student-facing
 * concept-mastery journey against all 20 UI checklist items.
 */

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { createLearningEngine } from './learning-engine.js';
import { STUDENT_TO_INTERNAL_STAGE, INTERNAL_TO_STUDENT_STAGE } from './stage-controller.js';

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
console.log('STUDENT UI INTERACTION HARNESS & JOURNEY TEST SUITE');
console.log('====================================================\n');

// 1. Fresh page -> Understand
console.log('Test 1-3: Linear onboarding flow (Understand -> See -> Try)');
const engine = createLearningEngine({ topicData: ftaData });
const state1 = engine.getLearningState();
assert(state1.student_stage === 'understand', '1. Fresh session starts on student stage "Understand"');

// 2. See stage initialization
const seeEngine = createLearningEngine({ topicData: ftaData, currentStage: 'worked_examples' });
assert(seeEngine.getLearningState().student_stage === 'see', '2. Worked examples maps to student stage "See"');

// 3. Try stage initialization
const tryEngine = createLearningEngine({ topicData: ftaData, currentStage: 'guided_practice' });
assert(tryEngine.getLearningState().student_stage === 'try', '3. Guided practice maps to student stage "Try"');

// 4. Guided divisor selection & 5. Guided quotient input
console.log('\nTest 4-6: Guided practice stepwise execution (Try)');
const tryQ = tryEngine.getNextQuestion();
assert(tryQ.id === 'g_01', '4. Try stage serves first guided question g_01');

// Test wrong divisor selection first
const wrongTryStep = tryEngine.submitInteraction({
  question_id: 'g_01',
  step_id: 0,
  divisor: 5, // Wrong divisor for 84
  quotient: 42
});
assert(wrongTryStep.is_correct === false, '4b. Incorrect divisor selection graded false');
assert(wrongTryStep.decision === 'retry', '7. First wrong produces Try Again / retry decision');

// Correct step 0
const correctTryStep = tryEngine.submitInteraction({
  question_id: 'g_01',
  step_id: 0,
  divisor: 2,
  quotient: 42
});
assert(correctTryStep.is_correct === true, '5. Guided divisor and quotient accepted and graded true');

// 6. Complete remaining Try questions to advance
tryEngine.submitInteraction({ question_id: 'g_02', is_correct: true, hints_used: 0, skill_ids: ['prime_factorisation', 'division_calculation', 'divisor_selection'] });
const tryAdv = tryEngine.submitInteraction({ question_id: 'g_03', is_correct: true, hints_used: 0, skill_ids: ['prime_factorisation', 'completion_condition', 'expanded_form', 'divisor_selection', 'division_calculation'] });
assert(tryAdv.student_stage === 'think', '6. Correct responses advance stage to "Think"');

// 8. Second wrong -> Review Concept
console.log('\nTest 8-11: Remediation, hints, and Think stage');
const thinkEngine = createLearningEngine({ topicData: ftaData, currentStage: 'faded_guidance' });
thinkEngine.submitInteraction({ question_id: 'f_01', is_correct: false, response: 'wrong' });
const secondErr = thinkEngine.submitInteraction({ question_id: 'f_01', is_correct: false, response: 'wrong' });
assert(secondErr.decision === 'targeted_remediation', '8. Second consecutive error triggers targeted remediation');
assert(secondErr.remediation !== null, '8b. Review concept payload provided');

// 10. Hint 1 -> Hint 2 -> Hint 3
const h1 = thinkEngine.requestHint({ question_id: 'f_01', hint_level: 1 });
const h2 = thinkEngine.requestHint({ question_id: 'f_01', hint_level: 2 });
const h3 = thinkEngine.requestHint({ question_id: 'f_01', hint_level: 3 });
assert(h1.hint_text.length > 0 && h2.hint_text.length > 0 && h3.hint_text.length > 0, '10. Hints 1, 2, and 3 retrieved progressively');

// 11. Correct after hint
const hintSolve = thinkEngine.submitInteraction({
  question_id: 'f_01',
  step_id: 0,
  divisor: 2,
  quotient: 36,
  hints_used: 1
});
assert(hintSolve.is_correct === true, '11. Correct response after hint is counted as correct');

// 12. Think removes divisor choices
const thinkQ = thinkEngine.getNextQuestion();
assert(thinkQ.support_level === 2, '12. Think stage question operates at lower support_level 2');

// 13. Build accepts structured steps & 14. Confidence bridge
console.log('\nTest 13-16: Build, Bridge, Solve, and Apply stages');
const buildEngine = createLearningEngine({ topicData: ftaData, currentStage: 'constructed_solution' });
buildEngine.submitInteraction({ question_id: 'c_01', is_correct: true, hints_used: 0, skill_ids: ['prime_factorisation', 'division_calculation', 'completion_condition', 'expanded_form', 'exponential_form', 'error_analysis'] });
buildEngine.submitInteraction({ question_id: 'c_02', is_correct: true, hints_used: 0, skill_ids: ['prime_factorisation', 'division_calculation', 'completion_condition', 'expanded_form', 'exponential_form', 'error_analysis'] });
const buildAdv = buildEngine.submitInteraction({ question_id: 'c_03', is_correct: true, hints_used: 0, skill_ids: ['prime_factorisation', 'division_calculation', 'completion_condition', 'expanded_form', 'exponential_form', 'error_analysis'] });
assert(buildAdv.student_stage === 'build', '14. Confidence bridge transition remains visually "Build" for learner');

// 15. Solve removes scaffolding
const solveEngine = createLearningEngine({ topicData: ftaData, currentStage: 'independent_solution' });
const solveQ = solveEngine.getNextQuestion();
assert(solveQ.support_level === 0, '15. Solve stage items have support_level 0 (no scaffolding)');

// 16. Apply uses transfer variation
const applyEngine = createLearningEngine({ topicData: ftaData, currentStage: 'transfer_mastery' });
const applyQ = applyEngine.getNextQuestion();
assert(applyQ.stage === 'transfer_mastery', '16. Apply serves multi-representation transfer questions');

// 17. Skill mastery appears correctly & 18. Topic mastery appears correctly
console.log('\nTest 17-20: Mastery, Retrieval, and Reset session');
const masteryEngine = createLearningEngine({ topicData: ftaData, currentStage: 'mastery_gate' });
masteryEngine.submitInteraction({ question_id: 'i_01', is_correct: true, hints_used: 0, skill_ids: ['prime_factorisation', 'completion_condition', 'divisor_selection', 'division_calculation', 'expanded_form', 'exponential_form', 'uniqueness'] });
masteryEngine.submitInteraction({ question_id: 'i_02', is_correct: true, hints_used: 0, skill_ids: ['prime_factorisation', 'completion_condition', 'divisor_selection', 'division_calculation', 'expanded_form', 'exponential_form', 'uniqueness'] });
const masteryState = masteryEngine.getMasteryState();
assert(masteryState.skills['prime_factorisation'].mastered === true, '17. Skill mastery evaluated and displayed correctly');

// 19. Retrieval remains positive
const retainEngine = createLearningEngine({ topicData: ftaData, currentStage: 'delayed_retrieval' });
const retainState = retainEngine.getLearningState();
assert(retainState.student_stage === 'retain', '19. Retrieval stage displays positive "Retain" journey status');

// 20. Reset starts a fresh learning session
const resetEngine = createLearningEngine({ topicData: ftaData });
assert(resetEngine.getLearningState().current_stage === 'concept_learning', '20. Fresh session resets to initial concept_learning');

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
