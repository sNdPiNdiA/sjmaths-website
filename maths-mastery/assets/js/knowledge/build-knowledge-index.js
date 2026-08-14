import fs from "fs";
import path from "path";


const KNOWLEDGE_ROOT =
    path.resolve(
        process.cwd(),
        "maths-mastery",
        "data",
        "knowledge"
    );


const GENERATED_ROOT =
    path.join(
        KNOWLEDGE_ROOT,
        "generated"
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


function readEntities(
    directoryName
) {

    const directory =
        path.join(
            KNOWLEDGE_ROOT,
            directoryName
        );


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
            file => {

                const filePath =
                    path.join(
                        directory,
                        file
                    );


                return {

                    file,

                    path:
                        filePath,

                    data:
                        readJson(
                            filePath
                        )

                };

            }
        );
}


function writeIndex(
    fileName,
    value
) {

    const output =
        path.join(
            GENERATED_ROOT,
            fileName
        );


    fs.writeFileSync(
        output,
        JSON.stringify(
            value,
            null,
            2
        ),
        "utf8"
    );


    return output;
}


function createEntityIndex(
    entities
) {

    const index = {};


    for (
        const entity of
        entities
    ) {

        index[
            entity.data.id
        ] = {

            id:
                entity.data.id,

            source:
                entity.file,

            data:
                entity.data

        };
    }


    return index;
}


console.log("");
console.log(
    "============================================"
);
console.log(
    " STEP 26 — BUILDING KNOWLEDGE INDEXES"
);
console.log(
    "============================================"
);
console.log("");


/* ============================================================
   Load all source data
   ============================================================ */

const domains =
    readEntities(
        "domains"
    );


const topics =
    readEntities(
        "topics"
    );


const concepts =
    readEntities(
        "concepts"
    );


const skills =
    readEntities(
        "skills"
    );


const patterns =
    readEntities(
        "patterns"
    );


const exams =
    readEntities(
        "exams"
    );


function readNestedEntities(
    directoryName
) {

    const directory =
        path.join(
            KNOWLEDGE_ROOT,
            directoryName
        );


    if (
        !fs.existsSync(
            directory
        )
    ) {

        return [];
    }


    const results = [];


    function scan(
        currentDirectory
    ) {

        for (
            const entry of
            fs.readdirSync(
                currentDirectory,
                {
                    withFileTypes: true
                }
            )
        ) {

            const fullPath =
                path.join(
                    currentDirectory,
                    entry.name
                );


            if (
                entry.isDirectory()
            ) {

                scan(
                    fullPath
                );

                continue;
            }


            if (
                entry.isFile() &&
                entry.name.endsWith(
                    ".json"
                ) &&
                entry.name !==
                    "manifest.json"
            ) {

                results.push({

                    file:
                        path.relative(
                            directory,
                            fullPath
                        ),

                    path:
                        fullPath,

                    data:
                        readJson(
                            fullPath
                        )

                });
            }
        }
    }


    scan(
        directory
    );


    return results;
}


const questions =
    readNestedEntities(
        "questions"
    );


/* ============================================================
   Build simple entity indexes
   ============================================================ */

const domainIndex =
    createEntityIndex(
        domains
    );


const topicIndex =
    createEntityIndex(
        topics
    );


const conceptIndex =
    createEntityIndex(
        concepts
    );


const skillIndex =
    createEntityIndex(
        skills
    );


const patternIndex =
    createEntityIndex(
        patterns
    );


const examIndex =
    createEntityIndex(
        exams
    );


const questionIndex =
    createEntityIndex(
        questions
    );


/* ============================================================
   Build topic → concepts index
   ============================================================ */

const conceptsByTopic = {};


for (
    const concept of
    concepts
) {

    const topicId =
        concept.data.topicId;


    if (
        !conceptsByTopic[
            topicId
        ]
    ) {

        conceptsByTopic[
            topicId
        ] = [];
    }


    conceptsByTopic[
        topicId
    ].push(
        concept.data.id
    );
}


/* ============================================================
   Build topic → skills index
   ============================================================ */

const skillsByTopic = {};


for (
    const skill of
    skills
) {

    const topicId =
        skill.data.topicId;


    if (
        !skillsByTopic[
            topicId
        ]
    ) {

        skillsByTopic[
            topicId
        ] = [];
    }


    skillsByTopic[
        topicId
    ].push(
        skill.data.id
    );
}


/* ============================================================
   Build concept → skills index
   ============================================================ */

const skillsByConcept = {};


for (
    const skill of
    skills
) {

    const conceptId =
        skill.data.conceptId;


    if (
        !skillsByConcept[
            conceptId
        ]
    ) {

        skillsByConcept[
            conceptId
        ] = [];
    }


    skillsByConcept[
        conceptId
    ].push(
        skill.data.id
    );
}


/* ============================================================
   Build domain → topics index
   ============================================================ */

const topicsByDomain = {};


for (
    const topic of
    topics
) {

    const domainId =
        topic.data.domainId;


    if (
        !topicsByDomain[
            domainId
        ]
    ) {

        topicsByDomain[
            domainId
        ] = [];
    }


    topicsByDomain[
        domainId
    ].push(
        topic.data.id
    );
}


/* ============================================================
   Build question indexes
   ============================================================ */

const questionsByTopic = {};
const questionsByConcept = {};
const questionsBySkill = {};
const questionsByExam = {};


