/**
 * SJMaths Maths Mastery
 * Progress Engine
 *
 * Responsibility:
 * ----------------
 * Record learning evidence.
 *
 * Does NOT:
 * ----------------
 * - calculate mastery
 * - make recommendations
 * - access DOM
 * - access localStorage
 * - access network
 *
 * Evidence is the source of truth.
 */


/* ============================================================
   Utilities
   ============================================================ */

function clone(value) {

    return JSON.parse(
        JSON.stringify(value)
    );
}


function now() {

    return new Date().toISOString();
}


function ensureObject(
    object,
    key
) {

    if (
        !object[key] ||
        typeof object[key] !== "object"
    ) {

        object[key] = {};
    }

    return object[key];
}


function ensureEvidence(object) {

    if (!object.evidence) {

        object.evidence = {

            attempts: 0,

            correct: 0,

            incorrect: 0,

            skipped: 0,

            timeSpentSeconds: 0,

            lastAttemptAt: null,

            firstAttemptAt: null
        };
    }

    return object.evidence;
}


/* ============================================================
   Create Empty Progress
   ============================================================ */

export function createEmptyProgress(
    studentId = "local"
) {

    return {

        version: "1.0.0",

        studentId,

        updatedAt: now(),

        topics: {}
    };
}


/* ============================================================
   Ensure Topic
   ============================================================ */

export function ensureTopicProgress(
    progress,
    topicId
) {

    if (
        !progress.topics
    ) {

        progress.topics = {};
    }


    if (
        !progress.topics[topicId]
    ) {

        progress.topics[topicId] = {

            topicId,

            status: "not-started",

            evidence: {

                attempts: 0,

                correct: 0,

                incorrect: 0,

                skipped: 0,

                timeSpentSeconds: 0,

                lastAttemptAt: null,

                firstAttemptAt: null
            },

            concepts: {},

            skills: {},

            miniTests: {}
        };
    }


    return progress.topics[topicId];
}


/* ============================================================
   Ensure Concept
   ============================================================ */

export function ensureConceptProgress(
    progress,
    topicId,
    conceptId
) {

    const topic =
        ensureTopicProgress(
            progress,
            topicId
        );


    if (
        !topic.concepts[conceptId]
    ) {

        topic.concepts[conceptId] = {

            conceptId,

            status: "not-started",

            evidence: {

                attempts: 0,

                correct: 0,

                incorrect: 0,

                skipped: 0,

                timeSpentSeconds: 0,

                lastAttemptAt: null,

                firstAttemptAt: null
            }
        };
    }


    return topic.concepts[conceptId];
}


/* ============================================================
   Ensure Skill
   ============================================================ */

export function ensureSkillProgress(
    progress,
    topicId,
    skillId
) {

    const topic =
        ensureTopicProgress(
            progress,
            topicId
        );


    if (
        !topic.skills[skillId]
    ) {

        topic.skills[skillId] = {

            skillId,

            score: 0,

            evidence: {

                attempts: 0,

                correct: 0,

                incorrect: 0,

                skipped: 0,

                timeSpentSeconds: 0,

                lastAttemptAt: null,

                firstAttemptAt: null
            },

            lastUpdatedAt: null
        };
    }


    return topic.skills[skillId];
}


/* ============================================================
   Record Evidence
   ============================================================ */

