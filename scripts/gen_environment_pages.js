/**
 * UPSSSC Lower Mains Environment Page Generator
 * Formatting matches scripts/gen_history_pages.js.
 * Run: node scripts/gen_environment_pages.js
 */

require('dotenv').config();
const { GoogleGenAI } = require('@google/genai');
const fs = require('fs');
const path = require('path');

const API_KEY = process.env.GEMINI_API_KEY;
const ai = new GoogleGenAI({ apiKey: API_KEY });
const BASE = path.join(__dirname, '..', 'upsssc-lower-mains', 'environment');

const TOPICS = [
    ['air-water-and-soil-pollution-causes-effects', 'Air, Water and Soil Pollution: Causes and Effects', 'वायु, जल और मृदा प्रदूषण: कारण और प्रभाव'],
    ['basics-of-ecology-ecosystem-structure', 'Basics of Ecology and Ecosystem Structure', 'पारिस्थितिकी के मूल तत्व और पारिस्थितिकी तंत्र की संरचना'],
    ['biogeochemical-cycles-carbon-nitrogen-water', 'Biogeochemical Cycles: Carbon, Nitrogen and Water', 'जैव-भू-रासायनिक चक्र: कार्बन, नाइट्रोजन और जल'],
    ['climate-change-global-warming-greenhouse-effect', 'Climate Change, Global Warming and Greenhouse Effect', 'जलवायु परिवर्तन, वैश्विक ऊष्मीकरण और ग्रीनहाउस प्रभाव'],
    ['concepts-and-levels-of-biodiversity', 'Concepts and Levels of Biodiversity', 'जैव विविधता की अवधारणा और स्तर'],
    ['disaster-management-cycle-mitigation-preparedness-response-recovery', 'Disaster Management Cycle: Mitigation, Preparedness, Response and Recovery', 'आपदा प्रबंधन चक्र: न्यूनीकरण, तैयारी, प्रतिक्रिया और पुनर्प्राप्ति'],
    ['food-chains-food-webs-and-ecological-pyramids', 'Food Chains, Food Webs and Ecological Pyramids', 'खाद्य श्रृंखला, खाद्य जाल और पारिस्थितिक पिरामिड'],
    ['important-conservation-projects-project-tiger-elephant', 'Important Conservation Projects: Project Tiger and Project Elephant', 'महत्वपूर्ण संरक्षण परियोजनाएं: प्रोजेक्ट टाइगर और प्रोजेक्ट एलीफेंट'],
    ['important-environmental-protocols-kyoto-montreal-paris', 'Important Environmental Protocols: Kyoto, Montreal and Paris', 'महत्वपूर्ण पर्यावरणीय समझौते: क्योटो, मॉन्ट्रियल और पेरिस'],
    ['in-situ-ex-situ-conservation-national-parks-sanctuaries', 'In-situ and Ex-situ Conservation: National Parks and Sanctuaries', 'इन-सीटू और एक्स-सीटू संरक्षण: राष्ट्रीय उद्यान और अभयारण्य'],
    ['institutional-framework-ndma-sdma-ndrf', 'Institutional Framework: NDMA, SDMA and NDRF', 'संस्थागत ढांचा: एनडीएमए, एसडीएमए और एनडीआरएफ'],
    ['major-biomes-and-ecotones', 'Major Biomes and Ecotones', 'प्रमुख बायोम और इकोटोन'],
    ['ozone-layer-depletion-acid-rain', 'Ozone Layer Depletion and Acid Rain', 'ओजोन परत क्षरण और अम्ल वर्षा'],
    ['threats-to-biodiversity-iucn-red-list', 'Threats to Biodiversity and IUCN Red List', 'जैव विविधता को खतरे और आईयूसीएन रेड लिस्ट'],
    ['types-of-disasters-earthquakes-floods-cyclones-tsunamis', 'Types of Disasters: Earthquakes, Floods, Cyclones and Tsunamis', 'आपदाओं के प्रकार: भूकंप, बाढ़, चक्रवात और सुनामी']
].map(([key, titleEn, titleHi]) => ({
    key,
    titleEn,
    titleHi,
    breadEn: titleEn,
    breadHi: titleHi,
    descEn: `Comprehensive UPSSSC Lower Mains Environment study guide covering ${titleEn.toLowerCase()}, exam facts, India/UP context, PYQ-style practice and timed test questions.`,
    descHi: `${titleHi} पर आधारित यूपीएसएसएससी लोअर मेन्स पर्यावरण की विस्तृत अध्ययन सामग्री, परीक्षा तथ्य, भारत/उत्तर प्रदेश संदर्भ, अभ्यास प्रश्न और समयबद्ध टेस्ट।`
}));

