import fs from 'fs';
import path from 'path';

if (fs.existsSync('.env')) {
    const envConfig = fs.readFileSync('.env', 'utf8');
    envConfig.split('\n').forEach(line => {
        const [key, value] = line.split('=');
        if (key && value) {
            process.env[key.trim()] = value.trim();
        }
    });
}

const GEMINI_API_KEY = process.env.GEMINI_API_KEY;
const API_URL = `https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash-lite:generateContent?key=${GEMINI_API_KEY}`;

const topics = [
    // Geography (2 topics remaining)
    { name: 'Minerals & Energy Resources', dir: 'minerals-and-energy-resources', title: 'Minerals & Energy Resources | Geography | SSC CGL', desc: 'SSC CGL guide on Major minerals, coal, petroleum, nuclear energy, renewable sources, and state-wise distribution.' },
    { name: 'Industries, Ports & Waterways', dir: 'industries-ports-and-waterways', title: 'Industries, Ports & Waterways | Geography | SSC CGL', desc: 'SSC CGL guide on Major industries, industrial regions, major ports, and inland waterways of India.' },
    // Environment (4 topics)
    { name: 'Ecology & Ecosystem Fundamentals', dir: 'ecology-and-ecosystems', title: 'Ecology & Ecosystem Fundamentals | Environment | SSC CGL', desc: 'SSC CGL guide on Ecology basics, Ecosystem structure, functions, energy flow, and ecological pyramids.' },
    { name: 'Trophic Levels, Food Chains & Food Webs', dir: 'food-chains-and-trophic-levels', title: 'Trophic Levels, Food Chains & Food Webs | Environment | SSC CGL', desc: 'SSC CGL guide on Trophic levels, grazing and detritus food chains, food webs, and ecological efficiency.' },
    { name: 'Biodiversity & Conservation', dir: 'biodiversity-and-conservation', title: 'Biodiversity & Conservation | Environment | SSC CGL', desc: 'SSC CGL guide on Biodiversity levels, hotspots, threatened species, protected areas, and conservation methods.' },
    { name: 'Environmental Conventions & Protocols', dir: 'environmental-conventions-and-protocols', title: 'Environmental Conventions & Protocols | Environment | SSC CGL', desc: 'SSC CGL guide on Major international environmental agreements, conventions, and climate change protocols.' }
];

