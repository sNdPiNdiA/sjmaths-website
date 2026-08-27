/**
 * stage-controller.js
 * 
 * Generic, topic-agnostic Stage Controller for the permanent SJMaths mastery-learning engine.
 * Consumes any valid Learning-Topic JSON (v3.3+).
 * 
 * Contains NO hard-coded question IDs, skill IDs, class constants, fixed question counts,
 * or hard-coded task types. All parameters, thresholds, and policies are derived from topicData.
 */

// ============================================================================
// 1. Stage Mappings & Constants
// ============================================================================

/**
 * Supported internal learning stages in canonical sequence.
 */
export const INTERNAL_STAGES = Object.freeze([
  'concept_learning',
  'worked_examples',
  'understanding_check',
  'guided_practice',
  'faded_guidance',
  'constructed_solution',
  'confidence_bridge',
  'independent_solution',
  'transfer_mastery',
  'mastery_gate',
  'delayed_retrieval'
]);

/**
 * Mapping from student-facing labels to canonical internal stage identifiers.
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
 * Mapping from internal engine stages to student-facing display labels.
 * Internal confidence_bridge maps to 'build' (student does not see a separate stage).
 * Understanding check maps to 'understand'.
 */
export const INTERNAL_TO_STUDENT_STAGE = Object.freeze({
  concept_learning: 'understand',
  worked_examples: 'see',
  understanding_check: 'see',
  guided_practice: 'try',
  faded_guidance: 'think',
  constructed_solution: 'build',
  confidence_bridge: 'build',
  independence_bridge: 'build',
  independent_solution: 'solve',
  transfer_mastery: 'apply',
  mastery_gate: 'master',
  delayed_retrieval: 'retain'
});

/**
 * Human-readable display titles for student-facing stages.
 */
export const STUDENT_STAGE_DISPLAY_NAMES = Object.freeze({
  understand: 'Understand',
  see: 'See',
  try: 'Try',
  think: 'Think',
  build: 'Build',
  solve: 'Solve',
  apply: 'Apply',
  master: 'Master',
  retain: 'Retain'
});

/**
 * Supported controller decision types.
 */
export const DECISION_TYPES = Object.freeze([
  'advance',
  'stay',
  'retry',
  'extend_practice',
  'targeted_remediation',
  'reduce_support',
  'confidence_check',
  'complete_skill',
  'complete_unit',
  'start_transfer',
  'start_mastery',
  'retrieval_due'
]);

/**
 * Helper to normalize any stage input string (internal or student-facing) to internal stage name.
 * 
 * @param {string} stage
 * @returns {string} canonical internal stage name
 */
export function normalizeStage(stage) {
  if (!stage || typeof stage !== 'string') return 'concept_learning';
  const lower = stage.toLowerCase().trim();
  if (STUDENT_TO_INTERNAL_STAGE[lower]) {
    return STUDENT_TO_INTERNAL_STAGE[lower];
  }
  if (lower === 'independence_bridge') {
    return 'confidence_bridge';
  }
  if (INTERNAL_STAGES.includes(lower)) {
    return lower;
  }
  return lower;
}

/**
 * Helper to get the student-facing stage label for any internal or student stage.
 * 
 * @param {string} stage
 * @returns {string} student-facing stage label (lowercase, e.g. 'try', 'think')
 */
export function getStudentStageLabel(stage) {
  if (!stage) return 'understand';
  const internal = normalizeStage(stage);
  return INTERNAL_TO_STUDENT_STAGE[internal] || 'understand';
}

/**
 * Helper to get the student-facing formatted title (e.g. 'Try', 'Think').
 * 
 * @param {string} stage
 * @returns {string} capitalized student-facing stage title
 */
export function getStudentFacingTitle(stage) {
  const label = getStudentStageLabel(stage);
  return STUDENT_STAGE_DISPLAY_NAMES[label] || label.charAt(0).toUpperCase() + label.slice(1);
}

// ============================================================================
// 2. Stage Controller Class
// ============================================================================

export class StageController {
  /**
   * @param {Object} params
   * @param {Object} params.topicData - Parsed Learning-Topic JSON (v3.3+)
   * @param {Object} [params.studentState] - Student state object
   * @param {string} [params.unitId] - Optional current unit identifier
   * @param {string} [params.currentStage] - Current internal or student-facing stage
   */
  constructor({ topicData, studentState = {}, unitId = null, currentStage = 'concept_learning' } = {}) {
    if (!topicData || typeof topicData !== 'object') {
      throw new Error('StageController requires a valid topicData object.');
    }
    this.topicData = topicData;
    if (this.topicData.units && typeof this.topicData.units === 'object' && !Array.isArray(this.topicData.units)) {
      for (const [uKey, uDef] of Object.entries(this.topicData.units)) {
        ['questions', 'question_pool', 'embedded_skill_practice', 'variants'].forEach(field => {
          if (Array.isArray(uDef[field])) {
            uDef[field].forEach((q, idx) => {
              if (!q.id) q.id = `${uKey}_${field}_${idx + 1}`;
            });
          }
        });
      }
    }
    this.studentState = studentState || {};
    this.unitId = unitId;
    this.currentStage = normalizeStage(currentStage);
  }

