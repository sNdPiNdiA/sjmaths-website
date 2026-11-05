const fs = require('fs');
const cheerio = require('cheerio');

const filePath = 'class-11-applied-mathematics/chapter-5-relations/5-2-relations/index.html';
const html = fs.readFileSync(filePath, 'utf8');
const $ = cheerio.load(html);

// 1. LEARN TAB
const learnHtml = `
  <h2>5.2 Relations: Foundations, Domain, Range, and Co-Domain</h2>
  <p class="lead-p">
    In Applied Mathematics, computational systems, and relational databases, a <strong>relation</strong> establishes structured linkages between distinct entities. From mapping bank customers to credit accounts to tracking logistics routes between suppliers and warehouses, relations translate intuitive real-world dependencies into rigorous set-theoretic algebra.
  </p>

  <div class="formula-box">
    <h3>Core Structural Theorems & Definitions</h3>
    <ul>
      <li><strong>Mathematical Definition of a Relation:</strong> A relation \\(R\\) from a non-empty set \\(A\\) to a non-empty set \\(B\\) is defined as any subset of the Cartesian product \\(A \\times B\\):
        \\[ R \\subseteq A \\times B \\]
        If \\((a, b) \\in R\\), we say that \\(a\\) is related to \\(b\\) under \\(R\\), denoted \\(a \\, R \\, b\\).
      </li>
      <li><strong>Total Number of Relations:</strong> If \\(n(A) = p\\) and \\(n(B) = q\\), the Cartesian product contains \\(p \\cdot q\\) ordered pairs. The total number of possible relations is the total number of subsets of \\(A \\times B\\):
        \\[ \\text{Total Relations} = 2^{p \\cdot q} \\]
        The number of non-empty relations is \\(2^{p \\cdot q} - 1\\).
      </li>
      <li><strong>Domain of a Relation:</strong> The set of all first coordinates of the ordered pairs belonging to \\(R\\):
        \\[ \\text{Dom}(R) = \\{ a \\in A : (a, b) \\in R \\text{ for some } b \\in B \\} \\subseteq A \\]
      </li>
      <li><strong>Range of a Relation:</strong> The set of all second coordinates of the ordered pairs belonging to \\(R\\):
        \\[ \\text{Range}(R) = \\{ b \\in B : (a, b) \\in R \\text{ for some } a \\in A \\} \\subseteq B \\]
      </li>
      <li><strong>Co-Domain:</strong> The entire target set \\(B\\) is called the co-domain of \\(R\\). Note that:
        \\[ \\text{Range}(R) \\subseteq \\text{Co-Domain}(R) \\]
      </li>
      <li><strong>Inverse Relation (\\(R^{-1}\\)):</strong> If \\(R\\) is a relation from \\(A\\) to \\(B\\), the inverse relation \\(R^{-1}\\) is a relation from \\(B\\) to \\(A\\) defined by:
        \\[ R^{-1} = \\{ (b, a) : (a, b) \\in R \\} \\]
        where \\(\\text{Dom}(R^{-1}) = \\text{Range}(R)\\) and \\(\\text{Range}(R^{-1}) = \\text{Dom}(R)\\).
      </li>
    </ul>
  </div>

  <h3>1. Visualizing the Distinction: Range vs Co-Domain</h3>
  <p>
    A central conceptual point in CBSE Applied Mathematics is that the <strong>Range</strong> is the set of actual outputs / matched elements, whereas the <strong>Co-Domain</strong> is the complete set of potentially eligible outputs.
  </p>
  <div class="worked-example">
    <h4>Example: Determining Domain, Range, and Co-domain</h4>
    <p><strong>Problem:</strong> Let \\(A = \\{1, 2, 3, 4, 5, 6\\}\\). Define a relation \\(R\\) from \\(A\\) to \\(A\\) by:
      \\[ R = \\{ (x, y) : y = x + 1 \\} \\]
    <ol>
      <li>Write \\(R\\) in roster form.</li>
      <li>Find the Domain, Range, and Co-domain of \\(R\\).</li>
      <li>Write the inverse relation \\(R^{-1}\\).</li>
    </ol>
    </p>
    <div class="solution">
      <p><strong>Solution:</strong></p>
      <ol>
        <li>Evaluating for each \\(x \\in A\\) such that \\(y = x + 1 \\in A\\):
          <ul>
            <li>For \\(x = 1\\), \\(y = 2 \\in A\\) \\(\\implies (1, 2) \\in R\\)</li>
            <li>For \\(x = 2\\), \\(y = 3 \\in A\\) \\(\\implies (2, 3) \\in R\\)</li>
            <li>For \\(x = 3\\), \\(y = 4 \\in A\\) \\(\\implies (3, 4) \\in R\\)</li>
            <li>For \\(x = 4\\), \\(y = 5 \\in A\\) \\(\\implies (4, 5) \\in R\\)</li>
            <li>For \\(x = 5\\), \\(y = 6 \\in A\\) \\(\\implies (5, 6) \\in R\\)</li>
            <li>For \\(x = 6\\), \\(y = 7 \\notin A\\) (excluded)</li>
          </ul>
          Therefore: \\(R = \\{ (1, 2), (2, 3), (3, 4), (4, 5), (5, 6) \\}\\).
        </li>
        <li>
          \\[ \\text{Domain}(R) = \\{1, 2, 3, 4, 5\\} \\]
          \\[ \\text{Range}(R) = \\{2, 3, 4, 5, 6\\} \\]
          \\[ \\text{Co-domain}(R) = A = \\{1, 2, 3, 4, 5, 6\\} \\]
        </li>
        <li>
          \\[ R^{-1} = \\{ (2, 1), (3, 2), (4, 3), (5, 4), (6, 5) \\} \\]
        </li>
      </ol>
    </div>
  </div>

  <h3>2. Applied Business Context: Relational Modeling</h3>
  <p>
    Consider an e-commerce platform with a set of Customers \\(C = \\{c_1, c_2, c_3\\}\\) and Product Categories \\(P = \\{\\text{Electronics}, \\text{Books}, \\text{Apparel}\\}\\).
    The "Purchased-From" relation \\(R \subseteq C \times P\\) records transactions:
  </p>
  <ul>
    <li>If customer \\(c_1\\) purchased Electronics and Books, then \\((c_1, \\text{Electronics}) \\in R\\) and \\((c_1, \\text{Books}) \\in R\\).</li>
    <li>The <strong>Domain</strong> represents all active customers who have made at least one purchase.</li>
    <li>The <strong>Range</strong> represents all product categories that have generated at least one sale.</li>
    <li>The <strong>Co-Domain</strong> is the complete product catalog, which may contain unsought or unsold categories.</li>
  </ul>
`;

