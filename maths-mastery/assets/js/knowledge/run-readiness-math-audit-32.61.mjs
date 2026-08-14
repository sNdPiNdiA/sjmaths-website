import fs from "fs";
import path from "path";

const root = path.resolve(process.cwd(), "maths-mastery");

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
        "readiness-mathematical-audit-32.61.json"
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


function normalizeText(value) {

    return String(value ?? "")
        .replace(/−/g, "-")
        .replace(/×/g, "*")
        .replace(/÷/g, "/")
        .replace(/²/g, "^2")
        .replace(/³/g, "^3")
        .replace(/[–—]/g, "-")
        .trim();
}


function normalizeAnswer(value) {

    return normalizeText(
        value
    )
        .replace(/\s+/g, "")
        .replace(/[₹$]/g, "")
        .replace(/cm²/g, "cm2")
        .replace(/m²/g, "m2")
        .toLowerCase();
}


function approxEqual(a, b) {

    return Math.abs(
        Number(a) - Number(b)
    ) < 1e-9;
}


function fractionToNumber(value) {

    const text =
        normalizeAnswer(
            value
        );


    const match =
        text.match(
            /^(-?\d+(?:\.\d+)?)\/(-?\d+(?:\.\d+)?)$/
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


function numericValue(value) {

    const clean =
        normalizeAnswer(
            value
        );


    if (
        /^-?\d+(?:\.\d+)?$/.test(
            clean
        )
    ) {

        return Number(
            clean
        );
    }


    return fractionToNumber(
        clean
    );
}


function parseList(value) {

    return normalizeAnswer(
        value
    )
        .split(",")
        .map(
            x => x.trim()
        )
        .filter(
            Boolean
        );
}


function sameNumericAnswer(
    actual,
    expected
) {

    const a =
        numericValue(
            actual
        );

    const b =
        numericValue(
            expected
        );


    return (
        a !== null &&
        b !== null &&
        approxEqual(
            a,
            b
        )
    );
}


function divisors(n) {

    const result = [];


    for (
        let i = 1;
        i <= Math.abs(n);
        i++
    ) {

        if (
            Math.abs(n) % i === 0
        ) {

            result.push(
                i
            );
        }
    }


    return result;
}


function positiveMultiples(
    n,
    count
) {

    const result = [];


    for (
        let i = 1;
        i <= count;
        i++
    ) {

        result.push(
            Math.abs(n) * i
        );
    }


    return result;
}


function gcd(
    a,
    b
) {

    a =
        Math.abs(
            a
        );

    b =
        Math.abs(
            b
        );


    while (
        b !== 0
    ) {

        const t = a % b;

        a = b;

        b = t;
    }


    return a;
}


function lcm(
    a,
    b
) {

    return Math.abs(
        a * b
    ) / gcd(
        a,
        b
    );
}


function evaluateKnownQuestion(
    question
) {

    const text =
        normalizeText(
            question.questionText
        );

    const answer =
        normalizeAnswer(
            question.correctAnswer
        );

    const skill =
        question.readinessSkillId;


    // ========================================================
    // SIGN RULES
    // ========================================================

    if (
        skill ===
        "arithmetic.sign-rules"
    ) {

        if (
            /one factor is negative.*other factor is positive/i
                .test(text)
        ) {

            return {
                status:
                    answer ===
                    "negative"
                        ? "PASS"
                        : "FAIL",
                expected:
                    "negative",
                method:
                    "sign-rule"
            };
        }


        const match =
            text.match(
                /(-?\d+)\s*\*\s*(-?\d+)/
            );


        if (
            match
        ) {

            const expected =
                Math.sign(
                    Number(match[1]) *
                    Number(match[2])
                );


            const expectedText =
                expected < 0
                    ? "negative"
                    : expected > 0
                        ? "positive"
                        : "zero";


            return {
                status:
                    answer === expectedText
                        ? "PASS"
                        : "FAIL",
                expected:
                    expectedText,
                method:
                    "numeric-sign"
            };
        }
    }


    // ========================================================
    // FACTORS
    // ========================================================

    if (
        skill ===
        "arithmetic.factors"
    ) {

        const match =
            text.match(
                /factors of\s+(\d+)/i
            );


        if (
            match &&
            /all positive factors/i.test(text)
        ) {

            const expected =
                divisors(
                    Number(
                        match[1]
                    )
                )
                    .join(",");


            return {
                status:
                    normalizeAnswer(
                        answer
                    ) ===
                    expected
                        ? "PASS"
                        : "FAIL",
                expected,
                method:
                    "factor-enumeration"
            };
        }
    }


    // ========================================================
    // MULTIPLES
    // ========================================================

    if (
        skill ===
        "arithmetic.multiples"
    ) {

        const match =
            text.match(
                /first\s+five\s+positive multiples of\s+(\d+)/i
            );


        if (
            match
        ) {

            const expected =
                positiveMultiples(
                    Number(
                        match[1]
                    ),
                    5
                ).join(",");


            return {
                status:
                    normalizeAnswer(
                        answer
                    ) === expected
                        ? "PASS"
                        : "FAIL",
                expected,
                method:
                    "multiple-generation"
            };
        }


        const thirdMatch =
            text.match(
                /third\s+positive multiple of\s+(\d+)/i
            );


        if (
            thirdMatch
        ) {

            const expected =
                Number(
                    thirdMatch[1]
                ) * 3;


            return {
                status:
                    sameNumericAnswer(
                        answer,
                        expected
                    )
                        ? "PASS"
                        : "FAIL",
                expected:
                    String(expected),
                method:
                    "multiple-position"
            };
        }
    }


    // ========================================================
    // HCF / GCF
    // ========================================================

    if (
        skill ===
        "arithmetic.hcf"
    ) {

        const match =
            text.match(
                /(?:HCF|GCF).*?(\d+).*?(\d+)/i
            );


        if (
            match
        ) {

            const expected =
                gcd(
                    Number(match[1]),
                    Number(match[2])
                );


            return {
                status:
                    sameNumericAnswer(
                        answer,
                        expected
                    )
                        ? "PASS"
                        : "FAIL",
                expected:
                    String(expected),
                method:
                    "gcd"
            };
        }
    }


    // ========================================================
    // LCM
    // ========================================================

    if (
        skill ===
        "arithmetic.lcm"
    ) {

        const match =
            text.match(
                /LCM of\s+(\d+)\s+and\s+(\d+)/i
            );


        if (
            match
        ) {

            const expected =
                lcm(
                    Number(match[1]),
                    Number(match[2])
                );


            return {
                status:
                    sameNumericAnswer(
                        answer,
                        expected
                    )
                        ? "PASS"
                        : "FAIL",
                expected:
                    String(expected),
                method:
                    "lcm"
            };
        }
    }


    // ========================================================
    // INTEGER ARITHMETIC
    // ========================================================

    const arithmeticMatch =
        text.match(
            /(?:simplify:?\s*)?(-?\d+)\s*([+\-*\/])\s*(-?\d+)/i
        );


    if (
        arithmeticMatch &&
        [
            "arithmetic.add-integers",
            "arithmetic.multiply-integers",
            "arithmetic.divide-integers"
        ].includes(skill)
    ) {

        const a =
            Number(
                arithmeticMatch[1]
            );

        const op =
            arithmeticMatch[2];

        const b =
            Number(
                arithmeticMatch[3]
            );


        let expected;


        if (
            op === "+"
        ) {

            expected =
                a + b;

        }
        else if (
            op === "-"
        ) {

            expected =
                a - b;

        }
        else if (
            op === "*"
        ) {

            expected =
                a * b;

        }
        else {

            if (
                b === 0
            ) {

                return {
                    status:
                        "MANUAL_REVIEW",
                    reason:
                        "Division by zero pattern."
                };
            }


            expected =
                a / b;
        }


        return {
            status:
                sameNumericAnswer(
                    answer,
                    expected
                )
                    ? "PASS"
                    : "FAIL",
            expected:
                String(expected),
            method:
                "integer-arithmetic"
        };
    }


    // ========================================================
    // FRACTION ARITHMETIC
    // ========================================================

    const fractionOp =
        text.match(
            /(-?\d+)\/(\d+)\s*([+\-*\/])\s*(-?\d+)\/(\d+)/i
        );


    if (
        fractionOp &&
        [
            "fractions.add",
            "fractions.subtract",
            "fractions.multiply",
            "fractions.divide"
        ].includes(skill)
    ) {

        const a =
            Number(fractionOp[1]) /
            Number(fractionOp[2]);

        const b =
            Number(fractionOp[4]) /
            Number(fractionOp[5]);

        const op =
            fractionOp[3];


        let expected;


        if (op === "+") {
            expected = a + b;
        }
        else if (op === "-") {
            expected = a - b;
        }
        else if (op === "*") {
            expected = a * b;
        }
        else {

            if (
                b === 0
            ) {

                return {
                    status:
                        "MANUAL_REVIEW",
                    reason:
                        "Fraction division by zero."
                };
            }

            expected = a / b;
        }


        const actual =
            numericValue(
                answer
            );


        return {
            status:
                actual !== null &&
                approxEqual(
                    actual,
                    expected
                )
                    ? "PASS"
                    : "FAIL",
            expected:
                String(expected),
            method:
                "fraction-arithmetic"
        };
    }


    // ========================================================
    // PERCENTAGE
    // ========================================================

    const percentMatch =
        text.match(
            /(\d+)%\s+of\s+(\d+(?:\.\d+)?)/i
        );


    if (
        percentMatch &&
        skill ===
        "percentage.basic"
    ) {

        const expected =
            Number(
                percentMatch[1]
            ) /
            100 *
            Number(
                percentMatch[2]
            );


        return {
            status:
                sameNumericAnswer(
                    answer,
                    expected
                )
                    ? "PASS"
                    : "FAIL",
            expected:
                String(expected),
            method:
                "percentage"
        };
    }


    // ========================================================
    // TRIANGLE ANGLE SUM
    // ========================================================

    const triangleMatch =
        text.match(
            /triangle.*angles?\s+(\d+)°?\s+and\s+(\d+)°?.*third/i
        );


    if (
        triangleMatch &&
        skill ===
        "geometry.triangle-angle-sum"
    ) {

        const expected =
            180 -
            Number(
                triangleMatch[1]
            ) -
            Number(
                triangleMatch[2]
            );


        return {
            status:
                normalizeAnswer(
                    answer
                ).replace(
                    "°",
                    ""
                ) ===
                String(expected)
                    ? "PASS"
                    : "FAIL",
            expected:
                `${expected}°`,
            method:
                "triangle-angle-sum"
        };
    }


    // ========================================================
    // COORDINATE POINTS
    // ========================================================

    const pointMatch =
        text.match(
            /x-coordinate of the point\s*\(\s*(-?\d+)\s*,\s*(-?\d+)\s*\)/i
        );


    if (
        pointMatch &&
        skill ===
        "geometry.coordinate-points"
    ) {

        const expected =
            Number(
                pointMatch[1]
            );


        return {
            status:
                sameNumericAnswer(
                    answer,
                    expected
                )
                    ? "PASS"
                    : "FAIL",
            expected:
                String(expected),
            method:
                "coordinate-x"
        };
    }


    // ========================================================
    // COORDINATE DISTANCE
    // ========================================================

    const distanceMatch =
        text.match(
            /distance between\s*\(\s*(-?\d+)\s*,\s*(-?\d+)\s*\)\s*and\s*\(\s*(-?\d+)\s*,\s*(-?\d+)\s*\)/i
        );


    if (
        distanceMatch
    ) {

        const x1 =
            Number(distanceMatch[1]);

        const y1 =
            Number(distanceMatch[2]);

        const x2 =
            Number(distanceMatch[3]);

        const y2 =
            Number(distanceMatch[4]);


        const expected =
            Math.sqrt(
                (
                    x2 - x1
                ) ** 2 +
                (
                    y2 - y1
                ) ** 2
            );


        return {
            status:
                sameNumericAnswer(
                    answer,
                    expected
                )
                    ? "PASS"
                    : "FAIL",
            expected:
                String(expected),
            method:
                "distance-formula"
        };
    }


    // ========================================================
    // QUADRATIC ROOTS
    // ========================================================

    const quadraticMatch =
        text.match(
            /x²\s*-\s*(\d+)x\s*\+\s*(\d+)\s*=\s*0/i
        );


    if (
        quadraticMatch &&
        skill ===
        "quadratic.roots"
    ) {

        const sum =
            Number(
                quadraticMatch[1]
            );

        const product =
            Number(
                quadraticMatch[2]
            );


        const roots = [];


        for (
            let a = -50;
            a <= 50;
            a++
        ) {

            for (
                let b = -50;
                b <= 50;
                b++
            ) {

                if (
                    a + b === sum &&
                    a * b === product
                ) {

                    roots.push(
                        Math.min(a, b),
                        Math.max(a, b)
                    );

                    a = 51;
                    break;
                }
            }
        }


        if (
            roots.length === 2
        ) {

            const expected =
                `${roots[0]},${roots[1]}`;


            return {
                status:
                    normalizeAnswer(
                        answer
                    ) === expected
                        ? "PASS"
                        : "FAIL",
                expected,
                method:
                    "quadratic-roots"
            };
        }
    }


    // ========================================================
    // QUADRATIC FACTORISATION
    // ========================================================

    const factorQuadMatch =
        text.match(
            /factor\s+x²\s*\+\s*(\d+)x\s*\+\s*(\d+)/i
        );


    if (
        factorQuadMatch &&
        (
            skill ===
            "quadratic.factorisation" ||
            skill ===
            "algebra.factor-quadratic"
        )
    ) {

        const b =
            Number(
                factorQuadMatch[1]
            );

        const c =
            Number(
                factorQuadMatch[2]
            );


        let expected = null;


        for (
            let a = 1;
            a <= Math.abs(c);
            a++
        ) {

            if (
                c % a !== 0
            ) {
                continue;
            }


            const d =
                c / a;


            if (
                a + d === b
            ) {

                expected =
                    `(x+${a})(x+${d})`;

                break;
            }
        }


        if (
            expected
        ) {

            const actual =
                answer
                    .replace(
                        /\s+/g,
                        ""
                    );


            const reverse =
                expected.replace(
                    `(x+${a})(x+${d})`,
                    `(x+${d})(x+${a})`
                );


            return {
                status:
                    actual === expected ||
                    actual === reverse
                        ? "PASS"
                        : "FAIL",
                expected,
                method:
                    "quadratic-factorisation"
            };
        }
    }


    // ========================================================
    // AREA OF RECTANGLE / SQUARE
    // ========================================================

    const rectangleArea =
        text.match(
            /area of a rectangle\s+(\d+)\s*cm\s*by\s*(\d+)\s*cm/i
        );


    if (
        rectangleArea &&
        skill ===
        "measurement.area"
    ) {

        const expected =
            Number(
                rectangleArea[1]
            ) *
            Number(
                rectangleArea[2]
            );


        const actual =
            numericValue(
                answer
            );


        return {
            status:
                actual !== null &&
                approxEqual(
                    actual,
                    expected
                )
                    ? "PASS"
                    : "FAIL",
            expected:
                `${expected} cm²`,
            method:
                "rectangle-area"
        };
    }


    // ========================================================
    // AREA SQUARE
    // ========================================================

    const squareArea =
        text.match(
            /area of a square(?: with side)?\s*(\d+)\s*cm/i
        );


    if (
        squareArea &&
        skill ===
        "measurement.area"
    ) {

        const side =
            Number(
                squareArea[1]
            );


        const expected =
            side * side;


        const actual =
            numericValue(
                answer
            );


        return {
            status:
                actual !== null &&
                approxEqual(
                    actual,
                    expected
                )
                    ? "PASS"
                    : "FAIL",
            expected:
                `${expected} cm²`,
            method:
                "square-area"
        };
    }


    // ========================================================
    // PERIMETER RECTANGLE
    // ========================================================

    const rectanglePerimeter =
        text.match(
            /perimeter of a rectangle\s+(\d+)\s*cm\s*by\s*(\d+)\s*cm/i
        );


    if (
        rectanglePerimeter &&
        skill ===
        "measurement.perimeter"
    ) {

        const l =
            Number(
                rectanglePerimeter[1]
            );

        const w =
            Number(
                rectanglePerimeter[2]
            );


        const expected =
            2 * (
                l + w
            );


        const actual =
            numericValue(
                answer
            );


        return {
            status:
                actual !== null &&
                approxEqual(
                    actual,
                    expected
                )
                    ? "PASS"
                    : "FAIL",
            expected:
                `${expected} cm`,
            method:
                "rectangle-perimeter"
        };
    }


    // ========================================================
    // CIRCLE
    // ========================================================

    const circleArea =
        text.match(
            /area.*r\s*=\s*(\d+)\s*cm.*22\/7/i
        );


    if (
        circleArea &&
        skill ===
        "mensuration.circle"
    ) {

        const r =
            Number(
                circleArea[1]
            );


        const expected =
            (
                22 /
                7
            ) *
            r *
            r;


        return {
            status:
                sameNumericAnswer(
                    answer,
                    expected
                )
                    ? "PASS"
                    : "FAIL",
            expected:
                `${expected} cm²`,
            method:
                "circle-area"
        };
    }


    const circumference =
        text.match(
            /circumference.*r\s*=\s*(\d+)\s*cm.*22\/7/i
        );


    if (
        circumference &&
        skill ===
        "mensuration.circle"
    ) {

        const r =
            Number(
                circumference[1]
            );


        const expected =
            2 *
            (
                22 /
                7
            ) *
            r;


        return {
            status:
                sameNumericAnswer(
                    answer,
                    expected
                )
                    ? "PASS"
                    : "FAIL",
            expected:
                `${expected} cm`,
            method:
                "circle-circumference"
        };
    }


    // ========================================================
    // MEAN
    // ========================================================

    const meanOf =
        text.match(
            /mean of\s+(.+?)(?:\.|$)/i
        );


    if (
        meanOf &&
        skill ===
        "data.mean"
    ) {

        const values =
            meanOf[1]
                .split(",")
                .map(
                    x =>
                        Number(
                            x.trim()
                        )
                );


        if (
            values.every(
                Number.isFinite
            )
        ) {

            const expected =
                values.reduce(
                    (
                        sum,
                        x
                    ) =>
                        sum + x,
                    0
                ) /
                values.length;


            return {
                status:
                    sameNumericAnswer(
                        answer,
                        expected
                    )
                        ? "PASS"
                        : "FAIL",
                expected:
                    String(expected),
                method:
                    "mean"
            };
        }
    }


    // ========================================================
    // MEDIAN
    // ========================================================

    const medianOf =
        text.match(
            /median of\s+(.+?)(?:\.|$)/i
        );


    if (
        medianOf &&
        skill ===
        "data.median"
    ) {

        const values =
            medianOf[1]
                .split(",")
                .map(
                    x =>
                        Number(
                            x.trim()
                        )
                )
                .sort(
                    (
                        a,
                        b
                    ) =>
                        a - b
                );


        if (
            values.every(
                Number.isFinite
            )
        ) {

            const middle =
                Math.floor(
                    values.length / 2
                );


            const expected =
                values.length % 2 === 1
                    ? values[middle]
                    : (
                        values[middle - 1] +
                        values[middle]
                    ) / 2;


            return {
                status:
                    sameNumericAnswer(
                        answer,
                        expected
                    )
                        ? "PASS"
                        : "FAIL",
                expected:
                    String(expected),
                method:
                    "median"
            };
        }
    }


    // ========================================================
    // MODE
    // ========================================================

    const modeOf =
        text.match(
            /mode of\s+(.+?)(?:\.|$)/i
        );


    if (
        modeOf &&
        skill ===
        "data.mode"
    ) {

        const values =
            modeOf[1]
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


        const max =
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
                        count === max
                )
                .map(
                    (
                        [value]
                    ) =>
                        value
                )
                .sort();


        const expected =
            max === 1
                ? "no mode"
                : modes.join(
                    " and "
                );


        return {
            status:
                normalizeAnswer(
                    answer
                ) ===
                normalizeAnswer(
                    expected
                )
                    ? "PASS"
                    : "FAIL",
            expected,
            method:
                "mode"
        };
    }


    // ========================================================
    // DEFAULT
    // ========================================================

    return {
        status:
            "MANUAL_REVIEW",
        reason:
            "Question pattern not safely machine-verifiable."
    };
}


const files =
    fs.readdirSync(
        questionRoot,
        {
            withFileTypes:
                true
        }
    );


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
            entry.isFile() &&
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

const counts = {
    PASS: 0,
    FAIL: 0,
    MANUAL_REVIEW: 0
};


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
            evaluateKnownQuestion(
                question
            );


        counts[
            result.status
        ]++;


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
                null,

            file

        });
    }
}


