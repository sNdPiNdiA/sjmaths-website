/* ==========================================================================
   SJMaths — Class 11 Chemistry Common JavaScript Engine
   Features: Tab switching, MathJax re-rendering, Solutions toggle, Quiz engine
   ========================================================================== */

document.addEventListener("DOMContentLoaded", function () {
    const tabs = document.querySelectorAll(".chem-tab, .science-tab, .tab");
    const panes = document.querySelectorAll(".tab-pane, .pane");
    const triggers = document.querySelectorAll("[data-go], [data-goto]");

    function activateTab(id, updateHash = true) {
        if (!id) return;
        
        tabs.forEach(tab => {
            const tabId = tab.dataset.tab || tab.getAttribute('data-tab');
            tab.classList.toggle("active", tabId === id);
        });

        panes.forEach(pane => {
            pane.classList.toggle("active", pane.id === id);
        });

        if (updateHash) {
            history.replaceState(null, "", "#" + id);
        }

        // Re-typeset MathJax formulas if available
        if (window.MathJax && typeof MathJax.typesetPromise === "function") {
            MathJax.typesetPromise();
        }

        // Smooth scroll to top of active section
        const activePane = document.getElementById(id);
        if (activePane) {
            const navBar = document.querySelector(".chem-tbar, .glass-header");
            const navHeight = navBar ? navBar.offsetHeight : 60;
            const topPos = activePane.getBoundingClientRect().top + window.pageYOffset - navHeight - 10;
            window.scrollTo({ top: Math.max(0, topPos), behavior: "smooth" });
        }
    }

    tabs.forEach(tab => {
        tab.addEventListener("click", () => {
            const target = tab.dataset.tab || tab.getAttribute('data-tab');
            activateTab(target);
        });
    });

    triggers.forEach(trigger => {
        trigger.addEventListener("click", (e) => {
            const target = trigger.dataset.go || trigger.dataset.goto || trigger.getAttribute('data-go') || trigger.getAttribute('data-goto');
            if (target) {
                e.preventDefault();
                activateTab(target);
            }
        });
    });

    // Hash navigation on load
    const initial = location.hash.replace("#", "");
    if (initial && document.getElementById(initial)) {
        activateTab(initial, false);
    }

    // Dynamic header/footer loader
    async function loadComponent(id, url) {
        const target = document.getElementById(id);
        if (!target) return;
        try {
            const response = await fetch(url);
            if (response.ok) {
                target.style.opacity = '0';
                target.style.transition = 'opacity 0.4s ease';
                target.innerHTML = await response.text();
                target.offsetHeight; 
                target.style.opacity = '1';
            }
        } catch (error) {
            console.warn("Component could not be loaded:", url);
        }
    }

    loadComponent("header-container", "/components/header.html");
    loadComponent("footer-container", "/components/footer.html");

    // Initialize Interactive Quiz Engine
    initQuizEngine();
});

// Interactive Solution Toggle Helper
window.toggleSolution = function (btn) {
    let box = btn.nextElementSibling;
    while (box && !box.classList.contains('solution-box')) {
        box = box.nextElementSibling;
    }
    if (!box) {
        box = btn.closest('.q-card, .question-card')?.querySelector('.solution-box');
    }
    if (!box) return;

    const isVisible = box.style.display === 'block';
    if (isVisible) {
        box.style.display = 'none';
        btn.innerHTML = '<i class="fas fa-eye"></i> Show Solution';
    } else {
        box.style.display = 'block';
        box.style.opacity = '0';
        box.style.transition = 'opacity 0.25s ease';
        box.offsetHeight;
        box.style.opacity = '1';
        btn.innerHTML = '<i class="fas fa-eye-slash"></i> Hide Solution';
        if (window.MathJax && typeof MathJax.typesetPromise === "function") {
            MathJax.typesetPromise([box]);
        }
    }
};