  // --------------------------------------------------------------------------
  // Core Public API
  // --------------------------------------------------------------------------

  /**
   * Returns the current internal stage.
   * @returns {string}
   */
  getCurrentStage() {
    return this.currentStage;
  }

  /**
   * Returns the student-facing stage label (e.g. 'understand', 'try', 'think').
   * @returns {string}
   */
  getStudentFacingStage() {
    return getStudentStageLabel(this.currentStage);
  }

  /**
   * Returns the student-facing capitalized title (e.g. 'Understand', 'Try', 'Think').
   * @returns {string}
   */
  getStudentFacingTitle() {
    return getStudentFacingTitle(this.currentStage);
  }

  /**
   * Evaluates the student's progress and evidence in the current stage.
   * 
   * @param {string} [stage] - Optional stage to evaluate (defaults to currentStage)
   * @returns {Object} Stage evaluation metrics
   */
  evaluateStage(stage = this.currentStage) {
    const internalStage = normalizeStage(stage);
    return this.getStageEvidence(this.topicData, this.studentState, this.unitId, internalStage);
  }

  /**
   * Evaluates all skills in the topic/unit against their mastery criteria.
   * 
   * @param {string} [unitId]
   * @returns {Object} Skills evaluation summary
   */
  evaluateSkills(unitId = this.unitId) {
    return this.evaluateUnitSkills(this.topicData, this.studentState, unitId);
  }

  /**
   * Determines if the learner has met all evidence requirements to advance from the current stage.
   * 
   * @param {string} [stage]
   * @returns {boolean}
   */
  canAdvance(stage = this.currentStage) {
    const internalStage = normalizeStage(stage);
    const stageEv = this.evaluateStage(internalStage);
    const stageConfig = this._getStageConfig(internalStage);

    // Passive learning stages (concept_learning, worked_examples) advance if minimum questions/views reached
    if (internalStage === 'concept_learning' || internalStage === 'worked_examples') {
      const minQ = stageConfig.minQuestions || 1;
      return stageEv.distinctAttempts >= minQ || stageEv.distinctCorrect >= minQ;
    }

    // Minimum question count check
    if (stageEv.distinctCorrect < stageEv.thresholds.minimum_questions) {
      return false;
    }

    // Accuracy threshold check
    if (stageEv.accuracy < stageEv.thresholds.minimum_accuracy) {
      return false;
    }

    // Hint dependency threshold check
    const maxHintDep = stageConfig.advancementRequirements?.max_hint_dependency ??
      this.topicData.sequence?.advancement_policy?.maximum_hint_dependency_for_advancement ?? 0.4;
    if (stageEv.hintDependencyRate > maxHintDep && stageEv.distinctUnassistedCorrect === 0) {
      return false;
    }

    // Core skill evidence check for this stage: evaluate skills touched in stage attempts
    if (internalStage !== 'transfer_mastery') {
      const coreMin = stageConfig.minEvidencePerCoreSkill || 1;
      const stageSkills = this._getSkillsForStage(internalStage, stageEv);
      for (const skillId of stageSkills) {
        const count = stageEv.coreSkillsEvidenced[skillId] || 0;
        if (count < coreMin) {
          return false;
        }
      }
    }

    // Stage-specific checks (e.g. confidence bridge requires at least 1 low-hint / unassisted success)
    if (internalStage === 'confidence_bridge' || internalStage === 'independence_bridge') {
      if (stageEv.distinctLowHintCorrect < 1) {
        return false;
      }
    }

    return true;
  }

