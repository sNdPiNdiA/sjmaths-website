/**
 * UPSSSC Lower Mains History Page Generator
 * Uses Gemini API to generate detailed content for 10 history topics
 * Run: node scripts/gen_history_pages.js
 */

require('dotenv').config();
const { GoogleGenAI } = require('@google/genai');
const fs = require('fs');
const path = require('path');

const API_KEY = process.env.GEMINI_API_KEY;
const ai = new GoogleGenAI({ apiKey: API_KEY });

const BASE = path.join(__dirname, '..', 'upsssc-lower-mains', 'history');

// Topic definitions
const TOPICS = [
  {
    key: 'cultural-aspects',
    titleEn: 'Cultural Aspects in Indian History',
    titleHi: 'भारतीय इतिहास में सांस्कृतिक पहलू',
    breadEn: 'Cultural Aspects',
    breadHi: 'सांस्कृतिक पहलू',
    descEn: 'Comprehensive study guide covering art, architecture, literature, religion, music, dance, and philosophy across ancient, medieval and modern India.',
    descHi: 'प्राचीन, मध्यकालीन और आधुनिक भारत में कला, वास्तुकला, साहित्य, धर्म, संगीत, नृत्य और दर्शन को कवर करने वाली व्यापक अध्ययन मार्गदर्शिका।',
    prompt: `Generate UPSSSC Lower Mains exam content for "Cultural Aspects in Indian History" (सांस्कृतिक पहलू).`
  },
  {
    key: 'economic-aspects',
    titleEn: 'Economic Aspects in Indian History',
    titleHi: 'भारतीय इतिहास में आर्थिक पहलू',
    breadEn: 'Economic Aspects',
    breadHi: 'आर्थिक पहलू',
    descEn: 'Comprehensive study guide covering trade, agriculture, guilds, land revenue systems, and economic policies across ancient, medieval and modern India.',
    descHi: 'प्राचीन, मध्यकालीन और आधुनिक भारत में व्यापार, कृषि, श्रेणियों, भू-राजस्व प्रणालियों और आर्थिक नीतियों को कवर करने वाली व्यापक अध्ययन मार्गदर्शिका।',
    prompt: `Generate UPSSSC Lower Mains exam content for "Economic Aspects in Indian History" (आर्थिक पहलू).`
  },
  {
    key: 'political-aspects',
    titleEn: 'Political Aspects in Indian History',
    titleHi: 'भारतीय इतिहास में राजनीतिक पहलू',
    breadEn: 'Political Aspects',
    breadHi: 'राजनीतिक पहलू',
    descEn: 'Comprehensive study guide covering dynasties, administrative systems, political theories, and governance across ancient, medieval and modern India.',
    descHi: 'प्राचीन, मध्यकालीन और आधुनिक भारत में राजवंशों, प्रशासनिक व्यवस्थाओं, राजनीतिक सिद्धांतों और शासन को कवर करने वाली व्यापक अध्ययन मार्गदर्शिका।',
    prompt: `Generate UPSSSC Lower Mains exam content for "Political Aspects in Indian History" (राजनीतिक पहलू).`
  },
  {
    key: 'revolt-of-1857',
    titleEn: 'Revolt of 1857 – First War of Independence',
    titleHi: '1857 का विद्रोह – प्रथम स्वतंत्रता संग्राम',
    breadEn: 'Revolt of 1857',
    breadHi: '1857 का विद्रोह',
    descEn: 'Comprehensive study guide covering causes, events, leaders, centres, and consequences of the 1857 revolt against British rule.',
    descHi: '1857 के विद्रोह के कारण, घटनाएं, नेता, केंद्र और परिणामों को कवर करने वाली व्यापक अध्ययन मार्गदर्शिका।',
    prompt: `Generate UPSSSC Lower Mains exam content for "Revolt of 1857 – First War of Independence" (1857 का विद्रोह).`
  },
  {
    key: 'foundation-of-indian-national-congress',
    titleEn: 'Foundation of Indian National Congress',
    titleHi: 'भारतीय राष्ट्रीय कांग्रेस की स्थापना',
    breadEn: 'Foundation of INC',
    breadHi: 'INC की स्थापना',
    descEn: 'Comprehensive study guide covering the founding, early sessions, moderate phase, and role of INC in India\'s independence movement.',
    descHi: 'INC की स्थापना, प्रारंभिक अधिवेशनों, उदारवादी चरण और स्वतंत्रता आंदोलन में भूमिका को कवर करने वाली व्यापक मार्गदर्शिका।',
    prompt: `Generate UPSSSC Lower Mains exam content for "Foundation of Indian National Congress" (भारतीय राष्ट्रीय कांग्रेस की स्थापना).`
  },
  {
    key: 'partition-of-bengal-swadeshi-movement',
    titleEn: 'Partition of Bengal & Swadeshi Movement',
    titleHi: 'बंगाल विभाजन एवं स्वदेशी आंदोलन',
    breadEn: 'Bengal Partition & Swadeshi',
    breadHi: 'बंगाल विभाजन और स्वदेशी',
    descEn: 'Comprehensive study guide covering the 1905 Partition of Bengal, the Swadeshi Movement, Boycott, and their impact on Indian nationalism.',
    descHi: '1905 बंगाल विभाजन, स्वदेशी आंदोलन, बहिष्कार और भारतीय राष्ट्रवाद पर उनके प्रभाव को कवर करने वाली मार्गदर्शिका।',
    prompt: `Generate UPSSSC Lower Mains exam content for "Partition of Bengal & Swadeshi Movement" (बंगाल विभाजन एवं स्वदेशी आंदोलन).`
  },
  {
    key: 'surat-split-rise-of-extremism',
    titleEn: 'Surat Split & Rise of Extremism',
    titleHi: 'सूरत विभाजन एवं उग्रवाद का उदय',
    breadEn: 'Surat Split & Extremism',
    breadHi: 'सूरत विभाजन और उग्रवाद',
    descEn: 'Comprehensive study guide covering the 1907 Surat Split, rise of Bal Gangadhar Tilak, Lal-Bal-Pal, and the extremist phase of Indian nationalism.',
    descHi: '1907 सूरत विभाजन, बाल गंगाधर तिलक, लाल-बाल-पाल और भारतीय राष्ट्रवाद के उग्रवादी चरण को कवर करने वाली मार्गदर्शिका।',
    prompt: `Generate UPSSSC Lower Mains exam content for "Surat Split & Rise of Extremism in Indian National Movement" (सूरत विभाजन एवं उग्रवाद का उदय).`
  },
  {
    key: 'home-rule-movement',
    titleEn: 'Home Rule Movement (1916)',
    titleHi: 'होम रूल आंदोलन (1916)',
    breadEn: 'Home Rule Movement',
    breadHi: 'होम रूल आंदोलन',
    descEn: 'Comprehensive study guide covering the Home Rule League by Tilak and Annie Besant, their demands, and impact on Indian nationalism.',
    descHi: 'तिलक और एनी बेसेंट द्वारा होम रूल लीग, उनकी मांगों और भारतीय राष्ट्रवाद पर प्रभाव को कवर करने वाली मार्गदर्शिका।',
    prompt: `Generate UPSSSC Lower Mains exam content for "Home Rule Movement 1916" (होम रूल आंदोलन).`
  },
  {
    key: 'non-cooperation-movement',
    titleEn: 'Non-Cooperation Movement (1920–22)',
    titleHi: 'असहयोग आंदोलन (1920–22)',
    breadEn: 'Non-Cooperation Movement',
    breadHi: 'असहयोग आंदोलन',
    descEn: 'Comprehensive study guide covering Gandhi\'s Non-Cooperation Movement, Khilafat issue, Chauri Chaura, and withdrawal of the movement.',
    descHi: 'गांधी के असहयोग आंदोलन, खिलाफत मुद्दा, चौरी चौरा और आंदोलन की वापसी को कवर करने वाली मार्गदर्शिका।',
    prompt: `Generate UPSSSC Lower Mains exam content for "Non-Cooperation Movement 1920-22" (असहयोग आंदोलन).`
  },
  {
    key: 'civil-disobedience-movement',
    titleEn: 'Civil Disobedience Movement (1930–34)',
    titleHi: 'सविनय अवज्ञा आंदोलन (1930–34)',
    breadEn: 'Civil Disobedience Movement',
    breadHi: 'सविनय अवज्ञा आंदोलन',
    descEn: 'Comprehensive study guide covering the Dandi March, Salt Satyagraha, Gandhi-Irwin Pact, and Round Table Conferences.',
    descHi: 'दांडी मार्च, नमक सत्याग्रह, गांधी-इरविन समझौता और गोलमेज सम्मेलनों को कवर करने वाली व्यापक अध्ययन मार्गदर्शिका।',
    prompt: `Generate UPSSSC Lower Mains exam content for "Civil Disobedience Movement 1930-34" (सविनय अवज्ञा आंदोलन).`
  },
  {
    key: 'early-political-associations-pre-inc',
    titleEn: 'Early Political Associations (Pre-INC)',
    titleHi: 'प्रारंभिक राजनीतिक संघ (INC से पहले)',
    breadEn: 'Early Political Associations',
    breadHi: 'प्रारंभिक राजनीतिक संघ',
    descEn: 'Comprehensive study guide covering pre-INC political associations, their formation, objectives, activities, and contribution to India\'s nationalist movement.',
    descHi: 'INC से पहले के राजनीतिक संघों, उनके गठन, उद्देश्यों, गतिविधियों और भारत के राष्ट्रीय आंदोलन में योगदान को कवर करने वाली व्यापक अध्ययन मार्गदर्शिका।',
    prompt: `Generate UPSSSC Lower Mains exam content for "Early Political Associations Pre-INC" (प्रारंभिक राजनीतिक संघ).`
  },
  {
    key: 'quit-india-movement-ina',
    titleEn: 'Quit India Movement & Indian National Army',
    titleHi: 'भारत छोड़ो आंदोलन एवं आज़ाद हिंद फ़ौज',
    breadEn: 'Quit India Movement & INA',
    breadHi: 'भारत छोड़ो आंदोलन और आईएनए',
    descEn: 'Comprehensive study guide covering the 1942 Quit India Movement, underground activities, and Subhas Chandra Bose\'s Indian National Army.',
    descHi: '1942 भारत छोड़ो आंदोलन, भूमिगत गतिविधियों और सुभाष चंद्र बोस की आज़ाद हिंद फ़ौज को कवर करने वाली व्यापक अध्ययन मार्गदर्शिका।',
    prompt: `Generate UPSSSC Lower Mains exam content for "Quit India Movement & Indian National Army" (भारत छोड़ो आंदोलन एवं आज़ाद हिंद फ़ौज).`
  },
  {
    key: 'august-offer-cripps-mission',
    titleEn: 'August Offer & Cripps Mission',
    titleHi: 'अगस्त प्रस्ताव एवं क्रिप्स मिशन',
    breadEn: 'August Offer & Cripps Mission',
    breadHi: 'अगस्त प्रस्ताव और क्रिप्स मिशन',
    descEn: 'Comprehensive study guide covering the 1940 August Offer, 1942 Cripps Mission proposals, reactions, and their significance in India\'s freedom struggle.',
    descHi: '1940 अगस्त प्रस्ताव, 1942 क्रिप्स मिशन प्रस्तावों, प्रतिक्रियाओं और स्वतंत्रता संग्राम में महत्व को कवर करने वाली व्यापक मार्गदर्शिका।',
    prompt: `Generate UPSSSC Lower Mains exam content for "August Offer & Cripps Mission" (अगस्त प्रस्ताव एवं क्रिप्स मिशन).`
  },
  {
    key: 'cabinet-mission-plan-1946',
    titleEn: 'Cabinet Mission Plan (1946)',
    titleHi: 'कैबिनेट मिशन योजना (1946)',
    breadEn: 'Cabinet Mission Plan',
    breadHi: 'कैबिनेट मिशन योजना',
    descEn: 'Comprehensive study guide covering the 1946 Cabinet Mission, its proposals, groupings, reactions of Congress & Muslim League, and its outcome.',
    descHi: '1946 कैबिनेट मिशन, इसके प्रस्तावों, समूहीकरण, कांग्रेस और मुस्लिम लीग की प्रतिक्रियाओं और परिणाम को कवर करने वाली मार्गदर्शिका।',
    prompt: `Generate UPSSSC Lower Mains exam content for "Cabinet Mission Plan 1946" (कैबिनेट मिशन योजना).`
  },
  {
    key: 'mountbatten-plan-1947',
    titleEn: 'Mountbatten Plan & Partition (1947)',
    titleHi: 'माउंटबेटन योजना एवं विभाजन (1947)',
    breadEn: 'Mountbatten Plan',
    breadHi: 'माउंटबेटन योजना',
    descEn: 'Comprehensive study guide covering the Mountbatten Plan of June 3, 1947, partition of India, Radcliffe Line, and the aftermath of independence.',
    descHi: '3 जून 1947 की माउंटबेटन योजना, भारत विभाजन, रैडक्लिफ रेखा और स्वतंत्रता के परिणाम को कवर करने वाली मार्गदर्शिका।',
    prompt: `Generate UPSSSC Lower Mains exam content for "Mountbatten Plan & Partition of India 1947" (माउंटबेटन योजना एवं विभाजन).`
  },
  {
    key: 'indian-independence-act-1947',
    titleEn: 'Indian Independence Act (1947)',
    titleHi: 'भारतीय स्वतंत्रता अधिनियम (1947)',
    breadEn: 'Indian Independence Act',
    breadHi: 'भारतीय स्वतंत्रता अधिनियम',
    descEn: 'Comprehensive study guide covering the Indian Independence Act 1947, its key provisions, constitutional impact, and the birth of India and Pakistan.',
    descHi: 'भारतीय स्वतंत्रता अधिनियम 1947, इसके प्रमुख प्रावधानों, संवैधानिक प्रभाव और भारत-पाकिस्तान के जन्म को कवर करने वाली मार्गदर्शिका।',
    prompt: `Generate UPSSSC Lower Mains exam content for "Indian Independence Act 1947" (भारतीय स्वतंत्रता अधिनियम).`
  },
  {
    key: 'integration-of-princely-states',
    titleEn: 'Integration of Princely States',
    titleHi: 'देशी रियासतों का एकीकरण',
    breadEn: 'Integration of Princely States',
    breadHi: 'देशी रियासतों का एकीकरण',
    descEn: 'Comprehensive study guide covering Sardar Patel\'s role in integrating 565 princely states, Instrument of Accession, and challenges in unification.',
    descHi: '565 देशी रियासतों के एकीकरण में सरदार पटेल की भूमिका, विलय पत्र और एकीकरण में चुनौतियों को कवर करने वाली मार्गदर्शिका।',
    prompt: `Generate UPSSSC Lower Mains exam content for "Integration of Princely States" (देशी रियासतों का एकीकरण).`
  },
  {
    key: 'impact-of-british-rule-economic-administrative',
    titleEn: 'Impact of British Rule: Economic & Administrative',
    titleHi: 'ब्रिटिश शासन का प्रभाव: आर्थिक एवं प्रशासनिक',
    breadEn: 'Impact of British Rule',
    breadHi: 'ब्रिटिश शासन का प्रभाव',
    descEn: 'Comprehensive study guide covering economic drain, deindustrialization, commercialization of agriculture, land revenue systems, and administrative changes under British rule.',
    descHi: 'आर्थिक निष्कासन, विऔद्योगीकरण, कृषि का व्यावसायीकरण, भू-राजस्व प्रणालियों और ब्रिटिश शासन के तहत प्रशासनिक परिवर्तनों को कवर करने वाली मार्गदर्शिका।',
    prompt: `Generate UPSSSC Lower Mains exam content for "Impact of British Rule: Economic and Administrative" (ब्रिटिश शासन का प्रभाव: आर्थिक एवं प्रशासनिक).`
  },
  {
    key: 'role-of-press-and-western-education',
    titleEn: 'Role of Press & Western Education',
    titleHi: 'प्रेस एवं पाश्चात्य शिक्षा की भूमिका',
    breadEn: 'Press & Western Education',
    breadHi: 'प्रेस और पश्चिमी शिक्षा',
    descEn: 'Comprehensive study guide covering the role of newspapers, journals, and Western education in spreading nationalist ideas and awakening political consciousness in India.',
    descHi: 'भारत में राष्ट्रीय विचारों के प्रसार और राजनीतिक चेतना जागृत करने में समाचार पत्रों, पत्रिकाओं और पश्चिमी शिक्षा की भूमिका को कवर करने वाली मार्गदर्शिका।',
    prompt: `Generate UPSSSC Lower Mains exam content for "Role of Press and Western Education in National Awakening" (प्रेस एवं पाश्चात्य शिक्षा की भूमिका).`
  },
  {
    key: 'socio-religious-reform-movements',
    titleEn: 'Socio-Religious Reform Movements',
    titleHi: 'सामाजिक-धार्मिक सुधार आंदोलन',
    breadEn: 'Socio-Religious Reforms',
    breadHi: 'सामाजिक-धार्मिक सुधार',
    descEn: 'Comprehensive study guide covering Brahmo Samaj, Arya Samaj, Ramakrishna Mission, Theosophical Society, Aligarh Movement, and other reform movements of 19th-20th century India.',
    descHi: 'ब्रह्म समाज, आर्य समाज, रामकृष्ण मिशन, थियोसॉफिकल सोसायटी, अलीगढ़ आंदोलन और 19वीं-20वीं सदी के अन्य सुधार आंदोलनों को कवर करने वाली मार्गदर्शिका।',
    prompt: `Generate UPSSSC Lower Mains exam content for "Socio-Religious Reform Movements in 19th-20th Century India" (सामाजिक-धार्मिक सुधार आंदोलन).`
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
                <a href="../../index.html#history">History</a>
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

// ─── Gemini Prompt Builder ────────────────────────────────────────────────────

function buildPrompt(topic) {
  return `You are an expert UPSSSC Lower Mains exam content creator for Indian History. 
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
Focus on: facts most commonly asked in UP state government exams, key dates, persons, causes, effects.`;
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

// ─── Model pool: rotate across 2 models to avoid 503 overload ────────────────
const MODEL_POOL = [
  'gemini-3.5-flash',        // Gemini 3.5 Flash (primary)
  'gemini-3.1-flash-lite',   // Gemini 3.1 Flash Lite (fallback)
];


let modelIndex = 0; // global round-robin index

// ─── Main Generator ───────────────────────────────────────────────────────────

async function generateTopic(topic) {
  console.log(`\n⟳ Generating: ${topic.titleEn}...`);

  const prompt = buildPrompt(topic);

  let raw;
  const MAX_RETRIES = MODEL_POOL.length * 2; // 2 models × 2 passes = 4 attempts

  const BASE_DELAY = 5000;

  for (let attempt = 0; attempt < MAX_RETRIES; attempt++) {
    // Rotate model on each attempt
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
      // Advance global index for next topic to spread load
      modelIndex = (attempt + 1) % MODEL_POOL.length;
      break; // success
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

  // Extract JSON from response (handle markdown code blocks)
  let jsonStr = raw.trim();
  if (jsonStr.startsWith('```')) {
    jsonStr = jsonStr.replace(/^```(?:json)?\n?/, '').replace(/\n?```$/, '');
  }

  let data;
  try {
    data = JSON.parse(jsonStr);
  } catch (e) {
    // Try to extract JSON object
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

  // Build test data array for JS
  const testDataArr = (data.testQs || []).map(q => ({
    ans: q.ans,
    solEn: q.solEn,
    solHi: q.solHi
  }));

  // Build HTML sections
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
  console.log('=== UPSSSC Lower Mains History Page Generator ===');
  console.log(`Using Gemini API Key: ${API_KEY ? API_KEY.substring(0, 10) + '...' : 'NOT FOUND'}`);

  if (!API_KEY) {
    console.error('ERROR: GEMINI_API_KEY not found in .env');
    process.exit(1);
  }

  // Support RETRY_KEYS env var to re-run only specific topics
  // e.g. RETRY_KEYS=economic-aspects,political-aspects,revolt-of-1857 node scripts/gen_history_pages.js
  const retryKeys = process.env.RETRY_KEYS ? process.env.RETRY_KEYS.split(',').map(k => k.trim()) : null;
  const topicsToRun = retryKeys ? TOPICS.filter(t => retryKeys.includes(t.key)) : TOPICS;

  if (retryKeys) console.log(`Retrying only: ${retryKeys.join(', ')}`);
  console.log(`Topics to generate: ${topicsToRun.length}`);

  const failed = [];
  for (const topic of topicsToRun) {
    try {
      await generateTopic(topic);
      // Delay between API calls to avoid rate limiting
      await new Promise(r => setTimeout(r, 3000));
    } catch (err) {
      console.error(`  ✗ Failed: ${topic.key} — ${err.message}`);
      failed.push(topic.key);
    }
  }

  console.log('\n=== Generation Complete ===');
  if (failed.length > 0) {
    console.log(`Failed topics (${failed.length}): ${failed.join(', ')}`);
    console.log(`Retry with: RETRY_KEYS=${failed.join(',')} node scripts/gen_history_pages.js`);
  } else {
    console.log('All topics generated successfully! ✓');
  }
}

main().catch(console.error);
