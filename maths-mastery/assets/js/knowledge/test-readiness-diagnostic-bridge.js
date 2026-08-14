/**
 * STEP 32.45E
 *
 * Readiness Diagnostic Bridge Contract Test
 */

import assert from "assert";


import {
    ReadinessDiagnosticBridge
} from "./readiness-diagnostic-bridge.js";


console.log("");
console.log("============================================================");
console.log(" STEP 32.45E — DIAGNOSTIC COVERAGE TEST");
console.log("============================================================");
console.log("");


/* ============================================================
   MOCK SELECTOR
   ============================================================ */

const mockSelector = {

    calls:
        [],


    selectQuestions(
        context,
        options
    ) {

        this.calls.push(
            {
                context,
                options
            }
        );


        const skillId =
            context.weakSkills[0]
                .skillId;


        /*
         * First call deliberately returns some unrelated
         * candidates followed by valid candidates.
         */

        const questions = [

            {

                score:
                    100,

                question: {

                    id:
                        "wrong-001",

                    topicId:
                        "algebra",

                    skillIds: [
                        "unrelated.skill"
                    ]
                }
            },

            {

                score:
                    99,

                question: {

                    id:
                        "wrong-002",

                    topicId:
                        "algebra",

                    skillIds: [
                        "different.skill"
                    ]
                }
            }
        ];


        if (
            context.currentTopicId ===
                null &&
            context.examId ===
                null
        ) {

            for (
                let i = 0;
                i < options.limit;
                i++
            ) {

                questions.push({

                    score:
                        90 -
                        i,

                    question: {

                        id:
                            `valid-${i + 1}`,

                        topicId:
                            "algebra",

                        skillIds: [
                            skillId
                        ]
                    }
                });
            }
        }


        return questions.slice(
            0,
            options.limit
        );
    },


    selectNextQuestion() {

        return null;
    }
};


const bridge =
    new ReadinessDiagnosticBridge({

        questionSelector:
            mockSelector,

        questionCount:
            5
    });


const intervention = {

    skillId:
        "algebra.negative-brackets"
};


/* ============================================================
   TEST 1 — PROGRESSIVE WIDENING
   ============================================================ */

console.log("");
console.log(
    "TEST 1 — Progressive Skill Matching"
);


const diagnostic =
    bridge.selectDiagnosticQuestions(
        intervention,
        {

            currentTopicId:
                "algebra",

            examId:
                "ssc",

            questionCount:
                5
        }
    );


assert.strictEqual(
    diagnostic.questions.length,
    5
);


assert.strictEqual(
    diagnostic.coverage,
    "widened"
);


assert.strictEqual(
    diagnostic.insufficientCoverage,
    false
);


assert.ok(
    diagnostic.questions.every(
        candidate => {

            const question =
                candidate.question;

            return question.skillIds.includes(
                "algebra.negative-brackets"
            );
        }
    )
);


assert.ok(
    mockSelector.calls.length >=
    2
);


console.log(
    "✓ Selector widened until exact skill coverage was found"
);


/* ============================================================
   TEST 2 — NO INVENTION
   ============================================================ */

console.log("");
console.log(
    "TEST 2 — Insufficient Coverage"
);


const emptySelector = {

    selectQuestions() {

        return [

            {

                score:
                    100,

                question: {

                    id:
                        "wrong",

                    topicId:
                        "algebra",

                    skillIds: [
                        "other.skill"
                    ]
                }
            }
        ];
    }
};


const sparseBridge =
    new ReadinessDiagnosticBridge({

        questionSelector:
            emptySelector,

        questionCount:
            5
    });


const sparse =
    sparseBridge.selectDiagnosticQuestions(
        intervention,
        {
            currentTopicId:
                "algebra",

            examId:
                "ssc",

            questionCount:
                5
        }
    );


assert.strictEqual(
    sparse.insufficientCoverage,
    true
);


assert.strictEqual(
    sparse.questions.length,
    0
);


console.log(
    "✓ Insufficient question coverage does not fabricate questions"
);


/* ============================================================
   TEST 3 — EXACT TARGET VALIDATION
   ============================================================ */

console.log("");
console.log(
    "TEST 3 — Exact Skill Validation"
);


const validation =
    bridge.validateDiagnosticSet(
        diagnostic
    );


assert.strictEqual(
    validation.valid,
    true
);


console.log(
    "✓ Exact intervention skill verified"
);


/* ============================================================
   TEST 4 — WRONG SKILL REJECTION
   ============================================================ */

console.log("");
console.log(
    "TEST 4 — Wrong Skill Rejection"
);


const invalid =
    bridge.validateDiagnosticSet({

        interventionSkillId:
            "algebra.negative-brackets",

        questions: [

            {

                question: {

                    id:
                        "wrong-999",

                    skillIds: [
                        "unrelated.skill"
                    ]
                }
            }
        ]
    });


assert.strictEqual(
    invalid.valid,
    false
);


console.log(
    "✓ Wrong-skill candidate rejected"
);


/* ============================================================
   SUMMARY
   ============================================================ */

console.log("");
console.log("============================================================");
console.log(" STEP 32.45E PASSED");
console.log("============================================================");
console.log("");

console.log(
    "✓ Progressive widening"
);

console.log(
    "✓ Exact skill filtering"
);

console.log(
    "✓ Insufficient coverage safety"
);

console.log(
    "✓ Wrong-skill rejection"
);

console.log("");
