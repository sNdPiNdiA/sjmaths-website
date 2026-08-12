from pathlib import Path
from html import escape

# ============================================================
# SJMaths — CBSE Class 10 Social Science
# Economics — Chapter 1: Development
#
# Creates a reusable SST UI system:
#
# class-10-social-science/
# ├── assets/
# │   ├── css/sst.css
# │   └── js/sst.js
# └── economics/
#     └── chapter-1-development/
#         └── index.html
#
# The CSS/JS are shared by ALL SST books and chapters.
# Run this script again safely: it overwrites only these files.
# ============================================================

ROOT = Path(__file__).resolve().parent
SST = ROOT / "class-10-social-science"

SHARED_CSS = SST / "assets" / "css" / "sst.css"
SHARED_JS = SST / "assets" / "js" / "sst.js"
CHAPTER_DIR = SST / "economics" / "chapter-1-development"
CHAPTER_HTML = CHAPTER_DIR / "index.html"


def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")
    print(f"✓ {path}")


CSS = r"""
:root{
  --sst-bg:#0d0e10;
  --sst-bg-soft:#151619;
  --sst-card:#191b1f;
  --sst-card-2:#1e2025;
  --sst-text:#f4f0e9;
  --sst-muted:#aaa39a;
  --sst-dim:#77736d;
  --sst-line:rgba(255,255,255,.10);
  --sst-accent:#c99a62;
  --sst-accent-soft:rgba(201,154,98,.12);
  --sst-green:#76957c;
  --sst-red:#b56d63;
  --sst-blue:#718ba4;
  --sst-purple:#9181a0;
  --sst-shadow:0 18px 50px rgba(0,0,0,.28);
}

*{box-sizing:border-box}

html{scroll-behavior:smooth}

body{
  margin:0;
  min-height:100vh;
  color:var(--sst-text);
  background:
    radial-gradient(circle at 10% 0%,rgba(201,154,98,.10),transparent 28%),
    radial-gradient(circle at 90% 10%,rgba(113,139,164,.08),transparent 25%),
    var(--sst-bg);
  font-family:Inter,"Segoe UI",Roboto,Arial,sans-serif;
  line-height:1.55;
}

button,input{font:inherit}
button{color:inherit}

.sst-shell{
  width:min(1160px,100%);
  margin:auto;
  padding:14px 14px 60px;
}

.sst-hero{
  position:relative;
  overflow:hidden;
  padding:22px;
  border:1px solid var(--sst-line);
  border-radius:24px;
  background:linear-gradient(145deg,#202126,#131417);
  box-shadow:var(--sst-shadow);
}

.sst-hero:after{
  content:"";
  position:absolute;
  width:210px;
  height:210px;
  right:-80px;
  top:-100px;
  border-radius:50%;
  background:var(--sst-accent);
  opacity:.10;
  filter:blur(12px);
}

.sst-breadcrumb{
  position:relative;
  z-index:1;
  display:flex;
  gap:7px;
  flex-wrap:wrap;
  color:var(--sst-dim);
  font-size:.70rem;
  font-weight:800;
}

.sst-breadcrumb b{color:#d1c8bc}

.sst-kicker{
  position:relative;
  z-index:1;
  display:inline-block;
  margin-top:23px;
  padding:6px 10px;
  border:1px solid rgba(201,154,98,.22);
  border-radius:999px;
  color:#ddc29f;
  background:var(--sst-accent-soft);
  font-size:.66rem;
  font-weight:900;
  text-transform:uppercase;
  letter-spacing:.10em;
}

.sst-hero h1{
  position:relative;
  z-index:1;
  margin:12px 0 5px;
  font-size:clamp(2rem,7vw,3.5rem);
  line-height:1.02;
  letter-spacing:-.055em;
}

.sst-subtitle{
  position:relative;
  z-index:1;
  margin:0;
  color:var(--sst-muted);
  font-family:Georgia,"Times New Roman",serif;
  font-size:.92rem;
}

.sst-meta{
  position:relative;
  z-index:1;
  display:flex;
  gap:18px;
  margin-top:20px;
}

.sst-meta strong{display:block;font-size:.95rem}
.sst-meta span{
  display:block;
  color:var(--sst-dim);
  font-size:.64rem;
  text-transform:uppercase;
  letter-spacing:.07em;
}

.sst-tabs{
  position:sticky;
  top:0;
  z-index:20;
  display:flex;
  gap:6px;
  overflow-x:auto;
  margin-top:14px;
  padding:6px;
  border:1px solid var(--sst-line);
  border-radius:15px;
  background:rgba(20,21,24,.94);
  backdrop-filter:blur(14px);
  scrollbar-width:none;
}

.sst-tabs::-webkit-scrollbar{display:none}

.sst-tab{
  flex:0 0 auto;
  border:1px solid transparent;
  border-radius:10px;
  padding:9px 12px;
  color:#8e8a84;
  background:transparent;
  cursor:pointer;
  font-size:.71rem;
  font-weight:850;
  white-space:nowrap;
}

.sst-tab:hover{color:#eee7de}

.sst-tab.active{
  color:#1b1510;
  background:var(--sst-accent);
}

.sst-panel{
  display:none;
  padding-top:22px;
}

.sst-panel.active{display:block}

.sst-section-head{
  display:flex;
  align-items:end;
  justify-content:space-between;
  gap:12px;
  margin:4px 2px 13px;
}

.sst-section-head h2{
  margin:0;
  font-size:1.18rem;
  letter-spacing:-.025em;
}

.sst-section-head p{
  margin:3px 0 0;
  color:var(--sst-dim);
  font-size:.72rem;
}

.sst-grid{
  display:grid;
  grid-template-columns:1fr;
  gap:11px;
}

.sst-card{
  padding:16px;
  border:1px solid var(--sst-line);
  border-radius:18px;
  background:linear-gradient(145deg,var(--sst-card),#151619);
  box-shadow:0 10px 28px rgba(0,0,0,.16);
}

.sst-card h3{
  margin:0 0 7px;
  font-size:.98rem;
  line-height:1.25;
}

.sst-card p{
  margin:0;
  color:#bbb4aa;
  font-size:.82rem;
}

.sst-card ul{
  margin:9px 0 0;
  padding-left:18px;
  color:#bdb6ad;
  font-size:.80rem;
}

.sst-card li+li{margin-top:5px}

.sst-label{
  display:inline-flex;
  margin-bottom:9px;
  padding:4px 7px;
  border-radius:999px;
  color:#c9a87c;
  background:var(--sst-accent-soft);
  font-size:.61rem;
  font-weight:900;
  text-transform:uppercase;
  letter-spacing:.07em;
}

.sst-formula{
  margin-top:10px;
  padding:11px 13px;
  border-left:3px solid var(--sst-accent);
  border-radius:0 10px 10px 0;
  background:rgba(201,154,98,.07);
  color:#f0dfc7;
  font-weight:800;
}

.sst-compare{
  width:100%;
  overflow:auto;
  border:1px solid var(--sst-line);
  border-radius:15px;
}

.sst-compare table{
  width:100%;
  min-width:520px;
  border-collapse:collapse;
  font-size:.76rem;
}

.sst-compare th,
.sst-compare td{
  padding:10px 11px;
  border-bottom:1px solid var(--sst-line);
  text-align:left;
}

.sst-compare th{
  color:#e6d9ca;
  background:rgba(255,255,255,.035);
}

.sst-compare td{color:#aaa39a}

.sst-compare tr:last-child td{border-bottom:0}

.sst-question{
  padding:15px;
  border:1px solid var(--sst-line);
  border-radius:16px;
  background:rgba(255,255,255,.025);
}

.sst-question+.sst-question{margin-top:9px}

.sst-q{
  margin:0;
  font-size:.84rem;
  font-weight:800;
}

.sst-options{
  display:grid;
  gap:6px;
  margin-top:10px;
}

.sst-option{
  padding:8px 10px;
  border:1px solid var(--sst-line);
  border-radius:9px;
  color:#aaa39a;
  font-size:.75rem;
}

.sst-answer{
  display:none;
  margin-top:9px;
  padding:9px 10px;
  border-radius:9px;
  color:#d9d0c5;
  background:rgba(118,149,124,.10);
  font-size:.74rem;
}

.sst-question.revealed .sst-answer{display:block}

.sst-reveal{
  margin-top:9px;
  padding:6px 9px;
  border:1px solid var(--sst-line);
  border-radius:8px;
  color:#d7c3aa;
  background:transparent;
  cursor:pointer;
  font-size:.67rem;
  font-weight:800;
}

.sst-score{
  display:none;
  margin-top:14px;
  padding:13px;
  border:1px solid var(--sst-line);
  border-radius:13px;
  color:#ded5ca;
  background:rgba(255,255,255,.035);
  font-weight:800;
}

.sst-revision{
  display:grid;
  gap:8px;
}

.sst-revision-item{
  display:flex;
  gap:11px;
  padding:12px;
  border:1px solid var(--sst-line);
  border-radius:13px;
  background:rgba(255,255,255,.025);
}

.sst-revision-num{
  flex:0 0 28px;
  display:grid;
  place-items:center;
  width:28px;
  height:28px;
  border-radius:9px;
  color:#20170f;
  background:var(--sst-accent);
  font-size:.68rem;
  font-weight:900;
}

.sst-revision-item strong{
  display:block;
  font-size:.80rem;
}

.sst-revision-item span{
  display:block;
  margin-top:2px;
  color:#958e85;
  font-size:.72rem;
}

.sst-note{
  padding:13px 14px;
  border:1px solid rgba(113,139,164,.18);
  border-radius:14px;
  background:rgba(113,139,164,.07);
  color:#b9c1c9;
  font-size:.76rem;
}

.sst-footer{
  margin-top:28px;
  padding-top:15px;
  border-top:1px solid var(--sst-line);
  color:#696660;
  text-align:center;
  font-size:.65rem;
}

@media(min-width:700px){
  .sst-shell{padding:25px 22px 70px}
  .sst-hero{padding:32px}
  .sst-grid{grid-template-columns:repeat(2,minmax(0,1fr))}
}

@media(min-width:1000px){
  .sst-grid{grid-template-columns:repeat(3,minmax(0,1fr))}
}

@media(max-width:430px){
  .sst-hero{padding:19px}
  .sst-hero h1{font-size:2.2rem}
}
"""

