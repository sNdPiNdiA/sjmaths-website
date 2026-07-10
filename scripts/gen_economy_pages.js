/**
 * UPSSSC Lower Mains Economy Page Generator
 * Uses Gemini API to generate detailed content for 18 economy topics
 * Run: node scripts/gen_economy_pages.js
 */

require('dotenv').config();
const { GoogleGenAI } = require('@google/genai');
const fs = require('fs');
const path = require('path');

const API_KEY = process.env.GEMINI_API_KEY;
const ai = new GoogleGenAI({ apiKey: API_KEY });

const BASE = path.join(__dirname, '..', 'upsssc-lower-mains', 'economy');

// Topic definitions
const TOPICS = [
    {
        key: 'economic-planning-in-india',
        titleEn: 'Economic Planning in India',
        titleHi: 'भारत में आर्थिक नियोजन',
        breadEn: 'Economic Planning',
        breadHi: 'आर्थिक नियोजन',
        descEn: 'Comprehensive study guide covering economic planning in India, Five-Year Plans, NITI Aayog, and planning objectives for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए भारत में आर्थिक नियोजन, पंचवर्षीय योजनाएं, नीति आयोग और नियोजन उद्देश्यों को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Economic Planning in India" (भारत में आर्थिक नियोजन).`
    },
    {
        key: 'objectives-and-achievements-of-economic-planning',
        titleEn: 'Objectives and Achievements of Economic Planning',
        titleHi: 'आर्थिक नियोजन के उद्देश्य और उपलब्धियां',
        breadEn: 'Objectives & Achievements',
        breadHi: 'उद्देश्य और उपलब्धियां',
        descEn: 'Comprehensive study guide covering objectives, achievements, and failures of economic planning in India for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए भारत में आर्थिक नियोजन के उद्देश्यों, उपलब्धियों और विफलताओं को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Objectives and Achievements of Economic Planning" (आर्थिक नियोजन के उद्देश्य और उपलब्धियां).`
    },
    {
        key: 'role-of-niti-aayog',
        titleEn: 'Role of NITI Aayog',
        titleHi: 'नीति आयोग की भूमिका',
        breadEn: 'Role of NITI Aayog',
        breadHi: 'नीति आयोग की भूमिका',
        descEn: 'Comprehensive study guide covering NITI Aayog\'s formation, structure, functions, and role in policy formulation for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए नीति आयोग के गठन, संरचना, कार्यों और नीति निर्माण में भूमिका को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Role of NITI Aayog" (नीति आयोग की भूमिका).`
    },
    {
        key: 'development-of-agriculture-in-india',
        titleEn: 'Development of Agriculture in India',
        titleHi: 'भारत में कृषि का विकास',
        breadEn: 'Agriculture Development',
        breadHi: 'कृषि विकास',
        descEn: 'Comprehensive study guide covering agricultural development, Green Revolution, land reforms, and agricultural policies for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए कृषि विकास, हरित क्रांति, भूमि सुधार और कृषि नीतियों को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Development of Agriculture in India" (भारत में कृषि का विकास).`
    },
    {
        key: 'land-reforms-in-india-after-independence',
        titleEn: 'Land Reforms in India After Independence',
        titleHi: 'स्वतंत्रता के बाद भारत में भूमि सुधार',
        breadEn: 'Land Reforms',
        breadHi: 'भूमि सुधार',
        descEn: 'Comprehensive study guide covering land reforms, abolition of zamindari, tenancy reforms, land ceiling, and consolidation for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए भूमि सुधार, जमींदारी उन्मूलन, काश्तकारी सुधार, भूमि सीमा और चकबंदी को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Land Reforms in India After Independence" (स्वतंत्रता के बाद भारत में भूमि सुधार).`
    },
    {
        key: 'development-of-industry-in-india',
        titleEn: 'Development of Industry in India',
        titleHi: 'भारत में उद्योग का विकास',
        breadEn: 'Industrial Development',
        breadHi: 'औद्योगिक विकास',
        descEn: 'Comprehensive study guide covering industrial development, Industrial Policy Resolutions, public sector, and industrial growth for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए औद्योगिक विकास, औद्योगिक नीति प्रस्ताव, सार्वजनिक क्षेत्र और औद्योगिक वृद्धि को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Development of Industry in India" (भारत में उद्योग का विकास).`
    },
    {
        key: 'changes-in-industrial-policy',
        titleEn: 'Changes in Industrial Policy',
        titleHi: 'औद्योगिक नीति में परिवर्तन',
        breadEn: 'Industrial Policy Changes',
        breadHi: 'औद्योगिक नीति में बदलाव',
        descEn: 'Comprehensive study guide covering changes in industrial policy, liberalization, privatization, and globalization reforms for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए औद्योगिक नीति में बदलाव, उदारीकरण, निजीकरण और वैश्वीकरण सुधारों को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Changes in Industrial Policy" (औद्योगिक नीति में परिवर्तन).`
    },
    {
        key: 'impact-of-industrial-policy-on-industrial-development',
        titleEn: 'Impact of Industrial Policy on Industrial Development',
        titleHi: 'औद्योगिक विकास पर औद्योगिक नीति का प्रभाव',
        breadEn: 'Industrial Policy Impact',
        breadHi: 'औद्योगिक नीति का प्रभाव',
        descEn: 'Comprehensive study guide covering the impact of industrial policies on India\'s industrial development and economic growth for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए भारत के औद्योगिक विकास और आर्थिक वृद्धि पर औद्योगिक नीतियों के प्रभाव को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Impact of Industrial Policy on Industrial Development" (औद्योगिक विकास पर औद्योगिक नीति का प्रभाव).`
    },
    {
        key: 'development-of-trade-commerce-in-india',
        titleEn: 'Development of Trade & Commerce in India',
        titleHi: 'भारत में व्यापार और वाणिज्य का विकास',
        breadEn: 'Trade & Commerce',
        breadHi: 'व्यापार और वाणिज्य',
        descEn: 'Comprehensive study guide covering internal and external trade, balance of payments, trade policies, and WTO for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए आंतरिक और बाह्य व्यापार, भुगतान संतुलन, व्यापार नीतियां और WTO को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Development of Trade and Commerce in India" (भारत में व्यापार और वाणिज्य का विकास).`
    },
    {
        key: 'effects-of-globalization-and-liberalization-in-india',
        titleEn: 'Effects of Globalization and Liberalization in India',
        titleHi: 'भारत में वैश्वीकरण और उदारीकरण के प्रभाव',
        breadEn: 'Globalization & Liberalization',
        breadHi: 'वैश्वीकरण और उदारीकरण',
        descEn: 'Comprehensive study guide covering the effects of 1991 economic reforms, globalization, and liberalization on Indian economy for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए भारतीय अर्थव्यवस्था पर 1991 के आर्थिक सुधारों, वैश्वीकरण और उदारीकरण के प्रभावों को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Effects of Globalization and Liberalization in India" (भारत में वैश्वीकरण और उदारीकरण के प्रभाव).`
    },
    {
        key: 'financial-system',
        titleEn: 'Financial System',
        titleHi: 'वित्तीय प्रणाली',
        breadEn: 'Financial System',
        breadHi: 'वित्तीय प्रणाली',
        descEn: 'Comprehensive study guide covering Indian financial system, banks, RBI, money market, capital market, and financial institutions for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए भारतीय वित्तीय प्रणाली, बैंक, RBI, मुद्रा बाजार, पूंजी बाजार और वित्तीय संस्थानों को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Financial System" (वित्तीय प्रणाली).`
    },
    {
        key: 'components-of-government-budget',
        titleEn: 'Components of Government Budget',
        titleHi: 'सरकारी बजट के घटक',
        breadEn: 'Government Budget',
        breadHi: 'सरकारी बजट',
        descEn: 'Comprehensive study guide covering government budget components, revenue and capital accounts, fiscal deficit, and budget process for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए सरकारी बजट घटकों, राजस्व और पूंजी खाते, राजकोषीय घाटा और बजट प्रक्रिया को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Components of Government Budget" (सरकारी बजट के घटक).`
    },
    {
        key: 'sustainable-development-goals-sdgs',
        titleEn: 'Sustainable Development Goals (SDGs)',
        titleHi: 'सतत विकास लक्ष्य (SDGs)',
        breadEn: 'Sustainable Development Goals',
        breadHi: 'सतत विकास लक्ष्य',
        descEn: 'Comprehensive study guide covering SDGs, their targets, indicators, India\'s progress, and global initiatives for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए SDGs, उनके लक्ष्यों, संकेतकों, भारत की प्रगति और वैश्विक पहलों को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Sustainable Development Goals SDGs" (सतत विकास लक्ष्य).`
    },
    {
        key: 'infrastructure-roads',
        titleEn: 'Infrastructure: Roads',
        titleHi: 'बुनियादी ढांचा: सड़कें',
        breadEn: 'Road Infrastructure',
        breadHi: 'सड़क बुनियादी ढांचा',
        descEn: 'Comprehensive study guide covering road infrastructure in India, NHDP, PMGSY, Bharatmala, and road transport for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए भारत में सड़क बुनियादी ढांचा, NHDP, PMGSY, भारतमाला और सड़क परिवहन को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Infrastructure Roads" (बुनियादी ढांचा: सड़कें).`
    },
    {
        key: 'infrastructure-railways',
        titleEn: 'Infrastructure: Railways',
        titleHi: 'बुनियादी ढांचा: रेलवे',
        breadEn: 'Railway Infrastructure',
        breadHi: 'रेलवे बुनियादी ढांचा',
        descEn: 'Comprehensive study guide covering Indian Railways, modernization, high-speed rail, Dedicated Freight Corridors, and railway reforms for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए भारतीय रेलवे, आधुनिकीकरण, हाई-स्पीड रेल, समर्पित फ्रेट कॉरिडोर और रेलवे सुधारों को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Infrastructure Railways" (बुनियादी ढांचा: रेलवे).`
    },
    {
        key: 'infrastructure-ports',
        titleEn: 'Infrastructure: Ports',
        titleHi: 'बुनियादी ढांचा: बंदरगाह',
        breadEn: 'Port Infrastructure',
        breadHi: 'बंदरगाह बुनियादी ढांचा',
        descEn: 'Comprehensive study guide covering major ports, port modernization, Sagarmala project, and maritime trade for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए प्रमुख बंदरगाहों, बंदरगाह आधुनिकीकरण, सागरमाला परियोजना और समुद्री व्यापार को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Infrastructure Ports" (बुनियादी ढांचा: बंदरगाह).`
    },
    {
        key: 'infrastructure-airports',
        titleEn: 'Infrastructure: Airports',
        titleHi: 'बुनियादी ढांचा: हवाई अड्डे',
        breadEn: 'Airport Infrastructure',
        breadHi: 'हवाई अड्डा बुनियादी ढांचा',
        descEn: 'Comprehensive study guide covering airport infrastructure, UDAN scheme, AAI, and civil aviation in India for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए हवाई अड्डा बुनियादी ढांचा, उड़ान योजना, AAI और भारत में नागरिक उड्डयन को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Infrastructure Airports" (बुनियादी ढांचा: हवाई अड्डे).`
    },
    {
        key: 'infrastructure-power',
        titleEn: 'Infrastructure: Power',
        titleHi: 'बुनियादी ढांचा: ऊर्जा',
        breadEn: 'Power Infrastructure',
        breadHi: 'ऊर्जा बुनियादी ढांचा',
        descEn: 'Comprehensive study guide covering power infrastructure, energy sources, renewable energy, power sector reforms for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए ऊर्जा बुनियादी ढांचा, ऊर्जा स्रोत, नवीकरणीय ऊर्जा, बिजली क्षेत्र सुधारों को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Infrastructure Power" (बुनियादी ढांचा: ऊर्जा).`
    }
];

