/**
 * test-runner.js
 * 
 * Comprehensive automated test suite for SJMaths WebMCP.
 * Tests all 8 tools, input validation, answer/solution sanitization, state persistence,
 * and Evidence-Based Skill Mastery (State Version 2).
 * 
 * Now fully generic - works with ANY chapter/topic from the learning/topics directory.
 */

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { createWebMCPTools } from './webmcp-tools.js';
import { registerWebMCPTools, buildToolDefinitions } from './webmcp-register.js';
import { StateStore, STATE_VERSION, evaluateSkillMastery } from './state-store.js';
import {
  discoverTopics,
  loadTopic,
  loadChapterTopics,
  topicToUnit,
  combineTopicsToChapter,
  listAvailableChapters
} from './topic-discovery.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// ============================================================
// TEST CONFIGURATION - Tests multiple chapters/topics
// ============================================================

const TEST_CONFIG = {
  testChapters: [
    { class: 'class-10', subject: 'mathematics', chapter: 'chapter-4-quadratic-equations' },
    { class: 'class-10', subject: 'mathematics', chapter: 'chapter-1-real-numbers' },
    { class: 'class-10', subject: 'mathematics', chapter: 'chapter-5-arithmetic-progressions' }
  ],
  testTopics: [
    { class: 'class-10', subject: 'mathematics', chapter: 'chapter-4-quadratic-equations', topic: 'standard-form-roots' },
    { class: 'class-10', subject: 'mathematics', chapter: 'chapter-1-real-numbers', topic: 'fta' },
    { class: 'class-10', subject: 'mathematics', chapter: 'chapter-5-arithmetic-progressions', topic: 'ap-basics-nth-term' }
  ]
};

// Load test data using topic-discovery.js
console.log('=== Loading Test Data ===');
const availableChapters = listAvailableChapters();
console.log(`Found ${availableChapters.length} chapters:`);
availableChapters.forEach(ch => {
  console.log(`  - ${ch.chapter} (${ch.topicCount} topics)`);
});

// Load Chapter 4 (Quadratic Equations) for primary tests
const chapter4Topics = loadChapterTopics('class-10', 'mathematics', 'chapter-4-quadratic-equations');
const chapterData = combineTopicsToChapter(chapter4Topics, {
  id: 'chapter-4-quadratic-equations',
  title: 'Quadratic Equations',
  description: 'Master quadratic equations through standard form identification, factorization, quadratic formula, discriminant nature of roots, and real-world mathematical modeling.'
});

// Load Chapter 1 (Real Numbers) for cross-chapter tests
const chapter1Topics = loadChapterTopics('class-10', 'mathematics', 'chapter-1-real-numbers');
const chapter1Data = combineTopicsToChapter(chapter1Topics, {
  id: 'chapter-1-real-numbers',
  title: 'Real Numbers',
  description: 'Master real numbers through fundamental theorem of arithmetic, HCF/LCM, and proof of irrationality.'
});

// Load Chapter 5 (Arithmetic Progressions) for cross-chapter tests
const chapter5Topics = loadChapterTopics('class-10', 'mathematics', 'chapter-5-arithmetic-progressions');
const chapter5Data = combineTopicsToChapter(chapter5Topics, {
  id: 'chapter-5-arithmetic-progressions',
  title: 'Arithmetic Progressions',
  description: 'Master arithmetic progressions through nth term, sum of n terms, and applications.'
});

console.log(`\nLoaded:`);
console.log(`  - Chapter 4: ${chapter4Topics.length} topics`);
console.log(`  - Chapter 1: ${chapter1Topics.length} topics`);
console.log(`  - Chapter 5: ${chapter5Topics.length} topics`);

// ============================================================
// TEST HELPERS
// ============================================================

let totalTests = 0;
let passedTests = 0;
let failedTests = 0;

function assert(condition, message) {
  totalTests++;
  if (condition) {
    passedTests++;
    console.log(`  ? ${message}`);
  } else {
    failedTests++;
    console.error(`  ? FAIL: ${message}`);
  }
}

function assertEqual(actual, expected, message) {
  assert(actual === expected, `${message} (expected: ${expected}, got: ${actual})`);
}

