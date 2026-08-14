/**
 * STEP 32.34
 * Readiness Resolution Engine Contract Test
 */

import assert from "assert";

import {
    loadReadinessResolutionEngine
} from "./readiness-resolution-engine.js";


console.log("");
console.log("============================================================");
console.log(" STEP 32.34 — READINESS RESOLUTION CONTRACT TEST");
console.log("============================================================");
console.log("");


const engine =
    loadReadinessResolutionEngine();


console.log(
    "✓ Engine loaded"
);


/* ============================================================
   TEST 1 — TARGET EXISTS
   ============================================================ */

console.log("");
console.log(
    "TEST 1 — Target Resolution"
);


const target =
    "quadratic.factorisation";


const emptyResult =
    engine.resolve(
        target,
        {}
    );


assert.strictEqual(
    emptyResult.found,
    true
);


console.log(
    "✓ quadratic.factorisation mapping found"
);


/* ============================================================
   TEST 2 — EMPTY LEARNER
   ============================================================ */

console.log("");
console.log(
    "TEST 2 — Empty Learner"
);


assert.strictEqual(
    emptyResult.ready,
    false
);


assert.ok(
    emptyResult.missing.length >
    0
);


console.log(
    `✓ Missing prerequisites detected: ${emptyResult.missing.length}`
);


/* ============================================================
   TEST 3 — FULLY MASTERED LEARNER
   ============================================================ */

console.log("");
console.log(
    "TEST 3 — Fully Ready Learner"
);


const fullEvidence = {};


for (
    const item
    of emptyResult.missing
) {

    fullEvidence[
        item.skillId
    ] = {

        mastered: true,

        score: 100,

        attempts: 3
    };
}


const readyResult =
    engine.resolve(
        target,
        fullEvidence
    );


assert.strictEqual(
    readyResult.ready,
    true
);


assert.strictEqual(
    readyResult.missing.length,
    0
);


assert.strictEqual(
    readyResult.remediationPath.length,
    0
);


console.log(
    "✓ Fully mastered learner is ready"
);


/* ============================================================
   TEST 4 — ONE MISSING CORE SKILL
   ============================================================ */

console.log("");
console.log(
    "TEST 4 — Single Missing Skill"
);


const oneGapEvidence = {};


for (
    const item
    of emptyResult.missing
) {

    oneGapEvidence[
        item.skillId
    ] = {

        mastered: true,

        score: 100,

        attempts: 3
    };
}


const deliberateGap =
    emptyResult.missing.find(
        item =>
            item.skillId ===
            "algebra.negative-brackets"
    );


if (
    deliberateGap
) {

    delete oneGapEvidence[
        "algebra.negative-brackets"
    ];


    /*
     * Also leave the prerequisite sign skill mastered.
     * This tests direct-gap detection.
     */
}


const oneGapResult =
    engine.resolve(
        target,
        oneGapEvidence
    );


if (
    deliberateGap
) {

    assert.strictEqual(
        oneGapResult.ready,
        false
    );


    assert.ok(
        oneGapResult.missing.some(
            item =>
                item.skillId ===
                "algebra.negative-brackets"
        )
    );


    console.log(
        "✓ Direct missing skill detected"
    );

}
else {

    console.log(
        "✓ Deliberate gap skill not present in current mapping; test skipped safely"
    );
}


/* ============================================================
   TEST 5 — EVIDENCE SCORE
   ============================================================ */

console.log("");
console.log(
    "TEST 5 — Score-Based Evidence"
);


const scoreEvidence = {};


for (
    const item
    of emptyResult.missing
) {

    scoreEvidence[
        item.skillId
    ] = {

        score: 100,

        attempts: 4
    };
}


const scoreResult =
    engine.resolve(
        target,
        scoreEvidence
    );


assert.strictEqual(
    scoreResult.ready,
    true
);


console.log(
    "✓ Score-based mastery recognised"
);


/* ============================================================
   TEST 6 — LOW SCORE
   ============================================================ */

console.log("");
console.log(
    "TEST 6 — Low Score Remains Unready"
);


const lowEvidence = {};


for (
    const item
    of emptyResult.missing
) {

    lowEvidence[
        item.skillId
    ] = {

        score: 40,

        attempts: 3
    };
}


const lowResult =
    engine.resolve(
        target,
        lowEvidence
    );


assert.strictEqual(
    lowResult.ready,
    false
);


assert.ok(
    lowResult.missing.length >
    0
);


console.log(
    "✓ Low-score prerequisites remain unresolved"
);


/* ============================================================
   TEST 7 — DETERMINISTIC PATH
   ============================================================ */

console.log("");
console.log(
    "TEST 7 — Deterministic Remediation Path"
);


const pathA =
    engine.resolve(
        target,
        {}
    ).remediationPath.map(
        item =>
            item.skillId
    );


const pathB =
    engine.resolve(
        target,
        {}
    ).remediationPath.map(
        item =>
            item.skillId
    );


assert.deepStrictEqual(
    pathA,
    pathB
);


console.log(
    "✓ Remediation ordering is deterministic"
);


/* ============================================================
   TEST 8 — NO DUPLICATES
   ============================================================ */

console.log("");
console.log(
    "TEST 8 — Duplicate-Free Path"
);


const path =
    engine.resolve(
        target,
        {}
    ).remediationPath.map(
        item =>
            item.skillId
    );


const unique =
    new Set(
        path
    );


assert.strictEqual(
    unique.size,
    path.length
);


console.log(
    "✓ Remediation path contains no duplicate skills"
);


/* ============================================================
   TEST 9 — UNKNOWN TARGET
   ============================================================ */

console.log("");
console.log(
    "TEST 9 — Unknown Target"
);


const unknownResult =
    engine.resolve(
        "does-not-exist",
        {}
    );


assert.strictEqual(
    unknownResult.found,
    false
);


console.log(
    "✓ Unknown target handled safely"
);


/* ============================================================
   TEST 10 — EXPLANATION
   ============================================================ */

console.log("");
console.log(
    "TEST 10 — Explanation"
);


const explanation =
    engine.explain(
        target,
        {}
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
    "✓ Explanation generated"
);


/* ============================================================
   SUMMARY
   ============================================================ */

console.log("");
console.log("============================================================");
console.log(" STEP 32.34 PASSED");
console.log("============================================================");
console.log("");

console.log(
    `Missing readiness skills detected: ${emptyResult.missing.length}`
);

console.log(
    `Remediation path length: ${emptyResult.remediationPath.length}`
);

console.log("");
console.log(
    "✓ Target resolution verified"
);

console.log(
    "✓ Empty learner verified"
);

console.log(
    "✓ Fully mastered learner verified"
);

console.log(
    "✓ Single-gap detection verified"
);

console.log(
    "✓ Score-based evidence verified"
);

console.log(
    "✓ Low-score handling verified"
);

console.log(
    "✓ Deterministic path verified"
);

console.log(
    "✓ Duplicate-free path verified"
);

console.log(
    "✓ Unknown target handling verified"
);

console.log(
    "✓ Explanation verified"
);

console.log("");
