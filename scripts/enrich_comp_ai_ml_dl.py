import os
import re

def build_ai_theory_html():
    return """<div class="tab-content" id="tab-theory" style="display:block">

<!-- Card 1: Mind Map -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">Mind Map: Artificial Intelligence Concepts, Classification &amp; Ecosystem</span>
    <span class="lang-hi">माइंड मैप: आर्टिफिशियल इंटेलिजेंस (AI) अवधारणाएं, वर्गीकरण एवं तंत्र</span>
  </div>
  <div class="lang-en">
    <div class="mermaid">
graph TD
    A[Artificial Intelligence AI] --> B[Foundational Concepts]
    A --> C[Classification & Types]
    A --> D[Core Subfields & Technologies]
    A --> E[Generative AI & LLMs]
    A --> F[National & UP AI Initiatives]

    B --> B1[Father of AI: John McCarthy 1956 Dartmouth]
    B --> B2[Alan Turing: Turing Test 1950 & Can Machines Think]
    B --> B3[Knowledge Base + Inference Engine Expert Systems]

    C --> C1[By Capability: ANI Narrow, AGI General, ASI Super]
    C --> C2[By Function: Reactive, Limited Memory, Theory of Mind, Self-Aware]

    D --> D1[Machine Learning ML: Statistical Patterns & Algorithms]
    D --> D2[Deep Learning DL: Multi-layer Neural Networks ANN/CNN/RNN]
    D --> D3[Natural Language Processing NLP: Text & Speech Understanding]
    D --> D4[Computer Vision & Robotics: Image Recognition & Autonomous Systems]

    E --> E1[Transformers Attention Mechanism: GPT-4, Gemini, Claude, LLaMA]
    E --> E2[Applications: Multimodal, Code Generation, Conversational AI]

    F --> F1[National: NITI Aayog #AIforAll, AIRAWAT C-DAC Pune, Bhashini]
    F --> F2[Uttar Pradesh: Lucknow AI City, Trinetra AI App for Policing]
    </div>
  </div>
  <div class="lang-hi">
    <div class="mermaid">
graph TD
    A[आर्टिफिशियल इंटेलिजेंस AI] --> B[मूलभूत अवधारणाएं एवं इतिहास]
    A --> C[वर्गीकरण एवं प्रकार]
    A --> D[प्रमुख उप-क्षेत्र एवं तकनीकें]
    A --> E[जेनेरेटिव AI एवं LLM मॉडल]
    A --> F[राष्ट्रीय एवं उत्तर प्रदेश AI पहलें]

    B --> B1[AI के जनक: जॉन मैकार्थी 1956 डार्टमाउथ सम्मेलन]
    B --> B2[एलन ट्यूरिंग: ट्यूरिंग टेस्ट 1950 एवं मशीन चिंतन]
    B --> B3[नॉलेज बेस + इन्फरेंस इंजन विशेषज्ञ प्रणाली]

    C --> C1[क्षमता आधार: ANI संकीर्ण, AGI सामान्य, ASI अतिबुद्धिमत्ता]
    C --> C2[कार्य आधार: रिएक्टिव, लिमिटेड मेमोरी, थ्योरी ऑफ माइंड, आत्म-जागरूक]

    D --> D1[मशीन लर्निंग: सांख्यिकीय पैटर्न एवं कलन विधि]
    D --> D2[डीप लर्निंग: बहु-स्तरीय न्यूरल नेटवर्क ANN/CNN/RNN]
    D --> D3[प्राकृतिक भाषा प्रसंस्करण NLP: भाषा व वाक पहचान]
    D --> D4[कंप्यूटर विजन व रोबोटिक्स: छवि पहचान व स्वायत्त प्रणाली]

    E --> E1[ट्रांसफॉर्मर अटेंशन मॉडल: GPT-4, जेमिनी, क्लॉड, लामा]
    E --> E2[अनुप्रयोग: मल्टीमॉडल, कोड निर्माण, संवादात्मक AI]

    F --> F1[राष्ट्रीय: नीति आयोग #AIforAll, ऐरावत C-DAC पुणे, भाषिणी]
    F --> F2[उत्तर प्रदेश: लखनऊ AI सिटी, त्रिनेत्र 2.0 पुलिसिंग ऐप]
    </div>
  </div>
</div>

<!-- Card 2: Foundational Concepts & Historical Milestones -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">1. Foundational Concepts &amp; Historical Milestones of AI</span>
    <span class="lang-hi">1. आर्टिफिशियल इंटेलिजेंस की मूलभूत अवधारणाएं एवं ऐतिहासिक मील के पत्थर</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Definition of AI (कृत्रिम बुद्धिमत्ता):</strong>
          <br>&bull; A branch of computer science focused on creating machines capable of simulating human intelligence—including learning, reasoning, problem-solving, perception, and natural language understanding.
          <br>&bull; Coined by <strong>John McCarthy</strong> in <strong>1956</strong> at the historic <em>Dartmouth Conference</em> (Dartmouth College, Hanover, New Hampshire), earning him the title <strong>"Father of Artificial Intelligence"</strong>.</span>
        <span class="lang-hi"><strong>AI की परिभाषा:</strong>
          <br>&bull; कंप्यूटर विज्ञान की वह शाखा जो ऐसी मशीनों के निर्माण से संबंधित है जो मानवीय बुद्धिमत्ता—जैसे सीखना (Learning), तर्क (Reasoning), समस्या-समाधान, प्रत्यक्षीकरण (Perception) और भाषा समझने का अनुकरण कर सकें।
          <br>&bull; <strong>1956</strong> में <em>डार्टमाउथ सम्मेलन</em> में <strong>जॉन मैकार्थी</strong> द्वारा सर्वप्रथम 'आर्टिफिशियल इंटेलिजेंस' शब्द गढ़ा गया, जिसके कारण उन्हें <strong>"AI का जनक"</strong> कहा जाता है।</span>
      </li>
      <li>
        <span class="lang-en"><strong>The Turing Test (1950 - Alan Turing):</strong>
          <br>&bull; Proposed by British mathematician <strong>Alan Mathison Turing</strong> in his paper <em>"Computing Machinery and Intelligence"</em>.
          <br>&bull; A test of a machine's ability to exhibit intelligent behavior equivalent to, or indistinguishable from, that of a human. If an interrogator cannot reliably tell whether a conversation is with a human or a machine, the machine passes the test.</span>
        <span class="lang-hi"><strong>ट्यूरिंग टेस्ट (1950 - एलन ट्यूरिंग):</strong>
          <br>&bull; ब्रिटिश गणितज्ञ <strong>एलन ट्यूरिंग</strong> द्वारा शोध पत्र <em>"कंप्यूटिंग मशीनरी एंड इंटेलिजेंस"</em> में प्रतिपादित।
          <br>&bull; यह मापने की विधि है कि क्या कोई मशीन मानव जैसी बुद्धिमत्ता से संवाद कर सकती है। यदि कोई मूल्यांकनकर्ता यह भेद न कर सके कि उत्तर मानव दे रहा है या मशीन, तो मशीन ट्यूरिंग टेस्ट पास मानी जाती है।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Milestones in AI History:</strong>
          <br>&bull; <strong>Logic Theorist (1955-56):</strong> Developed by Allen Newell and Herbert Simon; recognized as the first running AI program.
          <br>&bull; <strong>ELIZA (1966):</strong> Joseph Weizenbaum developed the first conversational chatbot at MIT simulating a psychotherapist.
          <br>&bull; <strong>Deep Blue (1997, IBM):</strong> Defeated World Chess Champion Garry Kasparov; world's first supercomputer victory over reigning human champion.
          <br>&bull; <strong>Watson (2011, IBM):</strong> Won the quiz show <em>Jeopardy!</em> against top human champions using natural language processing.
          <br>&bull; <strong>AlphaGo (2016, DeepMind):</strong> Defeated world Go champion Lee Sedol using deep reinforcement learning and Monte Carlo tree search.</span>
        <span class="lang-hi"><strong>AI इतिहास के ऐतिहासिक पड़ाव:</strong>
          <br>&bull; <strong>लॉजिक थ्योरिस्ट (1955-56):</strong> एलन नेवेल और हर्बर्ट साइमन द्वारा विकसित; विश्व का प्रथम कार्यरत AI प्रोग्राम।
          <br>&bull; <strong>एलीजा (ELIZA - 1966):</strong> MIT में जोसेफ वेइजनबॉम द्वारा विकसित प्रथम प्राकृतिक भाषा चैटबॉट।
          <br>&bull; <strong>डीप ब्लू (1997, IBM):</strong> विश्व शतरंज चैंपियन गैरी कास्पारोव को हराने वाला पहला सुपरकंप्यूटर।
          <br>&bull; <strong>आईबीएम वॉटसन (2011):</strong> क्विज शो <em>जियोपार्डी!</em> में शीर्ष मानव चैंपियनों को पराजित करने वाला संज्ञानात्मक सिस्टम।
          <br>&bull; <strong>अल्फागो (2016, DeepMind):</strong> 19x19 बोर्ड गेम 'गो' (Go) के विश्व चैंपियन ली सेडोल को हराने वाला डीप रीइन्फोर्समेंट लर्निंग सिस्टम।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 3: Classification of AI -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">2. Classification &amp; Types of Artificial Intelligence</span>
    <span class="lang-hi">2. आर्टिफिशियल इंटेलिजेंस का वर्गीकरण एवं प्रकार</span>
  </div>
  <div class="content-block">
    <p>
      <span class="lang-en">AI is classified into two primary frameworks: <strong>By Capability</strong> and <strong>By Functionality</strong>.</span>
      <span class="lang-hi">AI को दो प्रमुख श्रेणियों में वर्गीकृत किया जाता है: <strong>क्षमता के आधार पर</strong> एवं <strong>कार्यप्रणाली के आधार पर</strong>।</span>
    </p>
    <table class="comparison-table">
      <thead>
        <tr>
          <th><span class="lang-en">Category</span><span class="lang-hi">श्रेणी</span></th>
          <th><span class="lang-en">Type</span><span class="lang-hi">प्रकार</span></th>
          <th><span class="lang-en">Core Characteristics</span><span class="lang-hi">प्रमुख विशेषताएं</span></th>
          <th><span class="lang-en">Key Examples</span><span class="lang-hi">प्रमुख उदाहरण</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td rowspan="3"><strong><span class="lang-en">By Capability</span><span class="lang-hi">क्षमता आधार पर</span></strong></td>
          <td><strong>ANI (Narrow / Weak AI)</strong></td>
          <td><span class="lang-en">Dedicated to one specific task; cannot perform outside its domain. All present-day AI is ANI.</span><span class="lang-hi">केवल एक विशिष्ट कार्य करने में सक्षम। वर्तमान में मौजूद सभी AI तकनीकें ANI हैं।</span></td>
          <td>Siri, Google Assistant, Alexa, Chess engines, Netflix recommendations, Spam filters</td>
        </tr>
        <tr>
          <td><strong>AGI (General / Strong AI)</strong></td>
          <td><span class="lang-en">Human-level intellectual ability; can learn, reason, and solve diverse problems across any domain. Currently hypothetical.</span><span class="lang-hi">मानव के समान बौद्धिक क्षमता। किसी भी क्षेत्र में स्वतंत्र रूप से सीखने व निर्णय लेने में सक्षम (वर्तमान में सैद्धांतिक)।</span></td>
          <td>Human-level artificial general intelligence (In research phase)</td>
        </tr>
        <tr>
          <td><strong>ASI (Artificial Superintelligence)</strong></td>
          <td><span class="lang-en">Surpasses human cognitive capacity across all domains, including creativity, wisdom, and social skills. Future hypothetical state.</span><span class="lang-hi">मानव मस्तिष्क से कई गुना तीव्र व सक्षम बुद्धिमत्ता, जो सभी क्षेत्रों में मानव को पछाड़ दे (काल्पनिक/भविष्य)।</span></td>
          <td>Theoretical Singularity concept</td>
        </tr>
        <tr>
          <td rowspan="4"><strong><span class="lang-en">By Functionality</span><span class="lang-hi">कार्यप्रणाली आधार पर</span></strong></td>
          <td><strong>Reactive Machines (प्रतिक्रियाशील)</strong></td>
          <td><span class="lang-en">No memory; cannot store past experiences. Always produces identical output for identical input.</span><span class="lang-hi">कोई मेमोरी नहीं होती; पिछले अनुभवों से नहीं सीख सकता। प्रत्येक स्थिति पर सीधे प्रतिक्रिया देता है।</span></td>
          <td>IBM Deep Blue, Google AlphaGo</td>
        </tr>
        <tr>
          <td><strong>Limited Memory (सीमित स्मृति)</strong></td>
          <td><span class="lang-en">Stores past observations for a short period to make decisions; learns from historical training data.</span><span class="lang-hi">अल्पकाल के लिए विगत डेटा संग्रहीत कर निर्णय लेता है। अधिकांश आधुनिक AI इसी श्रेणी में आते हैं।</span></td>
          <td>Self-driving cars (Tesla Autopilot), ChatGPT, Apple FaceID</td>
        </tr>
        <tr>
          <td><strong>Theory of Mind (मन का सिद्धांत)</strong></td>
          <td><span class="lang-en">Understands human emotions, beliefs, intents, and social interactions. Currently in early academic research.</span><span class="lang-hi">मानवीय भावनाओं, विश्वासों, अपेक्षाओं व सामाजिक व्यवहार को समझने में सक्षम (अनुसंधान चरण)।</span></td>
          <td>Social robotics (Sophia humanoid in limited demos)</td>
        </tr>
        <tr>
          <td><strong>Self-Aware AI (आत्म-जागरूक)</strong></td>
          <td><span class="lang-en">Possesses its own consciousness, feelings, self-awareness, and emotions. Strictly theoretical concept.</span><span class="lang-hi">स्वयं की चेतना, आत्म-बोध एवं भावनाएं रखने वाली मशीन (पूर्णतः काल्पनिक)।</span></td>
          <td>Science fiction concepts (JARVIS, Skynet)</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- Card 4: Subfields & Key Technologies of AI -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">3. Core Subfields &amp; Technologies of Artificial Intelligence</span>
    <span class="lang-hi">3. आर्टिफिशियल इंटेलिजेंस के मुख्य उप-क्षेत्र एवं तकनीकें</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Natural Language Processing (NLP - प्राकृतिक भाषा प्रसंस्करण):</strong>
          <br>&bull; Enables computers to read, interpret, analyze, and generate human language (text and speech).
          <br>&bull; <strong>Key Tasks:</strong> Tokenization (splitting sentences into words), Stemming/Lemmatization (finding root words), Part-of-Speech (POS) Tagging, Named Entity Recognition (NER), Sentiment Analysis, and Machine Translation (e.g., Google Translate, Bhashini).</span>
        <span class="lang-hi"><strong>प्राकृतिक भाषा प्रसंस्करण (NLP):</strong>
          <br>&bull; कंप्यूटर को मानव भाषा (लिखित व मौखिक) को पढ़ने, समझने, विश्लेषण करने और उत्पन्न करने में सक्षम बनाता है।
          <br>&bull; <strong>प्रमुख कार्य:</strong> टोकनाइजेशन (वाक्य को शब्दों में तोड़ना), लेमेटाइजेशन (मूल शब्द खोजना), POS टैगिंग, भावना विश्लेषण (Sentiment Analysis) एवं मशीन अनुवाद।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Computer Vision (कंप्यूटर विज़न):</strong>
          <br>&bull; Enables machines to derive meaningful information from digital images, videos, and visual inputs.
          <br>&bull; <strong>Techniques:</strong> Image Classification, Object Detection (YOLO, R-CNN), Facial Recognition, Optical Character Recognition (OCR), and Semantic Segmentation.
          <br>&bull; <strong>Applications:</strong> Autonomous vehicles, biometric passport gates, medical radiology (MRI/CT analysis), UP Police surveillance.</span>
        <span class="lang-hi"><strong>कंप्यूटर विज़न:</strong>
          <br>&bull; डिजिटल छवियों और वीडियो से दृश्य जानकारी को पहचानने और व्याख्या करने की क्षमता।
          <br>&bull; <strong>प्रमुख तकनीकें:</strong> ऑब्जेक्ट डिटेक्शन, चेहरे की पहचान (Facial Recognition), ऑप्टिकल कैरेक्टर रिकॉग्निशन (OCR) एवं ऑटोमैटिक नंबर प्लेट पहचान (ANPR)।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Expert Systems (विशेषज्ञ प्रणालियाँ):</strong>
          <br>&bull; Computer systems that emulate the decision-making ability of a human expert in a specialized domain.
          <br>&bull; <strong>Core Architecture (Two Parts):</strong>
            <br>&nbsp;&nbsp;1. <strong>Knowledge Base:</strong> Repository of domain rules, facts, and heuristic data.
            <br>&nbsp;&nbsp;2. <strong>Inference Engine:</strong> Reasoning mechanism that applies logical rules (IF-THEN) to deduce new information.
          <br>&bull; <strong>Classic Examples:</strong> MYCIN (bacterial infection diagnosis), DENDRAL (chemical molecular analysis), PROSPECTOR (geological mineral exploration).</span>
        <span class="lang-hi"><strong>विशेषज्ञ प्रणालियाँ (Expert Systems):</strong>
          <br>&bull; वे कंप्यूटर सॉफ्टवेयर जो किसी विशिष्ट क्षेत्र में मानव विशेषज्ञ के निर्णय लेने की क्षमता का अनुकरण करते हैं।
          <br>&bull; <strong>दो मुख्य घटक:</strong>
            <br>&nbsp;&nbsp;1. <strong>नॉलेज बेस (Knowledge Base):</strong> नियमों, तथ्यों और अनुभवों का भंडार।
            <br>&nbsp;&nbsp;2. <strong>इन्फरेंस इंजन (Inference Engine):</strong> तार्किक नियमों (IF-THEN) को लागू कर निष्कर्ष निकालने वाला मस्तिष्क।
          <br>&bull; <strong>प्रमुख उदाहरण:</strong> MYCIN (चिकित्सा निदान), DENDRAL (रसायन शास्त्र), CADUCEUS।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Generative AI &amp; Large Language Models (LLMs):</strong>
          <br>&bull; Powered by deep neural network architectures called <strong>Transformers</strong> (introduced in 2017 Google paper <em>"Attention Is All You Need"</em>).
          <br>&bull; Capable of generating text, images (DALL-E, Midjourney, Stable Diffusion), audio, and code.
          <br>&bull; <strong>Major LLMs:</strong> GPT-4 / ChatGPT (OpenAI), Gemini (Google), Claude (Anthropic), LLaMA (Meta Open Source).
          <br>&bull; <strong>Key Terms:</strong> <em>Prompt</em> (user input instruction), <em>Token</em> (basic unit of text processed by model, ~4 characters), <em>Hallucination</em> (model generating confident but factually incorrect outputs), <em>Fine-tuning</em> (adapting a pre-trained model to specific tasks).</span>
        <span class="lang-hi"><strong>जेनेरेटिव AI एवं लार्ज लैंग्वेज मॉडल (LLM):</strong>
          <br>&bull; <strong>ट्रांसफॉर्मर आर्किटेक्चर</strong> (2017 का शोध पत्र <em>"अटेंशन इज ऑल यू नीड"</em>) पर आधारित, जो संदर्भ (Context) को समानांतर रूप से समझता है।
          <br>&bull; नया टेक्स्ट, चित्र, कोड, संगीत और वीडियो बनाने में सक्षम।
          <br>&bull; <strong>प्रमुख मॉडल:</strong> चैटजीपीटी (OpenAI), जेमिनी (गूगल), क्लॉड (एंथ्रोपिक), लामा (मेटा)।
          <br>&bull; <strong>महत्वपूर्ण शब्दावली:</strong> <em>प्रॉम्प्ट</em> (निर्देश), <em>टोकन</em> (प्रोसेसिंग इकाई), <em>हैलुसिनेशन</em> (AI द्वारा आत्मविश्वास से गलत तथ्य प्रस्तुत करना), <em>RAG</em> (बाहरी ज्ञान भंडार जोड़ना)।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 5: AI Initiatives in India & Uttar Pradesh -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">4. AI Initiatives in India &amp; Uttar Pradesh (Exam Focus)</span>
    <span class="lang-hi">4. भारत एवं उत्तर प्रदेश में AI पहलें (परीक्षा विशेष)</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>National Strategy for AI (#AIforAll):</strong>
          <br>&bull; Formulated by <strong>NITI Aayog</strong> in June 2018; prioritizes healthcare, agriculture, education, smart cities, and smart mobility.
          <br>&bull; Focuses on dual approach: Core research (International Centres of Transformational AI - ICTAI) and Applied research (Centres of Research Excellence - CORE).</span>
        <span class="lang-hi"><strong>राष्ट्रीय AI रणनीति (#AIforAll):</strong>
          <br>&bull; <strong>नीति आयोग</strong> द्वारा जून 2018 में जारी; स्वास्थ्य, कृषि, शिक्षा, स्मार्ट सिटी और मोबिलिटी में समावेशी विकास पर केंद्रित।
          <br>&bull; भारत को 'AI गैराज' के रूप में स्थापित करने का लक्ष्य।</span>
      </li>
      <li>
        <span class="lang-en"><strong>AIRAWAT (C-DAC, Pune):</strong>
          <br>&bull; <strong>AI Research, Analytics and Knowledge Assimilation Platform</strong>: India's fastest AI supercomputer installed at C-DAC Pune under the National AI Mission.
          <br>&bull; Ranked <strong>75th</strong> in the Global TOP500 Supercomputers list in 2023.</span>
        <span class="lang-hi"><strong>ऐरावत (AIRAWAT - C-DAC पुणे):</strong>
          <br>&bull; भारत का सबसे तेज AI सुपरकंप्यूटर, जिसे नेशनल AI प्रोग्राम के तहत C-DAC पुणे में स्थापित किया गया है।
          <br>&bull; वर्ष 2023 में वैश्विक टॉप 500 सुपरकंप्यूटर सूची में <strong>75वां स्थान</strong> प्राप्त किया।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Digital India Bhashini (भाषिणी):</strong>
          <br>&bull; Launched in July 2022 by Prime Minister Narendra Modi; an AI-powered language translation platform enabling easy access to digital services in 22 Indian languages.
          <br>&bull; Powers speech-to-text, text-to-speech, and machine translation across Indian dialects using crowdsourced voice data via <em>Bhasha Daan</em>.</span>
        <span class="lang-hi"><strong>डिजिटल इंडिया भाषिणी (Bhashini):</strong>
          <br>&bull; जुलाई 2022 में प्रधानमंत्री द्वारा लॉन्च किया गया AI-आधारित भाषा अनुवाद प्लेटफॉर्म।
          <br>&bull; 22 आधिकारिक भारतीय भाषाओं में डिजिटल सेवाएं, वाक्-से-टेक्स्ट और अनुवाद उपलब्ध कराता है। <em>भाषा दान</em> पोर्टल के माध्यम से डेटा संग्रह।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Uttar Pradesh AI Initiatives:</strong>
          <br>&bull; <strong>India's First AI City in Lucknow:</strong> Uttar Pradesh Electronics Corporation (UPEC) is developing India's premier AI City in <strong>Nadarganj, Lucknow</strong> spread over ~40 acres to house AI tech giants, startups, and research hubs.
          <br>&bull; <strong>Trinetra 2.0 (UP Police):</strong> An AI and facial recognition app used by UP Police with a database of millions of criminal records for instant face-matching and crime detection.
          <br>&bull; <strong>AI in UP Agriculture:</strong> AI-based crop pest detection and precision irrigation piloted via Krishi Vigyan Kendras (KVKs).</span>
        <span class="lang-hi"><strong>उत्तर प्रदेश की प्रमुख AI पहलें:</strong>
          <br>&bull; <strong>देश की पहली AI सिटी (लखनऊ):</strong> यूपी इलेक्ट्रॉनिक्स कॉर्पोरेशन (UPEC) द्वारा <strong>नादरगंज, लखनऊ</strong> में ~40 एकड़ में देश की पहली 'AI सिटी' विकसित की जा रही है।
          <br>&bull; <strong>त्रिनेत्र 2.0 (यूपी पुलिस):</strong> उत्तर प्रदेश पुलिस का AI एवं फेशियल रिकॉग्निशन ऐप, जो अपराधियों के चेहरे की पहचान और अपराध नियंत्रण में उपयोग होता है।
          <br>&bull; <strong>कृषि में AI:</strong> उप्र के कृषि विज्ञान केंद्रों (KVK) द्वारा कीट-पहचान एवं फसल निगरानी में AI प्रणालियों का उपयोग।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 6: One-Liner Exam Facts -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">Key One-Liner Exam Facts (UPSSSC Computer Special)</span>
    <span class="lang-hi">महत्वपूर्ण वन-लाइनर परीक्षा तथ्य (UPSSSC कंप्यूटर विशेष)</span>
  </div>
  <div class="content-block">
    <table class="comparison-table">
      <thead>
        <tr>
          <th><span class="lang-en">Exam Question Topic</span><span class="lang-hi">परीक्षा प्रश्न विषय</span></th>
          <th><span class="lang-en">Core Exam Fact &amp; Details</span><span class="lang-hi">महत्वपूर्ण तथ्य एवं विवरण</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="lang-en">Father of Artificial Intelligence</span><span class="lang-hi">AI के जनक</span></td>
          <td><span class="lang-en"><strong>John McCarthy</strong> (coined term in 1956 at Dartmouth Conference).</span><span class="lang-hi"><strong>जॉन मैकार्थी</strong> (1956 में डार्टमाउथ सम्मेलन में नामकरण)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Creator of Turing Test for Machine Intelligence</span><span class="lang-hi">ट्यूरिंग टेस्ट के प्रतिपादक</span></td>
          <td><span class="lang-en"><strong>Alan Turing</strong> (1950, British mathematician and computer pioneer).</span><span class="lang-hi"><strong>एलन ट्यूरिंग</strong> (1950, कंप्यूटर विज्ञान के जनक)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">First AI Programming Language</span><span class="lang-hi">AI की प्रथम प्रोग्रामिंग भाषा</span></td>
          <td><span class="lang-en"><strong>LISP</strong> (List Processing, developed by John McCarthy in 1958) and <strong>PROLOG</strong> (Programming in Logic, 1972).</span><span class="lang-hi"><strong>LISP</strong> (1958, जॉन मैकार्थी) एवं <strong>PROLOG</strong> (1972, कोलमेरौर)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Two Components of an Expert System</span><span class="lang-hi">विशेषज्ञ प्रणाली के दो मुख्य घटक</span></td>
          <td><span class="lang-en"><strong>Knowledge Base</strong> (stored domain rules) and <strong>Inference Engine</strong> (reasoning brain).</span><span class="lang-hi"><strong>नॉलेज बेस</strong> (तथ्यों का भंडार) एवं <strong>इन्फरेंस इंजन</strong> (तार्किक मस्तिष्क)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Category of AI representing current systems like Siri, Alexa, ChatGPT</span><span class="lang-hi">वर्तमान AI प्रणालियों (Siri, Alexa) की श्रेणी</span></td>
          <td><span class="lang-en"><strong>ANI</strong> (Artificial Narrow Intelligence / Weak AI).</span><span class="lang-hi"><strong>ANI</strong> (संकीर्ण या कमजोर AI)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">First Chatbot in AI History</span><span class="lang-hi">AI इतिहास का पहला चैटबॉट</span></td>
          <td><span class="lang-en"><strong>ELIZA</strong> (1966, Joseph Weizenbaum at MIT).</span><span class="lang-hi"><strong>एलीजा (ELIZA)</strong> (1966, जोसेफ वेइजनबॉम, MIT)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Supercomputer that defeated Garry Kasparov in Chess</span><span class="lang-hi">शतरंज में गैरी कास्पारोव को हराने वाला सुपरकंप्यूटर</span></td>
          <td><span class="lang-en"><strong>Deep Blue</strong> (IBM, 1997).</span><span class="lang-hi"><strong>डीप ब्लू</strong> (IBM, 1997)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Neural Architecture underlying modern LLMs</span><span class="lang-hi">आधुनिक LLM का आधारभूत आर्किटेक्चर</span></td>
          <td><span class="lang-en"><strong>Transformer</strong> Architecture (Self-Attention mechanism, 2017).</span><span class="lang-hi"><strong>ट्रांसफॉर्मर</strong> (Transformer, अटेंशन मैकेनिज्म, 2017)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">India's Fastest AI Supercomputer</span><span class="lang-hi">भारत का सबसे तेज AI सुपरकंप्यूटर</span></td>
          <td><span class="lang-en"><strong>AIRAWAT</strong> (installed at C-DAC, Pune).</span><span class="lang-hi"><strong>ऐरावत (AIRAWAT)</strong> (C-DAC, पुणे में स्थापित)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">City in Uttar Pradesh selected to build India's first AI City</span><span class="lang-hi">देश की पहली AI सिटी हेतु चयनित उप्र का शहर</span></td>
          <td><span class="lang-en"><strong>Lucknow</strong> (Nadarganj area, developed by UP Electronics Corporation).</span><span class="lang-hi"><strong>लखनऊ</strong> (नादरगंज, यूपी इलेक्ट्रॉनिक्स कॉर्पोरेशन द्वारा विकसित)।</span></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

</div>"""

