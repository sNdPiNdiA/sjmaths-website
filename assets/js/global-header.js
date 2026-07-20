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

    /* =========================================================
       USER ANALYTICS & ENGAGEMENT TRACKING
       ========================================================= */
    function initUserAnalytics() {
        // 1. Get or create User ID
        let userId = localStorage.getItem('sj_uid');
        if (!userId) {
            userId = 'user_' + Math.random().toString(36).substr(2, 9) + '_' + Date.now();
            localStorage.setItem('sj_uid', userId);
        }

        // 2. Microsoft Clarity
        if (window.clarity) {
            window.clarity("set", "userId", userId);
        } else {
            window.addEventListener('load', () => {
                if (window.clarity) window.clarity("set", "userId", userId);
            });
        }

        // 3. Page Tracking State
        const pageUrl = window.location.pathname;
        const referrerUrl = document.referrer || "direct";
        let startTime = Date.now();
        let totalActiveTime = 0;
        let lastVisibilityChange = startTime;
        let maxScrollDepth = 0;
        let hasSentAnalytics = false;
        const projectId = "sjmaths-web"; 

        // Update lastActive for registered users only (throttle to once every 5 minutes)
        if (!userId.startsWith('user_')) {
            let lastUpdate = sessionStorage.getItem('sj_last_active');
            if (!lastUpdate || (Date.now() - parseInt(lastUpdate)) > 5 * 60 * 1000) {
                const patchUrl = `https://firestore.googleapis.com/v1/projects/${projectId}/databases/(default)/documents/users/${userId}?updateMask.fieldPaths=lastActive`;
                const patchPayload = { fields: { lastActive: { timestampValue: new Date().toISOString() } } };
                fetch(patchUrl, { method: 'PATCH', body: JSON.stringify(patchPayload), keepalive: true }).catch(e=>{});
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

        // Scroll tracking
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

        // Click Tracking
        window.trackSJEvent = function(actionType, elementText = "", details = {}) {
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
            method: 'POST', body: JSON.stringify(payload), keepalive: true }).catch(e => {});
        };

        document.addEventListener("click", (e) => {
            let target = e.target.closest("button, a, .btn, .cta");
            if (target) {
                let text = target.innerText || target.value || target.title || target.id || "unknown";
                text = text.trim();
                if (text) window.trackSJEvent("click", text);
            }
        });

        // 4. Send Data to Firestore on Exit
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
                fetch(firebaseUrl, { method: 'POST', body: JSON.stringify(payload), keepalive: true }).catch(e => {});
            }
        }
        
        window.addEventListener("pagehide", sendAnalytics);
        window.addEventListener("beforeunload", sendAnalytics);

        // 5. GA4 Tagging (if gtag exists)
        if (typeof gtag === 'function') {
            gtag('config', 'G-K326N2KJ2G', { 'user_id': userId });
        } else {
            window.addEventListener('load', () => {
                if (typeof gtag === 'function') gtag('config', 'G-K326N2KJ2G', { 'user_id': userId });
            });
        }
    }

    // Initialize tracking after main thread frees up
    if ('requestIdleCallback' in window) {
        requestIdleCallback(initUserAnalytics);
    } else {
        setTimeout(initUserAnalytics, 1500);
    }

})();
