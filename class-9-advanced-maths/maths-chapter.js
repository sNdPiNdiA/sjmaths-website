/* Shared JS for Class 9 Advanced Maths */

document.addEventListener("DOMContentLoaded", function () {
    const tabLinks = document.querySelectorAll('#topic-tab-bar .sj-section-link');
    const tabPanes = document.querySelectorAll('.tab-pane');
    const triggers = document.querySelectorAll('.tab-trigger');

    function switchTab(targetId) {
        tabPanes.forEach(pane => {
            pane.classList.toggle('active', pane.id === targetId);
        });

        tabLinks.forEach(link => {
            link.classList.toggle('active', link.getAttribute('data-tab') === targetId);
        });

        window.scrollTo({ top: 0, behavior: 'smooth' });

        if (window.MathJax && typeof MathJax.typesetPromise === "function") {
            MathJax.typesetPromise([document.getElementById(targetId)]);
        }
    }

    tabLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('data-tab');
            switchTab(targetId);
            history.pushState(null, null, this.getAttribute('href'));
        });
    });

    triggers.forEach(trig => {
        trig.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('data-tab');
            switchTab(targetId);
            history.pushState(null, null, '#' + targetId.replace('tab-', ''));
        });
    });

    const hash = window.location.hash.replace('#', '');
    if (hash) {
        const matchedTab = 'tab-' + hash;
        if (document.getElementById(matchedTab)) {
            switchTab(matchedTab);
        }
    }

    // Dynamic component loader using root-relative path to work at any directory depth
    async function loadComponent(id, url) {
        const target = document.getElementById(id);
        if (!target) return;
        try {
            const response = await fetch(url);
            if (response.ok) {
                target.innerHTML = await response.text();
            }
        } catch (error) {
            console.warn("Component could not be loaded:", url);
        }
    }

    loadComponent("header-container", "/components/header.html");
    loadComponent("footer-container", "/components/footer.html");
});

// Premium Solutions toggle helper
window.toggleSolution = function (btn) {
    const box = btn.nextElementSibling;
    if (!box) return;
    const open = box.classList.toggle('open');
    if (open) {
        box.style.display = 'block';
        box.style.opacity = '0';
        box.style.transition = 'opacity 0.3s ease';
        box.offsetHeight;
        box.style.opacity = '1';
        btn.innerHTML = '<i class="fas fa-eye-slash"></i> Hide Solution';
    } else {
        box.style.display = 'none';
        btn.innerHTML = '<i class="fas fa-eye"></i> Show Solution';
    }
};

// Practice Test Engine Global variables
var activeTestLevel = null;
var curQIdx = 0;
var activeTestData = [];
var studentScores = [];

var selectionArea, activeArea, tLevelBadge, tTitle, pFill, qIdxLabel, qMarksLabel, qRoot, prevBtn, nextBtn;

function initTestEngine() {
    selectionArea = document.getElementById("selection-area");
    activeArea = document.getElementById("test-active-area");
    
    tLevelBadge = document.getElementById("test-level-badge");
    tTitle = document.getElementById("test-title");
    pFill = document.getElementById("progress-fill");
    qIdxLabel = document.getElementById("question-index-label");
    qMarksLabel = document.getElementById("question-marks-label");
    qRoot = document.getElementById("question-content-root");
    
    prevBtn = document.getElementById("btn-prev");
    nextBtn = document.getElementById("btn-next");

    if (prevBtn) {
        prevBtn.addEventListener("click", function () {
            if (curQIdx > 0) {
                curQIdx--;
                loadQuestion();
            }
        });
    }

    if (nextBtn) {
        nextBtn.addEventListener("click", function () {
            if (curQIdx < activeTestData.length - 1) {
                curQIdx++;
                loadQuestion();
            } else {
                finishAndShowScorecard();
            }
        });
    }
}

window.startTest = function(level) {
    if (!selectionArea) {
        initTestEngine();
    }
    activeTestLevel = level;
    activeTestData = testsDatabase[level];
    curQIdx = 0;
    studentScores = new Array(activeTestData.length).fill(null);
    
    selectionArea.style.display = "none";
    activeArea.style.display = "block";

    var colors = { basic: "#10b981", standard: "#f59e0b", advanced: "#ef4444" };
    var levelNames = { basic: "Basic Test (Easy)", standard: "Standard Test (Medium)", advanced: "Advanced Test (Hard)" };

    tLevelBadge.style.color = colors[level];
    tLevelBadge.textContent = levelNames[level];
    tTitle.textContent = "Chapter Assessment";
    if (document.getElementById("test-icon")) {
        document.getElementById("test-icon").style.color = colors[level];
    }
    pFill.style.background = `linear-gradient(90deg, ${colors[level]}, #3b82f6)`;

    loadQuestion();
};

