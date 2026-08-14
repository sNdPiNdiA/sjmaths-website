import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";


/* ============================================================
   Resolve paths relative to this file
   ============================================================ */

const __filename =
    fileURLToPath(import.meta.url);

const __dirname =
    path.dirname(__filename);


/*
 * test-progress-contract.js
 *
 * maths-mastery/
 * └── assets/
 *     └── js/
 *         └── test-progress-contract.js
 *
 * ../../ = maths-mastery
 */

const masteryRoot =
    path.resolve(
        __dirname,
        "../.."
    );


const schemaPath =
    path.join(
        masteryRoot,
        "schemas",
        "progress.schema.json"
    );


const progressPath =
    path.join(
        masteryRoot,
        "data",
        "progress",
        "progress-demo.json"
    );


/* ============================================================
   BOM-safe JSON loader
   ============================================================ */

function loadJson(filePath) {

    if (!fs.existsSync(filePath)) {

        throw new Error(
            `File not found: ${filePath}`
        );
    }


    let text =
        fs.readFileSync(
            filePath,
            "utf8"
        );


    /*
     * Remove UTF-8 BOM.
     */

    if (
        text.length > 0 &&
        text.charCodeAt(0) === 0xFEFF
    ) {

        text =
            text.slice(1);
    }


    return JSON.parse(text);
}


let allValid = true;


console.log("");

console.log(
    "============================================"
);

console.log(
    " STEP 12.1 — VALIDATING PROGRESS CONTRACT"
);

console.log(
    "============================================"
);

console.log("");


/* ============================================================
   Show resolved paths
   ============================================================ */

console.log(
    "Schema:",
    schemaPath
);

console.log(
    "Progress:",
    progressPath
);

console.log("");


/* ============================================================
   Validate schema JSON
   ============================================================ */

let schema;

try {

    schema =
        loadJson(
            schemaPath
        );

    console.log(
        "✓ VALID progress.schema.json"
    );

}
catch (error) {

    console.log(
        "✗ INVALID progress.schema.json"
    );

    console.log(
        error.message
    );

    allValid = false;
}


/* ============================================================
   Validate progress JSON
   ============================================================ */

let progress;

try {

    progress =
        loadJson(
            progressPath
        );

    console.log(
        "✓ VALID progress-demo.json"
    );

}
catch (error) {

    console.log(
        "✗ INVALID progress-demo.json"
    );

    console.log(
        error.message
    );

    allValid = false;
}


/* ============================================================
   Basic schema contract checks
   ============================================================ */

