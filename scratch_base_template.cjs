const fs = require('fs');
const path = require('path');

function safeWrite(filePath, content) {
  const dir = path.dirname(filePath);
  if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
  fs.writeFileSync(filePath, content, 'utf8');
}

// Common CSS & Head template
function getHead(title, desc, keywords) {
  return `<!DOCTYPE html>
<html lang="hi">
<head>
<script async="" crossorigin="anonymous" src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7924751316191829"></script>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>${title} — UP Upper Primary Teacher Mathematics | SJMaths</title>
<meta content="${keywords}" name="keywords"/>
<meta content="SJMaths" name="author"/>
<meta content="${desc}" name="description"/>
<meta content="index, follow" name="robots"/>
<link href="/assets/css/main.min.css" rel="stylesheet"/>
<!-- KaTeX for pristine math rendering -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css"/>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]});"></script>
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Noto+Sans+Devanagari:wght@400;500;600;700;800&family=Fira+Code:wght@400;500;600&display=swap" rel="stylesheet"/>
<style>
    :root {
        --brand-emerald: #059669;
        --brand-emerald-dark: #065f46;
        --brand-emerald-light: #d1fae5;
        --brand-emerald-accent: #10b981;
        --brand-indigo: #4f46e5;
        --brand-indigo-light: #e0e7ff;
        --brand-amber: #d97706;
        --brand-amber-light: #fef3c7;
        --brand-rose: #e11d48;
        --brand-rose-light: #ffe4e6;
        --brand-cyan: #0891b2;
        --brand-cyan-light: #cffafe;
        --bg-main: #f8fafc;
        --bg-surface: #ffffff;
        --border-subtle: #e2e8f0;
        --border-medium: #cbd5e1;
        --text-main: #0f172a;
        --text-sub: #334155;
        --text-muted: #64748b;
        --font-sans: 'Plus Jakarta Sans', 'Noto Sans Devanagari', sans-serif;
        --font-mono: 'Fira Code', monospace;
        --shadow-xs: 0 1px 2px rgba(0, 0, 0, 0.04);
        --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.08), 0 1px 2px rgba(0, 0, 0, 0.04);
        --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.08), 0 2px 4px -1px rgba(0, 0, 0, 0.04);
        --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.08), 0 4px 6px -2px rgba(0, 0, 0, 0.03);
    }

    body {
        font-family: var(--font-sans);
        background-color: var(--bg-main);
        color: var(--text-main);
        line-height: 1.7;
        margin: 0;
        padding: 0;
        -webkit-font-smoothing: antialiased;
    }

    .topic-page-container {
        max-width: 1040px;
        margin: 0 auto;
        padding: 1.5rem 1.25rem 4rem;
    }

    .top-action-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 1rem;
        margin-bottom: 1.5rem;
    }

    .breadcrumb-trail {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        font-size: 0.85rem;
        color: var(--text-muted);
        font-weight: 500;
        flex-wrap: wrap;
    }

    .breadcrumb-trail a {
        color: var(--text-sub);
        transition: color 0.2s ease;
        text-decoration: none;
    }

    .breadcrumb-trail a:hover {
        color: var(--brand-emerald);
    }

    .lang-toggle-btn {
        background: var(--bg-surface);
        border: 2px solid var(--brand-emerald);
        padding: 0.45rem 1.1rem;
        border-radius: 999px;
        cursor: pointer;
        font-size: 0.88rem;
        font-weight: 700;
        color: var(--brand-emerald-dark);
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        transition: all 0.2s ease;
        box-shadow: var(--shadow-xs);
    }

    .lang-toggle-btn:hover {
        background: var(--brand-emerald);
        color: #ffffff;
        transform: translateY(-1px);
        box-shadow: var(--shadow-sm);
    }

    /* Fixed Navigation Buttons */
    .portal-nav-bar {
        display: flex;
        gap: 0.75rem;
        margin-bottom: 1.5rem;
        flex-wrap: wrap;
    }

    .portal-nav-btn {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.55rem 1.15rem;
        border-radius: 10px;
        font-size: 0.88rem;
        font-weight: 700;
        text-decoration: none;
        background: #ffffff !important;
        border: 1px solid var(--border-medium) !important;
        color: #1e293b !important;
        transition: all 0.2s ease;
        box-shadow: 0 1px 3px rgba(15, 23, 42, 0.08);
    }

    .portal-nav-btn i {
        color: var(--brand-emerald);
        font-size: 0.95rem;
    }

    .portal-nav-btn span {
        color: #1e293b !important;
    }

    .portal-nav-btn:hover {
        background: #f1f5f9 !important;
        border-color: var(--brand-emerald) !important;
        transform: translateY(-1px);
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }

    /* Topic Hero Card: explicit display block and height auto so it NEVER gets squished */
    .topic-hero-card {
        display: block !important;
        height: auto !important;
        min-height: 180px;
        box-sizing: border-box !important;
        background: linear-gradient(135deg, #f0fdf4 0%, #ffffff 50%, #f0fdfa 100%);
        border: 1px solid #bbf7d0;
        border-radius: 16px;
        padding: 2.25rem 2rem;
        margin-bottom: 2rem;
        box-shadow: var(--shadow-sm);
        position: relative;
        overflow: hidden;
    }

    .topic-hero-card::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, var(--brand-emerald), #06b6d4, var(--brand-indigo));
    }

    .topic-badge-row {
        display: flex;
        gap: 0.6rem;
        flex-wrap: wrap;
        margin-bottom: 1rem;
    }

    .topic-badge {
        font-size: 0.78rem;
        font-weight: 700;
        padding: 0.3rem 0.75rem;
        border-radius: 6px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    .topic-badge.num { background: #dcfce7; color: #166534; border: 1px solid #bbf7d0; }
    .topic-badge.subject { background: #e0e7ff; color: #3730a3; border: 1px solid #c7d2fe; }
    .topic-badge.weightage { background: #fef3c7; color: #92400e; border: 1px solid #fde68a; }

    .topic-title {
        font-size: 2.15rem;
        font-weight: 800;
        color: var(--text-main);
        line-height: 1.25;
        margin-bottom: 0.75rem;
    }

    .topic-subtitle {
        font-size: 1.05rem;
        color: var(--text-sub);
        line-height: 1.6;
        margin-bottom: 1.5rem;
    }

    .progress-tracker-bar {
        background: var(--bg-surface);
        border: 1px solid var(--border-subtle);
        border-radius: 12px;
        padding: 1.1rem 1.35rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 1rem;
        box-shadow: var(--shadow-xs);
    }

    .tracker-status {
        display: flex;
        align-items: center;
        gap: 0.75rem;
    }

    .status-check-circle {
        width: 32px;
        height: 32px;
        border-radius: 50%;
        background: #ecfdf5;
        color: var(--brand-emerald);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1rem;
        border: 2px solid #a7f3d0;
    }

    .status-check-circle.completed {
        background: var(--brand-emerald);
        color: #ffffff;
        border-color: var(--brand-emerald-dark);
    }

    .tracker-btn {
        background: var(--brand-emerald);
        color: #ffffff;
        border: none;
        padding: 0.55rem 1.25rem;
        border-radius: 8px;
        font-weight: 700;
        font-size: 0.88rem;
        cursor: pointer;
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        transition: all 0.2s ease;
    }

    .tracker-btn:hover {
        background: var(--brand-emerald-dark);
        transform: translateY(-1px);
    }

    .content-card {
        background: var(--bg-surface);
        border: 1px solid var(--border-subtle);
        border-radius: 16px;
        padding: 2.25rem 2rem;
        margin-bottom: 2rem;
        box-shadow: var(--shadow-sm);
    }

    .content-card h2 {
        font-size: 1.5rem;
        font-weight: 800;
        color: var(--text-main);
        display: flex;
        align-items: center;
        gap: 0.75rem;
        margin-top: 0;
        margin-bottom: 1.5rem;
        padding-bottom: 0.75rem;
        border-bottom: 2px solid #f1f5f9;
    }

    .content-card h3 {
        font-size: 1.2rem;
        font-weight: 700;
        color: var(--text-main);
        margin-top: 1.75rem;
        margin-bottom: 0.75rem;
    }

    .rule-box {
        background: #f8fafc;
        border-left: 4px solid var(--brand-emerald);
        border-radius: 0 10px 10px 0;
        padding: 1.15rem 1.35rem;
        margin: 1.25rem 0;
        border-top: 1px solid #e2e8f0;
        border-right: 1px solid #e2e8f0;
        border-bottom: 1px solid #e2e8f0;
    }

    .rule-box.indigo {
        border-left-color: var(--brand-indigo);
        background: #f8faff;
    }

    .rule-box.amber {
        border-left-color: var(--brand-amber);
        background: #fffbeb;
    }

    .rule-box.rose {
        border-left-color: var(--brand-rose);
        background: #fff1f2;
    }

    /* Embedded Worked Example Box */
    .worked-example-box {
        background: #f0fdf4;
        border: 1.5px solid #86efac;
        border-radius: 12px;
        padding: 1.35rem 1.5rem;
        margin: 1.5rem 0;
        position: relative;
    }

    .worked-example-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 0.75rem;
        flex-wrap: wrap;
        gap: 0.5rem;
    }

    .worked-example-title {
        font-size: 0.98rem;
        font-weight: 800;
        color: #166534;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    .speed-badge {
        background: #dcfce7;
        color: #15803d;
        border: 1px solid #86efac;
        font-size: 0.75rem;
        font-weight: 800;
        padding: 0.2rem 0.6rem;
        border-radius: 999px;
        text-transform: uppercase;
    }

    .method-compare-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1rem;
        margin-top: 0.75rem;
    }

    @media (max-width: 768px) {
        .method-compare-grid {
            grid-template-columns: 1fr;
        }
    }

    .method-col {
        background: #ffffff;
        border-radius: 8px;
        padding: 1rem;
        border: 1px solid #d1fae5;
    }

    .method-col.standard {
        border-left: 3px solid #94a3b8;
    }

    .method-col.topper {
        border-left: 3px solid #10b981;
        background: #f7fee7;
    }

    .method-label {
        font-size: 0.78rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 0.4rem;
    }

    .method-label.standard { color: #64748b; }
    .method-label.topper { color: #15803d; }

    .formula-table-wrap {
        overflow-x: auto;
        margin: 1.5rem 0;
        border-radius: 10px;
        border: 1px solid var(--border-subtle);
    }

    .formula-table {
        width: 100%;
        border-collapse: collapse;
        text-align: left;
        font-size: 0.92rem;
    }

    .formula-table th {
        background: #f1f5f9;
        color: var(--text-main);
        font-weight: 700;
        padding: 0.85rem 1rem;
        border-bottom: 1px solid var(--border-medium);
    }

    .formula-table td {
        padding: 0.85rem 1rem;
        border-bottom: 1px solid var(--border-subtle);
        color: var(--text-sub);
    }

    .formula-table tr:last-child td {
        border-bottom: none;
    }

    .formula-table tr:hover td {
        background: #f8fafc;
    }

    /* Traps Grid */
    .traps-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1.25rem;
        margin-top: 1.25rem;
    }

    @media (max-width: 768px) {
        .traps-grid {
            grid-template-columns: 1fr;
        }
    }

    .trap-item {
        background: #ffffff;
        border: 1.5px solid #fecdd3;
        border-radius: 12px;
        padding: 1.25rem;
        position: relative;
    }

    .trap-item::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 6px;
        bottom: 0;
        background: var(--brand-rose);
        border-radius: 12px 0 0 12px;
    }

    .trap-badge {
        font-size: 0.75rem;
        font-weight: 800;
        color: var(--brand-rose);
        text-transform: uppercase;
        margin-bottom: 0.35rem;
        display: flex;
        align-items: center;
        gap: 0.4rem;
    }

    .trap-title {
        font-size: 1.05rem;
        font-weight: 700;
        color: #9f1239;
        margin-bottom: 0.5rem;
    }

    .trap-golden-rule {
        background: #fff1f2;
        border-radius: 6px;
        padding: 0.6rem 0.85rem;
        font-size: 0.85rem;
        color: #881337;
        margin-top: 0.6rem;
        border: 1px dashed #f43f5e;
    }

    /* Type Banner in Practice */
    .type-banner {
        background: linear-gradient(90deg, #f0fdf4 0%, #ecfdf5 100%);
        border: 1px solid #a7f3d0;
        border-left: 4px solid var(--brand-emerald);
        border-radius: 8px;
        padding: 0.75rem 1.25rem;
        margin: 2rem 0 1.25rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 0.5rem;
    }

    .type-banner-title {
        font-size: 1.02rem;
        font-weight: 800;
        color: #065f46;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    .type-banner-tag {
        font-size: 0.75rem;
        font-weight: 700;
        background: #dcfce7;
        color: #15803d;
        padding: 0.2rem 0.6rem;
        border-radius: 999px;
    }

    .mcq-question-card {
        background: #ffffff;
        border: 1px solid var(--border-subtle);
        border-radius: 12px;
        padding: 1.35rem 1.5rem;
        margin-bottom: 1.25rem;
        transition: box-shadow 0.2s ease;
    }

    .mcq-question-card:hover {
        box-shadow: var(--shadow-md);
    }

    .mcq-header {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        margin-bottom: 0.75rem;
        gap: 0.5rem;
    }

    .mcq-number {
        font-size: 0.82rem;
        font-weight: 800;
        background: #f1f5f9;
        color: #475569;
        padding: 0.25rem 0.65rem;
        border-radius: 6px;
    }

    .mcq-exam-tag {
        font-size: 0.75rem;
        font-weight: 700;
        color: #0369a1;
        background: #e0f2fe;
        padding: 0.2rem 0.6rem;
        border-radius: 999px;
    }

    .mcq-text {
        font-size: 1.02rem;
        font-weight: 600;
        color: var(--text-main);
        line-height: 1.6;
        margin-bottom: 1rem;
    }

    .options-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 0.65rem;
        margin-bottom: 1rem;
    }

    @media (max-width: 640px) {
        .options-grid {
            grid-template-columns: 1fr;
        }
    }

    .option-btn {
        background: #f8fafc;
        border: 1px solid var(--border-subtle);
        border-radius: 8px;
        padding: 0.7rem 1rem;
        text-align: left;
        font-size: 0.92rem;
        font-weight: 500;
        color: var(--text-sub);
        cursor: pointer;
        display: flex;
        align-items: center;
        gap: 0.6rem;
        transition: all 0.15s ease;
    }

    .option-btn:hover:not(.disabled) {
        background: #f1f5f9;
        border-color: var(--border-medium);
    }

    .option-btn.correct {
        background: #dcfce7 !important;
        border-color: #86efac !important;
        color: #166534 !important;
        font-weight: 700;
    }

    .option-btn.incorrect {
        background: #fee2e2 !important;
        border-color: #fca5a5 !important;
        color: #991b1b !important;
    }

    .option-prefix {
        width: 24px;
        height: 24px;
        border-radius: 50%;
        background: #ffffff;
        border: 1px solid #cbd5e1;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 0.78rem;
        font-weight: 700;
        flex-shrink: 0;
    }

    .explanation-box {
        display: none;
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-left: 4px solid #3b82f6;
        border-radius: 0 8px 8px 0;
        padding: 1rem 1.25rem;
        font-size: 0.9rem;
        color: var(--text-sub);
        margin-top: 0.75rem;
    }

    .explanation-box.visible {
        display: block;
        animation: fadeIn 0.3s ease;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-4px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .cheat-sheet-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 1rem;
        margin-top: 1rem;
    }

    .cheat-sheet-card {
        background: #ffffff;
        border: 1px solid var(--border-subtle);
        border-radius: 10px;
        padding: 1.1rem;
        border-top: 3px solid var(--brand-emerald);
    }

    .cheat-sheet-card h4 {
        margin: 0 0 0.5rem;
        font-size: 0.95rem;
        color: var(--text-main);
    }

    .footer-nav-hub {
        background: #ffffff;
        border: 1px solid var(--border-subtle);
        border-radius: 14px;
        padding: 1.5rem;
        margin-top: 3rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 1rem;
    }

    .footer-nav-item {
        display: flex;
        flex-direction: column;
        text-decoration: none;
    }

    .footer-nav-label {
        font-size: 0.75rem;
        font-weight: 700;
        color: var(--text-muted);
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    .footer-nav-title {
        font-size: 0.95rem;
        font-weight: 700;
        color: var(--brand-emerald-dark);
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    .footer-nav-item:hover .footer-nav-title {
        color: var(--brand-emerald);
    }

    .vbodmas-steps-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 1rem;
        margin: 1.5rem 0;
    }

    .vbodmas-step-card {
        background: #ffffff;
        border: 1px solid var(--border-subtle);
        border-radius: 10px;
        padding: 1.1rem;
        position: relative;
        box-shadow: var(--shadow-xs);
        transition: transform 0.2s ease;
    }

    .vbodmas-step-card:hover {
        transform: translateY(-2px);
    }

    .vbodmas-letter {
        font-size: 1.75rem;
        font-weight: 800;
        margin-bottom: 0.25rem;
    }

    .vbodmas-step-card.v .vbodmas-letter { color: #dc2626; }
    .vbodmas-step-card.b .vbodmas-letter { color: #ea580c; }
    .vbodmas-step-card.o .vbodmas-letter { color: #d97706; }
    .vbodmas-step-card.d .vbodmas-letter { color: #059669; }
    .vbodmas-step-card.m .vbodmas-letter { color: #0284c7; }
    .vbodmas-step-card.a .vbodmas-letter { color: #4f46e5; }
    .vbodmas-step-card.s .vbodmas-letter { color: #7c3aed; }

    .vbodmas-title {
        font-size: 0.95rem;
        font-weight: 700;
        color: var(--text-main);
        margin-bottom: 0.35rem;
    }

    .vbodmas-desc {
        font-size: 0.83rem;
        color: var(--text-sub);
        line-height: 1.5;
    }

    /* Bilingual display rules */
    body.lang-hindi .lang-en { display: none !important; }
    body.lang-english .lang-hi { display: none !important; }
</style>
</head>
<body class="lang-hindi">
<div class="topic-page-container">
`;
}

