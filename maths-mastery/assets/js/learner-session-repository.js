/**
 * SJMaths Maths Mastery
 * STEP 23 — Learner Session Repository
 *
 * Persistence layer for the unified learner flow.
 *
 * This repository stores the learner FLOW only.
 *
 * Progress evidence remains owned by the existing
 * Step 15 progress repository.
 *
 * The session repository therefore does NOT replace:
 *
 * progress-repository.js
 * local-progress-repository.js
 *
 * It only remembers where the learner currently is
 * in the unified learning journey.
 */


/* ============================================================
   Constants
   ============================================================ */

export const SESSION_VERSION =
    "1.0.0";


export const DEFAULT_SESSION_KEY =
    "sjmaths:maths-mastery:learner-session";


/* ============================================================
   Storage Adapter
   ============================================================ */

export function createBrowserStorage(
    storage = null
) {

    const target =
        storage ||
        (
            typeof localStorage !==
                "undefined"
                ? localStorage
                : null
        );


    if (!target) {

        throw new Error(
            "Browser storage is unavailable"
        );
    }


    return target;
}


/* ============================================================
   Session Repository
   ============================================================ */

export class LearnerSessionRepository {

    constructor(
        storage,
        key =
            DEFAULT_SESSION_KEY
    ) {

        this.storage =
            createBrowserStorage(
                storage
            );

        this.key =
            key;
    }


    /* ========================================================
       Create Session
       ======================================================== */

    create(
        flow
    ) {

        if (
            !flow ||
            !flow.studentId
        ) {

            throw new Error(
                "Valid learner flow is required"
            );
        }


        const session = {

            sessionVersion:
                SESSION_VERSION,

            studentId:
                flow.studentId,

            learnerFlow:
                structuredClone(
                    flow
                ),

            savedAt:
                new Date().toISOString()
        };


        this.saveSession(
            session
        );


        return structuredClone(
            session
        );
    }


    /* ========================================================
       Save Session
       ======================================================== */

    save(
        flow
    ) {

        if (
            !flow ||
            !flow.studentId
        ) {

            throw new Error(
                "Valid learner flow is required"
            );
        }


        const session = {

            sessionVersion:
                SESSION_VERSION,

            studentId:
                flow.studentId,

            learnerFlow:
                structuredClone(
                    flow
                ),

            savedAt:
                new Date().toISOString()
        };


        this.saveSession(
            session
        );


        return structuredClone(
            session
        );
    }


    /* ========================================================
       Internal Save
       ======================================================== */

    saveSession(
        session
    ) {

        if (
            !session ||
            !session.studentId ||
            !session.learnerFlow
        ) {

            throw new Error(
                "Invalid learner session"
            );
        }


        this.storage.setItem(
            this.key,
            JSON.stringify(
                session
            )
        );
    }


    /* ========================================================
       Load Session
       ======================================================== */

    load() {

        const raw =
            this.storage.getItem(
                this.key
            );


        if (!raw) {

            return null;
        }


        try {

            const session =
                JSON.parse(
                    raw
                );


            if (
                !this.validateSession(
                    session
                )
            ) {

                return null;
            }


            return structuredClone(
                session
            );

        }
        catch {

            return null;
        }
    }


    /* ========================================================
       Load Learner Flow
       ======================================================== */

    loadFlow() {

        const session =
            this.load();


        if (!session) {

            return null;
        }


        return structuredClone(
            session.learnerFlow
        );
    }


    /* ========================================================
       Exists
       ======================================================== */

    exists() {

        return (
            this.storage.getItem(
                this.key
            ) !== null
        );
    }


    /* ========================================================
       Clear
       ======================================================== */

    clear() {

        this.storage.removeItem(
            this.key
        );
    }


    /* ========================================================
       Validation
       ======================================================== */

    validateSession(
        session
    ) {

        if (
            !session
        ) {

            return false;
        }


        if (
            session.sessionVersion !==
            SESSION_VERSION
        ) {

            return false;
        }


        if (
            !session.studentId
        ) {

            return false;
        }


        if (
            !session.learnerFlow
        ) {

            return false;
        }


        if (
            session.learnerFlow.studentId !==
            session.studentId
        ) {

            return false;
        }


        if (
            !session.savedAt
        ) {

            return false;
        }


        return true;
    }


    /* ========================================================
       Safe Load
       ======================================================== */

    loadOrCreate(
        flow
    ) {

        const existing =
            this.load();


        if (
            existing
        ) {

            return existing;
        }


        return this.create(
            flow
        );
    }


    /* ========================================================
       Update Flow
       ======================================================== */

    update(
        updater
    ) {

        const session =
            this.load();


        if (!session) {

            throw new Error(
                "No learner session exists"
            );
        }


        const current =
            structuredClone(
                session.learnerFlow
            );


        if (
            typeof updater !==
            "function"
        ) {

            throw new Error(
                "updater must be a function"
            );
        }


        const updated =
            updater(
                current
            );


        if (
            !updated ||
            !updated.studentId
        ) {

            throw new Error(
                "Updated learner flow is invalid"
            );
        }


        return this.save(
            updated
        );
    }
}


export default {

    SESSION_VERSION,

    DEFAULT_SESSION_KEY,

    createBrowserStorage,

    LearnerSessionRepository
};
