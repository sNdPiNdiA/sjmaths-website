/**
 * learning-engine.js
 * 
 * Generic, topic-agnostic learning engine for SJMaths.
 * Accepts ANY valid Learning-Topic JSON specification (schema_version 2.0.0+)
 * and operates purely from topicData, studentState, and pedagogical policy.
 * 
 * Zero hardcoded chapter numbers, topic titles, or question IDs.
 */

import { StateStore } from './state-store.js';

/**
 * Factory creating a generic learning engine instance for any Learning-Topic.
 * 
 * @param {Object} options
 * @param {Object} options.topicData - Validated Learning-Topic JSON object
 * @param {StateStore} [options.stateStore] - Optional StateStore instance
 * @returns {Object} Generic learning engine interface
 */
export function createLearningEngine({ topicData, stateStore = null }) {
  if (!topicData || typeof topicData !== 'object') {
    throw new Error('LearningEngine requires a valid topicData object.');
  }

  // Freeze dataset to guarantee immutability
  const DATA = Object.freeze(JSON.parse(JSON.stringify(topicData)));
  const defaultStore = stateStore || new StateStore();

  /**
   * Helper: Find a question by ID anywhere across the topic dataset
   * (prerequisite checks, practice stages, PYQs, unit gates, chapter exams).
   */
  function findQuestionById(questionId) {
    if (!questionId) return null;

    if (Array.isArray(DATA.units)) {
      for (const unit of DATA.units) {
        // 1. Prerequisite Precheck
        if (unit.prerequisite_check && unit.prerequisite_check.id === questionId) {
          return { item: unit.prerequisite_check, type: 'precheck', unitId: unit.id };
        }
        // 2. Practice (Guided / Independent)
        if (unit.practice_stages && Array.isArray(unit.practice_stages.guided_and_independent)) {
          const found = unit.practice_stages.guided_and_independent.find(q => q.id === questionId);
          if (found) return { item: found, type: 'practice', unitId: unit.id };
        }
        // 3. PYQs / Transfer
        if (unit.practice_stages && Array.isArray(unit.practice_stages.transfer_and_pyq)) {
          const found = unit.practice_stages.transfer_and_pyq.find(q => q.id === questionId);
          if (found) return { item: found, type: 'pyq', unitId: unit.id };
        }
        // 4. Unit Mastery Gate
        if (unit.unit_mastery_gate && Array.isArray(unit.unit_mastery_gate.questions)) {
          const found = unit.unit_mastery_gate.questions.find(q => q.id === questionId);
          if (found) return { item: found, type: 'unit_test', unitId: unit.id };
        }
      }
    }

    // 5. Global Topic Prerequisites (if any)
    if (Array.isArray(DATA.prerequisites)) {
      const foundPrereq = DATA.prerequisites.find(p => p.id === questionId);
      if (foundPrereq) return { item: foundPrereq, type: 'precheck', unitId: null };
    }

    // 6. Chapter Mastery Gate Exam
    if (DATA.mastery && DATA.mastery.chapter_mastery_gate && Array.isArray(DATA.mastery.chapter_mastery_gate.questions)) {
      const found = DATA.mastery.chapter_mastery_gate.questions.find(q => q.id === questionId);
      if (found) return { item: found, type: 'chapter_exam', unitId: null };
    }

    return null;
  }

  /**
   * 1. getTopicOutline
   * Returns generic topic metadata, scope, sequence, skills, and unit summaries.
   */
  function getTopicOutline(params = {}) {
    return {
      topic: {
        id: DATA.topic.id,
        title: DATA.topic.title,
        grade: DATA.topic.grade,
        subject: DATA.topic.subject,
        standard: DATA.topic.standard,
        description: DATA.topic.description
      },
      scope: DATA.scope,
      sequence: DATA.sequence,
      skills: DATA.skills,
      units: (DATA.units || []).map(u => ({
        id: u.id,
        unit_number: u.unit_number,
        title: u.title,
        icon: u.icon,
        skills_covered: u.skills_covered
      }))
    };
  }

  /**
   * 2. getUnitContent
   * Retrieves sanitized instructional content with configurable assessment answer suppression.
   */
  function getUnitContent(params = {}) {
    if (!params.unit_id) {
      throw new Error('Parameter "unit_id" is required.');
    }
    const unit = (DATA.units || []).find(u => u.id === params.unit_id);
    if (!unit) {
      throw new Error(`Unit "${params.unit_id}" not found.`);
    }

    const mode = params.mode === 'study' ? 'study' : 'assessment';
    const includePractice = Boolean(params.include_practice);

    const result = {
      unit_id: unit.id,
      unit_number: unit.unit_number,
      title: unit.title,
      icon: unit.icon,
      skills_covered: unit.skills_covered,
      instruction: {
        core_concepts: unit.instruction ? unit.instruction.core_concepts : [],
        formulas: unit.instruction ? unit.instruction.formulas : [],
        callout_boxes: unit.instruction ? unit.instruction.callout_boxes : []
      }
    };

    if (includePractice && unit.practice_stages) {
      const practice = (unit.practice_stages.guided_and_independent || []).map(q => {
        const item = {
          id: q.id,
          stage: q.stage,
          skill_id: q.skill_id,
          difficulty: q.difficulty,
          question: q.question,
          options: q.options
        };
        if (mode === 'study') {
          item.correct_index = q.correct_index;
          item.solution = q.solution;
        }
        return item;
      });

      const pyqs = (unit.practice_stages.transfer_and_pyq || []).map(q => {
        const item = {
          id: q.id,
          stage: q.stage,
          skill_id: q.skill_id,
          year: q.year,
          marks: q.marks,
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

  /**
   * 3. getPrerequisiteCheck
   * Retrieves diagnostic precheck with answer suppression.
   */
  function getPrerequisiteCheck(params = {}) {
    if (!params.unit_id) {
      throw new Error('Parameter "unit_id" is required.');
    }
    const unit = (DATA.units || []).find(u => u.id === params.unit_id);
    if (!unit) {
      throw new Error(`Unit "${params.unit_id}" not found.`);
    }

    const check = unit.prerequisite_check;
    if (!check) {
      throw new Error(`No prerequisite check defined for unit "${params.unit_id}".`);
    }

    return {
      unit_id: unit.id,
      check_id: check.id,
      question: check.question,
      options: check.options
    };
  }

  /**
   * 4. evaluatePractice
   * Evaluates student answer submission, updates versioned evidence state,
   * detects error streak / remediation triggers, and enforces assessment safety.
   */
  function evaluatePractice(params = {}, store = defaultStore) {
    if (!params.question_id) {
      throw new Error('Parameter "question_id" is required.');
    }
    if (typeof params.selected_index !== 'number') {
      throw new Error('Parameter "selected_index" must be a number.');
    }

    const found = findQuestionById(params.question_id);
    if (!found) {
      throw new Error(`Question "${params.question_id}" not found.`);
    }

    const q = found.item;
    const isOutOfBounds = params.selected_index < 0 || params.selected_index >= q.options.length;
    if (isOutOfBounds) {
      throw new Error(`selected_index ${params.selected_index} is out of bounds (options length: ${q.options.length}).`);
    }

    const isCorrect = params.selected_index === q.correct_index;

    // Record attempt into student state store
    let updatedState = null;
    if (store) {
      updatedState = store.recordAttempt(q.id, isCorrect, params.selected_index, q.skill_id || null, q.stage || found.type);
    }

    const currentStreak = updatedState ? updatedState.recent_error_streak : 0;
    const remediationThreshold = (DATA.remediation && DATA.remediation.rules && DATA.remediation.rules.trigger_after_consecutive_errors) || 2;
    const shouldRemediate = !isCorrect && currentStreak >= remediationThreshold;

    const response = {
      question_id: q.id,
      skill_id: q.skill_id || null,
      is_correct: isCorrect,
      recent_error_streak: currentStreak,
      remediation_triggered: shouldRemediate
    };

    if (found.type === 'precheck') {
      if (isCorrect) {
        response.feedback = q.pass_feedback || 'Correct! Prerequisite validated.';
      } else {
        response.feedback = 'Incorrect. Review the prerequisite concept or request a hint.';
      }
      return response;
    }

    if (isCorrect) {
      response.feedback = 'Correct!';
      if (q.solution) {
        response.solution_derivation = q.solution;
      }
    } else {
      response.feedback = 'Incorrect. Try again, request a progressive hint, or review the formula.';
      if (shouldRemediate) {
        response.remediation_target = {
          type: 'formula_review',
          unit_id: found.unitId
        };
      }
    }

    return response;
  }

  /**
   * 5. getHint
   * Progressive 3-level hint delivery resolving actual skill names from topic taxonomy.
   */
  function getHint(params = {}, store = defaultStore) {
    if (!params.question_id) {
      throw new Error('Parameter "question_id" is required.');
    }
    const level = Number(params.hint_level) || 1;
    if (![1, 2, 3].includes(level)) {
      throw new Error('Parameter "hint_level" must be 1, 2, or 3.');
    }

    const found = findQuestionById(params.question_id);
    if (!found) {
      throw new Error(`Question "${params.question_id}" not found.`);
    }

    if (store) {
      store.recordHintUsage(params.question_id, level);
    }

    const q = found.item;
    const hints = q.hints || [];

    let hintType = 'conceptual';
    let hintText = '';

    if (level === 1) {
      hintType = 'conceptual';
      const skillObj = (q.skill_id && Array.isArray(DATA.skills)) ? DATA.skills.find(s => s.id === q.skill_id) : null;
      const skillDisplayName = skillObj ? skillObj.name : (q.skill_id || (DATA.topic ? DATA.topic.title : 'Concept Principles'));
      hintText = hints.length > 0 ? hints[0] : `Recall the fundamental principle for "${skillDisplayName}".`;
    } else if (level === 2) {
      hintType = 'procedural';
      hintText = hints.length > 1 ? hints[1] : (hints.length === 1 ? hints[0] : 'Form the algebraic equation in standard form and identify all required parameters.');
    } else if (level === 3) {
      hintType = 'full_solution';
      hintText = q.solution ? `Full Solution Derivation: ${q.solution}` : 'Complete solution derivation available.';
    }

    return {
      question_id: q.id,
      hint_level: level,
      hint_type: hintType,
      hint_text: hintText
    };
  }

  /**
   * 6. getNextLearningAction
   * Pedagogical decision engine evaluating progression across active unit practice,
   * evidence completeness, transfer PYQs, and remediation thresholds.
   */
  function getNextLearningAction(params = {}, store = defaultStore) {
    const state = store ? store.getState() : (params.student_state || {});
    const defaultUnitId = (DATA.sequence && DATA.sequence.unit_order && DATA.sequence.unit_order[0]) || (DATA.units && DATA.units[0] && DATA.units[0].id);
    const currentUnitId = params.current_unit_id || state.current_unit_id || defaultUnitId;
    const completedQIds = params.completed_question_ids || Object.keys(state.completed_questions || {});
    const recentErrors = typeof params.recent_error_streak === 'number' ? params.recent_error_streak : (state.recent_error_streak || 0);

    const unit = (DATA.units || []).find(u => u.id === currentUnitId);
    if (!unit) {
      throw new Error(`Unit "${currentUnitId}" not recognized in learning sequence.`);
    }

    // 1. Check for remediation fallback
    const errorThreshold = (DATA.remediation && DATA.remediation.rules && DATA.remediation.rules.trigger_after_consecutive_errors) || 2;
    if (recentErrors >= errorThreshold) {
      const firstFormula = (unit.instruction && unit.instruction.formulas && unit.instruction.formulas[0]) || null;
      return {
        action: 'recommend_remediation',
        reason: `Student encountered ${recentErrors} consecutive errors. Recommended formula review.`,
        target_resource: {
          type: 'formula_review',
          unit_id: unit.id,
          formula: firstFormula ? firstFormula.rule : (unit.title || 'Core Formulas')
        }
      };
    }

    // 2. Check practice progression
    const allPractice = (unit.practice_stages && unit.practice_stages.guided_and_independent) || [];
    const pendingPractice = allPractice.find(p => !completedQIds.includes(p.id));

    if (pendingPractice) {
      const skillEvidence = (state.skill_evidence && state.skill_evidence[pendingPractice.skill_id]) || null;
      const isInsufficient = skillEvidence && (!skillEvidence.correct_question_ids || skillEvidence.correct_question_ids.length < 2);
      return {
        action: 'continue_practice',
        reason: isInsufficient ? 'Skill requires additional evidence before mastery.' : 'Continue active unit practice questions.',
        next_question_id: pendingPractice.id,
        stage: pendingPractice.stage,
        skill_id: pendingPractice.skill_id
      };
    }

    // 3. Check PYQ / transfer progression
    const allPyqs = (unit.practice_stages && unit.practice_stages.transfer_and_pyq) || [];
    const pendingPyq = allPyqs.find(q => !completedQIds.includes(q.id));

    if (pendingPyq) {
      return {
        action: 'attempt_pyq_transfer',
        reason: 'Practice completed. Advance to board examination transfer questions.',
        next_question_id: pendingPyq.id,
        stage: pendingPyq.stage,
        skill_id: pendingPyq.skill_id
      };
    }

    // 4. Recommend Unit Mastery Gate
    return {
      action: 'take_unit_gate',
      reason: `All practice and transfer questions for "${unit.title}" completed. Ready for unit assessment gate.`,
      unit_id: unit.id
    };
  }

  /**
   * 7. startMasteryExam
   * Generates cumulative topic mastery exam with strict answer key suppression.
   */
  function startMasteryExam(params = {}) {
    const exam = (DATA.mastery && DATA.mastery.chapter_mastery_gate) || {
      assessment_id: 'mastery-exam-default',
      title: 'Chapter Mastery Exam',
      description: 'Comprehensive chapter exam',
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
      description: exam.description,
      pass_percent: exam.pass_percent,
      total_questions: sanitizedQuestions.length,
      questions: sanitizedQuestions
    };
  }

  /**
   * 8. getLearningProgress
   * Calculates overall progress percentage, unit completion, and evidence-based skills mastered.
   */
  function getLearningProgress(params = {}, store = defaultStore) {
    const state = store ? store.getState() : (params.student_state || {});
    const completedUnits = state.completed_units || [];
    const masteredSkills = state.mastered_skills || [];
    const completedQMap = state.completed_questions || {};

    const totalUnits = (DATA.units || []).length;
    const totalSkills = (DATA.skills || []).length;
    const solvedQuestionsCount = Object.values(completedQMap).filter(q => q && q.solved).length;

    const progressPct = totalUnits > 0 ? Math.round((completedUnits.length / totalUnits) * 100) : 0;
    const readyForExam = completedUnits.length >= totalUnits && totalUnits > 0;

    let nextUnit = null;
    const unitOrder = (DATA.sequence && DATA.sequence.unit_order) || (DATA.units || []).map(u => u.id);
    for (const uId of unitOrder) {
      if (!completedUnits.includes(uId)) {
        nextUnit = uId;
        break;
      }
    }

    return {
      topic_id: DATA.topic ? DATA.topic.id : 'unknown-topic',
      topic_title: DATA.topic ? DATA.topic.title : 'Unknown Topic',
      overall_progress_percent: progressPct,
      units_completed_count: completedUnits.length,
      total_units: totalUnits,
      skills_mastered_count: masteredSkills.length,
      total_skills: totalSkills,
      solved_questions_count: solvedQuestionsCount,
      is_ready_for_mastery_exam: readyForExam,
      next_pending_unit: nextUnit,
      exam_status: state.mastery_exam_session || null
    };
  }

  return {
    findQuestionById,
    getTopicOutline,
    getUnitContent,
    getPrerequisiteCheck,
    evaluatePractice,
    getHint,
    getNextLearningAction,
    startMasteryExam,
    getLearningProgress
  };
}

export default {
  createLearningEngine
};
