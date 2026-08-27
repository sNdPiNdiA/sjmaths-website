/**
 * stage-controller.js
 * 
 * Generic Adaptive Stage Controller & Student-Facing Learning-Flow Contract
 * for SJMaths.
 * 
 * Decoupled from hardcoded chapter content and UI rendering.
 * Coordinates student progression across learning stages and skills based on
 * real-time multi-dimensional assessment evidence.
 */

// ============================================================================
// 1. Stage Mapping & Contracts
// ============================================================================

/**
 * Student-facing stage labels mapped to internal engine stages.
 */
export const STUDENT_TO_INTERNAL_STAGE = Object.freeze({
  understand: 'concept_learning',
  see: 'worked_examples',
  try: 'guided_practice',
  think: 'faded_guidance',
  build: 'constructed_solution',
  solve: 'independent_solution',
  apply: 'transfer_mastery',
  master: 'mastery_gate',
  retain: 'delayed_retrieval'
});

/**
 * Internal engine stages mapped back to student-facing labels.
 */
export const INTERNAL_TO_STUDENT_STAGE = Object.freeze({
  concept_learning: 'understand',
  worked_examples: 'see',
  guided_practice: 'try',
  faded_guidance: 'think',
  constructed_solution: 'build',
  independent_solution: 'solve',
  transfer_mastery: 'apply',
  mastery_gate: 'master',
  delayed_retrieval: 'retain'
});

/**
 * Ordered sequence of pedagogical stages.
 */
export const STAGE_SEQUENCE = Object.freeze([
  'concept_learning',
  'worked_examples',
  'guided_practice',
  'faded_guidance',
  'constructed_solution',
  'independent_solution',
  'transfer_mastery',
  'mastery_gate',
  'delayed_retrieval'
]);

/**
 * Normalized support level hierarchy (higher numeric value = higher instructional support).
 */
export const SUPPORT_LEVELS = Object.freeze({
  full: 4,        // e.g., worked examples, complete step guidance
  high: 3,        // e.g., guided practice with full scaffolds
  moderate: 2,    // e.g., faded prompts, hints on request
  low: 1,         // e.g., independent practice, minimal assistance
  none: 0         // e.g., mastery gates, exams, unassisted transfer
});

/**
 * Difficulty scale ordering (higher numeric value = higher cognitive demand).
 */
export const DIFFICULTY_LEVELS = Object.freeze({
  introductory: 1,
  easy: 2,
  medium: 3,
  hard: 4,
  olympiad: 5
});

/**
 * Default stage progression thresholds and policy configuration.
 */
export const DEFAULT_STAGE_THRESHOLDS = Object.freeze({
  concept_learning: {
    minimum_questions: 1,
    maximum_questions: 2,
    minimum_accuracy: 1.0,
    required_skill_coverage: 0.5,
    minimum_support_level_evidence: 'high'
  },
  worked_examples: {
    minimum_questions: 1,
    maximum_questions: 3,
    minimum_accuracy: 1.0,
    required_skill_coverage: 0.5,
    minimum_support_level_evidence: 'full'
  },
  guided_practice: {
    minimum_questions: 2,
    maximum_questions: 5,
    minimum_accuracy: 0.75,
    required_skill_coverage: 0.8,
    minimum_support_level_evidence: 'high'
  },
  faded_guidance: {
    minimum_questions: 2,
    maximum_questions: 4,
    minimum_accuracy: 0.8,
    required_skill_coverage: 0.8,
    minimum_support_level_evidence: 'moderate'
  },
  constructed_solution: {
    minimum_questions: 2,
    maximum_questions: 4,
    minimum_accuracy: 0.8,
    required_skill_coverage: 0.8,
    minimum_support_level_evidence: 'moderate'
  },
  independent_solution: {
    minimum_questions: 2,
    maximum_questions: 5,
    minimum_accuracy: 0.8,
    required_skill_coverage: 1.0,
    minimum_support_level_evidence: 'low'
  },
  transfer_mastery: {
    minimum_questions: 2,
    maximum_questions: 4,
    minimum_accuracy: 0.8,
    required_skill_coverage: 1.0,
    minimum_support_level_evidence: 'low'
  },
  mastery_gate: {
    minimum_questions: 3,
    maximum_questions: 10,
    minimum_accuracy: 0.8,
    required_skill_coverage: 1.0,
    minimum_support_level_evidence: 'none'
  },
  delayed_retrieval: {
    minimum_questions: 1,
    maximum_questions: 3,
    minimum_accuracy: 0.8,
    required_skill_coverage: 0.5,
    minimum_support_level_evidence: 'none'
  }
});

