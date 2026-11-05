const fs = require('fs');
const cheerio = require('cheerio');

const filePath = 'class-11-applied-mathematics/chapter-5-relations/5-1-cartesian-product-of-sets/index.html';
const html = fs.readFileSync(filePath, 'utf8');
const $ = cheerio.load(html);

// 1. LEARN TAB
const learnHtml = `
  <h2>5.1 Cartesian Product of Sets</h2>
  <p class="lead-p">
    In Applied Mathematics, relational databases, inventory modeling, and algorithmic design, the <strong>Cartesian Product</strong> is the fundamental operation that constructs multi-dimensional structures from one-dimensional collections. It provides the rigorous formal framework for product variants (SKUs), coordinates in plane geometry, and pairing dependencies.
  </p>

  <div class="formula-box">
    <h3>Core Structural Theorems & Definitions</h3>
    <ul>
      <li><strong>Ordered Pair:</strong> An ordered pair \\((a, b)\\) consists of two elements \\(a\\) and \\(b\\) in a specified order, where \\(a\\) is the first coordinate and \\(b\\) is the second coordinate.
        \\[ (a_1, b_1) = (a_2, b_2) \\iff a_1 = a_2 \\quad \\text{and} \\quad b_1 = b_2 \\]
      </li>
      <li><strong>Cartesian Product (\\(A \\times B\\)):</strong> Given two non-empty sets \\(A\\) and \\(B\\), the Cartesian product \\(A \\times B\\) is the set of all ordered pairs \\((a, b)\\) such that \\(a \\in A\\) and \\(b \\in B\\):
        \\[ A \\times B = \\{ (a, b) : a \\in A \\text{ and } b \\in B \\} \\]
      </li>
      <li><strong>Cardinality Theorem:</strong> If \\(n(A) = p\\) and \\(n(B) = q\\), then:
        \\[ n(A \\times B) = n(A) \\times n(B) = p \\cdot q \\]
      </li>
      <li><strong>Non-Commutative Property:</strong>
        \\[ A \\times B \\neq B \\times A \\quad (\\text{unless } A = B \\text{ or } A = \\emptyset \\text{ or } B = \\emptyset) \\]
      </li>
      <li><strong>Empty Set Identity:</strong> If either \\(A = \\emptyset\\) or \\(B = \\emptyset\\), then:
        \\[ A \\times B = \\emptyset \\]
      </li>
      <li><strong>Distributive Identities:</strong>
        <ol>
          <li>\\(A \\times (B \\cup C) = (A \\times B) \\cup (A \\times C)\\)</li>
          <li>\\(A \\times (B \\cap C) = (A \\times B) \\cap (A \\times C)\\)</li>
          <li>\\(A \\times (B - C) = (A \\times B) - (A \\times C)\\)</li>
          <li>\\((A \\times B) \\cap (S \\times T) = (A \\cap S) \\times (B \\cap T)\\)</li>
        </ol>
      </li>
    </ul>
  </div>

  <h3>1. Equality of Ordered Pairs: Algebraic Foundations</h3>
  <p>
    Two ordered pairs are equal if and only if their respective first components are equal and their respective second components are equal. In CBSE examinations, this is frequently tested as linear or quadratic systems:
  </p>
  <div class="worked-example">
    <h4>Example: Solving for Unknown Parameters</h4>
    <p><strong>Problem:</strong> If \\(\\left( \\frac{x}{3} + 1, \\, y - \\frac{2}{3} \\right) = \\left( \\frac{5}{3}, \\, \\frac{1}{3} \\right)\\), find the values of \\(x\\) and \\(y\\).</p>
    <div class="solution">
      <p><strong>Solution:</strong> Equating corresponding components:</p>
      \\[ \\frac{x}{3} + 1 = \\frac{5}{3} \\implies \\frac{x}{3} = \\frac{5}{3} - 1 = \\frac{2}{3} \\implies x = 2 \\]
      \\[ y - \\frac{2}{3} = \\frac{1}{3} \\implies y = \\frac{1}{3} + \\frac{2}{3} = \\frac{3}{3} = 1 \\]
      <p>Therefore, \\(x = 2\\) and \\(y = 1\\).</p>
    </div>
  </div>

  <h3>2. Geometric and Real-World Interpretations</h3>
  <p>
    The Cartesian product extends into higher dimensions:
  </p>
  <ul>
    <li><strong>\\(\\mathbb{R} \\times \\mathbb{R} = \\mathbb{R}^2\\):</strong> Represents the set of all coordinates \\((x, y)\\) on the two-dimensional Cartesian plane.</li>
    <li><strong>\\(\\mathbb{R} \\times \\mathbb{R} \\times \\mathbb{R} = \\mathbb{R}^3\\):</strong> Represents 3-dimensional space where each point is an ordered triplet \\((x, y, z)\\).</li>
    <li><strong>E-Commerce SKU Enumeration:</strong> If a retail brand offers T-shirts in 3 sizes \\(S = \\{\\text{S, M, L}\\}\\) and 4 colors \\(C = \\{\\text{Red, Blue, Black, White}\\}\\), the total catalog of distinct product SKUs is \\(S \\times C\\), giving \\(3 \\times 4 = 12\\) items.</li>
  </ul>

  <div class="worked-example">
    <h4>Example: Intersection of Cartesian Products</h4>
    <p><strong>Problem:</strong> If \\(A = \\{1, 2\\}\\), \\(B = \\{2, 3\\}\\), and \\(C = \\{0, 5\\}\\), verify that \\(A \\times (B \\cap C) = (A \\times B) \\cap (A \\times C)\\).</p>
    <div class="solution">
      <p><strong>Solution:</strong></p>
      <ul>
        <li>First evaluate \\(B \\cap C\\): Since \\(B = \\{2, 3\\}\\) and \\(C = \\{0, 5\\}\\), \\(B \\cap C = \\emptyset\\).</li>
        <li>LHS: \\(A \\times (B \\cap C) = A \\times \\emptyset = \\emptyset\\).</li>
        <li>RHS:
          \\[ A \\times B = \\{(1, 2), (1, 3), (2, 2), (2, 3)\\} \\]
          \\[ A \\times C = \\{(1, 0), (1, 5), (2, 0), (2, 5)\\} \\]
          Notice that \\(A \\times B\\) and \\(A \\times C\\) share no common ordered pairs. Therefore, \\((A \\times B) \\cap (A \\times C) = \\emptyset\\).
        </li>
        <li>Since LHS \\(= \\emptyset =\\) RHS, the distributive identity is verified.</li>
      </ul>
    </div>
  </div>
`;

