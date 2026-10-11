/**
 * SJMaths - IB DP Mathematics Interactive Study Tabs & Mini-Test Engine
 * Universal controller supporting all 30 IB DP AA SL lesson guides.
 */
(function () {
  'use strict';

  function initStudyTabs() {
    const tabNav = document.querySelector('.study-tabs-nav');
    if (!tabNav) return;

    const tabBtns = Array.from(tabNav.querySelectorAll('.study-tab-btn'));
    const tabPanels = Array.from(document.querySelectorAll('.study-tab-panel, .study-tab-pane'));

    function getBtnTarget(btn) {
      return btn.getAttribute('data-tab') || btn.getAttribute('data-target') || '';
    }

    function activateTab(tabId, updateHash) {
      if (!tabId) return;

      tabBtns.forEach(btn => {
        const isTarget = getBtnTarget(btn) === tabId;
        btn.classList.toggle('active', isTarget);
        btn.setAttribute('aria-selected', isTarget ? 'true' : 'false');
      });

      tabPanels.forEach(panel => {
        const isTarget = panel.id === tabId;
        panel.classList.toggle('active', isTarget);
        if (isTarget && window.renderMathInElement) {
          try {
            renderMathInElement(panel, {
              delimiters: [
                { left: '$$', right: '$$', display: true },
                { left: '$', right: '$', display: false },
                { left: '\\(', right: '\\)', display: false },
                { left: '\\[', right: '\\]', display: true }
              ],
              throwOnError: false
            });
          } catch (e) {}
        }
      });

      if (updateHash && history.replaceState) {
        const cleanHash = tabId.replace(/^tab-/, '').replace(/^pane-/, '');
        history.replaceState(null, '', '#' + cleanHash);
      }
    }

    tabBtns.forEach(btn => {
      btn.addEventListener('click', function () {
        const tabId = getBtnTarget(this);
        if (tabId) activateTab(tabId, true);
      });
    });

    // Support in-page anchor links pointing to tabs
    document.querySelectorAll('a[href^="#tab-"], a[href^="#pane-"]').forEach(link => {
      link.addEventListener('click', function (e) {
        const targetId = this.getAttribute('href').slice(1);
        const matchingBtn = tabBtns.find(b => getBtnTarget(b) === targetId);
        if (matchingBtn) {
          e.preventDefault();
          activateTab(targetId, true);
          const panel = document.getElementById(targetId);
          if (panel) {
            panel.scrollIntoView({ behavior: 'smooth', block: 'start' });
          }
        }
      });
    });

    // Check URL hash on load
    const hash = window.location.hash.replace('#', '');
    if (hash) {
      let targetId = hash;
      let matchingBtn = tabBtns.find(b => getBtnTarget(b) === targetId);
      if (!matchingBtn) {
        targetId = 'tab-' + hash;
        matchingBtn = tabBtns.find(b => getBtnTarget(b) === targetId);
      }
      if (!matchingBtn) {
        targetId = 'pane-' + hash;
        matchingBtn = tabBtns.find(b => getBtnTarget(b) === targetId);
      }
      if (matchingBtn) {
        activateTab(targetId, false);
      }
    }
  }

  function initMiniQuiz() {
    // -------------------------------------------------------------
    // Format 1: Calculus Style (.quiz-card & .quiz-opt-btn)
    // -------------------------------------------------------------
    const quizWrap = document.querySelector('.quiz-container');
    const calcQuestions = quizWrap ? Array.from(quizWrap.querySelectorAll('.quiz-card')) : [];
    if (calcQuestions.length > 0) {
      const scoreDisplay = document.getElementById('quiz-score-val') || document.getElementById('quiz-score');
      const totalDisplay = document.getElementById('quiz-total-val') || document.getElementById('quiz-total');
      const resetBtn = document.getElementById('quiz-reset-btn');
      let correctCount = 0;

      if (totalDisplay) totalDisplay.textContent = calcQuestions.length;

      calcQuestions.forEach(card => {
        const cardCorrect = (card.getAttribute('data-correct') || '').trim().toUpperCase();
        const options = Array.from(card.querySelectorAll('.quiz-opt-btn, .quiz-option-btn'));
        const feedback = card.querySelector('.quiz-feedback');
        const explanation = card.querySelector('.quiz-explanation, .feedback-exp');

        function getBtnLetter(btn) {
          const direct = btn.getAttribute('data-choice') || btn.getAttribute('data-opt') || btn.getAttribute('data-option');
          if (direct) return direct.trim().toUpperCase();
          const txt = (btn.textContent || '').trim();
          const match = txt.match(/^([A-D])[\.\)\:\s]/i);
          return match ? match[1].toUpperCase() : '';
        }

        function checkCorrect(btn) {
          if (btn.getAttribute('data-correct') === 'true') return true;
          if (cardCorrect && getBtnLetter(btn) === cardCorrect) return true;
          return false;
        }

        options.forEach(opt => {
          opt.addEventListener('click', function () {
            if (card.dataset.answered === 'true') return;
            card.dataset.answered = 'true';

            const isCorrect = checkCorrect(this);

            options.forEach(o => {
              o.disabled = true;
              if (checkCorrect(o)) {
                o.classList.add('correct');
              }
            });

            if (isCorrect) {
              this.classList.add('correct');
              correctCount++;
              if (feedback) {
                feedback.removeAttribute('hidden');
                feedback.classList.remove('wrong', 'incorrect');
                feedback.classList.add('correct', 'show');
                feedback.style.display = 'block';
                const msg = feedback.querySelector('.feedback-msg');
                if (msg) msg.textContent = '✓ Correct!';
              }
            } else {
              this.classList.add('wrong');
              if (feedback) {
                feedback.removeAttribute('hidden');
                feedback.classList.remove('correct');
                feedback.classList.add('wrong', 'incorrect', 'show');
                feedback.style.display = 'block';
                const msg = feedback.querySelector('.feedback-msg');
                if (msg) msg.textContent = `✗ Incorrect. Correct answer is option ${cardCorrect || 'marked above'}.`;
              }
            }

            if (explanation) {
              explanation.removeAttribute('hidden');
              explanation.style.display = 'block';
            }

            if (window.renderMathInElement) {
              try {
                renderMathInElement(card, {
                  delimiters: [
                    { left: '$$', right: '$$', display: true },
                    { left: '$', right: '$', display: false },
                    { left: '\\(', right: '\\)', display: false },
                    { left: '\\[', right: '\\]', display: true }
                  ],
                  throwOnError: false
                });
              } catch(e) {}
            }

            if (scoreDisplay) scoreDisplay.textContent = correctCount;
          });
        });
      });

      if (resetBtn) {
        resetBtn.addEventListener('click', function () {
          correctCount = 0;
          if (scoreDisplay) scoreDisplay.textContent = '0';
          calcQuestions.forEach(card => {
            delete card.dataset.answered;
            const options = Array.from(card.querySelectorAll('.quiz-opt-btn, .quiz-option-btn'));
            const feedback = card.querySelector('.quiz-feedback');
            const explanation = card.querySelector('.quiz-explanation, .feedback-exp');
            options.forEach(opt => {
              opt.disabled = false;
              opt.classList.remove('correct', 'wrong', 'incorrect');
            });
            if (feedback) {
              feedback.classList.remove('correct', 'wrong', 'incorrect', 'show');
              feedback.style.display = 'none';
            }
            if (explanation && card.querySelector('.quiz-explanation')) {
              explanation.style.display = 'none';
            }
          });
        });
      }
    }

    // -------------------------------------------------------------
    // Format 2: Number & Algebra Style (.quiz-question & .quiz-option-btn)
    // -------------------------------------------------------------
    const naQuestions = Array.from(document.querySelectorAll('.quiz-question'));
    if (naQuestions.length > 0) {
      const naScoreDisplay = document.getElementById('quiz-score');
      let naCorrect = 0;

      naQuestions.forEach((card, idx) => {
        const correctVal = (card.getAttribute('data-correct') || '').trim().toUpperCase();
        const options = Array.from(card.querySelectorAll('.quiz-option-btn'));
        const feedback = card.querySelector('.quiz-feedback') || document.getElementById('fb-' + (idx + 1));

        options.forEach(opt => {
          opt.addEventListener('click', function () {
            if (card.dataset.answered === 'true') return;
            card.dataset.answered = 'true';

            const chosen = (this.getAttribute('data-option') || '').trim().toUpperCase();
            const isCorrect = chosen === correctVal;

            options.forEach(o => {
              o.disabled = true;
              const val = (o.getAttribute('data-option') || '').trim().toUpperCase();
              if (val === correctVal) {
                o.classList.add('correct');
              }
            });

            if (isCorrect) {
              this.classList.add('correct');
              naCorrect++;
              if (feedback) {
                feedback.classList.remove('wrong', 'incorrect');
                feedback.classList.add('correct', 'show');
                feedback.style.display = 'block';
              }
            } else {
              this.classList.add('wrong', 'incorrect');
              if (feedback) {
                feedback.classList.remove('correct');
                feedback.classList.add('wrong', 'show');
                feedback.style.display = 'block';
              }
            }

            if (naScoreDisplay) naScoreDisplay.textContent = naCorrect;
          });
        });
      });
    }

    // -------------------------------------------------------------
    // Format 3: Statistics & Probability Style (.mcq-card & .mcq-option)
    // -------------------------------------------------------------
    const mcqCards = Array.from(document.querySelectorAll('.mcq-card'));
    // Only apply if not already managed by radio-based inline scripts
    const unhandledMcqCards = mcqCards.filter(card => !card.querySelector('input[type="radio"]') && !card.dataset.handled);
    if (unhandledMcqCards.length > 0) {
      const mcqScoreDisplay = document.getElementById('mcq-score');
      const scoreBanner = document.getElementById('test-score-display');
      let mcqCorrect = 0;

      unhandledMcqCards.forEach(card => {
        card.dataset.handled = 'true';
        const correctChoice = (card.getAttribute('data-correct') || '').trim().toLowerCase();
        const options = Array.from(card.querySelectorAll('.mcq-option'));
        const feedback = card.querySelector('.mcq-feedback');

        options.forEach(opt => {
          opt.addEventListener('click', function () {
            if (card.dataset.answered === 'true') return;
            card.dataset.answered = 'true';

            const chosen = (this.getAttribute('data-choice') || '').trim().toLowerCase();
            const isCorrect = chosen === correctChoice;

            options.forEach(o => {
              o.disabled = true;
              const choice = (o.getAttribute('data-choice') || '').trim().toLowerCase();
              if (choice === correctChoice) {
                o.classList.add('correct');
              }
            });

            if (isCorrect) {
              this.classList.add('correct');
              mcqCorrect++;
              if (feedback) {
                feedback.classList.remove('wrong');
                feedback.classList.add('correct');
                feedback.innerHTML = '<i class="fa-solid fa-circle-check"></i> <strong>Correct!</strong> Well reasoned.';
                feedback.style.display = 'block';
              }
            } else {
              this.classList.add('wrong');
              if (feedback) {
                feedback.classList.remove('correct');
                feedback.classList.add('wrong');
                feedback.innerHTML = `<i class="fa-solid fa-circle-xmark"></i> <strong>Incorrect.</strong> The correct answer is Option ${correctChoice.toUpperCase()}.`;
                feedback.style.display = 'block';
              }
            }

            if (mcqScoreDisplay) mcqScoreDisplay.textContent = mcqCorrect;
            if (scoreBanner) scoreBanner.style.display = 'block';
          });
        });
      });
    }
  }

  document.addEventListener('DOMContentLoaded', function () {
    initStudyTabs();
    initMiniQuiz();
  });

  if (document.readyState === 'interactive' || document.readyState === 'complete') {
    initStudyTabs();
    initMiniQuiz();
  }
})();
