import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";


/* ============================================================
   Paths
   ============================================================ */

const __filename =
    fileURLToPath(import.meta.url);

const __dirname =
    path.dirname(__filename);

const root =
    path.resolve(
        __dirname,
        "../.."
    );


const pathwaysDir =
    path.join(
        root,
        "data",
        "pathways"
    );


const topicsDir =
    path.join(
        root,
        "data",
        "topics"
    );


const graphPath =
    path.join(
        root,
        "data",
        "taxonomy",
        "topic-graph.json"
    );


/* ============================================================
   Helpers
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


function loadJson(filePath) {

    let text =
        fs.readFileSync(
            filePath,
            "utf8"
        );


    /*
     * Remove UTF-8 BOM when PowerShell
     * has created the file.
     */

    if (
        text.length > 0 &&
        text.charCodeAt(0) === 0xFEFF
    ) {

        text =
            text.slice(1);
    }


    return JSON.parse(
        text
    );
}


/* ============================================================
   Header
   ============================================================ */

console.log("");

console.log(
    "============================================"
);

console.log(
    " STEP 17 — VALIDATING TOPIC MAP"
);

console.log(
    "============================================"
);

console.log("");


/* ============================================================
   TEST 1 — Pathway files
   ============================================================ */

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 1 — Pathway Files"
);

console.log(
    "--------------------------------------------"
);


const pathwayFiles = [
    "foundation-pathway.json",
    "arithmetic-pathway.json",
    "competitive-pathway.json"
];


const pathways = {};


for (
    const file
    of pathwayFiles
) {

    const filePath =
        path.join(
            pathwaysDir,
            file
        );


    if (
        !fs.existsSync(
            filePath
        )
    ) {

        fail(
            `Missing pathway: ${file}`
        );

        continue;
    }


    try {

        const data =
            loadJson(
                filePath
            );


        pathways[data.id] =
            data;


        pass(
            `Valid pathway JSON: ${data.id}`
        );

    }
    catch (error) {

        fail(
            `Invalid pathway JSON: ${file}`
        );
    }
}


