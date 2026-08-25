/**
 * =========================================================
 * CLASS 11 CHEMISTRY — COMMON JAVASCRIPT
 * Premium Mobile-First Learning UI
 * =========================================================
 *
 * Shared functionality for all Class 11 Chemistry units.
 *
 * Features:
 * - Mobile topic navigation
 * - Active section tracking
 * - Smooth scrolling
 * - Search
 * - Reading progress
 * - Sidebar synchronization
 * - Mobile bottom navigation
 * - Theme toggle
 * - Back-to-top
 * - Copy equations/formulas
 * - Accordion handling
 * - Keyboard accessibility
 * - Persistent reading position
 * =========================================================
 */

"use strict";


/* =========================================================
   01. GLOBAL CONFIGURATION
   ========================================================= */

const ChemistryApp = {
    config: {
        storagePrefix: "sj-chemistry-",
        progressKey: "reading-progress",
        themeKey: "theme",
        positionKey: "reading-position",
        searchDebounce: 180,
        scrollOffset: 88
    },

    state: {
        sections: [],
        currentSection: null,
        searchOpen: false,
        searchQuery: "",
        initialized: false
    }
};


/* =========================================================
   02. DOM HELPERS
   ========================================================= */

const $ = (selector, scope = document) =>
    scope.querySelector(selector);

const $$ = (selector, scope = document) =>
    [...scope.querySelectorAll(selector)];

const createElement = (tag, className = "") => {
    const element = document.createElement(tag);

    if (className) {
        element.className = className;
    }

    return element;
};


/* =========================================================
   03. UNIT INFORMATION
   ========================================================= */

function getUnitSlug() {
    return (
        document.body.dataset.unit ||
        document.documentElement.dataset.unit ||
        window.location.pathname
    );
}

function getUnitStorageKey(key) {
    return `${ChemistryApp.config.storagePrefix}${getUnitSlug()}-${key}`;
}


/* =========================================================
   04. INITIALIZATION
   ========================================================= */

document.addEventListener("DOMContentLoaded", () => {
    ChemistryApp.state.sections = $$(".content-section");

    initializeSmoothScrolling();
    initializeSectionTracking();
    initializeReadingProgress();
    initializeTopicNavigation();
    initializeSidebar();
    initializeMobileNavigation();
    initializeSearch();
    initializeCopyButtons();
    initializeAccordions();
    initializeTheme();
    initializeBackToTop();
    initializeReadingPosition();
    initializeKeyboardShortcuts();
    initializeExternalLinks();

    ChemistryApp.state.initialized = true;

    document.dispatchEvent(
        new CustomEvent("chemistry:ready")
    );
});


/* =========================================================
   05. SMOOTH SCROLLING
   ========================================================= */

function initializeSmoothScrolling() {
    document.addEventListener("click", event => {
        const link = event.target.closest('a[href^="#"]');

        if (!link) return;

        const targetId = link.getAttribute("href");

        if (!targetId || targetId === "#") return;

        const target = document.querySelector(targetId);

        if (!target) return;

        event.preventDefault();

        const headerOffset =
            ChemistryApp.config.scrollOffset;

        const targetPosition =
            target.getBoundingClientRect().top +
            window.scrollY -
            headerOffset;

        window.scrollTo({
            top: targetPosition,
            behavior:
                window.matchMedia(
                    "(prefers-reduced-motion: reduce)"
                ).matches
                    ? "auto"
                    : "smooth"
        });

        history.replaceState(
            null,
            "",
            targetId
        );

        setActiveSection(targetId.substring(1));
    });
}


/* =========================================================
   06. ACTIVE SECTION TRACKING
   ========================================================= */

function initializeSectionTracking() {
    const sections = ChemistryApp.state.sections;

    if (!sections.length) return;

    const observer = new IntersectionObserver(
        entries => {
            const visibleSections = entries
                .filter(entry => entry.isIntersecting)
                .sort(
                    (a, b) =>
                        a.boundingClientRect.top -
                        b.boundingClientRect.top
                );

            if (!visibleSections.length) return;

            const activeSection =
                visibleSections[0].target;

            setActiveSection(activeSection.id);
        },
        {
            rootMargin: "-100px 0px -65% 0px",
            threshold: [0, 0.15, 0.4]
        }
    );

    sections.forEach(section =>
        observer.observe(section)
    );
}

