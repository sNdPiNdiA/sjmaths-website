const fs = require('fs');
const cheerio = require('cheerio');

const filePath = 'class-11-applied-mathematics/chapter-8-combinatorics/8-1-fundamental-principles-of-counting/index.html';
const html = fs.readFileSync(filePath, 'utf8');
const $ = cheerio.load(html);

// 1. LEARN TAB
const learnHtml = `
  <h2>8.1 Fundamental Principles of Counting: Multiplication and Addition Rules</h2>
  <p class="lead-p">
    In Applied Mathematics, cybersecurity, operations research, and logistics design, combinatorial counting provides the mathematical rigor to quantify possibility spaces. The <strong>Fundamental Principle of Counting (FPC)</strong> allows analysts to count millions of combinations systematically without laborious listing.
  </p>

  <div class="formula-box">
    <h3>Fundamental Counting Axioms & Logic</h3>
    <ul>
      <li><strong>Fundamental Principle of Multiplication (The "AND" Rule):</strong>
        If an event \\(E_1\\) can occur in \\(m\\) distinct ways, and following its occurrence, a second independent/dependent event \\(E_2\\) can occur in \\(n\\) distinct ways, then the combined sequence of events \\(E_1\\) <strong>AND</strong> \\(E_2\\) can occur in:
        \\[ \\text{Total Ways} = m \\times n \\]
        <em>Generalized to \\(k\\) stages:</em> \\(n_1 \\times n_2 \\times n_3 \\times \\dots \\times n_k\\).
      </li>
      <li><strong>Fundamental Principle of Addition (The "OR" Rule):</strong>
        If an event can occur in \\(m\\) distinct ways and another mutually exclusive alternative event can occur in \\(n\\) distinct ways (neither can occur simultaneously), then either the first <strong>OR</strong> the second event can occur in:
        \\[ \\text{Total Ways} = m + n \\]
      </li>
      <li><strong>Repetition vs Non-Repetition:</strong>
        When forming \\(r\\)-length codes from \\(n\\) available distinct symbols:
        \\[ \\text{With Repetition Allowed} = n^r \\]
        \\[ \\text{Without Repetition (Strictly Distinct)} = n(n - 1)(n - 2)\\dots(n - r + 1) \\]
      </li>
      <li><strong>The Leading Zero Rule:</strong>
        In forming an \\(r\\)-digit positive integer, the most significant (leftmost) digit <strong>cannot be 0</strong>.
      </li>
    </ul>
  </div>

  <h3>Systematic Box-Filling Method for Constrained Number Formation</h3>
  <ol>
    <li><strong>Identify the Restrictive Positions First:</strong>
      <ul>
        <li>For <strong>Even numbers:</strong> The units place must be 0, 2, 4, 6, or 8.</li>
        <li>For <strong>Odd numbers:</strong> The units place must be 1, 3, 5, 7, or 9.</li>
        <li>For <strong>Numbers divisible by 5:</strong> The units place must be 0 or 5.</li>
        <li>For <strong>Numbers greater than \\(K\\):</strong> The leading digit is restricted to digits \\(\\ge\\) the leading digit of \\(K\\).</li>
      </ul>
    </li>
    <li><strong>Handle the Zero Dilemma:</strong> If 0 is among the allowed digits and units digit requires 0, split the problem into mutually exclusive cases (e.g. Case 1: Units digit is 0; Case 2: Units digit is non-zero even).</li>
    <li><strong>Fill Remaining Slots:</strong> Fill remaining positions using the Multiplication Principle, accounting for repetition constraints.</li>
    <li><strong>Aggregate Cases:</strong> Sum the counts from mutually exclusive cases using the Addition Principle.</li>
  </ol>

  <div class="worked-example">
    <h4>Comprehensive Worked Example: 4-Digit Number Formation with Restraints</h4>
    <p><strong>Problem:</strong> How many 4-digit even numbers can be formed using the digits \\(\\{0, 1, 2, 3, 4, 5\\}\\) if:</p>
    <ol>
      <li>Repetition of digits is allowed?</li>
      <li>Repetition of digits is NOT allowed?</li>
    </ol>
    <div class="solution">
      <p><strong>Solution:</strong></p>
      <p>A 4-digit number has four positions: [Thousands] [Hundreds] [Tens] [Units].</p>

      <p><strong>Case 1: Repetition is Allowed:</strong></p>
      <ul>
        <li><strong>Thousands place:</strong> Can take any digit from \\(\\{1, 2, 3, 4, 5\\}\\) (0 is excluded). Total choices = <strong>5</strong>.</li>
        <li><strong>Hundreds place:</strong> Can take any digit from \\(\\{0, 1, 2, 3, 4, 5\\}\\). Total choices = <strong>6</strong>.</li>
        <li><strong>Tens place:</strong> Can take any digit from \\(\\{0, 1, 2, 3, 4, 5\\}\\). Total choices = <strong>6</strong>.</li>
        <li><strong>Units place:</strong> Must be even: \\(\\{0, 2, 4\\}\\). Total choices = <strong>3</strong>.</li>
      </ul>
      By the Multiplication Principle:
      \\[ \\text{Total Numbers} = 5 \\times 6 \\times 6 \\times 3 = 540 \\text{ numbers.} \\]

      <p><strong>Case 2: Repetition is NOT Allowed:</strong></p>
      <p>Since 0 affects both the thousands place (cannot be 0) and the units place (makes it even), we split into two mutually exclusive sub-cases:</p>
      <ul>
        <li><strong>Sub-case 2A: Units digit is 0:</strong>
          <ul>
            <li>Units place = 1 choice (fixed as 0).</li>
            <li>Thousands place = 5 choices (any from \\(\\{1, 2, 3, 4, 5\\}\\)).</li>
            <li>Hundreds place = 4 choices (from remaining 4 non-zero digits).</li>
            <li>Tens place = 3 choices (from remaining 3 non-zero digits).</li>
            <li>Total for Sub-case 2A = \\(5 \\times 4 \\times 3 \\times 1 = 60\\).</li>
          </ul>
        </li>
        <li><strong>Sub-case 2B: Units digit is non-zero even (2 or 4):</strong>
          <ul>
            <li>Units place = 2 choices (either 2 or 4).</li>
            <li>Thousands place = Cannot be 0, and cannot be the digit used in units place. Out of 6 digits, 2 are unavailable, leaving <strong>4</strong> choices.</li>
            <li>Hundreds place = Out of 6 digits, 2 are used, leaving <strong>4</strong> choices (0 is now available).</li>
            <li>Tens place = Out of 6 digits, 3 are used, leaving <strong>3</strong> choices.</li>
            <li>Total for Sub-case 2B = \\(4 \\times 4 \\times 3 \\times 2 = 96\\).</li>
          </ul>
        </li>
      </ul>
      By the Addition Principle, total numbers without repetition:
      \\[ \\text{Total} = 60 + 96 = 156 \\text{ numbers.} \\]
    </div>
  </div>
`;

