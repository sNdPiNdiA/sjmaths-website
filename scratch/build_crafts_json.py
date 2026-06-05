import json
import os

ENG_DIR = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\HarappanIndus-Valley-Civilisation\Crafts"
HIN_DIR = os.path.join(ENG_DIR, "hi")
os.makedirs(HIN_DIR, exist_ok=True)

# English base structure
eng_data = {
    "breadcrumbs": {
        "parent": "UPSC Syllabus",
        "parentUrl": "/upsc/",
        "current": "Crafts of IVC"
    },
    "hero": {
        "title": "Crafts of the Indus Valley Civilisation",
        "description": "Explore the sophisticated metallurgical, lapidary, shell-working, ceramic, and sculpture traditions of the Harappan Civilisation for UPSC GS-1."
    },
    "labels": {
        "clickToExpand": "Click to expand details",
        "mockIntro": {
            "title": "Interactive UPSC Mock Test",
            "description": "Evaluate your mastery of Harappan craft traditions. This timed test contains 10 high-quality, exam-standard questions with negative marking.",
            "startBtn": "Start Mock Test"
        },
        "mockPlay": {
            "prevBtn": "Previous Question",
            "nextBtn": "Next Question",
            "submitBtn": "Submit Test"
        }
    },
    "timeline": {
        "title": "Craft & Technology Milestones",
        "description": "Track the technological developments in metallurgy, ceramics, bead processing, and brick making across the Indus Civilisation.",
        "cards": [
            {
                "period": "Bead-making & Lapidary",
                "date": "Chanhudaro & Lothal Workshops",
                "details": "Mass production of carnelian, lapis lazuli, and steatite beads using specialized micro-drills, furnaces, and grinding stones."
            },
            {
                "period": "Metallurgy & Bronze",
                "date": "Lost-Wax Casting Technique",
                "details": "Sophisticated metal casting (cire perdue) used to manufacture hollow and solid bronze sculptures, alongside copper tool production."
            },
            {
                "period": "Ceramics & Construction",
                "date": "Painted Pottery & 4:2:1 Bricks",
                "details": "Standardized wheel-made black-on-red pottery and uniform kiln-baked bricks with a strict 4:2:1 dimension ratio."
            }
        ]
    },
    "mnemonics": {
        "title": "Mnemonics & Memory Hacks",
        "description": "Use these visual memory hooks to retain critical facts about Harappan crafts and technology for the UPSC Civil Services Examination.",
        "items": [
            {
                "title": "Mnemonic 1: Specialized Bead Sites",
                "phrase": "\"Chan-Lo-Drill (Chanhudaro and Lothal Bead Drill Factories)\"",
                "decryption": "Remember that **Chanhudaro** and **Lothal** are the two premier centers where specialized bead-making workshops with drills and carnelian-heating kilns were excavated."
            },
            {
                "title": "Mnemonic 2: Coastal Shell Centers",
                "phrase": "\"Ba-Na-She (Balakot and Nageshwar Coastal Shell Industry)\"",
                "decryption": "**Ba**lakot and **Na**geshwar are located directly on the coast, functioning as specialized factories for **She**ll-working (bangles, ladles, inlays)."
            },
            {
                "title": "Mnemonic 3: Standard Brick Dimension",
                "phrase": "\"Brick-421 (Ratio of Length : Width : Thickness)\"",
                "decryption": "Harappan bricks maintained a highly standardized dimension ratio of **4:2:1** (e.g. 28 cm × 14 cm × 7 cm) across all Mature sites."
            }
        ]
    },
    "flashcards": {
        "title": "Active Recall Flashcards",
        "description": "Use these active recall questions to reinforce fact-dense syllabus details on Harappan crafts.",
        "items": [
            {
                "question": "What specialized metallurgical technique was used to cast the Dancing Girl bronze statue?",
                "answer": "The <strong>Lost-Wax technique</strong> (also known as <i>cire perdue</i>), involving hollow-casting over a clay core.",
                "icon": "fa-fire"
            },
            {
                "question": "Which coastal Harappan sites specialized in marine shell craft manufacture?",
                "answer": "<strong>Nageshwar</strong> (Gujarat) and <strong>Balakot</strong> (Balochistan), owing to direct access to coastal marine resources.",
                "icon": "fa-water"
            },
            {
                "question": "Name the primary material and the method used to harden Harappan seals.",
                "answer": "Seals were carved from soft <strong>steatite (soapstone)</strong> and then baked in a kiln to dry, harden, and whiten the stone.",
                "icon": "fa-stamp"
            },
            {
                "question": "How did Harappan potters produce the characteristic black-on-red painted ware?",
                "answer": "By applying a bright red clay slip as the base coat, painting designs in black manganese or iron pigment, and firing the pot.",
                "icon": "fa-paint-roller"
            },
            {
                "question": "What is the significance of the red sandstone torso found at Harappa?",
                "answer": "It demonstrates highly advanced, realistic <strong>three-dimensional human stone carving</strong> with socket holes for attaching limbs.",
                "icon": "fa-child"
            }
        ]
    },
    "deepDive": {
        "title": "Syllabus Core Study Notes (Deep-Dive)",
        "description": "Master the raw materials, technology, and regional specialization of Harappan craft guilds.",
        "sections": [
            {
                "title": "1. Bead-making, Shell-working & Gemstone Processing (Lothal, Chanhudaro & Balakot)",
                "content": """<p>The Harappans ran a highly specialized and geographically distributed lapidary and shell-working industry to cater to domestic demand and international trade.</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-gem"></i> Bead Factories & Gemstone Processing</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>Chanhudaro and Lothal:</strong> Dedicated bead-making factories have been excavated here, complete with working platforms, ovens, sorting jars, and specialized chert micro-drills.</li>
      <li><strong>Gemstone Sourcing:</strong> Carnelian was sourced from Gujarat and heated in kilns to turn deep red. Lapis Lazuli was imported from Badakhshan (Shortughai), Turquoise from Iran, and Steatite from Rajasthan.</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-fish"></i> Coastal Shell-Working Industry</div>
    <p style="font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;">
      Sites located near coastal waters like **Nageshwar** (Gujarat) and **Balakot** (Balochistan) were dedicated shell-working centers. Artisans manufactured bangles, rings, ladles, gaming pieces, and intricate floral or geometric inlays for furniture, which were transported to major metropolitan centers like Harappa and Mohenjo-daro.
    </p>
  </div>
</div>""",
                "masteryZone": []
            },
            {
                "title": "2. Metallurgy, Bronze Casting (Lost-Wax) & Stone/Terracotta Sculpture",
                "content": """<p>Harappan artistic expression is characterized by a balance of naturalism and technological ingenuity in bronze casting, stone carving, and terracotta art.</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-fire-burner"></i> Bronze Metallurgy & Lost-Wax Casting</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>Lost-Wax Technique (Cire Perdue):</strong> Artisans modeled figurines in wax, coated them in clay, heated the mold to drain the melted wax, and poured molten bronze into the hollow cavity. Famous examples include the *Dancing Girl* and bronze animals.</li>
      <li><strong>Copper Tools:</strong> Manufactured standard tools like flat chisels, knives, curved saws, fish hooks, and razors. Copper was sourced from the Khetri mines of Rajasthan.</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-shapes"></i> Stone & Terracotta Sculpture</div>
    <p style="font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;">
      **Stone Sculpture:** Notable works include the steatite *Priest-King* bust (showing a trefoil shawl pattern) and a realistic *red sandstone torso* from Harappa with socket joints.
      <br>**Terracotta Art:** Primarily hand-modeled, including Mother Goddess figurines, animal toys (humped bulls, moving-head monkeys), and toy carts, which reflect daily folk culture.
    </p>
  </div>
</div>""",
                "masteryZone": []
            },
            {
                "title": "3. Pottery Traditions, Seal Carving & Brick Manufacturing (4:2:1 Ratio)",
                "content": """<p>Standardization and industrial-scale production are key characteristics of Harappan pottery, glyptic arts, and municipal architecture.</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-cubes"></i> Standardized Bricks & Weights</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>The 4:2:1 Brick Ratio:</strong> All bricks (whether kiln-baked for public drains/Citadel bases or sun-dried for ordinary houses) maintained a strict ratio of 4:2:1 (Length:Width:Thickness).</li>
      <li><strong>Standardized Weights:</strong> Highly accurate cubic chert weights followed a binary system (1, 2, 4, 8, 16, 32...) for lower units, and a decimal system for higher weights.</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-stamp"></i> Ceramics & Seal glyptic Arts</div>
    <p style="font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;">
      **Pottery:** Standardized, wheel-made, painted black-on-red ware featuring geometric designs, pipal leaves, birds, and fish. Perforated jars were produced, likely for brewing or straining liquids.
      <br>**Seal Carving:** Square steatite seals were carved with animal reliefs (unicorn, bull, elephant) and script, then fired to create a durable, white glaze surface.
    </p>
  </div>
</div>""",
                "masteryZone": []
            }
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
        "current": "हड़प्पा के शिल्प"
    },
    "hero": {
        "title": "हड़प्पा सभ्यता के शिल्प और कलाएं",
        "description": "यूपीएससी परीक्षा (GS-1) के लिए सिंधु घाटी सभ्यता की धातुकर्म, मनका-निर्माण, शंख-शिल्प, मृदभांड और मूर्तिकला परंपराओं का विस्तृत अध्ययन करें।"
    },
    "labels": {
        "clickToExpand": "विवरण देखने के लिए क्लिक करें",
        "mockIntro": {
            "title": "इंटरैक्टिव परीक्षा मॉक टेस्ट",
            "description": "हड़प्पा शिल्प और कला परंपराओं के संबंध में अपनी तैयारी का मूल्यांकन करें। इस समयबद्ध परीक्षण में नकारात्मक अंकन के साथ 10 उच्च-स्तरीय यूपीएससी मानक के प्रश्न शामिल हैं।",
            "startBtn": "मॉक टेस्ट शुरू करें"
        },
        "mockPlay": {
            "prevBtn": "Previous Question",
            "nextBtn": "Next Question",
            "submitBtn": "Submit Test"
        }
    },
    "timeline": {
        "title": "शिल्प और प्रौद्योगिकी के चरण",
        "description": "सिंधु सभ्यता में धातुकर्म, मृदभांड, मनका प्रसंस्करण और ईंट निर्माण के तकनीकी विकास का कालक्रम देखें।",
        "cards": [
            {
                "period": "मनका और रत्न प्रसंस्करण",
                "date": "चन्हुदड़ो और लोथल कार्यशालाएं",
                "details": "सूक्ष्म-ड्रिल, भट्टियों और घिसाई पत्थरों का उपयोग करके अकीक (carnelian), लाजवर्द और सेलखड़ी के मनकों का बड़े पैमाने पर उत्पादन।"
            },
            {
                "period": "धातुकर्म और कांस्य",
                "date": "लुप्त-मोम ढलाई तकनीक",
                "details": "कांस्य की खोखली और ठोस मूर्तियों (जैसे नर्तकी) तथा तांबे के उपकरणों के निर्माण के लिए उन्नत धातु ढलाई (cire perdue) तकनीक का प्रयोग।"
            },
            {
                "period": "मृदभांड और निर्माण",
                "date": "चित्रित बर्तन और 4:2:1 ईंटें",
                "details": "चाक पर बने लाल और काले रंग के चित्रित बर्तनों का मानकीकरण और 4:2:1 के निश्चित अनुपात वाली पक्की ईंटों का सार्वभौमिक निर्माण।"
            }
        ]
    },
    "mnemonics": {
        "title": "याद रखने के सूत्र (Mnemonics)",
        "description": "यूपीएससी परीक्षा के लिए हड़प्पा के शिल्पों और संबंधित स्थलों को आसानी से याद रखने के लिए इन सूत्रों का उपयोग करें।",
        "items": [
            {
                "title": "याद रखने का सूत्र 1: मनका निर्माण स्थल",
                "phrase": "\"चन्हु-लो-ड्रिल (चन्हुदड़ो और लोथल मनका-ड्रिल कारखाने)\"",
                "decryption": "याद रखें कि **चन्हुदड़ो** और **लोथल** दो प्रमुख स्थल हैं जहाँ मनका बनाने के कारखाने, ड्रिल और अकीक को गर्म करने वाले अलाव मिले हैं।"
            },
            {
                "title": "याद रखने का सूत्र 2: तटीय शंख शिल्प",
                "phrase": "\"बा-ना-शंख (बालाकोट और नागेश्वर तटीय शंख शिल्प)\"",
                "decryption": "**बा**लाकोट और **ना**गेश्वर सीधे समुद्र तट पर स्थित थे, जो **शंख** (shell) शिल्प (चूड़ियाँ, कड़छी, पच्चीकारी) के प्रमुख केंद्र थे।"
            },
            {
                "title": "याद रखने का सूत्र 3: ईंटों का अनुपात",
                "phrase": "\"ईंट-421 (लंबाई : चौड़ाई : मोटाई का अनुपात)\"",
                "decryption": "हड़प्पा की ईंटों में सभी परिपक्व स्थलों पर **4:2:1** (जैसे 28 सेमी × 14 सेमी × 7 सेमी) का सख्त आकार अनुपात बनाए रखा गया था।"
            }
        ]
    },
    "flashcards": {
        "title": "सक्रिय स्मरण फ्लैशकार्ड (Active Recall)",
        "description": "तथ्य-प्रधान यूपीएससी प्रश्नों को याद रखने के लिए इन फ्लैशकार्ड्स का उपयोग करें। उत्तर देखने के लिए नीचे दिए गए कार्ड्स पर क्लिक करें।",
        "items": [
            {
                "question": "कांस्य की प्रसिद्ध 'नर्तकी' (Dancing Girl) मूर्ति को ढालने के लिए किस तकनीक का प्रयोग किया गया था?",
                "answer": "<strong>लुप्त-मोम पद्धति</strong> (Lost-Wax या <i>cire perdue</i>), जिसमें मिट्टी के सांचे के ऊपर धातु ढलाई की जाती थी।",
                "icon": "fa-fire"
            },
            {
                "question": "समुद्री शंख से बनी चूड़ियों और शिल्पों के निर्माण में कौन से तटीय स्थल विशिष्ट स्थान रखते थे?",
                "answer": "<strong>नागेश्वर</strong> (गुजरात) और <strong>बालाकोट</strong> (बलूचिस्तान), क्योंकि इनके पास समुद्री संसाधनों की सीधी पहुंच थी।",
                "icon": "fa-water"
            },
            {
                "question": "हड़प्पा की मुहरें किस प्राथमिक पत्थर से बनाई जाती थीं और उन्हें कठोर कैसे किया जाता था?",
                "answer": "मुहरें मुख्य रूप से नरम पत्थर <strong>सेलखड़ी (steatite)</strong> से बनाई जाती थीं और फिर उन्हें भट्टी में पकाकर कठोर व चमकीला सफेद बनाया जाता था।",
                "icon": "fa-stamp"
            },
            {
                "question": "हड़प्पा के कुम्हार लाल सतह पर काले रंग के चित्रित बर्तन (black-on-red ware) कैसे बनाते थे?",
                "answer": "बर्तन पर लाल मिट्टी का लेप लगाकर, मैंगनीज या लोहे के ऑक्साइड पिगमेंट से काली पेंटिंग करके और फिर उसे आग में पकाकर।",
                "icon": "fa-paint-roller"
            },
            {
                "question": "हड़प्पा से प्राप्त 'लाल बलुआ पत्थर के धड़' (red sandstone torso) का क्या महत्व है?",
                "answer": "यह अत्यंत यथार्थवादी <strong>त्रि-आयामी मानव पाषाण मूर्तिकला</strong> को दर्शाता है, जिसमें हाथ-पैर जोड़ने के लिए सॉकेट छेद बने थे।",
                "icon": "fa-child"
            }
        ]
    },
    "deepDive": {
        "title": "पाठ्यक्रम मुख्य नोट्स (गहन अध्ययन)",
        "description": "हड़प्पा शिल्प श्रेणियों, सामग्रियों के स्रोत और क्षेत्रीय विशेषज्ञता का गहन अध्ययन करें।",
        "sections": [
            {
                "title": "1. मनका-निर्माण, शंख-शिल्प और रत्न प्रसंस्करण (लोथल, चन्हुदड़ो और बालाकोट)",
                "content": """<p>सिंधु वासियों ने घरेलू मांग और मेसोपोटामिया जैसे विदेशी देशों के साथ व्यापार के लिए मनका-निर्माण और शंख-शिल्प का एक सुव्यवस्थित नेटवर्क विकसित किया था।</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-gem"></i> मनके के कारखाने और रत्न प्रसंस्करण</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>चन्हुदड़ो और लोथल:</strong> इन दोनों स्थलों से मनका बनाने की बड़ी कार्यशालाएं मिली हैं, जहाँ काम करने के चबूतरे, भट्टियां, कच्चे पत्थर और चर्ट के बारीक सूक्ष्म-ड्रिल मिले हैं।</li>
      <li><strong>पत्थरों का आयात:</strong> अकीक (carnelian) को गुजरात से लाकर भट्टी में पकाया जाता था जिससे उसका रंग गहरा लाल हो जाता था। लाजवर्द (lapis) को बदख्शां (शोरतूघई) से और सेलखड़ी को राजस्थान से मंगाया जाता था।</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-fish"></i> तटीय शंख-शिल्प उद्योग</div>
    <p style="font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;">
      तटीय क्षेत्रों के निकट स्थित स्थल जैसे **नागेश्वर** (गुजरात) और **बालाकोट** (बलूचिस्तान) शंख उद्योग के प्रमुख केंद्र थे। यहाँ समुद्र से प्राप्त शंखों से चूड़ियाँ, छल्ले, कड़छी (ladles), पासे और फर्नीचर पर जड़ने के लिए पच्चीकारी का सामान बनाया जाता था और बड़े शहरों में भेजा जाता था।
    </p>
  </div>
</div>""",
                "masteryZone": []
            },
            {
                "title": "2. धातुकर्म, कांस्य ढलाई (लुप्त-मोम पद्धति) और पाषाण/मृण्मूर्तियाँ (Terracotta)",
                "content": """<p>हड़प्पा की कलात्मक अभिव्यक्ति धातुकर्म, पत्थर की नक्काशी और मिट्टी की मूर्तिकला में यथार्थवाद और तकनीकी कुशलता का बेहतरीन संतुलन प्रस्तुत करती है।</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-fire-burner"></i> कांस्य धातुकर्म और लुप्त-मोम ढलाई</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>लुप्त-मोम पद्धति (Cire Perdue):</strong> कलाकार पहले मोम की मूर्ति बनाते थे, फिर उस पर गीली मिट्टी का लेप लगाकर सुखाते थे। गर्म करने पर मोम पिघल कर निकल जाता था, और उस खाली सांचे में पिघला हुआ कांसा भर दिया जाता था। जैसे 'कांस्य नर्तकी' की मूर्ति।</li>
      <li><strong>तांबे के उपकरण:</strong> छेनी, चाकू, आरी, मछली पकड़ने के कांटे और उस्तरे बनाए जाते थे। तांबा मुख्य रूप से राजस्थान की खेतड़ी खानों से आता था।</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-shapes"></i> पाषाण और पकी मिट्टी (Terracotta) की मूर्तियाँ</div>
    <p style="font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;">
      **पाषाण मूर्तियाँ:** प्रमुख उदाहरण सेलखड़ी से बनी 'पुरोहित-राजा' (Priest-King) की मूर्ति है जो तिपतियाPattern वाला शॉल ओढ़े हैं, और हड़प्पा से मिला लाल बलुआ पत्थर का मानव धड़ है जिसमें हाथ-पैर जोड़ने के सॉकेट बने हैं।
      <br>**टेराकोटा कला:** मुख्य रूप से हाथ से बनाई गई मूर्तियां हैं, जैसे मातृदेवी की मूर्तियां, खिलौना गाड़ियां, सीटियां और विभिन्न जानवरों (जैसे कूबड़ वाला सांड, गर्दन हिलाने वाला बंदर) के खिलौने।
    </p>
  </div>
</div>""",
                "masteryZone": []
            },
            {
                "title": "3. मृदभांड परंपराएं, मुहर निर्माण और ईंट निर्माण तकनीक (4:2:1 अनुपात)",
                "content": """<p>उत्पादन का मानकीकरण और व्यापक पैमाने पर निर्माण हड़प्पा वासियों के बर्तनों, मुहरों और नागरिक वास्तुकला की मुख्य विशेषता थी।</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-cubes"></i> मानकीकृत ईंटें और बाट</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>4:2:1 ईंटों का अनुपात:</strong> सभी ईंटें (चाहे नालियों व सार्वजनिक इमारतों के लिए आग में पकाई गई हों या साधारण घरों के लिए धूप में सुखाई गई हों) लंबाई:चौड़ाई:मोटाई में 4:2:1 के सख्त अनुपात में थीं।</li>
      <li><strong>मानकीकृत बाट:</strong> चर्ट पत्थर के वर्गाकार बाट द्वि-आधारी पद्धति (1, 2, 4, 8, 16, 32...) और उच्च भारों के लिए दशमलव प्रणाली पर आधारित थे।</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-stamp"></i> मृदभांड (Ceramics) और मुहर निर्माण</div>
    <p style="font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;">
      **मृदभांड:** चाक पर बने लाल सतह वाले काले रंग के चित्रित बर्तन जिन पर ज्यामितीय आकृतियाँ, पीपल के पत्ते, पक्षी और मछलियाँ चित्रित होती थीं। कुछ छिद्रित जार (perforated jars) भी मिले हैं, जिनका उपयोग पेय छानने के लिए होता था।
      <br>**मुहर नक्काशी:** सेलखड़ी के वर्गाकार पत्थरों पर जानवरों (एक सींग वाला सांड, बैल, हाथी) के चित्र और लिपि खोदकर उन्हें भट्टी में पकाया जाता था, जिससे उन पर सफेद चमकीली परत बन जाती थी।
    </p>
  </div>
</div>""",
                "masteryZone": []
            }
        ]
    },
    "practiceQuestions": [],
    "mockTestQuestions": []
}

# Practice Questions (50 Qs) - UPSC Prelims Multi-Statement Style
practice_data_eng = [
    (
        "Consider the following statements regarding Harappan bead-making technology:\n1. Dedicated bead factories have been excavated at Chanhudaro and Lothal, featuring working benches and kilns.\n2. Scribes utilized specialized chert micro-drills to bore holes in hard gemstones like carnelian and jasper.\n3. The deep red color of carnelian was obtained by heating the raw yellow-brown pebbles in specialized firing pots.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All three statements are correct, describing bead-making factories, specialized chert drills, and the firing process to obtain red carnelian."
    ),
    (
        "With reference to the shell-working craft of the Indus Civilisation, consider the following statements:\n1. Balakot in Balochistan and Nageshwar in Gujarat were specialized centers for shell manufacturing.\n2. Inhabitants processed marine shells to make items like bangles, rings, ladles, and furniture inlays.\n3. Finished shell products were strictly consumed locally and were never traded to inland metropolitan centers like Harappa.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: shell ornaments were highly prized inland luxury items and were regularly transported to cities like Harappa and Mohenjo-daro."
    ),
    (
        "Consider the following statements regarding Harappan bronze casting metallurgy:\n1. Metal casters used the lost-wax technique (cire perdue) to manufacture bronze sculptures.\n2. The Dancing Girl statue was cast hollow, demonstrating advanced knowledge of hollow-core casting.\n3. The alloy composition of Harappan bronze shows a highly consistent 10-12% tin addition to copper.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: although they alloyed copper and tin, the proportion of tin varied widely (often under 5-8%), indicating that alloying was done by rule of thumb rather than rigid percentage formulas."
    ),
    (
        "With reference to the stone sculpture of the Mature Harappan phase, consider the following statements:\n1. The steatite bust of the Priest-King shows a stylized beard and a shawl draped over the left shoulder decorated with trefoil motifs.\n2. The red sandstone male torso from Harappa features socket holes in the neck and shoulders for attaching movable head and arms.\n3. Both sculptures reflect an identical stylistic tradition of monumental, large-scale public stone statues.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: Harappan sculptures are small and domestic in scale (the Priest-King is only 17 cm high, and the torso is even smaller), completely lacking monumental public statue traditions."
    ),
    (
        "Consider the following statements regarding the terracotta figurines of the Indus Valley:\n1. Most terracotta figurines were hand-modeled rather than cast in multi-part clay molds.\n2. Mother Goddess figurines are characterized by elaborate fan-shaped headdresses and heavy jewelry.\n3. Animal models include toy carts with movable wheels, whistles shaped like birds, and humped bulls.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All three statements are correct and define the construction, representation, and variety of Harappan terracotta art."
    ),
    (
        "With reference to the pottery traditions of the Indus Valley, consider the following statements:\n1. The dominant pottery type was wheel-made, painted black-on-red ware.\n2. Common decorative motifs on painted pottery include geometric lines, pipal leaves, fish scales, and birds.\n3. Perforated jars, containing numerous small holes, were likely used to hold incense or strain fermented beverages.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All three statements are correct, describing painted black-on-red ware, decoration motifs, and perforated jar functions."
    ),
    (
        "Consider the following statements regarding Harappan brick manufacturing:\n1. Bricks were manufactured in a standardized size ratio of 4:2:1 for length, width, and thickness.\n2. Kiln-baked bricks were used for public structures and drains, while sun-dried mud bricks were used for ordinary houses.\n3. Different cities used entirely different brick ratios based on regional local standards.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: the brick ratio of 4:2:1 was highly standardized across the entire Indus civilisation, proving centralized standards."
    ),
    (
        "With reference to the manufacture of Harappan seals, consider the following statements:\n1. Square seals were carved from soft steatite (soapstone) before being fired in a kiln.\n2. Firing the steatite seals hardened the stone and produced a white, lustrous glazed finish.\n3. Seals were carved with positive (normal) engravings so they could be read directly on the seal stone itself.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: seals were carved in negative (reverse/mirror-image) relief so that the stamped clay impressions would read correctly in positive layout."
    ),
    (
        "Consider the following statements regarding gemstone raw material sourcing:\n1. Lapis Lazuli was imported from Badakhshan in Afghanistan, where the Harappans set up a trade colony at Shortughai.\n2. Amethyst and Carnelian were sourced from the Deccan plateau and Gujarat.\n3. Jade was imported from Central Asia, while Steatite was sourced from Rajasthan.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, outlining the geographic sourcing of lapis, carnelian/amethyst, jade, and steatite."
    ),
    (
        "With reference to the production of faience in the Indus Valley, consider the following statements:\n1. Faience is a natural stone mined in Baluchistan, famous for its blue-green color.\n2. It was manufactured by firing a paste of ground silica/sand mixed with clay, gum, and mineral glaze.\n3. Faience was a highly prized luxury material, used to make small cosmetic pots, beads, and amulets.\nWhich of the statements given above is/are correct?",
        ["2 and 3 only", "2 only", "1 and 3 only", "1, 2 and 3"],
        0,
        "Statements 2 and 3 are correct. Statement 1 is incorrect: faience is an artificial/synthetic glazed material, not a natural mined stone."
    ),
    (
        "Consider the following statements regarding gold and silver crafts:\n1. Silver made its earliest appearance in India during the Harappan Civilisation, used for large vessels and jewelry.\n2. Gold ornaments were crafted as micro-beads, hollow spacers, and pendants, often alloyed with silver (electrum).\n3. Scribes recorded gold workshop accounts on copper plaques using a standard decimal numbering system.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: there is no archaeological evidence of written accounts or tax records on copper plaques; the script is undeciphered."
    ),
    (
        "With reference to the copper tool metallurgy of Harappans, consider the following statements:\n1. They manufactured flat chisels, mid-ribbed swords, socketed axes, and fish hooks.\n2. Tools were made using both casting in open clay molds and cold-hammering methods.\n3. Iron was added in small amounts to copper tools to increase their hardness.\nWhich of the statements given above is/are correct?",
        ["2 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statement 2 is correct. Statement 1 is incorrect: Harappans did NOT manufacture mid-ribbed swords or socketed axes (which require advanced casting methods and appeared later/outside Indus). Statement 3 is incorrect: iron was completely unknown to the Harappans."
    ),
    (
        "Consider the following statements regarding the spatial organization of craft production in Harappan cities:\n1. Artisans and craftsmen lived and worked in dedicated quarters situated in the Lower Town.\n2. The proximity of bead kilns to outer town walls suggests strict municipal zoning to control smoke and fire hazards.\n3. High-value craft materials like gold and lapis lazuli were processed exclusively on the Citadel mound under direct elite monopoly.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: raw materials and workshops for gold and lapis have been found in Lower Town residential blocks, indicating artisans worked outside Citadels."
    ),
    (
        "With reference to the cotton textile craft, consider the following statements:\n1. Scribes and traders wore light cotton garments, as indicated by textile impressions on clay sealings.\n2. Spindle whorls made of terracotta and faience are commonly found in both rich and poor households.\n3. Harappans were the first civilisation in the ancient world to domesticate, spin, and weave cotton.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, detailing cotton impressions, spindle whorls, and early domestication."
    ),
    (
        "Consider the following statements regarding the use of ivory in Harappan craft:\n1. Ivory was carved to produce combs, hairpins, gaming dice, and small measuring scales.\n2. Raw tusks were sourced from local Indian elephants (*Elephas maximus*) and processed in urban workshops.\n3. Ivory objects were exclusively reserved for export to Mesopotamia and were banned from local use.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: ivory artifacts are frequently found in local urban houses, showing widespread domestic consumption among wealthy citizens."
    ),
    (
        "With reference to the technological tools of Harappan builders, consider the following statements:\n1. They utilized plumb-bobs and right-angle measuring squares made of bronze or shell.\n2. Builders used standardized measuring scales engraved on ivory, shell, and bronze rods.\n3. Scribes carved mathematical construction blueprints on clay tablets before buildingCitadel platforms.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: no architectural drawings or blueprint tablets have ever been discovered in Indus archaeology."
    ),
    (
        "Consider the following statements regarding the production of chert blades:\n1. Chert blades were mass-produced in specialized workshops using raw material from the Rohri Hills in Sindh.\n2. Scribes distributed chert blades to farmers to harvest wheat and barley crops.\n3. The Rohri chert workshops represent one of the largest industrial mining sites of the Bronze Age.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, detailing Rohri chert source, tool distribution, and scale of mining."
    ),
    (
        "With reference to the pottery clay slips and paints, consider the following statements:\n1. Red clay slips were made by mixing iron-rich red ochre (*geru*) with water.\n2. Black paint was made using manganese-rich mineral pigments.\n3. Glazed pottery, representing a shiny glass-like surface, was widely manufactured in all Mature sites.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: glazed pottery was extremely rare and experimental in the Indus valley, with true glazed ware appearing much later in Indian history."
    ),
    (
        "Consider the following statements regarding the stone sculpture known as the 'Dancing Girl':\n1. It is a four-inch bronze figurine cast in Mohenjo-daro.\n2. She is depicted standing with one hand on her hip, wearing numerous bangles on her left arm.\n3. S..R. Rao read her name as 'Pre-Dravidian dancer' using the rebus translation method.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: the figurine is undeciphered, and no written labels accompany the statue; S.R. Rao's readings do not apply to the sculpture itself."
    ),
    (
        "With reference to Harappan toy-making, consider the following statements:\n1. Toy-makers created hollow terracotta bulls with movable heads attached by a fiber string.\n2. Toy carts featured wheels carved with spokes, mimicking historical Maurya wheel designs.\n3. Whistles shaped like birds were hollow terracotta toys that produced sounds when blown.\nWhich of the statements given above is/are correct?",
        ["1 and 3 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 3 are correct. Statement 2 is incorrect: Harappan toy cart wheels were solid (either flat or with a raised hub), completely lacking spokes, which appeared in India later during the Vedic/historical phases."
    ),
    # Additional 30 questions
    (
        "Consider the following statements regarding the lost-wax bronze casting steps:\n1. The artist modeled the core shape in wax, then covered it with layers of clay.\n2. The clay mold was heated in a kiln, causing the wax to melt and flow out through small vents.\n3. Molten bronze was poured into the empty cavity, and once cooled, the clay outer shell was broken open.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All three statements correctly define the steps of the lost-wax casting (cire perdue) process."
    ),
    (
        "With reference to the stone carving known as the 'Male Torso' from Harappa, consider the following statements:\n1. It is made of red jasper or sandstone and is celebrated for its naturalistic musculature.\n2. It features socket holes to attach a separate head and arms, indicating a composite statue.\n3. The torso is over six feet tall, indicating it was placed in a public temple shrine.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: the torso is tiny (only about 9 cm high) and was likely a domestic or personal object, not a public temple statue."
    ),
    (
        "Consider the following statements regarding the raw material sourcing for bead-making:\n1. Carnelian was imported from Gujarat and processed in workshops using heat-treatment.\n2. Steatite (soapstone) was sourced from northern Rajasthan and Gujarat.\n3. Lapis Lazuli was imported directly from Mesopotamia in exchange for copper tools.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: Lapis Lazuli was imported from Badakhshan in Afghanistan (via the Shortughai trade outpost), not from Mesopotamia."
    ),
    (
        "With reference to the specialized drill bits found at craft sites, consider the following statements:\n1. Drill bits were made of a very hard, fine-grained stone called Ernestite.\n2. These drills were capable of drilling tiny holes through hard carnelian and jasper beads.\n3. Drill bits have been recovered in large quantities from Chanhudaro and Lothal.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All three statements are correct, describing the material (Ernestite), capability, and locations of Harappan bead drills."
    ),
    (
        "Consider the following statements regarding the production of faience:\n1. Faience objects show a bright, glossy blue-green glaze that mimics turquoise.\n2. The raw silica paste was molded into miniature pots, beads, and animal figurines before firing.\n3. Faience required high-temperature kilns and advanced chemical knowledge, making it a prestige material.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All three statements are correct and define the aesthetics, raw components, and prestige status of faience."
    ),
    (
        "With reference to the bronze animal figurines, consider the following statements:\n1. Cast bronze bulls and buffaloes have been excavated from Mohenjo-daro.\n2. These figures are rendered with expressive realism, showing muscles and skin folds.\n3. The animal figures were used as standardized weights in the grain markets.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: bronze animal figurines were artistic and religious works, while weights were made of cut and polished chert stone cuboids."
    ),
    (
        "Consider the following statements regarding Harappan pottery shapes:\n1. The classic Harappan pottery forms include S-shaped jars, dish-on-stands, and storage jars.\n2. Perforated jars feature circular holes all over the body, except on the solid base.\n3. S-shaped jars were used for cooking rice, as indicated by burnt residue inside them.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: S-shaped jars are tall, elaborately decorated wares likely used for storage or ceremonial display, not cooking."
    ),
    (
        "With reference to the production of terracotta bangles, consider the following statements:\n1. Terracotta bangles are found in massive quantities, indicating they were worn by commoners.\n2. High-quality terracotta bangles were polished and painted to mimic red carnelian.\n3. Bangles were exclusively made of metal, and clay bangles were completely forbidden.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: clay terracotta bangles were extremely common and worn by the majority of the population."
    ),
    (
        "Consider the following statements regarding the steatite seal carving technique:\n1. Carvers used sharp bronze chisels and chert tools to incise detailed animal reliefs.\n2. The back of the seal was carved with a small perforated boss (button) for threading a cord.\n3. Steatite seals were painted with natural organic inks to create colorful trade marks.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: seals were not painted with inks; they were fired to create a glazed white surface and pressed into clay."
    ),
    (
        "With reference to the brick kilns and ovens, consider the following statements:\n1. Brick-firing kilns have been found in the suburbs of major cities like Harappa.\n2. Kilns consumed massive quantities of timber, contributing to environmental deforestation.\n3. In early phases, Harappans used only imported Mesopotamian baked bricks.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: Harappans manufactured their own baked bricks locally; there is no evidence of importing bricks from Mesopotamia."
    ),
    (
        "Consider the following statements regarding the stone sculpture known as the 'Bearded Priest':\n1. It is carved from soft steatite and measures about 17 cm in height.\n2. The eyes are elongated and half-closed in a meditative state.\n3. He wears an armlet on his right arm and a head fillet with a circular clasp.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All three statements are correct and define the physical characteristics of the Priest-King steatite bust."
    ),
    (
        "With reference to the use of shells in architectural inlay, consider the following statements:\n1. Shell segments were cut into triangles, circles, and petals for furniture decoration.\n2. Shell inlays were held in place using natural bitumen or resin adhesives.\n3. Architectural shell inlay was a common craft technique at inland cities like Harappa.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, detailing the shapes, adhesives, and inland distribution of architectural shell inlay."
    ),
    (
        "Consider the following statements regarding the pottery painted designs:\n1. Painted designs are typically executed in black pigment over a bright red slip.\n2. Motif designs often show intersecting circles, creating geometric web-like patterns.\n3. The painted designs depict complex narrative scenes of battles and royal coronations.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: Harappan pottery designs feature geometric, floral, and animal motifs, but completely lack narrative historical scenes of battles or kings."
    ),
    (
        "With reference to the manufacture of weight units, consider the following statements:\n1. Weights were cut from high-quality chert and polished to form perfect cubes.\n2. The lower weight values progressed in a binary series (1, 2, 4, 8, 16, 32, 64).\n3. Weights were manufactured by individual merchants with no municipal quality control.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: the extreme accuracy and standardization of weights across all sites prove strict municipal quality control."
    ),
    (
        "Consider the following statements regarding the gold jewelry hoards:\n1. Hoards of gold ornaments have been found inside silver and bronze jars under house floors.\n2. Gold ornaments include headbands (fillets), armlets, necklaces, and micro-beads.\n3. The presence of gold hoards indicates wealth accumulation and private saving in cities.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, describing the gold jewelry hoards, ornament types, and economic implications."
    ),
    (
        "With reference to the copper fish hooks, consider the following statements:\n1. Numerous copper fish hooks have been excavated from coastal and riverine sites.\n2. The fish hooks feature a barbed design, showing high technological efficiency.\n3. Fish hooks suggest that fishing was a major dietary and craft livelihood in the IVC.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All three statements are correct and define the material, design, and livelihood significance of copper fish hooks."
    ),
    (
        "Consider the following statements regarding the production of steatite paste beads:\n1. Steatite paste beads were made by grinding steatite scrap into paste and extruding it.\n2. The paste beads were glazed and fired, allowing mass-production of micro-beads.\n3. Steatite paste beads were so heavy that they were only worn by draft animals.",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: steatite micro-beads were lightweight, highly delicate, and worn as jewelry by citizens."
    ),
    (
        "With reference to the terracotta animal figures, consider the following statements:\n1. Terracotta bulls often feature a large hump and detailed horns.\n2. Model monkeys have been found that can slide down a string, showing kinetic toy design.\n3. Toy carts are the most common terracotta vehicles found, with solid wheels.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, describing the humped bulls, sliding monkeys, and solid-wheeled toy carts."
    ),
    (
        "Consider the following statements regarding the pottery kiln temperatures:\n1. Harappan kilns reached firing temperatures between 800°C and 1000°C.\n2. The high firing temperatures produced very durable, fully baked terracotta and ceramics.\n3. Kilns were built inside Citadel palaces to keep the firing technology secret.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: kilns were located in the suburbs and lower quarters of towns near raw clay sources, not inside Citadel palaces."
    ),
    (
        "With reference to the sourcing of raw metals, consider the following statements:\n1. Copper was sourced from the Khetri mines of Rajasthan and Baluchistan.\n2. Tin was imported from Afghanistan and Central Asia to alloy with copper.\n3. Iron was mined in large quantities from the Chota Nagpur plateau.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: iron was completely unknown in the Bronze Age Harappan Civilisation."
    ),
    (
        "Consider the following statements regarding the stone tool Rohri chert blades:\n1. Rohri chert is characterized by a high-quality, uniform brownish-yellow color.\n2. The blades were struck from prepared cores using a pressure-flaking technique.\n3. Rohri chert blades are found in almost all Mature Harappan urban households.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct and define the material, manufacture technique, and distribution of Rohri chert blades."
    ),
    (
        "With reference to the lapis lazuli processing at Shortughai, consider the following statements:\n1. Shortughai was a Harappan trading outpost established in northeastern Afghanistan.\n2. Inhabitants mined lapis lazuli directly from the Badakhshan mountains and cut it into rough beads.\n3. Shortughai was fortified to prevent Siberian nomadic tribes from stealing the lapis stockpile.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: Shortughai was a trade outpost established near mining routes; there is no evidence of conflicts with Siberian tribes."
    ),
    (
        "Consider the following statements regarding the shell bangle manufacture steps:\n1. The artisan cut the shell spire using a curved bronze saw.\n2. The shell ring was ground and polished using sandstone blocks.\n3. Finished bangles often feature a carved chevron or V-shaped groove decoration.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All three statements are correct, outlining the sawing, polishing, and chevron decoration steps of shell bangle manufacture."
    ),
    (
        "With reference to the terracotta 'Mother Goddess' figurines, consider the following statements:\n1. They are hand-modeled using a pinching method to shape the facial features.\n2. The eyes are represented by applied round pellets of clay (coffee-bean eyes).\n3. They are found exclusively in administrative storage rooms on the Citadel mounds.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: Mother Goddess figurines are found in common domestic quarters of Lower Towns, indicating household worship."
    ),
    (
        "Consider the following statements regarding the bronze 'Dancing Girl' stylistic features:\n1. She wears a necklace with three pendants and has her hair tied in a bun.\n2. Her left arm is almost completely covered with 24 to 25 bangles.\n3. The figure is cast in a stiff, formal ritual posture similar to Egyptian pharaoh statues.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: the figurine is celebrated for its natural, fluid, and expressive posture (tribhanga-like dance pose), completely different from stiff Egyptian styles."
    ),
    (
        "With reference to the ceramic glaze and decoration, consider the following statements:\n1. The red slip on pottery was made from fine alluvial clay rich in iron oxides.\n2. The black manganese paint was applied using animal hair brushes on the unfired pot.\n3. Scribes painted short narrative text captions on the neck of all storage jars.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: there are no narrative text captions on storage jars; the script signs appear as brief stamped/scratched markings or graffiti."
    ),
    (
        "Consider the following statements regarding the stone sculpture known as the 'Red Torso':\n1. It was excavated at Harappa by archaeologist M.S. Vats.\n2. The sculpture displays realistic soft belly modeling and accurate human anatomy.\n3. The torso is carved in relief on the side of a large sandstone pillar.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: it is a three-dimensional freestanding sculpture, not a relief carving on a pillar."
    ),
    (
        "With reference to the production of terracotta toy carts, consider the following statements:\n1. Carts are modeled after actual bullock carts used for transporting agricultural goods.\n2. The cart frame features holes to insert wooden sticks representing the chassis and yoke.\n3. The cart wheels were fitted with rubber-like tree resin to reduce friction.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: wheels were solid terracotta or wood with no resin or rubber fittings."
    ),
    (
        "Consider the following statements regarding the steatite seal sizes:\n1. Most seals are small square plaques ranging from 2 to 4 cm in length.\n2. Rectangular seals carrying only script and no animal reliefs are also common.\n3. Large seals measuring over one meter were placed in markets to display royal tax rates.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: there are no monumental seals; all seals were small portable administrative tools."
    ),
    (
        "With reference to the metallurgical bronze tools, consider the following statements:\n1. Bronze tools were cast using two-part stone molds for complex shapes.\n2. Saws feature offset teeth that prevent the blade from binding during woodcutting.\n3. Harappans had specialized bronze helmets and body armor for military use.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: the Harappans were a peaceful commercial society and completely lacked specialized metal armor or helmets."
    )
]

practice_data_hin = [
    (
        "हड़प्पा मनका-निर्माण तकनीक के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. चन्हुदड़ो और लोथल से मनके बनाने के कारखाने मिले हैं, जिनमें काम करने के चबूतरे और भट्टियाँ शामिल हैं।\n2. शिल्पकार अकीक (carnelian) और जैस्पर जैसे कठोर पत्थरों में छेद करने के लिए विशिष्ट चर्ट सूक्ष्म-ड्रिल (micro-drills) का उपयोग करते थे।\n3. अकीक का गहरा लाल रंग पीले-भूरे पत्थरों को विशेष पकाने वाले बर्तनों में गर्म करके प्राप्त किया जाता था।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        3,
        "तीनों कथन सही हैं, जो मनका कारखानों, विशिष्ट चर्ट ड्रिल और अकीक को पकाकर लाल रंग प्राप्त करने की प्रक्रिया का वर्णन करते हैं।"
    ),
    (
        "सिंधु सभ्यता के शंख-शिल्प (shell-working) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. बलूचिस्तान का बालाकोट और गुजरात का नागेश्वर शंख निर्माण के विशिष्ट केंद्र थे।\n2. यहाँ के निवासी चूड़ियाँ, छल्ले, कड़छी और फर्नीचर पर जड़ने की पच्चीकारी जैसी वस्तुएँ बनाने के लिए समुद्री शंखों का प्रसंस्करण करते थे।\n3. शंख के बने सामानों का उपभोग केवल स्थानीय स्तर पर होता था और उन्हें हड़प्पा जैसे अंतर्देशीय शहरों में कभी नहीं भेजा जाता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: शंख के आभूषण अत्यधिक मूल्यवान विलासिता की वस्तुएँ थे और उन्हें नियमित रूप से हड़प्पा और मोहनजोदड़ो जैसे बड़े शहरों में भेजा जाता था।"
    ),
    (
        "हड़प्पा की कांस्य ढलाई धातुकर्म (bronze casting) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. धातु शिल्पकार कांस्य की मूर्तियाँ बनाने के लिए लुप्त-मोम पद्धति (lost-wax technique) का उपयोग करते थे।\n2. कांस्य की नर्तकी (Dancing Girl) मूर्ति अंदर से खोखली ढाली गई थी, जो खोखली ढलाई के उन्नत ज्ञान को दर्शाती है।\n3. हड़प्पा के कांस्य का रासायनिक संगठन तांबे में ठीक 10-12% टिन के मानकीकृत मिश्रण को दर्शाता है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: हालांकि वे तांबे और टिन का मिश्रण करते थे, पर टिन की मात्रा अलग-अलग उपकरणों में बहुत भिन्न (अक्सर 5-8% से कम) पाई गई है, जो दर्शाता है कि मानकीकृत अनुपात के बजाय केवल व्यावहारिक अनुमान से मिश्रण किया जाता था।"
    ),
    (
        "परिपक्व हड़प्पा चरण की पाषाण मूर्तिकला (stone sculpture) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. सेलखड़ी से बने 'पुरोहित-राजा' (Priest-King) के धड़ में सुव्यवस्थित दाढ़ी और बाएं कंधे पर तिपतियाPattern वाला शॉल ओढ़े दिखाया गया है।\n2. हड़प्पा से प्राप्त लाल बलुआ पत्थर के पुरुष धड़ (male torso) में गर्दन और कंधों पर सॉकेट छेद बने हैं ताकि अलग से सिर और हाथ जोड़े जा सकें।\n3. दोनों मूर्तियां सार्वजनिक स्थलों पर स्थापित की जाने वाली विशाल, बड़े पैमाने की पत्थर की मूर्तियों की परंपरा को दर्शाती हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: हड़प्पा की मूर्तियाँ आकार में बहुत छोटी और घरेलू पैमाने की हैं (पुरोहित-राजा केवल 17 सेमी ऊंचे हैं और लाल धड़ इससे भी छोटा है), यहाँ विशाल सार्वजनिक मूर्तियों की कोई परंपरा नहीं थी।"
    ),
    (
        "सिंधु घाटी की मिट्टी की मूर्तियों (terracotta figurines) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. अधिकांश मिट्टी की मूर्तियाँ हाथ से गढ़ी (hand-modeled) गई थीं, न कि सांचों में ढाली गई थीं।\n2. मातृदेवी की मूर्तियों की विशेषता पंखे के आकार का जटिल मुकुट और भारी आभूषण हैं।\n3. जानवरों के खिलौनों में चलने वाले पहियों वाली खिलौना गाड़ियाँ, पक्षी के आकार की सीटियाँ और कूबड़ वाले सांड शामिल हैं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं और हड़प्पा की टेराकोटा कला के निर्माण, रूपों और विविधता को परिभाषित करते हैं।"
    ),
    (
        "सिंधु घाटी की मृदभांड (pottery) परंपराओं के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मुख्य प्रकार का मृदभांड चाक पर बना, लाल सतह पर काले रंग का चित्रित बर्तन (black-on-red ware) था।\n2. चित्रित बर्तनों पर सामान्य सजावटी डिज़ाइनों में ज्यामितीय रेखाएँ, पीपल के पत्ते, मछली के शल्क और पक्षी शामिल हैं।\n3. छिद्रित जार (perforated jars), जिनमें चारों ओर छोटे छेद होते थे, संभवतः धूप रखने या पेय छानने के काम आते थे।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो चित्रित मृदभांड, सजावटी पैटर्न और छिद्रित जार के कार्यों का वर्णन करते हैं।"
    ),
    (
        "हड़प्पा की ईंट निर्माण तकनीक के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. ईंटों का निर्माण लंबाई, चौड़ाई और मोटाई के लिए 4:2:1 के मानकीकृत अनुपात में किया जाता था।\n2. भट्टी में पकी ईंटों का उपयोग नालियों और सार्वजनिक भवनों में होता था, जबकि धूप में सूखी ईंटों का उपयोग साधारण घरों में होता था।\n3. अलग-अलग शहरों में स्थानीय मानकों के आधार पर बिल्कुल भिन्न अनुपातों की ईंटें प्रयुक्त होती थीं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: 4:2:1 का ईंट अनुपात पूरी सिंधु सभ्यता में अत्यधिक मानकीकृत था, जो एकीकृत योजना को दर्शाता है।"
    ),
    (
        "हड़प्पा की मुहरों (seals) के निर्माण के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. वर्गाकार मुहरों को भट्टी में पकाने से पहले नरम सेलखड़ी (steatite) पत्थर से तराशा जाता था।\n2. सेलखड़ी को पकाने से पत्थर कठोर हो जाता था और उस पर एक चमकदार सफेद परत बन जाती थी।\n3. मुहरों पर अक्षरों को सीधे (positive) रूप में खोदा जाता था ताकि मुहर के पत्थर पर ही उन्हें सीधे पढ़ा जा सके।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: मुहरों को विपरीत (negative/mirror-image) रूप में खोदा जाता था ताकि जब उन्हें मिट्टी पर दबाया जाए तो छाप सीधी और पठनीय बने।"
    ),
    (
        "रत्नों और कच्चे माल के स्रोतों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. लाजवर्द (Lapis Lazuli) का आयात अफगानिस्तान के बदख्शां से होता था, जहाँ हड़प्पा वासियों ने शोरतूघई में व्यापारिक बस्ती बसाई थी।\n2. एमेथिस्ट (Amethyst) और अकीक (Carnelian) का स्रोत दक्कन का पठार और गुजरात के क्षेत्र थे।\n3. जेड (Jade) मध्य एशिया से आयात किया जाता था, जबकि सेलखड़ी राजस्थान से आती थी।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो लाजवर्द, अकीक, जेड और सेलखड़ी के भौगोलिक स्रोतों को स्पष्ट करते हैं।"
    ),
    (
        "सिंधु घाटी में फेयॉन्स (faience) के निर्माण के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. फेयॉन्स बलूचिस्तान की खदानों से निकाला जाने वाला एक प्राकृतिक पत्थर है, जो अपने नीले-हरे रंग के लिए प्रसिद्ध था।\n2. इसे घिसे हुए सिलिका/रेत, गोंद, मिट्टी और रंगीन खनिज लेप के मिश्रण को भट्टी में पकाकर तैयार किया जाता था।\n3. फेयॉन्स एक अत्यधिक कीमती विलासिता की सामग्री थी, जिसका उपयोग सौंदर्य प्रसाधनों के छोटे बर्तनों, मनकों और ताबीजों के निर्माण में होता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 2 और 3", "केवल 2", "केवल 1 और 3", "1, 2 और 3"],
        0,
        "कथन 2 और 3 सही हैं। कथन 1 गलत है: फेयॉन्स एक कृत्रिम/संश्लेषित सामग्री थी, प्राकृतिक खदान से निकाला जाने वाला पत्थर नहीं।"
    ),
    (
        "सोने और चांदी के शिल्पों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. भारत में चांदी का सबसे पहला साक्ष्य हड़प्पा सभ्यता में मिलता है, जहाँ इसका उपयोग बड़े बर्तनों और आभूषणों के लिए किया जाता था।\n2. सोने के आभूषण बारीक मनकों, खोखले स्पैकर्स और लटकनों के रूप में बनाए जाते थे, जिन्हें अक्सर चांदी के साथ मिश्रित (electrum) किया जाता था।\n3. लिपिकों ने सोने की कार्यशालाओं का हिसाब तांबे के फलकों पर दशमलव प्रणाली में दर्ज किया था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि लेखांकन का कोई लिखित साक्ष्य तांबे की पट्टियों पर नहीं मिला है; लिपि अभी भी अपठित है।"
    ),
    (
        "हड़प्पा वासियों के तांबे के उपकरणों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. वे चपटी छेनी, मध्य-पसली वाली तलवारें (mid-ribbed swords), छेद वाली कुल्हाड़ियाँ और मछली पकड़ने के कांटे बनाते थे।\n2. उपकरणों का निर्माण खुली मिट्टी के सांचों में ढलाई और ठंडी घिसाई/हथौड़े से ठोकने की विधियों से किया जाता था।\n3. तांबे के उपकरणों को अधिक कठोर बनाने के लिए उनमें थोड़ी मात्रा में लोहा मिलाया जाता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 2", "केवल 1 और 2", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 2 सही है। कथन 1 गलत है क्योंकि हड़प्पा वासी मध्य-पसली वाली तलवारें या सॉकेट वाली कुल्हाड़ियाँ नहीं बनाते थे; ये तकनीकें बाद के कालों में विकसित हुईं। कथन 3 गलत है क्योंकि लोहा हड़प्पा सभ्यता में पूरी तरह अज्ञात था।"
    ),
    (
        "हड़प्पा शहरों में शिल्प उत्पादन के स्थानिक संगठन (spatial organization) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. कारीगर और शिल्पकार निचले नगर (Lower Town) में स्थित समर्पित बस्तियों में रहते और काम करते थे।\n2. शहर की बाहरी दीवारों के पास मनका पकाने वाली भट्टियों की स्थिति धुएं और आग के खतरों को नियंत्रित करने के नागरिक नियमों को दर्शाती है।\n3. सोने और लाजवर्द जैसी मूल्यवान सामग्रियों का प्रसंस्करण विशेष रूप से प्रशासनिक दुर्ग (Citadel) पर शासक वर्ग के सीधे एकाधिकार में होता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि निचले नगर के आवासीय ब्लॉकों में भी सोने और लाजवर्द के प्रसंस्करण के साक्ष्य मिले हैं, जो दर्शाता है कि कारीगर निचले नगर में काम करते थे।"
    ),
    (
        "सूती वस्त्र शिल्प (cotton textile craft) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. लेखक और व्यापारी हल्के सूती कपड़े पहनते थे, जैसा कि मिट्टी की मुहरबंदियों पर कपड़ों के निशानों से स्पष्ट होता है।\n2. मिट्टी और फेयॉन्स से बने कताई चक्र (spindle whorls) धनी और निर्धन दोनों प्रकार के घरों में पाए गए हैं।\n3. हड़प्पा वासी प्राचीन विश्व में कपास को पालतू बनाने, सूत कातने और बुनने वाले पहले लोग थे।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो कपड़ों के निशान, कताई चक्र और कपास की शुरुआती खेती को स्पष्ट करते हैं।"
    ),
    (
        "हड़प्पा शिल्प में हाथीदांत (ivory) के उपयोग के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. हाथीदांत को तराश कर कंघियाँ, केश सूइयाँ, पासे और मापने के पैमाने बनाए जाते थे।\n2. कच्चा हाथीदांत स्थानीय भारतीय हाथियों से प्राप्त किया जाता था और शहरी कार्यशालाओं में इसका प्रसंस्करण होता था।\n3. हाथीदांत की वस्तुएं विशेष रूप से मेसोपोटामिया को निर्यात करने के लिए आरक्षित थीं और स्थानीय स्तर पर इनका उपयोग प्रतिबंधित था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि हाथीदांत की वस्तुएं स्थानीय घरों में भी प्रचुर मात्रा में मिली हैं, जो घरेलू उपभोग को दर्शाती हैं।"
    ),
    (
        "हड़प्पा के निर्माणकर्ताओं के तकनीकी उपकरणों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. वे कांसा या शंख से बने साहुल (plumb-bobs) और समकोण मापने वाले गुनिया (squares) का उपयोग करते थे।\n2. राजमिस्त्री हाथीदांत, शंख और कांसे की छड़ों पर खुदे हुए मानकीकृत मापने वाले पैमानों का उपयोग करते थे।\n3. लेखकों ने दुर्ग के चबूतरे बनाने से पहले मिट्टी की पट्टियों पर गणितीय ब्लूप्रिंट नक्शे बनाए थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "Clean 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि सिंधु पुरातत्व में कोई भी स्थापत्य ब्लूप्रिंट या नक्शा नहीं मिला है।"
    ),
    (
        "चर्ट ब्लेड (chert blades) के निर्माण के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. सिंध में रोहरी पहाड़ियों (Rohri Hills) से प्राप्त कच्चे माल का उपयोग करके विशिष्ट कार्यशालाओं में चर्ट ब्लेड का बड़े पैमाने पर उत्पादन किया जाता था।\n2. लेखक किसानों को गेहूं और जौ की कटाई के लिए इन चर्ट ब्लेडों का वितरण करते थे।\n3. रोहरी चर्ट कार्यशालाएं कांस्य युग की सबसे बड़ी औद्योगिक खनन खदानों में से एक का प्रतिनिधित्व करती हैं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो रोहरी चर्ट के स्रोत, औजारों के वितरण और खनन के पैमाने का वर्णन करते हैं।"
    ),
    (
        "मृदभांड के लेप और रंगों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. लाल लेप (slip) बनाने के लिए लोहे से समृद्ध लाल गेरू को पानी के साथ मिलाया जाता था।\n2. काला रंग मैंगनीज से समृद्ध खनिज पिगमेंट का उपयोग करके बनाया जाता था।\n3. चमकदार कांच जैसी परत वाले शीशेदार बर्तन (glazed pottery) सभी परिपक्व स्थलों पर बड़े पैमाने पर बनाए जाते थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि कांच जैसी परत वाले बर्तन सिंधु घाटी में अत्यंत दुर्लभ और प्रायोगिक थे, भारत में यह कला बहुत बाद में आई।"
    ),
    (
        "कांस्य की 'नर्तकी' (Dancing Girl) मूर्ति के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह लगभग चार इंच ऊंची एक छोटी मूर्ति है जिसे मोहनजोदड़ो से खोजा गया था।\n2. वह अपने कूल्हे पर एक हाथ रखे खड़ी है और उसकी बाईं भुजा चूड़ियों से पूरी तरह ढकी हुई है।\n3. एस.आर. राव ने रीबस पद्धति का उपयोग करके इस मूर्ति पर उसका नाम 'आदि-द्रविड़ नर्तकी' पढ़ा था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि मूर्ति पर कोई नाम नहीं लिखा मिला है; यह पूरी तरह से बेनाम कलाकृति है।"
    ),
    (
        "हड़प्पा के खिलौना-निर्माण के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. खिलौना निर्माताओं ने धागे से जुड़ी हिलने वाली गर्दन वाले मिट्टी के बैल बनाए थे।\n2. खिलौना गाड़ियों में मौर्य काल की तरह तीलियों वाले पहिये (spoked wheels) बने थे।\n3. पक्षियों के आकार की सीटियाँ मिट्टी के खोखले खिलौने थे जो फूँकने पर आवाज करते थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 3", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 3 सही हैं। कथन 2 गलत है क्योंकि हड़प्पा की खिलौना गाड़ियों के पहिये ठोस (solid) थे, उनमें तीलियाँ (spokes) नहीं थीं। तीलियों वाले पहिये वैदिक काल में आए।"
    ),
    # Additional 30 questions
    (
        "लुप्त-मोम कांस्य ढलाई पद्धति के चरणों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. कलाकार पहले मोम की मूर्ति बनाता था, फिर उसे मिट्टी की परतों से ढकता था।\n2. मिट्टी के सांचे को भट्टी में गर्म किया जाता था, जिससे मोम पिघलकर छोटे निकास द्वारों से बाहर निकल जाता था।\n3. इसके बाद खाली जगह में पिघला हुआ कांसा डाला जाता था, और ठंडा होने पर बाहरी मिट्टी को तोड़कर मूर्ति निकाली जाती थी।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन लुप्त-मोम ढलाई (lost-wax casting) की प्रक्रिया के चरणों को सही ढंग से परिभाषित करते हैं।"
    ),
    (
        "हड़प्पा से प्राप्त 'पुरुष धड़' (Male Torso) पाषाण मूर्ति के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह लाल बलुआ पत्थर से बना है और इसकी शारीरिक यथार्थवादी बनावट के लिए जाना जाता है।\n2. इसमें अलग से सिर और हाथ जोड़ने के लिए सॉकेट छेद बने हैं, जो यह दर्शाता है कि यह एक संयुक्त मूर्ति थी।\n3. यह धड़ छह फीट से अधिक ऊँचा है, जिसे किले के एक सार्वजनिक मंदिर में स्थापित किया गया था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि यह धड़ बहुत छोटा है (लगभग 9 सेमी), यह मंदिर की मूर्ति नहीं बल्कि घरेलू आकार की कलाकृति थी।"
    ),
    (
        "मनका-निर्माण के लिए कच्चे माल के स्रोतों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. अकीक (Carnelian) का आयात गुजरात से किया जाता था और भट्टियों में गर्म करके इसका प्रसंस्करण होता था।\n2. सेलखड़ी (Steatite) का स्रोत उत्तरी राजस्थान और गुजरात के क्षेत्र थे।\n3. लाजवर्द (Lapis Lazuli) का आयात तांबे के औजारों के बदले सीधे मेसोपोटामिया से किया जाता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि लाजवर्द का आयात अफगानिस्तान के बदख्शां (शोरतूघई चौकी) से होता था, मेसोपोटामिया से नहीं।"
    ),
    (
        "शिल्प स्थलों से मिले विशिष्ट ड्रिल बिट्स (drill bits) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. ये ड्रिल बिट्स 'अर्नेस्टाइट' (Ernestite) नामक एक अत्यंत कठोर पत्थर से बने थे।\n2. ये ड्रिल अकीक और जैस्पर जैसे कठोर मनकों में सूक्ष्म छेद करने में सक्षम थे।\n3. चन्हुदड़ो और लोथल से भारी मात्रा में ऐसे ड्रिल बिट्स बरामद हुए हैं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो अर्नेस्टाइट पत्थर, उसकी वेधन क्षमता और प्राप्ति स्थलों का वर्णन करते हैं।"
    ),
    (
        "फेयॉन्स (faience) के निर्माण के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. फेयॉन्स की वस्तुओं पर एक चमकीला, कांच जैसा नीला-हरा लेप होता है जो फ़िरोज़ा की तरह दिखता है।\n2. पकाने से पहले पिसे हुए सिलिका के लेप को छोटे बर्तनों, मनकों और जानवरों की आकृतियों में ढाला जाता था।\n3. फेयॉन्स के निर्माण के लिए उच्च तापमान वाली भट्टियों और रासायनिक ज्ञान की आवश्यकता होती थी, जिससे यह प्रतिष्ठा सूचक सामग्री थी।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं और फेयॉन्स की सुंदरता, घटकों और इसकी प्रतिष्ठा सूचक स्थिति को परिभाषित करते हैं।"
    ),
    (
        "कांस्य की पशु आकृतियों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मोहनजोदड़ो से कांसे के बने सांड और भैंसे की मूर्तियां मिली हैं।\n2. इन आकृतियों को अत्यधिक यथार्थवाद के साथ बनाया गया है, जिसमें मांसलता और त्वचा की परतें दिखाई देती हैं।\n3. इन पशु आकृतियों का उपयोग अनाज मंडियों में मानकीकृत बाटों के रूप में किया जाता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि कांस्य पशु मूर्तियाँ कलात्मक/धार्मिक थीं, जबकि बाट पत्थर (chert) के वर्गाकार टुकड़े होते थे।"
    ),
    (
        "हड़प्पा के बर्तनों के आकारों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. प्रसिद्ध हड़प्पा बर्तनों के रूपों में S-आकार के जार, स्टैंड वाले बर्तन (dish-on-stand) और भंडारण जार शामिल हैं।\n2. छिद्रित जार के ठोस तल को छोड़कर पूरे शरीर पर गोल छेद बने होते थे।\n3. S-आकार के जारों का उपयोग भोजन पकाने के लिए किया जाता था, जैसा कि उनके अंदर जले अवशेषों से पता चलता है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि S-आकार के जार लंबे, सजावटी बर्तन थे जिनका उपयोग भंडारण या उत्सवों में प्रदर्शन के लिए होता था, खाना पकाने के लिए नहीं।"
    ),
    (
        "मिट्टी की चूड़ियों (terracotta bangles) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. पकी मिट्टी की चूड़ियाँ बहुत अधिक मात्रा में मिली हैं, जो दर्शाती हैं कि इन्हें आम लोग पहनते थे।\n2. उच्च गुणवत्ता वाली मिट्टी की चूड़ियों को चमकाकर अकीक के समान लाल रंग में रंगा जाता था।\n3. चूड़ियाँ केवल धातुओं की बनती थीं, और मिट्टी की चूड़ियाँ पहनना पूरी तरह से वर्जित था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["Clean 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि मिट्टी की चूड़ियाँ अत्यंत आम थीं और समाज के बड़े हिस्से द्वारा पहनी जाती थीं।"
    ),
    (
        "सेलखड़ी की मुहरों पर नक्काशी तकनीक के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. नक्काशी करने वाले बारीक छेनी और चर्ट के औजारों से जानवरों के चित्र उकेरते थे।\n2. मुहर के पीछे धागा पिरोने के लिए एक छोटा उठा हुआ छेद वाला बटन (boss) बना होता था।\n3. मुहरों को प्राकृतिक जैविक स्याही से रंगा जाता था ताकि रंगीन व्यापारिक छाप बने।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि मुहरों को रंगा नहीं जाता था; उन्हें केवल भट्टी में पकाकर सफेद चमकीली परत दी जाती थी।"
    ),
    (
        "ईंट के भट्टों (kilns) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. हड़प्पा और अन्य प्रमुख शहरों के बाहरी इलाकों में ईंटें पकाने वाले भट्टे मिले हैं।\n2. भट्टों में पकाने के लिए भारी मात्रा में लकड़ी जलाई जाती थी, जिससे वनों की कटाई को बढ़ावा मिला।\n3. शुरुआती चरणों में हड़प्पा वासी केवल मेसोपोटामिया से आयातित पकी ईंटों का उपयोग करते थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि हड़प्पा वासियों ने अपनी ईंटें स्वयं बनाई थीं, मेसोपोटामिया से ईंट आयात का कोई साक्ष्य नहीं है।"
    ),
    (
        "पुरोहित-राजा (Priest-King) की पाषाण मूर्ति के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह सेलखड़ी (steatite) पत्थर से तराशी गई है और इसकी ऊंचाई लगभग 17 सेमी है।\n2. इसकी आँखें लंबी और ध्यान की मुद्रा में आधी बंद दिखाई देती हैं।\n3. वह दाहिनी बांह पर एक बाजूबंद और सिर पर गोल बटन वाली पट्टी (fillet) पहने है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं और पुरोहित-राजा की मूर्ति के शारीरिक लक्षणों को सही रूप में स्पष्ट करते हैं।"
    ),
    (
        "शंख की पच्चीकारी (shell inlay) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. शंख के टुकड़ों को त्रिकोण, गोल और पंखुड़ियों के रूप में काटकर लकड़ी के फर्नीचर पर सजाया जाता था।\n2. शंख की पच्चीकारी को चिपकाने के लिए प्राकृतिक डामर (bitumen) या राल (resin) का उपयोग होता था।\n3. यह पच्चीकारी तकनीक हड़प्पा जैसे अंतर्देशीय शहरों में भी बहुत लोकप्रिय थी।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो शंख पच्चीकारी के आकारों, गोंद और शहरों में इसके वितरण को स्पष्ट करते हैं।"
    ),
    (
        "मृदभांड के चित्रित डिजाइनों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. चित्रित डिजाइन आमतौर पर लाल पृष्ठभूमि पर काले रंग से बनाए जाते थे।\n2. डिज़ाइनों में अक्सर एक-दूसरे को काटते वृत्त (intersecting circles) दिखाई देते हैं, जो जाल जैसा पैटर्न बनाते हैं।\n3. डिजाइनों में राजाओं के राज्याभिषेक और युद्धों के विस्तृत ऐतिहासिक दृश्य चित्रित हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि हड़प्पा के बर्तनों पर ज्यामितीय और पशु चित्र हैं, लेकिन राजाओं या युद्धों के कोई ऐतिहासिक दृश्य नहीं हैं।"
    ),
    (
        "मानकीकृत बाटों (weights) के निर्माण के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. बाटों को उच्च गुणवत्ता वाले चर्ट पत्थर को काटकर चौकोर घनों के रूप में पॉलिश किया जाता था।\n2. कम वजन के मान द्वि-आधारी श्रृंखला (binary series - 1, 2, 4, 8, 16, 32) में आगे बढ़ते थे।\n3. बाटों का निर्माण प्रत्येक व्यापारी अपनी मर्जी से करता था और नगर प्रशासन का इन पर कोई नियंत्रण नहीं था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "Clean 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि पूरे सिंधु क्षेत्र में बाटों की अत्यधिक शुद्धता और मानकीकरण कड़े नागरिक नियंत्रण को प्रमाणित करता है।"
    ),
    (
        "सोने के आभूषणों के संग्रहों (hoards) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. घरों के फर्श के नीचे दबे कांसे या चांदी के बर्तनों में सोने के आभूषणों के संग्रह मिले हैं।\n2. सोने के आभूषणों में सिर की पट्टियाँ, बाजूबंद, हार और सूक्ष्म मनके शामिल हैं।\n3. सोने के इन संग्रहों की उपस्थिति शहरों में धन संचय और निजी बचत की प्रवृत्ति को दर्शाती है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो सोने के होर्ड्स, आभूषणों के प्रकार और आर्थिक पहलुओं को स्पष्ट करते हैं।"
    ),
    (
        "तांबे के मछली पकड़ने के कांटों (fish hooks) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. तटीय और नदी किनारे के स्थलों से भारी मात्रा में तांबे के कांटे मिले हैं।\n2. इन कांटों में मुड़े हुए हुक और नोक (barb) बनी है, जो उन्नत पकड़ तकनीक को दर्शाती है।\n3. ये कांटे दर्शाते हैं कि मछली पकड़ना सिंधु सभ्यता में एक प्रमुख आहार और आजीविका थी।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो तांबे के हुक की बनावट और आजीविका में मछली पकड़ने के महत्व को स्पष्ट करते हैं।"
    ),
    (
        "सेलखड़ी के पेस्ट के मनकों (steatite paste beads) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. सेलखड़ी के चूरे को गोंद के साथ मिलाकर पेस्ट बनाया जाता था और फिर उसे बेलनाकार धागे पर लपेटा जाता था।\n2. पेस्ट के मनकों को भट्टी में पकाकर चमकाया जाता था, जिससे सूक्ष्म मनकों का बड़े पैमाने पर उत्पादन संभव हुआ।\n3. ये मनके इतने भारी होते थे कि इन्हें केवल माल ढोने वाले बैल ही पहनते थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि ये सूक्ष्म मनके (micro-beads) अत्यंत हल्के और बारीक होते थे जिन्हें मनुष्य आभूषणों के रूप में पहनते थे।"
    ),
    (
        "मिट्टी के खिलौना जानवरों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मिट्टी के बने सांडों में अक्सर एक बड़ा कूबड़ (hump) और सुंदर सींग बने होते थे।\n2. धागे के सहारे ऊपर-नीचे सरकने वाले मिट्टी के बंदर मिले हैं, जो गतिज खिलौनों के डिज़ाइन को दर्शाते हैं।\n3. खिलौना गाड़ियाँ सबसे आम खिलौने हैं, जिनमें ठोस पहिये लगे मिले हैं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो मिट्टी के सांड, सरकने वाले बंदर और ठोस पहियों वाली खिलौना गाड़ियों का वर्णन करते हैं।"
    ),
    (
        "मृदभांड भट्टी (pottery kiln) के तापमान के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. हड़प्पा के कुम्हारों के भट्टी का तापमान 800°C से 1000°C तक पहुँच जाता था।\n2. उच्च तापमान के कारण अत्यंत मजबूत और टिकाऊ मृदभांड तथा टेराकोटा का निर्माण संभव हुआ।\n3. तकनीक को गुप्त रखने के लिए भट्टियाँ किले (Citadel) के अंदर राजमहलों में बनाई जाती थीं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि भट्टियाँ कच्चे माल के पास नगर के बाहरी इलाकों या निचले नगर में स्थित थीं, महलों में नहीं।"
    ),
    (
        "कच्ची धातुओं की प्राप्ति के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. तांबा राजस्थान की खेतड़ी खानों और बलूचिस्तान से प्राप्त किया जाता था।\n2. तांबे में मिलाने के लिए टिन का आयात अफगानिस्तान और मध्य एशिया से किया जाता था।\n3. लोहा छोटानागपुर पठार की खदानों से प्रचुर मात्रा में निकाला जाता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि कांस्य युगीन हड़प्पा सभ्यता में लोहा पूरी तरह से अज्ञात था।"
    ),
    (
        "चर्ट ब्लेड (Rohri chert blades) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. रोहरी चर्ट अपने उच्च गुणवत्ता वाले, पीले-भूरे रंग के लिए जाना जाता है।\n2. ब्लेडों का निर्माण दवाब-फ्लेकिंग (pressure-flaking) तकनीक से किया जाता था।\n3. ये ब्लेड परिपक्व चरण में लगभग हर हड़प्पा शहरी घर में पाए गए हैं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन चर्ट ब्लेड के रंग, निर्माण विधि और शहरी उपलब्धता को सही रूप में स्पष्ट करते हैं।"
    ),
    (
        "शोरतूघई में लाजवर्द प्रसंस्करण (lapis lazuli processing) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. शोरतूघई पूर्वोत्तर अफगानिस्तान में स्थापित एक हड़प्पा व्यापारिक चौकी थी।\n2. यहाँ के निवासी बदख्शां की पहाड़ियों से सीधे लाजवर्द निकालते थे और उनके कच्चे मनके बनाते थे।\n3. शोरतूघई को साइबेरियाई खानाबदोश जनजातियों के हमलों से लाजवर्द बचाने के लिए किलेबंद किया गया था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि शोरतूघई खनन मार्ग पर व्यापारिक बस्ती थी, साइबेरियाई हमलों का कोई पुरातात्विक साक्ष्य नहीं है।"
    ),
    (
        "शंख की चूड़ियाँ बनाने की प्रक्रिया के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. कारीगर कांसे की घुमावदार आरी से शंख के शिखरों को काटते थे।\n2. कटे हुए छल्ले को बलुआ पत्थर की घिसाई शिलाओं पर पॉलिश किया जाता था।\n3. तैयार चूड़ियों पर अक्सर V-आकार (chevron) का डिज़ाइन उकेरा जाता था।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन शंख काटने, चमकाने और चूड़ी के V-डिजाइन की प्रक्रिया को सही रूप में स्पष्ट करते हैं।"
    ),
    (
        "मिट्टी की मातृदेवी (Mother Goddess) मूर्तियों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इन्हें उंगलियों से पिंच करके (pinching method) चेहरे के हाव-भाव दिए जाते थे।\n2. इनकी आँखें मिट्टी की गोल गोलियों को चेहरे पर चिपकाकर बनाई जाती थीं (coffee-bean eyes)।\n3. ये मूर्तियाँ विशेष रूप से किले के प्रशासनिक गोदामों में ही सुरक्षित रखी जाती थीं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि मातृदेवी की मूर्तियां निचले नगर के आम घरों से मिली हैं, जो घरेलू पूजा का साक्ष्य हैं।"
    ),
    (
        "कांस्य नर्तकी (Dancing Girl) के शारीरिक लक्षणों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. वह तीन लटकनों वाला एक हार पहने है और उसके बाल जूड़े में बंधे हैं।\n2. उसकी बाईं बांह 24 से 25 चूड़ियों से पूरी तरह ढकी हुई है।\n3. मूर्ति को मिस्र के फिरौन की मूर्तियों की तरह एक कड़े, औपचारिक धार्मिक मुद्रा में खड़ा दिखाया गया है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["Clean 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि मूर्ति अपने लचीले और सहज नृत्य मुद्रा (त्रिभंग जैसी मुद्रा) के लिए प्रसिद्ध है, यह मिस्र की तरह कठोर नहीं है।"
    ),
    (
        "मृदभांड के लेप और चित्रकारी के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. बर्तनों पर चढ़ाया जाने वाला लाल लेप जलोढ़ मिट्टी और आयरन ऑक्साइड (गेरू) से बनता था।\n2. काले रंग की चित्रकारी बिना पके बर्तन पर जानवरों के बालों के ब्रश से की जाती थी।\n3. लेखक सभी बड़े निर्यात जारों के गले पर छोटी कहानियों के रूप में लेख लिखते थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि बर्तनों पर कहानियाँ या बड़े लेख नहीं मिलते; केवल संक्षिप्त भित्तिचित्र या मुहरें मिलती हैं।"
    ),
    (
        "लाल धड़ (Red Torso) पाषाण मूर्ति के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह मूर्ति पुरातत्वविद एम.एस. वत्स द्वारा हड़प्पा से खोजी गई थी।\n2. यह मूर्ति यथार्थवादी पेट की बनावट और मानव शरीर रचना की गहरी समझ को दर्शाती है।\n3. यह धड़ एक बड़े बलुआ पत्थर के स्तंभ के किनारे उभरी हुई नक्काशी (relief) के रूप में बनाया गया है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 and 2 सही हैं। कथन 3 गलत है क्योंकि यह एक त्रि-आयामी स्वतंत्र मूर्ति है, स्तंभ पर उभरी नक्काशी नहीं।"
    ),
    (
        "मिट्टी की खिलौना गाड़ियों के निर्माण के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. ये गाड़ियां खेतों से अनाज ढोने वाली वास्तविक बैलगाड़ियों के डिज़ाइन पर आधारित थीं।\n2. खिलौना गाड़ी के फ्रेम में लकड़ी के डंडे डालने के लिए छेद बने होते थे जो धुरी का काम करते थे।\n3. पहियों में घर्षण कम करने के लिए पेड़ों की राल (resin) से बनी रबर जैसी टायर चढ़ाई जाती थी।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि पहिये पूरी तरह से ठोस मिट्टी या लकड़ी के होते थे, उन पर कोई रबर या राल नहीं चढ़ाई जाती थी।"
    ),
    (
        "सेलखड़ी मुहरों के आकारों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. अधिकांश मुहरें 2 से 4 सेमी लंबाई वाली छोटी वर्गाकार प्लेटें हैं।\n2. आयताकार मुहरें भी आम हैं जिन पर केवल लेख हैं और कोई पशु चित्र नहीं हैं।\n3. बाजारों में राजकीय करों को प्रदर्शित करने के लिए एक मीटर से बड़े आकार की मुहरें लगाई जाती थीं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि सिंधु सभ्यता में कोई बड़ी या विशाल मुहरें नहीं मिली हैं; सभी मुहरें हाथ में रखने योग्य थीं।"
    ),
    (
        "कांस्य के उपकरणों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. जटिल आकारों के लिए द्वि-आधारी पत्थर के सांचों (two-part molds) का उपयोग करके उपकरण ढाले जाते थे।\n2. तांबे की आरी में दांतों को टेढ़ा (offset teeth) सेट किया जाता था ताकि लकड़ी काटते समय आरी फंसे नहीं।\n3. हड़प्पा वासियों के पास युद्ध के लिए विशेष धातु के हेलमेट और कवच (body armor) थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि हड़प्पा वासी एक शांतिप्रिय व्यापारिक समाज थे और उनके पास किसी भी प्रकार के धातु के सैनिक कवच या हेलमेट नहीं मिले हैं।"
    )
]

# Mock Test Questions (10 Qs) - UPSC Prelims Standard Multi-Statement
mock_data_eng = [
    (
        "Consider the following statements regarding the lost-wax bronze casting technique:\n1. It was utilized to manufacture solid metal sculptures like the Dancing Girl and hollow bull figurines.\n2. The technique involved modeling a wax figure, covering it with clay, melting the wax, and filling the void with molten metal.\n3. The lost-wax technique was unique to the Indus Valley and was not practiced in ancient Mesopotamia.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: lost-wax casting was also used in ancient Mesopotamia and Egypt during the Bronze Age."
    ),
    (
        "With reference to the stone sculpture of the Mature Harappan phase, consider the following statements:\n1. The steatite Priest-King statue shows a patterned shawl draped over the left shoulder, leaving the right arm free.\n2. The red sandstone male torso from Harappa features socket holes, indicating it was part of a composite assembly.\n3. These stone sculptures were carved on a monumental scale for public temple worship.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: Harappan stone sculptures are small, domestic art pieces, not monumental public temple installations."
    ),
    (
        "Consider the following statements regarding the manufacture of Harappan seals:\n1. Steatite seals were carved in reverse (negative) layout so that stamped sealings would display positive relief.\n2. Carved seals were heated in kilns to whiten and harden the soft steatite stone.\n3. The majority of square seals carry animal figures alongside brief script characters.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, describing reverse carving, heat-hardening, and common motifs of steatite seals."
    ),
    (
        "With reference to the shell-working industry, consider the following statements:\n1. Specialized workshops have been excavated at coastal Nageshwar and Balakot.\n2. Artisans manufactured shell bangles, rings, and inlays using curved bronze saws.\n3. The shell products were strictly limited to coastal sites and never reached inland cities.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "2 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: shell products were exported in large numbers to inland capitals like Harappa and Mohenjo-daro."
    ),
    (
        "Consider the following statements regarding the raw material sourcing for crafts:\n1. Lapis Lazuli was imported from Badakhshan in Afghanistan, where the Harappans set up a colony at Shortughai.\n2. Copper was imported from the Khetri mines of Rajasthan and tin from Afghanistan.\n3. Jade was imported from Gujarat, and Carnelian from Central Asia.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: Jade was imported from Central Asia/Pamir region, and Carnelian was sourced from Gujarat, not vice versa."
    ),
    (
        "With reference to the manufacture of faience, consider the following statements:\n1. Faience is a synthetic material produced by firing silica sand mixed with gum and mineral glaze.\n2. The blue-green glassy faience was a luxury material used for miniature jars and beads.\n3. Faience was easily manufactured in rural households using low-temperature open hearths.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "2 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: faience required high temperatures (above 900°C) and advanced kiln technology, restricting its manufacture to specialized urban craft guilds."
    ),
    (
        "Consider the following statements regarding Harappan brick technology:\n1. Sun-dried and kiln-baked bricks maintained a highly standardized size ratio of 4:2:1.\n2. Kiln-baked bricks were reserved for structures exposed to water, like public baths and sewers.\n3. The uniformity of brick sizes across thousands of kilometers suggests centralized municipal regulations.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All three statements are correct, describing brick ratios, usage, and civic standardization."
    ),
    (
        "With reference to the pottery painted slip and design motifs, consider the following statements:\n1. Potters painted designs in black manganese pigment over a bright red ochre slip.\n2. Common designs depict intersecting circles, pipal leaves, and fish scales.\n3. The pottery designs depict royal battles and narrative scenes of historical rulers.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: pottery designs are geometric, floral, and faunal, lacking any narrative historical scenes of kings or battles."
    ),
    (
        "Consider the following statements regarding the bead factories at Chanhudaro:\n1. Excavations revealed bead-making platforms, grinding stones, and carnelian-heating kilns.\n2. Artisans utilized specialized chert micro-drills made of Ernestite to bore gemstone beads.\n3. Chanhudaro was a heavily fortified administrative capital with a grand royal palace.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: Chanhudaro was an unfortified industrial suburb completely lacking a citadel or palace mounds."
    ),
    (
        "With reference to the metallurgical copper tools, consider the following statements:\n1. Harappans manufactured flat chisels, knives, fish hooks, and saws with offset teeth.\n2. They did not manufacture mid-ribbed swords or socketed axes, which appeared later.\n3. Scribes recorded metallurgy formulas on copper tablets using a phonetic alphabet.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: no metallurgical formulas or writing plaques are deciphered, and the script remains undeciphered."
    )
]

mock_data_hin = [
    (
        "लुप्त-मोम कांस्य ढलाई तकनीक के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इसका उपयोग कांस्य नर्तकी (Dancing Girl) जैसी ठोस धातु की मूर्तियों और बैल की खोखली मूर्तियों को बनाने में होता था।\n2. इस तकनीक में मोम की मूर्ति बनाना, उसे मिट्टी से ढकना, गर्म करके मोम को निकालना और खाली जगह में पिघली धातु भरना शामिल था।\n3. यह तकनीक केवल सिंधु घाटी की अनूठी विशेषता थी और प्राचीन मेसोपोटामिया में इसका अभ्यास नहीं होता था।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: कांस्य युग के दौरान प्राचीन मेसोपोटामिया और मिस्र में भी लुप्त-मोम पद्धति (lost-wax casting) का अभ्यास किया जाता था।"
    ),
    (
        "परिपक्व हड़प्पा काल की पाषाण मूर्तिकला के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. पुरोहित-राजा की मूर्ति में बाएं कंधे पर तिपतियाPattern वाला शॉल ओढ़े दिखाया गया है, जिससे दाहिना हाथ स्वतंत्र रहता है।\n2. हड़प्पा से प्राप्त लाल बलुआ पत्थर के पुरुष धड़ में सॉकेट छेद हैं, जो दर्शाता है कि यह एक संयुक्त मूर्ति का हिस्सा था।\n3. ये पाषाण मूर्तियां सार्वजनिक मंदिरों में पूजा के लिए विशाल पैमाने पर बनाई गई थीं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: हड़प्पा की पाषाण मूर्तियां आकार में छोटी, घरेलू कलाकृतियां हैं, न कि विशाल सार्वजनिक मंदिर की मूर्तियां।"
    ),
    (
        "हड़प्पा की मुहरों के निर्माण के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मुहरों को विपरीत (negative) रूप में खोदा जाता था ताकि मिट्टी की मुहरबंदियों पर छाप सीधी (positive) दिखाई दे।\n2. तराशी गई मुहरों को भट्टी में पकाया जाता था ताकि सेलखड़ी पत्थर सफेद और कठोर हो जाए।\n3. अधिकांश वर्गाकार मुहरों पर पशु चित्रों के साथ संक्षिप्त लिपि चिन्ह अंकित हैं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो विपरीत नक्काशी, भट्टी में पकाने और मुहरों के मुख्य डिज़ाइनों का वर्णन करते हैं।"
    ),
    (
        "शंख-शिल्प (shell-working) उद्योग के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. समुद्र तटीय नागेश्वर और बालाकोट से शंख निर्माण की विशिष्ट कार्यशालाएं प्राप्त हुई हैं।\n2. कारीगर कांसे की घुमावदार आरी का उपयोग करके शंख की चूड़ियाँ, छल्ले और पच्चीकारी का सामान बनाते थे।\n3. शंख के उत्पाद केवल तटीय क्षेत्रों तक ही सीमित थे और कभी भी अंतर्देशीय शहरों तक नहीं पहुँचे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 2", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: शंख के उत्पाद भारी मात्रा में हड़प्पा और मोहनजोदड़ो जैसे अंतर्देशीय शहरों को भेजे जाते थे।"
    ),
    (
        "शिल्प के लिए कच्चे माल के स्रोतों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. लाजवर्द (Lapis Lazuli) का आयात अफगानिस्तान के बदख्शां से होता था, जहाँ हड़प्पा वासियों ने शोरतूघई में व्यापारिक चौकी बसाई थी।\n2. तांबा राजस्थान की खेतड़ी खानों से और टिन अफगानिस्तान से आयात किया जाता था।\n3. जेड (Jade) का आयात गुजरात से और अकीक (Carnelian) का आयात मध्य एशिया से होता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: जेड का आयात मध्य एशिया से और अकीक का स्रोत गुजरात था।"
    ),
    (
        "फेयॉन्स (faience) के निर्माण के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. फेयॉन्स एक कृत्रिम सामग्री है जो गोंद और खनिज लेप के साथ मिश्रित सिलिका रेत को भट्टी में पकाकर बनाई जाती है।\n2. इस नीले-हरे चमकीले फेयॉन्स का उपयोग सौंदर्य प्रसाधनों की शीशियों और मनकों के निर्माण में होता था।\n3. फेयॉन्स का निर्माण ग्रामीण घरों में कम तापमान वाली खुली अंगीठियों में आसानी से किया जाता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 2", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: फेयॉन्स के लिए उच्च तापमान और भट्टी तकनीक की आवश्यकता होती थी, जो शहरी शिल्प संघों तक सीमित थी।"
    ),
    (
        "हड़प्पा की ईंट निर्माण तकनीक के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. धूप में सुखाई गई और भट्टी में पकाई गई ईंटें 4:2:1 के अत्यधिक मानकीकृत अनुपात में थीं।\n2. पक्की ईंटें उन संरचनाओं के लिए आरक्षित थीं जो पानी के सीधे संपर्क में आती थीं, जैसे सार्वजनिक स्नानगृह और नालियां।\n3. हजारों किलोमीटर में ईंटों के आकार में यह समानता एक सुव्यवस्थित नागरिक या नगरपालिका प्रशासन का संकेत देती है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो ईंट अनुपात, उनके उपयोग और नागरिक मानकीकरण को स्पष्ट करते हैं।"
    ),
    (
        "मृदभांड के लेप और चित्रित डिज़ाइनों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. कुम्हार लाल गेरू के लेप के ऊपर काले रंग के मैंगनीज पिगमेंट से चित्रकारी करते थे।\n2. सामान्य डिज़ाइनों में एक-दूसरे को काटते वृत्त, पीपल के पत्ते और मछली के शल्क चित्रित हैं।\n3. मृदभांड के चित्र शाही युद्धों और ऐतिहासिक राजाओं की कहानियों को दर्शाते हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["Clean 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि बर्तनों पर ज्यामितीय, वनस्पति और पशु चित्र हैं, राजाओं या युद्धों के ऐतिहासिक दृश्य नहीं हैं।"
    ),
    (
        "चन्हुदड़ो के मनका कारखानों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. उत्खनन से मनका बनाने के चबूतरे, घिसाई पत्थर और अकीक पकाने वाली भट्टियाँ मिली हैं।\n2. शिल्पकार रत्नों में छेद करने के लिए अर्नेस्टाइट पत्थर से बने विशिष्ट चर्ट सूक्ष्म-ड्रिल का उपयोग करते थे।\n3. चन्हुदड़ो एक सुदृढ़ रक्षा प्राचीर से घिरा प्रशासनिक मुख्यालय था जहाँ एक भव्य राजमहल था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि चन्हुदड़ो बिना किलेबंदी या महल वाला एक समर्पित औद्योगिक शिल्प उपनगर था।"
    ),
    (
        "तांबे के धात्विक उपकरणों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. हड़प्पा वासी चपटी छेनी, चाकू, मछली पकड़ने के कांटे और टेढ़े दांतों वाली आरी बनाते थे।\n2. वे मध्य-पसली वाली तलवारें या छेद वाली कुल्हाड़ियाँ नहीं बनाते थे, जो बाद के युग में आईं।\n3. लेखकों ने धातुकर्म के सूत्रों को तांबे की पट्टियों पर एक वर्णमाला लिपि में दर्ज किया था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि धातुकर्म के कोई सूत्र नहीं मिले हैं और लिपि अभी तक अपठित है।"
    )
]

# Write Practice Questions
for item in practice_data_eng:
    eng_data["practiceQuestions"].append({
        "q": item[0],
        "opts": item[1],
        "ans": item[2],
        "sol": item[3]
    })

for item in practice_data_hin:
    hin_data["practiceQuestions"].append({
        "q": item[0],
        "opts": item[1],
        "ans": item[2],
        "sol": item[3]
    })

# Write Mock Test Questions
for item in mock_data_eng:
    eng_data["mockTestQuestions"].append({
        "q": item[0],
        "opts": item[1],
        "ans": item[2],
        "sol": item[3]
    })

for item in mock_data_hin:
    hin_data["mockTestQuestions"].append({
        "q": item[0],
        "opts": item[1],
        "ans": item[2],
        "sol": item[3]
    })

# Save JSON Files (Without Mastery Zone Questions for now)
with open(os.path.join(ENG_DIR, "content.json"), "w", encoding="utf-8") as f:
    json.dump(eng_data, f, ensure_ascii=False, indent=2)

with open(os.path.join(HIN_DIR, "content.json"), "w", encoding="utf-8") as f:
    json.dump(hin_data, f, ensure_ascii=False, indent=2)

print("Crafts Base JSON files built successfully!")
