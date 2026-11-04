const cheerio = require('cheerio');
const fs = require('fs');
const path = require('path');

const file = path.join(process.cwd(), 'class-11-applied-mathematics/chapter-4-sets/4-2-types-of-sets/index.html');
const html = fs.readFileSync(file, 'utf8');
const $ = cheerio.load(html);

// 1. LEARN TAB
const learnContent = `
    <div class="card-premium">
        <h3 class="card-title"><i class="fas fa-book-reader"></i> Comprehensive Concepts &amp; Principles: Types of Sets</h3>
        <p class="theory-para">In set theory and CBSE Class 11 Applied Mathematics, sets are systematically classified according to the number and nature of elements they contain. Mastering these classifications is essential for analyzing categorical data, constructing database domain constraints, and evaluating logical boundary conditions.</p>
        
        <div class="theory-highlight">
            <strong>Core Taxonomy of Sets:</strong>
            <ul style="margin: 6px 0 0 1.2rem; padding: 0; line-height: 1.8;">
                <li><strong>1. Empty Set (Null Set / Void Set):</strong> A set that contains no elements at all, denoted by the Greek symbol $\\emptyset$ or empty braces $\\{\\}$.
                <br>• Cardinality: $n(\\emptyset) = 0$.
                <br>• <em>Critical Notation Alert:</em> The set $\\{\\emptyset\\}$ or $\\{0\\}$ is <strong>NOT</strong> an empty set; it is a singleton set containing one element!</li>
                <li><strong>2. Singleton Set (Unit Set):</strong> A set containing exactly one element ($n(A) = 1$).
                <br>• Example: $S = \\{x : x \\in \\mathbb{N}, x^2 = 4\\} = \\{2\\}$.</li>
                <li><strong>3. Finite Set:</strong> A set that has a definite, countable number of elements (its cardinality $n(A) \\in \\mathbb{W}$).
                <br>• Example: The set of days in a week ($n = 7$).</li>
                <li><strong>4. Infinite Set:</strong> A set whose elements cannot be counted to a terminal end.
                <br>• Examples: The set of all natural numbers $\\mathbb{N}$, the set of all real numbers between 0 and 1, the set of points on a line segment.</li>
                <li><strong>5. Equal Sets ($A = B$):</strong> Two sets $A$ and $B$ are equal if and only if they possess <em>identical elements</em>:
                <br>$$A = B \\iff (x \\in A \\iff x \\in B)$$</li>
                <li><strong>6. Equivalent Sets ($A \\approx B$):</strong> Two finite sets are equivalent if they have the <em>same cardinal number</em> of elements:
                <br>$$A \\approx B \\iff n(A) = n(B)$$
                <br>• <em>Golden Rule:</em> All equal sets are equivalent, but equivalent sets are <strong>not necessarily equal</strong>!</li>
            </ul>
        </div>
    </div>

    <div class="card-premium">
        <h3 class="card-title"><i class="fas fa-balance-scale"></i> Equal vs. Equivalent Sets Comparison</h3>
        <div style="overflow-x:auto;">
            <table class="audit-table" style="width:100%; border-collapse:collapse; margin-top:0.5rem;">
                <thead>
                    <tr style="background:var(--neutral-100); text-align:left;">
                        <th style="padding:10px; border:1px solid var(--neutral-300);">Feature</th>
                        <th style="padding:10px; border:1px solid var(--neutral-300);">Equal Sets ($A = B$)</th>
                        <th style="padding:10px; border:1px solid var(--neutral-300);">Equivalent Sets ($A \\approx B$)</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td style="padding:10px; border:1px solid var(--neutral-300); font-weight:600;">Criterion</td>
                        <td style="padding:10px; border:1px solid var(--neutral-300);">Identical elements</td>
                        <td style="padding:10px; border:1px solid var(--neutral-300);">Identical count of elements ($n(A) = n(B)$)</td>
                    </tr>
                    <tr>
                        <td style="padding:10px; border:1px solid var(--neutral-300); font-weight:600;">Example</td>
                        <td style="padding:10px; border:1px solid var(--neutral-300); font-family:var(--font-mono);">$\\{1, 2, 3\\} = \\{3, 1, 2\\}$</td>
                        <td style="padding:10px; border:1px solid var(--neutral-300); font-family:var(--font-mono);">$\\{1, 2, 3\\} \\approx \\{a, b, c\\}$</td>
                    </tr>
                    <tr>
                        <td style="padding:10px; border:1px solid var(--neutral-300); font-weight:600;">Bijection</td>
                        <td style="padding:10px; border:1px solid var(--neutral-300);">Trivially identical mapping</td>
                        <td style="padding:10px; border:1px solid var(--neutral-300);">Supports a one-to-one correspondence</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>

    <div class="card-premium">
        <h3 class="card-title"><i class="fas fa-pen-nib"></i> Worked Benchmark Examples</h3>
        
        <div class="example-box">
            <strong style="color:var(--neutral-900);">Example 1 (Identifying Empty Sets):</strong>
            <p class="theory-para" style="margin:6px 0;">State whether each of the following sets is Empty, Singleton, or neither:
            <br>(a) $A = \\{x : x \\in \\mathbb{N}, 2 < x < 3\\}$
            <br>(b) $B = \\{x : x \\in \\mathbb{Z}, x^2 = 0\\}$
            <br>(c) $C = \\{x : x \\text{ is an odd integer divisible by 2}\\}$
            <br>(d) $D = \\{\\emptyset\\}$</p>
            <details class="solution-details">
                <summary>Show Step-by-Step Solution</summary>
                <div class="solution-explanation">
                    <p>• <strong>(a) $A$: Empty Set ($\\emptyset$):</strong> There is no natural number strictly between 2 and 3.<br>
                    • <strong>(b) $B$: Singleton Set ($\\{0\\}$):</strong> Only $x = 0$ satisfies $x^2 = 0$, and 0 is an integer. Cardinality is 1.<br>
                    • <strong>(c) $C$: Empty Set ($\\emptyset$):</strong> By definition, odd numbers leave a remainder of 1 when divided by 2; none are divisible by 2.<br>
                    • <strong>(d) $D$: Singleton Set:</strong> $D$ contains exactly one element, which happens to be the symbol $\\emptyset$. Its cardinality is $n(D) = 1$.</p>
                </div>
            </details>
        </div>

        <div class="example-box">
            <strong style="color:var(--neutral-900);">Example 2 (Equal vs. Equivalent Verification):</strong>
            <p class="theory-para" style="margin:6px 0;">Given:
            <br>$A = \\{x : x \\text{ is a letter in the word 'WOLF'}\\}$
            <br>$B = \\{x : x \\text{ is a letter in the word 'FLOW'}\\}$
            <br>$C = \\{1, 2, 3, 4\\}$
            <br>State whether pairs $(A, B)$ and $(A, C)$ are Equal or Equivalent.</p>
            <details class="solution-details">
                <summary>Show Step-by-Step Solution</summary>
                <div class="solution-explanation">
                    <p>• $A = \\{W, O, L, F\\}$, $n(A) = 4$.<br>
                    • $B = \\{F, L, O, W\\}$, $n(B) = 4$.<br>
                    • $C = \\{1, 2, 3, 4\\}$, $n(C) = 4$.<br>
                    • <strong>Pair $(A, B)$: Equal ($A = B$) and Equivalent:</strong> Both sets have the exact same 4 letters.<br>
                    • <strong>Pair $(A, C)$: Equivalent ($A \\approx C$) but NOT Equal:</strong> Both sets share the same cardinal count of 4 elements, but their elements are completely different (letters vs numbers).</p>
                </div>
            </details>
        </div>
    </div>
`;
$('#tab-learn').html(learnContent);

