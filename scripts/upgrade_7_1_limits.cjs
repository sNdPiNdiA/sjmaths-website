const fs = require('fs');
const cheerio = require('cheerio');

const filePath = 'class-11-applied-mathematics/chapter-7-calculus/7-1-limits/index.html';
const html = fs.readFileSync(filePath, 'utf8');
const $ = cheerio.load(html);

// 1. LEARN TAB
const learnHtml = `
  <h2>7.1 Limits: Foundations, Left/Right Hand Bounds, and Indeterminate Forms</h2>
  <p class="lead-p">
    Calculus is the mathematical language of instantaneous change, continuous compounding, and economic marginality. The <strong>limit</strong> is the foundational gateway to calculus: it formalizes the behavior of a function near a point, rather than its value at the point itself, resolving apparent indeterminacies like \\(\\frac{0}{0}\\).
  </p>

  <div class="formula-box">
    <h3>Fundamental Definitions & Algebraic Limit Theorems</h3>
    <ul>
      <li><strong>Intuitive Definition of a Limit:</strong> We write:
        \\[ \\lim_{x \\to c} f(x) = L \\]
        if the values of \\(f(x)\\) can be made arbitrarily close to \\(L\\) by taking \\(x\\) sufficiently close to \\(c\\) (from either side), but \\(x \\neq c\\).
      </li>
      <li><strong>Existence Theorem (LHL = RHL):</strong> The two-sided limit exists if and only if both the Left-Hand Limit (LHL) and Right-Hand Limit (RHL) exist and are equal:
        \\[ \\lim_{x \\to c} f(x) = L \\iff \\lim_{x \\to c^-} f(x) = \\lim_{x \\to c^+} f(x) = L \\]
      </li>
      <li><strong>Algebra of Limits:</strong> If \\(\\lim_{x \\to c} f(x) = L\\) and \\(\\lim_{x \\to c} g(x) = M\\):
        <ol>
          <li>\\(\\lim [f(x) \\pm g(x)] = L \\pm M\\)</li>
          <li>\\(\\lim [k \\cdot f(x)] = k \\cdot L\\) (for any constant \\(k\\))</li>
          <li>\\(\\lim [f(x) \\cdot g(x)] = L \\cdot M\\)</li>
          <li>\\(\\lim \\left[ \\frac{f(x)}{g(x)} \\right] = \\frac{L}{M} \\quad (\\text{provided } M \\neq 0)\\)</li>
          <li>\\(\\lim [f(x)]^n = L^n\\)</li>
        </ol>
      </li>
      <li><strong>Standard Algebraic Limit Formula:</strong>
        For any real number \\(a > 0\\) and any rational number \\(n\\):
        \\[ \\lim_{x \\to a} \\frac{x^n - a^n}{x - a} = n a^{n-1} \\]
      </li>
      <li><strong>Limits at Infinity (Asymptotic Long-Run Behavior):</strong>
        For rational functions \\(\\frac{P(x)}{Q(x)}\\), divide numerator and denominator by the highest power of \\(x\\):
        \\[ \\lim_{x \\to \\infty} \\frac{1}{x^k} = 0 \\quad (\\text{for } k > 0) \\]
      </li>
      <li><strong>The Continuous Compounding Euler Limit:</strong>
        \\[ \\lim_{n \\to \\infty} \\left( 1 + \\frac{1}{n} \\right)^n = e \\approx 2.71828 \\implies \\lim_{x \\to 0} (1 + x)^{\\frac{1}{x}} = e \\]
        In continuous compound interest: \\(A = \\lim_{m \\to \\infty} P \\left(1 + \\frac{r}{m}\\right)^{mt} = P e^{rt}\\).
      </li>
    </ul>
  </div>

  <h3>Systematic Techniques for Evaluating Indeterminate Limits \\(\\left(\\frac{0}{0}\\right)\\)</h3>
  <table class="table-styled">
    <thead>
      <tr>
        <th>Method</th>
        <th>Applicable Scenario</th>
        <th>Algebraic Strategy</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Direct Substitution</strong></td>
        <td>When \\(f(c)\\) evaluates to a definite real number</td>
        <td>Simply evaluate \\(f(c)\\)</td>
      </tr>
      <tr>
        <td><strong>Factorization</strong></td>
        <td>Polynomial fractions yielding \\(\\frac{0}{0}\\)</td>
        <td>Factor out and cancel the vanishing factor \\((x - c)\\)</td>
      </tr>
      <tr>
        <td><strong>Rationalization</strong></td>
        <td>Expressions involving square roots yielding \\(\\frac{0}{0}\\)</td>
        <td>Multiply numerator and denominator by the algebraic conjugate</td>
      </tr>
      <tr>
        <td><strong>Standard Formula</strong></td>
        <td>Expressions resembling \\(\\frac{x^n - a^n}{x^m - a^m}\\)</td>
        <td>Apply \\(\\lim_{x \\to a} \\frac{x^n - a^n}{x - a} = n a^{n-1}\\)</td>
      </tr>
      <tr>
        <td><strong>Highest Power Division</strong></td>
        <td>Limits as \\(x \\to \\infty\\) of rational expressions</td>
        <td>Divide numerator and denominator by highest power of \\(x\\)</td>
      </tr>
    </tbody>
  </table>

  <div class="worked-example">
    <h4>Worked Example: Evaluating Algebraic and Rational Limits</h4>
    <p><strong>Evaluate the following limits:</strong></p>
    <ol>
      <li>\\(\\displaystyle \\lim_{x \\to 2} \\frac{x^3 - 8}{x^2 - 4}\\)</li>
      <li>\\(\\displaystyle \\lim_{x \\to 0} \\frac{\\sqrt{1 + x} - 1}{x}\\)</li>
      <li>\\(\\displaystyle \\lim_{x \\to a} \\frac{x^{5/2} - a^{5/2}}{x^{1/2} - a^{1/2}}\\)</li>
    </ol>
    <div class="solution">
      <p><strong>Solution:</strong></p>
      <ol>
        <li><strong>Factorization:</strong> Substituting \\(x=2\\) gives \\(\\frac{0}{0}\\).
          \\[ \\lim_{x \\to 2} \\frac{(x - 2)(x^2 + 2x + 4)}{(x - 2)(x + 2)} = \\lim_{x \\to 2} \\frac{x^2 + 2x + 4}{x + 2} = \\frac{2^2 + 2(2) + 4}{2 + 2} = \\frac{12}{4} = 3. \\]
        </li>
        <li><strong>Rationalization:</strong> Multiply numerator and denominator by \\(\\sqrt{1 + x} + 1\\):
          \\[ \\lim_{x \\to 0} \\frac{(\\sqrt{1 + x} - 1)(\\sqrt{1 + x} + 1)}{x(\\sqrt{1 + x} + 1)} = \\lim_{x \\to 0} \\frac{(1 + x) - 1}{x(\\sqrt{1 + x} + 1)} \\]
          \\[ = \\lim_{x \\to 0} \\frac{x}{x(\\sqrt{1 + x} + 1)} = \\lim_{x \\to 0} \\frac{1}{\\sqrt{1 + x} + 1} = \\frac{1}{\\sqrt{1} + 1} = \\frac{1}{2}. \\]
        </li>
        <li><strong>Using Standard Theorem:</strong> Divide numerator and denominator by \\(x - a\\):
          \\[ \\lim_{x \\to a} \\frac{\\frac{x^{5/2} - a^{5/2}}{x - a}}{\\frac{x^{1/2} - a^{1/2}}{x - a}} = \\frac{\\frac{5}{2} a^{\\frac{5}{2} - 1}}{\\frac{1}{2} a^{\\frac{1}{2} - 1}} = \\frac{\\frac{5}{2} a^{3/2}}{\\frac{1}{2} a^{-1/2}} = 5 a^{\\frac{3}{2} - (-\\frac{1}{2})} = 5 a^2. \\]
        </li>
      </ol>
    </div>
  </div>
`;

