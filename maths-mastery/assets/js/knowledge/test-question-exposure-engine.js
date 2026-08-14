import {
    createEmptyExposure,
    recordQuestionAttempt,
    getQuestionExposure,
    getQuestionAttemptCount,
    hasBeenAttempted,
    getRecentQuestionIds,
    getExposureSummary,
    getQuestionIdsByResult,
    getWeaklyPerformedQuestions,
    validateExposure
} from "./question-exposure-engine.js";


function assert(
    condition,
    message
) {

    if (
        !condition
    ) {

        throw new Error(
            message
        );
    }


    console.log(
        `✓ ${message}`
    );
}


function clone(
    value
) {

    return JSON.parse(
        JSON.stringify(
            value
        )
    );
}


console.log("");
console.log(
    "============================================"
);
console.log(
    " STEP 29 — QUESTION EXPOSURE TESTS"
);
console.log(
    "============================================"
);
console.log("");


/* ============================================================
   TEST 1 — Empty Exposure
   ============================================================ */

console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 1 — Empty Exposure"
);
console.log(
    "--------------------------------------------"
);


const empty =
    createEmptyExposure(
        "student-001"
    );


assert(
    empty.studentId ===
        "student-001",
    "Student ID stored"
);


assert(
    Object.keys(
        empty.questions
    ).length === 0,
    "New exposure contains no question history"
);


assert(
    validateExposure(
        empty
    ),
    "Empty exposure is valid"
);


