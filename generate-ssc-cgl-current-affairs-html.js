/**
 * generate-ssc-cgl-current-affairs-html.js
 * Generates 5 Current Affairs topic pages for SSC CGL General Awareness.
 * Output: ssc-cgl/general-awareness/national-and-international-current-events/<slug>/index.html
 *
 * Updated: July 2026
 */

const fs = require('fs');
const path = require('path');
const https = require('https');

// ── API key ─────────────────────────────────────────────────────────────────
const envContent = fs.readFileSync(
    path.join(__dirname, '.env'), 'utf8'
);
const keyMatch = envContent.match(/GEMINI_API_KEY\s*=\s*(.*)/);
const API_KEY = keyMatch ? keyMatch[1].trim() : '';
if (!API_KEY) { console.error('ERROR: GEMINI_API_KEY missing in .env'); process.exit(1); }

// ── Topics ───────────────────────────────────────────────────────────────────
const TOPICS = [
    { name: 'National news, bills, & policies (July 2026)', slug: 'current-affairs-national-news-bills-government-schemes' },
    { name: 'Central & state Government schemes (July 2026)', slug: 'current-affairs-central-state-government-schemes' },
    { name: 'International summits, growth data, & MoUs (July 2026)', slug: 'current-affairs-international-summits-growth-data-mous' },
    { name: 'Awards, honours, & Nobel winners (July 2026)', slug: 'current-affairs-awards-honours-nobel-winners' },
    { name: 'National & global appointments (July 2026)', slug: 'current-affairs-national-global-appointments' },
];

const OUTPUT_DIR = path.join(
    __dirname,
    'ssc-cgl', 'general-awareness', 'national-and-international-current-events'
);

// ── Helpers ──────────────────────────────────────────────────────────────────
function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }

async function callGemini(promptText) {
    const models = ['gemini-3.5-flash', 'gemini-3.6-flash', 'gemini-3.1-flash-lite'];
    let lastErr = null;
    for (const model of models) {
        try {
            const text = await new Promise((resolve, reject) => {
                const payload = JSON.stringify({
                    contents: [{ parts: [{ text: promptText }] }]
                });
                const url = `https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent?key=${API_KEY}`;
                const req = https.request(url, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Content-Length': Buffer.byteLength(payload)
                    }
                }, res => {
                    const chunks = [];
                    res.on('data', c => chunks.push(c));
                    res.on('end', () => {
                        try {
                            const raw = Buffer.concat(chunks).toString('utf8');
                            const json = JSON.parse(raw);
                            if (json.candidates?.[0]?.content) {
                                resolve(json.candidates[0].content.parts[0].text);
                            } else {
                                reject(new Error(raw.substring(0, 300)));
                            }
                        } catch (e) { reject(e); }
                    });
                });
                req.on('error', reject);
                req.write(payload);
                req.end();
            });
            return text;
        } catch (err) {
            console.warn(`  ⚠ Model ${model} failed: ${err.message.substring(0, 80)}...`);
            lastErr = err;
            await sleep(2000);
        }
    }
    throw lastErr;
}

function parseContent(raw) {
    const m = raw.match(/\[CONTENT_START\]([\s\S]*?)\[CONTENT_END\]/);
    return m ? m[1].trim() : raw.trim();
}

