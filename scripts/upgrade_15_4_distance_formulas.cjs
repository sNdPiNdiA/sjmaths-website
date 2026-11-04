const fs = require('fs');
const cheerio = require('cheerio');

const filePath = 'class-11-applied-mathematics/chapter-15-straight-lines/15-4-distance-formulas/index.html';
const html = fs.readFileSync(filePath, 'utf8');
const $ = cheerio.load(html);

// 1. LEARN TAB
const learnHtml = `
  <h2>15.4 Distance Formulas: Point-to-Line and Parallel Line Clearances</h2>
  <p class="lead-p">
    In Applied Mathematics, civil engineering, regional urban planning, and spatial logistics, calculating the <strong>shortest distance</strong> between facilities and linear infrastructures (highways, power lines, transit tracks) is a critical optimization task. The perpendicular distance formulas translate spatial separation into direct algebraic computation.
  </p>

  <div class="formula-box">
    <h3>Fundamental Formulae & Theorems</h3>
    <ul>
      <li><strong>Perpendicular Distance of a Point from a Line:</strong> The perpendicular distance \\(d\\) from a point \\(P(x_1, y_1)\\) to the line \\(Ax + By + C = 0\\):
        \\[ d = \\frac{|A x_1 + B y_1 + C|}{\\sqrt{A^2 + B^2}} \\]
      </li>
      <li><strong>Distance from the Origin \\((0, 0)\\):</strong>
        \\[ d_0 = \\frac{|C|}{\\sqrt{A^2 + B^2}} \\]
      </li>
      <li><strong>Distance Between Two Parallel Lines:</strong> Two parallel lines can always be written with identical \\(x\\) and \\(y\\) coefficients:
        \\[ L_1: Ax + By + C_1 = 0 \\quad \\text{and} \\quad L_2: Ax + By + C_2 = 0 \\]
        The perpendicular distance \\(d\\) between \\(L_1\\) and \\(L_2\\) is:
        \\[ d = \\frac{|C_1 - C_2|}{\\sqrt{A^2 + B^2}} \\]
        <em>Slope-Intercept Form:</em> If \\(y = mx + c_1\\) and \\(y = mx + c_2\\):
        \\[ d = \\frac{|c_1 - c_2|}{\\sqrt{1 + m^2}} \\]
      </li>
    </ul>
  </div>

  <div class="worked-example">
    <h4>Comprehensive Applied Example: Hazardous Pipeline Buffer Clearance</h4>
    <p><strong>Scenario:</strong> A high-pressure natural gas pipeline runs along the straight line \\(3x - 4y + 10 = 0\\) across an industrial zone. A petrochemical warehouse is located at coordinates \\(P(4, -1)\\).</p>
    <ol>
      <li>Find the shortest distance between the warehouse and the pipeline.</li>
      <li>If municipal safety regulations mandate a minimum safety clearance buffer of 6 km, determine whether the warehouse meets regulatory compliance.</li>
      <li>A parallel reserve pipeline is planned along the line \\(6x - 8y - 15 = 0\\). What is the exact separation distance between the primary and reserve pipelines?</li>
    </ol>
    <div class="solution">
      <p><strong>Solution:</strong></p>
      <ol>
        <li><strong>Distance from Warehouse \\(P(4, -1)\\) to Pipeline:</strong>
          Here \\(A = 3\\), \\(B = -4\\), \\(C = 10\\), \\(x_1 = 4\\), \\(y_1 = -1\\):
          \\[ d = \\frac{|3(4) + (-4)(-1) + 10|}{\\sqrt{3^2 + (-4)^2}} = \\frac{|12 + 4 + 10|}{\\sqrt{9 + 16}} = \\frac{|26|}{\\sqrt{25}} = \\frac{26}{5} = 5.2 \\text{ km.} \\]
        </li>
        <li><strong>Compliance Verification:</strong>
          Since the actual distance is \\(5.2\\text{ km} < 6\\text{ km}\\), the warehouse <strong>violates the 6 km safety clearance buffer</strong>.
        </li>
        <li><strong>Separation Distance Between Parallel Pipelines:</strong>
          The primary line is \\(3x - 4y + 10 = 0\\). Multiply by 2 so coefficients match:
          \\[ 6x - 8y + 20 = 0 \\quad \\implies C_1 = 20 \\]
          The secondary line is:
          \\[ 6x - 8y - 15 = 0 \\quad \\implies C_2 = -15 \\]
          Now apply the parallel line distance formula:
          \\[ d = \\frac{|C_1 - C_2|}{\\sqrt{A^2 + B^2}} = \\frac{|20 - (-15)|}{\\sqrt{6^2 + (-8)^2}} = \\frac{|35|}{\\sqrt{36 + 64}} = \\frac{35}{\\sqrt{100}} = \\frac{35}{10} = 3.5 \\text{ km.} \\]
          <strong>Separation Distance = 3.5 km</strong>.
        </li>
      </ol>
    </div>
  </div>
`;

