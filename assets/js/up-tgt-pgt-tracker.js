/**
 * Unified UP TGT & PGT Exam Tracker Engine
 * SJMaths - Reusable Tracker Progress & Filtering Script
 */
(function() {
  function initTracker() {
    const rootEl = document.querySelector('[data-tracker-key]') || document.body;
    if (rootEl.dataset.tgtPgtTrackerReady) return;
    rootEl.dataset.tgtPgtTrackerReady = 'true';
    let storageKey = rootEl.getAttribute('data-tracker-key');
    if (!storageKey) {
      if (typeof window.TRACKER_STORAGE_KEY === 'string') {
        storageKey = window.TRACKER_STORAGE_KEY;
      } else {
        const pathSlug = window.location.pathname.replace(/^\/|\/$/g, '').replace(/\//g, '_');
        storageKey = 'sjmaths_' + (pathSlug || 'tgt_pgt') + '_tracker_v1';
      }
    }

    const categoryModes = {};
    const categoryKeys = { branch: 'branch', section: 'officialSection', area: 'area', unit: 'unit', point: 'point' };
    Object.keys(categoryKeys).forEach(key => {
      const buttons = document.querySelectorAll('#' + key + 'Filters button');
      if (!buttons.length) return;
      categoryModes[key] = 'all';
      buttons.forEach(button => button.setAttribute('aria-pressed', String(button.classList.contains('active'))));
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
    let subjectMode = 'all';

    const topics = [...document.querySelectorAll('.topic')];
    const cards = [...document.querySelectorAll('.section-card')];
    const searchEl = document.getElementById('search');
    const emptyEl = document.getElementById('empty');

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

    function syncCounts() {
      const total = topics.length;
      const sharedTopics = topics.filter(t => t.dataset.relevance === 'shared');
      const shared = sharedTopics.length;
      const only = total - shared;

      const heroTags = document.querySelectorAll('.hero-tags .tag');
      if (heroTags.length >= 3) {
        if (heroTags[1] && heroTags[1].textContent.includes('tracked topics')) {
          heroTags[1].textContent = total + ' tracked topics';
        }
        if (heroTags[2] && heroTags[2].textContent.includes('TGT + PGT')) {
          heroTags[2].textContent = shared + ' TGT + PGT topics';
        }
      }

      const metrics = document.querySelectorAll('.metric strong');
      const hasRelevanceClassification = topics.some(topic => topic.hasAttribute('data-relevance'));
      if (hasRelevanceClassification && metrics.length >= 3) {
        metrics[0].textContent = shared;
        metrics[1].textContent = only;
        metrics[2].textContent = total;
      }

      const progressCopy = document.querySelector('.progress-copy');
      if (progressCopy) {
        progressCopy.innerHTML = '<span id="doneCount">0</span> / ' + total + '<br>topics complete';
      }

      const statPending = document.getElementById('statPending');
      if (statPending) statPending.textContent = total;

      cards.forEach(c => {
        const own = c.querySelectorAll('.topic');
        const n = own.length;
        const meta = c.querySelector('.section-meta');
        if (meta && meta.textContent.includes('syllabus topics')) {
          meta.textContent = n + ' syllabus topics';
        }
        const miniSmall = c.querySelector('.mini-progress small');
        if (miniSmall) {
          miniSmall.innerHTML = '<span data-done="' + c.id + '">0</span> / ' + n;
        }
      });
    }

    function updateProgress() {
      const data = loadProgress();
      const done = topics.filter(t => data[t.dataset.key]).length;
      const p = pct(done, topics.length);

      const overallPct = document.getElementById('overallPct');
      if (overallPct) overallPct.textContent = p + '%';

      const doneCount = document.getElementById('doneCount');
      if (doneCount) doneCount.textContent = done;

      const statDone = document.getElementById('statDone');
      if (statDone) statDone.textContent = done;

      const statPending = document.getElementById('statPending');
      if (statPending) statPending.textContent = topics.length - done;

      const overallBar = document.getElementById('overallBar');
      if (overallBar) overallBar.style.width = p + '%';

      cards.forEach(c => {
        const own = [...c.querySelectorAll('.topic')];
        const od = own.filter(t => data[t.dataset.key]).length;
        const op = pct(od, own.length);
        const id = c.id;

        document.querySelectorAll(`[data-done="${id}"]`).forEach(x => { x.textContent = od; });
        document.querySelectorAll(`[data-bar="${id}"]`).forEach(x => { x.style.width = op + '%'; });
        document.querySelectorAll(`[data-navpct="${id}"]`).forEach(x => { x.textContent = op + '%'; });
      });
    }

    function applyFilters() {
      const q = searchEl ? searchEl.value.trim().toLowerCase() : '';
      const data = loadProgress();
      let any = false;

      cards.forEach(c => {
        let cv = false;
        const smode = subjectMode === 'all' || c.dataset.subject === subjectMode;

        c.querySelectorAll('.topic').forEach(t => {
          const done = !!data[t.dataset.key];
          const searchAttr = t.dataset.search?.toLowerCase() || '';
          const textContent = t.textContent.toLowerCase();
          const sm = !q || searchAttr.includes(q) || textContent.includes(q);
          const pm = progressMode === 'all' || (progressMode === 'done' && done) || (progressMode === 'pending' && !done);
          const rm = relevanceMode === 'all' || t.dataset.relevance === relevanceMode;
          const v = matchesCategory(c) && smode && sm && pm && rm;

          t.hidden = !v;
          if (v) {
            cv = true;
            any = true;
          }
        });

        c.hidden = !cv;
        if ((q || progressMode !== 'all' || relevanceMode !== 'all' || subjectMode !== 'all' || categoryActive()) && cv) {
          c.classList.add('open');
          const head = c.querySelector('.section-head');
          if (head) head.setAttribute('aria-expanded', 'true');
        }
      });

      if (emptyEl) {
        emptyEl.style.display = any ? 'none' : 'block';
      }
    }

    function restore() {
      syncCounts();
      const data = loadProgress();
      topics.forEach(t => {
        const c = !!data[t.dataset.key];
        const chk = t.querySelector('.topic-check');
        if (chk) chk.checked = c;
        t.classList.toggle('done', c);
      });
      updateProgress();
    }

    // Event listeners
    topics.forEach(t => {
      const chk = t.querySelector('.topic-check');
      if (chk) {
        chk.addEventListener('change', ev => {
          const data = loadProgress();
          if (ev.target.checked) data[t.dataset.key] = true;
          else delete data[t.dataset.key];
          saveProgress(data);
          t.classList.toggle('done', ev.target.checked);
          updateProgress();
          applyFilters();
        });
      }
    });

    document.querySelectorAll('.section-head').forEach(h => {
      h.addEventListener('click', () => {
        const c = h.closest('.section-card');
        if (c) {
          c.classList.toggle('open');
          h.setAttribute('aria-expanded', String(c.classList.contains('open')));
        }
      });
    });

    if (searchEl) {
      searchEl.addEventListener('input', applyFilters);
    }

    document.querySelectorAll('#progressFilters button').forEach(b => {
      b.setAttribute('aria-pressed', String(b.classList.contains('active')));
      b.addEventListener('click', () => {
        progressMode = b.dataset.progress;
        document.querySelectorAll('#progressFilters button').forEach((x) => { x.classList.toggle('active', x === b); x.setAttribute('aria-pressed', String(x === b)); });
        applyFilters();
      });
    });

    document.querySelectorAll('#relevanceFilters button').forEach(b => {
      b.setAttribute('aria-pressed', String(b.classList.contains('active')));
      b.addEventListener('click', () => {
        relevanceMode = b.dataset.relevance;
        document.querySelectorAll('#relevanceFilters button').forEach((x) => { x.classList.toggle('active', x === b); x.setAttribute('aria-pressed', String(x === b)); });
        applyFilters();
      });
    });

    document.querySelectorAll('#subjectFilters button').forEach(b => {
      b.setAttribute('aria-pressed', String(b.classList.contains('active')));
      b.addEventListener('click', () => {
        subjectMode = b.dataset.subject;
        document.querySelectorAll('#subjectFilters button').forEach((x) => { x.classList.toggle('active', x === b); x.setAttribute('aria-pressed', String(x === b)); });
        applyFilters();
      });
    });

    const expandAllBtn = document.getElementById('expandAll');
    if (expandAllBtn) {
      expandAllBtn.addEventListener('click', ev => {
        const visible = cards.filter(c => !c.hidden);
        const open = visible.some(c => !c.classList.contains('open'));
        visible.forEach(c => {
          c.classList.toggle('open', open);
          const head = c.querySelector('.section-head');
          if (head) head.setAttribute('aria-expanded', String(open));
        });
        ev.currentTarget.textContent = open ? 'Collapse all' : 'Expand all';
      });
    }

    window.addEventListener('storage', event => {
      if (event.key === storageKey || event.key === null) {
        memoryOnly = false;
        restore();
        applyFilters();
      }
    });
    restore();
    applyFilters();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initTracker);
  } else {
    initTracker();
  }
})();
