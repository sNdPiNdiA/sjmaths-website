import {
    validateGraph,
    getPrerequisites,
    getRelatedTopics,
    getProgressionEdges,
    isTopicBlocked,
    findWeakPrerequisite,
    findCandidateTopics,
    findEarliestBlockingTopic,
    buildGraphLearningOrder,
    recommendGraphAwareStartingTopic,
    explainTopicReadiness
} from "./graph-diagnostic-engine.js";


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
    " STEP 21 — GRAPH-AWARE DIAGNOSTIC TESTS"
);

console.log(
    "============================================"
);

console.log("");


/* ============================================================
   Prototype Graph
   ============================================================ */

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
    ],


    edges: [

        {
            from:
                "number-system",

            to:
                "fractions",

            relation:
                "progression",

            strength:
                0.90
        },

        {
            from:
                "fractions",

            to:
                "decimals",

            relation:
                "progression",

            strength:
                0.85
        },

        {
            from:
                "fractions",

            to:
                "ratio-proportion",

            relation:
                "prerequisite",

            strength:
                0.80
        },

        {
            from:
                "decimals",

            to:
                "percentage",

            relation:
                "prerequisite",

            strength:
                0.80
        },

        {
            from:
                "fractions",

            to:
                "percentage",

            relation:
                "prerequisite",

            strength:
                0.90
        },

        {
            from:
                "ratio-proportion",

            to:
                "percentage",

            relation:
                "related",

            strength:
                0.65
        },

        {
            from:
                "percentage",

            to:
                "profit-loss",

            relation:
                "prerequisite",

            strength:
                0.95
        },

        {
            from:
                "ratio-proportion",

            to:
                "profit-loss",

            relation:
                "related",

            strength:
                0.70
        }
    ]
};


/* ============================================================
   TEST 1 — Graph Validation
   ============================================================ */

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 1 — Graph Validation"
);

console.log(
    "--------------------------------------------"
);


assert(
    validateGraph(
        graph
    ),
    "Prototype graph is valid"
);