JS = r"""
document.addEventListener("DOMContentLoaded", () => {
  const tabs = [...document.querySelectorAll(".sst-tab")];
  const panels = [...document.querySelectorAll(".sst-panel")];

  function activateTab(id, updateHash = true) {
    tabs.forEach(tab => {
      tab.classList.toggle("active", tab.dataset.tab === id);
    });

    panels.forEach(panel => {
      panel.classList.toggle("active", panel.id === "tab-" + id);
    });

    if (updateHash) {
      history.replaceState(null, "", "#" + id);
    }
  }

  tabs.forEach(tab => {
    tab.addEventListener("click", () => activateTab(tab.dataset.tab));
  });

  const initial = location.hash.replace("#", "");
  if (initial && tabs.some(tab => tab.dataset.tab === initial)) {
    activateTab(initial, false);
  }

  document.querySelectorAll(".sst-reveal").forEach(button => {
    button.addEventListener("click", () => {
      const question = button.closest(".sst-question");
      question.classList.toggle("revealed");
      button.textContent =
        question.classList.contains("revealed")
          ? "Hide answer"
          : "Show answer";
    });
  });

  document.querySelectorAll("[data-mini-test]").forEach(test => {
    const questions = [...test.querySelectorAll(".sst-question")];
    const submit = test.querySelector(".sst-submit");
    const score = test.querySelector(".sst-score");

    submit?.addEventListener("click", () => {
      let correct = 0;

      questions.forEach(q => {
        const selected = q.querySelector("input:checked");
        if (selected && selected.dataset.correct === "true") {
          correct++;
        }
        q.classList.add("revealed");
      });

      score.style.display = "block";
      score.textContent =
        `Score: ${correct}/${questions.length} · ` +
        (correct === questions.length
          ? "Excellent."
          : "Review the highlighted concepts and try again.");
    });
  });
});
"""


HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="CBSE Class 10 Economics Chapter 1 Development — concepts, practice, NCERT questions, mini test and revision.">
<meta name="theme-color" content="#0d0e10">
<title>Development | Class 10 Economics | SJMaths</title>
<link rel="stylesheet" href="../../assets/css/sst.css">
</head>

<body>
<main class="sst-shell">

<header class="sst-hero">
  <div class="sst-breadcrumb">
    <span>SJMaths</span><b>›</b>
    <span>Class 10</span><b>›</b>
    <span>Social Science</span><b>›</b>
    <span>Economics</span><b>›</b>
    <span>Chapter 1</span>
  </div>

  <div class="sst-kicker">Economics · Chapter 01</div>

  <h1>Development</h1>
  <p class="sst-subtitle">Understanding Economic Development</p>

  <div class="sst-meta">
    <div><strong>6</strong><span>Learning tabs</span></div>
    <div><strong>NCERT</strong><span>Based</span></div>
    <div><strong>CBSE</strong><span>Class 10</span></div>
  </div>
</header>

<nav class="sst-tabs" aria-label="Chapter sections">
  <button class="sst-tab active" data-tab="learn">Learn</button>
  <button class="sst-tab" data-tab="concepts">Concepts</button>
  <button class="sst-tab" data-tab="practice">Practice</button>
  <button class="sst-tab" data-tab="ncert">NCERT Qs</button>
  <button class="sst-tab" data-tab="test">Mini Test</button>
  <button class="sst-tab" data-tab="revision">Revision</button>
