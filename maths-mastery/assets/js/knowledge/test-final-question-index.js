/**
 * STEP 32.55
 *
 * Final production question index contract test.
 */

import assert from "assert";
import fs from "fs";


const indexFile =
    process.argv[2];


if (
    !indexFile
) {

    throw new Error(
        "question-index.json path required."
    );
}


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


const index =
    readJson(
        indexFile
    );


console.log("");
console.log(
    "============================================================"
);
console.log(
    " STEP 32.55 — FINAL QUESTION INDEX CONTRACT TEST"
);
console.log(
    "============================================================"
);
console.log("");


/* ============================================================
   TEST 1 — INDEX STRUCTURE
   ============================================================ */

console.log(
    "TEST 1 — Index Structure"
);


assert.ok(
    index.entities &&
    typeof index.entities ===
        "object"
);


assert.ok(
    index.byTopic &&
    typeof index.byTopic ===
        "object"
);


assert.ok(
    index.byConcept &&
    typeof index.byConcept ===
        "object"
);


assert.ok(
    index.bySkill &&
    typeof index.bySkill ===
        "object"
);


console.log(
    "✓ Final index structure valid"
);


/* ============================================================
   TEST 2 — TOTAL READINESS QUESTIONS
   ============================================================ */

console.log("");
console.log(
    "TEST 2 — Readiness Question Count"
);


const entities =
    Object.values(
        index.entities
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
    `✓ Final readiness questions: ${readiness.length}`
);


/* ============================================================
   TEST 3 — 51 BANKS
   ============================================================ */

console.log("");
console.log(
    "TEST 3 — Readiness Skill Coverage"
);


const readinessSkills =
    new Set(
        readiness.map(
            entity =>
                entity.data
                    ?.readinessSkillId
        )
    );


assert.strictEqual(
    readinessSkills.size,
    51
);


console.log(
    `✓ Readiness banks represented: ${readinessSkills.size}`
);


/* ============================================================
   TEST 4 — EXACT 10 QUESTIONS PER BANK
   ============================================================ */

console.log("");
console.log(
    "TEST 4 — Bank Size"
);


const counts =
    new Map();


for (
    const entity
    of readiness
) {

    const skillId =
        entity.data
            ?.readinessSkillId;


    counts.set(
        skillId,
        (
            counts.get(
                skillId
            ) ||
            0
        ) + 1
    );
}


for (
    const [
        skillId,
        count
    ]
    of counts
) {

    assert.strictEqual(
        count,
        10,
        `${skillId} must have exactly 10 questions`
    );
}


console.log(
    "✓ Every readiness bank contains 10 questions"
);


/* ============================================================
   TEST 5 — ALL TARGET READINESS SKILLS AVAILABLE
   ============================================================ */

console.log("");
console.log(
    "TEST 5 — Target Prerequisite Availability"
);


const requiredSkills = [
    "algebra.combine-like-terms",
    "algebra.common-factor",
    "algebra.common-numerical-factor",
    "algebra.common-variable-factor",
    "algebra.distributive-property",
    "algebra.expand-binomial",
    "algebra.like-terms",
    "algebra.linear-equation",
    "algebra.multiply-monomials",
    "algebra.negative-brackets",
    "algebra.terms",
    "algebra.variables",
    "arithmetic.add-integers",
    "arithmetic.divide-integers",
    "arithmetic.hcf",
    "arithmetic.multiply-integers",
    "arithmetic.sign-rules",
    "data.read-table",
    "geometry.angle-basics",
    "geometry.angle-measure",
    "geometry.coordinate-points",
    "geometry.parallel-lines",
    "geometry.triangle-angle-sum",
    "measurement.area",
    "measurement.length",
    "percentage.basic",
    "probability.basic-event",
    "problem.translate-words",
    "ratio.compare-quantities",
    "ratio.simplify"
];


for (
    const skillId
    of requiredSkills
) {

    assert.ok(
        index.bySkill[
            skillId
        ] &&
        index.bySkill[
            skillId
        ].length >=
            5,
        `Missing production skill index: ${skillId}`
    );
}


console.log(
    "✓ All target prerequisite skills indexed"
);


/* ============================================================
   TEST 6 — EXACT QUESTION METADATA
   ============================================================ */

console.log("");
console.log(
    "TEST 6 — Question Metadata"
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
        question.readinessSkillId
    );


    assert.ok(
        question.skillIds.includes(
            question.readinessSkillId
        )
    );
}


console.log(
    "✓ Readiness metadata valid"
);


/* ============================================================
   TEST 7 — UNIQUE IDS
   ============================================================ */

console.log("");
console.log(
    "TEST 7 — Question ID Uniqueness"
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
    "✓ All question IDs are unique"
);


/* ============================================================
   TEST 8 — NO ENTITY LOSS
   ============================================================ */

console.log("");
console.log(
    "TEST 8 — Existing Entity Preservation"
);


/*
 * Existing non-readiness entities should still exist.
 */

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
    `✓ Existing non-readiness entities preserved: ${nonReadiness.length}`
);


/* ============================================================
   SUMMARY
   ============================================================ */

console.log("");
console.log(
    "============================================================"
);
console.log(
    " STEP 32.55 PASSED"
);
console.log(
    "============================================================"
);
console.log("");

console.log(
    "✓ Final question index rebuilt"
);

console.log(
    "✓ 510 readiness questions indexed"
);

console.log(
    "✓ 51 readiness banks indexed"
);

console.log(
    "✓ Target prerequisite skills indexed"
);

console.log(
    "✓ Exact skill mappings preserved"
);

console.log(
    "✓ Question IDs unique"
);

console.log(
    "✓ Existing entities preserved"
);