// Interactive Quiz & 3-Level Test Engine
function initQuizEngine() {
    const quizCards = document.querySelectorAll('.quiz-card');
    
    quizCards.forEach(card => {
        const options = card.querySelectorAll('.quiz-opt');
        options.forEach(opt => {
            opt.addEventListener('click', () => {
                if (card.dataset.answered === 'true') return;

                const isQuizTab = card.closest('#quiz') !== null;
                const correctLetter = card.dataset.correct;
                const selectedLetter = opt.dataset.opt;

                if (isQuizTab) {
                    // Answers show immediately after selecting options in Quiz tab
                    card.dataset.answered = 'true';
                    card.dataset.userCorrect = (selectedLetter === correctLetter) ? 'true' : 'false';

                    const wraps = card.querySelectorAll('.quiz-opt-wrap');
                    if (wraps.length > 0) {
                        wraps.forEach(wrap => {
                            const o = wrap.querySelector('.quiz-opt');
                            const exp = wrap.querySelector('.opt-explain');
                            const oLet = o.dataset.opt;

                            if (oLet === correctLetter) {
                                o.classList.add('correct');
                                if (exp) {
                                    exp.classList.add('show', 'is-correct');
                                }
                            } else {
                                if (oLet === selectedLetter) {
                                    o.classList.add('wrong');
                                }
                                if (exp) {
                                    exp.classList.add('show', 'is-wrong');
                                }
                            }
                        });

                        if (window.MathJax && typeof MathJax.typesetPromise === "function") {
                            MathJax.typesetPromise(card.querySelectorAll('.opt-explain'));
                        }
                    } else {
                        // Fallback if no wraps
                        options.forEach(o => {
                            if (o.dataset.opt === correctLetter) {
                                o.classList.add('correct');
                            } else if (o === opt && selectedLetter !== correctLetter) {
                                o.classList.add('wrong');
                            }
                        });
                    }

                    // Dynamically update live quiz score tracker if present
                    updateQuizScore(card.closest('.tab-pane, section'));
                } else {
                    // For test cards, select option and allow reviewing before submit
                    options.forEach(o => o.classList.remove('selected'));
                    opt.classList.add('selected');
                }
            });
        });
    });

    function updateQuizScore(scope) {
        if (!scope) return;
        const cards = scope.querySelectorAll('.quiz-card');
        let answered = 0;
        let score = 0;
        cards.forEach(c => {
            if (c.dataset.answered === 'true') {
                answered++;
                if (c.dataset.userCorrect === 'true') {
                    score++;
                }
            }
        });
        const resultContainer = scope.querySelector('.quiz-result');
        if (resultContainer) {
            resultContainer.style.display = 'block';
            const scoreDisplay = resultContainer.querySelector('.quiz-score-num');
            if (scoreDisplay) {
                scoreDisplay.textContent = `${score} / ${cards.length}`;
            }
            const feedbackText = resultContainer.querySelector('.quiz-feedback');
            if (feedbackText) {
                const pct = cards.length > 0 ? Math.round((score / cards.length) * 100) : 0;
                feedbackText.textContent = `Completed ${answered} of ${cards.length} • Score: ${pct}% (${score} correct)`;
            }
        }
    }

    const submitBtns = document.querySelectorAll('.quiz-submit-btn');
    submitBtns.forEach(submitBtn => {
        submitBtn.addEventListener('click', () => {
            const scope = submitBtn.closest('.quiz-group, .test-level-pane, .tab-pane') || document;
            const cardsInScope = scope.querySelectorAll('.quiz-card');
            let score = 0;
            let total = cardsInScope.length;

            cardsInScope.forEach(card => {
                card.dataset.answered = 'true';
                const correctLetter = card.dataset.correct;
                const selectedOpt = card.querySelector('.quiz-opt.selected');
                const selectedLetter = selectedOpt ? selectedOpt.dataset.opt : null;

                const wraps = card.querySelectorAll('.quiz-opt-wrap');
                if (wraps.length > 0) {
                    wraps.forEach(wrap => {
                        const o = wrap.querySelector('.quiz-opt');
                        const exp = wrap.querySelector('.opt-explain');
                        const oLet = o.dataset.opt;

                        if (oLet === correctLetter) {
                            o.classList.add('correct');
                            if (exp) {
                                exp.classList.add('show', 'is-correct');
                            }
                        } else {
                            if (oLet === selectedLetter) {
                                o.classList.add('wrong');
                            }
                            if (exp) {
                                exp.classList.add('show', 'is-wrong');
                            }
                        }
                    });

                    if (window.MathJax && typeof MathJax.typesetPromise === "function") {
                        MathJax.typesetPromise(card.querySelectorAll('.opt-explain'));
                    }
                } else {
                    const options = card.querySelectorAll('.quiz-opt');
                    options.forEach(opt => {
                        if (opt.dataset.opt === correctLetter) {
                            opt.classList.add('correct');
                        } else if (opt.classList.contains('selected') && opt.dataset.opt !== correctLetter) {
                            opt.classList.add('wrong');
                        }
                    });
                }

                if (selectedLetter === correctLetter || card.dataset.userCorrect === 'true') {
                    score++;
                }
            });

            const resultContainer = scope.querySelector('.quiz-result') || document.querySelector('.quiz-result');
            if (resultContainer) {
                resultContainer.style.display = 'block';
                const scoreDisplay = resultContainer.querySelector('.quiz-score-num');
                if (scoreDisplay) {
                    scoreDisplay.textContent = `${score} / ${total}`;
                }
                const feedbackText = resultContainer.querySelector('.quiz-feedback');
                if (feedbackText) {
                    const pct = total > 0 ? Math.round((score / total) * 100) : 0;
                    feedbackText.textContent = `Score: ${pct}% • ${score} correct out of ${total}`;
                }
                resultContainer.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
            }
        });
    });

    // Sub-level test tab switcher inside Tests tab
    const levelTabs = document.querySelectorAll('.test-level-tab');
    const levelPanes = document.querySelectorAll('.test-level-pane');
    levelTabs.forEach(lt => {
        lt.addEventListener('click', () => {
            const targetLevel = lt.dataset.level;
            levelTabs.forEach(t => t.classList.toggle('active', t.dataset.level === targetLevel));
            levelPanes.forEach(p => p.classList.toggle('active', p.id === targetLevel));
            if (window.MathJax && typeof MathJax.typesetPromise === "function") {
                MathJax.typesetPromise();
            }
        });
    });
}