function getScripts(topicKey) {
  return `
<!-- Persistent Language & Completion Script -->
<script>
    function setLanguage(lang) {
        if (lang === 'english') {
            document.body.classList.remove('lang-hindi');
            document.body.classList.add('lang-english');
            localStorage.setItem('sjmaths_preferred_language', 'english');
        } else {
            document.body.classList.remove('lang-english');
            document.body.classList.add('lang-hindi');
            localStorage.setItem('sjmaths_preferred_language', 'hindi');
        }
    }

    function toggleLocalLanguage() {
        if (document.body.classList.contains('lang-hindi')) {
            setLanguage('english');
        } else {
            setLanguage('hindi');
        }
    }

    function checkMcqAnswer(qId, selectedIdx, isCorrect) {
        const card = document.getElementById(qId);
        if (!card) return;
        const buttons = card.querySelectorAll('.option-btn');
        buttons.forEach((btn, idx) => {
            btn.classList.add('disabled');
            if (idx === selectedIdx) {
                if (isCorrect) {
                    btn.classList.add('correct');
                } else {
                    btn.classList.add('incorrect');
                }
            }
        });
        const exp = document.getElementById(qId + '-exp');
        if (exp) {
            exp.classList.add('visible');
        }
    }

    function toggleTopicCompletion(topicKey) {
        const current = localStorage.getItem('sjmaths_' + topicKey) === 'completed';
        const newStatus = current ? 'incomplete' : 'completed';
        localStorage.setItem('sjmaths_' + topicKey, newStatus);
        updateCompletionUI(newStatus === 'completed');
    }

    function updateCompletionUI(isCompleted) {
        const icon = document.getElementById('topicStatusIcon');
        const btnText = document.getElementById('completeBtnText');
        if (isCompleted) {
            icon.classList.add('completed');
            btnText.innerHTML = '<span class="lang-hi">Completed (पूर्ण हुआ) ✔</span><span class="lang-en">Completed ✔</span>';
        } else {
            icon.classList.remove('completed');
            btnText.innerHTML = '<span class="lang-hi">Mark as Completed (पूर्ण करें)</span><span class="lang-en">Mark as Completed</span>';
        }
    }

    document.addEventListener('DOMContentLoaded', () => {
        const savedLang = localStorage.getItem('sjmaths_preferred_language') || 'hindi';
        setLanguage(savedLang);

        const topicStatus = localStorage.getItem('sjmaths_${topicKey}') === 'completed';
        updateCompletionUI(topicStatus);
    });
</script>
</body>
</html>
`;
}

console.log('Template generator loaded.');
module.exports = { getHead, getScripts, safeWrite };
