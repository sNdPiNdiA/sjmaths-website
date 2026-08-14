import {
    validateQuestionData,
    validateResult,
    resultToProgressOutcome,
    createProgressEvidenceDelta,
    createEmptyAccumulator,
    applyEvidenceDelta,
    aggregateQuestionEvidence,
    aggregateQuestionResults
} from "./question-progress-integrator.js";


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


const question = {

    id:
        "percentage-reverse-001",

    topicId:
        "percentage",

    conceptId:
        "reverse-percentage",

    skillIds: [
        "reverse-percentage"
    ]

};


console.log("");
console.log(
    "============================================"
);
console.log(
    " STEP 30 — EXPOSURE → PROGRESS INTEGRATION"
);
console.log(
    "============================================"
);


/* ============================================================
   TEST 1 — Question Validation
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 1 — Question Validation"
);
console.log(
    "--------------------------------------------"
);


assert(
    validateQuestionData(
        question
    ) === true,
    "Question metadata is valid"
);


/* ============================================================
   TEST 2 — Result Validation
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 2 — Result Validation"
);
console.log(
    "--------------------------------------------"
);


assert(
    validateResult(
        "correct"
    ) === true,
    "Correct result accepted"
);


assert(
    validateResult(
        "incorrect"
    ) === true,
    "Incorrect result accepted"
);


assert(
    validateResult(
        "skipped"
    ) === true,
    "Skipped result accepted"
);


let invalidResultRejected =
    false;

try {

    validateResult(
        "invalid"
    );

} catch {

    invalidResultRejected =
        true;
}


assert(
    invalidResultRejected,
    "Invalid result rejected"
);


/* ============================================================
   TEST 3 — Correct Mapping
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 3 — Correct Mapping"
);
console.log(
    "--------------------------------------------"
);


const correctOutcome =
    resultToProgressOutcome(
        "correct"
    );


assert(
    correctOutcome.attempted === true,
    "Correct result creates an attempt"
);


assert(
    correctOutcome.correct === 1,
    "Correct result creates correct evidence"
);


assert(
    correctOutcome.incorrect === 0,
    "Correct result creates no incorrect evidence"
);


/* ============================================================
   TEST 4 — Incorrect Mapping
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 4 — Incorrect Mapping"
);
console.log(
    "--------------------------------------------"
);


const incorrectOutcome =
    resultToProgressOutcome(
        "incorrect"
    );


assert(
    incorrectOutcome.attempted === true,
    "Incorrect result creates an attempt"
);


assert(
    incorrectOutcome.correct === 0,
    "Incorrect result creates no correct evidence"
);


assert(
    incorrectOutcome.incorrect === 1,
    "Incorrect result creates incorrect evidence"
);


/* ============================================================
   TEST 5 — Skipped Mapping
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 5 — Skipped Mapping"
);
console.log(
    "--------------------------------------------"
);


const skippedOutcome =
    resultToProgressOutcome(
        "skipped"
    );


assert(
    skippedOutcome.attempted === false,
    "Skipped result does not create answered attempt"
);


assert(
    skippedOutcome.skipped === 1,
    "Skipped result creates skipped evidence"
);


/* ============================================================
   TEST 6 — Evidence Delta
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 6 — Evidence Delta"
);
console.log(
    "--------------------------------------------"
);


const delta =
    createProgressEvidenceDelta(
        question,
        "correct",
        30
    );


assert(
    delta.questionId ===
        "percentage-reverse-001",
    "Question ID preserved"
);


assert(
    delta.topicId ===
        "percentage",
    "Topic ID preserved"
);


assert(
    delta.conceptId ===
        "reverse-percentage",
    "Concept ID preserved"
);


assert(
    delta.skillIds.includes(
        "reverse-percentage"
    ),
    "Skill mapping preserved"
);


assert(
    delta.timeSpentSeconds === 30,
    "Time evidence preserved"
);


/* ============================================================
   TEST 7 — Aggregate Topic / Concept / Skill
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 7 — Aggregate Targets"
);
console.log(
    "--------------------------------------------"
);


const aggregated =
    aggregateQuestionEvidence(
        question,
        "correct",
        30
    );


assert(
    aggregated.topic.id ===
        "percentage",
    "Topic evidence created"
);


assert(
    aggregated.concept.id ===
        "reverse-percentage",
    "Concept evidence created"
);


assert(
    aggregated.skills[
        "reverse-percentage"
    ] !== undefined,
    "Skill evidence created"
);


assert(
    aggregated.topic.evidence.correct === 1,
    "Correct evidence reaches topic"
);


assert(
    aggregated.concept.evidence.correct === 1,
    "Correct evidence reaches concept"
);


assert(
    aggregated.skills[
        "reverse-percentage"
    ].correct === 1,
    "Correct evidence reaches skill"
);


/* ============================================================
   TEST 8 — Multiple Attempts
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 8 — Multiple Attempts"
);
console.log(
    "--------------------------------------------"
);


const attempts = [

    {
        question,
        result:
            "correct",
        timeSpentSeconds:
            30
    },

    {
        question,
        result:
            "incorrect",
        timeSpentSeconds:
            20
    },

    {
        question,
        result:
            "correct",
        timeSpentSeconds:
            20
    }

];


const aggregate =
    aggregateQuestionResults(
        attempts
    );


assert(
    aggregate.topics.percentage.attempts === 3,
    "Topic attempt count aggregated"
);


assert(
    aggregate.topics.percentage.correct === 2,
    "Topic correct count aggregated"
);


assert(
    aggregate.topics.percentage.incorrect === 1,
    "Topic incorrect count aggregated"
);


assert(
    aggregate.topics.percentage.timeSpentSeconds === 70,
    "Topic time aggregated"
);


/* ============================================================
   TEST 9 — Concept Aggregation
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 9 — Concept Aggregation"
);
console.log(
    "--------------------------------------------"
);


assert(
    aggregate.concepts[
        "reverse-percentage"
    ].attempts === 3,
    "Concept attempts aggregated"
);


assert(
    aggregate.concepts[
        "reverse-percentage"
    ].correct === 2,
    "Concept correct evidence aggregated"
);


/* ============================================================
   TEST 10 — Skill Aggregation
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 10 — Skill Aggregation"
);
console.log(
    "--------------------------------------------"
);


assert(
    aggregate.skills[
        "reverse-percentage"
    ].attempts === 3,
    "Skill attempts aggregated"
);


assert(
    aggregate.skills[
        "reverse-percentage"
    ].incorrect === 1,
    "Skill incorrect evidence aggregated"
);


/* ============================================================
   TEST 11 — Skipped Does Not Become Answered
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 11 — Skipped Evidence"
);
console.log(
    "--------------------------------------------"
);


const withSkipped =
    aggregateQuestionResults(
        [
            {
                question,
                result:
                    "skipped",
                timeSpentSeconds:
                    5
            }
        ]
    );


assert(
    withSkipped.topics.percentage.attempts === 0,
    "Skipped question does not create answered attempt"
);


assert(
    withSkipped.topics.percentage.skipped === 1,
    "Skipped evidence is preserved"
);


assert(
    withSkipped.topics.percentage.timeSpentSeconds === 5,
    "Skipped time is preserved"
);


/* ============================================================
   TEST 12 — Multiple Skills
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 12 — Multiple Skills"
);
console.log(
    "--------------------------------------------"
);


const multiSkillQuestion = {

    ...question,

    id:
        "multi-skill-test",

    skillIds: [
        "reverse-percentage",
        "percentage-calculation"
    ]

};


const multiSkill =
    aggregateQuestionResults(
        [
            {
                question:
                    multiSkillQuestion,

                result:
                    "correct",

                timeSpentSeconds:
                    15
            }
        ]
    );


assert(
    multiSkill.skills[
        "reverse-percentage"
    ].correct === 1,
    "First skill receives evidence"
);


assert(
    multiSkill.skills[
        "percentage-calculation"
    ].correct === 1,
    "Second skill receives evidence"
);


/* ============================================================
   TEST 13 — Immutable Aggregation
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 13 — Immutable Aggregation"
);
console.log(
    "--------------------------------------------"
);


const original =
    createEmptyAccumulator();


const updated =
    applyEvidenceDelta(
        original,
        delta
    );


assert(
    original.attempts === 0,
    "Original accumulator remains unchanged"
);


assert(
    updated.attempts === 1,
    "Updated accumulator contains evidence"
);


assert(
    updated !== original,
    "Accumulator update is immutable"
);


/* ============================================================
   TEST 14 — No Hardcoded Question IDs
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 14 — DATA-DRIVEN INTEGRATION"
);
console.log(
    "--------------------------------------------"
);


const anotherQuestion = {

    id:
        "production-question-xyz",

    topicId:
        "profit-loss",

    conceptId:
        "profit-basics",

    skillIds: [
        "profit-percentage"
    ]

};


const anotherResult =
    aggregateQuestionResults(
        [
            {
                question:
                    anotherQuestion,

                result:
                    "incorrect",

                timeSpentSeconds:
                    25
            }
        ]
    );


assert(
    anotherResult.topics[
        "profit-loss"
    ].incorrect === 1,
    "Production topic mapping is data-driven"
);


assert(
    anotherResult.questions[
        "production-question-xyz"
    ].incorrect === 1,
    "Question ID is taken from data"
);


/* ============================================================
   TEST 15 — Final Integrity
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 15 — Integration Integrity"
);
console.log(
    "--------------------------------------------"
);


assert(
    Object.keys(
        aggregate.topics
    ).length === 1,
    "Topic aggregation contains expected entity"
);


assert(
    Object.keys(
        aggregate.concepts
    ).length === 1,
    "Concept aggregation contains expected entity"
);


assert(
    Object.keys(
        aggregate.skills
    ).length === 1,
    "Skill aggregation contains expected entity"
);


console.log("");
console.log(
    "============================================"
);
console.log(
    " STEP 30 TEST SUMMARY"
);
console.log(
    "============================================"
);

console.log("");
console.log(
    "✓ Question metadata validation works"
);
console.log(
    "✓ Result mapping works"
);
console.log(
    "✓ Correct evidence mapping works"
);
console.log(
    "✓ Incorrect evidence mapping works"
);
console.log(
    "✓ Skipped evidence mapping works"
);
console.log(
    "✓ Topic aggregation works"
);
console.log(
    "✓ Concept aggregation works"
);
console.log(
    "✓ Skill aggregation works"
);
console.log(
    "✓ Time aggregation works"
);
console.log(
    "✓ Multiple attempts aggregate correctly"
);
console.log(
    "✓ Multiple skills receive evidence"
);
console.log(
    "✓ Immutable aggregation works"
);
console.log(
    "✓ Integration is data-driven"
);
console.log(
    "✓ No hardcoded question IDs required"
);

console.log("");
console.log(
    "✓ ALL QUESTION → PROGRESS INTEGRATION TESTS PASSED"
);

console.log("");
console.log(
    "✓ STEP 30 COMPLETE"
);

console.log("");
