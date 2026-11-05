const fs = require('fs');
const cheerio = require('cheerio');

const filePath = 'class-11-applied-mathematics/chapter-7-calculus/7-2-continuity/index.html';
const html = fs.readFileSync(filePath, 'utf8');
const $ = cheerio.load(html);

// 1. LEARN TAB
const learnHtml = `
  <h2>7.2 Continuity: The 3-Step Verification, Discontinuity Types, and Economic Thresholds</h2>
  <p class="lead-p">
    In Applied Mathematics and econometric modeling, a continuous function models smooth, unbroken processes—such as steady asset price trajectories, smooth cost curves, and uninterrupted compounding. Understanding <strong>continuity</strong> is the prerequisite for differentiation, because only continuous curves can possess defined tangent slopes.
  </p>

  <div class="formula-box">
    <h3>The 3 Fundamental Conditions of Continuity</h3>
    <p>A real-valued function \\(f(x)\\) is continuous at a point \\(x = c\\) in its domain <strong>if and only if</strong> all three conditions are satisfied:</p>
    <ol>
      <li><strong>Existence of Function Value:</strong> \\(f(c)\\) is defined (yields a finite real number).</li>
      <li><strong>Existence of Two-Sided Limit:</strong> The limit \\(\\lim_{x \\to c} f(x)\\) exists:
        \\[ \\lim_{x \\to c^-} f(x) = \\lim_{x \\to c^+} f(x) = L \\]
      </li>
      <li><strong>Equivalence of Limit and Value:</strong>
        \\[ \\lim_{x \\to c} f(x) = f(c) \\]
      </li>
    </ol>
    <p>In concise operator form: \\(\\text{LHL} = \\text{RHL} = f(c)\\).</p>
  </div>

  <h3>Taxonomy of Discontinuities</h3>
  <table class="table-styled">
    <thead>
      <tr>
        <th>Discontinuity Type</th>
        <th>Mathematical Criterion</th>
        <th>Visual / Graphical Behavior</th>
        <th>Real-World / Business Example</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Removable Discontinuity</strong></td>
        <td>\\(\\lim_{x \\to c} f(x)\\) exists, but \\(\\lim_{x \\to c} f(x) \\neq f(c)\\) (or \\(f(c)\\) is undefined)</td>
        <td>A single missing "hole" on an otherwise smooth curve</td>
        <td>An pricing formula undefined at exactly zero quantity due to \\(0/0\\) division</td>
      </tr>
      <tr>
        <td><strong>Jump (Step) Discontinuity</strong></td>
        <td>\\(\\text{LHL} \\neq \\text{RHL}\\) (both finite but unequal)</td>
        <td>The curve abruptly steps up or down to a different height</td>
        <td>Income tax slabs under non-marginal regimes, postal weight brackets, or parking fee hour blocks</td>
      </tr>
      <tr>
        <td><strong>Infinite Discontinuity</strong></td>
        <td>One or both one-sided limits approach \\(\\pm \\infty\\)</td>
        <td>Vertical asymptote</td>
        <td>Average fixed cost \\(AFC(x) = \\frac{FC}{x}\\) as output \\(x \\to 0^+\\)</td>
      </tr>
    </tbody>
  </table>

  <div class="worked-example">
    <h4>Comprehensive Exam Example: Determining Unknown Parameters for Continuity</h4>
    <p><strong>Problem:</strong> Determine the values of \\(a\\) and \\(b\\) such that the function \\(f(x)\\) defined by:
      \\[ f(x) = \\begin{cases} 5, & x \\le 2 \\\\ ax + b, & 2 < x < 10 \\\\ 21, & x \\ge 10 \\end{cases} \\]
      is continuous everywhere.
    </p>
    <div class="solution">
      <p><strong>Solution:</strong></p>
      <p>For \\(f(x)\\) to be continuous everywhere, it must be continuous at the transition points \\(x = 2\\) and \\(x = 10\\).</p>
      <p><strong>1. Continuity at \\(x = 2\\):</strong></p>
      <ul>
        <li>\\(\\text{LHL} = \\lim_{x \\to 2^-} f(x) = 5\\)</li>
        <li>\\(\\text{RHL} = \\lim_{x \\to 2^+} f(x) = \\lim_{x \\to 2^+} (ax + b) = 2a + b\\)</li>
        <li>\\(f(2) = 5\\)</li>
      </ul>
      For continuity at \\(x = 2\\):
      \\[ 2a + b = 5 \\quad \\text{--- (Equation 1)} \\]

      <p><strong>2. Continuity at \\(x = 10\\):</strong></p>
      <ul>
        <li>\\(\\text{LHL} = \\lim_{x \\to 10^-} f(x) = \\lim_{x \\to 10^-} (ax + b) = 10a + b\\)</li>
        <li>\\(\\text{RHL} = \\lim_{x \\to 10^+} f(x) = 21\\)</li>
        <li>\\(f(10) = 21\\)</li>
      </ul>
      For continuity at \\(x = 10\\):
      \\[ 10a + b = 21 \\quad \\text{--- (Equation 2)} \\]

      <p><strong>3. Solving the Linear System:</strong></p>
      Subtract Equation (1) from Equation (2):
      \\[ (10a + b) - (2a + b) = 21 - 5 \\implies 8a = 16 \\implies a = 2 \\]
      Substitute \\(a = 2\\) into Equation (1):
      \\[ 2(2) + b = 5 \\implies 4 + b = 5 \\implies b = 1 \\]
      <strong>Answer:</strong> \\(a = 2\\) and \\(b = 1\\).
    </div>
  </div>
`;

