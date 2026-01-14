// main.js

/* =========================================
   1. CONFIGURATION & STATE (Run Immediately)
   ========================================= */

// Theme Definitions (Keys match CSS variables directly)
const themes = {
    purple: { primary: '#8e44ad', 'primary-dark': '#6c3483', 'primary-light': '#a569bd', secondary: '#e74c3c', accent: '#f39c12' },
    blue: { primary: '#2563eb', 'primary-dark': '#1e40af', 'primary-light': '#60a5fa', secondary: '#0ea5e9', accent: '#22c55e' },
    green: { primary: '#16a34a', 'primary-dark': '#166534', 'primary-light': '#4ade80', secondary: '#22c55e', accent: '#facc15' },
    orange: { primary: '#f97316', 'primary-dark': '#c2410c', 'primary-light': '#fdba74', secondary: '#ef4444', accent: '#f59e0b' }
};

// Apply Saved States Immediately (Prevents FOUC)
const savedDark = localStorage.getItem('sjmaths-dark') === 'on';
if (savedDark) document.body.classList.add('dark-mode');

const savedTheme = localStorage.getItem('sjmaths-theme');
if (savedTheme && themes[savedTheme]) applyThemeVars(savedTheme);


/* =========================================
   2. THEME CONTROLLER
   ========================================= */

function applyThemeVars(themeName) {
    const theme = themes[themeName];
    if (!theme) return;

    const root = document.documentElement.style;
    Object.entries(theme).forEach(([key, value]) => {
        root.setProperty(`--${key}`, value);
    });
}

// Global function for UI buttons
window.setTheme = function (themeName) {
    applyThemeVars(themeName);
    localStorage.setItem('sjmaths-theme', themeName);
};


/* =========================================
   3. DARK MODE INTERACTION
   ========================================= */

document.addEventListener('DOMContentLoaded', () => {

    // Helper: Update Icon based on Body Class
    const updateToggleIcon = (btn) => {
        const icon = btn.querySelector('i');
        if (!icon) return;
        const isDark = document.body.classList.contains('dark-mode');
        icon.className = isDark ? 'fas fa-sun' : 'fas fa-moon';
    };

    // 1. Event Delegation: Handles clicks even if button loads late
    document.addEventListener('click', (e) => {
        const toggleBtn = e.target.closest('#darkToggle');
        if (!toggleBtn) return;

        // Toggle State
        const isDark = document.body.classList.toggle('dark-mode');
        localStorage.setItem('sjmaths-dark', isDark ? 'on' : 'off');

        // Update Icon
        updateToggleIcon(toggleBtn);
    });

    // 2. Initialization: Find button to set initial icon
    const initIconState = () => {
        const btn = document.getElementById('darkToggle');
        if (btn) {
            updateToggleIcon(btn);
            return true; // Found it
        }
        return false; // Not found
    };

    // Try immediately
    if (!initIconState()) {
        // If not found (e.g. loaded via component.js), wait for it
        const observer = new MutationObserver((mutations, obs) => {
            if (initIconState()) obs.disconnect(); // Stop watching once found
        });
        observer.observe(document.body, { childList: true, subtree: true });
    }
});

/* =========================================
   4. SCROLL ANIMATION OBSERVER
   ========================================= */

const initScrollAnimations = () => {
    const observerOptions = {
        threshold: 0.15, // Trigger when 15% of element is visible
        rootMargin: "0px 0px -50px 0px"
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                observer.unobserve(entry.target); // Animate only once
            }
        });
    }, observerOptions);

    const elements = document.querySelectorAll('.animate-on-scroll');
    elements.forEach(el => observer.observe(el));
};

document.addEventListener('DOMContentLoaded', initScrollAnimations);

/* =========================================
   5. HERO PARALLAX EFFECT
   ========================================= */

const initParallax = () => {
    // Disable on mobile devices (< 768px) and if user prefers reduced motion for performance and UX
    if (window.innerWidth < 768 || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

    const blobs = document.querySelectorAll('.blob');
    if (!blobs.length) return;

    let ticking = false;

    window.addEventListener('scroll', () => {
        if (!ticking) {
            window.requestAnimationFrame(() => {
                const scrolled = window.scrollY;
                blobs.forEach((blob, index) => {
                    // Create depth by moving blobs at different speeds
                    const speed = (index + 1) * 0.15;
                    blob.style.transform = `translateY(${scrolled * speed}px)`;
                });
                ticking = false;
            });
            ticking = true;
        }
    });
};

document.addEventListener('DOMContentLoaded', initParallax);

/* =========================================
   6. BACK TO TOP BUTTON
   ========================================= */

document.addEventListener('DOMContentLoaded', () => {
    const backToTopBtn = document.getElementById('backToTop');

    if (backToTopBtn) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 300) {
                backToTopBtn.classList.add('show');
            } else {
                backToTopBtn.classList.remove('show');
            }
        });

        backToTopBtn.addEventListener('click', () => {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }
});