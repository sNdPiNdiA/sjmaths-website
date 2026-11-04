const fs = require('fs');
const cheerio = require('cheerio');

const filePath = 'class-11-applied-mathematics/chapter-6-sequences-and-series/6-4-practical-and-business-applications/index.html';
const html = fs.readFileSync(filePath, 'utf8');
const $ = cheerio.load(html);

// 1. LEARN TAB
const learnHtml = `
  <h2>6.4 Practical and Business Applications of Sequences and Series</h2>
  <p class="lead-p">
    Applied Mathematics bridges the abstract algebra of progressions with the operational reality of enterprise economics, accounting standards, and demographic forecasting. This chapter consolidates the practical applications of <strong>Arithmetic Progressions (linear models)</strong> and <strong>Geometric Progressions (exponential models)</strong> in asset depreciation, compensation ladders, compound investment plans, and macroeconomic multipliers.
  </p>

  <div class="formula-box">
    <h3>Comprehensive Financial & Business Modeling Framework</h3>
    <h4>1. Capital Asset Depreciation: Linear vs Compounded Models</h4>
    <table class="table-styled">
      <thead>
        <tr>
          <th>Attribute</th>
          <th>Straight Line Method (SLM) &mdash; AP</th>
          <th>Written Down Value (WDV) &mdash; GP</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Mathematical Nature</strong></td>
          <td>Arithmetic Progression (Constant annual deduction)</td>
          <td>Geometric Progression (Constant annual percentage decay)</td>
        </tr>
        <tr>
          <td><strong>Book Value Formula (Year \\(n\\))</strong></td>
          <td>\\[ V_n = V_0 - n \\cdot D \\]</td>
          <td>\\[ V_n = V_0 (1 - r)^n \\]</td>
        </tr>
        <tr>
          <td><strong>Depreciation in Year \\(n\\)</strong></td>
          <td>\\[ D = \\frac{V_0 - S}{L} \\quad (\\text{Constant}) \\]</td>
          <td>\\[ D_n = r \\cdot V_{n-1} = r V_0 (1 - r)^{n-1} \\]</td>
        </tr>
        <tr>
          <td><strong>Scrap Value Reachability</strong></td>
          <td>Reaches exact scrap value \\(S\\) at end of useful life \\(L\\)</td>
          <td>Asymptotically approaches zero; never theoretically reaches absolute zero</td>
        </tr>
      </tbody>
    </table>

    <h4>2. Structured Corporate Compensation Ladders</h4>
    <p>
      An employment salary grade with an initial pay \\(a\\) and fixed annual increment \\(d\\) represents an AP:
      \\[ \\text{Salary in Year } n = a + (n - 1)d \\]
      \\[ \\text{Total Earnings over } n \\text{ Years} = \\frac{n}{2} [2a + (n - 1)d] \\]
    </p>

    <h4>3. Population and Demographic Projections</h4>
    <p>
      Demographic counts growing at an annual compounding growth rate \\(r\\) follow an exponential GP:
      \\[ P_n = P_0 (1 + r)^n \\]
      If growth rate varies year-over-year: \\(P_n = P_0 (1 + r_1)(1 + r_2)\\dots(1 + r_n)\\).
    </p>
  </div>

  <div class="worked-example">
    <h4>Comprehensive Financial Worked Example: Corporate Asset Replacement Strategy</h4>
    <p><strong>Scenario:</strong> A manufacturing enterprise purchases heavy industrial machinery for ₹5,00,000. The operational lifespan of the machine is estimated to be 5 years.</p>
    <ol>
      <li>If the company adopts the <strong>Straight Line Method (SLM)</strong> with an expected scrap value of ₹50,000, find the annual depreciation charge and the book value at the end of the 3rd year.</li>
      <li>If the company adopts the <strong>Written Down Value (WDV) Method</strong> at a statutory depreciation rate of 20% per annum, find the book value at the end of 3 years and the depreciation charge for the 4th year.</li>
    </ol>
    <div class="solution">
      <p><strong>Solution:</strong></p>
      <p><strong>1. Under the Straight Line Method (SLM):</strong></p>
      <ul>
        <li>Cost \\(V_0 = ₹5{,}00{,}000\\), Scrap value \\(S = ₹50{,}000\\), Lifespan \\(L = 5\\) years.</li>
        <li>Annual constant depreciation:
          \\[ D = \\frac{V_0 - S}{L} = \\frac{5{,}00{,}000 - 50{,}000}{5} = \\frac{4{,}50{,}000}{5} = ₹90{,}000 \\text{ per annum.} \\]
        </li>
        <li>Book value at the end of 3 years (using AP):
          \\[ V_3 = V_0 - 3D = 5{,}00{,}000 - 3(90{,}000) = 5{,}00{,}000 - 2{,}70{,}000 = ₹2{,}30{,}000. \\]
        </li>
      </ul>
      <p><strong>2. Under the Written Down Value (WDV) Method:</strong></p>
      <ul>
        <li>Depreciation rate \\(r = 20\\% = 0.20\\).</li>
        <li>Book value at the end of 3 years (using GP):
          \\[ V_3 = V_0 (1 - r)^3 = 5{,}00{,}000 \\times (1 - 0.20)^3 = 5{,}00{,}000 \\times (0.80)^3 \\]
          \\[ V_3 = 5{,}00{,}000 \\times 0.512 = ₹2{,}56{,}000. \\]
        </li>
        <li>Depreciation charge during the 4th year:
          \\[ D_4 = r \\times V_3 = 0.20 \\times 2{,}56{,}000 = ₹51{,}200. \\]
        </li>
      </ul>
    </div>
  </div>
`;

