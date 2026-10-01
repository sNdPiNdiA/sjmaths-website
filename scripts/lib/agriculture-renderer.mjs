import { agricultureGeneratedScript } from './agriculture-runtime.mjs';

// Pure authoring renderer; preserve every concept, question and metadata field.
export function renderTopicHtml(item, context, data) {
  const title = `${data.title}: Study Notes, MCQs, Revision & Topic Test | Agriculture | SJ Maths`;
  const metaDesc = `Master ${data.title} for UP TGT and UP PGT Agriculture exams. In-depth agronomic notes, scientific principles, chapter summary, and 30 practice MCQs.`;
  const canonicalUrl = `https://sjmaths.com${item.url}`;

  // Exam badges markup
  const isTgt = item.inTgt || item.examRelevance === 'Both' || (item.examRelevance && item.examRelevance.includes('TGT'));
  const isPgt = item.inPgt || item.examRelevance === 'Both' || (item.examRelevance && item.examRelevance.includes('PGT'));

  let examBadgesHtml = '';
  if (isTgt && isPgt) {
    examBadgesHtml = `
      <a class="exam-chip both" href="/up-tgt-agriculture/">UP TGT Agriculture Tracker →</a>
      <a class="exam-chip both" href="/up-pgt-agriculture/">UP PGT Agriculture Tracker →</a>
    `;
  } else if (isTgt) {
    examBadgesHtml = `<a class="exam-chip tgt" href="/up-tgt-agriculture/">UP TGT Agriculture Tracker →</a>`;
  } else if (isPgt) {
    examBadgesHtml = `<a class="exam-chip pgt" href="/up-pgt-agriculture/">UP PGT Agriculture Tracker →</a>`;
  } else {
    examBadgesHtml = `
      <a class="exam-chip both" href="/up-tgt-agriculture/">UP TGT Agriculture Tracker →</a>
      <a class="exam-chip both" href="/up-pgt-agriculture/">UP PGT Agriculture Tracker →</a>
    `;
  }

  // Schema Breadcrumbs
  const breadcrumbElements = [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://sjmaths.com/" },
    { "@type": "ListItem", "position": 2, "name": "Agriculture", "item": "https://sjmaths.com/agriculture/" },
    { "@type": "ListItem", "position": 3, "name": context.sectionMeta.en, "item": `https://sjmaths.com/agriculture/${context.sectionKey}/` },
    { "@type": "ListItem", "position": 4, "name": data.title, "item": canonicalUrl }
  ];

  const schemaJsonLd = {
    "@context": "https://schema.org",
    "@type": "LearningResource",
    "name": data.title,
    "headline": `${data.title} — UP TGT/PGT Agriculture Study Notes & Mock Test`,
    "description": metaDesc,
    "url": canonicalUrl,
    "inLanguage": "en",
    "learningResourceType": "Study Guide / Quiz",
    "educationalLevel": "Post-Secondary / Teacher Eligibility Examination",
    "isPartOf": {
      "@type": "WebSite",
      "name": "SJ Maths",
      "url": "https://sjmaths.com/"
    },
    "breadcrumb": {
      "@type": "BreadcrumbList",
      "itemListElement": breadcrumbElements
    }
  };

  // Render Notes HTML
  let notesHtml = '';
  data.notes_sections.forEach((sec, idx) => {
    notesHtml += `
      <section class="notes-section" id="sec-${idx + 1}">
        <h2>${sec.heading}</h2>
        <div class="prose-content">
          ${sec.content_html}
        </div>
      </section>
    `;
  });

  // Render Comparison Tables
  if (data.comparison_tables && data.comparison_tables.length > 0) {
    data.comparison_tables.forEach(table => {
      let headersHtml = table.headers.map(h => `<th>${h}</th>`).join('');
      let rowsHtml = table.rows.map(row => `<tr>${row.map(cell => `<td>${cell}</td>`).join('')}</tr>`).join('');
      notesHtml += `
        <div class="comparison-card">
          <div class="comparison-title">${table.title}</div>
          <div class="table-responsive">
            <table class="styled-table">
              <thead><tr>${headersHtml}</tr></thead>
              <tbody>${rowsHtml}</tbody>
            </table>
          </div>
        </div>
      `;
    });
  }

  // Render Mnemonics
  if (data.mnemonics && data.mnemonics.length > 0) {
    data.mnemonics.forEach(m => {
      notesHtml += `
        <div class="mnemonic-card">
          <div class="mnemonic-badge">Memory Trick / Mnemonic</div>
          <div class="mnemonic-title">${m.title}</div>
          <div class="mnemonic-formula">${m.trick}</div>
          <p class="mnemonic-desc">${m.explanation}</p>
        </div>
      `;
    });
  }

  // Render Exam Points
  if (data.exam_points && data.exam_points.length > 0) {
    let pts = data.exam_points.map(p => `<li>${p}</li>`).join('');
    notesHtml += `
      <div class="exam-points-card">
        <div class="exam-points-title">⚡ High-Yield Exam Points (UP TGT / PGT Focus)</div>
        <ul class="exam-points-list">${pts}</ul>
      </div>
    `;
  }

  // Render Common Errors
  if (data.common_errors && data.common_errors.length > 0) {
    let errs = data.common_errors.map(e => `<li>${e}</li>`).join('');
    notesHtml += `
      <div class="common-errors-card">
        <div class="common-errors-title">⚠️ Common Mistakes & Exam Pitfalls</div>
        <ul class="common-errors-list">${errs}</ul>
      </div>
    `;
  }

  // Render Chapter Summary Concepts
  let summaryConceptsHtml = '';
  if (data.chapter_summary_concepts && data.chapter_summary_concepts.length > 0) {
    data.chapter_summary_concepts.forEach(c => {
      summaryConceptsHtml += `
        <div class="summary-concept-card">
          <div class="summary-concept-header">
            <span class="summary-concept-pill">${c.concept_num}</span>
            <h3 class="summary-concept-title">${c.concept_title}</h3>
          </div>
          <div class="summary-concept-body prose-content">
            ${c.concept_body_html}
          </div>
        </div>
      `;
    });
  }

  // Render Quick Revision
  const qr = data.quick_revision || {};
  let glossaryHtml = '';
  if (qr.terms_glossary && qr.terms_glossary.length > 0) {
    qr.terms_glossary.forEach(t => {
      glossaryHtml += `
        <div class="glossary-item">
          <div class="glossary-term-wrap">
            <span class="glossary-term">${t.term}</span>
            ${t.term_en ? `<span class="glossary-term-en">(${t.term_en})</span>` : ''}
          </div>
          <div class="glossary-def">${t.definition}</div>
        </div>
      `;
    });
  }

  let mustRememberHtml = '';
  if (qr.must_remember && qr.must_remember.length > 0) {
    mustRememberHtml = qr.must_remember.map(item => `<li>${item}</li>`).join('');
  }

  let summaryBulletsHtml = '';
  if (qr.summary && qr.summary.length > 0) {
    summaryBulletsHtml = qr.summary.map(item => `<li>${item}</li>`).join('');
  }

  let confusionsHtml = '';
  if (qr.common_confusions && qr.common_confusions.length > 0) {
    qr.common_confusions.forEach(cf => {
      confusionsHtml += `
        <div class="confusion-item">
          <div class="confusion-terms">
            <span class="conf-badge-a">${cf.term_a}</span>
            <span class="conf-vs">VS</span>
            <span class="conf-badge-b">${cf.term_b}</span>
          </div>
          <p class="confusion-diff">${cf.difference}</p>
        </div>
      `;
    });
  }

  // Render Quiz Cards (SSR for instant availability & SEO)
  let quizCardsHtml = '';
  data.quiz.forEach((q, idx) => {
    const options = Array.isArray(q.options) && q.options.length >= 4 
      ? q.options 
      : ['Option A', 'Option B', 'Option C', 'Option D'];

    let opts = options.map((opt, oIdx) => `
      <button type="button" class="quiz-option-btn" data-qindex="${idx}" data-optindex="${oIdx}">
        <span class="option-letter">${String.fromCharCode(65 + oIdx)}</span>
        <span class="option-text">${opt}</span>
      </button>
    `).join('');

    quizCardsHtml += `
      <div class="quiz-question-card" id="q-card-${idx}" data-correct="${q.correct_index}">
        <div class="q-header">
          <span class="q-number">Question ${idx + 1} of ${data.quiz.length}</span>
          <span class="q-badge">Conceptual MCQ</span>
        </div>
        <h3 class="q-text">${q.question}</h3>
        <div class="quiz-options-group">
          ${opts}
        </div>
        <div class="q-feedback hidden" id="feedback-${idx}">
          <div class="feedback-indicator"></div>
          <p class="feedback-explanation"><strong>Explanation:</strong> ${q.explanation}</p>
        </div>
      </div>
    `;
  });

  // Render Topic Test Cards (SSR)
  let topicTestCardsHtml = '';
  data.topic_test.forEach((t, idx) => {
    const options = Array.isArray(t.options) && t.options.length >= 4 
      ? t.options 
      : ['Option A', 'Option B', 'Option C', 'Option D'];

    let opts = options.map((opt, oIdx) => `
      <button type="button" class="test-option-btn" data-tindex="${idx}" data-optindex="${oIdx}">
        <span class="option-letter">${String.fromCharCode(65 + oIdx)}</span>
        <span class="option-text">${opt}</span>
      </button>
    `).join('');

    topicTestCardsHtml += `
      <div class="test-question-card" id="t-card-${idx}" data-correct="${t.correct_index}">
        <div class="q-header">
          <span class="q-number">Test Question ${idx + 1} of ${data.topic_test.length}</span>
          <span class="q-badge test">${t.difficulty || 'TGT/PGT'} Standard</span>
        </div>
        <h3 class="q-text">${t.question}</h3>
        <div class="quiz-options-group">
          ${opts}
        </div>
        <div class="t-feedback hidden" id="t-feedback-${idx}">
          <p class="feedback-explanation"><strong>Solution & Rationale:</strong> ${t.explanation}</p>
        </div>
      </div>
    `;
  });

  // Navigation Links
  const prevHtml = context.prevTopic
    ? `<a class="nav-prev" href="${context.prevTopic.href}">← Previous: ${context.prevTopic.title}</a>`
    : `<span class="nav-prev disabled">First Topic</span>`;
  const nextHtml = context.nextTopic
    ? `<a class="nav-next" href="${context.nextTopic.href}">Next: ${context.nextTopic.title} →</a>`
    : `<span class="nav-next disabled">End of Section</span>`;

  // Related Topics
  let relatedHtml = '';
  if (context.related && context.related.length > 0) {
    relatedHtml = context.related.map(r => `<li><a href="${r.url}">${r.title}</a></li>`).join('');
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
<meta name="theme-color" content="#15803d">
<link rel="canonical" href="${canonicalUrl}">
<link rel="icon" type="image/png" href="/favicon.png">

<!-- Open Graph -->
<meta property="og:type" content="article">
<meta property="og:site_name" content="SJ Maths">
<meta property="og:title" content="${title}">
<meta property="og:description" content="${metaDesc}">
<meta property="og:url" content="${canonicalUrl}">
<meta property="og:image" content="https://sjmaths.com/assets/icons/icon-512x512.png">
<meta property="og:locale" content="en_US">

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="${title}">
<meta name="twitter:description" content="${metaDesc}">
<meta name="twitter:image" content="https://sjmaths.com/assets/icons/icon-512x512.png">

<!-- Structured Data (JSON-LD) -->
<script type="application/ld+json">
${JSON.stringify(schemaJsonLd, null, 2)}
</script>

<!-- Stylesheets -->
<link rel="stylesheet" href="/assets/css/topic-page.css">
<style>
:root {
  --brand: #14532d;
  --brand-dark: #052e16;
  --brand-light: #16a34a;
  --accent: #15803d;
  --accent-hover: #166534;
  --accent-soft: rgba(21, 128, 61, 0.08);
  --accent-border: rgba(21, 128, 61, 0.24);
}
html.dark, body.dark-mode {
  --brand: #4ade80;
  --brand-dark: #86efac;
  --brand-light: #22c55e;
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
      <span class="brand-mark" style="background: linear-gradient(145deg, #14532d, #16a34a); font-family: serif; font-size: 1.35rem; font-style: italic; display: flex; align-items: center; justify-content: center;">&int;</span>
      <span>
        <span class="brand-name">SJ Maths</span>
        <span class="brand-sub">Agriculture Master Study System</span>
      </span>
    </a>
    <div class="header-actions">
      <button type="button" class="theme-toggle-btn" id="btn-theme-toggle" aria-label="Toggle Dark Mode">🌙 Dark Mode</button>
      <a class="back-btn" href="/up-pgt-agriculture/" title="UP PGT Agriculture Tracker">← UP PGT<span class="desk-only"> Agriculture</span></a>
      <a class="back-btn" href="/up-tgt-agriculture/" title="UP TGT Agriculture Tracker">← UP TGT<span class="desk-only"> Agriculture</span></a>
    </div>
  </div>
</header>

<main class="wrap">
  <!-- Hero Section -->
  <section class="hero">
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="https://sjmaths.com/">Home</a>
      <span class="breadcrumb-sep">›</span>
      <a href="/agriculture/">Agriculture</a>
      <span class="breadcrumb-sep">›</span>
      <a href="/agriculture/${context.sectionKey}/">${context.sectionMeta.en}</a>
      <span class="breadcrumb-sep">›</span>
      <span aria-current="page">${data.title}</span>
    </nav>
    <div class="kicker" style="color: #15803d; font-weight: 800;">${context.sectionMeta.en}</div>
    <h1>${data.title}</h1>
    <p class="lead">${data.short_intro}</p>

    <div class="exam-badges">
      ${examBadgesHtml}
    </div>
  </section>

  <!-- Interactive Learning Navigation Tabs -->
  <div class="study-tabs-sticky-wrapper">
    <div class="study-tabs" role="tablist" aria-label="Study Module Tabs">
      <button type="button" class="tab-btn active" role="tab" aria-selected="true" data-tab="tab-notes" id="tab-btn-notes">
        <span>📖</span> <span>Study Notes</span>
      </button>
      <button type="button" class="tab-btn" role="tab" aria-selected="false" data-tab="tab-summary" id="tab-btn-summary">
        <span>⚡</span> <span>Chapter Summary</span>
      </button>
      <button type="button" class="tab-btn" role="tab" aria-selected="false" data-tab="tab-revision" id="tab-btn-revision">
        <span>🔄</span> <span>Quick Revision</span>
      </button>
      <button type="button" class="tab-btn" role="tab" aria-selected="false" data-tab="tab-quiz" id="tab-btn-quiz">
        <span>❓</span> <span>Practice Quiz</span> <span class="tab-badge">${data.quiz.length}Q</span>
      </button>
      <button type="button" class="tab-btn" role="tab" aria-selected="false" data-tab="tab-test" id="tab-btn-test">
        <span>⏱️</span> <span>Topic Test</span> <span class="tab-badge">10Q</span>
      </button>
    </div>
  </div>

  <!-- Tab Panels & Main Grid Layout -->
  <div class="main-grid">
    <div class="content-col">

      <!-- TAB 1: NOTES (Present in Server Static HTML for Search Engines) -->
      <article class="tab-panel active" id="tab-notes" role="tabpanel" aria-labelledby="tab-btn-notes">
        ${notesHtml}
      </article>

      <!-- TAB 2: CHAPTER SUMMARY -->
      <article class="tab-panel hidden" id="tab-summary" role="tabpanel" aria-labelledby="tab-btn-summary">
        <div class="summary-container">
          <div class="summary-hero-box">
            <h2>⚡ Chapter Master Summary: ${data.title}</h2>
            <p>Systematic concept review designed for quick retention and last-minute pre-exam revision.</p>
          </div>
          ${summaryConceptsHtml}
        </div>
      </article>

      <!-- TAB 3: QUICK REVISION & GLOSSARY -->
      <article class="tab-panel hidden" id="tab-revision" role="tabpanel" aria-labelledby="tab-btn-revision">
        <div class="revision-container">
          <div class="revision-card-box">
            <h2>📚 Technical Terms Glossary</h2>
            <div class="glossary-grid">
              ${glossaryHtml}
            </div>
          </div>

          ${mustRememberHtml ? `
          <div class="revision-card-box highlight">
            <h2>🎯 Must-Remember High-Frequency Facts</h2>
            <ul class="must-remember-list">
              ${mustRememberHtml}
            </ul>
          </div>` : ''}

          ${summaryBulletsHtml ? `
          <div class="revision-card-box">
            <h2>📌 Quick Recap Bullet Points</h2>
            <ul class="recap-list">
              ${summaryBulletsHtml}
            </ul>
          </div>` : ''}

          ${confusionsHtml ? `
          <div class="revision-card-box diff">
            <h2>⚖️ Concepts Often Confused in Examinations</h2>
            <div class="confusions-grid">
              ${confusionsHtml}
            </div>
          </div>` : ''}
        </div>
      </article>

      <!-- TAB 4: CONCEPTUAL PRACTICE QUIZ -->
      <article class="tab-panel hidden" id="tab-quiz" role="tabpanel" aria-labelledby="tab-btn-quiz">
        <div class="quiz-panel-header">
          <div class="quiz-panel-title">
            <h2>❓ Conceptual Practice Questions (20 MCQs)</h2>
            <p>Solve each question to test your fundamental conceptual clarity. Click any option to verify your answer with detailed explanation.</p>
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

      <!-- TAB 5: TIMED TOPIC TEST -->
      <article class="tab-panel hidden" id="tab-test" role="tabpanel" aria-labelledby="tab-btn-test">
        <div class="test-panel-header">
          <div>
            <h2>⏱️ 10-Minute Topic Speed Test</h2>
            <p>Simulate exam conditions with 10 challenging competitive questions under a strict countdown timer.</p>
          </div>
          <div class="test-timer-badge" id="testTimerBadge">
            <span class="timer-icon">⏳</span> <span id="timerDisplay">10:00</span>
          </div>
        </div>

        <div class="test-start-wrapper" id="testStartWrap">
          <div class="test-instruction-box">
            <h3>Test Instructions</h3>
            <ul>
              <li><strong>Total Questions:</strong> 10 MCQs</li>
              <li><strong>Time Allowed:</strong> 10 Minutes</li>
              <li><strong>Marking Scheme:</strong> +1 mark for correct, 0 for unattempted</li>
              <li><strong>Exam Level:</strong> UP TGT / PGT Agriculture Standard</li>
            </ul>
            <button type="button" class="btn-start-test" id="btnStartTest">Start Test Now</button>
          </div>
        </div>

        <div class="test-active-container hidden" id="testActiveWrap">
          <div class="test-questions-list">
            ${topicTestCardsHtml}
          </div>
          <div class="test-submit-bar">
            <button type="button" class="btn-submit-test" id="btnSubmitTest">Submit & View Analysis</button>
          </div>
        </div>

        <div class="test-result-modal hidden" id="testResultModal">
          <div class="result-card">
            <h3>Test Results & Performance Summary</h3>
            <div class="result-score-circle">
              <span id="resFinalScore">0</span> / 10
            </div>
            <p id="resFeedbackText">Review detailed solutions below for all questions.</p>
            <button type="button" class="btn-retake-test" id="btnRetakeTest">Retake Test</button>
          </div>
        </div>
      </article>

      <!-- Topic Navigation (Previous & Next) -->
      <nav class="topic-pagination" aria-label="Topic Navigation">
        ${prevHtml}
        ${nextHtml}
      </nav>

    </div>

    <!-- Right Sidebar -->
    <aside class="sidebar-col">
      <div class="sidebar-card">
        <h3>Exam Syllabus Trackers</h3>
        <p>Monitor your study progress across all subjects in the UP competitive exam trackers.</p>
        <div class="action-box">
          <strong>UP TGT Agriculture Tracker</strong>
          <p>95 syllabus microtopics, checklist, and practice sets</p>
          <a class="action-btn" href="/up-tgt-agriculture/">Open TGT Tracker →</a>
        </div>
        <div class="action-box" style="margin-top: 12px;">
          <strong>UP PGT Agriculture Tracker</strong>
          <p>157 detailed syllabus topics with exam weights</p>
          <a class="action-btn" href="/up-pgt-agriculture/">Open PGT Tracker →</a>
        </div>
      </div>

      ${relatedHtml ? `
      <div class="sidebar-card" style="margin-top: 20px;">
        <h3>Related Topics</h3>
        <ul class="related-links">
          ${relatedHtml}
        </ul>
      </div>` : ''}
    </aside>
  </div>
</main>

<footer class="footer">
  <div class="wrap footer-inner">
    <span>SJ Maths • Master Subject Library • ${data.title}</span>
    <div>
      <a href="https://sjmaths.com/">Home</a> &nbsp;•&nbsp;
      <a href="/up-tgt-agriculture/">UP TGT Agriculture</a> &nbsp;•&nbsp;
      <a href="/up-pgt-agriculture/">UP PGT Agriculture</a>
    </div>
  </div>
</footer>

<!-- Interactive Page Scripts -->
${agricultureGeneratedScript}
</body>
</html>
`;
}

