/**
 * ============================================================================
 * SJ Maths — Home Science Topic Page Tabs & Interactive Controller
 * Accessible WAI-ARIA tabs with keyboard navigation and hash syncing
 * ============================================================================
 */

(function () {
  'use strict';

  // Eye-Care Warm & Night Theme Manager
  function initTheme() {
    try {
      const savedTheme = localStorage.getItem('sjmaths-theme');
      if (savedTheme === 'dark') {
        document.body.classList.add('dark-mode');
      }
    } catch (e) {}
    updateThemeToggleLabel();
  }

  function toggleTheme() {
    const isDark = document.body.classList.toggle('dark-mode');
    try {
      localStorage.setItem('sjmaths-theme', isDark ? 'dark' : 'light');
    } catch (e) {}
    updateThemeToggleLabel();
  }

  function updateThemeToggleLabel() {
    const btn = document.getElementById('btn-theme-toggle');
    if (!btn) return;
    const isDark = document.body.classList.contains('dark-mode');
    btn.innerHTML = isDark ? '☀️ दिन मोड' : '🌙 रात्रि मोड';
    btn.setAttribute('aria-label', isDark ? 'दिन मोड सक्रिय करें' : 'रात्रि मोड सक्रिय करें');
  }

  // Bilingual (English / Hindi) Language Manager
  function initLanguage() {
    var savedLang = 'en';
    try {
      savedLang = localStorage.getItem('sjmaths_preferred_language') || 'en';
    } catch (e) {}
    setLanguage(savedLang, false);
  }

  function setLanguage(lang, save) {
    if (lang !== 'hi' && lang !== 'en') lang = 'en';
    document.documentElement.setAttribute('data-lang', lang);
    if (save !== false) {
      try {
        localStorage.setItem('sjmaths_preferred_language', lang);
      } catch (e) {}
    }
    updateLangToggleLabel(lang);
    window.dispatchEvent(new CustomEvent('sjmaths:langchange', { detail: { lang: lang } }));
  }

  function toggleLanguage() {
    var currentLang = document.documentElement.getAttribute('data-lang') || 'en';
    var nextLang = currentLang === 'en' ? 'hi' : 'en';
    setLanguage(nextLang, true);
  }

  function updateLangToggleLabel(lang) {
    var btn = document.getElementById('btn-lang-toggle');
    if (!btn) return;
    btn.innerHTML = lang === 'hi' ? '🌐 <span style="font-weight:900;">हिन्दी</span> (EN)' : '🌐 <span style="font-weight:900;">EN</span> (हिन्दी)';
    btn.setAttribute('aria-label', lang === 'hi' ? 'Switch to English' : 'Switch to Hindi / हिन्दी में देखें');
  }

  document.addEventListener('DOMContentLoaded', function () {
    initTheme();
    initLanguage();

    const themeBtn = document.getElementById('btn-theme-toggle');
    if (themeBtn) {
      themeBtn.addEventListener('click', toggleTheme);
    }
    const langBtn = document.getElementById('btn-lang-toggle');
    if (langBtn) {
      langBtn.addEventListener('click', toggleLanguage);
    }
    const tabList = document.querySelector('[role="tablist"]');
    if (!tabList) return;

    const tabs = Array.from(tabList.querySelectorAll('[role="tab"]'));
    const panels = Array.from(document.querySelectorAll('[role="tabpanel"]'));

    function selectTab(targetTab, updateHash) {
      if (!targetTab) return;

      tabs.forEach(function (tab) {
        const isSelected = tab === targetTab;
        tab.setAttribute('aria-selected', isSelected ? 'true' : 'false');
        tab.setAttribute('tabindex', isSelected ? '0' : '-1');
      });

      const controlsId = targetTab.getAttribute('aria-controls');

      panels.forEach(function (panel) {
        if (panel.id === controlsId) {
          panel.classList.add('active');
          panel.hidden = false;
        } else {
          panel.classList.remove('active');
          panel.hidden = true;
        }
      });

      if (updateHash !== false) {
        const hash = '#' + controlsId;
        if (window.location.hash !== hash) {
          history.replaceState(null, '', hash);
        }
      }

      // Dispatch custom event for engines
      window.dispatchEvent(new CustomEvent('topic:tabchange', {
        detail: { tabId: controlsId }
      }));
    }

    // Click handler
    tabs.forEach(function (tab) {
      tab.addEventListener('click', function () {
        selectTab(tab, true);
      });
    });

    // Keyboard navigation (WAI-ARIA Tabs pattern)
    tabList.addEventListener('keydown', function (e) {
      const activeIdx = tabs.indexOf(document.activeElement);
      if (activeIdx === -1) return;

      let nextIdx = null;

      if (e.key === 'ArrowRight' || e.key === 'ArrowDown') {
        nextIdx = (activeIdx + 1) % tabs.length;
      } else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
        nextIdx = (activeIdx - 1 + tabs.length) % tabs.length;
      } else if (e.key === 'Home') {
        nextIdx = 0;
      } else if (e.key === 'End') {
        nextIdx = tabs.length - 1;
      }

      if (nextIdx !== null) {
        e.preventDefault();
        tabs[nextIdx].focus();
        selectTab(tabs[nextIdx], true);
      }
    });

    // Check URL hash on initial load
    function initFromHash() {
      const hash = window.location.hash.replace('#', '');
      if (hash) {
        const matchingTab = tabs.find(function (t) {
          return t.getAttribute('aria-controls') === hash;
        });
        if (matchingTab) {
          selectTab(matchingTab, false);
          return;
        }
      }
      // Default to the first tab (usually Notes)
      if (tabs.length > 0) {
        selectTab(tabs[0], false);
      }
    }

    window.addEventListener('hashchange', function () {
      initFromHash();
    });

    initFromHash();

    // Client-side math formula and fraction renderer
    function formatMathFormulas() {
      var elements = document.querySelectorAll('.formula-eq, .formula-name, .formula-meta, .prose-content, .summary-container, .trick-shortcut, .feedback-explanation');
      var symbolMap = {
        '\\\\hbar(?![a-zA-Z])': '&#x210f;',
        '\\\\times(?![a-zA-Z])': '&times;',
        '\\\\cdot(?![a-zA-Z])': '&middot;',
        '\\\\pm(?![a-zA-Z])': '&plusmn;',
        '\\\\approx(?![a-zA-Z])': '&asymp;',
        '\\\\propto(?![a-zA-Z])': '&prop;',
        '\\\\infty(?![a-zA-Z])': '&infin;',
        '\\\\Delta(?![a-zA-Z])': '&Delta;',
        '\\\\pi(?![a-zA-Z])': '&pi;',
        '\\\\mu(?![a-zA-Z])': '&mu;',
        '\\\\nu(?![a-zA-Z])': '&nu;',
        '\\\\alpha(?![a-zA-Z])': '&alpha;',
        '\\\\beta(?![a-zA-Z])': '&beta;',
        '\\\\gamma(?![a-zA-Z])': '&gamma;',
        '\\\\theta(?![a-zA-Z])': '&theta;',
        '\\\\lambda(?![a-zA-Z])': '&lambda;',
        '\\\\sigma(?![a-zA-Z])': '&sigma;',
        '\\\\rho(?![a-zA-Z])': '&rho;',
        '\\\\epsilon(?![a-zA-Z])': '&epsilon;',
        '\\\\tau(?![a-zA-Z])': '&tau;',
        '\\\\omega(?![a-zA-Z])': '&omega;',
        '\\\\phi(?![a-zA-Z])': '&phi;',
        '\\\\psi(?![a-zA-Z])': '&psi;',
        '\\\\chi(?![a-zA-Z])': '&chi;',
        '\\\\eta(?![a-zA-Z])': '&eta;',
        '\\\\kappa(?![a-zA-Z])': '&kappa;',
        '\\\\partial(?![a-zA-Z])': '&part;',
        '\\\\sum(?![a-zA-Z])': '&sum;',
        '\\\\int(?![a-zA-Z])': '&int;',
        '\\\\ge(?![a-zA-Z])': '&ge;',
        '\\\\geq(?![a-zA-Z])': '&ge;',
        '\\\\le(?![a-zA-Z])': '&le;',
        '\\\\leq(?![a-zA-Z])': '&le;',
        '\\\\ne(?![a-zA-Z])': '&ne;',
        '\\\\neq(?![a-zA-Z])': '&ne;',
        '\\\\rightarrow(?![a-zA-Z])': '&rarr;',
        '\\\\to(?![a-zA-Z])': '&rarr;',
        '\\\\rightleftharpoons(?![a-zA-Z])': '&#8652;',
        '\\\\AA(?![a-zA-Z])': '&#197;'
      };

      elements.forEach(function (el) {
        var html = el.innerHTML;
        if (!html || (!html.includes('&frac') && !html.includes('\\frac') && !html.includes('\\sqrt') && !html.includes('\\') && !html.includes('_') && !html.includes('^'))) {
          return;
        }

        html = html.replace(/\\text\{([^{}]+)\}/g, '$1');
        html = html.replace(/\\left\(/g, '(').replace(/\\right\)/g, ')').replace(/\\left\[/g, '[').replace(/\\right\]/g, ']');

        for (var pattern in symbolMap) {
          html = html.replace(new RegExp(pattern, 'g'), symbolMap[pattern]);
        }

        html = html.replace(/\\sqrt\{([^{}]+)\}/g, '<span class="math-sqrt">&radic;<span class="math-radicand">$1</span></span>');
        html = html.replace(/(?:&frac|\\frac)\{1\}\{2\}\s*([a-zA-Z])/g, '&frac12; $1');
        html = html.replace(/(?:&frac|\\frac)\{1\}\{2\}/g, '&frac12;');
        html = html.replace(/<span class="math-frac">\s*<span class="math-num">1<\/span>\s*<span class="math-denom">2<\/span>\s*<\/span>\s*([a-zA-Z])/g, '&frac12; $1');

        var changed = true;
        var safety = 0;
        while (changed && safety < 10) {
          changed = false;
          safety++;
          var nextHtml = html.replace(/(?:&frac|\\frac)\{([^{}]+)\}\{([^{}]+)\}/g, function (_, num, denom) {
            changed = true;
            return '<span class="math-frac"><span class="math-num">' + num + '</span><span class="math-denom">' + denom + '</span></span>';
          });
          html = nextHtml;
        }

        // Subscripts and superscripts attached to tokens
        html = html.replace(/([a-zA-Z0-9\)\]\}\&;\>])_\{([^{}]+)\}/g, '$1<sub>$2</sub>');
        html = html.replace(/([a-zA-Z0-9\)\]\}\&;\>])_([a-zA-Z0-9]+)/g, '$1<sub>$2</sub>');
        html = html.replace(/([a-zA-Z0-9\)\]\}\&;\>])\^\{([^{}]+)\}/g, '$1<sup>$2</sup>');
        html = html.replace(/([a-zA-Z0-9\)\]\}\&;\>])\^([0-9\+\-]+)/g, '$1<sup>$2</sup>');

        el.innerHTML = html;
      });
    }

    formatMathFormulas();
  });
})();
