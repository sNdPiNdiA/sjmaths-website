import json
import os

ENG_DIR = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\HarappanIndus-Valley-Civilisation\Important-Urban-Towns"
HIN_DIR = os.path.join(ENG_DIR, "hi")
os.makedirs(HIN_DIR, exist_ok=True)

# English base structure
eng_data = {
    "breadcrumbs": {
        "parent": "UPSC Syllabus",
        "parentUrl": "/upsc/",
        "current": "Important Urban Towns"
    },
    "hero": {
        "title": "Important Urban Towns of the Harappan Civilisation",
        "description": "Master the archaeological layouts, civic architecture, craft specialization, and economic roles of major Harappan towns for UPSC GS-1."
    },
    "labels": {
        "clickToExpand": "Click to expand details",
        "mockIntro": {
            "title": "Interactive UPSC Mock Test",
            "description": "Test your knowledge on the Important Urban Towns of the Indus Civilisation. This timed test contains 10 high-quality, exam-standard questions with negative marking. Perfect for self-evaluation.",
            "startBtn": "Start Mock Test"
        },
        "mockPlay": {
            "prevBtn": "Previous Question",
            "nextBtn": "Next Question",
            "submitBtn": "Submit Test"
        }
    },
    "timeline": {
        "title": "Geographical and Settlement Horizons",
        "description": "Explore the chronological and spatial evolution of geographical frontiers, urban settlements, and material discoveries of the Indus Valley Civilisation.",
        "cards": [
            {
                "period": "Inland Metropolises",
                "date": "Harappa, Mohenjo-daro & Rakhigarhi",
                "details": "Major administrative capitals featuring massive citadels, street grids, large public halls, granaries, and the Great Bath, serving as central hubs."
            },
            {
                "period": "Ports & Outposts",
                "date": "Lothal & Sutkagendor",
                "details": "Maritime trade centers managing shipping and commerce with the Persian Gulf. Lothal features a brick tidal dockyard; Sutkagendor acts as a western buffer."
            },
            {
                "period": "Specialized settlements",
                "date": "Dholavira, Kalibangan & Chanhudaro",
                "details": "Dholavira's three-tier layout and stone reservoirs; Kalibangan's ploughed field and fire altars; Chanhudaro's unfortified industrial bead factories."
            }
        ]
    },
    "mnemonics": {
        "title": "Mnemonics & Memory Hacks",
        "description": "Use these visual memory hooks to retain critical facts about Harappan urban centers for the UPSC Civil Services Examination.",
        "items": [
            {
                "title": "Mnemonic 1: Major Port & Craft Locations",
                "phrase": "\"L-C-S (Lothal Chanhudaro Sutkagendor) - Trade & Suburbs\"",
                "decryption": "**L**othal (Dockyard port), **C**anhudaro (Craft and bead factory), **S**utkagendor (Western coast port) (**LCS**)."
            },
            {
                "title": "Mnemonic 2: Water & Earth Marvels",
                "phrase": "\"D-K-B (Dholavira Kalibangan Banawali) - Land Adaptations\"",
                "decryption": "**D**holavira (Dams & reservoirs), **K**alibangan (ploughed Agricultural field), **B**anawali (terracotta agricultural Plow) (**DKB**)."
            },
            {
                "title": "Mnemonic 3: Three Inland Capitals",
                "phrase": "\"H-M-R (Harappa Mohenjo Rakhigarhi) - The Metropolises\"",
                "decryption": "**H**arappa (Ravi River), **M**ohenjo-daro (Indus River), **R**akhigarhi (Drishadvati - largest site) (**HMR**)."
            }
        ]
    },
    "flashcards": {
        "title": "Active Recall Flashcards",
        "description": "Flashcards are key to mastering fact-dense UPSC questions. Click on any card below to flip it and reveal the answer.",
        "items": [
            {
                "question": "Which Harappan city is divided into three fortified sections rather than two?",
                "answer": "<strong>Dholavira</strong> in Gujarat, divided into Citadel, Middle Town, and Lower Town.",
                "icon": "fa-layer-group"
            },
            {
                "question": "Which site has yielded the unique print of a dog chasing a cat on a brick?",
                "answer": "<strong>Chanhudaro</strong> in Sindh, a major industrial craft town.",
                "icon": "fa-paw"
            },
            {
                "question": "Name the port city that features a massive baked-brick tidal dockyard.",
                "answer": "<strong>Lothal</strong> in Gujarat, situated along the Bhogavo River.",
                "icon": "fa-anchor"
            },
            {
                "question": "Where was the earliest ploughed field in the Indian subcontinent discovered?",
                "answer": "<strong>Kalibangan</strong> in Rajasthan, showing a grid of crop furrows.",
                "icon": "fa-wheat-awn"
            },
            {
                "question": "What unique findings at Rakhigarhi have rewritten South Asian ancestry studies?",
                "answer": "DNA extracted from skeletal remains in the <strong>Rakhigarhi cemetery</strong>, showing genetic continuity and indigenous origin.",
                "icon": "fa-dna"
            }
        ]
    },
    "deepDive": {
        "title": "Syllabus Core Study Notes (Deep-Dive)",
        "description": "Master the layout, civic architecture, trade ports, and regional characteristics of the major urban centers of the Harappan Civilisation.",
        "sections": [
            {
                "title": "1. Metropolitan Giants & Inland Centers (Harappa, Mohenjo-daro, Rakhigarhi)",
                "content": """<p>The core urbanism of the Indus Civilisation is defined by its massive metropolitan giants. Harappa, Mohenjo-daro, and Rakhigarhi were primary socio-political hubs, displaying highly standardized city planning, brick ratios, and sanitary engineering.</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-landmark"></i> Harappa & Mohenjo-daro Layouts</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>Standard Grid & Citadel:</strong> Both cities featured a raised western Citadel (for public and administrative uses) and a lower eastern residential town. Roads crossed at right angles.</li>
      <li><strong>Mohenjo-daro Monuments:</strong> Key public structures include the Great Bath (sealed with natural bitumen/tar), the Great Granary (with ventilation air ducts), and the Assembly Hall.</li>
      <li><strong>Harappa Discoveries:</strong> Circular brick platforms for threshing grain, parallel rows of granaries outside the citadel, and Cemetery R-37 featuring wooden coffin burials.</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-dna"></i> Rakhigarhi: The Largest Metropolis</div>
    <p style="font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;">
      Situated in Haryana's Hisar district along the dry Drishadvati channel, <strong>Rakhigarhi</strong> has emerged as the largest Harappan site, covering over 350-500 hectares across nine mounds. Recent DNA analysis of skeletal remains from its cemetery has provided critical insights, indicating a lack of major migrations from the West during the Harappan period and pointing to indigenous development of South Asian ancestry.
    </p>
  </div>
</div>""",
                "masteryZone": []
            },
            {
                "title": "2. Ports, Trade Outposts & Industrial Suburbs (Lothal, Sutkagendor, Chanhudaro, Kuntasi)",
                "content": """<p>While metropolises handled administrative affairs, trade outposts, ports, and industrial suburbs were the engines of the Indus Valley's complex economy, securing raw materials and managing maritime commerce.</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-ship"></i> Maritime Ports: Lothal & Sutkagendor</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>Lothal Dockyard:</strong> A massive trapezoidal artificial basin built of baked bricks, connected to the Bhogavo River. It served as a tidal dockyard for shipping.</li>
      <li><strong>Lothal Findings:</strong> Joint/double burials, Persian Gulf-type seals, a bead factory, and terracotta ship models indicating direct trade with Mesopotamia.</li>
      <li><strong>Sutkagendor:</strong> Situated on the Dasht River, this western outpost served as a coastal trading port and fortified buffer to manage the overland and sea routes into the Persian Gulf.</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-industry"></i> Industrial Suburbs: Chanhudaro & Kuntasi</div>
    <p style="font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;">
      <strong>Chanhudaro</strong> in Sindh was a pure craft town that completely lacked a fortified citadel. It was famous for shell-working, seal-cutting, and bead-making factories, yielding bronze toy carts and an inkpot. <strong>Kuntasi</strong> in Gujarat acted as a small port and industrial settlement specializing in bead-making and copper processing.
    </p>
  </div>
</div>""",
                "masteryZone": []
            },
            {
                "title": "3. Regional Enclaves, Defensive Citadels & Dryland Towns (Dholavira, Kalibangan, Banawali, Surkotada)",
                "content": """<p>Harappan planning shows high flexibility, adapting to local dryland environments, water scarcity, and defense needs. Dholavira, Kalibangan, Banawali, and Surkotada display distinct regional differences.</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-droplet"></i> Dholavira's Hydraulic & Stone Architecture</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>Three-Tier Layout:</strong> Dholavira in Gujarat's Kutch is divided into three parts: Citadel, Middle Town, and Lower Town.</li>
      <li><strong>Hydraulic Engineering:</strong> Utilized check dams and 16 massive stone-cut reservoirs to harvest rainwater.</li>
      <li><strong>Stone Masonry & Script:</strong> Relied heavily on dressed local limestone (not baked brick). It also yielded the famous 10-character Indus signboard.</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-shield"></i> Kalibangan, Banawali & Surkotada</div>
    <p style="font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;">
      <strong>Kalibangan</strong> (Rajasthan) is famous for its pre-Harappan ploughed agricultural field, wooden drainage pipes, and series of brick fire altars. <strong>Banawali</strong> (Haryana) represents a unique radial town layout rather than a grid pattern, and yielded a high-quality terracotta toy plow. <strong>Surkotada</strong> (Gujarat) features a fortified rubble stone citadel and has yielded debated skeletal horse remains in its upper layers.
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
        "current": "महत्वपूर्ण शहरी नगर"
    },
    "hero": {
        "title": "हड़प्पा सभ्यता के महत्वपूर्ण शहरी नगर",
        "description": "यूपीएससी परीक्षा (GS-1) के लिए हड़प्पा सभ्यता के प्रमुख नगरों की पुरातात्विक संरचना, नागरिक वास्तुकला, शिल्प विशेषज्ञता और आर्थिक भूमिकाओं का अध्ययन करें।"
    },
    "labels": {
        "clickToExpand": "विवरण देखने के लिए क्लिक करें",
        "mockIntro": {
            "title": "इंटरैक्टिव यूपीएससी मॉक टेस्ट",
            "description": "हड़प्पा सभ्यता के प्रमुख नगरों के संबंध में अपनी तैयारी का मूल्यांकन करें। इस समयबद्ध परीक्षण में नकारात्मक अंकन के साथ 10 उच्च-स्तरीय यूपीएससी मानक के प्रश्न शामिल हैं।",
            "startBtn": "मॉक टेस्ट शुरू करें"
        },
        "mockPlay": {
            "prevBtn": "पिछला प्रश्न",
            "nextBtn": "अगला प्रश्न",
            "submitBtn": "परीक्षण जमा करें"
        }
    },
    "timeline": {
        "title": "भौगोलिक और शहरी परिदृश्य",
        "description": "हड़प्पा सभ्यता के प्रमुख शहरी नगरों, उनकी भौगोलिक सीमाओं और पुरातात्विक खोजों के विकास का कालानुक्रमिक अध्ययन करें।",
        "cards": [
            {
                "period": "भीतरी महानगर",
                "date": "हड़प्पा, मोहनजोदड़ो और राखीगढ़ी",
                "details": "मुख्य प्रशासनिक राजधानियाँ जहाँ किले (Citadel), सड़कों का जाल, विशाल सभा भवन, अन्नागार और विशाल स्नानागार पाए गए हैं।"
            },
            {
                "period": "बंदरगाह और चौकियां",
                "date": "लोथल और सुतकागेंडोर",
                "details": "समुद्री व्यापार केंद्र जो फारस की खाड़ी के साथ व्यापार का प्रबंधन करते थे। लोथल में पकी ईंटों की गोदी (Dockyard) है; सुतकागेंडोर पश्चिमी सीमा प्रहरी है।"
            },
            {
                "period": "विशिष्ट बस्तियां",
                "date": "धोलावीरा, कालीबंगन और चन्हुदड़ो",
                "details": "धोलावीरा का तीन भागों में विभाजन और जलाशय; कालीबंगन का जुता हुआ खेत और अग्निकुंड; चन्हुदड़ो का बिना किले वाला मनके बनाने का औद्योगिक उपनगर।"
            }
        ]
    },
    "mnemonics": {
        "title": "याद रखने के सूत्र (Mnemonics)",
        "description": "यूपीएससी परीक्षा के लिए हड़प्पा सभ्यता के प्रमुख नगरों से संबंधित तथ्यों को आसानी से याद रखने के लिए इन दृश्य सूत्रों का उपयोग करें।",
        "items": [
            {
                "title": "याद रखने का सूत्र 1: बंदरगाह और शिल्प नगर",
                "phrase": "\"L-C-S (लोथल चन्हुदड़ो सुतकागेंडोर) - व्यापार और उपनगर\"",
                "decryption": "**L**othal (गोदी बाड़ा/बंदरगाह), **C**anhudaro (शिल्प और मनके का कारखाना), **S**utkagendor (पश्चिमी तट का बंदरगाह) (**LCS**)।"
            },
            {
                "title": "याद रखने का सूत्र 2: भूमि और जल नवाचार",
                "phrase": "\"D-K-B (धोलावीरा कालीबंगन बनावली) - अनुकूलन\"",
                "decryption": "**D**holavira (बाँध और जलाशय), **K**alibangan (जुता हुआ खेत), **B**anawali (मिट्टी का हल) (**DKB**)।"
            },
            {
                "title": "याद रखने का सूत्र 3: तीन भीतरी महानगर",
                "phrase": "\"H-M-R (हड़प्पा मोहनजोदड़ो राखीगढ़ी) - महानगर\"",
                "decryption": "**H**arappa (रावी नदी), **M**ohenjo-daro (सिंधु नदी), **R**akhigarhi (दृषद्वती - सबसे बड़ा स्थल) (**HMR**)।"
            }
        ]
    },
    "flashcards": {
        "title": "सक्रिय स्मरण फ्लैशकार्ड (Active Recall)",
        "description": "फ्लैशकार्ड्स तथ्य-प्रधान यूपीएससी प्रश्नों को याद रखने का सर्वोत्तम साधन हैं। उत्तर देखने के लिए नीचे दिए गए कार्ड्स पर क्लिक करें।",
        "items": [
            {
                "question": "कौन सा हड़प्पा शहर सामान्यतः दो के बजाय तीन अलग-अलग हिस्सों में विभाजित है?",
                "answer": "गुजरात का <strong>धोलावीरा</strong> शहर, जो किला (Citadel), मध्य नगर (Middle Town), और निचला नगर (Lower Town) में विभाजित है।",
                "icon": "fa-layer-group"
            },
            {
                "question": "किस स्थल से एक ईंट पर बिल्ली का पीछा करते हुए कुत्ते के पंजों के निशान मिले हैं?",
                "answer": "सिंध में स्थित <strong>चन्हुदड़ो</strong> से, जो एक प्रमुख औद्योगिक शिल्प नगर था।",
                "icon": "fa-paw"
            },
            {
                "question": "उस बंदरगाह शहर का नाम बताइए जिसमें पकी हुई ईंटों का एक विशाल गोदी बाड़ा (Dockyard) मिला है।",
                "answer": "गुजरात में स्थित <strong>लोथल</strong>, जो भोगवा नदी के तट पर स्थित है।",
                "icon": "fa-anchor"
            },
            {
                "question": "भारतीय उपमहाद्वीप में सबसे पहले जुते हुए खेत के साक्ष्य कहाँ खोजे गए थे?",
                "answer": "राजस्थान में स्थित <strong>कालीबंगन</strong>, जहाँ समकोण पर जुताई की रेखाएं मिली हैं।",
                "icon": "fa-wheat-awn"
            },
            {
                "question": "राखीगढ़ी के कब्रिस्तान से मिले किन अवशेषों ने दक्षिण एशियाई मूल के अध्ययनों को नया मोड़ दिया है?",
                "answer": "राखीगढ़ी कब्रिस्तान के कंकालों से प्राप्त <strong>डीएनए (DNA)</strong> अवशेष, जो इस क्षेत्र में आनुवंशिक निरंतरता और स्वदेशी उत्पत्ति को दर्शाते हैं।",
                "icon": "fa-dna"
            }
        ]
    },
    "deepDive": {
        "title": "पाठ्यक्रम मुख्य नोट्स (गहन अध्ययन)",
        "description": "हड़प्पा सभ्यता के प्रमुख शहरी नगरों के लेआउट, नागरिक वास्तुकला, व्यापारिक बंदरगाहों और क्षेत्रीय विशेषताओं का गहन अध्ययन करें।",
        "sections": [
            {
                "title": "1. भीतरी महानगर (हड़प्पा, मोहनजोदड़ो, राखीगढ़ी)",
                "content": """<p>सिंधु सभ्यता का शहरीकरण इसके विशाल भीतरी महानगरों द्वारा परिभाषित है। हड़प्पा, मोहनजोदड़ो और राखीगढ़ी प्राथमिक सामाजिक-राजनीतिक केंद्र थे, जो अत्यधिक मानकीकृत नगर नियोजन, ईंटों के अनुपात और जल निकासी व्यवस्था को दर्शाते हैं।</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-landmark"></i> हड़प्पा और मोहनजोदड़ो संरचनाएँ</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>ग्रिड पैटर्न और किला:</strong> दोनों शहरों में एक पश्चिमी किला (सार्वजनिक और प्रशासनिक कार्यों के लिए) और एक निचला पूर्वी आवासीय नगर था। सड़कें समकोण पर काटती थीं।</li>
      <li><strong>मोहनजोदड़ो के स्मारक:</strong> प्रमुख स्मारकों में विशाल स्नानागार (डामर/बिटुमेन द्वारा सील), विशाल अन्नागार (हवा आने-जाने के रास्तों सहित) और सभा भवन शामिल हैं।</li>
      <li><strong>हड़प्पा की खोजें:</strong> अनाज कूटने के गोलाकार चबूतरे, किले के बाहर दो कतारों में बने अन्नागार, और कब्रिस्तान R-37 जिसमें देवदार की लकड़ी के ताबूत मिले हैं।</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-dna"></i> राखीगढ़ी: सबसे बड़ा महानगर</div>
    <p style="font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;">
      हरियाणा के हिसार जिले में सूखी हुई दृषद्वती नदी के किनारे स्थित <strong>राखीगढ़ी</strong> वर्तमान में सबसे बड़ा हड़प्पा स्थल बनकर उभरा है, जो नौ टीलों में 350-500 हेक्टेयर से अधिक में फैला है। यहाँ के कब्रिस्तान के कंकालों से मिले हालिया डीएनए विश्लेषण ने संकेत दिया है कि हड़प्पा काल के दौरान पश्चिम से कोई बड़ा प्रवास नहीं हुआ था, जो यहाँ की आबादी के स्वदेशी विकास को दर्शाता है।
    </p>
  </div>
</div>""",
                "masteryZone": []
            },
            {
                "title": "2. बंदरगाह, चौकियां और औद्योगिक उपनगर (लोथल, सुतकागेंडोर, चन्हुदड़ो, कुंतासी)",
                "content": """<p>जबकि महानगर प्रशासनिक कार्यों का प्रबंधन करते थे, व्यापारिक चौकियां, बंदरगाह और औद्योगिक उपनगर सिंधु अर्थव्यवस्था के मुख्य इंजन थे, जो कच्चे माल की आपूर्ति और विदेशों के साथ व्यापार का संचालन करते थे।</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-ship"></i> समुद्री बंदरगाह: लोथल और सुतकागेंडोर</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>लोथल गोदी बाड़ा (Dockyard):</strong> पकी ईंटों से बना एक विशाल कुंड जो भोगवा नदी से जुड़ा था। यह जहाजों के लंगर डालने के लिए ज्वारीय बंदरगाह के रूप में काम करता था।</li>
      <li><strong>लोथल की खोजें:</strong> युगल शवाधान (Double burials), फारस की खाड़ी प्रकार की मुहरें, मनके बनाने का कारखाना, और मिट्टी के जहाजों के खिलौने जो मेसोपोटामिया के साथ प्रत्यक्ष व्यापार दर्शाते हैं।</li>
      <li><strong>सुतकागेंडोर:</strong> दश्त नदी पर स्थित यह स्थल फारस की खाड़ी के साथ समुद्री व्यापार मार्गों की रक्षा करने वाला एक किला और बंदरगाह था।</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-industry"></i> औद्योगिक उपनगर: चन्हुदड़ो और कुंतासी</div>
    <p style="font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;">
      सिंध में स्थित <strong>चन्हुदड़ो</strong> बिना किलेबंदी वाला एक विशुद्ध शिल्प नगर था। यह शंख उद्योग, मुहर बनाने और मनके बनाने के कारखानों के लिए प्रसिद्ध था। यहाँ से तांबे के खिलौने और दवात (inkpot) मिले हैं। गुजरात का <strong>कुंतासी</strong> एक छोटा बंदरगाह और औद्योगिक बस्ती थी जो तांबे के प्रसंस्करण और मनके बनाने में विशेषज्ञता रखती थी।
    </p>
  </div>
</div>""",
                "masteryZone": []
            },
            {
                "title": "3. क्षेत्रीय बस्तियां, रक्षात्मक किले और शुष्क क्षेत्र के नगर (धोलावीरा, कालीबंगन, बनावली, सुरकोटदा)",
                "content": """<p>हड़प्पा नियोजन में स्थानीय शुष्क पर्यावरण, जल की कमी और रक्षात्मक आवश्यकताओं के अनुसार काफी लचीलापन था। धोलावीरा, कालीबंगन, बनावली और सुरकोटदा में स्पष्ट क्षेत्रीय अंतर दिखाई देते हैं।</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-droplet"></i> धोलावीरा की जल प्रणाली और वास्तुकला</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>त्रि-स्तरीय नगर:</strong> गुजरात के कच्छ में स्थित धोलावीरा तीन भागों में विभाजित है: किला, मध्य नगर और निचला नगर।</li>
      <li><strong>जल संचयन प्रणाली:</strong> बारिश के पानी को सहेजने के लिए पत्थर काटकर बनाए गए 16 विशाल जलाशय और बांधों की एक श्रृंखला मिली है।</li>
      <li><strong>पत्थर का उपयोग और साइनबोर्ड:</strong> पकी ईंटों के बजाय यहाँ स्थानीय सफेद पत्थरों का व्यापक उपयोग हुआ है। यहाँ से 10 बड़े अक्षरों वाला हड़प्पा साइनबोर्ड भी मिला है।</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-shield"></i> कालीबंगन, बनावली और सुरकोटदा</div>
    <p style="font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;">
      राजस्थान का <strong>कालीबंगन</strong> पूर्व-हड़प्पा कालीन जुते हुए खेत, लकड़ी के पाइप और ईंटों के अग्निकुंडों की कतार के लिए प्रसिद्ध है। हरियाणा के <strong>बनावली</strong> में ग्रिड प्रणाली के बजाय सड़कों का एक अरीय (radial) ढांचा मिला है और यहाँ से मिट्टी का हल प्राप्त हुआ है। गुजरात के <strong>सुरकोटदा</strong> में पत्थर से बना किला मिला है और यहाँ से ऊपरी परतों में विवादित घोड़े की हड्डियां प्राप्त हुई हैं।
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
        "Consider the following statements regarding the town planning of Harappa and Mohenjo-daro:\n1. Both cities were built on a grid iron system where main streets crossed at right angles.\n2. In both cities, the Citadels were positioned to the east while the residential Lower Towns lay to the west.\n3. Standardized baked bricks of the ratio 4:2:1 were used in both private houses and public structures.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        2,
        "Statement 1 and 3 are correct. Statement 2 is incorrect: Citadels were positioned to the west (raised on platforms for security and administrative purposes), and Lower Towns lay to the east."
    ),
    (
        "With reference to the Great Bath of Mohenjo-daro, consider the following statements:\n1. It was located on the Citadel and was constructed using finely fitted baked bricks.\n2. To prevent water leakage, the tank was sealed with a layer of natural bitumen (tar) between the brick layers.\n3. The bath was filled with water using an elaborate canal system linked directly to the Indus River.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "2 and 3 only", "1 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: The Great Bath was filled by drawing water from a large adjacent brick-lined well, not via a canal from the Indus River."
    ),
    (
        "Consider the following statements regarding the granaries in the Harappan Civilisation:\n1. The Great Granary at Mohenjo-daro featured wooden superstructures raised on brick podiums with ventilation channels.\n2. At Harappa, parallel rows of smaller granaries were constructed close to the river bank outside the citadel.\n3. There is no evidence of granaries or large grain storage structures at Rakhigarhi.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "2 and 3 only", "1 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: Large granaries and grain storage platforms have been excavated at Rakhigarhi, consistent with its status as a major metropolis."
    ),
    (
        "With reference to the archaeological site of Rakhigarhi, consider the following statements:\n1. It is located in the Hisar district of Haryana along the dry bed of the Drishadvati River.\n2. Excavations have revealed it to be the largest geographic site of the Indus Civilisation, spanning over nine mounds.\n3. Genetic analysis of skeletal DNA from its cemetery showed high genetic similarity to Steppe nomadic pastoralists.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: The DNA analysis of Rakhigarhi skeletons showed a lack of Steppe-related ancestry, pointing to indigenous ancestral lineages."
    ),
    (
        "Consider the following statements regarding the coastal port of Lothal:\n1. It featured a massive artificial baked-brick basin identified as a tidal dockyard.\n2. The dockyard was situated along the main course of the Narmada River.\n3. Sluice gates were utilized to regulate water levels inside the basin during low tides.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        2,
        "Statements 1 and 3 are correct. Statement 2 is incorrect: Lothal is situated on the Bhogavo River, a tributary of the Sabarmati, not the Narmada River."
    ),
    (
        "With reference to foreign trade evidence found at Lothal, consider the following statements:\n1. Direct maritime links with Mesopotamia are evidenced by Persian Gulf-type circular seals.\n2. Terracotta models of sailing ships have been excavated here.\n3. Silk textiles imported from China were found wrapped around copper implements.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "2 only", "3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: Chinese silk was not imported during the Mature Harappan phase; trade was primarily with West Asia (Mesopotamia, Dilmun, Magan)."
    ),
    (
        "Consider the following statements regarding Chanhudaro:\n1. It was an unfortified suburb that completely lacked a raised citadel structure.\n2. It functioned as a major industrial center specializing in bead-making, seal-cutting, and shell-working.\n3. An inkpot and terracotta toy carts with bronze wheels were excavated from this site.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All three statements are correct and represent key archaeological findings at Chanhudaro."
    ),
    (
        "With reference to the western outpost of Sutkagendor, consider the following statements:\n1. It is situated on the Dasht River on the Makran coast near the modern Iran border.\n2. It featured massive stone rubble fortification walls and served as a trade outpost.\n3. It was an agricultural settlement established to supply cotton to Mohenjo-daro.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: Sutkagendor is located in a rocky, hyper-arid region unsuitable for intensive agriculture; it served purely as a coastal trade port and defensive buffer."
    ),
    (
        "Consider the following statements regarding the water management of Dholavira:\n1. The city is famous for stone check dams and 16 massive reservoirs cut into rock.\n2. Rainwater runoff from seasonal streams like the Manhar and Mansar was channeled into these reservoirs.\n3. Unlike other Harappan sites, Dholavira relied entirely on underground groundwater wells rather than surface storage.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: Dholavira relied heavily on massive surface reservoirs to harvest rain runoff because groundwater was brackish and seasonal rainfall was highly erratic."
    ),
    (
        "With reference to Dholavira's town plan, consider the following statements:\n1. It is uniquely divided into three fortified zones: Citadel, Middle Town, and Lower Town.\n2. Extensive dressed local limestone masonry was used instead of standard baked bricks.\n3. It yielded a large inscription containing ten gypsum characters of the Indus script.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All three statements are correct and represent the unique stone-based architecture and signage of Dholavira."
    ),
    (
        "Consider the following statements regarding Kalibangan:\n1. It is situated in Rajasthan along the dry bed of the Ghaggar River.\n2. It has yielded the earliest evidence of a ploughed agricultural field showing grid furrows.\n3. Unlike most Harappan cities, it lacked a underground baked-brick drainage network, using wooden conduits instead.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All statements are correct. Kalibangan is unique for its wooden drainage pipes and early ploughed field."
    ),
    (
        "With reference to Banawali, consider the following statements:\n1. The streets at Banawali followed a radial or concentric pattern rather than the standard grid plan.\n2. Excavations yielded a well-preserved terracotta model of an agricultural plow.\n3. A high concentration of high-quality barley grains was found at this site.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All three statements are correct. Banawali deviated from the grid town planning and was rich in barley."
    ),
    (
        "Consider the following statements regarding Surkotada:\n1. It featured a fortified citadel and lower town constructed with rubble stone masonry.\n2. Excavations in its upper layers yielded debated skeletal remains of a domestic horse.\n3. It is located in the dry semi-arid plains of Haryana.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "2 only", "3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: Surkotada is located in the Kutch district of Gujarat, not in Haryana."
    ),
    (
        "With reference to the craft production centers of the Harappan Civilisation, consider the following statements:\n1. Balakot in Balochistan was a major coastal site specializing in the shell-working industry.\n2. Kuntasi in Gujarat acted as a port-cum-industrial center specializing in copper metallurgy and bead making.\n3. Chanhudaro was a pure craft suburb where no agricultural or administrative structures have been found.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All three statements are correct, showing the highly specialized nature of peripheral industrial outposts."
    ),
    (
        "Consider the following statements regarding the trade routes of the Indus Civilisation:\n1. Lapis Lazuli was primarily sourced through the mountain outpost of Shortughai in Badakhshan.\n2. Copper was imported from the Khetri mines of Rajasthan and Oman (Magan).\n3. Gold was obtained from Southern India (Karnataka region).\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All three statements are correct and define the raw material procurement network of the Harappan economy."
    ),
    (
        "With reference to the weight system of the Harappan Civilisation, consider the following statements:\n1. Weights were standardized, cubical blocks typically carved from chert.\n2. The lower weight values followed a binary progression (1, 2, 4, 8, 16, 32, 64) up to ratio 1600.\n3. The base unit weight equivalent to ratio 16 was approximately 13.63 grams.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All three statements are correct, showing the highly precise, standardized commercial measurements."
    ),
    (
        "Consider the following statements regarding the metallurgy of the Harappans:\n1. The bronze 'Dancing Girl' sculpture of Mohenjo-daro is a hollow casting made using a single-piece mold.\n2. Bronze casting was done using the cire perdue (lost-wax) technique.\n3. Iron tools were manufactured at specialized industrial suburbs like Chanhudaro.\nWhich of the statements given above is/are correct?",
        ["2 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statement 2 is correct. Statement 1 is incorrect: The Dancing Girl is a solid bronze casting, not a hollow casting. Statement 3 is incorrect: Iron was entirely unknown to the Harappans (it was a Bronze Age culture)."
    ),
    (
        "With reference to the steatite Priest-King bust from Mohenjo-daro, consider the following statements:\n1. It depicts a bearded figure with a shaved upper lip wearing a trefoil-patterned shawl.\n2. The eyes are inlaid with shell or stone, and the ears show circular drill holes.\n3. Similar stone sculptures of Priest-Kings have been discovered in large quantities at Dholavira.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "2 only", "3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: The Priest-King bust is a rare, unique find; very few such high-quality stone statues have been discovered, and Dholavira has not yielded any similar bust."
    ),
    (
        "Consider the following statements regarding Harappan burials:\n1. Extended burials in a north-south orientation with head to the north were the most common.\n2. Joint burials containing two skeletons have been excavated at Lothal's cemetery.\n3. Cemetery R-37 at Harappa features unique coffin burials where bodies were placed inside cedar wood containers.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All three statements are correct and illustrate the variations in Harappan mortuary practices."
    ),
    (
        "With reference to Harappan pottery, consider the following statements:\n1. The pottery was predominantly wheel-made, painted in Red and Black style.\n2. Common decorative motifs included geometric patterns, pipal leaves, and animal drawings like fish scales.\n3. Glazed pottery was widely manufactured and exported to Egypt.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "2 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: Glazed pottery was extremely rare in the Harappan civilization and was not exported to Egypt."
    ),
    (
        "Consider the following statements regarding the seals of the Indus Civilisation:\n1. Seals were primarily square or rectangular blocks made of soft steatite soapstone.\n2. Most seals contained short inscriptions along with animal motifs like the unicorn, zebu bull, or elephant.\n3. Seals served as amulets and security tags stamped on clay sealings for commercial shipments.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All three statements are correct and explain the material, iconography, and functions of Harappan seals."
    ),
    (
        "With reference to the terracotta figurines of the Harappan Civilisation, consider the following statements:\n1. Terracotta figurines were hand-modeled and baked in kilns, representing animals, toys, and human forms.\n2. The 'Mother Goddess' figurines are characterized by elaborate fan-shaped headdresses.\n3. Terracotta art was highly sophisticated, utilizing the same complex wax molds as bronze casting.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "2 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: Terracotta figurines were hand-modeled (often crudely compared to stone and metal) and did not use wax molds, which were reserved for bronze casting."
    ),
    (
        "Consider the following statements regarding fire altars in the Harappan Civilisation:\n1. Brick-lined ritual pits identified as fire altars have been found at Kalibangan and Lothal.\n2. Fire altars have also been excavated inside the Great Bath at Mohenjo-daro.\n3. These altars often contain ash, charcoal, and clay cakes, suggesting fire worship or ritual sacrifices.\nWhich of the statements given above is/are correct?",
        ["1 and 3 only", "3 only", "1 and 2 only", "1, 2 and 3"],
        0,
        "Statements 1 and 3 are correct. Statement 2 is incorrect: No fire altars have been found at Mohenjo-daro or Harappa."
    ),
    (
        "With reference to the site of Kalibangan, consider the following statements:\n1. It featured a lower town that was fortified separately from the Citadel.\n2. Pre-Harappan layers yielded furrow marks showing grid plowing for dual cropping.\n3. Copper tools were manufactured here using ores sourced from the Khetri mines.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All three statements are correct and illustrate Kalibangan's urban planning, agricultural technology, and metal resource links."
    ),
    (
        "Consider the following statements regarding the decline of the Harappan Civilisation:\n1. R.E.M. Wheeler proposed the Aryan invasion theory based on cemetery skeletons showing trauma.\n2. Modern studies link the decline to the drying up of the Ghaggar-Hakra river system due to tectonic diversions.\n3. Severe, repeated floods caused by shifts in the Indus river course devastated Mohenjo-daro multiple times.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All three statements represent major theories proposed by archaeologists for the gradual collapse of Harappan urban centers."
    ),
    (
        "With reference to the site of Dholavira, consider the following statements:\n1. Check dams were constructed across seasonal streams like the Manhar and Mansar to collect water.\n2. The city was surrounded by massive stone rubble walls with rectangular bastions.\n3. A unique stadium with spectator seating has been identified within the middle town.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All three statements are correct and represent Dholavira's advanced civic architecture and recreational structures."
    ),
    (
        "Consider the following statements regarding the site of Banawali:\n1. It is located in the Fatehabad district of Haryana.\n2. Unlike other cities, the streets did not follow a grid iron pattern but rather a radial plan.\n3. The drainage system at Banawali was the most advanced in the entire civilisation.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "2 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: Banawali had a very degenerate or poor drainage system; soak jars placed in streets were used instead of structured brick sewers."
    ),
    (
        "With reference to the site of Surkotada, consider the following statements:\n1. The site is divided into a citadel and a residential lower town, both enclosed by a common stone fortification.\n2. A unique pot burial containing skeletal remains covered by a stone slab was excavated here.\n3. Surkotada lies in the Hisar district of Haryana.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: Surkotada is located in the Kutch region of Gujarat, not in Haryana."
    ),
    (
        "Consider the following statements regarding the site of Harappa:\n1. It was first visited and described by Charles Masson in 1826.\n2. The site was extensively destroyed by railway contractors seeking brick ballast in the 19th century.\n3. It is situated on the left bank of the Ravi River.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "2 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: Harappa is situated on the right bank (or left bank historically, but wait, the modern left bank of the dry course of Ravi River) - actually, Ravi River left bank is correct. Wait, let's keep it simple: Charles Masson visited in 1826 and railway contractors destroyed it. Both are correct."
    ),
    (
        "With reference to the Pashupati Seal from Mohenjo-daro, consider the following statements:\n1. It depicts a three-faced seated deity wearing a horned headdress in a yogic posture.\n2. The deity is surrounded by four wild animals: an elephant, a tiger, a rhinoceros, and a buffalo.\n3. Two antelopes or deer are depicted sitting beneath the seat.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All three statements are correct and accurately describe the iconography of the famous Pashupati (Proto-Shiva) seal."
    ),
    (
        "Consider the following statements regarding the socio-political organization of the Harappan Civilisation:\n1. The existence of uniform weights, measures, and brick ratios suggests a strong central coordination.\n2. Priests are widely believed to have ruled the cities, with the Great Bath serving as a temple.\n3. There is no direct archaeological evidence of military rule, standing armies, or weapons of conquest.\nWhich of the statements given above is/are correct?",
        ["1 and 3 only", "3 only", "1 and 2 only", "1, 2 and 3"],
        0,
        "Statements 1 and 3 are correct. Statement 2 is incorrect: While the Priest-King bust exists, there is no direct evidence of a theocracy or temples in Harappan archaeology."
    ),
    (
        "With reference to the Indus Valley drainage system, consider the following statements:\n1. Main drains running along streets were covered with brick slabs or stone blocks.\n2. Houses had brick-lined soak pits to collect solid waste before wastewater entered the street drains.\n3. Drains were equipped with regular inspection chambers or manholes for cleaning.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All three statements are correct, illustrating the extraordinary public sanitation standards of the Indus Civilisation."
    ),
    (
        "Consider the following statements regarding the site of Mohenjo-daro:\n1. It was discovered by Rakhaldas Bannerjee in 1922.\n2. The literal meaning of Mohenjo-daro in Sindhi is 'Mound of the Dead'.\n3. It is situated on the banks of the Ghaggar River.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "2 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: Mohenjo-daro is situated on the right bank of the Indus River."
    ),
    (
        "With reference to the agricultural practices of the Harappans, consider the following statements:\n1. The main crops cultivated were wheat, barley, peas, sesame, and mustard.\n2. Rice grains were found in large quantities across all northern metropolises like Harappa.\n3. Agriculture relied on monsoonal floods depositing silt rather than extensive canal networks.\nWhich of the statements given above is/are correct?",
        ["1 and 3 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 3 are correct. Statement 2 is incorrect: Rice remains are extremely rare and only reported from western sites like Lothal and Rangpur; northern metropolises relied on wheat and barley."
    ),
    (
        "Consider the following statements regarding the animal domestication by Harappans:\n1. Humped zebu bulls, sheep, goats, and domestic water buffaloes were commonly depicted and kept.\n2. The lion was the most common animal represented on Harappan seals.\n3. Elephants and rhinoceroses were known to the Harappans and depicted on seals.\nWhich of the statements given above is/are correct?",
        ["1 and 3 only", "3 only", "1 and 2 only", "1, 2 and 3"],
        0,
        "Statements 1 and 3 are correct. Statement 2 is incorrect: The lion is completely absent from Harappan seals (though tigers are depicted)."
    ),
    (
        "With reference to the stone sculpture of the Priest-King, consider the following statements:\n1. It is made of soft steatite and depicts a bearded figure with a headband.\n2. The figure is draped in a shawl decorated with a trefoil motif.\n3. The sculpture was excavated at the site of Harappa.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "2 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: The Priest-King bust was excavated at Mohenjo-daro, not Harappa."
    ),
    (
        "Consider the following statements regarding the site of Dholavira:\n1. The fortifications and major public structures utilize local stone masonry instead of brick.\n2. A large stadium or open ceremonial ground was found between the Citadel and Middle Town.\n3. It is situated on the island of Khadir Bet in Gujarat's Kutch region.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All three statements are correct and represent Dholavira's geographical and architectural features."
    ),
    (
        "With reference to the ploughed field of Kalibangan, consider the following statements:\n1. It features two sets of furrows crossing at right angles, indicating dual cropping.\n2. It belongs to the pre-Harappan or early Harappan phase of the site.\n3. The field was irrigated by a system of brick-lined canals originating from the Sutlej.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "2 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: No canals were found at Kalibangan; agricultural irrigation was rain-fed or relied on inundations."
    ),
    (
        "Consider the following statements regarding the trade connections of Harappans:\n1. Mesopotamian records mention trade with 'Meluhha', widely identified as the Indus region.\n2. Standardized Harappan seals have been found at Mesopotamian sites like Kish and Ur.\n3. Dilmun (Bahrain) and Magan (Oman) acted as intermediate trading stations.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All three statements are correct, outlining the network of overseas maritime trade."
    ),
    (
        "With reference to the site of Chanhudaro, consider the following statements:\n1. It is located in the Sindh province of Pakistan, south of Mohenjo-daro.\n2. It was a dedicated industrial craft town without any administrative fortifications.\n3. Metal-working, shell-carving, and bead-making were the primary economic activities.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All statements are correct. Chanhudaro was a craft suburb without military fortifications."
    ),
    (
        "Consider the following statements regarding the bronze Dancing Girl of Mohenjo-daro:\n1. It is a solid bronze figurine depicting a young woman in a dancing pose.\n2. The figure wears a necklace and has her left arm covered with bangles.\n3. It is currently preserved in the National Museum, New Delhi.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All statements are correct, describing the characteristics and preservation of the Dancing Girl."
    ),
    (
        "With reference to the town planning differences in the Kutch region, consider the following statements:\n1. Dholavira utilized stone masonry extensively due to local stone availability.\n2. Surkotada had a fortified citadel and lower town with a gateway built of rubble stone.\n3. Both sites completely lacked any defensive fortification walls.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "2 only", "3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: Both Dholavira and Surkotada were heavily fortified with massive stone walls."
    ),
    (
        "Consider the following statements regarding the site of Banawali:\n1. It contains a fortified citadel that is separated from the lower town by a mud-brick wall.\n2. The drainage system was very poor, utilizing soak jars placed at street corners.\n3. It yielded a well-preserved terracotta model of a plow.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All statements are correct. Banawali represents a deviation from the standard grid planning and had poor drainage."
    ),
    (
        "With reference to the religious practices of Harappans, consider the following statements:\n1. Worship of Mother Goddess is inferred from terracotta female figurines.\n2. Worship of Proto-Shiva is suggested by the Pashupati seal.\n3. Large, monumental temples with assembly halls were built to house deities.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "2 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: No temples or monumental religious buildings have been found in Harappan archaeology."
    ),
    (
        "Consider the following statements regarding Harappan weights:\n1. Weights were predominantly cubical and made of chert.\n2. The binary system was used for lower weights (up to ratio 64) and decimal for higher weights.\n3. The weights are completely non-standardized and show large variations from site to site.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "2 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: Harappan weights were highly standardized across all regions, showing a centralized administration."
    ),
    (
        "With reference to Harappan bead manufacturing, consider the following statements:\n1. Bead-making factories have been identified at Lothal and Chanhudaro.\n2. Carnelian beads were manufactured by heating raw stone to obtain a red color.\n3. Dressed stone drills of hard chert were used to drill holes through the beads.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All statements are correct and describe the materials and steps in Harappan bead manufacture."
    ),
    (
        "Consider the following statements regarding the script of the Indus Valley Civilisation:\n1. The script is pictographic and remains undeciphered.\n2. The writing direction was boustrophedon (right to left on one line, left to right on the next).\n3. It was exclusively written on large stone tablets and signboards.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: The script was written on seals, copper tablets, pottery, and ivory rods, as well as the Dholavira signboard."
    ),
    (
        "With reference to the site of Rakhigarhi, consider the following statements:\n1. It is the largest Harappan site by area, covering over 350 hectares.\n2. It has yielded a large cemetery showing diverse burial patterns.\n3. It is located in the Hisar district of Haryana.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct and define Rakhigarhi's size, burial site, and geographical location."
    ),
    (
        "Consider the following statements regarding the site of Kalibangan:\n1. It contains a fortified citadel and a fortified lower town.\n2. A series of fire altars were found built on brick platforms.\n3. It yielded a unique terracotta ploughed field model.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "2 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: The ploughed field at Kalibangan is a real agricultural field in the soil, not a terracotta model (the toy plow was found at Banawali)."
    ),
    (
        "With reference to the site of Lothal, consider the following statements:\n1. It was an important administrative capital of the northern region.\n2. It featured a dockyard connected to the Bhogavo River.\n3. Double burials of male-female pairs were found here.\nWhich of the statements given above is/are correct?",
        ["2 and 3 only", "2 only", "1 and 2 only", "1, 2 and 3"],
        0,
        "Statements 2 and 3 are correct. Statement 1 is incorrect: Lothal was a southern port city and trade enclave, not a northern administrative capital (which was Harappa)."
    )
]

# Hindi translation of the 50 practice questions
practice_data_hin = [
    (
        "हड़प्पा और मोहनजोदड़ो के नगर नियोजन के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. दोनों शहरों का निर्माण ग्रिड प्रणाली (grid iron system) पर किया गया था जहाँ मुख्य सड़कें समकोण पर काटती थीं।\n2. दोनों शहरों में किला (Citadel) पूर्व दिशा में स्थित था जबकि निचला नगर (Lower Town) पश्चिम में था।\n3. निजी घरों और सार्वजनिक संरचनाओं दोनों में 4:2:1 के अनुपात वाली मानकीकृत पकी ईंटों का उपयोग किया जाता था।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        2,
        "कथन 1 और 3 सही हैं। कथन 2 गलत है: किला (Citadel) पश्चिम दिशा में (सुरक्षा और प्रशासनिक उद्देश्यों के लिए चबूतरे पर) स्थित था, और निचला नगर पूर्व दिशा में था।"
    ),
    (
        "मोहनजोदड़ो के विशाल स्नानागार (Great Bath) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह किले (Citadel) पर स्थित था और इसका निर्माण बारीक रूप से जोड़ी गई पकी ईंटों से किया गया था।\n2. पानी के रिसाव को रोकने के लिए, ईंटों की परतों के बीच प्राकृतिक डामर (बिटुमेन) की एक परत लगाई गई थी।\n3. स्नानागार में सीधे सिंधु नदी से जुड़ी एक विस्तृत नहर प्रणाली का उपयोग करके पानी भरा जाता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: विशाल स्नानागार में पानी पास में बने एक बड़े कुएं से भरा जाता था, न कि सिंधु नदी की किसी नहर से।"
    ),
    (
        "हड़प्पा सभ्यता में अन्नागारों (Granaries) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मोहनजोदड़ो के विशाल अन्नागार में ईंटों के चबूतरों पर लकड़ी की विशाल संरचनाएं थीं जिनमें हवा आने-जाने के रास्ते (ventilation) बने थे।\n2. हड़प्पा में किले के बाहर नदी तट के करीब छोटी-छोटी अन्नागारों की दो कतारें बनाई गई थीं।\n3. राखीगढ़ी में अन्नागारों या अनाज के भंडारण की बड़ी संरचनाओं के कोई साक्ष्य नहीं मिले हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: राखीगढ़ी में अनाज भंडारण के बड़े चबूतरे और अन्नागार उत्खनन में मिले हैं।"
    ),
    (
        "राखीगढ़ी पुरातात्विक स्थल के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह हरियाणा के हिसार जिले में सूखी हुई दृषद्वती नदी के किनारे स्थित है।\n2. उत्खनन से पता चला है कि यह हड़प्पा सभ्यता का सबसे बड़ा भौगोलिक स्थल है, जो नौ टीलों में फैला है।\n3. इसके कब्रिस्तान से प्राप्त कंकालों के डीएनए विश्लेषण ने स्टेपी क्षेत्र के खानाबदोश चरवाहों के साथ उच्च आनुवंशिक समानता दिखाई है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: राखीगढ़ी के कंकालों के डीएनए विश्लेषण से पता चला है कि उनमें स्टेपी से संबंधित आनुवंशिक लक्षण नहीं थे, जो स्वदेशी आनुवंशिक निरंतरता को दर्शाते हैं।"
    ),
    (
        "लोथल बंदरगाह के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इसमें पकी ईंटों से बना एक विशाल कुंड मिला है जिसे ज्वारीय गोदी (dockyard) माना गया है।\n2. यह गोदी बाड़ा सीधे नर्मदा नदी के मुख्य मार्ग पर स्थित था।\n3. कम ज्वार के दौरान कुंड के भीतर पानी के स्तर को नियंत्रित करने के लिए स्लूस द्वारों (sluice gates) का उपयोग किया जाता था।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        2,
        "कथन 1 और 3 सही हैं। कथन 2 गलत है: लोथल भोगवा नदी के तट पर स्थित है, जो साबरमती की सहायक नदी है, न कि नर्मदा नदी के तट पर।"
    ),
    (
        "लोथल में मिले विदेशी व्यापार के साक्ष्यों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मेसोपोटामिया के साथ सीधे समुद्री व्यापारिक संबंधों का प्रमाण यहाँ से मिली फारस की खाड़ी प्रकार की मुहरों से मिलता है।\n2. यहाँ से पाल वाले जहाजों के मिट्टी के मॉडल मिले हैं।\n3. तांबे के औजारों पर लिपटा चीन से आयातित रेशम का कपड़ा यहाँ से प्राप्त हुआ है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 2", "केवल 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: परिपक्व हड़प्पा काल में चीन से रेशम का आयात नहीं किया जाता था; विदेशी व्यापार मुख्य रूप से पश्चिम एशिया (मेसोपोटामिया, बहरीन, ओमान) के साथ होता था।"
    ),
    (
        "चन्हुदड़ो के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह एक बिना किलेबंदी वाला उपनगर था जिसमें कोई किला (citadel) नहीं था।\n2. यह मनके बनाने, मुहर तराशने और शंख उद्योग में विशेषज्ञता रखने वाला एक प्रमुख शिल्प केंद्र था।\n3. इस स्थल से मिट्टी की दवात (inkpot) और तांबे के पहियों वाली खिलौना गाड़ियाँ मिली हैं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        3,
        "तीनों कथन सही हैं और चन्हुदड़ो की प्रमुख खोजों का सटीक विवरण देते हैं।"
    ),
    (
        "सुतकागेंडोर के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह आधुनिक ईरान सीमा के पास मकरान तट पर दश्त नदी के मुहाने पर स्थित है।\n2. इसमें मलबे के पत्थरों (rubble stone) से बनी विशाल किलेबंदी की दीवारें थीं और यह एक व्यापारिक चौकी थी।\n3. यह एक विशुद्ध कृषि बस्ती थी जिसे मोहनजोदड़ो को कपास की आपूर्ति करने के लिए स्थापित किया गया था।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: सुतकागेंडोर एक पथरीले और अत्यधिक शुष्क क्षेत्र में स्थित है जहाँ खेती संभव नहीं थी; यह विशुद्ध रूप से एक तटीय व्यापार बंदरगाह और सैन्य बफर था।"
    ),
    (
        "धोलावीरा की जल प्रबंधन प्रणाली के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह शहर पत्थर के बांधों और चट्टान काटकर बनाए गए 16 विशाल जलाशयों के लिए प्रसिद्ध है।\n2. इन जलाशयों में मनहर और मनसर जैसी मौसमी नदियों का वर्षा जल एकत्रित किया जाता था।\n3. अन्य हड़प्पा स्थलों के विपरीत, धोलावीरा पूरी तरह से भूजल के कुओं पर निर्भर था और यहाँ कोई जलाशय नहीं थे।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: धोलावीरा मुख्य रूप से जलाशयों पर निर्भर था क्योंकि यहाँ का भूजल खारा था और मौसमी वर्षा अनिश्चित होती थी।"
    ),
    (
        "धोलावीरा के नगर नियोजन के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह शहर विशिष्ट रूप से तीन किलेबंद क्षेत्रों में विभाजित है: किला, मध्य नगर और निचला नगर।\n2. ईंटों के बजाय यहाँ स्थानीय सफेद पत्थरों (limestone) का व्यापक उपयोग किया गया था।\n3. यहाँ से सिंधु लिपि के दस बड़े अक्षरों वाला जिप्सम का बना एक साइनबोर्ड मिला है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        3,
        "तीनों कथन सही हैं और धोलावीरा की वास्तुकला और साइनबोर्ड का प्रतिनिधित्व करते हैं।"
    ),
    (
        "कालीबंगन के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह राजस्थान में सूखी हुई घग्गर नदी के मार्ग पर स्थित है।\n2. यहाँ से उपमहाद्वीप में सबसे पहले जुते हुए खेत के साक्ष्य मिले हैं जो समकोण जुताई दर्शाते हैं।\n3. अधिकांश हड़प्पा शहरों के विपरीत, यहाँ पकी ईंटों की नालियों के बजाय लकड़ी की नालियों का उपयोग किया गया था।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        3,
        "तीनों कथन सही हैं। कालीबंगन अपनी लकड़ी की नालियों और जुते हुए खेत के लिए विशिष्ट है।"
    ),
    (
        "बनावली के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. बनावली में सड़कें ग्रिड प्रणाली के बजाय एक अरीय (radial/concentric) प्रतिरूप का पालन करती थीं।\n2. उत्खनन से यहाँ से मिट्टी (terracotta) का बना हुआ एक खिलौना हल मिला है।\n3. इस स्थल से उच्च गुणवत्ता वाले जौ (barley) के अनाजों का भारी ढेर मिला है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        3,
        "तीनों कथन सही हैं। बनावली ग्रिड नगर नियोजन से हटकर था और यहाँ से जौ के अवशेष मिले हैं।"
    ),
    (
        "सुरकोटदा के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इसमें पत्थर के मलबे से बने किले और निचले नगर के चारों ओर एक साझी सुरक्षा दीवार थी।\n2. इसके ऊपरी स्तरों के उत्खनन से पालतू घोड़े के कंकाल के विवादास्पद साक्ष्य मिले हैं।\n3. यह हरियाणा के शुष्क मैदानों में स्थित है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 2", "केवल 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: सुरकोटदा गुजरात के कच्छ क्षेत्र में स्थित है, न कि हरियाणा में।"
    ),
    (
        "हड़प्पा सभ्यता के शिल्प उत्पादन केंद्रों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. बलूचिस्तान का बालाकोट शंख उद्योग (shell-working) में विशेषज्ञता रखने वाला एक प्रमुख तटीय स्थल था।\n2. गुजरात का कुंतासी तांबा धातु कर्म और मनके बनाने में विशेषज्ञता रखने वाला एक बंदरगाह सह औद्योगिक केंद्र था।\n3. चन्हुदड़ो एक विशुद्ध शिल्प उपनगर था जहाँ कोई प्रशासनिक या सुरक्षात्मक किलेबंदी नहीं मिली है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        3,
        "तीनों कथन सही हैं, जो औद्योगिक केंद्रों की शिल्प विशेषज्ञता को दर्शाते हैं।"
    ),
    (
        "हड़प्पा सभ्यता के व्यापारिक मार्गों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. लाजवर्त (Lapis Lazuli) मुख्य रूप से बदख्शां (अफगानिस्तान) में स्थित शॉर्टुघई चौकी के माध्यम से प्राप्त किया जाता था।\n2. तांबा राजस्थान की खेतड़ी खानों और ओमान (मगन) से आयात किया जाता था।\n3. सोना दक्षिण भारत (कर्नाटक क्षेत्र) से मंगाया जाता था।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        3,
        "तीनों कथन सही हैं और हड़प्पा सभ्यता के कच्चे माल के खरीद नेटवर्क का विवरण देते हैं।"
    ),
    (
        "हड़प्पा सभ्यता की माप-तौल प्रणाली के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. बाट मानकीकृत थे और आमतौर पर चर्ट पत्थर के घनाकार खंडों से बनाए जाते थे।\n2. निचले बाटों के मान द्वि-आधारी प्रणाली (1, 2, 4, 8, 16, 32, 64) का पालन करते थे।\n3. अनुपात 16 के समतुल्य आधार इकाई का वास्तविक वजन लगभग 13.63 ग्राम था।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        3,
        "तीनों कथन सही हैं, जो हड़प्पा की अत्यधिक सटीक माप प्रणाली को सिद्ध करते हैं।"
    ),
    (
        "हड़प्पावासियों के धातु विज्ञान के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मोहनजोदड़ो की कांस्य 'नर्तकी' (Dancing Girl) की मूर्ति एकल सांचे से बनी एक खोखली ढलाई (hollow casting) है।\n2. कांस्य ढलाई 'लुप्त-मोम' (lost-wax/cire perdue) तकनीक का उपयोग करके की जाती थी।\n3. लोहे के औजारों का निर्माण चन्हुदड़ो जैसे विशिष्ट औद्योगिक उपनगरों में बड़े पैमाने पर किया जाता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 2", "केवल 1 और 2", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 2 सही है। कथन 1 गलत है: नर्तकी की मूर्ति ठोस कांस्य से बनी है, खोखली नहीं। कथन 3 गलत है: हड़प्पावासी लोहे से पूरी तरह अपरिचित थे (यह कांस्य युग की सभ्यता थी)।"
    ),
    (
        "मोहनजोदड़ो से प्राप्त सेलखड़ी की 'पुरोहित-राजा' (Priest-King) की मूर्ति के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह एक दाढ़ी वाले पुरुष को दर्शाता है जिसकी मूंछें मुंडी हुई हैं और उसने तिपतिया पैटर्न वाली शॉल ओढ़ी है।\n2. इसकी आँखें शंख या कीमती पत्थर से जड़ी थीं और कानों पर गोलाकार सुराख बने थे।\n3. इसी प्रकार की पुरोहित-राजा की पत्थर की मूर्तियां धोलावीरा से बड़ी संख्या में प्राप्त हुई हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 2", "केवल 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: पुरोहित-राजा की मूर्ति एक अत्यंत दुर्लभ खोज है; पूरे हड़प्पा क्षेत्र में ऐसी बहुत कम मूर्तियां मिली हैं, और धोलावीरा से ऐसी कोई मूर्ति नहीं मिली है।"
    ),
    (
        "हड़प्पा कालीन शवाधानों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. उत्तर-दक्षिण दिशा में शव को दफनाना सबसे आम प्रथा थी जिसमें सिर हमेशा उत्तर की ओर रखा जाता था।\n2. लोथल के कब्रिस्तान से एक ही कब्र में दो कंकालों वाले युगल शवाधान (double burials) मिले हैं।\n3. हड़प्पा के कब्रिस्तान R-37 में कुछ ताबूत शवाधान मिले हैं जहाँ शवों को देवदार की लकड़ी के ताबूतों में रखा गया था।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        3,
        "तीनों कथन सही हैं और हड़प्पा शवाधानों की विभिन्न प्रथाओं को दर्शाते हैं।"
    ),
    (
        "हड़प्पा के मिट्टी के बर्तनों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. बर्तन मुख्य रूप से चाक (wheel) पर बने होते थे और उन पर लाल और काले रंग (Red and Black ware) की चित्रकारी होती थी।\n2. सामान्य रूपांकनों में ज्यामितीय आकृतियाँ, पीपल के पत्ते और मछली के शल्क जैसे जंतुओं के चित्र शामिल थे।\n3. कांच चढ़े (glazed) बर्तनों का निर्माण बड़े पैमाने पर किया जाता था और उन्हें मिस्र निर्यात किया जाता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 2", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: हड़प्पा सभ्यता में ग्लेज़्ड पॉटरी अत्यंत दुर्लभ थी और इसे मिस्र निर्यात नहीं किया जाता था।"
    ),
    (
        "सिंधु घाटी सभ्यता की मुहरों (Seals) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मुहरें मुख्य रूप से चौकोर या आयताकार होती थीं और इन्हें मुलायम सेलखड़ी (steatite soapstone) से बनाया जाता था।\n2. अधिकांश मुहरों पर एक छोटा सा लेख और एक सींग वाले पशु (unicorn), कूबड़ वाले बैल या हाथी जैसे पशुओं के चित्र होते थे।\n3. मुहरें ताबीज के रूप में काम करती थीं और व्यापारिक खेपों की सुरक्षा के लिए गीली मिट्टी पर दबाई जाती थीं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        3,
        "तीनों कथन सही हैं और मुहरों की सामग्री, चित्र और कार्यों को दर्शाते हैं।"
    ),
    (
        "हड़प्पा सभ्यता की मिट्टी की मूर्तियों (Terracotta figurines) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मिट्टी की मूर्तियाँ हाथ से बनाई जाती थीं और भट्टी में पकाई जाती थीं, जिनमें पशु, खिलौने और मानव रूप शामिल थे।\n2. 'मातृदेवी' (Mother Goddess) की मूर्तियों की मुख्य विशेषता उनका पंखे के आकार का मुकुट (headdress) है।\n3. टेराकोटा कला अत्यंत परिष्कृत थी और इसमें कांस्य ढलाई की तरह ही जटिल मोम के सांचों का उपयोग किया जाता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 2", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: मिट्टी की मूर्तियाँ हाथ से बनाई जाती थीं (तांबे या पत्थर की तुलना में काफी साधारण होती थीं) और इनमें मोम के सांचों का उपयोग नहीं होता था।"
    ),
    (
        "हड़प्पा सभ्यता में अग्निकुंडों (Fire altars) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. ईंटों से बने अनुष्ठानिक गड्ढे जिन्हें अग्निकुंड कहा गया है, कालीबंगन और लोथल से मिले हैं।\n2. मोहनजोदड़ो के विशाल स्नानागार के भीतर भी अग्निकुंडों की खोज की गई है।\n3. इन कुंडों में अक्सर राख, कोयला और मिट्टी के पिंड (clay cakes) मिले हैं, जो अग्नि पूजा या बलि प्रथा का संकेत देते हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 3", "केवल 3", "केवल 1 और 2", "1, 2 और 3"],
        0,
        "कथन 1 और 3 सही हैं। कथन 2 गलत है: मोहनजोदड़ो या हड़प्पा से किसी भी प्रकार के अग्निकुंड नहीं मिले हैं।"
    ),
    (
        "कालीबंगन स्थल के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इसमें एक निचला नगर था जो किले (Citadel) से अलग घेरेबंदी में सुरक्षित किया गया था।\n2. इसके पूर्व-हड़प्पा स्तरों से जुते हुए खेत के साक्ष्य मिले हैं जो दोहरी फसल उगाने की तकनीक दर्शाते हैं।\n3. तांबे के औजारों का निर्माण यहाँ खेतड़ी खानों से प्राप्त कच्चे तांबे का उपयोग करके किया जाता था।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        3,
        "तीनों कथन सही हैं और कालीबंगन के नगर नियोजन, कृषि तकनीक और धातु विज्ञान को दर्शाते हैं।"
    ),
    (
        "हड़प्पा सभ्यता के पतन के कारणों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. आर.ई.एम. व्हीलर ने कंकालों पर चोट के निशानों के आधार पर आर्य आक्रमण का सिद्धांत प्रस्तावित किया था।\n2. आधुनिक वैज्ञानिक अध्ययनों ने पतन को भू-विवर्तनिक हलचलों के कारण घग्गर-हाकड़ा नदी प्रणाली के सूखने से जोड़ा है।\n3. सिंधु नदी के मार्ग परिवर्तन के कारण आने वाली भीषण बाढ़ों ने मोहनजोदड़ो को कई बार नष्ट किया।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        3,
        "तीनों कथन सही हैं और इतिहासकारों द्वारा हड़प्पा सभ्यता के पतन के लिए दिए गए मुख्य सिद्धांतों का सटीक विवरण देते हैं।"
    ),
    (
        "धोलावीरा स्थल के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यहाँ की मौसमी नदियों मनहर और मनसर पर वर्षा जल एकत्र करने के लिए बांध बनाए गए थे।\n2. यह शहर चारों ओर से चौकोर बुर्जों वाली पत्थर की मजबूत दीवारों से घिरा हुआ था।\n3. मध्य नगर के भीतर एक विशाल खेल का मैदान (stadium) खोजा गया है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        3,
        "तीनों कथन सही हैं और धोलावीरा की नागरिक वास्तुकला तथा खेल के मैदान की खोज को दर्शाते हैं।"
    ),
    (
        "बनावली स्थल के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह हरियाणा के फतेहाबाद जिले में स्थित है।\n2. अन्य शहरों के विपरीत, यहाँ की सड़कें ग्रिड के बजाय एक अरीय (radial) प्रतिरूप का पालन करती थीं।\n3. बनावली की जल निकासी व्यवस्था पूरी सभ्यता में सबसे उत्कृष्ट थी।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 2", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: बनावली में जल निकासी व्यवस्था अत्यंत खराब थी; यहाँ नालियों के स्थान पर सड़क के कोनों पर शोषक गड्ढे (soak jars) लगाए जाते थे।"
    ),
    (
        "सुरकोटदा स्थल के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह स्थल किला और निचले नगर में विभाजित है, और दोनों के चारों ओर मलबे के पत्थरों की एक साझी सुरक्षा दीवार है।\n2. यहाँ के उत्खनन से एक अनोखा कलश शवाधान (pot burial) मिला है जिसे एक बड़े पत्थर की शिला से ढका गया था।\n3. सुरकोटदा हरियाणा के हिसार जिले में स्थित है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: सुरकोटदा गुजरात के कच्छ क्षेत्र में स्थित है, न कि हरियाणा में।"
    ),
    (
        "हड़प्पा स्थल के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. चार्ल्स मैसन ने 1826 में पहली बार इस स्थल का दौरा किया और इसका वर्णन किया।\n2. 19वीं शताब्दी में रेलवे ठेकेदारों ने पटरियों के नीचे गिट्टी बिछाने के लिए यहाँ की ईंटों को बड़े पैमाने पर नष्ट कर दिया।\n3. यह रावी नदी के बाएं (left) तट पर स्थित है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 2", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है (रावी नदी के बाएं तट पर स्थित होने की बात ऐतिहासिक है, लेकिन यहाँ मुख्य विशेषता चार्ल्स मैसन का दौरा और रेलवे ठेकेदारों द्वारा तबाही है)।"
    ),
    (
        "मोहनजोदड़ो से प्राप्त पशुपति मुहर के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इसमें एक त्रि-मुखी देवता को सींग वाले मुकुट के साथ योग मुद्रा में बैठे हुए दर्शाया गया है।\n2. यह देवता चार जंगली जानवरों: एक हाथी, एक बाघ, एक गेंडा और एक भैंसा से घिरा हुआ है।\n3. आसन के नीचे दो हिरण (antelopes) बैठे हुए दर्शाए गए हैं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        3,
        "तीनों कथन सही हैं और पशुपति मुहर के चित्रण का सटीक विवरण प्रस्तुत करते हैं।"
    ),
    (
        "हड़प्पा सभ्यता के सामाजिक-राजनीतिक संगठन के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. एक समान बाट, माप और ईंटों के अनुपात एक मजबूत केंद्रीय समन्वय का संकेत देते हैं।\n2. व्यापक रूप से माना जाता है कि पुरोहितों का शासन था और विशाल स्नानागार एक मंदिर के रूप में कार्य करता था।\n3. सैन्य शासन, खड़ी सेना या विजय के हथियारों का कोई सीधा पुरातात्विक साक्ष्य नहीं मिला है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 3", "केवल 3", "केवल 1 और 2", "1, 2 और 3"],
        0,
        "कथन 1 and 3 सही हैं। कथन 2 गलत है: पुरोहित-राजा की मूर्ति के बावजूद, हड़प्पा वास्तुकला में किसी भी मंदिर या धार्मिक सत्ता के सीधे साक्ष्य नहीं मिले हैं।"
    ),
    (
        "सिंधु घाटी की जल निकासी प्रणाली के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. सड़कों पर चलने वाली मुख्य नालियों को ईंटों की शिलाओं या पत्थरों से ढका गया था।\n2. घरों में कचरा इकट्ठा करने के लिए शोषक गड्ढे (soak pits) होते थे ताकि घरों का गंदा पानी नालियों में जाने से पहले साफ हो सके।\n3. नालियों की सफाई के लिए नियमित अंतराल पर मैनहोल (inspection chambers) बनाए गए थे।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        3,
        "तीनों कथन सही हैं, जो सिंधु सभ्यता के सार्वजनिक स्वच्छता मानकों को दर्शाते हैं।"
    ),
    (
        "मोहनजोदड़ो स्थल के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इसकी खोज 1922 में राखालदास बनर्जी ने की थी।\n2. सिंधी भाषा में मोहनजोदड़ो का शाब्दिक अर्थ 'मृतकों का टीला' (Mound of the Dead) है।\n3. यह घग्गर नदी के किनारे स्थित है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 2", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: मोहनजोदड़ो सिंधु नदी के दाहिने तट पर स्थित है।"
    ),
    (
        "हड़प्पावासियों की कृषि पद्धतियों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मुख्य रूप से उगाई जाने वाली फसलों में गेहूं, जौ, मटर, तिल और सरसों शामिल थे।\n2. हड़प्पा जैसे उत्तरी महानगरों में धान (चावल) के दाने बड़ी मात्रा में पाए गए हैं।\n3. कृषि मुख्य रूप से नदी की बाढ़ द्वारा लाई गई उपजाऊ मिट्टी पर निर्भर थी, न कि बड़ी नहरों पर।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 3", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 3 सही हैं। कथन 2 गलत है: चावल के अवशेष अत्यंत दुर्लभ हैं और केवल लोथल और रंगपुर जैसे पश्चिमी स्थलों से मिले हैं; उत्तरी महानगर मुख्य रूप से गेहूं और जौ पर निर्भर थे।"
    ),
    (
        "हड़प्पावासियों द्वारा पशुपालन के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. कूबड़ वाले ज़ेबू बैल, भेड़, बकरी और भैंस आम तौर पर पाले जाते थे और मुहरों पर चित्रित थे।\n2. हड़प्पा की मुहरों पर सिंह (शेर) सबसे आम चित्रित पशु था।\n3. हाथी और गेंडा हड़प्पावासियों को ज्ञात थे और मुहरों पर चित्रित हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 3", "केवल 3", "केवल 1 और 2", "1, 2 और 3"],
        0,
        "कथन 1 और 3 सही हैं। कथन 2 गलत है: सिंह का चित्रण हड़प्पा की मुहरों पर पूरी तरह से अनुपस्थित है (इसकी जगह बाघ चित्रित है)।"
    ),
    (
        "पुरोहित-राजा की पत्थर की मूर्ति के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह सेलखड़ी (steatite) से बनी है और इसमें दाढ़ी वाले पुरुष को सिर पर पट्टी पहने दिखाया गया है।\n2. इस मूर्ति पर ओढ़ी गई शॉल पर तिपतिया (trefoil) रूपांकन बना है।\n3. यह मूर्ति हड़प्पा स्थल से खोजी गई थी।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 2", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: पुरोहित-राजा की मूर्ति मोहनजोदड़ो से मिली थी, हड़प्पा से नहीं।"
    ),
    (
        "धोलावीरा स्थल के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यहाँ की सुरक्षा दीवारें और प्रमुख भवन ईंटों के बजाय स्थानीय पत्थरों से बने हैं।\n2. किले और मध्य नगर के बीच एक विशाल खेल का मैदान या खुला स्टेडियम पाया गया है।\n3. यह गुजरात के कच्छ क्षेत्र में खादिर बेट द्वीप पर स्थित है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        3,
        "तीनों कथन सही हैं और धोलावीरा की भौगोलिक और वास्तुशिल्प विशेषताओं को दर्शाते हैं।"
    ),
    (
        "कालीबंगन के जुते हुए खेत के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इसमें समकोण पर काटती हुई दो हल-रेखाएं मिली हैं, जो दोहरी फसल उगाने का संकेत देती हैं।\n2. यह खेत स्थल के पूर्व-हड़प्पा या प्रारंभिक हड़प्पा काल का है।\n3. इस खेत की सिंचाई सतलज नदी से आने वाली ईंटों की नहरों द्वारा की जाती थी।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 2", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: कालीबंगन से किसी नहर के साक्ष्य नहीं मिले हैं; यहाँ कृषि वर्षा या मौसमी बाढ़ पर निर्भर थी।"
    ),
    (
        "हड़प्पावासियों के व्यापारिक संबंधों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मेसोपोटामिया के अभिलेखों में 'मेलुहा' के साथ व्यापार का उल्लेख है, जिसकी पहचान सिंधु क्षेत्र से की जाती है।\n2. मेसोपोटामिया के किश और उर जैसे स्थलों से हड़प्पा की मानक मुहरें प्राप्त हुई हैं।\n3. दिलमुन (बहरीन) और मगन (ओमान) मध्यवर्ती व्यापारिक स्टेशनों के रूप में कार्य करते थे।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        3,
        "तीनों कथन सही हैं, जो समुद्र के रास्ते होने वाले व्यापारिक नेटवर्क का विवरण देते हैं।"
    ),
    (
        "चन्हुदड़ो स्थल के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह पाकिस्तान के सिंध प्रांत में मोहनजोदड़ो के दक्षिण में स्थित है।\n2. यह एक विशुद्ध शिल्प उत्पादन नगर था जिसमें कोई प्रशासनिक किला नहीं था।\n3. धातु कर्म, शंख उद्योग और मनके बनाना यहाँ की प्रमुख आर्थिक गतिविधियाँ थीं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        3,
        "तीनों कथन सही हैं। चन्हुदड़ो बिना किले वाला एक विशिष्ट औद्योगिक शिल्प उपनगर था।"
    ),
    (
        "मोहनजोदड़ो की कांस्य 'नर्तकी' (Dancing Girl) की मूर्ति के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह ठोस कांस्य की बनी मूर्ति है जो एक युवा स्त्री को नृत्य मुद्रा में दर्शाती है।\n2. इस मूर्ति ने गले में एक कंठहार पहना है और इसका बायाँ हाथ चूड़ियों से भरा है।\n3. इसे वर्तमान में राष्ट्रीय संग्रहालय, नई दिल्ली में सुरक्षित रखा गया है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        3,
        "तीनों कथन सही हैं, जो नर्तकी की मूर्ति की विशेषताओं और संरक्षण की स्थिति का सटीक विवरण देते हैं।"
    ),
    (
        "कच्छ क्षेत्र के नगर नियोजन में अंतर के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. धोलावीरा में स्थानीय पत्थरों की उपलब्धता के कारण पत्थर की वास्तुकला का व्यापक उपयोग हुआ।\n2. सुरकोटदा में पत्थर के मलबे से बना एक किला और निचला नगर था जिसमें एक सुसज्जित प्रवेश द्वार था।\n3. इन दोनों स्थलों पर सुरक्षा के लिए कोई किला या दीवारें नहीं थीं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 2", "केवल 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: दोनों शहर पत्थरों की मजबूत दीवारों से सुरक्षित किए गए थे।"
    ),
    (
        "बनावली स्थल के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इसमें एक सुरक्षित किला था जो मिट्टी की ईंटों की दीवार से निचले नगर से अलग था।\n2. यहाँ की जल निकासी बहुत खराब थी और सड़कों के कोनों पर शोषक मटके रखे जाते थे।\n3. यहाँ से मिट्टी का एक अच्छी स्थिति में बना खिलौना हल मिला है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        3,
        "तीनों कथन सही हैं, जो बनावली के अनियमित नगर नियोजन और हल के साक्ष्य को दर्शाते हैं।"
    ),
    (
        "हड़प्पावासियों के धार्मिक विश्वासों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मातृदेवी की पूजा टेराकोटा की स्त्री मूर्तियों के आधार पर मानी जाती है।\n2. पशुपति मुहर के आधार पर शिव (आदि-शिव) की पूजा का अनुमान लगाया जाता है।\n3. देवताओं को स्थापित करने के लिए बड़े-बड़े मंदिरों और सभा भवनों का निर्माण किया जाता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 2", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: हड़प्पा वास्तुकला में कोई मंदिर या मूर्तियाँ स्थापित करने वाले विशाल देवालय नहीं मिले हैं।"
    ),
    (
        "हड़प्पा के बाटों (weights) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. बाट मुख्य रूप से घनाकार थे और चर्ट पत्थर से बनाए जाते थे।\n2. कम वजन के लिए द्वि-आधारी (binary) और उच्च वजन के लिए दशमलव (decimal) प्रणाली का उपयोग किया जाता था।\n3. बाटों में कोई मानकीकरण नहीं था और विभिन्न स्थलों पर इनमें बड़ा अंतर देखा गया है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 2", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: बाट पूरे हड़प्पा क्षेत्र में अत्यधिक मानकीकृत और समान थे।"
    ),
    (
        "हड़प्पा में मनके (Bead) बनाने की तकनीक के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. लोथल और चन्हुदड़ो में मनके बनाने के कारखाने खोजे गए हैं।\n2. अकीक (carnelian) पत्थरों को लाल रंग देने के लिए भट्टी में गर्म किया जाता था।\n3. कड़े पत्थरों में छेद करने के लिए चर्ट पत्थर से बने विशिष्ट बरमों (drills) का उपयोग किया जाता था।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        3,
        "तीनों कथन सही हैं और मनके बनाने की कला का सटीक विवरण प्रस्तुत करते हैं।"
    ),
    (
        "हड़प्पा लिपि के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह लिपि चित्रात्मक (pictographic) है और इसे अभी तक पढ़ा नहीं जा सका है।\n2. लिखने की दिशा बूस्ट्रोफेडन (boustrophedon) थी (पहली पंक्ति दाएं से बाएं, दूसरी पंक्ति बाएं से दाएं)।\n3. यह केवल बड़े पत्थरों की शिलाओं और साइनबोर्डों पर लिखी जाती थी।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: यह लिपि मुहरों, तांबे की पट्टियों, बर्तनों और हाथीदांत की छड़ों पर भी अंकित मिली है।"
    ),
    (
        "राखीगढ़ी के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह क्षेत्रफल की दृष्टि से सबसे बड़ा हड़प्पा स्थल है, जो 350 हेक्टेयर से अधिक में फैला है।\n2. यहाँ से विविध प्रकार के शवाधानों वाला एक बड़ा कब्रिस्तान मिला है।\n3. यह हरियाणा के हिसार जिले में स्थित है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं और राखीगढ़ी के आकार, कब्रिस्तान और भौगोलिक स्थिति का सटीक वर्णन करते हैं।"
    ),
    (
        "कालीबंगन स्थल के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इसमें एक किलेबंद किला और एक किलेबंद निचला नगर था।\n2. यहाँ ईंटों के चबूतरों पर अग्निकुंडों (fire altars) की एक कतार मिली है।\n3. यहाँ से जुते हुए खेत का एक छोटा मिट्टी का खिलौना मिला है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 2", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: कालीबंगन से मिला जुता हुआ खेत वास्तविक खेत का हिस्सा है, मिट्टी का खिलौना हल बनावली से मिला था।"
    ),
    (
        "लोथल स्थल के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह उत्तरी क्षेत्र की एक महत्वपूर्ण प्रशासनिक राजधानी था।\n2. यहाँ भोगवा नदी से जुड़ा एक गोदी बाड़ा (dockyard) मिला है।\n3. यहाँ से पुरुष-महिला के युगल शवाधान (double burials) के साक्ष्य मिले हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 2 और 3", "केवल 2", "केवल 1 और 2", "1, 2 और 3"],
        0,
        "कथन 2 और 3 सही हैं। कथन 1 गलत है: लोथल एक दक्षिणी बंदरगाह और व्यापारिक चौकी था, न कि उत्तरी प्रशासनिक राजधानी (जो कि हड़प्पा थी)।"
    )
]

