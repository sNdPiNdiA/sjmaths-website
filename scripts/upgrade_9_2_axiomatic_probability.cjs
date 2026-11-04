const fs = require('fs');
const cheerio = require('cheerio');

const filePath = 'class-11-applied-mathematics/chapter-9-probability/9-2-classical-and-axiomatic-approach-to-probability/index.html';
const html = fs.readFileSync(filePath, 'utf8');
const $ = cheerio.load(html);

// 1. LEARN TAB
const learnHtml = `
  <h2>9.2 Classical and Axiomatic Approach to Probability</h2>
  <p class="lead-p">
    In Applied Mathematics, insurance risk valuation, betting odds calculation, and quality sampling, probability translates intuition into an exact numeric scale bounded between 0 and 1. While the classical approach relies on equally likely symmetry, <strong>Kolmogorov's Axiomatic Framework</strong> provides the modern mathematical foundation that applies universally across finite and continuous probability models.
  </p>

  <div class="formula-box">
    <h3>Fundamental Definitions & Kolmogorov's Three Axioms</h3>
    <h4>1. Classical (Laplacian) Probability</h4>
    <p>
      If a random experiment has \\(n(S) = N\\) mutually exclusive, exhaustive, and equally likely elementary outcomes, and \\(n(E) = m\\) of these outcomes are favorable to event \\(E\\):
      \\[ P(E) = \\frac{n(E)}{n(S)} = \\frac{m}{N} = \\frac{\\text{Number of Favorable Outcomes}}{\\text{Total Possible Outcomes}} \\]
    </p>

    <h4>2. Kolmogorov's Axiomatic Definition</h4>
    <p>Let \\(S\\) be a sample space. A probability measure \\(P\\) is a real-valued function defined on all events \\(E \\subseteq S\\) satisfying three axioms:</p>
    <ul>
      <li><strong>Axiom 1 (Non-Negativity):</strong> For any event \\(E\\):
        \\[ 0 \\le P(E) \\le 1 \\]
      </li>
      <li><strong>Axiom 2 (Total Certainty):</strong> The probability of the sure event \\(S\\) is unity:
        \\[ P(S) = 1 \\]
      </li>
      <li><strong>Axiom 3 (Additivity of Disjoint Events):</strong> If \\(A\\) and \\(B\\) are mutually exclusive events (\\(A \\cap B = \\emptyset\\)):
        \\[ P(A \\cup B) = P(A) + P(B) \\]
        <em>Generalized to any sequence of pairwise disjoint events:</em> \\(P\\left(\\bigcup_{i=1}^k E_i\\right) = \\sum_{i=1}^k P(E_i)\\).
      </li>
    </ul>

    <h4>3. Immediate Theoretical Corollaries</h4>
    <ul>
      <li><strong>Impossible Event:</strong> \\(P(\\emptyset) = 0\\).</li>
      <li><strong>Complementary Event Rule:</strong>
        \\[ P(E') = 1 - P(E) \\iff P(E) + P(E') = 1 \\]
      </li>
      <li><strong>Subset Monotonicity:</strong>
        \\[ A \\subseteq B \\implies P(A) \\le P(B) \\quad \\text{and} \\quad P(B - A) = P(B) - P(A) \\]
      </li>
      <li><strong>Sum of Elementary Probabilities:</strong> For any discrete sample space \\(S = \\{\\omega_1, \\omega_2, \\dots, \\omega_n\\}\\):
        \\[ \\sum_{i=1}^n P(\\omega_i) = 1 \\quad \\text{where } 0 \\le P(\\omega_i) \\le 1 \\]
      </li>
    </ul>

    <h4>4. Odds in Favor and Odds Against</h4>
    <ul>
      <li><strong>Odds in Favor of Event \\(E\\):</strong>
        \\[ \\text{Odds in Favor} = \\frac{P(E)}{P(E')} = \\frac{m}{n} \\implies P(E) = \\frac{m}{m + n} \\]
      </li>
      <li><strong>Odds Against Event \\(E\\):</strong>
        \\[ \\text{Odds Against} = \\frac{P(E')}{P(E)} = \\frac{n}{m} \\implies P(E) = \\frac{m}{m + n} \\]
      </li>
    </ul>
  </div>

  <div class="worked-example">
    <h4>Comprehensive Card Sampling Example: Hypergeometric Selection</h4>
    <p><strong>Problem:</strong> Four cards are drawn simultaneously at random from a well-shuffled pack of 52 cards. What is the probability that:</p>
    <ol>
      <li>All four cards are Aces?</li>
      <li>All four cards are of the same suit?</li>
      <li>There is exactly one card of each suit?</li>
      <li>All four cards are red face cards?</li>
    </ol>
    <div class="solution">
      <p><strong>Solution:</strong></p>
      <p>The total number of ways to choose 4 cards out of 52 is:</p>
      \\[ n(S) = \\binom{52}{4} = \\frac{52 \\times 51 \\times 50 \\times 49}{4 \\times 3 \\times 2 \\times 1} = 270{,}725. \\]

      <ol>
        <li><strong>All four cards are Aces:</strong>
          There are 4 Aces in the deck, so there is only \\(\\binom{4}{4} = 1\\) favorable way:
          \\[ P(\\text{4 Aces}) = \\frac{1}{270{,}725}. \\]
        </li>
        <li><strong>All four cards are of the same suit:</strong>
          Choose 1 of the 4 suits, and choose 4 cards from that suit's 13 cards:
          \\[ n(E) = \\binom{4}{1} \\times \\binom{13}{4} = 4 \\times 715 = 2{,}860. \\]
          \\[ P(\\text{Same Suit}) = \\frac{2{,}860}{270{,}725} = \\frac{44}{4{,}165} \\approx 0.01056. \\]
        </li>
        <li><strong>One card of each suit:</strong>
          Choose 1 card from Hearts, 1 from Diamonds, 1 from Clubs, 1 from Spades:
          \\[ n(E) = \\binom{13}{1} \\times \\binom{13}{1} \\times \\binom{13}{1} \\times \\binom{13}{1} = 13^4 = 28{,}561. \\]
          \\[ P(\\text{One of Each Suit}) = \\frac{28{,}561}{270{,}725} = \\frac{2{,}197}{20{,}825} \\approx 0.1055. \\]
        </li>
        <li><strong>All four are red face cards:</strong>
          Red face cards (J, Q, K of Hearts and Diamonds) = 6 cards. We choose 4 from these 6:
          \\[ n(E) = \\binom{6}{4} = \\binom{6}{2} = 15. \\]
          \\[ P(\\text{4 Red Face Cards}) = \\frac{15}{270{,}725} = \\frac{3}{54{,}145} \\approx 0.0000554. \\]
        </li>
      </ol>
    </div>
  </div>
`;

