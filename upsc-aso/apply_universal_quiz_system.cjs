const fs = require('fs');
const path = require('path');

const QUIZ_ENGINE_SCRIPT = `
<!-- UNIVERSAL INTERACTIVE QUIZ & TEST FEEDBACK SYSTEM -->
<script id="universal-quiz-feedback">
(function() {
    function getScopedVar(name) {
        try {
            if (typeof window !== 'undefined' && window[name] !== undefined) return window[name];
        } catch(e) {}
        try {
            return eval('typeof ' + name + ' !== "undefined" ? ' + name + ' : undefined');
        } catch(e) {}
        return undefined;
    }

    function normalizeAns(val) {
        if (val === undefined || val === null) return -1;
        if (typeof val === 'number') return val;
        const str = String(val).trim().toUpperCase();
        if (str === 'A') return 0;
        if (str === 'B') return 1;
        if (str === 'C') return 2;
        if (str === 'D') return 3;
        const num = parseInt(str, 10);
        return isNaN(num) ? -1 : num;
    }

    function handleOptionInteraction(target) {
        const optionEl = target.closest('label, .option-item, .quiz-opt-btn, .quiz-option, .quiz-opt-label, .quiz-choice, [data-option]');
        if (!optionEl) return;

        const card = optionEl.closest('.quiz-card, .quiz-item, .test-card, .concept-card, [id^="qc-"], [id^="q-card-"], [id^="q-block-"], [id^="q-box-"], [id^="card-q-"], [id^="l1-card-"], [id^="l2-card-"], [data-question], [data-qid], [data-q]') || optionEl.parentElement?.parentElement;
        if (!card) return;

        let allOptions = Array.from(card.querySelectorAll('label, .option-item, .quiz-opt-btn, .quiz-option, .quiz-opt-label, .quiz-choice, [data-option]'));
        if (allOptions.length === 0 && card.parentElement) {
            allOptions = Array.from(card.parentElement.querySelectorAll('label, .option-item, .quiz-opt-btn, .quiz-option'));
        }

        const radio = optionEl.querySelector('input[type="radio"]') || (target.tagName === 'INPUT' ? target : null);
        let selectedIdx = allOptions.indexOf(optionEl);
        if (radio && radio.value !== undefined) {
            const valIdx = normalizeAns(radio.value);
            if (valIdx !== -1) selectedIdx = valIdx;
        }

        if (selectedIdx === -1 && !radio) return;
        if (radio) radio.checked = true;

        const rName = radio?.name || card.querySelector('input[type="radio"]')?.name || '';
        const l1Match = rName.match(/(?:l1|t1|test1)[-_]?q?(\d+)/i) || (card.id && card.id.match(/(?:l1|t1)[-_]?card[-_]?(\d+)/i));
        const l2Match = rName.match(/(?:l2|t2|test2)[-_]?q?(\d+)/i) || (card.id && card.id.match(/(?:l2|t2)[-_]?card[-_]?(\d+)/i));
        const qMatch = rName.match(/(?:q|quiz)[-_]?(\d+)/i) || (card.id && card.id.match(/(?:qc|q|card|q-block|q-box)[-_]?(\d+)/i));

        let qNum = -1;
        if (l1Match) qNum = parseInt(l1Match[1], 10);
        else if (l2Match) qNum = parseInt(l2Match[1], 10);
        else if (qMatch) qNum = parseInt(qMatch[1], 10);
        else if (card.getAttribute('data-q') || card.getAttribute('data-qid') || card.getAttribute('data-question')) {
            qNum = parseInt(card.getAttribute('data-q') || card.getAttribute('data-qid') || card.getAttribute('data-question'), 10);
        }

        let correctIdx = -1;
        let explanationText = '';

        // 1. Direct attribute on card or option
        if (card.getAttribute('data-answer') || card.getAttribute('data-correct')) {
            correctIdx = normalizeAns(card.getAttribute('data-answer') || card.getAttribute('data-correct'));
        }

        // 2. Check if an option has data-correct or true onclick
        if (correctIdx === -1) {
            allOptions.forEach((opt, idx) => {
                if (opt.getAttribute('data-correct') === 'true' || opt.classList.contains('correct-answer') || (opt.getAttribute('onclick') && /,\s*true\s*\)/i.test(opt.getAttribute('onclick')))) {
                    correctIdx = idx;
                }
            });
        }

        // 3. Button onclick checkAnswer / verifyQuizAns in card
        if (correctIdx === -1) {
            const btn = card.querySelector('button[onclick*="Ans"], button[onclick*="Answer"], button[onclick*="Check"], button[onclick*="verify"]');
            if (btn) {
                const m = btn.getAttribute('onclick').match(/['"]([A-D])['"]/i);
                if (m) correctIdx = normalizeAns(m[1]);
            }
        }

        // 4. quizAnswers / answers dictionary map
        if (correctIdx === -1) {
            const ansMap = getScopedVar('quizAnswers') || getScopedVar('answers');
            if (ansMap) {
                const val = ansMap[rName] || ansMap['q' + qNum] || ansMap[String(qNum)];
                if (val !== undefined) {
                    if (typeof val === 'object' && val.correct !== undefined) {
                        correctIdx = normalizeAns(val.correct);
                        if (val.exp) explanationText = val.exp;
                    } else {
                        correctIdx = normalizeAns(val);
                    }
                }
            }
        }

        // 5. Dynamic Quiz Data
        if (correctIdx === -1 && !l1Match && !l2Match) {
            const qData = getScopedVar('quizData') || getScopedVar('quizQuestions') || getScopedVar('mcqsTab2');
            if (Array.isArray(qData)) {
                let item = qData[qNum];
                if (!item || (qNum > 0 && qData[qNum - 1])) {
                    item = qData[qNum - 1] || qData[qNum];
                }
                if (item) {
                    correctIdx = normalizeAns(item.answer !== undefined ? item.answer : (item.correct !== undefined ? item.correct : item.ans));
                    if (item.exp || item.explanation) explanationText = item.exp || item.explanation;
                }
            }
        }

        // 6. Level 1 Test Data
        if (correctIdx === -1 && l1Match) {
            const l1Data = getScopedVar('level1Data') || getScopedVar('test1Data') || getScopedVar('testDataLevel1') || getScopedVar('testLevel1Data') || getScopedVar('level1Questions') || getScopedVar('testDataL1') || getScopedVar('l1QuestionsData');
            if (Array.isArray(l1Data)) {
                let item = l1Data[qNum] || (qNum > 0 ? l1Data[qNum - 1] : null);
                if (item) {
                    correctIdx = normalizeAns(item.answer !== undefined ? item.answer : (item.correct !== undefined ? item.correct : item.ans));
                    if (item.exp || item.explanation) explanationText = item.exp || item.explanation;
                }
            }
        }

        // 7. Level 2 Test Data
        if (correctIdx === -1 && l2Match) {
            const l2Data = getScopedVar('level2Data') || getScopedVar('test2Data') || getScopedVar('testDataLevel2') || getScopedVar('testLevel2Data') || getScopedVar('level2Questions') || getScopedVar('testDataL2') || getScopedVar('l2QuestionsData');
            if (Array.isArray(l2Data)) {
                let item = l2Data[qNum] || (qNum > 0 ? l2Data[qNum - 1] : null);
                if (item) {
                    correctIdx = normalizeAns(item.answer !== undefined ? item.answer : (item.correct !== undefined ? item.correct : item.ans));
                    if (item.exp || item.explanation) explanationText = item.exp || item.explanation;
                }
            }
        }

        // 8. Text search in card / explanation
        if (correctIdx === -1) {
            const expElCheck = card.querySelector('.explanation, .quiz-explanation, .explanation-box, .quiz-exp-box, .quiz-feedback, [id*="exp"], [id*="feedback"]');
            const txt = (expElCheck ? expElCheck.textContent : card.textContent) || '';
            const match = txt.match(/Correct(?:\s+Answer|\s+Option)?:\s*([A-D])/i) || txt.match(/\(Correct:\s*([A-D])\)/i);
            if (match) {
                correctIdx = normalizeAns(match[1]);
            }
        }

        if (correctIdx === -1) return;

        const isCorrect = (selectedIdx === correctIdx);
        const correctLetter = String.fromCharCode(65 + correctIdx);

        // Highlight options
        allOptions.forEach((opt, idx) => {
            opt.classList.remove(
                'quiz-opt-correct', 'quiz-opt-incorrect', 'correct', 'incorrect',
                'border-emerald-500', 'bg-emerald-500/20', 'text-emerald-300',
                'border-rose-500', 'bg-rose-500/20', 'text-rose-300'
            );

            if (idx === correctIdx) {
                opt.classList.add('quiz-opt-correct', 'correct', 'border-emerald-500', 'bg-emerald-500/20', 'text-emerald-300', 'font-semibold');
                opt.style.setProperty('border-color', '#10b981', 'important');
                opt.style.setProperty('background-color', 'rgba(16, 185, 129, 0.22)', 'important');
                opt.style.setProperty('color', '#6ee7b7', 'important');
            } else if (idx === selectedIdx && !isCorrect) {
                opt.classList.add('quiz-opt-incorrect', 'incorrect', 'border-rose-500', 'bg-rose-500/20', 'text-rose-300');
                opt.style.setProperty('border-color', '#ef4444', 'important');
                opt.style.setProperty('background-color', 'rgba(239, 68, 68, 0.22)', 'important');
                opt.style.setProperty('color', '#fca5a5', 'important');
            } else {
                opt.style.removeProperty('border-color');
                opt.style.removeProperty('background-color');
                opt.style.removeProperty('color');
            }
        });

        // Reveal Explanation
        let expEl = card.querySelector('.explanation, .quiz-explanation, .explanation-box, .quiz-exp-box, .quiz-feedback, [id*="exp"], [id*="feedback"], [id*="fb"]');
        if (!expEl && qNum !== -1) {
            expEl = document.getElementById('q-exp-' + qNum) || 
                    document.getElementById('q-exp-' + (qNum - 1)) || 
                    document.getElementById('quiz-feedback-' + qNum) || 
                    document.getElementById('quiz-feedback-' + (qNum - 1)) || 
                    document.getElementById('q' + qNum + '-explanation') ||
                    document.getElementById('explanation-' + qNum) ||
                    document.getElementById('q' + qNum + '-feedback') ||
                    document.getElementById('fb-' + qNum) ||
                    document.getElementById('qexp-' + qNum) ||
                    document.getElementById('l1-fb-' + qNum) ||
                    document.getElementById('l2-fb-' + qNum);
        }

        if (!expEl) {
            expEl = document.createElement('div');
            expEl.className = 'quiz-feedback mt-3 p-3 rounded-lg border text-sm text-slate-200';
            card.appendChild(expEl);
        }

        if (expEl) {
            expEl.classList.remove('hidden');
            expEl.style.setProperty('display', 'block', 'important');
            expEl.classList.add('quiz-exp-revealed');

            let statusBadge = expEl.querySelector('.quiz-status-badge');
            if (!statusBadge) {
                statusBadge = document.createElement('div');
                statusBadge.className = 'quiz-status-badge font-bold mb-1.5 flex items-center gap-1.5';
                expEl.insertBefore(statusBadge, expEl.firstChild);
            }

            if (isCorrect) {
                statusBadge.innerHTML = '<span class="text-emerald-400 font-bold" style="color:#10b981;"><i class="fa-solid fa-circle-check mr-1"></i> Correct Answer!</span>';
                expEl.style.setProperty('border-color', 'rgba(16, 185, 129, 0.4)', 'important');
                expEl.style.setProperty('background-color', 'rgba(16, 185, 129, 0.08)', 'important');
            } else {
                statusBadge.innerHTML = '<span class="text-rose-400 font-bold" style="color:#ef4444;"><i class="fa-solid fa-circle-xmark mr-1"></i> Incorrect (Correct Answer: Option ' + correctLetter + ')</span>';
                expEl.style.setProperty('border-color', 'rgba(239, 68, 68, 0.4)', 'important');
                expEl.style.setProperty('background-color', 'rgba(239, 68, 68, 0.08)', 'important');
            }

            if (explanationText && (expEl.textContent.trim().length < 40 || !expEl.querySelector('.quiz-exp-content'))) {
                let contentEl = expEl.querySelector('.quiz-exp-content');
                if (!contentEl) {
                    contentEl = document.createElement('div');
                    contentEl.className = 'quiz-exp-content mt-1 text-slate-300 text-xs sm:text-sm leading-relaxed';
                    expEl.appendChild(contentEl);
                }
                contentEl.innerHTML = '<strong>Explanation:</strong> ' + explanationText;
            }

            if (window.MathJax && window.MathJax.typesetPromise) {
                window.MathJax.typesetPromise([expEl]).catch(function(){});
            }
        }
    }

    document.addEventListener('click', function(e) {
        const optionTarget = e.target.closest('label, .option-item, .quiz-opt-btn, .quiz-option, .quiz-opt-label, .quiz-choice, [data-option]');
        if (optionTarget) {
            handleOptionInteraction(optionTarget);
        }
    });

    document.addEventListener('change', function(e) {
        if (e.target.matches('input[type="radio"]')) {
            handleOptionInteraction(e.target);
        }
    });
})();
</script>
`;

