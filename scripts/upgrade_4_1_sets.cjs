const cheerio = require('cheerio');
const fs = require('fs');
const path = require('path');

const file = path.join(process.cwd(), 'class-11-applied-mathematics/chapter-4-sets/4-1-sets-and-representation/index.html');
const html = fs.readFileSync(file, 'utf8');
const $ = cheerio.load(html);

// 1. LEARN TAB
const learnContent = `
    <div class="card-premium">
        <h3 class="card-title"><i class="fas fa-book-reader"></i> Comprehensive Concepts &amp; Principles: Sets and Representation</h3>
        <p class="theory-para">In mathematics and quantitative analytics, a <strong>Set</strong> is a well-defined collection of distinct objects, termed elements or members. The phrase <em>well-defined</em> means that given any object, there is an objective, unequivocal criterion to decide whether it belongs to the collection or not. In CBSE Class 11 Applied Mathematics, set theory provides the foundational language for database querying, probability sample spaces, categorical market segmentation, and relational models.</p>
        
        <div class="theory-highlight">
            <strong>Key Set Theory Foundations:</strong>
            <ul style="margin: 6px 0 0 1.2rem; padding: 0; line-height: 1.8;">
                <li><strong>Membership Notation:</strong> If an element $x$ belongs to set $A$, we write $x \\in A$. If $x$ does not belong to set $A$, we write $x \\notin A$.</li>
                <li><strong>Well-Defined vs. Subjective Collections:</strong>
                <br>• <em>Well-Defined (A Set):</em> "The collection of all natural numbers less than 10" or "All vowels in the English alphabet".
                <br>• <em>Subjective (Not a Set):</em> "The collection of the 5 most talented batsmen in the world" (talent is subjective without strict statistical criteria).</li>
                <li><strong>Standard Mathematical Sets:</strong>
                <br>• $\\mathbb{N}$: The set of all natural numbers $\\{1, 2, 3, \\dots\\}$
                <br>• $\\mathbb{W}$: The set of all whole numbers $\\{0, 1, 2, 3, \\dots\\}$
                <br>• $\\mathbb{Z}$: The set of all integers $\\{\\dots, -2, -1, 0, 1, 2, \\dots\\}$
                <br>• $\\mathbb{Q}$: The set of all rational numbers $\\{\\frac{p}{q} : p, q \\in \\mathbb{Z}, q \\neq 0\\}$
                <br>• $\\mathbb{R}$: The set of all real numbers</li>
            </ul>
        </div>
    </div>

    <div class="card-premium">
        <h3 class="card-title"><i class="fas fa-pen-fancy"></i> Methods of Representing Sets</h3>
        <p class="theory-para">A set can be mathematically specified in two primary formats:</p>
        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; margin: 1rem 0;">
            <div style="background:var(--neutral-50); border:1px solid var(--neutral-200); border-radius:8px; padding:1.25rem;">
                <h4 style="color:var(--primary-700); margin-top:0;"><i class="fas fa-list-ol"></i> 1. Roster (Tabular) Form</h4>
                <p style="margin:0 0 8px 0; font-size:0.95rem;">All elements are listed explicitly inside curly braces $\\{ \\}$, separated by commas:</p>
                <div style="font-family:var(--font-mono); font-size:0.95rem; line-height:1.8;">
                    • $V = \\{a, e, i, o, u\\}$<br>
                    • $P = \\{2, 3, 5, 7, 11\\}$<br>
                    <em>Rules:</em> Order of listing is immaterial ($\\{1, 2\\} = \\{2, 1\\}$); elements are never duplicated ($\\{\\text{M, A, T, H, E, I, C, S}\\}$ for 'MATHEMATICS').
                </div>
            </div>
            
            <div style="background:var(--neutral-50); border:1px solid var(--neutral-200); border-radius:8px; padding:1.25rem;">
                <h4 style="color:var(--primary-700); margin-top:0;"><i class="fas fa-code"></i> 2. Set-Builder Form</h4>
                <p style="margin:0 0 8px 0; font-size:0.95rem;">Elements are described by characterizing a common defining rule/property $P(x)$:</p>
                <div style="font-family:var(--font-mono); font-size:0.95rem; line-height:1.8;">
                    • $A = \\{x : x \\in \\mathbb{N} \\text{ and } x < 6\\}$<br>
                    • $B = \\{x : x = 2n, n \\in \\mathbb{N}, n \\le 5\\}$<br>
                    <em>Read as:</em> "The set of all $x$ such that $x$ satisfies property $P$."
                </div>
            </div>
        </div>
    </div>

    <div class="card-premium">
        <h3 class="card-title"><i class="fas fa-pen-nib"></i> Worked Benchmark Examples</h3>
        
        <div class="example-box">
            <strong style="color:var(--neutral-900);">Example 1 (Converting Set-Builder to Roster Form):</strong>
            <p class="theory-para" style="margin:6px 0;">Write each of the following sets in Roster (Tabular) form:
            <br>(a) $A = \\{x : x \\text{ is an integer and } -3 \\le x < 5\\}$
            <br>(b) $B = \\{x : x \\in \\mathbb{N} \\text{ and } x^2 - 5x + 6 = 0\\}$
            <br>(c) $C = \\{x : x \\text{ is a two-digit natural number such that the sum of its digits is 8}\\}$</p>
            <details class="solution-details">
                <summary>Show Step-by-Step Solution</summary>
                <div class="solution-explanation">
                    <p>• <strong>(a) $A$:</strong> Integers from $-3$ up to (but excluding) $5$:
                    $$\\mathbf{A = \\{-3, -2, -1, 0, 1, 2, 3, 4\\}}$$<br>
                    • <strong>(b) $B$:</strong> Solve $x^2 - 5x + 6 = 0 \\implies (x - 2)(x - 3) = 0 \\implies x = 2, 3$. Since both are natural numbers:
                    $$\\mathbf{B = \\{2, 3\\}}$$<br>
                    • <strong>(c) $C$:</strong> Two-digit numbers where digits add to 8: $17, 26, 35, 44, 53, 62, 71, 80$:
                    $$\\mathbf{C = \\{17, 26, 35, 44, 53, 62, 71, 80\\}}$$</p>
                </div>
            </details>
        </div>

        <div class="example-box">
            <strong style="color:var(--neutral-900);">Example 2 (Converting Roster to Set-Builder Form):</strong>
            <p class="theory-para" style="margin:6px 0;">Express the following sets in Set-Builder form:
            <br>(a) $S = \\{1, 4, 9, 16, 25, \\dots, 100\\}$
            <br>(b) $T = \\left\\{\\frac{1}{2}, \\frac{2}{3}, \\frac{3}{4}, \\frac{4}{5}, \\frac{5}{6}, \\frac{6}{7}\\right\\}$</p>
            <details class="solution-details">
                <summary>Show Step-by-Step Solution</summary>
                <div class="solution-explanation">
                    <p>• <strong>(a) $S$:</strong> Elements are perfect squares of natural numbers from $1^2$ to $10^2$:
                    $$\\mathbf{S = \\{x : x = n^2, n \\in \\mathbb{N}, 1 \\le n \\le 10\\}}$$<br>
                    • <strong>(b) $T$:</strong> Each fraction has numerator $n$ and denominator $n+1$ for $n = 1, 2, \\dots, 6$:
                    $$\\mathbf{T = \\left\\{x : x = \\frac{n}{n+1}, n \\in \\mathbb{N}, 1 \\le n \\le 6\\right\\}}$$</p>
                </div>
            </details>
        </div>
    </div>
`;
$('#tab-learn').html(learnContent);

