import {
    calculateAccuracy,
    calculateConceptPerformance,
    calculateSkillPerformance,
    calculateMiniTestPerformance,
    calculateTopicMastery,
    calculateMastery,
    determineStatus,
    getWeakSkills,
    getMasterySummary
} from "./mastery-engine.js";


/* ============================================================
   Test helpers
   ============================================================ */

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


function section(number, title) {

    console.log("");

    console.log(
        "--------------------------------------------"
    );

    console.log(
        `TEST ${number} — ${title}`
    );

    console.log(
        "--------------------------------------------"
    );
}


/* ============================================================
   Mastery rules
   ============================================================ */

const rules = {

    algorithm: {

        version:
            "1.0.0",

        weights: {

            topicAccuracy:
                0.50,

            conceptPerformance:
                0.20,

            skillPerformance:
                0.15,

            miniTestPerformance:
                0.15
        },

        minimumEvidence: {

            attemptsForReliableScore:
                3,

            attemptsForMasteredStatus:
                5
        }
    },

    statusLevels: {

        "not-started": {

            minimumScore:
                0
        },

        learning: {

            minimumScore:
                40
        },

        developing: {

            minimumScore:
                60
        },

        proficient: {

            minimumScore:
                75
        },

        mastered: {

            minimumScore:
                90,

            minimumAttempts:
                5
        }
    }
};


/* ============================================================
   TEST 1
   Accuracy
   ============================================================ */

section(
    1,
    "Accuracy Calculation"
);


const accuracy =
    calculateAccuracy({

        attempts: 10,

        correct: 8,

        incorrect: 2,

        skipped: 0
    });


if (
    accuracy === 80
) {

    pass(
        "80% accuracy calculated correctly"
    );

}
else {

    fail(
        `Accuracy incorrect: ${accuracy}`
    );
}


/* ============================================================
   TEST 2
   Zero attempts
   ============================================================ */

section(
    2,
    "Zero Evidence"
);


const zeroAccuracy =
    calculateAccuracy({

        attempts: 0,

        correct: 0,

        incorrect: 0,

        skipped: 0
    });


if (
    zeroAccuracy === 0
) {

    pass(
        "Zero attempts produces zero accuracy"
    );

}
else {

    fail(
        "Zero-attempt accuracy is incorrect"
    );
}


/* ============================================================
   TEST 3
   Concept performance
   ============================================================ */

section(
    3,
    "Concept Performance"
);


const concepts = {

    basics: {

        conceptId:
            "basics",

        evidence: {

            attempts: 10,

            correct: 9,

            incorrect: 1,

            skipped: 0
        }
    },

    applications: {

        conceptId:
            "applications",

        evidence: {

            attempts: 10,

            correct: 7,

            incorrect: 3,

            skipped: 0
        }
    }
};


const conceptScore =
    calculateConceptPerformance(
        concepts
    );


if (
    conceptScore === 80
) {

    pass(
        "Concept performance calculated correctly"
    );

}
else {

    fail(
        `Concept performance incorrect: ${conceptScore}`
    );
}


/* ============================================================
   TEST 4
   Skill performance
   ============================================================ */

section(
    4,
    "Skill Performance"
);


const skills = {

    calculation: {

        skillId:
            "calculation",

        score:
            90,

        evidence: {

            attempts: 10,

            correct: 9,

            incorrect: 1,

            skipped: 0
        }
    },

    reverse: {

        skillId:
            "reverse",

        score:
            60,

        evidence: {

            attempts: 10,

            correct: 6,

            incorrect: 4,

            skipped: 0
        }
    }
};


const skillScore =
    calculateSkillPerformance(
        skills
    );


if (
    skillScore === 75
) {

    pass(
        "Skill performance calculated correctly"
    );

}
else {

    fail(
        `Skill performance incorrect: ${skillScore}`
    );
}


/* ============================================================
   TEST 5
   Mini-test performance
   ============================================================ */

section(
    5,
    "Mini-Test Performance"
);


const miniTests = {

    foundation: {

        testId:
            "foundation",

        attempts:
            2,

        bestScore:
            80,

        bestAccuracy:
            85
    },

    advanced: {

        testId:
            "advanced",

        attempts:
            1,

        bestScore:
            90,

        bestAccuracy:
            92
    }
};


const miniScore =
    calculateMiniTestPerformance(
        miniTests
    );


if (
    miniScore === 85
) {

    pass(
        "Mini-test performance calculated correctly"
    );

}
else {

    fail(
        `Mini-test performance incorrect: ${miniScore}`
    );
}


/* ============================================================
   TEST 6
   Topic mastery
   ============================================================ */

section(
    6,
    "Topic Mastery"
);


const strongTopic = {

    topicId:
        "percentage",

    status:
        "developing",

    evidence: {

        attempts:
            10,

        correct:
            9,

        incorrect:
            1,

        skipped:
            0
    },

    concepts,

    skills,

    miniTests
};


const topicMastery =
    calculateTopicMastery(
        strongTopic,
        rules
    );


if (
    topicMastery.score === 85
) {

    pass(
        "Topic mastery weighted score = 85 calculated correctly"
    );

}
else {

    fail(
        `Topic mastery score incorrect: ${topicMastery.score}`
    );
}


