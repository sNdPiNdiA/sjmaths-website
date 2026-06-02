/**
 * Global Header Component - SJMaths Website
 * Injects the standard glass-morphism header into #header-container
 */

(function () {
    'use strict';

    function initGlobalHeader() {
        // Prevent duplicate - Check for ANY header
        if (document.getElementById('site-header') || document.getElementById('exercise-page-header')) return;

        const container = document.getElementById('header-container');
        if (!container) {
            console.warn('SJMaths: #header-container not found. Creating one.');
            // Only creating if absent, but usually it should be present in the HTML skeleton
            const newContainer = document.createElement('div');
            newContainer.id = 'header-container';
            document.body.insertBefore(newContainer, document.body.firstChild);
        }

        const headerHTML = `
        <header class="glass-header" id="site-header">
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
                    <li><a href="/"><span class="lang-hi">मुख्य पृष्ठ</span><span class="lang-en">Home</span></a></li>
                    <li><a href="/class-9-maths/"><span class="lang-hi">कक्षा 9</span><span class="lang-en">Class 9</span></a></li>
                    <li><a href="/class-10-maths/"><span class="lang-hi">कक्षा 10</span><span class="lang-en">Class 10</span></a></li>
                    <li><a href="/class-11-maths/"><span class="lang-hi">कक्षा 11</span><span class="lang-en">Class 11</span></a></li>
                    <li><a href="/class-12-maths/"><span class="lang-hi">कक्षा 12</span><span class="lang-en">Class 12</span></a></li>
                    <li><a href="/ssc-cgl/syllabus/"><span class="lang-hi">एसएससी सीजीएल</span><span class="lang-en">SSC CGL</span></a></li>
                    <li><a href="/current-affairs/"><span class="lang-hi">समसामयिकी</span><span class="lang-en">Current Affairs</span></a></li>
                </ul>
            </nav>
            
            <div class="header-actions">
                    <div class="mobile-actions">
                        <button type="button" id="mobileSearchBtn" class="mobile-icon-btn" aria-label="Search">
                            <i class="fas fa-search"></i>
                        </button>
                </div>

                <a href="/login.html" class="auth-btn-pill" id="authBtn"><span class="lang-hi">लॉगिन</span><span class="lang-en">Login</span></a>
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
