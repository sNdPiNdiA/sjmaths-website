const fs = require('fs');
const cheerio = require('cheerio');

const filePath = 'class-11-applied-mathematics/chapter-9-probability/9-4-conditional-probability/index.html';
const html = fs.readFileSync(filePath, 'utf8');
const $ = cheerio.load(html);

// 1. LEARN TAB
const learnHtml = `
  <h2>9.4 Conditional Probability: Reduced Sample Spaces, Multiplication Rule, and Independent Events</h2>
  <p class="lead-p">
    In Applied Mathematics, corporate credit scoring, medical diagnostic screening, and algorithmic Bayesian models, probability estimates are constantly updated as new empirical information becomes available. <strong>Conditional probability</strong> formalizes how the probability of an event \\(A\\) is revised once we know that another event \\(B\\) has already occurred.
  </p>

  <div class="formula-box">
    <h3>Fundamental Definitions & Core Theorems</h3>
    <ul>
      <li><strong>Definition of Conditional Probability:</strong> If \\(A\\) and \\(B\\) are two events associated with the same sample space \\(S\\), the conditional probability of \\(A\\) given that \\(B\\) has already occurred (with \\(P(B) > 0\\)) is:
        \\[ P(A | B) = \\frac{P(A \\cap B)}{P(B)} = \\frac{n(A \\cap B)}{n(B)} \\]
        <em>Conceptual Meaning:</em> Event \\(B\\) replaces \\(S\\) as the new, reduced sample space.
      </li>
      <li><strong>Multiplication Theorem of Probability:</strong>
        \\[ P(A \\cap B) = P(A) \\cdot P(B | A) = P(B) \\cdot P(A | B) \\]
        <em>For 3 events:</em> \\(P(A \\cap B \\cap C) = P(A) \\cdot P(B | A) \\cdot P(C | (A \\cap B))\\).
      </li>
      <li><strong>Independent Events:</strong>
        Two events \\(A\\) and \\(B\\) are statistically independent if the occurrence of \\(B\\) has no influence on the probability of \\(A\\):
        \\[ P(A | B) = P(A) \\iff P(A \\cap B) = P(A) \\cdot P(B) \\]
      </li>
      <li><strong>Critical Distinction: Mutually Exclusive vs Independent:</strong>
        <table class="table-styled">
          <thead>
            <tr>
              <th>Property</th>
              <th>Mutually Exclusive Events</th>
              <th>Independent Events</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Definition</strong></td>
              <td>Cannot happen together (\\(A \\cap B = \\emptyset\\))</td>
              <td>Occurrence of one doesn't affect the other</td>
            </tr>
            <tr>
              <td><strong>Mathematical Condition</strong></td>
              <td>\\[ P(A \\cap B) = 0 \\]</td>
              <td>\\[ P(A \\cap B) = P(A) \\cdot P(B) \\]</td>
            </tr>
            <tr>
              <td><strong>Core Incompatibility</strong></td>
              <td colspan="2">Two events with non-zero probabilities <strong>can never be both</strong> mutually exclusive and independent!</td>
            </tr>
          </tbody>
        </table>
      </li>
      <li><strong>Independence of Complements Theorem:</strong>
        If \\(A\\) and \\(B\\) are independent events, then:
        <ol>
          <li>\\(A\\) and \\(B'\\) are independent: \\(P(A \\cap B') = P(A) \\cdot P(B')\\)</li>
          <li>\\(A'\\) and \\(B\\) are independent: \\(P(A' \\cap B) = P(A') \\cdot P(B)\\)</li>
          <li>\\(A'\\) and \\(B'\\) are independent: \\(P(A' \\cap B') = P(A') \\cdot P(B')\\)</li>
        </ol>
      </li>
    </ul>
  </div>

  <div class="worked-example">
    <h4>Comprehensive Applied Example: Target Reliability Engineering</h4>
    <p><strong>Scenario:</strong> Two independent defense radar units, \\(R_1\\) and \\(R_2\\), track an incoming airspace target. The probability that \\(R_1\\) detects the target is \\(P(R_1) = 0.8\\), and the probability that \\(R_2\\) detects the target is \\(P(R_2) = 0.7\\).</p>
    <p>Find the probability that:</p>
    <ol>
      <li>Both radar units detect the target.</li>
      <li>The target is detected by at least one radar unit.</li>
      <li>Exactly one radar unit detects the target.</li>
      <li>Neither radar unit detects the target.</li>
    </ol>
    <div class="solution">
      <p><strong>Solution:</strong></p>
      <p>Because the radar units operate independently: \\(P(R_1 \\cap R_2) = P(R_1) \\cdot P(R_2)\\).</p>
      <ol>
        <li><strong>Both detect the target:</strong>
          \\[ P(R_1 \\cap R_2) = 0.8 \\times 0.7 = 0.56. \\]
        </li>
        <li><strong>At least one detects the target (Addition Theorem):</strong>
          \\[ P(R_1 \\cup R_2) = P(R_1) + P(R_2) - P(R_1 \\cap R_2) = 0.8 + 0.7 - 0.56 = 0.94. \\]
          <em>Alternative via Complements:</em>
          \\[ P(R_1 \\cup R_2) = 1 - P(R_1' \\cap R_2') = 1 - (1 - 0.8)(1 - 0.7) = 1 - (0.2 \\times 0.3) = 1 - 0.06 = 0.94. \\]
        </li>
        <li><strong>Exactly one radar detects the target:</strong>
          \\[ P(\\text{Exactly 1}) = P(R_1 \\cap R_2') + P(R_1' \\cap R_2) = (0.8 \\times 0.3) + (0.2 \\times 0.7) = 0.24 + 0.14 = 0.38. \\]
        </li>
        <li><strong>Neither radar detects the target:</strong>
          \\[ P(R_1' \\cap R_2') = P(R_1') \\cdot P(R_2') = 0.2 \\times 0.3 = 0.06. \\]
        </li>
      </ol>
    </div>
  </div>
`;

