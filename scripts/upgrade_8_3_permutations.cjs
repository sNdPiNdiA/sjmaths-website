const fs = require('fs');
const cheerio = require('cheerio');

const filePath = 'class-11-applied-mathematics/chapter-8-combinatorics/8-3-permutations/index.html';
const html = fs.readFileSync(filePath, 'utf8');
const $ = cheerio.load(html);

// 1. LEARN TAB
const learnHtml = `
  <h2>8.3 Permutations: Ordered Arrangements, Constrained Groupings, and Multiset Permutations</h2>
  <p class="lead-p">
    In Applied Mathematics, cryptographic key design, and process scheduling, a <strong>permutation</strong> is an arrangement of items where <em>order strictly matters</em>. Whether sequencing industrial operations on an assembly line or generating secure alphanumeric passwords, permutations quantify ordered configurations.
  </p>

  <div class="formula-box">
    <h3>Fundamental Formulae & Theorems</h3>
    <ul>
      <li><strong>Definition:</strong> The number of permutations of \\(n\\) distinct objects taken \\(r\\) at a time without repetition is denoted by \\(^n P_r\\) or \\(P(n, r)\\):
        \\[ ^n P_r = \\frac{n!}{(n - r)!} = n(n - 1)(n - 2)\\dots(n - r + 1) \\quad (0 \\le r \\le n) \\]
      </li>
      <li><strong>Boundary Cases:</strong>
        \\[ ^n P_n = \\frac{n!}{0!} = n!, \\quad ^n P_0 = \\frac{n!}{n!} = 1, \\quad ^n P_1 = n \\]
      </li>
      <li><strong>Permutations with Repetition Allowed:</strong>
        The number of arrangements of \\(n\\) distinct objects taken \\(r\\) at a time when repetition is permitted:
        \\[ \\text{Arrangements} = n^r \\]
      </li>
      <li><strong>Permutations of Objects Not All Distinct (Multisets):</strong>
        If a collection of \\(n\\) objects contains \\(p_1\\) objects of type 1, \\(p_2\\) of type 2, \\dots, \\(p_k\\) of type \\(k\\) (where \\(p_1 + p_2 + \\dots + p_k = n\\)):
        \\[ \\text{Distinct Permutations} = \\frac{n!}{p_1! \\cdot p_2! \\cdot \\dots \\cdot p_k!} \\]
      </li>
      <li><strong>Circular Permutations:</strong>
        The number of ways to arrange \\(n\\) distinct objects in a closed loop or circle:
        \\[ \\text{Circular Arrangements} = (n - 1)! \\]
        <em>Necklaces & Garlands (where clockwise and counter-clockwise are identical):</em>
        \\[ \\text{Ways} = \\frac{(n - 1)!}{2} \\]
      </li>
    </ul>
  </div>

  <h3>Systematic Problem-Solving Strategies</h3>
  <table class="table-styled">
    <thead>
      <tr>
        <th>Constraint Type</th>
        <th>Standard Method</th>
        <th>Algebraic Strategy</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Items MUST be together</strong> (e.g. All vowels together)</td>
        <td><strong>String / Block Method</strong></td>
        <td>Tie the constrained objects into a single super-object. Arrange the \\((n - k + 1)\\) entities in \\((n - k + 1)!\\) ways, then multiply by internal permutations \\(k!\\) of the super-object.</td>
      </tr>
      <tr>
        <td><strong>Items must NEVER be together</strong> (e.g. No two boys together)</td>
        <td><strong>Gap Method</strong></td>
        <td>Arrange the unconstrained objects first. If there are \\(m\\) unconstrained objects, they create \\((m + 1)\\) available gaps (including ends). Choose and arrange the constrained items in these gaps.</td>
      </tr>
      <tr>
        <td><strong>Fixed positions</strong> (e.g. Word begins with 'P' and ends with 'S')</td>
        <td><strong>Slot Anchoring</strong></td>
        <td>Fill the fixed positions with 1 choice each, then permute the remaining \\((n - 2)\\) items in \\((n - 2)!\\) ways.</td>
      </tr>
    </tbody>
  </table>

  <div class="worked-example">
    <h4>Comprehensive Word Permutation Example: The Word "MATHEMATICS"</h4>
    <p><strong>Problem:</strong> Consider the word <strong>MATHEMATICS</strong>. There are 11 letters in total:</p>
    <ul>
      <li>M appears 2 times, A appears 2 times, T appears 2 times</li>
      <li>H, E, I, C, S appear 1 time each</li>
      <li>Vowels: \\(\\{\\text{A, E, A, I}\\}\\) (4 vowels: two A's, one E, one I)</li>
      <li>Consonants: \\(\\{\\text{M, T, H, M, T, C, S}\\}\\) (7 consonants: two M's, two T's)</li>
    </ul>
    <p>Find the number of arrangements if:</p>
    <ol>
      <li>There are no restrictions.</li>
      <li>All vowels must always occur together.</li>
      <li>No two vowels can occur together (gap method).</li>
    </ol>
    <div class="solution">
      <p><strong>Solution:</strong></p>
      <ol>
        <li><strong>No restrictions:</strong>
          \\[ \\frac{11!}{2! \\cdot 2! \\cdot 2!} = \\frac{39{,}916{,}800}{8} = 4{,}989{,}600 \\text{ arrangements.} \\]
        </li>
        <li><strong>All vowels together (String Method):</strong>
          Treat the 4 vowels \\([\\text{A, E, A, I}]\\) as a single super-block.
          Now we arrange 7 consonants + 1 vowel block = 8 entities:
          \\[ \\text{Ways to arrange 8 entities} = \\frac{8!}{2! \\cdot 2!} = \\frac{40{,}320}{4} = 10{,}080. \\]
          Internal arrangements within the vowel block (4 vowels with two A's):
          \\[ \\text{Vowel block permutations} = \\frac{4!}{2!} = \\frac{24}{2} = 12. \\]
          Total arrangements = \\(10{,}080 \\times 12 = 120{,}960\\).
        </li>
        <li><strong>No two vowels together (Gap Method):</strong>
          First arrange the 7 consonants (with two M's and two T's):
          \\[ \\text{Ways to arrange consonants} = \\frac{7!}{2! \\cdot 2!} = \\frac{5{,}040}{4} = 1{,}260. \\]
          7 consonants create \\(7 + 1 = 8\\) gaps:
          \\[ \\_ \\text{ C}_1 \\_ \\text{ C}_2 \\_ \\text{ C}_3 \\_ \\text{ C}_4 \\_ \\text{ C}_5 \\_ \\text{ C}_6 \\_ \\text{ C}_7 \\_ \\]
          We place 4 vowels into these 8 gaps. The number of ways to choose 4 gaps and arrange the vowels (two A's):
          \\[ \\binom{8}{4} \\times \\frac{4!}{2!} = 70 \\times 12 = 840. \\]
          Total arrangements = \\(1{,}260 \\times 840 = 1{,}058{,}400\\).
        </li>
      </ol>
    </div>
  </div>
`;

