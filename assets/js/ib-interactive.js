/**
 * SJMaths — Universal IB Mathematics Interactive Engine
 * Powers DP (AA SL, AI SL, AI HL), MYP, Command Terms, IA Guide, and Hubs.
 * Features: Markscheme Badges, Tier Filtering, Practice Tracker, Formula Copier,
 * Radio Quiz Glow, Hub Search, Command Terms Live Filter, and IA Score Calculator.
 */
(function () {
  'use strict';

  // =========================================================================
  // 1. NON-INTRUSIVE FLOATING TOAST NOTIFICATION
  // =========================================================================
  function showToast(message) {
    const existing = document.querySelector('.ib-toast-notification');
    if (existing) existing.remove();

    const toast = document.createElement('div');
    toast.className = 'ib-toast-notification';
    toast.setAttribute('role', 'alert');
    toast.innerHTML = `<i class="fa-solid fa-circle-check" style="color:#10b981;"></i> <span>${message}</span>`;
    document.body.appendChild(toast);

    setTimeout(() => {
      toast.style.opacity = '0';
      toast.style.transform = 'translateY(12px)';
      toast.style.transition = 'all 0.25s ease';
      setTimeout(() => toast.remove(), 260);
    }, 2400);
  }

  // =========================================================================
  // 2. IB MARKSCHEME & MYP CRITERIA BADGE PILL REPLACER
  // =========================================================================
  function initMarkschemeBadges() {
    const containers = document.querySelectorAll(
      '.solution-content, .markscheme-content, .solution-body, .markscheme, .practice-solution, .worked-solution, .solution-steps'
    );
    if (!containers.length) return;

    containers.forEach(container => {
      if (container.dataset.marksFormatted === 'true') return;
      container.dataset.marksFormatted = 'true';

      const walker = document.createTreeWalker(container, NodeFilter.SHOW_TEXT, null, false);
      const nodesToReplace = [];
      let node;

      while ((node = walker.nextNode())) {
        if (node.parentElement && node.parentElement.closest('.katex, .katex-html, math, script, style, .ib-mark-pill')) {
          continue;
        }
        if (/\[(M[0-9]|A[0-9]|R[0-9]|AG|G[0-9]|P[0-9]|C[0-9]|Crit\s*[A-D]|Criterion\s*[A-D])\]/i.test(node.nodeValue)) {
          nodesToReplace.push(node);
        }
      }

      nodesToReplace.forEach(textNode => {
        const span = document.createElement('span');
        span.innerHTML = textNode.nodeValue.replace(
          /\[(M[0-9]|A[0-9]|R[0-9]|AG|G[0-9]|P[0-9]|C[0-9]|Crit\s*[A-D]|Criterion\s*[A-D])\]/gi,
          (match, code) => {
            const clean = code.trim().toUpperCase().replace(/\s+/g, ' ');
            let cls = 'ib-mark-m';
            let title = `IB Mark: ${clean}`;

            if (clean.startsWith('A') && clean !== 'AG') {
              cls = 'ib-mark-a';
              title = `Accuracy / Answer Mark: ${clean}`;
            } else if (clean.startsWith('R')) {
              cls = 'ib-mark-r';
              title = `Reasoning Mark: ${clean}`;
            } else if (clean === 'AG') {
              cls = 'ib-mark-ag';
              title = 'Answer Given (Proof Goal Reached)';
            } else if (clean.startsWith('G')) {
              cls = 'ib-mark-g';
              title = `Graphic Display Calculator Mark: ${clean}`;
            } else if (clean.startsWith('P')) {
              cls = 'ib-mark-p';
              title = `Process Mark: ${clean}`;
            } else if (clean.startsWith('C') && !clean.includes('CRIT')) {
              cls = 'ib-mark-c';
              title = `Communication Mark: ${clean}`;
            } else if (clean.includes('CRIT')) {
              cls = 'ib-crit-pill';
              title = `MYP Assessment: ${clean}`;
            }

            return `<span class="ib-mark-pill ${cls}" title="${title}">${clean}</span>`;
          }
        );
        textNode.parentNode.replaceChild(span, textNode);
      });
    });
  }

  // =========================================================================
  // 3. UNIVERSAL PRACTICE TIER FILTER & "MARK AS SOLVED" TRACKER
  // =========================================================================
  function initPracticeTracker() {
    const practicePanel =
      document.getElementById('pane-practice') ||
      document.getElementById('tab-practice') ||
      document.querySelector('.practice-section, #practice');
    if (!practicePanel) return;

    const cards = Array.from(
      practicePanel.querySelectorAll('.exercise-card, .exercise-item, .practice-item')
    );
    if (!cards.length) return;

    const isMYP = window.location.pathname.includes('/myp-mathematics/');
    const storageKey = 'sjmaths_ib_solved_' + window.location.pathname.replace(/\/$/, '');
    let solvedSet = new Set();
    try {
      const saved = localStorage.getItem(storageKey);
      if (saved) solvedSet = new Set(JSON.parse(saved));
    } catch (e) {}

    function saveSolved() {
      try {
        localStorage.setItem(storageKey, JSON.stringify(Array.from(solvedSet)));
      } catch (e) {}
    }

    // Insert controls bar if not present
    let controlsBar = practicePanel.querySelector('.practice-controls-bar');
    if (!controlsBar) {
      controlsBar = document.createElement('div');
      controlsBar.className = 'practice-controls-bar';

      const filterGroup = document.createElement('div');
      filterGroup.className = 'practice-filter-group';

      if (isMYP) {
        filterGroup.innerHTML = `
          <button type="button" class="practice-filter-btn active" data-filter="all">All (${cards.length})</button>
          <button type="button" class="practice-filter-btn" data-filter="tier-1">🟢 Standard</button>
          <button type="button" class="practice-filter-btn" data-filter="tier-2">🟡 Extended</button>
          <button type="button" class="practice-filter-btn" data-filter="tier-3">🔴 Challenge</button>
        `;
      } else {
        filterGroup.innerHTML = `
          <button type="button" class="practice-filter-btn active" data-filter="all">All (${cards.length})</button>
          <button type="button" class="practice-filter-btn" data-filter="tier-1">🟢 Core</button>
          <button type="button" class="practice-filter-btn" data-filter="tier-2">🟡 Standard</button>
          <button type="button" class="practice-filter-btn" data-filter="tier-3">🔴 Challenge</button>
        `;
      }

      const progressPill = document.createElement('div');
      progressPill.className = 'practice-progress-pill';
      progressPill.id = 'practice-progress-pill';

      controlsBar.appendChild(filterGroup);
      controlsBar.appendChild(progressPill);

      const header = practicePanel.querySelector('h2, .test-header-card, .section-header');
      if (header && header.nextElementSibling) {
        header.parentNode.insertBefore(controlsBar, header.nextElementSibling);
      } else {
        practicePanel.prepend(controlsBar);
      }

      filterGroup.querySelectorAll('.practice-filter-btn').forEach(btn => {
        btn.addEventListener('click', function () {
          filterGroup.querySelectorAll('.practice-filter-btn').forEach(b => b.classList.remove('active'));
          this.classList.add('active');

          const filter = this.getAttribute('data-filter');
          cards.forEach((card, idx) => {
            if (filter === 'all') {
              card.style.display = '';
            } else if (filter === 'tier-1') {
              const match = card.querySelector('.tier-1, .badge-core, .badge-standard, .tier-standard') || idx < 3;
              card.style.display = match ? '' : 'none';
            } else if (filter === 'tier-2') {
              const match = card.querySelector('.tier-2, .badge-standard, .badge-extended, .tier-extended') || (idx >= 3 && idx < 7);
              card.style.display = match ? '' : 'none';
            } else if (filter === 'tier-3') {
              const match = card.querySelector('.tier-3, .badge-challenge, .tier-challenge') || idx >= 7;
              card.style.display = match ? '' : 'none';
            }
          });
        });
      });
    }

    function updateProgress() {
      const progressEl = document.getElementById('practice-progress-pill');
      if (progressEl) {
        const total = cards.length;
        const solved = solvedSet.size;
        const percent = Math.round((solved / total) * 100);
        progressEl.innerHTML = `<i class="fa-solid fa-list-check"></i> <span>Solved: <strong>${solved}</strong> / ${total} (${percent}%)</span>`;
      }
    }

    // Attach checkbox to each card
    cards.forEach((card, idx) => {
      const exerciseId = card.id || `ex-${idx + 1}`;
      const isSolved = solvedSet.has(exerciseId);
      card.classList.toggle('exercise-completed', isSolved);

      const header = card.querySelector('.exercise-header, .practice-header, h3, h4');
      if (header && !card.querySelector('.exercise-solve-toggle')) {
        const toggleLabel = document.createElement('label');
        toggleLabel.className = 'exercise-solve-toggle';
        toggleLabel.innerHTML = `
          <input type="checkbox" ${isSolved ? 'checked' : ''} aria-label="Mark exercise ${idx + 1} as solved">
          <span>${isSolved ? 'Solved ✓' : 'Mark Solved'}</span>
        `;

        const checkbox = toggleLabel.querySelector('input');
        checkbox.addEventListener('change', function () {
          if (this.checked) {
            solvedSet.add(exerciseId);
            card.classList.add('exercise-completed');
            toggleLabel.querySelector('span').textContent = 'Solved ✓';
            showToast(`Exercise ${idx + 1} marked as solved!`);
          } else {
            solvedSet.delete(exerciseId);
            card.classList.remove('exercise-completed');
            toggleLabel.querySelector('span').textContent = 'Mark Solved';
          }
          saveSolved();
          updateProgress();
        });

        if (header.classList.contains('exercise-header') || header.classList.contains('practice-header')) {
          header.appendChild(toggleLabel);
        } else {
          header.parentNode.insertBefore(toggleLabel, header.nextSibling);
        }
      }
    });

    updateProgress();
  }

  // =========================================================================
  // 4. ONE-CLICK FORMULA COPIER WITH TOAST
  // =========================================================================
  function initFormulaCopier() {
    const formulaCards = document.querySelectorAll(
      '.formula-card, .formula-block, .formula-item, .formula-box'
    );
    if (!formulaCards.length) return;

    formulaCards.forEach(card => {
      if (card.querySelector('.btn-copy-formula')) return;

      let formulaText = '';
      const mathMatch = card.innerHTML.match(/\$\$([^$]+)\$\$/) || card.innerHTML.match(/\$([^$]+)\$/);
      if (mathMatch) {
        formulaText = mathMatch[1].trim();
      } else {
        const katexElem = card.querySelector('.katex-mathml annotation[encoding="application/x-tex"]');
        if (katexElem) {
          formulaText = katexElem.textContent.trim();
        } else {
          formulaText = (card.innerText || card.textContent || '').trim();
        }
      }

      if (!formulaText) return;

      const copyBtn = document.createElement('button');
      copyBtn.type = 'button';
      copyBtn.className = 'btn-copy-formula';
      copyBtn.setAttribute('aria-label', 'Copy formula to clipboard');
      copyBtn.innerHTML = '<i class="fa-regular fa-copy" aria-hidden="true"></i> <span>Copy</span>';

      copyBtn.addEventListener('click', function (e) {
        e.stopPropagation();
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(formulaText).then(() => {
            copyBtn.innerHTML = '<i class="fa-solid fa-check" style="color:#10b981;"></i> <span>Copied!</span>';
            showToast('Formula copied to clipboard!');
            setTimeout(() => {
              copyBtn.innerHTML = '<i class="fa-regular fa-copy" aria-hidden="true"></i> <span>Copy</span>';
            }, 2000);
          }).catch(() => {
            showToast('Unable to copy formula.');
          });
        }
      });

      card.appendChild(copyBtn);
    });
  }

  // =========================================================================
  // 5. MINI TEST OPTION CLICK-SELECTION GLOW
  // =========================================================================
  function initQuizHighlights() {
    const radioInputs = document.querySelectorAll(
      '.quiz-option input[type="radio"], .quiz-option-label input[type="radio"], .mcq-option input[type="radio"], .quiz-choice input[type="radio"]'
    );

    radioInputs.forEach(radio => {
      radio.addEventListener('change', function () {
        const card = this.closest('.quiz-card, .quiz-question-card, .mcq-card, .quiz-question');
        if (!card) return;

        card.querySelectorAll('.quiz-option, .quiz-option-label, .mcq-option, .quiz-choice').forEach(opt => {
          opt.classList.remove('active-selected');
        });

        const label = this.closest('.quiz-option, .quiz-option-label, .mcq-option, .quiz-choice');
        if (label && this.checked) {
          label.classList.add('active-selected');
        }
      });
    });
  }

  // =========================================================================
  // 6. COMMAND TERMS LIVE SEARCH & CATEGORY FILTER (ib/command-terms/)
  // =========================================================================
  function initCommandTermsPage() {
    const tables = document.querySelectorAll('.terms-table');
    if (!tables.length) return;

    const mainContainer = document.querySelector('.hub-container, #main-content');
    if (!mainContainer || document.getElementById('cmd-terms-search-box')) return;

    const filterBox = document.createElement('div');
    filterBox.id = 'cmd-terms-search-box';
    filterBox.className = 'ib-command-terms-toolbar';
    filterBox.style.cssText = 'margin: 1.5rem 0 2rem; padding: 1.25rem; border-radius: 16px; background: var(--c-surface-elevated, #fff); border: 1px solid var(--c-border); box-shadow: var(--shadow-sm);';

    filterBox.innerHTML = `
      <div style="display:flex; flex-direction:column; gap:1rem;">
        <div style="position:relative; width:100%;">
          <i class="fa-solid fa-magnifying-glass" style="position:absolute; left:1rem; top:50%; transform:translateY(-50%); color:var(--c-text-muted); pointer-events:none;"></i>
          <input type="search" id="cmd-search-input" placeholder="Search command terms (e.g. show that, deduce, calculate, hence, justify)..." 
            style="width:100%; box-sizing:border-box; padding:0.85rem 1rem 0.85rem 2.8rem; border-radius:12px; border:1px solid var(--c-border); background:var(--c-surface); color:var(--c-text); font-size:0.95rem; outline:none; transition:all 0.2s;">
        </div>
        <div style="display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:0.75rem;">
          <div class="cmd-category-filters" style="display:flex; flex-wrap:wrap; gap:0.4rem;">
            <button type="button" class="cmd-filter-pill active" data-cat="all">All Terms</button>
            <button type="button" class="cmd-filter-pill" data-cat="recall">⚡ Recall</button>
            <button type="button" class="cmd-filter-pill" data-cat="calculate">🧮 Compute</button>
            <button type="button" class="cmd-filter-pill" data-cat="justify">⚖️ Reason</button>
            <button type="button" class="cmd-filter-pill" data-cat="describe">💬 Describe</button>
            <button type="button" class="cmd-filter-pill" data-cat="graphs">📐 Graphs</button>
          </div>
          <span id="cmd-terms-count" style="font-size:0.82rem; font-weight:700; color:var(--c-text-muted);">Showing all terms</span>
        </div>
      </div>
    `;

    const firstSection = mainContainer.querySelector('.hub-section');
    if (firstSection) {
      firstSection.parentNode.insertBefore(filterBox, firstSection);
    } else {
      mainContainer.prepend(filterBox);
    }

    const searchInput = document.getElementById('cmd-search-input');
    const countDisplay = document.getElementById('cmd-terms-count');
    const filterPills = filterBox.querySelectorAll('.cmd-filter-pill');

    // Style filter pills
    filterPills.forEach(pill => {
      pill.style.cssText =
        'padding:0.35rem 0.8rem; border-radius:9999px; border:1px solid var(--c-border); background:var(--c-surface-muted); color:var(--c-text-secondary); font-size:0.78rem; font-weight:700; cursor:pointer; transition:all 0.15s;';
    });

    const activePill = filterBox.querySelector('.cmd-filter-pill.active');
    if (activePill) {
      activePill.style.background = 'var(--c-primary, #047857)';
      activePill.style.color = '#fff';
      activePill.style.borderColor = 'var(--c-primary, #047857)';
    }

    const sections = Array.from(document.querySelectorAll('.hub-section'));
    const rows = Array.from(document.querySelectorAll('.terms-table tbody tr'));

    // Add copy button to each row
    rows.forEach(row => {
      const termCell = row.querySelector('.term-name');
      if (termCell && !termCell.querySelector('.cmd-copy-btn')) {
        const termName = (termCell.innerText || termCell.textContent || '').trim();
        const defCell = row.querySelector('.term-def');
        const defText = defCell ? (defCell.innerText || defCell.textContent || '').trim() : '';

        const copyBtn = document.createElement('button');
        copyBtn.type = 'button';
        copyBtn.className = 'cmd-copy-btn';
        copyBtn.title = `Copy "${termName}" definition`;
        copyBtn.innerHTML = '<i class="fa-regular fa-copy"></i>';
        copyBtn.style.cssText =
          'margin-left:0.5rem; background:none; border:none; color:var(--c-text-muted); cursor:pointer; font-size:0.8rem; padding:0.2rem; transition:color 0.15s;';

        copyBtn.addEventListener('click', e => {
          e.stopPropagation();
          const textToCopy = `${termName}: ${defText}`;
          if (navigator.clipboard) {
            navigator.clipboard.writeText(textToCopy).then(() => {
              showToast(`Copied "${termName}" definition!`);
            });
          }
        });
        termCell.appendChild(copyBtn);
      }
    });

    function applyFilters() {
      const query = searchInput ? searchInput.value.toLowerCase().trim() : '';
      const selectedCat = filterBox.querySelector('.cmd-filter-pill.active')?.getAttribute('data-cat') || 'all';

      let visibleCount = 0;
      const totalCount = rows.length;

      sections.forEach(sec => {
        const secId = sec.id || '';
        const secRows = Array.from(sec.querySelectorAll('.terms-table tbody tr'));
        let secVisibleCount = 0;

        secRows.forEach(row => {
          const rowText = (row.textContent || '').toLowerCase();
          const matchesQuery = !query || rowText.includes(query);

          let matchesCat = true;
          if (selectedCat === 'recall') matchesCat = secId.includes('recall');
          else if (selectedCat === 'calculate') matchesCat = secId.includes('calculate');
          else if (selectedCat === 'justify') matchesCat = secId.includes('justify');
          else if (selectedCat === 'describe') matchesCat = secId.includes('describe');
          else if (selectedCat === 'graphs') matchesCat = secId.includes('graphs');

          const isVisible = matchesQuery && matchesCat;
          row.style.display = isVisible ? '' : 'none';
          if (isVisible) {
            secVisibleCount++;
            visibleCount++;
          }
        });

        sec.style.display = secVisibleCount > 0 ? '' : 'none';
      });

      if (countDisplay) {
        countDisplay.textContent = `Showing ${visibleCount} of ${totalCount} terms`;
      }
    }

    if (searchInput) {
      searchInput.addEventListener('input', applyFilters);
    }

    filterPills.forEach(pill => {
      pill.addEventListener('click', function () {
        filterPills.forEach(p => {
          p.classList.remove('active');
          p.style.background = 'var(--c-surface-muted)';
          p.style.color = 'var(--c-text-secondary)';
          p.style.borderColor = 'var(--c-border)';
        });
        this.classList.add('active');
        this.style.background = 'var(--c-primary, #047857)';
        this.style.color = '#fff';
        this.style.borderColor = 'var(--c-primary, #047857)';
        applyFilters();
      });
    });
  }

  // =========================================================================
  // 7. HUB & SYLLABUS DIRECTORY LIVE SEARCH (AA SL, AI SL, AI HL, MYP, DP HUBS)
  // =========================================================================
  function initHubDirectorySearch() {
    const topicsGrid = document.querySelector('.topics-grid, .topic-overview-grid, .lessons-grid, .syllabus-grid');
    if (!topicsGrid) return;
    if (document.getElementById('ib-universal-hub-search')) return;

    const cards = Array.from(topicsGrid.children);
    if (cards.length < 3) return;

    const header = document.querySelector('.section-header, #topics .section-header, .hub-section .section-header');
    const container = header || topicsGrid.parentElement;

    const searchWrap = document.createElement('div');
    searchWrap.id = 'ib-universal-hub-search-wrap';
    searchWrap.className = 'ib-search-bar';
    searchWrap.innerHTML = `
      <i class="fa-solid fa-magnifying-glass" aria-hidden="true"></i>
      <input type="search" id="ib-universal-hub-search" placeholder="Search syllabus topics, concepts, lessons..." aria-label="Search topics">
    `;

    container.insertBefore(searchWrap, topicsGrid);

    const input = document.getElementById('ib-universal-hub-search');
    if (input) {
      input.addEventListener('input', function () {
        const query = this.value.toLowerCase().trim();
        cards.forEach(card => {
          const text = (card.textContent || '').toLowerCase();
          card.style.display = !query || text.includes(query) ? '' : 'none';
        });
      });
    }
  }

  // =========================================================================
  // 8. INTERNAL ASSESSMENT RUBRIC CALCULATOR (ib/dp-mathematics/internal-assessment/)
  // =========================================================================
  function initIACalculator() {
    const calculator = document.getElementById('ia-score-calculator') || document.querySelector('.ia-rubric-calculator');
    if (!calculator) return;

    // Enhance boundary visualizer
    const totalDisplay = calculator.querySelector('.total-score-val, #total-score');
    const gradeBadge = calculator.querySelector('.predicted-grade-pill, #predicted-grade');

    function updateGrade(total) {
      if (!gradeBadge) return;
      let grade = '1';
      let color = '#ef4444';

      if (total >= 16) { grade = 'Grade 7 (Excellent)'; color = '#10b981'; }
      else if (total >= 13) { grade = 'Grade 6 (Very Good)'; color = '#059669'; }
      else if (total >= 10) { grade = 'Grade 5 (Good)'; color = '#0284c7'; }
      else if (total >= 7) { grade = 'Grade 4 (Satisfactory)'; color = '#f59e0b'; }
      else if (total >= 4) { grade = 'Grade 3 (Mediocre)'; color = '#ea580c'; }
      else { grade = 'Grade 1-2 (Elementary)'; color = '#ef4444'; }

      gradeBadge.textContent = grade;
      gradeBadge.style.color = color;
    }

    calculator.querySelectorAll('input[type="range"], select, input[type="radio"]').forEach(input => {
      input.addEventListener('input', () => {
        let sum = 0;
        calculator.querySelectorAll('input[type="range"], select').forEach(el => {
          sum += parseInt(el.value, 10) || 0;
        });
        if (totalDisplay) totalDisplay.textContent = sum;
        updateGrade(sum);
      });
    });
  }

  // =========================================================================
  // INITIALIZATION ON DOM READY
  // =========================================================================
  function initAll() {
    initMarkschemeBadges();
    initPracticeTracker();
    initFormulaCopier();
    initQuizHighlights();
    initCommandTermsPage();
    initHubDirectorySearch();
    initIACalculator();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAll);
  } else {
    initAll();
  }
})();
