const fs = require('fs');
const cheerio = require('cheerio');

const filePath = 'class-11-applied-mathematics/chapter-8-combinatorics/8-2-factorial-notation/index.html';
const html = fs.readFileSync(filePath, 'utf8');
const $ = cheerio.load(html);

// 1. LEARN TAB
const learnHtml = `
  <h2>8.2 Factorial Notation: Properties, Algebraic Manipulation, and Legendre's Theorem</h2>
  <p class="lead-p">
    In Applied Mathematics, algorithmic complexity analysis, and combinatorial probability, the <strong>factorial</strong> is the foundational operator that encapsulates the cumulative product of sequential integers. It enables compact algebraic representation of permutations, combinations, and binomial coefficients.
  </p>

  <div class="formula-box">
    <h3>Fundamental Definitions & Recurrence Properties</h3>
    <ul>
      <li><strong>Definition of Factorial:</strong> For any positive integer \\(n \in \\mathbb{N}\\), \\(n!\\) (read as "\\(n\\) factorial") is the product of the first \\(n\\) consecutive natural numbers:
        \\[ n! = n \\times (n - 1) \\times (n - 2) \\times \\dots \\times 3 \\times 2 \\times 1 \\]
      </li>
      <li><strong>Fundamental Recurrence Relation:</strong>
        \\[ n! = n \\cdot (n - 1)! \\quad (\\text{for all } n \\ge 1) \\]
        Repeated expansion: \\(n! = n(n - 1)(n - 2)! = n(n - 1)(n - 2)(n - 3)!\\).
      </li>
      <li><strong>The \\(0! = 1\\) Identity:</strong>
        Setting \\(n = 1\\) into the recurrence relation:
        \\[ 1! = 1 \\cdot (1 - 1)! = 1 \\cdot 0! \\implies 0! = 1 \\]
        This standard convention guarantees that combinations and permutations evaluate consistently when selecting 0 items or all items.
      </li>
      <li><strong>Non-Distributivity Warning:</strong>
        Factorial is strictly <strong>non-linear</strong>:
        \\[ (a + b)! \\neq a! + b!, \\quad (a - b)! \\neq a! - b!, \\quad (a \\cdot b)! \\neq a! \\cdot b!, \\quad \\left(\\frac{a}{b}\\right)! \\neq \\frac{a!}{b!} \\]
      </li>
      <li><strong>Legendre's Formula (Exponent of a Prime in \\(n!\\)):</strong>
        The highest power of a prime \\(p\\) that divides \\(n!\\) is:
        \\[ E_p(n!) = \\left\\lfloor \\frac{n}{p} \\right\\rfloor + \\left\\lfloor \\frac{n}{p^2} \\right\\rfloor + \\left\\lfloor \\frac{n}{p^3} \\right\\rfloor + \\dots \\]
        <em>Trailing Zeros:</em> The number of trailing zeros in \\(n!\\) equals \\(E_5(n!)\\) because 2s always outnumber 5s.
      </li>
    </ul>
  </div>

  <h3>Key Algebraic Simplification Techniques</h3>
  <table class="table-styled">
    <thead>
      <tr>
        <th>Algebraic Expression</th>
        <th>Simplification Technique</th>
        <th>Result</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>\\(\\frac{n!}{(n - 2)!}\\)</td>
        <td>Expand numerator down to \\((n - 2)!\\): \\(\\frac{n(n - 1)(n - 2)!}{(n - 2)!}\\)</td>
        <td>\\(n(n - 1) = n^2 - n\\)</td>
      </tr>
      <tr>
        <td>\\(\\frac{(n + 1)!}{(n - 1)!}\\)</td>
        <td>Expand \\((n + 1)! = (n + 1) n (n - 1)!\\)</td>
        <td>\\(n(n + 1) = n^2 + n\\)</td>
      </tr>
      <tr>
        <td>\\(\\frac{1}{n!} - \\frac{1}{(n + 1)!}\\)</td>
        <td>Common denominator \\((n + 1)! = (n + 1)n!\\)</td>
        <td>\\(\\frac{(n + 1) - 1}{(n + 1)!} = \\frac{n}{(n + 1)!}\\)</td>
      </tr>
    </tbody>
  </table>

  <div class="worked-example">
    <h4>Comprehensive Worked Example: Solving Factorial Fractional Equations</h4>
    <p><strong>Problem:</strong> Solve for \\(x\\) if:
      \\[ \\frac{1}{6!} + \\frac{1}{7!} = \\frac{x}{8!} \\]
    </p>
    <div class="solution">
      <p><strong>Solution:</strong></p>
      <p>Multiply the entire equation by \\(8!\\) (the largest factorial present):</p>
      \\[ \\frac{8!}{6!} + \\frac{8!}{7!} = x \\]
      Expanding the ratios of factorials:
      \\[ \\frac{8 \\times 7 \\times 6!}{6!} + \\frac{8 \\times 7!}{7!} = x \\]
      \\[ (8 \\times 7) + 8 = x \\]
      \\[ 56 + 8 = x \\implies x = 64. \\]
      <strong>Answer:</strong> \\(x = 64\\).
    </div>
  </div>
`;

