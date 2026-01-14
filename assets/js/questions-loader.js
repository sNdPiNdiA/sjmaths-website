fetch("questions.json")
    .then(res => {
        if (!res.ok) throw new Error("JSON not found");
        return res.json();
    })
    .then(data => {
        const container = document.getElementById("question-container");
        container.innerHTML = "";

        data.sections.forEach(section => {

            // SAFE SECTION LETTER
            const sectionLetter = section.section.toUpperCase().split("SECTION ")[1][0];

            const sectionDiv = document.createElement("div");
            sectionDiv.id = sectionLetter;

            sectionDiv.innerHTML = `
                <h2 style="margin:1.2rem 0;color:#7b1fa2;">
                    ${section.section}
                </h2>
            `;

            section.questions.forEach(q => {
                const qDiv = document.createElement("div");
                qDiv.className = "question";
                qDiv.dataset.qid = q.id;

                let html = `
                    <div class="q-no">${q.number}</div>
                    <div class="q-text">${q.question || q.case_study || ""}</div>
                    <div class="write-note">
                        Write the answer as you would in the actual examination on a white paper for evaluation.
                    </div>
                `;

                if (q.options) {
                    html += "<ol class='mcq-options' type='a'>";
                    q.options.forEach((opt, i) => {
                        const val = String.fromCharCode(97 + i); // a, b, c, d
                        html += `<li style="margin-bottom:0.5rem;">
                            <label style="cursor:pointer; display:flex; align-items:flex-start; gap:8px;">
                                <input type="radio" name="${q.id}" value="${val}" style="margin-top:5px;">
                                <span>${opt}</span>
                            </label>
                        </li>`;
                    });
                    html += "</ol>";
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

                qDiv.innerHTML = html;
                sectionDiv.appendChild(qDiv);
            });

            container.appendChild(sectionDiv);
        });

        // 🔥 Render LaTeX AFTER everything is in DOM
        if (window.MathJax) {
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
            "<p style='color:red'>Failed to load questions.</p>";
    });
