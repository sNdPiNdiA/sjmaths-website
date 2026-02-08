// Inject Styles for Questions Module
const style = document.createElement('style');
style.innerHTML = `
    .question-card {
        background: var(--card-bg, #fff);
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        border: 1px solid var(--border-color, #eee);
        transition: transform 0.2s;
    }
    .question-card:hover { transform: translateY(-2px); box-shadow: 0 8px 25px rgba(0,0,0,0.08); }
    .q-header { display: flex; justify-content: space-between; margin-bottom: 1rem; align-items: center; }
    .q-badge { background: var(--primary, #8e44ad); color: white; padding: 4px 12px; border-radius: 20px; font-weight: 700; font-size: 0.9rem; }
    .q-text { font-size: 1.05rem; color: var(--text-dark, #2c3e50); margin-bottom: 1rem; line-height: 1.6; }
    .mcq-options { list-style: none; padding: 0; display: grid; gap: 10px; }
    .mcq-options li { background: var(--bg-body, #f8f9fa); padding: 10px 15px; border-radius: 8px; border: 1px solid transparent; transition: all 0.2s; }
    .mcq-options li:hover { border-color: var(--primary, #8e44ad); background: rgba(142, 68, 173, 0.05); }
    .mcq-label { cursor: pointer; display: flex; align-items: center; gap: 10px; width: 100%; }
    .solution-container { margin-top: 1.5rem; border-top: 1px dashed #ddd; padding-top: 1rem; }
    .solution-toggle-btn {
        background: transparent; border: 1px solid var(--primary, #8e44ad); color: var(--primary, #8e44ad);
        padding: 8px 16px; border-radius: 50px; cursor: pointer; font-weight: 600; font-size: 0.9rem;
        display: flex; align-items: center; gap: 8px; transition: all 0.2s;
    }
    .solution-toggle-btn:hover { background: var(--primary, #8e44ad); color: white; }
    .solution-content { margin-top: 1rem; background: var(--solution-bg, #f8f5ff); padding: 1.2rem; border-radius: 12px; border-left: 4px solid var(--primary, #8e44ad); animation: slideDown 0.3s ease; }
    .step-item { display: flex; gap: 10px; margin-bottom: 8px; font-size: 0.95rem; color: var(--text-body, #555); }
    .step-item i { color: var(--primary, #8e44ad); margin-top: 4px; }
    .final-answer { margin-top: 12px; font-weight: 600; color: var(--secondary, #27ae60); background: rgba(39, 174, 96, 0.1); padding: 8px 12px; border-radius: 8px; display: inline-block; }
    @keyframes slideDown { from { opacity: 0; transform: translateY(-10px); } to { opacity: 1; transform: translateY(0); } }
`;
document.head.appendChild(style);

// Global Toggle Function
window.toggleSolution = function(id) {
    const content = document.getElementById(`sol-${id}`);
    const btn = document.querySelector(`button[onclick="toggleSolution('${id}')"]`);
    if (content.style.display === 'none') {
        content.style.display = 'block';
        btn.innerHTML = '<i class="fas fa-eye-slash"></i> Hide Solution';
        if (window.MathJax) MathJax.typesetPromise([content]);
    } else {
        content.style.display = 'none';
        btn.innerHTML = '<i class="fas fa-eye"></i> Show Solution';
    }
};

const jsonPath = window.QUESTIONS_JSON || "questions.json";

