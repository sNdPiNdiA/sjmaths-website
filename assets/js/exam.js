document.addEventListener('DOMContentLoaded', () => {
    // 1. Theme Toggle
    window.toggleTheme = function () {
        document.body.classList.toggle("dark");
        localStorage.setItem("theme", document.body.classList.contains("dark") ? "dark" : "light");
    };
    if (localStorage.getItem("theme") === "dark") document.body.classList.add("dark");

    // 2. Sidebar Navigation
    window.toggleSidebar = function () {
        document.getElementById("sidebar").classList.toggle("open");
    };

    window.goTo = function (id) {
        const el = document.getElementById(id);
        if (el) {
            el.scrollIntoView({ behavior: "smooth" });
            toggleSidebar();
        }
    };

    // 3. Exam Timer (3 Hours)
    const examTimer = document.getElementById('examTimer');
    if (examTimer) {
        let seconds = 10800; // 3 hours
        const timerInterval = setInterval(() => {
            if (seconds <= 0) {
                clearInterval(timerInterval);
                examTimer.textContent = "00:00:00";
                alert("Time's up! Your exam will be submitted automatically.");
                if (typeof window.openSubmit === 'function') window.openSubmit();
                return;
            }
            seconds--;
            const h = String(Math.floor(seconds / 3600)).padStart(2, "0");
            const m = String(Math.floor((seconds % 3600) / 60)).padStart(2, "0");
            const s = String(seconds % 60).padStart(2, "0");
            examTimer.textContent = `${h}:${m}:${s}`;
            if (seconds < 300) examTimer.style.color = "#dc3545"; // Red warning for last 5 mins
        }, 1000);
    }

    // 4. Question Time Tracking
    let currentQ = null;
    let qTimer = null;
    const questionTime = {};
    const setId = document.body.dataset.setId || "default_set";
    const storageKey = `${setId}_question_time`;

    function startQTimer(qid) {
        if (currentQ === qid) return;
        if (qTimer) clearInterval(qTimer);

        currentQ = qid;
        questionTime[qid] = questionTime[qid] || 0;

        qTimer = setInterval(() => {
            questionTime[qid]++;
        }, 1000);
    }

    // Observer for visible questions
    const qObserver = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting && entry.intersectionRatio > 0.6) {
                const qid = entry.target.dataset.qid;
                if (qid) startQTimer(qid);
            }
        });
    }, { threshold: 0.6 });

    // Expose observer for questions-loader.js to use
    window.qObserver = qObserver;

    // 5. Submit Logic
    function saveQuestionTime() {
        if (qTimer) clearInterval(qTimer);
        localStorage.setItem(storageKey, JSON.stringify(questionTime));
    }

    window.openSubmit = async function () {
        saveQuestionTime();

        const popupSub = document.querySelector('.popup-sub');
        const originalText = popupSub ? popupSub.getAttribute('data-original') || popupSub.innerHTML : "";
        if (popupSub && !popupSub.getAttribute('data-original')) {
            popupSub.setAttribute('data-original', originalText);
        }

        try {
            const res = await fetch('answers.json');
            if (res.ok) {
                const data = await res.json();
                const answers = data.answers || {};
                let score = 0;
                let totalMcqs = 0;
                let attempted = 0;

                const processedQids = new Set();
                document.querySelectorAll('input[type="radio"]').forEach(radio => {
                    const qid = radio.name;
                    if (processedQids.has(qid)) return;
                    processedQids.add(qid);

                    if (answers[qid] && answers[qid].ans) {
                        totalMcqs++;
                        const selected = document.querySelector(`input[name="${qid}"]:checked`);
                        if (selected) {
                            attempted++;
                            // Extract option letter from answer string like "(a) Answer text"
                            const match = answers[qid].ans.match(/^\(([a-z])\)/i);
                            if (match && match[1].toLowerCase() === selected.value) {
                                score++;
                            }
                        }
                    }
                });

                if (totalMcqs > 0 && popupSub) {
                    popupSub.innerHTML = `<div style="margin-bottom:15px; padding:10px; background:#f0fdf4; border-radius:8px; border:1px solid #bbf7d0;">
                        <h3 style="color:#166534; margin:0 0 5px 0; font-size:1.1rem;">MCQ Score: ${score} / ${totalMcqs}</h3>
                        <p style="margin:0; font-size:0.9rem; color:#15803d;">You attempted ${attempted} questions.</p>
                    </div>` + originalText;
                }
            }
        } catch (e) {
            console.log("Auto-grading skipped:", e);
        }

        document.getElementById("submitOverlay").style.display = "flex";
    };

    window.closePopup = function () {
        document.getElementById("submitOverlay").style.display = "none";
    };

    window.goFreeResult = function () {
        // Assumes free-evaluation.html is in the same directory
        window.location.href = "free-evaluation.html";
    };
});