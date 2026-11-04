const fs = require('fs');
const cheerio = require('cheerio');

const filePath = 'class-11-applied-mathematics/chapter-4-sets/4-3-subsets-power-sets-and-universal-sets/index.html';
const html = fs.readFileSync(filePath, 'utf8');
const $ = cheerio.load(html);

// 1. LEARN TAB
const learnHtml = `
  <h2>4.3 Subsets, Power Sets, and Universal Sets</h2>
  <p class="lead-p">
    In Applied Mathematics and data modeling, understanding how sub-collections relate to broader populations is fundamental. Whether analyzing market segmentation, financial portfolios, or database filters, the mathematical formalisms of <strong>subsets</strong>, <strong>power sets</strong>, and <strong>universal sets</strong> provide the foundational logic.
  </p>

  <div class="formula-box">
    <h3>Core Structural Theorems & Definitions</h3>
    <ul>
      <li><strong>Subset (\\(A \\subseteq B\\)):</strong> Set \\(A\\) is a subset of \\(B\\) if and only if every element belonging to \\(A\\) also belongs to \\(B\\):
        \\[ x \\in A \\implies x \\in B \\]
      </li>
      <li><strong>Proper Subset (\\(A \\subset B\\) or \\(A \\subsetneq B\\)):</strong> \\(A\\) is a proper subset of \\(B\\) if \\(A \\subseteq B\\) and \\(A \\neq B\\). This implies \\(B\\) contains at least one element not in \\(A\\).</li>
      <li><strong>Universal Properties:</strong>
        <ol>
          <li>Every set is a subset of itself: \\(A \\subseteq A\\) for every set \\(A\\).</li>
          <li>The empty set is a subset of every set: \\(\\emptyset \\subseteq A\\) for every set \\(A\\).</li>
        </ol>
      </li>
      <li><strong>Total Number of Subsets:</strong> If a finite set \\(A\\) contains \\(n\\) elements (i.e., \\(n(A) = n\\)):
        \\[ \\text{Total Subsets} = 2^n, \\quad \\text{Total Proper Subsets} = 2^n - 1 \\]
      </li>
      <li><strong>Power Set (\\(\\mathcal{P}(A)\\) or \\(P(A)\\)):</strong> The collection of all subsets of set \\(A\\):
        \\[ P(A) = \\{ X : X \\subseteq A \\}, \\quad n(P(A)) = 2^{n(A)} \\]
      </li>
      <li><strong>Universal Set (\\(U\\)):</strong> A superset containing all objects or elements under consideration in a specific mathematical context.</li>
    </ul>
  </div>

  <h3>1. Mathematical Precision: \\(\\in\\) (Belongs to) vs \\(\\subseteq\\) (Subset of)</h3>
  <p>
    One of the most frequent traps in set theory is conflating element membership (\\(\\in\\)) with set inclusion (\\(\\subseteq\\)).
  </p>
  <ul>
    <li>An element \\(x\\) belongs to a set: \\(x \\in A\\).</li>
    <li>A set containing that element is a subset: \\(\\{x\\} \\subseteq A\\).</li>
    <li>Notice the critical case of nested sets: Let \\(A = \\{1, 2, \\{3, 4\\}, 5\\}\\).
      <ul>
        <li>\\(\\{3, 4\\} \\in A\\) is <strong>True</strong> (it is an explicit element of \\(A\\)).</li>
        <li>\\(\\{3, 4\\} \\subseteq A\\) is <strong>False</strong> (3 and 4 are not individual elements of \\(A\\)).</li>
        <li>\\(\\{\\{3, 4\\}\\} \\subseteq A\\) is <strong>True</strong> (the set containing the element \\(\\{3, 4\\}\\) is a subset).</li>
      </ul>
    </li>
  </ul>

  <h3>2. Subsets of Real Numbers: Interval Notation</h3>
  <p>
    In calculus, financial economics, and continuous business variables (such as price intervals, interest rate bounds, or profit ranges), subsets of the real number line \\(\\mathbb{R}\\) are expressed as intervals:
  </p>
  <table class="table-styled">
    <thead>
      <tr>
        <th>Interval Notation</th>
        <th>Set-Builder Definition</th>
        <th>Geometric Representation on Real Line</th>
        <th>Length</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Closed:</strong> \\([a, b]\\)</td>
        <td>\\(\\{x \\in \\mathbb{R} : a \\le x \\le b\\}\\)</td>
        <td>Solid circles at both endpoints \\(a\\) and \\(b\\)</td>
        <td>\\(b - a\\)</td>
      </tr>
      <tr>
        <td><strong>Open:</strong> \\((a, b)\\)</td>
        <td>\\(\\{x \\in \\mathbb{R} : a < x < b\\}\\)</td>
        <td>Hollow circles at endpoints \\(a\\) and \\(b\\)</td>
        <td>\\(b - a\\)</td>
      </tr>
      <tr>
        <td><strong>Semi-Open / Right-Half-Open:</strong> \\([a, b)\\)</td>
        <td>\\(\\{x \\in \\mathbb{R} : a \\le x < b\\}\\)</td>
        <td>Solid circle at \\(a\\), hollow circle at \\(b\\)</td>
        <td>\\(b - a\\)</td>
      </tr>
      <tr>
        <td><strong>Semi-Closed / Left-Half-Open:</strong> \\((a, b]\\)</td>
        <td>\\(\\{x \\in \\mathbb{R} : a < x \\le b\\}\\)</td>
        <td>Hollow circle at \\(a\\), solid circle at \\(b\\)</td>
        <td>\\(b - a\\)</td>
      </tr>
      <tr>
        <td><strong>Infinite Ray:</strong> \\([a, \\infty)\\)</td>
        <td>\\(\\{x \\in \\mathbb{R} : x \\ge a\\}\\)</td>
        <td>Solid circle at \\(a\\), extending infinitely rightward</td>
        <td>Infinite</td>
      </tr>
    </tbody>
  </table>

  <h3>3. The Power Set Hierarchy and Iterated Power Sets</h3>
  <p>
    The power set \\(P(A)\\) is always non-empty, even when \\(A\\) is the empty set:
  </p>
  <ul>
    <li>If \\(A = \\emptyset\\), then \\(n(A) = 0\\). Therefore \\(P(\\emptyset) = \\{\\emptyset\\}\\), with cardinality \\(n(P(\\emptyset)) = 2^0 = 1\\).</li>
    <li>For the second iteration: \\(P(P(\\emptyset)) = P(\\{\\emptyset\\}) = \\{\\emptyset, \\{\\emptyset\\}\\}\\), with cardinality \\(2^1 = 2\\).</li>
    <li>For the third iteration: \\(P(P(P(\\emptyset))) = \\{\\emptyset, \\{\\emptyset\\}, \\{\\{\\emptyset\\}\\}, \\{\\emptyset, \\{\\emptyset\\}\\}\\}\\), with cardinality \\(2^2 = 4\\).</li>
    <li>For the fourth iteration: \\(n(P(P(P(P(\\emptyset))))) = 2^4 = 16\\).</li>
  </ul>

  <div class="worked-example">
    <h4>Comprehensive Worked Example: Financial Portfolio Asset Allocation</h4>
    <p><strong>Problem:</strong> A hedge fund can select any combination of investments from a basket of 4 assets: \\(A = \\{\\text{Equities}, \\text{Bonds}, \\text{Gold}, \\text{Real Estate}\\}\\).</p>
    <ol>
      <li>How many distinct portfolio asset allocations (subsets) can be formulated?</li>
      <li>How many active portfolios can be constructed containing at least one asset?</li>
      <li>How many portfolios contain <strong>Equities</strong>?</li>
      <li>If a regulatory constraint requires portfolios to contain between 2 and 3 assets inclusive, how many such valid portfolios exist?</li>
    </ol>
    <div class="solution">
      <p><strong>Solution:</strong></p>
      <ol>
        <li>The total number of possible subsets of set \\(A\\) with \\(n=4\\) assets is:
          \\[ 2^n = 2^4 = 16 \\text{ portfolios.} \\]
          This includes the cash-only portfolio \\(\\emptyset\\) (investing in none of the 4 assets).
        </li>
        <li>Active portfolios containing at least one asset exclude \\(\\emptyset\\):
          \\[ 2^4 - 1 = 16 - 1 = 15 \\text{ active portfolios.} \\]
        </li>
        <li>Portfolios containing <strong>Equities</strong>: We fix Equities in the portfolio. The remaining 3 assets can either be included or excluded in \\(2^3 = 8\\) ways. Hence, exactly 8 portfolios contain Equities.</li>
        <li>Portfolios containing between 2 and 3 assets:
          \\[ \\binom{4}{2} + \\binom{4}{3} = \\frac{4 \\times 3}{2} + 4 = 6 + 4 = 10 \\text{ valid portfolios.} \\]
        </li>
      </ol>
    </div>
  </div>
`;

