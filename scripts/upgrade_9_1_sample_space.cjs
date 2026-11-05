const fs = require('fs');
const cheerio = require('cheerio');

const filePath = 'class-11-applied-mathematics/chapter-9-probability/9-1-random-experiments-and-sample-space/index.html';
const html = fs.readFileSync(filePath, 'utf8');
const $ = cheerio.load(html);

// 1. LEARN TAB
const learnHtml = `
  <h2>9.1 Random Experiments, Sample Space, and Event Algebra</h2>
  <p class="lead-p">
    In Applied Mathematics, financial risk engineering, actuarial science, and quality control, decision-making occurs under conditions of uncertainty. Probability begins by establishing a rigorous set-theoretic sample space containing all conceivable outcomes of a <strong>random experiment</strong>.
  </p>

  <div class="formula-box">
    <h3>Fundamental Definitions & Set-Theoretic Axioms</h3>
    <ul>
      <li><strong>Random Experiment:</strong> An experiment is random if:
        <ol>
          <li>It has more than one possible outcome.</li>
          <li>It is impossible to predict the exact outcome in advance with complete certainty.</li>
        </ol>
      </li>
      <li><strong>Sample Space (\\(S\\)):</strong> The set of all possible elementary outcomes of a random experiment:
        \\[ S = \\{ \\omega_1, \\omega_2, \\dots, \\omega_n \\} \\]
      </li>
      <li><strong>Event (\\(E\\)):</strong> Any subset of the sample space \\(S\\):
        \\[ E \\subseteq S \\]
      </li>
      <li><strong>Taxonomy of Events:</strong>
        <ul>
          <li><strong>Impossible Event:</strong> The empty set \\(\\emptyset\\) (cannot occur).</li>
          <li><strong>Sure (Certain) Event:</strong> The entire sample space \\(S\\) (guaranteed to occur).</li>
          <li><strong>Simple (Elementary) Event:</strong> A subset containing exactly one sample point \\(\\{\\omega_i\\}\\).</li>
          <li><strong>Compound Event:</strong> A subset containing two or more distinct sample points.</li>
        </ul>
      </li>
      <li><strong>Mutually Exclusive Events:</strong> Events \\(A\\) and \\(B\\) are mutually exclusive (disjoint) if their simultaneous occurrence is impossible:
        \\[ A \\cap B = \\emptyset \\]
      </li>
      <li><strong>Exhaustive Events:</strong> Events \\(E_1, E_2, \\dots, E_k\\) are exhaustive if their union constitutes the entire sample space:
        \\[ E_1 \\cup E_2 \\cup \\dots \\cup E_k = S \\]
      </li>
    </ul>
  </div>

  <h3>Standard Benchmark Sample Spaces in Applied Mathematics</h3>
  <table class="table-styled">
    <thead>
      <tr>
        <th>Experiment</th>
        <th>Sample Space \\(S\\)</th>
        <th>Total Cardinality \\(n(S)\\)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Tossing \\(n\\) Coins</strong></td>
        <td>\\(\\{ (x_1, x_2, \\dots, x_n) : x_i \\in \\{H, T\\} \\}\\)</td>
        <td>\\(2^n\\) (e.g. \\(n=3 \\implies 2^3 = 8\\))</td>
      </tr>
      <tr>
        <td><strong>Throwing 2 Fair Dice</strong></td>
        <td>\\(\\{ (i, j) : i, j \\in \\{1, 2, 3, 4, 5, 6\\} \\}\\)</td>
        <td>\\(6^2 = 36\\) ordered pairs</td>
      </tr>
      <tr>
        <td><strong>Drawing from a Standard 52-Card Deck</strong></td>
        <td>4 Suits: Hearts, Diamonds (Red = 26); Clubs, Spades (Black = 26)</td>
        <td>52 cards (12 Face cards: J, Q, K; 4 Aces)</td>
      </tr>
      <tr>
        <td><strong>Manufacturing Quality Inspection</strong></td>
        <td>Testing 3 consecutive items for Defective (\\(D\\)) or Non-defective (\\(N\\))</td>
        <td>\\(2^3 = 8\\) outcome sequences</td>
      </tr>
    </tbody>
  </table>

  <div class="worked-example">
    <h4>Comprehensive Applied Example: Industrial Quality Control Sampling</h4>
    <p><strong>Scenario:</strong> A quality assurance inspector examines 3 components selected at random from an assembly line. Each component is classified as either <strong>Defective (\\(D\\))</strong> or <strong>Non-Defective (\\(N\\))</strong>.</p>
    <ol>
      <li>Write down the complete sample space \\(S\\).</li>
      <li>Define event \\(A\\): "Exactly one component is defective".</li>
      <li>Define event \\(B\\): "At least two components are defective".</li>
      <li>Define event \\(C\\): "No component is defective".</li>
      <li>Determine whether \\(A\\) and \\(B\\) are mutually exclusive. Are \\(A, B, C\\) exhaustive?</li>
    </ol>
    <div class="solution">
      <p><strong>Solution:</strong></p>
      <ol>
        <li><strong>Sample Space:</strong>
          \\[ S = \\{ NNN, \\, NND, \\, NDN, \\, DNN, \\, NDD, \\, DND, \\, DDN, \\, DDD \\}, \\quad n(S) = 8. \\]
        </li>
        <li><strong>Event \\(A\\) (Exactly 1 defective):</strong>
          \\[ A = \\{ NND, NDN, DNN \\}, \\quad n(A) = 3. \\]
        </li>
        <li><strong>Event \\(B\\) (At least 2 defective):</strong>
          \\[ B = \\{ NDD, DND, DDN, DDD \\}, \\quad n(B) = 4. \\]
        </li>
        <li><strong>Event \\(C\\) (No defective component):</strong>
          \\[ C = \\{ NNN \\}, \\quad n(C) = 1. \\]
        </li>
        <li><strong>Mutually Exclusive & Exhaustive Verification:</strong>
          <ul>
            <li>\\(A \\cap B = \\emptyset\\). Since they share no common sample points, <strong>\\(A\\) and \\(B\\) are mutually exclusive</strong>.</li>
            <li>\\(A \\cup B \\cup C = \\{ NND, NDN, DNN, NDD, DND, DDN, DDD, NNN \\} = S\\).</li>
            <li>Because their union equals \\(S\\) and their pairwise intersections are empty, the events \\(A, B, C\\) form a <strong>mutually exclusive and exhaustive partition</strong> of \\(S\\).</li>
          </ul>
        </li>
      </ol>
    </div>
  </div>
`;

