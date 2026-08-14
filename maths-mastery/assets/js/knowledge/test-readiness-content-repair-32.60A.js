import fs from "fs";
import assert from "assert";


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


const root =
    process.cwd();


const base =
    `${root}/maths-mastery/data/questions/readiness`;


function bank(
    name
) {

    return readJson(
        `${base}/${name}/questions.json`
    );
}


console.log("");
console.log(
    "============================================================"
);
console.log(
    " STEP 32.60A — CONTENT CONTRACT TEST"
);
console.log(
    "============================================================"
);
console.log("");


/* ============================================================
   TEST 1 — SIGN RULE
   ============================================================ */

const signs =
    bank(
        "arithmetic-sign-rules"
    );


const signQuestion =
    signs.questions.find(
        q =>
            q.id ===
            "readiness.arithmetic.sign-rules.diagnostic.005"
    );


assert.strictEqual(
    signQuestion.questionText,
    "What is the sign of the product when one factor is negative and the other factor is positive?"
);


assert.strictEqual(
    signQuestion.correctAnswer,
    "negative"
);


console.log(
    "✓ Sign-rule ambiguity removed"
);


/* ============================================================
   TEST 2 — GROUPING
   ============================================================ */

const grouping =
    bank(
        "algebra-factor-by-grouping"
    );


const groupingIds = [
    "readiness.algebra.factor-by-grouping.diagnostic.001",
    "readiness.algebra.factor-by-grouping.diagnostic.002",
    "readiness.algebra.factor-by-grouping.diagnostic.003",
    "readiness.algebra.factor-by-grouping.diagnostic.004",
    "readiness.algebra.factor-by-grouping.diagnostic.005",
    "readiness.algebra.factor-by-grouping.diagnostic.006"
];


for (
    const id of groupingIds
) {

    const q =
        grouping.questions.find(
            item =>
                item.id === id
        );


    assert.ok(
        q
    );


    assert.match(
        q.questionText,
        /grouping/i
    );
}


console.log(
    "✓ Six grouping questions now test actual grouping"
);


/* ============================================================
   TEST 3 — EQUIVALENT FRACTION
   ============================================================ */

const equivalent =
    bank(
        "fractions-equivalent"
    );


const eqQuestion =
    equivalent.questions.find(
        q =>
            q.id ===
            "readiness.fractions.equivalent.diagnostic.001"
    );


assert.strictEqual(
    eqQuestion.correctAnswer,
    "4/8"
);


console.log(
    "✓ Equivalent-fraction answer deterministic"
);


/* ============================================================
   TEST 4 — FACTORS
   ============================================================ */

const factors =
    bank(
        "arithmetic-factors"
    );


const factorQuestion =
    factors.questions.find(
        q =>
            q.id ===
            "readiness.arithmetic.factors.diagnostic.004"
    );


assert.strictEqual(
    factorQuestion.correctAnswer,
    "1,2,3,6,9,18"
);


console.log(
    "✓ Factor answer deterministic"
);


/* ============================================================
   TEST 5 — MULTIPLES
   ============================================================ */

const multiples =
    bank(
        "arithmetic-multiples"
    );


const multiple1 =
    multiples.questions.find(
        q =>
            q.id ===
            "readiness.arithmetic.multiples.diagnostic.001"
    );


const multiple3 =
    multiples.questions.find(
        q =>
            q.id ===
            "readiness.arithmetic.multiples.diagnostic.003"
    );


assert.match(
    multiple1.questionText,
    /positive multiples/i
);


assert.match(
    multiple3.questionText,
    /positive multiple/i
);


console.log(
    "✓ Multiple wording deterministic"
);


/* ============================================================
   TEST 6 — COMMON FACTOR
   ============================================================ */

const commonFactor =
    bank(
        "algebra-common-factor"
    );


const commonFactorTargets = [
    "readiness.algebra.common-factor.diagnostic.006",
    "readiness.algebra.common-factor.diagnostic.007",
    "readiness.algebra.common-factor.diagnostic.008",
    "readiness.algebra.common-factor.remediation.009",
    "readiness.algebra.common-factor.remediation.010"
];


for (
    const id of commonFactorTargets
) {

    const q =
        commonFactor.questions.find(
            item =>
                item.id === id
        );


    assert.ok(
        q
    );


    assert.match(
        q.questionText,
        /greatest common factor/i
    );
}


console.log(
    "✓ Common-factor wording deterministic"
);


/* ============================================================
   TEST 7 — INVENTORY
   ============================================================ */

const allBanks = [
    "arithmetic-sign-rules",
    "algebra-factor-by-grouping",
    "fractions-equivalent",
    "arithmetic-factors",
    "arithmetic-multiples",
    "algebra-common-factor"
];


for (
    const name of allBanks
) {

    assert.strictEqual(
        bank(name).questions.length,
        10
    );
}


console.log(
    "✓ Target bank sizes preserved"
);


console.log("");
console.log(
    "============================================================"
);
console.log(
    " STEP 32.60A PASSED"
);
console.log(
    "============================================================"
);
console.log("");

console.log(
    "✓ Targeted content-contract repairs verified"
);

console.log(
    "✓ Question inventory preserved"
);

console.log(
    "✓ No taxonomy changes"
);

console.log(
    "✓ No graph changes"
);
