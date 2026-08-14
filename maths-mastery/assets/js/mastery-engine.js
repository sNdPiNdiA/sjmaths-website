/**
 * SJMaths Maths Mastery
 * Mastery Engine
 *
 * Responsibility:
 * ----------------
 * Convert stored evidence into mastery scores.
 *
 * Does NOT:
 * ----------------
 * - record question attempts
 * - mutate evidence
 * - access DOM
 * - access localStorage
 * - make recommendations
 *
 * Evidence remains the source of truth.
 */


/* ============================================================
   Utilities
   ============================================================ */

function clamp(
    value,
    minimum = 0,
    maximum = 100
) {

    return Math.max(
        minimum,
        Math.min(
            maximum,
            value
        )
    );
}


function round(
    value,
    decimals = 2
) {

    const factor =
        10 ** decimals;

    return (
        Math.round(
            value * factor
        ) / factor
    );
}


function weightedAverage(
    values
) {

    const valid =
        values.filter(
            item =>
                Number.isFinite(
                    item.value
                ) &&
                Number.isFinite(
                    item.weight
                ) &&
                item.weight > 0
        );


    if (
        valid.length === 0
    ) {

        return 0;
    }


    const totalWeight =
        valid.reduce(
            (
                total,
                item
            ) =>
                total +
                item.weight,
            0
        );


    if (
        totalWeight === 0
    ) {

        return 0;
    }


    const weightedTotal =
        valid.reduce(
            (
                total,
                item
            ) =>
                total +
                item.value *
                item.weight,
            0
        );


    return (
        weightedTotal /
        totalWeight
    );
}


/* ============================================================
   Evidence Accuracy
   ============================================================ */

export function calculateAccuracy(
    evidence
) {

    if (
        !evidence ||
        evidence.attempts <= 0
    ) {

        return 0;
    }


    return round(
        clamp(
            (
                evidence.correct /
                evidence.attempts
            ) * 100
        )
    );
}


/* ============================================================
   Concept Score
   ============================================================ */

export function calculateConceptScore(
    concept
) {

    if (
        !concept ||
        !concept.evidence
    ) {

        return 0;
    }


    return calculateAccuracy(
        concept.evidence
    );
}


/* ============================================================
   Skill Score
   ============================================================ */

export function calculateSkillScore(
    skill
) {

    if (!skill) {

        return 0;
    }


    /*
     * If the skill already has a calculated score,
     * use the evidence as the source for recalculation.
     */

    if (
        skill.evidence
    ) {

        return calculateAccuracy(
            skill.evidence
        );
    }


    return clamp(
        Number(
            skill.score
        ) || 0
    );
}


/* ============================================================
   Mini-Test Score
   ============================================================ */

export function calculateMiniTestPerformance(
    miniTests
) {

    if (
        !miniTests ||
        Object.keys(
            miniTests
        ).length === 0
    ) {

        return 0;
    }


    const tests =
        Object.values(
            miniTests
        );


    const scores =
        tests
            .map(
                test =>
                    Number(
                        test.bestScore
                    )
            )
            .filter(
                score =>
                    Number.isFinite(
                        score
                    )
            );


    if (
        scores.length === 0
    ) {

        return 0;
    }


    return round(
        scores.reduce(
            (
                total,
                score
            ) =>
                total + score,
            0
        ) /
        scores.length
    );
}


/* ============================================================
   Concept Performance
   ============================================================ */

export function calculateConceptPerformance(
    concepts
) {

    if (
        !concepts ||
        Object.keys(
            concepts
        ).length === 0
    ) {

        return 0;
    }


    const scores =
        Object.values(
            concepts
        )
            .map(
                calculateConceptScore
            )
            .filter(
                score =>
                    Number.isFinite(
                        score
                    )
            );


    if (
        scores.length === 0
    ) {

        return 0;
    }


    return round(
        scores.reduce(
            (
                total,
                score
            ) =>
                total + score,
            0
        ) /
        scores.length
    );
}


/* ============================================================
   Skill Performance
   ============================================================ */

export function calculateSkillPerformance(
    skills
) {

    if (
        !skills ||
        Object.keys(
            skills
        ).length === 0
    ) {

        return 0;
    }


    const scores =
        Object.values(
            skills
        )
            .map(
                calculateSkillScore
            )
            .filter(
                score =>
                    Number.isFinite(
                        score
                    )
            );


    if (
        scores.length === 0
    ) {

        return 0;
    }


    return round(
        scores.reduce(
            (
                total,
                score
            ) =>
                total + score,
            0
        ) /
        scores.length
    );
}


/* ============================================================
   Determine Status
   ============================================================ */

export function determineStatus(
    score,
    attempts,
    rules
) {

    const safeScore =
        clamp(
            Number(score) || 0
        );


    const safeAttempts =
        Number(attempts) || 0;


    if (
        safeAttempts === 0
    ) {

        return "not-started";
    }


    const levels =
        rules?.statusLevels ||
        {};


    if (
        safeScore >=
            (
                levels.mastered
                    ?.minimumScore ?? 90
            ) &&
        safeAttempts >=
            (
                levels.mastered
                    ?.minimumAttempts ?? 0
            )
    ) {

        return "mastered";
    }


    if (
        safeScore >=
            (
                levels.proficient
                    ?.minimumScore ?? 75
            )
    ) {

        return "proficient";
    }


    if (
        safeScore >=
            (
                levels.developing
                    ?.minimumScore ?? 60
            )
    ) {

        return "developing";
    }


    if (
        safeScore >=
            (
                levels.learning
                    ?.minimumScore ?? 40
            )
    ) {

        return "learning";
    }


    return "learning";
}


