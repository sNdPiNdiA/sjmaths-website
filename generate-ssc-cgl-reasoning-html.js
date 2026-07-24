const fs = require('fs');
const path = require('path');
const https = require('https');

// Load environment variables
const envPath = path.join(__dirname, '.env');
let apiKey = '';
if (fs.existsSync(envPath)) {
    const envContent = fs.readFileSync(envPath, 'utf8');
    const match = envContent.match(/GEMINI_API_KEY\s*=\s*(.*)/);
    if (match) apiKey = match[1].trim();
}

if (!apiKey) {
    console.error('❌ GEMINI_API_KEY not found in .env file!');
    process.exit(1);
}

const models = [
    'gemini-3.5-flash-lite',
    'gemini-3.1-flash-lite',
    'gemini-3.6-flash'
];

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function callGemini(promptText) {
    let lastError = null;
    for (const modelName of models) {
        try {
            const url = `https://generativelanguage.googleapis.com/v1beta/models/${modelName}:generateContent?key=${apiKey}`;
            const payload = JSON.stringify({
                contents: [{ parts: [{ text: promptText }] }]
            });

            const resData = await new Promise((resolve, reject) => {
                const req = https.request(url, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' }
                }, (res) => {
                    let body = '';
                    res.on('data', chunk => body += chunk);
                    res.on('end', () => {
                        if (res.statusCode >= 200 && res.statusCode < 300) {
                            resolve(body);
                        } else {
                            reject(new Error(`HTTP ${res.statusCode}: ${body}`));
                        }
                    });
                });
                req.on('error', reject);
                req.write(payload);
                req.end();
            });

            const parsed = JSON.parse(resData);
            const text = parsed.candidates?.[0]?.content?.parts?.[0]?.text;
            if (text) return text;
        } catch (err) {
            console.warn(`[Warning] Model ${modelName} failed/throttled: ${err.message.substring(0, 100)}... Retrying next model.`);
            lastError = err;
            await sleep(2000);
        }
    }
    throw lastError;
}

// Extract 30 Reasoning topics from reasoning_topics.json
const reasoningTopicsList = JSON.parse(fs.readFileSync('reasoning_topics.json', 'utf8'));

function discoverReasoningTopics() {
    const baseDir = path.join(__dirname, 'ssc-cgl/reasoning');
    const topics = [];

    reasoningTopicsList.forEach(relPath => {
        const fullDir = path.join(baseDir, relPath);
        const indexFile = path.join(fullDir, 'index.html');
        const isVisualTopic = /figural|non-verbal|embedded|paper-folding|pattern-folding|venn|syllogism|visual|space-visualisation|blood-relations/i.test(relPath);
        let isAlreadyGenerated = false;

        if (fs.existsSync(indexFile)) {
            const content = fs.readFileSync(indexFile, 'utf8');
            const hasSVG = content.includes('<svg') || content.includes('<circle') || content.includes('<rect') || content.includes('<polygon') || content.includes('<path');
            
            if (isVisualTopic) {
                isAlreadyGenerated = content.includes('1. Concept & Theory') &&
                                      content.includes('5. Notes & FAQs') &&
                                      content.includes('lang-hi') &&
                                      hasSVG &&
                                      content.length > 25000;
            } else {
                isAlreadyGenerated = content.includes('1. Concept & Theory') &&
                                      content.includes('5. Notes & FAQs') &&
                                      content.includes('lang-hi') &&
                                      content.length > 25000;
            }
        }

        if (!isAlreadyGenerated) {
            const formattedTitle = path.basename(relPath)
                .replace(/-/g, ' ')
                .replace(/\b\w/g, l => l.toUpperCase());

            topics.push({
                topicName: formattedTitle,
                categoryDir: relPath,
                indexPath: indexFile
            });
        }
    });

    return topics;
}

