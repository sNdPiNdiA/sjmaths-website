const fs = require('fs');
const path = require('path');
const https = require('https');

// Read API Key from .env
const envContent = fs.readFileSync('c:/Users/sande/Documents/GitHub/sjmaths-website/.env', 'utf8');
const keyMatch = envContent.match(/GEMINI_API_KEY\s*=\s*(.*)/);
const apiKey = keyMatch ? keyMatch[1].trim() : '';

function slugify(text) {
    return text.toLowerCase()
        .replace(/[^a-z0-9]+/g, '-')
        .replace(/(^-|-$)+/g, '');
}

const day8Topics = [
    { title: "Continuity equation – 1D, 3D", subject: "Fluid Mechanics & Machinery", day: 8 },
    { title: "Stream function, velocity potential", subject: "Fluid Mechanics & Machinery", day: 8 },
    { title: "Bernoulli's equation – derivation & assumptions", subject: "Fluid Mechanics & Machinery", day: 8 },
    { title: "Venturimeter, Pitot tube, Orifice meter", subject: "Fluid Mechanics & Machinery", day: 8 },
    { title: "Reynolds number – laminar vs turbulent", subject: "Fluid Mechanics & Machinery", day: 8 },
    { title: "Hagen-Poiseuille flow in pipes", subject: "Fluid Mechanics & Machinery", day: 8 },
    { title: "Boundary layer – development, thickness (Blasius)", subject: "Fluid Mechanics & Machinery", day: 8 }
];

// Strictly use gemini-3.5-flash with model fallback retry
function callGemini(promptText, modelName = 'gemini-3.5-flash') {
    return new Promise((resolve, reject) => {
        const payload = JSON.stringify({
            contents: [{
                parts: [{ text: promptText }]
            }]
        });

        const url = `https://generativelanguage.googleapis.com/v1beta/models/${modelName}:generateContent?key=${apiKey}`;
        const req = https.request(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Content-Length': Buffer.byteLength(payload)
            }
        }, (res) => {
            let data = '';
            res.on('data', chunk => data += chunk);
            res.on('end', () => {
                try {
                    const json = JSON.parse(data);
                    if (json.candidates && json.candidates[0] && json.candidates[0].content) {
                        resolve(json.candidates[0].content.parts[0].text);
                    } else {
                        reject(new Error(data));
                    }
                } catch (e) {
                    reject(e);
                }
            });
        });

        req.on('error', reject);
        req.write(payload);
        req.end();
    });
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function extractSections(aiText) {
    function getSection(startTag, endTag) {
        const regex = new RegExp(`${startTag}([\\s\\S]*?)${endTag}`);
        const match = aiText.match(regex);
        if (!match) return '';
        return match[1].trim();
    }

    return {
        understandHTML: getSection('SECTION_UNDERSTAND_START', 'SECTION_UNDERSTAND_END') || '<p>Basic definitions and foundational concepts explained from absolute scratch.</p>',
        learnConceptHTML: getSection('SECTION_LEARN_START', 'SECTION_LEARN_END') || '<p>Comprehensive theoretical framework, working principles, and derivations built step-by-step.</p>',
        memorizeFactsHTML: getSection('SECTION_MEMORIZE_START', 'SECTION_MEMORIZE_END') || '<ul><li>Key formulas, SI units, and standard constants.</li></ul>',
        aviationAppHTML: getSection('SECTION_AVIATION_START', 'SECTION_AVIATION_END') || '<p>Aviation applications in Pitot tubes, airspeed indicators, and boundary layers over wings.</p>',
        upscFocusHTML: getSection('SECTION_UPSC_START', 'SECTION_UPSC_END') || '<ul><li>UPSC ASO exam focus, PYQ patterns, and conceptual traps.</li></ul>',
        practiceMCQsHTML: getSection('SECTION_PRACTICE_START', 'SECTION_PRACTICE_END') || '<div>Practice MCQs (30 Questions)</div>',
        miniTestMCQsHTML: getSection('SECTION_MINITEST_START', 'SECTION_MINITEST_END') || '<div>Mini Test MCQs (10 Questions)</div>',
        errorAnalysisHTML: getSection('SECTION_ERROR_START', 'SECTION_ERROR_END') || '<p>Analysis of common student traps, unit conversion errors, and sign mistakes.</p>',
        activeRecallHTML: getSection('SECTION_ACTIVERECALL_START', 'SECTION_ACTIVERECALL_END') || '<p>Active recall questions, mind maps, and quick memory triggers.</p>'
    };
}

