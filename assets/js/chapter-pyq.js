/**
 * SJMaths - ICSE Class 10 Maths Chapter-Wise PYQ Practice Modules
 * Common interactive behaviors, solution accordion metrics, and deferred telemetry.
 */
(function () {
  'use strict';

  // 1. Deferred Firebase Telemetry & Analytics
  function initAnalytics() {
    var load = function () {
      try {
        import('/assets/js/firebase-analytics-only.min.js?v=b9396571');
      } catch (e) {
        console.debug('Analytics deferred');
      }
    };
    if ('requestIdleCallback' in window) {
      window.requestIdleCallback(load);
    } else {
      setTimeout(load, 3000);
    }
  }

  // 2. Deep Linking / Target Anchor Highlighting
  function initAnchorScroll() {
    if (window.location.hash) {
      try {
        var el = document.querySelector(window.location.hash);
        if (el) {
          setTimeout(function () {
            el.scrollIntoView({ behavior: 'smooth', block: 'start' });
          }, 150);
        }
      } catch (err) {}
    }
  }

  // 3. Solution Drawer Accessibility & Interaction
  function initSolutionDrawers() {
    var details = document.querySelectorAll('details.solution-drawer');
    details.forEach(function (drawer) {
      drawer.addEventListener('toggle', function () {
        if (drawer.open) {
          // Re-render KaTeX if new elements are revealed (failsafe)
          if (window.renderMathInElement) {
            var body = drawer.querySelector('.solution-body');
            if (body && !body.dataset.katexRendered) {
              window.renderMathInElement(body, {
                delimiters: [
                  { left: '$$', right: '$$', display: true },
                  { left: '$', right: '$', display: false }
                ]
              });
              body.dataset.katexRendered = 'true';
            }
          }
        }
      });
    });
  }

  // Initialize
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () {
      initAnalytics();
      initAnchorScroll();
      initSolutionDrawers();
    });
  } else {
    initAnalytics();
    initAnchorScroll();
    initSolutionDrawers();
  }
})();