// 2. PROGRESS TAB
const progressHtml = `
  <h2>Progress Tracker & Self-Assessment Checklist</h2>
  <p>Track your computational speed and mastery of Fundamental Counting Principles.</p>
  <div class="checklist-grid">
    <div class="checklist-card">
      <h4>Conceptual Milestones</h4>
      <ul>
        <li><label><input type="checkbox"> Correctly distinguish when to multiply (AND) and when to add (OR).</label></li>
        <li><label><input type="checkbox"> Master the box-filling method for sequential decision slots.</label></li>
        <li><label><input type="checkbox"> Handle leading zero restrictions in multi-digit numbers.</label></li>
        <li><label><input type="checkbox"> Partition complex digit constraints into disjoint mutually exclusive cases.</label></li>
      </ul>
    </div>
    <div class="checklist-card">
      <h4>Problem Solving Milestones</h4>
      <ul>
        <li><label><input type="checkbox"> Solved PIN code and password space enumeration problems.</label></li>
        <li><label><input type="checkbox"> Solved even/odd and divisibility-by-5 constrained number problems.</label></li>
        <li><label><input type="checkbox"> Computed routing paths and menu selection possibilities.</label></li>
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
    <h4>Problem 1 (ATM PIN Code Space Analysis)</h4>
    <p>A banking system generates 4-digit numeric ATM PINs using digits \\(0\\) to \\(9\\). Find the total number of PINs possible if:</p>
    <ol type="a">
      <li>Any digit can be repeated freely.</li>
      <li>All 4 digits must be distinct.</li>
      <li>The PIN must start with a non-zero digit and all digits must be distinct.</li>
    </ol>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        <p>Note: Unlike standard multi-digit numbers, ATM PINs CAN begin with 0 unless explicitly forbidden.</p>
        <ul>
          <li><strong>(a) Free Repetition:</strong> Each of the 4 slots has 10 options:
            \\[ 10 \\times 10 \\times 10 \\times 10 = 10^4 = 10{,}000 \\text{ PINs.} \\]
          </li>
          <li><strong>(b) All 4 digits distinct:</strong>
            \\[ 10 \\times 9 \\times 8 \\times 7 = 5{,}040 \\text{ PINs.} \\]
          </li>
          <li><strong>(c) Non-zero start & distinct:</strong>
            Slot 1 has 9 choices (1-9). Slot 2 has 9 choices (0 allowed, excluding slot 1). Slot 3 has 8 choices. Slot 4 has 7 choices.
            \\[ 9 \\times 9 \\times 8 \\times 7 = 4{,}536 \\text{ PINs.} \\]
          </li>
        </ul>
      </div>
    </details>
  </div>

  <div class="problem-card">
    <h4>Problem 2 (Threshold Inequality: Numbers Greater than 5000)</h4>
    <p>How many numbers greater than 5000 can be formed using the digits \\(\\{2, 4, 5, 7, 8\\}\\) without repetition?</p>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        <p>Any valid number can either be a 4-digit number (starting with 5, 7, or 8) OR a 5-digit number (since all 5-digit numbers from these positive digits exceed 5000).</p>
        <p><strong>Case 1: 4-digit numbers > 5000:</strong></p>
        <ul>
          <li>Thousands place: 3 choices (\\(\\{5, 7, 8\\}\\)).</li>
          <li>Hundreds place: 4 remaining choices.</li>
          <li>Tens place: 3 remaining choices.</li>
          <li>Units place: 2 remaining choices.</li>
          <li>Total 4-digit = \\(3 \\times 4 \\times 3 \\times 2 = 72\\).</li>
        </ul>
        <p><strong>Case 2: 5-digit numbers:</strong></p>
        <ul>
          <li>All 5 digits are used: \\(5 \\times 4 \\times 3 \\times 2 \\times 1 = 120\\).</li>
        </ul>
        <p>By the Addition Principle:</p>
        \\[ \\text{Total Numbers} = 72 + 120 = 192 \\text{ numbers.} \\]
      </div>
    </details>
  </div>

  <div class="problem-card">
    <h4>Problem 3 (Flag Signaling Combinations)</h4>
    <p>Given 5 flags of different colors, how many different signals can be generated if each signal requires the use of at least 2 flags, one below the other?</p>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        <p>Signals can use 2, 3, 4, or 5 flags:</p>
        <ul>
          <li>2-flag signals: \\(5 \\times 4 = 20\\)</li>
          <li>3-flag signals: \\(5 \\times 4 \\times 3 = 60\\)</li>
          <li>4-flag signals: \\(5 \\times 4 \\times 3 \\times 2 = 120\\)</li>
          <li>5-flag signals: \\(5 \\times 4 \\times 3 \\times 2 \\times 1 = 120\\)</li>
        </ul>
        By the Addition Principle:
        \\[ \\text{Total Signals} = 20 + 60 + 120 + 120 = 320 \\text{ signals.} \\]
      </div>
    </details>
  </div>
`;

