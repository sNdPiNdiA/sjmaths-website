/**
 * SJMaths Maths Mastery
 * STEP 22 — Unified Learner Flow
 *
 * This module is the orchestration layer.
 *
 * It deliberately does NOT duplicate:
 *
 * - progress calculations
 * - mastery calculations
 * - recommendation calculations
 * - diagnostic graph logic
 *
 * Those remain owned by their respective engines.
 */


/* ============================================================
   Constants
   ============================================================ */

export const FLOW_STATES = Object.freeze({

    NEW:
        "NEW",

    ONBOARDING:
        "ONBOARDING",

    DIAGNOSTIC:
        "DIAGNOSTIC",

    LEARNING:
        "LEARNING",

    RETURNING:
        "RETURNING"

});


export const FLOW_ROUTES = Object.freeze({

    DIAGNOSTIC:
        "diagnostic",

    FOUNDATION:
        "foundation"

});


/* ============================================================
   Create New Flow
   ============================================================ */

export function createNewLearnerFlow(
    studentId
) {

    if (
        !studentId ||
        typeof studentId !==
            "string"
    ) {

        throw new Error(
            "studentId is required"
        );
    }


    return {

        version:
            "1.0.0",

        studentId,

        learnerState:
            FLOW_STATES.NEW,

        hasEvidence:
            false,

        onboarding: {

            status:
                "not-started",

            route:
                null,

            selectedExam:
                null,

            startingPoint:
                null,

            completed:
                false
        },

        diagnostic: {

            status:
                "not-started",

            completed:
                false,

            questionCount:
                0,

            startingPoint:
                null
        },

        learning: {

            currentTopic:
                null,

            nextTopic:
                null,

            mastery:
                null,

            weakSkills:
                []
        }
    };
}


/* ============================================================
   Detect Evidence
   ============================================================ */

export function hasLearningEvidence(
    progress
) {

    if (!progress) {
        return false;
    }


    const topics =
        progress.topics || {};


    return Object.values(
        topics
    ).some(
        topic => {

            if (!topic) {
                return false;
            }


            const evidence =
                topic.evidence;


            if (!evidence) {
                return false;
            }


            return (
                Number(
                    evidence.attempts ||
                    evidence.answered ||
                    0
                ) > 0
            );
        }
    );
}


/* ============================================================
   Determine Learner State
   ============================================================ */

export function determineFlowState(
    flow,
    progress = null
) {

    const evidence =
        hasLearningEvidence(
            progress
        );


    if (
        evidence
    ) {

        return FLOW_STATES.LEARNING;
    }


    if (
        flow?.onboarding?.status ===
        "in-progress"
    ) {

        return FLOW_STATES.ONBOARDING;
    }


    if (
        flow?.diagnostic?.status ===
        "in-progress"
    ) {

        return FLOW_STATES.DIAGNOSTIC;
    }


    return FLOW_STATES.NEW;
}


/* ============================================================
   Start Onboarding
   ============================================================ */

export function startOnboarding(
    flow
) {

    if (!flow) {
        throw new Error(
            "flow is required"
        );
    }


    return {

        ...flow,

        learnerState:
            FLOW_STATES.ONBOARDING,

        onboarding: {

            ...flow.onboarding,

            status:
                "in-progress"
        }
    };
}


/* ============================================================
   Select Exam
   ============================================================ */

export function selectExam(
    flow,
    examId
) {

    if (
        !examId ||
        typeof examId !==
            "string"
    ) {

        throw new Error(
            "examId is required"
        );
    }


    return {

        ...flow,

        onboarding: {

            ...flow.onboarding,

            selectedExam:
                examId
        }
    };
}


/* ============================================================
   Select Foundation Route
   ============================================================ */

export function selectFoundationRoute(
    flow,
    startingPoint =
        "number-system"
) {

    return {

        ...flow,

        learnerState:
            FLOW_STATES.LEARNING,

        hasEvidence:
            false,

        onboarding: {

            ...flow.onboarding,

            status:
                "completed",

            route:
                FLOW_ROUTES.FOUNDATION,

            startingPoint,

            completed:
                true
        },

        learning: {

            ...flow.learning,

            currentTopic:
                startingPoint
        }
    };
}


/* ============================================================
   Prepare Diagnostic
   ============================================================ */

export function prepareDiagnostic(
    flow
) {

    return {

        ...flow,

        learnerState:
            FLOW_STATES.DIAGNOSTIC,

        onboarding: {

            ...flow.onboarding,

            route:
                FLOW_ROUTES.DIAGNOSTIC,

            status:
                "in-progress"
        },

        diagnostic: {

            ...flow.diagnostic,

            status:
                "in-progress",

            completed:
                false
        }
    };
}


/* ============================================================
   Complete Diagnostic
   ============================================================ */

