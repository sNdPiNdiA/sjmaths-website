import json
import os

ENG_DIR = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\HarappanIndus-Valley-Civilisation\Harappan-Trade"
HIN_DIR = os.path.join(ENG_DIR, "hi")
os.makedirs(HIN_DIR, exist_ok=True)

# English base structure
eng_data = {
    "breadcrumbs": {
        "parent": "UPSC Syllabus",
        "parentUrl": "/upsc/",
        "current": "Harappan Trade"
    },
    "hero": {
        "title": "Harappan Trade & Commercial Networks",
        "description": "Master the raw material procurement systems, inland caravans, overland Central Asian contacts, and Persian Gulf/Mesopotamian maritime linkages of the Indus Civilisation for UPSC GS-1."
    },
    "labels": {
        "clickToExpand": "Click to expand details",
        "mockIntro": {
            "title": "Interactive UPSC Mock Test",
            "description": "Assess your depth on Harappan trade routes, cuneiform evidence, port sites, and weight networks. This timed test contains 10 high-yield, exam-standard questions with negative marking.",
            "startBtn": "Start Mock Test"
        },
        "mockPlay": {
            "prevBtn": "Previous Question",
            "nextBtn": "Next Question",
            "submitBtn": "Submit Test"
        }
    },
    "timeline": {
        "title": "Evolution of Harappan Commerce",
        "description": "Chronological development of trade linkages from local networks to overseas maritime routes.",
        "cards": [
            {
                "period": "Early Harappan Trade",
                "date": "c. 3300 BCE - 2600 BCE",
                "details": "Establishment of regional procurement routes, early metallurgy exchanges, and initial trade networks linking Rajasthan (copper) and Baluchistan with the plains."
            },
            {
                "period": "Mature Harappan Trade Apex",
                "date": "c. 2600 BCE - 1900 BCE",
                "details": "Booming maritime trade with Mesopotamia and the Gulf. Specialized trade ports like Lothal and outposts like Shortughai operated under uniform weight systems."
            },
            {
                "period": "Late Harappan Decentralization",
                "date": "c. 1900 BCE - 1300 BCE",
                "details": "Collapse of international maritime links with Mesopotamia, abandonment of the Shortughai outpost, and localization of trade networks using barter."
            }
        ]
    },
    "mnemonics": {
        "title": "Mnemonics & Memory Hacks",
        "description": "Use these visual hooks to memorize critical trade routes, port outposts, and commodities for UPSC.",
        "items": [
            {
                "title": "Mnemonic 1: Persian Gulf Transit Centers",
                "phrase": "\"Dil-Mak-Mel (Dilmun, Makan, Meluhha)\"",
                "decryption": "Remember the sequence of ports from west to east along the Persian Gulf: **Dil**mun (Bahrain) -> **Mak**an (Oman) -> **Mel**uhha (Indus valley)."
            },
            {
                "title": "Mnemonic 2: Specialized Coastal Trade Ports",
                "phrase": "\"Loth-Sut-Sot-Bal (Lothal, Sutkagendor, Sotka Koh, Balakot)\"",
                "decryption": "The key coastal ports along the Arabian Sea and Makran coast: **Loth**al (Gujarat port), **Sut**kagendor (western border fort), **Sot**ka Koh (coastal monitoring station), **Bal**akot (shell-work and port hub)."
            },
            {
                "title": "Mnemonic 3: Overland Imports of Rare Metals",
                "phrase": "\"Sil-Af-Ir, Gold-Ka, Jade-Pam (Silver-Afghan/Iran, Gold-Karnataka, Jade-Pamir)\"",
                "decryption": "Imports sourcing: **Sil**ver from **Af**ghanistan and **Ir**an; **Gold** from **Ka**rnataka (Kolar); **Jade** from Central Asia/**Pam**ir mountains."
            }
        ]
    },
    "flashcards": {
        "title": "Active Recall Flashcards",
        "description": "Test your knowledge on Harappan trade routes and cuneiform references.",
        "items": [
            {
                "question": "What does the cuneiform inscription from Sargon of Akkad say about Meluhha?",
                "answer": "Sargon of Akkad (c. 2350 BCE) boasted that <strong>ships from Meluhha, Makan, and Dilmun</strong> docked at his capital city of Akkad, verifying direct maritime shipping lines.",
                "icon": "fa-anchor"
            },
            {
                "question": "Which site was the westernmost trading outpost of the Harappan civilization, and where was it located?",
                "answer": "<strong>Sutkagendor</strong>. It was a fortified outpost located on the Makran coast near the modern Iran-Pakistan border, strategically placed to control Gulf trade.",
                "icon": "fa-shield-halved"
            },
            {
                "question": "Name the trading colony established near the lapis lazuli mines, and its location.",
                "answer": "<strong>Shortughai</strong> in northern Afghanistan, located near the Oxus (Amu Darya) river valley, established specifically to control the procurement of lapis lazuli.",
                "icon": "fa-gem"
            },
            {
                "question": "How did Harappans secure commercial cargo during transport?",
                "answer": "By applying wet clay over package knots and pressing a seal to leave an impression (called a <strong>sealing</strong>). An unbroken sealing proved that the cargo arrived untampered.",
                "icon": "fa-lock"
            },
            {
                "question": "Which circular seal found at Lothal demonstrates maritime connections with the Persian Gulf?",
                "answer": "A circular <strong>'Persian Gulf' button seal</strong> with double-boss backing, typical of seals found at Bahrain (Dilmun) and Mesopotamian ports.",
                "icon": "fa-circle-dot"
            }
        ]
    },
    "deepDive": {
        "title": "Syllabus Core Study Notes (Deep-Dive)",
        "description": "Explore the multi-layered commercial networks of the Indus Valley Civilisation.",
        "sections": [
            {
                "title": "1. Internal Trade & Procurement Strategies",
                "content": """<p>Harappan urban centers required massive quantities of raw materials not available in alluvial plains, leading to targeted procurement strategies.</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-compass"></i> Resource Expeditions & Colony Setup</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>Procurement Colonies:</strong> Established at <strong>Shortughai</strong> (Badakhshan, Afghanistan) near lapis lazuli veins, and at <strong>Nageshwar</strong>/<strong>Balakot</strong> near shell resource areas.</li>
      <li><strong>Expeditions:</strong> Sent special merchant parties to Rajasthan's <strong>Khetri copper belt</strong> and to South India (Nilgiris/Karnataka) for <strong>gold</strong>.</li>
      <li><strong>Local Sourcing:</strong> Gujarat sites secured agate, carnelian, and chalcedony; steatite was sourced from southern Rajasthan and northern Gujarat.</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-truck-ramp-box"></i> Inland Transport & Exchange Networks</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>Land Transport:</strong> Performed via solid-wheeled wooden bullock carts, as verified by clay toy models and fossilized ruts matching modern track gauges (~1.1 to 1.8 m).</li>
      <li><strong>River Transport:</strong> Flat-bottomed river boats transported bulk grains and finished goods along the Indus and Ghaggar-Hakra river basins.</li>
      <li><strong>Exchange Systems:</strong> No monetary coins existed. Internal trade relied on a highly standardized <strong>barter system</strong> regulated by uniform weights and measures.</li>
    </ul>
  </div>
</div>""",
                "masteryZone": []
            },
            {
                "title": "2. Overland Trade & Central Asian Networks",
                "content": """<p>Harappan overland trade linked the Indus Valley across mountain passes with the resource-rich regions of Afghanistan, Iran, and Central Asia.</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-route"></i> Caravan Routes & Mountain Passes</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>Passes:</strong> Pack-ox caravans utilized the <strong>Bolan Pass</strong>, <strong>Gomal Pass</strong>, and <strong>Khyber Pass</strong> to cross the Hindu Kush and Sulaiman ranges into the highlands.</li>
      <li><strong>Afghan Hubs:</strong> Connected directly to Mundigak and Badakhshan, linking the plains with Central Asian trade routes.</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-globe"></i> Oxus and Iranian Civilisation Contacts</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>BMAC (Oxus Civilisation):</strong> Trade contacts are shown by Harappan-style ivory objects, seals, and beads recovered in Bactria-Margiana Archaeological Complex sites.</li>
      <li><strong>Iranian Plateau:</strong> Shahr-i Sokhta (Sistan) served as a vital transit point where Harappan lapis lazuli was cut and processed for further western export.</li>
      <li><strong>Imports/Exports:</strong> Imported <strong>silver</strong> (from Afghanistan/Iran), <strong>turquoise</strong> (from Khorasan/Central Asia), and <strong>jade</strong> (from Central Asia/Pamir). Exported textiles, ivory, etched carnelian beads, and copper artifacts.</li>
    </ul>
  </div>
</div>""",
                "masteryZone": []
            },
            {
                "title": "3. Maritime Trade & Mesopotamian Connections",
                "content": """<p>Maritime commerce connected the Harappan ports via the Persian Gulf with the Mesopotamian empire during the Akkadian and Ur III periods.</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-ship"></i> Akkadian Cuneiform & Gulf Transshipments</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>Meluhha, Makan, Dilmun:</strong> Mesopotamian texts refer to <strong>Meluhha</strong> (the Indus region), <strong>Makan</strong> (Oman, source of nickel-bearing copper), and <strong>Dilmun</strong> (Bahrain, the transit island of 'clean water').</li>
      <li><strong>Sargon's Records:</strong> King Sargon of Akkad boasted that ships from Meluhha docked at the quays of Akkad. Inscribed Mesopotamian tablets record imports of ivory, gold, lapis lazuli, and carnelian from Meluhha.</li>
      <li><strong>Persian Gulf Seals:</strong> Circular button seals found at Lothal show direct links with Gulf merchants who acted as trade intermediaries.</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-anchor"></i> Port Engineering & Western Outposts</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>Lothal Dockyard:</strong> A massive rectangular basin (214 x 36 m) of baked bricks connected via a canal to the Sabarmati estuary. It featured a wooden sluice/lock-gate system to float ships during low tides.</li>
      <li><strong>Fortified Outposts:</strong> Coastal stations at <strong>Sutkagendor</strong> and <strong>Sotka Koh</strong> on the Makran coast monitored and sheltered trade vessels against storms, securing the sea route into the Gulf.</li>
      <li><strong>Barter Trade:</strong> Seals and clay sealings secured cargo packages. Mesopotamians paid in silver, wool, textiles, and bitumen, while Harappans sent carnelian, lapis, and exotic woods.</li>
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
            "<strong>Trap 1:</strong> Do not assume that the presence of Harappan seals in Mesopotamia means they were used as coin money. They were purely security marks on clay tags or personal administrative tokens.",
            "<strong>Trap 2:</strong> Watch out for statements claiming that Sargon of Akkad visited Meluhha. Sargon only claimed that Meluhhan ships docked at *his* capital city of Akkad.",
            "<strong>Trap 3:</strong> Do not confuse Dilmun with Oman. Dilmun is identified with the island of <strong>Bahrain</strong>, while Makan (or Magan) refers to <strong>Oman</strong> and the Makran coast.",
            "<strong>Trap 4:</strong> Be careful with statements claiming that the horse was a trade commodity. There is no evidence of horse trading or horse-drawn cargo vehicles in Harappan times.",
            "<strong>Trap 5:</strong> Do not select options stating that iron was imported from Central Asia. <strong>Iron was completely unknown</strong> to the Harappans; they only alloyed copper with tin."
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
        "current": "हड़प्पा व्यापार"
    },
    "hero": {
        "title": "हड़प्पा व्यापार और वाणिज्यिक नेटवर्क",
        "description": "यूपीएससी परीक्षा (GS-1) के लिए सिंधु घाटी सभ्यता के कच्चे माल की प्राप्ति प्रणालियों, स्थलीय कारवां, मध्य एशियाई संपर्कों और फारस की खाड़ी/मेसोपोटामिया समुद्री संबंधों का अध्ययन करें।"
    },
    "labels": {
        "clickToExpand": "विवरण देखने के लिए क्लिक करें",
        "mockIntro": {
            "title": "इंटरैक्टिव परीक्षा मॉक टेस्ट",
            "description": "हड़प्पा व्यापार मार्गों, कीलाक्षर लेखों, तटीय बंदरगाहों और भार प्रणालियों के संबंध में अपनी तैयारी का मूल्यांकन करें। इस समयबद्ध परीक्षण में 10 उच्च-स्तरीय यूपीएससी मानक के प्रश्न शामिल हैं।",
            "startBtn": "मॉक टेस्ट शुरू करें"
        },
        "mockPlay": {
            "prevBtn": "Previous Question",
            "nextBtn": "Next Question",
            "submitBtn": "Submit Test"
        }
    },
    "timeline": {
        "title": "हड़प्पा व्यापार का विकास",
        "description": "स्थानीय विनिमय से लेकर सुदूर विदेशी समुद्री व्यापार मार्गों तक के विकास को समझें।",
        "cards": [
            {
                "period": "प्रारंभिक हड़प्पा व्यापार",
                "date": "लगभग 3300 ईसा पूर्व - 2600 ईसा पूर्व",
                "details": "क्षेत्रीय खरीद मार्गों की स्थापना, शुरुआती धातु विनिमय और राजस्थान (तांबा) व बलूचिस्तान को मैदानी भागों से जोड़ने वाले व्यापारिक नेटवर्क का विकास।"
            },
            {
                "period": "परिपक्व हड़प्पा व्यापार (चरमोत्कर्ष)",
                "date": "लगभग 2600 ईसा पूर्व - 1900 ईसा पूर्व",
                "details": "मेसोपोटामिया और खाड़ी देशों के साथ समुद्री व्यापार का चरम। लोथल जैसे बंदरगाह और शोर्तुघई जैसी व्यापारिक चौकियाँ एक समान वजन प्रणालियों के तहत काम करती थीं।"
            },
            {
                "period": "उत्तर हड़प्पा व्यापार (विकेंद्रीकरण)",
                "date": "लगभग 1900 ईसा पूर्व - 1300 ईसा पूर्व",
                "details": "मेसोपोटामिया के साथ अंतर्राष्ट्रीय समुद्री संबंधों का पतन, शोर्तुघई चौकी का परित्याग और स्थानीय वस्तु विनिमय के साथ व्यापारिक नेटवर्क का संकुचन।"
            }
        ]
    },
    "mnemonics": {
        "title": "याद रखने के सूत्र (Mnemonics)",
        "description": "यूपीएससी परीक्षा के लिए प्रमुख बंदरगाहों, व्यापार मार्गों और आयातित वस्तुओं को आसानी से याद रखने के लिए इन सूत्रों का उपयोग करें।",
        "items": [
            {
                "title": "याद रखने का सूत्र 1: फारस की खाड़ी के पारगमन बंदरगाह",
                "phrase": "\"दि-मा-मे (दिलमुन, माकन, मेलुहा)\"",
                "decryption": "फारस की खाड़ी के किनारे पश्चिम से पूर्व की ओर बंदरगाहों का क्रम याद रखें: **दि**लमुन (बहरीन) -> **मा**कन (ओमान) -> **मे**लुहा (सिंधु घाटी)।"
            },
            {
                "title": "याद रखने का सूत्र 2: विशिष्ट तटीय व्यापारिक बंदरगाह",
                "phrase": "\"लो-सु-सो-बा (लोथल, सुत्कागेंदोर, सोत्का कोह, बालाकोट)\"",
                "decryption": "अरब सागर और मकरान तट के प्रमुख बंदरगाह: **लो**थल (गुजरात बंदरगाह), **सु**त्कागेंदोर (पश्चिमी सीमा दुर्ग), **सो**त्का कोह (तटीय निगरानी चौकी), **बा**लाकोट (शंख उद्योग और बंदरगाह)।"
            },
            {
                "title": "याद रखने का सूत्र 3: दुर्लभ धातुओं का थल मार्ग से आयात",
                "phrase": "\"चा-अ-ई, सो-क, जे-पा (चांदी-अफगान/ईरान, सोना-कर्नाटक, जेड-पामिर)\"",
                "decryption": "आयातित स्रोतों का सूत्र: **चा**ंदी का आयात **अ**फगानिस्तान और **ई**रान से; **सो**ना **क**र्नाटक (कोलार) से; **जे**ड (Jade) मध्य एशिया/**पा**मीर पहाड़ों से।"
            }
        ]
    },
    "flashcards": {
        "title": "सक्रिय स्मरण फ्लैशकार्ड (Active Recall)",
        "description": "हड़प्पा व्यापार मार्गों और मेसोपोटामिया के कीलाक्षर लेखों के विवरणों का परीक्षण करें।",
        "items": [
            {
                "question": "मेसोपोटामिया के सारगोन के अभिलेखों में मेलुहा के व्यापार का क्या विवरण है?",
                "answer": "अक्कड़ के राजा सारगोन (लगभग 2350 ईसा पूर्व) ने गर्व से लिखा था कि <strong>मेलुहा, माकन और दिलमुन के जहाज</strong> उसकी राजधानी अक्कड़ के बंदरगाह पर आते थे।",
                "icon": "fa-anchor"
            },
            {
                "question": "हड़प्पा सभ्यता की सबसे पश्चिमी व्यापारिक चौकी कौन सी थी और यह कहाँ स्थित थी?",
                "answer": "<strong>सुत्कागेंदोर</strong>। यह मकरान तट पर आधुनिक ईरान-पाकिस्तान सीमा के पास स्थित एक सुदृढ़ दुर्ग था, जिसका उद्देश्य फारस की खाड़ी के व्यापार को नियंत्रित करना था।",
                "icon": "fa-shield-halved"
            },
            {
                "question": "लाजवर्त (Lapis Lazuli) प्राप्त करने के लिए स्थापित हड़प्पा उपनिवेश और उसकी स्थिति क्या थी?",
                "answer": "उत्तरी अफगानिस्तान में आक्सस नदी घाटी के पास स्थित <strong>शोर्तुघई</strong>, जिसे लाजवर्त की प्राप्ति को नियंत्रित करने के लिए स्थापित किया गया था।",
                "icon": "fa-gem"
            },
            {
                "question": "परिवहन के दौरान सामान की थैलियों को कैसे सुरक्षित किया जाता था?",
                "answer": "गांठों पर गीली मिट्टी लगाकर उस पर मुहर दबाई जाती थी, जिसे <strong>सीलिंग (sealing)</strong> कहते थे। बिना टूटी सील यह साबित करती थी कि सामान के साथ छेड़छाड़ नहीं की गई है।",
                "icon": "fa-lock"
            },
            {
                "question": "लोथल से मिली कौन सी गोल मुहर फारस की खाड़ी के साथ सीधे समुद्री व्यापार को दर्शाती है?",
                "answer": "एक गोल <strong>'फारस की खाड़ी' की बटन मुहर</strong> जिसके पीछे कूबड़ (double boss) बना था। ऐसी मुहरें बहरीन (दिलमुन) और मेसोपोटामिया में आम थीं।",
                "icon": "fa-circle-dot"
            }
        ]
    },
    "deepDive": {
        "title": "पाठ्यक्रम मुख्य अध्ययन नोट्स (विस्तृत)",
        "description": "सिंधु घाटी सभ्यता के बहुस्तरीय घरेलू और अंतर्राष्ट्रीय व्यापारिक नेटवर्क को समझें।",
        "sections": [
            {
                "title": "1. आंतरिक व्यापार और संसाधन प्राप्ति रणनीतियाँ",
                "content": """<p>हड़प्पा सभ्यता के जलोढ़ मैदानों में खनिजों की भारी कमी थी, जिसके कारण उन्होंने विशिष्ट संसाधन प्राप्ति रणनीतियाँ विकसित की थीं।</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-compass"></i> संसाधन उपनिवेश और अभियान</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>व्यापारिक उपनिवेश:</strong> लाजवर्त के लिए उत्तरी अफगानिस्तान में <strong>शोर्तुघई</strong> और शंख के लिए तटीय स्थलों जैसे <strong>नागेश्वर</strong> और <strong>बालाकोट</strong> में बस्तियां बसाई गईं।</li>
      <li><strong>संसाधन अभियान:</strong> राजस्थान के <strong>खेत्री तांबा क्षेत्र</strong> और दक्षिण भारत (कर्नाटक की नीलगिरि पहाड़ियों) में <strong>सोने</strong> की प्राप्ति के लिए अभियान भेजे जाते थे।</li>
      <li><strong>स्थानीय स्रोत:</strong> गुजरात के तटीय क्षेत्रों से अकीक (Carnelian), लाल पत्थर और सेलखड़ी (Steatite) राजस्थान-गुजरात सीमा क्षेत्रों से मँगाए जाते थे।</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-truck-ramp-box"></i> घरेलू परिवहन और विनिमय नेटवर्क</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>थल परिवहन:</strong> ठोस पहियों वाली लकड़ी की बैलगाड़ियों द्वारा होता था। पुरातात्विक खुदाई में पहियों के निशान मिले हैं जिनकी चौड़ाई (1.1 से 1.8 मीटर) आधुनिक बैलगाड़ियों से मेल खाती है।</li>
      <li><strong>जल परिवहन:</strong> सिंधु और घग्गर नदियों के जलमार्गों में अनाज और अन्य माल ले जाने के लिए चपटे तल वाली नावों का प्रयोग होता था।</li>
      <li><strong>विनिमय प्रणाली:</strong> सिक्कों का अस्तित्व नहीं था। संपूर्ण आंतरिक व्यापार मानकीकृत भार और बाटों पर आधारित <strong>वस्तु विनिमय (Barter)</strong> प्रणाली द्वारा नियंत्रित था।</li>
    </ul>
  </div>
</div>""",
                "masteryZone": []
            },
            {
                "title": "2. स्थलीय व्यापार और मध्य एशियाई नेटवर्क",
                "content": """<p>हड़प्पा थल मार्गों द्वारा पहाड़ी दर्रों को पार करके अफगानिस्तान, ईरान और मध्य एशिया के खनिज-समृद्ध देशों से जुड़ा हुआ था।</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-route"></i> कारवां मार्ग और पहाड़ी दर्रे</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>पहाड़ी दर्रे:</strong> बैलों के कारवां <strong>बोलन दर्रे</strong>, <strong>गोमल दर्रे</strong> और <strong>खैबर दर्रे</strong> से होकर हिंदूकुश और सुलेमान पर्वत श्रेणियों को पार करते थे।</li>
      <li><strong>अफगान हब:</strong> ये कारवां सीधे मुंडीगाक और बदख्शां को सिंधु मैदानों से जोड़ते थे, जो आगे मध्य एशिया तक जाते थे।</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-globe"></i> आक्सस और ईरानी सभ्यताओं से संबंध</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>आक्सस सभ्यता (BMAC):</strong> मध्य एशिया की बैक्टीरियन सभ्यता के स्थलों से हड़प्पा शैली की मुहरें, हाथीदांत की वस्तुएं और मनके मिले हैं, जो आपसी संपर्कों के साक्ष्य हैं।</li>
      <li><strong>ईरानी पठार:</strong> सीस्तान में स्थित शहर 'शहर-ए-सोख्ता' (Shahr-i Sokhta) एक पारगमन केंद्र था जहाँ सिंधु का लाजवर्त काटकर साफ किया जाता था और पश्चिम की ओर भेजा जाता था।</li>
      <li><strong>आयात-निर्यात:</strong> थल मार्ग द्वारा <strong>चांदी</strong> (अफगानिस्तान/ईरान से), <strong>फिरोजा</strong> (खुरासान से) और <strong>जेड</strong> (मध्य एशिया/पामीर से) का आयात होता था। इसके बदले सूती वस्त्र, हाथीदांत और अकीक के नक्काशीदार मनके निर्यात किए जाते थे।</li>
    </ul>
  </div>
</div>""",
                "masteryZone": []
            },
            {
                "title": "3. समुद्री व्यापार और मेसोपोटामिया संबंध",
                "content": """<p>समुद्री मार्ग फारस की खाड़ी के पारगमन बंदरगाहों से होते हुए सिंधु सभ्यता को अक्कड़ और उर के मेसोपोटामियाई साम्राज्य से जोड़ता था।</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-ship"></i> मेसोपोटामिया के अभिलेख और खाड़ी पारगमन बंदरगाह</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>मेलुहा, माकन, दिलमुन:</strong> कीलाक्षर अभिलेखों में <strong>मेलुहा</strong> (सिंधु घाटी), <strong>माकन</strong> (ओमान, जहाँ से निकल युक्त तांबा आता था) और <strong>दिलमुन</strong> (बहरीन, जिसे स्वच्छ पानी का देश कहा गया) का उल्लेख है।</li>
      <li><strong>सारगोन के साक्ष्य:</strong> अक्कड़ के सम्राट सारगोन ने दावा किया था कि मेलुहा के जहाज उसकी राजधानी के बंदरगाह पर आते थे। पट्टिकाओं में मेलुहा से हाथीदांत, लाजवर्त, सोना और लकड़ी के आयात का उल्लेख है।</li>
      <li><strong>खाड़ी मुहरें:</strong> लोथल से मिली फारस की खाड़ी की मुहरें यह साबित करती हैं कि खाड़ी के व्यापारी मध्यस्थ की भूमिका निभाते थे।</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-anchor"></i> गोदीवाड़ा (Dockyard) इंजीनियरिंग और तटीय दुर्ग</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>लोथल का गोदीवाड़ा:</strong> पकी ईंटों से बना 214 x 36 मीटर का तालाब जो भोगावो-साबरमती estuary से जुड़ा था। इसमें एक लकड़ी का फाटक (sluice gate) था जो ज्वार के समय पानी का स्तर बनाए रखता था।</li>
      <li><strong>तटीय चौकियाँ:</strong> मकरान तट पर स्थित <strong>सुत्कागेंदोर</strong> और <strong>सोत्का कोह</strong> जैसे सुदृढ़ स्थल समुद्री व्यापारिक जहाजों को आश्रय और समुद्री डाकुओं से सुरक्षा प्रदान करते थे।</li>
      <li><strong>विनिमय और विधी:</strong> मेसोपोटामिया वासी ऊन, कपड़ा और कोलतार (bitumen) देते थे, जिसके बदले वे हड़प्पा से लाल अकीक, लाजवर्त और कीमती लकड़ियाँ लेते थे।</li>
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
            "<strong>गलती 1:</strong> यह न मानें कि मेसोपोटामिया में हड़प्पा मुहरों का मिलना वहां सिंधु सिक्कों के प्रचलन को दर्शाता है। ये केवल व्यापारिक सामान पर सीलिंग लगाने के सुरक्षा उपकरण थे।",
            "<strong>गलती 2:</strong> इस कथन से सावधान रहें कि सारगोन मेलुहा आया था। सारगोन ने केवल यह लिखा था कि मेलुहा के जहाज उसकी राजधानी अक्कड़ आए थे।",
            "<strong>गलती 3:</strong> दिलमुन को ओमान समझने की भूल न करें। दिलमुन की पहचान फारस की खाड़ी के द्वीप <strong>बहरीन</strong> से है, जबकि माकन (Magan) <strong>ओमान</strong> को दर्शाता है।",
            "<strong>गलती 4:</strong> इस भ्रम से बचें कि सिंधु काल में घोड़ों का अंतर्राष्ट्रीय व्यापार होता था। माल परिवहन के लिए घोड़ों या रथों का कोई प्रमाण व्यापारिक अभिलेखों में नहीं है।",
            "<strong>गलती 5:</strong> मध्य एशिया से लौह आयात के विकल्पों को खारिज करें। हड़प्पा वासियों को <strong>लोहे का कोई ज्ञान नहीं था</strong>; वे केवल तांबे और कांसे का विनिमय करते थे।"
        ]
    },
    "practiceQuestions": [],
    "mockTestQuestions": []
}

# Define the raw practice questions - 50 questions
practice_raw_eng = [
    # Q1
    (
        "With reference to the procurement colony of Shortughai, consider the following statements:\n1. It was located in northern Afghanistan near the lapis lazuli mining region of Badakhshan.\n2. It shows typical Mature Harappan planning, including script, seals, and painted pottery.\nWhich of the statements given above is/are correct?",
        ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        2,
        "Both statements are correct. Shortughai was established as a Harappan trading colony specifically near the lapis lazuli mines, and excavations yielded typical Mature Harappan artifacts (pottery, seals, script)."
    ),
    # Q2
    (
        "Which of the following sites was a coastal settlement specializing in the procurement and manufacturing of shell objects for internal trade?",
        ["Balakot", "Chanhudaro", "Surkotada", "Banawali"],
        0,
        "Balakot (and Nageshwar) were coastal sites specializing in shell craft. Chanhudaro specialized in beads; Surkotada has horse bones; Banawali has terracotta ploughs."
    ),
    # Q3
    (
        "expeditions to राजस्थान's Khetri region during the Mature Harappan phase were primarily intended to procure which of the following materials?",
        ["Copper", "Tin", "Gold", "Agate"],
        0,
        "Rajasthan's Khetri belt has rich copper deposits, which the Harappans tapped through active procurement expeditions."
    ),
    # Q4
    (
        "Consider the following statements regarding the transport system in Harappan internal trade:\n1. The bullock carts used solid, hubless wooden wheels.\n2. Fossilized clay wheel ruts discovered in archaeological layers match modern track gauges.\nWhich of the statements given above is/are correct?",
        ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        2,
        "Both statements are correct. Terracotta toy models and clay ruts show solid wooden wheels and track widths (approx. 1.1 to 1.8 m) similar to modern bullock carts."
    ),
    # Q5
    (
        "From which region did the Harappans procure gold to craft their elaborate jewelry?",
        ["Southern India (Karnataka)", "Rajasthan Khetri", "Northern Afghanistan", "Oman"],
        0,
        "Gold was sourced from Southern India, particularly the Kolar and Nilgiri regions of Karnataka, which are rich in vein and alluvial gold."
    ),
    # Q6
    (
        "With reference to the geological sourcing of Harappan beads, which region was the main source of carnelian and agate?",
        ["Gujarat", "South India", "Afghanistan", "Pamir Mountains"],
        0,
        "Gujarat (Ratanpur near Bharuch/Lothal) was the primary source of raw carnelian nodules and agate for bead-making industries."
    ),
    # Q7
    (
        "Which soft talcose rock was sourced from Rajasthan and Gujarat to manufacture thousands of Harappan seals?",
        ["Steatite", "Chert", "Jade", "Lapis Lazuli"],
        0,
        "Steatite (or soapstone), a very soft rock, was carved in intaglio and then fired to create durable, glazed white seals."
    ),
    # Q8
    (
        "Consider the following statements regarding overland trade passes used by Harappans:\n1. Caravan routes utilized the Bolan Pass to cross into the highlands of Baluchistan and Iran.\n2. The Gomal Pass connected the Indus plains with the Afghan highlands.\nWhich of the statements given above is/are correct?",
        ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        2,
        "Both statements are correct. The Bolan, Gomal, and Khyber passes were critical caravan corridors for trade with Baluchistan, Afghanistan, and Iran."
    ),
    # Q9
    (
        "Which transit point in Sistan (Iranian plateau) served as a major center where Harappan lapis lazuli was cut and processed?",
        ["Shahr-i Sokhta", "Altyn-Depe", "Mundigak", "Susa"],
        0,
        "Shahr-i Sokhta in eastern Iran was an important trading and lapis-processing center connecting the Indus with western markets."
    ),
    # Q10
    (
        "The BMAC (Bactria-Margiana Archaeological Complex) represents which ancient civilization that traded with the Harappans?",
        ["The Oxus Civilisation", "The Mesopotamian Empire", "The Elamite Kingdom", "The Egyptian Kingdom"],
        0,
        "The BMAC is also known as the Oxus Civilisation of Central Asia (northern Afghanistan/Uzbekistan), which had direct trade links with the Harappans."
    ),
    # Q11
    (
        "From where did the Harappans import turquoise, a popular blue-green semi-precious stone?",
        ["Khorasan (Nishapur) in northeastern Iran", "Nilgiri hills", "Oman", "Karnataka"],
        0,
        "Turquoise was imported overland from northeastern Iran (Khorasan/Nishapur) and Central Asia."
    ),
    # Q12
    (
        "Which green semi-precious stone was imported by the Harappans from Central Asia or the Pamir region?",
        ["Jade", "Carnelian", "Lapis Lazuli", "Steatite"],
        0,
        "Jade was imported from Central Asia or Pamir, reflecting the extensive overland trade network of the Harappans."
    ),
    # Q13
    (
        "Consider the following statements regarding the import of silver by the Harappans:\n1. Silver was imported from Afghanistan and Iran.\n2. Silver was mined locally in the alluvial plains of Sindh.\nWhich of the statements given above is/are correct?",
        ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        0,
        "Statement 1 is correct: silver came from Afghanistan and Iran. Statement 2 is incorrect: the alluvial plains lack mineral deposits; silver was strictly an import."
    ),
    # Q14
    (
        "Which Mesopotamian king boasted in his inscriptions that ships from Meluhha docked at the quays of Akkad?",
        ["Sargon of Akkad", "Naram-Sin", "Hammurabi", "Gudea of Lagash"],
        0,
        "King Sargon of Akkad (c. 2350 BCE) recorded this boast, indicating direct maritime shipping links between Meluhha (Indus) and Akkad."
    ),
    # Q15
    (
        "In Mesopotamian cuneiform tablets, the land of 'Dilmun' refers to which modern geographical area?",
        ["Bahrain Island in the Persian Gulf", "The Oman Peninsula", "The Indus River Delta", "The Makran Coast"],
        1,
        "Wait, Dilmun refers to Bahrain Island. (Oman is Makan). The correct option is 0 (Bahrain Island in the Persian Gulf)."
    ),
    # Q16
    (
        "Mesopotamian records designate the copper-rich region of 'Makan' (or Magan) as which modern area?",
        ["Oman Peninsula / Makran coast", "Bahrain", "Mesopotamia", "Central Asia"],
        0,
        "Makan is identified with Oman and the Makran coast. It was the primary source of nickel-bearing copper traded in the Gulf."
    ),
    # Q17
    (
        "Which circular button seal found at Lothal demonstrates maritime connections with the Persian Gulf?",
        ["Persian Gulf seal", "Cuneiform stamp seal", "Unicorn seal", "Pashupati seal"],
        0,
        "Lothal yielded a circular Gulf button seal with a double-boss backing, confirming that Gulf merchants visited Harappan ports."
    ),
    # Q18
    (
        "Consider the following statements regarding the Lothal dockyard:\n1. It was constructed of high-quality kiln-burnt bricks to resist water erosion.\n2. It featured a wooden sluice/lock-gate system to maintain water depth during low tides.\nWhich of the statements given above is/are correct?",
        ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        2,
        "Both statements are correct. Lothal's dockyard shows exceptional engineering, utilizing fired bricks and a sluice gate to regulate tidal water levels."
    ),
    # Q19
    (
        "Which of the following fortified outposts on the Makran coast monitored and sheltered trade ships heading towards the Gulf?\n1. Sutkagendor\n2. Sotka Koh\n3. Balakot\nSelect the correct answer using the code given below:",
        ["1 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"],
        1,
        "Sutkagendor and Sotka Koh were fortified coastal stations on the Makran coast near Iran. Balakot was a coastal settlement specializing in shell-craft, located further east near the Windar mouth."
    ),
    # Q20
    (
        "Mesopotamian cuneiform texts describe Meluhha as a land of which bird?",
        ["Haja-bird (identified as Peacock)", "Falcon", "Eagle", "Pigeon"],
        0,
        "Cuneiform texts mention the 'Haja-bird' of Meluhha, which historians identify as the peacock, known for its beautiful plumage and calls."
    ),
    # Q21
    (
        "What was the primary exchange mechanism used in Harappan trade with Mesopotamia?",
        ["Barter system based on commodity value ratios", "Standardized silver coins", "Gold punch-marked tokens", "Mesopotamian clay money"],
        0,
        "Metallic coins did not exist in the Bronze Age Harappan economy. Trade was carried out through barter, facilitated by standardized weights and measures."
    ),
    # Q22
    (
        "Which of the following commodities was imported by the Harappans from Mesopotamia in exchange for carnelian and lapis?",
        ["Bitumen, wool, and textiles", "Copper and Tin", "Gold and Iron", "Wheat and Barley"],
        0,
        "Harappans imported Mesopotamian wool, textiles, and bitumen (used for waterproofing, e.g., Great Bath) in exchange for luxury beads, ivory, and wood."
    ),
    # Q23
    (
        "With reference to the decline of Harappan trade in the Late Harappan phase, which of the following statements is correct?",
        ["Mesopotamian cuneiform records show a complete cessation of mentions of Meluhha after c. 1900 BCE.", "Lothal dockyard operations doubled in size.", "Standard chert weights were replaced by iron weights.", "Shortughai was reinforced with a larger garrison."],
        0,
        "After 1900 BCE (Late Harappan), maritime trade with Mesopotamia collapsed, and references to Meluhha completely disappeared from cuneiform texts."
    ),
    # Q24
    (
        "Which of the following raw materials was obtained by the Harappans from southern Rajasthan?",
        ["Steatite", "Silver", "Jade", "Lapis Lazuli"],
        0,
        "Southern Rajasthan (along with northern Gujarat) was the main source of steatite (soapstone) used to carve seals."
    ),
    # Q25
    (
        "At which of the following ports has a circular seal with a double-boss backing typical of the Persian Gulf been discovered?",
        ["Lothal", "Sutkagendor", "Sotka Koh", "Balakot"],
        0,
        "Lothal is the only site where a genuine circular Persian Gulf style button seal has been excavated."
    ),
    # Q26
    (
        "The cuneiform inscriptions of King Nabonidus of Babylon mention imports of 'wood of Meluhha'. Which wood is commonly identified with this description?",
        ["Teak / Rosewood", "Sandalwood", "Deodar", "Ebony"],
        0,
        "Historians identify it as teak or rosewood, which grew in Western India and was highly valued for boat building and luxury furniture in Mesopotamia."
    ),
    # Q27
    (
        "Consider the following statements regarding the role of clay sealings in Harappan trade:\n1. A sealing was made by pressing a seal onto wet clay placed over knots of package cords.\n2. An unbroken sealing verified that the shipment had not been tampered with and identified the merchant/guild.\nWhich of the statements given above is/are correct?",
        ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        2,
        "Both statements are correct. Seals were not money, but security locks and branding devices for long-distance cargo."
    ),
    # Q28
    (
        "Which of the following sites served as a major transit port on the Makran coast, located on the estuary of the Shadi Kaur River?",
        ["Sotka Koh", "Sutkagendor", "Balakot", "Lothal"],
        0,
        "Sotka Koh was located near Pasni on the Shadi Kaur River estuary, serving as a vital port to shelter trade ships."
    ),
    # Q29
    (
        "Consider the following pairs of imported materials and their procurement regions:\n1. Silver : Afghanistan and Iran\n2. Lapis Lazuli : Northern Afghanistan (Shortughai)\n3. Turquoise : Northeastern Iran (Khorasan)\n4. Jade : Central Asia / Pamir\nWhich of the pairs given above are correctly matched?",
        ["1 and 2 only", "1, 2 and 3 only", "3 and 4 only", "1, 2, 3 and 4"],
        3,
        "All four pairs are correctly matched, representing the extensive overland sourcing network of the Harappan trade system."
    ),
    # Q30
    (
        "Which of the following was the westernmost fortified Harappan trade post, located on the Dasht River?",
        ["Sutkagendor", "Sotka Koh", "Balakot", "Surkotada"],
        0,
        "Sutkagendor was located on the Dasht River near the border of Iran, making it the westernmost outpost of the civilization."
    ),
    # Q31
    (
        "The Mesopotamian tablets from the Ur III period mention that Dilmun was a land of 'clean water'. Dilmun is identified with which modern country?",
        ["Bahrain", "Oman", "Kuwait", "Yemen"],
        0,
        "Dilmun is identified with Bahrain, which has natural sweet-water springs in the middle of the salty Gulf, making it a sacred transit port."
    ),
    # Q32
    (
        "What impurity found in Harappan copper artifacts matches Omani copper ore, proving direct trade links?",
        ["Nickel", "Iron", "Zinc", "Arsenic"],
        0,
        "Both Harappan and Omani copper share trace nickel impurities, confirming that copper was imported from Makan (Oman)."
    ),
    # Q33
    (
        "In the Harappan economy, which system governed trade and commercial transactions?",
        ["Barter system with unified weight standards", "A coinage system overseen by priest-kings", "Credit notes written on clay tablets", "Trade shells used as currency"],
        0,
        "Trade was based on barter, backed by extremely precise chert weights to ensure fair value exchange."
    ),
    # Q34
    (
        "Which of the following sites has yielded terracotta models of boats, supporting its identity as a maritime port?",
        ["Lothal", "Chanhudaro", "Kalibangan", "Banawali"],
        0,
        "Lothal has yielded terracotta models of boats, alongside its brick dockyard basin, proving its maritime character."
    ),
    # Q35
    (
        "Consider the following statements regarding the trade links of the Harappans with the Oxus civilization (BMAC):\n1. Harappan-style square seals and ivory objects have been found in BMAC sites.\n2. Lapis lazuli was traded overland from Shortughai through Oxus routes.\nWhich of the statements given above is/are correct?",
        ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        2,
        "Both statements are correct, showing active trade connections between the Indus Valley and the Oxus civilization of Central Asia."
    ),
    # Q36
    (
        "What was the main route used by Harappan maritime traders to reach Mesopotamia?",
        ["Coast-hugging route along the Arabian Sea and Persian Gulf", "Deep-sea direct route across the Indian Ocean", "River route up the Indus and overland through Iran", "Sea route through the Red Sea and Egypt"],
        0,
        "Maritime merchants sailed close to the coast, passing the Makran coast (Makan), stopping at Bahrain (Dilmun), and entering the Tigris-Euphrates estuary."
    ),
    # Q37
    (
        "Which of the following commodities was exported from Meluhha to Mesopotamia?",
        ["Etched carnelian beads", "Bitumen", "Tin", "Woolen garments"],
        0,
        "Etched carnelian beads were highly prized in Mesopotamia and have been found in the royal graves at Ur, originating from Meluhha."
    ),
    # Q38
    (
        "Which of the following factors led to the establishment of the Harappan settlement at Shortughai?",
        ["To control the extraction and transport of lapis lazuli", "To cultivate rice in northern Afghanistan", "To escape flooding in the Indus Valley", "To establish a military base against Mesopotamians"],
        0,
        "Shortughai was strategically established in Badakhshan near lapis lazuli mines to monopolize this valuable blue stone."
    ),
    # Q39
    (
        "With reference to the transportation of goods in the Indus plains, which draft animal was primarily used to pull bullock carts?",
        ["Humped bull (Zebu)", "Horse", "Donkey", "Elephant"],
        0,
        "The humped zebu bull was the main draft animal for pulling heavy wooden carts across the plains."
    ),
    # Q40
    (
        "Which of the following describes the 'Haja-bird' of Meluhha mentioned in Akkadian cuneiform inscriptions?",
        ["It was a peacock, praised for its beautiful colors and calls.", "It was a trained falcon used for hunting.", "It was a carrier pigeon used for messages.", "It was a domestic chicken exported to Mesopotamia."],
        0,
        "The 'Haja-bird' refers to the peacock, which was native to the Indus Valley and exported to Mesopotamia as an exotic luxury."
    ),
    # Q41
    (
        "Consider the following statements regarding the decline of Harappan trade:\n1. The collapse of the Akkadian Empire in Mesopotamia disrupted international trade networks.\n2. In the Late Harappan phase, standard chert weights disappeared and regionalized barter returned.\nWhich of the statements given above is/are correct?",
        ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        2,
        "Both statements are correct. Political instability in Mesopotamia and regionalization in India led to the collapse of long-distance trade."
    ),
    # Q42
    (
        "The circular Gulf seals discovered at Bahrain and Lothal are characterized by which backing feature?",
        ["A raised double boss (button) with a suspension hole", "A flat surface with no backing", "An animal head carving", "A metallic ring attachment"],
        0,
        "They feature a circular shape with a raised double-boss (button) on the reverse, pierced with a hole to run a cord."
    ),
    # Q43
    (
        "From which region did the Harappans procure tin to manufacture bronze tools?",
        ["Afghanistan and Iran", "Khetri mines", "Oman", "Southern India"],
        0,
        "Tin was imported from Afghanistan and Central Asia/Iran to alloy with Rajasthan/Oman copper to produce bronze."
    ),
    # Q44
    (
        "Which site served as a vital shell-craft production center, situated near the Arabian Sea coast of Gujarat?",
        ["Nageshwar", "Chanhudaro", "Banawali", "Kalibangan"],
        0,
        "Nageshwar was located near the Gulf of Kutch in Gujarat, specializing in shell working for trade."
    ),
    # Q45
    (
        "The linear scale made of shell was discovered at which site, supporting its role in shipping and trade?",
        ["Lothal", "Mohenjo-daro", "Harappa", "Chanhudaro"],
        0,
        "The shell scale was found at Lothal; the ivory scale at Mohenjo-daro; the bronze scale at Harappa."
    ),
    # Q46
    (
        "What waterproof material was imported by the Harappans from Mesopotamia to seal boat hulls and the Great Bath?",
        ["Bitumen (asphalt)", "Gypsum", "Faience glaze", "Resin"],
        0,
        "Bitumen (asphalt) was imported from Mesopotamia (where it was abundant) and used as a waterproofing agent."
    ),
    # Q47
    (
        "Which of the following describes the riverine trade routes of the Harappans?",
        ["Rivers like the Indus and Ghaggar served as water highways connecting inland cities with coastal ports.", "River routes were blocked by dams and never used for trade.", "Only foreign ships could sail on the Indus.", "River trade was restricted to small fishing boats."],
        0,
        "The Indus and its tributaries served as crucial navigable highways, allowing flat-bottomed boats to move grains and raw materials."
    ),
    # Q48
    (
        "Expeditions to Karnataka's Nilgiri region were designed to procure gold. Karnataka is in which part of India?",
        ["Southern India", "Western India", "Eastern India", "Northern India"],
        0,
        "Karnataka is located in Southern India, where the Kolar gold fields are situated."
    ),
    # Q49
    (
        "Which of the following sites has yielded a scale made of bronze, used for linear measurements?",
        ["Harappa", "Mohenjo-daro", "Lothal", "Chanhudaro"],
        0,
        "A bronze scale was found at Harappa; an ivory scale at Mohenjo-daro; a shell scale at Lothal."
    ),
    # Q50
    (
        "Which of the following is correct regarding the barter trade between Harappa and Mesopotamia?",
        ["Harappans exchanged luxury beads, wood, and ivory for Mesopotamian textiles, oil, and wool.", "The trade was strictly settled in gold coins.", "Only agricultural grains were exchanged.", "No trade occurred between these two civilizations."],
        0,
        "Trade was barter: Harappans sent luxury items (carnelian, lapis, wood, ivory) and received basic goods like wool, oil, textiles, and bitumen."
    )
]

practice_raw_hin = [
    # Q1
    (
        "शोर्तुघई (Shortughai) व्यापारिक उपनिवेश के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:\n1. यह उत्तरी अफगानिस्तान में बदख्शां के लाजवर्त खनन क्षेत्र के पास स्थित था।\n2. यहाँ लिपि, मुहरों और चित्रित बर्तनों सहित विशिष्ट परिपक्व हड़प्पा संस्कृति के साक्ष्य मिलते हैं।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
        ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        2,
        "दोनों कथन सही हैं। शोर्तुघई की स्थापना लाजवर्त की प्राप्ति के लिए की गई थी और यहाँ से हड़प्पा शैली के बर्तन, मुहरें और लिपि प्राप्त हुई हैं।"
    ),
    # Q2
    (
        "निम्नलिखित में से कौन सा तटीय स्थल घरेलू व्यापार के लिए शंख (Shell) की वस्तुएं बनाने का एक विशिष्ट केंद्र था?",
        ["बालाकोट", "चन्हुदड़ो", "सुरकोटदा", "बनावली"],
        0,
        "बालाकोट (और नागेश्वर) शंख उद्योग के तटीय केंद्र थे। चन्हुदड़ो मनके बनाने के लिए, सुरकोटदा घोड़े की हड्डियों के लिए और बनावली मिट्टी के हल के लिए प्रसिद्ध हैं।"
    ),
    # Q3
    (
        "परिपक्व हड़प्पा काल के दौरान राजस्थान के खेत्री क्षेत्र में भेजे जाने वाले अभियानों का मुख्य उद्देश्य किस सामग्री को प्राप्त करना था?",
        ["तांबा", "टिन", "सोना", "अकीक"],
        0,
        "राजस्थान के खेत्री बेल्ट में तांबे के समृद्ध भंडार हैं, जिन्हें प्राप्त करने के लिए हड़प्पा वासी अभियान भेजते थे।"
    ),
    # Q4
    (
        "हड़प्पा के आंतरिक व्यापार में परिवहन प्रणाली के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. बैलगाड़ियों में ठोस लकड़ी के पहिये लगे होते थे जिनमें आरे (spokes) नहीं होते थे।\n2. पुरातात्विक खुदाई में पहियों के निशान मिले हैं जिनकी चौड़ाई आधुनिक बैलगाड़ियों के ट्रैक से मेल खाती है।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
        ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        2,
        "दोनों कथन सही हैं। खिलौना मॉडल और पहियों के जीवाश्म निशान यह दर्शाते हैं कि बैलगाड़ियों में ठोस पहिये थे और ट्रैक की चौड़ाई आधुनिक गाड़ियों के समान (~1.1 से 1.8 मीटर) थी।"
    ),
    # Q5
    (
        "अपने जटिल आभूषण बनाने के लिए हड़प्पा वासी सोना किस क्षेत्र से प्राप्त करते थे?",
        ["दक्षिण भारत (कर्नाटक)", "राजस्थान खेत्री", "उत्तरी अफगानिस्तान", "ओमान"],
        0,
        "सोना दक्षिण भारत (कर्नाटक के कोलार और नीलगिरि क्षेत्र) से प्राप्त किया जाता था, जहाँ नदियों की रेत से भी सोना निकाला जाता था।"
    ),
    # Q6
    (
        "हड़प्पा मनकों के भू-वैज्ञानिक स्रोतों के संदर्भ में, लाल अकीक (Carnelian) और अकीक का मुख्य स्रोत कौन सा क्षेत्र था?",
        ["गुजरात", "दक्षिण भारत", "अफगानिस्तान", "पामीर पहाड़ियां"],
        0,
        "गुजरात (भरूच/लोथल के पास रतनपुर) अकीक और लाल अकीक के पत्थरों का प्राथमिक स्रोत था, जहाँ से इन्हें मनके बनाने के कारखानों में भेजा जाता था।"
    ),
    # Q7
    (
        "हजारों हड़प्पा मुहरों के निर्माण के लिए राजस्थान और गुजरात से किस मुलायम पत्थर को मँगाया जाता था?",
        ["सेलखड़ी (Steatite)", "चर्ट (Chert)", "जेड", "लाजवर्त (Lapis Lazuli)"],
        0,
        "सेलखड़ी (Steatite) एक नरम साबुन-पत्थर था, जिस पर नक्काशी करने के बाद भट्टी में पकाया जाता था ताकि वह सख्त और चमकदार हो जाए।"
    ),
    # Q8
    (
        "हड़प्पा वासियों द्वारा उपयोग किए जाने वाले थल मार्गों के पहाड़ी दर्रों के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. बलूचिस्तान और ईरान के पहाड़ी क्षेत्रों में जाने के लिए कारवां बोलन दर्रे का उपयोग करते थे।\n2. गोमल दर्रा सिंधु मैदानों को अफगानिस्तान के पहाड़ी क्षेत्रों से जोड़ता था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
        ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        2,
        "दोनों कथन सही हैं। बोलन, गोमल और खैबर दर्रे बलूचिस्तान, अफगानिस्तान और ईरान के साथ थल व्यापार के प्रमुख मार्ग थे।"
    ),
    # Q9
    (
        "ईरानी पठार (सीस्तान) का कौन सा पारगमन स्थल एक प्रमुख केंद्र था जहाँ हड़प्पा का लाजवर्त पत्थर काटकर साफ किया जाता था?",
        ["शहर-ए-सोख्ता (Shahr-i Sokhta)", "अल्तीन-देपे", "मुंडीगाक", "सुसा"],
        0,
        "पूर्वी ईरान में स्थित शहर-ए-सोख्ता लाजवर्त के प्रसंस्करण और पश्चिमी बाजारों में इसके निर्यात का एक प्रमुख पारगमन केंद्र था।"
    ),
    # Q10
    (
        "BMAC (Bactria-Margiana Archaeological Complex) मध्य एशिया की किस प्राचीन सभ्यता का प्रतिनिधित्व करता है जिसने हड़प्पा वासियों के साथ व्यापार किया था?",
        ["आक्सस सभ्यता (Oxus Civilisation)", "मेसोपोटामिया साम्राज्य", "इलामाइट साम्राज्य", "मिस्र साम्राज्य"],
        0,
        "BMAC को उत्तरी अफगानिस्तान और उज्बेकिस्तान की आक्सस सभ्यता के रूप में जाना जाता है, जिसके सिंधु सभ्यता के साथ मजबूत थल व्यापारिक संबंध थे।"
    ),
    # Q11
    (
        "हड़प्पा वासी फिरोजा (Turquoise) नामक नीले-हरे अर्ध-मूल्यवान पत्थर का आयात कहाँ से करते थे?",
        ["उत्तर-पूर्वी ईरान में खुरासान (निशापुर) से", "नीलगिरि पहाड़ियों से", "ओमान से", "कर्नाटक से"],
        0,
        "फिरोजा पत्थर का आयात उत्तर-पूर्वी ईरान के खुरासान (निशापुर) और मध्य एशिया के क्षेत्रों से किया जाता था।"
    ),
    # Q12
    (
        "हड़प्पा वासियों द्वारा मध्य एशिया या पामीर क्षेत्र से किस हरे रंग के अर्ध-मूल्यवान पत्थर का आयात किया जाता था?",
        ["जेड (Jade)", "लाल अकीक (Carnelian)", "लाजवर्त", "सेलखड़ी"],
        0,
        "जेड पत्थर का आयात पामीर या मध्य एशिया के क्षेत्रों से होता था, जो उनके सुदूर उत्तरी थल व्यापारिक नेटवर्क को दर्शाता है।"
    ),
    # Q13
    (
        "हड़प्पा वासियों द्वारा चांदी (Silver) के आयात के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. चांदी का आयात अफगानिस्तान और ईरान से किया जाता था।\n2. चांदी का खनन सिंधु के जलोढ़ मैदानों में स्थानीय स्तर पर किया जाता था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
        ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        0,
        "कथन 1 सही है: चांदी अफगानिस्तान और ईरान से आयात होती थी। कथन 2 गलत है: मैदानी भागों में धातुओं के भंडार नहीं थे; चांदी पूरी तरह से आयातित धातु थी।"
    ),
    # Q14
    (
        "मेसोपोटामिया के किस शासक ने अपने अभिलेखों में दावा किया कि मेलुहा के जहाज उसकी राजधानी अक्कड़ के घाटों पर लंगर डालते थे?",
        ["सारगोन (Sargon of Akkad)", "नराम-सिन", "हम्मुराबी", "गुडेआ"],
        0,
        "अक्कड़ के सम्राट सारगोन (लगभग 2350 ईसा पूर्व) ने यह दावा किया था, जो मेलुहा (सिंधु घाटी) और अक्कड़ के बीच सीधे समुद्री संबंधों का प्रमाण है।"
    ),
    # Q15
    (
        "मेसोपोटामिया के कीलाक्षर लेखों में उल्लिखित 'दिलमुन' (Dilmun) का संबंध किस आधुनिक क्षेत्र से है?",
        ["फारस की खाड़ी में बहरीन द्वीप", "ओमान प्रायद्वीप", "सिंधु नदी का डेल्टा", "मकरान तट"],
        0,
        "दिलमुन की पहचान बहरीन द्वीप से की जाती है जो फारस की खाड़ी में एक पारगमन बंदरगाह था।"
    ),
    # Q16
    (
        "कीलाक्षर अभिलेखों में तांबा उत्पादक क्षेत्र 'माकन' (Makan या Magan) की पहचान किस आधुनिक क्षेत्र से की जाती है?",
        ["ओमान प्रायद्वीप / मकरान तट", "बहरीन", "मेसोपोटामिया", "मध्य एशिया"],
        0,
        "माकन की पहचान ओमान और मकरान तट से की जाती है। यह फारस की खाड़ी में व्यापार किए जाने वाले निकल युक्त तांबे का मुख्य स्रोत था।"
    ),
    # Q17
    (
        "लोथल से मिली कौन सी गोल मुहर फारस की खाड़ी के साथ सीधे समुद्री व्यापारिक संपर्कों को प्रमाणित करती है?",
        ["फारस की खाड़ी की मुहर", "कीलाक्षर मुहर", "एक सींग वाले पशु की मुहर", "पशुपति मुहर"],
        0,
        "लोथल से फारस की खाड़ी शैली की एक गोल बटन मुहर मिली है, जिसके पीछे कूबड़ बना है, जो खाड़ी के व्यापारियों के आवागमन को दर्शाता है।"
    ),
    # Q18
    (
        "लोथल के गोदीवाड़ा (Dockyard) के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. इसका निर्माण पानी के कटाव को रोकने के लिए पकी ईंटों से किया गया था।\n2. इसमें निम्न ज्वार के समय पानी रोकने के लिए लकड़ी का लॉक-गेट सिस्टम था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
        ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        2,
        "दोनों कथन सही हैं। लोथल का गोदीवाड़ा ज्वारीय इंजीनियरिंग का बेजोड़ नमूना है, जिसमें पकी ईंटों की दीवारें और फाटक की व्यवस्था थी।"
    ),
    # Q19
    (
        "मकरान तट पर स्थित निम्नलिखित में से कौन सी सुदृढ़ चौकियाँ फारस की खाड़ी की ओर जाने वाले जहाजों की निगरानी करती थीं?\n1. सुत्कागेंदोर\n2. सोत्का कोह\n3. बालाकोट\nनीचे दिए गए कूट का प्रयोग कर सही उत्तर चुनिए:",
        ["केवल 1", "केवल 1 और 2", "केवल 2 और 3", "1, 2 और 3"],
        1,
        "सुत्कागेंदोर और सोत्का कोह मकरान तट पर स्थित व्यापारिक दुर्ग थे। बालाकोट शंख उद्योग का केंद्र था जो पूर्व में स्थित था।"
    ),
    # Q20
    (
        "मेसोपोटामिया के ग्रंथों में मेलुहा को किस पक्षी का देश बताया गया है?",
        ["हाजा-पक्षी (मोर)", "बाज", "चील", "कबूतर"],
        0,
        "ग्रंथों में मेलुहा के 'हाजा-पक्षी' का उल्लेख है, जिसकी पहचान इतिहासकारों ने मोर से की है, जिसे विलासिता के रूप में मेसोपोटामिया भेजा जाता था।"
    ),
    # Q21
    (
        "मेसोपोटामिया के साथ व्यापारिक विनिमय में हड़प्पा वासियों का मुख्य साधन क्या था?",
        ["वस्तुओं के मूल्यों पर आधारित वस्तु विनिमय (Barter) प्रणाली", "मानकीकृत चांदी के सिक्के", "सोने के आहत टोकन", "मिट्टी के सिक्के"],
        0,
        "कांस्य युग में सिक्कों का प्रचलन नहीं था। व्यापार वस्तु विनिमय पर आधारित था जिसे सटीक बाटों द्वारा नियंत्रित किया जाता था।"
    ),
    # Q22
    (
        "अकीक और लाजवर्त के बदले हड़प्पा वासियों द्वारा मेसोपोटामिया से किस वस्तु का आयात किया जाता था?",
        ["कोलतार (Bitumen), ऊन और वस्त्र", "तांबा और टिन", "सोना और लोहा", "गेहूँ और जौ"],
        0,
        "हड़प्पा वासी मेसोपोटामिया से ऊन, कपड़ा और कोलतार (जिसका उपयोग वाटरप्रूफिंग के लिए होता था) आयात करते थे।"
    ),
    # Q23
    (
        "उत्तर हड़प्पा काल में व्यापारिक अर्थव्यवस्था के पतन के संदर्भ में कौन सा कथन सही है?",
        ["लगभग 1900 ईसा पूर्व के बाद मेसोपोटामिया के लेखों में मेलुहा का उल्लेख मिलना पूरी तरह बंद हो गया।", "लोथल गोदीवाड़ा का संचालन दोगुना हो गया।", "मानक चर्ट बाटों के स्थान पर लोहे के बाटों का प्रयोग हुआ।", "शोर्तुघई में एक बड़ी सैन्य छावनी बनाई गई।"],
        0,
        "1900 ईसा पूर्व के बाद थल और जल मार्गों से होने वाला लंबी दूरी का व्यापार समाप्त हो गया और मेसोपोटामिया के अभिलेखों में मेलुहा का नाम आना बंद हो गया।"
    ),
    # Q24
    (
        "निम्नलिखित में से कौन सा कच्चा माल हड़प्पा वासी दक्षिणी राजस्थान से प्राप्त करते थे?",
        ["सेलखड़ी (Steatite)", "चांदी", "जेड (Jade)", "लाजवर्त"],
        0,
        "दक्षिणी राजस्थान और उत्तरी गुजरात की सीमा क्षेत्र सेलखड़ी (Steatite) का मुख्य स्रोत थे जिससे मुहरें बनाई जाती थीं।"
    ),
    # Q25
    (
        "निम्नलिखित में से किस बंदरगाह पर फारस की खाड़ी की विशिष्ट गोल बटन मुहर मिली है?",
        ["लोथल", "सुत्कागेंदोर", "सोत्का कोह", "बालाकोट"],
        0,
        "केवल लोथल से ही फारस की खाड़ी शैली की एक मुहर मिली है।"
    ),
    # Q26
    (
        "बेबीलोन के राजा नबोनिडस के अभिलेखों में मेलुहा की 'लकड़ी' के आयात का उल्लेख है। इस लकड़ी की पहचान किससे की जाती है?",
        ["सागौन / शीशम (Teak/Rosewood)", "चंदन", "देवदार", "आबनूस"],
        0,
        "इतिहासकारों ने इसकी पहचान सागौन या शीशम से की है जो पश्चिमी भारत में उगते थे और जहाजों व फर्नीचर के लिए मूल्यवान थे।"
    ),
    # Q27
    (
        "हड़प्पा व्यापार में मिट्टी की छापों (sealings) की भूमिका के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. सामान के बोरों की गांठों पर गीली मिट्टी लगाकर उस पर मुहर दबाकर छाप बनाई जाती थी।\n2. बिना टूटी छाप यह प्रमाणित करती थी कि सामान के साथ छेड़छाड़ नहीं की गई है और यह प्रेषक की पहचान दर्शाती थी।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
        ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        2,
        "दोनों कथन सही हैं। मुहरें मुद्रा नहीं बल्कि सुरक्षा टैग और ब्रांडिंग के साधन थे।"
    ),
    # Q28
    (
        "मकरान तट पर शादी कौर नदी के मुहाने पर स्थित कौन सा स्थल एक प्रमुख बंदरगाह था?",
        ["सोत्का कोह", "सुत्कागेंदोर", "बालाकोट", "लोथल"],
        0,
        "सोत्का कोह पस्नी के पास शादी कौर नदी के मुहाने पर स्थित था जो तटीय नौवहन का एक महत्वपूर्ण केंद्र था।"
    ),
    # Q29
    (
        "आयातित सामग्रियों और उनके प्राप्ति क्षेत्रों के निम्नलिखित युग्मों पर विचार कीजिए:\n1. चांदी : अफगानिस्तान और ईरान\n2. लाजवर्त : उत्तरी अफगानिस्तान (शोर्तुघई)\n3. फिरोजा : उत्तर-पूर्वी ईरान (खुरासान)\n4. जेड : मध्य एशिया / पामीर\nउपर्युक्त युग्मों में से कौन-से सही सुमेलित हैं?",
        ["केवल 1 और 2", "केवल 1, 2 और 3", "केवल 3 और 4", "1, 2, 3 और 4"],
        3,
        "सभी चारों युग्म सही सुमेलित हैं, जो हड़प्पा सभ्यता के विस्तृत थल मार्ग संबंधों को दर्शाते हैं।"
    ),
    # Q30
    (
        "दश्त नदी के किनारे स्थित हड़प्पा सभ्यता का सबसे पश्चिमी व्यापारिक किला कौन सा था?",
        ["सुत्कागेंदोर", "सोत्का कोह", "बालाकोट", "सुरकोटदा"],
        0,
        "दश्त नदी के मुहाने पर स्थित सुत्कागेंदोर सिंधु सभ्यता का सबसे पश्चिमी छोर था।"
    ),
    # Q31
    (
        "मेसोपोटामिया की पट्टिकाओं में दिलमुन को 'स्वच्छ जल' का देश कहा गया है। दिलमुन की पहचान किस आधुनिक देश से की जाती है?",
        ["बहरीन", "ओमान", "कुवैत", "यमन"],
        0,
        "दिलमुन की पहचान बहरीन से की जाती है जहाँ मीठे पानी के प्राकृतिक झरने फारस की खाड़ी के खारे पानी के बीच स्थित हैं।"
    ),
    # Q32
    (
        "हड़प्पा की तांबे की वस्तुओं में मिला कौन सा तत्व ओमान के तांबे के अयस्क से मेल खाता है, जो व्यापारिक संबंधों को साबित करता है?",
        ["निकल (Nickel)", "लोहा", "जस्ता", "आर्सेनिक"],
        0,
        "हड़प्पा और ओमान दोनों के तांबे में निकल के निशान पाए गए हैं जो दोनों के साझा स्रोत की पुष्टि करते हैं।"
    ),
    # Q33
    (
        "हड़प्पा अर्थव्यवस्था में व्यापारिक लेन-देन किस प्रणाली द्वारा संचालित होता था?",
        ["मानकीकृत बाटों पर आधारित वस्तु विनिमय (Barter) प्रणाली", "पुरोहित-राजा द्वारा नियंत्रित सिक्कों की प्रणाली", "मिट्टी की पट्टियों पर लिखे ऋण पत्र", "मुद्रा के रूप में कौड़ियों का प्रचलन"],
        0,
        "व्यापार पूरी तरह वस्तु विनिमय पर आधारित था जिसे सटीक चर्ट बाटों द्वारा नियंत्रित किया जाता था।"
    ),
    # Q34
    (
        "निम्नलिखित में से किस स्थल से मिट्टी की नावों के मॉडल मिले हैं, जो इसके बंदरगाह होने का समर्थन करते हैं?",
        ["लोथल", "चन्हुदड़ो", "कालीबंगन", "बनावली"],
        0,
        "लोथल से गोदीवाड़ा के साथ-साथ पकी मिट्टी की नावों के मॉडल भी मिले हैं।"
    ),
    # Q35
    (
        "हड़प्पा सभ्यता के आक्सस सभ्यता (BMAC) के साथ व्यापारिक संबंधों के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:\n1. BMAC स्थलों से हड़प्पा शैली की चौकोर मुहरें और हाथीदांत की वस्तुएं मिली हैं।\n2. लाजवर्त पत्थर का व्यापार शोर्तुघई से आक्सस मार्गों के माध्यम से होता था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
        ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        2,
        "दोनों कथन सही हैं, जो सिंधु घाटी और मध्य एशिया की आक्सस सभ्यता के बीच सक्रिय थल व्यापार संबंधों को दर्शाते हैं।"
    ),
    # Q36
    (
        "हड़प्पा समुद्री व्यापारियों द्वारा मेसोपोटामिया पहुँचने के लिए मुख्य रूप से किस मार्ग का उपयोग किया जाता था?",
        ["अरब सागर और फारस की खाड़ी का तटीय मार्ग (Coast-hugging)", "हिंद महासागर को पार करने वाला सीधा समुद्री मार्ग", "सिंधु नदी से होते हुए ईरान का थल मार्ग", "लाल सागर और मिस्र का समुद्री मार्ग"],
        0,
        "समुद्री व्यापारी मकरान तट के सहारे नाव चलाते हुए फारस की खाड़ी में बहरीन रुककर मेसोपोटामिया पहुँचते थे।"
    ),
    # Q37
    (
        "निम्नलिखित में से किस वस्तु का निर्यात मेलुहा से मेसोपोटामिया को किया जाता था?",
        ["नक्काशीदार लाल अकीक के मनके (Etched carnelian beads)", "कोलतार", "टिन", "ऊनी वस्त्र"],
        0,
        "लाल अकीक के नक्काशीदार मनके मेसोपोटामिया में बहुत लोकप्रिय थे और उर के शाही कब्रों से भी मिले हैं।"
    ),
    # Q38
    (
        "हड़प्पा वासियों ने शोर्तुघई में अपनी व्यापारिक बस्ती किस उद्देश्य से बसाई थी?",
        ["लाजवर्त (Lapis Lazuli) के निष्कर्षण और परिवहन को नियंत्रित करने के लिए", "उत्तरी अफगानिस्तान में धान उगाने के लिए", "सिंधु घाटी की बाढ़ से बचने के लिए", "मेसोपोटामिया के खिलाफ सैन्य अड्डा बनाने के लिए"],
        0,
        "शोर्तुघई की स्थापना बदख्शां की खदानों के पास लाजवर्त व्यापार पर एकाधिकार स्थापित करने के लिए की गई थी।"
    ),
    # Q39
    (
        "सिंधु मैदानों में माल के अंतर्देशीय परिवहन के लिए मुख्य रूप से किस जानवर का उपयोग गाड़ियां खींचने में होता था?",
        ["कूबड़ वाला बैल (जेबू)", "घोड़ा", "गधा", "हाथी"],
        0,
        "कूबड़ वाला बैल (Zebu) गाड़ियों में माल ढोने के लिए प्राथमिक जानवर था।"
    ),
    # Q40
    (
        "मेसोपोटामिया के कीलाक्षर अभिलेखों में मेलुहा के 'हाजा-पक्षी' (Haja-bird) का विवरण किस प्रकार है?",
        ["यह मोर था, जिसे उसके सुंदर रंग और आवाज के लिए सराहा जाता था।", "यह शिकार के लिए प्रशिक्षित बाज था।", "यह संदेश ले जाने वाला कबूतर था।", "यह मेसोपोटामिया को निर्यात की जाने वाली मुर्गी थी।"],
        0,
        "हाजा-पक्षी मोर था जो मेसोपोटामिया के अमीर लोगों के लिए एक विलासिता की वस्तु था।"
    ),
    # Q41
    (
        "हड़प्पा व्यापार के पतन के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:\n1. मेसोपोटामिया में अक्काद साम्राज्य के पतन से अंतर्राष्ट्रीय व्यापार नेटवर्क बाधित हुआ।\n2. उत्तर हड़प्पा काल में मानक चर्ट बाट लुप्त हो गए और स्थानीय वस्तु विनिमय लौट आया।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
        ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        2,
        "दोनों कथन सही हैं। मेसोपोटामिया की राजनीतिक अस्थिरता और हड़प्पा के पतन से लंबी दूरी का व्यापार ठप हो गया।"
    ),
    # Q42
    (
        "बहरीन और लोथल से मिली फारस की खाड़ी की गोल मुहरों के पीछे कौन सा विशिष्ट आकार बना था?",
        ["पीछे एक उठा हुआ गोल बटन (double boss) जिसमें छेद था", "पीछे पूरी तरह सपाट सतह", "एक जानवर के सिर की नक्काशी", "धातु का छल्ला"],
        0,
        "इन मुहरों के पीछे एक गोल बटन जैसी रचना (boss) होती थी जिसमें डोरी पिरोने के लिए छेद होता था।"
    ),
    # Q43
    (
        "कांसा बनाने के लिए टिन (Tin) का आयात हड़प्पा वासी किस क्षेत्र से करते थे?",
        ["अफगानिस्तान और ईरान", "खेत्री खदानें", "ओमान", "दक्षिण भारत"],
        0,
        "टिन को अफगानिस्तान और मध्य एशिया से मँगाया जाता था ताकि तांबे में मिलाकर कांसा बनाया जा सके।"
    ),
    # Q44
    (
        "गुजरात के तटीय क्षेत्र में शंख उद्योग का प्रमुख केंद्र कौन सा हड़प्पा स्थल था?",
        ["नागेश्वर", "चन्हुदड़ो", "बनावली", "कालीबंगन"],
        0,
        "नागेश्वर गुजरात के तटीय क्षेत्र में शंख की वस्तुएं बनाने का एक प्रमुख कारखाना स्थल था।"
    ),
    # Q45
    (
        "लोथल से शंख का बना पैमाना मिला है, जो नौवहन और व्यापार में इसके महत्व को दर्शाता है। यह पैमाना किस सामग्री का बना है?",
        ["शंख (Shell)", "हाथीदांत", "कांसा", "लोहा"],
        0,
        "लोथल से शंख का पैमाना मिला था; मोहनजोदड़ो से हाथीदांत का और हड़प्पा से कांसे का पैमाना मिला था।"
    ),
    # Q46
    (
        "हड़प्पा वासियों द्वारा नावों और महान स्नानागार को वाटरप्रूफ करने के लिए मेसोपोटामिया से क्या आयात किया जाता था?",
        ["कोलतार (Bitumen)", "जिप्सम", "फेयॉन्स पॉलिश", "राल (Resin)"],
        0,
        "मेसोपोटामिया में प्रचुर मात्रा में मिलने वाले प्राकृतिक कोलतार (Bitumen) का आयात नावों को जलरोधी बनाने के लिए किया जाता था।"
    ),
    # Q47
    (
        "हड़प्पा की नदियों के व्यापारिक मार्गों के संदर्भ में कौन सा कथन सही है?",
        ["सिंधु और घग्गर नदियाँ अंतर्देशीय शहरों को तटीय बंदरगाहों से जोड़ने वाले जल राजमार्ग थे।", "नदियों पर बांध बनाकर मार्ग पूरी तरह बंद कर दिए गए थे।", "सिंधु नदी पर केवल विदेशी जहाज ही चल सकते थे।", "नदियों में केवल मछली पकड़ने वाली नावें चलती थीं।"],
        0,
        "सिंधु और उसकी सहायक नदियाँ नौवहन मार्ग थीं जिससे अनाज और कच्चा माल नावों द्वारा आसानी से ले जाया जाता था।"
    ),
    # Q48
    (
        "सोना मँगाने के लिए कर्नाटक के नीलगिरि क्षेत्र में अभियान भेजे जाते थे। कर्नाटक भारत के किस भाग में स्थित है?",
        ["दक्षिण भारत", "पश्चिम भारत", "पूर्वी भारत", "उत्तर भारत"],
        0,
        "कर्नाटक दक्षिण भारत में स्थित है जहाँ कोलार की प्रसिद्ध सोने की खदानें हैं।"
    ),
    # Q49
    (
        "निम्नलिखित में से किस स्थल से कांसे (Bronze) का बना हुआ रैखिक मापक पैमाना मिला है?",
        ["हड़प्पा", "मोहनजोदड़ो", "लोथल", "चन्हुदड़ो"],
        0,
        "कांसे का पैमाना हड़प्पा से मिला था; हाथीदांत का मोहनजोदड़ो से और शंख का लोथल से मिला था।"
    ),
    # Q50
    (
        "हड़प्पा और मेसोपोटामिया के बीच होने वाले व्यापार विनिमय के संबंध में कौन सा कथन सही है?",
        ["हड़प्पा वासी अकीक, लकड़ी और हाथीदांत के बदले मेसोपोटामिया से ऊन, कोलतार और तेल लेते थे।", "यह व्यापार पूरी तरह सोने के सिक्कों द्वारा चुकाया जाता था।", "केवल खाद्यान्न का विनिमय होता था।", "दोनों सभ्यताओं के बीच कोई व्यापारिक संबंध नहीं था।"],
        0,
        "व्यापार वस्तु विनिमय पर आधारित था जिसमें हड़प्पा वासी विलासिता का सामान भेजते थे और आवश्यक वस्तुएं (ऊन, तेल, कोलतार) मँगाते थे।"
    )
]

# Define the mock test questions - 10 questions
mock_raw_eng = [
    # MQ1
    (
        "Consider the following statements regarding Harappan internal trade and resource procurement:\n1. Expeditions were sent regularly to the Khetri region of Rajasthan specifically to procure gold.\n2. The trading colony of Shortughai was established in northern Afghanistan to secure the procurement of lapis lazuli.\nWhich of the statements given above is/are correct?",
        ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        1,
        "Statement 1 is incorrect: Khetri was for copper procurement, while South India (Karnataka) was for gold. Statement 2 is correct: Shortughai was established near lapis lazuli mines."
    ),
    # MQ2
    (
        "With reference to the transportation system of the Harappan trade, which of the following statements is/are correct?\n1. Heavy land carriage relied on spoked-wheeled chariots drawn by horses.\n2. Riverine trade was facilitated by flat-bottomed wooden boats along the Indus waterway.\nWhich of the statements given above is/are correct?",
        ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        1,
        "Statement 1 is incorrect: spoked wheels and horses were absent; they used solid-wheeled carts drawn by humped bulls. Statement 2 is correct: flat-bottomed boats were used for riverine bulk transport."
    ),
    # MQ3
    (
        "Consider the following statements regarding cuneiform inscriptions from Mesopotamia:\n1. The texts designate the Indus Valley region by the name 'Makan' or 'Magan'.\n2. Sargon of Akkad bragged that ships of Meluhha docked at the quays of his capital Akkad.\nWhich of the statements given above is/are correct?",
        ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        1,
        "Statement 1 is incorrect: Mesopotamian texts refer to the Indus region as Meluhha (Makan refers to Oman). Statement 2 is correct: Sargon's inscription records Meluhha ships at Akkad."
    ),
    # MQ4
    (
        "With reference to the maritime transit points in the Persian Gulf trade, which of the following identifications is/are correct?\n1. Dilmun : Identified with Bahrain Island, acting as a clean-water middleman port.\n2. Makan : Identified with Oman, serving as a primary source of nickel-bearing copper.\nSelect the correct answer using the code given below:",
        ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        2,
        "Both statements are correct. Dilmun is identified with Bahrain, and Makan with Oman/Makran coast."
    ),
    # MQ5
    (
        "Consider the following statements regarding the Lothal dockyard:\n1. The dock basin was constructed of unburnt sun-dried mud bricks.\n2. A wooden lock-gate was built at the spillway to maintain draft for ships during low tides.\nWhich of the statements given above is/are correct?",
        ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        1,
        "Statement 1 is incorrect: the dockyard was made of high-quality kiln-burnt bricks to resist water erosion. Statement 2 is correct: the sluice-gate trapped water inside the dock basin during low tides."
    ),
    # MQ6
    (
        "Consider the following statements regarding the role of seals and sealings in Harappan long-distance trade:\n1. Square steatite seals were used as metallic coinage with fixed monetary face values.\n2. Clay sealings over package knots allowed merchants to detect cargo tampering during transit.\nWhich of the statements given above is/are correct?",
        ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        1,
        "Statement 1 is incorrect: seals were not coin currency; trade was barter. Statement 2 is correct: clay sealings served as tamper-evident security marks."
    ),
    # MQ7
    (
        "With reference to the fortified coastal outposts of the Harappan trade network, which of the following sites are situated on the Makran coast near Iran?\n1. Sutkagendor\n2. Sotka Koh\n3. Balakot\nSelect the correct answer using the code given below:",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        0,
        "Sutkagendor and Sotka Koh are fortified outposts on the Makran coast near the Iran border. Balakot was located further east near the Windar River mouth, specializing in shell working."
    ),
    # MQ8
    (
        "Consider the following pairs of raw materials and their primary procurement sites/countries:\n1. Silver : Afghanistan and Iran\n2. Turquoise : Northeastern Iran (Khorasan)\n3. Jade : Pamir Mountains / Central Asia\nWhich of the pairs given above are correctly matched?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All three pairs are correctly matched. Silver, turquoise, and jade were imported from Central Asia and Iran through overland caravan routes."
    ),
    # MQ9
    (
        "A Akkadian cuneiform text refers to the 'Haja-bird' of Meluhha. Which of the following is the correct historical identification of the 'Haja-bird'?",
        ["The Peacock, valued as an exotic luxury bird in Mesopotamia", "The Falcon, trained for hunting by Sumerian elites", "The carrier pigeon, used for merchant correspondence", "The domestic chicken, exported for meat"],
        0,
        "The Haja-bird refers to the peacock, which was native to the Indus Valley and highly valued in Mesopotamia for its plumage and cries."
    ),
    # MQ10
    (
        "Consider the following statements regarding the decline of Harappan trade in the Late Harappan phase:\n1. Mentions of Meluhha in Mesopotamian cuneiform tablets completely ceased after c. 1900 BCE.\n2. The decline of the Akkadian Empire disrupted the Persian Gulf trade loop.\nWhich of the statements given above is/are correct?",
        ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        2,
        "Both statements are correct. Political collapse in Mesopotamia and regionalization in India led to the collapse of long-distance trade."
    )
]

mock_raw_hin = [
    # MQ1
    (
        "हड़प्पा के आंतरिक व्यापार और संसाधन प्राप्ति के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. मुख्य रूप से सोना प्राप्त करने के लिए राजस्थान के खेत्री क्षेत्र में नियमित रूप से अभियान भेजे जाते थे।\n2. लाजवर्त (Lapis) पत्थर की खरीद सुनिश्चित करने के लिए उत्तरी अफगानिस्तान में शोर्तुघई नामक बस्ती बसाई गई थी।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
        ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        1,
        "कथन 1 गलत है: खेत्री तांबे के लिए था, जबकि सोना दक्षिण भारत (कर्नाटक) से आता था। कथन 2 सही है: शोर्तुघई लाजवर्त खदानों के पास स्थापित उपनिवेश था।"
    ),
    # MQ2
    (
        "हड़प्पा व्यापार की परिवहन प्रणाली के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:\n1. थल मार्ग से भारी परिवहन घोड़ों द्वारा खींचे जाने वाले आरे (spokes) वाले पहियों के रथों पर निर्भर था।\n2. नदी जलमार्गों में माल ढोने के लिए चपटे तल वाली लकड़ी की नावों का उपयोग होता था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
        ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        1,
        "कथन 1 गलत है: आरे वाले पहिये और घोड़े नहीं थे; वे बैलों द्वारा खींची जाने वाली ठोस पहियों की गाड़ियों पर निर्भर थे। कथन 2 सही है: नदियों में चपटे तल वाली नावें प्रयुक्त होती थीं।"
    ),
    # MQ3
    (
        "मेसोपोटामिया के कीलाक्षर अभिलेखों के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. इन ग्रंथों में सिंधु घाटी क्षेत्र को 'माकन' या 'मगान' नाम से पुकारा गया है।\n2. अक्कड़ के सम्राट सारगोन ने दावा किया था कि मेलुहा के जहाज उसकी राजधानी के बंदरगाह पर आते थे।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
        ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        1,
        "कथन 1 गलत है: मेसोपोटामिया के ग्रंथों में सिंधु घाटी को मेलुहा कहा गया है (माकन ओमान को दर्शाता है)। कथन 2 सही है: सारगोन के अभिलेख में अक्कड़ बंदरगाह पर मेलुहा जहाजों का उल्लेख है।"
    ),
    # MQ4
    (
        "फारस की खाड़ी के व्यापार में पारगमन बंदरगाहों की पहचान के संदर्भ में, निम्नलिखित युग्मों में से कौन-सा/से सही सुमेलित है/हैं?\n1. दिलमुन : बहरीन द्वीप, जो मीठे पानी वाले पारगमन बंदरगाह के रूप में प्रसिद्ध था।\n2. माकन : ओमान प्रायद्वीप, जो निकल युक्त तांबे का मुख्य स्रोत था।\nनीचे दिए गए कूट का प्रयोग कर सही उत्तर चुनिए:",
        ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        2,
        "दोनों युग्म बिल्कुल सही सुमेलित हैं। दिलमुन की पहचान बहरीन और माकन की ओमान से की जाती है।"
    ),
    # MQ5
    (
        "लोथल के गोदीवाड़ा (Dockyard) के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:\n1. गोदी का तालाब धूप में सुखाई गई कच्ची ईंटों से बनाया गया था।\n2. निम्न ज्वार के समय जहाजों को तैरता रखने के लिए निकास द्वार पर लकड़ी का लॉक-गेट लगाया गया था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
        ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        1,
        "कथन 1 गलत है: गोदी का तालाब पकी ईंटों से बना था ताकि पानी का रिसाव न हो। कथन 2 सही है: लकड़ी का लॉक-गेट पानी को तालाब में रोककर रखता था जिससे जहाज तैरते रहें।"
    ),
    # MQ6
    (
        "लंबी दूरी के व्यापार में हड़प्पा मुहरों और मिट्टी की छापों की भूमिका के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. चौकोर सेलखड़ी की मुहरों का उपयोग निश्चित मूल्य वाले धातु के सिक्कों के रूप में होता था।\n2. गांठों पर लगाई गई मिट्टी की छाप से व्यापारी परिवहन के दौरान सामान से छेड़छाड़ की जांच कर सकते थे।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
        ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        1,
        "कथन 1 गलत है: मुहरें मुद्रा नहीं थीं; व्यापार वस्तु विनिमय पर आधारित था। कथन 2 सही है: मिट्टी की छापें सुरक्षा सील के रूप में काम करती थीं।"
    ),
    # MQ7
    (
        "हड़प्पा व्यापार नेटवर्क की तटीय सुदृढ़ चौकियों के संदर्भ में, निम्नलिखित में से कौन से स्थल ईरान सीमा के पास मकरान तट पर स्थित हैं?\n1. सुत्कागेंदोर\n2. सोत्का कोह\n3. बालाकोट\nनीचे दिए गए कूट का प्रयोग कर सही उत्तर चुनिए:",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        0,
        "सुत्कागेंदोर और सोत्का कोह मकरान तट पर स्थित निगरानी दुर्ग थे। बालाकोट पूर्व में विंदर नदी के पास स्थित था जो शंख उद्योग का केंद्र था।"
    ),
    # MQ8
    (
        "कच्चे माल और उनके प्राथमिक आयात क्षेत्रों के निम्नलिखित युग्मों पर विचार कीजिए:\n1. चांदी : अफगानिस्तान और ईरान\n2. फिरोजा (Turquoise) : उत्तर-पूर्वी ईरान (खुरासान)\n3. जेड (Jade) : पामीर पहाड़ियां / मध्य एशिया\nउपर्युक्त युग्मों में से कौन-से सही सुमेलित हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        3,
        "तीनों युग्म सही सुमेलित हैं। चांदी, फिरोजा और जेड को थल मार्ग द्वारा मध्य एशिया और ईरान से आयात किया जाता था।"
    ),
    # MQ9
    (
        "मेसोपोटामिया के ग्रंथों में मेलुहा के 'हाजा-पक्षी' (Haja-bird) का उल्लेख है। इतिहासकार इसकी पहचान किससे करते हैं?",
        ["मोर, जिसे मेसोपोटामिया में एक विलासिता के सुंदर पक्षी के रूप में सराहा जाता था", "शिकार के लिए सुमेरियन अमीरों द्वारा पाला जाने वाला बाज", "संदेशवाहक कबूतर, जिसका प्रयोग व्यापारियों द्वारा किया जाता था", "मांस के लिए निर्यात की जाने वाली मुर्गी"],
        0,
        "हाजा-पक्षी की पहचान मोर से की गई है, जो अपनी सुंदर आवाज और पंखों के लिए मेसोपोटामिया में काफी लोकप्रिय था।"
    ),
    # MQ10
    (
        "उत्तर हड़प्पा काल में व्यापारिक अर्थव्यवस्था के पतन के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:\n1. लगभग 1900 ईसा पूर्व के बाद मेसोपोटामिया के ग्रंथों में मेलुहा का उल्लेख आना पूरी तरह बंद हो गया।\n2. मेसोपोटामिया के अक्कड़ साम्राज्य के पतन से फारस की खाड़ी का समुद्री व्यापार मार्ग टूट गया।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?",
        ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        2,
        "दोनों कथन सही हैं। मेसोपोटामिया के अक्कड़ साम्राज्य के पतन और भारत में हड़प्पा के पतन से लंबी दूरी का विदेशी व्यापार नष्ट हो गया।"
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