// 2. PROGRESS TAB
const progressHtml = `
  <h2>Progress Tracker & Self-Assessment Checklist</h2>
  <p>Track your computational speed and mastery of Limits and Indeterminate Forms.</p>
  <div class="checklist-grid">
    <div class="checklist-card">
      <h4>Conceptual Milestones</h4>
      <ul>
        <li><label><input type="checkbox"> Define Left-Hand and Right-Hand limits and the condition for limit existence.</label></li>
        <li><label><input type="checkbox"> Identify indeterminate forms (\\(\\frac{0}{0}, \\frac{\\infty}{\\infty}\\)).</label></li>
        <li><label><input type="checkbox"> Apply the standard power theorem \\(\\lim_{x \\to a} \\frac{x^n - a^n}{x - a} = n a^{n-1}\\).</label></li>
        <li><label><input type="checkbox"> Understand the Euler limit \\(e\\) and continuous compounding.</label></li>
      </ul>
    </div>
    <div class="checklist-card">
      <h4>Problem Solving Milestones</h4>
      <ul>
        <li><label><input type="checkbox"> Evaluated limits via algebraic factorization.</label></li>
        <li><label><input type="checkbox"> Evaluated radical limits via algebraic conjugate rationalization.</label></li>
        <li><label><input type="checkbox"> Solved limits as \\(x \\to \\infty\\) for rational functions.</label></li>
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
    <h4>Problem 1 (Piecewise Limit Existence Check)</h4>
    <p>Let \\(f(x) = \\begin{cases} 2x + 3, & x \\le 1 \\\\ 3x - 1, & x > 1 \\end{cases}\\). Determine whether \\(\\lim_{x \\to 1} f(x)\\) exists.</p>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        <p>Evaluate Left-Hand Limit (LHL):</p>
        \\[ \\text{LHL} = \\lim_{x \\to 1^-} f(x) = \\lim_{x \\to 1^-} (2x + 3) = 2(1) + 3 = 5. \\]
        <p>Evaluate Right-Hand Limit (RHL):</p>
        \\[ \\text{RHL} = \\lim_{x \\to 1^+} f(x) = \\lim_{x \\to 1^+} (3x - 1) = 3(1) - 1 = 2. \\]
        <p>Since \\(\\text{LHL} \\neq \\text{RHL}\\) (\\(5 \\neq 2\\)), the two-sided limit <strong>\\(\\lim_{x \\to 1} f(x)\\) does NOT exist</strong>.</p>
      </div>
    </details>
  </div>

  <div class="problem-card">
    <h4>Problem 2 (Finding Parameters from a Known Limit)</h4>
    <p>If \\(\\displaystyle \\lim_{x \\to 2} \\frac{x^n - 2^n}{x - 2} = 80\\), where \\(n\\) is a positive integer, find the value of \\(n\\).</p>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        <p>Using the standard theorem \\(\\lim_{x \\to a} \\frac{x^n - a^n}{x - a} = n a^{n-1}\\):</p>
        \\[ n (2^{n-1}) = 80 \\]
        Express 80 as a product of an integer and a power of 2:
        \\[ 80 = 5 \\times 16 = 5 \\times 2^4 = 5 \\times 2^{5 - 1} \\]
        Comparing both sides directly:
        \\[ n = 5 \\]
        <strong>Answer:</strong> \\(n = 5\\).
      </div>
    </details>
  </div>

  <div class="problem-card">
    <h4>Problem 3 (Long-Run Average Cost Limit as Output \\(x \\to \\infty\\))</h4>
    <p>A manufacturing plant's total cost function is \\(C(x) = 5000 + 40x + 0.05x^2\\). The average cost per unit is \\(AC(x) = \\frac{C(x)}{x}\\). What does the average fixed cost component approach as output expands infinitely?</p>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        \\[ AC(x) = \\frac{5000}{x} + 40 + 0.05x \\]
        The average fixed cost is \\(AFC(x) = \\frac{5000}{x}\\).
        \\[ \\lim_{x \\to \\infty} AFC(x) = \\lim_{x \\to \\infty} \\frac{5000}{x} = 0. \\]
        <em>Economic Interpretation:</em> As scale reaches infinity, fixed costs are spread over infinite volume and approach zero per unit.
      </div>
    </details>
  </div>
`;

