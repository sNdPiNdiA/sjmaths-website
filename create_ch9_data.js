const fs = require('fs');

const data = {
    "chapter": 9,
    "title": "Some Applications of Trigonometry",
    "class": 10,
    "concepts": [
        {
            "id": "angles-elevation-depression",
            "title": "Angles of Elevation & Depression",
            "icon": "🏔️",
            "precheck": {
                "question": "When we look upward at the top of a building from a point on the ground, the angle formed between the line of sight and the horizontal is called the:",
                "options": [
                    "Angle of Elevation",
                    "Angle of Depression",
                    "Angle of Inclination",
                    "Right Angle"
                ],
                "correctIndex": 0,
                "passMessage": "Correct! The angle of elevation is measured from the horizontal line to the line of sight when looking upward.",
                "failMessage": "When looking UP, the angle between the horizontal and the line of sight is called the Angle of Elevation."
            },
            "learn": {
                "paragraphs": [
                    "The **angle of elevation** is the angle between the horizontal line of sight and the line of sight directed **upward** to an object. Example: looking up at the top of a tower.",
                    "The **angle of depression** is the angle between the horizontal line of sight and the line of sight directed **downward** to an object. Example: looking down from a lighthouse at a boat.",
                    "**Key fact**: The angle of elevation from point A to point B equals the angle of depression from point B to point A (alternate interior angles with the horizontal).",
                    "In all these problems, we assume the objects are on **level ground**, the tower/pole is **vertical** (perpendicular to ground), and we work with the **right triangle** formed."
                ],
                "formulas": [
                    {
                        "rule": "Basic Setup",
                        "formula": "tan(angle) = Height / Distance",
                        "example": "Tower height h, distance d from base: tanθ = h/d"
                    },
                    {
                        "rule": "Key tan values",
                        "formula": "tan30° = 1/√3, tan45° = 1, tan60° = √3",
                        "example": "If θ=60°, d=10: h = 10tan60° = 10√3 m"
                    }
                ],
                "boxes": [
                    {
                        "type": "success",
                        "html": "<strong>Drawing the Figure:</strong> Always draw a rough figure first! Mark the observer, the object, the horizontal, the right angle at the base, and the angle given. Label the unknown as a variable."
                    },
                    {
                        "type": "warning",
                        "html": "<strong>Angle of Depression ≠ Angle at Base:</strong> The angle of depression is at the <em>top</em> (from horizontal looking down). But by alternate interior angles, this equals the angle of elevation at the bottom. Always identify which angle is given!"
                    },
                    {
                        "type": "info",
                        "html": "<strong>Board Exam Tip:</strong> Most 3-mark questions involve a single right triangle. 5-mark questions involve <strong>two triangles</strong> sharing a common side (usually the height). Set up two equations and eliminate the common variable."
                    }
                ]
            },
            "practice": [
                {
                    "question": "A tower stands vertically on the ground. From a point on the ground 20m from the base, the angle of elevation of the top is \\(60°\\). Find the height of the tower.",
                    "options": ["20√3 m", "20 m", "20/√3 m", "40 m"],
                    "correctIndex": 0,
                    "solution": "<p>Let height = \\(h\\). \\(\\tan 60° = \\frac{h}{20}\\).</p><p>\\(\\sqrt{3} = \\frac{h}{20} \\Rightarrow h = 20\\sqrt{3}\\) m ≈ 34.64 m.</p>"
                },
                {
                    "question": "A kite is flying at a height of 60m above the ground. The string attached to the kite is temporarily tied to a point on the ground. The inclination of the string with the ground is \\(60°\\). Find the length of the string (assume no slack).",
                    "options": ["40√3 m", "60√3 m", "120/√3 m", "60 m"],
                    "correctIndex": 0,
                    "solution": "<p>Here height = 60m and angle = 60°. We need the hypotenuse (string length).</p><p>\\(\\sin 60° = \\frac{60}{\\text{string}}\\)</p><p>\\(\\frac{\\sqrt{3}}{2} = \\frac{60}{l} \\Rightarrow l = \\frac{120}{\\sqrt{3}} = \\frac{120\\sqrt{3}}{3} = 40\\sqrt{3}\\) m.</p>"
                },
                {
                    "question": "The shadow of a tower standing on level ground is found to be 40m longer when the sun's altitude is \\(30°\\) than when it is \\(60°\\). Find the height of the tower.",
                    "options": ["20√3 m", "40√3 m", "20 m", "40 m"],
                    "correctIndex": 0,
                    "solution": "<p>Let height = \\(h\\). When angle = 60°: shadow = \\(\\frac{h}{\\tan 60°} = \\frac{h}{\\sqrt{3}}\\).</p><p>When angle = 30°: shadow = \\(\\frac{h}{\\tan 30°} = h\\sqrt{3}\\).</p><p>Difference: \\(h\\sqrt{3} - \\frac{h}{\\sqrt{3}} = 40\\).</p><p>\\(h\\left(\\sqrt{3} - \\frac{1}{\\sqrt{3}}\\right) = 40 \\Rightarrow h \\cdot \\frac{3-1}{\\sqrt{3}} = 40 \\Rightarrow \\frac{2h}{\\sqrt{3}} = 40\\).</p><p>\\(h = 20\\sqrt{3}\\) m.</p>"
                },
                {
                    "question": "From the top of a 7m building, the angle of elevation of the top of a cable tower is \\(60°\\) and the angle of depression of its foot is \\(45°\\). Find the height of the tower.",
                    "options": ["7(√3+1) m", "7√3 m", "14 m", "7(√3−1) m"],
                    "correctIndex": 0,
                    "solution": "<p>Let the cable tower height = \\(h\\). The building is 7m tall. The horizontal distance between them = \\(d\\).</p><p>From angle of depression 45°: \\(\\tan 45° = \\frac{7}{d} \\Rightarrow d = 7\\) m.</p><p>From angle of elevation 60°: \\(\\tan 60° = \\frac{h-7}{d} = \\frac{h-7}{7}\\).</p><p>\\(\\sqrt{3} = \\frac{h-7}{7} \\Rightarrow h-7 = 7\\sqrt{3} \\Rightarrow h = 7(\\sqrt{3}+1)\\) m.</p>"
                },
                {
                    "question": "A 1.5m tall boy is standing at some distance from a 30m tall building. The angle of elevation from his eyes to the top of the building increases from \\(30°\\) to \\(60°\\) as he walks towards the building. Find the distance he walked.",
                    "options": ["19√3 m", "28.5 m", "19 m", "28.5/√3 m"],
                    "correctIndex": 0,
                    "solution": "<p>Effective height = \\(30-1.5 = 28.5\\) m (from his eye level).</p><p>Initial distance \\(d_1\\): \\(\\tan 30° = \\frac{28.5}{d_1} \\Rightarrow d_1 = 28.5\\sqrt{3}\\).</p><p>Final distance \\(d_2\\): \\(\\tan 60° = \\frac{28.5}{d_2} \\Rightarrow d_2 = \\frac{28.5}{\\sqrt{3}} = 9.5\\sqrt{3}\\).</p><p>Distance walked = \\(d_1 - d_2 = 28.5\\sqrt{3} - 9.5\\sqrt{3} = 19\\sqrt{3}\\) m.</p>"
                },
                {
                    "question": "From a point on the ground, the angles of elevation of the bottom and top of a transmission tower on top of a 20m high building are \\(45°\\) and \\(60°\\) respectively. Find the height of the tower.",
                    "options": ["20(√3−1) m", "20√3 m", "20 m", "20(√3+1) m"],
                    "correctIndex": 0,
                    "solution": "<p>Let horizontal distance = \\(d\\), tower height = \\(t\\).</p><p>For building top (angle 45°): \\(\\tan 45° = \\frac{20}{d} \\Rightarrow d = 20\\) m.</p><p>For tower top (angle 60°): \\(\\tan 60° = \\frac{20+t}{20}\\).</p><p>\\(\\sqrt{3} = \\frac{20+t}{20} \\Rightarrow 20+t = 20\\sqrt{3} \\Rightarrow t = 20(\\sqrt{3}-1)\\) m ≈ 14.64 m.</p>"
                },
                {
                    "question": "A statue 1.6m tall stands on top of a pedestal. From a point on the ground, the angle of elevation of the top of the statue is \\(60°\\) and of the top of the pedestal is \\(45°\\). Find the height of the pedestal.",
                    "options": ["0.8(√3+1) m", "1.6 m", "0.8√3 m", "1.6(√3+1) m"],
                    "correctIndex": 0,
                    "solution": "<p>Let pedestal height = \\(h\\), distance = \\(d\\).</p><p>\\(\\tan 45° = \\frac{h}{d} \\Rightarrow d = h\\).</p><p>\\(\\tan 60° = \\frac{h+1.6}{d} = \\frac{h+1.6}{h}\\).</p><p>\\(\\sqrt{3}h = h+1.6 \\Rightarrow h(\\sqrt{3}-1) = 1.6\\).</p><p>\\(h = \\frac{1.6}{\\sqrt{3}-1} = \\frac{1.6(\\sqrt{3}+1)}{2} = 0.8(\\sqrt{3}+1)\\) m.</p>"
                },
                {
                    "question": "The angle of elevation of the top of a tower from two points distant \\(a\\) and \\(b\\) from the base and in the same straight line with it are complementary. Prove that the height of the tower is \\(\\sqrt{ab}\\).",
                    "options": ["h = √(ab) ✓", "h = a+b", "h = ab", "h = (a+b)/2"],
                    "correctIndex": 0,
                    "solution": "<p>Let height = \\(h\\). Angles are \\(\\theta\\) and \\(90°-\\theta\\).</p><p>\\(\\tan\\theta = \\frac{h}{a}\\) ...(1)</p><p>\\(\\tan(90°-\\theta) = \\cot\\theta = \\frac{h}{b}\\) → \\(\\frac{1}{\\tan\\theta} = \\frac{h}{b}\\) ...(2)</p><p>Multiply (1) and (2): \\(1 = \\frac{h^2}{ab} \\Rightarrow h^2 = ab \\Rightarrow h = \\sqrt{ab}\\) ✓</p>"
                }
            ],
            "pyq": [
                {
                    "question": "[2024] A straight highway leads to the foot of a tower. A man standing at the top of the tower observes a car at an angle of depression of \\(30°\\), which is approaching the tower with a uniform speed. Six seconds later, the angle of depression is \\(60°\\). Find the time taken by the car to reach the tower from this point.",
                    "options": ["3 seconds", "6 seconds", "9 seconds", "12 seconds"],
                    "correctIndex": 0,
                    "solution": "<p>Let tower height = \\(h\\), distance at 30° = \\(d_1\\), at 60° = \\(d_2\\).</p><p>\\(d_1 = h\\sqrt{3}\\), \\(d_2 = \\frac{h}{\\sqrt{3}}\\).</p><p>Distance covered in 6s: \\(d_1-d_2 = h\\sqrt{3} - \\frac{h}{\\sqrt{3}} = \\frac{2h}{\\sqrt{3}}\\).</p><p>Speed = \\(\\frac{2h}{\\sqrt{3} \\times 6}\\).</p><p>Remaining distance = \\(d_2 = \\frac{h}{\\sqrt{3}}\\).</p><p>Time = \\(\\frac{h/\\sqrt{3}}{2h/(6\\sqrt{3})} = \\frac{h}{\\sqrt{3}} \\times \\frac{6\\sqrt{3}}{2h} = 3\\) seconds.</p>"
                },
                {
                    "question": "[2023] From the top of a 15m high building, the angle of elevation of the top of a tower is \\(30°\\) and the angle of depression of the foot of the tower is \\(60°\\). Find the height of the tower.",
                    "options": ["20 m", "25 m", "15+5√3 m", "30 m"],
                    "correctIndex": 0,
                    "solution": "<p>Let tower height = \\(H\\), horizontal distance = \\(d\\).</p><p>Angle of depression of foot = 60°: \\(\\tan 60° = \\frac{15}{d} \\Rightarrow d = \\frac{15}{\\sqrt{3}} = 5\\sqrt{3}\\) m.</p><p>Angle of elevation of top = 30°: \\(\\tan 30° = \\frac{H-15}{d} = \\frac{H-15}{5\\sqrt{3}}\\).</p><p>\\(\\frac{1}{\\sqrt{3}} = \\frac{H-15}{5\\sqrt{3}} \\Rightarrow H-15 = 5 \\Rightarrow H = 20\\) m.</p>"
                },
                {
                    "question": "[2022] Two poles of equal heights are standing opposite to each other on either side of a road which is 80m wide. From a point between them, the angles of elevation of the tops are \\(60°\\) and \\(30°\\). Find the height of the poles and the distances of the point from the poles.",
                    "options": ["h=20√3 m, distances 20m and 60m", "h=40 m, distances 40m and 40m", "h=20 m, distances 20m and 60m", "h=30 m, distances 30m and 50m"],
                    "correctIndex": 0,
                    "solution": "<p>Let height = \\(h\\), point is \\(x\\) m from first pole, \\((80-x)\\) from second.</p><p>\\(\\tan 60° = \\frac{h}{x} \\Rightarrow h = x\\sqrt{3}\\) ...(1)</p><p>\\(\\tan 30° = \\frac{h}{80-x} \\Rightarrow h = \\frac{80-x}{\\sqrt{3}}\\) ...(2)</p><p>From (1) and (2): \\(x\\sqrt{3} = \\frac{80-x}{\\sqrt{3}} \\Rightarrow 3x = 80-x \\Rightarrow 4x = 80 \\Rightarrow x = 20\\).</p><p>\\(h = 20\\sqrt{3}\\) m. Distances: 20m and 60m.</p>"
                },
                {
                    "question": "[2021] The angle of elevation of the top of a building from the foot of a tower is \\(30°\\) and the angle of elevation of the top of the tower from the foot of the building is \\(60°\\). If the tower is 50m high, find the height of the building.",
                    "options": ["50/3 m", "50 m", "50√3 m", "25 m"],
                    "correctIndex": 0,
                    "solution": "<p>Let building height = \\(h\\), distance between them = \\(d\\).</p><p>From foot of building: \\(\\tan 60° = \\frac{50}{d} \\Rightarrow d = \\frac{50}{\\sqrt{3}}\\).</p><p>From foot of tower: \\(\\tan 30° = \\frac{h}{d} \\Rightarrow \\frac{1}{\\sqrt{3}} = \\frac{h \\cdot \\sqrt{3}}{50}\\).</p><p>\\(h = \\frac{50}{3}\\) m ≈ 16.67 m.</p>"
                },
                {
                    "question": "[2020] A tree breaks due to a storm and the broken part bends so that the top of the tree touches the ground at an angle of \\(30°\\) at a distance of \\(8\\) m from its foot. Find the original height of the tree.",
                    "options": ["8√3 m", "16/√3 m", "24/√3 m", "8(√3+1) m"],
                    "correctIndex": 0,
                    "solution": "<p>Let the broken part = \\(l\\) (hypotenuse) and standing part = \\(h\\).</p><p>\\(\\tan 30° = \\frac{h}{8} \\Rightarrow h = \\frac{8}{\\sqrt{3}}\\).</p><p>\\(\\cos 30° = \\frac{8}{l} \\Rightarrow l = \\frac{8}{\\cos 30°} = \\frac{8}{\\sqrt{3}/2} = \\frac{16}{\\sqrt{3}}\\).</p><p>Original height = \\(h + l = \\frac{8}{\\sqrt{3}} + \\frac{16}{\\sqrt{3}} = \\frac{24}{\\sqrt{3}} = 8\\sqrt{3}\\) m.</p>"
                }
            ],
            "test": [
                {
                    "question": "A person standing on the bank of a river observes that the angle of elevation of the top of a tree on the opposite bank is \\(60°\\). When he moves 40m away from the bank, the angle of elevation becomes \\(30°\\). Find the height of the tree and width of the river.",
                    "options": ["h=20√3 m, width=20 m", "h=40 m, width=40 m", "h=20 m, width=20√3 m", "h=40√3 m, width=40 m"],
                    "correctIndex": 0,
                    "solution": "<p>Let height = \\(h\\), river width = \\(d\\).</p><p>\\(\\tan 60° = \\frac{h}{d} \\Rightarrow h = d\\sqrt{3}\\).</p><p>\\(\\tan 30° = \\frac{h}{d+40} \\Rightarrow h = \\frac{d+40}{\\sqrt{3}}\\).</p><p>\\(d\\sqrt{3} = \\frac{d+40}{\\sqrt{3}} \\Rightarrow 3d = d+40 \\Rightarrow d = 20\\) m.</p><p>\\(h = 20\\sqrt{3}\\) m.</p>"
                },
                {
                    "question": "From a window (60m above ground) of a house, the angles of depression of the top and bottom of a lamp post are \\(30°\\) and \\(60°\\) respectively. Find the height of the lamp post.",
                    "options": ["40 m", "20 m", "30 m", "45 m"],
                    "correctIndex": 0,
                    "solution": "<p>Let lamp post height = \\(h\\), distance = \\(d\\).</p><p>\\(\\tan 60° = \\frac{60}{d} \\Rightarrow d = \\frac{60}{\\sqrt{3}} = 20\\sqrt{3}\\).</p><p>\\(\\tan 30° = \\frac{60-h}{d} \\Rightarrow \\frac{1}{\\sqrt{3}} = \\frac{60-h}{20\\sqrt{3}}\\).</p><p>\\(60-h = 20 \\Rightarrow h = 40\\) m.</p>"
                }
            ]
        },
        {
            "id": "multi-angle-problems",
            "title": "Two-Angle & Moving Observer Problems",
            "icon": "📐",
            "precheck": {
                "question": "If the angles of elevation of the top of a tower from two points at distances \\(a\\) and \\(b\\) from the base are complementary, then the height of the tower is:",
                "options": ["√(ab)", "a+b", "(a+b)/2", "ab"],
                "correctIndex": 0,
                "passMessage": "Correct! When angles are complementary, h² = ab, giving h = √(ab). This is a very important result!",
                "failMessage": "If angles θ and (90°−θ) give tanθ = h/a and cotθ = h/b, multiplying gives h² = ab, so h = √(ab)."
            },
            "learn": {
                "paragraphs": [
                    "Many board exam questions involve an observer **moving towards or away** from a tower, creating **two right triangles** that share the height as a common side.",
                    "**Strategy**: Set up two equations using \\(\\tan\\) of each angle. Both equations will have the height \\(h\\). Divide or subtract to eliminate one unknown.",
                    "Common patterns: (1) Shadow lengthening/shortening, (2) Car/boat approaching a lighthouse, (3) Two buildings of different heights, (4) Broken tree problems.",
                    "Always rationalize your answer: convert \\(\\frac{1}{\\sqrt{3}}\\) to \\(\\frac{\\sqrt{3}}{3}\\) for the final answer."
                ],
                "formulas": [
                    {
                        "rule": "Two-angle formula (same side)",
                        "formula": "h = d × tan(α) and h = (d+x) × tan(β)",
                        "example": "Eliminate d to find h when x (distance walked) is known"
                    },
                    {
                        "rule": "Complementary angle result",
                        "formula": "If angles α + β = 90°, then height h = √(ab)",
                        "example": "Distances a=9m, b=16m → h = √144 = 12m"
                    }
                ],
                "boxes": [
                    {
                        "type": "success",
                        "html": "<strong>5-Mark Problem Strategy:</strong><ol style='margin:4px 0 0 16px;padding:0'><li>Draw the figure with all given data.</li><li>Identify the two right triangles.</li><li>Write tanα and tanβ equations.</li><li>Eliminate the common unknown.</li><li>Substitute standard values and simplify.</li></ol>"
                    },
                    {
                        "type": "info",
                        "html": "<strong>Rationalisation reminder:</strong> \\(\\frac{a}{\\sqrt{3}} = \\frac{a\\sqrt{3}}{3}\\). CBSE expects simplified, rationalised answers."
                    }
                ]
            },
            "practice": [
                {
                    "question": "As observed from the top of a 75m tall lighthouse, the angles of depression of two ships are \\(30°\\) and \\(45°\\). If one ship is exactly behind the other on the same side, find the distance between the ships.",
                    "options": ["75(√3−1) m", "75√3 m", "75 m", "75(√3+1) m"],
                    "correctIndex": 0,
                    "solution": "<p>Let ship 1 (45°) be at distance \\(d_1\\), ship 2 (30°) at \\(d_2\\).</p><p>\\(\\tan 45° = \\frac{75}{d_1} \\Rightarrow d_1 = 75\\) m.</p><p>\\(\\tan 30° = \\frac{75}{d_2} \\Rightarrow d_2 = 75\\sqrt{3}\\) m.</p><p>Distance between ships = \\(d_2 - d_1 = 75\\sqrt{3} - 75 = 75(\\sqrt{3}-1)\\) m.</p>"
                },
                {
                    "question": "The angles of depression of the top and bottom of a 8m tall building from the top of a tower are \\(30°\\) and \\(45°\\) respectively. Find the height of the tower and the distance between the tower and building.",
                    "options": ["h = 4(√3+1) m, d = 4(√3+1) m", "h = 8√3 m, d = 8 m", "h = 16 m, d = 8 m", "h = 12 m, d = 12 m"],
                    "correctIndex": 0,
                    "solution": "<p>Let tower height = \\(H\\), distance = \\(d\\).</p><p>\\(\\tan 45° = \\frac{H}{d} \\Rightarrow H = d\\) ...(1)</p><p>\\(\\tan 30° = \\frac{H-8}{d}\\). Using (1): \\(\\frac{1}{\\sqrt{3}} = \\frac{d-8}{d}\\).</p><p>\\(d = \\sqrt{3}(d-8) = \\sqrt{3}d - 8\\sqrt{3}\\).</p><p>\\(d(\\sqrt{3}-1) = 8\\sqrt{3} \\Rightarrow d = \\frac{8\\sqrt{3}}{\\sqrt{3}-1} = \\frac{8\\sqrt{3}(\\sqrt{3}+1)}{2} = 4\\sqrt{3}(\\sqrt{3}+1) = 4(3+\\sqrt{3}) = 4(\\sqrt{3}+1) \\times \\sqrt{3}\\).</p><p>Simplifying: \\(d = 4(\\sqrt{3}+1) \\approx 10.93\\) m. \\(H = d = 4(\\sqrt{3}+1)\\) m.</p>"
                },
                {
                    "question": "The angle of elevation of a jet plane from point A on the ground is \\(60°\\). After 15 seconds, the angle of elevation becomes \\(30°\\). If the jet is flying at a constant height of \\(1500\\sqrt{3}\\) m, find its speed.",
                    "options": ["200 m/s = 720 km/h", "100 m/s", "150 m/s", "250 m/s"],
                    "correctIndex": 0,
                    "solution": "<p>Let the jet be at height \\(h = 1500\\sqrt{3}\\) m.</p><p>At 60°: horizontal dist from A = \\(\\frac{h}{\\tan 60°} = \\frac{1500\\sqrt{3}}{\\sqrt{3}} = 1500\\) m.</p><p>At 30°: horizontal dist from A = \\(\\frac{h}{\\tan 30°} = 1500\\sqrt{3} \\times \\sqrt{3} = 4500\\) m.</p><p>Distance covered = \\(4500-1500 = 3000\\) m in 15s.</p><p>Speed = \\(\\frac{3000}{15} = 200\\) m/s = 720 km/h.</p>"
                },
                {
                    "question": "A TV tower stands vertically on the bank of a canal. From a point on the other bank directly opposite, the angle of elevation of the top of the tower is \\(60°\\). From another point 20m from this point, also on the same bank, the angle of elevation is \\(30°\\). Find the height of the tower and width of the canal.",
                    "options": ["h=10√3 m, width=10 m", "h=20√3 m, width=20 m", "h=20 m, width=20√3 m", "h=10 m, width=10√3 m"],
                    "correctIndex": 0,
                    "solution": "<p>Let height = \\(h\\), canal width = \\(d\\).</p><p>\\(\\tan 60° = \\frac{h}{d} \\Rightarrow h = d\\sqrt{3}\\) ...(1)</p><p>\\(\\tan 30° = \\frac{h}{d+20} \\Rightarrow h = \\frac{d+20}{\\sqrt{3}}\\) ...(2)</p><p>From (1) and (2): \\(d\\sqrt{3} = \\frac{d+20}{\\sqrt{3}}\\).</p><p>\\(3d = d+20 \\Rightarrow d = 10\\) m. \\(h = 10\\sqrt{3}\\) m.</p>"
                },
                {
                    "question": "From the top of a 60m high building, the angle of depression of the top and bottom of a vertical lamp post are \\(30°\\) and \\(60°\\) respectively. Find: (i) the horizontal distance, (ii) the height of the lamp post.",
                    "options": ["d = 20√3 m, lamp = 40 m", "d = 30 m, lamp = 30 m", "d = 60/√3 m, lamp = 20 m", "d = 20 m, lamp = 40 m"],
                    "correctIndex": 0,
                    "solution": "<p>Let lamp height = \\(h\\), distance = \\(d\\).</p><p>Angle of depression of bottom (60°): \\(\\tan 60° = \\frac{60}{d} \\Rightarrow d = \\frac{60}{\\sqrt{3}} = 20\\sqrt{3}\\) m.</p><p>Angle of depression of top (30°): \\(\\tan 30° = \\frac{60-h}{d} = \\frac{60-h}{20\\sqrt{3}}\\).</p><p>\\(\\frac{1}{\\sqrt{3}} = \\frac{60-h}{20\\sqrt{3}} \\Rightarrow 20 = 60-h \\Rightarrow h = 40\\) m.</p>"
                },
                {
                    "question": "Two men on either side of a cliff 80m high observe the angles of elevation of the top of the cliff to be \\(30°\\) and \\(60°\\). Find the distance between the two men.",
                    "options": ["320/√3 m", "80√3 m", "80(1+√3) m", "160/√3 m"],
                    "correctIndex": 0,
                    "solution": "<p>\\(d_1 = \\frac{80}{\\tan 30°} = 80\\sqrt{3}\\) m.</p><p>\\(d_2 = \\frac{80}{\\tan 60°} = \\frac{80}{\\sqrt{3}}\\) m.</p><p>Total = \\(80\\sqrt{3} + \\frac{80}{\\sqrt{3}} = \\frac{240 + 80}{\\sqrt{3}} = \\frac{320}{\\sqrt{3}} = \\frac{320\\sqrt{3}}{3}\\) m ≈ 184.75 m.</p>"
                },
                {
                    "question": "A man in a boat rowing away from a lighthouse 100m high takes 2 minutes to change the angle of elevation of the top of the lighthouse from \\(60°\\) to \\(30°\\). Find the speed of the boat.",
                    "options": ["100√3/3 m/min", "50√3 m/min", "100/√3 m/min", "200/3 m/min"],
                    "correctIndex": 0,
                    "solution": "<p>At 60°: \\(d_1 = \\frac{100}{\\sqrt{3}}\\). At 30°: \\(d_2 = 100\\sqrt{3}\\).</p><p>Distance rowed = \\(100\\sqrt{3} - \\frac{100}{\\sqrt{3}} = \\frac{300-100}{\\sqrt{3}} = \\frac{200}{\\sqrt{3}}\\) m.</p><p>Speed = \\(\\frac{200}{\\sqrt{3} \\times 2} = \\frac{100}{\\sqrt{3}} = \\frac{100\\sqrt{3}}{3}\\) m/min.</p>"
                }
            ],
            "pyq": [
                {
                    "question": "[2024] Two pillars of equal heights stand on either side of a road 150m wide. From a point on the road between the pillars, the angles of elevation are \\(60°\\) and \\(30°\\). Find the position of the point and height of each pillar.",
                    "options": ["37.5 m from one pillar, h = 37.5√3 m", "75 m from each, h = 75√3 m", "50 m from one, h = 50√3 m", "100 m from one, h = 100/√3 m"],
                    "correctIndex": 0,
                    "solution": "<p>Let \\(x\\) = distance from pillar with 60° elevation. Then \\((150-x)\\) from the other.</p><p>\\(h = x\\tan 60° = x\\sqrt{3}\\) and \\(h = (150-x)\\tan 30° = \\frac{150-x}{\\sqrt{3}}\\).</p><p>\\(x\\sqrt{3} = \\frac{150-x}{\\sqrt{3}} \\Rightarrow 3x = 150-x \\Rightarrow x = 37.5\\) m.</p><p>\\(h = 37.5\\sqrt{3}\\) m ≈ 64.95 m.</p>"
                },
                {
                    "question": "[2023] From a point on the ground, the angle of elevation of the bottom and top of a transmission tower fixed at the top of a 20m high building are \\(45°\\) and \\(60°\\). Find the height of the tower.",
                    "options": ["20(√3−1) m", "20 m", "20√3 m", "40 m"],
                    "correctIndex": 0,
                    "solution": "<p>\\(\\tan 45° = \\frac{20}{d} \\Rightarrow d = 20\\).</p><p>\\(\\tan 60° = \\frac{20+t}{20} \\Rightarrow t = 20(\\sqrt{3}-1)\\) m ≈ 14.64 m.</p>"
                },
                {
                    "question": "[2022] The angle of elevation of the top of a tower from a point on the ground is \\(30°\\). After walking 150m towards the tower, the angle becomes \\(60°\\). Find the height of the tower.",
                    "options": ["75√3 m", "150 m", "75 m", "150√3 m"],
                    "correctIndex": 0,
                    "solution": "<p>Let height = \\(h\\), initial distance = \\(d\\).</p><p>\\(\\tan 30° = \\frac{h}{d} \\Rightarrow d = h\\sqrt{3}\\) ...(1)</p><p>\\(\\tan 60° = \\frac{h}{d-150} \\Rightarrow d-150 = \\frac{h}{\\sqrt{3}}\\) ...(2)</p><p>From (1): \\(h\\sqrt{3} - 150 = \\frac{h}{\\sqrt{3}}\\). Multiply by \\(\\sqrt{3}\\): \\(3h - 150\\sqrt{3} = h\\).</p><p>\\(2h = 150\\sqrt{3} \\Rightarrow h = 75\\sqrt{3}\\) m ≈ 129.9 m.</p>"
                },
                {
                    "question": "[2019] A 7m tall flagstaff is fixed on top of a tower. From a point on the ground, the angles of elevation of the top and bottom of the flagstaff are \\(45°\\) and \\(30°\\) respectively. Find the height of the tower. (Use \\(\\sqrt{3} = 1.732\\))",
                    "options": ["9.56 m", "7 m", "14 m", "7√3 m"],
                    "correctIndex": 0,
                    "solution": "<p>Let tower height = \\(h\\), distance = \\(d\\).</p><p>\\(\\tan 30° = \\frac{h}{d} \\Rightarrow d = h\\sqrt{3}\\).</p><p>\\(\\tan 45° = \\frac{h+7}{d} = \\frac{h+7}{h\\sqrt{3}} \\Rightarrow h\\sqrt{3} = h+7\\).</p><p>\\(h(\\sqrt{3}-1) = 7 \\Rightarrow h = \\frac{7}{\\sqrt{3}-1} = \\frac{7(\\sqrt{3}+1)}{2} = \\frac{7(1.732+1)}{2} = \\frac{7 \\times 2.732}{2} = 9.562\\) m ≈ 9.56 m.</p>"
                }
            ],
            "test": [
                {
                    "question": "From a helicopter at height 1200m, the angles of depression of two boats on opposite sides are \\(30°\\) and \\(45°\\). Find the distance between the boats.",
                    "options": ["1200(√3+1) m", "1200√3 m", "2400 m", "1200(√3−1) m"],
                    "correctIndex": 0,
                    "solution": "<p>\\(d_1 = \\frac{1200}{\\tan 45°} = 1200\\) m. \\(d_2 = \\frac{1200}{\\tan 30°} = 1200\\sqrt{3}\\) m.</p><p>Boats on opposite sides: total = \\(1200 + 1200\\sqrt{3} = 1200(1+\\sqrt{3})\\) m.</p>"
                },
                {
                    "question": "The angle of elevation of a cloud from a point 60m above a lake is \\(30°\\) and the angle of depression of its reflection in the lake is \\(60°\\). Find the height of the cloud above the lake.",
                    "options": ["120 m", "60 m", "90 m", "180 m"],
                    "correctIndex": 0,
                    "solution": "<p>Let cloud height above lake = \\(H\\). Point is 60m above lake.</p><p>\\(\\tan 30° = \\frac{H-60}{d}\\) and \\(\\tan 60° = \\frac{H+60}{d}\\).</p><p>Dividing: \\(\\frac{\\tan 60°}{\\tan 30°} = \\frac{H+60}{H-60} \\Rightarrow 3 = \\frac{H+60}{H-60}\\).</p><p>\\(3H-180 = H+60 \\Rightarrow 2H = 240 \\Rightarrow H = 120\\) m.</p>"
                }
            ]
        }
    ],
    "chapterTest": {
        "title": "Chapter 9 Test: Applications of Trigonometry",
        "description": "25 minutes · Board-level word problems · Pass mark 70%",
        "passPercent": 70,
        "questions": [
            {
                "concept": "Heights and Distances",
                "question": "A tree 12m high is broken by a storm. Its top touches the ground at an angle of \\(60°\\). Find the height of the part that is still standing.",
                "options": ["12(2−√3) m", "4√3 m", "6 m", "4 m"],
                "correctIndex": 0,
                "solution": "Let standing part = h, broken = 12−h. tan60° = h/d and (12−h) is the hypotenuse of the right triangle. sin60° = h/(12−h) → h√3/2 = h/(12−h)... Using tan60°: h/d = √3 → d = h/√3. Also (12−h)² = h² + d² → solve to get h."
            },
            {
                "concept": "Two-Angle Problems",
                "question": "From the top of a 120m high tower, a man observes two cars on opposite sides with angles of depression \\(60°\\) and \\(45°\\). Find the distance between the cars.",
                "options": ["120(1+1/√3) m", "120+40√3 m", "240 m", "120√3 m"],
                "correctIndex": 0,
                "solution": "d₁ = 120/tan60° = 120/√3 = 40√3 m. d₂ = 120/tan45° = 120 m. Total = 120 + 40√3 = 120(1+1/√3)."
            },
            {
                "concept": "Heights and Distances",
                "question": "A vertical pole and a vertical tower are on the same level ground. From the top of the pole the angle of elevation of the top of the tower is \\(60°\\) and the angle of depression of the bottom is \\(30°\\). The height of the tower is 75m. Find the height of the pole.",
                "options": ["18.75 m", "25 m", "37.5 m", "50 m"],
                "correctIndex": 0,
                "solution": "Let pole = h, distance = d. tan30° = h/d → d = h√3. tan60° = (75−h)/d → √3 = (75−h)/(h√3) → 3h = 75−h → 4h = 75 → h = 18.75 m."
            },
            {
                "concept": "Moving Observer",
                "question": "A man on the deck of a ship 14m above water observes that the angle of elevation of the top of a cliff is \\(60°\\) and the angle of depression of the base is \\(30°\\). Find the height of the cliff.",
                "options": ["56 m", "42 m", "28 m", "70 m"],
                "correctIndex": 0,
                "solution": "tan30° = 14/d → d = 14√3. tan60° = (H−14)/d → √3 = (H−14)/(14√3) → H−14 = 42 → H = 56 m."
            },
            {
                "concept": "Two-Angle Problems",
                "question": "The angles of elevation of the top of a tower from two points at distances \\(4\\) m and \\(9\\) m from the base in the same straight line are complementary. Find the height of the tower.",
                "options": ["6 m", "12 m", "13 m", "36 m"],
                "correctIndex": 0,
                "solution": "When angles are complementary, h = √(ab) = √(4×9) = √36 = 6 m."
            }
        ]
    },
    "completion": {
        "title": "Mastered Chapter 9! 🎉",
        "message": "You can now tackle any Heights & Distances problem in the Board Exam. Remember: draw the figure first, identify the right triangle, and use tan!",
        "nextChapter": {
            "label": "Move on to Circles →",
            "url": "/class-10-maths/chapter-10-circles.html"
        }
    }
};

fs.writeFileSync('class-10-maths/chapter-9-data.json', JSON.stringify(data, null, 4));
console.log('chapter-9-data.json written!');
console.log('Concept 0:', data.concepts[0].practice.length, 'practice,', data.concepts[0].pyq.length, 'PYQs');
console.log('Concept 1:', data.concepts[1].practice.length, 'practice,', data.concepts[1].pyq.length, 'PYQs');
console.log('Chapter test:', data.chapterTest.questions.length, 'Qs');
