import {
    createEmptyExposure,
    recordQuestionAttempt,
    getQuestionExposure
} from "./knowledge/question-exposure-engine.js";

import {
    QuestionExposureRepository
} from "./question-exposure-repository.js";


/* ============================================================
   Memory Storage
   ============================================================ */

class MemoryStorage {

    constructor() {

        this.data = {};
    }


    getItem(
        key
    ) {

        return Object.prototype.hasOwnProperty.call(
            this.data,
            key
        )
            ? this.data[key]
            : null;
    }


    setItem(
        key,
        value
    ) {

        this.data[key] =
            String(value);
    }


    removeItem(
        key
    ) {

        delete this.data[key];
    }
}


/* ============================================================
   Assertions
   ============================================================ */

function assert(
    condition,
    message
) {

    if (!condition) {

        throw new Error(
            message
        );
    }

    console.log(
        `✓ ${message}`
    );
}


/* ============================================================
   TEST HEADER
   ============================================================ */

console.log("");
console.log(
    "============================================================"
);
console.log(
    " STEP 31.27 — QUESTION EXPOSURE REPOSITORY TESTS"
);
console.log(
    "============================================================"
);


/* ============================================================
   TEST 1 — Repository Creation
   ============================================================ */

console.log("");
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
    new MemoryStorage();

const repository =
    new QuestionExposureRepository({
        storage,
        storageKey:
            "test-question-exposure"
    });

assert(
    repository.isAvailable(),
    "Exposure repository is available"
);

assert(
    !(await repository.exists()),
    "New repository has no exposure"
);


/* ============================================================
   TEST 2 — New Student
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 2 — New Student"
);
console.log(
    "--------------------------------------------"
);

const empty =
    await repository.load(
        "student-a"
    );

assert(
    empty.studentId ===
        "student-a",
    "Student ID restored for new exposure"
);

assert(
    Object.keys(
        empty.questions
    ).length === 0,
    "New exposure contains no questions"
);


/* ============================================================
   TEST 3 — Save Exposure
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 3 — Save Exposure"
);
console.log(
    "--------------------------------------------"
);

const updated =
    recordQuestionAttempt(
        empty,
        {
            questionId:
                "percentage-reverse-001",

            result:
                "correct",

            timeSpentSeconds:
                30,

            attemptedAt:
                "2026-08-13T13:00:00.000Z"
        }
    );

assert(
    getQuestionExposure(
        updated,
        "percentage-reverse-001"
    ) !== null,
    "Question exposure exists"
);

assert(
    await repository.save(
        updated
    ),
    "Exposure saved successfully"
);


/* ============================================================
   TEST 4 — Reload
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 4 — Reload"
);
console.log(
    "--------------------------------------------"
);

const restored =
    await repository.load(
        "student-a"
    );

const restoredRecord =
    getQuestionExposure(
        restored,
        "percentage-reverse-001"
    );

assert(
    restoredRecord !== null,
    "Question exposure survives reload"
);

assert(
    restoredRecord.attemptCount === 1,
    "Attempt count survives reload"
);

assert(
    restoredRecord.correctCount === 1,
    "Correct count survives reload"
);

assert(
    restoredRecord.totalTimeSpentSeconds === 30,
    "Time survives reload"
);


/* ============================================================
   TEST 5 — Immutability
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 5 — Immutability"
);
console.log(
    "--------------------------------------------"
);

restoredRecord.correctCount = 999;

const reloaded =
    await repository.load(
        "student-a"
    );

const reloadedRecord =
    getQuestionExposure(
        reloaded,
        "percentage-reverse-001"
    );

assert(
    reloadedRecord.correctCount === 1,
    "Loaded exposure is protected from local mutation"
);


/* ============================================================
   TEST 6 — Student Isolation
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 6 — Student Isolation"
);
console.log(
    "--------------------------------------------"
);

const storageA =
    new MemoryStorage();

const storageB =
    new MemoryStorage();

const repositoryA =
    new QuestionExposureRepository({
        storage: storageA,
        storageKey:
            "student-a-exposure"
    });

const repositoryB =
    new QuestionExposureRepository({
        storage: storageB,
        storageKey:
            "student-b-exposure"
    });

const exposureA =
    recordQuestionAttempt(
        createEmptyExposure(
            "student-a"
        ),
        {
            questionId:
                "percentage-reverse-001",

            result:
                "correct",

            timeSpentSeconds:
                10,

            attemptedAt:
                "2026-08-13T13:01:00.000Z"
        }
    );

await repositoryA.save(
    exposureA
);

const loadedB =
    await repositoryB.load(
        "student-b"
    );

assert(
    Object.keys(
        loadedB.questions
    ).length === 0,
    "Student B cannot see Student A exposure"
);


/* ============================================================
   TEST 7 — Corrupt Storage
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 7 — Corrupt Storage"
);
console.log(
    "--------------------------------------------"
);

const corruptStorage =
    new MemoryStorage();

corruptStorage.setItem(
    "corrupt",
    "{invalid-json"
);

const corruptRepository =
    new QuestionExposureRepository({
        storage:
            corruptStorage,

        storageKey:
            "corrupt"
    });

const recovered =
    await corruptRepository.load(
        "student-corrupt"
    );

assert(
    recovered.studentId ===
        "student-corrupt",
    "Corrupt storage safely recovers"
);

assert(
    Object.keys(
        recovered.questions
    ).length === 0,
    "Corrupt storage produces empty exposure"
);


/* ============================================================
   TEST 8 — Invalid Exposure Rejection
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 8 — Invalid Exposure"
);
console.log(
    "--------------------------------------------"
);

let rejected =
    false;

try {

    await repository.save({
        invalid:
            true
    });

} catch {

    rejected = true;
}

assert(
    rejected,
    "Invalid exposure is rejected"
);


/* ============================================================
   TEST 9 — Clear
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 9 — Clear"
);
console.log(
    "--------------------------------------------"
);

assert(
    await repository.clear(),
    "Exposure repository cleared"
);

assert(
    !(await repository.exists()),
    "Cleared exposure no longer exists"
);


/* ============================================================
   SUMMARY
   ============================================================ */

console.log("");
console.log(
    "============================================================"
);
console.log(
    " STEP 31.27 TEST SUMMARY"
);
console.log(
    "============================================================"
);

console.log(
    "✓ Repository creation"
);

console.log(
    "✓ New student exposure"
);

console.log(
    "✓ Save / load"
);

console.log(
    "✓ Question history persistence"
);

console.log(
    "✓ Immutable loading"
);

console.log(
    "✓ Student isolation"
);

console.log(
    "✓ Corrupt storage recovery"
);

console.log(
    "✓ Invalid exposure rejection"
);

console.log(
    "✓ Clear"
);

console.log("");
console.log(
    "✓ ALL QUESTION EXPOSURE REPOSITORY TESTS PASSED"
);
console.log(
    "✓ STEP 31.27 COMPLETE"
);
console.log("");