// 2. PROGRESS TAB
const progressHtml = `
  <h2>Progress Tracker & Self-Assessment Checklist</h2>
  <p>Track your conceptual mastery and diagnostic skills across Sample Spaces and Event Algebra.</p>
  <div class="checklist-grid">
    <div class="checklist-card">
      <h4>Conceptual Milestones</h4>
      <ul>
        <li><label><input type="checkbox"> Define a random experiment and construct its formal sample space \\(S\\).</label></li>
        <li><label><input type="checkbox"> Classify events into elementary, compound, impossible, and certain.</label></li>
        <li><label><input type="checkbox"> Apply set operations: union (OR), intersection (AND), and complement (NOT).</label></li>
        <li><label><input type="checkbox"> Test sets of events for mutual exclusivity and exhaustiveness.</label></li>
      </ul>
    </div>
    <div class="checklist-card">
      <h4>Problem Solving Milestones</h4>
      <ul>
        <li><label><input type="checkbox"> Constructed multi-stage coin and die sample spaces.</label></li>
        <li><label><input type="checkbox"> Evaluated 2-dice sum events and card deck partition events.</label></li>
        <li><label><input type="checkbox"> Verified mutually exclusive and exhaustive partitions in industrial testing.</label></li>
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
    <h4>Problem 1 (Two-Dice Event Space)</h4>
    <p>Two fair dice are thrown. Describe the following events in roster form:</p>
    <ol type="a">
      <li>\\(A\\): The sum of the numbers on the dice is greater than 8.</li>
      <li>\\(B\\): 2 occurs on either die.</li>
      <li>\\(C\\): The sum is at least 7 and a multiple of 3.</li>
      <li>Are \\(A\\) and \\(B\\) mutually exclusive?</li>
    </ol>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        <p>The sample space \\(S\\) consists of \\(6 \\times 6 = 36\\) pairs \\((i, j)\\).</p>
        <ul>
          <li><strong>(a) Event \\(A\\) (Sum > 8, so sums 9, 10, 11, 12):</strong>
            \\[ A = \\{ (3,6), (4,5), (5,4), (6,3), (4,6), (5,5), (6,4), (5,6), (6,5), (6,6) \\}, \\quad n(A) = 10. \\]
          </li>
          <li><strong>(b) Event \\(B\\) (2 occurs on either die):</strong>
            \\[ B = \\{ (2,1), (2,2), (2,3), (2,4), (2,5), (2,6), (1,2), (3,2), (4,2), (5,2), (6,2) \\}, \\quad n(B) = 11. \\]
          </li>
          <li><strong>(c) Event \\(C\\) (Sum \\(\\ge 7\\) and multiple of 3, so sums 9 or 12):</strong>
            \\[ C = \\{ (3,6), (4,5), (5,4), (6,3), (6,6) \\}, \\quad n(C) = 5. \\]
          </li>
          <li><strong>(d) Mutual Exclusivity of \\(A\\) and \\(B\\):</strong>
            Look for common pairs in \\(A\\) and \\(B\\). The maximum sum achievable with a 2 is \\((2, 6) = 8\\). But event \\(A\\) requires sum > 8.
            Hence \\(A \\cap B = \\emptyset\\).
            <strong>Yes, \\(A\\) and \\(B\\) are mutually exclusive.</strong>
          </li>
        </ul>
      </div>
    </details>
  </div>

  <div class="problem-card">
    <h4>Problem 2 (Tree Diagram Sample Space: Coin and Die)</h4>
    <p>A coin is tossed. If it shows Head, a die is thrown; if it shows Tail, the coin is tossed again. Write down the sample space.</p>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        <p>Using a probability tree structure:</p>
        <ul>
          <li>Branch 1 (Head on first toss): Followed by a die throw yielding \\(1, 2, 3, 4, 5, 6\\). Outcomes:
            \\[ (H, 1), (H, 2), (H, 3), (H, 4), (H, 5), (H, 6) \\]
          </li>
          <li>Branch 2 (Tail on first toss): Followed by a second coin toss yielding \\(H\\) or \\(T\\). Outcomes:
            \\[ (T, H), (T, T) \\]
          </li>
        </ul>
        <strong>Complete Sample Space:</strong>
        \\[ S = \\{ (H, 1), (H, 2), (H, 3), (H, 4), (H, 5), (H, 6), (T, H), (T, T) \\}, \\quad n(S) = 8. \\]
      </div>
    </details>
  </div>
`;