// 2. PROGRESS TAB
const progressContent = `
    <div class="card-premium">
        <h3 class="card-title"><i class="fas fa-tasks"></i> CHECK YOUR PROGRESS 4.1</h3>
        <p class="theory-para">Graded textbook exercises on Set Concepts, Well-Defined Criteria, and Dual Representations from CBSE Class 11 Applied Mathematics.</p>
    </div>

    <div class="q-card">
        <div class="q-header-meta">
            <span class="q-number-pill">Problem 1</span>
            <span class="q-marks-pill">Well-Defined Evaluation</span>
        </div>
        <p class="q-prompt">Which of the following collections represent valid mathematical sets? Give reasons:
        <br>(a) The collection of all prime numbers less than 20.
        <br>(b) The collection of all difficult chapters in Class 11 Applied Mathematics.
        <br>(c) The collection of all months of a year beginning with the letter 'J'.</p>
        <details class="solution-details">
            <summary>Show Step-by-Step Solution</summary>
            <div class="solution-explanation">
                <p>• <strong>(a) Is a Set:</strong> Whether a number is prime and $< 20$ is mathematically definitive: $\\{2, 3, 5, 7, 11, 13, 17, 19\\}$.<br>
                • <strong>(b) Not a Set:</strong> "Difficult" is a subjective judgment that varies from student to student without an objective boundary.<br>
                • <strong>(c) Is a Set:</strong> Well-defined: $\\{\\text{January, June, July}\\}$.</p>
            </div>
        </details>
    </div>

    <div class="q-card">
        <div class="q-header-meta">
            <span class="q-number-pill">Problem 2</span>
            <span class="q-marks-pill">Roster Conversion</span>
        </div>
        <p class="q-prompt">Write the set of all letters in the word "COMMISSION" in Roster form.</p>
        <details class="solution-details">
            <summary>Show Step-by-Step Solution</summary>
            <div class="solution-explanation">
                <p>• In roster form, duplicated letters are written only once.<br>
                • Unique letters: C, O, M, I, S, N.<br>
                • $\\mathbf{\\{C, O, M, I, S, N\\}}$.</p>
            </div>
        </details>
    </div>

    <div class="q-card">
        <div class="q-header-meta">
            <span class="q-number-pill">Problem 3</span>
            <span class="q-marks-pill">Set-Builder Pattern</span>
        </div>
        <p class="q-prompt">Write the set $D = \\{5, 25, 125, 625\\}$ in Set-Builder form.</p>
        <details class="solution-details">
            <summary>Show Step-by-Step Solution</summary>
            <div class="solution-explanation">
                <p>• Elements are powers of 5: $5^1, 5^2, 5^3, 5^4$.<br>
                • $\\mathbf{D = \\{x : x = 5^n, n \\in \\mathbb{N}, 1 \\le n \\le 4\\}}$.</p>
            </div>
        </details>
    </div>

    <div class="q-card">
        <div class="q-header-meta">
            <span class="q-number-pill">Problem 4</span>
            <span class="q-marks-pill">Equation Solution Set</span>
        </div>
        <p class="q-prompt">Write the solution set of the equation $x^2 + x - 2 = 0$ in roster form for $x \\in \\mathbb{R}$.</p>
        <details class="solution-details">
            <summary>Show Step-by-Step Solution</summary>
            <div class="solution-explanation">
                <p>• $x^2 + x - 2 = 0 \\implies (x + 2)(x - 1) = 0 \\implies x = 1, -2$.<br>
                • Both roots are real numbers.<br>
                • $\\mathbf{\\{-2, 1\\}}$.</p>
            </div>
        </details>
    </div>

    <div class="q-card">
        <div class="q-header-meta">
            <span class="q-number-pill">Problem 5</span>
            <span class="q-marks-pill">Membership Notation</span>
        </div>
        <p class="q-prompt">Let $A = \\{1, 2, \\{3, 4\\}, 5\\}$. State whether each statement is True or False:
        <br>(a) $\\{3, 4\\} \\in A$
        <br>(b) $3 \\in A$
        <br>(c) $5 \\in A$.</p>
        <details class="solution-details">
            <summary>Show Step-by-Step Solution</summary>
            <div class="solution-explanation">
                <p>• (a) <strong>TRUE:</strong> The set $\\{3, 4\\}$ is itself an element of $A$.<br>
                • (b) <strong>FALSE:</strong> The individual number 3 is an element of $\\{3, 4\\}$, but not a direct member of $A$.<br>
                • (c) <strong>TRUE:</strong> 5 is explicitly listed as a direct member of $A$.</p>
            </div>
        </details>
    </div>
`;
$('#tab-progress').html(progressContent);

