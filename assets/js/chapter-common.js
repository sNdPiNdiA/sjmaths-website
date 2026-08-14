(function () {
    function initChapterCommon() {
        // --- DARK MODE TOGGLE ---
        const themeToggle = document.getElementById('theme-toggle');
        const getIsDark = () => {
            if (typeof window.isDarkMode === 'function') return window.isDarkMode();
            const sjDark = localStorage.getItem('sjmaths-dark');
            if (sjDark !== null) return sjDark === 'on';
            const legacyTheme = localStorage.getItem('theme');
            if (legacyTheme !== null) return legacyTheme === 'dark';
            return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
        };

        const updateIcon = (isDark) => {
            const icon = themeToggle ? themeToggle.querySelector('i') : null;
            if (icon) {
                if (isDark) {
                    icon.classList.remove('fa-moon');
                    icon.classList.add('fa-sun');
                } else {
                    icon.classList.remove('fa-sun');
                    icon.classList.add('fa-moon');
                }
            }
        };

        const isCurrentDark = getIsDark();
        if (document.documentElement) {
            document.documentElement.classList.toggle('dark-mode', isCurrentDark);
            document.documentElement.setAttribute('data-theme', isCurrentDark ? 'dark' : 'light');
        }
        if (document.body) {
            document.body.classList.toggle('dark-mode', isCurrentDark);
        }
        updateIcon(isCurrentDark);

        if (themeToggle) {
            themeToggle.addEventListener('click', (e) => {
                e.preventDefault();
                if (typeof window.toggleDarkMode === 'function') {
                    window.toggleDarkMode();
                } else {
                    const nextDark = !document.body.classList.contains('dark-mode');
                    document.documentElement.classList.toggle('dark-mode', nextDark);
                    document.documentElement.setAttribute('data-theme', nextDark ? 'dark' : 'light');
                    document.body.classList.toggle('dark-mode', nextDark);
                    try {
                        localStorage.setItem('sjmaths-dark', nextDark ? 'on' : 'off');
                        localStorage.setItem('theme', nextDark ? 'dark' : 'light');
                        localStorage.setItem('sjmaths-test-dark', nextDark ? 'true' : 'false');
                    } catch(err) {}
                    updateIcon(nextDark);
                    window.dispatchEvent(new CustomEvent('themeChanged', { detail: { isDark: nextDark } }));
                }
            });
        }

        window.addEventListener('themeChanged', (e) => {
            if (e && e.detail) {
                updateIcon(e.detail.isDark);
            }
        });

        // --- SCROLL PROGRESS ---
        const progressBar = document.getElementById("progressBar");
        if (progressBar) {
            let ticking = false;
            window.addEventListener('scroll', () => {
                if (!ticking) {
                    window.requestAnimationFrame(() => {
                        const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
                        const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
                        const scrolled = (height > 0) ? (winScroll / height) * 100 : 0;
                        progressBar.style.width = scrolled + "%";
                        ticking = false;
                    });
                    ticking = true;
                }
            }, { passive: true });
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initChapterCommon);
    } else {
        initChapterCommon();
    }
})();

// --- GLOBAL QUIZ CHECKER ---
function checkQuiz(element, isCorrect) {
    const parent = element.parentElement;
    const options = parent.querySelectorAll('.quiz-option');
    options.forEach(opt => opt.style.pointerEvents = 'none');

    if (isCorrect) {
        element.classList.add('correct');
        element.innerHTML += ' <i class="fas fa-check-circle"></i>';
    } else {
        element.classList.add('wrong');
        element.innerHTML += ' <i class="fas fa-times-circle"></i>';
        // Highlight the correct answer
        options.forEach(opt => {
            if (opt.getAttribute('onclick') && opt.getAttribute('onclick').includes('true')) {
                opt.classList.add('correct');
            }
        });
    }
}

// --- GLOBAL ACCORDION ---
// --- GLOBAL ACCORDION ---
function toggleAccordion(header) {
    const body = header.nextElementSibling;
    if (!body) return;
    const isOpen = body.classList.contains('open');

    // Close siblings
    const parent = header.closest('.note-section') || header.parentElement?.parentElement;
    if (parent) {
        parent.querySelectorAll('.accordion-body.open').forEach(other => {
            if (other !== body) {
                other.classList.remove('open');
                other.style.maxHeight = null;
                const h = other.previousElementSibling;
                if (h) {
                    h.classList.remove('active');
                    h.setAttribute('aria-expanded', 'false');
                }
            }
        });
    }

    // Toggle Self
    if (isOpen) {
        body.classList.remove('open');
        body.style.maxHeight = null;
        header.classList.remove('active');
        header.setAttribute('aria-expanded', 'false');
    } else {
        // Read height first to avoid forced reflow after class mutation
        const height = body.scrollHeight;

        // Ensure display is reset in case inline styles blocked it
        body.style.display = '';
        body.classList.add('open');
        header.classList.add('active');
        header.setAttribute('aria-expanded', 'true');
        // Set dynamic height for transition (with buffer to prevent cutoff)
        body.style.maxHeight = (height + 40) + "px";
    }
}