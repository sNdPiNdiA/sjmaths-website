/**
 * ============================================================================
 * SSC CGL Topic Pages — Unified Interactive Logic (UPSSSC PET Architecture)
 * Replaces duplicated inline scripts across all 320+ topic pages.
 * ============================================================================
 */

(function () {
  'use strict';

  function triggerMathTypeset(target) {
    if (window.MathJax && typeof window.MathJax.typesetPromise === 'function') {
      try {
        const elements = target ? (Array.isArray(target) ? target : [target]) : undefined;
        window.MathJax.typesetPromise(elements).catch(function () {});
      } catch (e) {}
    }
  }

  // 1. 4-Tab Main Switcher
  window.openTab = function (evt, tabName) {
    if (evt && evt.preventDefault) evt.preventDefault();
    const tabPanels = document.querySelectorAll('.tab-panel');
    const tabBtns = document.querySelectorAll('.main-tabs-nav .tab-btn');

    tabPanels.forEach(p => p.classList.remove('active'));
    tabBtns.forEach(b => b.classList.remove('active'));

    const activePanel = document.getElementById(tabName);
    if (activePanel) {
      activePanel.classList.add('active');
      triggerMathTypeset(activePanel);
    }

    const activeBtn = (evt && evt.currentTarget) || document.querySelector(`.main-tabs-nav .tab-btn[onclick*="${tabName}"]`);
    if (activeBtn) activeBtn.classList.add('active');

    // Smooth scroll to tabs if below viewport
    const tabsNav = document.querySelector('.main-tabs-nav');
    if (tabsNav && window.scrollY > tabsNav.offsetTop) {
      tabsNav.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  };

  // 2. Tab 2: Practice Questions Subtab Switcher
  window.openPracticeSubTab = function (evt, subTabId) {
    if (evt && evt.preventDefault) evt.preventDefault();
    document.querySelectorAll('.practice-subtab-panel').forEach(p => p.classList.remove('active'));
    document.querySelectorAll('.practice-subtabs-nav .practice-subtab-btn').forEach(b => b.classList.remove('active'));

    const panel = document.getElementById(subTabId);
    if (panel) {
      panel.classList.add('active');
      triggerMathTypeset(panel);
    }

    const btn = (evt && evt.currentTarget) || document.querySelector(`.practice-subtabs-nav .practice-subtab-btn[onclick*="${subTabId}"]`);
    if (btn) btn.classList.add('active');
  };

  // 3. Tab 2: Practice Option Evaluator
  window.checkPracticeOption = function (btn, chosenOpt, correctOpt, solBoxId) {
    const parent = btn.closest('.q-options');
    if (!parent || parent.dataset.evaluated === 'true') return;
    parent.dataset.evaluated = 'true';

    const allBtns = parent.querySelectorAll('.q-opt-btn');
    allBtns.forEach(b => {
      b.disabled = true;
      const optMatch = b.getAttribute('onclick') && b.getAttribute('onclick').match(/checkPracticeOption\s*\(\s*this\s*,\s*['"]([A-D])['"]/);
      const letter = optMatch ? optMatch[1] : '';
      if (letter === correctOpt) {
        b.classList.add('correct-choice');
      } else if (b === btn && chosenOpt !== correctOpt) {
        b.classList.add('wrong-choice');
      }
    });

    const solBox = document.getElementById(solBoxId);
    if (solBox) {
      solBox.style.display = 'block';
      triggerMathTypeset(solBox);
    }
  };

  // 4. Difficulty Switcher (Used in some practice modules)
  window.switchDiff = function (diff, btn) {
    document.querySelectorAll('.difficulty-section').forEach(s => s.style.display = 'none');
    document.querySelectorAll('.diff-btn').forEach(b => b.classList.remove('active'));
    const target = document.getElementById('diff-' + diff);
    if (target) target.style.display = 'block';
    if (btn) btn.classList.add('active');
  };

  // 5. Tab 4: Timed Mini Test Engine
  window.testEngine = {
    questions: [],
    currentIndex: 0,
    answers: {},
    timerSeconds: 900,
    timerInterval: null,
    correctMarks: 3,
    negativeMarks: 1,
    isSubmitted: false
  };

  window.initMiniTestData = function () {
    const raw = document.getElementById('mini-test-data');
    if (raw) {
      try {
        window.testEngine.questions = JSON.parse(raw.textContent);
      } catch (e) {
        console.warn('Mini-test JSON parse error:', e);
        window.testEngine.questions = [];
      }
    }
  };

  window.startMiniTestEngine = function () {
    window.initMiniTestData();
    if (!window.testEngine.questions || window.testEngine.questions.length === 0) return;

    const intro = document.getElementById('test-intro-screen');
    const active = document.getElementById('test-active-screen');
    const results = document.getElementById('test-results-screen');

    if (intro) intro.style.display = 'none';
    if (active) active.style.display = 'block';
    if (results) results.style.display = 'none';

    window.testEngine.currentIndex = 0;
    window.testEngine.answers = {};
    window.testEngine.isSubmitted = false;
    window.testEngine.timerSeconds = 900;

    window.renderTestPalette();
    window.renderActiveQuestion();
    window.startTestTimer();
  };

  window.startTestTimer = function () {
    clearInterval(window.testEngine.timerInterval);
    window.testEngine.timerInterval = setInterval(() => {
      if (window.testEngine.timerSeconds <= 0) {
        clearInterval(window.testEngine.timerInterval);
        window.submitMiniTestEngine();
        return;
      }
      window.testEngine.timerSeconds--;
      const mins = Math.floor(window.testEngine.timerSeconds / 60);
      const secs = window.testEngine.timerSeconds % 60;
      const disp = (mins < 10 ? '0' : '') + mins + ':' + (secs < 10 ? '0' : '') + secs;
      const el = document.getElementById('test-timer-display');
      if (el) el.textContent = disp;
    }, 1000);
  };

  window.renderTestPalette = function () {
    const strip = document.getElementById('test-palette-strip');
    if (!strip) return;
    strip.innerHTML = '';
    for (let i = 0; i < window.testEngine.questions.length; i++) {
      const b = document.createElement('button');
      b.type = 'button';
      b.className = 'palette-btn' + (i === window.testEngine.currentIndex ? ' current' : '') + (window.testEngine.answers[i] ? ' answered' : '');
      b.textContent = i + 1;
      b.onclick = (function (idx) {
        return function () {
          window.testEngine.currentIndex = idx;
          window.renderTestPalette();
          window.renderActiveQuestion();
        };
      })(i);
      strip.appendChild(b);
    }
  };

  window.navigateTestQuestion = function (delta) {
    const newIdx = window.testEngine.currentIndex + delta;
    if (newIdx >= 0 && newIdx < window.testEngine.questions.length) {
      window.testEngine.currentIndex = newIdx;
      window.renderTestPalette();
      window.renderActiveQuestion();
    }
  };

  window.renderActiveQuestion = function () {
    const q = window.testEngine.questions[window.testEngine.currentIndex];
    if (!q) return;

    const curEl = document.getElementById('cur-q-num');
    if (curEl) curEl.textContent = window.testEngine.currentIndex + 1;

    const prevBtn = document.getElementById('btn-prev-q');
    const nextBtn = document.getElementById('btn-next-q');
    if (prevBtn) prevBtn.disabled = window.testEngine.currentIndex === 0;
    if (nextBtn) nextBtn.disabled = window.testEngine.currentIndex === window.testEngine.questions.length - 1;

    const wrapper = document.getElementById('active-question-wrapper');
    if (!wrapper) return;

    const chosen = window.testEngine.answers[window.testEngine.currentIndex];

    let html = '<div class="q-header">' +
      '<span class="q-badge"><span class="lang-en">Question ' + (window.testEngine.currentIndex + 1) + '</span><span class="lang-hi">प्रश्न ' + (window.testEngine.currentIndex + 1) + '</span></span>' +
      '</div>' +
      '<div class="q-text">' +
      '<p class="lang-en">' + (q.question.en || '') + '</p>' +
      '<p class="lang-hi">' + (q.question.hi || '') + '</p>' +
      '</div>' +
      '<div class="q-options">';

    (q.options || []).forEach(opt => {
      const isSelected = chosen === opt.letter;
      html += '<button type="button" class="q-opt-btn' + (isSelected ? ' selected-test-opt' : '') + '" onclick="selectTestAnswer(\'' + opt.letter + '\')">' +
        '<span class="opt-letter">' + opt.letter + '</span>' +
        '<span class="opt-content">' +
        '<span class="lang-en">' + (opt.text.en || '') + '</span>' +
        '<span class="lang-hi">' + (opt.text.hi || '') + '</span>' +
        '</span>' +
        '</button>';
    });

    html += '</div>';
    wrapper.innerHTML = html;
    triggerMathTypeset(wrapper);
  };

  window.selectTestAnswer = function (letter) {
    window.testEngine.answers[window.testEngine.currentIndex] = letter;
    window.renderTestPalette();
    window.renderActiveQuestion();
  };

  window.submitMiniTestEngine = function () {
    clearInterval(window.testEngine.timerInterval);
    window.testEngine.isSubmitted = true;

    const total = window.testEngine.questions.length;
    let correctCount = 0;
    let wrongCount = 0;
    let unattemptedCount = 0;

    for (let i = 0; i < total; i++) {
      const ans = window.testEngine.answers[i];
      const correct = window.testEngine.questions[i].correctAnswer;
      if (!ans) {
        unattemptedCount++;
      } else if (ans === correct) {
        correctCount++;
      } else {
        wrongCount++;
      }
    }

    const score = Math.max(0, (correctCount * window.testEngine.correctMarks) - (wrongCount * window.testEngine.negativeMarks));
    const attempted = correctCount + wrongCount;
    const accuracy = attempted > 0 ? Math.round((correctCount / attempted) * 100) : 0;

    const activeScreen = document.getElementById('test-active-screen');
    const resultsScreen = document.getElementById('test-results-screen');
    if (activeScreen) activeScreen.style.display = 'none';
    if (resultsScreen) resultsScreen.style.display = 'block';

    const scoreEl = document.getElementById('final-score-val');
    const accEl = document.getElementById('final-accuracy-val');
    const cEl = document.getElementById('count-correct');
    const wEl = document.getElementById('count-wrong');
    const uEl = document.getElementById('count-unattempted');

    if (scoreEl) scoreEl.textContent = score;
    if (accEl) accEl.textContent = accuracy + '%';
    if (cEl) cEl.textContent = correctCount;
    if (wEl) wEl.textContent = wrongCount;
    if (uEl) uEl.textContent = unattemptedCount;

    // Render Solutions List
    const solList = document.getElementById('test-solutions-list');
    if (solList) {
      solList.innerHTML = '';
      window.testEngine.questions.forEach((q, idx) => {
        const userAns = window.testEngine.answers[idx] || 'Not Attempted';
        const isRight = userAns === q.correctAnswer;
        const item = document.createElement('div');
        item.className = 'practice-q-card';
        item.innerHTML = '<div class="q-header">' +
          '<span class="q-badge">Q' + (idx + 1) + '</span>' +
          '<span class="q-difficulty ' + (isRight ? 'diff-easy' : 'diff-hard') + '">' + (isRight ? 'CORRECT' : (userAns === 'Not Attempted' ? 'UNATTEMPTED' : 'INCORRECT')) + '</span>' +
          '</div>' +
          '<div class="q-text"><p class="lang-en">' + (q.question.en || '') + '</p><p class="lang-hi">' + (q.question.hi || '') + '</p></div>' +
          '<div class="q-solution-box" style="display:block;">' +
          '<div class="sol-header"><strong><span class="lang-en">Correct: Option ' + q.correctAnswer + ' | Your Answer: ' + userAns + '</span><span class="lang-hi">सही: विकल्प ' + q.correctAnswer + ' | आपका उत्तर: ' + userAns + '</span></strong></div>' +
          '<div class="sol-explanation"><p class="lang-en">' + (q.explanation.en || '') + '</p><p class="lang-hi">' + (q.explanation.hi || '') + '</p></div>' +
          '</div>';
        solList.appendChild(item);
      });
      triggerMathTypeset(solList);
    }
  };

  window.retakeMiniTestEngine = function () {
    window.startMiniTestEngine();
  };

  // Re-typeset math whenever any details element is opened
  document.addEventListener('toggle', function (e) {
    if (e.target && e.target.open) {
      triggerMathTypeset(e.target);
    }
  }, true);

  // 6. Global DOM Initialization
  document.addEventListener('DOMContentLoaded', () => {
    // Initialize mini test data
    window.initMiniTestData();

    // Scroll active nav item into view
    setTimeout(() => {
      const activeItem = document.querySelector('.sub-nav-item.active');
      const navContainer = document.querySelector('.subject-nav');
      if (activeItem && navContainer) {
        const containerWidth = navContainer.offsetWidth;
        const itemOffset = activeItem.offsetLeft;
        const itemWidth = activeItem.offsetWidth;
        navContainer.scrollLeft = itemOffset - (containerWidth / 2) + (itemWidth / 2);
      }
    }, 100);

    // Handle checklist local storage
    const checkboxes = document.querySelectorAll('.checklist-checkbox');
    const storageKey = 'ssc-cgl-prep-checklist';
    const progress = JSON.parse(localStorage.getItem(storageKey)) || {};

    checkboxes.forEach(chk => {
      if (progress[chk.id]) chk.checked = true;
      chk.addEventListener('change', () => {
        progress[chk.id] = chk.checked;
        localStorage.setItem(storageKey, JSON.stringify(progress));
      });
      const parent = chk.closest('.checklist-item');
      if (parent) {
        parent.addEventListener('click', e => {
          if (e.target !== chk) {
            chk.checked = !chk.checked;
            chk.dispatchEvent(new Event('change'));
          }
        });
      }
    });
  });
})();