  /**
   * Computes and returns the next normalized pedagogical decision object.
   * 
   * @param {Object} [evalContext] - Optional context overrides { questionInput, isFormatError, failedStepSkillId, lastAttemptCorrect, etc. }
   * @returns {Object} Normalized decision object
   */
  getNextDecision(evalContext = {}) {
    const internalStage = this.currentStage;
    const stageEv = this.evaluateStage(internalStage);
    const skillEval = this.evaluateSkills(this.unitId);
    const stageConfig = this._getStageConfig(internalStage);

    // 1. Check for Input Format / Malformed Errors first (Rule 9)
    if (evalContext.isFormatError || evalContext.reason_type === 'input_error') {
      return {
        decision: 'retry',
        from_stage: internalStage,
        to_stage: internalStage,
        reason: 'Input format invalid or incomplete. Retry without penalizing conceptual progress.',
        reason_type: 'input_error',
        student_stage: getStudentStageLabel(internalStage),
        support_level: stageConfig.supportLevel
      };
    }

    // 2. Check Delayed Retrieval Schedule (Rule 15)
    if (internalStage === 'delayed_retrieval' || evalContext.isRetrievalDue) {
      return {
        decision: 'retrieval_due',
        from_stage: internalStage,
        to_stage: 'delayed_retrieval',
        reason: 'Scheduled spaced retention check due.',
        message: "Let's wake this skill up.",
        student_stage: 'retain',
        support_level: 0
      };
    }

    // 3. Check Error Streak / Misconception Remediation (Rule 8)
    const errorStreak = this.studentState.error_streak || 0;
    if (errorStreak >= 1 && evalContext.lastAttemptCorrect === false) {
      return this._handleErrorDecision(internalStage, errorStreak, evalContext, stageConfig);
    }

    // 4. Check if Current Stage can Advance (Rule 12 & Rule 2-7)
    if (this.canAdvance(internalStage)) {
      return this._handleAdvancementDecision(internalStage, stageEv, skillEval, stageConfig);
    }

    // 5. Check if Safe Support Reduction is possible within stage
    if (this._shouldReduceSupport(stageEv, internalStage, stageConfig)) {
      const newSupport = Math.max(0, stageConfig.supportLevel - 1);
      return {
        decision: 'reduce_support',
        from_stage: internalStage,
        to_stage: internalStage,
        reason: 'Learner demonstrated strong unassisted competency. Reducing instructional scaffolding.',
        next_action: 'continue_with_reduced_support',
        student_stage: getStudentStageLabel(internalStage),
        support_level: newSupport
      };
    }

    // 6. Otherwise: Stay in current stage and extend practice
    const neededSkills = Object.entries(stageEv.coreSkillsEvidenced)
      .filter(([_, count]) => count < (stageConfig.minEvidencePerCoreSkill || 1))
      .map(([id]) => id);

    return {
      decision: stageEv.distinctAttempts >= stageConfig.minQuestions ? 'extend_practice' : 'stay',
      from_stage: internalStage,
      to_stage: internalStage,
      reason: neededSkills.length > 0
        ? `Stage requirements in progress. Awaiting further evidence for core skill(s): ${neededSkills.join(', ')}.`
        : `Practicing in current stage (${stageEv.distinctCorrect}/${stageEv.thresholds.minimum_questions} required questions complete).`,
      next_action: 'present_next_question',
      student_stage: getStudentStageLabel(internalStage),
      support_level: stageConfig.supportLevel,
      recommended_task_types: this._getRecommendedTaskTypes(internalStage)
    };
  }

  /**
   * Compatibility / alias method for decide() API.
   */
  decide(context = {}) {
    if (context.topicData) this.topicData = context.topicData;
    if (context.studentState) this.studentState = context.studentState;
    if (context.currentUnitId) this.unitId = context.currentUnitId;
    if (context.currentStage) this.currentStage = normalizeStage(context.currentStage);

    const normDecision = this.getNextDecision(context);

    // Map to legacy fields if needed by existing test-runner or consumers
    return {
      action: normDecision.decision === 'extend_practice' ? 'repeat_with_new_question' : normDecision.decision,
      internal_stage: normDecision.to_stage,
      student_stage: normDecision.student_stage,
      decision: normDecision.decision,
      from_stage: normDecision.from_stage,
      to_stage: normDecision.to_stage,
      reason: normDecision.reason,
      support_level: normDecision.support_level,
      allow_retry: normDecision.allow_retry || false,
      diagnosed_skill_id: normDecision.diagnosed_skill_id || null,
      ...normDecision
    };
  }

  /**
   * Returns a complete summary of evidence collected across skills and stages.
   * @returns {Object}
   */
  getEvidenceSummary() {
    const stageEv = this.evaluateStage(this.currentStage);
    const skillEval = this.evaluateSkills(this.unitId);
    return {
      currentStage: this.currentStage,
      studentFacingStage: this.getStudentFacingStage(),
      stageEvidence: stageEv,
      skillsSummary: skillEval,
      canAdvance: this.canAdvance(this.currentStage)
    };
  }

  /**
   * Returns a diagnostic remediation action when learner encounters difficulties.
   * 
   * @param {Object} [errorDetails]
   * @returns {Object} Remediation proposal
   */
  getRemediationAction(errorDetails = {}) {
    const failedSkillId = errorDetails.failedStepSkillId ||
      errorDetails.skillId ||
      this._diagnoseFailedSkill(this.currentStage, errorDetails.questionId);

    const errorStreak = (this.studentState.error_streak || 1);

    if (errorStreak >= 3) {
      return {
        decision: 'targeted_remediation',
        remediation_type: 'micro_practice',
        target_skill_id: failedSkillId,
        return_stage: this.currentStage,
        message: this.topicData.student_experience?.student_messages?.third_related_error ||
          "Let's practise this one skill briefly, then return to your original problem."
      };
    }

    if (errorStreak === 2) {
      return {
        decision: 'targeted_remediation',
        remediation_type: 'concept_review_and_hint',
        target_skill_id: failedSkillId,
        return_stage: this.currentStage,
        message: this.topicData.student_experience?.student_messages?.second_related_error ||
          "Let's pause and review the idea that is causing difficulty."
      };
    }

    return {
      decision: 'retry',
      remediation_type: 'contextual_retry',
      target_skill_id: failedSkillId,
      return_stage: this.currentStage,
      message: this.topicData.student_experience?.student_messages?.first_wrong ||
        "Not this time. Look at the clue and try again."
    };
  }

