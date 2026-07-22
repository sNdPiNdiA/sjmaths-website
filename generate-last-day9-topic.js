const fs = require('fs');
const path = require('path');
const https = require('https');

const envContent = fs.readFileSync('c:/Users/sande/Documents/GitHub/sjmaths-website/.env', 'utf8');
const apiKey = envContent.match(/GEMINI_API_KEY\s*=\s*(.*)/)[1].trim();

const topicTitle = "Biot-Savart law for vortex tubes";
const topicSlug = "biot-savart-law-for-vortex-tubes";
const filePath = path.join('c:/Users/sande/Documents/GitHub/sjmaths-website/upsc-aso/day-9', topicSlug, 'index.html');

const prompt = `You are a world-renowned professor of Fluid Dynamics & Aeronautical Engineering and UPSC Air Safety Officer (ASO) exam author.
Generate an exhaustive, beginner-friendly study module for "${topicTitle}".
Cover zero-to-hero theory, 30 practice MCQs, and 10 mini test questions.
Format using LaTeX delimiters $...$ and $$...$$ and section tags:
SECTION_UNDERSTAND_START ... SECTION_UNDERSTAND_END
SECTION_LEARN_START ... SECTION_LEARN_END
SECTION_MEMORIZE_START ... SECTION_MEMORIZE_END
SECTION_AVIATION_START ... SECTION_AVIATION_END
SECTION_UPSC_START ... SECTION_UPSC_END
SECTION_PRACTICE_START ... (30 MCQs) ... SECTION_PRACTICE_END
SECTION_MINITEST_START ... (10 MCQs) ... SECTION_MINITEST_END
SECTION_ERROR_START ... SECTION_ERROR_END
SECTION_ACTIVERECALL_START ... SECTION_ACTIVERECALL_END`;

function extractSections(aiText) {
    function getSection(startTag, endTag) {
        const regex = new RegExp(`${startTag}([\\s\\S]*?)${endTag}`);
        const match = aiText.match(regex);
        return match ? match[1].trim() : '';
    }
    return {
        understandHTML: getSection('SECTION_UNDERSTAND_START', 'SECTION_UNDERSTAND_END') || '<p>Definition of Biot-Savart law for vortex tubes.</p>',
        learnConceptHTML: getSection('SECTION_LEARN_START', 'SECTION_LEARN_END') || '<p>Mathematical derivation and physical principles of vortex filaments.</p>',
        memorizeFactsHTML: getSection('SECTION_MEMORIZE_START', 'SECTION_MEMORIZE_END') || '<ul><li>Induced velocity formula: $d\\vec{V} = \\frac{\\Gamma}{4\\pi} \\frac{d\\vec{s} \\times \\vec{r}}{r^3}$</li></ul>',
        aviationAppHTML: getSection('SECTION_AVIATION_START', 'SECTION_AVIATION_END') || '<p>Application in aircraft wingtip vortices and downwash calculation.</p>',
        upscFocusHTML: getSection('SECTION_UPSC_START', 'SECTION_UPSC_END') || '<ul><li>UPSC exam traps and vortex tube theorems.</li></ul>',
        practiceMCQsHTML: getSection('SECTION_PRACTICE_START', 'SECTION_PRACTICE_END') || '<div>Practice MCQs</div>',
        miniTestMCQsHTML: getSection('SECTION_MINITEST_START', 'SECTION_MINITEST_END') || '<div>Mini Test MCQs</div>',
        errorAnalysisHTML: getSection('SECTION_ERROR_START', 'SECTION_ERROR_END') || '<p>Common student error traps.</p>',
        activeRecallHTML: getSection('SECTION_ACTIVERECALL_START', 'SECTION_ACTIVERECALL_END') || '<p>Active recall flash facts.</p>'
    };
}

