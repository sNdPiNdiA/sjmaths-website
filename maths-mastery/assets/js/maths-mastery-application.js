/**
 * SJMaths Maths Mastery
 * STEP 24 — Unified Application Controller
 *
 * Application orchestration layer.
 *
 * This controller coordinates the engines created in
 * Steps 15–23.
 *
 * It does NOT duplicate their algorithms.
 */


/* ============================================================
   Imports
   ============================================================ */

import {
    createNewLearnerFlow,
    startOnboarding,
    selectExam,
    selectFoundationRoute,
    prepareDiagnostic,
    completeDiagnostic,
    applyLearningResult,
    applyRecommendation,
    determineFlowState,
    buildDashboardState
} from "./learner-flow-engine.js";


import {
    LearnerSessionRepository
} from "./learner-session-repository.js";
import {
    ReadinessApplicationAdapter
} from "./knowledge/readiness-application-adapter.js";
import {
    ReadinessEvidenceAdapter
} from "./knowledge/readiness-evidence-adapter.js";
import {
    ReadinessRemediationOrchestrator
} from "./knowledge/readiness-remediation-orchestrator.js";


/* ============================================================
   Controller
   ============================================================ */

export class MathsMasteryApplication {

    constructor(
        options = {}
    ) {

        this.sessionRepository =
            options.sessionRepository ||
            new LearnerSessionRepository(
                options.storage,
                options.sessionKey
            );


        this.progressRepository =
            options.progressRepository ||
            null;


        this.masteryEngine =
            options.masteryEngine ||
            null;


        this.recommendationEngine =
            options.recommendationEngine ||
            null;


        this.diagnosticEngine =
            options.diagnosticEngine ||
            null;
        this.readinessAdapter =
            options.readinessAdapter ||
            new ReadinessApplicationAdapter();
        this.readinessEvidenceAdapter =
            options.readinessEvidenceAdapter ||
            new ReadinessEvidenceAdapter();


        this.flow =
            null;


        this.progress =
            null;


        this.mastery =
            null;


        this.recommendation =
            null;
    }


    /* ========================================================
       START
       ======================================================== */

    start(
        studentId
    ) {

        if (
            !studentId ||
            typeof studentId !==
                "string"
        ) {

            throw new Error(
                "studentId is required"
            );
        }


        const existing =
            this.sessionRepository.loadFlow();


        if (
            existing
        ) {

            this.flow =
                structuredClone(
                    existing
                );

            this.restoreProgress();


            return this.getState();
        }


        this.flow =
            createNewLearnerFlow(
                studentId
            );


        this.save();


        return this.getState();
    }


    /* ========================================================
       RESTORE
       ======================================================== */

    restore() {

        const restored =
            this.sessionRepository.loadFlow();


        if (
            !restored
        ) {

            return null;
        }


        this.flow =
            structuredClone(
                restored
            );


        this.restoreProgress();


        return this.getState();
    }


    /* ========================================================
       PROGRESS RESTORATION
       ======================================================== */

    restoreProgress() {

        if (
            !this.progressRepository ||
            !this.flow
        ) {

            return;
        }


        try {

            this.progress =
                this.progressRepository.load(
                    this.flow.studentId
                );

        }
        catch {

            try {

                this.progress =
                    this.progressRepository.load();

            }
            catch {

                this.progress =
                    null;
            }
        }
    }


    /* ========================================================
       SAVE
       ======================================================== */

    save() {

        if (
            !this.flow
        ) {

            throw new Error(
                "Application has not been started"
            );
        }


        this.sessionRepository.save(
            this.flow
        );


        return this.flow;
    }


    /* ========================================================
       ONBOARDING
       ======================================================== */

    beginOnboarding() {

        this.flow =
            startOnboarding(
                this.flow
            );


        this.save();


        return this.getState();
    }


    selectExam(
        examId
    ) {

        this.flow =
            selectExam(
                this.flow,
                examId
            );


        this.save();


        return this.getState();
    }


