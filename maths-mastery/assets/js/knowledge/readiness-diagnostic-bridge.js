/**
 * SJMaths Maths Mastery
 *
 * STEP 32.43
 *
 * Readiness Diagnostic Bridge
 *
 * Thin orchestration layer connecting:
 *
 *   Readiness intervention
 *          ↓
 *   Existing question-selection-engine
 *          ↓
 *   Existing learning-pipeline
 *
 * This component does NOT implement question selection,
 * progress calculation, mastery, or recommendation algorithms.
 */


import {
    selectQuestions,
    selectNextQuestion
} from "./question-selection-engine.js";


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


export class ReadinessDiagnosticBridge {

    constructor(
        options = {}
    ) {

        this.questionSelector =
            options.questionSelector || {

                selectQuestions,

                selectNextQuestion
            };


        this.defaultQuestionCount =
            Number(
                options.questionCount ??
                5
            );


        this.defaultMasteryStatus =
            options.masteryStatus ||
            "learning";
    }


    buildSelectionContext(
        intervention,
        options = {}
    ) {

        if (
            !intervention ||
            typeof intervention !==
            "object"
        ) {

            throw new Error(
                "intervention is required."
            );
        }


        const skillId =
            intervention.skillId;


        if (
            typeof skillId !==
            "string" ||
            skillId.length === 0
        ) {

            throw new Error(
                "intervention.skillId is required."
            );
        }


        return {

            currentTopicId:
                options.currentTopicId ??
                null,

            examId:
                options.examId ??
                null,

            weakSkills: [

                {

                    skillId,

                    score:
                        Number(
                            options.currentScore ??
                            0
                        )
                }

            ],

            masteryStatus:
                options.masteryStatus ??
                this.defaultMasteryStatus,

            attemptedQuestionIds:
                safeArray(
                    options.attemptedQuestionIds
                ).slice()
        };
    }


    selectDiagnosticQuestions(
        intervention,
        options = {}
    ) {

        if (
            !intervention ||
            typeof intervention !==
            "object"
        ) {

            throw new Error(
                "intervention is required."
            );
        }


        const skillId =
            intervention.skillId;


        if (
            typeof skillId !==
            "string" ||
            skillId.length === 0
        ) {

            throw new Error(
                "intervention.skillId is required."
            );
        }


        const desiredCount =
            Math.max(
                1,
                Number(
                    options.questionCount ??
                    this.defaultQuestionCount
                )
            );


        /*
         * ----------------------------------------------------
         * Stage 1
         *
         * Use the caller's full selector context.
         * ----------------------------------------------------
         */

        const primaryContext =
            this.buildSelectionContext(
                intervention,
                options
            );


        const primaryLimit =
            Math.max(
                desiredCount * 3,
                15
            );


        const primaryCandidates =
            this.questionSelector.selectQuestions(
                primaryContext,
                {
                    limit:
                        primaryLimit
                }
            );


        const matchingPrimary =
            this.filterMatchingCandidates(
                primaryCandidates,
                skillId
            );


        /*
         * ----------------------------------------------------
         * Stage 2
         *
         * Widen constraints.
         *
         * Keep the skill requirement.
         * Remove topic/exam restrictions.
         * ----------------------------------------------------
         */

        if (
            matchingPrimary.length >=
            desiredCount
        ) {

            const selected =
                matchingPrimary.slice(
                    0,
                    desiredCount
                );


            return {

                interventionSkillId:
                    skillId,

                questionCount:
                    selected.length,

                questions:
                    clone(
                        selected
                    ),

                selectionContext:
                    clone(
                        primaryContext
                    ),

                coverage:
                    "primary"
            };
        }


        const widenedContext = {

            currentTopicId:
                null,

            examId:
                null,

            weakSkills: [

                {

                    skillId,

                    score:
                        Number(
                            options.currentScore ??
                            0
                        )
                }

            ],

            masteryStatus:
                options.masteryStatus ??
                this.defaultMasteryStatus,

            attemptedQuestionIds:
                safeArray(
                    options.attemptedQuestionIds
                ).slice()
        };


        const widenedLimit =
            Math.max(
                desiredCount * 6,
                30
            );


        const widenedCandidates =
            this.questionSelector.selectQuestions(
                widenedContext,
                {
                    limit:
                        widenedLimit
                }
            );


        const matchingWidened =
            this.filterMatchingCandidates(
                widenedCandidates,
                skillId
            );


        /*
         * Avoid duplicates by question ID.
         */

        const combined =
            this.mergeUniqueCandidates(
                matchingPrimary,
                matchingWidened
            );


        if (
            combined.length <
            desiredCount
        ) {

            return {

                interventionSkillId:
                    skillId,

                questionCount:
                    combined.length,

                questions:
                    clone(
                        combined
                    ),

                selectionContext:
                    clone(
                        primaryContext
                    ),

                coverage:
                    "insufficient",

                requiredCount:
                    desiredCount,

                availableCount:
                    combined.length,

                insufficientCoverage:
                    true,

                reason:
                    "Not enough questions explicitly mapped to the intervention skill."
            };
        }


        const selected =
            combined.slice(
                0,
                desiredCount
            );


        return {

            interventionSkillId:
                skillId,

            questionCount:
                selected.length,

            questions:
                clone(
                    selected
                ),

            selectionContext:
                clone(
                    primaryContext
                ),

            coverage:
                "widened",

            insufficientCoverage:
                false
        };
    }


