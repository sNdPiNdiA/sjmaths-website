import MathsMasteryApplication
    from "./maths-mastery-application.js";


import {
    LearnerSessionRepository
} from "./learner-session-repository.js";


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

    if (
        condition
    ) {

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


/* ============================================================
   Memory Storage
   ============================================================ */

function createMemoryStorage() {

    const data =
        new Map();


    return {

        getItem(
            key
        ) {

            return data.has(
                key
            )
                ? data.get(
                    key
                )
                : null;
        },


        setItem(
            key,
            value
        ) {

            data.set(
                key,
                String(
                    value
                )
            );
        },


        removeItem(
            key
        ) {

            data.delete(
                key
            );
        }
    };
}


console.log("");

console.log(
    "============================================"
);

console.log(
    " STEP 24 — APPLICATION CONTROLLER TESTS"
);

console.log(
    "============================================"
);

console.log("");


/* ============================================================
   TEST 1 — Application Creation
   ============================================================ */

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 1 — Application Creation"
);

console.log(
    "--------------------------------------------"
);


const storage =
    createMemoryStorage();


const sessionRepository =
    new LearnerSessionRepository(
        storage
    );


const app =
    new MathsMasteryApplication({

        sessionRepository

    });


assert(
    app !==
        null,
    "Application controller created"
);


assert(
    app.hasSession() ===
        false,
    "Application starts without session"
);



