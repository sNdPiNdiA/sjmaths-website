const fs = require('fs');
const cheerio = require('cheerio');

const filePath = 'class-11-applied-mathematics/chapter-7-calculus/7-3-differentiation/index.html';
const html = fs.readFileSync(filePath, 'utf8');
const $ = cheerio.load(html);

// 1. LEARN TAB
const learnHtml = `
  <h2>7.3 Differentiation: First Principles, Geometric Slopes, and Rates of Change</h2>
  <p class="lead-p">
    In Applied Mathematics, corporate financial modeling, and engineering dynamics, the <strong>derivative</strong> quantifies instantaneous sensitivity: how rapidly an output metric (revenue, cost, production volume) responds to an infinitesimal change in an input variable. Geometrically, it defines the exact slope of the tangent line to a curve.
  </p>

  <div class="formula-box">
    <h3>Mathematical Definition & The First Principle (Delta Method)</h3>
    <ul>
      <li><strong>Definition of Derivative:</strong> Let \\(f(x)\\) be a real-valued function defined on an open interval. The derivative of \\(f\\) at \\(x\\), denoted by \\(f'(x)\\) or \\(\\frac{df}{dx}\\), is defined as the limit:
        \\[ f'(x) = \\lim_{h \\to 0} \\frac{f(x + h) - f(x)}{h} \\]
        provided this limit exists finitely.
      </li>
      <li><strong>Derivative at a Specific Point \\(x = c\\):</strong>
        \\[ f'(c) = \\lim_{h \\to 0} \\frac{f(c + h) - f(c)}{h} = \\lim_{x \\to c} \\frac{f(x) - f(c)}{x - c} \\]
      </li>
      <li><strong>Geometric Interpretation:</strong>
        The difference quotient \\(\\frac{f(x + h) - f(x)}{h}\\) represents the slope of the <strong>secant line</strong> connecting points \\(P(x, f(x))\\) and \\(Q(x + h, f(x + h))\\).
        As \\(h \\to 0\\), point \\(Q\\) travels along the curve toward \\(P\\), and the secant line approaches the <strong>tangent line</strong> at \\(P\\).
        \\[ \\text{Slope of Tangent at } (x_0, y_0) = m = f'(x_0) = \\left. \\frac{dy}{dx} \\right|_{x = x_0} \\]
      </li>
      <li><strong>One-Sided Derivatives (Differentiability Test):</strong>
        A function is differentiable at \\(x = c\\) if and only if its Left-Hand Derivative (LHD) equals its Right-Hand Derivative (RHD):
        \\[ \\text{LHD} = f'(c^-) = \\lim_{h \\to 0^+} \\frac{f(c - h) - f(c)}{-h} \\]
        \\[ \\text{RHD} = f'(c^+) = \\lim_{h \\to 0^+} \\frac{f(c + h) - f(c)}{h} \\]
        \\[ f \\text{ is differentiable at } c \\iff \\text{LHD} = \\text{RHD} \\]
      </li>
      <li><strong>The Fundamental Differentiability-Continuity Theorem:</strong>
        \\[ \\textbf{Differentiability} \\implies \\textbf{Continuity} \\]
        If \\(f(x)\\) is differentiable at \\(x = c\\), then it is necessarily continuous at \\(x = c\\).
        <em>Caution:</em> The converse is FALSE. Continuity does not guarantee differentiability.
      </li>
    </ul>
  </div>

  <h3>Standard First Principles Derivations (CBSE Delta Method)</h3>
  <table class="table-styled">
    <thead>
      <tr>
        <th>Function \\(f(x)\\)</th>
        <th>Algebraic Step via First Principle</th>
        <th>Derivative \\(f'(x)\\)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Constant \\(f(x) = c\\)</strong></td>
        <td>\\(\\lim_{h \\to 0} \\frac{c - c}{h} = \\lim_{h \\to 0} 0\\)</td>
        <td>\\(0\\)</td>
      </tr>
      <tr>
        <td><strong>Power \\(f(x) = x^n\\)</strong></td>
        <td>Binomial expansion of \\((x + h)^n = x^n + n x^{n-1}h + \\dots\\)</td>
        <td>\\(n x^{n-1}\\)</td>
      </tr>
      <tr>
        <td><strong>Square Root \\(f(x) = \\sqrt{x}\\)</strong></td>
        <td>Rationalize: \\(\\frac{\\sqrt{x+h} - \\sqrt{x}}{h} \\times \\frac{\\sqrt{x+h} + \\sqrt{x}}{\\sqrt{x+h} + \\sqrt{x}}\\)</td>
        <td>\\(\\frac{1}{2\\sqrt{x}}\\)</td>
      </tr>
      <tr>
        <td><strong>Reciprocal \\(f(x) = \\frac{1}{x}\\)</strong></td>
        <td>Common denominator: \\(\\frac{x - (x+h)}{h x (x+h)} = \\frac{-1}{x(x+h)}\\)</td>
        <td>\\(-\\frac{1}{x^2}\\)</td>
      </tr>
    </tbody>
  </table>

  <div class="worked-example">
    <h4>Classic Example: The Non-Differentiable Continuous Function</h4>
    <p><strong>Problem:</strong> Show that \\(f(x) = |x|\\) is continuous at \\(x = 0\\), but not differentiable at \\(x = 0\\).</p>
    <div class="solution">
      <p><strong>Part 1: Proof of Continuity:</strong></p>
      <ul>
        <li>\\(f(0) = |0| = 0\\)</li>
        <li>\\(\\lim_{x \\to 0^-} |x| = \\lim_{x \\to 0^-} (-x) = 0\\)</li>
        <li>\\(\\lim_{x \\to 0^+} |x| = \\lim_{x \\to 0^+} (x) = 0\\)</li>
      </ul>
      Since \\(\\text{LHL} = \\text{RHL} = f(0) = 0\\), \\(f(x)\\) is continuous at \\(x = 0\\).

      <p><strong>Part 2: Test of Differentiability at \\(x = 0\\):</strong></p>
      <ul>
        <li>Left-Hand Derivative (LHD):
          \\[ \\text{LHD} = \\lim_{h \\to 0^+} \\frac{f(0 - h) - f(0)}{-h} = \\lim_{h \\to 0^+} \\frac{|-h| - 0}{-h} = \\lim_{h \\to 0^+} \\frac{h}{-h} = -1. \\]
        </li>
        <li>Right-Hand Derivative (RHD):
          \\[ \\text{RHD} = \\lim_{h \\to 0^+} \\frac{f(0 + h) - f(0)}{h} = \\lim_{h \\to 0^+} \\frac{|h| - 0}{h} = \\lim_{h \\to 0^+} \\frac{h}{h} = 1. \\]
        </li>
      </ul>
      <p>Since \\(\\text{LHD} = -1 \\neq 1 = \\text{RHD}\\), the derivative at \\(x = 0\\) does not exist.</p>
      <p><em>Geometric Meaning:</em> The curve has a sharp corner (v-notch) at the origin with no unique tangent slope.</p>
    </div>
  </div>
`;