// 3. WORKSHEET TAB
const worksheetContent = `
    <div class="card-premium">
        <h3 class="card-title"><i class="fas fa-file-alt"></i> Comprehensive Practice Worksheet: Sets &amp; Representation</h3>
        <p class="theory-para">Graded problems matching CBSE Class 11 Applied Mathematics examination blueprint.</p>
    </div>

    <div class="card-premium">
        <h4 style="color:var(--primary-700); margin-top:0;">SECTION A: 1-Mark Objective &amp; Conceptual Questions</h4>
        
        <div class="q-card">
            <p class="q-prompt"><strong>Q1:</strong> Define a 'Set' in mathematics.</p>
            <details class="solution-details">
                <summary>Show Answer &amp; Scheme</summary>
                <div class="solution-explanation">
                    <p><strong>Definition [1 Mark]:</strong> A set is a well-defined collection of distinct objects.</p>
                </div>
            </details>
        </div>

        <div class="q-card">
            <p class="q-prompt"><strong>Q2:</strong> Represent the set $E = \\{x : x \\text{ is an even prime number}\\}$ in roster form.</p>
            <details class="solution-details">
                <summary>Show Answer &amp; Scheme</summary>
                <div class="solution-explanation">
                    <p>$$\\mathbf{\\{2\\}} \\quad [1 \\text{ Mark}]$$</p>
                </div>
            </details>
        </div>
    </div>

    <div class="card-premium">
        <h4 style="color:var(--primary-700); margin-top:0;">SECTION B: 2-Mark Short Answer Problems</h4>
        
        <div class="q-card">
            <p class="q-prompt"><strong>Q3:</strong> State the two primary rules to be followed when writing a set in Roster (Tabular) form.</p>
            <details class="solution-details">
                <summary>Show Answer &amp; Scheme</summary>
                <div class="solution-explanation">
                    <p><strong>Rules [2 Marks]:</strong><br>
                    (1) <strong>No Duplication:</strong> An element is not repeated; each distinct member is listed once.<br>
                    (2) <strong>Order Immaterial:</strong> The sequence or order in which elements are listed inside the braces does not alter the set.</p>
                </div>
            </details>
        </div>

        <div class="q-card">
            <p class="q-prompt"><strong>Q4:</strong> Write the set $A = \\{2, 4, 8, 16, 32\\}$ in set-builder form.</p>
            <details class="solution-details">
                <summary>Show Answer &amp; Scheme</summary>
                <div class="solution-explanation">
                    <p>$$\\mathbf{A = \\{x : x = 2^n, n \\in \\mathbb{N}, 1 \\le n \\le 5\\}} \\quad [2 \\text{ Marks}]$$</p>
                </div>
            </details>
        </div>
    </div>

    <div class="card-premium">
        <h4 style="color:var(--primary-700); margin-top:0;">SECTION C: 4-Mark Comprehensive Scenario Drill</h4>
        
        <div class="q-card">
            <p class="q-prompt"><strong>Q5:</strong> An e-commerce platform stores customer loyalty tiers based on annual order counts ($n \\in \\mathbb{N}$):
            <br>• Tier Alpha: $\\{n : n \\in \\mathbb{N}, n \\le 5\\}$
            <br>• Tier Beta: $\\{n : n = 2k + 1, k \\in \\mathbb{W}, 3 \\le k \\le 7\\}$
            <br>• Tier Gamma: $\\{n : n \\in \\mathbb{N}, n^2 - 12n + 35 = 0\\}$
            <br>(i) Express Tier Alpha in Roster form.
            <br>(ii) Express Tier Beta in Roster form.
            <br>(iii) Express Tier Gamma in Roster form.
            <br>(iv) Identify if any order count qualifies a customer for both Tier Beta and Tier Gamma simultaneously.</p>
            <details class="solution-details">
                <summary>Show Step-by-Step Solution &amp; Marking Scheme</summary>
                <div class="solution-explanation">
                    <p><strong>Part (i) Tier Alpha [1 Mark]:</strong> Natural numbers $\\le 5$: $\\mathbf{\\{1, 2, 3, 4, 5\\}}$.<br>
                    <strong>Part (ii) Tier Beta [1 Mark]:</strong> $k = 3, 4, 5, 6, 7 \\implies n = 7, 9, 11, 13, 15$: $\\mathbf{\\{7, 9, 11, 13, 15\\}}$.<br>
                    <strong>Part (iii) Tier Gamma [1 Mark]:</strong> $n^2 - 12n + 35 = 0 \\implies (n-5)(n-7) = 0 \\implies n = 5, 7$: $\\mathbf{\\{5, 7\\}}$.<br>
                    <strong>Part (iv) Overlap [1 Mark]:</strong> The value $\\mathbf{n = 7}$ belongs to both Tier Beta and Tier Gamma.</p>
                </div>
            </details>
        </div>
    </div>
`;
$('#tab-worksheet').html(worksheetContent);