/* ============================================================
   TEST 2 — First-Time User
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 2 — First-Time User"
);

console.log(
    "--------------------------------------------"
);


let state =
    app.start(
        "student-001"
    );


assert(
    state.studentId ===
        "student-001",
    "Student ID initialized"
);


assert(
    state.learnerState ===
        "NEW",
    "First-time user starts as NEW"
);


assert(
    state.hasEvidence ===
        false,
    "First-time user has no evidence"
);


assert(
    app.hasSession(),
    "First-time session persisted"
);



/* ============================================================
   TEST 3 — Begin Onboarding
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 3 — Begin Onboarding"
);

console.log(
    "--------------------------------------------"
);


state =
    app.beginOnboarding();


assert(
    state.learnerState ===
        "ONBOARDING",
    "Application enters onboarding"
);


assert(
    state.flow
        .onboarding
        .status ===
        "in-progress",
    "Onboarding status persisted"
);



/* ============================================================
   TEST 4 — Exam Selection
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 4 — Exam Selection"
);

console.log(
    "--------------------------------------------"
);


state =
    app.selectExam(
        "ssc"
    );


assert(
    state.flow
        .onboarding
        .selectedExam ===
        "ssc",
    "SSC exam selected"
);



/* ============================================================
   TEST 5 — Foundation Route
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 5 — Foundation Route"
);

console.log(
    "--------------------------------------------"
);


state =
    app.chooseFoundation(
        "number-system"
    );


assert(
    state.learnerState ===
        "LEARNING",
    "Foundation route enters learning"
);


assert(
    state.flow
        .learning
        .currentTopic ===
        "number-system",
    "Foundation starts at Number System"
);


assert(
    state.hasEvidence ===
        false,
    "Foundation route does not create fake evidence"
);



/* ============================================================
   TEST 6 — Reload Foundation User
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 6 — Reload Foundation User"
);

console.log(
    "--------------------------------------------"
);


const reloadedFoundationApp =
    new MathsMasteryApplication({

        sessionRepository:
            new LearnerSessionRepository(
                storage
            )

    });


const restoredFoundation =
    reloadedFoundationApp
        .restore();


assert(
    restoredFoundation
        .learnerState ===
        "LEARNING",
    "Foundation learning state survives reload"
);


assert(
    restoredFoundation
        .flow
        .learning
        .currentTopic ===
        "number-system",
    "Foundation topic survives reload"
);



/* ============================================================
   TEST 7 — Diagnostic User
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 7 — Diagnostic User"
);

console.log(
    "--------------------------------------------"
);


const diagnosticStorage =
    createMemoryStorage();


const diagnosticApp =
    new MathsMasteryApplication({

        sessionRepository:
            new LearnerSessionRepository(
                diagnosticStorage
            )

    });


diagnosticApp.start(
    "student-diagnostic"
);


diagnosticApp.beginOnboarding();


diagnosticApp.selectExam(
    "ssc"
);


state =
    diagnosticApp.startDiagnostic();


assert(
    state.learnerState ===
        "DIAGNOSTIC",
    "Diagnostic state entered"
);


assert(
    state.flow
        .diagnostic
        .status ===
        "in-progress",
    "Diagnostic status is in progress"
);



/* ============================================================
   TEST 8 — Complete Diagnostic
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 8 — Complete Diagnostic"
);

console.log(
    "--------------------------------------------"
);


state =
    diagnosticApp.completeDiagnostic({

        startingPoint:
            "fractions",

        questionCount:
            10,

        completedAt:
            "2026-08-13T12:00:00.000Z"

    });


assert(
    state.learnerState ===
        "LEARNING",
    "Diagnostic completion enters learning"
);


assert(
    state.flow
        .learning
        .currentTopic ===
        "fractions",
    "Diagnostic starting point becomes current topic"
);


assert(
    state.hasEvidence ===
        true,
    "Diagnostic creates evidence state"
);



/* ============================================================
   TEST 9 — Learning Result
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 9 — Learning Result"
);

console.log(
    "--------------------------------------------"
);


state =
    diagnosticApp.recordLearningResult({

        topicId:
            "fractions",

        mastery:
            72,

        weakSkills:
            [
                "fraction-comparison"
            ],

        nextTopic:
            "percentage"

    });


assert(
    state.flow
        .learning
        .mastery ===
        72,
    "Mastery reaches application state"
);


assert(
    state.flow
        .learning
        .weakSkills
        .includes(
            "fraction-comparison"
        ),
    "Weak skill reaches application state"
);


assert(
    state.flow
        .learning
        .nextTopic ===
        "percentage",
    "Next topic reaches application state"
);



/* ============================================================
   TEST 10 — Recommendation
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 10 — Recommendation"
);

console.log(
    "--------------------------------------------"
);


state =
    diagnosticApp.setRecommendation({

        topicId:
            "percentage",

        score:
            91,

        reason:
            "Next recommended topic"

    });


assert(
    state.flow
        .learning
        .nextTopic ===
        "percentage",
    "Recommendation becomes next topic"
);


assert(
    state.recommendation
        .topicId ===
        "percentage",
    "Recommendation stored"
);



/* ============================================================
   TEST 11 — Full Reload
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 11 — Full Reload"
);

console.log(
    "--------------------------------------------"
);


const reloadedDiagnosticApp =
    new MathsMasteryApplication({

        sessionRepository:
            new LearnerSessionRepository(
                diagnosticStorage
            )

    });


const reloadedState =
    reloadedDiagnosticApp
        .restore();


assert(
    reloadedState
        .learnerState ===
        "LEARNING",
    "Learning state survives complete reload"
);


assert(
    reloadedState
        .flow
        .learning
        .currentTopic ===
        "fractions",
    "Current topic survives reload"
);


assert(
    reloadedState
        .flow
        .learning
        .nextTopic ===
        "percentage",
    "Next topic survives reload"
);



/* ============================================================
   TEST 12 — Dashboard
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 12 — Dashboard"
);

console.log(
    "--------------------------------------------"
);


const dashboard =
    reloadedDiagnosticApp
        .getDashboard();


assert(
    dashboard !==
        null,
    "Dashboard state available"
);


assert(
    dashboard.mode ===
        "learning",
    "Learning dashboard returned"
);



/* ============================================================
   TEST 13 — Current / Next Topic
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 13 — Current / Next Topic"
);

console.log(
    "--------------------------------------------"
);


assert(
    reloadedDiagnosticApp
        .getCurrentTopic() ===
        "fractions",
    "Current topic API works"
);


assert(
    reloadedDiagnosticApp
        .getNextTopic() ===
        "percentage",
    "Next topic API works"
);


assert(
    reloadedDiagnosticApp
        .getLearnerState() ===
        "LEARNING",
    "Learner state API works"
);



/* ============================================================
   TEST 14 — Clear Session
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 14 — Clear Session"
);

console.log(
    "--------------------------------------------"
);


reloadedDiagnosticApp
    .clearSession();


assert(
    reloadedDiagnosticApp
        .hasSession() ===
        false,
    "Application session cleared"
);


assert(
    reloadedDiagnosticApp
        .getState() ===
        null,
    "Application state cleared"
);



/* ============================================================
   TEST 15 — Full First-Time Journey
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 15 — Full First-Time Journey"
);

console.log(
    "--------------------------------------------"
);


const journeyStorage =
    createMemoryStorage();


const journeyApp =
    new MathsMasteryApplication({

        sessionRepository:
            new LearnerSessionRepository(
                journeyStorage
            )

    });


let journey =
    journeyApp.start(
        "student-journey"
    );


assert(
    journey.learnerState ===
        "NEW",
    "Journey begins NEW"
);


journey =
    journeyApp.beginOnboarding();


journey =
    journeyApp.selectExam(
        "ssc"
    );


journey =
    journeyApp.startDiagnostic();


assert(
    journey.learnerState ===
        "DIAGNOSTIC",
    "Journey reaches diagnostic"
);


journey =
    journeyApp.completeDiagnostic({

        startingPoint:
            "fractions",

        questionCount:
            10,

        completedAt:
            "2026-08-13T13:00:00.000Z"

    });


journey =
    journeyApp.recordLearningResult({

        topicId:
            "fractions",

        mastery:
            75,

        weakSkills:
            [
                "fraction-comparison"
            ],

        nextTopic:
            "percentage"

    });


journey =
    journeyApp.setRecommendation({

        topicId:
            "percentage",

        score:
            92

    });


assert(
    journey.learnerState ===
        "LEARNING",
    "Complete journey reaches LEARNING"
);


assert(
    journey.flow
        .onboarding
        .selectedExam ===
        "ssc",
    "Exam survives complete journey"
);


assert(
    journey.flow
        .learning
        .currentTopic ===
        "fractions",
    "Starting topic survives complete journey"
);


assert(
    journey.flow
        .learning
        .nextTopic ===
        "percentage",
    "Recommendation survives complete journey"
);


assert(
    journey.hasEvidence ===
        true,
    "Evidence state survives complete journey"
);



/* ============================================================
   TEST 16 — Missing Session
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 16 — Missing Session"
);

console.log(
    "--------------------------------------------"
);


const emptyApp =
    new MathsMasteryApplication({

        sessionRepository:
            new LearnerSessionRepository(
                createMemoryStorage()
            )

    });


assert(
    emptyApp.restore() ===
        null,
    "Missing session returns null"
);



/* ============================================================
   FINAL
   ============================================================ */

console.log("");

console.log(
    "============================================"
);

console.log(
    " STEP 24 TEST SUMMARY"
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
        "✓ ALL APPLICATION CONTROLLER TESTS PASSED"
    );

    console.log(
        "✓ STEP 24 COMPLETE"
    );

}
else {

    console.log(
        "✗ STEP 24 FAILED — CHECK ERRORS ABOVE"
    );

    process.exitCode = 1;
}

console.log("");

console.log(
    "============================================"
);

console.log("");
