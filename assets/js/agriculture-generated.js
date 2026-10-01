document.addEventListener('DOMContentLoaded', () => {
  // Dual-Class Theme Toggle
  const btnTheme = document.getElementById('btn-theme-toggle');
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  const savedTheme = localStorage.getItem('sjmaths_theme') || localStorage.getItem('sj_theme');
  if (savedTheme === 'dark' || (!savedTheme && prefersDark)) {
    document.body.classList.add('dark-mode');
    document.documentElement.classList.add('dark');
    if (btnTheme) btnTheme.textContent = '☀️ Light Mode';
  }
  if (btnTheme) {
    btnTheme.addEventListener('click', () => {
      const isDark = document.body.classList.toggle('dark-mode');
      document.documentElement.classList.toggle('dark', isDark);
      localStorage.setItem('sjmaths_theme', isDark ? 'dark' : 'light');
      localStorage.setItem('sj_theme', isDark ? 'dark' : 'light');
      btnTheme.textContent = isDark ? '☀️ Light Mode' : '🌙 Dark Mode';
    });
  }

  // Tab Switching
  const tabBtns = document.querySelectorAll('.tab-btn');
  const tabPanels = document.querySelectorAll('.tab-panel');

  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const targetId = btn.getAttribute('data-tab');
      tabBtns.forEach(b => {
        b.classList.remove('active');
        b.setAttribute('aria-selected', 'false');
      });
      tabPanels.forEach(p => {
        p.classList.remove('active');
        p.classList.add('hidden');
      });

      btn.classList.add('active');
      btn.setAttribute('aria-selected', 'true');
      const activePanel = document.getElementById(targetId);
      if (activePanel) {
        activePanel.classList.remove('hidden');
        activePanel.classList.add('active');
      }
      window.scrollTo({ top: document.querySelector('.study-tabs-sticky-wrapper').offsetTop - 20, behavior: 'smooth' });
    });
  });

  // Practice Quiz Logic
  let quizScore = 0;
  const answeredQuestions = new Set();
  const quizOptionBtns = document.querySelectorAll('.quiz-option-btn');

  quizOptionBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const qIndex = parseInt(btn.getAttribute('data-qindex'), 10);
      const optIndex = parseInt(btn.getAttribute('data-optindex'), 10);
      const card = document.getElementById('q-card-' + qIndex);
      const correctIndex = parseInt(card.getAttribute('data-correct'), 10);
      const feedback = document.getElementById('feedback-' + qIndex);

      if (answeredQuestions.has(qIndex)) return;
      answeredQuestions.add(qIndex);

      const allBtnsForQ = card.querySelectorAll('.quiz-option-btn');
      allBtnsForQ.forEach((b, idx) => {
        b.disabled = true;
        if (idx === correctIndex) b.classList.add('correct');
        else if (idx === optIndex && optIndex !== correctIndex) b.classList.add('incorrect');
      });

      const letters = ['A', 'B', 'C', 'D'];
      if (optIndex === correctIndex) {
        quizScore++;
        document.getElementById('quizScore').textContent = quizScore;
        feedback.querySelector('.feedback-indicator').textContent = '✓ Correct Answer!';
        feedback.classList.add('correct');
      } else {
        feedback.querySelector('.feedback-indicator').textContent = '✗ Incorrect. Correct Option: ' + letters[correctIndex];
        feedback.classList.add('incorrect');
      }
      feedback.classList.remove('hidden');
    });
  });

  const btnResetQuiz = document.getElementById('btnResetQuiz');
  if (btnResetQuiz) {
    btnResetQuiz.addEventListener('click', () => {
      quizScore = 0;
      answeredQuestions.clear();
      document.getElementById('quizScore').textContent = '0';
      document.querySelectorAll('.quiz-option-btn').forEach(b => {
        b.disabled = false;
        b.classList.remove('correct', 'incorrect');
      });
      document.querySelectorAll('.q-feedback').forEach(f => {
        f.classList.add('hidden');
        f.classList.remove('correct', 'incorrect');
      });
    });
  }

  // Topic Test Logic
  const btnStartTest = document.getElementById('btnStartTest');
  const testStartWrap = document.getElementById('testStartWrap');
  const testActiveWrap = document.getElementById('testActiveWrap');
  const timerDisplay = document.getElementById('timerDisplay');
  let testTimer = null;
  let secondsLeft = 600;

  if (btnStartTest) {
    btnStartTest.addEventListener('click', () => {
      testStartWrap.classList.add('hidden');
      testActiveWrap.classList.remove('hidden');
      testTimer = setInterval(() => {
        secondsLeft--;
        const mins = Math.floor(secondsLeft / 60);
        const secs = secondsLeft % 60;
        timerDisplay.textContent = (mins < 10 ? '0' : '') + mins + ':' + (secs < 10 ? '0' : '') + secs;
        if (secondsLeft <= 0) {
          clearInterval(testTimer);
          submitTest();
        }
      }, 1000);
    });
  }

  const selectedTestAnswers = {};
  document.querySelectorAll('.test-option-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const tIndex = parseInt(btn.getAttribute('data-tindex'), 10);
      const optIndex = parseInt(btn.getAttribute('data-optindex'), 10);
      selectedTestAnswers[tIndex] = optIndex;
      const card = document.getElementById('t-card-' + tIndex);
      card.querySelectorAll('.test-option-btn').forEach(b => b.classList.remove('selected'));
      btn.classList.add('selected');
    });
  });

  function submitTest() {
    if (testTimer) clearInterval(testTimer);
    let score = 0;
    const testCards = document.querySelectorAll('.test-question-card');
    testCards.forEach((card, idx) => {
      const correct = parseInt(card.getAttribute('data-correct'), 10);
      const userAns = selectedTestAnswers[idx];
      const feedback = document.getElementById('t-feedback-' + idx);
      const btns = card.querySelectorAll('.test-option-btn');
      btns.forEach((b, oIdx) => {
        b.disabled = true;
        if (oIdx === correct) b.classList.add('correct');
        else if (oIdx === userAns && userAns !== correct) b.classList.add('incorrect');
      });
      if (userAns === correct) score++;
      feedback.classList.remove('hidden');
    });
    document.getElementById('resFinalScore').textContent = score;
    document.getElementById('testResultModal').classList.remove('hidden');
    document.getElementById('btnSubmitTest').classList.add('hidden');
  }

  const btnSubmitTest = document.getElementById('btnSubmitTest');
  if (btnSubmitTest) btnSubmitTest.addEventListener('click', submitTest);

  const btnRetakeTest = document.getElementById('btnRetakeTest');
  if (btnRetakeTest) {
    btnRetakeTest.addEventListener('click', () => {
      location.reload();
    });
  }
});
