/* Shared JS for all Class 10 Science Chapters */

// Global state variables for test engine
const selections = {
    1: {},
    2: {},
    3: {}
};
let currentLevel = 1;
let levelState = 1; // Alias for chapters 7-8 (renamed to avoid conflict with function level())

/* ==========================================================================
   Chapters 1-3 Helper Functions
   ========================================================================== */

function openTab(name, button, skipScroll) {
    const targetPanel = document.getElementById("tab-" + name);
    if (!targetPanel) return;

    document.querySelectorAll(".tab-panel")
        .forEach(panel => panel.classList.remove("active"));

    targetPanel.classList.add("active");

    document.querySelectorAll(".nav-btn")
        .forEach(btn => btn.classList.remove("active"));

    if (button) {
        button.classList.add("active");
    } else {
        const btn = document.querySelector(`.nav-btn[onclick*="'${name}'"]`);
        if (btn) btn.classList.add("active");
    }

    try {
        const key = 'activeTab_' + window.location.pathname;
        localStorage.setItem(key, name);
        if (history.replaceState) {
            history.replaceState(null, null, '#' + name);
        }
    } catch (e) {}

    if (!skipScroll) {
        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });
    }
}

function renderTest(level) {
    const container = document.getElementById("test" + level);
    if (!container) return;
    container.innerHTML = "";

    tests[level].forEach((item, index) => {
        const card = document.createElement("div");
        card.className = "test-question";
        card.dataset.answer = item.a;
        card.innerHTML = `
            <div class="test-number">
                QUESTION ${index + 1} / 10
            </div>
            <h3>${item.q}</h3>
            <div class="options">
                ${item.o.map((option, i) => `
                    <button class="option" onclick="selectOption(this, ${level}, ${index}, ${i})">
                        ${option}
                    </button>
                `).join("")}
            </div>
        `;
        container.appendChild(card);
    });
}

function selectOption(button, level, question, answer) {
    const card = button.closest(".test-question");
    card.querySelectorAll(".option")
        .forEach(btn => {
            btn.classList.remove(
                "correct-answer",
                "wrong-answer"
            );
        });

    button.style.borderColor = "#cfd3d7";
    selections[level][question] = answer;
    button.style.borderColor = "#e5483f";
}

function submitTest(level) {
    let score = 0;
    tests[level].forEach((item, index) => {
        const selected = selections[level][index];
        const card = document.querySelector(
            `#test${level} .test-question:nth-child(${index + 1})`
        );
        const buttons = card.querySelectorAll(".option");

        buttons.forEach(btn => {
            btn.classList.remove(
                "correct-answer",
                "wrong-answer"
            );
        });

        if (selected !== undefined) {
            if (selected === item.a) {
                score++;
                buttons[selected].classList.add("correct-answer");
            } else {
                buttons[selected].classList.add("wrong-answer");
                buttons[item.a].classList.add("correct-answer");
            }
        } else {
            buttons[item.a].classList.add("correct-answer");
        }
    });

    const scoreBox = document.getElementById(`score${level}`);
    if (scoreBox) {
        scoreBox.innerHTML = `
            <div class="score-title">Your Score: ${score} / 10</div>
            <p>Well done! Review the answers above.</p>
        `;
        scoreBox.style.display = "block";
    }
}

function switchLevel(level) {
    document.querySelectorAll(".level-btn")
        .forEach(btn => btn.classList.remove("active"));
    
    const activeBtn = document.querySelector(`.level-btn:nth-child(${level})`);
    if (activeBtn) activeBtn.classList.add("active");

    document.querySelectorAll(".test-level-pane")
        .forEach(pane => pane.classList.remove("active"));

    const targetPane = document.getElementById("level" + level);
    if (targetPane) targetPane.classList.add("active");
}

// Chapter 3 specific layout listeners
document.addEventListener("DOMContentLoaded", () => {
    const navButtons = document.querySelectorAll(".nav-btn");
    const tabs = document.querySelectorAll(".tab");
    if (navButtons.length > 0 && tabs.length > 0) {
        navButtons.forEach(button => {
            button.addEventListener("click", () => {
                const target = button.dataset.tab;
                if (target) {
                    tabs.forEach(tab => tab.classList.remove("active"));
                    const targetEl = document.getElementById(target);
                    if (targetEl) targetEl.classList.add("active");
                    navButtons.forEach(btn => btn.classList.remove("active"));
                    button.classList.add("active");
                    window.scrollTo({ top: 0, behavior: "smooth" });
                }
            });
        });
    }
});


/* ==========================================================================
   Chapters 4-6 Helper Functions
   ========================================================================== */

