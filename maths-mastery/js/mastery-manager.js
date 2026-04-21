/**
 * MasteryManager handles the learning loop: Explanation -> Practice -> Test -> Remediate/Advance
 * It manages state, progress persistence, and locking logic.
 */
class MasteryManager {
    constructor(subject, topics) {
        this.subject = subject;
        this.topics = topics; // Array of topic IDs in order
        this.currentTopicIndex = 0;
        this.state = 'explanation'; // explanation, practice, test, remediation_explanation, remediation_practice, remediation_test
        this.score = 0;
        this.mistakes = [];
        this.currentQuestionIndex = 0;
        this.practiceQuestions = [];
        this.testQuestions = [];

        this.init();
    }

    init() {
        this.loadProgress();
        this.renderTopicList();

        // Check for saved state or URL parameters for redirection
        const urlParams = new URLSearchParams(window.location.search);
        const redirectTopic = urlParams.get('topic');

        if (redirectTopic) {
            // Priority 1: URL Redirect (from Gateway Failure)
            const topicIndex = this.topics.findIndex(t => t.id === redirectTopic);
            if (topicIndex !== -1) {
                this.currentTopicIndex = topicIndex;
                this.loadTopic(redirectTopic);
            } else {
                this.loadTopic(this.topics[0].id); // Fallback
            }
        } else {
            // Priority 2: Saved State
            const savedState = localStorage.getItem(`sjmaths_${this.subject}_state`);
            if (savedState) {
                const parsed = JSON.parse(savedState);
                this.currentTopicIndex = parsed.topicIndex;
                this.loadTopic(this.topics[this.currentTopicIndex].id);
            } else {
                // Priority 3: Default Start
                this.loadTopic(this.topics[0].id);
            }
        }

        // Window resize listener
        let lastWidth = window.innerWidth;
        window.addEventListener('resize', () => {
            if (Math.abs(window.innerWidth - lastWidth) > 50) {
                lastWidth = window.innerWidth;
                this.renderTopicList();
                if (this.currentTopicContent) {
                    this.renderExplanation();
                }
            }
        });

        // Initial Mobile View
        if (window.innerWidth <= 768) {
            this.toggleView('path');
        }
    }

    loadProgress() {
        this.progress = JSON.parse(localStorage.getItem(`sjmaths_${this.subject}_progress`)) || {};
        // Ensure all topics have an entry
        this.topics.forEach(topic => {
            if (!this.progress[topic.id]) {
                this.progress[topic.id] = {
                    status: 'locked',
                    practiceLevel: 1,
                    testLevel: 1
                };
            } else {
                // Backfill for existing users
                if (!this.progress[topic.id].practiceLevel) this.progress[topic.id].practiceLevel = 1;
                if (!this.progress[topic.id].testLevel) this.progress[topic.id].testLevel = 1;
            }
        });

        // Unlock first topic if everything is locked
        if (this.progress[this.topics[0].id].status === 'locked') {
            this.progress[this.topics[0].id].status = 'unlocked';
        }
    }

    saveProgress() {
        localStorage.setItem(`sjmaths_${this.subject}_progress`, JSON.stringify(this.progress));
        localStorage.setItem(`sjmaths_${this.subject}_state`, JSON.stringify({
            topicIndex: this.currentTopicIndex
        }));
    }

    async loadTopic(topicId) {
        if (this.isLocked(topicId)) {
            alert("This topic is locked. Please complete the previous topics first.");
            return;
        }

        // Show loading
        document.getElementById('mastery-content').innerHTML = '<div class="spinner">Loading...</div>';

        // Fetch content
        try {
            const response = await fetch(`../microtopics/${topicId}.json`);
            if (!response.ok) throw new Error("Failed to load topic");
            this.currentTopicContent = await response.json();

            // Default activeContent to the whole file (legacy support)
            this.activeContent = this.currentTopicContent;

            // Check if this is a Module (Microtopics) or Single Topic
            if (this.currentTopicContent.microtopics) {
                this.renderModuleDashboard();
            } else {
                // Set initial state for legacy single-file topics
                this.startExplanation();
            }
        } catch (e) {
            console.error(e);
            document.getElementById('mastery-content').innerHTML = '<div class="error">Failed to load content.</div>';
        }

        this.updateActiveTopicUI(topicId);
    }

