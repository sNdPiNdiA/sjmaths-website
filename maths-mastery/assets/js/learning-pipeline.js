/**
 * SJMaths Maths Mastery
 * Learning Pipeline
 *
 * Connects:
 *
 * Question Attempt
 *       ↓
 * Progress Engine
 *       ↓
 * Progress Repository
 *       ↓
 * Mastery Engine
 *       ↓
 * Recommendation Engine
 *
 * This module coordinates the engines.
 * It does not contain their internal algorithms.
 */

import {
    recordQuestionAttempt,
    recordMiniTestAttempt
} from "./progress-engine.js";

import {
    recordQuestionAttempt as recordExposureAttempt
} from "./knowledge/question-exposure-engine.js";

import {
    calculateMastery,
    getWeakSkills
} from "./mastery-engine.js";


export class LearningPipeline {

    constructor({
        repository,
        exposureRepository = null,
        masteryRules,
        recommendationEngine
    }) {

        if (!repository) {

            throw new Error(
                "LearningPipeline: repository is required."
            );
        }


        if (!masteryRules) {

            throw new Error(
                "LearningPipeline: masteryRules are required."
            );
        }


        this.repository =
            repository;

        this.exposureRepository =
            exposureRepository;

        this.masteryRules =
            masteryRules;

        this.recommendationEngine =
            recommendationEngine || null;
    }


    /* ========================================================
       Load Student Progress
       ======================================================== */

    async loadProgress(
        studentId = "local"
    ) {

        return await this.repository.load(
            studentId
        );
    }


    /* ========================================================
       Record Question
       ======================================================== */

    async recordQuestion({
        studentId = "local",
        topicId,
        questionId,
        conceptId = null,
        skillIds = [],
        correct,
        timeSpentSeconds = 0,
        attemptedAt = null
    }) {

        const progress =
            await this.repository.load(
                studentId
            );


        const updatedProgress =
            recordQuestionAttempt(
                progress,
                {

                    topicId,

                    questionId,

                    conceptId,

                    skillIds,

                    correct,

                    timeSpentSeconds,

                    attemptedAt
                }
            );


        await this.repository.save(
            updatedProgress
        );
        /*
         * Question Exposure
         *
         * This is deliberately separate from progress-engine
         * mutation. The progress engine owns learner progress;
         * the exposure engine owns per-question history.
         */
        if (
            this.exposureRepository
        ) {

            const exposure =
                await this.exposureRepository.load(
                    studentId
                );

            const result =
                correct === true
                    ? "correct"
                    : correct === false
                        ? "incorrect"
                        : "skipped";

            const updatedExposure =
                recordExposureAttempt(
                    exposure,
                    {
                        questionId,

                        result,

                        timeSpentSeconds,

                        attemptedAt
                    }
                );

            await this.exposureRepository.save(
                updatedExposure
            );
        }


        return this.getLearningState(
            updatedProgress
        );
    }


    /* ========================================================
       Record Mini Test
       ======================================================== */

    async recordMiniTest({
        studentId = "local",
        topicId,
        testId,
        score,
        accuracy,
        attemptedAt = null
    }) {

        const progress =
            await this.repository.load(
                studentId
            );


        const updatedProgress =
            recordMiniTestAttempt(
                progress,
                {

                    topicId,

                    testId,

                    score,

                    accuracy,

                    attemptedAt
                }
            );


        await this.repository.save(
            updatedProgress
        );


        return this.getLearningState(
            updatedProgress
        );
    }


    /* ========================================================
       Calculate Current Learning State
       ======================================================== */

    getLearningState(
        progress
    ) {

        const mastery =
            calculateMastery(
                progress,
                this.masteryRules
            );


        const weakSkills = {};


        for (
            const [
                topicId,
                topic
            ]
            of Object.entries(
                progress.topics || {}
            )
        ) {

            weakSkills[topicId] =
                getWeakSkills(
                    topic
                );
        }


        return {

            progress,

            mastery,

            weakSkills,

            recommendation:
                null
        };
    }


    /* ========================================================
       Get Recommendation
       ======================================================== */

    getRecommendation({
        progress,
        currentTopicId,
        examId = null
    }) {

        if (
            !this.recommendationEngine
        ) {

            return null;
        }


        const mastery =
            calculateMastery(
                progress,
                this.masteryRules
            );


        /*
         * The recommendation engine is deliberately
         * called through its existing public API.
         *
         * This keeps recommendation logic outside
         * the learning pipeline.
         */

        if (
            typeof this
                .recommendationEngine
                .recommend !==
                "function"
        ) {

            throw new Error(
                "LearningPipeline: recommendation engine must expose recommend()."
            );
        }


        return this
            .recommendationEngine
            .recommend({

                currentTopicId,

                currentMastery:
                    mastery
                        .topics?.[
                            currentTopicId
                        ]?.score ?? 0,

                examId,

                progress,

                mastery
            });
    }
}


export default LearningPipeline;

