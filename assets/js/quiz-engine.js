/**
 * ============================================================================
 * SJ Maths — Home Science Practice Quiz Engine
 * Interactive learning-mode MCQ engine with immediate feedback & hints
 * ============================================================================
 */

(function () {
  'use strict';

  let quizQuestions = [];
  let userAnswers = {};
  let hintsRevealed = {};

  const container = document.getElementById('quiz-container');
  if (!container) return;

  async function loadQuizData() {
    // If inline data is provided, use it
    if (window.HOME_SCIENCE_QUIZ_DATA && Array.isArray(window.HOME_SCIENCE_QUIZ_DATA)) {
      quizQuestions = window.HOME_SCIENCE_QUIZ_DATA;
      renderQuiz();
      return;
    }

    // Otherwise load from quiz.json in same folder
    try {
      const resp = await fetch('quiz.json');
      if (resp.ok) {
        quizQuestions = await resp.json();
        renderQuiz();
      } else {
        container.innerHTML = '<p class="error-msg">क्विज़ डेटा लोड करने में त्रुटि हुई। कृपया पेज रीफ़्रेश करें।</p>';
      }
    } catch (err) {
      console.warn('quiz.json fetch failed:', err);
      container.innerHTML = '<p class="error-msg">क्विज़ डेटा लोड करने में त्रुटि हुई।</p>';
    }
  }

  function renderQuiz() {
    if (!quizQuestions || quizQuestions.length === 0) {
      container.innerHTML = '<p>इस टॉपिक के लिए क्विज़ उपलब्ध नहीं है।</p>';
      return;
    }

    const letters = ['A', 'B', 'C', 'D'];
    let html = `
      <div class="quiz-header">
        <div>
          <strong style="color:var(--brand);font-size:1.05rem;">अभ्यास क्विज़ (Practice Quiz)</strong>
          <span style="color:var(--muted);font-size:0.82rem;display:block;">सीखने का मोड • तत्काल समाधान एवं व्याख्या</span>
        </div>
        <div class="quiz-score-badge" id="quiz-live-score">कुल प्रश्न: ${quizQuestions.length}</div>
    var currentLang = document.documentElement.getAttribute('data-lang') || 'en';
    const isHi = currentLang === 'hi';

    quizQuestions.forEach(function (q, idx) {
      const ans = userAnswers[idx];
      const isAnswered = ans !== undefined;
      const isCorrect = isAnswered && ans === q.correct_index;

      const qText = (isHi && q.question_hi) ? q.question_hi : q.question;
      const opts = (isHi && Array.isArray(q.options_hi) && q.options_hi.length === 4) ? q.options_hi : q.options;
      const hintText = (isHi && q.hint_hi) ? q.hint_hi : q.hint;
      const expText = (isHi && q.explanation_hi) ? q.explanation_hi : (q.explanation || '');

      html += `
        <article class="quiz-item" id="quiz-item-${idx}">
          <div class="quiz-qno">${isHi ? 'प्रश्न' : 'Question'} ${idx + 1} / ${quizQuestions.length}</div>
          <div class="quiz-question">${escapeHtml(qText)}</div>
          
          <div class="quiz-options">
            ${opts.map(function (opt, optIdx) {
              let optClass = 'quiz-opt';
              if (isAnswered) {
                if (optIdx === q.correct_index) {
                  optClass += ' correct';
                } else if (optIdx === ans) {
                  optClass += ' incorrect';
                }
              }
              const disabled = isAnswered ? 'disabled' : '';
              return `
                <button type="button" class="${optClass}" ${disabled} data-q="${idx}" data-opt="${optIdx}">
                  <span class="quiz-opt-letter">${letters[optIdx]}</span>
                  <span>${escapeHtml(opt)}</span>
                </button>
              `;
            }).join('')}
          </div>

          <div class="quiz-actions">
            ${hintText ? `
              <button type="button" class="quiz-hint-btn" data-hint-q="${idx}">
                💡 ${isHi ? 'संकेत (Hint)' : 'Hint'}
              </button>
            ` : '<div></div>'}
            
            ${isAnswered ? `
              <button type="button" class="test-ctrl-btn" data-retry-q="${idx}" style="font-size:0.78rem;padding:5px 12px;">
                ${isHi ? 'पुनः प्रयास करें (Retry)' : 'Retry Question'}
              </button>
            ` : ''}
          </div>

          ${hintText ? `
            <div class="quiz-hint-box ${hintsRevealed[idx] ? 'show' : ''}" id="quiz-hint-${idx}">
              <strong>${isHi ? 'संकेत:' : 'Hint:'}</strong> ${escapeHtml(hintText)}
            </div>
          ` : ''}

          <div class="quiz-feedback ${isAnswered ? 'show' : ''} ${isAnswered ? (isCorrect ? 'correct' : 'incorrect') : ''}" id="quiz-feedback-${idx}">
            ${isAnswered ? `
              <strong>${isCorrect ? (isHi ? '✓ सही उत्तर!' : '✓ Correct!') : (isHi ? '✗ गलत उत्तर!' : '✗ Incorrect!')}</strong>
              <p style="margin:6px 0 0;">${escapeHtml(expText)}</p>
            ` : ''}
          </div>
        </article>
      `;
    });

    container.innerHTML = html;
    attachEventListeners();
    updateQuizScore();
  }

  function attachEventListeners() {
    // Option click
    container.querySelectorAll('.quiz-opt:not(:disabled)').forEach(function (btn) {
      btn.addEventListener('click', function () {
        const qIdx = parseInt(btn.getAttribute('data-q'), 10);
        const optIdx = parseInt(btn.getAttribute('data-opt'), 10);
        handleAnswer(qIdx, optIdx);
      });
    });

    // Hint button click
    container.querySelectorAll('.quiz-hint-btn').forEach(function (btn) {
      btn.addEventListener('click', function () {
        const qIdx = parseInt(btn.getAttribute('data-hint-q'), 10);
        hintsRevealed[qIdx] = !hintsRevealed[qIdx];
        const hintBox = document.getElementById('quiz-hint-' + qIdx);
        if (hintBox) {
          hintBox.classList.toggle('show', hintsRevealed[qIdx]);
        }
      });
    });

    // Retry question click
    container.querySelectorAll('[data-retry-q]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        const qIdx = parseInt(btn.getAttribute('data-retry-q'), 10);
        delete userAnswers[qIdx];
        renderQuiz();
      });
    });
  }

  function handleAnswer(qIdx, optIdx) {
    userAnswers[qIdx] = optIdx;
    renderQuiz();

    // Scroll slightly if feedback is not visible
    const card = document.getElementById('quiz-item-' + qIdx);
    if (card) {
      card.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
  }

  function updateQuizScore() {
    const answeredCount = Object.keys(userAnswers).length;
    if (answeredCount === 0) return;

    let correctCount = 0;
    Object.keys(userAnswers).forEach(function (idx) {
      const q = quizQuestions[parseInt(idx, 10)];
      if (q && userAnswers[idx] === q.correct_index) {
        correctCount++;
      }
    });

    const pct = Math.round((correctCount / quizQuestions.length) * 100);
    const scoreEl = document.getElementById('quiz-live-score');
    if (scoreEl) {
      scoreEl.innerHTML = `स्कोर: <strong>${correctCount} / ${quizQuestions.length}</strong> (${pct}%)`;
    }

    if (window.TopicProgress) {
      const prev = window.TopicProgress.get();
      const best = Math.max(prev.quizBestScore || 0, pct);
      const passed = best >= 70;
      window.TopicProgress.set('quizBestScore', best);
      window.TopicProgress.set('quizPassed', passed);
    }
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

  // Listen for tab switch to quiz tab
  window.addEventListener('topic:tabchange', function (e) {
    if (e.detail && e.detail.tabId === 'quiz') {
      if (quizQuestions.length === 0) {
        loadQuizData();
      }
    }
  });

  // Initial check
  document.addEventListener('DOMContentLoaded', function () {
    const quizPanel = document.getElementById('quiz');
    if (quizPanel && !quizPanel.hidden) {
      loadQuizData();
    }
  });

  // Listen for language changes
  window.addEventListener('sjmaths:langchange', function () {
    if (quizQuestions && quizQuestions.length > 0) {
      renderQuiz();
    }
  });
})();
