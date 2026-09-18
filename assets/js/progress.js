/**
 * ============================================================================
 * SJ Maths — Home Science Topic Progress Engine
 * LocalStorage-based progress & mastery tracker
 * ============================================================================
 */

(function () {
  'use strict';

  function getCanonicalUrl() {
    const canonicalLink = document.querySelector('link[rel="canonical"]');
    if (canonicalLink && canonicalLink.getAttribute('href')) {
      try {
        const u = new URL(canonicalLink.getAttribute('href'));
        return u.pathname.endsWith('/') ? u.pathname : u.pathname + '/';
      } catch (e) {
        return window.location.pathname;
      }
    }
    return window.location.pathname.endsWith('/') ? window.location.pathname : window.location.pathname + '/';
  }

  const CANONICAL_PATH = getCanonicalUrl();
  const STORAGE_KEY = 'sjmaths-topic:' + CANONICAL_PATH;

  const defaultProgress = {
    notesComplete: false,
    revisionComplete: false,
    quizBestScore: 0,
    quizPassed: false,
    pyqAttempted: false,
    testBestScore: 0,
    testPassed: false,
    hasGenuinePyq: false,
    updatedAt: Date.now()
  };

  function loadProgress() {
    try {
      const data = localStorage.getItem(STORAGE_KEY);
      if (data) {
        return Object.assign({}, defaultProgress, JSON.parse(data));
      }
    } catch (e) {
      console.warn('Progress load failed from localStorage:', e);
    }
    return Object.assign({}, defaultProgress);
  }

  function saveProgress(state) {
    try {
      state.updatedAt = Date.now();
      localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
    } catch (e) {
      console.warn('Progress save failed:', e);
    }
  }

  function calculateMastery(state) {
    let mastery = 0;
    if (state.hasGenuinePyq) {
      if (state.notesComplete) mastery += 20;
      if (state.revisionComplete) mastery += 10;
      if (state.quizPassed) mastery += 20;
      if (state.pyqAttempted) mastery += 20;
      if (state.testPassed) mastery += 30;
    } else {
      // Redistribute PYQ weight proportionally (25 / 15 / 25 / 35)
      if (state.notesComplete) mastery += 25;
      if (state.revisionComplete) mastery += 15;
      if (state.quizPassed) mastery += 25;
      if (state.testPassed) mastery += 35;
    }
    return Math.min(100, Math.round(mastery));
  }

  function refreshUI() {
    const state = loadProgress();
    const mastery = calculateMastery(state);

    const fillEl = document.querySelector('.topic-progress-fill');
    const pctEl = document.querySelector('.topic-progress-pct');

    if (fillEl) fillEl.style.width = mastery + '%';
    if (pctEl) pctEl.textContent = mastery + '%';

    // Update notes mark complete button if present
    const notesBtn = document.getElementById('btn-mark-notes-complete');
    if (notesBtn) {
      if (state.notesComplete) {
        notesBtn.classList.add('completed');
        notesBtn.innerHTML = '✓ नोट्स पूर्ण पढ़े गए (Completed)';
      } else {
        notesBtn.classList.remove('completed');
        notesBtn.innerHTML = 'मार्क नोट्स पूर्ण (Mark Completed)';
      }
    }

    // Update revision mark complete button if present
    const revBtn = document.getElementById('btn-mark-rev-complete');
    if (revBtn) {
      if (state.revisionComplete) {
        revBtn.classList.add('completed');
        revBtn.innerHTML = '✓ पुनरावृत्ति पूर्ण (Revision Completed)';
      } else {
        revBtn.classList.remove('completed');
        revBtn.innerHTML = 'मार्क पुनरावृत्ति पूर्ण (Mark Revision Done)';
      }
    }
  }

  const TopicProgress = {
    get: loadProgress,
    save: saveProgress,
    set: function (key, value) {
      const state = loadProgress();
      state[key] = value;
      saveProgress(state);
      refreshUI();
    },
    calculateMastery: calculateMastery,
    refreshUI: refreshUI,
    canonicalPath: CANONICAL_PATH
  };

  window.TopicProgress = TopicProgress;

  document.addEventListener('DOMContentLoaded', function () {
    refreshUI();

    const notesBtn = document.getElementById('btn-mark-notes-complete');
    if (notesBtn) {
      notesBtn.addEventListener('click', function () {
        const state = loadProgress();
        TopicProgress.set('notesComplete', !state.notesComplete);
      });
    }

    const revBtn = document.getElementById('btn-mark-rev-complete');
    if (revBtn) {
      revBtn.addEventListener('click', function () {
        const state = loadProgress();
        TopicProgress.set('revisionComplete', !state.revisionComplete);
      });
    }
  });
})();
