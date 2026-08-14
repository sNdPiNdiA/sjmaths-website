/**
 * ============================================================
 * SJMaths — Question → Progress Integrator
 * ============================================================
 *
 * Purpose:
 *
 * Convert validated question exposure events into Progress
 * Engine evidence.
 *
 * Architecture:
 *
 * Question
 *    ↓
 * Exposure
 *    ↓
 * Question metadata
 *    ↓
 * Progress evidence
 *    ↓
 * Topic / Concept / Skill
 *    ↓
 * Mastery Engine
 *
 * IMPORTANT:
 *
 * - Questions remain DATA.
 * - Topics remain DATA.
 * - Concepts remain DATA.
 * - Skills remain DATA.
 * - This module contains NO hardcoded question IDs.
 * - This module contains NO hardcoded topic IDs.
 * - This module does NOT calculate mastery.
 * - This module does NOT modify learner state.
 *
 * It only translates question-level results into the existing
 * progress representation.
 * ============================================================
 */


/* ============================================================
   VALID RESULTS
   ============================================================ */

const VALID_RESULTS = new Set([
    "correct",
    "incorrect",
    "skipped"
]);


/* ============================================================
   VALIDATION HELPERS
   ============================================================ */

function assertValidString(
    value,
    fieldName
) {

    if (
        typeof value !== "string" ||
        value.trim() === ""
    ) {

        throw new Error(
            `${fieldName} must be a non-empty string`
        );
    }
}


function validateQuestionData(
    question
) {

    if (
        !question ||
        typeof question !== "object"
    ) {

        throw new Error(
            "Question data is required"
        );
    }


    assertValidString(
        question.id,
        "question.id"
    );


    assertValidString(
        question.topicId,
        "question.topicId"
    );


    assertValidString(
        question.conceptId,
        "question.conceptId"
    );


    if (
        !Array.isArray(
            question.skillIds
        )
    ) {

        throw new Error(
            "question.skillIds must be an array"
        );
    }


    question.skillIds.forEach(
        skillId =>
            assertValidString(
                skillId,
                "question.skillIds[]"
            )
    );


    return true;
}


function validateResult(
    result
) {

    if (
        !VALID_RESULTS.has(
            result
        )
    ) {

        throw new Error(
            `Invalid question result: ${result}`
        );
    }

    return true;
}


/* ============================================================
   RESULT → PROGRESS MAPPING
   ============================================================ */

function resultToProgressOutcome(
    result
) {

    validateResult(
        result
    );


    if (
        result === "correct"
    ) {

        return {
            attempted: true,
            correct: 1,
            incorrect: 0,
            skipped: 0
        };
    }


    if (
        result === "incorrect"
    ) {

        return {
            attempted: true,
            correct: 0,
            incorrect: 1,
            skipped: 0
        };
    }


    return {
        attempted: false,
        correct: 0,
        incorrect: 0,
        skipped: 1
    };
}


/* ============================================================
   CREATE PROGRESS EVIDENCE DELTA
   ============================================================ */

function createProgressEvidenceDelta(
    question,
    result,
    timeSpentSeconds = 0
) {

    validateQuestionData(
        question
    );


    validateResult(
        result
    );


    if (
        typeof timeSpentSeconds !== "number" ||
        !Number.isFinite(
            timeSpentSeconds
        ) ||
        timeSpentSeconds < 0
    ) {

        throw new Error(
            "timeSpentSeconds must be a non-negative number"
        );
    }


    const outcome =
        resultToProgressOutcome(
            result
        );


    return {
        questionId: question.id,

        topicId: question.topicId,

        conceptId: question.conceptId,

        skillIds: [
            ...question.skillIds
        ],

        result,

        attempted:
            outcome.attempted,

        correct:
            outcome.correct,

        incorrect:
            outcome.incorrect,

        skipped:
            outcome.skipped,

        timeSpentSeconds
    };
}


/* ============================================================
   AGGREGATION HELPERS
   ============================================================ */

function createEmptyAccumulator() {

    return {
        attempts: 0,
        correct: 0,
        incorrect: 0,
        skipped: 0,
        timeSpentSeconds: 0
    };
}


