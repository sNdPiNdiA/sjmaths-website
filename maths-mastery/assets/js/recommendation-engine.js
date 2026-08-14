/**
 * SJMaths Maths Mastery
 * Recommendation Engine
 *
 * Pure logic only.
 * No DOM.
 * No localStorage.
 * No fetch.
 * No UI.
 *
 * Input:
 *   student
 *   graph
 *   rules
 *   topicData
 *
 * Output:
 *   ranked recommendations
 *   weak skills
 *   blocked candidates
 *   primary recommendation
 */


/* ============================================================
   Utility
   ============================================================ */

function clamp(value, min = 0, max = 100) {
    return Math.max(min, Math.min(max, value));
}


function round(value, decimals = 2) {
    const factor = Math.pow(10, decimals);
    return Math.round(value * factor) / factor;
}


function average(values) {

    if (!values || values.length === 0) {
        return 0;
    }

    return values.reduce((sum, value) => sum + value, 0) / values.length;
}


/* ============================================================
   Weak Skill Detection
   ============================================================ */

export function getWeakSkills(student, rules) {

    const threshold =
        rules.weakSkillThreshold ?? 70;

    const minimumEvidence =
        rules.gates?.minimumEvidenceForSkill ?? 0;

    const skills = student.skills || {};

    return Object.entries(skills)
        .filter(([skillId, data]) => {

            const score =
                typeof data === "number"
                    ? data
                    : Number(data?.score ?? 0);

            const evidence =
                typeof data === "number"
                    ? Infinity
                    : Number(data?.evidenceCount ?? 0);

            return (
                score < threshold &&
                evidence >= minimumEvidence
            );
        })
        .map(([skillId, data]) => {

            const score =
                typeof data === "number"
                    ? data
                    : Number(data?.score ?? 0);

            return {
                skillId,
                score: clamp(score),
                gap: round(threshold - score),
                severity:
                    score < threshold - 20
                        ? "high"
                        : "moderate"
            };
        })
        .sort((a, b) => a.score - b.score);
}


/* ============================================================
   Graph Helpers
   ============================================================ */

function getNode(graph, topicId) {

    return (graph.nodes || [])
        .find(node => node.topicId === topicId);
}


function getIncomingEdges(graph, topicId) {

    return (graph.edges || [])
        .filter(edge => edge.to === topicId);
}


function getOutgoingEdges(graph, topicId) {

    return (graph.edges || [])
        .filter(edge => edge.from === topicId);
}


/* ============================================================
   Candidate Discovery
   ============================================================ */

export function getCandidates(student, graph, rules) {

    const currentTopic =
        student.currentTopic;

    const outgoing =
        getOutgoingEdges(graph, currentTopic);

    const completed =
        new Set(student.completedTopics || []);

    const recent =
        new Set(student.recentTopics || []);

    const candidates = [];

    for (const edge of outgoing) {

        const topicId = edge.to;

        if (completed.has(topicId)) {
            continue;
        }

        if (
            rules.avoidRecentlyCompleted &&
            recent.has(topicId)
        ) {
            continue;
        }

        const node =
            getNode(graph, topicId);

        if (!node) {
            continue;
        }

        candidates.push({
            topicId,
            node,
            edge
        });
    }

    return candidates;
}


/* ============================================================
   Prerequisite Mastery
   ============================================================ */

function getTopicMastery(student, topicId) {

    if (
        student.topicMastery &&
        typeof student.topicMastery[topicId] === "number"
    ) {
        return student.topicMastery[topicId];
    }

    if (
        topicId === student.currentTopic &&
        typeof student.currentMastery === "number"
    ) {
        return student.currentMastery;
    }

    return 0;
}


