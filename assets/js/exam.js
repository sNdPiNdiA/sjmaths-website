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
        setInterval(() => {
            seconds--;
            const h = String(Math.floor(seconds / 3600)).padStart(2, "0");
            const m = String(Math.floor((seconds % 3600) / 60)).padStart(2, "0");
            const s = String(seconds % 60).padStart(2, "0");
            examTimer.textContent = `${h}:${m}:${s}`;
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

    window.openSubmit = function () {
        saveQuestionTime();
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