  /**
   * Returns progress state for UI reporting.
   * @returns {Object}
   */
  getProgressState() {
    const skillEval = this.evaluateSkills(this.unitId);
    const orderedSequence = this.topicData.sequence?.ordered_units || INTERNAL_STAGES;
    const currentIdx = orderedSequence.indexOf(this.currentStage);

    return {
      topic_id: this.topicData.topic?.id || 'unknown_topic',
      current_stage: this.currentStage,
      student_facing_stage: this.getStudentFacingStage(),
      student_facing_title: this.getStudentFacingTitle(),
      skills_mastered_count: skillEval.masteredSkillsCount,
      total_skills_count: skillEval.totalSkillsCount,
      all_core_mastered: skillEval.allCoreMastered,
      is_topic_mastered: skillEval.allCoreMastered && (this.studentState.mastery_gate_passed === true),
      stage_index: currentIdx >= 0 ? currentIdx : 0,
      total_stages: orderedSequence.length
    };
  }

  /**
   * Adjusts difficulty and support level safely according to Rule 1 & Rule 18.
   * Support decrease does NOT automatically force a difficulty jump.
   * 
   * @param {Object} currentDims { difficulty, support_level }
   * @param {Object} performanceMetrics { accuracy, consecutiveSuccesses, unassisted }
   * @returns {Object} adjusted dimensions
   */
  safelyAdjustDimensions(currentDims = {}, performanceMetrics = {}) {
    const difficultyOrder = ['introductory', 'easy', 'medium', 'hard', 'olympiad'];
    const supportOrder = [4, 3, 2, 1, 0]; // 4=full, 0=none

    let diff = currentDims.difficulty || 'medium';
    let supp = currentDims.support_level;

    // Convert string support to number if needed
    if (typeof supp === 'string') {
      const mapping = { full: 4, high: 3, moderate: 2, low: 1, none: 0 };
      supp = mapping[supp] !== undefined ? mapping[supp] : 3;
    } else if (supp === undefined) {
      supp = 3;
    }

    const accuracy = performanceMetrics.accuracy ?? 1.0;
    const consecutive = performanceMetrics.consecutiveSuccesses ?? 0;
    const unassisted = performanceMetrics.unassisted ?? false;

    // Rule: Safe support reduction first without touching difficulty
    if (accuracy >= 0.8 && consecutive >= 2 && supp > 0) {
      supp = supp - 1;
      const suppNames = ['none', 'low', 'moderate', 'high', 'full'];
      return {
        difficulty: diff,
        support_level: typeof currentDims.support_level === 'string' ? suppNames[supp] : supp,
        support_numeric: supp,
        applied_rule: 'safe_support_reduction'
      };
    }

    // Rule: Increase difficulty only when already low support and sustained high confidence
    if (accuracy === 1.0 && consecutive >= 3 && unassisted && supp <= 1) {
      const curIdx = difficultyOrder.indexOf(diff);
      if (curIdx >= 0 && curIdx < difficultyOrder.length - 1) {
        diff = difficultyOrder[curIdx + 1];
      }
      return {
        difficulty: diff,
        support_level: currentDims.support_level,
        applied_rule: 'difficulty_progression'
      };
    }

    return {
      difficulty: diff,
      support_level: currentDims.support_level,
      applied_rule: 'hold'
    };
  }

  // --------------------------------------------------------------------------
  // Internal Helpers & Decision Logic
  // --------------------------------------------------------------------------

