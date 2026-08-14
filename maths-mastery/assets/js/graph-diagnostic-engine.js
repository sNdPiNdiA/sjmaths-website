/**
 * SJMaths Maths Mastery
 * STEP 21
 *
 * Graph-Aware Diagnostic Placement
 *
 * The diagnostic engine now understands:
 *
 * prerequisite
 * progression
 * related
 *
 * IMPORTANT:
 *
 * "related" NEVER blocks progression.
 *
 * A prerequisite can block a downstream topic
 * when its readiness is below the configured threshold.
 */


/* ============================================================
   Constants
   ============================================================ */

const DEFAULT_MINIMUM_READINESS = 70;

const DEFAULT_FOUNDATION =
    "number-system";


const BLOCKING_RELATIONS = new Set([
    "prerequisite"
]);


/* ============================================================
   Validate Graph
   ============================================================ */

export function validateGraph(
    graph
) {

    if (!graph) {
        return false;
    }

    if (
        !Array.isArray(
            graph.nodes
        )
    ) {
        return false;
    }

    if (
        !Array.isArray(
            graph.edges
        )
    ) {
        return false;
    }


    const nodeIds =
        new Set(
            graph.nodes.map(
                node =>
                    node.topicId
            )
        );


    for (
        const edge
        of graph.edges
    ) {

        if (
            !edge.from ||
            !edge.to ||
            !edge.relation
        ) {
            return false;
        }


        if (
            !nodeIds.has(
                edge.from
            ) ||
            !nodeIds.has(
                edge.to
            )
        ) {
            return false;
        }


        if (
            ![
                "prerequisite",
                "progression",
                "related"
            ].includes(
                edge.relation
            )
        ) {
            return false;
        }
    }


    return true;
}


/* ============================================================
   Get Incoming Edges
   ============================================================ */

export function getIncomingEdges(
    graph,
    topicId
) {

    if (
        !validateGraph(
            graph
        )
    ) {
        throw new Error(
            "Invalid topic graph"
        );
    }


    return graph.edges.filter(
        edge =>
            edge.to ===
            topicId
    );
}


/* ============================================================
   Get Prerequisites
   ============================================================ */

export function getPrerequisites(
    graph,
    topicId
) {

    return getIncomingEdges(
        graph,
        topicId
    ).filter(
        edge =>
            edge.relation ===
            "prerequisite"
    );
}


/* ============================================================
   Get Related Topics
   ============================================================ */

export function getRelatedTopics(
    graph,
    topicId
) {

    return getIncomingEdges(
        graph,
        topicId
    ).filter(
        edge =>
            edge.relation ===
            "related"
    );
}


/* ============================================================
   Get Progression Edges
   ============================================================ */

export function getProgressionEdges(
    graph,
    topicId
) {

    return getIncomingEdges(
        graph,
        topicId
    ).filter(
        edge =>
            edge.relation ===
            "progression"
    );
}


/* ============================================================
   Determine Whether Topic Is Blocked
   ============================================================ */

export function isTopicBlocked(
    topicId,
    topicStatistics,
    graph,
    options = {}
) {

    const minimumReadiness =
        options.minimumReadiness ??
        DEFAULT_MINIMUM_READINESS;


    const prerequisites =
        getPrerequisites(
            graph,
            topicId
        );


    /*
     * No prerequisites means
     * nothing can block the topic.
     */

    if (
        prerequisites.length ===
            0
    ) {
        return {

            blocked:
                false,

            blockers:
                []
        };
    }


    const blockers = [];


    for (
        const prerequisite
        of prerequisites
    ) {

        const statistics =
            topicStatistics[
                prerequisite.from
            ];


        /*
         * No evidence for a prerequisite
         * means readiness has not been
         * demonstrated.
         */

        if (
            !statistics ||
            statistics.answered === 0
        ) {

            blockers.push({

                topicId:
                    prerequisite.from,

                reason:
                    "Prerequisite has insufficient diagnostic evidence.",

                accuracy:
                    null
            });

            continue;
        }


        if (
            statistics.accuracy <
                minimumReadiness
        ) {

            blockers.push({

                topicId:
                    prerequisite.from,

                reason:
                    `Prerequisite readiness is ${statistics.accuracy}%, below ${minimumReadiness}%.`,

                accuracy:
                    statistics.accuracy
            });
        }
    }


    return {

        blocked:
            blockers.length >
            0,

        blockers
    };
}