// 4. REVISION TAB
const revisionContent = `
    <div class="card-premium">
        <h3 class="card-title"><i class="fas fa-bolt"></i> High-Yield Quick Revision: Sets &amp; Representation</h3>
        <p class="theory-para">Summary of notation, representation modes, and standard number systems for Chapter 4.1.</p>
    </div>

    <div class="card-premium">
        <h4 style="color:var(--primary-700); margin-top:0;"><i class="fas fa-table"></i> Roster vs. Set-Builder Comparison</h4>
        <div style="overflow-x:auto;">
            <table class="audit-table" style="width:100%; border-collapse:collapse; margin-top:0.5rem;">
                <thead>
                    <tr style="background:var(--neutral-100); text-align:left;">
                        <th style="padding:10px; border:1px solid var(--neutral-300);">Feature</th>
                        <th style="padding:10px; border:1px solid var(--neutral-300);">Roster Form</th>
                        <th style="padding:10px; border:1px solid var(--neutral-300);">Set-Builder Form</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td style="padding:10px; border:1px solid var(--neutral-300); font-weight:600;">Format</td>
                        <td style="padding:10px; border:1px solid var(--neutral-300); font-family:var(--font-mono);">$\\{a_1, a_2, a_3, \\dots\\}$</td>
                        <td style="padding:10px; border:1px solid var(--neutral-300); font-family:var(--font-mono);">$\\{x : P(x)\\}$</td>
                    </tr>
                    <tr>
                        <td style="padding:10px; border:1px solid var(--neutral-300); font-weight:600;">Best Used For</td>
                        <td style="padding:10px; border:1px solid var(--neutral-300);">Small finite sets or clear enumerations</td>
                        <td style="padding:10px; border:1px solid var(--neutral-300);">Large/infinite sets governed by a mathematical formula</td>
                    </tr>
                    <tr>
                        <td style="padding:10px; border:1px solid var(--neutral-300); font-weight:600;">Example</td>
                        <td style="padding:10px; border:1px solid var(--neutral-300); font-family:var(--font-mono);">$\\{2, 4, 6, 8\\}$</td>
                        <td style="padding:10px; border:1px solid var(--neutral-300); font-family:var(--font-mono);">$\\{x : x = 2n, n \\in \\mathbb{N}, n \\le 4\\}$</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>

    <div class="card-premium">
        <h4 style="color:var(--primary-700); margin-top:0;"><i class="fas fa-lightbulb"></i> Critical Examination Trap</h4>
        <p style="margin:0; font-size:0.95rem; line-height:1.8;">
            Never duplicate elements when writing words in roster form! For instance, the letters of "BETTER" must be written as $\\{B, E, T, R\\}$, <strong>not</strong> $\\{B, E, T, T, E, R\\}$.
        </p>
    </div>
`;
$('#tab-revision').html(revisionContent);