// ─── HTML Template Functions ──────────────────────────────────────────────────

function pageShell(topic, theoryHtml, practiceHtml, pyqHtml, testHtml, testDataJSON) {
    return `<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${topic.titleEn} - UPSSSC Lower Mains</title>

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
                <a href="../../index.html#economy">Economy</a>
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
                    <span class="lang-hi">सभी 30 प्रश्नों का अभ्यास करें। प्रत्येक प्रश्न में तत्काल उत्तर।</span>
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
                    <span class="lang-hi">यूपी सरकार परीक्षाओं के पिछले वर्ष के प्रश्न (UPSSSC, UP PCS, UP लोअर PCS)।</span>
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
                        <button class="tact-btn" onclick="retakeTest()" style="background:#8e44ad;color:white"><i class="fas fa-redo"></i> <span class="lang-en">Retake</span><span class="lang-hi">पुनः दें</span></button>
                        <button class="tact-btn" data-tab="practice" onclick="switchTab('practice')" style="background:white;color:#8e44ad"><i class="fas fa-book"></i> <span class="lang-en">Practice More</span><span class="lang-hi">और अभ्यास करें</span></button>
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

// ─── Gemini Prompt Builder ────────────────────────────────────────────────────

function buildPrompt(topic) {
    return `You are an expert UPSSSC Lower Mains exam content creator for Indian Economy. 
Generate complete, exam-focused content for: "${topic.titleEn}" (${topic.titleHi})

IMPORTANT: Return ONLY valid JSON. No markdown, no explanation. Just the JSON object.

Generate this exact JSON structure:
{
  "theory": "<HTML string with 5-6 card-premium divs>",
  "practiceQs": [<array of exactly 30 MCQ objects>],
  "pyqs": [<array of exactly 10 PYQ objects>],
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

PRACTICE QUESTION RULES (30 questions):
Each object: { "qEn": "English question", "qHi": "हिंदी प्रश्न", "opts": [{"en":"A option","hi":"A विकल्प"},{"en":"B","hi":"B"},{"en":"C","hi":"C"},{"en":"D","hi":"D"}], "ans": 0, "solEn": "Explanation in English", "solHi": "हिंदी में व्याख्या" }
- ans is 0-based index (0=A, 1=B, 2=C, 3=D)
- Include mix of: factual, match-the-column, multi-statement True/False type
- All questions must be relevant to UPSSSC Lower Mains syllabus

PYQ RULES (10 questions):
Each object: { "qEn": "...", "qHi": "...", "opts": [...], "ans": 0, "year": "UP PCS 2019", "solEn": "...", "solHi": "..." }
- Use realistic UP exam years: UP PCS 2015-2023, UPSSSC 2016-2023, UP Lower PCS 2018-2022
- Questions must be realistic past-exam style

TEST QUESTION RULES (15 questions - different from practice):
Each object: { "qEn": "...", "qHi": "...", "opts": [{"en":"...","hi":"..."},{"en":"...","hi":"..."},{"en":"...","hi":"..."},{"en":"...","hi":"..."}], "ans": "A", "solEn": "...", "solHi": "..." }
- ans is "A", "B", "C", or "D" (letter, not number)
- These questions should be different from practice questions

Topic: ${topic.prompt}
Focus on: facts most commonly asked in UP state government exams, key economic concepts, policies, data.`;
}

// ─── HTML builders from JSON data ────────────────────────────────────────────

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

// ─── Model pool ──────────────────────────────────────────────────────────────
const MODEL_POOL = [
    'gemini-3.1-flash-lite',
    'gemini-2.0-flash',
    'gemini-1.5-flash',
];

// ─── Main Generator ───────────────────────────────────────────────────────────

async function generateTopic(topic) {
    console.log(`\n⟳ Generating: ${topic.titleEn}...`);

    const prompt = buildPrompt(topic);

    let raw;
    const MAX_RETRIES = MODEL_POOL.length * 2;
    const BASE_DELAY = 5000;

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
            break;
        } catch (err) {
            const msg = err.message || '';
            const isRetryable = (
                msg.includes('503') ||
                msg.includes('UNAVAILABLE') ||
                msg.includes('high demand') ||
                msg.includes('overloaded') ||
                msg.includes('404') ||
                msg.includes('NOT_FOUND') ||
                msg.includes('not found for API') ||
                msg.includes('429') ||
                msg.includes('RESOURCE_EXHAUSTED') ||
                msg.includes('quota')
            );
            if (isRetryable && attempt < MAX_RETRIES - 1) {
                const is503 = msg.includes('503') || msg.includes('UNAVAILABLE');
                const delay = is503 ? BASE_DELAY * (attempt + 1) : 2000;
                console.log(`  ⚠ ${model} error (attempt ${attempt + 1}) → switching model in ${delay / 1000}s...`);
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
        if (match) {
            try { data = JSON.parse(match[0]); }
            catch (e2) {
                console.error(`  ✗ JSON parse failed for ${topic.key}`);
                console.error('  Raw (first 500):', jsonStr.substring(0, 500));
                throw e2;
            }
        } else {
            throw e;
        }
    }

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
    console.log('=== UPSSSC Lower Mains Economy Page Generator ===');
    console.log(`Using Gemini API Key: ${API_KEY ? API_KEY.substring(0, 10) + '...' : 'NOT FOUND'}`);

    if (!API_KEY) {
        console.error('ERROR: GEMINI_API_KEY not found in .env');
        process.exit(1);
    }

    const retryKeys = process.env.RETRY_KEYS ? process.env.RETRY_KEYS.split(',').map(k => k.trim()) : null;
    const topicsToRun = retryKeys ? TOPICS.filter(t => retryKeys.includes(t.key)) : TOPICS;

    if (retryKeys) console.log(`Retrying only: ${retryKeys.join(', ')}`);
    console.log(`Topics to generate: ${topicsToRun.length}`);

    const failed = [];
    for (const topic of topicsToRun) {
        try {
            await generateTopic(topic);
            await new Promise(r => setTimeout(r, 3000));
        } catch (err) {
            console.error(`  ✗ Failed: ${topic.key} — ${err.message}`);
            failed.push(topic.key);
        }
    }

    console.log('\n=== Generation Complete ===');
    if (failed.length > 0) {
        console.log(`Failed topics (${failed.length}): ${failed.join(', ')}`);
        console.log(`Retry with: RETRY_KEYS=${failed.join(',')} node scripts/gen_economy_pages.js`);
    } else {
        console.log('All topics generated successfully! ✓');
    }
}

main().catch(console.error);