function assertDefined(value, message) {
  assert(value !== undefined && value !== null, message);
}

function assertContains(arr, item, message) {
  assert(arr.includes(item), message);
}

function assertNotContains(arr, item, message) {
  assert(!arr.includes(item), message);
}

function assertThrows(fn, message) {
  try {
    fn();
    assert(false, `${message} (did not throw)`);
  } catch (e) {
    assert(true, message);
  }
}

// ============================================================
// TEST SUITE 1: TOPIC DISCOVERY
// ============================================================

console.log('\n=== TEST SUITE 1: Topic Discovery ===');

// Test 1.1: listAvailableChapters returns chapters
assert(availableChapters.length > 0, '1.1 listAvailableChapters returns at least one chapter');

// Test 1.2: Chapter 4 is found
const ch4 = availableChapters.find(c => c.chapter === 'chapter-4-quadratic-equations');
assertDefined(ch4, '1.2 Chapter 4 (Quadratic Equations) found');
assert(ch4.topicCount >= 5, '1.2.1 Chapter 4 has at least 5 topics');

// Test 1.3: Chapter 1 is found
const ch1 = availableChapters.find(c => c.chapter === 'chapter-1-real-numbers');
assertDefined(ch1, '1.3 Chapter 1 (Real Numbers) found');
assert(ch1.topicCount >= 3, '1.3.1 Chapter 1 has at least 3 topics');

// Test 1.4: Chapter 5 is found
const ch5 = availableChapters.find(c => c.chapter === 'chapter-5-arithmetic-progressions');
assertDefined(ch5, '1.4 Chapter 5 (Arithmetic Progressions) found');
assert(ch5.topicCount >= 5, '1.4.1 Chapter 5 has at least 5 topics');

// Test 1.5: loadTopic loads a specific topic
const ftaTopic = loadTopic('class-10', 'mathematics', 'chapter-1-real-numbers', 'fta');
assertDefined(ftaTopic, '1.5 loadTopic loads FTA topic');
assertDefined(ftaTopic.topic, '1.5.1 FTA topic has topic object');

// Test 1.6: combineTopicsToChapter creates valid structure
assertDefined(chapterData.units, '1.6 combineTopicsToChapter creates units array');
assertEqual(chapterData.units.length, chapter4Topics.length, '1.6.1 Units count matches topics count');
assertEqual(chapterData.topic.id, 'chapter-4-quadratic-equations', '1.6.2 Chapter ID is correct');

// ============================================================
// TEST SUITE 2: TOOL REGISTRATION
// ============================================================

console.log('\n=== TEST SUITE 2: Tool Registration ===');

// Test 2.1: Tool definitions exist (built dynamically from chapter data)
const toolDefinitions = buildToolDefinitions(chapterData);
assertEqual(toolDefinitions.length, 8, '2.1 All 8 WebMCP tool definitions exist');

// Test 2.2: Tool names are correct
const toolNames = toolDefinitions.map(t => t.name);
const expectedTools = [
  'get_topic_outline',
  'get_prerequisite_check',
  'get_unit_content',
  'evaluate_unit_practice',
  'get_hint',
  'get_next_learning_action',
  'start_mastery_exam',
  'get_learning_progress'
];
expectedTools.forEach(toolName => {
  assertContains(toolNames, toolName, `2.2 Tool ${toolName} is defined`);
});

// Test 2.3: Each tool definition has required fields
toolDefinitions.forEach(tool => {
  assertDefined(tool.name, `2.3 Tool has name`);
  assertDefined(tool.description, `2.3 Tool ${tool.name} has description`);
  assertDefined(tool.inputSchema, `2.3 Tool ${tool.name} has inputSchema`);
});

// ============================================================
// TEST SUITE 3: GET_TOPIC_OUTLINE
// ============================================================

console.log('\n=== TEST SUITE 3: get_topic_outline ===');

const tools = createWebMCPTools(chapterData);

