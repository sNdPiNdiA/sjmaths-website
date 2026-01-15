// tests.js (now includes chapter-1-test.js logic for section navigation)

const initTests = () => {
    const navButtons = document.querySelectorAll('.nav-button');
    const questionSections = document.querySelectorAll('.question-section');
    const solutionsSection = document.getElementById('solutions');
    const testForm = document.getElementById('test-form');
    const nextBtn = document.getElementById('next-btn');
    const sidebarToggle = document.getElementById('sidebar-toggle');
    const sidebar = document.querySelector('.sidebar');

    // Function to show a specific section
    const showSection = (sectionId) => {
        questionSections.forEach(section => {
            section.classList.remove('active');
        });
        navButtons.forEach(button => {
            button.classList.remove('active');
        });

        const targetSection = document.getElementById(sectionId);
        if (targetSection) {
            targetSection.classList.add('active');
            const activeButton = document.querySelector(`.nav-button[data-section="${sectionId}"]`);
            if (activeButton) {
                activeButton.classList.add('active');
            }
        }
        // Typeset MathJax again for the newly visible section
        if (window.MathJax && typeof window.MathJax.typesetPromise === 'function') {
            window.MathJax.typesetPromise([targetSection]);
        } else if (window.MathJax && typeof window.MathJax.typeset === 'function') {
            // Fallback for typeset if typesetPromise isn't ready
            window.MathJax.typeset([targetSection]);
        }

        // Update Next Button Visibility
        if (nextBtn) {
            const sectionIds = Array.from(questionSections).map(s => s.id);
            const currentIndex = sectionIds.indexOf(sectionId);
            if (currentIndex === sectionIds.length - 1 || sectionId === 'solutions') {
                nextBtn.style.display = 'none';
            } else {
                nextBtn.style.display = 'inline-block';
            }
        }

        // Close sidebar on mobile after selection
        if (window.innerWidth <= 992 && sidebar && sidebar.classList.contains('active')) {
            sidebar.classList.remove('active');
            if (sidebarToggle) sidebarToggle.innerHTML = '<i class="fas fa-bars"></i>';
        }
    };

    // Event listeners for navigation buttons
    navButtons.forEach(button => {
        button.addEventListener('click', () => {
            const sectionId = button.dataset.section;
            showSection(sectionId);
        });
    });

    // Next Section Button Logic
    if (nextBtn) {
        nextBtn.addEventListener('click', () => {
            const activeSection = document.querySelector('.question-section.active');
            if (activeSection) {
                const sectionIds = Array.from(questionSections).map(s => s.id);
                const currentIndex = sectionIds.indexOf(activeSection.id);
                if (currentIndex >= 0 && currentIndex < sectionIds.length - 1) {
                    showSection(sectionIds[currentIndex + 1]);
                    window.scrollTo({ top: 0, behavior: 'smooth' });
                }
            }
        });
    }

    // Sidebar Toggle Logic
    if (sidebarToggle && sidebar) {
        sidebarToggle.addEventListener('click', (e) => {
            e.preventDefault();
            e.stopPropagation();
            sidebar.classList.toggle('active');
            // Change icon
            const icon = sidebarToggle.querySelector('i');
            if (sidebar.classList.contains('active')) {
                icon.className = 'fas fa-times';
            } else {
                icon.className = 'fas fa-bars';
            }
        });
    }

    // Initial load: show the first question section by default
    showSection('section-a');

    // --- Timer Logic ---
    let durationInMinutes = 0;

    // 1. Try reading from config (New Layout)
    if (window.testConfig && window.testConfig.time) {
        const timeMatch = window.testConfig.time.match(/(\d+)/);
        if (timeMatch) durationInMinutes = parseInt(timeMatch[1], 10);
    }
    // 2. Fallback to scraping (Old Layout)
    else {
        const headerInfo = document.querySelector('.header p');
        if (headerInfo) {
            const timeMatch = headerInfo.innerText.match(/Time:\s*(\d+)\s*Minutes/i);
            if (timeMatch) durationInMinutes = parseInt(timeMatch[1], 10);
        }
    }

    // Only initialize timer if a time is found
    if (durationInMinutes > 0) {
        initTimer(durationInMinutes);
    }

    // Handle form submission
    const submitBtn = document.getElementById('submit-test-btn') || document.querySelector('.submit-test-btn');
    if (submitBtn) {
        submitBtn.addEventListener('click', (e) => {
            e.preventDefault();
            submitTest();
        });
    }

    if (testForm) {
        testForm.addEventListener('submit', (event) => {
            event.preventDefault();
            submitTest();
        });
    }

    function submitTest() {
        const form = document.getElementById('test-form');
        if (!form) return;

        // Get the solutions URL before disabling inputs to ensure it's captured
        const solutionsUrl = form.getAttribute('data-solutions-url');

        // Stop timer if running
        if (window.examTimerInterval) {
            clearInterval(window.examTimerInterval);
        }

        // --- Grading Logic ---
        let scoreMessage = '';
        if (window.testConfig && window.testConfig.answers) {
            let score = 0;
            let total = 0;
            const answers = window.testConfig.answers;

            for (const [qName, correctVal] of Object.entries(answers)) {
                // Check if this question exists in the form
                const options = form.querySelectorAll(`input[name="${qName}"]`);
                if (options.length === 0) continue;

                total++;
                const selected = form.querySelector(`input[name="${qName}"]:checked`);

                // Visual Feedback
                options.forEach(opt => {
                    const label = opt.closest('label');
                    if (!label) return;

                    if (opt.value === correctVal) {
                        // Correct Answer Style
                        label.style.color = '#28a745';
                        label.style.fontWeight = 'bold';
                    } else if (opt.checked && opt.value !== correctVal) {
                        // Wrong Selection Style
                        label.style.color = '#dc3545';
                        label.style.textDecoration = 'line-through';
                    }
                });

                if (selected && selected.value === correctVal) {
                    score++;
                }
            }

            if (total > 0) {
                scoreMessage = `\n\nMCQ Score: ${score} / ${total}`;
            }
        }

        // Disable inputs to prevent further changes
        const inputs = form.querySelectorAll('input, textarea, button');
        inputs.forEach(input => input.disabled = true);

        // Check if there is a separate solutions page configured
        if (solutionsUrl) {
            if (window.showToast) window.showToast('Test submitted!' + scoreMessage + ' Redirecting...', 'success');
            else alert('Test submitted!' + scoreMessage);
            
            setTimeout(() => {
                window.location.href = solutionsUrl;
            }, 2000);
            return;
        }

        // Show alert
        if (window.showToast) window.showToast('Test submitted! Please review the solutions.' + scoreMessage, 'success');
        else alert('Test submitted! Please review the solutions.' + scoreMessage);

        // Automatically show solutions after submission
        showSection('solutions');

        // Scroll to solutions
        const solutionsElement = document.getElementById('solutions');
        if (solutionsElement) {
            solutionsElement.scrollIntoView({ behavior: 'smooth' });
        }
    }

    function initTimer(minutes) {
        // Inject CSS for Timer
        const style = document.createElement('style');
        style.innerHTML = `
            .exam-timer-container {
                position: fixed;
                top: 90px;
                right: 20px;
                background: white;
                padding: 10px 20px;
                border-radius: 50px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.1);
                z-index: 999;
                display: flex;
                align-items: center;
                gap: 10px;
                border: 2px solid var(--primary, #8e44ad);
                font-family: 'Poppins', sans-serif;
                transition: all 0.3s ease;
            }
            .exam-timer-icon {
                color: var(--primary, #8e44ad);
                font-size: 1.2rem;
            }
            .exam-timer-text {
                font-weight: 700;
                font-size: 1.1rem;
                color: #2c3e50;
                min-width: 60px;
                text-align: center;
            }
            .exam-timer-label {
                font-size: 0.85rem;
                color: #666;
                font-weight: 600;
                text-transform: uppercase;
            }
            .timer-warning {
                border-color: #f39c12;
                background: #fef9e7;
            }
            .timer-warning .exam-timer-text, .timer-warning .exam-timer-icon {
                color: #d35400;
            }
            .timer-critical {
                border-color: #e74c3c;
                background: #fceae9;
                animation: pulse 1s infinite;
            }
            .timer-critical .exam-timer-text, .timer-critical .exam-timer-icon {
                color: #c0392b;
            }
            @keyframes pulse {
                0% { transform: scale(1); }
                50% { transform: scale(1.05); }
                100% { transform: scale(1); }
            }
            @media (max-width: 768px) {
                .exam-timer-container {
                    top: auto;
                    bottom: 20px;
                    right: 50%;
                    transform: translateX(50%);
                    width: max-content;
                    padding: 8px 16px;
                }
                .timer-critical {
                    animation: none; /* Reduce distraction on mobile */
                }
            }
        `;
        document.head.appendChild(style);

        // Create Timer HTML
        const timerContainer = document.createElement('div');
        timerContainer.className = 'exam-timer-container';
        timerContainer.innerHTML = `
            <i class="fas fa-stopwatch exam-timer-icon"></i>
            <span class="exam-timer-label">Time Left</span>
            <span class="exam-timer-text" id="timer-display">00:00</span>
        `;
        document.body.appendChild(timerContainer);

        let timeRemaining = minutes * 60;
        const display = document.getElementById('timer-display');

        updateDisplay(timeRemaining, display, timerContainer);

        window.examTimerInterval = setInterval(() => {
            timeRemaining--;
            updateDisplay(timeRemaining, display, timerContainer);

            if (timeRemaining <= 0) {
                clearInterval(window.examTimerInterval);
                if (window.showToast) window.showToast("Time's up! Submitting your test.", "warning");
                else alert("Time's up! Submitting your test.");
                submitTest();
            }
        }, 1000);
    }

    function updateDisplay(seconds, displayElement, containerElement) {
        if (seconds < 0) seconds = 0;
        const m = Math.floor(seconds / 60);
        const s = seconds % 60;
        displayElement.textContent = `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;

        // Color coding logic
        if (seconds < 300) { // Less than 5 mins
            containerElement.classList.add('timer-critical');
            containerElement.classList.remove('timer-warning');
        } else if (seconds < 600) { // Less than 10 mins
            containerElement.classList.add('timer-warning');
        }
    }
};

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initTests);
} else {
    initTests();
}