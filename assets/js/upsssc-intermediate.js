/**
 * upsssc-intermediate.js
 * Unified JavaScript runtime for UPSSSC Intermediate Level Mains & Micro-Topic Study Pages.
 * Inspired by UPSSSC PET Homepage UI/UX Design System.
 * SJMaths - 2026
 */

(function () {
    'use strict';

    // ── 1. Bilingual Language Switcher ──────────────────────────────────────
    window.toggleLanguageMode = window.toggleLanguage = window.toggleLang = function () {
        var current = 'en';
        try {
            current = localStorage.getItem('sjmaths_preferred_language') ||
                      localStorage.getItem('sj_pref_lang') || 'en';
        } catch (e) {}

        var newLang = (current === 'hi') ? 'en' : 'hi';
        applyLanguage(newLang);
    };

    function applyLanguage(lang) {
        var isHi = (lang === 'hi');
        var html = document.documentElement;
        var body = document.body;

        try {
            localStorage.setItem('sjmaths_preferred_language', lang);
            localStorage.setItem('sj_pref_lang', lang);
            localStorage.setItem('sjmaths_ca_lang', lang);
            localStorage.setItem('ssc-cgl-lang', lang);
        } catch (e) {}

        if (isHi) {
            html.classList.add('lang-hi', 'lang-mode-hi');
            html.classList.remove('lang-en');
            html.lang = 'hi';
            if (body) {
                body.classList.add('lang-hi', 'lang-mode-hi');
                body.classList.remove('lang-en');
            }
        } else {
            html.classList.add('lang-en');
            html.classList.remove('lang-hi', 'lang-mode-hi');
            html.lang = 'en';
            if (body) {
                body.classList.add('lang-en');
                body.classList.remove('lang-hi', 'lang-mode-hi');
            }
        }

        // Clean up inline styles so CSS rules handle display
        var hiElements = document.querySelectorAll('.lang-hi:not(.always-hi)');
        var enElements = document.querySelectorAll('.lang-en:not(.always-en)');
        if (isHi) {
            enElements.forEach(function (el) { el.style.display = 'none'; });
            hiElements.forEach(function (el) { el.style.removeProperty('display'); });
        } else {
            hiElements.forEach(function (el) { el.style.display = 'none'; });
            enElements.forEach(function (el) { el.style.removeProperty('display'); });
        }

        // Update dedicated toggle buttons if present
        var pill = document.getElementById('pageLangToggle');
        if (pill) {
            pill.setAttribute('aria-label', isHi ? 'Read in English' : 'हिंदी में पढ़ें');
        }

        var headerLangText = document.getElementById('headerLangText');
        if (headerLangText) {
            headerLangText.textContent = isHi ? 'English' : 'हिन्दी';
        }

        var btnEn = document.getElementById('langEn');
        var btnHi = document.getElementById('langHi');
        if (btnEn && btnHi) {
            btnEn.classList.toggle('active', !isHi);
            btnHi.classList.toggle('active', isHi);
            btnEn.setAttribute('aria-pressed', String(!isHi));
            btnHi.setAttribute('aria-pressed', String(isHi));
        }

        if (window.MathJax && typeof MathJax.typesetPromise === 'function') {
            MathJax.typesetPromise();
        }

        document.dispatchEvent(new CustomEvent('sjmaths:language-changed', {
            detail: { language: lang }
        }));
    }

    // ── 2. Study Tabs Navigation (3-Tab System) ─────────────────────────────
    window.switchTopicTab = window.switchTab = function (tabName) {
        if (!tabName) return;

        // Strip prefixes if user passes 'pane-notes' or 'tab-notes'
        var cleanTab = tabName.replace(/^(pane-|panel-|tab-)/, '');

        var tabBtns = document.querySelectorAll('.topic-tab-btn, .tab-btn, .sub-nav-item');
        var tabPanes = document.querySelectorAll('.topic-tab-pane, .tab-panel, .tab-content');

        tabBtns.forEach(function (btn) {
            var target = btn.getAttribute('data-tab') || btn.getAttribute('data-target') || '';
            var onClickAttr = btn.getAttribute('onclick') || '';
            var isMatch = (target === cleanTab || target === tabName || onClickAttr.indexOf("'" + cleanTab + "'") !== -1 || onClickAttr.indexOf('"' + cleanTab + '"') !== -1);

            if (isMatch) {
                btn.classList.add('active');
                btn.setAttribute('aria-selected', 'true');
            } else {
                btn.classList.remove('active');
                btn.setAttribute('aria-selected', 'false');
            }
        });

        tabPanes.forEach(function (pane) {
            var isMatchPane = (
                pane.id === cleanTab ||
                pane.id === tabName ||
                pane.id === ('pane-' + cleanTab) ||
                pane.id === ('panel-' + cleanTab) ||
                pane.id === ('tab-' + cleanTab)
            );

            if (isMatchPane) {
                pane.classList.add('active');
                pane.removeAttribute('hidden');
                pane.style.display = 'block';
            } else {
                pane.classList.remove('active');
                pane.setAttribute('hidden', '');
                pane.style.display = 'none';
            }
        });

        // Auto-start mini test timer if switching to Mini Test tab
        if ((cleanTab === 'test' || cleanTab === 'mini-test') && !window.miniTestTimerStarted) {
            startMiniTestTimer();
        }

        try {
            sessionStorage.setItem('upsssc_active_tab', cleanTab);
        } catch (e) {}

        if (window.MathJax && typeof MathJax.typesetPromise === 'function') {
            MathJax.typesetPromise();
        }
    };

    // ── 3. Tab 2: 30 Revision Practice Questions Engine ─────────────────────
    window.checkAnswer = function (btn, correctOpt, qNum) {
        var card = btn.closest('.question-card') || btn.closest('.practice-question');
        if (!card) return;

        // Prevent multiple answers
        if (card.getAttribute('data-answered') === 'true') return;
        card.setAttribute('data-answered', 'true');

        var selectedOpt = btn.getAttribute('data-opt');
        var options = card.querySelectorAll('.opt-btn, .option-item');

        options.forEach(function (optBtn) {
            var optLetter = optBtn.getAttribute('data-opt');
            if (optLetter === correctOpt) {
                optBtn.classList.add('correct');
            } else if (optBtn === btn && selectedOpt !== correctOpt) {
                optBtn.classList.add('wrong', 'incorrect');
            }
            optBtn.disabled = true;
        });

        var solBox = card.querySelector('.solution-box');
        if (solBox) {
            solBox.style.display = 'block';
            solBox.classList.add('active');
        }

        updateQuizScoreTracker();
    };

    function updateQuizScoreTracker() {
        var answeredCards = document.querySelectorAll('.question-card[data-answered="true"]').length;
        var totalCards = document.querySelectorAll('.question-card').length;
        var badge = document.getElementById('quizAnsweredBadge');
        if (badge && totalCards > 0) {
            badge.textContent = answeredCards + '/' + totalCards;
        }
    }

    // ── 4. Tab 3: 15-Question Timed Mini Test Engine ────────────────────────
    var TEST_DURATION_SECONDS = 15 * 60; // 15 Minutes
    var timeRemaining = TEST_DURATION_SECONDS;
    var timerInterval = null;
    window.miniTestTimerStarted = false;
    window.miniTestSubmitted = false;

    function startMiniTestTimer() {
        if (window.miniTestTimerStarted || window.miniTestSubmitted) return;
        window.miniTestTimerStarted = true;

        var timerEl = document.getElementById('testTimerDisplay') || document.getElementById('testTimer') || document.getElementById('tmr-display');
        if (!timerEl) return;

        timerInterval = setInterval(function () {
            timeRemaining--;
            if (timeRemaining <= 0) {
                clearInterval(timerInterval);
                timeRemaining = 0;
                updateTimerDisplay(timerEl, 0);
                window.submitMiniTest(true);
            } else {
                updateTimerDisplay(timerEl, timeRemaining);
            }
        }, 1000);
    }

    function updateTimerDisplay(el, seconds) {
        var mins = Math.floor(seconds / 60);
        var secs = seconds % 60;
        var formatted = (mins < 10 ? '0' : '') + mins + ':' + (secs < 10 ? '0' : '') + secs;
        el.textContent = formatted;

        var badge = el.closest('.test-timer-badge') || el.closest('.test-timer');
        if (badge) {
            if (seconds <= 180) {
                badge.classList.add('urgent');
            } else {
                badge.classList.remove('urgent');
            }
        }
    }

    window.submitMiniTest = window.submitTest = function (isAutoSubmit) {
        if (window.miniTestSubmitted) return;
        window.miniTestSubmitted = true;

        if (timerInterval) clearInterval(timerInterval);

        var testData = window.upssscTestData || [];
        var totalQ = (testData.length > 0) ? testData.length : 15;
        var correctCount = 0;
        var wrongCount = 0;
        var skippedCount = 0;

        for (var i = 0; i < totalQ; i++) {
            var qBox = document.getElementById('tq-' + i);
            var selectedRadio = (qBox ? qBox.querySelector('input[type="radio"]:checked') : null) ||
                                document.querySelector('input[name="tq-' + i + '"]:checked') ||
                                document.querySelector('input[name="tq_' + i + '"]:checked') ||
                                document.querySelector('input[name="tq_ans_' + i + '"]:checked') ||
                                document.querySelector('input[name="tq_opt_' + i + '"]:checked') ||
                                document.querySelector('input[name="q' + (i + 1) + '"]:checked');
            var correctOpt = (testData[i] && testData[i].ans) ? testData[i].ans : null;

            // Fallback from DOM data-ans attribute
            if (!correctOpt && qBox) {
                correctOpt = qBox.getAttribute('data-ans');
            }

            if (!selectedRadio) {
                skippedCount++;
            } else {
                var selectedVal = selectedRadio.value;
                if (selectedVal === correctOpt) {
                    correctCount++;
                    if (qBox) {
                        var lbl = selectedRadio.closest('.tq-opt-label') || selectedRadio.closest('.test-opt');
                        if (lbl) lbl.classList.add('chosen-correct', 'ok', 'correct-option');
                    }
                } else {
                    wrongCount++;
                    if (qBox) {
                        var lblWrong = selectedRadio.closest('.tq-opt-label') || selectedRadio.closest('.test-opt');
                        if (lblWrong) lblWrong.classList.add('chosen-wrong', 'bad', 'incorrect-option');
                    }
                }
            }

            // Disable all radio inputs
            if (qBox) {
                var inputs = qBox.querySelectorAll('input[type="radio"]');
                inputs.forEach(function (inp) { inp.disabled = true; });
            }
        }

        // UPSSSC Negative Marking: +1 for correct, -0.25 for wrong
        var netScore = Math.max(0, (correctCount * 1.0) - (wrongCount * 0.25));
        var accuracy = (correctCount + wrongCount > 0)
            ? Math.round((correctCount / (correctCount + wrongCount)) * 100)
            : 0;

        // Render Scorecard
        var scorecard = document.getElementById('testScorecard') || document.getElementById('test-result');
        var submitBtn = document.getElementById('submitTestBtn') || document.getElementById('submit-btn') || document.getElementById('bottom-submit-btn');
        if (submitBtn) submitBtn.style.display = 'none';

        if (scorecard) {
            scorecard.style.display = 'block';

            var scoreValEl = document.getElementById('scoreValue') || document.getElementById('res-score');
            if (scoreValEl) {
                scoreValEl.textContent = (Number.isInteger(netScore) ? netScore : netScore.toFixed(2)) + ' / ' + totalQ;
            }

            var feedbackEl = document.getElementById('scoreFeedback');
            if (feedbackEl) {
                if (accuracy >= 80) feedbackEl.textContent = 'Excellent Performance! ★★★';
                else if (accuracy >= 60) feedbackEl.textContent = 'Good Effort! ★★';
                else if (accuracy >= 40) feedbackEl.textContent = 'Average Score ★';
                else feedbackEl.textContent = 'Needs Improvement. Revise Notes!';
            }

            var breakdownEl = document.getElementById('scoreBreakdown');
            if (breakdownEl) {
                breakdownEl.textContent = 'Correct: ' + correctCount + ' | Incorrect: ' + wrongCount + ' | Skipped: ' + skippedCount + ' (Accuracy: ' + accuracy + '%)';
            }

            var correctEl = document.getElementById('statCorrect');
            if (correctEl) correctEl.textContent = correctCount;

            var wrongEl = document.getElementById('statWrong');
            if (wrongEl) wrongEl.textContent = wrongCount;

            var skippedEl = document.getElementById('statSkipped');
            if (skippedEl) skippedEl.textContent = skippedCount;

            var accuracyEl = document.getElementById('statAccuracy');
            if (accuracyEl) accuracyEl.textContent = accuracy + '%';

            scorecard.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }
    };

    window.reviewTestAnswers = function () {
        var testData = window.upssscTestData || [];
        var totalQ = (testData.length > 0) ? testData.length : 15;

        for (var i = 0; i < totalQ; i++) {
            var qBox = document.getElementById('tq-' + i);
            if (!qBox) continue;

            var correctOpt = (testData[i] && testData[i].ans) ? testData[i].ans : qBox.getAttribute('data-ans');
            if (correctOpt) {
                var correctLabel = qBox.querySelector('.tq-opt-label[data-opt="' + correctOpt + '"]') ||
                                   qBox.querySelector('input[value="' + correctOpt + '"]')?.closest('.tq-opt-label') ||
                                   qBox.querySelector('.test-opt[data-ch="' + correctOpt + '"]');
                if (correctLabel) {
                    correctLabel.classList.add('correct-answer-highlight', 'ok', 'correct-option');
                }
            }

            var solBox = qBox.querySelector('.test-solution-box') || qBox.querySelector('.sol-box') || qBox.querySelector('.solution-box');
            if (solBox) {
                solBox.style.display = 'block';
                solBox.classList.add('active');
            }
        }

        var firstQ = document.getElementById('tq-0');
        if (firstQ) firstQ.scrollIntoView({ behavior: 'smooth', block: 'start' });
    };

    window.resetMiniTest = window.retakeTest = function () {
        window.miniTestSubmitted = false;
        window.miniTestTimerStarted = false;
        timeRemaining = TEST_DURATION_SECONDS;

        var timerEl = document.getElementById('testTimerDisplay') || document.getElementById('testTimer') || document.getElementById('tmr-display');
        if (timerEl) updateTimerDisplay(timerEl, TEST_DURATION_SECONDS);

        var totalQ = 15;
        for (var i = 0; i < totalQ; i++) {
            var qBox = document.getElementById('tq-' + i);
            if (!qBox) continue;

            var inputs = qBox.querySelectorAll('input[type="radio"]');
            inputs.forEach(function (inp) {
                inp.disabled = false;
                inp.checked = false;
            });

            var labels = qBox.querySelectorAll('.tq-opt-label, .test-opt');
            labels.forEach(function (lbl) {
                lbl.classList.remove('chosen-correct', 'chosen-wrong', 'correct-answer-highlight', 'ok', 'bad', 'correct-option', 'incorrect-option');
            });

            var solBox = qBox.querySelector('.test-solution-box') || qBox.querySelector('.sol-box') || qBox.querySelector('.solution-box');
            if (solBox) {
                solBox.style.display = 'none';
                solBox.classList.remove('active');
            }
        }

        var scorecard = document.getElementById('testScorecard') || document.getElementById('test-result');
        if (scorecard) scorecard.style.display = 'none';

        var submitBtn = document.getElementById('submitTestBtn') || document.getElementById('submit-btn') || document.getElementById('bottom-submit-btn');
        if (submitBtn) submitBtn.style.display = 'inline-flex';

        startMiniTestTimer();
    };

    // ── 5. Syllabus Checkbox Progress Tracker ───────────────────────────────
    function getStoredProgress() {
        try {
            return JSON.parse(localStorage.getItem('upsssc_intermediate_progress') || '{}');
        } catch (e) {
            return {};
        }
    }

    function saveProgress(data) {
        try {
            localStorage.setItem('upsssc_intermediate_progress', JSON.stringify(data));
        } catch (e) {}
    }

    function updateSyllabusProgress() {
        var checkboxes = document.querySelectorAll('.syllabus-checkbox');
        if (checkboxes.length === 0) return;

        var stored = getStoredProgress();
        var checkedCount = 0;

        checkboxes.forEach(function (cb) {
            if (stored[cb.id]) {
                cb.checked = true;
                checkedCount++;
            }
        });

        // Update overall percentage
        var percent = Math.round((checkedCount / checkboxes.length) * 100);
        var bar = document.getElementById('syllabusProgressBar');
        if (bar) bar.style.width = percent + '%';

        var percentText = document.getElementById('syllabusProgressPercent');
        if (percentText) percentText.textContent = percent + '%';

        // Update parts badges
        ['part1', 'part2', 'part3'].forEach(function (partKey) {
            var panel = document.getElementById('panel-' + partKey);
            if (panel) {
                var pBoxes = panel.querySelectorAll('.syllabus-checkbox');
                var pChecked = 0;
                pBoxes.forEach(function (b) { if (stored[b.id]) pChecked++; });
                var pBadge = document.getElementById('badge-' + partKey);
                if (pBadge && pBoxes.length > 0) {
                    var pPct = Math.round((pChecked / pBoxes.length) * 100);
                    pBadge.textContent = '(' + pPct + '%)';
                }
            }
        });

        // Update subsection counters
        document.querySelectorAll('.syllabus-subsection').forEach(function (section) {
            var secBoxes = section.querySelectorAll('.syllabus-checkbox');
            var progSpan = section.querySelector('.subsection-progress');
            if (progSpan && secBoxes.length > 0) {
                var sChecked = 0;
                secBoxes.forEach(function (b) { if (stored[b.id]) sChecked++; });
                progSpan.textContent = sChecked + '/' + secBoxes.length;
            }
        });
    }

    function initSyllabusTracker() {
        var checkboxes = document.querySelectorAll('.syllabus-checkbox');
        if (checkboxes.length === 0) return;

        var stored = getStoredProgress();

        checkboxes.forEach(function (cb) {
            if (stored[cb.id]) cb.checked = true;

            cb.addEventListener('change', function () {
                if (cb.checked) stored[cb.id] = true;
                else delete stored[cb.id];
                saveProgress(stored);
                updateSyllabusProgress();
            });

            var item = cb.closest('.syllabus-item');
            if (item) {
                item.addEventListener('click', function (e) {
                    if (e.target !== cb && !e.target.closest('a') && !e.target.closest('button')) {
                        cb.checked = !cb.checked;
                        cb.dispatchEvent(new Event('change'));
                    }
                });
            }
        });

        updateSyllabusProgress();
    }

    // ── 6. Accordion & Tab Link Behaviors ───────────────────────────────────
    window.openSubject = function (tabId, subjectId, event) {
        if (event && event.preventDefault) event.preventDefault();
        window.switchTopicTab(tabId);
        var subject = document.getElementById(subjectId);
        if (subject) {
            var subsection = subject.querySelector('.syllabus-subsection');
            if (subsection) subsection.open = true;
            subject.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    };

    // ── 7. DOM Ready Initialization ─────────────────────────────────────────
    function init() {
        // 1. Language Initialization
        var pref = 'en';
        try {
            pref = localStorage.getItem('sjmaths_preferred_language') ||
                   localStorage.getItem('sj_pref_lang') || 'en';
        } catch (e) {}
        applyLanguage(pref);

        // 2. Setup Tab Button Click Listeners
        document.querySelectorAll('.topic-tab-btn, .syllabus-tabs .tab-btn').forEach(function (btn) {
            btn.addEventListener('click', function (e) {
                var target = btn.getAttribute('data-tab') || btn.getAttribute('data-target');
                if (target) {
                    e.preventDefault();
                    window.switchTopicTab(target);
                }
            });
        });

        // 3. Initialize Checkbox Tracker
        initSyllabusTracker();

        // 4. Handle URL Hashes (e.g. #tab-practice, #tab-mini-test, #subj-hist)
        if (window.location.hash) {
            var hash = window.location.hash.substring(1);
            if (hash.startsWith('tab-') || hash === 'part1' || hash === 'part2' || hash === 'part3' || hash === 'notes' || hash === 'quiz' || hash === 'test') {
                window.switchTopicTab(hash);
            } else {
                var targetEl = document.getElementById(hash);
                if (targetEl) {
                    var panel = targetEl.closest('.tab-panel, .topic-tab-pane');
                    if (panel && panel.id) {
                        var panelTab = panel.id.replace('panel-', '').replace('pane-', '');
                        window.switchTopicTab(panelTab);
                    }
                    var details = targetEl.querySelector('details') || targetEl.closest('details');
                    if (details) details.open = true;
                    setTimeout(function () {
                        targetEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
                    }, 150);
                }
            }
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
