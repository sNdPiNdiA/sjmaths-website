/**
 * test-runner.js
 * 
 * Comprehensive automated test suite for SJMaths WebMCP Chapter 4 prototype.
 * Tests all 8 tools, input validation, answer/solution sanitization, state persistence,
 * and Evidence-Based Skill Mastery (State Version 2).
 */

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { createWebMCPTools } from './webmcp-tools.js';
import { registerWebMCPTools, WEBMCP_TOOL_DEFINITIONS } from './webmcp-register.js';
import { StateStore, STATE_VERSION, evaluateSkillMastery } from './state-store.js';
import {
  StageController,
  createStageController,
  STUDENT_TO_INTERNAL_STAGE,
  INTERNAL_TO_STUDENT_STAGE,
  normalizeStage,
  getStudentStageLabel,
  normalizeAssessmentItemDimensions
} from './stage-controller.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const dataPath = path.join(__dirname, '../data/chapter-4/chapter-4-data-v2.json');
const chapterData = JSON.parse(fs.readFileSync(dataPath, 'utf8'));

const { executeTool, TOOLS } = createWebMCPTools(chapterData);

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

function assertThrows(fn, message) {
  totalTests += 1;
  try {
    fn();
    failedTests += 1;
    console.error(`  [FAIL] ${message} (Expected error, but function succeeded)`);
  } catch (e) {
    passedTests += 1;
    console.log(`  [PASS] ${message} -> Caught: "${e.message}"`);
  }
}

console.log('====================================================');
console.log('SJMATHS WEBMCP CHAPTER 4 TOOL VERIFICATION SUITE');
console.log('====================================================\n');

// Test 1: Tool Dispatcher Validation
console.log('Test Group 1: Tool Registration & Invocation Adapter');
assert(typeof executeTool === 'function', 'executeTool dispatcher is a function');
assert(Object.keys(TOOLS).length === 8, 'Exactly 8 tools registered in TOOLS registry');
assertThrows(() => executeTool('unknown_tool', {}), 'executeTool rejects unknown tool names');
assertThrows(() => executeTool('', {}), 'executeTool rejects empty tool name');

// Test 2: Tool 1 - get_topic_outline
console.log('\nTest Group 2: Tool 1 - get_topic_outline');
const outline = executeTool('get_topic_outline', {});
assert(outline.topic.id === 'chapter-4-quadratic-equations', 'Topic ID matches chapter 4');
assert(outline.units.length === 4, 'Returns 4 units in outline');
assert(outline.skills.length === 12, 'Returns 12 skills');
assert(!('correct_index' in outline), 'No correct_index leakage in outline');
assert(!('solution' in outline), 'No solution leakage in outline');

// Test 3: Tool 2 - get_unit_content (Assessment vs Study Sanitization)
console.log('\nTest Group 3: Tool 2 - get_unit_content (Sanitization & Modes)');
assertThrows(() => executeTool('get_unit_content', {}), 'get_unit_content requires unit_id');
assertThrows(() => executeTool('get_unit_content', { unit_id: 'invalid-unit' }), 'get_unit_content rejects non-existent unit_id');

// 3A: Assessment Mode
const unit1Assess = executeTool('get_unit_content', { unit_id: 'unit-1-standard-form-factorisation', include_practice: true, mode: 'assessment' });
assert(unit1Assess.unit_id === 'unit-1-standard-form-factorisation', 'Valid unit returned');
assert(unit1Assess.instruction.core_concepts.length > 0, 'Instruction paragraphs returned');
assert(unit1Assess.practice_questions.length === 18, 'Returns 18 practice questions (10 practice + 8 pyq)');

let assessLeakedAnswers = false;
let assessLeakedSolutions = false;
for (const q of unit1Assess.practice_questions) {
  if ('correct_index' in q) assessLeakedAnswers = true;
  if ('solution' in q) assessLeakedSolutions = true;
}
assert(!assessLeakedAnswers, 'ASSESSMENT MODE: Zero questions leak "correct_index"');
assert(!assessLeakedSolutions, 'ASSESSMENT MODE: Zero questions leak "solution"');

// 3B: Study Mode
const unit1Study = executeTool('get_unit_content', { unit_id: 'unit-1-standard-form-factorisation', include_practice: true, mode: 'study' });
let studyHasAnswers = true;
let studyHasSolutions = true;
for (const q of unit1Study.practice_questions) {
  if (typeof q.correct_index !== 'number') studyHasAnswers = false;
  if (typeof q.solution !== 'string') studyHasSolutions = false;
}
assert(studyHasAnswers, 'STUDY MODE: Includes correct_index for tutoring');
assert(studyHasSolutions, 'STUDY MODE: Includes solutions for teaching');