    chooseFoundation(
        startingPoint =
            "number-system"
    ) {

        this.flow =
            selectFoundationRoute(
                this.flow,
                startingPoint
            );


        this.save();


        return this.getState();
    }


    /* ========================================================
       DIAGNOSTIC
       ======================================================== */

    startDiagnostic() {

        this.flow =
            prepareDiagnostic(
                this.flow
            );


        this.save();


        return this.getState();
    }


    completeDiagnostic(
        result
    ) {

        this.flow =
            completeDiagnostic(
                this.flow,
                result
            );


        this.save();


        return this.getState();
    }


    /* ========================================================
       LEARNING
       ======================================================== */

    recordLearningResult(
        result
    ) {

        this.flow =
            applyLearningResult(
                this.flow,
                result
            );


        this.save();


        return this.getState();
    }


    /* ========================================================
       RECOMMENDATION
       ======================================================== */

    setRecommendation(
        recommendation
    ) {

        this.recommendation =
            recommendation ||
            null;


        this.flow =
            applyRecommendation(
                this.flow,
                recommendation
            );


        this.save();


        return this.getState();
    }


    /* ========================================================
       MASTERY
       ======================================================== */

    setMastery(
        mastery
    ) {

        this.mastery =
            mastery ??
            null;


        return this.getState();
    }


    /* ========================================================
       PROGRESS
       ======================================================== */

    setProgress(
        progress
    ) {

        this.progress =
            progress ??
            null;


        return this.getState();
    }


    /* ========================================================
       DIAGNOSTIC ENGINE HANDOFF
       ======================================================== */

    runDiagnostic(
        diagnosticResult
    ) {

        if (
            !diagnosticResult
        ) {

            throw new Error(
                "diagnosticResult is required"
            );
        }


        return this.completeDiagnostic(
            diagnosticResult
        );
    }


    /* ========================================================
       MASTERY ENGINE HANDOFF
       ======================================================== */

    calculateMastery(
        masteryResult
    ) {

        this.mastery =
            masteryResult ??
            null;


        if (
            masteryResult
        ) {

            this.flow =
                applyLearningResult(
                    this.flow,
                    {

                        topicId:
                            masteryResult.topicId ||
                            this.flow
                                ?.learning
                                ?.currentTopic,

                        mastery:
                            masteryResult.score ??
                            masteryResult.mastery ??
                            null,

                        weakSkills:
                            masteryResult.weakSkills ||
                            [],

                        nextTopic:
                            this.flow
                                ?.learning
                                ?.nextTopic ||
                            null
                    }
                );


            this.save();
        }


        return this.getState();
    }


    /* ========================================================
       RECOMMENDATION ENGINE HANDOFF
       ======================================================== */

    calculateRecommendation(
        recommendationResult
    ) {

        this.recommendation =
            recommendationResult ??
            null;


        if (
            recommendationResult
        ) {

            this.flow =
                applyRecommendation(
                    this.flow,
                    recommendationResult
                );


            this.save();
        }


        return this.getState();
    }


    /* ========================================================
       CURRENT STATE
       ======================================================== */

    getState() {

        if (
            !this.flow
        ) {

            return null;
        }


        return {

            studentId:
                this.flow.studentId,

            learnerState:
                this.flow.learnerState,

            hasEvidence:
                this.flow.hasEvidence,

            flow:
                structuredClone(
                    this.flow
                ),

            progress:
                structuredClone(
                    this.progress
                ),

            mastery:
                structuredClone(
                    this.mastery
                ),

            recommendation:
                structuredClone(
                    this.recommendation
                ),

            dashboard:
                buildDashboardState(
                    this.flow
                )
        };
    }


    /* ========================================================
       DASHBOARD
       ======================================================== */

    /* ========================================================
       READINESS
       ======================================================== */

    getReadiness(
        targetSkillId,
        learnerEvidence = null
    ) {

        const evidence =
            this.resolveReadinessEvidence(
                learnerEvidence
            );


        return this.readinessAdapter.resolve(
            targetSkillId,
            evidence
        );
    }


