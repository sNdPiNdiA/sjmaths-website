const fs = require('fs');
const cheerio = require('cheerio');

const filePath = 'class-11-applied-mathematics/chapter-7-calculus/7-4-rules-and-formulas-of-differentiation/index.html';
const html = fs.readFileSync(filePath, 'utf8');
const $ = cheerio.load(html);

// 1. LEARN TAB
const learnHtml = `
  <h2>7.4 Rules and Formulas of Differentiation</h2>
  <p class="lead-p">
    In Applied Mathematics, corporate financial engineering, and revenue management, functions rarely exist in isolation; they appear as products, quotients, and nested compositions. The <strong>rules of differentiation</strong>—Power Rule, Product Rule, Quotient Rule, Chain Rule, and Logarithmic Differentiation—provide the algorithmic engine to differentiate complex economic models rapidly and accurately.
  </p>

  <div class="formula-box">
    <h3>Master Formulary of Differentiation Rules</h3>
    <ul>
      <li><strong>Power Rule:</strong>
        \\[ \\frac{d}{dx}(x^n) = n x^{n-1} \\quad (\\text{for any real } n) \\]
      </li>
      <li><strong>Constant Multiple Rule:</strong>
        \\[ \\frac{d}{dx}[c \\cdot f(x)] = c \\cdot f'(x) \\]
      </li>
      <li><strong>Sum & Difference Rule:</strong>
        \\[ \\frac{d}{dx}[u(x) \\pm v(x)] = u'(x) \\pm v'(x) \\]
      </li>
      <li><strong>Product Rule (Leibniz Rule):</strong>
        \\[ \\frac{d}{dx}[u \\cdot v] = u \\frac{dv}{dx} + v \\frac{du}{dx} = u v' + v u' \\]
        For three factors: \\((u v w)' = u' v w + u v' w + u v w'\\).
      </li>
      <li><strong>Quotient Rule:</strong>
        \\[ \\frac{d}{dx} \\left[ \\frac{u}{v} \\right] = \\frac{v \\frac{du}{dx} - u \\frac{dv}{dx}}{v^2} = \\frac{v u' - u v'}{v^2} \\quad (v \\neq 0) \\]
      </li>
      <li><strong>Chain Rule (Composite Functions):</strong>
        If \\(y = f(u)\\) and \\(u = g(x)\\):
        \\[ \\frac{dy}{dx} = \\frac{dy}{du} \\cdot \\frac{du}{dx} = f'(g(x)) \\cdot g'(x) \\]
        <em>Generalized Power Rule:</em> \\(\\frac{d}{dx}[u(x)]^n = n [u(x)]^{n-1} \\cdot u'(x)\\).
      </li>
      <li><strong>Exponential & Logarithmic Derivatives (Applied Math):</strong>
        \\[ \\frac{d}{dx}(e^x) = e^x, \\quad \\frac{d}{dx}(e^{kx}) = k e^{kx}, \\quad \\frac{d}{dx}(a^x) = a^x \\ln a \\]
        \\[ \\frac{d}{dx}(\\ln x) = \\frac{1}{x}, \\quad \\frac{d}{dx}(\\log_a x) = \\frac{1}{x \\ln a} \\]
      </li>
      <li><strong>Second Order Derivative (Concavity & Acceleration):</strong>
        \\[ \\frac{d^2 y}{dx^2} = f''(x) = \\frac{d}{dx} \\left( \\frac{dy}{dx} \\right) \\]
      </li>
    </ul>
  </div>

  <h3>Systematic Problem-Solving Strategy</h3>
  <table class="table-styled">
    <thead>
      <tr>
        <th>Form of Expression</th>
        <th>Primary Rule to Deploy</th>
        <th>Algebraic Tip</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>\\(y = (2x + 3)^5\\)</td>
        <td>Chain Rule (Generalized Power)</td>
        <td>Differentiate outer power, multiply by inner derivative: \\(5(2x+3)^4 \\times 2 = 10(2x+3)^4\\)</td>
      </tr>
      <tr>
        <td>\\(y = x^2 e^{3x}\\)</td>
        <td>Product Rule + Exponential Chain</td>
        <td>\\(x^2 \\frac{d}{dx}(e^{3x}) + e^{3x} \\frac{d}{dx}(x^2) = x^2(3e^{3x}) + 2x e^{3x}\\)</td>
      </tr>
      <tr>
        <td>\\(y = \\frac{2x - 1}{3x + 4}\\)</td>
        <td>Quotient Rule</td>
        <td>Denominator squared on bottom; keep \\(v u' - u v'\\) in correct order</td>
      </tr>
      <tr>
        <td>\\(y = x^x\\)</td>
        <td>Logarithmic Differentiation</td>
        <td>Take \\(\\ln\\) on both sides: \\(\\ln y = x \\ln x\\), then differentiate implicitly</td>
      </tr>
    </tbody>
  </table>

  <div class="worked-example">
    <h4>Comprehensive Multi-Step Worked Examples</h4>
    <p><strong>Differentiate the following with respect to \\(x\\):</strong></p>
    <ol>
      <li>\\(\\displaystyle y = \\frac{x^2 + 1}{x^2 - 1}\\)</li>
      <li>\\(\\displaystyle y = (3x^2 - 5)^4 \\cdot (2x + 1)^3\\)</li>
      <li>\\(\\displaystyle y = e^{2x} \\ln(x^2 + 1)\\)</li>
    </ol>
    <div class="solution">
      <p><strong>Solution:</strong></p>
      <ol>
        <li><strong>Quotient Rule:</strong>
          \\[ \\frac{dy}{dx} = \\frac{(x^2 - 1) \\frac{d}{dx}(x^2 + 1) - (x^2 + 1) \\frac{d}{dx}(x^2 - 1)}{(x^2 - 1)^2} \\]
          \\[ = \\frac{(x^2 - 1)(2x) - (x^2 + 1)(2x)}{(x^2 - 1)^2} = \\frac{2x^3 - 2x - (2x^3 + 2x)}{(x^2 - 1)^2} = \\frac{-4x}{(x^2 - 1)^2}. \\]
        </li>
        <li><strong>Product & Chain Rules:</strong>
          \\[ \\frac{dy}{dx} = (3x^2 - 5)^4 \\frac{d}{dx}[(2x + 1)^3] + (2x + 1)^3 \\frac{d}{dx}[(3x^2 - 5)^4] \\]
          \\[ = (3x^2 - 5)^4 [3(2x + 1)^2 \\times 2] + (2x + 1)^3 [4(3x^2 - 5)^3 \\times 6x] \\]
          \\[ = 6(3x^2 - 5)^4 (2x + 1)^2 + 24x(2x + 1)^3 (3x^2 - 5)^3 \\]
          Factor out common terms \\(6(3x^2 - 5)^3 (2x + 1)^2\\):
          \\[ = 6(3x^2 - 5)^3 (2x + 1)^2 [(3x^2 - 5) + 4x(2x + 1)] \\]
          \\[ = 6(3x^2 - 5)^3 (2x + 1)^2 [3x^2 - 5 + 8x^2 + 4x] = 6(3x^2 - 5)^3 (2x + 1)^2 (11x^2 + 4x - 5). \\]
        </li>
        <li><strong>Product & Chain on Exponential & Logarithmic:</strong>
          \\[ \\frac{dy}{dx} = e^{2x} \\frac{d}{dx}[\\ln(x^2 + 1)] + \\ln(x^2 + 1) \\frac{d}{dx}[e^{2x}] \\]
          \\[ = e^{2x} \\left[ \\frac{2x}{x^2 + 1} \\right] + 2 e^{2x} \\ln(x^2 + 1) = 2 e^{2x} \\left[ \\frac{x}{x^2 + 1} + \\ln(x^2 + 1) \\right]. \\]
        </li>
      </ol>
    </div>
  </div>
`;

