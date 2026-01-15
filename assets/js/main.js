// main.js

/* =========================================
   1. CONFIGURATION & STATE (Run Immediately)
   ========================================= */

// Theme Definitions (Keys match CSS variables directly)
const appThemes = {
    purple: { primary: '#8e44ad', 'primary-dark': '#6c3483', 'primary-light': '#a569bd', secondary: '#e74c3c', accent: '#f39c12' },
    blue: { primary: '#2563eb', 'primary-dark': '#1e40af', 'primary-light': '#60a5fa', secondary: '#0ea5e9', accent: '#22c55e' },
    green: { primary: '#16a34a', 'primary-dark': '#166534', 'primary-light': '#4ade80', secondary: '#22c55e', accent: '#facc15' },
    orange: { primary: '#f97316', 'primary-dark': '#c2410c', 'primary-light': '#fdba74', secondary: '#ef4444', accent: '#f59e0b' }
};


/* =========================================
   2. THEME CONTROLLER
   ========================================= */

function applyThemeVars(themeName) {
    const theme = appThemes[themeName];
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

    // 0. Initialize Dark Mode (Consolidated from ui-utils.js)
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
        document.body.classList.add('dark-mode');
        const icon = document.querySelector('#darkToggle i') || document.querySelector('#theme-toggle i');
        if (icon) {
            icon.classList.remove('fa-moon');
            icon.classList.add('fa-sun');
        }
    }

    // Helper: Update Icon based on Body Class
    const updateToggleIcon = (btn) => {
        const icon = btn.querySelector('i');
        if (!icon) return;
        const isDark = document.body.classList.contains('dark-mode');
        icon.className = isDark ? 'fas fa-sun' : 'fas fa-moon';
        
        if (btn.classList.contains('floating-dark-btn')) {
            btn.style.background = isDark ? '#ffffff' : '#2c3e50';
            btn.style.color = isDark ? '#2c3e50' : '#ffffff';
        }
    };

    // 1. Event Delegation: Handles clicks even if button loads late
    document.addEventListener('click', (e) => {
        const toggleBtn = e.target.closest('#darkToggle, #theme-toggle');
        if (!toggleBtn) return;

        // Toggle State
        const isDark = document.body.classList.toggle('dark-mode');
        localStorage.setItem('theme', isDark ? 'dark' : 'light');

        // Update Icon
        updateToggleIcon(toggleBtn);
    });

    // 2. Create/Manage Floating Button
    const ensureFloatingButton = () => {
        let btn = document.getElementById('darkToggle');
        
        // If button exists but isn't our floating one (e.g. from header), remove it
        if (btn && !btn.classList.contains('floating-dark-btn')) {
            btn.remove();
            btn = null;
        }

        if (!btn) {
            btn = document.createElement('button');
            btn.id = 'darkToggle';
            btn.className = 'floating-dark-btn';
            btn.innerHTML = '<i class="fas fa-moon"></i>';
            btn.setAttribute('aria-label', 'Toggle Dark Mode');
            
            Object.assign(btn.style, {
                position: 'fixed',
                bottom: '20px',
                left: '20px',
                width: '50px',
                height: '50px',
                borderRadius: '50%',
                border: 'none',
                boxShadow: '0 4px 15px rgba(0,0,0,0.3)',
                zIndex: '9999',
                cursor: 'pointer',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                fontSize: '1.2rem',
                transition: 'all 0.3s ease'
            });

            document.body.appendChild(btn);
        }
        
        updateToggleIcon(btn);
    };

    ensureFloatingButton();

    // Watch for header injections (remove duplicate header buttons if they appear)
    const observer = new MutationObserver(() => {
        const btns = document.querySelectorAll('#darkToggle');
        if (btns.length > 1) {
            btns.forEach(b => {
                if (!b.classList.contains('floating-dark-btn')) b.remove();
            });
        } else if (btns.length === 0) {
            ensureFloatingButton();
        }
    });
    
    // Optimization: Observe only the header if possible to avoid performance hits from timers/other changes
    const headerContainer = document.getElementById('header');
    if (headerContainer) {
        observer.observe(headerContainer, { childList: true, subtree: true });
    } else {
        observer.observe(document.body, { childList: true, subtree: true });
    }
});

