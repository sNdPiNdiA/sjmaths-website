const fs = require('fs');
const cheerio = require('cheerio');

const filePath = 'class-11-applied-mathematics/chapter-15-straight-lines/15-2-slope-of-a-line/index.html';
const html = fs.readFileSync(filePath, 'utf8');
const $ = cheerio.load(html);

// 1. LEARN TAB
const learnHtml = `
  <h2>15.2 Slope of a Line: Inclination, Parallelism, Perpendicularity, and Collinearity</h2>
  <p class="lead-p">
    In Applied Mathematics, corporate financial planning, and microeconomic supply-demand curves, the <strong>slope</strong> (gradient) of a line represents the constant rate of change between two variables. Whether measuring the unit variable cost in an expense curve or determining whether two commercial flight paths are parallel, slope provides the foundational directional metric.
  </p>

  <div class="formula-box">
    <h3>Fundamental Definitions & Core Theorems</h3>
    <ul>
      <li><strong>Inclination (\\(\\theta\\)):</strong> The angle made by a straight line with the positive direction of the \\(x\\)-axis, measured in the anti-clockwise direction:
        \\[ 0^\\circ \\le \\theta < 180^\\circ \\]
      </li>
      <li><strong>Slope (Gradient, \\(m\\)):</strong>
        \\[ m = \\tan \\theta \\quad (\\theta \\neq 90^\\circ) \\]
        <ul>
          <li>Horizontal line (parallel to \\(x\\)-axis): \\(\\theta = 0^\\circ \\implies m = \\tan 0^\\circ = 0\\).</li>
          <li>Vertical line (parallel to \\(y\\)-axis): \\(\\theta = 90^\\circ \\implies m = \\tan 90^\\circ\\) is <strong>undefined</strong>.</li>
          <li>Acute inclination (\\(0^\\circ < \\theta < 90^\\circ\\)): \\(m > 0\\) (Upward sloping; positive economic relationship).</li>
          <li>Obtuse inclination (\\(90^\\circ < \\theta < 180^\\circ\\)): \\(m < 0\\) (Downward sloping; demand curve relationship).</li>
        </ul>
      </li>
      <li><strong>Slope Through Two Points:</strong> The slope of the line passing through \\(A(x_1, y_1)\\) and \\(B(x_2, y_2)\\):
        \\[ m = \\frac{y_2 - y_1}{x_2 - x_1} \\quad (x_1 \\neq x_2) \\]
      </li>
      <li><strong>Condition of Parallelism:</strong> Two non-vertical lines \\(L_1\\) and \\(L_2\\) with slopes \\(m_1\\) and \\(m_2\\) are parallel if and only if their slopes are equal:
        \\[ L_1 \\parallel L_2 \\iff m_1 = m_2 \\]
      </li>
      <li><strong>Condition of Perpendicularity (Orthogonality):</strong> Two non-vertical lines \\(L_1\\) and \\(L_2\\) are perpendicular if and only if their slopes are negative reciprocals:
        \\[ L_1 \\perp L_2 \\iff m_1 \\cdot m_2 = -1 \\iff m_2 = -\\frac{1}{m_1} \\]
      </li>
      <li><strong>Acute Angle (\\(\\theta\\)) Between Two Intersecting Lines:</strong>
        \\[ \\tan \\theta = \\left| \\frac{m_2 - m_1}{1 + m_1 m_2} \\right| \\quad (1 + m_1 m_2 \\neq 0) \\]
      </li>
      <li><strong>Collinearity of Three Points via Slopes:</strong>
        Points \\(A, B, C\\) lie on the same straight line if and only if:
        \\[ \\text{Slope of } AB = \\text{Slope of } BC \\]
      </li>
    </ul>
  </div>

  <div class="worked-example">
    <h4>Comprehensive Applied Example: Perpendicular Production Boundaries</h4>
    <p><strong>Problem:</strong> Line \\(L_1\\) passes through points \\(A(3, y)\\) and \\(B(2, 7)\\), while line \\(L_2\\) passes through points \\(C(-1, 4)\\) and \\(D(0, 6)\\).</p>
    <ol>
      <li>Find the value of \\(y\\) if line \\(L_1\\) is parallel to line \\(L_2\\).</li>
      <li>Find the value of \\(y\\) if line \\(L_1\\) is perpendicular to line \\(L_2\\).</li>
      <li>Find the acute angle between \\(L_2\\) and the line \\(y = 3x - 5\\).</li>
    </ol>
    <div class="solution">
      <p><strong>Solution:</strong></p>
      <p>First find the slope of \\(L_2\\):</p>
      \\[ m_2 = \\frac{6 - 4}{0 - (-1)} = \\frac{2}{1} = 2. \\]
      <p>The slope of \\(L_1\\) is:</p>
      \\[ m_1 = \\frac{7 - y}{2 - 3} = \\frac{7 - y}{-1} = y - 7. \\]

      <ol>
        <li><strong>For Parallel Lines (\\(m_1 = m_2\\)):</strong>
          \\[ y - 7 = 2 \\implies y = 9. \\]
        </li>
        <li><strong>For Perpendicular Lines (\\(m_1 \\cdot m_2 = -1\\)):</strong>
          \\[ (y - 7)(2) = -1 \\implies 2y - 14 = -1 \\implies 2y = 13 \\implies y = \\frac{13}{2} = 6.5. \\]
        </li>
        <li><strong>Acute Angle with \\(y = 3x - 5\\):</strong>
          Here \\(m_1 = 3\\) and \\(m_2 = 2\\):
          \\[ \\tan \\theta = \\left| \\frac{3 - 2}{1 + 3(2)} \\right| = \\left| \\frac{1}{1 + 6} \\right| = \\frac{1}{7} \\]
          \\[ \\theta = \\tan^{-1}\\left(\\frac{1}{7}\\right) \\approx 8.13^\\circ. \\]
        </li>
      </ol>
    </div>
  </div>
`;

