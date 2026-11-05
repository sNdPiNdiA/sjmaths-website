const fs = require('fs');
const cheerio = require('cheerio');

const filePath = 'class-11-applied-mathematics/chapter-5-relations/5-3-representation-and-types-of-relations/index.html';
const html = fs.readFileSync(filePath, 'utf8');
const $ = cheerio.load(html);

// 1. LEARN TAB
const learnHtml = `
  <h2>5.3 Representation and Types of Relations</h2>
  <p class="lead-p">
    In Applied Mathematics, operations research, computer science, and economic theory, understanding the structural behavior of relationships is vital. Whether modeling parity across financial instruments, establishing equivalence classes in risk categories, or verifying transitivity in corporate organizational hierarchies, the taxonomy of relations provides the necessary algebraic tools.
  </p>

  <div class="formula-box">
    <h3>Core Structural Theorems & Classification</h3>
    <h4>1. Modes of Representation</h4>
    <ul>
      <li><strong>Roster (Tabular) Form:</strong> Explicitly listing all ordered pairs: \\(R = \\{(1, 2), (2, 4), (3, 6)\\}\\).</li>
      <li><strong>Set-Builder Form:</strong> Specifying the governing rule: \\(R = \\{(x, y) : y = 2x, \\, x, y \\in \\mathbb{N}\\}\\).</li>
      <li><strong>Arrow Diagram:</strong> Directed arrows drawn from elements in domain set \\(A\\) to target elements in co-domain \\(B\\).</li>
      <li><strong>Matrix Representation:</strong> A binary matrix \\(M_R\\) where entry \\(m_{ij} = 1\\) if \\((a_i, b_j) \\in R\\) and \\(0\\) otherwise.</li>
    </ul>

    <h4>2. Primary Types of Relations on a Set \\(A\\)</h4>
    <ul>
      <li><strong>Empty (Void) Relation:</strong> \\(R = \\emptyset \\subseteq A \\times A\\). No element of \\(A\\) is related to any element.</li>
      <li><strong>Universal Relation:</strong> \\(R = A \\times A\\). Every element of \\(A\\) is related to every element of \\(A\\). (Empty and Universal relations are called <em>trivial relations</em>).</li>
      <li><strong>Identity Relation (\\(I_A\\)):</strong> \\(I_A = \\{ (a, a) : a \\in A \\}\\). Every element of \\(A\\) is related to <em>itself and only itself</em>.</li>
      <li><strong>Reflexive Relation:</strong> A relation \\(R\\) is reflexive if:
        \\[ \\forall a \\in A, \\quad (a, a) \\in R \\]
        <em>Key Distinction:</em> Every identity relation is reflexive, but a reflexive relation may contain additional non-diagonal pairs \\((a, b)\\) with \\(a \\neq b\\).
      </li>
      <li><strong>Symmetric Relation:</strong> A relation \\(R\\) is symmetric if:
        \\[ (a, b) \\in R \\implies (b, a) \\in R, \\quad \\forall a, b \\in A \\]
        Equivalently, \\(R = R^{-1}\\).
      </li>
      <li><strong>Transitive Relation:</strong> A relation \\(R\\) is transitive if:
        \\[ (a, b) \\in R \\quad \\text{and} \\quad (b, c) \\in R \\implies (a, c) \\in R, \\quad \\forall a, b, c \\in A \\]
      </li>
      <li><strong>Equivalence Relation:</strong> A relation \\(R\\) on set \\(A\\) is an <strong>equivalence relation</strong> if and only if it is simultaneously:
        \\[ \\textbf{Reflexive}, \\quad \\textbf{Symmetric}, \\quad \\text{and} \\quad \\textbf{Transitive.} \\]
      </li>
      <li><strong>Equivalence Class:</strong> For an equivalence relation \\(R\\) on \\(A\\), the equivalence class containing \\(a\\) is:
        \\[ [a] = \\{ x \\in A : (x, a) \\in R \\} \\]
        Equivalence classes form a <em>partition</em> of \\(A\\): they are mutually disjoint and their union equals \\(A\\).
      </li>
    </ul>
  </div>

  <h3>Systematic Verification Workflow for Relation Types</h3>
  <table class="table-styled">
    <thead>
      <tr>
        <th>Property</th>
        <th>Mathematical Condition</th>
        <th>How to Prove</th>
        <th>How to Disprove (Counterexample)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Reflexive</strong></td>
        <td>\\((x, x) \\in R, \\, \\forall x \\in A\\)</td>
        <td>Show the algebraic condition holds when \\(y = x\\)</td>
        <td>Find a single \\(x_0 \\in A\\) such that \\((x_0, x_0) \\notin R\\)</td>
      </tr>
      <tr>
        <td><strong>Symmetric</strong></td>
        <td>\\((x, y) \\in R \\implies (y, x) \\in R\\)</td>
        <td>Assume \\((x, y) \\in R\\) and algebraically deduce \\((y, x) \\in R\\)</td>
        <td>Find a pair with \\((a, b) \\in R\\) but \\((b, a) \\notin R\\)</td>
      </tr>
      <tr>
        <td><strong>Transitive</strong></td>
        <td>\\((x, y) \\in R \\land (y, z) \\in R \\implies (x, z) \\in R\\)</td>
        <td>Assume \\((x, y) \\in R\\) and \\((y, z) \\in R\\) and deduce \\((x, z) \\in R\\)</td>
        <td>Find a chain where \\((a, b) \\in R\\) and \\((b, c) \\in R\\), but \\((a, c) \\notin R\\)</td>
      </tr>
    </tbody>
  </table>

  <div class="worked-example">
    <h4>Comprehensive Applied Example: Congruence Modulo \\(m\\)</h4>
    <p><strong>Problem:</strong> Let \\(\\mathbb{Z}\\) be the set of all integers. Define a relation \\(R\\) on \\(\\mathbb{Z}\\) by:
      \\[ R = \\{ (a, b) : a - b \\text{ is divisible by 5} \\} \\]
      Prove that \\(R\\) is an equivalence relation and determine all distinct equivalence classes.
    </p>
    <div class="solution">
      <p><strong>Proof:</strong></p>
      <ol>
        <li><strong>Reflexive:</strong> For any \\(a \\in \\mathbb{Z}\\), \\(a - a = 0 = 5 \\times 0\\), which is divisible by 5. Thus \\((a, a) \\in R\\) for all \\(a \\in \\mathbb{Z}\\). \\(R\\) is reflexive.</li>
        <li><strong>Symmetric:</strong> Let \\((a, b) \\in R\\). Then \\(a - b = 5k\\) for some \\(k \\in \\mathbb{Z}\\).
          Then:
          \\[ b - a = -(a - b) = -5k = 5(-k) \\]
          Since \\(-k \\in \\mathbb{Z}\\), \\(b - a\\) is divisible by 5. Thus \\((b, a) \\in R\\). \\(R\\) is symmetric.
        </li>
        <li><strong>Transitive:</strong> Let \\((a, b) \\in R\\) and \\((b, c) \\in R\\).
          Then \\(a - b = 5k\\) and \\(b - c = 5m\\) for integers \\(k, m\\).
          Adding these two equations:
          \\[ (a - b) + (b - c) = 5k + 5m \\implies a - c = 5(k + m) \\]
          Since \\(k + m \\in \\mathbb{Z}\\), \\(a - c\\) is divisible by 5. Thus \\((a, c) \\in R\\). \\(R\\) is transitive.
        </li>
      </ol>
      <p>Since \\(R\\) is reflexive, symmetric, and transitive, it is an <strong>equivalence relation</strong>.</p>
      <p><strong>Equivalence Classes:</strong> By the Division Algorithm, when any integer is divided by 5, the remainder is \\(0, 1, 2, 3,\\) or \\(4\\). There are exactly 5 distinct equivalence classes:
        \\[ [0] = \\{ \\dots, -10, -5, 0, 5, 10, \\dots \\} \\]
        \\[ [1] = \\{ \\dots, -9, -4, 1, 6, 11, \\dots \\} \\]
        \\[ [2] = \\{ \\dots, -8, -3, 2, 7, 12, \\dots \\} \\]
        \\[ [3] = \\{ \\dots, -7, -2, 3, 8, 13, \\dots \\} \\]
        \\[ [4] = \\{ \\dots, -6, -1, 4, 9, 14, \\dots \\} \\]
      </p>
    </div>
  </div>
`;

