/**
 * webmcp-tools.js
 * 
 * WebMCP Adapter for SJMaths CBSE Class 10 Mathematics Curriculum.
 * Browser-safe Vanilla JavaScript implementation of the 10 WebMCP tools.
 * 
 * Architecture:
 *   WebMCP Tool Request -> webmcp-tools.js (Adapter) -> Curriculum Catalog + Topic Data + State
 * 
 * Schema: Universal Schema v1.0.0
 * Coverage: Full CBSE Class 10 Mathematics (14 chapters, 43 topics)
 */

import { StateStore } from "./state-store.js";

// Per-process cache of parsed topic JSON files, keyed by catalog data_path.
// evaluate_practice/get_hint/get_topic_content all need the topic file; without the
// cache each question attempt re-reads and re-parses it from disk. Callers must
// treat returned objects as read-only (get_topic_content already clones via stripAnswers).
const topicJsonCache = new Map();
// Hoisted Node builtin imports (resolved once, reused by the fs fallback)
let nodeModsPromise = null;

export function createWebMCPTools(curriculumData, customStateStore = null) {
  if (!curriculumData) {
    throw new Error("WebMCP Tools require a valid CBSE Class 10 curriculum dataset.");
  }

  const defaultStore = customStateStore || new StateStore();
  const CATALOG = curriculumData;

  // Helper: canonical topic sequence across the whole curriculum (catalog order),
  // used to repair stale/broken previous_topic / next_topic pointers in content JSONs
  const TOPIC_SEQUENCE = [];
  for (const ch of CATALOG.chapters || []) {
    for (const t of ch.topics || []) {
      TOPIC_SEQUENCE.push({ id: t.id, title: t.title, data_path: t.data_path, chapter_id: ch.id, chapter_title: ch.title });
    }
  }
  function catalogTopicExists(id) {
    return TOPIC_SEQUENCE.some(t => t.id === id);
  }
  function catalogNeighbor(topic_id, dir) {
    const idx = TOPIC_SEQUENCE.findIndex(t => t.id === topic_id);
    if (idx === -1) return null;
    return TOPIC_SEQUENCE[idx + dir] || null;
  }
  // Resolve a content-authored pointer: trust it only if its id exists in the catalog,
  // otherwise fall back to the canonical catalog-sequence neighbor
  function resolveTopicPointer(pointer, topic_id, dir) {
    if (pointer?.id && catalogTopicExists(pointer.id)) {
      const cat = TOPIC_SEQUENCE.find(t => t.id === pointer.id);
      return { id: pointer.id, title: pointer.title || cat.title, data_path: cat.data_path, url: pointer.url || null };
    }
    return catalogNeighbor(topic_id, dir);
  }

  // Helper: locate a topic (and its chapter) in the catalog
  function findTopic(topic_id) {
    const rawId = topic_id.replace(/^math-foundations-/, '');
    for (const chapter of CATALOG.chapters || []) {
      const topic = (chapter.topics || []).find(t => t.id === topic_id || t.raw_id === topic_id || t.raw_id === rawId);
      if (topic) return { topic, chapter, dataPath: topic.data_path };
    }
    if (CATALOG.foundations) {
      const topic = (CATALOG.foundations.topics || []).find(t => t.id === topic_id || t.id === rawId || t.raw_id === rawId || `math-foundations-${t.id}` === topic_id);
      if (topic) return { topic, chapter: { id: "foundations", title: CATALOG.foundations.description }, dataPath: topic.data_path };
    }
    return null;
  }

  // Helper: fetch the full topic JSON via its catalog data_path (cached per process)
  async function fetchTopicJson(topic_id) {
    const found = findTopic(topic_id);
    if (!found || !found.dataPath) return null;
    if (topicJsonCache.has(found.dataPath)) return topicJsonCache.get(found.dataPath);
    const rawPath = found.dataPath.replace(/^\/+/, "");
    let json = null;
    const candidates = [
      "../../" + rawPath,
      "/" + rawPath,
      rawPath
    ];
    for (const p of candidates) {
      try {
        const response = await fetch(p);
        if (response.ok) {
          json = await response.json();
          break;
        }
      } catch (e) {}
    }
    // Node fallback (test-runner / offline verification): read from the repo root on disk
    if (!json && typeof process !== "undefined" && process.versions && process.versions.node) {
      try {
        if (!nodeModsPromise) {
          nodeModsPromise = Promise.all([
            import("node:fs/promises"), import("node:path"), import("node:url")
          ]);
        }
        const [{ readFile }, pathMod, { fileURLToPath }] = await nodeModsPromise;
        const repoRoot = pathMod.resolve(pathMod.dirname(fileURLToPath(import.meta.url)), "..", "..", "..");
        json = JSON.parse(await readFile(pathMod.join(repoRoot, found.dataPath), "utf8"));
      } catch (e) { /* topic file unreadable */ }
    }
    if (json) topicJsonCache.set(found.dataPath, json);
    return json;
  }

  // Helper: deep-clone and strip answer keys — assessment mode must never leak solutions
  const ANSWER_KEYS = ["is_correct", "correct_strategy_index", "correct_index", "correct_option_index", "correct_answer", "answer", "solution", "explanation", "option_details"];
  function stripAnswers(value) {
    if (Array.isArray(value)) return value.map(stripAnswers);
    if (value && typeof value === "object") {
      const clean = {};
      for (const [key, val] of Object.entries(value)) {
        if (ANSWER_KEYS.includes(key)) continue;
        clean[key] = stripAnswers(val);
      }
      return clean;
    }
    return value;
  }

  // Helper: locate a practice question inside a topic JSON's question-type pools
  function findQuestion(topicJson, question_id) {
    if (!topicJson || !Array.isArray(topicJson.question_types)) return null;
    const cleanId = String(question_id).trim().toLowerCase();
    
    // 1. Exact match
    for (const qt of topicJson.question_types) {
      const q = (qt.pool || []).find(item => item.id === question_id || String(item.id).toLowerCase() === cleanId);
      if (q) return q;
    }
    
    // 2. Loose prefix/suffix matching (e.g. "t1_p1" matches "fta_t1_p01_84" or "t1_p01")
    for (const qt of topicJson.question_types) {
      const q = (qt.pool || []).find(item => {
        const itemLow = String(item.id).toLowerCase();
        return itemLow.includes(cleanId) || cleanId.includes(itemLow);
      });
      if (q) return q;
    }

    // 3. Fallback: if asked for first question of first type (e.g. index 0 or generic id)
    if (topicJson.question_types.length && topicJson.question_types[0].pool && topicJson.question_types[0].pool.length) {
      return topicJson.question_types[0].pool[0];
    }

    return null;
  }

  // Tool 1: get_curriculum_outline
  function getCurriculumOutline(params = {}) {
    return {
      schema_version: CATALOG.schema_version,
      curriculum_id: CATALOG.catalog_info.id,
      title: CATALOG.catalog_info.title,
      board: CATALOG.catalog_info.board,
      class: CATALOG.catalog_info.class,
      subject: CATALOG.catalog_info.subject,
      total_chapters: CATALOG.catalog_info.total_chapters,
      total_topics: CATALOG.catalog_info.total_topics,
      chapters: (CATALOG.chapters || []).map(ch => ({
        id: ch.id,
        number: ch.number,
        title: ch.title,
        topic_count: (ch.topics || []).length
      })),
      foundations: CATALOG.foundations || null
    };
  }

  // Tool 2: get_chapter_topics
  function getChapterTopics(params = {}) {
    const chapter_id = params.chapter_id;
    if (!chapter_id) throw new Error("Parameter \"chapter_id\" is required.");
    const chapter = (CATALOG.chapters || []).find(ch => ch.id === chapter_id);
    if (!chapter) throw new Error(`Chapter "${chapter_id}" not found.`);
    return {
      chapter_id: chapter.id,
      chapter_number: chapter.number,
      title: chapter.title,
      description: chapter.description,
      topics: chapter.topics || []
    };
  }

  // Tool 3: get_topic_metadata
  function getTopicMetadata(params = {}) {
    const topic_id = params.topic_id;
    if (!topic_id) throw new Error("Parameter \"topic_id\" is required.");
    const found = findTopic(topic_id);
    if (!found) throw new Error(`Topic "${topic_id}" not found.`);
    return { chapter_id: found.chapter.id, chapter_title: found.chapter.title, topic: found.topic };
  }

  // Tool 4: get_topic_content
  async function getTopicContent(params = {}) {
    const topic_id = params.topic_id;
    if (!topic_id) throw new Error("Parameter \"topic_id\" is required.");
    const mode = params.mode || "assessment";
    const includeSolutions = mode === "study";
    const found = findTopic(topic_id);
    if (!found) throw new Error(`Topic "${topic_id}" not found.`);
    const topicMeta = found.topic, chapterMeta = found.chapter, dataPath = found.dataPath;

    // Fetch full content from the topic JSON file
    const fullContent = await fetchTopicJson(topic_id);

    const progression = fullContent?.stages?.progression || null;

    // Question type pools — answers stripped unless study mode
    const questionTypes = fullContent?.question_types || null;
    const questionTypeSummary = questionTypes
      ? questionTypes.map(qt => ({
          type_id: qt.type_id,
          type_title: qt.type_title,
          description: qt.description,
          pool_size: (qt.pool || []).length
        }))
      : null;
    const totalQuestions = questionTypes
      ? questionTypes.reduce((sum, qt) => sum + (qt.pool || []).length, 0)
      : 0;

    const result = {
      chapter_id: chapterMeta.id,
      chapter_title: chapterMeta.title,
      topic: {
        id: topicMeta.id,
        title: topicMeta.title,
        short_title: topicMeta.short_title,
        data_path: dataPath,
        stage_count: topicMeta.stage_count
      },
      mode: mode,
      content_loaded: !!fullContent,
      learning_stages: progression,
      stage_count: progression ? progression.length : 0,
      concepts: fullContent?.concepts || null,
      concept_count: fullContent?.concepts ? fullContent.concepts.length : 0,
      worked_examples: fullContent?.worked_examples || null,
      worked_example_count: fullContent?.worked_examples ? fullContent.worked_examples.length : 0,
      reference_drawer: fullContent?.reference_drawer || null,
      question_types: includeSolutions ? questionTypes : (questionTypes ? stripAnswers(questionTypes) : null),
      question_type_summary: questionTypeSummary,
      total_question_count: totalQuestions,
      previous_topic: resolveTopicPointer(fullContent?.previous_topic, topic_id, -1),
      next_topic: resolveTopicPointer(fullContent?.next_topic, topic_id, 1)
    };
    return result;
  }

  // Tool 4A: get_topic_concepts (Granular)
  async function getTopicConcepts(params = {}) {
    const topic_id = params.topic_id;
    if (!topic_id) throw new Error("Parameter \"topic_id\" is required.");
    const found = findTopic(topic_id);
    if (!found) throw new Error(`Topic "${topic_id}" not found.`);
    const fullContent = await fetchTopicJson(topic_id);
    return {
      topic_id: found.topic.id,
      topic_title: found.topic.title,
      chapter_title: found.chapter.title,
      concept_count: fullContent?.concepts ? fullContent.concepts.length : 0,
      concepts: fullContent?.concepts || [],
      reference_drawer: fullContent?.reference_drawer || null
    };
  }

  // Tool 4B: get_worked_examples (Granular)
  async function getWorkedExamples(params = {}) {
    const topic_id = params.topic_id;
    if (!topic_id) throw new Error("Parameter \"topic_id\" is required.");
    const found = findTopic(topic_id);
    if (!found) throw new Error(`Topic "${topic_id}" not found.`);
    const fullContent = await fetchTopicJson(topic_id);
    return {
      topic_id: found.topic.id,
      topic_title: found.topic.title,
      chapter_title: found.chapter.title,
      example_count: fullContent?.worked_examples ? fullContent.worked_examples.length : 0,
      worked_examples: fullContent?.worked_examples || []
    };
  }

  // Tool 4C: get_practice_questions (Granular)
  async function getPracticeQuestions(params = {}) {
    const topic_id = params.topic_id;
    if (!topic_id) throw new Error("Parameter \"topic_id\" is required.");
    const mode = params.mode || "assessment";
    const includeSolutions = mode === "study";
    const found = findTopic(topic_id);
    if (!found) throw new Error(`Topic "${topic_id}" not found.`);
    const fullContent = await fetchTopicJson(topic_id);
    const rawQuestionTypes = fullContent?.question_types || [];
    const questions = includeSolutions ? rawQuestionTypes : stripAnswers(rawQuestionTypes);
    const totalCount = (rawQuestionTypes || []).reduce((sum, qt) => sum + (qt.pool || []).length, 0);

    return {
      topic_id: found.topic.id,
      topic_title: found.topic.title,
      mode: mode,
      total_questions: totalCount,
      question_types: questions
    };
  }

  // Tool 5: get_prerequisite_check
  async function getPrerequisiteCheck(params = {}, store = defaultStore) {
    const topic_id = params.topic_id;
    if (!topic_id) throw new Error("Parameter \"topic_id\" is required.");
    const found = findTopic(topic_id);
    if (!found) throw new Error(`Topic "${topic_id}" not found.`);

    // Fetch the topic JSON for its explicit previous_topic pointer (only trusted if it resolves in the catalog)
    const fullContent = await fetchTopicJson(topic_id);
    const jsonPrev = (fullContent?.previous_topic?.id && catalogTopicExists(fullContent.previous_topic.id))
      ? fullContent.previous_topic : null;

    // Foundations topics are universal prerequisites across the curriculum
    const foundations = (CATALOG.foundations?.topics || []).map(t => ({
      id: t.id, title: t.title, data_path: t.data_path, kind: "foundation"
    }));

    const prerequisites = [];
    if (foundations.length) prerequisites.push(...foundations);
    if (jsonPrev?.id) {
      const cat = TOPIC_SEQUENCE.find(t => t.id === jsonPrev.id);
      prerequisites.push({ id: jsonPrev.id, title: jsonPrev.title || cat.title, data_path: cat.data_path, url: jsonPrev.url || null, kind: "previous_topic" });
    } else {
      // Fall back to the canonical previous topic in curriculum order (crosses chapter boundaries)
      const prevNeighbor = catalogNeighbor(topic_id, -1);
      if (prevNeighbor) prerequisites.push({ id: prevNeighbor.id, title: prevNeighbor.title, data_path: prevNeighbor.data_path, kind: "previous_topic" });
    }

    // Mastery state per prerequisite from the learning state store
    const state = store.getState();
    const mastered = state.mastered_skills || [];
    const completedTopics = state.completed_topics || [];
    const completedChapters = state.completed_chapters || [];
    const isMastered = (id) => {
      const raw = id.replace(/^math-foundations-/, '');
      return mastered.includes(id) || mastered.includes(raw) || mastered.includes(`math-foundations-${raw}`) ||
             completedTopics.includes(id) || completedTopics.includes(raw) || completedTopics.includes(`math-foundations-${raw}`) ||
             completedChapters.includes(id);
    };
    const withStatus = prerequisites.map(p => ({
      ...p,
      mastered: isMastered(p.id)
    }));

    return {
      topic_id: topic_id,
      prerequisite_count: withStatus.length,
      all_prerequisites_met: withStatus.every(p => p.mastered),
      prerequisites: withStatus
    };
  }

  // Question ids are only unique within a topic (e.g. "t1_p1" appears in many topics),
  // so per-question state must be keyed by topic + question to avoid cross-topic collisions
  function questionStateKey(topic_id, question_id) {
    return topic_id ? `${topic_id}:${question_id}` : question_id;
  }

  // Tool 6: evaluate_practice
  async function evaluatePractice(params = {}, store = defaultStore) {
    const question_id = params.question_id;
    const selected_index = params.selected_index;
    const topic_id = params.topic_id;
    if (!question_id) throw new Error("Parameter \"question_id\" is required.");
    if (selected_index === undefined || selected_index === null) throw new Error("Parameter \"selected_index\" is required.");

    // Validate the selection against the real answer key in the topic JSON when possible
    let is_correct = params.is_correct;
    let validated = false;
    if (topic_id) {
      const fullContent = await fetchTopicJson(topic_id);
      const question = findQuestion(fullContent, question_id);
      if (question && Array.isArray(question.steps) && question.steps.length) {
        const key = question.steps[0].correct_strategy_index;
        is_correct = selected_index === key;
        validated = true;
      }
    }
    if (is_correct === undefined) is_correct = false;

    store.recordAttempt(questionStateKey(topic_id, question_id), is_correct, selected_index, topic_id, "practice");
    const state = store.getState();
    const errorStreak = state.recent_error_streak || 0;
    return {
      question_id: question_id,
      selected_index: selected_index,
      is_correct: is_correct,
      validated_against_content: validated,
      error_streak: errorStreak,
      remediation_triggered: errorStreak >= 2
    };
  }

  // Tool 7: get_hint
  async function getHint(params = {}, store = defaultStore) {
    const question_id = params.question_id;
    const current_level = params.current_level || 0;
    if (!question_id) throw new Error("Parameter \"question_id\" is required.");
    const nextLevel = Math.min(current_level + 1, 3);
    const hintTypes = { 1: "conceptual", 2: "procedural", 3: "solution" };

    // Derive hint text from the question's own steps in the topic JSON when possible
    let hint_text = null;
    const topic_id = params.topic_id;
    if (topic_id) {
      const fullContent = await fetchTopicJson(topic_id);
      const question = findQuestion(fullContent, question_id);
      if (question && Array.isArray(question.steps) && question.steps.length) {
        const step = question.steps[0];
        if (nextLevel === 1) hint_text = step.focus || null;
        else if (nextLevel === 2) hint_text = step.strategy_question || null;
        else {
          const keyIdx = step.correct_strategy_index;
          hint_text = (step.strategy_options || [])[keyIdx] || null;
        }
      }
    }

    store.recordHintUsage(questionStateKey(topic_id, question_id), nextLevel);
    const result = { question_id: question_id, hint_level: nextLevel, hint_type: hintTypes[nextLevel], max_level: 3 };
    if (hint_text) result.hint_text = hint_text;
    return result;
  }

  // Tool 8: get_next_learning_action
  function getNextLearningAction(params = {}, store = defaultStore) {
    const state = store.getState();
    const errorStreak = state.recent_error_streak || 0;
    const completedTopics = state.completed_topics || [];
    const masteredSkills = state.mastered_skills || [];
    let action, reason;
    if (errorStreak >= 3) { action = "remediate"; reason = "Multiple errors. Review prerequisites."; }
    else if (errorStreak >= 2) { action = "hint"; reason = "Use a hint."; }
    else if (masteredSkills.length >= 5 || completedTopics.length >= 3) { action = "advance"; reason = "Ready for next chapter."; }
    else { action = "practice"; reason = "Continue practicing."; }
    return { action, reason, error_streak: errorStreak };
  }

  // Tool 9: start_mastery_exam
  function startMasteryExam(params = {}) {
    return {
      exam_id: "mastery-exam-all",
      title: "CBSE Class 10 Mathematics - Mastery Exam",
      total_questions: 10,
      pass_percent: 60,
      duration_minutes: 30
    };
  }

  // Tool 10: get_learning_progress
  function getLearningProgress(params = {}, store = defaultStore) {
    const state = store.getState();
    const completedChapters = state.completed_chapters || [];
    const completedTopics = state.completed_topics || [];
    const masteredSkills = state.mastered_skills || [];
    const solvedQuestions = Object.values(state.completed_questions || {}).filter(q => q && q.solved).length;
    const totalTopics = CATALOG.catalog_info.total_topics;
    const totalChapters = CATALOG.catalog_info.total_chapters;
    // Weighted: 70% topic completion, 30% chapter completion
    const progressPct = Math.round(
      70 * (completedTopics.length / Math.max(totalTopics, 1)) +
      30 * (completedChapters.length / Math.max(totalChapters, 1))
    );
    return {
      curriculum_id: CATALOG.catalog_info.id,
      overall_progress_percent: Math.min(progressPct, 100),
      chapters_completed: completedChapters.length,
      total_chapters: totalChapters,
      topics_completed: completedTopics.length,
      total_topics: totalTopics,
      skills_mastered: masteredSkills.length,
      questions_solved: solvedQuestions,
      current_topic_id: state.current_topic_id || null
    };
  }

  const TOOLS = {
    "get_curriculum_outline": getCurriculumOutline,
    "get_chapter_topics": getChapterTopics,
    "get_topic_metadata": getTopicMetadata,
    "get_topic_content": getTopicContent,
    "get_topic_concepts": getTopicConcepts,
    "get_worked_examples": getWorkedExamples,
    "get_practice_questions": getPracticeQuestions,
    "get_prerequisite_check": getPrerequisiteCheck,
    "evaluate_practice": evaluatePractice,
    "get_hint": getHint,
    "get_next_learning_action": getNextLearningAction,
    "start_mastery_exam": startMasteryExam,
    "get_learning_progress": getLearningProgress
  };

  async function executeTool(toolName, params = {}, customStore = defaultStore) {
    if (!toolName || typeof toolName !== "string") throw new Error("toolName must be a non-empty string.");
    const handler = TOOLS[toolName];
    if (!handler) throw new Error(`Unknown WebMCP tool: "${toolName}". Available tools: ${Object.keys(TOOLS).join(", ")}`);
    return await handler(params, customStore);
  }

  return {
    TOOLS, executeTool,
    getCurriculumOutline, getChapterTopics, getTopicMetadata, getTopicContent,
    getTopicConcepts, getWorkedExamples, getPracticeQuestions,
    getPrerequisiteCheck, evaluatePractice, getHint, getNextLearningAction,
    startMasteryExam, getLearningProgress
  };
}

export default { createWebMCPTools };