function pageShell(topic, theoryHtml, practiceHtml, pyqHtml, testHtml, testDataJSON) {
    return `<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${topic.titleEn} - UPSSSC Lower Mains Environment</title>

    <!-- CSS Dependencies -->
    <link
        href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700;800&family=Inter:wght@400;500;600;700&display=swap"
        rel="stylesheet">
    <link rel="stylesheet" href="/assets/vendor/fontawesome/css/all.min.css?v=7441465c">
    <link rel="stylesheet" href="/assets/css/main.min.css?v=05feb74c">
    <link rel="stylesheet" href="/assets/css/improved-ui.min.css?v=c323837a">
    <link rel="stylesheet" href="/assets/css/topic-details.min.css?v=7bf51abb">
    <link rel="stylesheet" href="/assets/css/upsssc-lower.min.css?v=9d684fc1">
</head>

<body>
    <div class="container">
        <div class="top-controls">
            <button class="lang-toggle-btn" onclick="toggleLang()">A/अ</button>
        </div>

        <div class="breadcrumbs">
            <div class="breadcrumbs-path">
                <a href="../../index.html">Syllabus</a>
                <i class="fas fa-chevron-right"></i>
                <a href="../../index.html#environment">Environment</a>
                <i class="fas fa-chevron-right"></i>
                <span class="lang-en">${topic.breadEn}</span>
                <span class="lang-hi">${topic.breadHi}</span>
            </div>
        </div>

        <div class="topic-header">
            <h1>
                <span class="lang-en">${topic.titleEn}</span>
                <span class="lang-hi">${topic.titleHi}</span>
            </h1>
            <p>
                <span class="lang-en">${topic.descEn}</span>
                <span class="lang-hi">${topic.descHi}</span>
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
                <span class="lang-en">UP Gov PYQs</span>
                <span class="lang-hi">यूपी सरकार PYQs</span>
            </button>
            <button class="sub-nav-item" data-tab="test" onclick="switchTab('test')">
                <span class="lang-en">15-Q Test</span>
                <span class="lang-hi">15-प्रश्न टेस्ट</span>
            </button>
        </div>

        <div class="topic-content">

            <div id="tab-theory" class="tab-content" style="display:block">
${theoryHtml}
                <div class="next-tab-btn-container">
                    <button class="next-tab-btn" data-tab="practice" onclick="switchTab('practice')">
                        <span class="lang-en">Next: Practice Questions</span>
                        <span class="lang-hi">अगला: अभ्यास प्रश्न</span>
                        <i class="fas fa-arrow-right"></i>
                    </button>
                </div>
            </div>

            <div id="tab-practice" class="tab-content" style="display:none">
                <div class="info-banner">
                    <span class="lang-en">Practice all 30 questions. Each question has an instant answer reveal.</span>
                    <span class="lang-hi">सभी 30 प्रश्नों का अभ्यास करें। प्रत्येक प्रश्न में तत्काल उत्तर देखें।</span>
                </div>
${practiceHtml}
                <div class="next-tab-btn-container">
                    <button class="next-tab-btn" data-tab="pyqs" onclick="switchTab('pyqs')">
                        <span class="lang-en">Next: UP Gov PYQs</span>
                        <span class="lang-hi">अगला: यूपी सरकार PYQs</span>
                        <i class="fas fa-arrow-right"></i>
                    </button>
                </div>
            </div>

            <div id="tab-pyqs" class="tab-content" style="display:none">
                <div class="info-banner">
                    <span class="lang-en">Previous Year Questions from UP Government exams (UPSSSC, UP PCS, UP Lower PCS).</span>
                    <span class="lang-hi">यूपी सरकार परीक्षाओं के पिछले वर्ष के प्रश्न (UPSSSC, UP PCS, UP Lower PCS)।</span>
                </div>
${pyqHtml}
                <div class="next-tab-btn-container">
                    <button class="next-tab-btn" data-tab="test" onclick="switchTab('test')">
                        <span class="lang-en">Next: 15-Q Test</span>
                        <span class="lang-hi">अगला: 15-प्रश्न टेस्ट</span>
                        <i class="fas fa-arrow-right"></i>
                    </button>
                </div>
            </div>

            <div id="tab-test" class="tab-content" style="display:none">
                <div class="test-start-scr" id="test-start">
                    <h3>
                        <span class="lang-en">15-Question Timed Test</span>
                        <span class="lang-hi">15-प्रश्न समयबद्ध टेस्ट</span>
                    </h3>
                    <p>
                        <span class="lang-en">Test your knowledge with 15 curated questions. Time limit: 15 minutes.</span>
                        <span class="lang-hi">15 चयनित प्रश्नों के साथ अपना ज्ञान परखें। समय सीमा: 15 मिनट।</span>
                    </p>
                    <div class="tinfo-grid">
                        <div class="tinfo-card"><div class="tinfo-num">15</div><div class="tinfo-lbl"><span class="lang-en">Questions</span><span class="lang-hi">प्रश्न</span></div></div>
                        <div class="tinfo-card"><div class="tinfo-num">15</div><div class="tinfo-lbl"><span class="lang-en">Minutes</span><span class="lang-hi">मिनट</span></div></div>
                        <div class="tinfo-card"><div class="tinfo-num">4</div><div class="tinfo-lbl"><span class="lang-en">Options each</span><span class="lang-hi">प्रत्येक विकल्प</span></div></div>
                    </div>
                    <button class="start-test-btn" onclick="startTest()">
                        <span class="lang-en">Start Test</span>
                        <span class="lang-hi">टेस्ट शुरू करें</span>
                    </button>
                </div>
                <div id="test-area" style="display:none">
                    <div class="test-hdr">
                        <div><span class="lang-en">Time Left</span><span class="lang-hi">शेष समय</span></div>
                        <div class="test-tmr" id="test-timer">15:00</div>
                    </div>
                    <div class="test-prog-bar"><div class="test-prog-fill" id="test-prog" style="width:0%"></div></div>
                    <div id="test-questions">
${testHtml}
                    </div>
                    <div style="text-align:center;margin:24px 0">
                        <button onclick="submitTest()" id="submit-btn" style="padding:13px 38px;background:linear-gradient(135deg,#27ae60,#2ecc71);color:white;border:none;border-radius:30px;font-size:1.1rem;font-weight:700;cursor:pointer;box-shadow:0 8px 20px rgba(39,174,96,0.4);">
                            <i class="fas fa-paper-plane"></i>
                            <span class="lang-en">Submit Test</span><span class="lang-hi">टेस्ट जमा करें</span>
                        </button>
                    </div>
                </div>
                <div class="test-result" id="test-result">
                    <div style="font-size:1.3rem"><i class="fas fa-trophy"></i> <span class="lang-en">Test Complete!</span><span class="lang-hi">टेस्ट पूर्ण!</span></div>
                    <div class="result-score" id="res-score">0/15</div>
                    <div id="res-label" style="font-size:1rem;opacity:0.9;margin-bottom:5px"></div>
                    <div class="grade-bdg" id="res-grade"></div>
                    <div style="margin-top:18px">
                        <button class="tact-btn" onclick="retakeTest()" style="background:#059669;color:white"><i class="fas fa-redo"></i> <span class="lang-en">Retake</span><span class="lang-hi">पुनः दें</span></button>
                        <button class="tact-btn" data-tab="practice" onclick="switchTab('practice')" style="background:white;color:#059669"><i class="fas fa-book"></i> <span class="lang-en">Practice More</span><span class="lang-hi">और अभ्यास करें</span></button>
                    </div>
                </div>
            </div>

        </div>
    </div>

            <script>
                window.upssscTestData = ${testDataJSON};
            </script>
            <script src="/assets/js/upsssc-lower.min.js?v=117a746d"></script>
            <script src="/assets/js/main.min.js?v=86340191"></script>
</body>

</html>`;
}