// 2. PROGRESS TAB
const progressHtml = `
  <h2>Progress Tracker & Self-Assessment Checklist</h2>
  <p>Track your conceptual mastery and diagnostic skills across Relation Types and Equivalence Proofs.</p>
  <div class="checklist-grid">
    <div class="checklist-card">
      <h4>Conceptual Milestones</h4>
      <ul>
        <li><label><input type="checkbox"> Distinguish between Identity and Reflexive relations.</label></li>
        <li><label><input type="checkbox"> Master algebraic proofs for Reflexivity, Symmetry, and Transitivity.</label></li>
        <li><label><input type="checkbox"> Formulate precise counterexamples to disprove non-equivalence relations.</label></li>
        <li><label><input type="checkbox"> Define Equivalence Classes and verify that they form a partition.</label></li>
      </ul>
    </div>
    <div class="checklist-card">
      <h4>Problem Solving Milestones</h4>
      <ul>
        <li><label><input type="checkbox"> Analyzed divisibility and congruence modulo relations.</label></li>
        <li><label><input type="checkbox"> Analyzed geometric relations (parallelism, perpendicularity, congruence).</label></li>
        <li><label><input type="checkbox"> Evaluated inequality relations (e.g. \\(a \\le b^2\\), \\(a < b\\)).</label></li>
        <li><label><input type="checkbox"> Scored 80%+ on the 10-Question Diagnostic Mock Exam.</label></li>
      </ul>
    </div>
  </div>
`;

