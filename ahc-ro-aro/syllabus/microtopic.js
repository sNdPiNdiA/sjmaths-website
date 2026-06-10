document.addEventListener("DOMContentLoaded", () => {
    const dataUrl = "data.json"; // Dynamically loads from the same directory

    // Tab Switching Logic
    const tabs = document.querySelectorAll('.mt-tab-btn');
    const contents = document.querySelectorAll('.mt-tab-content');

    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            tabs.forEach(t => t.classList.remove('active'));
            contents.forEach(c => c.classList.remove('active'));
            
            tab.classList.add('active');
            document.getElementById(tab.dataset.tab).classList.add('active');
        });
    });

    // Load JSON Data
    fetch(dataUrl)
        .then(res => {
            if (!res.ok) return null;
            const contentType = res.headers.get("content-type");
            if (contentType && !contentType.includes("application/json")) return null;
            return res.json();
        })
        .then(data => {
            if (!data) return;
            if (data.pedagogy) renderNotes(data.pedagogy);
            if (data.practice) renderPractice(data.practice);
            if (data.mock) renderMock(data.mock);
        })
        .catch(err => console.error("Error loading microtopic data:", err));
});

function renderNotes(pedagogy) {
    const container = document.getElementById("notes-container");
    let html = '';

    // 1. Introduction
    if(pedagogy.introduction) {
        html += `
        <div class="sci-concept-card" style="animation-delay: 0.1s;">
            <h2><i class="fas fa-book-open"></i> Overview</h2>
            <p>${pedagogy.introduction}</p>
        </div>`;
    }

    // 2. Systems of Units (Graphical)
    if(pedagogy.systems_of_units) {
        html += `<div class="sci-concept-card" style="animation-delay: 0.2s;">
            <h2><i class="fas fa-globe"></i> Systems of Units</h2>
            <div class="sci-grid">`;
        pedagogy.systems_of_units.forEach(sys => {
            html += `<div class="sci-box">
                <i class="fas fa-cubes"></i>
                <div class="sci-box-title">${sys.name}</div>
                <div style="font-size:0.9rem; color:#666;">${sys.desc}</div>
            </div>`;
        });
        html += `</div></div>`;
    }

    // 3. Base SI Units (Dual Coded)
    if(pedagogy.fundamental_units) {
        html += `<div class="sci-concept-card" style="animation-delay: 0.3s;">
            <h2><i class="fas fa-cube"></i> 7 Fundamental SI Units + 2 Supplementary</h2>
            <div class="sci-grid">`;
        pedagogy.fundamental_units.forEach(item => {
            html += `<div class="sci-box">
                <i class="fas ${item.icon}"></i>
                <div class="sci-box-title">${item.name}</div>
                <div class="sci-box-val">${item.unit} (${item.symbol})</div>
                ${item.dimension ? `<div class="sci-badge">Dim: ${item.dimension}</div>` : ''}
            </div>`;
        });
        html += `</div></div>`;
    }

    // 4. Important Derived Units with Dimensions (RO/ARO level)
    if(pedagogy.derived_units) {
        html += `<div class="sci-concept-card" style="animation-delay: 0.4s;">
            <h2><i class="fas fa-rocket"></i> Derived Units & Dimensional Formulas</h2>
            <ul class="instrument-list">`;
        pedagogy.derived_units.forEach(item => {
            html += `<li><strong>${item.name}</strong>: ${item.unit} <br><span class="sci-badge">${item.dimension}</span></li>`;
        });
        html += `</ul></div>`;
    }

    // 5. Special/Astronomical Units
    if(pedagogy.special_units) {
        html += `<div class="sci-concept-card" style="animation-delay: 0.5s;">
            <h2><i class="fas fa-meteor"></i> Special & Astronomical Units</h2>
            <div class="sci-grid">`;
        pedagogy.special_units.forEach(item => {
            html += `<div class="sci-box">
                <div class="sci-box-title">${item.name}</div>
                <div style="font-size:0.9rem; color:#555; margin-bottom:5px;">${item.use}</div>
                <div class="sci-badge">${item.value}</div>
            </div>`;
        });
        html += `</div></div>`;
    }

    // 6. Scientific Instruments
    if(pedagogy.measuring_instruments) {
        html += `<div class="sci-concept-card" style="animation-delay: 0.6s;">
            <h2><i class="fas fa-microscope"></i> Scientific Measuring Instruments</h2>
            <ul class="instrument-list">`;
        pedagogy.measuring_instruments.forEach(item => {
            html += `<li><strong>${item.instrument}</strong>: ${item.usage}</li>`;
        });
        html += `</ul></div>`;
    }

    // 6a. Scalar & Vector Quantities
    if(pedagogy.scalar_vector_quantities) {
        html += `<div class="sci-concept-card" style="animation-delay: 0.65s;">
            <h2><i class="fas fa-arrows-alt"></i> Scalar & Vector Quantities</h2>
            <div class="sci-grid">`;
        pedagogy.scalar_vector_quantities.forEach(item => {
            html += `<div class="sci-box">
                <div class="sci-box-title" style="color: var(--mt-primary);">${item.type}</div>
                <div style="font-size:0.9rem; color:#555; margin-bottom:5px;">${item.definition}</div>
                <div class="sci-badge" style="background:#eef2f3; color:#333; white-space:normal; text-align:left;"><strong>Examples:</strong> ${item.examples}</div>
            </div>`;
        });
        html += `</div></div>`;
    }

    // 6b. Visual Aids (Diagrams & Animations)
    if(pedagogy.visual_aids) {
        html += `<div class="sci-concept-card" style="animation-delay: 0.68s;">
            <h2><i class="fas fa-project-diagram"></i> Interactive Diagrams & Animations</h2>
            <div style="display:flex; flex-direction:column; gap:2rem; margin-top:1rem;">`;
        pedagogy.visual_aids.forEach(item => {
            html += `<div class="visual-aid-box" style="border: 1px solid #eee; border-radius: 10px; overflow:hidden; background:#fff;">
                <div style="padding: 1rem; background: #fafafa; border-bottom: 1px solid #eee;">
                    <h3 style="margin:0; font-size:1.1rem; color:#2c3e50;">${item.title}</h3>
                    <p style="margin:0.5rem 0 0 0; font-size:0.9rem; color:#666;">${item.description}</p>
                </div>
                <div style="padding: 1rem; display:flex; justify-content:center; align-items:center;">
                    <div style="width: 100%; max-width: 600px;">
                        ${item.svg_code}
                    </div>
                </div>
            </div>`;
        });
        html += `</div></div>`;
    }

    // 7. Active Recall Memory Block
    if(pedagogy.active_recall) {
        html += `<div class="sci-concept-card" style="animation-delay: 0.7s; background: linear-gradient(145deg, #f0fdf4, #ffffff); border-left-color: #2ecc71;">
            <h2><i class="fas fa-brain"></i> Active Recall (Testing Effect)</h2>
            <p style="font-size:0.9rem; margin-bottom:1rem;">Tap or hover over the blurred area to reveal the answer. Forcing your brain to guess first guarantees long-term retention!</p>
            <div style="display:flex; flex-direction:column; gap:0.5rem;">`;
        pedagogy.active_recall.forEach(item => {
            html += `<div class="active-recall-item">
                <div style="font-weight:600; width: 60%;">${item.q}</div>
                <div class="blur-reveal" onclick="this.classList.toggle('revealed')">${item.a}</div>
            </div>`;
        });
        html += `</div></div>`;
    }

    // 8. Mnemonics
    if(pedagogy.mnemonics) {
        html += `<div class="sci-concept-card" style="animation-delay: 0.8s;">
            <h2><i class="fas fa-lightbulb"></i> Exam Mnemonics</h2>
            <ul style="list-style:disc; padding-left:1.5rem;">`;
        pedagogy.mnemonics.forEach(mn => { 
            html += `<li style="margin-bottom:1rem;"><strong>${mn.title}</strong>: <span style="color:var(--mt-primary); font-weight:bold;">${mn.trick}</span> <br> <small>${mn.explanation}</small></li>`; 
        });
        html += `</ul></div>`;
    }

    container.innerHTML = html;
}