// 2. PROGRESS TAB
const progressContent = `
    <div class="card-premium">
        <h3 class="card-title"><i class="fas fa-tasks"></i> CHECK YOUR PROGRESS 4.2</h3>
        <p class="theory-para">Graded textbook exercises on Types of Sets, Finiteness, and Equality from CBSE Class 11 Applied Mathematics.</p>
    </div>

    <div class="q-card">
        <div class="q-header-meta">
            <span class="q-number-pill">Problem 1</span>
            <span class="q-marks-pill">Null Set Identification</span>
        </div>
        <p class="q-prompt">State whether the set $S = \\{x : x \\in \\mathbb{R}, x^2 + 1 = 0\\}$ is an empty set or not, giving justification.</p>
        <details class="solution-details">
            <summary>Show Step-by-Step Solution</summary>
            <div class="solution-explanation">
                <p>• $x^2 + 1 = 0 \\implies x^2 = -1 \\implies x = \\pm \\sqrt{-1} = \\pm i$ (imaginary numbers).<br>
                • Since there is no real number whose square is negative, no $x \\in \\mathbb{R}$ satisfies the equation.<br>
                • Therefore, $S$ is an <strong>Empty Set ($\u2205$)</strong>.</p>
            </div>
        </details>
    </div>

    <div class="q-card">
        <div class="q-header-meta">
            <span class="q-number-pill">Problem 2</span>
            <span class="q-marks-pill">Finite vs Infinite</span>
        </div>
        <p class="q-prompt">Classify the following sets as Finite or Infinite:
        <br>(a) The set of lines parallel to the $X$-axis.
        <br>(b) The set of concentric circles passing through the origin.
        <br>(c) The set of prime numbers less than 99.</p>
        <details class="solution-details">
            <summary>Show Step-by-Step Solution</summary>
            <div class="solution-explanation">
                <p>• (a) <strong>Infinite:</strong> Infinitely many parallel lines can be drawn.<br>
                • (b) <strong>Infinite:</strong> Circles of continuously varying radii can pass through the origin.<br>
                • (c) <strong>Finite:</strong> There are exactly 25 prime numbers less than 99 ($n = 25$).</p>
            </div>
        </details>
    </div>

    <div class="q-card">
        <div class="q-header-meta">
            <span class="q-number-pill">Problem 3</span>
            <span class="q-marks-pill">Equality of Solution Sets</span>
        </div>
        <p class="q-prompt">Are the sets $A = \\{2, 3\\}$ and $B = \\{x : x^2 + 5x + 6 = 0\\}$ equal? Justify.</p>
        <details class="solution-details">
            <summary>Show Step-by-Step Solution</summary>
            <div class="solution-explanation">
                <p>• Solve $x^2 + 5x + 6 = 0 \\implies (x + 2)(x + 3) = 0 \\implies x = -2, -3$.<br>
                • Thus $B = \\{-2, -3\\}$.<br>
                • While $A = \\{2, 3\\}$.<br>
                • Since $+2 \\in A$ but $+2 \\notin B$, the sets are <strong>NOT Equal</strong> ($A \\neq B$). They are, however, Equivalent ($n(A) = n(B) = 2$).</p>
            </div>
        </details>
    </div>

    <div class="q-card">
        <div class="q-header-meta">
            <span class="q-number-pill">Problem 4</span>
            <span class="q-marks-pill">Singleton Trap</span>
        </div>
        <p class="q-prompt">Is the set $A = \\{x : x \\in \\mathbb{W}, x < 1\\}$ an empty set? State its element and cardinality.</p>
        <details class="solution-details">
            <summary>Show Step-by-Step Solution</summary>
            <div class="solution-explanation">
                <p>• Whole numbers begin at 0: $\\mathbb{W} = \\{0, 1, 2, \\dots\\}$.<br>
                • The only whole number strictly less than 1 is 0.<br>
                • Thus $A = \\{0\\}$, which is a <strong>Singleton Set</strong> with cardinality $n(A) = 1$. It is NOT empty.</p>
            </div>
        </details>
    </div>

    <div class="q-card">
        <div class="q-header-meta">
            <span class="q-number-pill">Problem 5</span>
            <span class="q-marks-pill">Equivalence Criterion</span>
        </div>
        <p class="q-prompt">If $A = \\{x : x \\text{ is a vowel in 'EDUCATION'}\\}$ and $B = \\{2, 4, 6, 8, 10\\}$, determine whether $A$ and $B$ are equivalent.</p>
        <details class="solution-details">
            <summary>Show Step-by-Step Solution</summary>
            <div class="solution-explanation">
                <p>• Vowels in 'EDUCATION': E, U, A, I, O $\\implies A = \\{A, E, I, O, U\\} \\implies n(A) = 5$.<br>
                • $B = \\{2, 4, 6, 8, 10\\} \\implies n(B) = 5$.<br>
                • Since $n(A) = n(B) = 5$, the sets $A$ and $B$ are <strong>Equivalent</strong> ($A \\approx B$).</p>
            </div>
        </details>
    </div>
`;
$('#tab-progress').html(progressContent);

