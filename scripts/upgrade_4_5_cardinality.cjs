const fs = require('fs');
const cheerio = require('cheerio');

const filePath = 'class-11-applied-mathematics/chapter-4-sets/4-5-cardinality-and-practical-applications/index.html';
const html = fs.readFileSync(filePath, 'utf8');
const $ = cheerio.load(html);

// 1. LEARN TAB
const learnHtml = `
  <h2>4.5 Cardinality and Practical Applications of Sets</h2>
  <p class="lead-p">
    Cardinality — the count of elements in a finite set — is the quantitative bridge connecting pure set algebra to real-world business analytics, consumer surveys, market research, and risk modeling. The <strong>Principle of Inclusion-Exclusion (PIE)</strong> enables analysts to prevent double-counting across overlapping customer demographics or product lines.
  </p>

  <div class="formula-box">
    <h3>Fundamental Cardinality Theorems & Formulae</h3>
    <h4>1. Two-Set System (\\(A\\) and \\(B\\) within Universal Set \\(U\\))</h4>
    <ul>
      <li><strong>Union of Two Sets:</strong>
        \\[ n(A \\cup B) = n(A) + n(B) - n(A \\cap B) \\]
      </li>
      <li><strong>Disjoint Sets:</strong> If \\(A \\cap B = \\emptyset\\), then \\(n(A \\cup B) = n(A) + n(B)\\).</li>
      <li><strong>Only \\(A\\) (Difference \\(A - B\\) or \\(A \\cap B'\\)):</strong>
        \\[ n(A - B) = n(A) - n(A \\cap B) = n(A \\cup B) - n(B) \\]
      </li>
      <li><strong>Symmetric Difference \\(A \\Delta B\\) (Exactly one of \\(A\\) or \\(B\\)):</strong>
        \\[ n(A \\Delta B) = n(A - B) + n(B - A) = n(A) + n(B) - 2n(A \\cap B) = n(A \\cup B) - n(A \\cap B) \\]
      </li>
      <li><strong>Neither \\(A\\) nor \\(B\\) (De Morgan's Complement):</strong>
        \\[ n(A' \\cap B') = n((A \\cup B)') = n(U) - n(A \\cup B) \\]
      </li>
    </ul>

    <h4>2. Three-Set System (\\(A, B, C\\) within Universal Set \\(U\\))</h4>
    <ul>
      <li><strong>Union of Three Sets:</strong>
        \\[ n(A \\cup B \\cup C) = n(A) + n(B) + n(C) - n(A \\cap B) - n(B \\cap C) - n(C \\cap A) + n(A \\cap B \\cap C) \\]
      </li>
      <li><strong>Elements in Exactly Two of the Three Sets:</strong>
        \\[ n(\\text{Exactly 2}) = [n(A \\cap B) + n(B \\cap C) + n(C \\cap A)] - 3n(A \\cap B \\cap C) \\]
      </li>
      <li><strong>Elements in at Least Two Sets:</strong>
        \\[ n(\\text{At least 2}) = [n(A \\cap B) + n(B \\cap C) + n(C \\cap A)] - 2n(A \\cap B \\cap C) \\]
      </li>
      <li><strong>Elements in Exactly One Set:</strong>
        \\[ n(\\text{Exactly 1}) = n(A) + n(B) + n(C) - 2[n(A \\cap B) + n(B \\cap C) + n(C \\cap A)] + 3n(A \\cap B \\cap C) \\]
      </li>
    </ul>
  </div>

  <h3>Systematic 4-Step Region Filling Strategy for Survey Problems</h3>
  <p>
    When solving complex market research problems, setting up algebraic Venn diagram regions prevents algebraic errors:
  </p>
  <ol>
    <li><strong>Anchor at the Core:</strong> Always start by labeling or determining the innermost intersection of all sets \\(n(A \\cap B \\cap C) = x\\).</li>
    <li><strong>Determine Pairwise Exclusives:</strong> Subtract \\(x\\) from pairwise intersections to find elements belonging to <em>only</em> two sets:
      \\[ n(A \\cap B \\text{ only}) = n(A \\cap B) - x \\]
    </li>
    <li><strong>Determine Singleton Exclusives:</strong> Subtract the three adjoining intersection regions from the individual set totals to find elements in <em>only one</em> set:
      \\[ n(A \\text{ only}) = n(A) - [n(A \\cap B \\text{ only}) + n(A \\cap C \\text{ only}) + x] \\]
    </li>
    <li><strong>Account for Non-Participants (Outside):</strong> Subtract the union \\(n(A \\cup B \\cup C)\\) from the universal set \\(n(U)\\) to find elements satisfying none of the conditions.</li>
  </ol>

  <div class="worked-example">
    <h4>Comprehensive Applied Example: Fintech Consumer Survey</h4>
    <p><strong>Scenario:</strong> A market research agency surveys \\(1{,}000\\) smartphone users regarding their usage of three digital payment apps: <strong>PhonePe (\\(P\\))</strong>, <strong>Google Pay (\\(G\\))</strong>, and <strong>Paytm (\\(T\\))</strong>. The survey reports:</p>
    <ul>
      <li>\\(n(P) = 450\\), \\(n(G) = 380\\), \\(n(T) = 280\\)</li>
      <li>\\(n(P \\cap G) = 160\\), \\(n(G \\cap T) = 120\\), \\(n(P \\cap T) = 110\\)</li>
      <li>\\(n(P \\cap G \\cap T) = 50\\) (use all three apps)</li>
    </ul>
    <p><strong>Questions to Analyze:</strong></p>
    <ol>
      <li>How many users use at least one digital payment app?</li>
      <li>How many users use none of these three apps?</li>
      <li>How many users use exactly two apps?</li>
      <li>How many users use PhonePe only?</li>
    </ol>
    <div class="solution">
      <p><strong>Step-by-Step Solution:</strong></p>
      <ol>
        <li><strong>Users using at least one app:</strong>
          \\[ n(P \\cup G \\cup T) = n(P) + n(G) + n(T) - [n(P \\cap G) + n(G \\cap T) + n(P \\cap T)] + n(P \\cap G \\cap T) \\]
          \\[ n(P \\cup G \\cup T) = 450 + 380 + 280 - (160 + 120 + 110) + 50 \\]
          \\[ n(P \\cup G \\cup T) = 1110 - 390 + 50 = 770 \\text{ users.} \\]
        </li>
        <li><strong>Users using none of the three apps:</strong>
          \\[ n((P \\cup G \\cup T)') = n(U) - n(P \\cup G \\cup T) = 1000 - 770 = 230 \\text{ users.} \\]
        </li>
        <li><strong>Users using exactly two apps:</strong>
          \\[ n(\\text{Exactly 2}) = [n(P \\cap G) + n(G \\cap T) + n(P \\cap T)] - 3n(P \\cap G \\cap T) \\]
          \\[ n(\\text{Exactly 2}) = (160 + 120 + 110) - 3(50) = 390 - 150 = 240 \\text{ users.} \\]
          <em>Verification via pairwise exclusives:</em>
          <ul>
            <li>\\(P \\cap G\\) only \\(= 160 - 50 = 110\\)</li>
            <li>\\(G \\cap T\\) only \\(= 120 - 50 = 70\\)</li>
            <li>\\(P \\cap T\\) only \\(= 110 - 50 = 60\\)</li>
            <li>Total \\(= 110 + 70 + 60 = 240\\). Matches perfectly.</li>
          </ul>
        </li>
        <li><strong>Users using PhonePe only:</strong>
          \\[ n(P \\text{ only}) = n(P) - [n(P \\cap G \\text{ only}) + n(P \\cap T \\text{ only}) + n(P \\cap G \\cap T)] \\]
          \\[ n(P \\text{ only}) = 450 - (110 + 60 + 50) = 450 - 220 = 230 \\text{ users.} \\]
        </li>
      </ol>
    </div>
  </div>
`;