</nav>


<!-- =========================================================
     TAB 1 — LEARN
========================================================= -->
<section class="sst-panel active" id="tab-learn">
  <div class="sst-section-head">
    <div>
      <h2>Learn the chapter</h2>
      <p>Short concept blocks instead of long paragraphs.</p>
    </div>
  </div>

  <div class="sst-grid">

    <article class="sst-card">
      <span class="sst-label">01 · Core idea</span>
      <h3>What is development?</h3>
      <p>Development is about improving people's lives and achieving desired goals. Different people can have different ideas about progress.</p>
    </article>

    <article class="sst-card">
      <span class="sst-label">02 · Goals</span>
      <h3>Different people, different goals</h3>
      <ul>
        <li>More income and regular work</li>
        <li>Security and freedom</li>
        <li>Equal treatment and respect</li>
        <li>Better education and health</li>
      </ul>
    </article>

    <article class="sst-card">
      <span class="sst-label">03 · Conflict</span>
      <h3>Goals may conflict</h3>
      <p>What is development for one person or group may not be development for another. It can even be destructive for others.</p>
    </article>

    <article class="sst-card">
      <span class="sst-label">04 · National</span>
      <h3>National development</h3>
      <p>National development requires thinking about whose goals matter, how benefits are distributed and whether development is fair.</p>
    </article>

    <article class="sst-card">
      <span class="sst-label">05 · Comparison</span>
      <h3>Comparing countries or states</h3>
      <p>Income is commonly used for comparison, but income alone does not capture health, education, equality or quality of life.</p>
    </article>

    <article class="sst-card">
      <span class="sst-label">06 · Sustainability</span>
      <h3>Development for the future</h3>
      <p>Development should not destroy the resources and environmental conditions needed by future generations.</p>
    </article>

  </div>
</section>


<!-- =========================================================
     TAB 2 — CONCEPTS