// 3. WORKSHEET TAB
const worksheetContent = `
    <div class="card-premium">
        <h3 class="card-title"><i class="fas fa-file-alt"></i> Comprehensive Practice Worksheet: Types of Sets</h3>
        <p class="theory-para">Graded problems matching CBSE Class 11 Applied Mathematics examination blueprint.</p>
    </div>

    <div class="card-premium">
        <h4 style="color:var(--primary-700); margin-top:0;">SECTION A: 1-Mark Objective &amp; Conceptual Questions</h4>
        
        <div class="q-card">
            <p class="q-prompt"><strong>Q1:</strong> What is the cardinality of the empty set $\\emptyset$?</p>
            <details class="solution-details">
                <summary>Show Answer &amp; Scheme</summary>
                <div class="solution-explanation">
                    <p>$$n(\\emptyset) = \\mathbf{0} \\quad [1 \\text{ Mark}]$$</p>
                </div>
            </details>
        </div>

        <div class="q-card">
            <p class="q-prompt"><strong>Q2:</strong> State whether the set of points on a circle of radius 5 cm is finite or infinite.</p>
            <details class="solution-details">
                <summary>Show Answer &amp; Scheme</summary>
                <div class="solution-explanation">
                    <p><strong>Answer [1 Mark]:</strong> <strong>Infinite</strong>, because a continuous geometrical curve consists of uncountably infinite points.</p>
                </div>
            </details>
        </div>
    </div>

    <div class="card-premium">
        <h4 style="color:var(--primary-700); margin-top:0;">SECTION B: 2-Mark Short Answer Problems</h4>
        
        <div class="q-card">
            <p class="q-prompt"><strong>Q3:</strong> Differentiate between Equal sets and Equivalent sets with suitable examples.</p>
            <details class="solution-details">
                <summary>Show Answer &amp; Scheme</summary>
                <div class="solution-explanation">
                    <p><strong>Differences [2 Marks]:</strong><br>
                    • <strong>Equal Sets:</strong> Must possess exactly the same elements (e.g. $\\{1, 2\\} = \\{2, 1\\}$).<br>
                    • <strong>Equivalent Sets:</strong> Must possess the same number of elements ($n(A) = n(B)$), but the elements themselves can be completely distinct (e.g. $\\{1, 2\\} \\approx \\{x, y\\}$).</p>
                </div>
            </details>
        </div>

        <div class="q-card">
            <p class="q-prompt"><strong>Q4:</strong> Show that the set $A = \\{x : x \\in \\mathbb{Z}, x^2 - 4 = 0\\}$ and $B = \\{-2, 2\\}$ are equal sets.</p>
            <details class="solution-details">
                <summary>Show Answer &amp; Scheme</summary>
                <div class="solution-explanation">
                    <p>• $x^2 - 4 = 0 \\implies x^2 = 4 \\implies x = 2, -2$ [1 Mark].<br>
                    • Since both $2$ and $-2$ are integers, $A = \\{-2, 2\\}$.<br>
                    • Since $A$ and $B$ have identical elements, $\\mathbf{A = B}$ [1 Mark].</p>
                </div>
            </details>
        </div>
    </div>

    <div class="card-premium">
        <h4 style="color:var(--primary-700); margin-top:0;">SECTION C: 4-Mark Comprehensive Scenario Drill</h4>
        
        <div class="q-card">
            <p class="q-prompt"><strong>Q5:</strong> A telecommunications network categorizes subscriber account groups:
            <br>• Group Alpha: $\\{x : x \\text{ is a prime factor of } 30\\}$
            <br>• Group Beta: $\\{x : x \\in \\mathbb{N}, x^3 - 10x^2 + 31x - 30 = 0\\}$
            <br>• Group Gamma: $\\{x : x \\in \\mathbb{W}, x < 3\\}$
            <br>(i) Find the elements of Group Alpha in Roster form.
            <br>(ii) Find the elements of Group Beta in Roster form.
            <br>(iii) Are Group Alpha and Group Beta equal sets?
            <br>(iv) Are Group Alpha and Group Gamma equal or equivalent sets?</p>
            <details class="solution-details">
                <summary>Show Step-by-Step Solution &amp; Marking Scheme</summary>
                <div class="solution-explanation">
                    <p><strong>Part (i) Group Alpha [1 Mark]:</strong><br>
                    • Prime factors of 30 ($30 = 2 \\times 3 \\times 5$): $\\mathbf{\\{2, 3, 5\\}}$.</p>
                    <p><strong>Part (ii) Group Beta [1 Mark]:</strong><br>
                    • Test roots of $x^3 - 10x^2 + 31x - 30 = 0$:
                    $(x-2)(x-3)(x-5) = 0 \\implies x = 2, 3, 5$: $\\mathbf{\\{2, 3, 5\\}}$.</p>
                    <p><strong>Part (iii) Alpha vs Beta [1 Mark]:</strong><br>
                    • Since both have identical elements $\\{2, 3, 5\\}$, <strong>Group Alpha = Group Beta (Equal Sets)</strong>.</p>
                    <p><strong>Part (iv) Alpha vs Gamma [1 Mark]:</strong><br>
                    • Group Gamma: Whole numbers $< 3$: $\\{0, 1, 2\\}$.<br>
                    • $n(\\text{Alpha}) = 3$ and $n(\\text{Gamma}) = 3$.<br>
                    • They are <strong>Equivalent sets ($n=3$), but NOT equal</strong> because $0, 1 \\notin \\text{Alpha}$.</p>
                </div>
            </details>
        </div>
    </div>
`;
$('#tab-worksheet').html(worksheetContent);