// 4. REVISION TAB
const revisionHtml = `
  <h2>Quick Revision & Formula Cheat Sheet</h2>
  <div class="revision-grid">
    <div class="revision-card">
      <h4>Counting Principles</h4>
      <ul>
        <li><strong>Multiplication (AND):</strong> Sequential tasks \\(= n_1 \\times n_2 \\times \\dots\\)</li>
        <li><strong>Addition (OR):</strong> Mutually exclusive cases \\(= n_1 + n_2 + \\dots\\)</li>
        <li>With repetition: \\(n^r\\)</li>
        <li>Without repetition: \\(n(n-1)(n-2)\\dots(n-r+1)\\)</li>
      </ul>
    </div>
    <div class="revision-card">
      <h4>Digit Rules</h4>
      <ul>
        <li>Multi-digit numbers cannot have 0 as the leading digit</li>
        <li>Even: Units digit \\(\\in \\{0, 2, 4, 6, 8\\}\\)</li>
        <li>Odd: Units digit \\(\\in \\{1, 3, 5, 7, 9\\}\\)</li>
        <li>Divisible by 5: Units digit \\(\\in \\{0, 5\\}\\)</li>
      </ul>
    </div>
    <div class="revision-card">
      <h4>Strategy Framework</h4>
      <ul>
        <li>1. Fill constrained positions first</li>
        <li>2. Split zero-dependent parity into disjoint cases</li>
        <li>3. Multiply across sequential slots</li>
        <li>4. Add across independent alternative scenarios</li>
      </ul>
    </div>
  </div>
`;