// 2. PROGRESS TAB
const progressHtml = `
  <h2>Progress Tracker & Self-Assessment Checklist</h2>
  <p>Track your conceptual mastery and computational proficiency across Subsets, Power Sets, and Universal Sets.</p>
  <div class="checklist-grid">
    <div class="checklist-card">
      <h4>Conceptual Milestones</h4>
      <ul>
        <li><label><input type="checkbox"> Can mathematically distinguish between element belonging (\\(\\in\\)) and subset inclusion (\\(\\subseteq\\)).</label></li>
        <li><label><input type="checkbox"> Understand why the empty set \\(\\emptyset\\) is a subset of every set and why every set is a subset of itself.</label></li>
        <li><label><input type="checkbox"> Can determine the number of subsets (\\(2^n\\)) and proper subsets (\\(2^n - 1\\)) for any finite set.</label></li>
        <li><label><input type="checkbox"> Master interval notation on \\(\\mathbb{R}\\): open, closed, semi-open, and infinite rays.</label></li>
        <li><label><input type="checkbox"> Can construct the power set \\(P(A)\\) and calculate iterated power set cardinalities \\(n(P(P(A)))\\).</label></li>
      </ul>
    </div>
    <div class="checklist-card">
      <h4>Problem Solving Milestones</h4>
      <ul>
        <li><label><input type="checkbox"> Solved nested set membership problems (e.g., \\(\\{\\{a, b\\}\\} \\subseteq A\\)).</label></li>
        <li><label><input type="checkbox"> Handled combinatorics on subsets with constraints (e.g., subsets containing specific elements).</label></li>
        <li><label><input type="checkbox"> Formulated subset allocations in applied business and financial decision scenarios.</label></li>
        <li><label><input type="checkbox"> Completed the 10-Question Diagnostic Mock with a score of 80% or higher.</label></li>
      </ul>
    </div>
  </div>
`;

