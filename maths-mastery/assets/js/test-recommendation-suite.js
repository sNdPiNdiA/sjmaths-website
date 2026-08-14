import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

import {
    recommendNextTopics
} from "./recommendation-engine.js";


/* ============================================================
   PATHS
   ============================================================ */

const __filename =
    fileURLToPath(import.meta.url);

const __dirname =
    path.dirname(__filename);

const masteryRoot =
    path.resolve(
        __dirname,
        "../.."
    );


const graphPath =
    path.join(
        masteryRoot,
        "data",
        "taxonomy",
        "topic-graph.json"
    );


const rulesPath =
    path.join(
        masteryRoot,
        "data",
        "config",
        "recommendation-rules.json"
    );


/* ============================================================
   BOM-SAFE JSON LOADER
   ============================================================ */

function loadJson(filePath) {

    let text =
        fs.readFileSync(
            filePath,
            "utf8"
        );

    if (
        text.length > 0 &&
        text.charCodeAt(0) === 0xFEFF
    ) {
        text = text.slice(1);
    }

    return JSON.parse(text);
}


const graph =
    loadJson(graphPath);

const rules =
    loadJson(rulesPath);


/* ============================================================
   COMMON TOPIC DATA
   ============================================================ */

const topicData = {

    "profit-loss": {

        examRelevance: {

            ssc: 100,
            banking: 95,
            railway: 95,
            defence: 90,
            teaching: 85
        }
    },

    "percentage": {

        examRelevance: {

            ssc: 100,
            banking: 100,
            railway: 95,
            defence: 90,
            teaching: 85
        }
    },

    "ratio-proportion": {

        examRelevance: {

            ssc: 95,
            banking: 100,
            railway: 95,
            defence: 90,
            teaching: 90
        }
    }
};


/* ============================================================
   TEST HELPERS
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


function runRecommendation(student) {

    return recommendNextTopics({

        student,
        graph,
        rules,
        topicData
    });
}


/* ============================================================
   TEST 1
   Strong Percentage → Profit & Loss
   ============================================================ */

section(
    1,
    "Strong Percentage → Profit & Loss"
);


const student1 = {

    currentTopic: "percentage",

    selectedExam: "ssc",

    currentMastery: 78,

    completedTopics: [
        "number-system",
        "fractions",
        "decimals",
        "percentage"
    ],

    recentTopics: [
        "decimals",
        "percentage"
    ],

    topicMastery: {

        "number-system": 92,
        "fractions": 89,
        "decimals": 84,
        "percentage": 78
    },

    skills: {

        "percentage-calculation": 88,
        "percentage-increase": 82,
        "percentage-decrease": 79,
        "successive-percentage-change": 61,
        "reverse-percentage": 55
    }
};


const result1 =
    runRecommendation(student1);


if (
    result1.primaryRecommendation?.topicId ===
        "profit-loss"
) {

    pass(
        "Strong Percentage recommends Profit & Loss"
    );

}
else {

    fail(
        "Strong Percentage did not recommend Profit & Loss"
    );
}


if (
    result1.weakSkills[0]?.skillId ===
        "reverse-percentage"
) {

    pass(
        "Weakest skill correctly identified as Reverse Percentage"
    );

}
else {

    fail(
        "Weakest skill detection failed"
    );
}


/* ============================================================
   TEST 2
   Weak Percentage should block Profit & Loss
   ============================================================ */

section(
    2,
    "Weak Percentage → Prerequisite Gate"
);


const student2 = {

    currentTopic: "percentage",

    selectedExam: "ssc",

    currentMastery: 52,

    completedTopics: [
        "number-system",
        "fractions",
        "decimals",
        "percentage"
    ],

    recentTopics: [
        "percentage"
    ],

    topicMastery: {

        "number-system": 90,
        "fractions": 82,
        "decimals": 75,
        "percentage": 52
    },

    skills: {

        "percentage-calculation": 55,
        "percentage-increase": 50,
        "percentage-decrease": 48,
        "successive-percentage-change": 42,
        "reverse-percentage": 35
    }
};


