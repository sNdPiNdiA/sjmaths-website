/**
 * UPSC Topicwise PYQ & Concept Drill Engine
 * Native Mobile-App UI/UX with Instant Answer Reveal & Inline Option Analysis
 * 
 * Two-Stage Mastery Flow:
 * 1. Official UPSC PYQs (1 to 6) tested in sequence
 * 2. Cascading Concept Drill Bank unlocked to master all tested concepts
 */

(function () {
  'use strict';

  let topicData = null;
  let currentPyqIndex = 0;   // 0 to topicData.clusters.length - 1
  let currentDrillIndex = 0; // 0 to allDrills.length - 1
  let currentMode = 'pyq';    // 'pyq' (Official PYQs) or 'drills' (Concept Drills)
  let userAnswers = {};
  let bookmarkedIds = new Set();
  let currentLang = 'en';
  let isTransitioning = false;

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initApp);
  } else {
    initApp();
  }

  function initApp() {
    const dataScript = document.getElementById('pyq-topic-data');
    if (!dataScript) return;

    try {
      topicData = JSON.parse(dataScript.textContent);
    } catch (e) {
      console.error('Failed to parse pyq-topic-data JSON', e);
      return;
    }

    loadLanguagePreference();
    loadStoredProgress();
    setupEventListeners();
    updateLanguageUI();
    updateModeTabsUI();
    renderCurrentQuestion();
  }

  function normalizeQuestion(qObj, fallbackId) {
    if (!qObj) return null;
    qObj.id = qObj.id || qObj.drillId || fallbackId;

    // Normalize options if passed as an object { A: {...}, B: {...} }
    if (qObj.options && !Array.isArray(qObj.options) && typeof qObj.options === 'object') {
      const correctVal = qObj.correctAnswer || qObj.correct || '';
      qObj.options = Object.keys(qObj.options).map(key => {
        const item = qObj.options[key];
        const isCorrect = (String(key).toUpperCase() === String(correctVal).toUpperCase()) || (item && item.correct === true);
        return {
          key: key,
          text: (item && typeof item === 'object' && item.text) ? item.text : (item || ''),
          correct: isCorrect,
          explanation: (item && typeof item === 'object' && item.explanation) ? item.explanation : null
        };
      });
    }

    // Ensure correct key can be retrieved from top-level or from options array
    if (!qObj.correctAnswer) {
      qObj.correctAnswer = qObj.correctOption || qObj.correct || '';
      if (!qObj.correctAnswer && Array.isArray(qObj.options)) {
        const found = qObj.options.find(o => o.correct === true);
        if (found) {
          qObj.correctAnswer = found.key || found.letter || '';
        }
      }
    }
    if (qObj.correctAnswer) {
      qObj.correctAnswer = String(qObj.correctAnswer).toUpperCase();
    }
    if (qObj.correctOption) {
      qObj.correctOption = String(qObj.correctOption).toUpperCase();
    }

    if (qObj.options && Array.isArray(qObj.options)) {
      const targetKey = (qObj.correctAnswer || qObj.correctOption || '').toUpperCase();
      qObj.options.forEach(opt => {
        if (opt.key) opt.key = String(opt.key).toUpperCase();
        if (targetKey && opt.key) {
          opt.correct = (opt.key === targetKey);
        }
      });
    }

    return qObj;
  }

  function getAllTopicDrills() {
    if (!topicData || !topicData.clusters) return [];
    const list = [];
    topicData.clusters.forEach((cluster, cIdx) => {
      const drills = cluster.drills || cluster.conceptDrills || (cluster.drill ? [cluster.drill] : (cluster.conceptDrill ? [cluster.conceptDrill] : []));
      if (drills && drills.length > 0) {
        drills.forEach((drill, dIdx) => {
          const fallbackId = `drill-${cIdx + 1}-${dIdx + 1}`;
          const normalized = normalizeQuestion({ ...drill }, fallbackId);
          list.push({
            ...normalized,
            clusterIndex: cIdx,
            clusterTopic: cluster.topic || (cluster.clusterTitle ? cluster.clusterTitle.en : ''),
            clusterConceptNotes: cluster.conceptNotes
          });
        });
      }
    });
    return list;
  }

  function loadLanguagePreference() {
    const saved = localStorage.getItem('upsc_pyq_lang') || localStorage.getItem('site_lang') || 'en';
    currentLang = (saved === 'hi') ? 'hi' : 'en';
    applyLanguageState();
  }

  function toggleLanguage() {
    currentLang = (currentLang === 'hi') ? 'en' : 'hi';
    localStorage.setItem('upsc_pyq_lang', currentLang);
    localStorage.setItem('site_lang', currentLang);
    applyLanguageState();
    updateProgressBar();
  }

  function applyLanguageState() {
    if (currentLang === 'hi') {
      document.body.classList.add('lang-mode-hi');
      document.documentElement.lang = 'hi';
    } else {
      document.body.classList.remove('lang-mode-hi');
      document.documentElement.lang = 'en';
    }
    updateLanguageUI();
  }

  function updateLanguageUI() {
    const lbl = document.getElementById('langToggleLabel');
    if (lbl) {
      lbl.textContent = (currentLang === 'hi') ? 'हिन्दी' : 'EN';
    }
  }

  function getStorageKey() {
    if (!topicData) return 'sjmaths_pyq_default';
    const cleanPath = window.location.pathname.replace(/\/$/, '').split('/').pop() || 'default';
    const id = topicData.topicId || topicData.topicSlug || cleanPath;
    return `sjmaths_pyq_${id}`;
  }

  function loadStoredProgress() {
    const storageKey = getStorageKey();
    try {
      const stored = localStorage.getItem(storageKey);
      if (stored) userAnswers = JSON.parse(stored);
      const bMarks = localStorage.getItem('sjmaths_pyq_bookmarks');
      if (bMarks) bookmarkedIds = new Set(JSON.parse(bMarks));
    } catch (e) {}
  }

  function saveProgress() {
    const storageKey = getStorageKey();
    try {
      localStorage.setItem(storageKey, JSON.stringify(userAnswers));
      localStorage.setItem('sjmaths_pyq_bookmarks', JSON.stringify(Array.from(bookmarkedIds)));
    } catch (e) {}
  }

  function updateModeTabsUI() {
    const allDrills = getAllTopicDrills();
    const modeTabs = document.querySelectorAll('.mode-tab-btn');
    modeTabs.forEach(tab => {
      const mode = tab.dataset.mode;
      if (mode === currentMode) {
        tab.classList.add('active');
      } else {
        tab.classList.remove('active');
      }
      // Update label with drill count dynamically
      if (mode === 'drills') {
        const enSpan = tab.querySelector('.lang-en');
        const hiSpan = tab.querySelector('.lang-hi');
        if (enSpan) enSpan.textContent = `Concept Drills (${allDrills.length})`;
        if (hiSpan) hiSpan.textContent = `अवधारणा अभ्यास (${allDrills.length})`;
      } else if (mode === 'pyq') {
        const enSpan = tab.querySelector('.lang-en');
        const hiSpan = tab.querySelector('.lang-hi');
        if (enSpan) enSpan.textContent = `Official PYQs (${topicData.clusters.length})`;
        if (hiSpan) hiSpan.textContent = `आधिकारिक PYQ (${topicData.clusters.length})`;
      }
    });
  }

  function setupEventListeners() {
    const langBtn = document.getElementById('langToggleBtn');
    if (langBtn) langBtn.addEventListener('click', toggleLanguage);

    const bookmarkBtn = document.getElementById('bookmarkBtn');
    if (bookmarkBtn) bookmarkBtn.addEventListener('click', toggleBookmark);

    const modeTabs = document.querySelectorAll('.mode-tab-btn');
    modeTabs.forEach(tab => {
      tab.addEventListener('click', () => {
        if (isTransitioning) return;
        currentMode = tab.dataset.mode;
        updateModeTabsUI();
        renderCurrentQuestion();
      });
    });

    const nextBtn = document.getElementById('inlineNextBtn');
    if (nextBtn) nextBtn.addEventListener('click', handleNextAction);

    const restartBtn = document.getElementById('modalRestartBtn');
    if (restartBtn) {
      restartBtn.addEventListener('click', () => {
        userAnswers = {};
        saveProgress();
        currentPyqIndex = 0;
        currentDrillIndex = 0;
        currentMode = 'pyq';
        document.getElementById('completionModal').classList.remove('open');
        updateModeTabsUI();
        renderCurrentQuestion();
      });
    }
  }

  function toggleBookmark() {
    const qObj = getCurrentQuestionObject();
    if (!qObj) return;
    const qId = qObj.id;
    const btn = document.getElementById('bookmarkBtn');

    if (bookmarkedIds.has(qId)) {
      bookmarkedIds.delete(qId);
      btn && btn.classList.remove('active');
    } else {
      bookmarkedIds.add(qId);
      btn && btn.classList.add('active');
    }
    saveProgress();
  }

  function getCurrentCluster() {
    if (!topicData || !topicData.clusters) return null;
    if (currentMode === 'pyq') {
      if (currentPyqIndex < 0 || currentPyqIndex >= topicData.clusters.length) return null;
      return topicData.clusters[currentPyqIndex];
    } else {
      const allDrills = getAllTopicDrills();
      if (currentDrillIndex < 0 || currentDrillIndex >= allDrills.length) return null;
      const currentDrill = allDrills[currentDrillIndex];
      if (currentDrill && currentDrill.clusterIndex !== undefined) {
        return topicData.clusters[currentDrill.clusterIndex];
      }
      return topicData.clusters[0] || null;
    }
  }

  function getCurrentQuestionObject() {
    if (!topicData || !topicData.clusters) return null;
    if (currentMode === 'pyq') {
      if (currentPyqIndex < 0 || currentPyqIndex >= topicData.clusters.length) return null;
      const cluster = topicData.clusters[currentPyqIndex];
      if (!cluster || !cluster.anchorPyq) return null;
      return normalizeQuestion(cluster.anchorPyq, `pyq-${currentPyqIndex + 1}`);
    } else {
      const allDrills = getAllTopicDrills();
      if (currentDrillIndex < 0 || currentDrillIndex >= allDrills.length) return null;
      return allDrills[currentDrillIndex] || null;
    }
  }

  function formatQuestionPrompt(raw) {
    if (!raw || typeof raw !== 'string') return raw || '';

    // If it already contains structured statement containers, preserve
    if (raw.includes('<div class="statements-container"') || raw.includes('<div class="match-list-block"')) {
      return raw;
    }

    let text = raw.trim();

    // 1. Strip trailing options if duplicated inside question prompt
    text = text.replace(/\n\s*\(a\)[\s\S]*$/i, '');
    text = text.replace(/\s*\(a\)\s+[^()]+(?:\s*\(b\)\s+[^()]+)?\s*\(c\)\s+[^()]+(?:\s*\(d\)\s+[^()]+)?\s*$/i, '');

    // 2. Strip trailing UPSC exam tags like [UPSC 1995 · Q.27] or (UPSC 2004)
    text = text.replace(/\s*\[\s*(?:UPSC|CSE)[\s\S]*?\]/gi, '');
    text = text.replace(/\s*\(\s*(?:UPSC|CSE)\s+\d{4}[\s\S]*?\)/gi, '');

    // If it already contains other HTML tags like <table or <div, return the cleaned text
    if (text.includes('<div') || text.includes('<table') || text.includes('<p class=')) {
      return text;
    }

    // 3. Normalize newlines
    text = text.replace(/\r\n/g, '\n').trim();

    const lines = text.split('\n').map(l => l.trim()).filter(Boolean);

    // Check for Table (e.g. Sl. No. or pipe-separated)
    const isTable = lines.some(l => l.includes('|') || (l.toLowerCase().includes('sl. no.') && lines.length > 3) || (l.toLowerCase().includes('क्र.सं.') && lines.length > 3));
    if (isTable) {
      let headerLine = -1;
      for (let i = 0; i < lines.length; i++) {
        if (lines[i].toLowerCase().includes('sl. no.') || lines[i].toLowerCase().includes('क्र.सं.')) {
          headerLine = i;
          break;
        }
      }
      if (headerLine !== -1) {
        const lead = lines.slice(0, headerLine);
        const tableLines = lines.slice(headerLine);
        const closing = [];
        const dataRows = [];
        let headerCols = tableLines[0].split(/[|\t]+/).map(c => c.trim()).filter(Boolean);
        
        for (let j = 1; j < tableLines.length; j++) {
          const row = tableLines[j];
          if (row.toLowerCase().includes('in which of') || row.toLowerCase().includes('उपर्युक्त में')) {
            closing.push(...tableLines.slice(j));
            break;
          }
          const cols = row.split(/[|\t]+/).map(c => c.trim()).filter(Boolean);
          if (cols.length >= 2) {
            dataRows.push(cols);
          }
        }

        let tblHtml = '';
        if (lead.length > 0) tblHtml += `<div class="pyq-lead-prompt">${lead.join('<br>')}</div>`;
        tblHtml += `<div class="pyq-table-wrap"><table class="pyq-data-table"><thead><tr>`;
        headerCols.forEach(h => tblHtml += `<th>${h}</th>`);
        tblHtml += `</tr></thead><tbody>`;
        dataRows.forEach(r => {
          tblHtml += `<tr>`;
          r.forEach((c, idx) => {
            if (idx === 0) tblHtml += `<td class="table-key-cell">${c}</td>`;
            else tblHtml += `<td>${c}</td>`;
          });
          tblHtml += `</tr>`;
        });
        tblHtml += `</tbody></table></div>`;
        if (closing.length > 0) tblHtml += `<div class="pyq-closing-prompt">${closing.join('<br>')}</div>`;
        return tblHtml;
      }
    }

    // Check for Match Lists (List I / List II)
    const isMatchList = lines.some(l => l.toLowerCase().includes('list i') || l.toLowerCase().includes('सूची i'));
    if (isMatchList) {
      let html = '';
      const matchLines = [];
      const lead = [];
      const closing = [];
      let state = 'lead';
      for (let i = 0; i < lines.length; i++) {
        const line = lines[i];
        if (line.toLowerCase().includes('list i') || line.toLowerCase().includes('सूची i') || line.toLowerCase().includes('list ii') || line.toLowerCase().includes('सूची ii') || /^[a-d|1-4]\)/i.test(line) || /^[a-d|1-4]\./i.test(line) || /^[i|v|x]+\./i.test(line)) {
          state = 'match';
          matchLines.push(line);
        } else if (state === 'match' && (line.toLowerCase().includes('code') || line.toLowerCase().includes('कूट') || line.toLowerCase().includes('select the'))) {
          state = 'closing';
          closing.push(line);
        } else if (state === 'closing') {
          closing.push(line);
        } else {
          lead.push(line);
        }
      }
      if (lead.length > 0) html += `<div class="pyq-lead-prompt">${lead.join('<br>')}</div>`;
      html += `<div class="match-list-block">${matchLines.map(l => {
        if (/^list\s+[i|1]/i.test(l) || /^सूची\s+[i|1]/i.test(l)) {
          return `<div class="match-list-heading">${l}</div>`;
        }
        return `<div class="match-list-item">${l}</div>`;
      }).join('')}</div>`;
      if (closing.length > 0) html += `<div class="pyq-closing-prompt">${closing.join('<br>')}</div>`;
      return html;
    }

    const statementRegex = /^(Statement[\s–-]*[I|V|X\d]+|कथन[\s–-]*[I|V|X\d]+|[I|V|X]+\.|\d+\.)\s*[:.-]?\s*(.*)$/i;

    let statementCount = 0;
    lines.forEach(l => {
      if (statementRegex.test(l)) statementCount++;
    });

    if (statementCount < 2) {
      return lines.map(l => `<p class="pyq-lead-prompt">${l}</p>`).join('');
    }

    const leadLines = [];
    const statements = [];
    const closingLines = [];
    let state = 'lead';

    for (let i = 0; i < lines.length; i++) {
      const line = lines[i];
      const match = line.match(statementRegex);

      if (match && state !== 'closing') {
        state = 'statements';
        statements.push({
          num: match[1],
          txt: match[2]
        });
      } else if (state === 'statements' && !match) {
        if (line.toLowerCase().includes('which of') || 
            line.toLowerCase().includes('select the') || 
            line.toLowerCase().includes('in which of') || 
            line.toLowerCase().includes('the correct') ||
            line.toLowerCase().includes('why is the') ||
            line.toLowerCase().includes('उपर्युक्त') ||
            line.toLowerCase().includes('नीचे दिए') ||
            line.toLowerCase().includes('इनमें से') ||
            line.toLowerCase().includes('निम्नलिखित में')) {
          state = 'closing';
          closingLines.push(line);
        } else {
          if (statements.length > 0) {
            statements[statements.length - 1].txt += ' ' + line;
          } else {
            leadLines.push(line);
          }
        }
      } else if (state === 'closing') {
        closingLines.push(line);
      } else {
        leadLines.push(line);
      }
    }

    let html = '';
    if (leadLines.length > 0) {
      html += `<div class="pyq-lead-prompt">${leadLines.join('<br>')}</div>`;
    }

    if (statements.length > 0) {
      html += `<div class="statements-container">`;
      statements.forEach(s => {
        let cleanNum = s.num.replace(/\.$/, '');
        html += `
          <div class="statement-row">
            <span class="statement-num">${cleanNum}.</span>
            <div class="statement-txt">${s.txt}</div>
          </div>`;
      });
      html += `</div>`;
    }

    if (closingLines.length > 0) {
      html += `<div class="pyq-closing-prompt">${closingLines.join('<br>')}</div>`;
    }

    return html;
  }

  function renderCurrentQuestion() {
    const qObj = getCurrentQuestionObject();
    if (!qObj) {
      showCompletionModal();
      return;
    }

    // Hide inline explanation card on new question
    const expCard = document.getElementById('inlineExplanation');
    if (expCard) {
      expCard.classList.remove('open', 'correct-card', 'wrong-card');
      expCard.style.display = 'none';
    }

    const milestoneBanner = document.getElementById('stage1CompleteBanner');
    if (milestoneBanner) {
      milestoneBanner.style.display = 'none';
      milestoneBanner.innerHTML = '';
    }

    window.scrollTo({ top: 0, behavior: 'smooth' });

    updateModeTabsUI();
    updateProgressBar();

    // Bookmark icon status
    const bookmarkBtn = document.getElementById('bookmarkBtn');
    if (bookmarkBtn) {
      if (bookmarkedIds.has(qObj.id)) {
        bookmarkBtn.classList.add('active');
      } else {
        bookmarkBtn.classList.remove('active');
      }
    }

    // Question Header Pill & Type Badge
    const headerPill = document.getElementById('questionHeaderPill');
    const typeBadge = document.getElementById('questionTypeBadge');

    if (currentMode === 'drills') {
      const allDrills = getAllTopicDrills();
      headerPill.className = 'pyq-exam-pill drill-pill';
      headerPill.innerHTML = `
        <i class="fa-solid fa-bolt"></i>
        <span class="lang-en">Concept Drill ${currentDrillIndex + 1}/${allDrills.length}</span>
        <span class="lang-hi">अवधारणा अभ्यास ${currentDrillIndex + 1}/${allDrills.length}</span>
      `;
      typeBadge.textContent = qObj.type ? qObj.type.toUpperCase() : 'DRILL';
    } else {
      // Official UPSC PYQ (1 to 6)
      headerPill.className = 'pyq-exam-pill';
      headerPill.innerHTML = `
        <i class="fa-solid fa-graduation-cap"></i>
        <span class="lang-en">UPSC Prelims ${qObj.year || ''}</span>
        <span class="lang-hi">UPSC प्रीलिम्स ${qObj.year || ''}</span>
      `;
      typeBadge.innerHTML = `
        <span class="lang-en">Q.${currentPyqIndex + 1} of ${topicData.clusters.length}</span>
        <span class="lang-hi">प्रश्न ${currentPyqIndex + 1}/${topicData.clusters.length}</span>
      `;
    }

    // Question Text
    const qTextEl = document.getElementById('questionText');
    const enQ = qObj.question && qObj.question.en ? qObj.question.en : (qObj.question || '');
    const hiQ = qObj.question && qObj.question.hi ? qObj.question.hi : enQ;
    qTextEl.innerHTML = `
      <div class="lang-en">${formatQuestionPrompt(enQ)}</div>
      <div class="lang-hi">${formatQuestionPrompt(hiQ)}</div>
    `;

    // Render Body (Statements / Match Lists / Options)
    const optionsContainer = document.getElementById('optionsContainer');
    optionsContainer.innerHTML = '';

    // Render Question Image if present (e.g. Map-based questions)
    if (qObj.image) {
      const imgWrap = document.createElement('div');
      imgWrap.className = 'pyq-question-image-wrap';
      imgWrap.style.margin = '10px 0 14px';
      imgWrap.style.textAlign = 'center';
      imgWrap.style.background = '#ffffff';
      imgWrap.style.padding = '8px';
      imgWrap.style.borderRadius = '8px';
      imgWrap.style.border = '1px solid var(--pyq-border)';
      imgWrap.innerHTML = `
        <img src="${qObj.image}" alt="Question Map Illustration" style="max-width: 100%; height: auto; max-height: 320px; display: inline-block; border-radius: 4px;" loading="lazy">
      `;
      optionsContainer.appendChild(imgWrap);
    }

    // Render Statements if explicitly present in data object and not already formatted in qTextEl
    if (qObj.statements && qObj.statements.length > 0 && !qTextEl.querySelector('.statements-container')) {
      const stmtWrap = document.createElement('div');
      stmtWrap.className = 'statements-container';
      qObj.statements.forEach(stmt => {
        const row = document.createElement('div');
        row.className = 'statement-row';
        const sEn = stmt.text && stmt.text.en ? stmt.text.en : (stmt.text || '');
        const sHi = stmt.text && stmt.text.hi ? stmt.text.hi : sEn;
        row.innerHTML = `
          <span class="statement-num">${stmt.num || stmt.number}.</span>
          <div class="statement-txt">
            <span class="lang-en">${sEn}</span>
            <span class="lang-hi">${sHi}</span>
          </div>
        `;
        stmtWrap.appendChild(row);
      });
      optionsContainer.appendChild(stmtWrap);
    }

    // Render Match Columns if present (Bilingual)
    if (qObj.matchLists) {
      const matchWrap = document.createElement('div');
      matchWrap.className = 'match-grid-container';

      const ml = qObj.matchLists;
      const l1TitleEn = ml.list1Title && ml.list1Title.en ? ml.list1Title.en : (ml.list1Title || 'List I');
      const l1TitleHi = ml.list1Title && ml.list1Title.hi ? ml.list1Title.hi : l1TitleEn;
      const l2TitleEn = ml.list2Title && ml.list2Title.en ? ml.list2Title.en : (ml.list2Title || 'List II');
      const l2TitleHi = ml.list2Title && ml.list2Title.hi ? ml.list2Title.hi : l2TitleEn;

      matchWrap.innerHTML = `
        <div class="match-col">
          <div class="match-column-title">
            <span class="lang-en">${l1TitleEn}</span>
            <span class="lang-hi">${l1TitleHi}</span>
          </div>
          <div class="match-item-list">
            ${ml.list1.map(item => {
              const itemEn = item.text && item.text.en ? item.text.en : (item.text || '');
              const itemHi = item.text && item.text.hi ? item.text.hi : itemEn;
              return `
                <div class="match-item-row">
                  <span class="match-item-key">${item.key}.</span>
                  <span><span class="lang-en">${itemEn}</span><span class="lang-hi">${itemHi}</span></span>
                </div>
              `;
            }).join('')}
          </div>
        </div>
        <div class="match-col">
          <div class="match-column-title">
            <span class="lang-en">${l2TitleEn}</span>
            <span class="lang-hi">${l2TitleHi}</span>
          </div>
          <div class="match-item-list">
            ${ml.list2.map(item => {
              const itemEn = item.text && item.text.en ? item.text.en : (item.text || '');
              const itemHi = item.text && item.text.hi ? item.text.hi : itemEn;
              return `
                <div class="match-item-row">
                  <span class="match-item-key">${item.key}.</span>
                  <span><span class="lang-en">${itemEn}</span><span class="lang-hi">${itemHi}</span></span>
                </div>
              `;
            }).join('')}
          </div>
        </div>
      `;
      optionsContainer.appendChild(matchWrap);
    }

    // Render Options
    if (qObj.type === 'true-false') {
      renderTrueFalseOptions(qObj, optionsContainer);
    } else if (qObj.type === 'fill-blank') {
      renderFillBlankOption(qObj, optionsContainer);
    } else {
      renderStandardOptions(qObj, optionsContainer);
    }

    // Restore answered state if already answered
    if (userAnswers[qObj.id]) {
      evaluateAndReveal(userAnswers[qObj.id].selected, qObj, true);
    }
  }

  function renderStandardOptions(qObj, container) {
    const optGroup = document.createElement('div');
    optGroup.className = 'pyq-options-group';

    qObj.options.forEach((opt, idx) => {
      const optEl = document.createElement('div');
      optEl.className = 'pyq-option-item';
      const key = opt.key || opt.letter || String.fromCharCode(65 + idx);
      optEl.dataset.key = key;

      const enText = opt.text && opt.text.en ? opt.text.en : (opt.text || opt);
      const hiText = opt.text && opt.text.hi ? opt.text.hi : enText;

      optEl.innerHTML = `
        <div class="opt-header-row">
          <div class="opt-badge">${key}</div>
          <div class="opt-text">
            <span class="lang-en">${enText}</span>
            <span class="lang-hi">${hiText}</span>
          </div>
        </div>
        <div class="opt-inline-explanation" style="display:none;"></div>
      `;

      // Tap-to-Reveal: Instant Answer on Click!
      optEl.addEventListener('click', () => {
        if (isTransitioning || optGroup.classList.contains('locked') || userAnswers[qObj.id]) return;
        optGroup.classList.add('locked');
        evaluateAndReveal(key, qObj, false);
      });

      optGroup.appendChild(optEl);
    });

    container.appendChild(optGroup);
  }

  function renderTrueFalseOptions(qObj, container) {
    const tfRow = document.createElement('div');
    tfRow.className = 'true-false-row';

    const trueBtn = document.createElement('button');
    trueBtn.className = 'tf-btn btn-true';
    trueBtn.dataset.val = 'TRUE';
    trueBtn.innerHTML = `<i class="fa-solid fa-check"></i> <span class="lang-en">TRUE</span><span class="lang-hi">सत्य</span>`;
    trueBtn.addEventListener('click', () => {
      if (isTransitioning || tfRow.classList.contains('locked') || userAnswers[qObj.id]) return;
      tfRow.classList.add('locked');
      evaluateAndReveal('TRUE', qObj, false);
    });

    const falseBtn = document.createElement('button');
    falseBtn.className = 'tf-btn btn-false';
    falseBtn.dataset.val = 'FALSE';
    falseBtn.innerHTML = `<i class="fa-solid fa-xmark"></i> <span class="lang-en">FALSE</span><span class="lang-hi">असत्य</span>`;
    falseBtn.addEventListener('click', () => {
      if (isTransitioning || tfRow.classList.contains('locked') || userAnswers[qObj.id]) return;
      tfRow.classList.add('locked');
      evaluateAndReveal('FALSE', qObj, false);
    });

    tfRow.appendChild(trueBtn);
    tfRow.appendChild(falseBtn);
    container.appendChild(tfRow);
  }

  function renderFillBlankOption(qObj, container) {
    const wrap = document.createElement('div');
    wrap.className = 'fill-blank-wrap';

    const inputRow = document.createElement('div');
    inputRow.style.display = 'flex';
    inputRow.style.gap = '8px';
    inputRow.style.alignItems = 'center';

    const input = document.createElement('input');
    input.type = 'text';
    input.className = 'fill-input';
    input.placeholder = (currentLang === 'hi') ? 'अपना उत्तर यहाँ लिखें...' : 'Type answer here...';
    input.autocomplete = 'off';
    input.style.flex = '1';

    const submitBtn = document.createElement('button');
    submitBtn.className = 'btn-primary-action fill-submit-btn';
    submitBtn.style.padding = '8px 16px';
    submitBtn.style.minHeight = '38px';
    submitBtn.style.fontSize = '0.85rem';
    submitBtn.innerHTML = `<span class="lang-en">Submit</span><span class="lang-hi">जमा करें</span>`;

    const triggerSubmit = () => {
      if (isTransitioning || input.disabled || submitBtn.disabled || userAnswers[qObj.id]) return;
      const val = input.value.trim();
      if (!val) return;
      input.disabled = true;
      submitBtn.disabled = true;
      evaluateAndReveal(val, qObj, false);
    };

    submitBtn.addEventListener('click', triggerSubmit);
    input.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') {
        e.preventDefault();
        triggerSubmit();
      }
    });

    inputRow.appendChild(input);
    inputRow.appendChild(submitBtn);
    wrap.appendChild(inputRow);

    if (qObj.hint) {
      const hintEl = document.createElement('div');
      hintEl.style.fontSize = '0.8rem';
      hintEl.style.color = 'var(--pyq-text-muted)';
      hintEl.style.marginTop = '6px';
      const hEn = qObj.hint.en || qObj.hint;
      const hHi = qObj.hint.hi || hEn;
      hintEl.innerHTML = `<i class="fa-regular fa-lightbulb"></i> <span class="lang-en">Hint: ${hEn}</span><span class="lang-hi">संकेत: ${hHi}</span>`;
      wrap.appendChild(hintEl);
    }

    container.appendChild(wrap);
  }

  function evaluateAndReveal(selectedVal, qObj, isRestore = false) {
    const qId = qObj.id || qObj.drillId || ('q-' + currentMode + '-' + (currentMode === 'pyq' ? currentPyqIndex : currentDrillIndex));
    if (!isRestore && userAnswers[qId]) return; // Race condition prevention

    const cluster = getCurrentCluster();
    let isCorrect = false;
    let correctKey = '';

    if (qObj.type === 'true-false') {
      correctKey = String(qObj.answer || qObj.correctAnswer || '').toUpperCase();
      isCorrect = (selectedVal.toUpperCase() === correctKey);

      const tfButtons = document.querySelectorAll('.tf-btn');
      tfButtons.forEach(btn => {
        btn.classList.add('locked');
        if (btn.dataset.val === correctKey) {
          btn.classList.add('correct');
        } else if (btn.dataset.val === selectedVal && !isCorrect) {
          btn.classList.add('wrong');
        }
      });
    } else if (qObj.type === 'fill-blank') {
      const cleanInput = selectedVal.toLowerCase().trim();
      isCorrect = (qObj.acceptedAnswers || []).some(ans => ans.toLowerCase().trim() === cleanInput);
      correctKey = (qObj.acceptedAnswers && qObj.acceptedAnswers[0]) || '';

      const input = document.querySelector('.fill-input');
      const submitBtn = document.querySelector('.fill-submit-btn') || document.querySelector('.fill-blank-wrap .btn-primary-action');
      if (input) {
        input.value = selectedVal;
        input.disabled = true;
        if (isCorrect) {
          input.classList.add('correct');
        } else {
          input.classList.add('wrong');
        }
      }
      if (submitBtn) {
        submitBtn.disabled = true;
      }
    } else {
      correctKey = String(qObj.correctAnswer || qObj.correctOption || '').toUpperCase();
      if (!correctKey && qObj.options) {
        const correctOpt = qObj.options.find(o => o.correct === true);
        if (correctOpt) correctKey = String(correctOpt.key || correctOpt.letter).toUpperCase();
      }
      isCorrect = (String(selectedVal).toUpperCase() === correctKey);

      // Color code options and reveal explanation just below each option
      document.querySelectorAll('.pyq-option-item').forEach(el => {
        el.classList.add('locked', 'revealed');
        const key = el.dataset.key;
        const isOptCorrect = (key === correctKey);
        if (isOptCorrect) {
          el.classList.add('correct');
        } else if (key === selectedVal && !isCorrect) {
          el.classList.add('wrong');
        }

        // Find explanation for this option
        let itemAnalysis = null;
        if (qObj.optionAnalysis) {
          itemAnalysis = qObj.optionAnalysis.find(oa => oa.key === key);
        }

        let enExp = '';
        let hiExp = '';

        if (itemAnalysis) {
          enExp = itemAnalysis.text && itemAnalysis.text.en ? itemAnalysis.text.en : (itemAnalysis.text || '');
          hiExp = itemAnalysis.text && itemAnalysis.text.hi ? itemAnalysis.text.hi : enExp;
        } else {
          const optData = qObj.options && qObj.options.find(o => (o.key || o.letter) === key);
          if (optData && optData.explanation) {
            enExp = optData.explanation.en || optData.explanation;
            hiExp = optData.explanation.hi || enExp;
          } else {
            enExp = isOptCorrect ? 'This option is correct.' : 'This option is incorrect.';
            hiExp = isOptCorrect ? 'यह विकल्प सही उत्तर है।' : 'यह विकल्प सही नहीं है।';
          }
        }

        const expEl = el.querySelector('.opt-inline-explanation');
        if (expEl) {
          expEl.className = `opt-inline-explanation ${isOptCorrect ? 'is-correct' : 'is-wrong'}`;
          expEl.innerHTML = `
            <span class="lang-en"><strong>${isOptCorrect ? '✓ Correct:' : '✗ Incorrect:'}</strong> ${enExp}</span>
            <span class="lang-hi"><strong>${isOptCorrect ? '✓ सही:' : '✗ गलत:'}</strong> ${hiExp}</span>
          `;
          expEl.style.display = 'block';
        }
      });
    }

    // Save Progress if fresh submission
    if (!isRestore) {
      userAnswers[qObj.id] = { selected: selectedVal, isCorrect: isCorrect };
      saveProgress();
      updateProgressBar();
    }

    // Reveal Detailed Explanation immediately below all four options
    revealInlineExplanation(isCorrect, selectedVal, correctKey, qObj, cluster, isRestore);
  }

  function revealInlineExplanation(isCorrect, selectedVal, correctKey, qObj, cluster, isRestore = false) {
    const expCard = document.getElementById('inlineExplanation');
    if (!expCard) return;

    expCard.style.display = 'flex';
    expCard.classList.remove('correct-card', 'wrong-card');
    expCard.classList.add('open', isCorrect ? 'correct-card' : 'wrong-card');

    // Status Badge
    const badge = document.getElementById('resultStatusBadge');
    badge.className = isCorrect ? 'result-badge correct' : 'result-badge wrong';
    badge.innerHTML = isCorrect
      ? `<i class="fa-solid fa-circle-check"></i> <span class="lang-en">Correct! +10 XP</span><span class="lang-hi">शानदार! सही उत्तर (+10 XP)</span>`
      : `<i class="fa-solid fa-circle-xmark"></i> <span class="lang-en">Incorrect. Review Analysis</span><span class="lang-hi">गलत उत्तर. विश्लेषण देखें</span>`;

    // Key Pill
    const keyPill = document.getElementById('officialKeyPill');
    if (qObj.type === 'true-false') {
      const displayKey = (correctKey === 'TRUE') ? 'True' : 'False';
      const displayKeyHi = (correctKey === 'TRUE') ? 'सत्य' : 'असत्य';
      keyPill.innerHTML = `
        <span class="lang-en">Official Answer: ${displayKey}</span>
        <span class="lang-hi">आधिकारिक उत्तर: ${displayKeyHi}</span>
      `;
    } else if (qObj.type === 'fill-blank') {
      keyPill.innerHTML = `
        <span class="lang-en">Accepted: ${correctKey}</span>
        <span class="lang-hi">स्वीकार्य उत्तर: ${correctKey}</span>
      `;
    } else {
      keyPill.innerHTML = `
        <span class="lang-en">Official Key: Option ${correctKey}</span>
        <span class="lang-hi">आधिकारिक उत्तर: विकल्प ${correctKey}</span>
      `;
    }

    // Render Detailed Explanation Box (Displayed below all four options)
    const analysisBox = document.getElementById('optionAnalysisBox');
    analysisBox.innerHTML = '';

    if (qObj.explanation) {
      const expBox = document.createElement('div');
      expBox.className = 'concept-flashcard-box';
      expBox.style.marginTop = '4px';
      const enExp = qObj.explanation.en || qObj.explanation;
      const hiExp = qObj.explanation.hi || enExp;
      expBox.innerHTML = `
        <strong style="color: var(--pyq-accent); display: block; margin-bottom: 6px; font-size: 0.95rem;">
          📖 <span class="lang-en">Detailed Explanation & Core Concepts:</span>
          <span class="lang-hi">विस्तृत व्याख्या एवं मुख्य अवधारणा:</span>
        </strong>
        <div style="line-height: 1.65; font-size: 0.91rem;">
          <span class="lang-en">${enExp}</span>
          <span class="lang-hi">${hiExp}</span>
        </div>
      `;
      analysisBox.appendChild(expBox);
    }

    // Concept Flashcard Takeaway
    const conceptBox = document.getElementById('conceptFlashcardBox');
    if (conceptBox) {
      if (cluster && cluster.conceptNotes && currentMode === 'pyq' && cluster.conceptNotes.points) {
        conceptBox.style.display = 'block';
        const pts = cluster.conceptNotes.points;
        conceptBox.innerHTML = `
          <strong style="color: var(--pyq-accent);">💡 <span class="lang-en">Key Concept Takeaways:</span><span class="lang-hi">मुख्य अवधारणा बिंदु:</span></strong>
          <ul style="margin: 6px 0 0; padding-left: 18px; line-height: 1.6;">
            ${pts.map(p => {
              const pEn = p.en || p;
              const pHi = p.hi || pEn;
              return `<li><span class="lang-en">${pEn}</span><span class="lang-hi">${pHi}</span></li>`;
            }).join('')}
          </ul>
        `;
      } else {
        conceptBox.style.display = 'none';
      }
    }

    // Update Next Action Button
    const nextBtn = document.getElementById('inlineNextBtn');
    const allDrills = getAllTopicDrills();
    const milestoneBanner = document.getElementById('stage1CompleteBanner');

    if (currentMode === 'pyq') {
      if (currentPyqIndex < topicData.clusters.length - 1) {
        if (milestoneBanner) {
          milestoneBanner.style.display = 'none';
          milestoneBanner.innerHTML = '';
        }
        nextBtn.className = 'btn-primary-action';
        nextBtn.innerHTML = `
          <span class="lang-en">Next UPSC PYQ (${currentPyqIndex + 2}/${topicData.clusters.length}) ➔</span>
          <span class="lang-hi">अगला UPSC PYQ (${currentPyqIndex + 2}/${topicData.clusters.length}) ➔</span>
        `;
        nextBtn.dataset.state = 'next-pyq';
      } else {
        // Stage 1 (Official PYQs) Completed!
        const totalPyqs = topicData.clusters.length;
        const topicTitleEn = (topicData.topicTitle && topicData.topicTitle.en) ? topicData.topicTitle.en : 'this Topic';
        const topicTitleHi = (topicData.topicTitle && topicData.topicTitle.hi) ? topicData.topicTitle.hi : 'इस विषय';

        if (milestoneBanner) {
          milestoneBanner.style.display = 'flex';
          milestoneBanner.innerHTML = `
            <div class="milestone-tag">
              <i class="fa-solid fa-trophy"></i>
              <span class="lang-en">Stage 1 Complete · ${totalPyqs}/${totalPyqs} Official PYQs Solved</span>
              <span class="lang-hi">चरण 1 पूर्ण · ${totalPyqs}/${totalPyqs} आधिकारिक PYQ हल किए</span>
            </div>
            <div class="milestone-title">
              <span class="lang-en">Master All Concepts from ${topicTitleEn}!</span>
              <span class="lang-hi">${topicTitleHi} की सभी अवधारणाओं पर मास्टरी हासिल करें!</span>
            </div>
            <p class="milestone-desc">
              <span class="lang-en">Reinforce and master every concept tested in these ${totalPyqs} questions${allDrills.length > 0 ? ` with our <strong>${allDrills.length}-question concept mastery battery</strong>` : ''}.</span>
              <span class="lang-hi">इन ${totalPyqs} प्रश्नों में पूछी गई सभी अवधारणाओं को${allDrills.length > 0 ? ` हमारी <strong>${allDrills.length} प्रश्नों की अभ्यास श्रृंखला</strong> से पूरी तरह कंठस्थ करें` : ' पूरी तरह कंठस्थ करें'}।</span>
            </p>
          `;
        }
        if (allDrills.length > 0) {
          nextBtn.className = 'btn-primary-action btn-drill-cta';
          nextBtn.innerHTML = `
            <i class="fa-solid fa-bolt"></i>
            <span class="lang-en">Start Concept Drills (${allDrills.length} Questions) ➔</span>
            <span class="lang-hi">अवधारणा अभ्यास शुरू करें (${allDrills.length} प्रश्न) ➔</span>
          `;
          nextBtn.dataset.state = 'start-drills';
        } else {
          nextBtn.className = 'btn-primary-action';
          nextBtn.innerHTML = `
            <span class="lang-en">Complete Topic Mastery 🎉</span>
            <span class="lang-hi">विषय मास्टरी पूर्ण 🎉</span>
          `;
          nextBtn.dataset.state = 'finish-mastery';
        }
      }
    } else {
      if (milestoneBanner) {
        milestoneBanner.style.display = 'none';
        milestoneBanner.innerHTML = '';
      }
      // Drills Mode
      if (currentDrillIndex < allDrills.length - 1) {
        nextBtn.className = 'btn-primary-action btn-drill-cta';
        nextBtn.innerHTML = `
          <span class="lang-en">Next Concept Drill (${currentDrillIndex + 2}/${allDrills.length}) ➔</span>
          <span class="lang-hi">अगला अभ्यास प्रश्न (${currentDrillIndex + 2}/${allDrills.length}) ➔</span>
        `;
        nextBtn.dataset.state = 'next-drill';
      } else {
        // Last Drill!
        nextBtn.className = 'btn-primary-action';
        nextBtn.innerHTML = `
          <span class="lang-en">Complete Topic Mastery 🎉</span>
          <span class="lang-hi">विषय मास्टरी पूर्ण 🎉</span>
        `;
        nextBtn.dataset.state = 'finish-mastery';
      }
    }

    // Smooth scroll into explanation view only if partly below viewport and not restoring
    if (!isRestore) {
      setTimeout(() => {
        const rect = expCard.getBoundingClientRect();
        if (rect.bottom > window.innerHeight) {
          expCard.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }
      }, 150);
    }
  }

  function handleNextAction() {
    if (isTransitioning) return;
    isTransitioning = true;
    setTimeout(() => { isTransitioning = false; }, 250);

    const nextBtn = document.getElementById('inlineNextBtn');
    const state = nextBtn ? nextBtn.dataset.state : null;
    const allDrills = getAllTopicDrills();

    if (state === 'next-pyq') {
      if (currentPyqIndex < topicData.clusters.length - 1) {
        currentPyqIndex++;
        renderCurrentQuestion();
      } else if (allDrills.length > 0) {
        currentMode = 'drills';
        currentDrillIndex = 0;
        updateModeTabsUI();
        renderCurrentQuestion();
      } else {
        showCompletionModal();
      }
    } else if (state === 'start-drills') {
      if (allDrills.length > 0) {
        currentMode = 'drills';
        currentDrillIndex = 0;
        updateModeTabsUI();
        renderCurrentQuestion();
      } else {
        showCompletionModal();
      }
    } else if (state === 'next-drill') {
      if (currentDrillIndex < allDrills.length - 1) {
        currentDrillIndex++;
        renderCurrentQuestion();
      } else {
        showCompletionModal();
      }
    } else if (state === 'finish-mastery') {
      showCompletionModal();
    } else {
      // Robust Fallback: automatically determine the next logical action
      if (currentMode === 'pyq') {
        if (currentPyqIndex < topicData.clusters.length - 1) {
          currentPyqIndex++;
          renderCurrentQuestion();
        } else if (allDrills.length > 0) {
          currentMode = 'drills';
          currentDrillIndex = 0;
          updateModeTabsUI();
          renderCurrentQuestion();
        } else {
          showCompletionModal();
        }
      } else {
        if (currentDrillIndex < allDrills.length - 1) {
          currentDrillIndex++;
          renderCurrentQuestion();
        } else {
          showCompletionModal();
        }
      }
    }
  }

  function updateProgressBar() {
    const segmentsContainer = document.getElementById('progressSegments');
    if (!segmentsContainer) return;
    segmentsContainer.innerHTML = '';

    if (currentMode === 'pyq') {
      const total = topicData.clusters.length;
      let completedCount = 0;

      for (let i = 0; i < total; i++) {
        const seg = document.createElement('div');
        seg.className = 'progress-segment';
        const cluster = topicData.clusters[i];
        const pyq = cluster ? cluster.anchorPyq : null;
        const qId = (pyq && pyq.id) ? pyq.id : (`pyq-${i + 1}`);

        if (userAnswers[qId]) {
          seg.classList.add(userAnswers[qId].isCorrect ? 'completed' : 'wrong');
          completedCount++;
        } else if (i === currentPyqIndex) {
          seg.classList.add('active');
        }

        seg.style.cursor = 'pointer';
        seg.title = `PYQ ${i + 1}`;
        const targetIdx = i;
        seg.addEventListener('click', () => {
          if (isTransitioning) return;
          currentPyqIndex = targetIdx;
          renderCurrentQuestion();
        });

        segmentsContainer.appendChild(seg);
      }

      const counter = document.getElementById('progressCounter');
      if (counter) {
        counter.innerHTML = `
          <span class="lang-en">${completedCount}/${total} PYQs Solved</span>
          <span class="lang-hi">${completedCount}/${total} PYQ हल किए</span>
        `;
      }

      const pct = total > 0 ? Math.round((completedCount / total) * 100) : 0;
      const masteryEl = document.getElementById('masteryPercentage');
      if (masteryEl) {
        masteryEl.innerHTML = `
          <i class="fa-solid fa-fire"></i>
          <span class="lang-en">${pct}% PYQ Mastery</span>
          <span class="lang-hi">${pct}% PYQ मास्टरी</span>
        `;
      }
    } else {
      // Drills mode
      const allDrills = getAllTopicDrills();
      const total = allDrills.length;
      let completedCount = 0;

      const segCount = Math.min(total, 30);
      for (let i = 0; i < segCount; i++) {
        const seg = document.createElement('div');
        seg.className = 'progress-segment';
        const drillIdx = Math.floor((i / segCount) * total);
        const qId = allDrills[drillIdx]?.id;

        if (qId && userAnswers[qId]) {
          seg.classList.add(userAnswers[qId].isCorrect ? 'completed' : 'wrong');
        } else if (i === Math.floor((currentDrillIndex / total) * segCount)) {
          seg.classList.add('active');
        }

        seg.style.cursor = 'pointer';
        seg.title = `Drill ${drillIdx + 1}`;
        const targetDrillIdx = drillIdx;
        seg.addEventListener('click', () => {
          if (isTransitioning) return;
          currentDrillIndex = targetDrillIdx;
          renderCurrentQuestion();
        });

        segmentsContainer.appendChild(seg);
      }

      allDrills.forEach(d => {
        if (userAnswers[d.id]) completedCount++;
      });

      const counter = document.getElementById('progressCounter');
      if (counter) {
        counter.innerHTML = `
          <span class="lang-en">Drill ${currentDrillIndex + 1}/${total} (${completedCount} Done)</span>
          <span class="lang-hi">अभ्यास ${currentDrillIndex + 1}/${total} (${completedCount} पूर्ण)</span>
        `;
      }

      const pct = total > 0 ? Math.round((completedCount / total) * 100) : 0;
      const masteryEl = document.getElementById('masteryPercentage');
      if (masteryEl) {
        masteryEl.innerHTML = `
          <i class="fa-solid fa-bolt"></i>
          <span class="lang-en">${pct}% Drills Done</span>
          <span class="lang-hi">${pct}% अभ्यास पूर्ण</span>
        `;
      }
    }
  }

  function showCompletionModal() {
    const modal = document.getElementById('completionModal');
    if (!modal) return;

    let correct = 0;
    const total = (topicData && topicData.clusters) ? topicData.clusters.length : 0;
    const allDrills = getAllTopicDrills();

    if (topicData && topicData.clusters) {
      topicData.clusters.forEach((c, idx) => {
        const qId = (c && c.anchorPyq && c.anchorPyq.id) ? c.anchorPyq.id : (`pyq-${idx + 1}`);
        if (userAnswers[qId] && userAnswers[qId].isCorrect) {
          correct++;
        }
      });
    }

    let drillsCorrect = 0;
    allDrills.forEach((d, idx) => {
      const qId = d.id || `drill-${idx + 1}`;
      if (userAnswers[qId] && userAnswers[qId].isCorrect) {
        drillsCorrect++;
      }
    });

    const overallTotal = total + allDrills.length;
    const overallCorrect = correct + drillsCorrect;
    const pct = overallTotal > 0 ? Math.round((overallCorrect / overallTotal) * 100) : 0;
    const scoreRing = document.getElementById('modalScoreRing');
    if (scoreRing) scoreRing.textContent = `${pct}%`;

    const summaryText = document.getElementById('modalSummaryText');
    if (summaryText) {
      if (allDrills.length > 0) {
        summaryText.innerHTML = `
          <span class="lang-en">Outstanding! You solved all ${total} official UPSC PYQs (${correct} correct) and completed the concept drill bank (${drillsCorrect}/${allDrills.length} correct)!</span>
          <span class="lang-hi">शानदार! आपने सभी ${total} आधिकारिक UPSC PYQs हल किए (${correct} सही) और अवधारणा अभ्यास बैंक पूरा किया (${drillsCorrect}/${allDrills.length} सही)!</span>
        `;
      } else {
        summaryText.innerHTML = `
          <span class="lang-en">Outstanding! You solved all ${total} official UPSC PYQs (${correct} correct)!</span>
          <span class="lang-hi">शानदार! आपने सभी ${total} आधिकारिक UPSC PYQs हल किए (${correct} सही)!</span>
        `;
      }
    }

    modal.classList.add('open');
  }

})();
