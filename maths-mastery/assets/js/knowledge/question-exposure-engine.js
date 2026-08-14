import fs from "fs";
import path from "path";


const ROOT =
    path.resolve(
        process.cwd(),
        "maths-mastery"
    );


const RULES_PATH =
    path.join(
        ROOT,
        "data",
        "config",
        "question-exposure-rules.json"
    );


function readJson(
    file
) {

    const raw =
        fs.readFileSync(
            file,
            "utf8"
        );


    return JSON.parse(
        raw.replace(
            /^\uFEFF/,
            ""
        )
    );
}


const rules =
    readJson(
        RULES_PATH
    );


const VALID_RESULTS =
    new Set(
        rules.exposure.results
    );


function createEmptyExposure(
    studentId
) {

    if (
        typeof studentId !==
        "string" ||
        studentId.trim() === ""
    ) {

        throw new Error(
            "studentId is required"
        );
    }


    return {

        version:
            rules.version,

        studentId,

        updatedAt:
            new Date().toISOString(),

        questions: {}

    };
}


function validateResult(
    result
) {

    if (
        !VALID_RESULTS.has(
            result
        )
    ) {

        throw new Error(
            `Invalid question result: ${result}`
        );
    }

}


function validateQuestionId(
    questionId
) {

    if (
        typeof questionId !==
        "string" ||
        questionId.trim() === ""
    ) {

        throw new Error(
            "questionId is required"
        );
    }

}