function setActiveSection(id) {
    ChemistryApp.state.currentSection = id;

    $$(".sidebar-link").forEach(link => {
        const isActive =
            link.getAttribute("href") === `#${id}`;

        link.classList.toggle(
            "is-active",
            isActive
        );
    });

    $$(".topic-nav-link").forEach(link => {
        const isActive =
            link.getAttribute("href") === `#${id}`;

        link.classList.toggle(
            "is-active",
            isActive
        );
    });

    document.dispatchEvent(
        new CustomEvent(
            "chemistry:sectionchange",
            {
                detail: { id }
            }
        )
    );
}


/* =========================================================
   07. TOPIC NAVIGATION
   ========================================================= */

function initializeTopicNavigation() {
    const topicLinks = $$(".topic-nav-link");

    if (!topicLinks.length) return;

    topicLinks.forEach(link => {
        link.addEventListener("click", () => {
            closeMobileTopicNavigation();
        });
    });
}


/* =========================================================
   08. SIDEBAR
   ========================================================= */

function initializeSidebar() {
    const sidebarLinks = $$(".sidebar-link");

    sidebarLinks.forEach(link => {
        link.addEventListener("click", () => {
            const href = link.getAttribute("href");

            if (!href) return;

            setActiveSection(
                href.replace("#", "")
            );
        });
    });
}


/* =========================================================
   09. MOBILE NAVIGATION
   ========================================================= */

function initializeMobileNavigation() {
    const topicButton =
        document.querySelector(
            '[data-action="topics"]'
        );

    const searchButton =
        document.querySelector(
            '[data-action="search"]'
        );

    const homeButton =
        document.querySelector(
            '[data-action="home"]'
        );

    const progressButton =
        document.querySelector(
            '[data-action="progress"]'
        );

    topicButton?.addEventListener(
        "click",
        openMobileTopicNavigation
    );

    searchButton?.addEventListener(
        "click",
        openSearch
    );

    homeButton?.addEventListener(
        "click",
        () => {
            window.scrollTo({
                top: 0,
                behavior: "smooth"
            });
        }
    );

    progressButton?.addEventListener(
        "click",
        () => {
            const progress =
                getReadingProgress();

            showProgressMessage(
                `${progress}% completed`
            );
        }
    );
}

function openMobileTopicNavigation() {
    const nav = $(".topic-nav");

    if (!nav) return;

    nav.scrollIntoView({
        behavior: "smooth",
        block: "start"
    });
}

function closeMobileTopicNavigation() {
    // Reserved for future mobile drawer implementation.
}


/* =========================================================
   10. READING PROGRESS
   ========================================================= */

function initializeReadingProgress() {
    const progressBar =
        document.querySelector(
            ".progress-bar"
        );

    const progressValue =
        document.querySelector(
            ".progress-value"
        );

    const updateProgress = () => {
        const documentHeight =
            document.documentElement.scrollHeight -
            window.innerHeight;

        if (documentHeight <= 0) return;

        const progress =
            Math.min(
                100,
                Math.max(
                    0,
                    (window.scrollY / documentHeight) *
                    100
                )
            );

        const rounded =
            Math.round(progress);

        if (progressBar) {
            progressBar.style.setProperty(
                "--progress",
                `${rounded}%`
            );
        }

        if (progressValue) {
            progressValue.textContent =
                `${rounded}%`;
        }

        localStorage.setItem(
            getUnitStorageKey(
                ChemistryApp.config.progressKey
            ),
            String(rounded)
        );
    };

    window.addEventListener(
        "scroll",
        throttle(
            updateProgress,
            100
        ),
        { passive: true }
    );

    updateProgress();
}

