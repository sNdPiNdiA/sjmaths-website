/**
 * UPSSSC Lower Mains Computer Page Generator
 * Uses Gemini API to generate detailed content for 18 computer topics
 * Run: node scripts/gen_computer_pages.js
 */

require('dotenv').config();
const { GoogleGenAI } = require('@google/genai');
const fs = require('fs');
const path = require('path');

const API_KEY = process.env.GEMINI_API_KEY;
const ai = new GoogleGenAI({ apiKey: API_KEY });

const BASE = path.join(__dirname, '..', 'upsssc-lower-mains', 'computer');

// Topic definitions
const TOPICS = [
    {
        key: 'history-introduction-and-application-of-computer',
        titleEn: 'History, Introduction & Application of Computer',
        titleHi: 'कंप्यूटर का इतिहास, परिचय और अनुप्रयोग',
        breadEn: 'History & Introduction of Computer',
        breadHi: 'कंप्यूटर का इतिहास और परिचय',
        descEn: 'Comprehensive study guide covering the history, generations, types, and applications of computers for UPSSSC Lower Mains exam.',
        descHi: 'UPSSSC लोअर मेन्स परीक्षा के लिए कंप्यूटर के इतिहास, पीढ़ियों, प्रकारों और अनुप्रयोगों को कवर करने वाली व्यापक अध्ययन मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "History, Introduction and Application of Computer" (कंप्यूटर का इतिहास, परिचय और अनुप्रयोग).`
    },
    {
        key: 'input-and-output',
        titleEn: 'Input and Output Devices',
        titleHi: 'इनपुट और आउटपुट डिवाइस',
        breadEn: 'Input & Output Devices',
        breadHi: 'इनपुट और आउटपुट डिवाइस',
        descEn: 'Comprehensive study guide covering input devices (keyboard, mouse, scanner) and output devices (monitor, printer, speaker) for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए इनपुट डिवाइस (कीबोर्ड, माउस, स्कैनर) और आउटपुट डिवाइस (मॉनिटर, प्रिंटर, स्पीकर) को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Input and Output Devices" (इनपुट और आउटपुट डिवाइस).`
    },
    {
        key: 'hardware-and-software',
        titleEn: 'Hardware and Software',
        titleHi: 'हार्डवेयर और सॉफ्टवेयर',
        breadEn: 'Hardware & Software',
        breadHi: 'हार्डवेयर और सॉफ्टवेयर',
        descEn: 'Comprehensive study guide covering computer hardware components, software types (system, application), and their functions for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए कंप्यूटर हार्डवेयर घटकों, सॉफ्टवेयर प्रकारों (सिस्टम, एप्लिकेशन) और उनके कार्यों को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Hardware and Software" (हार्डवेयर और सॉफ्टवेयर).`
    },
    {
        key: 'operating-system-social-networking-e-governance',
        titleEn: 'Operating System, Social Networking & E-Governance',
        titleHi: 'ऑपरेटिंग सिस्टम, सोशल नेटवर्किंग और ई-गवर्नेंस',
        breadEn: 'OS, Social Networking & E-Gov',
        breadHi: 'OS, सोशल नेटवर्किंग और ई-गवर्नेंस',
        descEn: 'Comprehensive study guide covering operating systems, social media platforms, and e-governance initiatives for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए ऑपरेटिंग सिस्टम, सोशल मीडिया प्लेटफॉर्म और ई-गवर्नेंस पहलों को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Operating System, Social Networking and E-Governance" (ऑपरेटिंग सिस्टम, सोशल नेटवर्किंग और ई-गवर्नेंस).`
    },
    {
        key: 'important-elements-of-word-processing-ms-word-and-excel-processing-ms-excel',
        titleEn: 'Word Processing (MS Word) & Excel Processing (MS Excel)',
        titleHi: 'वर्ड प्रोसेसिंग (MS Word) और एक्सेल प्रोसेसिंग (MS Excel)',
        breadEn: 'MS Word & MS Excel',
        breadHi: 'MS Word और MS Excel',
        descEn: 'Comprehensive study guide covering MS Word and MS Excel features, functions, shortcuts, and applications for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए MS Word और MS Excel की विशेषताओं, कार्यों, शॉर्टकट और अनुप्रयोगों को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Important Elements of Word Processing MS Word and Excel Processing MS Excel" (वर्ड प्रोसेसिंग और एक्सेल प्रोसेसिंग).`
    },
    {
        key: 'creation-of-e-mail-id-and-use-operation-of-e-mail',
        titleEn: 'Creation of E-Mail ID & Use/Operation of E-Mail',
        titleHi: 'ई-मेल आईडी का निर्माण और ई-मेल का उपयोग/संचालन',
        breadEn: 'E-Mail Creation & Operation',
        breadHi: 'ई-मेल निर्माण और संचालन',
        descEn: 'Comprehensive study guide covering email creation, sending, receiving, attachments, CC/BCC, and email etiquette for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए ईमेल निर्माण, भेजना, प्राप्त करना, अटैचमेंट, CC/BCC और ईमेल शिष्टाचार को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Creation of E-Mail ID and Use Operation of E-Mail" (ई-मेल आईडी का निर्माण और ई-मेल का उपयोग).`
    },
    {
        key: 'internet',
        titleEn: 'Internet',
        titleHi: 'इंटरनेट',
        breadEn: 'Internet',
        breadHi: 'इंटरनेट',
        descEn: 'Comprehensive study guide covering internet basics, protocols, services, browsers, search engines, and applications for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए इंटरनेट की मूल बातें, प्रोटोकॉल, सेवाएं, ब्राउज़र, सर्च इंजन और अनुप्रयोगों को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Internet" (इंटरनेट).`
    },
    {
        key: 'world-wide-web-www',
        titleEn: 'World Wide Web (WWW)',
        titleHi: 'वर्ल्ड वाइड वेब (WWW)',
        breadEn: 'World Wide Web',
        breadHi: 'वर्ल्ड वाइड वेब',
        descEn: 'Comprehensive study guide covering WWW concepts, web servers, browsers, HTML, URLs, and web technologies for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए WWW अवधारणाओं, वेब सर्वर, ब्राउज़र, HTML, URL और वेब तकनीकों को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "World Wide Web WWW" (वर्ल्ड वाइड वेब).`
    },
    {
        key: 'internet-protocol-ip-address',
        titleEn: 'Internet Protocol (IP Address)',
        titleHi: 'इंटरनेट प्रोटोकॉल (IP पता)',
        breadEn: 'Internet Protocol & IP Address',
        breadHi: 'इंटरनेट प्रोटोकॉल और IP पता',
        descEn: 'Comprehensive study guide covering IP addressing, IPv4/IPv6, DNS, TCP/IP, and networking protocols for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए IP एड्रेसिंग, IPv4/IPv6, DNS, TCP/IP और नेटवर्किंग प्रोटोकॉल को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Internet Protocol IP Address" (इंटरनेट प्रोटोकॉल IP पता).`
    },
    {
        key: 'information-technology',
        titleEn: 'Information Technology',
        titleHi: 'सूचना प्रौद्योगिकी',
        breadEn: 'Information Technology',
        breadHi: 'सूचना प्रौद्योगिकी',
        descEn: 'Comprehensive study guide covering IT basics, databases, networking, cybersecurity, and IT applications for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए IT मूल बातें, डेटाबेस, नेटवर्किंग, साइबर सुरक्षा और IT अनुप्रयोगों को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Information Technology" (सूचना प्रौद्योगिकी).`
    },
    {
        key: 'it-gadgets-and-their-applications',
        titleEn: 'IT Gadgets and Their Applications',
        titleHi: 'IT गैजेट्स और उनके अनुप्रयोग',
        breadEn: 'IT Gadgets & Applications',
        breadHi: 'IT गैजेट्स और अनुप्रयोग',
        descEn: 'Comprehensive study guide covering modern IT gadgets, smartphones, tablets, wearables, and their applications for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए आधुनिक IT गैजेट्स, स्मार्टफोन, टैबलेट, वियरेबल्स और उनके अनुप्रयोगों को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "IT Gadgets and Their Applications" (IT गैजेट्स और उनके अनुप्रयोग).`
    },
    {
        key: 'operation-of-printer-tablet-and-mobile',
        titleEn: 'Operation of Printer, Tablet and Mobile',
        titleHi: 'प्रिंटर, टैबलेट और मोबाइल का संचालन',
        breadEn: 'Printer, Tablet & Mobile',
        breadHi: 'प्रिंटर, टैबलेट और मोबाइल',
        descEn: 'Comprehensive study guide covering operation, maintenance, and troubleshooting of printers, tablets, and mobile devices for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए प्रिंटर, टैबलेट और मोबाइल उपकरणों के संचालन, रखरखाव और समस्या निवारण को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Operation of Printer Tablet and Mobile" (प्रिंटर, टैबलेट और मोबाइल का संचालन).`
    },
    {
        key: 'india-s-achievements-in-this-field',
        titleEn: "India's Achievements in IT Field",
        titleHi: 'इस क्षेत्र में भारत की उपलब्धियां',
        breadEn: "India's IT Achievements",
        breadHi: 'भारत की IT उपलब्धियां',
        descEn: 'Comprehensive study guide covering India\'s achievements in IT, software exports, digital India, startups, and space technology for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए IT, सॉफ्टवेयर निर्यात, डिजिटल इंडिया, स्टार्टअप और अंतरिक्ष प्रौद्योगिकी में भारत की उपलब्धियों को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "India's Achievements in IT Field" (इस क्षेत्र में भारत की उपलब्धियां).`
    },
    {
        key: 'artificial-intelligence',
        titleEn: 'Artificial Intelligence',
        titleHi: 'आर्टिफिशियल इंटेलिजेंस',
        breadEn: 'Artificial Intelligence',
        breadHi: 'आर्टिफिशियल इंटेलिजेंस',
        descEn: 'Comprehensive study guide covering AI concepts, machine learning, neural networks, NLP, and AI applications for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए AI अवधारणाओं, मशीन लर्निंग, न्यूरल नेटवर्क, NLP और AI अनुप्रयोगों को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Artificial Intelligence" (आर्टिफिशियल इंटेलिजेंस).`
    },
    {
        key: 'machine-learning',
        titleEn: 'Machine Learning',
        titleHi: 'मशीन लर्निंग',
        breadEn: 'Machine Learning',
        breadHi: 'मशीन लर्निंग',
        descEn: 'Comprehensive study guide covering ML concepts, supervised/unsupervised learning, algorithms, and applications for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए ML अवधारणाओं, पर्यवेक्षित/अपर्यवेक्षित शिक्षण, एल्गोरिदम और अनुप्रयोगों को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Machine Learning" (मशीन लर्निंग).`
    },
    {
        key: 'deep-learning',
        titleEn: 'Deep Learning',
        titleHi: 'डीप लर्निंग',
        breadEn: 'Deep Learning',
        breadHi: 'डीप लर्निंग',
        descEn: 'Comprehensive study guide covering deep learning concepts, neural networks, CNNs, RNNs, and applications for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए डीप लर्निंग अवधारणाओं, न्यूरल नेटवर्क, CNN, RNN और अनुप्रयोगों को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Deep Learning" (डीप लर्निंग).`
    },
    {
        key: 'big-data-processing',
        titleEn: 'Big Data Processing',
        titleHi: 'बिग डेटा प्रोसेसिंग',
        breadEn: 'Big Data Processing',
        breadHi: 'बिग डेटा प्रोसेसिंग',
        descEn: 'Comprehensive study guide covering big data concepts, Hadoop, Spark, data analytics, and applications for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए बिग डेटा अवधारणाओं, Hadoop, Spark, डेटा एनालिटिक्स और अनुप्रयोगों को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Big Data Processing" (बिग डेटा प्रोसेसिंग).`
    },
    {
        key: 'internet-of-things',
        titleEn: 'Internet of Things (IoT)',
        titleHi: 'इंटरनेट ऑफ थिंग्स (IoT)',
        breadEn: 'Internet of Things',
        breadHi: 'इंटरनेट ऑफ थिंग्स',
        descEn: 'Comprehensive study guide covering IoT concepts, architecture, sensors, applications, and security for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए IoT अवधारणाओं, आर्किटेक्चर, सेंसर, अनुप्रयोगों और सुरक्षा को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Internet of Things IoT" (इंटरनेट ऑफ थिंग्स).`
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
                <a href="../../index.html#computer">Computer</a>
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
    return `You are an expert UPSSSC Lower Mains exam content creator for Computer Knowledge. 
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
Focus on: facts most commonly asked in UP state government exams, key definitions, concepts, applications.`;
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
    console.log('=== UPSSSC Lower Mains Computer Page Generator ===');
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
        console.log(`Retry with: RETRY_KEYS=${failed.join(',')} node scripts/gen_computer_pages.js`);
    } else {
        console.log('All topics generated successfully! ✓');
    }
}

main().catch(console.error);