function buildPrompt(topicName) {
    const requiresSVG = /figural|non-verbal|embedded|paper-folding|pattern-folding|venn|syllogism|visual|space-visualisation|blood-relations/i.test(topicName);

    return `You are the Senior Faculty & Content Experts of SJMaths for SSC CGL General Intelligence & Reasoning.
Your task is to generate complete, high-quality, BILINGUAL (English & Hindi) educational content for SSC CGL Reasoning on the topic: "${topicName}".

MANDATORY RULES:
1. EVERY SINGLE SECTION, HEADING, PARAGRAPH, LIST ITEM, TABLE CELL, MCQ QUESTION, OPTION, SOLUTION STEP, AND TRICK MUST HAVE BOTH ENGLISH AND HINDI VERSIONS wrapped inside:
   <div class="lang-en">English Content here</div>
   <div class="lang-hi">हिंदी सामग्री यहाँ</div>
   (For small inline texts, use <span class="lang-en">...</span> <span class="lang-hi">...</span>).

2. DO NOT include "Author:", "Target Audience:", or "Estimated Reading Time:" anywhere.

${requiresSVG ? `3. STRICT SVG DIAGRAM MANDATE: Because "${topicName}" is a visual/non-verbal reasoning topic, EVERY SINGLE ONE OF THE 10 PRACTICE QUESTIONS (Q1 to Q10) AND EVERY SINGLE ONE OF THE 10 PYQS (Q1 to Q10) MUST CONTAIN INLINE <svg> DIAGRAMS!
   - In EVERY Question block: Include an inline <svg> figure diagram for the problem statement (e.g. Figure A : Figure B :: Figure C : ? or sequence of figures).
   - In EVERY Option block (A, B, C, D): Include an inline <svg> figure diagram representing the choice (e.g. <span class="lang-en">(A) <svg width="50" height="50" ...>...</svg></span><span class="lang-hi">(A) <svg width="50" height="50" ...>...</svg></span>).
   - Do NOT omit SVGs for any question or option! All 10 Practice MCQs and all 10 PYQs must have SVG figures.
   - Keep SVGs simple, responsive, and styled with clean strokes (e.g., width="180" height="60" viewBox="0 0 180 60" fill="none" stroke="#2c3e50" stroke-width="2").
` : `3. Use clear formatting, LaTeX for math ($x$), and tables.`}

4. Example of required bilingual structure:
<h2><span class="lang-en">Quick Overview</span><span class="lang-hi">त्वरित अवलोकन</span></h2>
<p class="lang-en">Explanation in English here.</p>
<p class="lang-hi">हिंदी में व्याख्या यहाँ।</p>

Return your entire output organized with clean HTML tags for each of the 5 tab sections as demarcated below:

TAG STRUCTURE REQUIREMENT:
Use exact tags:

[TAB1_START]
Content for Tab 1: Comprehensive Theory & Basics (Bilingual ${requiresSVG ? '& SVG Diagrams' : ''})
(Includes: Quick Overview, Learning Objectives, Core Reasoning Rules & Types ${requiresSVG ? 'with inline SVG figures for theory' : ''}, Real-Life Applications, Key Terminology Table, Step-by-Step Logic & Rules, Common Mistakes & Pitfalls - All with .lang-en and .lang-hi wrappers)
[TAB1_END]

[TAB2_START]
Content for Tab 2: Shortcuts & Topper Tricks (Bilingual)
(Includes: Elimination Tricks, Speed Solving Logic, Pattern Identification Mnemonics, Shortcut Method Comparison Table, Examination Hacks - All with .lang-en and .lang-hi wrappers)
[TAB2_END]

[TAB3_START]
Content for Tab 3: Solved Practice MCQs (Bilingual ${requiresSVG ? '& SVG Diagrams for ALL 10 Questions and ALL Options' : ''})
(Generate EXACTLY 10 MCQ style practice questions. EVERY question Q1 to Q10 MUST have SVG diagrams for question figures and SVG diagrams for options A, B, C, D:
<div class="mcq-card">
  <div class="mcq-question">
    <div class="lang-en"><strong>Q1.</strong> Question in English<br><svg width="200" height="60" viewBox="0 0 200 60" fill="none" stroke="#2c3e50" stroke-width="2">...</svg></div>
    <div class="lang-hi"><strong>Q1.</strong> प्रश्न हिंदी में<br><svg width="200" height="60" viewBox="0 0 200 60" fill="none" stroke="#2c3e50" stroke-width="2">...</svg></div>
  </div>
  <div class="mcq-options">
    <div class="mcq-option"><span class="lang-en">(A) <svg width="50" height="50" ...>...</svg></span><span class="lang-hi">(A) <svg width="50" height="50" ...>...</svg></span></div>
    <div class="mcq-option"><span class="lang-en">(B) <svg width="50" height="50" ...>...</svg></span><span class="lang-hi">(B) <svg width="50" height="50" ...>...</svg></span></div>
    <div class="mcq-option"><span class="lang-en">(C) <svg width="50" height="50" ...>...</svg></span><span class="lang-hi">(C) <svg width="50" height="50" ...>...</svg></span></div>
    <div class="mcq-option"><span class="lang-en">(D) <svg width="50" height="50" ...>...</svg></span><span class="lang-hi">(D) <svg width="50" height="50" ...>...</svg></span></div>
  </div>
  <details class="mcq-solution-details">
    <summary>
      <span class="lang-en"><i class="fas fa-key"></i> View Solution</span>
      <span class="lang-hi"><i class="fas fa-key"></i> हल देखें</span>
    </summary>
    <div class="mcq-solution-body">
      <p class="correct-answer"><strong><span class="lang-en">Correct Option: (B)</span><span class="lang-hi">सही विकल्प: (B)</span></strong></p>
      <div class="lang-en"><strong>Step-by-Step Solution:</strong> Solution in English...</div>
      <div class="lang-hi"><strong>चरण-दर-चरण हल:</strong> हल हिंदी में...</div>
      <div class="topper-trick">
        <div class="lang-en"><strong><i class="fas fa-bolt"></i> Topper's Shortcut:</strong> Shortcut in English...</div>
        <div class="lang-hi"><strong><i class="fas fa-bolt"></i> टॉपर शॉर्टकट:</strong> शॉर्टकट हिंदी में...</div>
      </div>
    </div>
  </details>
</div>)
[TAB3_END]

[TAB4_START]
Content for Tab 4: Previous Year Questions (PYQs) (Bilingual ${requiresSVG ? '& SVG Diagrams for ALL 10 PYQs' : ''})
(Generate EXACTLY 10 SSC CGL Reasoning PYQs. EVERY question Q1 to Q10 MUST have SVG diagrams for question figures and SVG diagrams for options A, B, C, D, followed by PYQ Trend Analysis table)
[TAB4_END]

[TAB5_START]
Content for Tab 5: Revision Notes & FAQs (Bilingual)
(Includes: 1-Page Revision Notes, One Minute Revision bullets, Conceptual Interview/Exam Questions, Frequently Asked Questions in both .lang-en and .lang-hi - Do NOT use the term "SEO-Friendly", Conclusion)
[TAB5_END]

WRITING & FORMATTING RULES:
1. MUST wrap every paragraph, bullet point, heading, and table cell in .lang-en and .lang-hi.
2. DO NOT include Author or Target Audience headers.
3. DO NOT include mixed bilingual text with slashes like "(A) Option / विकल्प" inside any element. Keep .lang-en strictly English only and .lang-hi strictly Hindi only.
4. Do NOT wrap output in markdown \`\`\` code fences.`;
}

