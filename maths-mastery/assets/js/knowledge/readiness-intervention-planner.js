/**
 * SJMaths Maths Mastery
 *
 * STEP 32.35
 * Readiness Intervention Planner
 *
 * Converts raw readiness-resolution output into a compact,
 * learner-oriented intervention plan.
 *
 * READ-ONLY.
 */


function safeArray(
    value
) {

    return Array.isArray(
        value
    )
        ? value
        : [];
}


export class ReadinessInterventionPlanner {

    constructor(
        options = {}
    ) {

        this.maxVisibleBlocks =
            Number(
                options.maxVisibleBlocks ??
                3
            );


        this.maxVisiblePrerequisites =
            Number(
                options.maxVisiblePrerequisites ??
                4
            );


        this.diagnosticQuestionsPerBlock =
            Number(
                options.diagnosticQuestionsPerBlock ??
                5
            );
    }


    plan(
        resolution
    ) {

        if (
            !resolution ||
            !resolution.found
        ) {

            return {

                found:
                    false,

                ready:
                    false,

                targetSkillId:
                    resolution?.targetSkillId ||
                    null,

                interventionRequired:
                    false,

                blocks: [],

                explanation:
                    "No readiness resolution is available."
            };
        }


        if (
            resolution.ready
        ) {

            return {

                found:
                    true,

                ready:
                    true,

                targetSkillId:
                    resolution.targetSkillId,

                interventionRequired:
                    false,

                blocks: [],

                explanation:
                    "Learner is ready for the target skill."
            };
        }


        const missing =
            safeArray(
                resolution.missing
            );


        const path =
            safeArray(
                resolution.remediationPath
            );


        const blocks =
            this.buildBlocks(
                missing,
                path
            );


        return {

            found:
                true,

            ready:
                false,

            targetSkillId:
                resolution.targetSkillId,

            interventionRequired:
                blocks.length >
                0,

            blocks,

            totalMissingSkills:
                missing.length,

            totalRemediationSteps:
                path.length,

            explanation:
                this.buildExplanation(
                    blocks,
                    resolution.targetSkillId
                )
        };
    }


    buildBlocks(
        missing,
        remediationPath
    ) {

        const missingById =
            new Map(
                missing.map(
                    item => [
                        item.skillId,
                        item
                    ]
                )
            );


        /*
         * Prefer the highest immediate blockers.
         *
         * Direct prerequisites are more useful for the first
         * learner-facing intervention than exposing the entire
         * deep prerequisite closure.
         */

        const direct =
            missing.filter(
                item =>
                    item.direct === true
            );


        const prerequisiteOnly =
            missing.filter(
                item =>
                    item.direct !== true
            );


        let seeds =
            direct.length > 0
                ? direct
                : prerequisiteOnly;


        /*
         * Deterministic ordering:
         *   1. core before supporting
         *   2. shallower direct blocker first
         *   3. deeper prerequisite only if needed
         *   4. alphabetical fallback
         */

        seeds =
            [...seeds].sort(
                (
                    a,
                    b
                ) => {

                    const rank =
                        item =>
                            item.requirement ===
                            "core"
                                ? 0
                                : 1;


                    const aRank =
                        rank(a);

                    const bRank =
                        rank(b);


                    if (
                        aRank !==
                        bRank
                    ) {

                        return (
                            aRank -
                            bRank
                        );
                    }


                    if (
                        a.direct !==
                        b.direct
                    ) {

                        return a.direct
                            ? -1
                            : 1;
                    }


                    if (
                        a.depth !==
                        b.depth
                    ) {

                        return (
                            a.depth -
                            b.depth
                        );
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


        const selected =
            seeds.slice(
                0,
                this.maxVisibleBlocks
            );


        const blocks = [];


        for (
            const item
            of selected
        ) {

            const supporting =
                prerequisiteOnly
                    .filter(
                        candidate =>
                            candidate.skillId !==
                            item.skillId
                    )
                    .sort(
                        (
                            a,
                            b
                        ) =>
                            a.depth -
                            b.depth
                    )
                    .slice(
                        0,
                        this.maxVisiblePrerequisites
                    );


            blocks.push({

                id:
                    `readiness.${this.slug(
                        item.skillId
                    )}`,

                skillId:
                    item.skillId,

                title:
                    item.name,

                level:
                    item.level ||
                    null,

                requirement:
                    item.requirement,

                blockerType:
                    item.direct
                        ? "direct"
                        : "foundational",

                depth:
                    item.depth,

                diagnostic:
                    {

                        mode:
                            "targeted-readiness-check",

                        questionCount:
                            this.diagnosticQuestionsPerBlock,

                        completionCondition:
                            "demonstrate-sufficient-mastery"
                    },

                supportingPrerequisites:
                    supporting.map(
                        prerequisite => ({

                            skillId:
                                prerequisite.skillId,

                            name:
                                prerequisite.name,

                            level:
                                prerequisite.level ||
                                null,

                            depth:
                                prerequisite.depth
                        })
                    ),

                action:
                    {

                        type:
                            "remediate",

                        skillId:
                            item.skillId,

                        returnToTargetAfterCompletion:
                            true
                    }
            });
        }


        return blocks;
    }


    buildExplanation(
        blocks,
        targetSkillId
    ) {

        if (
            blocks.length === 0
        ) {

            return (
                `No intervention block is required for ${targetSkillId}.`
            );
        }


        const titles =
            blocks.map(
                block =>
                    block.title
            );


        return (
            `Before learning ${targetSkillId}, `
            +
            `strengthen: `
            +
            titles.join(
                ", "
            )
            +
            "."
        );
    }


    slug(
        value
    ) {

        return String(
            value
        )

        .toLowerCase()

        .replace(
            /[^a-z0-9]+/g,
            "-"
        )

        .replace(
            /^-+|-+$/g,
            ""
        );
    }
}