// 2. PROGRESS TAB
const progressHtml = `
  <h2>Progress Tracker & Self-Assessment Checklist</h2>
  <p>Track your computational speed and mastery of Differentiation Rules.</p>
  <div class="checklist-grid">
    <div class="checklist-card">
      <h4>Conceptual Milestones</h4>
      <ul>
        <li><label><input type="checkbox"> Apply Power, Sum, and Constant Multiple rules seamlessly.</label></li>
        <li><label><input type="checkbox"> Master the Product Rule \\((uv)' = u'v + uv'\\).</label></li>
        <li><label><input type="checkbox"> Master the Quotient Rule \\(\\left(\\frac{u}{v}\\right)' = \\frac{vu' - uv'}{v^2}\\).</label></li>
        <li><label><input type="checkbox"> Apply the Chain Rule to composite functions.</label></li>
        <li><label><input type="checkbox"> Differentiate exponential (\\(e^{kx}\\)) and logarithmic (\\(\\ln u\\)) functions.</label></li>
      </ul>
    </div>
    <div class="checklist-card">
      <h4>Problem Solving Milestones</h4>
      <ul>
        <li><label><input type="checkbox"> Differentiated combined product-chain functions and factored completely.</label></li>
        <li><label><input type="checkbox"> Computed second-order derivatives \\(\\frac{d^2 y}{dx^2}\\).</label></li>
        <li><label><input type="checkbox"> Performed logarithmic differentiation on variable exponent functions \\(u(x)^{v(x)}\\).</label></li>
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
    <h4>Problem 1 (Quotient Rule on Linear Fractional Model)</h4>
    <p>Find the derivative of \\(f(x) = \\frac{ax + b}{cx + d}\\) with respect to \\(x\\), where \\(a, b, c, d\\) are constants.</p>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        \\[ f'(x) = \\frac{(cx + d) \\frac{d}{dx}(ax + b) - (ax + b) \\frac{d}{dx}(cx + d)}{(cx + d)^2} \\]
        \\[ = \\frac{(cx + d)(a) - (ax + b)(c)}{(cx + d)^2} = \\frac{acx + ad - acx - bc}{(cx + d)^2} = \\frac{ad - bc}{(cx + d)^2}. \\]
        <strong>Answer:</strong> \\(f'(x) = \\frac{ad - bc}{(cx + d)^2}\\).
        <em>Notice:</em> The numerator is exactly the determinant \\(\\begin{vmatrix} a & b \\\\ c & d \\end{vmatrix}\\).
      </div>
    </details>
  </div>

  <div class="problem-card">
    <h4>Problem 2 (Second-Order Derivative)</h4>
    <p>If \\(y = x^3 - 6x^2 + 9x + 15\\), find \\(\\frac{dy}{dx}\\) and \\(\\frac{d^2 y}{dx^2}\\). Find the points where \\(\\frac{dy}{dx} = 0\\) and determine the sign of \\(\\frac{d^2 y}{dx^2}\\) at those points.</p>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        \\[ \\frac{dy}{dx} = 3x^2 - 12x + 9 = 3(x^2 - 4x + 3) = 3(x - 1)(x - 3) \\]
        \\[ \\frac{d^2 y}{dx^2} = \\frac{d}{dx}(3x^2 - 12x + 9) = 6x - 12 \\]
        Setting \\(\\frac{dy}{dx} = 0\\) gives \\(x = 1\\) and \\(x = 3\\).
        <ul>
          <li>At \\(x = 1\\): \\(\\frac{d^2 y}{dx^2} = 6(1) - 12 = -6 < 0\\) (Local Maximum).</li>
          <li>At \\(x = 3\\): \\(\\frac{d^2 y}{dx^2} = 6(3) - 12 = 6 > 0\\) (Local Minimum).</li>
        </ul>
      </div>
    </details>
  </div>

  <div class="problem-card">
    <h4>Problem 3 (Logarithmic Differentiation)</h4>
    <p>Differentiate \\(y = x^{\\sqrt{x}}\\) with respect to \\(x\\) for \\(x > 0\\).</p>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        <p>Taking natural logarithm on both sides:</p>
        \\[ \\ln y = \\ln(x^{\\sqrt{x}}) = \\sqrt{x} \\ln x \\]
        Differentiating implicitly with respect to \\(x\\) using the Product Rule on the right:
        \\[ \\frac{1}{y} \\frac{dy}{dx} = \\sqrt{x} \\cdot \\frac{d}{dx}(\\ln x) + \\ln x \\cdot \\frac{d}{dx}(\\sqrt{x}) \\]
        \\[ = \\sqrt{x} \\left(\\frac{1}{x}\\right) + (\\ln x) \\left(\\frac{1}{2\\sqrt{x}}\\right) = \\frac{1}{\\sqrt{x}} + \\frac{\\ln x}{2\\sqrt{x}} = \\frac{2 + \\ln x}{2\\sqrt{x}} \\]
        Multiplying by \\(y\\):
        \\[ \\frac{dy}{dx} = y \\left( \\frac{2 + \\ln x}{2\\sqrt{x}} \\right) = x^{\\sqrt{x}} \\left( \\frac{2 + \\ln x}{2\\sqrt{x}} \\right). \\]
      </div>
    </details>
  </div>
`;

