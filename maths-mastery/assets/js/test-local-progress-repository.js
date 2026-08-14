import {
    createEmptyProgress,
    recordQuestionAttempt
} from "./progress-engine.js";

import {
    LocalProgressRepository
} from "./local-progress-repository.js";

import {
    MemoryStorage
} from "./memory-storage.js";


/* ============================================================
   Test helpers
   ============================================================ */

let passed = 0;
let failed = 0;


function pass(message) {

    passed++;

    console.log(
        `✓ ${message}`
    );
}


function fail(message) {

    failed++;

    console.log(
        `✗ ${message}`
    );
}


function section(
    number,
    title
) {

    console.log("");

    console.log(
        "--------------------------------------------"
    );

    console.log(
        `TEST ${number} — ${title}`
    );

    console.log(
        "--------------------------------------------"
    );
}


/* ============================================================
   TEST 1
   Repository creation
   ============================================================ */

section(
    1,
    "Repository Creation"
);


const storage =
    new MemoryStorage();


const repository =
    new LocalProgressRepository({

        storage,

        storageKey:
            "test-progress"
    });


if (
    repository.isAvailable()
) {

    pass(
        "Repository storage is available"
    );

}
else {

    fail(
        "Repository storage unavailable"
    );
}


/* ============================================================
   TEST 2
   Empty load
   ============================================================ */

section(
    2,
    "Empty Load"
);


const initial =
    await repository.load(
        "test-student"
    );


if (
    initial.studentId ===
        "test-student"
) {

    pass(
        "Missing progress creates empty progress"
    );

}
else {

    fail(
        "Empty progress student ID incorrect"
    );
}


if (
    Object.keys(
        initial.topics
    ).length === 0
) {

    pass(
        "Empty progress contains no topics"
    );

}
else {

    fail(
        "Empty progress unexpectedly contains topics"
    );
}


/* ============================================================
   TEST 3
   Save progress
   ============================================================ */

section(
    3,
    "Save Progress"
);


let progress =
    createEmptyProgress(
        "test-student"
    );


progress =
    recordQuestionAttempt(
        progress,
        {

            topicId:
                "percentage",

            questionId:
                "percentage-p-001",

            conceptId:
                "percentage-basics",

            skillIds: [
                "percentage-calculation"
            ],

            correct:
                true,

            timeSpentSeconds:
                30,

            attemptedAt:
                "2026-08-13T10:00:00.000Z"
        }
    );


const saved =
    await repository.save(
        progress
    );


if (
    saved === true
) {

    pass(
        "Progress saved successfully"
    );

}
else {

    fail(
        "Progress save failed"
    );
}


/* ============================================================
   TEST 4
   Storage actually contains data
   ============================================================ */

section(
    4,
    "Stored Data"
);


const stored =
    storage.getItem(
        "test-progress"
    );


if (
    stored !== null
) {

    pass(
        "Progress exists in storage"
    );

}
else {

    fail(
        "Progress missing from storage"
    );
}


let parsed;

try {

    parsed =
        JSON.parse(
            stored
        );

    pass(
        "Stored progress is valid JSON"
    );

}
catch {

    fail(
        "Stored progress is invalid JSON"
    );
}


/* ============================================================
   TEST 5
   Reload
   ============================================================ */

section(
    5,
    "Reload Progress"
);


const reloaded =
    await repository.load(
        "test-student"
    );


if (
    reloaded.topics.percentage
) {

    pass(
        "Saved topic restored correctly"
    );

}
else {

    fail(
        "Saved topic was not restored"
    );
}


if (
    reloaded
        .topics
        .percentage
        .evidence
        .correct === 1
) {

    pass(
        "Saved evidence restored correctly"
    );

}
else {

    fail(
        "Saved evidence was not restored"
    );
}


/* ============================================================
   TEST 6
   Exists
   ============================================================ */

section(
    6,
    "Exists Check"
);