function buildHTMLPage(sections) {
    return `<!DOCTYPE html>
<html lang="en">
<head>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7924751316191829" crossorigin="anonymous"></script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Day 9: ${topicTitle} | UPSC Air Safety Officer (ASO) Study Hub</title>
    <meta name="description" content="Study module for ${topicTitle} under UPSC ASO Day 9.">
    <link rel="canonical" href="https://sjmaths.com/upsc-aso/day-9/${topicSlug}/">
    <link rel="icon" type="image/png" href="/favicon.png">

    <!-- Fonts and Icons -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@500;600;700;800&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/assets/vendor/fontawesome/css/all.min.css?v=7441465c">

    <!-- Stylesheets -->
    <link rel="stylesheet" href="/assets/css/main.min.css?v=4ba21ce7">
    <link rel="stylesheet" href="/assets/css/layout.min.css?v=e4922b08">
    <link rel="stylesheet" href="/assets/css/component.min.css?v=8c99f11f">
    <link rel="stylesheet" href="/assets/css/improved-ui.min.css?v=574ed909">

    <!-- MathJax 3 -->
    <script>
    MathJax = {
      tex: {
        inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
        displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']],
        processEscapes: true
      },
      options: {
        ignoreHtmlClass: 'tex2jax_ignore',
        processHtmlClass: 'tex2jax_process'
      }
    };
    </script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

    <style>
        :root {
            --glass-bg: rgba(255, 255, 255, 0.96);
            --glass-border: rgba(255, 255, 255, 0.25);
            --shadow-lg: 0 10px 30px -5px rgba(30, 60, 114, 0.12);
            --accent-gradient: linear-gradient(135deg, #1e3c72, #2a5298, #d4af37);
        }

        .module-container {
            max-width: 1100px;
            margin: 2rem auto;
            padding: 2rem 1.5rem;
        }

        .breadcrumb-nav {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            font-size: 0.9rem;
            color: #718096;
            margin-bottom: 1.5rem;
        }

        .breadcrumb-nav a {
            color: #2b6cb0;
            text-decoration: none;
        }

        .breadcrumb-nav a:hover {
            text-decoration: underline;
        }

        .module-header {
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            border-radius: 1.25rem;
            padding: 2rem;
            box-shadow: var(--shadow-lg);
            margin-bottom: 2rem;
            position: relative;
            overflow: hidden;
        }

        .module-header::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 5px;
            height: 100%;
            background: var(--accent-gradient);
        }

        .module-header h1 {
            font-family: 'Outfit', sans-serif;
            font-size: 2.2rem;
            font-weight: 800;
            color: #1a202c;
            margin-bottom: 0.75rem;
        }

        .module-badges {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            flex-wrap: wrap;
        }

        .badge-tag {
            font-size: 0.8rem;
            font-weight: 700;
            padding: 4px 12px;
            border-radius: 20px;
            background: rgba(30, 60, 114, 0.08);
            color: #1e3c72;
        }

        .main-tabs {
            display: flex;
            gap: 0.75rem;
            margin-bottom: 2rem;
            border-bottom: 2px solid #e2e8f0;
            padding-bottom: 0.5rem;
            flex-wrap: wrap;
        }

        .tab-button {
            background: transparent;
            border: none;
            outline: none;
            font-family: 'Outfit', sans-serif;
            font-size: 1rem;
            font-weight: 700;
            color: #718096;
            padding: 0.75rem 1.25rem;
            cursor: pointer;
            border-radius: 10px;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .tab-button:hover {
            color: #1e3c72;
            background: rgba(30, 60, 114, 0.05);
        }

        .tab-button.active {
            color: #ffffff;
            background: var(--accent-gradient);
            box-shadow: 0 4px 15px rgba(30, 60, 114, 0.25);
        }

        .tab-content-panel {
            display: none;
            animation: fadeIn 0.4s ease-out;
        }

        .tab-content-panel.active {
            display: block;
        }

        .step-card {
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            border-radius: 1rem;
            padding: 1.75rem;
            box-shadow: 0 4px 12px rgba(0,0,0,0.03);
            margin-bottom: 1.75rem;
        }

        .step-title {
            font-family: 'Outfit', sans-serif;
            font-size: 1.3rem;
            font-weight: 700;
            color: #1e3c72;
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
            gap: 0.6rem;
            border-bottom: 1px solid #edf2f7;
            padding-bottom: 0.6rem;
        }

        .step-title i {
            color: #d4af37;
        }

        .content-box {
            font-size: 1rem;
            line-height: 1.75;
            color: #2d3748;
        }

        .formula-card {
            background: #f7fafc;
            border-left: 4px solid #3182ce;
            padding: 1.25rem;
            border-radius: 8px;
            font-family: 'Fira Code', monospace;
            margin: 1.25rem 0;
            overflow-x: auto;
        }

        .mcq-card {
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.02);
        }

        .mcq-question {
            font-weight: 600;
            font-size: 1.05rem;
            color: #1a202c;
            margin-bottom: 1rem;
            line-height: 1.6;
        }

        .mcq-options {
            display: flex;
            flex-direction: column;
            gap: 0.6rem;
            margin-bottom: 1rem;
        }

        .mcq-option {
            padding: 0.75rem 1rem;
            border: 1px solid #cbd5e0;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.2s ease;
            font-size: 0.95rem;
        }

        .mcq-option:hover {
            border-color: #3182ce;
            background: #ebf8ff;
        }

        .mcq-option.correct {
            border-color: #38a169;
            background: #c6f6d5;
            color: #22543d;
            font-weight: 600;
        }

        .mcq-option.incorrect {
            border-color: #e53e3e;
            background: #fed7d7;
            color: #742a2a;
        }

        .explanation-box {
            display: none;
            background: #f7fafc;
            border: 1px solid #e2e8f0;
            padding: 1rem 1.25rem;
            border-radius: 8px;
            margin-top: 1rem;
            font-size: 0.92rem;
            color: #4a5568;
            line-height: 1.6;
        }

        .check-btn {
            background: #3182ce;
            color: white;
            border: none;
            padding: 0.5rem 1.25rem;
            border-radius: 6px;
            font-weight: 600;
            cursor: pointer;
            transition: background 0.2s ease;
        }

        .check-btn:hover {
            background: #2b6cb0;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(8px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>
<body>
    <div id="header-container"></div>

    <main class="module-container" id="main-content">
        <div class="breadcrumb-nav">
            <a href="/">Home</a> <i class="fas fa-chevron-right" style="font-size: 0.7rem;"></i>
            <a href="/upsc-aso/">UPSC ASO Hub</a> <i class="fas fa-chevron-right" style="font-size: 0.7rem;"></i>
            <span>Day 9 • ${topicTitle}</span>
        </div>

        <div class="module-header">
            <h1>${topicTitle}</h1>
            <div class="module-badges">
                <span class="badge-tag"><i class="fas fa-calendar-day"></i> Day 9 of 129</span>
                <span class="badge-tag"><i class="fas fa-water"></i> Fluid Mechanics & Machinery</span>
                <span class="badge-tag"><i class="fas fa-layer-group"></i> Phase 1: Foundations</span>
                <span class="badge-tag"><i class="far fa-clock"></i> 90-120 min Master Class</span>
            </div>
        </div>

        <div class="main-tabs">
            <button class="tab-button active" onclick="switchTab('tab-concepts', this)">
                <i class="fas fa-book-open"></i> 1. Basic-to-Advanced Concepts & Theories
            </button>
            <button class="tab-button" onclick="switchTab('tab-practice', this)">
                <i class="fas fa-tasks"></i> 2. UPSC Practice Questions (30 MCQs)
            </button>
            <button class="tab-button" onclick="switchTab('tab-minitest', this)">
                <i class="fas fa-vial"></i> 3. Mini Test (10 Questions)
            </button>
            <button class="tab-button" onclick="switchTab('tab-activerecall', this)">
                <i class="fas fa-brain"></i> 4. Active Recall & Error Analysis
            </button>
        </div>

        <div id="tab-concepts" class="tab-content-panel active">
            <div class="step-card">
                <h2 class="step-title"><i class="fas fa-lightbulb"></i> 1. Understand (From Absolute Zero, 5–10 min)</h2>
                <div class="content-box">${sections.understandHTML}</div>
            </div>
            <div class="step-card">
                <h2 class="step-title"><i class="fas fa-graduation-cap"></i> 2. Learn the Concept (20–25 min)</h2>
                <div class="content-box">${sections.learnConceptHTML}</div>
            </div>
            <div class="step-card">
                <h2 class="step-title"><i class="fas fa-brain"></i> 3. Memorize Important Facts (10 min)</h2>
                <div class="content-box">${sections.memorizeFactsHTML}</div>
            </div>
            <div class="step-card">
                <h2 class="step-title"><i class="fas fa-plane-flight"></i> 4. Aviation Application (5–10 min)</h2>
                <div class="content-box">${sections.aviationAppHTML}</div>
            </div>
            <div class="step-card">
                <h2 class="step-title"><i class="fas fa-bullseye"></i> 5. UPSC ASO Focus (10 min)</h2>
                <div class="content-box">${sections.upscFocusHTML}</div>
            </div>
        </div>

        <div id="tab-practice" class="tab-content-panel">
            <div class="step-card">
                <h2 class="step-title"><i class="fas fa-pen-nib"></i> 6. Practice Questions (30 Exhaustive UPSC ASO MCQs)</h2>
                ${sections.practiceMCQsHTML}
            </div>
        </div>

        <div id="tab-minitest" class="tab-content-panel">
            <div class="step-card">
                <h2 class="step-title"><i class="fas fa-stopwatch"></i> 7. Grand Mini Test (10 Exam-Level Questions)</h2>
                ${sections.miniTestMCQsHTML}
            </div>
        </div>

        <div id="tab-activerecall" class="tab-content-panel">
            <div class="step-card">
                <h2 class="step-title"><i class="fas fa-bug"></i> 8. Error Analysis & Common Traps (5 min)</h2>
                <div class="content-box">${sections.errorAnalysisHTML}</div>
            </div>
            <div class="step-card">
                <h2 class="step-title"><i class="fas fa-rotate-right"></i> 9. Active Recall & Quick Revision (5 min)</h2>
                <div class="content-box">${sections.activeRecallHTML}</div>
            </div>
        </div>
    </main>

    <script>
        function switchTab(tabId, btn) {
            document.querySelectorAll('.tab-button').forEach(b => b.classList.remove('active'));
            document.querySelectorAll('.tab-content-panel').forEach(p => p.classList.remove('active'));
            btn.classList.add('active');
            document.getElementById(tabId).classList.add('active');
        }

        let selectedOptions = {};

        function selectOption(el, qId) {
            const parent = el.closest('.mcq-options');
            parent.querySelectorAll('.mcq-option').forEach(o => {
                o.classList.remove('correct', 'incorrect');
            });
            selectedOptions[qId] = el;
        }

        function checkMCQ(qId, correctOpt) {
            const selected = selectedOptions[qId];
            const explain = document.getElementById('explain-' + qId);
            if (!selected) {
                alert('Please select an option first!');
                return;
            }
            const chosenText = selected.getAttribute('data-opt');
            if (chosenText === correctOpt) {
                selected.classList.add('correct');
            } else {
                selected.classList.add('incorrect');
            }
            if (explain) explain.style.display = 'block';
        }
    </script>

    <footer id="site-footer"></footer>
    <script src="/assets/js/main.min.js?v=10f0770d" defer></script>
    <script src="/assets/js/global-header.min.js?v=d6ad26b3" defer></script>
    <script src="/assets/js/global-footer.min.js?v=c641c625" defer></script>
</body>
</html>`;
}

// Call API
const payload = JSON.stringify({ contents: [{ parts: [{ text: prompt }] }] });
const url = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=${apiKey}`;

console.log('Generating final Day 9 topic via Gemini 2.5 Flash...');
const req = https.request(url, {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'Content-Length': Buffer.byteLength(payload)
    }
}, res => {
    let d = '';
    res.on('data', c => d += c);
    res.on('end', () => {
        try {
            const json = JSON.parse(d);
            const text = json.candidates[0].content.parts[0].text;
            const sections = extractSections(text);
            const fullHTML = buildHTMLPage(sections);

            const dirPath = path.join('c:/Users/sande/Documents/GitHub/sjmaths-website/upsc-aso/day-9', topicSlug);
            if (!fs.existsSync(dirPath)) {
                fs.mkdirSync(dirPath, { recursive: true });
            }
            fs.writeFileSync(filePath, fullHTML);
            console.log(`Successfully generated and saved ${filePath}`);
        } catch (e) {
            console.error('Error generating Biot-Savart topic:', e.message);
        }
    });
});

req.write(payload);
req.end();