    renderModuleDashboard() {
        this.state = 'dashboard';
        const container = document.getElementById('mastery-content');
        const topic = this.currentTopicContent;

        // Calculate progress for the module
        // const progress = this.progress[topic.id] || {}; 

        container.innerHTML = `
            <div class="module-dashboard fade-in">
                ${this.renderBackButton()}
                <h2>${topic.title}</h2>
                <p class="module-intro">Master these skills to complete the level.</p>
                
                <div class="microtopic-list">
                    ${topic.microtopics.map((mt, index) => `
                        <div class="microtopic-card" onclick="manager.loadMicrotopic(${index})">
                            <span class="mt-number">${index + 1}</span>
                            <div class="mt-info">
                                <h3>${mt.title}</h3>
                                <p>${mt.standard.explanation.substring(0, 50).replace(/<[^>]*>?/gm, '')}...</p>
                            </div>
                            <div class="mt-status">
                                <i class="fas fa-play-circle"></i>
                            </div>
                        </div>
                    `).join('')}
                </div>

                <div class="final-test-section disabled">
                    <button class="btn btn-block btn-secondary">
                        <i class="fas fa-lock"></i> Final Level Test
                    </button>
                    <small>Complete all topics to unlock.</small>
                </div>
            </div>
        `;
    }

    loadMicrotopic(index) {
        this.currentMicrotopicIndex = index;
        this.activeContent = this.currentTopicContent.microtopics[index];
        // Default to Study tab
        this.switchTab('study');
    }

    switchTab(tab, isRemedial = false) {
        this.state = tab; // 'study', 'practice', 'test'
        const container = this.getContentContainer();

        // Render common layout structure
        container.innerHTML = `
            <div class="microtopic-container fade-in">
                ${this.renderHeader()}
                ${this.renderTabs(tab)}
                <div id="tab-content" class="tab-content"></div>
            </div>
        `;

        if (window.renderMathInElement) renderMathInElement(container);

        // Render specific tab content
        const contentArea = document.getElementById('tab-content');
        if (tab === 'study') this.renderStudyContent(contentArea, isRemedial);
        else if (tab === 'practice') this.renderPracticeStartingPoint(contentArea);
        else if (tab === 'test') this.renderTestStartingPoint(contentArea);
    }

    renderHeader() {
        return `
            <div class="topic-header">
                <button class="btn-icon-back" onclick="manager.renderModuleDashboard()">
                    <i class="fas fa-arrow-left"></i>
                </button>
                <h2>${this.activeContent.title}</h2>
            </div>
        `;
    }

    renderTabs(activeTab) {
        return `
            <div class="mastery-tabs">
                <button class="tab-btn ${activeTab === 'study' ? 'active' : ''}" onclick="manager.switchTab('study')">
                    <i class="fas fa-book-open"></i> Study
                </button>
                <button class="tab-btn ${activeTab === 'practice' ? 'active' : ''}" onclick="manager.switchTab('practice')">
                    <i class="fas fa-dumbbell"></i> Practice
                </button>
                <button class="tab-btn ${activeTab === 'test' ? 'active' : ''}" onclick="manager.switchTab('test')">
                    <i class="fas fa-trophy"></i> Quiz
                </button>
            </div>
        `;
    }