// 5. MOCK EXAM TAB
const mockContent = `
    <div class="card-premium">
        <h3 class="card-title"><i class="fas fa-graduation-cap"></i> 10-Question Diagnostic Board Mock Examination: Sets &amp; Representation</h3>
        <p class="theory-para">Timed exam: 4 Objective MCQs / Assertion-Reason with instant automatic grading, plus 6 multi-mark subjective problems with CBSE marking rubrics.</p>
    </div>

    <div class="card-premium">
        <h4 style="color:var(--primary-700); margin-top:0;">PART 1: Objective Section (4 Marks)</h4>
        
        <div class="q-card">
            <p class="q-prompt"><strong>Q1:</strong> Which of the following is a well-defined set?</p>
            <div style="display:flex; flex-direction:column; gap:8px; margin:10px 0;">
                <label><input type="radio" name="mock_q1" value="A"> (A) The collection of beautiful flowers in a garden</label>
                <label><input type="radio" name="mock_q1" value="B"> (B) The collection of honest corporate managers in India</label>
                <label><input type="radio" name="mock_q1" value="C"> (C) The collection of all prime numbers less than 15</label>
                <label><input type="radio" name="mock_q1" value="D"> (D) The collection of difficult questions in a textbook</label>
            </div>
            <div id="mock-sol-1" style="display:none; background:var(--neutral-100); padding:10px; border-radius:6px; margin-top:8px;">
                <strong>Solution:</strong> (C) Prime numbers less than 15 have an objective, unambiguous mathematical definition.
            </div>
        </div>

        <div class="q-card">
            <p class="q-prompt"><strong>Q2:</strong> The set $\\{x : x \\in \\mathbb{Z}, x^2 < 10\\}$ in roster form is:</p>
            <div style="display:flex; flex-direction:column; gap:8px; margin:10px 0;">
                <label><input type="radio" name="mock_q2" value="A"> (A) $\\{1, 2, 3\\}$</label>
                <label><input type="radio" name="mock_q2" value="B"> (B) $\\{0, 1, 2, 3\\}$</label>
                <label><input type="radio" name="mock_q2" value="C"> (C) $\\{-3, -2, -1, 0, 1, 2, 3\\}$</label>
                <label><input type="radio" name="mock_q2" value="D"> (D) $\\{-3, 3\\}$</label>
            </div>
            <div id="mock-sol-2" style="display:none; background:var(--neutral-100); padding:10px; border-radius:6px; margin-top:8px;">
                <strong>Solution:</strong> (C) Integers whose squares are $< 10$ are $-3, -2, -1, 0, 1, 2, 3$.
            </div>
        </div>

        <div class="q-card">
            <p class="q-prompt"><strong>Q3:</strong> The set of all letters in the word "TRIGONOMETRY" in tabular form has how many distinct elements?</p>
            <div style="display:flex; flex-direction:column; gap:8px; margin:10px 0;">
                <label><input type="radio" name="mock_q3" value="A"> (A) 12</label>
                <label><input type="radio" name="mock_q3" value="B"> (B) 9</label>
                <label><input type="radio" name="mock_q3" value="C"> (C) 10</label>
                <label><input type="radio" name="mock_q3" value="D"> (D) 8</label>
            </div>
            <div id="mock-sol-3" style="display:none; background:var(--neutral-100); padding:10px; border-radius:6px; margin-top:8px;">
                <strong>Solution:</strong> (B) Unique letters: T, R, I, G, O, N, M, E, Y (9 distinct letters).
            </div>
        </div>

        <div class="q-card">
            <p class="q-prompt"><strong>Q4 (Assertion-Reason):</strong><br>
            <strong>Assertion (A):</strong> The collection $\\{1, 2, 2, 3\\}$ and $\\{1, 2, 3\\}$ represent the exact same mathematical set.<br>
            <strong>Reason (R):</strong> In set theory, the repetition of an element in roster form is redundant and does not change the membership of the set.</p>
            <div style="display:flex; flex-direction:column; gap:8px; margin:10px 0;">
                <label><input type="radio" name="mock_q4" value="A"> (A) Both (A) and (R) are true and (R) is the correct explanation of (A)</label>
                <label><input type="radio" name="mock_q4" value="B"> (B) Both (A) and (R) are true but (R) is NOT the correct explanation of (A)</label>
                <label><input type="radio" name="mock_q4" value="C"> (C) (A) is true but (R) is false</label>
                <label><input type="radio" name="mock_q4" value="D"> (D) (A) is false but (R) is true</label>
            </div>
            <div id="mock-sol-4" style="display:none; background:var(--neutral-100); padding:10px; border-radius:6px; margin-top:8px;">
                <strong>Solution:</strong> (A) Both Assertion and Reason are true and Reason provides the fundamental rule of set definition.
            </div>
        </div>

        <div style="margin-top:15px;">
            <button type="button" class="btn btn-primary" onclick="gradeObjectiveSection()">Submit &amp; Grade Objective Section</button>
            <div id="obj-result-box" style="display:none; margin-top:10px; font-weight:bold; font-size:1.1rem;"></div>
        </div>
    </div>

    <div class="card-premium">
        <h4 style="color:var(--primary-700); margin-top:0;">PART 2: Subjective Section (Q5 - Q10)</h4>
        
        <div class="q-card">
            <div class="q-header-meta">
                <span class="q-number-pill">Q5</span>
                <span class="q-marks-pill">2 Marks</span>
            </div>
            <p class="q-prompt">Write the set $A = \\{x : x \\in \\mathbb{Z}, x^2 - 9 = 0\\}$ in roster form.</p>
            <details class="solution-details">
                <summary>Show Step-by-Step Solution &amp; Marking Scheme</summary>
                <div class="solution-explanation">
                    <p>• $x^2 - 9 = 0 \\implies x^2 = 9 \\implies x = \\pm 3$ [1 Mark].<br>
                    • Both $+3$ and $-3$ are integers.<br>
                    • $\\mathbf{A = \\{-3, 3\\}}$ [1 Mark].</p>
                </div>
            </details>
        </div>

        <div class="q-card">
            <div class="q-header-meta">
                <span class="q-number-pill">Q6</span>
                <span class="q-marks-pill">2 Marks</span>
            </div>
            <p class="q-prompt">Write the set $B = \\{1, 8, 27, 64, 125\\}$ in set-builder form.</p>
            <details class="solution-details">
                <summary>Show Step-by-Step Solution &amp; Marking Scheme</summary>
                <div class="solution-explanation">
                    <p>• Elements are cubes of the first 5 natural numbers: $1^3, 2^3, 3^3, 4^3, 5^3$ [1 Mark].<br>
                    • $\\mathbf{B = \\{x : x = n^3, n \\in \\mathbb{N}, 1 \\le n \\le 5\\}}$ [1 Mark].</p>
                </div>
            </details>
        </div>

        <div class="q-card">
            <div class="q-header-meta">
                <span class="q-number-pill">Q7</span>
                <span class="q-marks-pill">3 Marks</span>
            </div>
            <p class="q-prompt">State whether the following are sets. Justify your answer mathematically:
            <br>(a) The collection of all honest politicians in India.
            <br>(b) The collection of all roots of the equation $2x^3 - 3x^2 - 11x + 6 = 0$.
            <br>(c) The collection of all intelligent students in a school.</p>
            <details class="solution-details">
                <summary>Show Step-by-Step Solution &amp; Marking Scheme</summary>
                <div class="solution-explanation">
                    <p>• (a) <strong>Not a set [1 Mark]:</strong> "Honest" is an uncalibrated subjective virtue, lacking an objective boundary.<br>
                    • (b) <strong>Is a set [1 Mark]:</strong> The roots of a polynomial equation are mathematically determined and well-defined.<br>
                    • (c) <strong>Not a set [1 Mark]:</strong> "Intelligent" is a qualitative relative adjective without standard defining criteria.</p>
                </div>
            </details>
        </div>

        <div class="q-card">
            <div class="q-header-meta">
                <span class="q-number-pill">Q8</span>
                <span class="q-marks-pill">3 Marks</span>
            </div>
            <p class="q-prompt">Let $A = \\{x : x \\text{ is a letter in the word 'MATHEMATICS'}\\}$.
            <br>(i) Write $A$ in roster form.
            <br>(ii) Find the cardinal number $n(A)$.
            <br>(iii) State whether $P \\in A$ and $M \\in A$.</p>
            <details class="solution-details">
                <summary>Show Step-by-Step Solution &amp; Marking Scheme</summary>
                <div class="solution-explanation">
                    <p>• (i) Roster Form: $\\mathbf{\\{M, A, T, H, E, I, C, S\\}}$ [1 Mark].<br>
                    • (ii) Cardinal Number: Count of distinct elements is $\\mathbf{n(A) = 8}$ [1 Mark].<br>
                    • (iii) $P \\notin A$ (False) and $M \\in A$ (True) [1 Mark].</p>
                </div>
            </details>
        </div>

        <div class="q-card">
            <div class="q-header-meta">
                <span class="q-number-pill">Q9 &amp; Q10</span>
                <span class="q-marks-pill">Case Study (4 Marks Total)</span>
            </div>
            <div style="background:var(--neutral-50); border-left:4px solid var(--primary-600); padding:1rem; margin-bottom:1rem;">
                <p style="margin:0; font-weight:600; color:var(--neutral-900);">
                    Case Context: Relational Database Query Filtering
                </p>
                <p style="margin:6px 0 0; font-size:0.95rem; color:var(--neutral-700);">
                    A relational database engineer defines three SQL customer record sets from table \`Orders\` with integer Order IDs ($x \\in \\mathbb{N}$):
                    <br>• $S_1 = \\{x : x = 3k, k \\in \\mathbb{N}, k \\le 6\\}$
                    <br>• $S_2 = \\{x : x = 2m, m \\in \\mathbb{N}, m \\le 9\\}$
                </p>
            </div>
            <p class="q-prompt" style="font-weight:600;">
                <strong>Q9 (2 Marks):</strong> List both sets $S_1$ and $S_2$ in Roster form.<br>
                <strong>Q10 (2 Marks):</strong> Write the set of Order IDs that belong to BOTH $S_1$ and $S_2$ in set-builder form.
            </p>
            <details class="solution-details">
                <summary>Show Step-by-Step Solution &amp; Marking Scheme</summary>
                <div class="solution-explanation">
                    <p><strong>Solution to Q9 [2 Marks]:</strong><br>
                    • $S_1 = \\{3, 6, 9, 12, 15, 18\\}$.<br>
                    • $S_2 = \\{2, 4, 6, 8, 10, 12, 14, 16, 18\\}$.</p>
                    <p><strong>Solution to Q10 [2 Marks]:</strong><br>
                    • Common elements are multiples of both 2 and 3 (i.e. multiples of 6) up to 18: $\\{6, 12, 18\\}$.<br>
                    • In Set-Builder form:
                    $$\\mathbf{\\{x : x = 6n, n \\in \\mathbb{N}, 1 \\le n \\le 3\\}}$$</p>
                </div>
            </details>
        </div>
    </div>
`;
$('#tab-mock').html(mockContent);