// 3. WORKSHEET TAB
const worksheetHtml = `
  <h2>Practice Worksheet: Graded Exercises & Case Problems</h2>
  <p>Work through these graded problems from foundational mechanics to applied multi-stage scenarios.</p>

  <div class="problem-card">
    <h4>Problem 1 (Foundational: Membership vs Inclusion)</h4>
    <p>Let \\(A = \\{1, 2, \\{3, 4\\}, 5\\}\\). Determine whether each of the following statements is True or False:</p>
    <ol type="a">
      <li>\\(\\{3, 4\\} \\subset A\\)</li>
      <li>\\(\\{\\{3, 4\\}\\} \\subset A\\)</li>
      <li>\\(\\{1, 2, 5\\} \\subseteq A\\)</li>
      <li>\\(\\emptyset \\in A\\)</li>
      <li>\\(\\emptyset \\subseteq A\\)</li>
    </ol>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        <ul>
          <li><strong>(a) False:</strong> The object \\(\\{3, 4\\}\\) is an element of \\(A\\) (i.e. \\(\\{3, 4\\} \\in A\\)), not a subset. 3 and 4 are not separate elements of \\(A\\).</li>
          <li><strong>(b) True:</strong> Since \\(\\{3, 4\\} \\in A\\), the set containing that element, \\(\\{\\{3, 4\\}\\}\\), is a valid subset of \\(A\\).</li>
          <li><strong>(c) True:</strong> The elements 1, 2, and 5 all belong individually to \\(A\\). Thus \\(\\{1, 2, 5\\} \\subseteq A\\).</li>
          <li><strong>(d) False:</strong> The empty set \\(\\emptyset\\) is not listed as an explicit element inside \\(A\\).</li>
          <li><strong>(e) True:</strong> The empty set is vacuously a subset of every set.</li>
        </ul>
      </div>
    </details>
  </div>

  <div class="problem-card">
    <h4>Problem 2 (Counting Subsets: Simultaneous Equations)</h4>
    <p>Two finite sets \\(A\\) and \\(B\\) have \\(m\\) and \\(k\\) elements respectively. The total number of subsets of \\(A\\) is 56 more than the total number of subsets of \\(B\\). Find the values of \\(m\\) and \\(k\\).</p>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        <p>The number of subsets of \\(A\\) is \\(2^m\\) and of \\(B\\) is \\(2^k\\). We are given:
          \\[ 2^m - 2^k = 56 \\]
        Since 56 is positive, \\(m > k\\). Factor out \\(2^k\\):
          \\[ 2^k (2^{m-k} - 1) = 56 \\]
        Express 56 as the product of a power of 2 and an odd integer:
          \\[ 56 = 8 \\times 7 = 2^3 \\times (2^3 - 1) \\]
        Equating the powers of 2 and the odd factors:
          \\[ 2^k = 2^3 \\implies k = 3 \\]
          \\[ 2^{m-k} - 1 = 7 \\implies 2^{m-3} = 8 = 2^3 \\implies m - 3 = 3 \\implies m = 6 \\]
        <strong>Answer:</strong> \\(m = 6\\) and \\(k = 3\\).
        (Verification: \\(2^6 - 2^3 = 64 - 8 = 56\\). Correct.)
        </p>
      </div>
    </details>
  </div>

  <div class="problem-card">
    <h4>Problem 3 (Interval Subsets of \\(\\mathbb{R}\\))</h4>
    <p>Let \\(A = [-3, 5)\\) and \\(B = (0, 7]\\). Express the following in interval notation:</p>
    <ol type="a">
      <li>\\(A \\cap B\\)</li>
      <li>\\(A \\cup B\\)</li>
      <li>\\(A - B\\)</li>
    </ol>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        <ul>
          <li><strong>(a) \\(A \\cap B\\):</strong> The overlap of \\([-3, 5)\\) and \\((0, 7]\\) contains all real numbers \\(x\\) such that \\(0 < x < 5\\). In interval notation: <strong>\\((0, 5)\\)</strong>.</li>
          <li><strong>(b) \\(A \\cup B\\):</strong> The union spans from the minimum left endpoint \\(-3\\) (included) to the maximum right endpoint \\(7\\) (included). In interval notation: <strong>\\([-3, 7]\\)</strong>.</li>
          <li><strong>(c) \\(A - B\\):</strong> Elements in \\(A\\) that are not in \\(B\\). Since \\(B = (0, 7]\\), removing \\(B\\) from \\([-3, 5)\\) leaves the interval from \\(-3\\) up to and including 0. In interval notation: <strong>\\([-3, 0]\\)</strong>.</li>
        </ul>
      </div>
    </details>
  </div>

  <div class="problem-card">
    <h4>Problem 4 (Iterated Power Sets)</h4>
    <p>Find the cardinality of the power set \\(P(P(P(A)))\\) if \\(A = \\{x\\}\\) is a singleton set.</p>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        <p>Given \\(n(A) = 1\\):</p>
        <ol>
          <li>\\(n(P(A)) = 2^{n(A)} = 2^1 = 2\\).</li>
          <li>\\(n(P(P(A))) = 2^{n(P(A))} = 2^2 = 4\\).</li>
          <li>\\(n(P(P(P(A)))) = 2^{n(P(P(A)))} = 2^4 = 16\\).</li>
        </ol>
        <p><strong>Answer:</strong> 16.</p>
      </div>
    </details>
  </div>
`;

