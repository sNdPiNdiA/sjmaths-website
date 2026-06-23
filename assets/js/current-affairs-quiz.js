// Interactive Quiz Engine for SJMaths Current Affairs
class CurrentAffairsQuiz {
  constructor(containerId, options = {}) {
    this.container = document.getElementById(containerId);
    if (!this.container) return;

    this.date = options.date || this.getTodayIST();
    this.timeLimit = options.timeLimit || 300; // 5 minutes standard
    this.questions = [];
    this.currentIdx = 0;
    this.userAnswers = {}; // questionIndex -> selectedOptionIndex
    this.timeRemaining = this.timeLimit;
    this.timerInterval = null;
    this.isSubmitted = false;

    // Listen for language toggles to refresh rendering instantly
    window.addEventListener('ca-lang-changed', () => {
      if (this.questions.length > 0) {
        if (this.isSubmitted) {
          this.submitQuiz(false, true); // Redisplay submission page
        } else {
          this.renderQuizFrame();
          this.renderQuestion(this.currentIdx);
        }
      }
    });

    this.init();
  }

  // Helper to translate quiz strings on the fly
  getQuizText(key, enVal) {
    const translations = {
      'loading': { hi: 'प्रश्नोत्तरी प्रश्न लोड हो रहे हैं...', en: 'Loading Quiz Questions...' },
      'unavailable': { hi: 'प्रश्नोत्तरी अनुपलब्ध', en: 'Quiz Unavailable' },
      'unavailable_desc': { hi: 'चयनित तिथि के लिए कोई प्रश्नोत्तरी उपलब्ध नहीं है। कृपया कोई अन्य तिथि चुनें या बाद में दोबारा जांचें।', en: 'No quiz questions are available for the selected date.' },
      'retry': { hi: 'पुनः प्रयास करें', en: 'Retry' },
      'title': { hi: 'दैनिक त्वरित प्रश्नोत्तरी', en: 'Daily Quick Quiz' },
      'question_of': { hi: 'प्रश्न {current} का {total}', en: 'Question {current} of {total}' },
      'prev': { hi: 'पिछला', en: 'Previous' },
      'next': { hi: 'अगला', en: 'Next' },
      'submit': { hi: 'प्रश्नोत्तरी सबमिट करें', en: 'Submit Quiz' },
      'explanation': { hi: 'स्पष्टीकरण', en: 'Explanation' },
      'completed': { hi: 'प्रश्नोत्तरी पूर्ण!', en: 'Quiz Completed!' },
      'times_up': { hi: 'समय समाप्त!', en: "Time's Up!" },
      'passed': { hi: 'उत्तीर्ण', en: 'Passed' },
      'needs_practice': { hi: 'अभ्यास की आवश्यकता है', en: 'Needs Practice' },
      'passed_desc': { hi: 'उत्कृष्ट! आज के समाचारों पर आपकी अच्छी पकड़ है। यह सिलसिला बनाए रखें!', en: "Excellent! You have a solid grasp of today's news events. Keep maintaining this streak!" },
      'fail_desc': { hi: 'अच्छा प्रयास। अपनी समझ को मजबूत करने के लिए छूटे हुए प्रश्नों के विस्तृत स्पष्टीकरण की समीक्षा करें।', en: 'Good attempt. Review the detailed explanations of the questions you missed to reinforce your knowledge.' },
      'review_answers': { hi: 'उत्तरों की समीक्षा करें', en: 'Review Answers' },
      'retake': { hi: 'पुनः प्रयास करें', en: 'Retake' },
      'submitted': { hi: 'सबमिट कर दिया गया', en: 'Submitted' }
    };
    
    const isHi = document.body.classList.contains('lang-hi');
    const tr = translations[key];
    if (!tr) return enVal;
    return isHi ? tr.hi : tr.en;
  }

  // Helper to get today's date in YYYY-MM-DD IST format
  getTodayIST() {
    const date = new Date();
    const tzOffset = 5.5 * 60 * 60 * 1000;
    const istTime = date.getTime() + date.getTimezoneOffset() * 60000 + tzOffset;
    const istDate = new Date(istTime);
    const yyyy = istDate.getFullYear();
    const mm = String(istDate.getMonth() + 1).padStart(2, '0');
    const dd = String(istDate.getDate()).padStart(2, '0');
    return `${yyyy}-${mm}-${dd}`;
  }

  async init() {
    this.renderLoading();
    const fetched = await this.fetchQuestions();
    if (!fetched || this.questions.length === 0) {
      this.renderError();
      return;
    }

    this.renderQuizFrame();
    this.renderQuestion(0);
    this.startTimer();
  }

