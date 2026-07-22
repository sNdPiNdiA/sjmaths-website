const fs = require('fs');
const path = require('path');
const https = require('https');

// Read API Key from .env
const envContent = fs.readFileSync('c:/Users/sande/Documents/GitHub/sjmaths-website/.env', 'utf8');
const keyMatch = envContent.match(/GEMINI_API_KEY\s*=\s*(.*)/);
const apiKey = keyMatch ? keyMatch[1].trim() : '';

if (!apiKey) {
    console.error('ERROR: GEMINI_API_KEY not found in .env file!');
    process.exit(1);
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// Call Gemini API using gemini-3.5-flash-lite / gemini-3.1-flash-lite / gemini-3.6-flash
async function callGemini(promptText) {
    const modelsToTry = ['gemini-3.5-flash-lite', 'gemini-3.1-flash-lite', 'gemini-3.6-flash'];
    let lastError = null;

    for (const modelName of modelsToTry) {
        try {
            const resText = await new Promise((resolve, reject) => {
                const payload = JSON.stringify({
                    contents: [{
                        parts: [{ text: promptText }]
                    }]
                });

                const url = 'https://generativelanguage.googleapis.com/v1beta/models/' + modelName + ':generateContent?key=' + apiKey;
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

            return resText;
        } catch (err) {
            console.warn(`[Warning] Model ${modelName} failed/throttled: ${err.message.substring(0, 100)}... Retrying next model.`);
            lastError = err;
            await sleep(2000);
        }
    }
    throw lastError;
}

// Automatically scan ssc-cgl/statistics for all microtopic directories needing 5-tab generation
function discoverAllStatsTopics() {
    const statsDir = 'c:/Users/sande/Documents/GitHub/sjmaths-website/ssc-cgl/statistics';
    const topics = [];

    function scan(dir) {
        const list = fs.readdirSync(dir);
        list.forEach(file => {
            const fullPath = path.join(dir, file);
            const stat = fs.statSync(fullPath);
            if (stat.isDirectory()) {
                const indexFile = path.join(fullPath, 'index.html');
                if (fs.existsSync(indexFile)) {
                    const content = fs.readFileSync(indexFile, 'utf8');
                    const relativePath = path.relative(statsDir, fullPath).replace(/\\/g, '/');

                    const isAlreadyGenerated = content.includes('1. Concept & Theory') &&
                                               content.includes('3. Notes & FAQs') &&
                                               content.includes('lang-hi') &&
                                               content.length > 25000;

                    if (!isAlreadyGenerated && relativePath !== '' && relativePath !== 'topics') {
                        const formattedTitle = path.basename(relativePath)
                            .replace(/-/g, ' ')
                            .replace(/\b\w/g, l => l.toUpperCase());

                        topics.push({
                            topicName: formattedTitle,
                            categoryDir: relativePath
                        });
                    }
                }
                scan(fullPath);
            }
        });
    }

    scan(statsDir);
    return topics;
}

const topicsToGenerate = discoverAllStatsTopics();
console.log(`📋 Total pending Statistics microtopic pages discovered: ${topicsToGenerate.length}`);

function buildPrompt(topicName) {
    return `You are the Senior Statistics & Mathematics Faculty and Content Team of SJMaths.
Your task is to generate complete, high-quality, BILINGUAL (English & Hindi) educational content for SSC CGL Statistics (Paper-III & General Aptitude Statistics) on the topic: "${topicName}".

MANDATORY RULES:
1. EVERY SINGLE SECTION, HEADING, PARAGRAPH, LIST ITEM, TABLE CELL, MCQ QUESTION, OPTION, SOLUTION STEP, AND TRICK MUST HAVE BOTH ENGLISH AND HINDI VERSIONS wrapped inside:
   <div class="lang-en">English Content here</div>
   <div class="lang-hi">हिंदी सामग्री यहाँ</div>
   (For small inline texts, use <span class="lang-en">...</span> <span class="lang-hi">...</span>).

2. DO NOT include "Author:", "Target Audience:", or "Estimated Reading Time:" anywhere.

3. Example of required bilingual structure:
<h2><span class="lang-en">Quick Overview</span><span class="lang-hi">त्वरित अवलोकन</span></h2>
<p class="lang-en">Explanation in English here.</p>
<p class="lang-hi">हिंदी में व्याख्या यहाँ।</p>

4. Use LaTeX math formatting ($x^2 + y^2 = 10$).

Generate content formatted EXACTLY into the following 5 distinct tags:

[TAB1_START]
Content for Tab 1: Concept & Detailed Theory (Bilingual)
(Includes: Quick Overview, Learning Objectives, Concept Introduction, Real-Life Applications, Important Terms & Definitions table, Formula Sheet table, Mathematical Derivations/Properties)
[TAB1_END]

[TAB2_START]
Content for Tab 2: Shortcuts & Topper Tricks (Bilingual)
(Includes: Shortcuts & Fast Calculation Methods, Exam Tricks, Shortcut Comparison Table, Memory Tricks & Mnemonics - All with .lang-en and .lang-hi wrappers)
[TAB2_END]

[TAB3_START]
Content for Tab 3: Revision Notes & 15 SEO FAQs (Bilingual)
(Includes: 1-Page Revision Notes, One Minute Revision bullets, Conceptual Questions, 15 SEO-friendly FAQs in both .lang-en and .lang-hi, Internal Links, External References, Conclusion)
[TAB3_END]

[TAB4_START]
Content for Tab 4: Solved Practice MCQs (Bilingual)
(Generate 10 MCQ style practice questions:
<div class="mcq-card">
  <div class="mcq-question">
    <div class="lang-en"><strong>Q1.</strong> Question text in English</div>
    <div class="lang-hi"><strong>Q1.</strong> प्रश्न पाठ हिंदी में</div>
  </div>
  <div class="mcq-options">
    <div class="mcq-option"><span class="lang-en">(A) Option 1</span><span class="lang-hi">(A) विकल्प 1</span></div>
    <div class="mcq-option"><span class="lang-en">(B) Option 2</span><span class="lang-hi">(B) विकल्प 2</span></div>
    <div class="mcq-option"><span class="lang-en">(C) Option 3</span><span class="lang-hi">(C) विकल्प 3</span></div>
    <div class="mcq-option"><span class="lang-en">(D) Option 4</span><span class="lang-hi">(D) विकल्प 4</span></div>
  </div>
  <details class="mcq-solution-details">
    <summary>
      <span class="lang-en"><i class="fas fa-key"></i> View Solution</span>
      <span class="lang-hi"><i class="fas fa-key"></i> हल देखें</span>
    </summary>
    <div class="mcq-solution-body">
      <p class="correct-answer"><strong><span class="lang-en">Correct Option: (A)</span><span class="lang-hi">सही विकल्प: (A)</span></strong></p>
      <div class="lang-en"><strong>Step-by-Step Solution:</strong> Solution text.</div>
      <div class="lang-hi"><strong>चरण-दर-चरण हल:</strong> हल पाठ।</div>
      <div class="topper-trick">
        <div class="lang-en"><strong><i class="fas fa-bolt"></i> Topper's Shortcut:</strong> Trick description.</div>
        <div class="lang-hi"><strong><i class="fas fa-bolt"></i> टॉपर शॉर्टकट:</strong> ट्रिक् का विवरण।</div>
      </div>
    </div>
  </details>
</div>
)
[TAB4_END]

[TAB5_START]
Content for Tab 5: Previous Year Questions (PYQs) (Bilingual)
(Generate 10 SSC CGL PYQs in Bilingual MCQ format using .lang-en and .lang-hi wrappers for questions, options, detailed solutions and topper tricks, followed by PYQ Trend Analysis table)
[TAB5_END]

WRITING & FORMATTING RULES:
1. MUST wrap every paragraph, bullet point, heading, and table cell in .lang-en and .lang-hi.
2. DO NOT include Author or Target Audience headers.
3. Do NOT wrap output in markdown \`\`\` code fences.`;
}

function parseTabs(aiText) {
    function getSection(startTag, endTag) {
        const regex = new RegExp(`${startTag}([\\s\\S]*?)${endTag}`);
        const match = aiText.match(regex);
        return match ? match[1].trim() : '';
    }

    return {
        tab1: getSection('\\[TAB1_START\\]', '\\[TAB1_END\\]') || '<p>Comprehensive theory content loading...</p>',
        tab2: getSection('\\[TAB2_START\\]', '\\[TAB2_END\\]') || '<p>Shortcuts & Topper Tricks content loading...</p>',
        tab3: getSection('\\[TAB3_START\\]', '\\[TAB3_END\\]') || '<p>Revision Notes & FAQs loading...</p>',
        tab4: getSection('\\[TAB4_START\\]', '\\[TAB4_END\\]') || '<p>Practice MCQs content loading...</p>',
        tab5: getSection('\\[TAB5_START\\]', '\\[TAB5_END\\]') || '<p>Previous Year Questions loading...</p>'
    };
}

function generateSingleHTMLPage(topicName, relativeUrlPath, tabs) {
    return `<!DOCTYPE html>
<html lang="en">
<head>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7924751316191829" crossorigin="anonymous"></script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${topicName} - SSC CGL Statistics | SJMaths</title>
    <meta name="description" content="Master ${topicName} for SSC CGL Tier 1 & Tier 2 / Paper-III. Complete concept notes, formulas, shortcuts, PYQs, practice questions, and FAQs.">
    <meta name="robots" content="index, follow, max-image-preview:large">
    <link rel="canonical" href="https://sjmaths.com/ssc-cgl/statistics/${relativeUrlPath}/">
    <meta name="keywords" content="${topicName}, SSC CGL Statistics, Statistics Paper 3, SSC CGL Tier 1, SSC CGL Tier 2, SJMaths">
    <meta name="author" content="SJMaths">
    <link rel="icon" type="image/png" href="/favicon.png">

    <!-- Fonts and Icons -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/assets/vendor/fontawesome/css/all.min.css?v=7441465c">

    <!-- Stylesheets -->
    <link rel="stylesheet" href="/assets/css/main.min.css?v=4ba21ce7">
    <link rel="stylesheet" href="/assets/css/layout.min.css?v=e4922b08">
    <link rel="stylesheet" href="/assets/css/component.min.css?v=8c99f11f">
    <link rel="stylesheet" href="/assets/css/improved-ui.min.css?v=574ed909">
    <link rel="stylesheet" href="/assets/css/pages.min.css?v=9e3bd560">

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
            --shadow-lg: 0 10px 30px -5px rgba(142, 68, 173, 0.12);
            --accent-gradient: linear-gradient(135deg, #059669, #3b82f6);
        }

        .topic-container {
            max-width: 1050px;
            margin: 1rem auto;
            padding: 0.75rem 1rem 3rem;
            animation: fadeIn 0.4s ease-out;
        }

        .breadcrumbs {
            margin-bottom: 1rem;
            font-size: 0.85rem;
            color: var(--text-light);
            display: flex;
            align-items: center;
            flex-wrap: wrap;
            gap: 0.3rem;
        }

        .breadcrumbs a {
            color: var(--primary);
            text-decoration: none;
            font-weight: 500;
        }

        .topic-header {
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            border-radius: 1rem;
            padding: 1.25rem 1rem;
            box-shadow: var(--shadow-lg);
            margin-bottom: 1.25rem;
            text-align: center;
        }

        .topic-header h1 {
            font-family: 'Outfit', sans-serif;
            font-size: clamp(1.5rem, 5vw, 2.2rem);
            font-weight: 800;
            background: var(--accent-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.4rem;
            line-height: 1.2;
        }

        /* Mobile-First 5 Main Tabs Navigation */
        .main-tabs-nav {
            display: flex;
            gap: 0.4rem;
            margin-bottom: 1.25rem;
            border-bottom: 2px solid #e2e8f0;
            padding-bottom: 0.4rem;
            overflow-x: auto;
            -webkit-overflow-scrolling: touch;
            scrollbar-width: none;
        }

        .main-tabs-nav::-webkit-scrollbar {
            display: none;
        }

        .tab-btn {
            background: transparent;
            border: none;
            outline: none;
            padding: 0.55rem 1rem;
            font-family: 'Outfit', sans-serif;
            font-size: 0.9rem;
            font-weight: 700;
            color: var(--text-light);
            cursor: pointer;
            border-radius: 8px 8px 0 0;
            transition: all 0.2s ease;
            white-space: nowrap;
            display: flex;
            align-items: center;
            gap: 0.4rem;
        }

        .tab-btn i {
            font-size: 0.85rem;
        }

        .tab-btn.active {
            background: var(--accent-gradient);
            color: #ffffff;
            box-shadow: 0 4px 12px rgba(5, 150, 105, 0.25);
        }

        .tab-panel {
            display: none;
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            border-radius: 1rem;
            padding: 1.25rem;
            box-shadow: var(--shadow-lg);
            animation: fadeIn 0.35s ease-out;
            line-height: 1.65;
            color: var(--text-dark);
        }

        .tab-panel.active {
            display: block;
        }

        /* Bilingual Language Toggle Integration */
        .lang-hi {
            display: none;
        }

        body.lang-mode-hi .lang-en {
            display: none !important;
        }

        body.lang-mode-hi .lang-hi {
            display: block !important;
        }

        body.lang-mode-hi span.lang-hi,
        body.lang-mode-hi strong.lang-hi,
        body.lang-mode-hi i.lang-hi {
            display: inline-block !important;
        }

        .tab-panel h2 {
            font-family: 'Outfit', sans-serif;
            font-size: 1.35rem;
            font-weight: 700;
            color: var(--primary);
            margin-top: 1.25rem;
            margin-bottom: 0.85rem;
            border-bottom: 2px solid rgba(5, 150, 105, 0.15);
            padding-bottom: 0.35rem;
        }

        .mcq-card {
            background: #ffffff;
            border: 1px solid rgba(5, 150, 105, 0.12);
            border-radius: 0.75rem;
            padding: 1rem;
            margin-bottom: 1.25rem;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }

        .mcq-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(5, 150, 105, 0.1);
        }

        .mcq-question {
            font-size: 0.98rem;
            font-weight: 600;
            color: #2c3e50;
            margin-bottom: 0.75rem;
        }

        .mcq-options {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 0.5rem;
            margin-bottom: 0.85rem;
        }

        .mcq-option {
            background: rgba(0, 0, 0, 0.02);
            border: 1px solid rgba(0, 0, 0, 0.06);
            border-radius: 6px;
            padding: 0.5rem 0.75rem;
            font-size: 0.9rem;
            color: #34495e;
            cursor: pointer;
            transition: all 0.25s ease;
        }

        details.mcq-solution-details {
            margin-top: 0.6rem;
            border-top: 1px dashed rgba(0,0,0,0.08);
            padding-top: 0.5rem;
        }

        details.mcq-solution-details summary {
            font-weight: 700;
            color: var(--primary);
            cursor: pointer;
            font-size: 0.88rem;
            user-select: none;
            outline: none;
        }

        .mcq-solution-body {
            margin-top: 0.6rem;
            background: rgba(5, 150, 105, 0.03);
            border-radius: 6px;
            padding: 0.85rem;
            font-size: 0.9rem;
        }

        .correct-answer {
            color: #27ae60;
            font-weight: 700;
            margin-bottom: 0.4rem;
        }

        .topper-trick {
            background: linear-gradient(135deg, rgba(241, 196, 15, 0.15), rgba(230, 126, 34, 0.15));
            border-left: 3px solid #f39c12;
            padding: 0.5rem 0.75rem;
            border-radius: 4px;
            margin-top: 0.5rem;
            font-size: 0.88rem;
            color: #d35400;
        }

        .tab-panel table {
            width: 100%;
            border-collapse: collapse;
            margin: 1rem 0;
            display: block;
            overflow-x: auto;
            -webkit-overflow-scrolling: touch;
        }

        .tab-panel th, .tab-panel td {
            border: 1px solid #e2e8f0;
            padding: 0.6rem;
            text-align: left;
            font-size: 0.88rem;
        }

        .tab-panel th {
            background: rgba(5, 150, 105, 0.08);
            color: var(--primary);
            font-weight: 700;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(6px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>
<body>
    <div id="header-container"></div>

    <main class="topic-container" id="main-content">
        <!-- Breadcrumbs -->
        <div class="breadcrumbs">
            <a href="/">Home</a> <i class="fas fa-chevron-right" style="font-size: 0.65rem; margin: 0 0.2rem;"></i>
            <a href="/ssc-cgl/syllabus/">SSC CGL Syllabus</a> <i class="fas fa-chevron-right" style="font-size: 0.65rem; margin: 0 0.2rem;"></i>
            <a href="/ssc-cgl/statistics/">Statistics</a> <i class="fas fa-chevron-right" style="font-size: 0.65rem; margin: 0 0.2rem;"></i>
            <span>${topicName}</span>
        </div>

        <!-- Topic Header -->
        <div class="topic-header">
            <h1>${topicName}</h1>
            <p>Complete 5-Tab SSC CGL Statistics Guide: Theory, Shortcuts, Notes & FAQs, Practice MCQs, & PYQs.</p>
        </div>

        <!-- 5-Tab Navigation Bar -->
        <div class="main-tabs-nav">
            <button class="tab-btn active" onclick="openTab(event, 'tab-theory')">
                <i class="fas fa-book-open"></i> 1. Concept & Theory
            </button>
            <button class="tab-btn" onclick="openTab(event, 'tab-tricks')">
                <i class="fas fa-bolt"></i> 2. Topper Tricks
            </button>
            <button class="tab-btn" onclick="openTab(event, 'tab-notes')">
                <i class="fas fa-file-alt"></i> 3. Notes & FAQs
            </button>
            <button class="tab-btn" onclick="openTab(event, 'tab-practice')">
                <i class="fas fa-tasks"></i> 4. Practice MCQs
            </button>
            <button class="tab-btn" onclick="openTab(event, 'tab-pyqs')">
                <i class="fas fa-history"></i> 5. PYQs (MCQs)
            </button>
        </div>

        <!-- Tab 1 Panel -->
        <div id="tab-theory" class="tab-panel active">
            ${tabs.tab1}
        </div>

        <!-- Tab 2 Panel -->
        <div id="tab-tricks" class="tab-panel">
            ${tabs.tab2}
        </div>

        <!-- Tab 3 Panel: Notes & FAQs -->
        <div id="tab-notes" class="tab-panel">
            ${tabs.tab3}
        </div>

        <!-- Tab 4 Panel: Practice MCQs -->
        <div id="tab-practice" class="tab-panel">
            ${tabs.tab4}
        </div>

        <!-- Tab 5 Panel: PYQs -->
        <div id="tab-pyqs" class="tab-panel">
            ${tabs.tab5}
        </div>
    </main>

    <div id="footer-container"></div>

    <script>
        function openTab(evt, tabName) {
            var i, tabcontent, tablinks;
            tabcontent = document.getElementsByClassName("tab-panel");
            for (i = 0; i < tabcontent.length; i++) {
                tabcontent[i].style.display = "none";
                tabcontent[i].classList.remove("active");
            }
            tablinks = document.getElementsByClassName("tab-btn");
            for (i = 0; i < tablinks.length; i++) {
                tablinks[i].classList.remove("active");
            }
            document.getElementById(tabName).style.display = "block";
            document.getElementById(tabName).classList.add("active");
            evt.currentTarget.classList.add("active");
        }
    </script>

    <script src="/assets/js/main.min.js?v=10f0770d" defer data-cfasync="false"></script>
    <script src="/assets/js/global-header.min.js?v=d6ad26b3" defer data-cfasync="false"></script>
    <script src="/assets/js/global-footer.min.js?v=c641c625" defer data-cfasync="false"></script>
    <script type="module">
        const load = async () => {
            try {
                await import("/assets/js/firebase-analytics-only.min.js?v=b9396571");
            } catch(e) { console.debug("Analytics deferred"); }
        };
        if ('requestIdleCallback' in window) requestIdleCallback(load); else setTimeout(load, 3000);
    </script>
</body>
</html>`;
}

async function main() {
    const statsDir = 'c:/Users/sande/Documents/GitHub/sjmaths-website/ssc-cgl/statistics';

    for (let i = 0; i < topicsToGenerate.length; i++) {
        const item = topicsToGenerate[i];
        console.log(`\n⏳ [${i + 1}/${topicsToGenerate.length}] Generating content for Statistics: ${item.topicName}...`);

        try {
            const prompt = buildPrompt(item.topicName);
            const aiText = await callGemini(prompt);
            const tabs = parseTabs(aiText);

            const htmlContent = generateSingleHTMLPage(item.topicName, item.categoryDir, tabs);
            const targetFilePath = path.join(statsDir, item.categoryDir, 'index.html');

            fs.mkdirSync(path.dirname(targetFilePath), { recursive: true });
            fs.writeFileSync(targetFilePath, htmlContent, 'utf8');

            console.log(`✅ Saved: ${targetFilePath}`);
        } catch (err) {
            console.error(`❌ Failed to generate ${item.topicName}: ${err.message}`);
        }

        // Brief delay between API requests
        await sleep(1500);
    }

    console.log('\n🎉 All Statistics Pages Generated Successfully!');
}

main();
