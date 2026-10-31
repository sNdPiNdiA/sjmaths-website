/**
 * UPPSC RO/ARO Topic Common Engine (ro-aro-topic.js)
 * Manages 5-tab switching, instant Practice PYQ evaluation, Mains word counter, and 3-level test engine
 */

(() => {
  'use strict';

  // --- 1. Right-Side Center Minimizable Tabs Dock System ---
  function initTabs() {
    const dock = document.getElementById('roTabsDock');
    const toggleBtn = document.getElementById('roDockToggle');
    const closeBtn = document.getElementById('roDockCloseBtn');
    const backdrop = document.getElementById('roDockBackdrop');
    const tabButtons = document.querySelectorAll('.ro-tab-btn, .ro-dock-btn');
    const tabPanels = document.querySelectorAll('.ro-tab-panel');

    function setMinimized(minimized) {
      if (!dock) return;
      dock.classList.toggle('minimized', minimized);
      document.body.classList.toggle('dock-open', !minimized);
      try {
        localStorage.setItem('ro_tabs_dock_minimized', minimized ? 'true' : 'false');
      } catch (e) {}
    }

    if (toggleBtn) {
      toggleBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        const isMin = dock.classList.contains('minimized');
        setMinimized(!isMin);
      });
    }

    if (closeBtn) {
      closeBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        setMinimized(true);
      });
    }

    if (backdrop) {
      backdrop.addEventListener('click', () => {
        setMinimized(true);
      });
    }

    // Close on Escape key
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && dock && !dock.classList.contains('minimized')) {
        setMinimized(true);
      }
    });

    function switchTab(targetId, updateHash = true) {
      tabButtons.forEach(btn => {
        const matches = btn.getAttribute('data-tab') === targetId;
        btn.classList.toggle('active', matches);
        btn.setAttribute('aria-selected', String(matches));
      });

      tabPanels.forEach(panel => {
        const matches = panel.id === targetId;
        panel.classList.toggle('active', matches);
      });

      if (updateHash && history.replaceState) {
        history.replaceState(null, '', '#' + targetId);
      }
    }

    tabButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        const targetId = btn.getAttribute('data-tab');
        switchTab(targetId, true);

        // On mobile, auto-minimize dock after selection so content is unobstructed
        if (window.innerWidth <= 768) {
          setMinimized(true);
        }

        // Scroll smoothly to top of content
        const hero = document.querySelector('.ro-hero');
        if (hero) {
          const top = hero.getBoundingClientRect().bottom + window.pageYOffset - 10;
          window.scrollTo({ top, behavior: 'smooth' });
        }
      });
    });

    // Check URL hash on page load
    const hash = window.location.hash ? window.location.hash.slice(1) : '';
    if (hash && document.getElementById(hash) && document.getElementById(hash).classList.contains('ro-tab-panel')) {
      switchTab(hash, false);
    } else {
      // Default to first tab (Study Notes)
      switchTab('tab-notes', false);
    }

    // Initial state from localStorage or default
    const savedMin = localStorage.getItem('ro_tabs_dock_minimized');
    if (savedMin === 'true') {
      setMinimized(true);
    } else if (savedMin === 'false') {
      setMinimized(false);
    } else {
      // Start expanded so user immediately sees the right-side tabs
      setMinimized(false);
    }

    // Global helper for in-page navigation links
    window.roSwitchTab = function(targetId, scrollIntoView = true) {
      switchTab(targetId, true);
      if (scrollIntoView) {
        const hero = document.querySelector('.ro-hero');
        if (hero) {
          hero.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      }
    };
  }

  // --- 2. Practice Tab: Instant Option Selection, Evaluation & Explanation Reveal ---
  function initPracticeInteractions() {
    document.querySelectorAll('.ro-pyq-card').forEach(card => {
      const options = card.querySelectorAll('.ro-pyq-opt');
      const qIdx = card.getAttribute('data-qidx');
      const solutionEl = document.getElementById(`ro-pyq-sol-${qIdx}`);
      const toggleBtn = document.getElementById(`ro-pyq-btn-${qIdx}`);

      options.forEach(opt => {
        opt.addEventListener('click', () => {
          const isCorrect = opt.getAttribute('data-correct') === 'true';

          // Reset previous state on this question
          options.forEach(o => {
            o.classList.remove('selected', 'correct', 'wrong');
            const fb = o.querySelector('.ro-opt-feedback');
            if (fb) fb.innerHTML = '';
          });

          // Mark clicked option
          if (isCorrect) {
            opt.classList.add('correct');
            const fb = opt.querySelector('.ro-opt-feedback');
            if (fb) fb.innerHTML = '<i class="fa-solid fa-circle-check" style="color: #10b981;"></i>';
          } else {
            opt.classList.add('wrong');
            const fb = opt.querySelector('.ro-opt-feedback');
            if (fb) fb.innerHTML = '<i class="fa-solid fa-circle-xmark" style="color: #ef4444;"></i>';

            // Also highlight the actual correct option in green
            options.forEach(o => {
              if (o.getAttribute('data-correct') === 'true') {
                o.classList.add('correct');
                const correctFb = o.querySelector('.ro-opt-feedback');
                if (correctFb) correctFb.innerHTML = '<i class="fa-solid fa-circle-check" style="color: #10b981;"></i>';
              }
            });
          }

          // Immediately display solution & explanation
          if (solutionEl) {
            solutionEl.style.display = 'block';
            // Smoothly bring explanation into view if partially offscreen
            solutionEl.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
          }

          // Update toggle button text to show revealed state
          if (toggleBtn) {
            toggleBtn.innerHTML = `
              <i class="fa-solid fa-circle-check"></i>
              <span class="lang-en">Explanation Revealed</span>
              <span class="lang-hi">व्याख्या प्रदर्शित</span>
            `;
          }
        });
      });
    });
  }

  // Solution Toggle helper for manual button clicks
  window.toggleRoSolution = function(id) {
    const el = document.getElementById(id);
    if (!el) return;
    el.style.display = el.style.display === 'block' ? 'none' : 'block';
  };

  // --- 3. Mains Word Counter ---
  function initWordCounters() {
    document.querySelectorAll('.ro-practice-textarea').forEach(textarea => {
      const counterId = textarea.getAttribute('data-counter-id');
      const counterEl = document.getElementById(counterId);
      const limit = parseInt(textarea.getAttribute('data-word-limit') || '75', 10);

      textarea.addEventListener('input', () => {
        const text = textarea.value.trim();
        const wordCount = text ? text.split(/\s+/).length : 0;
        if (counterEl) {
          const numEls = counterEl.querySelectorAll('.ro-wc-num');
          if (numEls.length > 0) {
            numEls.forEach(el => { el.textContent = wordCount; });
          } else {
            counterEl.textContent = `${wordCount} / ${limit} words`;
          }
          if (wordCount > limit) {
            counterEl.style.color = '#ef4444';
            counterEl.style.fontWeight = '700';
          } else {
            counterEl.style.color = '';
            counterEl.style.fontWeight = '';
          }
        }
      });
    });
  }

  // --- 4. Three-Level UPPSC Mini Test Engine ---
  window.RoTestEngine = function(config) {
    const { questionsByLevel, containerId } = config;
    let currentLevel = 1;
    let currentQIdx = 0;
    let userAnswers = {}; // { level: { qIdx: selectedOptionIdx } }
    let testSubmitted = {}; // { level: bool }
    let timerInterval = null;
    let secondsElapsed = 0;

    const container = document.getElementById(containerId);
    if (!container) return;

    const levelNames = {
      1: { en: 'Level 1: Foundation (Direct Factual)', hi: 'स्तर 1: आधारभूत (प्रत्यक्ष तथ्यात्मक प्रश्न)' },
      2: { en: 'Level 2: Moderate (Assertion & 2-Statements)', hi: 'स्तर 2: मध्यम (कथन-कारण व 2-कथनीय प्रश्न)' },
      3: { en: 'Level 3: Advanced (Multi-Statement & Elimination)', hi: 'स्तर 3: उच्च (बहु-कथनीय व विलोपन पद्धति)' }
    };

    function renderEngine() {
      const qList = questionsByLevel[currentLevel] || [];
      const currentQ = qList[currentQIdx];
      const isSub = testSubmitted[currentLevel];

      let html = `
        <div class="ro-test-header">
          <div class="ro-level-selector">
            <button class="ro-level-btn ${currentLevel === 1 ? 'active' : ''}" data-lvl="1">
              <i class="fa-solid fa-seedling"></i>
              <span class="lang-en">Level 1 (Factual)</span>
              <span class="lang-hi">स्तर 1 (तथ्यात्मक)</span>
            </button>
            <button class="ro-level-btn ${currentLevel === 2 ? 'active' : ''}" data-lvl="2">
              <i class="fa-solid fa-scale-balanced"></i>
              <span class="lang-en">Level 2 (Assertion/Reason)</span>
              <span class="lang-hi">स्तर 2 (कथन/कारण)</span>
            </button>
            <button class="ro-level-btn ${currentLevel === 3 ? 'active' : ''}" data-lvl="3">
              <i class="fa-solid fa-shield-halved"></i>
              <span class="lang-en">Level 3 (Multi-Statement)</span>
              <span class="lang-hi">स्तर 3 (बहु-कथनीय)</span>
            </button>
          </div>
          <div class="ro-test-timer">
            <i class="fa-regular fa-clock"></i> <span id="roTimerDisplay">${formatTime(secondsElapsed)}</span>
          </div>
        </div>

        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem; font-size: 0.85rem; color: var(--ro-text-muted);">
          <span>
            <span class="lang-en"><strong>${levelNames[currentLevel].en}</strong> &bull; Question ${currentQIdx + 1} of ${qList.length}</span>
            <span class="lang-hi"><strong>${levelNames[currentLevel].hi}</strong> &bull; प्रश्न ${currentQIdx + 1} / ${qList.length}</span>
          </span>
          <span>
            <span class="lang-en">Marking: +1.00 | -0.33</span>
            <span class="lang-hi">अंकन: +1.00 | -0.33</span>
          </span>
        </div>
      `;

      if (currentQ) {
        html += `
          <div class="ro-test-q-box" style="margin-bottom: 1.25rem;">
            <div style="font-weight: 700; font-size: 1rem; line-height: 1.45; color: var(--ro-text-heading); margin-bottom: 1rem;">
              <span class="lang-en">${currentQ.qEn}</span>
              <span class="lang-hi">${currentQ.qHi}</span>
            </div>
            <div class="ro-pyq-options" style="margin-bottom: 1rem;">
        `;

        const chosen = (userAnswers[currentLevel] && userAnswers[currentLevel][currentQIdx] !== undefined)
          ? userAnswers[currentLevel][currentQIdx] : null;

        currentQ.options.forEach((opt, oIdx) => {
          let optClass = 'ro-pyq-opt';
          const isSelected = chosen === oIdx;
          if (isSelected) optClass += ' selected';
          if (isSub) {
            if (oIdx === currentQ.correct) optClass += ' correct';
            else if (isSelected) optClass += ' wrong';
          }

          html += `
            <div class="${optClass}" data-opt-idx="${oIdx}" role="button" tabindex="0" style="${isSub ? 'cursor: default;' : ''}">
              <span class="ro-opt-letter">${String.fromCharCode(65 + oIdx)}</span>
              <span class="ro-opt-text">
                <span class="lang-en">${opt.en}</span>
                <span class="lang-hi">${opt.hi}</span>
              </span>
              <span class="ro-opt-feedback">
                ${isSelected && !isSub ? '<i class="fa-solid fa-circle-dot" style="color: var(--ro-primary);"></i>' : ''}
                ${isSub && oIdx === currentQ.correct ? '<i class="fa-solid fa-circle-check" style="color: #10b981;"></i>' : ''}
                ${isSub && isSelected && chosen !== currentQ.correct ? '<i class="fa-solid fa-circle-xmark" style="color: #ef4444;"></i>' : ''}
              </span>
            </div>
          `;
        });

        html += `</div></div>`;

        if (isSub) {
          html += `
            <div class="ro-solution" style="display: block; margin-bottom: 1.25rem;">
              <strong><i class="fa-solid fa-circle-check"></i> <span class="lang-en">Detailed Explanation:</span><span class="lang-hi">विस्तृत व्याख्या:</span></strong><br/>
              <span class="lang-en">${currentQ.explanation.en}</span>
              <span class="lang-hi">${currentQ.explanation.hi}</span>
            </div>
          `;
        }
      }

      html += `
        <div class="ro-test-nav">
          <button class="ro-btn" id="roPrevBtn" ${currentQIdx === 0 ? 'disabled style="opacity:0.5; cursor:not-allowed;"' : ''}>
            <i class="fa-solid fa-chevron-left"></i> <span class="lang-en">Previous</span><span class="lang-hi">पिछला</span>
          </button>
          <div style="display: flex; gap: 0.5rem; flex: 1; justify-content: center;">
            ${!isSub ? `
              <button class="ro-btn" id="roSubmitLevelBtn" style="background: #059669;">
                <i class="fa-solid fa-paper-plane"></i> <span class="lang-en">Submit Level</span><span class="lang-hi">स्तर सबमिट करें</span>
              </button>
            ` : `
              <button class="ro-btn" id="roResetLevelBtn" style="background: #475569;">
                <i class="fa-solid fa-rotate-left"></i> <span class="lang-en">Re-take Level</span><span class="lang-hi">पुनः टेस्ट दें</span>
              </button>
            `}
          </div>
          <button class="ro-btn" id="roNextBtn" ${currentQIdx === qList.length - 1 ? 'disabled style="opacity:0.5; cursor:not-allowed;"' : ''}>
            <span class="lang-en">Next</span><span class="lang-hi">अगला</span> <i class="fa-solid fa-chevron-right"></i>
          </button>
        </div>
      `;

      if (isSub) {
        const stats = calculateStats(currentLevel);
        html += `
          <div class="ro-test-summary" style="display: block;">
            <h3>
              <span class="lang-en">Level ${currentLevel} Performance Report</span>
              <span class="lang-hi">स्तर ${currentLevel} परीक्षा परिणाम</span>
            </h3>
            <div class="ro-test-score-badge">${stats.netScore.toFixed(2)} / ${qList.length}</div>
            <div style="display: flex; justify-content: center; gap: 1.25rem; flex-wrap: wrap; margin-top: 0.75rem; font-size: 0.9rem;">
              <span style="color: #059669;">
                <span class="lang-en"><strong>Correct:</strong> ${stats.correct}</span>
                <span class="lang-hi"><strong>सही उत्तर:</strong> ${stats.correct}</span>
              </span>
              <span style="color: #ef4444;">
                <span class="lang-en"><strong>Wrong (-0.33):</strong> ${stats.wrong}</span>
                <span class="lang-hi"><strong>गलत (-0.33):</strong> ${stats.wrong}</span>
              </span>
              <span style="color: #64748b;">
                <span class="lang-en"><strong>Unattempted:</strong> ${stats.unattempted}</span>
                <span class="lang-hi"><strong>अनुत्तरित:</strong> ${stats.unattempted}</span>
              </span>
              <span style="color: #0f766e;">
                <span class="lang-en"><strong>Accuracy:</strong> ${stats.accuracy}%</span>
                <span class="lang-hi"><strong>सटीकता:</strong> ${stats.accuracy}%</span>
              </span>
            </div>
          </div>
        `;
      }

      container.innerHTML = html;
      bindEvents();
    }

    function calculateStats(lvl) {
      const qList = questionsByLevel[lvl] || [];
      const answers = userAnswers[lvl] || {};
      let correct = 0;
      let wrong = 0;
      let unattempted = 0;

      qList.forEach((q, idx) => {
        const ans = answers[idx];
        if (ans === undefined) unattempted++;
        else if (ans === q.correct) correct++;
        else wrong++;
      });

      const netScore = Math.max(0, correct * 1.0 - wrong * 0.33);
      const attempted = correct + wrong;
      const accuracy = attempted > 0 ? Math.round((correct / attempted) * 100) : 0;
      return { correct, wrong, unattempted, netScore, accuracy };
    }

    function formatTime(sec) {
      const m = Math.floor(sec / 60);
      const s = sec % 60;
      return `${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;
    }

    function bindEvents() {
      // Level selector buttons
      container.querySelectorAll('.ro-level-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          currentLevel = parseInt(btn.getAttribute('data-lvl'), 10);
          currentQIdx = 0;
          renderEngine();
        });
      });

      // Option click inside test (Immediate visual highlighting)
      if (!testSubmitted[currentLevel]) {
        container.querySelectorAll('.ro-pyq-opt').forEach(opt => {
          opt.addEventListener('click', () => {
            const optIdx = parseInt(opt.getAttribute('data-opt-idx'), 10);
            if (!userAnswers[currentLevel]) userAnswers[currentLevel] = {};
            userAnswers[currentLevel][currentQIdx] = optIdx;
            renderEngine();
          });
        });
      }

      // Prev / Next
      const prevBtn = document.getElementById('roPrevBtn');
      if (prevBtn) {
        prevBtn.addEventListener('click', () => {
          if (currentQIdx > 0) {
            currentQIdx--;
            renderEngine();
          }
        });
      }

      const nextBtn = document.getElementById('roNextBtn');
      if (nextBtn) {
        nextBtn.addEventListener('click', () => {
          const qList = questionsByLevel[currentLevel] || [];
          if (currentQIdx < qList.length - 1) {
            currentQIdx++;
            renderEngine();
          }
        });
      }

      // Submit
      const subBtn = document.getElementById('roSubmitLevelBtn');
      if (subBtn) {
        subBtn.addEventListener('click', () => {
          testSubmitted[currentLevel] = true;
          renderEngine();
        });
      }

      // Re-take
      const resetBtn = document.getElementById('roResetLevelBtn');
      if (resetBtn) {
        resetBtn.addEventListener('click', () => {
          testSubmitted[currentLevel] = false;
          if (userAnswers[currentLevel]) delete userAnswers[currentLevel];
          currentQIdx = 0;
          renderEngine();
        });
      }
    }

    // Start timer
    timerInterval = setInterval(() => {
      secondsElapsed++;
      const timerEl = document.getElementById('roTimerDisplay');
      if (timerEl) timerEl.textContent = formatTime(secondsElapsed);
    }, 1000);

    renderEngine();
  };

  // Auto-init on DOMContentLoaded
  function initAll() {
    initTabs();
    initPracticeInteractions();
    initWordCounters();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAll);
  } else {
    initAll();
  }
})();
