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

// === COMPREHENSIVE DARK MODE + UI/UX CSS ===
const DARK_MODE_CSS = `
        /* =========================================
           POLITY PAGE - DARK MODE + UI/UX OVERHAUL
           ========================================= */

        /* --- Dark Mode: Core Variables --- */
        body.dark-mode {
            --glass-bg: rgba(20, 20, 35, 0.97);
            --glass-border: rgba(255, 255, 255, 0.07);
            --shadow-lg: 0 10px 30px -5px rgba(0, 0, 0, 0.6);
            --bg-card: #1a1a2e;
            --text-dark: #f1f5f9;
            --text-light: #94a3b8;
            color: #f1f5f9;
        }

        /* --- Dark Mode: Tab Panel --- */
        body.dark-mode .tab-panel {
            background: rgba(20, 20, 35, 0.97);
            border-color: rgba(255, 255, 255, 0.07);
            color: #f1f5f9;
        }

        /* --- Dark Mode: Topic Header --- */
        body.dark-mode .topic-header {
            background: rgba(20, 20, 35, 0.97);
            border-color: rgba(255, 255, 255, 0.07);
        }

        /* --- Dark Mode: Tab Nav --- */
        body.dark-mode .main-tabs-nav {
            border-bottom-color: rgba(255, 255, 255, 0.1);
        }

        body.dark-mode .tab-btn {
            color: #94a3b8;
        }

        body.dark-mode .tab-btn:hover {
            color: #c084fc;
            background: rgba(192, 132, 252, 0.08);
        }

        /* --- Dark Mode: Practice Card (PYQ + Practice Questions) --- */
        body.dark-mode .practice-card {
            background: #1e1b4b !important;
            border-color: rgba(167, 139, 250, 0.2) !important;
            color: #f1f5f9;
        }

        body.dark-mode .practice-card:hover {
            border-color: rgba(167, 139, 250, 0.5) !important;
            box-shadow: 0 8px 20px rgba(139, 92, 246, 0.15);
        }

        /* --- Dark Mode: Level Badge --- */
        body.dark-mode .level-badge {
            background: rgba(167, 139, 250, 0.15);
            color: #c084fc;
        }

        /* --- Dark Mode: Question Text --- */
        body.dark-mode .q-text,
        body.dark-mode .q-text p,
        body.dark-mode .q-text strong {
            color: #f1f5f9 !important;
        }

        /* --- Dark Mode: Options --- */
        body.dark-mode .q-options li,
        body.dark-mode .pyq-options li {
            color: #e2e8f0;
        }

        body.dark-mode .option {
            background: rgba(255, 255, 255, 0.04);
            border-color: rgba(255, 255, 255, 0.08);
            color: #e2e8f0;
        }

        body.dark-mode .option.correct {
            background: rgba(46, 204, 113, 0.12);
            border-color: rgba(46, 204, 113, 0.3);
        }

        /* --- Dark Mode: Solution Details --- */
        body.dark-mode details.solution-details {
            border-top-color: rgba(255, 255, 255, 0.08);
        }

        body.dark-mode details.solution-details summary {
            color: #a78bfa;
        }

        body.dark-mode .solution-body {
            background: rgba(139, 92, 246, 0.06);
            color: #e2e8f0;
        }

        body.dark-mode .solution-body > div {
            border-bottom-color: rgba(255, 255, 255, 0.06);
        }

        body.dark-mode .correct-answer {
            color: #4ade80;
        }

        body.dark-mode .explanation {
            color: #e2e8f0;
        }

        body.dark-mode .why-wrong {
            background: rgba(231, 76, 60, 0.07);
            border-left-color: rgba(231, 76, 60, 0.4);
        }

        body.dark-mode .memory-tip {
            background: rgba(243, 156, 18, 0.07);
            border-left-color: rgba(243, 156, 18, 0.5);
        }

        body.dark-mode .related-concept {
            background: rgba(52, 152, 219, 0.08);
            border-left-color: rgba(52, 152, 219, 0.4);
        }

        body.dark-mode .q-meta {
            color: #94a3b8;
        }

        /* --- Dark Mode: PYQ Timeline Wrapper --- */
        body.dark-mode .pyq-timeline h2 {
            color: #c084fc;
        }

        body.dark-mode .pyq-timeline > p {
            color: #94a3b8;
        }

        body.dark-mode .pyq-year-chain {
            color: #94a3b8;
        }

        body.dark-mode .pyq-year-chain span {
            color: #c084fc;
            background: rgba(192, 132, 252, 0.1);
            border-color: rgba(192, 132, 252, 0.25);
        }

        body.dark-mode .pyq-year-block h3 {
            color: #a78bfa;
            border-bottom-color: rgba(167, 139, 250, 0.2);
        }

        /* --- Dark Mode: Callout Boxes --- */
        body.dark-mode .exam-tip {
            background: rgba(142, 68, 173, 0.12);
            border-left-color: #a78bfa;
            color: #f1f5f9;
        }

        body.dark-mode .remember-this {
            background: rgba(52, 152, 219, 0.1);
            border-left-color: #60a5fa;
            color: #f1f5f9;
        }

        body.dark-mode .common-mistake {
            background: rgba(231, 76, 60, 0.08);
            border-left-color: #f87171;
            color: #f1f5f9;
        }

        body.dark-mode .py-insight {
            background: rgba(46, 204, 113, 0.08);
            border-left-color: #4ade80;
            color: #f1f5f9;
        }

        /* --- Dark Mode: Tables --- */
        body.dark-mode .premium-table-container {
            background: #1a1a2e;
            border-color: rgba(255, 255, 255, 0.08);
        }

        body.dark-mode .premium-table {
            color: #f1f5f9;
        }

        body.dark-mode .premium-table th {
            background: rgba(167, 139, 250, 0.12);
            color: #c084fc;
            border-bottom-color: rgba(167, 139, 250, 0.2);
        }

        body.dark-mode .premium-table td {
            border-bottom-color: rgba(255, 255, 255, 0.06);
        }

        body.dark-mode .premium-table tr:nth-child(even) td {
            background: rgba(255, 255, 255, 0.02);
        }

        body.dark-mode .premium-table tr:hover td {
            background: rgba(167, 139, 250, 0.06);
        }

        body.dark-mode .tab-panel th {
            background: rgba(167, 139, 250, 0.1);
            color: #c084fc;
        }

        body.dark-mode .tab-panel td,
        body.dark-mode .tab-panel th {
            border-color: rgba(255, 255, 255, 0.08);
        }

        /* --- Dark Mode: Level Buttons --- */
        body.dark-mode .level-btn {
            color: #94a3b8;
            border-color: rgba(167, 139, 250, 0.2);
        }

        body.dark-mode .level-btn:hover {
            background: rgba(167, 139, 250, 0.08);
            color: #c084fc;
        }

        /* --- Dark Mode: Practice Progress Bar --- */
        body.dark-mode .practice-progress-bar {
            background: rgba(20, 20, 35, 0.97);
            border-color: rgba(255, 255, 255, 0.07);
        }

        body.dark-mode .practice-stats span {
            color: #e2e8f0;
        }

        body.dark-mode .progress-dot {
            background: #334155;
        }

        /* --- Dark Mode: h2, h3 inside tab panels --- */
        body.dark-mode .tab-panel h2 {
            color: #c084fc;
            border-bottom-color: rgba(167, 139, 250, 0.2);
        }

        body.dark-mode .tab-panel h3 {
            color: #e2e8f0;
        }

        body.dark-mode .tab-panel p,
        body.dark-mode .tab-panel li {
            color: #e2e8f0;
        }

        body.dark-mode .tab-panel strong {
            color: #f1f5f9;
        }

        body.dark-mode .tab-panel a {
            color: #a78bfa;
        }

        /* --- Dark Mode: Coming Soon Box --- */
        body.dark-mode .coming-soon-box {
            background: linear-gradient(135deg, rgba(139, 92, 246, 0.06), rgba(231, 76, 60, 0.06));
            border-color: rgba(167, 139, 250, 0.25);
        }

        body.dark-mode .coming-soon-box h3 {
            color: #f1f5f9;
        }

        body.dark-mode .coming-soon-box p {
            color: #94a3b8;
        }

        /* ===================================
           PYQ TIMELINE - BASE LIGHT + DARK
           =================================== */

        /* Year Chain Styling */
        .pyq-year-chain {
            display: flex;
            flex-wrap: wrap;
            align-items: center;
            gap: 0.3rem;
            margin: 0.75rem 0 1.5rem;
            font-size: 0.85rem;
        }

        .pyq-year-chain span {
            display: inline-block;
            padding: 0.2rem 0.6rem;
            border-radius: 20px;
            background: rgba(142, 68, 173, 0.08);
            color: var(--primary, #8e44ad);
            border: 1px solid rgba(142, 68, 173, 0.18);
            font-weight: 700;
            font-size: 0.8rem;
        }

        .pyq-year-chain i {
            color: #94a3b8;
            font-size: 0.7rem;
        }

        /* Year Block */
        .pyq-year-block {
            margin-bottom: 0.5rem;
        }

        .pyq-year-block h3 {
            font-family: 'Outfit', sans-serif;
            font-size: 1.15rem;
            font-weight: 800;
            color: var(--primary, #8e44ad);
            margin: 1.25rem 0 0.6rem;
            padding-bottom: 0.4rem;
            border-bottom: 2px solid rgba(142, 68, 173, 0.15);
        }

        /* PYQ Options — Ordered list override */
        .pyq-options {
            list-style: none;
            padding: 0;
            margin: 0.5rem 0 0.75rem;
            display: flex;
            flex-direction: column;
            gap: 0.35rem;
        }

        .pyq-options li {
            background: rgba(0, 0, 0, 0.02);
            border: 1px solid rgba(0, 0, 0, 0.06);
            border-radius: 6px;
            padding: 0.45rem 0.75rem;
            font-size: 0.88rem;
            color: #34495e;
            line-height: 1.5;
        }

        body.dark-mode .pyq-options li {
            background: rgba(255, 255, 255, 0.03);
            border-color: rgba(255, 255, 255, 0.07);
            color: #e2e8f0;
        }

        /* PYQ Card extra polish */
        .pyq-card {
            border-left: 3px solid var(--primary, #8e44ad) !important;
        }

        body.dark-mode .pyq-card {
            border-left-color: #a78bfa !important;
        }

        /* ===================================
           SPACING: Tight year-block rhythm
           =================================== */
        .pyq-year-block {
            margin-bottom: 0;
        }

        .pyq-year-block h3 {
            font-family: 'Outfit', sans-serif;
            font-size: 1.15rem;
            font-weight: 800;
            color: var(--primary, #8e44ad);
            margin: 1.5rem 0 0.6rem;
            padding-bottom: 0.4rem;
            border-bottom: 2px solid rgba(142, 68, 173, 0.15);
        }

        body.dark-mode .pyq-year-block h3 {
            color: #a78bfa;
            border-bottom-color: rgba(167, 139, 250, 0.2);
        }

        /* No extra space after card before next year heading */
        .pyq-card {
            margin-bottom: 0 !important;
        }

        /* ===================================
           INTERACTIVE PYQ OPTIONS
           =================================== */

        /* Make options look clickable */
        .pyq-options li {
            cursor: pointer;
            user-select: none;
            transition: background 0.15s ease, border-color 0.15s ease, transform 0.1s ease;
            position: relative;
            padding-left: 1rem;
        }

        .pyq-options li:hover {
            background: rgba(142, 68, 173, 0.07) !important;
            border-color: rgba(142, 68, 173, 0.3) !important;
            transform: translateX(2px);
        }

        body.dark-mode .pyq-options li:hover {
            background: rgba(167, 139, 250, 0.1) !important;
            border-color: rgba(167, 139, 250, 0.35) !important;
        }

        /* Correct answer highlight - green */
        .pyq-options li.pyq-correct {
            background: rgba(46, 204, 113, 0.12) !important;
            border-color: rgba(46, 204, 113, 0.5) !important;
            color: #1a6636 !important;
            font-weight: 700;
        }

        .pyq-options li.pyq-correct::before {
            content: "✓ ";
            color: #27ae60;
            font-weight: 900;
        }

        body.dark-mode .pyq-options li.pyq-correct {
            background: rgba(46, 204, 113, 0.15) !important;
            border-color: rgba(46, 204, 113, 0.5) !important;
            color: #4ade80 !important;
        }

        body.dark-mode .pyq-options li.pyq-correct::before {
            color: #4ade80;
        }

        /* Wrong answer highlight - red */
        .pyq-options li.pyq-wrong {
            background: rgba(231, 76, 60, 0.08) !important;
            border-color: rgba(231, 76, 60, 0.4) !important;
            color: #922b21 !important;
        }

        .pyq-options li.pyq-wrong::before {
            content: "✗ ";
            color: #e74c3c;
            font-weight: 900;
        }

        body.dark-mode .pyq-options li.pyq-wrong {
            background: rgba(231, 76, 60, 0.12) !important;
            border-color: rgba(231, 76, 60, 0.45) !important;
            color: #f87171 !important;
        }

        body.dark-mode .pyq-options li.pyq-wrong::before {
            color: #f87171;
        }

        /* Click hint tooltip before first interaction */
        .pyq-options:not([data-answered="true"]) {
            position: relative;
        }

        /* Answered state - no hover effect */
        .pyq-options[data-answered="true"] li {
            cursor: default;
        }
`;

