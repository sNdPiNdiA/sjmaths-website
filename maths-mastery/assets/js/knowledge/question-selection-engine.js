const fs = typeof window === "undefined" ? await import("fs") : null;
const path = typeof window === "undefined" ? await import("path") : null;

let rules = null;
let questionEntities = null;

export function initializeQuestionSelectionData(data) {
    if (data.rules) {
        rules = data.rules;
    }
    if (data.questionEntities) {
        questionEntities = data.questionEntities;
    }
    if (data.questionIndex) {
        questionEntities = Object.values(data.questionIndex.entities || {}).map(entity => {
            const data = entity?.data;
            if (!data || typeof data !== "object") return null;
            return {
                ...data,
                id: data.id || entity.id,
                _indexSource: entity.source || null
            };
        }).filter(Boolean);
    }
}

if (typeof window === "undefined") {
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
            "question-selection-rules.json"
        );

    const QUESTION_INDEX_PATH =
        path.join(
            ROOT,
            "data",
            "knowledge",
            "generated",
            "question-index.json"
        );

    function readJson(file) {
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

    rules =
        readJson(
            RULES_PATH
        );

    if (fs.existsSync(QUESTION_INDEX_PATH)) {
        const index = readJson(QUESTION_INDEX_PATH);
        questionEntities = Object.values(index.entities || {}).map(entity => {
            const data = entity?.data;
            if (!data || typeof data !== "object") return null;
            return {
                ...data,
                id: data.id || entity.id,
                _indexSource: entity.source || null
            };
        }).filter(Boolean);
    }
}


function getQuestionEntities() {

    if (questionEntities) {
        return questionEntities;
    }

    if (
        !fs.existsSync(
            QUESTION_INDEX_PATH
        )
    ) {

        throw new Error(
            "question-index.json does not exist. Run the knowledge index builder first."
        );
    }


    const index =
        readJson(
            QUESTION_INDEX_PATH
        );


    const entities =
        Object.values(
            index.entities || {}
        );


    return entities
        .map(
            entity => {

                /*
                 * Knowledge index stores questions as:
                 *
                 * {
                 *     id,
                 *     source,
                 *     data: {
                 *         topicId,
                 *         conceptId,
                 *         skillIds,
                 *         exams,
                 *         difficulty,
                 *         ...
                 *     }
                 * }
                 *
                 * The selection engine works with the
                 * actual question data, not the index wrapper.
                 */


                const data =
                    entity?.data;


                if (
                    !data ||
                    typeof data !==
                        "object"
                ) {

                    return null;
                }


                return {

                    ...data,

                    /*
                     * Preserve canonical question ID.
                     */

                    id:
                        data.id ||
                        entity.id,


                    /*
                     * Preserve index metadata
                     * without polluting the
                     * production question schema.
                     */

                    _indexSource:
                        entity.source ||
                        null

                };

            }
        )
        .filter(
            Boolean
        );
}
function normalizeWeakSkills(
    weakSkills
) {

    if (
        !Array.isArray(
            weakSkills
        )
    ) {

        return [];
    }


    return weakSkills.map(
        item => {

            if (
                typeof item ===
                    "string"
            ) {

                return {
                    skillId: item,
                    score: 0
                };
            }


            return {
                skillId:
                    item.skillId,

                score:
                    Number(
                        item.score ?? 0
                    )
            };
        }
    );
}


function getMasteryDifficulty(
    masteryStatus
) {

    return (
        rules.selection
            .masteryBands[
                masteryStatus
            ]?.targetDifficulty
        ||
        "basic"
    );
}


function difficultyDistance(
    candidate,
    target
) {

    const levels =
        rules.selection
            .difficulty;


    const candidateLevel =
        levels[
            candidate
        ] ?? 3;


    const targetLevel =
        levels[
            target
        ] ?? 3;


    return Math.abs(
        candidateLevel -
        targetLevel
    );
}


