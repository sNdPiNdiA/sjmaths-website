// JS for Maths Mastery

document.addEventListener('DOMContentLoaded', () => {
    initMobileCarousel();
});

function initMobileCarousel() {
    // Disabled as per user request for Vertical Path Layout
    return;

    const grid = document.querySelector('.class-grid');
    if (!grid) return;

    let autoScrollInterval;
    let isPaused = false;
    const scrollDelay = 3000; // 3 seconds per card

    // Only active on mobile view where carousel exists
    const isMobile = () => window.innerWidth <= 768;

    const startAutoScroll = () => {
        if (!isMobile() || autoScrollInterval) return;

        autoScrollInterval = setInterval(() => {
            if (isPaused) return;

            // Calculate next scroll position
            const cardWidth = grid.querySelector('.class-card').offsetWidth;
            const gap = parseFloat(getComputedStyle(grid).gap) || 24; // 1.5rem approx 24px
            const scrollAmount = cardWidth + gap;

            // Check if we are near the end
            const maxScroll = grid.scrollWidth - grid.clientWidth;

            if (grid.scrollLeft >= maxScroll - 10) {
                // Determine behavior: Loop result or smooth rewind? 
                // Smooth rewind to start
                grid.scrollTo({ left: 0, behavior: 'smooth' });
            } else {
                // Scroll to next
                grid.scrollBy({ left: scrollAmount, behavior: 'smooth' });
            }

        }, scrollDelay);
    };

    const stopAutoScroll = () => {
        clearInterval(autoScrollInterval);
        autoScrollInterval = null;
    };

    // Event Listeners for Pause/Resume

    // 1. Mouse Hover (Desktop testing / Hybrid devices)
    grid.addEventListener('mouseenter', () => {
        isPaused = true;
    });

    grid.addEventListener('mouseleave', () => {
        isPaused = false;
    });

    // 2. Touch Interaction (Mobile)
    grid.addEventListener('touchstart', () => {
        isPaused = true;
        stopAutoScroll(); // Stop completely while user is dragging
    }, { passive: true });

    grid.addEventListener('touchend', () => {
        isPaused = false;
        // unexpected touch end, restart after a delay
        setTimeout(startAutoScroll, scrollDelay);
    });

    // Handle Resize
    window.addEventListener('resize', () => {
        if (!isMobile()) {
            stopAutoScroll();
            // Reset scroll position when switching to desktop to avoid awkward offsets
            grid.scrollTo({ left: 0 });
        } else {
            startAutoScroll();
        }
    });

    // Initialize
    if (isMobile()) {
        startAutoScroll();
    }
}