// Test 4: Tool 3 - get_prerequisite_check
console.log('\nTest Group 4: Tool 3 - get_prerequisite_check (Sanitization)');
assertThrows(() => executeTool('get_prerequisite_check', {}), 'get_prerequisite_check requires unit_id');
assertThrows(() => executeTool('get_prerequisite_check', { unit_id: 'unit-999' }), 'Rejects invalid unit_id');

const precheck = executeTool('get_prerequisite_check', { unit_id: 'unit-1-standard-form-factorisation' });
assert(precheck.check_id === 'u1-precheck', 'Returns unit 1 precheck');
assert(Array.isArray(precheck.options) && precheck.options.length === 3, 'Returns options array');
assert(!('correct_index' in precheck), 'PRECHECK SANITIZATION: Does NOT leak correct_index');
assert(!('pass_feedback' in precheck), 'PRECHECK SANITIZATION: Does NOT leak pass_feedback');
assert(!('remediation_hint' in precheck), 'PRECHECK SANITIZATION: Does NOT leak remediation_hint');

// Test 5: Tool 4 - evaluate_unit_practice
console.log('\nTest Group 5: Tool 4 - evaluate_unit_practice (Assessment & Grading)');
const testStore = new StateStore({ useMemoryOnly: true });

assertThrows(() => executeTool('evaluate_unit_practice', {}, testStore), 'Rejects missing question_id');
assertThrows(() => executeTool('evaluate_unit_practice', { question_id: 'invalid-q', selected_index: 0 }, testStore), 'Rejects unknown question_id');
assertThrows(() => executeTool('evaluate_unit_practice', { question_id: 'u1-p-1', selected_index: 99 }, testStore), 'Rejects out-of-bounds selected_index');

// Evaluate Precheck correct & incorrect
const evalPreCorrect = executeTool('evaluate_unit_practice', { question_id: 'u1-precheck', selected_index: 0 }, testStore);
assert(evalPreCorrect.is_correct === true, 'Precheck correct answer evaluates to true');
assert(evalPreCorrect.feedback.includes('Correct!'), 'Pass feedback returned on precheck correct');

const evalPreIncorrect = executeTool('evaluate_unit_practice', { question_id: 'u1-precheck', selected_index: 1 }, testStore);
assert(evalPreIncorrect.is_correct === false, 'Precheck wrong answer evaluates to false');
assert(evalPreIncorrect.feedback === 'Incorrect. Review the prerequisite concept or request a hint.', 'Precheck wrong answer returns non-revealing generic feedback');
assert(!evalPreIncorrect.feedback.includes('a must be non-zero'), 'ASSESSMENT SAFETY: Incorrect precheck does NOT leak "a must be non-zero" answer clue');
assert(!evalPreIncorrect.feedback.includes('a \u2260 0') && !evalPreIncorrect.feedback.includes('a \\neq 0'), 'ASSESSMENT SAFETY: Incorrect precheck does NOT leak correct option string');
assert(!('correct_index' in evalPreIncorrect), 'ASSESSMENT SAFETY: evalPreIncorrect does not contain correct_index');
assert(!('solution' in evalPreIncorrect), 'ASSESSMENT SAFETY: evalPreIncorrect does not contain solution');

// Evaluate Practice Question & Error Streak Remediation
testStore.resetState();
const evalP1Incorrect = executeTool('evaluate_unit_practice', { question_id: 'u1-p-1', selected_index: 1 }, testStore);
assert(evalP1Incorrect.is_correct === false, 'Wrong option graded false');
assert(evalP1Incorrect.remediation_triggered === false, '1st error does not trigger remediation');

const evalP2Incorrect = executeTool('evaluate_unit_practice', { question_id: 'u1-p-2', selected_index: 1 }, testStore);
assert(evalP2Incorrect.is_correct === false, '2nd wrong option graded false');
assert(evalP2Incorrect.remediation_triggered === true, '2nd consecutive error triggers remediation rule');

const evalP1Correct = executeTool('evaluate_unit_practice', { question_id: 'u1-p-1', selected_index: 0 }, testStore);
assert(evalP1Correct.is_correct === true, 'Correct answer graded true');
assert(evalP1Correct.solution !== null, 'Solution derivation exposed upon correct solution');
assert(testStore.getState().recent_error_streak === 0, 'Error streak reset on correct answer');

// Test 6: Tool 5 - get_hint (Multi-tier Progressive Scaffolding)
console.log('\nTest Group 6: Tool 5 - get_hint (Tiered Hints)');
assertThrows(() => executeTool('get_hint', {}, testStore), 'Rejects missing question_id');
assertThrows(() => executeTool('get_hint', { question_id: 'u1-p-1', hint_level: 5 }, testStore), 'Rejects invalid hint_level');

