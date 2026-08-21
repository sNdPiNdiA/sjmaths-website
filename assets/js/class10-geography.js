/**
 * class10-geography.js
 * Unified Client-Side Engine for Class 10 Geography Chapter Pages
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
        if (!tabOrder.includes(id)) id = "overview";
        const panels = document.querySelectorAll(".panel");
        panels.forEach(p => p.classList.toggle("active", p.id === id));

        document.querySelectorAll("[data-tab]").forEach(b => {
            const active = b.dataset.tab === id;
            b.classList.toggle("active", active);
            b.setAttribute("aria-selected", active ? "true" : "false");
        });

        const activeBtn = document.querySelector(`.tab[data-tab="${id}"]`);
        if (activeBtn) {
            activeBtn.scrollIntoView({ behavior: "smooth", block: "nearest", inline: "center" });
        }

        const progress = document.getElementById("progressText");
        const idx = tabOrder.indexOf(id);
        if (progress) progress.textContent = `${idx + 1} / ${tabOrder.length}`;

        if (updateHash) history.replaceState(null, "", `#${id}`);
        window.scrollTo({ top: 0, behavior: "smooth" });
    }

    function initTabs() {
        document.querySelectorAll("[data-tab]").forEach(b => {
            b.addEventListener("click", () => activateTab(b.dataset.tab));
        });

        document.querySelectorAll("[data-go]").forEach(b => {
            b.addEventListener("click", () => activateTab(b.dataset.go));
        });

        const initial = location.hash.replace("#", "");
        activateTab(tabOrder.includes(initial) ? initial : "overview", false);
    }

    function initDynamicTabNav() {
        tabOrder.forEach((id, i) => {
            const panel = document.getElementById(id);
            if (!panel) return;

            const existingNav = panel.querySelector(".tab-nav-buttons");
            if (existingNav) existingNav.remove();

            const nav = document.createElement("div");
            nav.className = "tab-nav-buttons";

            if (i > 0) {
                const b = document.createElement("button");
                b.textContent = "← " + tabNames[tabOrder[i - 1]];
                b.onclick = () => activateTab(tabOrder[i - 1]);
                nav.appendChild(b);
            } else {
                nav.appendChild(document.createElement("span"));
            }

            if (i < tabOrder.length - 1) {
                const b = document.createElement("button");
                b.textContent = tabNames[tabOrder[i + 1]] + " →";
                b.onclick = () => activateTab(tabOrder[i + 1]);
                nav.appendChild(b);
            }

            panel.appendChild(nav);
        });
    }

    function initGlobalListeners() {
        const back = document.getElementById("backTop");
        window.addEventListener("scroll", () => {
            if (back) back.classList.toggle("show", window.scrollY > 400);
        });

        if (back) {
            back.onclick = () => window.scrollTo({ top: 0, behavior: "smooth" });
        }

        document.addEventListener("keydown", e => {
            if (e.key >= "1" && e.key <= "6") activateTab(tabOrder[Number(e.key) - 1]);
        });
    }

    document.addEventListener("DOMContentLoaded", () => {
        initTabs();
        initDynamicTabNav();
        initGlobalListeners();
    });
})();