export function completeDiagnostic(
    flow,
    diagnosticResult
) {

    if (
        !diagnosticResult
    ) {

        throw new Error(
            "diagnosticResult is required"
        );
    }


    if (
        !diagnosticResult.startingPoint
    ) {

        throw new Error(
            "Diagnostic must provide startingPoint"
        );
    }


    return {

        ...flow,

        learnerState:
            FLOW_STATES.LEARNING,

        hasEvidence:
            true,

        onboarding: {

            ...flow.onboarding,

            status:
                "completed",

            route:
                FLOW_ROUTES.DIAGNOSTIC,

            startingPoint:
                diagnosticResult.startingPoint,

            completed:
                true
        },

        diagnostic: {

            ...flow.diagnostic,

            status:
                "completed",

            completed:
                true,

            questionCount:
                diagnosticResult.questionCount ||
                0,

            startingPoint:
                diagnosticResult.startingPoint,

            completedAt:
                diagnosticResult.completedAt ||
                new Date().toISOString()
        },

        learning: {

            ...flow.learning,

            currentTopic:
                diagnosticResult.startingPoint
        }
    };
}


/* ============================================================
   Record Learning Result
   ============================================================ */

export function applyLearningResult(
    flow,
    result
) {

    if (
        !result
    ) {

        throw new Error(
            "Learning result is required"
        );
    }


    if (
        !result.topicId
    ) {

        throw new Error(
            "Learning result requires topicId"
        );
    }


    return {

        ...flow,

        learnerState:
            FLOW_STATES.LEARNING,

        hasEvidence:
            true,

        learning: {

            ...flow.learning,

            currentTopic:
                result.topicId,

            nextTopic:
                result.nextTopic ??
                flow.learning.nextTopic,

            mastery:
                result.mastery ??
                flow.learning.mastery,

            weakSkills:
                result.weakSkills ??
                flow.learning.weakSkills
        }
    };
}


/* ============================================================
   Apply Recommendation
   ============================================================ */

export function applyRecommendation(
    flow,
    recommendation
) {

    if (
        !recommendation
    ) {

        return flow;
    }


    return {

        ...flow,

        learning: {

            ...flow.learning,

            nextTopic:
                recommendation.topicId ??
                null
        }
    };
}


/* ============================================================
   Returning Learner
   ============================================================ */

export function markReturningLearner(
    flow,
    progress
) {

    if (
        !hasLearningEvidence(
            progress
        )
    ) {

        return flow;
    }


    return {

        ...flow,

        learnerState:
            FLOW_STATES.RETURNING,

        hasEvidence:
            true
    };
}


/* ============================================================
   Build Dashboard State
   ============================================================ */

export function buildDashboardState(
    flow
) {

    const state =
        flow.learnerState;


    if (
        state ===
        FLOW_STATES.NEW
    ) {

        return {

            mode:
                "onboarding",

            title:
                "Start Your Maths Journey",

            action:
                "Begin"
        };
    }


    if (
        state ===
        FLOW_STATES.ONBOARDING
    ) {

        return {

            mode:
                "onboarding",

            title:
                "Set Up Your Learning Path",

            action:
                "Continue"
        };
    }


    if (
        state ===
        FLOW_STATES.DIAGNOSTIC
    ) {

        return {

            mode:
                "diagnostic",

            title:
                "Find Your Starting Point",

            action:
                "Continue Diagnostic"
        };
    }


    if (
        state ===
        FLOW_STATES.LEARNING
    ) {

        return {

            mode:
                "learning",

            title:
                "Continue Learning",

            action:
                flow.learning
                    ?.currentTopic
                    ? "Continue Topic"
                    : "Start Learning"
        };
    }


    if (
        state ===
        FLOW_STATES.RETURNING
    ) {

        return {

            mode:
                "returning",

            title:
                "Welcome Back",

            action:
                "Continue Learning"
        };
    }


    return {

        mode:
            "onboarding",

        title:
            "Start Your Maths Journey",

        action:
            "Begin"
    };
}


/* ============================================================
   Validate Flow
   ============================================================ */

export function validateLearnerFlow(
    flow
) {

    if (!flow) {
        return false;
    }


    if (
        !flow.studentId
    ) {
        return false;
    }


    if (
        !Object.values(
            FLOW_STATES
        ).includes(
            flow.learnerState
        )
    ) {

        return false;
    }


    if (
        typeof flow.hasEvidence !==
        "boolean"
    ) {

        return false;
    }


    if (
        !flow.onboarding
    ) {

        return false;
    }


    if (
        !flow.diagnostic
    ) {

        return false;
    }


    if (
        !flow.learning
    ) {

        return false;
    }


    return true;
}


/* ============================================================
   Immutable Flow Update
   ============================================================ */

export function updateFlow(
    flow,
    updater
) {

    if (
        typeof updater !==
        "function"
    ) {

        throw new Error(
            "updater must be a function"
        );
    }


    const updated =
        updater(
            structuredClone(
                flow
            )
        );


    if (
        !validateLearnerFlow(
            updated
        )
    ) {

        throw new Error(
            "Updated learner flow is invalid"
        );
    }


    return updated;
}


export default {

    FLOW_STATES,

    FLOW_ROUTES,

    createNewLearnerFlow,

    hasLearningEvidence,

    determineFlowState,

    startOnboarding,

    selectExam,

    selectFoundationRoute,

    prepareDiagnostic,

    completeDiagnostic,

    applyLearningResult,

    applyRecommendation,

    markReturningLearner,

    buildDashboardState,

    validateLearnerFlow,

    updateFlow
};