// 4. REVISION TAB
const revisionContent = `
    <div class="card-premium">
        <h3 class="card-title"><i class="fas fa-bolt"></i> High-Yield Quick Revision: Types of Sets</h3>
        <p class="theory-para">Summary of definitions, cardinality rules, and common boundary conditions for Chapter 4.2.</p>
    </div>

    <div class="card-premium">
        <h4 style="color:var(--primary-700); margin-top:0;"><i class="fas fa-table"></i> Set Classification Cheat Sheet</h4>
        <div style="overflow-x:auto;">
            <table class="audit-table" style="width:100%; border-collapse:collapse; margin-top:0.5rem;">
                <thead>
                    <tr style="background:var(--neutral-100); text-align:left;">
                        <th style="padding:10px; border:1px solid var(--neutral-300);">Set Type</th>
                        <th style="padding:10px; border:1px solid var(--neutral-300);">Defining Property</th>
                        <th style="padding:10px; border:1px solid var(--neutral-300);">Cardinality $n(A)$</th>
                        <th style="padding:10px; border:1px solid var(--neutral-300);">Standard Example</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td style="padding:10px; border:1px solid var(--neutral-300); font-weight:600;">Empty Set ($\\emptyset$)</td>
                        <td style="padding:10px; border:1px solid var(--neutral-300);">No elements exist</td>
                        <td style="padding:10px; border:1px solid var(--neutral-300); font-family:var(--font-mono);">$0$</td>
                        <td style="padding:10px; border:1px solid var(--neutral-300); font-family:var(--font-mono);">$\\{x \\in \\mathbb{R} : x^2 + 4 = 0\\}$</td>
                    </tr>
                    <tr>
                        <td style="padding:10px; border:1px solid var(--neutral-300); font-weight:600;">Singleton Set</td>
                        <td style="padding:10px; border:1px solid var(--neutral-300);">Exactly one element</td>
                        <td style="padding:10px; border:1px solid var(--neutral-300); font-family:var(--font-mono);">$1$</td>
                        <td style="padding:10px; border:1px solid var(--neutral-300); font-family:var(--font-mono);">$\\{x \\in \\mathbb{N} : x^2 = 9\\} = \\{3\\}$</td>
                    </tr>
                    <tr>
                        <td style="padding:10px; border:1px solid var(--neutral-300); font-weight:600;">Finite Set</td>
                        <td style="padding:10px; border:1px solid var(--neutral-300);">Countable terminal elements</td>
                        <td style="padding:10px; border:1px solid var(--neutral-300); font-family:var(--font-mono);">$k \\in \\mathbb{W}$</td>
                        <td style="padding:10px; border:1px solid var(--neutral-300); font-family:var(--font-mono);">$\\{x \\in \\mathbb{N} : x < 100\\}$</td>
                    </tr>
                    <tr>
                        <td style="padding:10px; border:1px solid var(--neutral-300); font-weight:600;">Infinite Set</td>
                        <td style="padding:10px; border:1px solid var(--neutral-300);">Uncountable / non-terminating</td>
                        <td style="padding:10px; border:1px solid var(--neutral-300); font-family:var(--font-mono);">$\\infty$</td>
                        <td style="padding:10px; border:1px solid var(--neutral-300); font-family:var(--font-mono);">$\\mathbb{N}, \\mathbb{Z}, \\mathbb{R}$</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>

    <div class="card-premium">
        <h4 style="color:var(--primary-700); margin-top:0;"><i class="fas fa-exclamation-triangle"></i> Examination Alert: Empty vs. Singleton</h4>
        <p style="margin:0; font-size:0.95rem; line-height:1.8;">
            Do not confuse $\\emptyset$ with $\\{\\emptyset\\}$ or $\\{0\\}$:
            <br>• $\\emptyset$ has <strong>0 elements</strong> (Empty Set).
            <br>• $\\{\\emptyset\\}$ has <strong>1 element</strong> (the symbol $\\emptyset$ itself).
            <br>• $\\{0\\}$ has <strong>1 element</strong> (the number 0).
        </p>
    </div>
`;
$('#tab-revision').html(revisionContent);

