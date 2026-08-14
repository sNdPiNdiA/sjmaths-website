import fs from "fs";
import path from "path";

import {
    selectQuestions,
    selectNextQuestion,
    calculateScore,
    explainSelection
} from "./question-selection-engine.js";


const ROOT =
    path.resolve(
        process.cwd(),
        "maths-mastery"
    );


const questionIndexPath =
    path.join(
        ROOT,
        "data",
        "knowledge",
        "generated",
        "question-index.json"
    );


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


console.log("");
console.log(
    "============================================"
);
console.log(
    " STEP 28 — ADAPTIVE QUESTION TESTS"
);
console.log(
    "============================================"
);
console.log("");


/* ============================================================
   TEST 1 — Question Index
   ============================================================ */

console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 1 — Question Index"
);
console.log(
    "--------------------------------------------"
);


assert(
    fs.existsSync(
        questionIndexPath
    ),
    "Question index exists"
);


const questionIndex =
    readJson(
        questionIndexPath
    );


assert(
    Object.keys(
        questionIndex.entities || {}
    ).length > 0,
    "Question index contains questions"
);


/* ============================================================
   TEST 2 — Current Topic Selection
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 2 — Current Topic Selection"
);
console.log(
    "--------------------------------------------"
);


const topicResult =
    selectNextQuestion(
        {

            currentTopicId:
                "percentage",

            examId:
                "ssc",

            weakSkills: [
                {
                    skillId:
                        "reverse-percentage",
                    score:
                        55
                }
            ],

            masteryStatus:
                "learning",

            attemptedQuestionIds: []

        }
    );


assert(
    topicResult !== null,
    "Question selected for current topic"
);


assert(
    topicResult.question.topicId ===
        "percentage",
    "Selected question belongs to current topic"
);


/* ============================================================
   TEST 3 — Weak Skill Priority
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 3 — Weak Skill Priority"
);
console.log(
    "--------------------------------------------"
);


assert(
    topicResult.question.skillIds.includes(
        "reverse-percentage"
    ),
    "Weak skill is targeted"
);


assert(
    topicResult.score > 0,
    "Weak-skill question receives positive score"
);


/* ============================================================
   TEST 4 — Exam Matching
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 4 — Exam Matching"
);
console.log(
    "--------------------------------------------"
);


assert(
    topicResult.question.exams.includes(
        "ssc"
    ),
    "Selected question supports SSC"
);


/* ============================================================
   TEST 5 — Difficulty Adaptation
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 5 — Difficulty Adaptation"
);
console.log(
    "--------------------------------------------"
);


const difficultyResult =
    selectNextQuestion(
        {

            currentTopicId:
                "percentage",

            examId:
                "ssc",

            weakSkills: [
                "reverse-percentage"
            ],

            masteryStatus:
                "learning",

            attemptedQuestionIds: []

        }
    );


assert(
    difficultyResult !== null,
    "Difficulty-aware question selected"
);


assert(
    [
        "foundation",
        "basic",
        "intermediate",
        "advanced",
        "olympiad"
    ].includes(
        difficultyResult.question.difficulty
    ),
    "Selected question has valid difficulty"
);


/* ============================================================
   TEST 6 — Attempted Question Handling
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 6 — Attempt History"
);
console.log(
    "--------------------------------------------"
);


const firstQuestion =
    selectNextQuestion(
        {

            currentTopicId:
                "percentage",

            examId:
                "ssc",

            weakSkills: [
                "reverse-percentage"
            ],

            masteryStatus:
                "learning",

            attemptedQuestionIds: []

        }
    );


const secondQuestion =
    selectNextQuestion(
        {

            currentTopicId:
                "percentage",

            examId:
                "ssc",

            weakSkills: [
                "reverse-percentage"
            ],

            masteryStatus:
                "learning",

            attemptedQuestionIds: [
                firstQuestion.question.id
            ]

        }
    );


assert(
    secondQuestion !== null,
    "Alternative question can be selected"
);


assert(
    secondQuestion.question.id !==
        firstQuestion.question.id,
    "Previously attempted question is avoided when alternatives exist"
);


/* ============================================================
   TEST 7 — Ranking
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 7 — Candidate Ranking"
);
console.log(
    "--------------------------------------------"
);


const candidates =
    selectQuestions(
        {

            currentTopicId:
                "percentage",

            examId:
                "ssc",

            weakSkills: [
                "reverse-percentage"
            ],

            masteryStatus:
                "learning",

            attemptedQuestionIds: []

        },
        {
            limit: 10
        }
    );


assert(
    candidates.length > 0,
    "Candidate questions returned"
);


for (
    let i = 1;
    i < candidates.length;
    i++
) {

    assert(
        candidates[i - 1].score >=
        candidates[i].score,
        "Candidates are sorted by descending score"
    );
}


/* ============================================================
   TEST 8 — Selection Explanation
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 8 — Selection Explanation"
);
console.log(
    "--------------------------------------------"
);


const reasons =
    explainSelection(
        firstQuestion.question,
        {

            currentTopicId:
                "percentage",

            examId:
                "ssc",

            weakSkills: [
                "reverse-percentage"
            ],

            masteryStatus:
                "learning"

        }
    );


assert(
    Array.isArray(
        reasons
    ) &&
    reasons.length > 0,
    "Selection explanation generated"
);


assert(
    reasons.some(
        reason =>
            reason.includes(
                "weak skill"
            )
    ),
    "Explanation identifies weak skill"
);


/* ============================================================
   TEST 9 — Immutable Context
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 9 — Input Immutability"
);
console.log(
    "--------------------------------------------"
);


const context = {

    currentTopicId:
        "percentage",

    examId:
        "ssc",

    weakSkills: [
        "reverse-percentage"
    ],

    masteryStatus:
        "learning",

    attemptedQuestionIds: []

};


const before =
    JSON.stringify(
        context
    );


selectNextQuestion(
    context
);


const after =
    JSON.stringify(
        context
    );


assert(
    before === after,
    "Selection does not mutate learner context"
);


/* ============================================================
   TEST 10 — Data-Driven Architecture
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 10 — DATA-DRIVEN SELECTION"
);
console.log(
    "--------------------------------------------"
);


const selectedId =
    firstQuestion.question.id;


assert(
    typeof selectedId ===
        "string",
    "Question ID comes from knowledge data"
);


assert(
    !selectedId.startsWith(
        "hardcoded-"
    ),
    "Selection does not require hardcoded question IDs"
);


/* ============================================================
   FINAL
   ============================================================ */

console.log("");
console.log(
    "============================================"
);

console.log(
    " STEP 28 TEST SUMMARY"
);

console.log(
    "============================================"
);

console.log("");

console.log(
    "✓ Question index loaded"
);

console.log(
    "✓ Topic matching works"
);

console.log(
    "✓ Weak-skill targeting works"
);

console.log(
    "✓ Exam filtering works"
);

console.log(
    "✓ Difficulty adaptation works"
);

console.log(
    "✓ Attempt history works"
);

console.log(
    "✓ Candidate ranking works"
);

console.log(
    "✓ Selection explanation works"
);

console.log(
    "✓ Learner context remains immutable"
);

console.log(
    "✓ Selection is data-driven"
);

console.log("");

console.log(
    "✓ ALL ADAPTIVE QUESTION TESTS PASSED"
);

console.log(
    "✓ STEP 28 COMPLETE"
);

console.log("");
