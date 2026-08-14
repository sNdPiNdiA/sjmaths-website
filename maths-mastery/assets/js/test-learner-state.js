import {
    STATES,
    hasProgressEvidence,
    determineLearnerState,
    buildLearnerState,
    isNewLearner,
    isLearning,
    isReturning,
    startOnboarding,
    completeStartingSelection,
    completeDiagnostic
} from "./learner-state-engine.js";


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

        pass(message);

    }
    else {

        fail(message);
    }
}


/* ============================================================
   Header
   ============================================================ */

console.log("");

console.log(
    "============================================"
);

console.log(
    " STEP 18 — LEARNER STATE TESTS"
);

console.log(
    "============================================"
);

console.log("");



/* ============================================================
   TEST 1 — Empty Progress
   ============================================================ */

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 1 — First-Time User"
);

console.log(
    "--------------------------------------------"
);


const emptyProgress = {

    studentId:
        "student-new",

    topics: {}
};


assert(
    hasProgressEvidence(
        emptyProgress
    ) === false,
    "New student has no evidence"
);


const newState =
    determineLearnerState(
        emptyProgress
    );


assert(
    newState === STATES.NEW,
    "New student detected as NEW"
);


assert(
    isNewLearner({
        state: newState
    }),
    "NEW state helper works"
);



/* ============================================================
   TEST 2 — Topic Exists But No Evidence
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 2 — Empty Topic Does Not Count"
);

console.log(
    "--------------------------------------------"
);


const emptyTopicProgress = {

    studentId:
        "student-empty",

    topics: {

        percentage: {

            attempts: 0,

            timeSpentSeconds: 0,

            evidenceCount: 0
        }
    }
};


assert(
    hasProgressEvidence(
        emptyTopicProgress
    ) === false,
    "Topic without evidence remains NEW"
);


assert(
    determineLearnerState(
        emptyTopicProgress
    ) === STATES.NEW,
    "Empty topic does not create false learning state"
);



/* ============================================================
   TEST 3 — First Question
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 3 — First Learning Evidence"
);

console.log(
    "--------------------------------------------"
);


const firstAttempt = {

    studentId:
        "student-learning",

    topics: {

        percentage: {

            attempts: 1,

            timeSpentSeconds: 60,

            evidenceCount: 1
        }
    }
};


assert(
    hasProgressEvidence(
        firstAttempt
    ),
    "First question creates evidence"
);


const learningState =
    determineLearnerState(
        firstAttempt
    );


assert(
    learningState === STATES.LEARNING,
    "First learning activity creates LEARNING state"
);


assert(
    isLearning({
        state: learningState
    }),
    "LEARNING state helper works"
);



/* ============================================================
   TEST 4 — Returning Student
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 4 — Returning Learner"
);

console.log(
    "--------------------------------------------"
);


const returningProgress = {

    studentId:
        "student-returning",

    topics: {

        percentage: {

            attempts: 10,

            timeSpentSeconds: 600,

            evidenceCount: 10
        },

        fractions: {

            attempts: 8,

            timeSpentSeconds: 500,

            evidenceCount: 8
        }
    }
};


const returningState =
    determineLearnerState(
        returningProgress
    );


assert(
    returningState ===
        STATES.RETURNING,
    "Established learner detected as RETURNING"
);


assert(
    isReturning({
        state: returningState
    }),
    "RETURNING state helper works"
);



/* ============================================================
   TEST 5 — Build State
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 5 — Build Learner State"
);

console.log(
    "--------------------------------------------"
);


const builtState =
    buildLearnerState(
        firstAttempt,
        {
            selectedExam:
                "ssc",

            startingPoint:
                "percentage"
        }
    );


assert(
    builtState.studentId ===
        "student-learning",
    "Student ID preserved"
);


assert(
    builtState.state ===
        STATES.LEARNING,
    "Learner state calculated"
);


assert(
    builtState.hasEvidence ===
        true,
    "Evidence flag calculated"
);


assert(
    builtState.selectedExam ===
        "ssc",
    "Selected exam preserved"
);


assert(
    builtState.startingPoint ===
        "percentage",
    "Starting point preserved"
);



/* ============================================================
   TEST 6 — Onboarding
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 6 — Onboarding State"
);

console.log(
    "--------------------------------------------"
);


const onboarding =
    startOnboarding(
        {
            state:
                STATES.NEW,

            hasEvidence:
                false
        }
    );


assert(
    onboarding.state ===
        STATES.ONBOARDING,
    "NEW → ONBOARDING transition works"
);



/* ============================================================
   TEST 7 — Starting Point
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 7 — Foundation / Starting Point"
);

console.log(
    "--------------------------------------------"
);


const selectedStart =
    completeStartingSelection(
        onboarding,
        {
            selectedExam:
                "ssc",

            startingPoint:
                "number-system"
        }
    );


assert(
    selectedStart.state ===
        STATES.LEARNING,
    "Starting selection creates LEARNING state"
);


assert(
    selectedStart.selectedExam ===
        "ssc",
    "Exam selection preserved"
);


assert(
    selectedStart.startingPoint ===
        "number-system",
    "Starting point preserved"
);


assert(
    selectedStart.hasEvidence ===
        false,
    "Starting selection does not fake evidence"
);



/* ============================================================
   TEST 8 — Diagnostic
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 8 — Diagnostic Completion"
);

console.log(
    "--------------------------------------------"
);


const diagnostic =
    completeDiagnostic(
        onboarding,
        {
            selectedExam:
                "ssc",

            startingPoint:
                "percentage"
        }
    );


assert(
    diagnostic.state ===
        STATES.LEARNING,
    "Diagnostic creates LEARNING state"
);


assert(
    diagnostic.hasEvidence ===
        true,
    "Diagnostic creates evidence state"
);


assert(
    diagnostic.diagnosticCompleted ===
        true,
    "Diagnostic completion recorded"
);


assert(
    diagnostic.startingPoint ===
        "percentage",
    "Diagnostic starting point preserved"
);



/* ============================================================
   TEST 9 — No Mutation
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 9 — Immutable State Updates"
);

console.log(
    "--------------------------------------------"
);


const original = {

    state:
        STATES.NEW,

    hasEvidence:
        false
};


const updated =
    startOnboarding(
        original
    );


assert(
    original.state ===
        STATES.NEW,
    "Original state remains unchanged"
);


assert(
    updated.state ===
        STATES.ONBOARDING,
    "Updated state contains new state"
);



/* ============================================================
   FINAL
   ============================================================ */

console.log("");

console.log(
    "============================================"
);

console.log(
    " STEP 18 TEST SUMMARY"
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
        "✓ ALL LEARNER STATE TESTS PASSED"
    );

    console.log(
        "✓ STEP 18 COMPLETE"
    );

}
else {

    console.log(
        "✗ STEP 18 FAILED — CHECK ERRORS ABOVE"
    );

    process.exitCode = 1;
}

console.log("");

console.log(
    "============================================"
);

console.log("");