    filterMatchingCandidates(
        candidates,
        skillId
    ) {

        return safeArray(
            candidates
        ).filter(
            candidate => {

                const question =
                    candidate &&
                    candidate.question
                        ? candidate.question
                        : candidate;


                if (
                    !question ||
                    typeof question !==
                    "object"
                ) {

                    return false;
                }


                const skillIds =
                    Array.isArray(
                        question.skillIds
                    )
                        ? question.skillIds
                        : [];


                return skillIds.includes(
                    skillId
                );
            }
        );
    }


    mergeUniqueCandidates(
        first,
        second
    ) {

        const output =
            [];


        const seen =
            new Set();


        for (
            const candidate
            of [
                ...safeArray(
                    first
                ),
                ...safeArray(
                    second
                )
            ]
        ) {

            const question =
                candidate &&
                candidate.question
                    ? candidate.question
                    : candidate;


            const id =
                question?.id ??
                null;


            if (
                !id ||
                seen.has(
                    id
                )
            ) {

                continue;
            }


            seen.add(
                id
            );


            output.push(
                candidate
            );
        }


        return output;
    }

    selectNextDiagnosticQuestion(
        intervention,
        options = {}
    ) {

        const context =
            this.buildSelectionContext(
                intervention,
                options
            );


        const result =
            this.questionSelector
                .selectNextQuestion(
                    context
                );


        if (
            !result
        ) {

            return null;
        }


        return {

            interventionSkillId:
                intervention.skillId,

            question:
                clone(
                    result.question
                ),

            score:
                result.score ??
                null,

            reasons:
                safeArray(
                    result.reasons
                )
        };
    }


    normalizeQuestionCandidate(
        candidate
    ) {

        if (
            candidate &&
            candidate.question
        ) {

            return candidate.question;
        }


        return candidate;
    }


    getQuestionFromCandidate(
        candidate
    ) {

        return this.normalizeQuestionCandidate(
            candidate
        );
    }

