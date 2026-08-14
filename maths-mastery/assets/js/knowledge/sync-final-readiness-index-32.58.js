import fs from "fs";
import path from "path";

import {
    loadReadinessQuestionEntities,
    mergeReadinessEntities
} from "./readiness-question-index-adapter.js";


const root =
    path.resolve(
        process.cwd(),
        "maths-mastery"
    );


const indexFile =
    path.join(
        root,
        "data",
        "knowledge",
        "generated",
        "question-index.json"
    );


const readinessRoot =
    path.join(
        root,
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


const current =
    readJson(
        indexFile
    );


const before =
    Object.keys(
        current.entities || {}
    ).length;


const readinessEntities =
    loadReadinessQuestionEntities(
        readinessRoot
    );


const next =
    mergeReadinessEntities(
        current,
        readinessEntities
    );


const after =
    Object.keys(
        next.entities || {}
    ).length;


if (
    before !== after
) {

    console.log(
        `Entity count changed: ${before} -> ${after}`
    );
}


fs.writeFileSync(
    indexFile,
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
    " STEP 32.58 — READINESS INDEX SYNC"
);
console.log(
    "============================================================"
);
console.log("");


console.log(
    `Existing entities : ${before}`
);

console.log(
    `Readiness entities: ${readinessEntities.length}`
);

console.log(
    `Final entities    : ${after}`
);

console.log("");

console.log(
    "✓ Readiness source banks synchronized"
);

console.log(
    "✓ Production question index refreshed"
);