  renderLoading() {
    this.container.innerHTML = `
      <div style="text-align: center; padding: 3rem;">
        <i class="fas fa-spinner fa-spin" style="font-size: 3rem; color: var(--primary); margin-bottom: 1rem;"></i>
        <p>${this.getQuizText('loading', 'Loading Quiz Questions...')}</p>
      </div>
    `;
  }

  renderError() {
    this.container.innerHTML = `
      <div class="ca-results-card" style="padding: 2rem;">
        <i class="fas fa-exclamation-triangle" style="font-size: 3rem; color: var(--secondary); margin-bottom: 1rem;"></i>
        <h2>${this.getQuizText('unavailable', 'Quiz Unavailable')}</h2>
        <p>${this.getQuizText('unavailable_desc', 'No quiz questions are available for the selected date')} (${this.date}).</p>
        <button onclick="location.reload()" class="ca-date-btn" style="margin-top: 1rem; border: none; cursor: pointer;">
          <i class="fas fa-redo"></i> ${this.getQuizText('retry', 'Retry')}
        </button>
      </div>
    `;
  }

  async fetchQuestions() {
    // Try to fetch quiz data. If not found, try to search up to 7 days back.
    let targetDate = new Date(this.date);
    let attempts = 0;

    while (attempts < 7) {
      const yyyy = targetDate.getFullYear();
      const mm = String(targetDate.getMonth() + 1).padStart(2, '0');
      const dd = String(targetDate.getDate()).padStart(2, '0');
      const dateStr = `${yyyy}-${mm}-${dd}`;
      const url = `/current-affairs/data/mcqs/${dateStr}.json`;

      try {
        console.log(`Trying to fetch quiz from: ${url}`);
        const res = await fetch(url);
        if (res.ok) {
          const data = await res.json();
          if (data && data.length > 0) {
            this.questions = data;
            this.date = dateStr;
            return true;
          }
        }
      } catch (err) {
        console.error(`Fetch error for ${dateStr}:`, err);
      }

      // Move one day back
      targetDate.setDate(targetDate.getDate() - 1);
      attempts++;
    }
    return false;
  }

  renderQuizFrame() {
    const titleText = this.getQuizText('title', 'Daily Quick Quiz');
    const progressText = this.getQuizText('question_of', 'Question {current} of {total}')
      .replace('{current}', this.currentIdx + 1)
      .replace('{total}', this.questions.length);
    const prevText = this.getQuizText('prev', 'Previous');
    const nextText = this.getQuizText('next', 'Next');

    this.container.innerHTML = `
      <div class="ca-quiz-header">
        <div>
          <h2 style="font-family: 'Outfit', sans-serif;">${titleText} — ${this.date}</h2>
          <p class="ca-quiz-progress" id="quiz-progress-text">${progressText}</p>
        </div>
        <div class="ca-quiz-timer" id="quiz-timer-display">
          <i class="fas fa-clock"></i> 05:00
        </div>
      </div>

      <!-- Question Container -->
      <div id="quiz-question-container"></div>

      <!-- Footer Navigation Controls -->
      <div class="ca-quiz-controls">
        <button class="ca-quiz-btn ca-quiz-btn-prev" id="quiz-btn-prev" disabled>
          <i class="fas fa-arrow-left"></i> ${prevText}
        </button>
        <button class="ca-quiz-btn ca-quiz-btn-next" id="quiz-btn-next">
          ${nextText} <i class="fas fa-arrow-right"></i>
        </button>
      </div>

      <!-- Question Grid Navigator -->
      <div style="margin-top: 2rem; display: flex; flex-wrap: wrap; gap: 0.5rem; justify-content: center;" id="quiz-grid-navigator">
        ${this.questions.map((_, idx) => `
          <button class="ca-category-pill" style="min-width: 40px; padding: 0.5rem; justify-content: center;" data-target="${idx}" id="grid-nav-${idx}">
            ${idx + 1}
          </button>
        `).join('')}
      </div>
    `;

    // Hook events
    document.getElementById('quiz-btn-prev').addEventListener('click', () => this.navigate(-1));
    document.getElementById('quiz-btn-next').addEventListener('click', () => this.navigate(1));
    
    document.getElementById('quiz-grid-navigator').addEventListener('click', (e) => {
      const btn = e.target.closest('button');
      if (btn) {
        const targetIdx = parseInt(btn.dataset.target, 10);
        this.navigate(targetIdx - this.currentIdx);
      }
    });

    const qContainer = document.getElementById('quiz-question-container');
    if (qContainer && !qContainer.dataset.bound) {
      qContainer.dataset.bound = '1';
      qContainer.addEventListener('click', (e) => {
        const opt = e.target.closest('.ca-mcq-option');
        if (!opt || this.isSubmitted) return;
        const selected = parseInt(opt.dataset.optIdx, 10);
        this.userAnswers[this.currentIdx] = selected;
        this.renderQuestion(this.currentIdx);
      });
    }

    if (this.isSubmitted) {
      const timerDisplay = document.getElementById('quiz-timer-display');
      if (timerDisplay) {
        timerDisplay.innerHTML = `<i class="fas fa-check-circle"></i> ${this.getQuizText('submitted', 'Submitted')}`;
        timerDisplay.style.color = '#2ecc71';
        timerDisplay.style.background = 'rgba(46, 204, 113, 0.1)';
      }
    } else {
      this.updateTimerDisplay();
    }
  }

