/**
 * ============================================================
 * STEP 32.55
 *
 * FINAL PRODUCTION QUESTION INDEX REBUILD
 * ============================================================
 */

import fs from "fs";
import path from "path";


import {
    loadReadinessQuestionEntities,
    mergeReadinessEntities
} from "./readiness-question-index-adapter.js";


const ROOT =
    path.resolve(
        process.cwd(),
        "maths-mastery"
    );


const INDEX_FILE =
    path.join(
        ROOT,
        "data",
        "knowledge",
        "generated",
        "question-index.json"
    );


const READINESS_ROOT =
    path.join(
        ROOT,
        "data",
        "questions",
        "readiness"
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


const index =
    readJson(
        INDEX_FILE
    );


const beforeEntities =
    Object.keys(
        index.entities || {}
    ).length;


const readinessEntities =
    loadReadinessQuestionEntities(
        READINESS_ROOT
    );


const next =
    mergeReadinessEntities(
        index,
        readinessEntities
    );


const afterEntities =
    Object.keys(
        next.entities || {}
    ).length;


/*
 * Safety:
 * never allow the rebuild to lose an existing entity.
 */

if (
    afterEntities <
    beforeEntities
) {

    throw new Error(
        [
            "QUESTION INDEX SAFETY FAILURE",
            `Existing entities : ${beforeEntities}`,
            `Final entities    : ${afterEntities}`
        ].join(
            "\n"
        )
    );
}


fs.writeFileSync(
    INDEX_FILE,
    JSON.stringify(
        next,
        null,
        2
    ) + "\n",
    "utf8"
);


console.log("");
console.log(
    "============================================================"
);
console.log(
    " STEP 32.55 — FINAL QUESTION INDEX REBUILD"
);
console.log(
    "============================================================"
);
console.log("");


console.log(
    `Existing entities            : ${beforeEntities}`
);


console.log(
    `Readiness entities discovered : ${readinessEntities.length}`
);


console.log(
    `Final entities               : ${afterEntities}`
);


console.log("");
console.log(
    "✓ Existing entities preserved"
);


console.log(
    "✓ Readiness entities merged"
);


console.log(
    "✓ Topic lookup rebuilt"
);


console.log(
    "✓ Concept lookup rebuilt"
);


console.log(
    "✓ Skill lookup rebuilt"
);


console.log(
    "✓ Exam lookup rebuilt"
);


console.log(
    "✓ Final question index written"
);