function parseTabs(aiText) {
    const t1 = aiText.match(/\[TAB1_START\]([\s\S]*?)\[TAB1_END\]/);
    const t2 = aiText.match(/\[TAB2_START\]([\s\S]*?)\[TAB2_END\]/);
    const t3 = aiText.match(/\[TAB3_START\]([\s\S]*?)\[TAB3_END\]/);
    const t4 = aiText.match(/\[TAB4_START\]([\s\S]*?)\[TAB4_END\]/);
    const t5 = aiText.match(/\[TAB5_START\]([\s\S]*?)\[TAB5_END\]/);

    return {
        tab1: t1 ? t1[1].trim() : '<p>Theory content generating...</p>',
        tab2: t2 ? t2[1].trim() : '<p>Shortcuts content generating...</p>',
        tab3: t3 ? t3[1].trim() : '<p>Practice MCQs content generating...</p>',
        tab4: t4 ? t4[1].trim() : '<p>PYQs content generating...</p>',
        tab5: t5 ? t5[1].trim() : '<p>Notes & FAQs content generating...</p>'
    };
}

function buildHTMLPage(topicName, tabs) {
    return `<!DOCTYPE html>
<html lang="en">
<head>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7924751316191829" crossorigin="anonymous"></script>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
    <title>${topicName} - SSC CGL Reasoning 5-Tab Masterclass | SJMaths</title>
    <meta name="description" content="Master ${topicName} for SSC CGL General Intelligence & Reasoning. Complete bilingual theory, topper tricks, practice MCQs, PYQs, and revision notes."/>
    <meta name="keywords" content="${topicName}, SSC CGL Reasoning, SSC General Intelligence, Reasoning MCQs, Topper Tricks, SJMaths"/>
    <meta name="robots" content="index, follow, max-image-preview:large"/>
    <link rel="icon" type="image/png" href="/favicon.png"/>
    <link rel="preconnect" href="https://fonts.googleapis.com"/>
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin=""/>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@500;600;700;800&display=swap" rel="stylesheet"/>
    <link rel="preload" as="style" href="/assets/vendor/fontawesome/css/all.min.css?v=7441465c" onload="this.onload=null;this.rel='stylesheet'" crossorigin="anonymous"/>
    <noscript><link rel="stylesheet" href="/assets/vendor/fontawesome/css/all.min.css?v=7441465c"/></noscript>
    <link href="/assets/css/main.min.css?v=4ba21ce7" rel="stylesheet"/>
    <link href="/assets/css/layout.min.css?v=e4922b08" rel="stylesheet"/>
    <link href="/assets/css/component.min.css?v=8c99f11f" rel="stylesheet"/>
    <link href="/assets/css/improved-ui.min.css?v=574ed909" rel="stylesheet"/>
    <link href="/assets/css/pages.min.css?v=9e3bd560" rel="stylesheet"/>
    <!-- MathJax for LaTeX support -->
    <script>
      window.MathJax = {
        tex: { inlineMath: [['$', '$'], ['\\\\(', '\\\\)']], displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']] },
        options: { ignoreHtmlClass: 'tex2jax_ignore', processHtmlClass: 'tex2jax_process' }
      };
    </script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

    <style>
        :root {
            --primary: #8e44ad;
            --primary-dark: #6c3483;
            --accent-gradient: linear-gradient(135deg, #8e44ad, #e74c3c);
            --bg-card: rgba(255, 255, 255, 0.96);
            --border-card: rgba(142, 68, 173, 0.15);
            --text-dark: #2c3e50;
            --text-muted: #7f8c8d;
        }

        /* Bilingual Toggle Mechanics */
        .lang-hi { display: none; }
        body.lang-mode-hi .lang-en { display: none !important; }
        body.lang-mode-hi .lang-hi { display: block !important; }
        body.lang-mode-hi span.lang-hi, body.lang-mode-hi strong.lang-hi, body.lang-mode-hi i.lang-hi { display: inline !important; }

        .quant-container {
            max-width: 1000px;
            margin: 1rem auto 3rem;
            padding: 0 1rem;
        }

        .subject-nav {
            display: flex;
            gap: 0.5rem;
            margin-bottom: 1.5rem;
            overflow-x: auto;
            padding-bottom: 0.5rem;
            border-bottom: 1px solid rgba(0,0,0,0.05);
        }

        .sub-nav-item {
            padding: 0.5rem 1.25rem;
            text-decoration: none;
            color: var(--text-muted);
            font-size: 0.95rem;
            font-weight: 600;
            border-radius: 20px;
            background: rgba(0,0,0,0.03);
            transition: all 0.2s ease;
            white-space: nowrap;
        }

        .sub-nav-item.active {
            background: var(--accent-gradient);
            color: #ffffff;
            box-shadow: 0 4px 12px rgba(142, 68, 173, 0.25);
        }

        /* Mobile First Tabs Navigation */
        .tab-nav {
            display: flex;
            gap: 0.4rem;
            overflow-x: auto;
            padding-bottom: 0.75rem;
            margin-bottom: 1.5rem;
            scrollbar-width: thin;
        }

        .tab-btn {
            flex: 0 0 auto;
            padding: 0.65rem 1.1rem;
            font-family: 'Outfit', sans-serif;
            font-size: 0.9rem;
            font-weight: 700;
            color: var(--text-dark);
            background: #ffffff;
            border: 1.5px solid var(--border-card);
            border-radius: 12px;
            cursor: pointer;
            transition: all 0.25s ease;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            box-shadow: 0 2px 6px rgba(0,0,0,0.03);
        }

        .tab-btn i {
            color: var(--primary);
            font-size: 1rem;
        }

        .tab-btn.active {
            background: var(--accent-gradient);
            color: #ffffff;
            border-color: transparent;
            box-shadow: 0 4px 15px rgba(142, 68, 173, 0.3);
        }

        .tab-btn.active i {
            color: #ffffff;
        }

        .tab-panel {
            display: none;
            background: var(--bg-card);
            border: 1px solid var(--border-card);
            border-radius: 16px;
            padding: 1.75rem;
            box-shadow: 0 10px 30px rgba(0,0,0,0.04);
            animation: fadeIn 0.35s ease;
        }

        .tab-panel.active {
            display: block;
        }

        /* Typography inside tabs */
        .tab-panel h1 { font-family: 'Outfit', sans-serif; font-size: 1.75rem; font-weight: 800; color: var(--primary-dark); margin-bottom: 1rem; }
        .tab-panel h2 { font-family: 'Outfit', sans-serif; font-size: 1.4rem; font-weight: 700; color: #34495e; margin: 1.5rem 0 0.75rem; border-bottom: 2px solid rgba(142, 68, 173, 0.1); padding-bottom: 0.4rem; }
        .tab-panel h3 { font-size: 1.15rem; font-weight: 700; color: var(--primary); margin: 1.2rem 0 0.5rem; }
        .tab-panel p { line-height: 1.75; color: #34495e; font-size: 1rem; margin-bottom: 1rem; }
        .tab-panel ul, .tab-panel ol { margin: 0.5rem 0 1.2rem 1.5rem; color: #34495e; }
        .tab-panel li { margin-bottom: 0.4rem; line-height: 1.6; }

        /* Tables */
        .tab-panel table {
            width: 100%;
            border-collapse: collapse;
            margin: 1.25rem 0;
            font-size: 0.95rem;
        }
        .tab-panel th { background: #8e44ad; color: #ffffff; font-weight: 700; padding: 0.75rem; text-align: left; }
        .tab-panel td { padding: 0.75rem; border-bottom: 1px solid rgba(0,0,0,0.06); }
        .tab-panel tr:nth-child(even) { background: rgba(142, 68, 173, 0.03); }

        /* MCQ Card Styles */
        .mcq-card {
            background: #ffffff;
            border: 1px solid rgba(142, 68, 173, 0.2);
            border-radius: 12px;
            padding: 1.25rem;
            margin-bottom: 1.25rem;
            box-shadow: 0 4px 12px rgba(0,0,0,0.03);
            position: relative;
        }

        .pyq-badge {
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            background: linear-gradient(135deg, #e74c3c, #c0392b);
            color: #ffffff;
            font-size: 0.75rem;
            font-weight: 700;
            padding: 0.2rem 0.6rem;
            border-radius: 6px;
            margin-bottom: 0.75rem;
            text-transform: uppercase;
        }

        .mcq-question {
            font-weight: 700;
            font-size: 1.05rem;
            color: var(--text-dark);
            margin-bottom: 1rem;
            line-height: 1.5;
        }

        .mcq-options {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 0.75rem;
            margin-bottom: 1rem;
        }

        .mcq-option {
            background: rgba(142, 68, 173, 0.04);
            border: 1px solid rgba(142, 68, 173, 0.12);
            padding: 0.65rem 0.9rem;
            border-radius: 8px;
            font-size: 0.95rem;
            color: #2c3e50;
            font-weight: 500;
        }

        .mcq-solution-details {
            margin-top: 0.75rem;
            border-top: 1px dashed rgba(0,0,0,0.1);
            padding-top: 0.75rem;
        }

        .mcq-solution-details summary {
            cursor: pointer;
            font-weight: 700;
            color: var(--primary);
            font-size: 0.9rem;
            outline: none;
        }

        .mcq-solution-body {
            margin-top: 0.75rem;
            padding: 0.85rem;
            background: rgba(46, 204, 113, 0.06);
            border-left: 4px solid #2ecc71;
            border-radius: 6px;
            font-size: 0.95rem;
        }

        .correct-answer {
            color: #27ae60;
            font-weight: 700;
            margin-bottom: 0.5rem;
        }

        .topper-trick {
            margin-top: 0.6rem;
            padding: 0.6rem;
            background: rgba(241, 196, 15, 0.15);
            border-left: 3px solid #f39c12;
            border-radius: 4px;
            font-size: 0.9rem;
            color: #d35400;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(6px); }
            to { opacity: 1; transform: translateY(0); }
        }

        @media (max-width: 600px) {
            .tab-panel { padding: 1.1rem; }
            .mcq-options { grid-template-columns: 1fr; }
        }
    </style>
</head>
<body>
    <div id="header-container"></div>

    <main class="quant-container">
        <!-- 5-Tab Navigation -->
        <div class="tab-nav">
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
            <div class="next-tab-btn-container">
              <button type="button" class="next-tab-btn" onclick="const btn = document.querySelector('.main-tabs-nav button[onclick*=\\'tab-tricks\\']'); if (btn) btn.click(); window.scrollTo({top: 0, behavior: 'smooth'});">
                <span class="lang-en">Next: Topper Tricks</span>
                <span class="lang-hi">आगे: टॉपर ट्रिक्स</span>
                <i class="fas fa-arrow-right"></i>
              </button>
            </div>
        </div>

        <!-- Tab 2 Panel -->
        <div id="tab-tricks" class="tab-panel">
            ${tabs.tab2}
            <div class="next-tab-btn-container">
              <button type="button" class="next-tab-btn" onclick="const btn = document.querySelector('.main-tabs-nav button[onclick*=\\'tab-notes\\']'); if (btn) { btn.click(); } window.scrollTo({top: 0, behavior: 'smooth'});">
                <span class="lang-en">Next: Notes & FAQs</span>
                <span class="lang-hi">आगे: नोट्स और अक्सर पूछे जाने वाले प्रश्न</span>
                <i class="fas fa-arrow-right"></i>
              </button>
            </div>
        </div>

        <!-- Tab 3 Panel: Notes & FAQs -->
        <div id="tab-notes" class="tab-panel">
            ${tabs.tab5}
            <div class="next-tab-btn-container">
              <button type="button" class="next-tab-btn" onclick="const btn = document.querySelector('.main-tabs-nav button[onclick*=\\'tab-practice\\']'); if (btn) { btn.click(); } window.scrollTo({top: 0, behavior: 'smooth'});">
                <span class="lang-en">Next: Practice MCQs</span>
                <span class="lang-hi">आगे: अभ्यास प्रश्न (MCQs)</span>
                <i class="fas fa-arrow-right"></i>
              </button>
            </div>
        </div>

        <!-- Tab 4 Panel: Practice MCQs -->
        <div id="tab-practice" class="tab-panel">
            ${tabs.tab3}
            <div class="next-tab-btn-container">
              <button type="button" class="next-tab-btn" onclick="const btn = document.querySelector('.main-tabs-nav button[onclick*=\\'tab-pyqs\\']'); if (btn) { btn.click(); } window.scrollTo({top: 0, behavior: 'smooth'});">
                <span class="lang-en">Next: PYQs (MCQs)</span>
                <span class="lang-hi">आगे: पिछले वर्षों के प्रश्न (PYQs)</span>
                <i class="fas fa-arrow-right"></i>
              </button>
            </div>
        </div>

        <!-- Tab 5 Panel: PYQs -->
        <div id="tab-pyqs" class="tab-panel">
            ${tabs.tab4}
        </div>
    </main>

    <div id="footer-container"></div>

    <script src="/assets/js/main.min.js?v=10f0770d" defer></script>
    <script src="/assets/js/global-header.min.js?v=d6ad26b3" defer></script>
    <script src="/assets/js/global-footer.min.js?v=c641c625" defer></script>

    <script>
        function openTab(evt, tabName) {
            var i, tabpanel, tabbtns;
            tabpanel = document.getElementsByClassName("tab-panel");
            for (i = 0; i < tabpanel.length; i++) {
                tabpanel[i].classList.remove("active");
            }
            tabbtns = document.getElementsByClassName("tab-btn");
            for (i = 0; i < tabbtns.length; i++) {
                tabbtns[i].classList.remove("active");
            }
            document.getElementById(tabName).classList.add("active");
            evt.currentTarget.classList.add("active");
        }
    </script>
</body>
</html>`;
}

