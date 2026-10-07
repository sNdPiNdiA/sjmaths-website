/* Shared existing Current Affairs quiz controller. */
document.addEventListener('DOMContentLoaded', () => {
      // Set up sub-tab navigation inside month panels
      const months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul'];
      months.forEach(month => {
        const panel = document.getElementById(month);
        if (!panel) return;
        
        const subNav = panel.querySelector('.month-sub-nav');
        if (!subNav) return;
        
        const subTabButtons = subNav.querySelectorAll('.sub-tab-btn');
        const subTabPanels = panel.querySelectorAll('.sub-tab-panel');
        
        subTabButtons.forEach(button => {
          button.addEventListener('click', () => {
            subTabButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');
            
            const targetId = button.getAttribute('data-subtab');
            subTabPanels.forEach(p => p.classList.remove('active'));
            const targetPanel = panel.querySelector('#' + targetId);
            if (targetPanel) {
              targetPanel.classList.add('active');
              if (targetId.endsWith('-quiz')) {
                initQuiz(month);
              }
            }
          });
        });
      });

      // Quiz controller state
      const quizStates = {};

      function initQuiz(month) {
        if (quizStates[month]) return; // Already initialized
        
        const questions = window.quizData ? window.quizData[month] : [];
        if (!questions || questions.length === 0) return;
        
        quizStates[month] = {
          currentIndex: 0,
          score: 0,
          answers: new Array(questions.length).fill(null),
          questions: questions
        };
        
        renderQuestion(month);
      }

      function renderQuestion(month) {
        const state = quizStates[month];
        const q = state.questions[state.currentIndex];
        const panel = document.getElementById(month);
        const quizPanel = panel.querySelector('#' + month + '-quiz');
        
        // Update header and progress
        quizPanel.querySelector('.quiz-progress').textContent = `Question ${state.currentIndex + 1} of ${state.questions.length}`;
        quizPanel.querySelector('.quiz-score').textContent = `Score: ${state.score}/${state.answers.filter(a => a !== null).length}`;
        quizPanel.querySelector('.quiz-progress-fill').style.width = `${((state.currentIndex + 1) / state.questions.length) * 100}%`;
        
        // Set question text
        quizPanel.querySelector('.quiz-question-text.en-text').innerHTML = q.question_en;
        quizPanel.querySelector('.quiz-question-text.hi-text').innerHTML = q.question_hi;
        
        // Render options list
        const optionsList = quizPanel.querySelector('.quiz-options-list');
        optionsList.innerHTML = '';
        
        const options = q.type === 'tf' 
          ? [{ key: 'A', en: 'True', hi: 'सत्य' }, { key: 'B', en: 'False', hi: 'असत्य' }]
          : q.options;
          
        options.forEach(opt => {
          const btn = document.createElement('button');
          btn.className = 'quiz-option-btn';
          btn.innerHTML = `<span class="option-marker">${opt.key}</span>
            <div>
              <span class="en-text">${opt.en}</span>
              <span class="hi-text">${opt.hi}</span>
            </div>`;
            
          // If already answered this question
          const previousAnswer = state.answers[state.currentIndex];
          if (previousAnswer !== null) {
            btn.disabled = true;
            if (opt.key === q.correct_option) {
              btn.classList.add('correct');
            } else if (opt.key === previousAnswer) {
              btn.classList.add('wrong');
            }
          } else {
            btn.addEventListener('click', () => selectOption(month, opt.key));
          }
          optionsList.appendChild(btn);
        });
        
        // Render explanation box
        const expBox = quizPanel.querySelector('.quiz-explanation-box');
        if (state.answers[state.currentIndex] !== null) {
          expBox.style.display = 'block';
          expBox.querySelector('.explanation-text.en-text').textContent = q.explanation_en;
          expBox.querySelector('.explanation-text.hi-text').textContent = q.explanation_hi;
        } else {
          expBox.style.display = 'none';
        }
        
        // Navigation buttons state
        quizPanel.querySelector('.prev-btn').disabled = state.currentIndex === 0;
        quizPanel.querySelector('.next-btn').disabled = state.currentIndex === state.questions.length - 1;
      }

      function selectOption(month, key) {
        const state = quizStates[month];
        const q = state.questions[state.currentIndex];
        
        state.answers[state.currentIndex] = key;
        const isCorrect = key === q.correct_option;
        if (isCorrect) {
          state.score++;
        }
        
        renderQuestion(month);
      }

      // Handle navigation clicks
      document.addEventListener('click', (e) => {
        const prevBtn = e.target.closest('.prev-btn');
        const nextBtn = e.target.closest('.next-btn');
        
        if (prevBtn) {
          const panel = prevBtn.closest('.tab-panel');
          const month = panel.id;
          const state = quizStates[month];
          if (state && state.currentIndex > 0) {
            state.currentIndex--;
            renderQuestion(month);
          }
        }
        
        if (nextBtn) {
          const panel = nextBtn.closest('.tab-panel');
          const month = panel.id;
          const state = quizStates[month];
          if (state && state.currentIndex < state.questions.length - 1) {
            state.currentIndex++;
            renderQuestion(month);
          }
        }
      });
    });
