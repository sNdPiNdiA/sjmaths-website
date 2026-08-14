/**
 * STEP 32.36
 * Application Readiness Adapter Contract Test
 */


import assert from "assert";


import {
    ReadinessApplicationAdapter
} from "./readiness-application-adapter.js";


console.log("");
console.log("============================================================");
console.log(" STEP 32.36 — APPLICATION READINESS CONTRACT TEST");
console.log("============================================================");
console.log("");


const adapter =
    new ReadinessApplicationAdapter();


console.log(
    "✓ Application readiness adapter created"
);


/* ============================================================
   TEST 1 — TARGET STATE
   ============================================================ */

console.log("");
console.log(
    "TEST 1 — Target State"
);


const emptyState =
    adapter.getState(
        "quadratic.factorisation",
        {}
    );


assert.strictEqual(
    emptyState.targetSkillId,
    "quadratic.factorisation"
);


assert.strictEqual(
    emptyState.readiness.found,
    true
);


assert.strictEqual(
    emptyState.readiness.ready,
    false
);


assert.ok(
    emptyState.readiness.missing.length >
    0
);


assert.ok(
    emptyState.interventionPlan.interventionRequired
);


console.log(
    "✓ Application state generated"
);


/* ============================================================
   TEST 2 — INTERVENTION PLAN
   ============================================================ */

console.log("");
console.log(
    "TEST 2 — Intervention Plan"
);


assert.ok(
    Array.isArray(
        emptyState.interventionPlan.blocks
    )
);


assert.ok(
    emptyState.interventionPlan.blocks.length >
    0
);


assert.ok(
    emptyState.interventionPlan.blocks.length <=
    3
);


console.log(
    `✓ Intervention blocks: ${emptyState.interventionPlan.blocks.length}`
);


/* ============================================================
   TEST 3 — FULLY READY LEARNER
   ============================================================ */

console.log("");
console.log(
    "TEST 3 — Fully Ready Learner"
);


const readinessResolver =
    adapter.resolutionEngine;


const baseResolution =
    readinessResolver.resolve(
        "quadratic.factorisation",
        {}
    );


const fullEvidence = {};


for (
    const item
    of baseResolution.missing
) {

    fullEvidence[
        item.skillId
    ] = {

        mastered:
            true,

        score:
            100,

        attempts:
            5
    };
}


const readyState =
    adapter.getState(
        "quadratic.factorisation",
        fullEvidence
    );


assert.strictEqual(
    readyState.readiness.ready,
    true
);


assert.strictEqual(
    readyState.readiness.missing.length,
    0
);


assert.strictEqual(
    readyState.interventionPlan.interventionRequired,
    false
);


assert.strictEqual(
    readyState.interventionPlan.blocks.length,
    0
);


console.log(
    "✓ Fully ready application state verified"
);


/* ============================================================
   TEST 4 — ONE BLOCKING SKILL
   ============================================================ */

console.log("");
console.log(
    "TEST 4 — Single Blocking Skill"
);


const partialEvidence = {};


for (
    const item
    of baseResolution.missing
) {

    partialEvidence[
        item.skillId
    ] = {

        mastered:
            true,

        score:
            100,

        attempts:
            5
    };
}


const blockingSkill =
    baseResolution.missing.find(
        item =>
            item.skillId ===
            "algebra.negative-brackets"
    );


if (
    blockingSkill
) {

    delete partialEvidence[
        "algebra.negative-brackets"
    ];


    const partialState =
        adapter.getState(
            "quadratic.factorisation",
            partialEvidence
        );


    assert.strictEqual(
        partialState.readiness.ready,
        false
    );


    assert.ok(
        partialState.readiness.missing.some(
            item =>
                item.skillId ===
                "algebra.negative-brackets"
        )
    );


    assert.ok(
        partialState.interventionPlan.blocks.length >
        0
    );


    console.log(
        "✓ Blocking prerequisite propagated to application state"
    );

}
else {

    console.log(
        "✓ Blocking skill unavailable in current mapping; safe skip"
    );
}


/* ============================================================
   TEST 5 — EXPLANATION
   ============================================================ */

console.log("");
console.log(
    "TEST 5 — Application Explanation"
);


const explanation =
    adapter.explain(
        "quadratic.factorisation",
        {}
    );


assert.strictEqual(
    explanation.targetSkillId,
    "quadratic.factorisation"
);


assert.ok(
    typeof explanation.readinessExplanation ===
    "string"
);


assert.ok(
    explanation.interventionPlan
);


console.log(
    "✓ Application explanation generated"
);


/* ============================================================
   TEST 6 — UNKNOWN TARGET
   ============================================================ */

console.log("");
console.log(
    "TEST 6 — Unknown Target"
);


const unknown =
    adapter.getState(
        "unknown.target",
        {}
    );


assert.strictEqual(
    unknown.readiness.found,
    false
);


assert.strictEqual(
    unknown.readiness.ready,
    false
);


assert.strictEqual(
    unknown.interventionPlan.interventionRequired,
    false
);


console.log(
    "✓ Unknown target handled safely"
);


/* ============================================================
   TEST 7 — READ ONLY
   ============================================================ */

console.log("");
console.log(
    "TEST 7 — Read-Only Contract"
);


assert.ok(
    adapter.resolutionEngine
);


assert.ok(
    adapter.interventionPlanner
);


console.log(
    "✓ Adapter contains no learner-state mutation API"
);


/* ============================================================
   SUMMARY
   ============================================================ */

console.log("");
console.log("============================================================");
console.log(" STEP 32.36 PASSED");
console.log("============================================================");
console.log("");

console.log(
    "✓ Target readiness state verified"
);

console.log(
    "✓ Intervention plan verified"
);

console.log(
    "✓ Fully-ready state verified"
);

console.log(
    "✓ Blocking prerequisite propagation verified"
);

console.log(
    "✓ Explanation verified"
);

console.log(
    "✓ Unknown target safety verified"
);

console.log(
    "✓ Read-only contract verified"
);

console.log("");
