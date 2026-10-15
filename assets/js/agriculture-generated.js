function initAgricultureGenerated() {
  // Theme preference follows the shared SJMaths preference contract.
  const btnTheme = document.getElementById('btn-theme-toggle');
  const themePreferenceKey = 'sjmaths.theme.preference';
  const isDarkPreference = preference => preference === 'dark'
    || (preference === 'system' && window.matchMedia('(prefers-color-scheme: dark)').matches);
  const updateThemeToggle = isDark => {
    document.documentElement.classList.toggle('dark', isDark);
    if (!btnTheme) return;
    btnTheme.textContent = isDark ? '☀️ Light Mode' : '🌙 Dark Mode';
    btnTheme.setAttribute('aria-label', isDark ? 'Switch to light mode' : 'Switch to dark mode');
    btnTheme.setAttribute('aria-pressed', String(isDark));
  };
  const applyLocalTheme = (preference, persist = true) => {
    if (!['system', 'light', 'dark'].includes(preference)) return;
    themePreference = preference;
    const isDark = isDarkPreference(preference);
    document.documentElement.dataset.theme = isDark ? 'dark' : 'light';
    document.documentElement.dataset.themePreference = preference;
    document.documentElement.style.colorScheme = isDark ? 'dark' : 'light';
    document.documentElement.classList.toggle('dark-mode', isDark);
    document.body.classList.toggle('dark-mode', isDark);
    updateThemeToggle(isDark);
    if (persist) {
      try { localStorage.setItem(themePreferenceKey, preference); } catch (error) {}
    }
    window.dispatchEvent(new CustomEvent('sjmaths:themechange', {
      detail: { preference, theme: isDark ? 'dark' : 'light', isDark }
    }));
    window.dispatchEvent(new CustomEvent('themeChanged', { detail: { isDark } }));
  };
  let themePreference = 'system';
  if (window.SJMathsTheme) {
    themePreference = window.SJMathsTheme.getPreference();
    updateThemeToggle(isDarkPreference(themePreference));
    window.addEventListener('sjmaths:themechange', event => updateThemeToggle(event.detail?.theme === 'dark'));
    window.addEventListener('themeChanged', event => updateThemeToggle(Boolean(event.detail?.isDark)));
  } else {
    try {
      const saved = localStorage.getItem(themePreferenceKey);
      if (['system', 'light', 'dark'].includes(saved)) themePreference = saved;
      else {
        const legacy = [
          ['sjmaths-dark', { on: 'dark', off: 'light' }],
          ['sjmaths_theme', { dark: 'dark', light: 'light' }],
          ['sj_theme', { dark: 'dark', light: 'light' }],
          ['theme', { dark: 'dark', light: 'light' }],
          ['sjmaths-test-dark', { true: 'dark', false: 'light' }],
          ['sjmaths-theme', { dark: 'dark', light: 'light' }]
        ];
        for (const [key, values] of legacy) {
          const migrated = values[localStorage.getItem(key)];
          if (!migrated) continue;
          themePreference = migrated;
          localStorage.setItem(themePreferenceKey, migrated);
          break;
        }
      }
    } catch (error) {}
    applyLocalTheme(themePreference, false);
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener?.('change', () => {
      if (themePreference === 'system') applyLocalTheme('system', false);
    });
    window.addEventListener('storage', event => {
      if (event.key === themePreferenceKey) {
        applyLocalTheme(['system', 'light', 'dark'].includes(event.newValue) ? event.newValue : 'system', false);
      }
    });
  }
  if (btnTheme) {
    btnTheme.addEventListener('click', event => {
      event.preventDefault();
      const next = isDarkPreference(themePreference) ? 'light' : 'dark';
      if (window.SJMathsTheme) window.SJMathsTheme.setPreference(next);
      else applyLocalTheme(next);
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
      const stickyWrap = document.querySelector('.study-tabs-sticky-wrapper');
      if (stickyWrap) {
        const topOffset = stickyWrap.getBoundingClientRect().top + window.scrollY - 20;
        window.scrollTo({ top: topOffset, behavior: 'smooth' });
      }
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
      if (!card) return;
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
        const scoreEl = document.getElementById('quizScore');
        if (scoreEl) scoreEl.textContent = quizScore;
        if (feedback) {
          const ind = feedback.querySelector('.feedback-indicator');
          if (ind) ind.textContent = '✓ Correct Answer!';
          feedback.classList.add('correct');
        }
      } else {
        if (feedback) {
          const ind = feedback.querySelector('.feedback-indicator');
          if (ind) ind.textContent = '✗ Incorrect. Correct Option: ' + letters[correctIndex];
          feedback.classList.add('incorrect');
        }
      }
      if (feedback) feedback.classList.remove('hidden');
    });
  });

  const btnResetQuiz = document.getElementById('btnResetQuiz');
  if (btnResetQuiz) {
    btnResetQuiz.addEventListener('click', () => {
      quizScore = 0;
      answeredQuestions.clear();
      const scoreEl = document.getElementById('quizScore');
      if (scoreEl) scoreEl.textContent = '0';
      document.querySelectorAll('.quiz-option-btn').forEach(b => {
        b.disabled = false;
        b.classList.remove('correct', 'incorrect');
      });
      document.querySelectorAll('.q-feedback').forEach(f => {
        f.classList.add('hidden');
        f.classList.remove('correct', 'incorrect');
        const ind = f.querySelector('.feedback-indicator');
        if (ind) ind.textContent = '';
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
  let testSubmitted = false;

  if (btnStartTest) {
    btnStartTest.addEventListener('click', () => {
      if (testTimer) {
        clearInterval(testTimer);
        testTimer = null;
      }
      btnStartTest.disabled = true;
      if (testStartWrap) testStartWrap.classList.add('hidden');
      if (testActiveWrap) testActiveWrap.classList.remove('hidden');
      testTimer = setInterval(() => {
        secondsLeft--;
        const mins = Math.floor(secondsLeft / 60);
        const secs = secondsLeft % 60;
        if (timerDisplay) {
          timerDisplay.textContent = (mins < 10 ? '0' : '') + mins + ':' + (secs < 10 ? '0' : '') + secs;
        }
        if (secondsLeft <= 0) {
          clearInterval(testTimer);
          testTimer = null;
          submitTest();
        }
      }, 1000);
    });
  }

  const selectedTestAnswers = {};
  document.querySelectorAll('.test-option-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      if (testSubmitted) return;
      const tIndex = parseInt(btn.getAttribute('data-tindex'), 10);
      const optIndex = parseInt(btn.getAttribute('data-optindex'), 10);
      selectedTestAnswers[tIndex] = optIndex;
      const card = document.getElementById('t-card-' + tIndex);
      if (card) {
        card.querySelectorAll('.test-option-btn').forEach(b => b.classList.remove('selected'));
      }
      btn.classList.add('selected');
    });
  });

  function submitTest() {
    if (testSubmitted) return;
    testSubmitted = true;
    if (testTimer) {
      clearInterval(testTimer);
      testTimer = null;
    }
    const btnSub = document.getElementById('btnSubmitTest');
    if (btnSub) {
      btnSub.disabled = true;
      btnSub.classList.add('hidden');
    }
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
      if (feedback) feedback.classList.remove('hidden');
    });
    const resScore = document.getElementById('resFinalScore');
    if (resScore) resScore.textContent = score;
    const resModal = document.getElementById('testResultModal');
    if (resModal) resModal.classList.remove('hidden');
  }

  const btnSubmitTest = document.getElementById('btnSubmitTest');
  if (btnSubmitTest) btnSubmitTest.addEventListener('click', submitTest);

  const resModal = document.getElementById('testResultModal');
  if (resModal) {
    const card = resModal.querySelector('.result-card');
    const retakeBtn = resModal.querySelector('#btnRetakeTest');
    if (card && retakeBtn && !resModal.querySelector('.btn-review-solutions')) {
      const reviewBtn = document.createElement('button');
      reviewBtn.type = 'button';
      reviewBtn.className = 'btn-review-solutions';
      reviewBtn.textContent = 'Review Solutions ↓';
      reviewBtn.setAttribute('data-dismiss', 'modal');
      reviewBtn.style.cssText = 'margin-right:10px;padding:10px 20px;border-radius:9999px;font-weight:800;cursor:pointer;background:var(--paper-card,#f8fafc);border:1.5px solid var(--line,#cbd5e1);color:var(--ink,#1e293b);';
      retakeBtn.parentNode.insertBefore(reviewBtn, retakeBtn);
      reviewBtn.addEventListener('click', () => {
        resModal.classList.add('hidden');
      });
    }

    // Backdrop click closes modal to allow reviewing solutions below
    resModal.addEventListener('click', event => {
      if (event.target === resModal) {
        resModal.classList.add('hidden');
      }
    });
    // Escape key closes modal
    document.addEventListener('keydown', event => {
      if (event.key === 'Escape' && !resModal.classList.contains('hidden')) {
        resModal.classList.add('hidden');
      }
    });
    const closeBtn = resModal.querySelector('.btn-close-modal, .btn-review-solutions, [data-dismiss="modal"]');
    if (closeBtn) {
      closeBtn.addEventListener('click', () => {
        resModal.classList.add('hidden');
      });
    }
  }

  const btnRetakeTest = document.getElementById('btnRetakeTest');
  if (btnRetakeTest) {
    btnRetakeTest.addEventListener('click', () => {
      location.reload();
    });
  }
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initAgricultureGenerated);
} else {
  initAgricultureGenerated();
}