// 2. PROGRESS TAB
const progressHtml = `
  <h2>Progress Tracker & Self-Assessment Checklist</h2>
  <p>Track your conceptual mastery and computational proficiency across Relations, Domain, Range, and Inverse Relations.</p>
  <div class="checklist-grid">
    <div class="checklist-card">
      <h4>Conceptual Milestones</h4>
      <ul>
        <li><label><input type="checkbox"> Define a relation formally as a subset of the Cartesian product \\(A \\times B\\).</label></li>
        <li><label><input type="checkbox"> Compute total possible relations \\(2^{p \\cdot q}\\) and non-empty relations.</label></li>
        <li><label><input type="checkbox"> Correctly extract the Domain as first coordinates and Range as second coordinates.</label></li>
        <li><label><input type="checkbox"> Distinguish sharply between Range and Co-domain.</label></li>
        <li><label><input type="checkbox"> Invert relations and verify \\(\\text{Dom}(R^{-1}) = \\text{Range}(R)\\).</label></li>
      </ul>
    </div>
    <div class="checklist-card">
      <h4>Problem Solving Milestones</h4>
      <ul>
        <li><label><input type="checkbox"> Filtered ordered pairs under algebraic conditions (e.g. \\(3x - y = 0\\), \\(x^2 + y^2 \\le 25\\)).</label></li>
        <li><label><input type="checkbox"> Evaluated divisibility relations on sets of integers.</label></li>
        <li><label><input type="checkbox"> Mapped real-world enterprise databases to relational set formulations.</label></li>
        <li><label><input type="checkbox"> Completed the 10-Question Diagnostic Mock with an 80%+ score.</label></li>
      </ul>
    </div>
  </div>
`;