// 2. PROGRESS TAB
const progressHtml = `
  <h2>Progress Tracker & Self-Assessment Checklist</h2>
  <p>Track your conceptual mastery and diagnostic skills across Continuity and Parameter Determinations.</p>
  <div class="checklist-grid">
    <div class="checklist-card">
      <h4>Conceptual Milestones</h4>
      <ul>
        <li><label><input type="checkbox"> Verify continuity at a point using the 3-step test: \\(\\text{LHL} = \\text{RHL} = f(c)\\).</label></li>
        <li><label><input type="checkbox"> Classify discontinuities into Removable, Jump, and Infinite.</label></li>
        <li><label><input type="checkbox"> State the continuity properties of polynomials, rational functions, and modulus functions.</label></li>
        <li><label><input type="checkbox"> Understand why continuity is a necessary (but not sufficient) condition for differentiability.</label></li>
      </ul>
    </div>
    <div class="checklist-card">
      <h4>Problem Solving Milestones</h4>
      <ul>
        <li><label><input type="checkbox"> Solved single-parameter continuity problems (finding \\(k\\)).</label></li>
        <li><label><input type="checkbox"> Solved dual-parameter simultaneous systems (finding \\(a\\) and \\(b\\)).</label></li>
        <li><label><input type="checkbox"> Analyzed economic tariff and tax functions for step discontinuities.</label></li>
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
    <h4>Problem 1 (Finding Constant \\(k\\) for Continuity)</h4>
    <p>Find the value of \\(k\\) so that the function \\(f(x)\\) is continuous at \\(x = 0\\):
      \\[ f(x) = \\begin{cases} \\displaystyle \\frac{\\sqrt{1 + kx} - \\sqrt{1 - kx}}{x}, & \\text{if } -1 \\le x < 0 \\\\[10pt] \\displaystyle \\frac{2x + 1}{x - 1}, & \\text{if } 0 \\le x \\le 1 \\end{cases} \\]
    </p>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        <p>At \\(x = 0\\), \\(f(0) = \\frac{2(0) + 1}{0 - 1} = \\frac{1}{-1} = -1\\).</p>
        <p>Evaluate Left-Hand Limit (LHL) by rationalizing:</p>
        \\[ \\text{LHL} = \\lim_{x \\to 0^-} \\frac{\\sqrt{1 + kx} - \\sqrt{1 - kx}}{x} = \\lim_{x \\to 0^-} \\frac{(1 + kx) - (1 - kx)}{x(\\sqrt{1 + kx} + \\sqrt{1 - kx})} \\]
        \\[ = \\lim_{x \\to 0^-} \\frac{2kx}{x(\\sqrt{1 + kx} + \\sqrt{1 - kx})} = \\frac{2k}{\\sqrt{1} + \\sqrt{1}} = \\frac{2k}{2} = k. \\]
        <p>For \\(f(x)\\) to be continuous at \\(x = 0\\), we must have \\(\\text{LHL} = f(0)\\):</p>
        \\[ k = -1. \\]
        <strong>Answer:</strong> \\(k = -1\\).
      </div>
    </details>
  </div>

  <div class="problem-card">
    <h4>Problem 2 (Greatest Integer Function Discontinuity)</h4>
    <p>Prove that the greatest integer function \\(f(x) = [x]\\) is discontinuous at all integral points.</p>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        <p>Let \\(c\\) be any integer (\\(c \\in \\mathbb{Z}\\)).</p>
        <ul>
          <li>\\(f(c) = [c] = c\\).</li>
          <li>For \\(x \\to c^-\\), \\(x\\) lies strictly between \\(c - 1\\) and \\(c\\) (e.g. \\(c - 0.001\\)).
            Hence \\([x] = c - 1\\).
            \\[ \\text{LHL} = \\lim_{x \\to c^-} [x] = c - 1. \\]
          </li>
          <li>For \\(x \\to c^+\\), \\(x\\) lies strictly between \\(c\\) and \\(c + 1\\) (e.g. \\(c + 0.001\\)).
            Hence \\([x] = c\\).
            \\[ \\text{RHL} = \\lim_{x \\to c^+} [x] = c. \\]
          </li>
        </ul>
        <p>Since \\(\\text{LHL} = c - 1 \\neq c = \\text{RHL}\\), the limit \\(\\lim_{x \\to c} [x]\\) does not exist at any integer \\(c\\).
        Therefore, \\(f(x) = [x]\\) has a jump discontinuity of size 1 at every integer point.</p>
      </div>
    </details>
  </div>

  <div class="problem-card">
    <h4>Problem 3 (Modulus Function Continuity)</h4>
    <p>Examine the continuity of \\(f(x) = |x - 3|\\) at \\(x = 3\\).</p>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        <p>By definition of absolute value:</p>
        \\[ f(x) = \\begin{cases} -(x - 3) = 3 - x, & x < 3 \\\\ x - 3, & x \\ge 3 \\end{cases} \\]
        <ul>
          <li>\\(f(3) = 3 - 3 = 0\\).</li>
          <li>\\(\\text{LHL} = \\lim_{x \\to 3^-} (3 - x) = 3 - 3 = 0\\).</li>
          <li>\\(\\text{RHL} = \\lim_{x \\to 3^+} (x - 3) = 3 - 3 = 0\\).</li>
        </ul>
        <p>Since \\(\\text{LHL} = \\text{RHL} = f(3) = 0\\), \\(f(x)\\) is <strong>continuous at \\(x = 3\\)</strong>.</p>
      </div>
    </details>
  </div>
`;

