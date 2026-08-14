import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

import {
    createEmptyProgress,
    recordQuestionAttempt,
    recordMiniTestAttempt,
    getEvidenceSummary,
    getSkillEvidence,
    validateProgressEvidence
} from "./progress-engine.js";


/* ============================================================
   Paths
   ============================================================ */

const __filename =
    fileURLToPath(import.meta.url);

const __dirname =
    path.dirname(__filename);

const masteryRoot =
    path.resolve(
        __dirname,
        "../.."
    );


const progressPath =
    path.join(
        masteryRoot,
        "data",
        "progress",
        "progress-demo.json"
    );


/* ============================================================
   BOM-safe loader
   ============================================================ */

function loadJson(filePath) {

    let text =
        fs.readFileSync(
            filePath,
            "utf8"
        );


    if (
        text.length > 0 &&
        text.charCodeAt(0) === 0xFEFF
    ) {

        text =
            text.slice(1);
    }


    return JSON.parse(text);
}


/* ============================================================
   Test helpers
   ============================================================ */

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


function section(number, title) {

    console.log("");

    console.log(
        "--------------------------------------------"
    );

    console.log(
        `TEST ${number} — ${title}`
    );

    console.log(
        "--------------------------------------------"
    );
}


/* ============================================================
   TEST 1
   Create empty progress
   ============================================================ */

section(
    1,
    "Create Empty Progress"
);


const empty =
    createEmptyProgress(
        "test-student"
    );


if (
    empty.studentId ===
        "test-student"
) {

    pass(
        "Empty progress contains student ID"
    );

}
else {

    fail(
        "Empty progress student ID missing"
    );
}


if (
    empty.topics &&
    typeof empty.topics ===
        "object"
) {

    pass(
        "Empty progress contains topics object"
    );

}
else {

    fail(
        "Empty progress topics object missing"
    );
}


/* ============================================================
   TEST 2
   Record correct question
   ============================================================ */

section(
    2,
    "Record Correct Question"
);


let progress =
    createEmptyProgress(
        "test-student"
    );


progress =
    recordQuestionAttempt(
        progress,
        {

            topicId:
                "percentage",

            questionId:
                "percentage-p-001",

            conceptId:
                "percentage-basics",

            skillIds: [
                "percentage-calculation"
            ],

            correct:
                true,

            timeSpentSeconds:
                30,

            attemptedAt:
                "2026-08-13T10:00:00.000Z"
        }
    );


const topic =
    progress.topics.percentage;


if (
    topic.evidence.attempts === 1 &&
    topic.evidence.correct === 1
) {

    pass(
        "Correct answer recorded at topic level"
    );

}
else {

    fail(
        "Correct answer topic evidence incorrect"
    );
}


if (
    topic.concepts[
        "percentage-basics"
    ].evidence.correct === 1
) {

    pass(
        "Correct answer recorded at concept level"
    );

}
else {

    fail(
        "Correct answer concept evidence incorrect"
    );
}


if (
    topic.skills[
        "percentage-calculation"
    ].evidence.correct === 1
) {

    pass(
        "Correct answer recorded at skill level"
    );

}
else {

    fail(
        "Correct answer skill evidence incorrect"
    );
}


/* ============================================================
   TEST 3
   Record incorrect question
   ============================================================ */

section(
    3,
    "Record Incorrect Question"
);


progress =
    recordQuestionAttempt(
        progress,
        {

            topicId:
                "percentage",

            questionId:
                "percentage-p-002",

            conceptId:
                "percentage-basics",

            skillIds: [
                "percentage-calculation"
            ],

            correct:
                false,

            timeSpentSeconds:
                45,

            attemptedAt:
                "2026-08-13T10:01:00.000Z"
        }
    );


if (
    progress.topics.percentage
        .evidence.incorrect === 1
) {

    pass(
        "Incorrect answer recorded"
    );

}
else {

    fail(
        "Incorrect answer not recorded"
    );
}


if (
    progress.topics.percentage
        .evidence.attempts === 2
) {

    pass(
        "Attempt count incremented correctly"
    );

}
else {

    fail(
        "Attempt count incorrect"
    );
}


/* ============================================================
   TEST 4
   Record skipped question
   ============================================================ */

section(
    4,
    "Record Skipped Question"
);


progress =
    recordQuestionAttempt(
        progress,
        {

            topicId:
                "percentage",

            questionId:
                "percentage-p-003",

            conceptId:
                "percentage-basics",

            skillIds: [
                "percentage-calculation"
            ],

            correct:
                null,

            timeSpentSeconds:
                5,

            attemptedAt:
                "2026-08-13T10:02:00.000Z"
        }
    );


if (
    progress.topics.percentage
        .evidence.skipped === 1
) {

    pass(
        "Skipped answer recorded"
    );

}
else {

    fail(
        "Skipped answer not recorded"
    );
}


/* ============================================================
   TEST 5
   Time accumulation
   ============================================================ */

section(
    5,
    "Time Evidence"
);


const summary =
    getEvidenceSummary(
        progress,
        "percentage"
    );