// 2. PROGRESS TAB
const progressHtml = `
  <h2>Progress Tracker & Self-Assessment Checklist</h2>
  <p>Track your computational speed and mastery of Point-to-Line and Parallel Line Distances.</p>
  <div class="checklist-grid">
    <div class="checklist-card">
      <h4>Conceptual Milestones</h4>
      <ul>
        <li><label><input type="checkbox"> Compute distance from a point to a line using \\(d = \\frac{|Ax_1+By_1+C|}{\\sqrt{A^2+B^2}}\\).</label></li>
        <li><label><input type="checkbox"> Equalize coefficients before calculating distance between parallel lines.</label></li>
        <li><label><input type="checkbox"> Solve for unknown line constants given a specified distance.</label></li>
        <li><label><input type="checkbox"> Apply distance formulas to spatial clearance and buffer zones.</label></li>
      </ul>
    </div>
    <div class="checklist-card">
      <h4>Problem Solving Milestones</h4>
      <ul>
        <li><label><input type="checkbox"> Solved parallel line distance with unequal fractional coefficients.</label></li>
        <li><label><input type="checkbox"> Found points on a line equidistant from two given points.</label></li>
        <li><label><input type="checkbox"> Calculated altitude lengths of triangles using distance to side lines.</label></li>
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
    <h4>Problem 1 (Distance Between Two Parallel Lines)</h4>
    <p>Find the distance between the parallel lines \\(15x + 8y - 34 = 0\\) and \\(15x + 8y + 31 = 0\\).</p>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        <p>Here \\(A = 15\\), \\(B = 8\\), \\(C_1 = -34\\), \\(C_2 = 31\\):</p>
        \\[ d = \\frac{|C_1 - C_2|}{\\sqrt{A^2 + B^2}} = \\frac{|-34 - 31|}{\\sqrt{15^2 + 8^2}} = \\frac{|-65|}{\\sqrt{225 + 64}} = \\frac{65}{\\sqrt{289}} = \\frac{65}{17} \\text{ units.} \\]
        <strong>Answer:</strong> \\(\\frac{65}{17}\\) units.
      </div>
    </details>
  </div>

  <div class="problem-card">
    <h4>Problem 2 (Finding Points on the X-axis at a Given Distance)</h4>
    <p>Find the points on the \\(x\\)-axis whose distance from the line \\(\\frac{x}{3} + \\frac{y}{4} = 1\\) is 4 units.</p>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        <p>First convert \\(\\frac{x}{3} + \\frac{y}{4} = 1\\) to general form: \\(4x + 3y - 12 = 0\\).</p>
        <p>Any point on the \\(x\\)-axis has coordinates \\(P(x_0, 0)\\). Its distance from the line is:</p>
        \\[ d = \\frac{|4x_0 + 3(0) - 12|}{\\sqrt{4^2 + 3^2}} = \\frac{|4x_0 - 12|}{5} = 4 \\]
        \\[ |4x_0 - 12| = 20 \\]
        This yields two linear cases:
        <ul>
          <li>Case 1: \\(4x_0 - 12 = 20 \\implies 4x_0 = 32 \\implies x_0 = 8\\). Point is \\((8, 0)\\).</li>
          <li>Case 2: \\(4x_0 - 12 = -20 \\implies 4x_0 = -8 \\implies x_0 = -2\\). Point is \\((-2, 0)\\).</li>
        </ul>
        <strong>Answer:</strong> The points are <strong>\\((8, 0)\\)</strong> and <strong>\\((-2, 0)\\)</strong>.
      </div>
    </details>
  </div>
`;

