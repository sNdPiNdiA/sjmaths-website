/**
 * SJMaths Maths Mastery
 *
 * STEP 32.34
 * Readiness Resolution Engine
 *
 * Read-only adaptive prerequisite resolver.
 */

const fs = typeof window === "undefined" ? await import("fs") : null;
const path = typeof window === "undefined" ? await import("path") : null;



function safeArray(value) {

    return Array.isArray(value)
        ? value
        : [];
}


function readJsonFile(
    filePath
) {

    const raw =
        fs.readFileSync(
            filePath,
            "utf8"
        );


    /*
     * PowerShell 5.1 can write UTF-8 BOM.
     * Remove U+FEFF before JSON.parse().
     */

    const clean =
        raw.charCodeAt(0) === 0xFEFF
            ? raw.slice(1)
            : raw;


    return JSON.parse(
        clean
    );
}


export class ReadinessResolutionEngine {

    constructor({
        readinessTaxonomy,
        readinessGraph,
        readinessTargets
    } = {}) {

        if (!readinessTaxonomy) {

            throw new Error(
                "ReadinessResolutionEngine: readinessTaxonomy is required."
            );
        }


        if (!readinessGraph) {

            throw new Error(
                "ReadinessResolutionEngine: readinessGraph is required."
            );
        }


        if (!readinessTargets) {

            throw new Error(
                "ReadinessResolutionEngine: readinessTargets is required."
            );
        }


        this.taxonomy =
            readinessTaxonomy;

        this.graph =
            readinessGraph;

        this.targets =
            readinessTargets;


        this.skillById =
            new Map(
                safeArray(
                    this.taxonomy.skills
                ).map(
                    skill => [
                        skill.id,
                        skill
                    ]
                )
            );


        this.targetById =
            new Map(
                safeArray(
                    this.targets.targets
                ).map(
                    target => [
                        target.targetSkillId,
                        target
                    ]
                )
            );


        this.incoming =
            this.buildIncomingGraph(
                this.graph.edges
            );
    }


    buildIncomingGraph(
        edges
    ) {

        const incoming =
            new Map();


        for (
            const edge
            of safeArray(edges)
        ) {

            if (
                !incoming.has(
                    edge.to
                )
            ) {

                incoming.set(
                    edge.to,
                    []
                );
            }


            incoming
                .get(
                    edge.to
                )
                .push(
                    edge
                );
        }


        return incoming;
    }


    getTarget(
        targetSkillId
    ) {

        return (
            this.targetById.get(
                targetSkillId
            ) ||
            null
        );
    }


    getDirectRequirements(
        targetSkillId
    ) {

        const target =
            this.getTarget(
                targetSkillId
            );


        if (!target) {

            return [];
        }


        return safeArray(
            target.readiness
        );
    }


    collectRequiredAncestors(
        readinessSkillId
    ) {

        const result =
            new Map();

        const active =
            new Set();


        const visit =
            skillId => {

                if (
                    active.has(
                        skillId
                    )
                ) {

                    throw new Error(
                        `Required-before cycle detected at ${skillId}`
                    );
                }


                if (
                    result.has(
                        skillId
                    )
                ) {

                    return;
                }


                active.add(
                    skillId
                );


                const incomingEdges =
                    this.incoming.get(
                        skillId
                    ) ||
                    [];


                for (
                    const edge
                    of incomingEdges
                ) {

                    if (
                        edge.relation !==
                        "required-before"
                    ) {

                        continue;
                    }


                    if (
                        !this.skillById.has(
                            edge.from
                        )
                    ) {

                        throw new Error(
                            `Unknown readiness skill: ${edge.from}`
                        );
                    }


                    visit(
                        edge.from
                    );


                    if (
                        !result.has(
                            edge.from
                        )
                    ) {

                        result.set(
                            edge.from,
                            {
                                skillId:
                                    edge.from,

                                depth:
                                    1
                            }
                        );
                    }
                    else {

                        const current =
                            result.get(
                                edge.from
                            );


                        current.depth += 1;
                    }
                }


                active.delete(
                    skillId
                );
            };


        visit(
            readinessSkillId
        );


        return Array.from(
            result.values()
        );
    }


    buildRequirementMap(
        targetSkillId
    ) {

        const target =
            this.getTarget(
                targetSkillId
            );


        if (!target) {

            return null;
        }


        const requirements =
            new Map();


        for (
            const direct
            of safeArray(
                target.readiness
            )
        ) {

            const skillId =
                direct.skillId;


            if (
                !this.skillById.has(
                    skillId
                )
            ) {

                throw new Error(
                    `Unknown readiness skill: ${skillId}`
                );
            }


            requirements.set(
                skillId,
                {
                    skillId,

                    requirement:
                        direct.requirement,

                    direct:
                        true,

                    depth:
                        0
                }
            );


            const ancestors =
                this.collectRequiredAncestors(
                    skillId
                );


            for (
                const ancestor
                of ancestors
            ) {

                if (
                    !requirements.has(
                        ancestor.skillId
                    )
                ) {

                    requirements.set(
                        ancestor.skillId,
                        {
                            skillId:
                                ancestor.skillId,

                            requirement:
                                "prerequisite",

                            direct:
                                false,

                            depth:
                                ancestor.depth
                        }
                    );
                }
            }
        }


        return requirements;
    }