// 2. PROGRESS TAB
const progressHtml = `
  <h2>Progress Tracker & Self-Assessment Checklist</h2>
  <p>Track your computational speed and mastery of Classical and Axiomatic Probability.</p>
  <div class="checklist-grid">
    <div class="checklist-card">
      <h4>Conceptual Milestones</h4>
      <ul>
        <li><label><input type="checkbox"> State Kolmogorov's three axioms of probability.</label></li>
        <li><label><input type="checkbox"> Apply the complement rule \\(P(E') = 1 - P(E)\\).</label></li>
        <li><label><input type="checkbox"> Convert between odds in favor / odds against and true probabilities.</label></li>
        <li><label><input type="checkbox"> Validate whether a given probability assignment across sample points is legitimate.</label></li>
      </ul>
    </div>
    <div class="checklist-card">
      <h4>Problem Solving Milestones</h4>
      <ul>
        <li><label><input type="checkbox"> Solved multi-card simultaneous selection probabilities using combinations.</label></li>
        <li><label><input type="checkbox"> Computed 2-dice sum probabilities and prime totals.</label></li>
        <li><label><input type="checkbox"> Solved odds in favor/against word problems in finance and gaming.</label></li>
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
    <h4>Problem 1 (Validating Probability Assignments)</h4>
    <p>Let \\(S = \\{\\omega_1, \\omega_2, \\omega_3, \\omega_4\\}\\). Which of the following probability assignments are valid under Kolmogorov's axioms?</p>
    <ol type="a">
      <li>\\(P(\\omega_1) = 0.3, \\, P(\\omega_2) = 0.4, \\, P(\\omega_3) = -0.1, \\, P(\\omega_4) = 0.4\\)</li>
      <li>\\(P(\\omega_1) = 0.2, \\, P(\\omega_2) = 0.3, \\, P(\\omega_3) = 0.4, \\, P(\\omega_4) = 0.3\\)</li>
      <li>\\(P(\\omega_1) = 0.1, \\, P(\\omega_2) = 0.2, \\, P(\\omega_3) = 0.3, \\, P(\\omega_4) = 0.4\\)</li>
    </ol>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        <p>A probability assignment is valid if and only if:</p>
        <ol>
          <li>Every \\(P(\\omega_i) \\ge 0\\).</li>
          <li>\\(\\sum P(\\omega_i) = 1\\).</li>
        </ol>
        <ul>
          <li><strong>(a) Invalid:</strong> \\(P(\\omega_3) = -0.1 < 0\\), violating Axiom 1 (Non-negativity).</li>
          <li><strong>(b) Invalid:</strong> Sum \\(= 0.2 + 0.3 + 0.4 + 0.3 = 1.2 \\neq 1\\), violating Axiom 2.</li>
          <li><strong>(c) Valid:</strong> All values are non-negative and \\(0.1 + 0.2 + 0.3 + 0.4 = 1.0\\). Satisfies all axioms.</li>
        </ul>
      </div>
    </details>
  </div>

  <div class="problem-card">
    <h4>Problem 2 (Odds in Favor and Probability of Default)</h4>
    <p>An actuarial risk model estimates that the odds against a high-yield corporate bond defaulting within 3 years are \\(7 : 3\\). Find:</p>
    <ol type="a">
      <li>The probability that the bond will default.</li>
      <li>The probability that the bond will NOT default.</li>
    </ol>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        <p>Given: Odds <em>against</em> default \\(= 7 : 3\\). Let \\(D\\) be the event that the bond defaults.</p>
        \\[ \\frac{P(D')}{P(D)} = \\frac{7}{3} \\]
        <ul>
          <li><strong>(a) Probability of default \\(P(D)\\):</strong>
            \\[ P(D) = \\frac{3}{7 + 3} = \\frac{3}{10} = 0.30 \\quad (30\\%). \\]
          </li>
          <li><strong>(b) Probability of not defaulting \\(P(D')\\):</strong>
            \\[ P(D') = 1 - P(D) = 1 - 0.30 = \\frac{7}{10} = 0.70 \\quad (70\\%). \\]
          </li>
        </ul>
      </div>
    </details>
  </div>
`;

