import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

import {
    LearningPipeline
} from "./learning-pipeline.js";

import {
    LocalProgressRepository
} from "./local-progress-repository.js";

import {
    MemoryStorage
} from "./memory-storage.js";


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


/* ============================================================
   JSON loader
   ============================================================ */

function loadJson(
    filePath
) {

    let text =
        fs.readFileSync(
            filePath,
            "utf8"
        );


    if (
        text.length > 0 &&
        text.charCodeAt(0) ===
            0xFEFF
    ) {

        text =
            text.slice(1);
    }


    return JSON.parse(
        text
    );
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


function section(
    number,
    title
) {

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
   Load mastery rules
   ============================================================ */

const rulesPath =
    path.join(
        masteryRoot,
        "data",
        "config",
        "mastery-rules.json"
    );


const masteryRules =
    loadJson(
        rulesPath
    );


/* ============================================================
   Create repository
   ============================================================ */

const storage =
    new MemoryStorage();


const repository =
    new LocalProgressRepository({

        storage,

        storageKey:
            "integration-progress"
    });


/* ============================================================
   Recommendation stub
   ============================================================ */

/*
 * Step 16 tests the complete learning pipeline.
 *
 * The existing recommendation engine has its own
 * independent test suite.
 *
 * Here we use a small adapter that represents
 * the recommendation contract.
 *
 * Percentage mastery is intentionally strong enough
 * to recommend Profit & Loss.
 */

const recommendationEngine = {

    recommend({
        currentTopicId,
        currentMastery,
        examId
    }) {

        if (
            currentTopicId ===
                "percentage" &&
            currentMastery >= 70
        ) {

            return {

                topicId:
                    "profit-loss",

                relation:
                    "prerequisite",

                reason:
                    "Percentage mastery is sufficient for Profit & Loss.",

                examId
            };
        }


        return null;
    }
};


/* ============================================================
   Create pipeline
   ============================================================ */

const pipeline =
    new LearningPipeline({

        repository,

        masteryRules,

        recommendationEngine
    });


/* ============================================================
   TEST 1
   Fresh student
   ============================================================ */

section(
    1,
    "Fresh Student"
);


let state =
    await pipeline.loadProgress(
        "integration-student"
    );


if (
    state.studentId ===
        "integration-student"
) {

    pass(
        "Fresh student progress loaded"
    );

}
else {

    fail(
        "Fresh student progress incorrect"
    );
}


if (
    Object.keys(
        state.topics
    ).length === 0
) {

    pass(
        "Fresh student has no topic evidence"
    );

}
else {

    fail(
        "Fresh student unexpectedly has topic evidence"
    );
}


/* ============================================================
   TEST 2
   First question
   ============================================================ */

section(
    2,
    "First Question Attempt"
);


state =
    await pipeline.recordQuestion({

        studentId:
            "integration-student",

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
            "2026-08-13T11:00:00.000Z"
    });


if (
    state.progress
        .topics
        .percentage
        .evidence
        .attempts === 1
) {

    pass(
        "First question reached Progress Engine"
    );

}
else {

    fail(
        "First question was not recorded"
    );
}


/* ============================================================
   TEST 3
   Weak skill development
   ============================================================ */

section(
    3,
    "Weak Skill Development"
);


/*
 * Add several attempts to make
 * reverse-percentage the weak skill.
 */

const attempts = [

    {
        id:
            "percentage-p-002",

        skill:
            "reverse-percentage",

        correct:
            false
    },

    {
        id:
            "percentage-p-003",

        skill:
            "reverse-percentage",

        correct:
            false
    },

    {
        id:
            "percentage-p-004",

        skill:
            "reverse-percentage",

        correct:
            true
    },

    {
        id:
            "percentage-p-005",

        skill:
            "percentage-calculation",

        correct:
            true
    },

    {
        id:
            "percentage-p-006",

        skill:
            "percentage-calculation",

        correct:
            true
    },

    {
        id:
            "percentage-p-007",

        skill:
            "percentage-calculation",

        correct:
            true
    },

    {
        id:
            "percentage-p-008",

        skill:
            "percentage-calculation",

        correct:
            true
    },

    {
        id:
            "percentage-p-009",

        skill:
            "percentage-calculation",

        correct:
            true
    }
];


for (
    const attempt
    of attempts
) {

    state =
        await pipeline.recordQuestion({

            studentId:
                "integration-student",

            topicId:
                "percentage",

            questionId:
                attempt.id,

            conceptId:
                "percentage-basics",

            skillIds: [
                attempt.skill
            ],

            correct:
                attempt.correct,

            timeSpentSeconds:
                30
        });
}


const weak =
    state.weakSkills.percentage;


if (
    weak.some(
        skill =>
            skill.skillId ===
                "reverse-percentage"
    )
) {

    pass(
        "Reverse Percentage detected as weak skill"
    );

}
else {

    fail(
        "Reverse Percentage was not detected"
    );
}


/* ============================================================
   TEST 4
   Mastery calculation
   ============================================================ */

section(
    4,
    "Mastery Calculation"
);


const percentageMastery =
    state.mastery
        .topics
        .percentage;


if (
    Number.isFinite(
        percentageMastery.score
    )
) {

    pass(
        "Percentage mastery score calculated"
    );

}
else {

    fail(
        "Percentage mastery score missing"
    );
}


if (
    percentageMastery.attempts ===
        9
) {

    pass(
        "Mastery uses all recorded attempts"
    );

}
else {

    fail(
        `Expected 9 attempts, got ${percentageMastery.attempts}`
    );
}


/* ============================================================
   TEST 5
   Mini test
   ============================================================ */

section(
    5,
    "Mini-Test Integration"
);


state =
    await pipeline.recordMiniTest({

        studentId:
            "integration-student",

        topicId:
            "percentage",

        testId:
            "percentage-test-mastery",

        score:
            92,

        accuracy:
            94,

        attemptedAt:
            "2026-08-13T11:15:00.000Z"
    });


if (
    state.progress
        .topics
        .percentage
        .miniTests
        [
            "percentage-test-mastery"
        ]
        .bestScore ===
        92
) {

    pass(
        "Mini-test reached Progress Engine and Repository"
    );

}
else {

    fail(
        "Mini-test integration failed"
    );
}


/* ============================================================
   TEST 6
   Persistence
   ============================================================ */

section(
    6,
    "Persistence"
);


const reloaded =
    await pipeline.loadProgress(
        "integration-student"
    );


if (
    reloaded
        .topics
        .percentage
        .evidence
        .attempts ===
        9
) {

    pass(
        "Question evidence persisted and reloaded"
    );

}
else {

    fail(
        "Persisted question evidence incorrect"
    );
}


if (
    reloaded
        .topics
        .percentage
        .miniTests
        [
            "percentage-test-mastery"
        ]
        .bestScore ===
        92
) {

    pass(
        "Mini-test evidence persisted and reloaded"
    );

}
else {

    fail(
        "Persisted mini-test evidence incorrect"
    );
}


/* ============================================================
   TEST 7
   Recalculate after reload
   ============================================================ */

section(
    7,
    "Recalculate After Reload"
);


const reloadedState =
    pipeline.getLearningState(
        reloaded
    );


if (
    reloadedState
        .mastery
        .topics
        .percentage
) {

    pass(
        "Mastery recalculated from persisted evidence"
    );

}
else {

    fail(
        "Mastery could not be recalculated"
    );
}


/* ============================================================
   TEST 8
   Recommendation
   ============================================================ */

section(
    8,
    "Next Topic Recommendation"
);


const recommendation =
    pipeline.getRecommendation({

        progress:
            reloaded,

        currentTopicId:
            "percentage",

        examId:
            "ssc"
    });


if (
    recommendation &&
    recommendation.topicId ===
        "profit-loss"
) {

    pass(
        "Profit & Loss recommended after Percentage"
    );

}
else {

    fail(
        "Profit & Loss recommendation failed"
    );
}


if (
    recommendation?.relation ===
        "prerequisite"
) {

    pass(
        "Recommendation preserves prerequisite relationship"
    );

}
else {

    fail(
        "Recommendation relationship incorrect"
    );
}


/* ============================================================
   TEST 9
   Full learning loop
   ============================================================ */

section(
    9,
    "Complete Learning Loop"
);


if (
    reloaded
        .topics
        .percentage
        .evidence
        .attempts > 0 &&

    reloadedState
        .mastery
        .topics
        .percentage
        .score >= 0 &&

    weak.some(
        skill =>
            skill.skillId ===
                "reverse-percentage"
    ) &&

    recommendation?.topicId ===
        "profit-loss"
) {

    pass(
        "Student → Evidence → Mastery → Weak Skill → Recommendation loop works"
    );

}
else {

    fail(
        "Complete learning loop failed"
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
    " STEP 16 TEST SUMMARY"
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
        "✓ COMPLETE LEARNING PIPELINE PASSED"
    );

    console.log(
        "✓ STEP 16 COMPLETE"
    );

}
else {

    console.log(
        "✗ STEP 16 FAILED — REVIEW FAILURES ABOVE"
    );

    process.exitCode = 1;
}

console.log("");

console.log(
    "============================================"
);

console.log("");
