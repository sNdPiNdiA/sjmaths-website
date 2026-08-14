import {
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
} from "./learner-flow-engine.js";


let passed = 0;
let failed = 0;


function pass(
    message
) {

    passed++;

    console.log(
        `✓ ${message}`
    );
}


function fail(
    message
) {

    failed++;

    console.log(
        `✗ ${message}`
    );
}


function assert(
    condition,
    message
) {

    if (condition) {

        pass(
            message
        );

    }
    else {

        fail(
            message
        );
    }
}


console.log("");

console.log(
    "============================================"
);

console.log(
    " STEP 22 — UNIFIED LEARNER FLOW TESTS"
);

console.log(
    "============================================"
);

console.log("");


/* ============================================================
   TEST 1 — Brand New User
   ============================================================ */

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 1 — Brand New User"
);

console.log(
    "--------------------------------------------"
);


let flow =
    createNewLearnerFlow(
        "student-001"
    );


assert(
    flow.studentId ===
        "student-001",
    "Student ID stored"
);


assert(
    flow.learnerState ===
        FLOW_STATES.NEW,
    "New user starts in NEW state"
);


assert(
    flow.hasEvidence ===
        false,
    "New user has no evidence"
);


assert(
    validateLearnerFlow(
        flow
    ),
    "New learner flow is valid"
);


assert(
    determineFlowState(
        flow,
        null
    ) ===
        FLOW_STATES.NEW,
    "NEW state detected correctly"
);