// 2. PROGRESS TAB
const progressHtml = `
  <h2>Progress Tracker & Self-Assessment Checklist</h2>
  <p>Track your conceptual mastery and computational proficiency across Cartesian Products.</p>
  <div class="checklist-grid">
    <div class="checklist-card">
      <h4>Conceptual Milestones</h4>
      <ul>
        <li><label><input type="checkbox"> Understand the rigorous definition of an ordered pair and component equality.</label></li>
        <li><label><input type="checkbox"> Master the cardinality rule \\(n(A \\times B) = n(A) \\cdot n(B)\\).</label></li>
        <li><label><input type="checkbox"> Understand why \\(A \\times B \\neq B \\times A\\) in general.</label></li>
        <li><label><input type="checkbox"> Master the distributive properties over union, intersection, and difference.</label></li>
        <li><label><input type="checkbox"> Understand Cartesian products in real coordinates (\\(\\mathbb{R}^2, \\mathbb{R}^3\\)).</label></li>
      </ul>
    </div>
    <div class="checklist-card">
      <h4>Problem Solving Milestones</h4>
      <ul>
        <li><label><input type="checkbox"> Solved linear and non-linear systems from equality of ordered pairs.</label></li>
        <li><label><input type="checkbox"> Reconstructed constituent sets from partial Cartesian product subsets.</label></li>
        <li><label><input type="checkbox"> Computed ordered triplets (e.g. \\(A \\times A \\times A\\)).</label></li>
        <li><label><input type="checkbox"> Achieved 80%+ on the 10-Question Diagnostic Mock Exam.</label></li>
      </ul>
    </div>
  </div>
`;