// Test 3.1: Returns topic outline
const outline = tools.getTopicOutline();
assertDefined(outline, '3.1 getTopicOutline returns result');
assertEqual(outline.topic.id, chapterData.topic.id, '3.1.1 Topic ID matches');
assertEqual(outline.topic.title, chapterData.topic.title, '3.1.2 Title matches');
assertDefined(outline.units, '3.1.3 Units array exists');
assertEqual(outline.units.length, chapterData.units.length, '3.1.4 Units count matches');

// Test 3.2: Outline does NOT leak answers
assert(!JSON.stringify(outline).includes('"correct_index":'), '3.2 Outline does not contain correct_index');
assert(!JSON.stringify(outline).includes('"solution":'), '3.2.1 Outline does not contain solution');

// Test 3.3: Each unit in outline has expected fields
outline.units.forEach((unit, i) => {
  assertDefined(unit.id, `3.3 Unit ${i} has id`);
  assertDefined(unit.title, `3.3 Unit ${i} has title`);
});

// Test 3.4: Outline includes stage_progression (the 5-stage learning path)
if (outline.stage_progression) {
  assert(Array.isArray(outline.stage_progression) && outline.stage_progression.length > 0, '3.4 stage_progression present in outline');
  const stageIds = outline.stage_progression.map(s => s.id);
  assert(stageIds.includes('concepts'), '3.4.1 Stage concepts present');
  assert(stageIds.includes('worked_examples'), '3.4.2 Stage worked_examples present');
}

// ============================================================
// TEST SUITE 4: GET_PREREQUISITE_CHECK
// ============================================================

console.log('\n=== TEST SUITE 4: get_prerequisite_check ===');

// Test 4.1: Returns prerequisite check for first unit
const precheck = tools.getPrerequisiteCheck({ unit_id: chapterData.units[0].id });
assertDefined(precheck, '4.1 getPrerequisiteCheck returns result');
assertDefined(precheck.question, '4.1.1 Prerequisite question exists');
assertDefined(precheck.options, '4.1.2 Prerequisite options exist');

// Test 4.2: Does NOT leak correct answer
assert(precheck.correct_index === undefined, '4.2 correct_index is hidden');
assert(precheck.answer === undefined, '4.2.1 answer is hidden');

// Test 4.3: Error on invalid unit_id
assertThrows(() => tools.getPrerequisiteCheck({ unit_id: 'nonexistent-unit' }), '4.3 Throws error for invalid unit_id');

// ============================================================
// TEST SUITE 5: GET_UNIT_CONTENT
// ============================================================

console.log('\n=== TEST SUITE 5: get_unit_content ===');

// Test 5.1: Returns unit content with flattened pedagogical fields
const unitContent = tools.getUnitContent({ unit_id: chapterData.units[0].id });
assertDefined(unitContent, '5.1 getUnitContent returns result');
assertDefined(unitContent.core_concepts, '5.1.1 Core concepts exist');
assertDefined(unitContent.worked_examples, '5.1.2 Worked examples exist');
assertDefined(unitContent.stage_progression, '5.1.3 Stage progression exists');
assert(Array.isArray(unitContent.core_concepts), '5.1.4 core_concepts is array');
assert(Array.isArray(unitContent.worked_examples), '5.1.5 worked_examples is array');
assert(Array.isArray(unitContent.stage_progression), '5.1.6 stage_progression is array');

// Test 5.2: Does NOT leak answers or solutions
assert(!JSON.stringify(unitContent).includes('"correct_index":'), '5.2 correct_index is hidden');
assert(!JSON.stringify(unitContent).includes('"solution":'), '5.2.1 solution is hidden');

// Test 5.3: Error on invalid unit_id
assertThrows(() => tools.getUnitContent({ unit_id: 'nonexistent-unit' }), '5.3 Throws error for invalid unit_id');

// Test 5.4: The MCP tool surface IGNORES mode:'study' — an agent can never
// pull the answer key through the tool, even by explicitly requesting it.
const leakyContent = tools.getUnitContent({ unit_id: chapterData.units[0].id, include_practice: true, mode: 'study' });
assert(!JSON.stringify(leakyContent).includes('"correct_index":'), '5.4 Tool surface ignores mode=study (no correct_index leak)');
assert(!JSON.stringify(leakyContent).includes('"solution":'), '5.4.1 Tool surface ignores mode=study (no solution leak)');