function calculatePrerequisiteScore(
    student,
    graph,
    candidate,
    rules
) {

    const prerequisiteEdges =
        getIncomingEdges(graph, candidate.topicId)
            .filter(edge =>
                edge.relation === "prerequisite"
            );

    /*
     * If there are no prerequisite edges,
     * use graph connection strength.
     */

    if (prerequisiteEdges.length === 0) {

        return {
            score: round(
                candidate.edge.strength * 100
            ),
            blocked: false,
            prerequisites: []
        };
    }


    const prerequisites =
        prerequisiteEdges.map(edge => {

            const mastery =
                getTopicMastery(
                    student,
                    edge.from
                );

            return {
                topicId: edge.from,
                mastery: clamp(mastery),
                required:
                    rules.gates.minimumPrerequisiteMastery,
                strength: edge.strength
            };
        });


    const blocked =
        rules.hardPrerequisiteGate &&
        prerequisites.some(
            item =>
                item.mastery <
                item.required
        );


    /*
     * Mastery contributes continuously.
     * A student at 70% should not be treated
     * exactly the same as one at 95%.
     */

    const weightedScores =
        prerequisites.map(item => {

            const masteryRatio =
                clamp(item.mastery) / 100;

            return (
                masteryRatio *
                item.strength *
                100
            );
        });


    const totalStrength =
        prerequisites.reduce(
            (sum, item) =>
                sum + item.strength,
            0
        );


    const score =
        totalStrength > 0
            ? weightedScores.reduce(
                (sum, value) =>
                    sum + value,
                0
            ) / totalStrength
            : 0;


    return {
        score: round(score),
        blocked,
        prerequisites
    };
}


/* ============================================================
   Exam Relevance
   ============================================================ */

function calculateExamRelevance(
    candidate,
    student,
    topicData
) {

    const exam =
        student.selectedExam;

    /*
     * Expected structure:
     *
     * topicData[topicId].examRelevance = {
     *     ssc: 95,
     *     banking: 80
     * }
     */

    const relevance =
        topicData?.[candidate.topicId]
            ?.examRelevance?.[exam];


    if (typeof relevance === "number") {
        return clamp(relevance);
    }


    /*
     * If no exam-specific value exists,
     * use a neutral score rather than inventing
     * importance.
     */

    return 50;
}


/* ============================================================
   Path Continuity
   ============================================================ */

function calculatePathContinuity(
    candidate,
    graph,
    student
) {

    const currentTopic =
        student.currentTopic;

    const edge =
        (graph.edges || []).find(
            item =>
                item.from === currentTopic &&
                item.to === candidate.topicId
        );


    if (!edge) {
        return 0;
    }


    let score =
        edge.strength * 100;


    if (edge.relation === "prerequisite") {
        score += 10;
    }

    if (edge.relation === "progression") {
        score += 5;
    }


    return clamp(score);
}


/* ============================================================
   Mastery Fit
   ============================================================ */

function calculateMasteryFit(
    student,
    candidate
) {

    const mastery =
        clamp(
            student.currentMastery ?? 0
        );


    /*
     * Best fit is around the student's
     * current learning level.
     */

    const level =
        candidate.node?.level;


    const targetRanges = {

        foundation: [0, 45],

        basic: [35, 70],

        intermediate: [55, 85],

        advanced: [70, 95],

        competitive: [75, 100]
    };


    const range =
        targetRanges[level] ??
        [40, 90];


    const [min, max] = range;


    if (
        mastery >= min &&
        mastery <= max
    ) {
        return 100;
    }


    if (mastery < min) {

        const gap =
            min - mastery;

        return clamp(
            100 - gap * 2
        );
    }


    const gap =
        mastery - max;

    return clamp(
        100 - gap * 2
    );
}


/* ============================================================
   Difficulty Fit
   ============================================================ */

function calculateDifficultyFit(
    student,
    candidate
) {

    const mastery =
        clamp(
            student.currentMastery ?? 0
        );


    const level =
        candidate.node?.level;


    const difficultyMinimum = {

        foundation: 0,

        basic: 40,

        intermediate: 60,

        advanced: 75,

        competitive: 80
    };


    const minimum =
        difficultyMinimum[level] ?? 50;


    if (mastery >= minimum) {
        return 100;
    }


    const gap =
        minimum - mastery;


    return clamp(
        100 - gap * 2
    );
}


/* ============================================================
   Candidate Score
   ============================================================ */

function calculateCandidateScore(
    candidate,
    student,
    graph,
    rules,
    topicData
) {

    const prerequisite =
        calculatePrerequisiteScore(
            student,
            graph,
            candidate,
            rules
        );


    const examRelevance =
        calculateExamRelevance(
            candidate,
            student,
            topicData
        );


    const pathContinuity =
        calculatePathContinuity(
            candidate,
            graph,
            student
        );


    const masteryFit =
        calculateMasteryFit(
            student,
            candidate
        );


    const difficultyFit =
        calculateDifficultyFit(
            student,
            candidate
        );


    const weights =
        rules.weights;


    let score =

        prerequisite.score *
        weights.prerequisite +

        examRelevance *
        weights.examRelevance +

        pathContinuity *
        weights.pathContinuity +

        masteryFit *
        weights.masteryFit +

        difficultyFit *
        weights.difficultyFit;


    /*
     * Hard prerequisite gate.
     */

    if (prerequisite.blocked) {
        score = 0;
    }


    return {

        score: round(score),

        components: {

            prerequisite: prerequisite.score,

            examRelevance: round(
                examRelevance
            ),

            pathContinuity: round(
                pathContinuity
            ),

            masteryFit: round(
                masteryFit
            ),

            difficultyFit: round(
                difficultyFit
            )
        },

        prerequisiteDetails:
            prerequisite.prerequisites,

        blocked:
            prerequisite.blocked
    };
}


