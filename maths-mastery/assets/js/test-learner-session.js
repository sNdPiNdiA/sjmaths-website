import {
    LearnerSessionRepository,
    SESSION_VERSION
} from "./learner-session-repository.js";

import LearnerSessionManager
    from "./learner-session-manager.js";

import {
    createNewLearnerFlow,
    startOnboarding,
    selectExam,
    prepareDiagnostic,
    completeDiagnostic,
    applyLearningResult
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
        },


        corrupt(
            key,
            value
        ) {

            data.set(
                key,
                value
            );
        }
    };
}


console.log("");

console.log(
    "============================================"
);

console.log(
    " STEP 23 — LEARNER SESSION TESTS"
);

console.log(
    "============================================"
);

console.log("");


/* ============================================================
   TEST 1 — Repository Creation
   ============================================================ */

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 1 — Repository Creation"
);

console.log(
    "--------------------------------------------"
);


const storage =
    createMemoryStorage();


const repository =
    new LearnerSessionRepository(
        storage
    );


assert(
    repository !==
        null,
    "Session repository created"
);


assert(
    repository.exists() ===
        false,
    "New repository has no session"
);



/* ============================================================
   TEST 2 — New User Persistence
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 2 — New User Persistence"
);

console.log(
    "--------------------------------------------"
);


let flow =
    createNewLearnerFlow(
        "student-001"
    );


repository.create(
    flow
);


assert(
    repository.exists(),
    "New learner session exists"
);


const restoredNew =
    repository.loadFlow();


assert(
    restoredNew.studentId ===
        "student-001",
    "Student ID restored"
);


assert(
    restoredNew.learnerState ===
        "NEW",
    "NEW state restored"
);


assert(
    restoredNew.hasEvidence ===
        false,
    "New user evidence state restored"
);



/* ============================================================
   TEST 3 — Onboarding Persistence
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 3 — Onboarding Persistence"
);

console.log(
    "--------------------------------------------"
);


flow =
    startOnboarding(
        flow
    );


flow =
    selectExam(
        flow,
        "ssc"
    );


repository.save(
    flow
);


const restoredOnboarding =
    repository.loadFlow();


assert(
    restoredOnboarding.learnerState ===
        "ONBOARDING",
    "Onboarding state restored"
);


assert(
    restoredOnboarding
        .onboarding
        .selectedExam ===
        "ssc",
    "Selected exam restored"
);


assert(
    restoredOnboarding
        .onboarding
        .status ===
        "in-progress",
    "Onboarding status restored"
);



/* ============================================================
   TEST 4 — Diagnostic Persistence
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 4 — Diagnostic Persistence"
);

console.log(
    "--------------------------------------------"
);


flow =
    prepareDiagnostic(
        flow
    );


repository.save(
    flow
);


const restoredDiagnostic =
    repository.loadFlow();


assert(
    restoredDiagnostic.learnerState ===
        "DIAGNOSTIC",
    "Diagnostic state restored"
);


assert(
    restoredDiagnostic
        .diagnostic
        .status ===
        "in-progress",
    "Diagnostic status restored"
);


assert(
    restoredDiagnostic
        .onboarding
        .route ===
        "diagnostic",
    "Diagnostic route restored"
);



/* ============================================================
   TEST 5 — Completed Diagnostic Persistence
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 5 — Completed Diagnostic"
);

console.log(
    "--------------------------------------------"
);


flow =
    completeDiagnostic(
        flow,
        {

            startingPoint:
                "fractions",

            questionCount:
                10,

            completedAt:
                "2026-08-13T10:00:00.000Z"
        }
    );


repository.save(
    flow
);


const restoredLearning =
    repository.loadFlow();


assert(
    restoredLearning.learnerState ===
        "LEARNING",
    "Learning state restored after diagnostic"
);


assert(
    restoredLearning
        .diagnostic
        .completed ===
        true,
    "Diagnostic completion restored"
);


assert(
    restoredLearning
        .learning
        .currentTopic ===
        "fractions",
    "Diagnostic starting topic restored"
);


assert(
    restoredLearning
        .hasEvidence ===
        true,
    "Diagnostic evidence state restored"
);



/* ============================================================
   TEST 6 — Learning Progress Persistence
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 6 — Learning Progress Persistence"
);

console.log(
    "--------------------------------------------"
);


flow =
    applyLearningResult(
        flow,
        {

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
        }
    );


repository.save(
    flow
);


const restoredProgress =
    repository.loadFlow();


assert(
    restoredProgress
        .learning
        .mastery ===
        72,
    "Mastery restored"
);


assert(
    restoredProgress
        .learning
        .weakSkills
        .includes(
            "fraction-comparison"
        ),
    "Weak skill restored"
);


assert(
    restoredProgress
        .learning
        .nextTopic ===
        "percentage",
    "Next topic restored"
);



/* ============================================================
   TEST 7 — Session Metadata
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 7 — Session Metadata"
);

console.log(
    "--------------------------------------------"
);


const session =
    repository.load();


assert(
    session.sessionVersion ===
        SESSION_VERSION,
    "Session version stored"
);


assert(
    session.studentId ===
        "student-001",
    "Session student ID stored"
);


assert(
    typeof session.savedAt ===
        "string",
    "Saved timestamp stored"
);


assert(
    session.learnerFlow !==
        null,
    "Learner flow stored inside session"
);



/* ============================================================
   TEST 8 — Corrupt Storage Recovery
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 8 — Corrupt Storage Recovery"
);

console.log(
    "--------------------------------------------"
);


storage.corrupt(
    repository.key,
    "{ INVALID JSON"
);


const corruptResult =
    repository.load();


assert(
    corruptResult ===
        null,
    "Corrupt session safely returns null"
);


assert(
    repository.exists(),
    "Corrupt storage does not crash repository"
);



/* ============================================================
   TEST 9 — Invalid Session Rejection
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 9 — Invalid Session Rejection"
);

console.log(
    "--------------------------------------------"
);


storage.corrupt(
    repository.key,

    JSON.stringify({

        sessionVersion:
            SESSION_VERSION,

        studentId:
            "student-001",

        learnerFlow:
            null,

        savedAt:
            new Date().toISOString()
    })
);


assert(
    repository.load() ===
        null,
    "Invalid session is rejected"
);



/* ============================================================
   TEST 10 — Student Isolation
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 10 — Student Isolation"
);

console.log(
    "--------------------------------------------"
);


const storageA =
    createMemoryStorage();


const storageB =
    createMemoryStorage();


const repoA =
    new LearnerSessionRepository(
        storageA
    );


const repoB =
    new LearnerSessionRepository(
        storageB
    );


repoA.create(
    createNewLearnerFlow(
        "student-A"
    )
);


repoB.create(
    createNewLearnerFlow(
        "student-B"
    )
);


assert(
    repoA.loadFlow().studentId ===
        "student-A",
    "Student A session isolated"
);


assert(
    repoB.loadFlow().studentId ===
        "student-B",
    "Student B session isolated"
);



/* ============================================================
   TEST 11 — Clear Session
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 11 — Clear Session"
);

console.log(
    "--------------------------------------------"
);


repoA.clear();


assert(
    repoA.exists() ===
        false,
    "Session cleared"
);


assert(
    repoA.load() ===
        null,
    "Cleared session cannot be restored"
);



/* ============================================================
   TEST 12 — Session Manager
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 12 — Session Manager"
);

console.log(
    "--------------------------------------------"
);


const managerStorage =
    createMemoryStorage();


const manager =
    new LearnerSessionManager(
        managerStorage
    );


const managerFlow =
    createNewLearnerFlow(
        "student-manager"
    );


manager.start(
    managerFlow
);


assert(
    manager.hasSession(),
    "Manager detects active session"
);


const managerRestored =
    manager.restore();


assert(
    managerRestored.studentId ===
        "student-manager",
    "Manager restores learner flow"
);


manager.clear();


assert(
    manager.hasSession() ===
        false,
    "Manager clears session"
);



/* ============================================================
   TEST 13 — Immutable Persistence
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 13 — Immutable Persistence"
);

console.log(
    "--------------------------------------------"
);


const immutableStorage =
    createMemoryStorage();


const immutableRepo =
    new LearnerSessionRepository(
        immutableStorage
    );


const immutableFlow =
    createNewLearnerFlow(
        "student-immutable"
    );


immutableRepo.create(
    immutableFlow
);


const restoredImmutable =
    immutableRepo.loadFlow();


restoredImmutable
    .onboarding
    .status =
        "changed-locally";


const restoredAgain =
    immutableRepo.loadFlow();


assert(
    restoredAgain
        .onboarding
        .status !==
        "changed-locally",
    "Loaded session is protected from local mutation"
);



/* ============================================================
   TEST 14 — Full Reload Simulation
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 14 — Full Reload Simulation"
);

console.log(
    "--------------------------------------------"
);


const reloadStorage =
    createMemoryStorage();


const firstRepository =
    new LearnerSessionRepository(
        reloadStorage
    );


let reloadFlow =
    createNewLearnerFlow(
        "student-reload"
    );


reloadFlow =
    startOnboarding(
        reloadFlow
    );


reloadFlow =
    selectExam(
        reloadFlow,
        "ssc"
    );


reloadFlow =
    prepareDiagnostic(
        reloadFlow
    );


firstRepository.save(
    reloadFlow
);


/*
 * Simulate browser/application reload
 * by creating a completely new repository
 * against the same storage.
 */