// 4. REVISION TAB
const revisionHtml = `
  <h2>Quick Revision & Formula Cheat Sheet</h2>
  <div class="revision-grid">
    <div class="revision-card">
      <h4>Limit Theorems</h4>
      <ul>
        <li>\\(\\lim_{x \\to c} f(x) = L \\iff \\text{LHL} = \\text{RHL} = L\\)</li>
        <li>\\(\\lim_{x \\to a} \\frac{x^n - a^n}{x - a} = n a^{n-1}\\)</li>
        <li>\\(\\lim_{x \\to 0} (1 + x)^{1/x} = e\\)</li>
        <li>\\(\\lim_{x \\to \\infty} (1 + 1/x)^x = e\\)</li>
      </ul>
    </div>
    <div class="revision-card">
      <h4>Technique Checklist</h4>
      <ul>
        <li>Try direct substitution first</li>
        <li>If \\(0/0\\) with polynomials: factor & cancel \\(x - a\\)</li>
        <li>If \\(0/0\\) with surds: multiply by conjugate</li>
        <li>If \\(x \\to \\infty\\): divide by highest degree term</li>
      </ul>
    </div>
    <div class="revision-card">
      <h4>Continuous Compounding</h4>
      <ul>
        <li>\\(A = P e^{rt}\\) is the limiting case of compounding \\(m \\to \\infty\\) times per year</li>
        <li>Euler's constant \\(e \\approx 2.71828\\)</li>
      </ul>
    </div>
  </div>
`;