function buildHTMLPage(topicTitle, topicSlug, sections) {
    return `<!DOCTYPE html>
<html lang="en">
<head>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7924751316191829" crossorigin="anonymous"></script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Day 8: ${topicTitle} | UPSC Air Safety Officer (ASO) Study Hub</title>
    <meta name="description" content="Beginner-to-advanced 4-tab study module for ${topicTitle} under UPSC ASO Day 8: Step-by-step theory, 30 practice MCQs, 10-question mini test, and active recall.">
    <link rel="canonical" href="https://sjmaths.com/upsc-aso/day-8/${topicSlug}/">
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

    <!-- MathJax 3 for LaTeX rendering -->
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

        /* 4 Main Tabs System */
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
        <!-- Breadcrumb Navigation -->
        <div class="breadcrumb-nav">
            <a href="/">Home</a> <i class="fas fa-chevron-right" style="font-size: 0.7rem;"></i>
            <a href="/upsc-aso/">UPSC ASO Hub</a> <i class="fas fa-chevron-right" style="font-size: 0.7rem;"></i>
            <span>Day 8 • ${topicTitle}</span>
        </div>

        <!-- Header -->
        <div class="module-header">
            <h1>${topicTitle}</h1>
            <div class="module-badges">
                <span class="badge-tag"><i class="fas fa-calendar-day"></i> Day 8 of 129</span>
                <span class="badge-tag"><i class="fas fa-water"></i> Fluid Mechanics & Machinery</span>
                <span class="badge-tag"><i class="fas fa-layer-group"></i> Phase 1: Foundations</span>
                <span class="badge-tag"><i class="far fa-clock"></i> 90-120 min Master Class</span>
            </div>
        </div>

        <!-- 4 Primary Navigation Tabs -->
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

        <!-- ==================== TAB 1: CONCEPTS & THEORIES ==================== -->
        <div id="tab-concepts" class="tab-content-panel active">
            <div class="step-card">
                <h2 class="step-title"><i class="fas fa-lightbulb"></i> 1. Understand (From Absolute Zero, 5–10 min)</h2>
                <div class="content-box">
                    ${sections.understandHTML}
                </div>
            </div>
            <div class="step-card">
                <h2 class="step-title"><i class="fas fa-graduation-cap"></i> 2. Learn the Concept (Complete Theoretical Foundation & Derivations, 20–25 min)</h2>
                <div class="content-box">
                    ${sections.learnConceptHTML}
                </div>
            </div>
            <div class="step-card">
                <h2 class="step-title"><i class="fas fa-brain"></i> 3. Memorize Important Facts (10 min)</h2>
                <div class="content-box">
                    ${sections.memorizeFactsHTML}
                </div>
            </div>
            <div class="step-card">
                <h2 class="step-title"><i class="fas fa-plane-flight"></i> 4. Aviation Application (5–10 min)</h2>
                <div class="content-box">
                    ${sections.aviationAppHTML}
                </div>
            </div>
            <div class="step-card">
                <h2 class="step-title"><i class="fas fa-bullseye"></i> 5. UPSC ASO Focus (10 min)</h2>
                <div class="content-box">
                    ${sections.upscFocusHTML}
                </div>
            </div>
        </div>

        <!-- ==================== TAB 2: PRACTICE QUESTIONS ==================== -->
        <div id="tab-practice" class="tab-content-panel">
            <div class="step-card">
                <h2 class="step-title"><i class="fas fa-pen-nib"></i> 6. Practice Questions (30 Exhaustive UPSC ASO MCQs)</h2>
                ${sections.practiceMCQsHTML}
            </div>
        </div>

        <!-- ==================== TAB 3: MINI TEST ==================== -->
        <div id="tab-minitest" class="tab-content-panel">
            <div class="step-card">
                <h2 class="step-title"><i class="fas fa-stopwatch"></i> 7. Grand Mini Test (10 Exam-Level Questions)</h2>
                ${sections.miniTestMCQsHTML}
            </div>
        </div>

        <!-- ==================== TAB 4: ACTIVE RECALL & ERROR ANALYSIS ==================== -->
        <div id="tab-activerecall" class="tab-content-panel">
            <div class="step-card">
                <h2 class="step-title"><i class="fas fa-bug"></i> 8. Error Analysis & Common Traps (5 min)</h2>
                <div class="content-box">
                    ${sections.errorAnalysisHTML}
                </div>
            </div>
            <div class="step-card">
                <h2 class="step-title"><i class="fas fa-rotate-right"></i> 9. Active Recall & Quick Revision (5 min)</h2>
                <div class="content-box">
                    ${sections.activeRecallHTML}
                </div>
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

async function runGeneration() {
    console.log('Starting Gemini 3.5 Flash Generation for Day 8 Microtopics (Zero-to-Hero Theory, 30 Practice MCQs & 10 Mini Test Questions, 13s delay)...\n');

    for (let i = 0; i < day8Topics.length; i++) {
        const topic = day8Topics[i];
        const slug = slugify(topic.title);
        const filePath = path.join('c:/Users/sande/Documents/GitHub/sjmaths-website/upsc-aso/day-8', slug, 'index.html');

        console.log(`[${i + 1}/${day8Topics.length}] Generating 30 MCQs & full Day 8 module via Gemini 3.5 Flash for: "${topic.title}"...`);

        const prompt = `You are a world-renowned professor of Fluid Dynamics & Aeronautical Engineering and UPSC Air Safety Officer (ASO) exam author.
Generate an exhaustive, beginner-friendly yet highly rigorous study module for the Day 8 microtopic: "${topic.title}".

SPECIAL PEDAGOGICAL INSTRUCTIONS:
1. Explain ALL concepts from absolute basic principles assuming zero prior knowledge, building up step-by-step to advanced UPSC ASO level.
2. In SECTION_PRACTICE_START, generate EXACTLY 30 high-quality, exam-oriented practice MCQs (numerical calculation, conceptual sub-cases, statement-based evaluation, and assertion-reasoning questions).
3. In SECTION_MINITEST_START, generate EXACTLY 10 Grand Mini Test MCQs (Q1 to Q10).

IMPORTANT LATEX MATH INSTRUCTIONS:
- Format ALL math formulas using LaTeX enclosed strictly in $...$ for inline math and $$...$$ for display math (e.g. $\\frac{\\partial u}{\\partial x} + \\frac{\\partial v}{\\partial y} + \\frac{\\partial w}{\\partial z} = 0$).

Format your entire response using the following EXACT DELIMITER TAGS (do not omit any tag):

SECTION_UNDERSTAND_START
<p>Basics from scratch: What is ${topic.title}? Intuitive explanation, physical meaning, SI units, and standard UPSC terminology.</p>
SECTION_UNDERSTAND_END

SECTION_LEARN_START
<p>Complete theoretical foundation built step-by-step from zero background. Cover working principles, physical conservation laws (mass, momentum, energy), step-by-step derivations, velocity fields, and boundary layer equations.</p>
<div class="formula-card">
$$ \\text{Main LaTeX governing equations, Bernoulli integrals, or boundary layer thickness formulas} $$
</div>
<p>Analytical details, sub-cases, and mathematical properties.</p>
SECTION_LEARN_END

SECTION_MEMORIZE_START
<ul>
  <li><strong>Core Formula 1 & Units:</strong> $...$</li>
  <li><strong>Standard Constant / Dimensionless Number:</strong> $...$</li>
  <li><strong>Key Theorem / Assumption:</strong> $...$</li>
</ul>
SECTION_MEMORIZE_END

SECTION_AVIATION_START
<p>Direct application of ${topic.title} in Aviation & Aircraft Systems (e.g., Pitot-static tube airspeed measurement, Venturi tubes in carburetor/vacuum instruments, boundary layer growth over wing airfoils, boundary layer separation, stall phenomena, or skin friction drag).</p>
SECTION_AVIATION_END

SECTION_UPSC_START
<ul>
  <li><strong>Frequently Asked Exam Facts:</strong> Specific numerical values, units, dimensions, and empirical relations tested in UPSC ASO / GATE.</li>
  <li><strong>Conceptual Traps:</strong> Irrotational vs Rotational flow traps, irrotational stream function existence, compressible vs incompressible Bernoulli assumptions.</li>
</ul>
SECTION_UPSC_END

SECTION_PRACTICE_START
Generate EXACTLY 30 practice MCQs (Q1 to Q30) covering all sub-cases, numerical problems, property assertions, and edge-cases of ${topic.title}.
Format EACH MCQ strictly as:
<div class="mcq-card">
  <div class="mcq-question">Q1. Question statement with LaTeX math...</div>
  <div class="mcq-options">
    <div class="mcq-option" data-opt="A" onclick="selectOption(this, ${8000 + (i*50) + 1})">A) Option A text</div>
    <div class="mcq-option" data-opt="B" onclick="selectOption(this, ${8000 + (i*50) + 1})">B) Option B text</div>
    <div class="mcq-option" data-opt="C" onclick="selectOption(this, ${8000 + (i*50) + 1})">C) Option C text</div>
    <div class="mcq-option" data-opt="D" onclick="selectOption(this, ${8000 + (i*50) + 1})">D) Option D text</div>
  </div>
  <button class="check-btn" onclick="checkMCQ(${8000 + (i*50) + 1}, 'B')">Check Answer</button>
  <div class="explanation-box" id="explain-${8000 + (i*50) + 1}">Exhaustive step-by-step solution with full LaTeX math.</div>
