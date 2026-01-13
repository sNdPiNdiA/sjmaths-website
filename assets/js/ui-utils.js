document.addEventListener('DOMContentLoaded', () => {
    /* =========================================
       1. DARK MODE TOGGLE
       Handles IDs: 'theme-toggle' or 'darkToggle'
       Storage Key: 'theme'
    ========================================= */
    const themeToggle = document.getElementById('theme-toggle') || document.getElementById('darkToggle');
    const body = document.body;

    if (themeToggle) {
        const icon = themeToggle.querySelector('i');

        // Load saved preference
        const savedTheme = localStorage.getItem('theme');
        if (savedTheme === 'dark') {
            body.classList.add('dark-mode');
            if (icon) {
                icon.classList.remove('fa-moon');
                icon.classList.add('fa-sun');
            }
        }

        themeToggle.addEventListener('click', () => {
            body.classList.toggle('dark-mode');
            const isDark = body.classList.contains('dark-mode');

            // Update Icon
            if (icon) {
                if (isDark) {
                    icon.classList.remove('fa-moon');
                    icon.classList.add('fa-sun');
                } else {
                    icon.classList.remove('fa-sun');
                    icon.classList.add('fa-moon');
                }
            }

            // Save Preference
            localStorage.setItem('theme', isDark ? 'dark' : 'light');
        });
    }

    /* =========================================
       2. SCROLL PROGRESS BAR
       Target ID: 'progressBar'
    ========================================= */
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