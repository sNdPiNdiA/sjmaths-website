/**
 * SJMaths Maths Mastery
 * Diagnostic Engine
 *
 * PURPOSE:
 * Determine the student's most appropriate starting topic.
 *
 * This is a PLACEMENT engine.
 * It is NOT the Mastery Engine.
 *
 * It does not permanently modify student progress.
 */


/* ============================================================
   Constants
   ============================================================ */

const DEFAULT_MINIMUM_QUESTIONS = 10;

const DEFAULT_START_TOPIC =
    "number-system";


/* ============================================================
   Validate Diagnostic Definition
   ============================================================ */

export function validateDiagnostic(
    diagnostic
) {

    if (!diagnostic) {
        return false;
    }

    if (
        typeof diagnostic.id !==
            "string"
    ) {
        return false;
    }

    if (
        !Array.isArray(
            diagnostic.questions
        )
    ) {
        return false;
    }

    if (
        diagnostic.questions.length ===
            0
    ) {
        return false;
    }

    const ids = new Set();

    for (
        const question
        of diagnostic.questions
    ) {

        if (
            !question.id ||
            !question.topicId ||
            !question.skillId
        ) {
            return false;
        }

        if (
            ids.has(
                question.id
            )
        ) {
            return false;
        }

        ids.add(
            question.id
        );
    }

    return true;
}


/* ============================================================
   Validate Diagnostic Answer
   ============================================================ */

export function validateAnswer(
    answer
) {

    if (!answer) {
        return false;
    }

    if (
        typeof answer.questionId !==
            "string"
    ) {
        return false;
    }

    if (
        ![
            "correct",
            "incorrect",
            "skipped"
        ].includes(
            answer.result
        )
    ) {
        return false;
    }

    return true;
}


/* ============================================================
   Calculate Topic Statistics
   ============================================================ */

export function calculateTopicStatistics(
    diagnostic,
    answers
) {

    if (
        !validateDiagnostic(
            diagnostic
        )
    ) {
        throw new Error(
            "Invalid diagnostic"
        );
    }

    if (
        !Array.isArray(
            answers
        )
    ) {
        throw new Error(
            "Answers must be an array"
        );
    }


    const questionMap =
        new Map(
            diagnostic.questions.map(
                question => [
                    question.id,
                    question
                ]
            )
        );


    const topics = {};


    for (
        const answer
        of answers
    ) {

        if (
            !validateAnswer(
                answer
            )
        ) {
            throw new Error(
                "Invalid diagnostic answer"
            );
        }


        const question =
            questionMap.get(
                answer.questionId
            );


        if (!question) {

            throw new Error(
                `Unknown diagnostic question: ${answer.questionId}`
            );
        }


        const topicId =
            question.topicId;


        if (!topics[topicId]) {

            topics[topicId] = {

                topicId,

                attempts: 0,

                correct: 0,

                incorrect: 0,

                skipped: 0,

                accuracy: 0,

                answered: 0
            };
        }


        const topic =
            topics[topicId];


        topic.attempts++;


        if (
            answer.result ===
                "correct"
        ) {

            topic.correct++;
            topic.answered++;

        }
        else if (
            answer.result ===
                "incorrect"
        ) {

            topic.incorrect++;
            topic.answered++;

        }
        else {

            topic.skipped++;
        }


        if (
            topic.answered > 0
        ) {

            topic.accuracy =
                Math.round(
                    (
                        topic.correct /
                        topic.answered
                    ) * 100
                );
        }
    }


    return topics;
}


/* ============================================================
   Calculate Skill Statistics
   ============================================================ */

export function calculateSkillStatistics(
    diagnostic,
    answers
) {

    const questionMap =
        new Map(
            diagnostic.questions.map(
                question => [
                    question.id,
                    question
                ]
            )
        );


    const skills = {};


    for (
        const answer
        of answers
    ) {

        if (
            !validateAnswer(
                answer
            )
        ) {
            throw new Error(
                "Invalid diagnostic answer"
            );
        }


        const question =
            questionMap.get(
                answer.questionId
            );


        if (!question) {

            throw new Error(
                `Unknown diagnostic question: ${answer.questionId}`
            );
        }


        const skillId =
            question.skillId;


        if (!skills[skillId]) {

            skills[skillId] = {

                skillId,

                topicId:
                    question.topicId,

                attempts: 0,

                correct: 0,

                incorrect: 0,

                skipped: 0,

                accuracy: 0
            };
        }


        const skill =
            skills[skillId];


        skill.attempts++;


        if (
            answer.result ===
                "correct"
        ) {

            skill.correct++;

        }
        else if (
            answer.result ===
                "incorrect"
        ) {

            skill.incorrect++;

        }
        else {

            skill.skipped++;
        }


        const answered =
            skill.correct +
            skill.incorrect;


        if (
            answered > 0
        ) {

            skill.accuracy =
                Math.round(
                    (
                        skill.correct /
                        answered
                    ) * 100
                );
        }
    }


    return skills;
}


/* ============================================================
   Find Weakest Topic
   ============================================================ */

export function findWeakestTopic(
    topicStatistics
) {

    const topics =
        Object.values(
            topicStatistics || {}
        );


    const withEvidence =
        topics.filter(
            topic =>
                topic.answered > 0
        );


    if (
        withEvidence.length ===
            0
    ) {

        return null;
    }


    /*
     * Lowest accuracy wins.
     *
     * If tied, the topic with
     * more answered questions wins.
     */

    return (
        [...withEvidence]
            .sort(
                (
                    a,
                    b
                ) => {

                    if (
                        a.accuracy !==
                            b.accuracy
                    ) {

                        return (
                            a.accuracy -
                            b.accuracy
                        );
                    }


                    return (
                        b.answered -
                        a.answered
                    );
                }
            )[0]
    );
}