// 3. WORKSHEET TAB
const worksheetHtml = `
  <h2>Practice Worksheet: Graded Exercises & Case Problems</h2>
  <p>Work through these graded problems from foundational mechanics to applied multi-stage scenarios.</p>

  <div class="problem-card">
    <h4>Problem 1 (Geometric Relations: Parallelism vs Perpendicularity)</h4>
    <p>Let \\(L\\) be the set of all lines in an \\(xy\\)-plane. Consider two relations on \\(L\\):</p>
    <ol type="a">
      <li>\\(R_1 = \\{ (l_1, l_2) : l_1 \\parallel l_2 \\}\\) (where a line is defined as parallel to itself)</li>
      <li>\\(R_2 = \\{ (l_1, l_2) : l_1 \\perp l_2 \\}\\)</li>
    </ol>
    <p>Test each relation for reflexivity, symmetry, and transitivity.</p>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        <p><strong>For \\(R_1\\) (Parallelism):</strong></p>
        <ul>
          <li><strong>Reflexive:</strong> Every line is parallel to itself: \\((l_1, l_1) \\in R_1\\). (Yes)</li>
          <li><strong>Symmetric:</strong> If \\(l_1 \\parallel l_2\\), then clearly \\(l_2 \\parallel l_1\\). (Yes)</li>
          <li><strong>Transitive:</strong> If \\(l_1 \\parallel l_2\\) and \\(l_2 \\parallel l_3\\), then \\(l_1 \\parallel l_3\\). (Yes)</li>
          <li><strong>Conclusion:</strong> \\(R_1\\) is an <strong>equivalence relation</strong>.</li>
        </ul>
        <p><strong>For \\(R_2\\) (Perpendicularity):</strong></p>
        <ul>
          <li><strong>Reflexive:</strong> A line cannot be perpendicular to itself. \\((l_1, l_1) \\notin R_2\\). (No)</li>
          <li><strong>Symmetric:</strong> If \\(l_1 \\perp l_2\\), then \\(l_2 \\perp l_1\\). (Yes)</li>
          <li><strong>Transitive:</strong> If \\(l_1 \\perp l_2\\) and \\(l_2 \\perp l_3\\), in the plane \\(l_1\\) is <em>parallel</em> to \\(l_3\\), not perpendicular! \\((l_1, l_3) \\notin R_2\\). (No)</li>
          <li><strong>Conclusion:</strong> \\(R_2\\) is symmetric, but neither reflexive nor transitive.</li>
        </ul>
      </div>
    </details>
  </div>

  <div class="problem-card">
    <h4>Problem 2 (Inequality Relation: The Real Number Trap)</h4>
    <p>Let \\(R\\) be the relation on \\(\\mathbb{R}\\) defined by \\(R = \\{ (a, b) : a \\le b^2 \\}\\). Determine whether \\(R\\) is reflexive, symmetric, or transitive.</p>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        <ul>
          <li><strong>Reflexivity:</strong> For \\(a = \\frac{1}{2}\\), \\(a^2 = \\frac{1}{4}\\). Since \\(\\frac{1}{2} \\not\\le \\frac{1}{4}\\), \\((\\frac{1}{2}, \\frac{1}{2}) \\notin R\\). Thus \\(R\\) is <strong>NOT reflexive</strong>.</li>
          <li><strong>Symmetry:</strong> Take \\(a = 1, b = 2\\). Then \\(1 \\le 2^2 = 4\\), so \\((1, 2) \\in R\\). But for \\((2, 1)\\), \\(2 \\not\\le 1^2 = 1\\), so \\((2, 1) \\notin R\\). Thus \\(R\\) is <strong>NOT symmetric</strong>.</li>
          <li><strong>Transitivity:</strong> Take \\(a = 2\\), \\(b = -2\\), \\(c = 1\\).
            <ul>
              <li>\\(2 \\le (-2)^2 = 4 \\implies (2, -2) \\in R\\).</li>
              <li>\\(-2 \\le 1^2 = 1 \\implies (-2, 1) \\in R\\).</li>
              <li>Check \\((2, 1)\\): \\(2 \\not\\le 1^2 = 1 \\implies (2, 1) \\notin R\\).</li>
            </ul>
            Thus \\(R\\) is <strong>NOT transitive</strong>.
          </li>
          <li><strong>Conclusion:</strong> \\(R\\) is neither reflexive, nor symmetric, nor transitive.</li>
        </ul>
      </div>
    </details>
  </div>

  <div class="problem-card">
    <h4>Problem 3 (Set Inclusion Relation)</h4>
    <p>Let \\(X\\) be a non-empty set and \\(P(X)\\) be its power set. Define a relation \\(R\\) on \\(P(X)\\) by \\((A, B) \\in R \\iff A \\subseteq B\\). Is \\(R\\) an equivalence relation?</p>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        <ul>
          <li><strong>Reflexive:</strong> For every subset \\(A \\in P(X)\\), \\(A \\subseteq A\\). Yes.</li>
          <li><strong>Symmetric:</strong> If \\(A \\subseteq B\\), does \\(B \\subseteq A\\)? No (unless \\(A = B\\)). For example, if \\(A = \\{1\\}\\) and \\(B = \\{1, 2\\}\\), \\(A \\subseteq B\\) but \\(B \\not\\subseteq A\\). Thus \\(R\\) is not symmetric.</li>
          <li><strong>Transitive:</strong> If \\(A \\subseteq B\\) and \\(B \\subseteq C\\), then \\(A \\subseteq C\\). Yes.</li>
        </ul>
        <p>Because \\(R\\) fails symmetry, it is <strong>not an equivalence relation</strong>. (It is a partial order relation).</p>
      </div>
    </details>
  </div>
`;