// Test 5.5: Practice questions included by default (include_practice defaults true)
assert(Array.isArray(unitContent.practice_questions) && unitContent.practice_questions.length > 0, '5.5 practice_questions included by default');

// Test 5.6: include_practice:false strips practice questions
const noPractice = tools.getUnitContent({ unit_id: chapterData.units[0].id, include_practice: false });
assert(!noPractice.practice_questions || noPractice.practice_questions.length === 0, '5.6 include_practice:false strips practice');

// ============================================================
// TEST SUITE 6: EVALUATE_UNIT_PRACTICE
// ============================================================

console.log('\n=== TEST SUITE 6: evaluate_unit_practice ===');

// Test 6.1: Evaluates correct answer
const evalCorrect = tools.evaluateUnitPractice({
  unit_id: chapterData.units[0].id,
  question_id: chapterData.units[0].practice_stages.guided_and_independent[0].id,
  selected_index: chapterData.units[0].practice_stages.guided_and_independent[0].correct_index
});
assertDefined(evalCorrect, '6.1 evaluateUnitPractice returns result');
assertEqual(evalCorrect.is_correct, true, '6.1.1 Correct answer identified');
assertDefined(evalCorrect.skill_id, '6.1.2 Skill ID returned');

// Test 6.2: Evaluates incorrect answer
const evalIncorrect = tools.evaluateUnitPractice({
  unit_id: chapterData.units[0].id,
  question_id: chapterData.units[0].practice_stages.guided_and_independent[0].id,
  selected_index: (chapterData.units[0].practice_stages.guided_and_independent[0].correct_index + 1) % 4
});
assertEqual(evalIncorrect.is_correct, false, '6.2 Incorrect answer identified');

// Test 6.3: Does NOT leak correct answer in response
assert(evalCorrect.correct_index === undefined, '6.3 correct_index hidden in evaluation response');
assert(evalCorrect.solution === undefined, '6.3.1 solution hidden in evaluation response');

// Test 6.4: Error on invalid question_id
assertThrows(() => tools.evaluateUnitPractice({
  unit_id: chapterData.units[0].id,
  question_id: 'nonexistent-question',
  selected_index: 0
}), '6.4 Throws error for invalid question_id');

// ============================================================
// TEST SUITE 7: GET_HINT
// ============================================================

console.log('\n=== TEST SUITE 7: get_hint ===');

// Test 7.1: Returns hint
const hint = tools.getHint({
  unit_id: chapterData.units[0].id,
  question_id: chapterData.units[0].practice_stages.guided_and_independent[0].id,
  hint_level: 1
});
assertDefined(hint, '7.1 getHint returns result');
assertDefined(hint.hint_text, '7.1.1 Hint text exists');

// Test 7.2: Does NOT leak correct answer
assert(hint.correct_index === undefined, '7.2 correct_index hidden in hint');
assert(hint.solution === undefined, '7.2.1 solution hidden in hint');

// Test 7.3: Error on invalid question_id
assertThrows(() => tools.getHint({
  unit_id: chapterData.units[0].id,
  question_id: 'nonexistent-question',
  hint_level: 1
}), '7.3 Throws error for invalid question_id');

// ============================================================
// TEST SUITE 8: STATE PERSISTENCE
// ============================================================

console.log('\n=== TEST SUITE 8: State Persistence ===');

// Test 8.1: StateStore initializes with correct version
const stateStore = new StateStore({ useMemoryOnly: true, topicId: 'test-topic' });
const initialState = stateStore.getState();
assertEqual(initialState.state_version, STATE_VERSION, '8.1 Initial state has correct version');
assertEqual(initialState.topic_id, 'test-topic', '8.1.1 Topic ID is set');

// Test 8.2: recordAttempt tracks correct answers
stateStore.recordAttempt('q1', true, 0, 'skill-1', 'guided_practice');
let state = stateStore.getState();
assertNotContains(state.mastered_skills, 'skill-1', '8.2 Skill NOT mastered with only 1 question - requires 2 distinct');

// Test 8.3: recordAttempt tracks incorrect answers
stateStore.recordAttempt('q2', false, 1, 'skill-2', 'guided_practice');
state = stateStore.getState();
assertEqual(state.recent_error_streak, 1, '8.3 Error streak tracked');

