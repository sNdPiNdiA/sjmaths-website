/**
 * UPSSSC Lower Mains Current Events Page Generator
 * Generates comprehensive content (Theory, Practice, PYQs, Test) for all 10 Current Events topics
 */

require('dotenv').config();
const { GoogleGenAI } = require('@google/genai');
const fs = require('fs');
const path = require('path');

const API_KEY = process.env.GEMINI_API_KEY;
const ai = new GoogleGenAI({ apiKey: API_KEY });

const BASE = path.join(__dirname, '..', 'upsssc-lower-mains', 'current-events');

const PREMIUM_MODELS = [
  'gemini-3.5-flash',
  'gemini-3-flash-preview',
  'gemini-2.5-flash',
  'gemini-2.5-flash-lite'
];

const TOPICS = [
  {
    key: 'important-government-schemes-policies',
    titleEn: 'Important Government Schemes & Policies',
    titleHi: 'महत्वपूर्ण सरकारी योजनाएं एवं नीतियां',
    breadEn: 'Govt Schemes',
    breadHi: 'सरकारी योजनाएं',
    descEn: 'Exhaustive study guide covering flagship schemes, welfare policies, and development initiatives of Central and UP Governments.',
    descHi: 'केंद्र और उत्तर प्रदेश सरकारों की प्रमुख योजनाओं, कल्याणकारी नीतियों और विकास पहलों को कवर करने वाली व्यापक मार्गदर्शिका।',
    prompt: 'Flagship Central government schemes (PM-Kisan, PM-Jan Dhan, Ayushman Bharat, etc.) and UP State government schemes (Kanya Sumangala, ODOP, etc.) launched recently.'
  },
  {
    key: 'national-summits-conferences-reports',
    titleEn: 'National Summits, Conferences & Reports',
    titleHi: 'राष्ट्रीय शिखर सम्मेलन, सम्मेलन एवं रिपोर्ट',
    breadEn: 'National Summits',
    breadHi: 'राष्ट्रीय सम्मेलन',
    descEn: 'Study notes on major national conferences, index reports, policy documents, and bilateral developments in India.',
    descHi: 'भारत में प्रमुख राष्ट्रीय सम्मेलनों, सूचकांक रिपोर्टों, नीतिगत दस्तावेजों और द्विपक्षीय विकास पर अध्ययन नोट्स।',
    prompt: 'Major national summits, national policy conferences, reports released by NITI Aayog and central ministries.'
  },
  {
    key: 'awards-honors-and-persons-in-news',
    titleEn: 'Awards, Honors & Persons in News',
    titleHi: 'पुरस्कार, सम्मान और समाचारों में चर्चित व्यक्ति',
    breadEn: 'Awards & Persons',
    breadHi: 'पुरस्कार व चर्चित व्यक्ति',
    descEn: 'Detailed guide to Bharat Ratna, Padma Awards, national sports honors, Nobel Prizes, and prominent individuals in recent news.',
    descHi: 'भारत रत्न, पद्म पुरस्कारों, राष्ट्रीय खेल सम्मानों, नोबेल पुरस्कारों और हाल के समाचारों में प्रमुख व्यक्तियों के लिए विस्तृत मार्गदर्शिका।',
    prompt: 'National awards (Padma, Khel Ratna, Sahitya Akademi), international awards (Nobel, Booker), and newly appointed key dignitaries or deceased personalities.'
  },
  {
    key: 'supreme-court-judgments-constitutional-developments',
    titleEn: 'Supreme Court Judgments & Constitutional Developments',
    titleHi: 'उच्चतम न्यायालय के निर्णय एवं संवैधानिक विकास',
    breadEn: 'SC Judgments',
    breadHi: 'न्यायालय के निर्णय',
    descEn: 'Exhaustive notes on landmark SC judgments, constitutional amendments, and bills in recent current affairs.',
    descHi: 'हाल के समसामयिक मामलों में मील का पत्थर साबित होने वाले सुप्रीम कोर्ट के फैसलों, संवैधानिक संशोधनों और विधेयकों पर विस्तृत नोट्स।',
    prompt: 'Significant Supreme Court judgments, key Constitutional Amendment acts, important bills passed, and legislative developments.'
  },
  {
    key: 'international-summits-g20-brics-un',
    titleEn: 'International Summits: G20, BRICS, UN',
    titleHi: 'अंतर्राष्ट्रीय शिखर सम्मेलन: G20, BRICS, UN',
    breadEn: 'Intl Summits',
    breadHi: 'अंतर्राष्ट्रीय सम्मेलन',
    descEn: 'Study guide covering G20 summits, BRICS expansion, UN conferences, COP summits, and global security developments.',
    descHi: 'G20 शिखर सम्मेलनों, ब्रिक्स विस्तार, संयुक्त राष्ट्र सम्मेलनों, सीओपी सम्मेलनों और वैश्विक सुरक्षा विकास को कवर करने वाली अध्ययन मार्गदर्शिका।',
    prompt: 'Details on international summits including G20, BRICS, SCO, ASEAN, G7, United Nations General Assembly, and COP climate summits.'
  },
  {
    key: 'bilateral-agreements-and-international-relations',
    titleEn: 'Bilateral Agreements & International Relations',
    titleHi: 'द्विपक्षीय समझौते और अंतर्राष्ट्रीय संबंध',
    breadEn: 'Bilateral & IR',
    breadHi: 'द्विपक्षीय संबंध',
    descEn: 'Study notes on India\'s foreign relations, bilateral trade pacts, defense agreements, and diplomatic visits.',
    descHi: 'भारत के विदेश संबंधों, द्विपक्षीय व्यापार समझौतों, रक्षा समझौतों और राजनयिक यात्राओं पर अध्ययन नोट्स।',
    prompt: 'India\'s bilateral relations, major pacts, defense deals, MoU signatures, joint military exercises, and neighborhood first policy.'
  },
  {
    key: 'global-indices-and-reports',
    titleEn: 'Global Indices & Reports',
    titleHi: 'वैश्विक सूचकांक और रिपोर्ट',
    breadEn: 'Global Indices',
    breadHi: 'वैश्विक सूचकांक',
    descEn: 'Detailed guide to India\'s ranking in global indices, environmental reports, and human development surveys.',
    descHi: 'वैश्विक सूचकांकों, पर्यावरण रिपोर्टों और मानव विकास सर्वेक्षणों में भारत की रैंकिंग के लिए विस्तृत मार्गदर्शिका।',
    prompt: 'India\'s rank and score in important global indexes (Human Development Index, Hunger Index, Press Freedom, Corruption Perception, etc.) and issuing organizations.'
  },
  {
    key: 'important-sports-events-and-trophies',
    titleEn: 'Important Sports Events & Trophies',
    titleHi: 'महत्वपूर्ण खेल आयोजन और ट्रॉफियां',
    breadEn: 'Sports & Events',
    breadHi: 'खेल व ट्रॉफियां',
    descEn: 'Comprehensive notes on Olympics, Asian Games, ICC tournaments, Grand Slams, and national sports achievements.',
    descHi: 'ओलंपिक, एशियाई खेलों, आईसीसी टूर्नामेंटों, ग्रैंड स्लैम और राष्ट्रीय खेल उपलब्धियों पर व्यापक नोट्स।',
    prompt: 'Major sports current affairs: Olympics, Paralympics, Asian Games, National Games, Cricket World Cups, Grand Slams, and state-level sport initiatives.'
  },
  {
    key: 'recent-isro-drdo-missions-tech-developments',
    titleEn: 'Recent ISRO, DRDO Missions & Tech Developments',
    titleHi: 'हालिया ISRO, DRDO मिशन और तकनीकी विकास',
    breadEn: 'ISRO & DRDO',
    breadHi: 'इसरो व डीआरडीओ',
    descEn: 'Exhaustive notes on space missions (Chandrayaan, Aditya), missile defense tests, and technological breakthroughs.',
    descHi: 'अंतरिक्ष अभियानों (चंद्रयान, आदित्य), मिसाइल रक्षा परीक्षणों और तकनीकी सफलताओं पर विस्तृत नोट्स।',
    prompt: 'Recent satellite launches by ISRO (Chandrayaan-3, Aditya-L1, Gaganyaan updates), defense equipment and missile tests by DRDO, AI developments.'
  },
  {
    key: 'economic-updates-budgets-and-rbi-policies',
    titleEn: 'Economic Updates, Budgets & RBI Policies',
    titleHi: 'आर्थिक अपडेट, बजट एवं RBI नीतियां',
    breadEn: 'Economic Updates',
    breadHi: 'आर्थिक अपडेट व बजट',
    descEn: 'Study guide covering Union Budget, UP Budget, Economic Survey, repo rate changes, and banking updates.',
    descHi: 'केंद्रीय बजट, यूपी बजट, आर्थिक सर्वेक्षण, रेपो दर में बदलाव और बैंकिंग अपडेट को कवर करने वाली अध्ययन मार्गदर्शिका।',
    prompt: 'Union Budget highlights, UP State Budget highlights, Economic Survey highlights, monetary policy decisions of RBI, GDP growth forecasts.'
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
  return `You are an expert UPSSSC Lower Mains exam content creator for Current Events (समसामयिक घटनाएँ).
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
- Include names of awards, persons, summits, dates, schemes, and relevant statistics.

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

  console.log(`  ✓ Written: current-events/${topic.key}/index.html (${Math.round(html.length / 1024)} KB)`);
}

async function main() {
  console.log('=== UPSSSC Lower Mains Current Events Page Generator ===');
  
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

  console.log('\n=== Current Events Generation Complete ===');
  if (failed.length > 0) {
    console.log(`Failed topics (${failed.length}): ${failed.join(', ')}`);
  }
}

main().catch(console.error);