    renderStudyContent(container, isRemedial = false) {
        const content = isRemedial ? this.activeContent.remedial.explanation : this.activeContent.standard.explanation;
        container.innerHTML = `
            <div class="study-content fade-in">
                ${isRemedial ? '<h3>Let\'s try a different approach</h3>' : ''}
                ${content}
                <div class="action-footer">
                    <button class="btn btn-primary" onclick="manager.switchTab('practice')">
                        Start Practice <i class="fas fa-arrow-right"></i>
                    </button>
                </div>
            </div>
        `;
        if (window.renderMathInElement) renderMathInElement(container);
        // Initialize any interactive "Try It" buttons
        container.querySelectorAll('.try-it-btn').forEach(btn => {
            btn.onclick = () => {
                const answer = btn.getAttribute('data-answer');
                const input = btn.previousElementSibling;
                const feedback = btn.nextElementSibling;

                if (input.value.trim().toLowerCase() === answer.toLowerCase()) {
                    feedback.innerHTML = '<span style="color: green"><i class="fas fa-check"></i> Correct!</span>';
                } else {
                    feedback.innerHTML = '<span style="color: red"><i class="fas fa-times"></i> Try again</span>';
                }
            };
        });
    }

    renderPracticeStartingPoint(container) {
        // Simple start screen for practice
        container.innerHTML = `
            <div class="start-screen fade-in">
                <div class="icon-circle"><i class="fas fa-dumbbell"></i></div>
                <h3>Ready to Practice?</h3>
                <p>Questions will get harder as you go.</p>
                <button class="btn btn-primary btn-lg" onclick="manager.startAdaptivePractice()">
                    Start Session
                </button>
            </div>
        `;
    }

    renderTestStartingPoint(container) {
        container.innerHTML = `
            <div class="start-screen fade-in">
                <div class="icon-circle"><i class="fas fa-trophy"></i></div>
                <h3>Level Assessment</h3>
                <p>Prove your mastery to earn this badge.</p>
                <button class="btn btn-primary btn-lg" onclick="manager.startTest()">
                    Start Quiz
                </button>
            </div>
        `;
    }

    startAdaptivePractice() {
        // Load questions from all levels for a comprehensive session
        // For now, simpler logic: Level 1 -> Level 2 -> Level 3 concatenated
        const p = this.activeContent.standard.practice;
        const allQuestions = [
            ...(p.level1 || []),
            ...(p.level2 || []),
            ...(p.level3 || [])
        ];

        // Pick 10 random
        this.practiceQuestions = this.getRandomQuestions(allQuestions, 10);
        this.currentQuestionIndex = 0;
        this.currentLevel = 'Adaptive'; // Display purpose
        this.renderPracticeSession();
    }

    renderPracticeSession() {
        const question = this.practiceQuestions[this.currentQuestionIndex];
        const container = document.getElementById('tab-content');
        if (!container) return; // Safety

        const isLast = this.currentQuestionIndex === this.practiceQuestions.length - 1;
        const progress = ((this.currentQuestionIndex + 1) / this.practiceQuestions.length) * 100;

        let optionsHtml = '';
        if (question.type === 'input') {
            optionsHtml = `
            <div class="input-question">
                 <input type="text" id="practice-input" placeholder="Enter answer" class="form-control" autocomplete="off">
                 <button class="btn btn-secondary" onclick="manager.checkPracticeInput('${question.answer}', this)">Submit</button>
            </div>`;
        } else {
            optionsHtml = `
            <div class="options-grid">
                ${question.options.map((opt, i) => `
                    <button class="option-btn" onclick="manager.checkPracticeAnswer(${i}, ${question.correct}, this)">${opt}</button>
                `).join('')}
            </div>`;
        }

        container.innerHTML = `
            <div class="practice-session fade-in">
                <div class="session-progress">
                    <div class="progress-bar-fill" style="width: ${progress}%"></div>
                </div>
                <div class="question-card">
                    <p class="question-text">${question.q}</p>
                    ${optionsHtml}
                    <div id="feedback" class="feedback-area"></div>
                </div>
                <div class="actions" style="display:none" id="next-btn-container">
                    <button class="btn btn-primary" onclick="manager.nextPractice()">
                        ${isLast ? 'Finish' : 'Next'} <i class="fas fa-arrow-right"></i>
                    </button>
                </div>
            </div>
        `;
        if (window.renderMathInElement) renderMathInElement(container);
    }

