/**
 * ============================================================
 * SJMaths — Readiness Question → Knowledge Index Adapter
 * STEP 32.50B
 * ============================================================
 *
 * Converts readiness question-bank files into the same question
 * entity shape already consumed by question-index.json.
 *
 * This adapter does NOT modify the question-selection engine.
 */

import fs from "fs";
import path from "path";


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


function clone(
    value
) {

    return JSON.parse(
        JSON.stringify(
            value
        )
    );
}


function normalizeQuestion(
    question,
    sourceFile
) {

    if (
        !question ||
        typeof question !==
        "object"
    ) {

        return null;
    }


    if (
        typeof question.id !==
        "string"
    ) {

        return null;
    }


    if (
        typeof question.topicId !==
        "string"
    ) {

        return null;
    }


    if (
        typeof question.conceptId !==
        "string"
    ) {

        return null;
    }


    if (
        !Array.isArray(
            question.skillIds
        )
    ) {

        return null;
    }


    /*
     * The existing index stores the real question in
     * entity.data. We preserve the question structure as-is.
     */

    return {

        id:
            question.id,

        source:
            "readiness",

        data: {

            ...clone(
                question
            ),

            /*
             * Readiness questions currently do not need an
             * exam restriction. This leaves them available to
             * foundational diagnostics regardless of exam.
             */

            exams:
                Array.isArray(
                    question.exams
                )
                    ? question.exams
                    : [],

            /*
             * Keep explicit readiness identity available to
             * readiness-aware consumers.
             */

            readinessSkillId:
                question.readinessSkillId,

            _readinessSourceFile:
                sourceFile
        }
    };
}


export function loadReadinessQuestionEntities(
    readinessRoot
) {

    if (
        !fs.existsSync(
            readinessRoot
        )
    ) {

        return [];
    }


    const entities =
        [];


    const directories =
        fs.readdirSync(
            readinessRoot,
            {
                withFileTypes:
                    true
            }
        )
        .filter(
            item =>
                item.isDirectory()
        );


    for (
        const directory
        of directories
    ) {

        const file =
            path.join(
                readinessRoot,
                directory.name,
                "questions.json"
            );


        if (
            !fs.existsSync(
                file
            )
        ) {

            continue;
        }


        const payload =
            readJson(
                file
            );


        const questions =
            Array.isArray(
                payload.questions
            )
                ? payload.questions
                : [];


        for (
            const question
            of questions
        ) {

            const entity =
                normalizeQuestion(
                    question,
                    file
                );


            if (
                entity
            ) {

                entities.push(
                    entity
                );
            }
        }
    }


    return entities;
}


export function mergeReadinessEntities(
    index,
    readinessEntities
) {

    const next =
        clone(
            index
        );


    if (
        !next.entities ||
        typeof next.entities !==
            "object"
    ) {

        next.entities =
            {};
    }


    for (
        const entity
        of readinessEntities
    ) {

        /*
         * Existing IDs always win.
         * We never overwrite an existing production question.
         */

        if (
            next.entities[
                entity.id
            ]
        ) {

            continue;
        }


        next.entities[
            entity.id
        ] =
            entity;
    }


    /*
     * Rebuild all lookup maps so the existing selector sees
     * readiness questions exactly like normal question data.
     */

    next.byTopic =
        {};

    next.byConcept =
        {};

    next.bySkill =
        {};

    next.byExam =
        {};


    for (
        const entity
        of Object.values(
            next.entities
        )
    ) {

        const question =
            entity?.data;


        if (
            !question
        ) {

            continue;
        }


        const add =
            (
                container,
                key,
                id
            ) => {

                if (
                    !key
                ) {

                    return;
                }


                if (
                    !container[key]
                ) {

                    container[key] =
                        [];
                }


                if (
                    !container[key]
                        .includes(
                            id
                        )
                ) {

                    container[key].push(
                        id
                    );
                }
            };


        add(
            next.byTopic,
            question.topicId,
            entity.id
        );


        add(
            next.byConcept,
            question.conceptId,
            entity.id
        );


        for (
            const skillId
            of Array.isArray(
                question.skillIds
            )
                ? question.skillIds
                : []
        ) {

            add(
                next.bySkill,
                skillId,
                entity.id
            );
        }


        for (
            const examId
            of Array.isArray(
                question.exams
            )
                ? question.exams
                : []
        ) {

            add(
                next.byExam,
                examId,
                entity.id
            );
        }
    }


    return next;
}