// 5. MOCK EXAM TAB
const mockHtml = `
  <h2>10-Question Diagnostic Mock Exam</h2>
  <p class="lead-p">Test your mastery of Limits, Left/Right Bounds, and Indeterminate Forms under timed CBSE conditions.</p>
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
    question: "Evaluate \\(\\displaystyle \\lim_{x \\to 3} \\frac{x^2 - 9}{x - 3}\\).",
    options: ["0", "3", "6", "Does not exist"],
    correct: 2,
    explanation: "\\(\\lim_{x \\to 3} \\frac{(x-3)(x+3)}{x-3} = \\lim_{x \\to 3} (x + 3) = 3 + 3 = 6\\)."
  },
  {
    id: 2,
    question: "Evaluate \\(\\displaystyle \\lim_{x \\to 1} \\frac{x^4 - 1}{x - 1}\\).",
    options: ["1", "2", "4", "16"],
    correct: 2,
    explanation: "Using \\(n a^{n-1}\\): \\(4(1)^3 = 4\\)."
  },
  {
    id: 3,
    question: "What is \\(\\displaystyle \\lim_{x \\to 0} \\frac{|x|}{x}\\)?",
    options: ["1", "-1", "0", "Does not exist"],
    correct: 3,
    explanation: "For \\(x > 0\\), \\(|x|/x = x/x = 1\\) (RHL = 1). For \\(x < 0\\), \\(|x|/x = -x/x = -1\\) (LHL = -1). Since LHL \\(\\neq\\) RHL, the limit does not exist."
  },
  {
    id: 4,
    question: "Evaluate \\(\\displaystyle \\lim_{x \\to \\infty} \\frac{3x^2 + 5x + 7}{2x^2 - 3x + 1}\\).",
    options: ["0", "\\(\\frac{3}{2}\\)", "\\(7\\)", "\\(\\infty\\)"],
    correct: 1,
    explanation: "Dividing numerator and denominator by \\(x^2\\): \\(\\frac{3 + 5/x + 7/x^2}{2 - 3/x + 1/x^2} \\to \\frac{3}{2}\\)."
  },
  {
    id: 5,
    question: "Evaluate \\(\\displaystyle \\lim_{x \\to 0} \\frac{\\sqrt{4 + x} - 2}{x}\\).",
    options: ["\\(\\frac{1}{4}\\)", "\\(\\frac{1}{2}\\)", "1", "2"],
    correct: 0,
    explanation: "Multiplying numerator and denominator by \\(\\sqrt{4+x} + 2\\): \\(\\lim_{x \\to 0} \\frac{(4+x) - 4}{x(\\sqrt{4+x} + 2)} = \\frac{1}{2 + 2} = \\frac{1}{4}\\)."
  },
  {
    id: 6,
    question: "If \\(\\displaystyle \\lim_{x \\to a} \\frac{x^9 - a^9}{x - a} = 9\\), find the possible real values of \\(a\\).",
    options: ["\\(\\pm 1\\)", "\\(1\\)", "\\(0\\)", "\\(\\pm 3\\)"],
    correct: 0,
    explanation: "\\(9 a^8 = 9 \\implies a^8 = 1 \\implies a = \\pm 1\\)."
  },
  {
    id: 7,
    question: "Evaluate \\(\\displaystyle \\lim_{x \\to 2} \\frac{x^3 - 4x}{x^2 - 4}\\).",
    options: ["1", "2", "4", "0"],
    correct: 1,
    explanation: "\\(\\lim_{x \\to 2} \\frac{x(x^2 - 4)}{x^2 - 4} = \\lim_{x \\to 2} x = 2\\)."
  },
  {
    id: 8,
    question: "The value of \\(\\displaystyle \\lim_{n \\to \\infty} \\left( 1 + \\frac{1}{n} \\right)^n\\) is:",
    options: ["0", "1", "\\(e\\)", "\\(\\infty\\)"],
    correct: 2,
    explanation: "This is the fundamental definition of Euler's number \\(e \\approx 2.71828\\)."
  },
  {
    id: 9,
    question: "Evaluate \\(\\displaystyle \\lim_{x \\to 0} \\frac{(1 + x)^5 - 1}{x}\\).",
    options: ["1", "5", "10", "0"],
    correct: 1,
    explanation: "Let \\(y = 1 + x\\). As \\(x \\to 0\\), \\(y \\to 1\\). Then \\(\\lim_{y \\to 1} \\frac{y^5 - 1^5}{y - 1} = 5(1)^4 = 5\\)."
  },
  {
    id: 10,
    question: "If \\(f(x) = \\begin{cases} x + 2, & x < 2 \\\\ c, & x = 2 \\\\ 2x, & x > 2 \\end{cases}\\), for what value of \\(c\\) is the limit \\(\\lim_{x \\to 2} f(x)\\) equal to \\(f(2)\\)?",
    options: ["2", "4", "6", "Any real number"],
    correct: 1,
    explanation: "\\(\\text{LHL} = 2 + 2 = 4\\), \\(\\text{RHL} = 2(2) = 4\\). So \\(\\lim_{x \\to 2} f(x) = 4\\). For the limit to equal \\(f(2) = c\\), we must have \\(c = 4\\)."
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
    resultsBox.innerHTML += '<p style="color:#059669; font-weight:600;">Outstanding! Masterful proficiency in algebraic limits and indeterminate forms.</p>';
  } else if (pct >= 50) {
    resultsBox.innerHTML += '<p style="color:#d97706; font-weight:600;">Good effort! Review rationalization and standard limit theorems and retry.</p>';
  } else {
    resultsBox.innerHTML += '<p style="color:#dc2626; font-weight:600;">Needs revision. Study the worked examples on limits and try again.</p>';
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
console.log('Successfully upgraded 7-1-limits/index.html');