// 2. PROGRESS TAB
const progressHtml = `
  <h2>Progress Tracker & Self-Assessment Checklist</h2>
  <p>Track your computational speed and mastery of Line Slopes, Parallelism, and Angles.</p>
  <div class="checklist-grid">
    <div class="checklist-card">
      <h4>Conceptual Milestones</h4>
      <ul>
        <li><label><input type="checkbox"> Define inclination \\(\\theta\\) and slope \\(m = \\tan \\theta\\).</label></li>
        <li><label><input type="checkbox"> Compute two-point slope \\(m = \\frac{y_2 - y_1}{x_2 - x_1}\\).</label></li>
        <li><label><input type="checkbox"> Apply parallelism condition \\(m_1 = m_2\\).</label></li>
        <li><label><input type="checkbox"> Apply perpendicularity condition \\(m_1 m_2 = -1\\).</label></li>
        <li><label><input type="checkbox"> Calculate acute angles between lines using \\(\\tan \\theta = |\\frac{m_2 - m_1}{1 + m_1 m_2}|\\).</label></li>
      </ul>
    </div>
    <div class="checklist-card">
      <h4>Problem Solving Milestones</h4>
      <ul>
        <li><label><input type="checkbox"> Solved unknown coordinate parameters for parallel and perpendicular lines.</label></li>
        <li><label><input type="checkbox"> Proved collinearity using equal slopes.</label></li>
        <li><label><input type="checkbox"> Verified right-angled triangles using perpendicular slope products.</label></li>
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
    <h4>Problem 1 (Angle Between Two Lines)</h4>
    <p>Find the angle between the lines \\(y - \\sqrt{3}x - 5 = 0\\) and \\(\\sqrt{3}y - x + 6 = 0\\).</p>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        <p>First convert both equations to slope-intercept form \\(y = mx + c\\):</p>
        <ul>
          <li>Line 1: \\(y = \\sqrt{3}x + 5 \\implies m_1 = \\sqrt{3}\\).</li>
          <li>Line 2: \\(\\sqrt{3}y = x - 6 \\implies y = \\frac{1}{\\sqrt{3}}x - \\frac{6}{\\sqrt{3}} \\implies m_2 = \\frac{1}{\\sqrt{3}}\\).</li>
        </ul>
        Apply the angle formula:
        \\[ \\tan \\theta = \\left| \\frac{m_1 - m_2}{1 + m_1 m_2} \\right| = \\left| \\frac{\\sqrt{3} - \\frac{1}{\\sqrt{3}}}{1 + (\\sqrt{3})\\left(\\frac{1}{\\sqrt{3}}\\right)} \\right| = \\left| \\frac{\\frac{3 - 1}{\\sqrt{3}}}{1 + 1} \\right| = \\frac{2 / \\sqrt{3}}{2} = \\frac{1}{\\sqrt{3}}. \\]
        Since \\(\\tan \\theta = \\frac{1}{\\sqrt{3}}\\):
        \\[ \\theta = 30^\\circ \\quad (\\text{or acute angle } 30^\\circ, \\text{ obtuse angle } 150^\\circ). \\]
        <strong>Answer:</strong> The acute angle between the lines is <strong>\\(30^\\circ\\)</strong>.
      </div>
    </details>
  </div>

  <div class="problem-card">
    <h4>Problem 2 (Collinearity Proof via Slope)</h4>
    <p>Without using the distance or area formula, show that the points \\(A(-2, -1)\\), \\(B(4, 0)\\), and \\(C(16, 2)\\) are collinear.</p>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        \\[ \\text{Slope of } AB = \\frac{0 - (-1)}{4 - (-2)} = \\frac{1}{6}. \\]
        \\[ \\text{Slope of } BC = \\frac{2 - 0}{16 - 4} = \\frac{2}{12} = \\frac{1}{6}. \\]
        Since \\(\\text{Slope of } AB = \\text{Slope of } BC\\) and point \\(B\\) is common to both segments, the points \\(A, B, C\\) lie on the same straight line and are therefore <strong>collinear</strong>.
      </div>
    </details>
  </div>
`;

