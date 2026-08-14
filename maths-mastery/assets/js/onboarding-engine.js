/**
 * SJMaths Maths Mastery
 * First-Time User Onboarding Engine
 *
 * Responsibilities:
 * - Determine onboarding status
 * - Select onboarding route
 * - Preserve optional exam selection
 * - Start foundation pathway
 * - Start diagnostic pathway
 *
 * This module does NOT:
 * - calculate mastery
 * - calculate recommendations
 * - record question evidence
 * - run diagnostic scoring
 */


/* ============================================================
   Constants
   ============================================================ */

const ONBOARDING_STATUS = {

    NOT_STARTED:
        "not-started",

    IN_PROGRESS:
        "in-progress",

    COMPLETED:
        "completed"
};


const ONBOARDING_ROUTES = {

    DIAGNOSTIC:
        "diagnostic",

    FOUNDATION:
        "foundation"
};


/* ============================================================
   Create Empty Onboarding
   ============================================================ */

export function createEmptyOnboarding(
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

        status:
            ONBOARDING_STATUS.NOT_STARTED,

        route:
            null,

        selectedExam:
            null,

        startingPoint:
            null,

        completedAt:
            null
    };
}


/* ============================================================
   Start Onboarding
   ============================================================ */

export function startOnboarding(
    onboarding
) {

    if (!onboarding) {

        throw new Error(
            "onboarding state is required"
        );
    }


    return {

        ...onboarding,

        status:
            ONBOARDING_STATUS.IN_PROGRESS
    };
}


/* ============================================================
   Select Exam
   ============================================================ */

export function selectExam(
    onboarding,
    examId
) {

    if (!onboarding) {

        throw new Error(
            "onboarding state is required"
        );
    }


    if (
        examId !== null &&
        typeof examId !==
            "string"
    ) {

        throw new Error(
            "examId must be a string or null"
        );
    }


    return {

        ...onboarding,

        selectedExam:
            examId
    };
}


/* ============================================================
   Select Diagnostic Route
   ============================================================ */

export function selectDiagnosticRoute(
    onboarding
) {

    if (!onboarding) {

        throw new Error(
            "onboarding state is required"
        );
    }


    return {

        ...onboarding,

        status:
            ONBOARDING_STATUS.IN_PROGRESS,

        route:
            ONBOARDING_ROUTES.DIAGNOSTIC,

        startingPoint:
            null
    };
}


/* ============================================================
   Select Foundation Route
   ============================================================ */

export function selectFoundationRoute(
    onboarding,
    startingTopic =
        "number-system"
) {

    if (!onboarding) {

        throw new Error(
            "onboarding state is required"
        );
    }


    if (
        !startingTopic ||
        typeof startingTopic !==
            "string"
    ) {

        throw new Error(
            "startingTopic is required"
        );
    }


    return {

        ...onboarding,

        status:
            ONBOARDING_STATUS.COMPLETED,

        route:
            ONBOARDING_ROUTES.FOUNDATION,

        startingPoint:
            startingTopic,

        completedAt:
            new Date().toISOString()
    };
}


/* ============================================================
   Prepare Diagnostic Route
   ============================================================ */

export function prepareDiagnostic(
    onboarding
) {

    if (!onboarding) {

        throw new Error(
            "onboarding state is required"
        );
    }


    return {

        ...onboarding,

        status:
            ONBOARDING_STATUS.IN_PROGRESS,

        route:
            ONBOARDING_ROUTES.DIAGNOSTIC,

        startingPoint:
            null
    };
}


/* ============================================================
   Complete Diagnostic Onboarding
   ============================================================ */

export function completeDiagnosticOnboarding(
    onboarding,
    startingPoint
) {

    if (!onboarding) {

        throw new Error(
            "onboarding state is required"
        );
    }


    if (
        !startingPoint ||
        typeof startingPoint !==
            "string"
    ) {

        throw new Error(
            "startingPoint is required"
        );
    }


    return {

        ...onboarding,

        status:
            ONBOARDING_STATUS.COMPLETED,

        route:
            ONBOARDING_ROUTES.DIAGNOSTIC,

        startingPoint,

        completedAt:
            new Date().toISOString()
    };
}


/* ============================================================
   Validation
   ============================================================ */

export function validateOnboarding(
    onboarding
) {

    if (!onboarding) {

        return false;
    }


    if (
        !onboarding.studentId ||
        typeof onboarding.studentId !==
            "string"
    ) {

        return false;
    }


    if (
        !Object.values(
            ONBOARDING_STATUS
        ).includes(
            onboarding.status
        )
    ) {

        return false;
    }


    if (
        onboarding.route !== null &&
        !Object.values(
            ONBOARDING_ROUTES
        ).includes(
            onboarding.route
        )
    ) {

        return false;
    }


    if (
        onboarding.selectedExam !== null &&
        typeof onboarding.selectedExam !==
            "string"
    ) {

        return false;
    }


    if (
        onboarding.startingPoint !== null &&
        typeof onboarding.startingPoint !==
            "string"
    ) {

        return false;
    }


    return true;
}


/* ============================================================
   Completion Check
   ============================================================ */

export function isOnboardingComplete(
    onboarding
) {

    return (
        onboarding?.status ===
            ONBOARDING_STATUS.COMPLETED
    );
}


/* ============================================================
   Export Constants
   ============================================================ */

export {
    ONBOARDING_STATUS,
    ONBOARDING_ROUTES
};


export default {

    ONBOARDING_STATUS,

    ONBOARDING_ROUTES,

    createEmptyOnboarding,

    startOnboarding,

    selectExam,

    selectDiagnosticRoute,

    selectFoundationRoute,

    prepareDiagnostic,

    completeDiagnosticOnboarding,

    validateOnboarding,

    isOnboardingComplete
};