  _getStageConfig(internalStage) {
    const unitDef = (this.topicData.units && this.topicData.units[internalStage]) || {};
    const seqAdvPolicy = this.topicData.sequence?.advancement_policy || {};
    const minDistinctMap = seqAdvPolicy.minimum_distinct_questions_by_stage || {};
    const stageBounds = this.topicData.adaptive_practice_policy?.default_stage_question_bounds?.[internalStage] || {};

    const contractDef = (this.topicData.stage_contract && this.topicData.stage_contract[internalStage]) || {};

    const supportLevel = unitDef.support_level !== undefined
      ? unitDef.support_level
      : (contractDef.support_level !== undefined ? contractDef.support_level : 2);

    const isPassiveStage = internalStage === 'concept_learning' || internalStage === 'worked_examples';
    const minQuestions = unitDef.advancement_requirements?.minimum_questions ??
      minDistinctMap[internalStage] ??
      stageBounds.minimum ??
      (isPassiveStage ? 1 : 2);

    const maxQuestions = unitDef.adaptive_question_bounds?.maximum ??
      stageBounds.maximum ??
      5;

    const minAccuracy = unitDef.advancement_requirements?.accuracy ??
      unitDef.mastery?.accuracy ??
      seqAdvPolicy.default_accuracy_threshold ??
      0.8;

    const minEvidencePerCoreSkill = unitDef.advancement_requirements?.minimum_evidence_per_core_skill ??
      this.topicData.adaptive_practice_policy?.core_skill_evidence?.core_skill_minimum_by_stage?.[internalStage] ??
      1;

    return {
      unitDef,
      contractDef,
      supportLevel,
      minQuestions,
      maxQuestions,
      minAccuracy,
      minEvidencePerCoreSkill,
      advancementRequirements: unitDef.advancement_requirements || {}
    };
  }

  _handleErrorDecision(internalStage, errorStreak, evalContext, stageConfig) {
    const diagnosedSkill = evalContext.failedStepSkillId ||
      evalContext.skillId ||
      this._diagnoseFailedSkill(internalStage, evalContext.questionId);

    // Single error: contextual retry (Rule 8)
    if (errorStreak === 1) {
      return {
        decision: 'retry',
        from_stage: internalStage,
        to_stage: internalStage,
        reason: 'Single error encountered. Offer contextual retry with feedback.',
        next_action: 'contextual_retry',
        student_stage: getStudentStageLabel(internalStage),
        support_level: stageConfig.supportLevel,
        diagnosed_skill_id: diagnosedSkill,
        allow_retry: true
      };
    }

    // Two related errors: targeted diagnosis & review recommendation (Rule 8)
    if (errorStreak === 2) {
      return {
        decision: 'targeted_remediation',
        action: 'remediate', // compatibility alias
        from_stage: internalStage,
        to_stage: internalStage,
        reason: `Two consecutive errors on skill "${diagnosedSkill}". Offering targeted review and hint.`,
        next_action: 'offer_targeted_review',
        student_stage: getStudentStageLabel(internalStage),
        support_level: stageConfig.supportLevel,
        diagnosed_skill_id: diagnosedSkill,
        remediation_type: 'contextual_hint_and_micropractice',
        allow_retry: true
      };
    }

    // Three or more errors: targeted micro-practice (Rule 8)
    return {
      decision: 'targeted_remediation',
      action: 'remediate',
      from_stage: internalStage,
      to_stage: internalStage,
      reason: `Repeated difficulty with skill "${diagnosedSkill}". Launching targeted micro-practice.`,
      next_action: 'targeted_micro_practice',
      student_stage: getStudentStageLabel(internalStage),
      support_level: stageConfig.supportLevel,
      diagnosed_skill_id: diagnosedSkill,
      remediation_type: 'targeted_micro_practice',
      allow_retry: true
    };
  }