function loadQuestion() {
    var q = activeTestData[curQIdx];
    qIdxLabel.textContent = "Question " + (curQIdx + 1) + " of " + activeTestData.length;
    qMarksLabel.textContent = q.marks + (q.marks === 1 ? " Mark" : " Marks");
    
    var progressPct = ((curQIdx + 1) / activeTestData.length) * 100;
    pFill.style.width = progressPct + "%";

    qRoot.innerHTML = "";

    if (q.type === "mcq" || q.type === "ar") {
        var header = document.createElement("p");
        header.style.fontWeight = "600";
        header.style.marginBottom = "15px";
        header.style.whiteSpace = "pre-line";
        header.textContent = q.question;
        qRoot.appendChild(header);

        q.options.forEach(function (optText, idx) {
            var btn = document.createElement("button");
            btn.className = "option-button";
            btn.textContent = ["A", "B", "C", "D"][idx] + ". " + optText;

            if (q.userSelection === idx) {
                btn.classList.add("selected");
            }

            btn.addEventListener("click", function () {
                q.userSelection = idx;
                var parentButtons = qRoot.querySelectorAll(".option-button");
                parentButtons.forEach(function (b) { b.classList.remove("selected"); });
                btn.classList.add("selected");
            });

            qRoot.appendChild(btn);
        });

    } else {
        var header = document.createElement("p");
        header.style.fontWeight = "600";
        header.style.marginBottom = "15px";
        header.style.whiteSpace = "pre-line";
        header.textContent = q.question;
        qRoot.appendChild(header);

        var area = document.createElement("div");
        area.style.background = "#fff";
        area.style.border = "none";
        area.style.padding = "0";

        var txtArea = document.createElement("textarea");
        txtArea.placeholder = "Write your response step-by-step here...";
        txtArea.style.width = "100%";
        txtArea.style.height = "150px";
        txtArea.style.padding = "12px";
        txtArea.style.borderRadius = "12px";
        txtArea.style.border = "1px solid #cbd5e1";
        txtArea.style.fontFamily = "inherit";
        txtArea.style.fontSize = "0.95rem";
        txtArea.style.resize = "vertical";

        txtArea.value = q.userAnswerText || "";
        txtArea.addEventListener("input", function (e) {
            q.userAnswerText = e.target.value;
        });

        area.appendChild(txtArea);
        qRoot.appendChild(area);
    }

    if (window.MathJax && typeof MathJax.typesetPromise === "function") {
        MathJax.typesetPromise([qRoot]);
    }

    prevBtn.disabled = curQIdx === 0;
    if (curQIdx === activeTestData.length - 1) {
        nextBtn.textContent = "Finish Test";
    } else {
        nextBtn.textContent = "Next";
    }
    nextBtn.disabled = false;
}

window.gradeSubjectiveFromScorecard = function (qIdx, score) {
    activeTestData[qIdx].selectedScore = score;
    renderDynamicScorecard();
};

function finishAndShowScorecard() {
    activeTestData.forEach(function (q, idx) {
        if (q.type === "mcq" || q.type === "ar") {
            q.selectedScore = q.userSelection === q.correctIdx ? q.marks : 0;
        } else if (q.selectedScore === undefined) {
            q.selectedScore = 0;
        }
    });
    renderDynamicScorecard();
}

