/* ==========================================================================
   SJMaths — Class 11 Chemistry Common JavaScript Engine
   Features: Tab switching, Safe MathJax queueing, Solution toggle, 
             Hash routing, Quiz engine, Test evaluation & reset
   ========================================================================== */

// Global MathJax Typeset Queue to prevent race conditions and unhandled rejections
let mathJaxQueue = Promise.resolve();
function safeTypesetMath(elements) {
    if (window.MathJax && typeof window.MathJax.typesetPromise === "function") {
        mathJaxQueue = mathJaxQueue
            .then(() => window.MathJax.typesetPromise(elements))
            .catch(err => console.warn("MathJax typeset error:", err));
        return mathJaxQueue;
    } else if (window.MathJax && window.MathJax.startup && window.MathJax.startup.promise) {
        window.MathJax.startup.promise.then(() => safeTypesetMath(elements)).catch(() => {});
    }
}
window.safeTypesetMath = safeTypesetMath;

document.addEventListener("DOMContentLoaded", function () {
    const tabs = document.querySelectorAll(".chem-tab, .science-tab, .tab");
    const panes = document.querySelectorAll(".tab-pane, .pane");
    const triggers = document.querySelectorAll("[data-go], [data-goto]");

    function activateTab(id, updateHash = true) {
        if (!id) return;

        // Guard: Verify target pane exists to prevent removing .active from all panes
        const targetPane = document.getElementById(id);
        if (!targetPane || (!targetPane.classList.contains("tab-pane") && !targetPane.classList.contains("pane"))) {
            return;
        }

        tabs.forEach(tab => {
            const tabId = tab.dataset.tab || tab.getAttribute("data-tab");
            tab.classList.toggle("active", tabId === id);
        });

        panes.forEach(pane => {
            pane.classList.toggle("active", pane.id === id);
        });

        if (updateHash) {
            history.replaceState(null, "", "#" + id);
        }

        // Re-typeset MathJax formulas safely
        safeTypesetMath();

        // Smooth scroll to top of active section/tabs
        const prefersReduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
        const tabsNav = document.querySelector(".chem-tabs, .science-tabs, .tabs");
        if (tabsNav) {
            const tabsTop = tabsNav.getBoundingClientRect().top + window.pageYOffset - 10;
            if (window.pageYOffset > tabsTop) {
                window.scrollTo({ top: Math.max(0, tabsTop), behavior: prefersReduced ? "instant" : "smooth" });
            }
        } else {
            window.scrollTo({ top: 0, behavior: prefersReduced ? "instant" : "smooth" });
        }
    }
    window.activateTab = activateTab;

    tabs.forEach(tab => {
        tab.addEventListener("click", () => {
            const target = tab.dataset.tab || tab.getAttribute("data-tab");
            activateTab(target);
        });
    });

    triggers.forEach(trigger => {
        trigger.addEventListener("click", (e) => {
            const target = trigger.dataset.go || trigger.dataset.goto || trigger.getAttribute("data-go") || trigger.getAttribute("data-goto");
            if (target) {
                e.preventDefault();
                activateTab(target);
            }
        });
    });

    // Deep-link hash navigation handling (tabs and elements)
    function openChapterHash() {
        let hash;
        try {
            hash = decodeURIComponent(location.hash.slice(1));
        } catch {
            return;
        }
        if (!hash) return;

        // 1. Direct tab navigation
        const targetTab = document.querySelector(`.chem-tab[data-tab="${hash}"], .science-tab[data-tab="${hash}"], .tab[data-tab="${hash}"]`);
        if (targetTab) {
            activateTab(hash, false);
            return;
        }

        // 2. Element anchor navigation inside a tab pane
        const el = document.getElementById(hash);
        if (!el) return;

        const pane = el.closest(".tab-pane, .pane") || (el.classList.contains("tab-pane") || el.classList.contains("pane") ? el : null);
        if (pane) {
            activateTab(pane.id, false);
            const prefersReduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
            setTimeout(() => {
                el.scrollIntoView({ block: "start", behavior: prefersReduced ? "instant" : "smooth" });
            }, 80);
        }
    }
    window.openChapterHash = openChapterHash;

    window.addEventListener("hashchange", openChapterHash);
    if (location.hash) {
        openChapterHash();
    }

    function initInjectedMobileNavigation(root) {
        const mobileToggle = root.querySelector(".mobile-toggle");
        const navMenu = root.querySelector("#primary-navigation") || root.querySelector(".desktop-nav");
        if (!mobileToggle || !navMenu || mobileToggle.dataset.sjMobileBound === "true") return;

        mobileToggle.dataset.sjMobileBound = "true";

        const setMobileNavState = (isOpen) => {
            navMenu.classList.toggle("active", isOpen);
            mobileToggle.setAttribute("aria-expanded", String(isOpen));
            mobileToggle.setAttribute("aria-label", isOpen ? "Close navigation menu" : "Open navigation menu");
            const icon = mobileToggle.querySelector("i");
            if (icon) icon.className = isOpen ? "fas fa-times" : "fas fa-bars";
        };

        mobileToggle.addEventListener("click", (event) => {
            event.stopPropagation();
            setMobileNavState(!navMenu.classList.contains("active"));
        });

        document.addEventListener("keydown", (event) => {
            if (event.key === "Escape" && navMenu.classList.contains("active")) {
                setMobileNavState(false);
                mobileToggle.focus();
            }
        });

        document.addEventListener("click", (event) => {
            if (!navMenu.classList.contains("active")) return;
            if (navMenu.contains(event.target) || mobileToggle.contains(event.target)) return;
            setMobileNavState(false);
        });
    }

    // Dynamic header/footer loader
    async function loadComponent(id, url) {
        const target = document.getElementById(id);
        if (!target) return;
        if (id === "header-container" && document.getElementById("site-header")) return;
        if (id === "footer-container" && document.getElementById("site-footer")) return;
        try {
            const response = await fetch(url);
            if (response.ok) {
                const html = await response.text();
                if (id === "header-container" && document.getElementById("site-header")) return;
                if (id === "footer-container" && document.getElementById("site-footer")) return;
                target.style.opacity = "0";
                target.style.transition = "opacity 0.4s ease";
                target.innerHTML = html;
                target.offsetHeight; 
                target.style.opacity = "1";
                if (id === "header-container") initInjectedMobileNavigation(target);
                document.dispatchEvent(new CustomEvent("sjmaths:component-loaded", {
                    detail: { id, target }
                }));
            }
        } catch (error) {
            console.warn("Component could not be loaded:", url);
        }
    }

    loadComponent("header-container", "/components/header.html");
    loadComponent("footer-container", "/components/footer.html");

    // Initialize Interactive Quiz & Test Engine
    initQuizEngine();
});