  _handleAdvancementDecision(internalStage, stageEv, skillEval, stageConfig) {
    const sequence = this.topicData.sequence?.ordered_units || INTERNAL_STAGES;
    const currentIdx = sequence.indexOf(internalStage);

    // Worked examples advance directly to guided_practice (Try)
    if (internalStage === 'worked_examples' || internalStage === 'understanding_check') {
      return {
        decision: 'advance',
        from_stage: internalStage,
        to_stage: 'guided_practice',
        reason: 'Worked examples completed. Advancing to guided practice (Try).',
        next_action: 'present_guided_question',
        student_stage: 'try',
        support_level: 3
      };
    }

    // Hidden Confidence Bridge Transition (Rule 5)
    if (internalStage === 'constructed_solution') {
      // Check if topicData defines confidence_bridge or independence_bridge
      const hasBridge = sequence.includes('confidence_bridge') ||
        sequence.includes('independence_bridge') ||
        Boolean(this.topicData.units?.confidence_bridge || this.topicData.units?.independence_bridge);

      if (hasBridge) {
        const bridgeStage = sequence.includes('confidence_bridge') ? 'confidence_bridge' : 'independence_bridge';
        return {
          decision: 'advance',
          from_stage: 'constructed_solution',
          to_stage: bridgeStage,
          reason: 'Constructed solution complete. Transitioning to internal confidence bridge before independent solving.',
          next_action: 'present_bridge_question',
          student_stage: 'build', // Rule 5: Keep student-facing label as Build!
          support_level: 1,
          is_internal_transition: true
        };
      }
    }

    if (internalStage === 'confidence_bridge' || internalStage === 'independence_bridge') {
      return {
        decision: 'advance',
        from_stage: internalStage,
        to_stage: 'independent_solution',
        reason: 'Confidence bridge passed with unassisted/low-hint success. Advancing to independent solving.',
        next_action: 'present_independent_question',
        student_stage: 'solve',
        support_level: 0
      };
    }

    // If unit or topic mastery gate completed (Rule 14)
    if (internalStage === 'mastery_gate') {
      return {
        decision: 'complete_unit',
        from_stage: 'mastery_gate',
        to_stage: 'delayed_retrieval',
        reason: 'Mastery gate completed successfully.',
        next_action: 'schedule_retrieval',
        student_stage: 'retain',
        support_level: 0,
        unit_completed: true
      };
    }

    // If in independent solution and transfer mastery is next
    if (internalStage === 'independent_solution') {
      return {
        decision: 'start_transfer',
        from_stage: 'independent_solution',
        to_stage: 'transfer_mastery',
        reason: 'Independent solution verified. Advancing to multi-representation transfer mastery.',
        next_action: 'present_transfer_task',
        student_stage: 'apply',
        support_level: 0
      };
    }

    // If in transfer mastery and ready for mastery gate
    if (internalStage === 'transfer_mastery') {
      return {
        decision: 'start_mastery',
        from_stage: 'transfer_mastery',
        to_stage: 'mastery_gate',
        reason: 'Transfer tasks successfully demonstrated. Advancing to topic mastery gate.',
        next_action: 'start_mastery_gate',
        student_stage: 'master',
        support_level: 0
      };
    }

    // General sequential advance
    if (currentIdx >= 0 && currentIdx < sequence.length - 1) {
      const nextInternal = sequence[currentIdx + 1];
      const nextStudent = getStudentStageLabel(nextInternal);
      const nextConfig = this._getStageConfig(nextInternal);

      const isSkillComplete = skillEval.allMastered;

      return {
        decision: isSkillComplete ? 'complete_skill' : 'advance',
        from_stage: internalStage,
        to_stage: nextInternal,
        reason: `Stage ${getStudentStageLabel(internalStage)} requirements met (${stageEv.distinctCorrect} distinct questions correct). Advancing to ${nextStudent}.`,
        next_action: `start_${nextInternal}`,
        student_stage: nextStudent,
        support_level: nextConfig.supportLevel,
        previous_stage: internalStage
      };
    }

    return {
      decision: 'complete_skill',
      from_stage: internalStage,
      to_stage: internalStage,
      reason: 'Stage progression completed.',
      next_action: 'finish_topic',
      student_stage: getStudentStageLabel(internalStage),
      support_level: stageConfig.supportLevel
    };
  }

  _shouldReduceSupport(stageEv, internalStage, stageConfig) {
    if (stageConfig.supportLevel <= 1) return false;

    // If learner solved with 100% accuracy and has at least 1 distinct unassisted/low-hint success
    if (stageEv.accuracy === 1.0 && stageEv.distinctLowHintCorrect >= 1 && stageEv.distinctAttempts >= 2) {
      return true;
    }
    return false;
  }

  _getRecommendedTaskTypes(internalStage) {
    const unitDef = (this.topicData.units && this.topicData.units[internalStage]) || {};
    const taskTypes = new Set();

    if (Array.isArray(unitDef.questions)) {
      unitDef.questions.forEach(q => {
        if (q.task_type) taskTypes.add(q.task_type);
      });
    }

    if (Array.isArray(unitDef.embedded_skill_practice)) {
      unitDef.embedded_skill_practice.forEach(q => {
        if (q.task_type) taskTypes.add(q.task_type);
      });
    }

    // Default fallback to topic-defined task types
    if (taskTypes.size === 0 && Array.isArray(this.topicData.question_model?.task_types)) {
      this.topicData.question_model.task_types.slice(0, 3).forEach(t => taskTypes.add(t));
    }

    return Array.from(taskTypes);
  }

  _diagnoseFailedSkill(internalStage, questionId) {
    // 1. Look up question object in topicData
    const qObj = this._findQuestionInTopic(questionId);
    if (qObj) {
      if (qObj.primary_skill_id) return qObj.primary_skill_id;
      if (qObj.skill) return qObj.skill;
      if (Array.isArray(qObj.skill_ids) && qObj.skill_ids.length > 0) return qObj.skill_ids[0];
    }

    // 2. Look up skills associated with this stage
    const skills = this.topicData.skills || {};
    for (const [sId, sDef] of Object.entries(skills)) {
      if (sDef.first_practised_in === internalStage || sDef.introduced_in === internalStage) {
        return sId;
      }
    }

    // 3. Fallback to first core skill in topicData
    const firstCore = Object.keys(skills).find(k => skills[k].importance === 'core');
    return firstCore || 'core_concept_understanding';
  }