// 4. REVISION TAB
const revisionHtml = `
  <h2>Quick Revision & Formula Cheat Sheet</h2>
  <div class="revision-grid">
    <div class="revision-card">
      <h4>Taxonomy of Relations</h4>
      <ul>
        <li><strong>Reflexive:</strong> \\((a, a) \\in R, \\, \\forall a \\in A\\)</li>
        <li><strong>Symmetric:</strong> \\((a, b) \\in R \\implies (b, a) \\in R\\)</li>
        <li><strong>Transitive:</strong> \\((a, b) \\in R \\land (b, c) \\in R \\implies (a, c) \\in R\\)</li>
        <li><strong>Equivalence:</strong> Reflexive + Symmetric + Transitive</li>
      </ul>
    </div>
    <div class="revision-card">
      <h4>Number of Relations</h4>
      <ul>
        <li>Total relations on set with \\(n\\) elements: \\(2^{n^2}\\)</li>
        <li>Total reflexive relations: \\(2^{n(n-1)}\\)</li>
        <li>Total symmetric relations: \\(2^{n(n+1)/2}\\)</li>
        <li>Total reflexive and symmetric: \\(2^{n(n-1)/2}\\)</li>
      </ul>
    </div>
    <div class="revision-card">
      <h4>Equivalence Classes</h4>
      <ul>
        <li>\\([a] = \\{x \\in A : (x, a) \\in R\\}\\)</li>
        <li>\\([a] = [b] \\iff (a, b) \\in R\\)</li>
        <li>\\([a] \\cap [b] = \\emptyset\\) if \\((a, b) \\notin R\\)</li>
        <li>\\(\\bigcup_{a \\in A} [a] = A\\) (Partitions the universe)</li>
      </ul>
    </div>
  </div>
`;