// 4. REVISION TAB
const revisionHtml = `
  <h2>Quick Revision & Formula Cheat Sheet</h2>
  <div class="revision-grid">
    <div class="revision-card">
      <h4>Slope Formulas</h4>
      <ul>
        <li>\\(m = \\tan \\theta\\) (\\(\\theta\\) is inclination)</li>
        <li>\\(m = \\frac{y_2 - y_1}{x_2 - x_1}\\)</li>
        <li>Horizontal: \\(m = 0\\)</li>
        <li>Vertical: \\(m = \\text{undefined}\\)</li>
      </ul>
    </div>
    <div class="revision-card">
      <h4>Parallel & Perpendicular</h4>
      <ul>
        <li>Parallel: \\(m_1 = m_2\\)</li>
        <li>Perpendicular: \\(m_1 \\cdot m_2 = -1\\)</li>
        <li>Collinear points: \\(\\text{Slope}(AB) = \\text{Slope}(BC)\\)</li>
      </ul>
    </div>
    <div class="revision-card">
      <h4>Angle Between Lines</h4>
      <ul>
        <li>\\(\\tan \\theta = \\left| \\frac{m_2 - m_1}{1 + m_1 m_2} \\right|\\)</li>
        <li>Acute angle \\(\\theta\\)</li>
        <li>Obtuse angle \\(= 180^\\circ - \\theta\\)</li>
      </ul>
    </div>
  </div>
`;

