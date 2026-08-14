import fs from "fs";
import path from "path";


const root =
    path.resolve(
        process.cwd(),
        "maths-mastery"
    );


const syllabusDir =
    path.join(
        root,
        "data",
        "syllabi"
    );


const generatedDir =
    path.join(
        root,
        "data",
        "knowledge",
        "generated"
    );


fs.mkdirSync(
    generatedDir,
    {
        recursive: true
    }
);


function loadJson(
    filePath
) {

    const raw =
        fs.readFileSync(
            filePath,
            "utf8"
        );


    const clean =
        raw.charCodeAt(0) ===
            0xFEFF
            ? raw.slice(1)
            : raw;


    return JSON.parse(
        clean
    );
}


const files =
    fs.existsSync(
        syllabusDir
    )
        ? fs.readdirSync(
            syllabusDir
        )
        .filter(
            file =>
                file.endsWith(
                    ".json"
                )
        )
        .sort()
        : [];


const syllabi = [];


for (
    const file
    of files
) {

    const filePath =
        path.join(
            syllabusDir,
            file
        );


    const data =
        loadJson(
            filePath
        );


    syllabi.push({

        id:
            data.id,

        examId:
            data.examId,

        name:
            data.name,

        version:
            data.version,

        file,

        sections:
            Array.isArray(
                data.sections
            )
                ? data.sections.length
                : 0,

        topics:
            Array.isArray(
                data.sections
            )
                ? data.sections.reduce(
                    (
                        total,
                        section
                    ) =>
                        total +
                        (
                            Array.isArray(
                                section.topics
                            )
                                ? section.topics.length
                                : 0
                        ),
                    0
                )
                : 0

    });

}


const index = {

    generatedAt:
        new Date().toISOString(),

    count:
        syllabi.length,

    syllabi

};


fs.writeFileSync(

    path.join(
        generatedDir,
        "syllabus-index.json"
    ),

    JSON.stringify(
        index,
        null,
        2
    ),

    "utf8"
);


console.log(
    "✓ syllabus-index.json generated"
);


console.log(
    `Syllabi: ${syllabi.length}`
);
