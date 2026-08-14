import {
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
} from "./onboarding-engine.js";


let passed = 0;
let failed = 0;


function pass(message) {

    passed++;

    console.log(
        `✓ ${message}`
    );
}


function fail(message) {

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


console.log("");

console.log(
    "============================================"
);

console.log(
    " STEP 19 — ONBOARDING TESTS"
);

console.log(
    "============================================"
);

console.log("");



/* ============================================================
   TEST 1 — Empty Onboarding
   ============================================================ */

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 1 — Create Empty Onboarding"
);

console.log(
    "--------------------------------------------"
);


const empty =
    createEmptyOnboarding(
        "student-001"
    );


assert(
    empty.studentId ===
        "student-001",
    "Student ID stored"
);


assert(
    empty.status ===
        ONBOARDING_STATUS.NOT_STARTED,
    "Initial status = not-started"
);


assert(
    empty.route === null,
    "Initial route is null"
);


assert(
    empty.selectedExam === null,
    "Initial exam is null"
);


assert(
    empty.startingPoint === null,
    "Initial starting point is null"
);


assert(
    validateOnboarding(
        empty
    ),
    "Empty onboarding is valid"
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


const started =
    startOnboarding(
        empty
    );


assert(
    started.status ===
        ONBOARDING_STATUS.IN_PROGRESS,
    "Onboarding started"
);



/* ============================================================
   TEST 3 — Exam Selection
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 3 — Optional Exam Selection"
);

console.log(
    "--------------------------------------------"
);


const examSelected =
    selectExam(
        started,
        "ssc"
    );


assert(
    examSelected.selectedExam ===
        "ssc",
    "SSC exam selected"
);


const examSkipped =
    selectExam(
        started,
        null
    );


assert(
    examSkipped.selectedExam ===
        null,
    "Exam selection can be skipped"
);



/* ============================================================
   TEST 4 — Diagnostic Route
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 4 — Diagnostic Route"
);

console.log(
    "--------------------------------------------"
);


const diagnostic =
    selectDiagnosticRoute(
        examSelected
    );


assert(
    diagnostic.route ===
        ONBOARDING_ROUTES.DIAGNOSTIC,
    "Diagnostic route selected"
);


assert(
    diagnostic.status ===
        ONBOARDING_STATUS.IN_PROGRESS,
    "Diagnostic remains in progress"
);


assert(
    diagnostic.startingPoint ===
        null,
    "Diagnostic does not invent starting point"
);



/* ============================================================
   TEST 5 — Prepare Diagnostic
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 5 — Prepare Diagnostic"
);

console.log(
    "--------------------------------------------"
);


const prepared =
    prepareDiagnostic(
        examSelected
    );


assert(
    prepared.route ===
        ONBOARDING_ROUTES.DIAGNOSTIC,
    "Prepared diagnostic route is correct"
);


assert(
    prepared.status ===
        ONBOARDING_STATUS.IN_PROGRESS,
    "Prepared diagnostic is in progress"
);



/* ============================================================
   TEST 6 — Foundation Route
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 6 — Foundation Route"
);

console.log(
    "--------------------------------------------"
);


const foundation =
    selectFoundationRoute(
        examSelected
    );


assert(
    foundation.route ===
        ONBOARDING_ROUTES.FOUNDATION,
    "Foundation route selected"
);


assert(
    foundation.startingPoint ===
        "number-system",
    "Foundation starts at Number System"
);


assert(
    foundation.status ===
        ONBOARDING_STATUS.COMPLETED,
    "Foundation onboarding completed"
);


assert(
    isOnboardingComplete(
        foundation
    ),
    "Foundation onboarding completion detected"
);


assert(
    foundation.completedAt !==
        null,
    "Foundation completion timestamp recorded"
);



/* ============================================================
   TEST 7 — Diagnostic Completion
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 7 — Diagnostic Completion"
);

console.log(
    "--------------------------------------------"
);


const completedDiagnostic =
    completeDiagnosticOnboarding(
        diagnostic,
        "percentage"
    );


assert(
    completedDiagnostic.route ===
        ONBOARDING_ROUTES.DIAGNOSTIC,
    "Diagnostic route preserved"
);


assert(
    completedDiagnostic.startingPoint ===
        "percentage",
    "Diagnostic starting point recorded"
);


assert(
    completedDiagnostic.status ===
        ONBOARDING_STATUS.COMPLETED,
    "Diagnostic onboarding completed"
);


assert(
    completedDiagnostic.completedAt !==
        null,
    "Diagnostic completion timestamp recorded"
);


assert(
    isOnboardingComplete(
        completedDiagnostic
    ),
    "Diagnostic completion detected"
);



/* ============================================================
   TEST 8 — Validation
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 8 — Validation"
);

console.log(
    "--------------------------------------------"
);


assert(
    validateOnboarding(
        foundation
    ),
    "Foundation onboarding validates"
);


assert(
    validateOnboarding(
        completedDiagnostic
    ),
    "Diagnostic onboarding validates"
);


assert(
    validateOnboarding(
        diagnostic
    ),
    "In-progress onboarding validates"
);



/* ============================================================
   TEST 9 — Invalid State
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 9 — Invalid State Rejection"
);

console.log(
    "--------------------------------------------"
);


const invalid = {

    version:
        "1.0.0",

    studentId:
        "student-invalid",

    status:
        "something-invalid",

    route:
        null,

    selectedExam:
        null,

    startingPoint:
        null,

    completedAt:
        null
};


assert(
    validateOnboarding(
        invalid
    ) === false,
    "Invalid onboarding status rejected"
);



/* ============================================================
   TEST 10 — Immutable Updates
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 10 — Immutable Updates"
);

console.log(
    "--------------------------------------------"
);


const original = {

    ...empty
};


const changed =
    selectExam(
        original,
        "ssc"
    );


assert(
    original.selectedExam ===
        null,
    "Original onboarding remains unchanged"
);


assert(
    changed.selectedExam ===
        "ssc",
    "Updated onboarding contains selected exam"
);



/* ============================================================
   FINAL
   ============================================================ */

console.log("");

console.log(
    "============================================"
);

console.log(
    " STEP 19 TEST SUMMARY"
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
        "✓ ALL ONBOARDING TESTS PASSED"
    );

    console.log(
        "✓ STEP 19 COMPLETE"
    );

}
else {

    console.log(
        "✗ STEP 19 FAILED — CHECK ERRORS ABOVE"
    );

    process.exitCode = 1;
}

console.log("");

console.log(
    "============================================"
);

console.log("");