// 3. WORKSHEET TAB
const worksheetHtml = `
  <h2>Practice Worksheet: Graded Exercises & Case Problems</h2>
  <p>Work through these graded problems from foundational mechanics to applied multi-stage scenarios.</p>

  <div class="problem-card">
    <h4>Problem 1 (Linear Constraint on Finite Integer Set)</h4>
    <p>Let \\(A = \\{1, 2, 3, \\dots, 14\\}\\). Define a relation \\(R\\) from \\(A\\) to \\(A\\) by:
      \\[ R = \\{ (x, y) : 3x - y = 0, \\text{ where } x, y \\in A \\} \\]
    Write down its roster form, domain, co-domain, and range.
    </p>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        <p>The condition \\(3x - y = 0\\) means \\(y = 3x\\). Since both \\(x, y \\in A = \\{1, 2, \\dots, 14\\}\\):</p>
        <ul>
          <li>For \\(x = 1\\), \\(y = 3 \\in A \\implies (1, 3) \\in R\\)</li>
          <li>For \\(x = 2\\), \\(y = 6 \\in A \\implies (2, 6) \\in R\\)</li>
          <li>For \\(x = 3\\), \\(y = 9 \\in A \\implies (3, 9) \\in R\\)</li>
          <li>For \\(x = 4\\), \\(y = 12 \\in A \\implies (4, 12) \\in R\\)</li>
          <li>For \\(x = 5\\), \\(y = 15 \\notin A\\) (stops here)</li>
        </ul>
        <p><strong>Roster form:</strong> \\(R = \\{ (1, 3), (2, 6), (3, 9), (4, 12) \\}\\)</p>
        <p><strong>Domain:</strong> \\(\\{1, 2, 3, 4\\}\\)</p>
        <p><strong>Range:</strong> \\(\\{3, 6, 9, 12\\}\\)</p>
        <p><strong>Co-domain:</strong> \\(A = \\{1, 2, 3, \\dots, 14\\}\\)</p>
      </div>
    </details>
  </div>

  <div class="problem-card">
    <h4>Problem 2 (Counting Total Relations)</h4>
    <p>Let \\(A = \\{x, y, z\\}\\) and \\(B = \\{1, 2\\}\\). Find:</p>
    <ol type="a">
      <li>The total number of relations from \\(A\\) to \\(B\\).</li>
      <li>The number of non-empty relations from \\(A\\) to \\(B\\).</li>
      <li>The total number of relations on set \\(A\\) (i.e. from \\(A\\) to \\(A\\)).</li>
    </ol>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        <ul>
          <li><strong>(a)</strong> \\(n(A) = 3\\), \\(n(B) = 2\\). Total relations \\(= 2^{3 \\times 2} = 2^6 = 64\\).</li>
          <li><strong>(b)</strong> Non-empty relations exclude the empty relation \\(\\emptyset\\): \\(64 - 1 = 63\\).</li>
          <li><strong>(c)</strong> Relations on \\(A\\) are subsets of \\(A \\times A\\): \\(n(A \\times A) = 3 \\times 3 = 9\\).
            Total relations \\(= 2^9 = 512\\).
          </li>
        </ul>
      </div>
    </details>
  </div>

  <div class="problem-card">
    <h4>Problem 3 (Divisibility Relation)</h4>
    <p>Let \\(A = \\{2, 3, 4, 5, 6\\}\\). Let \\(R\\) be the relation on \\(A\\) defined by:
      \\[ R = \\{ (a, b) : a \\in A, b \\in A, \\, a \\text{ divides } b \\} \\]
    <ol type="a">
      <li>Write \\(R\\) in roster form.</li>
      <li>Find the Domain and Range of \\(R\\).</li>
    </ol>
    </p>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        <p>For each \\(a \\in A\\), find all \\(b \\in A\\) such that \\(b\\) is a multiple of \\(a\\):</p>
        <ul>
          <li>\\(a = 2\\): divides 2, 4, 6 \\(\\implies (2, 2), (2, 4), (2, 6)\\)</li>
          <li>\\(a = 3\\): divides 3, 6 \\(\\implies (3, 3), (3, 6)\\)</li>
          <li>\\(a = 4\\): divides 4 \\(\\implies (4, 4)\\)</li>
          <li>\\(a = 5\\): divides 5 \\(\\implies (5, 5)\\)</li>
          <li>\\(a = 6\\): divides 6 \\(\\implies (6, 6)\\)</li>
        </ul>
        <p><strong>Roster form:</strong>
          \\[ R = \\{ (2, 2), (2, 4), (2, 6), (3, 3), (3, 6), (4, 4), (5, 5), (6, 6) \\} \\]
        </p>
        <p><strong>Domain:</strong> \\(\\{2, 3, 4, 5, 6\\} = A\\)</p>
        <p><strong>Range:</strong> \\(\\{2, 3, 4, 5, 6\\} = A\\)</p>
      </div>
    </details>
  </div>

  <div class="problem-card">
    <h4>Problem 4 (Inverse of an Integer Relation)</h4>
    <p>Let \\(R = \\{ (x, y) : x, y \\in \\mathbb{Z}, \\, x^2 + y^2 = 25 \\}\\). Find the Domain, Range, and Inverse of \\(R\\).</p>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        <p>The integer pairs \\((x, y)\\) whose sum of squares is 25 are:</p>
        \\[ R = \\{ (0, \\pm 5), (\\pm 5, 0), (\\pm 3, \\pm 4), (\\pm 4, \\pm 3) \\} \\]
        <p>Specifically, the 12 pairs are:
          \\((0, 5), (0, -5), (5, 0), (-5, 0), (3, 4), (3, -4), (-3, 4), (-3, -4), (4, 3), (4, -3), (-4, 3), (-4, -3)\\).
        </p>
        <p><strong>Domain:</strong> \\(\\{-5, -4, -3, 0, 3, 4, 5\\}\\)</p>
        <p><strong>Range:</strong> \\(\\{-5, -4, -3, 0, 3, 4, 5\\}\\)</p>
        <p>Since the relation is completely symmetric in \\(x\\) and \\(y\\), \\(R^{-1} = R\\).</p>
      </div>
    </details>
  </div>
`;