// 2. PROGRESS TAB
const progressHtml = `
  <h2>Progress Tracker & Self-Assessment Checklist</h2>
  <p>Track your computational speed and mastery of practical set cardinality problems.</p>
  <div class="checklist-grid">
    <div class="checklist-card">
      <h4>Conceptual Milestones</h4>
      <ul>
        <li><label><input type="checkbox"> Master the two-set Principle of Inclusion-Exclusion formula \\(n(A \\cup B)\\).</label></li>
        <li><label><input type="checkbox"> Derive formulas for "Only A", "Only B", and symmetric difference \\(A \\Delta B\\).</label></li>
        <li><label><input type="checkbox"> Master the 3-set PIE expansion with exact coefficient signs.</label></li>
        <li><label><input type="checkbox"> Distinguish clearly between "at least two" and "exactly two" intersections.</label></li>
        <li><label><input type="checkbox"> Apply De Morgan's complement law to determine non-participant counts.</label></li>
      </ul>
    </div>
    <div class="checklist-card">
      <h4>Problem Solving Milestones</h4>
      <ul>
        <li><label><input type="checkbox"> Successfully solved 2-set consumer preference survey problems.</label></li>
        <li><label><input type="checkbox"> Executed 3-set outward Venn diagram filling starting from the 3-way intersection.</label></li>
        <li><label><input type="checkbox"> Solved bounded inequality problems (e.g., minimum and maximum possible intersection size).</label></li>
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
    <h4>Problem 1 (Two-Set Survey: Minimum and Maximum Bounds)</h4>
    <p>In a town of 10,000 families, it was found that 40% of families buy newspaper \\(A\\), 20% buy newspaper \\(B\\), and 10% buy newspaper \\(C\\). Also, 5% buy \\(A\\) and \\(B\\), 3% buy \\(B\\) and \\(C\\), and 4% buy \\(A\\) and \\(C\\). If 2% buy all three newspapers, find:</p>
    <ol type="a">
      <li>The number of families that buy newspaper \\(A\\) only.</li>
      <li>The number of families that buy none of the newspapers.</li>
    </ol>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        <p>Total families \\(n(U) = 10{,}000\\).</p>
        <ul>
          <li>\\(n(A) = 40\\% \\times 10{,}000 = 4{,}000\\)</li>
          <li>\\(n(B) = 20\\% \\times 10{,}000 = 2{,}000\\)</li>
          <li>\\(n(C) = 10\\% \\times 10{,}000 = 1{,}000\\)</li>
          <li>\\(n(A \\cap B) = 5\\% = 500\\)</li>
          <li>\\(n(B \\cap C) = 3\\% = 300\\)</li>
          <li>\\(n(A \\cap C) = 4\\% = 400\\)</li>
          <li>\\(n(A \\cap B \\cap C) = 2\\% = 200\\)</li>
        </ul>
        <p><strong>Part (a): Number of families buying \\(A\\) only:</strong></p>
        \\[ n(A \\text{ only}) = n(A) - [n(A \\cap B) + n(A \\cap C) - n(A \\cap B \\cap C)] \\]
        \\[ n(A \\text{ only}) = 4{,}000 - [500 + 400 - 200] = 4{,}000 - 700 = 3{,}300 \\text{ families.} \\]
        <p><strong>Part (b): Families buying none:</strong></p>
        \\[ n(A \\cup B \\cup C) = (4000 + 2000 + 1000) - (500 + 300 + 400) + 200 = 7000 - 1200 + 200 = 6{,}000 \\]
        \\[ n(\\text{None}) = n(U) - n(A \\cup B \\cup C) = 10{,}000 - 6{,}000 = 4{,}000 \\text{ families.} \\]
      </div>
    </details>
  </div>

  <div class="problem-card">
    <h4>Problem 2 (Corporate Skills Audit)</h4>
    <p>An IT firm audits 120 software engineers on three skills: <strong>Python (\\(P\\))</strong>, <strong>Java (\\(J\\))</strong>, and <strong>Cloud Architecture (\\(C\\))</strong>.</p>
    <ul>
      <li>65 know Python, 50 know Java, 45 know Cloud.</li>
      <li>30 know Python and Java, 25 know Java and Cloud, 20 know Python and Cloud.</li>
      <li>15 know all three skills.</li>
    </ul>
    <p>Find the number of engineers who know:</p>
    <ol type="a">
      <li>Exactly one of the three skills.</li>
      <li>At least two of the three skills.</li>
    </ol>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        <p>Given: \\(n(U) = 120\\), \\(n(P)=65\\), \\(n(J)=50\\), \\(n(C)=45\\); \\(n(P \\cap J)=30\\), \\(n(J \\cap C)=25\\), \\(n(P \\cap C)=20\\); \\(n(P \\cap J \\cap C)=15\\).</p>
        <p><strong>Part (a): Exactly one skill:</strong></p>
        \\[ n(\\text{Exactly 1}) = \\sum n(A) - 2 \\sum n(A \\cap B) + 3 n(A \\cap B \\cap C) \\]
        \\[ = (65 + 50 + 45) - 2(30 + 25 + 20) + 3(15) \\]
        \\[ = 160 - 2(75) + 45 = 160 - 150 + 45 = 55 \\text{ engineers.} \\]
        <p><strong>Part (b): At least two skills:</strong></p>
        \\[ n(\\text{At least 2}) = \\sum n(A \\cap B) - 2 n(A \\cap B \\cap C) \\]
        \\[ = (30 + 25 + 20) - 2(15) = 75 - 30 = 45 \\text{ engineers.} \\]
      </div>
    </details>
  </div>

  <div class="problem-card">
    <h4>Problem 3 (Theoretical Bounds on Intersection)</h4>
    <p>In a survey of 500 consumers, 350 like Product \\(X\\) and 280 like Product \\(Y\\). What is the minimum and maximum possible number of consumers who like both products?</p>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        <p>We know \\(n(X \\cup Y) = n(X) + n(Y) - n(X \\cap Y) \\le n(U) = 500\\).</p>
        \\[ 350 + 280 - n(X \\cap Y) \\le 500 \\implies 630 - n(X \\cap Y) \\le 500 \\implies n(X \\cap Y) \\ge 130 \\]
        <p>Hence, the <strong>minimum</strong> number who like both is <strong>130</strong>.</p>
        <p>For the maximum, \\(X \\cap Y\\) cannot exceed the size of the smaller set:
          \\[ n(X \\cap Y) \\le \\min(n(X), n(Y)) = \\min(350, 280) = 280 \\]
        </p>
        <p>Hence, the <strong>maximum</strong> number who like both is <strong>280</strong> (which occurs if all who like \\(Y\\) also like \\(X\\)).</p>
      </div>
    </details>
  </div>
`;

