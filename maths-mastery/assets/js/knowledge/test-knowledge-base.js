import fs from "fs";
import path from "path";


const root =
    path.resolve(
        process.cwd(),
        "maths-mastery",
        "data",
        "knowledge"
    );


function readJson(
    filePath
) {

    const raw =
        fs.readFileSync(
            filePath,
            "utf8"
        );

    return JSON.parse(
        raw.replace(
            /^\uFEFF/,
            ""
        )
    );
}


function readDirectory(
    directory
) {

    if (
        !fs.existsSync(
            directory
        )
    ) {

        return [];
    }


    return fs
        .readdirSync(
            directory
        )
        .filter(
            file =>
                file.endsWith(
                    ".json"
                )
        )
        .map(
            file => ({

                file,

                path:
                    path.join(
                        directory,
                        file
                    ),

                data:
                    readJson(
                        path.join(
                            directory,
                            file
                        )
                    )

            })
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


function validateUniqueIds(
    items,
    label
) {

    const ids =
        new Set();


    for (
        const item of items
    ) {

        assert(
            typeof item.data.id ===
                "string" &&
            item.data.id.length > 0,
            `${label} has valid ID: ${item.file}`
        );


        assert(
            !ids.has(
                item.data.id
            ),
            `No duplicate ${label} ID: ${item.data.id}`
        );


        ids.add(
            item.data.id
        );
    }


    return ids;
}


console.log("");
console.log(
    "============================================"
);
console.log(
    " STEP 25 — KNOWLEDGE BASE VALIDATION"
);
console.log(
    "============================================"
);
console.log("");


/* ============================================================
   Load entities
   ============================================================ */

const domains =
    readDirectory(
        path.join(
            root,
            "domains"
        )
    );


const topics =
    readDirectory(
        path.join(
            root,
            "topics"
        )
    );


const concepts =
    readDirectory(
        path.join(
            root,
            "concepts"
        )
    );


const skills =
    readDirectory(
        path.join(
            root,
            "skills"
        )
    );


const exams =
    readDirectory(
        path.join(
            root,
            "exams"
        )
    );


/* ============================================================
   TEST 1 — Entity counts
   ============================================================ */

console.log(
    "--------------------------------------------"
);

console.log(
    "TEST 1 — Knowledge Entities"
);

console.log(
    "--------------------------------------------"
);


assert(
    domains.length > 0,
    "At least one domain exists"
);


assert(
    topics.length > 0,
    "At least one topic exists"
);


assert(
    concepts.length > 0,
    "At least one concept exists"
);


assert(
    skills.length > 0,
    "At least one skill exists"
);


assert(
    exams.length > 0,
    "At least one exam exists"
);


/* ============================================================
   TEST 2 — Unique IDs
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 2 — Unique IDs"
);
console.log(
    "--------------------------------------------"
);


const domainIds =
    validateUniqueIds(
        domains,
        "domain"
    );


const topicIds =
    validateUniqueIds(
        topics,
        "topic"
    );


const conceptIds =
    validateUniqueIds(
        concepts,
        "concept"
    );


const skillIds =
    validateUniqueIds(
        skills,
        "skill"
    );


const examIds =
    validateUniqueIds(
        exams,
        "exam"
    );


/* ============================================================
   TEST 3 — Topic → Domain References
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 3 — Topic References"
);
console.log(
    "--------------------------------------------"
);


for (
    const topic of topics
) {

    assert(
        domainIds.has(
            topic.data.domainId
        ),
        `Topic ${topic.data.id} → domain ${topic.data.domainId}`
    );
}


/* ============================================================
   TEST 4 — Concept → Topic References
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 4 — Concept References"
);
console.log(
    "--------------------------------------------"
);


for (
    const concept of concepts
) {

    assert(
        topicIds.has(
            concept.data.topicId
        ),
        `Concept ${concept.data.id} → topic ${concept.data.topicId}`
    );
}


/* ============================================================
   TEST 5 — Skill → Topic + Concept References
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 5 — Skill References"
);
console.log(
    "--------------------------------------------"
);


for (
    const skill of skills
) {

    assert(
        topicIds.has(
            skill.data.topicId
        ),
        `Skill ${skill.data.id} → topic exists`
    );


    assert(
        conceptIds.has(
            skill.data.conceptId
        ),
        `Skill ${skill.data.id} → concept exists`
    );
}


/* ============================================================
   TEST 6 — Graph Integrity
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 6 — Graph Integrity"
);
console.log(
    "--------------------------------------------"
);


const relationFile =
    path.join(
        root,
        "relations",
        "topic-relations.json"
    );


const relationData =
    readJson(
        relationFile
    );


assert(
    Array.isArray(
        relationData.relations
    ),
    "Topic relation graph is valid"
);


const validRelations = [
    "prerequisite",
    "related",
    "progression"
];


for (
    const relation of
    relationData.relations
) {

    assert(
        topicIds.has(
            relation.from
        ),
        `Graph source exists: ${relation.from}`
    );


    assert(
        topicIds.has(
            relation.to
        ),
        `Graph target exists: ${relation.to}`
    );


    assert(
        validRelations.includes(
            relation.relation
        ),
        `Valid relation: ${relation.from} → ${relation.to}`
    );


    assert(
        typeof relation.strength ===
            "number" &&
        relation.strength >= 0 &&
        relation.strength <= 1,
        `Valid strength: ${relation.from} → ${relation.to}`
    );
}


/* ============================================================
   TEST 7 — Prototype Critical Path
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 7 — Critical Learning Path"
);
console.log(
    "--------------------------------------------"
);


function hasRelation(
    from,
    to,
    relation
) {

    return relationData.relations.some(
        item =>
            item.from === from &&
            item.to === to &&
            item.relation === relation
    );
}


assert(
    hasRelation(
        "percentage",
        "profit-loss",
        "prerequisite"
    ),
    "Percentage → Profit & Loss prerequisite preserved"
);


assert(
    hasRelation(
        "ratio-proportion",
        "profit-loss",
        "related"
    ),
    "Ratio-Proportion → Profit & Loss remains related"
);


/* ============================================================
   TEST 8 — No Self Relations
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 8 — Self Relation Detection"
);
console.log(
    "--------------------------------------------"
);


for (
    const relation of
    relationData.relations
) {

    assert(
        relation.from !==
            relation.to,
        `No self relation: ${relation.from}`
    );
}


/* ============================================================
   TEST 9 — Knowledge Base Manifest
   ============================================================ */

console.log("");
console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 9 — Knowledge Base Manifest"
);
console.log(
    "--------------------------------------------"
);


const manifest =
    readJson(
        path.join(
            root,
            "knowledge-base.json"
        )
    );


assert(
    manifest.sourceOfTruth !==
        undefined,
    "Knowledge source-of-truth manifest exists"
);


assert(
    manifest.generated !==
        undefined,
    "Generated index configuration exists"
);


assert(
    manifest.sourceOfTruth.topics !==
        undefined,
    "Topic source directory declared"
);


/* ============================================================
   FINAL
   ============================================================ */

console.log("");
console.log(
    "============================================"
);

console.log(
    " STEP 25 KNOWLEDGE BASE SUMMARY"
);

console.log(
    "============================================"
);

console.log("");

console.log(
    `Domains:   ${domains.length}`
);

console.log(
    `Topics:    ${topics.length}`
);

console.log(
    `Concepts:  ${concepts.length}`
);

console.log(
    `Skills:    ${skills.length}`
);

console.log(
    `Exams:     ${exams.length}`
);

console.log(
    `Relations: ${relationData.relations.length}`
);

console.log("");

console.log(
    "✓ KNOWLEDGE BASE VALIDATION PASSED"
);

console.log(
    "✓ STEP 25 FOUNDATION COMPLETE"
);

console.log("");

console.log(
    "IMPORTANT:"
);

console.log(
    "These 6 topics are prototype seed data only."
);

console.log(
    "Future 100+ topics will be added as DATA,"
);

console.log(
    "not hardcoded into engine JavaScript."
);

console.log("");

console.log(
    "============================================"
);
