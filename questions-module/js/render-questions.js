/* =========================================================
   SJMaths – Question Renderer (FINAL STABLE FIX)
   ✔ One solution open at a time
   ✔ Timer stops immediately on solution open
   ✔ Timer resumes only when solution closes
   ✔ Scroll-safe
   ✔ MathJax v2 + v3 compatible
========================================================= */

/* ---------- TIMER STATE ---------- */
let activeCard = null;
let timerInterval = null;
const timerSeconds = {};
let solutionOpen = false;

/* ---------- FORMAT TIME ---------- */
function formatTime(sec) {
    const m = String(Math.floor(sec / 60)).padStart(2, "0");
    const s = String(sec % 60).padStart(2, "0");
    return `${m}:${s}`;
}

/* ---------- STOP TIMER ---------- */
function stopTimer() {
    if (timerInterval) {
        clearInterval(timerInterval);
        timerInterval = null;
    }
    activeCard = null;
}

/* ---------- START TIMER ---------- */
function startTimer(card) {
    if (!card || solutionOpen) return;
    if (activeCard === card) return;

    stopTimer();
    activeCard = card;

    const id = card.id;
    const timerEl = card.querySelector(".q-timer");
    timerSeconds[id] = timerSeconds[id] || 0;

    timerInterval = setInterval(() => {
        timerSeconds[id]++;
        timerEl.textContent = formatTime(timerSeconds[id]);
    }, 1000);
}

/* ---------- FIND ACTIVE QUESTION ---------- */
function detectActiveQuestion() {
    if (solutionOpen) return;

    const cards = document.querySelectorAll(".question-card");
    let candidate = null;
    let bestScore = Infinity;

    cards.forEach(card => {
        const r = card.getBoundingClientRect();
        if (r.bottom < 0 || r.top > window.innerHeight) return;

        const score = Math.abs(r.top - window.innerHeight * 0.35);
        if (score < bestScore) {
            bestScore = score;
            candidate = card;
        }
    });

    if (candidate) startTimer(candidate);
}

/* ---------- SCROLL HANDLER ---------- */
let scrollTick = false;
window.addEventListener("scroll", () => {
    if (scrollTick || solutionOpen) return;
    scrollTick = true;

    requestAnimationFrame(() => {
        detectActiveQuestion();
        scrollTick = false;
    });
});

/* ---------- SOLUTION TOGGLE (ACCORDION) ---------- */
window.toggleSol = function (solId, btn) {
    const sol = document.getElementById(solId);
    const card = btn.closest(".question-card");
    const isOpen = sol.classList.contains("open");

    // Close ALL solutions
    document.querySelectorAll(".solution-content.open").forEach(s => {
        s.classList.remove("open");
        const c = s.closest(".question-card");
        c.classList.remove("solution-open");
        c.querySelector(".solution-btn").textContent = "Show Solution ▼";
    });

    stopTimer();

    if (!isOpen) {
        // Open selected
        sol.classList.add("open");
        card.classList.add("solution-open");
        btn.textContent = "Hide Solution ▲";
        solutionOpen = true;
    } else {
        // Close selected
        solutionOpen = false;
        detectActiveQuestion();
    }
};

/* ---------- MATHJAX SAFE RENDER ---------- */
function renderMath() {
    if (!window.MathJax) return;

    if (MathJax.typesetPromise) {
        MathJax.typesetPromise();
    } else if (MathJax.Hub && MathJax.Hub.Queue) {
        MathJax.Hub.Queue(["Typeset", MathJax.Hub]);
    }
}

/* ---------- RENDER QUESTIONS ---------- */
fetch(window.QUESTIONS_JSON)
    .then(res => res.json())
    .then(questions => {
        const container = document.getElementById("questionContainer");

        questions.forEach(q => {
            const card = document.createElement("div");
            card.className = "question-card";
            card.id = `q${q.id}`;

            card.innerHTML = `
                <div class="q-header">
    <span class="q-badge">Q${q.id}</span>

    <div class="q-controls">
        <span class="q-timer">00:00</span>

        <button class="toggle-btn imp-btn" onclick="toggleStatus('q${q.id}','important')">
            Important
        </button>

        <button class="toggle-btn mast-btn" onclick="toggleStatus('q${q.id}','mastered')">
            Mastered
        </button>
    </div>
</div>


                <div class="question-text">
                    ${q.question}
                    ${q.options?.length
                    ? `<br><br>${q.options.map((o, i) =>
                        `(${String.fromCharCode(97 + i)}) ${o}`
                    ).join(" &nbsp; ")}`
                    : ""
                }
                    ${q.year ? `<br><em>(${q.year})</em>` : ""}
                </div>

                <button class="solution-btn" onclick="toggleSol('sol${q.id}', this)">
                    Show Solution ▼
                </button>

                <div id="sol${q.id}" class="solution-content">
                    ${q.solutionSteps.map(s => `<div class="step">${s}</div>`).join("")}
                    <div class="final-ans"><strong>${q.finalAnswer}</strong></div>
                </div>
            `;

            container.appendChild(card);
        });

        renderMath();
        detectActiveQuestion(); // start first timer
    });