// 5. MOCK EXAM TAB
const mockContent = `
    <div class="card-premium">
        <h3 class="card-title"><i class="fas fa-graduation-cap"></i> 10-Question Diagnostic Board Mock Examination: Types of Sets</h3>
        <p class="theory-para">Standard timed test: 4 Objective MCQs / Assertion-Reason with instant automatic grading, plus 6 multi-mark subjective problems with CBSE marking rubrics.</p>
    </div>

    <div class="card-premium">
        <h4 style="color:var(--primary-700); margin-top:0;">PART 1: Objective Section (4 Marks)</h4>
        
        <div class="q-card">
            <p class="q-prompt"><strong>Q1:</strong> Which of the following is an empty set?</p>
            <div style="display:flex; flex-direction:column; gap:8px; margin:10px 0;">
                <label><input type="radio" name="mock_q1" value="A"> (A) $\\{0\\}$</label>
                <label><input type="radio" name="mock_q1" value="B"> (B) $\\{\\emptyset\\}$</label>
                <label><input type="radio" name="mock_q1" value="C"> (C) $\\{x : x \\in \\mathbb{N}, 2x + 1 = 4\\}$</label>
                <label><input type="radio" name="mock_q1" value="D"> (D) $\\{x : x \\in \\mathbb{Z}, x^2 = 4\\}$</label>
            </div>
            <div id="mock-sol-1" style="display:none; background:var(--neutral-100); padding:10px; border-radius:6px; margin-top:8px;">
                <strong>Solution:</strong> (C) $2x + 1 = 4 \\implies 2x = 3 \\implies x = 1.5$. Since $1.5 \\notin \\mathbb{N}$, this set is empty.
            </div>
        </div>

        <div class="q-card">
            <p class="q-prompt"><strong>Q2:</strong> Two sets $A$ and $B$ are said to be equivalent if:</p>
            <div style="display:flex; flex-direction:column; gap:8px; margin:10px 0;">
                <label><input type="radio" name="mock_q2" value="A"> (A) $A = B$</label>
                <label><input type="radio" name="mock_q2" value="B"> (B) $n(A) = n(B)$</label>
                <label><input type="radio" name="mock_q2" value="C"> (C) $A \\subseteq B$</label>
                <label><input type="radio" name="mock_q2" value="D"> (D) $A \\cap B = \\emptyset$</label>
            </div>
            <div id="mock-sol-2" style="display:none; background:var(--neutral-100); padding:10px; border-radius:6px; margin-top:8px;">
                <strong>Solution:</strong> (B) Equivalent sets are defined by having the exact same cardinal number of elements: $n(A) = n(B)$.
            </div>
        </div>

        <div class="q-card">
            <p class="q-prompt"><strong>Q3:</strong> The set of all circles passing through three non-collinear points is a:</p>
            <div style="display:flex; flex-direction:column; gap:8px; margin:10px 0;">
                <label><input type="radio" name="mock_q3" value="A"> (A) Infinite set</label>
                <label><input type="radio" name="mock_q3" value="B"> (B) Empty set</label>
                <label><input type="radio" name="mock_q3" value="C"> (C) Singleton set</label>
                <label><input type="radio" name="mock_q3" value="D"> (D) Universal set</label>
            </div>
            <div id="mock-sol-3" style="display:none; background:var(--neutral-100); padding:10px; border-radius:6px; margin-top:8px;">
                <strong>Solution:</strong> (C) By basic Euclidean geometry, there is one and only one unique circle passing through three non-collinear points (Singleton set).
            </div>
        </div>

        <div class="q-card">
            <p class="q-prompt"><strong>Q4 (Assertion-Reason):</strong><br>
            <strong>Assertion (A):</strong> All equal sets are equivalent, but all equivalent sets are not necessarily equal.<br>
            <strong>Reason (R):</strong> Equal sets require identical elements, which inherently guarantees identical cardinality, whereas equivalent sets only require equal cardinality.</p>
            <div style="display:flex; flex-direction:column; gap:8px; margin:10px 0;">
                <label><input type="radio" name="mock_q4" value="A"> (A) Both (A) and (R) are true and (R) is the correct explanation of (A)</label>
                <label><input type="radio" name="mock_q4" value="B"> (B) Both (A) and (R) are true but (R) is NOT the correct explanation of (A)</label>
                <label><input type="radio" name="mock_q4" value="C"> (C) (A) is true but (R) is false</label>
                <label><input type="radio" name="mock_q4" value="D"> (D) (A) is false but (R) is true</label>
            </div>
            <div id="mock-sol-4" style="display:none; background:var(--neutral-100); padding:10px; border-radius:6px; margin-top:8px;">
                <strong>Solution:</strong> (A) Both Assertion and Reason are true and Reason provides the precise set theory relationship.
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
            <p class="q-prompt">Examine whether the set $A = \\{x : x \\in \\mathbb{N}, x^2 = 9\\}$ and $B = \\{x : x \\in \\mathbb{Z}, x^2 = 9\\}$ are equal.</p>
            <details class="solution-details">
                <summary>Show Step-by-Step Solution &amp; Marking Scheme</summary>
                <div class="solution-explanation">
                    <p>• In $\\mathbb{N}$: $x^2 = 9 \\implies x = 3 \\implies A = \\{3\\}$ [1 Mark].<br>
                    • In $\\mathbb{Z}$: $x^2 = 9 \\implies x = 3, -3 \\implies B = \\{-3, 3\\}$ [1 Mark].<br>
                    • Since $-3 \\in B$ but $-3 \\notin A$, $\\mathbf{A \\neq B}$ (Not equal).</p>
                </div>
            </details>
        </div>

        <div class="q-card">
            <div class="q-header-meta">
                <span class="q-number-pill">Q6</span>
                <span class="q-marks-pill">2 Marks</span>
            </div>
            <p class="q-prompt">State whether the set of points on the line segment $AB$ of length 5 cm is finite or infinite. Justify.</p>
            <details class="solution-details">
                <summary>Show Step-by-Step Solution &amp; Marking Scheme</summary>
                <div class="solution-explanation">
                    <p><strong>Answer [2 Marks]:</strong><br>
                    It is an <strong>Infinite Set</strong>. A geometric line segment consists of a continuum of real numbers representing lengths, between any two of which there are infinitely many more real points.</p>
                </div>
            </details>
        </div>

        <div class="q-card">
            <div class="q-header-meta">
                <span class="q-number-pill">Q7</span>
                <span class="q-marks-pill">3 Marks</span>
            </div>
            <p class="q-prompt">Classify each of the following sets as empty, singleton, finite, or infinite:
            <br>(a) $\\{x : x \\in \\mathbb{N}, x \\text{ is even and prime}\\}$
            <br>(b) $\\{x : x \\in \\mathbb{Z}, 2x = 3\\}$
            <br>(c) $\\{x : x \\in \\mathbb{R}, 0 < x < 1\\}$.</p>
            <details class="solution-details">
                <summary>Show Step-by-Step Solution &amp; Marking Scheme</summary>
                <div class="solution-explanation">
                    <p>• (a) $\\{2\\} \\implies$ <strong>Singleton set</strong> ($n = 1$) [1 Mark].<br>
                    • (b) $x = 1.5 \\notin \\mathbb{Z} \\implies$ <strong>Empty set ($\\emptyset$)</strong> [1 Mark].<br>
                    • (c) Real numbers strictly between 0 and 1 form a continuum $\\implies$ <strong>Infinite set</strong> [1 Mark].</p>
                </div>
            </details>
        </div>

        <div class="q-card">
            <div class="q-header-meta">
                <span class="q-number-pill">Q8</span>
                <span class="q-marks-pill">3 Marks</span>
            </div>
            <p class="q-prompt">Explain why the set $\\{\\emptyset\\}$ has cardinality 1, while $\\emptyset$ has cardinality 0.</p>
            <details class="solution-details">
                <summary>Show Step-by-Step Solution &amp; Marking Scheme</summary>
                <div class="solution-explanation">
                    <p>• $\\emptyset$ is the empty set, defined as having no members: $n(\\emptyset) = 0$ [1.5 Marks].<br>
                    • $\\{\\emptyset\\}$ is a set that contains one element (namely, the empty set as a member entity). Its cardinality is $n(\\{\\emptyset\\}) = 1$ [1.5 Marks].<br>
                    • <em>Analogy:</em> An empty box ($\emptyset$) vs. a box containing an empty box ($\{\emptyset\}$).</p>
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
                    Case Context: Software Permissions Access Groups
                </p>
                <p style="margin:6px 0 0; font-size:0.95rem; color:var(--neutral-700);">
                    A cloud security architect configures user role groups:
                    <br>• Group $P_1 = \\{x : x \\text{ is a root admin with ID } x \\in \\mathbb{N}, x^2 - 16 = 0\\}$
                    <br>• Group $P_2 = \\{x : x \\text{ is a guest account with ID } x \\in \\mathbb{N}, x < 1\\}$
                </p>
            </div>
            <p class="q-prompt" style="font-weight:600;">
                <strong>Q9 (2 Marks):</strong> Identify the type of set represented by Group $P_1$ and state its elements.<br>
                <strong>Q10 (2 Marks):</strong> Identify the type of set represented by Group $P_2$ and justify why it contains no active accounts.
            </p>
            <details class="solution-details">
                <summary>Show Step-by-Step Solution &amp; Marking Scheme</summary>
                <div class="solution-explanation">
                    <p><strong>Solution to Q9 [2 Marks]:</strong><br>
                    • $x^2 - 16 = 0 \\implies x = \\pm 4$. Since $x \\in \\mathbb{N}$, only $x = 4$ is allowed.<br>
                    • $P_1 = \\{4\\}$, which is a <strong>Singleton Set</strong> with cardinality 1.</p>
                    <p><strong>Solution to Q10 [2 Marks]:</strong><br>
                    • Natural numbers begin at 1 ($1, 2, 3, \\dots$). There is no natural number $< 1$.<br>
                    • Therefore, $P_2 = \\emptyset$, which is an <strong>Empty Set</strong> containing 0 accounts.</p>
                </div>
            </details>
        </div>
    </div>
`;
$('#tab-mock').html(mockContent);

// 6. UPDATE MOCK SCRIPT
const mockData = [
    {"ans": "C", "sol": "2x + 1 = 4 => x = 1.5, which is not a natural number, so the set is empty."},
    {"ans": "B", "sol": "Equivalent sets have identical cardinality: n(A) = n(B)."},
    {"ans": "C", "sol": "Exactly one unique circle passes through 3 non-collinear points (Singleton set)."},
    {"ans": "A", "sol": "Both Assertion and Reason are true and Reason provides the set theory justification."}
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
console.log('Successfully upgraded 4-2-types-of-sets/index.html');