// 2. PROGRESS TAB
const progressHtml = `
  <h2>Progress Tracker & Self-Assessment Checklist</h2>
  <p>Track your computational speed and mastery of Permutations and Arrangement Techniques.</p>
  <div class="checklist-grid">
    <div class="checklist-card">
      <h4>Conceptual Milestones</h4>
      <ul>
        <li><label><input type="checkbox"> Compute \\(^n P_r = \\frac{n!}{(n-r)!}\\) quickly.</label></li>
        <li><label><input type="checkbox"> Apply the Multiset Permutation formula for words with repeating letters.</label></li>
        <li><label><input type="checkbox"> Master the String Method for "together" constraints.</label></li>
        <li><label><input type="checkbox"> Master the Gap Method for "never together" constraints.</label></li>
        <li><label><input type="checkbox"> Understand Circular permutations \\((n-1)!\\) and necklace arrangements.</label></li>
      </ul>
    </div>
    <div class="checklist-card">
      <h4>Problem Solving Milestones</h4>
      <ul>
        <li><label><input type="checkbox"> Solved dictionary rank problems (finding word rank in alphabetical listing).</label></li>
        <li><label><input type="checkbox"> Solved circular seating arrangements with alternating gender constraints.</label></li>
        <li><label><input type="checkbox"> Solved letter anagram problems with multiple identical characters.</label></li>
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
    <h4>Problem 1 (Solving for \\(n\\) and \\(r\\) in Permutations)</h4>
    <p>Find \\(n\\) if \\(^n P_4 : {}^{n-1}P_4 = 5 : 3\\), where \\(n > 4\\).</p>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        \\[ \\frac{^n P_4}{^{n-1}P_4} = \\frac{\\frac{n!}{(n - 4)!}}{\\frac{(n - 1)!}{(n - 1 - 4)!}} = \\frac{n!}{(n - 4)!} \\times \\frac{(n - 5)!}{(n - 1)!} \\]
        \\[ = \\frac{n(n - 1)!}{(n - 4)(n - 5)!} \\times \\frac{(n - 5)!}{(n - 1)!} = \\frac{n}{n - 4} \\]
        Given ratio:
        \\[ \\frac{n}{n - 4} = \\frac{5}{3} \\implies 3n = 5n - 20 \\implies 2n = 20 \\implies n = 10. \\]
        <strong>Answer:</strong> \\(n = 10\\).
      </div>
    </details>
  </div>

  <div class="problem-card">
    <h4>Problem 2 (Circular Seating Arrangement with Constraints)</h4>
    <p>In how many ways can 5 Indian and 5 Japanese executives sit around a round conference table so that no two Indian executives sit together?</p>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        <p>Use the Gap Method in a circle:</p>
        <ol>
          <li>First seat the 5 Japanese executives around the circle. Since circular arrangements of 5 distinct entities have \\((5 - 1)! = 4!\\) ways:
            \\[ 4! = 24 \\text{ ways.} \\]
          </li>
          <li>The 5 seated Japanese executives create exactly 5 gaps between them in the circle:
            Notice that in a circle, \\(n\\) objects create exactly \\(n\\) gaps (not \\(n+1\\)).
          </li>
          <li>Now place the 5 Indian executives into these 5 gaps. Because the positions are now defined relative to the already-seated Japanese executives, this is a standard linear permutation:
            \\[ 5! = 120 \\text{ ways.} \\]
          </li>
        </ol>
        Total ways = \\(4! \\times 5! = 24 \\times 120 = 2{,}880\\) ways.
      </div>
    </details>
  </div>

  <div class="problem-card">
    <h4>Problem 3 (Dictionary Rank Problem)</h4>
    <p>If all the letters of the word <strong>RANDOM</strong> are permuted and listed in dictionary (alphabetical) order, what is the rank of the word "RANDOM"?</p>
    <details>
      <summary>View Step-by-Step Solution</summary>
      <div class="solution-content">
        <p><strong>Solution:</strong></p>
        <p>Alphabetical order of letters in RANDOM: <strong>A, D, M, N, O, R</strong> (6 distinct letters).</p>
        <ul>
          <li>Words starting with A: \\(5! = 120\\)</li>
          <li>Words starting with D: \\(5! = 120\\)</li>
          <li>Words starting with M: \\(5! = 120\\)</li>
          <li>Words starting with N: \\(5! = 120\\)</li>
          <li>Words starting with O: \\(5! = 120\\)</li>
          <li>Now start with R:
            <ul>
              <li>Next letter is A (matches RANDOM).</li>
              <li>Next letter alphabetically is D: Words starting with RAD: \\(3! = 6\\)</li>
              <li>Next letter is M: Words starting with RAM: \\(3! = 6\\)</li>
              <li>Next letter is N (matches RANDOM):
                <ul>
                  <li>Remaining letters: D, O, M. Alphabetically: D, M, O.</li>
                  <li>Words starting with RAND: \\(2! = 2\\) (RANDMO, RANDMO...)
                    Specifically:
                    \\(\\text{RANDMO} = 1\\)
                    \\(\\text{RANDOM} = 2\\)
                  </li>
                </ul>
              </li>
            </ul>
          </li>
        </ul>
        Summing preceding words:
        \\[ 5 \\times 120 + 6 + 6 + 1 + 1 = 600 + 12 + 2 = 614. \\]
        <strong>Rank of RANDOM = 614</strong>.
      </div>
    </details>
  </div>
`;