========================================================= -->
<section class="sst-panel" id="tab-concepts">
  <div class="sst-section-head">
    <div>
      <h2>Core concepts</h2>
      <p>Definitions, indicators and relationships.</p>
    </div>
  </div>

  <div class="sst-grid">

    <article class="sst-card">
      <span class="sst-label">Developmental goals</span>
      <h3>Income is not the only goal</h3>
      <p>People also value security, equal treatment, freedom, respect, education and health.</p>
    </article>

    <article class="sst-card">
      <span class="sst-label">Per capita income</span>
      <h3>Average income</h3>
      <div class="sst-formula">Per Capita Income = Total Income ÷ Total Population</div>
      <p>It is also called average income.</p>
    </article>

    <article class="sst-card">
      <span class="sst-label">Limitation</span>
      <h3>Average can hide inequality</h3>
      <p>Two countries may have the same average income while having very different distributions of income.</p>
    </article>

    <article class="sst-card">
      <span class="sst-label">Human development</span>
      <h3>Beyond income</h3>
      <ul>
        <li>Health</li>
        <li>Education</li>
        <li>Income</li>
        <li>Well-being of people</li>
      </ul>
    </article>

    <article class="sst-card">
      <span class="sst-label">Key indicators</span>
      <h3>Important terms</h3>
      <ul>
        <li>Infant Mortality Rate</li>
        <li>Literacy Rate</li>
        <li>Net Attendance Ratio</li>
        <li>Life Expectancy</li>
        <li>Human Development Index</li>
      </ul>
    </article>

    <article class="sst-card">
      <span class="sst-label">Sustainability</span>
      <h3>Resources and future generations</h3>
      <p>Renewable resources can also be overused. Non-renewable resources have a limited stock and eventually get exhausted.</p>
    </article>

  </div>

  <div class="sst-section-head" style="margin-top:24px">
    <div>
      <h2>State comparison</h2>
      <p>Selected NCERT data used to show why income alone is insufficient.</p>
    </div>
  </div>

  <div class="sst-compare">
    <table>
      <thead>
        <tr>
          <th>State</th>
          <th>Per Capita Income (Rs)</th>
          <th>Literacy %</th>
          <th>IMR</th>
          <th>Attendance Ratio</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>Haryana</td><td>3,25,759</td><td>82</td><td>28</td><td>73</td></tr>
        <tr><td>Kerala</td><td>2,81,001</td><td>94</td><td>6</td><td>94</td></tr>
        <tr><td>Bihar</td><td>60,337</td><td>62</td><td>27</td><td>69</td></tr>
      </tbody>
    </table>
  </div>
</section>


<!-- =========================================================
     TAB 3 — PRACTICE
========================================================= -->
<section class="sst-panel" id="tab-practice">
  <div class="sst-section-head">
    <div>
      <h2>Practice</h2>
      <p>Short-answer and application-based questions.</p>
    </div>
  </div>

  <div class="sst-grid">

    <article class="sst-card">
      <span class="sst-label">Q01 · Concept</span>
      <h3>Why can two people have different developmental goals?</h3>
      <p>Write two reasons and give one example.</p>
    </article>

    <article class="sst-card">
      <span class="sst-label">Q02 · Concept</span>
      <h3>Why is income not enough to judge development?</h3>
      <p>Use health and education as examples.</p>
    </article>

    <article class="sst-card">
      <span class="sst-label">Q03 · Numerical</span>
      <h3>A country has total income of ₹8,00,000 and population 200.</h3>
      <p>Calculate its per capita income.</p>
    </article>

    <article class="sst-card">
      <span class="sst-label">Q04 · Analysis</span>
      <h3>Can a country with higher average income be worse off in some aspects?</h3>
      <p>Explain using the idea of average and distribution.</p>
    </article>

    <article class="sst-card">
      <span class="sst-label">Q05 · Application</span>
      <h3>Why are some public facilities better provided collectively?</h3>
      <p>Give two examples from health, education or security.</p>
    </article>

    <article class="sst-card">
      <span class="sst-label">Q06 · Sustainability</span>
      <h3>Why can renewable resources still be overused?</h3>
      <p>Use groundwater as your example.</p>
    </article>

  </div>
</section>


<!-- =========================================================
     TAB 4 — NCERT QUESTIONS