    getInterventionPlan(
        targetSkillId,
        learnerEvidence = null
    ) {

        const evidence =
            this.resolveReadinessEvidence(
                learnerEvidence
            );


        return this.readinessAdapter.plan(
            targetSkillId,
            evidence
        );
    }


    getLearningReadinessState(
        targetSkillId,
        learnerEvidence = null
    ) {

        const evidence =
            this.resolveReadinessEvidence(
                learnerEvidence
            );


        return this.readinessAdapter.getState(
            targetSkillId,
            evidence
        );
    }


    explainReadiness(
        targetSkillId,
        learnerEvidence = null
    ) {

        const evidence =
            this.resolveReadinessEvidence(
                learnerEvidence
            );


        return this.readinessAdapter.explain(
            targetSkillId,
            evidence
        );
    }


    resolveReadinessEvidence(
        learnerEvidence = null
    ) {

        /*
         * Explicit evidence remains supported.
         *
         * This is useful for diagnostics/tests and prevents
         * breaking the existing API contract.
         */

        if (
            learnerEvidence !== null &&
            learnerEvidence !== undefined
        ) {

            return learnerEvidence;
        }


        /*
         * Otherwise derive evidence directly from the
         * application's current learner state.
         */

        return this.readinessEvidenceAdapter
            .fromApplicationState({

                progress:
                    this.progress,

                mastery:
                    this.mastery
            });
    }
    /* ========================================================
       ADAPTIVE LEARNING
       ======================================================== */

    getAdaptiveRemediationOrchestrator() {

        if (
            !this.adaptiveRemediationOrchestrator
        ) {

            const application =
                this;


            const applicationLearningBridge = {

                async recordQuestion(
                    attempt
                ) {

                    return await application
                        .recordLearningResult(
                            attempt
                        );
                }
            };


            this.adaptiveRemediationOrchestrator =
                new ReadinessRemediationOrchestrator({

                    readinessProvider:
                        this,

                    learningPipeline:
                        applicationLearningBridge,

                    studentId:
                        this.flow?.studentId ??
                        "local"
                });
        }


        return this.adaptiveRemediationOrchestrator;
    }


    async startAdaptiveTarget(
    targetSkillId
) {

    if (
        typeof targetSkillId !==
        "string" ||
        targetSkillId.trim().length ===
        0
    ) {

        throw new Error(
            "Adaptive target skill ID is required."
        );
    }


    const normalizedTarget =
        targetSkillId.trim();


    /*
     * IMPORTANT:
     *
     * Use the application's REAL readiness adapter contract.
     *
     * Existing application inspection shows:
     *
     *     readinessAdapter.resolve(...)
     *     readinessAdapter.plan(...)
     *     readinessAdapter.getState(...)
     *     readinessAdapter.explain(...)
     *
     * Do not invent a second target-resolution API.
     */

    const resolution =
        await this.readinessAdapter.resolve(
            normalizedTarget
        );


    /*
     * Unknown target protection.
     *
     * Accept all legitimate non-null resolution objects.
     * Reject only explicit unresolved/error states.
     */

    if (
        resolution === null ||
        resolution === false ||
        resolution?.found === false ||
        resolution?.resolved === false ||
        resolution?.valid === false ||
        resolution?.unknown === true
    ) {

        throw new Error(
            `Unknown readiness target: ${normalizedTarget}`
        );
    }


    /*
     * Some resolution implementations return:
     *
     *   { target: ... }
     *   { targetSkillId: ... }
     *   { id: ... }
     *
     * They are all valid as long as the resolution object
     * exists and did not explicitly report failure.
     */


    /*
     * Only mutate the remediation state AFTER successful
     * readiness-target resolution.
     */

    const orchestrator =
        this.getAdaptiveRemediationOrchestrator();


    if (
        !orchestrator ||
        typeof orchestrator.selectTarget !==
        "function"
    ) {

        throw new Error(
            "Adaptive remediation orchestrator target-selection API is unavailable."
        );
    }


    await orchestrator.selectTarget(
        normalizedTarget
    );


    /*
     * Return the normal live readiness state through the
     * existing application adapter.
     */

    return await this.checkAdaptiveReadiness();
}

getAdaptiveState() {

        return this
            .getAdaptiveRemediationOrchestrator()
            .snapshot();
    }