    startExplanation() {
        this.state = 'explanation';
        // This method is for legacy single-file topics.
        // For microtopics, `switchTab('study')` is used.
        this.renderLegacyExplanation();
    }

    renderLegacyExplanation(isRemedial = false) {
        const container = this.getContentContainer();
        const content = isRemedial ? this.activeContent.remedial.explanation : this.activeContent.standard.explanation;

        let backButton = this.renderBackButton();
        // This condition is for when a single-file topic is loaded, not a microtopic within a module
        if (this.currentTopicContent.microtopics && this.state !== 'dashboard') {
            // This case should ideally not be hit if `startExplanation` is only for legacy topics
            // and `loadMicrotopic` uses `switchTab`. Keeping for robustness.
            backButton = `<button class="btn-back-path" onclick="manager.renderModuleDashboard()"><i class="fas fa-arrow-left"></i> Back to Level</button>`;
        }

        const currentProgress = this.progress[this.topics[this.currentTopicIndex].id];

        // Level Selection UI
        let levelsHtml = '';
        if (!isRemedial) {
            levelsHtml = `
                <div class="level-selector">
                    <h3>Select Level</h3>
                    <div class="levels-grid">
                        ${[1, 2, 3].map(lvl => {
                const isLocked = lvl > currentProgress.practiceLevel;
                const isCompleted = lvl < currentProgress.practiceLevel;
                const statusClass = isLocked ? 'locked' : (isCompleted ? 'completed' : 'current');
                const icon = isLocked ? 'lock' : (isCompleted ? 'check' : 'play');

                return `
                                <div class="level-card ${statusClass}" ${!isLocked ? `onclick="manager.startPractice(${lvl})"` : ''}>
                                    <div class="level-icon"><i class="fas fa-${icon}"></i></div>
                                    <div class="level-info">
                                        <h4>Level ${lvl}</h4>
                                        <p>${isLocked ? 'Locked' : (isCompleted ? 'Completed' : 'Start Practice')}</p>
                                    </div>
                                </div>
                            `;
            }).join('')}
                    </div>
                </div>
            `;
        }

        container.innerHTML = `
            <div class="explanation-container fade-in">
                ${backButton}
                <h2>${isRemedial ? 'Let\'s try a different approach' : this.activeContent.title}</h2>
                <div class="content opacity-0" style="animation: fadeIn 0.5s forwards;">
                    ${content}
                </div>
                ${!isRemedial ? levelsHtml : `
                    <div class="actions">
                        <button class="btn btn-primary" onclick="manager.startPractice(1)">
                            Start Practice <i class="fas fa-arrow-right"></i>
                        </button>
                    </div>
                `}
            </div >
            `;

        // Render math if needed
        if (window.renderMathInElement) {
            renderMathInElement(container);
        }

        // Initialize any interactive "Try It" buttons
        container.querySelectorAll('.try-it-btn').forEach(btn => {
            btn.onclick = () => {
                const answer = btn.getAttribute('data-answer');
                const input = btn.previousElementSibling;
                const feedback = btn.nextElementSibling;

                if (input.value.trim().toLowerCase() === answer.toLowerCase()) {
                    feedback.innerHTML = '<span style="color: green"><i class="fas fa-check"></i> Correct!</span>';
                } else {
                    feedback.innerHTML = '<span style="color: red"><i class="fas fa-times"></i> Try again</span>';
                }
            };
        });
    }

    startRemediation() {
        this.state = 'remediation_explanation';
        if (this.currentTopicContent.microtopics) {
            this.switchTab('study', true);
        } else {
            this.renderLegacyExplanation(true); // Use legacy explanation for remediation for now
        }
    }