// ── Prompt ───────────────────────────────────────────────────────────────────
function buildPrompt(topicName) {
    return `You are the Current Affairs Faculty and Content Team of SJMaths.
Generate complete, high-quality, BILINGUAL (English & Hindi) educational content for SSC CGL General Awareness on the topic: "${topicName}".

IMPORTANT: This content must cover the LATEST developments from JULY 2026. Use real, current, and verified information as of July 2026.

MANDATORY RULES:
1. EVERY SECTION, HEADING, PARAGRAPH, LIST ITEM, TABLE CELL must have BOTH English and Hindi versions:
   <div class="lang-en">English Content</div>
   <div class="lang-hi">हिंदी सामग्री</div>
   (For small inline texts: <span class="lang-en">...</span><span class="lang-hi">...</span>)

2. Do NOT include "Author:", "Target Audience:", or "Estimated Reading Time:".

3. Start with a brief context/background, then cover the July 2026 updates and developments.
    Use simple conversational English. Include real-life examples.
    Prefer tables, flowcharts (Unicode symbols), and bullet points over long paragraphs.
    Highlight important facts, dates, names, and landmark events.
    Add callout boxes: <div class="exam-tip">, <div class="remember-this">, <div class="common-mistake">, <div class="py-insight"> (each bilingual).
    Include internal links using <a href="../related-topic-slug/"> format.
    Use proper heading hierarchy (H2 → H3 only; H1 is in the page template).

4. CONTENT STRUCTURE for Tab 1 (Concept & Theory) — include ALL applicable sections:
   - Quick Overview (2–3 sentence summary)
   - Learning Objectives (bullet list)
   - Concept Introduction (basics first)
   - Important Definitions & Terms (premium-table format)
   - Detailed Explanation (simple → complex)
   - Key Facts / Dates / Names / Events (premium-table) — MUST include July 2026 updates
   - Examples & Context (describe in text for clarity)
   - Related Topics (internal links)
   - Exam Tips & Common Mistakes
   - Practice Questions (5 MCQs with answers)

Return output demarcated as:

[CONTENT_START]
Full HTML content for Tab 1: Concept & Theory (Bilingual, latest July 2026)
[CONTENT_END]

WRITING & FORMATTING RULES:
1. Wrap every paragraph, heading, list item, and table cell in .lang-en and .lang-hi.
2. No Author/Target Audience headers.
3. No markdown \\\`\\\`\\\` code fences around output.
4. Use <div class="exam-tip">, <div class="remember-this">, <div class="common-mistake">, <div class="py-insight"> for callouts.
5. For tables:
   <div class="premium-table-container">
   <table class="premium-table">...</table>
   </div>
6. CRITICAL RULE — lang-en sections:
   - For dates/numbers use plain text: January 1, 2024, 1947, etc.
   - For formulas/measurements use LaTeX: inline $formula$ and display $$formula$$.
   - ONLY English letters/symbols inside LaTeX.
7. CRITICAL RULE — lang-hi sections:
   - Do NOT use LaTeX $...$ or $$...$ in Hindi sections.
   - Write dates/numbers as plain text.
   - Use <sub> and <sup> for subscripts/superscripts.`;
}

// ── MathJax block (array join avoids $ mangling) ─────────────────────────────
const MATHJAX_BLOCK = [
    '',
    '    <!-- MathJax v3 -->',
    '    <script>',
    '        window.MathJax = {',
    '            tex: {',
    "                inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],",
    "                displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']],",
    '                processEscapes: true',
    '            },',
    '            options: {',
    "                skipHtmlTags: ['script','noscript','style','textarea','pre']",
    '            }',
    '        };',
    '    </script>',
    '    <script async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>',
    ''
].join('\n');