// ============================================================================
// 2. Helper Utilities & Dimension Normalization
// ============================================================================

/**
 * Normalizes any external or internal stage name to standard internal representation.
 * 
 * @param {string} stage 
 * @returns {string} Internal stage identifier
 */
export function normalizeStage(stage) {
  if (!stage || typeof stage !== 'string') return 'concept_learning';
  const clean = stage.trim().toLowerCase();
  if (STUDENT_TO_INTERNAL_STAGE[clean]) {
    return STUDENT_TO_INTERNAL_STAGE[clean];
  }
  if (INTERNAL_TO_STUDENT_STAGE[clean]) {
    return clean;
  }
  // Fallback aliases
  if (clean === 'prerequisite_check') return 'concept_learning';
  if (clean === 'transfer_and_pyq') return 'transfer_mastery';
  return clean;
}

/**
 * Converts internal stage name to student-facing label.
 * 
 * @param {string} internalStage 
 * @returns {string} Student-facing stage name
 */
export function getStudentStageLabel(internalStage) {
  const norm = normalizeStage(internalStage);
  return INTERNAL_TO_STUDENT_STAGE[norm] || 'understand';
}

/**
 * Ensures assessment item retains all 4 distinct pedagogical dimensions.
 * 
 * @param {Object} item 
 * @returns {Object} Normalized 4D item metadata
 */
export function normalizeAssessmentItemDimensions(item = {}) {
  const stage = normalizeStage(item.stage || 'guided_practice');
  const task_type = item.task_type || (item.options ? 'multiple_choice' : 'constructed_response');
  const difficulty = item.difficulty ? item.difficulty.toLowerCase() : 'medium';
  
  let support_level = item.support_level;
  if (!support_level) {
    if (stage === 'concept_learning' || stage === 'worked_examples') support_level = 'full';
    else if (stage === 'guided_practice') support_level = 'high';
    else if (stage === 'faded_guidance' || stage === 'constructed_solution') support_level = 'moderate';
    else if (stage === 'independent_solution' || stage === 'transfer_mastery') support_level = 'low';
    else if (stage === 'mastery_gate' || stage === 'delayed_retrieval') support_level = 'none';
    else support_level = 'moderate';
  }

  return {
    stage,
    task_type,
    difficulty,
    support_level
  };
}

/**
 * Extracts and filters all question items for a given unit across all practice and gate pools.
 * 
 * @param {Object} topicData 
 * @param {string} unitId 
 * @returns {Array<Object>} List of unit items
 */
export function getUnitQuestions(topicData, unitId) {
  if (!topicData || !Array.isArray(topicData.units)) return [];
  const unit = topicData.units.find(u => u.id === unitId);
  if (!unit) return [];

  const items = [];
  if (unit.prerequisite_check) {
    items.push({ ...unit.prerequisite_check, default_stage: 'concept_learning' });
  }
  if (unit.practice_stages) {
    if (Array.isArray(unit.practice_stages.guided_and_independent)) {
      items.push(...unit.practice_stages.guided_and_independent);
    }
    if (Array.isArray(unit.practice_stages.transfer_and_pyq)) {
      items.push(...unit.practice_stages.transfer_and_pyq);
    }
  }
  if (unit.unit_mastery_gate && Array.isArray(unit.unit_mastery_gate.questions)) {
    items.push(...unit.unit_mastery_gate.questions);
  }
  return items;
}

// ============================================================================
// 3. Stage Controller Implementation
// ============================================================================

export class StageController {
  /**
   * @param {Object} [options]
   * @param {Object} [options.thresholds] Custom stage thresholds override
   * @param {Object} [options.policy] Custom pedagogical policies
   */
  constructor(options = {}) {
    this.thresholds = { ...DEFAULT_STAGE_THRESHOLDS, ...(options.thresholds || {}) };
    this.policy = {
      remediationErrorStreak: 2,
      stageFailureRepeatsThreshold: 2,
      minDistinctForSkillMastery: 2,
      requireHigherStageForSkillMastery: true,
      ...(options.policy || {})
    };
  }

