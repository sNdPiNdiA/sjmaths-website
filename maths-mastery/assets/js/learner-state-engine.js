/**
 * SJMaths Maths Mastery
 * Learner State Engine
 *
 * Determines where the student is in the learning lifecycle.
 *
 * IMPORTANT:
 * This engine does not calculate mastery.
 * It only determines learner state.
 */


/* ============================================================
   Constants
   ============================================================ */

const STATES = {

    NEW:
        "new",

    ONBOARDING:
        "onboarding",

    LEARNING:
        "learning",

    RETURNING:
        "returning"
};


/* ============================================================
   Check Evidence
   ============================================================ */

export function hasProgressEvidence(
    progress
) {

    if (
        !progress ||
        !progress.topics
    ) {

        return false;
    }


    const topicIds =
        Object.keys(
            progress.topics
        );


    if (
        topicIds.length === 0
    ) {

        return false;
    }


    /*
     * Evidence exists only when there is
     * actual activity.
     */

    return topicIds.some(
        topicId => {

            const topic =
                progress.topics[
                    topicId
                ];


            if (!topic) {

                return false;
            }


            const attempts =
                topic.attempts || 0;


            const timeSpent =
                topic.timeSpentSeconds || 0;


            const evidenceCount =
                topic.evidenceCount || 0;


            return (
                attempts > 0 ||
                timeSpent > 0 ||
                evidenceCount > 0
            );
        }
    );
}


/* ============================================================
   Determine Learner State
   ============================================================ */

export function determineLearnerState(
    progress
) {

    const evidence =
        hasProgressEvidence(
            progress
        );


    if (!evidence) {

        return STATES.NEW;
    }


    /*
     * If the student has evidence,
     * they are no longer a new learner.
     *
     * Returning state is reserved for
     * a student who already has established
     * learning history.
     */

    const topics =
        progress.topics || {};


    const topicCount =
        Object.keys(
            topics
        ).length;


    if (
        topicCount >= 2
    ) {

        return STATES.RETURNING;
    }


    return STATES.LEARNING;
}


/* ============================================================
   Build Learner State
   ============================================================ */

export function buildLearnerState(
    progress,
    options = {}
) {

    const state =
        determineLearnerState(
            progress
        );


    const evidence =
        hasProgressEvidence(
            progress
        );


    return {

        version:
            "1.0.0",

        studentId:
            progress?.studentId ||
            options.studentId ||
            "local",

        state,

        hasEvidence:
            evidence,

        selectedExam:
            options.selectedExam ??
            progress?.selectedExam ??
            null,

        startingPoint:
            options.startingPoint ??
            progress?.startingPoint ??
            null,

        diagnosticCompleted:
            options.diagnosticCompleted ??
            progress?.diagnosticCompleted ??
            false,

        lastActiveAt:
            options.lastActiveAt ??
            progress?.updatedAt ??
            null
    };
}


/* ============================================================
   State Helpers
   ============================================================ */

export function isNewLearner(
    learnerState
) {

    return (
        learnerState?.state ===
            STATES.NEW
    );
}


export function isOnboarding(
    learnerState
) {

    return (
        learnerState?.state ===
            STATES.ONBOARDING
    );
}


export function isLearning(
    learnerState
) {

    return (
        learnerState?.state ===
            STATES.LEARNING
    );
}


export function isReturning(
    learnerState
) {

    return (
        learnerState?.state ===
            STATES.RETURNING
    );
}


/* ============================================================
   Start Onboarding
   ============================================================ */

export function startOnboarding(
    learnerState
) {

    return {

        ...learnerState,

        state:
            STATES.ONBOARDING
    };
}


/* ============================================================
   Complete Starting Selection
   ============================================================ */

export function completeStartingSelection(
    learnerState,
    {
        selectedExam = null,
        startingPoint = null
    } = {}
) {

    return {

        ...learnerState,

        state:
            STATES.LEARNING,

        hasEvidence:
            false,

        selectedExam,

        startingPoint
    };
}


/* ============================================================
   Complete Diagnostic
   ============================================================ */

export function completeDiagnostic(
    learnerState,
    {
        selectedExam = null,
        startingPoint = null
    } = {}
) {

    return {

        ...learnerState,

        state:
            STATES.LEARNING,

        hasEvidence:
            true,

        selectedExam,

        startingPoint,

        diagnosticCompleted:
            true
    };
}


/* ============================================================
   Export Constants
   ============================================================ */

export {
    STATES
};


export default {

    STATES,

    hasProgressEvidence,

    determineLearnerState,

    buildLearnerState,

    isNewLearner,

    isOnboarding,

    isLearning,

    isReturning,

    startOnboarding,

    completeStartingSelection,

    completeDiagnostic
};