function showTab(id, btn) {
    document.querySelectorAll('.tab').forEach(x => x.classList.remove('active'));
    const target = document.getElementById(id);
    if (target) target.classList.add('active');
    document.querySelectorAll('.nav-btn').forEach(x => x.classList.remove('active'));
    if (btn) btn.classList.add('active');
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

function toggle(btn) {
    const a = btn.nextElementSibling;
    if (a) {
        a.classList.toggle('show');
        btn.textContent = a.classList.contains('show') ? 'Hide answer' : 'Show answer';
    }
}

function level(n, btn) {
    currentLevel = n;
    document.querySelectorAll('.test').forEach(x => x.classList.remove('active'));
    const target = document.getElementById('level' + n);
    if (target) target.classList.add('active');
    document.querySelectorAll('.level-btn').forEach(x => x.classList.remove('active'));
    if (btn) btn.classList.add('active');
    const result = document.getElementById('result');
    if (result) result.classList.remove('show');
}

function pick(btn, val) {
    if (val !== undefined) {
        // Chapters 4-6 logic
        const q = btn.parentElement;
        q.querySelectorAll('.option').forEach(x => x.classList.remove('selected'));
        btn.classList.add('selected');
        const index = [...document.querySelectorAll('#level' + currentLevel + ' .test-question')].indexOf(q);
        selections[currentLevel + '-' + index] = val;
    } else {
        // Chapters 7-8 logic (btn acts as 'b')
        btn.parentElement.querySelectorAll('.opt').forEach(x => x.classList.remove('sel'));
        btn.classList.add('sel');
    }
}

function gradeTest() {
    const qs = document.querySelectorAll('#level' + currentLevel + ' .test-question');
    let score = 0, attempt = 0;
    qs.forEach((q, i) => {
        const selected = q.querySelector('.option.selected');
        q.querySelectorAll('.option').forEach(o => o.classList.remove('correct', 'wrong'));
        if (selected) {
            attempt++;
            if (selected.textContent.trim().startsWith(answers[currentLevel][i])) {
                score++;
                selected.classList.add('correct');
            } else {
                selected.classList.add('wrong');
            }
        }
    });
    const pct = Math.round(score / qs.length * 100);
    const r = document.getElementById('result');
    if (r) {
        r.classList.add('show');
        r.innerHTML = '<div class="score">' + score + '/' + qs.length + '</div><p><b>' + pct + '%</b> • Attempted ' + attempt + '/' + qs.length + '</p><p>' + (pct >= 80 ? 'Excellent. Move to the next level.' : pct >= 60 ? 'Good. Revisit the weak concepts once.' : 'Revise the Learn + Revision tabs and try again.') + '</p>';
        r.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
}


/* ==========================================================================
   Chapters 7-8 Helper Functions
   ========================================================================== */

function tab(id, b) {
    document.querySelectorAll('.tab').forEach(x => x.classList.remove('on'));
    const target = document.getElementById(id);
    if (target) target.classList.add('on');
    document.querySelectorAll('.nav button').forEach(x => x.classList.remove('on'));
    if (b) b.classList.add('on');
    scrollTo(0, 0);
}

function setLevel(n, b) {
    levelState = n;
    document.querySelectorAll('.test').forEach(x => x.classList.remove('on'));
    const target = document.getElementById('L' + n);
    if (target) target.classList.add('on');
    document.querySelectorAll('.lev').forEach(x => x.classList.remove('on'));
    if (b) b.classList.add('on');
    const result = document.getElementById('result');
    if (result) result.classList.remove('show');
}

function grade() {
    const key = KEY[levelState];
    const qs = document.querySelectorAll('#L' + levelState + ' .q');
    const r = document.getElementById('result');
    let s = 0, a = 0;
    qs.forEach((q, i) => {
        q.querySelectorAll('.opt').forEach(x => x.classList.remove('good', 'bad'));
        let x = q.querySelector('.sel');
        if (x) {
            a++;
            if (x.dataset.v === key[i]) s++;
            x.classList.add(x.dataset.v === key[i] ? 'good' : 'bad');
        }
        q.querySelectorAll('.opt').forEach(x => {
            if (x.dataset.v === key[i]) x.classList.add('good');
        });
    });
    if (r) {
        r.classList.add('show');
        r.innerHTML = '<div class="score">' + s + '/' + qs.length + '</div><p>' + Math.round(s / qs.length * 100) + '% • Attempted ' + a + '/' + qs.length + '</p>';
        r.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
}


/* ==========================================================================
   Chapter 9 Helper Functions
   ========================================================================== */

document.addEventListener("DOMContentLoaded", () => {
    // Restore remembered tab from hash or localStorage
    try {
        const hash = window.location.hash.replace('#', '').trim();
        const key = 'activeTab_' + window.location.pathname;
        const savedTab = hash || localStorage.getItem(key);
        if (savedTab) {
            const panel = document.getElementById("tab-" + savedTab);
            if (panel) {
                const btn = document.querySelector(`.nav-btn[onclick*="'${savedTab}'"]`);
                openTab(savedTab, btn, true);
            }
        }
    } catch (e) {}

    const buttons = [...document.querySelectorAll("[data-page]")];
    const pages = [...document.querySelectorAll(".page")];
    if (buttons.length > 0 && pages.length > 0) {
        window.activate = function(id) {
            pages.forEach(p => p.classList.toggle("active", p.id === id));
            buttons.forEach(b => b.classList.toggle("active", b.getAttribute("data-page") === id));
            window.scrollTo({ top: 0, behavior: "smooth" });
        };
        buttons.forEach(b => {
            b.addEventListener("click", () => {
                activate(b.getAttribute("data-page"));
            });
        });
    }
});