const exists =
    await repository.exists();


if (
    exists === true
) {

    pass(
        "Repository detects existing progress"
    );

}
else {

    fail(
        "Repository exists check failed"
    );
}


/* ============================================================
   TEST 7
   Save invalid progress
   ============================================================ */

section(
    7,
    "Invalid Progress Protection"
);


let rejected =
    false;


try {

    await repository.save({

        invalid:
            true
    });

}
catch {

    rejected =
        true;
}


if (
    rejected
) {

    pass(
        "Invalid progress is rejected"
    );

}
else {

    fail(
        "Invalid progress was saved"
    );
}


/* ============================================================
   TEST 8
   Corrupt stored JSON
   ============================================================ */

section(
    8,
    "Corrupt Storage Recovery"
);


storage.setItem(
    "test-progress",
    "{invalid-json"
);


const recovered =
    await repository.load(
        "test-student"
    );


if (
    recovered.studentId ===
        "test-student" &&
    Object.keys(
        recovered.topics
    ).length === 0
) {

    pass(
        "Corrupt storage safely falls back to empty progress"
    );

}
else {

    fail(
        "Corrupt storage recovery failed"
    );
}


/* ============================================================
   TEST 9
   Clear
   ============================================================ */

section(
    9,
    "Clear Progress"
);


await repository.save(
    progress
);


const cleared =
    await repository.clear();


if (
    cleared === true
) {

    pass(
        "Clear operation completed"
    );

}
else {

    fail(
        "Clear operation failed"
    );
}


if (
    storage.getItem(
        "test-progress"
    ) === null
) {

    pass(
        "Progress removed from storage"
    );

}
else {

    fail(
        "Progress still exists after clear"
    );
}


/* ============================================================
   TEST 10
   Repository isolation
   ============================================================ */

section(
    10,
    "Repository Isolation"
);


const storageA =
    new MemoryStorage();


const storageB =
    new MemoryStorage();


const repositoryA =
    new LocalProgressRepository({

        storage:
            storageA,

        storageKey:
            "student-a"
    });


const repositoryB =
    new LocalProgressRepository({

        storage:
            storageB,

        storageKey:
            "student-b"
    });


await repositoryA.save(
    progress
);


const b =
    await repositoryB.load(
        "student-b"
    );


if (
    Object.keys(
        b.topics
    ).length === 0
) {

    pass(
        "Repositories remain isolated"
    );

}
else {

    fail(
        "Repository data leaked between instances"
    );
}


/* ============================================================
   TEST 11
   Storage failure handling
   ============================================================ */

section(
    11,
    "Storage Failure"
);


const failingStorage = {

    getItem() {

        return null;
    },

    setItem() {

        throw new Error(
            "Quota exceeded"
        );
    },

    removeItem() {}
};


const failingRepository =
    new LocalProgressRepository({

        storage:
            failingStorage
    });


let saveFailed =
    false;


try {

    await failingRepository.save(
        progress
    );

}
catch {

    saveFailed =
        true;
}


if (
    saveFailed
) {

    pass(
        "Storage save failure is surfaced safely"
    );

}
else {

    fail(
        "Storage save failure was swallowed"
    );
}


/* ============================================================
   SUMMARY
   ============================================================ */

console.log("");

console.log(
    "============================================"
);

console.log(
    " STEP 15 TEST SUMMARY"
);

console.log(
    "============================================"
);

console.log("");

console.log(
    `Passed: ${passed}`
);

console.log(
    `Failed: ${failed}`
);

console.log("");

if (
    failed === 0
) {

    console.log(
        "✓ ALL REPOSITORY TESTS PASSED"
    );

    console.log(
        "✓ STEP 15 COMPLETE"
    );

}
else {

    console.log(
        "✗ STEP 15 FAILED — REVIEW FAILURES ABOVE"
    );

    process.exitCode = 1;
}

console.log("");

console.log(
    "============================================"
);

console.log("");