function renderPractice(questions) {
    const container = document.getElementById("practice-container");
    let html = '';

    questions.forEach((q, index) => {
        html += `
            <div class="question-card" id="prac-q-${index}">
                <div class="q-text">Q${index + 1}. ${q.q}</div>
                <div class="options-list">
                    ${q.options.map((opt, i) => `
                        <button class="option-btn" onclick="checkPracticeAnswer(${index}, ${i}, ${q.correct})">${opt}</button>
                    `).join('')}
                </div>
                <div class="explanation" id="prac-exp-${index}">
                    <strong>Explanation:</strong> ${q.exp}
                </div>
            </div>
        `;
    });
    container.innerHTML = html;
}

window.checkPracticeAnswer = function(qIndex, selectedIndex, correctIndex) {
    const qCard = document.getElementById(`prac-q-${qIndex}`);
    const options = qCard.querySelectorAll('.option-btn');
    const expBox = document.getElementById(`prac-exp-${qIndex}`);

    options.forEach((opt, i) => {
        opt.disabled = true;
        if (i === correctIndex) opt.classList.add('correct');
        if (i === selectedIndex && selectedIndex !== correctIndex) opt.classList.add('wrong');
    });

    expBox.classList.add('show');
}

function renderMock(questions) {
    const container = document.getElementById("mock-container");
    window.mockCorrectAnswers = questions.map(q => q.correct);
    
    let html = '';
    questions.forEach((q, index) => {
        html += `
            <div class="question-card mock-card" id="mock-q-${index}">
                <div class="q-text">Q${index + 1}. ${q.q}</div>
                <div class="options-list">
                    ${q.options.map((opt, i) => `
                        <label class="option-btn" style="display:block; cursor:pointer;">
                            <input type="radio" name="mock-${index}" value="${i}"> ${opt}
                        </label>
                    `).join('')}
                </div>
            </div>
        `;
    });

    html += `<button id="submit-mock" onclick="submitMock()">Submit Mock Test</button>`;
    html += `<div id="mock-result"></div>`;
    container.innerHTML = html;
}

window.submitMock = function() {
    const total = window.mockCorrectAnswers.length;
    let score = 0;

    for (let i = 0; i < total; i++) {
        const selected = document.querySelector(`input[name="mock-${i}"]:checked`);
        const qCard = document.getElementById(`mock-q-${i}`);
        const labels = qCard.querySelectorAll('.option-btn');

        if (selected) {
            const selectedVal = parseInt(selected.value);
            if (selectedVal === window.mockCorrectAnswers[i]) {
                score++;
                labels[selectedVal].classList.add('correct');
            } else {
                labels[selectedVal].classList.add('wrong');
                labels[window.mockCorrectAnswers[i]].classList.add('correct');
            }
        } else {
            // Highlight correct if not attempted
            labels[window.mockCorrectAnswers[i]].classList.add('correct');
        }
    }

    document.getElementById('mock-result').innerHTML = `<strong>Your Score: ${score} / ${total}</strong>`;
    document.getElementById('submit-mock').disabled = true;
}