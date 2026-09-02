/**
 * state-store.js
 * 
 * Client-side student state manager for SJMaths WebMCP prototype.
 * Completely decoupled from curriculum content data.
 * Supports localStorage when available with seamless in-memory fallback.
 * Implements Evidence-Based Skill Mastery (State Version 2).
 */

export const STATE_VERSION = 2;

/**
 * Creates a fresh, empty student state conforming to STATE_VERSION 2.
 * @param {string} topicId - Optional topic ID for default unit initialization
 * @param {string} firstUnitId - Optional first unit ID to set as current
 */
export function createInitialState(topicId = null, firstUnitId = null) {
  return {
    state_version: STATE_VERSION,
    topic_id: topicId,
    current_unit_id: firstUnitId || null,
    completed_units: [],
    completed_topics: [],
    completed_chapters: [],
    mastered_skills: [],
    skill_evidence: {},
    completed_questions: {}, // question_id -> { attempts: count, solved: boolean, history: [] }
    recent_error_streak: 0,
    hint_usage: {},          // question_id -> max_hint_level_accessed
    mastery_exam_session: null, // { completed_at, score, total_questions, passed }
    last_updated: new Date().toISOString()
  };
}

/**
 * Evaluates whether a skill meets the evidence-based mastery policy.
 * 
 * Mastery Policy:
 * 1. At least 2 DISTINCT questions answered correctly.
 * 2. At least 1 of those correct answers comes from 'independent_solution' OR 'transfer_mastery'.
 * (Prechecks and guided-practice-only successes are insufficient).
 * 
 * @param {string} skillId 
 * @param {Object} evidence 
 * @returns {{ mastered: boolean, reason: string, evidence: Object }}
 */
export function evaluateSkillMastery(skillId, evidence) {
  if (!evidence) {
    return {
      mastered: false,
      reason: 'No evidence recorded for skill.',
      evidence: null
    };
  }

  const distinctCount = (evidence.correct_question_ids || []).length;
  const higherStageCount = (evidence.independent_correct || 0) + (evidence.transfer_correct || 0);

  if (distinctCount < 2) {
    return {
      mastered: false,
      reason: `Insufficient distinct questions solved (${distinctCount}/2 required).`,
      evidence
    };
  }

  if (higherStageCount < 1) {
    return {
      mastered: false,
      reason: 'Requires at least 1 correct answer from independent practice or transfer mastery.',
      evidence
    };
  }

  return {
    mastered: true,
    reason: `Mastery achieved with ${distinctCount} distinct questions (${evidence.guided_correct} guided, ${evidence.independent_correct} independent, ${evidence.transfer_correct} transfer).`,
    evidence
  };
}

export class StateStore {
  constructor(options = {}) {
    this.useMemoryOnly = options.useMemoryOnly || typeof window === 'undefined' || !window.localStorage;
    this.topicId = options.topicId || 'default';
    this.storageKey = `sjmaths_${this.topicId}_student_state_v2`;
    // Probe localStorage availability ONCE (a write/remove round-trip) and
    // cache the result, instead of re-probing on every getState/saveState.
    this._storageAvailable = !this.useMemoryOnly && this._probeLocalStorage();
    this.memoryState = createInitialState(this.topicId, options.firstUnitId);
  }

  _probeLocalStorage() {
    try {
      const testKey = '__sjm_storage_test__';
      window.localStorage.setItem(testKey, '1');
      window.localStorage.removeItem(testKey);
      return true;
    } catch (e) {
      return false;
    }
  }

  _hasLocalStorage() {
    return this._storageAvailable;
  }

  getState() {
    if (this._hasLocalStorage()) {
      try {
        const raw = window.localStorage.getItem(this.storageKey);
        if (raw) {
          const parsed = JSON.parse(raw);
          if (parsed && parsed.state_version === STATE_VERSION) {
            return parsed;
          }
          // State version mismatch or legacy state: invalidate & reset
          const fresh = createInitialState();
          this.saveState(fresh);
          return fresh;
        }
        // If legacy v1 key exists, clean it up
        const legacyKey = 'sjmaths_learning_student_state';
        if (window.localStorage.getItem(legacyKey)) {
          window.localStorage.removeItem(legacyKey);
          const fresh = createInitialState();
          this.saveState(fresh);
          return fresh;
        }
      } catch (e) {
        // Fall back to memory on parse error
      }
    }
    return JSON.parse(JSON.stringify(this.memoryState));
  }

