/**
 * ============================================================================
 * SJ Maths — Home Science Topic Test Engine
 * Full-featured timed assessment test engine with navigator, review & analytics
 * ============================================================================
 */

(function () {
  'use strict';

  let testQuestions = [];
  let currentQuestionIdx = 0;
  let userResponses = {}; // { qIdx: optIdx }
  let timerInterval = null;
  let totalTimeSeconds = 600; // 10 minutes default
  let remainingSeconds = 600;
  let testSubmitted = false;

  const container = document.getElementById('topic-test-container');
  if (!container) return;

  async function loadTestData() {
    if (window.HOME_SCIENCE_TEST_DATA && Array.isArray(window.HOME_SCIENCE_TEST_DATA)) {
      testQuestions = window.HOME_SCIENCE_TEST_DATA;
      initTestScreen();
      return;
    }

    try {
      const resp = await fetch('topic-test.json');
      if (resp.ok) {
        testQuestions = await resp.json();
        initTestScreen();
      } else {
        container.innerHTML = '<p class="error-msg">टॉपिक टेस्ट डेटा लोड करने में असमर्थ। कृपया पुनः प्रयास करें।</p>';
      }
    } catch (e) {
      console.warn('topic-test.json fetch failed:', e);
      container.innerHTML = '<p class="error-msg">टॉपिक टेस्ट डेटा लोड करने में असमर्थ।</p>';
    }
  }

  function initTestScreen() {
    if (!testQuestions || testQuestions.length === 0) {
      container.innerHTML = '<p>इस टॉपिक के लिए टेस्ट उपलब्ध नहीं है।</p>';
      return;
    }

    totalTimeSeconds = Math.max(300, testQuestions.length * 60); // 1 minute per question
    remainingSeconds = totalTimeSeconds;

    container.innerHTML = `
      <div class="test-start-view" id="test-start-view">
        <div class="test-start-icon">⏱️</div>
        <h2>टॉपिक मॉक टेस्ट (Topic Mock Test)</h2>
        <p>अपनी वास्तविक परीक्षा तैयारी का मूल्यांकन करें। यह टेस्ट परीक्षा के वातावरण के अनुरूप समयबद्ध है।</p>
        
        <div class="test-rules-grid">
          <div class="test-rule-item">
            <strong>${testQuestions.length}</strong>
            <span>कुल प्रश्न</span>
          </div>
          <div class="test-rule-item">
            <strong>${Math.round(totalTimeSeconds / 60)} मिनट</strong>
            <span>कुल समय</span>
          </div>
          <div class="test-rule-item">
            <strong>60%</strong>
            <span>उत्तीर्ण अंक</span>
          </div>
          <div class="test-rule-item">
            <strong>शून्य</strong>
            <span>नेगेटिव मार्किंग</span>
          </div>
        </div>

        <button type="button" class="start-test-btn" id="btn-start-test">
          टेस्ट शुरू करें (Start Test) →
        </button>
      </div>

      <div class="test-active-view" id="test-active-view">
        <div class="test-header-bar">
          <div>
            <strong style="color:var(--brand);font-size:1.05rem;">टॉपिक टेस्ट (Active Test)</strong>
            <span style="color:var(--muted);font-size:0.8rem;display:block;">प्रश्न <span id="active-q-num">1</span> / ${testQuestions.length}</span>
          </div>
          <div class="test-timer" id="test-timer-badge">
            <span>⏳</span> <span id="test-time-text">10:00</span>
          </div>
        </div>

        <!-- Question Navigator Dots -->
        <div class="test-nav-matrix" id="test-nav-matrix"></div>

        <!-- Question Area -->
        <div id="test-question-box"></div>

        <!-- Controls Row -->
        <div class="test-controls-row">
          <button type="button" class="test-ctrl-btn" id="btn-test-prev">← पिछला (Previous)</button>
          <div>
            <button type="button" class="test-ctrl-btn" id="btn-test-clear" style="margin-right:8px;font-size:0.8rem;">उत्तर हटाएं (Clear)</button>
            <button type="button" class="test-submit-btn" id="btn-test-submit">टेस्ट सबमिट करें (Submit Test)</button>
          </div>
          <button type="button" class="test-ctrl-btn" id="btn-test-next">अगला (Next) →</button>
        </div>
      </div>

      <div class="test-result-view" id="test-result-view"></div>
    `;

    document.getElementById('btn-start-test').addEventListener('click', startTest);
  }

  function startTest() {
    testSubmitted = false;
    userResponses = {};
    currentQuestionIdx = 0;
    remainingSeconds = totalTimeSeconds;

    document.getElementById('test-start-view').style.display = 'none';
    document.getElementById('test-active-view').style.display = 'block';
    document.getElementById('test-result-view').style.display = 'none';

    renderNavMatrix();
    renderActiveQuestion();
    startTimer();
    attachActiveListeners();
  }

  function startTimer() {
    if (timerInterval) clearInterval(timerInterval);
    updateTimerDisplay();

    timerInterval = setInterval(function () {
      remainingSeconds--;
      updateTimerDisplay();

      if (remainingSeconds <= 0) {
        clearInterval(timerInterval);
        submitTest(true);
      }
    }, 1000);
  }

  function updateTimerDisplay() {
    const mins = Math.floor(remainingSeconds / 60);
    const secs = remainingSeconds % 60;
    const timeStr = `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
    const el = document.getElementById('test-time-text');
    if (el) el.textContent = timeStr;

    const badge = document.getElementById('test-timer-badge');
    if (badge) {
      if (remainingSeconds <= 120) {
        badge.style.background = '#fef2f2';
        badge.style.color = '#dc2626';
        badge.style.borderColor = '#f87171';
      } else {
        badge.style.background = '#f8fafc';
        badge.style.color = '#1e293b';
        badge.style.borderColor = '#cbd5e1';
      }
    }
  }

  function renderNavMatrix() {
    const matrix = document.getElementById('test-nav-matrix');
    if (!matrix) return;

    let html = '';
    testQuestions.forEach(function (q, idx) {
      let cls = 'test-nav-dot';
      if (idx === currentQuestionIdx) cls += ' active';
      if (userResponses[idx] !== undefined) cls += ' answered';

      html += `<button type="button" class="${cls}" data-goto-q="${idx}">${idx + 1}</button>`;
    });
    matrix.innerHTML = html;

    matrix.querySelectorAll('[data-goto-q]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        currentQuestionIdx = parseInt(btn.getAttribute('data-goto-q'), 10);
        renderNavMatrix();
        renderActiveQuestion();
      });
    });
  }

  function renderActiveQuestion() {
    const box = document.getElementById('test-question-box');
    if (!box) return;

    const q = testQuestions[currentQuestionIdx];
    const letters = ['A', 'B', 'C', 'D'];
    const currentAns = userResponses[currentQuestionIdx];

    const isHi = (document.documentElement.getAttribute('data-lang') || 'en') === 'hi';
    const qText = (isHi && q.question_hi) ? q.question_hi : q.question;
    const opts = (isHi && Array.isArray(q.options_hi) && q.options_hi.length === 4) ? q.options_hi : q.options;

    document.getElementById('active-q-num').textContent = String(currentQuestionIdx + 1);

    let html = `
      <div style="margin:20px 0 16px;">
        <span style="font-size:0.75rem;font-weight:800;color:var(--muted);text-transform:uppercase;letter-spacing:0.06em;">
          ${isHi ? 'प्रश्न' : 'Question'} ${currentQuestionIdx + 1} / ${testQuestions.length} ${q.difficulty ? `• [${q.difficulty}]` : ''}
        </span>
        <h3 style="font-size:1.1rem;color:var(--brand);margin:8px 0 16px;line-height:1.5;">
          ${escapeHtml(qText)}
        </h3>
      </div>

      <div class="quiz-options">
        ${opts.map(function (opt, optIdx) {
          const isSelected = currentAns === optIdx;
          const selClass = isSelected ? 'style="background:#eff6ff;border-color:#2563eb;font-weight:700;"' : '';
          return `
            <button type="button" class="quiz-opt" ${selClass} data-test-opt="${optIdx}">
              <span class="quiz-opt-letter" ${isSelected ? 'style="background:#2563eb;color:#fff;"' : ''}>${letters[optIdx]}</span>
              <span>${escapeHtml(opt)}</span>
            </button>
          `;
        }).join('')}
      </div>
    `;

    box.innerHTML = html;

    box.querySelectorAll('[data-test-opt]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        const optIdx = parseInt(btn.getAttribute('data-test-opt'), 10);
        userResponses[currentQuestionIdx] = optIdx;
        renderNavMatrix();
        renderActiveQuestion();
      });
    });

    // Update prev/next button states
    const prevBtn = document.getElementById('btn-test-prev');
    const nextBtn = document.getElementById('btn-test-next');
    if (prevBtn) prevBtn.disabled = currentQuestionIdx === 0;
    if (nextBtn) nextBtn.disabled = currentQuestionIdx === testQuestions.length - 1;
  }

  function attachActiveListeners() {
    document.getElementById('btn-test-prev').addEventListener('click', function () {
      if (currentQuestionIdx > 0) {
        currentQuestionIdx--;
        renderNavMatrix();
        renderActiveQuestion();
      }
    });

    document.getElementById('btn-test-next').addEventListener('click', function () {
      if (currentQuestionIdx < testQuestions.length - 1) {
        currentQuestionIdx++;
        renderNavMatrix();
        renderActiveQuestion();
      }
    });

    document.getElementById('btn-test-clear').addEventListener('click', function () {
      delete userResponses[currentQuestionIdx];
      renderNavMatrix();
      renderActiveQuestion();
    });

    document.getElementById('btn-test-submit').addEventListener('click', function () {
      const answeredCount = Object.keys(userResponses).length;
      const unattempted = testQuestions.length - answeredCount;

      let msg = 'क्या आप टेस्ट सबमिट करना चाहते हैं?';
      if (unattempted > 0) {
        msg = `आपके ${unattempted} प्रश्न अनुत्तरित (unanswered) हैं। क्या आप निश्चित रूप से टेस्ट सबमिट करना चाहते हैं?`;
      }

      if (window.confirm(msg)) {
        submitTest(false);
      }
    });
  }

  function submitTest(autoSubmitted) {
    if (timerInterval) clearInterval(timerInterval);
    testSubmitted = true;

    const timeSpentSeconds = totalTimeSeconds - remainingSeconds;
    const timeSpentMins = Math.floor(timeSpentSeconds / 60);
    const timeSpentSecs = timeSpentSeconds % 60;
    const timeFormatted = `${timeSpentMins} मिनट ${timeSpentSecs} सेकंड`;

    let correctCount = 0;
    let incorrectCount = 0;
    let unattemptedCount = 0;

    testQuestions.forEach(function (q, idx) {
      const ans = userResponses[idx];
      if (ans === undefined) {
        unattemptedCount++;
      } else if (ans === q.correct_index) {
        correctCount++;
      } else {
        incorrectCount++;
      }
    });

    const scorePct = Math.round((correctCount / testQuestions.length) * 100);
    const attemptedCount = correctCount + incorrectCount;
    const accuracyPct = attemptedCount > 0 ? Math.round((correctCount / attemptedCount) * 100) : 0;
    const passed = scorePct >= 60;

    // Update TopicProgress
    if (window.TopicProgress) {
      const prev = window.TopicProgress.get();
      const best = Math.max(prev.testBestScore || 0, scorePct);
      window.TopicProgress.set('testBestScore', best);
      window.TopicProgress.set('testPassed', best >= 60);
    }

    renderResultView({
      scorePct,
      correctCount,
      incorrectCount,
      unattemptedCount,
      accuracyPct,
      timeFormatted,
      passed,
      autoSubmitted
    });
  }

  function renderResultView(data) {
    document.getElementById('test-active-view').style.display = 'none';
    const resultView = document.getElementById('test-result-view');
    resultView.style.display = 'block';

    resultView.innerHTML = `
      <div class="test-result-score-circle" style="background:${data.passed ? 'linear-gradient(135deg, #15803d, #10b981)' : 'linear-gradient(135deg, #b91c1c, #ef4444)'}">
        <div class="test-result-score">${data.scorePct}%</div>
        <div class="test-result-score-label">${data.passed ? 'उत्तीर्ण (PASSED)' : 'सुधार आवश्यक'}</div>
      </div>

      <h2 style="margin:0 0 6px;color:var(--brand);font-size:1.35rem;">
        ${data.passed ? 'बधाई हो! आपने टेस्ट उत्तीर्ण किया।' : 'अभ्यास जारी रखें!'}
      </h2>
      <p style="color:var(--muted);margin:0 0 24px;font-size:0.9rem;">
        ${data.autoSubmitted ? 'समय समाप्त होने पर टेस्ट स्वतः सबमिट हुआ।' : 'आपका टेस्ट सफलतापूर्वक सबमिट हुआ।'}
      </p>

      <div class="test-metrics-grid">
        <div class="test-metric-card">
          <strong style="color:var(--success);">${data.correctCount}</strong>
          <span>सही उत्तर</span>
        </div>
        <div class="test-metric-card">
          <strong style="color:var(--error);">${data.incorrectCount}</strong>
          <span>गलत उत्तर</span>
        </div>
        <div class="test-metric-card">
          <strong style="color:var(--muted);">${data.unattemptedCount}</strong>
          <span>छोड़े गए प्रश्न</span>
        </div>
        <div class="test-metric-card">
          <strong style="color:var(--brand);">${data.accuracyPct}%</strong>
          <span>सटीकता (Accuracy)</span>
        </div>
        <div class="test-metric-card">
          <strong style="color:var(--brand);font-size:1.05rem;">${data.timeFormatted}</strong>
          <span>उपयोग हुआ समय</span>
        </div>
      </div>

      <div class="test-result-actions">
        <button type="button" class="retake-test-btn" id="btn-retake-test">
          🔄 पुनः टेस्ट दें (Retake Test)
        </button>
        <button type="button" class="review-test-btn" id="btn-review-test">
          📝 विस्तृत समाधान देखें (Review Solutions)
        </button>
      </div>

      <div id="test-review-container" style="display:none;margin-top:36px;text-align:left;"></div>
    `;

    document.getElementById('btn-retake-test').addEventListener('click', startTest);
    document.getElementById('btn-review-test').addEventListener('click', toggleReviewSolutions);
  }

  function toggleReviewSolutions() {
    const revBox = document.getElementById('test-review-container');
    if (!revBox) return;

    if (revBox.style.display === 'block') {
      revBox.style.display = 'none';
      document.getElementById('btn-review-test').textContent = '📝 विस्तृत समाधान देखें (Review Solutions)';
      return;
    }

    revBox.style.display = 'block';
    document.getElementById('btn-review-test').textContent = 'छिपाएं (Hide Review)';

    const letters = ['A', 'B', 'C', 'D'];
    let html = `
      <div style="padding:14px 18px;background:#f8fafc;border:1px solid var(--line);border-radius:var(--radius);margin-bottom:20px;">
        <h3 style="margin:0;color:var(--brand);font-size:1.1rem;">विस्तृत प्रश्न समीक्षा एवं समाधान (Detailed Review)</h3>
      </div>
    `;

    testQuestions.forEach(function (q, idx) {
      const userAns = userResponses[idx];
      const isUnanswered = userAns === undefined;
      const isCorrect = !isUnanswered && userAns === q.correct_index;

      html += `
        <article class="quiz-item" style="border-left:4px solid ${isCorrect ? 'var(--success)' : (isUnanswered ? 'var(--muted)' : 'var(--error)')};">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
            <div class="quiz-qno">प्रश्न ${idx + 1} / ${testQuestions.length}</div>
            <span style="font-size:0.75rem;font-weight:800;color:${isCorrect ? 'var(--success)' : (isUnanswered ? 'var(--muted)' : 'var(--error)')};">
              ${isCorrect ? '✓ सही (+1)' : (isUnanswered ? '○ अनुत्तरित (0)' : '✗ गलत (0)')}
            </span>
          </div>
          
          <div class="quiz-question">${escapeHtml(q.question)}</div>

          <div class="quiz-options">
            ${q.options.map(function (opt, optIdx) {
              let optClass = 'quiz-opt';
              if (optIdx === q.correct_index) {
                optClass += ' correct';
              } else if (optIdx === userAns) {
                optClass += ' incorrect';
              }
              return `
                <div class="${optClass}" style="cursor:default;">
                  <span class="quiz-opt-letter">${letters[optIdx]}</span>
                  <span>${escapeHtml(opt)}</span>
                  ${optIdx === q.correct_index ? '<strong style="margin-left:auto;color:var(--success);font-size:0.8rem;">(सही उत्तर)</strong>' : ''}
                  ${optIdx === userAns && optIdx !== q.correct_index ? '<strong style="margin-left:auto;color:var(--error);font-size:0.8rem;">(आपका उत्तर)</strong>' : ''}
                </div>
              `;
            }).join('')}
          </div>

          <div class="quiz-feedback show correct" style="margin-top:14px;">
            <strong>व्याख्या (Solution & Explanation):</strong>
            <p style="margin:6px 0 0;">${escapeHtml(q.explanation || 'व्याख्या उपलब्ध है।')}</p>
          </div>
        </article>
      `;
    });

    revBox.innerHTML = html;
  }

  function escapeHtml(str) {
    if (!str) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  window.addEventListener('topic:tabchange', function (e) {
    if (e.detail && e.detail.tabId === 'topic-test') {
      if (testQuestions.length === 0) {
        loadTestData();
      }
    }
  });

  document.addEventListener('DOMContentLoaded', function () {
    const testPanel = document.getElementById('topic-test');
    if (testPanel && !testPanel.hidden) {
      loadTestData();
    }
  });

  window.addEventListener('sjmaths:langchange', function () {
    if (testQuestions && testQuestions.length > 0) {
      var activeBox = document.getElementById('test-question-box');
      if (activeBox && activeBox.innerHTML.trim() !== '') {
        renderActiveQuestion();
      }
    }
  });
})();