// 3. WORKSHEET TAB
const worksheetHtml = `
  <h2>Practice Worksheet: Graded Exercises & Case Problems</h2>
  <p>Work through these graded problems from foundational mechanics to applied multi-stage scenarios.</p>

  <div class="problem-card">
    <h4>Problem 1 (Ordered Pair Algebraic Systems)</h4>
    <p>Find the values of \\(a\\) and \\(b\\) if \\((2a + b, \\, a - 2b) = (7, \\, 1)\\).</p>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        <p>Equating corresponding components yields a simultaneous linear system:
          \\[ 2a + b = 7 \\quad \\text{--- (1)} \\]
          \\[ a - 2b = 1 \\implies a = 2b + 1 \\quad \\text{--- (2)} \\]
        Substitute \\(a = 2b + 1\\) into (1):
          \\[ 2(2b + 1) + b = 7 \\implies 4b + 2 + b = 7 \\implies 5b = 5 \\implies b = 1 \\]
        Then:
          \\[ a = 2(1) + 1 = 3 \\]
        <strong>Answer:</strong> \\(a = 3, b = 1\\).
        </p>
      </div>
    </details>
  </div>

  <div class="problem-card">
    <h4>Problem 2 (Reconstructing Sets from Product Subsets)</h4>
    <p>The Cartesian product \\(A \\times A\\) has 9 elements, among which are found the pairs \\((-1, 0)\\) and \\((0, 1)\\). Find the set \\(A\\) and the remaining elements of \\(A \\times A\\).</p>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        <p>Since \\(n(A \\times A) = [n(A)]^2 = 9\\), we have \\(n(A) = 3\\).</p>
        <p>Since \\((-1, 0) \\in A \\times A\\) and \\((0, 1) \\in A \\times A\\), the first and second coordinates must all be elements of \\(A\\):
          \\[ -1 \\in A, \\quad 0 \\in A, \\quad 1 \\in A \\]
        Since \\(n(A) = 3\\), set \\(A\\) must be exactly:
          \\[ A = \\{-1, 0, 1\\} \\]
        The 9 elements of \\(A \\times A\\) are:
          \\[ \\{(-1,-1), (-1,0), (-1,1), (0,-1), (0,0), (0,1), (1,-1), (1,0), (1,1)\\} \\]
        The remaining 7 elements (excluding \\((-1, 0)\\) and \\((0, 1)\\)) are:
          \\[ \\{(-1,-1), (-1,1), (0,-1), (0,0), (1,-1), (1,0), (1,1)\\} \\]
        </p>
      </div>
    </details>
  </div>

  <div class="problem-card">
    <h4>Problem 3 (Common Elements of Cartesian Products)</h4>
    <p>If set \\(A\\) and set \\(B\\) have \\(n\\) elements in common, prove that \\(A \\times B\\) and \\(B \\times A\\) have \\(n^2\\) elements in common.</p>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        <p>We need to find the cardinality of \\((A \\times B) \\cap (B \\times A)\\).</p>
        <p>Using the distributive property of intersections across products:
          \\[ (A \\times B) \\cap (B \\times A) = (A \\cap B) \\times (B \\cap A) \\]
        Since intersection is commutative, \\(B \\cap A = A \\cap B\\). Thus:
          \\[ (A \\times B) \\cap (B \\times A) = (A \\cap B) \\times (A \\cap B) \\]
        Given that \\(n(A \\cap B) = n\\):
          \\[ n((A \\times B) \\cap (B \\times A)) = n(A \\cap B) \\times n(A \\cap B) = n \\times n = n^2 \\]
        This completes the proof.
        </p>
      </div>
    </details>
  </div>

  <div class="problem-card">
    <h4>Problem 4 (Ordered Triplets)</h4>
    <p>Let \\(A = \\{1, 2\\}\\). Form the Cartesian product \\(A \\times A \\times A\\).</p>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        <p>The number of elements is \\(n(A)^3 = 2^3 = 8\\). The elements are all ordered triplets:
          \\[ A \\times A \\times A = \\{ (1,1,1), (1,1,2), (1,2,1), (1,2,2), (2,1,1), (2,1,2), (2,2,1), (2,2,2) \\} \\]
        </p>
      </div>
    </details>
  </div>
`;

