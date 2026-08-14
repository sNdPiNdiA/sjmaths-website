import {
    validateDiagnostic,
    validateAnswer,
    calculateTopicStatistics,
    calculateSkillStatistics,
    findWeakestTopic,
    findStrongestTopic,
    buildTopicOrder,
    recommendStartingTopic,
    completeDiagnostic
} from "./diagnostic-engine.js";


let passed = 0;
let failed = 0;


function pass(message) {

    passed++;

    console.log(
        `✓ ${message}`
    );
}


function fail(message) {

    failed++;

    console.log(
        `✗ ${message}`
    );
}


function assert(
    condition,
    message
) {

    if (condition) {

        pass(message);

    }
    else {

        fail(message);
    }
}


console.log("");

console.log(
    "============================================"
);

console.log(
    " STEP 20 — DIAGNOSTIC ENGINE TESTS"
);

console.log(
    "============================================"
);

console.log("");


/* ============================================================
   Prototype Diagnostic
   ============================================================ */

const diagnostic = {

    version:
        "1.0.0",

    id:
        "test-diagnostic",

    minimumQuestions:
        10,

    questions: [

        {
            id:
                "q-ns-1",

            topicId:
                "number-system",

            skillId:
                "number-skill",

            difficulty:
                "foundation",

            questionType:
                "mcq"
        },

        {
            id:
                "q-ns-2",

            topicId:
                "number-system",

            skillId:
                "number-skill",

            difficulty:
                "basic",

            questionType:
                "mcq"
        },

        {
            id:
                "q-fr-1",

            topicId:
                "fractions",

            skillId:
                "fraction-skill",

            difficulty:
                "foundation",

            questionType:
                "mcq"
        },

        {
            id:
                "q-fr-2",

            topicId:
                "fractions",

            skillId:
                "fraction-skill",

            difficulty:
                "basic",

            questionType:
                "mcq"
        },

        {
            id:
                "q-de-1",

            topicId:
                "decimals",

            skillId:
                "decimal-skill",

            difficulty:
                "foundation",

            questionType:
                "mcq"
        },

        {
            id:
                "q-de-2",

            topicId:
                "decimals",

            skillId:
                "decimal-skill",

            difficulty:
                "basic",

            questionType:
                "mcq"
        },

        {
            id:
                "q-rp-1",

            topicId:
                "ratio-proportion",

            skillId:
                "ratio-skill",

            difficulty:
                "basic",

            questionType:
                "mcq"
        },

        {
            id:
                "q-rp-2",

            topicId:
                "ratio-proportion",

            skillId:
                "ratio-skill",

            difficulty:
                "intermediate",

            questionType:
                "mcq"
        },

        {
            id:
                "q-pct-1",

            topicId:
                "percentage",

            skillId:
                "percentage-skill",

            difficulty:
                "basic",

            questionType:
                "mcq"
        },

        {
            id:
                "q-pct-2",

            topicId:
                "percentage",

            skillId:
                "reverse-percentage",

            difficulty:
                "intermediate",

            questionType:
                "mcq"
        }
    ]
};


const graph = {

    nodes: [

        {
            topicId:
                "number-system",

            level:
                "foundation"
        },

        {
            topicId:
                "fractions",

            level:
                "foundation"
        },

        {
            topicId:
                "decimals",

            level:
                "foundation"
        },

        {
            topicId:
                "ratio-proportion",

            level:
                "basic"
        },

        {
            topicId:
                "percentage",

            level:
                "basic"
        },

        {
            topicId:
                "profit-loss",

            level:
                "intermediate"
        }
    ]
};


/* ============================================================
   TEST 1 — Diagnostic Validation
   ============================================================ */

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 1 — Diagnostic Validation"
);

console.log(
    "--------------------------------------------"
);


assert(
    validateDiagnostic(
        diagnostic
    ),
    "Diagnostic definition is valid"
);


assert(
    diagnostic.questions.length ===
        10,
    "Diagnostic contains 10 questions"
);


const ids =
    diagnostic.questions.map(
        q => q.id
    );