// 4. REVISION TAB
const revisionHtml = `
  <h2>Quick Revision & Formula Cheat Sheet</h2>
  <div class="revision-grid">
    <div class="revision-card">
      <h4>3-Step Continuity Test</h4>
      <ul>
        <li>1. \\(f(c)\\) is defined</li>
        <li>2. \\(\\lim_{x \\to c^-} f(x) = \\lim_{x \\to c^+} f(x) = L\\)</li>
        <li>3. \\(L = f(c)\\)</li>
        <li>If any condition fails, \\(f\\) is discontinuous</li>
      </ul>
    </div>
    <div class="revision-card">
      <h4>Standard Continuous Functions</h4>
      <ul>
        <li>Every polynomial function is continuous everywhere on \\(\\mathbb{R}\\)</li>
        <li>Every rational function is continuous on its entire domain</li>
        <li>The modulus function \\(|x - a|\\) is continuous everywhere</li>
      </ul>
    </div>
    <div class="revision-card">
      <h4>Discontinuity Types</h4>
      <ul>
        <li><strong>Removable:</strong> Hole in graph; limit exists</li>
        <li><strong>Jump:</strong> Step in graph; \\(\\text{LHL} \\neq \\text{RHL}\\)</li>
        <li><strong>Infinite:</strong> Asymptotic curve; limits are \\(\\pm \\infty\\)</li>
      </ul>
    </div>
  </div>
`;