// 2. PROGRESS TAB
const progressHtml = `
  <h2>Progress Tracker & Self-Assessment Checklist</h2>
  <p>Track your conceptual mastery and computational proficiency across Differentiation from First Principles.</p>
  <div class="checklist-grid">
    <div class="checklist-card">
      <h4>Conceptual Milestones</h4>
      <ul>
        <li><label><input type="checkbox"> Define the derivative as the limit of the difference quotient \\(\\lim_{h \\to 0} \\frac{f(x+h)-f(x)}{h}\\).</label></li>
        <li><label><input type="checkbox"> Interpret the derivative geometrically as the slope of the tangent line.</label></li>
        <li><label><input type="checkbox"> Distinguish between average rate of change and instantaneous rate of change.</label></li>
        <li><label><input type="checkbox"> Prove that differentiability implies continuity, but continuity does not imply differentiability.</label></li>
      </ul>
    </div>
    <div class="checklist-card">
      <h4>Problem Solving Milestones</h4>
      <ul>
        <li><label><input type="checkbox"> Differentiated polynomial functions from first principles.</label></li>
        <li><label><input type="checkbox"> Differentiated radical functions (e.g. \\(\\sqrt{2x+3}\\)) via conjugate rationalization.</label></li>
        <li><label><input type="checkbox"> Evaluated LHD and RHD at corner/piecewise junction points.</label></li>
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
    <h4>Problem 1 (First Principles: Radical Function)</h4>
    <p>Find the derivative of \\(f(x) = \\sqrt{2x + 1}\\) from first principles.</p>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        \\[ f'(x) = \\lim_{h \\to 0} \\frac{f(x + h) - f(x)}{h} = \\lim_{h \\to 0} \\frac{\\sqrt{2(x + h) + 1} - \\sqrt{2x + 1}}{h} \\]
        Multiply numerator and denominator by the conjugate \\(\\sqrt{2x + 2h + 1} + \\sqrt{2x + 1}\\):
        \\[ = \\lim_{h \\to 0} \\frac{(2x + 2h + 1) - (2x + 1)}{h (\\sqrt{2x + 2h + 1} + \\sqrt{2x + 1})} \\]
        \\[ = \\lim_{h \\to 0} \\frac{2h}{h (\\sqrt{2x + 2h + 1} + \\sqrt{2x + 1})} \\]
        Cancel the non-zero \\(h\\):
        \\[ = \\lim_{h \\to 0} \\frac{2}{\\sqrt{2x + 2h + 1} + \\sqrt{2x + 1}} = \\frac{2}{2\\sqrt{2x + 1}} = \\frac{1}{\\sqrt{2x + 1}}. \\]
        <strong>Answer:</strong> \\(f'(x) = \\frac{1}{\\sqrt{2x + 1}}\\).
      </div>
    </details>
  </div>

  <div class="problem-card">
    <h4>Problem 2 (Instantaneous Speed vs Average Speed)</h4>
    <p>A delivery vehicle's displacement in kilometers after \\(t\\) hours is given by \\(s(t) = 40t + 5t^2\\).</p>
    <ol type="a">
      <li>Find the average speed of the vehicle between \\(t = 2\\) and \\(t = 4\\) hours.</li>
      <li>Find the instantaneous speed at exactly \\(t = 3\\) hours using differentiation.</li>
    </ol>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        <p><strong>Part (a): Average Speed:</strong></p>
        \\[ s(2) = 40(2) + 5(2^2) = 80 + 20 = 100 \\text{ km} \\]
        \\[ s(4) = 40(4) + 5(4^2) = 160 + 80 = 240 \\text{ km} \\]
        \\[ v_{\\text{avg}} = \\frac{s(4) - s(2)}{4 - 2} = \\frac{240 - 100}{2} = \\frac{140}{2} = 70 \\text{ km/h.} \\]
        <p><strong>Part (b): Instantaneous Speed at \\(t = 3\\):</strong></p>
        \\[ v(t) = s'(t) = \\frac{d}{dt}(40t + 5t^2) = 40 + 10t \\]
        \\[ v(3) = 40 + 10(3) = 40 + 30 = 70 \\text{ km/h.} \\]
      </div>
    </details>
  </div>

  <div class="problem-card">
    <h4>Problem 3 (Slope of Tangent to a Cost Curve)</h4>
    <p>A firm's total production cost is modeled by \\(C(x) = 2x^2 + 15x + 50\\), where \\(x\\) is units produced. Find the slope of the cost curve when 10 units are produced.</p>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        <p>The slope of the curve at any output \\(x\\) is given by the derivative \\(C'(x)\\):</p>
        \\[ C'(x) = \\frac{d}{dx}(2x^2 + 15x + 50) = 4x + 15 \\]
        At \\(x = 10\\):
        \\[ C'(10) = 4(10) + 15 = 40 + 15 = 55. \\]
        <strong>Answer:</strong> The slope of the tangent line is <strong>55</strong> (representing marginal cost ₹55/unit).
      </div>
    </details>
  </div>
`;