========================================================= -->
<section class="sst-panel" id="tab-ncert">
  <div class="sst-section-head">
    <div>
      <h2>NCERT questions</h2>
      <p>Chapter-end questions for focused preparation.</p>
    </div>
  </div>

  <div class="sst-grid">

    <article class="sst-card">
      <span class="sst-label">MCQ</span>
      <h3>Development of a country can generally be determined by</h3>
      <ul>
        <li>Per capita income</li>
        <li>Average literacy level</li>
        <li>Health status</li>
        <li>All of the above</li>
      </ul>
    </article>

    <article class="sst-card">
      <span class="sst-label">MCQ</span>
      <h3>Which neighbouring country has better human development performance than India?</h3>
      <ul>
        <li>Bangladesh</li>
        <li>Sri Lanka</li>
        <li>Nepal</li>
        <li>Pakistan</li>
      </ul>
    </article>

    <article class="sst-card">
      <span class="sst-label">Short answer</span>
      <h3>What is the main criterion used by the World Bank in classifying countries?</h3>
      <p>Explain the limitations of this criterion.</p>
    </article>

    <article class="sst-card">
      <span class="sst-label">Short answer</span>
      <h3>Why do we use averages?</h3>
      <p>Explain their limitations with an example related to development.</p>
    </article>

    <article class="sst-card">
      <span class="sst-label">Discuss</span>
      <h3>Why is per capita income useful but not sufficient?</h3>
      <p>Use the comparison of states to support your answer.</p>
    </article>

    <article class="sst-card">
      <span class="sst-label">Long answer</span>
      <h3>Why is sustainability important for development?</h3>
      <p>Explain with reference to natural resources and future generations.</p>
    </article>

  </div>
</section>


<!-- =========================================================
     TAB 5 — MINI TEST
========================================================= -->
<section class="sst-panel" id="tab-test">
  <div class="sst-section-head">
    <div>
      <h2>Mini test</h2>
      <p>5 questions · instant score</p>
    </div>
  </div>

  <div data-mini-test>

    <div class="sst-question">
      <p class="sst-q">1. Average income is also known as:</p>
      <div class="sst-options">
        <label class="sst-option"><input type="radio" name="q1" data-correct="true"> Per capita income</label>
        <label class="sst-option"><input type="radio" name="q1"> Total income</label>
        <label class="sst-option"><input type="radio" name="q1"> National income only</label>
      </div>
      <div class="sst-answer">Correct: Per capita income.</div>
    </div>

    <div class="sst-question">
      <p class="sst-q">2. Which is a limitation of average income?</p>
      <div class="sst-options">
        <label class="sst-option"><input type="radio" name="q2"> It cannot be calculated</label>
        <label class="sst-option"><input type="radio" name="q2" data-correct="true"> It can hide income inequality</label>
        <label class="sst-option"><input type="radio" name="q2"> It measures only population</label>
      </div>
      <div class="sst-answer">Correct: It can hide income inequality.</div>
    </div>

    <div class="sst-question">
      <p class="sst-q">3. Which is a human-development indicator?</p>
      <div class="sst-options">
        <label class="sst-option"><input type="radio" name="q3"> Road length only</label>
        <label class="sst-option"><input type="radio" name="q3"> Number of shops</label>
        <label class="sst-option"><input type="radio" name="q3" data-correct="true"> Life expectancy</label>
      </div>
      <div class="sst-answer">Correct: Life expectancy.</div>
    </div>

    <div class="sst-question">
      <p class="sst-q">4. Groundwater is an example of:</p>
      <div class="sst-options">
        <label class="sst-option"><input type="radio" name="q4" data-correct="true"> A renewable resource that can be overused</label>
        <label class="sst-option"><input type="radio" name="q4"> A resource that never changes</label>
        <label class="sst-option"><input type="radio" name="q4"> A non-renewable mineral</label>
      </div>
      <div class="sst-answer">Correct: A renewable resource that can be overused.</div>
    </div>

    <div class="sst-question">
      <p class="sst-q">5. Sustainable development considers:</p>
      <div class="sst-options">
        <label class="sst-option"><input type="radio" name="q5"> Only present income</label>
        <label class="sst-option"><input type="radio" name="q5" data-correct="true"> Present needs and future generations</label>
        <label class="sst-option"><input type="radio" name="q5"> Only industrial production</label>
      </div>
      <div class="sst-answer">Correct: Present needs and future generations.</div>
    </div>

    <button class="sst-reveal sst-submit" type="button">Submit test</button>
    <div class="sst-score"></div>

  </div>