function getReadingProgress() {
    const value =
        localStorage.getItem(
            getUnitStorageKey(
                ChemistryApp.config.progressKey
            )
        );

    return Number(value || 0);
}


/* =========================================================
   11. SEARCH
   ========================================================= */

function initializeSearch() {
    const searchInput =
        $(".search-input");

    if (!searchInput) return;

    searchInput.addEventListener(
        "input",
        debounce(
            event => {
                performSearch(
                    event.target.value
                );
            },
            ChemistryApp.config.searchDebounce
        )
    );

    searchInput.addEventListener(
        "keydown",
        event => {
            if (event.key === "Escape") {
                closeSearch();
            }

            if (
                event.key === "Enter" &&
                event.target.value.trim()
            ) {
                performSearch(
                    event.target.value
                );
            }
        }
    );
}

function openSearch() {
    const search =
        $(".search-container");

    if (!search) return;

    search.classList.add("is-open");

    const input =
        $(".search-input", search);

    input?.focus();

    ChemistryApp.state.searchOpen = true;
}

function closeSearch() {
    const search =
        $(".search-container");

    if (!search) return;

    search.classList.remove(
        "is-open"
    );

    ChemistryApp.state.searchOpen = false;
}

function performSearch(query) {
    const normalized =
        query
            .trim()
            .toLowerCase();

    ChemistryApp.state.searchQuery =
        normalized;

    const searchable =
        $$(
            ".content-section"
        );

    if (!normalized) {
        searchable.forEach(
            section => {
                section.hidden = false;
            }
        );

        return;
    }

    searchable.forEach(section => {
        const text =
            section.textContent
                .toLowerCase();

        section.hidden =
            !text.includes(normalized);
    });

    const firstMatch =
        searchable.find(
            section => !section.hidden
        );

    if (firstMatch) {
        firstMatch.scrollIntoView({
            behavior: "smooth",
            block: "start"
        });
    }
}


/* =========================================================
   12. COPY FORMULAS / EQUATIONS
   ========================================================= */

function initializeCopyButtons() {
    $(
        ".formula-card, .equation, pre"
    ).forEach(block => {

        if (
            block.querySelector(
                ".copy-button"
            )
        ) {
            return;
        }

        const button =
            createElement(
                "button",
                "copy-button"
            );

        button.type = "button";
        button.textContent = "Copy";
        button.setAttribute(
            "aria-label",
            "Copy content"
        );

        button.addEventListener(
            "click",
            async () => {
                const text =
                    block.innerText
                        .trim();

                try {
                    await navigator.clipboard.writeText(
                        text
                    );

                    button.textContent =
                        "Copied";

                    setTimeout(() => {
                        button.textContent =
                            "Copy";
                    }, 1400);

                } catch {
                    button.textContent =
                        "Unable to copy";
                }
            }
        );

        block.style.position =
            "relative";

        block.appendChild(button);
    });
}


/* =========================================================
   13. ACCORDIONS
   ========================================================= */

function initializeAccordions() {
    const accordions =
        $$(".accordion");

    accordions.forEach(
        accordion => {

            const summary =
                accordion.querySelector(
                    "summary"
                );

            if (!summary) return;

            summary.addEventListener(
                "click",
                () => {

                    document.dispatchEvent(
                        new CustomEvent(
                            "chemistry:accordion",
                            {
                                detail: {
                                    accordion
                                }
                            }
                        )
                    );

                }
            );
        }
    );
}


/* =========================================================
   14. THEME
   ========================================================= */

function initializeTheme() {
    const themeButton =
        document.querySelector(
            '[data-action="theme"]'
        );

    if (!themeButton) return;

    const savedTheme =
        localStorage.getItem(
            getUnitStorageKey(
                ChemistryApp.config.themeKey
            )
        );

    if (savedTheme) {
        document.documentElement.dataset.theme =
            savedTheme;
    }

    updateThemeButton(
        themeButton
    );

    themeButton.addEventListener(
        "click",
        () => {

            const current =
                document.documentElement
                    .dataset.theme ||
                "system";

            let next;

            if (current === "light") {
                next = "dark";
            } else if (current === "dark") {
                next = "system";
            } else {
                next = "light";
            }

            if (next === "system") {
                delete document.documentElement
                    .dataset.theme;
            } else {
                document.documentElement
                    .dataset.theme = next;
            }

            localStorage.setItem(
                getUnitStorageKey(
                    ChemistryApp.config.themeKey
                ),
                next
            );

            updateThemeButton(
                themeButton
            );
        }
    );
}

