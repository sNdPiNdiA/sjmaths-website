/**
 * UPPSC RO/ARO Topic Common Engine (ro-aro-topic.js)
 * Manages 5-tab switching, instant Practice PYQ evaluation, Mains word counter, and 3-level test engine
 */

(() => {
  'use strict';

  const TAB_SYNONYMS = {
    notes: ['tab-notes', 'notes-panel'],
    practice: ['tab-practice', 'pyq-panel', 'pyqs-panel', 'practice-panel'],
    test: ['tab-test', 'test-panel'],
    mains: ['tab-mains', 'mains-panel'],
    revision: ['tab-revision', 'revision-panel']
  };

  function findPanel(id) {
    if (!id) return null;
    let p = document.getElementById(id);
    if (p && p.classList.contains('ro-tab-panel')) return p;
    for (const group of Object.values(TAB_SYNONYMS)) {
      if (group.includes(id)) {
        for (const syn of group) {
          p = document.getElementById(syn);
          if (p && p.classList.contains('ro-tab-panel')) return p;
        }
      }
    }
    return null;
  }

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
      const targetPanel = findPanel(targetId);
      const actualTargetId = targetPanel ? targetPanel.id : targetId;

      let activeSynonyms = [targetId, actualTargetId];
      for (const group of Object.values(TAB_SYNONYMS)) {
        if (group.includes(targetId) || group.includes(actualTargetId)) {
          activeSynonyms = group;
          break;
        }
      }

      tabButtons.forEach(btn => {
        const btnTab = btn.getAttribute('data-tab');
        const matches = activeSynonyms.includes(btnTab);
        btn.classList.toggle('active', matches);
        btn.setAttribute('aria-selected', String(matches));
      });

      tabPanels.forEach(panel => {
        const matches = (panel === targetPanel) || (panel.id === actualTargetId);
        panel.classList.toggle('active', matches);
      });

      if (updateHash && history.replaceState) {
        history.replaceState(null, '', '#' + actualTargetId);
      }
    }

    tabButtons.forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        const targetId = btn.getAttribute('data-tab');
        switchTab(targetId, true);

        // On mobile, auto-minimize dock after selection so content is unobstructed
        if (window.innerWidth <= 768) {
          setMinimized(true);
        }

        // Scroll smoothly to top of content
        const hero = document.querySelector('.ro-hero, .ro-hero-header');
        if (hero) {
          const top = hero.getBoundingClientRect().bottom + window.pageYOffset - 10;
          window.scrollTo({ top, behavior: 'smooth' });
        }
      });
    });

    // Check URL hash on page load
    const hash = window.location.hash ? window.location.hash.slice(1) : '';
    const initialPanel = findPanel(hash);
    if (initialPanel) {
      switchTab(initialPanel.id, false);
    } else {
      // Default to first tab (Study Notes) in DOM
      const firstPanel = document.querySelector('.ro-tab-panel');
      const defaultId = firstPanel ? firstPanel.id : 'tab-notes';
      switchTab(defaultId, false);
      // Ensure page starts at the top on fresh load without anchor
      if (window.scrollY > 100) {
        window.scrollTo({ top: 0, behavior: 'instant' });
      }
    }

    // Initial state from localStorage or default
    const savedMin = localStorage.getItem('ro_tabs_dock_minimized');
    if (savedMin === 'true') {
      setMinimized(true);
    } else if (savedMin === 'false') {
      setMinimized(false);
    } else {
      // On mobile, start minimized so screen space is immediately free
      setMinimized(window.innerWidth <= 768);
    }

    // Global helper for in-page navigation links
    window.roSwitchTab = function(targetId, scrollIntoView = true) {
      switchTab(targetId, true);
      if (window.innerWidth <= 768) {
        setMinimized(true);
      }
      if (scrollIntoView) {
        const hero = document.querySelector('.ro-hero, .ro-hero-header');
        if (hero) {
          hero.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      }
    };
  }

  // --- 2. Practice Tab: Instant Option Selection, Evaluation & Explanation Reveal ---
  window.handlePyqOptClick = function(optEl) {
    if (!optEl) return;
    const card = optEl.closest('.ro-pyq-card, .pyq-card, .ro-fact-card');
    if (!card) return;

    const options = card.querySelectorAll('.ro-pyq-opt, .pyq-option');
    const isCorrect = optEl.getAttribute('data-correct') === 'true';

    options.forEach(o => {
      o.classList.remove('selected', 'correct', 'wrong');
      const fb = o.querySelector('.ro-opt-feedback');
      if (fb) fb.innerHTML = '';
    });

    if (isCorrect) {
      optEl.classList.add('correct');
      const fb = optEl.querySelector('.ro-opt-feedback');
      if (fb) fb.innerHTML = '<i class="fa-solid fa-circle-check" style="color: #10b981;"></i>';
    } else {
      optEl.classList.add('wrong');
      const fb = optEl.querySelector('.ro-opt-feedback');
      if (fb) fb.innerHTML = '<i class="fa-solid fa-circle-xmark" style="color: #ef4444;"></i>';

      options.forEach(o => {
        if (o.getAttribute('data-correct') === 'true') {
          o.classList.add('correct');
          const correctFb = o.querySelector('.ro-opt-feedback');
          if (correctFb) correctFb.innerHTML = '<i class="fa-solid fa-circle-check" style="color: #10b981;"></i>';
        }
      });
    }

    const sol = card.querySelector('.ro-pyq-explanation, .pyq-explanation') ||
                (card.dataset.qidx ? document.getElementById(`ro-pyq-sol-${card.dataset.qidx}`) : null);
    if (sol) {
      sol.style.display = 'block';
      sol.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }

    if (card.dataset.qidx) {
      const toggleBtn = document.getElementById(`ro-pyq-btn-${card.dataset.qidx}`);
      if (toggleBtn) {
        toggleBtn.innerHTML = `
          <i class="fa-solid fa-circle-check"></i>
          <span class="lang-en">Explanation Revealed</span>
          <span class="lang-hi">व्याख्या प्रदर्शित</span>
        `;
      }
    }
  };

  window.checkOption = function(optEl, correctIdx) {
    if (!optEl) return;
    const card = optEl.closest('.pyq-card, .ro-pyq-card, .ro-fact-card');
    if (!card) return;

    const options = card.querySelectorAll('.pyq-option, .ro-pyq-opt');
    const optIdx = parseInt(optEl.getAttribute('data-opt'), 10);
    const isCorrect = (optIdx === correctIdx);

    options.forEach(o => {
      o.classList.remove('selected', 'correct', 'wrong');
      const fb = o.querySelector('.ro-opt-feedback');
      if (fb) fb.innerHTML = '';
    });

    if (isCorrect) {
      optEl.classList.add('correct');
      const fb = optEl.querySelector('.ro-opt-feedback');
      if (fb) fb.innerHTML = '<i class="fa-solid fa-circle-check" style="color: #10b981;"></i>';
    } else {
      optEl.classList.add('wrong');
      const fb = optEl.querySelector('.ro-opt-feedback');
      if (fb) fb.innerHTML = '<i class="fa-solid fa-circle-xmark" style="color: #ef4444;"></i>';

      options.forEach(o => {
        if (parseInt(o.getAttribute('data-opt'), 10) === correctIdx) {
          o.classList.add('correct');
          const correctFb = o.querySelector('.ro-opt-feedback');
          if (correctFb) correctFb.innerHTML = '<i class="fa-solid fa-circle-check" style="color: #10b981;"></i>';
        }
      });
    }

    const sol = card.querySelector('.pyq-explanation, .ro-pyq-explanation');
    if (sol) {
      sol.style.display = 'block';
      sol.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
  };

  function initPracticeInteractions() {
    document.querySelectorAll('.ro-pyq-card').forEach(card => {
      const options = card.querySelectorAll('.ro-pyq-opt');
      options.forEach(opt => {
        if (!opt.hasAttribute('onclick')) {
          opt.addEventListener('click', () => {
            window.handlePyqOptClick(opt);
          });
        }
      });
    });
  }

  window.toggleRoSolution = function(id) {
    const el = document.getElementById(id);
    if (!el) return;
    el.style.display = el.style.display === 'block' ? 'none' : 'block';
  };

  // --- 3. Mains Word Counter ---
  window.updateWordCount = function(textarea) {
    if (!textarea) return;
    const text = textarea.value.trim();
    const wordCount = text ? text.split(/\s+/).length : 0;
    const box = textarea.closest('.mains-input-box, .mains-card, .ro-fact-card');
    if (box) {
      const wcCount = box.querySelector('.wc-count');
      if (wcCount) wcCount.textContent = wordCount;

      const bar = box.querySelector('.word-count-bar');
      let limit = 75;
      if (bar && bar.textContent) {
        const m = bar.textContent.match(/\/\s*(\d+)/);
        if (m) limit = parseInt(m[1], 10);
      } else if (textarea.hasAttribute('data-word-limit')) {
        limit = parseInt(textarea.getAttribute('data-word-limit'), 10);
      }

      if (bar) {
        if (wordCount > limit) {
          bar.style.color = '#ef4444';
          bar.style.fontWeight = '700';
        } else {
          bar.style.color = '';
          bar.style.fontWeight = '';
        }
      }
    }
  };

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

    document.querySelectorAll('.mains-textarea').forEach(textarea => {
      if (!textarea.hasAttribute('oninput')) {
        textarea.addEventListener('input', () => {
          window.updateWordCount(textarea);
        });
      }
    });
  }

  // --- 4. Three-Level UPPSC Mini Test Engine ---
  window.RoTestEngine = function(config) {
    let { questionsByLevel, containerId } = config;

    // Normalize if questionsByLevel is an array
    if (Array.isArray(questionsByLevel)) {
      const grouped = { 1: [], 2: [], 3: [] };
      questionsByLevel.forEach(q => {
        const lvl = q.level || 1;
        if (!grouped[lvl]) grouped[lvl] = [];
        grouped[lvl].push(q);
      });
      questionsByLevel = grouped;
    }
    let currentLevel = 1;
    let currentQIdx = 0;
    let userAnswers = {}; // { level: { qIdx: selectedOptionIdx } }
    let testSubmitted = {}; // { level: bool }
    let timerInterval = null;
    let secondsElapsed = 0;

    const container = document.getElementById(containerId);
    if (!container) return;
    if (container._roTimerInterval) {
      clearInterval(container._roTimerInterval);
    }
    container.dataset.initialized = 'true';

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
            <button type="button" class="ro-level-btn ${currentLevel === 1 ? 'active' : ''}" data-lvl="1">
              <i class="fa-solid fa-seedling"></i>
              <span class="lang-en">Level 1 (Factual)</span>
              <span class="lang-hi">स्तर 1 (तथ्यात्मक)</span>
            </button>
            <button type="button" class="ro-level-btn ${currentLevel === 2 ? 'active' : ''}" data-lvl="2">
              <i class="fa-solid fa-scale-balanced"></i>
              <span class="lang-en">Level 2 (Assertion/Reason)</span>
              <span class="lang-hi">स्तर 2 (कथन/कारण)</span>
            </button>
            <button type="button" class="ro-level-btn ${currentLevel === 3 ? 'active' : ''}" data-lvl="3">
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
        const qEnText = currentQ.qEn || currentQ.questionEn || currentQ.q || currentQ.qHi || currentQ.questionHi || currentQ.question || '';
        const qHiText = currentQ.qHi || currentQ.questionHi || currentQ.q || currentQ.question || currentQ.qEn || currentQ.questionEn || '';
        const expStr = typeof currentQ.explanation === 'string' ? currentQ.explanation : (typeof currentQ.exp === 'string' ? currentQ.exp : '');
        const expEn = (currentQ.explanation && currentQ.explanation.en) || currentQ.explanationEn || currentQ.expEn || expStr || (currentQ.explanation && currentQ.explanation.hi) || currentQ.explanationHi || currentQ.expHi || '';
        const expHi = (currentQ.explanation && currentQ.explanation.hi) || currentQ.explanationHi || currentQ.expHi || expStr || (currentQ.explanation && currentQ.explanation.en) || currentQ.explanationEn || currentQ.expEn || '';

        html += `
          <div class="ro-test-q-box" style="margin-bottom: 1.25rem;">
            <div style="font-weight: 700; font-size: 1rem; line-height: 1.55; color: var(--ro-text-heading); margin-bottom: 1rem; white-space: pre-line;">
              <span class="lang-en">${qEnText}</span>
              <span class="lang-hi">${qHiText}</span>
            </div>
            <div class="ro-pyq-options" style="margin-bottom: 1rem;">
        `;

        const chosen = (userAnswers[currentLevel] && userAnswers[currentLevel][currentQIdx] !== undefined)
          ? userAnswers[currentLevel][currentQIdx] : null;

        (currentQ.options || []).forEach((opt, oIdx) => {
          let optClass = 'ro-pyq-opt';
          const isSelected = chosen === oIdx;
          if (isSelected) optClass += ' selected';
          if (isSub) {
            if (oIdx === currentQ.correct) optClass += ' correct';
            else if (isSelected) optClass += ' wrong';
          }

          let optEn = '';
          let optHi = '';
          if (typeof opt === 'string') {
            const clean = opt.replace(/^[A-D\u0915-\u0918][\.\)\-]\s*/, '').trim();
            optEn = clean;
            optHi = clean;
          } else if (opt && typeof opt === 'object') {
            const rawEn = opt.en || opt.hi || '';
            const rawHi = opt.hi || opt.en || '';
            optEn = String(rawEn).replace(/^[A-D\u0915-\u0918][\.\)\-]\s*/, '').trim();
            optHi = String(rawHi).replace(/^[A-D\u0915-\u0918][\.\)\-]\s*/, '').trim();
          }

          html += `
            <div class="${optClass}" data-opt-idx="${oIdx}" role="button" tabindex="0" style="${isSub ? 'cursor: default;' : ''}">
              <span class="ro-opt-letter">${String.fromCharCode(65 + oIdx)}</span>
              <span class="ro-opt-text">
                <span class="lang-en">${optEn}</span>
                <span class="lang-hi">${optHi}</span>
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
            <div class="ro-solution" style="display: block; margin-bottom: 1.25rem; white-space: pre-line;">
              <strong><i class="fa-solid fa-circle-check"></i> <span class="lang-en">Detailed Explanation:</span><span class="lang-hi">विस्तृत व्याख्या:</span></strong><br/>
              <span class="lang-en">${expEn}</span>
              <span class="lang-hi">${expHi}</span>
            </div>
          `;
        }
      }

      html += `
        <div class="ro-test-nav">
          <button type="button" class="ro-btn" id="roPrevBtn" ${currentQIdx === 0 ? 'disabled style="opacity:0.5; cursor:not-allowed;"' : ''}>
            <i class="fa-solid fa-chevron-left"></i> <span class="lang-en">Previous</span><span class="lang-hi">पिछला</span>
          </button>
          <div style="display: flex; gap: 0.5rem; flex: 1; justify-content: center;">
            ${!isSub ? `
              <button type="button" class="ro-btn" id="roSubmitLevelBtn" style="background: #059669;">
                <i class="fa-solid fa-paper-plane"></i> <span class="lang-en">Submit Level</span><span class="lang-hi">स्तर सबमिट करें</span>
              </button>
            ` : `
              <button type="button" class="ro-btn" id="roResetLevelBtn" style="background: #475569;">
                <i class="fa-solid fa-rotate-left"></i> <span class="lang-en">Re-take Level</span><span class="lang-hi">पुनः टेस्ट दें</span>
              </button>
            `}
          </div>
          <button type="button" class="ro-btn" id="roNextBtn" ${currentQIdx === qList.length - 1 ? 'disabled style="opacity:0.5; cursor:not-allowed;"' : ''}>
            <span class="lang-en">Next</span><span class="lang-hi">अगला</span> <i class="fa-solid fa-chevron-right"></i>
          </button>
        </div>
      `;

      if (isSub) {
        const stats = calculateStats(currentLevel);
        html += `
          <div class="ro-test-result-box" style="margin-top: 1.5rem; padding: 1.25rem; border-radius: var(--ro-radius-md); background: #f0fdf4; border: 1px solid #bbf7d0; text-align: center;">
            <h3 style="margin: 0 0 0.5rem 0; font-size: 1.1rem; color: #166534;">
              <span class="lang-en">Level ${currentLevel} Performance Summary</span>
              <span class="lang-hi">स्तर ${currentLevel} परिणाम सारांश</span>
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
        btn.addEventListener('click', (e) => {
          e.preventDefault();
          currentLevel = parseInt(btn.getAttribute('data-lvl'), 10);
          currentQIdx = 0;
          renderEngine();
        });
      });

      // Option click inside test (Immediate visual highlighting)
      if (!testSubmitted[currentLevel]) {
        container.querySelectorAll('.ro-pyq-opt').forEach(opt => {
          opt.addEventListener('click', (e) => {
            e.preventDefault();
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
        prevBtn.addEventListener('click', (e) => {
          e.preventDefault();
          if (currentQIdx > 0) {
            currentQIdx--;
            renderEngine();
          }
        });
      }

      const nextBtn = document.getElementById('roNextBtn');
      if (nextBtn) {
        nextBtn.addEventListener('click', (e) => {
          e.preventDefault();
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
        subBtn.addEventListener('click', (e) => {
          e.preventDefault();
          testSubmitted[currentLevel] = true;
          renderEngine();
        });
      }

      // Re-take
      const resetBtn = document.getElementById('roResetLevelBtn');
      if (resetBtn) {
        resetBtn.addEventListener('click', (e) => {
          e.preventDefault();
          testSubmitted[currentLevel] = false;
          if (userAnswers[currentLevel]) delete userAnswers[currentLevel];
          currentQIdx = 0;
          renderEngine();
        });
      }
    }

    // Start timer
    if (timerInterval) clearInterval(timerInterval);
    timerInterval = setInterval(() => {
      secondsElapsed++;
      const timerEl = document.getElementById('roTimerDisplay');
      if (timerEl) timerEl.textContent = formatTime(secondsElapsed);
    }, 1000);
    container._roTimerInterval = timerInterval;

    renderEngine();
  };

  window.RoTestEngine.init = function(containerId, testData) {
    return window.RoTestEngine({
      containerId: containerId,
      questionsByLevel: testData
    });
  };

  // Auto-init RoTestEngine from #ro-test-data if container is present and unpopulated
  function initTestEngineAuto() {
    const container = document.getElementById('roTestContainer');
    if (!container) return;
    if (container.children.length > 0 || container.dataset.initialized === 'true') return;

    const script = document.getElementById('ro-test-data');
    if (!script) return;

    try {
      const raw = JSON.parse(script.textContent || script.innerText || '[]');
      let questionsByLevel = { "1": [], "2": [], "3": [] };

      function normalizeQ(q) {
        const qHi = q.qHi || q.questionHi || q.q || q.question || q.qEn || q.questionEn || '';
        const qEn = q.qEn || q.questionEn || q.q || q.question || qHi || '';
        const expStr = typeof q.explanation === 'string' ? q.explanation : (typeof q.exp === 'string' ? q.exp : '');
        const expHi = (q.explanation && q.explanation.hi) || q.explanationHi || q.expHi || expStr || (q.explanation && q.explanation.en) || q.explanationEn || q.expEn || '';
        const expEn = (q.explanation && q.explanation.en) || q.explanationEn || q.expEn || expStr || expHi;

        let correctIdx = 0;
        if (q.correct !== undefined && q.correct !== null && !isNaN(Number(q.correct))) {
          correctIdx = Number(q.correct);
        } else {
          const ansVal = q.ans !== undefined ? q.ans : (q.answer !== undefined ? q.answer : null);
          if (typeof ansVal === 'number') {
            correctIdx = ansVal;
          } else if (typeof ansVal === 'string') {
            const trimmed = ansVal.trim().toUpperCase();
            if (trimmed.startsWith('A') || trimmed === '0') correctIdx = 0;
            else if (trimmed.startsWith('B') || trimmed === '1') correctIdx = 1;
            else if (trimmed.startsWith('C') || trimmed === '2') correctIdx = 2;
            else if (trimmed.startsWith('D') || trimmed === '3') correctIdx = 3;
            else {
              const parsed = parseInt(trimmed, 10);
              if (!isNaN(parsed)) correctIdx = parsed;
            }
          }
        }

        return {
          id: q.id,
          qEn: qEn,
          qHi: qHi,
          options: (q.options || []).map(opt => {
            if (typeof opt === 'string') {
              const clean = opt.replace(/^[A-D\u0915-\u0918][\.\)\-]\s*/, '').trim();
              return { en: clean, hi: clean };
            }
            if (opt && typeof opt === 'object') {
              const oEn = (opt.en || opt.hi || '').replace(/^[A-D\u0915-\u0918][\.\)\-]\s*/, '').trim();
              const oHi = (opt.hi || opt.en || '').replace(/^[A-D\u0915-\u0918][\.\)\-]\s*/, '').trim();
              return { en: oEn, hi: oHi };
            }
            return { en: String(opt || ''), hi: String(opt || '') };
          }),
          correct: correctIdx,
          explanation: { en: expEn, hi: expHi }
        };
      }

      if (Array.isArray(raw)) {
        raw.forEach(q => {
          const lvl = String(q.level || 1);
          if (!questionsByLevel[lvl]) questionsByLevel[lvl] = [];
          questionsByLevel[lvl].push(normalizeQ(q));
        });
      } else if (raw.questions && Array.isArray(raw.questions)) {
        raw.questions.forEach(q => {
          const lvl = String(q.level || 1);
          if (!questionsByLevel[lvl]) questionsByLevel[lvl] = [];
          questionsByLevel[lvl].push(normalizeQ(q));
        });
      } else {
        const srcLevels = raw.questionsByLevel || raw;
        ['1', '2', '3'].forEach(lvl => {
          if (Array.isArray(srcLevels[lvl])) {
            questionsByLevel[lvl] = srcLevels[lvl].map(normalizeQ);
          }
        });
      }

      if (window.RoTestEngine) {
        window.RoTestEngine({
          containerId: 'roTestContainer',
          questionsByLevel: questionsByLevel
        });
      }
    } catch (e) {
      console.error('Error auto-initializing RoTestEngine from ro-test-data:', e);
    }
  }

  // Auto-init on DOMContentLoaded
  function initAll() {
    initTabs();
    initPracticeInteractions();
    initWordCounters();
    initTestEngineAuto();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAll);
  } else {
    initAll();
  }
})();