  /**
   * Main decision point: Evaluates current state and returns next pedagogical decision.
   * 
   * @param {Object} params
   * @param {Object} params.topicData Learning-Topic JSON specification
   * @param {Object} params.studentState Current student state from StateStore
   * @param {string} params.currentUnitId Current active unit ID
   * @param {string} [params.currentStage] Current internal or student-facing stage
   * @returns {Object} Decision object containing action, target stage, reason, and context
   */
  decide({ topicData, studentState, currentUnitId, currentStage }) {
    if (!topicData) {
      throw new Error('StageController requires valid topicData.');
    }
    const state = studentState || {};
    const unitId = currentUnitId || state.current_unit_id || (topicData.units && topicData.units[0] && topicData.units[0].id);
    const unit = (topicData.units || []).find(u => u.id === unitId) || null;
    
    // Resolve current stage
    const internalStage = normalizeStage(currentStage || state.current_stage || 'guided_practice');
    const studentStage = getStudentStageLabel(internalStage);

    // 1. Check for delayed retrieval obligations across completed units
    if (this._isRetrievalDue(state, topicData, unitId)) {
      return {
        action: 'retrieval_due',
        internal_stage: 'delayed_retrieval',
        student_stage: 'retain',
        unit_id: unitId,
        reason: 'Spaced repetition retrieval is due for consolidated concepts.'
      };
    }

    // 2. Check for targeted error / remediation state
    const errorStreak = state.recent_error_streak || 0;
    if (errorStreak >= this.policy.remediationErrorStreak) {
      const remediationDecision = this._handleRemediation(state, unit, internalStage);
      if (remediationDecision) return remediationDecision;
    }

    // 3. Evaluate Skill Mastery independently from stage completion
    const skillEvaluation = this.evaluateUnitSkills(topicData, state, unitId);

    // 4. If all unit skills are mastered and learner is at or past independent practice, check mastery gate
    if (skillEvaluation.allMastered && internalStage === 'transfer_mastery') {
      return {
        action: 'start_mastery',
        internal_stage: 'mastery_gate',
        student_stage: 'master',
        unit_id: unitId,
        reason: 'All unit skills mastered with transfer evidence. Ready for unit mastery gate.',
        skills: skillEvaluation
      };
    }

    // 5. Evaluate current stage progress & adaptive advancement
    const stageEvidence = this.getStageEvidence(topicData, state, unitId, internalStage);
    const stageCriteria = this.thresholds[internalStage] || DEFAULT_STAGE_THRESHOLDS[internalStage] || DEFAULT_STAGE_THRESHOLDS.guided_practice;

    // Check early advancement or standard stage completion
    if (stageEvidence.isComplete) {
      return this._handleStageCompletion(topicData, state, unitId, internalStage, skillEvaluation, stageEvidence);
    }

    // If max questions reached without passing accuracy, diagnose stage failure vs retry
    if (stageEvidence.attemptsCount >= stageCriteria.maximum_questions && stageEvidence.accuracy < stageCriteria.minimum_accuracy) {
      return this._handleStageFailure(topicData, state, unitId, internalStage, stageEvidence);
    }

    // Check support reduction condition within current stage
    if (this._shouldReduceSupport(stageEvidence, internalStage)) {
      return {
        action: 'reduce_support',
        internal_stage: internalStage,
        student_stage: studentStage,
        unit_id: unitId,
        reason: 'Learner demonstrated high confidence on current stage; reducing scaffold/support level without increasing difficulty.',
        target_support: 'lower'
      };
    }

    // Standard in-stage continuation
    return {
      action: stageEvidence.attemptsCount > 0 ? 'repeat_with_new_question' : 'stay',
      internal_stage: internalStage,
      student_stage: studentStage,
      unit_id: unitId,
      reason: `Continuing practice in ${studentStage} (${internalStage}): solved ${stageEvidence.distinctCorrect}/${stageCriteria.minimum_questions} required questions (accuracy: ${(stageEvidence.accuracy * 100).toFixed(0)}%).`,
      stage_evidence: stageEvidence
    };
  }

