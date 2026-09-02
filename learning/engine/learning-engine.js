/**
 * learning-engine.js
 * 
 * Generic, topic-agnostic Learning Engine for SJMaths.
 * 
 * Functions as the orchestration layer between:
 *   Topic Data JSON (v3.3+)
 *   + Student State
 *   + Generic Stage Controller (stage-controller.js)
 * 
 * Exposes a normalized Learning Engine session API to WebMCP and UI layers.
 * Preserves curriculum immutability, assessment safety, and separates pedagogical dimensions.
 */

import {
  StageController,
  createStageController,
  normalizeStage,
  getStudentStageLabel,
  getStudentFacingTitle,
  INTERNAL_STAGES
} from './stage-controller.js';

/**
 * Creates and initializes a generic Learning Engine session instance.
 * 
 * @param {Object} options
 * @param {Object} options.topicData - Parsed Learning-Topic JSON (v3.3+ or v2.0+)
 * @param {Object} [options.studentState] - Initial student state object
 * @param {Object} [options.stateStore] - Optional external StateStore instance
 * @param {string} [options.currentStage] - Initial stage
 * @param {string} [options.unitId] - Initial unit identifier
 * @returns {LearningEngine}
 */
export function createLearningEngine({
  topicData,
  studentState = null,
  stateStore = null,
  currentStage = 'concept_learning',
  unitId = null
} = {}) {
  if (!topicData || typeof topicData !== 'object') {
    throw new Error('LearningEngine requires a valid topicData object.');
  }

  // Freeze curriculum dataset to guarantee immutability
  const DATA = Object.freeze(JSON.parse(JSON.stringify(topicData)));

  // Internal state management
  let state = studentState
    ? JSON.parse(JSON.stringify(studentState))
    : (stateStore ? stateStore.getState() : createInitialStudentState(DATA, currentStage, unitId));

  if (!state.current_stage) state.current_stage = normalizeStage(currentStage);
  if (!state.attempts) state.attempts = [];
  if (!state.error_streak) state.error_streak = 0;
  if (!state.hint_usage) state.hint_usage = {};
  if (!state.step_progress) state.step_progress = {};
  if (!state.completed_questions) state.completed_questions = {};
  // Guarantee every question item has a valid string ID
  if (DATA.units && typeof DATA.units === 'object' && !Array.isArray(DATA.units)) {
    for (const [uKey, uDef] of Object.entries(DATA.units)) {
      ['questions', 'question_pool', 'embedded_skill_practice', 'variants'].forEach(field => {
        if (Array.isArray(uDef[field])) {
          uDef[field].forEach((q, idx) => {
            if (!q.id) q.id = `${uKey}_${field}_${idx + 1}`;
          });
        }
      });
    }
  }

  let currentUnitId = unitId || state.current_unit || determineInitialUnitId(DATA);
  state.current_unit = currentUnitId;

  // Initialize stage controller
  let stageController = createStageController({
    topicData: DATA,
    studentState: state,
    unitId: currentUnitId,
    currentStage: state.current_stage
  });

  function syncController() {
    stageController = createStageController({
      topicData: DATA,
      studentState: state,
      unitId: currentUnitId,
      currentStage: state.current_stage
    });
  }

  // --------------------------------------------------------------------------
  // Question Lookup & Indexing Helpers
  // --------------------------------------------------------------------------

  function findQuestionById(questionId) {
    if (!questionId) return null;

    // 1. Topic v3.3 Units Object structure
    if (DATA.units && typeof DATA.units === 'object' && !Array.isArray(DATA.units)) {
      for (const [uKey, uDef] of Object.entries(DATA.units)) {
        if (Array.isArray(uDef.questions)) {
          const found = uDef.questions.find(q => q.id === questionId);
          if (found) return { item: found, unitId: uKey, stage: uDef.stage || uKey, type: uDef.type || 'practice' };
        }
        if (Array.isArray(uDef.question_pool)) {
          const found = uDef.question_pool.find(q => q.id === questionId);
          if (found) return { item: found, unitId: uKey, stage: uDef.stage || uKey, type: uDef.type || 'pool' };
        }
        if (Array.isArray(uDef.embedded_skill_practice)) {
          const found = uDef.embedded_skill_practice.find(q => q.id === questionId);
          if (found) return { item: found, unitId: uKey, stage: uDef.stage || uKey, type: 'embedded' };
        }
      }
    }

    // 2. Topic v2 Array of Units structure (Legacy / Chapter 4 compatibility)
    if (Array.isArray(DATA.units)) {
      for (const u of DATA.units) {
        if (u.prerequisite_check && u.prerequisite_check.id === questionId) {
          return { item: u.prerequisite_check, unitId: u.id, stage: 'prerequisite_check', type: 'precheck' };
        }
        if (u.practice_stages && Array.isArray(u.practice_stages.guided_and_independent)) {
          const found = u.practice_stages.guided_and_independent.find(q => q.id === questionId);
          if (found) return { item: found, unitId: u.id, stage: found.stage || 'guided_practice', type: 'practice' };
        }
        if (u.practice_stages && Array.isArray(u.practice_stages.transfer_and_pyq)) {
          const found = u.practice_stages.transfer_and_pyq.find(q => q.id === questionId);
          if (found) return { item: found, unitId: u.id, stage: found.stage || 'transfer_mastery', type: 'pyq' };
        }
        if (u.unit_mastery_gate && Array.isArray(u.unit_mastery_gate.questions)) {
          const found = u.unit_mastery_gate.questions.find(q => q.id === questionId);
          if (found) return { item: found, unitId: u.id, stage: 'mastery_gate', type: 'unit_test' };
        }
      }
    }

    // 3. Topic Prerequisites
    if (Array.isArray(DATA.prerequisites)) {
      const found = DATA.prerequisites.find(p => p.id === questionId);
      if (found) return { item: found, unitId: null, stage: 'prerequisite_check', type: 'precheck' };
    }

    // 4. Chapter Mastery Gate Exam
    if (DATA.mastery && DATA.mastery.chapter_mastery_gate && Array.isArray(DATA.mastery.chapter_mastery_gate.questions)) {
      const found = DATA.mastery.chapter_mastery_gate.questions.find(q => q.id === questionId);
      if (found) return { item: found, unitId: null, stage: 'mastery_gate', type: 'chapter_exam' };
    }

    return null;
  }

  // --------------------------------------------------------------------------
  // Core Engine Session API
  // --------------------------------------------------------------------------

  /**
   * Returns current learning state (UI safe).
   */
  function getLearningState() {
    syncController();
    const progress = stageController.getProgressState();
    return {
      topic_id: DATA.topic?.id || 'unknown_topic',
      topic_title: DATA.topic?.title || 'Unknown Topic',
      current_stage: state.current_stage,
      student_stage: getStudentStageLabel(state.current_stage),
      student_title: getStudentFacingTitle(state.current_stage),
      current_unit: state.current_unit,
      current_question_id: state.current_question_id || null,
      error_streak: state.error_streak || 0,
      skills_mastered_count: progress.skills_mastered_count,
      total_skills_count: progress.total_skills_count,
      is_topic_mastered: progress.is_topic_mastered,
      step_progress: state.step_progress || {}
    };
  }

  /**
   * Returns current pedagogical recommendation and next learning action.
   */
  function getCurrentLearningAction() {
    syncController();
    const decision = stageController.getNextDecision();
    const currentQ = state.current_question_id ? findQuestionById(state.current_question_id) : null;
    const nextQ = getNextQuestion();

    return {
      decision: decision.decision,
      from_stage: decision.from_stage,
      to_stage: decision.to_stage,
      student_stage: decision.student_stage,
      support_level: decision.support_level,
      reason: decision.reason,
      next_action: decision.next_action || (decision.decision === 'retry' ? 'contextual_retry' : 'present_next_question'),
      current_question: currentQ ? sanitizeQuestionForAssessment(currentQ.item) : null,
      next_question: nextQ ? sanitizeQuestionForAssessment(nextQ) : null,
      allow_retry: decision.allow_retry || false,
      remediation: decision.remediation_type ? stageController.getRemediationAction() : null,
      progress: stageController.getProgressState()
    };
  }

  /**
   * Submits an atomic interaction or full question answer.
   * Handles stepwise questions, input format verification, skill evidence,
   * error streaks, and invokes the StageController for pedagogical transitions.
   * 
   * @param {Object} payload
   * @param {string} payload.question_id
   * @param {string} [payload.stage]
   * @param {string|number} [payload.step_id]
   * @param {any} [payload.response]
   * @param {number} [payload.selected_index]
   * @param {boolean} [payload.is_correct]
   * @param {string} [payload.input_type]
   * @param {number} [payload.hints_used]
   * @param {Array<string>} [payload.skill_ids]
   * @param {boolean} [payload.is_format_error]
   * @returns {Object} Normalized evaluation response
   */
  function submitInteraction(payload = {}) {
    if (!payload.question_id) {
      throw new Error('Parameter "question_id" is required.');
    }

    let found = findQuestionById(payload.question_id);
    if (!found) {
      // Support passive stage transitions (e.g. concept_learning, worked_examples) where no question items exist
      const passiveStages = ['concept_learning', 'worked_examples', 'understanding_check'];
      const targetStage = normalizeStage(payload.stage || state.current_stage);
      if (passiveStages.includes(targetStage)) {
        found = {
          item: {
            id: payload.question_id,
            stage: targetStage,
            primary_skill_id: (Array.isArray(DATA.skills) && DATA.skills[0]?.id) || 'concept_overview'
          },
          stage: targetStage
        };
      } else {
        throw new Error(`Question "${payload.question_id}" not found.`);
      }
    }

    const qItem = found.item;
    const questionStage = normalizeStage(payload.stage || qItem.stage || found.stage || state.current_stage);

    // 1. Check for Input / Formatting Error First (Rule 9)
    const isFormatError = payload.is_format_error === true ||
      (payload.input_type === 'numeric' && payload.response !== undefined && (payload.response === null || isNaN(Number(payload.response)) || String(payload.response).trim() === ''));

    if (isFormatError) {
      syncController();
      const decision = stageController.getNextDecision({ isFormatError: true, reason_type: 'input_error' });
      return {
        result: 'input_error',
        is_correct: false,
        reason_type: 'input_error',
        message: DATA.student_experience?.student_messages?.input_retry || 'Check the value or format you entered and try again.',
        decision: decision.decision,
        current_stage: state.current_stage,
        student_stage: getStudentStageLabel(state.current_stage),
        next_action: 'contextual_retry',
        allow_retry: true
      };
    }

    // 2. Evaluate Correctness (Support atomic steps, selected_index, or explicit is_correct)
    const evaluation = evaluateInteractionCorrectness(qItem, payload);

    // If interaction is unsupported or malformed, return immediately without awarding evidence
    if (evaluation.reason_type === 'unsupported_interaction' || evaluation.isCorrect === undefined) {
      syncController();
      return {
        result: 'unsupported_interaction',
        is_correct: false,
        reason_type: 'unsupported_interaction',
        message: 'Unsupported interaction format or missing response.',
        decision: 'retry',
        current_stage: state.current_stage,
        student_stage: getStudentStageLabel(state.current_stage),
        next_action: 'contextual_retry',
        allow_retry: true
      };
    }

    const isCorrect = evaluation.isCorrect === true;
    const stepCompleted = evaluation.stepCompleted === true;
    const questionFullySolved = evaluation.questionFullySolved === true;
    const failedSkillId = evaluation.failedSkillId || qItem.primary_skill_id || (Array.isArray(qItem.skill_ids) ? qItem.skill_ids[0] : null);

    // 3. Update Error Streak & Hints
    const hintsUsedOnItem = payload.hints_used || (state.hint_usage && state.hint_usage[payload.question_id]) || 0;
    if (isCorrect) {
      state.error_streak = 0;
    } else {
      state.error_streak = (state.error_streak || 0) + 1;
    }

    // 4. Record Learner Evidence ONLY for validated attempts
    const attemptRecord = {
      question_id: payload.question_id,
      stage: questionStage,
      step_id: payload.step_id !== undefined ? payload.step_id : null,
      correct: isCorrect,
      hints_used: hintsUsedOnItem,
      support_level: payload.support_level !== undefined ? payload.support_level : (qItem.support_level !== undefined ? qItem.support_level : 2),
      skill_ids: payload.skill_ids || qItem.skill_ids || (qItem.skill ? [qItem.skill] : []),
      primary_skill_id: qItem.primary_skill_id || null,
      timestamp: Date.now()
    };
    state.attempts.push(attemptRecord);

    // Track completed question status
    if (questionFullySolved) {
      state.completed_questions[payload.question_id] = {
        solved: true,
        correct: isCorrect,
        hints_used: hintsUsedOnItem
      };
    }

    // Also update state store if connected
    if (stateStore && typeof stateStore.recordAttempt === 'function') {
      stateStore.recordAttempt(
        payload.question_id,
        isCorrect,
        payload.selected_index !== undefined ? payload.selected_index : (isCorrect ? 0 : 1),
        failedSkillId,
        questionStage
      );
    }

    // 5. Evaluate with StageController
    syncController();
    const decision = stageController.getNextDecision({
      questionId: payload.question_id,
      lastAttemptCorrect: isCorrect,
      failedStepSkillId: failedSkillId
    });

    // 6. Handle Stage Advancement if Decision is Advance
    if (decision.decision === 'advance' || decision.decision === 'start_transfer' || decision.decision === 'start_mastery') {
      state.current_stage = decision.to_stage;
      state.current_question_id = null; // Prepare for fresh question in next stage
      syncController();
    }

    // 7. Check Skill Mastery Updates
    const skillEval = stageController.evaluateSkills();
    const newlyMastered = [];
    for (const [sId, sRes] of Object.entries(skillEval.skills)) {
      if (sRes.mastered && !state.mastered_skills.includes(sId)) {
        state.mastered_skills.push(sId);
        newlyMastered.push(sId);
      }
    }

    // 8. Extract option-level and step-level pedagogical feedback / hint
    let optionFeedback = null;
    let optionHint = null;
    let mathematicalValidity = isCorrect ? 'valid_preferred' : 'invalid';

    if (payload.step_id !== undefined && Array.isArray(qItem.steps)) {
      const stepIdx = typeof payload.step_id === 'number' ? payload.step_id : parseInt(payload.step_id, 10);
      const step = qItem.steps[stepIdx];
      if (step) {
        const respKey = payload.divisor !== undefined ? String(payload.divisor) : (payload.response !== undefined ? String(payload.response) : null);
        if (respKey && step.options_feedback && step.options_feedback[respKey]) {
          const optMeta = step.options_feedback[respKey];
          optionFeedback = optMeta.feedback || null;
          optionHint = optMeta.hint || null;
          mathematicalValidity = optMeta.mathematical_validity || (isCorrect ? 'valid_preferred' : 'invalid');
        }
      }
    } else if (payload.selected_index !== undefined && qItem.options_feedback && Array.isArray(qItem.options_feedback)) {
      const optMeta = qItem.options_feedback[payload.selected_index];
      if (optMeta) {
        optionFeedback = optMeta.feedback || null;
        optionHint = optMeta.hint || null;
        mathematicalValidity = optMeta.mathematical_validity || (isCorrect ? 'valid_preferred' : 'invalid');
      }
    }

    const defaultFeedback = isCorrect
      ? (qItem.pass_feedback || 'Correct! Well done.')
      : (DATA.student_experience?.student_messages?.first_wrong || 'Not this time. Check your reasoning and try again.');

    // Build Normalized UI / WebMCP Safe Response
    return {
      result: isCorrect ? 'correct' : 'incorrect',
      is_correct: isCorrect,
      step_id: payload.step_id !== undefined ? payload.step_id : null,
      step_completed: stepCompleted,
      question_fully_solved: questionFullySolved,
      decision: decision.decision,
      current_stage: state.current_stage,
      student_stage: getStudentStageLabel(state.current_stage),
      support_level: decision.support_level,
      next_action: decision.next_action,
      allow_retry: decision.allow_retry || (!isCorrect && decision.decision === 'retry'),
      error_streak: state.error_streak,
      diagnosed_skill_id: decision.diagnosed_skill_id || null,
      remediation: decision.remediation_type ? stageController.getRemediationAction({ failedStepSkillId: failedSkillId }) : null,
      newly_mastered_skills: newlyMastered,
      progress: stageController.getProgressState(),
      feedback: optionFeedback || defaultFeedback,
      hint: optionHint || null,
      mathematical_validity: mathematicalValidity
    };
  }

  /**
   * Evaluates atomic correctness for diverse question models (options, numeric steps, formulas).
   * Fully topic-agnostic: derives step skills from step definition or question metadata.
   */
  function evaluateInteractionCorrectness(qItem, payload) {
    // A. Multiple Choice / Options
    if (payload.selected_index !== undefined && Array.isArray(qItem.options)) {
      const isOutOfBounds = payload.selected_index < 0 || payload.selected_index >= qItem.options.length;
      if (isOutOfBounds) {
        return { isCorrect: false, stepCompleted: false, questionFullySolved: false, reason_type: 'unsupported_interaction' };
      }
      const correctIdx = qItem.correct_index !== undefined ? qItem.correct_index : 0;
      const isCorrect = payload.selected_index === correctIdx;
      return { isCorrect, stepCompleted: true, questionFullySolved: true };
    }

    // B. Explicit is_correct boolean in payload (e.g. from validated client grading)
    if (payload.is_correct !== undefined && typeof payload.is_correct === 'boolean') {
      return { isCorrect: payload.is_correct, stepCompleted: true, questionFullySolved: true };
    }

    // C. Stepwise Solutions (e.g. multi-step procedural tasks)
    if (Array.isArray(qItem.steps) && payload.step_id !== undefined) {
      const stepIdx = typeof payload.step_id === 'number' ? payload.step_id : parseInt(payload.step_id, 10);
      if (isNaN(stepIdx) || stepIdx < 0 || stepIdx >= qItem.steps.length) {
        return { isCorrect: false, stepCompleted: false, questionFullySolved: false, reason_type: 'unsupported_interaction' };
      }

      const step = qItem.steps[stepIdx];
      if (!step) {
        return { isCorrect: false, stepCompleted: false, questionFullySolved: false, reason_type: 'unsupported_interaction' };
      }

      // Step targets can be defined in object form or array form
      let expectedDivisor = step.correct_divisor !== undefined ? step.correct_divisor : (Array.isArray(step) ? step[1] : null);
      let expectedQuotient = step.quotient !== undefined ? step.quotient : (Array.isArray(step) ? step[2] : null);

      // Derive step skill dynamically from step metadata if present, else fallback to question skills
      const stepDivisorSkill = step.divisor_skill_id || step.skill_id || (Array.isArray(qItem.skill_ids) ? qItem.skill_ids[0] : qItem.primary_skill_id);
      const stepQuotientSkill = step.quotient_skill_id || step.skill_id || (Array.isArray(qItem.skill_ids) && qItem.skill_ids.length > 1 ? qItem.skill_ids[1] : qItem.primary_skill_id);

      let isCorrect = true;
      let failedSkill = null;
      let evaluatedAny = false;

      if (payload.divisor !== undefined && expectedDivisor !== null) {
        evaluatedAny = true;
        if (Number(payload.divisor) !== Number(expectedDivisor)) {
          isCorrect = false;
          failedSkill = stepDivisorSkill;
        }
      }

      if (isCorrect && payload.quotient !== undefined && expectedQuotient !== null) {
        evaluatedAny = true;
        if (Number(payload.quotient) !== Number(expectedQuotient)) {
          isCorrect = false;
          failedSkill = stepQuotientSkill;
        }
      }

      if (!evaluatedAny && payload.selected_index !== undefined && Array.isArray(step.options)) {
        evaluatedAny = true;
        const correctVal = step.correct !== undefined ? step.correct : step.answer;
        const userChoice = step.options[payload.selected_index];
        isCorrect = userChoice === correctVal || payload.selected_index === step.correct_index || payload.selected_index === step.correct_option_index;
        if (!isCorrect) failedSkill = step.skill_id || qItem.primary_skill_id;
      }

      if (!evaluatedAny && payload.response !== undefined) {
        evaluatedAny = true;
        const respNum = Number(payload.response);
        if (payload.input_type === 'divisor' && expectedDivisor !== null) {
          isCorrect = respNum === Number(expectedDivisor);
          if (!isCorrect) failedSkill = stepDivisorSkill;
        } else if (payload.input_type === 'quotient' && expectedQuotient !== null) {
          isCorrect = respNum === Number(expectedQuotient);
          if (!isCorrect) failedSkill = stepQuotientSkill;
        } else if (step.correct !== undefined || step.answer !== undefined) {
          const normalizeMathString = (str) => {
            if (str === undefined || str === null) return '';
            return String(str)
              .replace(/\s+/g, '')
              .replace(/\\times/g, '×')
              .replace(/\*/g, '×')
              .replace(/x/g, '×')
              .replace(/\^2/g, '²')
              .replace(/\^3/g, '³')
              .replace(/\^4/g, '⁴')
              .replace(/\^5/g, '⁵')
              .toLowerCase();
          };
          const userNorm = normalizeMathString(payload.response);
          const expNorm1 = step.correct !== undefined ? normalizeMathString(step.correct) : null;
          const expNorm2 = step.answer !== undefined ? normalizeMathString(step.answer) : null;
          isCorrect = (expNorm1 && (userNorm === expNorm1 || userNorm.includes(expNorm1) || expNorm1.includes(userNorm))) ||
                      (expNorm2 && (userNorm === expNorm2 || userNorm.includes(expNorm2) || expNorm2.includes(userNorm)));
          if (!isCorrect) failedSkill = step.skill_id || qItem.primary_skill_id;
        } else {
          isCorrect = false;
          failedSkill = qItem.primary_skill_id;
        }
      }

      if (!evaluatedAny) {
        return { isCorrect: false, stepCompleted: false, questionFullySolved: false, reason_type: 'unsupported_interaction' };
      }

      const isLastStep = stepIdx >= qItem.steps.length - 1;
      return {
        isCorrect,
        stepCompleted: isCorrect,
        questionFullySolved: isCorrect && isLastStep,
        failedSkillId: failedSkill,
        feedback: isCorrect ? (step.feedback?.correct || 'Correct!') : (step.feedback?.wrong || step.hint || 'Check your reasoning.')
      };
    }

    // D. Final Answer Comparison (String, numeric, or mathematical formula)
    if (payload.response !== undefined && (qItem.answer !== undefined || qItem.exponential_answer !== undefined || qItem.expanded_answer !== undefined || qItem.options !== undefined)) {
      if (typeof payload.response !== 'string' && typeof payload.response !== 'number') {
        return { isCorrect: false, stepCompleted: false, questionFullySolved: false, reason_type: 'unsupported_interaction' };
      }
      const normalizeMathString = (str) => {
        if (str === undefined || str === null) return '';
        return String(str)
          .replace(/\s+/g, '')
          .replace(/\\times/g, '×')
          .replace(/\*/g, '×')
          .replace(/x/g, '×')
          .replace(/\^2/g, '²')
          .replace(/\^3/g, '³')
          .replace(/\^4/g, '⁴')
          .replace(/\^5/g, '⁵')
          .replace(/²/g, '²')
          .replace(/³/g, '³')
          .replace(/⁴/g, '⁴')
          .toLowerCase();
      };

      const normUser = normalizeMathString(payload.response);
      const possibleAnswers = [
        normalizeMathString(qItem.answer),
        normalizeMathString(qItem.exponential_answer),
        normalizeMathString(qItem.expanded_answer),
        normalizeMathString(qItem.corrected_answer),
        qItem.options && qItem.correct_option_index !== undefined ? normalizeMathString(qItem.options[qItem.correct_option_index]) : null
      ].filter(Boolean);

      const isCorrect = possibleAnswers.some(ans => ans === normUser || (ans.length > 5 && normUser.includes(ans)) || (normUser.length > 5 && ans.includes(normUser)));
      return {
        isCorrect,
        stepCompleted: true,
        questionFullySolved: true,
        feedback: isCorrect ? (qItem.solution?.explanation || 'Correct!') : (qItem.hints?.level_1 || 'Check your reasoning.')
      };
    }

    // D2. Multiple Choice selected_index evaluation
    if (payload.selected_index !== undefined && Array.isArray(qItem.options)) {
      const correctIdx = qItem.correct_option_index !== undefined ? qItem.correct_option_index : (qItem.correct_index !== undefined ? qItem.correct_index : 0);
      const isCorrect = payload.selected_index === correctIdx;
      return {
        isCorrect,
        stepCompleted: true,
        questionFullySolved: true,
        feedback: isCorrect ? (qItem.solution?.explanation || 'Correct!') : (qItem.hints?.level_1 || 'Check your reasoning.')
      };
    }

    // E. Hardened Fallback: Unsupported interaction must NEVER award learner evidence
    return {
      isCorrect: false,
      stepCompleted: false,
      questionFullySolved: false,
      reason_type: 'unsupported_interaction'
    };
  }

  /**
   * Requests a progressive hint for a question (Assessment Safe).
   * 
   * @param {Object} payload { question_id, hint_level }
   * @returns {Object} Hint response
   */
  function requestHint(payload = {}) {
    if (!payload.question_id) {
      throw new Error('Parameter "question_id" is required.');
    }
    const level = payload.hint_level || 1;
    if (level < 1 || level > 3) {
      throw new Error('Parameter "hint_level" must be 1, 2, or 3.');
    }

    const found = findQuestionById(payload.question_id);
    if (!found) {
      throw new Error(`Question "${payload.question_id}" not found.`);
    }

    // Record hint usage (does not invalidate future correct response)
    state.hint_usage[payload.question_id] = Math.max(state.hint_usage[payload.question_id] || 0, level);

    const q = found.item;
    let hintText = '';

    // 0. Step-level hints if step_id provided
    if (payload.step_id !== undefined && Array.isArray(q.steps)) {
      const stepIdx = typeof payload.step_id === 'number' ? payload.step_id : parseInt(payload.step_id, 10);
      const step = q.steps[stepIdx];
      if (step && step.hints) {
        if (step.hints[`level_${level}`]) {
          hintText = step.hints[`level_${level}`];
        } else if (Array.isArray(step.hints) && step.hints[level - 1]) {
          hintText = step.hints[level - 1];
        }
      }
    }

    // 1. Question-level hints
    if (!hintText) {
      if (q.hints && q.hints[`level_${level}`]) {
        hintText = q.hints[`level_${level}`];
      } else if (q.hints && Array.isArray(q.hints) && q.hints[level - 1]) {
        hintText = q.hints[level - 1];
      }
    }

    // 2. Unit/Stage level hints
    if (!hintText && DATA.units && DATA.units[state.current_stage]?.hints) {
      const stageHints = DATA.units[state.current_stage].hints;
      hintText = stageHints[`level_${level}`] || stageHints[level - 1] || '';
    }

    // 3. Topic-level generic hint policy fallback
    if (!hintText && DATA.hint_system?.levels) {
      const hDef = DATA.hint_system.levels.find(h => h.level === level);
      if (hDef) hintText = hDef.example || hDef.type || '';
    }

    // 4. Default pedagogical fallback
    if (!hintText) {
      const fallbacks = {
        1: 'Review the underlying rule and divisibility properties for this step.',
        2: 'Identify the smallest prime divisor or isolate the variable before calculating.',
        3: q.solution ? 'Full derivation available after attempt.' : 'Perform division or simplification step-by-step.'
      };
      hintText = fallbacks[level] || 'Consider the key concept for this question.';
    }

    return {
      question_id: payload.question_id,
      hint_level: level,
      hint_text: hintText,
      hints_used_so_far: state.hint_usage[payload.question_id]
    };
  }

  /**
   * Question selection taking into account:
   * - stage & unit
   * - task_type cognitive variation (Rule 13 & 8)
   * - support level
   * - unanswered questions vs already solved
   * - skill coverage
   */
  function getNextQuestion() {
    syncController();
    const stage = state.current_stage;
    const completedMap = state.completed_questions || {};
    const solvedIds = Object.keys(completedMap).filter(k => completedMap[k]?.solved);

    const candidatePool = [];

    // Collect candidates from current stage unit
    if (DATA.units && DATA.units[stage]) {
      const unit = DATA.units[stage];
      if (Array.isArray(unit.questions)) candidatePool.push(...unit.questions);
      if (Array.isArray(unit.question_pool)) candidatePool.push(...unit.question_pool);
      if (Array.isArray(unit.embedded_skill_practice)) candidatePool.push(...unit.embedded_skill_practice);
    }

    // Also search legacy units practice stages if candidate pool empty
    if (candidatePool.length === 0 && Array.isArray(DATA.units)) {
      for (const u of DATA.units) {
        if (u.practice_stages && Array.isArray(u.practice_stages.guided_and_independent)) {
          const matching = u.practice_stages.guided_and_independent.filter(q => normalizeStage(q.stage) === stage);
          candidatePool.push(...matching);
        }
        if (u.practice_stages && Array.isArray(u.practice_stages.transfer_and_pyq)) {
          const matching = u.practice_stages.transfer_and_pyq.filter(q => normalizeStage(q.stage) === stage);
          candidatePool.push(...matching);
        }
      }
    }

    if (candidatePool.length === 0) return null;

    // Filter out already solved questions (Fresh questions preferred)
    let freshQuestions = candidatePool.filter(q => !solvedIds.includes(q.id));
    if (freshQuestions.length === 0) {
      freshQuestions = candidatePool; // Recycle pool if all solved
    }

    // Cognitive variation: Avoid consecutive same task_type (Rule 13)
    const lastAttempt = state.attempts[state.attempts.length - 1];
    let lastTaskType = null;
    if (lastAttempt) {
      const lastQ = findQuestionById(lastAttempt.question_id);
      lastTaskType = lastQ?.item?.task_type || null;
    }

    if (lastTaskType && freshQuestions.length > 1) {
      const varied = freshQuestions.filter(q => q.task_type && q.task_type !== lastTaskType);
      if (varied.length > 0) {
        return sanitizeQuestionForAssessment(varied[0]);
      }
    }

    return sanitizeQuestionForAssessment(freshQuestions[0]) || null;
  }

  /**
   * Sanitizes question object to prevent answer / solution leaks in assessment mode (Rule 14).
   */
  function sanitizeQuestionForAssessment(q) {
    if (!q) return null;
    const sanitized = {
      id: q.id,
      number: q.number,
      question: q.question,
      task_type: q.task_type,
      stage: q.stage,
      support_level: q.support_level,
      difficulty: q.difficulty,
      primary_skill_id: q.primary_skill_id,
      skill_ids: q.skill_ids,
      prime_factorisations: q.prime_factorisations ? { ...q.prime_factorisations } : (q.prime_factorizations ? { ...q.prime_factorizations } : undefined),
      options: q.options ? [...q.options] : undefined,
      steps: q.steps ? q.steps.map((s, idx) => {
        if (Array.isArray(s)) return { step_id: idx, current: s[0] };
        if (typeof s === 'object') {
          return {
            step_id: idx,
            current: s.current,
            focus: s.focus,
            prompt: s.prompt,
            options: s.options ? [...s.options] : undefined,
            divisors: s.divisors ? [...s.divisors] : undefined,
            options_feedback: s.options_feedback ? { ...s.options_feedback } : undefined
          };
        }
        return { step_id: idx };
      }) : undefined
    };
    return sanitized;
  }

  /**
   * Returns topic outline metadata.
   */
  function getTopicOutline() {
    return {
      topic: {
        id: DATA.topic?.id,
        title: DATA.topic?.title,
        grade: DATA.topic?.grade || DATA.topic?.class,
        subject: DATA.topic?.subject,
        standard: DATA.topic?.standard || DATA.topic?.board,
        description: DATA.topic?.description || DATA.topic?.title
      },
      scope: DATA.scope,
      sequence: DATA.sequence,
      skills: DATA.skills,
      units: Array.isArray(DATA.units)
        ? DATA.units.map(u => ({ id: u.id, title: u.title, skills_covered: u.skills_covered }))
        : Object.keys(DATA.units || {}).map(uKey => ({ id: uKey, title: DATA.units[uKey].title || uKey }))
    };
  }

  /**
   * Returns unit content and practice items.
   */
  function getUnitContent(params = {}) {
    const uId = params.unit_id || state.current_unit;
    if (!uId) throw new Error('Parameter "unit_id" is required.');

    // 1. Support v2 legacy unit array
    if (Array.isArray(DATA.units)) {
      const unit = DATA.units.find(u => u.id === uId);
      if (!unit) throw new Error(`Unit "${uId}" not found.`);

      const mode = params.mode || 'assessment';
      const result = {
        unit_id: unit.id,
        unit_number: unit.unit_number,
        title: unit.title,
        instruction: unit.instruction || { core_concepts: [] }
      };

      if (params.include_practice) {
        const practice = (unit.practice_stages?.guided_and_independent || []).map(q => {
          const item = {
            id: q.id,
            stage: q.stage,
            skill_id: q.skill_id,
            question: q.question,
            options: q.options
          };
          if (mode === 'study') {
            item.correct_index = q.correct_index;
            item.solution = q.solution;
          }
          return item;
        });

        const pyqs = (unit.practice_stages?.transfer_and_pyq || []).map(q => {
          const item = {
            id: q.id,
            stage: q.stage,
            skill_id: q.skill_id,
            question: q.question,
            options: q.options
          };
          if (mode === 'study') {
            item.correct_index = q.correct_index;
            item.solution = q.solution;
          }
          return item;
        });

        result.practice_questions = practice.concat(pyqs);
      }
      return result;
    }

    // 2. Support v3.3 unit object map
    if (DATA.units && DATA.units[uId]) {
      const uDef = DATA.units[uId];
      return {
        unit_id: uId,
        title: uDef.title,
        type: uDef.type,
        support_level: uDef.support_level,
        questions: (uDef.questions || []).map(q => sanitizeQuestionForAssessment(q))
      };
    }

    throw new Error(`Unit "${uId}" not found.`);
  }

  /**
   * Diagnostic prerequisite check.
   */
  function getPrerequisiteCheck(params = {}) {
    const uId = params.unit_id || state.current_unit;
    if (!uId) throw new Error('Parameter "unit_id" is required.');

    // 1. Check v2 unit prerequisite
    if (Array.isArray(DATA.units)) {
      const unit = DATA.units.find(u => u.id === uId);
      if (!unit) throw new Error(`Unit "${uId}" not found.`);
      if (!unit.prerequisite_check) throw new Error(`No prerequisite check defined for unit "${uId}".`);
      return {
        unit_id: unit.id,
        check_id: unit.prerequisite_check.id,
        question: unit.prerequisite_check.question,
        options: unit.prerequisite_check.options
      };
    }

    // 2. Check v3.3 prerequisite_check unit
    if (DATA.units?.prerequisite_check) {
      const pUnit = DATA.units.prerequisite_check;
      const firstQ = (pUnit.questions && pUnit.questions[0]) || {};
      return {
        unit_id: 'prerequisite_check',
        check_id: firstQ.id || 'pre_01',
        question: firstQ.question,
        options: firstQ.options
      };
    }

    throw new Error(`Unit "${uId}" not found.`);
  }

  /**
   * Cumulative chapter mastery exam.
   */
  function startMasteryExam(params = {}) {
    const exam = (DATA.mastery && DATA.mastery.chapter_mastery_gate) || {
      assessment_id: 'mastery-exam-default',
      title: 'Chapter Mastery Exam',
      pass_percent: 80,
      questions: []
    };

    const sanitizedQuestions = (exam.questions || []).map(q => ({
      id: q.id,
      skill_id: q.skill_id,
      question: q.question,
      options: q.options
    }));

    return {
      assessment_id: exam.assessment_id,
      title: exam.title,
      pass_percent: exam.pass_percent,
      total_questions: sanitizedQuestions.length,
      questions: sanitizedQuestions
    };
  }

  /**
   * Progress reporting.
   */
  function getLearningProgress(params = {}, store = null) {
    syncController();
    const st = store ? store.getState() : state;
    const completedUnits = st.completed_units || [];
    const masteredSkills = st.mastered_skills || [];

    const totalUnits = Array.isArray(DATA.units) ? DATA.units.length : Object.keys(DATA.units || {}).length;
    const totalSkills = Object.keys(DATA.skills || {}).length;

    const progressPct = totalSkills > 0 ? Math.round((masteredSkills.length / totalSkills) * 100) : 0;

    return {
      topic_id: DATA.topic?.id || 'unknown_topic',
      topic_title: DATA.topic?.title || 'Unknown Topic',
      overall_progress_percent: progressPct,
      units_completed_count: completedUnits.length,
      total_units: totalUnits,
      skills_mastered_count: masteredSkills.length,
      total_skills: totalSkills,
      current_stage: state.current_stage,
      student_stage: getStudentStageLabel(state.current_stage),
      is_topic_mastered: masteredSkills.length >= totalSkills
    };
  }

  // Legacy evaluation compatibility adapter for existing WebMCP tests
  function evaluatePractice(params = {}, store = null) {
    const qId = params.question_id;
    const sIdx = params.selected_index;
    const found = findQuestionById(qId);
    if (!found) throw new Error(`Question "${qId}" not found.`);
    if (typeof sIdx !== 'number') throw new Error('Parameter "selected_index" must be a number.');

    const q = found.item;
    if (q.options && (sIdx < 0 || sIdx >= q.options.length)) {
      throw new Error(`selected_index ${sIdx} is out of bounds (options length: ${q.options.length}).`);
    }

    const isCorrect = sIdx === (q.correct_index !== undefined ? q.correct_index : 0);
    const subRes = submitInteraction({
      question_id: qId,
      selected_index: sIdx,
      is_correct: isCorrect,
      skill_ids: q.skill_id ? [q.skill_id] : (q.skill_ids || [])
    });

    const resp = {
      question_id: q.id,
      skill_id: q.skill_id || q.primary_skill_id || null,
      is_correct: isCorrect,
      recent_error_streak: state.error_streak,
      remediation_triggered: state.error_streak >= 2
    };

    if (found.type === 'precheck') {
      resp.feedback = isCorrect
        ? (q.pass_feedback || 'Correct! Prerequisite validated.')
        : 'Incorrect. Review the prerequisite concept or request a hint.';
      return resp;
    }

    if (isCorrect) {
      resp.feedback = 'Correct!';
      resp.solution = q.solution || 'Solution validated.';
    } else {
      resp.feedback = 'Incorrect. Try again or request a hint.';
    }

    return resp;
  }

  function getHint(params = {}, store = null) {
    return requestHint(params);
  }

  function getNextLearningAction(params = {}, store = null) {
    syncController();
    const decision = stageController.getNextDecision();
    const nextQ = getNextQuestion();

    if (decision.decision === 'targeted_remediation' || decision.action === 'remediate') {
      return {
        action: 'remediate',
        decision: decision.decision,
        reason: decision.reason || 'Consecutive error threshold reached. Recommending targeted concept review.',
        recommendation: {
          type: 'formula_card',
          title: 'Formula Review',
          diagnosed_skill_id: decision.diagnosed_skill_id || null
        },
        diagnosed_skill_id: decision.diagnosed_skill_id || null
      };
    }

    return {
      action: decision.decision === 'advance' ? 'advance' : 'continue_practice',
      decision: decision.decision,
      reason: decision.reason || 'Continue active unit practice questions.',
      next_question_id: nextQ ? nextQ.id : null,
      stage: state.current_stage,
      student_stage: getStudentStageLabel(state.current_stage),
      skill_id: nextQ?.primary_skill_id || nextQ?.skill_id || null
    };
  }

  function getMasteryState() {
    syncController();
    return stageController.evaluateSkills();
  }

  function exportRawState() {
    return JSON.parse(JSON.stringify(state));
  }

  function setStage(stageId) {
    if (!stageId) return getLearningState();
    state.current_stage = stageId;
    state.current_unit_id = stageId;
    if (stateStore && typeof stateStore.saveState === 'function') {
      stateStore.saveState(state);
    }
    syncController();
    return getLearningState();
  }

  function resetLearnerState() {
    state = createInitialStudentState(DATA, 'concept_learning', currentUnitId);
    if (stateStore && typeof stateStore.clear === 'function') {
      stateStore.clear();
    }
    syncController();
    return getLearningState();
  }

  return {
    getLearningState,
    getCurrentLearningAction,
    submitInteraction,
    requestHint,
    getNextQuestion,
    getLearningProgress,
    getMasteryState,
    getTopicOutline,
    getUnitContent,
    getPrerequisiteCheck,
    startMasteryExam,
    evaluatePractice,
    getHint,
    getNextLearningAction,
    exportRawState,
    setStage,
    resetLearnerState
  };
}

// ----------------------------------------------------------------------------
// Helpers
// ----------------------------------------------------------------------------

function determineInitialUnitId(topicData) {
  if (Array.isArray(topicData.units) && topicData.units.length > 0) {
    return topicData.units[0].id;
  }
  if (topicData.units && typeof topicData.units === 'object') {
    const keys = Object.keys(topicData.units);
    return keys[0] || 'concept_learning';
  }
  return 'concept_learning';
}

function createInitialStudentState(topicData, initialStage, unitId) {
  return {
    current_stage: normalizeStage(initialStage),
    current_unit: unitId,
    current_question_id: null,
    step_progress: {},
    attempts: [],
    error_streak: 0,
    hint_usage: {},
    completed_questions: {},
    mastered_skills: [],
    completed_units: []
  };
}

export default {
  createLearningEngine
};
