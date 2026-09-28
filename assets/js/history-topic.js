document.addEventListener("DOMContentLoaded", () => {
  const quiz = JSON.parse(document.getElementById("history-quiz-data").textContent || "[]");
  const test = JSON.parse(document.getElementById("history-test-data").textContent || "[]");
  const esc = (value) => String(value ?? "").replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;").replace(/'/g, "&#39;");
  let quizScore = 0;
  const answered = /* @__PURE__ */ new Set();
  const feedback = (ok, text) => '<div class="quiz-feedback ' + (ok ? "correct" : "incorrect") + '"><strong>' + (ok ? "Correct" : "Review") + "</strong><p>" + esc(text) + "</p></div>";
  function markQuiz(i, ok, text) {
    if (answered.has(i)) return;
    answered.add(i);
    if (ok) quizScore++;
    const card = document.getElementById("quiz-card-" + i);
    card.dataset.answered = "true";
    card.querySelectorAll("button").forEach((button) => button.disabled = true);
    document.getElementById("quiz-feedback-" + i).innerHTML = feedback(ok, text);
    document.getElementById("quiz-score").textContent = "Score: " + quizScore + " / " + quiz.length;
  }
  document.querySelectorAll("[data-quiz]").forEach((button) => button.addEventListener("click", () => {
    const i = Number(button.dataset.quiz), option = Number(button.dataset.option), question = quiz[i];
    document.querySelectorAll("#quiz-card-" + i + " [data-option]").forEach((item, index) => {
      item.disabled = true;
      if (index === question.correct_index) item.classList.add("correct");
      if (index === option && option !== question.correct_index) item.classList.add("incorrect");
    });
    markQuiz(i, option === question.correct_index, question.explanation);
  }));
  document.querySelectorAll("[data-fill]").forEach((button) => button.addEventListener("click", () => {
    const i = Number(button.dataset.fill), question = quiz[i], value = document.getElementById("quiz-input-" + i).value.trim().toLowerCase();
    markQuiz(i, (question.accepted_answers || []).some((answer) => value === String(answer).trim().toLowerCase()), "Accepted answer(s): " + (question.accepted_answers || []).join(", ") + " — " + question.explanation);
  }));
  document.querySelectorAll("[data-short]").forEach((button) => button.addEventListener("click", () => {
    const i = Number(button.dataset.short), question = quiz[i];
    markQuiz(i, false, "Expected answer: " + (question.expected_answer || "See the explanation") + " — " + question.explanation);
  }));
  document.getElementById("btn-reset-quiz").addEventListener("click", () => location.reload());
  const chosen = {};
  let submitted = false;
  document.querySelectorAll("[data-test]").forEach((button) => button.addEventListener("click", () => {
    if (submitted) return;
    const i = Number(button.dataset.test);
    chosen[i] = Number(button.dataset.option);
    document.querySelectorAll("#test-card-" + i + " [data-option]").forEach((item) => item.classList.remove("selected"));
    button.classList.add("selected");
  }));
  function submitTest() {
    if (submitted) return;
    submitted = true;
    clearInterval(timer);
    timer = null;
    let score = 0;
    test.forEach((question, i) => {
      const answer = chosen[i];
      if (answer === question.correct_index) score++;
      document.querySelectorAll("#test-card-" + i + " [data-option]").forEach((item, index) => {
        item.disabled = true;
        if (index === question.correct_index) item.classList.add("correct");
        if (index === answer && answer !== question.correct_index) item.classList.add("incorrect");
      });
      document.getElementById("test-feedback-" + i).innerHTML = feedback(answer === question.correct_index, question.explanation);
    });
    document.getElementById("test-score").textContent = score;
    document.getElementById("test-result").classList.remove("hidden");
    document.getElementById("btn-submit-test").classList.add("hidden");
  }
  document.getElementById("btn-submit-test").addEventListener("click", submitTest);
  document.getElementById("btn-retake-test").addEventListener("click", () => location.reload());
  let timer = null, remaining = 600;
  function startTimer() {
    if (timer || submitted) return;
    timer = setInterval(() => {
      remaining--;
      document.getElementById("test-timer").textContent = String(Math.floor(remaining / 60)).padStart(2, "0") + ":" + String(remaining % 60).padStart(2, "0");
      if (remaining <= 0) {
        submitTest();
      }
    }, 1e3);
  }
  const tabs = document.querySelectorAll(".tab-btn"), panels = document.querySelectorAll(".tab-panel");
  tabs.forEach((button) => button.addEventListener("click", () => {
    tabs.forEach((item) => {
      item.classList.remove("active");
      item.setAttribute("aria-selected", "false");
    });
    panels.forEach((panel) => {
      panel.classList.remove("active");
      panel.classList.add("hidden");
    });
    button.classList.add("active");
    button.setAttribute("aria-selected", "true");
    document.getElementById(button.dataset.tab).classList.remove("hidden");
    document.getElementById(button.dataset.tab).classList.add("active");
    if (button.dataset.tab === "tab-test") startTimer();
    window.scrollTo({ top: document.querySelector(".history-tab-shell").offsetTop - 15, behavior: "smooth" });
  }));
});