/* ============================================================
   TEST 2 — First Correct Attempt
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 2 — First Correct Attempt"
);
console.log(
    "--------------------------------------------"
);


const first =
    recordQuestionAttempt(
        empty,
        {

            questionId:
                "percentage-reverse-001",

            result:
                "correct",

            timeSpentSeconds:
                32,

            attemptedAt:
                "2026-08-13T10:00:00.000Z"

        }
    );


const firstRecord =
    getQuestionExposure(
        first,
        "percentage-reverse-001"
    );


assert(
    firstRecord !== null,
    "First question exposure recorded"
);


assert(
    firstRecord.attemptCount === 1,
    "Attempt count = 1"
);


assert(
    firstRecord.correctCount === 1,
    "Correct count = 1"
);


assert(
    firstRecord.incorrectCount === 0,
    "Incorrect count = 0"
);


assert(
    firstRecord.skippedCount === 0,
    "Skipped count = 0"
);


assert(
    firstRecord.totalTimeSpentSeconds === 32,
    "Time spent recorded"
);


assert(
    firstRecord.lastResult ===
        "correct",
    "Last result recorded"
);


/* ============================================================
   TEST 3 — Incorrect Attempt
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 3 — Incorrect Attempt"
);
console.log(
    "--------------------------------------------"
);


const second =
    recordQuestionAttempt(
        first,
        {

            questionId:
                "percentage-reverse-001",

            result:
                "incorrect",

            timeSpentSeconds:
                18,

            attemptedAt:
                "2026-08-13T10:02:00.000Z"

        }
    );


const secondRecord =
    getQuestionExposure(
        second,
        "percentage-reverse-001"
    );


assert(
    secondRecord.attemptCount === 2,
    "Attempt count incremented"
);


assert(
    secondRecord.correctCount === 1,
    "Correct count preserved"
);


assert(
    secondRecord.incorrectCount === 1,
    "Incorrect count incremented"
);


assert(
    secondRecord.totalTimeSpentSeconds === 50,
    "Time accumulated correctly"
);


assert(
    secondRecord.lastResult ===
        "incorrect",
    "Last result updated"
);


assert(
    secondRecord.consecutiveIncorrect ===
        1,
    "Consecutive incorrect count recorded"
);


/* ============================================================
   TEST 4 — Consecutive Correct
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 4 — Consecutive Correct"
);
console.log(
    "--------------------------------------------"
);


const third =
    recordQuestionAttempt(
        second,
        {

            questionId:
                "percentage-reverse-001",

            result:
                "correct",

            timeSpentSeconds:
                20,

            attemptedAt:
                "2026-08-13T10:04:00.000Z"

        }
    );


const thirdRecord =
    getQuestionExposure(
        third,
        "percentage-reverse-001"
    );


assert(
    thirdRecord.correctCount === 2,
    "Second correct answer recorded"
);


assert(
    thirdRecord.consecutiveCorrect ===
        1,
    "Consecutive correct count restarted correctly"
);


assert(
    thirdRecord.consecutiveIncorrect ===
        0,
    "Consecutive incorrect count reset"
);


/* ============================================================
   TEST 5 — Skipped Attempt
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 5 — Skipped Attempt"
);
console.log(
    "--------------------------------------------"
);


const skipped =
    recordQuestionAttempt(
        third,
        {

            questionId:
                "percentage-reverse-002",

            result:
                "skipped",

            timeSpentSeconds:
                5,

            attemptedAt:
                "2026-08-13T10:05:00.000Z"

        }
    );


const skippedRecord =
    getQuestionExposure(
        skipped,
        "percentage-reverse-002"
    );


assert(
    skippedRecord !== null,
    "Skipped question exposure recorded"
);


assert(
    skippedRecord.skippedCount === 1,
    "Skipped count recorded"
);


assert(
    skippedRecord.lastResult ===
        "skipped",
    "Skipped result recorded"
);


/* ============================================================
   TEST 6 — Attempt Detection
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 6 — Attempt Detection"
);
console.log(
    "--------------------------------------------"
);


assert(
    hasBeenAttempted(
        skipped,
        "percentage-reverse-001"
    ),
    "Attempted question is detected"
);


assert(
    hasBeenAttempted(
        skipped,
        "percentage-reverse-002"
    ),
    "Skipped question counts as exposed"
);


assert(
    !hasBeenAttempted(
        skipped,
        "percentage-reverse-999"
    ),
    "Unknown question is not marked attempted"
);


/* ============================================================
   TEST 7 — Attempt Count API
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 7 — Attempt Count"
);
console.log(
    "--------------------------------------------"
);


assert(
    getQuestionAttemptCount(
        skipped,
        "percentage-reverse-001"
    ) === 3,
    "Question attempt count API works"
);


assert(
    getQuestionAttemptCount(
        skipped,
        "percentage-reverse-002"
    ) === 1,
    "Second question attempt count works"
);


assert(
    getQuestionAttemptCount(
        skipped,
        "unknown-question"
    ) === 0,
    "Unknown question returns zero attempts"
);


/* ============================================================
   TEST 8 — Recent Questions
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 8 — Recent Questions"
);
console.log(
    "--------------------------------------------"
);


const recent =
    getRecentQuestionIds(
        skipped
    );


assert(
    recent.length === 2,
    "Recent question list contains exposed questions"
);


assert(
    recent[0] ===
        "percentage-reverse-002",
    "Most recently attempted question appears first"
);


/* ============================================================
   TEST 9 — Result Queries
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 9 — Result Queries"
);
console.log(
    "--------------------------------------------"
);


const correctIds =
    getQuestionIdsByResult(
        skipped,
        "correct"
    );


assert(
    correctIds.includes(
        "percentage-reverse-001"
    ),
    "Question with final correct result is returned as last-correct"
);


const skippedIds =
    getQuestionIdsByResult(
        skipped,
        "skipped"
    );


assert(
    skippedIds.includes(
        "percentage-reverse-002"
    ),
    "Skipped question can be queried"
);


/* ============================================================
   TEST 10 — Weak Performance
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 10 — Weak Performance"
);
console.log(
    "--------------------------------------------"
);


const weak =
    getWeaklyPerformedQuestions(
        skipped
    );


assert(
    Array.isArray(
        weak
    ),
    "Weak question list returned"
);


assert(
    weak.some(
        record =>
            record.questionId ===
            "percentage-reverse-002"
    ),
    "Question with no correct answers is identified as weakly performed"
);


/* ============================================================
   TEST 11 — Summary
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 11 — Exposure Summary"
);
console.log(
    "--------------------------------------------"
);


const summary =
    getExposureSummary(
        skipped
    );


assert(
    summary.uniqueQuestions === 2,
    "Unique question count calculated"
);


assert(
    summary.totalAttempts === 4,
    "Total attempts calculated"
);


assert(
    summary.correctAttempts === 2,
    "Correct attempts calculated"
);


assert(
    summary.incorrectAttempts === 1,
    "Incorrect attempts calculated"
);


assert(
    summary.skippedAttempts === 1,
    "Skipped attempts calculated"
);


assert(
    summary.totalTimeSpentSeconds === 75,
    "Total time calculated"
);


/* ============================================================
   TEST 12 — Invalid Result
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 12 — Invalid Result"
);
console.log(
    "--------------------------------------------"
);


let invalidRejected =
    false;


try {

    recordQuestionAttempt(
        skipped,
        {

            questionId:
                "percentage-reverse-001",

            result:
                "unknown-result",

            timeSpentSeconds:
                10

        }
    );

}
catch {

    invalidRejected =
        true;
}


assert(
    invalidRejected,
    "Invalid result is rejected"
);


/* ============================================================
   TEST 13 — Invalid Time
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 13 — Invalid Time"
);
console.log(
    "--------------------------------------------"
);


let invalidTimeRejected =
    false;


try {

    recordQuestionAttempt(
        skipped,
        {

            questionId:
                "percentage-reverse-001",

            result:
                "correct",

            timeSpentSeconds:
                -10

        }
    );

}
catch {

    invalidTimeRejected =
        true;
}


assert(
    invalidTimeRejected,
    "Negative time is rejected"
);


/* ============================================================
   TEST 14 — Immutable Update
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 14 — Immutable Update"
);
console.log(
    "--------------------------------------------"
);


const before =
    clone(
        skipped
    );


const updated =
    recordQuestionAttempt(
        skipped,
        {

            questionId:
                "percentage-reverse-002",

            result:
                "incorrect",

            timeSpentSeconds:
                12

        }
    );


assert(
    JSON.stringify(
        before
    ) ===
    JSON.stringify(
        skipped
    ),
    "Original exposure remains unchanged"
);


assert(
    updated.questions[
        "percentage-reverse-002"
    ].attemptCount === 2,
    "Updated exposure contains new evidence"
);


/* ============================================================
   TEST 15 — Validation
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 15 — Exposure Integrity"
);
console.log(
    "--------------------------------------------"
);


assert(
    validateExposure(
        updated
    ),
    "Updated exposure passes integrity validation"
);


/* ============================================================
   FINAL
   ============================================================ */

console.log("");
console.log(
    "============================================"
);

console.log(
    " STEP 29 TEST SUMMARY"
);

console.log(
    "============================================"
);

console.log("");

console.log(
    "✓ Attempt tracking works"
);

console.log(
    "✓ Correct / incorrect / skipped tracking works"
);

console.log(
    "✓ Time tracking works"
);

console.log(
    "✓ Consecutive performance tracking works"
);

console.log(
    "✓ Attempt detection works"
);

console.log(
    "✓ Recent exposure tracking works"
);

console.log(
    "✓ Result queries work"
);

console.log(
    "✓ Weak-question detection works"
);

console.log(
    "✓ Exposure summary works"
);

console.log(
    "✓ Invalid input is rejected"
);

console.log(
    "✓ Exposure updates are immutable"
);

console.log(
    "✓ Exposure integrity validation works"
);

console.log("");

console.log(
    "✓ ALL QUESTION EXPOSURE TESTS PASSED"
);

console.log(
    "✓ STEP 29 COMPLETE"
);

console.log("");