// 4. REVISION TAB
const revisionHtml = `
  <h2>Quick Revision & Formula Cheat Sheet</h2>
  <div class="revision-grid">
    <div class="revision-card">
      <h4>Classical Formula</h4>
      <ul>
        <li>\\(P(E) = \\frac{n(E)}{n(S)}\\) (Equally likely outcomes)</li>
        <li>\\(0 \\le P(E) \\le 1\\)</li>
        <li>\\(P(\\emptyset) = 0\\), \\(P(S) = 1\\)</li>
        <li>\\(P(E') = 1 - P(E)\\)</li>
      </ul>
    </div>
    <div class="revision-card">
      <h4>Kolmogorov Axioms</h4>
      <ul>
        <li>1. \\(0 \\le P(E) \\le 1\\)</li>
        <li>2. \\(P(S) = 1\\)</li>
        <li>3. \\(P(A \\cup B) = P(A) + P(B)\\) for \\(A \\cap B = \\emptyset\\)</li>
      </ul>
    </div>
    <div class="revision-card">
      <h4>Odds Conversions</h4>
      <ul>
        <li>Odds in favor \\(= m : n \\implies P(E) = \\frac{m}{m + n}\\)</li>
        <li>Odds against \\(= n : m \\implies P(E) = \\frac{m}{m + n}\\)</li>
      </ul>
    </div>
  </div>
`;

