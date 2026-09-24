const fs = require('fs');
const path = require('path');

function convertMicrotopicContent(html) {
  // 1. Remove dark-mode class from html and body
  html = html.replace(/<html([^>]*)\s+class="dark-mode"([^>]*)>/i, '<html$1$2>');
  html = html.replace(/<html([^>]*)\s+class='dark-mode'([^>]*)>/i, '<html$1$2>');
  html = html.replace(/<body([^>]*)\s+class="dark-mode"([^>]*)>/i, '<body$1$2>');
  html = html.replace(/<body([^>]*)\s+class='dark-mode'([^>]*)>/i, '<body$1$2>');

  // 2. Replace :root dark variables with stress-free daylight tokens
  const oldRootRegex = /:root\s*\{[\s\S]*?--text-muted:\s*#64748b;\s*\}/;
  const newRoot = `:root {
            --bg-void: #f8fafc;
            --bg-surface: #ffffff;
            --bg-card: #ffffff;
            --bg-card-hover: #f1f5f9;
            --border-glass: #e2e8f0;
            --border-accent: rgba(37, 99, 235, 0.25);
            --cyan-primary: #0284c7;
            --cyan-glow: rgba(2, 132, 199, 0.12);
            --indigo-accent: #4f46e5;
            --emerald-accent: #059669;
            --amber-accent: #d97706;
            --text-main: #0f172a;
            --text-sub: #475569;
            --text-muted: #64748b;
        }`;
  html = html.replace(oldRootRegex, newRoot);

  // 3. Update html, body
  const oldBodyRegex = /html,\s*body\s*\{[\s\S]*?min-height:\s*100vh;\s*\}/;
  const newBody = `html, body {
            background-color: var(--bg-void) !important;
            background: #f8fafc !important;
            color: #1e293b !important;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            margin: 0;
            padding: 0;
            line-height: 1.7;
            min-height: 100vh;
            -webkit-font-smoothing: antialiased;
        }`;
  html = html.replace(oldBodyRegex, newBody);

  // 4. Update topbar
  html = html.replace(
    /\.sj-topbar\s*\{[\s\S]*?box-shadow:\s*0\s+4px\s+20px\s+rgba\(0,\s*0,\s*0,\s*0\.4\);\s*\}/,
    `.sj-topbar {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(12px);
            border-bottom: 1px solid var(--border-glass);
            position: sticky;
            top: 0;
            z-index: 1000;
            padding: 0.75rem 1.5rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
        }`
  );

  // 5. Update breadcrumb-trail hover
  html = html.replace(
    /\.breadcrumb-trail\s+a:hover\s*\{\s*color:\s*#ffffff;\s*text-decoration:\s*underline;\s*\}/,
    `.breadcrumb-trail a:hover {
            color: var(--cyan-primary);
            text-decoration: underline;
        }`
  );

  // 6. Update micro-hero
  html = html.replace(
    /\.micro-hero\s*\{[\s\S]*?min-height:\s*auto\s*!important;\s*\}/,
    `.micro-hero {
            background: linear-gradient(135deg, #ffffff 0%, #eff6ff 100%) !important;
            border: 1px solid var(--border-glass) !important;
            border-left: 5px solid var(--cyan-primary) !important;
            border-radius: 1rem !important;
            padding: 1.75rem 2rem !important;
            margin-bottom: 1.5rem !important;
            box-shadow: 0 2px 12px rgba(15, 23, 42, 0.04) !important;
            position: relative !important;
            overflow: hidden !important;
            display: flex !important;
            flex-direction: column !important;
            height: auto !important;
            min-height: auto !important;
        }`
  );

  // 7. Micro-hero h1 text color
  html = html.replace(
    /\.micro-hero\s+h1\s*\{([\s\S]*?)color:\s*#ffffff\s*!important;/,
    `.micro-hero h1 {$1color: #0f172a !important;`
  );

  // 8. Hero badge
  html = html.replace(
    /\.hero-badge\s*\{[\s\S]*?letter-spacing:\s*0\.5px;\s*\}/,
    `.hero-badge {
            font-size: 0.75rem;
            font-weight: 700;
            padding: 3px 10px;
            border-radius: 20px;
            background: #eff6ff;
            color: var(--cyan-primary);
            border: 1px solid #bfdbfe;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }`
  );
  html = html.replace(
    /\.hero-badge\.day-badge\s*\{[\s\S]*?border-color:\s*rgba\(129,\s*140,\s*248,\s*0\.2\);\s*\}/,
    `.hero-badge.day-badge {
            background: #eef2ff;
            color: var(--indigo-accent);
            border-color: #c7d2fe;
        }`
  );

  // 9. ASO mission banner
  html = html.replace(
    /\.aso-mission-banner\s*\{[\s\S]*?box-shadow:\s*0\s+8px\s+24px\s+rgba\(0,\s*0,\s*0,\s*0\.35\);\s*\}/,
    `.aso-mission-banner {
            background: linear-gradient(135deg, #eff6ff 0%, #f0fdf4 100%);
            border: 1px solid #bfdbfe;
            border-left: 5px solid var(--cyan-primary);
            border-radius: 14px;
            padding: 1.5rem 1.75rem;
            margin-bottom: 2rem;
            box-shadow: 0 2px 10px rgba(2, 132, 199, 0.04);
        }`
  );
  html = html.replace(
    /\.aso-mission-title\s*\{([\s\S]*?)color:\s*#ffffff;/,
    `.aso-mission-title {$1color: #0f172a;`
  );
  html = html.replace(
    /\.aso-bullets\s+li\s*\{[\s\S]*?color:\s*#e2e8f0;[\s\S]*?transition:\s*transform\s*0\.2s\s*ease,\s*border-color\s*0\.2s\s*ease;\s*\}/,
    `.aso-bullets li {
            background: #ffffff;
            border: 1px solid var(--border-glass);
            border-radius: 10px;
            padding: 1rem 1.15rem;
            font-size: 0.88rem;
            line-height: 1.6;
            color: #334155;
            transition: transform 0.2s ease, border-color 0.2s ease;
        }`
  );
  html = html.replace(
    /\.aso-bullets\s+li:hover\s*\{\s*border-color:\s*rgba\(56,\s*189,\s*248,\s*0\.4\);\s*transform:\s*translateY\(-2px\);\s*\}/,
    `.aso-bullets li:hover {
            border-color: #93c5fd;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(2, 132, 199, 0.08);
        }`
  );

  // 10. Tab Strip & Buttons
  html = html.replace(
    /\.tab-strip\s*\{[\s\S]*?scrollbar-width:\s*none;\s*\}/,
    `.tab-strip {
            display: flex;
            gap: 0.35rem;
            margin-bottom: 2rem;
            background: #f1f5f9;
            padding: 5px;
            border-radius: 12px;
            border: 1px solid var(--border-glass);
            overflow-x: auto;
            scrollbar-width: none;
        }`
  );
  html = html.replace(
    /\.tab-btn:hover\s*\{\s*color:\s*#ffffff;\s*background:\s*rgba\(255,\s*255,\s*255,\s*0\.05\);\s*\}/,
    `.tab-btn:hover {
            color: #0f172a;
            background: #e2e8f0;
        }`
  );
  html = html.replace(
    /\.tab-btn\.active\s*\{[\s\S]*?box-shadow:\s*0\s+2px\s+10px\s+rgba\(56,\s*189,\s*248,\s*0\.2\);\s*\}/,
    `.tab-btn.active {
            color: #1e40af;
            background: #ffffff;
            border: 1px solid var(--border-glass);
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
            font-weight: 700;
        }`
  );

  // 11. Pillar Cards
  html = html.replace(
    /\.pillar-card\s*\{[\s\S]*?box-shadow:\s*0\s+4px\s+15px\s+rgba\(0,\s*0,\s*0,\s*0\.25\);[\s\S]*?transition:\s*transform\s*0\.2s\s*ease,\s*border-color\s*0\.2s\s*ease;\s*\}/,
    `.pillar-card {
            background: var(--bg-card);
            border: 1px solid var(--border-glass);
            border-radius: 1rem;
            padding: 1.75rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 2px 8px rgba(15, 23, 42, 0.03);
            transition: transform 0.2s ease, border-color 0.2s ease;
        }`
  );
  html = html.replace(
    /\.pillar-title\s*\{([\s\S]*?)color:\s*#ffffff;([\s\S]*?)border-bottom:\s*1px\s+solid\s+rgba\(255,\s*255,\s*255,\s*0\.06\);/,
    `.pillar-title {$1color: #0f172a;$2border-bottom: 1px solid #f1f5f9;`
  );
  html = html.replace(
    /\.pillar-content\s*\{([\s\S]*?)color:\s*#e2e8f0;/,
    `.pillar-content {$1color: #334155;`
  );
  html = html.replace(
    /\.pillar-content\s+h3,\s*\.pillar-content\s+h4\s*\{([\s\S]*?)color:\s*#ffffff;/,
    `.pillar-content h3, .pillar-content h4 {$1color: #0f172a;`
  );

  // 12. Lead definition & concept list & step-item
  html = html.replace(
    /\.lead-definition\s*\{[\s\S]*?color:\s*#ffffff;[\s\S]*?font-weight:\s*500;\s*\}/,
    `.lead-definition {
            background: #f0f9ff;
            border-left: 4px solid var(--cyan-primary);
            border-radius: 8px;
            padding: 1rem 1.25rem;
            font-size: 1rem;
            line-height: 1.65;
            margin-bottom: 1.25rem;
            color: #0c4a6e;
            font-weight: 500;
        }`
  );
  html = html.replace(
    /\.concept-list\s+li\s*\{[\s\S]*?color:\s*#cbd5e1;\s*\}/,
    `.concept-list li {
            background: #f8fafc;
            border: 1px solid var(--border-glass);
            border-radius: 8px;
            padding: 0.85rem 1.15rem;
            line-height: 1.6;
            margin-bottom: 0 !important;
            color: #334155;
        }`
  );
  html = html.replace(
    /\.step-item\s*\{[\s\S]*?border-radius:\s*8px;[\s\S]*?margin-bottom:\s*1rem;\s*\}/,
    `.step-item {
            background: #f8fafc;
            border: 1px solid var(--border-glass);
            border-left: 3px solid var(--indigo-accent);
            border-radius: 8px;
            padding: 1rem 1.25rem;
            margin-bottom: 1rem;
        }`
  );

  // 13. Trap box
  html = html.replace(
    /\.trap-box\s*\{[\s\S]*?margin-bottom:\s*1rem;\s*\}/,
    `.trap-box {
            background: #fffbeb;
            border: 1px solid #fde68a;
            border-radius: 10px;
            padding: 1rem 1.25rem;
            margin-bottom: 1rem;
        }`
  );
  html = html.replace(
    /\.trap-header\s*\{([\s\S]*?)color:\s*#[0-9a-fA-F]+;/,
    `.trap-header {$1color: #b45309;`
  );
  html = html.replace(
    /\.safety-title\s*\{([\s\S]*?)color:\s*#[0-9a-fA-F]+;/,
    `.safety-title {$1color: #b45309;`
  );
  html = html.replace(
    /\.trap-misconception\s*\{[\s\S]*?color:\s*#fca5a5;[\s\S]*?\}/,
    `.trap-misconception {
            color: #b91c1c;
            margin: 0 0 0.4rem !important;
            font-size: 0.92rem;
            line-height: 1.5;
        }`
  );
  html = html.replace(
    /\.trap-correction\s*\{[\s\S]*?color:\s*#86efac;[\s\S]*?\}/,
    `.trap-correction {
            color: #15803d;
            margin: 0 !important;
            font-size: 0.92rem;
            line-height: 1.5;
        }`
  );

  // 14. Tables
  html = html.replace(
    /\.data-table\s*\{[\s\S]*?background:\s*var\(--bg-surface\);\s*\}/,
    `.data-table {
            width: 100%;
            border-collapse: collapse;
            font-size: 0.88rem;
            text-align: left;
            background: #ffffff;
        }`
  );
  html = html.replace(
    /\.data-table\s+th\s*\{[\s\S]*?white-space:\s*nowrap;\s*\}/,
    `.data-table th {
            background: #f1f5f9;
            color: #0f172a;
            padding: 10px 14px;
            font-weight: 700;
            border-bottom: 2px solid #cbd5e1;
            white-space: nowrap;
        }`
  );
  html = html.replace(
    /\.data-table\s+td\s*\{[\s\S]*?color:\s*#cbd5e1;\s*\}/,
    `.data-table td {
            padding: 10px 14px;
            border-bottom: 1px solid var(--border-glass);
            color: #334155;
        }`
  );
  html = html.replace(
    /\.data-table\s+tr:hover\s+td\s*\{\s*background:\s*rgba\(255,\s*255,\s*255,\s*0\.02\);\s*\}/,
    `.data-table tr:hover td {
            background: #eff6ff;
        }`
  );

  // 15. Numerical Cards
  html = html.replace(
    /\.numerical-card\s*\{[\s\S]*?margin-top:\s*1rem;\s*\}/,
    `.numerical-card {
            background: #f8fafc;
            border: 1px solid #bfdbfe;
            border-radius: 12px;
            padding: 1.5rem;
            margin-top: 1rem;
        }`
  );
  html = html.replace(
    /\.num-problem\s*\{([\s\S]*?)color:\s*#f1f5f9;/,
    `.num-problem {$1color: #1e293b;`
  );
  html = html.replace(
    /\.num-box\s*\{[\s\S]*?padding:\s*1rem;\s*\}/,
    `.num-box {
            background: #ffffff;
            border: 1px solid var(--border-glass);
            border-radius: 8px;
            padding: 1rem;
        }`
  );
  html = html.replace(
    /\.num-val\s*\{[\s\S]*?font-family:\s*'Fira Code',\s*monospace;\s*\}/,
    `.num-val {
            font-size: 0.92rem;
            color: #0f172a;
            font-family: 'Fira Code', monospace;
        }`
  );
  html = html.replace(
    /\.num-solution\s*\{[\s\S]*?margin-bottom:\s*1\.25rem;\s*\}/,
    `.num-solution {
            background: #ffffff;
            border-radius: 8px;
            padding: 1.25rem;
            border: 1px solid var(--border-glass);
            border-left: 3px solid var(--emerald-accent);
            margin-bottom: 1.25rem;
        }`
  );
  html = html.replace(
    /\.num-solution-steps\s*\{([\s\S]*?)color:\s*#e2e8f0;/,
    `.num-solution-steps {$1color: #1e293b;`
  );
  html = html.replace(
    /\.num-final-ans\s*\{[\s\S]*?font-family:\s*'Fira Code',\s*monospace;\s*\}/,
    `.num-final-ans {
            margin-top: 0.75rem;
            padding: 0.6rem 0.85rem;
            background: #ecfdf5;
            border: 1px solid #a7f3d0;
            border-radius: 6px;
            color: #065f46;
            font-weight: 600;
            font-family: 'Fira Code', monospace;
        }`
  );
  html = html.replace(
    /\.num-safety-box\s*\{[\s\S]*?padding:\s*1rem;\s*\}/,
    `.num-safety-box {
            background: #fffbeb;
            border: 1px solid #fde68a;
            border-radius: 8px;
            padding: 1rem;
        }`
  );
  html = html.replace(
    /\.safety-desc\s*\{[\s\S]*?color:\s*#fde68a;[\s\S]*?\}/,
    `.safety-desc {
            font-size: 0.88rem;
            color: #78350f;
            margin: 0;
            line-height: 1.55;
        }`
  );

  // 16. Practice MCQs
  html = html.replace(
    /\.question-card\s*\{[\s\S]*?box-shadow:\s*0\s+4px\s+12px\s+rgba\(0,\s*0,\s*0,\s*0\.2\);\s*\}/,
    `.question-card {
            background: var(--bg-card);
            border: 1px solid var(--border-glass);
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 2px 8px rgba(15, 23, 42, 0.04);
        }`
  );
  html = html.replace(
    /\.q-text\s*\{([\s\S]*?)color:\s*#ffffff;/,
    `.q-text {$1color: #0f172a;`
  );
  html = html.replace(
    /\.quiz-option\s*\{[\s\S]*?font-size:\s*0\.94rem;\s*\}/,
    `.quiz-option {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            padding: 0.75rem 1rem;
            background: #f8fafc;
            border: 1px solid var(--border-glass);
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.2s ease;
            font-size: 0.94rem;
            color: #1e293b;
        }`
  );
  html = html.replace(
    /\.quiz-option:hover\s*\{[\s\S]*?background:\s*rgba\(56,\s*189,\s*248,\s*0\.05\);\s*\}/,
    `.quiz-option:hover {
            border-color: #93c5fd;
            background: #eff6ff;
        }`
  );
  html = html.replace(
    /\.quiz-option\.correct\s*\{[\s\S]*?font-weight:\s*600;\s*\}/,
    `.quiz-option.correct {
            border-color: #86efac !important;
            background: #dcfce7 !important;
            color: #14532d !important;
            font-weight: 600;
        }`
  );
  html = html.replace(
    /\.quiz-option\.incorrect\s*\{[\s\S]*?color:\s*#fca5a5\s*!important;\s*\}/,
    `.quiz-option.incorrect {
            border-color: #fca5a5 !important;
            background: #fee2e2 !important;
            color: #7f1d1d !important;
        }`
  );
  html = html.replace(
    /\.explanation-box\s*\{[\s\S]*?margin-top:\s*1rem;\s*\}/,
    `.explanation-box {
            display: none;
            background: #f0fdf4;
            border: 1px solid #bbf7d0;
            border-radius: 8px;
            padding: 1rem 1.25rem;
            margin-top: 1rem;
        }`
  );
  html = html.replace(
    /\.exp-title\s*\{[\s\S]*?gap:\s*0\.5rem;\s*\}/,
    `.exp-title {
            font-weight: 700;
            color: #15803d;
            font-size: 0.88rem;
            margin-bottom: 0.5rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }`
  );
  html = html.replace(
    /\.exp-content\s*\{[\s\S]*?line-height:\s*1\.6;\s*\}/,
    `.exp-content {
            font-size: 0.9rem;
            color: #166534;
            line-height: 1.6;
        }`
  );

  // 17. Mini Test
  html = html.replace(
    /\.test-header-bar\s*\{[\s\S]*?gap:\s*1rem;\s*\}/,
    `.test-header-bar {
            background: var(--bg-card);
            border: 1px solid var(--border-glass);
            border-radius: 12px;
            padding: 1.25rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 1.5rem;
            flex-wrap: wrap;
            gap: 1rem;
        }`
  );
  html = html.replace(
    /\.test-question-item\s*\{[\s\S]*?border-radius:\s*12px;\s*\}/,
    `.test-question-item {
            background: var(--bg-card);
            border: 1px solid var(--border-glass);
            border-radius: 12px;
        }`
  );

  // 18. Flashcards
  html = html.replace(
    /\.flashcard-front\s*\{[\s\S]*?color:\s*#ffffff;\s*\}/,
    `.flashcard-front {
            background: var(--bg-card);
            color: #0f172a;
        }`
  );
  html = html.replace(
    /\.flashcard-back\s*\{[\s\S]*?transform:\s*rotateY\(180deg\);\s*\}/,
    `.flashcard-back {
            background: linear-gradient(135deg, #eff6ff, #f8fafc);
            border-color: #bfdbfe;
            color: #0f172a;
            transform: rotateY(180deg);
        }`
  );
  html = html.replace(
    /\.card-answer\s*\{[\s\S]*?color:\s*#f8fafc;\s*\}/,
    `.card-answer {
            font-size: 0.95rem;
            line-height: 1.55;
            color: #0f172a;
        }`
  );

  // 19. Footer
  html = html.replace(
    /\.micro-footer\s*\{[\s\S]*?background:\s*rgba\(6,\s*9,\s*17,\s*0\.6\);\s*\}/,
    `.micro-footer {
            border-top: 1px solid var(--border-glass);
            padding: 2.5rem 1rem;
            text-align: center;
            color: var(--text-muted);
            font-size: 0.85rem;
            margin-top: 4rem;
            background: #f8fafc;
        }`
  );

  return html;
}

module.exports = { convertMicrotopicContent };