export function recordEvidence(
    progress,
    {
        topicId,
        conceptId = null,
        skillIds = [],
        result,
        timeSpentSeconds = 0,
        attemptedAt = null
    }
) {

    if (!topicId) {

        throw new Error(
            "Progress Engine: topicId is required."
        );
    }


    const validResults = [
        "correct",
        "incorrect",
        "skipped"
    ];


    if (
        !validResults.includes(result)
    ) {

        throw new Error(
            `Progress Engine: invalid result "${result}".`
        );
    }


    const updated =
        clone(progress);


    const timestamp =
        attemptedAt || now();


    const topic =
        ensureTopicProgress(
            updated,
            topicId
        );


    const entities = [];


    /*
     * Topic evidence
     */

    entities.push(
        topic
    );


    /*
     * Concept evidence
     */

    if (conceptId) {

        entities.push(
            ensureConceptProgress(
                updated,
                topicId,
                conceptId
            )
        );
    }


    /*
     * Skill evidence
     */

    for (
        const skillId
        of skillIds
    ) {

        if (!skillId) {
            continue;
        }

        entities.push(
            ensureSkillProgress(
                updated,
                topicId,
                skillId
            )
        );
    }


    /*
     * Update every evidence-bearing entity.
     */

    for (
        const entity
        of entities
    ) {

        const evidence =
            ensureEvidence(
                entity
            );


        evidence.attempts += 1;


        if (
            result === "correct"
        ) {

            evidence.correct += 1;
        }


        if (
            result === "incorrect"
        ) {

            evidence.incorrect += 1;
        }


        if (
            result === "skipped"
        ) {

            evidence.skipped += 1;
        }


        evidence.timeSpentSeconds +=
            Math.max(
                0,
                Number(
                    timeSpentSeconds
                ) || 0
            );


        if (
            !evidence.firstAttemptAt
        ) {

            evidence.firstAttemptAt =
                timestamp;
        }


        evidence.lastAttemptAt =
            timestamp;


        /*
         * Skill timestamps.
         */

        if (
            entity.skillId
        ) {

            entity.lastUpdatedAt =
                timestamp;
        }
    }


    /*
     * Update topic timestamp.
     */

    updated.updatedAt =
        timestamp;


    return updated;
}


/* ============================================================
   Record Practice Question
   ============================================================ */

export function recordQuestionAttempt(
    progress,
    {
        topicId,
        questionId,
        conceptId = null,
        skillIds = [],
        correct,
        timeSpentSeconds = 0,
        attemptedAt = null
    }
) {

    if (!questionId) {

        throw new Error(
            "Progress Engine: questionId is required."
        );
    }


    /*
     * Question result contract:
     *
     * true  = correct
     * false = incorrect
     * null  = skipped
     *
     * Anything else is invalid and MUST be rejected.
     */

    if (
        correct !== true &&
        correct !== false &&
        correct !== null
    ) {

        throw new Error(
            'Progress Engine: "correct" must be true, false, or null.'
        );
    }


    const result =
        correct === true
            ? "correct"
            : correct === false
                ? "incorrect"
                : "skipped";


    return recordEvidence(
        progress,
        {

            topicId,

            conceptId,

            skillIds,

            result,

            timeSpentSeconds,

            attemptedAt
        }
    );
}


/* ============================================================
   Record Mini Test
   ============================================================ */

export function recordMiniTestAttempt(
    progress,
    {
        topicId,
        testId,
        score,
        accuracy,
        attemptedAt = null
    }
) {

    if (!topicId) {

        throw new Error(
            "Progress Engine: topicId is required."
        );
    }


    if (!testId) {

        throw new Error(
            "Progress Engine: testId is required."
        );
    }


    const updated =
        clone(progress);


    const topic =
        ensureTopicProgress(
            updated,
            topicId
        );


    if (
        !topic.miniTests[testId]
    ) {

        topic.miniTests[testId] = {

            testId,

            attempts: 0,

            bestScore: 0,

            bestAccuracy: 0,

            lastScore: 0,

            lastAccuracy: 0,

            lastAttemptAt: null
        };
    }


    const test =
        topic.miniTests[testId];


    const safeScore =
        Math.max(
            0,
            Math.min(
                100,
                Number(score) || 0
            )
        );


    const safeAccuracy =
        Math.max(
            0,
            Math.min(
                100,
                Number(accuracy) || 0
            )
        );


    const timestamp =
        attemptedAt || now();


    test.attempts += 1;

    test.lastScore =
        safeScore;

    test.lastAccuracy =
        safeAccuracy;

    test.bestScore =
        Math.max(
            test.bestScore,
            safeScore
        );

    test.bestAccuracy =
        Math.max(
            test.bestAccuracy,
            safeAccuracy
        );

    test.lastAttemptAt =
        timestamp;


    updated.updatedAt =
        timestamp;


    return updated;
}