  renderQuestion(index) {
    if (index < 0 || index >= this.questions.length) return;
    this.currentIdx = index;

    // Update controls & navigation
    const prevBtn = document.getElementById('quiz-btn-prev');
    const nextBtn = document.getElementById('quiz-btn-next');
    
    prevBtn.disabled = index === 0;
    
    if (index === this.questions.length - 1) {
      nextBtn.innerHTML = `${this.getQuizText('submit', 'Submit Quiz')} <i class="fas fa-check-circle"></i>`;
      nextBtn.className = 'ca-quiz-btn ca-quiz-btn-submit';
    } else {
      nextBtn.innerHTML = `${this.getQuizText('next', 'Next')} <i class="fas fa-arrow-right"></i>`;
      nextBtn.className = 'ca-quiz-btn ca-quiz-btn-next';
    }

    // Update progress text
    document.getElementById('quiz-progress-text').textContent = this.getQuizText('question_of', 'Question {current} of {total}')
      .replace('{current}', index + 1)
      .replace('{total}', this.questions.length);

    // Highlight active in grid
    this.questions.forEach((_, idx) => {
      const gridBtn = document.getElementById(`grid-nav-${idx}`);
      if (gridBtn) {
        gridBtn.classList.remove('active');
        if (idx === index) {
          gridBtn.classList.add('active');
        } else if (this.userAnswers[idx] !== undefined) {
          // If already answered, color differently
          gridBtn.style.border = '2px solid var(--primary)';
        }
      }
    });

    const q = this.questions[index];
    const qContainer = document.getElementById('quiz-question-container');
    const selectedAnswer = this.userAnswers[index];

    qContainer.innerHTML = `
      <div class="ca-mcq-card">
        <div class="ca-card-meta">
          <span class="ca-card-source"><i class="fas fa-tag"></i> ${q.category.toUpperCase()}</span>
          <span class="ca-badge ca-badge-importance-high" style="text-transform: capitalize;">${q.difficulty}</span>
        </div>
        <div class="ca-mcq-question">${index + 1}. ${q.question}</div>
        <div class="ca-mcq-options">
          ${q.options.map((option, optIdx) => {
            let extraClass = '';
            if (this.isSubmitted) {
              extraClass += ' disabled';
              if (optIdx === q.correctAnswer) {
                extraClass += ' correct';
              } else if (optIdx === selectedAnswer) {
                extraClass += ' wrong';
              }
            } else if (selectedAnswer === optIdx) {
              extraClass += ' correct'; // Visual selection before submission
            }
            
            return `
              <div class="ca-mcq-option${extraClass}" data-opt-idx="${optIdx}">
                <div class="ca-mcq-option-letter">${String.fromCharCode(65 + optIdx)}</div>
                <div>${option}</div>
              </div>
            `;
          }).join('')}
        </div>

        ${this.isSubmitted ? `
          <div class="ca-mcq-explanation" style="display: block;">
            <div class="ca-mcq-explanation-title">
              <i class="fas fa-info-circle"></i> ${this.getQuizText('explanation', 'Explanation')}
            </div>
            <p>${q.explanation}</p>
          </div>
        ` : ''}
      </div>
    `;
  }

  navigate(direction) {
    const targetIdx = this.currentIdx + direction;
    
    // If clicking "Submit" on last question
    if (this.currentIdx === this.questions.length - 1 && direction === 1 && !this.isSubmitted) {
      this.submitQuiz(false);
      return;
    }

    if (targetIdx >= 0 && targetIdx < this.questions.length) {
      this.renderQuestion(targetIdx);
    }
  }