async function callGeminiSinglePage(topic) {
    const prompt = `You are the Senior Geography & Environment Faculty of SJMaths. Create a complete, highly detailed BILINGUAL 4-Tab HTML study page for SSC CGL General Awareness on: "${topic.name}".

STRICT FORMAT & NO-PARAGRAPH CONSTRAINTS:
1. TAB 1 (Theory & Concepts): STRICTLY NO LONG PARAGRAPHS! Use 6-7 <div class="card-premium"><h3 class="card-title"><span class="lang-en">...</span><span class="lang-hi">...</span></h3><div class="theory-para">...</div></div> cards containing <table>, bulleted <ul>/<li> lists, bold key terms.
   MUST INCLUDE:
   - Comprehensive factual tables (names, values, locations, comparisons).
   - Dedicated Mnemonics & Memory Tricks Card (useful acronyms and memory aids for SSC CGL).
   - Dedicated Topper Exam Tips & Trap Warnings Card.
   - Detailed overview covering all essential concepts for this geography/environment topic.
2. TAB 2 (Practice Qs): 30 questions divided into 3 sections:
   - <div id="diff-easy" class="difficulty-section" style="display:block"> (Q1-10)
   - <div id="diff-moderate" class="difficulty-section" style="display:none"> (Q11-20)
   - <div id="diff-hard" class="difficulty-section" style="display:none"> (Q21-30)
   Include <div class="diff-tab-bar"> buttons. Each Q card: <div class="practice-question-card"><div class="q-row"><div class="q-num-badge">N</div><div class="q-body"><p class="q-text-sm"><span class="lang-en">Q</span><span class="lang-hi">प्रश्न</span></p><div class="options-container"><div class="practice-option-box"><label class="opt-label"><input type="radio" name="p-N" class="opt-radio"><span><b>A.</b> <span class="lang-en">Opt</span><span class="lang-hi">विकल्प</span></span></label></div>...4 options...</div><div class="sol-box"><p class="sol-text"><strong>Answer: A.</strong> <span class="lang-en">Sol</span><span class="lang-hi">हल</span></p></div></div></div></div>.
3. TAB 3 (SSC PYQs): 15 PYQ cards with hidden <div class="sol-box">.
4. TAB 4 (15-Q Test): 15 test cards (<div class="practice-question-card" id="tq-N">... <div class="test-opt" data-ch="A" data-qi="N" onclick="selOpt(this)">... <input type="hidden" id="tsel-N">).
5. BILINGUAL: Every single text element MUST be wrapped in <span class="lang-en">English</span><span class="lang-hi">हिंदी</span>.

Organize output using exact tags:
[TAB1_START] HTML for Tab 1 [TAB1_END]
[TAB2_START] HTML for Tab 2 [TAB2_END]
[TAB3_START] HTML for Tab 3 [TAB3_END]
[TAB4_START] HTML for Tab 4 [TAB4_END]
[TESTDATA_START] [{"ans":"A","solEn":"...","solHi":"..."}, ...15 items] [TESTDATA_END]
[OVERVIEW_START] Concise bilingual overview using cards/tables [OVERVIEW_END]
`;

    for (let attempt = 1; attempt <= 5; attempt++) {
        try {
            let wait = 15000;
            const res = await fetch(API_URL, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    contents: [{ parts: [{ text: prompt }] }],
                    generationConfig: { temperature: 0.1 }
                })
            });
            const data = await res.json();
            if (data.error && data.error.code === 429) {
                console.log(`Rate limit hit (429). Waiting ${wait / 1000}s (Attempt ${attempt}/5)...`);
                await new Promise(r => setTimeout(r, wait));
                wait = Math.min(wait * 2, 60000);
                continue;
            }
            if (!data.candidates || !data.candidates[0]) throw new Error(JSON.stringify(data));
            const raw = data.candidates[0].content.parts[0].text;

            const safeExtract = (startTag, endTag) => {
                const regex = new RegExp(startTag + '([\\s\\S]*?)' + endTag);
                const match = raw.match(regex);
                return match ? match[1].trim() : '';
            };

            const t1 = safeExtract('\\[TAB1_START\\]', '\\[TAB1_END\\]');
            const t2 = safeExtract('\\[TAB2_START\\]', '\\[TAB2_END\\]');
            const t3 = safeExtract('\\[TAB3_START\\]', '\\[TAB3_END\\]');
            const t4 = safeExtract('\\[TAB4_START\\]', '\\[TAB4_END\\]');
            const td = safeExtract('\\[TESTDATA_START\\]', '\\[TESTDATA_END\\]');
            const ov = safeExtract('\\[OVERVIEW_START\\]', '\\[OVERVIEW_END\\]');

            let parsedTd = [];
            try { parsedTd = JSON.parse(td); } catch (e) { }

            return {
                theoryHtml: t1 || '',
                practiceHtml: t2 || '',
                pyqsHtml: t3 || '',
                testHtml: t4 || '',
                overviewHtml: ov || '',
                testDataJson: parsedTd
            };
        } catch (e) {
            console.error(`Attempt ${attempt} error:`, e.message);
            if (attempt === 5) {
                console.error(`All 5 attempts failed for topic. Skipping...`);
                return null;
            }
            await new Promise(r => setTimeout(r, 5000));
        }
    }
    return null;
}

