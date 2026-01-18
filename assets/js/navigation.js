// ===== MOBILE NAV TOGGLE (OPTIMIZED & ACCESSIBLE) =====
document.addEventListener('click', ({ target }) => {
    // 1. Identify the toggle button safely
    const toggleBtn = target.closest('.mobile-toggle');
    if (!toggleBtn) return;

    // 2. Identify the navigation menu
    const navMenu = document.querySelector('.desktop-nav') || document.querySelector('nav');
    if (!navMenu) return;

    // 3. Toggle State & Capture Result (True = Open, False = Closed)
    const isOpen = navMenu.classList.toggle('active');

    // 4. Optimize Icon Swapping (Uses boolean force)
    const icon = toggleBtn.querySelector('i');
    if (icon) {
        icon.classList.toggle('fa-times', isOpen); // Force 'times' if open
        icon.classList.toggle('fa-bars', !isOpen); // Force 'bars' if closed
    }

    // 5. Accessibility Update (Crucial for screen readers)
    toggleBtn.setAttribute('aria-expanded', isOpen);
});

// ===== OPTIONAL: CLOSE MENU ON CLICK OUTSIDE =====
// (Uncomment this block if you want the menu to close when clicking the body)
/*
document.addEventListener('click', (e) => {
    const nav = document.querySelector('nav');
    const toggle = e.target.closest('.mobile-toggle');
    
    // If nav is open, and click is NOT on nav AND NOT on toggle
    if (nav && nav.classList.contains('active') && !nav.contains(e.target) && !toggle) {
        nav.classList.remove('active');
        const icon = document.querySelector('.mobile-toggle i');
        if (icon) {
            icon.classList.add('fa-bars');
            icon.classList.remove('fa-times');
        }
    }
});
*/