// 4. REVISION TAB
const revisionHtml = `
  <h2>Quick Revision & Formula Cheat Sheet</h2>
  <div class="revision-grid">
    <div class="revision-card">
      <h4>Core Definitions</h4>
      <ul>
        <li>Sample space \\(S\\): Set of all possible outcomes</li>
        <li>Event \\(E \\subseteq S\\)</li>
        <li>Impossible: \\(\\emptyset\\)</li>
        <li>Sure/Certain: \\(S\\)</li>
      </ul>
    </div>
    <div class="revision-card">
      <h4>Event Algebra</h4>
      <ul>
        <li>Complement: \\(A' = S - A\\)</li>
        <li>Union: \\(A \\cup B\\) (Event \\(A\\) OR \\(B\\))</li>
        <li>Intersection: \\(A \\cap B\\) (Event \\(A\\) AND \\(B\\))</li>
        <li>Difference: \\(A - B = A \\cap B'\\) (\\(A\\) but not \\(B\\))</li>
      </ul>
    </div>
    <div class="revision-card">
      <h4>Partition Conditions</h4>
      <ul>
        <li>Mutually Exclusive: \\(A \\cap B = \\emptyset\\)</li>
        <li>Exhaustive: \\(\\bigcup E_i = S\\)</li>
        <li>Partition: Disjoint and exhaustive simultaneously</li>
      </ul>
    </div>
  </div>
`;