  startTimer() {
    this.timerInterval = setInterval(() => {
      this.timeRemaining--;
      this.updateTimerDisplay();

      if (this.timeRemaining <= 0) {
        clearInterval(this.timerInterval);
        this.submitQuiz(true); // Auto submit
      }
    }, 1000);
  }

  updateTimerDisplay() {
    const mins = Math.floor(this.timeRemaining / 60);
    const secs = this.timeRemaining % 60;
    const timerDisplay = document.getElementById('quiz-timer-display');
    if (timerDisplay) {
      timerDisplay.innerHTML = `<i class="fas fa-clock"></i> ${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
      if (this.timeRemaining < 30) {
        timerDisplay.style.color = '#e74c3c';
        timerDisplay.style.background = 'rgba(231, 76, 60, 0.2)';
      }
    }
  }

  submitQuiz(isTimeUp = false, isRedisplay = false) {
    if (!isRedisplay) {
      clearInterval(this.timerInterval);
      this.isSubmitted = true;
    }

    // Calculate score
    let score = 0;
    this.questions.forEach((q, idx) => {
      if (this.userAnswers[idx] === q.correctAnswer) {
        score++;
      }
    });

    const percent = Math.round((score / this.questions.length) * 100);
    const isPassed = score >= Math.ceil(this.questions.length * 0.7);

    if (!isRedisplay) {
      // Save local history
      this.saveQuizResult(score, this.questions.length);
    }

    const completedText = this.getQuizText('completed', 'Quiz Completed!');
    const timesUpText = this.getQuizText('times_up', "Time's Up!");
    const youScoredText = document.body.classList.contains('lang-hi') ? `आपने स्कोर किया` : `You scored`;
    const passedBadgeText = this.getQuizText('passed', 'Passed');
    const failBadgeText = this.getQuizText('needs_practice', 'Needs Practice');
    const descText = isPassed 
      ? this.getQuizText('passed_desc', "Excellent! You have a solid grasp of today's news events. Keep maintaining this streak!")
      : this.getQuizText('fail_desc', "Good attempt. Review the detailed explanations of the questions you missed to reinforce your knowledge.");
    const reviewText = this.getQuizText('review_answers', 'Review Answers');
    const retakeText = this.getQuizText('retake', 'Retake');

    // Render results view
    this.container.innerHTML = `
      <div class="ca-results-card">
        <h2 style="font-family: 'Outfit', sans-serif;">${completedText}</h2>
        ${isTimeUp ? `<p style="color: #e74c3c; font-weight: 600;">${timesUpText}</p>` : ''}
        <div class="ca-results-score">${score} / ${this.questions.length}</div>
        <p>${youScoredText} <strong>${percent}%</strong></p>
        
        <div class="ca-results-badge ${isPassed ? '' : 'fail'}">
          ${isPassed ? `<i class="fas fa-award"></i> ${passedBadgeText}` : `<i class="fas fa-times-circle"></i> ${failBadgeText}`}
        </div>

        <p style="color: var(--text-light); max-width: 500px; margin: 0.5rem auto;">
          ${descText}
        </p>

        <div style="display: flex; gap: 1rem; margin-top: 1rem;">
          <button id="view-answers-btn" class="ca-quiz-btn ca-quiz-btn-submit">
            <i class="fas fa-eye"></i> ${reviewText}
          </button>
          <button onclick="location.reload()" class="ca-quiz-btn ca-quiz-btn-prev">
            <i class="fas fa-redo"></i> ${retakeText}
          </button>
        </div>
      </div>
    `;

    document.getElementById('view-answers-btn').addEventListener('click', () => {
      this.renderQuizFrame();
      this.renderQuestion(0);
    });
  }

  saveQuizResult(score, total) {
    try {
      const history = JSON.parse(localStorage.getItem('sjmaths_ca_quiz_history') || '[]');
      history.push({
        date: this.date,
        score,
        total,
        timestamp: new Date().toISOString()
      });
      localStorage.setItem('sjmaths_ca_quiz_history', JSON.stringify(history.slice(-50))); // Keep last 50
    } catch (err) {
      console.error('Error saving quiz result to localStorage:', err);
    }
  }
}

// Auto-initialize if the container is present
document.addEventListener('DOMContentLoaded', () => {
  if (document.getElementById('ca-quiz-root')) {
    const urlParams = new URLSearchParams(window.location.search);
    const dateParam = urlParams.get('date');
    new CurrentAffairsQuiz('ca-quiz-root', { date: dateParam });
  }
});
