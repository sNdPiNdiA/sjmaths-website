/**
 * ============================================================
 * SJMaths — Question Exposure Repository
 * ============================================================
 *
 * Purpose:
 *
 * Persist question-level exposure separately from learner
 * progress evidence.
 *
 * Architecture:
 *
 * Question Exposure Engine
 *          ↓
 * Question Exposure Repository
 *          ↓
 * Storage
 *
 * IMPORTANT:
 *
 * - Does NOT contain learning algorithms.
 * - Does NOT calculate mastery.
 * - Does NOT select questions.
 * - Does NOT modify progress state.
 * - Exposure remains a separate production data object.
 */

import {
    createEmptyExposure,
    validateExposure
} from "./knowledge/question-exposure-engine.js";


const DEFAULT_STORAGE_KEY =
    "sjmaths-mastery-question-exposure-v1";


/* ============================================================
   Browser Storage Adapter
   ============================================================ */

export function createBrowserStorage(
    target = null
) {

    const storage =
        target ||
        (
            typeof localStorage !== "undefined"
                ? localStorage
                : null
        );

    if (!storage) {

        throw new Error(
            "QuestionExposureRepository: browser storage is unavailable."
        );
    }

    return storage;
}


/* ============================================================
   Clone
   ============================================================ */

function clone(
    value
) {

    if (
        value === null ||
        value === undefined
    ) {

        return value;
    }

    return JSON.parse(
        JSON.stringify(value)
    );
}


/* ============================================================
   Repository
   ============================================================ */

export class QuestionExposureRepository {

    constructor({
        storage = null,
        storageKey = DEFAULT_STORAGE_KEY
    } = {}) {

        this.storage =
            storage ||
            (
                typeof localStorage !== "undefined"
                    ? localStorage
                    : null
            );

        this.storageKey =
            storageKey;
    }


    /* ========================================================
       Availability
       ======================================================== */

    isAvailable() {

        return (
            this.storage !== null &&
            typeof this.storage.getItem === "function" &&
            typeof this.storage.setItem === "function" &&
            typeof this.storage.removeItem === "function"
        );
    }


    /* ========================================================
       Load
       ======================================================== */

    async load(
        studentId = "local"
    ) {

        if (
            typeof studentId !== "string" ||
            studentId.trim() === ""
        ) {

            throw new Error(
                "QuestionExposureRepository: studentId is required."
            );
        }


        if (
            !this.isAvailable()
        ) {

            return createEmptyExposure(
                studentId
            );
        }


        let raw;

        try {

            raw =
                this.storage.getItem(
                    this.storageKey
                );

        } catch {

            return createEmptyExposure(
                studentId
            );
        }


        if (!raw) {

            return createEmptyExposure(
                studentId
            );
        }


        let parsed;

        try {

            parsed =
                JSON.parse(
                    raw
                );

        } catch {

            return createEmptyExposure(
                studentId
            );
        }


        if (
            !parsed ||
            parsed.studentId !== studentId
        ) {

            return createEmptyExposure(
                studentId
            );
        }


        const validation =
            validateExposure(
                parsed
            );


        if (
            validation !== true &&
            !(
                validation &&
                validation.valid === true
            )
        ) {

            return createEmptyExposure(
                studentId
            );
        }


        return clone(
            parsed
        );
    }


    /* ========================================================
       Save
       ======================================================== */

    async save(
        exposure
    ) {

        if (!exposure) {

            throw new Error(
                "QuestionExposureRepository: exposure is required."
            );
        }


        if (
            !this.isAvailable()
        ) {

            throw new Error(
                "QuestionExposureRepository: storage is unavailable."
            );
        }


        const validation =
            validateExposure(
                exposure
            );


        if (
            validation !== true &&
            !(
                validation &&
                validation.valid === true
            )
        ) {

            const errors =
                validation?.errors ||
                ["Invalid question exposure."];

            throw new Error(
                "QuestionExposureRepository: invalid exposure. " +
                errors.join("; ")
            );
        }


        try {

            this.storage.setItem(
                this.storageKey,
                JSON.stringify(
                    exposure
                )
            );

        } catch (error) {

            throw new Error(
                "QuestionExposureRepository: unable to save exposure. " +
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


        try {

            this.storage.removeItem(
                this.storageKey
            );

        } catch {

            return false;
        }


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


        try {

            return (
                this.storage.getItem(
                    this.storageKey
                ) !== null
            );

        } catch {

            return false;
        }
    }
}


/* ============================================================
   Default Export
   ============================================================ */

export default QuestionExposureRepository;