// 4. REVISION TAB
const revisionHtml = `
  <h2>Quick Revision & Formula Cheat Sheet</h2>
  <div class="revision-grid">
    <div class="revision-card">
      <h4>Relation Basics</h4>
      <ul>
        <li>Relation from \\(A\\) to \\(B\\): \\(R \\subseteq A \\times B\\)</li>
        <li>Number of relations: \\(2^{n(A) \\cdot n(B)}\\)</li>
        <li>Empty relation: \\(\\emptyset \\subseteq A \\times B\\)</li>
        <li>Universal relation: \\(A \\times B\\)</li>
      </ul>
    </div>
    <div class="revision-card">
      <h4>Domain & Range</h4>
      <ul>
        <li>\\(\\text{Dom}(R) = \\{a : (a, b) \\in R\\} \\subseteq A\\)</li>
        <li>\\(\\text{Range}(R) = \\{b : (a, b) \\in R\\} \\subseteq B\\)</li>
        <li>\\(\\text{Co-domain} = B\\)</li>
        <li>\\(\\text{Range} \\subseteq \\text{Co-domain}\\)</li>
      </ul>
    </div>
    <div class="revision-card">
      <h4>Inverse Relation</h4>
      <ul>
        <li>\\(R^{-1} = \\{(b, a) : (a, b) \\in R\\}\\)</li>
        <li>\\(\\text{Dom}(R^{-1}) = \\text{Range}(R)\\)</li>
        <li>\\(\\text{Range}(R^{-1}) = \\text{Dom}(R)\\)</li>
        <li>\\((R^{-1})^{-1} = R\\)</li>
      </ul>
    </div>
  </div>
`;