// 2. PROGRESS TAB
const progressHtml = `
  <h2>Progress Tracker & Self-Assessment Checklist</h2>
  <p>Track your computational speed and mastery of Conditional Probability and Independent Events.</p>
  <div class="checklist-grid">
    <div class="checklist-card">
      <h4>Conceptual Milestones</h4>
      <ul>
        <li><label><input type="checkbox"> Compute conditional probability \\(P(A | B) = \\frac{P(A \\cap B)}{P(B)}\\).</label></li>
        <li><label><input type="checkbox"> Apply the Multiplication Rule \\(P(A \\cap B) = P(B) P(A | B)\\).</label></li>
        <li><label><input type="checkbox"> Test whether two events are statistically independent using \\(P(A \\cap B) = P(A)P(B)\\).</label></li>
        <li><label><input type="checkbox"> Differentiate between mutually exclusive and independent events.</label></li>
      </ul>
    </div>
    <div class="checklist-card">
      <h4>Problem Solving Milestones</h4>
      <ul>
        <li><label><input type="checkbox"> Solved sampling without replacement problems using conditional chains.</label></li>
        <li><label><input type="checkbox"> Solved system reliability and target detection problems.</label></li>
        <li><label><input type="checkbox"> Calculated probabilities of independent complements.</label></li>
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
    <h4>Problem 1 (Two-Children Family Conditioning)</h4>
    <p>A family has two children. What is the conditional probability that both are boys given that:</p>
    <ol type="a">
      <li>The youngest child is a boy?</li>
      <li>At least one of the children is a boy?</li>
    </ol>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        <p>Sample space of genders in birth order (older, younger): \\(S = \\{ BB, BG, GB, GG \\}\\), \\(n(S) = 4\\).</p>
        <p>Let \\(A\\) be the event "both children are boys": \\(A = \\{ BB \\}\\), \\(n(A) = 1\\).</p>

        <p><strong>Part (a): Given youngest is a boy (\\(B_1\\)):</strong></p>
        \\[ B_1 = \\{ BB, GB \\}, \\quad n(B_1) = 2. \\]
        \\[ A \\cap B_1 = \\{ BB \\}, \\quad n(A \\cap B_1) = 1. \\]
        \\[ P(A | B_1) = \\frac{n(A \\cap B_1)}{n(B_1)} = \\frac{1}{2}. \\]

        <p><strong>Part (b): Given at least one is a boy (\\(B_2\\)):</strong></p>
        \\[ B_2 = \\{ BB, BG, GB \\}, \\quad n(B_2) = 3. \\]
        \\[ A \\cap B_2 = \\{ BB \\}, \\quad n(A \\cap B_2) = 1. \\]
        \\[ P(A | B_2) = \\frac{n(A \\cap B_2)}{n(B_2)} = \\frac{1}{3}. \\]
      </div>
    </details>
  </div>

  <div class="problem-card">
    <h4>Problem 2 (Independent Problem Solving)</h4>
    <p>A problem in Applied Mathematics is given to three students, \\(A, B, C\\), whose probabilities of solving it independently are \\(\\frac{1}{2}, \\frac{1}{3},\\) and \\(\\frac{1}{4}\\) respectively. What is the probability that the problem is solved?</p>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        <p>The problem is solved if at least one student solves it. It is much easier to evaluate the complementary event that <em>none</em> of the three students solves it:</p>
        <ul>
          <li>\\(P(A') = 1 - 1/2 = 1/2\\)</li>
          <li>\\(P(B') = 1 - 1/3 = 2/3\\)</li>
          <li>\\(P(C') = 1 - 1/4 = 3/4\\)</li>
        </ul>
        Because they work independently:
        \\[ P(\\text{None solves}) = P(A') \\cdot P(B') \\cdot P(C') = \\frac{1}{2} \\times \\frac{2}{3} \\times \\frac{3}{4} = \\frac{1}{4}. \\]
        Therefore, the probability that the problem is solved is:
        \\[ P(\\text{Solved}) = 1 - P(\\text{None solves}) = 1 - \\frac{1}{4} = \\frac{3}{4}. \\]
        <strong>Answer:</strong> \\(\\frac{3}{4}\\) (or 75%).
      </div>
    </details>
  </div>
`;