// 5. MOCK EXAM TAB
const mockHtml = `
  <h2>10-Question Diagnostic Mock Exam</h2>
  <p class="lead-p">Test your mastery of Relation Types, Reflexivity, Symmetry, Transitivity, and Equivalence Classes under timed CBSE conditions.</p>
  <div id="mock-exam-container" class="mock-exam">
    <div id="quiz-questions"></div>
    <div class="mock-controls" style="margin-top:20px;">
      <button id="btn-submit-mock" class="btn btn-primary" onclick="gradeObjectiveSection()">Submit & Grade Exam</button>
      <button id="btn-reset-mock" class="btn btn-secondary" onclick="resetMockExam()" style="margin-left:10px;">Reset Exam</button>
    </div>
    <div id="mock-results" style="display:none; margin-top:25px;" class="result-box"></div>
  </div>
`;

// Apply Tab updates
$('#tab-learn').html(learnHtml);
$('#tab-progress').html(progressHtml);
$('#tab-worksheet').html(worksheetHtml);
$('#tab-revision').html(revisionHtml);
$('#tab-mock').html(mockHtml);

// 6. Mock Data Script
const mockQuestionsData = [
  {
    id: 1,
    question: "Let \\(A = \\{1, 2, 3\\}\\). Which of the following relations on \\(A\\) is an equivalence relation?",
    options: [
      "\\(\\{(1, 1), (2, 2), (3, 3), (1, 2), (2, 1)\\}\\)",
      "\\(\\{(1, 1), (2, 2), (1, 2), (2, 1)\\}\\)",
      "\\(\\{(1, 1), (2, 2), (3, 3), (1, 2)\\}\\)",
      "\\(\\{(1, 2), (2, 3), (1, 3)\\}\\)"
    ],
    correct: 0,
    explanation: "Option A contains (1,1), (2,2), (3,3) (reflexive); (1,2) and (2,1) (symmetric); and its compositions are closed (transitive). Option B lacks (3,3) so is not reflexive. Option C lacks (2,1) so is not symmetric."
  },
  {
    id: 2,
    question: "How many reflexive relations can be defined on a finite set containing 3 elements?",
    options: ["8", "64", "512", "4096"],
    correct: 1,
    explanation: "For a set with \\(n\\) elements, the number of reflexive relations is \\(2^{n(n-1)}\\). For \\(n=3\\), \\(2^{3(2)} = 2^6 = 64\\)."
  },
  {
    id: 3,
    question: "The relation 'is perpendicular to' (\\(\\perp\\)) on the set of straight lines in a plane is:",
    options: [
      "Reflexive and Symmetric",
      "Symmetric only",
      "Transitive only",
      "An Equivalence relation"
    ],
    correct: 1,
    explanation: "It is not reflexive because no line is perpendicular to itself. If \\(l_1 \\perp l_2\\), then \\(l_2 \\perp l_1\\) (symmetric). But if \\(l_1 \\perp l_2\\) and \\(l_2 \\perp l_3\\), then \\(l_1 \\parallel l_3\\), so it is not transitive."
  },
  {
    id: 4,
    question: "A relation \\(R\\) is defined on \\(\\mathbb{N}\\) by \\((a, b) \\in R \\iff a\\) divides \\(b\\). This relation is:",
    options: [
      "Reflexive and Symmetric",
      "Reflexive and Transitive",
      "Symmetric and Transitive",
      "An Equivalence relation"
    ],
    correct: 1,
    explanation: "Every number divides itself (reflexive). If \\(a\\) divides \\(b\\) and \\(b\\) divides \\(c\\), then \\(a\\) divides \\(c\\) (transitive). However, 2 divides 4 but 4 does not divide 2, so it is not symmetric."
  },
  {
    id: 5,
    question: "Let \\(R = \\{(1, 1), (2, 2), (3, 3), (1, 2), (2, 3), (1, 3)\\}\\) on set \\(A = \\{1, 2, 3\\}\\). Then \\(R\\) is:",
    options: [
      "Reflexive and Transitive, but not Symmetric",
      "Reflexive and Symmetric, but not Transitive",
      "Symmetric and Transitive, but not Reflexive",
      "An Equivalence relation"
    ],
    correct: 0,
    explanation: "\\(R\\) has (1,1), (2,2), (3,3) so it is reflexive. (1,2) and (2,3) give (1,3), which is in \\(R\\) (transitive). But (1,2) is in \\(R\\) while (2,1) is not, so it is not symmetric."
  },
  {
    id: 6,
    question: "What is the minimum number of ordered pairs that must be added to \\(R = \\{(1, 2), (2, 3)\\}\\) on \\(A = \\{1, 2, 3\\}\\) to make it an equivalence relation?",
    options: ["4", "5", "6", "7"],
    correct: 3,
    explanation: "To make it an equivalence relation on \\(\\{1, 2, 3\\}\\), we need: (1,1), (2,2), (3,3) for reflexivity (3 pairs); (2,1) and (3,2) for symmetry (2 pairs); and since (1,2) and (2,3) implies (1,3), we also need (1,3) and its symmetric pair (3,1) (2 pairs). Total added = 3 + 2 + 2 = 7 pairs (making all 9 pairs of \\(A \\times A\\))."
  },
  {
    id: 7,
    question: "If \\(R\\) is an equivalence relation on set \\(A\\), then \\(R^{-1}\\) is:",
    options: [
      "Not necessarily an equivalence relation",
      "Always an equivalence relation",
      "Never an equivalence relation",
      "Empty"
    ],
    correct: 1,
    explanation: "If \\(R\\) is an equivalence relation, \\(R = R^{-1}\\) by symmetry, hence \\(R^{-1}\\) is identically the same equivalence relation."
  },
  {
    id: 8,
    question: "Let \\(R\\) be an equivalence relation on \\(\\mathbb{Z}\\) defined by \\(a \\, R \\, b \\iff a - b\\) is a multiple of 4. What is the equivalence class \\([2]\\)?",
    options: [
      "\\(\\{\\dots, -6, -2, 2, 6, 10, \\dots\\}\\)",
      "\\(\\{\\dots, -8, -4, 0, 4, 8, \\dots\\}\\)",
      "\\(\\{\\dots, -7, -3, 1, 5, 9, \\dots\\}\\)",
      "\\(\\{2, 4, 6, 8\\}\\)"
    ],
    correct: 0,
    explanation: "\\([2] = \\{x \\in \\mathbb{Z} : x - 2 = 4k\\} = \\{4k + 2 : k \\in \\mathbb{Z}\\}\\), which generates \\(\\dots, -6, -2, 2, 6, 10, \\dots\\)."
  },
  {
    id: 9,
    question: "A relation \\(R\\) on \\(A\\) is called an Identity Relation if:",
    options: [
      "\\((a, a) \\in R\\) for all \\(a \\in A\\) and no other pairs exist",
      "\\((a, a) \\in R\\) for all \\(a \\in A\\)",
      "\\((a, b) \\in R \\implies (b, a) \\in R\\)",
      "\\(R = A \\times A\\)"
    ],
    correct: 0,
    explanation: "An identity relation requires every element to be related to itself and ONLY itself."
  },
  {
    id: 10,
    question: "Let \\(R\\) be a relation on \\(\\mathbb{R}\\) defined by \\((a, b) \\in R \\iff 1 + ab > 0\\). Then \\(R\\) is:",
    options: [
      "Reflexive and Symmetric, but not Transitive",
      "Reflexive and Transitive, but not Symmetric",
      "An Equivalence relation",
      "Neither Reflexive nor Symmetric"
    ],
    correct: 0,
    explanation: "Reflexive: \\(1 + a^2 > 0\\) for all \\(a \\in \\mathbb{R}\\) (True). Symmetric: \\(1 + ab > 0 \\iff 1 + ba > 0\\) (True). Transitive: Take \\(a = -1, b = -0.5, c = 2\\). Then \\(1 + ab = 1 + 0.5 = 1.5 > 0\\), and \\(1 + bc = 1 - 1 = 0 \\not> 0\\); or take \\(a = 1, b = 0.5, c = -1\\): \\(1 + (1)(0.5) > 0\\) and \\(1 + (0.5)(-1) = 0.5 > 0\\), but \\(1 + (1)(-1) = 0 \\not> 0\\). Hence not transitive."
  }
];

