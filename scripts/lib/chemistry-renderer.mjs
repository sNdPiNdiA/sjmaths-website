import { chemistryEnglishScript } from './chemistry-runtime.mjs';

/** Render complete topic HTML with the original five-tab content layout. */
export function renderTopicHtml(item, context, data) {
  const segs = item.url.split('/').filter(Boolean);
  const topicSlug = segs[segs.length - 1];
  const topicTitleGuess = item.titleGuess || topicSlug.split('-').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' ');

  // Clean topic title: strip any AI artifacts like "High-Yield", "Study Notes", "UP PGT", etc.
  const rawTitle = data.title || topicTitleGuess;
  const cleanTitle = rawTitle
    .replace(/\s*[-–—:]\s*(High-Yield|Study Notes|UP PGT|Notes|Chemistry|Rasayan|Comprehensive|Master|Ultimate|Guide).*$/i, '')
    .trim() || topicTitleGuess;

  const canonicalUrl = `https://sjmaths.com${item.url}`;
  const title = `${cleanTitle} | UP PGT Chemistry`;
  const metaDesc = `${cleanTitle}: Key formulas, concise theory, critical exceptions, shortcuts, PYQs, and practice test for UP PGT Chemistry.`;

  // Schema.org Structured Data
  const schemaJsonLd = {
    "@context": "https://schema.org",
    "@type": "LearningResource",
    "name": cleanTitle,
    "headline": `${cleanTitle} — UP PGT Chemistry`,
    "description": metaDesc,
    "url": canonicalUrl,
    "inLanguage": "en",
    "learningResourceType": "Study Guide / Quiz",
    "educationalLevel": "Postgraduate Teacher Recruitment / B.Sc. & M.Sc.",
    "isPartOf": {
      "@type": "WebSite",
      "name": "SJ Maths",
      "url": "https://sjmaths.com/"
    },
    "breadcrumb": {
      "@type": "BreadcrumbList",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://sjmaths.com/" },
        { "@type": "ListItem", "position": 2, "name": "Chemistry", "item": "https://sjmaths.com/chemistry/" },
        { "@type": "ListItem", "position": 3, "name": context.sectionMeta.en, "item": `https://sjmaths.com/chemistry/${context.sectionKey}/` },
        { "@type": "ListItem", "position": 4, "name": cleanTitle, "item": canonicalUrl }
      ]
    }
  };

  // Exam Chips
  const examBadgesHtml = `
    <a class="exam-chip pgt" href="/up-pgt-chemistry/">UP PGT Chemistry</a>
    <span class="exam-chip both">Subject Code 02</span>
    <span class="exam-chip both">B.Sc. / M.Sc. Level</span>
  `;

  // TAB 1: FORMULA SHEET
  function formatMathHtml(str) {
    if (!str) return '';
    const symbolMap = {
      '\\\\hbar': '&#x210f;',
      '\\\\times': '&times;',
      '\\\\cdot': '&middot;',
      '\\\\pm': '&plusmn;',
      '\\\\approx': '&asymp;',
      '\\\\propto': '&prop;',
      '\\\\infty': '&infin;',
      '\\\\Delta': '&Delta;',
      '\\\\pi': '&pi;',
      '\\\\mu': '&mu;',
      '\\\\nu': '&nu;',
      '\\\\alpha': '&alpha;',
      '\\\\beta': '&beta;',
      '\\\\gamma': '&gamma;',
      '\\\\theta': '&theta;',
      '\\\\lambda': '&lambda;',
      '\\\\sigma': '&sigma;',
      '\\\\rho': '&rho;',
      '\\\\epsilon': '&epsilon;',
      '\\\\tau': '&tau;',
      '\\\\omega': '&omega;',
      '\\\\phi': '&phi;',
      '\\\\psi': '&psi;',
      '\\\\partial': '&part;',
      '\\\\sum': '&sum;',
      '\\\\int': '&int;',
      '\\\\rightarrow': '&rarr;',
      '\\\\rightleftharpoons': '&#8652;'
    };
    for (const [pattern, rep] of Object.entries(symbolMap)) {
      str = str.replace(new RegExp(pattern, 'g'), rep);
    }
    str = str.replace(/\\sqrt\{([^{}]+)\}/g, '<span class="math-sqrt">&radic;<span class="math-radicand">$1</span></span>');
    let changed = true;
    let safety = 0;
    while (changed && safety < 10) {
      changed = false;
      safety++;
      str = str.replace(/(?:&frac|\\frac)\{([^{}]+)\}\{([^{}]+)\}/g, (_, num, denom) => {
        changed = true;
        return `<span class="math-frac"><span class="math-num">${num}</span><span class="math-denom">${denom}</span></span>`;
      });
    }
    return str;
  }

  let formulaSheetHtml = '';
  if (Array.isArray(data.formula_sheet) && data.formula_sheet.length > 0) {
    const cards = data.formula_sheet.map(f => `
      <div class="formula-card">
        <div class="formula-name">${f.name}</div>
        <div class="formula-eq">${formatMathHtml(f.equation_html || f.equation)}</div>
        <div class="formula-meta">
          ${f.conditions ? `<div><strong>Conditions:</strong> ${f.conditions}</div>` : ''}
          ${f.units ? `<div><strong>Units:</strong> ${f.units}</div>` : ''}
        </div>
      </div>
    `).join('');

    formulaSheetHtml = `
      <div class="formula-sheet-box">
        <div class="formula-sheet-title">📐 Key Formulas & Equations</div>
        <div class="formula-grid">${cards}</div>
      </div>
    `;
  }

  // TAB 1: CONCISE BULLET NOTES
  let bulletNotesHtml = '';
  if (Array.isArray(data.concise_notes) && data.concise_notes.length > 0) {
    bulletNotesHtml = data.concise_notes.map((m, idx) => `
      <section class="notes-section" id="note-sec-${idx + 1}">
        <h2>${m.module_title}</h2>
        <div class="prose-content">
          <ul class="notes-bullet-list">
            ${m.bullets.map(b => `<li>${b}</li>`).join('')}
          </ul>
        </div>
      </section>
    `).join('');
  }

  // TAB 1: CRITICAL ANOMALIES & EXCEPTIONS
  let exceptionsHtml = '';
  if (Array.isArray(data.critical_exceptions) && data.critical_exceptions.length > 0) {
    const list = data.critical_exceptions.map(e => `
      <div class="exception-card">
        <div class="exception-head">
          <span class="exception-badge">Exception</span>
          <span class="exception-rule">${e.rule}</span>
        </div>
        <p class="exception-detail"><strong>Observation:</strong> ${e.exception} — <em>${e.reason}</em></p>
      </div>
    `).join('');

    exceptionsHtml = `
      <div class="exception-alert-box">
        <div class="exception-alert-title">⚠️ Important Exceptions & Anomalies</div>
        <div class="exception-list">${list}</div>
      </div>
    `;
  }

  // TAB 1: TIPS & MNEMONICS
  let tricksHtml = '';
  if (Array.isArray(data.tips_and_tricks) && data.tips_and_tricks.length > 0) {
    const list = data.tips_and_tricks.map(t => `
      <div class="trick-card">
        <div class="trick-title">${t.trick_title.replace(/^⚡\s*/, '')}</div>
        <div class="trick-shortcut">${t.shortcut_formula}</div>
        <p class="trick-app"><strong>Application:</strong> ${t.application}</p>
      </div>
    `).join('');

    tricksHtml = `
      <div class="trick-box">
        <div class="trick-box-title">💡 Shortcuts & Memory Aids</div>
        <div class="tricks-grid">${list}</div>
      </div>
    `;
  }

  // TAB 1: COMPARISON MATRIX
  let comparisonHtml = '';
  if (data.comparison_matrix && Array.isArray(data.comparison_matrix.headers)) {
    const m = data.comparison_matrix;
    const ths = m.headers.map(h => `<th>${h}</th>`).join('');
    const trs = m.rows.map(r => `<tr>${r.map(c => `<td>${c}</td>`).join('')}</tr>`).join('');

    comparisonHtml = `
      <div class="comparison-card">
        <div class="comparison-title">${m.title || 'Key Differences'}</div>
        <div class="table-responsive">
          <table class="styled-table">
            <thead><tr>${ths}</tr></thead>
            <tbody>${trs}</tbody>
          </table>
        </div>
      </div>
    `;
  }

  // TAB 1: EXAM POINTS & COMMON ERRORS
  let examPointsHtml = '';
  if (Array.isArray(data.exam_points) && data.exam_points.length > 0) {
    examPointsHtml = `
      <div class="exam-points-card">
        <div class="exam-points-title">🎯 Key Exam Points</div>
        <ul class="exam-points-list">
          ${data.exam_points.map(p => `<li>${p}</li>`).join('')}
        </ul>
      </div>
    `;
  }

  let pitfallsHtml = '';
  const pitfallsList = data.common_pitfalls || data.common_errors;
  if (Array.isArray(pitfallsList) && pitfallsList.length > 0) {
    pitfallsHtml = `
      <div class="common-errors-card">
        <div class="common-errors-title">🚫 Common Errors & Confusions</div>
        <ul class="common-errors-list">
          ${pitfallsList.map(e => `<li>${e}</li>`).join('')}
        </ul>
      </div>
    `;
  }

  // TAB 2: REVISION SUMMARY & GLOSSARY
  let summaryConceptsHtml = '';
  if (Array.isArray(data.chapter_summary_concepts) && data.chapter_summary_concepts.length > 0) {
    summaryConceptsHtml = data.chapter_summary_concepts.map(c => `
      <div class="summary-concept-card">
        <div class="summary-concept-header">
          <h3 class="summary-concept-title">${c.concept_title}</h3>
        </div>
        <div class="summary-concept-body prose-content">
          ${c.concept_body_html}
        </div>
      </div>
    `).join('');
  }

  const qr = data.quick_revision || {};
  let glossaryHtml = '';
  if (Array.isArray(qr.terms_glossary) && qr.terms_glossary.length > 0) {
    glossaryHtml = qr.terms_glossary.map(t => `
      <div class="glossary-item">
        <div class="glossary-term-wrap">
          <span class="glossary-term">${t.term}</span>
          ${t.term_en ? `<span class="glossary-term-en">(${t.term_en})</span>` : ''}
        </div>
        <div class="glossary-def">${t.definition}</div>
      </div>
    `).join('');
  }

  let mustRememberHtml = '';
  if (Array.isArray(qr.must_remember) && qr.must_remember.length > 0) {
    mustRememberHtml = qr.must_remember.map(item => `<li>${item}</li>`).join('');
  }

  let recapBulletsHtml = '';
  if (Array.isArray(qr.summary) && qr.summary.length > 0) {
    recapBulletsHtml = qr.summary.map(item => `<li>${item}</li>`).join('');
  }

  let confusionsHtml = '';
  if (Array.isArray(qr.common_confusions) && qr.common_confusions.length > 0) {
    confusionsHtml = qr.common_confusions.map(cf => `
      <div class="confusion-item">
        <div class="confusion-terms">
          <span class="conf-badge-a">${cf.term_a}</span>
          <span class="conf-vs">VS</span>
          <span class="conf-badge-b">${cf.term_b}</span>
        </div>
        <p class="confusion-diff">${cf.difference}</p>
      </div>
    `).join('');
  }

  // TAB 3: PRACTICE QUIZ (18-20 MCQs)
  const letters = ['A', 'B', 'C', 'D'];
  let quizCardsHtml = '';
  (data.quiz || []).forEach((q, idx) => {
    const optsList = Array.isArray(q.options) && q.options.length === 4 ? q.options : ['Option A', 'Option B', 'Option C', 'Option D'];
    let opts = optsList.map((opt, oIdx) => `
      <button type="button" class="quiz-option-btn" data-qindex="${idx}" data-optindex="${oIdx}">
        <span class="option-letter">${letters[oIdx]}</span>
        <span class="option-text">${opt}</span>
      </button>
    `).join('');

    quizCardsHtml += `
      <div class="quiz-question-card" id="q-card-${idx}" data-correct="${q.correct_index ?? 0}">
        <div class="q-header">
          <span class="q-number">Question ${idx + 1} of ${data.quiz.length}</span>
        </div>
        <h3 class="q-text">${q.question || 'Practice Question'}</h3>
        <div class="quiz-options-group">${opts}</div>
        <div class="q-feedback hidden" id="feedback-${idx}">
          <div class="feedback-indicator"></div>
          <p class="feedback-explanation"><strong>Explanation:</strong> ${q.explanation || 'See solution above.'}</p>
        </div>
      </div>
    `;
  });

  // TAB 4: PREVIOUS YEARS QUESTIONS (PYQs & Exam Trends)
  let pyqCardsHtml = '';
  const pyqList = Array.isArray(data.pyq_patterns) && data.pyq_patterns.length > 0
    ? data.pyq_patterns
    : (data.quiz || []).slice(0, 6);

  pyqList.forEach((q, idx) => {
    const optsList = Array.isArray(q.options) && q.options.length === 4 ? q.options : ['Option A', 'Option B', 'Option C', 'Option D'];
    let opts = optsList.map((opt, oIdx) => `
      <button type="button" class="quiz-option-btn" data-pyqindex="${idx}" data-optindex="${oIdx}">
        <span class="option-letter">${letters[oIdx]}</span>
        <span class="option-text">${opt}</span>
      </button>
    `).join('');

    const correctIdx = (typeof q.correct_index === 'number' && q.correct_index >= 0 && q.correct_index < 4) ? q.correct_index : 0;
    const correctOptText = optsList[correctIdx] || '';

    pyqCardsHtml += `
      <div class="pyq-card" id="pyq-card-${idx}" data-correct="${correctIdx}">
        <div class="pyq-header-meta">
          <span class="pyq-badge">${q.year_tag || 'UP PGT'}</span>
        </div>
        <div class="pyq-question-text">${q.question || 'PYQ Question'}</div>
        <div class="quiz-options-group">${opts}</div>
        <div class="pyq-expl-box hidden" id="pyq-expl-${idx}">
          <strong>Answer: Option ${letters[correctIdx]} (${correctOptText})</strong>
          <span>${q.explanation || ''}</span>
        </div>
      </div>
    `;
  });

  // TAB 5: TIMED TOPIC TEST (10 MCQs)
  let testCardsHtml = '';
  (data.topic_test || []).forEach((t, idx) => {
    const optsList = Array.isArray(t.options) && t.options.length === 4 ? t.options : ['Option A', 'Option B', 'Option C', 'Option D'];
    let opts = optsList.map((opt, oIdx) => `
      <button type="button" class="test-option-btn" data-tindex="${idx}" data-optindex="${oIdx}">
        <span class="option-letter">${letters[oIdx]}</span>
        <span class="option-text">${opt}</span>
      </button>
    `).join('');

    testCardsHtml += `
      <div class="test-question-card" id="t-card-${idx}" data-correct="${t.correct_index ?? 0}">
        <div class="test-q-header">
          <span class="t-badge">Question ${idx + 1} of ${(data.topic_test || []).length}</span>
        </div>
        <div class="test-question-text">${t.question || 'Test Question'}</div>
        <div class="test-options-grid">${opts}</div>
        <div class="t-feedback hidden" id="t-feedback-${idx}">
          <p class="feedback-explanation"><strong>Solution:</strong> ${t.explanation || 'See solution above.'}</p>
        </div>
      </div>
    `;
  });

  // Navigation Links
  const prevHtml = context.prevTopic
    ? `<a class="topic-nav-btn prev" href="${context.prevTopic.href}"><span>← Previous:</span> <strong>${context.prevTopic.rawText || context.prevTopic.title || 'Previous'}</strong></a>`
    : `<div class="topic-nav-btn disabled"><span>← Start of Branch</span></div>`;

  const nextHtml = context.nextTopic
    ? `<a class="topic-nav-btn next" href="${context.nextTopic.href}"><span>Next:</span> <strong>${context.nextTopic.rawText || context.nextTopic.title || 'Next'} →</strong></a>`
    : `<a class="topic-nav-btn next" href="/up-pgt-chemistry/"><span>Exam Tracker →</span> <strong>UP PGT Chemistry</strong></a>`;

  // Sidebar Links
  let relatedHtml = '';
  if (context.related && context.related.length > 0) {
    relatedHtml = context.related.map(r => `
      <a href="${r.url}">
        <span>${r.title}</span>
        <span>→</span>
      </a>
    `).join('');
  }

  return `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>${title}</title>
<meta name="description" content="${metaDesc}">
<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1">
<meta name="author" content="SJ Maths">
<meta name="theme-color" content="#1e3a8a">
<link rel="canonical" href="${canonicalUrl}">
<link rel="icon" type="image/png" href="/favicon.png">

<!-- OpenGraph Metadata -->
<meta property="og:type" content="article">
<meta property="og:site_name" content="SJ Maths">
<meta property="og:title" content="${cleanTitle} | Chemistry Notes & Test">
<meta property="og:description" content="${metaDesc}">
<meta property="og:url" content="${canonicalUrl}">

<!-- Twitter Card Metadata -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="${cleanTitle} | UP PGT Chemistry">
<meta name="twitter:description" content="${metaDesc}">

<!-- JSON-LD Structured Data -->
<script type="application/ld+json">
${JSON.stringify(schemaJsonLd, null, 2)}
</script>

<link rel="stylesheet" href="/assets/css/topic-page.css">
<style>
:root {
  --brand: #1e3a8a;
  --brand-dark: #0f172a;
  --brand-light: #2563eb;
  --accent: #2563eb;
  --accent-hover: #1d4ed8;
  --accent-soft: rgba(37, 99, 235, 0.08);
  --accent-border: rgba(37, 99, 235, 0.24);
}
html.dark, body.dark-mode {
  --brand: #93c5fd;
  --brand-dark: #bfdbfe;
  --brand-light: #60a5fa;
  --accent: #60a5fa;
  --accent-hover: #93c5fd;
  --accent-soft: rgba(96, 165, 250, 0.14);
  --accent-border: rgba(96, 165, 250, 0.35);
}
.desk-only { display: none; }
@media (min-width: 640px) {
  .desk-only { display: inline; }
}
</style>
</head>
<body>

<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="https://sjmaths.com/">
      <span class="brand-mark" style="background: linear-gradient(145deg, #1e3a8a, #2563eb); font-family: serif; font-size: 1.35rem; font-style: italic; display: flex; align-items: center; justify-content: center;">&int;</span>
      <span>
        <span class="brand-name">SJ Maths</span>
        <span class="brand-sub">Chemistry</span>
      </span>
    </a>
    <div class="header-actions">
      <button type="button" class="theme-toggle-btn" id="btn-theme-toggle" aria-label="Toggle Dark Mode">🌙 Dark Mode</button>
      <a class="back-btn" href="/up-pgt-chemistry/" title="UP PGT Chemistry Tracker">← UP PGT<span class="desk-only"> Chemistry</span></a>
    </div>
  </div>
</header>

<main class="wrap">
  <!-- Hero Section -->
  <section class="hero">
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="https://sjmaths.com/">Home</a>
      <span class="breadcrumb-sep">›</span>
      <a href="/chemistry/">Chemistry</a>
      <span class="breadcrumb-sep">›</span>
      <a href="/chemistry/${context.sectionKey}/">${context.sectionMeta.en}</a>
      <span class="breadcrumb-sep">›</span>
      <span aria-current="page">${cleanTitle}</span>
    </nav>
    <div class="kicker" style="color: #2563eb; font-weight: 800;">${context.sectionMeta.en}</div>
    <h1>${cleanTitle}</h1>
    <p class="lead">${data.short_intro}</p>

    <div class="exam-badges">
      ${examBadgesHtml}
    </div>
  </section>

  <!-- Interactive Learning Navigation Tabs (5 Tabs) -->
  <div class="study-tabs-sticky-wrapper">
    <div class="study-tabs" role="tablist" aria-label="Study Module Tabs">
      <button type="button" class="tab-btn active" role="tab" aria-selected="true" data-tab="tab-notes" id="tab-btn-notes">
        <span>📖</span> <span>Study Notes</span>
      </button>
      <button type="button" class="tab-btn" role="tab" aria-selected="false" data-tab="tab-summary" id="tab-btn-summary">
        <span>⚡</span> <span>Revision Summary</span>
      </button>
      <button type="button" class="tab-btn" role="tab" aria-selected="false" data-tab="tab-quiz" id="tab-btn-quiz">
        <span>❓</span> <span>Practice Quiz</span> <span class="tab-badge">${data.quiz.length}Q</span>
      </button>
      <button type="button" class="tab-btn" role="tab" aria-selected="false" data-tab="tab-pyqs" id="tab-btn-pyqs">
        <span>🏛️</span> <span>PYQs & Trends</span>
      </button>
      <button type="button" class="tab-btn" role="tab" aria-selected="false" data-tab="tab-test" id="tab-btn-test">
        <span>⏱️</span> <span>Topic Test</span> <span class="tab-badge">${data.topic_test.length}Q</span>
      </button>
    </div>
  </div>

  <!-- Tab Panels & Main Grid Layout -->
  <div class="main-grid">
    <div class="content-col">

      <!-- TAB 1: CONCISE EXAM-RELEVANT NOTES & CHEAT SHEET -->
      <article class="tab-panel active" id="tab-notes" role="tabpanel" aria-labelledby="tab-btn-notes">
        ${bulletNotesHtml}
        ${formulaSheetHtml}
        ${exceptionsHtml}
        ${tricksHtml}
        ${comparisonHtml}
        ${examPointsHtml}
        ${pitfallsHtml}
      </article>

      <!-- TAB 2: REVISION SUMMARY & FLASHCARDS -->
      <article class="tab-panel hidden" id="tab-summary" role="tabpanel" aria-labelledby="tab-btn-summary">
        <div class="summary-container">
          <div class="summary-hero-box" style="background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%);">
            <h2>⚡ Quick Revision: ${cleanTitle}</h2>
            <p>Core formulas, rapid recall points, and distinguishing criteria at a glance.</p>
          </div>
          ${summaryConceptsHtml}
        </div>

        <div class="revision-container" style="margin-top: 24px;">
          <div class="revision-card-box">
            <h2>📚 Terms & Units Glossary</h2>
            <div class="glossary-grid">
              ${glossaryHtml}
            </div>
          </div>

          ${mustRememberHtml ? `
          <div class="revision-card-box highlight">
            <h2>🎯 Key Takeaways</h2>
            <ul class="must-remember-list">
              ${mustRememberHtml}
            </ul>
          </div>` : ''}

          ${recapBulletsHtml ? `
          <div class="revision-card-box">
            <h2>📌 Quick Recall</h2>
            <ul class="recap-list">
              ${recapBulletsHtml}
            </ul>
          </div>` : ''}

          ${confusionsHtml ? `
          <div class="revision-card-box diff">
            <h2>⚖️ Key Differences</h2>
            <div class="confusions-grid">
              ${confusionsHtml}
            </div>
          </div>` : ''}
        </div>
      </article>

      <!-- TAB 3: PRACTICE QUIZ (18-20 MCQs) -->
      <article class="tab-panel hidden" id="tab-quiz" role="tabpanel" aria-labelledby="tab-btn-quiz">
        <div class="quiz-panel-header">
          <div class="quiz-panel-title">
            <h2>❓ Practice Questions (${data.quiz.length} MCQs)</h2>
            <p>Select an option to test your understanding with instant verification and explanations.</p>
          </div>
          <div class="quiz-live-scoreboard">
            <div class="score-pill">Score: <span id="quizScore">0</span> / ${data.quiz.length}</div>
            <button type="button" class="btn-reset-quiz" id="btnResetQuiz">Restart Quiz</button>
          </div>
        </div>

        <div class="quiz-questions-list">
          ${quizCardsHtml}
        </div>
      </article>

      <!-- TAB 4: PREVIOUS YEARS QUESTIONS (PYQs & Exam Trends) -->
      <article class="tab-panel hidden" id="tab-pyqs" role="tabpanel" aria-labelledby="tab-btn-pyqs">
        <div class="pyq-trend-card">
          <h2>🏛️ Exam Trends & Question Pattern</h2>
          <p>Historical question weightage and patterns for <strong>${cleanTitle}</strong> in UP PGT Chemistry.</p>
          <div class="pyq-trend-grid">
            <div class="pyq-stat-item">
              <span class="pyq-stat-val">2–4</span>
              <span class="pyq-stat-label">Expected Questions</span>
            </div>
            <div class="pyq-stat-item">
              <span class="pyq-stat-val">8–12%</span>
              <span class="pyq-stat-label">Topic Weightage</span>
            </div>
            <div class="pyq-stat-item">
              <span class="pyq-stat-val">Medium</span>
              <span class="pyq-stat-label">Difficulty</span>
            </div>
          </div>
        </div>

        <div class="pyq-questions-list">
          ${pyqCardsHtml}
        </div>
      </article>

      <!-- TAB 5: TIMED TOPIC TEST (10 MCQs / 10 Minutes) -->
      <article class="tab-panel hidden" id="tab-test" role="tabpanel" aria-labelledby="tab-btn-test">
        <div class="test-panel-header">
          <div>
            <h2>⏱️ Timed Topic Test</h2>
            <p>10 questions &bull; 10 minutes &bull; Timed practice</p>
          </div>
          <div class="test-timer-badge" id="testTimerBadge">
            <span class="timer-icon">⏳</span> <span id="timerDisplay">10:00</span>
          </div>
        </div>

        <div class="test-instruction-box" id="testStartWrap">
          <h3>Instructions</h3>
          <ul>
            <li><strong>Questions:</strong> 10 MCQs</li>
            <li><strong>Time Allowed:</strong> 10 Minutes</li>
            <li><strong>Marking:</strong> +1 mark for correct, 0 for unattempted or wrong</li>
          </ul>
          <button type="button" class="btn-start-test" id="btnStartTest" style="background: linear-gradient(135deg, #1e3a8a, #2563eb);">Start Test</button>
        </div>

        <div class="test-active-container hidden" id="testActiveWrap">
          <div class="test-questions-list">
            ${testCardsHtml}
          </div>
          <div class="test-submit-bar">
            <button type="button" class="btn-submit-test" id="btnSubmitTest" style="background: #2563eb;">Submit Test</button>
          </div>
        </div>

        <div class="test-result-modal hidden" id="testResultModal">
          <div class="result-card">
            <h3>Test Result</h3>
            <div class="result-score-circle" style="background: linear-gradient(135deg, #1e3a8a, #2563eb);">
              <span id="resFinalScore">0</span> / 10
            </div>
            <p id="resFeedbackText">Review detailed solutions above for all questions.</p>
            <button type="button" class="btn-retake-test" id="btnRetakeTest" style="background: #2563eb;">Retake Test</button>
          </div>
        </div>
      </article>

      <!-- Bottom Prev / Next Navigation -->
      <nav class="topic-pagination" aria-label="Topic Navigation">
        ${prevHtml}
        ${nextHtml}
      </nav>

    </div>

    <!-- Sticky Sidebar -->
    <aside class="sidebar-col">
      <div class="sidebar-card side-card">
        <div class="side-card-header">
          <span class="side-badge">Syllabus Section</span>
          <h3>${context.sectionMeta.en}</h3>
        </div>
        <p class="side-desc">Branch topics covered under official UP PGT Chemistry curriculum.</p>
        <div class="side-nav-links">
          ${relatedHtml}
        </div>
        <div class="side-action-box">
          <a class="side-action-btn" href="/up-pgt-chemistry/" style="background: #1e3a8a;">Full Chemistry Tracker →</a>
        </div>
      </div>
    </aside>
  </div>
</main>

<footer class="site-footer">
  <div class="wrap footer-inner">
    <div>
      <p><strong>SJ Maths — Chemistry</strong></p>
      <p>Study notes and test prep for UP PGT Chemistry (Subject Code 02).</p>
    </div>
    <div class="footer-links">
      <a href="https://sjmaths.com/">Home</a>
      <a href="/up-pgt-chemistry/">UP PGT Chemistry</a>
      <a href="/privacy-policy/">Privacy Policy</a>
    </div>
  </div>
</footer>

${chemistryEnglishScript}
</body>
</html>
`;
}

/**
 * Process single topic through rotating Gemini models
 */