</section>


<!-- =========================================================
     TAB 6 — REVISION
========================================================= -->
<section class="sst-panel" id="tab-revision">
  <div class="sst-section-head">
    <div>
      <h2>Quick revision</h2>
      <p>High-yield points to recall before an exam.</p>
    </div>
  </div>

  <div class="sst-revision">

    <div class="sst-revision-item">
      <div class="sst-revision-num">01</div>
      <div>
        <strong>Development</strong>
        <span>Different people can have different and conflicting goals.</span>
      </div>
    </div>

    <div class="sst-revision-item">
      <div class="sst-revision-num">02</div>
      <div>
        <strong>Income</strong>
        <span>More income is important, but it is not the only developmental goal.</span>
      </div>
    </div>

    <div class="sst-revision-item">
      <div class="sst-revision-num">03</div>
      <div>
        <strong>Per capita income</strong>
        <span>Total income divided by total population.</span>
      </div>
    </div>

    <div class="sst-revision-item">
      <div class="sst-revision-num">04</div>
      <div>
        <strong>Average limitation</strong>
        <span>An average can hide unequal distribution of income.</span>
      </div>
    </div>

    <div class="sst-revision-item">
      <div class="sst-revision-num">05</div>
      <div>
        <strong>Other indicators</strong>
        <span>Health, education and other quality-of-life indicators matter.</span>
      </div>
    </div>

    <div class="sst-revision-item">
      <div class="sst-revision-num">06</div>
      <div>
        <strong>Public facilities</strong>
        <span>Some goods and services are more effectively provided collectively.</span>
      </div>
    </div>

    <div class="sst-revision-item">
      <div class="sst-revision-num">07</div>
      <div>
        <strong>HDI</strong>
        <span>The chapter uses health, education and income as major dimensions of human development.</span>
      </div>
    </div>

    <div class="sst-revision-item">
      <div class="sst-revision-num">08</div>
      <div>
        <strong>Sustainability</strong>
        <span>Development should not compromise resources and environmental conditions for the future.</span>
      </div>
    </div>

  </div>

  <div class="sst-note" style="margin-top:14px">
    Exam tip: learn the relationship between <b>income → averages → human development → sustainability</b>.
    Do not memorise indicators without understanding what each tells us.
  </div>
</section>


<footer class="sst-footer">
  SJMaths · CBSE Class 10 Social Science · Economics · Chapter 1
</footer>

</main>

<script src="../../assets/js/sst.js"></script>
</body>
</html>
"""


def main():
    print("=" * 76)
    print("SJMaths — Class 10 SST")
    print("Economics · Chapter 1 · Development")
    print("=" * 76)
    print()
    print("Creating reusable SST assets...")
    write(SHARED_CSS, CSS)
    write(SHARED_JS, JS)

    print()
    print("Creating Chapter 1...")
    CHAPTER_DIR.mkdir(parents=True, exist_ok=True)
    write(CHAPTER_HTML, HTML)

    print()
    print("DONE")
    print("-" * 76)
    print("Shared CSS :", SHARED_CSS)
    print("Shared JS  :", SHARED_JS)
    print("Chapter    :", CHAPTER_HTML)
    print()
    print("Tabs created:")
    print("  1. Learn")
    print("  2. Concepts")
    print("  3. Practice")
    print("  4. NCERT Qs")
    print("  5. Mini Test")
    print("  6. Revision")
    print()
    print("The same sst.css and sst.js can be reused by every")
    print("History, Geography, Political Science and Economics chapter.")
    print()
    print("IMPORTANT:")
    print("This generator does not create separate CSS/JS files per chapter.")


if __name__ == "__main__":
    main()