/* ============================================================
   TEST 2 — Prerequisite Detection
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 2 — Prerequisite Detection"
);

console.log(
    "--------------------------------------------"
);


const percentagePrereqs =
    getPrerequisites(
        graph,
        "percentage"
    );


assert(
    percentagePrereqs.length ===
        2,
    "Percentage has two prerequisite edges"
);


assert(
    percentagePrereqs.some(
        edge =>
            edge.from ===
            "fractions"
    ),
    "Fractions detected as Percentage prerequisite"
);


assert(
    percentagePrereqs.some(
        edge =>
            edge.from ===
            "decimals"
    ),
    "Decimals detected as Percentage prerequisite"
);



/* ============================================================
   TEST 3 — Related Does Not Become Prerequisite
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 3 — Related Relationship"
);

console.log(
    "--------------------------------------------"
);


const related =
    getRelatedTopics(
        graph,
        "profit-loss"
    );


assert(
    related.length ===
        1,
    "Profit & Loss has one related topic"
);


assert(
    related[0].from ===
        "ratio-proportion",
    "Ratio-Proportion detected as related"
);


const profitPrereqs =
    getPrerequisites(
        graph,
        "profit-loss"
    );


assert(
    profitPrereqs.length ===
        1,
    "Profit & Loss has exactly one prerequisite"
);


assert(
    profitPrereqs[0].from ===
        "percentage",
    "Percentage is the only blocking prerequisite"
);



/* ============================================================
   TEST 4 — Progression Relationship
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 4 — Progression Relationship"
);

console.log(
    "--------------------------------------------"
);


const decimalProgression =
    getProgressionEdges(
        graph,
        "decimals"
    );


assert(
    decimalProgression.length ===
        1,
    "Decimals has progression relationship"
);


assert(
    decimalProgression[0].from ===
        "fractions",
    "Fractions → Decimals progression detected"
);



/* ============================================================
   TEST 5 — Blocked Topic
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 5 — Prerequisite Blocking"
);

console.log(
    "--------------------------------------------"
);


const weakPrerequisiteStats = {

    "fractions": {

        topicId:
            "fractions",

        answered:
            2,

        accuracy:
            50
    },

    "decimals": {

        topicId:
            "decimals",

        answered:
            2,

        accuracy:
            90
    }
};


const percentageBlocked =
    isTopicBlocked(
        "percentage",
        weakPrerequisiteStats,
        graph
    );


assert(
    percentageBlocked.blocked ===
        true,
    "Percentage is blocked by weak prerequisite"
);


assert(
    percentageBlocked.blockers.some(
        blocker =>
            blocker.topicId ===
            "fractions"
    ),
    "Fractions identified as blocker"
);



/* ============================================================
   TEST 6 — Related Topic Cannot Block
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 6 — Related Topic Cannot Block"
);

console.log(
    "--------------------------------------------"
);


const relatedOnlyStats = {

    "ratio-proportion": {

        topicId:
            "ratio-proportion",

        answered:
            2,

        accuracy:
            20
    },

    "percentage": {

        topicId:
            "percentage",

        answered:
            2,

        accuracy:
            90
    }
};


const profitState =
    isTopicBlocked(
        "profit-loss",
        relatedOnlyStats,
        graph
    );


assert(
    profitState.blocked ===
        false,
    "Weak related topic does not block Profit & Loss"
);


assert(
    profitState.blockers.length ===
        0,
    "Related topic produces no blocker"
);



/* ============================================================
   TEST 7 — Weak Prerequisite
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 7 — Weak Prerequisite Detection"
);

console.log(
    "--------------------------------------------"
);


const weak =
    findWeakPrerequisite(
        "percentage",
        weakPrerequisiteStats,
        graph
    );


assert(
    weak !== null,
    "Weak prerequisite detected"
);


assert(
    weak.topicId ===
        "fractions",
    "Fractions identified as weak prerequisite"
);



/* ============================================================
   TEST 8 — Graph Learning Order
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 8 — Graph Learning Order"
);

console.log(
    "--------------------------------------------"
);


const order =
    buildGraphLearningOrder(
        graph
    );


assert(
    order.indexOf(
        "number-system"
    ) <
    order.indexOf(
        "fractions"
    ),
    "Number System comes before Fractions"
);


assert(
    order.indexOf(
        "fractions"
    ) <
    order.indexOf(
        "percentage"
    ),
    "Fractions comes before Percentage"
);


assert(
    order.indexOf(
        "percentage"
    ) <
    order.indexOf(
        "profit-loss"
    ),
    "Percentage comes before Profit & Loss"
);



/* ============================================================
   TEST 9 — Graph-Aware Starting Point
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 9 — Graph-Aware Starting Point"
);

console.log(
    "--------------------------------------------"
);


const startingStats = {

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
            50
    },

    "decimals": {

        topicId:
            "decimals",

        answered:
            2,

        accuracy:
            90
    },

    "percentage": {

        topicId:
            "percentage",

        answered:
            2,

        accuracy:
            0
    }
};


const startingPoint =
    recommendGraphAwareStartingTopic(
        startingStats,
        graph
    );


assert(
    startingPoint.topicId ===
        "fractions",
    "Weak prerequisite determines starting point"
);



/* ============================================================
   TEST 10 — Strong Prerequisites Allow Progression
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 10 — Strong Prerequisites"
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
            90
    },

    "decimals": {

        topicId:
            "decimals",

        answered:
            2,

        accuracy:
            90
    },

    "percentage": {

        topicId:
            "percentage",

        answered:
            2,

        accuracy:
            40
    }
};


const percentageWeak =
    recommendGraphAwareStartingTopic(
        strongStats,
        graph
    );


assert(
    percentageWeak.topicId ===
        "percentage",
    "Strong prerequisites allow Percentage to be evaluated"
);



/* ============================================================
   TEST 11 — Profit & Loss Prerequisite
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 11 — Profit & Loss Prerequisite"
);

console.log(
    "--------------------------------------------"
);


/*
 * This test verifies the GRAPH relationship itself.
 *
 * Percentage is a prerequisite of Profit & Loss.
 *
 * Therefore:
 *
 * Percentage weak
 *        ↓
 * Profit & Loss blocked
 *
 * However, the learner should remain at Percentage as the
 * starting point because Percentage itself is weak.
 */