async function run() {
    const topicsToGenerate = discoverReasoningTopics();
    console.log(`📋 Total pending Reasoning microtopic pages discovered: ${topicsToGenerate.length}`);

    if (topicsToGenerate.length === 0) {
        console.log('🎉 All Reasoning microtopic pages are already generated and up to date!');
        return;
    }

    console.log('🚀 Starting SSC CGL Reasoning Mobile-First 5-Tab HTML Generator...\n');

    for (let i = 0; i < topicsToGenerate.length; i++) {
        const item = topicsToGenerate[i];
        console.log(`⏳ [${i+1}/${topicsToGenerate.length}] Generating content for Reasoning: ${item.topicName}`);

        try {
            const prompt = buildPrompt(item.topicName);
            const aiText = await callGemini(prompt);
            const tabs = parseTabs(aiText);
            const finalHTML = buildHTMLPage(item.topicName, tabs);

            // Ensure directory exists
            fs.mkdirSync(path.dirname(item.indexPath), { recursive: true });
            fs.writeFileSync(item.indexPath, finalHTML, { encoding: 'utf8' });

            console.log(`✅ Saved: ${item.indexPath}\n`);
            await sleep(1500); // Friendly rate limiting delay
        } catch (err) {
            console.error(`❌ Failed for Reasoning topic: ${item.topicName}`, err.message);
        }
    }

    console.log('🎉 All Reasoning Pages Generated Successfully!');
}

run();