// 4. REVISION TAB
const revisionHtml = `
  <h2>Quick Revision & Formula Cheat Sheet</h2>
  <div class="revision-grid">
    <div class="revision-card">
      <h4>Permutation Formulas</h4>
      <ul>
        <li>\\(^n P_r = \\frac{n!}{(n - r)!}\\)</li>
        <li>\\(^n P_n = n!\\)</li>
        <li>Repetition allowed: \\(n^r\\)</li>
        <li>Multisets: \\(\\frac{n!}{p_1! p_2! \\dots p_k!}\\)</li>
      </ul>
    </div>
    <div class="revision-card">
      <h4>Circular Arrangements</h4>
      <ul>
        <li>Circular: \\((n - 1)!\\)</li>
        <li>Garlands/Necklaces: \\(\\frac{(n - 1)!}{2}\\)</li>
        <li>In a circle, \\(n\\) seated people create exactly \\(n\\) gaps</li>
      </ul>
    </div>
    <div class="revision-card">
      <h4>Technique Framework</h4>
      <ul>
        <li><strong>Together:</strong> Tie into block, arrange, then permute block interior</li>
        <li><strong>Separated:</strong> Arrange non-constrained items, insert into gaps</li>
        <li><strong>Dictionary Rank:</strong> Alphabetize letters and count blocks by initial letters</li>
      </ul>
    </div>
  </div>
`;