/* ============================================================
   TEST 2 — Prototype topics exist
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 2 — Topic References"
);

console.log(
    "--------------------------------------------"
);


const expectedTopics = [
    "number-system",
    "fractions",
    "decimals",
    "ratio-proportion",
    "percentage",
    "profit-loss"
];


for (
    const topicId
    of expectedTopics
) {

    const topicPath =
        path.join(
            topicsDir,
            topicId,
            "topic.json"
        );


    if (
        fs.existsSync(
            topicPath
        )
    ) {

        pass(
            `Topic exists: ${topicId}`
        );

    }
    else {

        fail(
            `Missing topic: ${topicId}`
        );
    }
}


/* ============================================================
   TEST 3 — No broken pathway references
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 3 — Broken Pathway References"
);

console.log(
    "--------------------------------------------"
);


for (
    const pathway
    of Object.values(
        pathways
    )
) {

    for (
        const topicId
        of pathway.topics || []
    ) {

        const topicPath =
            path.join(
                topicsDir,
                topicId,
                "topic.json"
            );


        if (
            fs.existsSync(
                topicPath
            )
        ) {

            pass(
                `${pathway.id} → ${topicId}`
            );

        }
        else {

            fail(
                `Broken reference: ${pathway.id} → ${topicId}`
            );
        }
    }
}


/* ============================================================
   TEST 4 — Graph nodes
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 4 — Graph Nodes"
);

console.log(
    "--------------------------------------------"
);


let graph;


try {

    graph =
        loadJson(
            graphPath
        );

    pass(
        "topic-graph.json loaded"
    );

}
catch {

    fail(
        "topic-graph.json could not be loaded"
    );
}


const graphNodeIds =
    new Set(
        (graph?.nodes || [])
            .map(
                node =>
                    node.topicId
            )
    );


for (
    const topicId
    of expectedTopics
) {

    if (
        graphNodeIds.has(
            topicId
        )
    ) {

        pass(
            `Graph node exists: ${topicId}`
        );

    }
    else {

        fail(
            `Graph node missing: ${topicId}`
        );
    }
}


/* ============================================================
   TEST 5 — Graph edge integrity
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 5 — Graph Edge Integrity"
);

console.log(
    "--------------------------------------------"
);


for (
    const edge
    of graph?.edges || []
) {

    if (
        !graphNodeIds.has(
            edge.from
        )
    ) {

        fail(
            `Broken graph source: ${edge.from}`
        );

        continue;
    }


    if (
        !graphNodeIds.has(
            edge.to
        )
    ) {

        fail(
            `Broken graph destination: ${edge.to}`
        );

        continue;
    }


    pass(
        `Valid edge: ${edge.from} → ${edge.to}`
    );
}


/* ============================================================
   TEST 6 — Important prerequisite
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 6 — Percentage → Profit & Loss"
);

console.log(
    "--------------------------------------------"
);


const percentageProfitEdge =
    (graph?.edges || [])
        .find(
            edge =>
                edge.from ===
                    "percentage" &&
                edge.to ===
                    "profit-loss"
        );


if (
    percentageProfitEdge &&
    percentageProfitEdge.relation ===
        "prerequisite"
) {

    pass(
        "Percentage → Profit & Loss is a prerequisite"
    );

}
else {

    fail(
        "Percentage → Profit & Loss prerequisite missing"
    );
}


/* ============================================================
   TEST 7 — Ratio must remain supporting
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 7 — Supporting Relationship"
);

console.log(
    "--------------------------------------------"
);


const ratioProfitEdge =
    (graph?.edges || [])
        .find(
            edge =>
                edge.from ===
                    "ratio-proportion" &&
                edge.to ===
                    "profit-loss"
        );


if (
    ratioProfitEdge &&
    ratioProfitEdge.relation ===
        "related"
) {

    pass(
        "Ratio-Proportion → Profit & Loss is supporting"
    );

}
else {

    fail(
        "Ratio-Proportion → Profit & Loss relationship incorrect"
    );
}


/* ============================================================
   TEST 8 — Recommended order
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 8 — Foundation Order"
);

console.log(
    "--------------------------------------------"
);


const foundation =
    pathways[
        "foundation-pathway"
    ];


const expectedOrder = [
    "number-system",
    "fractions",
    "decimals",
    "ratio-proportion",
    "percentage",
    "profit-loss"
];


const orderMatches =
    JSON.stringify(
        foundation?.recommendedOrder
    ) ===
    JSON.stringify(
        expectedOrder
    );


if (
    orderMatches
) {

    pass(
        "Foundation progression order is correct"
    );

}
else {

    fail(
        "Foundation progression order is incorrect"
    );
}


/* ============================================================
   TEST 9 — No duplicate pathway topics
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 9 — Duplicate Detection"
);

console.log(
    "--------------------------------------------"
);


for (
    const pathway
    of Object.values(
        pathways
    )
) {

    const topics =
        pathway.topics || [];


    const unique =
        new Set(
            topics
        );


    if (
        unique.size ===
            topics.length
    ) {

        pass(
            `No duplicate topics: ${pathway.id}`
        );

    }
    else {

        fail(
            `Duplicate topics found: ${pathway.id}`
        );
    }
}


/* ============================================================
   TEST 10 — Pathway graph consistency
   ============================================================ */

console.log("");

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 10 — Pathway / Graph Consistency"
);

console.log(
    "--------------------------------------------"
);


for (
    const pathway
    of Object.values(
        pathways
    )
) {

    const pathwayTopics =
        new Set(
            pathway.topics || []
        );


    for (
        const edge
        of graph?.edges || []
    ) {

        if (
            pathwayTopics.has(
                edge.from
            ) &&
            pathwayTopics.has(
                edge.to
            )
        ) {

            pass(
                `${pathway.id}: graph relationship ${edge.from} → ${edge.to}`
            );
        }
    }
}


/* ============================================================
   FINAL
   ============================================================ */

console.log("");

console.log(
    "============================================"
);

console.log(
    " STEP 17 TEST SUMMARY"
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
        "✓ ALL TOPIC MAP TESTS PASSED"
    );

    console.log(
        "✓ STEP 17 COMPLETE"
    );

}
else {

    console.log(
        "✗ STEP 17 FAILED — REVIEW FAILURES ABOVE"
    );

    process.exitCode = 1;
}

console.log("");

console.log(
    "============================================"
);

console.log("");