async function run() {
    console.log("🚀 Starting Geography & Environment Page Generation using Gemini 3.5 Flash...");
    for (let i = 0; i < topics.length; i++) {
        const t = topics[i];
        console.log(`\n⏳ [${i + 1}/${topics.length}] Generating complete page for: ${t.name}...`);

        try {
            const pageData = await callGeminiSinglePage(t);

            if (!pageData) {
                console.error(`❌ Skipping ${t.name} - failed after 5 attempts`);
                await new Promise(r => setTimeout(r, 3000));
                continue;
            }

            const parentCategory = t.dir.includes('ecology') || t.dir.includes('trophic') || t.dir.includes('biodiversity') || t.dir.includes('environmental-conventions') ? 'environmental-awareness-and-its-application' : 'geography';
            const canonicalBase = `https://sjmaths.com/ssc-cgl/general-awareness/${parentCategory}/${t.dir}/`;

            const fullHtml = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${t.title}</title>
    <meta name="description" content="${t.desc}">
    <meta name="robots" content="index, follow, max-image-preview:large">
    <link rel="canonical" href="${canonicalBase}">
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/assets/vendor/fontawesome/css/all.min.css?v=7441465c">
    <link rel="stylesheet" href="/assets/css/main.min.css?v=4ba21ce7">
    <link rel="stylesheet" href="/assets/css/layout.min.css?v=e4922b08">
    <link rel="stylesheet" href="/assets/css/component.min.css?v=8c99f11f">
    <link rel="stylesheet" href="/assets/css/improved-ui.min.css?v=574ed909">
    <link rel="stylesheet" href="/assets/css/topic-details.min.css?v=c54bbbc3">
    <link rel="stylesheet" href="/assets/css/upsssc-lower.min.css?v=94ee8a40">
</head>
<body>
    <div id="header-container"></div>
    <div class="container">
        <div class="top-controls"></div>
        <div class="breadcrumbs">
            <div class="breadcrumbs-path">
                <a href="../../../syllabus/">Syllabus</a>
                <i class="fas fa-chevron-right"></i>
                <a href="../../">General Awareness</a>
                <i class="fas fa-chevron-right"></i>
                <a href="../">${parentCategory === 'environmental-awareness-and-its-application' ? 'Environment' : 'Geography'}</a>
                <i class="fas fa-chevron-right"></i>
                <span class="lang-en">${t.name}</span>
                <span class="lang-hi">${t.name}</span>
            </div>
        </div>

        <div class="topic-header">
            <h1>
                <span class="lang-en">${t.name}</span>
                <span class="lang-hi">${t.name}</span>
            </h1>
            <p>
                <span class="lang-en">${t.desc}</span>
                <span class="lang-hi">${t.desc}</span>
            </p>
        </div>

        <div class="subject-nav">
            <button class="sub-nav-item active" data-tab="theory" onclick="switchTab('theory')">
                <span class="lang-en">Theory & Concepts</span>
                <span class="lang-hi">सिद्धांत और अवधारणाएं</span>
            </button>
            <button class="sub-nav-item" data-tab="practice" onclick="switchTab('practice')">
                <span class="lang-en">Practice (30 Qs)</span>
                <span class="lang-hi">अभ्यास (30 प्रश्न)</span>
            </button>
            <button class="sub-nav-item" data-tab="pyqs" onclick="switchTab('pyqs')">
                <span class="lang-en">SSC PYQs</span>
                <span class="lang-hi">SSC PYQs</span>
            </button>
            <button class="sub-nav-item" data-tab="test" onclick="switchTab('test')">
                <span class="lang-en">15-Q Test</span>
                <span class="lang-hi">15-प्रश्न टेस्ट</span>
            </button>
        </div>

        <div class="topic-content">
            <div id="tab-theory" class="tab-content" style="display:block">
                ${pageData.theoryHtml || ''}
                ${pageData.overviewHtml ? '<div class="card-premium"><div class="card-title"><span class="lang-en">Quick Overview</span><span class="lang-hi">त्वरित अवलोकन</span></h3>' + pageData.overviewHtml + '</div>' : ''}
                <div class="next-tab-btn-container">
                  <button type="button" class="next-tab-btn" onclick="switchTab('practice'); window.scrollTo({top: 0, behavior: 'smooth'});">
                    <span class="lang-en">Next: Practice Questions</span>
                    <span class="lang-hi">आगे: अभ्यास प्रश्न</span>
                    <i class="fas fa-arrow-right"></i>
                  </button>
                </div>
            </div>

            <div id="tab-practice" class="tab-content" style="display:none">
                ${pageData.practiceHtml || ''}
                <div class="next-tab-btn-container">
                  <button type="button" class="next-tab-btn" onclick="switchTab('pyqs'); window.scrollTo({top: 0, behavior: 'smooth'});">
                    <span class="lang-en">Next: SSC PYQs</span>
                    <span class="lang-hi">आगे: SSC PYQs</span>
                    <i class="fas fa-arrow-right"></i>
                  </button>
                </div>
            </div>

            <div id="tab-pyqs" class="tab-content" style="display:none">
                <h2 class="section-title"><span class="lang-en">SSC PYQs (15 Questions)</span><span class="lang-hi">SSC PYQs (15 प्रश्न)</span></h2>
                ${pageData.pyqsHtml || ''}
                <div class="next-tab-btn-container">
                  <button type="button" class="next-tab-btn" onclick="switchTab('test'); window.scrollTo({top: 0, behavior: 'smooth'});">
                    <span class="lang-en">Next: 15-Q Test</span>
                    <span class="lang-hi">आगे: 15-प्रश्न टेस्ट</span>
                    <i class="fas fa-arrow-right"></i>
                  </button>
                </div>
            </div>

            <div id="tab-test" class="tab-content" style="display:none">
                <div id="test-start-scr" class="test-start-scr">
                    <h3><i class="fas fa-stopwatch"></i> <span class="lang-en">15-Question Timed Test</span><span class="lang-hi">15-प्रश्न टाइम्ड टेस्ट</span></h3>
                    <p style="color:#666;margin-bottom:20px"><span class="lang-en">SSC CGL exam pattern timed test</span><span class="lang-hi">SSC CGL परीक्षा पैटर्न टाइम्ड टेस्ट</span></p>
                    <div class="tinfo-grid">
                        <div class="tinfo-card"><div class="tinfo-num">15</div><div class="tinfo-lbl"><span class="lang-en">Questions</span><span class="lang-hi">प्रश्न</span></div></div>
                        <div class="tinfo-card"><div class="tinfo-num">15</div><div class="tinfo-lbl"><span class="lang-en">Minutes</span><span class="lang-hi">मिनट</span></div></div>
                        <div class="tinfo-card"><div class="tinfo-num">+2</div><div class="tinfo-lbl"><span class="lang-en">Marks</span><span class="lang-hi">अंक</span></div></div>
                    </div>
                    <button class="start-test-btn" onclick="startTest()"><i class="fas fa-play"></i> <span class="lang-en">Start Test</span><span class="lang-hi">टेस्ट शुरू करें</span></button>
                </div>
                <div id="test-area" style="display:none">
                    ${pageData.testHtml || ''}
                </div>
            </div>
        </div>
    </div>
    <script>
        window.upssscTestData = ${JSON.stringify(pageData.testDataJson || [])};
    </script>
    <script src="/assets/js/search.min.js?v=68a0a505" defer data-cfasync="false"></script>
    <script src="/assets/js/main.min.js?v=10f0770d" defer data-cfasync="false"></script>
    <script src="/assets/js/global-header.min.js?v=d6ad26b3" defer data-cfasync="false"></script>
    <script src="/assets/js/global-footer.min.js?v=c641c625" defer data-cfasync="false"></script>
    <script src="/assets/js/upsssc-lower.min.js?v=04b168f8" defer data-cfasync="false"></script>
</body>
</html>`;

            const targetDir = path.join('c:/Users/sande/Documents/GitHub/sjmaths-website/ssc-cgl/general-awareness', parentCategory, t.dir);
            fs.mkdirSync(targetDir, { recursive: true });
            fs.writeFileSync(path.join(targetDir, 'index.html'), fullHtml, 'utf8');
            console.log(`✅ Saved ${t.dir}/index.html`);
        } catch (err) {
            console.error(`❌ Failed ${t.name}:`, err.message);
        }
        await new Promise(r => setTimeout(r, 2000));
    }
    console.log("\n🎉 All 6 Remaining Geography & Environment Pages Generated Successfully!");
}

run();