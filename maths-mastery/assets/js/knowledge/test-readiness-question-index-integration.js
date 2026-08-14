/**
 * STEP 32.50B
 *
 * Readiness Question Index Integration Test
 *
 * READ-ONLY AGAINST THE QUESTION INDEX SNAPSHOT PASSED
 * TO THE TEST.
 */

import assert from "assert";
import fs from "fs";


function readJson(
    file
) {

    const raw =
        fs.readFileSync(
            file,
            "utf8"
        );


    return JSON.parse(
        raw.replace(
            /^\uFEFF/,
            ""
        )
    );
}


const indexFile =
    process.argv[2];


if (
    !indexFile
) {

    throw new Error(
        "question-index.json path required."
    );
}


const index =
    readJson(
        indexFile
    );


const entities =
    Object.values(
        index.entities || {}
    );


console.log("");
console.log(
    "============================================================"
);
console.log(
    " STEP 32.50B — QUESTION INDEX CONTRACT TEST"
);
console.log(
    "============================================================"
);
console.log("");


/* ============================================================
   TEST 1 — INDEX EXISTS
   ============================================================ */

console.log(
    "TEST 1 — Question Index"
);


assert.ok(
    index.entities
);


assert.ok(
    index.bySkill
);


console.log(
    "✓ Question index structure valid"
);


/* ============================================================
   TEST 2 — READINESS ENTITY COUNT
   ============================================================ */

console.log("");
console.log(
    "TEST 2 — Readiness Entities"
);


const readiness =
    entities.filter(
        entity =>
            entity.source ===
            "readiness"
    );


assert.strictEqual(
    readiness.length,
    510
);


console.log(
    `✓ Readiness entities: ${readiness.length}`
);


/* ============================================================
   TEST 3 — EXACT READINESS SKILLS
   ============================================================ */

console.log("");
console.log(
    "TEST 3 — Exact Readiness Skills"
);


const targetSkills =
    new Set([
        "arithmetic.sign-rules",
        "arithmetic.add-integers",
        "arithmetic.multiply-integers",
        "arithmetic.divide-integers",
        "arithmetic.hcf",
        "algebra.negative-brackets",
        "algebra.common-numerical-factor",
        "algebra.common-variable-factor",
        "algebra.common-factor",
        "algebra.distributive-property",
        "algebra.expand-binomial",
        "algebra.like-terms",
        "algebra.combine-like-terms"
    ]);


for (
    const skillId
    of targetSkills
) {

    const ids =
        index.bySkill?.[
            skillId
        ] ||
        [];


    const readinessForSkill =
        readiness.filter(
            entity =>
                entity.data?.readinessSkillId ===
                skillId
        );


    assert.strictEqual(
        readinessForSkill.length,
        10
    );


    assert.ok(
        ids.length >= 10
    );
}


console.log(
    "✓ All 13 readiness skills indexed"
);


/* ============================================================
   TEST 4 — EXISTING QUESTIONS PRESERVED
   ============================================================ */

console.log("");
console.log(
    "TEST 4 — Existing Entities Preserved"
);


const nonReadiness =
    entities.filter(
        entity =>
            entity.source !==
            "readiness"
    );


assert.ok(
    nonReadiness.length >
    0
);


console.log(
    `✓ Existing entities preserved: ${nonReadiness.length}`
);


/* ============================================================
   TEST 5 — QUESTION DATA SHAPE
   ============================================================ */

console.log("");
console.log(
    "TEST 5 — Question Data Shape"
);


for (
    const entity
    of readiness
) {

    const question =
        entity.data;


    assert.ok(
        question.id
    );


    assert.ok(
        question.topicId
    );


    assert.ok(
        question.conceptId
    );


    assert.ok(
        Array.isArray(
            question.skillIds
        )
    );


    assert.ok(
        question.skillIds.includes(
            question.readinessSkillId
        )
    );
}


console.log(
    "✓ Readiness question data shape valid"
);


/* ============================================================
   TEST 6 — NO DUPLICATE IDs
   ============================================================ */

console.log("");
console.log(
    "TEST 6 — Duplicate IDs"
);


const ids =
    entities.map(
        entity =>
            entity.id
    );


assert.strictEqual(
    new Set(
        ids
    ).size,
    ids.length
);


console.log(
    "✓ Question IDs remain unique"
);


/* ============================================================
   SUMMARY
   ============================================================ */

console.log("");
console.log(
    "============================================================"
);
console.log(
    " STEP 32.50B PASSED"
);
console.log(
    "============================================================"
);
console.log("");

console.log(
    "✓ Readiness entities indexed"
);

console.log(
    "✓ Skill lookups rebuilt"
);

console.log(
    "✓ Existing entities preserved"
);

console.log(
    "✓ Exact readinessSkillId preserved"
);

console.log(
    "✓ Question schema preserved"
);

console.log(
    "✓ Duplicate IDs rejected"
);
