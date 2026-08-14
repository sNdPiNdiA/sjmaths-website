import fs from "fs";
import path from "path";

const root =
    path.resolve(
        process.cwd(),
        "maths-mastery"
    );

const questionRoot =
    path.join(
        root,
        "data",
        "questions",
        "readiness"
    );

const reportFile =
    path.join(
        root,
        "data",
        "taxonomy",
        "generated",
        "readiness-mathematical-audit-32.61A.json"
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


function norm(value) {

    return String(
        value ?? ""
    )
        .replace(/−/g, "-")
        .replace(/×/g, "*")
        .replace(/÷/g, "/")
        .replace(/²/g, "^2")
        .replace(/³/g, "^3")
        .replace(/°/g, "")
        .replace(/\s+/g, "")
        .toLowerCase()
        .trim();
}


function number(value) {

    const cleaned =
        String(
            value ?? ""
        )
            .replace(/−/g, "-")
            .replace(/°/g, "")
            .replace(/₹/g, "")
            .replace(/,/g, "")
            .replace(/%/g, "")
            .replace(/cm²/g, "")
            .replace(/m²/g, "")
            .replace(/cm2/g, "")
            .replace(/m2/g, "")
            .replace(/cm/g, "")
            .replace(/m/g, "")
            .trim();


    const n =
        Number(
            cleaned
        );


    return Number.isFinite(
        n
    )
        ? n
        : null;
}


function fraction(value) {

    const match =
        norm(value).match(
            /^(-?\d+)\/(-?\d+)$/
        );

    if (!match) {
        return null;
    }

    const denominator =
        Number(
            match[2]
        );

    if (
        denominator === 0
    ) {
        return null;
    }

    return (
        Number(match[1]) /
        denominator
    );
}


function equivalentNumber(
    a,
    b
) {

    if (
        a === null ||
        b === null
    ) {
        return false;
    }

    return Math.abs(
        a - b
    ) < 1e-9;
}


function parseValues(
    text
) {

    return text
        .split(",")
        .map(
            x =>
                Number(
                    x.trim()
                )
        );
}


function mean(
    values
) {

    return (
        values.reduce(
            (
                sum,
                x
            ) =>
                sum + x,
            0
        ) /
        values.length
    );
}


function median(
    values
) {

    const sorted =
        [...values].sort(
            (
                a,
                b
            ) =>
                a - b
        );

    const mid =
        Math.floor(
            sorted.length / 2
        );

    if (
        sorted.length % 2
    ) {

        return sorted[mid];
    }

    return (
        sorted[mid - 1] +
        sorted[mid]
    ) / 2;
}


function gcd(
    a,
    b
) {

    a =
        Math.abs(a);

    b =
        Math.abs(b);

    while (
        b !== 0
    ) {

        const t =
            a % b;

        a =
            b;

        b =
            t;
    }

    return a;
}


function classify(
    q
) {

    const text =
        norm(
            q.questionText
        );

    const answer =
        norm(
            q.correctAnswer
        );

    const skill =
        q.readinessSkillId;


    // ========================================================
    // MEAN
    // ========================================================

    if (
        skill ===
        "data.mean"
    ) {

        let match =
            q.questionText.match(
                /mean of\s+(.+?)\./i
            );

        if (
            match
        ) {

            const values =
                parseValues(
                    match[1]
                );


            if (
                values.every(
                    Number.isFinite
                )
            ) {

                const expected =
                    mean(
                        values
                    );


                const actual =
                    number(
                        q.correctAnswer
                    );


                return {
                    status:
                        equivalentNumber(
                            actual,
                            expected
                        )
                            ? "PASS"
                            : "FAIL",

                    expected:
                        String(expected),

                    method:
                        "mean-direct"
                };
            }
        }


        const unknown =
            q.questionText.match(
                /mean of\s+(\d+),\s*(\d+)\s*and\s*x\s*is\s*(\d+)/i
            );


        if (
            unknown
        ) {

            const a =
                Number(
                    unknown[1]
                );

            const b =
                Number(
                    unknown[2]
                );

            const m =
                Number(
                    unknown[3]
                );


            const expected =
                m * 3 -
                a -
                b;


            const actual =
                number(
                    q.correctAnswer
                );


            return {
                status:
                    equivalentNumber(
                        actual,
                        expected
                    )
                        ? "PASS"
                        : "FAIL",

                expected:
                    String(expected),

                method:
                    "mean-unknown"
            };
        }


        const totalMatch =
            q.questionText.match(
                /mean of\s+(\d+)\s+numbers.*?(\d+)/i
            );


        if (
            totalMatch
        ) {

            const count =
                Number(
                    totalMatch[1]
                );

            const m =
                Number(
                    totalMatch[2]
                );

            const expected =
                count * m;


            const actual =
                number(
                    q.correctAnswer
                );


            return {
                status:
                    equivalentNumber(
                        actual,
                        expected
                    )
                        ? "PASS"
                        : "FAIL",

                expected:
                    String(expected),

                method:
                    "mean-times-count"
            };
        }


        const totalObs =
            q.questionText.match(
                /total\s+(\d+).*?(\d+)\s+observations/i
            );


        if (
            totalObs
        ) {

            const expected =
                Number(
                    totalObs[1]
                ) /
                Number(
                    totalObs[2]
                );


            const actual =
                number(
                    q.correctAnswer
                );


            return {
                status:
                    equivalentNumber(
                        actual,
                        expected
                    )
                        ? "PASS"
                        : "FAIL",

                expected:
                    String(expected),

                method:
                    "mean-total-observations"
            };
        }


        if (
            /arithmetic mean/i.test(
                q.questionText
            )
        ) {

            if (
                answer ===
                "sumofobservations/numberofobservations"
            ) {

                return {
                    status:
                        "PASS",
                    expected:
                        "sum of observations / number of observations",
                    method:
                        "mean-definition"
                };
            }
        }
    }


    // ========================================================
    // MEDIAN
    // ========================================================

    if (
        skill ===
        "data.median"
    ) {

        const match =
            q.questionText.match(
                /median of\s+(.+?)\./i
            );


        if (
            match
        ) {

            const values =
                parseValues(
                    match[1]
                );


            if (
                values.every(
                    Number.isFinite
                )
            ) {

                const expected =
                    median(
                        values
                    );


                const actual =
                    number(
                        q.correctAnswer
                    );


                return {
                    status:
                        equivalentNumber(
                            actual,
                            expected
                        )
                            ? "PASS"
                            : "FAIL",

                    expected:
                        String(expected),

                    method:
                        "median-direct"
                };
            }
        }


        if (
            /arrange in order/i.test(
                q.questionText
            )
        ) {

            return {
                status:
                    answer ===
                    "arrangeinorder"
                        ? "PASS"
                        : "FAIL",

                expected:
                    "arrange in order",

                method:
                    "median-order"
            };
        }


        if (
            /even number of ordered observations/i.test(
                q.questionText
            )
        ) {

            return {
                status:
                    answer.includes(
                        "averageofthetwomiddlevalues"
                    )
                        ? "PASS"
                        : "FAIL",

                expected:
                    "average of the two middle values",

                method:
                    "median-even-rule"
            };
        }
    }


    // ========================================================
    // MODE
    // ========================================================

    if (
        skill ===
        "data.mode"
    ) {

        const match =
            q.questionText.match(
                /mode of\s+(.+?)\./i
            );


        if (
            match
        ) {

            const values =
                match[1]
                    .split(",")
                    .map(
                        x =>
                            x.trim()
                    );


            const frequency =
                new Map();


            for (
                const value
                of values
            ) {

                frequency.set(
                    value,
                    (
                        frequency.get(
                            value
                        ) || 0
                    ) + 1
                );
            }


            const highest =
                Math.max(
                    ...frequency.values()
                );


            const modes =
                [
                    ...frequency.entries()
                ]
                    .filter(
                        (
                            [, count]
                        ) =>
                            count ===
                            highest
                    )
                    .map(
                        (
                            [value]
                        ) =>
                            value
                    )
                    .sort();


            const expected =
                highest === 1
                    ? "no mode"
                    : modes.join(
                        " and "
                    );


            return {
                status:
                    norm(
                        q.correctAnswer
                    ) ===
                    norm(
                        expected
                    )
                        ? "PASS"
                        : "FAIL",

                expected,

                method:
                    "mode-direct"
            };
        }


        if (
            /which frequency identifies the mode/i.test(
                q.questionText
            )
        ) {

            return {
                status:
                    answer ===
                    "highestfrequency"
                        ? "PASS"
                        : "FAIL",

                expected:
                    "highest frequency",

                method:
                    "mode-definition"
            };
        }
    }


    // ========================================================
    // DECIMAL → PERCENT
    // ========================================================

    if (
        skill ===
        "decimals.convert-percent"
    ) {

        const match =
            q.questionText.match(
                /convert\s+([0-9.]+)\s+to\s+percent/i
            );


        if (
            match
        ) {

            const decimal =
                Number(
                    match[1]
                );


            const expected =
                decimal *
                100;


            const actual =
                number(
                    q.correctAnswer
                );


            return {
                status:
                    equivalentNumber(
                        actual,
                        expected
                    )
                        ? "PASS"
                        : "FAIL",

                expected:
                    `${expected}%`,

                method:
                    "decimal-percent"
            };
        }
    }


    // ========================================================
    // FRACTION EQUIVALENCE
    // ========================================================

    if (
        skill ===
        "fractions.equivalent"
    ) {

        const source =
            q.questionText.match(
                /(?:for|to)\s+(\d+)\/(\d+)/i
            );


        if (
            source
        ) {

            const expectedSource =
                Number(
                    source[1]
                ) /
                Number(
                    source[2]
                );


            const actual =
                fraction(
                    q.correctAnswer
                );


            if (
                actual !== null
            ) {

                return {
                    status:
                        equivalentNumber(
                            actual,
                            expectedSource
                        )
                            ? "PASS"
                            : "FAIL",

                    expected:
                        "equivalent fraction",

                    method:
                        "fraction-equivalence"
                };
            }
        }
    }


    // ========================================================
    // FRACTION SIMPLIFICATION
    // ========================================================

    if (
        skill ===
        "fractions.simplify"
    ) {

        const match =
            q.questionText.match(
                /simplify\s+(\d+)\/(\d+)/i
            );


        if (
            match
        ) {

            const n =
                Number(
                    match[1]
                );

            const d =
                Number(
                    match[2]
                );


            const g =
                gcd(
                    n,
                    d
                );


            const expected =
                `${n / g}/${d / g}`;


            return {
                status:
                    norm(
                        q.correctAnswer
                    ) ===
                    norm(
                        expected
                    )
                        ? "PASS"
                        : "FAIL",

                expected,

                method:
                    "fraction-simplify"
            };
        }
    }


    // ========================================================
    // PERCENTAGE BASIC
    // ========================================================

    if (
        skill ===
        "percentage.basic"
    ) {

        const fractionMatch =
            q.questionText.match(
                /convert\s+(\d+)%\s+to\s+a\s+fraction/i
            );


        if (
            fractionMatch
        ) {

            const n =
                Number(
                    fractionMatch[1]
                );


            const g =
                gcd(
                    n,
                    100
                );


            const expected =
                `${n / g}/${100 / g}`;


            return {
                status:
                    norm(
                        q.correctAnswer
                    ) ===
                    norm(
                        expected
                    )
                        ? "PASS"
                        : "FAIL",

                expected,

                method:
                    "percent-to-fraction"
            };
        }


        const decimalMatch =
            q.questionText.match(
                /convert\s+(\d+)%\s+to\s+a\s+decimal/i
            );


        if (
            decimalMatch
        ) {

            const expected =
                Number(
                    decimalMatch[1]
                ) /
                100;


            return {
                status:
                    equivalentNumber(
                        number(
                            q.correctAnswer
                        ),
                        expected
                    )
                        ? "PASS"
                        : "FAIL",

                expected:
                    String(expected),

                method:
                    "percent-to-decimal"
            };
        }


        const percentValueMatch =
            q.questionText.match(
                /(\d+)%\s+of\s+(\d+)/i
            );


        if (
            percentValueMatch
        ) {

            const expected =
                Number(
                    percentValueMatch[1]
                ) /
                100 *
                Number(
                    percentValueMatch[2]
                );


            return {
                status:
                    equivalentNumber(
                        number(
                            q.correctAnswer
                        ),
                        expected
                    )
                        ? "PASS"
                        : "FAIL",

                expected:
                    String(expected),

                method:
                    "percentage-of"
            };
        }
    }


    // ========================================================
    // LENGTH CONVERSION
    // ========================================================

    if (
        skill ===
        "measurement.length"
    ) {

        const cmMatch =
            q.questionText.match(
                /convert\s+(\d+)\s*m\s+to\s+centimetres/i
            );


        if (
            cmMatch
        ) {

            const expected =
                Number(
                    cmMatch[1]
                ) *
                100;


            return {
                status:
                    equivalentNumber(
                        number(
                            q.correctAnswer
                        ),
                        expected
                    )
                        ? "PASS"
                        : "FAIL",

                expected:
                    `${expected} cm`,

                method:
                    "m-to-cm"
            };
        }


        const metreMatch =
            q.questionText.match(
                /convert\s+(\d+)\s*cm\s+to\s+metres/i
            );


        if (
            metreMatch
        ) {

            const expected =
                Number(
                    metreMatch[1]
                ) /
                100;


            return {
                status:
                    equivalentNumber(
                        number(
                            q.correctAnswer
                        ),
                        expected
                    )
                        ? "PASS"
                        : "FAIL",

                expected:
                    `${expected} m`,

                method:
                    "cm-to-m"
            };
        }


        if (
            /how many centimetres are in 1 metre/i.test(
                q.questionText
            )
        ) {

            return {
                status:
                    answer === "100"
                        ? "PASS"
                        : "FAIL",

                expected:
                    "100",

                method:
                    "m-cm-fact"
            };
        }


        if (
            /how many metres are in 1 kilometre/i.test(
                q.questionText
            )
        ) {

            return {
                status:
                    answer === "1000"
                        ? "PASS"
                        : "FAIL",

                expected:
                    "1000",

                method:
                    "km-m-fact"
            };
        }
    }


    // ========================================================
    // TRIANGLE ANGLE SUM
    // ========================================================

    if (
        skill ===
        "geometry.triangle-angle-sum"
    ) {

        const match =
            q.questionText.match(
                /(\d+)°?\s+and\s+(\d+)°?.*third/i
            );


        if (
            match
        ) {

            const expected =
                180 -
                Number(
                    match[1]
                ) -
                Number(
                    match[2]
                );


            return {
                status:
                    number(
                        q.correctAnswer
                    ) ===
                    expected
                        ? "PASS"
                        : "FAIL",

                expected:
                    `${expected}°`,

                method:
                    "triangle-third-angle"
            };
        }


        const yesNo =
            q.questionText.match(
                /triangle.*angles?\s+(\d+)°.*?(\d+)°.*?(\d+)°/i
            );


        if (
            yesNo
        ) {

            const sum =
                Number(
                    yesNo[1]
                ) +
                Number(
                    yesNo[2]
                ) +
                Number(
                    yesNo[3]
                );


            const expected =
                sum === 180
                    ? "yes"
                    : "no";


            return {
                status:
                    answer === expected
                        ? "PASS"
                        : "FAIL",

                expected,

                method:
                    "triangle-validity"
            };
        }
    }


    // ========================================================
    // COORDINATE POINTS
    // ========================================================

    if (
        skill ===
        "geometry.coordinate-points"
    ) {

        let match =
            q.questionText.match(
                /y-coordinate of the point\s*\(\s*(-?\d+)\s*,\s*(-?\d+)\s*\)/i
            );


        if (
            match
        ) {

            return {
                status:
                    number(
                        q.correctAnswer
                    ) ===
                    Number(
                        match[2]
                    )
                        ? "PASS"
                        : "FAIL",

                expected:
                    match[2],

                method:
                    "coordinate-y"
            };
        }


        match =
            q.questionText.match(
                /x-coordinate of\s*\(\s*(-?\d+)\s*,\s*(-?\d+)\s*\)/i
            );


        if (
            match
        ) {

            return {
                status:
                    number(
                        q.correctAnswer
                    ) ===
                    Number(
                        match[1]
                    )
                        ? "PASS"
                        : "FAIL",

                expected:
                    match[1],

                method:
                    "coordinate-x"
            };
        }
    }


    // ========================================================
    // DEFAULT
    // ========================================================

    return {
        status:
            "MANUAL_REVIEW",

        reason:
            "Pattern not safely machine-verifiable."
    };
}


const bankFiles = [];


function walk(
    directory
) {

    for (
        const entry
        of fs.readdirSync(
            directory,
            {
                withFileTypes:
                    true
            }
        )
    ) {

        const full =
            path.join(
                directory,
                entry.name
            );


        if (
            entry.isDirectory()
        ) {

            walk(
                full
            );

        }
        else if (
            entry.name ===
            "questions.json"
        ) {

            bankFiles.push(
                full
            );
        }
    }
}


walk(
    questionRoot
);


const results = [];


for (
    const file
    of bankFiles
) {

    const bank =
        readJson(
            file
        );


    for (
        const question
        of bank.questions || []
    ) {

        const result =
            classify(
                question
            );


        results.push({

            skillId:
                question.readinessSkillId,

            id:
                question.id,

            question:
                question.questionText,

            answer:
                question.correctAnswer,

            status:
                result.status,

            expected:
                result.expected ??
                null,

            method:
                result.method ??
                null,

            reason:
                result.reason ??
                null
        });
    }
}


const pass =
    results.filter(
        r =>
            r.status ===
            "PASS"
    );

const fail =
    results.filter(
        r =>
            r.status ===
            "FAIL"
    );

const review =
    results.filter(
        r =>
            r.status ===
            "MANUAL_REVIEW"
    );


console.log("");
console.log(
    "============================================================"
);
console.log(
    " STEP 32.61A — EXTENDED MATHEMATICAL AUDIT"
);
console.log(
    "============================================================"
);
console.log("");

console.log(
    `Banks scanned       : ${bankFiles.length}`
);

console.log(
    `Questions scanned   : ${results.length}`
);

console.log(
    `AUTO PASS           : ${pass.length}`
);

console.log(
    `AUTO FAIL           : ${fail.length}`
);

console.log(
    `MANUAL REVIEW       : ${review.length}`
);


console.log("");
console.log(
    "============================================================"
);
console.log(
    "AUTO FAILURES"
);
console.log(
    "============================================================"
);
console.log("");


if (
    fail.length === 0
) {

    console.log(
        "✓ No automatically detected mathematical errors"
    );

}
else {

    for (
        const item
        of fail
    ) {

        console.log(
            `[FAIL] ${item.skillId} | ${item.id}`
        );

        console.log(
            `Q: ${item.question}`
        );

        console.log(
            `A: ${item.answer}`
        );

        console.log(
            `EXPECTED: ${item.expected}`
        );

        console.log(
            `METHOD: ${item.method}`
        );

        console.log("");
    }
}


fs.mkdirSync(
    path.dirname(
        reportFile
    ),
    {
        recursive:
            true
    }
);



console.log("");
console.log(
    "============================================================"
);
console.log(
    "DEGREE-SYMBOL REGRESSION"
);
console.log(
    "============================================================"
);
console.log("");


const degreeRegressionCases = [
    {
        answer:
            "70°",
        expected:
            70
    },
    {
        answer:
            "60°",
        expected:
            60
    },
    {
        answer:
            "50°",
        expected:
            50
    },
    {
        answer:
            "70",
        expected:
            70
    }
];


for (
    const item
    of degreeRegressionCases
) {

    const actual =
        number(
            item.answer
        );


    if (
        actual !==
        item.expected
    ) {

        throw new Error(
            `Degree parsing regression: ${item.answer} -> ${actual}`
        );
    }
}


console.log(
    "✓ Degree-symbol numeric parsing verified"
);

fs.writeFileSync(
    reportFile,
    JSON.stringify(
        {
            step:
                "32.61A",

            generatedAt:
                new Date().toISOString(),

            banks:
                bankFiles.length,

            questions:
                results.length,

            automaticPass:
                pass.length,

            automaticFail:
                fail.length,

            manualReview:
                review.length,

            failures:
                fail,

            reviewQueue:
                review,

            allResults:
                results

        },
        null,
        2
    ) + "\n",
    "utf8"
);


console.log("");
console.log(
    "REPORT:"
);

console.log(
    reportFile
);

console.log("");