// Test 8.4: completeUnit marks unit as completed
stateStore.completeUnit('unit-1');
state = stateStore.getState();
assertContains(state.completed_units, 'unit-1', '8.4 Unit marked as completed');

// Test 8.5: recordExamResult stores exam session
stateStore.recordExamResult(85, true, 20);
state = stateStore.getState();
assertDefined(state.mastery_exam_session, '8.5 Exam session recorded');
assertEqual(state.mastery_exam_session.score, 85, '8.5.1 Exam score correct');
assertEqual(state.mastery_exam_session.passed, true, '8.5.2 Exam passed status correct');

// ============================================================
// TEST SUITE 9: EVIDENCE-BASED SKILL MASTERY
// ============================================================

console.log('\n=== TEST SUITE 9: Evidence-Based Skill Mastery ===');

// Test 9.1: Mastery requires 2 distinct questions
const masteryStore1 = new StateStore({ useMemoryOnly: true });
masteryStore1.recordAttempt('q1', true, 0, 'skill-a', 'guided_practice');
let masteryState = masteryStore1.getState();
let eval1 = evaluateSkillMastery('skill-a', masteryState.skill_evidence['skill-a']);
assertEqual(eval1.mastered, false, '9.1 Not mastered with only 1 question');

// Test 9.2: Mastery requires independent/transfer evidence
masteryStore1.recordAttempt('q2', true, 0, 'skill-a', 'guided_practice');
masteryState = masteryStore1.getState();
let eval2 = evaluateSkillMastery('skill-a', masteryState.skill_evidence['skill-a']);
assertEqual(eval2.mastered, false, '9.2 Not mastered with only guided practice');

// Test 9.3: Mastery achieved with guided + independent
masteryStore1.recordAttempt('q3', true, 0, 'skill-a', 'independent_solution');
masteryState = masteryStore1.getState();
let eval3 = evaluateSkillMastery('skill-a', masteryState.skill_evidence['skill-a']);
assertEqual(eval3.mastered, true, '9.3 Mastered with guided + independent');

// Test 9.4: Duplicate question does not count twice
const masteryStore2 = new StateStore({ useMemoryOnly: true });
masteryStore2.recordAttempt('q1', true, 0, 'skill-b', 'guided_practice');
masteryStore2.recordAttempt('q1', true, 0, 'skill-b', 'guided_practice');
let masteryState2 = masteryStore2.getState();
let eval4 = evaluateSkillMastery('skill-b', masteryState2.skill_evidence['skill-b']);
assertEqual(eval4.mastered, false, '9.4 Duplicate question does not count twice');
assertEqual(eval4.evidence.correct_question_ids.length, 1, '9.4.1 Only 1 distinct question recorded');

// ============================================================
// TEST SUITE 10: CROSS-CHAPTER COMPATIBILITY
// ============================================================

console.log('\n=== TEST SUITE 10: Cross-Chapter Compatibility ===');

// Test 10.1: Chapter 1 tools work
const ch1Tools = createWebMCPTools(chapter1Data);
const ch1Outline = ch1Tools.getTopicOutline();
assertDefined(ch1Outline, '10.1 Chapter 1 getTopicOutline works');
assertEqual(ch1Outline.topic.id, 'chapter-1-real-numbers', '10.1.1 Chapter 1 topic ID correct');

// Test 10.2: Chapter 5 tools work
const ch5Tools = createWebMCPTools(chapter5Data);
const ch5Outline = ch5Tools.getTopicOutline();
assertDefined(ch5Outline, '10.2 Chapter 5 getTopicOutline works');
assertEqual(ch5Outline.topic.id, 'chapter-5-arithmetic-progressions', '10.2.1 Chapter 5 topic ID correct');

// Test 10.3: Chapter 1 prerequisite check works
const ch1Precheck = ch1Tools.getPrerequisiteCheck({ unit_id: chapter1Data.units[0].id });
assertDefined(ch1Precheck, '10.3 Chapter 1 prerequisite check works');
assertDefined(ch1Precheck.question, '10.3.1 Chapter 1 prerequisite question exists');

