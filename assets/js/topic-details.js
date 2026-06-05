document.addEventListener('DOMContentLoaded', () => {
// Scroll active nav item into view
            setTimeout(() => {
                const activeItem = document.querySelector('.sub-nav-item.active');
                const navContainer = document.querySelector('.subject-nav');
                if (activeItem && navContainer) {
                    const containerWidth = navContainer.offsetWidth;
                    const itemOffset = activeItem.offsetLeft;
                    const itemWidth = activeItem.offsetWidth;
                    navContainer.scrollLeft = itemOffset - (containerWidth / 2) + (itemWidth / 2);
                }
            }, 100);

            function scrollActiveTabIntoView() {
                const activeTab = document.querySelector('.tab-btn.active');
                const tabsContainer = document.querySelector('.tabs-container');
                if (activeTab && tabsContainer) {
                    const containerWidth = tabsContainer.offsetWidth;
                    const itemOffset = activeTab.offsetLeft;
                    const itemWidth = activeTab.offsetWidth;
                    tabsContainer.scrollTo({
                        left: itemOffset - (containerWidth / 2) + (itemWidth / 2),
                        behavior: 'smooth'
                    });
                }
            }

            // Initial call for active tab
            setTimeout(scrollActiveTabIntoView, 150);

            // Handle checklist local storage
            const checkboxes = document.querySelectorAll('.checklist-checkbox');
            const storageKey = 'ssc-cgl-prep-checklist';
            const progress = JSON.parse(localStorage.getItem(storageKey)) || {};

            checkboxes.forEach(chk => {
                if (progress[chk.id]) {
                    chk.checked = true;
                }
                chk.addEventListener('change', () => {
                    progress[chk.id] = chk.checked;
                    localStorage.setItem(storageKey, JSON.stringify(progress));
                });
                
                // Allow clicking parent checklist-item to toggle checkbox
                const parent = chk.closest('.checklist-item');
                if (parent) {
                    parent.addEventListener('click', (e) => {
                        if (e.target !== chk) {
                            chk.checked = !chk.checked;
                            chk.dispatchEvent(new Event('change'));
                        }
                    });
                }
            });

            // Language Toggle logic
            const langToggleBtn = document.getElementById('langToggleBtn');
            const langText = langToggleBtn.querySelector('span');
            let currentLang = localStorage.getItem('ssc-cgl-lang') || 'en';
            
            if (currentLang === 'hi') {
                document.body.classList.add('lang-mode-hi');
                langText.textContent = 'English';
            } else {
                langText.textContent = 'Hindi / हिंदी';
            }
            
            langToggleBtn.addEventListener('click', () => {
                if (document.body.classList.contains('lang-mode-hi')) {
                    document.body.classList.remove('lang-mode-hi');
                    langText.textContent = 'Hindi / हिंदी';
                    localStorage.setItem('ssc-cgl-lang', 'en');
                } else {
                    document.body.classList.add('lang-mode-hi');
                    langText.textContent = 'English';
                    localStorage.setItem('ssc-cgl-lang', 'hi');
                }
                // Trigger MathJax typeset to render newly visible formulas
                if (window.MathJax) {
                    MathJax.typesetPromise();
                }
            });
        
            // Horizontal Tabs Switcher Event Listener
            const tabButtons = document.querySelectorAll('.tab-btn');
            const tabPanels = document.querySelectorAll('.tab-panel');

            tabButtons.forEach(btn => {
                btn.addEventListener('click', () => {
                    const targetTab = btn.getAttribute('data-tab');
                    
                    tabButtons.forEach(b => {
                        b.classList.remove('active');
                        b.setAttribute('aria-selected', 'false');
                    });
                    btn.classList.add('active');
                    btn.setAttribute('aria-selected', 'true');
                    
                    tabPanels.forEach(p => {
                        p.classList.remove('active');
                    });
                    
                    const activePanel = document.getElementById(`panel-${targetTab}`);
                    if (activePanel) {
                        activePanel.classList.add('active');
                    }
                    
                    scrollActiveTabIntoView();
                    
                    if (window.MathJax) {
                        MathJax.typesetPromise();
                    }
                });
            });

            // Scroll to end auto-jump to next tab
            let lastScrollTime = 0;
            window.addEventListener('scroll', () => {
                const scrollPosition = window.innerHeight + window.scrollY;
                const scrollHeight = document.documentElement.scrollHeight;
                
                if (scrollPosition >= scrollHeight - 5) {
                    const now = Date.now();
                    if (now - lastScrollTime > 1500) {
                        const activeBtn = document.querySelector('.tab-btn.active');
                        if (activeBtn) {
                            const nextBtn = activeBtn.nextElementSibling;
                            if (nextBtn && nextBtn.classList.contains('tab-btn')) {
                                lastScrollTime = now;
                                nextBtn.click();
                                const tabContainer = document.querySelector('.tabs-container');
                                if (tabContainer) {
                                    tabContainer.scrollIntoView({ behavior: 'smooth', block: 'start' });
                                }
                            }
                        }
                    }
                }
            });

            // Dynamic Content Loader Logic
            // 1. Load Practice Questions
            fetch('data/practice-questions.json')
                .then(res => res.json())
                .then(data => {
                    const container = document.getElementById('practice-questions-container');
                    if (!container) return;
                    let html = '';
                    data.forEach((q, idx) => {
                        html += `
                        <div class="question-box">
                            <div class="question-text">
                                <span class="lang-en">Q${idx + 1}. ${q.question.en}</span>
                                <span class="lang-hi">Q${idx + 1}. ${q.question.hi}</span>
                            </div>
                            <div style="font-size: 0.95rem; color: var(--text-light); margin-bottom: 0.5rem;">
                                <span class="lang-en">Difficulty: ${q.difficulty.en}</span>
                                <span class="lang-hi">कठिनाई: ${q.difficulty.hi}</span>
                            </div>
                            ${q.options ? `<div style="font-size: 0.95rem; color: var(--text-light); margin-bottom: 0.5rem;">${q.options}</div>` : ''}
                            <details class="solution-details">
                                <summary>
                                    <span class="lang-en">View Solution & Explanation</span>
                                    <span class="lang-hi">हल और स्पष्टीकरण देखें</span>
                                </summary>
                                <div class="solution-content">
                                    <div class="lang-en">${q.solution.en}</div>
                                    <div class="lang-hi">${q.solution.hi}</div>
                                </div>
                            </details>
                        </div>`;
                    });
                    container.innerHTML = html;
                    if (window.MathJax) MathJax.typesetPromise([container]);
                });

            // 2. Load PYQs
            fetch('data/pyqs.json')
                .then(res => res.json())
                .then(data => {
                    const container = document.getElementById('pyqs-container');
                    if (!container) return;
                    let html = '';
                    data.forEach((q, idx) => {
                        html += `
                        <div class="question-box" style="border-left-color: #e74c3c;">
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem; flex-wrap: wrap; gap: 0.5rem;">
                                <span style="background: rgba(231,76,60,0.1); color: #e74c3c; font-size: 0.75rem; font-weight: 700; padding: 3px 10px; border-radius: 20px;">${q.badge}</span>
                            </div>
                            <div class="question-text">
                                <span class="lang-en">Q${idx + 1}. ${q.question.en}</span>
                                <span class="lang-hi">Q${idx + 1}. ${q.question.hi}</span>
                            </div>
                            <div style="font-size: 0.95rem; color: var(--text-light); margin-bottom: 0.5rem;">
                                ${q.options}
                            </div>
                            <details class="solution-details">
                                <summary>
                                    <span class="lang-en">View Solution & Explanation</span>
                                    <span class="lang-hi">हल और स्पष्टीकरण देखें</span>
                                </summary>
                                <div class="solution-content">
                                    <div class="lang-en">${q.solution.en}</div>
                                    <div class="lang-hi">${q.solution.hi}</div>
                                </div>
                            </details>
                        </div>`;
                    });
                    container.innerHTML = html;
                    if (window.MathJax) MathJax.typesetPromise([container]);
                });

            // 3. Load Mini Test Questions
            let quizTimerInterval = null;
            let quizTimeLeft = 240; // 4 minutes in seconds
            let quizStarted = false;

            fetch('data/mini-test.json')
                .then(res => res.json())
                .then(data => {
                    const container = document.getElementById('mini-test-questions');
                    if (!container) return;
                    
                    let html = '';
                    data.forEach(q => {
                        let optsHtml = '';
                        q.options.forEach(opt => {
                            optsHtml += `
                            <label class="quiz-option">
                                <input type="radio" name="${q.id}" value="${opt.value}" class="quiz-radio">
                                <span>${opt.text}</span>
                            </label>`;
                        });
                        html += `
                        <div class="question-box" style="margin-bottom: 2rem;">
                            <div class="question-text">
                                <span class="lang-en">${q.question.en}</span>
                                <span class="lang-hi">${q.question.hi}</span>
                            </div>
                            <div style="display: flex; flex-direction: column; gap: 0.5rem; margin-top: 1rem;">
                                ${optsHtml}
                            </div>
                        </div>`;
                    });
                    container.innerHTML = html;
                    if (window.MathJax) MathJax.typesetPromise([container]);

                    // Hide questions and submit button initially
                    container.style.display = 'none';
                    const submitBtn = document.getElementById('quizSubmitBtn');
                    if (submitBtn) submitBtn.style.display = 'none';

                    // Inject Timer UI
                    let timerBar = document.getElementById('quiz-timer-bar');
                    if (!timerBar) {
                        timerBar = document.createElement('div');
                        timerBar.id = 'quiz-timer-bar';
                        timerBar.style.cssText = 'background: rgba(142, 68, 173, 0.08); border: 1px solid rgba(142, 68, 173, 0.2); border-radius: 12px; padding: 1.25rem; margin-bottom: 1.5rem; display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 1rem; font-family: "Outfit", sans-serif; transition: all 0.3s ease;';
                        timerBar.innerHTML = `
                            <div style="display: flex; align-items: center; gap: 0.75rem;">
                                <div style="background: var(--primary); color: white; width: 42px; height: 42px; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 10px rgba(142,68,173,0.3);">
                                    <i class="fas fa-hourglass-half" id="timer-icon" style="font-size: 1.15rem;"></i>
                                </div>
                                <div>
                                    <div style="font-size: 0.75rem; text-transform: uppercase; letter-spacing: 1px; color: var(--text-light); font-weight: 700;">
                                        <span class="lang-en">Time Remaining</span><span class="lang-hi">शेष समय</span>
                                    </div>
                                    <div id="timer-countdown" style="font-size: 1.5rem; font-weight: 800; color: var(--text-dark);">04:00</div>
                                </div>
                            </div>
                            <div style="display: flex; align-items: center; gap: 1rem;">
                                <div id="quiz-status-text" style="font-size: 0.9rem; color: var(--text-light); font-weight: 500;">
                                    <span class="lang-en">${data.length} Questions • 4 Mins</span><span class="lang-hi">${data.length} प्रश्न • 4 मिनट</span>
                                </div>
                                <button type="button" id="startQuizBtn" class="quiz-submit-btn" style="margin: 0; padding: 0.6rem 1.5rem; font-size: 0.9rem; background: var(--primary); border-radius: 30px; border: none; cursor: pointer; color: white;">
                                    <span class="lang-en">Start Test</span><span class="lang-hi">टेस्ट शुरू करें</span>
                                </button>
                            </div>
                        `;
                        container.parentNode.insertBefore(timerBar, container);

                        const startBtn = document.getElementById('startQuizBtn');
                        const countdownEl = document.getElementById('timer-countdown');
                        const statusEl = document.getElementById('quiz-status-text');

                        startBtn.addEventListener('click', () => {
                            if (quizStarted) return;
                            quizStarted = true;
                            
                            // Show questions and submit button
                            container.style.display = 'block';
                            if (submitBtn) submitBtn.style.display = 'block';
                            
                            // Disable start button
                            startBtn.style.background = '#bdc3c7';
                            startBtn.style.cursor = 'not-allowed';
                            startBtn.innerHTML = '<span class="lang-en">In Progress</span><span class="lang-hi">प्रगति पर है</span>';
                            
                            // Start Countdown
                            quizTimerInterval = setInterval(() => {
                                quizTimeLeft--;
                                let minutes = Math.floor(quizTimeLeft / 60);
                                let seconds = quizTimeLeft % 60;
                                countdownEl.textContent = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;

                                if (quizTimeLeft <= 30) {
                                    countdownEl.style.color = '#e74c3c';
                                    countdownEl.style.animation = 'pulse 1s infinite';
                                }

                                if (quizTimeLeft <= 0) {
                                    clearInterval(quizTimerInterval);
                                    alert("Time's up! Your quiz will be submitted automatically.");
                                    if (submitBtn) submitBtn.click();
                                }
                            }, 1000);
                        });
                    }
                });

            // Mini Quiz Evaluator Logic
            const quizSubmitBtn = document.getElementById('quizSubmitBtn');
            const quizScoreCard = document.getElementById('quizScoreCard');
            const scoreText = document.getElementById('scoreText');
            const explContainer = document.getElementById('quiz-explanations-container');
            
            if (quizSubmitBtn) {
                quizSubmitBtn.addEventListener('click', (e) => {
                    e.preventDefault();
                    
                    // Stop timer
                    if (quizTimerInterval) {
                        clearInterval(quizTimerInterval);
                    }
                    
                    const countdownEl = document.getElementById('timer-countdown');
                    if (countdownEl) {
                        countdownEl.style.color = '#2ecc71';
                        countdownEl.style.animation = 'none';
                    }

                    const startBtn = document.getElementById('startQuizBtn');
                    if (startBtn) {
                        startBtn.innerHTML = '<span class="lang-en">Completed</span><span class="lang-hi">पूरा हुआ</span>';
                        startBtn.style.background = '#2ecc71';
                    }

                    fetch('data/mini-test.json')
                        .then(res => res.json())
                        .then(data => {
                            let score = 0;
                            let total = data.length;
                            let explsHtml = '';
                            
                            data.forEach((q, idx) => {
                                const selected = document.querySelector(`input[name="${q.id}"]:checked`);
                                const isCorrect = selected && selected.value === q.answer;
                                if (isCorrect) score++;
                                
                                // Highlight Options
                                const options = document.querySelectorAll(`input[name="${q.id}"]`);
                                options.forEach(opt => {
                                    const parentLabel = opt.closest('.quiz-option');
                                    if (parentLabel) {
                                        parentLabel.style.borderColor = '';
                                        parentLabel.style.background = '';
                                        if (opt.value === q.answer) {
                                            parentLabel.style.borderColor = '#2ecc71';
                                            parentLabel.style.background = 'rgba(46,204,113,0.05)';
                                        } else if (opt.checked) {
                                            parentLabel.style.borderColor = '#e74c3c';
                                            parentLabel.style.background = 'rgba(231,76,60,0.05)';
                                        }
                                    }
                                });
                                
                                // Solution markup
                                explsHtml += `
                                <div style="padding: 0.75rem; background: rgba(0,0,0,0.01); border-radius: 6px; border-left: 3px solid ${isCorrect ? '#2ecc71' : '#e74c3c'};">
                                    <strong>Q${idx+1} Solution:</strong><br>
                                    <div class="lang-en">${q.solution.en}</div>
                                    <div class="lang-hi">${q.solution.hi}</div>
                                </div>`;
                            });
                            
                            scoreText.textContent = `${score} / ${total}`;
                            quizScoreCard.style.display = 'block';
                            if (explContainer) {
                                explContainer.innerHTML = explsHtml;
                            }
                            
                            if (window.MathJax) {
                                MathJax.typesetPromise([quizScoreCard]);
                            }

                            // Smooth scroll to results
                            quizScoreCard.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
                        });
                });
            }
});