// 5. MOCK EXAM TAB
const mockHtml = `
  <h2>10-Question Diagnostic Mock Exam</h2>
  <p class="lead-p">Test your mastery of Fundamental Principles of Counting and Constrained Digit Formation under timed CBSE conditions.</p>
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
    question: "How many 3-digit numbers can be formed from the digits 1, 2, 3, 4, and 5 assuming that repetition of digits is allowed?",
    options: ["60", "120", "125", "150"],
    correct: 2,
    explanation: "Each of the 3 positions has 5 independent choices: \\(5 \\times 5 \\times 5 = 125\\)."
  },
  {
    id: 2,
    question: "How many 3-digit numbers can be formed from the digits 1, 2, 3, 4, and 5 if repetition of digits is NOT allowed?",
    options: ["60", "120", "125", "243"],
    correct: 0,
    explanation: "First position has 5 choices, second has 4, third has 3: \\(5 \\times 4 \\times 3 = 60\\)."
  },
  {
    id: 3,
    question: "How many 3-digit even numbers can be formed from the digits 1, 2, 3, 4, 5, 6 if digits can be repeated?",
    options: ["72", "108", "120", "216"],
    correct: 1,
    explanation: "Units place must be 2, 4, or 6 (3 choices). Hundreds and tens places have 6 choices each: \\(6 \\times 6 \\times 3 = 108\\)."
  },
  {
    id: 4,
    question: "How many 4-digit numbers can be formed using the digits 0 to 9 if repetition is not allowed and no number starts with 0?",
    options: ["4536", "5040", "9000", "10000"],
    correct: 0,
    explanation: "Thousands place has 9 choices (1-9). Hundreds place has 9 choices (0 is now eligible). Tens place has 8 choices. Units place has 7 choices: \\(9 \\times 9 \\times 8 \\times 7 = 4536\\)."
  },
  {
    id: 5,
    question: "A coin is tossed 3 times and the outcomes are recorded. How many possible outcomes are there?",
    options: ["6", "8", "9", "16"],
    correct: 1,
    explanation: "Each toss has 2 outcomes: \\(2 \\times 2 \\times 2 = 2^3 = 8\\)."
  },
  {
    id: 6,
    question: "A student can travel from city A to city B by 4 different train routes and from city B to city C by 3 different bus routes. How many total ways can the student travel from A to C via B?",
    options: ["7", "12", "14", "24"],
    correct: 1,
    explanation: "By the Multiplication Principle: \\(4 \\times 3 = 12\\) routes."
  },
  {
    id: 7,
    question: "How many 2-digit numbers can be formed using digits \\(\\{0, 1, 2, 3, 4\\}\\) without repetition?",
    options: ["16", "20", "25", "12"],
    correct: 0,
    explanation: "Tens place cannot be 0, so 4 choices (1-4). Units place has 4 remaining choices (including 0): \\(4 \\times 4 = 16\\)."
  },
  {
    id: 8,
    question: "In how many ways can 3 prizes (1st, 2nd, 3rd) be awarded to a class of 10 students if no student gets more than one prize?",
    options: ["30", "120", "720", "1000"],
    correct: 2,
    explanation: "1st prize has 10 candidates, 2nd has 9, 3rd has 8: \\(10 \\times 9 \\times 8 = 720\\) ways."
  },
  {
    id: 9,
    question: "How many 5-digit telephone numbers can be constructed using the digits 0 to 9 if each number starts with 67 and no digit appears more than once?",
    options: ["336", "512", "672", "720"],
    correct: 0,
    explanation: "The first two digits '67' are fixed (1 choice). The remaining 3 positions must be filled from the remaining 8 digits without repetition: \\(8 \\times 7 \\times 6 = 336\\)."
  },
  {
    id: 10,
    question: "When should the Fundamental Principle of Addition (FPA) be applied instead of the Multiplication Principle (FPM)?",
    options: [
      "When tasks occur sequentially in successive stages",
      "When choices represent mutually exclusive alternate pathways",
      "When repetition of symbols is allowed",
      "When ordering of elements matters"
    ],
    correct: 1,
    explanation: "The Addition Principle is applied when choices are disjunctive alternatives (OR logic) that cannot occur simultaneously."
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
    resultsBox.innerHTML += '<p style="color:#059669; font-weight:600;">Outstanding! Masterful proficiency in the Fundamental Principles of Counting.</p>';
  } else if (pct >= 50) {
    resultsBox.innerHTML += '<p style="color:#d97706; font-weight:600;">Good effort! Review the zero-exclusion rules and digit constraints.</p>';
  } else {
    resultsBox.innerHTML += '<p style="color:#dc2626; font-weight:600;">Needs revision. Study the worked examples on constrained number formation.</p>';
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
console.log('Successfully upgraded 8-1-fundamental-principles-of-counting/index.html');

