import {
    SyllabusRepository
} from "./syllabus-repository.js";

import {
    SyllabusEngine
} from "./syllabus-engine.js";


function assert(
    condition,
    message
) {

    if (!condition) {

        throw new Error(
            message
        );
    }

    console.log(
        `✓ ${message}`
    );
}


console.log("");
console.log(
    "============================================================"
);
console.log(
    " SYLLABUS ENGINE TEST"
);
console.log(
    "============================================================"
);
console.log("");


const repository =
    new SyllabusRepository();


const engine =
    new SyllabusEngine({
        repository
    });


console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 1 — Repository"
);
console.log(
    "--------------------------------------------"
);


const files =
    repository.listSyllabusFiles();


assert(
    Array.isArray(
        files
    ),
    "Syllabus file list returned"
);


console.log("");


console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 2 — Load All"
);
console.log(
    "--------------------------------------------"
);


const syllabi =
    repository.loadAll();


assert(
    Array.isArray(
        syllabi
    ),
    "All syllabi loaded"
);


for (
    const syllabus
    of syllabi
) {

    assert(
        Boolean(
            syllabus.id
        ),
        `Syllabus ${syllabus.id} has ID`
    );


    assert(
        Boolean(
            syllabus.examId
        ),
        `Syllabus ${syllabus.id} has examId`
    );


    assert(
        Array.isArray(
            syllabus.sections
        ),
        `Syllabus ${syllabus.id} has sections`
    );

}


console.log("");


console.log(
    "--------------------------------------------"
);
console.log(
    "TEST 3 — Engine"
);
console.log(
    "--------------------------------------------"
);


for (
    const syllabus
    of syllabi
) {

    const summary =
        engine.getSummary(
            syllabus.id
        );


    assert(
        summary.id ===
            syllabus.id,
        `Summary returned for ${syllabus.id}`
    );


    assert(
        Number.isInteger(
            summary.sections
        ),
        `${syllabus.id} section count valid`
    );


    assert(
        Number.isInteger(
            summary.topics
        ),
        `${syllabus.id} topic count valid`
    );

}


console.log("");


console.log(
    "============================================================"
);
console.log(
    " SYLLABUS ENGINE TEST COMPLETE"
);
console.log(
    "============================================================"
);
console.log("");