</div>
(Repeat for Q2 through Q30 with unique qId indices!)
SECTION_PRACTICE_END

SECTION_MINITEST_START
Generate EXACTLY 10 Grand Mini Test MCQs (Q1 to Q10) covering statement-based, assertion-reasoning, numerical, and conceptual questions.
Format using unique IDs (e.g., 9801 to 9810).
<div class="mcq-card">
  <div class="mcq-question">Q1. Statement 1 and Statement 2 question...</div>
  <div class="mcq-options">
    <div class="mcq-option" data-opt="A" onclick="selectOption(this, 9801)">A) Option A</div>
    <div class="mcq-option" data-opt="B" onclick="selectOption(this, 9801)">B) Option B</div>
    <div class="mcq-option" data-opt="C" onclick="selectOption(this, 9801)">C) Option C</div>
    <div class="mcq-option" data-opt="D" onclick="selectOption(this, 9801)">D) Option D</div>
  </div>
  <button class="check-btn" onclick="checkMCQ(9801, 'A')">Check Answer</button>
  <div class="explanation-box" id="explain-9801">Detailed explanation.</div>
</div>
(Repeat up to Q10 with IDs 9801 through 9810!)
SECTION_MINITEST_END

SECTION_ERROR_START
<p>Exhaustive breakdown of common student errors, calculation traps, irrotational flow existence confusion, or Blasius boundary layer profile misapplications in ${topic.title}.</p>
SECTION_ERROR_END

SECTION_ACTIVERECALL_START
<p>15 active recall prompts without answers, formula memory triggers, and quick revision mind map for ${topic.title}.</p>
SECTION_ACTIVERECALL_END`;

        try {
            const rawResponse = await callGemini(prompt, 'gemini-3.5-flash');
            const sections = extractSections(rawResponse);
            const htmlPage = buildHTMLPage(topic.title, slug, sections);

            const dirPath = path.join('c:/Users/sande/Documents/GitHub/sjmaths-website/upsc-aso/day-8', slug);
            if (!fs.existsSync(dirPath)) {
                fs.mkdirSync(dirPath, { recursive: true });
            }
            fs.writeFileSync(filePath, htmlPage);
            console.log(`  -> Successfully generated & saved via gemini-3.5-flash: ${filePath}`);
        } catch (err) {
            console.error(`  -> Failed generation for ${topic.title}:`, err.message);
        }

        if (i < day8Topics.length - 1) {
            console.log('  Waiting 13 seconds delay before next API call...');
            await sleep(13000);
        }
    }

    console.log('\nAll 7 Day 8 microtopics generated with Gemini 3.5 Flash (Beginner-to-Advanced Theory, 30 Practice MCQs & 10 Mini Test Questions)!');
}

runGeneration();
