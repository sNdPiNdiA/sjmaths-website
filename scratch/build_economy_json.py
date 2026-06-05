import json
import os

ENG_DIR = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\HarappanIndus-Valley-Civilisation\Economic-Aspects-of-Indus-Valley-Civilisation"
HIN_DIR = os.path.join(ENG_DIR, "hi")
os.makedirs(HIN_DIR, exist_ok=True)

# English base structure
eng_data = {
    "breadcrumbs": {
        "parent": "UPSC Syllabus",
        "parentUrl": "/upsc/",
        "current": "Economic Aspects of IVC"
    },
    "hero": {
        "title": "Economic Aspects of the Indus Valley Civilisation",
        "description": "Master the agrarian foundations, craft specialization, metal trade networks, weight standards, and external maritime connections of the Harappan Civilisation for UPSC GS-1."
    },
    "labels": {
        "clickToExpand": "Click to expand details",
        "mockIntro": {
            "title": "Interactive UPSC Mock Test",
            "description": "Assess your understanding of Harappan trade, agriculture, metallurgy, and economy. This timed test contains 10 high-yield, exam-standard questions with negative marking.",
            "startBtn": "Start Mock Test"
        },
        "mockPlay": {
            "prevBtn": "Previous Question",
            "nextBtn": "Next Question",
            "submitBtn": "Submit Test"
        }
    },
    "timeline": {
        "title": "Development of the Harappan Economy",
        "description": "Track the technological and trade milestones that defined the economy of the Indus Valley Civilisation.",
        "cards": [
            {
                "period": "Early Harappan Phase",
                "date": "c. 3300 BCE - 2600 BCE",
                "details": "Development of agrarian surplus, early craft workshops, local trade circuits, and initial standardization of pottery styles and raw material procurement."
            },
            {
                "period": "Mature Harappan Phase",
                "date": "c. 2600 BCE - 1900 BCE",
                "details": "Apex of urban planning, unified weight systems, industrial-scale craft workshops, and robust maritime trade links with Mesopotamia and the Persian Gulf."
            },
            {
                "period": "Late Harappan Phase",
                "date": "c. 1900 BCE - 1300 BCE",
                "details": "Decentralization of craft production, breakdown of international trade networks, regionalization of weights, and shift from long-distance to local barter trade."
            }
        ]
    },
    "mnemonics": {
        "title": "Mnemonics & Memory Hacks",
        "description": "Use these visual memory hooks to retain critical facts about Harappan trade, agriculture, and material procurement.",
        "items": [
            {
                "title": "Mnemonic 1: External Trade Partners in Cuneiform",
                "phrase": "\"Me-Di-Ma (Meluhha, Dilmun, Makan)\"",
                "decryption": "Remember the three lands mentioned in Mesopotamian cuneiform texts: **Me**luhha (Indus region), **Di**lmun (Bahrain, the clean/sunland), and **Ma**kan (Makran coast/Oman)."
            },
            {
                "title": "Mnemonic 2: Raw Material Sourcing sites",
                "phrase": "\"Khet-Cop, Short-Lap, Loth-Car (Khetri-Copper, Shortughai-Lapis, Lothal-Carnelian)\"",
                "decryption": "Sourcing links: **Khet**ri mines in Rajasthan for **Cop**per; **Short**ughai colony in Afghanistan for **Lap**is Lazuli; **Loth**al (and Gujarat sites) for **Car**nelian beads."
            },
            {
                "title": "Mnemonic 3: Agrarian Indicators",
                "phrase": "\"Bana-Plough, Kali-Field (Banawali-Plough, Kalibangan-Field)\"",
                "decryption": "Crucial agrarian evidence: **Bana**wali yielded a terracotta model of a **plough**; **Kali**bangan yielded a double-ploughed agricultural **field**."
            }
        ]
    },
    "flashcards": {
        "title": "Active Recall Flashcards",
        "description": "Use these active recall cards to reinforce technical details of the Harappan economic system.",
        "items": [
            {
                "question": "What evidence indicates the cultivation of cotton in the Indus Valley Civilisation?",
                "answer": "The discovery of <strong>woven cotton textile fragments</strong> at Mohenjo-daro and traces of cotton seeds. The Greeks called cotton <strong>sindon</strong>, derived from the word 'Sindhu' (Indus).",
                "icon": "fa-seedling"
            },
            {
                "question": "Describe the mathematical ratio used in the Harappan weight system.",
                "answer": "For lower denominations, weights followed a <strong>binary system</strong> (1, 2, 4, 8, 16, 32, 64), while higher values transitioned into a <strong>decimal system</strong> (160, 200, 320, 640, 1600, 3200, etc.), with a unit weight of approx. 13.63g.",
                "icon": "fa-scale-balanced"
            },
            {
                "question": "Where is the earliest and most direct evidence of canal irrigation found?",
                "answer": "At <strong>Shortughai</strong> in northern Afghanistan, though generally canal irrigation was rare inside the main alluvial plains, where agriculture relied on seasonal floodwater and wells.",
                "icon": "fa-water"
            },
            {
                "question": "Which two sites were dedicated centers for the manufacture of shell objects?",
                "answer": "<strong>Balakot</strong> and <strong>Nageshwar</strong>. Both are coastal sites rich in marine shells, specializing in making bangles, ladles, and inlay pieces.",
                "icon": "fa-shuttle-space"
            },
            {
                "question": "Which cuneiform term refers to the Indus region, and how is its trade described?",
                "answer": "Mesopotamian texts refer to the Indus region as <strong>Meluhha</strong>, describing it as a land of exotic timbers, carnelian, lapis lazuli, gold, and copper, whose ships docked at Akkad.",
                "icon": "fa-ship"
            }
        ]
    },
    "deepDive": {
        "title": "Syllabus Core Study Notes (Deep-Dive)",
        "description": "Master the agriculture, craft workshops, weights, and trade networks of the Indus Valley Civilisation for UPSC GS-1.",
        "sections": [
            {
                "title": "1. Agriculture and Animal Husbandry",
                "content": """<p>The urban structure of Harappan towns was sustained by a robust agricultural surplus generated in rural hinterlands, using innovative farming and water management systems.</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-seedling"></i> Crops & Agricultural Technology</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>Principal Crops:</strong> Wheat, barley, peas, lentils, mustard, sesame, and chickpeas. Rice husks have been recovered from Lothal and Rangpur, showing localized cultivation.</li>
      <li><strong>Cotton:</strong> The Harappans were the first in the world to cultivate cotton (Greek: <em>Sindon</em>), which was exported to the West.</li>
      <li><strong>Tillage Evidence:</strong> A ploughed field showing grid furrows (double-cropping pattern of mustard and horse gram/peas) was excavated at <strong>Kalibangan</strong>. Terracotta models of ploughs have been recovered from <strong>Banawali</strong> (Haryana) and Jawaiwala (Pakistan).</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-droplet"></i> Irrigation, Water Storage & Livestock</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>Irrigation:</strong> Direct traces of canals are found at <strong>Shortughai</strong> (Afghanistan). In the plains, alluvial inundation and well irrigation (like the public wells at Mohenjo-daro) were mainstays. <em>Gabarbands</em> (stone dams) in Baluchistan collected slope runoff.</li>
      <li><strong>Water Reservoirs:</strong> Dholavira features massive stone-cut reservoirs to store rainwater, indicating sophisticated dryland water management.</li>
      <li><strong>Animal Husbandry:</strong> Domestication of humped cattle (zebu), sheep, goats, pigs, buffaloes, asses, and camels. Humped bulls were highly revered.</li>
      <li><strong>The Horse Controversy:</strong> Horse bones have been reported at <strong>Surkotada</strong> (Gujarat), but horse depictions are absent on Harappan seals and pottery. The animal was not a central part of Harappan socio-economic life.</li>
    </ul>
  </div>
</div>""",
                "masteryZone": []
            },
            {
                "title": "2. Craft Production, Metallurgy, and Weight Systems",
                "content": """<p>Craft specialization and state-monitored weight systems highlight the centralized quality control and industrial output of Harappan cities.</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-hammer"></i> Craft Specialized Centers & Metallurgy</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>Bead-Making:</strong> Specialized workshops operated at <strong>Chanhudaro</strong> and <strong>Lothal</strong>. Processes involved drilling, heating carnelian to acquire red color, and etching designs with acid.</li>
      <li><strong>Shell-Working:</strong> Coastal specialized hubs at <strong>Nageshwar</strong> and <strong>Balakot</strong> manufactured shell bangles, ladles, and inlay work.</li>
      <li><strong>Metallurgy:</strong> Mastered copper and tin alloying to produce bronze. <strong>Copper</strong> was sourced from Khetri mines (Rajasthan) and Oman; <strong>tin</strong> was imported from Afghanistan and Central Asia. They created bronze chisels, saws, and axes. <strong>Iron was completely unknown.</strong></li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-scale-balanced"></i> Weight Standardization & Measures</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>Weights Material & Shape:</strong> Made of a fine-grained siliceous stone called <strong>chert</strong>, and were typically cubical. They were unmarked and manufactured to precise standards.</li>
      <li><strong>Weight Math:</strong> Followed a <strong>binary scale</strong> for lower denominations (1, 2, 4, 8, 16, 32, 64) and a <strong>decimal scale</strong> for higher denominations (160, 200, 320, 640, 1600, 3200, 6400, etc.). The 16th unit served as a key standard, equivalent to approx. 13.63 grams.</li>
      <li><strong>Measurement Scales:</strong> An ivory scale was discovered at Mohenjo-daro, a shell scale at Lothal, and a bronze scale at Harappa, proving standardization in linear measures.</li>
    </ul>
  </div>
</div>""",
                "masteryZone": []
            },
            {
                "title": "3. Trade Networks, Transport, and Maritime Communications",
                "content": """<p>The Harappan economy relied heavily on extensive regional overland networks and international maritime trade routes connecting the Indus Valley to the Near East.</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-globe"></i> Procurement, External Trade & Mesopotamian Links</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>Procurement Colonies:</strong> Established at <strong>Shortughai</strong> in northern Afghanistan near Lapis Lazuli mines, and at Badakhshan.</li>
      <li><strong>Mesopotamian Cuneiform Texts:</strong> Dating to Sargon of Akkad (c. 2350 BCE), they record trade with three key regions: <strong>Dilmun</strong> (Bahrain, Persian Gulf), <strong>Makan</strong> (Oman/Makran coast, source of copper), and <strong>Meluhha</strong> (the Indus region).</li>
      <li><strong>Trade Cargo:</strong> Exports included carnelian, lapis lazuli, gold, copper, peacock figurines, and ivory products in exchange for Mesopotamian wool, oil, and textiles.</li>
      <li><strong>Currency Absence:</strong> Trade relied on a <strong>barter system</strong>. Coins did not exist. Seals and clay sealings were used to secure trade packets.</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-ship"></i> Transport Technology & The Lothal Dockyard</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>Lothal Dockyard:</strong> A massive trapezoidal brick basin measuring 214 x 36 meters. Connected to a tributary of the Sabarmati, it featured an inlet channel, a spillway, and a wooden lock-gate system to maintain water levels during low tides, facilitating shipping.</li>
      <li><strong>Land Transport:</strong> Solid-wheeled wooden bullock carts (represented by abundant terracotta toy carts and clay wheel ruts in archaeological strata).</li>
      <li><strong>Water Transport:</strong> Flat-bottomed river boats and masted maritime vessels, depicted on Harappan seals and clay amulets.</li>
    </ul>
  </div>
</div>""",
                "masteryZone": []
            }
        ]
    },
    "traps": {
        "title": "UPSC Warning Alerts (Traps to Avoid)",
        "items": [
            "<strong>Trap 1:</strong> Do not confuse Khetri copper with tin. Copper was sourced from the Khetri mines of Rajasthan (and Oman), while tin was imported from Afghanistan and Iran to alloy copper into bronze.",
            "<strong>Trap 2:</strong> Watch out for statements claiming canal irrigation was common. Inside the main alluvial valleys of the Indus and Ghaggar, canal traces are absent. The only clear canals are found at <strong>Shortughai</strong> in Afghanistan.",
            "<strong>Trap 3:</strong> Do not assume the Harappan economy was based on monetary currency. Metal coinage did not exist; trade was carried out purely through barter, facilitated by seals and sealings for cargo security and authentication.",
            "<strong>Trap 4:</strong> Be careful with statements about the horse. While horse bones are found at Surkotada, the horse is NOT depicted on seals, and there is no evidence of horse-drawn chariots. The economy was powered by humped bulls and bullock carts.",
            "<strong>Trap 5:</strong> Do not select options identifying iron as a trade commodity. <strong>Iron was unknown</strong> to the Harappans; it was only introduced during the Later Vedic Period (c. 1000 BCE)."
        ]
    },
    "practiceQuestions": [],
    "mockTestQuestions": []
}

