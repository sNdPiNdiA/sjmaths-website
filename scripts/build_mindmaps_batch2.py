import sys, os, re

sys.stdout.reconfigure(encoding='utf-8')

pattern = re.compile(r'(<!--\s*Card 1:.*?-->.*?)(?=<!--\s*Card 2:)', re.DOTALL)

# ==========================================
# Topic 6: Artificial Intelligence
# ==========================================
mm_t6 = '''<!-- Card 1: Mind Map -->
<div class="card-premium mindmap-container">
    <div class="mindmap-header">
        <h3 class="theory-heading">
            <i class="fas fa-sitemap" style="color: var(--primary, #059669);"></i>
            <span class="lang-en">Comprehensive Concept Mindmap: Artificial Intelligence Architecture &amp; Ecosystem</span>
            <span class="lang-hi">विस्तृत संकल्पना माइंडमैप: कृत्रिम बुद्धिमत्ता (AI) वास्तुकला एवं पारिस्थितिकी</span>
        </h3>
        <p class="mindmap-subtitle">
            <span class="lang-en">Exhaustive Thematic Flow • 6 Pillars • Turing Test &amp; McCarthy • Narrow vs General vs Super AI • Generative AI &amp; LLMs • AI Ethics • National Strategy &amp; UP AI City</span>
            <span class="lang-hi">समग्र विषयवार संकल्पना प्रवाह • 6 प्रमुख स्तंभ • ट्यूरिंग टेस्ट व मैकार्थी • नैरो बनाम जनरल बनाम सुपर AI • जनरेटिव AI व LLMs • AI नैतिकता • राष्ट्रीय नीति व लखनऊ AI सिटी</span>
        </p>
    </div>

    <!-- Central Hub -->
    <div class="mindmap-root">
        <div class="mindmap-root-badge">
            <i class="fas fa-brain"></i>
            <span class="lang-en">Artificial Intelligence (AI) Conceptual Architecture</span>
            <span class="lang-hi">कृत्रिम बुद्धिमत्ता (AI) वैचारिक वास्तुकला</span>
        </div>
    </div>

    <!-- 6 Branch Nodes Grid -->
    <div class="mindmap-grid">

        <!-- Branch 1: Historical Genesis & Turing Foundations -->
        <div class="mindmap-node epoch-prehistoric">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-history" style="color: #059669;"></i>
                    <span class="lang-en">1. Origins &amp; Foundational Concepts</span>
                    <span class="lang-hi">1. उद्भव, दार्शनिक आधार एवं ट्यूरिंग टेस्ट</span>
                </h4>
                <span class="mindmap-node-tag">1950 Turing • 1956 Dartmouth</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Pioneers &amp; Historical Milestones</span>
                        <span class="lang-hi">अग्रणी वैज्ञानिक एवं ऐतिहासिक पड़ाव</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Alan Turing</strong> (1950, Computing Machinery)</span>
                        <span class="mindmap-chip"><strong>Turing Test</strong> (Imitation Game)</span>
                        <span class="mindmap-chip"><strong>John McCarthy</strong> (Father of AI, 1956)</span>
                        <span class="mindmap-chip"><strong>Dartmouth Workshop</strong> (Coined "AI")</span>
                        <span class="mindmap-chip"><strong>Marvin Minsky</strong> (Dartmouth Co-founder)</span>
                        <span class="mindmap-chip"><strong>AI Winters</strong> (1974-80 &amp; 1987-93)</span>
                        <span class="mindmap-chip"><strong>Rational Agent</strong> (PEAS Framework)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Key Milestones &amp; Theoretical Concepts</span>
                        <span class="lang-hi">प्रमुख मील के पत्थर एवं सैद्धांतिक संकल्पनाएं</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Alan Turing &amp; Turing Test (1950):</strong> In paper <em>"Computing Machinery and Intelligence"</em>, Turing posed "Can machines think?" and proposed the <strong>Turing Test (Imitation Game)</strong>: if a human interrogator cannot reliably distinguish between human and machine text responses, the machine is deemed intelligent.</span>
                            <span class="lang-hi"><strong>एलन ट्यूरिंग एवं ट्यूरिंग टेस्ट (1950):</strong> अपने ऐतिहासिक शोधपत्र में पूछा "क्या मशीनें सोच सकती हैं?" तथा <strong>इमिटेशन गेम (ट्यूरिंग टेस्ट)</strong> प्रस्तुत किया: यदि मानव परीक्षक बातचीत में यह न पहचान सके कि जवाब मशीन दे रही है या मनुष्य, तो मशीन बुद्धिमान मानी जाएगी।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>John McCarthy &amp; Dartmouth Conference (1956):</strong> John McCarthy (Father of AI) coined the term <em>"Artificial Intelligence"</em> at the 1956 Dartmouth Summer Research Project alongside Marvin Minsky, Nathaniel Rochester, and Claude Shannon. Invented LISP programming language (1958).</span>
                            <span class="lang-hi"><strong>जॉन मैकार्थी एवं डार्टमाउथ सम्मेलन (1956):</strong> जॉन मैकार्थी (AI के जनक) ने 1956 के डार्टमाउथ सम्मेलन में <em>"आर्टिफिशियल इंटेलिजेंस"</em> शब्द गढ़ा। इन्होंने AI की प्रसिद्ध भाषा LISP (1958) का भी आविष्कार किया।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>AI Winters:</strong> Periods of reduced funding and interest due to unmet expectations. <strong>1st AI Winter (1974-1980):</strong> Triggered by Lighthill Report (1973) and DARPA funding cuts. <strong>2nd AI Winter (1987-1993):</strong> Collapse of specialized LISP hardware market and commercial expert systems.</span>
                            <span class="lang-hi"><strong>AI विंटर्स (शीतकाल):</strong> अत्यधिक उम्मीदों के टूटने से फंडिंग में भारी गिरावट का दौर। <strong>पहला शीतकाल (1974-80):</strong> लाइटहिल रिपोर्ट व DARPA कटौतियों के कारण। <strong>दूसरा शीतकाल (1987-93):</strong> LISP मशीनों और एक्सपर्ट सिस्टम्स बाजार के पतन के कारण।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> John McCarthy coined the term "Artificial Intelligence" in 1956 and is known as the Father of AI; Alan Turing created the Turing Test in 1950!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> जॉन मैकार्थी ने 1956 में 'आर्टिफिशियल इंटेलिजेंस' शब्द गढ़ा और उन्हें AI का जनक कहा जाता है; एलन ट्यूरिंग ने 1950 में ट्यूरिंग टेस्ट प्रस्तुत किया!</span>
                </div>
            </div>
        </div>

        <!-- Branch 2: Classification by Capability & Functionality -->
        <div class="mindmap-node epoch-ancient">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-sitemap" style="color: #0284c7;"></i>
                    <span class="lang-en">2. Classification &amp; Types of AI</span>
                    <span class="lang-hi">2. AI का संपूर्ण वर्गीकरण एवं प्रकार</span>
                </h4>
                <span class="mindmap-node-tag">ANI • AGI • ASI • Hintze</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Taxonomies &amp; Functional Classes</span>
                        <span class="lang-hi">वर्गीकरण श्रेणियां एवं प्रकार</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Narrow AI (ANI)</strong> (Weak AI, Single Task)</span>
                        <span class="mindmap-chip"><strong>General AI (AGI)</strong> (Strong AI, Human-Level)</span>
                        <span class="mindmap-chip"><strong>Super AI (ASI)</strong> (Surpasses Humans)</span>
                        <span class="mindmap-chip"><strong>Reactive Machines</strong> (Deep Blue 1997)</span>
                        <span class="mindmap-chip"><strong>Limited Memory</strong> (Self-Driving Cars)</span>
                        <span class="mindmap-chip"><strong>Theory of Mind</strong> (Social/Emotions)</span>
                        <span class="mindmap-chip"><strong>Self-Awareness</strong> (Consciousness)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Functional Capabilities &amp; Real-World Examples</span>
                        <span class="lang-hi">कार्यात्मक क्षमताएं एवं व्यावहारिक उदाहरण</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Classification by Capabilities:</strong> <strong>Narrow AI (Weak AI):</strong> Dedicated to single specific task; cannot generalize (Siri, Alexa, AlphaGo, recommendation engines). All existing AI today is Narrow AI. <strong>General AI (AGI):</strong> Hypothetical system possessing human-level cognitive ability across diverse domains. <strong>Super AI (ASI):</strong> Hypothetical stage where machine intelligence surpasses collective human intelligence.</span>
                            <span class="lang-hi"><strong>क्षमता आधारित वर्गीकरण:</strong> <strong>नैरो AI (कमजोर AI):</strong> केवल एक विशिष्ट कार्य में दक्ष (सिरी, एलेक्सा, अल्फागो, चैटजीपीटी)। आज मौजूद समस्त AI नैरो AI है। <strong>जनरल AI (AGI):</strong> मानव मस्तिष्क के समान बहु-क्षेत्रीय बुद्धिमत्ता (काल्पनिक/अनुसंधानरत)। <strong>सुपर AI (ASI):</strong> मानव से श्रेष्ठ बुद्धिमत्ता (काल्पनिक)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Arend Hintze Functional Classification:</strong> <strong>1. Reactive Machines:</strong> No memory; cannot use past experiences (IBM Deep Blue chess computer, 1997). <strong>2. Limited Memory:</strong> Stores past data for short windows to inform immediate decisions (autonomous self-driving cars). <strong>3. Theory of Mind:</strong> Understands human emotions, social intentions (in development). <strong>4. Self-Awareness:</strong> Possesses consciousness, self-reflection (theoretical).</span>
                            <span class="lang-hi"><strong>आर्एंड हिंट्ज़े का कार्यात्मक वर्गीकरण:</strong> <strong>1. रिएक्टिव मशीनें:</strong> कोई स्मृति नहीं, केवल वर्तमान पर निर्णय (IBM डीप ब्लू शतरंज कंप्यूटर 1997)। <strong>2. लिमिटेड मेमोरी:</strong> अल्पकालिक डेटा संचयन (टेस्ला की सेल्फ-ड्राइविंग कारें)। <strong>3. थ्योरी ऑफ माइंड:</strong> मानव भावनाओं व सामाजिक संवेदनाओं की समझ। <strong>4. आत्म-जागरूकता (Self-Awareness):</strong> चेतना युक्त मशीनें।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> IBM Deep Blue defeated World Chess Champion Garry Kasparov in 1997 (Reactive Machine); all AI systems in existence today belong to Narrow/Weak AI!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> IBM डीप ब्लू ने 1997 में विश्व चैंपियन गैरी कास्पारोव को हराया (रिएक्टिव मशीन); वर्तमान में मौजूद सभी AI प्रणालियां 'नैरो AI' (Narrow AI) के अंतर्गत आती हैं!</span>
                </div>
            </div>
        </div>

        <!-- Branch 3: Core Subfields: ML, DL, NLP & Computer Vision -->
        <div class="mindmap-node epoch-classical">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-layer-group" style="color: #7c3aed;"></i>
                    <span class="lang-en">3. Core AI Subfields &amp; Technologies</span>
                    <span class="lang-hi">3. AI के प्रमुख उप-क्षेत्र एवं तकनीक</span>
                </h4>
                <span class="mindmap-node-tag">ML • DL • NLP • CV</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Subfields &amp; Specialized Disciplines</span>
                        <span class="lang-hi">उप-क्षेत्र एवं विशिष्ट तकनीकें</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Machine Learning</strong> (Subset of AI)</span>
                        <span class="mindmap-chip"><strong>Deep Learning</strong> (Neural Subset of ML)</span>
                        <span class="mindmap-chip"><strong>NLP</strong> (Text &amp; Speech Understanding)</span>
                        <span class="mindmap-chip"><strong>Computer Vision</strong> (Image &amp; Video)</span>
                        <span class="mindmap-chip"><strong>Expert Systems</strong> (Inference Engine)</span>
                        <span class="mindmap-chip"><strong>Robotics</strong> (Actuators &amp; Control)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Subfield Interactions &amp; Real-World Mechanisms</span>
                        <span class="lang-hi">पारस्परिक संबंध एवं कार्यात्मक प्रक्रियाएं</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>The AI Hierarchy:</strong> AI is the overarching umbrella -> Machine Learning is a subset of AI (learning patterns from data) -> Deep Learning is a subset of ML (using deep multi-layered artificial neural networks).</span>
                            <span class="lang-hi"><strong>AI पदानुक्रम:</strong> AI व्यापक छत्र है -> मशीन लर्निंग (ML) AI का उप-क्षेत्र है (डेटा से सीखना) -> डीप लर्निंग (DL) ML का उप-क्षेत्र है (बहुस्तरीय कृत्रिम न्यूरल नेटवर्क का प्रयोग)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Natural Language Processing (NLP):</strong> Enables machines to understand, interpret, and manipulate human language. Key pipeline: Tokenization, Stopword removal, Stemming, Lemmatization, Named Entity Recognition (NER), Sentiment Analysis.</span>
                            <span class="lang-hi"><strong>नेचुरल लैंग्वेज प्रोसेसिंग (NLP):</strong> मशीनों द्वारा मानव भाषा को समझने और उत्पन्न करने की तकनीक। मुख्य चरण: टोकनाइजेशन, स्टॉपवर्ड रिमूवल, स्टेमिंग, लेमैटाइजेशन, नेम्ड एंटिटी रिकॉग्निशन (NER)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Computer Vision &amp; Expert Systems:</strong> <strong>Computer Vision:</strong> Extracts high-level understanding from digital images and videos (Object Detection via YOLO, Face Recognition, OCR). <strong>Expert Systems:</strong> Emulates human expert decision-making via Knowledge Base (facts/rules) and Inference Engine (e.g. MYCIN for bacterial infections).</span>
                            <span class="lang-hi"><strong>कंप्यूटर विजन एवं एक्सपर्ट सिस्टम्स:</strong> <strong>कंप्यूटर विजन:</strong> डिजिटल छवियों से अर्थ निकालना (ऑब्जेक्ट डिटेक्शन, फेशियल रिकॉग्निशन)। <strong>एक्सपर्ट सिस्टम:</strong> मानव विशेषज्ञ जैसी सलाह देने वाली प्रणाली; घटक: नॉलेज बेस व इन्फेरेंस इंजन (उदा. MYCIN)।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Deep Learning is a subset of Machine Learning, which is a subset of AI; Expert Systems consist of a Knowledge Base and an Inference Engine!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> डीप लर्निंग मशीन लर्निंग का और मशीन लर्निंग AI का उप-क्षेत्र है; एक्सपर्ट सिस्टम के दो मुख्य भाग 'नॉलेज बेस' व 'इन्फेरेंस इंजन' होते हैं!</span>
                </div>
            </div>
        </div>

        <!-- Branch 4: Generative AI, LLMs & Foundation Models -->
        <div class="mindmap-node epoch-medieval">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-robot" style="color: #d97706;"></i>
                    <span class="lang-en">4. Generative AI &amp; LLMs</span>
                    <span class="lang-hi">4. जनरेटिव एआई एवं लार्ज लैंग्वेज मॉडल्स (LLM)</span>
                </h4>
                <span class="mindmap-node-tag">Transformers • Vaswani 2017</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Pillars of GenAI &amp; Leading Models</span>
                        <span class="lang-hi">जनरेटिव AI के स्तंभ एवं प्रमुख मॉडल्स</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Transformers</strong> (Vaswani et al. 2017)</span>
                        <span class="mindmap-chip"><strong>Self-Attention</strong> (Attention Is All You Need)</span>
                        <span class="mindmap-chip"><strong>ChatGPT</strong> (OpenAI, Nov 2022)</span>
                        <span class="mindmap-chip"><strong>Gemini</strong> (Google Multimodal)</span>
                        <span class="mindmap-chip"><strong>Claude</strong> (Anthropic)</span>
                        <span class="mindmap-chip"><strong>LLaMA</strong> (Meta Open-Weights)</span>
                        <span class="mindmap-chip"><strong>Bhashini</strong> (Govt of India AI)</span>
                        <span class="mindmap-chip"><strong>RLHF &amp; Hallucination</strong></span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Generative Mechanics &amp; Terminology</span>
                        <span class="lang-hi">जनरेटिव कार्यप्रणाली एवं तकनीकी शब्दावली</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Discriminative vs Generative AI:</strong> Discriminative models classify data ($P(Y|X)$ e.g. spam vs non-spam). Generative AI models generate new novel synthetic content ($P(X)$ text, images, audio, video, code) based on learned patterns.</span>
                            <span class="lang-hi"><strong>भेदभावपूर्ण बनाम जनरेटिव AI:</strong> डिस्क्रिमिनिटिव मॉडल डेटा का वर्गीकरण करते हैं (स्पैम या नहीं)। जनरेटिव AI सीखे गए पैटर्नों के आधार पर नया मौलिक कंटेंट (टेक्स्ट, चित्र, ऑडियो, वीडियो, कोड) रचता है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Transformer Architecture (2017):</strong> Landmark paper <em>"Attention Is All You Need"</em> by Ashish Vaswani et al. (Google Research) introduced the <strong>Self-Attention Mechanism</strong>, eliminating recurrent loops and enabling massive parallel training of LLMs on GPUs. Foundation of GPT, BERT, Gemini.</span>
                            <span class="lang-hi"><strong>ट्रांसफॉर्मर वास्तुकला (2017):</strong> गूगल के शोधपत्र <em>"Attention Is All You Need"</em> (आशीष वासवानी आदि) ने <strong>सेल्फ-अटेंशन मैकेनिज्म</strong> दिया; इसने आवर्ती लूप हटाकर GPU पर समानांतर ट्रेनिंग संभव बनाई। GPT, BERT, Gemini का आधार।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Key LLM Concepts:</strong> <strong>Hallucination:</strong> Phenomenon where LLM generates plausible-sounding but factually incorrect or fabricated statements. <strong>RLHF:</strong> Reinforcement Learning from Human Feedback used to align AI outputs with human values and safety.</span>
                            <span class="lang-hi"><strong>प्रमुख LLM शब्दावली:</strong> <strong>हैलुसिनेशन (Hallucination):</strong> जब AI मॉडल आत्मविश्वास के साथ पूरी तरह गलत या मनगढ़ंत तथ्य प्रस्तुत करता है। <strong>RLHF:</strong> मानव प्रतिक्रिया आधारित सुदृढीकरण शिक्षण, जो मॉडल को सुरक्षित बनाता है।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Transformer architecture was introduced in 2017 in paper "Attention Is All You Need"; Hallucination refers to AI generating false information confidently!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> ट्रांसफॉर्मर आर्किटेक्चर 2017 में "Attention Is All You Need" शोधपत्र द्वारा आया; AI द्वारा गलत तथ्य गढ़ने को 'हैलुसिनेशन' कहते हैं!</span>
                </div>
            </div>
        </div>

        <!-- Branch 5: Ethics, Bias, Safety & Governance -->
        <div class="mindmap-node epoch-revolt">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-balance-scale" style="color: #dc2626;"></i>
                    <span class="lang-en">5. AI Ethics, Bias &amp; Safety</span>
                    <span class="lang-hi">5. AI नैतिकता, पूर्वाग्रह, सुरक्षा एवं वैश्विक कानून</span>
                </h4>
                <span class="mindmap-node-tag">EU AI Act 2024 • Deepfakes</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Ethical Challenges &amp; Legal Frameworks</span>
                        <span class="lang-hi">नैतिक चुनौतियां एवं विधिक ढांचे</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Algorithmic Bias</strong> (Training Data Bias)</span>
                        <span class="mindmap-chip"><strong>Black-Box Problem</strong> (Lack of Clarity)</span>
                        <span class="mindmap-chip"><strong>Explainable AI (XAI)</strong> (Transparency)</span>
                        <span class="mindmap-chip"><strong>Deepfakes</strong> (Synthetic Disinformation)</span>
                        <span class="mindmap-chip"><strong>EU AI Act (2024)</strong> (World's 1st Law)</span>
                        <span class="mindmap-chip"><strong>Risk Classification</strong> (Unacceptable/High)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Ethical Dimensions &amp; Global AI Governance</span>
                        <span class="lang-hi">नैतिक आयाम एवं वैश्विक AI नियमन</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Algorithmic Bias &amp; Fairness:</strong> When AI models reproduce and amplify historical human prejudices present in their training datasets (e.g. discriminatory hiring algorithms, facial recognition misidentifying minority populations).</span>
                            <span class="lang-hi"><strong>एल्गोरिथमिक पूर्वाग्रह (Bias):</strong> जब AI मॉडल अपने ट्रेनिंग डेटा में मौजूद मानवीय पूर्वाग्रहों को दोहराते और बढ़ाते हैं (उदा. चेहरे की पहचान में त्रुटियां, भर्ती में पक्षपात)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Explainable AI (XAI):</strong> Set of processes and methods that allow human users to comprehend and trust the results and output created by machine learning algorithms, overcoming the "Black-Box" problem where internal reasoning is opaque.</span>
                            <span class="lang-hi"><strong>व्याख्यात्मक AI (XAI):</strong> ऐसी प्रणालियां जो 'ब्लैक-बॉक्स समस्या' को हल कर यह स्पष्ट करती हैं कि AI ने कोई विशिष्ट निर्णय क्यों और कैसे लिया।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>European Union AI Act (2024):</strong> World's first comprehensive horizontal legal regulation for artificial intelligence. Categorizes AI into 4 risk tiers: <strong>Unacceptable Risk:</strong> Banned (social scoring, biometric mass surveillance), <strong>High Risk:</strong> Strict compliance (critical infrastructure, education, law enforcement), <strong>Limited Risk:</strong> Transparency/watermarking (chatbots, deepfakes), <strong>Minimal Risk:</strong> Unregulated.</span>
                            <span class="lang-hi"><strong>यूरोपीय संघ AI अधिनियम (2024):</strong> विश्व का पहला व्यापक AI कानून। 4 जोखिम स्तर: <strong>अस्वीकार्य जोखिम:</strong> प्रतिबंधित (सोशल स्कोरिंग), <strong>उच्च जोखिम:</strong> कठोर नियम (स्वास्थ्य, भर्ती, कानून), <strong>सीमित जोखिम:</strong> पारदर्शिता व वाटरमार्क (डीपफेक), <strong>न्यूनतम जोखिम:</strong> अनियंत्रित।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> The European Union passed the world's first comprehensive AI Act in 2024 with risk-based categorization; XAI aims to make AI decisions interpretable!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> यूरोपीय संघ (EU) ने 2024 में विश्व का पहला व्यापक 'AI एक्ट' पारित किया; XAI का उद्देश्य AI निर्णयों को पारदर्शी बनाना है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 6: National AI Mission & Uttar Pradesh AI Ecosystem -->
        <div class="mindmap-node epoch-modern">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-flag-checkered" style="color: #4f46e5;"></i>
                    <span class="lang-en">6. India &amp; UP State AI Initiatives</span>
                    <span class="lang-hi">6. राष्ट्रीय AI मिशन एवं उप्र AI पहल</span>
                </h4>
                <span class="mindmap-node-tag">IndiaAI • Lucknow AI City</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">National &amp; State Flagship Schemes</span>
                        <span class="lang-hi">राष्ट्रीय एवं राज्य स्तरीय प्रमुख योजनाएं</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>#AIforAll</strong> (NITI Aayog Strategy, 2018)</span>
                        <span class="mindmap-chip"><strong>IndiaAI Mission</strong> (₹10,372 Cr, 2024)</span>
                        <span class="mindmap-chip"><strong>AIRAWAT</strong> (AI Supercomputer, C-DAC)</span>
                        <span class="mindmap-chip"><strong>Digital Bhashini</strong> (Language AI)</span>
                        <span class="mindmap-chip"><strong>Lucknow AI City</strong> (Nadarganj, India's 1st)</span>
                        <span class="mindmap-chip"><strong>Trinetra 2.0</strong> (UP Police AI App)</span>
                        <span class="mindmap-chip"><strong>IIT Kanpur CoE</strong> (AI &amp; Cyber Security)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">National Strategy &amp; Uttar Pradesh AI City</span>
                        <span class="lang-hi">राष्ट्रीय रणनीति एवं उत्तर प्रदेश AI सिटी</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>National AI Strategy (#AIforAll):</strong> Released by NITI Aayog in June 2018 focusing on 5 core sectors: Healthcare, Agriculture, Education, Smart Cities/Infrastructure, Smart Mobility. Emphasizes social inclusion.</span>
                            <span class="lang-hi"><strong>राष्ट्रीय AI रणनीति (#AIforAll):</strong> नीति आयोग द्वारा जून 2018 में जारी; 5 प्रमुख क्षेत्रों पर केंद्रित: स्वास्थ्य, कृषि, शिक्षा, स्मार्ट सिटीज तथा स्मार्ट मोबिलिटी।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>IndiaAI Mission (Approved March 2024):</strong> ₹10,372 crore national initiative by Cabinet to establish 10,000+ GPUs public-private AI compute capacity, develop indigenous sovereign foundation models, and fund AI startups.</span>
                            <span class="lang-hi"><strong>इंडिया AI मिशन (मार्च 2024):</strong> केंद्रीय मंत्रिमंडल द्वारा स्वीकृत ₹10,372 करोड़ की राष्ट्रीय योजना; 10,000 से अधिक GPU की सुपरकंप्यूटिंग क्षमता और स्वदेशी AI मॉडल तैयार करना।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Lucknow AI City (India's First AI City):</strong> Uttar Pradesh government developing India's first designated AI City in Nadarganj, Lucknow; housing AI research hubs, global tech headquarters, incubation centers, and grade-A offices.</span>
                            <span class="lang-hi"><strong>लखनऊ AI सिटी (भारत की पहली AI सिटी):</strong> उत्तर प्रदेश सरकार लखनऊ के नादरगंज में भारत की प्रथम AI सिटी विकसित कर रही है; जहाँ AI रिसर्च हब, वैश्विक टेक मुख्यालय व इन्क्यूबेशन सेंटर होंगे।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Trinetra 2.0 (UP Police AI Tool):</strong> Comprehensive facial recognition and crime analytics tool developed for UP Police containing database of 9.5+ lakh criminals for instant crime detection and crowd monitoring at Maha Kumbh.</span>
                            <span class="lang-hi"><strong>त्रिनेत्र 2.0 (उप्र पुलिस AI ऐप):</strong> उप्र पुलिस का फेशियल रिकॉग्निशन एवं क्राइम एनालिटिक्स ऐप जिसमें 9.5 लाख से अधिक अपराधियों का डेटाबेस है; महाकुंभ व मेलों में सुरक्षा निगरानी हेतु प्रयुक्त।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> India's first AI City is being established in Lucknow (Nadarganj, UP); Trinetra 2.0 is the UP Police AI crime-detection application!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> भारत की पहली AI सिटी लखनऊ (नादरगंज, उप्र) में स्थापित की जा रही है; 'त्रिनेत्र 2.0' उप्र पुलिस का AI आधारित अपराध जांच ऐप है!</span>
                </div>
            </div>
        </div>

    </div>
</div>
'''

from mindmap_t7_ml import mm_t7
from mindmap_t8_dl import mm_t8
from mindmap_t9_bigdata import mm_t9
from mindmap_t10_iot import mm_t10

batch2_map = {
    'artificial-intelligence': mm_t6,
    'machine-learning': mm_t7,
    'deep-learning': mm_t8,
    'big-data-processing': mm_t9,
    'internet-of-things': mm_t10
}

print("Starting Batch 2 replacements (Topics 6-10)...")
for topic, new_mm in batch2_map.items():
    file_path = os.path.join('upsssc-computer', topic, 'index.html')
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    m = pattern.search(content)
    if not m:
        print(f"ERROR: Could not find Card 1 pattern in {topic}")
        continue
    
    updated_content = content[:m.start()] + new_mm + "\n\n" + content[m.end():]
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    print(f"SUCCESS: Replaced Card 1 in {topic}")

print("Batch 2 completed successfully!")

