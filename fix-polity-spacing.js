const fs = require('fs');
const path = require('path');

const topics = [
    'constituent-assembly-and-making-of-constitution',
    'preamble-of-the-constitution',
    'sources-of-the-indian-constitution',
    'parts-and-schedules-of-the-constitution',
    'citizenship-articles-5-11-and-caa',
    'fundamental-rights-articles-12-35-and-writs',
    'directive-principles-of-state-policy-dpsp-articles-36-51',
    'fundamental-duties-article-51a-and-swaran-singh',
    'union-executive-president-vp-pm-and-cabinet',
    'parliament-lok-sabha-rajya-sabha-and-officers',
    'parliamentary-proceedings-bills-motions-and-committees',
    'state-executive-governor-cm-and-council',
    'state-legislature-assembly-and-council',
    'judiciary-supreme-court-and-high-courts',
    'panchayati-raj-system-73rd-amendment-and-11th-schedule',
    'municipalities-74th-amendment-and-12th-schedule',
    'constitutional-bodies-ec-fc-cag-upsc',
    'statutory-and-non-constitutional-bodies-niti-aayog-nhrc-lokpal'
];

const base = path.join(__dirname, 'ssc-cgl', 'general-awareness', 'general-policy-polity');

let updated = 0;

topics.forEach(slug => {
    const file = path.join(base, slug, 'index.html');
    if (!fs.existsSync(file)) { console.log('Missing: ' + slug); return; }

    let html = fs.readFileSync(file, 'utf8');
    const original = html;

    // ── 1. Remove stray "/* Practice Questions Tab Styling */" outside <style> ──
    // It sits between </style> and </head>, strip it including any surrounding whitespace
    html = html.replace(/(<\/style>)\s*\/\*\s*Practice Questions Tab Styling\s*\*\/\s*\n?/gi, '$1\n');

    // ── 2. SPACING & PADDING POLISH (update existing inline CSS rules) ──

    // topic-container: better breathing room
    html = html.replace(
        /\.topic-container\s*\{[^}]*\}/,
        `.topic-container {
            max-width: 1050px;
            margin: 0 auto;
            padding: 1.5rem 1.25rem 4rem;
            animation: fadeIn 0.4s ease-out;
        }`
    );

    // topic-header: more padding, less cramped
    html = html.replace(
        /\.topic-header\s*\{[^}]*\}/,
        `.topic-header {
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            border-radius: 1.25rem;
            padding: 2rem 1.5rem;
            box-shadow: var(--shadow-lg);
            margin-bottom: 1.75rem;
            text-align: center;
        }`
    );

    // main-tabs-nav: tighter bottom, cleaner
    html = html.replace(
        /\.main-tabs-nav\s*\{[^}]*\}/,
        `.main-tabs-nav {
            display: flex;
            gap: 0.5rem;
            margin-bottom: 1.75rem;
            border-bottom: 2px solid #e2e8f0;
            padding-bottom: 0;
            overflow-x: auto;
            -webkit-overflow-scrolling: touch;
            scrollbar-width: none;
        }`
    );

    // tab-btn: more spacious, pill-ish feel
    html = html.replace(
        /\.tab-btn\s*\{[^}]*\}/,
        `.tab-btn {
            background: transparent;
            border: none;
            border-bottom: 3px solid transparent;
            outline: none;
            font-family: 'Outfit', sans-serif;
            font-size: 0.88rem;
            font-weight: 700;
            color: #718096;
            padding: 0.75rem 1rem 0.65rem;
            cursor: pointer;
            border-radius: 8px 8px 0 0;
            transition: all 0.25s ease;
            display: flex;
            align-items: center;
            gap: 0.45rem;
            white-space: nowrap;
            flex-shrink: 0;
            letter-spacing: 0.01em;
        }`
    );

    // tab-btn active: bottom border instead of box, cleaner
    html = html.replace(
        /\.tab-btn\.active\s*\{[^}]*\}/,
        `.tab-btn.active {
            color: var(--primary, #8e44ad);
            background: rgba(142, 68, 173, 0.06);
            border-bottom-color: var(--primary, #8e44ad);
            box-shadow: none;
        }`
    );

    // tab-panel: generous padding, softer radius
    html = html.replace(
        /\.tab-panel\s*\{[^}]*\}/,
        `.tab-panel {
            display: none;
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            border-radius: 1.25rem;
            padding: 2rem 1.75rem;
            box-shadow: var(--shadow-lg);
            animation: fadeIn 0.35s ease-out;
            line-height: 1.7;
            color: var(--text-dark);
        }`
    );

    // practice-card: better spacing
    html = html.replace(
        /\.practice-card\s*\{[\s\S]*?background: #fff;[\s\S]*?transition:.*?\}/,
        `.practice-card {
            background: #fff;
            border: 1px solid rgba(142, 68, 173, 0.12);
            border-radius: 1rem;
            padding: 1.5rem 1.5rem 1.25rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 2px 12px rgba(0,0,0,0.04);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }`
    );

    // solution-body: more room
    html = html.replace(
        /\.solution-body\s*\{[^}]*\}/,
        `.solution-body {
            margin-top: 1rem;
            background: rgba(142, 68, 173, 0.03);
            border-radius: 10px;
            padding: 1.25rem 1.25rem 0.5rem;
            font-size: 0.9rem;
            line-height: 1.65;
        }`
    );

    // solution-body > div spacing
    html = html.replace(
        /\.solution-body\s*>\s*div\s*\{[^}]*\}/,
        `.solution-body > div {
            margin-bottom: 1rem;
            padding-bottom: 1rem;
            border-bottom: 1px solid rgba(0,0,0,0.05);
        }`
    );

    // level-navigation: more bottom margin
    html = html.replace(
        /\.level-navigation\s*\{[^}]*\}/,
        `.level-navigation {
            display: flex;
            gap: 0.5rem;
            margin-bottom: 2rem;
            overflow-x: auto;
            padding-bottom: 0.5rem;
            -webkit-overflow-scrolling: touch;
            scrollbar-width: none;
        }`
    );

    // pyq-year-block h3: more breathing room
    html = html.replace(
        /\.pyq-year-block h3\s*\{[^}]*\}/,
        `.pyq-year-block h3 {
            font-family: 'Outfit', sans-serif;
            font-size: 1.2rem;
            font-weight: 800;
            color: var(--primary, #8e44ad);
            margin: 2rem 0 0.75rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid rgba(142, 68, 173, 0.15);
        }`
    );

    // pyq-year-chain: more margin
    html = html.replace(
        /\.pyq-year-chain\s*\{[^}]*\}/,
        `.pyq-year-chain {
            display: flex;
            flex-wrap: wrap;
            align-items: center;
            gap: 0.35rem;
            margin: 1rem 0 2rem;
            font-size: 0.85rem;
        }`
    );

    // pyq-options li: nicer spacing
    html = html.replace(
        /\.pyq-options li\s*\{[^}]*\}/,
        `.pyq-options li {
            background: rgba(0, 0, 0, 0.02);
            border: 1px solid rgba(0, 0, 0, 0.06);
            border-radius: 8px;
            padding: 0.6rem 0.9rem;
            font-size: 0.9rem;
            color: #34495e;
            line-height: 1.5;
        }`
    );

    // q-text: bigger, more weight
    html = html.replace(
        /\.q-text\s*\{[^}]*\}/,
        `.q-text {
            font-size: 1rem;
            font-weight: 600;
            color: #1a202c;
            margin-bottom: 1rem;
            line-height: 1.6;
        }`
    );

    // level-badge: more polish
    html = html.replace(
        /\.level-badge\s*\{[^}]*\}/,
        `.level-badge {
            display: inline-block;
            background: rgba(142, 68, 173, 0.08);
            color: var(--primary, #8e44ad);
            font-size: 0.72rem;
            font-weight: 700;
            padding: 0.25rem 0.7rem;
            border-radius: 20px;
            margin-bottom: 0.9rem;
            letter-spacing: 0.03em;
            text-transform: uppercase;
        }`
    );

    // callout boxes: more padding
    html = html.replace(
        /\.exam-tip,\s*\.remember-this,\s*\.common-mistake,\s*\.py-insight\s*\{[^}]*\}/,
        `.exam-tip, .remember-this, .common-mistake, .py-insight {
            padding: 1rem 1.1rem;
            border-radius: 10px;
            margin: 1.25rem 0;
            border-left: 4px solid;
            font-size: 0.93rem;
            line-height: 1.65;
        }`
    );

    // details.solution-details: more top margin
    html = html.replace(
        /details\.solution-details\s*\{[^}]*\}/,
        `details.solution-details {
            margin-top: 0.9rem;
            border-top: 1px dashed rgba(0,0,0,0.08);
            padding-top: 0.7rem;
        }`
    );

    // solution-details summary: better click target
    html = html.replace(
        /details\.solution-details summary\s*\{[^}]*\}/,
        `details.solution-details summary {
            font-weight: 700;
            color: var(--primary);
            cursor: pointer;
            font-size: 0.9rem;
            user-select: none;
            outline: none;
            padding: 0.5rem 0;
            display: flex;
            align-items: center;
            gap: 0.4rem;
        }`
    );

    // tab-panel h2
    html = html.replace(
        /\.tab-panel h2\s*\{[^}]*\}/,
        `.tab-panel h2 {
            font-family: 'Outfit', sans-serif;
            font-size: 1.4rem;
            font-weight: 700;
            color: var(--primary);
            margin-top: 1.75rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid rgba(142, 68, 173, 0.15);
            padding-bottom: 0.4rem;
        }`
    );

    // tab-panel h3
    html = html.replace(
        /\.tab-panel h3\s*\{[^}]*\}/,
        `.tab-panel h3 {
            font-family: 'Outfit', sans-serif;
            font-size: 1.1rem;
            font-weight: 700;
            color: var(--text-dark);
            margin-top: 1.25rem;
            margin-bottom: 0.65rem;
        }`
    );

    // q-options spacing
    html = html.replace(
        /\.q-options\s*\{[^}]*\}/,
        `.q-options {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 0.6rem;
            margin-bottom: 1rem;
            padding: 0;
        }`
    );

    // pyq-options spacing
    html = html.replace(
        /\.pyq-options\s*\{[^}]*\}/,
        `.pyq-options {
            list-style: none;
            padding: 0;
            margin: 0.75rem 0 1rem;
            display: flex;
            flex-direction: column;
            gap: 0.4rem;
        }`
    );

    // next-tab-btn-container: more breathing room
    html = html.replace(
        /\.next-tab-btn-container\s*\{[^}]*\}/,
        `.next-tab-btn-container {
            margin-top: 2.5rem;
            text-align: center;
        }`
    );

    // memory-tip and why-wrong: better padding
    html = html.replace(
        /\.memory-tip\s*\{[^}]*\}/,
        `.memory-tip {
            background: linear-gradient(135deg, rgba(241, 196, 15, 0.08), rgba(230, 126, 34, 0.08));
            padding: 0.75rem 1rem;
            border-radius: 8px;
            border-left: 3px solid #f39c12;
        }`
    );

    html = html.replace(
        /\.why-wrong\s*\{[^}]*\}/,
        `.why-wrong {
            background: rgba(231, 76, 60, 0.04);
            padding: 0.75rem 1rem;
            border-radius: 8px;
            border-left: 3px solid rgba(231, 76, 60, 0.4);
        }`
    );

    html = html.replace(
        /\.related-concept\s*\{[^}]*\}/,
        `.related-concept {
            background: rgba(52, 152, 219, 0.06);
            padding: 0.75rem 1rem;
            border-radius: 8px;
            border-left: 3px solid #3498db;
        }`
    );

    // mobile responsive
    html = html.replace(
        /@media \(max-width: 768px\)\s*\{[\s\S]*?\.premium-table td\s*\{[^}]*\}\s*\}/,
        `@media (max-width: 768px) {
            .topic-container {
                padding: 0.75rem 0.875rem 2.5rem;
            }
            .tab-panel {
                padding: 1.25rem 1rem;
                border-radius: 1rem;
            }
            .tab-btn {
                font-size: 0.76rem;
                padding: 0.6rem 0.65rem 0.55rem;
            }
            .premium-table {
                font-size: 0.83rem;
            }
            .premium-table th,
            .premium-table td {
                padding: 9px 11px;
            }
            .practice-card {
                padding: 1.1rem 1rem;
            }
            .q-text {
                font-size: 0.93rem;
            }
        }`
    );

    if (html !== original) {
        fs.writeFileSync(file, html, 'utf8');
        console.log('Updated: ' + slug);
        updated++;
    } else {
        console.log('No change: ' + slug);
    }
});

console.log('\nDone. Updated: ' + updated + '/' + topics.length);
