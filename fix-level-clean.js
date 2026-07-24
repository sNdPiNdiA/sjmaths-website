const fs = require('fs');
const path = require('path');

const topics = [
    "constituent-assembly-and-making-of-constitution",
    "preamble-of-the-constitution",
    "sources-of-the-indian-constitution",
    "parts-and-schedules-of-the-constitution",
    "citizenship-articles-5-11-and-caa",
    "fundamental-rights-articles-12-35-and-writs",
    "directive-principles-of-state-policy-dpsp-articles-36-51",
    "fundamental-duties-article-51a-and-swaran-singh",
    "union-executive-president-vp-pm-and-cabinet",
    "parliament-lok-sabha-rajya-sabha-and-officers",
    "parliamentary-proceedings-bills-motions-and-committees",
    "state-executive-governor-cm-and-council",
    "state-legislature-assembly-and-council",
    "judiciary-supreme-court-and-high-courts",
    "panchayati-raj-system-73rd-amendment-and-11th-schedule",
    "municipalities-74th-amendment-and-12th-schedule",
    "constitutional-bodies-ec-fc-cag-upsc",
    "statutory-and-non-constitutional-bodies-niti-aayog-nhrc-lokpal"
];

const baseDir = 'c:/Users/sande/Documents/GitHub/sjmaths-website/ssc-cgl/general-awareness/general-policy-polity';

const cleanCSS = `
        .practice-card { display: none; }
        .practice-card.level-active { display: block; }`;

const cleanJS = `
        <script>
        (function() {
            var btns = document.querySelectorAll('#levelNav .level-btn');
            var cards = document.querySelectorAll('#tab-practice .practice-card');
            var totalQuestions = 49;

            // Build progress dots
            var progressTrack = document.getElementById('progressTrack');
            if (progressTrack) {
                progressTrack.innerHTML = '';
                for (var i = 1; i <= totalQuestions; i++) {
                    var dot = document.createElement('span');
                    dot.className = 'progress-dot';
                    dot.id = 'dot-' + i;
                    dot.dataset.qId = i;
                    progressTrack.appendChild(dot);
                }
            }

            function showLevel(level) {
               cards.forEach(function(card) {
                    var cl = card.getAttribute('data-level');
                    if (cl === level) {
                        card.classList.add('level-active');
                    } else {
                        card.classList.remove('level-active');
                    }
                });
            }

            btns.forEach(function(btn) {
                btn.addEventListener('click', function() {
                    btns.forEach(function(b) { b.classList.remove('active'); });
                    this.classList.add('active');
                    var lvl = this.getAttribute('data-level');
                    showLevel(lvl);
                });
            });

            // Default: show level 1
            showLevel('1');

            // Track solution views
            var details = document.querySelectorAll('#tab-practice .solution-details');
            details.forEach(function(det, idx) {
                det.addEventListener('toggle', function() {
                    if (this.open) {
                        var dot = document.getElementById('dot-' + (idx + 1));
                        if (dot) dot.classList.add('completed');
                        var attempted = document.querySelectorAll('.progress-dot.completed').length;
                        var attemptedCount = document.getElementById('attemptedCount');
                        var correctCount = document.getElementById('correctCount');
                        var scoreDisplay = document.getElementById('scoreDisplay');
                        if (attemptedCount) attemptedCount.textContent = attempted + '/' + totalQuestions;
                        if (correctCount) correctCount.textContent = attempted + '/' + totalQuestions;
                        if (scoreDisplay) scoreDisplay.textContent = Math.round((attempted / totalQuestions) * 100) + '%';
                    }
                });
            });
        })();
        </script>`;

topics.forEach(slug => {
    const filePath = path.join(baseDir, slug, 'index.html');
    if (!fs.existsSync(filePath)) {
        console.log(`Skipping ${slug}`);
        return;
    }

    let html = fs.readFileSync(filePath, 'utf8');

    // Remove ALL existing inline scripts that manage levels/practice
    html = html.replace(/<script>[\s\S]*?<\/script>/g, function (match) {
        if (match.indexOf('DOMContentLoaded') !== -1 || match.indexOf('levelNav') !== -1 || match.indexOf('showLevel') !== -1 || match.indexOf('level-active') !== -1) {
            return '';
        }
        return match;
    });

    // Remove ALL the duplicated/conflicting practice CSS inside <style>
    // Strategy: keep everything up to /* Practice Questions Tab Styling */ and its following comment, remove the leaked CSS block between there and </style>
    const leakedBlock = /\/\* Practice Questions Tab Styling \*\/\s*[^<]*\s*<\/style>/;
    html = html.replace(leakedBlock, '/* Practice Questions Tab Styling */\n        </style>');

    // Now inject clean CSS before </style>
    const styleEnd = html.indexOf('</style>');
    if (styleEnd !== -1) {
        html = html.slice(0, styleEnd) + cleanCSS + html.slice(styleEnd);
    }

    // Inject clean JS before </script> (the last remaining script tag, typically main app script)
    const lastScriptEnd = html.lastIndexOf('</script>');
    if (lastScriptEnd !== -1) {
        html = html.slice(0, lastScriptEnd) + cleanJS + html.slice(lastScriptEnd);
    }

    fs.writeFileSync(filePath, html, 'utf8');
    console.log(`Clean level fix applied: ${slug}`);
});

console.log('Done!');