// 2. PROGRESS TAB
const progressHtml = `
  <h2>Progress Tracker & Self-Assessment Checklist</h2>
  <p>Track your computational speed and mastery of Factorial Notation and Algebraic Simplifications.</p>
  <div class="checklist-grid">
    <div class="checklist-card">
      <h4>Conceptual Milestones</h4>
      <ul>
        <li><label><input type="checkbox"> Define \\(n!\\) and explain why \\(0! = 1\\).</label></li>
        <li><label><input type="checkbox"> Factor expressions using \\(n! = n(n-1)!\\).</label></li>
        <li><label><input type="checkbox"> Master Legendre's formula for finding prime powers in \\(n!\\).</label></li>
        <li><label><input type="checkbox"> Compute trailing zeros of large factorials using multiples of 5.</label></li>
      </ul>
    </div>
    <div class="checklist-card">
      <h4>Problem Solving Milestones</h4>
      <ul>
        <li><label><input type="checkbox"> Solved fractional factorial equations by clearing denominators.</label></li>
        <li><label><input type="checkbox"> Solved quadratic and polynomial equations in \\(n\\) derived from factorial ratios.</label></li>
        <li><label><input type="checkbox"> Proven combinatorial identities using factorial algebra.</label></li>
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
    <h4>Problem 1 (Solving for \\(n\\) from a Factorial Ratio)</h4>
    <p>Find \\(n\\) if \\(\\frac{(n + 2)!}{n!} = 2550\\).</p>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        <p>Expand \\((n + 2)!\\):</p>
        \\[ \\frac{(n + 2)(n + 1)n!}{n!} = 2550 \\implies (n + 2)(n + 1) = 2550 \\]
        Notice that \\((n + 2)\\) and \\((n + 1)\\) are two consecutive positive integers whose product is 2550:
        \\[ 2550 = 50 \\times 51 = 51 \\times 50 \\]
        Equating factors:
        \\[ n + 2 = 51 \\implies n = 49. \\]
        (Alternatively, via quadratic: \\(n^2 + 3n + 2 - 2550 = 0 \\implies n^2 + 3n - 2548 = 0 \\implies (n - 49)(n + 52) = 0\\). Since \\(n \\in \\mathbb{N}\\), \\(n = 49\\)).
      </div>
    </details>
  </div>

  <div class="problem-card">
    <h4>Problem 2 (Legendre's Formula: Trailing Zeros)</h4>
    <p>How many trailing zeros are there at the end of \\(100!\\)?</p>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        <p>The number of trailing zeros is determined by the highest power of 10 dividing \\(100!\\), which equals the exponent of 5 in \\(100!\\):</p>
        \\[ E_5(100!) = \\left\\lfloor \\frac{100}{5} \\right\\rfloor + \\left\\lfloor \\frac{100}{25} \\right\\rfloor + \\left\\lfloor \\frac{100}{125} \\right\\rfloor + \\dots \\]
        \\[ = 20 + 4 + 0 = 24. \\]
        <strong>Answer:</strong> \\(100!\\) ends in exactly <strong>24 zeros</strong>.
      </div>
    </details>
  </div>

  <div class="problem-card">
    <h4>Problem 3 (Factorial Inequality Proof)</h4>
    <p>Prove that \\(n! > 2^n\\) for all integers \\(n \\ge 4\\).</p>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        <p>For \\(n = 4\\): \\(4! = 24\\) and \\(2^4 = 16\\). Since \\(24 > 16\\), the base case holds.</p>
        <p>For \\(n > 4\\):
          \\[ n! = 1 \\times 2 \\times 3 \\times 4 \\times 5 \\times \\dots \\times n \\]
          Notice that:
          \\[ 1 \\times 2 = 2 \\]
          \\[ 3 > 2 \\]
          \\[ 4 > 2 \\]
          \\[ \\dots \\]
          \\[ n > 2 \\]
          Multiplying these together:
          \\[ n! = 2 \\times (3 \\times 4 \\times \\dots \\times n) > 2 \\times (2 \\times 2 \\times \\dots \\times 2) = 2^n. \\]
        Hence \\(n! > 2^n\\) for all \\(n \\ge 4\\).
      </div>
    </details>
  </div>
`;