// 2. PROGRESS TAB
const progressHtml = `
  <h2>Progress Tracker & Self-Assessment Checklist</h2>
  <p>Track your computational speed and mastery of business applications of sequences and series.</p>
  <div class="checklist-grid">
    <div class="checklist-card">
      <h4>Conceptual Milestones</h4>
      <ul>
        <li><label><input type="checkbox"> Distinguish between Straight Line (AP) and Written Down Value (GP) depreciation.</label></li>
        <li><label><input type="checkbox"> Formulate cumulative compensation earnings using AP summation.</label></li>
        <li><label><input type="checkbox"> Model compound demographic and customer subscriber growth via GP.</label></li>
        <li><label><input type="checkbox"> Compute loan amortization schedules with progressive repayment steps.</label></li>
      </ul>
    </div>
    <div class="checklist-card">
      <h4>Problem Solving Milestones</h4>
      <ul>
        <li><label><input type="checkbox"> Computed multi-year depreciation schedules comparing SLM vs WDV.</label></li>
        <li><label><input type="checkbox"> Solved break-even and asset replacement horizon problems.</label></li>
        <li><label><input type="checkbox"> Modeled macroeconomic fiscal multiplier cash flows.</label></li>
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
    <h4>Problem 1 (Compensation Package Comparison: AP vs GP)</h4>
    <p>A university graduate receives two competing job offers from financial consulting firms:</p>
    <ul>
      <li><strong>Offer A:</strong> Starting salary of ₹6,00,000 per annum with a fixed annual increment of ₹50,000 (AP).</li>
      <li><strong>Offer B:</strong> Starting salary of ₹5,50,000 per annum with a guaranteed 10% annual salary increase (GP).</li>
    </ul>
    <p>Calculate:</p>
    <ol type="a">
      <li>The salary offered by each firm in the 5th year.</li>
      <li>The total cumulative income earned from each firm over 5 years. Which offer yields greater total earnings?</li>
    </ol>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        <p><strong>Offer A (AP):</strong> \\(a = 6{,}00{,}000, d = 50{,}000, n = 5\\).</p>
        <ul>
          <li>Salary in 5th year: \\(T_5 = a + 4d = 6{,}00{,}000 + 4(50{,}000) = ₹8{,}00{,}000\\).</li>
          <li>Total earnings over 5 years:
            \\[ S_5 = \\frac{5}{2} [2(6{,}00{,}000) + 4(50{,}000)] = 2.5 [12{,}00{,}000 + 2{,}00{,}000] = 2.5 \\times 14{,}00{,}000 = ₹35{,}00{,}000. \\]
          </li>
        </ul>
        <p><strong>Offer B (GP):</strong> \\(a = 5{,}50{,}000, r = 1 + 0.10 = 1.10, n = 5\\).</p>
        <ul>
          <li>Salary in 5th year:
            \\[ T_5 = a r^4 = 5{,}50{,}000 \\times (1.10)^4 = 5{,}50{,}000 \\times 1.4641 = ₹8{,}05{,}255. \\]
          </li>
          <li>Total earnings over 5 years:
            \\[ S_5 = \\frac{a(r^5 - 1)}{r - 1} = \\frac{5{,}50{,}000((1.10)^5 - 1)}{1.10 - 1} = \\frac{5{,}50{,}000(1.61051 - 1)}{0.10} \\]
            \\[ S_5 = 55{,}00{,}000 \\times 0.61051 = ₹33{,}57{,}805. \\]
          </li>
        </ul>
        <p><strong>Comparison:</strong> Although Offer B pays a higher salary in the 5th year (₹8,05,255 vs ₹8,00,000), <strong>Offer A yields ₹1,42,195 more in total cumulative income</strong> over the 5-year horizon (₹35,00,000 vs ₹33,57,805).</p>
      </div>
    </details>
  </div>

  <div class="problem-card">
    <h4>Problem 2 (Corporate Sinking Fund for Machinery Replacement)</h4>
    <p>A machine costs ₹10,00,000 and depreciates at 15% per annum on the reducing balance method. At the same time, the cost of a replacement machine increases by 5% per annum due to inflation. What is the net capital gap required to replace the machine at the end of 4 years?</p>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        <p><strong>1. Salvage Value of Existing Machine (WDV):</strong></p>
        \\[ V_4 = 10{,}00{,}000 \\times (1 - 0.15)^4 = 10{,}00{,}000 \\times (0.85)^4 \\]
        \\[ (0.85)^4 = 0.52200625 \\implies V_4 \\approx ₹5{,}22{,}006. \\]
        <p><strong>2. Cost of New Replacement Machine (Inflation GP):</strong></p>
        \\[ C_4 = 10{,}00{,}000 \\times (1 + 0.05)^4 = 10{,}00{,}000 \\times (1.05)^4 \\]
        \\[ (1.05)^4 = 1.21550625 \\implies C_4 \\approx ₹12{,}15{,}506. \\]
        <p><strong>3. Capital Gap Required:</strong></p>
        \\[ \\text{Net Capital Gap} = C_4 - V_4 = 12{,}15{,}506 - 5{,}22{,}006 = ₹6{,}93{,}500. \\]
      </div>
    </details>
  </div>
`;