// 4. REVISION TAB
const revisionHtml = `
  <h2>Quick Revision & Formula Cheat Sheet</h2>
  <div class="revision-grid">
    <div class="revision-card">
      <h4>Subset Quick Reference</h4>
      <ul>
        <li>\\(A \\subseteq B \\iff (x \\in A \\implies x \\in B)\\)</li>
        <li>\\(\\emptyset \\subseteq A\\) for any set \\(A\\)</li>
        <li>\\(A \\subseteq A\\) (Reflexivity of inclusion)</li>
        <li>If \\(A \\subseteq B\\) and \\(B \\subseteq A\\), then \\(A = B\\)</li>
        <li>If \\(A \\subseteq B\\) and \\(B \\subseteq C\\), then \\(A \\subseteq C\\)</li>
      </ul>
    </div>
    <div class="revision-card">
      <h4>Counting Formulas</h4>
      <ul>
        <li>Total subsets of set with \\(n\\) elements: \\(2^n\\)</li>
        <li>Total proper subsets: \\(2^n - 1\\)</li>
        <li>Total non-empty subsets: \\(2^n - 1\\)</li>
        <li>Subsets of size \\(k\\): \\(\\binom{n}{k} = \\frac{n!}{k!(n-k)!}\\)</li>
      </ul>
    </div>
    <div class="revision-card">
      <h4>Interval Types Summary</h4>
      <ul>
        <li><strong>\\([a, b]\\):</strong> \\(a \\le x \\le b\\) (Both closed)</li>
        <li><strong>\\((a, b)\\):</strong> \\(a < x < b\\) (Both open)</li>
        <li><strong>\\([a, b)\\):</strong> \\(a \\le x < b\\) (Left closed, right open)</li>
        <li><strong>\\((a, b]\\):</strong> \\(a < x \\le b\\) (Left open, right closed)</li>
      </ul>
    </div>
    <div class="revision-card">
      <h4>Power Set Key Facts</h4>
      <ul>
        <li>\\(P(A) = \\{X : X \\subseteq A\\}\\)</li>
        <li>\\(\\emptyset \\in P(A)\\) and \\(A \\in P(A)\\) always</li>
        <li>\\(n(P(A)) = 2^{n(A)}\\)</li>
        <li>If \\(A = \\emptyset\\), \\(P(A) = \\{\\emptyset\\}\\), \\(n(P(A)) = 1\\)</li>
      </ul>
    </div>
  </div>
`;