    startPractice(level = 1) {
        // This method is now primarily for legacy topics or specific level practice.
        // For microtopics, `startAdaptivePractice` is the main entry.
        this.currentLevel = level;
        this.state = this.state === 'remediation_explanation' ? 'remediation_practice' : 'practice';
        this.currentQuestionIndex = 0;

        let pool;
        if (this.state === 'remediation_practice') {
            pool = this.activeContent.remedial.practice; // Remedial uses simple array
        } else {
            // Standard uses levels object
            pool = this.activeContent.standard.practice[`level${level}`] || this.activeContent.standard.practice;
        }

        // Just take distinct questions, simple shuffle
        this.practiceQuestions = this.getRandomQuestions(pool, 5);
        this.renderPractice(); // This will render into the main content area, not a tab
    }

    renderPractice() {
        // This method is for legacy topics, rendering directly into mastery-content
        const question = this.practiceQuestions[this.currentQuestionIndex];
        const container = this.getContentContainer();
        const isLast = this.currentQuestionIndex === this.practiceQuestions.length - 1;
        const progress = (this.currentQuestionIndex / this.practiceQuestions.length) * 100;

        let optionsHtml = '';
        if (question.type === 'input') {
            optionsHtml = `
            <div class="input-question" >
                <input type="text" id="practice-input" placeholder="Enter your answer" class="form-control" autocomplete="off">
                    <button class="btn btn-secondary" onclick="manager.checkPracticeInput('${question.answer}', this)">Submit</button>
                </div>
        `;
        } else {
            optionsHtml = `
            <div class="options-grid" >
                ${question.options.map((opt, i) => `
                        <button class="option-btn" onclick="manager.checkPracticeAnswer(${i}, ${question.correct}, this)">
                            ${opt}
                        </button>
                    `).join('')
                }
                </div >
            `;
        }

        container.innerHTML = `
            <div class="practice-container fade-in" >
                <div class="progress-header">
                    <span>Level ${this.currentLevel} Practice</span>
                    <div class="progress-bar"><div style="width: ${progress}%"></div></div>
                </div>
                <div class="question-card">
                    <p class="question-text">${question.q}</p>
                    ${optionsHtml}
                    <div id="feedback" class="feedback-area"></div>
                </div>
                <div class="actions" style="display:none" id="next-btn-container">
                    <button class="btn btn-primary" onclick="manager.nextPractice()">
                        ${isLast ? 'Take Test' : 'Next Question'} <i class="fas fa-arrow-right"></i>
                    </button>
                </div>
            </div >
            `;

        if (window.renderMathInElement) renderMathInElement(container);
    }

    startTest(level = 1) {
        this.currentLevel = level || 1;
        this.state = this.state.includes('remediation') ? 'remediation_test' : 'test';
        this.currentQuestionIndex = 0;
        this.score = 0;

        let pool;
        if (this.state === 'remediation_test') {
            pool = this.activeContent.remedial.test;
        } else {
            pool = this.activeContent.standard.test[`level${this.currentLevel}`] || this.activeContent.standard.test;
        }

        this.testQuestions = this.getRandomQuestions(pool, 5);
        this.renderTest();
    }

    getRandomQuestions(pool, count) {
        // Fisher-Yates shuffle
        const shuffled = [...pool];
        for (let i = shuffled.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
        }
        return shuffled.slice(0, count);
    }

    isLocked(topicId) {
        return this.progress[topicId]?.status === 'locked';
    }

    getContentContainer() {
        return document.getElementById('mastery-content');
    }

    renderTopicList() {
        const listContainer = document.getElementById('topic-list');
        const isMobile = window.innerWidth <= 768;

        listContainer.innerHTML = this.topics.map((topic, index) => {
            const status = this.progress[topic.id].status;
            let statusIcon = '<i class="fas fa-lock"></i>';
            let statusClass = 'locked';

            if (status === 'unlocked') {
                statusIcon = '<i class="fas fa-play-circle"></i>';
                statusClass = 'unlocked';
            } else if (status === 'mastered') {
                statusIcon = '<i class="fas fa-check-circle"></i>';
                statusClass = 'mastered';
            }

            if (index === this.currentTopicIndex) {
                statusClass += ' active';
            }

            return `
                <div class="topic-item-wrapper">
                    <div class="topic-item ${statusClass}" onclick="manager.selectTopic(${index})">
                        <div class="topic-info">
                            <div class="topic-number">${index + 1}</div>
                            <div class="topic-name">${topic.title}</div>
                        </div>
                        <div class="topic-status">
                            ${statusIcon}
                        </div>
                    </div>
                </div>
            `;
        }).join('');
    }

