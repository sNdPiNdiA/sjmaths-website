/**
 * UP Upper Primary Teacher - Unified Topic Runtime Engine
 * Handles Tab Switching, Checklist Sync, MCQ Assessment, Mini Test Engine, Back-to-Top
 * & High-Fidelity KaTeX Mathematical / Scientific Formula Rendering.
 * Fully supports all Topic Page DOM layouts (Patterns 1, 2, and 3).
 */

(function () {
    'use strict';

    // Global Configuration Helpers (dynamic access to avoid script-order race conditions)
    function getStorageKey() {
        return window.TOPIC_STORAGE_KEY || 'up-upper-primary-teacher-checklist-v2';
    }

    function getCheckboxId() {
        return window.TOPIC_CHECKBOX_ID || '';
    }

    function getTestData() {
        return Array.isArray(window.testData) ? window.testData : [];
    }

    // ==========================================
    // Unified High-Fidelity Math Rendering Engine
    // ==========================================
    const KATEX_CSS_URL = 'https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css';
    const KATEX_JS_URL = 'https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js';
    const KATEX_AUTORENDER_URL = 'https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js';

    let isKatexLoading = false;
    let katexReadyCallbacks = [];

    function ensureKatexLoaded(callback) {
        if (window.katex && typeof window.renderMathInElement === 'function') {
            callback();
            return;
        }

        katexReadyCallbacks.push(callback);
        if (isKatexLoading) return;
        isKatexLoading = true;

        // Ensure KaTeX CSS is loaded
        if (!document.querySelector('link[href*="katex"]')) {
            const link = document.createElement('link');
            link.rel = 'stylesheet';
            link.href = KATEX_CSS_URL;
            link.crossOrigin = 'anonymous';
            document.head.appendChild(link);
        }

        function loadScript(src, cb) {
            const existing = document.querySelector(`script[src*="${src.split('/').pop()}"]`);
            if (existing) {
                if (existing.getAttribute('data-loaded') === 'true') {
                    cb();
                    return;
                }
                existing.addEventListener('load', () => {
                    existing.setAttribute('data-loaded', 'true');
                    cb();
                });
                return;
            }

            const s = document.createElement('script');
            s.src = src;
            s.defer = true;
            s.crossOrigin = 'anonymous';
            s.onload = () => {
                s.setAttribute('data-loaded', 'true');
                cb();
            };
            s.onerror = () => {
                console.warn('Failed to load KaTeX script:', src);
                isKatexLoading = false;
            };
            document.head.appendChild(s);
        }

        loadScript(KATEX_JS_URL, () => {
            loadScript(KATEX_AUTORENDER_URL, () => {
                isKatexLoading = false;
                const cbs = katexReadyCallbacks;
                katexReadyCallbacks = [];
                cbs.forEach(cb => {
                    try { cb(); } catch (e) { console.error('Error in KaTeX callback:', e); }
                });
            });
        });
    }

    const KATEX_OPTIONS = {
        delimiters: [
            { left: '$$', right: '$$', display: true },
            { left: '$', right: '$', display: false },
            { left: '\\(', right: '\\)', display: false },
            { left: '\\[', right: '\\]', display: true }
        ],
        ignoredTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'],
        throwOnError: false
    };

    function renderMath(targetElement) {
        const el = targetElement || document.body;
        if (!el) return;
        ensureKatexLoaded(() => {
            if (typeof window.renderMathInElement === 'function') {
                try {
                    window.renderMathInElement(el, KATEX_OPTIONS);
                } catch (e) {
                    console.warn('KaTeX render error:', e);
                }
            }
        });
    }

    window.renderMath = renderMath;

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
                if (targetPane) {
                    targetPane.classList.add('active');
                    renderMath(targetPane);
                }
            });
        });
    }

    // Checkbox & Topic Completion Sync
    function initCompletionStatus() {
        const cid = getCheckboxId();
        if (!cid) return;
        try {
            const stored = JSON.parse(localStorage.getItem(getStorageKey())) || {};
            const isDone = !!stored[cid];
            updateCompletionUI(isDone);
        } catch (e) {
            console.warn('Storage sync error:', e);
        }
    }

    window.toggleTopicStatus = function () {
        const cid = getCheckboxId();
        if (!cid) return;
        try {
            const key = getStorageKey();
            const stored = JSON.parse(localStorage.getItem(key)) || {};
            const current = !stored[cid];
            stored[cid] = current;
            localStorage.setItem(key, JSON.stringify(stored));
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
        if (exp) {
            exp.style.display = 'block';
            renderMath(exp);
        }

        const totalQuestions = document.querySelectorAll('.mcq-item-card').length || 10;
        const answeredCount = Object.keys(userAnswers).length;
        const correctCount = Object.values(userAnswers).filter(Boolean).length;
        const progressEl = document.getElementById('practiceProgressText') || document.getElementById('practiceScoreDisplay');
        const badgeEl = document.getElementById('practiceScoreBadge');
        if (progressEl) {
            if (progressEl.id === 'practiceScoreDisplay') {
                progressEl.textContent = 'स्कोर: ' + correctCount + ' / ' + totalQuestions;
            } else {
                progressEl.textContent = answeredCount + ' of ' + totalQuestions + ' Answered';
            }
        }
        if (badgeEl) badgeEl.textContent = 'Score: ' + correctCount + ' / ' + totalQuestions;
    };

    // ==========================================
    // Mini Test Interactive Engine (Universal)
    // Supports Pattern 1, Pattern 2 & Pattern 3
    // ==========================================
    let testCurrentIndex = 0;
    let testUserAnswers = {};
    let testTimeRemaining = 300;
    let testTimerInterval = null;

    function getTestIntroElement() {
        return document.getElementById('miniTestIntro') ||
            document.getElementById('testIntroScreen') ||
            document.getElementById('testRulesCard');
    }

    function getTestActiveElement() {
        return document.getElementById('miniTestActive') ||
            document.getElementById('testActiveScreen') ||
            document.getElementById('testActiveContainer');
    }

    function getTestResultElement() {
        return document.getElementById('miniTestResult') ||
            document.getElementById('testResultScreen') ||
            document.getElementById('testScoreModal');
    }

    function getQuestionsContainer() {
        return document.getElementById('testQuestionContainer') ||
            document.getElementById('testQuestionsContainer') ||
            document.getElementById('testQuestionsTarget');
    }

    window.startMiniTest = function () {
        const intro = getTestIntroElement();
        const active = getTestActiveElement();
        const result = getTestResultElement();

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
            const formatted = (mins < 10 ? '0' : '') + mins + ':' + (secs < 10 ? '0' : '') + secs;

            const timerDisplay = document.getElementById('timerDisplay');
            const testTimerText = document.getElementById('testTimerText');

            if (timerDisplay) {
                timerDisplay.textContent = formatted;
            }
            if (testTimerText) {
                if (testTimerText.tagName.toLowerCase() === 'span') {
                    testTimerText.textContent = formatted;
                } else {
                    testTimerText.innerHTML = '<i class="fas fa-clock"></i> ' + formatted;
                }
            }

            if (testTimeRemaining <= 0) {
                clearInterval(testTimerInterval);
                window.submitMiniTest();
            }
        }, 1000);
    }

    function renderTestQuestion(idx) {
        const testData = getTestData();
        if (!testData || !testData[idx]) return;
        const q = testData[idx];
        const container = getQuestionsContainer();
        const currentQEl = document.getElementById('testCurrentQ') || document.getElementById('testQIndexIndicator');
        if (currentQEl) {
            if (currentQEl.id === 'testCurrentQ') {
                currentQEl.textContent = (idx + 1);
            } else {
                currentQEl.textContent = (idx + 1) + ' / ' + testData.length;
            }
        }

        const isHi = document.body.classList.contains('lang-mode-hi') || document.body.classList.contains('lang-hi');
        const qText = isHi && q.question_hi ? q.question_hi : q.question;
        const opts = isHi && q.options_hi && q.options_hi.length ? q.options_hi : q.options;

        let optionsHtml = '';
        (opts || []).forEach((opt, optIdx) => {
            const letter = ['A', 'B', 'C', 'D'][optIdx] || String.fromCharCode(65 + optIdx);
            const isSelected = testUserAnswers[idx] === optIdx;
            const cleaned = String(opt || '').replace(/^(\([A-D]\)|\[[A-D]\]|[A-D][\).:-]|[A-D]\s*[-–—]\s*|[A-D]\s+)\s*/i, '').trim();
            optionsHtml += `
                <button type="button" class="mcq-option-btn ${isSelected ? 'opt-correct' : ''}" style="margin-bottom: 0.6rem;" onclick="selectTestOption(${idx}, ${optIdx})">
                    <span class="opt-label">${letter}</span>
                    <span>${cleaned}</span>
                </button>`;
        });

        // For Pattern 3 (testQuestionsTarget), static prev/next buttons do not exist in HTML, so render them dynamically
        const isPattern3 = container && container.id === 'testQuestionsTarget';
        let navHtml = '';
        if (isPattern3) {
            navHtml = `
                <div class="test-nav-controls" style="display: flex; justify-content: space-between; align-items: center; margin-top: 1.5rem; gap: 0.75rem;">
                    <button type="button" class="test-btn-nav" onclick="navTest(-1)" ${idx === 0 ? 'disabled' : ''} style="background: #f1f5f9; border: 1px solid var(--border-subtle); padding: 0.5rem 1rem; border-radius: 6px; font-weight: 600; cursor: pointer;">
                        <i class="fas fa-chevron-left"></i> Previous
                    </button>
                    <span style="font-weight: 700; color: var(--text-sub);">${idx + 1} / ${testData.length}</span>
                    ${idx === testData.length - 1 ? `
                        <button type="button" class="test-submit-btn" onclick="submitMiniTest()" style="background: var(--gradient-subject); color: #fff; border: none; padding: 0.6rem 1.4rem; border-radius: 8px; font-weight: 700; cursor: pointer;">
                            Submit Test <i class="fas fa-check"></i>
                        </button>
                    ` : `
                        <button type="button" class="test-btn-nav" onclick="navTest(1)" style="background: #f1f5f9; border: 1px solid var(--border-subtle); padding: 0.5rem 1rem; border-radius: 6px; font-weight: 600; cursor: pointer;">
                            Next <i class="fas fa-chevron-right"></i>
                        </button>
                    `}
                </div>
            `;
        }

        if (container) {
            container.innerHTML = `
                <div style="font-size: 1.05rem; font-weight: 600; color: var(--text-headline); margin-bottom: 1.25rem;">
                    <p><strong>${idx + 1}.</strong> ${qText}</p>
                </div>
                <div>${optionsHtml}</div>
                ${navHtml}
            `;
            renderMath(container);
        }

        // Handle static buttons for Pattern 1 and Pattern 2
        const prevBtn = document.getElementById('testPrevBtn') || document.getElementById('btnPrevTestQ');
        const nextBtn = document.getElementById('testNextBtn') || document.getElementById('btnNextTestQ');
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
        const testData = getTestData();
        testCurrentIndex += step;
        if (testCurrentIndex < 0) testCurrentIndex = 0;
        if (testCurrentIndex >= testData.length) testCurrentIndex = testData.length - 1;
        renderTestQuestion(testCurrentIndex);
    };

    window.navigateTestQuestion = window.navTest;

    window.submitMiniTest = function () {
        clearInterval(testTimerInterval);
        const active = getTestActiveElement();
        const result = getTestResultElement();

        if (active) active.style.display = 'none';
        if (result) result.style.display = 'block';

        const testData = getTestData();
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
        const totalAttempted = correct + incorrect;
        const accuracy = totalAttempted > 0 ? Math.round((correct / totalAttempted) * 100) : 0;
        const scorePercent = maxScore > 0 ? Math.round((score / maxScore) * 100) : 0;
        const isHi = document.body.classList.contains('lang-mode-hi') || document.body.classList.contains('lang-hi');

        // 1. Populate Pattern 1 & Pattern 2 score elements
        const scoreValEl = document.getElementById('testResultScore') ||
            document.getElementById('finalScoreVal') ||
            document.getElementById('resultScoreBanner');

        if (scoreValEl) {
            scoreValEl.textContent = `${score} / ${maxScore}`;
        }

        const feedbackEl = document.getElementById('testResultFeedback') ||
            document.getElementById('testAccuracySummary') ||
            document.getElementById('resultTitle');

        const summaryText = isHi
            ? `शुद्धता (Accuracy): ${accuracy}% | सही: ${correct} (+3) | गलत: ${incorrect} (-1) | अप्रयासित: ${unattempted}`
            : `Accuracy: ${accuracy}% | Correct: ${correct} (+3) | Incorrect: ${incorrect} (-1) | Unattempted: ${unattempted}`;

        if (feedbackEl) {
            feedbackEl.textContent = summaryText;
        }

        // 2. Populate Pattern 3 (Math score modal)
        const statCorrect = document.getElementById('statCorrect');
        const statIncorrect = document.getElementById('statIncorrect');
        const statSkipped = document.getElementById('statSkipped');
        const statFinalScore = document.getElementById('statFinalScore');
        const scoreTitle = document.getElementById('scoreTitle');
        const scoreSubtitle = document.getElementById('scoreSubtitle');

        if (statCorrect) statCorrect.textContent = correct;
        if (statIncorrect) statIncorrect.textContent = incorrect;
        if (statSkipped) statSkipped.textContent = unattempted;
        if (statFinalScore) statFinalScore.textContent = `${score} / ${maxScore}`;
        if (scoreTitle) {
            scoreTitle.textContent = score >= 21 ? 'Outstanding Performance!' : (score >= 12 ? 'Good Effort!' : 'Keep Practicing!');
        }
        if (scoreSubtitle) {
            scoreSubtitle.textContent = summaryText;
        }

        // 3. Build Detailed Question Breakdown & Answer Review
        const breakdownHtml = `
            <div style="display: flex; justify-content: center; gap: 0.75rem; margin: 1.25rem 0; flex-wrap: wrap;">
                <div class="test-stat-chip" style="color: #065f46; background: #ecfdf5; border: 1px solid #a7f3d0; font-weight: 700; padding: 0.4rem 0.9rem; border-radius: 999px;">
                    <i class="fas fa-check-circle"></i> ${isHi ? 'सही' : 'Correct'}: ${correct} (+${correct * 3})
                </div>
                <div class="test-stat-chip" style="color: #991b1b; background: #fef2f2; border: 1px solid #fecaca; font-weight: 700; padding: 0.4rem 0.9rem; border-radius: 999px;">
                    <i class="fas fa-times-circle"></i> ${isHi ? 'गलत' : 'Incorrect'}: ${incorrect} (-${incorrect * 1})
                </div>
                <div class="test-stat-chip" style="color: #475569; background: #f8fafc; border: 1px solid var(--border-subtle); font-weight: 700; padding: 0.4rem 0.9rem; border-radius: 999px;">
                    <i class="fas fa-minus-circle"></i> ${isHi ? 'अप्रयासित' : 'Unattempted'}: ${unattempted}
                </div>
                <div class="test-stat-chip" style="color: var(--brand-emerald-dark); background: var(--brand-emerald-subtle); border: 1px solid var(--brand-emerald-border); font-weight: 800; padding: 0.4rem 0.9rem; border-radius: 999px;">
                    <i class="fas fa-bullseye"></i> ${isHi ? 'शुद्धता' : 'Accuracy'}: ${accuracy}%
                </div>
            </div>

            <!-- Detailed Question Review Accordion / List -->
            <div class="mini-test-review-block" style="text-align: left; margin: 1.75rem 0 1.25rem; border-top: 1px solid var(--border-subtle); padding-top: 1.25rem;">
                <h4 style="font-family: Outfit, sans-serif; font-size: 1.15rem; font-weight: 800; color: var(--text-headline); margin: 0 0 1rem; display: flex; align-items: center; gap: 0.5rem;">
                    <i class="fas fa-clipboard-check" style="color: var(--brand-indigo);"></i>
                    <span>${isHi ? 'विस्तृत प्रश्न समीक्षा एवं व्याख्या' : 'Detailed Question Review & Explanations'}</span>
                </h4>
                <div class="test-review-list" style="display: flex; flex-direction: column; gap: 0.85rem;">
                    ${testData.map((q, qI) => {
                        const userAns = testUserAnswers[qI];
                        const isCorrect = userAns === q.correct_index;
                        const isSkipped = userAns === undefined;
                        const qT = isHi && q.question_hi ? q.question_hi : q.question;
                        const qOpts = isHi && q.options_hi && q.options_hi.length ? q.options_hi : q.options;
                        const expT = isHi && q.explanation_hi ? q.explanation_hi : q.explanation;
                        const correctOptText = qOpts[q.correct_index] || '';
                        const userOptText = !isSkipped ? qOpts[userAns] : '';
                        const statusBadge = isCorrect
                            ? `<span style="background: #ecfdf5; color: #065f46; border: 1px solid #a7f3d0; font-weight: 700; font-size: 0.76rem; padding: 0.2rem 0.55rem; border-radius: 6px;"><i class="fas fa-check"></i> +3 Correct</span>`
                            : isSkipped
                                ? `<span style="background: #f1f5f9; color: #64748b; border: 1px solid #cbd5e1; font-weight: 700; font-size: 0.76rem; padding: 0.2rem 0.55rem; border-radius: 6px;"><i class="fas fa-minus"></i> Skipped (0)</span>`
                                : `<span style="background: #fef2f2; color: #991b1b; border: 1px solid #fecaca; font-weight: 700; font-size: 0.76rem; padding: 0.2rem 0.55rem; border-radius: 6px;"><i class="fas fa-times"></i> -1 Wrong</span>`;

                        return `
                            <div style="background: var(--bg-surface); border: 1px solid ${isCorrect ? '#a7f3d0' : isSkipped ? 'var(--border-subtle)' : '#fecaca'}; border-left: 4px solid ${isCorrect ? '#10b981' : isSkipped ? '#94a3b8' : '#ef4444'}; border-radius: 10px; padding: 0.9rem 1rem; box-shadow: var(--shadow-xs);">
                                <div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 0.5rem; margin-bottom: 0.45rem;">
                                    <span style="font-weight: 800; font-size: 0.88rem; color: var(--text-headline);">Q${qI + 1}</span>
                                    ${statusBadge}
                                </div>
                                <div style="font-size: 0.93rem; font-weight: 600; color: var(--text-headline); margin-bottom: 0.65rem; line-height: 1.5;">${qT}</div>
                                <div style="font-size: 0.86rem; color: var(--text-sub); display: flex; flex-direction: column; gap: 0.25rem; margin-bottom: 0.6rem;">
                                    ${!isSkipped ? `<div><strong>${isHi ? 'आपका उत्तर' : 'Your Answer'}:</strong> <span style="color: ${isCorrect ? '#059669' : '#dc2626'}; font-weight: 700;">${['A', 'B', 'C', 'D'][userAns]}) ${userOptText}</span></div>` : `<div style="color: #64748b; font-style: italic;">${isHi ? 'आपने इस प्रश्न का उत्तर नहीं दिया' : 'You did not attempt this question'}</div>`}
                                    <div><strong>${isHi ? 'सही उत्तर' : 'Correct Answer'}:</strong> <span style="color: #059669; font-weight: 700;">${['A', 'B', 'C', 'D'][q.correct_index]}) ${correctOptText}</span></div>
                                </div>
                                ${expT ? `
                                    <div style="background: #f8fafc; border-radius: 6px; padding: 0.6rem 0.8rem; font-size: 0.86rem; color: var(--text-sub); border-left: 3px solid var(--brand-emerald); margin-top: 0.4rem; line-height: 1.55;">
                                        <strong style="color: var(--brand-emerald-dark); display: block; margin-bottom: 0.2rem;"><i class="fas fa-lightbulb"></i> ${isHi ? 'स्पष्टीकरण' : 'Explanation'}:</strong>
                                        ${expT}
                                    </div>
                                ` : ''}
                            </div>
                        `;
                    }).join('')}
                </div>
            </div>
        `;

        // Render breakdown into whichever target exists
        const breakdownTarget = document.getElementById('resultBreakdownGrid') ||
            document.getElementById('testDetailedBreakdown');

        if (breakdownTarget) {
            breakdownTarget.innerHTML = breakdownHtml;
            renderMath(breakdownTarget);
        } else if (result) {
            // For Pattern 2 or Pattern 3 where breakdownTarget is not hardcoded
            let customContainer = result.querySelector('.dynamic-test-breakdown');
            if (!customContainer) {
                customContainer = document.createElement('div');
                customContainer.className = 'dynamic-test-breakdown';
                // Insert before retake button
                const retakeBtn = result.querySelector('.retry-test-btn, .retake-test-btn, button[onclick*="resetMiniTest"], button[onclick*="restartMiniTest"]');
                if (retakeBtn) {
                    result.insertBefore(customContainer, retakeBtn);
                } else {
                    result.appendChild(customContainer);
                }
            }
            customContainer.innerHTML = breakdownHtml;
            renderMath(customContainer);
        }
    };

    window.resetMiniTest = function () {
        clearInterval(testTimerInterval);
        const intro = getTestIntroElement();
        const active = getTestActiveElement();
        const result = getTestResultElement();

        if (intro) intro.style.display = 'block';
        if (active) active.style.display = 'none';
        if (result) result.style.display = 'none';

        testCurrentIndex = 0;
        testUserAnswers = {};
        testTimeRemaining = 300;
    };

    window.restartMiniTest = window.resetMiniTest;

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

        const active = getTestActiveElement();
        if (active && active.style.display !== 'none') {
            renderTestQuestion(testCurrentIndex);
        }
        renderMath(document.body);
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

        // Initial Math Rendering
        renderMath(document.body);
    });
})();
