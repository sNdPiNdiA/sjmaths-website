/**
 * SJMaths — IB DP Mathematics Analysis & Approaches Higher Level (AA HL)
 * Interactive UI/UX Enhancements: Tier Filters, Markscheme Badges, Formula Copier,
 * Practice Tracker, Quiz Option Highlighting, and Hub Search.
 */
(function () {
  'use strict';

  // Helper to show non-intrusive toast notifications
  function showToast(message) {
    const existing = document.querySelector('.hl-toast');
    if (existing) existing.remove();

    const toast = document.createElement('div');
    toast.className = 'hl-toast';
    toast.setAttribute('role', 'alert');
    toast.innerHTML = `<i class="fa-solid fa-circle-check" style="color:#22c55e;"></i> <span>${message}</span>`;
    document.body.appendChild(toast);

    setTimeout(() => {
      toast.style.opacity = '0';
      toast.style.transform = 'translateY(10px)';
      toast.style.transition = 'all 0.25s ease';
      setTimeout(() => toast.remove(), 260);
    }, 2400);
  }

  // 1. Transform IB mark codes like [M1], [A1], [R1], [AG] into styled badges
  function initMarkschemeBadges() {
    const solutions = document.querySelectorAll('.solution-content, .markscheme-content');
    if (!solutions.length) return;

    solutions.forEach(solution => {
      if (solution.dataset.marksFormatted === 'true') return;
      solution.dataset.marksFormatted = 'true';

      // Traverse text nodes to safely replace marks without breaking KaTeX or HTML
      const walker = document.createTreeWalker(solution, NodeFilter.SHOW_TEXT, null, false);
      const nodesToReplace = [];
      let node;

      while ((node = walker.nextNode())) {
        // Skip text inside KaTeX elements
        if (node.parentElement && node.parentElement.closest('.katex, .katex-html, math, script, style')) {
          continue;
        }
        if (/\[(M[0-9]|A[0-9]|R[0-9]|AG)\]/i.test(node.nodeValue)) {
          nodesToReplace.push(node);
        }
      }

      nodesToReplace.forEach(textNode => {
        const span = document.createElement('span');
        span.innerHTML = textNode.nodeValue.replace(/\[(M[0-9]|A[0-9]|R[0-9]|AG)\]/gi, (match, code) => {
          const upper = code.toUpperCase();
          let cls = 'ib-mark-m';
          if (upper.startsWith('A') && upper !== 'AG') cls = 'ib-mark-a';
          else if (upper.startsWith('R')) cls = 'ib-mark-r';
          else if (upper === 'AG') cls = 'ib-mark-ag';
          return `<span class="ib-mark-pill ${cls}" title="IB Examiner Mark: ${upper}">${upper}</span>`;
        });
        textNode.parentNode.replaceChild(span, textNode);
      });
    });
  }

  // 2. Practice Exercises: Tier Filter Bar & "Mark as Solved" Progress Tracker
  function initPracticeTracker() {
    const practicePanel = document.getElementById('tab-practice');
    if (!practicePanel) return;

    const exerciseCards = Array.from(practicePanel.querySelectorAll('.exercise-card, .exercise-item'));
    if (!exerciseCards.length) return;

    const storageKey = 'sjmaths_ib_hl_solved_' + window.location.pathname.replace(/\/$/, '');
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

    // Create or find controls bar
    let controlsBar = practicePanel.querySelector('.practice-controls-bar');
    if (!controlsBar) {
      controlsBar = document.createElement('div');
      controlsBar.className = 'practice-controls-bar';

      const filterGroup = document.createElement('div');
      filterGroup.className = 'practice-filter-group';
      filterGroup.innerHTML = `
        <button type="button" class="practice-filter-btn active" data-filter="all">All (${exerciseCards.length})</button>
        <button type="button" class="practice-filter-btn" data-filter="tier-1">🟢 Core</button>
        <button type="button" class="practice-filter-btn" data-filter="tier-2">🟡 Standard</button>
        <button type="button" class="practice-filter-btn" data-filter="tier-3">🔴 AHL Hard</button>
      `;

      const progressPill = document.createElement('div');
      progressPill.className = 'practice-progress-pill';
      progressPill.id = 'practice-progress-pill';

      controlsBar.appendChild(filterGroup);
      controlsBar.appendChild(progressPill);

      const firstHeader = practicePanel.querySelector('h2');
      if (firstHeader && firstHeader.nextElementSibling) {
        firstHeader.parentNode.insertBefore(controlsBar, firstHeader.nextElementSibling.nextElementSibling);
      } else {
        practicePanel.prepend(controlsBar);
      }

      // Filter click handlers
      filterGroup.querySelectorAll('.practice-filter-btn').forEach(btn => {
        btn.addEventListener('click', function () {
          filterGroup.querySelectorAll('.practice-filter-btn').forEach(b => b.classList.remove('active'));
          this.classList.add('active');

          const filter = this.getAttribute('data-filter');
          exerciseCards.forEach(card => {
            if (filter === 'all') {
              card.style.display = '';
            } else if (filter === 'tier-1') {
              const isMatch = card.querySelector('.tier-1, .badge-core') || /exercise\s*(1|2|3)\b/i.test(card.textContent);
              card.style.display = isMatch ? '' : 'none';
            } else if (filter === 'tier-2') {
              const isMatch = card.querySelector('.tier-2, .badge-standard') || /exercise\s*(4|5|6|7)\b/i.test(card.textContent);
              card.style.display = isMatch ? '' : 'none';
            } else if (filter === 'tier-3') {
              const isMatch = card.querySelector('.tier-3, .badge-challenge') || /exercise\s*(8|9|10)\b/i.test(card.textContent);
              card.style.display = isMatch ? '' : 'none';
            }
          });
        });
      });
    }

    function updateProgress() {
      const progressEl = document.getElementById('practice-progress-pill');
      if (progressEl) {
        const total = exerciseCards.length;
        const solved = solvedSet.size;
        const percent = Math.round((solved / total) * 100);
        progressEl.innerHTML = `<i class="fa-solid fa-list-check"></i> <span>Solved: <strong>${solved}</strong> / ${total} (${percent}%)</span>`;
      }
    }

    // Add checkbox to each card
    exerciseCards.forEach((card, idx) => {
      const exerciseId = card.id || `ex-${idx + 1}`;
      const isSolved = solvedSet.has(exerciseId);
      card.classList.toggle('exercise-completed', isSolved);

      const header = card.querySelector('.exercise-header');
      if (header && !header.querySelector('.exercise-solve-toggle')) {
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
            showToast(`Exercise ${idx + 1} marked as completed!`);
          } else {
            solvedSet.delete(exerciseId);
            card.classList.remove('exercise-completed');
            toggleLabel.querySelector('span').textContent = 'Mark Solved';
          }
          saveSolved();
          updateProgress();
        });

        header.appendChild(toggleLabel);
      }
    });

    updateProgress();
  }

  // 3. Formula Sheet: One-click "Copy LaTeX" Button
  function initFormulaCopier() {
    const formulaCards = document.querySelectorAll('.formula-card');
    if (!formulaCards.length) return;

    formulaCards.forEach(card => {
      if (card.querySelector('.btn-copy-formula')) return;

      // Extract raw formula text or math expression
      let formulaText = '';
      const textContent = card.innerText || card.textContent || '';
      
      // Look for $$...$$ pattern in HTML
      const mathMatch = card.innerHTML.match(/\$\$([^$]+)\$\$/) || card.innerHTML.match(/\$([^$]+)\$/);
      if (mathMatch) {
        formulaText = mathMatch[1].trim();
      } else {
        const katexElem = card.querySelector('.katex-mathml annotation[encoding="application/x-tex"]');
        if (katexElem) {
          formulaText = katexElem.textContent.trim();
        } else {
          formulaText = textContent.split('\n')[1] || textContent;
        }
      }

      if (!formulaText) return;

      const copyBtn = document.createElement('button');
      copyBtn.type = 'button';
      copyBtn.className = 'btn-copy-formula';
      copyBtn.setAttribute('aria-label', 'Copy formula LaTeX');
      copyBtn.innerHTML = '<i class="fa-regular fa-copy" aria-hidden="true"></i> <span>Copy</span>';

      copyBtn.addEventListener('click', function () {
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(formulaText).then(() => {
            copyBtn.innerHTML = '<i class="fa-solid fa-check" style="color:#22c55e;"></i> <span>Copied!</span>';
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

  // 4. Mini Test: Interactive Option Highlighting on Click
  function initQuizHighlights() {
    const radioInputs = document.querySelectorAll('.quiz-option input[type="radio"], .quiz-option-label input[type="radio"]');
    if (!radioInputs.length) return;

    radioInputs.forEach(radio => {
      radio.addEventListener('change', function () {
        const card = this.closest('.quiz-card, .quiz-question-card');
        if (!card) return;

        card.querySelectorAll('.quiz-option, .quiz-option-label').forEach(opt => {
          opt.classList.remove('active-selected');
        });

        const label = this.closest('.quiz-option, .quiz-option-label');
        if (label && this.checked) {
          label.classList.add('active-selected');
        }
      });
    });
  }

  // 5. AA HL Hub Page Quick Filter / Search
  function initHubSearch() {
    const topicsGrid = document.querySelector('.topics-grid');
    if (!topicsGrid) return;

    // Check if on the main AA HL hub page
    const sectionHeader = document.querySelector('#topics .section-header');
    if (!sectionHeader || document.getElementById('hl-hub-search')) return;

    const searchWrap = document.createElement('div');
    searchWrap.style.cssText = 'margin: 1rem 0 1.5rem; max-width: 500px; position: relative;';
    searchWrap.innerHTML = `
      <div style="position:relative; display:flex; align-items:center;">
        <i class="fa-solid fa-magnifying-glass" style="position:absolute; left:1rem; color:var(--hl-text-muted); pointer-events:none;"></i>
        <input type="search" id="hl-hub-search" placeholder="Search topics, e.g. induction, vectors, differential..." 
          style="width:100%; padding:0.75rem 1rem 0.75rem 2.6rem; border-radius:12px; border:1px solid var(--hl-border); background:var(--hl-surface); color:var(--hl-text); font-size:0.92rem; outline:none; transition:all 0.2s ease;">
      </div>
    `;

    sectionHeader.parentNode.insertBefore(searchWrap, topicsGrid);

    const input = document.getElementById('hl-hub-search');
    if (input) {
      input.addEventListener('focus', () => {
        input.style.borderColor = 'var(--hl-primary)';
        input.style.boxShadow = '0 0 0 3px var(--hl-primary-glow)';
      });
      input.addEventListener('blur', () => {
        input.style.borderColor = 'var(--hl-border)';
        input.style.boxShadow = 'none';
      });

      input.addEventListener('input', function () {
        const query = this.value.toLowerCase().trim();
        const cards = topicsGrid.querySelectorAll('.topic-card-col');

        cards.forEach(col => {
          const text = col.textContent.toLowerCase();
          col.style.display = (!query || text.includes(query)) ? '' : 'none';
        });
      });
    }
  }

  // Initialize on load
  function init() {
    initMarkschemeBadges();
    initPracticeTracker();
    initFormulaCopier();
    initQuizHighlights();
    initHubSearch();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init, { once: true });
  } else {
    init();
  }
})();