// ── HTML builder (array parts — safe with $ in content) ──────────────────────
function buildHTML(topicName, slug, tab1Content) {
    const safeTitle = topicName.replace(/&/g, '&');
    const gradColor = '#16a085';
    const gradColor2 = '#27ae60';
    const accentGrad = `linear-gradient(135deg, ${gradColor}, ${gradColor2})`;

    const parts = [];

    parts.push(`<!DOCTYPE html>
<html lang="en">
<head>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7924751316191829" crossorigin="anonymous"></script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${safeTitle} - SSC CGL Current Affairs Notes | SJMaths</title>
    <meta name="description" content="Master ${safeTitle} for SSC CGL General Awareness. Bilingual concept notes, tables, practice questions, and exam tips.">
    <meta name="robots" content="index, follow, max-image-preview:large">
    <link rel="canonical" href="https://sjmaths.com/ssc-cgl/general-awareness/national-and-international-current-events/${slug}/">
    <meta name="keywords" content="${safeTitle}, SSC CGL Current Affairs, General Awareness, SSC CGL Tier 1, SJMaths">
    <meta name="author" content="SJMaths">
    <link rel="icon" type="image/png" href="/favicon.png">

    <!-- Fonts & Icons -->
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
    <link rel="stylesheet" href="/assets/css/competitive-exam-guide.min.css?v=bcdc8e39">`);

    parts.push(MATHJAX_BLOCK);

    parts.push(`
    <style>
        :root {
            --cat-grad: ${accentGrad};
            --glass-bg: rgba(255,255,255,0.96);
            --glass-border: rgba(255,255,255,0.25);
            --shadow-lg: 0 10px 30px -5px rgba(0,0,0,0.1);
        }
        .topic-container { max-width: 1050px; margin: 1rem auto; padding: 0.75rem 1rem 3rem; animation: fadeIn .4s ease-out; }
        .breadcrumbs { margin-bottom: 1rem; font-size: 0.85rem; color: var(--text-light); display: flex; align-items: center; flex-wrap: wrap; gap: 0.3rem; }
        .breadcrumbs a { color: var(--primary); text-decoration: none; font-weight: 500; }
        .topic-header { background: var(--glass-bg); border: 1px solid var(--glass-border); border-radius: 1rem; padding: 1.25rem 1rem; box-shadow: var(--shadow-lg); margin-bottom: 1.25rem; text-align: center; }
        .topic-header h1 { font-family: 'Outfit', sans-serif; font-size: clamp(1.5rem,5vw,2.2rem); font-weight: 800; background: var(--cat-grad); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: .4rem; line-height: 1.2; }
        .main-tabs-nav { display: flex; gap: .4rem; margin-bottom: 1.25rem; border-bottom: 2px solid #e2e8f0; padding-bottom: .4rem; overflow-x: auto; -webkit-overflow-scrolling: touch; scrollbar-width: none; }
        .main-tabs-nav::-webkit-scrollbar { display: none; }
        .tab-btn { background: transparent; border: none; outline: none; font-family: 'Outfit', sans-serif; font-size: .85rem; font-weight: 700; color: #718096; padding: .6rem .9rem; cursor: pointer; border-radius: 8px; transition: all .25s ease; display: flex; align-items: center; gap: .4rem; white-space: nowrap; flex-shrink: 0; }
        .tab-btn:hover { color: ${gradColor2}; background: rgba(0,0,0,.04); }
        .tab-btn.active { color: #fff; background: var(--cat-grad); box-shadow: 0 4px 10px rgba(0,0,0,.15); }
        .tab-panel { display: none; background: var(--glass-bg); border: 1px solid var(--glass-border); border-radius: 1rem; padding: 1.25rem; box-shadow: var(--shadow-lg); animation: fadeIn .35s ease-out; line-height: 1.65; color: var(--text-dark); }
        .tab-panel.active { display: block; }
        .coming-soon-box { text-align: center; padding: 3rem 1.5rem; background: linear-gradient(135deg, rgba(0,0,0,.02), rgba(0,0,0,.02)); border-radius: 1rem; border: 2px dashed rgba(0,0,0,.12); }
        .coming-soon-box i { font-size: 3rem; color: ${gradColor2}; margin-bottom: 1rem; opacity: .6; }
        .coming-soon-box h3 { font-family: 'Outfit', sans-serif; font-size: 1.5rem; font-weight: 700; margin-bottom: .5rem; }
        .coming-soon-box p { color: var(--text-light); font-size: .95rem; max-width: 400px; margin: 0 auto; }
        .lang-hi { display: none; }
        body.lang-mode-hi .lang-en { display: none !important; }
        body.lang-mode-hi .lang-hi { display: block !important; }
        body.lang-mode-hi span.lang-hi, body.lang-mode-hi strong.lang-hi, body.lang-mode-hi i.lang-hi { display: inline-block !important; }
        .tab-panel h2 { font-family: 'Outfit', sans-serif; font-size: 1.35rem; font-weight: 700; color: ${gradColor2}; margin-top: 1.25rem; margin-bottom: .85rem; border-bottom: 2px solid rgba(0,0,0,.08); padding-bottom: .35rem; }
        .tab-panel h3 { font-family: 'Outfit', sans-serif; font-size: 1.1rem; font-weight: 700; color: var(--text-dark); margin-top: 1rem; margin-bottom: .6rem; }
        .exam-tip, .remember-this, .common-mistake, .py-insight { padding: .85rem 1rem; border-radius: 8px; margin: 1rem 0; border-left: 4px solid; font-size: .92rem; }
        .exam-tip { background: rgba(39,174,96,.06); border-left-color: #27ae60; }
        .remember-this { background: rgba(41,128,185,.06); border-left-color: #2980b9; }
        .common-mistake { background: rgba(231,76,60,.06); border-left-color: #e74c3c; }
        .py-insight { background: rgba(243,156,18,.06); border-left-color: #f39c12; }
        .premium-table-container { width: 100%; overflow-x: auto; margin: 1.5rem 0; border-radius: 12px; border: 1px solid rgba(128,128,128,.15); box-shadow: 0 4px 12px rgba(0,0,0,.03); background: var(--bg-card,#fff); -webkit-overflow-scrolling: touch; }
        .premium-table { width: 100%; border-collapse: separate; border-spacing: 0; text-align: left; font-size: .9rem; color: var(--text-dark,#2c3e50); }
        .premium-table th { background: rgba(0,0,0,.04); font-weight: 700; color: ${gradColor2}; padding: 12px 14px; border-bottom: 2px solid rgba(0,0,0,.08); white-space: nowrap; }
        .premium-table td { padding: 12px 14px; border-bottom: 1px solid rgba(128,128,128,.1); line-height: 1.6; vertical-align: top; }
        .premium-table tr:last-child td { border-bottom: none; }
        .premium-table tr:nth-child(even) td { background: rgba(128,128,128,.015); }
        .premium-table tr:hover td { background: rgba(0,0,0,.02); }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }
        @media (max-width: 768px) { .topic-container { padding: .5rem .75rem 2rem; } .tab-panel { padding: 1rem; } .tab-btn { font-size: .75rem; padding: .5rem .6rem; } .premium-table { font-size: .82rem; } .premium-table th, .premium-table td { padding: 8px 10px; } }
    </style>
</head>
<body>
    <div id="header-container"></div>
    <main class="topic-container" id="main-content">
        <div class="breadcrumbs">
            <a href="/">Home</a> <i class="fas fa-chevron-right" style="font-size:.65rem;margin:0 .2rem;"></i>
            <a href="/ssc-cgl/syllabus/">SSC CGL Syllabus</a> <i class="fas fa-chevron-right" style="font-size:.65rem;margin:0 .2rem;"></i>
            <a href="/ssc-cgl/general-awareness/">General Awareness</a> <i class="fas fa-chevron-right" style="font-size:.65rem;margin:0 .2rem;"></i>
            <a href="/ssc-cgl/general-awareness/national-and-international-current-events/">Current Affairs</a> <i class="fas fa-chevron-right" style="font-size:.65rem;margin:0 .2rem;"></i>
            <span>${safeTitle}</span>
        </div>
        <div class="topic-header">
            <h1>${safeTitle}</h1>
            <p><span class="lang-en">Complete SSC CGL Current Affairs Guide: Latest July 2026 Updates, Concepts, Facts & Exam Tips</span><span class="lang-hi">संपूर्ण SSC CGL करंट अफेयर्स गाइड: जुलाई 2026 के नवीनतम अपडेट, अवधारणाएं, तथ्य और परीक्षा टिप्स</span></p>
        </div>
        <div class="main-tabs-nav">
            <button class="tab-btn active" onclick="openTab(event,'tab-theory')">
                <i class="fas fa-book-open"></i> <span class="lang-en">1. Concepts & Theory</span><span class="lang-hi">1. अवधारणाएं और सिद्धांत</span>
            </button>
            <button class="tab-btn" onclick="openTab(event,'tab-practice')">
                <i class="fas fa-tasks"></i> <span class="lang-en">2. Practice Questions</span><span class="lang-hi">2. अभ्यास प्रश्न</span>
            </button>
            <button class="tab-btn" onclick="openTab(event,'tab-pyqs')">
                <i class="fas fa-history"></i> <span class="lang-en">3. Previous Year Questions</span><span class="lang-hi">3. पिछले वर्ष के प्रश्न</span>
            </button>
            <button class="tab-btn" onclick="openTab(event,'tab-mini-test')">
                <i class="fas fa-stopwatch"></i> <span class="lang-en">4. Mini Test</span><span class="lang-hi">4. मिनी टेस्ट</span>
            </button>
        </div>
        <div id="tab-theory" class="tab-panel active">`);

    parts.push('\n');
    parts.push(tab1Content);
    parts.push(`
        </div>
        <div id="tab-practice" class="tab-panel">
            <div class="coming-soon-box">
                <i class="fas fa-tasks"></i>
                <h3><span class="lang-en">Practice Questions — Coming Soon</span><span class="lang-hi">अभ्यास प्रश्न — जल्द आ रहे हैं</span></h3>
                <p><span class="lang-en">Topic-wise practice questions with detailed solutions are being prepared.</span><span class="lang-hi">विषय-वार अभ्यास प्रश्न विस्तृत समाधान के साथ तैयार किए जा रहे हैं।</span></p>
            </div>
        </div>
        <div id="tab-pyqs" class="tab-panel">
            <div class="coming-soon-box">
                <i class="fas fa-history"></i>
                <h3><span class="lang-en">Previous Year Questions — Coming Soon</span><span class="lang-hi">पिछले वर्ष के प्रश्न — जल्द आ रहे हैं</span></h3>
                <p><span class="lang-en">SSC CGL previous year questions with trend analysis are being compiled.</span><span class="lang-hi">SSC CGL के पिछले वर्ष के प्रश्न संकलित किए जा रहे हैं।</span></p>
            </div>
        </div>
        <div id="tab-mini-test" class="tab-panel">
            <div class="coming-soon-box">
                <i class="fas fa-stopwatch"></i>
                <h3><span class="lang-en">Mini Test — Coming Soon</span><span class="lang-hi">मिनी टेस्ट — जल्द आ रहा है</span></h3>
                <p><span class="lang-en">Timed mini mock tests with performance analytics are under development.</span><span class="lang-hi">समयबद्ध मिनी मॉक टेस्ट विकसित किए जा रहे हैं।</span></p>
            </div>
        </div>
    </main>
    <div id="footer-container"></div>
    <script data-cfasync="false" defer src="/assets/js/main.min.js?v=10f0770d"></script>
    <script data-cfasync="false" defer src="/assets/js/global-header.min.js?v=d6ad26b3"></script>
    <script data-cfasync="false" defer src="/assets/js/global-footer.min.js?v=c641c625"></script>
    <script>
        function openTab(evt, tabId) {
            document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
            document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
            document.getElementById(tabId).classList.add('active');
            evt.currentTarget.classList.add('active');
        }
    </script>
</body>
</html>`);

    return parts.join('');
}

// ── Main ─────────────────────────────────────────────────────────────────────
async function main() {
    console.log('📚 SSC CGL Current Affairs Page Generator (July 2026)\n');
    fs.mkdirSync(OUTPUT_DIR, { recursive: true });

    for (let i = 0; i < TOPICS.length; i++) {
        const { name, slug } = TOPICS[i];
        console.log(`⏳ [${i + 1}/${TOPICS.length}] ${name}`);

        try {
            const raw = await callGemini(buildPrompt(name));
            const tab1 = parseContent(raw);
            const html = buildHTML(name, slug, tab1);

            const dir = path.join(OUTPUT_DIR, slug);
            fs.mkdirSync(dir, { recursive: true });
            fs.writeFileSync(path.join(dir, 'index.html'), html, { encoding: 'utf8' });
            console.log(`  ✅ Saved: national-and-international-current-events/${slug}/index.html`);
        } catch (err) {
            console.error(`  ❌ Failed: ${name} —`, err.message);
        }

        if (i < TOPICS.length - 1) await sleep(4000);
    }

    console.log('\n🎉 Current Affairs generation complete!');
    console.log(`📁 Output: ssc-cgl/general-awareness/national-and-international-current-events/`);
}

main();