// 5. MOCK EXAM TAB
const mockHtml = `
  <h2>10-Question Diagnostic Mock Exam</h2>
  <p class="lead-p">Test your mastery of Subsets, Power Sets, Intervals, and Universal Sets under timed CBSE examination conditions.</p>
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
    question: "If a set \\(A\\) contains 5 distinct elements, what is the total number of non-empty proper subsets of \\(A\\)?",
    options: ["32", "31", "30", "25"],
    correct: 2,
    explanation: "Total subsets = \\(2^5 = 32\\). Proper subsets exclude \\(A\\) itself (31). Non-empty proper subsets also exclude \\(\\emptyset\\), leaving \\(32 - 2 = 30\\)."
  },
  {
    id: 2,
    question: "Let \\(A = \\{1, 2, \\{3\\}\\}\\). Which of the following statements is mathematically FALSE?",
    options: ["\\(\\{3\\} \\in A\\)", "\\(\\{\\{3\\}\\} \\subseteq A\\)", "\\(\\{3\\} \\subseteq A\\)", "\\(\\{1, 2\\} \\subseteq A\\)"],
    correct: 2,
    explanation: "\\(\\{3\\}\\) is an element of \\(A\\) (so \\(\\{3\\} \\in A\\) is true). The set containing that element is \\(\\{\\{3\\}\\}\\), which is a subset. But \\(\\{3\\} \\subseteq A\\) is false because 3 is not an individual element of \\(A\\)."
  },
  {
    id: 3,
    question: "What is the cardinality of \\(P(P(\\emptyset))\\)?",
    options: ["0", "1", "2", "4"],
    correct: 2,
    explanation: "\\(n(\\emptyset) = 0\\). \\(n(P(\\emptyset)) = 2^0 = 1\\). Therefore, \\(n(P(P(\\emptyset))) = 2^1 = 2\\)."
  },
  {
    id: 4,
    question: "Two finite sets have \\(m\\) and \\(n\\) elements. If the total number of subsets of the first set is 112 more than the total number of subsets of the second set, find the values of \\(m\\) and \\(n\\).",
    options: ["\\(m=7, n=4\\)", "\\(m=8, n=4\\)", "\\(m=6, n=3\\)", "\\(m=7, n=5\\)"],
    correct: 0,
    explanation: "\\(2^m - 2^n = 112 \\implies 2^n(2^{m-n} - 1) = 112 = 16 \\times 7 = 2^4(2^3 - 1)\\). Equating powers: \\(n = 4\\) and \\(m - n = 3 \\implies m = 7\\)."
  },
  {
    id: 5,
    question: "Which of the following represents the interval \\((-4, 6]\\) in set-builder form?",
    options: [
      "\\(\\{x \\in \\mathbb{R} : -4 \\le x < 6\\}\\)",
      "\\(\\{x \\in \\mathbb{R} : -4 < x \\le 6\\}\\)",
      "\\(\\{x \\in \\mathbb{R} : -4 < x < 6\\}\\)",
      "\\(\\{x \\in \\mathbb{R} : -4 \\le x \\le 6\\}\\)"
    ],
    correct: 1,
    explanation: "Parenthesis \\((\\) means open (strict inequality \\(>\\)), and bracket \\(]\\) means closed (\\(\\le\\)). Hence \\(\\{x \\in \\mathbb{R} : -4 < x \\le 6\\}\\)."
  },
  {
    id: 6,
    question: "If \\(A \\subseteq B\\), then which of the following is always true?",
    options: ["\\(A \\cup B = A\\)", "\\(A \\cap B = B\\)", "\\(A - B = \\emptyset\\)", "\\(B - A = \\emptyset\\)"],
    correct: 2,
    explanation: "If every element of \\(A\\) is in \\(B\\), removing all elements of \\(B\\) from \\(A\\) leaves no elements, so \\(A - B = \\emptyset\\)."
  },
  {
    id: 7,
    question: "If set \\(X = \\{a, b, c, d\\}\\), how many subsets of \\(X\\) contain the element \\(a\\) but do NOT contain the element \\(b\\)?",
    options: ["2", "4", "8", "16"],
    correct: 1,
    explanation: "We fix element \\(a\\) as included (1 choice) and \\(b\\) as excluded (1 choice). The remaining 2 elements \\(\\{c, d\\}\\) can be independently included or excluded in \\(2^2 = 4\\) ways."
  },
  {
    id: 8,
    question: "What is the intersection of intervals \\([-5, 3)\\) and \\((-2, 8]\\)?",
    options: ["\\([-5, 8]\\)", "\\((-2, 3)\\)", "\\([-2, 3]\\)", "\\((-5, 8)\\)"],
    correct: 1,
    explanation: "The overlap starts strictly after \\(-2\\) and ends strictly before \\(3\\). Thus, \\((-2, 3)\\)."
  },
  {
    id: 9,
    question: "If \\(P(A)\\) has 64 elements, how many elements does set \\(A\\) have?",
    options: ["5", "6", "7", "8"],
    correct: 1,
    explanation: "\\(n(P(A)) = 2^{n(A)} = 64 = 2^6 \\implies n(A) = 6\\)."
  },
  {
    id: 10,
    question: "Let \\(U = \\{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\\}\\) be the universal set. If \\(A = \\{x \\in U : x \\text{ is prime}\\}\\), what is \\(n(P(A))\\)?",
    options: ["8", "16", "32", "64"],
    correct: 1,
    explanation: "The prime numbers in \\(U\\) are \\(\\{2, 3, 5, 7\\}\\), so \\(n(A) = 4\\). Therefore, \\(n(P(A)) = 2^4 = 16\\)."
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
    resultsBox.innerHTML += '<p style="color:#059669; font-weight:600;">Excellent! Outstanding mastery of Subsets, Power Sets, and Intervals.</p>';
  } else if (pct >= 50) {
    resultsBox.innerHTML += '<p style="color:#d97706; font-weight:600;">Good effort! Review the detailed explanations and retry missed problems.</p>';
  } else {
    resultsBox.innerHTML += '<p style="color:#dc2626; font-weight:600;">Needs revision. Review the Learn tab definitions and worksheet problems before attempting again.</p>';
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
console.log('Successfully upgraded 4-3-subsets-power-sets-and-universal-sets/index.html');
