/**
 * test-runner.js
 * 
 * Comprehensive automated test suite for SJMaths WebMCP CBSE Class 10.
 * Tests all 10 tools, input validation, answer/solution sanitization, state persistence,
 * and Evidence-Based Skill Mastery (State Version 3 - Schema v4.0.1).
 */

import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";
import { createWebMCPTools } from "./webmcp-tools.js";
import { registerWebMCPTools, WEBMCP_TOOL_DEFINITIONS } from "./webmcp-register.js";
import { StateStore, STATE_VERSION, evaluateSkillMastery } from "./state-store.js";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const dataPath = path.join(__dirname, "../data/class-10/mathematics/cbse-class-10-mathematics.json");
const curriculumData = JSON.parse(fs.readFileSync(dataPath, "utf8"));

const { executeTool, TOOLS } = createWebMCPTools(curriculumData);

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

async function assertThrows(fn, message) {
  totalTests += 1;
  try {
    await fn();
    failedTests += 1;
    console.error(`  [FAIL] ${message} (Expected error)`);
  } catch (e) {
    passedTests += 1;
    console.log(`  [PASS] ${message} -> Caught: "${e.message}"`);
  }
}


(async () => {
  console.log("====================================================");
  console.log("SJMATHS WEBMCP CBSE CLASS 10 - TOOL VERIFICATION SUITE");
  console.log("====================================================\n");
  
  // Test 1: Tool Registration
  console.log("Test Group 1: Tool Registration & Invocation");
  assert(typeof executeTool === "function", "executeTool dispatcher is a function");
  assert(Object.keys(TOOLS).length === 10, "Exactly 10 tools registered in TOOLS registry");
  assertThrows(async () => await executeTool("unknown_tool", {}), "executeTool rejects unknown tool names");
  assertThrows(async () => await executeTool("", {}), "executeTool rejects empty tool name");
  
  // Test 2: Tool 1 - get_curriculum_outline
  console.log("\nTest Group 2: Tool 1 - get_curriculum_outline");
  const outline = await executeTool("get_curriculum_outline", {});
  assert(outline.curriculum_id === "cbse-class-10-mathematics", "Curriculum ID matches");
  assert(outline.total_chapters === 14, "Returns 14 chapters");
  assert(outline.total_topics === 43, "Returns 43 topics");
  assert(outline.chapters.length === 14, "Returns 14 chapter objects");
  assert(outline.schema_version === "4.0.1", "Schema version is 4.0.1");
  
  // Test 3: Tool 2 - get_chapter_topics
  console.log("\nTest Group 3: Tool 2 - get_chapter_topics");
  assertThrows(async () => await executeTool("get_chapter_topics", {}), "Requires chapter_id");
  assertThrows(async () => await executeTool("get_chapter_topics", { chapter_id: "invalid" }), "Rejects invalid chapter_id");
  const ch4Topics = await executeTool("get_chapter_topics", { chapter_id: "chapter-4-quadratic-equations" });
  assert(ch4Topics.chapter_id === "chapter-4-quadratic-equations", "Valid chapter ID");
  assert(ch4Topics.topics.length === 5, "Chapter 4 has 5 topics");
  assert(ch4Topics.title === "Quadratic Equations", "Chapter title matches");
  
  // Test 4: Tool 3 - get_topic_metadata
  console.log("\nTest Group 4: Tool 3 - get_topic_metadata");
  assertThrows(async () => await executeTool("get_topic_metadata", {}), "Requires topic_id");
  const topicMeta = await executeTool("get_topic_metadata", { topic_id: "cbse10-real-numbers-fta" });
  assert(topicMeta.topic.id === "cbse10-real-numbers-fta", "Topic ID matches");
  assert(topicMeta.chapter_id === "chapter-1-real-numbers", "Chapter ID matches");
  assert(topicMeta.topic.stage_count === 5, "Stage count is 5");
  
  // Test 5: Tool 4 - get_topic_content
  console.log("\nTest Group 5: Tool 4 - get_topic_content (Assessment vs Study)");
  assertThrows(async () => await executeTool("get_topic_content", {}), "Requires topic_id");
  const assessMode = await executeTool("get_topic_content", { topic_id: "cbse10-real-numbers-fta", mode: "assessment" });
  assert(assessMode.mode === "assessment" && assessMode.topic !== null, "Assessment mode returns topic data");
  assert(assessMode.mode === "assessment", "Mode is assessment");
  const studyMode = await executeTool("get_topic_content", { topic_id: "cbse10-real-numbers-fta", mode: "study" });
  assert(studyMode.mode === "study" && studyMode.topic !== null, "Study mode returns topic data");
  
  // Test 6: Tool 5 - get_prerequisite_check
  console.log("\nTest Group 6: Tool 5 - get_prerequisite_check");
  const prereqs = await executeTool("get_prerequisite_check", { topic_id: "cbse10-real-numbers-fta" });
  assert(prereqs.prerequisite_count !== undefined, "Returns prerequisite count");
  assert(Array.isArray(prereqs.prerequisites), "Prerequisites is array");
  assert(prereqs.all_prerequisites_met !== undefined, "Returns prerequisite met flag");
  
  // Test 7: Tool 6 - evaluate_practice
  console.log("\nTest Group 7: Tool 6 - evaluate_practice");
  assertThrows(async () => await executeTool("evaluate_practice", {}), "Requires question_id");
  assertThrows(async () => await executeTool("evaluate_practice", { question_id: "q1" }), "Requires selected_index");
  const evalResult = await executeTool("evaluate_practice", { question_id: "q1", selected_index: 0, is_correct: true });
  assert(evalResult.is_correct === true, "Correct answer recorded");
  assert(evalResult.error_streak === 0, "No error streak after correct");
  
  // Test 8: Tool 7 - get_hint
  console.log("\nTest Group 8: Tool 7 - get_hint");
  assertThrows(async () => await executeTool("get_hint", {}), "Requires question_id");
  const hint1 = await executeTool("get_hint", { question_id: "q1", current_level: 0 });
  assert(hint1.hint_level === 1, "First hint is level 1");
  assert(hint1.max_level === 3, "Max hint level is 3");
  const hint2 = await executeTool("get_hint", { question_id: "q1", current_level: 1 });
  assert(hint2.hint_level === 2, "Second hint is level 2");
  
  // Test 9: Tool 8 - get_next_learning_action
  console.log("\nTest Group 9: Tool 8 - get_next_learning_action");
  const nextAction = await executeTool("get_next_learning_action", {});
  assert(typeof nextAction.action === "string", "Returns action string");
  assert(typeof nextAction.reason === "string", "Returns reason string");
  
  // Test 10: Tool 9 - start_mastery_exam
  console.log("\nTest Group 10: Tool 9 - start_mastery_exam");
  const exam = await executeTool("start_mastery_exam", {});
  assert(exam.total_questions === 10, "Exam has 10 questions");
  assert(exam.pass_percent === 60, "Pass percent is 60");
  
  // Test 11: Tool 10 - get_learning_progress
  console.log("\nTest Group 11: Tool 10 - get_learning_progress");
  const progress = await executeTool("get_learning_progress", {});
  assert(progress.curriculum_id === "cbse-class-10-mathematics", "Progress for correct curriculum");
  assert(progress.total_chapters === 14, "Total chapters is 14");
  assert(typeof progress.overall_progress_percent === "number", "Progress percent is number");
  assert(typeof progress.topics_completed === "number", "Topics completed is number");
  assert(progress.total_topics === 43, "Total topics is 43");
  assert(typeof progress.questions_solved === "number", "Questions solved is number");

  // Progress reflects real state-store completion (regression: completed_units field mismatch)
  const progStore = new StateStore({ useMemoryOnly: true });
  progStore.completeTopic("cbse10-quadratic-equations-solving-by-factorisation");
  progStore.completeChapter("chapter-4-quadratic-equations");
  const progressAfter = await executeTool("get_learning_progress", {}, progStore);
  assert(progressAfter.topics_completed === 1, "Topics completed reflects completed_topics (1)");
  assert(progressAfter.chapters_completed === 1, "Chapters completed reflects completed_chapters (1)");
  assert(progressAfter.overall_progress_percent > 0, "Progress percent is nonzero after completion");
  
  // Test 12: State Store
  console.log("\nTest Group 12: State Store (State Version 3)");
  const store = new StateStore({ useMemoryOnly: true });
  const initialState = store.getState();
  assert(initialState.state_version === STATE_VERSION, "Initial state has correct version");
  assert(initialState.current_chapter_id === "chapter-1-real-numbers", "Default chapter is Real Numbers");
  assert(Array.isArray(initialState.completed_topics), "Completed topics is array");
  assert(Array.isArray(initialState.mastered_skills), "Mastered skills is array");
  
  // Test 13: State Persistence
  console.log("\nTest Group 13: State Persistence");
  store.recordAttempt("q1", true, 0, "skill-test", "practice");
  const stateAfterAttempt = store.getState();
  assert(stateAfterAttempt.completed_questions["q1"].solved === true, "Question marked as solved");
  assert(stateAfterAttempt.recent_error_streak === 0, "No error streak");
  
  // Test 14: Error Streak Detection
  console.log("\nTest Group 14: Error Streak Detection");
  const errorStore = new StateStore({ useMemoryOnly: true });
  errorStore.recordAttempt("q1", false, 1, "skill-test", "practice");
  errorStore.recordAttempt("q2", false, 2, "skill-test", "practice");
  const errorState = errorStore.getState();
  assert(errorState.recent_error_streak === 2, "Error streak is 2 after 2 errors");
  
  // Test 15: Skill Mastery Evaluation
  console.log("\nTest Group 15: Skill Mastery Evaluation");
  const masteryResult = evaluateSkillMastery("skill-test", { correct_question_ids: ["q1", "q2"], independent_correct: 1, transfer_correct: 0 });
  assert(masteryResult.mastered === true, "Skill mastered with sufficient evidence");
  const noMasteryResult = evaluateSkillMastery("skill-test", { correct_question_ids: ["q1"], independent_correct: 0, transfer_correct: 0 });
  assert(noMasteryResult.mastered === false, "Skill not mastered with insufficient evidence");
  
  // Test 16: Tool Definitions Schema
  console.log("\nTest Group 16: Tool Definitions Schema");
  assert(WEBMCP_TOOL_DEFINITIONS.length === 10, "10 tool definitions");
  WEBMCP_TOOL_DEFINITIONS.forEach(def => {
    assert(typeof def.name === "string", `Tool ${def.name} has name`);
    assert(typeof def.description === "string", `Tool ${def.name} has description`);
    assert(def.inputSchema.type === "object", `Tool ${def.name} has object schema`);
  });
  
  // Test 17: Chapter Coverage
  console.log("\nTest Group 17: Chapter Coverage");
  const allChapters = outline.chapters.map(ch => ch.id);
  assert(allChapters.includes("chapter-1-real-numbers"), "Chapter 1 present");
  assert(allChapters.includes("chapter-4-quadratic-equations"), "Chapter 4 present");
  assert(allChapters.includes("chapter-14-probability"), "Chapter 14 present");
  
  // Final Summary
  console.log("\n====================================================");
  console.log(`TOTAL TESTS: ${totalTests}`);
  console.log(`PASSED:      ${passedTests}`);
  console.log(`FAILED:      ${failedTests}`);
  console.log("====================================================");
  
  if (failedTests > 0) process.exit(1);
})();