// 4. REVISION TAB
const revisionHtml = `
  <h2>Quick Revision & Formula Cheat Sheet</h2>
  <div class="revision-grid">
    <div class="revision-card">
      <h4>First Principle Definition</h4>
      <ul>
        <li>\\(f'(x) = \\lim_{h \\to 0} \\frac{f(x + h) - f(x)}{h}\\)</li>
        <li>\\(f'(c) = \\lim_{x \\to c} \\frac{f(x) - f(c)}{x - c}\\)</li>
        <li>Geometrically: Slope of tangent \\(m = f'(x_0)\\)</li>
        <li>Physically: Instantaneous rate of change</li>
      </ul>
    </div>
    <div class="revision-card">
      <h4>Standard First Principle Derivatives</h4>
      <ul>
        <li>\\(\\frac{d}{dx}(c) = 0\\)</li>
        <li>\\(\\frac{d}{dx}(x^n) = n x^{n-1}\\)</li>
        <li>\\(\\frac{d}{dx}(\\sqrt{x}) = \\frac{1}{2\\sqrt{x}}\\)</li>
        <li>\\(\\frac{d}{dx}\\left(\\frac{1}{x}\\right) = -\\frac{1}{x^2}\\)</li>
      </ul>
    </div>
    <div class="revision-card">
      <h4>Differentiability Core Facts</h4>
      <ul>
        <li>Differentiable \\(\\implies\\) Continuous</li>
        <li>Continuous does NOT imply Differentiable</li>
        <li>Sharp corners, vertical tangents, and breaks lack derivatives</li>
        <li>Differentiable \\(\\iff \\text{LHD} = \\text{RHD}\\)</li>
      </ul>
    </div>
  </div>
`;

