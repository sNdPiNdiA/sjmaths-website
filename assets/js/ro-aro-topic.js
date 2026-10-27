/**
 * UPPSC RO/ARO Topic Common Engine (ro-aro-topic.js)
 * Manages 4-tab switching, Prelims PYQs, Mains simulator, and 3-level test engine
 */

(() => {
  'use strict';

  // --- 1. Tab Navigation System ---
  function initTabs() {
    const tabButtons = document.querySelectorAll('.ro-tab-btn');
    const tabPanels = document.querySelectorAll('.ro-tab-panel');

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

    // Global helper for in-page navigation links
    window.roSwitchTab = function(targetId, scrollIntoView = true) {
      switchTab(targetId, true);
      if (scrollIntoView) {
        const tabsBar = document.querySelector('.ro-tabs-bar');
        if (tabsBar) {
          tabsBar.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      }
    };
  }

  // --- 2. Solution Toggle for PYQ Cards ---
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
          counterEl.textContent = `${wordCount} / ${limit} words`;
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

    function renderEngine() {
      const qList = questionsByLevel[currentLevel] || [];
      const currentQ = qList[currentQIdx];
      const isSub = testSubmitted[currentLevel];

      let levelName = currentLevel === 1 ? 'Level 1: Foundation (Direct Factual)' :
                      currentLevel === 2 ? 'Level 2: Moderate (Assertion & 2-Statements)' :
                                           'Level 3: Advanced (Multi-Statement & Elimination)';

      let html = `
        <div class="ro-test-header">
          <div class="ro-level-selector">
            <button class="ro-level-btn ${currentLevel === 1 ? 'active' : ''}" data-lvl="1">
              <i class="fa-solid fa-seedling"></i> Level 1 (Factual)
            </button>
            <button class="ro-level-btn ${currentLevel === 2 ? 'active' : ''}" data-lvl="2">
              <i class="fa-solid fa-scale-balanced"></i> Level 2 (Assertion/Reason)
            </button>
            <button class="ro-level-btn ${currentLevel === 3 ? 'active' : ''}" data-lvl="3">
              <i class="fa-solid fa-shield-halved"></i> Level 3 (Multi-Statement)
            </button>
          </div>
          <div class="ro-test-timer">
            <i class="fa-regular fa-clock"></i> <span id="roTimerDisplay">${formatTime(secondsElapsed)}</span>
          </div>
        </div>

        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem; font-size: 0.85rem; color: var(--ro-text-muted);">
          <span><strong>${levelName}</strong> &bull; Question ${currentQIdx + 1} of ${qList.length}</span>
          <span>Marking: +1.00 | -0.33</span>
        </div>
      `;

      if (currentQ) {
        html += `
          <div class="ro-test-q-box" style="margin-bottom: 1.25rem;">
            <div style="font-weight: 700; font-size: 1rem; color: var(--ro-text-heading); margin-bottom: 1rem;">
              <span class="lang-en">${currentQ.qEn}</span>
              <span class="lang-hi">${currentQ.qHi}</span>
            </div>
            <div style="display: flex; flex-direction: column; gap: 0.5rem;">
        `;

        const chosen = (userAnswers[currentLevel] && userAnswers[currentLevel][currentQIdx] !== undefined)
          ? userAnswers[currentLevel][currentQIdx] : null;

        currentQ.options.forEach((opt, oIdx) => {
          let optClass = 'ro-pyq-opt';
          if (chosen === oIdx) optClass += ' selected';
          if (isSub) {
            if (oIdx === currentQ.correct) optClass += ' correct';
            else if (chosen === oIdx) optClass += ' wrong';
          }

          html += `
            <div class="${optClass}" data-opt-idx="${oIdx}" style="${isSub ? 'cursor: default;' : ''}">
              <span style="font-weight: 700; width: 1.5rem;">${String.fromCharCode(65 + oIdx)}.</span>
              <span><span class="lang-en">${opt.en}</span><span class="lang-hi">${opt.hi}</span></span>
            </div>
          `;
        });

        html += `</div></div>`;

        if (isSub) {
          html += `
            <div style="background: #f0fdfa; border: 1px solid #99f6e4; border-radius: 8px; padding: 1rem; font-size: 0.88rem; color: #0f766e; margin-bottom: 1rem;">
              <strong><i class="fa-solid fa-circle-check"></i> Explanation:</strong><br/>
              <span class="lang-en">${currentQ.explanation.en}</span>
              <span class="lang-hi">${currentQ.explanation.hi}</span>
            </div>
          `;
        }
      }

      html += `
        <div class="ro-test-nav">
          <button class="ro-btn" id="roPrevBtn" ${currentQIdx === 0 ? 'disabled style="opacity:0.5; cursor:not-allowed;"' : ''}>
            <i class="fa-solid fa-chevron-left"></i> Previous
          </button>
          <div style="display: flex; gap: 0.5rem;">
            ${!isSub ? `
              <button class="ro-btn" id="roSubmitLevelBtn" style="background: #047857;">
                <i class="fa-solid fa-paper-plane"></i> Submit Level
              </button>
            ` : `
              <button class="ro-btn" id="roResetLevelBtn" style="background: #475569;">
                <i class="fa-solid fa-rotate-left"></i> Re-take Level
              </button>
            `}
          </div>
          <button class="ro-btn" id="roNextBtn" ${currentQIdx === qList.length - 1 ? 'disabled style="opacity:0.5; cursor:not-allowed;"' : ''}>
            Next <i class="fa-solid fa-chevron-right"></i>
          </button>
        </div>
      `;

      if (isSub) {
        const stats = calculateStats(currentLevel);
        html += `
          <div class="ro-test-summary" style="display: block;">
            <h3>Level ${currentLevel} Performance Report</h3>
            <div class="ro-test-score-badge">${stats.netScore.toFixed(2)} / ${qList.length}</div>
            <div style="display: flex; justify-content: center; gap: 1.5rem; flex-wrap: wrap; margin-top: 0.75rem; font-size: 0.9rem;">
              <span style="color: #047857;"><strong>Correct:</strong> ${stats.correct}</span>
              <span style="color: #b91c1c;"><strong>Wrong (-0.33):</strong> ${stats.wrong}</span>
              <span style="color: #64748b;"><strong>Unattempted:</strong> ${stats.unattempted}</span>
              <span style="color: #0f766e;"><strong>Accuracy:</strong> ${stats.accuracy}%</span>
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

      // Option click
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
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
      initTabs();
      initWordCounters();
    });
  } else {
    initTabs();
    initWordCounters();
  }
})();