    validateDiagnosticSet(
        diagnosticSet
    ) {

        if (
            !diagnosticSet ||
            !Array.isArray(
                diagnosticSet.questions
            )
        ) {

            return {

                valid:
                    false,

                reason:
                    "Diagnostic set is missing questions."
            };
        }


        if (
            diagnosticSet.questions.length ===
            0
        ) {

            return {

                valid:
                    false,

                reason:
                    diagnosticSet.reason ||
                    "No diagnostic questions available."
            };
        }


        const skillId =
            diagnosticSet.interventionSkillId;


        if (
            typeof skillId !==
            "string" ||
            skillId.length === 0
        ) {

            return {

                valid:
                    false,

                reason:
                    "Diagnostic intervention skill is missing."
            };
        }


        const invalid =
            [];


        for (
            const candidate
            of diagnosticSet.questions
        ) {

            const question =
                candidate &&
                candidate.question
                    ? candidate.question
                    : candidate;


            const skillIds =
                Array.isArray(
                    question?.skillIds
                )
                    ? question.skillIds
                    : [];


            if (
                !skillIds.includes(
                    skillId
                )
            ) {

                invalid.push(
                    question?.id ??
                    null
                );
            }
        }


        if (
            invalid.length > 0
        ) {

            return {

                valid:
                    false,

                reason:
                    "One or more selected questions do not target the intervention skill.",

                invalidQuestionIds:
                    invalid
            };
        }


        return {

            valid:
                true,

            reason:
                null,

            coverage:
                diagnosticSet.coverage ||
                "verified"
        };
    }

    evaluateDiagnosticResults(
        results,
        options = {}
    ) {

        const items =
            safeArray(
                results
            );


        if (
            items.length === 0
        ) {

            return {

                attempted:
                    0,

                correct:
                    0,

                incorrect:
                    0,

                skipped:
                    0,

                score:
                    0,

                passed:
                    false,

                reason:
                    "No diagnostic results."
            };
        }


        let correct =
            0;

        let incorrect =
            0;

        let skipped =
            0;


        for (
            const item
            of items
        ) {

            if (
                item.result ===
                "correct"
            ) {

                correct += 1;

            }
            else if (
                item.result ===
                "incorrect"
            ) {

                incorrect += 1;

            }
            else {

                skipped += 1;
            }
        }


        const attempted =
            correct +
            incorrect;


        const score =
            attempted >
            0
                ? (
                    correct /
                    attempted
                ) *
                100
                : 0;


        const threshold =
            Number(
                options.passScore ??
                80
            );


        const minimumCorrect =
            Number(
                options.minimumCorrect ??
                1
            );


        const passed =
            attempted >
            0 &&
            correct >=
            minimumCorrect &&
            score >=
            threshold;


        return {

            attempted,

            correct,

            incorrect,

            skipped,

            score,

            passed,

            threshold,

            minimumCorrect
        };
    }


    buildProgressAttempt(
        question,
        result,
        options = {}
    ) {

        if (
            !question ||
            typeof question !==
            "object"
        ) {

            throw new Error(
                "question is required."
            );
        }


        if (
            ![
                "correct",
                "incorrect",
                "skipped"
            ].includes(
                result
            )
        ) {

            throw new Error(
                `Invalid diagnostic result: ${result}`
            );
        }


        return {

            studentId:
                options.studentId ??
                "local",

            topicId:
                question.topicId,

            questionId:
                question.id,

            conceptId:
                question.conceptId ??
                null,

            skillIds:
                safeArray(
                    question.skillIds
                ).slice(),

            correct:
                result ===
                "correct"
                    ? true
                    : result ===
                        "incorrect"
                        ? false
                        : null,

            timeSpentSeconds:
                Number(
                    options.timeSpentSeconds ??
                    0
                ),

            attemptedAt:
                options.attemptedAt ??
                null
        };
    }


    async recordDiagnosticResult({
        learningPipeline,
        question,
        result,
        studentId = "local",
        timeSpentSeconds = 0,
        attemptedAt = null
    } = {}) {

        if (
            !learningPipeline
        ) {

            throw new Error(
                "learningPipeline is required."
            );
        }


        const attempt =
            this.buildProgressAttempt(
                question,
                result,
                {
                    studentId,
                    timeSpentSeconds,
                    attemptedAt
                }
            );


        /*
         * Delegate mutation completely to the existing
         * learning pipeline.
         */

        return await learningPipeline.recordQuestion(
            attempt
        );
    }
}


/**
 * Convenience factory.
 */
export function createReadinessDiagnosticBridge(
    options = {}
) {

    return new ReadinessDiagnosticBridge(
        options
    );
}