  _findQuestionInTopic(questionId) {
    if (!questionId || !this.topicData.units) return null;
    for (const unit of Object.values(this.topicData.units)) {
      if (Array.isArray(unit.questions)) {
        const found = unit.questions.find(q => q.id === questionId);
        if (found) return found;
      }
      if (Array.isArray(unit.question_pool)) {
        const found = unit.question_pool.find(q => q.id === questionId);
        if (found) return found;
      }
      if (Array.isArray(unit.embedded_skill_practice)) {
        const found = unit.embedded_skill_practice.find(q => q.id === questionId);
        if (found) return found;
      }
    }
    return null;
  }

  _getSkillsForStage(internalStage, stageEv = null) {
    const stageSkills = new Set();
    const skills = this.topicData.skills || {};

    // If stageEv has attempts, only require skills that have been touched in the stage attempts
    if (stageEv && stageEv.coreSkillsEvidenced) {
      for (const [sId, count] of Object.entries(stageEv.coreSkillsEvidenced)) {
        if (count > 0 && skills[sId]?.importance === 'core') {
          stageSkills.add(sId);
        }
      }
      if (stageSkills.size > 0) {
        return Array.from(stageSkills);
      }
    }

    const unitDef = (this.topicData.units && this.topicData.units[internalStage]) || {};

    if (Array.isArray(unitDef.questions)) {
      unitDef.questions.forEach(q => {
        if (q.primary_skill_id && skills[q.primary_skill_id]?.importance === 'core') {
          stageSkills.add(q.primary_skill_id);
        }
      });
    }

    return Array.from(stageSkills);
  }

  // --------------------------------------------------------------------------
  // Evidence & Skill Mastery Calculation Methods (Rule 10 & 11)
  // --------------------------------------------------------------------------

  /**
   * Gathers stage-level evidence from studentState.
   */
  getStageEvidence(topicData, studentState = {}, unitId = null, internalStage = 'guided_practice') {
    const normStage = normalizeStage(internalStage);
    const stageConfig = this._getStageConfig(normStage);

    const attempts = studentState.attempts || [];
    const stageAttempts = attempts.filter(a => {
      const aStage = normalizeStage(a.stage || a.internal_stage || a.student_stage);
      return aStage === normStage;
    });

    const distinctQuestionIds = new Set();
    const distinctCorrectQuestionIds = new Set();
    const distinctUnassistedQuestionIds = new Set();
    const distinctLowHintQuestionIds = new Set();

    let totalCorrect = 0;
    let totalHintedSuccesses = 0;

    const coreSkillsEvidenced = {};
    const coreSkills = Object.keys(topicData.skills || {}).filter(
      k => topicData.skills[k].importance === 'core'
    );
    coreSkills.forEach(k => { coreSkillsEvidenced[k] = 0; });

    stageAttempts.forEach(attempt => {
      const qId = attempt.question_id || attempt.id;
      if (!qId) return;

      distinctQuestionIds.add(qId);
      const isCorrect = attempt.correct === true || attempt.is_correct === true;
      const hintCount = attempt.hints_used || attempt.hint_level || (studentState.hint_usage && studentState.hint_usage[qId]) || 0;

      if (isCorrect) {
        totalCorrect += 1;
        distinctCorrectQuestionIds.add(qId);

        if (hintCount === 0) {
          distinctUnassistedQuestionIds.add(qId);
          distinctLowHintQuestionIds.add(qId);
        } else if (hintCount === 1) {
          distinctLowHintQuestionIds.add(qId);
          totalHintedSuccesses += 1;
        } else {
          totalHintedSuccesses += 1;
        }

        // Skill evidence contribution (Rule 10: Deduplicate skill_ids before calculating evidence)
        const mappedSkills = this._getAttemptSkillIds(attempt, qId);
        const uniqueSkills = [...new Set(mappedSkills)];

        uniqueSkills.forEach(sId => {
          if (coreSkillsEvidenced[sId] !== undefined) {
            coreSkillsEvidenced[sId] += 1;
          }
        });
      }
    });

    const attemptsCount = stageAttempts.length;
    const distinctAttempts = distinctQuestionIds.size;
    const distinctCorrect = distinctCorrectQuestionIds.size;
    const distinctUnassistedCorrect = distinctUnassistedQuestionIds.size;
    const distinctLowHintCorrect = distinctLowHintQuestionIds.size;

    const accuracy = attemptsCount > 0 ? distinctCorrect / distinctAttempts : 0;
    const hintDependencyRate = distinctCorrect > 0 ? (totalHintedSuccesses / distinctCorrect) : 0;

    return {
      stage: normStage,
      attemptsCount,
      distinctAttempts,
      distinctCorrect,
      distinctUnassistedCorrect,
      distinctLowHintCorrect,
      accuracy,
      hintDependencyRate,
      coreSkillsEvidenced,
      thresholds: {
        minimum_questions: stageConfig.minQuestions,
        maximum_questions: stageConfig.maxQuestions,
        minimum_accuracy: stageConfig.minAccuracy
      }
    };
  }

