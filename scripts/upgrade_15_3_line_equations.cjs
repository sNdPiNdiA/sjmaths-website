const fs = require('fs');
const cheerio = require('cheerio');

const filePath = 'class-11-applied-mathematics/chapter-15-straight-lines/15-3-various-forms-of-equations-of-a-line/index.html';
const html = fs.readFileSync(filePath, 'utf8');
const $ = cheerio.load(html);

// 1. LEARN TAB
const learnHtml = `
  <h2>15.3 Various Forms of Equations of a Line: Point-Slope, Intercept, and Business Models</h2>
  <p class="lead-p">
    In Applied Mathematics, corporate budgeting, and econometric regression, straight lines are the primary mathematical instrument for modeling linear trends. From linear cost accounting ($C = mx + F$) to asset depreciation schedules and consumer demand relationships ($p = -mx + c$), mastering the various forms of straight line equations allows analysts to translate empirical data into predictive algebraic models.
  </p>

  <div class="formula-box">
    <h3>Master Formulary of Straight Line Equations</h3>
    <table class="table-styled">
      <thead>
        <tr>
          <th>Standard Form</th>
          <th>Given Geometric Parameters</th>
          <th>Algebraic Equation</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Horizontal Line</strong></td>
          <td>Parallel to \\(x\\)-axis at distance \\(b\\)</td>
          <td>\\[ y = b \\quad (\\text{or } y = -b) \\]</td>
        </tr>
        <tr>
          <td><strong>Vertical Line</strong></td>
          <td>Parallel to \\(y\\)-axis at distance \\(a\\)</td>
          <td>\\[ x = a \\quad (\\text{or } x = -a) \\]</td>
        </tr>
        <tr>
          <td><strong>Point-Slope Form</strong></td>
          <td>Passes through \\((x_0, y_0)\\) with slope \\(m\\)</td>
          <td>\\[ y - y_0 = m(x - x_0) \\]</td>
        </tr>
        <tr>
          <td><strong>Two-Point Form</strong></td>
          <td>Passes through \\((x_1, y_1)\\) and \\((x_2, y_2)\\)</td>
          <td>\\[ y - y_1 = \\frac{y_2 - y_1}{x_2 - x_1} (x - x_1) \\]</td>
        </tr>
        <tr>
          <td><strong>Slope-Intercept Form</strong></td>
          <td>Slope \\(m\\) and \\(y\\)-intercept \\(c\\)</td>
          <td>\\[ y = mx + c \\]</td>
        </tr>
        <tr>
          <td><strong>Intercept Form</strong></td>
          <td>\\(x\\)-intercept \\(a\\) and \\(y\\)-intercept \\(b\\)</td>
          <td>\\[ \\frac{x}{a} + \\frac{y}{b} = 1 \\]</td>
        </tr>
        <tr>
          <td><strong>General Form</strong></td>
          <td>Arbitrary linear coefficients \\(A, B, C\\)</td>
          <td>\\[ Ax + By + C = 0 \\implies m = -\\frac{A}{B}, \\, c = -\\frac{C}{B} \\]</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="worked-example">
    <h4>Comprehensive Applied Business Example: Linear Cost Accounting</h4>
    <p><strong>Scenario:</strong> A manufacturing firm incurs total production costs of ₹2,50,000 when manufacturing 500 units of a product, and ₹3,70,000 when manufacturing 800 units. Assuming a linear relationship exists between output \\(x\\) and total cost \\(C\\):</p>
    <ol>
      <li>Find the linear cost equation using the Two-Point Form.</li>
      <li>Identify the fixed overhead cost \\(F\\) and the marginal variable cost per unit \\(m\\).</li>
      <li>Forecast the total cost of producing 1,200 units.</li>
      <li>If the firm sells each unit for ₹500, determine the break-even production volume.</li>
    </ol>
    <div class="solution">
      <p><strong>Solution:</strong></p>
      <ol>
        <li><strong>Two-Point Form of Linear Cost Equation:</strong>
          Data points: \\((x_1, C_1) = (500, 250000)\\) and \\((x_2, C_2) = (800, 370000)\\).
          \\[ m = \\frac{C_2 - C_1}{x_2 - x_1} = \\frac{3{,}70{,}000 - 2{,}50{,}000}{800 - 500} = \\frac{1{,}20{,}000}{300} = 400. \\]
          Using Point-Slope Form:
          \\[ C - 2{,}50{,}000 = 400(x - 500) \\]
          \\[ C - 2{,}50{,}000 = 400x - 2{,}00{,}000 \\implies C(x) = 400x + 50{,}000. \\]
        </li>
        <li><strong>Economic Metrics:</strong>
          <ul>
            <li><strong>Marginal Variable Cost per unit:</strong> \\(m = ₹400\\) (the slope).</li>
            <li><strong>Fixed Overhead Cost:</strong> \\(F = ₹50{,}000\\) (the vertical intercept).</li>
          </ul>
        </li>
        <li><strong>Cost for 1,200 units:</strong>
          \\[ C(1200) = 400(1200) + 50{,}000 = 4{,}80{,}000 + 50{,}000 = ₹5{,}30{,}000. \\]
        </li>
        <li><strong>Break-Even Production Volume:</strong>
          Total Revenue \\(R(x) = 500x\\). At break-even, \\(R(x) = C(x)\\):
          \\[ 500x = 400x + 50{,}000 \\implies 100x = 50{,}000 \\implies x = 500 \\text{ units.} \\]
          <strong>Break-Even Volume = 500 units</strong>.
        </li>
      </ol>
    </div>
  </div>
`;

