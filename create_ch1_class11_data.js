const fs = require('fs');

const data = {
    "chapter": 1,
    "title": "Sets",
    "class": 11,
    "concepts": [
        {
            "id": "introduction-representation",
            "title": "Intro & Representation",
            "icon": "📦",
            "precheck": {
                "question": "Which of the following is a well-defined collection?",
                "options": [
                    "The collection of 5 most talented writers of India.",
                    "A collection of the most dangerous animals in the world.",
                    "The collection of all even integers.",
                    "The collection of best cricket players."
                ],
                "correctIndex": 2,
                "passMessage": "Correct! 'Even integers' is clear and objective, whereas 'most talented', 'most dangerous', or 'best' are subjective and vary from person to person.",
                "failMessage": "A set must be a well-defined collection of objects. Adjectives like 'talented', 'dangerous', and 'best' are subjective. 'Even integers' is an exact mathematical definition."
            },
            "learn": {
                "paragraphs": [
                    "A **set** is a well-defined collection of distinct objects. Every set is denoted by capital letters like \\(A, B, C, X, Y, Z\\), whereas its elements are represented by small letters \\(a, b, c, x, y, z\\).",
                    "If \\(a\\) is an element of set \\(A\\), we say that \\(a\\) belongs to \\(A\\) and write it as \\(a \\in A\\). If it does not belong, we write \\(a \\notin A\\).",
                    "**Roster (Tabular) Form:** Elements are listed, separated by commas, and enclosed in curly braces \\(\\{ \\}\\). For example, the set of vowels \\(V = \\{a, e, i, o, u\\}\\). Important rule: Elements are generally NOT repeated.",
                    "**Set-Builder Form:** All elements of the set possess a single common property \\(P(x)\\). Written as \\(A = \\{x : x \\text{ has property } P\\}\\). Example: \\(V = \\{x : x \\text{ is a vowel in English alphabet}\\}\\)."
                ],
                "formulas": [
                    {
                        "rule": "Belongs to",
                        "formula": "\\(x \\in A\\)",
                        "example": "If \\(A = \\{1, 2, 3\\}\\), then \\(2 \\in A\\) and \\(4 \\notin A\\)."
                    },
                    {
                        "rule": "Standard Sets",
                        "formula": "\\(N, Z, Q, R, Z^+, Q^+, R^+\\)",
                        "example": "\\(N\\) = Natural, \\(Z\\) = Integers, \\(R\\) = Real"
                    }
                ],
                "boxes": [
                    {
                        "type": "success",
                        "html": "<strong>PRO TIP:</strong> In Roster form, the order of listing doesn't matter. \\(\\{1, 2, 3\\}\\) is exactly the same set as \\(\\{3, 1, 2\\}\\)."
                    },
                    {
                        "type": "warning",
                        "html": "<strong>Common Mistake:</strong> Repeating elements in Roster form. The set of letters in the word 'SCHOOL' should be written as \\(\\{S, C, H, O, L\\}\\), NOT \\(\\{S, C, H, O, O, L\\}\\)."
                    }
                ]
            },
            "practice": [
                {
                    "question": "Which of the following are sets? (Choose the set)",
                    "options": [
                        "The collection of all months of a year beginning with the letter J.",
                        "A team of eleven best-cricket batsmen of the world.",
                        "A collection of the most dangerous animals of the world.",
                        "Most talented writers of India."
                    ],
                    "correctIndex": 0,
                    "solution": "<p>A set must be well-defined. Months beginning with 'J' are absolute: January, June, July. The others are subjective.</p>"
                },
                {
                    "question": "Write the set \\(A = \\{x : x \\text{ is an integer and } -3 < x < 7\\}\\) in roster form.",
                    "options": [
                        "\\(\\{-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7\\}\\)",
                        "\\(\\{-2, -1, 0, 1, 2, 3, 4, 5, 6\\}\\)",
                        "\\(\\{-3, -2, -1, 0, 1, 2, 3, 4, 5, 6\\}\\)",
                        "\\(\\{-2, -1, 0, 1, 2, 3, 4, 5, 6, 7\\}\\)"
                    ],
                    "correctIndex": 1,
                    "solution": "<p>We want integers strictly greater than -3 and strictly less than 7.</p><p>So, the integers are -2, -1, 0, 1, 2, 3, 4, 5, 6.</p><p>Roster form: \\(\\{-2, -1, 0, 1, 2, 3, 4, 5, 6\\}\\).</p>"
                },
                {
                    "question": "Write the set \\(\\{14, 21, 28, 35, 42, ..., 98\\}\\) in set-builder form.",
                    "options": [
                        "\\(\\{x : x = 7n, n \\in N \\text{ and } n \\leq 14\\}\\)",
                        "\\(\\{x : x = 7n, n \\in N \\text{ and } 1 \\leq n \\leq 14\\}\\)",
                        "\\(\\{x : x = 7n, n \\in N \\text{ and } 2 \\leq n \\leq 14\\}\\)",
                        "\\(\\{x : x = 7n, n \\in N \\text{ and } 2 \\leq n < 15\\}\\)"
                    ],
                    "correctIndex": 2,
                    "solution": "<p>The numbers are multiples of 7: \\(7\\times 2, 7\\times 3, ..., 7\\times 14\\).</p><p>So, \\(x = 7n\\) where \\(n\\) starts from 2 and goes up to 14.</p><p>Set-builder form: \\(\\{x : x = 7n, n \\in N \\text{ and } 2 \\leq n \\leq 14\\}\\).</p>"
                },
                {
                    "question": "If \\(X = \\{ \\text{letters in word 'MISSISSIPPI'} \\}\\), then \\(n(X)\\) (the number of elements in \\(X\\)) is:",
                    "options": ["11", "4", "5", "6"],
                    "correctIndex": 1,
                    "solution": "<p>In a set, elements are not repeated. Distinct letters are M, I, S, P.</p><p>\\(X = \\{M, I, S, P\\}\\).</p><p>Number of elements = 4.</p>"
                }
            ],
            "pyq": [
                {
                    "question": "[Class 11 CBSE] Write the set \\(A = \\{\\frac{1}{2}, \\frac{2}{3}, \\frac{3}{4}, \\frac{4}{5}, \\frac{5}{6}, \\frac{6}{7}\\}\\) in the set-builder form.",
                    "options": [
                        "\\(\\{x : x = \\frac{n}{n+1}, n \\in N\\}\\)",
                        "\\(\\{x : x = \\frac{n}{n+1}, n \\in N \\text{ and } 1 \\leq n \\leq 6\\}\\)",
                        "\\(\\{x : x = \\frac{n}{n+1}, n \\in W \\text{ and } n \\leq 6\\}\\)",
                        "\\(\\{x : x = \\frac{n}{n+2}, n \\in N \\text{ and } 1 \\leq n \\leq 6\\}\\)"
                    ],
                    "correctIndex": 1,
                    "solution": "<p>Observe the pattern: numerator is \\(n\\), denominator is \\(n+1\\).</p><p>Thus, \\(x = \\frac{n}{n+1}\\).</p><p>The sequence starts at \\(n=1\\) and ends at \\(n=6\\).</p><p>So, \\(n \\in N\\) and \\(1 \\leq n \\leq 6\\).</p>"
                }
            ],
            "test": [
                {
                    "question": "Let \\(A = \\{1, 2, \\{3, 4\\}, 5\\}\\). Which of the following statements is INCORRECT?",
                    "options": [
                        "\\(3 \\in A\\)",
                        "\\(\\{3, 4\\} \\in A\\)",
                        "\\(1 \\in A\\)",
                        "\\(5 \\in A\\)"
                    ],
                    "correctIndex": 0,
                    "solution": "The elements of \\(A\\) are 1, 2, the set \\(\\{3, 4\\}\\), and 5. The number 3 itself is NOT an element directly inside \\(A\\). Therefore, \\(3 \\in A\\) is incorrect."
                }
            ]
        },
        {
            "id": "types-of-sets",
            "title": "Types of Sets & Subsets",
            "icon": "🎭",
            "precheck": {
                "question": "If set A has \\(m\\) elements, how many subsets does set A have?",
                "options": [
                    "\\(m^2\\)",
                    "\\(2m\\)",
                    "\\(2^m\\)",
                    "\\(m!\\)"
                ],
                "correctIndex": 2,
                "passMessage": "Exactly! The total number of subsets of a finite set containing \\(n\\) elements is \\(2^n\\).",
                "failMessage": "The total number of subsets of a set with \\(m\\) elements is \\(2^m\\)."
            },
            "learn": {
                "paragraphs": [
                    "**Empty Set (\\(\\phi\\)):** A set which does not contain any element. Ex: \\(\\{x : x > 1 \\text{ and } x < 0\\}\\). Also called null set or void set.",
                    "**Finite & Infinite Sets:** A set consists of a definite number of elements is finite, otherwise infinite. The empty set is finite.",
                    "**Equal Sets:** Two sets \\(A\\) and \\(B\\) are equal if they have exactly the same elements. Order does not matter.",
                    "**Subsets (\\(A \\subset B\\)):** \\(A\\) is a subset of \\(B\\) if every element of \\(A\\) is also an element of \\(B\\). Total subsets of a set with \\(n\\) elements = \\(2^n\\).",
                    "**Intervals:** subsets of \\(R\\). Closed \\([a, b]\\), Open \\((a, b)\\), Semi-open \\([a, b)\\).",
                    "**Power Set \\(P(A)\\):** The collection of all subsets of a set \\(A\\).",
                    "**Universal Set (\\(U\\)):** The basic set containing all elements and of which all other sets are subsets."
                ],
                "formulas": [
                    {
                        "rule": "Number of Subsets",
                        "formula": "\\(n(P(A)) = 2^m\\)",
                        "example": "If \\(A=\\{1,2\\}\\), subsets = \\(2^2 = 4\\)."
                    },
                    {
                        "rule": "Empty Set",
                        "formula": "\\(\\phi \\subset A\\)",
                        "example": "Empty set is a subset of EVERY set."
                    }
                ],
                "boxes": [
                    {
                        "type": "success",
                        "html": "<strong>Number of Proper Subsets:</strong> The number of proper subsets of a set with \\(n\\) elements is \\(2^n - 1\\). (We exclude the set itself)."
                    },
                    {
                        "type": "warning",
                        "html": "<strong>Important distinction:</strong> \\(\\phi\\) is an empty set. \\(\\{\\phi\\}\\) is NOT an empty set; it is a set containing one element (the symbol \\(\\phi\\))."
                    }
                ]
            },
            "practice": [
                {
                    "question": "Which of the following is an empty set?",
                    "options": [
                        "\\(\\{x : x \\text{ is an even prime number}\\}\\)",
                        "\\(\\{x : x^2 - 2 = 0 \\text{ and x is rational}\\}\\)",
                        "\\(\\{0\\}\\)",
                        "\\(\\{\\phi\\}\\)"
                    ],
                    "correctIndex": 1,
                    "solution": "<p>A) Even prime is \\(\\{2\\}\\).</p><p>B) \\(x^2 - 2 = 0 \\Rightarrow x = \\pm \\sqrt{2}\\), which are irrational. So no rational satisfies this. Thus, it's an empty set.</p><p>C) Contains the element 0.</p><p>D) Contains the element \\(\\phi\\).</p>"
                },
                {
                    "question": "Write the interval corresponding to \\(\\{x : x \\in R, -4 < x \\leq 6\\}\\).",
                    "options": [
                        "\\((-4, 6)\\)",
                        "\\([-4, 6]\\)",
                        "\\((-4, 6]\\)",
                        "\\([-4, 6)\\)"
                    ],
                    "correctIndex": 2,
                    "solution": "<p>Strict inequality \\( < \\) means open bracket '('.</p><p>Less than or equal \\( \\leq \\) means closed bracket ']'.</p><p>Thus, \\((-4, 6]\\).</p>"
                },
                {
                    "question": "If \\(A = \\{1, 2\\}\\), find the Power Set \\(P(A)\\).",
                    "options": [
                        "\\(\\{1, 2, \\{1, 2\\}\\}\\)",
                        "\\(\\{\\phi, \\{1\\}, \\{2\\}, \\{1, 2\\}\\}\\)",
                        "\\(\\{\\{1\\}, \\{2\\}, \\{1, 2\\}\\}\\)",
                        "\\(\\{\\phi, 1, 2, \\{1, 2\\}\\}\\)"
                    ],
                    "correctIndex": 1,
                    "solution": "<p>Subsets of \\(A\\) are: \\(\\phi\\), \\(\\{1\\}\\), \\(\\{2\\}\\), and \\(\\{1, 2\\}\\).</p><p>Power set is the set of all subsets: \\(\\{\\phi, \\{1\\}, \\{2\\}, \\{1, 2\\}\\}\\).</p>"
                }
            ],
            "pyq": [
                {
                    "question": "[School Exam] Two finite sets have \\(m\\) and \\(n\\) elements respectively. The total number of subsets of first set is 56 more than the total number of subsets of the second set. The values of \\(m\\) and \\(n\\) respectively are:",
                    "options": ["7, 6", "6, 3", "5, 1", "8, 7"],
                    "correctIndex": 1,
                    "solution": "<p>Number of subsets of first set = \\(2^m\\).</p><p>Number of subsets of second set = \\(2^n\\).</p><p>Given: \\(2^m - 2^n = 56\\).</p><p>Let's check options. For \\(m=6, n=3\\): \\(2^6 - 2^3 = 64 - 8 = 56\\). Correct.</p>"
                }
            ],
            "test": [
                {
                    "question": "The number of proper subsets of a set containing 4 elements is:",
                    "options": ["16", "15", "14", "8"],
                    "correctIndex": 1,
                    "solution": "Total subsets = \\(2^4 = 16\\). Proper subsets exclude the set itself, so \\(16 - 1 = 15\\)."
                }
            ]
        },
        {
            "id": "operations",
            "title": "Operations & Venn Diagrams",
            "icon": "📊",
            "precheck": {
                "question": "For any two sets A and B, \\(A \\cup (A \\cap B)\\) is equal to:",
                "options": [
                    "A",
                    "B",
                    "\\(A \\cap B\\)",
                    "U (Universal Set)"
                ],
                "correctIndex": 0,
                "passMessage": "Spot on! The intersection \\(A \\cap B\\) is perfectly contained within \\(A\\). Therefore, their union is simply \\(A\\).",
                "failMessage": "Since \\(A \\cap B\\) contains elements common to A and B, all of its elements already belong to A. Thus, adding it to A via Union doesn't change A."
            },
            "learn": {
                "paragraphs": [
                    "**Union (\\(A \\cup B\\)):** The set of all elements which are either in \\(A\\) or in \\(B\\) or in both.",
                    "**Intersection (\\(A \\cap B\\)):** The set of all elements which are common to both \\(A\\) and \\(B\\). If \\(A \\cap B = \\phi\\), the sets are **disjoint**.",
                    "**Difference (\\(A - B\\)):** The set of elements which belong to \\(A\\) but not to \\(B\\).",
                    "**Complement (\\(A'\\) or \\(A^c\\)):** The set of all elements of the universal set \\(U\\) which are not in \\(A\\). \\(A' = U - A\\).",
                    "**De Morgan's Laws:**",
                    "1) \\((A \\cup B)' = A' \\cap B'\\)",
                    "2) \\((A \\cap B)' = A' \\cup B'\\)"
                ],
                "formulas": [
                    {
                        "rule": "Cardinality Formula (2 Sets)",
                        "formula": "\\(n(A \\cup B) = n(A) + n(B) - n(A \\cap B)\\)",
                        "example": "Used for practical problems."
                    },
                    {
                        "rule": "Difference",
                        "formula": "\\(A - B = A \\cap B'\\)",
                        "example": "Elements strictly in A."
                    }
                ],
                "boxes": [
                    {
                        "type": "success",
                        "html": "<strong>Venn Diagrams:</strong> In a Venn Diagram, the Universal Set \\(U\\) is represented by a rectangle, and subsets are circles inside it. Shading regions is the best way to prove set identities."
                    },
                    {
                        "type": "info",
                        "html": "<strong>Keyword Translation for Practical Problems:</strong> 'At least one of A or B' = Union \\((A \\cup B)\\). 'Both A and B' = Intersection \\((A \\cap B)\\). 'A but not B' = Difference \\(A - B\\)."
                    }
                ]
            },
            "practice": [
                {
                    "question": "Let \\(A = \\{1, 2, 3, 4\\}\\) and \\(B = \\{3, 4, 5, 6\\}\\). Find \\(A - B\\).",
                    "options": [
                        "\\(\\{1, 2\\}\\)",
                        "\\(\\{5, 6\\}\\)",
                        "\\(\\{3, 4\\}\\)",
                        "\\(\\{1, 2, 5, 6\\}\\)"
                    ],
                    "correctIndex": 0,
                    "solution": "<p>\\(A - B\\) consists of elements that are strictly in \\(A\\) but NOT in \\(B\\).</p><p>Remove common elements \\(\\{3, 4\\}\\) from \\(A\\).</p><p>\\(A - B = \\{1, 2\\}\\).</p>"
                },
                {
                    "question": "If \\(U = \\{1, 2, 3, 4, 5, 6, 7, 8, 9\\}\\) and \\(A = \\{2, 4, 6, 8\\}\\), find \\(A'\\).",
                    "options": [
                        "\\(\\{1, 3, 5, 7, 9\\}\\)",
                        "\\(\\{1, 2, 3, 5, 7, 9\\}\\)",
                        "\\(\\{2, 4, 6, 8\\}\\)",
                        "\\(\\phi\\)"
                    ],
                    "correctIndex": 0,
                    "solution": "<p>\\(A' = U - A\\).</p><p>Elements of \\(U\\) not in \\(A\\) are odd numbers.</p><p>\\(A' = \\{1, 3, 5, 7, 9\\}\\).</p>"
                },
                {
                    "question": "If \\(n(A) = 20\\), \\(n(B) = 30\\) and \\(n(A \\cup B) = 40\\), evaluate \\(n(A \\cap B)\\).",
                    "options": ["10", "20", "50", "0"],
                    "correctIndex": 0,
                    "solution": "<p>Use the formula: \\(n(A \\cup B) = n(A) + n(B) - n(A \\cap B)\\)</p><p>\\(40 = 20 + 30 - n(A \\cap B)\\)</p><p>\\(40 = 50 - n(A \\cap B)\\)</p><p>\\(n(A \\cap B) = 10\\).</p>"
                }
            ],
            "pyq": [
                {
                    "question": "[Class 11 CBSE] In a group of 400 people, 250 can speak Hindi and 200 can speak English. How many people can speak both Hindi and English? (Assuming everyone speaks at least one language).",
                    "options": ["50", "100", "150", "0"],
                    "correctIndex": 0,
                    "solution": "<p>Let \\(H\\) be people speaking Hindi and \\(E\\) be people speaking English.</p><p>Given: \\(n(H \\cup E) = 400\\) (since everyone speaks at least one).</p><p>\\(n(H) = 250\\), \\(n(E) = 200\\).</p><p>\\(n(H \\cup E) = n(H) + n(E) - n(H \\cap E)\\)</p><p>\\(400 = 250 + 200 - n(H \\cap E)\\)</p><p>\\(400 = 450 - n(H \\cap E)\\)</p><p>\\(n(H \\cap E) = 50\\).</p>"
                }
            ],
            "test": [
                {
                    "question": "If A and B are two disjoint sets, then \\(n(A \\cup B)\\) is equal to:",
                    "options": [
                        "\\(n(A) + n(B)\\)",
                        "\\(n(A) - n(B)\\)",
                        "\\(n(A) \\cdot n(B)\\)",
                        "0"
                    ],
                    "correctIndex": 0,
                    "solution": "For disjoint sets, \\(n(A \\cap B) = 0\\). Using the formula, \\(n(A \\cup B) = n(A) + n(B) - 0 = n(A) + n(B)\\)."
                },
                {
                    "question": "For any two sets A and B, \\(A - B\\) is equal to:",
                    "options": [
                        "\\(A \\cap B'\\)",
                        "\\(A' \\cap B\\)",
                        "\\(A \\cup B'\\)",
                        "\\(A' \\cup B\\)"
                    ],
                    "correctIndex": 0,
                    "solution": "\\(A - B\\) means elements in A AND NOT in B. This translates directly to \\(A \\cap B'\\)."
                }
            ]
        }
    ],
    "chapterTest": {
        "title": "Chapter 1 Test: Sets",
        "description": "30 minutes \u00b7 Comprehensive exam on Set Theory, Operations & Venn Diagrams \u00b7 Pass mark 70%",
        "passPercent": 70,
        "questions": [
            {
                "concept": "Sets",
                "question": "Which of the following sets are equal? \\(A = \\{x : x \\text{ is a letter in the word FOLLOW}\\}\\), \\(B = \\{x : x \\text{ is a letter in the word WOLF}\\}\\)",
                "options": [
                    "A and B are equal",
                    "A and B are disjoint",
                    "A is subset of B but not equal",
                    "B is subset of A but not equal"
                ],
                "correctIndex": 0,
                "solution": "Roster forms: \\(A = \\{F, O, L, W\\}\\). \\(B = \\{W, O, L, F\\}\\). Both sets contain the exact same elements. So, \\(A = B\\)."
            },
            {
                "concept": "Subsets",
                "question": "If a set has 3 elements, what is the number of subsets of the set?",
                "options": ["8", "6", "9", "4"],
                "correctIndex": 0,
                "solution": "Number of subsets = \\(2^n\\). If \\(n = 3\\), subsets = \\(2^3 = 8\\)."
            },
            {
                "concept": "Operations",
                "question": "In a school, there are 20 teachers who teach mathematics or physics. Of these, 12 teach mathematics and 4 teach both physics and mathematics. How many teach physics?",
                "options": ["12", "8", "16", "20"],
                "correctIndex": 0,
                "solution": "Use \\(n(M \\cup P) = n(M) + n(P) - n(M \\cap P)\\).<br>\\(20 = 12 + n(P) - 4\\)<br>\\(20 = 8 + n(P)\\)<br>\\(n(P) = 12\\)."
            },
            {
                "concept": "Complement",
                "question": "Let \\(U = \\{1, 2, 3, 4, 5, 6, 7\\}\\), \\(A = \\{2, 4, 6\\}\\), \\(B = \\{3, 5\\}\\) and \\(C = \\{1, 2, 4, 7\\}\\). Find \\((A \\cup B)'\\).",
                "options": ["{1, 7}", "{1, 2, 3, 7}", "{2, 4}", "{1, 2, 4, 7}"],
                "correctIndex": 0,
                "solution": "\\(A \\cup B = \\{2, 3, 4, 5, 6\\}\\). The complement relates to elements in U but not in this union: \\(\\{1, 7\\}\\)."
            },
            {
                "concept": "De Morgan",
                "question": "\\((A \\cap B)'\\) is equal to:",
                "options": [
                    "\\(A' \\cup B'\\)",
                    "\\(A' \\cap B'\\)",
                    "\\(A \\cup B\\)",
                    "\\(A' - B'\\)"
                ],
                "correctIndex": 0,
                "solution": "By De Morgan's Law, the complement of an intersection is the union of the complements: \\(A' \\cup B'\\)."
            }
        ]
    },
    "completion": {
        "title": "Mastered Chapter 1! \ud83c\udf89",
        "message": "Congratulations! You successfully finished the first chapter of Class 11 Mathematics. You now have a solid foundation in Set Theory.",
        "nextChapter": {
            "label": "Next Chapter: Relations & Functions",
            "url": "/class-11-maths/chapter-2-relations-functions.html"
        }
    }
};

fs.writeFileSync('class-11-maths/chapter-1-data.json', JSON.stringify(data, null, 4));
console.log('chapter-1-data.json written for class 11!');
