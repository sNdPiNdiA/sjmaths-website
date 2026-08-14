/**
 * SJMaths Maths Mastery
 *
 * STEP 32.40
 *
 * Readiness Diagnostic / Remediation Flow
 *
 * State-machine layer between live readiness and future
 * diagnostic/remediation UI.
 *
 * IMPORTANT:
 *   This class does NOT mutate learner progress or mastery.
 */


export const READINESS_FLOW_STATES = Object.freeze({

    TARGET_SELECTED:
        "TARGET_SELECTED",

    READINESS_CHECK:
        "READINESS_CHECK",

    TARGET_LEARNING:
        "TARGET_LEARNING",

    NOT_READY:
        "NOT_READY",

    INTERVENTION:
        "INTERVENTION",

    DIAGNOSTIC:
        "DIAGNOSTIC",

    DIAGNOSTIC_RESULT:
        "DIAGNOSTIC_RESULT",

    REASSESS:
        "REASSESS",

    COMPLETE:
        "COMPLETE"
});


function safeArray(
    value
) {

    return Array.isArray(
        value
    )
        ? value
        : [];
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


export class ReadinessRemediationFlow {

    constructor(
        options = {}
    ) {

        this.maxInterventions =
            Number(
                options.maxInterventions ??
                3
            );


        this.targetSkillId =
            null;


        this.currentState =
            null;


        this.readiness =
            null;


        this.interventionPlan =
            null;


        this.currentIntervention =
            null;


        this.diagnosticResult =
            null;


        this.history =
            [];
    }


    reset() {

        this.targetSkillId =
            null;

        this.currentState =
            null;

        this.readiness =
            null;

        this.interventionPlan =
            null;

        this.currentIntervention =
            null;

        this.diagnosticResult =
            null;

        this.history =
            [];

        return this.snapshot();
    }


    transition(
        nextState,
        metadata = {}
    ) {

        this.currentState =
            nextState;


        this.history.push({

            state:
                nextState,

            metadata:
                clone(
                    metadata
                )
        });


        return this.snapshot();
    }


    selectTarget(
        targetSkillId
    ) {

        if (
            typeof targetSkillId !==
            "string" ||
            targetSkillId.length ===
            0
        ) {

            throw new Error(
                "targetSkillId is required."
            );
        }


        this.targetSkillId =
            targetSkillId;


        this.readiness =
            null;


        this.interventionPlan =
            null;


        this.currentIntervention =
            null;


        this.diagnosticResult =
            null;


        return this.transition(
            READINESS_FLOW_STATES.TARGET_SELECTED,
            {
                targetSkillId
            }
        );
    }


    beginReadinessCheck() {

        this.ensureTarget();


        return this.transition(
            READINESS_FLOW_STATES.READINESS_CHECK
        );
    }


    applyReadinessState(
        readinessState
    ) {

        this.ensureTarget();


        if (
            !readinessState ||
            typeof readinessState !==
            "object"
        ) {

            throw new Error(
                "readinessState is required."
            );
        }


        this.readiness =
            clone(
                readinessState
            );


        /*
         * READY
         */

        if (
            readinessState.readiness &&
            readinessState.readiness.ready === true
        ) {

            this.interventionPlan =
                null;


            this.currentIntervention =
                null;


            return this.transition(
                READINESS_FLOW_STATES.TARGET_LEARNING,
                {
                    reason:
                        "learner-ready"
                }
            );
        }


        /*
         * NOT READY
         */

        return this.transition(
            READINESS_FLOW_STATES.NOT_READY,
            {
                reason:
                    "readiness-gaps-found"
            }
        );
    }


    applyInterventionPlan(
        interventionPlan
    ) {

        this.ensureTarget();


        if (
            !interventionPlan ||
            typeof interventionPlan !==
            "object"
        ) {

            throw new Error(
                "interventionPlan is required."
            );
        }


        this.interventionPlan =
            clone(
                interventionPlan
            );


        const blocks =
            safeArray(
                interventionPlan.blocks
            );


        if (
            blocks.length === 0
        ) {

            /*
             * No intervention means return to
             * readiness check rather than creating
             * a dead-end state.
             */

            return this.transition(
                READINESS_FLOW_STATES.REASSESS,
                {
                    reason:
                        "no-intervention-block"
                }
            );
        }


        this.currentIntervention =
            clone(
                blocks[0]
            );


        return this.transition(
            READINESS_FLOW_STATES.INTERVENTION,
            {
                interventionSkillId:
                    this.currentIntervention.skillId
            }
        );
    }


    beginDiagnostic() {

        this.ensureTarget();


        if (
            !this.currentIntervention
        ) {

            throw new Error(
                "No current intervention is selected."
            );
        }


        return this.transition(
            READINESS_FLOW_STATES.DIAGNOSTIC,
            {
                skillId:
                    this.currentIntervention.skillId
            }
        );
    }


    submitDiagnosticResult(
        diagnosticResult
    ) {

        this.ensureTarget();


        if (
            !diagnosticResult ||
            typeof diagnosticResult !==
            "object"
        ) {

            throw new Error(
                "diagnosticResult is required."
            );
        }


        this.diagnosticResult =
            clone(
                diagnosticResult
            );


        return this.transition(
            READINESS_FLOW_STATES.DIAGNOSTIC_RESULT,
            {
                skillId:
                    this.currentIntervention
                        ?.skillId ||
                    null
            }
        );
    }


    beginReassessment() {

        this.ensureTarget();


        return this.transition(
            READINESS_FLOW_STATES.REASSESS,
            {
                afterDiagnostic:
                    true
            }
        );
    }


    completeTarget() {

        this.ensureTarget();


        return this.transition(
            READINESS_FLOW_STATES.COMPLETE,
            {
                reason:
                    "target-complete"
            }
        );
    }


    shouldReturnToTarget(
        readinessState
    ) {

        return !!(
            readinessState &&
            readinessState.readiness &&
            readinessState.readiness.ready === true
        );
    }


    continueAfterReassessment(
        readinessState,
        interventionPlan = null
    ) {

        this.ensureTarget();


        this.readiness =
            clone(
                readinessState
            );


        /*
         * READY → target learning
         */

        if (
            this.shouldReturnToTarget(
                readinessState
            )
        ) {

            this.interventionPlan =
                null;


            this.currentIntervention =
                null;


            this.diagnosticResult =
                null;


            return this.transition(
                READINESS_FLOW_STATES.TARGET_LEARNING,
                {
                    reason:
                        "remediation-succeeded"
                }
            );
        }


        /*
         * Still blocked.
         */

        if (
            interventionPlan
        ) {

            this.applyInterventionPlan(
                interventionPlan
            );


            return this.snapshot();
        }


        return this.transition(
            READINESS_FLOW_STATES.NOT_READY,
            {
                reason:
                    "still-not-ready"
            }
        );
    }


    getCurrentIntervention() {

        return (
            this.currentIntervention
                ? clone(
                    this.currentIntervention
                )
                : null
        );
    }


    getState() {

        return this.currentState;
    }


    snapshot() {

        return {

            state:
                this.currentState,

            targetSkillId:
                this.targetSkillId,

            readiness:
                this.readiness
                    ? clone(
                        this.readiness
                    )
                    : null,

            interventionPlan:
                this.interventionPlan
                    ? clone(
                        this.interventionPlan
                    )
                    : null,

            currentIntervention:
                this.currentIntervention
                    ? clone(
                        this.currentIntervention
                    )
                    : null,

            diagnosticResult:
                this.diagnosticResult
                    ? clone(
                        this.diagnosticResult
                    )
                    : null,

            history:
                clone(
                    this.history
                )
        };
    }


    ensureTarget() {

        if (
            !this.targetSkillId
        ) {

            throw new Error(
                "No target skill selected."
            );
        }
    }
}


/**
 * Convenience factory.
 */
export function createReadinessRemediationFlow(
    options = {}
) {

    return new ReadinessRemediationFlow(
        options
    );
}