# Hindi base structure
hin_data = {
    "breadcrumbs": {
        "parent": "यूपीएससी पाठ्यक्रम",
        "parentUrl": "/upsc/",
        "current": "सिंधु घाटी सभ्यता के आर्थिक पहलू"
    },
    "hero": {
        "title": "सिंधु घाटी सभ्यता के आर्थिक पहलू",
        "description": "यूपीएससी परीक्षा (GS-1) के लिए हड़प्पा सभ्यता के कृषि आधार, शिल्प विशिष्टता, धातु व्यापार नेटवर्क, भार मानक और बाहरी समुद्री संबंधों का अध्ययन करें।"
    },
    "labels": {
        "clickToExpand": "विवरण देखने के लिए क्लिक करें",
        "mockIntro": {
            "title": "इंटरैक्टिव परीक्षा मॉक टेस्ट",
            "description": "हड़प्पा व्यापार, कृषि, धातु विज्ञान और अर्थव्यवस्था के संबंध में अपनी तैयारी का मूल्यांकन करें। इस समयबद्ध परीक्षण में 10 उच्च-स्तरीय यूपीएससी मानक के प्रश्न शामिल हैं।",
            "startBtn": "मॉक टेस्ट शुरू करें"
        },
        "mockPlay": {
            "prevBtn": "Previous Question",
            "nextBtn": "Next Question",
            "submitBtn": "Submit Test"
        }
    },
    "timeline": {
        "title": "हड़प्पा अर्थव्यवस्था का विकास",
        "description": "सिंधु घाटी सभ्यता की अर्थव्यवस्था को परिभाषित करने वाले तकनीकी और व्यापारिक मील के पत्थरों को समझें।",
        "cards": [
            {
                "period": "प्रारंभिक हड़प्पा काल",
                "date": "लगभग 3300 ईसा पूर्व - 2600 ईसा पूर्व",
                "details": "कृषि अधिशेष का विकास, प्रारंभिक शिल्प कार्यशालाएं, स्थानीय व्यापारिक मार्ग और मृदभांड शैली व कच्चे माल की प्राप्ति का प्रारंभिक मानकीकरण।"
            },
            {
                "period": "परिपक्व हड़प्पा काल",
                "date": "लगभग 2600 ईसा पूर्व - 1900 ईसा पूर्व",
                "details": "नगर नियोजन का चरमोत्कर्ष, एकीकृत भार प्रणाली, औद्योगिक स्तर की शिल्प कार्यशालाएं और मेसोपोटामिया व फारस की खाड़ी के साथ मजबूत समुद्री व्यापार संबंध।"
            },
            {
                "period": "उत्तर हड़प्पा काल",
                "date": "लगभग 1900 ईसा पूर्व - 1300 ईसा पूर्व",
                "details": "शिल्प उत्पादन का विकेंद्रीकरण, अंतर्राष्ट्रीय व्यापार नेटवर्क का पतन, भार प्रणालियों का क्षेत्रीयकरण और दूरस्थ व्यापार से स्थानीय वस्तु विनिमय (Barter) में संक्रमण।"
            }
        ]
    },
    "mnemonics": {
        "title": "याद रखने के सूत्र (Mnemonics)",
        "description": "यूपीएससी परीक्षा के लिए हड़प्पा व्यापार, कृषि और कच्चे माल की प्राप्ति के स्रोतों को आसानी से याद रखने के लिए इन सूत्रों का उपयोग करें।",
        "items": [
            {
                "title": "याद रखने का सूत्र 1: मेसोपोटामिया के ग्रंथों में विदेशी व्यापारिक भागीदार",
                "phrase": "\"मे-दि-मा (मेलुहा, दिलमुन, माकन)\"",
                "decryption": "मेसोपोटामिया के कीलाक्षर (Cuneiform) लेखों में उल्लिखित तीन क्षेत्रों को याद रखें: **मे**लुहा (सिंधु क्षेत्र), **दि**लमुन (बहरीन, स्वच्छ/सूर्य का देश), और **मा**कन (मकरान तट/ओमान)।"
            },
            {
                "title": "याद रखने का सूत्र 2: कच्चे माल की प्राप्ति के स्थल",
                "phrase": "\"खे-तां, शो-ला, लो-ला (खेत्री-तांबा, शोर्तुघई-लाजवर्त, लोथल-लाल अकीक)\"",
                "decryption": "कच्चे माल के स्रोत: **खे**त्री खदानें (राजस्थान) **तां**बे के लिए; **शो**र्तुघई (अफगानिस्तान) **ला**जवर्त (Lapis Lazuli) के लिए; **लो**थल (गुजरात) **ला**ल अकीक (Carnelian) के मोतियों के लिए।"
            },
            {
                "title": "याद रखने का सूत्र 3: कृषि के प्रमुख पुरातात्विक साक्ष्य",
                "phrase": "\"ब-हल, का-खेत (बनावली-हल, कालीबंगन-खेत)\"",
                "decryption": "महत्वपूर्ण कृषि साक्ष्य: **ब**नावली से **हल** का मिट्टी का मॉडल मिला; **का**लीबंगन से दोहरे जुते हुए **खेत** के साक्ष्य मिले।"
            }
        ]
    },
    "flashcards": {
        "title": "सक्रिय स्मरण फ्लैशकार्ड (Active Recall)",
        "description": "हड़प्पा अर्थव्यवस्था और कृषि प्रणालियों से संबंधित तकनीकी तथ्यों को याद रखने के लिए इन कार्डों का उपयोग करें।",
        "items": [
            {
                "question": "सिंधु घाटी सभ्यता में कपास की खेती के क्या साक्ष्य मिले हैं?",
                "answer": "मोहनजोदड़ो से <strong>सूती कपड़े के बुने हुए टुकड़े</strong> और कपास के बीजों के अवशेष मिले हैं। यूनानी लोग कपास को <strong>सिंडन (Sindon)</strong> कहते थे, जो 'सिंधु' शब्द से बना है।",
                "icon": "fa-seedling"
            },
            {
                "question": "हड़प्पा सभ्यता की वजन प्रणाली में प्रयुक्त गणितीय अनुपात क्या था?",
                "answer": "कम वजन के लिए <strong>द्वि-आधारी प्रणाली (Binary System: 1, 2, 4, 8, 16, 32, 64)</strong> थी, जबकि उच्च मूल्यों के लिए यह <strong>दशमलव प्रणाली (Decimal System: 160, 200, 320, 640, 1600, 3200 आदि)</strong> में बदल जाती थी। मानक इकाई लगभग 13.63 ग्राम थी।",
                "icon": "fa-scale-balanced"
            },
            {
                "question": "नहरों द्वारा सिंचाई का सबसे स्पष्ट और प्रारंभिक साक्ष्य कहाँ मिला है?",
                "answer": "उत्तरी अफगानिस्तान के <strong>शोर्तुघई</strong> में। हालांकि, मुख्य मैदानी क्षेत्रों में नहरों के साक्ष्य दुर्लभ हैं, जहाँ कृषि वर्षा बाढ़ और कुओं पर निर्भर थी।",
                "icon": "fa-water"
            },
            {
                "question": "शंख (Shell) की वस्तुएं बनाने के लिए कौन से दो स्थल विशेष रूप से प्रसिद्ध थे?",
                "answer": "<strong>बालाकोट</strong> और <strong>नागेश्वर</strong>। ये दोनों तटीय स्थल समुद्री शंख की उपलब्धता के कारण शंख की चूड़ियाँ, करछुल और पच्चीकारी के काम के प्रमुख केंद्र थे।",
                "icon": "fa-shuttle-space"
            },
            {
                "question": "मेसोपोटामिया के ग्रंथों में सिंधु क्षेत्र को किस नाम से पुकारा गया है और वहाँ के व्यापार का क्या विवरण है?",
                "answer": "मेसोपोटामिया के ग्रंथों में सिंधु क्षेत्र को <strong>मेलुहा (Meluhha)</strong> कहा गया है। इसे बहुमूल्य लकड़ी, अकीक, लाजवर्त, सोने और तांबे का देश बताया गया है, जिसके जहाज अक्कड़ के बंदरगाह पर आते थे।",
                "icon": "fa-ship"
            }
        ]
    },
    "deepDive": {
        "title": "पाठ्यक्रम मुख्य अध्ययन नोट्स (विस्तृत)",
        "description": "यूपीएससी परीक्षा (GS-1) के लिए हड़प्पा सभ्यता के कृषि आधारों, शिल्प उत्पादन, तौल प्रणालियों और अंतर्राष्ट्रीय व्यापार नेटवर्क को समझें।",
        "sections": [
            {
                "title": "1. कृषि और पशुपालन",
                "content": """<p>हड़प्पा शहरों की नगरीय संरचना ग्रामीण क्षेत्रों में उत्पन्न होने वाले कृषि अधिशेष पर टिकी थी, जो उन्नत कृषि विधियों और जल प्रबंधन प्रणालियों द्वारा संचालित होती थी।</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-seedling"></i> फसलें और कृषि तकनीक</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>मुख्य फसलें:</strong> गेहूँ, जौ, मटर, मसूर, सरसों, तिल और चना। लोथल और रंगपुर से धान की भूसी मिली है, जो स्थानीय धान की खेती दर्शाती है।</li>
      <li><strong>कपास:</strong> हड़प्पा के लोग दुनिया में सबसे पहले कपास (यूनानी: <em>सिंडन</em>) उगाने वाले थे, जिसका निर्यात पश्चिम को किया जाता था।</li>
      <li><strong>जुताई के साक्ष्य:</strong> <strong>कालीबंगन</strong> से ग्रिड पैटर्न में जुता हुआ खेत मिला है, जो दोहरी फसल (सरसों और चना/मटर) की जुताई दर्शाता है। मिट्टी के हल का मॉडल <strong>बनावली</strong> (हरियाणा) और जवईवाला (पाकिस्तान) से मिला है।</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-droplet"></i> सिंचाई, जल भंडारण और पशुपालन</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>सिंचाई:</strong> नहरों के स्पष्ट साक्ष्य अफगानिस्तान के <strong>शोर्तुघई</strong> में मिले हैं। मैदानी भागों में कृषि वर्षा बाढ़ और कुओं (जैसे मोहनजोदड़ो के सार्वजनिक कुएं) पर निर्भर थी। बलूचिस्तान में ढलान वाले पानी को रोकने के लिए <em>गबरबंद</em> (पत्थर के बांध) बनाए गए थे।</li>
      <li><strong>जलाशय:</strong> धोलावीरा में वर्षा जल को संचित करने के लिए विशाल पत्थर कटवाकर बनाए गए जलाशय मिले हैं, जो शुष्क क्षेत्रों में जल संरक्षण का उत्कृष्ट उदाहरण हैं।</li>
      <li><strong>पशुपालन:</strong> कूबड़ वाले बैल (जेबू), भेड़, बकरी, सूअर, भैंस, गधे और ऊंट पाले जाते थे। कूबड़ वाले बैल का धार्मिक और आर्थिक महत्व था।</li>
      <li><strong>घोड़े का विवाद:</strong> घोड़े की हड्डियाँ <strong>सुरकोटदा</strong> (गुजरात) से मिली हैं, लेकिन मुहरों और बर्तनों पर घोड़े का कोई अंकन नहीं है। यह पशु हड़प्पा की आर्थिक जीवन शैली का केंद्रीय हिस्सा नहीं था।</li>
    </ul>
  </div>
</div>""",
                "masteryZone": []
            },
            {
                "title": "2. शिल्प उत्पादन, धातु विज्ञान और भार प्रणाली",
                "content": """<p>विशिष्ट शिल्प केंद्र और राज्य-नियंत्रित तौल प्रणाली हड़प्पा शहरों की एकीकृत गुणवत्ता नियंत्रण प्रणाली और औद्योगिक क्षमता को दर्शाते हैं।</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-hammer"></i> विशिष्ट शिल्प केंद्र और धातु विज्ञान</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>मनके बनाना:</strong> मनके (Beads) बनाने के कारखाने <strong>चन्हुदड़ो</strong> और <strong>लोथल</strong> में सक्रिय थे। मनके बनाने के लिए अकीक (Carnelian) को गर्म कर लाल रंग दिया जाता था और बारीक छेद किए जाते थे।</li>
      <li><strong>शंख उद्योग:</strong> नागेश्वर और बालाकोट जैसे तौल तटीय स्थल विशेष रूप से शंख की चूड़ियाँ, करछुल और पच्चीकारी के काम के लिए प्रसिद्ध थे।</li>
      <li><strong>धातु विज्ञान:</strong> हड़प्पा वासियों ने तांबे में टिन मिलाकर कांसा बनाने की तकनीक सीख ली थी। <strong>तांबा</strong> राजस्थान की खेत्री खदानों और ओमान से प्राप्त होता था; <strong>टिन</strong> अफगानिस्तान और मध्य एशिया से आयात किया जाता था। <strong>लोहे का कोई ज्ञान नहीं था।</strong></li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-scale-balanced"></i> भार का मानकीकरण और माप</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>भार की सामग्री और आकार:</strong> बाट आमतौर पर <strong>चर्ट (Chert)</strong> नामक महीन पत्थर से बने घनाकार (Cubical) होते थे। वे बिना किसी निशान के बहुत सटीक रूप से बनाए जाते थे।</li>
      <li><strong>भार अनुपात:</strong> छोटी इकाइयों के लिए <strong>द्वि-आधारी प्रणाली (Binary: 1, 2, 4, 8, 16, 32, 64)</strong> थी, जबकि उच्च इकाइयों के लिए <strong>दशमलव प्रणाली (Decimal: 160, 200, 320, 640, 1600 आदि)</strong> थी। 16वीं इकाई (लगभग 13.63 ग्राम) सबसे मुख्य मानक थी।</li>
      <li><strong>मापक पैमाने:</strong> मोहनजोदड़ो से हाथीदांत का पैमाना, लोथल से शंख का पैमाना और हड़प्पा से कांसे का मापक पैमाना मिला है, जो लंबाई की माप में मानकीकरण को प्रमाणित करता है।</li>
    </ul>
  </div>
</div>""",
                "masteryZone": []
            },
            {
                "title": "3. व्यापार नेटवर्क, परिवहन और समुद्री संचार",
                "content": """<p>हड़प्पा की अर्थव्यवस्था व्यापक क्षेत्रीय स्थलीय मार्गों और अंतर्राष्ट्रीय समुद्री मार्गों पर निर्भर थी, जो सिंधु घाटी को पश्चिम एशिया के देशों से जोड़ते थे।</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-globe"></i> संसाधन प्राप्ति, बाहरी व्यापार और मेसोपोटामिया संबंध</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>व्यापारिक चौकियाँ:</strong> लाजवर्त (Lapis Lazuli) प्राप्त करने के लिए उत्तरी अफगानिस्तान के <strong>शोर्तुघई</strong> (बदख्शां) में एक व्यापारिक उपनिवेश स्थापित किया गया था।</li>
      <li><strong>मेसोपोटामिया के साक्ष्य:</strong> अक्कड़ के शासक सारगोन (लगभग 2350 ईसा पूर्व) के अभिलेखों में तीन देशों से व्यापारिक संबंधों का उल्लेख है: <strong>दिलमुन</strong> (बहरीन), <strong>माकन</strong> (ओमान/मकरान तट, जहाँ से तांबा मिलता था) और <strong>मेलुहा</strong> (सिंधु क्षेत्र)।</li>
      <li><strong>निर्यातित माल:</strong> हड़प्पा से लाल अकीक, लाजवर्त, तांबा, सोना, मोर और हाथीदांत की वस्तुओं का निर्यात होता था, जिसके बदले वे मेसोपोटामिया से ऊन, तेल और कपड़ा आयात करते थे।</li>
      <li><strong>मुद्रा का अभाव:</strong> व्यापार मुख्य रूप से <strong>वस्तु विनिमय प्रणाली (Barter System)</strong> पर आधारित था। सिक्के नहीं मिले हैं। मुहरों और गीली मिट्टी की छापों का उपयोग व्यापारिक पैकेजों को सुरक्षित करने के लिए किया जाता था।</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-ship"></i> परिवहन तकनीक और लोथल गोदीवाड़ा (Dockyard)</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>लोथल का गोदीवाड़ा:</strong> यह पकी ईंटों से बना 214 x 36 मीटर का एक विशाल आयताकार ढांचा था। यह साबरमती नदी की एक सहायक धारा से जुड़ा हुआ था। इसमें जहाजों के प्रवेश के लिए एक नहर, अतिरिक्त पानी निकालने का मार्ग (Spillway) और लकड़ी का लॉक-गेट सिस्टम था जो ज्वार-भाटे के समय पानी का स्तर बनाए रखता था।</li>
      <li><strong>स्थल परिवहन:</strong> लकड़ी की बैलगाड़ियाँ जिनके पहिये ठोस होते थे। इनके पुरातात्विक साक्ष्य मिट्टी की खिलौना बैलगाड़ियों और जमीन पर बने पहियों के निशानों से मिलते हैं।</li>
      <li><strong>जल परिवहन:</strong> नदियों के लिए चपटे तल वाली नावें और समुद्र के लिए पाल वाले बड़े जहाज, जिनके चित्र मुहरों और मिट्टी की पट्टिकाओं पर उकेरे गए हैं।</li>
    </ul>
  </div>
</div>""",
                "masteryZone": []
            }
        ]
    },
    "traps": {
        "title": "यूपीएससी परीक्षा के लिए चेतावनियाँ (गलतियों से बचें)",
        "items": [
            "<strong>गलती 1:</strong> राजस्थान के खेत्री खदानों से तांबा मिलता था न कि टिन। तांबे में मिलाने के लिए टिन को अफगानिस्तान और ईरान से आयात किया जाता था ताकि कांसा बनाया जा सके।",
            "<strong>गलती 2:</strong> नहरों द्वारा व्यापक सिंचाई के बयानों से सावधान रहें। सिंधु और घग्गर नदियों के मुख्य मैदानी भाग में नहरों के साक्ष्य नहीं मिले हैं। नहर का एकमात्र स्पष्ट साक्ष्य अफगानिस्तान के <strong>शोर्तुघई</strong> में मिला है।",
            "<strong>गलती 3:</strong> यह न मानें कि हड़प्पा की अर्थव्यवस्था मौद्रिक मुद्रा पर आधारित थी। यहाँ धात्विक सिक्कों का प्रचलन नहीं था; संपूर्ण व्यापार वस्तु विनिमय (Barter) द्वारा होता था जिसे मुहरों और मिट्टी की छापों से प्रामाणिक बनाया जाता था।",
            "<strong>गलती 4:</strong> घोड़े से संबंधित कथनों पर ध्यान दें। यद्यपि सुरकोटदा से घोड़े की हड्डियां मिली हैं, लेकिन मुहरों पर घोड़े का अंकन नहीं है और रथों में इनके प्रयोग के साक्ष्य नहीं हैं। भार वहन के लिए बैलगाड़ियों का प्रयोग होता था।",
            "<strong>गलती 5:</strong> व्यापार की वस्तुओं में लोहे को शामिल न करें। हड़प्पा वासियों को <strong>लोहे का कोई ज्ञान नहीं था</strong>; भारत में लोहे का प्रचलन उत्तर वैदिक काल (लगभग 1000 ईसा पूर्व) में शुरू हुआ था।"
        ]
    },
    "practiceQuestions": [],
    "mockTestQuestions": []
}

