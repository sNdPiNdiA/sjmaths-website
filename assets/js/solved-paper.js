/**
 * SJMaths - ICSE Class 10 Maths Solved Examination Papers
 * Common interactive behaviors: Section filters, solution toggles, KaTeX render, and telemetry.
 */
(function () {
  'use strict';

  // Failsafe SJ_GLOBAL setup for header/footer components
  if (!window.SJ_GLOBAL) {
    var metaDesc = document.querySelector('meta[name="description"]');
    window.SJ_GLOBAL = {
      title: document.title,
      description: metaDesc ? metaDesc.getAttribute('content') : ''
    };
  }

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

  // 3. Toggle All Solutions (if button present)
  function initSolutionToggles() {
    var toggleBtn = document.getElementById('toggleAllSolBtn') || document.getElementById('toggleAllBtn');
    if (toggleBtn) {
      var allOpen = false;
      toggleBtn.addEventListener('click', function () {
        var drawers = document.querySelectorAll('details.solution-drawer, details.sol-details');
        allOpen = !allOpen;
        drawers.forEach(function (d) {
          if (allOpen) d.setAttribute('open', '');
          else d.removeAttribute('open');
        });
        toggleBtn.innerHTML = allOpen
          ? '<i class="fa-solid fa-eye-slash"></i> Hide All Solutions'
          : '<i class="fa-solid fa-eye"></i> Show All Solutions';
      });
    }

    // Individual details KaTeX fallback
    var allDetails = document.querySelectorAll('details.solution-drawer, details.sol-details');
    allDetails.forEach(function (d) {
      d.addEventListener('toggle', function () {
        if (d.open && window.renderMathInElement) {
          var body = d.querySelector('.solution-body, .sol-content');
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
      });
    });
  }

  // 4. Section A / Section B Filters (if present)
  function initSectionFilters() {
    var secBtns = document.querySelectorAll('.filter-sec-btn');
    var secA = document.getElementById('paper-section-a');
    var secB = document.getElementById('paper-section-b');

    if (secBtns.length && secA && secB) {
      secBtns.forEach(function (btn) {
        btn.addEventListener('click', function () {
          secBtns.forEach(function (b) { b.classList.remove('active'); });
          btn.classList.add('active');
          var sec = btn.getAttribute('data-sec');

          if (sec === 'all') {
            secA.style.display = 'block';
            secB.style.display = 'block';
          } else if (sec === 'secA') {
            secA.style.display = 'block';
            secB.style.display = 'none';
          } else if (sec === 'secB') {
            secA.style.display = 'none';
            secB.style.display = 'block';
          }
        });
      });
    }
  }

  // Initialize
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () {
      initAnalytics();
      initAnchorScroll();
      initSolutionToggles();
      initSectionFilters();
    });
  } else {
    initAnalytics();
    initAnchorScroll();
    initSolutionToggles();
    initSectionFilters();
  }
})();
