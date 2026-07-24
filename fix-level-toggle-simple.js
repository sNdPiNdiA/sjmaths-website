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

const extraCSS = `
        .practice-card[data-level="1"], .practice-card[data-level="2"],
        .practice-card[data-level="3"], .practice-card[data-level="4"],
        .practice-card[data-level="5"], .practice-card[data-level="6"],
        .practice-card[data-level="7"] { display: none; }
        .practice-card.level-active { display: block; }`;

const simpleLevelJS = `
        <script>
        document.addEventListener('DOMContentLoaded', function() {
            const btns = document.querySelectorAll('#levelNav .level-btn');
            const cards = document.querySelectorAll('#tab-practice .practice-card');
            const totalQuestions = 49;

            // Build progress dots
            const progressTrack = document.getElementById('progressTrack');
            if (progressTrack) {
                progressTrack.innerHTML = '';
                for (let i = 1; i <= totalQuestions; i++) {
                    const dot = document.createElement('span');
                    dot.className = 'progress-dot';
                    dot.id = 'dot-' + i;
                    dot.dataset.qId = i;
                    progressTrack.appendChild(dot);
                }
            }

            function showLevel(level) {
                cards.forEach(card => {
                    const cl = card.getAttribute('data-level');
                    if (cl === level) {
                        card.classList.add('level-active');
                    } else {
                        card.classList.remove('level-active');
                    }
                });
            }

            btns.forEach(btn => {
                btn.addEventListener('click', function() {
                    btns.forEach(b => b.classList.remove('active'));
                    this.classList.add('active');
                    const lvl = this.getAttribute('data-level');
                    showLevel(lvl);
                });
            });

            // Default level 1 active
            showLevel('1');

            // Track solution views
            const details = document.querySelectorAll('#tab-practice .solution-details');
            details.forEach((det, idx) => {
                det.addEventListener('toggle', function() {
                    if (this.open) {
                        const dot = document.getElementById('dot-' + (idx + 1));
                        if (dot) dot.classList.add('completed');
                        const attempted = document.querySelectorAll('.progress-dot.completed').length;
                        const attemptedCount = document.getElementById('attemptedCount');
                        const correctCount = document.getElementById('correctCount');
                        const scoreDisplay = document.getElementById('scoreDisplay');
                        if (attemptedCount) attemptedCount.textContent = attempted + '/' + totalQuestions;
                        if (correctCount) correctCount.textContent = attempted + '/' + totalQuestions;
                        if (scoreDisplay) scoreDisplay.textContent = Math.round((attempted / totalQuestions) * 100) + '%';
                    }
                });
            });
        });
        </script>`;

topics.forEach(slug => {
    const filePath = path.join(baseDir, slug, 'index.html');
    if (!fs.existsSync(filePath)) {
        console.log(`Skipping ${slug}`);
        return;
    }

    let html = fs.readFileSync(filePath, 'utf8');

    // Remove old level scripts
    const oldRegex = /<script>\s*document\.addEventListener\('DOMContentLoaded'[\s\S]*?<\/script>/;
    html = html.replace(oldRegex, '');

    // Add CSS before </style>
    const styleEnd = html.indexOf('</style>');
    if (styleEnd !== -1) {
        html = html.slice(0, styleEnd) + extraCSS + html.slice(styleEnd);
    }

    // Add simple JS before last </script>
    const lastScriptEnd = html.lastIndexOf('</script>');
    if (lastScriptEnd !== -1) {
        html = html.slice(0, lastScriptEnd) + simpleLevelJS + html.slice(lastScriptEnd);
    }

    fs.writeFileSync(filePath, html, 'utf8');
    console.log(`Simple level toggle fixed: ${slug}`);
});

console.log('Done!');