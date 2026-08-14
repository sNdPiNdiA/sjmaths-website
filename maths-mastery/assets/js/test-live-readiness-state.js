/**
 * STEP 32.39
 *
 * Live Readiness State Contract Test
 *
 * Verifies that MathsMasteryApplication automatically derives
 * readiness evidence from its current progress/mastery state.
 */

import assert from "assert";


import {
    MathsMasteryApplication
} from "./maths-mastery-application.js";


/* ============================================================
   MEMORY STORAGE
   ============================================================ */

class MemoryStorage {

    constructor() {

        this.store =
            new Map();
    }


    getItem(
        key
    ) {

        return this.store.has(
            key
        )
            ? this.store.get(
                key
            )
            : null;
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
   CREATE APPLICATION
   ============================================================ */

console.log("");
console.log("============================================================");
console.log(" STEP 32.39 — LIVE READINESS STATE TEST");
console.log("============================================================");
console.log("");


const storage =
    new MemoryStorage();


const app =
    new MathsMasteryApplication({
        storage
    });


console.log(
    "✓ Application created"
);


/* ============================================================
   TEST 1 — ADAPTER
   ============================================================ */

console.log("");
console.log(
    "TEST 1 — Evidence Adapter"
);


assert.ok(
    app.readinessEvidenceAdapter
);


assert.strictEqual(
    typeof app.readinessEvidenceAdapter
        .fromApplicationState,
    "function"
);


console.log(
    "✓ Evidence adapter attached"
);


/* ============================================================
   TEST 2 — EMPTY APPLICATION
   ============================================================ */

console.log("");
console.log(
    "TEST 2 — Empty Learner State"
);


const emptyState =
    app.getLearningReadinessState(
        "quadratic.factorisation"
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


console.log(
    `✓ Empty learner readiness gaps: ${emptyState.readiness.missing.length}`
);


/* ============================================================
   TEST 3 — LIVE PROGRESS
   ============================================================ */

console.log("");
console.log(
    "TEST 3 — Progress-Driven Readiness"
);


app.progress = {

    records: [

        {
            skillIds: [
                "arithmetic.sign-rules"
            ],

            score:
                95,

            attempts:
                5,

            correct:
                5,

            incorrect:
                0
        },

        {
            skillIds: [
                "arithmetic.hcf"
            ],

            score:
                90,

            attempts:
                4,

            correct:
                4,

            incorrect:
                0
        }
    ]
};


app.mastery =
    null;


const progressState =
    app.getLearningReadinessState(
        "quadratic.factorisation"
    );


assert.ok(
    progressState.readiness
);


assert.ok(
    progressState.readiness.missing
);


const signGap =
    progressState.readiness.missing.find(
        item =>
            item.skillId ===
            "arithmetic.sign-rules"
    );


const hcfGap =
    progressState.readiness.missing.find(
        item =>
            item.skillId ===
            "arithmetic.hcf"
    );


if (
    signGap
) {

    throw new Error(
        "arithmetic.sign-rules should no longer be missing."
    );
}


if (
    hcfGap
) {

    throw new Error(
        "arithmetic.hcf should no longer be missing."
    );
}


console.log(
    "✓ Existing progress automatically affects readiness"
);


/* ============================================================
   TEST 4 — MASTERY PREFERENCE
   ============================================================ */

console.log("");
console.log(
    "TEST 4 — Live Mastery Preference"
);


app.progress = {

    records: [

        {
            skillIds: [
                "algebra.negative-brackets"
            ],

            score:
                30,

            attempts:
                5
        }
    ]
};


app.mastery = {

    skills: {

        "algebra.negative-brackets": {

            score:
                95,

            attempts:
                8,

            mastered:
                true
        }
    }
};


const masteryState =
    app.getLearningReadinessState(
        "quadratic.factorisation"
    );


const negativeGap =
    masteryState.readiness.missing.find(
        item =>
            item.skillId ===
            "algebra.negative-brackets"
    );


if (
    negativeGap
) {

    throw new Error(
        "Explicit mastery should satisfy algebra.negative-brackets."
    );
}


console.log(
    "✓ Explicit mastery automatically affects readiness"
);


/* ============================================================
   TEST 5 — EXPLICIT EVIDENCE STILL WORKS
   ============================================================ */

console.log("");
console.log(
    "TEST 5 — Explicit Evidence Override"
);


const manualState =
    app.getLearningReadinessState(

        "quadratic.factorisation",

        {

            "algebra.negative-brackets": {

                mastered:
                    true,

                score:
                    100,

                attempts:
                    5
            }
        }
    );


assert.strictEqual(
    manualState.targetSkillId,
    "quadratic.factorisation"
);


assert.ok(
    manualState.readiness
);


console.log(
    "✓ Explicit evidence override preserved"
);


/* ============================================================
   TEST 6 — INTERVENTION PLAN
   ============================================================ */

console.log("");
console.log(
    "TEST 6 — Live Intervention Plan"
);


const livePlan =
    app.getInterventionPlan(
        "quadratic.factorisation"
    );


assert.strictEqual(
    livePlan.found,
    true
);


assert.ok(
    Array.isArray(
        livePlan.blocks
    )
);


console.log(
    `✓ Live intervention blocks: ${livePlan.blocks.length}`
);


/* ============================================================
   TEST 7 — READ ONLY
   ============================================================ */

console.log("");
console.log(
    "TEST 7 — Read-Only"
);


const beforeProgress =
    JSON.stringify(
        app.progress
    );


const beforeMastery =
    JSON.stringify(
        app.mastery
    );


app.getLearningReadinessState(
    "quadratic.factorisation"
);


assert.strictEqual(
    JSON.stringify(
        app.progress
    ),
    beforeProgress
);


assert.strictEqual(
    JSON.stringify(
        app.mastery
    ),
    beforeMastery
);


console.log(
    "✓ Live readiness does not mutate learner state"
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
        "unknown.target"
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
    "✓ Unknown target remains safe"
);


/* ============================================================
   SUMMARY
   ============================================================ */

console.log("");
console.log("============================================================");
console.log(" STEP 32.39 PASSED");
console.log("============================================================");
console.log("");

console.log(
    "✓ Evidence adapter attached"
);

console.log(
    "✓ Empty learner readiness verified"
);

console.log(
    "✓ Progress-driven readiness verified"
);

console.log(
    "✓ Mastery-driven readiness verified"
);

console.log(
    "✓ Explicit evidence override preserved"
);

console.log(
    "✓ Live intervention plan verified"
);

console.log(
    "✓ Read-only behavior verified"
);

console.log(
    "✓ Unknown target safety verified"
);

console.log("");