// Test 10.4: Chapter 5 unit content works
const ch5Content = ch5Tools.getUnitContent({ unit_id: chapter5Data.units[0].id });
assertDefined(ch5Content, '10.4 Chapter 5 unit content works');
assertDefined(ch5Content.core_concepts, '10.4.1 Chapter 5 core_concepts exists');
assertDefined(ch5Content.instruction, '10.4.1 Chapter 5 instruction exists');

// ============================================================
// TEST SUITE 11: NEXT-ACTION PROGRESSION REGRESSION
// ============================================================

console.log('\n=== TEST SUITE 11: Next-Action Progression Regression ===');

// Test 11.1: An attempted-but-UNSOLVED question must NOT be skipped by
// get_next_learning_action (regression: attempt records were previously
// treated as completed, advancing learners past questions they got wrong).
const progressStore = new StateStore({ useMemoryOnly: true });
const progressTools = createWebMCPTools(chapterData, progressStore);
const regressionUnit = chapterData.units[0];
const regressionQ = regressionUnit.practice_stages.guided_and_independent[0];
const wrongIndex = (regressionQ.correct_index + 1) % regressionQ.options.length;
progressTools.evaluateUnitPractice({
  question_id: regressionQ.id,
  selected_index: wrongIndex
}, progressStore);
const regressionNext = progressTools.getNextLearningAction({}, progressStore);
assertEqual(regressionNext.action, 'continue_practice', '11.1 Unsolved question NOT skipped (still continue_practice)');
assertEqual(regressionNext.next_question_id, regressionQ.id, '11.1.1 Engine recommends retrying the unsolved question');

// Test 11.2: After SOLVING the question, the engine advances to the next one
progressTools.evaluateUnitPractice({
  question_id: regressionQ.id,
  selected_index: regressionQ.correct_index
}, progressStore);
const solvedNext = progressTools.getNextLearningAction({}, progressStore);
assert(solvedNext.next_question_id !== regressionQ.id, '11.2 Solved question no longer recommended');

// ============================================================
// TEST SUITE 12: MASTERY EXAM SERVING & EVALUATION CLOSURE
// ============================================================

console.log('\n=== TEST SUITE 12: Mastery Exam Serving & Evaluation Closure ===');

// Test 12.1: combineTopicsToChapter populates the chapter mastery exam
const examData = chapterData.mastery && chapterData.mastery.chapter_mastery_gate;
assertDefined(examData, '12.1 Chapter mastery exam exists');
assert(examData.questions.length > 0, `12.1.1 Exam populated with questions (got ${examData.questions.length})`);
assert(examData.questions.length <= 10, '12.1.2 Exam capped at 10 questions');

// Test 12.1.3: Exam question IDs are unique
const examIds = examData.questions.map(q => q.id);
assertEqual(new Set(examIds).size, examIds.length, '12.1.3 Exam question IDs are unique');

// Test 12.2: start_mastery_exam serves the exam fully sanitized
const examToolsStore = new StateStore({ useMemoryOnly: true });
const examTools = createWebMCPTools(chapterData, examToolsStore);
const servedExam = examTools.startMasteryExam();
assertEqual(servedExam.total_questions, examData.questions.length, '12.2 Served exam matches populated exam size');
assert(!JSON.stringify(servedExam).includes('"correct_index":'), '12.2.1 Served exam hides correct_index');
assert(!JSON.stringify(servedExam).includes('"solution":'), '12.2.2 Served exam hides solution');

// Test 12.3: Evaluating every exam question records the final exam session
let lastExamResponse = null;
for (const eq of examData.questions) {
  lastExamResponse = examTools.evaluateUnitPractice({
    question_id: eq.id,
    selected_index: eq.correct_index
  }, examToolsStore);
}
assertDefined(lastExamResponse.exam_progress, '12.3 Exam progress tracked per submission');
assertEqual(lastExamResponse.exam_progress.answered, examData.questions.length, '12.3.1 All exam questions answered');
assertDefined(lastExamResponse.exam_result, '12.3.2 Exam result computed on final submission');
assertEqual(lastExamResponse.exam_result.score_percent, 100, '12.3.3 Perfect score recorded');
assertEqual(lastExamResponse.exam_result.passed, true, '12.3.4 Exam passed');
const examSession = examToolsStore.getState().mastery_exam_session;
assertDefined(examSession, '12.3.5 Exam session persisted in state store');
assertEqual(examSession.score, 100, '12.3.6 Persisted exam score correct');