// 4. REVISION TAB
const revisionHtml = `
  <h2>Quick Revision & Formula Cheat Sheet</h2>
  <div class="revision-grid">
    <div class="revision-card">
      <h4>Ordered Pairs & Products</h4>
      <ul>
        <li>\\((a, b) = (c, d) \\iff a = c\\) and \\(b = d\\)</li>
        <li>\\(A \\times B = \\{(a, b) : a \\in A, b \\in B\\}\\)</li>
        <li>\\(n(A \\times B) = n(A) \\cdot n(B)\\)</li>
        <li>\\(A \\times B \\neq B \\times A\\) (unless \\(A = B\\) or empty)</li>
      </ul>
    </div>
    <div class="revision-card">
      <h4>Key Identities</h4>
      <ul>
        <li>\\(A \\times (B \\cup C) = (A \\times B) \\cup (A \\times C)\\)</li>
        <li>\\(A \\times (B \\cap C) = (A \\times B) \\cap (A \\times C)\\)</li>
        <li>\\((A \\times B) \\cap (B \\times A) = (A \\cap B)^2\\)</li>
        <li>If \\(A \\subseteq B\\), then \\(A \\times C \\subseteq B \\times C\\)</li>
      </ul>
    </div>
    <div class="revision-card">
      <h4>Subsets of \\(A \\times B\\)</h4>
      <ul>
        <li>Total subsets of \\(A \\times B = 2^{n(A) \\cdot n(B)}\\)</li>
        <li>Each subset of \\(A \\times B\\) defines a <strong>relation</strong> from \\(A\\) to \\(B\\)</li>
      </ul>
    </div>
  </div>
`;

