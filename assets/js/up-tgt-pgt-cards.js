/**
 * Unified UP TGT & PGT Card Tracker Engine
 * Handles modern card-based syllabus trackers (English, Art, Commerce, Sanskrit, Biology, Civics, Education, Sociology)
 */
(function() {
  function initCardTracker() {
    const rootEl = document.querySelector('[data-tracker-key]') || document.body;
    if (rootEl.dataset.tgtPgtTrackerReady) return;
    rootEl.dataset.tgtPgtTrackerReady = 'true';
    let storageKey = rootEl.getAttribute('data-tracker-key');
    if (!storageKey) {
      if (typeof window.TRACKER_STORAGE_KEY === 'string') {
        storageKey = window.TRACKER_STORAGE_KEY;
      } else {
        const pathSlug = window.location.pathname.replace(/^\/|\/$/g, '').replace(/\//g, '_');
        storageKey = 'sjmaths_' + (pathSlug || 'card_tracker') + '_tracker_v1';
      }
    }

    const categoryModes = {};
    const categoryKeys = { branch: 'branch', section: 'officialSection', area: 'area', unit: 'unit', point: 'point' };
    Object.keys(categoryKeys).forEach(key => {
      const buttons = document.querySelectorAll('#' + key + 'Filters button');
      if (!buttons.length) return;
      categoryModes[key] = 'all';
      buttons.forEach(button => button.addEventListener('click', () => {
        categoryModes[key] = button.dataset[key];
        buttons.forEach(other => {
          other.classList.toggle('active', other === button);
          other.setAttribute('aria-pressed', String(other === button));
        });
        applyFilters();
      }));
    });
    const matchesCategory = card => Object.entries(categoryModes).every(([key, mode]) => mode === 'all' || card.dataset[categoryKeys[key]] === mode);
    const categoryActive = () => Object.values(categoryModes).some(mode => mode !== 'all');
    let progressMode = 'all';
    let relevanceMode = 'all';

    const topics = [...document.querySelectorAll('.topic')];
    const searchEl = document.getElementById('search');
    const emptyEl = document.getElementById('emptyState') || document.getElementById('empty');

    let memoryProgress = {};
    let memoryOnly = false;
    function loadProgress() {
      if (memoryOnly) return memoryProgress;
      try {
        const parsed = JSON.parse(localStorage.getItem(storageKey) || '{}');
        memoryProgress = parsed && typeof parsed === 'object' && !Array.isArray(parsed) ? parsed : {};
        return memoryProgress;
      } catch (e) {
        return memoryProgress;
      }
    }

    function saveProgress(data) {
      memoryProgress = data;
      try {
        localStorage.setItem(storageKey, JSON.stringify(data));
      } catch (e) { memoryOnly = true; }
    }

    function pct(a, b) {
      return b ? Math.round((a / b) * 100) : 0;
    }

    function restoreProgress() {
      const data = loadProgress();
      topics.forEach(topic => {
        const checked = !!data[topic.dataset.key];
        const chk = topic.querySelector('.topic-check');
        if (chk) chk.checked = checked;
        topic.classList.toggle('done', checked);
      });
      updateProgress();
    }

    topics.forEach(topic => {
      const chk = topic.querySelector('.topic-check');
      if (chk) {
        chk.addEventListener('change', e => {
          const data = loadProgress();
          if (e.target.checked) data[topic.dataset.key] = true;
          else delete data[topic.dataset.key];
          saveProgress(data);
          topic.classList.toggle('done', e.target.checked);
          updateProgress();
          applyFilters();
        });
      }
    });

    document.querySelectorAll('.section-head').forEach(head => {
      head.addEventListener('click', () => {
        const card = head.closest('.section-card');
        if (card) {
          card.classList.toggle('open');
          head.setAttribute('aria-expanded', String(card.classList.contains('open')));
        }
      });
    });

    function updateProgress() {
      const data = loadProgress();
      const done = topics.filter(t => data[t.dataset.key]).length;
      const percent = pct(done, topics.length);

      const pctEl = document.getElementById('progressPercent');
      if (pctEl) pctEl.textContent = percent + '%';

      const completedCountEl = document.getElementById('completedCount');
      if (completedCountEl) completedCountEl.textContent = done;

      const doneStatEl = document.getElementById('doneStat');
      if (doneStatEl) doneStatEl.textContent = done;

      const pendingStatEl = document.getElementById('pendingStat');
      if (pendingStatEl) pendingStatEl.textContent = topics.length - done;

      const barEl = document.getElementById('progressBar');
      if (barEl) barEl.style.width = percent + '%';

      document.querySelectorAll('.section-card').forEach(card => {
        const own = [...card.querySelectorAll('.topic')];
        const ownDone = own.filter(t => data[t.dataset.key]).length;
        const ownPct = pct(ownDone, own.length);

        document.querySelectorAll(`[data-section-done="${card.id}"]`).forEach(el => { el.textContent = ownDone; });
        document.querySelectorAll(`[data-section-bar="${card.id}"]`).forEach(el => { el.style.width = ownPct + '%'; });
        document.querySelectorAll(`[data-nav-pct="${card.id}"]`).forEach(el => { el.textContent = ownPct + '%'; });
      });
    }

    function applyFilters() {
      const q = searchEl ? searchEl.value.trim().toLowerCase() : '';
      const data = loadProgress();
      let any = false;

      document.querySelectorAll('.section-card').forEach(card => {
        let visibleCard = false;
        card.querySelectorAll('.topic').forEach(topic => {
          const done = !!data[topic.dataset.key];
          const searchAttr = topic.dataset.search?.toLowerCase() || '';
          const matchesSearch = !q || searchAttr.includes(q) || topic.textContent.toLowerCase().includes(q);
          const matchesProgress = progressMode === 'all' || (progressMode === 'done' && done) || (progressMode === 'pending' && !done);
          const matchesRelevance = relevanceMode === 'all' || topic.dataset.relevance === relevanceMode;
          const visible = matchesCategory(card) && matchesSearch && matchesProgress && matchesRelevance;
          topic.hidden = !visible;
          if (visible) {
            visibleCard = true;
            any = true;
          }
        });
        card.hidden = !visibleCard;
        if ((q || progressMode !== 'all' || relevanceMode !== 'all' || categoryActive()) && visibleCard) {
          card.classList.add('open');
          const head = card.querySelector('.section-head');
          if (head) head.setAttribute('aria-expanded', 'true');
        }
      });

      // Optional table rows search support for commerce / education / civics / sociology
      document.querySelectorAll('#topicTable tr').forEach(r => {
        const sAttr = r.dataset.search?.toLowerCase() || '';
        r.style.display = (!q || sAttr.includes(q) || r.textContent.toLowerCase().includes(q)) ? '' : 'none';
      });

      if (emptyEl) {
        emptyEl.style.display = any ? 'none' : 'block';
      }
    }

    if (searchEl) {
      searchEl.addEventListener('input', applyFilters);
    }

    document.querySelectorAll('#progressFilters button').forEach(btn => {
      btn.addEventListener('click', () => {
        progressMode = btn.dataset.progress;
        document.querySelectorAll('#progressFilters button').forEach((b) => { b.classList.toggle('active', b === btn); b.setAttribute('aria-pressed', String(b === btn)); });
        applyFilters();
      });
    });

    document.querySelectorAll('#relevanceFilters button').forEach(btn => {
      btn.addEventListener('click', () => {
        relevanceMode = btn.dataset.relevance;
        document.querySelectorAll('#relevanceFilters button').forEach((b) => { b.classList.toggle('active', b === btn); b.setAttribute('aria-pressed', String(b === btn)); });
        applyFilters();
      });
    });

    const expandAllBtn = document.getElementById('expandAll');
    if (expandAllBtn) {
      expandAllBtn.addEventListener('click', e => {
        const cards = [...document.querySelectorAll('.section-card:not([hidden])')];
        const shouldOpen = cards.some(c => !c.classList.contains('open'));
        cards.forEach(c => {
          c.classList.toggle('open', shouldOpen);
          const head = c.querySelector('.section-head');
          if (head) head.setAttribute('aria-expanded', String(shouldOpen));
        });
        e.currentTarget.textContent = shouldOpen ? 'Collapse all' : 'Expand all';
      });
    }

    window.addEventListener('storage', event => {
      if (event.key === storageKey || event.key === null) {
        memoryOnly = false;
        restoreProgress();
        applyFilters();
      }
    });
    restoreProgress();
    applyFilters();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initCardTracker);
  } else {
    initCardTracker();
  }
})();