// 4. REVISION TAB
const revisionHtml = `
  <h2>Quick Revision & Formula Cheat Sheet</h2>
  <div class="revision-grid">
    <div class="revision-card">
      <h4>Point-to-Line Distance</h4>
      <ul>
        <li>\\(d = \\frac{|Ax_1 + By_1 + C|}{\\sqrt{A^2 + B^2}}\\)</li>
        <li>From origin: \\(d_0 = \\frac{|C|}{\\sqrt{A^2 + B^2}}\\)</li>
        <li>Sign inside absolute value indicates which half-plane point lies in</li>
      </ul>
    </div>
    <div class="revision-card">
      <h4>Parallel Line Distance</h4>
      <ul>
        <li>\\(d = \\frac{|C_1 - C_2|}{\\sqrt{A^2 + B^2}}\\)</li>
        <li>Coefficients \\(A\\) and \\(B\\) MUST be matched first</li>
        <li>Slope-intercept: \\(d = \\frac{|c_1 - c_2|}{\\sqrt{1 + m^2}}\\)</li>
      </ul>
    </div>
  </div>
`;

// 5. MOCK EXAM TAB
const mockHtml = `
  <h2>10-Question Diagnostic Mock Exam</h2>
  <p class="lead-p">Test your mastery of Perpendicular Distances and Parallel Line Clearances under timed CBSE conditions.</p>
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
    question: "What is the perpendicular distance of the point \\((3, -5)\\) from the line \\(3x - 4y - 26 = 0\\)?",
    options: ["\\(\\frac{3}{5}\\)", "\\(\\frac{1}{2}\\)", "\\(\\frac{1}{5}\\)", "1"],
    correct: 0,
    explanation: "\\(d = \\frac{|3(3) - 4(-5) - 26|}{\\sqrt{9 + 16}} = \\frac{|9 + 20 - 26|}{5} = \\frac{|3|}{5} = \\frac{3}{5}\\)."
  },
  {
    id: 2,
    question: "What is the distance of the origin from the line \\(4x - 3y + 15 = 0\\)?",
    options: ["2", "3", "4", "5"],
    correct: 1,
    explanation: "\\(d = \\frac{|15|}{\\sqrt{16 + 9}} = \\frac{15}{5} = 3\\)."
  },
  {
    id: 3,
    question: "What is the distance between the parallel lines \\(3x + 4y - 9 = 0\\) and \\(6x + 8y - 15 = 0\\)?",
    options: ["\\(\\frac{3}{10}\\)", "\\(\\frac{6}{5}\\)", "\\(\\frac{3}{5}\\)", "\\(\\frac{9}{10}\\)"],
    correct: 0,
    explanation: "Multiply first equation by 2: \\(6x + 8y - 18 = 0\\). \\(d = \\frac{|-18 - (-15)|}{\\sqrt{36 + 64}} = \\frac{|-3|}{10} = \\frac{3}{10}\\)."
  },
  {
    id: 4,
    question: "If the perpendicular distance of \\((1, 1)\\) from \\(3x + 4y + c = 0\\) is 2, what are the possible values of \\(c\\)?",
    options: ["\\(3\\) or \\(-17\\)", "\\(17\\) or \\(-3\\)", "\\(7\\) or \\(-7\\)", "\\(10\\) or \\(-10\\)"],
    correct: 0,
    explanation: "\\(\\frac{|3(1) + 4(1) + c|}{\\sqrt{9 + 16}} = \\frac{|7 + c|}{5} = 2 \\implies |7 + c| = 10 \\implies 7 + c = 10 \\implies c = 3\\), or \\(7 + c = -10 \\implies c = -17\\)."
  },
  {
    id: 5,
    question: "What is the distance between parallel lines \\(y = 2x + 7\\) and \\(y = 2x - 3\\)?",
    options: ["\\(\\sqrt{5}\\)", "\\(2\\sqrt{5}\\)", "\\(4\\sqrt{5}\\)", "10"],
    correct: 1,
    explanation: "\\(d = \\frac{|c_1 - c_2|}{\\sqrt{1 + m^2}} = \\frac{|7 - (-3)|}{\\sqrt{1 + 2^2}} = \\frac{10}{\\sqrt{5}} = 2\\sqrt{5}\\)."
  },
  {
    id: 6,
    question: "The distance of any point \\((x_1, y_1)\\) lying ON the line \\(Ax + By + C = 0\\) from the line itself is:",
    options: ["1", "-1", "0", "Undefined"],
    correct: 2,
    explanation: "Since the point satisfies \\(Ax_1 + By_1 + C = 0\\), the numerator vanishes, so distance is 0."
  },
  {
    id: 7,
    question: "What is the distance of point \\((2, 3)\\) from the line \\(x - y + 1 = 0\\)?",
    options: ["0", "\\(\\sqrt{2}\\)", "2", "\\(2\\sqrt{2}\\)"],
    correct: 0,
    explanation: "\\(d = \\frac{|2 - 3 + 1|}{\\sqrt{1^2 + (-1)^2}} = \\frac{|0|}{\\sqrt{2}} = 0\\) (The point lies directly on the line!)."
  },
  {
    id: 8,
    question: "If lines \\(Ax + By + C_1 = 0\\) and \\(Ax + By + C_2 = 0\\) are coincident (identical), then the distance between them is:",
    options: ["0", "1", "\\(C_1 - C_2\\)", "Undefined"],
    correct: 0,
    explanation: "Coincident lines have \\(C_1 = C_2\\), yielding distance 0."
  },
  {
    id: 9,
    question: "What is the length of the altitude from vertex \\(A(0, 0)\\) to the line \\(5x + 12y - 26 = 0\\)?",
    options: ["1", "2", "3", "4"],
    correct: 1,
    explanation: "\\(d = \\frac{|-26|}{\\sqrt{5^2 + 12^2}} = \\frac{26}{13} = 2\\)."
  },
  {
    id: 10,
    question: "Why must the coefficients of \\(x\\) and \\(y\\) be made identical before applying the parallel distance formula \\(\\frac{|C_1 - C_2|}{\\sqrt{A^2 + B^2}}\\)?",
    options: [
      "To ensure the denominator \\(\\sqrt{A^2 + B^2}\\) uses a consistent metric normal",
      "Because lines are only parallel if \\(A = B\\)",
      "To eliminate the slope parameter",
      "Because the distance depends on the origin"
    ],
    correct: 0,
    explanation: "Matching \\(A\\) and \\(B\\) ensures that both equations are normalized to the identical gradient vector length in the denominator."
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
    resultsBox.innerHTML += '<p style="color:#059669; font-weight:600;">Outstanding! Masterful proficiency in perpendicular distances and parallel line separation.</p>';
  } else if (pct >= 50) {
    resultsBox.innerHTML += '<p style="color:#d97706; font-weight:600;">Good effort! Review the parallel distance formula coefficient matching.</p>';
  } else {
    resultsBox.innerHTML += '<p style="color:#dc2626; font-weight:600;">Needs revision. Study the worked examples on distance formulas and retry.</p>';
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
console.log('Successfully upgraded 15-4-distance-formulas/index.html');
