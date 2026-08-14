/**
 * STEP 32.47
 *
 * Readiness Question Generator Contract Test
 */

import assert from "assert";


import {
    ReadinessQuestionGenerator
} from "./readiness-question-generator.js";


console.log("");
console.log("============================================================");
console.log(" STEP 32.47 — READINESS QUESTION GENERATOR TEST");
console.log("============================================================");
console.log("");


const generator =
    new ReadinessQuestionGenerator({

        minimumPoolSize:
            10,

        recommendedPoolSize:
            15,

        diagnosticSelectionCount:
            5
    });


console.log(
    "✓ Generator contract created"
);


/* ============================================================
   TEST 1 — NORMALIZE
   ============================================================ */

console.log("");
console.log(
    "TEST 1 — Question Normalization"
);


const rawQuestion = {

    id:
        "readiness.arithmetic.sign-rules.diagnostic.001",

    questionType:
        "mcq",

    topicId:
        "arithmetic",

    conceptId:
        "arithmetic-sign-rules",

    skillIds: [
        "arithmetic.sign-rules"
    ],

    readinessSkillId:
        "arithmetic.sign-rules",

    role:
        "diagnostic",

    difficulty:
        "basic",

    questionText:
        "Which statement correctly describes the sign of the product of a positive and a negative number?",

    correctAnswer:
        "negative",

    explanation:
        "A positive number multiplied by a negative number gives a negative result."
};


const normalized =
    generator.normalizeQuestion(
        rawQuestion
    );


assert.strictEqual(
    normalized.readinessSkillId,
    "arithmetic.sign-rules"
);


assert.ok(
    normalized.skillIds.includes(
        "arithmetic.sign-rules"
    )
);


console.log(
    "✓ Question normalized"
);


/* ============================================================
   TEST 2 — VALID QUESTION
   ============================================================ */

console.log("");
console.log(
    "TEST 2 — Question Validation"
);


const validation =
    generator.validateQuestion(
        normalized
    );


assert.strictEqual(
    validation.valid,
    true
);


assert.strictEqual(
    validation.errors.length,
    0
);


console.log(
    "✓ Valid readiness question accepted"
);


/* ============================================================
   TEST 3 — WRONG SKILL REJECTION
   ============================================================ */

console.log("");
console.log(
    "TEST 3 — Exact Skill Enforcement"
);


const wrongSkill = {

    ...normalized,

    id:
        "wrong-skill-question",

    readinessSkillId:
        "arithmetic.hcf",

    skillIds: [
        "arithmetic.sign-rules"
    ]
};


const wrongValidation =
    generator.validateQuestion(
        wrongSkill
    );


assert.strictEqual(
    wrongValidation.valid,
    false
);


console.log(
    "✓ Wrong readiness skill rejected"
);


/* ============================================================
   TEST 4 — DUPLICATE IDS
   ============================================================ */

console.log("");
console.log(
    "TEST 4 — Duplicate Question IDs"
);


const duplicatePool = [

    normalized,

    {
        ...normalized
    }
];


const duplicateResult =
    generator.validatePool(
        duplicatePool,
        "arithmetic.sign-rules"
    );


assert.strictEqual(
    duplicateResult.valid,
    false
);


assert.ok(
    duplicateResult.errors.some(
        error =>
            error.includes(
                "Duplicate question ID"
            )
    )
);


console.log(
    "✓ Duplicate question IDs rejected"
);


/* ============================================================
   TEST 5 — INSUFFICIENT POOL
   ============================================================ */

console.log("");
console.log(
    "TEST 5 — Insufficient Pool"
);


const insufficient =
    generator.validatePool(
        [
            normalized
        ],
        "arithmetic.sign-rules"
    );


assert.strictEqual(
    insufficient.valid,
    false
);


assert.strictEqual(
    insufficient.exactSkillCount,
    1
);


assert.strictEqual(
    insufficient.diagnosticCount,
    1
);


console.log(
    "✓ Small readiness pool correctly rejected"
);


/* ============================================================
   TEST 6 — VALID POOL
   ============================================================ */

