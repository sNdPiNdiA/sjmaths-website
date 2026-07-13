/**
 * UPSSSC Lower Mains UP GK Page Generator
 * Generates comprehensive content (Theory, Practice, PYQs, Test) for all 23 UP GK topics
 */

require('dotenv').config();
const { GoogleGenAI } = require('@google/genai');
const fs = require('fs');
const path = require('path');

const API_KEY = process.env.GEMINI_API_KEY;
const ai = new GoogleGenAI({ apiKey: API_KEY });

const BASE = path.join(__dirname, '..', 'upsssc-lower-mains', 'up-gk');

const PREMIUM_MODELS = [
  'gemini-3.5-flash',
  'gemini-3-flash-preview',
  'gemini-2.5-flash',
  'gemini-2.5-flash-lite'
];

const TOPICS = [
  {
    key: 'history-of-uttar-pradesh',
    titleEn: 'History of Uttar Pradesh',
    titleHi: 'उत्तर प्रदेश का इतिहास',
    breadEn: 'UP History',
    breadHi: 'यूपी का इतिहास',
    descEn: 'Comprehensive study notes on the ancient, medieval, and modern history of Uttar Pradesh, major events, and historical personalities.',
    descHi: 'उत्तर प्रदेश के प्राचीन, मध्यकालीन और आधुनिक इतिहास, प्रमुख घटनाओं और ऐतिहासिक व्यक्तित्वों पर व्यापक अध्ययन नोट्स।',
    prompt: 'Ancient, Medieval and Modern history of Uttar Pradesh, major rulers, dynasties, and key historical events.'
  },
  {
    key: 'culture',
    titleEn: 'Culture of Uttar Pradesh',
    titleHi: 'उत्तर प्रदेश की संस्कृति',
    breadEn: 'UP Culture',
    breadHi: 'यूपी की संस्कृति',
    descEn: 'Study guide covering the rich cultural heritage, traditions, fairs, and festivals of Uttar Pradesh.',
    descHi: 'उत्तर प्रदेश की समृद्ध सांस्कृतिक विरासत, परंपराओं, मेलों और त्योहारों को कवर करने वाली अध्ययन मार्गदर्शिका।',
    prompt: 'Cultural traditions, fairs, religious centers, and cultural heritage of Uttar Pradesh.'
  },
  {
    key: 'art',
    titleEn: 'Art of Uttar Pradesh',
    titleHi: 'उत्तर प्रदेश की कला',
    breadEn: 'UP Art',
    breadHi: 'यूपी की कला',
    descEn: 'Exhaustive notes on the painting, craft, sculpture, and traditional arts of Uttar Pradesh.',
    descHi: 'उत्तर प्रदेश की चित्रकला, शिल्प, मूर्तिकला और पारंपरिक कलाओं पर विस्तृत नोट्स।',
    prompt: 'Traditional arts, paintings, crafts, and regional artistic schools of Uttar Pradesh.'
  },
  {
    key: 'architecture',
    titleEn: 'Architecture of Uttar Pradesh',
    titleHi: 'उत्तर प्रदेश की वास्तुकला',
    breadEn: 'UP Architecture',
    breadHi: 'यूपी की वास्तुकला',
    descEn: 'Detailed guide to the architectural landmarks, monuments, and historical structures of Uttar Pradesh.',
    descHi: 'उत्तर प्रदेश के वास्तुकला स्थलों, स्मारकों और ऐतिहासिक संरचनाओं के लिए विस्तृत मार्गदर्शिका।',
    prompt: 'Architectural heritage, monuments, temples, mosques, and stupas of Uttar Pradesh.'
  },
  {
    key: 'festivals',
    titleEn: 'Festivals of Uttar Pradesh',
    titleHi: 'उत्तर प्रदेश के त्यौहार',
    breadEn: 'UP Festivals',
    breadHi: 'यूपी के त्यौहार',
    descEn: 'Study notes on major regional festivals, Kumbh Mela, and cultural celebrations in Uttar Pradesh.',
    descHi: 'उत्तर प्रदेश में प्रमुख क्षेत्रीय त्योहारों, कुंभ मेले और सांस्कृतिक उत्सवों पर अध्ययन नोट्स।',
    prompt: 'Major festivals, regional celebrations, Kumbh Mela, Taj Mahotsav, and local fairs of UP.'
  },
  {
    key: 'folk-dances',
    titleEn: 'Folk Dances of Uttar Pradesh',
    titleHi: 'उत्तर प्रदेश के लोक नृत्य',
    breadEn: 'UP Folk Dances',
    breadHi: 'यूपी के लोक नृत्य',
    descEn: 'Exhaustive details on classical Kathak, Charkula, Karma, Raslila, and regional folk dances of UP.',
    descHi: 'यूपी के शास्त्रीय कथक, चरकुला, कर्मा, रासलीला और क्षेत्रीय लोक नृत्यों पर विस्तृत विवरण।',
    prompt: 'Classical dance (Kathak), folk dances like Charkula, Karma, Nautanki, Raslila, and regional music genres.'
  },
  {
    key: 'literature',
    titleEn: 'Literature of Uttar Pradesh',
    titleHi: 'उत्तर प्रदेश का साहित्य',
    breadEn: 'UP Literature',
    breadHi: 'यूपी का साहित्य',
    descEn: 'Study guide covering famous writers, poets, Kabir, Tulsidas, Premchand, and literary heritage of UP.',
    descHi: 'यूपी के प्रसिद्ध लेखकों, कवियों, कबीर, तुलसीदास, प्रेमचंद और साहित्यिक विरासत को कवर करने वाली अध्ययन मार्गदर्शिका।',
    prompt: 'Famous poets and writers from Uttar Pradesh, their major works, Hindi and Urdu literature development.'
  },
  {
    key: 'regional-languages',
    titleEn: 'Regional Languages of Uttar Pradesh',
    titleHi: 'उत्तर प्रदेश की क्षेत्रीय भाषाएँ',
    breadEn: 'UP Regional Languages',
    breadHi: 'यूपी की क्षेत्रीय भाषाएँ',
    descEn: 'Study notes on Hindi, Awadhi, Bhojpuri, Brajbhasha, Bundeli, and Urdu dialects in Uttar Pradesh.',
    descHi: 'उत्तर प्रदेश में हिंदी, अवधी, भोजपुरी, ब्रजभाषा, बुंदेली और उर्दू बोलियों पर अध्ययन नोट्स।',
    prompt: 'Dialects of Uttar Pradesh including Awadhi, Bhojpuri, Brajbhasha, Bundeli, Urdu, and linguistic history.'
  },
  {
    key: 'heritage',
    titleEn: 'Heritage of Uttar Pradesh',
    titleHi: 'उत्तर प्रदेश की धरोहर',
    breadEn: 'UP Heritage',
    breadHi: 'यूपी की धरोहर',
    descEn: 'Exhaustive guide to UNESCO World Heritage Sites, monuments, and historical sites in Uttar Pradesh.',
    descHi: 'उत्तर प्रदेश में यूनेस्को विश्व धरोहर स्थलों, स्मारकों और ऐतिहासिक स्थलों के लिए विस्तृत मार्गदर्शिका।',
    prompt: 'UNESCO World Heritage Sites (Taj Mahal, Agra Fort, Fatehpur Sikri), monuments, and archaeological sites of UP.'
  },
  {
    key: 'social-customs-and-tourism',
    titleEn: 'Social Customs & Tourism of Uttar Pradesh',
    titleHi: 'उत्तर प्रदेश के सामाजिक रीति-रिवाज एवं पर्यटन',
    breadEn: 'UP Customs & Tourism',
    breadHi: 'यूपी रीति-रिवाज व पर्यटन',
    descEn: 'Study notes on social customs, tribes, and tourism infrastructure development in Uttar Pradesh.',
    descHi: 'उत्तर प्रदेश में सामाजिक रीति-रिवाजों, जनजातियों और पर्यटन बुनियादी ढांचे के विकास पर अध्ययन नोट्स।',
    prompt: 'Social customs, tribes (Tharu, Buksa, etc.), major tourist circuits, and tourism policy of Uttar Pradesh.'
  },
  {
    key: 'geographical-landscape-and-environment',
    titleEn: 'Geographical Landscape & Environment of Uttar Pradesh',
    titleHi: 'उत्तर प्रदेश का भौगोलिक परिदृश्य एवं पर्यावरण',
    breadEn: 'UP Geography & Env',
    breadHi: 'यूपी भूगोल व पर्यावरण',
    descEn: 'Exhaustive guide to physical division, rivers, mountains, and environmental issues of Uttar Pradesh.',
    descHi: 'उत्तर प्रदेश के भौतिक विभाजन, नदियों, पहाड़ों और पर्यावरणीय मुद्दों के लिए विस्तृत मार्गदर्शिका।',
    prompt: 'Physiographic divisions of UP, major river systems (Ganga, Yamuna, Ghaghra, etc.), climate zones, and environmental conservation.'
  },
  {
    key: 'natural-resources',
    titleEn: 'Natural Resources of Uttar Pradesh',
    titleHi: 'उत्तर प्रदेश के प्राकृतिक संसाधन',
    breadEn: 'UP Natural Resources',
    breadHi: 'यूपी प्राकृतिक संसाधन',
    descEn: 'Study notes on water resources, minerals, and land resources in Uttar Pradesh.',
    descHi: 'उत्तर प्रदेश में जल संसाधनों, खनिजों और भूमि संसाधनों पर अध्ययन नोट्स।',
    prompt: 'Water resources, canals, dams, mineral resources, and energy resource distribution in Uttar Pradesh.'
  },
  {
    key: 'climate',
    titleEn: 'Climate of Uttar Pradesh',
    titleHi: 'उत्तर प्रदेश की जलवायु',
    breadEn: 'UP Climate',
    breadHi: 'यूपी की जलवायु',
    descEn: 'Detailed guide to seasons, rainfall distribution, and temperature patterns in Uttar Pradesh.',
    descHi: 'उत्तर प्रदेश में मौसम, वर्षा वितरण और तापमान पैटर्न के लिए विस्तृत मार्गदर्शिका।',
    prompt: 'Climatic regions, temperature variations, monsoon and rainfall patterns across different zones of UP.'
  },
  {
    key: 'soil',
    titleEn: 'Soil of Uttar Pradesh',
    titleHi: 'उत्तर प्रदेश की मिट्टी',
    breadEn: 'UP Soil',
    breadHi: 'यूपी की मिट्टी',
    descEn: 'Study notes on alluvial, red, black, and regional soil types and agriculture suitability in UP.',
    descHi: 'यूपी में जलोढ़, लाल, काली और क्षेत्रीय मिट्टी के प्रकारों और कृषि उपयुक्तता पर अध्ययन नोट्स।',
    prompt: 'Soil types of UP (Bhangar, Khadar, Red, Bundelkhand soils), soil erosion issues, and soil fertility management.'
  },
  {
    key: 'forests',
    titleEn: 'Forests of Uttar Pradesh',
    titleHi: 'उत्तर प्रदेश के वन',
    breadEn: 'UP Forests',
    breadHi: 'यूपी के वन',
    descEn: 'Comprehensive notes on forest cover, forest types, and government policies in Uttar Pradesh.',
    descHi: 'उत्तर प्रदेश में वन आवरण, वन प्रकारों और सरकारी नीतियों पर व्यापक नोट्स।',
    prompt: 'Types of forests in UP, forest cover statistics, Social Forestry, and state forest policies.'
  },
  {
    key: 'wildlife',
    titleEn: 'Wildlife of Uttar Pradesh',
    titleHi: 'उत्तर प्रदेश के वन्यजीव',
    breadEn: 'UP Wildlife',
    breadHi: 'यूपी के वन्यजीव',
    descEn: 'Study notes on Dudhwa National Park, wildlife sanctuaries, and biodiversity conservation in UP.',
    descHi: 'यूपी में दुधवा राष्ट्रीय उद्यान, वन्यजीव अभ्यारण्यों और जैव विविधता संरक्षण पर अध्ययन नोट्स।',
    prompt: 'National Parks (Dudhwa), Wildlife Sanctuaries, Bird Sanctuaries, tiger reserves, and state wildlife conservation projects in UP.'
  },
  {
    key: 'mines-and-minerals',
    titleEn: 'Mines & Minerals of Uttar Pradesh',
    titleHi: 'उत्तर प्रदेश के खान और खनिज',
    breadEn: 'UP Mines & Minerals',
    breadHi: 'यूपी खान व खनिज',
    descEn: 'Detailed guide to mineral reserves, coal, limestone, and mining activities in Uttar Pradesh.',
    descHi: 'उत्तर प्रदेश में खनिज भंडार, कोयला, चूना पत्थर और खनन गतिविधियों के लिए विस्तृत मार्गदर्शिका।',
    prompt: 'Mineral distribution (limestone, coal in Singrauli, silica sand, bauxite), mines, and mineral-based industries in UP.'
  },
  {
    key: 'economy',
    titleEn: 'Economy of Uttar Pradesh',
    titleHi: 'उत्तर प्रदेश की अर्थव्यवस्था',
    breadEn: 'UP Economy',
    breadHi: 'यूपी की अर्थव्यवस्था',
    descEn: 'Comprehensive notes on GSDP, budget highlights, state tax revenue, and economic trends of UP.',
    descHi: 'यूपी के GSDP, बजट हाइलाइट्स, राज्य कर राजस्व और आर्थिक रुझानों पर व्यापक नोट्स।',
    prompt: 'Economic structure of UP, GSDP, state budget, source of revenue, and industrial growth.'
  },
  {
    key: 'agriculture',
    titleEn: 'Agriculture of Uttar Pradesh',
    titleHi: 'उत्तर प्रदेश की कृषि',
    breadEn: 'UP Agriculture',
    breadHi: 'यूपी की कृषि',
    descEn: 'Study notes on major crops (wheat, sugarcane, paddy), irrigation, and agricultural policy in UP.',
    descHi: 'यूपी में प्रमुख फसलों (गेहूं, गन्ना, धान), सिंचाई और कृषि नीति पर अध्ययन नोट्स।',
    prompt: 'Cropping patterns, food grains (wheat, rice), commercial crops (sugarcane), irrigation sources, and agricultural schemes.'
  },
  {
    key: 'industry',
    titleEn: 'Industry of Uttar Pradesh',
    titleHi: 'उत्तर प्रदेश के उद्योग',
    breadEn: 'UP Industry',
    breadHi: 'यूपी के उद्योग',
    descEn: 'Exhaustive notes on ODOP, heavy industries, IT parks, and MSME sector in Uttar Pradesh.',
    descHi: 'उत्तर प्रदेश में ओडीओपी (ODOP), भारी उद्योगों, आईटी पार्कों और एमएसएमई क्षेत्र पर विस्तृत नोट्स।',
    prompt: 'Industrial zones, MSMEs, One District One Product (ODOP) scheme, handicraft industries, and industrial corridors (UPIDA).'
  },
  {
    key: 'business-and-employment',
    titleEn: 'Business & Employment of Uttar Pradesh',
    titleHi: 'उत्तर प्रदेश में व्यवसाय और रोजगार',
    breadEn: 'UP Biz & Employment',
    breadHi: 'यूपी व्यवसाय व रोजगार',
    descEn: 'Study guide covering business regulations, employment generation schemes, and labor reforms in UP.',
    descHi: 'यूपी में व्यावसायिक नियमों, रोजगार सृजन योजनाओं और श्रम सुधारों को कवर करने वाली अध्ययन मार्गदर्शिका।',
    prompt: 'Business environment, Ease of Doing Business rankings, start-up policy, and employment schemes (ODOP, PMEGGP) in UP.'
  },
  {
    key: 'polity-and-administration',
    titleEn: 'Polity & Administration of Uttar Pradesh',
    titleHi: 'उत्तर प्रदेश की राजव्यवस्था एवं प्रशासन',
    breadEn: 'UP Polity & Admin',
    breadHi: 'यूपी शासन व प्रशासन',
    descEn: 'Detailed guide to Governor, Chief Minister, Legislative Assembly, Panchayati Raj, and administration of UP.',
    descHi: 'उत्तर प्रदेश के राज्यपाल, मुख्यमंत्री, विधानसभा, पंचायती राज और प्रशासन के लिए विस्तृत मार्गदर्शिका।',
    prompt: 'Administrative divisions, state legislature (bicameral), Governor, Chief Minister, High Court (Allahabad), and Panchayati Raj in UP.'
  },
  {
    key: 'current-events-and-achievements-of-uttar-pradesh-state-in-various-fields-etc',
    titleEn: 'Current Events & Achievements of Uttar Pradesh',
    titleHi: 'उत्तर प्रदेश की वर्तमान घटनाएं और उपलब्धियां',
    breadEn: 'UP Current & Awards',
    breadHi: 'यूपी समसामयिकी',
    descEn: 'Comprehensive notes on recent state news, policy updates, awards, and sports achievements in Uttar Pradesh.',
    descHi: 'उत्तर प्रदेश में हालिया राज्य समाचारों, नीतिगत अपडेट, पुरस्कारों और खेल उपलब्धियों पर व्यापक नोट्स।',
    prompt: 'Recent state level current affairs, new schemes, infrastructure projects (expressways, airports), and achievements of Uttar Pradesh.'
  }
];

