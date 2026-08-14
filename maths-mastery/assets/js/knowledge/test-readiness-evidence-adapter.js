/**
 * STEP 32.38B
 * Robust Readiness Evidence Adapter Contract Test
 */

import assert from "assert";


import {
    ReadinessEvidenceAdapter
} from "./readiness-evidence-adapter.js";


console.log("");
console.log("============================================================");
console.log(" STEP 32.38B — READINESS EVIDENCE ADAPTER TEST");
console.log("============================================================");
console.log("");


const adapter =
    new ReadinessEvidenceAdapter();


console.log(
    "✓ Evidence adapter created"
);


/* ============================================================
   TEST 1
   ============================================================ */

console.log("");
console.log(
    "TEST 1 — Skill Map"
);


const progressA = {

    skills: {

        "algebra.negative-brackets": {

            score:
                91,

            attempts:
                5,

            correct:
                5
        },

        "arithmetic.sign-rules": {

            score:
                72,

            attempts:
                4,

            correct:
                3,

            incorrect:
                1
        }
    }
};


const evidenceA =
    adapter.extractSkillEvidence(
        progressA
    );


assert.ok(
    evidenceA[
        "algebra.negative-brackets"
    ]
);


assert.strictEqual(
    evidenceA[
        "algebra.negative-brackets"
    ].mastered,
    true
);


assert.strictEqual(
    evidenceA[
        "arithmetic.sign-rules"
    ].mastered,
    false
);


console.log(
    "✓ Skill map normalized"
);


/* ============================================================
   TEST 2 — QUESTION RECORDS
   ============================================================ */

console.log("");
console.log(
    "TEST 2 — Question-Level Skill Evidence"
);


const progressB = {

    records: [

        {
            questionId:
                "q1",

            skillIds: [
                "algebra.negative-brackets"
            ],

            score:
                100,

            correct:
                1,

            incorrect:
                0,

            skipped:
                0
        },

        {
            questionId:
                "q2",

            skillIds: [
                "algebra.negative-brackets"
            ],

            score:
                0,

            correct:
                0,

            incorrect:
                1,

            skipped:
                0
        }
    ]
};


const evidenceB =
    adapter.extractSkillEvidence(
        progressB
    );


assert.ok(
    Object.prototype.hasOwnProperty.call(
        evidenceB,
        "algebra.negative-brackets"
    )
);


assert.ok(
    evidenceB[
        "algebra.negative-brackets"
    ].attempts >=
    2
);


assert.ok(
    evidenceB[
        "algebra.negative-brackets"
    ].correct >=
    1
);


assert.ok(
    evidenceB[
        "algebra.negative-brackets"
    ].incorrect >=
    1
);


assert.strictEqual(
    evidenceB[
        "algebra.negative-brackets"
    ].score,
    100
);


console.log(
    "✓ Question-level evidence normalized"
);


/* ============================================================
   TEST 3 — SINGLE skillId RECORD
   ============================================================ */

console.log("");
console.log(
    "TEST 3 — Single skillId Record"
);


const progressC = {

    records: [

        {
            skillId:
                "arithmetic.hcf",

            score:
                90,

            attempts:
                3,

            correct:
                3
        }
    ]
};


const evidenceC =
    adapter.extractSkillEvidence(
        progressC
    );


assert.ok(
    evidenceC[
        "arithmetic.hcf"
    ]
);


assert.strictEqual(
    evidenceC[
        "arithmetic.hcf"
    ].mastered,
    true
);


console.log(
    "✓ Single skillId record handled"
);


/* ============================================================
   TEST 4 — NESTED LEARNING
   ============================================================ */

console.log("");
console.log(
    "TEST 4 — Nested Learning Records"
);


const progressD = {

    learning: {

        records: [

            {
                skillIds: [
                    "algebra.common-factor"
                ],

                score:
                    88,

                attempts:
                    4
            }
        ]
    }
};


const evidenceD =
    adapter.extractSkillEvidence(
        progressD
    );


assert.ok(
    evidenceD[
        "algebra.common-factor"
    ]
);


console.log(
    "✓ Nested learning records handled"
);


/* ============================================================
   TEST 5 — APPLICATION STATE
   ============================================================ */

console.log("");
console.log(
    "TEST 5 — Application State"
);