function updateThemeButton(button) {
    const theme =
        document.documentElement
            .dataset.theme ||
        "system";

    button.setAttribute(
        "aria-label",
        `Theme: ${theme}`
    );

    button.title =
        `Theme: ${theme}`;
}


/* =========================================================
   15. BACK TO TOP
   ========================================================= */

function initializeBackToTop() {
    let button =
        document.querySelector(
            ".back-to-top"
        );

    if (!button) {
        button =
            createElement(
                "button",
                "back-to-top"
            );

        button.type = "button";
        button.textContent = "↑";
        button.setAttribute(
            "aria-label",
            "Back to top"
        );

        Object.assign(
            button.style,
            {
                position: "fixed",
                right: "18px",
                bottom: "84px",
                zIndex: "80",
                width: "42px",
                height: "42px",
                border: "0",
                borderRadius: "50%",
                background: "var(--gray-950)",
                color: "var(--white)",
                opacity: "0",
                pointerEvents: "none",
                transition:
                    "opacity 200ms ease, transform 200ms ease"
            }
        );

        document.body.appendChild(
            button
        );
    }

    window.addEventListener(
        "scroll",
        throttle(() => {

            const visible =
                window.scrollY > 500;

            button.style.opacity =
                visible ? "1" : "0";

            button.style.pointerEvents =
                visible ? "auto" : "none";

        }, 100),
        { passive: true }
    );

    button.addEventListener(
        "click",
        () => {
            window.scrollTo({
                top: 0,
                behavior: "smooth"
            });
        }
    );
}


/* =========================================================
   16. READING POSITION
   ========================================================= */

function initializeReadingPosition() {
    const key =
        getUnitStorageKey(
            ChemistryApp.config.positionKey
        );

    let restored = false;

    window.addEventListener(
        "scroll",
        throttle(() => {

            if (
                window.scrollY < 100
            ) {
                return;
            }

            sessionStorage.setItem(
                key,
                String(window.scrollY)
            );

        }, 700),
        { passive: true }
    );

    window.addEventListener(
        "load",
        () => {

            if (restored) return;

            const saved =
                Number(
                    sessionStorage.getItem(
                        key
                    )
                );

            if (
                saved > 150 &&
                !window.location.hash
            ) {
                setTimeout(() => {
                    window.scrollTo({
                        top: saved,
                        behavior: "auto"
                    });

                    restored = true;
                }, 150);
            }
        }
    );
}


/* =========================================================
   17. KEYBOARD SHORTCUTS
   ========================================================= */

function initializeKeyboardShortcuts() {
    document.addEventListener(
        "keydown",
        event => {

            const target =
                event.target;

            const isTyping =
                target instanceof
                HTMLInputElement ||
                target instanceof
                HTMLTextAreaElement ||
                target.isContentEditable;

            if (isTyping) return;

            /* / = search */
            if (
                event.key === "/" &&
                !event.ctrlKey &&
                !event.metaKey
            ) {
                event.preventDefault();
                openSearch();
            }

            /* Home = top */
            if (event.key === "Home") {
                window.scrollTo({
                    top: 0,
                    behavior: "smooth"
                });
            }

            /* Escape = close UI */
            if (event.key === "Escape") {
                closeSearch();
            }
        }
    );
}


/* =========================================================
   18. EXTERNAL LINKS
   ========================================================= */

function initializeExternalLinks() {
    $$("a[href]").forEach(link => {

        const href =
            link.getAttribute("href");

        if (!href) return;

        if (
            href.startsWith("http://") ||
            href.startsWith("https://")
        ) {
            link.target = "_blank";
            link.rel =
                "noopener noreferrer";
        }
    });
}