// 5. MOCK EXAM TAB
const mockHtml = `
  <h2>10-Question Diagnostic Mock Exam</h2>
  <p class="lead-p">Test your mastery of Differentiation from First Principles and Geometric Slopes under timed CBSE conditions.</p>
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
    question: "What is the derivative of \\(f(x) = x^3\\) from first principles?",
    options: ["\\(x^2\\)", "\\(2x^2\\)", "\\(3x^2\\)", "\\(3x^3\\)"],
    correct: 2,
    explanation: "\\(\\lim_{h \\to 0} \\frac{(x+h)^3 - x^3}{h} = \\lim_{h \\to 0} (3x^2 + 3xh + h^2) = 3x^2\\)."
  },
  {
    id: 2,
    question: "Geometrically, the derivative \\(f'(a)\\) represents:",
    options: [
      "The area under the curve at \\(x = a\\)",
      "The slope of the tangent line to \\(y = f(x)\\) at \\(x = a\\)",
      "The length of the curve from 0 to \\(a\\)",
      "The secant line connecting \\((0, 0)\\) and \\((a, f(a))\\)"
    ],
    correct: 1,
    explanation: "The derivative \\(f'(a)\\) is the exact slope of the tangent line to the curve at the point \\((a, f(a))\\)."
  },
  {
    id: 3,
    question: "What is the slope of the tangent line to \\(y = 3x^2 - 5x + 2\\) at \\(x = 2\\)?",
    options: ["4", "7", "9", "12"],
    correct: 1,
    explanation: "\\(y' = 6x - 5\\). At \\(x = 2\\), \\(y'(2) = 6(2) - 5 = 12 - 5 = 7\\)."
  },
  {
    id: 4,
    question: "If a function \\(f(x)\\) is differentiable at \\(x = c\\), which of the following is necessarily true?",
    options: [
      "\\(f(x)\\) is continuous at \\(x = c\\)",
      "\\(f'(c) = 0\\)",
      "\\(f(x)\\) is a polynomial",
      "\\(f(c) = 0\\)"
    ],
    correct: 0,
    explanation: "Differentiability strictly implies continuity: every differentiable function is continuous."
  },
  {
    id: 5,
    question: "What is the derivative of \\(f(x) = \\frac{1}{x^2}\\) with respect to \\(x\\)?",
    options: ["\\(\\frac{1}{2x}\\)", "\\(-\\frac{2}{x^3}\\)", "\\(-\\frac{1}{x^3}\\)", "\\(\\frac{2}{x^3}\\)"],
    correct: 1,
    explanation: "\\(\\frac{d}{dx}(x^{-2}) = -2 x^{-2-1} = -2x^{-3} = -\\frac{2}{x^3}\\)."
  },
  {
    id: 6,
    question: "What is the Right-Hand Derivative of \\(f(x) = |x - 2|\\) at \\(x = 2\\)?",
    options: ["-1", "0", "1", "Does not exist"],
    correct: 2,
    explanation: "For \\(x > 2\\), \\(f(x) = x - 2\\). The right-hand slope is \\(\\lim_{h \\to 0^+} \\frac{(2+h-2) - 0}{h} = \\frac{h}{h} = 1\\)."
  },
  {
    id: 7,
    question: "What is the Left-Hand Derivative of \\(f(x) = |x - 2|\\) at \\(x = 2\\)?",
    options: ["-1", "0", "1", "Does not exist"],
    correct: 0,
    explanation: "For \\(x < 2\\), \\(f(x) = -(x - 2)\\). The left-hand slope is \\(\\lim_{h \\to 0^+} \\frac{-(2-h-2) - 0}{-h} = \\frac{h}{-h} = -1\\)."
  },
  {
    id: 8,
    question: "If \\(f(x) = c\\) (a constant function), what is \\(f'(x)\\)?",
    options: ["\\(c\\)", "1", "0", "Undefined"],
    correct: 2,
    explanation: "The derivative of any constant is zero because the rate of change of an unchanging value is 0."
  },
  {
    id: 9,
    question: "The displacement of a delivery drone is \\(s(t) = 3t^2 + 2t\\). What is its instantaneous velocity at \\(t = 4\\)?",
    options: ["24", "26", "28", "56"],
    correct: 1,
    explanation: "\\(v(t) = s'(t) = 6t + 2\\). At \\(t = 4\\), \\(v(4) = 6(4) + 2 = 24 + 2 = 26\\)."
  },
  {
    id: 10,
    question: "Why is the function \\(f(x) = |x|\\) not differentiable at \\(x = 0\\)?",
    options: [
      "Because \\(f(0)\\) is undefined",
      "Because the limit \\(\\lim_{x \\to 0} |x|\\) does not exist",
      "Because the left-hand derivative (-1) is not equal to the right-hand derivative (+1)",
      "Because \\(f(x)\\) is discontinuous at \\(x = 0\\)"
    ],
    correct: 2,
    explanation: "At \\(x = 0\\), LHD = -1 while RHD = +1. Since LHD \\(\\neq\\) RHD, the derivative does not exist."
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
    resultsBox.innerHTML += '<p style="color:#059669; font-weight:600;">Outstanding! Masterful command of differentiation from first principles and tangent slopes.</p>';
  } else if (pct >= 50) {
    resultsBox.innerHTML += '<p style="color:#d97706; font-weight:600;">Good effort! Review one-sided derivatives and the first principle delta method.</p>';
  } else {
    resultsBox.innerHTML += '<p style="color:#dc2626; font-weight:600;">Needs revision. Study the worked examples on difference quotients and try again.</p>';
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
console.log('Successfully upgraded 7-3-differentiation/index.html');