/* =========================================
   4. SCROLL ANIMATION OBSERVER
   ========================================= */

const initScrollAnimations = () => {
    // Fallback: If IntersectionObserver is missing, show elements immediately
    if (!('IntersectionObserver' in window)) {
        document.querySelectorAll('.animate-on-scroll').forEach(el => el.classList.add('is-visible'));
        return;
    }

    const observerOptions = {
        threshold: 0.1, // Reduced threshold for better mobile triggering
        rootMargin: "0px 0px -20px 0px"
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    const elements = document.querySelectorAll('.animate-on-scroll');
    elements.forEach(el => observer.observe(el));

    // Safety Net: Force visible after 1 second if observer fails or layout shifts
    setTimeout(() => {
        const hidden = document.querySelectorAll('.animate-on-scroll:not(.is-visible)');
        hidden.forEach(el => el.classList.add('is-visible'));
    }, 1000);
};

// Robust initialization: Run immediately if DOM is already ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initScrollAnimations);
} else {
    initScrollAnimations();
}

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
   7. PWA INSTALLATION LOGIC
   ========================================= */

let deferredPrompt;
const installBtnId = 'pwa-install-btn';

window.addEventListener('beforeinstallprompt', (e) => {
    console.log('PWA Install Prompt fired'); // Debugging: Check console to see if this runs
    // Prevent Chrome 67 and earlier from automatically showing the prompt
    e.preventDefault();
    // Stash the event so it can be triggered later.
    deferredPrompt = e;
    // Update UI to notify the user they can add to home screen
    showInstallButton();
});

function showInstallButton() {
    let btn = document.getElementById(installBtnId);

    // Create button if it doesn't exist
    if (!btn) {
        btn = document.createElement('button');
        btn.id = installBtnId;
        btn.className = 'nav-btn'; 
        btn.innerHTML = '<i class="fas fa-download"></i> Install';
        btn.style.cursor = 'pointer';
        btn.style.border = 'none';
        btn.style.marginRight = '10px';
        
        btn.addEventListener('click', async () => {
            if (!deferredPrompt) return;
            deferredPrompt.prompt();
            const { outcome } = await deferredPrompt.userChoice;
            console.log(`User response to the install prompt: ${outcome}`);
            deferredPrompt = null;
            btn.remove();
        });
    }

    const placeButton = () => {
        // Target placement: Beside the mobile menu toggle (inside the controls div)
        const mobileToggle = document.getElementById('mobileMenuToggle') || document.querySelector('.mobile-toggle');
        
        if (mobileToggle && mobileToggle.parentElement) {
            // If button is not already in the correct place, move/insert it
            if (btn.parentElement !== mobileToggle.parentElement) {
                // Reset fixed positioning styles if it was previously a fallback
                btn.style.position = '';
                btn.style.bottom = '';
                btn.style.left = '';
                btn.style.zIndex = '';
                btn.style.boxShadow = '';
                btn.style.marginLeft = '0';

                // Insert before the hamburger menu
                mobileToggle.parentElement.insertBefore(btn, mobileToggle);
            }
            return true;
        }
        return false;
    };

    if (!placeButton()) {
        // Fallback: If header isn't loaded yet, show fixed at bottom left
        if (!document.body.contains(btn)) {
            btn.style.position = 'fixed';
            btn.style.bottom = '90px';
            btn.style.left = '20px';
            btn.style.zIndex = '1000';
            btn.style.boxShadow = '0 4px 15px rgba(0,0,0,0.3)';
            document.body.appendChild(btn);
        }

        // Watch for header injection to move button to correct place
        const observer = new MutationObserver((mutations, obs) => {
            if (placeButton()) obs.disconnect();
        });
        observer.observe(document.body, { childList: true, subtree: true });
    }
}

