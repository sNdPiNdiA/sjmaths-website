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
                    <nav class="desktop-nav">
                        <ul>
                            <li><a href="/">Home</a></li>
                            <li><a href="/classes/class-9/index.html">Class 9</a></li>
                            <li><a href="/classes/class-10/index.html">Class 10</a></li>
                            <li><a href="/classes/class-11/index.html">Class 11</a></li>
                            <li><a href="/classes/class-12/index.html">Class 12</a></li>
                        </ul>
                    </nav>
            
            <div class="region-wrapper">
                <i class="fas fa-globe"></i>
                <select id="region-switcher" class="region-select" aria-label="Language Selector">
                    <option value="in" selected>India (English)</option>
                    <option value="global">Global (English)</option>
                    <option value="hi">India (Hindi)</option>
                </select>
            </div>

            <a href="/login.html" class="auth-btn-pill" id="authBtn">Login</a>
            <div class="mobile-toggle"><i class="fas fa-bars"></i></div>
        </div>
    </div>
    
    <!-- Hidden Google Translate Widget and styling to prevent banner push -->
    <div id="google_translate_element" style="display:none;"></div>
    <style>
        body { top: 0 !important; }
        .goog-te-banner-frame.skiptranslate { display: none !important; }
        .goog-te-gadget { display: none !important; }
    </style>
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

        // --- Google Translate Integration ---
        // Prevent injecting the script multiple times (solves 429 Too Many Requests)
        if (!document.getElementById('google-translate-script')) {
            window.googleTranslateElementInit = function () {
                new google.translate.TranslateElement({
                    pageLanguage: 'en',
                    includedLanguages: 'en,hi',
                    autoDisplay: false
                }, 'google_translate_element');
            };

            const gtScript = document.createElement('script');
            gtScript.id = 'google-translate-script';
            gtScript.src = '//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit';
            gtScript.defer = true;
            document.body.appendChild(gtScript);
        }

        const regionSwitcher = document.getElementById('region-switcher');
        if (regionSwitcher) {
            // Restore selection from google translate cookie (googtrans=/en/hi)
            const match = document.cookie.match(/(^|;) ?googtrans=([^;]*)(;|$)/);
            if (match && match[2]) {
                const activeLang = match[2].split('/')[2];
                if (activeLang === 'hi') {
                    regionSwitcher.value = 'hi';
                }
            }

            regionSwitcher.addEventListener('change', (e) => {
                const tgtLang = e.target.value === 'hi' ? 'hi' : 'en';
                const teCombo = document.querySelector('.goog-te-combo');

                if (teCombo) {
                    teCombo.value = tgtLang;
                    teCombo.dispatchEvent(new Event('change'));
                } else {
                    // Fallback to cookie
                    if (tgtLang === 'en') {
                        document.cookie = 'googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';
                        document.cookie = 'googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; domain=.' + window.location.hostname + '; path=/;';
                    } else {
                        document.cookie = 'googtrans=/en/' + tgtLang + '; path=/';
                        document.cookie = 'googtrans=/en/' + tgtLang + '; domain=.' + window.location.hostname + '; path=/';
                    }
                    window.location.reload();
                }
            });
        }
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