    normalizeEvidence(
        evidence = {}
    ) {

        if (
            evidence.mastered === true
        ) {

            return {
                mastered: true,

                score:
                    Number(
                        evidence.score ??
                        100
                    ),

                attempts:
                    Number(
                        evidence.attempts ??
                        0
                    )
            };
        }


        const score =
            Number(
                evidence.score ??
                0
            );


        return {

            mastered:
                score >= 80,

            score,

            attempts:
                Number(
                    evidence.attempts ??
                    0
                )
        };
    }


    resolve(
        targetSkillId,
        learnerEvidence = {}
    ) {

        const requirements =
            this.buildRequirementMap(
                targetSkillId
            );


        if (!requirements) {

            return {

                targetSkillId,

                found:
                    false,

                ready:
                    false,

                missing: [],

                remediationPath: [],

                explanation:
                    "No readiness target mapping exists."
            };
        }


        const missing = [];


        for (
            const requirement
            of requirements.values()
        ) {

            const evidence =
                learnerEvidence[
                    requirement.skillId
                ] ||
                {};


            const normalized =
                this.normalizeEvidence(
                    evidence
                );


            if (
                !normalized.mastered
            ) {

                const skill =
                    this.skillById.get(
                        requirement.skillId
                    );


                missing.push({

                    skillId:
                        requirement.skillId,

                    name:
                        skill?.name ||
                        requirement.skillId,

                    level:
                        skill?.level ||
                        null,

                    requirement:
                        requirement.requirement,

                    direct:
                        requirement.direct,

                    depth:
                        requirement.depth,

                    score:
                        normalized.score,

                    attempts:
                        normalized.attempts
                });
            }
        }


        const remediationPath =
            this.buildRemediationPath(
                missing
            );


        return {

            targetSkillId,

            found:
                true,

            ready:
                missing.length === 0,

            missing,

            remediationPath,

            explanation:
                missing.length === 0
                    ? "Learner is sufficiently ready."
                    : "Learner has unresolved readiness gaps."
        };
    }


    buildRemediationPath(
        missing
    ) {

        /*
         * Deep prerequisites first.
         *
         * More foundational skills should therefore appear
         * before the target's direct prerequisite.
         */

        const sorted =
            [...missing].sort(
                (
                    a,
                    b
                ) => {

                    if (
                        a.depth !==
                        b.depth
                    ) {

                        return (
                            b.depth -
                            a.depth
                        );
                    }


                    if (
                        a.direct !==
                        b.direct
                    ) {

                        return a.direct
                            ? 1
                            : -1;
                    }


                    return String(
                        a.name
                    ).localeCompare(
                        String(
                            b.name
                        )
                    );
                }
            );


        const seen =
            new Set();


        const result = [];


        for (
            const item
            of sorted
        ) {

            if (
                seen.has(
                    item.skillId
                )
            ) {

                continue;
            }


            seen.add(
                item.skillId
            );


            result.push({

                step:
                    result.length + 1,

                skillId:
                    item.skillId,

                name:
                    item.name,

                level:
                    item.level,

                requirement:
                    item.requirement,

                direct:
                    item.direct,

                depth:
                    item.depth
            });
        }


        return result;
    }


    explain(
        targetSkillId,
        learnerEvidence = {}
    ) {

        const result =
            this.resolve(
                targetSkillId,
                learnerEvidence
            );


        if (
            !result.found
        ) {

            return [
                "No readiness mapping found."
            ];
        }


        if (
            result.ready
        ) {

            return [
                "Learner is ready for the target skill."
            ];
        }


        return [
            `Target: ${targetSkillId}`,

            `Missing readiness skills: ${result.missing.length}`,

            ...result.remediationPath.map(
                item =>
                    `${item.step}. ${item.name}`
            )
        ];
    }
}


export function loadReadinessResolutionEngine(
    rootDir
) {

    const root =
        rootDir ||
        path.resolve(
            process.cwd(),
            "maths-mastery"
        );


    const taxonomy =
        readJsonFile(
            path.join(
                root,
                "data",
                "taxonomy",
                "readiness-taxonomy.json"
            )
        );


    const graph =
        readJsonFile(
            path.join(
                root,
                "data",
                "taxonomy",
                "readiness-graph.json"
            )
        );


    const targets =
        readJsonFile(
            path.join(
                root,
                "data",
                "taxonomy",
                "readiness-targets.json"
            )
        );


    return new ReadinessResolutionEngine({

        readinessTaxonomy:
            taxonomy,

        readinessGraph:
            graph,

        readinessTargets:
            targets
    });
}
