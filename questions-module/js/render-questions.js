/* =========================================================
   SJMaths – Section-wise Question Renderer (FINAL)
   ✔ Timer
   ✔ MathJax
   ✔ SVG / Ray Diagrams
   ✔ Solution Toggle
========================================================= */

let activeCard = null;
let timerInterval = null;
const timerSeconds = {};
let solutionOpen = false;

function formatTime(sec) {
    const m = String(Math.floor(sec / 60)).padStart(2, "0");
    const s = String(sec % 60).padStart(2, "0");
    return `${m}:${s}`;
}

function stopTimer() {
    if (timerInterval) clearInterval(timerInterval);
    timerInterval = null;
    activeCard = null;
}

function startTimer(card) {
    if (!card || solutionOpen || activeCard === card) return;

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

window.addEventListener("scroll", () => {
    if (!solutionOpen) requestAnimationFrame(detectActiveQuestion);
});

window.toggleSol = function (solId, btn) {
    const sol = document.getElementById(solId);
    const card = btn.closest(".question-card");
    const isOpen = sol.classList.contains("open");

    document.querySelectorAll(".solution-content.open").forEach(s => {
        s.classList.remove("open");
        s.closest(".question-card").classList.remove("solution-open");
        s.closest(".question-card").querySelector(".solution-btn").textContent = "Show Solution ▼";
    });

    stopTimer();

    if (!isOpen) {
        sol.classList.add("open");
        card.classList.add("solution-open");
        btn.textContent = "Hide Solution ▲";
        solutionOpen = true;
    } else {
        solutionOpen = false;
        detectActiveQuestion();
    }
};

function renderMath() {
    if (!window.MathJax) return;
    if (MathJax.typesetPromise) MathJax.typesetPromise();
}

/* ---------- LOAD QUESTIONS ---------- */
fetch(window.QUESTIONS_JSON)
    .then(res => res.json())
    .then(data => {
        const container = document.getElementById("question-container");

        data.sections.forEach(section => {

            const secTitle = document.createElement("h2");
            secTitle.className = "section-title";
            secTitle.textContent = section.section;
            container.appendChild(secTitle);

            section.questions.forEach(q => {
                const card = document.createElement("div");
                card.className = "question-card";
                card.id = q.id;

                let questionHTML = q.question || q.case_study || "";
                if (q.parts) {
                    Object.entries(q.parts).forEach(([k, v]) => {
                        questionHTML += `<br><strong>(${k})</strong> ${v}`;
                    });
                }

                card.innerHTML = `
                    <div class="q-header">
                        <span class="q-badge">${q.number}</span>
                        <span class="q-timer">00:00</span>
                    </div>

                    <div class="question-text">
                        ${questionHTML}
                        ${q.options ? "<br><br>" + q.options.map((o,i)=>`(${String.fromCharCode(97+i)}) ${o}`).join(" &nbsp; ") : ""}
                    </div>

                    ${q.diagram ? `<div class="question-diagram">${q.diagram}</div>` : ""}

                    ${q.solutionSteps ? `
                        <button class="solution-btn" onclick="toggleSol('sol_${q.id}', this)">Show Solution ▼</button>
                        <div id="sol_${q.id}" class="solution-content">
                            ${q.solutionSteps.map(s=>`<div class="step">${s}</div>`).join("")}
                            <div class="final-ans"><strong>${q.finalAnswer}</strong></div>
                        </div>` : ""}
                `;

                container.appendChild(card);
            });
        });

        renderMath();
        detectActiveQuestion();
    });
