/**
 * STEP 32.48B
 *
 * BOM-Safe Foundation Readiness Question Bank Validator
 */

import fs from "fs";
import path from "path";


import {
    ReadinessQuestionGenerator
} from "./readiness-question-generator.js";


const root =
    process.argv[2];


if (!root) {

    throw new Error(
        "Question-bank root argument is required."
    );
}


const generator =
    new ReadinessQuestionGenerator({

        minimumPoolSize:
            10,

        recommendedPoolSize:
            15,

        diagnosticSelectionCount:
            5
    });


function readJson(
    file
) {

    const raw =
        fs.readFileSync(
            file,
            "utf8"
        );


    /*
     * PowerShell 5.1 Set-Content -Encoding UTF8
     * may write UTF-8 BOM.
     *
     * Remove BOM before JSON.parse().
     */

    const clean =
        raw.replace(
            /^\uFEFF/,
            ""
        );


    return JSON.parse(
        clean
    );
}


const directories =
    fs.readdirSync(
        root,
        {
            withFileTypes:
                true
        }
    )
    .filter(
        item =>
            item.isDirectory()
    )
    .sort(
        (
            a,
            b
        ) =>
            a.name.localeCompare(
                b.name
            )
    );


let total =
    0;

let validatedBanks =
    0;


for (
    const directory
    of directories
) {

    const file =
        path.join(
            root,
            directory.name,
            "questions.json"
        );


    if (
        !fs.existsSync(
            file
        )
    ) {

        continue;
    }


    const payload =
        readJson(
            file
        );


    if (
        !payload ||
        typeof payload !==
        "object"
    ) {

        console.error(
            `INVALID ${directory.name}: JSON root is not an object.`
        );


        process.exit(
            1
        );
    }


    if (
        typeof payload.readinessSkillId !==
        "string"
    ) {

        console.error(
            `INVALID ${directory.name}: readinessSkillId missing.`
        );


        process.exit(
            1
        );
    }


    if (
        !Array.isArray(
            payload.questions
        )
    ) {

        console.error(
            `INVALID ${payload.readinessSkillId}: questions must be an array.`
        );


        process.exit(
            1
        );
    }


    const result =
        generator.validatePool(
            payload.questions,
            payload.readinessSkillId
        );


    if (
        !result.valid
    ) {

        console.error(
            `INVALID ${payload.readinessSkillId}`
        );


        for (
            const error
            of result.errors
        ) {

            console.error(
                `  ${error}`
            );
        }


        process.exit(
            1
        );
    }


    total +=
        result.exactSkillCount;


    validatedBanks +=
        1;


    console.log(
        `✓ ${payload.readinessSkillId}: ${result.exactSkillCount} exact-skill questions`
    );
}


console.log("");
console.log(
    `VALIDATED BANKS: ${validatedBanks}`
);


console.log(
    `VALIDATED QUESTIONS: ${total}`
);