/* =========================================================
   19. PROGRESS MESSAGE
   ========================================================= */

function showProgressMessage(message) {
    let toast =
        $(".chemistry-toast");

    if (!toast) {
        toast =
            createElement(
                "div",
                "chemistry-toast"
            );

        Object.assign(
            toast.style,
            {
                position: "fixed",
                zIndex: "999",
                left: "50%",
                bottom: "82px",
                transform:
                    "translateX(-50%) translateY(10px)",
                padding: "10px 15px",
                borderRadius: "999px",
                background:
                    "var(--gray-950)",
                color:
                    "var(--white)",
                fontSize: "0.78rem",
                fontWeight: "700",
                opacity: "0",
                pointerEvents: "none",
                transition:
                    "opacity 180ms ease, transform 180ms ease",
                whiteSpace: "nowrap"
            }
        );

        document.body.appendChild(
            toast
        );
    }

    toast.textContent =
        message;

    requestAnimationFrame(() => {
        toast.style.opacity = "1";
        toast.style.transform =
            "translateX(-50%) translateY(0)";
    });

    clearTimeout(
        toast._timeout
    );

    toast._timeout =
        setTimeout(() => {
            toast.style.opacity = "0";
            toast.style.transform =
                "translateX(-50%) translateY(10px)";
        }, 1800);
}


/* =========================================================
   20. DEBOUNCE
   ========================================================= */

function debounce(
    callback,
    delay
) {
    let timeout;

    return (...args) => {

        clearTimeout(timeout);

        timeout =
            setTimeout(
                () => callback(...args),
                delay
            );
    };
}


/* =========================================================
   21. THROTTLE
   ========================================================= */

function throttle(
    callback,
    delay
) {
    let waiting = false;

    return (...args) => {

        if (waiting) return;

        callback(...args);

        waiting = true;

        setTimeout(() => {
            waiting = false;
        }, delay);
    };
}


/* =========================================================
   22. PUBLIC API
   ========================================================= */

window.ChemistryApp =
    ChemistryApp;

window.ChemistryUtils = {
    getUnitSlug,
    getReadingProgress,
    setActiveSection,
    openSearch,
    closeSearch
};
/* =========================================================
   STEPWISE SOLUTIONS
   ========================================================= */

document.addEventListener("click", function (event) {

    /* Open / close complete solution */
    const solutionToggle = event.target.closest(".solution-toggle");

    if (solutionToggle) {
        const box = solutionToggle.closest(".solution-box");

        if (box) {
            box.classList.toggle("open");

            const expanded = box.classList.contains("open");
            solutionToggle.setAttribute("aria-expanded", expanded);
        }

        return;
    }


    /* Reveal individual step */
    const stepButton = event.target.closest(".step-reveal");

    if (stepButton) {
        const step = stepButton.closest(".solution-step");

        if (step) {
            step.classList.add("revealed");
        }

        return;
    }


    /* Show all steps */
    const showAllButton = event.target.closest(".show-all-steps");

    if (showAllButton) {
        const solutionBox = showAllButton.closest(".solution-box");

        if (solutionBox) {
            solutionBox
                .querySelectorAll(".solution-step")
                .forEach(step => {
                    step.classList.add("revealed");
                });

            showAllButton.textContent = "All Steps Revealed";
            showAllButton.disabled = true;
        }
    }

});


/* =========================================================
   OPTIONAL: RESET SOLUTIONS WHEN TAB CHANGES
   ========================================================= */

function resetStepwiseSolutions(container = document) {

    container.querySelectorAll(".solution-box").forEach(box => {
        box.classList.remove("open");

        const toggle = box.querySelector(".solution-toggle");

        if (toggle) {
            toggle.setAttribute("aria-expanded", "false");
        }

        box.querySelectorAll(".solution-step").forEach(step => {
            step.classList.remove("revealed");
        });

        const showAll = box.querySelector(".show-all-steps");

        if (showAll) {
            showAll.textContent = "Show All Steps";
            showAll.disabled = false;
        }
    });

}