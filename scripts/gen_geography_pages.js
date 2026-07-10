/**
 * UPSSSC Lower Mains Geography Page Generator
 * Uses Gemini API to generate detailed content for 19 geography topics
 * Run: node scripts/gen_geography_pages.js
 */

require('dotenv').config();
const { GoogleGenAI } = require('@google/genai');
const fs = require('fs');
const path = require('path');

const API_KEY = process.env.GEMINI_API_KEY;
const ai = new GoogleGenAI({ apiKey: API_KEY });

const BASE = path.join(__dirname, '..', 'upsssc-lower-mains', 'geography');

// Topic definitions
const TOPICS = [
    {
        key: 'physical-features-mountains-plains-plateaus-coasts-islands',
        titleEn: 'Physical Features of India',
        titleHi: 'भारत के भौतिक विशेषताएं',
        breadEn: 'Physical Features',
        breadHi: 'भौतिक विशेषताएं',
        descEn: 'Comprehensive study guide covering India\'s physical features - mountains, plains, plateaus, coasts, and islands for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए भारत के भौतिक विशेषताएं - पर्वत, मैदान, पठार, तट और द्वीपों को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Physical Features of India" (भारत के भौतिक विशेषताएं - पर्वत, मैदान, पठार, तट, द्वीप).`
    },
    {
        key: 'drainage-system-himalayan-peninsular-rivers',
        titleEn: 'Drainage System of India',
        titleHi: 'भारत के अपवाह तंत्र',
        breadEn: 'Drainage System',
        breadHi: 'अपवाह तंत्र',
        descEn: 'Comprehensive study guide covering Himalayan and Peninsular river systems, major rivers, and drainage patterns for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए हिमालयी और प्रायद्वीपीय नदी तंत्र, प्रमुख नदियां और अपवाह पैटर्न को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Drainage System of India" (भारत के अपवाह तंत्र - हिमालयी और प्रायद्वीपीय नदियां).`
    },
    {
        key: 'climate-seasons-monsoons',
        titleEn: 'Climate and Seasons of India',
        titleHi: 'भारत की जलवायु और ऋतुएं',
        breadEn: 'Climate & Seasons',
        breadHi: 'जलवायु और ऋतुएं',
        descEn: 'Comprehensive study guide covering Indian climate, monsoon patterns, seasons, and climatic factors for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए भारत की जलवायु, मानसून पैटर्न, ऋतुएं और जलवायु कारकों को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Climate and Seasons of India" (भारत की जलवायु और मानसून).`
    },
    {
        key: 'soils-natural-vegetation',
        titleEn: 'Soils and Natural Vegetation',
        titleHi: 'मृदा और प्राकृतिक वनस्पति',
        breadEn: 'Soils & Vegetation',
        breadHi: 'मृदा और वनस्पति',
        descEn: 'Comprehensive study guide covering Indian soil types, distribution, natural vegetation, and forest types for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए भारत की मृदा प्रकार, वितरण, प्राकृतिक वनस्पति और वन प्रकारों को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Soils and Natural Vegetation" (भारत की मृदाएं और प्राकृतिक वनस्पति).`
    },
    {
        key: 'economic-geography-minerals-energy-resources-industries',
        titleEn: 'Economic Geography of India',
        titleHi: 'भारत का आर्थिक भूगोल',
        breadEn: 'Economic Geography',
        breadHi: 'आर्थिक भूगोल',
        descEn: 'Comprehensive study guide covering minerals, energy resources, industries, and economic activities of India for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए भारत के खनिज, ऊर्जा संसाधन, उद्योग और आर्थिक गतिविधियों को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Economic Geography of India" (भारत का आर्थिक भूगोल - खनिज, ऊर्जा, उद्योग).`
    },
    {
        key: 'major-crops-cropping-patterns',
        titleEn: 'Major Crops and Cropping Patterns',
        titleHi: 'प्रमुख फसलें और फसल पैटर्न',
        breadEn: 'Major Crops',
        breadHi: 'प्रमुख फसलें',
        descEn: 'Comprehensive study guide covering major crops, cropping patterns, agricultural regions, and food crops of India for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए भारत की प्रमुख फसलें, फसल पैटर्न, कृषि क्षेत्र और खाद्य फसलें को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Major Crops and Cropping Patterns" (भारत की प्रमुख फसलें और फसल पैटर्न).`
    },
    {
        key: 'irrigation-farming-systems',
        titleEn: 'Irrigation and Farming Systems',
        titleHi: 'सिंचाई और कृषि प्रणालियाँ',
        breadEn: 'Irrigation & Farming',
        breadHi: 'सिंचाई और खेती',
        descEn: 'Comprehensive study guide covering irrigation methods, farming systems, and agricultural practices in India for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए भारत में सिंचाई विधियां, कृषि प्रणालियां और कृषिकरण प्रथाओं को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Irrigation and Farming Systems" (सिंचाई और कृषि प्रणालियाँ).`
    },
    {
        key: 'horticulture-fruits-vegetables-floriculture',
        titleEn: 'Horticulture',
        titleHi: 'बागवानी',
        breadEn: 'Horticulture',
        breadHi: 'बागवानी',
        descEn: 'Comprehensive study guide covering horticulture, fruits, vegetables, floriculture, and medicinal plants for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए बागवानी, फल, सब्जियां, पुष्प कृषि और औषधीय पौधों को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Horticulture" (बागवानी - फल, सब्जियां, पुष्प कृषि).`
    },
    {
        key: 'forestry-forest-produce',
        titleEn: 'Forestry and Forest Produce',
        titleHi: 'वानिकी और वन उत्पाद',
        breadEn: 'Forestry',
        breadHi: 'वानिकी',
        descEn: 'Comprehensive study guide covering forest types, forest resources, forest produce, and forestry programs for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए वन प्रकार, वन संसाधन, वन उत्पाद और वानिकी कार्यक्रमों को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Forestry and Forest Produce" (वानिकी और वन उत्पाद).`
    },
    {
        key: 'animal-husbandry-livestock-dairying-poultry-fisheries',
        titleEn: 'Animal Husbandry',
        titleHi: 'पशुपालन',
        breadEn: 'Animal Husbandry',
        breadHi: 'पशुपालन',
        descEn: 'Comprehensive study guide covering animal husbandry, livestock, dairying, poultry, and fisheries for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए पशुपालन, पशुधन, डेयरी, मुर्गी पालन और मत्स्य पालन को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Animal Husbandry" (पशुपालन - पशुधन, डेयरी, मुर्गी पालन, मत्स्य पालन).`
    },
    {
        key: 'social-geography-demographics-tribes-migration',
        titleEn: 'Social Geography of India',
        titleHi: 'भारत का सामाजिक भूगोल',
        breadEn: 'Social Geography',
        breadHi: 'सामाजिक भूगोल',
        descEn: 'Comprehensive study guide covering population, tribes, migration, and social aspects of Indian geography for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए जनसंख्या, जनजातियां, प्रवास और भारत के जनसांख्यिकीय पहलुओं को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Social Geography of India" (भारत का सामाजिक भूगोल - जनसंख्या, जनजातियां, प्रवास).`
    },
    {
        key: 'census-data-demographic-attributes',
        titleEn: 'Census Data and Demographics',
        titleHi: 'जनगणना और जनसांख्यिकी',
        breadEn: 'Census & Demographics',
        breadHi: 'जनगणना और जनसांख्यिकी',
        descEn: 'Comprehensive study guide covering census data, demographic attributes, population trends, and statistical data for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए जनगणना डेटा, जनसांख्यिकीय विशेषताएं, जनसंख्या रुझानों और सांख्यिकीय आँकड़े को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Census Data and Demographics" (जनगणना और जनसांख्यिकी).`
    },
    {
        key: 'urbanization-trends-issues',
        titleEn: 'Urbanization Trends and Issues',
        titleHi: 'शहरीकरण के रुझान और मुद्दे',
        breadEn: 'Urbanization',
        breadHi: 'शहरीकरण',
        descEn: 'Comprehensive study guide covering urbanization trends, issues, urban infrastructure, and urban development in India for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए शहरीकरण रुझान, मुद्दे, शहरी बुनियादी ढांचा और शहरी विकास को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Urbanization Trends and Issues" (शहरीकरण के रुझान और मुद्दे).`
    },
    {
        key: 'slums-urban-infrastructure',
        titleEn: 'Slums and Urban Infrastructure',
        titleHi: 'मलिन बस्तियां और शहरी बुनियादी ढांचा',
        breadEn: 'Slums & Urban Infrastructure',
        breadHi: 'मलिन बस्तियां और शहरी बुनियादी ढांचा',
        descEn: 'Comprehensive study guide covering slums, urban infrastructure, housing, and urban amenities for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए मलिन बस्तियां, शहरी बुनियादी ढांचा, आवास और शहरी सुविधाओं को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Slums and Urban Infrastructure" (मलिन बस्तियां और शहरी बुनियादी ढांचा).`
    },
    {
        key: 'smart-cities-mission',
        titleEn: 'Smart Cities Mission',
        titleHi: 'स्मार्ट सिटी मिशन',
        breadEn: 'Smart Cities Mission',
        breadHi: 'स्मार्ट सिटी मिशन',
        descEn: 'Comprehensive study guide covering Smart Cities Mission, objectives, features, and implementation in India for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए स्मार्ट सिटी मिशन, उद्देश्य, विशेषताएं और भारत में कार्यान्वयन को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Smart Cities Mission" (स्मार्ट सिटी मिशन).`
    },
    {
        key: 'shyama-prasad-mukherji-rurban-mission-smart-villages',
        titleEn: 'Shyama Prasad Mukherji Rurban Mission',
        titleHi: 'श्यामा प्रसाद मुखर्जी रूर्बन मिशन',
        breadEn: 'Rurban Mission',
        breadHi: 'रूर्बन मिशन',
        descEn: 'Comprehensive study guide covering Rurban Mission, smart villages, and rural development initiatives for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए रूर्बन मिशन, स्मार्ट ग्राम और ग्रामीण विकास पहलों को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Shyama Prasad Mukherji Rurban Mission" (श्यामा प्रसाद मुखर्जी रूर्बन मिशन).`
    },
    {
        key: 'climatology-oceanography-basic-concepts',
        titleEn: 'Climatology and Oceanography',
        titleHi: 'जलवायु विज्ञान और समुद्र विज्ञान',
        breadEn: 'Climatology & Oceanography',
        breadHi: 'जलवायु और समुद्र विज्ञान',
        descEn: 'Comprehensive study guide covering basic concepts of climatology and oceanography for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए जलवायु विज्ञान और समुद्र विज्ञान के मूल अवधारणाओं को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Climatology and Oceanography" (जलवायु विज्ञान और समुद्र विज्ञान - मूल अवधारणाएं).`
    },
    {
        key: 'continents-oceans-major-mountains-rivers-deserts',
        titleEn: 'World Geography',
        titleHi: 'विश्व भूगोल',
        breadEn: 'World Geography',
        breadHi: 'विश्व भूगोल',
        descEn: 'Comprehensive study guide covering world geography - continents, oceans, major mountains, rivers, and deserts for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए विश्व भूगोल - महाद्वीप, महासागर, प्रमुख पर्वत, नदियां और मरुस्थल को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "World Geography" (विश्व भूगोल - महाद्वीप, महासागर, पर्वत, नदियां, मरुस्थल).`
    },
    {
        key: 'major-economic-regions-of-the-world',
        titleEn: 'Major Economic Regions of the World',
        titleHi: 'विश्व के प्रमुख आर्थिक क्षेत्र',
        breadEn: 'World Economic Regions',
        breadHi: 'विश्व के आर्थिक क्षेत्र',
        descEn: 'Comprehensive study guide covering major economic regions of the world for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए विश्व के प्रमुख आर्थिक क्षेत्रों को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Major Economic Regions of the World" (विश्व के प्रमुख आर्थिक क्षेत्र).`
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
                <a href="../../index.html#geo">Geography</a>
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
    return `You are an expert UPSSSC Lower Mains exam content creator for Indian Geography. 
Generate EXTREMELY COMPREHENSIVE and DETAILED exam-focused content for: "${topic.titleEn}" (${topic.titleHi})

CRITICAL SIZE REQUIREMENTS:
- The final HTML file must be at least 250KB
- The theory section alone must contain 15-20 detailed cards (card-premium divs)
- Each card must have extensive paragraphs with facts, data, figures, examples
- Theory must be 150KB+ of content with maximum detail

IMPORTANT: Return ONLY valid JSON. No markdown, no explanation. Just the JSON object.

Generate this exact JSON structure:
{
  "theory": "<VERY LARGE HTML string with 15-20 card-premium divs - MINIMUM 150KB OF THEORY CONTENT>",
  "practiceQs": [<array of exactly 30 MCQ objects WITH COMPLETE MIXTURE of all question types>],
  "pyqs": [<array of exactly 10 PYQ objects>],
  "testQs": [<array of exactly 15 MCQ objects>]
}

THEORY HTML RULES (CRITICAL - MAKE EXTREMELY DETAILED):
- Use these exact CSS classes: card-premium, card-title, theory-heading, theory-para, theory-highlight, theory-overflow-mb, tab-active-bar, theory-section-sep
- Each card has: <div class="card-premium"><h3 class="card-title">...</h3>...</div>
- Use <span class="lang-en">English text</span> and <span class="lang-hi">हिंदी पाठ</span> for ALL text
- Use <h4 class="lang-en theory-heading">heading</h4> and <h4 class="lang-hi theory-heading">शीर्षक</h4>
- Use tables with thead/tbody, class="tab-active-bar" on header rows
- Highlight key facts with <div class="theory-highlight">
- MAKE THEORY EXTREMELY DETAILED with 15-20 cards covering ALL aspects
- Each card must have 3-4 paragraphs of detailed content with facts, figures, data
- Include specific numbers, percentages, rankings, important dates, names of places, rivers, mountains, etc.
- Add multiple tables comparing different features, listing important data
- Make it suitable for UPSSSC Lower Mains, UP PCS level - maximum detail required

PRACTICE QUESTION RULES (30 questions - MUST INCLUDE ALL TYPES):
Each object: { "qEn": "English question", "qHi": "हिंदी प्रश्न", "opts": [{"en":"A option","hi":"A विकल्प"},{"en":"B","hi":"B"},{"en":"C","hi":"C"},{"en":"D","hi":"D"}], "ans": 0, "solEn": "Explanation in English", "solHi": "हिंदी में व्याख्या" }
- ans is 0-based index (0=A, 1=B, 2=C, 3=D)
- MUST INCLUDE ALL THESE TYPES (at least 3-4 of each):
  * Factual questions (What, Which, Where, When, Who)
  * Match the column questions (Match column A with column B)
  * Multi-statement True/False questions (Which of the following statements are correct)
  * Assertion-Reason questions
  * Data-based questions (Based on census data, rankings, percentages)
  * Cause-Effect questions
  * Application-based questions
- All questions must be relevant to UPSSSC Lower Mains syllabus
- Explanations must be detailed with correct answers clearly marked

PYQ RULES (10 questions):
Each object: { "qEn": "...", "qHi": "...", "opts": [...], "ans": 0, "year": "UP PCS 2019", "solEn": "...", "solHi": "..." }
- Use realistic UP exam years: UP PCS 2015-2023, UPSSSC 2016-2023, UP Lower PCS 2018-2022
- Questions must be realistic past-exam style with detailed explanations

TEST QUESTION RULES (15 questions - different from practice):
Each object: { "qEn": "...", "qHi": "...", "opts": [{"en":"...","hi":"..."},{"en":"...","hi":"..."},{"en":"...","hi":"..."},{"en":"...","hi":"..."}], "ans": "A", "solEn": "...", "solHi": "..." }
- ans is "A", "B", "C", or "D" (letter, not number)
- These questions should be different from practice questions
- Include detailed explanations

Topic: ${topic.prompt}
CRITICAL REMINDERS:
1. Theory MUST have 15-20 cards with extensive content - each card 8-10KB of HTML
2. Total file size must exceed 250KB
3. Practice questions must include ALL types: factual, match-column, True/False, assertion-reason, data-based, cause-effect, application-based
4. Use specific data, figures, percentages, rankings from official sources
5. Make content exam-focused for UPSSSC Lower Mains with maximum detail`;
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
    'gemini-3.5-flash',
    'gemini-3.1-flash-lite',
];

// ─── Main Generator ───────────────────────────────────────────────────────────

async function generateTopic(topic) {
    console.log(`\n⟳ Generating: ${topic.titleEn}...`);

    // ── Pass 1: Theory (3 calls to reach 250KB+) ────────────────────────────
    const theoryPrompt = `You are an expert UPSSSC Lower Mains exam content creator for Indian Geography.
Generate EXTREMELY COMPREHENSIVE theory content for: "${topic.titleEn}" (${topic.titleHi})

CRITICAL: Theory must be 150KB+ of HTML with 15-20 detailed cards.

Return ONLY valid JSON:
{
  "theory": "<VERY LARGE HTML with 15-20 card-premium divs. Each card 3-4 paragraphs with facts, data, tables. Minimum 150KB total theory content.>"
}

RULES:
- Use card-premium, card-title, theory-heading, theory-para, theory-highlight, tab-active-bar, theory-section-sep
- Bilingual: <span class="lang-en"> and <span class="lang-hi">
- Include 4+ tables with geographical data
- Include 5+ theory-highlight boxes
- Every paragraph substantive with real data

Topic: ${topic.prompt}`;

    let theoryParts = [];
    for (let part = 0; part < 3; part++) {
        for (let attempt = 0; attempt < 2; attempt++) {
            try {
                console.log(`  → Theory part ${part + 1}/3: attempt ${attempt + 1}/2`);
                const response = await ai.models.generateContent({
                    model: MODEL_POOL[0],
                    contents: theoryPrompt,
                    config: {
                        thinkingConfig: { thinkingBudget: 0 },
                        temperature: 0.7,
                        maxOutputTokens: 131072
                    }
                });
                let jsonStr = response.text.trim();
                if (jsonStr.startsWith('```')) jsonStr = jsonStr.replace(/^```(?:json)?\n?/, '').replace(/\n?```$/, '');
                const data = JSON.parse(jsonStr);
                const partHtml = data.theory || '';
                theoryParts.push(partHtml);
                console.log(`  ✓ Theory part ${part + 1} generated: ${Math.round(partHtml.length / 1024)} KB`);
                break;
            } catch (err) {
                console.log(`  ⚠ Theory part ${part + 1} attempt ${attempt + 1} failed: ${err.message}`);
                await new Promise(r => setTimeout(r, 3000));
            }
        }
    }
    const theoryHtml = theoryParts.join('');

    // ── Pass 2: Questions ───────────────────────────────────────────────────
    const questionsPrompt = `You are an expert UPSSSC Lower Mains exam content creator for Indian Geography.
Generate practice questions, PYQs, and test for: "${topic.titleEn}" (${topic.titleHi})

CRITICAL: Include ALL question types with detailed explanations.

Return ONLY valid JSON:
{
  "practiceQs": [30 MCQ objects - MIXTURE of all types],
  "pyqs": [10 PYQ objects],
  "testQs": [15 MCQ objects]
}

PRACTICE (30 Qs) DISTRIBUTION:
- Q1-6: Factual
- Q7-10: Match the column
- Q11-15: Multi-statement True/False
- Q16-20: Assertion-Reason
- Q21-24: Data-based (census, stats)
- Q25-27: Cause-Effect
- Q28-30: Application-based

Format each MCQ:
{ "qEn": "...", "qHi": "...", "opts": [{"en":"A","hi":"A"},{"en":"B","hi":"B"},{"en":"C","hi":"C"},{"en":"D","hi":"D"}], "ans": 0, "solEn": "50+ word explanation", "solHi": "व्याख्या" }

PYQs: Use real UP exam years (UP PCS 2015-2023, UPSSSC 2016-2023). Each with year field.
Test: 15 different questions from practice.

Topic: ${topic.prompt}`;

    let practiceQs = [], pyqs = [], testQs = [];
    for (let attempt = 0; attempt < 2; attempt++) {
        try {
            console.log(`  → Questions: attempt ${attempt + 1}/2`);
            const response = await ai.models.generateContent({
                model: MODEL_POOL[0],
                contents: questionsPrompt,
                config: {
                    thinkingConfig: { thinkingBudget: 0 },
                    temperature: 0.7,
                    maxOutputTokens: 131072
                }
            });
            let jsonStr = response.text.trim();
            if (jsonStr.startsWith('```')) jsonStr = jsonStr.replace(/^```(?:json)?\n?/, '').replace(/\n?```$/, '');
            const data = JSON.parse(jsonStr);
            practiceQs = data.practiceQs || [];
            pyqs = data.pyqs || [];
            testQs = data.testQs || [];
            console.log(`  ✓ Questions: ${practiceQs.length} practice, ${pyqs.length} PYQs, ${testQs.length} test`);
            break;
        } catch (err) {
            console.log(`  ⚠ Questions attempt ${attempt + 1} failed: ${err.message}`);
            await new Promise(r => setTimeout(r, 3000));
        }
    }

    // ── Combine and Write ───────────────────────────────────────────────────
    const practiceHtml = buildPracticeHtml(practiceQs);
    const pyqHtml = buildPyqHtml(pyqs);
    const testHtml = buildTestHtml(testQs);
    const testDataJSON = JSON.stringify(testQs.map(q => ({ ans: q.ans, solEn: q.solEn, solHi: q.solHi })));

    const html = pageShell(topic, theoryHtml, practiceHtml, pyqHtml, testHtml, testDataJSON);

    const outDir = path.join(BASE, topic.key);
    if (!fs.existsSync(outDir)) fs.mkdirSync(outDir, { recursive: true });
    const outFile = path.join(outDir, 'index.html');
    fs.writeFileSync(outFile, html, 'utf8');

    const sizeKB = Math.round(html.length / 1024);
    console.log(`  ✓ Written: ${topic.key}/index.html (${sizeKB} KB)`);
}

async function main() {
    console.log('=== UPSSSC Lower Mains Geography Page Generator ===');
    console.log(`Using Gemini API Key: ${API_KEY ? API_KEY.substring(0, 10) + '...' : 'NOT FOUND'}`);

    if (!API_KEY) {
        console.error('ERROR: GEMINI_API_KEY not found in .env');
        process.exit(1);
    }

    const retryKeys = process.env.RETRY_KEYS ? process.env.RETRY_KEYS.split(',').map(k => k.trim()) : null;
    const topicsToRun = retryKeys ? TOPICS.filter(t => t.key.includes(retryKeys)) : TOPICS;

    if (retryKeys) console.log(`Retrying only: ${retryKeys.join(', ')}`);
    console.log(`Topics to generate: ${topicsToRun.length}`);

    const failed = [];
    for (const topic of topicsToRun) {
        try {
            await generateTopic(topic);
            await new Promise(r => setTimeout(r, 3000));
        } catch (err) {
            console.error(`  ✗ Failed: ${topic.key} — err.message`);
            failed.push(topic.key);
        }
    }

    console.log('\n=== Generation Complete ===');
    if (failed.length > 0) {
        console.log(`Failed topics (${failed.length}): ${failed.join(', ')}`);
        console.log(`Retry with: RETRY_KEYS=${failed.join(',')} node scripts/gen_geography_pages.js`);
    } else {
        console.log('All topics generated successfully! ✓');
    }
}

main().catch(console.error);