  _getAttemptSkillIds(attempt, qId) {
    let rawSkills = [];
    if (attempt.skill_ids && Array.isArray(attempt.skill_ids)) {
      rawSkills.push(...attempt.skill_ids);
    }
    if (attempt.skill_id) rawSkills.push(attempt.skill_id);
    if (attempt.primary_skill_id) rawSkills.push(attempt.primary_skill_id);
    if (attempt.skill) rawSkills.push(attempt.skill);

    // If attempt has no explicit skills, look up question in topicData
    if (rawSkills.length === 0) {
      const qObj = this._findQuestionInTopic(qId);
      if (qObj) {
        if (Array.isArray(qObj.skill_ids)) rawSkills.push(...qObj.skill_ids);
        if (qObj.primary_skill_id) rawSkills.push(qObj.primary_skill_id);
        if (qObj.skill) rawSkills.push(qObj.skill);
      }
    }

    return rawSkills;
  }

  /**
   * Evaluates all skills for unit or topic against topic-defined mastery policies.
   */
  evaluateUnitSkills(topicData, studentState = {}, unitId = null) {
    const topicSkills = topicData.skills || {};
    const skillResults = {};
    let allMastered = true;
    let allCoreMastered = true;
    let masteredCount = 0;
    let totalSkillsCount = Object.keys(topicSkills).length;

    for (const [skillId, skillDef] of Object.entries(topicSkills)) {
      const masteryReq = skillDef.mastery_evidence || {};
      const minDistinct = masteryReq.minimum_distinct_correct ?? 2;
      const minLowSupport = masteryReq.minimum_low_support_correct ?? 1;
      const lowSupportLevels = masteryReq.low_support_levels ?? [0, 1];
      const precheckCounts = masteryReq.precheck_counts_as_mastery ?? false;

      // Extract student attempts that evidence this skill
      const attempts = studentState.attempts || [];
      const skillAttempts = attempts.filter(a => {
        if (!precheckCounts) {
          const st = normalizeStage(a.stage || a.internal_stage);
          if (st === 'prerequisite_check') return false;
        }

        const qId = a.question_id || a.id;
        const mappedSkills = this._getAttemptSkillIds(a, qId);
        return mappedSkills.includes(skillId);
      });

      const distinctCorrectQuestions = new Set();
      let lowSupportCount = 0;

      skillAttempts.forEach(a => {
        const isCorrect = a.correct === true || a.is_correct === true;
        const qId = a.question_id || a.id;
        if (isCorrect && qId) {
          distinctCorrectQuestions.add(qId);

          // Check support level of attempt
          const qObj = this._findQuestionInTopic(qId);
          const suppLevel = a.support_level !== undefined
            ? a.support_level
            : (qObj?.support_level !== undefined ? qObj.support_level : 2);

          const hintCount = a.hints_used || (studentState.hint_usage && studentState.hint_usage[qId]) || 0;

          // Low support qualifying response (Rule 6: hints reduce weight, but hint <= 1 can provide low-support evidence)
          if (lowSupportLevels.includes(suppLevel) && hintCount <= 1) {
            lowSupportCount += 1;
          }
        }
      });

      const distinctCorrectCount = distinctCorrectQuestions.size;
      const isSkillMastered = (distinctCorrectCount >= minDistinct) && (lowSupportCount >= minLowSupport);

      skillResults[skillId] = {
        id: skillId,
        name: skillDef.name || skillId,
        importance: skillDef.importance || 'core',
        distinctCorrectCount,
        lowSupportCount,
        requiredDistinct: minDistinct,
        requiredLowSupport: minLowSupport,
        mastered: isSkillMastered
      };

      if (isSkillMastered) {
        masteredCount += 1;
      } else {
        allMastered = false;
        if (skillDef.importance === 'core') {
          allCoreMastered = false;
        }
      }
    }

    return {
      skills: skillResults,
      allMastered,
      allCoreMastered,
      masteredSkillsCount: masteredCount,
      totalSkillsCount
    };
  }
}

/**
 * Factory function for creating a topic-agnostic StageController.
 * 
 * @param {Object} params
 * @param {Object} params.topicData - Learning-Topic JSON (v3.3+)
 * @param {Object} [params.studentState] - Student state
 * @param {string} [params.unitId] - Unit identifier
 * @param {string} [params.currentStage] - Current internal or student-facing stage
 * @returns {StageController}
 */
export function createStageController(params = {}) {
  return new StageController(params);
}

export default {
  INTERNAL_STAGES,
  STUDENT_TO_INTERNAL_STAGE,
  INTERNAL_TO_STUDENT_STAGE,
  STUDENT_STAGE_DISPLAY_NAMES,
  DECISION_TYPES,
  normalizeStage,
  getStudentStageLabel,
  getStudentFacingTitle,
  StageController,
  createStageController
};