// 5. MOCK EXAM TAB
const mockHtml = `
  <h2>10-Question Diagnostic Mock Exam</h2>
  <p class="lead-p">Test your mastery of Permutations, Word Anagrams, and Circular Arrangements under timed CBSE conditions.</p>
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
    question: "What is the value of \\(^7 P_3\\)?",
    options: ["35", "210", "420", "840"],
    correct: 1,
    explanation: "\\(^7 P_3 = 7 \\times 6 \\times 5 = 210\\)."
  },
  {
    id: 2,
    question: "If \\(^n P_5 = 42 \\times {}^n P_3\\), find \\(n\\) (for \\(n > 4\\)).",
    options: ["7", "9", "10", "12"],
    correct: 2,
    explanation: "\\(n(n-1)(n-2)(n-3)(n-4) = 42 \\times n(n-1)(n-2) \\implies (n-3)(n-4) = 42 = 7 \\times 6 \\implies n - 3 = 7 \\implies n = 10\\)."
  },
  {
    id: 3,
    question: "How many different words can be formed from the letters of the word 'ALLAHABAD'?",
    options: ["3780", "7560", "15120", "30240"],
    correct: 1,
    explanation: "ALLAHABAD has 9 letters: 4 A's, 2 L's, 1 H, 1 B, 1 D. \\(\\frac{9!}{4! \\times 2!} = \\frac{362880}{24 \\times 2} = \\frac{362880}{48} = 7560\\)."
  },
  {
    id: 4,
    question: "In how many ways can 6 people be seated at a round table?",
    options: ["60", "120", "360", "720"],
    correct: 1,
    explanation: "Circular permutations of \\(n\\) people = \\((n - 1)! = 5! = 120\\)."
  },
  {
    id: 5,
    question: "In how many ways can 8 different beads be strung into a necklace?",
    options: ["2520", "5040", "20160", "40320"],
    correct: 0,
    explanation: "Necklace arrangements = \\(\\frac{(n - 1)!}{2} = \\frac{7!}{2} = \\frac{5040}{2} = 2520\\)."
  },
  {
    id: 6,
    question: "How many 4-letter permutations can be formed from the word 'ROSE' if repetition is not allowed?",
    options: ["12", "16", "24", "64"],
    correct: 2,
    explanation: "\\(^4 P_4 = 4! = 24\\)."
  },
  {
    id: 7,
    question: "In how many ways can the letters of the word 'EQUATION' be arranged so that all the vowels occur together?",
    options: ["1440", "2880", "4320", "7200"],
    correct: 2,
    explanation: "EQUATION has 8 letters: 5 vowels (E, U, A, I, O) and 3 consonants (Q, T, N). Treat 5 vowels as 1 block. Total entities = 3 + 1 = 4. Arrangements = \\(4! \\times 5! = 24 \\times 120 = 2880\\dots\\) Wait! Let's check: 3 consonants + 1 vowel block = 4 entities. \\(4! = 24\\). 5 vowels can be arranged among themselves in \\(5! = 120\\) ways. \\(24 \\times 120 = 2880\\) ways!"
  },
  {
    id: 8,
    question: "If \\(^n P_r = 720\\) and \\(^n C_r = 120\\), what is the value of \\(r\\)?",
    options: ["2", "3", "4", "5"],
    correct: 1,
    explanation: "\\(r! = \\frac{^n P_r}{^n C_r} = \\frac{720}{120} = 6 = 3! \\implies r = 3\\)."
  },
  {
    id: 9,
    question: "In how many ways can 4 boys and 4 girls sit in a row so that boys and girls sit alternately?",
    options: ["576", "1152", "2304", "40320"],
    correct: 1,
    explanation: "Two patterns: BGBGBGBG or GBGBGBGB. For each pattern, boys can sit in \\(4!\\) ways and girls in \\(4!\\) ways. Total = \\(2 \\times 4! \\times 4! = 2 \\times 24 \\times 24 = 1152\\) ways."
  },
  {
    id: 10,
    question: "What is the number of permutations of \\(n\\) distinct objects taken \\(r\\) at a time when a particular object is always to be excluded?",
    options: ["\\(^{n-1}P_r\\)", "\\(^{n-1}P_{r-1}\\)", "\\(r \\cdot {}^{n-1}P_{r-1}\\)", "\\(^n P_{r-1}\\)"],
    correct: 0,
    explanation: "Excluding that particular object leaves \\(n - 1\\) objects from which to choose and arrange \\(r\\) items, giving \\(^{n-1}P_r\\)."
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
    resultsBox.innerHTML += '<p style="color:#059669; font-weight:600;">Outstanding! Exceptional mastery of permutations, word anagrams, and seating constraints.</p>';
  } else if (pct >= 50) {
    resultsBox.innerHTML += '<p style="color:#d97706; font-weight:600;">Good effort! Review the string and gap methods and retry.</p>';
  } else {
    resultsBox.innerHTML += '<p style="color:#dc2626; font-weight:600;">Needs revision. Study the multiset permutation formulas and circular arrangements.</p>';
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
console.log('Successfully upgraded 8-3-permutations/index.html');
