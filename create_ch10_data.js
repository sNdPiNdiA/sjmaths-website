const fs = require('fs');

const data = {
    "chapter": 10,
    "title": "Circles",
    "class": 10,
    "concepts": [
        {
            "id": "tangent-properties",
            "title": "Tangent to a Circle",
            "icon": "⭕",
            "precheck": {
                "question": "A tangent to a circle is a line that touches the circle at exactly ______ point(s).",
                "options": ["One", "Two", "Three", "Zero"],
                "correctIndex": 0,
                "passMessage": "Correct! A tangent touches the circle at exactly one point, called the point of tangency (or point of contact).",
                "failMessage": "A tangent is a line that touches the circle at exactly ONE point. This point is called the point of contact."
            },
            "learn": {
                "paragraphs": [
                    "A **tangent** to a circle is a line that intersects (touches) the circle at exactly **one point**. This point is called the **point of contact** or **point of tangency**.",
                    "**Theorem 1**: The tangent at any point of a circle is **perpendicular** to the radius through the point of contact. That is, if \\(OA\\) is a radius and \\(PA\\) is a tangent at \\(A\\), then \\(OA \\perp PA\\).",
                    "**Theorem 2** (Converse): A line drawn through the end of a radius and perpendicular to it is a tangent to the circle.",
                    "These two theorems are the foundation of almost every circle problem in the board exam. They create a **right angle** at the point of contact, which lets us use the Pythagorean theorem."
                ],
                "formulas": [
                    {
                        "rule": "Tangent ⊥ Radius",
                        "formula": "If PA is tangent at A, then OA ⊥ PA",
                        "example": "OA = 5cm, OP = 13cm → PA = √(169−25) = 12cm"
                    },
                    {
                        "rule": "Tangent Length",
                        "formula": "PA = √(OP² − OA²)",
                        "example": "Centre O, external point P, radius r, OP = d → tangent = √(d²−r²)"
                    }
                ],
                "boxes": [
                    {
                        "type": "success",
                        "html": "<strong>Key Properties of a Tangent:</strong><br>• Tangent ⊥ Radius at point of contact<br>• The perpendicular from centre to tangent passes through point of contact<br>• A tangent never enters the interior of the circle"
                    },
                    {
                        "type": "warning",
                        "html": "<strong>Common Mistake:</strong> Students confuse tangent with secant. A <strong>secant</strong> intersects a circle at TWO points. A <strong>tangent</strong> touches at exactly ONE point."
                    },
                    {
                        "type": "info",
                        "html": "<strong>Number of Tangents:</strong><br>• From a point <em>inside</em> the circle → <strong>0</strong> tangents<br>• From a point <em>on</em> the circle → <strong>1</strong> tangent<br>• From a point <em>outside</em> the circle → <strong>2</strong> tangents (equal in length!)"
                    }
                ]
            },
            "practice": [
                {
                    "question": "If a line is tangent to a circle of radius 5 cm at point A, and O is the centre, what is the angle \\(\\angle OAP\\) where P is any point on the tangent?",
                    "options": ["90°", "60°", "45°", "180°"],
                    "correctIndex": 0,
                    "solution": "<p>By the theorem: tangent ⊥ radius at point of contact.</p><p>So \\(\\angle OAP = 90°\\).</p>"
                },
                {
                    "question": "From a point P, 13 cm away from the centre of a circle of radius 5 cm, a tangent is drawn. Find the length of the tangent.",
                    "options": ["12 cm", "8 cm", "10 cm", "√194 cm"],
                    "correctIndex": 0,
                    "solution": "<p>In right \\(\\triangle OAP\\) (right angle at A):</p><p>\\(PA = \\sqrt{OP^2 - OA^2} = \\sqrt{169 - 25} = \\sqrt{144} = 12\\) cm.</p>"
                },
                {
                    "question": "A tangent PQ at point P of a circle of radius 5 cm meets a line through the centre O at point Q so that \\(OQ = 12\\) cm. Find the length PQ.",
                    "options": ["√119 cm", "7 cm", "13 cm", "√169 cm"],
                    "correctIndex": 0,
                    "solution": "<p>\\(PQ = \\sqrt{OQ^2 - OP^2} = \\sqrt{144 - 25} = \\sqrt{119}\\) cm.</p>"
                },
                {
                    "question": "If the tangent at point P to the circle with centre O makes an angle of \\(50°\\) with OP extended, find \\(\\angle OPT\\) where T is on the tangent.",
                    "options": ["90°", "50°", "40°", "130°"],
                    "correctIndex": 0,
                    "solution": "<p>The tangent is always perpendicular to the radius at the point of contact.</p><p>So \\(\\angle OPT = 90°\\) regardless of any other angle.</p>"
                },
                {
                    "question": "How many tangents can be drawn to a circle from a point lying inside the circle?",
                    "options": ["0", "1", "2", "Infinite"],
                    "correctIndex": 0,
                    "solution": "<p>No tangent can be drawn from a point inside the circle, as any line through an interior point will intersect the circle at two points (it becomes a secant).</p>"
                },
                {
                    "question": "In the figure, if TP and TQ are two tangents from T to a circle with centre O, and \\(\\angle PTQ = 70°\\), find \\(\\angle POQ\\).",
                    "options": ["110°", "70°", "140°", "90°"],
                    "correctIndex": 0,
                    "solution": "<p>In quadrilateral OPTQ: \\(\\angle OPT = 90°\\), \\(\\angle OQT = 90°\\).</p><p>Sum of angles = 360°: \\(90° + 90° + 70° + \\angle POQ = 360°\\).</p><p>\\(\\angle POQ = 110°\\).</p>"
                },
                {
                    "question": "Prove that the tangents drawn at the ends of a diameter of a circle are parallel.",
                    "options": ["True — both are ⊥ to the diameter, hence parallel", "False", "Only for large circles", "Cannot be determined"],
                    "correctIndex": 0,
                    "solution": "<p>Let AB be a diameter. Tangent at A ⊥ OA, tangent at B ⊥ OB.</p><p>Since OA and OB are the same line (diameter), both tangents are perpendicular to the same line.</p><p>Two lines perpendicular to the same line are parallel. ✓</p>"
                },
                {
                    "question": "If the angle between two tangents drawn from an external point to a circle of radius \\(r\\) is \\(60°\\), find the length of each tangent.",
                    "options": ["r√3", "r", "2r", "r/√3"],
                    "correctIndex": 0,
                    "solution": "<p>Let O be centre, P be external point. \\(\\angle TPT' = 60°\\).</p><p>Then \\(\\angle TPO = 30°\\) (by symmetry, OP bisects the angle).</p><p>In right \\(\\triangle OTP\\): \\(\\tan 30° = \\frac{OT}{PT} = \\frac{r}{PT}\\).</p><p>\\(PT = \\frac{r}{\\tan 30°} = \\frac{r}{1/\\sqrt{3}} = r\\sqrt{3}\\).</p>"
                }
            ],
            "pyq": [
                {
                    "question": "[2024] In the given figure, from an external point P, two tangents PA and PB are drawn to a circle with centre O. If \\(\\angle APB = 40°\\), find \\(\\angle AOB\\).",
                    "options": ["140°", "40°", "80°", "100°"],
                    "correctIndex": 0,
                    "solution": "<p>In quadrilateral OAPB: \\(\\angle OAP = \\angle OBP = 90°\\).</p><p>\\(\\angle AOB = 360° - 90° - 90° - 40° = 140°\\).</p>"
                },
                {
                    "question": "[2023] Prove that the length of tangents drawn from an external point to a circle are equal.",
                    "options": ["True — by RHS congruence of △OAP and △OBP", "True — by SSS only", "False", "True — by ASA"],
                    "correctIndex": 0,
                    "solution": "<p>In \\(\\triangle OAP\\) and \\(\\triangle OBP\\):</p><p>• \\(OA = OB\\) (radii)</p><p>• \\(OP = OP\\) (common)</p><p>• \\(\\angle OAP = \\angle OBP = 90°\\) (tangent ⊥ radius)</p><p>By RHS congruence: \\(\\triangle OAP \\cong \\triangle OBP\\).</p><p>Therefore \\(PA = PB\\) (CPCT). ✓</p>"
                },
                {
                    "question": "[2022] Two tangents TP and TQ are drawn to a circle with centre O from an external point T. Prove that \\(\\angle PTQ = 2\\angle OPQ\\).",
                    "options": ["True — using isosceles △OPQ and angle sum", "False", "Only when TP=TQ", "Only for unit circle"],
                    "correctIndex": 0,
                    "solution": "<p>Since TP = TQ (tangent lengths equal), \\(\\triangle TPQ\\) is isosceles.</p><p>Let \\(\\angle TPQ = \\alpha\\). Then \\(\\angle TQP = \\alpha\\) and \\(\\angle PTQ = 180° - 2\\alpha\\).</p><p>Now \\(\\angle OPT = 90°\\), so \\(\\angle OPQ = 90° - \\alpha\\).</p><p>\\(2\\angle OPQ = 180° - 2\\alpha = \\angle PTQ\\). ✓</p>"
                },
                {
                    "question": "[2020] If a circle touches all four sides of a quadrilateral ABCD, prove that \\(AB + CD = BC + DA\\).",
                    "options": ["True — using equal tangent lengths from each vertex", "False", "Only for squares", "Only for rhombus"],
                    "correctIndex": 0,
                    "solution": "<p>Let the circle touch AB at P, BC at Q, CD at R, DA at S.</p><p>By equal tangent lengths: AP=AS, BP=BQ, CQ=CR, DR=DS.</p><p>\\(AB + CD = (AP+PB) + (CR+RD)\\)</p><p>\\(= (AS+BQ) + (CQ+DS)\\)</p><p>\\(= (AS+DS) + (BQ+CQ) = DA + BC\\). ✓</p>"
                },
                {
                    "question": "[2019] In the figure, XY and X'Y' are two parallel tangents to a circle with centre O and another tangent AB with point of contact C, intersecting XY at A and X'Y' at B. Prove that \\(\\angle AOB = 90°\\).",
                    "options": ["True — using tangent properties and angle sums", "False", "Only for specific radii", "Cannot determine"],
                    "correctIndex": 0,
                    "solution": "<p>Join OC. \\(\\angle OAP = \\angle OAC\\) (OA bisects \\(\\angle PAC\\), as tangent lengths from A are equal).</p><p>Similarly \\(\\angle OBQ = \\angle OBC\\).</p><p>Since XY \\(\\parallel\\) X'Y': \\(\\angle PAC + \\angle QBC = 180°\\) (co-interior angles).</p><p>So \\(2\\angle OAC + 2\\angle OBC = 180° \\Rightarrow \\angle OAC + \\angle OBC = 90°\\).</p><p>In \\(\\triangle AOB\\): \\(\\angle AOB = 180° - (\\angle OAC + \\angle OBC) = 90°\\). ✓</p>"
                }
            ],
            "test": [
                {
                    "question": "From an external point P, tangents PA and PB are drawn to a circle with centre O. If \\(PA = 8\\) cm and \\(OP = 10\\) cm, find the radius of the circle.",
                    "options": ["6 cm", "8 cm", "12 cm", "5 cm"],
                    "correctIndex": 0,
                    "solution": "<p>In right \\(\\triangle OAP\\): \\(OA = \\sqrt{OP^2 - PA^2} = \\sqrt{100-64} = \\sqrt{36} = 6\\) cm.</p>"
                },
                {
                    "question": "PQ is a tangent to a circle with centre O at the point P. If \\(\\triangle OPQ\\) is an isosceles triangle, then find \\(\\angle OQP\\).",
                    "options": ["45°", "90°", "60°", "30°"],
                    "correctIndex": 0,
                    "solution": "<p>\\(\\angle OPQ = 90°\\) (tangent ⊥ radius). If \\(\\triangle OPQ\\) is isosceles with \\(OP = PQ\\):</p><p>\\(\\angle OQP = \\angle QOP = \\frac{180°-90°}{2} = 45°\\).</p>"
                }
            ]
        },
        {
            "id": "tangent-lengths-theorems",
            "title": "Equal Tangent Lengths & Applications",
            "icon": "✂️",
            "precheck": {
                "question": "Two tangents PA and PB are drawn from an external point P to a circle. What can be said about PA and PB?",
                "options": ["PA = PB (equal in length)", "PA > PB always", "PA < PB always", "No relationship"],
                "correctIndex": 0,
                "passMessage": "Correct! Tangents from an external point are always equal in length. This is one of the most important theorems!",
                "failMessage": "The tangent lengths from an external point to a circle are ALWAYS equal. PA = PB. This follows from the RHS congruence of the two triangles formed."
            },
            "learn": {
                "paragraphs": [
                    "**Theorem**: The lengths of tangents drawn from an **external point** to a circle are **equal**. If PA and PB are tangents from P to a circle with centre O, then \\(PA = PB\\).",
                    "**Proof**: In \\(\\triangle OPA\\) and \\(\\triangle OPB\\): OA = OB (radii), OP = OP (common), \\(\\angle OAP = \\angle OBP = 90°\\). By RHS, \\(\\triangle OPA \\cong \\triangle OPB\\). Hence PA = PB (CPCT).",
                    "This theorem has powerful **applications**: (1) Tangent from vertex of circumscribed polygon, (2) Proving \\(AB+CD = BC+DA\\) for a quadrilateral circumscribing a circle, (3) Finding unknown tangent lengths.",
                    "Also: OP bisects \\(\\angle APB\\) and OP bisects chord AB perpendicularly."
                ],
                "formulas": [
                    {
                        "rule": "Equal Tangent Lengths",
                        "formula": "PA = PB (tangents from external point P)",
                        "example": "If PA = 8cm then PB = 8cm automatically"
                    },
                    {
                        "rule": "Circumscribed Quadrilateral",
                        "formula": "AB + CD = BC + DA",
                        "example": "If AB=6, BC=7, CD=4 → DA = 6+4−7 = 3"
                    },
                    {
                        "rule": "Angle between tangents",
                        "formula": "∠APB + ∠AOB = 180°",
                        "example": "If ∠APB = 50° then ∠AOB = 130°"
                    }
                ],
                "boxes": [
                    {
                        "type": "success",
                        "html": "<strong>Tangent from each vertex (circumscribed polygon):</strong> Label the tangent lengths from each vertex. From vertex A: if tangent touches at P and S, then AP = AS. This gives a system of equations to solve for unknowns."
                    },
                    {
                        "type": "info",
                        "html": "<strong>Incircle of a Triangle:</strong> If a circle is inscribed in \\(\\triangle ABC\\) with sides a, b, c: the tangent lengths from each vertex are \\(s-a\\), \\(s-b\\), \\(s-c\\) where \\(s = \\frac{a+b+c}{2}\\) (semi-perimeter)."
                    },
                    {
                        "type": "warning",
                        "html": "<strong>Board Exam Alert:</strong> The proof of 'equal tangent lengths' is a frequently asked 3-mark question. Memorise the RHS congruence proof with all steps clearly written."
                    }
                ]
            },
            "practice": [
                {
                    "question": "In the figure, a circle is inscribed in \\(\\triangle ABC\\) with AB = 12 cm, BC = 8 cm, AC = 10 cm. Find the lengths AD, BE, CF where D, E, F are points of contact on BC, CA, AB respectively.",
                    "options": ["AD=7, BE=5, CF=3", "AD=5, BE=3, CF=7", "AD=3, BE=7, CF=5", "AD=7, BE=3, CF=5"],
                    "correctIndex": 3,
                    "solution": "<p>Let AF = AE = x, BF = BD = y, CD = CE = z.</p><p>AB: x+y = 12 ...(1)</p><p>BC: y+z = 8 ...(2)</p><p>AC: x+z = 10 ...(3)</p><p>Adding all: 2(x+y+z) = 30, so x+y+z = 15.</p><p>From (1): z = 15-12 = 3. From (2): x = 15-8 = 7. From (3): y = 15-10 = 5.</p><p>AD = x = 7, BE = y = 5, CF = z = 3.</p>"
                },
                {
                    "question": "A circle is inscribed in a quadrilateral ABCD where AB = 6 cm, BC = 7 cm, CD = 4 cm. Find AD.",
                    "options": ["3 cm", "5 cm", "4 cm", "6 cm"],
                    "correctIndex": 0,
                    "solution": "<p>For a circumscribed quadrilateral: AB + CD = BC + AD.</p><p>6 + 4 = 7 + AD → AD = 3 cm.</p>"
                },
                {
                    "question": "Two concentric circles of radii 5 cm and 3 cm have centre O. A chord of the larger circle touches the smaller circle. Find the length of the chord.",
                    "options": ["8 cm", "6 cm", "4 cm", "10 cm"],
                    "correctIndex": 0,
                    "solution": "<p>The chord of the larger circle is tangent to the smaller circle. The perpendicular from O to the chord = radius of smaller circle = 3 cm.</p><p>Half-chord = \\(\\sqrt{5^2 - 3^2} = \\sqrt{16} = 4\\) cm.</p><p>Full chord = 2 × 4 = 8 cm.</p>"
                },
                {
                    "question": "PA and PB are tangents from P to a circle with centre O such that \\(\\angle APB = 80°\\). Find \\(\\angle POA\\).",
                    "options": ["50°", "80°", "40°", "100°"],
                    "correctIndex": 0,
                    "solution": "<p>Since OP bisects \\(\\angle APB\\): \\(\\angle APO = 40°\\).</p><p>In right \\(\\triangle OAP\\): \\(\\angle POA = 90° - 40° = 50°\\).</p>"
                },
                {
                    "question": "Prove that the parallelogram circumscribing a circle is a rhombus.",
                    "options": ["True — AB+CD = BC+DA and AB=CD, BC=DA → all sides equal", "False", "Only for squares", "Cannot determine"],
                    "correctIndex": 0,
                    "solution": "<p>Let ABCD be a parallelogram circumscribing a circle.</p><p>By circumscribed property: AB + CD = BC + DA.</p><p>Since ABCD is a parallelogram: AB = CD and BC = DA.</p><p>So 2AB = 2BC → AB = BC.</p><p>All sides are equal → ABCD is a rhombus. ✓</p>"
                },
                {
                    "question": "In the figure, a triangle ABC is drawn to circumscribe a circle of radius 4 cm such that BD = 8 cm and DC = 6 cm. Find the sides AB and AC. (Given: area of \\(\\triangle ABC = 84\\) cm²)",
                    "options": ["AB=15 cm, AC=13 cm", "AB=13 cm, AC=15 cm", "AB=14 cm, AC=14 cm", "AB=12 cm, AC=16 cm"],
                    "correctIndex": 0,
                    "solution": "<p>Let AF = AE = x. Then AB = AF+FB = x+8, AC = AE+EC = x+6, BC = 14.</p><p>Semi-perimeter s = (x+8+x+6+14)/2 = x+14.</p><p>Area = r × s → 84 = 4(x+14) → x+14 = 21 → x = 7.</p><p>AB = 7+8 = 15 cm, AC = 7+6 = 13 cm.</p>"
                },
                {
                    "question": "If tangents PA and PB from point P to a circle with centre O are inclined to each other at \\(120°\\), find \\(\\angle POA\\).",
                    "options": ["30°", "60°", "90°", "45°"],
                    "correctIndex": 0,
                    "solution": "<p>OP bisects \\(\\angle APB\\): \\(\\angle OPA = 60°\\).</p><p>In right \\(\\triangle OAP\\): \\(\\angle POA = 90° - 60° = 30°\\).</p>"
                },
                {
                    "question": "A circle touches the side BC of \\(\\triangle ABC\\) at P and the extensions of sides AB and AC at Q and R respectively. Prove that \\(AQ = \\frac{1}{2}(\\text{Perimeter of } \\triangle ABC)\\).",
                    "options": ["True — AQ = AB+BP = AB+BQ, and using equal tangent lengths", "False", "Only for equilateral triangles", "AQ = perimeter"],
                    "correctIndex": 0,
                    "solution": "<p>By equal tangent lengths: BQ = BP and CR = CP and AQ = AR.</p><p>AQ = AB + BQ = AB + BP ...(since BQ=BP)</p><p>AR = AC + CR = AC + CP ...(since CR=CP)</p><p>Since AQ = AR: AB + BP = AC + CP.</p><p>Also perimeter = AB + BC + AC = AB + (BP+PC) + AC = (AB+BP) + (AC+PC) = AQ + AR = 2AQ.</p><p>So AQ = Perimeter/2. ✓</p>"
                }
            ],
            "pyq": [
                {
                    "question": "[2024] A quadrilateral ABCD is drawn to circumscribe a circle. Prove that AB + CD = AD + BC.",
                    "options": ["True — using equal tangent lengths from each vertex", "False", "Only for rectangles", "Only for squares"],
                    "correctIndex": 0,
                    "solution": "<p>Let circle touch AB at P, BC at Q, CD at R, DA at S.</p><p>Equal tangent lengths: AP=AS, BP=BQ, CQ=CR, DR=DS.</p><p>AB+CD = (AP+PB)+(CR+RD) = (AS+BQ)+(CQ+DS) = (AS+DS)+(BQ+CQ) = AD+BC. ✓</p>"
                },
                {
                    "question": "[2023] In the figure, two tangents RQ and RP are drawn from an external point R to a circle with centre O. If \\(\\angle PRQ = 120°\\), prove that OR = PR + RQ.",
                    "options": ["True — OR = 2PR and PR=RQ, so OR = PR+RQ", "False", "Only when angle is 90°", "Only for unit circles"],
                    "correctIndex": 0,
                    "solution": "<p>\\(\\angle PRQ = 120°\\). Since RP = RQ (equal tangent lengths), \\(\\angle ORP = 60°\\) (OR bisects \\(\\angle PRQ\\)).</p><p>In right \\(\\triangle OPR\\): \\(\\cos 60° = \\frac{PR}{OR}\\)</p><p>\\(\\frac{1}{2} = \\frac{PR}{OR} \\Rightarrow OR = 2PR\\).</p><p>Since PR = RQ: OR = PR + PR = PR + RQ. ✓</p>"
                },
                {
                    "question": "[2021] Prove that the tangent at any point of a circle is perpendicular to the radius through the point of contact.",
                    "options": ["True — proven by contradiction (any other line from centre is longer than radius)", "True — by construction", "False", "Cannot prove"],
                    "correctIndex": 0,
                    "solution": "<p>Let O be centre, P be point of contact, XY be tangent.</p><p>Assume OQ < OP for some Q on XY (Q≠P). Then Q is inside the circle. But Q is on tangent XY, so XY enters the circle — contradiction (tangent touches at only one point).</p><p>So OP ≤ OQ for all Q on XY, meaning OP is the shortest distance from O to XY. The shortest distance from a point to a line is the perpendicular. Hence OP ⊥ XY. ✓</p>"
                },
                {
                    "question": "[2020] In the figure, PQ is a chord of length 8 cm of a circle of radius 5 cm. The tangents at P and Q intersect at T. Find the length TP.",
                    "options": ["20/3 cm", "5 cm", "8 cm", "13/3 cm"],
                    "correctIndex": 0,
                    "solution": "<p>Draw OM ⊥ PQ. Then PM = 4 cm (M is midpoint of PQ).</p><p>OM = \\(\\sqrt{25-16} = 3\\) cm.</p><p>Let TP = x, TM = TQ + QM... Actually: In right \\(\\triangle OPT\\): \\(OT^2 = OP^2 + PT^2 = 25 + x^2\\).</p><p>Also OT = OM + MT = 3 + MT. And in right \\(\\triangle PMT\\): \\(PT^2 = PM^2 + MT^2 \\Rightarrow x^2 = 16 + MT^2\\).</p><p>From \\(\\triangle OPT\\): \\((3+MT)^2 = 25 + x^2 = 25 + 16 + MT^2 = 41 + MT^2\\).</p><p>\\(9 + 6MT + MT^2 = 41 + MT^2 \\Rightarrow 6MT = 32 \\Rightarrow MT = 16/3\\).</p><p>\\(x = \\sqrt{16 + 256/9} = \\sqrt{400/9} = 20/3\\) cm.</p>"
                }
            ],
            "test": [
                {
                    "question": "If two tangents inclined at \\(60°\\) are drawn to a circle of radius 3 cm, find the length of each tangent.",
                    "options": ["3√3 cm", "3 cm", "6 cm", "3/√3 cm"],
                    "correctIndex": 0,
                    "solution": "<p>\\(\\angle OPA = 30°\\) (half of 60°). \\(\\tan 30° = \\frac{3}{PT}\\).</p><p>\\(PT = \\frac{3}{1/\\sqrt{3}} = 3\\sqrt{3}\\) cm.</p>"
                },
                {
                    "question": "A triangle ABC with AB = 10nm, BC = 8 cm, CA = 6 cm has an inscribed circle. Find the tangent lengths from vertex A.",
                    "options": ["4 cm", "3 cm", "5 cm", "6 cm"],
                    "correctIndex": 0,
                    "solution": "<p>s = (10+8+6)/2 = 12. Tangent from A = s − a = 12 − 8 = 4 cm (where a = BC).</p>"
                }
            ]
        }
    ],
    "chapterTest": {
        "title": "Chapter 10 Test: Circles",
        "description": "25 minutes · Tangent theorems & applications · Pass mark 70%",
        "passPercent": 70,
        "questions": [
            {
                "concept": "Tangent Properties",
                "question": "In the figure, if TP and TQ are tangents from T to a circle with centre O and \\(\\angle POQ = 110°\\), find \\(\\angle PTQ\\).",
                "options": ["70°", "110°", "55°", "90°"],
                "correctIndex": 0,
                "solution": "∠PTQ = 360° − 90° − 90° − 110° = 70°."
            },
            {
                "concept": "Equal Tangent Lengths",
                "question": "A circle is inscribed in a \\(\\triangle ABC\\) with AB = 14 cm, BC = 13 cm, CA = 15 cm. Find the tangent length from vertex B.",
                "options": ["6 cm", "7 cm", "8 cm", "5 cm"],
                "correctIndex": 0,
                "solution": "s = (14+13+15)/2 = 21. Tangent from B = s − b = 21 − 15 = 6 cm."
            },
            {
                "concept": "Tangent Properties",
                "question": "The length of a tangent from a point 10 cm away from the centre of a circle of radius 6 cm is:",
                "options": ["8 cm", "6 cm", "10 cm", "4 cm"],
                "correctIndex": 0,
                "solution": "Tangent = √(10²−6²) = √(100−36) = √64 = 8 cm."
            },
            {
                "concept": "Equal Tangent Lengths",
                "question": "ABCD is a quadrilateral circumscribing a circle. If AB = 8, BC = 6, CD = 5, find DA.",
                "options": ["7", "5", "3", "9"],
                "correctIndex": 0,
                "solution": "AB + CD = BC + DA → 8+5 = 6+DA → DA = 7."
            },
            {
                "concept": "Tangent Properties",
                "question": "Two tangents PA and PB are drawn to a circle from P. If \\(\\angle PAB = 50°\\), then \\(\\angle APB = \\)?",
                "options": ["80°", "100°", "50°", "40°"],
                "correctIndex": 0,
                "solution": "Since PA=PB (equal tangents), △PAB is isosceles. ∠PBA = ∠PAB = 50°. ∠APB = 180°−50°−50° = 80°."
            }
        ]
    },
    "completion": {
        "title": "Mastered Chapter 10! 🎉",
        "message": "You've conquered Circles — tangent properties, equal tangent lengths, and all the key theorems. These are guaranteed questions in the Board Exam!",
        "nextChapter": {
            "label": "Move on to Areas Related to Circles →",
            "url": "/class-10-maths/chapter-11-areas-circles.html"
        }
    }
};

fs.writeFileSync('class-10-maths/chapter-10-data.json', JSON.stringify(data, null, 4));
console.log('chapter-10-data.json written!');
console.log('Concept 0:', data.concepts[0].practice.length, 'practice,', data.concepts[0].pyq.length, 'PYQs');
console.log('Concept 1:', data.concepts[1].practice.length, 'practice,', data.concepts[1].pyq.length, 'PYQs');
console.log('Chapter test:', data.chapterTest.questions.length, 'Qs');
