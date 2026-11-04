const fs = require('fs');
const cheerio = require('cheerio');

const filePath = 'class-11-applied-mathematics/chapter-6-sequences-and-series/6-3-relationship-between-am-and-gm/index.html';
const html = fs.readFileSync(filePath, 'utf8');
const $ = cheerio.load(html);

// 1. LEARN TAB
const learnHtml = `
  <h2>6.3 Relationship Between AM and GM: Inequality Proofs and Optimization</h2>
  <p class="lead-p">
    In Applied Mathematics, cost minimization, and financial engineering, the relationship between the <strong>Arithmetic Mean (AM)</strong> and the <strong>Geometric Mean (GM)</strong> provides one of the most powerful algebraic bounds in existence. It enables analysts to find minimum operating costs and maximum asset yields without requiring differential calculus.
  </p>

  <div class="formula-box">
    <h3>Fundamental Theorems & Properties</h3>
    <ul>
      <li><strong>The AM-GM Inequality:</strong> For any two positive real numbers \\(a > 0\\) and \\(b > 0\\):
        \\[ \\text{AM} \\ge \\text{GM} \\iff \\frac{a + b}{2} \\ge \\sqrt{ab} \\]
        Equality holds (\\(\\text{AM} = \\text{GM}\\)) <strong>if and only if</strong> \\(a = b\\).
      </li>
      <li><strong>Rigorous Algebraic Proof:</strong>
        Consider the difference:
        \\[ \\text{AM} - \\text{GM} = \\frac{a + b}{2} - \\sqrt{ab} = \\frac{a + b - 2\\sqrt{ab}}{2} = \\frac{(\\sqrt{a} - \\sqrt{b})^2}{2} \\]
        Since the square of any real number is non-negative, \\(\\frac{(\\sqrt{a} - \\sqrt{b})^2}{2} \\ge 0\\).
        Hence, \\(\\text{AM} \\ge \\text{GM}\\).
      </li>
      <li><strong>Quadratic Equation Construction:</strong> If \\(A\\) and \\(G\\) are the AM and GM of two positive numbers \\(a\\) and \\(b\\):
        \\[ a + b = 2A, \\quad ab = G^2 \\]
        The quadratic equation whose roots are \\(a\\) and \\(b\\) is:
        \\[ x^2 - 2Ax + G^2 = 0 \\]
        By the quadratic formula, the numbers are given by:
        \\[ a, b = A \\pm \\sqrt{A^2 - G^2} \\]
      </li>
      <li><strong>The Ratio Theorem:</strong> If the AM of two positive numbers is to their GM in the ratio \\(m : n\\) (where \\(m > n > 0\\)), then the ratio of the two numbers is:
        \\[ \\frac{a}{b} = \\frac{m + \\sqrt{m^2 - n^2}}{m - \\sqrt{m^2 - n^2}} \\]
      </li>
      <li><strong>Generalization to \\(n\\) Positive Variables:</strong>
        \\[ \\frac{x_1 + x_2 + \\dots + x_n}{n} \\ge \\sqrt[n]{x_1 x_2 \\dots x_n} \\]
      </li>
    </ul>
  </div>

  <h3>Applied Business Optimization: Minimizing Operating Cost</h3>
  <div class="worked-example">
    <h4>Example: Inventory Carrying and Ordering Costs</h4>
    <p><strong>Scenario:</strong> A supply chain manager models the annual operating cost \\(C(x)\\) of maintaining a warehouse stocking quantity \\(x > 0\\) as:
      \\[ C(x) = 4x + \\frac{2500}{x} \\]
      where \\(4x\\) represents carrying storage costs and \\(\\frac{2500}{x}\\) represents ordering overheads.
      Using the AM-GM inequality, determine the minimum annual operating cost and the optimal stocking quantity \\(x\\).
    </p>
    <div class="solution">
      <p><strong>Solution:</strong></p>
      <p>Let \\(a = 4x\\) and \\(b = \\frac{2500}{x}\\). Since \\(x > 0\\), both \\(a > 0\\) and \\(b > 0\\).</p>
      <p>By the AM-GM Inequality:</p>
      \\[ \\frac{a + b}{2} \\ge \\sqrt{ab} \\implies a + b \\ge 2\\sqrt{ab} \\]
      \\[ C(x) = 4x + \\frac{2500}{x} \\ge 2 \\sqrt{4x \\cdot \\frac{2500}{x}} = 2 \\sqrt{10{,}000} = 2 \\times 100 = 200 \\]
      <p>The minimum annual operating cost is <strong>₹200</strong>.</p>
      <p>This minimum occurs when equality holds in the AM-GM inequality, which requires \\(a = b\\):</p>
      \\[ 4x = \\frac{2500}{x} \\implies 4x^2 = 2500 \\implies x^2 = 625 \\implies x = 25 \\text{ units.} \\]
      <p>Thus, the optimal stocking order is <strong>25 units</strong>.</p>
    </div>
  </div>
`;