  /**
   * Evaluates stage-specific evidence for the student in a unit.
   * 
   * @param {Object} topicData 
   * @param {Object} studentState 
   * @param {string} unitId 
   * @param {string} stage 
   * @returns {Object} Stage evidence metrics
   */
  getStageEvidence(topicData, studentState, unitId, stage) {
    const internalStage = normalizeStage(stage);
    const thresholds = this.thresholds[internalStage] || DEFAULT_STAGE_THRESHOLDS[internalStage] || DEFAULT_STAGE_THRESHOLDS.guided_practice;
    const completedQuestions = (studentState && studentState.completed_questions) || {};
    const unitQuestions = getUnitQuestions(topicData, unitId);

    // Filter questions corresponding to this stage
    const stageQuestions = unitQuestions.filter(q => {
      const qStage = normalizeStage(q.stage || q.default_stage);
      return qStage === internalStage;
    });

    const stageQuestionIds = new Set(stageQuestions.map(q => q.id));
    
    let attemptsCount = 0;
    let correctCount = 0;
    let distinctCorrect = 0;
    const solvedDistinctIds = new Set();
    const coveredSkills = new Set();
    const hintUsedOnQuestions = new Set();
    let distinctUnassistedCorrect = 0;

    for (const [qId, rec] of Object.entries(completedQuestions)) {
      if (stageQuestionIds.has(qId)) {
        attemptsCount += (rec.attempts || 1);
        if (rec.solved) {
          correctCount += 1;
          if (!solvedDistinctIds.has(qId)) {
            solvedDistinctIds.add(qId);
            distinctCorrect += 1;
            
            // Skill coverage
            const matchingQ = stageQuestions.find(q => q.id === qId);
            if (matchingQ && matchingQ.skill_id) {
              coveredSkills.add(matchingQ.skill_id);
            }

            // Hint check - hint use does not count as unassisted mastery
            const hintLevel = (studentState.hint_usage && studentState.hint_usage[qId]) || 0;
            if (hintLevel === 0) {
              distinctUnassistedCorrect += 1;
            } else {
              hintUsedOnQuestions.add(qId);
            }
          }
        }
      }
    }

    const accuracy = attemptsCount > 0 ? (correctCount / attemptsCount) : 0;
    const totalStageQuestionsCount = stageQuestions.length;
    const unit = (topicData.units || []).find(u => u.id === unitId);
    const unitSkills = (unit && unit.skills_covered) || [];
    const skillCoverageRatio = unitSkills.length > 0 ? (coveredSkills.size / unitSkills.length) : 1.0;

    // Evaluate completion conditions
    // 1. Min distinct questions satisfied (or all available stage questions solved)
    const minRequired = Math.min(thresholds.minimum_questions, totalStageQuestionsCount || thresholds.minimum_questions);
    const hasSufficientDistinct = distinctCorrect >= minRequired;

    // 2. Min accuracy met
    const hasSufficientAccuracy = accuracy >= thresholds.minimum_accuracy;

    // 3. Required skill coverage met
    const hasRequiredSkillCoverage = skillCoverageRatio >= thresholds.required_skill_coverage;

    // 4. Adaptive early advancement: if student is unassisted, highly accurate, and covered distinct items
    const isComplete = (hasSufficientDistinct && hasSufficientAccuracy && hasRequiredSkillCoverage) ||
                       (distinctUnassistedCorrect >= minRequired && accuracy === 1.0);

    return {
      internal_stage: internalStage,
      student_stage: getStudentStageLabel(internalStage),
      attemptsCount,
      correctCount,
      distinctCorrect,
      distinctUnassistedCorrect,
      solvedDistinctIds: Array.from(solvedDistinctIds),
      accuracy,
      skillCoverageRatio,
      coveredSkills: Array.from(coveredSkills),
      isComplete,
      thresholds
    };
  }

  /**
   * Evaluates skill mastery criteria independently from stage progression.
   * 
   * Criteria:
   * 1. Distinct correct questions >= policy threshold (default 2)
   * 2. Evidence across task types / support levels (at least 1 independent or transfer)
   * 3. No unresolved critical misconceptions
   * 4. Hint usage tracked: questions solved purely with hints don't suffice for unassisted mastery.
   * 
   * @param {Object} topicData 
   * @param {Object} studentState 
   * @param {string} unitId 
   * @returns {Object} Comprehensive skills evaluation
   */
  evaluateUnitSkills(topicData, studentState, unitId) {
    const unit = (topicData.units || []).find(u => u.id === unitId);
    const unitSkills = (unit && unit.skills_covered) || [];
    const skillEvidenceMap = (studentState && studentState.skill_evidence) || {};
    const masteredList = (studentState && studentState.mastered_skills) || [];

    const results = {};
    let allMastered = unitSkills.length > 0;

    for (const skillId of unitSkills) {
      const ev = skillEvidenceMap[skillId] || {
        guided_correct: 0,
        independent_correct: 0,
        transfer_correct: 0,
        total_correct: 0,
        correct_question_ids: []
      };

      const distinctCorrect = (ev.correct_question_ids || []).length;
      const higherStageEvidence = (ev.independent_correct || 0) + (ev.transfer_correct || 0);
      const isAlreadyMastered = masteredList.includes(skillId);

      const hasMinDistinct = distinctCorrect >= this.policy.minDistinctForSkillMastery;
      const hasHigherStage = !this.policy.requireHigherStageForSkillMastery || higherStageEvidence >= 1;

      const isMastered = isAlreadyMastered || (hasMinDistinct && hasHigherStage);

      if (!isMastered) {
        allMastered = false;
      }

      results[skillId] = {
        skill_id: skillId,
        mastered: isMastered,
        distinct_correct: distinctCorrect,
        guided_correct: ev.guided_correct || 0,
        independent_correct: ev.independent_correct || 0,
        transfer_correct: ev.transfer_correct || 0,
        higher_stage_correct: higherStageEvidence,
        requires: {
          min_distinct: this.policy.minDistinctForSkillMastery,
          min_higher_stage: 1
        }
      };
    }

    return {
      unit_id: unitId,
      total_skills: unitSkills.length,
      mastered_skills_count: Object.values(results).filter(r => r.mastered).length,
      allMastered,
      skills: results
    };
  }

