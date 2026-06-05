import json
import os

ENG_DIR = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\HarappanIndus-Valley-Civilisation\Agriculture"
HIN_DIR = os.path.join(ENG_DIR, "hi")
os.makedirs(HIN_DIR, exist_ok=True)

# English base structure
eng_data = {
    "breadcrumbs": {
        "parent": "UPSC Syllabus",
        "parentUrl": "/upsc/",
        "current": "Harappan Agriculture"
    },
    "hero": {
        "title": "Harappan Agriculture & Food Economy",
        "description": "Examine the crop systems, animal husbandry, advanced hydraulic irrigation, granary storage, and subsistence economy of the Indus Valley Civilisation for UPSC GS-1."
    },
    "labels": {
        "clickToExpand": "Click to expand details",
        "mockIntro": {
            "title": "Interactive UPSC Mock Test",
            "description": "Test your grasp on Harappan farming techniques, irrigation outposts, and domestic animal assemblages. This timed mock test contains 10 high-yield, exam-standard questions with negative marking.",
            "startBtn": "Start Mock Test"
        },
        "mockPlay": {
            "prevBtn": "Previous Question",
            "nextBtn": "Next Question",
            "submitBtn": "Submit Test"
        }
    },
    "timeline": {
        "title": "Evolution of Harappan Subsistence",
        "description": "Chronological trajectory of farming, pastoralism, and grain storage systems.",
        "cards": [
            {
                "period": "Early Harappan Agriculture",
                "date": "c. 3300 BCE - 2600 BCE",
                "details": "Development of village-based farming, early animal domestication (zebu cattle, sheep), and the initiation of ploughed field technology at Kalibangan."
            },
            {
                "period": "Mature Harappan Agrarian Surplus",
                "date": "c. 2600 BCE - 1900 BCE",
                "details": "High-yield double-cropping, specialized irrigation canals at Shortughai, massive water reservoirs at Dholavira, and state-managed granary networks to feed urban centers."
            },
            {
                "period": "Late Harappan Desiccation",
                "date": "c. 1900 BCE - 1300 BCE",
                "details": "Shift in monsoon patterns, drying up of the Ghaggar-Hakra system, soil salinization, and decline of agricultural surplus, leading to urban de-population."
            }
        ]
    },
    "mnemonics": {
        "title": "Mnemonics & Memory Hacks",
        "description": "Visual triggers to memorize key crops, animals, and irrigation systems for UPSC.",
        "items": [
            {
                "title": "Mnemonic 1: Major Rabi Crops Cultivated",
                "phrase": "\"W-B-P-M-S (Wheat, Barley, Peas, Mustard, Sesame)\"",
                "decryption": "Remember the primary winter crop suite: **W**heat, **B**arley, **P**eas, **M**ustard, **S**esame."
            },
            {
                "title": "Mnemonic 2: Controversial Animal & Sourcing",
                "phrase": "\"Sur-Horse-Loth-Rice (Surkotada-Horse, Lothal-Rice)\"",
                "decryption": "Key archaeological debates: **Sur**kotada is associated with the controversial **horse** bones; **Loth**al (and Rangpur) yielded evidence of **rice** husks."
            },
            {
                "title": "Mnemonic 3: Specialized Water Management Sites",
                "phrase": "\"Short-Canal, Dhol-Reservoir, Bal-Dam (Shortughai-Canal, Dholavira-Reservoir, Baluchistan-Dam/Gabarband)\"",
                "decryption": "Remember irrigation architecture: **Short**ughai has **canals**; **Dhol**avira has stone **reservoirs**; **Bal**uchistan has stream check **dams** (Gabarbands)."
            }
        ]
    },
    "flashcards": {
        "title": "Active Recall Flashcards",
        "description": "Test your memory on crucial Harappan agrarian discoveries and debates.",
        "items": [
            {
                "question": "Which site provides the earliest direct evidence of a ploughed field showing grid furrows?",
                "answer": "<strong>Kalibangan</strong> in Rajasthan. The field shows two sets of furrows crossing at right angles, suggesting double-cropping (growing two different crops simultaneously).",
                "icon": "fa-tractor"
            },
            {
                "question": "Where were terracotta models of ploughshares discovered?",
                "answer": "At <strong>Banawali</strong> (Haryana) and <strong>Jawariwala / Cholistan</strong> (Pakistan), confirming the shape and use of functional wooden ploughshares.",
                "icon": "fa-screwdriver-wrench"
            },
            {
                "question": "Why are canals absent from the main alluvial plains of Sindh and Punjab?",
                "answer": "Because the high-silt river floods of the Indus and its tributaries filled up and buried ancient canals over centuries, leaving only wells and flood-basin inundation.",
                "icon": "fa-water"
            },
            {
                "question": "What does the Greek word 'Sindon' refer to, and what is its origin?",
                "answer": "It refers to <strong>cotton</strong>. The Greeks called it 'Sindon' because it was produced in the Indus valley (derived from the word 'Sindhu').",
                "icon": "fa-shirt"
            },
            {
                "question": "Which site has yielded controversial skeletal remains of a horse?",
                "answer": "<strong>Surkotada</strong> in Gujarat. Although horse bones are reported here, the horse is not depicted on seals, and its domestication is highly debated.",
                "icon": "fa-horse"
            }
        ]
    },
    "deepDive": {
        "title": "Syllabus Core Study Notes (Deep-Dive)",
        "description": "Master the agrarian foundations, technology, and economic distribution systems of the Indus valley.",
        "sections": [
            {
                "title": "1. Crops and Animal Domestication",
                "content": """<p>Harappan agriculture was highly diversified, providing the essential food surplus that supported large urban populations in the Indus valley.</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-seedling"></i> Crop Suite & Cultivation Pattern</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>Principal Crops:</strong> Wheat (bread and club wheat) and barley (two-row and six-row) were the main staples. Peas, mustard, chickpeas, lentils, and sesame were also grown.</li>
      <li><strong>Fiber & Rice:</strong> The Harappans were pioneers in cultivating <strong>cotton</strong>, which Greeks termed <em>Sindon</em>. Rice was rare, with husks only found in Gujarat (Lothal, Rangpur).</li>
      <li><strong>Millets:</strong> Millets (ragi, kodon, jowar) were cultivated in Gujarat, showing adaptation to dry-crop regimes.</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-cow"></i> Animal Husbandry & Domestication</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>Domesticates:</strong> Humped cattle (zebu/<em>Bos indicus</em>) were highly prized, along with water buffaloes, sheep, goats, pigs, camels, and asses.</li>
      <li><strong>The Horse Controversy:</strong> While horse bones were identified at Surkotada, the horse is completely absent from seals and terracotta art. Most historians agree it was not domesticated or widely used.</li>
      <li><strong>Wild Game:</strong> Bone deposits show they hunted or encountered wild animals like rhinoceros, elephants, deer, and gharials.</li>
    </ul>
  </div>
</div>""",
                "masteryZone": []
            },
            {
                "title": "2. Agricultural Technology and Irrigation",
                "content": """<p>Harappans utilized advanced tools and hydraulic engineering to cultivate the fertile but flood-prone alluvial soils.</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-compass"></i> Tillage and Harvesting Tools</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>Plough Agriculture:</strong> Direct evidence of a ploughed field with grid furrows exists at <strong>Kalibangan</strong>. Terracotta plough models from <strong>Banawali</strong> and Cholistan confirm that wooden ploughshares were used.</li>
      <li><strong>Harvesting:</strong> Chert blades set in wooden handles were used as sickles to harvest grains. Metal sickles of copper or bronze were rare.</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-faucet-drip"></i> Irrigation Systems</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>Canals:</strong> Absent in the main Indus plain due to heavy silting. However, a stone-lined canal network was discovered at <strong>Shortughai</strong> in northern Afghanistan.</li>
      <li><strong>Reservoirs & Dams:</strong> <strong>Dholavira</strong> features massive stone-cut reservoirs to store rainwater. Hilly areas of Baluchistan utilized stone check dams called <strong>Gabarbands</strong>.</li>
      <li><strong>Wells:</strong> Hundreds of brick-lined wells (like the ones at Mohenjo-daro) supplied water for both household and small-plot cultivation.</li>
    </ul>
  </div>
</div>""",
                "masteryZone": []
            },
            {
                "title": "3. Food Storage, Granaries and Decline",
                "content": """<p>The management of food surplus and its long-term vulnerability to environmental shifts were key to the rise and fall of the Indus cities.</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-warehouse"></i> Storage Systems & State Control</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>Granaries:</strong> The **Great Granary** at Mohenjo-daro (a massive brick platform with timber sockets) and the six granaries in a row at Harappa acted as public food reserves.</li>
      <li><strong>Threshing Floors:</strong> Circular brick platforms at Harappa next to the granaries contained traces of wheat and barley, indicating central threshing areas.</li>
      <li><strong>Taxation & Tribute:</strong> Food surplus was transported in bullock carts from rural hinterlands to cities, likely collected as tax or tribute by the state.</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-cloud-sun-rain"></i> Climate Change and Agrarian Collapse</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>Monsoon Shift:</strong> Around 1900 BCE, a general weakening of the summer monsoon reduced agricultural yields in the core Indus region.</li>
      <li><strong>Hydrological Changes:</strong> The migration and drying up of rivers (like the Ghaggar-Hakra) caused severe water scarcity, while tectonic shifts led to devastating floods in Sindh.</li>
      <li><strong>Desubstantation:</strong> The decline of agricultural surplus made it impossible to support large city populations, causing people to migrate east to Gujarat and UP.</li>
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
            "<strong>Trap 1:</strong> Do not choose options claiming that the Harappans cultivated sugarcane or tea. These crops were completely unknown to them.",
            "<strong>Trap 2:</strong> Watch out for statements claiming that iron ploughshares were used. The Harappans were in the **Bronze Age** and had no knowledge of iron; they used wooden ploughs.",
            "<strong>Trap 3:</strong> Do not assume that rice was the main staple crop. Rice husks are only found at Lothal and Rangpur; wheat and barley were the primary staples.",
            "<strong>Trap 4:</strong> Be careful with statements stating that horse domestication was central to Harappan farming. The horse is not depicted on seals, and its presence is highly debated.",
            "<strong>Trap 5:</strong> Do not assume canals were the primary irrigation method in Punjab/Sindh. Canals are absent in the main plains; **wells and seasonal floods** were the main water sources."
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
        "current": "हड़प्पा कृषि"
    },
    "hero": {
        "title": "हड़प्पा कृषि और खाद्य अर्थव्यवस्था",
        "description": "सिंधु घाटी सभ्यता की फसल प्रणालियों, पशुपालन, उन्नत सिंचाई प्रणालियों, अनाज भंडारण और आर्थिक आधार का अध्ययन करें।"
    },
    "labels": {
        "clickToExpand": "विवरण देखने के लिए क्लिक करें",
        "mockIntro": {
            "title": "इंटरैक्टिव परीक्षा मॉक टेस्ट",
            "description": "हड़प्पा कृषि तकनीकों, सिंचाई प्रणालियों और पालतू पशुओं से जुड़े विवरणों का परीक्षण करें। इस समयबद्ध मॉक टेस्ट में नकारात्मक अंकन के साथ 10 उच्च स्तरीय यूपीएससी मानक प्रश्न शामिल हैं।",
            "startBtn": "मॉक टेस्ट शुरू करें"
        },
        "mockPlay": {
            "prevBtn": "Previous Question",
            "nextBtn": "Next Question",
            "submitBtn": "Submit Test"
        }
    },
    "timeline": {
        "title": "हड़प्पा कृषि का विकास",
        "description": "कृषि, पशुपालन और अनाज भंडारण प्रणालियों के विकास की समयरेखा।",
        "cards": [
            {
                "period": "प्रारंभिक हड़प्पा कृषि",
                "date": "लगभग 3300 ईसा पूर्व - 2600 ईसा पूर्व",
                "details": "ग्रामीण स्तर पर खेती का विकास, पशुपालन (कूबड़ वाले बैल, भेड़) की शुरुआत और कालीबंगन में जुते हुए खेत की तकनीक का विकास।"
            },
            {
                "period": "परिपक्व हड़प्पा कृषि अधिशेष",
                "date": "लगभग 2600 ईसा पूर्व - 1900 ईसा पूर्व",
                "details": "दोहरी फसल प्रणाली, शोर्तुघई में सिंचाई नहरें, धोलावीरा में विशाल जलाशय और शहरों के लिए सरकारी अन्नागार नेटवर्क।"
            },
            {
                "period": "उत्तर हड़प्पा शुष्कीकरण",
                "date": "लगभग 1900 ईसा पूर्व - 1300 ईसा पूर्व",
                "details": "मानसूनी चक्र में बदलाव, घग्गर-हकरा नदी प्रणाली का सूखना, मिट्टी का लवणीकरण और कृषि अधिशेष का पतन जिसके कारण शहरों का परित्याग हुआ।"
            }
        ]
    },
    "mnemonics": {
        "title": "याद रखने के सूत्र (Mnemonics)",
        "description": "यूपीएससी परीक्षा के लिए प्रमुख फसलों, जानवरों और सिंचाई स्थलों को आसानी से याद रखने के सूत्र।",
        "items": [
            {
                "title": "याद रखने का सूत्र 1: उगाई जाने वाली रबी फसलें",
                "phrase": "\"गे-जौ-म-स-ती (गेहूँ, जौ, मटर, सरसों, तिल)\"",
                "decryption": "मुख्य शीतकालीन फसलों को याद रखें: **गे**हूँ, **जौ**, **म**टर, **स**रसों, **ति**ल।"
            },
            {
                "title": "याद रखने का सूत्र 2: विवादास्पद पशु और स्रोत",
                "phrase": "\"सुर-घोड़ा-लो-चावल (सुरकोटदा-घोड़ा, लोथल-चावल)\"",
                "decryption": "प्रमुख बहस वाले खोज स्थल: **सुर**कोटदा से विवादास्पद **घोड़े** की हड्डियाँ मिलीं; **लो**थल (और रंगपुर) से **चावल** की भूसी के साक्ष्य मिले।"
            },
            {
                "title": "याद रखने का सूत्र 3: विशिष्ट जल प्रबंधन स्थल",
                "phrase": "\"शो-नहर, धो-जलाशय, ब-बांध (शोर्तुघई-नहर, धोलावीरा-जलाशय, बलूचिस्तान-गबरबंद)\"",
                "decryption": "सिंचाई संरचनाएं: **शो**र्तुघई में **नहरें** मिलीं; **धो**लावीरा में पत्थर के **जलाशय** मिले; **ब**लूचिस्तान में पत्थर के **गबरबंद** (बांध) मिले।"
            }
        ]
    },
    "flashcards": {
        "title": "सक्रिय स्मरण फ्लैशकार्ड (Active Recall)",
        "description": "हड़प्पा कृषि से जुड़ी प्रमुख खोजों और बहसों पर अपने ज्ञान का परीक्षण करें।",
        "items": [
            {
                "question": "किस हड़प्पा स्थल से ग्रिड पैटर्न में जुते हुए खेत के साक्ष्य मिले हैं?",
                "answer": "राजस्थान के <strong>कालीबंगन</strong> से। यहाँ दोहरे जुते हुए खेत मिले हैं जहाँ हल की रेखाएं एक-दूसरे को समकोण पर काटती हैं, जो एक साथ दो फसलें उगाने को दर्शाती हैं।",
                "icon": "fa-tractor"
            },
            {
                "question": "मिट्टी के हल के मॉडल किन स्थलों से प्राप्त हुए हैं?",
                "answer": "हरियाणा के <strong>बनावली</strong> और पाकिस्तान के <strong>चोलिस्तान</strong> (जवारीवाला) से, जो लकड़ी के हल के आकार की पुष्टि करते हैं।",
                "icon": "fa-screwdriver-wrench"
            },
            {
                "question": "सिंध और पंजाब के मुख्य जलोढ़ मैदानों में नहरों के अवशेष क्यों नहीं मिलते हैं?",
                "answer": "क्योंकि सिंधु और उसकी सहायक नदियों की तेज बाढ़ में बहने वाली गाद (silt) ने सदियों में प्राचीन नहरों को ढक दिया, जिससे केवल कुएं और बाढ़-सिंचाई के अवशेष बचे।",
                "icon": "fa-water"
            },
            {
                "question": "यूनानी शब्द 'सिंडन' (Sindon) का क्या अर्थ है और यह किससे बना है?",
                "answer": "इसका अर्थ <strong>कपास</strong> है। यूनानियों ने इसे 'सिंडन' कहा क्योंकि यह सिंधु (Sindhu) घाटी में पैदा होता था।",
                "icon": "fa-shirt"
            },
            {
                "question": "किस स्थल से घोड़े के विवादास्पद अस्थि अवशेष मिले हैं?",
                "answer": "गुजरात के <strong>सुरकोटदा</strong> से। यहाँ घोड़े की हड्डियां मिली हैं, लेकिन मुहरों और कलाकृतियों पर इसका कोई चित्रण नहीं है, जिससे इसके पालतू होने पर विवाद है।",
                "icon": "fa-horse"
            }
        ]
    },
    "deepDive": {
        "title": "पाठ्यक्रम मुख्य अध्ययन नोट्स (विस्तृत)",
        "description": "सिंधु घाटी की कृषि प्रणालियों, तकनीकों और अनाज वितरण प्रणालियों का अध्ययन करें।",
        "sections": [
            {
                "title": "1. फसलें और पशुओं का घरेलूकरण",
                "content": """<p>हड़प्पा की कृषि अत्यधिक विविध थी, जो शहरों में रहने वाली बड़ी आबादी को भोजन अधिशेष प्रदान करती थी।</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-seedling"></i> फसलें और बुवाई का पैटर्न</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>मुख्य फसलें:</strong> गेहूँ (ब्रेड और क्लब गेहूँ) और जौ मुख्य खाद्य फसलें थीं। मटर, सरसों, चना, मसूर और तिल भी उगाए जाते थे।</li>
      <li><strong>कपास और धान:</strong> हड़प्पा वासी विश्व में सबसे पहले <strong>कपास</strong> उगाने वाले लोग थे, जिसे यूनानियों ने <em>सिंडन</em> कहा। धान की भूसी केवल गुजरात (लोथल, रंगपुर) में मिली है।</li>
      <li><strong>बाजरा:</strong> गुजरात में बाजरा (रागी, कोदोन, ज्वार) उगाया जाता था, जो शुष्क क्षेत्रों में खेती के अनुकूलन को दर्शाता है।</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-cow"></i> पशुपालन और पालतू जानवर</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>पालतू पशु:</strong> कूबड़ वाला बैल (Zebu) सबसे महत्वपूर्ण था। भैंस, भेड़, बकरी, सूअर, ऊंट और गधे भी पाले जाते थे।</li>
      <li><strong>घोड़े का विवाद:</strong> यद्यपि सुरकोटदा में घोड़े की हड्डियां मिली हैं, लेकिन मुहरों पर इसका कोई अंकन नहीं है। इतिहासकार इसे पालतू या व्यापक उपयोग वाला जानवर नहीं मानते हैं।</li>
      <li><strong>जंगली जानवर:</strong> अस्थि अवशेषों से पता चलता है कि वे गैंडे, हाथी, हिरण और घड़ियाल जैसे जंगली जीवों से भी परिचित थे।</li>
    </ul>
  </div>
</div>""",
                "masteryZone": []
            },
            {
                "title": "2. कृषि तकनीक और सिंचाई",
                "content": """<p>हड़प्पा वासियों ने जलोढ़ मिट्टी जोतने और बाढ़ के पानी के प्रबंधन के लिए उन्नत उपकरणों और जल इंजीनियरिंग का विकास किया था।</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-compass"></i> जुताई और कटाई के उपकरण</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>हल आधारित कृषि:</strong> राजस्थान के <strong>कालीबंगन</strong> से जुते हुए खेत के सीधे साक्ष्य मिले हैं। <strong>बनावली</strong> और चोलिस्तान से मिले मिट्टी के हलों से लकड़ी के हल के उपयोग की पुष्टि होती है।</li>
      <li><strong>कटाई उपकरण:</strong> फसल काटने के लिए लकड़ी के हत्थों में चर्ट (पत्थर) के फलक (blades) फिट कर हँसिए के रूप में उपयोग किए जाते थे। तांबे के हँसिए दुर्लभ थे।</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-faucet-drip"></i> सिंचाई और जल तकनीक</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>नहरें:</strong> सिंधु घाटी के मैदानों में सिल्ट जमा होने के कारण नहरें लुप्त हो गईं। लेकिन उत्तरी अफगानिस्तान के <strong>शोर्तुघई</strong> में पत्थरों से बनी नहरों का जाल मिला है।</li>
      <li><strong>जलाशय और बांध:</strong> <strong>धोलावीरा</strong> में वर्षा जल संचयन के लिए चट्टानों को काटकर बनाए गए विशाल जलाशय मिले हैं। बलूचिस्तान की पहाड़ियों में पानी रोकने के लिए <strong>गबरबंद</strong> नामक बांध बनाए गए थे।</li>
      <li><strong>कुएं:</strong> मोहनजोदड़ो जैसे शहरों में कुओं का व्यापक जाल था जो पीने और बागवानी के काम आता था।</li>
    </ul>
  </div>
</div>""",
                "masteryZone": []
            },
            {
                "title": "3. अनाज भंडारण, कृषि अर्थव्यवस्था और पतन",
                "content": """<p>अधिशेष अनाज का प्रबंधन और पर्यावरणीय बदलावों के कारण कृषि का संकट सिंधु शहरों के उत्थान और पतन के प्रमुख कारक थे।</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-warehouse"></i> भंडारण और केंद्रीय नियंत्रण</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>अन्नागार (Granaries):</strong> मोहनजोदड़ो का <strong>विशाल अन्नागार</strong> (ईंटों का मंच और लकड़ी की संरचना) और हड़प्पा में छह-छह अन्नागारों की दो कतारें आपातकालीन खाद्य भंडार का काम करती थीं।</li>
      <li><strong>खलिहान (Threshing Floors):</strong> हड़प्पा में अन्नागारों के पास ईंटों के वृत्ताकार चबूतरे मिले हैं, जिनमें गेहूँ और जौ के दाने मिले हैं, जो यह दर्शाते हैं कि यहाँ अनाज की गहाई होती थी।</li>
      <li><strong>कर प्रणाली:</strong> बैलगाड़ियों द्वारा ग्रामीण इलाकों से शहरों में अनाज लाया जाता था, जिसे संभवतः कर या भेंट के रूप में एकत्र किया जाता था।</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-cloud-sun-rain"></i> जलवायु परिवर्तन और पतन</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>मानसून में कमी:</strong> 1900 ईसा पूर्व के बाद ग्रीष्मकालीन मानसून के कमजोर होने से सिंधु बेसिन में फसल उत्पादकता प्रभावित हुई।</li>
      <li><strong>नदियों का मार्ग बदलना:</strong> घग्गर-हकरा जैसी नदियों के सूखने और मार्ग बदलने से जल संकट पैदा हुआ, जबकि सिंध में विवर्तनिक बदलावों से भयानक बाढ़ आई।</li>
      <li><strong>अधिशेष का अंत:</strong> जब कृषि अधिशेष समाप्त हो गया, तो शहरों की बड़ी आबादी को बनाए रखना असंभव हो गया, जिससे लोगों ने पूर्व में गंगा घाटी और गुजरात की ओर पलायन किया।</li>
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
            "<strong>गलती 1:</strong> इस भ्रम से बचें कि हड़प्पा वासी गन्ना या चाय उगाते थे। इन फसलों से वे पूरी तरह अपरिचित थे।",
            "<strong>गलती 2:</strong> इस कथन को गलत मानें कि हड़प्पा काल में लोहे के हलों का उपयोग होता था। हड़प्पा वासी **कांस्य युग** के थे और वे लोहे से अपरिचित थे; वे लकड़ी के हलों का उपयोग करते थे।",
            "<strong>गलती 3:</strong> यह न मानें कि चावल मुख्य खाद्य फसल थी। चावल के अवशेष केवल लोथल और रंगपुर में मिले हैं; गेहूँ और जौ ही मुख्य खाद्य फसलें थीं।",
            "<strong>गलती 4:</strong> इस कथन से सावधान रहें कि घोड़े का कृषि और परिवहन में केंद्रीय महत्व था। मुहरों पर घोड़े का अंकन नहीं है और इसके पालतू होने पर विवाद है।",
            "<strong>गलती 5:</strong> सिंधु घाटी के मैदानों में नहरों को प्राथमिक सिंचाई साधन न मानें। वहां नहरें नहीं मिली हैं; **कुएं और बाढ़ का पानी** ही मुख्य सिंचाई स्रोत थे।"
        ]
    },
    "practiceQuestions": [],
    "mockTestQuestions": []
}

# Define the raw practice questions - 50 questions
practice_raw_eng = [
    ("With reference to the agricultural practices of the Harappans, consider the following statements:\n1. Direct evidence of a ploughed field has been discovered at Kalibangan in Rajasthan.\n2. The field featured a grid pattern of furrows, indicating the practice of double-cropping.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 2, "Both statements are correct. Kalibangan has yielded a ploughed field with two sets of furrows at right angles, demonstrating grid tilling and double-cropping."),
    ("Terracotta models of ploughs have been recovered from which of the following Harappan sites?\n1. Banawali in Haryana\n2. Cholistan (Jawariwala) in Pakistan\n3. Mohenjo-daro in Sindh\nSelect the correct answer using the code given below:", ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"], 0, "Terracotta models of ploughs were recovered from Banawali (Haryana) and sites in Cholistan (like Jawariwala). Mohenjo-daro has not yielded direct terracotta models of ploughs."),
    ("Which of the following was the primary winter (Rabi) crop suite cultivated by the Harappans?", ["Wheat, Barley, Peas, and Mustard", "Rice, Sugarcane, and Ragi", "Maize, Cotton, and Jowar", "Tea, Coffee, and Indigo"], 0, "The primary crop suite was Rabi (winter) crops: wheat, barley, peas, lentils, sesame, and mustard. Sugarcane, maize, tea, and coffee were unknown."),
    ("Consider the following statements regarding cotton cultivation in the Indus Valley Civilisation:\n1. The Harappans were the first in the world to grow cotton.\n2. The Greeks referred to cotton as 'Sindon' due to its Indus Valley origins.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 2, "Both statements are correct. Cotton was first cultivated in the Indus Valley, and Greeks called it Sindon (derived from Sindhu)."),
    ("At which of the following Gujarat sites have archaeologists discovered direct evidence of rice husks embedded in pottery?", ["Lothal and Rangpur", "Dholavira and Surkotada", "Nageshwar and Balakot", "Rojdi and Bhagatrav"], 0, "Lothal and Rangpur are the two sites in Gujarat that have yielded rice husks, indicating localized rice cultivation in the Gujarat region."),
    ("With reference to animal domestication by the Harappans, which of the following was the most frequently depicted and revered animal on seals?", ["Humped bull (Zebu)", "African elephant", "One-horned unicorn", "Bactrian camel"], 2, "The one-horned unicorn is the most frequently depicted animal on seals. Among actual domestic animals, the humped bull (zebu) was highly revered and common."),
    ("Consider the following statements regarding the controversy of the horse in Harappan culture:\n1. Skeletal remains of a horse have been identified at the site of Surkotada in Gujarat.\n2. The horse is frequently depicted alongside the unicorn on seals.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 0, "Statement 1 is correct. Statement 2 is incorrect: the horse is completely absent from Harappan seal iconography and terracotta art."),
    ("At which of the following remote outposts did the Harappans construct a stone-lined canal network to irrigate crops near lapis lazuli veins?", ["Shortughai in northern Afghanistan", "Sutkagendor on the Makran coast", "Mundigak in southern Afghanistan", "Altyn-Depe in Turkmenistan"], 0, "Shortughai on the Oxus River in northern Afghanistan has yielded clear traces of canal networks used for agriculture and domestic water supply."),
    ("Why are canal ruins rare in the main alluvial plains of Sindh and Punjab?", ["The Harappans did not know how to dig canals", "Ancient canals were buried over centuries by silt-laden floods of the Indus and its tributaries", "The state banned canal construction to prevent water conflicts", "All agricultural fields were irrigated using rainwater harvesting only"], 1, "The heavy silt deposits carried by the Indus and its tributaries during annual floods buried the canals over centuries, making them archaeologically invisible today."),
    ("Which Harappan site is famous for having massive stone-cut reservoirs and elaborate check-dams for rainwater harvesting?", ["Dholavira", "Lothal", "Kalibangan", "Mohenjo-daro"], 0, "Dholavira in Gujarat is famous for its sophisticated water management system, including 16 large stone-cut reservoirs."),
    ("The stone-walled check dams constructed across seasonal streams in Baluchistan to trap water and soil are known as:", ["Gabarbands", "Sluice-gates", "Bunds", "Johads"], 0, "They are known as Gabarbands (or stone dams), which helped check water run-off and accumulate fertile silt in Baluchistan."),
    ("What tools did the Harappans use to harvest mature grain crops?", ["Chert/stone blades set in wooden handles", "Iron sickles with metal loops", "Bronze scythes with bone handles", "Copper blades without handles"], 0, "They used chert (stone) blades set in wooden handles to act as sickles. Iron was unknown, and copper sickles were extremely rare."),
    ("Consider the following statements regarding the 'Great Granary' of Mohenjo-daro:\n1. It was built on a massive brick platform with sockets for timber columns.\n2. It featured an air-duct system below the floors to keep the grain dry and prevent spoilage.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 2, "Both statements are correct. The granary design utilized air ducts and elevated timber structures to keep stored grain dry and aerated."),
    ("Circular brick platforms discovered near the granaries at Harappa served which of the following agricultural functions?", ["Threshing floors for grain processing", "Storage silos for grain husks", "Ritual altars for harvest sacrifices", "Cattle pens for draft oxen"], 0, "Traces of wheat and barley chaff found in the central hollows of these circular platforms indicate they were used as threshing floors."),
    ("Which of the following millets was widely cultivated in the Gujarat region during the Mature Harappan phase?", ["Ragi and Jowar", "Oats and Rye", "Maize", "Spelt"], 0, "Millets like ragi, jowar, and bajra were cultivated in Gujarat, showing adaptation to drier climates."),
    ("Consider the following statements regarding water wells in Harappan cities:\n1. Hundreds of brick-lined public and private wells were dug, especially at Mohenjo-daro.\n2. Wells were the primary source of irrigation in the dry plains of Sindh.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 2, "Both statements are correct. Well irrigation was highly developed to water plots in Sindh where river floods did not reach."),
    ("What was the main staple crop in the northern Harappan regions (Punjab and Haryana)?", ["Wheat and Barley", "Rice", "Cotton", "Millets"], 0, "Wheat and barley were the absolute staple crops in the northern plains of Punjab, Haryana, and Rajasthan."),
    ("With reference to the relationship between rural hinterlands and urban cities, how was agricultural surplus collected?", ["Through state-managed collection using bullock carts as tribute or tax", "By buying from independent foreign grain merchants", "By using coins to purchase crops in village markets", "By importing grain exclusively from Mesopotamia"], 0, "Agricultural surplus was brought from villages in bullock carts, likely collected as tax or tribute to fill the public granaries of the state."),
    ("Which of the following animals was NOT domesticated by the Harappans?", ["African Elephant", "Humped cattle", "Water buffalo", "Sheep and Goat"], 0, "Harappans domesticated Indian elephants, humped cattle, water buffaloes, sheep, and goats. They did not domesticate African elephants."),
    ("Consider the following statements regarding the decline of Harappan agriculture:\n1. Weakening of the summer monsoon around 1900 BCE reduced rainfall in the core area.\n2. Tectonic changes shifted river courses and dried up the Ghaggar-Hakra system.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 2, "Both statements are correct. Climate desiccation, monsoon failures, and tectonic shifts drying up rivers led to agricultural decline."),
    ("Which non-food crop was highly valued by the Harappans as a major trade and manufacturing commodity?", ["Cotton", "Jute", "Indigo", "Hemp"], 0, "Cotton was a major trade commodity, exported as raw fiber and woven textiles to the Persian Gulf and Mesopotamia."),
    ("The double-cropped field at Kalibangan shows furrows in two directions. What does this suggest?", ["One set of furrows was for winter crops and the other for summer crops", "Two different crops were grown together at the same time to maximize efficiency", "The field was abandoned due to water-logging", "Different social classes cultivated separate parts of the field"], 1, "The grid pattern of furrows suggests that two crops with different growth requirements were cultivated at the same time in the same field."),
    ("Which of the following tools was completely absent from Harappan agricultural inventory?", ["Iron ploughshares", "Wooden ploughshares", "Chert sickles", "Copper blades"], 0, "Iron ploughshares were completely absent. Iron was unknown to the Harappans (Bronze Age civilization)."),
    ("With reference to the diet of the Harappans, animal bones indicate that they consumed which domesticated animals?", ["Cattle, Buffalo, Sheep, Goat, and Pig", "Cheetah, Leopard, and Lion", "Horse and Donkey primarily", "African Elephant only"], 0, "Bone assemblages show they consumed cattle, buffalo, sheep, goat, and pig meat."),
    ("At which site in Pakistan did archaeologists find a series of brick platforms that functioned as storage units or granaries, similar to Harappa?", ["Mohenjo-daro", "Kalibangan", "Lothal", "Sutkagendor"], 0, "Mohenjo-daro contains the Great Granary, and Harappa has six granaries in a row. Kalibangan has brick platforms that may have held granaries."),
    ("Consider the following statements:\n1. The Harappans relied on natural floodwaters of the rivers to irrigate their low-lying plains.\n2. Inundation canals were built to divert seasonal floodwaters into fields.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 2, "Both statements are correct. They utilized flood-basin irrigation and simple inundation canals to divert water."),
    ("Which of the following wild animals' bones have been found at Harappan sites, indicating they were hunted for food?", ["Deer, Wild Boar, and Gharial", "Lion, Cheetah, and Zebra", "Giraffe and Kangaroo", "African Elephant"], 0, "Deer, wild boar, and gharial bones are found in Harappan refuse heaps, indicating they supplement their diet with wild game."),
    ("Which of the following crops was NOT cultivated by the Harappans?", ["Sugarcane", "Wheat", "Barley", "Sesame"], 0, "Sugarcane was not cultivated by the Harappans; wheat, barley, and sesame were cultivated."),
    ("How did Dholavira's check dams operate?", ["By diverting seasonal river run-off of the Manhar and Mandsar streams into reservoirs", "By trapping seawater during high tide", "By generating electricity for grain mills", "By keeping river boats afloat"], 0, "Dholavira's check dams were built across the seasonal streams of Manhar and Mandsar to divert rainwater run-off into large stone-cut reservoirs."),
    ("Which animal was used as the primary beast of burden in the plains for transporting harvested grain?", ["Humped Bull / Ox", "Horse", "Cheetah", "Elephant"], 0, "The humped bull/ox was the primary draft and transport animal used to pull solid-wheeled grain carts."),
    ("Which Harappan site in Haryana has yielded a terracotta model of a plough showing the curved share?", ["Banawali", "Rakhigarhi", "Mitathal", "Birrana"], 0, "Banawali has yielded a highly famous, complete terracotta model of a plough."),
    ("Consider the following statements regarding rice remains at Lothal:\n1. Rice husks were found mixed with pottery clay to bind it.\n2. Large granaries filled entirely with rice grains were excavated at the site.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 0, "Statement 1 is correct. Statement 2 is incorrect: only traces of rice husks have been found, not massive rice granaries."),
    ("The agricultural economy of the Harappans is best described as:", ["A highly productive surplus economy supporting urban specialization", "A subsistence nomadic pastoral economy", "An import-dependent agricultural system", "A state-monopolized plantation economy"], 0, "It was a highly productive surplus agricultural economy that allowed specialized urban populations (craftsmen, administrative elites) to thrive."),
    ("Which of the following oilseeds was cultivated by the Harappans?", ["Sesame and Mustard", "Sunflower", "Soybean", "Olive"], 0, "Sesame and mustard were the main oilseeds grown and used for cooking oil."),
    ("Where is the site of Cholistan located, and what is its agricultural significance?", ["Desert region in Pakistan, yielded terracotta plough models at Jawariwala", "Hilly region in Baluchistan, has dams", "Coastal area in Gujarat, has rice", "Northern plains of Punjab, has canals"], 0, "Cholistan is a desert region in Punjab, Pakistan. It has yielded terracotta ploughs at sites like Jawariwala."),
    ("Consider the following statements:\n1. Harappan agriculture was entirely dependent on artificial canals from the Indus River.\n2. Wells and seasonal floods were the primary water sources in the main valley.\nWhich of the statements given above is/are correct?", ["2 only", "1 only", "Both 1 and 2", "Neither 1 nor 2"], 0, "Statement 2 is correct. Statement 1 is incorrect: canals are absent in the main plains due to silting."),
    ("The use of check-dams in Baluchistan suggests what about the ancient environment?", ["Rainfall was seasonal and scarce, requiring water conservation", "The region was a tropical rainforest", "The sea level was much higher than today", "Rivers were overflowing throughout the year"], 0, "Gabarbands suggest that Baluchistan had seasonal, scarce rainfall, requiring check dams to trap water and silt for cultivation."),
    ("What was the main purpose of the circular platforms discovered at Harappa?", ["To thresh wheat and barley by hand or animal stamping", "To act as foundations for temples", "To pen sheep and goats", "To manufacture clay pottery"], 0, "They functioned as threshing floors, where grain stalks were beaten to extract wheat and barley kernels."),
    ("Which of the following fibers was cultivated by the Harappans for textile production?", ["Cotton", "Silk", "Jute", "Flax"], 0, "Cotton was the main fiber cultivated and woven into cloth."),
    ("Which animal was used to pull the heavy wooden ploughshares in Harappan fields?", ["Humped Oxen (Zebu)", "Horses", "Elephants", "Lions"], 0, "Humped oxen (zebu) were utilized to pull ploughs, as depicted in terracotta art and toy models."),
    ("The presence of granaries in multiple Harappan cities indicates:", ["A centralized system of food security and redistribution", "A lack of local farming knowledge", "That all citizens were farmers", "That grain was imported from Mesopotamia for storage"], 0, "It indicates a highly organized, centralized state-supervised food security and redistribution system."),
    ("What plant remains were found inside the circular platforms at Harappa, confirming their function?", ["Wheat and Barley", "Rice and Cotton", "Mustard and Sesame", "Sugarcane and Lentils"], 0, "Wheat and barley chaff/grains were discovered in the central depressions of these platforms."),
    ("Consider the following statements:\n1. The camel was known and domesticated by the Harappans.\n2. Camel bones are reported at sites like Kalibangan.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 2, "Both statements are correct. Camels were used as beasts of burden, and their bones are found at Kalibangan."),
    ("The agricultural fields of the Harappans were mostly situated in:", ["Alluvial floodplains of rivers", "High mountain terraces", "Deep forest clearances", "Coastal salt marshes"], 0, "Fields were situated in the fertile alluvial floodplains of the Indus, Ghaggar-Hakra, and their tributaries."),
    ("Which of the following states of India has yielded the maximum number of Harappan farming villages and millets?", ["Gujarat", "Punjab", "Rajasthan", "Uttar Pradesh"], 0, "Gujarat has yielded many rural sites showing millet cultivation (ragi, jowar, bajra)."),
    ("Which water management structure is unique to the site of Dholavira in Gujarat?", ["Interconnected stone-cut reservoirs", "A baked brick dockyard", "An automated siphon canal", "A deep stepwell with a water wheel"], 0, "Interconnected stone-cut reservoirs carved out of bedrock are unique to Dholavira."),
    ("With reference to the Harappan diet, what role did fish play?", ["Fish and marine resources were widely consumed, especially at coastal sites", "Fish was considered taboo and not eaten", "They only ate freshwater fish, not marine fish", "Fish was only imported from Mesopotamia in dried form"], 0, "Fish bones and hooks found at both coastal and inland sites indicate fish was a vital dietary protein."),
    ("What is the significance of the double-furrow grid pattern found at Kalibangan?", ["It allows two crops (one tall, one short) to be grown together without shading each other", "It prevents water erosion of the topsoil", "It was a ritual design dedicated to the rain god", "It shows the fields were ploughed using two different animals"], 0, "The grid pattern features wide furrows in one direction and narrow furrows in the other, allowing double-cropping without crop interference."),
    ("Which animal's bones are rare in Harappan layers but common in later Vedic layers, highlighting a key cultural shift?", ["Horse", "Humped bull", "Buffalo", "Goat"], 0, "Horse remains are rare/controversial in Harappan layers but extremely common in later Rigvedic/Vedic layers, showing a distinct transition."),
    ("How did river migrations contribute to the decline of Harappan agriculture?", ["By depriving agricultural fields of water, turning fertile areas into dry basins", "By drowning the entire civilization in a single day", "By making it impossible to sail trade ships", "By turning river water toxic"], 0, "River migrations (such as the shifts of the Sutlej and Yamuna away from the Ghaggar-Hakra) starved fertile agricultural lands of water, leading to desertification.")
]

# Define 10 Mock Questions in UPSC standard style
mock_raw_eng = [
    ("With reference to the agricultural technology of the Indus Valley Civilisation, consider the following statements:\n1. Terracotta models of ploughs have been excavated at Banawali and Cholistan.\n2. The ploughed field discovered at Kalibangan belongs to the Mature Harappan phase.\n3. The Harappans utilized heavy iron sickles to harvest their winter wheat.\nWhich of the statements given above is/are correct?", ["1 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"], 0, "Statement 1 is correct. Statement 2 is incorrect: the ploughed field belongs to the Early Harappan/Pre-Mature phase of Kalibangan. Statement 3 is incorrect: iron was unknown to the Harappans; they used chert/stone sickles."),
    ("Which of the following pairs is/are correctly matched?\nArchaeological Site - Agrarian Finding\n1. Kalibangan - Grid-patterned ploughed field\n2. Banawali - Terracotta model of a plough\n3. Shortughai - Stone-lined canal irrigation network\nSelect the correct answer using the code given below:", ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"], 3, "All three pairs are correctly matched. Kalibangan yielded the ploughed field, Banawali the plough model, and Shortughai the canal network."),
    ("Consider the following statements regarding crop cultivation in the Harappan civilization:\n1. Wheat and barley were the primary winter staple crops in the northern plains.\n2. Rice was cultivated extensively throughout the main alluvial plain of Sindh.\n3. The Harappans were the first civilization to domesticate and weave cotton.\nWhich of the statements given above are correct?", ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"], 2, "Statements 1 and 3 are correct. Statement 2 is incorrect: rice was rare and localized to Gujarat (Lothal, Rangpur), not cultivated extensively in Sindh."),
    ("With reference to the water management systems of the Indus Valley Civilisation, consider the following statements:\n1. Rainwater harvesting through stone-cut reservoirs was a unique feature of Dholavira.\n2. Gabarbands were stone check dams built across seasonal streams in Baluchistan.\n3. Canals were the primary source of irrigation throughout the alluvial plains of Sindh.\nWhich of the statements given above is/are correct?", ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"], 0, "Statements 1 and 2 are correct. Statement 3 is incorrect: canals are absent in the main plains of Sindh due to siltation; well and flood irrigation were primary."),
    ("Consider the following statements regarding the domestication of animals in Harappan society:\n1. Humped cattle (zebu) and water buffaloes were domesticated for milk and draft work.\n2. The horse was widely depicted on administrative seals to represent royal power.\n3. Bones of camels and asses indicate their use as draft animals.\nWhich of the statements given above is/are correct?", ["1 and 3 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"], 0, "Statements 1 and 3 are correct. Statement 2 is incorrect: the horse is completely absent from Harappan seal iconography."),
    ("Which of the following statements best explains why the agricultural surplus of the Harappans declined during the Late Harappan phase?", ["A general weakening of the summer monsoon and the migration/drying up of river courses starved fields of water and silt", "The soil was depleted of all nutrients due to lack of crop rotation", "Mesopotamian merchants stopped exporting fertilizers to the Indus Valley", "A massive plague wiped out all domesticated humped cattle"], 0, "Weakening monsoons and shifts/drying up of rivers (like the Ghaggar-Hakra system) deprived fields of water, leading to agricultural decline and urban de-population."),
    ("Consider the following statements regarding granaries in the Indus Valley Civilisation:\n1. The Great Granary at Mohenjo-daro featured elevated timber structures and air ducts.\n2. Circular brick platforms used as threshing floors were discovered next to the granaries at Harappa.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 2, "Both statements are correct. Granaries had air ducts for ventilation, and Harappa had circular threshing floors with grain chaff."),
    ("Which of the following crops were cultivated by the Harappans?\n1. Wheat and Barley\n2. Mustard and Sesame\n3. Millets\n4. Sugarcane\nSelect the correct answer using the code given below:", ["1, 2 and 3 only", "1, 2 and 4 only", "2, 3 and 4 only", "1, 2, 3 and 4"], 0, "Wheat, barley, mustard, sesame, and millets were cultivated. Sugarcane was completely unknown to the Harappans."),
    ("Consider the following statements:\nStatement 1: The Greeks called cotton 'Sindon', which is etymologically derived from 'Sindhu' (Indus).\nStatement 2: The Harappans traded cotton textiles with Mesopotamia in exchange for silver and bitumen.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 2, "Both statements are correct. The Greeks named cotton 'Sindon' after the Indus (Sindhu), and cotton textiles were exported to Mesopotamia."),
    ("Which of the following pairs is/are correctly matched?\nArchaeological Finding - Harappan Site\n1. Rice husks in pottery - Lothal\n2. Horse skeletal remains - Surkotada\n3. Terracotta plough model - Banawali\nSelect the correct answer using the code given below:", ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"], 3, "All three pairs are correctly matched. Lothal has rice husks, Surkotada has horse remains, and Banawali has the plough model.")
]

# Provide Hindi translations for practice questions
practice_raw_hin = [
    ("हड़प्पा वासियों की कृषि पद्धतियों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. राजस्थान के कालीबंगन में एक जुते हुए खेत का प्रत्यक्ष साक्ष्य मिला है।\n2. जुते हुए खेत में ग्रिड पैटर्न (हल की रेखाएं) मिला है, जो दोहरी फसल प्रणाली का संकेत देता है।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 2, "दोनों कथन सही हैं। कालीबंगन से दोहरे जुते हुए खेत के साक्ष्य मिले हैं जो ग्रिड पैटर्न में समकोण पर काटती हल-रेखाओं को दर्शाते हैं।"),
    ("मिट्टी के हल के मॉडल निम्नलिखित में से किस हड़प्पा स्थल से प्राप्त हुए हैं?\n1. हरियाणा में बनावली\n2. पाकिस्तान में चोलिस्तान (जवारीवाला)\n3. सिंध में मोहनजोदड़ो\nनीचे दिए गए कूट का प्रयोग कर सही उत्तर चुनिए:", ["1 और 2 केवल", "2 और 3 केवल", "1 और 3 केवल", "1, 2 और 3"], 0, "मिट्टी के हल के मॉडल बनावली (हरियाणा) और चोलिस्तान (जैसे जवारीवाला) से मिले हैं। मोहनजोदड़ो से प्रत्यक्ष हल मॉडल नहीं मिले हैं।"),
    ("निम्नलिखित में से कौन सी हड़प्पा वासियों द्वारा उगाई जाने वाली प्राथमिक शीतकालीन (रबी) फसलें थीं?", ["गेहूँ, जौ, मटर और सरसों", "चावल, गन्ना और रागी", "मक्का, कपास और ज्वार", "चाय, कॉफी और नील"], 0, "प्राथमिक रबी फसलों में गेहूँ, जौ, मटर, मसूर, तिल और सरसों शामिल थे। गन्ना, मक्का और चाय उस समय अज्ञात थे।"),
    ("सिंधु घाटी सभ्यता में कपास की खेती के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:\n1. हड़प्पा वासी विश्व में सबसे पहले कपास उगाने वाले लोग थे।\n2. यूनानी लोग कपास को इसके सिंधु घाटी उद्गम के कारण 'सिंडन' (Sindon) कहते थे।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 2, "दोनों कथन सही हैं। कपास सबसे पहले सिंधु घाटी में उगाया गया था और इसके सिंधु (Sindhu) नाम के कारण यूनानियों ने इसे सिंडन कहा।"),
    ("गुजरात के निम्नलिखित में से किस स्थल पर पुरातत्वविदों को मिट्टी के बर्तनों में धान (चावल) की भूसी के सीधे साक्ष्य मिले हैं?", ["लोथल और रंगपुर", "धोलावीरा और सुरकोटदा", "नागेश्वर और बालाकोट", "रोजदी और भगतराव"], 0, "गुजरात के लोथल और रंगपुर से बर्तनों के गारे में दबी धान की भूसी मिली है, जो चावल की खेती को दर्शाती है।"),
    ("हड़प्पा वासियों द्वारा पशुओं को पालतू बनाने के संदर्भ में, निम्नलिखित में से कौन सा जानवर मुहरों पर सबसे अधिक चित्रित और पूजनीय था?", ["कूबड़ वाला बैल (Zebu)", "अफ्रीकी हाथी", "एक सींग वाला गेंडा (Unicorn)", "बैक्टीरियन ऊँट"], 2, "मुहरों पर एक सींग वाले गेंडे (unicorn) का सर्वाधिक अंकन है। वास्तविक जानवरों में कूबड़ वाला बैल अत्यंत पूजनीय था।"),
    ("हड़प्पा संस्कृति में घोड़े से जुड़े विवादों के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:\n1. गुजरात के सुरकोटदा नामक स्थल से घोड़े के अस्थि अवशेष मिले हैं।\n2. मुहरों पर एक सींग वाले गेंडे के साथ घोड़े का भी अक्सर चित्रण मिलता है।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि मुहरों और कलाकृतियों पर घोड़े का कोई अंकन नहीं मिलता है।"),
    ("निम्नलिखित में से किस सुदूर व्यापारिक चौकी पर हड़प्पा वासियों ने लाजवर्त खदानों के पास खेती के लिए पत्थरों से बनी नहरों का जाल बनाया था?", ["उत्तरी अफगानिस्तान में शोर्तुघई", "मकरान तट पर सुत्कागेंदोर", "दक्षिणी अफगानिस्तान में मुंडीगाक", "तुर्कमेनिस्तान में अल्टिन-देपे"], 0, "उत्तरी अफगानिस्तान में आक्सस नदी पर स्थित शोर्तुघई से पत्थरों से बनी सिंचाई नहरों के अवशेष मिले हैं।"),
    ("सिंध और पंजाब के मुख्य जलोढ़ मैदानों में नहरों के खंडहर दुर्लभ क्यों हैं?", ["हड़प्पा वासी नहर खोदना नहीं जानते थे", "सिंधु और उसकी सहायक नदियों की गाद-युक्त बाढ़ ने सदियों में प्राचीन नहरों को पाट दिया", "पानी के विवादों को रोकने के लिए राज्य ने नहरों के निर्माण पर प्रतिबंध लगा दिया था", "सभी कृषि क्षेत्रों की सिंचाई केवल वर्षा जल संचयन से होती थी"], 1, "सिंधु नदी की गाद युक्त बाढ़ ने समय के साथ नहरों को मिट्टी से भर दिया, जिससे वे आज पुरातात्विक रूप से दिखाई नहीं देतीं।"),
    ("कौन सा हड़प्पा स्थल वर्षा जल संचयन के लिए विशाल प्रस्तर जलाशयों और बांधों के निर्माण के लिए प्रसिद्ध है?", ["धोलावीरा", "लोथल", "कालीबंगन", "मोहनजोदड़ो"], 0, "गुजरात का धोलावीरा अपने जल प्रबंधन के लिए प्रसिद्ध है, जहाँ चट्टानों को काटकर बनाए गए 16 बड़े जलाशय मिले हैं।"),
    ("बलूचिस्तान में मौसमी नदियों के पानी और मिट्टी को रोकने के लिए बनाई गई पत्थरों की दीवारों (बांधों) को क्या कहा जाता है?", ["गबरबंद", "लॉक-गेट", "तटबंध", "जोहड़"], 0, "इन्हें गबरबंद कहा जाता है, जो पानी के बहाव को नियंत्रित करने और खेती के लिए गाद जमा करने का काम करते थे।"),
    ("हड़प्पा वासी पकी हुई फसलों की कटाई के लिए किस उपकरण का उपयोग करते थे?", ["लकड़ी के हत्थों में लगे चर्ट/पत्थर के फलक", "लोहे के हँसिए", "कांस्य के हँसिए", "तांबे के बिना हत्थे वाले फलक"], 0, "वे लकड़ी के हत्थों में पत्थर (चर्ट) के फलक लगाकर हँसिए के रूप में उपयोग करते थे। लोहे का ज्ञान नहीं था।"),
    ("मोहनजोदड़ो के 'विशाल अन्नागार' के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:\n1. यह ईंटों के एक बड़े मंच पर बना था जिसमें लकड़ी के खंभों के लिए खांचे थे।\n2. अनाज को सूखा रखने और सड़ने से बचाने के लिए फर्श के नीचे हवा के आवागमन (Air-duct) की व्यवस्था थी।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 2, "दोनों कथन सही हैं। अन्नागार में अनाज को सुरक्षित और नमी से दूर रखने के लिए हवा के मार्ग बने हुए थे।"),
    ("हड़प्पा में अन्नागारों के पास मिले ईंटों के वृत्ताकार चबूतरे किस कृषि कार्य के काम आते थे?", ["अनाज की गहाई (Threshing floors) के लिए", "भूसे के भंडारण के लिए", "फसल कटाई के समय पूजा के लिए", "बैलों को बांधने के लिए"], 0, "इन चबूतरों के केंद्रीय छिद्रों में गेहूँ और जौ की भूसी के अवशेष मिले हैं, जिससे सिद्ध होता है कि ये गहाई (threshing) के चबूतरे थे।"),
    ("परिपक्व हड़प्पा काल के दौरान गुजरात क्षेत्र में कौन सा बाजरा/मोटा अनाज व्यापक रूप से उगाया जाता था?", ["रागी और ज्वार", "जई (Oats)", "मक्का", "स्पेलट (Spelt)"], 0, "गुजरात में रागी, बाजरा और ज्वार उगाया जाता था, जो शुष्क क्षेत्रों में खेती के अनुकूलन को दर्शाता है।"),
    ("हड़प्पा शहरों में पानी के कुओं के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:\n1. मोहनजोदड़ो में सैकड़ों ईंटों से बने सार्वजनिक और निजी कुएं खोदे गए थे।\n2. सिंध के शुष्क मैदानों में कुएं सिंचाई के मुख्य साधन थे जहां बाढ़ का पानी नहीं पहुँचता था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 2, "दोनों कथन सही हैं। कुएं घरेलू उपयोग और छोटी कृषि भूमियों की सिंचाई के लिए खोदे गए थे।"),
    ("उत्तरी हड़प्पा क्षेत्रों (पंजाब और हरियाणा) में मुख्य खाद्य फसल क्या थी?", ["गेहूँ और जौ", "चावल", "कपास", "बाजरा"], 0, "उत्तरी मैदानों में गेहूँ और जौ ही मुख्य खाद्य फसलें थीं।"),
    ("ग्रामीण इलाकों और शहरों के बीच संबंधों के संदर्भ में, कृषि अधिशेष कैसे एकत्र किया जाता था?", ["राज्य द्वारा बैलगाड़ियों के माध्यम से कर या भेंट के रूप में", "विदेशी व्यापारियों से खरीद कर", "गांवों के बाजारों से सिक्कों द्वारा खरीद कर", "केवल मेसोपोटामिया से अनाज का आयात करके"], 0, "कृषि अधिशेष को बैलगाड़ियों से लाया जाता था, जिसे संभवतः कर या भेंट के रूप में सरकारी अन्नागारों में जमा किया जाता था।"),
    ("निम्नलिखित में से किस जानवर को हड़प्पा वासियों द्वारा पालतू नहीं बनाया गया था?", ["अफ्रीकी हाथी", "कूबड़ वाले बैल", "भैंस", "भेड़ और बकरी"], 0, "वे भारतीय हाथी, बैल, भैंस, भेड़ और बकरियों को पालते थे, लेकिन अफ्रीकी हाथी से उनका कोई संबंध नहीं था।"),
    ("हड़प्पा कृषि के पतन के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:\n1. 1900 ईसा पूर्व के आसपास ग्रीष्मकालीन मानसून के कमजोर होने से वर्षा में कमी आई।\n2. विवर्तनिक बदलावों ने नदियों का मार्ग बदल दिया और घग्गर-हकरा प्रणाली सूख गई।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 2, "दोनों कथन सही हैं। शुष्क जलवायु, मानसून विफलता और नदियों के सूखने से कृषि आधारित शहरों का पतन हुआ।"),
    ("किस गैर-खाद्य फसल का हड़प्पा काल में व्यापार और कपड़ा निर्माण में अत्यधिक मूल्य था?", ["कपास", "जूट", "नील", "भांग"], 0, "कपास का कपड़ा और सूत हड़प्पा काल के प्रमुख व्यापारिक निर्यात थे जो मेसोपोटामिया तक जाते थे।"),
    ("कालीबंगन में जुते हुए खेत में दो दिशाओं में हल की रेखाएं मिली हैं। यह क्या दर्शाता है?", ["एक रेखा शीतकालीन और दूसरी ग्रीष्मकालीन फसलों के लिए थी", "एक साथ दो अलग-अलग फसलें उगाने की तकनीक (दोहरी फसल)", "खेत जलभराव के कारण छोड़ दिया गया था", "समाज के विभिन्न वर्गों के लिए अलग-अलग खेत थे"], 1, "ग्रिड पैटर्न दर्शाता है कि एक ही समय में खेत में दो फसलें उगाई जाती थीं ताकि उत्पादकता बढ़ सके।"),
    ("हड़प्पा के कृषि उपकरणों में कौन सा उपकरण पूरी तरह से अनुपस्थित था?", ["लोहे के हल", "लकड़ी के हल", "पत्थर के हँसिए", "तांबे के फलक"], 0, "लोहे का ज्ञान न होने के कारण लोहे के हलों का पूर्ण अभाव था। वे लकड़ी के हलों का प्रयोग करते थे।"),
    ("हड़प्पा वासियों के भोजन के संदर्भ में, हड्डियों के अवशेष किन पालतू पशुओं के मांस के सेवन को दर्शाते हैं?", ["बैल, भैंस, भेड़, बकरी और सूअर", "चीता, तेंदुआ और शेर", "मुख्य रूप से घोड़ा और गधा", "केवल अफ्रीकी हाथी"], 0, "हड्डियों के ढेर दर्शाते हैं कि वे गाय, भैंस, भेड़, बकरी और सूअर का मांस खाते थे।"),
    ("पाकिस्तान के किस स्थल पर हड़प्पा के समान अन्नागार या ईंटों के विशाल चबूतरे मिले हैं?", ["मोहनजोदड़ो", "कालीबंगन", "लोथल", "सुत्कागेंदोर"], 0, "मोहनजोदड़ो में विशाल अन्नागार और हड़प्पा में कतारबद्ध अन्नागार मिले हैं। कालीबंगन में भी ऐसे चबूतरे मिले हैं।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\n1. हड़प्पा वासी फसलों की सिंचाई के लिए नदियों के प्राकृतिक बाढ़ के पानी पर निर्भर थे।\n2. खेतों में पानी मोड़ने के लिए साधारण बाढ़-नहरें (inundation canals) बनाई गई थीं।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 2, "दोनों कथन सही हैं। वे प्राकृतिक बाढ़ सिंचाई और साधारण जल मोड़ों का उपयोग करते थे।"),
    ("हड़प्पा स्थलों से किन जंगली जानवरों की हड्डियां मिली हैं, जो यह दर्शाती हैं कि उनका शिकार किया जाता था?", ["हिरण, जंगली सूअर और घड़ियाल", "शेर, चीता और जेब्रा", "जिराफ और कंगारू", "अफ्रीकी हाथी"], 0, "हिरण, जंगली सूअर और घड़ियाल की हड्डियां कचरे के ढेरों में मिली हैं, जो शिकार को दर्शाती हैं।"),
    ("निम्नलिखित में से कौन सी फसल हड़प्पा वासियों द्वारा नहीं उगाई जाती थी?", ["गन्ना", "गेहूँ", "जौ", "तिल"], 0, "गन्ने की खेती नहीं की जाती थी; गेहूँ, जौ और तिल उगाए जाते थे।"),
    ("धोलावीरा के बांध कैसे काम करते थे?", ["मनहर और मंदसर नदियों के मौसमी बहाव को जलाशयों की ओर मोड़कर", "ज्वार के समय समुद्र का पानी रोककर", "चक्की चलाने के लिए बिजली पैदा करके", "नावों को तैराने के लिए"], 0, "धोलावीरा के बांध मौसमी नदियों के पानी को रोककर पत्थरों के जलाशयों में भेजने का काम करते थे।"),
    ("मैदानी इलाकों में कटे हुए अनाज को ढोने के लिए मुख्य रूप से किस जानवर का उपयोग किया जाता था?", ["बैल", "घोड़ा", "चीता", "हाथी"], 0, "बैलगाड़ियों को खींचने के लिए बैल ही मुख्य साधन थे।"),
    ("हरियाणा के किस हड़प्पा स्थल से मिट्टी के हल का मॉडल मिला है जिस पर मुड़ा हुआ फलक दर्शाया गया है?", ["बनावली", "राखीगढ़ी", "मिथाथल", "भिराना"], 0, "बनावली से मिट्टी के हल का सबसे प्रसिद्ध खिलौना मॉडल मिला है।"),
    ("लोथल में मिले चावल के साक्ष्यों के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:\n1. बर्तनों की मिट्टी को मजबूती देने के लिए चावल की भूसी मिलाई गई थी।\n2. स्थल से चावल के दानों से भरे बड़े अन्नागार मिले हैं।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि बड़े धान के अन्नागार नहीं मिले हैं, केवल भूसी के निशान मिले हैं।"),
    ("हड़प्पा की कृषि अर्थव्यवस्था को सबसे अच्छी तरह इस प्रकार वर्णित किया जा सकता है:", ["शहरी विशिष्टता को बनाए रखने वाली एक अत्यधिक उत्पादक अधिशेष अर्थव्यवस्था", "एक निर्वाह खानाबदोश पशुपालन अर्थव्यवस्था", "आयात पर निर्भर कृषि प्रणाली", "राज्य के एकाधिकार वाली वृक्षारोपण अर्थव्यवस्था"], 0, "यह एक समृद्ध कृषि अधिशेष अर्थव्यवस्था थी जिसने प्रशासनिक और शिल्पी वर्ग को शहरों में रहने की सुविधा प्रदान की।"),
    ("हड़प्पा वासियों द्वारा निम्नलिखित में से किस तिलहन की खेती की जाती थी?", ["तिल और सरसों", "सूरजमुखी", "सोयाबीन", "जैतून"], 0, "तिल और सरसों ही मुख्य तिलहन फसलें थीं।"),
    ("चोलिस्तान का क्षेत्र कहाँ स्थित है और इसका कृषि के इतिहास में क्या महत्व है?", ["पाकिस्तान का मरुस्थलीय क्षेत्र, जहाँ जवारीवाला से मिट्टी के हल मिले हैं", "बलूचिस्तान का पहाड़ी क्षेत्र, जहाँ बांध मिले हैं", "गुजरात का तटीय क्षेत्र, जहाँ चावल मिले हैं", "पंजाब का मैदान, जहाँ नहरें मिली हैं"], 0, "चोलिस्तान पाकिस्तान के पंजाब का मरुस्थलीय भाग है जहाँ जवारीवाला जैसे स्थलों से मिट्टी के हल मिले हैं।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\n1. हड़प्पा कृषि पूरी तरह से सिंधु नदी से निकलने वाली कृत्रिम नहरों पर निर्भर थी।\n2. कुएं और मौसमी बाढ़ ही मुख्य घाटी में पानी के प्राथमिक स्रोत थे।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["2 केवल", "1 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 0, "कथन 2 सही है। कथन 1 गलत है क्योंकि मैदानों में गाद के कारण नहरें नहीं बचीं।"),
    ("बलूचिस्तान में गबरबंदों (check-dams) का मिलना प्राचीन पर्यावरण के बारे में क्या दर्शाता है?", ["वर्षा मौसमी और दुर्लभ थी, जिससे जल संरक्षण आवश्यक था", "यह क्षेत्र एक उष्णकटिबंधीय वर्षावन था", "समुद्र का स्तर आज से बहुत अधिक था", "नदियाँ साल भर उफान पर रहती थीं"], 0, "गबरबंद यह दर्शाते हैं कि वर्षा कम और मौसमी होती थी, जिससे सूखी नदियों में पानी और गाद रोकना आवश्यक था।"),
    ("हड़प्पा में मिले वृत्ताकार चबूतरों का मुख्य उद्देश्य क्या था?", ["हाथ या पैरों से गेहूँ और जौ की गहाई (threshing) करना", "मंदिरों के लिए चबूतरा बनाना", "भेड़-बकरियों को बाड़े में रखना", "मिट्टी के बर्तन बनाना"], 0, "ये गहाई के खलिहान थे जहाँ अनाज को भूसे से अलग किया जाता था।"),
    ("कपड़ा उत्पादन के लिए हड़प्पा वासियों द्वारा किस रेशे की खेती की जाती थी?", ["कपास", "रेशम", "जूट", "सन (Flax)"], 0, "कपास की खेती की जाती थी जिससे सूती कपड़ा तैयार होता था।"),
    ("हड़प्पा के खेतों में लकड़ी के भारी हलों को खींचने के लिए किस जानवर का उपयोग किया जाता था?", ["कूबड़ वाले बैल", "घोड़े", "हाथी", "शेर"], 0, "हल खींचने के लिए कूबड़ वाले बैलों (zebu) का उपयोग किया जाता था।"),
    ("विभिन्न हड़प्पा शहरों में अन्नागारों का मिलना क्या दर्शाता है?", ["खाद्य सुरक्षा और वितरण की एक केंद्रीकृत प्रणाली", "स्थानीय कृषि ज्ञान की कमी", "कि सभी नागरिक किसान थे", "कि अनाज भंडारण के लिए मेसोपोटामिया से मँगाया जाता था"], 0, "यह राज्य द्वारा प्रबंधित एक मजबूत खाद्य सुरक्षा और आपातकालीन राशन प्रणाली को दर्शाता है।"),
    ("हड़प्पा के वृत्ताकार चबूतरों में पौधों के कौन से अवशेष मिले हैं, जिससे उनके कार्य की पुष्टि होती है?", ["गेहूँ और जौ", "चावल और कपास", "सरसों और तिल", "गन्ना और मसूर"], 0, "चबूतरों के दरारों में गेहूँ और जौ के दानों के अवशेष मिले हैं।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\n1. ऊंट हड़प्पा वासियों को ज्ञात था और उसे पालतू बनाया गया था।\n2. कालीबंगन जैसे स्थलों से ऊंट की हड्डियां मिली हैं।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 2, "दोनों कथन सही हैं। ऊंट का उपयोग भार ढोने के लिए किया जाता था।"),
    ("हड़प्पा के कृषि क्षेत्र मुख्य रूप से कहाँ स्थित थे?", ["नदियों के जलोढ़ बाढ़ के मैदानों में", "पर्वतों की ढलानों पर", "घने जंगलों को साफ करके", "तटीय दलदली क्षेत्रों में"], 0, "खेत नदियों की लाई गई उपजाऊ जलोढ़ (alluvial) मिट्टी के मैदानों में स्थित थे।"),
    ("भारत के किस राज्य से हड़प्पा कालीन कृषि बस्तियां और बाजरे के सर्वाधिक साक्ष्य मिले हैं?", ["गुजरात", "पंजाब", "राजस्थान", "उत्तर प्रदेश"], 0, "गुजरात के शुष्क ग्रामीण स्थलों से बाजरे की खेती के सर्वाधिक साक्ष्य मिले हैं।"),
    ("गुजरात के धोलावीरा में जल प्रबंधन की कौन सी अनूठी संरचना खोजी गई है?", ["चट्टानों को काटकर बनाए गए जलाशय", "पकी ईंटों का गोदीवाड़ा", "स्वचालित साइफन नहर", "पानी की चक्की वाला कुआं"], 0, "चट्टानों को काटकर बनाए गए विशाल जलाशयों की श्रृंखला धोलावीरा की अनूठी विशेषता है।"),
    ("हड़प्पा वासियों के भोजन में मछली की क्या भूमिका थी?", ["मछली और जलीय जीवों का व्यापक उपभोग होता था, विशेष रूप से तटीय स्थलों पर", "मछली खाना मना था", "वे केवल मीठे पानी की मछली खाते थे, समुद्री नहीं", "मछली केवल सूखी हुई अवस्था में मेसोपोटामिया से आयात होती थी"], 0, "तटीय और अंतर्देशीय स्थलों से मिली मछलियों की हड्डियाँ और तांबे के कांटे यह दर्शाते हैं कि मछली भोजन का मुख्य हिस्सा थी।"),
    ("कालीबंगन में ग्रिड पैटर्न में दोहरी जुताई का क्या लाभ था?", ["इससे दो फसलें (एक लंबी, एक छोटी) बिना एक-दूसरे को प्रभावित किए उगाई जा सकती थीं", "यह ऊपरी मिट्टी के कटाव को रोकता था", "यह वर्षा देवता को समर्पित एक धार्मिक डिजाइन था", "यह दर्शाता है कि खेत को दो अलग-अलग पशुओं से जोता गया था"], 0, "ग्रिड पैटर्न में एक दिशा की रेखाएं चौड़ी और दूसरी दिशा की संकरी थीं, जिससे दो फसलें साथ में उगाई जा सकती थीं।"),
    ("किस पशु की हड्डियाँ हड़प्पा परतों में दुर्लभ हैं लेकिन उत्तरवर्ती वैदिक परतों में प्रचुर हैं, जो एक सांस्कृतिक बदलाव दर्शाती हैं?", ["घोड़ा", "कूबड़ वाला बैल", "भैंस", "बकरी"], 0, "घोड़े के अवशेष हड़प्पा परतों में अत्यंत विवादास्पद/दुर्लभ हैं, लेकिन ऋग्वैदिक/वैदिक काल में बहुत आम हो जाते हैं।"),
    ("नदियों के मार्ग बदलने ने हड़प्पा कृषि के पतन में कैसे योगदान दिया?", ["खेतों को पानी से वंचित कर दिया, जिससे उपजाऊ क्षेत्र रेगिस्तान में बदल गए", "एक ही दिन में पूरी सभ्यता को डुबो दिया", "व्यापारिक जहाजों को चलाना असंभव बना दिया", "नदी के पानी को जहरीला बना दिया"], 0, "नदियों के मार्ग बदलने (जैसे सतलुज और यमुना का घग्गर से हटना) ने उपजाऊ कृषि भूमि को पानी से वंचित कर शुष्क बना दिया।")
]

# Translate mock to Hindi
mock_raw_hin = [
    ("सिंधु घाटी सभ्यता की कृषि तकनीक के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. बनावली और चोलिस्तान से मिट्टी के हलों के मॉडल मिले हैं।\n2. कालीबंगन में खोजा गया जुता हुआ खेत परिपक्व हड़प्पा काल का है।\n3. हड़प्पा वासी शीतकालीन गेहूँ काटने के लिए लोहे के भारी हँसियों का उपयोग करते थे।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "1 और 2 केवल", "2 और 3 केवल", "1, 2 और 3"], 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि कालीबंगन का जुता हुआ खेत प्रारंभिक हड़प्पा स्तर का है। कथन 3 गलत है क्योंकि लोहे का ज्ञान नहीं था; वे चर्ट के हँसियों का उपयोग करते थे।"),
    ("निम्नलिखित में से कौन से युग्म सही सुमेलित हैं?\nपुरातात्विक स्थल - कृषि खोज\n1. कालीबंगन - ग्रिड पैटर्न में जुता हुआ खेत\n2. बनावली - मिट्टी के हल का मॉडल\n3. शोर्तुघई - पत्थरों से बनी सिंचाई नहर प्रणाली\nनीचे दिए गए कूट का प्रयोग कर सही उत्तर चुनिए:", ["1 और 2 केवल", "2 और 3 केवल", "1 and 3 केवल", "1, 2 और 3"], 3, "तीनों युग्म सही सुमेलित हैं। कालीबंगन से जुता खेत, बनावली से हल का मॉडल और शोर्तुघई से नहरें मिली हैं।"),
    ("हड़प्पा सभ्यता में फसल की खेती के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:\n1. उत्तरी मैदानों में गेहूँ और जौ मुख्य शीतकालीन फसलें थीं।\n2. सिंध के मुख्य जलोढ़ मैदानों में धान (चावल) की व्यापक खेती की जाती थी।\n3. हड़प्पा वासी विश्व में सबसे पहले कपास उगाने वाले और बुनने वाले लोग थे।\nउपर्युक्त कथनों में से कौन-सा/से सही हैं?", ["1 और 2 केवल", "2 और 3 केवल", "1 और 3 केवल", "1, 2 और 3"], 2, "कथन 1 और 3 सही हैं। कथन 2 गलत है क्योंकि चावल केवल गुजरात में स्थानीय स्तर पर उगाया जाता था, सिंध में नहीं।"),
    ("सिंधु घाटी सभ्यता की जल प्रबंधन प्रणालियों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. पत्थरों से बने जलाशयों द्वारा वर्षा जल संचयन धोलावीरा की एक अनूठी विशेषता थी।\n2. गबरबंद बलूचिस्तान की मौसमी नदियों पर बनाए गए पत्थर के बांध थे।\n3. सिंध के जलोढ़ मैदानों में नहरें ही सिंचाई का प्राथमिक स्रोत थीं।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 और 2 केवल", "2 और 3 केवल", "1 और 3 केवल", "1, 2 और 3"], 0, "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि मैदानों में गाद जमने के कारण नहरें नहीं बचीं; कुएं और बाढ़ ही मुख्य थे।"),
    ("हड़प्पा समाज में पशुओं को पालतू बनाने के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:\n1. दूध और माल ढोने के लिए कूबड़ वाले बैल और भैंस पाले जाते थे।\n2. शाही सत्ता को दर्शाने के लिए प्रशासनिक मुहरों पर घोड़े का व्यापक अंकन मिलता था।\n3. ऊंट और गधों की हड्डियां उनके मालवाहक पशुओं के रूप में उपयोग को दर्शाती हैं।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 और 3 केवल", "1 and 2 केवल", "2 और 3 केवल", "1, 2 और 3"], 0, "कथन 1 और 3 सही हैं। कथन 2 गलत है क्योंकि मुहरों पर घोड़े का कोई अंकन नहीं मिलता है।"),
    ("निम्नलिखित में से कौन सा कथन सबसे अच्छी तरह यह स्पष्ट करता है कि उत्तर हड़प्पा काल में कृषि अधिशेष क्यों घट गया?", ["ग्रीष्मकालीन मानसून के कमजोर होने और नदियों के मार्ग बदलने से खेतों को पानी मिलना बंद हो गया", "फसलों के चक्रण न होने के कारण मिट्टी के सारे पोषक तत्व समाप्त हो गए", "मेसोपोटामिया के व्यापारियों ने सिंधु घाटी को खादों का निर्यात बंद कर दिया", "एक भयानक महामारी ने सभी पालतू बैलों को नष्ट कर दिया"], 0, "मानसून का कमजोर होना और नदियों (जैसे घग्गर-हकरा) के मार्ग बदलने/सूखने से पानी की कमी हुई, जिससे कृषि उत्पादकता समाप्त हो गई और शहरों का पतन हुआ।"),
    ("सिंधु घाटी सभ्यता में अन्नागारों के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:\n1. मोहनजोदड़ो के विशाल अन्नागार में ऊंचे लकड़ी के ढांचे और हवा के मार्ग बने थे।\n2. हड़प्पा में अन्नागारों के पास ईंटों के वृत्ताकार चबूतरे मिले हैं जो गहाई के फर्श थे।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "Both 1 और 2", "न तो 1 न ही 2"], 2, "दोनों कथन सही हैं। अन्नागारों में हवा के मार्ग थे और हड़प्पा में अनाज की गहाई के लिए वृत्ताकार फर्श मिले हैं।"),
    ("हड़प्पा वासियों द्वारा निम्नलिखित में से किन फसलों की खेती की जाती थी?\n1. गेहूँ और जौ\n2. सरसों और तिल\n3. बाजरा\n4. गन्ना\nनीचे दिए गए कूट का प्रयोग कर सही उत्तर चुनिए:", ["1, 2 और 3 केवल", "1, 2 और 4 केवल", "2, 3 और 4 केवल", "1, 2, 3 और 4"], 0, "गेहूँ, जौ, सरसों, तिल और बाजरा उगाए जाते थे। गन्ने का ज्ञान हड़प्पा वासियों को नहीं था।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: यूनानियों ने कपास को 'सिंडन' कहा, जो भाषाई रूप से 'सिंधु' शब्द से बना है।\nकथन 2: हड़प्पा वासी चांदी और कोलतार के बदले मेसोपोटामिया को सूती कपड़ों का निर्यात करते थे।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 2, "दोनों कथन सही हैं। यूनानियों ने कपास को सिंडन कहा और सूती कपड़े मेसोपोटामिया को निर्यात किए जाते थे।"),
    ("निम्नलिखित में से कौन से युग्म सही सुमेलित हैं?\nपुरातात्विक खोज - हड़प्पा स्थल\n1. बर्तनों में धान की भूसी - लोथल\n2. घोड़े के अस्थि अवशेष - सुरकोटदा\n3. मिट्टी के हल का मॉडल - बनावली\nनीचे दिए गए कूट का प्रयोग कर सही उत्तर चुनिए:", ["1 और 2 केवल", "2 और 3 केवल", "1 और 3 केवल", "1, 2 और 3"], 3, "तीनों युग्म सही सुमेलित हैं। लोथल से भूसी, सुरकोटदा से घोड़े की हड्डियां और बनावली से हल का खिलौना मिला है।")
]

# Compile practiceQuestions
for idx, (q, opts, ans, sol) in enumerate(practice_raw_eng):
    eng_data["practiceQuestions"].append({
        "id": f"ag-prac-{idx+1}",
        "q": q,
        "opts": opts,
        "ans": ans,
        "sol": sol
    })

for idx, (q, opts, ans, sol) in enumerate(practice_raw_hin):
    hin_data["practiceQuestions"].append({
        "id": f"ag-prac-hin-{idx+1}",
        "q": q,
        "opts": opts,
        "ans": ans,
        "sol": sol
    })

# Compile mockQuestions
for idx, (q, opts, ans, sol) in enumerate(mock_raw_eng):
    eng_data["mockTestQuestions"].append({
        "id": f"ag-mock-{idx+1}",
        "q": q,
        "opts": opts,
        "ans": ans,
        "sol": sol
    })

for idx, (q, opts, ans, sol) in enumerate(mock_raw_hin):
    hin_data["mockTestQuestions"].append({
        "id": f"ag-mock-hin-{idx+1}",
        "q": q,
        "opts": opts,
        "ans": ans,
        "sol": sol
    })

# Save English content
eng_file = os.path.join(ENG_DIR, "content.json")
with open(eng_file, "w", encoding="utf-8") as f:
    json.dump(eng_data, f, ensure_ascii=False, indent=2)
print(f"Writing English base content to {eng_file}")

# Save Hindi content
hin_file = os.path.join(HIN_DIR, "content.json")
with open(hin_file, "w", encoding="utf-8") as f:
    json.dump(hin_data, f, ensure_ascii=False, indent=2)
print(f"Writing Hindi base content to {hin_file}")

print("Base build script executed successfully!")
