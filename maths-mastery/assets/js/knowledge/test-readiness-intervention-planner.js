/**
 * STEP 32.35
 * Readiness Intervention Planner Contract Test
 */

import assert from "assert";

import {
    ReadinessInterventionPlanner
} from "./readiness-intervention-planner.js";


console.log("");
console.log("============================================================");
console.log(" STEP 32.35 — INTERVENTION PLANNER CONTRACT TEST");
console.log("============================================================");
console.log("");


const planner =
    new ReadinessInterventionPlanner({
        maxVisibleBlocks:
            3,

        maxVisiblePrerequisites:
            4,

        diagnosticQuestionsPerBlock:
            5
    });


console.log(
    "✓ Planner created"
);


/* ============================================================
   TEST 1 — READY LEARNER
   ============================================================ */

console.log("");
console.log(
    "TEST 1 — Ready Learner"
);


const readyPlan =
    planner.plan({

        found:
            true,

        ready:
            true,

        targetSkillId:
            "quadratic.factorisation",

        missing: [],

        remediationPath: []
    });


assert.strictEqual(
    readyPlan.ready,
    true
);


assert.strictEqual(
    readyPlan.interventionRequired,
    false
);


assert.strictEqual(
    readyPlan.blocks.length,
    0
);


console.log(
    "✓ No intervention for ready learner"
);


/* ============================================================
   TEST 2 — UNREADY LEARNER
   ============================================================ */

console.log("");
console.log(
    "TEST 2 — Unready Learner"
);


const resolution = {

    found:
        true,

    ready:
        false,

    targetSkillId:
        "quadratic.factorisation",

    missing: [

        {
            skillId:
                "algebra.negative-brackets",

            name:
                "Handle negative signs before brackets",

            level:
                "basic",

            requirement:
                "core",

            direct:
                true,

            depth:
                0
        },

        {
            skillId:
                "arithmetic.sign-rules",

            name:
                "Apply positive and negative sign rules",

            level:
                "foundation",

            requirement:
                "prerequisite",

            direct:
                false,

            depth:
                1
        },

        {
            skillId:
                "algebra.common-factor",

            name:
                "Extract a common factor",

            level:
                "elementary",

            requirement:
                "core",

            direct:
                true,

            depth:
                0
        },

        {
            skillId:
                "arithmetic.hcf",

            name:
                "Find HCF",

            level:
                "basic",

            requirement:
                "prerequisite",

            direct:
                false,

            depth:
                1
        }
    ],

    remediationPath: [

        {
            step:
                1,

            skillId:
                "arithmetic.sign-rules",

            name:
                "Apply positive and negative sign rules",

            level:
                "foundation",

            requirement:
                "prerequisite",

            direct:
                false,

            depth:
                1
        },

        {
            step:
                2,

            skillId:
                "algebra.negative-brackets",

            name:
                "Handle negative signs before brackets",

            level:
                "basic",

            requirement:
                "core",

            direct:
                true,

            depth:
                0
        },

        {
            step:
                3,

            skillId:
                "arithmetic.hcf",

            name:
                "Find HCF",

            level:
                "basic",

            requirement:
                "prerequisite",

            direct:
                false,

            depth:
                1
        },

        {
            step:
                4,

            skillId:
                "algebra.common-factor",

            name:
                "Extract a common factor",

            level:
                "elementary",

            requirement:
                "core",

            direct:
                true,

            depth:
                0
        }
    ]
};


const plan =
    planner.plan(
        resolution
    );


assert.strictEqual(
    plan.found,
    true
);


assert.strictEqual(
    plan.ready,
    false
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
    `✓ Intervention blocks created: ${plan.blocks.length}`
);


/* ============================================================
   TEST 3 — BLOCK STRUCTURE
   ============================================================ */

console.log("");
console.log(
    "TEST 3 — Block Structure"
);


for (
    const block
    of plan.blocks
) {

    assert.ok(
        block.id
    );

    assert.ok(
        block.skillId
    );

    assert.ok(
        block.title
    );

    assert.ok(
        block.diagnostic
    );

    assert.strictEqual(
        block.diagnostic.questionCount,
        5
    );

    assert.ok(
        block.action
    );

    assert.strictEqual(
        block.action.type,
        "remediate"
    );

    assert.strictEqual(
        block.action.returnToTargetAfterCompletion,
        true
    );
}


console.log(
    "✓ Block contract valid"
);


/* ============================================================
   TEST 4 — DEEP PREREQUISITES
   ============================================================ */

console.log("");
console.log(
    "TEST 4 — Supporting Prerequisites"
);


const negativeBlock =
    plan.blocks.find(
        block =>
            block.skillId ===
            "algebra.negative-brackets"
    );


assert.ok(
    negativeBlock
);


assert.ok(
    negativeBlock.supportingPrerequisites
        .some(
            item =>
                item.skillId ===
                "arithmetic.sign-rules"
        )
);


console.log(
    "✓ Deep prerequisite surfaced as supporting context"
);


/* ============================================================
   TEST 5 — LIMITS
   ============================================================ */

console.log("");
console.log(
    "TEST 5 — Visible Intervention Limits"
);


assert.ok(
    plan.blocks.length <= 3
);


for (
    const block
    of plan.blocks
) {

    assert.ok(
        block.supportingPrerequisites.length <= 4
    );
}


console.log(
    "✓ Learner-facing complexity limits respected"
);


/* ============================================================
   TEST 6 — EXPLANATION
   ============================================================ */

console.log("");
console.log(
    "TEST 6 — Explanation"
);


assert.ok(
    typeof plan.explanation ===
    "string"
);


assert.ok(
    plan.explanation.length >
    0
);


console.log(
    "✓ Learner explanation generated"
);


/* ============================================================
   TEST 7 — UNKNOWN RESOLUTION
   ============================================================ */

console.log("");
console.log(
    "TEST 7 — Missing Resolution"
);


const missingResolutionPlan =
    planner.plan({

        found:
            false,

        ready:
            false,

        targetSkillId:
            "unknown-target"
    });


assert.strictEqual(
    missingResolutionPlan.interventionRequired,
    false
);


assert.strictEqual(
    missingResolutionPlan.blocks.length,
    0
);


console.log(
    "✓ Missing resolution handled safely"
);


/* ============================================================
   SUMMARY
   ============================================================ */

console.log("");
console.log("============================================================");
console.log(" STEP 32.35 PASSED");
console.log("============================================================");
console.log("");

console.log(
    "✓ Ready learner handling verified"
);

console.log(
    "✓ Unready learner handling verified"
);

console.log(
    "✓ Intervention block generation verified"
);

console.log(
    "✓ Supporting prerequisite surfacing verified"
);

console.log(
    "✓ Learner-facing limits verified"
);

console.log(
    "✓ Explanation verified"
);

console.log(
    "✓ Unknown resolution handling verified"
);

console.log("");