/*
 * Dedicated Test 11 statistics.
 *
 * Percentage has been assessed and is weak.
 * Profit & Loss has not yet been assessed.
 *
 * Therefore:
 *
 * Percentage → Profit & Loss
 *          prerequisite
 *
 * Profit & Loss must be blocked.
 */

const profitStats = {

    "number-system": {

        accuracy: 100,

        answered: 2

    },

    "fractions": {

        accuracy: 90,

        answered: 2

    },

    "decimals": {

        accuracy: 90,

        answered: 2

    },

    "percentage": {

        accuracy: 50,

        answered: 2

    },

    "profit-loss": {

        accuracy: 0,

        answered: 0

    }

};

const profitBlockingState =
    isTopicBlocked(
        "profit-loss",
        profitStats,
        graph
    );


assert(
    profitBlockingState.blocked ===
        true,
    "Profit & Loss is blocked by weak Percentage"
);


assert(
    profitBlockingState.blockers.some(
        blocker =>
            blocker.topicId ===
            "percentage"
    ),
    "Percentage is identified as the Profit & Loss blocker"
);


/*
 * Placement check:
 *
 * Because Percentage is already weak, the learner should
 * remain at Percentage rather than jump to Profit & Loss.
 */

const profitRecommendation =
    recommendGraphAwareStartingTopic(
        profitStats,
        graph
    );


assert(
    profitRecommendation.topicId ===
        "percentage",
    "Weak Percentage keeps learner at Percentage"
);

/* ============================================================
   TEST 12 — Candidate Topics
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 12 — Candidate Topics"
);

console.log(
    "--------------------------------------------"
);


const candidates =
    findCandidateTopics(
        strongStats,
        graph
    );


assert(
    candidates.includes(
        "profit-loss"
    ),
    "Unassessed Profit & Loss is a candidate"
);


assert(
    !candidates.includes(
        "percentage"
    ),
    "Assessed Percentage is not a candidate"
);



/* ============================================================
   TEST 13 — Explain Readiness
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 13 — Topic Readiness Explanation"
);

console.log(
    "--------------------------------------------"
);


const explanation =
    explainTopicReadiness(
        "percentage",
        startingStats,
        graph
    );


assert(
    explanation.topicId ===
        "percentage",
    "Readiness explanation contains topic ID"
);


assert(
    explanation.accuracy ===
        0,
    "Readiness explanation contains accuracy"
);


assert(
    explanation.prerequisites.length ===
        2,
    "Readiness explanation contains prerequisites"
);


assert(
    explanation.relatedTopics.length ===
        1 &&
    explanation.relatedTopics.includes(
        "ratio-proportion"
    ),
    "Percentage related topic is informational and does not block placement"
);


assert(
    explanation.blocked ===
        true,
    "Percentage readiness is correctly marked blocked"
);



/* ============================================================
   TEST 14 — Related Topic Still Informational
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 14 — Related Topic Information"
);

console.log(
    "--------------------------------------------"
);


const profitExplanation =
    explainTopicReadiness(
        "profit-loss",
        profitStats,
        graph
    );


assert(
    profitExplanation.relatedTopics.includes(
        "ratio-proportion"
    ),
    "Ratio-Proportion appears as related information"
);


assert(
    profitExplanation.prerequisites.length ===
        1,
    "Profit & Loss has one prerequisite"
);


assert(
    profitExplanation.prerequisites[0].topicId ===
        "percentage",
    "Percentage remains the blocking prerequisite"
);



/* ============================================================
   FINAL
   ============================================================ */

console.log("");

console.log(
    "============================================"
);

console.log(
    " STEP 21 TEST SUMMARY"
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
        "✓ ALL GRAPH-AWARE DIAGNOSTIC TESTS PASSED"
    );

    console.log(
        "✓ STEP 21 COMPLETE"
    );

}
else {

    console.log(
        "✗ STEP 21 FAILED — CHECK ERRORS ABOVE"
    );

    process.exitCode = 1;
}

console.log("");

console.log(
    "============================================"
);

console.log("");