function applyEvidenceDelta(
    accumulator,
    delta
) {

    if (
        !accumulator ||
        typeof accumulator !== "object"
    ) {

        throw new Error(
            "Accumulator is required"
        );
    }


    if (
        !delta ||
        typeof delta !== "object"
    ) {

        throw new Error(
            "Evidence delta is required"
        );
    }


    const next = {
        ...accumulator
    };


    if (
        delta.attempted
    ) {

        next.attempts += 1;
    }


    next.correct +=
        delta.correct || 0;


    next.incorrect +=
        delta.incorrect || 0;


    next.skipped +=
        delta.skipped || 0;


    next.timeSpentSeconds +=
        delta.timeSpentSeconds || 0;


    return next;
}


/* ============================================================
   AGGREGATE QUESTION INTO TARGETS
   ============================================================ */

function aggregateQuestionEvidence(
    question,
    result,
    timeSpentSeconds = 0
) {

    const delta =
        createProgressEvidenceDelta(
            question,
            result,
            timeSpentSeconds
        );


    const topic =
        applyEvidenceDelta(
            createEmptyAccumulator(),
            delta
        );


    const concept =
        applyEvidenceDelta(
            createEmptyAccumulator(),
            delta
        );


    const skills = {};


    question.skillIds.forEach(
        skillId => {

            skills[skillId] =
                applyEvidenceDelta(
                    createEmptyAccumulator(),
                    delta
                );
        }
    );


    return {
        questionId:
            question.id,

        topic: {
            id:
                question.topicId,

            evidence:
                topic
        },

        concept: {
            id:
                question.conceptId,

            evidence:
                concept
        },

        skills,

        delta
    };
}


/* ============================================================
   IMMUTABLE BATCH AGGREGATION
   ============================================================ */

function aggregateQuestionResults(
    attempts
) {

    if (
        !Array.isArray(
            attempts
        )
    ) {

        throw new Error(
            "attempts must be an array"
        );
    }


    const result = {
        topics: {},
        concepts: {},
        skills: {},
        questions: {}
    };


    attempts.forEach(
        attempt => {

            if (
                !attempt ||
                typeof attempt !== "object"
            ) {

                throw new Error(
                    "Invalid attempt"
                );
            }


            const question =
                attempt.question;


            const delta =
                createProgressEvidenceDelta(
                    question,
                    attempt.result,
                    attempt.timeSpentSeconds || 0
                );


            /*
             * QUESTION
             */

            if (
                !result.questions[
                    question.id
                ]
            ) {

                result.questions[
                    question.id
                ] =
                    createEmptyAccumulator();
            }


            result.questions[
                question.id
            ] =
                applyEvidenceDelta(
                    result.questions[
                        question.id
                    ],
                    delta
                );


            /*
             * TOPIC
             */

            if (
                !result.topics[
                    question.topicId
                ]
            ) {

                result.topics[
                    question.topicId
                ] =
                    createEmptyAccumulator();
            }


            result.topics[
                question.topicId
            ] =
                applyEvidenceDelta(
                    result.topics[
                        question.topicId
                    ],
                    delta
                );


            /*
             * CONCEPT
             */

            if (
                !result.concepts[
                    question.conceptId
                ]
            ) {

                result.concepts[
                    question.conceptId
                ] =
                    createEmptyAccumulator();
            }


            result.concepts[
                question.conceptId
            ] =
                applyEvidenceDelta(
                    result.concepts[
                        question.conceptId
                    ],
                    delta
                );


            /*
             * SKILLS
             */

            question.skillIds.forEach(
                skillId => {

                    if (
                        !result.skills[
                            skillId
                        ]
                    ) {

                        result.skills[
                            skillId
                        ] =
                            createEmptyAccumulator();
                    }


                    result.skills[
                        skillId
                    ] =
                        applyEvidenceDelta(
                            result.skills[
                                skillId
                            ],
                            delta
                        );
                }
            );
        }
    );


    return result;
}


/* ============================================================
   EXPORTS
   ============================================================ */

export {
    validateQuestionData,

    validateResult,

    resultToProgressOutcome,

    createProgressEvidenceDelta,

    createEmptyAccumulator,

    applyEvidenceDelta,

    aggregateQuestionEvidence,

    aggregateQuestionResults
};