// 4. REVISION TAB
const revisionHtml = `
  <h2>Quick Revision & Formula Cheat Sheet</h2>
  <div class="revision-grid">
    <div class="revision-card">
      <h4>Conditional Formulas</h4>
      <ul>
        <li>\\(P(A | B) = \\frac{P(A \\cap B)}{P(B)}\\)</li>
        <li>\\(P(A \\cap B) = P(B) \\cdot P(A | B)\\)</li>
        <li>\\(P(S | B) = 1\\)</li>
        <li>\\(P(A' | B) = 1 - P(A | B)\\)</li>
      </ul>
    </div>
    <div class="revision-card">
      <h4>Independent Events</h4>
      <ul>
        <li>\\(P(A \\cap B) = P(A) \\cdot P(B)\\)</li>
        <li>\\(P(A | B) = P(A)\\)</li>
        <li>\\(P(\\text{At least 1}) = 1 - P(A')P(B')\\dots\\)</li>
        <li>Independence implies complements are independent</li>
      </ul>
    </div>
    <div class="revision-card">
      <h4>Trap Warning</h4>
      <ul>
        <li>Mutually exclusive: \\(P(A \\cap B) = 0\\)</li>
        <li>Independent: \\(P(A \\cap B) = P(A)P(B)\\)</li>
        <li>Two non-zero events cannot be both!</li>
      </ul>
    </div>
  </div>
`;

