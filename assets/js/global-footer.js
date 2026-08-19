/**
 * Global Footer Component - SJMaths Website
 * Compact mobile-first footer with horizontal inline links
 */

(function () {
    'use strict';

    function initGlobalFooter() {
        // Prevent duplicate
        if (document.getElementById('site-footer')) return;

        const container = document.getElementById('footer-container');
        if (!container) {
            console.warn('SJMaths: #footer-container not found. Appending one.');
            const newContainer = document.createElement('div');
            newContainer.id = 'footer-container';
            document.body.appendChild(newContainer);
        }

        const footerHTML = `
        <style>
          .sf { background: var(--surface, #fff); padding: 2rem 1rem 1.2rem; margin-top: auto; border-top: 1px solid rgba(0,0,0,.05); }
          .sf-inner { max-width: 1200px; margin: 0 auto; }
          /* Desktop: grid */
          .sf-grid { display: grid; grid-template-columns: 1.4fr 1fr 1fr 1fr; gap: 2rem; }
          .sf-brand-name { font-size: 1.4rem; font-weight: 800; color: var(--primary-600, #6f42c1); text-decoration: none; display: inline-flex; align-items: center; gap: .4rem; }
          .sf-brand-name span { color: var(--primary-500, #059669); font-size: 1.7rem; }
          .sf-desc { color: var(--muted, #6b7280); font-size: .88rem; line-height: 1.55; margin: .6rem 0 1rem; }
          .sf-social { display: flex; gap: .8rem; }
          .sf-social .social-link { color: var(--muted, #6b7280); font-size: 1.1rem; }
          .sf h4 { font-size: .95rem; font-weight: 700; margin-bottom: .8rem; color: var(--text-dark, #1f2937); }
          .sf-links { list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: .5rem; }
          .sf-links a { color: var(--muted, #6b7280); text-decoration: none; font-size: .88rem; transition: color .2s; }
          .sf-links a:hover { color: var(--primary-500, #059669); }
          .sf-contact-item { display: flex; align-items: center; gap: 8px; color: var(--muted, #6b7280); font-size: .88rem; }
          .sf-contact-item i { color: var(--primary-500, #059669); font-size: .85rem; }
          .sf-contact-item a { color: inherit; text-decoration: none; }
          .sf-bottom { margin-top: 1.5rem; padding-top: 1rem; border-top: 1px solid rgba(0,0,0,.05); color: var(--muted, #6b7280); font-size: .8rem; text-align: center; }

          /* MOBILE: compact horizontal layout */
          @media (max-width: 640px) {
            .sf { padding: 1.2rem 1rem .8rem; }
            .sf-grid { grid-template-columns: 1fr; gap: 0; text-align: center; }
            .sf-brand-col { padding-bottom: .8rem; border-bottom: 1px solid rgba(0,0,0,.04); margin-bottom: .6rem; }
            .sf-desc { font-size: .8rem; margin: .4rem 0 .6rem; }
            .sf-social { justify-content: center; gap: 1rem; }
            .sf h4 { font-size: .8rem; margin-bottom: .4rem; text-transform: uppercase; letter-spacing: .5px; color: var(--muted, #6b7280); }
            .sf-links { flex-direction: row; flex-wrap: wrap; justify-content: center; gap: .2rem .6rem; }
            .sf-links li { display: inline; }
            .sf-links a { font-size: .78rem; }
            .sf-links li:not(:last-child)::after { content: " · "; color: var(--muted, #6b7280); opacity: .4; margin-left: .3rem; }
            .sf-link-col { padding: .5rem 0; }
            .sf-contact-col { padding: .5rem 0; }
            .sf-contact-col .sf-links { gap: .3rem .8rem; }
            .sf-contact-item { justify-content: center; font-size: .78rem; }
            .sf-bottom { margin-top: .8rem; padding-top: .6rem; font-size: .72rem; }
          }
        </style>
        <footer id="site-footer" class="sf notranslate">
          <div class="sf-inner">
            <div class="sf-grid">
              <div class="sf-brand-col">
                <a href="/" class="sf-brand-name"><span>&int;</span> SJMaths</a>
                <p class="sf-desc">Empowering students with comprehensive resources to master mathematics and excel in exams.</p>
                <div class="sf-social">
                  <span class="social-link" aria-label="Facebook"><i class="fab fa-facebook"></i></span>
                  <span class="social-link" aria-label="Twitter"><i class="fab fa-twitter"></i></span>
                  <span class="social-link" aria-label="Instagram"><i class="fab fa-instagram"></i></span>
                  <span class="social-link" aria-label="YouTube"><i class="fab fa-youtube"></i></span>
                </div>
              </div>
              <div class="sf-link-col">
                <h4>Quick Links</h4>
                <ul class="sf-links">
                  <li><a href="/">Home</a></li>
                  <li><a href="/pages/about">About</a></li>
                  <li><a href="/pages/contact">Contact</a></li>
                  <li><a href="/pages/privacy-policy">Privacy</a></li>
                  <li><a href="/pages/terms">Terms</a></li>
                  <li><a href="/pages/sitemap">Sitemap</a></li>
                  <li><a href="/current-affairs/">Current Affairs</a></li>
                </ul>
              </div>
              <div class="sf-link-col">
                <h4>Exams &amp; Classes</h4>
                <ul class="sf-links">
                  <li><a href="/competitive-exams/">All Exams</a></li>
                  <li><a href="/ssc-cgl/syllabus/">SSC CGL Prep</a></li>
                  <li><a href="/upsc/">UPSC Prep</a></li>
                  <li><a href="/class-9-maths/">Class 9 Maths</a></li>
                  <li><a href="/class-10-maths/">Class 10 Maths</a></li>
                  <li><a href="/class-11-maths/">Class 11 Maths</a></li>
                  <li><a href="/class-12-maths/">Class 12 Maths</a></li>
                </ul>
              </div>
              <div class="sf-contact-col">
                <h4>Get in Touch</h4>
                <ul class="sf-links">
                  <li class="sf-contact-item"><i class="fas fa-envelope"></i><a href="mailto:support@sjmaths.com">support@sjmaths.com</a></li>
                  <li class="sf-contact-item"><i class="fas fa-phone"></i><a href="tel:+919170940900">+91 9170940900</a></li>
                </ul>
              </div>
            </div>
            <div class="sf-bottom">&copy; ${new Date().getFullYear()} SJMaths. All Rights Reserved.</div>
          </div>
        </footer>`;

        // Inject the HTML
        const targetContainer = document.getElementById('footer-container');
        if (targetContainer) {
            targetContainer.innerHTML = footerHTML;
        }

        // Dynamically inject the mobile bottom navigation globally on all pages
        injectMobileBottomNav();
    }

    function injectMobileBottomNav() {
        if (document.querySelector('.mobile-bottom-nav')) return; // Prevent duplicate

        const nav = document.createElement('div');
        nav.className = 'mobile-bottom-nav';
        nav.setAttribute('role', 'navigation');
        nav.setAttribute('aria-label', 'Mobile Bottom Navigation');

        const currentPath = window.location.pathname;
        const isHome = currentPath === '/' || currentPath === '/index.html' || currentPath.endsWith('/index.html') || currentPath === '';
        const isSearch = currentPath.includes('/search.html');
        const isProfile = currentPath.includes('/profile.html');
        const isCompetitive = currentPath.includes('/competitive-exams') || currentPath.includes('/ssc-cgl') || currentPath.includes('/upsc') || currentPath.includes('/ahc-ro-aro');
        const isClasses = (currentPath.includes('/pages/index.html') || 
                          currentPath.includes('/class-9-maths') || 
                          currentPath.includes('/class-10-maths') || 
                          currentPath.includes('/class-11-maths') || 
                          currentPath.includes('/class-12-maths') || 
                          (currentPath.includes('/pages/') && !isSearch && !isProfile && !currentPath.includes('/about.html') && !currentPath.includes('/contact.html') && !currentPath.includes('/terms.html') && !currentPath.includes('/privacy-policy.html') && !currentPath.includes('/cookie-policy.html'))) && !isCompetitive;

        nav.innerHTML = `
            <a href="/" class="nav-item ${isHome ? 'active' : ''}">
                <i class="fas fa-home"></i>
                <span>Home</span>
            </a>
            <a href="/competitive-exams/" class="nav-item ${isCompetitive ? 'active' : ''}">
                <i class="fas fa-trophy"></i>
                <span>Competitive</span>
            </a>
            <a href="/pages/index.html" class="nav-item ${isClasses ? 'active' : ''}">
                <i class="fas fa-graduation-cap"></i>
                <span>Classes</span>
            </a>
            <a href="/profile.html" class="nav-item ${isProfile ? 'active' : ''}">
                <i class="fas fa-user"></i>
                <span>Profile</span>
            </a>
        `;

        document.body.appendChild(nav);
    }

    // Initialize
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initGlobalFooter);
    } else {
        initGlobalFooter();
    }
})();