/* ============================================================
   TEST 2 — Start Onboarding
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 2 — Start Onboarding"
);

console.log(
    "--------------------------------------------"
);


flow =
    startOnboarding(
        flow
    );


assert(
    flow.learnerState ===
        FLOW_STATES.ONBOARDING,
    "Learner enters ONBOARDING state"
);


assert(
    flow.onboarding.status ===
        "in-progress",
    "Onboarding is in progress"
);



/* ============================================================
   TEST 3 — Optional Exam Selection
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 3 — Exam Selection"
);

console.log(
    "--------------------------------------------"
);


flow =
    selectExam(
        flow,
        "ssc"
    );


assert(
    flow.onboarding.selectedExam ===
        "ssc",
    "SSC exam stored"
);


assert(
    flow.learnerState ===
        FLOW_STATES.ONBOARDING,
    "Exam selection does not prematurely start learning"
);



/* ============================================================
   TEST 4 — Foundation Route
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 4 — Foundation Route"
);

console.log(
    "--------------------------------------------"
);


const foundationFlow =
    selectFoundationRoute(
        flow,
        "number-system"
    );


assert(
    foundationFlow.learnerState ===
        FLOW_STATES.LEARNING,
    "Foundation route enters LEARNING"
);


assert(
    foundationFlow.onboarding.route ===
        FLOW_ROUTES.FOUNDATION,
    "Foundation route recorded"
);


assert(
    foundationFlow.learning.currentTopic ===
        "number-system",
    "Foundation starts at Number System"
);


assert(
    foundationFlow.hasEvidence ===
        false,
    "Foundation selection does not invent evidence"
);



/* ============================================================
   TEST 5 — Diagnostic Route
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 5 — Diagnostic Route"
);

console.log(
    "--------------------------------------------"
);


let diagnosticFlow =
    prepareDiagnostic(
        flow
    );


assert(
    diagnosticFlow.learnerState ===
        FLOW_STATES.DIAGNOSTIC,
    "Diagnostic enters DIAGNOSTIC state"
);


assert(
    diagnosticFlow.onboarding.route ===
        FLOW_ROUTES.DIAGNOSTIC,
    "Diagnostic route recorded"
);


assert(
    diagnosticFlow.diagnostic.status ===
        "in-progress",
    "Diagnostic is in progress"
);


assert(
    diagnosticFlow.hasEvidence ===
        false,
    "Preparing diagnostic does not invent evidence"
);



/* ============================================================
   TEST 6 — Diagnostic Completion
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 6 — Diagnostic Completion"
);

console.log(
    "--------------------------------------------"
);


diagnosticFlow =
    completeDiagnostic(
        diagnosticFlow,
        {

            startingPoint:
                "fractions",

            questionCount:
                10,

            completedAt:
                "2026-08-13T10:00:00.000Z"
        }
    );


assert(
    diagnosticFlow.learnerState ===
        FLOW_STATES.LEARNING,
    "Completed diagnostic enters LEARNING"
);


assert(
    diagnosticFlow.hasEvidence ===
        true,
    "Diagnostic creates evidence state"
);


assert(
    diagnosticFlow.diagnostic.completed ===
        true,
    "Diagnostic completion recorded"
);


assert(
    diagnosticFlow.diagnostic.startingPoint ===
        "fractions",
    "Diagnostic starting point preserved"
);


assert(
    diagnosticFlow.learning.currentTopic ===
        "fractions",
    "Learning starts at diagnostic placement"
);



/* ============================================================
   TEST 7 — Learning Result
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 7 — Learning Result"
);

console.log(
    "--------------------------------------------"
);


let learningFlow =
    applyLearningResult(
        diagnosticFlow,
        {

            topicId:
                "fractions",

            mastery:
                68,

            weakSkills:
                [
                    "fraction-comparison"
                ],

            nextTopic:
                "percentage"
        }
    );


assert(
    learningFlow.hasEvidence ===
        true,
    "Learning result preserves evidence state"
);


assert(
    learningFlow.learning.mastery ===
        68,
    "Mastery result stored"
);


assert(
    learningFlow.learning.weakSkills.includes(
        "fraction-comparison"
    ),
    "Weak skill stored"
);


assert(
    learningFlow.learning.nextTopic ===
        "percentage",
    "Next topic stored"
);



/* ============================================================
   TEST 8 — Recommendation
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 8 — Recommendation Integration"
);

console.log(
    "--------------------------------------------"
);


learningFlow =
    applyRecommendation(
        learningFlow,
        {

            topicId:
                "percentage"
        }
    );


assert(
    learningFlow.learning.nextTopic ===
        "percentage",
    "Recommendation becomes next topic"
);



/* ============================================================
   TEST 9 — Returning Learner
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 9 — Returning Learner"
);

console.log(
    "--------------------------------------------"
);


const returningFlow =
    markReturningLearner(
        learningFlow,
        {

            topics: {

                percentage: {

                    evidence: {

                        attempts:
                            10,

                        answered:
                            10
                    }
                }
            }
        }
    );


assert(
    returningFlow.learnerState ===
        FLOW_STATES.RETURNING,
    "Established learner becomes RETURNING"
);


assert(
    returningFlow.hasEvidence ===
        true,
    "Returning learner retains evidence"
);



/* ============================================================
   TEST 10 — Evidence Detection
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 10 — Evidence Detection"
);

console.log(
    "--------------------------------------------"
);


assert(
    hasLearningEvidence(
        null
    ) ===
        false,
    "Missing progress has no evidence"
);


assert(
    hasLearningEvidence(
        {
            topics: {}
        }
    ) ===
        false,
    "Empty topics have no evidence"
);


assert(
    hasLearningEvidence(
        {

            topics: {

                percentage: {

                    evidence: {

                        attempts:
                            1
                    }
                }
            }

        }
    ) ===
        true,
    "Recorded attempt creates evidence"
);



/* ============================================================
   TEST 11 — Dashboard State
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 11 — Dashboard State"
);

console.log(
    "--------------------------------------------"
);


const newDashboard =
    buildDashboardState(
        flow
    );


assert(
    newDashboard.mode ===
        "onboarding",
    "NEW user receives onboarding dashboard"
);


const diagnosticDashboard =
    buildDashboardState(
        diagnosticFlow
    );


assert(
    diagnosticDashboard.mode ===
        "learning",
    "Completed diagnostic receives learning dashboard"
);


const returningDashboard =
    buildDashboardState(
        returningFlow
    );


assert(
    returningDashboard.mode ===
        "returning",
    "Returning learner receives returning dashboard"
);



/* ============================================================
   TEST 12 — Immutable Updates
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 12 — Immutable Updates"
);

console.log(
    "--------------------------------------------"
);


const original =
    createNewLearnerFlow(
        "student-immutable"
    );


const updated =
    updateFlow(
        original,
        draft => {

            draft.onboarding.status =
                "in-progress";

            draft.learnerState =
                FLOW_STATES.ONBOARDING;

            return draft;
        }
    );


assert(
    original.learnerState ===
        FLOW_STATES.NEW,
    "Original flow remains unchanged"
);


assert(
    updated.learnerState ===
        FLOW_STATES.ONBOARDING,
    "Updated flow contains new state"
);


assert(
    updated !==
        original,
    "Flow update is immutable"
);



/* ============================================================
   TEST 13 — Complete First-Time Journey
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 13 — Complete First-Time Journey"
);

console.log(
    "--------------------------------------------"
);


let journey =
    createNewLearnerFlow(
        "student-journey"
    );


assert(
    journey.learnerState ===
        FLOW_STATES.NEW,
    "Journey begins as NEW"
);


journey =
    startOnboarding(
        journey
    );


assert(
    journey.learnerState ===
        FLOW_STATES.ONBOARDING,
    "Journey enters onboarding"
);


journey =
    selectExam(
        journey,
        "ssc"
    );


journey =
    prepareDiagnostic(
        journey
    );


assert(
    journey.learnerState ===
        FLOW_STATES.DIAGNOSTIC,
    "Journey enters diagnostic"
);


journey =
    completeDiagnostic(
        journey,
        {

            startingPoint:
                "fractions",

            questionCount:
                10,

            completedAt:
                "2026-08-13T10:00:00.000Z"
        }
    );


assert(
    journey.learnerState ===
        FLOW_STATES.LEARNING,
    "Journey reaches learning"
);


assert(
    journey.onboarding.selectedExam ===
        "ssc",
    "Selected exam survives complete journey"
);


assert(
    journey.learning.currentTopic ===
        "fractions",
    "Diagnostic placement survives complete journey"
);


assert(
    journey.hasEvidence ===
        true,
    "Diagnostic evidence state survives complete journey"
);



/* ============================================================
   TEST 14 — Foundation First-Time Journey
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 14 — Foundation First-Time Journey"
);

console.log(
    "--------------------------------------------"
);


let foundationJourney =
    createNewLearnerFlow(
        "student-foundation"
    );


foundationJourney =
    startOnboarding(
        foundationJourney
    );


foundationJourney =
    selectExam(
        foundationJourney,
        "ssc"
    );


foundationJourney =
    selectFoundationRoute(
        foundationJourney,
        "number-system"
    );


assert(
    foundationJourney.learnerState ===
        FLOW_STATES.LEARNING,
    "Foundation journey reaches learning"
);


assert(
    foundationJourney.learning.currentTopic ===
        "number-system",
    "Foundation journey starts at Number System"
);


assert(
    foundationJourney.hasEvidence ===
        false,
    "Foundation journey does not fake diagnostic evidence"
);



/* ============================================================
   TEST 15 — Flow Validation
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 15 — Flow Validation"
);

console.log(
    "--------------------------------------------"
);


assert(
    validateLearnerFlow(
        journey
    ),
    "Complete diagnostic journey is valid"
);


assert(
    validateLearnerFlow(
        foundationJourney
    ),
    "Foundation journey is valid"
);


assert(
    validateLearnerFlow(
        returningFlow
    ),
    "Returning learner flow is valid"
);



/* ============================================================
   FINAL
   ============================================================ */

console.log("");

console.log(
    "============================================"
);

console.log(
    " STEP 22 TEST SUMMARY"
);

console.log(
    "============================================"
);

console.log("");

console.log(
    `Passed: ${passed}`
);

console.log(
    `Failed: ${failed}`
);

console.log("");

if (
    failed === 0
) {

    console.log(
        "✓ ALL UNIFIED LEARNER FLOW TESTS PASSED"
    );

    console.log(
        "✓ STEP 22 COMPLETE"
    );

}
else {

    console.log(
        "✗ STEP 22 FAILED — CHECK ERRORS ABOVE"
    );

    process.exitCode = 1;
}

console.log("");

console.log(
    "============================================"
);

console.log("");