// 4. REVISION TAB
const revisionHtml = `
  <h2>Quick Revision & Formula Cheat Sheet</h2>
  <div class="revision-grid">
    <div class="revision-card">
      <h4>Depreciation Models</h4>
      <ul>
        <li><strong>SLM (AP):</strong> \\(V_n = V_0 - n D\\)</li>
        <li>\\(D = (V_0 - \\text{Scrap})/L\\)</li>
        <li><strong>WDV (GP):</strong> \\(V_n = V_0 (1 - r)^n\\)</li>
        <li>Depreciation in year \\(n\\): \\(D_n = r V_0(1-r)^{n-1}\\)</li>
      </ul>
    </div>
    <div class="revision-card">
      <h4>Cumulative Income & Growth</h4>
      <ul>
        <li>Cumulative AP pay: \\(S_n = \\frac{n}{2}[2a + (n-1)d]\\)</li>
        <li>Cumulative GP pay: \\(S_n = \\frac{a(r^n - 1)}{r - 1}\\)</li>
        <li>Population projection: \\(P_n = P_0 (1 + r)^n\\)</li>
      </ul>
    </div>
    <div class="revision-card">
      <h4>Key Trade-offs</h4>
      <ul>
        <li>SLM has higher depreciation in later years than WDV</li>
        <li>WDV provides tax benefits earlier by front-loading deductions</li>
        <li>Linear growth (AP) dominates compounding (GP) in early periods if initial base is sufficiently high</li>
      </ul>
    </div>
  </div>
`;