function renderDynamicScorecard() {
    var totalMarks = 0;
    var maxMarks = 0;
    var detailsHtml = "";

    activeTestData.forEach(function (q, idx) {
        maxMarks += q.marks;
        var score = q.selectedScore || 0;
        totalMarks += score;

        if (q.type === "mcq" || q.type === "ar") {
            var isCorrect = q.userSelection === q.correctIdx;
            var color = isCorrect ? "#10b981" : "#ef4444";
            var selectedLetter = q.userSelection !== undefined ? ["A", "B", "C", "D"][q.userSelection] : "None";
            var correctLetter = ["A", "B", "C", "D"][q.correctIdx];

            detailsHtml += `
                <div style="border-bottom: 1px solid #e2e8f0; padding: 20px 0; font-size: 0.95rem;">
                    <div style="display:flex; justify-content:space-between; margin-bottom: 8px;">
                        <strong style="color: ${color};">
                            Question ${idx + 1} (${q.type.toUpperCase()})
                        </strong>
                        <span style="font-weight:700; color: ${color};">${score} / ${q.marks} Mark</span>
                    </div>
                    <p style="margin: 4px 0; color: #1e293b; font-weight: 500; white-space: pre-line;">${q.question}</p>
                    <p style="margin: 4px 0; font-size: 0.88rem; color: #475569;">
                        <strong>Your Selection:</strong> ${selectedLetter} &nbsp;|&nbsp; 
                        <strong>Correct Choice:</strong> ${correctLetter}
                    </p>
                </div>
            `;
        } else {
            var color = score === q.marks ? "#10b981" : (score > 0 ? "#f59e0b" : "#ef4444");
            var userAns = q.userAnswerText ? q.userAnswerText.trim() : "No answer written.";

            detailsHtml += `
                <div style="border-bottom: 1px solid #e2e8f0; padding: 20px 0; font-size: 0.95rem;">
                    <div style="display:flex; justify-content:space-between; margin-bottom: 8px;">
                        <strong style="color: #4f46e5;">
                            Question ${idx + 1} (${q.type.toUpperCase()})
                        </strong>
                        <span style="font-weight:700; color: ${color};">${score} / ${q.marks} Marks</span>
                    </div>
                    <p style="margin: 4px 0; color: #1e293b; font-weight: 500; white-space: pre-line;">${q.question}</p>
                    <div style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 10px; border-radius: 8px; margin: 10px 0;">
                        <strong style="font-size:0.8rem; color:#475569; display:block;">Your Response:</strong>
                        <p style="margin:4px 0; white-space:pre-line; font-size:0.88rem; color:#334155;">${userAns}</p>
                    </div>
                    <div style="background: #f0fdf4; border: 1px dashed #10b981; padding: 10px; border-radius: 8px; margin: 10px 0;">
                        <strong style="font-size:0.8rem; color:#047857; display:block;">Official Marking Guidelines:</strong>
                        <p style="margin:4px 0; white-space:pre-line; font-size:0.88rem; color:#065f46;">${q.sampleAnswer}</p>
                    </div>
                    
                    <div style="margin-top: 12px;">
                        <span style="font-weight:700; font-size: 0.8rem; display:block; margin-bottom: 6px; color: #1e293b;">Grade this question:</span>
                        <div class="grading-option ${score === q.marks ? 'active-full' : ''}" onclick="gradeSubjectiveFromScorecard(${idx}, ${q.marks})">Award Full Marks (${q.marks}M)</div>
                        <div class="grading-option ${score === Math.round(q.marks/2) ? 'active-half' : ''}" onclick="gradeSubjectiveFromScorecard(${idx}, ${Math.round(q.marks/2)})">Award Partial Marks (${Math.round(q.marks/2)}M)</div>
                        <div class="grading-option ${score === 0 ? 'active-zero' : ''}" onclick="gradeSubjectiveFromScorecard(${idx}, 0)">Award 0 Marks</div>
                    </div>
                </div>
            `;
        }
    });

    var pct = Math.round((totalMarks / maxMarks) * 100);
    var badge = "";
    if (pct >= 85) badge = "Distinction Grade 🏆";
    else if (pct >= 60) badge = "Passed Standard 🎯";
    else badge = "Revision Advised 📚";

    var contentRoot = document.getElementById("test-active-area");
    contentRoot.innerHTML = `
        <section class="sj-card">
            <div style="text-align: center; margin-bottom: 30px;">
                <h2 style="font-family: 'Outfit', sans-serif; color: #4f46e5; font-size: 2.2rem; margin-bottom: 8px;">Test Assessment</h2>
                <h3 style="font-size: 1.8rem; margin-bottom: 15px;">Total Score: ${totalMarks} / ${maxMarks} Marks</h3>
                <span style="background: #f5f3ff; border: 1px solid #ddd6fe; color: #5b21b6; padding: 6px 20px; font-weight:700; font-size:0.9rem; border-radius: 20px; display:inline-block;">
                    ${badge} (${pct}%)
                </span>
            </div>

            <div style="text-align: left;">
                <h4 style="font-family: 'Outfit', sans-serif; border-bottom: 2px solid #4f46e5; padding-bottom: 8px; margin-bottom: 15px;">Detailed Marks Evaluation & Answer Keys</h4>
                <p style="font-size: 0.88rem; color:#475569; margin-bottom: 15px;"><i class="fas fa-circle-info"></i> For subjective/descriptive questions, compare your written response with the official marking key and click the grading buttons to dynamically update your score.</p>
                <div id="scorecard-details-root">${detailsHtml}</div>
            </div>

            <div style="text-align: center; margin-top: 30px;">
                <button onclick="location.reload()" class="test-action-btn">Return to Tests List</button>
            </div>
        </section>
    `;

    if (window.MathJax && typeof MathJax.typesetPromise === "function") {
        MathJax.typesetPromise([document.getElementById("scorecard-details-root")]);
    }
}
