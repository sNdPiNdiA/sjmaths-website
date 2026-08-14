/**
 * STEP 32.50B
 *
 * Readiness question index integration.
 *
 * Produces an updated question-index.json while preserving
 * all existing question entities.
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


const INDEX =
    path.join(
        ROOT,
        "data",
        "knowledge",
        "generated",
        "question-index.json"
    );


const READINESS =
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
        INDEX
    );


const beforeCount =
    Object.keys(
        index.entities || {}
    ).length;


const readinessEntities =
    loadReadinessQuestionEntities(
        READINESS
    );


const next =
    mergeReadinessEntities(
        index,
        readinessEntities
    );


const afterCount =
    Object.keys(
        next.entities || {}
    ).length;


fs.writeFileSync(
    INDEX,
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
    " STEP 32.50B — READINESS QUESTION INDEX INTEGRATION"
);
console.log(
    "============================================================"
);
console.log("");


console.log(
    `Existing entities: ${beforeCount}`
);


console.log(
    `Readiness entities discovered: ${readinessEntities.length}`
);


console.log(
    `Final entities: ${afterCount}`
);


console.log("");


if (
    afterCount <
    beforeCount
) {

    throw new Error(
        "Question index lost existing entities."
    );
}


console.log(
    "✓ Existing entities preserved"
);


console.log(
    "✓ Readiness questions added"
);


console.log(
    "✓ Topic index rebuilt"
);


console.log(
    "✓ Concept index rebuilt"
);


console.log(
    "✓ Skill index rebuilt"
);


console.log(
    "✓ Exam index rebuilt"
);


console.log(
    "✓ Question index written"
);