const QUIZ_CSS = `
/* Universal Quiz Option Interactive States */
.quiz-opt-correct,
.option-item.correct,
.quiz-option.correct,
.quiz-opt-btn.correct,
label.quiz-opt-correct {
    border-color: #10b981 !important;
    background-color: rgba(16, 185, 129, 0.22) !important;
    color: #6ee7b7 !important;
}
.quiz-opt-incorrect,
.option-item.incorrect,
.quiz-option.incorrect,
.quiz-opt-btn.incorrect,
label.quiz-opt-incorrect {
    border-color: #ef4444 !important;
    background-color: rgba(239, 68, 68, 0.22) !important;
    color: #fca5a5 !important;
}
.quiz-exp-revealed {
    display: block !important;
    opacity: 1 !important;
    visibility: visible !important;
    animation: fadeIn 0.3s ease-out;
}
`;

async function applyQuizEnhancements() {
  const genModule = await import('./generate_gemini_study_page.mjs');
  const allDays = genModule.parseAllDays();
  const existingDays = allDays.filter(d => fs.existsSync(d.outputPath));

  console.log(`Applying Universal Quiz & Test Interactivity across ${existingDays.length} Day study modules...\n`);

  let modifiedCount = 0;

  for (const d of existingDays) {
    let html = fs.readFileSync(d.outputPath, 'utf8');

    // 0. Clean multiple </html> closures if present
    if (html.includes('</html>')) {
      const parts = html.split('</html>');
      if (parts.length > 2) {
        html = parts[0] + '</html>\n';
      }
    }

    const original = html;

    // 1. Add Quiz CSS rules if not present
    if (!html.includes('.quiz-opt-correct')) {
      if (html.includes('</style>')) {
        html = html.replace('</style>', `${QUIZ_CSS}\n    </style>`);
      } else if (html.includes('</head>')) {
        html = html.replace('</head>', `    <style>${QUIZ_CSS}</style>\n</head>`);
      }
    } else {
      // Update existing QUIZ_CSS
      html = html.replace(/\/\* (?:Universal )?Quiz Option Interactive States \*\/[\s\S]*?(?=\n\s*<\/style>)/, QUIZ_CSS.trim());
    }

    // 2. Inject or Replace universal-quiz-feedback script
    if (html.includes('id="universal-quiz-feedback"')) {
      html = html.replace(/<!-- UNIVERSAL INTERACTIVE QUIZ & TEST FEEDBACK SYSTEM -->[\s\S]*?<\/script>\s*/g, '');
      html = html.replace(/<script id="universal-quiz-feedback">[\s\S]*?<\/script>\s*/g, '');
    }
    
    // Inject right before </body> or append
    if (html.includes('</body>')) {
      html = html.replace('</body>', `${QUIZ_ENGINE_SCRIPT}\n</body>`);
    } else {
      html = html + QUIZ_ENGINE_SCRIPT;
    }

    if (html !== original) {
      fs.writeFileSync(d.outputPath, html, 'utf8');
      modifiedCount++;
      console.log(`✓ Enhanced Quiz in Day ${d.day}: ${d.topic}`);
    }
  }

  console.log(`\nSuccessfully applied Universal Quiz Interactivity to ${modifiedCount} / ${existingDays.length} pages.`);
}

applyQuizEnhancements().catch(console.error);

module.exports = { QUIZ_ENGINE_SCRIPT, QUIZ_CSS };
