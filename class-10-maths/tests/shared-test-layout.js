(function () {
    const config = window.testConfig || {
        title: 'Periodic Test - 1',
        subtitle: 'Class 10 - Mathematics',
        time: '30 Minutes',
        marks: '25',
        backLink: '../../index.html',
        backText: 'Class 10 Home',
        instructions: []
    };

    // Minimal sticky toolbar with back-link, integrated timer, and print paper button
    const headerHTML = `
    <div class="exam-header-banner" id="exam-header-banner">
        <div class="container">
            <div class="header-nav-bar">
                <a href="${config.backLink}" class="back-link">
                    <i class="fas fa-arrow-left"></i> ${config.backText}
                </a>
                <div class="header-nav-actions">
                    <div class="header-timer-pill" id="header-timer-pill">
                        <i class="fas fa-stopwatch timer-icon"></i>
                        <span class="timer-label">Time Left:</span>
                        <span class="timer-digits" id="timer-display">--:--</span>
                    </div>
                    <button type="button" class="paper-print-trigger-btn" onclick="window.print()">
                        <i class="fas fa-print"></i> Print Paper
                    </button>
                </div>
            </div>
        </div>
    </div>`;

    const footerHTML = `
    <footer class="test-footer-simple">
        <div class="container">
            <p>&copy; 2026 SJMaths. All rights reserved.</p>
            <p><a href="${config.backLink}">Back to Class 10 Dashboard</a></p>
        </div>
    </footer>`;

    // Inject Top Bar below the Global Site Header
    const siteHeaderContainer = document.getElementById('header-container');
    if (siteHeaderContainer) {
        siteHeaderContainer.insertAdjacentHTML('afterend', headerHTML);
    } else {
        document.body.insertAdjacentHTML('afterbegin', headerHTML);
    }

    const initLayout = () => {
        // Inject Footer after main content
        const main = document.querySelector('main');
        if (main && !document.querySelector('.test-footer-simple')) {
            main.insertAdjacentHTML('afterend', footerHTML);
        }

        const testForm = document.getElementById('test-form');
        if (testForm && !testForm.querySelector('.paper-sheet-header')) {
            const listItems = (config.instructions && config.instructions.length > 0)
                ? config.instructions.map(item => `<li>${item}</li>`).join('')
                : `
                    <li>The question paper consists of 5 sections: A, B, C, D, and E.</li>
                    <li><strong>Section A:</strong> 3 MCQs and 1 Assertion-Reason (1 mark each).</li>
                    <li><strong>Section B:</strong> 3 questions of 2 marks each.</li>
                    <li><strong>Section C:</strong> 2 questions of 3 marks each.</li>
                    <li><strong>Section D:</strong> 1 question of 5 marks.</li>
                    <li><strong>Section E:</strong> 1 Case-based question of 4 marks.</li>
                    <li>All questions are compulsory. Use of calculators is not permitted.</li>
                `;

            const paperHeaderHTML = `
                <div class="paper-sheet-header">
                    <div class="paper-roll-row">
                        <span>Roll No.</span>
                        <span class="paper-roll-line">...........................................................................</span>
                    </div>
                    <div class="paper-board-heading">CENTRAL BOARD OF SECONDARY EDUCATION</div>
                    <h1 class="paper-main-title">${config.title.toUpperCase()}</h1>
                    <div class="paper-class-subject">CLASS X — MATHEMATICS</div>
                    <div class="paper-chapter-name">${(config.subtitle || '').replace(/^Class\s*10\s*-\s*Mathematics\s*/i, '').replace(/[()]/g, '').trim()}</div>
                    <div class="paper-meta-strip">
                        <span class="meta-item"><strong>Time Allowed:</strong> ${config.time}</span>
                        <span class="meta-item"><strong>Maximum Marks:</strong> ${config.marks}</span>
                    </div>
                    <div class="paper-double-rule"></div>
                    <div class="paper-general-instructions">
                        <div class="instructions-head">General Instructions:</div>
                        <ol class="instructions-list">
                            ${listItems}
                        </ol>
                    </div>
                    <div class="paper-double-rule"></div>
                </div>
            `;
            testForm.insertAdjacentHTML('afterbegin', paperHeaderHTML);
        }

        // Add End of Paper marker before action buttons
        if (testForm && !testForm.querySelector('.paper-end-mark')) {
            const testActions = testForm.querySelector('.test-actions');
            const endMarkHTML = `<div class="paper-end-mark">— END OF QUESTION PAPER —</div>`;
            if (testActions) {
                testActions.insertAdjacentHTML('beforebegin', endMarkHTML);
            } else {
                testForm.insertAdjacentHTML('beforeend', endMarkHTML);
            }
        }
    };

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initLayout);
    } else {
        initLayout();
    }
})();