// 6. UPDATE MOCK SCRIPT
const mockData = [
    {"ans": "C", "sol": "Prime numbers less than 15 is an objective, well-defined mathematical set."},
    {"ans": "C", "sol": "Integers with squares < 10 are {-3, -2, -1, 0, 1, 2, 3}."},
    {"ans": "B", "sol": "Unique letters of TRIGONOMETRY are T, R, I, G, O, N, M, E, Y (9 distinct letters)."},
    {"ans": "A", "sol": "Both Assertion and Reason are true and Reason provides the fundamental rule."}
];

const scriptTag = `
<script>
    window.mockObjectiveData = ${JSON.stringify(mockData, null, 8)};

    function gradeObjectiveSection() {
        let score = 0;
        let total = window.mockObjectiveData.length;
        window.mockObjectiveData.forEach((item, index) => {
            let qNum = index + 1;
            let selected = document.querySelector('input[name="mock_q' + qNum + '"]:checked');
            let solBox = document.getElementById('mock-sol-' + qNum);
            if (solBox) solBox.style.display = 'block';
            if (selected && selected.value === item.ans) {
                score++;
            }
        });
        let resultBox = document.getElementById('obj-result-box');
        if (resultBox) {
            resultBox.style.display = 'block';
            resultBox.innerHTML = 'Your Score: ' + score + ' / ' + total + ' (' + Math.round((score/total)*100) + '%)';
            resultBox.style.color = (score >= 3) ? '#16a34a' : '#dc2626';
        }
    }
</script>
`;

let updatedHtml = $.html();
updatedHtml = updatedHtml.replace(/<script>[\s\S]*?window\.mockObjectiveData[\s\S]*?<\/script>/, '');
updatedHtml = updatedHtml.replace('</body>', `${scriptTag}\n</body>`);

fs.writeFileSync(file, updatedHtml, 'utf8');
console.log('Successfully upgraded 4-1-sets-and-representation/index.html');