// 5. MOCK EXAM TAB
const mockHtml = `
  <h2>10-Question Diagnostic Mock Exam</h2>
  <p class="lead-p">Test your mastery of Line Slopes, Angles Between Lines, and Perpendicularity under timed CBSE conditions.</p>
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
    question: "What is the slope of a line whose inclination with the positive \\(x\\)-axis is \\(135^\\circ\\)?",
    options: ["1", "-1", "\\(\\frac{1}{\\sqrt{3}}\\)", "\\(-\\sqrt{3}\\)"],
    correct: 1,
    explanation: "\\(m = \\tan(135^\\circ) = \\tan(180^\\circ - 45^\\circ) = -\\tan 45^\\circ = -1\\)."
  },
  {
    id: 2,
    question: "What is the slope of the line passing through \\((3, -2)\\) and \\((-1, 4)\\)?",
    options: ["\\(\\frac{3}{2}\\)", "\\(-\\frac{3}{2}\\)", "\\(\\frac{2}{3}\\)", "\\(-\\frac{2}{3}\\)"],
    correct: 1,
    explanation: "\\(m = \\frac{4 - (-2)}{-1 - 3} = \\frac{6}{-4} = -\\frac{3}{2}\\)."
  },
  {
    id: 3,
    question: "If a line has slope \\(\\frac{2}{3}\\), what is the slope of any line perpendicular to it?",
    options: ["\\(\\frac{2}{3}\\)", "\\(-\\frac{2}{3}\\)", "\\(\\frac{3}{2}\\)", "\\(-\\frac{3}{2}\\)"],
    correct: 3,
    explanation: "Perpendicular slope \\(m_2 = -1 / m_1 = -1 / (2/3) = -3/2\\)."
  },
  {
    id: 4,
    question: "If the line joining \\((2, 5)\\) and \\((x, 3)\\) is parallel to the line joining \\((4, -1)\\) and \\((2, 1)\\), find \\(x\\).",
    options: ["1", "3", "4", "5"],
    correct: 2,
    explanation: "\\(m_2 = \\frac{1 - (-1)}{2 - 4} = \\frac{2}{-2} = -1\\). Then \\(m_1 = \\frac{3 - 5}{x - 2} = \\frac{-2}{x - 2} = -1 \\implies x - 2 = 2 \\implies x = 4\\)."
  },
  {
    id: 5,
    question: "What is the slope of a line perpendicular to the \\(x\\)-axis?",
    options: ["0", "1", "-1", "Undefined"],
    correct: 3,
    explanation: "A line perpendicular to the \\(x\\)-axis is a vertical line (\\(\\theta = 90^\\circ\\)), whose slope is undefined."
  },
  {
    id: 6,
    question: "What is the acute angle between the lines with slopes \\(m_1 = 2\\) and \\(m_2 = -3\\)?",
    options: ["\\(30^\\circ\\)", "\\(45^\\circ\\)", "\\(60^\\circ\\)", "\\(90^\\circ\\)"],
    correct: 1,
    explanation: "\\(\\tan \\theta = \\left| \\frac{-3 - 2}{1 + 2(-3)} \\right| = \\left| \\frac{-5}{1 - 6} \\right| = \\left| \\frac{-5}{-5} \\right| = 1 \\implies \\theta = 45^\\circ\\)."
  },
  {
    id: 7,
    question: "If the slope of a line is 0, the line is:",
    options: [
      "Parallel to the \\(x\\)-axis",
      "Parallel to the \\(y\\)-axis",
      "Passing through the origin at \\(45^\\circ\\)",
      "Undefined"
    ],
    correct: 0,
    explanation: "\\(m = \\tan \\theta = 0 \\implies \\theta = 0^\\circ\\), which represents a line parallel to the \\(x\\)-axis."
  },
  {
    id: 8,
    question: "If points \\(A(1, 4)\\), \\(B(3, -2)\\), and \\(C(k, 1)\\) are collinear, what is \\(k\\)?",
    options: ["1", "2", "3", "4"],
    correct: 1,
    explanation: "\\(\\text{Slope}(AB) = \\frac{-2 - 4}{3 - 1} = \\frac{-6}{2} = -3\\). \\(\\text{Slope}(AC) = \\frac{1 - 4}{k - 1} = \\frac{-3}{k - 1} = -3 \\implies k - 1 = 1 \\implies k = 2\\)."
  },
  {
    id: 9,
    question: "The product of the slopes of two perpendicular non-vertical lines is ALWAYS:",
    options: ["1", "0", "-1", "\\(\\infty\\)"],
    correct: 2,
    explanation: "By the orthogonality theorem: \\(m_1 \\cdot m_2 = -1\\)."
  },
  {
    id: 10,
    question: "If the acute angle between two lines is \\(45^\\circ\\) and the slope of one line is \\(\\frac{1}{2}\\), what is the slope of the other line?",
    options: ["3 or \\(-\\frac{1}{3}\\)", "2 or \\(-\\frac{1}{2}\\)", "1 or -1", "4 or \\(-\\frac{1}{4}\\)"],
    correct: 0,
    explanation: "\\(\\tan 45^\\circ = 1 = \\left| \\frac{m - 1/2}{1 + m/2} \\right| = \\left| \\frac{2m - 1}{2 + m} \\right|\\). Either \\(\\frac{2m - 1}{2 + m} = 1 \\implies 2m - 1 = 2 + m \\implies m = 3\\), or \\(\\frac{2m - 1}{2 + m} = -1 \\implies 2m - 1 = -2 - m \\implies 3m = -1 \\implies m = -1/3\\)."
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
    resultsBox.innerHTML += '<p style="color:#059669; font-weight:600;">Outstanding! Masterful proficiency in slopes, parallelism, and perpendicularity.</p>';
  } else if (pct >= 50) {
    resultsBox.innerHTML += '<p style="color:#d97706; font-weight:600;">Good effort! Review angle formulas and negative reciprocal slopes.</p>';
  } else {
    resultsBox.innerHTML += '<p style="color:#dc2626; font-weight:600;">Needs revision. Study the worked examples on line slopes and retry.</p>';
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
console.log('Successfully upgraded 15-2-slope-of-a-line/index.html');
