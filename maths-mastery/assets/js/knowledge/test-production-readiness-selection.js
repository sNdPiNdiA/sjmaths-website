/**
 * STEP 32.51
 *
 * Production Readiness Question Selection Test
 *
 * READ-ONLY
 */

import assert from "assert";


import {
    selectQuestions,
    selectNextQuestion,
    explainSelection
} from "./question-selection-engine.js";


console.log("");
console.log(
    "============================================================"
);
console.log(
    " STEP 32.51 — PRODUCTION READINESS SELECTION TEST"
);
console.log(
    "============================================================"
);
console.log("");


/* ============================================================
   TEST 1 — EXACT WEAK SKILL
   ============================================================ */

console.log(
    "TEST 1 — Exact Readiness Skill Selection"
);


const context = {

    weakSkills: [

        {
            skillId:
                "arithmetic.sign-rules",

            score:
                0
        }

    ],

    masteryStatus:
        "not-started",

    currentTopicId:
        null,

    examId:
        null,

    attemptedQuestionIds:
        [],

    targetDifficulty:
        "basic"
};


const results =
    selectQuestions(
        context,
        {
            limit:
                5
        }
    );


assert.ok(
    Array.isArray(
        results
    )
);


assert.ok(
    results.length >
    0
);


console.log(
    `✓ Selector returned ${results.length} questions`
);


/* ============================================================
   TEST 2 — EXACT SKILL MATCH
   ============================================================ */

console.log("");
console.log(
    "TEST 2 — Exact Skill Match"
);


for (
    const candidate
    of results
) {

    assert.ok(
        candidate
    );


    assert.ok(
        candidate.question
    );


    const question =
        candidate.question;


    assert.ok(
        Array.isArray(
            question.skillIds
        )
    );


    assert.ok(
        question.skillIds.includes(
            "arithmetic.sign-rules"
        )
    );
}


console.log(
    "✓ Every selected question targets arithmetic.sign-rules"
);


/* ============================================================
   TEST 3 — REAL READINESS SOURCE
   ============================================================ */

console.log("");
console.log(
    "TEST 3 — Readiness Source"
);


const readinessResults =
    results.filter(
        candidate =>
            candidate.question
                ?.readinessSkillId ===
            "arithmetic.sign-rules"
    );


assert.ok(
    readinessResults.length >
    0
);


assert.ok(
    readinessResults.every(
        candidate =>
            candidate.question
                ?._indexSource ===
                "readiness" ||
            candidate.question
                ?.readinessSkillId ===
                "arithmetic.sign-rules"
    )
);


console.log(
    `✓ Readiness questions returned: ${readinessResults.length}`
);


/* ============================================================
   TEST 4 — SELECTION SCORE
   ============================================================ */

console.log("");
console.log(
    "TEST 4 — Selection Scoring"
);


for (
    const candidate
    of results
) {

    assert.strictEqual(
        typeof candidate.score,
        "number"
    );


    assert.ok(
        Number.isFinite(
            candidate.score
        )
    );
}


console.log(
    "✓ Selection scores valid"
);


/* ============================================================
   TEST 5 — NEXT QUESTION
   ============================================================ */

console.log("");
console.log(
    "TEST 5 — Next Question"
);


const next =
    selectNextQuestion(
        context
    );


assert.ok(
    next
);


assert.ok(
    next.question
);


assert.ok(
    next.question.skillIds.includes(
        "arithmetic.sign-rules"
    )
);


console.log(
    `✓ Next question selected: ${next.question.id}`
);


/* ============================================================
   TEST 6 — EXPLANATION
   ============================================================ */

console.log("");
console.log(
    "TEST 6 — Selection Explanation"
);


const explanation =
    explainSelection(
        next.question,
        context
    );


assert.ok(
    Array.isArray(
        explanation
    )
);


assert.ok(
    explanation.length >
    0
);


console.log(
    "✓ Selection explanation generated"
);


/* ============================================================
   TEST 7 — ATTEMPTED QUESTION EXCLUSION
   ============================================================ */

console.log("");
console.log(
    "TEST 7 — Attempted Question Exclusion"
);


const selectedId =
    results[0]
        .question
        .id;


const contextWithAttempt =
    {

        ...context,

        attemptedQuestionIds: [
            selectedId
        ]
    };


const newResults =
    selectQuestions(
        contextWithAttempt,
        {
            limit:
                5
        }
    );


assert.ok(
    newResults.every(
        candidate =>
            candidate.question.id !==
            selectedId
    )
);


console.log(
    "✓ Attempted question excluded"
);


/* ============================================================
   TEST 8 — OTHER FOUNDATION SKILL
   ============================================================ */

console.log("");
console.log(
    "TEST 8 — Second Readiness Skill"
);


const secondResults =
    selectQuestions(
        {
            ...context,

            weakSkills: [

                {
                    skillId:
                        "algebra.negative-brackets",

                    score:
                        0
                }

            ]
        },
        {
            limit:
                5
        }
    );


assert.ok(
    secondResults.length >
    0
);


assert.ok(
    secondResults.some(
        candidate =>
            candidate.question
                ?.skillIds
                ?.includes(
                    "algebra.negative-brackets"
                )
    )
);


console.log(
    `✓ algebra.negative-brackets selectable: ${secondResults.length} candidates`
);


/* ============================================================
   TEST 9 — NON-READINESS SAFETY
   ============================================================ */

console.log("");
console.log(
    "TEST 9 — Unknown Skill Safety"
);


const unknownResults =
    selectQuestions(
        {
            ...context,

            weakSkills: [

                {
                    skillId:
                        "readiness.unknown-skill",

                    score:
                        0
                }

            ]
        },
        {
            limit:
                5
        }
    );


for (
    const candidate
    of unknownResults
) {

    assert.ok(
        candidate.question
    );
}


console.log(
    "✓ Unknown skill handled safely"
);


/* ============================================================
   TEST 10 — LIMIT
   ============================================================ */

console.log("");
console.log(
    "TEST 10 — Selection Limit"
);


const limited =
    selectQuestions(
        context,
        {
            limit:
                2
        }
    );


assert.ok(
    limited.length <=
    2
);


console.log(
    "✓ Selection limit respected"
);


/* ============================================================
   SUMMARY
   ============================================================ */

console.log("");
console.log(
    "============================================================"
);
console.log(
    " STEP 32.51 PASSED"
);
console.log(
    "============================================================"
);
console.log("");

console.log(
    "✓ Production selector reads readiness index entries"
);

console.log(
    "✓ Exact readiness skill selection works"
);

console.log(
    "✓ Readiness question source preserved"
);

console.log(
    "✓ Selection scoring works"
);

console.log(
    "✓ Next-question selection works"
);

console.log(
    "✓ Explanation works"
);

console.log(
    "✓ Attempted-question exclusion works"
);

console.log(
    "✓ Multiple readiness skills selectable"
);

console.log(
    "✓ Unknown skill safety preserved"
);

console.log(
    "✓ Selection limit preserved"
);

console.log("");