// 2. PROGRESS TAB
const progressHtml = `
  <h2>Progress Tracker & Self-Assessment Checklist</h2>
  <p>Track your computational speed and mastery of Straight Line Equations and Business Modeling.</p>
  <div class="checklist-grid">
    <div class="checklist-card">
      <h4>Conceptual Milestones</h4>
      <ul>
        <li><label><input type="checkbox"> Convert fluidly between Point-Slope, Slope-Intercept, and Intercept forms.</label></li>
        <li><label><input type="checkbox"> Extract slope \\(-A/B\\) and intercepts from general form \\(Ax + By + C = 0\\).</label></li>
        <li><label><input type="checkbox"> Model fixed and variable business costs as straight lines.</label></li>
        <li><label><input type="checkbox"> Solve break-even points at the intersection of cost and revenue lines.</label></li>
      </ul>
    </div>
    <div class="checklist-card">
      <h4>Problem Solving Milestones</h4>
      <ul>
        <li><label><input type="checkbox"> Formulated perpendicular bisector equations.</label></li>
        <li><label><input type="checkbox"> Found straight lines passing through points with given intercept sums.</label></li>
        <li><label><input type="checkbox"> Modeled demand and supply equilibrium intersections.</label></li>
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
    <h4>Problem 1 (Equal Intercepts Form)</h4>
    <p>Find the equation of a line that passes through the point \\((2, 3)\\) and makes equal non-zero intercepts on the coordinate axes.</p>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        <p>Using the Intercept Form \\(\\frac{x}{a} + \\frac{y}{b} = 1\\). Since intercepts are equal, \\(a = b\\):</p>
        \\[ \\frac{x}{a} + \\frac{y}{a} = 1 \\implies x + y = a. \\]
        Since the line passes through \\((2, 3)\\):
        \\[ 2 + 3 = a \\implies a = 5. \\]
        Therefore, the equation of the line is:
        \\[ x + y = 5 \\quad \\text{or} \\quad x + y - 5 = 0. \\]
      </div>
    </details>
  </div>

  <div class="problem-card">
    <h4>Problem 2 (Perpendicular Bisector Equation)</h4>
    <p>Find the equation of the perpendicular bisector of the line segment joining the points \\(A(2, 3)\\) and \\(B(6, -5)\\).</p>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        <p><strong>Step 1: Find Midpoint \\(M\\) of \\(AB\\):</strong></p>
        \\[ M = \\left( \\frac{2 + 6}{2}, \\, \\frac{3 + (-5)}{2} \\right) = (4, -1). \\]
        <p><strong>Step 2: Find Slope of \\(AB\\):</strong></p>
        \\[ m_{AB} = \\frac{-5 - 3}{6 - 2} = \\frac{-8}{4} = -2. \\]
        <p><strong>Step 3: Slope of Perpendicular Bisector:</strong></p>
        \\[ m_\\perp = -\\frac{1}{m_{AB}} = -\\frac{1}{-2} = \\frac{1}{2}. \\]
        <p><strong>Step 4: Equation using Point-Slope Form through \\((4, -1)\\):</strong></p>
        \\[ y - (-1) = \\frac{1}{2}(x - 4) \\implies 2(y + 1) = x - 4 \\implies 2y + 2 = x - 4 \\]
        \\[ x - 2y - 6 = 0. \\]
        <strong>Answer:</strong> \\(x - 2y - 6 = 0\\).
      </div>
    </details>
  </div>
`;

