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
    if (window.MathJax && window.MathJax.typesetPromise) {
        window.MathJax.typesetPromise();
    }
}

function formatContent(text) {
    if (!text) return "";
    
    let content = text;

    // 1. Markdown Tables Parser
    if (content.includes('|')) {
        const lines = content.split('\n');
        let tableHtml = '';
        let inTable = false;
        let tableRows = [];

        for (let i = 0; i < lines.length; i++) {
            const line = lines[i].trim();
            if (line.startsWith('|') && line.endsWith('|')) {
                if (!inTable) {
                    inTable = true;
                    tableRows = [];
                }
                tableRows.push(line);
            } else {
                if (inTable) {
                    tableHtml = parseMarkdownTable(tableRows);
                    content = content.replace(tableRows.join('\n'), tableHtml);
                    inTable = false;
                }
            }
        }
        // Handle table at the very end
        if (inTable) {
            tableHtml = parseMarkdownTable(tableRows);
            content = content.replace(tableRows.join('\n'), tableHtml);
        }
    }

    // 2. Other Formatting
    return content
        .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
        .replace(/\[(\d+)\s*marks?\]/gi, (match, n) => {
            return `<span class="q-marks">${n} Mark${n > 1 ? 's' : ''}</span>`;
        })
        .replace(/\*\*OR\*\*/g, '<span class="q-or">OR</span>');
}

function parseMarkdownTable(rows) {
    if (rows.length < 2) return rows.join('\n');

    // Split by | and filter out empty first/last elements
    const cleanRows = rows.map(r => {
        const parts = r.split('|').map(c => c.trim());
        if (parts[0] === '') parts.shift();
        if (parts[parts.length - 1] === '') parts.pop();
        return parts;
    });
    
    // Remove the separator row (e.g., |---|---|)
    const headerRow = cleanRows[0];
    const dataRows = cleanRows.slice(1).filter(r => !r.every(c => c.match(/^[:\s-]*$/)));

    let html = '<div class="table-wrapper"><table class="data-table"><thead><tr>';
    headerRow.forEach(h => {
        html += `<th>${h}</th>`;
    });
    html += '</tr></thead><tbody>';

    dataRows.forEach(row => {
        html += '<tr>';
        row.forEach(c => {
            html += `<td>${c}</td>`;
        });
        html += '</tr>';
    });

    html += '</tbody></table></div>';
    return html;
}

/* ---------- LOAD QUESTIONS ---------- */
const container = document.getElementById("questionContainer");
if (container && container.children.length > 0) {
    // Some generated PYQ pages contain a repeated static question block.
    // Keep the first card for each ID so the sequence never restarts.
    const seenQuestionIds = new Set();
    Array.from(container.querySelectorAll(".question-card")).forEach(card => {
        if (seenQuestionIds.has(card.id)) {
            card.remove();
        } else {
            seenQuestionIds.add(card.id);
        }
    });
    renderMath();
    detectActiveQuestion();
} else if (window.QUESTIONS_JSON) {
fetch(window.QUESTIONS_JSON)
    .then(res => res.json())
    .then(data => {
        const container = document.getElementById("questionContainer");
        if (container.children.length > 0) {
            renderMath();
            detectActiveQuestion();
            return;
        }

        // Handle both array format and sections format
        const questions = Array.isArray(data) ? data : (data.sections ? data.sections.flatMap(s => s.questions) : []);

        questions.forEach(q => {
                const card = document.createElement("div");
                card.className = "question-card";
                card.id = q.id;

                let questionHTML = formatContent(q.question || q.case_study || "");
                if (q.parts) {
                    Object.entries(q.parts).forEach(([k, v]) => {
                        questionHTML += `<br><strong>(${k})</strong> ${formatContent(v)}`;
                    });
                }
                
                let optionsHTML = "";
                if (q.options) {
                    if (Array.isArray(q.options)) {
                        optionsHTML = `<div class="q-options-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 12px; margin-top: 16px;">` + 
                            q.options.map((o,i)=>`<div class="q-option-item" style="display: flex; align-items: flex-start; gap: 10px; padding: 12px 16px; background: rgba(0,0,0,0.02); border: 1px solid rgba(0,0,0,0.08); border-radius: 8px;"><span style="font-weight: 600; color: var(--primary, #2c3e50);">(${String.fromCharCode(97+i)})</span><span style="flex: 1;">${formatContent(o)}</span></div>`).join("") + 
                            `</div>`;
                    } else {
                        optionsHTML = `<div class="q-options-text" style="margin-top: 16px; padding: 12px 16px; background: rgba(0,0,0,0.02); border: 1px solid rgba(0,0,0,0.08); border-radius: 8px;">${formatContent(q.options)}</div>`;
                    }
                }

                card.innerHTML = `
                    <div class="q-header">
                        <div style="display:flex; align-items:center; gap:8px;">
                            <span class="q-badge">Q${q.id}</span>
                            ${q.year ? `<span class="q-year" style="font-size:0.8rem; font-weight:600; color:#666; background:#f3f4f6; padding:2px 8px; border-radius:12px;">${q.year}</span>` : ""}
                        </div>
                        <span class="q-timer">00:00</span>
                    </div>

                    <div class="question-text">
                        ${questionHTML}
                        ${optionsHTML}
                    </div>

                    ${q.diagram ? `<div class="question-diagram">${q.diagram}</div>` : ""}
                    ${q.graphRef ? `<div class="graph-container" data-ref="${q.graphRef}"></div>` : ""}

                    ${q.solutionSteps ? `
                        <button class="solution-btn" onclick="toggleSol('sol_${q.id}', this)">Show Solution ▼</button>
                        <div id="sol_${q.id}" class="solution-content">
                            ${q.solutionSteps.map(s=>`<div class="step">${formatContent(s)}</div>`).join("")}
                            <div class="final-ans"><strong>${formatContent(q.finalAnswer)}</strong></div>
                        </div>` : ""}
                `;

                container.appendChild(card);
        });

        renderMath();
        detectActiveQuestion();
    });
}
