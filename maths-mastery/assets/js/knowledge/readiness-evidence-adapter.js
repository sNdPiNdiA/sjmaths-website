/**
 * SJMaths Maths Mastery
 *
 * STEP 32.38B
 *
 * Robust Readiness Evidence Adapter
 *
 * Converts existing learner progress / mastery structures
 * into readiness-skill evidence.
 *
 * READ-ONLY.
 */


function isObject(
    value
) {

    return (
        value !== null &&
        typeof value === "object" &&
        !Array.isArray(value)
    );
}


function safeArray(
    value
) {

    return Array.isArray(
        value
    )
        ? value
        : [];
}


function toNumber(
    value,
    fallback = 0
) {

    if (
        value === null ||
        value === undefined ||
        value === ""
    ) {

        return fallback;
    }


    const number =
        Number(
            value
        );


    return Number.isFinite(
        number
    )
        ? number
        : fallback;
}


export class ReadinessEvidenceAdapter {

    constructor(
        options = {}
    ) {

        this.masteryThreshold =
            toNumber(
                options.masteryThreshold,
                80
            );


        this.minimumAttempts =
            Math.max(
                0,
                toNumber(
                    options.minimumAttempts,
                    1
                )
            );
    }


    normalizeSkillEvidence(
        evidence = {}
    ) {

        if (
            !isObject(
                evidence
            )
        ) {

            return {

                mastered:
                    false,

                score:
                    0,

                attempts:
                    0,

                correct:
                    0,

                incorrect:
                    0,

                skipped:
                    0,

                lastAttemptAt:
                    null
            };
        }


        const correct =
            toNumber(
                evidence.correct,
                0
            );


        const incorrect =
            toNumber(
                evidence.incorrect,
                0
            );


        const skipped =
            toNumber(
                evidence.skipped,
                0
            );


        const suppliedAttempts =
            toNumber(
                evidence.attempts,
                -1
            );


        const attempts =
            suppliedAttempts >= 0
                ? suppliedAttempts
                : (
                    correct +
                    incorrect +
                    skipped
                );


        const score =
            toNumber(
                evidence.score ??
                evidence.mastery ??
                evidence.lastScore ??
                evidence.bestScore ??
                evidence.accuracy,
                0
            );


        const mastered =
            evidence.mastered === true ||
            (
                score >=
                this.masteryThreshold
                &&
                attempts >=
                this.minimumAttempts
            );


        return {

            mastered,

            score,

            attempts,

            correct,

            incorrect,

            skipped,

            lastAttemptAt:
                evidence.lastAttemptAt ??
                evidence.attemptedAt ??
                null
        };
    }


    mergeEvidence(
        result,
        skillId,
        evidence
    ) {

        if (
            typeof skillId !== "string" ||
            skillId.length === 0
        ) {

            return;
        }


        const normalized =
            this.normalizeSkillEvidence(
                evidence
            );


        if (
            !result[skillId]
        ) {

            result[skillId] =
                normalized;

            return;
        }


        const current =
            result[skillId];


        current.score =
            Math.max(
                current.score,
                normalized.score
            );


        current.attempts +=
            normalized.attempts;


        current.correct +=
            normalized.correct;


        current.incorrect +=
            normalized.incorrect;


        current.skipped +=
            normalized.skipped;


        current.mastered =
            current.mastered ||
            normalized.mastered;


        if (
            normalized.lastAttemptAt
        ) {

            current.lastAttemptAt =
                normalized.lastAttemptAt;
        }
    }


    mergeRecord(
        result,
        record
    ) {

        if (
            !isObject(
                record
            )
        ) {

            return;
        }


        const sharedEvidence = {

            score:
                record.score ??
                record.mastery ??
                record.lastScore ??
                record.bestScore ??
                record.accuracy ??
                0,

            correct:
                record.correct ??
                0,

            incorrect:
                record.incorrect ??
                0,

            skipped:
                record.skipped ??
                0,

            attempts:
                record.attempts,

            mastered:
                record.mastered === true,

            lastAttemptAt:
                record.lastAttemptAt ??
                record.attemptedAt ??
                record.timestamp ??
                null
        };


        /*
         * Single skillId
         */

        const directSkillId =
            record.skillId;


        if (
            typeof directSkillId ===
            "string" &&
            directSkillId.length > 0
        ) {

            this.mergeEvidence(
                result,
                directSkillId,
                sharedEvidence
            );
        }


        /*
         * Multiple skillIds
         */

        for (
            const skillId
            of safeArray(
                record.skillIds
            )
        ) {

            if (
                typeof skillId ===
                "string" &&
                skillId.length > 0
            ) {

                this.mergeEvidence(
                    result,
                    skillId,
                    sharedEvidence
                );
            }
        }
    }