// 5. MOCK EXAM TAB
const mockHtml = `
  <h2>10-Question Diagnostic Mock Exam</h2>
  <p class="lead-p">Test your mastery of Conditional Probability, Independent Events, and Multiplication Rules under timed CBSE conditions.</p>
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
    question: "If \\(P(A) = 0.8\\), \\(P(B) = 0.5\\), and \\(P(B | A) = 0.4\\), what is \\(P(A \\cap B)\\)?",
    options: ["0.20", "0.32", "0.40", "0.50"],
    correct: 1,
    explanation: "\\(P(A \\cap B) = P(A) \\cdot P(B | A) = 0.8 \\times 0.4 = 0.32\\)."
  },
  {
    id: 2,
    question: "Using the values from Question 1, what is \\(P(A | B)\\)?",
    options: ["0.32", "0.40", "0.64", "0.80"],
    correct: 2,
    explanation: "\\(P(A | B) = \\frac{P(A \\cap B)}{P(B)} = \\frac{0.32}{0.50} = 0.64\\)."
  },
  {
    id: 3,
    question: "If \\(A\\) and \\(B\\) are independent events with \\(P(A) = 0.3\\) and \\(P(B) = 0.4\\), what is \\(P(A \\cap B)\\)?",
    options: ["0.12", "0.58", "0.70", "0.88"],
    correct: 0,
    explanation: "For independent events: \\(P(A \\cap B) = P(A) \\cdot P(B) = 0.3 \\times 0.4 = 0.12\\)."
  },
  {
    id: 4,
    question: "For the independent events in Question 3, what is \\(P(A \\cup B)\\)?",
    options: ["0.58", "0.70", "0.82", "0.88"],
    correct: 0,
    explanation: "\\(P(A \\cup B) = P(A) + P(B) - P(A \\cap B) = 0.3 + 0.4 - 0.12 = 0.58\\)."
  },
  {
    id: 5,
    question: "If \\(P(A) = \\frac{1}{2}\\), \\(P(B) = 0\\), then \\(P(A | B)\\) is:",
    options: ["0", "\\(\\frac{1}{2}\\)", "1", "Not defined"],
    correct: 3,
    explanation: "\\(P(A | B) = \\frac{P(A \\cap B)}{P(B)}\\). Since the denominator \\(P(B) = 0\\), division by zero makes the conditional probability undefined."
  },
  {
    id: 6,
    question: "If \\(A\\) and \\(B\\) are two independent events, which of the following is FALSE?",
    options: [
      "\\(P(A | B) = P(A)\\)",
      "\\(P(B | A) = P(B)\\)",
      "\\(P(A \\cap B) = 0\\)",
      "\\(P(A' \\cap B') = P(A') P(B')\\)"
    ],
    correct: 2,
    explanation: "\\(P(A \\cap B) = 0\\) represents mutually exclusive events, not independent events (unless one event has zero probability)."
  },
  {
    id: 7,
    question: "A die is rolled. If the outcome is an even number, what is the probability that it is a prime number?",
    options: ["\\(\\frac{1}{6}\\)", "\\(\\frac{1}{3}\\)", "\\(\\frac{1}{2}\\)", "\\(\\frac{2}{3}\\)"],
    correct: 1,
    explanation: "Given event \\(B\\) (even): \\(\\{2, 4, 6\\}\\) (3 outcomes). The only even prime is 2 (1 outcome). Probability = \\(1/3\\)."
  },
  {
    id: 8,
    question: "If \\(P(A | B) = P(B | A)\\) and \\(P(A), P(B) > 0\\), then:",
    options: ["\\(A = B\\)", "\\(P(A) = P(B)\\)", "\\(A \\subseteq B\\)", "\\(A \\cap B = \\emptyset\\)"],
    correct: 1,
    explanation: "\\(\\frac{P(A \\cap B)}{P(B)} = \\frac{P(A \\cap B)}{P(A)} \\implies P(A) = P(B)\\)."
  },
  {
    id: 9,
    question: "Two cards are drawn successively without replacement from a pack of 52 cards. What is the probability that both are black cards?",
    options: ["\\(\\frac{25}{102}\\)", "\\(\\frac{1}{4}\\)", "\\(\\frac{26}{51}\\)", "\\(\\frac{1}{2}\\)"],
    correct: 0,
    explanation: "First card black: \\(26/52 = 1/2\\). Second card black given first is black: \\(25/51\\). Total = \\(1/2 \\times 25/51 = 25/102\\)."
  },
  {
    id: 10,
    question: "If \\(A\\) and \\(B\\) are independent events with \\(P(A) = 0.2\\) and \\(P(B) = 0.5\\), what is \\(P(A' \\cap B')\\)?",
    options: ["0.1", "0.3", "0.4", "0.7"],
    correct: 2,
    explanation: "\\(P(A' \\cap B') = P(A') \\cdot P(B') = (1 - 0.2)(1 - 0.5) = 0.8 \\times 0.5 = 0.40\\)."
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
    resultsBox.innerHTML += '<p style="color:#059669; font-weight:600;">Outstanding! Masterful proficiency in conditional probability, independence, and multiplication theorems.</p>';
  } else if (pct >= 50) {
    resultsBox.innerHTML += '<p style="color:#d97706; font-weight:600;">Good effort! Review the distinction between mutually exclusive and independent events.</p>';
  } else {
    resultsBox.innerHTML += '<p style="color:#dc2626; font-weight:600;">Needs revision. Study the worked examples on conditional probability and retry.</p>';
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
console.log('Successfully upgraded 9-4-conditional-probability/index.html');

