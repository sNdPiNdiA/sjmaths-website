/* Shared JS for all Class 9 Advanced Science Chapters */

document.addEventListener("DOMContentLoaded", function () {
    const tabs = document.querySelectorAll(".science-tab, .tab");
    const panes = document.querySelectorAll(".tab-pane, .pane");
    const triggers = document.querySelectorAll("[data-go], [data-goto]");

    function activateTab(id, updateHash = true) {
        if (!id) return;
        
        tabs.forEach(tab => {
            tab.classList.toggle("active", tab.dataset.tab === id || tab.getAttribute('data-tab') === id);
        });

        panes.forEach(pane => {
            pane.classList.toggle("active", pane.id === id);
        });

        if (updateHash) {
            history.replaceState(null, "", "#" + id);
        }

        if (window.MathJax && typeof MathJax.typesetPromise === "function") {
            MathJax.typesetPromise();
        }

        // Trigger resize event to force Three.js canvases in the newly visible tab to recalculate dimensions
        setTimeout(() => {
            window.dispatchEvent(new Event('resize'));
        }, 50);

        // Smooth scroll to top of tab container instead of absolute top of page
        const tabContainer = document.querySelector(".science-tabs, .tabs");
        if (tabContainer) {
            tabContainer.scrollIntoView({ behavior: "smooth", block: "start" });
        } else {
            window.scrollTo({ top: 0, behavior: "smooth" });
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

    // Dynamic component loader with root-relative paths for reliability at any path depth
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

    // Load common header/footer layouts using root-relative paths
    loadComponent("header-container", "/components/header.html");
    loadComponent("footer-container", "/components/footer.html");
});

// Premium Solutions toggle helper
window.toggleSolution = function (btn) {
    const box = btn.nextElementSibling;
    if (!box) return;
    const open = box.classList.toggle('open');
    if (open) {
        box.style.display = 'block';
        box.style.opacity = '0';
        box.style.transition = 'opacity 0.3s ease';
        box.offsetHeight;
        box.style.opacity = '1';
        btn.innerHTML = '<i class="fas fa-eye-slash"></i> Hide Solution';
    } else {
        box.style.display = 'none';
        btn.innerHTML = '<i class="fas fa-eye"></i> Show Solution';
    }
};