// 5. MOCK EXAM TAB
const mockHtml = `
  <h2>10-Question Diagnostic Mock Exam</h2>
  <p class="lead-p">Test your understanding of Cartesian Products, Ordered Pairs, and Algebraic Systems under timed CBSE examination conditions.</p>
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
    question: "If \\((x + 1, \\, y - 2) = (3, \\, 1)\\), find the values of \\(x\\) and \\(y\\).",
    options: ["\\(x=2, y=3\\)", "\\(x=4, y=3\\)", "\\(x=2, y=-1\\)", "\\(x=3, y=2\\)"],
    correct: 0,
    explanation: "\\(x + 1 = 3 \\implies x = 2\\), and \\(y - 2 = 1 \\implies y = 3\\)."
  },
  {
    id: 2,
    question: "If \\(n(A) = 3\\) and \\(n(B) = 4\\), how many elements are in \\(A \\times B\\)?",
    options: ["7", "12", "64", "81"],
    correct: 1,
    explanation: "\\(n(A \\times B) = n(A) \\times n(B) = 3 \\times 4 = 12\\)."
  },
  {
    id: 3,
    question: "If set \\(A\\) has 3 elements and set \\(B = \\{3, 4, 5\\}\\), what is the total number of subsets of \\(A \\times B\\)?",
    options: ["\\(2^6\\)", "\\(2^9\\)", "\\(2^{12}\\)", "\\(3^9\\)"],
    correct: 1,
    explanation: "\\(n(A) = 3\\) and \\(n(B) = 3\\), so \\(n(A \\times B) = 3 \\times 3 = 9\\). The total number of subsets of \\(A \\times B\\) is \\(2^9 = 512\\)."
  },
  {
    id: 4,
    question: "If \\(A = \\{1, 2\\}\\) and \\(B = \\{3, 4\\}\\), how many elements does \\(A \\times (B \\cap \\emptyset)\\) contain?",
    options: ["0", "2", "4", "8"],
    correct: 0,
    explanation: "\\(B \\cap \\emptyset = \\emptyset\\). The Cartesian product of any set with the empty set is the empty set: \\(A \\times \\emptyset = \\emptyset\\), which has 0 elements."
  },
  {
    id: 5,
    question: "If \\(A \\times B = \\{(a, x), (a, y), (b, x), (b, y)\\}\\), what are the sets \\(A\\) and \\(B\\)?",
    options: [
      "\\(A = \\{a, b\\}, B = \\{x, y\\}\\)",
      "\\(A = \\{x, y\\}, B = \\{a, b\\}\\)",
      "\\(A = \\{a, x\\}, B = \\{b, y\\}\\)",
      "\\(A = \\{a, b, x\\}, B = \\{y\\}\\)"
    ],
    correct: 0,
    explanation: "Set \\(A\\) consists of all first coordinates: \\(\\{a, b\\}\\). Set \\(B\\) consists of all second coordinates: \\(\\{x, y\\}\\)."
  },
  {
    id: 6,
    question: "If two sets \\(A\\) and \\(B\\) have 4 elements in common, how many elements do \\(A \\times B\\) and \\(B \\times A\\) have in common?",
    options: ["4", "8", "16", "64"],
    correct: 2,
    explanation: "The common elements are \\((A \\times B) \\cap (B \\times A) = (A \\cap B) \\times (A \\cap B)\\). Its cardinality is \\(4 \\times 4 = 16\\)."
  },
  {
    id: 7,
    question: "If \\(A = \\{-1, 1\\}\\), what is the number of elements in \\(A \\times A \\times A\\)?",
    options: ["3", "6", "8", "9"],
    correct: 2,
    explanation: "\\(n(A) = 2\\). Therefore \\(n(A \\times A \\times A) = 2 \\times 2 \\times 2 = 8\\)."
  },
  {
    id: 8,
    question: "Which of the following identities is FALSE for general non-empty sets \\(A, B, C\\)?",
    options: [
      "\\(A \\times (B \\cap C) = (A \\times B) \\cap (A \\times C)\\)",
      "\\(A \\times (B \\cup C) = (A \\times B) \\cup (A \\times C)\\)",
      "\\(A \\times B = B \\times A\\)",
      "\\(A \\times (B - C) = (A \\times B) - (A \\times C)\\)"
    ],
    correct: 2,
    explanation: "The Cartesian product is NOT commutative; \\(A \\times B \\neq B \\times A\\) unless \\(A = B\\)."
  },
  {
    id: 9,
    question: "Let \\(A = \\{1, 2, 3\\}\\). What is the total number of ordered pairs in \\(A \\times A\\) of the form \\((a, b)\\) such that \\(a < b\\)?",
    options: ["2", "3", "4", "6"],
    correct: 1,
    explanation: "The pairs in \\(A \\times A\\) with \\(a < b\\) are \\((1, 2), (1, 3), (2, 3)\\). There are exactly 3 such pairs."
  },
  {
    id: 10,
    question: "If \\(n(A \\times B) = 6\\) and three elements of \\(A \\times B\\) are \\((1, 4), (2, 5), (3, 4)\\), then set \\(B\\) is:",
    options: ["\\(\\{1, 2, 3\\}\\)", "\\(\\{4, 5\\}\\)", "\\(\\{1, 4, 5\\}\\)", "\\(\\{2, 4, 5\\}\\)"],
    correct: 1,
    explanation: "From the given pairs, the first coordinates show \\(\\{1, 2, 3\\} \\subseteq A\\), so \\(n(A) \\ge 3\\). The second coordinates show \\(\\{4, 5\\} \\subseteq B\\), so \\(n(B) \\ge 2\\). Since \\(n(A \\times B) = 6 = 3 \\times 2\\), we must have \\(A = \\{1, 2, 3\\}\\) and \\(B = \\{4, 5\\}\\)."
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
    resultsBox.innerHTML += '<p style="color:#059669; font-weight:600;">Outstanding! Superb command of Cartesian products and ordered pairs.</p>';
  } else if (pct >= 50) {
    resultsBox.innerHTML += '<p style="color:#d97706; font-weight:600;">Good effort! Review distributive laws and subset counts of products.</p>';
  } else {
    resultsBox.innerHTML += '<p style="color:#dc2626; font-weight:600;">Needs revision. Study the worked examples on ordered pairs and try again.</p>';
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
console.log('Successfully upgraded 5-1-cartesian-product-of-sets/index.html');