    selectTopic(index) {
        if (this.currentTopicIndex !== index) {
            this.currentTopicIndex = index;
            this.loadTopic(this.topics[index].id);
        } else {
            // Reload even if active to ensure content shows up
            this.loadTopic(this.topics[index].id);
        }
        this.toggleView('topic');
    }




    renderPracticeSession() {
        const question = this.practiceQuestions[this.currentQuestionIndex];
        let container = document.getElementById('tab-content');
        if (!container) container = this.getContentContainer();

        const isLast = this.currentQuestionIndex === this.practiceQuestions.length - 1;
        const progress = (this.currentQuestionIndex / this.practiceQuestions.length) * 100;

        let optionsHtml = '';
        if (question.type === 'input') {
            optionsHtml = `
            <div class="input-question">
                <input type="text" id="practice-input" placeholder="Enter your answer" class="form-control" autocomplete="off">
                    <button class="btn btn-secondary" onclick="manager.checkPracticeInput('${question.answer}', this)">Submit</button>
                </div>
        `;
        } else {
            optionsHtml = `
            <div class="options-grid">
                ${question.options.map((opt, i) => `
                        <button class="option-btn" onclick="manager.checkPracticeAnswer(${i}, ${question.correct}, this)">
                            ${opt}
                        </button>
                    `).join('')
                }
                </div>
            `;
        }

        container.innerHTML = `
            <div class="practice-container fade-in">
                <div class="progress-header">
                    <span>Level ${this.currentLevel} Practice</span>
                    <div class="progress-bar"><div style="width: ${progress}%"></div></div>
                </div>
                <div class="question-card">
                    <p class="question-text">${question.q}</p>
                    ${optionsHtml}
                    <div id="feedback" class="feedback-area"></div>
                </div>
                <div class="actions" style="display:none" id="next-btn-container">
                    <button class="btn btn-primary" onclick="manager.nextPractice()">
                        ${isLast ? 'Take Test' : 'Next Question'} <i class="fas fa-arrow-right"></i>
                    </button>
                </div>
            </div>
            `;

        if (window.renderMathInElement) renderMathInElement(container);
    }

    checkPracticeInput(correctAnswer, btn) {
        const input = document.getElementById('practice-input');
        const feedback = document.getElementById('feedback');
        const userVal = input.value.trim();

        btn.disabled = true;
        input.disabled = true;

        if (userVal === correctAnswer || parseFloat(userVal) === parseFloat(correctAnswer)) {
            feedback.innerHTML = `<div class="alert success"><i class="fas fa-check"></i> Correct!</div>`;
        } else {
            feedback.innerHTML = `<div class="alert error"><i class="fas fa-times"></i> Incorrect. The answer is ${correctAnswer}</div>`;
        }
        document.getElementById('next-btn-container').style.display = 'block';
    }

    checkPracticeAnswer(selected, correct, btn) {
        const feedback = document.getElementById('feedback');
        const btns = document.querySelectorAll('.option-btn');

        btns.forEach(b => b.disabled = true);

        if (selected === correct) {
            btn.classList.add('correct');
            feedback.innerHTML = `<div class="alert success"><i class="fas fa-check"></i> Correct!</div>`;
        } else {
            btn.classList.add('wrong');
            btns[correct].classList.add('correct');
            feedback.innerHTML = `<div class="alert error"><i class="fas fa-times"></i> Incorrect. The answer is ${btns[correct].innerText}</div>`;
        }

        document.getElementById('next-btn-container').style.display = 'block';
    }

