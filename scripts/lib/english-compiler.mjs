import { examTopicScript } from './exam-topic-runtime.mjs';

// Pure English renderer: prompts/API execution remain in the generator.
export function compileTopicHtml(call1, call2, context) {
  const canonicalUrl = `https://sjmaths.com${context.topicUrl}`;
  const metaDesc = `${call1.title}. Detailed study notes, literary analysis, grammar rules, mnemonics, PYQs, and topic test for UP TGT & PGT English.`;

  // Study Notes HTML
  let pillarsHtml = '';
  (call1.conceptual_pillars || []).forEach((p, idx) => {
    const takeaways = (p.key_takeaways || []).map(t => `<li>${t}</li>`).join('');
    const detailedPoints = (p.detailed_analysis_points || []).map(pt => `<li>${pt}</li>`).join('');
    pillarsHtml += `
      <section class="notes-section" id="pillar-${idx + 1}">
        <h2>${idx + 1}. ${p.pillar_title}</h2>
        <div class="prose-content">
          <p class="lead-concept" style="font-weight:600;color:var(--brand);margin-bottom:0.75rem;">${p.lead_concept}</p>
          ${detailedPoints ? `<ul class="notes-bullet-list" style="margin-bottom:1rem;">${detailedPoints}</ul>` : ''}
          ${p.comparative_insights ? `<div class="info-callout" style="background:var(--accent-soft);border-left:4px solid var(--accent);padding:1rem;margin:1rem 0;border-radius:6px;"><strong>Comparative Analysis:</strong> ${p.comparative_insights}</div>` : ''}
          ${takeaways ? `<ul class="notes-bullet-list" style="margin-top:0.75rem;">${takeaways}</ul>` : ''}
        </div>
      </section>
    `;
  });

  // Formulas / Scales
  let formulasHtml = '';
  if (call1.formulas_and_scales && call1.formulas_and_scales.length > 0) {
    const cards = call1.formulas_and_scales.map(f => `
      <div class="formula-card">
        <div class="formula-name">${f.name}</div>
        <div class="formula-eq">${f.equation}</div>
        <div class="formula-meta">
          <div><strong>Parameters:</strong> ${f.parameters}</div>
          <div><strong>Exam Focus:</strong> ${f.exam_significance}</div>
        </div>
      </div>
    `).join('');

    formulasHtml = `
      <div class="formula-sheet-box">
        <div class="formula-sheet-title">📐 Key Literary Devices & Grammar Rules</div>
        <div class="formula-grid">${cards}</div>
      </div>
    `;
  }

  // Spatial & Regional Distribution
  let spatialHtml = '';
  if (call1.spatial_and_regional_distribution) {
    spatialHtml = `
      <section class="notes-section" id="spatial-distribution">
        <h2>Literary Periods & Regional Context</h2>
        <div class="prose-content">
          <div style="margin-bottom:1rem;">
            <h3 style="font-size:1.1rem;color:var(--brand);margin-bottom:0.4rem;">🌐 Global/Historical Context</h3>
            <p>${call1.spatial_and_regional_distribution.global_patterns || ''}</p>
          </div>
          <div>
            <h3 style="font-size:1.1rem;color:var(--brand);margin-bottom:0.4rem;">🇮🇳 Indian Literature in English</h3>
            <p>${call1.spatial_and_regional_distribution.indian_context || ''}</p>
          </div>
        </div>
      </section>
    `;
  }

  // Tricks & Mnemonics
  let tricksHtml = '';
  if (call1.tricks_and_mnemonics && call1.tricks_and_mnemonics.length > 0) {
    const cards = call1.tricks_and_mnemonics.map(t => `
      <div class="trick-card" style="background:var(--paper-card);border:1px solid var(--accent-border);border-radius:var(--radius);padding:1.25rem;margin-bottom:1rem;">
        <div style="font-weight:700;color:var(--accent);font-size:1.05rem;margin-bottom:0.35rem;">💡 ${t.title}</div>
        <div style="font-size:1.1rem;font-weight:800;letter-spacing:0.5px;color:var(--brand);margin-bottom:0.5rem;background:var(--accent-soft);padding:0.5rem 0.75rem;border-radius:6px;display:inline-block;">${t.mnemonic}</div>
        <p style="margin-bottom:0.5rem;font-size:0.95rem;">${t.explanation}</p>
        <div style="font-size:0.85rem;color:var(--muted);"><strong>⚠️ Exam Trap:</strong> ${t.exam_pitfall_warning}</div>
      </div>
    `).join('');

    tricksHtml = `
      <section class="notes-section" id="mnemonics-section">
        <h2>Mnemonics, Memory Shortcuts & Exam Traps</h2>
        <div>${cards}</div>
      </section>
    `;
  }

  // Quick Revision Summary
  let glossaryHtml = '';
  const glossary = (call2.quick_revision && call2.quick_revision.glossary_terms) || [];
  if (glossary.length > 0) {
    const items = glossary.map(g => `
      <div style="border-bottom:1px solid var(--softline);padding:0.85rem 0;">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.25rem;">
          <strong style="color:var(--brand);font-size:1.05rem;">${g.term}</strong>
          <span style="font-size:0.75rem;background:var(--accent-soft);color:var(--accent);padding:2px 8px;border-radius:12px;font-weight:600;">${g.exam_tag || 'Concept'}</span>
        </div>
        <p style="margin:0;font-size:0.92rem;color:var(--ink2);">${g.definition}</p>
      </div>
    `).join('');

    glossaryHtml = `
      <div class="card" style="margin-bottom:1.5rem;">
        <h3 style="margin-bottom:1rem;color:var(--brand);font-size:1.2rem;">📚 High-Yield Literary & Grammatical Terminology</h3>
        <div>${items}</div>
      </div>
    `;
  }

  let theoriesHtml = '';
  const theories = (call2.quick_revision && call2.quick_revision.high_yield_laws_and_theories) || [];
  if (theories.length > 0) {
    const items = theories.map(th => `
      <div style="border-left:3px solid var(--brand);padding-left:1rem;margin-bottom:1rem;">
        <div style="font-weight:700;color:var(--brand);">${th.theorist_or_law} <span style="font-size:0.8rem;color:var(--muted);font-weight:400;">(${th.year_or_period})</span></div>
        <p style="margin:0.25rem 0 0;font-size:0.92rem;">${th.core_postulate}</p>
      </div>
    `).join('');

    theoriesHtml = `
      <div class="card">
        <h3 style="margin-bottom:1rem;color:var(--brand);font-size:1.2rem;">🧭 Prescribed Authors, Critics & Rules</h3>
        <div>${items}</div>
      </div>
    `;
  }

  // Practice Quiz MCQs
  let quizCardsHtml = '';
  const letters = ['A', 'B', 'C', 'D'];
  (call2.practice_quiz || []).forEach((q, idx) => {
    const opts = (q.options || []).map((opt, oIdx) => `
      <button type="button" class="quiz-option-btn" data-qindex="${idx}" data-optindex="${oIdx}">
        <span class="option-letter">${letters[oIdx]}</span>
        <span class="option-text">${opt}</span>
      </button>
    `).join('');

    quizCardsHtml += `
      <div class="quiz-question-card" id="q-card-${idx}" data-correct="${q.correct_index ?? 0}">
        <div class="quiz-q-header"><span class="q-badge">Question ${idx + 1} of ${(call2.practice_quiz || []).length}</span></div>
        <div class="question-text">${q.question}</div>
        <div class="quiz-options-grid">${opts}</div>
        <div class="quiz-feedback hidden" id="feedback-${idx}">
          <div class="feedback-indicator"></div>
          <p class="feedback-explanation"><strong>Rationale:</strong> ${q.explanation}</p>
        </div>
      </div>
    `;
  });

  // PYQs
  let pyqCardsHtml = '';
  (call2.pyqs || []).forEach((q, idx) => {
    const opts = (q.options || []).map((opt, oIdx) => `
      <button type="button" class="quiz-option-btn" data-pyqindex="${idx}" data-optindex="${oIdx}">
        <span class="option-letter">${letters[oIdx]}</span>
        <span class="option-text">${opt}</span>
      </button>
    `).join('');

    pyqCardsHtml += `
      <div class="pyq-card" id="pyq-card-${idx}" data-correct="${q.correct_index ?? 0}">
        <div class="pyq-header">
          <span class="exam-tag">${q.exam_year || 'UP PGT/TGT English'}</span>
        </div>
        <div class="question-text">${q.question}</div>
        <div class="quiz-options-grid">${opts}</div>
        <div class="pyq-solution hidden" id="pyq-expl-${idx}">
          <p><strong>Official Benchmark Explanation:</strong> ${q.explanation}</p>
        </div>
      </div>
    `;
  });

  // Timed Topic Test (10 Items)
  let topicTestCardsHtml = '';
  (call2.topic_test || []).forEach((q, idx) => {
    const opts = (q.options || []).map((opt, oIdx) => `
      <button type="button" class="test-option-btn" data-tindex="${idx}" data-optindex="${oIdx}">
        <span class="option-letter">${letters[oIdx]}</span>
        <span class="option-text">${opt}</span>
      </button>
    `).join('');

    topicTestCardsHtml += `
      <div class="test-question-card" id="t-card-${idx}" data-correct="${q.correct_index ?? 0}">
        <div class="test-q-header"><span class="t-badge">Question ${idx + 1} of 10</span></div>
        <div class="test-question-text">${q.question}</div>
        <div class="test-options-grid">${opts}</div>
        <div class="t-feedback hidden" id="t-feedback-${idx}">
          <p class="feedback-explanation"><strong>Solution:</strong> ${q.explanation}</p>
        </div>
      </div>
    `;
  });

  return `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>${call1.title} | UP TGT &amp; PGT English</title>
<meta name="description" content="${metaDesc}">
<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1">
<meta name="author" content="SJ Maths">
<meta name="theme-color" content="#064e3b">
<link rel="canonical" href="${canonicalUrl}">
<link rel="icon" type="image/png" href="/favicon.png">

<!-- Unified Topic Page Stylesheet (Chemistry Standard) -->
<link rel="stylesheet" href="/assets/css/topic-page.min.css?v=718ef3ff">

<!-- Theme Override -->
<style>
:root {
  --brand: #064e3b;
  --brand-dark: #022c22;
  --brand-light: #059669;
  --brand-gradient: linear-gradient(135deg, #064e3b 0%, #059669 100%);
  --accent: #059669;
  --accent-hover: #047857;
  --accent-soft: rgba(5, 150, 105, 0.08);
  --accent-border: rgba(5, 150, 105, 0.24);
}
html.dark, body.dark-mode {
  --brand: #6ee7b7;
  --brand-dark: #a7f3d0;
  --brand-light: #34d399;
  --brand-gradient: linear-gradient(135deg, #064e3b 0%, #022c22 100%);
  --accent: #34d399;
  --accent-hover: #6ee7b7;
  --accent-soft: rgba(52, 211, 153, 0.14);
  --accent-border: rgba(52, 211, 153, 0.35);
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
      <span class="brand-mark" style="background: linear-gradient(145deg, #064e3b, #059669); font-family: serif; font-size: 1.35rem; font-style: italic; display: flex; align-items: center; justify-content: center;">&int;</span>
      <span>
        <span class="brand-name">SJ Maths</span>
        <span class="brand-sub">English</span>
      </span>
    </a>
    <div class="header-actions">
      <button type="button" class="theme-toggle-btn" id="btn-theme-toggle" aria-label="Toggle Dark Mode">🌙 Dark Mode</button>
      <a class="back-btn" href="/up-pgt-english/" title="UP PGT English Tracker">← UP PGT<span class="desk-only"> English</span></a>
    </div>
  </div>
</header>

<main class="wrap">
  <!-- Hero Section -->
  <section class="hero">
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="https://sjmaths.com/">Home</a>
      <span class="breadcrumb-sep">›</span>
      <a href="/up-pgt-english/">English</a>
      <span class="breadcrumb-sep">›</span>
      <span>${context.sectionTitle}</span>
      <span class="breadcrumb-sep">›</span>
      <span aria-current="page">${context.topicName}</span>
    </nav>
    <div class="kicker" style="color: #059669; font-weight: 800;">${context.sectionTitle}</div>
    <h1>${call1.title}</h1>
    <p class="lead">${call1.short_intro}</p>

    <div class="exam-badges">
      <a class="exam-chip pgt" href="/up-pgt-english/">UP PGT English</a>
      <a class="exam-chip both" href="/up-tgt-english/">UP TGT English</a>
      <span class="exam-chip both">B.A. / M.A. Level</span>
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
        <span>❓</span> <span>Practice Quiz</span> <span class="tab-badge">${(call2.practice_quiz || []).length}Q</span>
      </button>
      <button type="button" class="tab-btn" role="tab" aria-selected="false" data-tab="tab-pyqs" id="tab-btn-pyqs">
        <span>🏛️</span> <span>PYQs &amp; Trends</span>
      </button>
      <button type="button" class="tab-btn" role="tab" aria-selected="false" data-tab="tab-test" id="tab-btn-test">
        <span>⏱️</span> <span>Topic Test</span> <span class="tab-badge">10Q</span>
      </button>
    </div>
  </div>

  <!-- Tab Panels & Main Grid Layout -->
  <div class="main-grid">
    <div class="content-col">

      <!-- TAB 1: STUDY NOTES -->
      <article class="tab-panel active" id="tab-notes" role="tabpanel" aria-labelledby="tab-btn-notes">
        ${call1.academic_synopsis ? `<div class="card" style="margin-bottom:1.5rem;"><p style="font-size:1.05rem;line-height:1.75;margin:0;">${call1.academic_synopsis}</p></div>` : ''}
        ${pillarsHtml}
        ${spatialHtml}
        ${formulasHtml}
        ${tricksHtml}
      </article>

      <!-- TAB 2: REVISION SUMMARY -->
      <article class="tab-panel hidden" id="tab-summary" role="tabpanel" aria-labelledby="tab-btn-summary">
        ${glossaryHtml}
        ${theoriesHtml}
      </article>

      <!-- TAB 3: PRACTICE QUIZ -->
      <article class="tab-panel hidden" id="tab-quiz" role="tabpanel" aria-labelledby="tab-btn-quiz">
        <div class="quiz-summary-card">
          <h3>Interactive Concept Practice</h3>
          <p>Instant evaluation with detailed explanations for each question.</p>
        </div>
        <div id="quiz-container">
          ${quizCardsHtml}
        </div>
      </article>

      <!-- TAB 4: PYQS & TRENDS -->
      <article class="tab-panel hidden" id="tab-pyqs" role="tabpanel" aria-labelledby="tab-btn-pyqs">
        <div class="pyq-header-card">
          <h3>Previous Years Questions &amp; Exam Benchmarks</h3>
          <p>Real and benchmark questions aligned with UP PGT, TGT, and National Eligibility tests.</p>
        </div>
        <div id="pyq-container">
          ${pyqCardsHtml}
        </div>
      </article>

      <!-- TAB 5: TIMED TOPIC TEST -->
      <article class="tab-panel hidden" id="tab-test" role="tabpanel" aria-labelledby="tab-btn-test">
        <div class="test-header-bar">
          <div>
            <h3>Timed Exam Simulator</h3>
            <p>10 Questions • 10 Minutes • Real-time scoring</p>
          </div>
          <div class="timer-display" id="testTimerDisplay">10:00</div>
        </div>

        <div class="test-questions-wrapper">
          ${topicTestCardsHtml}
        </div>

        <div class="test-submit-bar">
          <button type="button" class="btn-submit-test" id="btnSubmitTest" style="background: #059669;">Submit Test</button>
        </div>

        <div class="test-result-modal hidden" id="testResultModal">
          <div class="result-card">
            <h3>Test Result</h3>
            <div class="result-score-circle" style="background: linear-gradient(135deg, #064e3b, #059669);">
              <span id="resFinalScore">0</span> / 10
            </div>
            <p id="resFeedbackText">Review detailed solutions above for all questions.</p>
            <button type="button" class="btn-retake-test" id="btnRetakeTest" style="background: #059669;">Retake Test</button>
          </div>
        </div>
      </article>

      <!-- Bottom Pagination -->
      <nav class="topic-pagination" aria-label="Topic Navigation" style="margin-top:2rem;">
        <a class="topic-nav-btn next" href="/up-pgt-english/"><span>Exam Tracker →</span> <strong>UP PGT English</strong></a>
      </nav>

    </div>

    <!-- Sticky Sidebar -->
    <aside class="sidebar-col">
      <div class="sidebar-card side-card">
        <div class="side-card-header">
          <span class="side-badge">Syllabus Section</span>
          <h3>${context.sectionTitle}</h3>
        </div>
        <p class="side-desc">Official UP PGT English curriculum module.</p>
        <div class="side-action-box" style="margin-top:1.5rem;">
          <a class="side-action-btn" href="/up-pgt-english/" style="background: #064e3b; display:block; text-align:center; padding:10px; color:#fff; border-radius:8px; font-weight:600;">Full English Tracker →</a>
        </div>
      </div>
    </aside>
  </div>
</main>

<footer class="site-footer">
  <div class="wrap footer-inner">
    <div>
      <p><strong>SJ Maths — English</strong></p>
      <p>Master curriculum resources for UP PGT English &amp; UP TGT English.</p>
    </div>
    <div class="footer-links">
      <a href="https://sjmaths.com/">Home</a>
      <a href="/up-pgt-english/">UP PGT English</a>
      <a href="/up-tgt-english/">UP TGT English</a>
    </div>
  </div>
</footer>

<!-- Standard Chemistry/Topic-Page Interactive Controller -->
${examTopicScript}
</body>
</html>
`;
}