console.log("");
console.log(
    "TEST 6 — Valid Diagnostic Pool"
);


const validPool = [];


for (
    let i = 1;
    i <= 10;
    i++
) {

    validPool.push({

        ...normalized,

        id:
            `readiness.arithmetic.sign-rules.diagnostic.${String(i).padStart(3, "0")}`,

        difficulty:
            i <= 3
                ? "basic"
                : i <= 6
                    ? "standard"
                    : "intermediate"
    });
}


const validPoolResult =
    generator.validatePool(
        validPool,
        "arithmetic.sign-rules"
    );


assert.strictEqual(
    validPoolResult.valid,
    true
);


assert.strictEqual(
    validPoolResult.exactSkillCount,
    10
);


assert.strictEqual(
    validPoolResult.diagnosticCount,
    10
);


assert.strictEqual(
    validPoolResult.difficultyCounts.basic,
    3
);


assert.strictEqual(
    validPoolResult.difficultyCounts.standard,
    3
);


assert.strictEqual(
    validPoolResult.difficultyCounts.intermediate,
    4
);


console.log(
    "✓ Ten-question exact-skill pool accepted"
);


/* ============================================================
   TEST 7 — SPECIFICATION
   ============================================================ */

console.log("");
console.log(
    "TEST 7 — Generation Specification"
);


const specification =
    generator.buildSpecification({

        id:
            "arithmetic.sign-rules",

        name:
            "Sign rules"
    });


assert.strictEqual(
    specification.readinessSkillId,
    "arithmetic.sign-rules"
);


assert.strictEqual(
    specification.exactSkillRequired,
    true
);


assert.ok(
    specification.requiredFields.includes(
        "readinessSkillId"
    )
);


assert.ok(
    specification.requiredFields.includes(
        "skillIds"
    )
);


console.log(
    "✓ Generation specification created"
);


/* ============================================================
   TEST 8 — COVERAGE RECORD
   ============================================================ */

console.log("");
console.log(
    "TEST 8 — Coverage Record"
);


const coverage =
    generator.createCoverageRecord(
        "arithmetic.sign-rules",
        validPool
    );


assert.strictEqual(
    coverage.questionCount,
    10
);


assert.strictEqual(
    coverage.missing,
    0
);


assert.strictEqual(
    coverage.status,
    "READY"
);


console.log(
    "✓ Coverage record generated"
);


/* ============================================================
   TEST 9 — REMEDIATION ROLE
   ============================================================ */

console.log("");
console.log(
    "TEST 9 — Remediation Role"
);


const remediationQuestion = {

    ...normalized,

    id:
        "readiness.arithmetic.sign-rules.remediation.001",

    role:
        "remediation"
};


const remediationValidation =
    generator.validateQuestion(
        remediationQuestion
    );


assert.strictEqual(
    remediationValidation.valid,
    true
);


console.log(
    "✓ Remediation question accepted"
);


/* ============================================================
   TEST 10 — QUESTION ID STABILITY
   ============================================================ */

console.log("");
console.log(
    "TEST 10 — Stable IDs"
);


assert.strictEqual(
    normalized.id,
    "readiness.arithmetic.sign-rules.diagnostic.001"
);


console.log(
    "✓ Stable readiness question ID contract verified"
);


/* ============================================================
   SUMMARY
   ============================================================ */

console.log("");
console.log("============================================================");
console.log(" STEP 32.47 PASSED");
console.log("============================================================");
console.log("");

console.log(
    "✓ Question normalization"
);

console.log(
    "✓ Question validation"
);

console.log(
    "✓ Exact readiness skill enforcement"
);

console.log(
    "✓ Duplicate ID detection"
);

console.log(
    "✓ Minimum pool validation"
);

console.log(
    "✓ Valid pool validation"
);

console.log(
    "✓ Generation specification"
);

console.log(
    "✓ Coverage reporting"
);

console.log(
    "✓ Remediation role"
);

console.log(
    "✓ Stable question IDs"
);

console.log("");