for (
    const question of
    questions
) {

    const data =
        question.data;


    if (
        data.topicId
    ) {

        if (
            !questionsByTopic[
                data.topicId
            ]
        ) {

            questionsByTopic[
                data.topicId
            ] = [];
        }


        questionsByTopic[
            data.topicId
        ].push(
            data.id
        );
    }


    if (
        data.conceptId
    ) {

        if (
            !questionsByConcept[
                data.conceptId
            ]
        ) {

            questionsByConcept[
                data.conceptId
            ] = [];
        }


        questionsByConcept[
            data.conceptId
        ].push(
            data.id
        );
    }


    if (
        Array.isArray(
            data.skillIds
        )
    ) {

        for (
            const skillId of
            data.skillIds
        ) {

            if (
                !questionsBySkill[
                    skillId
                ]
            ) {

                questionsBySkill[
                    skillId
                ] = [];
            }


            questionsBySkill[
                skillId
            ].push(
                data.id
            );
        }
    }


    if (
        Array.isArray(
            data.exams
        )
    ) {

        for (
            const examId of
            data.exams
        ) {

            if (
                !questionsByExam[
                    examId
                ]
            ) {

                questionsByExam[
                    examId
                ] = [];
            }


            questionsByExam[
                examId
            ].push(
                data.id
            );
        }
    }
}


/* ============================================================
   Graph index
   ============================================================ */

const relationFile =
    path.join(
        KNOWLEDGE_ROOT,
        "relations",
        "topic-relations.json"
    );


let relations = [];


if (
    fs.existsSync(
        relationFile
    )
) {

    const relationData =
        readJson(
            relationFile
        );


    relations =
        Array.isArray(
            relationData.relations
        )
            ? relationData.relations
            : [];
}


const prerequisites = {};
const related = {};
const progression = {};


for (
    const relation of
    relations
) {

    if (
        relation.relation ===
            "prerequisite"
    ) {

        if (
            !prerequisites[
                relation.to
            ]
        ) {

            prerequisites[
                relation.to
            ] = [];
        }


        prerequisites[
            relation.to
        ].push(
            relation.from
        );
    }


    if (
        relation.relation ===
            "related"
    ) {

        if (
            !related[
                relation.to
            ]
        ) {

            related[
                relation.to
            ] = [];
        }


        related[
            relation.to
        ].push(
            relation.from
        );
    }


    if (
        relation.relation ===
            "progression"
    ) {

        if (
            !progression[
                relation.from
            ]
        ) {

            progression[
                relation.from
            ] = [];
        }


        progression[
            relation.from
        ].push(
            relation.to
        );
    }
}


/* ============================================================
   Write indexes
   ============================================================ */

writeIndex(
    "domain-index.json",
    domainIndex
);


writeIndex(
    "topic-index.json",
    {

        entities:
            topicIndex,

        byDomain:
            topicsByDomain

    }
);


writeIndex(
    "concept-index.json",
    {

        entities:
            conceptIndex,

        byTopic:
            conceptsByTopic

    }
);


writeIndex(
    "skill-index.json",
    {

        entities:
            skillIndex,

        byTopic:
            skillsByTopic,

        byConcept:
            skillsByConcept

    }
);


writeIndex(
    "pattern-index.json",
    patternIndex
);


writeIndex(
    "exam-index.json",
    examIndex
);


writeIndex(
    "question-index.json",
    {

        entities:
            questionIndex,

        byTopic:
            questionsByTopic,

        byConcept:
            questionsByConcept,

        bySkill:
            questionsBySkill,

        byExam:
            questionsByExam

    }
);


writeIndex(
    "graph-index.json",
    {

        version:
            "1.0.0",

        relations,

        prerequisites,

        related,

        progression

    }
);


/* ============================================================
   Build manifest
   ============================================================ */

const manifest = {

    version:
        "1.0.0",

    generatedAt:
        new Date().toISOString(),

    counts: {

        domains:
            domains.length,

        topics:
            topics.length,

        concepts:
            concepts.length,

        skills:
            skills.length,

        patterns:
            patterns.length,

        exams:
            exams.length,

        questions:
            questions.length,

        relations:
            relations.length
    },

    indexes: [

        "domain-index.json",
        "topic-index.json",
        "concept-index.json",
        "skill-index.json",
        "pattern-index.json",
        "exam-index.json",
        "question-index.json",
        "graph-index.json"

    ]
};


writeIndex(
    "build-manifest.json",
    manifest
);


/* ============================================================
   Output
   ============================================================ */

console.log(
    "✓ domain-index.json generated"
);

console.log(
    "✓ topic-index.json generated"
);

console.log(
    "✓ concept-index.json generated"
);

console.log(
    "✓ skill-index.json generated"
);

console.log(
    "✓ pattern-index.json generated"
);

console.log(
    "✓ exam-index.json generated"
);

console.log(
    "✓ question-index.json generated"
);

console.log(
    "✓ graph-index.json generated"
);

console.log(
    "✓ build-manifest.json generated"
);

console.log("");

console.log(
    "============================================"
);

console.log(
    " KNOWLEDGE INDEX SUMMARY"
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
    `Patterns:  ${patterns.length}`
);

console.log(
    `Exams:     ${exams.length}`
);

console.log(
    `Questions: ${questions.length}`
);

console.log(
    `Relations: ${relations.length}`
);

console.log("");

console.log(
    "✓ KNOWLEDGE INDEX BUILD COMPLETE"
);

console.log("");