function buildPrompt(topic) {
    return `You are an expert UPSSSC Lower Mains exam content creator for Environment.
Generate complete, exam-focused content for: "${topic.titleEn}" (${topic.titleHi})

IMPORTANT: Return ONLY valid JSON. No markdown, no explanation. Just the JSON object.

Generate this exact JSON structure:
{
  "theory": "<HTML string with 6-8 card-premium divs>",
  "practiceQs": [<array of exactly 30 MCQ objects>],
  "pyqs": [<array of exactly 30 PYQ objects>],
  "testQs": [<array of exactly 15 MCQ objects>]
}

THEORY HTML RULES:
- Use these exact CSS classes (already defined): card-premium, card-title, theory-heading, theory-para, theory-highlight, theory-overflow-mb, tab-active-bar, theory-section-sep
- Each card has: <div class="card-premium"><h3 class="card-title">...</h3>...</div>
- Use <span class="lang-en">English text</span> and <span class="lang-hi">हिंदी पाठ</span> for ALL text
- Use <h4 class="lang-en theory-heading">heading</h4> and <h4 class="lang-hi theory-heading">शीर्षक</h4>
- Use tables with thead/tbody, class="tab-active-bar" on header rows
- Highlight key facts with <div class="theory-highlight">
- Make content DEEPLY detailed and exam-specific for UPSSSC Lower Mains, UP PCS level
- Include: concept explanation, key terms, India and Uttar Pradesh context, comparison table, exam traps, important acts/institutions/protocols if relevant, revision highlights

PRACTICE QUESTION RULES (exactly 30 questions):
Each object: { "qEn": "English question", "qHi": "हिंदी प्रश्न", "opts": [{"en":"A option","hi":"A विकल्प"},{"en":"B","hi":"B"},{"en":"C","hi":"C"},{"en":"D","hi":"D"}], "ans": 0, "solEn": "Explanation in English", "solHi": "हिंदी में व्याख्या" }
- ans is 0-based index (0=A, 1=B, 2=C, 3=D)
- Include mix of: factual, match-the-column, multi-statement True/False type
- All questions must be relevant to UPSSSC Lower Mains syllabus

PYQ RULES (exactly 30 questions):
Each object: { "qEn": "...", "qHi": "...", "opts": [...], "ans": 0, "year": "UP PCS 2019", "solEn": "...", "solHi": "..." }
- Use realistic UP exam years: UP PCS 2015-2023, UPSSSC 2016-2023, UP Lower PCS 2018-2022
- Questions must be realistic past-exam style

TEST QUESTION RULES (exactly 15 questions - different from practice):
Each object: { "qEn": "...", "qHi": "...", "opts": [{"en":"...","hi":"..."},{"en":"...","hi":"..."},{"en":"...","hi":"..."},{"en":"...","hi":"..."}], "ans": "A", "solEn": "...", "solHi": "..." }
- ans is "A", "B", "C", or "D" (letter, not number)
- These questions should be different from practice questions

Focus on: stable facts, concepts, causes, effects, legal/institutional points, exam traps, India/UP context. Avoid unsupported current statistics.`;
}