const failures =
    results.filter(
        x =>
            x.status ===
            "FAIL"
    );


const manualReview =
    results.filter(
        x =>
            x.status ===
            "MANUAL_REVIEW"
    );


console.log("");
console.log(
    "============================================================"
);
console.log(
    " STEP 32.61 — MATHEMATICAL CORRECTNESS AUDIT"
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
    `AUTO PASS           : ${counts.PASS}`
);

console.log(
    `AUTO FAIL           : ${counts.FAIL}`
);

console.log(
    `MANUAL REVIEW       : ${counts.MANUAL_REVIEW}`
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
    failures.length === 0
) {

    console.log(
        "✓ No automatically detected mathematical errors"
    );

}
else {

    for (
        const item
        of failures
    ) {

        console.log(
            `[FAIL] ${item.skillId} | ${item.id}`
        );

        console.log(
            `       Q: ${item.question}`
        );

        console.log(
            `       A: ${item.answer}`
        );

        console.log(
            `       EXPECTED: ${item.expected}`
        );

        console.log(
            `       METHOD: ${item.method}`
        );

        console.log("");
    }
}


console.log(
    "============================================================"
);
console.log(
    "MANUAL REVIEW QUEUE"
);
console.log(
    "============================================================"
);
console.log("");


for (
    const item
    of manualReview
) {

    console.log(
        `[REVIEW] ${item.skillId} | ${item.id}`
    );

    console.log(
        `         Q: ${item.question}`
    );

    console.log(
        `         A: ${item.answer}`
    );

    console.log(
        `         REASON: ${item.reason}`
    );

    console.log("");
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


fs.writeFileSync(
    reportFile,
    JSON.stringify(
        {
            step:
                "32.61",

            generatedAt:
                new Date().toISOString(),

            banks:
                bankFiles.length,

            questions:
                results.length,

            counts,

            automaticFailures:
                failures,

            manualReview,

            results

        },
        null,
        2
    ) + "\n",
    "utf8"
);


console.log(
    "============================================================"
);

console.log(
    "REPORT:"
);

console.log(
    reportFile
);

console.log(
    "============================================================"
);