/* ============================================================
   Reason Generator
   ============================================================ */

function generateReason(
    candidate,
    result,
    weakSkills
) {

    if (result.blocked) {

        return {
            type: "prerequisite-blocked",
            text:
                "Strengthen the prerequisite topic before moving to this topic."
        };
    }


    const components =
        result.components;


    const strongest =
        Object.entries(components)
            .sort(
                (a, b) => b[1] - a[1]
            )[0];


    const reasons = {

        prerequisite:
            "This topic builds directly on concepts you have already learned.",

        examRelevance:
            "This topic is highly relevant to your selected examination.",

        pathContinuity:
            "This topic continues your current learning path.",

        masteryFit:
            "Your current mastery makes this an appropriate next step.",

        difficultyFit:
            "The difficulty is appropriate for your current level."
    };


    const primaryReason =
        reasons[strongest[0]];


    const weakSkill =
        weakSkills.length > 0
            ? weakSkills[0]
            : null;


    return {

        type: strongest[0],

        text: primaryReason,

        weakSkill: weakSkill
            ? {
                skillId:
                    weakSkill.skillId,

                score:
                    weakSkill.score,

                gap:
                    weakSkill.gap
            }
            : null
    };
}


/* ============================================================
   Main Recommendation Function
   ============================================================ */

export function recommendNextTopics({
    student,
    graph,
    rules,
    topicData = {}
}) {

    if (!student) {
        throw new Error(
            "Recommendation Engine: student data is required."
        );
    }


    if (!graph) {
        throw new Error(
            "Recommendation Engine: graph is required."
        );
    }


    if (!rules) {
        throw new Error(
            "Recommendation Engine: rules are required."
        );
    }


    const weakSkills =
        getWeakSkills(
            student,
            rules
        );


    const candidates =
        getCandidates(
            student,
            graph,
            rules
        );


    const ranked =
        candidates
            .map(candidate => {

                const result =
                    calculateCandidateScore(
                        candidate,
                        student,
                        graph,
                        rules,
                        topicData
                    );


                return {

                    topicId:
                        candidate.topicId,

                    level:
                        candidate.node.level,

                    relation:
                        candidate.edge.relation,

                    edgeStrength:
                        candidate.edge.strength,

                    score:
                        result.score,

                    components:
                        result.components,

                    prerequisites:
                        result.prerequisiteDetails,

                    blocked:
                        result.blocked,

                    reason:
                        generateReason(
                            candidate,
                            result,
                            weakSkills
                        )
                };
            })
            .sort(
                (a, b) =>
                    b.score - a.score
            );


    const limit =
        rules.recommendationLimit ?? 3;


    const recommendations =
        ranked
            .filter(
                item =>
                    !item.blocked
            )
            .slice(0, limit);


    const blocked =
        ranked
            .filter(
                item =>
                    item.blocked
            );


    let primary =
        recommendations[0] ?? null;


    /*
     * Fallback when no candidate passes.
     */

    if (
        !primary &&
        rules.fallback?.enabled
    ) {

        const fallback =
            ranked.find(
                item =>
                    item.score >=
                    rules.fallback.minimumScore
            );

        if (fallback) {
            primary = fallback;
        }
    }


    return {

        currentTopic:
            student.currentTopic,

        currentMastery:
            clamp(
                student.currentMastery ?? 0
            ),

        selectedExam:
            student.selectedExam ?? null,

        weakSkills,

        primaryRecommendation:
            primary,

        recommendations,

        blocked,

        candidateCount:
            candidates.length,

        generatedAt:
            new Date().toISOString()
    };
}


/* ============================================================
   Default export
   ============================================================ */

export default {
    recommendNextTopics,
    getWeakSkills,
    getCandidates
};