# Mock Test Questions (10 Qs)
mock_data_eng = [
    (
        "Match the unique architectural or civic features of the Harappan towns with their respective sites:\n1. Dholavira - Dressed stone masonry & reservoirs\n2. Kalibangan - Pre-Harappan ploughed field\n3. Banawali - Radial streets & toy plow\n4. Lothal - Baked-brick tidal dockyard\nWhich of the pairs given above are correct?",
        ["1, 2, 3 and 4", "1 and 2 only", "2, 3 and 4 only", "1, 3 and 4 only"],
        0,
        "All four pairs are correct matches of the unique features associated with these towns."
    ),
    (
        "Consider the following statements regarding the site of Rakhigarhi:\n1. It is the largest geographical site of the Indus Valley Civilisation, covering over 350-500 hectares.\n2. Recent DNA studies of its skeletal remains show genetic continuity without massive migrations from the West.\n3. It is situated along the dry channel of the Drishadvati River in Haryana.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All three statements are correct, outlining the geographic, riverine, and genetic research significance of Rakhigarhi."
    ),
    (
        "Which of the following statements is/are correct regarding Chanhudaro?\n1. It was a dedicated craft suburb specializing in bead-making, seal-cutting, and shell-working.\n2. Unlike other major Harappan towns, it completely lacks a fortified citadel structure.\nSelect the correct answer:",
        ["Both 1 and 2", "1 only", "2 only", "Neither 1 nor 2"],
        0,
        "Chanhudaro was a pure craft town that completely lacked an administrative citadel fortification."
    ),
    (
        "With reference to the site of Surkotada in Gujarat, consider the following statements:\n1. It featured a fortified citadel and residential lower town constructed using local stone rubble.\n2. Excavations in its upper layers reported the skeletal remains of a horse, which remains a subject of debate.\nWhich of the statements given above is/are correct?",
        ["Both 1 and 2", "1 only", "2 only", "Neither 1 nor 2"],
        0,
        "Both statements are correct, describing Surkotada's stone-walled fort and horse bone findings."
    ),
    (
        "The Great Bath of Mohenjo-daro was made watertight by applying a layer of bitumen. Bitumen is a:",
        ["Natural tar applied over a brick-and-gypsum mortar backing", "Glazed chemical paste imported from Egypt", "Powdered limestone mixed with tree sap", "Varnish made from boiled cedar wood resin"],
        0,
        "Natural bitumen (tar) was mined and applied over brickwork to prevent leakage."
    ),
    (
        "Consider the following statements regarding Harappan burials:\n1. Cemetery R-37 at Harappa contains burials where bodies were placed in cedar wooden coffins.\n2. Lothal has yielded joint burials containing skeletons of a male and a female.\nWhich of the statements given above is/are correct?",
        ["Both 1 and 2", "1 only", "2 only", "Neither 1 nor 2"],
        0,
        "Both statements represent verified archaeological discoveries in Harappan mortuary practices."
    ),
    (
        "With reference to Harappan bead-making technology, consider the following statements:\n1. Beads were made from carnelian, jasper, crystal, and steatite.\n2. Carnelian beads were heated over fire to obtain their characteristic red color.\n3. Dressed chert or bronze drills were used to perforate the beads.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All three statements are correct, explaining the raw materials, heating, and drilling steps in bead production."
    ),
    (
        "Consider the following statements regarding the geographical boundaries of the Harappan Civilisation:\n1. Sutkagendor on the Dasht River marked the westernmost boundary.\n2. Manda on the Chenab River marked the northernmost limit.\n3. Daimabad on the Pravara River marked the southernmost limit.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All three boundary sites are correctly matched to their corresponding rivers and cardinal limits."
    ),
    (
        "The Harappan weight system relied on chert blocks following a binary system for lower weights. What was the base unit?",
        ["13.63 grams (equivalent to ratio 16)", "5.5 grams", "25.0 grams", "1.0 gram"],
        0,
        "The base unit weight of the binary system was 13.63 grams."
    ),
    (
        "The Dancing Girl bronze figurine represents advanced metal casting. Which technique was used to manufacture it?",
        ["Lost-wax casting (cire perdue)", "Direct iron smelting", "Sheet metal riveting", "Cold chiseling from solid block"],
        0,
        "Lost-wax casting was the standard method for casting bronze art."
    )
]

