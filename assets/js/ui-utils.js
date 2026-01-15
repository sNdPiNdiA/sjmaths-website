document.addEventListener('DOMContentLoaded', () => {
    /* =========================================
       1. SCROLL HANDLER (Progress Bar & Back to Top)
    ========================================= */
    const progressBar = document.getElementById("progressBar");
    const backToTopBtn = document.getElementById('backToTop');

    if (progressBar || backToTopBtn) {
        let ticking = false;

        // Back to Top Click Handler
        if (backToTopBtn) {
            backToTopBtn.addEventListener('click', () => {
                window.scrollTo({ top: 0, behavior: 'smooth' });
            });
        }

        window.addEventListener('scroll', () => {
            if (!ticking) {
                window.requestAnimationFrame(() => {
                    const scrollTop = window.scrollY || document.documentElement.scrollTop;

                    // 1. Progress Bar
                    if (progressBar) {
                        const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
                        const scrolled = (height > 0) ? (scrollTop / height) * 100 : 0;
                        progressBar.style.width = scrolled + "%";
                    }

                    // 2. Back to Top
                    if (backToTopBtn) {
                        backToTopBtn.classList.toggle('show', scrollTop > 300);
                    }

                    ticking = false;
                });
                ticking = true;
            }
        });
    }
});