  /**
   * Recommends safe difficulty and support level adjustment.
   * Hard rule: Do NOT simultaneously increase difficulty AND reduce support unless learner demonstrates high confidence.
   * 
   * @param {Object} currentDimensions { difficulty, support_level }
   * @param {Object} learnerPerformance { accuracy, consecutiveSuccesses, unassisted }
   * @returns {Object} Adjusted safe dimensions
   */
  safelyAdjustDimensions(currentDimensions, learnerPerformance) {
    const currDiff = currentDimensions.difficulty || 'medium';
    const currSupport = currentDimensions.support_level || 'moderate';
    
    const accuracy = learnerPerformance.accuracy || 0;
    const streak = learnerPerformance.consecutiveSuccesses || 0;
    const isHighConfidence = accuracy >= 0.9 && streak >= 2 && learnerPerformance.unassisted;

    // If struggling (low accuracy or error streak) -> increase support, keep or reduce difficulty
    if (accuracy < 0.6 || learnerPerformance.recentErrors >= 1) {
      return {
        difficulty: currDiff === 'hard' ? 'medium' : (currDiff === 'medium' ? 'easy' : 'easy'),
        support_level: currSupport === 'low' ? 'moderate' : (currSupport === 'moderate' ? 'high' : 'full'),
        applied_rule: 'remediation_support_increase'
      };
    }

    // If high confidence demonstrated -> can increase difficulty OR reduce support
    if (isHighConfidence) {
      // Step 1: Reduce support first while maintaining difficulty
      if (currSupport === 'full' || currSupport === 'high') {
        return {
          difficulty: currDiff,
          support_level: currSupport === 'full' ? 'high' : 'moderate',
          applied_rule: 'safe_support_reduction'
        };
      }
      // Step 2: Once support is low, increase difficulty
      return {
        difficulty: currDiff === 'easy' ? 'medium' : (currDiff === 'medium' ? 'hard' : 'hard'),
        support_level: 'low',
        applied_rule: 'difficulty_progression_after_mastered_support'
      };
    }

    // Default: Maintain steady dimensions
    return {
      difficulty: currDiff,
      support_level: currSupport,
      applied_rule: 'maintain_dimensions'
    };
  }

  // ==========================================================================
  // Internal Pedagogical Routing Helpers
  // ==========================================================================

  _isRetrievalDue(studentState, topicData, currentUnitId) {
    if (!studentState || !Array.isArray(studentState.completed_units)) return false;
    // If learner has completed previous units and retrieval is scheduled
    if (studentState.completed_units.length > 0 && studentState.retrieval_due_units && studentState.retrieval_due_units.length > 0) {
      return true;
    }
    return false;
  }

  _handleRemediation(studentState, unit, internalStage) {
    const errorStreak = studentState.recent_error_streak || 0;
    const lastAttemptedQuestionId = studentState.last_attempted_question_id;

    // Diagnose likely skill from last failed question
    let likelySkillId = null;
    if (unit && unit.practice_stages) {
      const allQ = [
        ...(unit.practice_stages.guided_and_independent || []),
        ...(unit.practice_stages.transfer_and_pyq || [])
      ];
      const qObj = allQ.find(q => q.id === lastAttemptedQuestionId);
      if (qObj) likelySkillId = qObj.skill_id;
    }

    // Single wrong answer does NOT cause stage regression.
    // When error streak threshold is reached (e.g. 2 consecutive errors):
    // Offer targeted micro-practice or contextual hint/retry without wiping topic progress.
    return {
      action: 'remediate',
      internal_stage: internalStage,
      student_stage: getStudentStageLabel(internalStage),
      reason: `Consecutive error threshold reached (${errorStreak} errors). Recommending contextual remediation micro-practice.`,
      diagnosed_skill_id: likelySkillId,
      remediation_type: 'contextual_hint_and_micropractice',
      allow_retry: true
    };
  }