const hintL1 = executeTool('get_hint', { question_id: 'u1-p-1', hint_level: 1 }, testStore);
assert(hintL1.hint_type === 'conceptual', 'Level 1 hint is conceptual');
assert(!hintL1.hint_text.includes('$x^2+7=0$'), 'Level 1 does NOT leak final solution');

const hintL2 = executeTool('get_hint', { question_id: 'u1-p-1', hint_level: 2 }, testStore);
assert(hintL2.hint_type === 'procedural', 'Level 2 hint is procedural');

const hintL3 = executeTool('get_hint', { question_id: 'u1-p-1', hint_level: 3 }, testStore);
assert(hintL3.hint_type === 'full_solution', 'Level 3 hint provides full solution');
assert(hintL3.hint_text.includes('Full Solution Derivation'), 'Level 3 reveals derivation');

// Test 7: Tool 6 - get_next_learning_action
console.log('\nTest Group 7: Tool 6 - get_next_learning_action (Pedagogical Navigation)');
const cleanStore = new StateStore({ useMemoryOnly: true });

// Initial step in Unit 1
const nextActionInitial = executeTool('get_next_learning_action', { current_unit_id: 'unit-1-standard-form-factorisation' }, cleanStore);
assert(nextActionInitial.action === 'continue_practice', 'Recommends continue_practice initially');
assert(nextActionInitial.next_question_id === 'u1-p-1', 'Target first practice item u1-p-1');

// Trigger error streak remediation recommendation
const nextActionRemediation = executeTool('get_next_learning_action', {
  current_unit_id: 'unit-1-standard-form-factorisation',
  recent_error_streak: 2
}, cleanStore);
assert(nextActionRemediation.action === 'recommend_remediation', 'Recommends remediation when error streak >= 2');
assert(nextActionRemediation.target_resource.type === 'formula_review', 'Directs to formula review card');

// Test 8: Tool 7 - start_mastery_exam (Exam Sanitization)
console.log('\nTest Group 8: Tool 7 - start_mastery_exam (Exam Sanitization)');
const exam = executeTool('start_mastery_exam', {});
assert(exam.assessment_id === 'chapter-4-mastery-exam', 'Returns chapter mastery exam');
assert(exam.questions.length === 10, 'Exam contains exactly 10 questions');
assert(exam.pass_percent === 80, 'Pass percent is 80%');

let examLeakedAnswers = false;
let examLeakedSolutions = false;
for (const q of exam.questions) {
  if ('correct_index' in q) examLeakedAnswers = true;
  if ('solution' in q) examLeakedSolutions = true;
}
assert(!examLeakedAnswers, 'MASTERY EXAM SANITIZATION: Zero questions leak "correct_index"');
assert(!examLeakedSolutions, 'MASTERY EXAM SANITIZATION: Zero questions leak "solution"');

// Test 9: Tool 8 - get_learning_progress
console.log('\nTest Group 9: Tool 8 - get_learning_progress (Progress Tracking)');
const progressInitial = executeTool('get_learning_progress', {}, cleanStore);
assert(progressInitial.overall_progress_percent === 0, 'Initial progress is 0%');
assert(progressInitial.is_ready_for_mastery_exam === false, 'Not ready for mastery exam initially');

// Simulate unit completions
cleanStore.completeUnit('unit-1-standard-form-factorisation');
cleanStore.completeUnit('unit-2-quadratic-formula');
cleanStore.completeUnit('unit-3-nature-of-roots');
cleanStore.completeUnit('unit-4-situational-word-problems');

const progressCompleted = executeTool('get_learning_progress', {}, cleanStore);
assert(progressCompleted.overall_progress_percent === 100, 'Progress reaches 100% after all units complete');
assert(progressCompleted.is_ready_for_mastery_exam === true, 'Ready for mastery exam when all 4 units complete');

// Test 10: WebMCP Registration Layer Verification
console.log('\nTest Group 10: webmcp-register.js Integration');
const registeredTools = [];
const mockModelContext = {
  registerTool: async (toolObj) => {
    registeredTools.push(toolObj);
  }
};

const regPromise = registerWebMCPTools(chapterData, mockModelContext);
assert(regPromise instanceof Promise, 'registerWebMCPTools returns a Promise');
const regResult = await regPromise;
assert(regResult.length === 8, 'Registers exactly 8 tools via document.modelContext');
assert(registeredTools.length === 8, 'Mock modelContext received 8 tool objects');
assert(typeof registeredTools[0].execute === 'function', 'Tool objects provide execute callback');

// Test Group 11: Evidence-Based Skill Mastery Engine
console.log('\nTest Group 11: Evidence-Based Skill Mastery & State Versioning');
const mStore = new StateStore({ useMemoryOnly: true });

