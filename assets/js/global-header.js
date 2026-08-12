/**
 * Global Header Component - SJMaths Website
 * Injects the redesigned glass-morphism header into #header-container
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
            const newContainer = document.createElement('div');
            newContainer.id = 'header-container';
            document.body.insertBefore(newContainer, document.body.firstChild);
        }

        const headerHTML = `
        <header class="glass-header notranslate" id="site-header">
            <div class="header-container">
                <!-- Left: Logo with Mathematical Integral Symbol -->
                <div class="header-left">
                    <a href="/" class="logo" aria-label="SJMaths Homepage">
                        <span class="logo-integral">&int;</span>
                        <span class="logo-text">SJMaths</span>
                    </a>
                </div>

                <!-- Center: Desktop Search Trigger -->
                <div class="header-center">
                    <div class="header-search-bar" id="headerSearchBox" role="button" tabindex="0" aria-label="Search topics, chapters and exams">
                        <i class="fas fa-search search-icon"></i>
                        <span class="search-placeholder">Search topics, formulas, exams...</span>
                        <span class="search-kbd-pill"><kbd>Ctrl</kbd> <kbd>K</kbd></span>
                    </div>
                </div>

                <!-- Right: Navigation, Utilities & Actions -->
                <div class="header-right">
                    <nav class="desktop-nav" id="primary-navigation" aria-label="Main Navigation">
                        <ul>
                            <li><a href="/" class="nav-link">Home</a></li>
                            <li><a href="/pages/index.html" class="nav-link">Classes</a></li>
                            <li><a href="/competitive-exams/" class="nav-link">Exams</a></li>
                            <li><a href="/current-affairs/" class="nav-link">Current Affairs</a></li>
                            <li><a href="/pages/pricing.html" class="nav-link nav-link-live"><span class="live-dot"></span> Live Batches</a></li>
                            <li><a href="/pages/ebooks.html" class="nav-link">E-Books</a></li>
                            <li><a href="/smart-learning/" class="nav-link nav-link-app"><i class="fas fa-rocket"></i> App</a></li>
                        </ul>
                    </nav>

                    <div class="header-actions">
                        <!-- Mobile Search Trigger -->
                        <div class="mobile-actions">
                            <button type="button" id="mobileSearchBtn" class="header-icon-btn" aria-label="Search">
                                <i class="fas fa-search"></i>
                            </button>
                        </div>

                        <!-- Bilingual Language Toggle -->
                        <button type="button" id="headerLangToggleBtn" class="lang-toggle-btn" aria-label="Switch Language" onclick="window.toggleLanguage?.()">
                            <i class="fas fa-globe"></i>
                            <span id="headerLangText">हिन्दी</span>
                        </button>

                        <!-- Auth / Login -->
                        <a href="/login.html" class="auth-btn-pill" id="authBtn">
                            <i class="fas fa-user-circle"></i> Login
                        </a>

                        <!-- Mobile Hamburger Toggle -->
                        <button type="button" class="mobile-toggle" aria-label="Open navigation menu" aria-controls="primary-navigation" aria-expanded="false">
                            <i class="fas fa-bars"></i>
                        </button>
                    </div>
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

        // Initialize Search Trigger
        const headerSearchBox = targetContainer.querySelector('#headerSearchBox');
        if (headerSearchBox) {
            headerSearchBox.addEventListener('click', () => {
                if (typeof window.openSearch === 'function') {
                    window.openSearch();
                } else {
                    const searchInput = document.getElementById('site-search') || document.querySelector('.header-search input');
                    if (searchInput) {
                        searchInput.focus();
                    } else {
                        window.location.href = '/search.html';
                    }
                }
            });
            headerSearchBox.addEventListener('keydown', (e) => {
                if (e.key === 'Enter' || e.key === ' ') {
                    e.preventDefault();
                    headerSearchBox.click();
                }
            });
        }

        // Highlight Active Link
        const currentPath = window.location.pathname;
        const navLinks = targetContainer.querySelectorAll('.desktop-nav a');

        navLinks.forEach(link => {
            const linkPath = link.getAttribute('href');
            if (pathMatches(currentPath, linkPath)) {
                link.classList.add('active');
            }
        });
    }

    function pathMatches(current, link) {
        if (link === '/' && (current === '/' || current === '/index.html' || current === '')) return true;
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

    /* =========================================================
       USER ANALYTICS & ENGAGEMENT TRACKING
       ========================================================= */
    function initUserAnalytics() {
        let userId = localStorage.getItem('sj_uid');
        if (!userId) {
            userId = 'user_' + Math.random().toString(36).substr(2, 9) + '_' + Date.now();
            localStorage.setItem('sj_uid', userId);
        }

        if (window.clarity) {
            window.clarity("set", "userId", userId);
        } else {
            window.addEventListener('load', () => {
                if (window.clarity) window.clarity("set", "userId", userId);
            });
        }

        const pageUrl = window.location.pathname;
        const referrerUrl = document.referrer || "direct";
        let startTime = Date.now();
        let totalActiveTime = 0;
        let lastVisibilityChange = startTime;
        let maxScrollDepth = 0;
        let hasSentAnalytics = false;
        const projectId = "sjmaths-web";

        if (!userId.startsWith('user_')) {
            let lastUpdate = sessionStorage.getItem('sj_last_active');
            if (!lastUpdate || (Date.now() - parseInt(lastUpdate)) > 5 * 60 * 1000) {
                const patchUrl = `https://firestore.googleapis.com/v1/projects/${projectId}/databases/(default)/documents/users/${userId}?updateMask.fieldPaths=lastActive`;
                const patchPayload = { fields: { lastActive: { timestampValue: new Date().toISOString() } } };
                fetch(patchUrl, { method: 'PATCH', body: JSON.stringify(patchPayload), keepalive: true }).catch(e => { });
                sessionStorage.setItem('sj_last_active', Date.now().toString());
            }
        }

        function updateActiveTime() {
            if (!document.hidden) {
                lastVisibilityChange = Date.now();
            } else {
                totalActiveTime += (Date.now() - lastVisibilityChange);
            }
        }

        document.addEventListener("visibilitychange", updateActiveTime);

        let scrollTimeout;
        window.addEventListener("scroll", () => {
            if (!scrollTimeout) {
                scrollTimeout = setTimeout(() => {
                    let scrollPercent = Math.round((window.scrollY + window.innerHeight) / document.documentElement.scrollHeight * 100);
                    if (scrollPercent > maxScrollDepth) {
                        maxScrollDepth = scrollPercent > 100 ? 100 : scrollPercent;
                    }
                    scrollTimeout = null;
                }, 200);
            }
        });

        window.trackSJEvent = function (actionType, elementText = "", details = {}) {
            const payload = {
                fields: {
                    userId: { stringValue: userId },
                    page: { stringValue: pageUrl },
                    actionType: { stringValue: actionType },
                    elementText: { stringValue: elementText.substring(0, 100) },
                    timestamp: { timestampValue: new Date().toISOString() }
                }
            };
            if (Object.keys(details).length > 0) {
                payload.fields.details = { stringValue: JSON.stringify(details) };
            }
            const firebaseUrl = `https://firestore.googleapis.com/v1/projects/${projectId}/databases/(default)/documents/users/${userId}/user_actions`;
            fetch(firebaseUrl, {
                method: 'POST', body: JSON.stringify(payload), keepalive: true
            }).catch(e => { });
        };

        document.addEventListener("click", (e) => {
            let target = e.target.closest("button, a, .btn, .cta");
            if (target) {
                let text = target.innerText || target.value || target.title || target.id || "unknown";
                text = text.trim();
                if (text) window.trackSJEvent("click", text);
            }
        });

        function sendAnalytics() {
            if (hasSentAnalytics) return;
            hasSentAnalytics = true;

            if (!document.hidden) {
                totalActiveTime += (Date.now() - lastVisibilityChange);
            }

            const payload = {
                fields: {
                    userId: { stringValue: userId },
                    page: { stringValue: pageUrl },
                    referrer: { stringValue: referrerUrl },
                    activeSeconds: { integerValue: Math.floor(totalActiveTime / 1000).toString() },
                    maxScrollDepth: { integerValue: maxScrollDepth.toString() },
                    timestamp: { timestampValue: new Date().toISOString() }
                }
            };

            const firebaseUrl = `https://firestore.googleapis.com/v1/projects/${projectId}/databases/(default)/documents/users/${userId}/page_views`;

            if (navigator.sendBeacon) {
                navigator.sendBeacon(firebaseUrl, JSON.stringify(payload));
            } else {
                fetch(firebaseUrl, { method: 'POST', body: JSON.stringify(payload), keepalive: true }).catch(e => { });
            }
        }

        window.addEventListener("pagehide", sendAnalytics);
        window.addEventListener("beforeunload", sendAnalytics);

        if (typeof gtag === 'function') {
            gtag('config', 'G-K326N2KJ2G', { 'user_id': userId });
        } else {
            window.addEventListener('load', () => {
                if (typeof gtag === 'function') gtag('config', 'G-K326N2KJ2G', { 'user_id': userId });
            });
        }
    }

    if ('requestIdleCallback' in window) {
        requestIdleCallback(initUserAnalytics);
    } else {
        setTimeout(initUserAnalytics, 1500);
    }

})();