/* ============================================================
   Calculate Topic Mastery
   ============================================================ */

export function calculateTopicMastery(
    topic,
    rules
) {

    if (!topic) {

        return {

            score: 0,

            status:
                "not-started",

            reliable: false,

            components: {

                topicAccuracy: 0,

                conceptPerformance: 0,

                skillPerformance: 0,

                miniTestPerformance: 0
            }
        };
    }


    const weights =
        rules?.algorithm?.weights ||
        {};


    const topicAccuracy =
        calculateAccuracy(
            topic.evidence
        );


    const conceptPerformance =
        calculateConceptPerformance(
            topic.concepts
        );


    const skillPerformance =
        calculateSkillPerformance(
            topic.skills
        );


    const miniTestPerformance =
        calculateMiniTestPerformance(
            topic.miniTests
        );


    const score =
        weightedAverage(
            [

                {
                    value:
                        topicAccuracy,

                    weight:
                        weights.topicAccuracy ??
                        0.50
                },

                {
                    value:
                        conceptPerformance,

                    weight:
                        weights.conceptPerformance ??
                        0.20
                },

                {
                    value:
                        skillPerformance,

                    weight:
                        weights.skillPerformance ??
                        0.15
                },

                {
                    value:
                        miniTestPerformance,

                    weight:
                        weights.miniTestPerformance ??
                        0.15
                }

            ]
        );


    const attempts =
        topic.evidence?.attempts ||
        0;


    const minimumReliableAttempts =
        rules
            ?.algorithm
            ?.minimumEvidence
            ?.attemptsForReliableScore ??
        3;


    const reliable =
        attempts >=
        minimumReliableAttempts;


    const status =
        determineStatus(
            score,
            attempts,
            rules
        );


    return {

        score:
            round(
                clamp(score)
            ),

        status,

        reliable,

        attempts,

        components: {

            topicAccuracy:
                round(
                    topicAccuracy
                ),

            conceptPerformance:
                round(
                    conceptPerformance
                ),

            skillPerformance:
                round(
                    skillPerformance
                ),

            miniTestPerformance:
                round(
                    miniTestPerformance
                )
        },

        algorithmVersion:
            rules?.algorithm?.version ||
            "1.0.0"
    };
}


/* ============================================================
   Calculate Complete Mastery
   ============================================================ */

export function calculateMastery(
    progress,
    rules
) {

    if (
        !progress ||
        !progress.topics
    ) {

        return {

            version:
                rules?.algorithm?.version ||
                "1.0.0",

            topics: {}
        };
    }


    const result = {

        version:
            rules?.algorithm?.version ||
            "1.0.0",

        calculatedAt:
            new Date().toISOString(),

        topics: {}
    };


    for (
        const [topicId, topic]
        of Object.entries(
            progress.topics
        )
    ) {

        result.topics[topicId] =
            calculateTopicMastery(
                topic,
                rules
            );
    }


    return result;
}


/* ============================================================
   Get Weak Skills
   ============================================================ */

export function getWeakSkills(
    topic,
    minimumScore = 70
) {

    if (
        !topic?.skills
    ) {

        return [];
    }


    return Object.values(
        topic.skills
    )
        .map(
            skill => ({

                skillId:
                    skill.skillId,

                score:
                    calculateSkillScore(
                        skill
                    )
            })
        )
        .filter(
            skill =>
                skill.score <
                minimumScore
        )
        .sort(
            (
                a,
                b
            ) =>
                a.score -
                b.score
        );
}


/* ============================================================
   Mastery Summary
   ============================================================ */

export function getMasterySummary(
    mastery
) {

    if (
        !mastery?.topics
    ) {

        return {

            totalTopics: 0,

            mastered: 0,

            proficient: 0,

            developing: 0,

            learning: 0,

            notStarted: 0
        };
    }


    const summary = {

        totalTopics: 0,

        mastered: 0,

        proficient: 0,

        developing: 0,

        learning: 0,

        notStarted: 0
    };


    for (
        const topic
        of Object.values(
            mastery.topics
        )
    ) {

        summary.totalTopics += 1;


        if (
            topic.status ===
                "mastered"
        ) {

            summary.mastered += 1;

        }
        else if (
            topic.status ===
                "proficient"
        ) {

            summary.proficient += 1;

        }
        else if (
            topic.status ===
                "developing"
        ) {

            summary.developing += 1;

        }
        else if (
            topic.status ===
                "learning"
        ) {

            summary.learning += 1;

        }
        else {

            summary.notStarted += 1;
        }
    }


    return summary;
}


/* ============================================================
   Default Export
   ============================================================ */

export default {

    calculateAccuracy,

    calculateConceptScore,

    calculateSkillScore,

    calculateMiniTestPerformance,

    calculateConceptPerformance,

    calculateSkillPerformance,

    determineStatus,

    calculateTopicMastery,

    calculateMastery,

    getWeakSkills,

    getMasterySummary
};