const mockScript = `
<script>
window.mockObjectiveData = ${JSON.stringify(mockQuestionsData, null, 2)};

function renderMockExam() {
  var container = document.getElementById('quiz-questions');
  if (!container) return;
  var data = window.mockObjectiveData;
  var html = '';
  for (var i = 0; i < data.length; i++) {
    var q = data[i];
    html += '<div class="quiz-item" style="margin-bottom:20px; padding:15px; border:1px solid #e2e8f0; border-radius:8px; background:#fff;">';
    html += '<p style="font-weight:600; margin-bottom:10px;">Q' + (i+1) + '. ' + q.question + '</p>';
    html += '<div class="options-group">';
    for (var j = 0; j < q.options.length; j++) {
      html += '<label style="display:block; margin:6px 0; cursor:pointer;">';
      html += '<input type="radio" name="question_' + q.id + '" value="' + j + '" style="margin-right:8px;">';
      html += q.options[j];
      html += '</label>';
    }
    html += '</div>';
    html += '<div id="feedback_' + q.id + '" class="question-feedback" style="display:none; margin-top:10px; padding:8px 12px; border-radius:6px;"></div>';
    html += '</div>';
  }
  container.innerHTML = html;
  if (window.MathJax && window.MathJax.typesetPromise) {
    window.MathJax.typesetPromise([container]);
  }
}

function gradeObjectiveSection() {
  var data = window.mockObjectiveData;
  var score = 0;
  var total = data.length;
  for (var i = 0; i < total; i++) {
    var q = data[i];
    var radios = document.getElementsByName('question_' + q.id);
    var selected = -1;
    for (var r = 0; r < radios.length; r++) {
      if (radios[r].checked) {
        selected = parseInt(radios[r].value, 10);
        break;
      }
    }
    var fb = document.getElementById('feedback_' + q.id);
    fb.style.display = 'block';
    if (selected === q.correct) {
      score++;
      fb.style.backgroundColor = '#ecfdf5';
      fb.style.color = '#065f46';
      fb.style.border = '1px solid #a7f3d0';
      fb.innerHTML = '<strong>Correct!</strong> ' + q.explanation;
    } else {
      fb.style.backgroundColor = '#fef2f2';
      fb.style.color = '#991b1b';
      fb.style.border = '1px solid #fecaca';
      fb.innerHTML = '<strong>Incorrect.</strong> Correct answer: ' + q.options[q.correct] + '. ' + q.explanation;
    }
  }
  var resultsBox = document.getElementById('mock-results');
  resultsBox.style.display = 'block';
  var pct = Math.round((score / total) * 100);
  resultsBox.innerHTML = '<h3>Diagnostic Exam Results</h3><p style="font-size:18px;">You scored <strong>' + score + ' / ' + total + '</strong> (' + pct + '%).</p>';
  if (pct >= 80) {
    resultsBox.innerHTML += '<p style="color:#059669; font-weight:600;">Outstanding! Exceptional mastery of equivalence relations and counterexamples.</p>';
  } else if (pct >= 50) {
    resultsBox.innerHTML += '<p style="color:#d97706; font-weight:600;">Good effort! Review the transitivity counterexample patterns and retry.</p>';
  } else {
    resultsBox.innerHTML += '<p style="color:#dc2626; font-weight:600;">Needs revision. Study the 3-step proof method for equivalence relations.</p>';
  }
  if (window.MathJax && window.MathJax.typesetPromise) {
    window.MathJax.typesetPromise([resultsBox]);
  }
}

function resetMockExam() {
  var data = window.mockObjectiveData;
  for (var i = 0; i < data.length; i++) {
    var radios = document.getElementsByName('question_' + data[i].id);
    for (var r = 0; r < radios.length; r++) {
      radios[r].checked = false;
    }
    var fb = document.getElementById('feedback_' + data[i].id);
    if (fb) {
      fb.style.display = 'none';
      fb.innerHTML = '';
    }
  }
  var resultsBox = document.getElementById('mock-results');
  if (resultsBox) resultsBox.style.display = 'none';
}

document.addEventListener('DOMContentLoaded', function() {
  renderMockExam();
});
</script>
`;

// Remove any existing mock script before appending
$('script').each((i, el) => {
  const text = $(el).html();
  if (text && text.includes('mockObjectiveData')) {
    $(el).remove();
  }
});

$('body').append(mockScript);

fs.writeFileSync(filePath, $.html(), 'utf8');
console.log('Successfully upgraded 5-3-representation-and-types-of-relations/index.html');

