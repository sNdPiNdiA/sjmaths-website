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
        window.addEventListener('scroll', () => {
            const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
            const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
            const scrolled = (height > 0) ? (winScroll / height) * 100 : 0;
            progressBar.style.width = scrolled + "%";
        });
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
function toggleAccordion(header) {
    const body = header.nextElementSibling;
    const expanded = header.getAttribute('aria-expanded') === 'true';

    header.setAttribute('aria-expanded', !expanded);
    if (expanded) {
        body.style.display = "none";
        header.querySelector('i').classList.remove('fa-chevron-up');
        header.querySelector('i').classList.add('fa-chevron-down');
    } else {
        body.style.display = "block";
        header.querySelector('i').classList.remove('fa-chevron-down');
        header.querySelector('i').classList.add('fa-chevron-up');
    }
}