const fs = require('fs');
const path = 'class-11-maths/chapter-1-data.json';
let data = JSON.parse(fs.readFileSync(path, 'utf8'));

// Concept 1: Intro & Representation
data.concepts[0].practice.push(
    {
        "question": "Write the set \\(B = \\{x : x \\text{ is a two-digit natural number such that the sum of its digits is } 8\\}\\) in roster form.",
        "options": [
            "\\(\\{17, 26, 35, 44, 53, 62, 71, 80\\}\\)",
            "\\(\\{17, 26, 35, 44, 53, 62, 71\\}\\)",
            "\\(\\{08, 17, 26, 35, 44, 53, 62, 71, 80\\}\\)",
            "\\(\\{17, 26, 35, 53, 62, 71, 80\\}\\)"
        ],
        "correctIndex": 0,
        "solution": "<p>Two digit natural numbers where sum of digits is 8:</p><p>1+7=8 $\\Rightarrow$ 17</p><p>2+6=8 $\\Rightarrow$ 26</p><p>3+5=8 $\\Rightarrow$ 35</p><p>4+4=8 $\\Rightarrow$ 44</p><p>5+3=8 $\\Rightarrow$ 53</p><p>6+2=8 $\\Rightarrow$ 62</p><p>7+1=8 $\\Rightarrow$ 71</p><p>8+0=8 $\\Rightarrow$ 80</p><p>(08 is a one-digit number, so it is excluded). Thus: \\(\\{17, 26, 35, 44, 53, 62, 71, 80\\}\\).</p>"
    },
    {
        "question": "Which of the following sets is infinite?",
        "options": [
            "The set of months of a year",
            "\\(\\{1, 2, 3, ...\\}\\)",
            "The set of letters in the English alphabet",
            "The set of prime numbers less than 99"
        ],
        "correctIndex": 1,
        "solution": "<p>A) Finite (12 months).</p><p>B) This is the set of natural numbers, which has no end. Thus, it is infinite.</p><p>C) Finite (26 letters).</p><p>D) Finite (Prime numbers less than 99 are countable).</p>"
    }
);

// Concept 2: Types of Sets
data.concepts[1].practice.push(
    {
        "question": "If \\(A = \\{x : x \\in R, x^2 - 8x + 12 = 0\\}\\) and \\(B = \\{2, 4, 6\\}\\), then which applies?",
        "options": [
            "\\(A \\subset B\\)",
            "\\(B \\subset A\\)",
            "\\(A = B\\)",
            "\\(A \\cap B = \\phi\\)"
        ],
        "correctIndex": 0,
        "solution": "<p>Solve \\(x^2 - 8x + 12 = 0\\).</p><p>\\((x - 2)(x - 6) = 0 \\Rightarrow x = 2, 6\\).</p><p>So, \\(A = \\{2, 6\\}\\).</p><p>Since all elements of \\(A\\) are present in \\(B = \\{2, 4, 6\\}\\), we can say \\(A \\subset B\\).</p>"
    },
    {
        "question": "Two finite sets have \\(m\\) and \\(n\\) elements. The number of subsets of the first set is 112 more than that of the second set. The values of \\(m\\) and \\(n\\) are:",
        "options": [
            "m = 4, n = 7",
            "m = 7, n = 4",
            "m = 8, n = 5",
            "m = 5, n = 8"
        ],
        "correctIndex": 1,
        "solution": "<p>Given \\(2^m - 2^n = 112\\).</p><p>Let's check options. For \\(m = 7, n = 4\\):</p><p>\\(2^7 - 2^4 = 128 - 16 = 112\\).</p><p>Thus, \\(m = 7, n = 4\\) is correct.</p>"
    }
);