/* ============================================================
   Evidence Summary
   ============================================================ */

export function getEvidenceSummary(
    progress,
    topicId
) {

    const topic =
        progress.topics?.[topicId];


    if (!topic) {

        return null;
    }


    const evidence =
        topic.evidence;


    const accuracy =
        evidence.attempts > 0

            ? (
                evidence.correct /
                evidence.attempts
            ) * 100

            : 0;


    return {

        topicId,

        attempts:
            evidence.attempts,

        correct:
            evidence.correct,

        incorrect:
            evidence.incorrect,

        skipped:
            evidence.skipped,

        timeSpentSeconds:
            evidence.timeSpentSeconds,

        accuracy:
            Math.round(
                accuracy * 100
            ) / 100,

        firstAttemptAt:
            evidence.firstAttemptAt,

        lastAttemptAt:
            evidence.lastAttemptAt
    };
}


/* ============================================================
   Skill Evidence Summary
   ============================================================ */

export function getSkillEvidence(
    progress,
    topicId,
    skillId
) {

    const skill =
        progress
            .topics?.[topicId]
            ?.skills?.[skillId];


    if (!skill) {

        return null;
    }


    const evidence =
        skill.evidence;


    const accuracy =
        evidence.attempts > 0

            ? (
                evidence.correct /
                evidence.attempts
            ) * 100

            : 0;


    return {

        skillId,

        score:
            skill.score,

        attempts:
            evidence.attempts,

        correct:
            evidence.correct,

        incorrect:
            evidence.incorrect,

        skipped:
            evidence.skipped,

        accuracy:
            Math.round(
                accuracy * 100
            ) / 100,

        timeSpentSeconds:
            evidence.timeSpentSeconds,

        lastUpdatedAt:
            skill.lastUpdatedAt
    };
}


/* ============================================================
   Validate Evidence Integrity
   ============================================================ */

export function validateProgressEvidence(
    progress
) {

    const errors = [];


    if (!progress) {

        errors.push(
            "Progress object is required."
        );

        return errors;
    }


    if (!progress.topics) {

        errors.push(
            "topics object is missing."
        );

        return errors;
    }


    for (
        const [topicId, topic]
        of Object.entries(
            progress.topics
        )
    ) {

        if (
            topic.topicId !== topicId
        ) {

            errors.push(
                `Topic ID mismatch: ${topicId}`
            );
        }


        const evidence =
            topic.evidence;


        if (evidence) {

            const total =
                evidence.correct +
                evidence.incorrect +
                evidence.skipped;


            if (
                evidence.attempts !==
                total
            ) {

                errors.push(
                    `Evidence count mismatch for topic ${topicId}`
                );
            }
        }


        for (
            const [conceptId, concept]
            of Object.entries(
                topic.concepts || {}
            )
        ) {

            if (
                concept.conceptId !==
                conceptId
            ) {

                errors.push(
                    `Concept ID mismatch: ${topicId}/${conceptId}`
                );
            }
        }


        for (
            const [skillId, skill]
            of Object.entries(
                topic.skills || {}
            )
        ) {

            if (
                skill.skillId !==
                skillId
            ) {

                errors.push(
                    `Skill ID mismatch: ${topicId}/${skillId}`
                );
            }


            if (
                skill.score < 0 ||
                skill.score > 100
            ) {

                errors.push(
                    `Invalid skill score: ${topicId}/${skillId}`
                );
            }
        }
    }


    return errors;
}


/* ============================================================
   Default Export
   ============================================================ */

export default {

    createEmptyProgress,

    ensureTopicProgress,

    ensureConceptProgress,

    ensureSkillProgress,

    recordEvidence,

    recordQuestionAttempt,

    recordMiniTestAttempt,

    getEvidenceSummary,

    getSkillEvidence,

    validateProgressEvidence
};