# Define the raw practice questions - 50 questions
practice_raw_eng = [
    # Q1
    (
        "Which of the following sites has yielded the most direct evidence of a ploughed field showing grid furrows indicating double-cropping during the Mature Harappan phase?",
        ["Banawali", "Kalibangan", "Lothal", "Surkotada"],
        1,
        "Kalibangan in Rajasthan has yielded a ploughed field with grid-patterned furrows, suggesting double-cropping (mustard and chickpea/horse gram) during the Harappan period. Banawali yielded terracotta models of ploughs."
    ),
    # Q2
    (
        "Terracotta models of ploughs have been discovered at which of the following Harappan sites?\n1. Banawali\n2. Kalibangan\n3. Bahawalpur (Jawaiwala)\nSelect the correct answer using the code given below:",
        ["1 only", "1 and 2 only", "1 and 3 only", "1, 2 and 3"],
        2,
        "Terracotta models of ploughs have been found at Banawali (Haryana) and at sites in Cholistan/Bahawalpur (like Jawaiwala). Kalibangan yielded the actual ploughed field, not the terracotta models of ploughs."
    ),
    # Q3
    (
        "With reference to Harappan agriculture, the term 'Sindon' referred to which of the following crops?",
        ["Wheat", "Barley", "Mustard", "Cotton"],
        3,
        "The Greeks called cotton 'Sindon', which is derived from 'Sindhu' (the Indus region), since the Harappans were the earliest people in the world to cultivate cotton."
    ),
    # Q4
    (
        "Consider the following statements regarding the irrigation system of the Indus Valley Civilisation:\n1. Direct traces of canals have been recovered from the site of Shortughai in northern Afghanistan.\n2. Alluvial plains of Punjab and Sindh show a dense network of brick-lined masonry canals.\nWhich of the statements given above is/are correct?",
        ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        0,
        "Statement 1 is correct: traces of canals have been found at Shortughai (Afghanistan). Statement 2 is incorrect: brick-lined canals are absent in the Indus plains of Punjab and Sindh. It is believed that siltation filled up any ancient canals there, or agriculture relied primarily on inundation and wells."
    ),
    # Q5
    (
        "Which of the following animals were domesticated by the Harappans?\n1. Humped Cattle (Zebu)\n2. Water Buffalo\n3. Ass and Camel\n4. Elephants\nSelect the correct answer using the code given below:",
        ["1 and 2 only", "1, 3 and 4 only", "2, 3 and 4 only", "1, 2, 3 and 4"],
        3,
        "All four animals were domesticated or known/exploited by the Harappans. Humped cattle (zebu), water buffalo, ass, camel, and elephant bone and artistic evidence are widely recorded in Mature Harappan levels."
    ),
    # Q6
    (
        "With reference to the horse in the Indus Valley Civilisation, consider the following statements:\n1. The horse was frequently depicted on Harappan seals and painted pottery.\n2. Skeletal remains of a horse have been identified at the site of Surkotada in Gujarat.\nWhich of the statements given above is/are correct?",
        ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        1,
        "Statement 1 is incorrect: the horse is never depicted on seals or painted pottery. Statement 2 is correct: Surkotada in Gujarat has yielded controversial horse bones, but the horse was not a central part of Harappan economic or cultural life."
    ),
    # Q7
    (
        "At which of the following Harappan sites were massive stone-cut water reservoirs discovered to manage seasonal dryland agriculture?",
        ["Dholavira", "Lothal", "Rakhigarhi", "Kalibangan"],
        0,
        "Dholavira in Gujarat features large stone-cut reservoirs designed to collect and store rain runoff, representing a sophisticated system of water management in a semi-arid zone."
    ),
    # Q8
    (
        "Which crop's husks have been found embedded in pottery clay at Lothal and Rangpur, showing localized cultivation?",
        ["Wheat", "Barley", "Rice", "Sesame"],
        2,
        "Lothal and Rangpur have yielded rice husks and fragments embedded in pottery, indicating localized rice cultivation in Gujarat, whereas wheat and barley were the primary staples in the northern regions."
    ),
    # Q9
    (
        "The stone dams known as 'Gabarbands' were constructed to check water flow for agriculture in which region of the Indus Valley Civilisation?",
        ["Baluchistan", "Sindh", "Punjab", "Gujarat"],
        0,
        "Gabarbands are stone-walled dams built across watercourses in Baluchistan to slow down surface runoff and deposit fertile silt on agricultural fields."
    ),
    # Q10
    (
        "Which of the following statements is correct regarding the procurement of copper by the Harappans?",
        ["Copper was imported exclusively from Mesopotamia.", "Copper was sourced locally from the Khetri mines of Rajasthan and also imported from Oman.", "Copper was sourced from Shortughai in Afghanistan.", "Copper was not alloyed with tin during the Mature Harappan phase."],
        1,
        "Harappans procured copper from the Khetri mines of Rajasthan and also imported it from Makan (Oman). Chemical analyses of Harappan and Omani copper show traces of nickel, confirming a common origin."
    ),
    # Q11
    (
        "With reference to Harappan bead-making industries, which of the following sites had specialized workshops?",
        ["Nageshwar and Balakot", "Chanhudaro and Lothal", "Kalibangan and Banawali", "Surkotada and Kot Diji"],
        1,
        "Chanhudaro and Lothal were major centers for bead-making, equipped with specialized bead drills, kilns for heating carnelian, and raw stone nodules."
    ),
    # Q12
    (
        "Nageshwar and Balakot were highly specialized Harappan centers for the production of which of the following crafts?",
        ["Bead making", "Shell-working", "Metal tools", "Terracotta toys"],
        1,
        "Both Nageshwar and Balakot are coastal sites that specialized in shell-working, including the manufacture of shell bangles, ladles, and inlay pieces, which were distributed inland."
    ),
    # Q13
    (
        "Consider the following statements regarding the metallurgy of the Harappan Civilisation:\n1. The Harappans mastered the technology of smelting iron to make heavy implements.\n2. Tin was alloyed with copper to manufacture bronze tools like axes and chisels.\nWhich of the statements given above is/are correct?",
        ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        1,
        "Statement 1 is incorrect: Iron was completely unknown to the Harappans. Statement 2 is correct: Tin was imported from Afghanistan and alloyed with copper to make bronze implements."
    ),
    # Q14
    (
        "From where did the Harappans import tin to alloy with copper for making bronze?",
        ["Khetri mines of Rajasthan", "Southern India", "Afghanistan and Central Asia (Iran)", "Oman"],
        2,
        "Tin was a rare metal in the subcontinent and was imported from Afghanistan and Central Asia/Iran to alloy with locally procured copper to manufacture bronze."
    ),
    # Q15
    (
        "Which material was used to make the standard, highly precise, cubical weights of the Indus Valley Civilisation?",
        ["Steatite", "Chert", "Faience", "Carnelian"],
        1,
        "Standard Harappan weights were made of chert, a fine-grained silica stone. They were cubical, unmarked, and polished to high standards of accuracy."
    ),
    # Q16
    (
        "With reference to the Harappan weight system, consider the following statements:\n1. The system followed a purely binary scale for all weight categories.\n2. For higher values, the weight system transitioned into a decimal scale.\nWhich of the statements given above is/are correct?",
        ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        1,
        "Statement 1 is incorrect: the binary scale (1, 2, 4, 8, 16, 32, 64) was used for lower weights, but it transitioned into decimal fractions (160, 200, 320, 640, 1600, etc.) for higher denominations. Statement 2 is correct."
    ),
    # Q17
    (
        "An ivory scale showing divisions of linear measurement was discovered at which of the following Harappan sites?",
        ["Lothal", "Mohenjo-daro", "Harappa", "Chanhudaro"],
        1,
        "An ivory scale was discovered at Mohenjo-daro. A shell scale was found at Lothal, and a bronze scale at Harappa, demonstrating a standardized system of linear measurement."
    ),
    # Q18
    (
        "With reference to the trade colony of Shortughai, consider the following statements:\n1. It was established in northern Afghanistan by the Harappans.\n2. Its primary function was to secure the supply of Lapis Lazuli.\nWhich of the statements given above is/are correct?",
        ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        2,
        "Both statements are correct. Shortughai was a Harappan trading outpost established in Badakhshan, northern Afghanistan, to exploit and control the procurement of precious Lapis Lazuli."
    ),
    # Q19
    (
        "In Mesopotamian cuneiform inscriptions dating to Sargon of Akkad, the term 'Meluhha' refers to which geographical region?",
        ["Oman Peninsula", "Bahrain Islands", "Indus Valley region", "Makran Coast"],
        2,
        "Mesopotamian cuneiform texts refer to the Indus Valley region as 'Meluhha', while Dilmun refers to Bahrain, and Makan refers to Oman/Makran coast."
    ),
    # Q20
    (
        "The cuneiform inscriptions refer to 'Dilmun' as a land of trade. Dilmun is identified with which modern region?",
        ["Oman", "Bahrain", "Iran", "Iraq"],
        1,
        "Dilmun is identified with the island of Bahrain in the Persian Gulf, which served as an important maritime transshipment point between Mesopotamia and India."
    ),
    # Q21
    (
        "Mesopotamian texts describe Makan (or Magan) as a major source of which of the following commodities imported by them?",
        ["Lapis Lazuli", "Copper", "Gold", "Ivory"],
        1,
        "Makan is identified with Oman/Makran coast, and was celebrated in Mesopotamian cuneiform records as a major source of copper."
    ),
    # Q22
    (
        "With reference to the Lothal dockyard, which of the following statements is/are correct?\n1. It was a massive basin of baked bricks connected to a tributary of the Sabarmati River.\n2. It featured a lock-gate mechanism to control water levels during tides.\nSelect the correct answer using the code given below:",
        ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        2,
        "Both statements are correct. Lothal's dockyard was a highly advanced tidal dock made of kiln-burnt bricks, featuring an inlet channel and a wooden lock-gate to regulate water levels for ships."
    ),
    # Q23
    (
        "What was the main medium of exchange in Harappan trade?",
        ["Silver coins called Shatamana", "Copper punch-marked coins", "Barter system based on exchange of goods", "Standardized gold bars"],
        2,
        "The Harappan economy did not have metallic coinage. Trade was carried out entirely through the barter system, facilitated by standardized weights and measures."
    ),
    # Q24
    (
        "Which of the following archaeological findings suggests that the Harappans engaged in long-distance maritime transport?\n1. Representations of masted ships on seals and amulets\n2. Terracotta models of boats at Lothal\n3. Traces of Indus-style seals in Mesopotamia\nSelect the correct answer using the code given below:",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All three findings support Harappan maritime activity. Representations of boats/ships on seals, terracotta boat models at Lothal, and Harappan seals found in Mesopotamian excavations confirm maritime trade links."
    ),
    # Q25
    (
        "Where did the Harappans procure Lapis Lazuli from?",
        ["Kolar mines of Karnataka", "Khetri mines of Rajasthan", "Badakhshan region of Afghanistan", "Persian Gulf region"],
        2,
        "Lapis Lazuli, a prized blue semi-precious stone, was procured from the Badakhshan region of Afghanistan, where the Harappans established a colony at Shortughai."
    ),
    # Q26
    (
        "With reference to Harappan pottery and its economic role, which of the following statements is correct?",
        ["Harappan pottery was exclusively hand-modeled and coarse.", "Red-and-black painted pottery was mass-produced on wheels for domestic and export storage.", "Pottery was painted using iron oxide base and white gypsum patterns.", "Pottery was not used for transport of commercial goods."],
        1,
        "Harappan pottery was mostly wheel-made and mass-produced. The red-and-black painted jars were used as storage jars for trade goods like wine or oil, and have been found in Oman (Makan)."
    ),
    # Q27
    (
        "Which of the following semi-precious stones was sourced from Gujarat (Bharuch/Lothal) for bead-making?",
        ["Lapis Lazuli", "Carnelian", "Jade", "Amethyst"],
        1,
        "Carnelian, a beautiful red-orange chalcedony stone, was sourced from Gujarat (Ratanpur near Bharuch) and processed into beads at Lothal and Chanhudaro."
    ),
    # Q28
    (
        "Which of the following statements is/are correct regarding the transport system of the Harappan Civilisation?\n1. Solid-wheeled wooden bullock carts were the primary means of inland transport.\n2. Clay wheel ruts matching modern track gauges have been excavated at several sites.\nSelect the correct answer using the code given below:",
        ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        2,
        "Both statements are correct. Terracotta toy cart models and fossilized clay wheel ruts matching modern gauges confirm that wooden bullock carts were standard land transport."
    ),
    # Q29
    (
        "Consider the following pairs of raw materials and their primary procurement areas in Harappan times:\n1. Gold : Karnataka (Kolar)\n2. Lapis Lazuli : Afghanistan (Shortughai)\n3. Steatite : Southern Rajasthan and Gujarat\n4. Carnelian : Gujarat (Lothal)\nWhich of the pairs given above are correctly matched?",
        ["1 and 2 only", "1, 2 and 4 only", "3 and 4 only", "1, 2, 3 and 4"],
        3,
        "All four pairs are correctly matched. Gold came from Southern India (Kolar); Lapis Lazuli from Badakhshan (Shortughai); Steatite from Rajasthan/Gujarat; Carnelian from Gujarat."
    ),
    # Q30
    (
        "In the Harappan weight system, the unit value of the key standard weight (corresponding to the 16th multiple) was approximately equal to:",
        ["5.5 grams", "13.63 grams", "28.4 grams", "64.0 grams"],
        1,
        "The unit standard weight (binary ratio 16) was equivalent to approximately 13.63 grams, which served as the baseline for everyday commercial exchanges."
    ),
    # Q31
    (
        "Consider the following statements regarding the role of seals and sealings in Harappan commerce:\n1. A sealing was created by pressing a seal onto wet clay placed over knots of trade bundles.\n2. If the cargo arrived with its clay sealing intact, it proved that the goods had not been tampered with.\nWhich of the statements given above is/are correct?",
        ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        2,
        "Both statements are correct. Seals were not currency, but security devices. The sealing (imprint on wet clay) secured trade packages and authenticated the sender."
    ),
    # Q32
    (
        "Which of the following sites has yielded a scale made of shell, used for linear measurements?",
        ["Mohenjo-daro", "Lothal", "Harappa", "Kalibangan"],
        1,
        "A scale made of shell was discovered at Lothal. An ivory scale was found at Mohenjo-daro, and a bronze scale at Harappa."
    ),
    # Q33
    (
        "Faience, a glassy glazed material manufactured from silica and gum, was primarily used for making what in the Harappan economy?",
        ["Large agricultural tools", "Weights and measures", "Luxurious small vessels and beads", "Structural bricks for houses"],
        2,
        "Faience was a high-status, difficult-to-make material. It was used to craft luxury items like small perfume bottles, beads, and amulets, representing elite consumption."
    ),
    # Q34
    (
        "Which of the following states was the primary source of Steatite (soapstone) used to manufacture thousands of Harappan seals?",
        ["Rajasthan", "Karnataka", "Bihar", "Tamil Nadu"],
        0,
        "Steatite was sourced primarily from Rajasthan and northern Gujarat, which are rich in soft soapstone deposits."
    ),
    # Q35
    (
        "Consider the following statements regarding Harappan agricultural tools:\n1. Wooden ploughs were likely used, which decayed over time in the alluvial soil.\n2. Sickles made of iron were used for harvesting wheat and barley crops.\nWhich of the statements given above is/are correct?",
        ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        0,
        "Statement 1 is correct: Harappans used wooden ploughs (as indicated by terracotta models). Statement 2 is incorrect: Iron sickles did not exist, as iron was unknown. They used stone blades mounted on wooden handles for harvesting."
    ),
    # Q36
    (
        "With reference to the Indus Valley Civilisation, which of the following sites shows evidence of maritime contacts with the Persian Gulf through the discovery of a circular button seal?",
        ["Lothal", "Chanhudaro", "Rakhigarhi", "Banawali"],
        0,
        "Lothal has yielded a circular 'Persian Gulf' button seal, confirming direct maritime trade contacts between Gujarat, Bahrain, and the Persian Gulf."
    ),
    # Q37
    (
        "Mesopotamian cuneiform records refer to Meluhha as a land of 'exotic birds'. Which bird is commonly identified with this description?",
        ["Sparrow", "Peacock", "Falcon", "Pigeon"],
        1,
        "The texts mention the 'Haja-bird' of Meluhha, which historians identify as the peacock, known for its beautiful plumage and calls."
    ),
    # Q38
    (
        "Which of the following statements about the craft of seal-making in the Harappan economy is correct?",
        ["Seals were cast in bronze molds.", "Seals were hand-carved in intaglio on soft steatite and then kiln-fired.", "Agate seals were the most common type.", "Seals were exclusively manufactured at Harappa."],
        1,
        "Seals were carved in reverse (intaglio) on soft steatite blocks. After carving, they were heated in kilns to dehydrate the talc, turning it into hard white enstatite."
    ),
    # Q39
    (
        "With reference to Harappan textile industries, what was the primary source of dye used for coloring fabrics?",
        ["Chemical aniline dyes", "Madder (vegetable dye) yielding red color", "Saffron", "Indigo only"],
        1,
        "Traces of red dye on cotton fragments suggest the use of madder, a vegetable root dye, demonstrating an advanced knowledge of dyeing textiles."
    ),
    # Q40
    (
        "Which of the following factors contributed to the centralization and standardization of the Mature Harappan economy?\n1. Uniform weights and measures based on chert standards\n2. Standardized brick sizes in the ratio 1:2:4\n3. Centralized procurement colonies like Shortughai\nSelect the correct answer using the code given below:",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All three factors contributed to economic integration and centralization across the vast Harappan territory."
    ),
    # Q41
    (
        "Which of the following is correct about the animal bones found at Harappan sites?",
        ["Wild animal bones like deer and boar are completely absent.", "Bones of cattle, sheep, and goat indicate they were used for meat and draft labor.", "No fish or fowl bones have been recovered.", "Bones of domestic animals show they were only used for religious sacrifices."],
        1,
        "Bones of cattle, sheep, goats, and buffaloes are common at Harappan sites, indicating their central role in the agricultural and pastoral economy for meat, milk, and draft work."
    ),
    # Q42
    (
        "Jade, a green semi-precious stone used in Harappan jewelry, was imported from which region?",
        ["Central Asia / Pamirs", "Oman", "Karnataka", "Bihar"],
        0,
        "Jade was imported from Central Asia or the Pamir region, reflecting the long-distance overland trade connections of the Harappans."
    ),
    # Q43
    (
        "Silver ornaments were manufactured by the Harappans. Where did they source silver from?",
        ["Kolar mines", "Afghanistan and Iran", "Rajasthan Khetri mines", "Oman"],
        1,
        "Silver was imported from Afghanistan and Iran, as it was not widely available locally in the Indus Valley plains."
    ),
    # Q44
    (
        "Which coastal Harappan site in Sindh served as an export base near the Indus mouth, specializing in shell objects?",
        ["Balakot", "Sutkagendor", "Allahdino", "Surkotada"],
        0,
        "Balakot was a coastal settlement specializing in shell-craft production and located near the mouth of the Windar River, serving as a maritime hub."
    ),
    # Q45
    (
        "The Westernmost outpost of the Indus Valley Civilisation, which served as a fortified trade post on the Makran coast near Iran, is:",
        ["Sutkagendor", "Balakot", "Dholavira", "Sotka Koh"],
        0,
        "Sutkagendor on the Makran coast was the westernmost Harappan site, functioning as a fortified trading post to monitor maritime traffic entering the Persian Gulf."
    ),
    # Q46
    (
        "With reference to the decline of the Harappan trade economy in the Late Harappan phase, which of the following occurred?",
        ["Mesopotamian trade increased significantly.", "Weights and measures became even more strictly standardized.", "Long-distance trade networks collapsed, and weights became localized and non-uniform.", "Iron coinage was introduced to replace barter."],
        2,
        "During the Late Harappan phase (after 1900 BCE), long-distance trade with Mesopotamia collapsed, standard chert weights disappeared, and regionalized barter systems returned."
    ),
    # Q47
    (
        "What was the main purpose of the spillway in the Lothal dockyard?",
        ["To import drinking water to the town", "To allow excess water to escape and prevent flooding of the dock walls", "To act as a passage for small fishing boats", "To clean the silt from the dock basin manually"],
        1,
        "The spillway was a channel equipped with a sliding gate that allowed excess water to escape during high tides or floods, maintaining a constant water level in the dock."
    ),
    # Q48
    (
        "Which of the following raw materials was sourced from the Nilgiri hills of Southern India?",
        ["Amethyst", "Gold", "Copper", "Lapis Lazuli"],
        1,
        "Gold was sourced from Southern India, particularly the Kolar/Nilgiri regions, which were rich in alluvial and vein gold."
    ),
    # Q49
    (
        "Which site is known as a manufacturing hub for microscopic steatite beads, a highly specialized craft of the Harappans?",
        ["Chanhudaro", "Harappa", "Kalibangan", "Rakhigarhi"],
        0,
        "Chanhudaro was a premier craft production center, famous for producing tiny, microscopic beads of steatite that required high technical precision."
    ),
    # Q50
    (
        "Which of the following statements is correct regarding the double-cropping grid pattern of Kalibangan?",
        ["The furrows ran parallel to each other in only one direction.", "The furrows were cut at right angles to each other, with one set spaced closer and the other set wider.", "The pattern shows that rice and wheat were grown simultaneously.", "The grid pattern was constructed for drainage, not farming."],
        1,
        "At Kalibangan, the furrows were arranged in a grid, cutting each other at right angles. The wider-spaced furrows were for taller crops (like mustard), and the narrower ones for smaller crops (like chickpea)."
    )
]