function buildPracticeHtml(qs) {
    const letters = ['A', 'B', 'C', 'D'];
    return qs.map((q, i) => {
        const opts = q.opts.map((o, j) => `
                    <label class="opt-label">
                        <input type="radio" class="opt-radio" name="q${i}" value="${letters[j]}">
                        <span class="lang-en"><b>${letters[j]}.</b> ${o.en}</span>
                        <span class="lang-hi"><b>${letters[j]}.</b> ${o.hi}</span>
                    </label>`).join('');
        return `
                <div class="practice-question-card">
                    <div class="q-row">
                        <div class="q-num-badge">${i + 1}</div>
                        <div class="q-body">
                            <p class="q-text lang-en">${q.qEn}</p>
                            <p class="q-text lang-hi">${q.qHi}</p>
                            <div class="q-options">${opts}
                            </div>
                            <details class="solution-details">
                                <summary class="lang-en">Show Answer</summary>
                                <summary class="lang-hi">उत्तर देखें</summary>
                                <p class="solution-correct lang-en">✔ Correct: ${letters[q.ans]}</p>
                                <p class="solution-correct lang-hi">✔ सही उत्तर: ${letters[q.ans]}</p>
                                <p class="lang-en">${q.solEn}</p>
                                <p class="lang-hi">${q.solHi}</p>
                            </details>
                        </div>
                    </div>
                </div>`;
    }).join('');
}