// 4. REVISION TAB
const revisionHtml = `
  <h2>Quick Revision & Formula Cheat Sheet</h2>
  <div class="revision-grid">
    <div class="revision-card">
      <h4>Basic Definitions</h4>
      <ul>
        <li>\\(n! = n \\times (n - 1) \\times \\dots \\times 1\\)</li>
        <li>\\(0! = 1\\) and \\(1! = 1\\)</li>
        <li>\\(n! = n(n - 1)!\\)</li>
        <li>Factorials of negative numbers are undefined</li>
      </ul>
    </div>
    <div class="revision-card">
      <h4>Algebraic Identities</h4>
      <ul>
        <li>\\(\\frac{n!}{(n - 1)!} = n\\)</li>
        <li>\\(\\frac{n!}{(n - 2)!} = n(n - 1)\\)</li>
        <li>\\(\\frac{1}{n!} + \\frac{1}{(n+1)!} = \\frac{n+2}{(n+1)!}\\)</li>
      </ul>
    </div>
    <div class="revision-card">
      <h4>Legendre's Formula</h4>
      <ul>
        <li>\\(E_p(n!) = \\sum_{k=1}^\\infty \\lfloor n / p^k \\rfloor\\)</li>
        <li>Trailing zeros in \\(n!\\) \\(= \\lfloor n/5 \\rfloor + \\lfloor n/25 \\rfloor + \\dots\\)</li>
      </ul>
    </div>
  </div>
`;