fetch(jsonPath)
    .then(res => {
        if (!res.ok) throw new Error("JSON not found");
        return res.json();
    })
    .then(data => {
        const container = document.getElementById("question-container");
        container.innerHTML = "";

        // Handle both structured (sections) and flat (array) JSON formats
        const sections = Array.isArray(data) 
            ? [{ section: "Questions", questions: data }] 
            : (data.sections || []);

        sections.forEach(section => {

            // SAFE SECTION LETTER
            const sectionName = section.section || "Questions";
            const sectionParts = sectionName.toUpperCase().split("SECTION ");
            const sectionLetter = sectionParts.length > 1 ? sectionParts[1][0] : sectionName.charAt(0);

            const sectionDiv = document.createElement("div");
            sectionDiv.id = sectionLetter;

            sectionDiv.innerHTML = `
                <h2 style="margin:1.2rem 0;color:#7b1fa2;text-align:center;">
                    ${sectionName}
                </h2>
            `;

            section.questions.forEach(q => {
                const qDiv = document.createElement("div");
                qDiv.className = "question-card";
                qDiv.dataset.qid = q.id;

                let html = `
                    <div class="q-header">
                        <span class="q-badge">Q${q.number || q.id}</span>
                    </div>
                    <div class="q-text">${q.question || q.case_study || ""}</div>
                `;

                if (q.options) {
                    html += "<ul class='mcq-options'>";
                    q.options.forEach((opt, i) => {
                        const val = String.fromCharCode(97 + i); // a, b, c, d
                        html += `<li>
                            <label class="mcq-label">
                                <input type="radio" name="${q.id}" value="${val}">
                                <span class="opt-text">(${val}) ${opt}</span>
                            </label>
                        </li>`;
                    });
                    html += "</ul>";
                }

                if (q.parts) {
                    Object.entries(q.parts).forEach(([k, v]) => {
                        html += `<div><strong>${k}.</strong> ${v}</div>`;
                    });
                }

                if (q.visually_impaired) {
                    html += `
                        <div style="margin-top:6px;font-style:italic;color:#6b7280;">
                            For Visually Impaired: ${q.visually_impaired}
                        </div>
                    `;
                }

                if (q.hint) {
                    html += `
                        <div class="hint-container" style="margin-top: 10px;">
                            <button class="btn-hint" onclick="this.nextElementSibling.style.display = this.nextElementSibling.style.display === 'none' ? 'block' : 'none'; this.textContent = this.textContent === 'Show Hint' ? 'Hide Hint' : 'Show Hint';" style="background:none; border:none; color:#666; cursor:pointer; text-decoration:underline; font-size:0.9rem;">Show Hint</button>
                            <div class="hint-text" style="display:none; margin-top:5px; color:#555; font-style:italic; background:#f9f9f9; padding:8px; border-radius:4px; border-left:3px solid #ccc;">${q.hint}</div>
                        </div>
                    `;
                }

                // Solution Section
                if (q.solutionSteps || q.solution) {
                    html += `
                        <div class="solution-container">
                            <button class="solution-toggle-btn" onclick="toggleSolution('${q.id}')">
                                <i class="fas fa-eye"></i> Show Solution
                            </button>
                            <div id="sol-${q.id}" class="solution-content" style="display: none;">
                    `;
                    if (q.solutionSteps) {
                        html += `<div class="solution-steps">${q.solutionSteps.map(step => `<div class="step-item"><i class="fas fa-angle-right"></i> <span>${step}</span></div>`).join('')}</div>`;
                    } else {
                        html += `<div class="solution-text" style="color:var(--text-body); line-height:1.6; margin-bottom:10px;">${q.solution}</div>`;
                    }
                    const finalAns = q.finalAnswer || q.answer;
                    if (finalAns) html += `<div class="final-answer">${finalAns}</div>`;
                    html += `
                            </div>
                        </div>
                    `;
                }

                qDiv.innerHTML = html;
                sectionDiv.appendChild(qDiv);
            });

            container.appendChild(sectionDiv);
        });

        // 🔥 Render LaTeX AFTER everything is in DOM
        if (window.MathJax && window.MathJax.typesetPromise) {
            MathJax.typesetPromise();
        }

        // 🔥 OBSERVER AFTER QUESTIONS EXIST
        if (typeof qObserver !== 'undefined') {
            document.querySelectorAll(".question").forEach(q => {
                qObserver.observe(q);
            });
        }
    })
    .catch(err => {
        console.error("❌ Question loading failed:", err);
        document.getElementById("question-container").innerHTML =
            `<div style="text-align:center; padding:2rem; color:var(--secondary);">
                <i class="fas fa-exclamation-circle fa-2x"></i><br><br>
                <strong>Failed to load questions</strong><br>
                <small>${err.message}</small>
            </div>`;
    });
