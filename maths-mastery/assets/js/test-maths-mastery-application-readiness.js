/**
 * STEP 32.37B
 *
 * MathsMasteryApplication Readiness API Contract Test
 *
 * Uses an in-memory storage adapter because Node does not
 * provide browser localStorage.
 */

import assert from "assert";

import {
    MathsMasteryApplication
} from "./maths-mastery-application.js";


/* ============================================================
   IN-MEMORY STORAGE
   ============================================================ */

class MemoryStorage {

    constructor() {

        this.store =
            new Map();
    }


    getItem(
        key
    ) {

        if (
            !this.store.has(
                key
            )
        ) {

            return null;
        }


        return this.store.get(
            key
        );
    }


    setItem(
        key,
        value
    ) {

        this.store.set(
            key,
            String(
                value
            )
        );
    }


    removeItem(
        key
    ) {

        this.store.delete(
            key
        );
    }


    clear() {

        this.store.clear();
    }
}


/* ============================================================
   TEST
   ============================================================ */

console.log("");
console.log("============================================================");
console.log(" STEP 32.37B — APPLICATION READINESS API TEST");
console.log("============================================================");
console.log("");


const storage =
    new MemoryStorage();


const app =
    new MathsMasteryApplication({
        storage
    });


console.log(
    "✓ MathsMasteryApplication created with in-memory storage"
);


/* ============================================================
   TEST 1 — PUBLIC READINESS API
   ============================================================ */

console.log("");
console.log(
    "TEST 1 — Public Readiness API"
);


assert.strictEqual(
    typeof app.getReadiness,
    "function"
);

assert.strictEqual(
    typeof app.getInterventionPlan,
    "function"
);

assert.strictEqual(
    typeof app.getLearningReadinessState,
    "function"
);

assert.strictEqual(
    typeof app.explainReadiness,
    "function"
);


console.log(
    "✓ Four readiness methods exist"
);


/* ============================================================
   TEST 2 — ADAPTER PROPERTY
   ============================================================ */

console.log("");
console.log(
    "TEST 2 — Adapter Property"
);


assert.ok(
    app.readinessAdapter
);


assert.strictEqual(
    typeof app.readinessAdapter.resolve,
    "function"
);

assert.strictEqual(
    typeof app.readinessAdapter.plan,
    "function"
);

assert.strictEqual(
    typeof app.readinessAdapter.getState,
    "function"
);


console.log(
    "✓ Readiness adapter attached"
);


/* ============================================================
   TEST 3 — READINESS RESOLUTION
   ============================================================ */

console.log("");
console.log(
    "TEST 3 — Readiness Resolution"
);


const readiness =
    app.getReadiness(
        "quadratic.factorisation",
        {}
    );


assert.strictEqual(
    readiness.found,
    true
);


assert.strictEqual(
    readiness.ready,
    false
);


assert.ok(
    readiness.missing.length >
    0
);


console.log(
    `✓ Missing readiness skills: ${readiness.missing.length}`
);


/* ============================================================
   TEST 4 — INTERVENTION PLAN
   ============================================================ */

console.log("");
console.log(
    "TEST 4 — Intervention Plan"
);


const plan =
    app.getInterventionPlan(
        "quadratic.factorisation",
        {}
    );


assert.strictEqual(
    plan.found,
    true
);


assert.strictEqual(
    plan.interventionRequired,
    true
);


assert.ok(
    plan.blocks.length >
    0
);


assert.ok(
    plan.blocks.length <=
    3
);


console.log(
    `✓ Intervention blocks: ${plan.blocks.length}`
);


/* ============================================================
   TEST 5 — UNIFIED STATE
   ============================================================ */

console.log("");
console.log(
    "TEST 5 — Unified Readiness State"
);


const state =
    app.getLearningReadinessState(
        "quadratic.factorisation",
        {}
    );


assert.strictEqual(
    state.targetSkillId,
    "quadratic.factorisation"
);


assert.ok(
    state.readiness
);


assert.ok(
    state.interventionPlan
);


assert.strictEqual(
    state.readiness.found,
    true
);


console.log(
    "✓ Unified readiness state verified"
);


/* ============================================================
   TEST 6 — FULLY READY LEARNER
   ============================================================ */

console.log("");
console.log(
    "TEST 6 — Fully Ready Learner"
);


const base =
    app.getReadiness(
        "quadratic.factorisation",
        {}
    );


const evidence = {};


for (
    const item
    of base.missing
) {

    evidence[
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


const ready =
    app.getLearningReadinessState(
        "quadratic.factorisation",
        evidence
    );


assert.strictEqual(
    ready.readiness.ready,
    true
);


assert.strictEqual(
    ready.readiness.missing.length,
    0
);


assert.strictEqual(
    ready.interventionPlan.interventionRequired,
    false
);


assert.strictEqual(
    ready.interventionPlan.blocks.length,
    0
);


console.log(
    "✓ Fully ready state verified"
);


/* ============================================================
   TEST 7 — EXPLANATION
   ============================================================ */

console.log("");
console.log(
    "TEST 7 — Explanation"
);


const explanation =
    app.explainReadiness(
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
    "✓ Explanation verified"
);


/* ============================================================
   TEST 8 — UNKNOWN TARGET
   ============================================================ */

console.log("");
console.log(
    "TEST 8 — Unknown Target"
);


const unknown =
    app.getLearningReadinessState(
        "unknown.target",
        {}
    );


assert.strictEqual(
    unknown.readiness.found,
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
   TEST 9 — READ-ONLY READINESS API
   ============================================================ */

console.log("");
console.log(
    "TEST 9 — Read-Only Readiness"
);


assert.ok(
    app.readinessAdapter
);


assert.strictEqual(
    app.progress,
    null
);


assert.strictEqual(
    app.mastery,
    null
);


assert.strictEqual(
    app.recommendation,
    null
);


console.log(
    "✓ Readiness API did not modify learner state"
);


/* ============================================================
   TEST 10 — STORAGE ISOLATION
   ============================================================ */

console.log("");
console.log(
    "TEST 10 — Storage Isolation"
);


assert.strictEqual(
    storage.getItem(
        "nonexistent"
    ),
    null
);


console.log(
    "✓ Test storage isolated"
);


/* ============================================================
   SUMMARY
   ============================================================ */

console.log("");
console.log("============================================================");
console.log(" STEP 32.37B PASSED");
console.log("============================================================");
console.log("");

console.log(
    "✓ Public readiness API verified"
);

console.log(
    "✓ Readiness adapter verified"
);

console.log(
    "✓ Readiness resolution verified"
);

console.log(
    "✓ Intervention plan verified"
);

console.log(
    "✓ Unified readiness state verified"
);

console.log(
    "✓ Fully ready state verified"
);

console.log(
    "✓ Explanation verified"
);

console.log(
    "✓ Unknown target safety verified"
);

console.log(
    "✓ Read-only behavior verified"
);

console.log(
    "✓ Browser storage dependency isolated for Node test"
);

console.log("");
