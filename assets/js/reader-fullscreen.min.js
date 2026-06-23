(function () {
    function initFullscreenReader() {
        const canvasWrap = document.querySelector('[data-pdf-canvas-wrap]');
        if (!canvasWrap) return;

        // Add hint element
        let hint = document.querySelector('.fullscreen-hint');
        if (!hint) {
            hint = document.createElement('div');
            hint.className = 'fullscreen-hint';
            hint.textContent = 'Tap to exit fullscreen';
            document.body.appendChild(hint);
        }

        canvasWrap.style.cursor = 'pointer';

        const toggleFullscreen = () => {
            const isFullscreen = document.body.classList.toggle('fullscreen-reader');

            if (isFullscreen) {
                document.body.classList.remove('hint-hidden');
                // Hide hint after 3 seconds
                setTimeout(() => {
                    document.body.classList.add('hint-hidden');
                }, 3000);
            }

            // Trigger resize to force PDF re-render
            window.dispatchEvent(new Event('resize'));
        };

        canvasWrap.addEventListener('click', toggleFullscreen);

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
                window.location.href = '/pages/ebooks.html';
            });
        }

        // Also allow Esc key to exit
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && document.body.classList.contains('fullscreen-reader')) {
                document.body.classList.remove('fullscreen-reader');
                window.dispatchEvent(new Event('resize'));
            }
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', () => {
            initFullscreenReader();

            // Auto-trigger fullscreen unless #landing is specified
            if (window.location.hash !== '#landing') {
                const canvasWrap = document.querySelector('[data-pdf-canvas-wrap]');
                if (canvasWrap) {
                    // Slight delay to ensure PDF.js and other UI elements are ready
                    setTimeout(() => {
                        window.dispatchEvent(new Event('resize'));
                        document.body.classList.add('fullscreen-reader');
                        window.dispatchEvent(new Event('resize'));
                    }, 300);
                }
            }
        });
    } else {
        initFullscreenReader();
        if (window.location.hash !== '#landing') {
            document.body.classList.add('fullscreen-reader');
            window.dispatchEvent(new Event('resize'));
        }
    }
})();
