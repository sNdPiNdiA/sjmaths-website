/**
 * SJMaths Maths Mastery
 *
 * Local Progress Repository
 *
 * Storage:
 *     Browser localStorage
 *
 * Important:
 *     This class owns storage.
 *
 *     Progress Engine does NOT know
 *     that localStorage exists.
 */

import {
    createEmptyProgress,
    validateProgressEvidence
} from "./progress-engine.js";


export class LocalProgressRepository {

    constructor(
        {
            storage = null,
            storageKey =
                "sjmaths-mastery-progress-v1"
        } = {}
    ) {

        /*
         * Dependency injection allows the repository
         * to be tested without a real browser.
         */

        this.storage =
            storage ||
            (
                typeof localStorage !==
                    "undefined"
                    ? localStorage
                    : null
            );


        this.storageKey =
            storageKey;
    }


    /* ========================================================
       Check storage availability
       ======================================================== */

    isAvailable() {

        return (
            this.storage !== null &&
            typeof this.storage.getItem ===
                "function" &&
            typeof this.storage.setItem ===
                "function"
        );
    }


    /* ========================================================
       Load
       ======================================================== */

    async load(
        studentId = "local"
    ) {

        /*
         * No stored progress.
         */

        if (
            !this.isAvailable()
        ) {

            return createEmptyProgress(
                studentId
            );
        }


        const raw =
            this.storage.getItem(
                this.storageKey
            );


        if (!raw) {

            return createEmptyProgress(
                studentId
            );
        }


        try {

            const progress =
                JSON.parse(
                    raw
                );


            /*
             * Basic structural protection.
             */

            if (
                !progress ||
                typeof progress !==
                    "object"
            ) {

                return createEmptyProgress(
                    studentId
                );
            }


            if (
                !progress.topics ||
                typeof progress.topics !==
                    "object"
            ) {

                return createEmptyProgress(
                    studentId
                );
            }


            return progress;

        }
        catch {

            /*
             * Corrupt JSON should not crash
             * the entire learning application.
             */

            return createEmptyProgress(
                studentId
            );
        }
    }


    /* ========================================================
       Save
       ======================================================== */

    async save(
        progress
    ) {

        if (!progress) {

            throw new Error(
                "LocalProgressRepository: progress is required."
            );
        }


        if (
            !this.isAvailable()
        ) {

            throw new Error(
                "LocalProgressRepository: storage unavailable."
            );
        }


        /*
         * Validate evidence before persisting.
         */

        const errors =
            validateProgressEvidence(
                progress
            );


        if (
            errors.length > 0
        ) {

            throw new Error(
                "Invalid progress data: " +
                errors.join("; ")
            );
        }


        const serialized =
            JSON.stringify(
                progress
            );


        try {

            this.storage.setItem(
                this.storageKey,
                serialized
            );

        }
        catch (error) {

            throw new Error(
                "LocalProgressRepository: unable to save progress. " +
                error.message
            );
        }


        return true;
    }


    /* ========================================================
       Clear
       ======================================================== */

    async clear() {

        if (
            !this.isAvailable()
        ) {

            return false;
        }


        this.storage.removeItem(
            this.storageKey
        );


        return true;
    }


    /* ========================================================
       Exists
       ======================================================== */

    async exists() {

        if (
            !this.isAvailable()
        ) {

            return false;
        }


        return (
            this.storage.getItem(
                this.storageKey
            ) !== null
        );
    }
}


export default LocalProgressRepository;