const result2 =
    runRecommendation(student2);


const blockedProfitLoss =
    result2.blocked.some(
        item =>
            item.topicId ===
                "profit-loss"
    );


if (blockedProfitLoss) {

    pass(
        "Profit & Loss correctly blocked when Percentage mastery is below 70%"
    );

}
else {

    fail(
        "Profit & Loss was not blocked despite weak Percentage mastery"
    );
}


/* ============================================================
   TEST 3
   Exact 70% prerequisite should pass
   ============================================================ */

section(
    3,
    "Boundary Test — Exactly 70%"
);


const student3 = {

    currentTopic: "percentage",

    selectedExam: "ssc",

    currentMastery: 70,

    completedTopics: [
        "percentage"
    ],

    recentTopics: [],

    topicMastery: {

        "percentage": 70
    },

    skills: {

        "percentage-calculation": 70
    }
};


const result3 =
    runRecommendation(student3);


const result3ProfitLoss =
    result3.recommendations.find(
        item =>
            item.topicId ===
                "profit-loss"
    );


if (result3ProfitLoss) {

    pass(
        "Exactly 70% prerequisite passes the hard gate"
    );

}
else {

    fail(
        "Exactly 70% prerequisite incorrectly blocked"
    );
}


/* ============================================================
   TEST 4
   Below 70% should fail
   ============================================================ */

section(
    4,
    "Boundary Test — 69%"
);


const student4 = {

    currentTopic: "percentage",

    selectedExam: "ssc",

    currentMastery: 69,

    completedTopics: [
        "percentage"
    ],

    recentTopics: [],

    topicMastery: {

        "percentage": 69
    },

    skills: {

        "percentage-calculation": 69
    }
};


const result4 =
    runRecommendation(student4);


const blocked69 =
    result4.blocked.some(
        item =>
            item.topicId ===
                "profit-loss"
    );


if (blocked69) {

    pass(
        "69% correctly fails the prerequisite gate"
    );

}
else {

    fail(
        "69% incorrectly passed the prerequisite gate"
    );
}


/* ============================================================
   TEST 5
   Already completed topic should not be recommended
   ============================================================ */

section(
    5,
    "Completed Topic Exclusion"
);


const student5 = {

    currentTopic: "percentage",

    selectedExam: "ssc",

    currentMastery: 90,

    completedTopics: [
        "percentage",
        "profit-loss"
    ],

    recentTopics: [
        "percentage"
    ],

    topicMastery: {

        "percentage": 90,
        "profit-loss": 85
    },

    skills: {

        "percentage-calculation": 90
    }
};


const result5 =
    runRecommendation(student5);


const recommendedCompleted =
    result5.recommendations.some(
        item =>
            item.topicId ===
                "profit-loss"
    );


if (!recommendedCompleted) {

    pass(
        "Completed Profit & Loss is excluded"
    );

}
else {

    fail(
        "Completed Profit & Loss was incorrectly recommended"
    );
}


/* ============================================================
   TEST 6
   Recently completed topic exclusion
   ============================================================ */

section(
    6,
    "Recently Completed Topic Exclusion"
);


const student6 = {

    currentTopic: "percentage",

    selectedExam: "ssc",

    currentMastery: 90,

    completedTopics: [
        "percentage"
    ],

    recentTopics: [
        "percentage",
        "profit-loss"
    ],

    topicMastery: {

        "percentage": 90
    },

    skills: {

        "percentage-calculation": 90
    }
};


const result6 =
    runRecommendation(student6);


const recentRecommended =
    result6.recommendations.some(
        item =>
            item.topicId ===
                "profit-loss"
    );


if (!recentRecommended) {

    pass(
        "Recently completed Profit & Loss is excluded"
    );

}
else {

    fail(
        "Recently completed Profit & Loss was recommended"
    );
}


/* ============================================================
   TEST 7
   Exam relevance affects score
   ============================================================ */

