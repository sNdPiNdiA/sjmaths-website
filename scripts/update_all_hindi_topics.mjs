import fs from 'fs';
import path from 'path';

const baseDir = path.join(process.cwd(), 'up-upper-primary-teacher', 'hindi');
const entries = fs.readdirSync(baseDir, { withFileTypes: true });

const robustHeadThemeScript = `<!-- Theme & Palette Sync Script (Light / Dark Mode Persistence matching Homepage) -->
<script>
    (function () {
        const sjDark = localStorage.getItem('sjmaths-dark');
        const legacyTheme = localStorage.getItem('theme');
        const isDark = sjDark === 'on' || (sjDark === null && legacyTheme === 'dark') || (sjDark === null && legacyTheme === null && window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches);
        if (isDark) {
            document.documentElement.classList.add('dark-mode');
            document.documentElement.setAttribute('data-theme', 'dark');
        } else {
            document.documentElement.classList.remove('dark-mode');
            document.documentElement.setAttribute('data-theme', 'light');
        }
        const savedTheme = localStorage.getItem('sjmaths-theme');
        const themePalettes = {
            green: { primary: '#059669', 'primary-dark': '#047857', 'primary-light': '#ecfdf5' },
            blue: { primary: '#2563eb', 'primary-dark': '#1e40af', 'primary-light': '#eff6ff' },
            purple: { primary: '#7c3aed', 'primary-dark': '#6d28d9', 'primary-light': '#f5f3ff' },
            orange: { primary: '#ea580c', 'primary-dark': '#c2410c', 'primary-light': '#fff7ed' }
        };
        if (savedTheme && themePalettes[savedTheme]) {
            Object.entries(themePalettes[savedTheme]).forEach(([k, v]) => {
                document.documentElement.style.setProperty('--brand-' + k, v);
            });
        }
    })();
</script>`;

const robustBodyThemeScript = `<script>
    (function () {
        const sjDark = localStorage.getItem('sjmaths-dark');
        const legacyTheme = localStorage.getItem('theme');
        const isDark = sjDark === 'on' || (sjDark === null && legacyTheme === 'dark') || (sjDark === null && legacyTheme === null && window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches);
        if (isDark) {
            document.body.classList.add('dark-mode');
        } else {
            document.body.classList.remove('dark-mode');
        }
    })();
</script>`;

let processed = 0;

for (const entry of entries) {
    if (!entry.isDirectory()) continue;
    const filePath = path.join(baseDir, entry.name, 'index.html');
    if (!fs.existsSync(filePath)) continue;

    let content = fs.readFileSync(filePath, 'utf8');

    // 1. Update CSS link to include cache buster ?v=20261002_02
    content = content.replace(
        /\/assets\/css\/up-upper-primary-topic\.min\.css(?:\?v=[a-zA-Z0-9_-]+)?/g,
        '/assets/css/up-upper-primary-topic.min.css?v=20261002_02'
    );

    // 2. Update JS link to include cache buster ?v=20261002_02
    content = content.replace(
        /\/assets\/js\/up-upper-primary-topic\.min\.js(?:\?v=[a-zA-Z0-9_-]+)?/g,
        '/assets/js/up-upper-primary-topic.min.js?v=20261002_02'
    );

    // 3. Replace inline style strategy box with .strategy-banner-box class
    content = content.replace(
        /<div style="background:\s*var\(--brand-emerald-subtle\);\s*border-left:\s*4px solid var\(--brand-emerald\);\s*padding:\s*1rem 1\.25rem;\s*border-radius:\s*8px;\s*margin-bottom:\s*1\.5rem;">/g,
        '<div class="strategy-banner-box">'
    );

    // 4. Update head theme script
    content = content.replace(
        /<!-- Theme & Palette Sync Script[\s\S]*?<\/script>\s*(?=<\/head>)/,
        robustHeadThemeScript + '\n'
    );

    // 5. Update body immediate script
    content = content.replace(
        /<body class="lang-mode-hi">\s*<script>[\s\S]*?<\/script>/,
        `<body class="lang-mode-hi">\n${robustBodyThemeScript}`
    );

    fs.writeFileSync(filePath, content, 'utf8');
    processed++;
}

console.log(`Successfully updated ${processed} Hindi topic files with robust theme scripts and cache-busting CSS/JS links.`);