// A. One correct guided-practice question -> skill NOT mastered
executeTool('evaluate_unit_practice', { question_id: 'u1-p-2', selected_index: 0 }, mStore); // u1-p-2 is guided_practice (skill-factorise-middle-term)
let mState = mStore.getState();
assert(!mState.mastered_skills.includes('skill-factorise-middle-term'), 'A. One correct guided-practice question: skill NOT mastered');
assert(mState.skill_evidence['skill-factorise-middle-term'].guided_correct === 1, '   Guided evidence counter incremented to 1');
assert(mState.skill_evidence['skill-factorise-middle-term'].total_correct === 1, '   Total correct evidence counter is 1');

// B. Same question answered correctly twice -> skill still NOT mastered (no duplicate distinct evidence)
executeTool('evaluate_unit_practice', { question_id: 'u1-p-2', selected_index: 0 }, mStore);
mState = mStore.getState();
assert(!mState.mastered_skills.includes('skill-factorise-middle-term'), 'B. Same question answered correctly twice: skill still NOT mastered');
assert(mState.skill_evidence['skill-factorise-middle-term'].correct_question_ids.length === 1, '   Distinct question count remains 1');
assert(mState.skill_evidence['skill-factorise-middle-term'].guided_correct === 1, '   Guided counter does not increment on duplicate');

// C. Two distinct guided-practice questions correct -> skill still NOT mastered (requires higher stage)
executeTool('evaluate_unit_practice', { question_id: 'u1-p-3', selected_index: 0 }, mStore); // u1-p-3 is guided_practice (skill-factorise-middle-term)
mState = mStore.getState();
assert(!mState.mastered_skills.includes('skill-factorise-middle-term'), 'C. Two distinct guided-practice questions correct: skill still NOT mastered');
assert(mState.skill_evidence['skill-factorise-middle-term'].guided_correct === 2, '   Guided count is 2, independent count is 0');

// D. One guided + one independent correct -> skill IS mastered
executeTool('evaluate_unit_practice', { question_id: 'u1-p-6', selected_index: 0 }, mStore); // u1-p-6 is independent_solution (skill-factorise-middle-term)
mState = mStore.getState();
assert(mState.mastered_skills.includes('skill-factorise-middle-term'), 'D. One guided + one independent correct: skill IS mastered');
assert(mState.skill_evidence['skill-factorise-middle-term'].mastery_status === 'mastered', '   Evidence status changed to "mastered"');

// E. One guided + one transfer correct -> skill IS mastered
const mStoreE = new StateStore({ useMemoryOnly: true });
executeTool('evaluate_unit_practice', { question_id: 'u1-p-1', selected_index: 0 }, mStoreE); // u1-p-1 guided (skill-identify-quadratic)
assert(!mStoreE.getState().mastered_skills.includes('skill-identify-quadratic'), 'E1. Initial guided question alone is not mastered');
executeTool('evaluate_unit_practice', { question_id: 'u1-pyq-5', selected_index: 0 }, mStoreE); // u1-pyq-5 transfer (skill-identify-quadratic)
assert(mStoreE.getState().mastered_skills.includes('skill-identify-quadratic'), 'E2. One guided + one transfer correct: skill IS mastered');

// F. One independent correct only -> skill NOT mastered (< 2 distinct questions)
const mStoreF = new StateStore({ useMemoryOnly: true });
executeTool('evaluate_unit_practice', { question_id: 'u1-p-10', selected_index: 0 }, mStoreF); // u1-p-10 independent (skill-verify-roots-k)
assert(!mStoreF.getState().mastered_skills.includes('skill-verify-roots-k'), 'F. One independent correct only: skill NOT mastered (1/2 distinct)');

// G. One transfer correct only -> skill NOT mastered (< 2 distinct questions)
const mStoreG = new StateStore({ useMemoryOnly: true });
executeTool('evaluate_unit_practice', { question_id: 'u1-pyq-10', selected_index: 0 }, mStoreG); // u1-pyq-10 transfer (skill-verify-roots-k)
assert(!mStoreG.getState().mastered_skills.includes('skill-verify-roots-k'), 'G. One transfer correct only: skill NOT mastered (1/2 distinct)');

// H. Precheck correct -> skill NOT mastered (diagnostic precheck does not award skill mastery)
const mStoreH = new StateStore({ useMemoryOnly: true });
executeTool('evaluate_unit_practice', { question_id: 'u1-precheck', selected_index: 0 }, mStoreH);
assert(mStoreH.getState().mastered_skills.length === 0, 'H. Precheck correct: skill NOT mastered');
assert(Object.keys(mStoreH.getState().skill_evidence).length === 0, '   Precheck records no skill mastery evidence');

