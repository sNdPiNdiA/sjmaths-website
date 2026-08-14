/**
 * SJMaths Maths Mastery
 *
 * STEP 32.47
 *
 * Readiness Question Generator Contract
 *
 * This module validates and normalizes generated readiness
 * questions.
 *
 * It does NOT call an LLM and does NOT generate text itself.
 *
 * A future content-generation script/API can use this contract
 * before questions enter the production question bank.
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


function clone(
    value
) {

    return JSON.parse(
        JSON.stringify(
            value
        )
    );
}


export class ReadinessQuestionGenerator {

    constructor(
        options = {}
    ) {

        this.minimumPoolSize =
            Number(
                options.minimumPoolSize ??
                10
            );


        this.recommendedPoolSize =
            Number(
                options.recommendedPoolSize ??
                15
            );


        this.diagnosticSelectionCount =
            Number(
                options.diagnosticSelectionCount ??
                5
            );


        this.passScore =
            Number(
                options.passScore ??
                80
            );
    }


    normalizeQuestion(
        question
    ) {

        if (
            !isObject(
                question
            )
        ) {

            throw new Error(
                "Readiness question must be an object."
            );
        }


        const normalized = {

            ...question,

            skillIds:
                safeArray(
                    question.skillIds
                )
        };


        if (
            typeof normalized.readinessSkillId !==
            "string"
        ) {

            throw new Error(
                "readinessSkillId is required."
            );
        }


        if (
            !normalized.skillIds.includes(
                normalized.readinessSkillId
            )
        ) {

            throw new Error(
                "readinessSkillId must be present in skillIds."
            );
        }


        return normalized;
    }


    validateQuestion(
        question
    ) {

        const errors =
            [];


        if (
            !isObject(
                question
            )
        ) {

            errors.push(
                "Question must be an object."
            );


            return {

                valid:
                    false,

                errors
            };
        }


        const requiredFields = [
            "id",
            "questionType",
            "topicId",
            "conceptId",
            "skillIds",
            "readinessSkillId",
            "role",
            "difficulty"
        ];


        for (
            const field
            of requiredFields
        ) {

            if (
                question[field] ===
                    undefined ||
                question[field] ===
                    null
            ) {

                errors.push(
                    `${field} is required.`
                );
            }
        }


        if (
            typeof question.id !==
            "string"
        ) {

            errors.push(
                "id must be a string."
            );
        }


        if (
            !Array.isArray(
                question.skillIds
            )
        ) {

            errors.push(
                "skillIds must be an array."
            );
        }


        if (
            typeof question.readinessSkillId !==
            "string"
        ) {

            errors.push(
                "readinessSkillId must be a string."
            );
        }


        if (
            Array.isArray(
                question.skillIds
            ) &&
            typeof question.readinessSkillId ===
                "string" &&
            !question.skillIds.includes(
                question.readinessSkillId
            )
        ) {

            errors.push(
                "readinessSkillId must be contained in skillIds."
            );
        }


        const validRoles = [
            "diagnostic",
            "remediation",
            "mixed"
        ];


        if (
            !validRoles.includes(
                question.role
            )
        ) {

            errors.push(
                "Invalid question role."
            );
        }


        const validDifficulties = [
            "basic",
            "standard",
            "intermediate",
            "advanced"
        ];


        if (
            !validDifficulties.includes(
                question.difficulty
            )
        ) {

            errors.push(
                "Invalid question difficulty."
            );
        }


        return {

            valid:
                errors.length ===
                0,

            errors
        };
    }


    validateExactSkill(
        question,
        readinessSkillId
    ) {

        if (
            !question ||
            typeof readinessSkillId !==
            "string"
        ) {

            return false;
        }


        return (
            question.readinessSkillId ===
                readinessSkillId &&
            Array.isArray(
                question.skillIds
            ) &&
            question.skillIds.includes(
                readinessSkillId
            )
        );
    }


    validatePool(
        questions,
        readinessSkillId
    ) {

        const list =
            safeArray(
                questions
            );


        const errors =
            [];


        const ids =
            new Set();


        let exactSkillCount =
            0;

        let diagnosticCount =
            0;

        let remediationCount =
            0;


        const difficultyCounts = {

            basic:
                0,

            standard:
                0,

            intermediate:
                0,

            advanced:
                0
        };


        for (
            const question
            of list
        ) {

            const validation =
                this.validateQuestion(
                    question
                );


            if (
                !validation.valid
            ) {

                errors.push(
                    ...validation.errors.map(
                        error =>
                            `${question?.id ?? "unknown"}: ${error}`
                    )
                );


                continue;
            }


            if (
                ids.has(
                    question.id
                )
            ) {

                errors.push(
                    `Duplicate question ID: ${question.id}`
                );

            }
            else {

                ids.add(
                    question.id
                );
            }


            if (
                this.validateExactSkill(
                    question,
                    readinessSkillId
                )
            ) {

                exactSkillCount +=
                    1;

            }
            else {

                errors.push(
                    `${question.id}: exact readiness skill mismatch`
                );
            }


            if (
                question.role ===
                "diagnostic" ||
                question.role ===
                "mixed"
            ) {

                diagnosticCount +=
                    1;
            }


            if (
                question.role ===
                "remediation" ||
                question.role ===
                "mixed"
            ) {

                remediationCount +=
                    1;
            }


            if (
                difficultyCounts[
                    question.difficulty
                ] !==
                undefined
            ) {

                difficultyCounts[
                    question.difficulty
                ] +=
                    1;
            }
        }


        if (
            exactSkillCount <
            this.minimumPoolSize
        ) {

            errors.push(
                `Pool contains only ${exactSkillCount} exact-skill questions; minimum is ${this.minimumPoolSize}.`
            );
        }


        if (
            diagnosticCount ===
            0
        ) {

            errors.push(
                "Pool contains no diagnostic questions."
            );
        }


        return {

            valid:
                errors.length ===
                0,

            errors,

            readinessSkillId,

            totalQuestions:
                list.length,

            exactSkillCount,

            diagnosticCount,

            remediationCount,

            difficultyCounts,

            recommendedPoolSize:
                this.recommendedPoolSize,

            diagnosticSelectionCount:
                this.diagnosticSelectionCount
        };
    }


    buildSpecification(
        readinessSkill,
        options = {}
    ) {

        if (
            !isObject(
                readinessSkill
            )
        ) {

            throw new Error(
                "readinessSkill is required."
            );
        }


        const skillId =
            readinessSkill.id;


        return {

            readinessSkillId:
                skillId,

            name:
                readinessSkill.name ??
                null,

            rolePlan: {

                diagnostic:
                    Number(
                        options.diagnosticCount ??
                        this.diagnosticSelectionCount
                    ),

                remediation:
                    Number(
                        options.remediationCount ??
                        this.recommendedPoolSize
                    )
            },

            difficultyPlan: {

                basic:
                    Number(
                        options.basicCount ??
                        3
                    ),

                standard:
                    Number(
                        options.standardCount ??
                        3
                    ),

                intermediate:
                    Number(
                        options.intermediateCount ??
                        2
                    ),

                advanced:
                    Number(
                        options.advancedCount ??
                        0
                    )
            },

            exactSkillRequired:
                true,

            requiredFields: [
                "id",
                "questionType",
                "topicId",
                "conceptId",
                "skillIds",
                "readinessSkillId",
                "role",
                "difficulty",
                "questionText",
                "correctAnswer",
                "explanation"
            ]
        };
    }


    createCoverageRecord(
        readinessSkillId,
        questions
    ) {

        const list =
            safeArray(
                questions
            );


        const validQuestions =
            list.filter(
                question =>
                    this.validateQuestion(
                        question
                    ).valid &&
                    this.validateExactSkill(
                        question,
                        readinessSkillId
                    )
            );


        return {

            readinessSkillId,

            questionCount:
                validQuestions.length,

            requiredQuestionCount:
                this.minimumPoolSize,

            missing:
                Math.max(
                    0,
                    this.minimumPoolSize -
                    validQuestions.length
                ),

            status:
                validQuestions.length ===
                    0
                    ? "CRITICAL"
                    : validQuestions.length <
                        this.minimumPoolSize
                        ? "HIGH"
                        : "READY"
        };
    }
}


export function createReadinessQuestionGenerator(
    options = {}
) {

    return new ReadinessQuestionGenerator(
        options
    );
}