// 5. MOCK EXAM TAB
const mockHtml = `
  <h2>10-Question Diagnostic Mock Exam</h2>
  <p class="lead-p">Test your mastery of Continuity, Discontinuity Types, and Parameter Solving under timed CBSE conditions.</p>
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
    question: "If \\(f(x) = \\begin{cases} kx + 1, & x \\le 5 \\\\ 3x - 5, & x > 5 \\end{cases}\\) is continuous at \\(x = 5\\), what is the value of \\(k\\)?",
    options: ["1", "\\(\\frac{9}{5}\\)", "2", "\\(\\frac{11}{5}\\)"],
    correct: 1,
    explanation: "\\(\\text{LHL} = f(5) = 5k + 1\\). \\(\\text{RHL} = 3(5) - 5 = 10\\). Setting \\(5k + 1 = 10 \\implies 5k = 9 \\implies k = 9/5\\)."
  },
  {
    id: 2,
    question: "The function \\(f(x) = \\frac{x^2 - 16}{x - 4}\\) is undefined at \\(x = 4\\). What value must be assigned to \\(f(4)\\) to make \\(f\\) continuous at \\(x = 4\\)?",
    options: ["0", "4", "8", "16"],
    correct: 2,
    explanation: "\\(\\lim_{x \\to 4} \\frac{(x-4)(x+4)}{x-4} = 4 + 4 = 8\\). For continuity, \\(f(4)\\) must equal the limit, so \\(f(4) = 8\\)."
  },
  {
    id: 3,
    question: "At which points is the rational function \\(f(x) = \\frac{x + 2}{x^2 - 5x + 6}\\) discontinuous?",
    options: ["\\(x = -2\\)", "\\(x = 2\\) and \\(x = 3\\)", "\\(x = -2, 2, 3\\)", "\\(x = 5\\) and \\(x = 6\\)"],
    correct: 1,
    explanation: "Discontinuities occur where denominator vanishes: \\(x^2 - 5x + 6 = (x - 2)(x - 3) = 0 \\implies x = 2, 3\\)."
  },
  {
    id: 4,
    question: "The modulus function \\(f(x) = |x|\\) is:",
    options: [
      "Continuous and differentiable everywhere",
      "Continuous everywhere, but not differentiable at \\(x = 0\\)",
      "Discontinuous at \\(x = 0\\)",
      "Neither continuous nor differentiable at \\(x = 0\\)"
    ],
    correct: 1,
    explanation: "\\(f(x) = |x|\\) is continuous everywhere on \\(\\mathbb{R}\\), but has a sharp corner (cusp) at \\(x = 0\\) making it non-differentiable there."
  },
  {
    id: 5,
    question: "If \\(f(x) = \\begin{cases} \\frac{\\sin x}{x}, & x \\neq 0 \\\\ 1, & x = 0 \\end{cases}\\), then \\(f(x)\\) at \\(x = 0\\) is:",
    options: ["Continuous", "Has a jump discontinuity", "Has an infinite discontinuity", "Undefined"],
    correct: 0,
    explanation: "\\(\\lim_{x \\to 0} \\frac{\\sin x}{x} = 1 = f(0)\\), so \\(f(x)\\) is continuous at \\(x = 0\\)."
  },
  {
    id: 6,
    question: "What type of discontinuity does \\(f(x) = [x]\\) (the greatest integer function) exhibit at \\(x = 3\\)?",
    options: ["Removable discontinuity", "Jump discontinuity", "Infinite discontinuity", "It is continuous"],
    correct: 1,
    explanation: "\\(\\text{LHL} = 2\\) and \\(\\text{RHL} = 3\\). Because the left and right limits are finite but unequal, it is a jump discontinuity."
  },
  {
    id: 7,
    question: "If \\(f(x) = \\begin{cases} x^2 + 1, & x < 1 \\\\ 3, & x = 1 \\\\ 2x, & x > 1 \\end{cases}\\), which condition of continuity fails at \\(x = 1\\)?",
    options: [
      "\\(f(1)\\) is undefined",
      "\\(\\lim_{x \\to 1} f(x)\\) does not exist",
      "\\(\\lim_{x \\to 1} f(x) \\neq f(1)\\)",
      "No condition fails; it is continuous"
    ],
    correct: 2,
    explanation: "\\(\\text{LHL} = 1^2 + 1 = 2\\), \\(\\text{RHL} = 2(1) = 2\\). So \\(\\lim_{x \\to 1} f(x) = 2\\). But \\(f(1) = 3 \\neq 2\\). Condition 3 fails (removable discontinuity)."
  },
  {
    id: 8,
    question: "Every polynomial function of degree \\(n \\ge 0\\) is continuous:",
    options: [
      "Only for \\(x > 0\\)",
      "Only on closed intervals",
      "Everywhere on \\(\\mathbb{R}\\)",
      "At all points except roots"
    ],
    correct: 2,
    explanation: "By the fundamental theorem of continuous functions, every polynomial function is continuous everywhere on the real line \\(\\mathbb{R}\\)."
  },
  {
    id: 9,
    question: "If \\(f(x) = \\begin{cases} \\frac{x^2 - 1}{x - 1}, & x \\neq 1 \\\\ k, & x = 1 \\end{cases}\\) is continuous at \\(x = 1\\), what is \\(k\\)?",
    options: ["0", "1", "2", "4"],
    correct: 2,
    explanation: "\\(\\lim_{x \\to 1} \\frac{(x-1)(x+1)}{x-1} = 1 + 1 = 2\\). Thus \\(k = 2\\)."
  },
  {
    id: 10,
    question: "If \\(f(x)\\) and \\(g(x)\\) are continuous at \\(x = c\\), then \\(\\frac{f(x)}{g(x)}\\) is continuous at \\(x = c\\) provided:",
    options: ["\\(f(c) \\neq 0\\)", "\\(g(c) \\neq 0\\)", "\\(f(c) = g(c)\\)", "\\(c > 0\\)"],
    correct: 1,
    explanation: "The quotient of two continuous functions is continuous at all points where the denominator is non-zero: \\(g(c) \\neq 0\\)."
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
    resultsBox.innerHTML += '<p style="color:#059669; font-weight:600;">Outstanding! Exceptional mastery of continuity proofs and piecewise parameters.</p>';
  } else if (pct >= 50) {
    resultsBox.innerHTML += '<p style="color:#d97706; font-weight:600;">Good effort! Review the 3 conditions of continuity and retry.</p>';
  } else {
    resultsBox.innerHTML += '<p style="color:#dc2626; font-weight:600;">Needs revision. Study the worked examples on solving for unknown constants.</p>';
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
console.log('Successfully upgraded 7-2-continuity/index.html');