const MARKER = '/* =========================================\n           POLITY PAGE - DARK MODE + UI/UX OVERHAUL';
const END_STYLE = '</style>';

let updated = 0;

topics.forEach(slug => {
    const file = path.join(base, slug, 'index.html');
    if (!fs.existsSync(file)) {
        console.log('Missing: ' + slug);
        return;
    }
    let html = fs.readFileSync(file, 'utf8');

    // Remove existing dark mode block if already injected
    if (html.includes(MARKER)) {
        const startIdx = html.indexOf('/* =========================================\n           POLITY PAGE - DARK MODE');
        const blockEnd = html.indexOf('</style>', startIdx);
        if (startIdx !== -1 && blockEnd !== -1) {
            html = html.slice(0, startIdx) + html.slice(blockEnd);
        }
    }

    // Find the last </style> tag before </head>
    const headEnd = html.indexOf('</head>');
    const styleEnd = html.lastIndexOf('</style>', headEnd);

    if (styleEnd === -1) {
        console.log('No </style> found: ' + slug);
        return;
    }

    // Inject our CSS block just before the </style>
    const updated_html = html.slice(0, styleEnd) + DARK_MODE_CSS + '\n    ' + html.slice(styleEnd);
    fs.writeFileSync(file, updated_html, 'utf8');
    console.log('Updated: ' + slug);
    updated++;
});

console.log('\nDone. Updated: ' + updated + '/' + topics.length);