// 2. PROGRESS TAB
const progressHtml = `
  <h2>Progress Tracker & Self-Assessment Checklist</h2>
  <p>Track your computational speed and mastery of the AM-GM relationship and optimization bounds.</p>
  <div class="checklist-grid">
    <div class="checklist-card">
      <h4>Conceptual Milestones</h4>
      <ul>
        <li><label><input type="checkbox"> Formulate and prove the fundamental AM-GM inequality \\(\\frac{a+b}{2} \\ge \\sqrt{ab}\\).</label></li>
        <li><label><input type="checkbox"> Understand the exact equality condition \\(a = b\\).</label></li>
        <li><label><input type="checkbox"> Reconstruct numbers from AM and GM via \\(x^2 - 2Ax + G^2 = 0\\).</label></li>
        <li><label><input type="checkbox"> Master the Ratio Theorem \\(\\frac{a}{b} = \\frac{m + \\sqrt{m^2-n^2}}{m - \\sqrt{m^2-n^2}}\\).</label></li>
      </ul>
    </div>
    <div class="checklist-card">
      <h4>Problem Solving Milestones</h4>
      <ul>
        <li><label><input type="checkbox"> Solved algebraic minimum values for reciprocal expressions \\(x + \\frac{1}{x}\\).</label></li>
        <li><label><input type="checkbox"> Computed the ratio of numbers given \\(\\text{AM} : \\text{GM} = m : n\\).</label></li>
        <li><label><input type="checkbox"> Applied AM-GM bounds to supply chain and inventory optimization problems.</label></li>
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
    <h4>Problem 1 (Finding Numbers from AM and GM)</h4>
    <p>If the Arithmetic Mean (AM) of two positive numbers is 10 and their Geometric Mean (GM) is 8, find the two numbers.</p>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        <p>Given \\(A = 10\\) and \\(G = 8\\).</p>
        <p>The numbers are given by the roots of \\(x^2 - 2Ax + G^2 = 0\\):</p>
        \\[ x^2 - 2(10)x + 8^2 = 0 \\implies x^2 - 20x + 64 = 0 \\]
        Factoring:
        \\[ (x - 16)(x - 4) = 0 \\implies x = 16 \\quad \\text{or} \\quad x = 4 \\]
        Alternatively, using the formula:
        \\[ a, b = A \\pm \\sqrt{A^2 - G^2} = 10 \\pm \\sqrt{100 - 64} = 10 \\pm \\sqrt{36} = 10 \\pm 6 \\]
        This gives \\(10 + 6 = 16\\) and \\(10 - 6 = 4\\).
        <strong>Answer:</strong> The numbers are <strong>16 and 4</strong>.
      </div>
    </details>
  </div>

  <div class="problem-card">
    <h4>Problem 2 (Ratio of Numbers from AM:GM Ratio)</h4>
    <p>If the AM and GM of two positive numbers are in the ratio \\(5 : 4\\), show that the ratio of the numbers is \\(4 : 1\\).</p>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        <p>Given \\(\\frac{\\text{AM}}{\\text{GM}} = \\frac{a + b}{2\\sqrt{ab}} = \\frac{5}{4}\\).</p>
        <p>Using the Ratio Theorem with \\(m = 5\\) and \\(n = 4\\):</p>
        \\[ \\frac{a}{b} = \\frac{m + \\sqrt{m^2 - n^2}}{m - \\sqrt{m^2 - n^2}} = \\frac{5 + \\sqrt{25 - 16}}{5 - \\sqrt{25 - 16}} = \\frac{5 + \\sqrt{9}}{5 - \\sqrt{9}} = \\frac{5 + 3}{5 - 3} = \\frac{8}{2} = \\frac{4}{1} \\]
        Hence, the ratio of the numbers is <strong>\\(4 : 1\\)</strong>.
      </div>
    </details>
  </div>

  <div class="problem-card">
    <h4>Problem 3 (Inequality Bound for Sum of Reciprocals)</h4>
    <p>If \\(a, b, c\\) are positive real numbers, prove that:
      \\[ (a + b + c) \\left( \\frac{1}{a} + \\frac{1}{b} + \\frac{1}{c} \\right) \\ge 9 \\]
    </p>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        <p>Apply the AM-GM Inequality to \\(a, b, c\\):</p>
        \\[ \\frac{a + b + c}{3} \\ge \\sqrt[3]{abc} \\implies a + b + c \\ge 3 \\sqrt[3]{abc} \\quad \\text{--- (1)} \\]
        Apply the AM-GM Inequality to \\(\\frac{1}{a}, \\frac{1}{b}, \\frac{1}{c}\\):</p>
        \\[ \\frac{\\frac{1}{a} + \\frac{1}{b} + \\frac{1}{c}}{3} \\ge \\sqrt[3]{\\frac{1}{abc}} \\implies \\frac{1}{a} + \\frac{1}{b} + \\frac{1}{c} \\ge 3 \\sqrt[3]{\\frac{1}{abc}} \\quad \\text{--- (2)} \\]
        Multiplying inequalities (1) and (2):
        \\[ (a + b + c) \\left( \\frac{1}{a} + \\frac{1}{b} + \\frac{1}{c} \\right) \\ge \\left( 3 \\sqrt[3]{abc} \\right) \\left( 3 \\sqrt[3]{\\frac{1}{abc}} \\right) = 9 \\]
        This completes the proof.
      </div>
    </details>
  </div>
`;