function buildPyqHtml(qs) {
    const letters = ['A', 'B', 'C', 'D'];
    return qs.map((q, i) => {
        const opts = q.opts.map((o, j) => `
                    <label class="opt-label">
                        <input type="radio" class="opt-radio" name="pyq${i}" value="${letters[j]}">
                        <span class="lang-en"><b>${letters[j]}.</b> ${o.en}</span>
                        <span class="lang-hi"><b>${letters[j]}.</b> ${o.hi}</span>
                    </label>`).join('');
        return `
                <div class="practice-question-card">
                    <div class="q-row">
                        <div class="q-num-badge">${i + 1}</div>
                        <div class="q-body">
                            <span class="badge-pyq lang-en">${q.year} (UP Exam)</span>
                            <span class="badge-pyq lang-hi">${q.year} (यूपी परीक्षा)</span>
                            <p class="q-text lang-en">${q.qEn}</p>
                            <p class="q-text lang-hi">${q.qHi}</p>
                            <div class="q-options">${opts}
                            </div>
                            <details class="solution-details">
                                <summary class="lang-en">Show Answer</summary>
                                <summary class="lang-hi">उत्तर देखें</summary>
                                <p class="solution-correct lang-en">✔ Correct: ${letters[q.ans]}</p>
                                <p class="solution-correct lang-hi">✔ सही उत्तर: ${letters[q.ans]}</p>
                                <p class="lang-en">${q.solEn}</p>
                                <p class="lang-hi">${q.solHi}</p>
                            </details>
                        </div>
                    </div>
                </div>`;
    }).join('');
}

function buildTestHtml(qs) {
    return qs.map((q, i) => {
        const opts = q.opts.map((o, j) => {
            const letters = ['A', 'B', 'C', 'D'];
            return `\n                                <div class="test-opt" data-qi="${i}" data-ch="${letters[j]}" onclick="selOpt(this)"><span class="opt-ltr">${letters[j]}</span><span class="lang-en">${o.en}</span><span class="lang-hi">${o.hi}</span></div>`;
        }).join('');
        return `
                        <div class="test-qblock" id="tq-${i}">
                            <p class="test-qtext"><span class="test-qnum">Q${i + 1}</span><span style="display:block;margin-top:6px"><span class="lang-en">${q.qEn}</span><span class="lang-hi">${q.qHi}</span></span></p>
                            <div class="test-opts-grid">${opts}
                            </div><input type="hidden" id="tans-${i}" value="${q.ans}"><input type="hidden" id="tsel-${i}" value="">
                        </div>`;
    }).join('');
}

// ─── Model pool: gemini-3.5-flash produces perfect 30/30/15 content but has tight RPM limit ──
const MODEL_POOL = [
    'gemini-3.5-flash',
];

let modelIndex = 0;