// Test 12.4: A failing exam records passed=false
const failStore = new StateStore({ useMemoryOnly: true });
const failTools = createWebMCPTools(chapterData, failStore);
const halfIdx = Math.ceil(examData.questions.length / 2);
for (let i = 0; i < examData.questions.length; i++) {
  const eq = examData.questions[i];
  const idx = i < halfIdx ? eq.correct_index : (eq.correct_index + 1) % eq.options.length;
  failTools.evaluateUnitPractice({ question_id: eq.id, selected_index: idx }, failStore);
}
const failSession = failStore.getState().mastery_exam_session;
assertEqual(failSession.passed, false, '12.4 Failing exam marks passed=false');

// ============================================================
// TEST SUITE 13: PROGRESSIVE HINT GATING
// ============================================================

console.log('\n=== TEST SUITE 13: Progressive Hint Gating ===');

const hintStore = new StateStore({ useMemoryOnly: true });
const hintTools = createWebMCPTools(chapterData, hintStore);
const hintUnit = chapterData.units[0];
const hintQ = hintUnit.practice_stages.guided_and_independent[0];

// Test 13.1: Level 1 is always available (no attempts yet)
const freeHint = hintTools.getHint({ question_id: hintQ.id, hint_level: 1 }, hintStore);
assertEqual(freeHint.hint_level, 1, '13.1 Level 1 available without attempts');
assert(typeof freeHint.hint_text === 'string' && freeHint.hint_text.length > 0, '13.1.1 Level 1 hint text is a non-empty string');

// Test 13.2: Level 2 gated before any attempt
assertThrows(() => hintTools.getHint({ question_id: hintQ.id, hint_level: 2 }, hintStore), '13.2 Level 2 gated before any attempt');

// Test 13.3: Level 3 gated before any attempt
assertThrows(() => hintTools.getHint({ question_id: hintQ.id, hint_level: 3 }, hintStore), '13.3 Level 3 gated before any attempt');

// Test 13.4: Level 2 served after one attempt (incorrect)
hintTools.evaluateUnitPractice({
  question_id: hintQ.id,
  selected_index: (hintQ.correct_index + 1) % hintQ.options.length
}, hintStore);
const l2Hint = hintTools.getHint({ question_id: hintQ.id, hint_level: 2 }, hintStore);
assertEqual(l2Hint.hint_level, 2, '13.4 Level 2 served after an attempt');

// Test 13.5: Level 3 served after an incorrect attempt
const l3Hint = hintTools.getHint({ question_id: hintQ.id, hint_level: 3 }, hintStore);
assertEqual(l3Hint.hint_level, 3, '13.5 Level 3 served after an incorrect attempt');
assert(typeof l3Hint.hint_text === 'string' && l3Hint.hint_text.length > 0, '13.5.1 Level 3 hint text is a non-empty string');

// Test 13.6: Level 3 still gated when the only attempt was CORRECT
// (use a question from another unit so it has a clean attempt history)
const hintUnit2 = chapterData.units[1] || hintUnit;
const hintQ2 = hintUnit2.practice_stages.guided_and_independent[0] ||
  (chapterData.mastery.chapter_mastery_gate.questions[0] || hintQ);
hintTools.evaluateUnitPractice({
  question_id: hintQ2.id,
  selected_index: hintQ2.correct_index
}, hintStore);
assertThrows(() => hintTools.getHint({ question_id: hintQ2.id, hint_level: 3 }, hintStore), '13.6 Level 3 gated when only attempt was correct');

// ============================================================
// FINAL SUMMARY
// ============================================================

console.log('\n====================================================');
console.log(`TOTAL TESTS: ${totalTests}`);
console.log(`PASSED:      ${passedTests}`);
console.log(`FAILED:      ${failedTests}`);
console.log('====================================================');

if (failedTests > 0) {
  process.exit(1);
}