// 4. REVISION TAB
const revisionHtml = `
  <h2>Quick Revision & Formula Cheat Sheet</h2>
  <div class="revision-grid">
    <div class="revision-card">
      <h4>Two-Set Formulas</h4>
      <ul>
        <li>\\(n(A \\cup B) = n(A) + n(B) - n(A \\cap B)\\)</li>
        <li>\\(n(A - B) = n(A) - n(A \\cap B)\\)</li>
        <li>\\(n(\\text{Exactly 1}) = n(A \\cup B) - n(A \\cap B)\\)</li>
        <li>\\(n(\\text{Neither}) = n(U) - n(A \\cup B)\\)</li>
      </ul>
    </div>
    <div class="revision-card">
      <h4>Three-Set Formulas</h4>
      <ul>
        <li>\\(n(A \\cup B \\cup C) = \\sum n(A) - \\sum n(A \\cap B) + n(A \\cap B \\cap C)\\)</li>
        <li>\\(n(\\text{Exactly 2}) = \\sum n(A \\cap B) - 3n(A \\cap B \\cap C)\\)</li>
        <li>\\(n(\\text{At least 2}) = \\sum n(A \\cap B) - 2n(A \\cap B \\cap C)\\)</li>
        <li>\\(n(\\text{Exactly 1}) = \\sum n(A) - 2\\sum n(A \\cap B) + 3n(A \\cap B \\cap C)\\)</li>
      </ul>
    </div>
    <div class="revision-card">
      <h4>Boundary Conditions</h4>
      <ul>
        <li>\\(\\max(0, n(A)+n(B)-n(U)) \\le n(A \\cap B) \\le \\min(n(A), n(B))\\)</li>
        <li>\\(\\max(n(A), n(B)) \\le n(A \\cup B) \\le \\min(n(U), n(A)+n(B))\\)</li>
      </ul>
    </div>
  </div>
`;