practice_raw_hin = [
    # Q1
    (
        "निम्नलिखित में से किस स्थल से परिपक्व हड़प्पा काल के दौरान ग्रिड हल-रेखाओं (furrows) को दर्शाने वाले जुते हुए खेत के सबसे प्रत्यक्ष साक्ष्य मिले हैं, जो दोहरी फसल का संकेत देते हैं?",
        ["बनावली", "कालीबंगन", "लोथल", "सुरकोटदा"],
        1,
        "राजस्थान के कालीबंगन से ग्रिड पैटर्न में जुते हुए खेत के साक्ष्य मिले हैं, जो हड़प्पा काल में दोहरी फसल (सरसों और चना/मटर) की ओर इशारा करते हैं। बनावली से मिट्टी के हल का मॉडल मिला है।"
    ),
    # Q2
    (
        "हड़प्पा सभ्यता के किस स्थल से मिट्टी के हल (Terracotta plough) के मॉडल प्राप्त हुए हैं?\n1. बनावली\n2. कालीबंगन\n3. बहावलपुर (जवईवाला)\nनीचे दिए गए कूट का प्रयोग कर सही उत्तर चुनिए:",
        ["केवल 1", "केवल 1 और 2", "केवल 1 और 3", "1, 2 और 3"],
        2,
        "मिट्टी के हल के मॉडल हरियाणा के बनावली और चोलिस्तान/बहावलपुर क्षेत्र (जैसे जवईवाला) से मिले हैं। कालीबंगन से जुता हुआ खेत मिला है, न कि हल का मिट्टी का मॉडल।"
    ),
    # Q3
    (
        "हड़प्पा कृषि के संदर्भ में, 'सिंडन' (Sindon) शब्द निम्नलिखित में से किस फसल को संदर्भित करता था?",
        ["गेहूँ", "जौ", "सरसों", "कपास"],
        3,
        "यूनानी लोग कपास को 'सिंडन' कहते थे, जो 'सिंधु' (सिंधु क्षेत्र) शब्द से बना है, क्योंकि हड़प्पा के लोग दुनिया में सबसे पहले कपास उगाने वाले थे।"
    ),
    # Q4
    (
        "सिंधु घाटी सभ्यता की सिंचाई प्रणाली के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. उत्तरी अफगानिस्तान में शोर्तुघई नामक स्थल से नहरों के सीधे अवशेष प्राप्त हुए हैं।\n2. पंजाब और सिंध के जलोढ़ मैदानों में ईंटों से बनी पक्की नहरों का सघन जाल मिला है।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
        ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        0,
        "कथन 1 सही है: शोर्तुघई (अफगानिस्तान) में नहरों के साक्ष्य मिले हैं। कथन 2 गलत है: पंजाब और सिंध के मैदानी इलाकों में ईंटों से बनी नहरें अनुपस्थित हैं। ऐसा माना जाता है कि सिल्ट जमा होने से प्राचीन नहरें भर गईं, या कृषि मुख्यतः बाढ़ के पानी और कुओं पर निर्भर थी।"
    ),
    # Q5
    (
        "हड़प्पा वासियों द्वारा निम्नलिखित में से किन पशुओं को पाला जाता था?\n1. कूबड़ वाला बैल (जेबू)\n2. भैंस\n3. गधा और ऊंट\n4. हाथी\nनीचे दिए गए कूट का प्रयोग कर सही उत्तर चुनिए:",
        ["केवल 1 और 2", "केवल 1, 3 और 4", "केवल 2, 3 और 4", "1, 2, 3 और 4"],
        3,
        "इन चारों पशुओं को हड़प्पा वासियों द्वारा पाला जाता था या उनका उपयोग किया जाता था। परिपक्व हड़प्पा स्तरों में कूबड़ वाले बैल, भैंस, गधे, ऊंट और हाथी की हड्डियों व कलाकृतियों के साक्ष्य व्यापक रूप से दर्ज हैं।"
    ),
    # Q6
    (
        "सिंधु घाटी सभ्यता में घोड़े के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:\n1. हड़प्पा की मुहरों और चित्रित बर्तनों पर घोड़े का अक्सर अंकन किया जाता था।\n2. गुजरात के सुरकोटदा नामक स्थल से घोड़े के कंकाल के अवशेषों की पहचान की गई है।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
        ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        1,
        "कथन 1 गलत है: मुहरों या मिट्टी के बर्तनों पर घोड़े का चित्रण कभी नहीं मिलता। कथन 2 सही है: गुजरात के सुरकोटदा से विवादास्पद घोड़े की हड्डियाँ मिली हैं, लेकिन घोड़ा हड़प्पा के आर्थिक या सांस्कृतिक जीवन का केंद्रीय हिस्सा नहीं था।"
    ),
    # Q7
    (
        "मौसमी शुष्क कृषि के प्रबंधन के लिए किस हड़प्पा स्थल पर पत्थर को काटकर बनाए गए विशाल जलाशयों की खोज की गई थी?",
        ["धोलावीरा", "लोथल", "राखीगढ़ी", "कालीबंगन"],
        0,
        "गुजरात के धोलावीरा में वर्षा जल को संचित करने के लिए विशाल जलाशय मिले हैं, जो अर्ध-शुष्क क्षेत्रों में जल प्रबंधन की एक उन्नत प्रणाली का प्रतिनिधित्व करते हैं।"
    ),
    # Q8
    (
        "लोथल और रंगपुर में बर्तनों की मिट्टी में धँसे हुए किस फसल के छिलके (husks) मिले हैं, जो स्थानीय कृषि को दर्शाते हैं?",
        ["गेहूँ", "जौ", "धान (चावल)", "तिल"],
        2,
        "लोथल और रंगपुर से मिट्टी के बर्तनों में धान की भूसी के अवशेष मिले हैं, जो गुजरात में चावल की खेती को दर्शाते हैं, जबकि उत्तरी क्षेत्रों में गेहूँ और जौ मुख्य फसलें थीं।"
    ),
    # Q9
    (
        "सिंधु घाटी सभ्यता के किस क्षेत्र में कृषि के लिए पानी के बहाव को रोकने के लिए 'गबरबंद' नामक पत्थरों के बांध बनाए गए थे?",
        ["बलूचिस्तान", "सिंध", "पंजाब", "गुजरात"],
        0,
        "गबरबंद बलूचिस्तान में जलमार्गों के पार बनाई गई पत्थर की दीवारें थीं जो वर्षा के पानी के बहाव को धीमा करती थीं और खेतों पर उपजाऊ गाद जमा करती थीं।"
    ),
    # Q10
    (
        "हड़प्पा वासियों द्वारा तांबे की प्राप्ति के संबंध में निम्नलिखित में से कौन सा कथन सही है?",
        ["तांबा विशेष रूप से मेसोपोटामिया से आयात किया जाता था।", "तांबा राजस्थान की खेत्री खदानों से स्थानीय स्तर पर प्राप्त किया जाता था और ओमान से भी आयात किया जाता था।", "तांबा अफगानिस्तान के शोर्तुघई से प्राप्त किया जाता था।", "परिपक्व हड़प्पा काल में तांबे को टिन के साथ मिश्रित नहीं किया जाता था।"],
        1,
        "हड़प्पा वासी राजस्थान के खेत्री क्षेत्र से तांबा प्राप्त करते थे और ओमान से भी आयात करते थे। हड़प्पा और ओमानी तांबे के रासायनिक विश्लेषण में निकल के अंश मिले हैं, जिससे दोनों का स्रोत समान होने की पुष्टि होती।"
    ),
    # Q11
    (
        "हड़प्पा के मनके (beads) बनाने के उद्योगों के संदर्भ में, निम्नलिखित में से किन स्थलों पर विशिष्ट कारखाने थे?",
        ["नागेश्वर और बालाकोट", "चन्हुदड़ो और लोथल", "कालीबंगन और बनावली", "सुरकोटदा और कोटदीजी"],
        1,
        "चन्हुदड़ो और लोथल मनके बनाने के प्रमुख केंद्र थे, जहाँ से मनकों में छेद करने वाले विशिष्ट बर्मा (Drills), भट्टियाँ और कच्चे पत्थर के टुकड़े मिले हैं।"
    ),
    # Q12
    (
        "नागेश्वर और बालाकोट निम्नलिखित में से किस शिल्प के उत्पादन के लिए विशिष्ट हड़प्पा केंद्र थे?",
        ["मनके बनाना", "शंख उद्योग (Shell-working)", "धातु के उपकरण", "मिट्टी के खिलौने"],
        1,
        "नागेश्वर और बालाकोट दोनों तटीय स्थल थे जो शंख के काम में माहिर थे। यहाँ से शंख की चूड़ियाँ, करछुल और पच्चीकारी की वस्तुएँ बनाई जाती थीं और उन्हें आंतरिक भागों में भेजा जाता था।"
    ),
    # Q13
    (
        "सिंधु घाटी सभ्यता के धातु विज्ञान के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. हड़प्पा वासियों ने भारी उपकरण बनाने के लिए लोहे को गलाने की तकनीक में महारत हासिल कर ली थी।\n2. कुल्हाड़ी और छेनी जैसे कांसे के उपकरण बनाने के लिए तांबे में टिन मिलाया जाता था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
        ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        1,
        "कथन 1 गलत है: हड़प्पा वासियों को लोहे का कोई ज्ञान नहीं था। कथन 2 सही है: तांबे में टिन मिलाकर कांसा तैयार किया जाता था और टिन को अफगानिस्तान से आयात किया जाता था।"
    ),
    # Q14
    (
        "कांसा बनाने के लिए तांबे के साथ मिलाने हेतु हड़प्पा वासी टिन का आयात कहाँ से करते थे?",
        ["राजस्थान की खेत्री खदानें", "दक्षिण भारत", "अफगानिस्तान और मध्य एशिया (ईरान)", "ओमान"],
        2,
        "टिन उपमहाद्वीप में एक दुर्लभ धातु थी और कांसे के औजार बनाने के लिए इसे अफगानिस्तान और मध्य एशिया/ईरान से आयात किया जाता था।"
    ),
    # Q15
    (
        "सिंधु घाटी सभ्यता के मानक, अत्यधिक सटीक, घनाकार (cubical) बाट बनाने के लिए किस सामग्री का उपयोग किया जाता था?",
        ["सेलखड़ी (Steatite)", "चर्ट (Chert)", "फेयॉन्स (Faience)", "लाल अकीक (Carnelian)"],
        1,
        "मानक हड़प्पा बाट चर्ट नामक महीन पत्थर से बने होते थे। वे बिना किसी निशान के घनाकार और बहुत सटीक रूप से पॉलिश किए जाते थे।"
    ),
    # Q16
    (
        "हड़प्पा की तौल प्रणाली के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:\n1. यह प्रणाली सभी श्रेणियों के बाटों के लिए विशुद्ध रूप से द्वि-आधारी (binary) पैमाने का पालन करती थी।\n2. उच्च मूल्यों के लिए, भार प्रणाली दशमलव पैमाने में परिवर्तित हो जाती थी।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
        ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        1,
        "कथन 1 गलत है: द्वि-आधारी पैमाना (1, 2, 4, 8, 16, 32, 64) छोटे बाटों के लिए था, लेकिन बड़े मूल्य के बाटों के लिए दशमलव प्रणाली (160, 200, 320, 640, 1600 आदि) का उपयोग होता था। कथन 2 सही है।"
    ),
    # Q17
    (
        "रैखिक माप (linear measurement) को दर्शाने वाला हाथीदांत का पैमाना (Ivory scale) किस हड़प्पा स्थल से खोजा गया था?",
        ["लोथल", "मोहनजोदड़ो", "हड़प्पा", "चन्हुदड़ो"],
        1,
        "मोहनजोदड़ो से हाथीदांत का पैमाना मिला था। लोथल से शंख का पैमाना और हड़प्पा से कांसे का पैमाना मिला था, जो मानकीकृत माप प्रणाली को दर्शाता है।"
    ),
    # Q18
    (
        "शोर्तुघई (Shortughai) व्यापारिक उपनिवेश के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:\n1. इसे हड़प्पा वासियों द्वारा उत्तरी अफगानिस्तान में स्थापित किया गया था।\n2. इसका मुख्य कार्य लाजवर्त (Lapis Lazuli) की आपूर्ति सुरक्षित करना था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
        ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        2,
        "दोनों कथन सही हैं। शोर्तुघई उत्तरी अफगानिस्तान के बदख्शां क्षेत्र में एक हड़प्पा व्यापारिक चौकी थी, जिसका उपयोग कीमती लाजवर्त पत्थर की प्राप्ति को नियंत्रित करने के लिए किया जाता था।"
    ),
    # Q19
    (
        "मेसोपोटामिया के सारगोन के काल के कीलाक्षर (Cuneiform) अभिलेखों में, 'मेलुहा' (Meluhha) शब्द किस भौगोलिक क्षेत्र को संदर्भित करता है?",
        ["ओमान प्रायद्वीप", "बहरीन द्वीप", "सिंधु घाटी क्षेत्र", "मकरान तट"],
        2,
        "मेसोपोटामिया के अभिलेखों में सिंधु घाटी क्षेत्र को 'मेलुहा' कहा गया है, जबकि दिलमुन बहरीन को और माकन ओमान/मकरान तट को संदर्भित करता है।"
    ),
    # Q20
    (
        "कीलाक्षर अभिलेखों में 'दिलमुन' (Dilmun) को एक व्यापारिक देश कहा गया है। दिलमुन की पहचान किस आधुनिक क्षेत्र से की जाती है?",
        ["ओमान", "बहरीन", "ईरान", "इराक"],
        1,
        "दिलमुन की पहचान फारस की खाड़ी में स्थित बहरीन द्वीप से की जाती है, जो मेसोपोटामिया और भारत के बीच एक प्रमुख समुद्री मध्यवर्ती व्यापारिक केंद्र था।"
    ),
    # Q21
    (
        "मेसोपोटामिया के ग्रंथों में 'माकन' (Makan या Magan) को किस आयातित वस्तु के प्रमुख स्रोत के रूप में वर्णित किया गया है?",
        ["लाजवर्त", "तांबा", "सोना", "हाथीदांत"],
        1,
        "माकन (ओमान/मकरान तट) को मेसोपोटामिया के ग्रंथों में तांबे के प्रमुख स्रोत के रूप में उल्लिखित किया गया है।"
    ),
    # Q22
    (
        "लोथल के गोदीवाड़ा (Dockyard) के संदर्भ में, निम्नलिखित में से कौन सा/से कथन सही है/हैं?\n1. यह पकी ईंटों से बना एक विशाल ढांचा था जो साबरमती नदी की एक सहायक नदी से जुड़ा था।\n2. इसमें ज्वार के दौरान पानी के स्तर को नियंत्रित करने के लिए एक लॉक-गेट तंत्र था।\nनीचे दिए गए कूट का प्रयोग कर सही उत्तर चुनिए:",
        ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        2,
        "दोनों कथन सही हैं। लोथल का गोदीवाड़ा पकी ईंटों से बना एक अत्यंत उन्नत ढांचा था, जिसमें प्रवेश द्वार और ज्वार-भाटे के समय पानी को नियंत्रित करने के लिए लकड़ी का लॉक-गेट लगा हुआ था।"
    ),
    # Q23
    (
        "हड़प्पा व्यापार में विनिमय का मुख्य साधन क्या था?",
        ["शतमान नामक चांदी के सिक्के", "तांबे के आहत (punch-marked) सिक्के", "वस्तुओं के आदान-प्रदान पर आधारित वस्तु विनिमय (Barter) प्रणाली", "मानकीकृत सोने की छड़ें"],
        2,
        "हड़प्पा अर्थव्यवस्था में धातु के सिक्कों का प्रचलन नहीं था। व्यापार पूरी तरह से वस्तु विनिमय प्रणाली द्वारा संचालित होता था, जिसे मानकीकृत तौल और माप द्वारा आसान बनाया गया था।"
    ),
    # Q24
    (
        "निम्नलिखित में से कौन से पुरातात्विक साक्ष्य दर्शाते हैं कि हड़प्पा वासी लंबी दूरी के समुद्री परिवहन में शामिल थे?\n1. मुहरों और ताबीज पर पाल वाले जहाजों का अंकन\n2. लोथल से मिट्टी की नावों के मॉडल\n3. मेसोपोटामिया में हड़प्पा शैली की मुहरों के मिलना\nनीचे दिए गए कूट का प्रयोग कर सही उत्तर चुनिए:",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 and 3", "1, 2 और 3"],
        3,
        "तीनों साक्ष्य समुद्री गतिविधियों की पुष्टि करते हैं। मुहरों पर जहाजों के चित्र, लोथल से मिट्टी की नावों के मॉडल और मेसोपोटामिया में मिली हड़प्पा मुहरें लंबी दूरी के समुद्री व्यापार को साबित करती हैं।"
    ),
    # Q25
    (
        "हड़प्पा वासी लाजवर्त (Lapis Lazuli) कहाँ से प्राप्त करते थे?",
        ["कर्नाटक की कोलार खदानें", "राजस्थान की खेत्री खदानें", "अफगानिस्तान का बदख्शां क्षेत्र", "फारस की खाड़ी क्षेत्र"],
        2,
        "लाजवर्त, जो एक मूल्यवान नीला पत्थर था, अफगानिस्तान के बदख्शां क्षेत्र से मँगाया जाता था, जहाँ हड़प्पा वासियों ने शोर्तुघई नामक एक बस्ती स्थापित की थी।"
    ),
    # Q26
    (
        "हड़प्पा के मृदभांडों (pottery) और उनकी आर्थिक भूमिका के संदर्भ में निम्नलिखित में से कौन सा कथन सही है?",
        ["हड़प्पा के बर्तन केवल हाथ से बने और खुरदरे होते थे।", "घरेलू उपयोग और व्यापारिक सामान रखने के लिए पहिये पर बने लाल-काले बर्तनों का बड़े पैमाने पर निर्माण होता था।", "बर्तनों पर लोहे के ऑक्साइड के आधार पर सफेद जिप्सम से चित्रकारी की जाती थी।", "व्यापारिक वस्तुओं के परिवहन के लिए बर्तनों का उपयोग नहीं होता था।"],
        1,
        "हड़प्पा के अधिकांश बर्तन चाक (wheel) पर बनाए जाते थे। गुजरात के लोथल से मिले लाल-काले बड़े जार का उपयोग तेल या शराब जैसी व्यापारिक वस्तुओं के परिवहन के लिए किया जाता था, और ऐसे जार ओमान (माकन) में भी मिले हैं।"
    ),
    # Q27
    (
        "निम्नलिखित में से कौन सा अर्ध-मूल्यवान पत्थर मनके बनाने के लिए गुजरात (भरूच/लोथल) से प्राप्त किया जाता था?",
        ["लाजवर्त (Lapis Lazuli)", "लाल अकीक (Carnelian)", "जड़े (Jade)", "एमेथिस्ट (Amethyst)"],
        1,
        "लाल अकीक (Carnelian) गुजरात के भरूच के पास रतनपुर से प्राप्त किया जाता था और लोथल व चन्हुदड़ो में इसके मनके बनाए जाते थे।"
    ),
    # Q28
    (
        "हड़प्पा सभ्यता की परिवहन प्रणाली के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. लकड़ी की बैलगाड़ियाँ अंतर्देशीय परिवहन का प्राथमिक साधन थीं।\n2. कई स्थलों से आधुनिक रेल की पटरियों की चौड़ाई से मेल खाते हुए मिट्टी के पहियों के निशान मिले हैं।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
        ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        2,
        "दोनों कथन सही हैं। मिट्टी की खिलौना गाड़ियों के मॉडल और पहियों के जीवाश्म निशान यह साबित करते हैं कि ठोस पहियों वाली लकड़ी की बैलगाड़ियाँ मुख्य अंतर्देशीय परिवहन थीं।"
    ),
    # Q29
    (
        "कच्चे माल और उनके मुख्य प्राप्ति क्षेत्रों के निम्नलिखित युग्मों पर विचार कीजिए:\n1. सोना : कर्नाटक (कोलार)\n2. लाजवर्त : अफगानिस्तान (शोर्तुघई)\n3. सेलखड़ी (Steatite) : दक्षिणी राजस्थान और गुजरात\n4. लाल अकीक (Carnelian) : गुजरात (लोथल)\nउपर्युक्त युग्मों में से कौन-से सही सुमेलित हैं?",
        ["केवल 1 और 2", "केवल 1, 2 और 4", "केवल 3 और 4", "1, 2, 3 और 4"],
        3,
        "सभी चारों युग्म सही सुमेलित हैं। सोना दक्षिण भारत (कोलार) से; लाजवर्त उत्तरी अफगानिस्तान (शोर्तुघई) से; सेलखड़ी राजस्थान व गुजरात से; और लाल अकीक गुजरात के तटीय स्थलों से प्राप्त होता था।"
    ),
    # Q30
    (
        "हड़प्पा की भार प्रणाली में, मुख्य मानक बाट का मूल्य (जो 16वीं इकाई के गुणज के बराबर था) लगभग किसके बराबर था?",
        ["5.5 ग्राम", "13.63 ग्राम", "28.4 ग्राम", "64.0 ग्राम"],
        1,
        "मुख्य मानक बाट (द्वि-आधारी अनुपात 16) लगभग 13.63 ग्राम के बराबर था, जो रोज़मर्रा के व्यावसायिक लेन-देन का मुख्य आधार था।"
    ),
    # Q31
    (
        "हड़प्पा के वाणिज्य में मुहरों और मिट्टी की छापों (sealings) की भूमिका के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. व्यापारिक सामान के पैकेजों के गांठों पर गीली मिट्टी लगाकर उस पर मुहर दबाकर छाप बनाई जाती थी।\n2. यदि सामान बिना टूटी छाप के गंतव्य पर पहुँचता था, तो यह साबित होता था कि सामान से छेड़छाड़ नहीं की गई है।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
        ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        2,
        "दोनों कथन सही हैं। मुहरें सिक्के नहीं बल्कि सुरक्षा उपकरण थीं। गीली मिट्टी पर मुहर की छाप पैकेजों को सुरक्षित करती थी और प्रेषक की पहचान को प्रमाणित करती थी।"
    ),
    # Q32
    (
        "निम्नलिखित में से किस स्थल से शंख (Shell) से बना एक मापक पैमाना मिला है, जिसका उपयोग रैखिक माप के लिए किया जाता था?",
        ["मोहनजोदड़ो", "लोथल", "हड़प्पा", "कालीबंगन"],
        1,
        "लोथल से शंख का बना मापक पैमाना मिला था। मोहनजोदड़ो से हाथीदांत का और हड़प्पा से कांसे का पैमाना मिला था।"
    ),
    # Q33
    (
        "हड़प्पा अर्थव्यवस्था में सिलिका और गोंद से निर्मित चमकीले पदार्थ फेयॉन्स (Faience) का मुख्य उपयोग क्या बनाने के लिए किया जाता था?",
        ["भारी कृषि औजार", "तौलने के बाट", "विलासिता के छोटे पात्र और मनके", "घरों की ईंटें"],
        2,
        "फेयॉन्स एक मूल्यवान और कठिन तकनीक से निर्मित सामग्री थी। इसका उपयोग केवल विलासिता की छोटी चीजें जैसे इत्र की बोतलें, मनके और ताबीज बनाने के लिए किया जाता था।"
    ),
    # Q34
    (
        "हजारों हड़प्पा मुहरों के निर्माण में प्रयुक्त होने वाले मुलायम पत्थर सेलखड़ी (Steatite) का मुख्य स्रोत कौन सा राज्य था?",
        ["राजस्थान", "कर्नाटक", "बिहार", "तमिलनाडु"],
        0,
        "सेलखड़ी मुख्य रूप से राजस्थान और उत्तरी गुजरात से मंगाई जाती थी, जहाँ इस मुलायम पत्थर के प्रचुर भंडार हैं।"
    ),
    # Q35
    (
        "हड़प्पा के कृषि उपकरणों के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. लकड़ी के हलों का उपयोग किया जाता था, जो जलोढ़ मिट्टी में समय के साथ नष्ट हो गए।\n2. गेहूँ और जौ की कटाई के लिए लोहे के हंसियों (Sickles) का उपयोग किया जाता था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
        ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        0,
        "कथन 1 सही है: हड़प्पा वासी लकड़ी के हलों का उपयोग करते थे (मिट्टी के मॉडल इसके प्रमाण हैं)। कथन 2 गलत है: लोहे के औजार नहीं थे क्योंकि लोहे का ज्ञान नहीं था। फसल काटने के लिए लकड़ी के हैंडल में फिट किए गए पत्थर के फलकों का उपयोग किया जाता था।"
    ),
    # Q36
    (
        "सिंधु घाटी सभ्यता के संदर्भ में, निम्नलिखित में से कौन सा स्थल फारस की खाड़ी के साथ व्यापारिक संपर्कों की पुष्टि एक गोल बटन मुहर के माध्यम से करता है?",
        ["लोथल", "चन्हुदड़ो", "राखीगढ़ी", "बनावली"],
        0,
        "लोथल से फारस की खाड़ी शैली की एक गोल बटन मुहर मिली है, जो गुजरात, बहरीन और फारस की खाड़ी के बीच सीधे समुद्री व्यापारिक संपर्कों को दर्शाती है।"
    ),
    # Q37
    (
        "मेसोपोटामिया के अभिलेखों में मेलुहा को 'हाजा-पक्षी' (Haja-bird) का देश कहा गया है। यह पक्षी कौन सा माना जाता है?",
        ["गौरैया", "मोर", "बाज", "कबूतर"],
        1,
        "ग्रंथों में उल्लिखित 'हाजा-पक्षी' की पहचान अधिकांश इतिहासकारों द्वारा मोर से की गई है, जो अपनी सुंदर आवाज और पंखों के लिए जाना जाता था।"
    ),
    # Q38
    (
        "हड़प्पा अर्थव्यवस्था में मुहर बनाने की कला के संबंध में निम्नलिखित में से कौन सा कथन सही है?",
        ["मुहरों को कांसे के सांचों में ढाला जाता था।", "मुहरों को मुलायम सेलखड़ी पर उकेरकर (Intaglio) बनाया जाता था और फिर भट्टी में पकाया जाता था।", "अकीक (Agate) की मुहरें सबसे आम थीं।", "मुहरों का निर्माण केवल हड़प्पा में किया जाता था।"],
        1,
        "मुहरों को सेलखड़ी के चौकोर टुकड़ों पर उल्टी नक्काशी (Intaglio) करके बनाया जाता था। नक्काशी के बाद इन्हें भट्टी में पकाया जाता था ताकि पत्थर सख्त सफेद इनस्टैटाइट में बदल जाए।"
    ),
    # Q39
    (
        "हड़प्पा कपड़ा उद्योग के संदर्भ में, वस्त्रों को रंगने के लिए प्रयुक्त होने वाले रंग का मुख्य स्रोत क्या था?",
        ["रासायनिक डाई", "मजीठ (मदार) की जड़ से मिलने वाला लाल रंग", "केसर", "केवल नील"],
        1,
        "सूती कपड़े के टुकड़ों पर मिले लाल रंग के अवशेषों से मजीठ (Madder) नामक वनस्पति डाई के उपयोग का संकेत मिलता है, जो रंगाई कला के उन्नत ज्ञान को दर्शाता है।"
    ),
    # Q40
    (
        "निम्नलिखित में से किन कारकों ने परिपक्व हड़प्पा अर्थव्यवस्था के एकीकरण और मानकीकरण में योगदान दिया?\n1. चर्ट पत्थरों पर आधारित एक समान तौल माप प्रणाली\n2. 1:2:4 के अनुपात में मानकीकृत ईंटों का आकार\n3. शोर्तुघई जैसी व्यापारिक चौकियाँ (Procurement colonies)\nनीचे दिए गए कूट का प्रयोग कर सही उत्तर चुनिए:",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        3,
        "ये तीनों कारक हड़प्पा सभ्यता की विशाल भौगोलिक सीमा के भीतर आर्थिक एकीकरण और केंद्रीकृत नियंत्रण को दर्शाते हैं।"
    ),
    # Q41
    (
        "हड़प्पा स्थलों से मिले जानवरों की हड्डियों के बारे में निम्नलिखित में से कौन सा कथन सही है?",
        ["हिरण और जंगली सूअर जैसे जंगली जानवरों की हड्डियाँ पूरी तरह से अनुपस्थित हैं।", "पालतू गाय, भेड़ और बकरी की हड्डियाँ इंगित करती हैं कि उनका उपयोग मांस और श्रम के लिए किया जाता था।", "मछली या पक्षियों की कोई हड्डी नहीं मिली है।", "पालतू जानवरों की हड्डियाँ दर्शाती हैं कि उनका उपयोग केवल धार्मिक बलिदान के लिए होता था।"],
        1,
        "हड़प्पा स्थलों से बड़ी मात्रा में मवेशियों, भैंसों, भेड़ों और बकरियों की हड्डियाँ मिली हैं, जो कृषि और पशुपालन आधारित अर्थव्यवस्था में उनकी उपयोगिता को दर्शाती हैं।"
    ),
    # Q42
    (
        "हड़प्पा के गहनों में प्रयुक्त होने वाला हरे रंग का अर्ध-मूल्यवान पत्थर जेड (Jade) किस क्षेत्र से आयात किया जाता था?",
        ["मध्य एशिया / पामीर", "ओमान", "कर्नाटक", "बिहार"],
        0,
        "जेड पत्थर को पामीर या मध्य एशिया के क्षेत्रों से आयात किया जाता था, जो उनके विस्तृत थल व्यापारिक मार्गों को दर्शाता है।"
    ),
    # Q43
    (
        "हड़प्पा वासियों द्वारा चांदी (Silver) के आभूषण बनाए जाते थे। वे चांदी कहाँ से प्राप्त करते थे?",
        ["कोलार खदानें", "अफगानिस्तान और ईरान", "राजस्थान की खेत्री खदानें", "ओमान"],
        1,
        "चांदी को मुख्य रूप से अफगानिस्तान और ईरान से आयात किया जाता था क्योंकि यह सिंधु घाटी के मैदानी भागों में उपलब्ध नहीं थी।"
    ),
    # Q44
    (
        "सिंध में सिंधु नदी के मुहाने के पास स्थित कौन सा तटीय हड़प्पा स्थल शंख की वस्तुएं बनाने और निर्यात के लिए प्रसिद्ध था?",
        ["बालाकोट", "सुत्कागेंदोर", "अल्लाहदीनो", "सुरकोटदा"],
        0,
        "बालाकोट विंदर नदी के मुहाने के पास स्थित एक तटीय स्थल था जो शंख उद्योग और तटीय व्यापारिक गतिविधियों का प्रमुख केंद्र था।"
    ),
    # Q45
    (
        "सिंधु घाटी सभ्यता का सबसे पश्चिमी स्थल, जो मकरान तट पर ईरान सीमा के पास एक सुदृढ़ व्यापारिक चौकी के रूप में कार्य करता था, कौन सा है?",
        ["सुत्कागेंदोर", "बालाकोट", "धोलावीरा", "सोत्का कोह"],
        0,
        "मकरान तट पर स्थित सुत्कागेंदोर सिंधु सभ्यता का सबसे पश्चिमी छोर था, जो फारस की खाड़ी और ओमान की ओर जाने वाले समुद्री मार्गों की निगरानी करने वाला एक दुर्ग था।"
    ),
    # Q46
    (
        "उत्तर हड़प्पा काल (Late Harappan phase) में व्यापारिक अर्थव्यवस्था के पतन के संदर्भ में निम्नलिखित में से कौन सी घटना घटी?",
        ["मेसोपोटामिया के साथ व्यापार में भारी वृद्धि हुई।", "तौल और माप अधिक कड़े रूप से मानकीकृत हो गए।", "लंबी दूरी के व्यापार नेटवर्क समाप्त हो गए और बाट क्षेत्रीय व असमान हो गए।", "वस्तु विनिमय के स्थान पर लोहे के सिक्कों का प्रचलन हुआ।"],
        2,
        "1900 ईसा पूर्व के बाद उत्तर हड़प्पा काल में मेसोपोटामिया के साथ व्यापार समाप्त हो गया, मानक चर्ट बाट लुप्त हो गए और स्थानीय वस्तु विनिमय प्रणालियाँ लौट आईं।"
    ),
    # Q47
    (
        "लोथल गोदीवाड़ा में अतिरिक्त पानी निकालने वाले मार्ग (Spillway) का मुख्य उद्देश्य क्या था?",
        ["शहर को पीने का पानी पहुँचाना", "दीवारों को टूटने से बचाने के लिए अतिरिक्त पानी बाहर निकालना", "मछली पकड़ने वाली छोटी नावों को रास्ता देना", "गोदी से जमे हुए गाद को साफ करना"],
        1,
        "स्पिलवे एक चैनल था जिसमें एक सरकने वाला गेट लगा हुआ था, जो बाढ़ या उच्च ज्वार के समय अतिरिक्त पानी को बाहर निकाल देता था ताकि गोदी में पानी का स्तर स्थिर रहे।"
    ),
    # Q48
    (
        "निम्नलिखित में से कौन सा कच्चा माल दक्षिण भारत की नीलगिरी पहाड़ियों से मँगाया जाता था?",
        ["एमेथिस्ट", "सोना", "तांबा", "लाजवर्त"],
        1,
        "सोना दक्षिण भारत (कर्नाटक की कोलार और नीलगिरी पहाड़ियों) से मँगाया जाता था, जहाँ नदियों की रेत से भी सोना निकाला जाता था।"
    ),
    # Q49
    (
        "हड़प्पा शिल्प में सूक्ष्म सेलखड़ी मनकों (steatite beads) के निर्माण के लिए कौन सा स्थल एक प्रमुख औद्योगिक हब माना जाता है?",
        ["चन्हुदड़ो", "हड़प्पा", "कालीबंगन", "राखीगढ़ी"],
        0,
        "चन्हुदड़ो एक शिल्प उत्पादन केंद्र था, जो विशेष रूप से सेलखड़ी के अति-सूक्ष्म (microscopic) मनके बनाने के लिए प्रसिद्ध था, जिसमें उच्च तकनीकी कौशल की आवश्यकता होती थी।"
    ),
    # Q50
    (
        "कालीबंगन के दोहरे जुते हुए खेत के ग्रिड पैटर्न के संबंध में निम्नलिखित में से कौन सा कथन सही है?",
        ["हल रेखाएँ केवल एक ही दिशा में एक-दूसरे के समानांतर थीं।", "हल रेखाएँ एक-दूसरे को समकोण पर काटती थीं, जिसमें एक समूह पास-पास और दूसरा दूर-दूर था।", "यह दर्शाता है कि धान और गेहूँ एक साथ उगाए जाते थे।", "यह ग्रिड जल निकासी के लिए बनाया गया था, खेती के लिए नहीं।"],
        1,
        "कालीबंगन में जुते हुए खेत की रेखाएँ एक-दूसरे को समकोण पर काटती थीं। चौड़ी दूरी वाली रेखाओं में सरसों जैसी लंबी फसलें और संकरी दूरी वाली रेखाओं में चने जैसी छोटी फसलें उगाई जाती थीं।"
    )
]