// 4. REVISION TAB
const revisionHtml = `
  <h2>Quick Revision & Formula Cheat Sheet</h2>
  <div class="revision-grid">
    <div class="revision-card">
      <h4>Forms Summary</h4>
      <ul>
        <li>Point-Slope: \\(y - y_0 = m(x - x_0)\\)</li>
        <li>Two-Point: \\(y - y_1 = \\frac{y_2 - y_1}{x_2 - x_1}(x - x_1)\\)</li>
        <li>Slope-Intercept: \\(y = mx + c\\)</li>
        <li>Intercept: \\(\\frac{x}{a} + \\frac{y}{b} = 1\\)</li>
      </ul>
    </div>
    <div class="revision-card">
      <h4>General Form Conversion</h4>
      <ul>
        <li>\\(Ax + By + C = 0\\)</li>
        <li>Slope: \\(m = -A/B\\)</li>
        <li>\\(y\\)-intercept: \\(c = -C/B\\)</li>
        <li>\\(x\\)-intercept: \\(d = -C/A\\)</li>
      </ul>
    </div>
    <div class="revision-card">
      <h4>Business Applications</h4>
      <ul>
        <li>Linear Cost: \\(C(x) = mx + F\\)</li>
        <li>Revenue: \\(R(x) = px\\)</li>
        <li>Break-even: \\(R(x) = C(x)\\)</li>
      </ul>
    </div>
  </div>
`;