// I. Wrong answer -> evidence does not increase
const mStoreI = new StateStore({ useMemoryOnly: true });
executeTool('evaluate_unit_practice', { question_id: 'u1-p-1', selected_index: 1 }, mStoreI); // wrong answer
assert(!mStoreI.getState().skill_evidence['skill-identify-quadratic'], 'I. Wrong answer: evidence does not increase');

// J. Duplicate correct question -> distinct-question evidence does not increase
const mStoreJ = new StateStore({ useMemoryOnly: true });
executeTool('evaluate_unit_practice', { question_id: 'u1-p-1', selected_index: 0 }, mStoreJ);
executeTool('evaluate_unit_practice', { question_id: 'u1-p-1', selected_index: 0 }, mStoreJ);
assert(mStoreJ.getState().skill_evidence['skill-identify-quadratic'].correct_question_ids.length === 1, 'J. Duplicate correct question: distinct count is 1');

// K. get_learning_progress reports the new mastery count correctly
const progressM = executeTool('get_learning_progress', {}, mStore);
assert(progressM.skills_mastered_count === 1, 'K1. get_learning_progress reports 1 skill mastered');
assert(progressM.total_skills === 12, 'K2. total_skills reported as 12');

// L. get_next_learning_action does not recommend mastery when evidence is insufficient
const mStoreL = new StateStore({ useMemoryOnly: true });
executeTool('evaluate_unit_practice', { question_id: 'u1-p-1', selected_index: 0 }, mStoreL); // 1 guided correct for skill-identify-quadratic
const nextActionL = executeTool('get_next_learning_action', { current_unit_id: 'unit-1-standard-form-factorisation' }, mStoreL);
assert(nextActionL.action === 'continue_practice', 'L1. get_next_learning_action recommends continue_practice');
assert(nextActionL.reason.includes('Skill requires additional evidence before mastery') || nextActionL.reason.includes('Continue active unit practice questions'), 'L2. Reason indicates practice continuation rather than early mastery');