    nextPractice() {
        if (this.currentQuestionIndex < this.practiceQuestions.length - 1) {
            this.currentQuestionIndex++;
            this.renderPracticeSession();
        } else {
            // End of sesson
            let container = document.getElementById('tab-content');
            if (!container) container = this.getContentContainer();

            container.innerHTML = `
            <div class="start-screen fade-in">
                <div class="icon-circle success"><i class="fas fa-check"></i></div>
                <h3>Session Complete!</h3>
                <p>Good job. You can continue practicing or take the quiz.</p>
                <div class="actions">
                    <button class="btn btn-secondary" onclick="manager.reloadTopic()">Back to Menu</button>
                    ${container.id === 'tab-content' ?
                    `<button class="btn btn-primary" onclick="manager.switchTab('test')">Take Quiz</button>` :
                    `<button class="btn btn-primary" onclick="manager.startTest()">Take Test</button>`
                }
                </div>
            </div>
            `;
        }
    }

    reloadTopic() {
        // Helper to go back to the start of the topic (Tab view or Legacy view)
        if (this.currentTopicContent.microtopics) {
            this.switchTab('study');
        } else {
            this.loadTopic(this.topics[this.currentTopicIndex].id);
        }
    }

    renderTest() {
        const question = this.testQuestions[this.currentQuestionIndex];
        let container = document.getElementById('tab-content');
        if (!container) container = this.getContentContainer();

        let optionsHtml = '';
        if (question.type === 'input') {
            optionsHtml = `
            <div class="input-question">
                <input type="text" id="test-input" placeholder="Enter answer" class="form-control" autocomplete="off">
                    <button class="btn btn-secondary" onclick="manager.submitTestInput('${question.answer}')">Submit</button>
                </div>
        `;
        } else {
            optionsHtml = `
            <div class="options-grid">
                ${question.options.map((opt, i) => `
                        <button class="option-btn" onclick="manager.submitTestAnswer(${i}, ${question.correct})">
                            ${opt}
                        </button>
                    `).join('')
                }
                </div>
            `;
        }

        container.innerHTML = `
            <div class="test-container fade-in">
                <div class="progress-header">
                    <span>Test ${this.currentQuestionIndex + 1}/${this.testQuestions.length}</span>
                    <div class="progress-bar"><div style="width: ${(this.currentQuestionIndex / this.testQuestions.length) * 100}%"></div></div>
                </div>
                 <div class="question-card">
                    <p class="question-text">${question.q}</p>
                    ${optionsHtml}
                </div>
            </div>
            `;
        if (window.renderMathInElement) renderMathInElement(container);
    }

    submitTestInput(correctAnswer) {
        const input = document.getElementById('test-input');
        const userVal = input.value.trim();

        if (userVal === correctAnswer || parseFloat(userVal) === parseFloat(correctAnswer)) {
            this.score++;
        }
        this.nextTestQuestion();
    }

    submitTestAnswer(selected, correct) {
        if (selected === correct) {
            this.score++;
        }
        this.nextTestQuestion();
    }

    nextTestQuestion() {
        if (this.currentQuestionIndex < this.testQuestions.length - 1) {
            this.currentQuestionIndex++;
            this.renderTest();
        } else {
            this.completeTest();
        }
    }

