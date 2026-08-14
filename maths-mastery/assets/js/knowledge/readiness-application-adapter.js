/**
 * SJMaths Maths Mastery
 *
 * STEP 32.36
 * Application Readiness Integration
 *
 * Application-facing facade between the application controller
 * and the internal readiness intelligence layer.
 *
 * READ-ONLY.
 */


import {
    loadReadinessResolutionEngine
} from "./readiness-resolution-engine.js";


import {
    ReadinessInterventionPlanner
} from "./readiness-intervention-planner.js";


export class ReadinessApplicationAdapter {

    constructor(
        options = {}
    ) {

        this.resolutionEngine =
            options.resolutionEngine ||
            loadReadinessResolutionEngine(
                options.rootDir
            );


        this.interventionPlanner =
            options.interventionPlanner ||
            new ReadinessInterventionPlanner(
                options.plannerOptions
            );
    }


    resolve(
        targetSkillId,
        learnerEvidence = {}
    ) {

        if (
            !targetSkillId
        ) {

            throw new Error(
                "ReadinessApplicationAdapter: targetSkillId is required."
            );
        }


        return this.resolutionEngine.resolve(
            targetSkillId,
            learnerEvidence
        );
    }


    plan(
        targetSkillId,
        learnerEvidence = {}
    ) {

        const resolution =
            this.resolve(
                targetSkillId,
                learnerEvidence
            );


        return this.interventionPlanner.plan(
            resolution
        );
    }


    getState(
        targetSkillId,
        learnerEvidence = {}
    ) {

        const resolution =
            this.resolve(
                targetSkillId,
                learnerEvidence
            );


        const interventionPlan =
            this.interventionPlanner.plan(
                resolution
            );


        return {

            targetSkillId,

            readiness: {

                found:
                    resolution.found,

                ready:
                    resolution.ready,

                missing:
                    resolution.missing,

                remediationPath:
                    resolution.remediationPath
            },

            interventionPlan
        };
    }


    explain(
        targetSkillId,
        learnerEvidence = {}
    ) {

        const resolution =
            this.resolve(
                targetSkillId,
                learnerEvidence
            );


        return {

            targetSkillId,

            readinessExplanation:
                resolution.explanation,

            interventionPlan:
                this.interventionPlanner.plan(
                    resolution
                )
        };
    }
}


/**
 * Create an application-facing readiness adapter.
 */
export function createReadinessApplicationAdapter(
    options = {}
) {

    return new ReadinessApplicationAdapter(
        options
    );
}
