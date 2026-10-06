import * as cheerio from 'cheerio';
import { hydrateHistoryStyles, externalizeHistoryStyles } from './history-styles.mjs';
import { historyRuntimeScript } from './history-runtime.mjs';

export const TAB_VERSION = 'history-tabs-v1';

const plainHistoryLabels = new Map([
  ['Detailed explanation', 'Details'],
  ['Key points', 'Remember'],
  ['Examples and evidence', 'Examples & sources'],
  ['Important distinctions', 'Compare'],
  ['Common misconceptions', 'Common confusions'],
  ['Exam focus', 'Exam points'],
  ['Point-wise rapid recall', 'Quick recall'],
  ['Mnemonic', 'Memory aid'],
  ['Tips', 'Review tips'],
  ['Exam tricks', 'Quick checks'],
  ['Common traps', 'Watch for'],
  ['Topic mnemonics', 'Memory aids'],
  ['Revision tips', 'Review tips'],
  ['Important comparisons', 'Compare'],
  ['Exam traps and cautions', 'Watch for'],
  ['Self-assessment checklist', 'Check yourself']
]);

export function cleanHistoryCopy($) {
  $('.hero p.lead').each((_, element) => {
    if (/^Core study module, theoretical overview, and exam revision checklist for\s+/i.test($(element).text())) $(element).remove();
  });
  $('.exam-badges .history-generated-badge').remove();
  $('.exam-badges').each((_, element) => {
    if (!$(element).text().trim() && !$(element).children().length) $(element).remove();
  });
  $('.notes-section h3, .revision-card-box h3, .revision-card-box h2, .tab-panel#tab-notes > .card h2').each((_, element) => {
    const current = $(element).text().trim();
    if (plainHistoryLabels.has(current)) $(element).text(plainHistoryLabels.get(current));
  });
  $('.history-callout > strong').text('Examples & sources');
  $('.comparison-callout > strong').text('Compare');
  $('.trap-callout > strong').text('Common confusions');
  $('.exam-focus > strong').text('Exam points');
  $('.summary-hero-box p, #tab-quiz .quiz-panel-header p, #tab-test .test-panel-header p').remove();
  $('p').each((_, element) => {
    const text = $(element).text().trim();
    if (/^Check off each item as you master the factual and analytical aspects of\s+/i.test(text)
      || /^In competitive examinations\s*\(/i.test(text)) $(element).remove();
  });
  $('.check-item span').each((_, element) => {
    const text = $(element).text().trim();
    const match = text.match(/^I can explain (.+) with its key dates, terms and exam distinctions\.$/i);
    if (match) $(element).text(`Explain ${match[1]} from memory.`);
  });
  return $;
}

function escapeHtml(str) {
  return String(str || '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

export function renderLegacyHtml(originalHtml, data, metadata) {
  const $ = cheerio.load(hydrateHistoryStyles(originalHtml));
  cleanHistoryCopy($);

  // Update lead text if suitable
  if (metadata.title) {
    $('.hero h1').text(metadata.title);
  }

  // Build the new point-wise cards inside .content-col
  const contentCol = $('.main-grid .content-col');
  contentCol.empty();

  // Card 1: Syllabus Overview & Exam Focus (Point-wise)
  let card1Html = `<article class="card">
    <h2>1. Topic outline</h2>
    <ul class="point-notes">`;
  for (const pt of (data.syllabus_focus_points || [])) {
    card1Html += `<li>${pt}</li>`;
  }
  card1Html += `</ul>
  </article>`;
  contentCol.append(card1Html);

  // Card 2+: Study Notes Sections (Point-wise notes)
  let sectionIndex = 2;
  for (const section of (data.study_sections || [])) {
    let secHtml = `<article class="card">
      <h2>${sectionIndex}. ${escapeHtml(section.heading)}</h2>
      <ul class="point-notes">`;
    for (const pt of (section.points || [])) {
      secHtml += `<li>${pt}</li>`;
    }
    secHtml += `</ul>
    </article>`;
    contentCol.append(secHtml);
    sectionIndex++;
  }

  // Card: High-Yield Key Facts & Chronology
  if (Array.isArray(data.key_facts_revision) && data.key_facts_revision.length > 0) {
    let factsHtml = `<article class="card">
      <h2>${sectionIndex}. Key facts</h2>
      <div class="quick-facts-box">
        <ul class="point-notes">`;
    for (const fact of data.key_facts_revision) {
      factsHtml += `<li>${fact}</li>`;
    }
    factsHtml += `</ul>
      </div>
    </article>`;
    contentCol.append(factsHtml);
    sectionIndex++;
  }

  // Card: Common Misconceptions & Exam Traps
  if (Array.isArray(data.exam_traps_and_distinctions) && data.exam_traps_and_distinctions.length > 0) {
    let trapsHtml = `<article class="card">
      <h2>${sectionIndex}. Common confusions</h2>
      <ul class="point-notes warning-points">`;
    for (const trap of data.exam_traps_and_distinctions) {
      trapsHtml += `<li>${trap}</li>`;
    }
    trapsHtml += `</ul>
    </article>`;
    contentCol.append(trapsHtml);
    sectionIndex++;
  }

  // Card: Topic Self-Assessment Checklist
  const checklistItems = Array.isArray(data.interactive_checklist) && data.interactive_checklist.length > 0
    ? data.interactive_checklist
    : [
        `Master fundamental chronology and sources for ${metadata.title}`,
        `Understand key terms, inscriptions, and archaeological findings`,
        `Review major rulers, thinkers, or socio-economic dynamics`,
        `Solve minimum 20 previous years' questions (PYQ)`,
        `Mark complete on the main syllabus tracker`
      ];

  let checkHtml = `<article class="card">
    <h2>${sectionIndex}. Self-assessment</h2>
    <div class="checklist">`;
  for (const item of checklistItems) {
    checkHtml += `<label class="check-item"><input type="checkbox"> <span>${item}</span></label>`;
  }
  checkHtml += `</div>
  </article>`;
  contentCol.append(checkHtml);

  // Ensure styling for point-notes is present in <style>
  if (!$('style').text().includes('.point-notes')) {
    const additionalCss = `
.point-notes{margin:8px 0 16px 20px;padding:0;display:grid;gap:10px}
.point-notes li{color:var(--ink2);line-height:1.65;font-size:.92rem}
.point-notes li strong{color:var(--ink)}
.quick-facts-box{background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;padding:14px 16px}
.warning-points li{color:#92400e}
.warning-points li strong{color:#78350f}
`;
    $('style').append(additionalCss);
  }

  cleanHistoryCopy($);
  return externalizeHistoryStyles($.html());
}

function inlineText(value) {
  return escapeHtml(value).replace(/\n/g, '<br>');
}

function list(items, className = '') {
  return `<ul${className ? ` class="${className}"` : ''}>${(items || []).map((item) => `<li>${inlineText(item)}</li>`).join('')}</ul>`;
}

function renderChecklist(items) {
  return `<div class="checklist">${(items || []).map((item) => `<label class="check-item"><input type="checkbox"><span>${inlineText(item)}</span></label>`).join('')}</div>`;
}

function safeJson(value) {
  return JSON.stringify(value).replace(/</g, '\\u003c').replace(/>/g, '\\u003e').replace(/&/g, '\\u0026');
}

function renderHistoryConcepts(content) {
  return content.concepts.map((concept, index) => `<section class="notes-section" id="concept-${escapeHtml(concept.id)}">
    <div class="concept-number">Concept ${index + 1}</div>
    <h2>${escapeHtml(concept.title)}</h2>
    <p class="lead-concept">${inlineText(concept.lead)}</p>
    <h3>Details</h3>${list(concept.explanation_points, 'notes-bullet-list')}
    <h3>Remember</h3>${list(concept.key_points, 'notes-bullet-list')}
    <div class="history-callout"><strong>Examples &amp; sources</strong>${list(concept.examples, 'notes-bullet-list')}</div>
    <div class="comparison-callout"><strong>Compare</strong>${list(concept.comparison_points, 'notes-bullet-list')}</div>
    <div class="trap-callout"><strong>Common confusions</strong>${list(concept.common_misconceptions, 'notes-bullet-list')}</div>
    <div class="exam-focus"><strong>Exam points</strong>${list(concept.exam_focus_points, 'notes-bullet-list')}</div>
  </section>`).join('\n');
}

function renderHistoryRevision(revision) {
  const conceptRevisions = revision.concept_revisions.map((item, index) => `<section class="revision-card-box">
    <div class="concept-number">Concept ${index + 1}</div>
    <h2>${escapeHtml(item.title)}</h2>
    <h3>Quick recall</h3>${list(item.pointwise_summary, 'must-remember-list')}
    <h3>Memory aid</h3>${list(item.mnemonics, 'must-remember-list')}
    <h3>Review tips</h3>${list(item.tips, 'must-remember-list')}
    <h3>Quick checks</h3>${list(item.tricks, 'must-remember-list')}
    <h3>Watch for</h3>${list(item.common_traps, 'must-remember-list')}
  </section>`).join('\n');
  const comparisons = revision.comparisons.map((item) => `<div class="revision-comparison"><div><strong>${escapeHtml(item.left)}</strong><span>vs</span><strong>${escapeHtml(item.right)}</strong></div>${list(item.difference_points, 'must-remember-list')}</div>`).join('');
  return `<div class="summary-hero-box"><h2>Rapid revision</h2></div>
    ${conceptRevisions}
    <section class="revision-card-box"><h2>Quick facts</h2>${list(revision.quick_facts, 'must-remember-list')}</section>
    <section class="revision-card-box"><h2>Memory aids</h2>${list(revision.mnemonics, 'must-remember-list')}</section>
    <section class="revision-card-box"><h2>Review tips</h2>${list(revision.tips, 'must-remember-list')}</section>
    <section class="revision-card-box"><h2>Question cues</h2>${list(revision.tricks, 'must-remember-list')}</section>
    <section class="revision-card-box"><h2>Compare</h2><div class="revision-comparisons">${comparisons}</div></section>
    <section class="revision-card-box"><h2>Watch for</h2>${list(revision.exam_traps, 'must-remember-list')}</section>`;
}

const questionTypeNames = {
  mcq: 'MCQ',
  assertion_reason: 'Assertion–Reason',
  true_false: 'True / False',
  fill_blank: 'Fill in the blank',
  match_following: 'Match the following',
  case_based: 'Case-based',
  short_answer: 'Short answer'
};

function renderHistoryQuizQuestion(question, index) {
  const letters = ['A', 'B', 'C', 'D', 'E'];
  let answerBody;
  if (question.type === 'fill_blank') {
    answerBody = `<input class="quiz-answer-input" id="quiz-input-${index}" aria-label="Your answer"><button type="button" class="quiz-check-btn" data-fill="${index}">Check answer</button>`;
  } else if (question.type === 'short_answer') {
    answerBody = `<textarea class="quiz-answer-textarea" id="quiz-input-${index}" aria-label="Your answer"></textarea><button type="button" class="quiz-check-btn" data-short="${index}">Show answer</button>`;
  } else {
    answerBody = `<div class="quiz-options-group">${(question.options || []).map((option, optionIndex) => `<button type="button" class="quiz-option-btn" data-quiz="${index}" data-option="${optionIndex}"><span class="option-letter">${letters[optionIndex] || optionIndex + 1}</span><span class="option-text">${inlineText(option)}</span></button>`).join('')}</div>`;
  }
  return `<article class="quiz-question-card" id="quiz-card-${index}" data-index="${index}" data-type="${escapeHtml(question.type)}">
    <div class="q-header"><span class="q-number">Question ${index + 1}</span><span class="question-type">${questionTypeNames[question.type] || escapeHtml(question.type)}</span></div>
    <p class="q-text">${inlineText(question.question)}</p>${answerBody}<div id="quiz-feedback-${index}" role="status" aria-live="polite"></div>
  </article>`;
}

function renderHistoryTestQuestion(question, index) {
  const letters = ['A', 'B', 'C', 'D', 'E'];
  return `<article class="test-question-card" id="test-card-${index}" data-index="${index}">
    <div class="test-q-header"><span class="t-badge">Question ${index + 1}</span><span class="question-type">${questionTypeNames[question.type] || escapeHtml(question.type)}</span></div>
    <p class="test-question-text">${inlineText(question.question)}</p>
    <div class="quiz-options-group">${question.options.map((option, optionIndex) => `<button type="button" class="test-option-btn quiz-option-btn" data-test="${index}" data-option="${optionIndex}"><span class="option-letter">${letters[optionIndex] || optionIndex + 1}</span><span class="option-text">${inlineText(option)}</span></button>`).join('')}</div>
    <div id="test-feedback-${index}" role="status" aria-live="polite"></div>
  </article>`;
}

export function historyTabCss() {
  return `.history-tab-shell{position:sticky;top:66px;z-index:30;padding:10px 0;background:rgba(246,248,251,.96);backdrop-filter:blur(10px)}
.study-tabs{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:8px;padding:8px;background:#fff;border:1px solid var(--line);border-radius:14px;box-shadow:0 8px 22px rgba(28,39,60,.08)}
.tab-btn{min-height:52px;border:1px solid transparent;border-radius:10px;background:transparent;color:var(--ink2);font:inherit;font-weight:800;cursor:pointer;padding:8px 10px}.tab-btn.active{background:var(--accent-soft);border-color:var(--accent-border);color:var(--accent)}.tab-btn:hover{border-color:var(--accent-border)}.tab-badge{display:inline-block;margin-left:4px;font-size:.7rem;color:var(--muted)}
.tab-panel.hidden,.question-source-data,.hidden{display:none!important}.notes-section h3{margin-top:18px;color:var(--brand);font-size:1rem}.concept-number{display:inline-block;margin-bottom:8px;color:var(--accent);font-size:.74rem;font-weight:900;text-transform:uppercase;letter-spacing:.08em}.lead-concept{font-weight:700;color:var(--brand);font-size:1rem}.history-callout,.comparison-callout,.trap-callout,.exam-focus{padding:14px 16px;border-radius:10px;margin:14px 0;line-height:1.6}.history-callout{background:#eff6ff;border-left:4px solid #2563eb}.comparison-callout{background:#f0fdf4;border-left:4px solid #15803d}.trap-callout{background:#fffbeb;border-left:4px solid #d97706}.exam-focus{background:var(--accent-soft);border-left:4px solid var(--accent)}
.quiz-panel-header,.test-panel-header{display:flex;justify-content:space-between;gap:16px;align-items:center;flex-wrap:wrap}.quiz-live-scoreboard{display:flex;gap:8px;align-items:center}.score-pill,.test-timer-badge{padding:7px 11px;border-radius:999px;background:var(--accent-soft);color:var(--accent);font-weight:800;font-size:.8rem}.btn-reset-quiz,.quiz-check-btn,.btn-submit-test,.btn-retake-test{border:0;border-radius:8px;background:var(--brand);color:#fff;font:inherit;font-weight:800;padding:9px 13px;cursor:pointer}.quiz-questions-list,.test-questions-list{display:grid;gap:14px}.quiz-question-card,.test-question-card,.revision-card-box{background:#fff;border:1px solid var(--line);border-radius:14px;padding:18px}.q-header,.test-q-header{display:flex;justify-content:space-between;gap:10px;align-items:center;flex-wrap:wrap}.q-number,.t-badge{font-size:.76rem;font-weight:900;color:var(--muted);text-transform:uppercase;letter-spacing:.06em}.question-type{display:inline-flex;padding:3px 9px;border-radius:999px;background:var(--accent-soft);color:var(--accent);font-size:.72rem;font-weight:850}.q-text,.test-question-text{font-weight:750;color:var(--ink);line-height:1.6}.quiz-options-group{display:grid;gap:8px}.quiz-option-btn{width:100%;display:flex;gap:10px;align-items:flex-start;text-align:left;border:1px solid var(--line);border-radius:9px;background:#fff;color:var(--ink);padding:10px 12px;font:inherit;cursor:pointer}.quiz-option-btn:hover,.quiz-option-btn.selected{border-color:var(--accent);background:var(--accent-soft)}.quiz-option-btn.correct{border-color:#15803d;background:#f0fdf4}.quiz-option-btn.incorrect{border-color:#b91c1c;background:#fef2f2}.option-letter{font-weight:900;color:var(--accent);min-width:20px}.quiz-answer-input,.quiz-answer-textarea{width:100%;padding:11px 13px;border:1px solid var(--line);border-radius:9px;background:var(--paper);color:var(--ink);font:inherit}.quiz-answer-textarea{min-height:96px;resize:vertical}.quiz-check-btn{margin-top:10px}.quiz-feedback{margin-top:12px}.quiz-feedback.correct{color:#166534}.quiz-feedback.incorrect{color:#991b1b}.test-submit-bar{display:flex;justify-content:flex-end;margin-top:18px}.test-result-modal{margin-top:18px;padding:18px;border:1px solid var(--accent-border);border-radius:14px;background:var(--accent-soft)}.revision-card-box{margin-bottom:14px}.revision-card-box h2{margin-top:0}.revision-card-box h3{color:var(--brand);font-size:.95rem}.must-remember-list{margin-top:8px}.revision-comparisons{display:flex;flex-direction:column;gap:12px}.revision-comparison{padding:14px 16px;border:1px solid var(--line);border-radius:10px;background:var(--paper)}.revision-comparison>div{display:flex;gap:9px;align-items:center;flex-wrap:wrap;color:var(--brand)}.revision-comparison span{color:var(--muted);font-size:.78rem}
@media(max-width:680px){.study-tabs{grid-template-columns:repeat(2,minmax(0,1fr))}.tab-btn{font-size:.78rem}.history-tab-shell{top:58px}}`;
}


export function renderHistoryHtml(originalHtml, data, questions, metadata) {
  const $ = cheerio.load(hydrateHistoryStyles(originalHtml));
  cleanHistoryCopy($);
  const hasAsset = (selector, attribute, source) => $(selector).toArray().some(element => {
    const value = ($(element).attr(attribute) || '').split(/[?#]/)[0];
    return value === source || value === source.replace(/\.(css|js)$/, '.min.$1');
  });
  if (!hasAsset('link[rel="stylesheet"]', 'href', '/assets/css/design-system.css')) {
    $('head').append('<link rel="stylesheet" href="/assets/css/design-system.css">');
  }
  const historyHeader = $('.site-header .header-inner').first();
  const historyBack = historyHeader.find('a.back-btn').first();
  if (historyBack.length && !historyBack.parent().hasClass('header-actions')) {
    historyBack.wrap('<div class="header-actions"></div>');
  }
  const mainGrid = $('.main-grid').first();
  const contentCol = mainGrid.find('.content-col').first();
  if (!mainGrid.length || !contentCol.length) throw new Error('History page is missing .main-grid or .content-col');

  $('.history-tab-shell').remove();
  $('script#history-quiz-data, script#history-test-data, script#history-runtime').remove();
  contentCol.empty();
  mainGrid.before(`<div class="history-tab-shell" data-history-tabs="${TAB_VERSION}"><div class="study-tabs" role="tablist" aria-label="History study tabs">
    <button type="button" class="tab-btn active" role="tab" aria-selected="true" data-tab="tab-notes" id="tab-btn-notes"><span>Study Notes</span></button>
    <button type="button" class="tab-btn" role="tab" aria-selected="false" data-tab="tab-quiz" id="tab-btn-quiz"><span>Concept Quiz</span><span class="tab-badge">${questions.quiz_questions.length}Q</span></button>
    <button type="button" class="tab-btn" role="tab" aria-selected="false" data-tab="tab-summary" id="tab-btn-summary"><span>Revision Summary</span></button>
    <button type="button" class="tab-btn" role="tab" aria-selected="false" data-tab="tab-test" id="tab-btn-test"><span>Mini Test</span><span class="tab-badge">10Q</span></button>
  </div></div>`);

  const checklist = data.concepts.map((concept) => `Explain ${concept.title} from memory.`);
  contentCol.append(`<article class="tab-panel active" id="tab-notes" role="tabpanel" aria-labelledby="tab-btn-notes"><div class="card"><h2>Topic overview</h2>${list(data.introduction_points, 'notes-bullet-list')}</div>${renderHistoryConcepts(data)}<article class="card"><h2>Self-assessment checklist</h2>${renderChecklist(checklist)}</article></article>`);
  contentCol.append(`<article class="tab-panel hidden" id="tab-quiz" role="tabpanel" aria-labelledby="tab-btn-quiz"><div class="card"><div class="quiz-panel-header"><div><h2>Concept Quiz</h2></div><div class="quiz-live-scoreboard"><span class="score-pill" id="quiz-score">Score: 0 / ${questions.quiz_questions.length}</span><button type="button" class="btn-reset-quiz" id="btn-reset-quiz">Reset</button></div></div><div class="quiz-questions-list">${questions.quiz_questions.map(renderHistoryQuizQuestion).join('')}</div></div></article>`);
  contentCol.append(`<article class="tab-panel hidden" id="tab-summary" role="tabpanel" aria-labelledby="tab-btn-summary"><div class="summary-container">${renderHistoryRevision(data.revision)}</div></article>`);
  contentCol.append(`<article class="tab-panel hidden" id="tab-test" role="tabpanel" aria-labelledby="tab-btn-test"><div class="card"><div class="test-panel-header"><div><h2>Mini test · 10 questions</h2></div><span class="test-timer-badge" id="test-timer">10:00</span></div><div class="test-questions-list">${questions.topic_test.map(renderHistoryTestQuestion).join('')}</div><div class="test-submit-bar"><button type="button" class="btn-submit-test" id="btn-submit-test">Submit Test</button></div><div class="test-result-modal hidden" id="test-result"><h3>Test result</h3><p><strong><span id="test-score">0</span> / 10</strong></p><button type="button" class="btn-retake-test" id="btn-retake-test">Retake Test</button></div></div></article>`);

  const tabCss = historyTabCss();
  if (!$('style').text().replace(/\r\n/g, '\n').includes(tabCss.replace(/\r\n/g, '\n'))) {
    $('style').first().append(tabCss);
  }
  $('.exam-badges .history-generated-badge').remove();
  cleanHistoryCopy($);
  $('body').append(`<script type="application/json" id="history-quiz-data">${safeJson(questions.quiz_questions)}</script><script type="application/json" id="history-test-data">${safeJson(questions.topic_test)}</script>${historyRuntimeScript}`);
  if (!hasAsset('script[src]', 'src', '/assets/js/topic-mobile-nav.js')) {
    $('body').append('<script src="/assets/js/topic-mobile-nav.js" defer></script>');
  }
  return externalizeHistoryStyles($.html());
}