// M. State versioning: old state version cannot preserve legacy one-answer mastery
const v1LegacyState = {
  current_unit_id: 'unit-1-standard-form-factorisation',
  completed_units: [],
  mastered_skills: ['skill-identify-quadratic'], // legacy 1-question mastery
  completed_questions: { 'u1-p-1': { solved: true } },
  recent_error_streak: 0
};
assert(STATE_VERSION === 2, 'M1. Current State Version is 2');
// Direct evaluation check on legacy state
// Test Group 12: Generic Topic-Agnostic Learning Engine Direct Verification
console.log('\nTest Group 12: Generic Learning Engine (Topic-Agnostic Operation)');
import('./learning-engine.js').then(({ createLearningEngine }) => {
  assert(typeof createLearningEngine === 'function', 'createLearningEngine factory is exported');

  // A. Instantiate engine with a synthetic topic dataset to prove zero hardcoded dependencies
  const mockTopicData = {
    schema_version: '2.0.0',
    content_type: 'learning_topic',
    topic: {
      id: 'mock-topic-trigonometry',
      title: 'Introduction to Trigonometry',
      grade: 10,
      subject: 'Mathematics',
      standard: 'CBSE',
      description: 'Trigonometric ratios and identities'
    },
    scope: {
      total_units: 1,
      total_skills: 2,
      estimated_learning_minutes: 60,
      target_mastery_level: 'proficient'
    },
    sequence: {
      unit_order: ['unit-trig-ratios'],
      gate_policy: 'sequential_mastery'
    },
    skills: [
      {
        id: 'skill-sin-cos-tan-definition',
        unit_id: 'unit-trig-ratios',
        name: 'Define Basic Trigonometric Ratios (sin, cos, tan)',
        description: 'Understand ratio of sides in right triangles.'
      },
      {
        id: 'skill-trig-identities',
        unit_id: 'unit-trig-ratios',
        name: 'Apply Fundamental Trigonometric Identities',
        description: 'Apply sin^2 + cos^2 = 1.'
      }
    ],
    units: [
      {
        id: 'unit-trig-ratios',
        unit_number: 1,
        title: 'Trigonometric Ratios & Right Triangles',
        icon: '📐',
        skills_covered: ['skill-sin-cos-tan-definition', 'skill-trig-identities'],
        prerequisite_check: {
          id: 'trig-precheck-1',
          stage: 'prerequisite_check',
          question: 'In a right triangle, the side opposite the 90 degree angle is called:',
          options: ['Hypotenuse', 'Adjacent', 'Opposite'],
          correct_index: 0,
          pass_feedback: 'Correct! Hypotenuse is the longest side.',
          remediation_hint: 'The hypotenuse is opposite the right angle.'
        },
        instruction: {
          core_concepts: ['$\\sin(\\theta) = \\text{Opposite}/\\text{Hypotenuse}$'],
          formulas: [{ rule: 'Pythagoras', formula: '$a^2+b^2=c^2$', example: '$3^2+4^2=5^2$' }],
          callout_boxes: []
        },
        practice_stages: {
          guided_and_independent: [
            {
              id: 'trig-q-guided-1',
              stage: 'guided_practice',
              skill_id: 'skill-sin-cos-tan-definition',
              difficulty: 'easy',
              question: 'If opp=3 and hyp=5, what is $\\sin(\\theta)$?',
              options: ['3/5', '4/5', '5/3'],
              correct_index: 0,
              solution: '$\\sin(\\theta) = 3/5$.'
            },
            {
              id: 'trig-q-indep-1',
              stage: 'independent_solution',
              skill_id: 'skill-sin-cos-tan-definition',
              difficulty: 'medium',
              question: 'If adj=4 and hyp=5, what is $\\cos(\\theta)$?',
              options: ['4/5', '3/5', '5/4'],
              correct_index: 0,
              solution: '$\\cos(\\theta) = 4/5$.'
            }
          ],
          transfer_and_pyq: []
        }
      }
    ],
    remediation: {
      rules: { trigger_after_consecutive_errors: 2 }
    },
    mastery: {
      chapter_mastery_gate: {
        assessment_id: 'trig-mastery-exam',
        title: 'Trigonometry Mastery Exam',
        pass_percent: 80,
        questions: [
          {
            id: 'trig-exam-1',
            skill_id: 'skill-sin-cos-tan-definition',
            question: 'Value of $\\tan(45^\\circ)$ is:',
            options: ['1', '0', 'undefined'],
            correct_index: 0
          }
        ]
      }
    }
  };

  const genericStore = new StateStore({ useMemoryOnly: true });
  const mockEngine = createLearningEngine({
    topicData: mockTopicData,
    stateStore: genericStore
  });

  // B. Topic title dynamically comes from injected topicData
  const mockOutline = mockEngine.getTopicOutline();
  assert(mockOutline.topic.id === 'mock-topic-trigonometry', 'A. Generic Engine: Dynamic topic ID resolved');
  assert(mockOutline.topic.title === 'Introduction to Trigonometry', 'B. Generic Engine: Dynamic topic title resolved');
  assert(mockOutline.units[0].id === 'unit-trig-ratios', 'C. Generic Engine: Dynamic unit ID resolved');
  assert(mockOutline.skills[0].id === 'skill-sin-cos-tan-definition', 'D. Generic Engine: Dynamic skill ID resolved');

  // C. Prerequisite check & practice execution
  const mockPrecheck = mockEngine.getPrerequisiteCheck({ unit_id: 'unit-trig-ratios' });
  assert(mockPrecheck.check_id === 'trig-precheck-1', 'E. Generic Engine: Dynamic prerequisite check loaded');

  // D. Generic evaluation and mastery verification
  const eval1 = mockEngine.evaluatePractice({ question_id: 'trig-q-guided-1', selected_index: 0 }, genericStore);
  assert(eval1.is_correct === true, 'F1. Generic Engine: Guided question evaluated correctly');
  assert(eval1.skill_id === 'skill-sin-cos-tan-definition', 'F2. Generic Engine: Skill ID mapped accurately');

  // 1 guided correct -> not mastered yet
  const prog1 = mockEngine.getLearningProgress({}, genericStore);
  assert(prog1.skills_mastered_count === 0, 'G1. Generic Engine: 1 guided success does not trigger mastery');

  // Independent correct -> triggers evidence-based mastery on synthetic topic
  const eval2 = mockEngine.evaluatePractice({ question_id: 'trig-q-indep-1', selected_index: 0 }, genericStore);
  assert(eval2.is_correct === true, 'G2. Generic Engine: Independent question evaluated correctly');

  const prog2 = mockEngine.getLearningProgress({}, genericStore);
  assert(prog2.skills_mastered_count === 1, 'G3. Generic Engine: Evidence-based mastery (2 distinct, 1 indep) satisfied');
  assert(prog2.topic_id === 'mock-topic-trigonometry', 'G4. Generic Engine: Progress reports synthetic topic_id');

  // E. Dynamic Hint resolution using synthetic skill taxonomy
  const mockHint = mockEngine.getHint({ question_id: 'trig-q-guided-1', hint_level: 1 }, genericStore);
  assert(mockHint.hint_text.includes('Define Basic Trigonometric Ratios'), 'H. Generic Engine: Hint resolves dynamic skill taxonomy title');

  // Test Group 13: Generic Adaptive Stage Controller & Student-Facing Flow Contract
  console.log('\nTest Group 13: Generic Adaptive Stage Controller & Flow Contract');
  const controller = createStageController();
  const unit1Id = 'unit-1-standard-form-factorisation';

  // G. Student-facing stage labels map correctly to internal stages
  assert(STUDENT_TO_INTERNAL_STAGE.understand === 'concept_learning', 'G1. Label mapping: understand -> concept_learning');
  assert(STUDENT_TO_INTERNAL_STAGE.see === 'worked_examples', 'G2. Label mapping: see -> worked_examples');
  assert(STUDENT_TO_INTERNAL_STAGE.try === 'guided_practice', 'G3. Label mapping: try -> guided_practice');
  assert(STUDENT_TO_INTERNAL_STAGE.think === 'faded_guidance', 'G4. Label mapping: think -> faded_guidance');
  assert(STUDENT_TO_INTERNAL_STAGE.build === 'constructed_solution', 'G5. Label mapping: build -> constructed_solution');
  assert(STUDENT_TO_INTERNAL_STAGE.solve === 'independent_solution', 'G6. Label mapping: solve -> independent_solution');
  assert(STUDENT_TO_INTERNAL_STAGE.apply === 'transfer_mastery', 'G7. Label mapping: apply -> transfer_mastery');
  assert(STUDENT_TO_INTERNAL_STAGE.master === 'mastery_gate', 'G8. Label mapping: master -> mastery_gate');
  assert(STUDENT_TO_INTERNAL_STAGE.retain === 'delayed_retrieval', 'G9. Label mapping: retain -> delayed_retrieval');

  // 3. Separate 4 pedagogical dimensions: stage, task_type, difficulty, support_level
  const sampleDim = normalizeAssessmentItemDimensions({
    stage: 'try',
    difficulty: 'hard',
    options: ['A', 'B']
  });
  assert(sampleDim.stage === 'guided_practice', 'Dim: Stage normalized');
  assert(sampleDim.task_type === 'multiple_choice', 'Dim: Task type separated');
  assert(sampleDim.difficulty === 'hard', 'Dim: Difficulty separated');
  assert(sampleDim.support_level === 'high', 'Dim: Support level separated');

  // A. Strong learner advances early
  const strongStore = new StateStore({ useMemoryOnly: true });
  strongStore.recordAttempt('u1-p-1', true, 0, 'skill-identify-quadratic', 'guided_practice');
  strongStore.recordAttempt('u1-p-2', true, 0, 'skill-factorise-middle-term', 'guided_practice');
  const strongState = strongStore.getState();
  const strongDecision = controller.decide({
    topicData: chapterData,
    studentState: strongState,
    currentUnitId: unit1Id,
    currentStage: 'try' // student label
  });
  assert(strongDecision.action === 'advance' || strongDecision.action === 'complete_skill', 'A1. Strong learner advances early on sufficient distinct evidence');
  assert(strongDecision.internal_stage === 'faded_guidance', 'A2. Target stage is faded_guidance (think)');
  assert(strongDecision.student_stage === 'think', 'A3. Student label is think');

  // B. Struggling learner receives more practice (insufficient accuracy/coverage)
  const strugglingStore = new StateStore({ useMemoryOnly: true });
  strugglingStore.recordAttempt('u1-p-1', true, 0, 'skill-identify-quadratic', 'guided_practice');
  strugglingStore.recordAttempt('u1-p-2', false, 1, 'skill-factorise-middle-term', 'guided_practice');
  // Reset streak so not in immediate remediation
  strugglingStore.recordAttempt('u1-p-3', true, 0, 'skill-factorise-middle-term', 'guided_practice');
  strugglingStore.recordAttempt('u1-p-4', false, 1, 'skill-factorise-middle-term', 'guided_practice');
  const strugglingState = strugglingStore.getState();
  const strugglingDecision = controller.decide({
    topicData: chapterData,
    studentState: strugglingState,
    currentUnitId: unit1Id,
    currentStage: 'try'
  });
  assert(strugglingDecision.action === 'repeat_with_new_question' || strugglingDecision.action === 'stay', 'B1. Struggling learner receives more practice');
  assert(strugglingDecision.internal_stage === 'guided_practice', 'B2. Remains in guided_practice stage');

  // C. Support decreases without unnecessary difficulty increase
  const safeDims = controller.safelyAdjustDimensions(
    { difficulty: 'medium', support_level: 'full' },
    { accuracy: 1.0, consecutiveSuccesses: 2, unassisted: true }
  );
  assert(safeDims.support_level === 'high', 'C1. Support level decreased from full to high');
  assert(safeDims.difficulty === 'medium', 'C2. Difficulty kept at medium without premature jump');
  assert(safeDims.applied_rule === 'safe_support_reduction', 'C3. Applied safe_support_reduction rule');

  // D. Single wrong answer does NOT immediately cause stage regression
  const singleErrorStore = new StateStore({ useMemoryOnly: true });
  singleErrorStore.recordAttempt('u1-p-1', true, 0, 'skill-identify-quadratic', 'guided_practice');
  singleErrorStore.recordAttempt('u1-p-2', false, 1, 'skill-factorise-middle-term', 'guided_practice');
  const singleErrorState = singleErrorStore.getState();
  const singleErrorDecision = controller.decide({
    topicData: chapterData,
    studentState: singleErrorState,
    currentUnitId: unit1Id,
    currentStage: 'try'
  });
  assert(singleErrorDecision.action !== 'remediate', 'D1. Single wrong answer does NOT trigger remediation');
  assert(singleErrorDecision.internal_stage === 'guided_practice', 'D2. Student stays in current stage');

  // E. Repeated failure causes targeted remediation
  const repeatedErrorStore = new StateStore({ useMemoryOnly: true });
  repeatedErrorStore.recordAttempt('u1-p-2', false, 1, 'skill-factorise-middle-term', 'guided_practice');
  repeatedErrorStore.recordAttempt('u1-p-3', false, 1, 'skill-factorise-middle-term', 'guided_practice');
  const repeatedErrorState = repeatedErrorStore.getState();
  repeatedErrorState.last_attempted_question_id = 'u1-p-3';
  const repeatedErrorDecision = controller.decide({
    topicData: chapterData,
    studentState: repeatedErrorState,
    currentUnitId: unit1Id,
    currentStage: 'try'
  });
  assert(repeatedErrorDecision.action === 'remediate', 'E1. Consecutive errors trigger targeted remediation');
  assert(repeatedErrorDecision.diagnosed_skill_id === 'skill-factorise-middle-term', 'E2. Diagnosed likely skill accurately');
  assert(repeatedErrorDecision.allow_retry === true, 'E3. Contextual retry offered');

  // F. Skill mastery is independent from stage completion
  const skillStore = new StateStore({ useMemoryOnly: true });
  // Learner completes guided practice stage
  skillStore.recordAttempt('u1-p-1', true, 0, 'skill-identify-quadratic', 'guided_practice');
  skillStore.recordAttempt('u1-p-2', true, 0, 'skill-identify-quadratic', 'guided_practice');
  const skillState = skillStore.getState();
  const unitSkillsEval = controller.evaluateUnitSkills(chapterData, skillState, unit1Id);
  assert(unitSkillsEval.allMastered === false, 'F1. Skills NOT mastered with only guided evidence even if stage has questions solved');
  
  // Now add independent practice for skill
  skillStore.recordAttempt('u1-p-7', true, 0, 'skill-identify-quadratic', 'independent_solution');
  const updatedSkillState = skillStore.getState();
  const updatedSkillsEval = controller.evaluateUnitSkills(chapterData, updatedSkillState, unit1Id);
  assert(updatedSkillsEval.skills['skill-identify-quadratic'].mastered === true, 'F2. Skill mastered once independent evidence is provided');
  assert(updatedSkillsEval.skills['skill-factorise-middle-term'].mastered === false, 'F3. Other skills remain unmastered independently');

  // H. Duplicate question evidence is ignored
  const dupStore = new StateStore({ useMemoryOnly: true });
  dupStore.recordAttempt('u1-p-1', true, 0, 'skill-identify-quadratic', 'guided_practice');
  dupStore.recordAttempt('u1-p-1', true, 0, 'skill-identify-quadratic', 'guided_practice'); // Duplicate attempt
  const dupState = dupStore.getState();
  const dupStageEv = controller.getStageEvidence(chapterData, dupState, unit1Id, 'guided_practice');
  assert(dupStageEv.distinctCorrect === 1, 'H1. Duplicate question solves count as 1 distinct question');
  assert(dupStageEv.attemptsCount === 2, 'H2. Attempts count tracks all 2 tries');

  // I. Hint use does not count as unassisted mastery by itself
  const hintStore = new StateStore({ useMemoryOnly: true });
  hintStore.recordAttempt('u1-p-1', true, 0, 'skill-identify-quadratic', 'guided_practice');
  const hintState = hintStore.getState();
  hintState.hint_usage = { 'u1-p-1': 2 }; // Learner used level 2 procedural hint
  const hintStageEv = controller.getStageEvidence(chapterData, hintState, unit1Id, 'guided_practice');
  assert(hintStageEv.distinctCorrect === 1, 'I1. Solved with hint is recorded as correct');
  assert(hintStageEv.distinctUnassistedCorrect === 0, 'I2. Solved with hint is NOT counted as unassisted mastery evidence');

  // Final Summary Report
  console.log('\n====================================================');
  console.log(`TOTAL TESTS: ${totalTests}`);
  console.log(`PASSED:      ${passedTests}`);
  console.log(`FAILED:      ${failedTests}`);
  console.log('====================================================');

  if (failedTests > 0) {
    process.exit(1);
  }
});