// 4. REVISION TAB
const revisionHtml = `
  <h2>Quick Revision & Formula Cheat Sheet</h2>
  <div class="revision-grid">
    <div class="revision-card">
      <h4>AM-GM Inequality</h4>
      <ul>
        <li>\\(\\frac{a + b}{2} \\ge \\sqrt{ab}\\) for all \\(a, b > 0\\)</li>
        <li>Equality holds \\(\\iff a = b\\)</li>
        <li>Minimum value of \\(x + \\frac{k}{x}\\) is \\(2\\sqrt{k}\\) (for \\(x > 0\\))</li>
        <li>\\(\\text{AM} - \\text{GM} = \\frac{(\\sqrt{a} - \\sqrt{b})^2}{2}\\)</li>
      </ul>
    </div>
    <div class="revision-card">
      <h4>Forming Quadratic Equations</h4>
      <ul>
        <li>\\(x^2 - 2Ax + G^2 = 0\\)</li>
        <li>Roots: \\(a, b = A \\pm \\sqrt{A^2 - G^2}\\)</li>
        <li>Discriminant \\(D = 4(A^2 - G^2) \\ge 0\\) ensures real roots</li>
      </ul>
    </div>
    <div class="revision-card">
      <h4>Ratio Formula</h4>
      <ul>
        <li>If \\(\\text{AM} : \\text{GM} = m : n\\):</li>
        <li>\\(\\frac{a}{b} = \\frac{m + \\sqrt{m^2 - n^2}}{m - \\sqrt{m^2 - n^2}}\\)</li>
      </ul>
    </div>
  </div>
`;