# Define the mock test questions - 10 questions
mock_raw_eng = [
    # MQ1
    (
        "Consider the following statements regarding Harappan agriculture and land tillage:\n1. The ploughed field excavated at Kalibangan shows grid furrows, implying double-cropping during the Mature phase.\n2. Banawali in Haryana has yielded the actual preserved wooden ploughshares used by Harappan farmers.\nWhich of the statements given above is/are correct?",
        ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        0,
        "Statement 1 is correct: Kalibangan has the ploughed field showing double-cropping. Statement 2 is incorrect: wooden ploughshares have not been preserved due to decay; Banawali yielded terracotta models of ploughs, not the actual wooden ones."
    ),
    # MQ2
    (
        "With reference to water resource management in the Indus Valley Civilisation, which of the following statements is/are correct?\n1. Traces of stone-built dams or Gabarbands have been found in the Baluchistan region.\n2. Massive, stone-cut rainwater harvesting reservoirs have been discovered at Dholavira.\n3. A complex network of brick-lined irrigation canals is present throughout the Indus alluvial plains.\nSelect the correct answer using the code given below:",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Gabarbands in Baluchistan and reservoirs at Dholavira are well-documented. Statement 3 is incorrect: there is a lack of brick-lined irrigation canals in the alluvial plains of Punjab and Sindh (only found at Shortughai, Afghanistan)."
    ),
    # MQ3
    (
        "Consider the following statements about animal domestication and representations in the Harappan Civilisation:\n1. The horse is the most frequently depicted animal on Harappan seals and copper tablets.\n2. Bones of humped cattle, sheep, goats, and pigs are widely found at Harappan residential sites, showing their dietary importance.\nWhich of the statements given above is/are correct?",
        ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        1,
        "Statement 1 is incorrect: the horse is never depicted on seals; the unicorn is the most common animal, followed by the bull, elephant, etc. Statement 2 is correct: bones of domestic livestock indicate they were kept for meat, milk, and labor."
    ),
    # MQ4
    (
        "Consider the following pairs of craft specialization centers and their primary raw materials:\n1. Balakot : Shell-working\n2. Chanhudaro : Bead-making\n3. Nageshwar : Steatite seal production\nWhich of the pairs given above is/are correctly matched?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        0,
        "Pairs 1 and 2 are correctly matched: Balakot was coastal and specialized in shell-working; Chanhudaro specialized in bead-making. Nageshwar is also coastal and specialized in shell-working, not steatite seal production."
    ),
    # MQ5
    (
        "With reference to the system of weights and measures in the Mature Harappan Civilisation, consider the following statements:\n1. Lower denominations followed a binary system, while higher weights followed a decimal system.\n2. The standard unit of weight was based on chert cubical weights weighing approximately 13.63 grams.\n3. The system of linear measurement was completely non-standardized and varied between cities.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Standardized chert weights followed a binary-decimal system. Statement 3 is incorrect: linear scales found at Mohenjo-daro, Lothal, and Harappa prove that linear measurement was highly standardized."
    ),
    # MQ6
    (
        "Consider the following statements regarding Harappan metallurgy and resource procurement:\n1. Tin was sourced locally from Rajasthan to manufacture bronze tools.\n2. Copper was imported from Makan (modern Oman) and also obtained from the Khetri mines of Rajasthan.\n3. Iron was utilized to reinforce bronze chisels and saws for stone carving.\nWhich of the statements given above is/are correct?",
        ["2 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statement 2 is correct: copper came from Khetri and Oman. Statement 1 is incorrect: tin was imported from Afghanistan/Iran, not sourced locally. Statement 3 is incorrect: iron was completely unknown to the Harappans."
    ),
    # MQ7
    (
        "With reference to external trade as recorded in Mesopotamian cuneiform texts, consider the following identifications:\n1. Meluhha : The Indus region\n2. Dilmun : Bahrain in the Persian Gulf\n3. Makan : The Oman Peninsula\nWhich of the pairs given above are correctly matched?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All three identifications are widely accepted by historians. Meluhha represents the Indus region, Dilmun represents Bahrain, and Makan represents Oman/Makran coast."
    ),
    # MQ8
    (
        "The Lothal dockyard is considered an engineering marvel. Which of the following features supported its functioning?\n1. A massive wall of kiln-burnt bricks enclosing a rectangular basin.\n2. A timber lock-gate at the spillway to regulate water level according to tides.\n3. An inlet channel connecting the basin to a tributary of the Sabarmati River.\nSelect the correct answer using the code given below:",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All three statements are correct. The dockyard featured a kiln-burnt brick basin, a lock-gate spillway for tidal regulation, and an inlet channel connecting it to the river to allow ships to enter."
    ),
    # MQ9
    (
        "Consider the following statements regarding the role of seals and sealings in Harappan trade:\n1. Seals were primarily used as metallic currency to pay for imported goods.\n2. Wet clay tags (sealings) placed over package knots allowed merchants to verify if a shipment was tampered with.\nWhich of the statements given above is/are correct?",
        ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        1,
        "Statement 1 is incorrect: seals were not currency; trade was barter. Statement 2 is correct: clay sealings served as security tags to detect tampering and identify the sender."
    ),
    # MQ10
    (
        "With reference to the trade post of Shortughai, which of the following statements is/are correct?\n1. It was located in northern Afghanistan near the Kokcha River valley.\n2. It was established specifically to control the trade of Lapis Lazuli.\n3. It shows a complete absence of typical Harappan features like script and pottery.\nSelect the correct answer using the code given below:",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct: Shortughai was in northern Afghanistan and controlled lapis lazuli. Statement 3 is incorrect: Shortughai was a typical Harappan settlement yielding Harappan pottery, seals, and script inscriptions."
    )
]

mock_raw_hin = [
    # MQ1
    (
        "हड़प्पा कृषि और भूमि की जुताई के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. कालीबंगन से जुते हुए खेत में ग्रिड पैटर्न मिला है, जो परिपक्व काल के दौरान दोहरी फसल का संकेत देता है।\n2. हरियाणा के बनावली से हड़प्पा किसानों द्वारा उपयोग किए जाने वाले वास्तविक लकड़ी के हल के फलक मिले हैं।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
        ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        0,
        "कथन 1 सही है: कालीबंगन से दोहरी फसल को दर्शाने वाला जुता हुआ खेत मिला है। कथन 2 गलत है: लकड़ी के हल समय के साथ नष्ट हो गए; बनावली से मिट्टी के हल का मॉडल मिला है, न कि लकड़ी के वास्तविक हल।"
    ),
    # MQ2
    (
        "सिंधु घाटी सभ्यता में जल संसाधन प्रबंधन के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. बलूचिस्तान क्षेत्र में पत्थरों से बने बांधों या गबरबंदों के साक्ष्य मिले हैं।\n2. धोलावीरा से वर्षा जल संचयन के लिए विशाल, पत्थरों को काटकर बनाए गए जलाशय मिले हैं।\n3. सिंधु के मैदानी भागों में ईंटों से बनी सिंचाई नहरों का एक जटिल जाल बिछा हुआ था।\nनीचे दिए गए कूट का प्रयोग कर सही उत्तर चुनिए:",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। बलूचिस्तान में गबरबंद और धोलावीरा में जलाशय अच्छी तरह से प्रलेखित हैं। कथन 3 गलत है: मैदानी भागों में सिंचाई नहरों का पूर्ण अभाव है (केवल शोर्तुघई, अफगानिस्तान में नहरों के साक्ष्य मिले हैं)।"
    ),
    # MQ3
    (
        "हड़प्पा सभ्यता में पशुपालन और उनके अंकन के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. हड़प्पा की मुहरों और तांबे की पट्टिकाओं पर सबसे अधिक चित्रित किया जाने वाला पशु घोड़ा है।\n2. हड़प्पा के आवासीय स्थलों से मवेशियों, भेड़ों, बकरियों और सूअरों की हड्डियाँ बड़ी मात्रा में मिली हैं, जो उनके आहार में महत्व को दर्शाती हैं।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
        ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        1,
        "कथन 1 गलत है: मुहरों पर घोड़ा कभी चित्रित नहीं हुआ; एक सींग वाला जानवर (unicorn) सबसे आम है। कथन 2 सही है: पालतू मवेशियों की हड्डियाँ दर्शाती हैं कि उनका उपयोग मांस, दूध और श्रम के लिए किया जाता था।"
    ),
    # MQ4
    (
        "शिल्प विशिष्टता केंद्रों और उनके प्राथमिक कच्चे माल के निम्नलिखित युग्मों पर विचार कीजिए:\n1. बालाकोट : शंख उद्योग\n2. चन्हुदड़ो : मनके बनाना\n3. नागेश्वर : सेलखड़ी की मुहरों का निर्माण\nउपर्युक्त युग्मों में से कौन-सा/से सही सुमेलित है/हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        0,
        "युग्म 1 और 2 सही सुमेलित हैं: बालाकोट शंख उद्योग के लिए और चन्हुदड़ो मनके बनाने के लिए प्रसिद्ध थे। नागेश्वर भी शंख उद्योग का केंद्र था न कि सेलखड़ी मुहरों के निर्माण का।"
    ),
    # MQ5
    (
        "परिपक्व हड़प्पा सभ्यता में तौल और माप की प्रणाली के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:\n1. छोटी इकाइयाँ द्वि-आधारी (binary) प्रणाली का पालन करती थीं, जबकि बड़ी इकाइयाँ दशमलव प्रणाली का पालन करती थीं।\n2. तौल की मानक इकाई चर्ट पत्थर से बने घनाकार बाटों पर आधारित थी, जिनका वजन लगभग 13.63 ग्राम था।\n3. रैखिक माप की प्रणाली पूरी तरह से गैर-मानकीकृत थी और विभिन्न शहरों में भिन्न थी।\nउपर्युक्त कथनों में से कौन-से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। चर्ट पत्थरों से बने बाट द्वि-आधारी-दशमलव प्रणाली का पालन करते थे। कथन 3 गलत है: मोहनजोदड़ो, लोथल और हड़प्पा से मिले पैमाने यह साबित करते हैं कि माप प्रणाली अत्यधिक मानकीकृत थी।"
    ),
    # MQ6
    (
        "हड़प्पा धातु विज्ञान और संसाधन खरीद के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. कांस्य उपकरण बनाने के लिए टिन स्थानीय स्तर पर राजस्थान से प्राप्त किया जाता था।\n2. तांबा ओमान (माकन) से आयात किया जाता था और राजस्थान की खेत्री खदानों से भी प्राप्त होता था।\n3. पत्थर की नक्काशी के लिए छेनी और आरी को मजबूत करने के लिए लोहे का उपयोग किया जाता था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
        ["केवल 2", "केवल 1 और 2", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 2 सही है: तांबा खेत्री और ओमान से आता था। कथन 1 गलत है: टिन को अफगानिस्तान/ईरान से आयात किया जाता था, स्थानीय स्तर पर नहीं। कथन 3 गलत है: हड़प्पा वासियों को लोहे का कोई ज्ञान नहीं था।"
    ),
    # MQ7
    (
        "मेसोपोटामिया के कीलाक्षर ग्रंथों में उल्लिखित बाहरी व्यापार के संदर्भ में, निम्नलिखित युग्मों पर विचार कीजिए:\n1. मेलुहा : सिंधु क्षेत्र\n2. दिलमुन : फारस की खाड़ी में बहरीन\n3. माकन : ओमान प्रायद्वीप\nउपर्युक्त युग्मों में से कौन-से सही सुमेलित हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        3,
        "तीनों युग्म इतिहासकारों द्वारा व्यापक रूप से स्वीकृत हैं। मेलुहा सिंधु क्षेत्र को, दिलमुन बहरीन को और माकन ओमान को दर्शाता है।"
    ),
    # MQ8
    (
        "लोथल के गोदीवाड़ा (Dockyard) को इंजीनियरिंग का एक उत्कृष्ट नमूना माना जाता है। निम्नलिखित में से कौन सी विशेषताएं इसके संचालन का समर्थन करती थीं?\n1. पकी ईंटों की एक विशाल दीवार जो एक आयताकार बेसिन को घेरती थी।\n2. ज्वार-भाटे के अनुसार पानी के स्तर को नियंत्रित करने के लिए लकड़ी का लॉक-गेट।\n3. बेसिन को साबरमती नदी की एक सहायक नदी से जोड़ने वाली एक नहर (inlet channel)।\nनीचे दिए गए कूट का प्रयोग कर सही उत्तर चुनिए:",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        3,
        "तीनों कथन सही हैं। गोदीवाड़ा में पकी ईंटों का बेसिन, ज्वार नियंत्रण के लिए लॉक-गेट स्पिलवे और प्रवेश के लिए एक फीडर नहर शामिल थी।"
    ),
    # MQ9
    (
        "हड़प्पा व्यापार में मुहरों और मिट्टी की छापों की भूमिका के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. मुहरों का उपयोग मुख्य रूप से आयातित वस्तुओं के भुगतान के लिए धातु की मुद्रा के रूप में किया जाता था।\n2. पैकेजों की गांठों पर लगाई गई गीली मिट्टी की छाप (sealings) से व्यापारी यह जांच सकते थे कि सामान से छेड़छाड़ हुई है या नहीं।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
        ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        1,
        "कथन 1 गलत है: मुहरें मुद्रा नहीं थीं; व्यापार वस्तु विनिमय आधारित था। कथन 2 सही है: मिट्टी की छापें सामान की सुरक्षा और प्रेषक की पहचान के प्रमाण के रूप में कार्य करती थीं।"
    ),
    # MQ10
    (
        "शोर्तुघई (Shortughai) व्यापारिक चौकी के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:\n1. यह उत्तरी अफगानिस्तान में कोकचा नदी घाटी के पास स्थित था।\n2. इसकी स्थापना विशेष रूप से लाजवर्त (Lapis Lazuli) के व्यापार को नियंत्रित करने के लिए की गई थी।\n3. यहाँ हड़प्पा सभ्यता की सामान्य विशेषताओं जैसे लिपि और बर्तनों का पूर्ण अभाव है।\nनीचे दिए गए कूट का प्रयोग कर सही उत्तर चुनिए:",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं: शोर्तुघई उत्तरी अफगानिस्तान में था और लाजवर्त व्यापार को नियंत्रित करता था। कथन 3 गलत है: शोर्तुघई एक विशिष्ट हड़प्पा बस्ती थी जहाँ से हड़प्पा शैली के बर्तन, मुहरें और सिंधु लिपि के साक्ष्य मिले हैं।"
    )
]

# Convert raw practice list into expected dict format
for item in practice_raw_eng:
    q, opts, ans, sol = item
    eng_data["practiceQuestions"].append({
        "q": q,
        "opts": opts,
        "ans": ans,
        "sol": sol
    })

for item in practice_raw_hin:
    q, opts, ans, sol = item
    hin_data["practiceQuestions"].append({
        "q": q,
        "opts": opts,
        "ans": ans,
        "sol": sol
    })

# Convert raw mock list into expected dict format
for item in mock_raw_eng:
    q, opts, ans, sol = item
    eng_data["mockTestQuestions"].append({
        "q": q,
        "opts": opts,
        "ans": ans,
        "sol": sol
    })

for item in mock_raw_hin:
    q, opts, ans, sol = item
    hin_data["mockTestQuestions"].append({
        "q": q,
        "opts": opts,
        "ans": ans,
        "sol": sol
    })

# Paths to output files
eng_out = os.path.join(ENG_DIR, "content.json")
hin_out = os.path.join(HIN_DIR, "content.json")

print(f"Writing English base content to {eng_out}")
with open(eng_out, "w", encoding="utf-8") as f:
    json.dump(eng_data, f, ensure_ascii=False, indent=2)

print(f"Writing Hindi base content to {hin_out}")
with open(hin_out, "w", encoding="utf-8") as f:
    json.dump(hin_data, f, ensure_ascii=False, indent=2)

print("Base build script executed successfully!")
