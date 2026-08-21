/**
 * class10-economics.js
 * Unified Client-Side Engine for Class 10 Economics Chapter & PYQ Pages
 * Handles:
 * - 5-Tab Navigation (Concepts, NCERT Exercises, PYQs, Revision, Mini Test)
 * - Routing / Deep-linking via Hash
 * - PYQ Topic Sub-Tabs & Mini Test Level Switching
 * - Unified Model Answer Reveals (.answer-btn, .answer-toggle)
 * - Interactive MCQ Activity Choice Validation (.choice, .test-option-btn)
 * - Test Submission & Reset Scoring Engines
 * - Survey / Checklist interactive calculators (Chapter 5 specific)
 * - Dynamic Next / Previous Tab Navigation Footers
 * - Back to Top & Keyboard Shortcuts
 */

(() => {
    const tabOrder = ["concepts", "ncert", "pyqs", "revision", "test"];
    const tabNames = {
        concepts: "Concepts",
        ncert: "NCERT Exercises",
        pyqs: "PYQs",
        revision: "Revision",
        test: "Mini Test"
    };

    function activateTab(id, updateHash = true) {
        const panels = document.querySelectorAll(".tab-panel");
        panels.forEach(panel => panel.classList.toggle("active", panel.id === id));

        document.querySelectorAll(".tab-btn").forEach(btn => {
            const active = btn.dataset.tab === id;
            btn.classList.toggle("active", active);
            btn.setAttribute("aria-selected", active ? "true" : "false");
        });

        const progressText = document.getElementById("progressText");
        const index = tabOrder.indexOf(id);
        if (progressText && index >= 0) {
            progressText.textContent = `${index + 1} / ${tabOrder.length}`;
        }

        if (updateHash) {
            try {
                history.replaceState(null, "", `#${id}`);
            } catch (e) {
                try { location.hash = `#${id}`; } catch (err) {}
            }
        }
        
        // Keep active tab scrolled into view inside the tab strip on mobile
        const activeBtn = document.querySelector(`.tab-btn[data-tab="${id}"]`);
        if (activeBtn) {
            activeBtn.scrollIntoView({ behavior: "smooth", block: "nearest", inline: "center" });
        }
    }

    function initTabs() {
        const tabButtons = document.querySelectorAll("[data-tab]");
        tabButtons.forEach(btn => {
            btn.addEventListener("click", () => {
                const targetTab = btn.dataset.tab;
                // If it's a standalone separate PYQ directory in some chapters and no #pyqs panel exists
                const pyqPanel = document.getElementById("pyqs");
                if (targetTab === "pyqs" && !pyqPanel) {
                    window.location.href = "previous-years-questions/";
                    return;
                }
                activateTab(targetTab);
            });
        });

        // Check if page loaded with #pyqs hash on standalone pages
        if (location.hash === "#pyqs" && !document.getElementById("pyqs")) {
            window.location.replace("previous-years-questions/");
        }

        const initial = location.hash.replace("#", "");
        if (tabOrder.includes(initial)) {
            activateTab(initial, false);
        } else {
            activateTab("concepts", false);
        }
    }

    function initSubTabs() {
        // Level switch for Mini Test
        document.querySelectorAll(".level-btn").forEach(btn => {
            btn.addEventListener("click", () => {
                const parent = btn.closest(".level-switch") || document;
                parent.querySelectorAll(".level-btn").forEach(b => b.classList.remove("active"));
                document.querySelectorAll(".test-panel").forEach(panel => panel.classList.remove("active"));
                btn.classList.add("active");
                const target = document.getElementById(btn.dataset.level);
                if (target) target.classList.add("active");
            });
        });

        // Topic switch for PYQs
        document.querySelectorAll(".pyq-topic-btn").forEach(btn => {
            btn.addEventListener("click", () => {
                const parent = btn.closest(".level-switch") || document;
                parent.querySelectorAll(".pyq-topic-btn").forEach(b => b.classList.remove("active"));
                document.querySelectorAll(".pyq-topic-panel").forEach(panel => panel.classList.remove("active"));
                btn.classList.add("active");
                const target = document.getElementById(btn.dataset.topic);
                if (target) target.classList.add("active");
            });
        });
    }

    function initAnswerToggles() {
        // Unified Answer Reveal for .answer-btn (NCERT), .answer-toggle (Revision/PYQ)
        document.querySelectorAll(".answer-btn, .answer-toggle").forEach(btn => {
            if (btn.id === "surveyBtn" || btn.id === "consciousBtn") return;
            btn.addEventListener("click", () => {
                const solution = btn.nextElementSibling || (btn.parentElement ? btn.parentElement.querySelector(".answer, .solution, .test-solution") : null);
                if (!solution) return;
                const open = solution.classList.toggle("show");
                btn.textContent = open ? "Hide answer" : "Show answer";
            });
        });
    }

    function initInteractiveChoices() {
        // Activity Choice Selection (Multiple Choice Questions)
        document.querySelectorAll(".choice").forEach(c => {
            c.addEventListener("click", () => {
                const parent = c.closest(".activity-card") || c.closest(".choice-grid") || c.parentElement;
                if (!parent) return;
                
                parent.querySelectorAll(".choice").forEach(x => x.classList.remove("correct", "wrong"));
                const isCorrect = c.dataset.answer === "correct" || c.dataset.option === "correct";
                c.classList.add(isCorrect ? "correct" : "wrong");
                
                const feedback = parent.querySelector(".feedback");
                if (feedback) {
                    feedback.textContent = isCorrect 
                        ? "✓ Correct — good application of the chapter concept."
                        : "↺ Recheck the concept and try again.";
                    feedback.style.color = isCorrect ? "#10b981" : "#ef4444";
                }
            });
        });
    }

    function initTestEngines() {
        // Mini Test Options Selection
        document.querySelectorAll(".test-options-grid").forEach(grid => {
            const buttons = grid.querySelectorAll(".test-option-btn");
            buttons.forEach(btn => {
                btn.addEventListener("click", () => {
                    if (btn.disabled) return;
                    buttons.forEach(b => b.classList.remove("selected"));
                    btn.classList.add("selected");
                });
            });
        });

        // Mini Test Submission
        document.querySelectorAll(".submit-test-btn").forEach(submitBtn => {
            submitBtn.addEventListener("click", () => {
                const levelId = submitBtn.dataset.level;
                const levelContainer = document.getElementById(levelId);
                if (!levelContainer) return;

                const cards = levelContainer.querySelectorAll(".test-card");
                let correctCount = 0;
                let totalMcq = 0;

                cards.forEach(card => {
                    const type = card.dataset.type;
                    if (type === "mcq") {
                        totalMcq++;
                        const selectedBtn = card.querySelector(".test-option-btn.selected");
                        const correctOption = card.dataset.correct;
                        const optionBtns = card.querySelectorAll(".test-option-btn");

                        optionBtns.forEach(btn => {
                            btn.disabled = true;
                            if (btn.dataset.option === correctOption) {
                                btn.classList.add("correct-ans");
                            } else if (btn.classList.contains("selected")) {
                                btn.classList.add("incorrect-ans");
                            }
                        });

                        if (selectedBtn && selectedBtn.dataset.option === correctOption) {
                            correctCount++;
                        }
                    } else if (type === "subjective") {
                        const textarea = card.querySelector(".test-textarea");
                        if (textarea) {
                            textarea.disabled = true;
                        }
                    }

                    const solution = card.querySelector(".test-solution");
                    if (solution) {
                        solution.classList.add("show");
                    }
                });

                const summary = document.getElementById(`${levelId}-summary`);
                if (summary) {
                    let feedbackHtml = "";
                    if (totalMcq > 0) {
                        feedbackHtml += `<strong>Score: ${correctCount}/${totalMcq} MCQs correct.</strong><br>`;
                    }
                    feedbackHtml += "Level submitted! Check the suggested model answers revealed below in green boxes to self-assess your answers.";
                    summary.innerHTML = feedbackHtml;
                    summary.classList.add("show");
                }

                submitBtn.style.display = "none";
                const resetBtn = levelContainer.querySelector(".reset-test-btn");
                if (resetBtn) resetBtn.style.display = "inline-block";
            });
        });

        // Mini Test Reset
        document.querySelectorAll(".reset-test-btn").forEach(resetBtn => {
            resetBtn.addEventListener("click", () => {
                const levelId = resetBtn.dataset.level;
                const levelContainer = document.getElementById(levelId);
                if (!levelContainer) return;

                const cards = levelContainer.querySelectorAll(".test-card");

                cards.forEach(card => {
                    const type = card.dataset.type;
                    if (type === "mcq") {
                        const optionBtns = card.querySelectorAll(".test-option-btn");
                        optionBtns.forEach(btn => {
                            btn.disabled = false;
                            btn.classList.remove("selected", "correct-ans", "incorrect-ans");
                        });
                    } else if (type === "subjective") {
                        const textarea = card.querySelector(".test-textarea");
                        if (textarea) {
                            textarea.disabled = false;
                            textarea.value = "";
                        }
                    }

                    const solution = card.querySelector(".test-solution");
                    if (solution) {
                        solution.classList.remove("show");
                    }
                });

                const summary = document.getElementById(`${levelId}-summary`);
                if (summary) {
                    summary.classList.remove("show");
                    summary.innerHTML = "";
                }

                resetBtn.style.display = "none";
                const submitBtn = levelContainer.querySelector(".submit-test-btn");
                if (submitBtn) submitBtn.style.display = "inline-block";
            });
        });
    }

    function initSurveyHelpers() {
        const surveyBtn = document.getElementById("surveyBtn");
        if (surveyBtn) {
            surveyBtn.addEventListener("click", () => {
                const vals = [...document.querySelectorAll(".survey-row select")].map(x => x.value).filter(Boolean);
                const yes = vals.filter(x => x === "Yes").length;
                const score = document.getElementById("surveyScore");
                if (!score) return;
                if (!vals.length) { score.textContent = "Select Yes or No for at least one question."; return; }
                const pct = Math.round(yes / vals.length * 100);
                score.textContent = `${yes} of ${vals.length} Yes responses (${pct}%). Use the result to identify areas where consumer awareness can be improved.`;
            });
        }

        const consciousBtn = document.getElementById("consciousBtn");
        if (consciousBtn) {
            consciousBtn.addEventListener("click", () => {
                const n = document.querySelectorAll(".check-item input:checked").length;
                const s = document.getElementById("consciousScore");
                if (!s) return;
                if (n >= 8) s.textContent = `${n} / 10 — Strong consumer awareness. Keep applying these habits.`;
                else if (n >= 5) s.textContent = `${n} / 10 — Developing awareness. Strengthen the practices you missed.`;
                else s.textContent = `${n} / 10 — Consumer awareness needs improvement. Review the rights and duties section.`;
            });
        }
    }

    function initDynamicTabNav() {
        tabOrder.forEach((tabId, idx) => {
            const panel = document.getElementById(tabId);
            if (!panel) return;

            const existingNav = panel.querySelector(".tab-nav-buttons");
            if (existingNav) existingNav.remove();

            const navWrapper = document.createElement("div");
            navWrapper.className = "tab-nav-buttons";

            if (idx > 0) {
                const prevTabId = tabOrder[idx - 1];
                const prevBtn = document.createElement("button");
                prevBtn.className = "btn-prev-tab";
                prevBtn.innerHTML = `← Previous: ${tabNames[prevTabId]}`;
                prevBtn.addEventListener("click", () => {
                    activateTab(prevTabId);
                    window.scrollTo({ top: 0, behavior: "smooth" });
                });
                navWrapper.appendChild(prevBtn);
            }

            if (idx < tabOrder.length - 1) {
                const nextTabId = tabOrder[idx + 1];
                const nextBtn = document.createElement("button");
                nextBtn.className = "btn-next-tab";
                nextBtn.innerHTML = `Next: ${tabNames[nextTabId]} →`;
                nextBtn.addEventListener("click", () => {
                    activateTab(nextTabId);
                    window.scrollTo({ top: 0, behavior: "smooth" });
                });
                navWrapper.appendChild(nextBtn);
            }

            panel.appendChild(navWrapper);
        });
    }

    function initGlobalListeners() {
        const backTop = document.getElementById("backTop");
        window.addEventListener("scroll", () => {
            if (backTop) backTop.classList.toggle("show", window.scrollY > 400);
        });

        if (backTop) {
            backTop.addEventListener("click", () => window.scrollTo({ top: 0, behavior: "smooth" }));
        }

        document.addEventListener("keydown", (event) => {
            if (event.key >= "1" && event.key <= "5") {
                const targetTab = tabOrder[Number(event.key) - 1];
                if (targetTab) activateTab(targetTab);
            }
        });
    }

    document.addEventListener("DOMContentLoaded", () => {
        initTabs();
        initSubTabs();
        initAnswerToggles();
        initInteractiveChoices();
        initTestEngines();
        initSurveyHelpers();
        initDynamicTabNav();
        initGlobalListeners();
    });
})();
