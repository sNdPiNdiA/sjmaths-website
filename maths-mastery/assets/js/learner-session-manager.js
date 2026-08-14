/**
 * SJMaths Maths Mastery
 * STEP 23 — Learner Session Manager
 *
 * Connects:
 *
 * Step 22 Learner Flow
 * +
 * Step 23 Session Repository
 *
 * The manager provides the application-level API.
 */

import {
    LearnerSessionRepository
} from "./learner-session-repository.js";


export class LearnerSessionManager {

    constructor(
        storage,
        key
    ) {

        this.repository =
            new LearnerSessionRepository(
                storage,
                key
            );
    }


    /* ========================================================
       Start New Session
       ======================================================== */

    start(
        flow
    ) {

        return this.repository.create(
            flow
        );
    }


    /* ========================================================
       Save Current Flow
       ======================================================== */

    save(
        flow
    ) {

        return this.repository.save(
            flow
        );
    }


    /* ========================================================
       Restore
       ======================================================== */

    restore() {

        return this.repository.loadFlow();
    }


    /* ========================================================
       Restore Session
       ======================================================== */

    restoreSession() {

        return this.repository.load();
    }


    /* ========================================================
       Has Session
       ======================================================== */

    hasSession() {

        return this.repository.exists();
    }


    /* ========================================================
       Clear
       ======================================================== */

    clear() {

        this.repository.clear();
    }


    /* ========================================================
       Save And Restore
       ======================================================== */

    saveAndRestore(
        flow
    ) {

        this.save(
            flow
        );

        return this.restore();
    }
}


export default
    LearnerSessionManager;