def build_ml_theory_html():
    return """<div class="tab-content" id="tab-theory" style="display:block">

<!-- Card 1: Mind Map -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">Mind Map: Machine Learning Paradigms, Algorithms &amp; Lifecycle</span>
    <span class="lang-hi">माइंड मैप: मशीन लर्निंग प्रतिमान, कलन विधियां एवं जीवनचक्र</span>
  </div>
  <div class="lang-en">
    <div class="mermaid">
graph TD
    A[Machine Learning ML] --> B[Foundational Concepts]
    A --> C[Three Core ML Paradigms]
    A --> D[Evaluation & Performance Metrics]
    A --> E[Underfitting vs Overfitting]
    A --> F[Tools & Real-World Use Cases]

    B --> B1[Arthur Samuel 1959: Learning without explicit programming]
    B --> B2[Tom Mitchell 1997: Task T, Performance P, Experience E]

    C --> C1[Supervised Learning: Labeled Data | Classification & Regression]
    C --> C2[Unsupervised Learning: Unlabeled Data | Clustering & Dimensionality Reduction]
    C --> C3[Reinforcement Learning: Agent + Environment | Reward & Penalty | Q-Learning]

    D --> D1[Confusion Matrix: TP, TN, FP Type I, FN Type II]
    D --> D2[Metrics: Accuracy, Precision, Recall, F1-Score Harmonic Mean]
    D --> D3[Regression Metrics: Mean Squared Error MSE, R2 Score]

    E --> E1[Underfitting: High Bias, Poor Train & Test Performance]
    E --> E2[Overfitting: High Variance, High Train but Poor Test]
    E --> E3[Remedies: Cross-Validation, Regularization L1/L2, Pruning]

    F --> F1[Libraries: Scikit-Learn, Pandas, NumPy, SciPy]
    F --> F2[Applications: Fraud Detection, Spam Filters, Credit Scoring, Weather]
    </div>
  </div>
  <div class="lang-hi">
    <div class="mermaid">
graph TD
    A[मशीन लर्निंग ML] --> B[मूलभूत अवधारणाएं]
    A --> C[तीन प्रमुख ML प्रतिमान]
    A --> D[मूल्यांकन एवं प्रदर्शन मानक]
    A --> E[अंडरफिटिंग बनाम ओवरफिटिंग]
    A --> F[उपकरण एवं व्यावहारिक अनुप्रयोग]

    B --> B1[आर्थर सैमुअल 1959: बिना स्पष्ट कोडिंग के सीखने की क्षमता]
    B --> B2[टॉम मिशेल 1997: कार्य T, प्रदर्शन P, अनुभव E]

    C --> C1[सुपरवाइज्ड लर्निंग: लेबल युक्त डेटा | वर्गीकरण एवं प्रतिगमन]
    C --> C2[अनसुपरवाइज्ड लर्निंग: बिना लेबल डेटा | क्लस्टरिंग एवं आयाम न्यूनीकरण]
    C --> C3[रीइन्फोर्समेंट लर्निंग: एजेंट + वातावरण | पुरस्कार एवं दंड | Q-लर्निंग]

    D --> D1[कन्फ्यूजन मैट्रिक्स: TP, TN, FP टाइप I एरर, FN टाइप II एरर]
    D --> D2[मानक: एक्यूरेसी, प्रिसिजन, रिकॉल, F1-स्कोर हरात्मक माध्य]
    D --> D3[प्रतिगमन मानक: MSE माध्य वर्ग त्रुटि, R2 स्कोर]

    E --> E1[अंडरफिटिंग: उच्च बायस, प्रशिक्षण व टेस्ट दोनों में खराब]
    E --> E2[ओवरफिटिंग: उच्च विचरण, प्रशिक्षण में उत्तम परंतु टेस्ट में खराब]
    E --> E3[उपाय: क्रॉस-वैलिडेशन, रेगुलराइजेशन L1/L2, प्रूनिंग]

    F --> F1[लाइब्रेरी: Scikit-Learn, Pandas, NumPy, SciPy]
    F --> F2[अनुप्रयोग: धोखाधड़ी पहचान, स्पैम फिल्टर, क्रेडिट स्कोर, मौसम]
    </div>
  </div>
</div>

<!-- Card 2: Core Concepts of Machine Learning -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">1. Foundational Concepts of Machine Learning</span>
    <span class="lang-hi">1. मशीन लर्निंग की मूलभूत अवधारणाएं</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Definition of Machine Learning:</strong>
          <br>&bull; A subset of Artificial Intelligence (AI) that provides systems the ability to automatically learn and improve from experience without being explicitly programmed.
          <br>&bull; Coined in <strong>1959</strong> by <strong>Arthur Samuel</strong> (IBM scientist who built a self-learning Checkers program).
          <br>&bull; <strong>Tom Mitchell's Formal Definition (1997):</strong> <em>"A computer program is said to learn from experience E with respect to some class of tasks T and performance measure P, if its performance at tasks in T, as measured by P, improves with experience E."</em></span>
        <span class="lang-hi"><strong>मशीन लर्निंग की परिभाषा:</strong>
          <br>&bull; आर्टिफिशियल इंटेलिजेंस (AI) का वह उप-क्षेत्र जो कंप्यूटर को बिना स्पष्ट रूप से प्रोग्राम किए, पिछले अनुभवों (डेटा) से स्वतः सीखने और सुधार करने की क्षमता प्रदान करता है।
          <br>&bull; <strong>1959</strong> में <strong>आर्थर सैमुअल</strong> (IBM) द्वारा 'मशीन लर्निंग' शब्द प्रतिपादित किया गया (इन्होंने चेकर्स गेम खेलने वाला प्रोग्राम बनाया था)।
          <br>&bull; <strong>टॉम मिशेल (1997) की परिभाषा:</strong> यदि किसी कार्य <em>T</em> पर अनुभव <em>E</em> के साथ प्रणाली का प्रदर्शन माप <em>P</em> सुधरता है, तो वह प्रणाली मशीन लर्निंग करती है।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Traditional Programming vs Machine Learning:</strong>
          <br>&bull; <strong>Traditional Programming:</strong> Data + Program (Rules written by Human) &rarr; Computer &rarr; <strong>Output</strong>.
          <br>&bull; <strong>Machine Learning:</strong> Data + Output (Desired Results) &rarr; Computer &rarr; <strong>Model / Rules</strong> (Automatically learned algorithm).</span>
        <span class="lang-hi"><strong>पारंपरिक प्रोग्रामिंग बनाम मशीन लर्निंग:</strong>
          <br>&bull; <strong>पारंपरिक प्रोग्रामिंग:</strong> डेटा + नियम (प्रोग्रामर द्वारा लिखित कोड) &rarr; कंप्यूटर &rarr; <strong>आउटपुट</strong>।
          <br>&bull; <strong>मशीन लर्निंग:</strong> डेटा + अपेक्षित आउटपुट &rarr; कंप्यूटर &rarr; <strong>मॉडल/नियम</strong> (कंप्यूटर स्वयं सीखता है)।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Machine Learning Workflow Lifecycle:</strong>
          <br>&bull; <strong>1. Data Collection:</strong> Gathering raw structured or unstructured data.
          <br>&bull; <strong>2. Data Cleaning &amp; Preprocessing:</strong> Handling missing values, outliers, encoding categorical variables, normalization/scaling.
          <br>&bull; <strong>3. Feature Engineering:</strong> Selecting and transforming relevant variables for prediction.
          <br>&bull; <strong>4. Model Training:</strong> Splitting data into Training Set (typically 70-80%) and Testing Set (20-30%).
          <br>&bull; <strong>5. Evaluation &amp; Hyperparameter Tuning:</strong> Testing on unseen data and optimizing parameters.
          <br>&bull; <strong>6. Deployment &amp; Monitoring:</strong> Integrating model into production APIs.</span>
        <span class="lang-hi"><strong>मशीन लर्निंग का कार्यचक्र:</strong>
          <br>&bull; <strong>1. डेटा संग्रहण:</strong> कच्चा डेटा एकत्र करना।
          <br>&bull; <strong>2. डेटा प्री-प्रोसेसिंग:</strong> मिसिंग वैल्यू भरना, आउटलायर्स हटाना, स्केलिंग करना।
          <br>&bull; <strong>3. फीचर इंजीनियरिंग:</strong> सबसे महत्वपूर्ण चर/विशेषताओं का चयन करना।
          <br>&bull; <strong>4. मॉडल ट्रेनिंग:</strong> डेटा को ट्रेनिंग (70-80%) और टेस्टिंग (20-30%) में बांटकर मॉडल सिखाना।
          <br>&bull; <strong>5. मॉडल मूल्यांकन:</strong> नए डेटा पर प्रदर्शन मापना और ट्यूनिंग करना।
          <br>&bull; <strong>6. परिनियोजन (Deployment):</strong> वास्तविक उपयोग में लाना।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 3: Types of Machine Learning -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">2. The Three Pillars of Machine Learning (Types &amp; Algorithms)</span>
    <span class="lang-hi">2. मशीन लर्निंग के तीन मुख्य प्रकार एवं कलन विधियां (Algorithms)</span>
  </div>
  <div class="content-block">
    <table class="comparison-table">
      <thead>
        <tr>
          <th><span class="lang-en">Paradigm</span><span class="lang-hi">प्रतिमान</span></th>
          <th><span class="lang-en">Training Data Type</span><span class="lang-hi">प्रशिक्षण डेटा प्रकार</span></th>
          <th><span class="lang-en">Sub-Tasks</span><span class="lang-hi">उप-कार्य</span></th>
          <th><span class="lang-en">Prominent Algorithms</span><span class="lang-hi">प्रमुख एल्गोरिदम</span></th>
          <th><span class="lang-en">Real-World Examples</span><span class="lang-hi">व्यावहारिक उदाहरण</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Supervised Learning (पर्यवेक्षित)</strong></td>
          <td><span class="lang-en"><strong>Labeled Data</strong> (Input $X$ mapped to known output $Y$).</span><span class="lang-hi"><strong>लेबल युक्त डेटा</strong> (इनपुट के साथ सही उत्तर दिया होता है)।</span></td>
          <td><span class="lang-en"><strong>1. Classification:</strong> Discrete category prediction.<br><strong>2. Regression:</strong> Continuous numerical value prediction.</span><span class="lang-hi"><strong>1. वर्गीकरण:</strong> श्रेणी पहचान (हाँ/ना)।<br><strong>2. प्रतिगमन:</strong> संख्यात्मक मान का अनुमान।</span></td>
          <td>Linear Regression, Logistic Regression, Decision Trees, Random Forest, Support Vector Machines (SVM), k-Nearest Neighbors (k-NN), Naive Bayes</td>
          <td>Email spam filtering, credit card fraud detection, house price estimation, medical tumor diagnosis (Malignant vs Benign)</td>
        </tr>
        <tr>
          <td><strong>Unsupervised Learning (गैर-पर्यवेक्षित)</strong></td>
          <td><span class="lang-en"><strong>Unlabeled Data</strong> (Only Input $X$ is given, no target label).</span><span class="lang-hi"><strong>बिना लेबल वाला डेटा</strong> (कोई पूर्व-निर्धारित उत्तर या श्रेणी नहीं होती)।</span></td>
          <td><span class="lang-en"><strong>1. Clustering:</strong> Grouping similar data points.<br><strong>2. Association Rule:</strong> Finding relations between items.<br><strong>3. Dimensionality Reduction:</strong> Compressing features.</span><span class="lang-hi"><strong>1. क्लस्टरिंग:</strong> समान डेटा के समूह बनाना।<br><strong>2. एसोसिएशन नियम:</strong> सह-संबंध खोजना।<br><strong>3. आयाम न्यूनीकरण:</strong> विशेषताएं घटाना।</span></td>
          <td>k-Means Clustering, Hierarchical Clustering, Principal Component Analysis (PCA), Apriori Algorithm</td>
          <td>Customer segmentation in retail, market basket analysis (e.g., Bread &rarr; Butter), anomaly/intrusion detection, image compression</td>
        </tr>
        <tr>
          <td><strong>Reinforcement Learning (सुदृढ़ीकरण)</strong></td>
          <td><span class="lang-en"><strong>Trial and Error via Environment Feedback</strong> (No static dataset; learns via Rewards and Penalties).</span><span class="lang-hi"><strong>वातावरण से परस्पर संवाद</strong> (सकारात्मक पुरस्कार एवं नकारात्मक दंड के आधार पर सीखना)।</span></td>
          <td><span class="lang-en"><strong>Policy Optimization:</strong> Agent takes actions in Environment to maximize cumulative reward over time.</span><span class="lang-hi"><strong>नीति अनुकूलन:</strong> एजेंट अधिकतम कुल पुरस्कार प्राप्त करने हेतु निर्णय लेता है।</span></td>
          <td>Q-Learning, Deep Q-Networks (DQN), Markov Decision Process (MDP), SARSA, Policy Gradients</td>
          <td>Self-driving car lane control, robotics navigation, chess/Go game bots (AlphaGo), automated financial trading</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- Card 4: Evaluation Metrics & Model Errors -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">3. Model Evaluation Metrics, Confusion Matrix &amp; Errors</span>
    <span class="lang-hi">3. मॉडल मूल्यांकन मानक, कन्फ्यूजन मैट्रिक्स एवं त्रुटियां</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Confusion Matrix (वर्गीकरण मैट्रिक्स):</strong>
          <br>&bull; A $2 \times 2$ table used to evaluate the performance of a classification model:
          <br>&nbsp;&nbsp;&bull; <strong>True Positive (TP):</strong> Positive correctly predicted as Positive.
          <br>&nbsp;&nbsp;&bull; <strong>True Negative (TN):</strong> Negative correctly predicted as Negative.
          <br>&nbsp;&nbsp;&bull; <strong>False Positive (FP - Type I Error):</strong> Negative wrongly predicted as Positive (e.g., normal email marked as spam).
          <br>&nbsp;&nbsp;&bull; <strong>False Negative (FN - Type II Error):</strong> Positive wrongly predicted as Negative (e.g., diseased patient diagnosed as healthy - highly critical error).</span>
        <span class="lang-hi"><strong>कन्फ्यूजन मैट्रिक्स (Confusion Matrix):</strong>
          <br>&bull; वर्गीकरण मॉडल के प्रदर्शन को मापने वाली तालिका:
          <br>&nbsp;&nbsp;&bull; <strong>ट्रू पॉजिटिव (TP):</strong> सही रूप से पहचाना गया पॉजिटिव।
          <br>&nbsp;&nbsp;&bull; <strong>ट्रू नेगेटिव (TN):</strong> सही रूप से पहचाना गया नेगेटिव।
          <br>&nbsp;&nbsp;&bull; <strong>फाल्स पॉजिटिव (FP - टाइप I त्रुटि):</strong> गलत रूप से पॉजिटिव बताना (जैसे निर्दोष मेल को स्पैम घोषित करना)।
          <br>&nbsp;&nbsp;&bull; <strong>फाल्स नेगेटिव (FN - टाइप II त्रुटि):</strong> बीमारी होने पर भी नेगेटिव बताना (सबसे घातक त्रुटि)।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Core Performance Metrics:</strong>
          <br>&bull; <strong>Accuracy:</strong> $\frac{TP + TN}{TP + TN + FP + FN}$ (Total correct predictions over all predictions).
          <br>&bull; <strong>Precision:</strong> $\frac{TP}{TP + FP}$ (Out of all positive predictions, how many were actually positive).
          <br>&bull; <strong>Recall (Sensitivity):</strong> $\frac{TP}{TP + FN}$ (Out of all actual positives, how many were correctly detected).
          <br>&bull; <strong>F1-Score:</strong> The <em>Harmonic Mean</em> of Precision and Recall: $2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$. Ideal for imbalanced datasets.</span>
        <span class="lang-hi"><strong>प्रमुख मूल्यांकन मानक:</strong>
          <br>&bull; <strong>सटीकता (Accuracy):</strong> कुल सही अनुमान / कुल परीक्षण मामले।
          <br>&bull; <strong>प्रिसिजन (Precision):</strong> मॉडल द्वारा बताए गए कुल पॉजिटिव में से कितने वास्तव में सही थे।
          <br>&bull; <strong>रिकॉल (Recall / संवेदनशीलता):</strong> वास्तविक पॉजिटिव मामलों में से मॉडल कितने पकड़ पाया।
          <br>&bull; <strong>F1-स्कोर:</strong> प्रिसिजन और रिकॉल का <em>हरात्मक माध्य (Harmonic Mean)</em>; असंतुलित डेटासेट में सर्वश्रेष्ठ मापक।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Overfitting vs Underfitting (Bias-Variance Dilemma):</strong>
          <br>&bull; <strong>Underfitting (High Bias):</strong> Model is too simplistic; fails to capture patterns in training data and performs poorly on both training and test data.
          <br>&bull; <strong>Overfitting (High Variance):</strong> Model is overly complex; memorizes noise in training data. Performs exceptionally well on training set but poorly on new/unseen test data.
          <br>&bull; <strong>Remedies for Overfitting:</strong> Cross-validation ($k$-fold), Regularization ($L_1$ Lasso, $L_2$ Ridge), pruning decision trees, dropout, gathering more training data.</span>
        <span class="lang-hi"><strong>ओवरफिटिंग बनाम अंडरफिटिंग (बायस-वेरिएंस द्वंद्व):</strong>
          <br>&bull; <strong>अंडरफिटिंग (उच्च बायस):</strong> मॉडल बहुत सरल है; वह ट्रेनिंग डेटा के पैटर्न को भी नहीं सीख पाता (दोनों में खराब प्रदर्शन)।
          <br>&bull; <strong>ओवरफिटिंग (उच्च विचरण):</strong> मॉडल बहुत जटिल है; उसने ट्रेनिंग डेटा को रट लिया है। ट्रेनिंग में 100% अंक लाता है किंतु नए डेटा पर फेल हो जाता है।
          <br>&bull; <strong>ओवरफिटिंग रोकने के उपाय:</strong> $k$-फोल्ड क्रॉस वैलिडेशन, रेगुलराइजेशन ($L_1$ लासो, $L_2$ रिज), डिसिजन ट्री की प्रूनिंग (कटाई), अधिक डेटा जोड़ना।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 5: One-Liner Exam Facts -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">Key One-Liner Exam Facts (UPSSSC Computer Special)</span>
    <span class="lang-hi">महत्वपूर्ण वन-लाइनर परीक्षा तथ्य (UPSSSC कंप्यूटर विशेष)</span>
  </div>
  <div class="content-block">
    <table class="comparison-table">
      <thead>
        <tr>
          <th><span class="lang-en">Exam Question Topic</span><span class="lang-hi">परीक्षा प्रश्न विषय</span></th>
          <th><span class="lang-en">Core Exam Fact &amp; Details</span><span class="lang-hi">महत्वपूर्ण तथ्य एवं विवरण</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="lang-en">Who coined the term 'Machine Learning'?</span><span class="lang-hi">'मशीन लर्निंग' शब्द किसने गढ़ा?</span></td>
          <td><span class="lang-en"><strong>Arthur Samuel</strong> in <strong>1959</strong> at IBM.</span><span class="lang-hi"><strong>आर्थर सैमुअल</strong> (1959, IBM)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Machine learning that utilizes labeled training datasets</span><span class="lang-hi">लेबल युक्त डेटा पर आधारित मशीन लर्निंग</span></td>
          <td><span class="lang-en"><strong>Supervised Learning</strong> (पर्यवेक्षित शिक्षण).</span><span class="lang-hi"><strong>सुपरवाइज्ड लर्निंग</strong> (वर्गीकरण एवं प्रतिगमन)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Common algorithm used for customer segmentation (clustering)</span><span class="lang-hi">ग्राहक वर्गीकरण (क्लस्टरिंग) हेतु सर्वाधिक प्रयुक्त एल्गोरिदम</span></td>
          <td><span class="lang-en"><strong>k-Means Clustering</strong> (Unsupervised learning).</span><span class="lang-hi"><strong>k-मीन्स क्लस्टरिंग</strong> (अनसुपरवाइज्ड लर्निंग)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Type of error when a healthy person is classified as diseased</span><span class="lang-hi">स्वस्थ व्यक्ति को बीमार घोषित करने वाली त्रुटि</span></td>
          <td><span class="lang-en"><strong>False Positive (Type I Error)</strong>.</span><span class="lang-hi"><strong>फाल्स पॉजिटिव (टाइप I त्रुटि)</strong>।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Mathematical nature of F1-Score</span><span class="lang-hi">F1-स्कोर का गणितीय स्वरूप</span></td>
          <td><span class="lang-en"><strong>Harmonic Mean</strong> of Precision and Recall.</span><span class="lang-hi">प्रिसिजन और रिकॉल का <strong>हरात्मक माध्य (Harmonic Mean)</strong>।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Algorithm based on Bayes' Theorem of probability</span><span class="lang-hi">प्रायिकता के बेयस प्रमेय पर आधारित एल्गोरिदम</span></td>
          <td><span class="lang-en"><strong>Naive Bayes Classifier</strong> (popular in text classification and spam detection).</span><span class="lang-hi"><strong>नाइव बेयस क्लासिफायर</strong> (टेक्स्ट एवं स्पैम वर्गीकरण)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Condition where model fits training data too closely</span><span class="lang-hi">जब मॉडल ट्रेनिंग डेटा को अत्यधिक रट लेता है</span></td>
          <td><span class="lang-en"><strong>Overfitting</strong> (characterized by High Variance and Low Bias).</span><span class="lang-hi"><strong>ओवरफिटिंग</strong> (उच्च विचरण एवं न्यून बायस)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Leading Python open-source library for classic Machine Learning</span><span class="lang-hi">पारंपरिक मशीन लर्निंग की प्रमुख पायथन लाइब्रेरी</span></td>
          <td><span class="lang-en"><strong>Scikit-Learn</strong> (sklearn).</span><span class="lang-hi"><strong>Scikit-Learn</strong> (sklearn)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Machine learning paradigm based on reward and punishment</span><span class="lang-hi">इनाम व सजा के सिद्धांत पर कार्य करने वाली लर्निंग</span></td>
          <td><span class="lang-en"><strong>Reinforcement Learning</strong> (सुदृढ़ीकरण शिक्षण).</span><span class="lang-hi"><strong>रीइन्फोर्समेंट लर्निंग</strong> (जैसे Q-लर्निंग)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Technique used to reduce dimensionality without losing information</span><span class="lang-hi">डेटा का आकार/आयाम घटाने वाली तकनीक</span></td>
          <td><span class="lang-en"><strong>PCA</strong> (Principal Component Analysis).</span><span class="lang-hi"><strong>PCA</strong> (प्रिंसिपल कंपोनेंट एनालिसिस)।</span></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

</div>"""