// 5. MOCK EXAM TAB
const mockHtml = `
  <h2>10-Question Diagnostic Mock Exam</h2>
  <p class="lead-p">Test your mastery of Factorial Notation, Algebraic Simplifications, and Legendre's Formula under timed CBSE conditions.</p>
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
    question: "What is the value of \\(\\frac{8!}{6! \\times 2!}\\)?",
    options: ["14", "28", "56", "112"],
    correct: 1,
    explanation: "\\(\\frac{8 \\times 7 \\times 6!}{6! \\times 2} = \\frac{56}{2} = 28\\)."
  },
  {
    id: 2,
    question: "If \\(\\frac{1}{8!} + \\frac{1}{9!} = \\frac{x}{10!}\\), find \\(x\\).",
    options: ["81", "90", "100", "110"],
    correct: 2,
    explanation: "Multiply by \\(10!\\): \\(\\frac{10!}{8!} + \\frac{10!}{9!} = x \\implies (10 \\times 9) + 10 = 90 + 10 = 100\\)."
  },
  {
    id: 3,
    question: "What is the value of \\(0!\\)?",
    options: ["0", "1", "-1", "Undefined"],
    correct: 1,
    explanation: "By convention and definition of the empty product, \\(0! = 1\\)."
  },
  {
    id: 4,
    question: "If \\((n + 1)! = 12(n - 1)!\\), what is the value of natural number \\(n\\)?",
    options: ["2", "3", "4", "5"],
    correct: 1,
    explanation: "\\(\\frac{(n+1)!}{(n-1)!} = (n+1)n = 12 = 4 \\times 3 \\implies n = 3\\)."
  },
  {
    id: 5,
    question: "How many trailing zeros does \\(50!\\) end with?",
    options: ["10", "12", "14", "16"],
    correct: 1,
    explanation: "\\(\\lfloor 50/5 \\rfloor + \\lfloor 50/25 \\rfloor = 10 + 2 = 12\\)."
  },
  {
    id: 6,
    question: "Which of the following expressions is identically equal to \\(\\frac{(2n)!}{n!}\\)?",
    options: [
      "\\(2^n [1 \\cdot 3 \\cdot 5 \\dots (2n - 1)]\\)",
      "\\(2^n \\cdot n!\\)",
      "\\((2n - 1)!\\)",
      "\\(2 \\cdot n!\\)"
    ],
    correct: 0,
    explanation: "\\((2n)! = [1 \\cdot 3 \\dots (2n-1)] \\times [2 \\cdot 4 \\dots 2n] = [1 \\cdot 3 \\dots (2n-1)] \\times 2^n n!\\). Dividing by \\(n!\\) yields \\(2^n [1 \\cdot 3 \\cdot 5 \\dots (2n - 1)]\\)."
  },
  {
    id: 7,
    question: "What is the unit digit of the sum \\(1! + 2! + 3! + 4! + \\dots + 100!\\)?",
    options: ["1", "3", "5", "7"],
    correct: 1,
    explanation: "For \\(n \\ge 5\\), \\(n!\\) ends in 0 (multiples of 10). The unit digit depends only on \\(1! + 2! + 3! + 4! = 1 + 2 + 6 + 24 = 33\\). The unit digit is 3."
  },
  {
    id: 8,
    question: "What is the highest power of 3 that completely divides \\(30!\\)?",
    options: ["10", "12", "14", "15"],
    correct: 2,
    explanation: "\\(E_3(30!) = \\lfloor 30/3 \\rfloor + \\lfloor 30/9 \\rfloor + \\lfloor 30/27 \\rfloor = 10 + 3 + 1 = 14\\)."
  },
  {
    id: 9,
    question: "If \\(\\frac{n!}{2!(n-2)!}\\) and \\(\\frac{n!}{4!(n-4)!}\\) are in the ratio \\(2 : 1\\), find \\(n\\).",
    options: ["4", "5", "6", "7"],
    correct: 1,
    explanation: "\\(\\frac{n(n-1)/2}{n(n-1)(n-2)(n-3)/24} = \\frac{12}{(n-2)(n-3)} = \\frac{2}{1} \\implies (n-2)(n-3) = 6 = 3 \\times 2 \\implies n - 2 = 3 \\implies n = 5\\)."
  },
  {
    id: 10,
    question: "Is \\((a + b)! = a! + b!\\) true for non-zero natural numbers?",
    options: [
      "Always true",
      "True only when \\(a = b\\)",
      "Never true for non-zero natural numbers",
      "True only when \\(a = 1\\)"
    ],
    correct: 2,
    explanation: "Factorial is strictly non-distributive over addition; \\((a + b)! > a! + b!\\) for all natural numbers \\(a, b \\ge 1\\)."
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
    resultsBox.innerHTML += '<p style="color:#059669; font-weight:600;">Outstanding! Masterful proficiency in factorial algebra and Legendre theorems.</p>';
  } else if (pct >= 50) {
    resultsBox.innerHTML += '<p style="color:#d97706; font-weight:600;">Good effort! Review prime factorizations of factorials and retry.</p>';
  } else {
    resultsBox.innerHTML += '<p style="color:#dc2626; font-weight:600;">Needs revision. Study the worked examples on solving factorial equations.</p>';
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
console.log('Successfully upgraded 8-2-factorial-notation/index.html');

