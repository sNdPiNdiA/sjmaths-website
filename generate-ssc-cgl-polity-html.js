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

function slugify(text) {
    return text.toLowerCase()
        .replace(/[^a-z0-9]+/g, '-')
        .replace(/(^-|-$)+/g, '');
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// Call Gemini API using gemini-3.5-flash-lite with fallback
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

// 18 Polity Topics
const polityTopics = [
    "Constituent Assembly & Making of Constitution",
    "Preamble of the Constitution",
    "Sources of the Indian Constitution",
    "Parts & Schedules of the Constitution",
    "Citizenship (Articles 5-11 & CAA)",
    "Fundamental Rights (Articles 12-35 & Writs)",
    "Directive Principles of State Policy (DPSP, Articles 36-51)",
    "Fundamental Duties (Article 51A & Swaran Singh)",
    "Union Executive: President, VP, PM & Cabinet",
    "Parliament: Lok Sabha, Rajya Sabha & Officers",
    "Parliamentary Proceedings: Bills, Motions & Committees",
    "State Executive: Governor, CM & Council",
    "State Legislature: Assembly & Council",
    "Judiciary: Supreme Court & High Courts",
    "Panchayati Raj System (73rd Amendment & 11th Schedule)",
    "Municipalities (74th Amendment & 12th Schedule)",
    "Constitutional Bodies: EC, FC, CAG, UPSC",
    "Statutory & Non-Constitutional Bodies: NITI Aayog, NHRC, Lokpal"
];

function buildPrompt(topicName) {
    return `You are the Senior Polity Faculty and Content Team of SJMaths.
Your task is to generate complete, high-quality, BILINGUAL (English & Hindi) educational content for SSC CGL General Awareness on the topic: "${topicName}".

MANDATORY RULES:
1. EVERY SINGLE SECTION, HEADING, PARAGRAPH, LIST ITEM, TABLE CELL MUST HAVE BOTH ENGLISH AND HINDI VERSIONS wrapped inside:
   <div class="lang-en">English Content here</div>
   <div class="lang-hi">हिंदी सामग्री यहाँ</div>
   (For small inline texts, use <span class="lang-en">...</span> <span class="lang-hi">...</span>).

2. DO NOT include "Author:", "Target Audience:", or "Estimated Reading Time:" anywhere.

3. Example of required bilingual structure:
<h2><span class="lang-en">Quick Overview</span><span class="lang-hi">त्वरित अवलोकन</span></h2>
<p class="lang-en">Explanation in English here.</p>
<p class="lang-hi">हिंदी में व्याख्या यहाँ।</p>

4. Start from absolute beginner level and progress to SSC CGL exam level.
   Use simple, conversational English with clear explanations.
   Include examples wherever they improve understanding.
   Prefer tables, flowcharts (using Unicode symbols), and bullet points over long paragraphs.
   Highlight constitutional Articles, Parts, Schedules, Amendments, Committees, and landmark judgments wherever relevant.
   Add <div class="exam-tip">...</div>, <div class="remember-this">...</div>, <div class="common-mistake">...</div>, and <div class="py-insight">...</div> callout boxes throughout the content (each with bilingual content).
   Include hyperlinks to related topics using <a href="../related-topic-slug/"> format for internal navigation.
   Be SEO-friendly with proper heading hierarchy (H1 → H2 → H3) and descriptive metadata.

5. CONTENT STRUCTURE for Tab 1 (Concept & Theory) - generate ALL of these sections that are applicable:
   - Quick Overview (short summary of the topic)
   - Learning Objectives (what student will learn)
   - Concept Introduction (start from basics)
   - Important Definitions & Terms (in table format)
   - Detailed Explanation (break down complex ideas into simple parts)
   - Key Articles / Schedules / Amendments (table format with Article numbers, what they say, Hindi meaning)
   - Examples & Illustrations (real-life or exam-style examples)
   - Related Topics Links (internal navigation links)
   - Exam Tips & Common Mistakes
   - Practice Questions (5 simple questions with answers at the end of theory section)

Return your entire output organized with clean HTML tags as demarcated below:

[CONTENT_START]
Full HTML content for Tab 1: Concept & Theory (Bilingual)
[CONTENT_END]

WRITING & FORMATTING RULES:
1. MUST wrap every paragraph, bullet point, heading, and table cell in .lang-en and .lang-hi.
2. DO NOT include Author or Target Audience headers.
3. Do NOT wrap output in markdown \`\`\` code fences.
4. Use <div class="exam-tip">, <div class="remember-this">, <div class="common-mistake">, <div class="py-insight"> for callout boxes.
5. For tables use the premium-table class structure:
   <div class="premium-table-container">
   <table class="premium-table">
   ...
   </table>
   </div>`;
}

function parseContent(aiText) {
    const startTag = '\\[CONTENT_START\\]';
    const endTag = '\\[CONTENT_END\\]';
    const regex = new RegExp(`${startTag}([\\s\\S]*?)${endTag}`);
    const match = aiText.match(regex);
    return match ? match[1].trim() : aiText.trim();
}

function generateSingleHTMLPage(topicName, relativeUrlPath, tab1Content) {
    const h1Title = topicName.replace(/&/g, '&');
    const metaTitle = topicName.replace(/&/g, '&');

    return `<!DOCTYPE html>
<html lang="en">
<head>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7924751316191829" crossorigin="anonymous"></script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${metaTitle} - SSC CGL Polity Notes | SJMaths</title>
    <meta name="description" content="Master ${metaTitle} for SSC CGL General Awareness. Complete bilingual concept notes, articles, amendments, practice questions, and exam tips.">
    <meta name="robots" content="index, follow, max-image-preview:large">
    <link rel="canonical" href="https://sjmaths.com/ssc-cgl/general-awareness/general-policy-polity/${relativeUrlPath}/">
    <meta name="keywords" content="${metaTitle}, SSC CGL Polity, Indian Constitution, General Awareness, SSC CGL Tier 1, SSC CGL Tier 2, SJMaths">
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
    <link rel="stylesheet" href="/assets/css/competitive-exam-guide.min.css?v=bcdc8e39">

    <style>
        :root {
            --glass-bg: rgba(255, 255, 255, 0.96);
            --glass-border: rgba(255, 255, 255, 0.25);
            --shadow-lg: 0 10px 30px -5px rgba(142, 68, 173, 0.12);
            --accent-gradient: linear-gradient(135deg, #8e44ad, #e74c3c);
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

        /* Subject Navigation */
        .subject-nav {
            display: flex;
            gap: 0.4rem;
            margin-bottom: 1.25rem;
            overflow-x: auto;
            padding-bottom: 0.5rem;
            border-bottom: 1px solid rgba(0,0,0,0.05);
            -webkit-overflow-scrolling: touch;
            scrollbar-width: none;
        }

        .subject-nav::-webkit-scrollbar {
            display: none;
        }

        .sub-nav-item {
            padding: 0.4rem 0.85rem;
            text-decoration: none;
            color: var(--text-light);
            font-size: 0.85rem;
            font-weight: 600;
            border-radius: 20px;
            background: rgba(0, 0, 0, 0.03);
            transition: all 0.2s ease;
            white-space: nowrap;
            flex-shrink: 0;
        }

        .sub-nav-item.active {
            background: var(--accent-gradient);
            color: #ffffff;
            box-shadow: 0 4px 10px rgba(142, 68, 173, 0.25);
        }

        /* 4-Tab Navigation */
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
            font-family: 'Outfit', sans-serif;
            font-size: 0.85rem;
            font-weight: 700;
            color: #718096;
            padding: 0.6rem 0.9rem;
            cursor: pointer;
            border-radius: 8px;
            transition: all 0.25s ease;
            display: flex;
            align-items: center;
            gap: 0.4rem;
            white-space: nowrap;
            flex-shrink: 0;
        }

        .tab-btn:hover {
            color: var(--primary);
            background: rgba(142, 68, 173, 0.05);
        }

        .tab-btn.active {
            color: #ffffff;
            background: var(--accent-gradient);
            box-shadow: 0 4px 10px rgba(142, 68, 173, 0.25);
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

        /* Coming Soon */
        .coming-soon-box {
            text-align: center;
            padding: 3rem 1.5rem;
            background: linear-gradient(135deg, rgba(142, 68, 173, 0.03), rgba(231, 76, 60, 0.03));
            border-radius: 1rem;
            border: 2px dashed rgba(142, 68, 173, 0.2);
        }

        .coming-soon-box i {
            font-size: 3rem;
            color: var(--primary);
            margin-bottom: 1rem;
            opacity: 0.6;
        }

        .coming-soon-box h3 {
            font-family: 'Outfit', sans-serif;
            font-size: 1.5rem;
            font-weight: 700;
            color: var(--text-dark);
            margin-bottom: 0.5rem;
        }

        .coming-soon-box p {
            color: var(--text-light);
            font-size: 0.95rem;
            max-width: 400px;
            margin: 0 auto;
        }

        /* Bilingual Language Toggle */
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

        /* Content Typography */
        .tab-panel h2 {
            font-family: 'Outfit', sans-serif;
            font-size: 1.35rem;
            font-weight: 700;
            color: var(--primary);
            margin-top: 1.25rem;
            margin-bottom: 0.85rem;
            border-bottom: 2px solid rgba(142, 68, 173, 0.15);
            padding-bottom: 0.35rem;
        }

        .tab-panel h3 {
            font-family: 'Outfit', sans-serif;
            font-size: 1.1rem;
            font-weight: 700;
            color: var(--text-dark);
            margin-top: 1rem;
            margin-bottom: 0.6rem;
        }

        /* Callout Boxes */
        .exam-tip, .remember-this, .common-mistake, .py-insight {
            padding: 0.85rem 1rem;
            border-radius: 8px;
            margin: 1rem 0;
            border-left: 4px solid;
            font-size: 0.92rem;
        }

        .exam-tip {
            background: rgba(142, 68, 173, 0.06);
            border-left-color: #8e44ad;
        }

        .remember-this {
            background: rgba(52, 152, 219, 0.06);
            border-left-color: #3498db;
        }

        .common-mistake {
            background: rgba(231, 76, 60, 0.06);
            border-left-color: #e74c3c;
        }

        .py-insight {
            background: rgba(46, 204, 113, 0.06);
            border-left-color: #2ecc71;
        }

        .exam-tip::before {
            content: "\\f0eb";
            font-family: "Font Awesome 6 Free";
            font-weight: 900;
            margin-right: 0.5rem;
            color: #8e44ad;
        }

        .remember-this::before {
            content: "\\f0a4";
            font-family: "Font Awesome 6 Free";
            font-weight: 900;
            margin-right: 0.5rem;
            color: #3498db;
        }

        .common-mistake::before {
            content: "\\f071";
            font-family: "Font Awesome 6 Free";
            font-weight: 900;
            margin-right: 0.5rem;
            color: #e74c3c;
        }

        .py-insight::before {
            content: "\\f1ea";
            font-family: "Font Awesome 6 Free";
            font-weight: 900;
            margin-right: 0.5rem;
            color: #2ecc71;
        }

        /* Premium Table */
        .premium-table-container {
            width: 100%;
            overflow-x: auto;
            margin: 1.5rem 0;
            border-radius: 12px;
            border: 1px solid rgba(128, 128, 128, 0.15);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
            background: var(--bg-card, #ffffff);
            -webkit-overflow-scrolling: touch;
        }

        .premium-table {
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
            text-align: left;
            font-size: 0.9rem;
            color: var(--text-dark, #2c3e50);
        }

        .premium-table th {
            background: rgba(142, 68, 173, 0.08);
            font-weight: 700;
            color: var(--primary, #8e44ad);
            padding: 12px 14px;
            border-bottom: 2px solid rgba(142, 68, 173, 0.15);
            white-space: nowrap;
        }

        .premium-table td {
            padding: 12px 14px;
            border-bottom: 1px solid rgba(128, 128, 128, 0.1);
            line-height: 1.6;
            vertical-align: top;
        }

        .premium-table tr:last-child td {
            border-bottom: none;
        }

        .premium-table tr:nth-child(even) td {
            background: rgba(128, 128, 128, 0.015);
        }

        .premium-table tr:hover td {
            background: rgba(142, 68, 173, 0.03);
        }

        /* Responsive Tables fallback */
        .tab-panel table:not(.premium-table) {
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
            background: rgba(142, 68, 173, 0.08);
            color: var(--primary);
            font-weight: 700;
        }

        /* Next Tab Button */
        .next-tab-btn-container {
            margin-top: 2rem;
            text-align: center;
        }

        .next-tab-btn {
            background: var(--accent-gradient);
            color: #fff;
            border: none;
            padding: 0.75rem 1.5rem;
            border-radius: 30px;
            font-family: 'Outfit', sans-serif;
            font-weight: 700;
            font-size: 0.95rem;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }

        .next-tab-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(142, 68, 173, 0.3);
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(6px); }
            to { opacity: 1; transform: translateY(0); }
        }

        @media (max-width: 768px) {
            .topic-container {
                padding: 0.5rem 0.75rem 2rem;
            }
            .tab-panel {
                padding: 1rem;
            }
            .tab-btn {
                font-size: 0.75rem;
                padding: 0.5rem 0.6rem;
            }
            .premium-table {
                font-size: 0.82rem;
            }
            .premium-table th,
            .premium-table td {
                padding: 8px 10px;
            }
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
            <a href="/ssc-cgl/general-awareness/">General Awareness</a> <i class="fas fa-chevron-right" style="font-size: 0.65rem; margin: 0 0.2rem;"></i>
            <a href="/ssc-cgl/general-awareness/general-policy-polity/">General Policy & Polity</a> <i class="fas fa-chevron-right" style="font-size: 0.65rem; margin: 0 0.2rem;"></i>
            <span>${h1Title}</span>
        </div>

        <!-- Topic Header -->
        <div class="topic-header">
            <h1>${h1Title}</h1>
            <p><span class="lang-en">Complete SSC CGL Polity Guide: Concepts, Practice, PYQs & Mock Test</span><span class="lang-hi">संपूर्ण SSC CGL राजनीति गाइड: अवधारणाएं, अभ्यास, PYQ और मॉक टेस्ट</span></p>
        </div>

        <!-- 4-Tab Navigation Bar -->
        <div class="main-tabs-nav">
            <button class="tab-btn active" onclick="openTab(event, 'tab-theory')">
                <i class="fas fa-book-open"></i> <span class="lang-en">1. Concepts & Theory</span><span class="lang-hi">1. अवधारणाएं और सिद्धांत</span>
            </button>
            <button class="tab-btn" onclick="openTab(event, 'tab-practice')">
                <i class="fas fa-tasks"></i> <span class="lang-en">2. Practice Questions</span><span class="lang-hi">2. अभ्यास प्रश्न</span>
            </button>
            <button class="tab-btn" onclick="openTab(event, 'tab-pyqs')">
                <i class="fas fa-history"></i> <span class="lang-en">3. Previous Year Questions</span><span class="lang-hi">3. पिछले वर्ष के प्रश्न</span>
            </button>
            <button class="tab-btn" onclick="openTab(event, 'tab-mini-test')">
                <i class="fas fa-stopwatch"></i> <span class="lang-en">4. Mini Test</span><span class="lang-hi">4. मिनी टेस्ट</span>
            </button>
        </div>

        <!-- Tab 1 Panel: Concepts & Theory -->
        <div id="tab-theory" class="tab-panel active">
            ${tab1Content}
        </div>

        <!-- Tab 2 Panel: Practice Questions (Coming Soon) -->
        <div id="tab-practice" class="tab-panel">
            <div class="coming-soon-box">
                <i class="fas fa-tasks"></i>
                <h3><span class="lang-en">Practice Questions — Coming Soon</span><span class="lang-hi">अभ्यास प्रश्न — जल्द आ रहे हैं</span></h3>
                <p><span class="lang-en">Topic-wise practice questions with detailed solutions are being prepared. Check back soon!</span><span class="lang-hi">विषय-वार अभ्यास प्रश्न विस्तृत समाधान के साथ तैयार किए जा रहे हैं। जल्द ही देखें!</span></p>
            </div>
        </div>

        <!-- Tab 3 Panel: PYQs (Coming Soon) -->
        <div id="tab-pyqs" class="tab-panel">
            <div class="coming-soon-box">
                <i class="fas fa-history"></i>
                <h3><span class="lang-en">Previous Year Questions — Coming Soon</span><span class="lang-hi">पिछले वर्ष के प्रश्न — जल्द आ रहे हैं</span></h3>
                <p><span class="lang-en">SSC CGL previous year questions with trend analysis are being compiled. Stay tuned!</span><span class="lang-hi">SSC CGL के पिछले वर्ष के प्रश्न ट्रेंड विश्लेषण के साथ संकलित किए जा रहे हैं। जुड़े रहें!</span></p>
            </div>
        </div>

        <!-- Tab 4 Panel: Mini Test (Coming Soon) -->
        <div id="tab-mini-test" class="tab-panel">
            <div class="coming-soon-box">
                <i class="fas fa-stopwatch"></i>
                <h3><span class="lang-en">Mini Test — Coming Soon</span><span class="lang-hi">मिनी टेस्ट — जल्द आ रहा है</span></h3>
                <p><span class="lang-en">Timed mini mock tests with performance analytics are under development.</span><span class="lang-hi">समयबद्ध मिनी मॉक टेस्ट प्रदर्शन विश्लेषण के साथ विकसित किए जा रहे हैं।</span></p>
            </div>
        </div>

    </main>

    <div id="footer-container"></div>

    <!-- Scripts -->
    <script data-cfasync="false" defer src="/assets/js/main.min.js?v=10f0770d"></script>
    <script data-cfasync="false" defer src="/assets/js/global-header.min.js?v=d6ad26b3"></script>
    <script data-cfasync="false" defer src="/assets/js/global-footer.min.js?v=c641c625"></script>
    <script>
        function openTab(evt, tabId) {
            const panels = document.querySelectorAll('.tab-panel');
            panels.forEach(p => p.classList.remove('active'));

            const buttons = document.querySelectorAll('.tab-btn');
            buttons.forEach(b => b.classList.remove('active'));

            document.getElementById(tabId).classList.add('active');
            evt.currentTarget.classList.add('active');
        }
    </script>
</body>
</html>`;
}

async function runGenerator() {
    console.log('🚀 Starting SSC CGL Polity 4-Tab HTML Generator...');
    console.log(`📋 Total topics to generate: ${polityTopics.length}\n`);

    for (let i = 0; i < polityTopics.length; i++) {
        const topicName = polityTopics[i];
        const slug = slugify(topicName.replace(/&/g, 'and'));
        console.log(`⏳ [${i + 1}/${polityTopics.length}] Generating: ${topicName}`);

        const prompt = buildPrompt(topicName);

        try {
            const aiResponse = await callGemini(prompt);
            const tab1Content = parseContent(aiResponse);

            const htmlContent = generateSingleHTMLPage(topicName, slug, tab1Content);

            const targetDir = path.join(
                'c:/Users/sande/Documents/GitHub/sjmaths-website/ssc-cgl/general-awareness/general-policy-polity',
                slug
            );
            fs.mkdirSync(targetDir, { recursive: true });

            const targetFile = path.join(targetDir, 'index.html');
            fs.writeFileSync(targetFile, htmlContent, 'utf8');
            console.log(`✅ Saved: ${targetFile}`);
        } catch (err) {
            console.error(`❌ Failed for topic: ${topicName}`, err.message);
        }

        // Wait between API calls to avoid rate limiting
        await sleep(3000);
    }
    console.log('\n🎉 Generation Completed Successfully!');
}

runGenerator();