function calculateScore(
    question,
    context
) {

    const weights =
        rules.selection
            .weights;


    let score = 0;


    /* --------------------------------------------------------
       Weak skill
       -------------------------------------------------------- */

    const weakSkills =
        normalizeWeakSkills(
            context.weakSkills
        );


    const questionSkills =
        Array.isArray(
            question.skillIds
        )
            ? question.skillIds
            : [];


    const matchingWeakSkill =
        weakSkills.find(
            weak =>
                questionSkills.includes(
                    weak.skillId
                )
        );


    if (
        matchingWeakSkill
    ) {

        score +=
            weights.weakSkill;
    }


    /* --------------------------------------------------------
       Topic match
       -------------------------------------------------------- */

    if (
        context.currentTopicId &&
        question.topicId ===
            context.currentTopicId
    ) {

        score +=
            weights.topicMatch;
    }


    /* --------------------------------------------------------
       Exam match
       -------------------------------------------------------- */

    if (
        context.examId &&
        Array.isArray(
            question.exams
        ) &&
        question.exams.includes(
            context.examId
        )
    ) {

        score +=
            weights.examMatch;
    }


    /* --------------------------------------------------------
       Difficulty fit
       -------------------------------------------------------- */

    const targetDifficulty =
        context.targetDifficulty
        ||
        getMasteryDifficulty(
            context.masteryStatus
        );


    const distance =
        difficultyDistance(
            question.difficulty,
            targetDifficulty
        );


    if (
        distance === 0
    ) {

        score +=
            weights.difficultyFit;

    }
    else if (
        distance === 1
    ) {

        score +=
            weights.difficultyFit *
            0.5;
    }


    /* --------------------------------------------------------
       Novelty
       -------------------------------------------------------- */

    const attempted =
        Array.isArray(
            context.attemptedQuestionIds
        )
            ? context.attemptedQuestionIds
            : [];


    if (
        !attempted.includes(
            question.id
        )
    ) {

        score +=
            weights.novelty;
    }


    return score;
}


function selectQuestions(
    context = {},
    options = {}
) {

    const limit =
        Math.max(
            1,
            Number(
                options.limit ?? 1
            )
        );


    const attempted =
        new Set(
            Array.isArray(
                context.attemptedQuestionIds
            )
                ? context.attemptedQuestionIds
                : []
        );


    let questions =
        getQuestionEntities();


    /* --------------------------------------------------------
       Exam filter
       -------------------------------------------------------- */

    if (
        context.examId
    ) {

        questions =
            questions.filter(
                question =>
                    Array.isArray(
                        question.exams
                    ) &&
                    question.exams.includes(
                        context.examId
                    )
            );
    }


    /* --------------------------------------------------------
       Topic filter
       -------------------------------------------------------- */

    if (
        context.currentTopicId
    ) {

        const topicQuestions =
            questions.filter(
                question =>
                    question.topicId ===
                    context.currentTopicId
            );


        if (
            topicQuestions.length > 0
        ) {

            questions =
                topicQuestions;
        }
    }


    /* --------------------------------------------------------
       Exclude attempted questions
       -------------------------------------------------------- */

    if (
        rules.selection
            .excludeAttempted
    ) {

        const fresh =
            questions.filter(
                question =>
                    !attempted.has(
                        question.id
                    )
            );


        if (
            fresh.length > 0
        ) {

            questions =
                fresh;
        }
    }


    /* --------------------------------------------------------
       Score
       -------------------------------------------------------- */

    const scored =
        questions.map(
            question => ({

                question,

                score:
                    calculateScore(
                        question,
                        context
                    )

            })
        );


    /* --------------------------------------------------------
       Sort
       -------------------------------------------------------- */

    scored.sort(
        (a, b) => {

            if (
                b.score !==
                a.score
            ) {

                return (
                    b.score -
                    a.score
                );
            }


            return a.question.id.localeCompare(
                b.question.id
            );
        }
    );


    return scored
        .slice(
            0,
            limit
        );
}


function selectNextQuestion(
    context = {}
) {

    const results =
        selectQuestions(
            context,
            {
                limit: 1
            }
        );


    if (
        results.length === 0
    ) {

        return null;
    }


    return results[0];
}


function explainSelection(
    question,
    context = {}
) {

    if (
        !question
    ) {

        return [
            "No eligible question found."
        ];
    }


    const reasons = [];


    const weakSkills =
        normalizeWeakSkills(
            context.weakSkills
        );


    if (
        weakSkills.some(
            weak =>
                Array.isArray(
                    question.skillIds
                ) &&
                question.skillIds.includes(
                    weak.skillId
                )
        )
    ) {

        reasons.push(
            "targets a weak skill"
        );
    }


    if (
        context.currentTopicId &&
        question.topicId ===
            context.currentTopicId
    ) {

        reasons.push(
            "matches the current topic"
        );
    }


    if (
        context.examId &&
        Array.isArray(
            question.exams
        ) &&
        question.exams.includes(
            context.examId
        )
    ) {

        reasons.push(
            "matches the selected examination"
        );
    }


    if (
        context.masteryStatus
    ) {

        reasons.push(
            `difficulty is adapted to ${context.masteryStatus} mastery`
        );
    }


    if (
        reasons.length === 0
    ) {

        reasons.push(
            "is the highest-ranked eligible question"
        );
    }


    return reasons;
}


export {
    selectQuestions,
    selectNextQuestion,
    calculateScore,
    explainSelection
};