    async checkAdaptiveReadiness() {

        return await this
            .getAdaptiveRemediationOrchestrator()
            .checkReadiness();
    }


    async prepareAdaptiveDiagnostic(
        options = {}
    ) {

        const orchestrator =
            this.getAdaptiveRemediationOrchestrator();


        if (
            !orchestrator.flow.targetSkillId
        ) {

            throw new Error(
                "No adaptive target selected."
            );
        }


        const readinessState =
            await orchestrator.getCurrentReadiness();


        if (
            readinessState?.readiness?.ready === true
        ) {

            return {

                available:
                    false,

                reason:
                    "learner-ready",

                readinessState,

                state:
                    orchestrator.snapshot()
            };
        }


        const interventionPlan =
            readinessState?.interventionPlan ||
            null;


        if (
            !interventionPlan
        ) {

            throw new Error(
                "Learner is not ready, but no intervention plan is available."
            );
        }


        if (
            !orchestrator.flow
                .getCurrentIntervention()
        ) {

            orchestrator.flow
                .applyInterventionPlan(
                    interventionPlan
                );
        }


        const intervention =
            orchestrator.flow
                .getCurrentIntervention();


        if (
            !intervention
        ) {

            throw new Error(
                "Intervention plan contains no usable intervention block."
            );
        }


        const diagnostic =
            orchestrator.prepareDiagnostic(
                intervention,
                options
            );


        /*
         * Coverage unavailable is surfaced to the caller.
         * Nothing is marked as mastered and no progress is written.
         */

        if (
            diagnostic.available === false
        ) {

            return {

                ...diagnostic,

                readinessState,

                state:
                    orchestrator.snapshot()
            };
        }


        return {

            ...diagnostic,

            readinessState
        };
    }

    async submitAdaptiveAnswer({
        question,
        result,
        timeSpentSeconds = 0,
        attemptedAt = null
    } = {}) {

        return await this
            .getAdaptiveRemediationOrchestrator()
            .recordDiagnosticAnswer({

                question,

                result,

                timeSpentSeconds,

                attemptedAt
            });
    }


    async completeAdaptiveDiagnostic(
        results
    ) {

        return await this
            .getAdaptiveRemediationOrchestrator()
            .completeDiagnostic(
                results
            );
    }


    async continueAdaptiveLearning() {

        return await this
            .getAdaptiveRemediationOrchestrator()
            .checkReadiness();
    }


    resetAdaptiveLearning() {

        if (
            !this.adaptiveRemediationOrchestrator
        ) {

            return {

                state:
                    null,

                targetSkillId:
                    null,

                history: []
            };
        }


        return this
            .adaptiveRemediationOrchestrator
            .flow
            .reset();
    }

    getDashboard() {

        if (
            !this.flow
        ) {

            return null;
        }


        return buildDashboardState(
            this.flow
        );
    }


    /* ========================================================
       CURRENT TOPIC
       ======================================================== */

    getCurrentTopic() {

        return (
            this.flow
                ?.learning
                ?.currentTopic ||
            null
        );
    }


    /* ========================================================
       NEXT TOPIC
       ======================================================== */

    getNextTopic() {

        return (
            this.flow
                ?.learning
                ?.nextTopic ||
            null
        );
    }


    /* ========================================================
       LEARNER STATE
       ======================================================== */

    getLearnerState() {

        return (
            this.flow
                ?.learnerState ||
            null
        );
    }


    /* ========================================================
       SESSION EXISTS
       ======================================================== */

    hasSession() {

        return this.sessionRepository.exists();
    }


    /* ========================================================
       LOGOUT / CLEAR SESSION
       ======================================================== */

    clearSession() {

        this.sessionRepository.clear();


        this.flow =
            null;

        this.progress =
            null;

        this.mastery =
            null;

        this.recommendation =
            null;
    }
}


export default
    MathsMasteryApplication;