    mergeObjectMap(
        result,
        objectMap
    ) {

        if (
            !isObject(
                objectMap
            )
        ) {

            return;
        }


        for (
            const [
                skillId,
                evidence
            ]
            of Object.entries(
                objectMap
            )
        ) {

            if (
                isObject(
                    evidence
                )
            ) {

                this.mergeEvidence(
                    result,
                    skillId,
                    evidence
                );
            }
        }
    }


    processRecordCollection(
        result,
        collection
    ) {

        for (
            const record
            of safeArray(
                collection
            )
        ) {

            this.mergeRecord(
                result,
                record
            );
        }
    }


    extractSkillEvidence(
        progress
    ) {

        const result =
            {};


        if (
            !isObject(
                progress
            )
        ) {

            return result;
        }


        /*
         * ----------------------------------------------------
         * 1. Direct skill maps
         * ----------------------------------------------------
         */

        this.mergeObjectMap(
            result,
            progress.skills
        );


        this.mergeObjectMap(
            result,
            progress.skillProgress
        );


        this.mergeObjectMap(
            result,
            progress.evidence
        );


        /*
         * ----------------------------------------------------
         * 2. Direct record collections
         * ----------------------------------------------------
         */

        this.processRecordCollection(
            result,
            progress.records
        );


        this.processRecordCollection(
            result,
            progress.questionResults
        );


        /*
         * ----------------------------------------------------
         * 3. Nested learning records
         * ----------------------------------------------------
         */

        if (
            isObject(
                progress.learning
            )
        ) {

            this.mergeObjectMap(
                result,
                progress.learning.skills
            );


            this.mergeObjectMap(
                result,
                progress.learning.skillProgress
            );


            this.mergeObjectMap(
                result,
                progress.learning.evidence
            );


            this.processRecordCollection(
                result,
                progress.learning.records
            );


            this.processRecordCollection(
                result,
                progress.learning.questionResults
            );
        }


        /*
         * ----------------------------------------------------
         * 4. Nested progress.records inside state containers
         * ----------------------------------------------------
         */

        if (
            isObject(
                progress.progress
            )
        ) {

            const nested =
                this.extractSkillEvidence(
                    progress.progress
                );


            for (
                const [
                    skillId,
                    evidence
                ]
                of Object.entries(
                    nested
                )
            ) {

                this.mergeEvidence(
                    result,
                    skillId,
                    evidence
                );
            }
        }


        return result;
    }


    fromApplicationState(
        applicationState
    ) {

        if (
            !isObject(
                applicationState
            )
        ) {

            return {};
        }


        /*
         * Explicit mastery takes precedence.
         */

        if (
            isObject(
                applicationState.mastery
            )
        ) {

            const masteryEvidence =
                this.extractSkillEvidence(
                    applicationState.mastery
                );


            if (
                Object.keys(
                    masteryEvidence
                ).length > 0
            ) {

                return masteryEvidence;
            }
        }


        /*
         * Existing learner progress becomes fallback.
         */

        return this.extractSkillEvidence(
            applicationState.progress
        );
    }


    buildTargetEvidence(
        targetSkillId,
        applicationState,
        readinessTarget
    ) {

        const allEvidence =
            this.fromApplicationState(
                applicationState
            );


        const requirements =
            safeArray(
                readinessTarget?.readiness
            );


        const result =
            {};


        for (
            const requirement
            of requirements
        ) {

            const skillId =
                requirement.skillId;


            if (
                allEvidence[skillId]
            ) {

                result[skillId] =
                    allEvidence[skillId];
            }
            else {

                result[skillId] = {

                    mastered:
                        false,

                    score:
                        0,

                    attempts:
                        0,

                    correct:
                        0,

                    incorrect:
                        0,

                    skipped:
                        0,

                    lastAttemptAt:
                        null
                };
            }
        }


        return {

            targetSkillId,

            evidence:
                result
        };
    }
}