/* ============================================================
   TEST 7
   Reliable evidence
   ============================================================ */

section(
    7,
    "Reliable Evidence"
);


if (
    topicMastery.reliable === true &&
    topicMastery.attempts === 10
) {

    pass(
        "Topic becomes reliable after minimum evidence"
    );

}
else {

    fail(
        "Reliable evidence detection failed"
    );
}


/* ============================================================
   TEST 8
   Status — mastered
   ============================================================ */

section(
    8,
    "Mastered Status"
);


const mastered =
    determineStatus(
        95,
        10,
        rules
    );


if (
    mastered ===
        "mastered"
) {

    pass(
        "95% with sufficient attempts becomes mastered"
    );

}
else {

    fail(
        `Mastered status incorrect: ${mastered}`
    );
}


/* ============================================================
   TEST 9
   Status — proficient
   ============================================================ */

section(
    9,
    "Proficient Status"
);


const proficient =
    determineStatus(
        82,
        5,
        rules
    );


if (
    proficient ===
        "proficient"
) {

    pass(
        "82% becomes proficient"
    );

}
else {

    fail(
        `Proficient status incorrect: ${proficient}`
    );
}


/* ============================================================
   TEST 10
   Status — developing
   ============================================================ */

section(
    10,
    "Developing Status"
);


const developing =
    determineStatus(
        65,
        5,
        rules
    );


if (
    developing ===
        "developing"
) {

    pass(
        "65% becomes developing"
    );

}
else {

    fail(
        `Developing status incorrect: ${developing}`
    );
}


/* ============================================================
   TEST 11
   Status — learning
   ============================================================ */

section(
    11,
    "Learning Status"
);


const learning =
    determineStatus(
        45,
        3,
        rules
    );


if (
    learning ===
        "learning"
) {

    pass(
        "45% becomes learning"
    );

}
else {

    fail(
        `Learning status incorrect: ${learning}`
    );
}


/* ============================================================
   TEST 12
   No evidence
   ============================================================ */

section(
    12,
    "Not Started Status"
);


const notStarted =
    determineStatus(
        0,
        0,
        rules
    );


if (
    notStarted ===
        "not-started"
) {

    pass(
        "Zero evidence becomes not-started"
    );

}
else {

    fail(
        `Not-started status incorrect: ${notStarted}`
    );
}


/* ============================================================
   TEST 13
   Weak skill detection
   ============================================================ */

section(
    13,
    "Weak Skill Detection"
);


const weakSkills =
    getWeakSkills(
        strongTopic,
        70
    );


if (
    weakSkills.length === 1 &&
    weakSkills[0].skillId ===
        "reverse" &&
    weakSkills[0].score === 60
) {

    pass(
        "Weak skill correctly identified"
    );

}
else {

    fail(
        "Weak skill detection failed"
    );
}


/* ============================================================
   TEST 14
   Complete mastery calculation
   ============================================================ */

section(
    14,
    "Complete Mastery Calculation"
);


const progress = {

    version:
        "1.0.0",

    studentId:
        "test-student",

    topics: {

        percentage:
            strongTopic
    }
};


const mastery =
    calculateMastery(
        progress,
        rules
    );


if (
    mastery.topics.percentage &&
    mastery.topics.percentage.score ===
        topicMastery.score
) {

    pass(
        "Complete mastery calculation works"
    );

}
else {

    fail(
        "Complete mastery calculation failed"
    );
}


/* ============================================================
   TEST 15
   Mastery algorithm version
   ============================================================ */

section(
    15,
    "Algorithm Version"
);


if (
    mastery.version ===
        "1.0.0"
) {

    pass(
        "Mastery algorithm version is stored"
    );

}
else {

    fail(
        "Mastery algorithm version missing"
    );
}


/* ============================================================
   TEST 16
   Mastery summary
   ============================================================ */

section(
    16,
    "Mastery Summary"
);


const summary =
    getMasterySummary(
        mastery
    );


if (
    summary.totalTopics === 1 &&
    summary.proficient === 1
) {

    pass(
        "Mastery summary calculated correctly"
    );

}
else {

    fail(
        "Mastery summary incorrect"
    );
}


/* ============================================================
   TEST 17
   Evidence remains source of truth
   ============================================================ */

section(
    17,
    "Evidence Preservation"
);


if (
    strongTopic.evidence.correct === 9 &&
    strongTopic.evidence.attempts === 10
) {

    pass(
        "Mastery calculation does not modify evidence"
    );

}
else {

    fail(
        "Mastery calculation modified evidence"
    );
}


/* ============================================================
   SUMMARY
   ============================================================ */

console.log("");

console.log(
    "============================================"
);

console.log(
    " STEP 14 TEST SUMMARY"
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
        "✓ ALL MASTERY ENGINE TESTS PASSED"
    );

    console.log(
        "✓ STEP 14 COMPLETE"
    );

}
else {

    console.log(
        "✗ STEP 14 FAILED — REVIEW FAILURES ABOVE"
    );

    process.exitCode = 1;
}

console.log("");

console.log(
    "============================================"
);

console.log("");

