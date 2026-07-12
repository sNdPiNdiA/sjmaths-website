/**
 * upsssc-lower.js
 * Shared JavaScript for all UPSSSC Lower Subordinate topic pages.
 * Handles: tab switching, language toggle, timed test engine, practice scoring.
 */

(function () {
    'use strict';

    /* ── Tab Switching ─────────────────────────────────────── */
    window.switchTab = function (tabId) {
        document.querySelectorAll('.tab-content').forEach(function (tab) {
            tab.style.display = 'none';
        });
        document.querySelectorAll('.sub-nav-item').forEach(function (btn) {
            btn.classList.remove('active');
        });
        const targetTab = document.getElementById('tab-' + tabId);
        if (targetTab) {
            targetTab.style.display = 'block';
            targetTab.classList.add('active');
        }
        const activeBtn = document.querySelector('[data-tab="' + tabId + '"]');
        if (activeBtn) activeBtn.classList.add('active');
        window.scrollTo({ top: 0, behavior: 'smooth' });
    };

    /* ── Language Toggle ────────────────────────────────────── */
    window.toggleLang = function () {
        const isHi = document.body.classList.toggle('lang-mode-hi');
        const lang = isHi ? 'hi' : 'en';
        const keys = ['sjmaths_preferred_language', 'sjmaths_ca_lang', 'ssc-cgl-lang'];
        keys.forEach(function (k) { localStorage.setItem(k, lang); });
        const btn = document.querySelector('.lang-toggle-btn');
        if (btn) btn.textContent = isHi ? 'A (En)' : 'A/अ';
        window.location.reload();
    };

    /* ── Difficulty Sub-tabs (Practice tab) ─────────────────── */
    window.switchDifficulty = function (level) {
        document.querySelectorAll('.practice-sub-tab').forEach(function (t) {
            t.style.display = 'none';
        });
        document.querySelectorAll('.practice-difficulty-btn').forEach(function (b) {
            b.classList.remove('active');
        });
        const target = document.getElementById('practice-' + level);
        if (target) target.style.display = 'block';
        const activeBtn = document.querySelector('[data-level="' + level + '"]');
        if (activeBtn) activeBtn.classList.add('active');
    };

    /* ── Timed Test Engine ──────────────────────────────────── */
    var TT = {
        timer: null,
        secs: 900,
        submitted: false,
        totalQ: 15,
        data: []           // populated from HTML via window.upssscTestData
    };

    window.startTest = function () {
        if (window.upssscTestData) TT.data = window.upssscTestData;
        TT.totalQ = TT.data.length;
        TT.secs = TT.totalQ * 60;   // 1 min per question
        TT.submitted = false;

        var startScr = document.getElementById('test-start-scr');
        var testArea = document.getElementById('test-area');
        if (startScr) startScr.style.display = 'none';
        if (testArea) testArea.style.display = 'block';

        _updTmr();
        TT.timer = setInterval(function () {
            TT.secs--;
            _updTmr();
            var pct = (TT.totalQ * 60 - TT.secs) / (TT.totalQ * 60) * 100;
            var fill = document.getElementById('prog-fill');
            if (fill) fill.style.width = pct + '%';
            if (TT.secs <= 0) { clearInterval(TT.timer); submitTest(); }
        }, 1000);
    };

    function _updTmr() {
        var m = Math.floor(TT.secs / 60), s = TT.secs % 60;
        var el = document.getElementById('tmr-display');
        if (el) {
            el.textContent = (m < 10 ? '0' : '') + m + ':' + (s < 10 ? '0' : '') + s;
            el.className = 'test-tmr' + (TT.secs <= 60 ? ' urgent' : '');
        }
    }

    window.selOpt = function (el) {
        if (TT.submitted) return;
        var qi = el.getAttribute('data-qi');
        var block = document.getElementById('tq-' + qi);
        if (block) block.querySelectorAll('.test-opt').forEach(function (o) { o.classList.remove('sel'); });
        el.classList.add('sel');
        var selInput = document.getElementById('tsel-' + qi);
        if (selInput) selInput.value = el.getAttribute('data-ch');
    };

    window.submitTest = function () {
        if (TT.submitted) return;
        TT.submitted = true;
        if (TT.timer) clearInterval(TT.timer);

        var score = 0;
        for (var i = 0; i < TT.totalQ; i++) {
            var sel = document.getElementById('tsel-' + i) ? document.getElementById('tsel-' + i).value : '';
            var cor = TT.data[i] ? TT.data[i].ans : '';
            var block = document.getElementById('tq-' + i);
            if (block) {
                block.querySelectorAll('.test-opt').forEach(function (o) {
                    o.classList.add('no-click');
                    var ch = o.getAttribute('data-ch');
                    if (ch === cor) o.classList.add('ok');
                    else if (ch === sel && sel !== cor) o.classList.add('bad');
                });
                // Inject solution
                var sb = document.createElement('div');
                sb.className = 'test-sol-box';
                sb.style.display = 'block';
                var solEn = TT.data[i] ? TT.data[i].solEn : '';
                var solHi = TT.data[i] ? TT.data[i].solHi : '';
                sb.innerHTML = '<strong><i class="fas fa-lightbulb"></i> Solution:</strong> ' +
                    '<span class="lang-en">' + solEn + '</span>' +
                    '<span class="lang-hi">' + solHi + '</span>';
                block.appendChild(sb);
            }
            if (sel === cor) score++;
        }

        var submitBtn = document.getElementById('submit-btn');
        if (submitBtn) submitBtn.style.display = 'none';

        var rb = document.getElementById('test-result');
        if (rb) rb.style.display = 'block';

        var resScore = document.getElementById('res-score');
        if (resScore) resScore.textContent = score + '/' + TT.totalQ;

        var pct = Math.round(score / TT.totalQ * 100);
        var gr, gs, le, lh;
        if (pct >= 80)      { gr = 'Excellent! ★★★'; gs = '#27ae60'; le = 'Outstanding performance!'; lh = 'शानदार प्रदर्शन!'; }
        else if (pct >= 60) { gr = 'Good! ★★';        gs = '#3498db'; le = 'Good performance!';        lh = 'अच्छा प्रदर्शन!'; }
        else if (pct >= 40) { gr = 'Average ★';        gs = '#e67e22'; le = 'Keep practicing!';         lh = 'अभ्यास जारी रखें!'; }
        else                { gr = 'Need Improvement'; gs = '#e74c3c'; le = 'Revise theory section!';   lh = 'थ्योरी पुनः पढ़ें!'; }

        var ge = document.getElementById('res-grade');
        if (ge) { ge.textContent = gr; ge.style.cssText = 'background:' + gs + ';padding:5px 18px;border-radius:20px;'; }

        var rl = document.getElementById('res-label');
        if (rl) rl.innerHTML = '<span class="lang-en">' + le + '</span><span class="lang-hi">' + lh + '</span>';

        if (rb) rb.scrollIntoView({ behavior: 'smooth', block: 'center' });
    };

    window.retakeTest = function () {
        TT.submitted = false;
        var result = document.getElementById('test-result');
        var submitBtn = document.getElementById('submit-btn');
        var testArea = document.getElementById('test-area');
        var startScr = document.getElementById('test-start-scr');
        if (result) result.style.display = 'none';
        if (submitBtn) submitBtn.style.display = 'inline-block';
        if (testArea) testArea.style.display = 'none';
        if (startScr) startScr.style.display = 'block';

        for (var i = 0; i < TT.totalQ; i++) {
            var selInput = document.getElementById('tsel-' + i);
            if (selInput) selInput.value = '';
            var block = document.getElementById('tq-' + i);
            if (block) {
                block.querySelectorAll('.test-opt').forEach(function (o) {
                    o.classList.remove('sel', 'ok', 'bad', 'no-click');
                });
                var sb = block.querySelector('.test-sol-box');
                if (sb) sb.remove();
            }
        }
        var fill = document.getElementById('prog-fill');
        if (fill) fill.style.width = '0%';
    };

    /* ── DOMContentLoaded Init ──────────────────────────────── */
    document.addEventListener('DOMContentLoaded', function () {
        // Restore language preference
        if (localStorage.getItem('sjmaths_preferred_language') === 'hi') {
            document.body.classList.add('lang-mode-hi');
        }

        // Wire up tab buttons via data-tab attribute
        document.querySelectorAll('.sub-nav-item[data-tab]').forEach(function (btn) {
            btn.addEventListener('click', function () {
                switchTab(btn.getAttribute('data-tab'));
            });
        });

        // Show first tab by default if none is active
        var firstTab = document.querySelector('.tab-content');
        var firstBtn = document.querySelector('.sub-nav-item[data-tab]');
        if (firstTab && firstTab.style.display !== 'block') {
            firstTab.style.display = 'block';
            if (firstBtn) firstBtn.classList.add('active');
        }
    });

})();