def build_deep_learning_theory_html():
    return """<div class="tab-content" id="tab-theory" style="display:block">

<!-- Card 1: Mind Map -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">Mind Map: Deep Learning Architecture, Neural Networks &amp; Hardware</span>
    <span class="lang-hi">माइंड मैप: डीप लर्निंग वास्तुकला, न्यूरल नेटवर्क एवं हार्डवेयर तंत्र</span>
  </div>
  <div class="lang-en">
    <div class="mermaid">
graph TD
    A[Deep Learning DL] --> B[Biological to Artificial Neurons]
    A --> C[Neural Network Architecture]
    A --> D[Training & Mathematics]
    A --> E[Core DL Specialized Networks]
    A --> F[Hardware & Frameworks]

    B --> B1[Biological: Dendrite, Soma, Axon, Synapse]
    B --> B2[Artificial: Inputs x, Weights w, Bias b, Activation f]
    B --> B3[Perceptron: Frank Rosenblatt 1958 Single Layer]

    C --> C1[Input Layer: Features Vector]
    C --> C2[Hidden Layers: Deep = 2 or more hidden layers]
    C --> C3[Output Layer: Predictions Softmax/Sigmoid]

    D --> D1[Activation Functions: ReLU, Sigmoid, Tanh, Softmax]
    D --> D2[Forward Propagation: Calculating output and Loss]
    D --> D3[Backpropagation: Geoffrey Hinton Chain Rule Gradient Descent]

    E --> E1[CNN: Convolutional Neural Networks Image & Vision]
    E --> E2[RNN / LSTM: Recurrent Networks Sequential & Time Series]
    E --> E3[Transformers: Attention Mechanism Foundation of LLMs]
    E --> E4[GANs: Generative Adversarial Networks Generator vs Discriminator]

    F --> F1[Hardware: GPUs Nvidia CUDA, Tensor Cores, TPUs Google]
    F --> F2[Frameworks: TensorFlow Google, PyTorch Meta, Keras]
    </div>
  </div>
  <div class="lang-hi">
    <div class="mermaid">
graph TD
    A[डीप लर्निंग DL] --> B[जैविक से कृत्रिम न्यूरॉन]
    A --> C[न्यूरल नेटवर्क वास्तुकला]
    A --> D[प्रशिक्षण एवं गणितीय प्रक्रिया]
    A --> E[प्रमुख विशिष्ट न्यूरल नेटवर्क]
    A --> F[हार्डवेयर एवं प्रमुख फ्रेमवर्क]

    B --> B1[जैविक न्यूरॉन: डेंड्राइट, सोमा, एक्सॉन, सिनेप्स]
    B --> B2[कृत्रिम न्यूरॉन: इनपुट x, भार w, बायस b, सक्रियण फलन f]
    B --> B3[परसेप्ट्रॉन: फ्रैंक रोसेनब्लाट 1958 एकल परत]

    C --> C1[इनपुट लेयर: कच्चा डेटा/फीचर वेक्टर]
    C --> C2[हिडन लेयर: डीप = 2 या अधिक छिपी हुई परतें]
    C --> C3[आउटपुट लेयर: अंतिम परिणाम/संभाव्यता]

    D --> D1[सक्रियण फलन: ReLU, सिग्मॉइड, टैन-एच, सॉफ्टमैक्स]
    D --> D2[फॉरवर्ड प्रोपेगेशन: आउटपुट एवं लॉस की गणना]
    D --> D3[बैकप्रोपेगेशन: जेफ्री हिंटन चेन रूल ग्रेडिएंट डिसेंट]

    E --> E1[CNN: कॉन्वोल्यूशनल न्यूरल नेटवर्क छवि व विजन]
    E --> E2[RNN / LSTM: आवर्तक न्यूरल नेटवर्क अनुक्रमिक डेटा व भाषा]
    E --> E3[ट्रांसफॉर्मर: अटेंशन मैकेनिज्म आधुनिक LLM का आधार]
    E --> E4[GAN: जेनरेटर बनाम डिस्क्रिमिनेटर यथार्थवादी छवियां]

    F --> F1[हार्डवेयर: GPU एनवीडिया CUDA, TPU गूगल]
    F --> F2[सॉफ्टवेयर: टेन्सरफ्लो, पायटॉर्च, केरास]
    </div>
  </div>
</div>

<!-- Card 2: Fundamentals of Deep Learning & Perceptron -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">1. Biological vs Artificial Neurons &amp; The Perceptron</span>
    <span class="lang-hi">1. जैविक बनाम कृत्रिम न्यूरॉन एवं परसेप्ट्रॉन की मूल अवधारणा</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>What is Deep Learning?</strong>
          <br>&bull; A specialized subset of Machine Learning based on <strong>Artificial Neural Networks (ANNs)</strong> with representation learning.
          <br>&bull; Called "Deep" because it utilizes <strong>multiple hidden layers</strong> (typically tens or hundreds) between the input and output layers, allowing the network to automatically extract complex hierarchical features without manual feature engineering.
          <br>&bull; <strong>Godfathers of Deep Learning:</strong> <strong>Geoffrey Hinton</strong>, <strong>Yann LeCun</strong>, and <strong>Yoshua Bengio</strong> (jointly awarded the prestigious <em>Turing Award in 2018</em>).</span>
        <span class="lang-hi"><strong>डीप लर्निंग क्या है?</strong>
          <br>&bull; मशीन लर्निंग का एक विशिष्ट उपसमुच्चय जो <strong>आर्टिफिशियल न्यूरल नेटवर्क (ANN)</strong> पर आधारित है।
          <br>&bull; इसे "डीप" (गहन) इसलिए कहा जाता है क्योंकि इसमें इनपुट और आउटपुट के बीच <strong>दो या दो से अधिक 'छिपी हुई परतें' (Hidden Layers)</strong> होती हैं। यह मानवीय हस्तक्षेप के बिना कच्चे डेटा से जटिल विशेषताओं को स्वतः निकाल लेता है।
          <br>&bull; <strong>डीप लर्निंग के जनक (Godfathers):</strong> <strong>जेफ्री हिंटन</strong>, <strong>यान लेकुन</strong> और <strong>योशुआ बेंगियो</strong> (तीनों को संयुक्त रूप से 2018 का ट्यूरिंग पुरस्कार मिला)।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Biological vs Artificial Neuron Analogy:</strong>
          <br>&bull; <strong>Dendrites &rarr; Inputs ($x_1, x_2, \dots, x_n$):</strong> Receive incoming signals.
          <br>&bull; <strong>Synapses &rarr; Weights ($w_1, w_2, \dots, w_n$):</strong> Strength or importance of connection.
          <br>&bull; <strong>Soma (Cell Body) &rarr; Summation &amp; Bias ($z = \sum w_i x_i + b$):</strong> Accumulates incoming inputs with bias.
          <br>&bull; <strong>Axon &rarr; Output Activation ($a = f(z)$):</strong> Fires signal through an activation function to next neuron.</span>
        <span class="lang-hi"><strong>जैविक बनाम कृत्रिम न्यूरॉन की तुलना:</strong>
          <br>&bull; <strong>डेंड्राइट्स (Dendrites) &rarr; इनपुट ($x_i$):</strong> आने वाले संकेतों को ग्रहण करना।
          <br>&bull; <strong>सिनेप्स (Synapses) &rarr; भार (Weights - $w_i$):</strong> कनेक्शन की शक्ति या महत्व।
          <br>&bull; <strong>सोमा (कोशिका पिंड) &rarr; योग एवं बायस ($\sum w_i x_i + b$):</strong> संकेतों का कुल योग।
          <br>&bull; <strong>एक्सॉन (Axon) &rarr; आउटपुट ($f(z)$):</strong> सक्रियण फलन द्वारा अगले न्यूरॉन को संकेत भेजना।</span>
      </li>
      <li>
        <span class="lang-en"><strong>The Perceptron (1958 - Frank Rosenblatt):</strong>
          <br>&bull; Invented at Cornell Aeronautical Laboratory; the simplest and earliest model of an artificial neural network.
          <br>&bull; A binary linear classifier that computes a weighted sum of inputs and applies a step threshold function.
          <br>&bull; <strong>Limitation:</strong> Minsky and Papert (1969) proved a single-layer perceptron cannot solve non-linearly separable problems such as the <strong>XOR problem</strong>, triggering the first "AI Winter" until Multi-Layer Perceptrons (MLP) emerged.</span>
        <span class="lang-hi"><strong>परसेप्ट्रॉन (1958 - फ्रैंक रोसेनब्लाट):</strong>
          <br>&bull; कॉर्नेल एयरोनॉटिकल लैब में विकसित; कृत्रिम न्यूरल नेटवर्क का सबसे पहला और सरलतम मॉडल।
          <br>&bull; यह एक बाइनरी क्लासिफायर था जो इनपुट के भारित योग पर स्टेप फंक्शन लगाता था।
          <br>&bull; <strong>सीमा:</strong> मार्विन मिंस्की ने सिद्ध किया कि एकल परसेप्ट्रॉन <strong>XOR समस्या</strong> (गैर-रैखिक समस्या) को हल नहीं कर सकता, जिससे पहला "AI विंटर" आया।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 3: Neural Network Architecture & Mathematics -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">2. Neural Network Architecture, Activation Functions &amp; Training</span>
    <span class="lang-hi">2. न्यूरल नेटवर्क वास्तुकला, सक्रियण फलन एवं प्रशिक्षण गणित</span>
  </div>
  <div class="content-block">
    <p>
      <span class="lang-en">An Artificial Neural Network is trained via <strong>Forward Propagation</strong> (calculating predictions) and <strong>Backpropagation</strong> (updating weights using gradient descent).</span>
      <span class="lang-hi">ANN का प्रशिक्षण दो चरणों में होता है: <strong>फॉरवर्ड प्रोपेगेशन</strong> (अनुमान निकालना) एवं <strong>बैकप्रोपेगेशन</strong> (त्रुटि घटाने हेतु भार को ठीक करना)।</span>
    </p>
    <table class="comparison-table">
      <thead>
        <tr>
          <th><span class="lang-en">Activation Function</span><span class="lang-hi">सक्रियण फलन</span></th>
          <th><span class="lang-en">Mathematical Formula</span><span class="lang-hi">गणितीय सूत्र</span></th>
          <th><span class="lang-en">Output Range</span><span class="lang-hi">आउटपुट परास</span></th>
          <th><span class="lang-en">Primary Usage &amp; Properties</span><span class="lang-hi">उपयोग एवं विशेषताएं</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Sigmoid (Logistic)</strong></td>
          <td>$\sigma(z) = \frac{1}{1 + e^{-z}}$</td>
          <td>$(0, 1)$</td>
          <td><span class="lang-en">Binary classification output layer; suffers from <em>Vanishing Gradient</em> problem.</span><span class="lang-hi">बाइनरी वर्गीकरण के आउटपुट लेयर में; वैनिशिंग ग्रेडिएंट की समस्या होती है।</span></td>
        </tr>
        <tr>
          <td><strong>ReLU (Rectified Linear Unit)</strong></td>
          <td>$f(z) = \max(0, z)$</td>
          <td>$[0, \infty)$</td>
          <td><span class="lang-en"><strong>Most widely used</strong> in hidden layers; computationally fast, prevents vanishing gradient for positive values.</span><span class="lang-hi">छिपी परतों (Hidden layers) में <strong>सर्वाधिक प्रयुक्त</strong>; गणना में तीव्र, वैनिशिंग ग्रेडिएंट से बचाव।</span></td>
        </tr>
        <tr>
          <td><strong>Tanh (Hyperbolic Tangent)</strong></td>
          <td>$\tanh(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}}$</td>
          <td>$(-1, 1)$</td>
          <td><span class="lang-en">Zero-centered; preferred over Sigmoid in some recurrent networks.</span><span class="lang-hi">शून्य-केंद्रित (Zero-centered); कुछ रिकरेंट नेटवर्कों में सिग्मॉइड से बेहतर।</span></td>
        </tr>
        <tr>
          <td><strong>Softmax</strong></td>
          <td>$\sigma(z)_i = \frac{e^{z_i}}{\sum e^{z_j}}$</td>
          <td>$(0, 1)$, Sum $= 1$</td>
          <td><span class="lang-en">Multi-class classification output layer; outputs normalized probability distribution.</span><span class="lang-hi">मल्टी-क्लास वर्गीकरण की आउटपुट लेयर; सभी वर्गों की प्रायिकताओं का योग 1 होता है।</span></td>
        </tr>
      </tbody>
    </table>
    <ul class="points-list" style="margin-top:16px;">
      <li>
        <span class="lang-en"><strong>Backpropagation &amp; Gradient Descent:</strong>
          <br>&bull; <strong>Backpropagation:</strong> Popularized by Geoffrey Hinton, David Rumelhart, and Ronald Williams (1986). Uses the mathematical <em>Chain Rule of calculus</em> to propagate errors backwards from output layer to input layer.
          <br>&bull; <strong>Gradient Descent:</strong> Optimization algorithm that iteratively updates network weights in the direction opposite to the gradient of the loss function ($\theta = \theta - \alpha \nabla L$, where $\alpha$ is the <em>Learning Rate</em>).</span>
        <span class="lang-hi"><strong>बैकप्रोपेगेशन एवं ग्रेडिएंट डिसेंट:</strong>
          <br>&bull; <strong>बैकप्रोपेगेशन:</strong> 1986 में जेफ्री हिंटन आदि द्वारा लोकप्रिय बनाया गया। यह कलन के <em>चेन रूल (Chain Rule)</em> का उपयोग कर आउटपुट से इनपुट की ओर त्रुटि भेजता है।
          <br>&bull; <strong>ग्रेडिएंट डिसेंट:</strong> ऑप्टिमाइजेशन एल्गोरिदम जो लॉस फलन की ढलान (Gradient) के विपरीत दिशा में भार को अपडेट करता है ($\alpha$ = लर्निंग रेट)।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 4: Specialized Deep Learning Architectures -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">3. Major Deep Learning Architectures (CNN, RNN, Transformers, GAN)</span>
    <span class="lang-hi">3. प्रमुख डीप लर्निंग वास्तुकला (CNN, RNN, ट्रांसफॉर्मर, GAN)</span>
  </div>
  <div class="content-block">
    <table class="comparison-table">
      <thead>
        <tr>
          <th><span class="lang-en">Architecture</span><span class="lang-hi">आर्किटेक्चर</span></th>
          <th><span class="lang-en">Full Form &amp; Pioneer</span><span class="lang-hi">पूर्ण रूप एवं प्रणेता</span></th>
          <th><span class="lang-en">Core Mechanism</span><span class="lang-hi">मुख्य कार्यप्रणाली</span></th>
          <th><span class="lang-en">Primary Applications</span><span class="lang-hi">प्रमुख अनुप्रयोग</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>CNN</strong></td>
          <td><strong>Convolutional Neural Network</strong> (Yann LeCun - LeNet, 1989 / AlexNet, 2012)</td>
          <td><span class="lang-en">Uses <strong>Convolution kernels/filters</strong> and <strong>Pooling layers</strong> (MaxPool) to preserve spatial grid hierarchy of pixels.</span><span class="lang-hi">कॉन्वोल्यूशन फिल्टर और पूलिंग परतों का उपयोग कर पिक्सेल के स्थानिक पैटर्न को पहचानता है।</span></td>
          <td>Image recognition, facial recognition, medical X-ray/MRI diagnosis, self-driving car vision, object detection</td>
        </tr>
        <tr>
          <td><strong>RNN / LSTM</strong></td>
          <td><strong>Recurrent Neural Network / Long Short-Term Memory</strong> (Hochreiter &amp; Schmidhuber, 1997)</td>
          <td><span class="lang-en">Processes sequential time-series data with internal feedback loops. LSTM solves vanishing gradient via Forget, Input, and Output gates.</span><span class="lang-hi">डेटा में समय-अनुक्रम (Sequential) याद रखता है। LSTM गेट्स (Forget, Input, Output) द्वारा दीर्घकालिक स्मृति रखता है।</span></td>
          <td>Speech recognition, stock market prediction, language translation, time-series forecasting</td>
        </tr>
        <tr>
          <td><strong>Transformer</strong></td>
          <td><strong>Transformer Architecture</strong> (Vaswani et al., Google Brain, 2017)</td>
          <td><span class="lang-en">Eliminates recurrence; uses <strong>Self-Attention Mechanism</strong> to process entire sequences in parallel, capturing long-range contextual relationships.</span><span class="lang-hi">रिकरेंस हटाकर 'सेल्फ-अटेंशन' का उपयोग करता है। पूरे वाक्य को समानांतर रूप से प्रोसेस कर संदर्भ समझता है।</span></td>
          <td>Large Language Models (GPT-4, Claude, Gemini, BERT, LLaMA), generative text, protein folding (AlphaFold)</td>
        </tr>
        <tr>
          <td><strong>GAN</strong></td>
          <td><strong>Generative Adversarial Network</strong> (Ian Goodfellow, 2014)</td>
          <td><span class="lang-en">Consists of two competing neural networks: <strong>Generator</strong> (creates fake data) and <strong>Discriminator</strong> (detects real vs fake) in a minimax game.</span><span class="lang-hi">दो नेटवर्क आपस में प्रतिस्पर्धा करते हैं: <strong>जेनेरेटर</strong> (नकली डेटा बनाता है) और <strong>डिस्क्रिमिनेटर</strong> (असली व नकली की पहचान करता है)।</span></td>
          <td>Deepfake generation, photorealistic face synthesis, art generation, image super-resolution</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- Card 5: Hardware & Software Frameworks for Deep Learning -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">4. Hardware Acceleration &amp; Software Frameworks for Deep Learning</span>
    <span class="lang-hi">4. डीप लर्निंग हेतु हार्डवेयर त्वरण एवं सॉफ्टवेयर फ्रेमवर्क</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Why Traditional CPUs are Insufficient:</strong>
          <br>&bull; Deep learning models require billions of simultaneous matrix multiplications (linear algebra operations).
          <br>&bull; CPUs have few powerful cores (4 to 64) optimized for sequential computing, whereas Deep Learning requires thousands of parallel cores.</span>
        <span class="lang-hi"><strong>पारंपरिक CPU डीप लर्निंग के लिए अपर्याप्त क्यों हैं:</strong>
          <br>&bull; डीप लर्निंग में अरबों मैट्रिक्स गुणा (Matrix Multiplications) एक साथ करने पड़ते हैं।
          <br>&bull; CPU में कम कोर (4 से 64) होते हैं जो क्रमिक गणना करते हैं, जबकि DL को हजारों समानांतर कोर की आवश्यकता होती है।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Hardware Accelerators:</strong>
          <br>&bull; <strong>GPU (Graphics Processing Unit):</strong> Specialized chips with thousands of small cores (Nvidia CUDA architecture, Tensor Cores). Companies like Nvidia (A100, H100, Blackwell) dominate AI training.
          <br>&bull; <strong>TPU (Tensor Processing Unit):</strong> Custom Application-Specific Integrated Circuit (ASIC) designed specifically by <strong>Google</strong> for accelerating machine learning workloads with native tensor matrix math.
          <br>&bull; <strong>NPU (Neural Processing Unit):</strong> On-device AI chips in modern smartphones (e.g., Apple Neural Engine, Qualcomm Hexagon).</span>
        <span class="lang-hi"><strong>हार्डवेयर एक्सेलरेटर्स:</strong>
          <br>&bull; <strong>GPU (ग्राफिक्स प्रोसेसिंग यूनिट):</strong> हजारों समानांतर कोर से युक्त चिप्स (एनवीडिया CUDA, H100, A100)।
          <br>&bull; <strong>TPU (टेन्सर प्रोसेसिंग यूनिट):</strong> <strong>गूगल</strong> द्वारा विशेष रूप से न्यूरल नेटवर्क ट्रेनिंग हेतु विकसित कस्टम ASIC चिप।
          <br>&bull; <strong>NPU (न्यूरल प्रोसेसिंग यूनिट):</strong> आधुनिक स्मार्टफोन और लैपटॉप में ऑन-डिवाइस AI कार्यों हेतु चिप (उदा. एप्पल न्यूरल इंजन)।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Leading Software Frameworks:</strong>
          <br>&bull; <strong>TensorFlow:</strong> Developed by Google Brain; open-source library for high-performance numerical computation and deep neural networks.
          <br>&bull; <strong>PyTorch:</strong> Developed by Meta AI (Facebook); widely favored by AI researchers for its dynamic computational graph.
          <br>&bull; <strong>Keras:</strong> High-level neural network API written in Python, running on top of TensorFlow.</span>
        <span class="lang-hi"><strong>प्रमुख सॉफ्टवेयर फ्रेमवर्क:</strong>
          <br>&bull; <strong>टेन्सरफ्लो (TensorFlow):</strong> गूगल ब्रेन द्वारा विकसित ओपन-सोर्स डीप लर्निंग लाइब्रेरी।
          <br>&bull; <strong>पायटॉर्च (PyTorch):</strong> मेटा (फेसबुक) द्वारा विकसित, शोधकर्ताओं में सर्वाधिक लोकप्रिय।
          <br>&bull; <strong>केरास (Keras):</strong> उच्च-स्तरीय न्यूरल नेटवर्क API जो टेन्सरफ्लो पर चलती है।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 6: One-Liner Exam Facts -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">Key One-Liner Exam Facts (UPSSSC Computer Special)</span>
    <span class="lang-hi">महत्वपूर्ण वन-लाइनर परीक्षा तथ्य (UPSSSC कंप्यूटर विशेष)</span>
  </div>
  <div class="content-block">
    <table class="comparison-table">
      <thead>
        <tr>
          <th><span class="lang-en">Exam Question Topic</span><span class="lang-hi">परीक्षा प्रश्न विषय</span></th>
          <th><span class="lang-en">Core Exam Fact &amp; Details</span><span class="lang-hi">महत्वपूर्ण तथ्य एवं विवरण</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="lang-en">Earliest model of an artificial neuron</span><span class="lang-hi">कृत्रिम न्यूरॉन का सबसे पहला मॉडल</span></td>
          <td><span class="lang-en"><strong>Perceptron</strong> (developed by Frank Rosenblatt in 1958).</span><span class="lang-hi"><strong>परसेप्ट्रॉन</strong> (1958 में फ्रैंक रोसेनब्लाट द्वारा विकसित)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Primary neural network architecture used for Image Recognition</span><span class="lang-hi">छवि पहचान हेतु प्रयुक्त प्राथमिक न्यूरल नेटवर्क</span></td>
          <td><span class="lang-en"><strong>CNN</strong> (Convolutional Neural Network).</span><span class="lang-hi"><strong>CNN</strong> (कॉन्वोल्यूशनल न्यूरल नेटवर्क)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Most popular activation function in hidden layers of modern DL</span><span class="lang-hi">आधुनिक DL की छिपी परतों में सर्वाधिक प्रयुक्त एक्टिवेशन फलन</span></td>
          <td><span class="lang-en"><strong>ReLU</strong> (Rectified Linear Unit, $f(x) = \max(0, x)$).</span><span class="lang-hi"><strong>ReLU</strong> (रेक्टिफाइड लीनियर यूनिट)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Activation function used in multi-class output layers</span><span class="lang-hi">मल्टी-क्लास आउटपुट लेयर में प्रयुक्त फलन</span></td>
          <td><span class="lang-en"><strong>Softmax</strong> (converts raw logits into probabilities summing to 1).</span><span class="lang-hi"><strong>सॉफ्टमैक्स (Softmax)</strong> (संभाव्यता योग = 1)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Core algorithm used to compute gradients and update weights in neural nets</span><span class="lang-hi">न्यूरल नेटवर्क में त्रुटि घटाने व भार बदलने की मुख्य विधि</span></td>
          <td><span class="lang-en"><strong>Backpropagation</strong> (यूजिंग चेन रूल) with <strong>Gradient Descent</strong>.</span><span class="lang-hi"><strong>बैकप्रोपेगेशन</strong> एवं <strong>ग्रेडिएंट डिसेंट</strong>।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Deep learning architecture designed for sequential text/audio processing</span><span class="lang-hi">अनुक्रमिक टेक्स्ट व ऑडियो प्रोसेसिंग हेतु उपयुक्त नेटवर्क</span></td>
          <td><span class="lang-en"><strong>RNN</strong> (Recurrent Neural Network) and <strong>LSTM</strong>.</span><span class="lang-hi"><strong>RNN</strong> एवं <strong>LSTM</strong>।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Neural architecture introduced in 2017 paper 'Attention Is All You Need'</span><span class="lang-hi">2017 के 'अटेंशन इज ऑल यू नीड' पेपर में पेश आर्किटेक्चर</span></td>
          <td><span class="lang-en"><strong>Transformer</strong> Architecture (Self-Attention mechanism).</span><span class="lang-hi"><strong>ट्रांसफॉर्मर</strong> (Transformer, LLM का आधार)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Architecture consisting of a Generator and Discriminator network</span><span class="lang-hi">जेनेरेटर एवं डिस्क्रिमिनेटर पर आधारित नेटवर्क</span></td>
          <td><span class="lang-en"><strong>GAN</strong> (Generative Adversarial Network, Ian Goodfellow, 2014).</span><span class="lang-hi"><strong>GAN</strong> (जेनेरेटिव एडवर्सेरियल नेटवर्क)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Proprietary AI accelerator chip developed by Google</span><span class="lang-hi">गूगल द्वारा विकसित विशेष AI एक्सेलेरेटर चिप</span></td>
          <td><span class="lang-en"><strong>TPU</strong> (Tensor Processing Unit).</span><span class="lang-hi"><strong>TPU</strong> (टेन्सर प्रोसेसिंग यूनिट)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Turing Award winners recognized as 'Godfathers of Deep Learning'</span><span class="lang-hi">'डीप लर्निंग के गॉडफादर' के रूप में सम्मानित ट्यूरिंग पुरस्कार विजेता</span></td>
          <td><span class="lang-en"><strong>Geoffrey Hinton</strong>, <strong>Yann LeCun</strong>, and <strong>Yoshua Bengio</strong> (2018).</span><span class="lang-hi"><strong>जेफ्री हिंटन</strong>, <strong>यान लेकुन</strong> एवं <strong>योशुआ बेंगियो</strong> (2018)।</span></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

</div>"""

def enrich_file(rel_path, theory_html):
    target_file = os.path.join("upsssc-computer", rel_path, "index.html")
    if not os.path.exists(target_file):
        print(f"Error: {target_file} not found")
        return False

    with open(target_file, "r", encoding="utf-8") as f:
        html = f.read()

    pattern = re.compile(r'<div class="tab-content" id="tab-theory"[^>]*>.*?</div>\s*(?=<div class="tab-content" id="tab-practice")', re.DOTALL)
    match = pattern.search(html)
    if not match:
        print(f"ERROR: Could not locate tab-theory boundary in {target_file}!")
        return False

    updated_html = html[:match.start()] + theory_html.strip() + "\n" + html[match.end():]

    with open(target_file, "w", encoding="utf-8") as f:
        f.write(updated_html)

    print(f"Successfully enriched {target_file}")
    return True

def main():
    enrich_file("artificial-intelligence", build_ai_theory_html())
    enrich_file("machine-learning", build_ml_theory_html())
    enrich_file("deep-learning", build_deep_learning_theory_html())

if __name__ == "__main__":
    main()