data.concepts[1].pyq.push(
    {
        "question": "[School Exam] Let \\(A = \\{a, b, c, d\\}\\), \\(B = \\{a, b, c\\}\\) and \\(C = \\{b, d\\}\\). Find the set \\(X\\) such that \\(X \\subset B\\) and \\(X \\subset C\\).",
        "options": [
            "\\(\\{b\\}\\) and \\(\\phi\\)",
            "\\(\\{b, c\\}\\)",
            "\\(\\{a, d\\}\\)",
            "\\(\\{a, b, c, d\\}\\)"
        ],
        "correctIndex": 0,
        "solution": "<p>If \\(X \\subset B\\) and \\(X \\subset C\\), then \\(X\\) must be a subset of their intersection \\(B \\cap C\\).</p><p>\\(B \\cap C = \\{a, b, c\\} \\cap \\{b, d\\} = \\{b\\}\\).</p><p>The subsets of \\(\\{b\\}\\) are the empty set \\(\\phi\\) and the set \\(\\{b\\}\\) itself.</p>"
    }
);

// Concept 3: Operations & Venn Diagrams
data.concepts[2].practice.push(
    {
        "question": "In a town of 10000 families, it was found that 40% subscribe to newspaper A, 20% to newspaper B, and 10% to newspaper C. 5% read A and B, 3% read B and C, and 4% read A and C. If 2% read all three, find the number of families which read none of the newspapers.",
        "options": ["3000", "4000", "5000", "6000"],
        "correctIndex": 1,
        "solution": "<p>Let the total percentage be 100%.</p><p>\\(n(A) = 40, n(B) = 20, n(C) = 10\\).</p><p>\\(n(A \\cap B) = 5, n(B \\cap C) = 3, n(A \\cap C) = 4\\).</p><p>\\(n(A \\cap B \\cap C) = 2\\).</p><p>Formula: \\(n(A \\cup B \\cup C) = n(A) + n(B) + n(C) - n(A \\cap B) - n(B \\cap C) - n(A \\cap C) + n(A \\cap B \\cap C)\\)</p><p>\\(n(A \\cup B \\cup C) = 40 + 20 + 10 - 5 - 3 - 4 + 2 = 60\\%\\).</p><p>So 60% read at least one. Thus, \\(100\\% - 60\\% = 40\\%\\) read none.</p><p>40% of 10000 = 4000 families.</p>"
    },
    {
        "question": "If \\(A\\) and \\(B\\) are two sets such that \\(n(A) = 115\\), \\(n(B) = 326\\), and \\(n(A-B) = 47\\), find \\(n(A \\cup B)\\).",
        "options": ["373", "394", "441", "300"],
        "correctIndex": 0,
        "solution": "<p>We know \\(n(A) = n(A-B) + n(A \\cap B)\\).</p><p>\\(115 = 47 + n(A \\cap B) \\Rightarrow n(A \\cap B) = 115 - 47 = 68\\).</p><p>Now find union: \\(n(A \\cup B) = n(A) + n(B) - n(A \\cap B)\\)</p><p>\\(n(A \\cup B) = 115 + 326 - 68 = 441 - 68 = 373\\).</p>"
    }
);

data.concepts[2].pyq.push(
    {
        "question": "[Class 11 CBSE] In a group of 65 people, 40 like cricket, 10 like both cricket and tennis. How many like tennis only and not cricket?",
        "options": ["25", "35", "15", "40"],
        "correctIndex": 0,
        "solution": "<p>Let \\(C\\) = cricket, \\(T\\) = tennis. Total \\(n(C \\cup T) = 65\\).</p><p>\\(n(C) = 40\\), \\(n(C \\cap T) = 10\\).</p><p>We know \\(n(C \\cup T) = n(C) + n(T) - n(C \\cap T)\\)</p><p>\\(65 = 40 + n(T) - 10 \\Rightarrow 65 = 30 + n(T)\\) so \\(n(T) = 35\\).</p><p>People who like tennis only and NOT cricket is \\(n(T - C) = n(T) - n(C \\cap T)\\).</p><p>\\(n(T - C) = 35 - 10 = 25\\).</p>"
    }
);

fs.writeFileSync(path, JSON.stringify(data, null, 4));
console.log('Added more questions successfully!');