// 5. MOCK EXAM TAB
const mockHtml = `
  <h2>10-Question Diagnostic Mock Exam</h2>
  <p class="lead-p">Test your mastery of Sample Spaces, Event Classifications, and Mutual Exclusivity under timed CBSE conditions.</p>
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
    question: "What is the total number of outcomes in the sample space when 3 coins are tossed simultaneously?",
    options: ["6", "8", "9", "16"],
    correct: 1,
    explanation: "\\(2^3 = 8\\) outcomes: \\(\\{HHH, HHT, HTH, HTT, THH, THT, TTH, TTT\\}\\)."
  },
  {
    id: 2,
    question: "When two fair dice are thrown simultaneously, how many outcomes result in a sum equal to 7?",
    options: ["4", "5", "6", "7"],
    correct: 2,
    explanation: "The pairs are (1,6), (2,5), (3,4), (4,3), (5,2), (6,1). There are 6 pairs."
  },
  {
    id: 3,
    question: "Two events \\(A\\) and \\(B\\) are mutually exclusive if and only if:",
    options: [
      "\\(A \\cup B = S\\)",
      "\\(A \\cap B = \\emptyset\\)",
      "\\(A \\subseteq B\\)",
      "\\(A' = B\\)"
    ],
    correct: 1,
    explanation: "Mutually exclusive events cannot occur simultaneously, meaning their intersection is empty: \\(A \\cap B = \\emptyset\\)."
  },
  {
    id: 4,
    question: "If \\(E_1, E_2, \\dots, E_k\\) are exhaustive events in sample space \\(S\\), then:",
    options: [
      "\\(E_1 \\cap E_2 \\cap \\dots = \\emptyset\\)",
      "\\(E_1 \\cup E_2 \\cup \\dots \\cup E_k = S\\)",
      "\\(n(E_i) = n(S)/k\\)",
      "\\(E_i \\cap E_j \\neq \\emptyset\\)"
    ],
    correct: 1,
    explanation: "Events are exhaustive if their union spans the entire sample space \\(S\\)."
  },
  {
    id: 5,
    question: "In drawing a single card from a 52-card deck, how many elementary outcomes correspond to drawing a face card?",
    options: ["4", "12", "13", "16"],
    correct: 1,
    explanation: "There are 3 face cards (J, Q, K) per suit across 4 suits: \\(3 \\times 4 = 12\\) face cards."
  },
  {
    id: 6,
    question: "Which of the following represents an impossible event?",
    options: [
      "Getting a sum of 12 with two dice",
      "Getting an odd number on a die",
      "Getting a sum of 13 with two standard dice",
      "Drawing a red Queen from a deck"
    ],
    correct: 2,
    explanation: "The maximum possible sum on two standard six-sided dice is \\(6 + 6 = 12\\), so a sum of 13 is an impossible event (\\(\\emptyset\\))."
  },
  {
    id: 7,
    question: "Let \\(S = \\{1, 2, 3, 4, 5, 6\\}\\). If \\(A = \\{2, 4, 6\\}\\) and \\(B = \\{1, 2, 3\\}\\), what is \\(A - B\\)?",
    options: ["\\(\\{2\\}\\)", "\\(\\{4, 6\\}\\)", "\\(\\{1, 3\\}\\)", "\\(\\{1, 2, 3, 4, 6\\}\\)"],
    correct: 1,
    explanation: "\\(A - B = A \\cap B'\\) contains elements in \\(A\\) that are not in \\(B\\): \\(\\{4, 6\\}\\)."
  },
  {
    id: 8,
    question: "An experiment consists of rolling a die until a 6 appears. The sample space for this experiment is:",
    options: [
      "Finite with 6 outcomes",
      "Finite with 36 outcomes",
      "Countably infinite",
      "Continuous"
    ],
    correct: 2,
    explanation: "A 6 could appear on toss 1, toss 2, ..., toss \\(k\\), without an upper bound. The sample space is countably infinite."
  },
  {
    id: 9,
    question: "If \\(A\\) and \\(B\\) are two mutually exclusive events such that \\(A \\cup B = S\\), then:",
    options: ["\\(B = A'\\)", "\\(A = B\\)", "\\(A \\cap B \\neq \\emptyset\\)", "\\(A = \\emptyset\\)"],
    correct: 0,
    explanation: "If \\(A \\cap B = \\emptyset\\) and \\(A \\cup B = S\\), then \\(B\\) is the exact complement of \\(A\\): \\(B = A'\\)."
  },
  {
    id: 10,
    question: "An elementary event is an event that contains:",
    options: [
      "No outcomes",
      "Exactly one sample point",
      "All sample points",
      "At least two sample points"
    ],
    correct: 1,
    explanation: "An elementary (or simple) event contains exactly one sample point \\(\\{\\omega\\}\\)."
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
    resultsBox.innerHTML += '<p style="color:#059669; font-weight:600;">Outstanding! Masterful proficiency in sample spaces, event algebra, and partition testing.</p>';
  } else if (pct >= 50) {
    resultsBox.innerHTML += '<p style="color:#d97706; font-weight:600;">Good effort! Review the definitions of mutually exclusive vs exhaustive events.</p>';
  } else {
    resultsBox.innerHTML += '<p style="color:#dc2626; font-weight:600;">Needs revision. Study the worked examples on sample spaces and retry.</p>';
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
console.log('Successfully upgraded 9-1-random-experiments-and-sample-space/index.html');

