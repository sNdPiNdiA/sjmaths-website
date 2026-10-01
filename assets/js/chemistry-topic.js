(function() {
  const bilingual = document.currentScript?.getAttribute("data-chemistry-runtime") === "bilingual";
  document.addEventListener("DOMContentLoaded", () => {
    if (bilingual) {
      let setLanguage = function(lang, save) {
        if (lang !== "hi" && lang !== "en") lang = "en";
        document.documentElement.setAttribute("data-lang", lang);
        if (save !== false) {
          localStorage.setItem("sjmaths_preferred_language", lang);
        }
        if (langToggleBtn) {
          langToggleBtn.innerHTML = lang === "hi" ? '🌐 <span style="font-weight:900;">हिन्दी</span> (EN)' : '🌐 <span style="font-weight:900;">EN</span> (हिन्दी)';
        }
      };
      const langToggleBtn = document.getElementById("btn-lang-toggle");
      const savedLang = localStorage.getItem("sjmaths_preferred_language") || "en";
      setLanguage(savedLang, false);
      if (langToggleBtn) {
        langToggleBtn.addEventListener("click", () => {
          const currentLang = document.documentElement.getAttribute("data-lang") || "en";
          const nextLang = currentLang === "en" ? "hi" : "en";
          setLanguage(nextLang, true);
        });
      }
    }
    const themeToggleBtn = document.getElementById("btn-theme-toggle");
    const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
    const savedTheme = localStorage.getItem("sjmaths_theme") || localStorage.getItem("sj_theme");
    if (savedTheme === "dark" || !savedTheme && prefersDark) {
      document.body.classList.add("dark-mode");
      document.documentElement.classList.add("dark");
      if (themeToggleBtn) themeToggleBtn.textContent = "☀️ Light Mode";
    }
    if (themeToggleBtn) {
      themeToggleBtn.addEventListener("click", () => {
        const isDark = document.body.classList.toggle("dark-mode");
        document.documentElement.classList.toggle("dark", isDark);
        localStorage.setItem("sjmaths_theme", isDark ? "dark" : "light");
        localStorage.setItem("sj_theme", isDark ? "dark" : "light");
        themeToggleBtn.textContent = isDark ? "☀️ Light Mode" : "🌙 Dark Mode";
      });
    }
    const tabBtns = document.querySelectorAll(".tab-btn");
    const tabPanels = document.querySelectorAll(".tab-panel");
    tabBtns.forEach((btn) => {
      btn.addEventListener("click", () => {
        const targetTab = btn.getAttribute("data-tab");
        tabBtns.forEach((b) => {
          b.classList.remove("active");
          b.setAttribute("aria-selected", "false");
        });
        tabPanels.forEach((p) => {
          p.classList.remove("active");
          p.classList.add("hidden");
        });
        btn.classList.add("active");
        btn.setAttribute("aria-selected", "true");
        const activePanel = document.getElementById(targetTab);
        if (activePanel) {
          activePanel.classList.remove("hidden");
          activePanel.classList.add("active");
        }
        const stickyWrap = document.querySelector(".study-tabs-sticky-wrapper");
        if (stickyWrap) {
          window.scrollTo({ top: stickyWrap.offsetTop - 15, behavior: "smooth" });
        }
      });
    });
    let quizScore = 0;
    const answeredQuestions = /* @__PURE__ */ new Set();
    const quizOptionBtns = document.querySelectorAll(".quiz-option-btn");
    quizOptionBtns.forEach((btn) => {
      btn.addEventListener("click", () => {
        const qIndex = parseInt(btn.getAttribute("data-qindex"), 10);
        const optIndex = parseInt(btn.getAttribute("data-optindex"), 10);
        const isPyq = btn.hasAttribute("data-pyqindex");
        if (isPyq) {
          const pyqIdx = parseInt(btn.getAttribute("data-pyqindex"), 10);
          const card2 = document.getElementById("pyq-card-" + pyqIdx);
          const correct = parseInt(card2.getAttribute("data-correct"), 10);
          const expl = document.getElementById("pyq-expl-" + pyqIdx);
          card2.querySelectorAll(".quiz-option-btn").forEach((b, idx) => {
            b.disabled = true;
            if (idx === correct) b.classList.add("correct");
            else if (idx === optIndex && optIndex !== correct) b.classList.add("incorrect");
          });
          if (expl) expl.classList.remove("hidden");
          return;
        }
        const card = document.getElementById("q-card-" + qIndex);
        if (!card) return;
        const correctIndex = parseInt(card.getAttribute("data-correct"), 10);
        const feedback = document.getElementById("feedback-" + qIndex);
        const statusEl = feedback ? feedback.querySelector(".feedback-indicator") : null;
        if (answeredQuestions.has(qIndex)) return;
        answeredQuestions.add(qIndex);
        const allBtns = card.querySelectorAll(".quiz-option-btn");
        allBtns.forEach((b, idx) => {
          b.disabled = true;
          if (idx === correctIndex) b.classList.add("correct");
          else if (idx === optIndex && optIndex !== correctIndex) b.classList.add("incorrect");
        });
        const letters = ["A", "B", "C", "D"];
        if (optIndex === correctIndex) {
          quizScore++;
          if (statusEl) {
            statusEl.textContent = "✓ Correct Answer!";
            statusEl.className = "feedback-indicator correct";
          }
          if (feedback) feedback.className = "q-feedback correct";
        } else {
          if (statusEl) {
            statusEl.textContent = "✗ Incorrect. Correct Option: " + letters[correctIndex];
            statusEl.className = "feedback-indicator incorrect";
          }
          if (feedback) feedback.className = "q-feedback incorrect";
        }
        if (feedback) feedback.classList.remove("hidden");
        const scoreEl = document.getElementById("quizScore");
        if (scoreEl) scoreEl.textContent = quizScore;
      });
    });
    const btnResetQuiz = document.getElementById("btnResetQuiz");
    if (btnResetQuiz) {
      btnResetQuiz.addEventListener("click", () => {
        quizScore = 0;
        answeredQuestions.clear();
        const scoreEl = document.getElementById("quizScore");
        if (scoreEl) scoreEl.textContent = "0";
        document.querySelectorAll(".quiz-option-btn").forEach((b) => {
          b.disabled = false;
          b.classList.remove("correct", "incorrect");
        });
        document.querySelectorAll(".q-feedback").forEach((f) => {
          f.classList.add("hidden");
          f.classList.remove("correct", "incorrect");
        });
      });
    }
    let testTimer = null;
    let secondsLeft = 600;
    const btnStartTest = document.getElementById("btnStartTest");
    const testStartWrap = document.getElementById("testStartWrap");
    const testActiveWrap = document.getElementById("testActiveWrap");
    const timerDisplay = document.getElementById("timerDisplay");
    if (btnStartTest) {
      btnStartTest.addEventListener("click", () => {
        if (testStartWrap) testStartWrap.classList.add("hidden");
        if (testActiveWrap) testActiveWrap.classList.remove("hidden");
        testTimer = setInterval(() => {
          secondsLeft--;
          const mins = Math.floor(secondsLeft / 60);
          const secs = secondsLeft % 60;
          if (timerDisplay) {
            timerDisplay.textContent = (mins < 10 ? "0" : "") + mins + ":" + (secs < 10 ? "0" : "") + secs;
          }
          if (secondsLeft <= 0) {
            clearInterval(testTimer);
            submitTest();
          }
        }, 1e3);
      });
    }
    const selectedTestAnswers = {};
    document.querySelectorAll(".test-option-btn").forEach((btn) => {
      btn.addEventListener("click", () => {
        const tIndex = parseInt(btn.getAttribute("data-tindex"), 10);
        const optIndex = parseInt(btn.getAttribute("data-optindex"), 10);
        selectedTestAnswers[tIndex] = optIndex;
        const card = document.getElementById("t-card-" + tIndex);
        if (card) {
          card.querySelectorAll(".test-option-btn").forEach((b) => b.classList.remove("selected"));
        }
        btn.classList.add("selected");
      });
    });
    function submitTest() {
      if (testTimer) clearInterval(testTimer);
      let score = 0;
      const testCards = document.querySelectorAll(".test-question-card");
      testCards.forEach((card, idx) => {
        const correct = parseInt(card.getAttribute("data-correct"), 10);
        const userAns = selectedTestAnswers[idx];
        const feedback = document.getElementById("t-feedback-" + idx);
        const btns = card.querySelectorAll(".test-option-btn");
        btns.forEach((b, oIdx) => {
          b.disabled = true;
          if (oIdx === correct) b.classList.add("correct");
          else if (oIdx === userAns && userAns !== correct) b.classList.add("incorrect");
        });
        if (userAns === correct) score++;
        if (feedback) feedback.classList.remove("hidden");
      });
      const resScore = document.getElementById("resFinalScore");
      if (resScore) resScore.textContent = score;
      const resModal = document.getElementById("testResultModal");
      if (resModal) resModal.classList.remove("hidden");
      const btnSub = document.getElementById("btnSubmitTest");
      if (btnSub) btnSub.classList.add("hidden");
    }
    const btnSubmitTest = document.getElementById("btnSubmitTest");
    if (btnSubmitTest) btnSubmitTest.addEventListener("click", submitTest);
    const btnRetakeTest = document.getElementById("btnRetakeTest");
    if (btnRetakeTest) {
      btnRetakeTest.addEventListener("click", () => {
        location.reload();
      });
    }
  });
})();