    completeTest() {
        const percentage = (this.score / this.testQuestions.length) * 100;
        const passed = percentage >= 80;
        let container = document.getElementById('tab-content');
        if (!container) container = this.getContentContainer();

        let message, action;

        if (passed) {
            // Passed Logic
            const topicId = this.topics[this.currentTopicIndex].id;
            const currentProgress = this.progress[topicId];

            if (this.state.includes('remediation')) { // Remedial passed
                message = `
            <div class="result-card success">
                <i class="fas fa-check result-icon"></i>
                <h2>Concept Clarified!</h2>
                <p>You seem ready to try the standard path again.</p>
            </div>
            `;
                action = `<button class="btn btn-primary" onclick="manager.startPractice(1)">Return to Level 1 <i class="fas fa-arrow-right"></i></button>`;
            } else { // Standard passed
                if (this.currentLevel < 3) {
                    // Unlock next level
                    if (currentProgress.practiceLevel === this.currentLevel) {
                        currentProgress.practiceLevel++;
                        currentProgress.testLevel++;
                    }
                    message = `
            <div class="result-card success">
                <i class="fas fa-star result-icon"></i>
                <h2>Level ${this.currentLevel} Complete!</h2>
                <p>Score: ${percentage}%. Level ${this.currentLevel + 1} Unlocked.</p>
            </div>
            `;
                    action = `<button class="btn btn-primary" onclick="manager.startPractice(${this.currentLevel + 1})">Start Level ${this.currentLevel + 1} <i class="fas fa-arrow-right"></i></button>`;
                } else {
                    // Mastered all 3 levels
                    currentProgress.status = 'mastered';
                    if (this.currentTopicIndex < this.topics.length - 1) {
                        const nextId = this.topics[this.currentTopicIndex + 1].id;
                        if (this.progress[nextId].status === 'locked') {
                            this.progress[nextId].status = 'unlocked';
                        }
                    }
                    message = `
            <div class="result-card success">
                <i class="fas fa-trophy result-icon"></i>
                <h2>Topic Mastered!</h2>
                <p>You have completed all 3 levels of ${this.topics[this.currentTopicIndex].title}!</p>
            </div>
            `;
                    action = `<button class="btn btn-primary" onclick="manager.advanceTopic()">Next Topic <i class="fas fa-forward"></i></button>`;

                    if (window.confetti) window.confetti();
                }
            }

            this.saveProgress();
            this.renderTopicList();

        } else {
            message = `
            <div class="result-card warning">
                <i class="fas fa-sync result-icon"></i>
                <h2>Keep Trying!</h2>
                <p>You scored ${percentage}%. You need 80% to pass.</p>
                <p>Let's look at this topic in a simpler way.</p>
            </div>
            `;
            action = `<button class="btn btn-primary" onclick="manager.startRemediation()">Review Concept <i class="fas fa-redo"></i></button>`;
        }

        container.innerHTML = `
            <div class="results-container fade-in">
                ${message}
                <div class="actions">
                    ${action}
                </div>
            </div>
            `;
    }

    advanceTopic() {
        if (this.currentTopicIndex < this.topics.length - 1) {
            this.currentTopicIndex++;
            this.loadTopic(this.topics[this.currentTopicIndex].id);
        } else {
            document.getElementById('mastery-content').innerHTML = `
            <div class="completion-screen fade-in">
                <i class="fas fa-graduation-cap"></i>
                <h2>Subject Completed!</h2>
                <p>You have mastered all topics in this subject.</p>
                <a href="/maths-mastery/" class="btn btn-secondary">Back to Menu</a>
            </div>
            `;
        }
    }

    toggleView(mode) {
        // mode: 'path' or 'topic'
        const isMobile = window.innerWidth <= 768;
        if (!isMobile) return;

        const sidebar = document.querySelector('.topic-sidebar');
        const content = document.querySelector('.mastery-content');

        if (mode === 'path') {
            sidebar.style.display = 'flex';
            content.style.display = 'none';
            // Scroll to top of path
            window.scrollTo(0, 0);
        } else {
            sidebar.style.display = 'none';
            content.style.display = 'block';
            // Scroll to top of content
            window.scrollTo(0, 0);
        }
    }

    renderBackButton() {
        const isMobile = window.innerWidth <= 768;
        if (!isMobile) return '';

        return `
            <button class="btn-back-path" onclick="manager.toggleView('path')">
                <i class="fas fa-arrow-left"></i> Back to Path
            </button>
        `;
    }

    updateActiveTopicUI(topicId) {
        document.querySelectorAll('.topic-item').forEach(el => el.classList.remove('active'));
        const activeItem = Array.from(document.querySelectorAll('.topic-item')).find(el => el.querySelector('.topic-name').innerText === this.getCurrentTopicTitle());
        if (activeItem) activeItem.classList.add('active');
    }

    getCurrentTopicTitle() {
        return this.topics[this.currentTopicIndex].title;
    }
}