// 5. MOCK EXAM TAB
const mockHtml = `
  <h2>10-Question Diagnostic Mock Exam</h2>
  <p class="lead-p">Test your mastery of Practical and Business Applications of AP and GP under timed CBSE conditions.</p>
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
    question: "A company purchases equipment for ₹2,00,000. Under the Straight Line Method with a scrap value of ₹20,000 over 10 years, what is the annual depreciation charge?",
    options: ["₹18,000", "₹20,000", "₹22,000", "₹25,000"],
    correct: 0,
    explanation: "\\(D = \\frac{200{,}000 - 20{,}000}{10} = \\frac{180{,}000}{10} = ₹18{,}000\\)."
  },
  {
    id: 2,
    question: "Using the data from Question 1, what is the book value of the equipment at the end of 6 years?",
    options: ["₹80,000", "₹92,000", "₹1,08,000", "₹1,20,000"],
    correct: 1,
    explanation: "\\(V_6 = 200{,}000 - 6(18{,}000) = 200{,}000 - 108{,}000 = ₹92{,}000\\)."
  },
  {
    id: 3,
    question: "An asset costing ₹1,00,000 is depreciated at 20% p.a. on the Written Down Value method. What is its book value at the end of 2 years?",
    options: ["₹60,000", "₹64,000", "₹70,000", "₹80,000"],
    correct: 1,
    explanation: "\\(V_2 = 100{,}000 \\times (1 - 0.20)^2 = 100{,}000 \\times 0.64 = ₹64{,}000\\)."
  },
  {
    id: 4,
    question: "For the asset in Question 3, what is the exact depreciation charged in the 3rd year?",
    options: ["₹12,800", "₹16,000", "₹20,000", "₹25,600"],
    correct: 0,
    explanation: "\\(D_3 = 0.20 \\times V_2 = 0.20 \\times 64{,}000 = ₹12{,}800\\)."
  },
  {
    id: 5,
    question: "The population of a city is 1,00,000 and increases at a constant compound rate of 10% per annum. What will the population be after 3 years?",
    options: ["1,30,000", "1,33,100", "1,40,000", "1,46,410"],
    correct: 1,
    explanation: "\\(P_3 = 100{,}000 \\times (1.10)^3 = 100{,}000 \\times 1.331 = 1{,}33{,}100\\)."
  },
  {
    id: 6,
    question: "An employee starts at an initial annual salary of ₹4,00,000 with a fixed annual increment of ₹30,000. What is their total cumulative compensation over 8 years?",
    options: ["₹35,20,000", "₹37,60,000", "₹40,40,000", "₹42,00,000"],
    correct: 2,
    explanation: "\\(S_8 = \\frac{8}{2}[2(400{,}000) + 7(30{,}000)] = 4[800{,}000 + 210{,}000] = 4(1{,}010{,}000) = ₹40{,}40{,}000\\)."
  },
  {
    id: 7,
    question: "Under which depreciation method does the annual depreciation charge remain constant across all years of an asset's useful life?",
    options: [
      "Straight Line Method (AP)",
      "Written Down Value Method (GP)",
      "Sum of Years' Digits Method",
      "Double Declining Balance Method"
    ],
    correct: 0,
    explanation: "Under the Straight Line Method (SLM), annual depreciation is constant, representing an Arithmetic Progression."
  },
  {
    id: 8,
    question: "A viral marketing video achieves 10,000 views on day 1. If each viewer shares it such that views increase by 50% each day, how many views occur on day 4?",
    options: ["22,500", "33,750", "50,625", "75,937"],
    correct: 1,
    explanation: "\\(a_4 = 10{,}000 \\times (1.5)^3 = 10{,}000 \\times 3.375 = 33{,}750\\) views."
  },
  {
    id: 9,
    question: "If a loan is repaid in 12 monthly installments such that the first installment is ₹1,000 and each subsequent installment increases by ₹100, what is the total amount repaid?",
    options: ["₹15,600", "₹18,600", "₹20,400", "₹22,000"],
    correct: 1,
    explanation: "\\(S_{12} = \\frac{12}{2}[2(1000) + 11(100)] = 6[2000 + 1100] = 6(3100) = ₹18{,}600\\)."
  },
  {
    id: 10,
    question: "Why do corporate tax planners often prefer the Written Down Value (WDV) method over the Straight Line Method (SLM)?",
    options: [
      "WDV allows higher tax deductions in the early years, deferring tax liability",
      "WDV reduces the asset book value to zero faster",
      "WDV is simpler to calculate than SLM",
      "WDV increases the reported accounting profit in year 1"
    ],
    correct: 0,
    explanation: "Because WDV front-loads depreciation expense, it reduces taxable income in the earlier years, providing a time-value-of-money tax deferral benefit."
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
    resultsBox.innerHTML += '<p style="color:#059669; font-weight:600;">Outstanding! Masterful proficiency in financial and business progressions.</p>';
  } else if (pct >= 50) {
    resultsBox.innerHTML += '<p style="color:#d97706; font-weight:600;">Good effort! Review SLM vs WDV depreciation differences and retry.</p>';
  } else {
    resultsBox.innerHTML += '<p style="color:#dc2626; font-weight:600;">Needs revision. Study the worked examples on corporate salary ladders and depreciation.</p>';
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
console.log('Successfully upgraded 6-4-practical-and-business-applications/index.html');
