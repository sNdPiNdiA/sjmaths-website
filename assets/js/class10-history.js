/**
 * class10-history.js
 * Unified Client-Side Engine for Class 10 History Chapter Pages
 */

(() => {
    const tabOrder = ["overview", "concepts", "exercise", "worksheets", "revision", "tests"];
    const tabNames = {
        overview: "Overview",
        concepts: "Concepts",
        exercise: "Exercises",
        worksheets: "Worksheets",
        revision: "Revision",
        tests: "Tests"
    };

    function activateTab(id, updateHash = true) {
        const panels = document.querySelectorAll(".tab-panel, .panel");
        panels.forEach(panel => panel.classList.toggle("active", panel.id === id));

        document.querySelectorAll(".tab-btn, .tab").forEach(btn => {
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
        
        const activeBtn = document.querySelector(`.tab-btn[data-tab="${id}"], .tab[data-tab="${id}"]`);
        if (activeBtn) {
            activeBtn.scrollIntoView({ behavior: "smooth", block: "nearest", inline: "center" });
        }
    }

    function initTabs() {
        const tabButtons = document.querySelectorAll("[data-tab]");
        tabButtons.forEach(btn => {
            btn.addEventListener("click", () => activateTab(btn.dataset.tab));
        });

        document.querySelectorAll("[data-go]").forEach(b => {
            b.addEventListener("click", () => activateTab(b.dataset.go));
        });

        const initial = location.hash.replace("#", "");
        if (tabOrder.includes(initial)) {
            activateTab(initial, false);
        } else {
            activateTab("overview", false);
        }
    }

    function initDynamicTabNav() {
        tabOrder.forEach((tabId, idx) => {
            const panel = document.getElementById(tabId);
            if (!panel) return;

            const existingNav = panel.querySelector(".tab-nav-buttons, .tab-nav");
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
        const backTop = document.getElementById("backTop") || document.getElementById("top");
        window.addEventListener("scroll", () => {
            if (backTop) backTop.classList.toggle("show", window.scrollY > 400);
        });

        if (backTop) {
            backTop.addEventListener("click", () => window.scrollTo({ top: 0, behavior: "smooth" }));
        }

        document.addEventListener("keydown", (event) => {
            if (event.key >= "1" && event.key <= "6") {
                const targetTab = tabOrder[Number(event.key) - 1];
                if (targetTab) activateTab(targetTab);
            }
        });
    }

    document.addEventListener("DOMContentLoaded", () => {
        initTabs();
        initDynamicTabNav();
        initGlobalListeners();
    });
})();