if (
    summary.timeSpentSeconds === 80
) {

    pass(
        "Time spent accumulated correctly"
    );

}
else {

    fail(
        `Time accumulation incorrect: ${summary.timeSpentSeconds}`
    );
}


/* ============================================================
   TEST 6
   Accuracy summary
   ============================================================ */

section(
    6,
    "Accuracy Calculation"
);


if (
    summary.accuracy ===
        33.33
) {

    pass(
        "Topic accuracy calculated correctly"
    );

}
else {

    fail(
        `Topic accuracy incorrect: ${summary.accuracy}`
    );
}


/* ============================================================
   TEST 7
   Skill evidence
   ============================================================ */

section(
    7,
    "Skill Evidence"
);


const skill =
    getSkillEvidence(
        progress,
        "percentage",
        "percentage-calculation"
    );


if (
    skill.attempts === 3 &&
    skill.correct === 1 &&
    skill.incorrect === 1 &&
    skill.skipped === 1
) {

    pass(
        "Skill evidence correctly accumulated"
    );

}
else {

    fail(
        "Skill evidence accumulation incorrect"
    );
}


/* ============================================================
   TEST 8
   Mini-test attempt
   ============================================================ */

section(
    8,
    "Mini-Test Evidence"
);


progress =
    recordMiniTestAttempt(
        progress,
        {

            topicId:
                "percentage",

            testId:
                "percentage-test-foundation",

            score:
                82,

            accuracy:
                85,

            attemptedAt:
                "2026-08-13T10:05:00.000Z"
        }
    );


const miniTest =
    progress.topics.percentage
        .miniTests[
            "percentage-test-foundation"
        ];


if (
    miniTest.attempts === 1 &&
    miniTest.bestScore === 82 &&
    miniTest.bestAccuracy === 85
) {

    pass(
        "Mini-test attempt recorded"
    );

}
else {

    fail(
        "Mini-test evidence incorrect"
    );
}


/* ============================================================
   TEST 9
   Better mini-test score updates best
   ============================================================ */

section(
    9,
    "Mini-Test Best Score"
);


progress =
    recordMiniTestAttempt(
        progress,
        {

            topicId:
                "percentage",

            testId:
                "percentage-test-foundation",

            score:
                91,

            accuracy:
                93,

            attemptedAt:
                "2026-08-13T10:10:00.000Z"
        }
    );


const updatedTest =
    progress.topics.percentage
        .miniTests[
            "percentage-test-foundation"
        ];


if (
    updatedTest.attempts === 2 &&
    updatedTest.bestScore === 91 &&
    updatedTest.bestAccuracy === 93 &&
    updatedTest.lastScore === 91
) {

    pass(
        "Mini-test best score updated correctly"
    );

}
else {

    fail(
        "Mini-test best score logic incorrect"
    );
}


/* ============================================================
   TEST 10
   Evidence integrity
   ============================================================ */

section(
    10,
    "Evidence Integrity"
);


const errors =
    validateProgressEvidence(
        progress
    );


if (
    errors.length === 0
) {

    pass(
        "Progress evidence integrity passed"
    );

}
else {

    fail(
        `Evidence validation failed: ${errors.join("; ")}`
    );
}


/* ============================================================
   TEST 11
   Input validation
   ============================================================ */

section(
    11,
    "Input Validation"
);


let validationPassed =
    false;


try {

    recordQuestionAttempt(
        progress,
        {

            topicId:
                "percentage",

            questionId:
                "invalid-test",

            correct:
                "maybe"
        }
    );

}
catch {

    validationPassed =
        true;
}


if (
    validationPassed
) {

    pass(
        "Invalid question result is rejected"
    );

}
else {

    fail(
        "Invalid question result was accepted"
    );
}


/* ============================================================
   TEST 12
   Original data not mutated
   ============================================================ */

section(
    12,
    "Immutable Update"
);


const original =
    createEmptyProgress(
        "immutable-test"
    );


const updated =
    recordQuestionAttempt(
        original,
        {

            topicId:
                "percentage",

            questionId:
                "percentage-p-001",

            correct:
                true
        }
    );


if (
    Object.keys(
        original.topics
    ).length === 0
) {

    pass(
        "Original progress remains unchanged"
    );

}
else {

    fail(
        "Original progress was mutated"
    );
}


if (
    Object.keys(
        updated.topics
    ).length === 1
) {

    pass(
        "Updated progress contains new evidence"
    );

}
else {

    fail(
        "Updated progress missing evidence"
    );
}


/* ============================================================
   SUMMARY
   ============================================================ */

console.log("");

console.log(
    "============================================"
);

console.log(
    " STEP 13 TEST SUMMARY"
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
        "✓ ALL PROGRESS ENGINE TESTS PASSED"
    );

    console.log(
        "✓ STEP 13 COMPLETE"
    );

}
else {

    console.log(
        "✗ STEP 13 FAILED — REVIEW FAILURES ABOVE"
    );

    process.exitCode = 1;
}

console.log("");

console.log(
    "============================================"
);

console.log("");
