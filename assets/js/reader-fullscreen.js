(function () {
    function initFullscreenReader() {
        const toggleFullscreen = () => {
            const isFullscreen = document.body.classList.toggle('fullscreen-reader');
            window.dispatchEvent(new Event('resize'));
        };

        const toggleBtn = document.querySelector('[data-toggle-fullscreen]');
        if (toggleBtn) {
            toggleBtn.style.cursor = 'pointer';
            toggleBtn.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                toggleFullscreen();
            });
        }

        const closeBtn = document.querySelector('[data-close-fullscreen]');
        if (closeBtn) {
            closeBtn.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                document.body.classList.remove('fullscreen-reader');
                window.dispatchEvent(new Event('resize'));
            });
        }

        // Allow Esc key to exit fullscreen
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && document.body.classList.contains('fullscreen-reader')) {
                document.body.classList.remove('fullscreen-reader');
                window.dispatchEvent(new Event('resize'));
            }
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initFullscreenReader);
    } else {
        initFullscreenReader();
    }
})();