/* ============================================================
   Find Earliest Weak Prerequisite
   ============================================================ */

export function findWeakPrerequisite(
    topicId,
    topicStatistics,
    graph,
    options = {}
) {

    const minimumReadiness =
        options.minimumReadiness ??
        DEFAULT_MINIMUM_READINESS;


    const prerequisites =
        getPrerequisites(
            graph,
            topicId
        );


    for (
        const edge
        of prerequisites
    ) {

        const statistics =
            topicStatistics[
                edge.from
            ];


        if (
            !statistics ||
            statistics.answered === 0
        ) {

            return {

                topicId:
                    edge.from,

                reason:
                    "Prerequisite has not demonstrated sufficient readiness."
            };
        }


        if (
            statistics.accuracy <
                minimumReadiness
        ) {

            return {

                topicId:
                    edge.from,

                reason:
                    `Prerequisite readiness is ${statistics.accuracy}%, below ${minimumReadiness}%.`
            };
        }
    }


    return null;
}


/* ============================================================
   Find Candidate Topics
   ============================================================ */

export function findCandidateTopics(
    topicStatistics,
    graph
) {

    const nodeIds =
        graph.nodes.map(
            node =>
                node.topicId
        );


    return nodeIds.filter(
        topicId => {

            const statistics =
                topicStatistics[
                    topicId
                ];


            /*
             * Unassessed topics are
             * candidates.
             */

            return (
                !statistics ||
                statistics.answered === 0
            );
        }
    );
}


/* ============================================================
   Find Earliest Blocking Topic
   ============================================================ */

export function findEarliestBlockingTopic(
    topicStatistics,
    graph,
    options = {}
) {

    const minimumReadiness =
        options.minimumReadiness ??
        DEFAULT_MINIMUM_READINESS;


    const orderedTopics =
        buildGraphLearningOrder(
            graph
        );


    /*
     * --------------------------------------------------------
     * RULE 1
     *
     * If a topic has evidence and is below the readiness
     * threshold, it is a genuine diagnostic weakness.
     *
     * We evaluate ONLY topics that were actually assessed.
     *
     * This prevents an unassessed "related" topic from
     * hijacking placement.
     * --------------------------------------------------------
     */

    for (
        const topicId
        of orderedTopics
    ) {

        const statistics =
            topicStatistics[
                topicId
            ];


        if (
            !statistics ||
            statistics.answered === 0
        ) {

            continue;
        }


        if (
            statistics.accuracy <
                minimumReadiness
        ) {

            /*
             * Before returning the weak topic, check whether
             * one of its own prerequisites is even weaker.
             *
             * If so, placement should start at that prerequisite.
             */

            const weakPrerequisite =
                findWeakPrerequisite(
                    topicId,
                    topicStatistics,
                    graph,
                    {
                        minimumReadiness
                    }
                );


            if (
                weakPrerequisite
            ) {

                return {

                    topicId:
                        weakPrerequisite.topicId,

                    reason:
                        weakPrerequisite.reason
                };
            }


            return {

                topicId,

                reason:
                    `Diagnostic readiness is ${statistics.accuracy}%, below ${minimumReadiness}%.`
            };
        }
    }


    /*
     * --------------------------------------------------------
     * RULE 2
     *
     * If all assessed topics are ready, find the first
     * UNASSESSED topic whose TRUE PREREQUISITES are ready.
     *
     * "related" edges are deliberately ignored.
     * --------------------------------------------------------
     */

    for (
        const topicId
        of orderedTopics
    ) {

        const statistics =
            topicStatistics[
                topicId
            ];


        if (
            statistics &&
            statistics.answered > 0
        ) {

            continue;
        }


        const prerequisiteState =
            isTopicBlocked(
                topicId,
                topicStatistics,
                graph,
                {
                    minimumReadiness
                }
            );


        if (
            !prerequisiteState.blocked
        ) {

            return {

                topicId,

                reason:
                    "All assessed topics are ready and this topic's prerequisites are ready."
            };
        }
    }


    /*
     * --------------------------------------------------------
     * RULE 3
     *
     * If every topic has evidence and all are ready, return
     * the final topic.
     * --------------------------------------------------------
     */

    if (
        orderedTopics.length > 0
    ) {

        return {

            topicId:
                orderedTopics[
                    orderedTopics.length - 1
                ],

            reason:
                "All assessed topics meet the diagnostic readiness threshold."
        };
    }


    return null;
}

