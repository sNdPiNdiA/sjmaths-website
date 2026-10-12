/**
 * SJMaths - IB DP Mathematics Interactive Study Tabs & Mini-Test Engine
 * Universal controller supporting all 30 IB DP AA SL lesson guides.
 */
(function () {
  'use strict';

  function initStudyTabs() {
    const tabNav = document.querySelector('.study-tabs-nav');
    if (!tabNav) return;
    if (tabNav.dataset.ibTabsInitialized === 'true') return;
    tabNav.dataset.ibTabsInitialized = 'true';

    const tabBtns = Array.from(tabNav.querySelectorAll('.study-tab-btn'));
    const tabPanels = Array.from(document.querySelectorAll('.study-tab-panel, .study-tab-pane'));

    // Some older IB pages omit tab roles and leave aria-labelledby pointing at
    // button IDs that were never added. Complete the relationships at runtime
    // while keeping each page's existing IDs and visible labels intact.
    tabNav.setAttribute('role', 'tablist');
    tabNav.setAttribute('aria-orientation', 'horizontal');

    tabBtns.forEach(btn => {
      const tabId = btn.getAttribute('data-tab') || btn.getAttribute('data-target') || '';
      const panel = tabId ? document.getElementById(tabId) : null;
      if (!btn.id) {
        const expectedIds = (panel?.getAttribute('aria-labelledby') || '').split(/\s+/).filter(Boolean);
        const missingExpectedId = expectedIds.find(id => !document.getElementById(id));
        btn.id = missingExpectedId || (tabId ? `${tabId}-btn` : `ib-study-tab-${tabBtns.indexOf(btn) + 1}`);
      }
      btn.setAttribute('role', 'tab');
      if (panel) {
        btn.setAttribute('aria-controls', panel.id);
        panel.setAttribute('role', 'tabpanel');
        panel.setAttribute('aria-labelledby', btn.id);
        if (!panel.hasAttribute('tabindex')) panel.setAttribute('tabindex', '0');
      }
    });

    const initialBtn = tabBtns.find(btn => btn.classList.contains('active') || btn.getAttribute('aria-selected') === 'true') || tabBtns[0];
    if (initialBtn) {
      tabBtns.forEach(btn => {
        const selected = btn === initialBtn;
        btn.setAttribute('aria-selected', selected ? 'true' : 'false');
        btn.tabIndex = selected ? 0 : -1;
      });
    }

    function getBtnTarget(btn) {
      return btn.getAttribute('data-tab') || btn.getAttribute('data-target') || '';
    }

    function activateTab(tabId, updateHash) {
      if (!tabId) return;

      tabBtns.forEach(btn => {
        const isTarget = getBtnTarget(btn) === tabId;
        btn.classList.toggle('active', isTarget);
        btn.setAttribute('aria-selected', isTarget ? 'true' : 'false');
        btn.tabIndex = isTarget ? 0 : -1;
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

    tabNav.addEventListener('keydown', event => {
      const currentIndex = tabBtns.indexOf(event.target.closest('.study-tab-btn'));
      if (currentIndex < 0) return;

      let nextIndex = currentIndex;
      if (event.key === 'ArrowRight') nextIndex = (currentIndex + 1) % tabBtns.length;
      else if (event.key === 'ArrowLeft') nextIndex = (currentIndex - 1 + tabBtns.length) % tabBtns.length;
      else if (event.key === 'Home') nextIndex = 0;
      else if (event.key === 'End') nextIndex = tabBtns.length - 1;
      else return;

      event.preventDefault();
      const nextBtn = tabBtns[nextIndex];
      nextBtn.focus();
      const tabId = getBtnTarget(nextBtn);
      if (tabId) activateTab(tabId, true);
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

    // Submit-style radio quizzes used by the AA HL topic guides.
    const submitQuizButton = document.getElementById('btn-submit-quiz');
    const answerKeyNode = document.getElementById('ib-quiz-answer-key');
    const answerKey = new Map();
    if (answerKeyNode) {
      try {
        JSON.parse(answerKeyNode.textContent || '[]').forEach(item => {
          if (item && item.id != null) answerKey.set(String(item.id), item);
        });
      } catch (error) {
        console.error('Unable to read the IB mini-test answer key.', error);
      }
    }

    const submitQuizCards = Array.from(document.querySelectorAll('#tab-test .quiz-card, #tab-test .quiz-question-card'))
      .filter(card => card.querySelector('input[type="radio"]') && (answerKey.has(card.id) || card.hasAttribute('data-correct')));

    if (submitQuizButton && submitQuizCards.length > 0) {
      const scoreDisplay = document.getElementById('quiz-score-display');
      if (scoreDisplay) scoreDisplay.setAttribute('aria-live', 'polite');

      submitQuizCards.forEach(card => {
        const prompt = card.querySelector('.quiz-question, .quiz-stem');
        const optionsGroup = card.querySelector('.quiz-options, .quiz-options-group');
        if (prompt && optionsGroup) {
          if (!prompt.id) prompt.id = `${card.id}-prompt`;
          optionsGroup.setAttribute('role', 'radiogroup');
          optionsGroup.setAttribute('aria-labelledby', prompt.id);
        }
        card.querySelectorAll('.quiz-option, .quiz-option-label').forEach(label => label.classList.add('quiz-opt-btn'));
      });

      submitQuizButton.addEventListener('click', function () {
        if (submitQuizButton.disabled) return;

        let score = 0;
        submitQuizCards.forEach(card => {
          const key = answerKey.get(card.id);
          const rawCorrect = key ? key.correct : card.getAttribute('data-correct');
          const correctIndex = Number(rawCorrect);
          if (!Number.isInteger(correctIndex)) return;

          const radios = Array.from(card.querySelectorAll('input[type="radio"]'));
          const selected = radios.find(radio => radio.checked) || null;
          const selectedIndex = selected ? Number(selected.value) : -1;
          const isCorrect = selectedIndex === correctIndex;
          if (isCorrect) score++;

          card.querySelectorAll('.quiz-option, .quiz-option-label').forEach(label => {
            const radio = label.querySelector('input[type="radio"]');
            const optionIndex = Number(radio?.value ?? label.getAttribute('data-option'));
            label.classList.toggle('correct', optionIndex === correctIndex);
            label.classList.toggle('wrong', selectedIndex === optionIndex && !isCorrect);
          });
          radios.forEach(radio => { radio.disabled = true; });

          const feedback = card.querySelector('.quiz-feedback, .quiz-feedback-box');
          if (!feedback) return;

          const answerLetter = String.fromCharCode(65 + correctIndex);
          const resultText = selected
            ? (isCorrect ? 'Correct. ' : `Incorrect. Correct answer: ${answerLetter}. `)
            : `Choose an answer. Correct answer: ${answerLetter}. `;
          const specialFeedback = feedback.querySelector('.option-feedback[data-opt]');

          if (specialFeedback) {
            let result = feedback.querySelector('.quiz-result');
            if (!selected) {
              if (!result) {
                result = document.createElement('p');
                result.className = 'quiz-result';
                feedback.prepend(result);
              }
              result.textContent = `No answer selected. Correct answer: ${answerLetter}.`;
            } else if (result) {
              result.remove();
            }
            const selectedFeedbackIndex = selected ? selectedIndex : correctIndex;
            feedback.querySelectorAll('.option-feedback[data-opt]').forEach(item => {
              item.style.display = Number(item.getAttribute('data-opt')) === selectedFeedbackIndex ? 'block' : 'none';
            });
          } else {
            const explanation = key?.explanation || '';
            feedback.textContent = resultText + explanation;
          }

          feedback.classList.add('show', isCorrect ? 'correct' : 'wrong');
          feedback.setAttribute('role', 'status');
          feedback.setAttribute('aria-live', 'polite');
          feedback.style.display = 'block';
          if (window.renderMathInElement) {
            try {
              renderMathInElement(feedback, {
                delimiters: [
                  { left: '$$', right: '$$', display: true },
                  { left: '$', right: '$', display: false },
                  { left: '\\(', right: '\\)', display: false },
                  { left: '\\[', right: '\\]', display: true }
                ],
                throwOnError: false
              });
            } catch (error) {}
          }
        });

        if (scoreDisplay) {
          scoreDisplay.textContent = `Score: ${score} / ${submitQuizCards.length}`;
          scoreDisplay.style.display = 'block';
          scoreDisplay.setAttribute('role', 'status');
        }
        submitQuizButton.disabled = true;
      });
    }
  }

  let initialized = false;
  function initialize() {
    if (initialized) return;
    initialized = true;
    initStudyTabs();
    initMiniQuiz();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initialize, { once: true });
  } else {
    initialize();
  }
})();