  saveState(nextState) {
    nextState.state_version = STATE_VERSION;
    nextState.last_updated = new Date().toISOString();
    if (this._hasLocalStorage()) {
      try {
        window.localStorage.setItem(this.storageKey, JSON.stringify(nextState));
        return nextState;
      } catch (e) {
        // Fall back to memory on write error
      }
    }
    this.memoryState = JSON.parse(JSON.stringify(nextState));
    return nextState;
  }

  resetState() {
    const fresh = createInitialState();
    return this.saveState(fresh);
  }

  /**
   * Records a question attempt and updates error streak and skill evidence.
   * 
   * @param {string} questionId 
   * @param {boolean} isCorrect 
   * @param {number} selectedIndex 
   * @param {string|null} skillId 
   * @param {string|null} stage ('guided_practice', 'independent_solution', 'transfer_mastery', 'prerequisite_check', etc.)
   */
  recordAttempt(questionId, isCorrect, selectedIndex, skillId = null, stage = null) {
    const state = this.getState();

    if (!state.completed_questions[questionId]) {
      state.completed_questions[questionId] = {
        attempts: 0,
        solved: false,
        history: []
      };
    }

    const qRec = state.completed_questions[questionId];
    qRec.attempts += 1;
    qRec.history.push({
      selected_index: selectedIndex,
      is_correct: isCorrect,
      timestamp: new Date().toISOString()
    });

    if (isCorrect) {
      qRec.solved = true;
      state.recent_error_streak = 0;

      // Update skill evidence only for non-precheck questions with valid skill_id
      if (skillId && stage !== 'prerequisite_check') {
        if (!state.skill_evidence) {
          state.skill_evidence = {};
        }

        if (!state.skill_evidence[skillId]) {
          state.skill_evidence[skillId] = {
            correct_question_ids: [],
            guided_correct: 0,
            independent_correct: 0,
            transfer_correct: 0,
            total_correct: 0,
            mastery_status: 'in_progress',
            mastered_at: null
          };
        }

        const ev = state.skill_evidence[skillId];

        // Distinct question check: only increment evidence counters if this question was not already recorded
        if (!ev.correct_question_ids.includes(questionId)) {
          ev.correct_question_ids.push(questionId);
          ev.total_correct += 1;

          if (stage === 'guided_practice') {
            ev.guided_correct += 1;
          } else if (stage === 'independent_solution') {
            ev.independent_correct += 1;
          } else if (stage === 'transfer_mastery') {
            ev.transfer_correct += 1;
          }

          // Evaluate evidence-based mastery
          const masteryEval = evaluateSkillMastery(skillId, ev);
          if (masteryEval.mastered) {
            ev.mastery_status = 'mastered';
            if (!ev.mastered_at) {
              ev.mastered_at = new Date().toISOString();
            }
            if (!state.mastered_skills.includes(skillId)) {
              state.mastered_skills.push(skillId);
            }
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
    if (level > currentLevel) {
      state.hint_usage[questionId] = level;
    }
    return this.saveState(state);
  }

  completeUnit(unitId) {
    const state = this.getState();
    if (!state.completed_units.includes(unitId)) {
      state.completed_units.push(unitId);
    }
    return this.saveState(state);
  }

  markSkillMastered(skillId) {
    const state = this.getState();
    if (!state.mastered_skills) state.mastered_skills = [];
    if (!state.mastered_skills.includes(skillId)) {
      state.mastered_skills.push(skillId);
    }
    return this.saveState(state);
  }

  markTopicCompleted(topicId) {
    const state = this.getState();
    if (!state.completed_topics) state.completed_topics = [];
    if (!state.completed_topics.includes(topicId)) {
      state.completed_topics.push(topicId);
    }
    return this.saveState(state);
  }

  markChapterCompleted(chapterId) {
    const state = this.getState();
    if (!state.completed_chapters) state.completed_chapters = [];
    if (!state.completed_chapters.includes(chapterId)) {
      state.completed_chapters.push(chapterId);
    }
    return this.saveState(state);
  }

  resetRecentErrors() {
    const state = this.getState();
    state.recent_error_streak = 0;
    return this.saveState(state);
  }

  recordExamResult(score, passed, totalQuestions) {
    const state = this.getState();
    state.mastery_exam_session = {
      completed_at: new Date().toISOString(),
      score,
      total_questions: totalQuestions,
      passed
    };
    return this.saveState(state);
  }
}

export default {
  STATE_VERSION,
  StateStore,
  createInitialState,
  evaluateSkillMastery
};