// 4. REVISION TAB
const revisionHtml = `
  <h2>Quick Revision & Formula Cheat Sheet</h2>
  <div class="revision-grid">
    <div class="revision-card">
      <h4>Core Derivative Formulas</h4>
      <ul>
        <li>\\((x^n)' = n x^{n-1}\\)</li>
        <li>\\((e^{kx})' = k e^{kx}\\)</li>
        <li>\\((\\ln x)' = \\frac{1}{x}\\)</li>
        <li>\\((a^x)' = a^x \\ln a\\)</li>
      </ul>
    </div>
    <div class="revision-card">
      <h4>Combination Rules</h4>
      <ul>
        <li><strong>Product:</strong> \\((uv)' = u'v + uv'\\)</li>
        <li><strong>Quotient:</strong> \\((u/v)' = \\frac{vu' - uv'}{v^2}\\)</li>
        <li><strong>Chain:</strong> \\(\\frac{dy}{dx} = \\frac{dy}{du} \\cdot \\frac{du}{dx}\\)</li>
        <li><strong>Power Chain:</strong> \\(([u(x)]^n)' = n [u(x)]^{n-1} u'(x)\\)</li>
      </ul>
    </div>
    <div class="revision-card">
      <h4>Second Order Tests</h4>
      <ul>
        <li>\\(f''(x) > 0 \\implies\\) Concave upward (local minimum)</li>
        <li>\\(f''(x) < 0 \\implies\\) Concave downward (local maximum)</li>
        <li>\\(f''(x) = 0\\) with sign change \\(\\implies\\) Point of inflection</li>
      </ul>
    </div>
  </div>
`;

