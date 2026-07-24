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

const levelVisibilityCSS = `
        .level-section { display: none; }
        .level-section.active { display: block; }`;

const levelVisibilityJS = `
        <script>
        document.addEventListener('DOMContentLoaded', function() {
            const levelBtns = document.querySelectorAll('#levelNav .level-btn');
            const practiceContainer = document.getElementById('tab-practice');
            const cards = practiceContainer.querySelectorAll('.practice-card');
            const dots = document.querySelectorAll('.progress-dot');
            const totalQuestions = 49;

            if (!practiceContainer || cards.length === 0) return;

            // Group cards by level
            const levels = {};
            cards.forEach(card => {
                const lvl = card.getAttribute('data-level');
                if (!levels[lvl]) levels[lvl] = [];
                levels[lvl].push(card);
            });

            // Wrap each level group in a .level-section
            Object.keys(levels).sort((a,b) => parseInt(a) - parseInt(b)).forEach(lvl => {
                const section = document.createElement('div');
                section.className = 'level-section' + (lvl === '1' ? ' active' : '');
                section.id = 'level-' + lvl;

                // Find the first card of this level
                const firstCard = levels[lvl][0];
                const parent = firstCard.parentNode;

                firstCard.parentNode.insertBefore(section, firstCard);
                levels[lvl].forEach(card => section.appendChild(card));
            });

            // Wire level buttons
            levelBtns.forEach(btn => {
                btn.addEventListener('click', function() {
                    levelBtns.forEach(b => b.classList.remove('active'));
                    this.classList.add('active');
                    const target = document.getElementById('level-' + this.dataset.level);
                    if (target) target.classList.add('active');
                });
            });

            // Initialize progress dots visibility by level
            function updateProgressByLevel() {
                const sections = document.querySelectorAll('.level-section');
                sections.forEach((sec, idx) => {
                    const lvl = sec.id.replace('level-', '');
                    const levelCards = sec.querySelectorAll('.practice-card');
                    levelCards.forEach((card, cIdx) => {
                        const dot = document.querySelector('.progress-dot[data-q-id="' + card.getAttribute('data-card-id') + '"]');
                        if (!dot) {
                            const dotEl = document.createElement('span');
                            dotEl.className = 'progress-dot';
                            dotEl.dataset.qId = card.getAttribute('data-card-id');
                            document.getElementById('progressTrack').appendChild(dotEl);
                        }
                    });
                });
            }

            // Assign sequential IDs to cards
            cards.forEach((card, idx) => {
                card.setAttribute('data-card-id', idx + 1);
            });

            // Rebuild progress track with proper IDs
            const progressTrack = document.getElementById('progressTrack');
            if (progressTrack) {
                progressTrack.innerHTML = '';
                for (let i = 1; i <= totalQuestions; i++) {
                    const dot = document.createElement('span');
                    dot.className = 'progress-dot';
                    dot.dataset.qId = i;
                    dot.id = 'dot-' + i;
                    progressTrack.appendChild(dot);
                }
            }

            // Track solution views and update progress
            const details = document.querySelectorAll('.solution-details');
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
        console.log(`Skipping: ${slug} (not found)`);
        return;
    }

    let html = fs.readFileSync(filePath, 'utf8');

    // Remove the old buggy level navigation script
    const oldScriptRegex = /<script>\s*document\.addEventListener\('DOMContentLoaded'[\s\S]*?<\/script>/;
    html = html.replace(oldScriptRegex, '');

    // Inject level visibility CSS before </style>
    const styleEndIdx = html.indexOf('</style>');
    if (styleEndIdx !== -1) {
        html = html.slice(0, styleEndIdx) + levelVisibilityCSS + html.slice(styleEndIdx);
    }

    // Inject the new level visibility JS before </script> at the end
    const lastScriptEndIdx = html.lastIndexOf('</script>');
    if (lastScriptEndIdx !== -1) {
        html = html.slice(0, lastScriptEndIdx) + levelVisibilityJS + html.slice(lastScriptEndIdx);
    }

    fs.writeFileSync(filePath, html, 'utf8');
    console.log(`Fixed level visibility: ${slug}`);
});

console.log('\nDone! All files now show one level at a time.');