async function generateTopic(topic) {
    console.log(`\n⟳ Generating: ${topic.titleEn}...`);

    const prompt = buildPrompt(topic);

    let raw;
    const MAX_RETRIES = 20;
    const BASE_DELAY = 15000;

    for (let attempt = 0; attempt < MAX_RETRIES; attempt++) {
        const model = MODEL_POOL[attempt % MODEL_POOL.length];
        try {
            console.log(`  → Using model: ${model} (attempt ${attempt + 1}/${MAX_RETRIES})`);
            const response = await ai.models.generateContent({
                model,
                contents: prompt,
                config: {
                    thinkingConfig: { thinkingBudget: 0 },
                    temperature: 0.7,
                    maxOutputTokens: 65536
                }
            });
            raw = response.text;
            console.log(`  ✓ Got response from ${model}`);
            modelIndex = (attempt + 1) % MODEL_POOL.length;
            break;
        } catch (err) {
            const is503 = err.message && (
                err.message.includes('503') ||
                err.message.includes('UNAVAILABLE') ||
                err.message.includes('high demand') ||
                err.message.includes('overloaded')
            );
            if (is503 && attempt < MAX_RETRIES - 1) {
                const delay = BASE_DELAY * (attempt + 1);
                console.log(`  ⚠ ${model} 503 (attempt ${attempt + 1}) → switching model in ${delay / 1000}s...`);
                await new Promise(r => setTimeout(r, delay));
            } else {
                console.error(`  ✗ All models failed for ${topic.key}:`, err.message);
                throw err;
            }
        }
    }

    let jsonStr = raw.trim();
    if (jsonStr.startsWith('```')) {
        jsonStr = jsonStr.replace(/^```(?:json)?\n?/, '').replace(/\n?```$/, '');
    }

    let data;
    try {
        data = JSON.parse(jsonStr);
    } catch (e) {
        const match = jsonStr.match(/\{[\s\S]*\}/);
        if (!match) throw new Error('No JSON object found in response');
        try { data = JSON.parse(match[0]); }
        catch (e2) {
            console.error(`  ✗ JSON parse failed for ${topic.key}`);
            console.error('  Raw (first 500):', jsonStr.substring(0, 500));
            throw e2;
        }
    }

    // Count actual questions generated
    const practiceCount = (data.practiceQs || []).length;
    const pyqCount = (data.pyqs || []).length;
    const testCount = (data.testQs || []).length;
    console.log(`  📊 Questions: ${practiceCount} practice, ${pyqCount} PYQs, ${testCount} test`);

    const testDataArr = (data.testQs || []).map(q => ({
        ans: q.ans,
        solEn: q.solEn,
        solHi: q.solHi
    }));

    const theoryHtml = data.theory || '';
    const practiceHtml = buildPracticeHtml(data.practiceQs || []);
    const pyqHtml = buildPyqHtml(data.pyqs || []);
    const testHtml = buildTestHtml(data.testQs || []);
    const testDataJSON = JSON.stringify(testDataArr);

    const html = pageShell(topic, theoryHtml, practiceHtml, pyqHtml, testHtml, testDataJSON);

    const outDir = path.join(BASE, topic.key);
    if (!fs.existsSync(outDir)) fs.mkdirSync(outDir, { recursive: true });
    const outFile = path.join(outDir, 'index.html');
    fs.writeFileSync(outFile, html, 'utf8');

    const sizeKB = Math.round(html.length / 1024);
    console.log(`  ✓ Written: ${topic.key}/index.html (${sizeKB} KB)`);
}

async function main() {
    console.log('=== UPSSSC Lower Mains Environment Page Generator ===');
    console.log(`Using Gemini API Key: ${API_KEY ? API_KEY.substring(0, 10) + '...' : 'NOT FOUND'}`);

    if (!API_KEY) throw new Error('GEMINI_API_KEY not found in .env');

    const retryKeys = process.env.RETRY_KEYS ? process.env.RETRY_KEYS.split(',').map(k => k.trim()) : null;
    const topicsToRun = retryKeys ? TOPICS.filter(t => retryKeys.includes(t.key)) : TOPICS;

    if (retryKeys) console.log(`Retrying only: ${retryKeys.join(', ')}`);
    console.log(`Topics to generate: ${topicsToRun.length}`);

    const failed = [];
    for (const topic of topicsToRun) {
        console.log(`\n⏳ Waiting 60s before next topic to respect gemini-3.5-flash RPM limits...`);
        await new Promise(r => setTimeout(r, 60000));
        try {
            await generateTopic(topic);
        } catch (err) {
            console.error(`  ✗ Failed: ${topic.key} — ${err.message}`);
            failed.push(topic.key);
        }
    }

    console.log('\n=== Generation Complete ===');
    if (failed.length > 0) {
        console.log(`Failed topics (${failed.length}): ${failed.join(', ')}`);
        console.log(`Retry with: RETRY_KEYS=${failed.join(',')} node scripts/gen_environment_pages.js`);
    } else {
        console.log('All topics generated successfully! ✓');
    }
}

main().catch(console.error);