function validateTime(
    timeSpentSeconds
) {

    if (
        timeSpentSeconds ===
        undefined
    ) {

        return 0;
    }


    if (
        typeof timeSpentSeconds !==
        "number" ||
        !Number.isFinite(
            timeSpentSeconds
        ) ||
        timeSpentSeconds < 0
    ) {

        throw new Error(
            "timeSpentSeconds must be a non-negative number"
        );
    }


    return timeSpentSeconds;
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


function recordQuestionAttempt(
    exposure,
    input
) {

    if (
        !exposure ||
        typeof exposure !==
        "object"
    ) {

        throw new Error(
            "Valid exposure state is required"
        );
    }


    validateQuestionId(
        input?.questionId
    );


    validateResult(
        input?.result
    );


    const timeSpentSeconds =
        validateTime(
            input?.timeSpentSeconds
        );


    const questionId =
        input.questionId;


    const now =
        input.attemptedAt ||
        new Date().toISOString();


    const previous =
        exposure.questions?.[
            questionId
        ];


    const existing =
        previous
            ? clone(previous)
            : {

                questionId,

                attemptCount: 0,

                correctCount: 0,

                incorrectCount: 0,

                skippedCount: 0,

                totalTimeSpentSeconds: 0,

                lastResult: null,

                firstAttemptedAt: null,

                lastAttemptedAt: null,

                consecutiveCorrect: 0,

                consecutiveIncorrect: 0

            };


    existing.attemptCount += 1;


    if (
        input.result ===
        "correct"
    ) {

        existing.correctCount += 1;

        existing.consecutiveCorrect += 1;

        existing.consecutiveIncorrect = 0;

    }


    if (
        input.result ===
        "incorrect"
    ) {

        existing.incorrectCount += 1;

        existing.consecutiveIncorrect += 1;

        existing.consecutiveCorrect = 0;

    }


    if (
        input.result ===
        "skipped"
    ) {

        existing.skippedCount += 1;

        existing.consecutiveCorrect = 0;

        existing.consecutiveIncorrect = 0;

    }


    existing.totalTimeSpentSeconds +=
        timeSpentSeconds;


    existing.lastResult =
        input.result;


    if (
        !existing.firstAttemptedAt
    ) {

        existing.firstAttemptedAt =
            now;
    }


    existing.lastAttemptedAt =
        now;


    const updated =
        clone(
            exposure
        );


    if (
        !updated.questions
    ) {

        updated.questions = {};
    }


    updated.questions[
        questionId
    ] =
        existing;


    updated.updatedAt =
        now;


    return updated;
}


function getQuestionExposure(
    exposure,
    questionId
) {

    validateQuestionId(
        questionId
    );


    const record =
        exposure?.questions?.[
            questionId
        ];


    if (
        !record
    ) {

        return null;
    }


    return clone(
        record
    );
}


function getQuestionAttemptCount(
    exposure,
    questionId
) {

    const record =
        getQuestionExposure(
            exposure,
            questionId
        );


    return (
        record?.attemptCount ??
        0
    );
}


function hasBeenAttempted(
    exposure,
    questionId
) {

    return (
        getQuestionAttemptCount(
            exposure,
            questionId
        ) > 0
    );
}


function getRecentQuestionIds(
    exposure,
    limit =
        rules.exposure.maxRecentAttempts
) {

    const records =
        Object.values(
            exposure?.questions ||
            {}
        );


    return records
        .filter(
            record =>
                record.lastAttemptedAt
        )
        .sort(
            (
                a,
                b
            ) =>
                new Date(
                    b.lastAttemptedAt
                ) -
                new Date(
                    a.lastAttemptedAt
                )
        )
        .slice(
            0,
            Math.max(
                0,
                limit
            )
        )
        .map(
            record =>
                record.questionId
        );
}


function getExposureSummary(
    exposure
) {

    const records =
        Object.values(
            exposure?.questions ||
            {}
        );


    return {

        uniqueQuestions:
            records.length,

        totalAttempts:
            records.reduce(
                (
                    total,
                    record
                ) =>
                    total +
                    record.attemptCount,
                0
            ),

        correctAttempts:
            records.reduce(
                (
                    total,
                    record
                ) =>
                    total +
                    record.correctCount,
                0
            ),

        incorrectAttempts:
            records.reduce(
                (
                    total,
                    record
                ) =>
                    total +
                    record.incorrectCount,
                0
            ),

        skippedAttempts:
            records.reduce(
                (
                    total,
                    record
                ) =>
                    total +
                    record.skippedCount,
                0
            ),

        totalTimeSpentSeconds:
            records.reduce(
                (
                    total,
                    record
                ) =>
                    total +
                    record.totalTimeSpentSeconds,
                0
            )

    };
}


function getQuestionIdsByResult(
    exposure,
    result
) {

    validateResult(
        result
    );


    return Object.values(
        exposure?.questions ||
        {}
    )
        .filter(
            record =>
                record.lastResult ===
                result
        )
        .map(
            record =>
                record.questionId
        );
}


function getWeaklyPerformedQuestions(
    exposure
) {

    return Object.values(
        exposure?.questions ||
        {}
    )
        .filter(
            record =>
                record.attemptCount > 0 &&
                record.correctCount === 0
        )
        .map(
            record =>
                clone(record)
        );
}


function validateExposure(
    exposure
) {

    if (
        !exposure ||
        typeof exposure !==
        "object"
    ) {

        return false;
    }


    if (
        typeof exposure.version !==
        "string"
    ) {

        return false;
    }


    if (
        typeof exposure.studentId !==
        "string" ||
        exposure.studentId.trim() === ""
    ) {

        return false;
    }


    if (
        typeof exposure.updatedAt !==
        "string"
    ) {

        return false;
    }


    if (
        !exposure.questions ||
        typeof exposure.questions !==
        "object"
    ) {

        return false;
    }


    for (
        const [
            questionId,
            record
        ]
        of Object.entries(
            exposure.questions
        )
    ) {

        if (
            record.questionId !==
            questionId
        ) {

            return false;
        }


        if (
            !Number.isInteger(
                record.attemptCount
            ) ||
            record.attemptCount < 1
        ) {

            return false;
        }


        if (
            record.correctCount < 0 ||
            record.incorrectCount < 0 ||
            record.skippedCount < 0
        ) {

            return false;
        }


        if (
            record.correctCount +
            record.incorrectCount +
            record.skippedCount !==
            record.attemptCount
        ) {

            return false;
        }


        if (
            !VALID_RESULTS.has(
                record.lastResult
            )
        ) {

            return false;
        }

    }


    return true;
}


export {

    createEmptyExposure,

    recordQuestionAttempt,

    getQuestionExposure,

    getQuestionAttemptCount,

    hasBeenAttempted,

    getRecentQuestionIds,

    getExposureSummary,

    getQuestionIdsByResult,

    getWeaklyPerformedQuestions,

    validateExposure

};
