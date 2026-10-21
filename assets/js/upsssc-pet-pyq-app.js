/**
 * UPSSSC PET PYQ Interactive Practice Engine
 * High-performance mobile-friendly quiz app with bilingual toggle, chapter filters,
 * bookmarking, and instant verified explanation reveal.
 */

(function () {
  'use strict';

  let subjectData = null;
  let questions = [];
  let filteredQuestions = [];
  let currentIndex = 0;
  let userResponses = {}; // { qNum: { selectedOption, isCorrect } }
  let bookmarks = new Set();
  let currentLang = 'en';
  let activeChapterId = 'all';
  let activeShift = 'all';

  function getText(val, lang) {
    if (!val) return '';
    if (typeof val === 'object') {
      if (lang === 'hi') return val.hi || val.en || '';
      return val.en || val.hi || '';
    }
    return String(val);
  }

  function renderMath(targetEl) {
    if (!targetEl) return;
    if (typeof renderMathInElement === 'function') {
      try {
        renderMathInElement(targetEl, {
          delimiters: [
            { left: '$$', right: '$$', display: true },
            { left: '$', right: '$', display: false },
            { left: '\\(', right: '\\)', display: false },
            { left: '\\[', right: '\\]', display: true }
          ],
          ignoredTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code', 'svg'],
          throwOnError: false
        });
      } catch (err) {
        console.warn('KaTeX auto-render error:', err);
      }
    } else {
      let retries = 0;
      const timer = setInterval(() => {
        retries++;
        if (typeof renderMathInElement === 'function') {
          clearInterval(timer);
          renderMath(targetEl);
        } else if (retries > 30) {
          clearInterval(timer);
        }
      }, 80);
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initApp);
  } else {
    initApp();
  }

  function initApp() {
    const dataEl = document.getElementById('pet-subject-data');
    if (!dataEl) return;

    try {
      subjectData = JSON.parse(dataEl.textContent);
      questions = subjectData.questions || [];
      filteredQuestions = [...questions];
    } catch (e) {
      console.error('Failed to parse PET subject data', e);
      return;
    }

    loadPreferences();
    setupFilters();
    setupEventListeners();
    handleHash();
    renderQuestion();
    updateProgress();

    // Trigger math rendering on the crawlable SEO archive on initial load
    if (document.readyState === 'complete') {
      renderMath(document.querySelector('.pyq-seo-archive') || document.body);
    } else {
      window.addEventListener('load', () => {
        renderMath(document.querySelector('.pyq-seo-archive') || document.body);
      });
    }

    const seoDetails = document.querySelector('.pyq-seo-details');
    if (seoDetails) {
      seoDetails.addEventListener('toggle', () => {
        if (seoDetails.open) {
          renderMath(seoDetails);
        }
      });
    }
  }

  function loadPreferences() {
    const savedLang = localStorage.getItem('preferredLang') || 'en';
    setLanguage(savedLang);

    const savedBookmarks = localStorage.getItem(`pet_bookmarks_${subjectData.subjectId}`);
    if (savedBookmarks) {
      try {
        bookmarks = new Set(JSON.parse(savedBookmarks));
      } catch (e) {}
    }

    const savedResponses = localStorage.getItem(`pet_responses_${subjectData.subjectId}`);
    if (savedResponses) {
      try {
        userResponses = JSON.parse(savedResponses);
      } catch (e) {}
    }
  }

  function setLanguage(lang) {
    currentLang = lang === 'hi' ? 'hi' : 'en';
    localStorage.setItem('preferredLang', currentLang);

    if (currentLang === 'hi') {
      document.body.classList.add('lang-mode-hi');
      document.documentElement.classList.add('lang-mode-hi');
      document.documentElement.lang = 'hi';
    } else {
      document.body.classList.remove('lang-mode-hi');
      document.documentElement.classList.remove('lang-mode-hi');
      document.documentElement.lang = 'en';
    }

    const langBtn = document.getElementById('langToggleLabel');
    if (langBtn) {
      langBtn.textContent = currentLang === 'hi' ? 'HI' : 'EN';
    }
  }

  function setupFilters() {
    const chapterFilter = document.getElementById('chapterFilterSelect');
    if (chapterFilter && subjectData.chapters) {
      chapterFilter.innerHTML = `<option value="all">All Chapters (${questions.length} MCQs)</option>`;
      subjectData.chapters.forEach(ch => {
        const opt = document.createElement('option');
        opt.value = ch.id;
        opt.textContent = `${ch.number} ${ch.title} (${ch.count} Qs)`;
        chapterFilter.appendChild(opt);
      });
      chapterFilter.addEventListener('change', (e) => {
        activeChapterId = e.target.value;
        applyFilters();
      });
    }

    const shiftFilter = document.getElementById('shiftFilterSelect');
    if (shiftFilter) {
      shiftFilter.addEventListener('change', (e) => {
        activeShift = e.target.value;
        applyFilters();
      });
    }
  }

  function applyFilters() {
    filteredQuestions = questions.filter(q => {
      const matchChapter = activeChapterId === 'all' || q.chapterId === activeChapterId;
      const matchShift = activeShift === 'all' || (q.shift && q.shift.includes(activeShift));
      return matchChapter && matchShift;
    });

    if (filteredQuestions.length === 0) {
      filteredQuestions = [...questions];
      activeChapterId = 'all';
      activeShift = 'all';
      if (document.getElementById('chapterFilterSelect')) document.getElementById('chapterFilterSelect').value = 'all';
      if (document.getElementById('shiftFilterSelect')) document.getElementById('shiftFilterSelect').value = 'all';
    }

    currentIndex = 0;
    renderQuestion();
    updateProgress();
  }

  function setupEventListeners() {
    const langBtn = document.getElementById('langToggleBtn');
    if (langBtn) {
      langBtn.addEventListener('click', () => {
        setLanguage(currentLang === 'en' ? 'hi' : 'en');
        renderQuestion();
      });
    }

    const bookmarkBtn = document.getElementById('bookmarkBtn');
    if (bookmarkBtn) {
      bookmarkBtn.addEventListener('click', toggleBookmark);
    }

    const prevBtn = document.getElementById('prevQuestionBtn');
    if (prevBtn) {
      prevBtn.addEventListener('click', () => {
        if (currentIndex > 0) {
          currentIndex--;
          renderQuestion();
          scrollToQuestionTop(true);
        }
      });
    }

    const nextBtn = document.getElementById('nextQuestionBtn');
    if (nextBtn) {
      nextBtn.addEventListener('click', () => {
        if (currentIndex < filteredQuestions.length - 1) {
          currentIndex++;
          renderQuestion();
          scrollToQuestionTop(true);
        }
      });
    }

    const inlineNextBtn = document.getElementById('inlineNextBtn');
    if (inlineNextBtn) {
      inlineNextBtn.addEventListener('click', () => {
        if (currentIndex < filteredQuestions.length - 1) {
          currentIndex++;
          renderQuestion();
          scrollToQuestionTop(true);
        }
      });
    }

    window.addEventListener('hashchange', handleHash);

    // Keyboard shortcuts
    document.addEventListener('keydown', (e) => {
      if (e.target.tagName === 'INPUT' || e.target.tagName === 'SELECT') return;
      if (e.key === 'ArrowRight') {
        if (currentIndex < filteredQuestions.length - 1) {
          currentIndex++;
          renderQuestion();
          scrollToQuestionTop(true);
        }
      } else if (e.key === 'ArrowLeft') {
        if (currentIndex > 0) {
          currentIndex--;
          renderQuestion();
          scrollToQuestionTop(true);
        }
      }
    });
  }

  function scrollToQuestionTop(smooth = true) {
    const mainEl = document.getElementById('appMainContent') || document.querySelector('.pyq-card');
    if (mainEl) {
      mainEl.scrollIntoView({ behavior: smooth ? 'smooth' : 'instant', block: 'start' });
    } else {
      window.scrollTo({ top: 0, behavior: smooth ? 'smooth' : 'instant' });
    }
  }

  function handleHash() {
    const hash = window.location.hash;
    if (!hash) return;

    if (hash.startsWith('#q')) {
      const qNum = parseInt(hash.replace('#q', ''), 10);
      const foundIdx = filteredQuestions.findIndex(q => q.qNum === qNum);
      if (foundIdx !== -1) {
        currentIndex = foundIdx;
        renderQuestion();
        scrollToQuestionTop(false);
      }
    } else if (hash.startsWith('#ch-') || hash.startsWith('#')) {
      const chId = hash.replace('#', '');
      const match = questions.some(q => q.chapterId === chId);
      if (match) {
        activeChapterId = chId;
        const sel = document.getElementById('chapterFilterSelect');
        if (sel) sel.value = chId;
        applyFilters();
        scrollToQuestionTop(false);
      }
    }
  }

  function renderQuestion() {
    if (!filteredQuestions || filteredQuestions.length === 0) return;
    const q = filteredQuestions[currentIndex];
    if (!q) return;

    // Header Pills
    const pill = document.getElementById('questionHeaderPill');
    if (pill) {
      pill.innerHTML = `<i class="fa-solid fa-calendar-check"></i> ${q.shift || 'UPSSSC PET'}`;
    }

    const typeBadge = document.getElementById('questionTypeBadge');
    if (typeBadge) {
      typeBadge.textContent = `Q.${q.qNum} (${currentIndex + 1} of ${filteredQuestions.length})`;
    }

    // Question Text
    const textEl = document.getElementById('questionText');
    if (textEl) {
      let extraHtml = '';
      if (q.passageText) {
        extraHtml += `<div class="passage-box" style="margin-bottom:12px; padding:12px 14px; background:var(--pyq-surface-muted); border-left:3px solid var(--pyq-accent); border-radius:8px; font-size:0.9rem; line-height:1.6; max-height:220px; overflow-y:auto;"><strong>Passage / गद्यांश:</strong><p style="margin:6px 0 0;">${q.passageText}</p></div>`;
      }
      if (q.tableData) {
        extraHtml += `<div class="pyq-table-wrap" style="margin-bottom:12px;">${renderMarkdownTable(q.tableData)}</div>`;
      }
      if (q.graphSvg) {
        extraHtml += q.graphSvg;
      } else if (q.graphDescription) {
        extraHtml += `<div class="graph-info-banner" style="margin-bottom:12px; font-size:0.85rem; color:var(--pyq-text-muted); background:var(--pyq-surface-muted); padding:8px 12px; border-radius:6px; border:1px solid var(--pyq-border);"><i class="fa-solid fa-chart-line" style="color:var(--pyq-accent);"></i> ${q.graphDescription}</div>`;
      }

      const qEn = getText(q.question, 'en');
      const qHi = q.hindiQuestion ? getText(q.hindiQuestion, 'hi') : getText(q.question, 'hi');

      textEl.innerHTML = `${extraHtml}
        <div class="lang-en" style="${currentLang === 'hi' ? 'display:none;' : ''}">${qEn}</div>
        <div class="lang-hi" style="${currentLang === 'en' ? 'display:none;' : ''}">${qHi}</div>
      `;
    }

    // Options Group
    const optContainer = document.getElementById('optionsContainer');
    if (optContainer) {
      optContainer.innerHTML = '';
      const group = document.createElement('div');
      group.className = 'pyq-options-group';

      const existingResp = userResponses[q.qNum];
      const isAnswered = !!existingResp;

      ['A', 'B', 'C', 'D', 'E'].forEach(optKey => {
        const rawOpt = q.options ? q.options[optKey] : null;
        if (rawOpt === undefined || rawOpt === null) return;

        const optEn = getText(rawOpt, 'en');
        const optHi = getText(rawOpt, 'hi');

        const optItem = document.createElement('div');
        optItem.className = 'pyq-option-item';
        optItem.dataset.key = optKey;

        if (isAnswered) {
          optItem.classList.add('locked');
          if (optKey === q.correctOption) {
            optItem.classList.add('correct');
          } else if (existingResp.selectedOption === optKey) {
            optItem.classList.add('wrong');
          }
        }

        optItem.innerHTML = `
          <div class="opt-header-row">
            <span class="opt-badge">${optKey}</span>
            <span class="opt-text">
              <span class="lang-en" style="${currentLang === 'hi' ? 'display:none;' : ''}">${optEn}</span>
              <span class="lang-hi" style="${currentLang === 'en' ? 'display:none;' : ''}">${optHi}</span>
            </span>
          </div>
        `;

        if (!isAnswered) {
          optItem.addEventListener('click', () => selectOption(q, optKey));
        }

        group.appendChild(optItem);
      });

      optContainer.appendChild(group);
    }

    // Inline Explanation Box
    const expBox = document.getElementById('inlineExplanation');
    if (expBox) {
      const resp = userResponses[q.qNum];
      if (resp) {
        expBox.style.display = 'flex';
        expBox.className = 'pyq-inline-explanation open ' + (resp.isCorrect ? 'correct-card' : 'wrong-card');

        const statusBadge = document.getElementById('resultStatusBadge');
        if (statusBadge) {
          statusBadge.className = 'result-badge ' + (resp.isCorrect ? 'correct' : 'wrong');
          statusBadge.innerHTML = resp.isCorrect 
            ? '<i class="fa-solid fa-circle-check"></i> Correct!' 
            : '<i class="fa-solid fa-circle-xmark"></i> Incorrect';
        }

        const keyPill = document.getElementById('officialKeyPill');
        if (keyPill) {
          const ansText = getText(q.answerText || (q.options ? q.options[q.correctOption] : ''), currentLang);
          keyPill.innerHTML = `Official Key: <strong>(${q.correctOption}) ${ansText}</strong>`;
          renderMath(keyPill);
        }

        const optAnalysis = document.getElementById('optionAnalysisBox');
        if (optAnalysis) {
          let verificationHtml = '';
          if (q.verificationNote) {
            verificationHtml = `
              <div style="background:rgba(234,179,8,0.12); border:1px solid rgba(234,179,8,0.4); border-radius:8px; padding:10px 12px; margin-bottom:12px; font-size:0.85rem; color:#fef08a;">
                <i class="fa-solid fa-triangle-exclamation" style="color:#eab308; margin-right:6px;"></i>
                <strong>Verification Note:</strong> ${q.verificationNote}
              </div>
            `;
          }

          const expEn = getText(q.explanation, 'en');
          const expHi = getText(q.explanation, 'hi');

          optAnalysis.innerHTML = `
            ${verificationHtml}
            <div style="font-size:0.92rem; line-height:1.6; color:var(--pyq-text);">
              <div style="font-weight:700; color:var(--pyq-accent); margin-bottom:6px;"><i class="fa-solid fa-lightbulb"></i> Step-by-Step Explanation:</div>
              <div class="lang-en" style="white-space:pre-line; ${currentLang === 'hi' ? 'display:none;' : ''}">${expEn}</div>
              <div class="lang-hi" style="white-space:pre-line; ${currentLang === 'en' ? 'display:none;' : ''}">${expHi}</div>
            </div>
          `;
          renderMath(optAnalysis);
        }

        const inlineNext = document.getElementById('inlineNextBtn');
        if (inlineNext) {
          inlineNext.style.display = currentIndex < filteredQuestions.length - 1 ? 'flex' : 'none';
        }
      } else {
        expBox.style.display = 'none';
        expBox.className = 'pyq-inline-explanation';
      }
    }

    // Bookmark button state
    const bBtn = document.getElementById('bookmarkBtn');
    if (bBtn) {
      if (bookmarks.has(q.qNum)) {
        bBtn.classList.add('active');
        bBtn.innerHTML = '<i class="fa-solid fa-bookmark"></i>';
      } else {
        bBtn.classList.remove('active');
        bBtn.innerHTML = '<i class="fa-regular fa-bookmark"></i>';
      }
    }

    // Nav button state
    const prevBtn = document.getElementById('prevQuestionBtn');
    if (prevBtn) prevBtn.disabled = currentIndex === 0;

    const nextBtn = document.getElementById('nextQuestionBtn');
    if (nextBtn) nextBtn.disabled = currentIndex === filteredQuestions.length - 1;

    // Update URL hash smoothly without reload
    if (history.replaceState) {
      history.replaceState(null, null, `#q${q.qNum}`);
    }

    // Math Typesetting
    if (textEl) renderMath(textEl);
    if (optContainer) renderMath(optContainer);
    if (expBox && expBox.style.display !== 'none') {
      renderMath(expBox);
    }
  }

  function selectOption(q, selectedKey) {
    const isCorrect = selectedKey === q.correctOption;
    userResponses[q.qNum] = { selectedOption: selectedKey, isCorrect };

    try {
      localStorage.setItem(`pet_responses_${subjectData.subjectId}`, JSON.stringify(userResponses));
    } catch (e) {}

    renderQuestion();
    updateProgress();
  }

  function toggleBookmark() {
    const q = filteredQuestions[currentIndex];
    if (!q) return;

    if (bookmarks.has(q.qNum)) {
      bookmarks.delete(q.qNum);
    } else {
      bookmarks.add(q.qNum);
    }

    try {
      localStorage.setItem(`pet_bookmarks_${subjectData.subjectId}`, JSON.stringify(Array.from(bookmarks)));
    } catch (e) {}

    renderQuestion();
  }

  function updateProgress() {
    const answeredCount = Object.keys(userResponses).filter(qNum => {
      return questions.some(q => q.qNum === parseInt(qNum, 10));
    }).length;

    const correctCount = Object.values(userResponses).filter(r => r.isCorrect).length;

    const counterEl = document.getElementById('progressCounter');
    if (counterEl) {
      counterEl.textContent = `${answeredCount}/${questions.length} Attempted`;
    }

    const masteryBadge = document.getElementById('masteryPercentage');
    if (masteryBadge) {
      const pct = questions.length > 0 ? Math.round((correctCount / questions.length) * 100) : 0;
      masteryBadge.innerHTML = `<i class="fa-solid fa-fire"></i> ${pct}% Accuracy`;
    }

    const segmentsContainer = document.getElementById('progressSegments');
    if (segmentsContainer) {
      segmentsContainer.innerHTML = '';
      const totalSegs = Math.min(filteredQuestions.length, 40);
      const step = filteredQuestions.length / totalSegs;

      for (let i = 0; i < totalSegs; i++) {
        const seg = document.createElement('div');
        seg.className = 'progress-segment';
        const qIdx = Math.floor(i * step);
        const curQ = filteredQuestions[qIdx];
        if (qIdx === currentIndex) {
          seg.classList.add('active');
        } else if (curQ && userResponses[curQ.qNum]) {
          seg.classList.add(userResponses[curQ.qNum].isCorrect ? 'completed' : 'wrong');
        }
        seg.style.cursor = 'pointer';
        seg.title = `Jump to Q.${curQ ? curQ.qNum : qIdx + 1}`;
        seg.addEventListener('click', () => {
          currentIndex = qIdx;
          renderQuestion();
          scrollToQuestionTop(true);
        });
        segmentsContainer.appendChild(seg);
      }
    }
  }

  function renderMarkdownTable(md) {
    if (!md) return '';
    const lines = md.trim().split('\n').filter(l => l.includes('|'));
    if (lines.length < 2) return `<pre>${md}</pre>`;

    let html = '<table class="pyq-data-table"><thead><tr>';
    const headers = lines[0].split('|').map(c => c.trim()).filter((c, i, arr) => i > 0 && i < arr.length - 1);
    headers.forEach(h => {
      html += `<th>${h}</th>`;
    });
    html += '</tr></thead><tbody>';

    for (let i = 2; i < lines.length; i++) {
      const cells = lines[i].split('|').map(c => c.trim()).filter((c, idx, arr) => idx > 0 && idx < arr.length - 1);
      html += '<tr>';
      cells.forEach(c => {
        html += `<td>${c}</td>`;
      });
      html += '</tr>';
    }
    html += '</tbody></table>';
    return html;
  }

})();
