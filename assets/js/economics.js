/**
 * ============================================================================
 * SJ Maths — Economics Interactive Engine
 * Handles:
 *  - 5-Tab Navigation Switching
 *  - Interactive Practice Quiz with instant feedback and score
 *  - Timed 10-minute Topic Test with timer countdown and result evaluation
 *  - Theme switching & persistence
 * ============================================================================
 */

document.addEventListener('DOMContentLoaded', () => {
  // Theme Toggle Support
  const themeToggleBtn = document.getElementById('theme-toggle-btn') || document.querySelector('.theme-toggle-btn');
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  const savedTheme = localStorage.getItem('sjmaths_theme') || localStorage.getItem('sj_theme');
  
  if (savedTheme === 'dark' || (!savedTheme && prefersDark)) {
    document.body.classList.add('dark-mode');
    document.documentElement.classList.add('dark');
    if (themeToggleBtn) themeToggleBtn.textContent = '☀️ Light';
  }

  if (themeToggleBtn) {
    themeToggleBtn.addEventListener('click', () => {
      const isDark = document.body.classList.toggle('dark-mode');
      document.documentElement.classList.toggle('dark', isDark);
      localStorage.setItem('sjmaths_theme', isDark ? 'dark' : 'light');
      localStorage.setItem('sj_theme', isDark ? 'dark' : 'light');
      themeToggleBtn.textContent = isDark ? '☀️ Light' : '🌙 Dark';
    });
  }

  // 5 Modular Tabs Switching
  const tabBtns = document.querySelectorAll('.tab-btn');
  const tabPanes = document.querySelectorAll('.tab-pane');

  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const targetId = btn.dataset.tab;
      tabBtns.forEach(b => {
        b.classList.remove('active');
        b.setAttribute('aria-selected', 'false');
      });
      tabPanes.forEach(p => {
        p.classList.remove('active');
      });

      btn.classList.add('active');
      btn.setAttribute('aria-selected', 'true');
      const targetPane = document.getElementById(targetId);
      if (targetPane) {
        targetPane.classList.add('active');
      }

      // Smooth scroll if tabs bar is scrolled out of view
      const tabsNav = document.querySelector('.tabs-nav');
      if (tabsNav && window.scrollY > tabsNav.offsetTop) {
        window.scrollTo({ top: tabsNav.offsetTop - 70, behavior: 'smooth' });
      }
    });
  });

  // Practice Quiz Logic
  document.querySelectorAll('.quiz-option-btn').forEach(opt => {
    opt.addEventListener('click', function() {
      const card = this.closest('.quiz-question-card');
      if (!card) return;
      
      const correctIdx = parseInt(card.dataset.correct, 10);
      const selectedIdx = parseInt(this.dataset.optindex, 10);
      const feedback = card.querySelector('.q-feedback');

      // Disable all options in this card once clicked
      card.querySelectorAll('.quiz-option-btn').forEach(b => {
        b.disabled = true;
        const bIdx = parseInt(b.dataset.optindex, 10);
        if (bIdx === correctIdx) b.classList.add('selected-correct');
      });

      if (selectedIdx !== correctIdx) {
        this.classList.add('selected-wrong');
      }
      if (feedback) {
        feedback.classList.remove('hidden');
      }
    });
  });

  // Timed Test Logic (10 Questions in 10 Minutes)
  let testTimerSec = 600;
  let testInterval = null;

  function startTimer() {
    if (testInterval) return;
    const timerElem = document.getElementById('test-timer');
    testInterval = setInterval(() => {
      testTimerSec--;
      const mins = Math.floor(testTimerSec / 60);
      const secs = testTimerSec % 60;
      if (timerElem) {
        timerElem.textContent = (mins < 10 ? '0' : '') + mins + ':' + (secs < 10 ? '0' : '') + secs;
      }
      if (testTimerSec <= 0) {
        clearInterval(testInterval);
        submitTest();
      }
    }, 1000);
  }

  document.querySelectorAll('.test-option-btn').forEach(btn => {
    btn.addEventListener('click', function() {
      const card = this.closest('.test-question-card');
      if (!card) return;
      card.querySelectorAll('.test-option-btn').forEach(b => b.style.borderColor = 'var(--border)');
      this.style.borderColor = 'var(--primary)';
      card.dataset.userchoice = this.dataset.optindex;
      startTimer();
    });
  });

  function submitTest() {
    if (testInterval) clearInterval(testInterval);
    let score = 0;
    const testCards = document.querySelectorAll('.test-question-card');
    const totalQuestions = testCards.length || 10;

    testCards.forEach((card, idx) => {
      const correct = parseInt(card.dataset.correct, 10);
      const choice = parseInt(card.dataset.userchoice, 10);
      if (choice === correct) score++;

      card.querySelectorAll('.test-option-btn').forEach(b => {
        b.disabled = true;
        const bIdx = parseInt(b.dataset.optindex, 10);
        if (bIdx === correct) b.classList.add('selected-correct');
        else if (bIdx === choice) b.classList.add('selected-wrong');
      });
      const feedback = document.getElementById('test-feedback-' + idx);
      if (feedback) feedback.classList.remove('hidden');
    });

    const scoreElem = document.getElementById('test-score-text');
    if (scoreElem) scoreElem.textContent = `${score} / ${totalQuestions}`;
    const scoreCard = document.getElementById('test-score-card');
    if (scoreCard) {
      scoreCard.classList.remove('hidden');
      scoreCard.scrollIntoView({ behavior: 'smooth' });
    }
    const finishBtn = document.getElementById('finish-test-btn');
    if (finishBtn) finishBtn.disabled = true;
  }

  const finishTestBtn = document.getElementById('finish-test-btn');
  if (finishTestBtn) {
    finishTestBtn.addEventListener('click', submitTest);
  }
});
