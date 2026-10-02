/**
 * UP Upper Primary Teacher - Unified Topic Runtime Engine
 * Handles Tab Switching, Checklist Sync, MCQ Assessment, Mini Test Engine & Back-to-Top
 */

(function () {
    'use strict';

    // Global Configuration Fallbacks
    const STORAGE_KEY = window.TOPIC_STORAGE_KEY || 'up-upper-primary-teacher-checklist-v2';
    const CHECKBOX_ID = window.TOPIC_CHECKBOX_ID || '';
    const testData = window.testData || [];

    // Tab Switching
    function initTabs() {
        const tabBtns = document.querySelectorAll('.study-tab-btn');
        if (!tabBtns.length) return;

        tabBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                const targetTab = btn.getAttribute('data-tab');
                document.querySelectorAll('.study-tab-btn').forEach(b => b.classList.remove('active'));
                document.querySelectorAll('.study-tab-pane').forEach(p => p.classList.remove('active'));
                btn.classList.add('active');
                const targetPane = document.getElementById('tab-' + targetTab);
                if (targetPane) targetPane.classList.add('active');
            });
        });
    }

    // Checkbox & Topic Completion Sync
    function initCompletionStatus() {
        if (!CHECKBOX_ID) return;
        try {
            const stored = JSON.parse(localStorage.getItem(STORAGE_KEY)) || {};
            const isDone = !!stored[CHECKBOX_ID];
            updateCompletionUI(isDone);
        } catch (e) {
            console.warn('Storage sync error:', e);
        }
    }

    window.toggleTopicStatus = function () {
        if (!CHECKBOX_ID) return;
        try {
            const stored = JSON.parse(localStorage.getItem(STORAGE_KEY)) || {};
            const current = !stored[CHECKBOX_ID];
            stored[CHECKBOX_ID] = current;
            localStorage.setItem(STORAGE_KEY, JSON.stringify(stored));
            updateCompletionUI(current);
        } catch (e) {
            console.warn('Storage toggle error:', e);
        }
    };

    function updateCompletionUI(isDone) {
        const btn = document.getElementById('topicCompletionBtn');
        const text = document.getElementById('completionBtnText');
        const desc = document.getElementById('statusDesc');
        if (!btn || !text) return;
        if (isDone) {
            btn.classList.add('completed');
            text.textContent = 'Completed ✓';
            if (desc) desc.textContent = 'Topic mastered. Progress is recorded in your study checklist.';
        } else {
            btn.classList.remove('completed');
            text.textContent = 'Mark as Completed';
            if (desc) desc.textContent = 'Mark complete once covered. Progress syncs automatically with the main syllabus hub.';
        }
    }

    // MCQ Practice Mode
    const userAnswers = {};
    window.handleMcqOptionClick = function (btn, qIdx) {
        const card = document.getElementById('mcq-card-' + qIdx);
        if (!card) return;
        const allBtns = card.querySelectorAll('.mcq-option-btn');
        allBtns.forEach(b => {
            b.disabled = true;
            if (b.getAttribute('data-correct') === 'true') {
                b.classList.add('opt-correct');
            }
        });
        const isCorrect = btn.getAttribute('data-correct') === 'true';
        if (!isCorrect) {
            btn.classList.add('opt-wrong');
        }
        userAnswers[qIdx] = isCorrect;
        const exp = document.getElementById('mcq-exp-' + qIdx);
        if (exp) exp.style.display = 'block';

        const totalQuestions = document.querySelectorAll('.mcq-item-card').length || 10;
        const answeredCount = Object.keys(userAnswers).length;
        const correctCount = Object.values(userAnswers).filter(Boolean).length;
        const progressEl = document.getElementById('practiceProgressText');
        const badgeEl = document.getElementById('practiceScoreBadge');
        if (progressEl) progressEl.textContent = answeredCount + ' of ' + totalQuestions + ' Answered';
        if (badgeEl) badgeEl.textContent = 'Score: ' + correctCount + ' / ' + totalQuestions;
    };

    // Mini Test Interactive Engine
    let testCurrentIndex = 0;
    let testUserAnswers = {};
    let testTimeRemaining = 300;
    let testTimerInterval = null;

    window.startMiniTest = function () {
        const intro = document.getElementById('miniTestIntro');
        const active = document.getElementById('miniTestActive');
        const result = document.getElementById('miniTestResult');
        if (intro) intro.style.display = 'none';
        if (active) active.style.display = 'block';
        if (result) result.style.display = 'none';

        testCurrentIndex = 0;
        testUserAnswers = {};
        testTimeRemaining = 300;
        renderTestQuestion(0);
        startTimer();
    };

    function startTimer() {
        clearInterval(testTimerInterval);
        testTimerInterval = setInterval(() => {
            testTimeRemaining--;
            const mins = Math.floor(testTimeRemaining / 60);
            const secs = testTimeRemaining % 60;
            const display = document.getElementById('timerDisplay');
            if (display) {
                display.textContent = (mins < 10 ? '0' : '') + mins + ':' + (secs < 10 ? '0' : '') + secs;
            }
            if (testTimeRemaining <= 0) {
                clearInterval(testTimerInterval);
                window.submitMiniTest();
            }
        }, 1000);
    }

    function renderTestQuestion(idx) {
        if (!testData || !testData[idx]) return;
        const q = testData[idx];
        const container = document.getElementById('testQuestionContainer');
        const currentQEl = document.getElementById('testCurrentQ');
        if (currentQEl) currentQEl.textContent = (idx + 1);

        const isHi = document.body.classList.contains('lang-mode-hi');
        const qText = isHi && q.question_hi ? q.question_hi : q.question;
        const opts = isHi && q.options_hi && q.options_hi.length ? q.options_hi : q.options;

        let optionsHtml = '';
        (opts || []).forEach((opt, optIdx) => {
            const letter = ['A', 'B', 'C', 'D'][optIdx];
            const isSelected = testUserAnswers[idx] === optIdx;
            const cleaned = String(opt || '').replace(/^(\([A-D]\)|\[[A-D]\]|[A-D][\).:-]|[A-D]\s*[-–—]\s*|[A-D]\s+)\s*/i, '').trim();
            optionsHtml += `
                <button type="button" class="mcq-option-btn ${isSelected ? 'opt-correct' : ''}" style="margin-bottom: 0.6rem;" onclick="selectTestOption(${idx}, ${optIdx})">
                    <span class="opt-label">${letter}</span>
                    <span>${cleaned}</span>
                </button>`;
        });

        if (container) {
            container.innerHTML = `
                <div style="font-size: 1.05rem; font-weight: 600; color: var(--text-headline); margin-bottom: 1.25rem;">
                    <p><strong>${idx + 1}.</strong> ${qText}</p>
                </div>
                <div>${optionsHtml}</div>
            `;
        }

        const prevBtn = document.getElementById('testPrevBtn');
        const nextBtn = document.getElementById('testNextBtn');
        const submitBtn = document.getElementById('testSubmitBtn');
        if (prevBtn) prevBtn.disabled = (idx === 0);
        if (idx === testData.length - 1) {
            if (nextBtn) nextBtn.style.display = 'none';
            if (submitBtn) submitBtn.style.display = 'inline-block';
        } else {
            if (nextBtn) nextBtn.style.display = 'inline-block';
            if (submitBtn) submitBtn.style.display = 'none';
        }
    }

    window.selectTestOption = function (qIdx, optIdx) {
        testUserAnswers[qIdx] = optIdx;
        renderTestQuestion(qIdx);
    };

    window.navTest = function (step) {
        testCurrentIndex += step;
        if (testCurrentIndex < 0) testCurrentIndex = 0;
        if (testCurrentIndex >= testData.length) testCurrentIndex = testData.length - 1;
        renderTestQuestion(testCurrentIndex);
    };

    window.submitMiniTest = function () {
        clearInterval(testTimerInterval);
        const active = document.getElementById('miniTestActive');
        const result = document.getElementById('miniTestResult');
        if (active) active.style.display = 'none';
        if (result) result.style.display = 'block';

        let correct = 0;
        let incorrect = 0;
        let unattempted = 0;

        testData.forEach((q, idx) => {
            const userAns = testUserAnswers[idx];
            if (userAns === undefined) {
                unattempted++;
            } else if (userAns === q.correct_index) {
                correct++;
            } else {
                incorrect++;
            }
        });

        const score = (correct * 3) - (incorrect * 1);
        const maxScore = testData.length * 3;

        const scoreBanner = document.getElementById('resultScoreBanner');
        const resultTitle = document.getElementById('resultTitle');
        if (scoreBanner) scoreBanner.textContent = 'Score: ' + score + ' / ' + maxScore;
        if (resultTitle) {
            resultTitle.textContent = score >= 20 ? 'Outstanding Performance!' : (score >= 12 ? 'Good Effort!' : 'Needs Review & Practice');
        }

        const breakdown = document.getElementById('resultBreakdownGrid');
        if (breakdown) {
            breakdown.innerHTML = `
                <div style="display: flex; justify-content: center; gap: 1rem; margin: 1.5rem 0; flex-wrap: wrap;">
                    <div class="test-stat-chip" style="color: #065f46; background: #ecfdf5; border-color: #a7f3d0;"><i class="fas fa-check"></i> Correct: ${correct} (+3 each)</div>
                    <div class="test-stat-chip" style="color: #991b1b; background: #fef2f2; border-color: #fecaca;"><i class="fas fa-times"></i> Incorrect: ${incorrect} (-1 each)</div>
                    <div class="test-stat-chip" style="color: #475569;"><i class="fas fa-minus"></i> Unattempted: ${unattempted}</div>
                </div>
            `;
        }
    };

    window.resetMiniTest = function () {
        const intro = document.getElementById('miniTestIntro');
        const active = document.getElementById('miniTestActive');
        const result = document.getElementById('miniTestResult');
        if (intro) intro.style.display = 'block';
        if (active) active.style.display = 'none';
        if (result) result.style.display = 'none';
    };

    window.updateMasteryProgress = function () {
        // Optional tracking of mastery checklist
    };

    // Bilingual Language Toggle
    window.toggleLanguageMode = function () {
        document.body.classList.toggle('lang-mode-hi');
        const isHi = document.body.classList.contains('lang-mode-hi');
        try {
            localStorage.setItem('up_topic_lang', isHi ? 'hi' : 'en');
            localStorage.setItem('sjmaths_preferred_language', isHi ? 'hi' : 'en');
        } catch (e) {}

        const active = document.getElementById('miniTestActive') || document.getElementById('testActiveContainer');
        if (active && active.style.display !== 'none') {
            renderTestQuestion(testCurrentIndex);
        }
    };

    // Back to top button
    function initBackToTop() {
        const btn = document.getElementById('backToTopBtn');
        if (!btn) return;
        window.addEventListener('scroll', () => {
            if (window.scrollY > 300) {
                btn.style.display = 'flex';
            } else {
                btn.style.display = 'none';
            }
        });
        btn.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    // Auto-init on page load
    document.addEventListener('DOMContentLoaded', () => {
        initTabs();
        initCompletionStatus();
        initBackToTop();

        // Restore language preference if previously set
        try {
            const pref = localStorage.getItem('up_topic_lang') || localStorage.getItem('sjmaths_preferred_language');
            if (pref === 'hi') {
                document.body.classList.add('lang-mode-hi');
            }
        } catch (e) {}
    });
})();