  _handleStageCompletion(topicData, studentState, unitId, internalStage, skillEvaluation, stageEvidence) {
    const currentIdx = STAGE_SEQUENCE.indexOf(internalStage);
    const nextIdx = currentIdx + 1;

    // If unit mastery gate completed
    if (internalStage === 'mastery_gate') {
      return {
        action: 'complete_stage',
        internal_stage: 'mastery_gate',
        student_stage: 'master',
        unit_id: unitId,
        reason: 'Unit mastery gate passed successfully.',
        unit_completed: true
      };
    }

    // If all skills mastered before all stages, learner can start transfer or mastery
    if (skillEvaluation.allMastered && internalStage === 'independent_solution') {
      return {
        action: 'start_transfer',
        internal_stage: 'transfer_mastery',
        student_stage: 'apply',
        unit_id: unitId,
        reason: 'Independent solution mastered for all unit skills. Advancing to transfer mastery & PYQs.'
      };
    }

    // Standard sequence advance
    if (nextIdx < STAGE_SEQUENCE.length) {
      const nextInternalStage = STAGE_SEQUENCE[nextIdx];
      const nextStudentStage = getStudentStageLabel(nextInternalStage);

      // Check if skill completion happens at this boundary
      const isSkillComplete = skillEvaluation.allMastered;

      return {
        action: isSkillComplete ? 'complete_skill' : 'advance',
        internal_stage: nextInternalStage,
        student_stage: nextStudentStage,
        unit_id: unitId,
        reason: `Stage ${getStudentStageLabel(internalStage)} complete (${stageEvidence.distinctCorrect} distinct questions solved). Advancing to ${nextStudentStage}.`,
        previous_stage: internalStage
      };
    }

    return {
      action: 'complete_stage',
      internal_stage: internalStage,
      student_stage: getStudentStageLabel(internalStage),
      unit_id: unitId,
      reason: 'Stage sequence completed.'
    };
  }

  _handleStageFailure(topicData, studentState, unitId, internalStage, stageEvidence) {
    // Only regress support level when the stage itself has failed repeatedly
    const stageFailCount = (studentState.stage_failures && studentState.stage_failures[internalStage]) || 0;

    if (stageFailCount >= this.policy.stageFailureRepeatsThreshold) {
      const currentIdx = STAGE_SEQUENCE.indexOf(internalStage);
      const prevInternalStage = currentIdx > 0 ? STAGE_SEQUENCE[currentIdx - 1] : internalStage;

      return {
        action: 'remediate',
        internal_stage: prevInternalStage,
        student_stage: getStudentStageLabel(prevInternalStage),
        unit_id: unitId,
        reason: `Stage ${getStudentStageLabel(internalStage)} failed repeatedly (${stageEvidence.attemptsCount} attempts, ${(stageEvidence.accuracy * 100).toFixed(0)}% accuracy). Regressing support level to ${getStudentStageLabel(prevInternalStage)}.`,
        regress_support: true
      };
    }

    return {
      action: 'repeat_with_new_question',
      internal_stage: internalStage,
      student_stage: getStudentStageLabel(internalStage),
      unit_id: unitId,
      reason: `Stage requirements not yet met (${(stageEvidence.accuracy * 100).toFixed(0)}% accuracy < ${(stageEvidence.thresholds.minimum_accuracy * 100).toFixed(0)}%). Extending practice within current stage.`
    };
  }

  _shouldReduceSupport(stageEvidence, internalStage) {
    // If student has solved at least 1 distinct question unassisted with 100% accuracy in high/full support stages
    if ((internalStage === 'worked_examples' || internalStage === 'guided_practice') &&
        stageEvidence.distinctUnassistedCorrect >= 1 &&
        stageEvidence.accuracy === 1.0) {
      return true;
    }
    return false;
  }
}

/**
 * Factory function for creating a StageController instance.
 * 
 * @param {Object} [options]
 * @returns {StageController}
 */
export function createStageController(options = {}) {
  return new StageController(options);
}