function pageShell(topic, theoryHtml, practiceHtml, pyqHtml, testHtml, testDataJSON) {
  return `<!DOCTYPE html>
<html lang="en">

<head>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7924751316191829" crossorigin="anonymous"></script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${topic.titleEn} - UPSSSC Lower Subordinate Mains | SJMaths</title>
    <meta name="description" content="${topic.descEn}">
    <meta name="robots" content="index, follow">
    <link rel="icon" type="image/png" href="/favicon.png">
    
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/assets/vendor/fontawesome/css/all.min.css?v=7441465c">
    
    <!-- Stylesheets -->
    <link rel="stylesheet" href="/assets/css/main.min.css?v=b1e44e09">
    <link rel="stylesheet" href="/assets/css/layout.min.css?v=68b2a46f">
    <link rel="stylesheet" href="/assets/css/component.min.css?v=015629f5">
    <link rel="stylesheet" href="/assets/css/improved-ui.min.css?v=ac5776e0">
    <link rel="stylesheet" href="/assets/css/pages.min.css?v=9e3bd560">
</head>

<body>
    <!-- Top Progress Bar -->
    <div class="top-prog-container"><div class="top-prog-bar" id="top-prog"></div></div>

    <button class="lang-toggle-btn" onclick="toggleLang()" aria-label="Toggle Language">A/अ</button>

    <div class="page-container">
        <div class="breadcrumb">
            <a href="/"><i class="fas fa-home"></i></a>
            <i class="fas fa-chevron-right"></i>
            <a href="/upsssc-lower-mains/" class="lang-en">UPSSSC Lower Subordinate</a>
            <a href="/upsssc-lower-mains/" class="lang-hi">UPSSSC लोअर सबऑर्डिनेट</a>
            <i class="fas fa-chevron-right"></i>
            <span class="lang-en">${topic.breadEn}</span>
            <span class="lang-hi">${topic.breadHi}</span>
        </div>

        <div class="topic-header">
            <h1 class="lang-en">${topic.titleEn}</h1>
            <h1 class="lang-hi">${topic.titleHi}</h1>
            <p>
                <span class="lang-en">${topic.descEn}</span>
                <span class="lang-hi">${topic.descHi}</span>
            </p>
        </div>

        <div class="subject-nav">
            <button class="sub-nav-item active" data-tab="theory" onclick="switchTab('theory')">
                <span class="lang-en">Theory &amp; Concepts</span>
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
                <div class="test-container">
                    <div id="test-start-screen">
                        <p class="test-desc lang-en">This test contains 15 multiple-choice questions based on the exam syllabus. You have 15 minutes to complete the test.</p>
                        <p class="test-desc lang-hi">इस परीक्षा में पाठ्यक्रम के आधार पर 15 बहुविकल्पीय प्रश्न हैं। परीक्षा पूरी करने के लिए आपके पास 15 मिनट का समय है।</p>
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
    </div>

    <script>
        window.upssscTestData = ${testDataJSON};
    </script>
    <script src="/assets/js/upsssc-lower.min.js?v=117a746d"></script>
    <script src="/assets/js/main.min.js?v=86340191"></script>
    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
    <script>mermaid.initialize({startOnLoad:true, theme: 'default'});</script>
</body>

</html>`;
}