// Interactive Solution Toggle Helper
window.toggleSolution = function (btn) {
    let box = btn.nextElementSibling;
    while (box && !box.classList.contains("solution-box")) {
        box = box.nextElementSibling;
    }
    if (!box) {
        box = btn.closest(".q-card, .question-card, .chem-card")?.querySelector(".solution-box");
    }
    if (!box) return;

    const isVisible = box.style.display === "block";
    if (isVisible) {
        box.style.display = "none";
        btn.classList.remove("active");
        btn.innerHTML = '<i class="fas fa-eye"></i> Show Solution';
    } else {
        box.style.display = "block";
        box.style.opacity = "0";
        box.style.transition = "opacity 0.25s ease";
        box.offsetHeight;
        box.style.opacity = "1";
        btn.classList.add("active");
        btn.innerHTML = '<i class="fas fa-eye-slash"></i> Hide Solution';
        safeTypesetMath([box]);
    }
};

// Reset Active Test Function
function resetActiveTest(scope) {
    if (!scope) scope = document;
    const cards = scope.querySelectorAll(".quiz-card");
    cards.forEach(card => {
        delete card.dataset.answered;
        delete card.dataset.userCorrect;
        const opts = card.querySelectorAll(".quiz-opt");
        opts.forEach(opt => opt.classList.remove("selected", "correct", "wrong"));
        const explains = card.querySelectorAll(".opt-explain");
        explains.forEach(exp => exp.classList.remove("show", "is-correct", "is-wrong"));
    });
    const resultContainer = scope.querySelector(".quiz-result") || (scope.classList.contains("quiz-result") ? scope : null);
    if (resultContainer) {
        resultContainer.style.display = "none";
        const scoreDisplay = resultContainer.querySelector(".quiz-score-num");
        if (scoreDisplay) scoreDisplay.textContent = `0 / ${cards.length}`;
        const feedbackText = resultContainer.querySelector(".quiz-feedback");
        if (feedbackText) feedbackText.textContent = "";
    }
}
window.resetActiveTest = resetActiveTest;

