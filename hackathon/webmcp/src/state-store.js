/**
 * state-store.js
 * 
 * Client-side student state manager for SJMaths WebMCP.
 * Completely decoupled from curriculum content data.
 * Supports localStorage when available with seamless in-memory fallback.
 * Implements Evidence-Based Skill Mastery (State Version 3 - Schema v4.0.1).
 */

export const STATE_VERSION = 3;
const STORAGE_KEY = "sjmaths_cbse10_state_v3";
const LEGACY_STORAGE_KEY = "sjmaths_ch4_student_state_v2";

/** Creates a fresh, empty student state conforming to STATE_VERSION 3. */
export function createInitialState() {
  return {
    state_version: STATE_VERSION,
    current_chapter_id: "chapter-1-real-numbers",
    current_topic_id: "cbse10-real-numbers-fta",
    completed_chapters: [],
    completed_topics: [],
    mastered_skills: [],
    skill_evidence: {},
    completed_questions: {},
    recent_error_streak: 0,
    hint_usage: {},
    mastery_exam_session: null,
    last_updated: new Date().toISOString()
  };
}

/** Evaluates whether a skill meets the evidence-based mastery policy. */
export function evaluateSkillMastery(skillId, evidence) {
  if (!evidence) return { mastered: false, reason: "No evidence recorded.", evidence: null };
  const distinctCount = (evidence.correct_question_ids || []).length;
  const higherStageCount = (evidence.independent_correct || 0) + (evidence.transfer_correct || 0);
  if (distinctCount < 2) return { mastered: false, reason: `Insufficient distinct questions (${distinctCount}/2).`, evidence };
  if (higherStageCount < 1) return { mastered: false, reason: "Requires independent or transfer evidence.", evidence };
  return { mastered: true, reason: `Mastered with ${distinctCount} questions.`, evidence };
}

export class StateStore {
  constructor(options = {}) {
    this.useMemoryOnly = options.useMemoryOnly || typeof window === "undefined" || !window.localStorage;
    this.memoryState = createInitialState();
  }

  _hasLocalStorage() {
    if (this.useMemoryOnly) return false;
    try {
      const testKey = "__sjm_storage_test__";
      window.localStorage.setItem(testKey, "1");
      window.localStorage.removeItem(testKey);
      return true;
    } catch (e) { return false; }
  }

  getState() {
    if (this._hasLocalStorage()) {
      try {
        const raw = window.localStorage.getItem(STORAGE_KEY);
        if (raw) {
          const parsed = JSON.parse(raw);
          if (parsed && parsed.state_version === STATE_VERSION) return parsed;
        }
      } catch (e) { this.memoryState = createInitialState(); }
    }
    return this.memoryState;
  }

  saveState(state) {
    state.last_updated = new Date().toISOString();
    if (this._hasLocalStorage()) {
      try { window.localStorage.setItem(STORAGE_KEY, JSON.stringify(state)); return state; } catch (e) {}
    }
    this.memoryState = state;
    return state;
  }

  resetState() {
    const fresh = createInitialState();
    if (this._hasLocalStorage()) {
      try {
        window.localStorage.removeItem(STORAGE_KEY);
        window.localStorage.removeItem(LEGACY_STORAGE_KEY);
      } catch (e) {}
    }
    this.memoryState = fresh;
    return fresh;
  }

  recordAttempt(questionId, isCorrect, selectedIndex, skillId = null, stage = null) {
    const state = this.getState();
    if (!state.completed_questions[questionId]) {
      state.completed_questions[questionId] = { attempts: 0, solved: false, history: [] };
    }
    const qRec = state.completed_questions[questionId];
    qRec.attempts += 1;
    qRec.history.push({ selected_index: selectedIndex, is_correct: isCorrect, timestamp: new Date().toISOString() });
    if (isCorrect) {
      qRec.solved = true;
      state.recent_error_streak = 0;
      if (skillId && stage !== "prerequisite_check") {
        if (!state.skill_evidence[skillId]) {
          state.skill_evidence[skillId] = { correct_question_ids: [], guided_correct: 0, independent_correct: 0, transfer_correct: 0, total_correct: 0 };
        }
        const ev = state.skill_evidence[skillId];
        if (!ev.correct_question_ids.includes(questionId)) {
          ev.correct_question_ids.push(questionId);
          ev.total_correct += 1;
          if (stage === "guided_practice") ev.guided_correct += 1;
          else if (stage === "independent_solution") ev.independent_correct += 1;
          else if (stage === "transfer_mastery") ev.transfer_correct += 1;
          const masteryEval = evaluateSkillMastery(skillId, ev);
          if (masteryEval.mastered && !state.mastered_skills.includes(skillId)) {
            state.mastered_skills.push(skillId);
          }
        }
      }
    } else {
      state.recent_error_streak += 1;
    }
    return this.saveState(state);
  }

  recordHintUsage(questionId, level) {
    const state = this.getState();
    const currentLevel = state.hint_usage[questionId] || 0;
    if (level > currentLevel) state.hint_usage[questionId] = level;
    return this.saveState(state);
  }

  completeTopic(topicId) {
    const state = this.getState();
    if (!state.completed_topics.includes(topicId)) state.completed_topics.push(topicId);
    return this.saveState(state);
  }

  completeChapter(chapterId) {
    const state = this.getState();
    if (!state.completed_chapters.includes(chapterId)) state.completed_chapters.push(chapterId);
    return this.saveState(state);
  }

  recordExamResult(score, passed, totalQuestions) {
    const state = this.getState();
    state.mastery_exam_session = { completed_at: new Date().toISOString(), score, total_questions: totalQuestions, passed };
    return this.saveState(state);
  }
}

export default { STATE_VERSION, StateStore, createInitialState, evaluateSkillMastery };
