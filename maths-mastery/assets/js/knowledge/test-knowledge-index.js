import fs from "fs";
import path from "path";


const root =
    path.resolve(
        process.cwd(),
        "maths-mastery"
    );


const generated =
    path.join(
        root,
        "data",
        "knowledge",
        "generated"
    );


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


function assert(
    condition,
    message
) {

    if (
        !condition
    ) {

        throw new Error(
            message
        );
    }

    console.log(
        `✓ ${message}`
    );
}


console.log("");
console.log(
    "============================================"
);
console.log(
    " STEP 26 — INDEX VALIDATION"
);
console.log(
    "============================================"
);
console.log("");


/* ============================================================
   Required indexes
   ============================================================ */

const requiredIndexes = [

    "domain-index.json",
    "topic-index.json",
    "concept-index.json",
    "skill-index.json",
    "pattern-index.json",
    "exam-index.json",
    "question-index.json",
    "graph-index.json",
    "build-manifest.json"

];


for (
    const file of
    requiredIndexes
) {

    assert(
        fs.existsSync(
            path.join(
                generated,
                file
            )
        ),
        `${file} exists`
    );
}


/* ============================================================
   Load indexes
   ============================================================ */

const domainIndex =
    readJson(
        path.join(
            generated,
            "domain-index.json"
        )
    );


const topicIndex =
    readJson(
        path.join(
            generated,
            "topic-index.json"
        )
    );


const conceptIndex =
    readJson(
        path.join(
            generated,
            "concept-index.json"
        )
    );


const skillIndex =
    readJson(
        path.join(
            generated,
            "skill-index.json"
        )
    );


const questionIndex =
    readJson(
        path.join(
            generated,
            "question-index.json"
        )
    );


const graphIndex =
    readJson(
        path.join(
            generated,
            "graph-index.json"
        )
    );


const manifest =
    readJson(
        path.join(
            generated,
            "build-manifest.json"
        )
    );


/* ============================================================
   TEST 1 — Topic Index
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 1 — Topic Index"
);
console.log(
    "--------------------------------------------"
);


assert(
    topicIndex.entities[
        "percentage"
    ] !== undefined,
    "Percentage exists in topic index"
);


assert(
    topicIndex.entities[
        "profit-loss"
    ] !== undefined,
    "Profit & Loss exists in topic index"
);


assert(
    topicIndex.byDomain[
        "arithmetic"
    ].includes(
        "percentage"
    ),
    "Percentage mapped to Arithmetic"
);



/* ============================================================
   TEST 2 — Concept Index
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 2 — Concept Index"
);
console.log(
    "--------------------------------------------"
);


assert(
    conceptIndex.entities[
        "reverse-percentage"
    ] !== undefined,
    "Reverse Percentage exists in concept index"
);


assert(
    conceptIndex.byTopic[
        "percentage"
    ].includes(
        "reverse-percentage"
    ),
    "Reverse Percentage mapped to Percentage"
);



/* ============================================================
   TEST 3 — Skill Index
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 3 — Skill Index"
);
console.log(
    "--------------------------------------------"
);


assert(
    skillIndex.entities[
        "reverse-percentage"
    ] !== undefined,
    "Reverse Percentage skill exists"
);


assert(
    skillIndex.byConcept[
        "reverse-percentage"
    ].includes(
        "reverse-percentage"
    ),
    "Reverse Percentage skill mapped to concept"
);



/* ============================================================
   TEST 4 — Graph Index
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 4 — Graph Index"
);
console.log(
    "--------------------------------------------"
);


assert(
    graphIndex.prerequisites[
        "profit-loss"
    ].includes(
        "percentage"
    ),
    "Percentage indexed as Profit & Loss prerequisite"
);


assert(
    graphIndex.related[
        "profit-loss"
    ].includes(
        "ratio-proportion"
    ),
    "Ratio-Proportion indexed as related"
);



/* ============================================================
   TEST 5 — Manifest
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 5 — Build Manifest"
);
console.log(
    "--------------------------------------------"
);


assert(
    manifest.version ===
        "1.0.0",
    "Build manifest version exists"
);


assert(
    manifest.counts.topics ===
        6,
    "Manifest topic count = 6"
);


assert(
    manifest.counts.concepts ===
        8,
    "Manifest concept count = 8"
);


assert(
    manifest.counts.skills ===
        8,
    "Manifest skill count = 8"
);



/* ============================================================
   TEST 6 — Data-Driven Proof
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 6 — DATA-DRIVEN ARCHITECTURE"
);
console.log(
    "--------------------------------------------"
);


assert(
    topicIndex.entities[
        "percentage"
    ].source ===
        "percentage.json",
    "Topic index points to source data"
);


assert(
    conceptIndex.entities[
        "reverse-percentage"
    ].source ===
        "reverse-percentage.json",
    "Concept index points to source data"
);


assert(
    skillIndex.entities[
        "reverse-percentage"
    ].source ===
        "reverse-percentage.json",
    "Skill index points to source data"
);



/* ============================================================
   FINAL
   ============================================================ */

console.log("");
console.log(
    "============================================"
);

console.log(
    " STEP 26 TEST SUMMARY"
);

console.log(
    "============================================"
);

console.log("");

console.log(
    "✓ All generated indexes exist"
);

console.log(
    "✓ Topic lookup works"
);

console.log(
    "✓ Concept lookup works"
);

console.log(
    "✓ Skill lookup works"
);

console.log(
    "✓ Graph lookup works"
);

console.log(
    "✓ Build manifest works"
);

console.log(
    "✓ Data-driven architecture verified"
);

console.log("");

console.log(
    "✓ ALL KNOWLEDGE INDEX TESTS PASSED"
);

console.log(
    "✓ STEP 26 COMPLETE"
);

console.log("");