// Interactive Quiz & 3-Level Test Engine
function initQuizEngine() {
    const quizCards = document.querySelectorAll(".quiz-card");
    
    quizCards.forEach(card => {
        const options = card.querySelectorAll(".quiz-opt");
        options.forEach(opt => {
            opt.addEventListener("click", () => {
                if (card.dataset.answered === "true") return;

                const isQuizTab = card.closest("#quiz") !== null;
                const correctLetter = (card.dataset.correct || "").toUpperCase();
                const selectedLetter = (opt.dataset.opt || "").toUpperCase();

                if (isQuizTab) {
                    // Answers show immediately after selecting options in Quiz tab
                    card.dataset.answered = "true";
                    card.dataset.userCorrect = (selectedLetter === correctLetter) ? "true" : "false";

                    const wraps = card.querySelectorAll(".quiz-opt-wrap");
                    if (wraps.length > 0) {
                        wraps.forEach(wrap => {
                            const o = wrap.querySelector(".quiz-opt");
                            const exp = wrap.querySelector(".opt-explain");
                            const oLet = (o?.dataset.opt || "").toUpperCase();

                            if (oLet === correctLetter) {
                                o?.classList.add("correct");
                                if (exp) {
                                    exp.classList.add("show", "is-correct");
                                }
                            } else {
                                if (oLet === selectedLetter) {
                                    o?.classList.add("wrong");
                                }
                                if (exp) {
                                    exp.classList.add("show", "is-wrong");
                                }
                            }
                        });

                        safeTypesetMath(card.querySelectorAll(".opt-explain"));
                    } else {
                        // Fallback if no wraps
                        options.forEach(o => {
                            const oLet = (o.dataset.opt || "").toUpperCase();
                            if (oLet === correctLetter) {
                                o.classList.add("correct");
                            } else if (o === opt && selectedLetter !== correctLetter) {
                                o.classList.add("wrong");
                            }
                        });
                    }

                    // Dynamically update live quiz score tracker if present
                    updateQuizScore(card.closest(".tab-pane, section"));
                } else {
                    // For test cards, select option and allow reviewing before submit
                    options.forEach(o => o.classList.remove("selected"));
                    opt.classList.add("selected");
                }
            });
        });
    });

    function updateQuizScore(scope) {
        if (!scope) return;
        const cards = scope.querySelectorAll(".quiz-card");
        let answered = 0;
        let score = 0;
        cards.forEach(c => {
            if (c.dataset.answered === "true") {
                answered++;
                if (c.dataset.userCorrect === "true") {
                    score++;
                }
            }
        });
        const resultContainer = scope.querySelector(".quiz-result");
        if (resultContainer) {
            resultContainer.style.display = "block";
            const scoreDisplay = resultContainer.querySelector(".quiz-score-num");
            if (scoreDisplay) {
                scoreDisplay.textContent = `${score} / ${cards.length}`;
            }
            const feedbackText = resultContainer.querySelector(".quiz-feedback");
            if (feedbackText) {
                const pct = cards.length > 0 ? Math.round((score / cards.length) * 100) : 0;
                feedbackText.textContent = `Completed ${answered} of ${cards.length} • Score: ${pct}% (${score} correct)`;
            }
        }
    }

    // Submit Test Handler
    const submitBtns = document.querySelectorAll(".quiz-submit-btn");
    submitBtns.forEach(submitBtn => {
        submitBtn.addEventListener("click", () => {
            const scope = submitBtn.closest(".quiz-group, .test-level-pane, .concept-card, .tab-pane") || document;
            const cardsInScope = scope.querySelectorAll(".quiz-card");
            let score = 0;
            let total = cardsInScope.length;

            cardsInScope.forEach(card => {
                card.dataset.answered = "true";
                const correctLetter = (card.dataset.correct || "").toUpperCase();
                const selectedOpt = card.querySelector(".quiz-opt.selected");
                const selectedLetter = selectedOpt ? (selectedOpt.dataset.opt || "").toUpperCase() : null;

                const wraps = card.querySelectorAll(".quiz-opt-wrap");
                if (wraps.length > 0) {
                    wraps.forEach(wrap => {
                        const o = wrap.querySelector(".quiz-opt");
                        const exp = wrap.querySelector(".opt-explain");
                        const oLet = (o?.dataset.opt || "").toUpperCase();

                        if (oLet === correctLetter) {
                            o?.classList.add("correct");
                            if (exp) {
                                exp.classList.add("show", "is-correct");
                            }
                        } else {
                            if (oLet === selectedLetter) {
                                o?.classList.add("wrong");
                            }
                            if (exp) {
                                exp.classList.add("show", "is-wrong");
                            }
                        }
                    });

                    safeTypesetMath(card.querySelectorAll(".opt-explain"));
                } else {
                    const options = card.querySelectorAll(".quiz-opt");
                    options.forEach(opt => {
                        const oLet = (opt.dataset.opt || "").toUpperCase();
                        if (oLet === correctLetter) {
                            opt.classList.add("correct");
                        } else if (opt.classList.contains("selected") && oLet !== correctLetter) {
                            opt.classList.add("wrong");
                        }
                    });
                }

                if (selectedLetter === correctLetter || card.dataset.userCorrect === "true") {
                    score++;
                }
            });

            const resultContainer = scope.querySelector(".quiz-result") || document.querySelector(".quiz-result");
            if (resultContainer) {
                resultContainer.style.display = "block";
                const scoreDisplay = resultContainer.querySelector(".quiz-score-num");
                if (scoreDisplay) {
                    scoreDisplay.textContent = `${score} / ${total}`;
                }
                const feedbackText = resultContainer.querySelector(".quiz-feedback");
                if (feedbackText) {
                    const pct = total > 0 ? Math.round((score / total) * 100) : 0;
                    feedbackText.textContent = `Score: ${pct}% • ${score} correct out of ${total}`;
                }
                resultContainer.scrollIntoView({ behavior: "smooth", block: "nearest" });
            }
        });
    });

    // Reset Test Handler
    const resetBtns = document.querySelectorAll(".quiz-reset-btn");
    resetBtns.forEach(resetBtn => {
        resetBtn.addEventListener("click", () => {
            const scope = resetBtn.closest(".quiz-group, .test-level-pane, .concept-card, .tab-pane") || document;
            resetActiveTest(scope);
        });
    });

    // Sub-level test tab switcher inside Tests tab
    const levelTabs = document.querySelectorAll(".test-level-tab");
    const levelPanes = document.querySelectorAll(".test-level-pane");
    levelTabs.forEach(lt => {
        lt.addEventListener("click", () => {
            const targetLevel = lt.dataset.level;
            levelTabs.forEach(t => t.classList.toggle("active", t.dataset.level === targetLevel));
            levelPanes.forEach(p => p.classList.toggle("active", p.id === targetLevel));
            safeTypesetMath();
        });
    });
}
