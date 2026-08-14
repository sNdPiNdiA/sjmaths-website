import fs from "fs";
import path from "path";

const root =
    path.resolve(
        process.cwd(),
        "maths-mastery"
    );

const questionRoot =
    path.join(
        root,
        "data",
        "knowledge",
        "questions"
    );

const schemaPath =
    path.join(
        root,
        "schemas",
        "question.schema.json"
    );


function readJson(file) {

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

    if (!condition) {

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
    " STEP 27 — QUESTION BANK VALIDATION"
);
console.log(
    "============================================"
);
console.log("");


/* ============================================================
   Schema
   ============================================================ */

assert(
    fs.existsSync(schemaPath),
    "Question schema exists"
);

const schema =
    readJson(
        schemaPath
    );

assert(
    schema.title ===
        "SJMaths Question",
    "Question schema loaded"
);


/* ============================================================
   Find question files
   ============================================================ */

const questionFiles = [];


function scanDirectory(
    directory
) {

    if (
        !fs.existsSync(
            directory
        )
    ) {
        return;
    }

    for (
        const entry of
        fs.readdirSync(
            directory,
            {
                withFileTypes: true
            }
        )
    ) {

        const fullPath =
            path.join(
                directory,
                entry.name
            );

        if (
            entry.isDirectory()
        ) {

            scanDirectory(
                fullPath
            );

        }

        else if (
            entry.isFile() &&
            entry.name.endsWith(
                ".json"
            ) &&
            entry.name !==
                "manifest.json"
        ) {

            questionFiles.push(
                fullPath
            );
        }
    }
}


scanDirectory(
    questionRoot
);


assert(
    questionFiles.length >= 1,
    "At least one question exists"
);


/* ============================================================
   Validate questions
   ============================================================ */

const ids =
    new Set();


for (
    const file of
    questionFiles
) {

    const question =
        readJson(
            file
        );


    assert(
        typeof question.id ===
            "string" &&
        question.id.length > 0,
        `Question ID valid: ${path.basename(file)}`
    );


    assert(
        !ids.has(
            question.id
        ),
        `No duplicate question ID: ${question.id}`
    );


    ids.add(
        question.id
    );


    assert(
        typeof question.topicId ===
            "string",
        `${question.id} has topicId`
    );


    assert(
        typeof question.conceptId ===
            "string",
        `${question.id} has conceptId`
    );


    assert(
        Array.isArray(
            question.skillIds
        ) &&
        question.skillIds.length > 0,
        `${question.id} has skill mapping`
    );


    assert(
        Array.isArray(
            question.exams
        ) &&
        question.exams.length > 0,
        `${question.id} has exam mapping`
    );


    assert(
        question.question &&
        typeof question.question.text ===
            "string",
        `${question.id} has question text`
    );


    assert(
        question.answer &&
        question.answer.value !==
            undefined,
        `${question.id} has answer`
    );


    assert(
        question.solution &&
        Array.isArray(
            question.solution.steps
        ) &&
        question.solution.steps.length > 0,
        `${question.id} has solution steps`
    );


    assert(
        question.metadata &&
        typeof question.metadata.source ===
            "string",
        `${question.id} has source metadata`
    );


    assert(
        [
            "foundation",
            "basic",
            "intermediate",
            "advanced",
            "olympiad"
        ].includes(
            question.difficulty
        ),
        `${question.id} difficulty valid`
    );


    assert(
        [
            "draft",
            "reviewed",
            "verified",
            "published"
        ].includes(
            question.metadata.authoringStatus
        ),
        `${question.id} authoring status valid`
    );
}


/* ============================================================
   Final
   ============================================================ */

console.log("");

console.log(
    "============================================"
);

console.log(
    " STEP 27 TEST SUMMARY"
);

console.log(
    "============================================"
);

console.log("");

console.log(
    `✓ Questions validated: ${questionFiles.length}`
);

console.log(
    `✓ Unique question IDs: ${ids.size}`
);

console.log(
    "✓ Topic mapping validated"
);

console.log(
    "✓ Concept mapping validated"
);

console.log(
    "✓ Skill mapping validated"
);

console.log(
    "✓ Exam mapping validated"
);

console.log(
    "✓ Difficulty model validated"
);

console.log(
    "✓ Answer structure validated"
);

console.log(
    "✓ Solution structure validated"
);

console.log(
    "✓ Metadata structure validated"
);

console.log("");

console.log(
    "✓ ALL QUESTION BANK TESTS PASSED"
);

console.log(
    "✓ STEP 27 COMPLETE"
);

console.log("");
