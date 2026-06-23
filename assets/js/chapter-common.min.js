document.addEventListener('DOMContentLoaded', () => {
    // --- DARK MODE TOGGLE ---
    const themeToggle = document.getElementById('theme-toggle');
    const body = document.body;
    const icon = themeToggle ? themeToggle.querySelector('i') : null;

    if (themeToggle) {
        // Initialize state
        if (localStorage.getItem('theme') === 'dark') {
            body.classList.add('dark-mode');
            if (icon) {
                icon.classList.remove('fa-moon');
                icon.classList.add('fa-sun');
            }
        }

        themeToggle.addEventListener('click', () => {
            body.classList.toggle('dark-mode');
            const isDark = body.classList.contains('dark-mode');

            if (icon) {
                if (isDark) {
                    icon.classList.remove('fa-moon');
                    icon.classList.add('fa-sun');
                    localStorage.setItem('theme', 'dark');
                } else {
                    icon.classList.remove('fa-sun');
                    icon.classList.add('fa-moon');
                    localStorage.setItem('theme', 'light');
                }
            }

            // Dispatch event so specific chapters can redraw graphs if needed
            window.dispatchEvent(new CustomEvent('themeChanged', { detail: { isDark } }));
        });
    }

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
});

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