// 5. MOCK EXAM TAB
const mockHtml = `
  <h2>10-Question Diagnostic Mock Exam</h2>
  <p class="lead-p">Test your mastery of Practical Cardinality and Survey Analysis under timed CBSE conditions.</p>
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
    question: "If \\(n(A) = 28\\), \\(n(B) = 32\\), and \\(n(A \\cup B) = 50\\), what is \\(n(A \\cap B)\\)?",
    options: ["10", "12", "14", "16"],
    correct: 0,
    explanation: "\\(n(A \\cap B) = n(A) + n(B) - n(A \\cup B) = 28 + 32 - 50 = 60 - 50 = 10\\)."
  },
  {
    id: 2,
    question: "In a class of 60 students, 35 play cricket, 25 play football, and 12 play both. How many students play neither cricket nor football?",
    options: ["8", "10", "12", "15"],
    correct: 2,
    explanation: "\\(n(C \\cup F) = 35 + 25 - 12 = 48\\). Students playing neither = \\(60 - 48 = 12\\)."
  },
  {
    id: 3,
    question: "If \\(n(U) = 700\\), \\(n(A) = 200\\), \\(n(B) = 300\\), and \\(n(A \\cap B) = 100\\), find \\(n(A' \\cap B')\\).",
    options: ["200", "300", "400", "500"],
    correct: 1,
    explanation: "\\(n(A \\cup B) = 200 + 300 - 100 = 400\\). By De Morgan's Law, \\(n(A' \\cap B') = n(U) - n(A \\cup B) = 700 - 400 = 300\\)."
  },
  {
    id: 4,
    question: "In a committee, 50 people speak French, 20 speak Spanish, and 10 speak both Spanish and French. How many speak at least one of these two languages?",
    options: ["50", "60", "70", "80"],
    correct: 1,
    explanation: "\\(n(F \\cup S) = n(F) + n(S) - n(F \\cap S) = 50 + 20 - 10 = 60\\)."
  },
  {
    id: 5,
    question: "In a survey of 100 students, the numbers studying various languages were: English 28, German 30, French 42, English & German 8, English & French 10, German & French 5, and all three 3. How many students study none of the three languages?",
    options: ["15", "18", "20", "22"],
    correct: 2,
    explanation: "\\(n(E \\cup G \\cup F) = (28 + 30 + 42) - (8 + 10 + 5) + 3 = 100 - 23 + 3 = 80\\). Neither = \\(100 - 80 = 20\\)."
  },
  {
    id: 6,
    question: "From the data in Question 5, how many students study English ONLY?",
    options: ["10", "13", "15", "18"],
    correct: 1,
    explanation: "\\(n(E \\text{ only}) = n(E) - [n(E \\cap G) + n(E \\cap F) - n(E \\cap G \\cap F)] = 28 - [8 + 10 - 3] = 28 - 15 = 13\\)."
  },
  {
    id: 7,
    question: "If \\(n(A) = 15\\) and \\(n(B) = 20\\), what is the MINIMUM possible value of \\(n(A \\cup B)\\)?",
    options: ["5", "15", "20", "35"],
    correct: 2,
    explanation: "The minimum union occurs when \\(A\\) is completely contained in \\(B\\) (\\(A \\subseteq B\\)). Then \\(n(A \\cup B) = n(B) = 20\\)."
  },
  {
    id: 8,
    question: "If \\(n(A) = 15\\) and \\(n(B) = 20\\), what is the MAXIMUM possible value of \\(n(A \\cup B)\\)?",
    options: ["20", "25", "35", "300"],
    correct: 2,
    explanation: "The maximum union occurs when \\(A\\) and \\(B\\) are completely disjoint (\\(A \\cap B = \\emptyset\\)). Then \\(n(A \\cup B) = 15 + 20 = 35\\)."
  },
  {
    id: 9,
    question: "In an examination, 80% of candidates passed in English and 70% passed in Mathematics. If 10% failed in both subjects and 144 candidates passed in both, find the total number of candidates.",
    options: ["200", "240", "300", "360"],
    correct: 1,
    explanation: "Candidates passing at least one subject = \\(100\\% - 10\\% = 90\\%\\). Then \\(P(E \\cap M) = P(E) + P(M) - P(E \\cup M) = 80\\% + 70\\% - 90\\% = 60\\%\\). Since \\(60\\%\\) corresponds to 144 candidates, total candidates = \\(144 / 0.60 = 240\\)."
  },
  {
    id: 10,
    question: "Given \\(n(A \\Delta B) = 24\\) and \\(n(A \\cap B) = 6\\), what is \\(n(A \\cup B)\\)?",
    options: ["18", "24", "30", "36"],
    correct: 2,
    explanation: "\\(n(A \\Delta B) = n(A \\cup B) - n(A \\cap B) \\implies n(A \\cup B) = n(A \\Delta B) + n(A \\cap B) = 24 + 6 = 30\\)."
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
    resultsBox.innerHTML += '<p style="color:#059669; font-weight:600;">Outstanding! Exceptional command of practical survey cardinality and Venn diagrams.</p>';
  } else if (pct >= 50) {
    resultsBox.innerHTML += '<p style="color:#d97706; font-weight:600;">Good effort! Review the 3-set region equations and retry missed problems.</p>';
  } else {
    resultsBox.innerHTML += '<p style="color:#dc2626; font-weight:600;">Needs revision. Review the 4-step region filling strategy and retry.</p>';
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
console.log('Successfully upgraded 4-5-cardinality-and-practical-applications/index.html');