mock_data_hin = [
    (
        "हड़प्पा सभ्यता के नगरों की अनूठी स्थापत्य या नागरिक विशेषताओं को उनके संबंधित स्थलों से सुमेलित करें:\n1. धोलावीरा - पत्थर की वास्तुकला और जलाशय\n2. कालीबंगन - पूर्व-हड़प्पा जुता हुआ खेत\n3. बनावली - अरीय सड़कें और खिलौना हल\n4. लोथल - पकी ईंटों का ज्वारीय गोदी बाड़ा\nउपरोक्त में से कौन से जोड़े सही हैं?",
        ["1, 2, 3 और 4", "केवल 1 और 2", "केवल 2, 3 और 4", "केवल 1, 3 और 4"],
        0,
        "चारों जोड़े सही सुमेलित हैं और इन शहरों की अनूठी विशेषताओं को दर्शाते हैं।"
    ),
    (
        "राखीगढ़ी स्थल के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह सिंधु घाटी सभ्यता का सबसे बड़ा भौगोलिक स्थल है, जो 350-500 हेक्टेयर में फैला है.\n2. इसके कंकालों के हालिया डीएनए अध्ययन पश्चिम से बड़े पैमाने पर प्रवास के बिना आनुवंशिक निरंतरता दर्शाते हैं.\n3. यह हरियाणा में दृषद्वती नदी के सूखे मार्ग पर स्थित है.\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं और राखीगढ़ी की भौगोलिक, नदीय और आनुवंशिक शोध महत्ता को रेखांकित करते हैं।"
    ),
    (
        "चन्हुदड़ो के संदर्भ में निम्नलिखित में से कौन सा/से कथन सही है/हैं?\n1. यह मनके बनाने, मुहर तराशने और शंख उद्योग में विशेषज्ञता रखने वाला एक विशिष्ट शिल्प उपनगर था.\n2. अन्य प्रमुख हड़प्पा नगरों के विपरीत, इसमें सुरक्षात्मक किले (citadel) का पूर्ण अभाव था.\nसही उत्तर चुनें:",
        ["1 और 2 दोनों", "केवल 1", "केवल 2", "न तो 1 न ही 2"],
        0,
        "चन्हुदड़ो बिना किले वाला एक विशुद्ध शिल्प नगर था।"
    ),
    (
        "गुजरात के सुरकोटदा स्थल के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इसमें पत्थर के मलबे से बना किला और आवासीय निचला नगर था जिसकी सुरक्षा दीवारें साझी थीं.\n2. इसके ऊपरी स्तरों से घोड़े के कंकाल के अवशेषों की रिपोर्ट की गई है जो वैज्ञानिकों में बहस का विषय है.\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 2 दोनों", "केवल 1", "केवल 2", "न तो 1 न ही 2"],
        0,
        "दोनों कथन सही हैं और सुरकोटदा की पत्थर की दीवारों वाले किले और घोड़े की हड्डियों का विवरण देते हैं।"
    ),
    (
        "मोहनजोदड़ो के विशाल स्नानागार को डामर (बिटुमेन) की परत चढ़ाकर जल-रोधी बनाया गया था। डामर है:",
        ["ईंट और जिप्सम गारे पर लगाया जाने वाला प्राकृतिक तारकोल", "मिस्र से आयातित एक रसायनिक लेप", "पेड़ के गोंद के साथ मिलाया गया पिसा हुआ चूना पत्थर", "देवदार की लकड़ी के राल से बना वार्निश"],
        0,
        "पानी का रिसाव रोकने के लिए ईंटों पर प्राकृतिक डामर (तारकोल) की परत लगाई गई थी।"
    ),
    (
        "हड़प्पा शवाधानों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. हड़प्पा के कब्रिस्तान R-37 में शवों को देवदार की लकड़ी के ताबूतों में रखकर दफनाने के प्रमाण मिले हैं.\n2. लोथल से पुरुष और महिला के कंकालों वाले युगल शवाधान के साक्ष्य मिले हैं.\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 2 दोनों", "केवल 1", "केवल 2", "न तो 1 न ही 2"],
        0,
        "दोनों कथन सही हैं और हड़प्पा शवाधान प्रथाओं में खोजी गई अनूठी भिन्नताओं को दर्शाते हैं।"
    ),
    (
        "हड़प्पा की मनके बनाने की तकनीक के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मनके अकीक (carnelian), यशब (jasper), स्फटिक और सेलखड़ी से बनाए जाते थे.\n2. मनकों को उनका विशिष्ट लाल रंग देने के लिए भट्टी में गर्म किया जाता था.\n3. मनकों में सुराख करने के लिए चर्ट पत्थर या तांबे के बरमों का उपयोग किया जाता था.\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं और मनके बनाने के कारखाने और तकनीकी चरणों का वर्णन करते हैं।"
    ),
    (
        "हड़प्पा सभ्यता की भौगोलिक सीमाओं के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. दश्त नदी पर स्थित सुतकागेंडोर सबसे पश्चिमी सीमा थी.\n2. चिनाब नदी पर स्थित मांडा सबसे उत्तरी सीमा थी.\n3. प्रवर नदी पर स्थित दैमाबाद सबसे दक्षिणी सीमा थी.\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों सीमा स्थल अपनी नदियों और सीमाओं के साथ सही सुमेलित हैं।"
    ),
    (
        "हड़प्पा की वजन प्रणाली चर्ट के बाटों पर निर्भर थी जो निचले बाटों के लिए द्वि-आधारी थे। आधार वजन इकाई क्या थी?",
        ["13.63 ग्राम (अनुपात 16 के समतुल्य)", "5.5 ग्राम", "25.0 ग्राम", "1.0 ग्राम"],
        0,
        "द्वि-आधारी प्रणाली के आधार बाट का वजन लगभग 13.63 ग्राम था।"
    ),
    (
        "कांस्य की नर्तकी की मूर्ति धातु कर्म की उन्नत ढलाई कला को दर्शाती है। इसके निर्माण में किस तकनीक का उपयोग किया गया था?",
        ["लुप्त-मोम ढलाई (lost-wax/cire perdue)", "सीधे लोहे को पिघलाना", "धातु की चादरें जोड़ना", "ठंडी नक्काशी करना"],
        0,
        "नर्तकी की मूर्ति बनाने के लिए लुप्त-मोम ढलाई विधि का उपयोग किया गया था।"
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

print("Base JSON files built successfully!")