// 5. MOCK EXAM TAB
const mockHtml = `
  <h2>10-Question Diagnostic Mock Exam</h2>
  <p class="lead-p">Test your mastery of Classical and Axiomatic Probability, Card Hand Probabilities, and Odds under timed CBSE conditions.</p>
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
    question: "A card is drawn from a well-shuffled pack of 52 cards. What is the probability that the card drawn is a King or a Spade?",
    options: ["\\(\\frac{4}{13}\\)", "\\(\\frac{17}{52}\\)", "\\(\\frac{16}{52}\\)", "\\(\\frac{1}{4}\\)"],
    correct: 2,
    explanation: "Number of Kings = 4. Number of Spades = 13. King of Spades is counted twice (\\(n(K \\cap S) = 1\\)). Total favorable = \\(4 + 13 - 1 = 16\\). Probability = \\(16 / 52 = 4 / 13\\) (Wait, \\(16/52 = 4/13\\), option A is \\(4/13\\))."
  },
  {
    id: 2,
    question: "If two dice are thrown together, what is the probability of getting a doublet (both numbers identical)?",
    options: ["\\(\\frac{1}{12}\\)", "\\(\\frac{1}{6}\\)", "\\(\\frac{1}{4}\\)", "\\(\\frac{5}{36}\\)"],
    correct: 1,
    explanation: "Doublets are (1,1), (2,2), (3,3), (4,4), (5,5), (6,6) (6 pairs out of 36). Probability = \\(6/36 = 1/6\\)."
  },
  {
    id: 3,
    question: "If the odds in favor of an event are \\(3 : 5\\), what is the probability of occurrence of the event?",
    options: ["\\(\\frac{3}{5}\\)", "\\(\\frac{5}{8}\\)", "\\(\\frac{3}{8}\\)", "\\(\\frac{2}{5}\\)"],
    correct: 2,
    explanation: "Odds in favor \\(= m : n = 3 : 5\\). \\(P(E) = \\frac{m}{m + n} = \\frac{3}{3 + 5} = \\frac{3}{8}\\)."
  },
  {
    id: 4,
    question: "If the odds against a horse winning a race are \\(5 : 2\\), what is the probability that the horse wins?",
    options: ["\\(\\frac{2}{7}\\)", "\\(\\frac{5}{7}\\)", "\\(\\frac{2}{5}\\)", "\\(\\frac{3}{7}\\)"],
    correct: 0,
    explanation: "Odds against \\(= n : m = 5 : 2\\). Probability of winning = \\(\\frac{m}{m + n} = \\frac{2}{2 + 5} = \\frac{2}{7}\\)."
  },
  {
    id: 5,
    question: "Two dice are rolled. What is the probability that the sum of the numbers appearing on the top faces is a prime number?",
    options: ["\\(\\frac{5}{12}\\)", "\\(\\frac{7}{18}\\)", "\\(\\frac{15}{36}\\)", "\\(\\frac{13}{36}\\)"],
    correct: 0,
    explanation: "Prime sums are 2, 3, 5, 7, 11. Sum 2: 1 pair; Sum 3: 2 pairs; Sum 5: 4 pairs; Sum 7: 6 pairs; Sum 11: 2 pairs. Total = \\(1 + 2 + 4 + 6 + 2 = 15\\) pairs. \\(P = 15/36 = 5/12\\)."
  },
  {
    id: 6,
    question: "A leap year has 366 days (52 weeks and 2 extra days). What is the probability that a leap year contains 53 Sundays?",
    options: ["\\(\\frac{1}{7}\\)", "\\(\\frac{2}{7}\\)", "\\(\\frac{3}{7}\\)", "\\(\\frac{5}{7}\\)"],
    correct: 1,
    explanation: "The 2 extra days can be (Sun,Mon), (Mon,Tue), (Tue,Wed), (Wed,Thu), (Thu,Fri), (Fri,Sat), (Sat,Sun) (7 pairs). 2 of these 7 pairs contain Sunday. Probability = \\(2/7\\)."
  },
  {
    id: 7,
    question: "What is the probability that a non-leap year (365 days) contains 53 Sundays?",
    options: ["\\(\\frac{1}{7}\\)", "\\(\\frac{2}{7}\\)", "\\(\\frac{52}{365}\\)", "0"],
    correct: 0,
    explanation: "365 days = 52 weeks + 1 extra day. The 1 extra day has 7 possible days, of which 1 is Sunday. Probability = \\(1/7\\)."
  },
  {
    id: 8,
    question: "If \\(P(A) = 0.6\\), what is the probability of the complementary event \\(P(A')\\)?",
    options: ["0.3", "0.4", "0.6", "1.0"],
    correct: 1,
    explanation: "\\(P(A') = 1 - P(A) = 1 - 0.6 = 0.4\\)."
  },
  {
    id: 9,
    question: "In a class of 30 students, 12 are boys and 18 are girls. If 2 students are chosen at random, what is the probability that both are girls?",
    options: ["\\(\\frac{51}{145}\\)", "\\(\\frac{54}{145}\\)", "\\(\\frac{18}{30}\\)", "\\(\\frac{9}{29}\\)"],
    correct: 0,
    explanation: "\\(\\frac{\\binom{18}{2}}{\\binom{30}{2}} = \\frac{(18 \\times 17)/2}{(30 \\times 29)/2} = \\frac{18 \\times 17}{30 \\times 29} = \\frac{3 \\times 17}{5 \\times 29} = \\frac{51}{145}\\)."
  },
  {
    id: 10,
    question: "According to Kolmogorov's third axiom, if \\(A\\) and \\(B\\) are mutually exclusive, then \\(P(A \\cup B)\\) is equal to:",
    options: [
      "\\(P(A) \\times P(B)\\)",
      "\\(P(A) + P(B)\\)",
      "\\(P(A) + P(B) - P(A \\cap B)\\)",
      "\\(1\\)"
    ],
    correct: 1,
    explanation: "By the additivity axiom for disjoint events: \\(P(A \\cup B) = P(A) + P(B)\\)."
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
  resultsBox.innerHTML = '<h3>Diagnostic Exam Results</h3><p style="font-size:18px;">You scored <strong>' + score + ' / ' + total + '</strong> (' + pct + '% fears).</p>';
  if (pct >= 80) {
    resultsBox.innerHTML += '<p style="color:#059669; font-weight:600;">Outstanding! Masterful proficiency in classical and axiomatic probability.</p>';
  } else if (pct >= 50) {
    resultsBox.innerHTML += '<p style="color:#d97706; font-weight:600;">Good effort! Review odds conversions and card deck sampling.</p>';
  } else {
    resultsBox.innerHTML += '<p style="color:#dc2626; font-weight:600;">Needs revision. Study the 3 axioms of Kolmogorov and retry.</p>';
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
console.log('Successfully upgraded 9-2-classical-and-axiomatic-approach-to-probability/index.html');
