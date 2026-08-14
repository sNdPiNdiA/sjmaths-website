import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

import {
    recommendNextTopics
} from "./recommendation-engine.js";


/* ============================================================
   Resolve paths relative to this file
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
   BOM-safe JSON loader
   ============================================================ */

function loadJson(filePath) {

    if (!fs.existsSync(filePath)) {

        throw new Error(
            `JSON file not found: ${filePath}`
        );
    }


    let text =
        fs.readFileSync(
            filePath,
            "utf8"
        );


    /*
     * Remove UTF-8 BOM if present.
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


/* ============================================================
   Load production JSON
   ============================================================ */

const graph =
    loadJson(graphPath);


const rules =
    loadJson(rulesPath);


console.log(
    "✓ Graph JSON loaded"
);

console.log(
    "✓ Recommendation rules JSON loaded"
);


/* ============================================================
   Student test scenario
   ============================================================ */

const student = {

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


/* ============================================================
   Topic-specific exam relevance
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
    }
};


/* ============================================================
   Run engine
   ============================================================ */

const result =
    recommendNextTopics({

        student,

        graph,

        rules,

        topicData
    });


/* ============================================================
   Display result
   ============================================================ */

console.log("");

console.log(
    "============================================"
);

console.log(
    " SJMaths RECOMMENDATION ENGINE TEST"
);

console.log(
    "============================================"
);

console.log("");

console.log(
    "Graph:",
    graphPath
);

console.log(
    "Rules:",
    rulesPath
);

console.log("");

console.log(
    "Current Topic:",
    result.currentTopic
);

console.log(
    "Current Mastery:",
    result.currentMastery + "%"
);

console.log(
    "Selected Exam:",
    result.selectedExam
);

console.log("");


/* ============================================================
   Weak skills
   ============================================================ */

console.log(
    "Weak Skills:"
);

if (
    result.weakSkills.length === 0
) {

    console.log(
        "  NONE"
    );

}
else {

    for (
        const skill
        of result.weakSkills
    ) {

        console.log(
            "  -",
            skill.skillId,
            "|",
            skill.score + "%",
            "| gap:",
            skill.gap + "%"
        );
    }
}


/* ============================================================
   Recommendations
   ============================================================ */

console.log("");

console.log(
    "Recommendations:"
);

if (
    result.recommendations.length === 0
) {

    console.log(
        "  NONE"
    );

}
else {

    for (
        const recommendation
        of result.recommendations
    ) {

        console.log(
            "  -",
            recommendation.topicId,
            "| score:",
            recommendation.score,
            "| relation:",
            recommendation.relation
        );

        console.log(
            "    prerequisite:",
            recommendation.components.prerequisite
        );

        console.log(
            "    exam:",
            recommendation.components.examRelevance
        );

        console.log(
            "    continuity:",
            recommendation.components.pathContinuity
        );

        console.log(
            "    mastery fit:",
            recommendation.components.masteryFit
        );

        console.log(
            "    difficulty:",
            recommendation.components.difficultyFit
        );

        console.log(
            "    reason:",
            recommendation.reason.text
        );
    }
}


/* ============================================================
   Blocked candidates
   ============================================================ */

console.log("");

console.log(
    "Blocked Candidates:"
);

if (
    result.blocked.length === 0
) {

    console.log(
        "  NONE"
    );

}
else {

    for (
        const item
        of result.blocked
    ) {

        console.log(
            "  -",
            item.topicId,
            "| score:",
            item.score
        );
    }
}


/* ============================================================
   Test 1 — Weak skill
   ============================================================ */

console.log("");

if (
    result.weakSkills.length > 0 &&
    result.weakSkills[0].skillId ===
        "reverse-percentage"
) {

    console.log(
        "✓ WEAK SKILL DETECTION = reverse-percentage"
    );

}
else {

    console.log(
        "✗ WEAK SKILL DETECTION FAILED"
    );

    process.exitCode = 1;
}


/* ============================================================
   Test 2 — Primary recommendation
   ============================================================ */

if (
    result.primaryRecommendation?.topicId ===
        "profit-loss"
) {

    console.log(
        "✓ PRIMARY RECOMMENDATION = profit-loss"
    );

}
else {

    console.log(
        "✗ PRIMARY RECOMMENDATION TEST FAILED"
    );

    process.exitCode = 1;
}


/* ============================================================
   Test 3 — Percentage prerequisite
   ============================================================ */

const profitLoss =
    result.recommendations.find(
        item =>
            item.topicId ===
                "profit-loss"
    );


if (
    profitLoss &&
    profitLoss.prerequisites.some(
        item =>
            item.topicId ===
                "percentage"
    )
) {

    console.log(
        "✓ Percentage prerequisite detected"
    );

}
else {

    console.log(
        "✗ Percentage prerequisite test failed"
    );

    process.exitCode = 1;
}


/* ============================================================
   Test 4 — Ratio-Proportion is NOT blocking
   ============================================================ */

const ratioEdge =
    graph.edges.find(
        edge =>
            edge.from ===
                "ratio-proportion" &&
            edge.to ===
                "profit-loss"
    );


if (
    ratioEdge &&
    ratioEdge.relation ===
        "related"
) {

    console.log(
        "✓ Ratio-Proportion is supporting/related"
    );

}
else {

    console.log(
        "✗ Ratio-Proportion graph relationship failed"
    );

    process.exitCode = 1;
}


/* ============================================================
   Final
   ============================================================ */

console.log("");

console.log(
    "============================================"
);

if (
    result.primaryRecommendation?.topicId ===
        "profit-loss" &&

    result.weakSkills.length > 0 &&

    result.weakSkills[0].skillId ===
        "reverse-percentage" &&

    profitLoss
) {

    console.log(
        " STEP 10 ENGINE TEST PASSED"
    );

}
else {

    console.log(
        " STEP 10 ENGINE TEST FAILED"
    );

}

console.log(
    "============================================"
);

console.log("");