function buildPrompt(topic) {
  return `You are an expert UPSSSC Lower Mains exam content creator for Uttar Pradesh General Knowledge (UP GK - उत्तर प्रदेश सामान्य ज्ञान).
Generate comprehensive and detailed exam-focused content for: "${topic.titleEn}" (${topic.titleHi}).

Generate this exact JSON structure:
{
  "theory": "<VERY DETAILED HTML string with 12-18 card-premium divs>",
  "practiceQs": [<array of exactly 30 MCQ objects>],
  "pyqs": [<array of exactly 10 PYQ objects>],
  "testQs": [<array of exactly 15 MCQ objects>]
}

THEORY HTML RULES:
- Use these exact CSS classes: card-premium, card-title, theory-heading, theory-para, theory-highlight, theory-overflow-mb, tab-active-bar, theory-section-sep
- First card MUST contain a Mindmap summarizing the topic. For the mindmap, YOU MUST generate TWO separate Mermaid diagrams: one entirely in English wrapped in <div class="lang-en"><div class="mermaid">...</div></div> and one entirely in Hindi wrapped in <div class="lang-hi"><div class="mermaid">...</div></div>. Newlines must be escaped as \\n.
- Second card MUST contain a comparison table summarizing key points.
- Include 12-18 card-premium divs covering all aspects of the topic.
- Use <span class="lang-en">English</span> and <span class="lang-hi">Hindi</span> for all text content.
- Cover all data, facts, names, years, and specific UP context (e.g. census details, rankings, districts, ministries, historical events).

PRACTICE QUESTION RULES (30 questions):
Each object: { "qEn": "Question in English", "qHi": "Question in Hindi", "opts": [{"en":"Opt A","hi":"वैकल्पिक A"},{"en":"B","hi":"B"},{"en":"C","hi":"C"},{"en":"D","hi":"D"}], "ans": 0, "solEn": "Detailed explanation", "solHi": "विस्तृत व्याख्या" }
- Mixture of types (factual, match the column, statement-based, assertion-reason).

PYQ RULES (10 questions):
Include year and exam name (e.g., "UPSSSC Lower Mains 2021", "UP PCS 2022").

TEST QUESTION RULES (15 questions):
ans is option letter ("A", "B", "C", "D").`;
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

async function generateTopic(topic, topicIndex = 0) {
  console.log(`\n Generating: ${topic.titleEn}...`);
  const prompt = buildPrompt(topic);

  let raw;
  const MAX_RETRIES = PREMIUM_MODELS.length * 2;
  const BASE_DELAY = 15000;

  for (let attempt = 0; attempt < MAX_RETRIES; attempt++) {
    const model = PREMIUM_MODELS[(attempt + topicIndex) % PREMIUM_MODELS.length];
    try {
      console.log(`  -> Using model: ${model} (attempt ${attempt + 1}/${MAX_RETRIES})`);
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
      console.log(`  OK Got response from ${model}`);
      break; 
    } catch (err) {
      const isRetryable = err.message && (
        err.message.includes('503') ||
        err.message.includes('UNAVAILABLE') ||
        err.message.includes('high demand') ||
        err.message.includes('overloaded') ||
        err.message.includes('429') ||
        err.message.includes('RESOURCE_EXHAUSTED')
      );
      if (isRetryable && attempt < MAX_RETRIES - 1) {
        const delay = BASE_DELAY * (attempt + 1);
        console.log(`  WARN ${model} error (attempt ${attempt + 1}) -> switching model in ${delay / 1000}s...`);
        await new Promise(r => setTimeout(r, delay));
      } else {
        console.error(`  FAIL All models failed for ${topic.key}:`, err.message);
        throw err;
      }
    }
  }

  let jsonStr = raw.trim();
  jsonStr = jsonStr.replace(/^```(?:json)?\n?/m, '').replace(/\n?```$/m, '');

  let data;
  try {
    data = JSON.parse(jsonStr);
  } catch (e) {
    const match = jsonStr.match(/\{[\s\S]*\}/);
    if (match) {
      try { data = JSON.parse(match[0]); }
      catch (e2) {
        console.error(`  FAIL JSON parse failed for ${topic.key}`);
        throw e2;
      }
    } else {
      throw e;
    }
  }

  const theoryHtml = data.theory || '<p>Content generation failed. Please retry.</p>';
  const practiceHtml = buildPracticeHtml(data.practiceQs || []);
  const pyqHtml = buildPyqHtml(data.pyqs || []);
  const testHtml = buildTestHtml(data.testQs || []);
  const testDataJSON = JSON.stringify((data.testQs || []).map(q => ({ ans: q.ans, solEn: q.solEn, solHi: q.solHi })));

  const html = pageShell(topic, theoryHtml, practiceHtml, pyqHtml, testHtml, testDataJSON);

  const outDir = path.join(BASE, topic.key);
  if (!fs.existsSync(outDir)) fs.mkdirSync(outDir, { recursive: true });
  const outFile = path.join(outDir, 'index.html');
  fs.writeFileSync(outFile, html, 'utf8');

  console.log(`  ✓ Written: up-gk/${topic.key}/index.html (${Math.round(html.length / 1024)} KB)`);
}

async function main() {
  console.log('=== UPSSSC Lower Mains UP GK Page Generator ===');
  
  const retryKeys = process.env.RETRY_KEYS ? process.env.RETRY_KEYS.split(',').map(k => k.trim()) : null;
  const topicsToRun = retryKeys ? TOPICS.filter(t => retryKeys.includes(t.key)) : TOPICS;

  console.log(`Topics to generate: ${topicsToRun.length}`);

  const failed = [];
  for (let i = 0; i < topicsToRun.length; i++) {
    const topic = topicsToRun[i];
    try {
      await generateTopic(topic, i);
      await new Promise(r => setTimeout(r, 12000));
    } catch (err) {
      console.error(`  ✗ Failed: ${topic.key} - ${err.message}`);
      failed.push(topic.key);
    }
  }

  console.log('\n=== UP GK Generation Complete ===');
  if (failed.length > 0) {
    console.log(`Failed topics (${failed.length}): ${failed.join(', ')}`);
  }
}

main().catch(console.error);