// 5. MOCK EXAM TAB
const mockHtml = `
  <h2>10-Question Diagnostic Mock Exam</h2>
  <p class="lead-p">Test your mastery of the AM-GM Relationship, Roots Reconstruction, and Algebraic Bounds under timed CBSE examination conditions.</p>
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
    question: "If \\(a\\) and \\(b\\) are distinct positive real numbers, which of the following is strictly true?",
    options: ["\\(\\text{AM} > \\text{GM}\\)", "\\(\\text{AM} = \\text{GM}\\)", "\\(\\text{AM} < \\text{GM}\\)", "\\(\\text{AM} \\le \\text{GM}\\)"],
    correct: 0,
    explanation: "Because \\(a\\) and \\(b\\) are distinct (\\(a \\neq b\\)), equality cannot hold, hence \\(\\text{AM} > \\text{GM}\\)."
  },
  {
    id: 2,
    question: "If the AM of two positive numbers is 25 and their GM is 20, what are the two numbers?",
    options: ["40 and 10", "45 and 5", "30 and 20", "35 and 15"],
    correct: 0,
    explanation: "\\(a, b = A \\pm \\sqrt{A^2 - G^2} = 25 \\pm \\sqrt{625 - 400} = 25 \\pm 15\\). This gives 40 and 10."
  },
  {
    id: 3,
    question: "For \\(x > 0\\), what is the minimum value of \\(9x + \\frac{16}{x}\\)?",
    options: ["12", "24", "25", "144"],
    correct: 1,
    explanation: "By AM-GM: \\(9x + 16/x \\ge 2\\sqrt{9x \\cdot 16/x} = 2\\sqrt{144} = 2(12) = 24\\)."
  },
  {
    id: 4,
    question: "If the AM between two positive numbers is to their GM as \\(13 : 12\\), what is the ratio of the numbers?",
    options: ["\\(3 : 2\\)", "\\(4 : 1\\)", "\\(9 : 4\\)", "\\(5 : 1\\)"],
    correct: 2,
    explanation: "\\(\\frac{a}{b} = \\frac{13 + \\sqrt{169 - 144}}{13 - \\sqrt{169 - 144}} = \\frac{13 + 5}{13 - 5} = \\frac{18}{8} = \\frac{9}{4}\\)."
  },
  {
    id: 5,
    question: "If the AM of two numbers is 34 and their GM is 16, what is the quadratic equation whose roots are these two numbers?",
    options: [
      "\\(x^2 - 68x + 256 = 0\\)",
      "\\(x^2 - 34x + 256 = 0\\)",
      "\\(x^2 - 68x + 16 = 0\\)",
      "\\(x^2 - 34x + 16 = 0\\)"
    ],
    correct: 0,
    explanation: "Equation is \\(x^2 - 2Ax + G^2 = 0 \\implies x^2 - 2(34)x + 16^2 = 0 \\implies x^2 - 68x + 256 = 0\\)."
  },
  {
    id: 6,
    question: "What is the minimum value of \\(2^x + 2^{-x}\\) for any real number \\(x\\)?",
    options: ["0", "1", "2", "4"],
    correct: 2,
    explanation: "Since \\(2^x > 0\\) for all \\(x \\in \\mathbb{R}\\), by AM-GM: \\(\\frac{2^x + 2^{-x}}{2} \\ge \\sqrt{2^x \\cdot 2^{-x}} = \\sqrt{1} = 1 \\implies 2^x + 2^{-x} \\ge 2\\). Minimum is 2 (at \\(x=0\\))."
  },
  {
    id: 7,
    question: "If \\(a, b, c > 0\\), what is the minimum value of \\(\\frac{a}{b} + \\frac{b}{c} + \\frac{c}{a}\\)?",
    options: ["1", "2", "3", "6"],
    correct: 2,
    explanation: "By AM-GM on 3 positive terms: \\(\\frac{a/b + b/c + c/a}{3} \\ge \\sqrt[3]{(a/b)(b/c)(c/a)} = 1 \\implies \\text{Sum} \\ge 3\\)."
  },
  {
    id: 8,
    question: "Under what condition does \\(\\text{AM} = \\text{GM}\\) hold for positive numbers?",
    options: ["\\(a + b = 1\\)", "\\(a = b\\)", "\\(ab = 1\\)", "\\(a^2 + b^2 = 1\\)"],
    correct: 1,
    explanation: "\\(\\text{AM} = \\text{GM} \\iff \\frac{(\\sqrt{a} - \\sqrt{b})^2}{2} = 0 \\iff \\sqrt{a} = \\sqrt{b} \\iff a = b\\)."
  },
  {
    id: 9,
    question: "If \\(A\\) is the AM and \\(G\\) is the GM between two distinct positive numbers, then:",
    options: [
      "\\(A^2 - G^2 < 0\\)",
      "\\(A^2 - G^2 = 0\\)",
      "\\(A^2 - G^2 > 0\\)",
      "\\(A^2 + G^2 = 0\\)"
    ],
    correct: 2,
    explanation: "Since \\(A > G > 0\\), squaring gives \\(A^2 > G^2 \\implies A^2 - G^2 > 0\\)."
  },
  {
    id: 10,
    question: "A company’s total cost function is \\(TC(q) = 5q + \\frac{180}{q} + 50\\) for \\(q > 0\\). What is the minimum possible total cost?",
    options: ["₹60", "₹110", "₹140", "₹170"],
    correct: 1,
    explanation: "By AM-GM on \\(5q + 180/q\\): \\(5q + 180/q \\ge 2\\sqrt{5 \\times 180} = 2\\sqrt{900} = 2(30) = 60\\). Adding fixed cost ₹50 gives total cost \\(\\ge 60 + 50 = ₹110\\)."
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
    resultsBox.innerHTML += '<p style="color:#059669; font-weight:600;">Outstanding! Exceptional mastery of AM-GM inequalities and economic optimization.</p>';
  } else if (pct >= 50) {
    resultsBox.innerHTML += '<p style="color:#d97706; font-weight:600;">Good effort! Review the Ratio Theorem and quadratic reconstruction.</p>';
  } else {
    resultsBox.innerHTML += '<p style="color:#dc2626; font-weight:600;">Needs revision. Study the AM-GM proofs and minimal cost worked examples.</p>';
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
console.log('Successfully upgraded 6-3-relationship-between-am-and-gm/index.html');
