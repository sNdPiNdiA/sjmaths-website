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
assert(!JSON.stringify(outline).includes('correct_index'), '3.2 Outline does not contain correct_index');
assert(!JSON.stringify(outline).includes('solution'), '3.2.1 Outline does not contain solution');

// Test 3.3: Each unit in outline has expected fields
outline.units.forEach((unit, i) => {
  assertDefined(unit.id, `3.3 Unit ${i} has id`);
  assertDefined(unit.title, `3.3 Unit ${i} has title`);
});

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

// Test 5.1: Returns unit content
const unitContent = tools.getUnitContent({ unit_id: chapterData.units[0].id });
assertDefined(unitContent, '5.1 getUnitContent returns result');
assertDefined(unitContent.instruction, '5.1.1 Instruction exists');
assertDefined(unitContent.instruction.core_concepts, '5.1.2 Core concepts exist');

// Test 5.2: Does NOT leak answers or solutions
assert(!JSON.stringify(unitContent).includes('correct_index'), '5.2 correct_index is hidden');
assert(!JSON.stringify(unitContent).includes('solution'), '5.2.1 solution is hidden');

// Test 5.3: Error on invalid unit_id
assertThrows(() => tools.getUnitContent({ unit_id: 'nonexistent-unit' }), '5.3 Throws error for invalid unit_id');

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
assertDefined(ch5Content.instruction, '10.4.1 Chapter 5 instruction exists');

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