if (
    progress
) {


    /* --------------------------------------------------------
       Version
       -------------------------------------------------------- */

    if (
        typeof progress.version ===
            "string"
    ) {

        console.log(
            "✓ Progress version present"
        );

    }
    else {

        console.log(
            "✗ Progress version missing"
        );

        allValid = false;
    }


    /* --------------------------------------------------------
       Student ID
       -------------------------------------------------------- */

    if (
        typeof progress.studentId ===
            "string" &&
        progress.studentId.length > 0
    ) {

        console.log(
            "✓ Student ID present"
        );

    }
    else {

        console.log(
            "✗ Student ID missing"
        );

        allValid = false;
    }


    /* --------------------------------------------------------
       Updated timestamp
       -------------------------------------------------------- */

    if (
        typeof progress.updatedAt ===
            "string"
    ) {

        console.log(
            "✓ Updated timestamp present"
        );

    }
    else {

        console.log(
            "✗ Updated timestamp missing"
        );

        allValid = false;
    }


    /* --------------------------------------------------------
       Topics
       -------------------------------------------------------- */

    if (
        progress.topics &&
        typeof progress.topics ===
            "object"
    ) {

        console.log(
            "✓ Topics object present"
        );

    }
    else {

        console.log(
            "✗ Topics object missing"
        );

        allValid = false;
    }


    /* ========================================================
       Percentage topic
       ======================================================== */

    const percentage =
        progress.topics?.percentage;


    if (
        percentage
    ) {

        console.log(
            "✓ Percentage progress found"
        );


        /* ----------------------------------------------------
           Topic ID
           ---------------------------------------------------- */

        if (
            percentage.topicId ===
                "percentage"
        ) {

            console.log(
                "✓ Percentage topicId correct"
            );

        }
        else {

            console.log(
                "✗ Percentage topicId incorrect"
            );

            allValid = false;
        }


        /* ----------------------------------------------------
           Status
           ---------------------------------------------------- */

        if (
            [
                "not-started",
                "learning",
                "developing",
                "proficient",
                "mastered"
            ].includes(
                percentage.status
            )
        ) {

            console.log(
                "✓ Topic status valid"
            );

        }
        else {

            console.log(
                "✗ Topic status invalid"
            );

            allValid = false;
        }


        /* ----------------------------------------------------
           Evidence
           ---------------------------------------------------- */

        if (
            percentage.evidence
        ) {

            console.log(
                "✓ Topic evidence present"
            );

        }
        else {

            console.log(
                "✗ Topic evidence missing"
            );

            allValid = false;
        }


        /* ----------------------------------------------------
           Concepts
           ---------------------------------------------------- */

        if (
            percentage.concepts &&
            typeof percentage.concepts ===
                "object"
        ) {

            console.log(
                "✓ Concept evidence present"
            );

        }
        else {

            console.log(
                "✗ Concept evidence missing"
            );

            allValid = false;
        }


        /* ----------------------------------------------------
           Skills
           ---------------------------------------------------- */

        if (
            percentage.skills &&
            typeof percentage.skills ===
                "object"
        ) {

            console.log(
                "✓ Skill evidence present"
            );

        }
        else {

            console.log(
                "✗ Skill evidence missing"
            );

            allValid = false;
        }


        /* ----------------------------------------------------
           Mini tests
           ---------------------------------------------------- */

        if (
            percentage.miniTests &&
            typeof percentage.miniTests ===
                "object"
        ) {

            console.log(
                "✓ Mini-test progress present"
            );

        }
        else {

            console.log(
                "✗ Mini-test progress missing"
            );

            allValid = false;
        }


        /* ====================================================
           Evidence integrity
           ==================================================== */

        const evidence =
            percentage.evidence;


        if (
            evidence.attempts ===
                evidence.correct +
                evidence.incorrect +
                evidence.skipped
        ) {

            console.log(
                "✓ Topic evidence counts are consistent"
            );

        }
        else {

            console.log(
                "✗ Topic evidence counts are inconsistent"
            );

            allValid = false;
        }


        /* ====================================================
           Reverse Percentage
           ==================================================== */

        const reversePercentage =
            percentage.skills[
                "reverse-percentage"
            ];


        if (
            reversePercentage
        ) {

            console.log(
                "✓ Reverse Percentage skill found"
            );

        }
        else {

            console.log(
                "✗ Reverse Percentage skill missing"
            );

            allValid = false;
        }


        if (
            reversePercentage?.score ===
                55
        ) {

            console.log(
                "✓ Reverse Percentage score = 55%"
            );

        }
        else {

            console.log(
                "✗ Reverse Percentage score incorrect"
            );

            allValid = false;
        }


        /* ====================================================
           Mini-test evidence
           ==================================================== */

        const foundationTest =
            percentage.miniTests[
                "percentage-test-foundation"
            ];


        if (
            foundationTest
        ) {

            console.log(
                "✓ Foundation mini-test progress found"
            );

        }
        else {

            console.log(
                "✗ Foundation mini-test progress missing"
            );

            allValid = false;
        }


        if (
            foundationTest?.bestScore >= 0 &&
            foundationTest?.bestScore <= 100
        ) {

            console.log(
                "✓ Mini-test score within valid range"
            );

        }
        else {

            console.log(
                "✗ Mini-test score outside valid range"
            );

            allValid = false;
        }
    }
    else {

        console.log(
            "✗ Percentage progress missing"
        );

        allValid = false;
    }
}


/* ============================================================
   Final
   ============================================================ */

console.log("");

if (
    allValid
) {

    console.log(
        "============================================"
    );

    console.log(
        " STEP 12.1 COMPLETE"
    );

    console.log(
        "============================================"
    );

    console.log("");

    console.log(
        "✓ Progress schema loaded"
    );

    console.log(
        "✓ Progress data loaded"
    );

    console.log(
        "✓ Topic evidence validated"
    );

    console.log(
        "✓ Concept evidence validated"
    );

    console.log(
        "✓ Skill evidence validated"
    );

    console.log(
        "✓ Mini-test evidence validated"
    );

    console.log(
        "✓ Evidence counts validated"
    );

}
else {

    console.log(
        "============================================"
    );

    console.log(
        " STEP 12.1 FAILED — CHECK ERRORS ABOVE"
    );

    console.log(
        "============================================"
    );

    process.exitCode = 1;
}

console.log("");