/* ============================================================
   Build Graph Learning Order
   ============================================================ */

export function buildGraphLearningOrder(
    graph
) {

    if (
        !validateGraph(
            graph
        )
    ) {
        throw new Error(
            "Invalid topic graph"
        );
    }


    const nodes =
        graph.nodes;


    const indegree = {};

    const adjacency = {};


    for (
        const node
        of nodes
    ) {

        indegree[
            node.topicId
        ] = 0;

        adjacency[
            node.topicId
        ] = [];
    }


    /*
     * Only prerequisite and progression
     * edges affect learning order.
     *
     * Related edges are deliberately
     * excluded.
     */

    for (
        const edge
        of graph.edges
    ) {

        if (
            ![
                "prerequisite",
                "progression"
            ].includes(
                edge.relation
            )
        ) {

            continue;
        }


        if (
            !adjacency[
                edge.from
            ]
        ) {

            adjacency[
                edge.from
            ] = [];
        }


        adjacency[
            edge.from
        ].push(
            edge.to
        );


        indegree[
            edge.to
        ]++;
    }


    const queue =
        nodes
            .filter(
                node =>
                    indegree[
                        node.topicId
                    ] === 0
            )
            .map(
                node =>
                    node.topicId
            );


    const order = [];


    while (
        queue.length >
        0
    ) {

        const current =
            queue.shift();


        order.push(
            current
        );


        for (
            const next
            of adjacency[
                current
            ] || []
        ) {

            indegree[
                next
            ]--;


            if (
                indegree[
                    next
                ] === 0
            ) {

                queue.push(
                    next
                );
            }
        }
    }


    /*
     * Safety fallback in case a
     * graph contains a cycle.
     */

    if (
        order.length !==
        nodes.length
    ) {

        return nodes.map(
            node =>
                node.topicId
        );
    }


    return order;
}


/* ============================================================
   Recommend Starting Topic
   ============================================================ */

export function recommendGraphAwareStartingTopic(
    topicStatistics,
    graph,
    options = {}
) {

    const minimumReadiness =
        options.minimumReadiness ??
        DEFAULT_MINIMUM_READINESS;


    const result =
        findEarliestBlockingTopic(
            topicStatistics,
            graph,
            {
                minimumReadiness
            }
        );


    if (result) {

        return result;
    }


    return {

        topicId:
            graph.nodes[0]?.topicId ||
            DEFAULT_FOUNDATION,

        reason:
            "Foundation topic selected."
    };
}


/* ============================================================
   Explain Topic Readiness
   ============================================================ */

export function explainTopicReadiness(
    topicId,
    topicStatistics,
    graph,
    options = {}
) {

    const minimumReadiness =
        options.minimumReadiness ??
        DEFAULT_MINIMUM_READINESS;


    const statistics =
        topicStatistics[
            topicId
        ];


    const prerequisites =
        getPrerequisites(
            graph,
            topicId
        );


    const related =
        getRelatedTopics(
            graph,
            topicId
        );


    const progression =
        getProgressionEdges(
            graph,
            topicId
        );


    const blockerState =
        isTopicBlocked(
            topicId,
            topicStatistics,
            graph,
            {
                minimumReadiness
            }
        );


    return {

        topicId,

        accuracy:
            statistics?.accuracy ??
            null,

        answered:
            statistics?.answered ??
            0,

        prerequisites:
            prerequisites.map(
                edge => ({
                    topicId:
                        edge.from,

                    relation:
                        edge.relation,

                    strength:
                        edge.strength ??
                        null
                })
            ),

        relatedTopics:
            related.map(
                edge =>
                    edge.from
            ),

        progressionSources:
            progression.map(
                edge =>
                    edge.from
            ),

        blocked:
            blockerState.blocked,

        blockers:
            blockerState.blockers
    };
}


/* ============================================================
   Export
   ============================================================ */

export default {

    validateGraph,

    getIncomingEdges,

    getPrerequisites,

    getRelatedTopics,

    getProgressionEdges,

    isTopicBlocked,

    findWeakPrerequisite,

    findCandidateTopics,

    findEarliestBlockingTopic,

    buildGraphLearningOrder,

    recommendGraphAwareStartingTopic,

    explainTopicReadiness
};