// 5. MOCK EXAM TAB
const mockHtml = `
  <h2>10-Question Diagnostic Mock Exam</h2>
  <p class="lead-p">Test your mastery of Relations, Domain, Range, and Inverse Relations under timed CBSE examination conditions.</p>
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
    question: "If set \\(A\\) has 2 elements and set \\(B\\) has 4 elements, what is the total number of non-empty relations from \\(A\\) to \\(B\\)?",
    options: ["16", "64", "255", "256"],
    correct: 2,
    explanation: "Total relations = \\(2^{2 \\times 4} = 2^8 = 256\\). Non-empty relations = \\(256 - 1 = 255\\)."
  },
  {
    id: 2,
    question: "Let \\(A = \\{1, 2, 3\\}\\). A relation is defined by \\(R = \\{(1, 2), (2, 3), (1, 3)\\}\\). What is the Domain of \\(R\\)?",
    options: ["\\(\\{1, 2\\}\\)", "\\(\\{2, 3\\}\\)", "\\(\\{1, 2, 3\\}\\)", "\\(\\{1, 3\\}\\)"],
    correct: 0,
    explanation: "The domain is the set of all first coordinates: \\(\\{1, 2\\}\\)."
  },
  {
    id: 3,
    question: "For the relation in Question 2, what is the Range of \\(R\\)?",
    options: ["\\(\\{1, 2\\}\\)", "\\(\\{2, 3\\}\\)", "\\(\\{1, 2, 3\\}\\)", "\\(\\{3\\}\\)"],
    correct: 1,
    explanation: "The range is the set of all second coordinates: \\(\\{2, 3\\}\\)."
  },
  {
    id: 4,
    question: "Let \\(R = \\{ (x, y) : x, y \\in \\mathbb{N}, \\, 2x + y = 10 \\}\\). What is the Range of \\(R\\)?",
    options: ["\\(\\{2, 4, 6, 8\\}\\)", "\\(\\{1, 2, 3, 4\\}\\)", "\\(\\{2, 4, 6, 8, 10\\}\\)", "\\(\\{1, 3, 5, 7\\}\\)"],
    correct: 0,
    explanation: "\\(y = 10 - 2x\\). Since \\(x, y \\in \\mathbb{N}\\): for \\(x=1 \\implies y=8\\); \\(x=2 \\implies y=6\\); \\(x=3 \\implies y=4\\); \\(x=4 \\implies y=2\\). For \\(x \\ge 5\\), \\(y \\le 0 \\notin \\mathbb{N}\\). Hence Range = \\(\\{2, 4, 6, 8\\}\\)."
  },
  {
    id: 5,
    question: "If \\(R\\) is a relation from \\(A\\) to \\(B\\), which of the following statements is ALWAYS true?",
    options: [
      "\\(\\text{Range}(R) = B\\)",
      "\\(\\text{Domain}(R) = A\\)",
      "\\(\\text{Range}(R) \\subseteq B\\)",
      "\\(\\text{Range}(R) = \\text{Domain}(R)\\)"
    ],
    correct: 2,
    explanation: "By definition, the Range is a subset of the target set \\(B\\) (the co-domain): \\(\\text{Range}(R) \\subseteq B\\)."
  },
  {
    id: 6,
    question: "If \\(R = \\{(1, 4), (2, 5), (3, 6)\\}\\), what is \\(R^{-1}\\)?",
    options: [
      "\\(\\{(4, 1), (5, 2), (6, 3)\\}\\)",
      "\\(\\{(1, 4), (2, 5), (3, 6)\\}\\)",
      "\\(\\{(4, 5), (5, 6), (6, 1)\\}\\)",
      "\\(\\{(1, 1), (2, 2), (3, 3)\\}\\)"
    ],
    correct: 0,
    explanation: "The inverse relation swaps the coordinates: \\(R^{-1} = \\{(4, 1), (5, 2), (6, 3)\\}\\)."
  },
  {
    id: 7,
    question: "Let \\(A = \\{2, 3, 4, 5\\}\\) and \\(B = \\{3, 6, 7, 10\\}\\). Let \\(R\\) be 'is a factor of' from \\(A\\) to \\(B\\). How many elements are in \\(R\\)?",
    options: ["4", "5", "6", "7"],
    correct: 1,
    explanation: "Pairs \\((a, b)\\) where \\(a\\) is a factor of \\(b\\): (2, 6), (2, 10), (3, 3), (3, 6), (5, 10). There are 5 pairs."
  },
  {
    id: 8,
    question: "What is the relationship between the domain of \\(R^{-1}\\) and the range of \\(R\\)?",
    options: [
      "\\(\\text{Dom}(R^{-1}) = \\text{Range}(R)\\)",
      "\\(\\text{Dom}(R^{-1}) = \\text{Dom}(R)\\)",
      "\\(\\text{Dom}(R^{-1}) \\cap \\text{Range}(R) = \\emptyset\\)",
      "\\(\\text{Dom}(R^{-1}) = \\text{Co-domain}(R)\\)"
    ],
    correct: 0,
    explanation: "The first coordinates of \\(R^{-1}\\) are the second coordinates of \\(R\\), so \\(\\text{Dom}(R^{-1}) = \\text{Range}(R)\\)."
  },
  {
    id: 9,
    question: "If \\(n(A) = 3\\), how many relations can be defined on \\(A\\)?",
    options: ["9", "27", "81", "512"],
    correct: 3,
    explanation: "Relations on \\(A\\) are subsets of \\(A \\times A\\). Since \\(n(A \\times A) = 3 \\times 3 = 9\\), there are \\(2^9 = 512\\) relations."
  },
  {
    id: 10,
    question: "Let \\(R = \\{(x, y) : x, y \\in \\mathbb{W}, \\, x + 2y = 8\\}\\). What is the domain of \\(R\\)?",
    options: ["\\(\\{0, 2, 4, 6, 8\\}\\)", "\\(\\{0, 1, 2, 3, 4\\}\\)", "\\(\\{2, 4, 6, 8\\}\\)", "\\(\\{0, 1, 2, 4, 8\\}\\)"],
    correct: 0,
    explanation: "\\(x = 8 - 2y\\). Since \\(y \\in \\mathbb{W}\\): for \\(y=0 \\implies x=8\\); \\(y=1 \\implies x=6\\); \\(y=2 \\implies x=4\\); \\(y=3 \\implies x=2\\); \\(y=4 \\implies x=0\\). Thus \\(\\text{Dom}(R) = \\{0, 2, 4, 6, 8\\}\\)."
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
    resultsBox.innerHTML += '<p style="color:#059669; font-weight:600;">Outstanding! Perfect mastery of relation domains, ranges, and counting.</p>';
  } else if (pct >= 50) {
    resultsBox.innerHTML += '<p style="color:#d97706; font-weight:600;">Good effort! Review the definitions of domain vs co-domain and retry.</p>';
  } else {
    resultsBox.innerHTML += '<p style="color:#dc2626; font-weight:600;">Needs revision. Study the worked examples on relations and try again.</p>';
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
console.log('Successfully upgraded 5-2-relations/index.html');