const state = {

    progress: {

        records: [

            {
                skillIds: [
                    "algebra.common-factor"
                ],

                score:
                    92,

                attempts:
                    9,

                correct:
                    8,

                incorrect:
                    1
            }
        ]
    },

    mastery:
        null
};


const evidenceE =
    adapter.fromApplicationState(
        state
    );


assert.ok(
    evidenceE[
        "algebra.common-factor"
    ]
);


assert.strictEqual(
    evidenceE[
        "algebra.common-factor"
    ].mastered,
    true
);


console.log(
    "✓ Application state converted"
);


/* ============================================================
   TEST 6 — MASTERY PREFERENCE
   ============================================================ */

console.log("");
console.log(
    "TEST 6 — Mastery Preference"
);


const stateF = {

    progress: {

        records: [

            {
                skillIds: [
                    "algebra.common-factor"
                ],

                score:
                    40,

                attempts:
                    5
            }
        ]
    },

    mastery: {

        skills: {

            "algebra.common-factor": {

                score:
                    95,

                attempts:
                    8
            }
        }
    }
};


const evidenceF =
    adapter.fromApplicationState(
        stateF
    );


assert.ok(
    evidenceF[
        "algebra.common-factor"
    ]
);


assert.strictEqual(
    evidenceF[
        "algebra.common-factor"
    ].score,
    95
);


console.log(
    "✓ Mastery preferred when explicitly available"
);


/* ============================================================
   TEST 7 — TARGET FILTER
   ============================================================ */

console.log("");
console.log(
    "TEST 7 — Target Filtering"
);


const target = {

    targetSkillId:
        "quadratic.factorisation",

    readiness: [

        {
            skillId:
                "algebra.negative-brackets",

            requirement:
                "core"
        },

        {
            skillId:
                "arithmetic.hcf",

            requirement:
                "supporting"
        }
    ]
};


const targetEvidence =
    adapter.buildTargetEvidence(
        "quadratic.factorisation",

        {

            progress: {

                skills: {

                    "algebra.negative-brackets": {

                        score:
                            90,

                        attempts:
                            3
                    },

                    "arithmetic.hcf": {

                        score:
                            75,

                        attempts:
                            4
                    },

                    "unrelated.skill": {

                        score:
                            100,

                        attempts:
                            20
                    }
                }
            },

            mastery:
                null
        },

        target
    );


assert.ok(
    targetEvidence.evidence[
        "algebra.negative-brackets"
    ]
);


assert.ok(
    targetEvidence.evidence[
        "arithmetic.hcf"
    ]
);


assert.strictEqual(
    Object.prototype.hasOwnProperty.call(
        targetEvidence.evidence,
        "unrelated.skill"
    ),
    false
);


console.log(
    "✓ Target-specific filtering works"
);


/* ============================================================
   TEST 8 — MISSING EVIDENCE
   ============================================================ */

console.log("");
console.log(
    "TEST 8 — Missing Evidence"
);


const missing =
    adapter.buildTargetEvidence(
        "quadratic.factorisation",

        {
            progress: {},
            mastery: null
        },

        target
    );


assert.strictEqual(
    missing.evidence[
        "algebra.negative-brackets"
    ].mastered,
    false
);


assert.strictEqual(
    missing.evidence[
        "algebra.negative-brackets"
    ].score,
    0
);


console.log(
    "✓ Missing evidence defaults safely"
);


/* ============================================================
   TEST 9 — EXPLICIT MASTERY
   ============================================================ */

console.log("");
console.log(
    "TEST 9 — Explicit Mastery"
);


const explicit =
    adapter.normalizeSkillEvidence({

        mastered:
            true,

        score:
            20,

        attempts:
            1
    });


assert.strictEqual(
    explicit.mastered,
    true
);


console.log(
    "✓ Explicit mastery respected"
);


/* ============================================================
   SUMMARY
   ============================================================ */

console.log("");
console.log("============================================================");
console.log(" STEP 32.38B PASSED");
console.log("============================================================");
console.log("");

console.log(
    "✓ Skill-map evidence"
);

console.log(
    "✓ Question-level evidence"
);

console.log(
    "✓ Single-skill records"
);

console.log(
    "✓ Nested learning records"
);

console.log(
    "✓ Application-state conversion"
);

console.log(
    "✓ Mastery preference"
);

console.log(
    "✓ Target filtering"
);

console.log(
    "✓ Missing-evidence handling"
);

console.log(
    "✓ Explicit mastery"
);

console.log("");