/* ============================================================
   Find Strongest Topic
   ============================================================ */

export function findStrongestTopic(
    topicStatistics
) {

    const topics =
        Object.values(
            topicStatistics || {}
        );


    const withEvidence =
        topics.filter(
            topic =>
                topic.answered > 0
        );


    if (
        withEvidence.length ===
            0
    ) {

        return null;
    }


    return (
        [...withEvidence]
            .sort(
                (
                    a,
                    b
                ) => {

                    if (
                        a.accuracy !==
                            b.accuracy
                    ) {

                        return (
                            b.accuracy -
                            a.accuracy
                        );
                    }


                    return (
                        b.answered -
                        a.answered
                    );
                }
            )[0]
    );
}


/* ============================================================
   Build Topic Order From Graph
   ============================================================ */

export function buildTopicOrder(
    graph
) {

    if (
        !graph ||
        !Array.isArray(
            graph.nodes
        )
    ) {

        throw new Error(
            "Invalid topic graph"
        );
    }


    /*
     * Foundation nodes first,
     * followed by basic/intermediate/
     * advanced nodes.
     *
     * Within the same level,
     * graph declaration order is preserved.
     */

    const levelOrder = {

        foundation: 0,

        basic: 1,

        intermediate: 2,

        advanced: 3
    };


    return [...graph.nodes]
        .sort(
            (
                a,
                b
            ) => {

                return (
                    (
                        levelOrder[
                            a.level
                        ] ??
                        99
                    ) -
                    (
                        levelOrder[
                            b.level
                        ] ??
                        99
                    )
                );
            }
        )
        .map(
            node =>
                node.topicId
        );
}


/* ============================================================
   Recommend Starting Topic
   ============================================================ */

export function recommendStartingTopic(
    topicStatistics,
    graph,
    options = {}
) {

    const minimumReadiness =
        options.minimumReadiness ??
        70;


    const topicOrder =
        buildTopicOrder(
            graph
        );


    const topics =
        Object.values(
            topicStatistics || {}
        );


    const answered =
        topics.filter(
            topic =>
                topic.answered > 0
        );


    /*
     * No diagnostic evidence.
     *
     * Always begin from the
     * foundation.
     */

    if (
        answered.length === 0
    ) {

        return {

            topicId:
                topicOrder[0] ||
                DEFAULT_START_TOPIC,

            reason:
                "No diagnostic evidence available; start from the foundation."
        };
    }


    /*
     * First find the earliest topic
     * in the learning graph that has
     * insufficient readiness.
     *
     * This is deliberately different
     * from simply selecting the
     * lowest score.
     */

    for (
        const topicId
        of topicOrder
    ) {

        const statistics =
            topicStatistics[
                topicId
            ];


        /*
         * No evidence means the learner
         * has not yet demonstrated
         * readiness for this topic.
         */

        if (
            !statistics ||
            statistics.answered === 0
        ) {

            return {

                topicId,

                reason:
                    "This is the next topic without sufficient diagnostic evidence."
            };
        }


        /*
         * Topic has evidence but is below
         * the readiness threshold.
         */

        if (
            statistics.accuracy <
                minimumReadiness
        ) {

            return {

                topicId,

                reason:
                    `Diagnostic readiness is ${statistics.accuracy}%, below the ${minimumReadiness}% threshold.`
            };
        }
    }


    /*
     * Everything assessed so far is
     * sufficiently ready.
     *
     * Continue to the next topic.
     */

    for (
        const topicId
        of topicOrder
    ) {

        if (
            !topicStatistics[
                topicId
            ]
        ) {

            return {

                topicId,

                reason:
                    "All assessed prerequisites meet the readiness threshold; continue to the next topic."
            };
        }
    }


    /*
     * All topics have evidence and
     * all are ready.
     */

    const strongest =
        findStrongestTopic(
            topicStatistics
        );


    if (strongest) {

        return {

            topicId:
                strongest.topicId,

            reason:
                "All assessed topics meet the diagnostic readiness threshold."
        };
    }


    return {

        topicId:
            topicOrder[0] ||
            DEFAULT_START_TOPIC,

        reason:
            "Foundation topic selected."
    };
}

/* ============================================================
   Complete Diagnostic
   ============================================================ */

export function completeDiagnostic(
    diagnostic,
    answers,
    graph,
    options = {}
) {

    const minimumQuestions =
        options.minimumQuestions ??
        diagnostic.minimumQuestions ??
        DEFAULT_MINIMUM_QUESTIONS;


    if (
        answers.length <
            minimumQuestions
    ) {

        throw new Error(
            `Diagnostic requires at least ${minimumQuestions} answers`
        );
    }


    const topicStatistics =
        calculateTopicStatistics(
            diagnostic,
            answers
        );


    const skillStatistics =
        calculateSkillStatistics(
            diagnostic,
            answers
        );


    const recommendation =
        recommendStartingTopic(
            topicStatistics,
            graph
        );


    return {

        version:
            "1.0.0",

        diagnosticId:
            diagnostic.id,

        completed:
            true,

        questionCount:
            answers.length,

        topicStatistics,

        skillStatistics,

        startingPoint:
            recommendation.topicId,

        recommendationReason:
            recommendation.reason,

        selectedExam:
            options.selectedExam ??
            null,

        completedAt:
            new Date().toISOString()
    };
}


/* ============================================================
   Export
   ============================================================ */

export default {

    validateDiagnostic,

    validateAnswer,

    calculateTopicStatistics,

    calculateSkillStatistics,

    findWeakestTopic,

    findStrongestTopic,

    buildTopicOrder,

    recommendStartingTopic,

    completeDiagnostic
};