// Re-run logic after page load to ensure button moves to header if it was fixed
window.addEventListener('load', () => {
    if (deferredPrompt) {
        showInstallButton();
    }
});

window.addEventListener('appinstalled', () => {
    // Hide the app-provided install promotion
    const btn = document.getElementById(installBtnId);
    if (btn) {
         const container = btn.closest('li');
         if (container) container.remove();
         else btn.remove();
    }
    deferredPrompt = null;
    console.log('PWA was installed');
});

/* =========================================
   8. SHARE BUTTON LOGIC
   ========================================= */

const initShareButton = () => {
    // Feature detection: Web Share API (Mobile & supported desktops)
    if (!navigator.share) return;

    const placeBtn = () => {
        // Target the mobile navigation menu list
        const navList = document.querySelector('nav ul');
        if (!navList) return false;

        const shareBtnId = 'pwa-share-btn-mobile';
        if (document.getElementById(shareBtnId)) return true;

        const li = document.createElement('li');
        li.className = 'nav-mobile'; // Only show on mobile
        
        const btn = document.createElement('button');
        btn.id = shareBtnId;
        btn.className = 'nav-mobile-link';
        btn.innerHTML = 'Share App <i class="fas fa-share-alt"></i>';
        btn.style.width = '100%';
        btn.style.cursor = 'pointer';
        
        btn.addEventListener('click', () => {
            navigator.share({
                title: document.title || 'SJMaths',
                text: 'Check out SJMaths - Master Mathematics!',
                url: window.location.href
            }).catch(err => console.log('Share failed:', err));
        });

        li.appendChild(btn);
        navList.appendChild(li);
        return true;
    };

    // Try immediately
    if (!placeBtn()) {
        // Wait for header to load (if dynamic)
        const observer = new MutationObserver((mutations, obs) => {
            if (placeBtn()) obs.disconnect();
        });
        observer.observe(document.body, { childList: true, subtree: true });
    }
};

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initShareButton);
} else {
    initShareButton();
}

/* =========================================
   11. LAUNCH DAY CELEBRATION
   ========================================= */

const initCelebration = () => {
    // Only run on homepage
    const isHomePage = window.location.pathname === '/' || window.location.pathname.endsWith('/index.html');
    if (!isHomePage) return;

    // Check if confetti library is loaded
    if (typeof confetti === 'function') {
        
        // --- TESTING: Uncomment the line below to force animation on every reload ---
        // sessionStorage.removeItem('sjmaths_launch_celebrated');

        // Run only once per session to avoid annoyance
        if (sessionStorage.getItem('sjmaths_launch_celebrated')) {
            console.log('🎉 Launch celebration skipped (already shown this session).');
            return;
        }
        
        sessionStorage.setItem('sjmaths_launch_celebrated', 'true');
        console.log('🚀 Launch celebration started!');

        // Show Welcome Toast
        if (window.showToast) {
            setTimeout(() => window.showToast("Welcome to SJMaths! 🚀", "success"), 500);
        }

        const duration = 3000;
        const end = Date.now() + duration;
        const colors = ['#8e44ad', '#9b59b6', '#f39c12', '#e74c3c', '#ffffff'];

        (function frame() {
            confetti({
                particleCount: 3,
                angle: 60,
                spread: 55,
                origin: { x: 0 },
                colors: colors,
                zIndex: 10001 // Above header
            });
            confetti({
                particleCount: 3,
                angle: 120,
                spread: 55,
                origin: { x: 1 },
                colors: colors,
                zIndex: 10001
            });

            if (Date.now() < end) {
                requestAnimationFrame(frame);
            }
        }());
    }
};

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initCelebration);
} else {
    initCelebration();
}