assert(
    new Set(ids).size ===
        ids.length,
    "Diagnostic question IDs are unique"
);



/* ============================================================
   TEST 2 — Answer Validation
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 2 — Answer Validation"
);

console.log(
    "--------------------------------------------"
);


assert(
    validateAnswer({
        questionId:
            "q-pct-1",

        result:
            "correct"
    }),
    "Correct answer accepted"
);


assert(
    validateAnswer({
        questionId:
            "q-pct-1",

        result:
            "incorrect"
    }),
    "Incorrect answer accepted"
);


assert(
    validateAnswer({
        questionId:
            "q-pct-1",

        result:
            "skipped"
    }),
    "Skipped answer accepted"
);


assert(
    validateAnswer({
        questionId:
            "q-pct-1",

        result:
            "invalid"
    }) === false,
    "Invalid answer rejected"
);



/* ============================================================
   TEST 3 — Topic Statistics
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 3 — Topic Statistics"
);

console.log(
    "--------------------------------------------"
);


const answers = [

    {
        questionId:
            "q-ns-1",

        result:
            "correct"
    },

    {
        questionId:
            "q-ns-2",

        result:
            "correct"
    },

    {
        questionId:
            "q-fr-1",

        result:
            "correct"
    },

    {
        questionId:
            "q-fr-2",

        result:
            "incorrect"
    },

    {
        questionId:
            "q-de-1",

        result:
            "correct"
    },

    {
        questionId:
            "q-de-2",

        result:
            "correct"
    },

    {
        questionId:
            "q-rp-1",

        result:
            "correct"
    },

    {
        questionId:
            "q-rp-2",

        result:
            "incorrect"
    },

    {
        questionId:
            "q-pct-1",

        result:
            "incorrect"
    },

    {
        questionId:
            "q-pct-2",

        result:
            "incorrect"
    }
];


const topicStats =
    calculateTopicStatistics(
        diagnostic,
        answers
    );


assert(
    topicStats[
        "number-system"
    ].accuracy === 100,
    "Number System accuracy = 100%"
);


assert(
    topicStats[
        "fractions"
    ].accuracy === 50,
    "Fractions accuracy = 50%"
);


assert(
    topicStats[
        "percentage"
    ].accuracy === 0,
    "Percentage accuracy = 0%"
);


assert(
    topicStats[
        "percentage"
    ].answered === 2,
    "Percentage answered count = 2"
);



/* ============================================================
   TEST 4 — Skill Statistics
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 4 — Skill Statistics"
);

console.log(
    "--------------------------------------------"
);


const skillStats =
    calculateSkillStatistics(
        diagnostic,
        answers
    );


assert(
    skillStats[
        "number-skill"
    ].accuracy === 100,
    "Number skill accuracy = 100%"
);


assert(
    skillStats[
        "fraction-skill"
    ].accuracy === 50,
    "Fraction skill accuracy = 50%"
);


assert(
    skillStats[
        "reverse-percentage"
    ].accuracy === 0,
    "Reverse Percentage accuracy = 0%"
);



/* ============================================================
   TEST 5 — Weakest / Strongest
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 5 — Weakest and Strongest Topics"
);

console.log(
    "--------------------------------------------"
);


const weakest =
    findWeakestTopic(
        topicStats
    );


assert(
    weakest.topicId ===
        "percentage",
    "Percentage identified as weakest topic"
);


const strongest =
    findStrongestTopic(
        topicStats
    );


assert(
    strongest.topicId ===
        "number-system",
    "Number System identified as strongest topic"
);



/* ============================================================
   TEST 6 — Graph Ordering
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 6 — Topic Graph Ordering"
);

console.log(
    "--------------------------------------------"
);


const order =
    buildTopicOrder(
        graph
    );


assert(
    order[0] ===
        "number-system",
    "Foundation topic appears first"
);


assert(
    order.indexOf(
        "percentage"
    ) >
    order.indexOf(
        "fractions"
    ),
    "Percentage appears after Fractions"
);


assert(
    order.indexOf(
        "profit-loss"
    ) >
    order.indexOf(
        "percentage"
    ),
    "Profit & Loss appears after Percentage"
);



/* ============================================================
   TEST 7 — Starting Topic Recommendation
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 7 — Starting Topic Recommendation"
);

console.log(
    "--------------------------------------------"
);


const recommendation =
    recommendStartingTopic(
        topicStats,
        graph
    );


assert(
    recommendation.topicId ===
        "fractions",
    "Fractions selected because it is the earliest insufficiently ready prerequisite"
);


assert(
    recommendation.reason.length >
        0,
    "Recommendation contains explanation"
);



/* ============================================================
   TEST 8 — No Evidence
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 8 — No Diagnostic Evidence"
);

console.log(
    "--------------------------------------------"
);


const noEvidence =
    recommendStartingTopic(
        {},
        graph
    );


assert(
    noEvidence.topicId ===
        "number-system",
    "No evidence starts at foundation"
);



/* ============================================================
   TEST 9 — All Strong
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 9 — All Assessed Topics Strong"
);

console.log(
    "--------------------------------------------"
);


const strongStats = {

    "number-system": {

        topicId:
            "number-system",

        answered:
            2,

        accuracy:
            100
    },

    "fractions": {

        topicId:
            "fractions",

        answered:
            2,

        accuracy:
            100
    },

    "decimals": {

        topicId:
            "decimals",

        answered:
            2,

        accuracy:
            100
    }
};


const strongRecommendation =
    recommendStartingTopic(
        strongStats,
        graph
    );


assert(
    strongRecommendation.topicId ===
        "ratio-proportion",
    "Next unassessed topic selected after strong foundation"
);



/* ============================================================
   TEST 10 — Complete Diagnostic
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 10 — Complete Diagnostic"
);

console.log(
    "--------------------------------------------"
);


const completed =
    completeDiagnostic(
        diagnostic,
        answers,
        graph,
        {
            selectedExam:
                "ssc"
        }
    );


assert(
    completed.completed ===
        true,
    "Diagnostic marked complete"
);


assert(
    completed.questionCount ===
        10,
    "Question count recorded"
);


assert(
    completed.startingPoint ===
        "fractions",
    "Starting point recorded"
);


assert(
    completed.selectedExam ===
        "ssc",
    "Selected exam preserved"
);


assert(
    completed.completedAt !==
        undefined,
    "Completion timestamp recorded"
);



/* ============================================================
   TEST 11 — Minimum Evidence
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 11 — Minimum Evidence"
);

console.log(
    "--------------------------------------------"
);


let minimumError =
    false;


try {

    completeDiagnostic(
        diagnostic,
        answers.slice(
            0,
            5
        ),
        graph
    );

}
catch {

    minimumError =
        true;
}


assert(
    minimumError,
    "Incomplete diagnostic is rejected"
);



/* ============================================================
   TEST 12 — Unknown Question
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 12 — Unknown Question Rejection"
);

console.log(
    "--------------------------------------------"
);


let unknownError =
    false;


try {

    calculateTopicStatistics(
        diagnostic,
        [
            {
                questionId:
                    "does-not-exist",

                result:
                    "correct"
            }
        ]
    );

}
catch {

    unknownError =
        true;
}


assert(
    unknownError,
    "Unknown diagnostic question rejected"
);



/* ============================================================
   FINAL
   ============================================================ */

console.log("");

console.log(
    "============================================"
);

console.log(
    " STEP 20 TEST SUMMARY"
);

console.log(
    "============================================"
);

console.log("");

console.log(
    `Passed: ${passed}`
);

console.log(
    `Failed: ${failed}`
);

console.log("");

if (
    failed === 0
) {

    console.log(
        "✓ ALL DIAGNOSTIC ENGINE TESTS PASSED"
    );

    console.log(
        "✓ STEP 20 COMPLETE"
    );

}
else {

    console.log(
        "✗ STEP 20 FAILED — CHECK ERRORS ABOVE"
    );

    process.exitCode = 1;
}

console.log("");

console.log(
    "============================================"
);

console.log("");