// 5. MOCK EXAM TAB
const mockHtml = `
  <h2>10-Question Diagnostic Mock Exam</h2>
  <p class="lead-p">Test your mastery of Forms of Straight Line Equations and Business Modeling under timed CBSE conditions.</p>
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
    question: "What is the equation of a line passing through \\((-2, 3)\\) with slope \\(-4\\)?",
    options: ["\\(4x + y + 5 = 0\\)", "\\(4x + y - 5 = 0\\)", "\\(4x - y + 5 = 0\\)", "\\(x + 4y - 10 = 0\\)"],
    correct: 0,
    explanation: "\\(y - 3 = -4(x - (-2)) \\implies y - 3 = -4x - 8 \\implies 4x + y + 5 = 0\\)."
  },
  {
    id: 2,
    question: "What is the slope of the line \\(3x - 4y + 12 = 0\\)?",
    options: ["\\(-\\frac{3}{4}\\)", "\\(\\frac{3}{4}\\)", "\\(\\frac{4}{3}\\)", "3"],
    correct: 1,
    explanation: "\\(4y = 3x + 12 \\implies y = \\frac{3}{4}x + 3\\). Slope is \\(\\frac{3}{4}\\)."
  },
  {
    id: 3,
    question: "What is the \\(y\\)-intercept of the line \\(2x + 5y - 15 = 0\\)?",
    options: ["2", "3", "5", "-3"],
    correct: 1,
    explanation: "Set \\(x = 0\\): \\(5y = 15 \\implies y = 3\\)."
  },
  {
    id: 4,
    question: "What is the equation of the line cutting off intercepts \\(a = 3\\) and \\(b = -4\\) on the coordinate axes?",
    options: ["\\(4x - 3y = 12\\)", "\\(4x + 3y = 12\\)", "\\(3x - 4y = 12\\)", "\\(4x - 3y = -12\\)"],
    correct: 0,
    explanation: "\\(\\frac{x}{3} + \\frac{y}{-4} = 1 \\implies \\frac{x}{3} - \\frac{y}{4} = 1 \\implies 4x - 3y = 12\\)."
  },
  {
    id: 5,
    question: "What is the equation of the line passing through \\((1, -1)\\) and \\((3, 5)\\)?",
    options: ["\\(3x - y - 4 = 0\\)", "\\(3x + y - 2 = 0\\)", "\\(x - 3y - 4 = 0\\)", "\\(2x - y - 3 = 0\\)"],
    correct: 0,
    explanation: "\\(m = \\frac{5 - (-1)}{3 - 1} = \\frac{6}{2} = 3\\). \\(y - 5 = 3(x - 3) \\implies y - 5 = 3x - 9 \\implies 3x - y - 4 = 0\\)."
  },
  {
    id: 6,
    question: "A company’s total cost function is \\(C(x) = 25x + 4000\\). What is the fixed cost?",
    options: ["₹25", "₹160", "₹4,000", "₹1,00,000"],
    correct: 2,
    explanation: "Fixed cost is the constant vertical intercept: \\(F = ₹4,000\\)."
  },
  {
    id: 7,
    question: "What is the equation of a line parallel to the \\(y\\)-axis passing through \\((-3, 5)\\)?",
    options: ["\\(y = 5\\)", "\\(x = -3\\)", "\\(y = -3\\)", "\\(x = 5\\)"],
    correct: 1,
    explanation: "A line parallel to the \\(y\\)-axis has constant \\(x\\)-coordinate: \\(x = -3\\)."
  },
  {
    id: 8,
    question: "Find the equation of the line passing through \\((0, 0)\\) with inclination \\(60^\\circ\\).",
    options: ["\\(y = x\\)", "\\(y = \\sqrt{3}x\\)", "\\(\\sqrt{3}y = x\\)", "\\(y = 3x\\)"],
    correct: 1,
    explanation: "\\(m = \\tan 60^\\circ = \\sqrt{3}\\). Equation through origin: \\(y = \\sqrt{3}x\\)."
  },
  {
    id: 9,
    question: "What is the equation of a line passing through \\((2, 2\\sqrt{3})\\) and inclined with the \\(x\\)-axis at an angle of \\(75^\\circ\\)?",
    options: [
      "\\((\\sqrt{3}-1)x - (\\sqrt{3}+1)y = 4\\)",
      "\\((\\sqrt{3}+1)x - (\\sqrt{3}-1)y = 4\\)",
      "\\(x + y = 2\\sqrt{3}\\)",
      "\\(x - y = 2\\)"
    ],
    correct: 1,
    explanation: "\\(\\tan 75^\\circ = \\tan(45^\\circ + 30^\\circ) = \\frac{1 + 1/\\sqrt{3}}{1 - 1/\\sqrt{3}} = \\frac{\\sqrt{3}+1}{\\sqrt{3}-1}\\). \\(y - 2\\sqrt{3} = \\frac{\\sqrt{3}+1}{\\sqrt{3}-1}(x - 2) \\implies (\\sqrt{3}+1)x - (\\sqrt{3}-1)y = 4\\)."
  },
  {
    id: 10,
    question: "What are the intercepts made by the line \\(3x + 2y - 12 = 0\\) on the coordinate axes?",
    options: ["\\(a = 4, b = 6\\)", "\\(a = 6, b = 4\\)", "\\(a = 3, b = 2\\)", "\\(a = 12, b = 12\\)"],
    correct: 0,
    explanation: "\\(\\frac{3x}{12} + \\frac{2y}{12} = 1 \\implies \\frac{x}{4} + \\frac{y}{6} = 1\\). So \\(a = 4\\) and \\(b = 6\\)."
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
    resultsBox.innerHTML += '<p style="color:#059669; font-weight:600;">Outstanding! Masterful proficiency in straight line forms, intercepts, and linear cost equations.</p>';
  } else if (pct >= 50) {
    resultsBox.innerHTML += '<p style="color:#d97706; font-weight:600;">Good effort! Review the intercept form and point-slope conversions.</p>';
  } else {
    resultsBox.innerHTML += '<p style="color:#dc2626; font-weight:600;">Needs revision. Study the worked examples on straight line forms and retry.</p>';
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
console.log('Successfully upgraded 15-3-various-forms-of-equations-of-a-line/index.html');

