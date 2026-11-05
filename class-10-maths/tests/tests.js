// tests.js - Authentic CBSE Board Examination Paper Engine

const initTests = () => {
    const questionSections = document.querySelectorAll('.question-section');
    const testForm = document.getElementById('test-form');
    const nextBtn = document.getElementById('next-btn');
    const solutionsUrl = testForm ? testForm.getAttribute('data-solutions-url') : null;

    let reattemptBtn = null;
    let initialTimerMinutes = 0;

    // 1. Display all sections in one continuous scrolling paper
    questionSections.forEach(section => {
        section.classList.add('active');
        section.style.display = 'block';
    });

    if (nextBtn) {
        nextBtn.style.display = 'none';
    }

    // 2. Add authentic board exam marks indicator [1], [2], [3], [5] to each question if missing
    questionSections.forEach(section => {
        let marksText = '';
        const id = section.id.toLowerCase();
        if (id.includes('section-a')) marksText = '[1]';
        else if (id.includes('section-b')) marksText = '[2]';
        else if (id.includes('section-c')) marksText = '[3]';
        else if (id.includes('section-d')) marksText = '[5]';
        else if (id.includes('section-e')) marksText = '[4]';

        if (marksText) {
            section.querySelectorAll('.question-block').forEach(block => {
                const firstP = block.querySelector('p');
                if (firstP && !block.querySelector('.question-marks') && !firstP.textContent.includes('[' + marksText.replace(/[\[\]]/g, '') + ']')) {
                    const marksSpan = document.createElement('span');
                    marksSpan.className = 'question-marks';
                    marksSpan.textContent = marksText;
                    firstP.insertBefore(marksSpan, firstP.firstChild);
                }
            });
        }
    });

    // 3. Format Bottom Actions
    const testActionsContainer = document.querySelector('.test-actions');
    if (testActionsContainer) {
        // Hide next button
        const nb = testActionsContainer.querySelector('.next-section-btn');
        if (nb) nb.style.display = 'none';

        // Add progress tracker if not present
        if (!document.getElementById('mcq-progress-banner')) {
            const banner = document.createElement('div');
            banner.className = 'mcq-progress-banner';
            banner.id = 'mcq-progress-banner';
            banner.innerHTML = '<i class="fas fa-tasks"></i> <span id="mcq-progress-text">MCQs Answered: 0 / 4</span>';
            testActionsContainer.insertBefore(banner, testActionsContainer.firstChild);
        }

        // Action buttons container
        let buttonsWrapper = testActionsContainer.querySelector('.test-action-buttons');
        if (!buttonsWrapper) {
            buttonsWrapper = document.createElement('div');
            buttonsWrapper.className = 'test-action-buttons';

            // Submit button
            const submitBtn = document.getElementById('submit-test-btn') || testActionsContainer.querySelector('.submit-test-btn');
            if (submitBtn) {
                submitBtn.innerHTML = '<i class="fas fa-check-circle"></i> Submit Test & View Solutions';
                buttonsWrapper.appendChild(submitBtn);
            }

            // Print button
            const printBtn = document.createElement('button');
            printBtn.type = 'button';
            printBtn.className = 'print-paper-btn';
            printBtn.innerHTML = '<i class="fas fa-print"></i> Print Paper';
            printBtn.addEventListener('click', () => window.print());
            buttonsWrapper.appendChild(printBtn);

            // Solutions link
            if (solutionsUrl) {
                const solLink = document.createElement('a');
                solLink.href = solutionsUrl;
                solLink.className = 'solutions-direct-link';
                solLink.innerHTML = '<i class="fas fa-lightbulb"></i> View Solutions Directly';
                buttonsWrapper.appendChild(solLink);
            }

            testActionsContainer.appendChild(buttonsWrapper);
        }

        // Re-attempt button
        if (!reattemptBtn && !document.getElementById('reattempt-test-btn')) {
            reattemptBtn = document.createElement('button');
            reattemptBtn.type = 'button';
            reattemptBtn.id = 'reattempt-test-btn';
            reattemptBtn.className = 'reattempt-test-btn';
            reattemptBtn.innerHTML = '<i class="fas fa-redo"></i> Re-attempt Test';
            reattemptBtn.style.display = 'none';
            reattemptBtn.addEventListener('click', resetTest);
            buttonsWrapper.appendChild(reattemptBtn);
        }
    }

    // 4. MCQ Tracking
    const setupMCQTracking = () => {
        if (!testForm) return;

        const mcqRadios = testForm.querySelectorAll('input[type="radio"]');
        const questionNames = new Set();
        mcqRadios.forEach(r => questionNames.add(r.name));
        const totalMCQs = questionNames.size;

        const updateMCQCounter = () => {
            let answered = 0;
            questionNames.forEach(name => {
                if (testForm.querySelector(`input[name="${name}"]:checked`)) {
                    answered++;
                }
            });

            const progressText = document.getElementById('mcq-progress-text');
            if (progressText) {
                progressText.textContent = `MCQs Answered: ${answered} of ${totalMCQs}`;
            }
        };

        mcqRadios.forEach(radio => {
            if (radio.checked) {
                const label = radio.closest('label');
                if (label) label.classList.add('selected');
            }

            radio.addEventListener('change', () => {
                const name = radio.name;
                testForm.querySelectorAll(`input[name="${name}"]`).forEach(r => {
                    const label = r.closest('label');
                    if (label) {
                        if (r.checked) label.classList.add('selected');
                        else label.classList.remove('selected');
                    }
                });
                updateMCQCounter();
            });
        });

        updateMCQCounter();
    };
    setupMCQTracking();

    // 5. Timer Logic
    if (window.testConfig && window.testConfig.time) {
        const timeMatch = window.testConfig.time.match(/(\d+)/);
        if (timeMatch) initialTimerMinutes = parseInt(timeMatch[1], 10);
    }

    if (initialTimerMinutes > 0) {
        initTimer(initialTimerMinutes);
    }

    function initTimer(minutes) {
        let display = document.getElementById('timer-display');
        let timerContainer = document.getElementById('header-timer-pill');

        if (!display) {
            timerContainer = document.createElement('div');
            timerContainer.className = 'header-timer-pill';
            timerContainer.id = 'header-timer-pill';
            timerContainer.innerHTML = `
                <i class="fas fa-stopwatch timer-icon"></i>
                <span class="timer-label">Time Left:</span>
                <span class="timer-digits" id="timer-display">00:00</span>
            `;
            const navActions = document.querySelector('.header-nav-actions');
            if (navActions) {
                navActions.insertBefore(timerContainer, navActions.firstChild);
            } else {
                const headerBanner = document.getElementById('exam-header-banner');
                if (headerBanner) headerBanner.appendChild(timerContainer);
            }
            display = document.getElementById('timer-display');
        }

        let timeRemaining = minutes * 60;

        updateTimerDisplay(timeRemaining, display, timerContainer);

        if (window.examTimerInterval) clearInterval(window.examTimerInterval);
        window.examTimerInterval = setInterval(() => {
            timeRemaining--;
            updateTimerDisplay(timeRemaining, display, timerContainer);

            if (timeRemaining <= 0) {
                clearInterval(window.examTimerInterval);
                if (window.showToast) window.showToast("Time's up! Submitting your test.", "warning");
                submitTest();
            }
        }, 1000);
    }

    function updateTimerDisplay(seconds, displayElement, containerElement) {
        if (seconds < 0) seconds = 0;
        const m = Math.floor(seconds / 60);
        const s = seconds % 60;
        if (displayElement) {
            displayElement.textContent = `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
        }

        if (containerElement) {
            if (seconds < 300) {
                containerElement.classList.add('timer-critical');
                containerElement.classList.remove('timer-warning');
            } else if (seconds < 600) {
                containerElement.classList.add('timer-warning');
                containerElement.classList.remove('timer-critical');
            } else {
                containerElement.classList.remove('timer-warning', 'timer-critical');
            }
        }
    }

    // 6. Submit & Reset
    const submitBtn = document.getElementById('submit-test-btn') || document.querySelector('.submit-test-btn');
    if (submitBtn) {
        submitBtn.addEventListener('click', (e) => {
            e.preventDefault();
            submitTest();
        });
    }

    if (testForm) {
        testForm.addEventListener('submit', (e) => {
            e.preventDefault();
            submitTest();
        });
    }

    function submitTest() {
        if (!testForm) return;

        if (window.examTimerInterval) {
            clearInterval(window.examTimerInterval);
        }

        let scoreMessage = '';
        if (window.testConfig && window.testConfig.answers) {
            let score = 0;
            let total = 0;
            const answers = window.testConfig.answers;

            for (const [qName, correctVal] of Object.entries(answers)) {
                const options = testForm.querySelectorAll(`input[name="${qName}"]`);
                if (options.length === 0) continue;

                total++;
                const selected = testForm.querySelector(`input[name="${qName}"]:checked`);

                options.forEach(opt => {
                    const label = opt.closest('label');
                    if (!label) return;

                    if (opt.value === correctVal) {
                        label.style.borderColor = '#059669';
                        label.style.backgroundColor = '#ecfdf5';
                        label.style.color = '#065f46';
                        label.style.fontWeight = '700';
                    } else if (opt.checked && opt.value !== correctVal) {
                        label.style.borderColor = '#dc2626';
                        label.style.backgroundColor = '#fef2f2';
                        label.style.color = '#991b1b';
                        label.style.textDecoration = 'line-through';
                    }
                });

                if (selected && selected.value === correctVal) {
                    score++;
                }
            }

            if (total > 0) {
                scoreMessage = ` | MCQ Score: ${score} / ${total}`;
            }
        }

        const inputs = testForm.querySelectorAll('input, textarea, button');
        inputs.forEach(input => input.disabled = true);

        if (reattemptBtn) {
            reattemptBtn.style.display = 'inline-flex';
            reattemptBtn.disabled = false;
        }

        if (solutionsUrl) {
            const toastMsg = `Test submitted!${scoreMessage}. Redirecting to solutions...`;
            if (window.showToast) window.showToast(toastMsg, 'success');
            else console.log(toastMsg);

            setTimeout(() => {
                window.location.href = solutionsUrl;
            }, 2000);
            return;
        }

        const solutionsSection = document.getElementById('solutions');
        if (solutionsSection) {
            solutionsSection.style.display = 'block';
            solutionsSection.scrollIntoView({ behavior: 'smooth' });
        }
    }

    function resetTest() {
        if (!testForm) return;

        testForm.querySelectorAll('input, textarea, select, button').forEach(control => {
            if (control.tagName === 'BUTTON') {
                control.disabled = false;
                return;
            }
            if (control.type === 'radio' || control.type === 'checkbox') {
                control.checked = false;
            } else {
                control.value = '';
            }
            control.disabled = false;
        });

        testForm.querySelectorAll('label').forEach(label => {
            label.classList.remove('selected');
            label.style.borderColor = '';
            label.style.backgroundColor = '';
            label.style.color = '';
            label.style.fontWeight = '';
            label.style.textDecoration = '';
        });

        testForm.reset();
        window.scrollTo({ top: 0, behavior: 'smooth' });

        if (reattemptBtn) {
            reattemptBtn.style.display = 'none';
        }

        const progressText = document.getElementById('mcq-progress-text');
        if (progressText) progressText.textContent = 'MCQs Answered: 0 of 4';

        if (initialTimerMinutes > 0) {
            if (window.examTimerInterval) clearInterval(window.examTimerInterval);
            initTimer(initialTimerMinutes);
        }
    }

    // 7. MathJax typeset on load
    if (window.MathJax && typeof window.MathJax.typesetPromise === 'function') {
        try {
            window.MathJax.typesetPromise().catch(() => {});
        } catch (e) {}
    }
};

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initTests);
} else {
    initTests();
}