section(
    7,
    "Exam Relevance Influence"
);


const student7SSC = {

    currentTopic: "percentage",

    selectedExam: "ssc",

    currentMastery: 80,

    completedTopics: [
        "percentage"
    ],

    recentTopics: [],

    topicMastery: {

        "percentage": 80
    },

    skills: {

        "percentage-calculation": 85
    }
};


const student7Banking = {

    ...student7SSC,

    selectedExam: "banking"
};


const result7SSC =
    runRecommendation(student7SSC);

const result7Banking =
    runRecommendation(student7Banking);


const sscScore =
    result7SSC.primaryRecommendation?.score ?? 0;

const bankingScore =
    result7Banking.primaryRecommendation?.score ?? 0;


if (
    typeof sscScore === "number" &&
    typeof bankingScore === "number"
) {

    pass(
        "Exam-specific recommendation scoring is functioning"
    );

}
else {

    fail(
        "Exam-specific scoring failed"
    );
}


/* ============================================================
   TEST 8
   Weak skill should be surfaced
   ============================================================ */

section(
    8,
    "Weak Skill Detection"
);


const student8 = {

    currentTopic: "percentage",

    selectedExam: "ssc",

    currentMastery: 82,

    completedTopics: [
        "percentage"
    ],

    recentTopics: [],

    topicMastery: {

        "percentage": 82
    },

    skills: {

        "percentage-calculation": 91,
        "percentage-increase": 88,
        "percentage-decrease": 86,
        "successive-percentage-change": 58,
        "reverse-percentage": 76
    }
};


const result8 =
    runRecommendation(student8);


if (
    result8.weakSkills[0]?.skillId ===
        "successive-percentage-change"
) {

    pass(
        "Successive Percentage Change correctly identified as weakest skill"
    );

}
else {

    fail(
        "Weak skill ranking failed"
    );
}


/* ============================================================
   TEST 9
   High mastery should remain eligible
   ============================================================ */

section(
    9,
    "High Mastery Progression"
);


const student9 = {

    currentTopic: "percentage",

    selectedExam: "ssc",

    currentMastery: 95,

    completedTopics: [
        "number-system",
        "fractions",
        "decimals",
        "percentage"
    ],

    recentTopics: [],

    topicMastery: {

        "number-system": 95,
        "fractions": 95,
        "decimals": 95,
        "percentage": 95
    },

    skills: {

        "percentage-calculation": 95,
        "percentage-increase": 94,
        "percentage-decrease": 94,
        "successive-percentage-change": 92,
        "reverse-percentage": 90
    }
};


const result9 =
    runRecommendation(student9);


if (
    result9.primaryRecommendation
) {

    pass(
        "High mastery student receives a next-topic recommendation"
    );

}
else {

    fail(
        "High mastery student received no recommendation"
    );
}


/* ============================================================
   TEST 10
   No false recommendation when prerequisite absent
   ============================================================ */

section(
    10,
    "False Recommendation Prevention"
);


const student10 = {

    currentTopic: "percentage",

    selectedExam: "ssc",

    currentMastery: 40,

    completedTopics: [],

    recentTopics: [],

    topicMastery: {},

    skills: {}
};


const result10 =
    runRecommendation(student10);


const falseProfitLoss =
    result10.recommendations.some(
        item =>
            item.topicId ===
                "profit-loss"
    );


if (!falseProfitLoss) {

    pass(
        "Engine does not falsely recommend Profit & Loss without prerequisite mastery"
    );

}
else {

    fail(
        "Engine falsely recommended Profit & Loss"
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
    " STEP 11 TEST SUMMARY"
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
        "✓ ALL RECOMMENDATION TESTS PASSED"
    );

    console.log(
        "✓ STEP 11 COMPLETE"
    );

}
else {

    console.log(
        "✗ STEP 11 FAILED — REVIEW FAILURES ABOVE"
    );

    process.exitCode = 1;
}

console.log("");

console.log(
    "============================================"
);

console.log("");