// 5. MOCK EXAM TAB
const mockHtml = `
  <h2>10-Question Diagnostic Mock Exam</h2>
  <p class="lead-p">Test your mastery of Differentiation Rules, Chain Rule, and Logarithmic Derivatives under timed CBSE conditions.</p>
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
    question: "What is the derivative of \\(f(x) = (2x - 5)^4\\)?",
    options: ["\\(4(2x - 5)^3\\)", "\\(8(2x - 5)^3\\)", "\\(2(2x - 5)^3\\)", "\\(8(2x - 5)^4\\)"],
    correct: 1,
    explanation: "By the Chain Rule: \\(4(2x - 5)^3 \\times \\frac{d}{dx}(2x - 5) = 4(2x - 5)^3 \\times 2 = 8(2x - 5)^3\\)."
  },
  {
    id: 2,
    question: "If \\(y = x^2 e^x\\), what is \\(\\frac{dy}{dx}\\)?",
    options: ["\\(2x e^x\\)", "\\(x^2 e^x\\)", "\\(e^x(x^2 + 2x)\\)", "\\(2x + e^x\\)"],
    correct: 2,
    explanation: "By Product Rule: \\(x^2(e^x) + e^x(2x) = e^x(x^2 + 2x)\\)."
  },
  {
    id: 3,
    question: "What is the derivative of \\(y = \\frac{x - 1}{x + 1}\\)?",
    options: ["\\(\\frac{2}{(x+1)^2}\\)", "\\(\\frac{-2}{(x+1)^2}\\)", "\\(\\frac{2x}{(x+1)^2}\\)", "1"],
    correct: 0,
    explanation: "By Quotient Rule: \\(\\frac{(x+1)(1) - (x-1)(1)}{(x+1)^2} = \\frac{x + 1 - x + 1}{(x+1)^2} = \\frac{2}{(x+1)^2}\\)."
  },
  {
    id: 4,
    question: "What is the derivative of \\(y = \\ln(3x^2 + 5)\\)?",
    options: ["\\(\\frac{1}{3x^2 + 5}\\)", "\\(\\frac{6x}{3x^2 + 5}\\)", "\\(\\frac{3x}{3x^2 + 5}\\)", "\\(6x\\ln(3x^2 + 5)\\)"],
    correct: 1,
    explanation: "By Chain Rule: \\(\\frac{1}{3x^2 + 5} \\times \\frac{d}{dx}(3x^2 + 5) = \\frac{6x}{3x^2 + 5}\\)."
  },
  {
    id: 5,
    question: "If \\(y = 2^x\\), what is \\(\\frac{dy}{dx}\\)?",
    options: ["\\(x 2^{x-1}\\)", "\\(2^x\\)", "\\(2^x \\ln 2\\)", "\\(\\frac{2^x}{\\ln 2}\\)"],
    correct: 2,
    explanation: "By formula \\(\\frac{d}{dx}(a^x) = a^x \\ln a\\), so \\(\\frac{d}{dx}(2^x) = 2^x \\ln 2\\)."
  },
  {
    id: 6,
    question: "If \\(y = x^4 - 2x^3 + 5x\\), what is the second derivative \\(\\frac{d^2 y}{dx^2}\\)?",
    options: ["\\(4x^3 - 6x^2 + 5\\)", "\\(12x^2 - 12x\\)", "\\(12x^2 - 12x + 5\\)", "\\(24x - 12\\)"],
    correct: 1,
    explanation: "\\(y' = 4x^3 - 6x^2 + 5\\). \\(y'' = 12x^2 - 12x\\)."
  },
  {
    id: 7,
    question: "What is the derivative of \\(f(x) = \\sqrt{x^2 + 9}\\)?",
    options: ["\\(\\frac{1}{2\\sqrt{x^2+9}}\\)", "\\(\\frac{x}{\\sqrt{x^2+9}}\\)", "\\(\\frac{2x}{\\sqrt{x^2+9}}\\)", "\\(x\\sqrt{x^2+9}\\)"],
    correct: 1,
    explanation: "\\(\\frac{d}{dx}(x^2 + 9)^{1/2} = \\frac{1}{2}(x^2 + 9)^{-1/2}(2x) = \\frac{x}{\\sqrt{x^2 + 9}}\\)."
  },
  {
    id: 8,
    question: "If \\(y = e^{-3x}\\), what is \\(\\frac{d^2 y}{dx^2}\\)?",
    options: ["\\(-3e^{-3x}\\)", "\\(3e^{-3x}\\)", "\\(9e^{-3x}\\)", "\\(-9e^{-3x}\\)"],
    correct: 2,
    explanation: "\\(y' = -3e^{-3x}\\). \\(y'' = -3(-3e^{-3x}) = 9e^{-3x}\\)."
  },
  {
    id: 9,
    question: "If \\(f(x) = x \\ln x\\), what is \\(f'(e)\\)?",
    options: ["1", "2", "\\(e\\)", "\\(1 + e\\)"],
    correct: 1,
    explanation: "\\(f'(x) = x(1/x) + \\ln x = 1 + \\ln x\\). At \\(x = e\\), \\(f'(e) = 1 + \\ln e = 1 + 1 = 2\\)."
  },
  {
    id: 10,
    question: "What is the derivative of \\(y = \\frac{1}{2x + 1}\\)?",
    options: ["\\(\\frac{2}{(2x+1)^2}\\)", "\\(-\\frac{2}{(2x+1)^2}\\)", "\\(-\\frac{1}{(2x+1)^2}\\)", "\\(\\frac{1}{2}\\)"],
    correct: 1,
    explanation: "\\(y = (2x + 1)^{-1} \\implies y' = -(2x + 1)^{-2}(2) = -\\frac{2}{(2x + 1)^2}\\)."
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
    resultsBox.innerHTML += '<p style="color:#059669; font-weight:600;">Outstanding! Flawless mastery of differentiation rules, chain rule, and quotients.</p>';
  } else if (pct >= 50) {
    resultsBox.innerHTML += '<p style="color:#d97706; font-weight:600;">Good effort! Review quotient rule signs and chain rule factors.</p>';
  } else {
    resultsBox.innerHTML += '<p style="color:#dc2626; font-weight:600;">Needs revision. Study the worked examples on product, quotient, and chain rules.</p>';
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
console.log('Successfully upgraded 7-4-rules-and-formulas-of-differentiation/index.html');