const secondRepository =
    new LearnerSessionRepository(
        reloadStorage
    );


const afterReload =
    secondRepository.loadFlow();


assert(
    afterReload.learnerState ===
        "DIAGNOSTIC",
    "Learner state survives reload"
);


assert(
    afterReload
        .onboarding
        .selectedExam ===
        "ssc",
    "Exam survives reload"
);


assert(
    afterReload
        .onboarding
        .route ===
        "diagnostic",
    "Route survives reload"
);



/* ============================================================
   TEST 15 — Complete Returning Session
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 15 — Returning Session"
);

console.log(
    "--------------------------------------------"
);


reloadFlow =
    completeDiagnostic(
        reloadFlow,
        {

            startingPoint:
                "percentage",

            questionCount:
                10,

            completedAt:
                "2026-08-13T11:00:00.000Z"
        }
    );


reloadFlow =
    applyLearningResult(
        reloadFlow,
        {

            topicId:
                "percentage",

            mastery:
                78,

            weakSkills:
                [
                    "reverse-percentage"
                ],

            nextTopic:
                "profit-loss"
        }
    );


firstRepository.save(
    reloadFlow
);


/*
 * Simulate another complete reload.
 */

const returningRepository =
    new LearnerSessionRepository(
        reloadStorage
    );


const returningFlow =
    returningRepository.loadFlow();


assert(
    returningFlow.learnerState ===
        "LEARNING",
    "Returning learner state survives reload"
);


assert(
    returningFlow
        .learning
        .currentTopic ===
        "percentage",
    "Current topic survives reload"
);


assert(
    returningFlow
        .learning
        .nextTopic ===
        "profit-loss",
    "Recommendation survives reload"
);


assert(
    returningFlow
        .learning
        .mastery ===
        78,
    "Mastery survives reload"
);


assert(
    returningFlow
        .learning
        .weakSkills
        .includes(
            "reverse-percentage"
        ),
    "Weak skill survives reload"
);



/* ============================================================
   FINAL
   ============================================================ */

console.log("");

console.log(
    "============================================"
);

console.log(
    " STEP 23 TEST SUMMARY"
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
        "✓ ALL LEARNER SESSION TESTS PASSED"
    );

    console.log(
        "✓ STEP 23 COMPLETE"
    );

}
else {

    console.log(
        "✗ STEP 23 FAILED — CHECK ERRORS ABOVE"
    );

    process.exitCode = 1;
}

console.log("");

console.log(
    "============================================"
);

console.log("");
