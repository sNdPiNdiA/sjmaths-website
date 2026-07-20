/**
 * Global Header Component - SJMaths Website
 * Injects the standard glass-morphism header into #header-container
 */

(function () {
    'use strict';

    function initGlobalHeader() {
        // If a static placeholder header exists, remove it so we can inject the dynamic one
        const existingHeader = document.getElementById('site-header');
        if (existingHeader && !existingHeader.classList.contains('glass-header')) {
            existingHeader.remove();
        } else if (existingHeader) {
            return; // Already injected
        }
        
        if (document.getElementById('exercise-page-header')) return;

        const container = document.getElementById('header-container');
        if (!container) {
            console.warn('SJMaths: #header-container not found. Creating one.');
            // Only creating if absent, but usually it should be present in the HTML skeleton
            const newContainer = document.createElement('div');
            newContainer.id = 'header-container';
            document.body.insertBefore(newContainer, document.body.firstChild);
        }

        const headerHTML = `
        <header class="glass-header notranslate" id="site-header">
            <div class="header-container">
                <!-- Left: Logo -->
                <div class="header-left">
                    <a href="/" class="logo">
                        <span class="logo-symbol">&int;</span> SJMaths
                    </a>
                </div>

                <!-- Center: Search (Desktop) / Right (Mobile) -->
                <div class="header-center">
                    <div class="header-search">
                        <label for="site-search" class="sr-only">Search</label>
                        <button type="button" aria-label="Search">
                            <i class="fas fa-search search-icon"></i>
                        </button>
                        <input type="text" id="site-search" placeholder="Search topics...">
                    </div>
                </div>

                <!-- Right: Actions -->
                <div class="header-right">
            <nav class="desktop-nav" id="primary-navigation">
                <ul>
                    <li><a href="/">Home</a></li>
                    <li><a href="/class-9-maths/">Class 9</a></li>
                    <li><a href="/class-10-maths/">Class 10</a></li>
                    <li><a href="/class-11-maths/">Class 11</a></li>
                    <li><a href="/class-12-maths/">Class 12</a></li>
                    <li><a href="/competitive-exams/">Competitive Exams</a></li>
                    <li><a href="/current-affairs/">Current Affairs</a></li>
                    <li><a href="/app/index.html#/app/learn" style="color: var(--primary); font-weight: bold;"><i class="fas fa-rocket"></i> App</a></li>
                </ul>
            </nav>
            
            <div class="header-actions">
                    <div class="mobile-actions">
                        <button type="button" id="mobileSearchBtn" class="mobile-icon-btn" aria-label="Search">
                            <i class="fas fa-search"></i>
                        </button>
                </div>

                <button type="button" id="headerLangToggleBtn" class="lang-toggle-btn" aria-label="Switch Language" onclick="window.toggleLanguage?.()" style="background:transparent; border:none; color:var(--text-dark); cursor:pointer; font-size:0.95rem; display:inline-flex; align-items:center; gap:6px; margin-right:12px; font-family:'Outfit',sans-serif; font-weight:600; padding:6px 12px; border-radius:20px; transition:background 0.3s;">
                    <i class="fas fa-globe"></i>
                    <span id="headerLangText">हिन्दी</span>
                </button>

                <a href="/login.html" class="auth-btn-pill" id="authBtn">Login</a>
            </div>
            
            <button type="button" class="mobile-toggle" aria-label="Open navigation menu" aria-controls="primary-navigation" aria-expanded="false">
                <i class="fas fa-bars"></i>
            </button>
        </div>
    </div>
    
</header>`;

        // Inject the HTML
        const targetContainer = document.getElementById('header-container');
        targetContainer.innerHTML = headerHTML;

        // Initialize Lang Toggle Text
        const headerLangText = targetContainer.querySelector('#headerLangText');
        if (headerLangText) {
            const isCurrentlyHindi = window.location.pathname.includes('/hi/') || document.documentElement.lang === 'hi';
            headerLangText.textContent = isCurrentlyHindi ? 'English' : 'हिन्दी';
        }


        // Highlight Active Link
        const currentPath = window.location.pathname;
        const navLinks = targetContainer.querySelectorAll('.desktop-nav a');

        navLinks.forEach(link => {
            const linkPath = link.getAttribute('href');
            // Exact match or sub-directory match for classes
            if (pathMatches(currentPath, linkPath)) {
                link.classList.add('active');
            }
        });

    }

    function pathMatches(current, link) {
        if (link === '/' && current === '/') return true;
        if (link === '/' && (current === '/index.html' || current === '')) return true;
        if (link !== '/' && current.startsWith(link)) return true;
        if (link.endsWith('index.html')) {
            const dir = link.replace('index.html', '');
            if (current.startsWith(dir)) return true;
        }
        return false;
    }

    // Initialize
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initGlobalHeader);
    } else {
        initGlobalHeader();
    }

})();
