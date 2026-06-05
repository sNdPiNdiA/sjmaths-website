import json
import os

ENG_DIR = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\HarappanIndus-Valley-Civilisation\Geography-and-Archaeological-Findings-of-Indus-Valley-Civilisation"
HIN_DIR = os.path.join(ENG_DIR, "hi")

os.makedirs(HIN_DIR, exist_ok=True)

# Common Options
mcq_opts = ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"]
ar_opts = [
    "Both A and R are true and R is the correct explanation of A",
    "Both A and R are true but R is not the correct explanation of A",
    "A is true but R is false",
    "A is false but R is true"
]

hin_mcq_opts = ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"]
hin_ar_opts = [
    "A और R दोनों सत्य हैं और R, A की सही व्याख्या है",
    "A और R दोनों सत्य हैं लेकिन R, A की सही व्याख्या नहीं है",
    "A सत्य है लेकिन R असत्य है",
    "A असत्य है लेकिन R सत्य है"
]

# Skeletons
eng_data = {
    "breadcrumbs": {
        "parent": "UPSC Syllabus",
        "parentUrl": "/upsc/",
        "current": "Geography and Archaeological Findings of Indus Valley Civilisation"
    },
    "hero": {
        "title": "Geography and Archaeological Findings of Indus Valley Civilisation",
        "description": "Master the geographical extent, frontiers, river settings, urban settlement typologies, and key archaeological discoveries of the Indus Valley Civilisation for UPSC GS-1."
    },
    "labels": {
        "clickToExpand": "Click to expand details",
        "mockIntro": {
            "title": "Interactive UPSC Mock Test",
            "description": "Test your knowledge on the Geography and Archaeological Findings of Indus Valley Civilisation. This timed test contains 10 high-quality, exam-standard questions with negative marking. Perfect for self-evaluation.",
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
                "period": "Geographical Frontiers",
                "date": "Frontiers & Boundaries",
                "details": "The massive triangular boundary of the Indus Valley Civilisation spanning 1.3-1.5 million sq km, from Manda in Jammu to Daimabad in Maharashtra, and Sutkagendor in Balochistan to Alamgirpur in Uttar Pradesh."
            },
            {
                "period": "Settlement Typologies",
                "date": "Cities & Craft Suburbs",
                "details": "Standardized town planning with Citadels and Lower Towns. Includes Dholavira's stone-cut reservoirs and three-tier layout, Lothal's baked-brick tidal dockyard, Chanhudaro's unfortified industrial bead factories, and Rakhigarhi as the largest metropolis."
            },
            {
                "period": "Material Findings",
                "date": "Artifacts & Technology",
                "details": "Rich archaeological discoveries including steatite seals (unicorn, Pashupati), bronze casting (Dancing Girl), stone art (Priest-King), cubical chert weights, and red-and-black painted pottery."
            }
        ]
    },
    "mnemonics": {
        "title": "Mnemonics & Memory Hacks",
        "description": "Use these visual memory hooks to retain critical geographical facts and findings for the UPSC Civil Services Examination.",
        "items": [
            {
                "title": "Mnemonic 1: Boundary Site Cardinal Directions",
                "phrase": "\"M-D-S-A (My Dear Sweet Ally) - Boundaries\"",
                "decryption": "**M**anda (North), **D**aimabad (South), **S**utkagendor (West), **A**lamgirpur (East) (**MDSA**)."
            },
            {
                "title": "Mnemonic 2: Unique Archaeological Capitals",
                "phrase": "\"L-C-D (Lothal Craft Dholavira) - Specialized Cities\"",
                "decryption": "**L**othal (Dockyard), **C**anhudaro (Craft center), **D**holavira (Dams and Reservoirs) (**LCD**)."
            },
            {
                "title": "Mnemonic 3: Rivers of Key Frontier Sites",
                "phrase": "\"C-P-D-H (Chenab Pravara Dasht Hindon) - River Frontiers\"",
                "decryption": "Manda along **C**henab, Daimabad along **P**ravara, Sutkagendor along **D**asht, Alamgirpur along **H**indon (**CPDH**)."
            }
        ]
    },
    "traps": {
        "title": "UPSC Common Exam Traps to Avoid",
        "items": [
            "<strong>Trap 1: The 'All Cities Fortified' Fallacy:</strong> UPSC may claim every major city was fortified. **False.** Chanhudaro in Sindh had no administrative citadel or fortifications. Dholavira was divided into three fortified sections, not the typical two.",
            "<strong>Trap 2: Dockyards at All Coastal Sites:</strong> Do not assume all coastal sites have dockyards. **Lothal** is the only site with an excavated baked-brick tidal dockyard. Sutkagendor and Balakot were coastal outposts but lack dockyards.",
            "<strong>Trap 3: Domestication of the Horse:</strong> UPSC often tests the presence of horse. While **Surkotada** yielded equine bones, there is no evidence that horses were domesticated or played a major role in the mature Harappan agricultural economy.",
            "<strong>Trap 4: Material Differences in Seals and Weights:</strong> Do not confuse materials. Seals were primarily made of soft **steatite** (soapstone), whereas weights were cubical blocks made of hard **chert**."
        ]
    },
    "flashcards": {
        "title": "Active Recall Flashcards",
        "description": "Flashcards are key to mastering fact-dense UPSC questions. Click on any card below to flip it and reveal the answer.",
        "items": [
            {
                "question": "Which site represents the westernmost boundary of the Indus Valley Civilisation?",
                "answer": "<strong>Sutkagendor</strong> on the Dasht River in Pakistani Balochistan, near the Iranian border.",
                "icon": "fa-compass"
            },
            {
                "question": "Name the largest geographic site of the Indus Valley Civilisation by area.",
                "answer": "<strong>Rakhigarhi</strong> in Haryana, spanning over 350 hectares.",
                "icon": "fa-map"
            },
            {
                "question": "Which major Harappan town uniquely lacks a fortified citadel?",
                "answer": "<strong>Chanhudaro</strong> in Sindh, which functioned primarily as an unfortified industrial craft suburb.",
                "icon": "fa-industry"
            },
            {
                "question": "Where was the famous stone sculpture of the Priest-King found?",
                "answer": "<strong>Mohenjo-daro</strong>. It is carved from steatite and shows a trefoil shawl pattern.",
                "icon": "fa-crown"
            },
            {
                "question": "What is the key difference between Harappan seals and weights?",
                "answer": "Seals were carved from soft **steatite** (soapstone) and baked, while weights were standardized cubical blocks of hard **chert**.",
                "icon": "fa-scale-balanced"
            }
        ]
    },
    "deepDive": {
        "title": "Syllabus Core Study Notes (Deep-Dive)",
        "description": "Master the extent, environmental settings, settlement patterns, and artifact assemblages of the Indus Valley Civilisation.",
        "sections": [
            {
                "title": "1. Geographical Extent, Boundaries, and Environmental Settings",
                "content": """<p>The Indus Valley Civilisation (IVC) at its peak (c. 2600 BCE – 1900 BCE) covered an estimated area of 1.3 to 1.5 million square kilometers, forming a massive triangular geographic layout. It spanned modern Pakistan, northwest India, and parts of Afghanistan.</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-compass"></i> Geographical Frontiers & Boundaries</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>Northern Frontier:</strong> Manda in Jammu & Kashmir (right bank of the Chenab River).</li>
      <li><strong>Southern Frontier:</strong> Daimabad in Maharashtra (Pravara River, a tributary of the Godavari).</li>
      <li><strong>Western Frontier:</strong> Sutkagendor in Pakistani Balochistan (on the Dasht River, near the Iranian border).</li>
      <li><strong>Eastern Frontier:</strong> Alamgirpur in western Uttar Pradesh (Hindon River, a tributary of the Yamuna).</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-cloud-sun-rain"></i> Environmental Settings & River Networks</div>
    <p style="font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;">
      The core heartland lay along the Indus River and the Ghaggar-Hakra river system (often identified with the dry Sarasvati). The climate was semi-arid, requiring floodwater management. Annual monsoonal floods deposited fertile alluvial silt, allowing winter sowing (rabi crops) of wheat and barley without large-scale canal networks. Outposts like Shortughai in northern Afghanistan were established to exploit the Central Asian lapis lazuli trade.
    </p>
  </div>
</div>""",
                "masteryZone": []
            },
            {
                "title": "2. Major Settlement Types and Urban Centers",
                "content": """<p>Civic planning and town layout are the most defining elements of Mature Harappan urbanisation. Settlements ranged from large metropolises to small craft suburbs and coastal ports.</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-city"></i> Civic Layout & Fortifications</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>Citadel & Lower Town:</strong> Most cities were divided into a western raised Citadel (public buildings) and an eastern Lower Town (residential).</li>
      <li><strong>Three-Tier Division:</strong> Dholavira is unique for its three sections: Citadel, Middle Town, and Lower Town, utilizing local stone instead of bricks.</li>
      <li><strong>Citadel-Free Site:</strong> Chanhudaro in Sindh was a dedicated industrial craft town that completely lacked a fortified citadel.</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-industry"></i> Specialized Urban Roles</div>
    <p style="font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;">
      <strong>Lothal</strong> was a coastal port featuring a massive baked-brick tidal dockyard. <strong>Kalibangan</strong> in Rajasthan features fire altars and a pre-mature ploughed agricultural field. <strong>Rakhigarhi</strong> in Haryana is the largest geographical site of the IVC, spanning over 350 hectares. <strong>Banawali</strong> in Haryana represents a degenerate town layout with radial streets and yielded a terracotta model of a agricultural plow.
    </p>
  </div>
</div>""",
                "masteryZone": []
            },
            {
                "title": "3. Key Archaeological Findings, Materials, and Cultural Artifacts",
                "content": """<p>Indus Valley artisans achieved high standards in metallurgy, stone sculpture, seal engraving, and standardized measurement systems, proving a centralized administrative authority.</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-hammer"></i> Artifacts & Artistry</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>Dancing Girl:</strong> A solid bronze casting made using the lost-wax (cire perdue) process, found at Mohenjo-daro.</li>
      <li><strong>Priest-King:</strong> A steatite (soapstone) bust wearing a draped trefoil-patterned shawl.</li>
      <li><strong>Steatite Seals:</strong> Square seals containing short inscriptions and animal motifs (unicorn, humped zebu bull, Pashupati).</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-scale-balanced"></i> Standarization & Burials</div>
    <p style="font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;">
      Weights were highly standardized cubical chert blocks, following a binary progression for lower weights and decimal for higher weights. The basic unit of weight was 13.63g. Burials were typically in north-south orientation with pottery. <strong>Cemetery R-37</strong> at Harappa contains unique wooden coffin burials. Lothal features unique joint double burials. Painted pottery was Red and Black ware.
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

# Translate skeletons for Hindi
hin_data = {
    "breadcrumbs": {
        "parent": "यूपीएससी पाठ्यक्रम",
        "parentUrl": "/upsc/",
        "current": "सिंधु घाटी सभ्यता का भूगोल और पुरातात्विक खोजें"
    },
    "hero": {
        "title": "सिंधु घाटी सभ्यता का भूगोल और पुरातात्विक खोजें",
        "description": "यूपीएससी परीक्षा (GS-1) के लिए सिंधु घाटी सभ्यता के भौगोलिक विस्तार, सीमाओं, पर्यावरणीय परिस्थितियों, शहरी बस्तियों और प्रमुख पुरातात्विक खोजों पर महारत हासिल करें।"
    },
    "labels": {
        "clickToExpand": "विवरण देखने के लिए क्लिक करें",
        "mockIntro": {
            "title": "इंटरैक्टिव यूपीएससी मॉक टेस्ट",
            "description": "सिंधु घाटी सभ्यता के भूगोल और पुरातात्विक खोजों पर अपने ज्ञान का परीक्षण करें। इस समयबद्ध परीक्षण में नकारात्मक अंकन के साथ 10 उच्च गुणवत्ता वाले प्रश्न हैं।",
            "startBtn": "मॉक टेस्ट शुरू करें"
        },
        "mockPlay": {
            "prevBtn": "पिछला प्रश्न",
            "nextBtn": "अगला प्रश्न",
            "submitBtn": "परीक्षण सबमिट करें"
        }
    },
    "timeline": {
        "title": "भौगोलिक और बस्तियों का क्षितिज",
        "description": "भौगोलिक सीमाओं, नगर नियोजन और सिंधु घाटी सभ्यता की भौतिक खोजों के क्रमिक विकास का पता लगाएं।",
        "cards": [
            {
                "period": "भौगोलिक सीमाएँ",
                "date": "विस्तार और पर्यावरण",
                "details": "सिंधु घाटी सभ्यता की विशाल त्रिकोणीय सीमा 13-15 लाख वर्ग किलोमीटर में फैली थी, जो उत्तर में जम्मू के मांडा से दक्षिण में महाराष्ट्र के दैमाबाद तक, और पश्चिम में बलूचिस्तान के सुतकागेंडोर से पूर्व में उत्तर प्रदेश के आलमगीरपुर तक थी।"
            },
            {
                "period": "बस्ती के प्रकार",
                "date": "शहर और शिल्प केंद्र",
                "details": "दुर्ग (Citadel) और निचले नगर (Lower Town) के साथ मानकीकृत नगर नियोजन। इसमें धोलावीरा के पत्थर के जलाशय और त्रि-स्तरीय नगर नियोजन, लोथल का पकी ईंटों से बना गोदीवाड़ा (dockyard), चन्हुदड़ो के बिना दुर्ग वाले मनके बनाने के कारखाने और राखीगढ़ी शामिल हैं।"
            },
            {
                "period": "भौतिक खोजें",
                "date": "कलाकृतियाँ और तकनीक",
                "details": "सेलखड़ी की मुहरें (एकश्रृंगी, पशुपति), कांसे की मूर्तियाँ (नर्तकी), पत्थर की कला (पुरोहित-राजा), चर्ट पत्थर के घनाकार बाट, और लाल व काले चित्रित मृदभांड।"
            }
        ]
    },
    "mnemonics": {
        "title": "याद रखने के स्मृति सूत्र (Mnemonics)",
        "description": "महत्वपूर्ण भौगोलिक तथ्यों और खोजों को याद रखने के लिए इन स्मृति सूत्रों का उपयोग करें।",
        "items": [
            {
                "title": "स्मृति सूत्र 1: सीमा स्थलों की दिशाएँ",
                "phrase": "\"M-D-S-A (माय डियर स्वीट एली) - सीमाएँ\"",
                "decryption": "**M**anda (उत्तर), **D**aimabad (दक्षिण), **S**utkagendor (पश्चिम), **A**lamgirpur (पूर्व) (**MDSA**)।"
            },
            {
                "title": "स्मृति सूत्र 2: विशिष्ट पुरातात्विक राजधानियाँ",
                "phrase": "\"L-C-D (लोथल क्राफ्ट धोलावीरा) - विशिष्ट शहर\"",
                "decryption": "**L**othal (गोदीवाड़ा / dockyard), **C**anhudaro (शिल्प केंद्र), **D**holavira (बांध और जलाशय) (**LCD**)।"
            },
            {
                "title": "स्मृति सूत्र 3: प्रमुख सीमा स्थलों की नदियाँ",
                "phrase": "\"C-P-D-H (चिनाब प्रवरा दश्त हिंडन) - सीमा नदियाँ\"",
                "decryption": "मांडा **C**henab नदी, दैमाबाद **P**ravara नदी, सुतकागेंडोर **D**asht नदी, आलमगीरपुर **H**indon नदी के किनारे स्थित हैं (**CPDH**)।"
            }
        ]
    },
    "traps": {
        "title": "यूपीएससी परीक्षा के सामान्य जाल (टैप्स) जिनसे बचें",
        "items": [
            "<strong>जाल 1: 'सभी शहर किलेबंद थे' का भ्रम:</strong> यूपीएससी दावा कर सकता है कि हर शहर किलेबंद था। **गलत।** सिंध के चन्हुदड़ो में कोई प्रशासनिक दुर्ग या किलेबंदी नहीं थी। धोलावीरा दो के बजाय तीन भागों में विभाजित था।",
            "<strong>जाल 2: सभी तटीय स्थलों पर गोदीवाड़ा (Dockyard):</strong> यह न मानें कि सभी तटीय स्थलों पर गोदीवाड़ा था। केवल **लोथल** से पकी ईंटों का गोदीवाड़ा मिला है। सुतकागेंडोर और बालाकोट तटीय चौकियाँ थीं लेकिन वहाँ कोई गोदीवाड़ा नहीं था।",
            "<strong>जाल 3: घोड़े का घरेलूकरण:</strong> यूपीएससी अक्सर घोड़े की उपस्थिति का परीक्षण करता है। हालांकि **सुरकोटदा** से घोड़े की हड्डियां मिली हैं, लेकिन इस बात का कोई पुख्ता सबूत नहीं है कि परिपक्व हड़प्पा काल में घोड़े पालतू थे या कृषि में महत्वपूर्ण भूमिका निभाते थे।",
            "<strong>जाल 4: मुहरों और बाटों की निर्माण सामग्री:</strong> निर्माण सामग्री में भ्रमित न हों। मुहरें मुख्य रूप से नरम **सेलखड़ी (steatite)** से बनी थीं, जबकि बाट कठोर **चर्ट (chert)** पत्थर से बने चौकोर टुकड़े थे।"
        ]
    },
    "flashcards": {
        "title": "सक्रिय स्मरण फ्लैशकार्ड (Active Recall Flashcards)",
        "description": "फ्लैशकार्ड तथ्य-प्रधान यूपीएससी प्रश्नों को याद रखने के लिए अत्यंत उपयोगी हैं। कार्ड को पलटने और उत्तर देखने के लिए उस पर क्लिक करें।",
        "items": [
            {
                "question": "सिंधु घाटी सभ्यता की सबसे पश्चिमी सीमा का प्रतिनिधित्व कौन सा स्थल करता है?",
                "answer": "पाकिस्तानी बलूचिस्तान में दश्त नदी के किनारे स्थित <strong>सुतकागेंडोर</strong> (ईरानी सीमा के पास)।",
                "icon": "fa-compass"
            },
            {
                "question": "क्षेत्रफल की दृष्टि से सिंधु घाटी सभ्यता का सबसे बड़ा भौगोलिक स्थल कौन सा है?",
                "answer": "हरियाणा का <strong>राखीगढ़ी</strong>, जो 350 हेक्टेयर से अधिक क्षेत्र में फैला है।",
                "icon": "fa-map"
            },
            {
                "question": "हड़प्पा सभ्यता का कौन सा प्रमुख नगर बिना किसी गढ़ या दुर्ग (citadel) के था?",
                "answer": "सिंध का <strong>चन्हुदड़ो</strong>, जो मुख्य रूप से एक औद्योगिक शिल्प उपनगर था।",
                "icon": "fa-industry"
            },
            {
                "question": "पुरोहित-राजा (Priest-King) की प्रसिद्ध पत्थर की मूर्ति कहाँ पाई गई थी?",
                "answer": "<strong>मोहनजोदड़ो</strong> से। यह सेलखड़ी (steatite) से बनी है और तिपतिया शॉल ओढ़े हुए है।",
                "icon": "fa-crown"
            },
            {
                "question": "हड़प्पा मुहरों और बाटों की निर्माण सामग्री में क्या मुख्य अंतर है?",
                "answer": "मुहरें मुख्य रूप से नरम <strong>सेलखड़ी (steatite)</strong> से बनती थीं, जबकि बाट कठोर <strong>चर्ट (chert)</strong> पत्थर से बने घनाकार टुकड़े थे।",
                "icon": "fa-scale-balanced"
            }
        ]
    },
    "deepDive": {
        "title": "पाठ्यक्रम मुख्य अध्ययन नोट्स (गहन अध्ययन)",
        "description": "सिंधु घाटी सभ्यता के भौगोलिक विस्तार, पर्यावरणीय परिस्थितियों, बस्तियों के प्रकार और कलाकृतियों पर विस्तृत अध्ययन नोट्स।",
        "sections": [
            {
                "title": "1. भौगोलिक विस्तार, सीमाएँ और पर्यावरणीय स्थिति",
                "content": """<p>सिंधु घाटी सभ्यता (IVC) अपने चरम पर (लगभग 2600 ईसा पूर्व - 1900 ईसा पूर्व) लगभग 13 से 15 लाख वर्ग किलोमीटर के क्षेत्र में फैली हुई थी, जो एक विशाल त्रिकोणीय भौगोलिक आकार बनाती थी। यह आधुनिक पाकिस्तान, उत्तर-पश्चिम भारत और अफगानिस्तान के कुछ हिस्सों में फैली हुई थी।</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-compass"></i> भौगोलिक सीमाएँ</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>उत्तरी सीमा:</strong> जम्मू-कश्मीर में मांडा (चिनाब नदी का दाहिना तट)।</li>
      <li><strong>दक्षिणी सीमा:</strong> महाराष्ट्र में दैमाबाद (गोदावरी की सहायक नदी प्रवरा)।</li>
      <li><strong>पश्चिमी सीमा:</strong> पाकिस्तानी बलूचिस्तान में सुतकागेंडोर (दश्त नदी के किनारे, ईरानी सीमा के पास)।</li>
      <li><strong>पूर्वी सीमा:</strong> पश्चिमी उत्तर प्रदेश में आलमगीरपुर (यमुना की सहायक नदी हिंडन)।</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-cloud-sun-rain"></i> पर्यावरणीय स्थिति और नदी प्रणाली</div>
    <p style="font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;">
      सभ्यता का मुख्य केंद्र सिंधु और घग्गर-हाकड़ा नदी प्रणाली (जिसे प्राचीन सरस्वती नदी मार्ग माना जाता है) के किनारे स्थित था। यहाँ की जलवायु अर्ध-शुष्क थी। मानसूनी बाढ़ द्वारा हर साल लाई जाने वाली उपजाऊ जलोढ़ मिट्टी से बिना नहरों के ही सर्दियों की फसलें (गेहूं, जौ) उगाई जाती थीं। अफ़गानिस्तान के शॉर्टुघई में स्थापित व्यापारिक चौकी का उपयोग बलोचिस्तान और मध्य एशिया के व्यापार और लाजवर्त मणि (Lapis Lazuli) को नियंत्रित करने के लिए किया जाता था।
    </p>
  </div>
</div>""",
                "masteryZone": []
            },
            {
                "title": "2. प्रमुख बस्तियों के प्रकार और शहरी केंद्र",
                "content": """<p>नागरिक योजना और नगर नियोजन परिपक्व हड़प्पा काल की सबसे प्रमुख विशेषताएँ हैं। बस्तियाँ बड़े महानगरों से लेकर छोटे औद्योगिक उपनगरों और तटीय बंदरगाहों तक फैली हुई थीं।</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-city"></i> नगर नियोजन और किलेबंदी</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>दुर्ग और निचला नगर:</strong> अधिकांश शहर दो भागों में विभाजित थे: पश्चिम में स्थित प्रशासनिक दुर्ग (Citadel) और पूर्व में आम जनता के लिए निचला नगर।</li>
      <li><strong>त्रि-स्तरीय विभाजन:</strong> गुजरात का धोलावीरा अपने त्रि-स्तरीय विभाजन (दुर्ग, मध्य नगर और निचला नगर) के लिए प्रसिद्ध है, जहाँ ईंटों के स्थान पर स्थानीय पत्थरों का उपयोग हुआ है।</li>
      <li><strong>बिना दुर्ग वाला स्थल:</strong> सिंध का चन्हुदड़ो एकमात्र ऐसा प्रमुख नगर है जहाँ किसी प्रशासनिक दुर्ग के साक्ष्य नहीं मिले हैं; यह एक पूर्ण शिल्प केंद्र था।</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-industry"></i> विशिष्ट नगर प्रकार</div>
    <p style="font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;">
      <strong>लोथल</strong> गुजरात में एक तटीय गोदी (dockyard) वाला स्थल था, जो पकी ईंटों से बना था। <strong>कालीबंगन</strong> राजस्थान में स्थित है जहाँ अग्निवेदियाँ और आड़े-तिरछे जुते हुए खेत मिले हैं। <strong>राखीगढ़ी</strong> हरियाणा में स्थित सबसे बड़ा भौगोलिक हड़प्पा स्थल है, जो 350 हेक्टेयर से अधिक में फैला है। <strong>बनावली</strong> हरियाणा में स्थित है जहाँ से मिट्टी का हल मिला है और यहाँ ग्रिड प्रणाली की कमी थी।
    </p>
  </div>
</div>""",
                "masteryZone": []
            },
            {
                "title": "3. प्रमुख पुरातात्विक खोजें, सामग्री और कलाकृतियाँ",
                "content": """<p>सिंधु घाटी के कारीगरों ने धातु विज्ञान, पत्थर की मूर्तिकला, मुहर उत्कीर्णन और मानकीकृत मापन प्रणालियों में उच्च मानदंड हासिल किए, जो एक केंद्रीय प्रशासनिक प्राधिकरण को साबित करते हैं।</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-hammer"></i> कलाकृतियाँ और धातु कर्म</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>नर्तकी की मूर्ति:</strong> मोहनजोदड़ो से प्राप्त यह मूर्ति ठोस कांसे की है, जिसे लुप्त-मोम (lost-wax/cire perdue) विधि से ढाला गया था।</li>
      <li><strong>पुरोहित-राजा की मूर्ति:</strong> सेलखड़ी (steatite) से बनी यह अर्ध-मूर्ति तिपतिया (trefoil) पैटर्न वाली शॉल ओढ़े हुए है।</li>
      <li><strong>सेलखड़ी की मुहरें:</strong> चौकोर मुहरें जिन पर संक्षिप्त लेख और एकश्रृंगी (unicorn), कूबड़ वाले बैल और पशुपति के चित्र उत्कीर्ण हैं।</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-scale-balanced"></i> मानकीकरण और शवाधान</div>
    <p style="font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;">
      बांट प्रणाली मानकीकृत चर्ट पत्थर से बनी थी, जो निचली श्रेणियों में द्वि-आधारी (binary - 1, 2, 4, 8, 16...) और उच्च श्रेणियों में दशमलव पद्धति का पालन करती थी। मूल इकाई 13.63 ग्राम थी। <strong>कब्रिस्तान R-37</strong> हड़प्पा में स्थित है जहाँ देवदार की लकड़ी के ताबूत वाले शवाधान मिले हैं। लोथल से युगल शवाधान मिले हैं। विशिष्ट मृदभांड लाल और काले चित्रित शैली के थे।
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

# =========================================================================
# SECTION 1: GEOGRAPHICAL EXTENT, BOUNDARIES, AND ENVIRONMENT (62 Qs)
# =========================================================================
s1_mastery_eng = []

# MCQs (5)
for q, opts, ans, sol in [
    ("Which of the following sites represents the westernmost boundary of the Indus Valley Civilisation?", ["Manda", "Daimabad", "Sutkagendor", "Alamgirpur"], 2, "Sutkagendor in Balochistan represents the westernmost frontier, situated on the Dasht River."),
    ("The highest density of Indus Valley settlements has been discovered in which river basin?", ["The Indus River Basin", "The Ghaggar-Hakra River Basin", "The Ganga-Yamuna Basin", "The Narmada Valley Basin"], 1, "The Ghaggar-Hakra system hosts the highest concentration of settlements (often linked to the heartland of the culture)."),
    ("Manda, the northernmost limit of the mature Harappan phase, is situated on the banks of which river?", ["Sutlej", "Chenab", "Jhelum", "Indus"], 1, "Manda is located in Jammu & Kashmir along the right bank of the Chenab River."),
    ("The southern boundary of the Indus Valley Civilisation is marked by Daimabad, which is located in which modern state?", ["Gujarat", "Maharashtra", "Rajasthan", "Madhya Pradesh"], 1, "Daimabad is situated in Ahmednagar district, Maharashtra, on the Pravara River, a tributary of the Godavari."),
    ("The geographical outpost of Shortughai, indicating direct access to Central Asian lapis lazuli trade, is in which country?", ["Iran", "Pakistan", "Afghanistan", "Tajikistan"], 2, "Shortughai is a Harappan trading outpost situated in northern Afghanistan.")
]:
    s1_mastery_eng.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# Multi-Correct (5)
for q, opts, ans, sol in [
    ("Identify the coastal ports and maritime trading outposts of the Indus Civilisation: (Select all that apply)", ["Lothal", "Sutkagendor", "Balakot", "Shortughai"], [0, 1, 2], "Lothal, Sutkagendor, and Balakot are coastal maritime outposts. Shortughai is an inland northern trade enclave."),
    ("Which of the following sites are situated in the modern state of Gujarat? (Select all that apply)", ["Dholavira", "Surkotada", "Rojdi", "Banawali"], [0, 1, 2], "Dholavira, Surkotada, and Rojdi are in Gujarat. Banawali is in Haryana."),
    ("Select the sites situated in the Ghaggar-Hakra river basin in Haryana: (Select all that apply)", ["Rakhigarhi", "Banawali", "Bhirrana", "Amri"], [0, 1, 2], "Rakhigarhi, Banawali, and Bhirrana are Ghaggar-Hakra basin sites in Haryana. Amri is in Sindh."),
    ("Which boundaries define the geographical quadrangle of the Indus Valley Civilisation? (Select all that apply)", ["Manda in Jammu (North)", "Daimabad in Maharashtra (South)", "Sutkagendor in Balochistan (West)", "Mehrgarh in Balochistan (South)"], [0, 1, 2], "The boundaries are Manda (North), Daimabad (South), Sutkagendor (West), and Alamgirpur (East). Mehrgarh is a neolithic site."),
    ("Which agricultural crop zones were geographically distinct in the Harappan empire? (Select all that apply)", ["Wheat and Barley in Punjab/Sindh", "Rice cultivation in Gujarat (Lothal/Rangpur)", "Mustard and Sesame in dry plains", "Sugarcane across Gangetic outposts"], [0, 1, 2], "Wheat, barley, mustard, sesame, and rice were grown. Sugarcane was not cultivated by Harappans.")
]:
    s1_mastery_eng.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# True/False (8)
for q, ans, sol in [
    ("The geographical area of the Indus Valley Civilisation was larger than contemporary Egypt and Mesopotamia combined.", True, "True. The IVC covered over 1 million sq km, dwarfing other contemporary civilizations."),
    ("Daimabad, the southernmost limit, is situated on the Godavari River itself.", False, "False. It is on the Pravara River, a tributary of the Godavari."),
    ("Shortughai in Afghanistan was established as a major agricultural colony to export wheat to Harappa.", False, "False. It was a trading colony established near Badakhshan to directly control the lapis lazuli trade."),
    ("The Ghaggar-Hakra river basin was completely dry during the entire Mature Harappan period.", False, "False. The river was perennial during the Mature period and only dried up gradually, causing decline."),
    ("Alamgirpur, the easternmost outpost, is located in Meerut district along the Hindon River.", True, "True. Alamgirpur marks the easternmost extent of the late phase expansion in western Uttar Pradesh."),
    ("The core Harappan region was characterized by heavy tropical monsoon forests.", False, "False. It was a semi-arid zone that relied on river inundation and seasonal alluvial floods."),
    ("Balakot in Balochistan was an inland administrative capital without access to the sea.", False, "False. Balakot was a coastal site famous for marine shell-working and fishing."),
    ("Sutkagendor lies on the border between Pakistan and Iran.", True, "True. It is located in Pakistani Makran on the edge of the Iranian frontier.")
]:
    s1_mastery_eng.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

# Fill Blank (8)
for q, ans, sol in [
    ("The northernmost boundary site of the Indus Valley Civilisation is __________.", "Manda", "Manda is located in Jammu and Kashmir."),
    ("The southernmost boundary site of the Indus Valley Civilisation is __________.", "Daimabad", "Daimabad is in Ahmednagar, Maharashtra."),
    ("The easternmost boundary site of the Indus Valley Civilisation is __________.", "Alamgirpur", "Alamgirpur is in Meerut, UP."),
    ("The westernmost boundary site of the Indus Valley Civilisation is __________.", "Sutkagendor", "Sutkagendor is in Makran, Balochistan."),
    ("Shortughai is situated in the modern nation of __________.", "Afghanistan", "Shortughai is in northern Afghanistan."),
    ("The dry river bed often identified with the ancient Sarasvati is the __________ channel.", "Ghaggar-Hakra", "The Ghaggar-Hakra river channel matches the description."),
    ("Sutkagendor is situated on the banks of the __________ River.", "Dasht", "Sutkagendor is on the Dasht River."),
    ("The alluvial plains of the Indus were replenished annually by silt deposits from the __________ floods.", "monsoon", "Monsoonal floods in the catchment areas fed the rivers annually.")
]:
    s1_mastery_eng.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

# Matching (3)
s1_mastery_eng.extend([
    {
        "type": "Match the Following",
        "q": "Match the geographical boundary sites of the Indus Civilisation with their respective card directions:",
        "items": [{"left": "I. Manda", "key": "A"}, {"left": "II. Daimabad", "key": "B"}, {"left": "III. Sutkagendor", "key": "C"}],
        "options": [{"val": "A", "text": "A. Northern Frontier"}, {"val": "B", "text": "B. Southern Frontier"}, {"val": "C", "text": "C. Western Frontier"}],
        "sol": "Manda is North, Daimabad is South, and Sutkagendor is West."
    },
    {
        "type": "Match the Following",
        "q": "Match the archaeological sites with their corresponding modern regions/provinces:",
        "items": [{"left": "I. Dholavira", "key": "A"}, {"left": "II. Rakhigarhi", "key": "B"}, {"left": "III. Shortughai", "key": "C"}],
        "options": [{"val": "A", "text": "A. Gujarat (Kutch)"}, {"val": "B", "text": "B. Haryana"}, {"val": "C", "text": "C. Afghanistan"}],
        "sol": "Dholavira is in Gujarat, Rakhigarhi in Haryana, and Shortughai in Afghanistan."
    },
    {
        "type": "Match the Following",
        "q": "Match the boundary sites with the rivers they are situated along:",
        "items": [{"left": "I. Alamgirpur", "key": "A"}, {"left": "II. Daimabad", "key": "B"}, {"left": "III. Sutkagendor", "key": "C"}],
        "options": [{"val": "A", "text": "A. Hindon River"}, {"val": "B", "text": "B. Pravara River"}, {"val": "C", "text": "C. Dasht River"}],
        "sol": "Alamgirpur is on the Hindon, Daimabad on the Pravara, and Sutkagendor on the Dasht."
    }
])

# One-Liner (8)
for q, sol in [
    ("What is the approximate total geographic area covered by the Indus Civilisation at its height?", "Around 1.3 to 1.5 million square kilometers, forming a huge triangular expanse."),
    ("Name the geographic pass that provided land trade routes between Balochistan and the Indus plains.", "The Bolan Pass."),
    ("Which modern Indian state has the highest count of Indus Valley sites discovered so far?", "Gujarat."),
    ("Name the coastal site near Karachi that is famous for its large shell-working industry.", "Balakot."),
    ("What was the primary type of soil in the Indus basins that sustained their intensive agricultural output?", "Fertile alluvial soil deposited by seasonal river floods."),
    ("Which mountain ranges define the western geographical boundary of the Indus core plains?", "The Kirthar and Sulaiman ranges."),
    ("Which site provides direct evidence of maritime trade links on the coastal Makran region?", "Sutkagendor."),
    ("What was the navigable channel through which Mesopotamians traded with Meluhha?", "The Persian Gulf / Arabian Sea.")
]:
    s1_mastery_eng.append({"type": "One-Liner", "q": q, "sol": sol})

# Assertion-Reason (8)
for q, ans, sol in [
    ("Assertion (A): The Indus Valley Civilisation expanded in a massive triangular layout.\\nReason (R): This pattern followed the ecological zones of the Indus basin and river deltas, expanding along trade networks.", 0, "Both statements are true and R explains A. The shape is a result of geographic and economic expansion."),
    ("Assertion (A): Shortughai in Afghanistan was established as a temporary wheat farming base.\\nReason (R): Shortughai gave direct access to the Badakhshan lapis lazuli mines and Central Asian metal networks.", 3, "A is false because Shortughai was a permanent trading post, not agricultural. R is true."),
    ("Assertion (A): The Ghaggar-Hakra river system is often linked with the historical Sarasvati river.\\nReason (R): Satellite imagery and ground studies confirm a dense network of ancient settlements along its dry channel.", 0, "Both are true and R explains why the Ghaggar-Hakra basin is associated with the core heartland."),
    ("Assertion (A): Daimabad marks the southernmost limit of the Harappan expansion.\\nReason (R): Harappans migrated southwards to Maharashtra during the Late phase, settling in the Godavari basin.", 0, "Both are true and R explains the Late Harappan southern shift."),
    ("Assertion (A): Sutkagendor was equipped with a massive brick-built dockyard.\\nReason (R): Sutkagendor was a fortified trade outpost built on a rocky cliff rather than an inland tidal basin.", 3, "Assertion is false: Sutkagendor did not have a dockyard like Lothal. Reason is true."),
    ("Assertion (A): The Indus Valley plain was prone to tectonic uplifts.\\nReason (R): Tectonic changes diverted rivers like the Yamuna and Sutlej, causing drying of the Ghaggar and flooding of the Indus.", 0, "Both are true and R explains the geographical impact of tectonic uplifts."),
    ("Assertion (A): Alamgirpur shows a complete lack of public brick-built street drains.\\nReason (R): Alamgirpur was a Late Harappan peripheral village where civic planning standards had degraded.", 0, "Both are true and R explains the decay in civic standards at the periphery."),
    ("Assertion (A): The core regions of the IVC were located in heavy tropical rainfall zones.\\nReason (R): Harappans relied on seasonal river inundation and mud embankments rather than rainfall for farming.", 3, "A is false because the core was semi-arid. R is true.")
]:
    s1_mastery_eng.append({"type": "Assertion-Reason", "q": q, "opts": ar_opts, "ans": ans, "sol": sol})

# Statement-Based (5)
for q, ans, sol in [
    ("Consider the following statements regarding the boundary outposts:\\n1. Manda in the north was situated on the Chenab River.\\n2. Daimabad in the south was situated on the Pravara River.\\nWhich of the statements given above is/are correct?", 2, "Both statements are correct."),
    ("Consider the following statements regarding the geography of Gujarat sites:\\n1. Lothal was located at the head of the Gulf of Khambhat on the Bhogavo River.\\n2. Dholavira was built in the salt flats of the Rann of Kutch on Khadir Bet island.\\nWhich of the statements given above is/are correct?", 2, "Both statements are correct. These represent two different maritime ecological settings."),
    ("Consider the following statements regarding the Cholistan desert:\\n1. It contains the highest concentration of Hakra and early Harappan settlements.\\n2. The Ghaggar-Hakra river system was completely dry throughout the Mature Harappan phase.\\nWhich of the statements given above is/are correct?", 0, "Statement 2 is incorrect. The river was active during the Mature phase and dried up later."),
    ("Consider the following statements regarding the climatic context of IVC:\\n1. The core Indus region received heavy monsoonal rain similar to the Ganga Valley.\\n2. The climate was semi-arid, requiring seasonal floodwater management for crops.\\nWhich of the statements given above is/are correct?", 1, "Only statement 2 is correct. The region was semi-arid."),
    ("Consider the following statements regarding the Shortughai outpost:\\n1. It is situated in northern Afghanistan near the Oxus (Amu Darya) River.\\n2. It was established primarily to control the export of copper from Khetri mines.\\nWhich of the statements given above is/are correct?", 0, "Statement 2 is incorrect. Khetri is in Rajasthan; Shortughai controlled lapis lazuli from Badakhshan.")
]:
    s1_mastery_eng.append({"type": "Statement-Based", "q": q, "opts": mcq_opts, "ans": ans, "sol": sol})

# Conceptual Qs (12)
for qtype, q, sol in [
    ("Why", "Why did the Harappans establish peripheral outposts like Shortughai and Sutkagendor?", "To secure strategic trade routes and monopolize rare raw materials: Shortughai for lapis lazuli/copper from Central Asia, and Sutkagendor to control sea trade with Mesopotamia."),
    ("Why", "Why is the Ghaggar-Hakra river valley called the heartland of the Indus Civilisation?", "Because over 60% of all discovered IVC sites lie along this dry basin, indicating it supported the largest agricultural and urban population density."),
    ("Why", "Why was the geographical location of Dholavira in the Rann of Kutch highly strategic?", "During the Bronze Age, the Rann was a navigable sea gulf. Dholavira acted as a massive island fortress controlling maritime trade coming from the Arabian Sea."),
    ("How", "How did river course migrations alter the geography of Harappan cities?", "Shifting rivers left cities stranded away from water or submerged them in floods, forcing populations to migrate and leading to de-urbanization."),
    ("How", "How did the geographical location of Sutkagendor aid maritime trade?", "It served as a protected coastal port and watering station on the Makran coast, acting as a bridge between the Indus valley and the Persian Gulf."),
    ("How", "How did the alluvial ecology of the Indus Basin shape the Harappan crop cycle?", "Annual river floods deposited fertile silt. Harappans sowed crops (wheat/barley) in winter as floodwaters receded and harvested them in spring without complex canals."),
    ("Case Study", "Case Study: The Shortughai Trade Outpost", "A Harappan settlement in northern Afghanistan. It shows classic Harappan bricks, pottery, and seals, proving the state established long-distance enclaves to control the lapis lazuli trade of Badakhshan."),
    ("Case Study", "Case Study: The Drying of the Ghaggar-Hakra River", "Tectonic shifts diverted the Sutlej into the Indus and the Yamuna into the Ganga. This cut off the water source of the Ghaggar-Hakra, turning it into a seasonal dry channel and leading to the abandonment of cities like Kalibangan."),
    ("Case Study", "Case Study: Daimabad Peripheral Expansion", "Daimabad in Maharashtra yields late Harappan pottery and a massive copper/bronze hoard. It demonstrates that as the core cities declined, populations migrated southwards, expanding the cultural footprint."),
    ("Teach the Concept", "Teach the Concept: The Harappan Geographical Quadrangle", "Teach the four boundary markers of the civilization at its peak: Manda (North, J&K), Daimabad (South, Maharashtra), Alamgirpur (East, UP), and Sutkagendor (West, Balochistan), covering 1.5 million sq km."),
    ("Teach the Concept", "Teach the Concept: Alluvial Floodplain Farming", "Explain that Harappan agriculture was not dependent on canal irrigation or heavy rainfall, but on exploiting the natural flood cycles of the Indus system, utilizing soft alluvial soil for easy plowing."),
    ("Teach the Concept", "Teach the Concept: Coastal Maritime Gateway Sites", "Explain how coastal sites like Lothal, Sutkagendor, Balakot, and Kuntasi formed a maritime network that supported fish exports, shell-craft production, and shipping links to Mesopotamia.")
]:
    s1_mastery_eng.append({"type": qtype, "q": q, "sol": sol})

# =========================================================================
# SECTION 2: MAJOR SETTLEMENT TYPES AND URBAN CENTERS (62 Qs)
# =========================================================================
s2_mastery_eng = []

# MCQs (5)
for q, opts, ans, sol in [
    ("Which of the following Mature Harappan cities is divided into three distinct parts: a Citadel, a Middle Town, and a Lower Town?", ["Harappa", "Mohenjo-daro", "Dholavira", "Kalibangan"], 2, "Dholavira is unique for its three-tier town planning, whereas most other cities have a two-tier division."),
    ("The famous artificial baked-brick dockyard connected to a river channel was discovered at which site?", ["Lothal", "Sutkagendor", "Balakot", "Kuntasi"], 0, "Lothal in Gujarat contains a massive baked-brick dockyard connected to a channel of the Bhogavo River."),
    ("Which of the following sites is famous for yielding a terracotta model of a plow, showing agricultural practices?", ["Kalibangan", "Banawali", "Rakhigarhi", "Lothal"], 1, "Banawali in Fatehabad district, Haryana, yielded a well-preserved terracotta model of a agricultural plow."),
    ("Which major Harappan industrial center shows a complete absence of a fortified administrative citadel?", ["Chanhudaro", "Mohenjo-daro", "Lothal", "Dholavira"], 0, "Chanhudaro in Sindh was a dedicated industrial town famous for craft and bead factories, and lacks a citadel."),
    ("Rakhigarhi, currently recognized as the largest geographic site of the Indus Valley Civilisation, is located in which state?", ["Punjab", "Rajasthan", "Gujarat", "Haryana"], 3, "Rakhigarhi is in Hisar district, Haryana, and covers over 350 hectares.")
]:
    s2_mastery_eng.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# Multi-Correct (5)
for q, opts, ans, sol in [
    ("Identify the architectural and archaeological discoveries associated with Dholavira: (Select all that apply)", ["Massive stone water reservoirs", "A signboard with ten large Indus script characters", "A three-tier town layout", "An artificial brick dockyard"], [0, 1, 2], "Dholavira has stone reservoirs, a ten-character signboard, and a three-tier layout. Lothal contains the dockyard."),
    ("Which of the following sites contain evidence of fire altars, indicating ritual activity? (Select all that apply)", ["Kalibangan", "Lothal", "Banawali", "Mohenjo-daro"], [0, 1, 2], "Fire altars have been found at Kalibangan, Lothal, and Banawali. They are absent at Mohenjo-daro."),
    ("Select the coastal ports and maritime centers of the Harappan civilization: (Select all that apply)", ["Lothal", "Kuntasi", "Sutkagendor", "Chanhudaro"], [0, 1, 2], "Lothal, Kuntasi, and Sutkagendor are coastal ports. Chanhudaro is an inland industrial site."),
    ("Which sites show evidence of pre-mature (Early Harappan) agricultural activities? (Select all that apply)", ["Kalibangan (ploughed field)", "Bhirrana (Hakra levels)", "Mehrgarh (Neolithic farming)", "Lothal (dockyard)"], [0, 1, 2], "Kalibangan, Bhirrana, and Mehrgarh have early farming levels. Lothal is a Mature/Late phase port city."),
    ("Identify the major public structures excavated at Mohenjo-daro: (Select all that apply)", ["The Great Bath", "The Great Granary", "Assembly Hall of columns", "A stone dockyard"], [0, 1, 2], "Mohenjo-daro contains the Great Bath, Great Granary, and Assembly Hall. Lothal contains the dockyard.")
]:
    s2_mastery_eng.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# True/False (8)
for q, ans, sol in [
    ("Mohenjo-daro literally means 'Mound of the Dead' in the Sindhi language.", True, "True. R.D. Banerji discovered the site under this local name."),
    ("Lothal's dockyard basin was constructed using sun-dried mud-bricks.", False, "False. It was built using high-quality baked bricks to withstand tidal water pressure."),
    ("Chanhudaro was a major administrative capital containing a large royal palace.", False, "False. It was a craft center with no citadel or palace structures."),
    ("Kalibangan is famous for yielding the earliest ploughed field in the subcontinent.", True, "True. The criss-cross ploughed field belongs to the pre-mature Early Harappan phase."),
    ("Banawali yielded a terracotta toy model of a plow.", True, "True. This discovery confirms that wooden plows were used for farming."),
    ("Dholavira's city walls were made entirely of mud-bricks without stone.", False, "False. Dholavira is famous for its extensive use of local stone in fortifications."),
    ("Rakhigarhi in Haryana has been declared the largest site of the Indus Valley Civilisation by area.", True, "True. Recent excavations show it is larger than Mohenjo-daro and Harappa."),
    ("All Harappan towns were divided into exactly two fortified sections.", False, "False. Dholavira is divided into three sections: Citadel, Middle Town, and Lower Town.")
]:
    s2_mastery_eng.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

# Fill Blank (8)
for q, ans, sol in [
    ("Mohenjo-daro is situated on the banks of the __________ River.", "Indus", "Mohenjo-daro lies in Sindh along the Indus River."),
    ("The largest site of the Indus Valley Civilisation by geographic area is __________.", "Rakhigarhi", "Rakhigarhi in Haryana is the largest site."),
    ("The Harappan city uniquely divided into three parts is __________.", "Dholavira", "Dholavira in Gujarat features three divisions."),
    ("A terracotta model of an agricultural plow was excavated at __________.", "Banawali", "Banawali yielded the clay plow model."),
    ("The port site of Lothal was excavated by the archaeologist __________.", "S.R. Rao", "S.R. Rao excavated Lothal in 1954."),
    ("Fire altars indicating ritual sacrifices have been found at Lothal and __________.", "Kalibangan", "Kalibangan has a row of seven fire altars."),
    ("Chanhudaro was a major manufacturing center for __________ beads.", "carnelian", "Carnelian beads were made in craft factories at Chanhudaro."),
    ("The city of Harappa is located on the banks of the __________ River.", "Ravi", "Harappa lies along the Ravi River in Punjab, Pakistan.")
]:
    s2_mastery_eng.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

# Matching (3)
s2_mastery_eng.extend([
    {
        "type": "Match the Following",
        "q": "Match the Indus Valley sites with their pioneer archaeological excavators:",
        "items": [{"left": "I. Harappa", "key": "A"}, {"left": "II. Mohenjo-daro", "key": "B"}, {"left": "III. Lothal", "key": "C"}],
        "options": [{"val": "A", "text": "A. Daya Ram Sahni"}, {"val": "B", "text": "B. R.D. Banerji"}, {"val": "C", "text": "C. S.R. Rao"}],
        "sol": "Harappa was excavated by Sahni, Mohenjo-daro by Banerji, and Lothal by Rao."
    },
    {
        "type": "Match the Following",
        "q": "Match the major Harappan towns with their unique architectural features/discoveries:",
        "items": [{"left": "I. Mohenjo-daro", "key": "A"}, {"left": "II. Dholavira", "key": "B"}, {"left": "III. Lothal", "key": "C"}],
        "options": [{"val": "A", "text": "A. The Great Bath"}, {"val": "B", "text": "B. Giant stone reservoirs and signboard"}, {"val": "C", "text": "C. Baked-brick dockyard"}],
        "sol": "Mohenjo-daro has the Great Bath, Dholavira has stone reservoirs, and Lothal has the dockyard."
    },
    {
        "type": "Match the Following",
        "q": "Match the Harappan settlements with the rivers they are situated along:",
        "items": [{"left": "I. Harappa", "key": "A"}, {"left": "II. Mohenjo-daro", "key": "B"}, {"left": "III. Lothal", "key": "C"}],
        "options": [{"val": "A", "text": "A. Ravi River"}, {"val": "B", "text": "B. Indus River"}, {"val": "C", "text": "C. Bhogavo River"}],
        "sol": "Harappa is on the Ravi, Mohenjo-daro on the Indus, and Lothal on the Bhogavo."
    }
])

# One-Liner (8)
for q, sol in [
    ("Which site is known as the industrial craft suburb of Mohenjo-daro due to its bead factories?", "Chanhudaro in Sindh."),
    ("Name the Harappan site where a wooden coffin burial (indicating international contacts) was found.", "Harappa (Cemetery R-37)."),
    ("Which site contains the earliest direct evidence of cotton cultivation in the ancient world?", "Mohenjo-daro (woven cotton scrap on a silver jar)."),
    ("In which modern Indian state is the massive site of Rakhigarhi located?", "Haryana (Hisar district)."),
    ("Name the port site that yielded copper oxhide ingots, showing trade connections with the Persian Gulf.", "Lothal."),
    ("Which site uniquely showed that almost every house had its own brick-lined water well?", "Mohenjo-daro."),
    ("What is the name of the river tributary along which Lothal is situated?", "The Bhogavo River (tributary of the Sabarmati)."),
    ("At which site in Gujarat were bones and skeletal remains of a horse reported?", "Surkotada.")
]:
    s2_mastery_eng.append({"type": "One-Liner", "q": q, "sol": sol})

# Assertion-Reason (8)
for q, ans, sol in [
    ("Assertion (A): Mohenjo-daro was rebuilt at least seven times on top of older ruins.\\nReason (R): The city was situated on the Indus floodplain and was repeatedly devastated by massive river floods.", 0, "Both A and R are true and R explains A. Silt deposits show repeated flood rebuilding cycles."),
    ("Assertion (A): Chanhudaro was a heavily fortified administrative city housing elite rulers.\\nReason (R): The site lacks a defensive wall or citadel and is packed with bead workshops and metal smelters.", 3, "A is false because Chanhudaro was an unfortified industrial suburb. R is true."),
    ("Assertion (A): Dholavira utilized massive stone masonry for its fortification walls.\\nReason (R): Local sandstone quarries in Kutch provided abundant stone, whereas brick-clay was scarce.", 0, "Both A and R are true and R explains A. Geography influenced Dholavira's stone architecture."),
    ("Assertion (A): Lothal served as a major maritime trading hub for the Harappan empire.\\nReason (R): Archaeologists excavated a massive baked-brick basin linked to a river channel and Persian Gulf button seals at Lothal.", 0, "Both are true and R explains A. The dockyard and seals prove its international port status."),
    ("Assertion (A): Kalibangan houses were constructed using sun-dried mud bricks instead of baked bricks.\\nReason (R): Kalibangan lacked easy access to dense forests to bake bricks, relying on sun-drying.", 0, "Both are true and R explains why mud-bricks dominated at Kalibangan."),
    ("Assertion (A): Banawali represents a degenerate phase of mature town planning.\\nReason (R): Streets at Banawali did not follow a strict grid pattern and radial lanes were present.", 0, "Both are true and R explains why Banawali is considered an exception to the grid layout."),
    ("Assertion (A): Rakhigarhi is recognized as the largest Indus Valley site.\\nReason (R): Excavations revealed a cemetery and nine massive mounds covering over 350 hectares.", 0, "Both are true and R explains why Rakhigarhi is the largest site."),
    ("Assertion (A): Surkotada was fortified with a stone-reinforced gateway.\\nReason (R): The gateway and stone walls provided security against cattle raids and external attacks in peripheral Gujarat.", 0, "Both are true and R explains the function of Surkotada's stone gateway.")
]:
    s2_mastery_eng.append({"type": "Assertion-Reason", "q": q, "opts": ar_opts, "ans": ans, "sol": sol})

# Statement-Based (5)
for q, ans, sol in [
    ("Consider the following statements regarding the Lothal dockyard:\\n1. It was constructed of high-quality baked bricks to resist water pressure.\\n2. It was connected to the Bhogavo River, which allowed ships to enter at high tide.\\nWhich of the statements given above is/are correct?", 2, "Both statements are correct."),
    ("Consider the following statements regarding Dholavira:\\n1. The city is divided into three sections: Citadel, Middle Town, and Lower Town.\\n2. It has yielded a signboard containing ten large gypsum characters in the Indus script.\\nWhich of the statements given above is/are correct?", 2, "Both statements are correct."),
    ("Consider the following statements regarding Mohenjo-daro:\\n1. The Great Bath was lined with a layer of natural tar (bitumen) to prevent leakage.\\n2. The Great Granary was built on a high brick platform to protect grain from dampness and floods.\\nWhich of the statements given above is/are correct?", 2, "Both statements are correct."),
    ("Consider the following statements regarding Kalibangan:\\n1. A row of seven fire altars was found on a platform in the citadel.\\n2. Skeletons of a male and female buried together (double burial) were excavated here.\\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect because the double burial was found at Lothal, not Kalibangan."),
    ("Consider the following statements regarding Chanhudaro:\\n1. It was a major industrial center specializing in bead-making, seal-cutting, and shell-working.\\n2. It is the only Harappan city that has yielded a brick with the paw print of a dog chasing a cat.\\nWhich of the statements given above is/are correct?", 2, "Both statements are correct. The paw print brick is a famous discovery from Chanhudaro.")
]:
    s2_mastery_eng.append({"type": "Statement-Based", "q": q, "opts": mcq_opts, "ans": ans, "sol": sol})

# Conceptual Qs (12)
for qtype, q, sol in [
    ("Why", "Why did Mohenjo-daro houses feature an abundance of water wells?", "Almost every house had its own brick well, providing fresh water and maintaining high sanitation standards, which was unique in the ancient world."),
    ("Why", "Why did Chanhudaro lack defensive fortifications or a citadel structure?", "Because it was a dedicated industrial and craft center, not an administrative or political seat, focusing entirely on manufacture."),
    ("Why", "Why did Dholavira implement a three-tier town layout?", "It represents a stratified social hierarchy: the elite rulers in the Citadel, merchants/middle class in the Middle Town, and artisans/laborers in the Lower Town."),
    ("How", "How did Lothal's dockyard operate with tidal water flows?", "It used a sluice gate mechanism to trap water in the basin at high tide, allowing ships to float and remain stable for loading/unloading even during low tide."),
    ("How", "How did the Great Granary at Mohenjo-daro keep stored grain fresh?", "Built on a high platform to prevent flood damage, it featured air channels (ducts) that allowed cool air to circulate, keeping the grain dry and preventing rot."),
    ("How", "How did Kalibangan's pre-mature agricultural layout optimize double-cropping?", "The furrows ran in two perpendicular directions: one set spaced closely (30cm) for small crops (mustard) and another spaced widely (1.9m) for taller crops (chickpeas), preventing shadow competition."),
    ("Case Study", "Case Study: The Lothal Dockyard", "A baked-brick basin measuring 218m x 37m. It shows advanced understanding of tidal hydrodynamics, enabling ships to dock from the Gulf of Khambhat via a river channel."),
    ("Case Study", "Case Study: Dholavira's Reservoir Network", "Dholavira constructed 16 stone-cut reservoirs that collected rainwater from seasonal streams. This system sustained a large population in an arid region with no perennial rivers."),
    ("Case Study", "Case Study: The Craft Workshops of Chanhudaro", "Excavations revealed bead-making factories with drills, furnaces, and raw materials (carnelian, jasper). It confirms Chanhudaro was a highly specialized manufacturing hub."),
    ("Teach the Concept", "Teach the Concept: The Citadel vs Lower Town", "Explain that most Harappan cities had a dual layout: the western, raised Citadel (administrative offices and public halls) and the eastern, larger Lower Town (residential houses for the public)."),
    ("Teach the Concept", "Teach the Concept: The Granary and Food Security", "Explain how the state controlled food security by storing surplus grain in large public granaries (like those at Harappa and Mohenjo-daro) to survive famines and floods."),
    ("Teach the Concept", "Teach the Concept: The Three-Tier Town Layout of Dholavira", "Highlight how Dholavira broke the standard dual layout by adding a 'Middle Town' between the Citadel and Lower Town, representing a unique social structure and civic complexity.")
]:
    s2_mastery_eng.append({"type": qtype, "q": q, "sol": sol})


# =========================================================================
# SECTION 3: KEY ARCHAEOLOGICAL FINDINGS, MATERIALS, AND ARTIFACTS (62 Qs)
# =========================================================================
s3_mastery_eng = []

# MCQs (5)
for q, opts, ans, sol in [
    ("What soft soapstone material was primarily used to manufacture Harappan seals?", ["Chert", "Steatite", "Faience", "Copper"], 1, "Most Harappan seals were carved from steatite (soapstone), which was easy to engrave and then baked to harden."),
    ("The famous bronze Dancing Girl statue was cast using which technical metallurgical process?", ["Sand casting", "Lost-wax casting (Cire Perdue)", "Cold hammering", "Sheet metal joining"], 1, "The Dancing Girl was made using the lost-wax casting technique, showing advanced metallurgy."),
    ("Which of the following materials was primarily used to make the highly standardized Harappan cubical weights?", ["Steatite", "Chert", "Lapis Lazuli", "Alabaster"], 1, "Standardized cubical weights were made from a hard, fine-grained stone called chert."),
    ("The famous bearded 'Priest-King' stone statue was excavated at which Mature Harappan site?", ["Harappa", "Mohenjo-daro", "Lothal", "Dholavira"], 1, "The steatite Priest-King statue was discovered at Mohenjo-daro."),
    ("Which site yielded a unique clay pot featuring a painting of a crow and a fox, resembling the Panchatantra fable?", ["Kalibangan", "Lothal", "Banawali", "Rakhigarhi"], 1, "Lothal yielded a painted jar showing a crow with a fish and a fox, often compared to the 'Cunning Crow' fable.")
]:
    s3_mastery_eng.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# Multi-Correct (5)
for q, opts, ans, sol in [
    ("Identify the animals depicted around the central yogic figure on the Pashupati Seal: (Select all that apply)", ["Elephant and Tiger", "Rhinoceros and Buffalo", "Two Deer (at the feet)", "Horse and Lion"], [0, 1, 2], "The Pashupati seal depicts an elephant, tiger, rhino, buffalo, and two deer. The horse and lion are absent."),
    ("Which metals were known and used by Indus Valley metalworkers? (Select all that apply)", ["Copper", "Bronze", "Gold", "Iron"], [0, 1, 2], "Copper, bronze, gold, and silver were used. Iron was completely unknown to the Harappans."),
    ("Select the burial types identified in Mature Harappan cemeteries: (Select all that apply)", ["Wooden coffin burials", "Pot/Urn burials", "Brick-chambered burials", "Mummified burials"], [0, 1, 2], "Harappans used coffin, pot, and brick-chamber burials. Mummification was not practiced."),
    ("Which of the following items are associated with Mohenjo-daro? (Select all that apply)", ["The Bronze Dancing Girl", "The Steatite Priest-King", "Woven cotton fragments", "A red sandstone torso of a male dancer"], [0, 1, 2], "Dancing Girl, Priest-King, and cotton are from Mohenjo-daro. The red sandstone male torso is from Harappa."),
    ("Identify the primary raw materials imported for craft production: (Select all that apply)", ["Lapis Lazuli from Badakhshan", "Copper from Khetri mines", "Carnelian from Gujarat", "Iron from Central India"], [0, 1, 2], "Lapis Lazuli, Copper, and Carnelian were imported/mined. Iron was unknown.")
]:
    s3_mastery_eng.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# True/False (8)
for q, ans, sol in [
    ("The Pashupati seal depicts a three-faced seated deity wearing a horned headdress.", True, "True. The figure sits in a yogic yogasana posture with arms covered in bangles."),
    ("The bronze Dancing Girl is depicted wearing a large number of bangles on her left arm.", True, "True. She wears 24 to 25 bangles on her left arm, holding it on her thigh."),
    ("Harappan pottery was mostly plain, handmade grey ware with no paint.", False, "False. Most pottery was wheel-made Red and Black ware, painted with black designs on red slips."),
    ("Traces of woven cotton cloth were discovered wrapped around a silver jar at Mohenjo-daro.", True, "True. This provides the oldest evidence of cotton use in the ancient world."),
    ("Harappan weights were spherical stone balls with no uniform values.", False, "False. They were highly standardized cubical chert blocks following binary and decimal systems."),
    ("The Priest-King statue is made of steatite and wears a shawl decorated with trefoil patterns.", True, "True. The trefoil patterns indicate contacts with Mesopotamian royal symbols."),
    ("Iron weapons and tools were excavated from the Cemetery R-37 at Harappa.", False, "False. Harappans were in the Bronze Age and had no knowledge of iron."),
    ("The double burial at Lothal contains the skeletons of a male and female buried in the same grave.", True, "True. This unique joint burial is found only at Lothal in Gujarat.")
]:
    s3_mastery_eng.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

# Fill Blank (8)
for q, ans, sol in [
    ("The bearded Priest-King stone statue was discovered at the site of __________.", "Mohenjo-daro", "Mohenjo-daro yielded this steatite sculpture."),
    ("The metallurgical process used to cast the bronze Dancing Girl is called __________ casting.", "lost-wax", "Lost-wax casting (cire perdue) was used."),
    ("Most Harappan seals feature an engraving of a mythical one-horned beast called the __________.", "unicorn", "The unicorn is the most common animal on seals."),
    ("The primary hard stone used to make Harappan cubical weights is __________.", "chert", "Chert was used for its durability and consistency."),
    ("Harappan painted pottery is scientifically classified as __________ and Black Ware.", "Red", "Red and Black Ware is the characteristic style."),
    ("A joint grave containing a double burial was discovered at the port site of __________.", "Lothal", "Lothal has double burials in its cemetery."),
    ("The Priest-King shawl features a repeating decorative motif known as the __________ pattern.", "trefoil", "The trefoil pattern resembles clover leaves."),
    ("Engraved seals were made of a soft soapstone called __________.", "steatite", "Steatite was carved and heated to form durable seals.")
]:
    s3_mastery_eng.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

# Matching (3)
s3_mastery_eng.extend([
    {
        "type": "Match the Following",
        "q": "Match the famous archaeological artifacts with their primary manufacturing materials:",
        "items": [{"left": "I. Dancing Girl", "key": "A"}, {"left": "II. Priest-King", "key": "B"}, {"left": "III. Cubical Weights", "key": "C"}],
        "options": [{"val": "A", "text": "A. Bronze (Metal Alloy)"}, {"val": "B", "text": "B. Steatite (Soapstone)"}, {"val": "C", "text": "C. Chert (Hard Stone)"}],
        "sol": "Dancing Girl is bronze, Priest-King is steatite, and weights are chert."
    },
    {
        "type": "Match the Following",
        "q": "Match the unique burial types with their corresponding Harappan sites:",
        "items": [{"left": "I. Double Burial", "key": "A"}, {"left": "II. Wooden Coffin Burial", "key": "B"}, {"left": "III. Pot Burial", "key": "C"}],
        "options": [{"val": "A", "text": "A. Lothal"}, {"val": "B", "text": "B. Harappa (Cemetery R-37)"}, {"val": "C", "text": "C. Kalibangan"}],
        "sol": "Double burial is from Lothal, coffin burial from Harappa, and pot burial from Kalibangan."
    },
    {
        "type": "Match the Following",
        "q": "Match the animals depicted on Harappan seals with their academic interpretations:",
        "items": [{"left": "I. Pashupati figure", "key": "A"}, {"left": "II. Unicorn figure", "key": "B"}, {"left": "III. Humped Bull", "key": "C"}],
        "options": [{"val": "A", "text": "A. Proto-Shiva / Lord of Animals"}, {"val": "B", "text": "B. Mythical merchant clan symbol"}, {"val": "C", "text": "C. Sacred zebu / strength symbol"}],
        "sol": "Pashupati is Proto-Shiva, unicorn is merchant symbol, and bull represents strength."
    }
])

# One-Liner (8)
for q, sol in [
    ("What is the exact height of the famous bronze Dancing Girl statue?", "10.5 centimeters."),
    ("Which site yielded a red sandstone sculpture of a male dancer with twisting torso?", "Harappa."),
    ("What characteristic color is the glazed surface of Harappan faience ornaments?", "Greenish-blue or turquoise."),
    ("Name the animal painted on a Lothal pot that resembles the Panchatantra fox fable.", "A crow and a fox."),
    ("What term is used to describe the yet-undeciphered script carved on Harappan seals?", "Indus Script (written in Boustrophedon style)."),
    ("What type of drills were used in bead-making workshops at Chanhudaro and Lothal?", "Specialized chert or bronze drills."),
    ("Which site in Maharashtra yielded a hoard of solid copper figures of animals?", "Daimabad."),
    ("What are the clay toys and mother goddess figures found at Harappan sites called?", "Terracotta figurines.")
]:
    s3_mastery_eng.append({"type": "One-Liner", "q": q, "sol": sol})

# Assertion-Reason (8)
for q, ans, sol in [
    ("Assertion (A): Steatite was the most popular material for seal carving.\\nReason (R): Steatite is a soft soapstone that allows fine engraving and hardens when fired.", 0, "Both A and R are true and R explains A. Steatite's properties made it ideal for seal production."),
    ("Assertion (A): The Dancing Girl is depicted as an active cultural figure.\\nReason (R): She stands in the tribhanga dance pose with her hand on her hip and wear bangles.", 0, "Both A and R are true and R explains her representation as a dancer."),
    ("Assertion (A): The Harappans traded extensively for lapis lazuli beads.\\nReason (R): Lapis lazuli was imported from Badakhshan to manufacture luxury items for elites.", 0, "Both are true and R explains the trade dynamics of lapis lazuli."),
    ("Assertion (A): Cotton textiles were exported to Sumerian markets.\\nReason (R): Woven cotton fragments were found preserved on a silver jar at Mohenjo-daro.", 1, "Both statements are true but R does not explain why it was exported; it only proves preservation."),
    ("Assertion (A): Iron implements were placed in Cemetery R-37 burials.\\nReason (R): The Harappan culture was a Bronze Age society that had no knowledge of iron metallurgy.", 3, "Assertion is false: iron was absent. Reason is true."),
    ("Assertion (A): Faience ornaments were considered high-status items.\\nReason (R): Faience was made of ground sand and glaze, requiring complex kiln firing that was difficult to master.", 0, "Both are true and R explains why faience was considered a luxury ornament."),
    ("Assertion (A): The Pashupati seal is often linked to the origins of Shiva worship.\\nReason (R): The seated figure wears a horned crown, sits in a yogic posture, and is surrounded by wild animals.", 0, "Both are true and R explains the Pashupati-Shiva connection."),
    ("Assertion (A): The double burial at Lothal indicates Sati practice.\\nReason (R): Joint burials can occur due to epidemics or natural deaths, and there is no proof of immolation.", 3, "A is false because Sati is not proven. R is true.")
]:
    s3_mastery_eng.append({"type": "Assertion-Reason", "q": q, "opts": ar_opts, "ans": ans, "sol": sol})

# Statement-Based (5)
for q, ans, sol in [
    ("Consider the following statements regarding Harappan seals:\\n1. Most seals are square and contain short inscriptions alongside animal carvings.\\n2. Seals were made of steatite, terracotta, and sometimes copper.\\nWhich of the statements given above is/are correct?", 2, "Both statements are correct."),
    ("Consider the following statements regarding the Dancing Girl:\\n1. It is a solid bronze casting made using the lost-wax process.\\n2. She is shown completely naked except for a necklace and bangles.\\nWhich of the statements given above is/are correct?", 2, "Both statements are correct."),
    ("Consider the following statements regarding Harappan pottery:\\n1. The pottery was primarily black-on-red painted ware.\\n2. The designs painted on the pottery include geometric circles, pipal leaves, and fish scales.\\nWhich of the statements given above is/are correct?", 2, "Both statements are correct. These motifs are characteristic of Harappan ceramics."),
    ("Consider the following statements regarding burials:\\n1. Cemetery R-37 at Harappa contains burials where bodies were placed inside wooden coffins.\\n2. Skeletons were buried with pottery and personal ornaments, indicating a belief in life after death.\\nWhich of the statements given above is/are correct?", 2, "Both statements are correct."),
    ("Consider the following statements regarding the Priest-King:\\n1. The statue is made of steatite and shows a draped shawl with trefoil patterns.\\n2. The eyes are elongated and were originally inlaid with shell or stone.\\nWhich of the statements given above is/are correct?", 2, "Both statements are correct. Trefoil pattern shawl and shell-inlaid eyes are key features of this statue.")
]:
    s3_mastery_eng.append({"type": "Statement-Based", "q": q, "opts": mcq_opts, "ans": ans, "sol": sol})

# Conceptual Qs (12)
for qtype, q, sol in [
    ("Why", "Why did the Harappans paint animal and floral motifs on their pottery?", "To express their naturalistic religious beliefs, utilizing symbols like the pipal leaf, zebu bull, and fish scales for ritual and domestic purposes."),
    ("Why", "Why was steatite the preferred material for seal manufacturing?", "Because it is soft soapstone that can be easily carved with fine steel-like tools and then baked to trigger a phase change into hard steatite."),
    ("Why", "Why did Cemetery R-37 burials contain extensive pottery vessels?", "They placed vessels containing food and water with the deceased, showing their belief in an afterlife where the soul needed nourishment."),
    ("How", "How did lost-wax casting work in the Harappan bronze industry?", "Artisans modeled a figure in wax, coated it in clay, baked it to melt and drain the wax out, and poured molten bronze into the hollow clay mold."),
    ("How", "How did the cubical chert weights facilitate commercial integration?", "By providing highly standardized, fraud-resistant measures across all cities, supporting trade trust from Gujarat to Punjab."),
    ("How", "How does the Priest-King's trefoil shawl pattern indicate international connections?", "The trefoil pattern is also found in Mesopotamian and Egyptian royal art, representing a shared elite ideological symbol of the Bronze Age."),
    ("Case Study", "Case Study: The Pashupati Seal Iconography", "A steatite seal from Mohenjo-daro depicting a seated deity in yogic pose. It is surrounded by an elephant, tiger, rhino, buffalo, and two deer, representing Lord of Animals."),
    ("Case Study", "Case Study: The Daimabad Copper Hoard", "A cache of solid copper sculptures (chariot, bull, elephant, rhino) weighing over 60 kg, showing that metallurgy survived into the peripheral Late phase."),
    ("Case Study", "Case Study: Cemetery R-37 Burials at Harappa", "Excavations revealed bodies laid in north-south orientation with pottery. One burial had a wooden coffin of cedar, showing trade links with the Himalayas."),
    ("Teach the Concept", "Teach the Concept: The Lost-Wax Method", "Explain the step-by-step process of lost-wax casting (wax model, clay layer, heating, draining, metal pouring, breaking clay mold) used to make the Dancing Girl."),
    ("Teach the Concept", "Teach the Concept: Harappan Faience Production", "Explain how faience was made from crushed quartz/sand mixed with color glaze, then fired to create glassy, turquoise beads, representing a luxury industry."),
    ("Teach the Concept", "Teach the Concept: The Cubical Chert Weights System", "Highlight how Harappan weights followed a binary system (1, 2, 4, 8, 16, 32...) for lighter weights and a decimal system for higher weights, indicating strict trade standards.")
]:
    s3_mastery_eng.append({"type": qtype, "q": q, "sol": sol})


# =========================================================================
# PRACTICE QUESTIONS (50 Qs) - UPSC PRELIMS MULTI-STATEMENT STYLE
# =========================================================================

practice_data_eng = [
    (
        "Consider the following statements regarding the boundary markers of the Indus Valley Civilisation:\n1. Manda, the northernmost boundary, is situated along the Jhelum River.\n2. Daimabad, the southernmost limit, is located on the Pravara River, a tributary of the Godavari.\n3. Sutkagendor, marking the western frontier, lies along the Dasht River.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        1,
        "Statement 1 is incorrect: Manda is situated on the Chenab River, not the Jhelum. Statements 2 and 3 are correct."
    ),
    (
        "Consider the following statements regarding the geographical extent of the Harappan Culture:\n1. The civilization covered a massive triangular area of over 1 million square kilometers.\n2. The geographical expanse of the Harappan empire was larger than contemporary Egypt and Mesopotamia combined.\n3. The easternmost limit is represented by Alamgirpur in Meerut along the Yamuna River itself.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "2 only", "3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: Alamgirpur is situated along the Hindon River, which is a tributary of the Yamuna, not the Yamuna River itself."
    ),
    (
        "Consider the following statements regarding the environmental and agricultural settings of the Indus Civilisation:\n1. The core region was characterized by heavy monsoonal tropical rainforests.\n2. Harappan agriculture relied heavily on canal network systems derived from the Indus.\n3. Winter sowing of crops like wheat and barley relied on seasonal alluvial soil replenished by annual floods.\nWhich of the statements given above is/are correct?",
        ["1 and 3 only", "3 only", "2 and 3 only", "1, 2 and 3"],
        1,
        "Statements 1 and 2 are incorrect: the core region was semi-arid, not a tropical rainforest, and canal irrigation was extremely rare (they relied on natural river inundations). Statement 3 is correct."
    ),
    (
        "With reference to the geographical outpost of Shortughai, consider the following statements:\n1. It was a mature Harappan trading enclave established in northern Afghanistan.\n2. It is situated along the Oxus (Amu Darya) River.\n3. Its primary strategic function was to secure direct access to the Khetri copper mines.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: Shortughai was established near the Badakhshan mines to secure lapis lazuli and Central Asian metals; the Khetri mines are in Rajasthan, far from Afghanistan."
    ),
    (
        "Consider the following statements regarding the Ghaggar-Hakra river valley:\n1. Over 60% of all discovered Indus Valley sites are concentrated in this dry basin.\n2. In cuneiform records, the river Ghaggar-Hakra is referred to as 'Meluhha'.\n3. The drying of this river channel is linked to tectonic shifts that diverted its water tributaries.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        2,
        "Statements 1 and 3 are correct. Statement 2 is incorrect: Meluhha was the Mesopotamian name for the entire Indus valley region, not specifically the Ghaggar-Hakra River."
    ),
    (
        "Consider the following statements regarding Lothal:\n1. It contains a massive artificial baked-brick basin identified as a tidal dockyard.\n2. It is situated at the head of the Gulf of Khambhat on the Bhogavo River, a Sabarmati tributary.\n3. A unique double burial containing a male and a female skeleton was excavated at its cemetery.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All three statements are correct, reflecting key archaeological findings at the port city of Lothal."
    ),
    (
        "With reference to the water management system of Dholavira, consider the following statements:\n1. The city is famous for its massive stone-cut water reservoirs and check dams.\n2. Unlike other Harappan cities, it relied completely on a system of private household wells rather than public reservoirs.\n3. The reservoirs collected rainwater channeled from seasonal streams like the Manhar and Mansar.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        2,
        "Statements 1 and 3 are correct. Statement 2 is incorrect: Dholavira relied on monumental public reservoirs and dams to collect runoff water in an arid environment; private wells were scarce compared to Mohenjo-daro."
    ),
    (
        "Consider the following statements regarding the town planning of Dholavira:\n1. Unlike the standard two-tier division of Harappan cities, Dholavira is divided into three fortified sections: Citadel, Middle Town, and Lower Town.\n2. The fortifications and structures at Dholavira are characterized by extensive stone masonry.\n3. Dholavira has yielded a unique signboard containing ten large gypsum characters in the Indus script.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All three statements are correct and represent Dholavira's unique architectural and scripts findings."
    ),
    (
        "Consider the following statements regarding Chanhudaro:\n1. It was an unfortified industrial town specializing in bead-making, seal-cutting, and shell-working.\n2. It is the only major Harappan city that completely lacks a raised citadel structure.\n3. A brick showing the paw print of a dog chasing a cat was excavated here.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All statements are correct. Chanhudaro was a pure craft suburb without administrative fortifications."
    ),
    (
        "With reference to the archaeological site of Rakhigarhi, consider the following statements:\n1. It is currently recognized as the largest geographic site of the Indus Valley Civilisation, covering over 350 hectares.\n2. It is situated in the Hisar district of Haryana in the dry Ghaggar river basin.\n3. Excavations at Rakhigarhi have yielded no signs of a cemetery or skeletal remains.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "2 and 3 only", "1 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: Rakhigarhi has yielded a significant Harappan cemetery with several burials and skeletal remains that have been used for DNA studies."
    ),
    (
        "Consider the following statements regarding Kalibangan:\n1. It has yielded a pre-mature Early Harappan agricultural field showing criss-cross ploughed furrows.\n2. The layout of the ploughed field indicates that two different crops were grown together (double-cropping).\n3. It is located on the dry bed of the Ghaggar-Hakra River in Rajasthan.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All three statements are correct. The criss-cross plow pattern is the earliest evidence of double-cropping in the world."
    ),
    (
        "With reference to Banawali, consider the following statements:\n1. It yielded a well-preserved terracotta toy model of an agricultural plow.\n2. It represents a strict adherence to the grid-iron town planning with no exceptions.\n3. It is situated in the Fatehabad district of Haryana.\nWhich of the statements given above is/are correct?",
        ["1 and 3 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 3 are correct. Statement 2 is incorrect: Banawali is famous for being an exception to the grid town planning, featuring radial streets and a lack of systematic grid layout."
    ),
    (
        "Consider the following statements regarding the Great Bath of Mohenjo-daro:\n1. The tank was made water-tight using a layer of natural bitumen (tar) between bricks.\n2. It is situated in the eastern Lower Town section of the city.\n3. It was surrounded by changing rooms and is believed to have been used for ritual purification.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        2,
        "Statements 1 and 3 are correct. Statement 2 is incorrect: the Great Bath is located in the Citadel (administrative/religious) section of the city, not the Lower Town."
    ),
    (
        "Consider the following statements regarding the storage of grain in Harappan cities:\n1. Large granaries built on raised platforms have been excavated at Mohenjo-daro and Harappa.\n2. The Harappan granaries featured air ducts (circulation channels) to prevent dampness and grain rot.\n3. Sourcing and distribution of grains from these granaries indicate state-controlled food security.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All three statements are correct, showing the complex administrative organization of the Harappan state."
    ),
    (
        "With reference to the civic sanitation of Mohenjo-daro, consider the following statements:\n1. Unlike other contemporary civilizations, almost every house had its own private brick well.\n2. Household drains connected to covered main street drains equipped with inspection manholes.\n3. All street drains were left open to direct sunlight for natural sterilization.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "2 and 3 only", "1 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: street drains were systematically covered with loose brick slabs or stone blocks, which could be removed for cleaning."
    ),
    (
        "Consider the following statements regarding the presence of horses in the Indus Civilisation:\n1. Surkotada in Gujarat is the only site where skeletal remains of a horse have been reported.\n2. The horse played a major role in mature Harappan agriculture and pulling heavy vehicles.\nWhich of the statements given above is/are correct?",
        ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        0,
        "Statement 1 is correct (though horse bones presence is debated among scholars). Statement 2 is incorrect: the primary draught animal was the bull; horse played no role in agriculture and was not domesticated."
    ),
    (
        "With reference to Balakot, consider the following statements:\n1. It is a coastal site situated near Karachi, Pakistani Balochistan.\n2. It was a major shell-working craft center specializing in shell bangles and beads.\n3. Balakot completely lacked any access to marine resource trade.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: Balakot relied heavily on coastal marine shell resources for both local crafts and export trade."
    ),
    (
        "Consider the following statements regarding Sutkagendor:\n1. It served as a protected coastal port and watering station on the Makran coast near Iran.\n2. It shows direct archaeological evidence of sea trade links with Mesopotamia.\n3. It featured a massive baked-brick tidal dockyard similar to the one at Lothal.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: Sutkagendor is a fortified outpost built on a rocky cliff; it did not have a dockyard like Lothal."
    ),
    (
        "Consider the following statements regarding Kuntasi:\n1. It was a fortified port and shell-working craft center situated in Gujarat.\n2. It acted as a coastal gateway that monitored trade entering the Gulf of Kutch.\n3. Unlike Lothal, it was purely a residential town with no manufacturing workshops.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: Kuntasi had active shell craft workshops and functioned as a fortified manufacturing-cum-trading base."
    ),
    (
        "Consider the following statements regarding the Daimabad Bronzes:\n1. A hoard of four solid copper-bronze animal and chariot sculptures was discovered at Daimabad.\n2. The sculptures include a chariot pulled by bulls, an elephant, a rhinoceros, and a buffalo.\n3. This hoard shows that metallurgy survived into the peripheral Late phase in Maharashtra.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All three statements are correct and represent the significance of the Daimabad copper hoard."
    ),
    (
        "With reference to the pre-mature site of Kot Diji, consider the following statements:\n1. It is situated on the left bank of the Indus River in Sindh.\n2. A thick layer of ash and charcoal separates the Early Harappan level from the Mature Harappan phase, indicating destruction by fire.\n3. Kot Diji pottery is plain and lacks any painted motifs like horned deities.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "2 only", "1 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: Kot Diji pottery is famous for its painted motifs, particularly the horned deity design."
    ),
    (
        "Consider the following statements regarding Harappan burials:\n1. Skeletons were typically buried in a north-south orientation with pottery and ornaments.\n2. Sarcophagus burials made of fired clay were the standard across all cities.\n3. Cemetery R-37 at Harappa contains unique burials where bodies were placed inside wooden coffins of cedar.\nWhich of the statements given above are correct?",
        ["1 and 3 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 3 are correct. Statement 2 is incorrect: simple earth graves (pit burials) were the standard; clay sarcophagi were extremely rare exceptions."
    ),
    (
        "Consider the following statements regarding joint burials:\n1. Lothal is the only site where skeletons of a male and a female were buried together in a single grave.\n2. These double burials provide absolute, uncontested proof of the prevalence of Sati.\nWhich of the statements given above is/are correct?",
        ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        0,
        "Statement 1 is correct. Statement 2 is incorrect: scholars suggest joint burials can occur due to sudden deaths, epidemics, or natural occurrences; there is no proof of self-immolation or Sati."
    ),
    (
        "With reference to fire altars in Harappan sites, consider the following statements:\n1. A row of seven fire altars built on mud-brick platforms was discovered at Kalibangan.\n2. Evidence of fire altars has also been found at Lothal and Banawali.\n3. Fire altars were a standard feature found in the citadels of Harappa and Mohenjo-daro.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: fire altars are completely absent at Harappa and Mohenjo-daro; they are restricted to Rajasthan, Gujarat, and Haryana."
    ),
    (
        "Consider the following statements regarding Harappan seals:\n1. They were primarily manufactured from soft steatite (soapstone) and then fired to harden.\n2. Most seals are square or rectangular and feature a brief inscription along with animal carvings.\n3. Seals were used by administrators to seal doors of granaries, but never to stamp trade goods.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: the primary function of seals was to stamp clay labels on merchant shipments to verify ownership and prevent tampering during transit."
    ),
    (
        "With reference to the Pashupati Seal, consider the following statements:\n1. It depicts a seated male deity in a yogic posture, wearing a horned headdress.\n2. The figure is surrounded by five animals: an elephant, a tiger, a rhinoceros, a buffalo, and two deer at his feet.\n3. Sir John Marshall identified this figure as 'Proto-Shiva'.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All three statements are correct and accurately detail the Pashupati seal iconography."
    ),
    (
        "Consider the following statements regarding the unicorn motif on Harappan seals:\n1. The mythical one-horned unicorn is the most frequently depicted animal on mature seals.\n2. It is often carved alongside a 'standard' or 'incense burner' object.\n3. Academic consensus suggests the unicorn represents a royal seal of the emperor.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "2 only", "1 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: there is no consensus on an emperor; scholars suggest the unicorn represented a dominant merchant guild or clan."
    ),
    (
        "Consider the following statements regarding the bronze Dancing Girl statue:\n1. It is a solid bronze casting made using the lost-wax (cire perdue) technique.\n2. The girl is depicted wearing a large number of bangles on her left arm.\n3. She stands in a rigid, vertical stance with no movement in her joints.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: she stands in a dynamic 'tribhanga' dance posture with her right hand on her hip, showing physical realism."
    ),
    (
        "With reference to the steatite Priest-King statue, consider the following statements:\n1. It depicts a bearded figure draped in a shawl decorated with trefoil patterns.\n2. The eyes are elongated and were originally inlaid with shell or precious stone.\n3. The trefoil motif indicates cultural or trade contacts with Mesopotamia.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All three statements are correct and define the key features of the Priest-King statue."
    ),
    (
        "Consider the following statements regarding stone sculptures of Harappa:\n1. A red sandstone torso of a male dancer showing exceptional anatomical realism was found at Harappa.\n2. Unlike Mohenjo-daro, Harappa yielded a large number of life-size bronze statues.\n3. The male dancer torso features socket holes in the neck and shoulders for attaching moving limbs.\nWhich of the statements given above are correct?",
        ["1 and 3 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 3 are correct. Statement 2 is incorrect: Harappa did not yield life-size bronze statues; bronze sculptures were rare and small."
    ),
    (
        "Consider the following statements regarding the Harappan weights system:\n1. The weights were highly standardized cubical blocks made of chert.\n2. The weights followed a binary system for lighter units and a decimal system for higher units.\n3. The basic binary unit of weight was equivalent to 13.63 grams, representing the ratio 16.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All three statements are correct, indicating a highly regulated commercial infrastructure."
    ),
    (
        "With reference to Harappan bricks, consider the following statements:\n1. Bricks used in Mature Harappan public works followed a strict ratio of 1:2:4 (thickness:width:length).\n2. Standard size bricks were used for building houses, while larger ones were used for city ramparts.\n3. Sun-dried bricks were preferred over baked bricks for construction of drainage lines.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: baked bricks were strictly used for drains, wells, and baths to prevent water erosion; sun-dried bricks were used for basic walls and platforms."
    ),
    (
        "Consider the following statements regarding the Indus Script:\n1. The script is written in Boustrophedon style (alternating directions from right-to-left and left-to-right).\n2. The script contains approximately 400 to 600 logo-syllabic symbols.\n3. The script was successfully deciphered in the 1950s using bilingual seals.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: the Indus Script remains completely undeciphered to this day."
    ),
    (
        "Consider the following statements regarding Harappan pottery:\n1. The characteristic pottery is painted Red and Black Ware.\n2. Common motifs painted on the red slips include pipal leaves, intersecting circles, and fish scales.\n3. Wheel-made pottery was completely absent, and all vessels were handmade.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "2 only", "1 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: the majority of Harappan pottery was wheel-made using fast potters' wheels."
    ),
    (
        "With reference to Harappan metallurgy, consider the following statements:\n1. The copper needed for bronze tools was primarily sourced from the Khetri mines of Rajasthan.\n2. Tin was imported from Afghanistan and Khorasan (Iran) to alloy copper into bronze.\n3. Iron metallurgy was widely practiced in the late Harappan phase.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "2 only", "1 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: the entire Harappan civilization was strictly pre-Iron; iron appeared in India during the Vedic period (c. 1000 BCE)."
    ),
    (
        "Consider the following statements regarding Faience in the Harappan culture:\n1. Faience ornaments were made of ground quartz sand glued together and glazed to create a glassy surface.\n2. Due to the complex manufacturing process, faience items were considered luxury, high-status goods.\n3. Large storage jars were commonly made of cheap, unglazed faience.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "2 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: faience was difficult to produce and reserved for tiny luxury items like beads, mini pots, and amulets, not large storage jars."
    ),
    (
        "With reference to shell-working, consider the following statements:\n1. Coastal sites like Lothal and Balakot were major centers for shell manufacturing.\n2. Shell-working craft included making bangles, ladles, inlay pieces, and beads.\n3. The shell ornaments were exported to inland cities like Harappa and Mohenjo-daro.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All three statements are correct and illustrate the inland distribution of coastal marine resources."
    ),
    (
        "Consider the following statements regarding trade with Mesopotamia:\n1. Mesopotamian records mention importing carnelian beads, lapis lazuli, gold, and ivory from Meluhha.\n2. Several Harappan seals and weights have been excavated from Mesopotamian cities like Ur and Susa.\n3. The trade was conducted primarily through overland caravan routes across the Hindu Kush.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: trade was primarily maritime, conducted via shipping routes across the Persian Gulf and Arabian Sea."
    ),
    (
        "With reference to Mesopotamian cuneiform records, consider the following statements:\n1. Meluhha is identified with the Indus Valley region.\n2. Dilmun represents the intermediate trade station of ancient Bahrain.\n3. Magan represents the copper-rich region of ancient Oman.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All three statements are correct, mapping the Bronze Age maritime trade route."
    ),
    (
        "Consider the following statements regarding the Late Harappan southern migration:\n1. The decline of the core Indus cities triggered a migration eastward and southward.\n2. Daimabad in Maharashtra represents a key late Harappan site that expanded southwards.\n3. The late phase in the south is characterized by the sudden adoption of iron metallurgy.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "2 only", "1 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: the Late phase remained pre-iron; they continued to use copper and stone tools."
    ),
    (
        "Consider the following statements regarding Late Harappan regional cultures:\n1. The Jhukar culture emerged as a post-urban regional adaptation in Sindh.\n2. The Cemetery H culture was centered in the Punjab region.\n3. Lustrous Red Ware culture represents the late Harappan phase in Gujarat.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All three statements are correct and represent the post-urban regional fragmentation of the civilization."
    ),
    (
        "With reference to the Late Harappan site of Mitathal, consider the following statements:\n1. It is located in the Haryana region and shows the post-urban transition.\n2. Excavations at Mitathal yielded copper flat axes and wire bangles from the late phase.\n3. The site retains the strict grid-iron planning and advanced drainage systems of Mohenjo-daro.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "2 only", "1 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: late phase sites like Mitathal show a degradation of civic planning, with a lack of grid layout and covered drainage."
    ),
    (
        "Consider the following statements regarding Alamgirpur in Uttar Pradesh:\n1. It represents the easternmost boundary site of the Harappan civilization.\n2. Excavations show a complete lack of public covered street drains and standard kiln-burnt bricks.\n3. It represents a rural, late phase village adaptation rather than a planned metropolis.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All three statements are correct, indicating the ruralized nature of peripheral late sites."
    ),
    (
        "Consider the following statements regarding Harappan agricultural diet:\n1. The primary agricultural crops were wheat, barley, lentils, and chickpeas.\n2. In Gujarat (Lothal and Rangpur), rice husks and impressions indicate early rice cultivation.\n3. Sugarcane and maize were the staple crops grown in the core Indus valley.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: sugarcane and maize were completely unknown to the Harappans."
    ),
    (
        "With reference to animal husbandry and depicted animals, consider the following statements:\n1. The humped zebu bull was domesticated and commonly depicted on seals.\n2. The wild buffalo and rhinoceros are depicted on Harappan seals and amulets.\n3. The lion was highly revered and frequently carved on administrative seals.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "2 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: the lion is completely absent from Harappan seals and art (it was replaced by the tiger)."
    ),
    (
        "Consider the following statements regarding bead manufacturing technology:\n1. Bead-making centers were excavated at Chanhudaro and Lothal.\n2. Carnelian beads were manufactured by heating the raw jasper/agate stone to trigger color changes.\n3. Bead artisans used specialized chert or bronze drills to perforate hard stones.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All three statements are correct and illustrate the high technological precision of Harappan bead craft."
    ),
    (
        "With reference to the water systems of Dholavira and Mohenjo-daro, consider the following statements:\n1. Mohenjo-daro relied on an abundance of groundwater wells, with over 700 wells discovered.\n2. Dholavira relied on conserving surface runoff water using stone check dams and reservoirs.\nWhich of the statements given above is/are correct?",
        ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        2,
        "Both statements are correct, reflecting two distinct ecological adaptions to water availability."
    ),
    (
        "Consider the following statements regarding the settlement hierarchy of the Indus Civilisation:\n1. Settlements can be grouped into large metropolises (Harappa, Mohenjo-daro), specialized ports (Lothal), industrial towns (Chanhudaro), and small rural sites.\n2. The uniformity of weights and brick dimensions suggests a strong central authority coordinating these different sites.\nWhich of the statements given above is/are correct?",
        ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        2,
        "Both statements are correct, showing a highly integrated settlement hierarchy and administrative organization."
    ),
    (
        "Consider the following statements regarding the sourcing of precious raw materials:\n1. Gold was primarily imported from Karnataka (Kolar gold fields).\n2. Carnelian and agate stones were sourced from Gujarat.\n3. Lapis Lazuli was imported from Badakhshan region through Shortughai.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All three statements are correct, detailing the extensive raw material procurement network."
    ),
    (
        "With reference to the decline of the Indus Civilisation, consider the following statements:\n1. Shifts in river courses Stranded cities away from navigable water channels.\n2. Tectonic uplifts diverted tributaries like the Yamuna and Sutlej, causing the drying of the Ghaggar-Hakra River.\n3. Repeated massive floods in the Indus plain forced the abandonment of Mohenjo-daro.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All statements represent valid, geographically supported theories of the civilization's gradual decline."
    )
]

# Hindi translation of the 50 practice questions
practice_data_hin = [
    (
        "सिंधु घाटी सभ्यता के सीमा स्थलों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. सबसे उत्तरी सीमा मांडा, झेलम नदी के किनारे स्थित है।\n2. सबसे दक्षिणी सीमा दैमाबाद, गोदावरी की सहायक नदी प्रवरा पर स्थित है।\n3. पश्चिमी सीमा का प्रतिनिधित्व करने वाला सुतकागेंडोर, दश्त नदी के किनारे स्थित है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        1,
        "कथन 1 गलत है: मांडा चिनाब नदी के किनारे स्थित है, झेलम के नहीं। कथन 2 और 3 सही हैं।"
    ),
    (
        "हड़प्पा संस्कृति के भौगोलिक विस्तार के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इस सभ्यता ने 10 लाख वर्ग किलोमीटर से अधिक के विशाल त्रिकोणीय क्षेत्र को कवर किया।\n2. हड़प्पा साम्राज्य का भौगोलिक विस्तार समकालीन मिस्र और मेसोपोटामिया के संयुक्त क्षेत्र से बड़ा था।\n3. सबसे पूर्वी सीमा मेरठ में यमुना नदी के किनारे आलमगीरपुर द्वारा दर्शाई जाती है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 2", "केवल 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: आलमगीरपुर हिंडन नदी के किनारे स्थित है, जो यमुना की सहायक नदी है, न कि सीधे यमुना नदी।"
    ),
    (
        "सिंधु सभ्यता की पर्यावरणीय और कृषि स्थितियों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. मुख्य क्षेत्र घने उष्णकटिबंधीय मानसूनी वर्षावनों से घिरा हुआ था।\n2. हड़प्पा की कृषि मुख्य रूप से सिंधु नदी से निकलने वाली नहरों के जाल पर निर्भर थी।\n3. गेहूं और जौ जैसी फसलों की शीतकालीन बुवाई मौसमी बाढ़ से जमा हुई उपजाऊ जलोढ़ मिट्टी पर निर्भर थी।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 3", "केवल 3", "केवल 2 और 3", "1, 2 और 3"],
        1,
        "कथन 1 और 2 गलत हैं: मुख्य क्षेत्र अर्ध-शुष्क था, न कि उष्णकटिबंधीय वर्षावन, और नहर सिंचाई बहुत दुर्लभ थी। कथन 3 सही है।"
    ),
    (
        "शॉर्टुघई की भौगोलिक चौकी के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह उत्तरी अफ़गानिस्तान में स्थापित एक परिपक्व हड़प्पा व्यापारिक केंद्र था।\n2. यह ऑक्सस (अमु दरिया) नदी के किनारे स्थित है।\n3. इसका मुख्य रणनीतिक कार्य खेतड़ी तांबा खदानों तक सीधी पहुँच सुनिश्चित करना था।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: शॉर्टुघई की स्थापना बदख्शां खदानों से लाजवर्त (lapis lazuli) और मध्य एशियाई धातुओं को प्राप्त करने के लिए की गई थी; खेतड़ी खदानें राजस्थान में हैं।"
    ),
    (
        "घग्गर-हाकड़ा नदी घाटी के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. खोजे गए सभी सिंधु घाटी स्थलों में से 60% से अधिक इस सूखे बेसिन में केंद्रित हैं।\n2. क्यूनिफॉर्म अभिलेखों में घग्गर-हाकड़ा नदी को 'मेलुहा' कहा गया है।\n3. इस नदी मार्ग का सूखना विवर्तनिक बदलावों से जुड़ा है जिसने इसके जल स्रोतों को मोड़ दिया।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "Visual केवल 1 और 3", "1, 2 और 3"],
        2,
        "कथन 1 और 3 सही हैं। कथन 2 गलत है: मेलुहा संपूर्ण सिंधु क्षेत्र के लिए मेसोपोटामियाई नाम था, न कि केवल घग्गर-हाकड़ा नदी के लिए।"
    ),
    (
        "लोथल के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. यहाँ से पकी ईंटों से बना एक विशाल बेसिन मिला है जिसे ज्वारीय गोदीवाड़ा (dockyard) माना जाता है।\n2. यह खंभात की खाड़ी के मुहाने पर साबरमती की सहायक नदी भोगवो के किनारे स्थित है।\n3. इसके कब्रिस्तान से एक ही कब्र में पुरुष और महिला के युगल शवाधान के साक्ष्य मिले हैं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        3,
        "तीनों कथन सही हैं और लोथल बंदरगाह शहर की प्रमुख पुरातात्विक खोजों को दर्शाते हैं।"
    ),
    (
        "धोलावीरा की जल प्रबंधन प्रणाली के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह शहर पत्थर को काटकर बनाए गए विशाल जलाशयों और बांधों के लिए प्रसिद्ध है।\n2. अन्य हड़प्पा शहरों के विपरीत, यह पूरी तरह से घरेलू कुओं पर निर्भर था न कि सार्वजनिक जलाशयों पर।\n3. जलाशय मनहर और मनसर जैसे मौसमी नालों से आने वाले बारिश के पानी को इकट्ठा करते थे।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        2,
        "कथन 1 और 3 सही हैं। कथन 2 गलत है: धोलावीरा शुष्क वातावरण में पानी जमा करने के लिए सार्वजनिक जलाशयों पर निर्भर था; मोहनजोदड़ो की तुलना में यहाँ निजी कुएं बहुत कम थे।"
    ),
    (
        "धोलावीरा के नगर नियोजन के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. मानक दोहरे लेआउट के विपरीत, धोलावीरा तीन किलेबंद भागों में विभाजित है: दुर्ग, मध्य नगर और निचला नगर।\n2. धोलावीरा के किले और संरचनाओं की विशेषता बड़े पैमाने पर पत्थर की चिनाई का उपयोग है।\n3. धोलावीरा से सिंधु लिपि के दस बड़े जिप्सम अक्षरों वाला एक अनोखा साइनबोर्ड मिला है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        3,
        "तीनों कथन सही हैं और धोलावीरा की अनूठी वास्तुकला और लिपियों को दर्शाते हैं।"
    ),
    (
        "चन्हुदड़ो के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह मनके बनाने, मुहर तराशने और शंख-शिल्प में विशेषज्ञता रखने वाला एक अभेद्य औद्योगिक शहर था।\n2. यह एकमात्र ऐसा प्रमुख शहर है जहाँ प्रशासनिक दुर्ग (citadel) का पूर्ण अभाव है।\n3. यहाँ से बिल्ली का पीछा करते हुए कुत्ते के पंजे के निशान वाली ईंट मिली है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 and 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        3,
        "तीनों कथन सही हैं। चन्हुदड़ो प्रशासनिक दुर्ग के बिना एक विशुद्ध शिल्प उपनगर था।"
    ),
    (
        "राखीगढ़ी पुरातात्विक स्थल के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इसे वर्तमान में सिंधु घाटी सभ्यता का सबसे बड़ा भौगोलिक स्थल (350 हेक्टेयर से अधिक) माना जाता है।\n2. यह हरियाणा के हिसार जिले में सूखी घग्गर नदी घाटी में स्थित है।\n3. राखीगढ़ी के उत्खनन से कोई कब्रिस्तान या मानव कंकाल नहीं मिले हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: राखीगढ़ी से एक बड़ा कब्रिस्तान मिला है, जिसके कंकालों का उपयोग डीएनए (DNA) अध्ययनों के लिए किया गया है।"
    ),
    (
        "कालीबंगन के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. यहाँ से पूर्व-परिपक्व प्रारंभिक हड़प्पा काल का एक खेत मिला है जिस पर आड़े-तिरछे जुताई के निशान हैं।\n2. जुते हुए खेत का स्वरूप दर्शाता है कि यहाँ एक साथ दो फसलें उगाई जाती थीं (दोहरी फसल)।\n3. यह राजस्थान में घग्गर-हाकड़ा नदी के सूखे मार्ग पर स्थित है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        3,
        "तीनों कथन सही हैं। आड़े-तिरछे हल का प्रतिरूप दुनिया में दोहरी फसल का सबसे पहला साक्ष्य है।"
    ),
    (
        "बनावली के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यहाँ से मिट्टी का बना हल का एक अच्छी तरह से संरक्षित खिलौना मिला है।\n2. यह ग्रिड-नियोजित सड़कों वाले नगर नियोजन का पूर्ण रूप से पालन करता है।\n3. यह हरियाणा के फतेहाबाद जिले में स्थित है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 3", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 3 सही हैं। कथन 2 गलत है: बनावली ग्रिड नगर नियोजन का अपवाद होने के लिए प्रसिद्ध है, यहाँ गलियाँ त्रिज्यीय (radial) हैं।"
    ),
    (
        "मोहनजोदड़ो के विशाल स्नानागार (Great Bath) के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. जलाशय को वाटर-प्रूफ बनाने के लिए ईंटों के बीच प्राकृतिक डामर (बिटुमेन) की परत लगाई गई थी।\n2. यह शहर के पूर्वी निचले नगर (Lower Town) वाले हिस्से में स्थित है।\n3. यह चारों ओर से बदलने वाले कमरों से घिरा था और इसका उपयोग धार्मिक स्नान के लिए माना जाता है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        2,
        "कथन 1 और 3 सही हैं। कथन 2 गलत है: विशाल स्नानागार दुर्ग (Citadel) क्षेत्र में स्थित है, निचले नगर में नहीं।"
    ),
    (
        "हड़प्पा शहरों में अनाज के भंडारण के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. मोहनजोदड़ो और हड़प्पा में ऊंचे चबूतरे पर बने विशाल अन्नागार उत्खनित किए गए हैं।\n2. इन अन्नागारों में सीलन और सड़न को रोकने के लिए हवा के आने-जाने के मार्ग (ducts) बने थे।\n3. अन्नागारों से अनाज का नियंत्रण और वितरण राज्य-नियंत्रित खाद्य सुरक्षा को दर्शाता है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        3,
        "तीनों कथन सही हैं, जो हड़प्पा राज्य के जटिल प्रशासनिक संगठन को दर्शाते हैं।"
    ),
    (
        "मोहनजोदड़ो की नागरिक स्वच्छता के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. समकालीन सभ्यताओं के विपरीत, लगभग हर घर में ईंटों से बना अपना कुआँ था।\n2. घरों की नालियाँ सड़कों की ढकी हुई मुख्य नालियों से जुड़ी थीं जिनमें मेनहोल बने थे।\n3. प्राकृतिक कीटाणुशोधन के लिए सड़कों की सभी नालियों को खुला छोड़ दिया गया था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: नालियों को ईंटों या पत्थरों से व्यवस्थित रूप से ढका गया था, जिन्हें सफाई के लिए हटाया जा सकता था।"
    ),
    (
        "हड़प्पा सभ्यता में घोड़ों की उपस्थिति के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. गुजरात का सुरकोटदा एकमात्र ऐसा स्थल है जहाँ से घोड़े के कंकाल के अवशेष मिलने की सूचना मिली है।\n2. घोड़े ने परिपक्व हड़प्पा कृषि और भारी वाहनों को खींचने में महत्वपूर्ण भूमिका निभाई थी।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
        0,
        "कथन 1 सही है (हालांकि विद्वानों में घोड़े की उपस्थिति पर बहस है)। कथन 2 गलत है: मुख्य खींचने वाला जानवर बैल था; कृषि में घोड़े की कोई भूमिका नहीं थी।"
    ),
    (
        "बालाकोट के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह पाकिस्तानी बलूचिस्तान में कराची के पास स्थित एक तटीय स्थल है।\n2. यह शंख की चूड़ियाँ और मनके बनाने में विशेषज्ञता रखने वाला प्रमुख शिल्प केंद्र था।\n3. बालाकोट में समुद्री संसाधनों के व्यापार की कोई सुविधा उपलब्ध नहीं थी।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: बालाकोट स्थानीय शिल्पों और निर्यात व्यापार के लिए समुद्री शंख संसाधनों पर अत्यधिक निर्भर था।"
    ),
    (
        "सुतकागेंडोर के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. यह ईरान सीमा के पास मकरान तट पर एक सुरक्षित तटीय बंदरगाह और मीठे पानी का स्टेशन था।\n2. यह मेसोपोटामिया के साथ समुद्री व्यापार संपर्कों के प्रत्यक्ष पुरातात्विक साक्ष्य दिखाता है।\n3. यहाँ लोथल की तरह पकी ईंटों से बना एक विशाल ज्वारीय गोदीवाड़ा (dockyard) था।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: सुतकागेंडोर एक चट्टानी पहाड़ी पर बना किला है, यहाँ लोथल जैसा गोदीवाड़ा नहीं था।"
    ),
    (
        "कुंतासी के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. यह गुजरात में स्थित एक किला बंद बंदरगाह और शंख-शिल्प केंद्र था।\n2. इसने कच्छ की खाड़ी में प्रवेश करने वाले व्यापार की निगरानी करने वाले तटीय द्वार के रूप में कार्य किया।\n3. लोथल के विपरीत, यह बिना किसी विनिर्माण कारखाने के विशुद्ध रूप से आवासीय नगर था।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: कुंतासी में शंख शिल्प की कार्यशालाएं सक्रिय थीं और इसने व्यापारिक-सह-विनिर्माण केंद्र के रूप में कार्य किया।"
    ),
    (
        "दैमाबाद की कांस्य मूर्तियों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. दैमाबाद से तांबे-कांसे की चार ठोस पशु और रथ मूर्तियाँ मिली हैं।\n2. इन मूर्तियों में सांडों द्वारा खींचा जाने वाला रथ, एक हाथी, एक गेंडा और एक भैंसा शामिल हैं।\n3. यह भंडार दर्शाता है कि महाराष्ट्र में उत्तर हड़प्पा काल में भी धातु कर्म जीवित रहा।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        3,
        "तीनों कथन सही हैं और दैमाबाद तांबे के भंडार के महत्व को दर्शाते हैं।"
    ),
    (
        "कोट दीजी के पूर्व-परिपक्व स्थल के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह सिंध में सिंधु नदी के बाएं तट पर स्थित है।\n2. प्रारंभिक स्तर को परिपक्व स्तर से अलग करने वाली राख की एक मोटी परत यहाँ भीषण आग से तबाही को दर्शाती है।\n3. कोट दीजी के मिट्टी के बर्तन सादे हैं और उन पर सींग वाले देवता जैसे कोई चित्र नहीं हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 2", "केवल 1 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: कोट दीजी के बर्तन सींग वाले देवता के चित्रों के लिए प्रसिद्ध हैं।"
    ),
    (
        "हड़प्पा काल के शवाधानों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. शवों को आमतौर पर मिट्टी के बर्तनों और आभूषणों के साथ उत्तर-दक्षिण दिशा में दफनाया जाता था।\n2. पकी मिट्टी (terracotta) से बने ताबूत सभी शहरों में शवाधान के मानक थे।\n3. हड़प्पा के कब्रिस्तान R-37 से देवदार की लकड़ी के ताबूत वाले शवाधान के साक्ष्य मिले हैं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 3", "केवल 1 और 2", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 3 सही हैं। कथन 2 गलत है: साधारण कब्रें (गर्त शवाधान) मानक थीं; टेराकोटा ताबूत अत्यंत दुर्लभ अपवाद थे।"
    ),
    (
        "युगल शवाधान (Double Burials) के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. लोथल एकमात्र ऐसा स्थल है जहाँ एक ही कब्र में पुरुष और महिला को एक साथ दफनाने के प्रमाण मिले हैं।\n2. ये युगल शवाधान सती प्रथा के प्रचलन का पूर्ण और अकाट्य प्रमाण प्रदान करते हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
        0,
        "कथन 1 सही है। कथन 2 गलत है: विद्वानों के अनुसार संयुक्त कब्रें महामारी या प्राकृतिक आपदाओं के कारण हो सकती हैं; सती का कोई पुख्ता प्रमाण नहीं है।"
    ),
    (
        "हड़प्पा स्थलों में अग्निवेदियों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. कालीबंगन में मिट्टी की ईंटों के चबूतरे पर सात अग्निवेदियों की एक पंक्ति खोजी गई थी।\n2. अग्निवेदियों के साक्ष्य लोथल और बनावली से भी प्राप्त हुए हैं।\n3. अग्निवेदियां हड़प्पा और मोहनजोदड़ो के दुर्गों की भी एक मानक विशेषता थीं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: हड़प्पा और मोहनजोदड़ो में अग्निवेदियों का पूर्ण अभाव है।"
    ),
    (
        "हड़प्पा मुहरों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. इनका निर्माण मुख्य रूप से नरम सेलखड़ी (steatite) से किया जाता था और फिर पकाया जाता था।\n2. अधिकांश मुहरें चौकोर या आयताकार हैं जिन पर संक्षिप्त लेख और पशुओं का अंकन है।\n3. मुहरों का उपयोग केवल अन्नागारों के दरवाजों को बंद करने के लिए होता था, व्यापारिक माल के लिए नहीं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: मुहरों का मुख्य उपयोग व्यापारिक वस्तुओं पर मिट्टी की गिल्टी को सील करने के लिए होता था।"
    ),
    (
        "पशुपति मुहर के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह एक सींग वाला मुकुट पहने और योग मुद्रा में बैठे एक पुरुष देवता को दर्शाता है।\n2. यह आकृति पांच जानवरों: एक हाथी, एक बाघ, एक गेंडा, एक भैंसा और पैरों के पास दो हिरणों से घिरी है।\n3. सर जॉन मार्शल ने इस आकृति की पहचान 'आदि-शिव' के रूप में की थी।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        3,
        "तीनों कथन सही हैं और पशुपति मुहर के रूपांकनों का सटीक विवरण देते हैं।"
    ),
    (
        "मुहरों पर एकश्रृंगी (unicorn) रूपांकन के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. काल्पनिक एक सींग वाला यह पशु परिपक्व मुहरों पर सबसे अधिक चित्रित किया गया जानवर है।\n2. इसे अक्सर एक 'धूपदानी' या 'मानक' (standard) वस्तु के साथ उकेरा जाता है।\n3. विद्वानों में सहमति है कि यह केवल सम्राट की शाही मुहर का प्रतिनिधित्व करता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 2", "Ref केवल 1 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: सम्राट पर कोई सहमति नहीं है; विद्वानों के अनुसार यह एक प्रमुख व्यापारी श्रेणी या कबीले का प्रतीक था।"
    ),
    (
        "कांस्य की नर्तकी की मूर्ति के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. यह लुप्त-मोम (lost-wax/cire perdue) तकनीक का उपयोग करके बनाई गई ठोस मूर्ति है।\n2. नर्तकी को उसकी बाईं भुजा पर बड़ी संख्या में चूड़ियाँ पहने हुए चित्रित किया गया है।\n3. वह जोड़ों में बिना किसी हलचल के बिल्कुल सीधी और खड़ी मुद्रा में दिखाई गई है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: वह अपने कूल्हे पर हाथ रखे एक गतिशील 'त्रिभंग' नृत्य मुद्रा में खड़ी है।"
    ),
    (
        "सेलखड़ी से बनी पुरोहित-राजा की मूर्ति के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह तिपतिया पैटर्न से सजी शॉल ओढ़े एक दाढ़ी वाली आकृति को दर्शाती है।\n2. आँखें लंबी हैं और मूल रूप से शंख या कीमती पत्थर से जड़ी हुई थीं।\n3. तिपतिया रूपांकन मेसोपोटामिया के साथ सांस्कृतिक या व्यापारिक संपर्कों का संकेत देता है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        3,
        "तीनों कथन सही हैं और पुरोहित-राजा की मूर्ति की प्रमुख विशेषताओं को परिभाषित करते हैं।"
    ),
    (
        "हड़प्पा की पत्थर की मूर्तियों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. हड़प्पा से शारीरिक यथार्थवाद दर्शाने वाले पुरुष नर्तक का लाल बलुआ पत्थर का धड़ मिला है।\n2. मोहनजोदड़ो के विपरीत, हड़प्पा से जीवन-आकार की कई कांस्य मूर्तियां मिली हैं।\n3. पुरुष नर्तक के धड़ में गर्दन और कंधों पर घूमने वाले अंगों को जोड़ने के लिए छेद बने हैं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 3", "केवल 1 और 2", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 3 सही हैं। कथन 2 गलत है: हड़प्पा से जीवन-आकार की कांस्य मूर्तियां नहीं मिली हैं।"
    ),
    (
        "हड़प्पा की वजन प्रणाली के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. बाट चर्ट पत्थर से बने अत्यधिक मानकीकृत घनाकार टुकड़े थे।\n2. बाट निचले मूल्यों के लिए द्वि-आधारी प्रणाली और उच्च मूल्यों के लिए दशमलव प्रणाली का पालन करते थे।\n3. वजन की मूल द्वि-आधारी इकाई 13.63 ग्राम के बराबर थी, जो अनुपात 16 का प्रतिनिधित्व करती थी।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        3,
        "तीनों कथन सही हैं, जो एक अत्यधिक विनियमित वाणिज्यिक प्रणाली को दर्शाते हैं।"
    ),
    (
        "हड़प्पा कालीन ईंटों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. परिपक्व सार्वजनिक कार्यों में उपयोग की जाने वाली ईंटें मोटाई-चौड़ाई-लंबाई के कड़े 1:2:4 अनुपात का पालन करती थीं।\n2. घर बनाने के लिए मानक आकार की ईंटों का उपयोग होता था, जबकि शहर की दीवारों के लिए बड़ी ईंटों का उपयोग किया जाता था।\n3. नालियों के निर्माण के लिए पकी ईंटों के बजाय धूप में सुखाई गई ईंटों को प्राथमिकता दी जाती थी।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: पानी के क्षरण को रोकने के लिए नालियों और कुओं में केवल पकी ईंटों का उपयोग किया जाता था।"
    ),
    (
        "सिंधु लिपि के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. यह लिपि बूस्ट्रोफेडन शैली (वैकल्पिक रूप से दाएं-से-बाएं और बाएं-से-दाएं) में लिखी जाती थी।\n2. लिपि में लगभग 400 से 600 तक शब्द-अक्षरात्मक (logo-syllabic) प्रतीक पाए जाते हैं।\n3. इस लिपि को 1950 के दशक में द्विभाषी मुहरों की सहायता से सफलतापूर्वक पढ़ लिया गया था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: सिंधु लिपि आज तक पूरी तरह से अपठित है।"
    ),
    (
        "हड़प्पा के मिट्टी के बर्तनों (pottery) के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. यहाँ के विशिष्ट मृदभांड लाल और काले चित्रित मृदभांड हैं।\n2. लाल सतह पर काले रंग से बनाए गए चित्रों में पीपल के पत्ते, वृत्त और मछली के शल्क शामिल हैं।\n3. चाक पर बनने वाले बर्तन पूरी तरह अनुपस्थित थे और सभी बर्तन हाथ से बनाए जाते थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 2", "केवल 1 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: अधिकांश बर्तन चाक का उपयोग करके बनाए जाते थे।"
    ),
    (
        "हड़प्पा धातु कर्म के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. कांस्य औजारों के लिए आवश्यक तांबा मुख्य रूप से राजस्थान की खेतड़ी खदानों से मंगाया जाता था।\n2. तांबे में मिलाने के लिए आवश्यक रांगा (tin) अफ़गानिस्तान और ईरान से आयात किया जाता था।\n3. उत्तर हड़प्पा चरण में लोहे के धातु कर्म का व्यापक प्रचलन था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 2", "केवल 1 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: संपूर्ण हड़प्पा सभ्यता लौह-पूर्व थी; लोहा बाद में वैदिक काल में आया।"
    ),
    (
        "हड़प्पा संस्कृति में फेयॉन्स (Faience) के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. फेयॉन्स के गहने पिसे हुए क्वार्ट्ज/रेत को गोंद के साथ मिलाकर और भट्टी में पकाकर चमकीले बनाए जाते थे।\n2. जटिल निर्माण प्रक्रिया के कारण फेयॉन्स की वस्तुओं को सामाजिक प्रतिष्ठा का प्रतीक माना जाता था।\n3. अनाज रखने के बड़े मटके आमतौर पर सस्ते और बिना पॉलिश वाले फेयॉन्स से बनाए जाते थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 2", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: फेयॉन्स कठिनता से बनता था और यह केवल छोटे गहनों और डिब्बियों तक सीमित था, न कि अनाज के मटकों के लिए।"
    ),
    (
        "शंख-शिल्प (shell-working) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. लोथल और बालाकोट जैसे तटीय स्थल शंख के आभूषण बनाने के प्रमुख केंद्र थे।\n2. शंख शिल्प में चूड़ियाँ, चमचे, पच्चीकारी के टुकड़े और मनके शामिल थे।\n3. शंख के गहनों का निर्यात हड़प्पा और मोहनजोदड़ो जैसे अंतर्देशीय शहरों में किया जाता था।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        3,
        "तीनों कथन सही हैं और तटीय समुद्री संसाधनों के अंतर्देशीय वितरण को दर्शाते हैं।"
    ),
    (
        "मेसोपोटामिया के साथ व्यापार के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. मेसोपोटामिया के अभिलेखों में मेलुहा से अकीक के मनके, लाजवर्त, सोना और हाथी दांत मंगाने का उल्लेख है।\n2. मेसोपोटामिया के शहरों (उर, सूसा) से हड़प्पा की कई मुहरें और बाट मिले हैं।\n3. यह व्यापार मुख्य रूप से हिंदूकुश के स्थलीय काफिला मार्गों से होता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: यह व्यापार मुख्यतः समुद्री मार्ग से फ़ारस की खाड़ी के माध्यम से होता था।"
    ),
    (
        "मेसोपोटामिया के क्यूनिफॉर्म अभिलेखों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मेलुहा का तात्पर्य सिंधु घाटी क्षेत्र से है।\n2. दिलमुन बहरीन के तटीय व्यापार स्टेशन का प्रतिनिधित्व करता है।\n3. मगन तांबे से समृद्ध प्राचीन ओमान क्षेत्र को दर्शाता है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "Ref केवल 1 और 3", "1, 2 और 3"],
        3,
        "तीनों कथन सही हैं और कांस्य युग के समुद्री व्यापार मार्ग को दर्शाते हैं।"
    ),
    (
        "उत्तर हड़प्पा काल के दक्षिण की ओर विस्थापन के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. मुख्य शहरों के पतन ने आबादी को पूर्व और दक्षिण की ओर पलायन करने के लिए प्रेरित किया।\n2. महाराष्ट्र का दैमाबाद दक्षिण की ओर हुए विस्तार का प्रतिनिधित्व करने वाला प्रमुख स्थल है।\n3. दक्षिण में उत्तर चरण की पहचान अचानक लोहे के धातु कर्म को अपनाने से होती है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 2", "केवल 1 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: उत्तर चरण भी पूरी तरह से लौह-पूर्व था और लोग तांबे और पत्थर का उपयोग करते थे।"
    ),
    (
        "उत्तर हड़प्पा कालीन क्षेत्रीय संस्कृतियों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. झुकर संस्कृति सिंध में एक उत्तर-शहरी क्षेत्रीय अनुकूलन के रूप में उभरी।\n2. सिमेट्री एच संस्कृति पंजाब क्षेत्र में केंद्रित थी।\n3. चमकीले लाल मृदभांड (Lustrous Red Ware) संस्कृति गुजरात में उत्तर चरण को दर्शाती है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        3,
        "तीनों कथन सही हैं और सभ्यता के उत्तर-शहरी विखंडन को दर्शाते हैं।"
    ),
    (
        "उत्तर हड़प्पा स्थल मिताथल के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह हरियाणा क्षेत्र में स्थित है और उत्तर-शहरी संक्रमण को दर्शाता है।\n2. मिताथल से तांबे की कुल्हाड़ियाँ और तार की चूड़ियाँ मिली हैं।\n3. यह स्थल मोहनजोदड़ो की तरह कड़े ग्रिड नगर नियोजन और ढकी नालियों को बनाए रखता है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 2", "केवल 1 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: मिताथल जैसे उत्तर स्थलों में नागरिक नियोजन और ढकी नालियों का पतन दिखाई देता है।"
    ),
    (
        "उत्तर प्रदेश के आलमगीरपुर के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. यह सिंधु सभ्यता की सबसे पूर्वी सीमा का प्रतिनिधित्व करता है।\n2. यहाँ से सार्वजनिक ढकी नालियों और मानक पकी ईंटों के निर्माण का पूर्ण अभाव मिला है।\n3. यह एक नियोजित महानगर के बजाय ग्रामीण उत्तर चरण के गाँव का प्रतिनिधित्व करता है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        3,
        "तीनों कथन सही हैं, जो बाहरी उत्तर बस्तियों के ग्रामीण स्वरूप को दर्शाते हैं।"
    ),
    (
        "हड़प्पा कृषि आहार के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. मुख्य कृषि फसलें गेहूं, जौ, दालें और चने थे।\n2. गुजरात (लोथल और रंगपुर) से धान की भूसी के साक्ष्य मिले हैं जो शुरुआती धान की खेती दर्शाते हैं।\n3. गन्ना और मक्का सिंधु घाटी में उगाई जाने वाली प्रमुख फसलें थीं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: गन्ना और मक्का हड़प्पावासियों के लिए पूरी तरह से अज्ञात थे।"
    ),
    (
        "पशुपालन और चित्रित जानवरों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. कूबड़ वाले ज़ेबू बैल को पालतू बनाया गया था और इसे आमतौर पर मुहरों पर चित्रित किया गया था।\n2. जंगली भैंसा और गेंडा मुहरों और ताबीज पर उकेरे गए मिलते हैं।\n3. सिंह (शेर) को अत्यधिक सम्मानित माना जाता था और इसे मुहरों पर अक्सर उकेरा जाता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 2", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: हड़प्पा मुहरों पर सिंह (शेर) का चित्रण पूरी तरह से अनुपस्थित है (इसकी जगह बाघ चित्रित है)।"
    ),
    (
        "मनके बनाने की तकनीक के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. चन्हुदड़ो और लोथल से मनके बनाने के कारखाने मिले हैं।\n2. अकीक (carnelian) के मनकों को उनका विशिष्ट लाल रंग देने के लिए गर्म किया जाता था।\n3. कारीगर पत्थरों में छेद करने के लिए विशिष्ट चर्ट या कांस्य के बरमों का उपयोग करते थे।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "Ref केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        3,
        "तीनों कथन सही हैं और मनके बनाने की उच्च तकनीक को दर्शाते हैं।"
    ),
    (
        "धोलावीरा और मोहनजोदड़ो की जल प्रणालियों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मोहनजोदड़ो भूजल के कुओं पर अत्यधिक निर्भर था, यहाँ से 700 से अधिक कुएँ मिले हैं।\n2. धोलावीरा ने पत्थर के बांधों और जलाशयों का उपयोग करके बारिश के पानी के संरक्षण को प्राथमिकता दी।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
        2,
        "दोनों कथन सही हैं, जो दो अलग-अलग भौगोलिक क्षेत्रों में पानी की उपलब्धता के अनुकूलन को दर्शाते हैं।"
    ),
    (
        "सिंधु सभ्यता की बस्तियों के पदानुक्रम के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. बस्तियों को महानगरों (हड़प्पा, मोहनजोदड़ो), विशिष्ट बंदरगाहों (लोथल) और औद्योगिक कस्बों (चन्हुदड़ो) में वर्गीकृत किया जा सकता है।\n2. बाटों और ईंटों के आयामों की एकरूपता इन विभिन्न स्थलों के बीच समन्वय करने वाले एक मजबूत केंद्रीय अधिकार का संकेत देती है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
        2,
        "दोनों कथन सही हैं, जो अत्यधिक संगठित और एकीकृत निपटान पदानुक्रम को दर्शाते हैं।"
    ),
    (
        "कच्चे माल के स्रोतों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. सोना मुख्य रूप से कर्नाटक (कोलार स्वर्ण क्षेत्र) से मंगाया जाता था।\n2. अकीक और गोमेद पत्थर मुख्य रूप से गुजरात से मंगाए जाते थे।\n3. लाजवर्त (lapis lazuli) का आयात शॉर्टुघई के माध्यम से बदख्शां क्षेत्र से किया जाता था।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        3,
        "तीनों कथन सही हैं और प्रचुर मात्रा में कच्चे माल की खरीद नेटवर्क का विवरण देते हैं।"
    ),
    (
        "सिंधु सभ्यता के पतन के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. नदियों के मार्ग बदलने से शहर पानी और परिवहन मार्गों से दूर होकर एकाकी हो गए।\n2. विवर्तनिक हलचलों ने यमुना और सतलज जैसी सहायक नदियों को मोड़ दिया, जिससे घग्गर-हाकड़ा नदी सूख गई।\n3. सिंधु के मैदानों में बार-बार आने वाली भीषण बाढ़ ने मोहनजोदड़ो को छोड़ने के लिए मजबूर किया।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        3,
        "सभी कथन सिंधु सभ्यता के क्रमिक पतन के संबंध में विवर्तनिक और भौगोलिक रूप से समर्थित सिद्धांतों को दर्शाते हैं।"
    )
]


# =========================================================================
# MOCK TEST QUESTIONS (10 Qs)
# =========================================================================
# (Already defined in UPSC Multi-Statement Style)


# Translation Map of all English strings to Hindi for Mastery Zone
TRANS_MAP = {
    # Types
    "MCQ": "MCQ",
    "Multiple Correct MCQ": "Multiple Correct MCQ",
    "True/False": "True/False",
    "Fill in the Blank": "Fill in the Blank",
    "Match the Following": "Match the Following",
    "One-Liner": "One-Liner",
    "Assertion-Reason": "Assertion-Reason",
    "Statement-Based": "Statement-Based",
    "Why": "Why",
    "How": "How",
    "Case Study": "Case Study",
    "Teach the Concept": "Teach the Concept",

    # Section 1 Qs
    "Which of the following sites represents the westernmost boundary of the Indus Valley Civilisation?": "निम्नलिखित में से कौन सा स्थल सिंधु घाटी सभ्यता की सबसे पश्चिमी सीमा का प्रतिनिधित्व करता है?",
    "Manda": "मांडा", "Daimabad": "दैमाबाद", "Sutkagendor": "सुतकागेंडोर", "Alamgirpur": "आलमगीरपुर",
    "Sutkagendor in Balochistan represents the westernmost frontier, situated on the Dasht River.": "बलूचिस्तान में सुतकागेंडोर सबसे पश्चिमी सीमा का प्रतिनिधित्व करता है, जो दश्त नदी के किनारे स्थित है।",
    "The highest density of Indus Valley settlements has been discovered in which river basin?": "सिंधु घाटी की बस्तियों का सबसे अधिक घनत्व किस नदी बेसिन में खोजा गया है?",
    "The Indus River Basin": "सिंधु नदी बेसिन", "The Ghaggar-Hakra River Basin": "घग्गर-हाकड़ा नदी बेसिन", "The Ganga-Yamuna Basin": "गंगा-यमुना बेसिन", "The Narmada Valley Basin": "नर्मदा घाटी बेसिन",
    "The Ghaggar-Hakra system hosts the highest concentration of settlements (often linked to the heartland of the culture).": "घग्गर-हाकड़ा नदी प्रणाली में बस्तियों का सबसे अधिक संकेंद्रण है (इसे सभ्यता का मुख्य केंद्र माना जाता है)।",
    "Manda, the northernmost limit of the mature Harappan phase, is situated on the banks of which river?": "परिपक्व हड़प्पा काल का सबसे उत्तरी सीमा स्थल मांडा किस नदी के किनारे स्थित है?",
    "Sutlej": "सतलज", "Chenab": "चिनाब", "Jhelum": "झेलम", "Indus": "सिंधु",
    "Manda is located in Jammu & Kashmir along the right bank of the Chenab River.": "मांडा जम्मू-कश्मीर में चिनाब नदी के दाहिने तट पर स्थित है।",
    "The southern boundary of the Indus Valley Civilisation is marked by Daimabad, which is located in which modern state?": "सिंधु घाटी सभ्यता की दक्षिणी सीमा दैमाबाद द्वारा चिह्नित है, जो किस आधुनिक राज्य में स्थित है?",
    "Gujarat": "गुजरात", "Maharashtra": "महाराष्ट्र", "Rajasthan": "राजस्थान", "Madhya Pradesh": "मध्य प्रदेश",
    "Daimabad is situated in Ahmednagar district, Maharashtra, on the Pravara River, a tributary of the Godavari.": "दैमाबाद महाराष्ट्र के अहमदनगर जिले में गोदावरी की सहायक नदी प्रवरा के किनारे स्थित है।",
    "The geographical outpost of Shortughai, indicating direct access to Central Asian lapis lazuli trade, is in which country?": "लाजवर्त (लापीस लाजुली) व्यापार तक सीधी पहुँच दर्शाने वाली शॉर्टुघई की भौगोलिक चौकी किस देश में स्थित है?",
    "Iran": "ईरान", "Pakistan": "पाकिस्तान", "Afghanistan": "अफ़गानिस्तान", "Tajikistan": "ताजिकिस्तान",
    "Shortughai is a Harappan trading outpost situated in northern Afghanistan.": "शॉर्टुघई उत्तरी अफ़गानिस्तान में स्थित एक हड़प्पाई व्यापारिक चौकी है।",

    # S1 Multi-Correct
    "Identify the coastal ports and maritime trading outposts of the Indus Civilisation: (Select all that apply)": "सिंधु सभ्यता के तटीय बंदरगाहों और समुद्री व्यापारिक चौकियों की पहचान करें: (लागू होने वाले सभी विकल्प चुनें)",
    "Lothal": "लोथल", "Balakot": "बालाकोट", "Shortughai": "शॉर्टुघई",
    "Lothal, Sutkagendor, and Balakot are coastal maritime outposts. Shortughai is an inland northern trade enclave.": "लोथल, सुतकागेंडोर और बालाकोट तटीय बंदरगाह स्थल हैं। शॉर्टुघई एक अंतर्देशीय व्यापारिक क्षेत्र है।",
    "Which of the following sites are situated in the modern state of Gujarat? (Select all that apply)": "निम्नलिखित में से कौन से स्थल आधुनिक गुजरात राज्य में स्थित हैं? (लागू होने वाले सभी विकल्प चुनें)",
    "Dholavira": "धोलावीरा", "Surkotada": "सुरकोटदा", "Rojdi": "रोजड़ी", "Banawali": "बनावली",
    "Dholavira, Surkotada, and Rojdi are in Gujarat. Banawali is in Haryana.": "धोलावीरा,存रकोटदा और रोजड़ी गुजरात में हैं। बनावली हरियाणा में है।",
    "Select the sites situated in the Ghaggar-Hakra river basin in Haryana: (Select all that apply)": "हरियाणा में घग्गर-हाकड़ा नदी बेसिन में स्थित स्थलों का चयन करें: (लागू होने वाले सभी विकल्प चुनें)",
    "Rakhigarhi": "राखीगढ़ी", "Bhirrana": "भिरड़ाना", "Amri": "आमरी",
    "Rakhigarhi, Banawali, and Bhirrana are Ghaggar-Hakra basin sites in Haryana. Amri is in Sindh.": "राखीगढ़ी, बनावली और भिरड़ाना हरियाणा में घग्गर-हाकड़ा बेसिन के स्थल हैं। आमरी सिंध में है।",
    "Which boundaries define the geographical quadrangle of the Indus Valley Civilisation? (Select all that apply)": "कौन सी सीमाएँ सिंधु घाटी सभ्यता के भौगोलिक चतुर्भुज को परिभाषित करती हैं? (लागू होने वाले सभी विकल्प चुनें)",
    "Manda in Jammu (North)": "जम्मू में मांडा (उत्तर)", "Daimabad in Maharashtra (South)": "महाराष्ट्र में दैमाबाद (दक्षिण)", "Sutkagendor in Balochistan (West)": "बलूचिस्तान में सुतकागेंडोर (पश्चिम)", "Mehrgarh in Balochistan (South)": "बलूचिस्तान में मेहरगढ़ (दक्षिण)",
    "The boundaries are Manda (North), Daimabad (South), Sutkagendor (West), and Alamgirpur (East). Mehrgarh is a neolithic site.": "सीमाएँ मांडा (उत्तर), दैमाबाद (दक्षिण), सुतकागेंडोर (पश्चिम) और आलमगीरपुर (पूर्व) हैं। मेहरगढ़ एक नवपाषाण स्थल है।",
    "Which agricultural crop zones were geographically distinct in the Harappan empire? (Select all that apply)": "हड़प्पा साम्राज्य में कौन से कृषि फसल क्षेत्र भौगोलिक रूप से भिन्न थे? (लागू होने वाले सभी विकल्प चुनें)",
    "Wheat and Barley in Punjab/Sindh": "पंजाब/सिंध में गेहूं और जौ", "Rice cultivation in Gujarat (Lothal/Rangpur)": "गुजरात (लोथल/रंगपुर) में धान (चावल) की खेती", "Mustard and Sesame in dry plains": "शुष्क मैदानों में सरसों और तिल", "Sugarcane across Gangetic outposts": "गंगा के बाहरी चौकियों पर गन्ना",
    "Wheat, barley, mustard, sesame, and rice were grown. Sugarcane was not cultivated by Harappans.": "गेहूं, जौ, सरसों, तिल और चावल उगाए जाते थे। हड़प्पावासियों द्वारा गन्ने की खेती नहीं की जाती थी।",

    # S1 True/False
    "The geographical area of the Indus Valley Civilisation was larger than contemporary Egypt and Mesopotamia combined.": "सिंधु घाटी सभ्यता का भौगोलिक क्षेत्र समकालीन मिस्र और मेसोपोटामिया के संयुक्त क्षेत्र से बड़ा था।",
    "True. The IVC covered over 1 million sq km, dwarfing other contemporary civilizations.": "सत्य। सिंधु सभ्यता 10 लाख वर्ग किमी से अधिक क्षेत्र में फैली थी, जो समकालीन सभ्यताओं से बहुत बड़ी थी।",
    "Daimabad, the southernmost limit, is situated on the Godavari River itself.": "दक्षिणी सीमा दैमाबाद सीधे गोदावरी नदी के किनारे स्थित है।",
    "False. It is on the Pravara River, a tributary of the Godavari.": "असत्य। यह गोदावरी की सहायक नदी प्रवरा के किनारे स्थित है।",
    "Shortughai in Afghanistan was established as a major agricultural colony to export wheat to Harappa.": "अफ़गानिस्तान में शॉर्टुघई की स्थापना मुख्य रूप से हड़प्पा को गेहूं निर्यात करने के लिए एक कृषि कॉलोनी के रूप में की गई थी।",
    "False. It was a trading colony established near Badakhshan to directly control the lapis lazuli trade.": "असत्य। यह बदख्शां के पास लाजवर्त (lapis lazuli) के व्यापार को सीधे नियंत्रित करने के लिए स्थापित एक व्यापारिक बस्ती थी।",
    "The Ghaggar-Hakra river basin was completely dry during the entire Mature Harappan period.": "परिपक्व हड़प्पा काल के दौरान घग्गर-हाकड़ा नदी बेसिन पूरी तरह से सूखा हुआ था।",
    "False. The river was perennial during the Mature period and only dried up gradually, causing decline.": "असत्य। परिपक्व काल में नदी बारहमासी थी और बाद में धीरे-धीरे सूख गई, जिससे सभ्यता का पतन हुआ।",
    "Alamgirpur, the easternmost outpost, is located in Meerut district along the Hindon River.": "सबसे पूर्वी चौकी आलमगीरपुर मेरठ जिले में हिंडन नदी के किनारे स्थित है।",
    "True. Alamgirpur marks the easternmost extent of the late phase expansion in western Uttar Pradesh.": "सत्य। आलमगीरपुर पश्चिमी उत्तर प्रदेश में उत्तर हड़प्पा काल के विस्तार की सबसे पूर्वी सीमा को चिह्नित करता है।",
    "The core Harappan region was characterized by heavy tropical monsoon forests.": "मुख्य हड़प्पा क्षेत्र घने उष्णकटिबंधीय मानसूनी जंगलों से घिरा हुआ था।",
    "False. It was a semi-arid zone that relied on river inundation and seasonal alluvial floods.": "असत्य। यह एक अर्ध-शुष्क क्षेत्र था जो नदी के जलभराव और मौसमी जलोढ़ बाढ़ पर निर्भर था।",
    "Balakot in Balochistan was an inland administrative capital without access to the sea.": "बलूचिस्तान में बालाकोट एक अंतर्देशीय प्रशासनिक राजधानी थी जिसकी समुद्र तक कोई पहुँच नहीं थी।",
    "False. Balakot was a coastal site famous for marine shell-working and fishing.": "असत्य। बालाकोट एक तटीय स्थल था जो समुद्री शंख-शिल्प और मछली पकड़ने के लिए प्रसिद्ध था।",
    "Sutkagendor lies on the border between Pakistan and Iran.": "सुतकागेंडोर पाकिस्तान और ईरान की सीमा पर स्थित है।",
    "True. It is located in Pakistani Makran on the edge of the Iranian frontier.": "सत्य। यह ईरानी सीमा के पास पाकिस्तानी मकरान तट पर स्थित है।",

    # S1 Fill Blank
    "The northernmost boundary site of the Indus Valley Civilisation is __________.": "सिंधु घाटी सभ्यता का सबसे उत्तरी सीमा स्थल __________ है।",
    "Manda is located in Jammu and Kashmir.": "मांडा जम्मू और कश्मीर में स्थित है।",
    "The southernmost boundary site of the Indus Valley Civilisation is __________.": "सिंधु घाटी सभ्यता का सबसे दक्षिणी सीमा स्थल __________ है।",
    "Daimabad is in Ahmednagar, Maharashtra.": "दैमाबाद अहमदनगर, महाराष्ट्र में है।",
    "The easternmost boundary site of the Indus Valley Civilisation is __________.": "सिंधु घाटी सभ्यता का सबसे पूर्वी सीमा स्थल __________ है।",
    "Alamgirpur is in Meerut, UP.": "आलमगीरपुर मेरठ, उत्तर प्रदेश में है।",
    "The westernmost boundary site of the Indus Valley Civilisation is __________.": "सिंधु घाटी सभ्यता का सबसे पश्चिमी सीमा स्थल __________ है।",
    "Sutkagendor is in Makran, Balochistan.": "सुतकागेंडोर मकरान, बलूचिस्तान में है।",
    "Shortughai is situated in the modern nation of __________.": "शॉर्टुघई आधुनिक देश __________ में स्थित है।",
    "Shortughai is in northern Afghanistan.": "शॉर्टुघई उत्तरी अफ़गानिस्तान में है।",
    "The dry river bed often identified with the ancient Sarasvati is the __________ channel.": "सूखी नदी घाटी जिसे अक्सर प्राचीन सरस्वती माना जाता है, वह __________ मार्ग है।",
    "The Ghaggar-Hakra river channel matches the description.": "घग्गर-हाकड़ा नदी मार्ग इस विवरण से मेल खाता है।",
    "Sutkagendor is situated on the banks of the __________ River.": "सुतकागेंडोर __________ नदी के किनारे स्थित है।",
    "Sutkagendor is on the Dasht River.": "सुतकागेंडोर दश्त नदी के किनारे है।",
    "The alluvial plains of the Indus were replenished annually by silt deposits from the __________ floods.": "सिंधु के जलोढ़ मैदानों में हर साल __________ बाढ़ से गाद जमा होती थी।",
    "Monsoonal floods in the catchment areas fed the rivers annually.": "जलग्रहण क्षेत्रों में मानसूनी बाढ़ हर साल नदियों में पानी और उपजाऊ मिट्टी लाती थी।",

    # S1 Matching
    "Match the geographical boundary sites of the Indus Civilisation with their respective card directions:": "सिंधु सभ्यता के भौगोलिक सीमा स्थलों को उनके संबंधित दिशाओं से सुमेलित करें:",
    "I. Manda": "I. मांडा", "II. Daimabad": "II. दैमाबाद", "III. Sutkagendor": "III. सुतकागेंडोर",
    "A. Northern Frontier": "A. उत्तरी सीमा", "B. Southern Frontier": "B. दक्षिणी सीमा", "C. Western Frontier": "C. पश्चिमी सीमा",
    "Manda is North, Daimabad is South, and Sutkagendor is West.": "मांडा उत्तर में है, दैमाबाद दक्षिण में है, और सुतकागेंडोर पश्चिम में है।",
    "Match the archaeological sites with their corresponding modern regions/provinces:": "पुरातात्विक स्थलों को उनके संबंधित आधुनिक क्षेत्रों/प्रांतों से सुमेलित करें:",
    "I. Dholavira": "I. धोलावीरा", "II. Rakhigarhi": "II. राखीगढ़ी", "III. Shortughai": "III. शॉर्टुघई",
    "A. Gujarat (Kutch)": "A. गुजरात (कच्छ)", "B. Haryana": "B. हरियाणा", "C. Afghanistan": "C. अफ़गानिस्तान",
    "Dholavira is in Gujarat, Rakhigarhi in Haryana, and Shortughai in Afghanistan.": "धोलावीरा गुजरात में, राखीगढ़ी हरियाणा में और शॉर्टुघई अफ़गानिस्तान में है।",
    "Match the boundary sites with the rivers they are situated along:": "सीमा स्थलों को उन नदियों से सुमेलित करें जिनके किनारे वे स्थित हैं:",
    "I. Alamgirpur": "I. आलमगीरपुर",
    "A. Hindon River": "A. हिंडन नदी", "B. Pravara River": "B. प्रवरा नदी", "C. Dasht River": "C. दश्त नदी",
    "Alamgirpur is on the Hindon, Daimabad on the Pravara, and Sutkagendor on the Dasht.": "आलमगीरपुर हिंडन पर, दैमाबाद प्रवरा पर और सुतकागेंडोर दश्त नदी पर है।",

    # S1 One-Liners
    "What is the approximate total geographic area covered by the Indus Civilisation at its height?": "सिंधु सभ्यता ने अपने चरम पर लगभग कितना कुल भौगोलिक क्षेत्र कवर किया था?",
    "Around 1.3 to 1.5 million square kilometers, forming a huge triangular expanse.": "लगभग 13 से 15 लाख वर्ग किलोमीटर, जो एक विशाल त्रिकोणीय क्षेत्र बनाता था।",
    "Name the geographic pass that provided land trade routes between Balochistan and the Indus plains.": "उस भौगोलिक दर्रे का नाम बताइए जिसने बलूचिस्तान और सिंधु मैदानों के बीच भूमि व्यापार मार्ग प्रदान किया।",
    "The Bolan Pass.": "बोलन दर्रा।",
    "Which modern Indian state has the highest count of Indus Valley sites discovered so far?": "अब तक खोजे गए सिंधु घाटी स्थलों की सर्वाधिक संख्या किस आधुनिक भारतीय राज्य में है?",
    "Gujarat.": "गुजरात।",
    "Name the coastal site near Karachi that is famous for its large shell-working industry.": "कराची के पास स्थित उस तटीय स्थल का नाम बताइए जो अपने बड़े शंख-शिल्प उद्योग के लिए प्रसिद्ध है।",
    "Balakot.": "बालाकोट।",
    "What was the primary type of soil in the Indus basins that sustained their intensive agricultural output?": "सिंधु बेसिन में मुख्य रूप से किस प्रकार की मिट्टी पाई जाती थी जिसने कृषि उत्पादन को सुदृढ़ किया?",
    "Fertile alluvial soil deposited by seasonal river floods.": "नदियों की मौसमी बाढ़ द्वारा जमा की गई उपजाऊ जलोढ़ मिट्टी।",
    "Which mountain ranges define the western geographical boundary of the Indus core plains?": "कौन सी पर्वत श्रृंखलाएं सिंधु के मुख्य मैदानों की पश्चिमी भौगोलिक सीमा को परिभाषित करती करती हैं?",
    "The Kirthar and Sulaiman ranges.": "किर्थर और सुलेमान पर्वत श्रृंखलाएं।",
    "Which site provides direct evidence of maritime trade links on the coastal Makran region?": "मकरान तटीय क्षेत्र पर कौन सा स्थल समुद्री व्यापारिक संपर्कों का प्रत्यक्ष प्रमाण प्रदान करता है?",
    "Sutkagendor.": "सुतकागेंडोर।",
    "What was the navigable channel through which Mesopotamians traded with Meluhha?": "वह नौगम्य जलमार्ग कौन सा था जिसके माध्यम से मेसोपोटामिया के लोग मेलुहा के साथ व्यापार करते थे?",
    "The Persian Gulf / Arabian Sea.": "फ़ारस की खाड़ी / अरब सागर।",

    # S1 Assertion-Reason
    "Assertion (A): The Indus Valley Civilisation expanded in a massive triangular layout.\\nReason (R): This pattern followed the ecological zones of the Indus basin and river deltas, expanding along trade networks.": "कथन (A): सिंधु घाटी सभ्यता का विस्तार एक विशाल त्रिकोणीय आकार में हुआ।\nकारण (R): यह प्रतिरूप सिंधु बेसिन और नदी डेल्टा के पारिस्थितिक क्षेत्रों के अनुकूल था और व्यापार नेटवर्क के साथ फैला।",
    "Both statements are true and R explains A. The shape is a result of geographic and economic expansion.": "दोनों कथन सत्य हैं और कारण कथन की सही व्याख्या है। भौगोलिक और आर्थिक विस्तार के कारण यह आकार बना।",
    "Assertion (A): Shortughai in Afghanistan was established as a temporary wheat farming base.\\nReason (R): Shortughai gave direct access to the Badakhshan lapis lazuli mines and Central Asian metal networks.": "कथन (A): अफ़गानिस्तान में शॉर्टुघई की स्थापना एक अस्थायी गेहूं खेती केंद्र के रूप में की गई थी।\nकारण (R): शॉर्टुघई ने बदख्शां की लाजवर्त खदानों और मध्य एशियाई धातु नेटवर्क तक सीधी पहुँच प्रदान की।",
    "A is false because Shortughai was a permanent trading post, not agricultural. R is true.": "कथन असत्य है क्योंकि शॉर्टुघई एक स्थायी व्यापारिक चौकी थी, न कि कृषि केंद्र। कारण सत्य है।",
    "Assertion (A): The Ghaggar-Hakra river system is often linked with the historical Sarasvati river.\\nReason (R): Satellite imagery and ground studies confirm a dense network of ancient settlements along its dry channel.": "कथन (A): घग्गर-हाकड़ा नदी प्रणाली को अक्सर ऐतिहासिक सरस्वती नदी से जोड़ा जाता है।\nकारण (R): उपग्रह चित्रों और मैदानी अध्ययनों से इसके सूखे मार्ग के किनारे प्राचीन बस्तियों के घने नेटवर्क की पुष्टि होती है।",
    "Both are true and R explains why the Ghaggar-Hakra basin is associated with the core heartland.": "दोनों सत्य हैं और कारण सही व्याख्या करता है कि क्यों इस बेसिन को सभ्यता के मुख्य केंद्र से जोड़ा जाता है।",
    "Assertion (A): Daimabad marks the southernmost limit of the Harappan expansion.\\nReason (R): Harappans migrated southwards to Maharashtra during the Late phase, settling in the Godavari basin.": "कथन (A): दैमाबाद हड़प्पा सभ्यता के विस्तार की सबसे दक्षिणी सीमा को चिह्नित करता है।\nकारण (R): उत्तर हड़प्पा चरण के दौरान हड़प्पावासी दक्षिण की ओर महाराष्ट्र में स्थानांतरित हुए और गोदावरी बेसिन में बस गए।",
    "Both are true and R explains the Late Harappan southern shift.": "दोनों सत्य हैं और कारण उत्तर हड़प्पा काल में दक्षिण की ओर हुए पलायन की सही व्याख्या करता है।",
    "Assertion (A): Sutkagendor was equipped with a massive brick-built dockyard.\\nReason (R): Sutkagendor was a fortified trade outpost built on a rocky cliff rather than an inland tidal basin.": "कथन (A): सुतकागेंडोर पकी ईंटों से बने एक विशाल गोदीवाड़े (dockyard) से सुसज्जित था।\nकारण (R): सुतकागेंडोर एक चट्टानी पहाड़ी पर बना एक मजबूत व्यापारिक किला था, न कि पानी से घिरा ज्वारीय बेसिन।",
    "Assertion is false: Sutkagendor did not have a dockyard like Lothal. Reason is true.": "कथन असत्य है: सुतकागेंडोर में लोथल की तरह कोई गोदीवाड़ा नहीं था। कारण सत्य है।",
    "Assertion (A): The Indus Valley plain was prone to tectonic uplifts.\\nReason (R): Tectonic changes diverted rivers like the Yamuna and Sutlej, causing drying of the Ghaggar and flooding of the Indus.": "कथन (A): सिंधु घाटी का मैदानी क्षेत्र विवर्तनिक (tectonic) हलचलों के प्रति संवेदनशील था।\nकारण (R): विवर्तनिक बदलावों ने यमुना और सतलज जैसी नदियों का मार्ग बदल दिया, जिससे घग्गर सूख गई और सिंधु में बाढ़ आ गई।",
    "Both are true and R explains the geographical impact of tectonic uplifts.": "दोनों सत्य हैं और कारण विवर्तनिक हलचलों के भौगोलिक प्रभाव की सही व्याख्या करता है।",
    "Assertion (A): Alamgirpur shows a complete lack of public brick-built street drains.\\nReason (R): Alamgirpur was a Late Harappan peripheral village where civic planning standards had degraded.": "कथन (A): आलमगीरपुर की सड़कों पर पकी ईंटों से बनी सार्वजनिक नालियों का पूर्ण अभाव दिखाई देता है।\nकारण (R): आलमगीरपुर एक उत्तर हड़प्पा कालीन बाहरी गाँव था जहाँ नागरिक नियोजन के मानकों में गिरावट आ गई थी।",
    "Both are true and R explains the decay in civic standards at the periphery.": "दोनों सत्य हैं और कारण बाहरी क्षेत्रों में नागरिक नियोजन मानकों में गिरावट की सही व्याख्या करता है।",
    "Assertion (A): The core regions of the IVC were located in heavy tropical rainfall zones.\\nReason (R): Harappans relied on seasonal river inundation and mud embankments rather than rainfall for farming.": "कथन (A): सिंधु सभ्यता का मुख्य क्षेत्र भारी उष्णकटिबंधीय वर्षा वाले क्षेत्रों में स्थित था।\nकारण (R): हड़प्पावासी खेती के लिए वर्षा के बजाय मौसमी बाढ़ के पानी और मिट्टी के तटबंधों पर निर्भर थे।",
    "A is false because the core was semi-arid. R is true.": "कथन असत्य है क्योंकि मुख्य क्षेत्र अर्ध-शुष्क था। कारण सत्य है।",

    # S1 Statement-Based
    "Consider the following statements regarding the boundary outposts:\\n1. Manda in the north was situated on the Chenab River.\\n2. Daimabad in the south was situated on the Pravara River.\\nWhich of the statements given above is/are correct?": "सीमा चौकियों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. उत्तर में स्थित मांडा चिनाब नदी के किनारे था।\n2. दक्षिण में स्थित दैमाबाद प्रवरा नदी के किनारे था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
    "Both statements are correct.": "दोनों कथन सही हैं।",
    "Consider the following statements regarding the geography of Gujarat sites:\\n1. Lothal was located at the head of the Gulf of Khambhat on the Bhogavo River.\\n2. Dholavira was built in the salt flats of the Rann of Kutch on Khadir Bet island.\\nWhich of the statements given above is/are correct?": "गुजरात के स्थलों के भूगोल के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. लोथल खंभात की खाड़ी के शीर्ष पर भोगवो नदी के किनारे स्थित था।\n2. धोलावीरा कच्छ के रण के खारे मैदान में खादिर बेट द्वीप पर बनाया गया था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
    "Both statements are correct. These represent two different maritime ecological settings.": "दोनों कथन सही हैं। ये दो अलग-अलग समुद्री पारिस्थितिक व्यवस्था को दर्शाते हैं।",
    "Consider the following statements regarding the Cholistan desert:\\n1. It contains the highest concentration of Hakra and early Harappan settlements.\\n2. The Ghaggar-Hakra river system was completely dry throughout the Mature Harappan phase.\\nWhich of the statements given above is/are correct?": "चोलिस्तान रेगिस्तान के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. इसमें हाकड़ा और प्रारंभिक हड़प्पा बस्तियों का उच्चतम संकेंद्रण है।\n2. घग्गर-हाकड़ा नदी प्रणाली परिपक्व हड़प्पा काल के दौरान पूरी तरह से सूखी हुई थी।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
    "Statement 2 is incorrect. The river was active during the Mature phase and dried up later.": "कथन 2 गलत है। परिपक्व चरण में नदी सक्रिय थी और बाद में सूखी।",
    "Consider the following statements regarding the climatic context of IVC:\\n1. The core Indus region received heavy monsoonal rain similar to the Ganga Valley.\\n2. The climate was semi-arid, requiring seasonal floodwater management for crops.\\nWhich of the statements given above is/are correct?": "सिंधु सभ्यता के जलवायु संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मुख्य सिंधु क्षेत्र में गंगा घाटी की तरह भारी मानसूनी वर्षा होती थी।\n2. यहाँ की जलवायु अर्ध-शुष्क थी, जिससे फसलों के लिए मौसमी बाढ़ के पानी का प्रबंधन आवश्यक था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
    "Only statement 2 is correct. The region was semi-arid.": "केवल कथन 2 सही है। यह क्षेत्र अर्ध-शुष्क था।",
    "Consider the following statements regarding the Shortughai outpost:\\n1. It is situated in northern Afghanistan near the Oxus (Amu Darya) River.\\n2. It was established primarily to control the export of copper from Khetri mines.\\nWhich of the statements given above is/are correct?": "शॉर्टुघई चौकी के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. यह उत्तरी अफ़गानिस्तान में ऑक्सस (अमु दरिया) नदी के पास स्थित है।\n2. इसकी स्थापना मुख्य रूप से खेतड़ी खदानों से तांबे के निर्यात को नियंत्रित करने के लिए की गई थी।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
    "Statement 2 is incorrect. Khetri is in Rajasthan; Shortughai controlled lapis lazuli from Badakhshan.": "कथन 2 गलत है। खेतड़ी राजस्थान में है; शॉर्टुघई बदख्शां से लाजवर्त व्यापार को नियंत्रित करता था।",

    # S1 Conceptual
    "Why did the Harappans establish peripheral outposts like Shortughai and Sutkagendor?": "हड़प्पावासियों ने शॉर्टुघई और सुतकागेंडोर जैसी बाहरी चौकियां क्यों स्थापित की थीं?",
    "To secure strategic trade routes and monopolize rare raw materials: Shortughai for lapis lazuli/copper from Central Asia, and Sutkagendor to control sea trade with Mesopotamia.": "रणनीतिक व्यापार मार्गों को सुरक्षित करने और दुर्लभ कच्चे माल पर एकाधिकार स्थापित करने के लिए: शॉर्टुघई मध्य एशिया से लाजवर्त/तांबे के लिए, और सुतकागेंडोर मेसोपोटामिया के साथ समुद्री व्यापार को नियंत्रित करने के लिए।",
    "Why is the Ghaggar-Hakra river valley called the heartland of the Indus Civilisation?": "घग्गर-हाकड़ा नदी घाटी को सिंधु सभ्यता का मुख्य केंद्र (हार्टलैंड) क्यों कहा जाता है?",
    "Because over 60% of all discovered IVC sites lie along this dry basin, indicating it supported the largest agricultural and urban population density.": "क्योंकि खोजे गए सभी सिंधु स्थलों में से 60% से अधिक इस सूखे बेसिन के किनारे स्थित हैं, जो यह दर्शाता है कि इसने सबसे बड़े कृषि और शहरी जनसंख्या घनत्व को सहारा दिया।",
    "Why was the geographical location of Dholavira in the Rann of Kutch highly strategic?": "कच्छ के रण में धोलावीरा की भौगोलिक स्थिति अत्यधिक रणनीतिक क्यों थी?",
    "During the Bronze Age, the Rann was a navigable sea gulf. Dholavira acted as a massive island fortress controlling maritime trade coming from the Arabian Sea.": "कांस्य युग के दौरान, रण एक नौगम्य समुद्री खाड़ी था। धोलावीरा ने अरब सागर से आने वाले समुद्री व्यापार को नियंत्रित करने वाले एक विशाल द्वीप किले के रूप में काम किया।",
    "How did river course migrations alter the geography of Harappan cities?": "नदियों के मार्ग परिवर्तन ने हड़प्पा के शहरों के भूगोल को कैसे बदल दिया?",
    "Shifting rivers left cities stranded away from water or submerged them in floods, forcing populations to migrate and leading to de-urbanization.": "नदियों के मार्ग बदलने से शहर पानी से दूर हो गए या बाढ़ में डूब गए, जिससे आबादी को पलायन करने के लिए मजबूर होना पड़ा और वि-शहरीकरण हुआ।",
    "How did the geographical location of Sutkagendor aid maritime trade?": "सुतकागेंडोर की भौगोलिक स्थिति ने समुद्री व्यापार में किस प्रकार सहायता की?",
    "It served as a protected coastal port and watering station on the Makran coast, acting as a bridge between the Indus valley and the Persian Gulf.": "यह मकरान तट पर एक सुरक्षित तटीय बंदरगाह और मीठे पानी के केंद्र के रूप में कार्य करता था, जो सिंधु घाटी और फ़ारस की खाड़ी के बीच एक सेतु का काम करता था।",
    "How did the alluvial ecology of the Indus Basin shape the Harappan crop cycle?": "सिंधु बेसिन की जलोढ़ पारिस्थितिकी ने हड़प्पा की फसल चक्र को कैसे आकार दिया?",
    "Annual river floods deposited fertile silt. Harappans sowed crops (wheat/barley) in winter as floodwaters receded and harvested them in spring without complex canals.": "वार्षिक नदी बाढ़ ने उपजाऊ गाद जमा की। हड़प्पावासियों ने सर्दियों में बाढ़ का पानी कम होने पर फसलें (गेहूं/जौ) बोईं और बिना जटिल नहरों के वसंत में उनकी कटाई की।",
    "Case Study: The Shortughai Trade Outpost": "केस स्टडी: शॉर्टुघई व्यापारिक चौकी",
    "A Harappan settlement in northern Afghanistan. It shows classic Harappan bricks, pottery, and seals, proving the state established long-distance enclaves to control the lapis lazuli trade of Badakhshan.": "उत्तरी अफ़गानिस्तान में एक हड़प्पाई बस्ती। यह क्लासिक हड़प्पा ईंटें, मिट्टी के बर्तन और मुहरें दिखाता है, जिससे साबित होता है कि राज्य ने बदख्शां के लाजवर्त व्यापार को नियंत्रित करने के लिए दूरदराज के क्षेत्र में चौकियां स्थापित की थीं।",
    "Case Study: The Drying of the Ghaggar-Hakra River": "केस स्टडी: घग्गर-हाकड़ा नदी का सूखना",
    "Tectonic shifts diverted the Sutlej into the Indus and the Yamuna into the Ganga. This cut off the water source of the Ghaggar-Hakra, turning it into a seasonal dry channel and leading to the abandonment of cities like Kalibangan.": "विवर्तनिक बदलावों ने सतलज को सिंधु में और यमुना को गंगा में मोड़ दिया। इसने घग्गर-हाकड़ा के जल स्रोत को काट दिया, इसे एक मौसमी सूखे मार्ग में बदल दिया और कालीबंगन जैसे शहरों को छोड़ने के लिए मजबूर किया।",
    "Case Study: Daimabad Peripheral Expansion": "केस स्टडी: दैमाबाद का बाहरी विस्तार",
    "Daimabad in Maharashtra yields late Harappan pottery and a massive copper/bronze hoard. It demonstrates that as the core cities declined, populations migrated southwards, expanding the cultural footprint.": "महाराष्ट्र के दैमाबाद से उत्तर हड़प्पा काल के मिट्टी के बर्तन और तांबे/कांसे का विशाल भंडार मिला है। यह दर्शाता है कि जैसे-जैसे मुख्य शहरों का पतन हुआ, आबादी दक्षिण की ओर चली गई, जिससे संस्कृति का भौगोलिक विस्तार हुआ।",
    "Teach the Concept: The Harappan Geographical Quadrangle": "अवधारणा को समझें: हड़प्पा सभ्यता का भौगोलिक चतुर्भुज",
    "Teach the four boundary markers of the civilization at its peak: Manda (North, J&K), Daimabad (South, Maharashtra), Alamgirpur (East, UP), and Sutkagendor (West, Balochistan), covering 1.5 million sq km.": "सभ्यता के चरम पर इसके चार सीमा चिह्नों को समझें: मांडा (उत्तर, जम्मू-कश्मीर), दैमाबाद (दक्षिण, महाराष्ट्र), आलमगीरपुर (पूर्व, उत्तर प्रदेश), और सुतकागेंडोर (पश्चिम, बलूचिस्तान), जो लगभग 15 लाख वर्ग किमी में फैला था।",
    "Teach the Concept: Alluvial Floodplain Farming": "अवधारणा को समझें: जलोढ़ बाढ़ के मैदानों में खेती",
    "Explain that Harappan agriculture was not dependent on canal irrigation or heavy rainfall, but on exploiting the natural flood cycles of the Indus system, utilizing soft alluvial soil for easy plowing.": "समझाएं कि हड़प्पा की कृषि नहर सिंचाई या भारी वर्षा पर निर्भर नहीं थी, बल्कि सिंधु प्रणाली के प्राकृतिक बाढ़ चक्रों का उपयोग करने पर आधारित थी, जिसमें जुताई के लिए नरम जलोढ़ मिट्टी का लाभ उठाया जाता था।",
    "Teach the Concept: Coastal Maritime Gateway Sites": "अवधारणा को समझें: तटीय समुद्री प्रवेश द्वार स्थल",
    "Explain how coastal sites like Lothal, Sutkagendor, Balakot, and Kuntasi formed a maritime network that supported fish exports, shell-craft production, and shipping links to Mesopotamia.": "समझाएं कि कैसे लोथल, सुतकागेंडोर, बालाकोट और कुंतासी जैसे तटीय स्थलों ने एक समुद्री नेटवर्क बनाया जो मछली निर्यात, शंख-शिल्प उत्पादन और मेसोपोटामिया के साथ जहाजरानी संपर्कों का समर्थन करता था।",

    # Section 2 Qs
    "Which of the following Mature Harappan cities is divided into three distinct parts: a Citadel, a Middle Town, and a Lower Town?": "निम्नलिखित में से कौन सा परिपक्व हड़प्पा शहर तीन अलग-अलग भागों में विभाजित है: एक दुर्ग (Citadel), एक मध्य नगर (Middle Town), और एक निचला नगर (Lower Town)?",
    "Harappa": "हड़प्पा", "Mohenjo-daro": "मोहनजोदड़ो", "Dholavira": "धोलावीरा", "Kalibangan": "कालीबंगन",
    "Dholavira is unique for its three-tier town planning, whereas most other cities have a two-tier division.": "धोलावीरा अपने त्रि-स्तरीय नगर नियोजन के लिए अद्वितीय है, जबकि अन्य अधिकांश शहरों में दो-स्तरीय विभाजन है।",
    "The famous artificial baked-brick dockyard connected to a river channel was discovered at which site?": "नदी के मार्ग से जुड़ा पकी ईंटों का प्रसिद्ध कृत्रिम गोदीवाड़ा (dockyard) किस स्थल पर खोजा गया था?",
    "Kuntasi": "कुंतासी",
    "Lothal in Gujarat contains a massive baked-brick dockyard connected to a channel of the Bhogavo River.": "गुजरात के लोथल में भोगवो नदी की एक धारा से जुड़ा पकी ईंटों का एक विशाल गोदीवाड़ा स्थित है।",
    "Which of the following sites is famous for yielding a terracotta model of a plow, showing agricultural practices?": "कृषि पद्धतियों को दर्शाने वाला, मिट्टी (terracotta) का बना हल का खिलौना किस स्थल से प्राप्त हुआ था?",
    "Rakhigarhi": "राखीगढ़ी",
    "Banawali in Fatehabad district, Haryana, yielded a well-preserved terracotta model of a agricultural plow.": "हरियाणा के फतेहाबाद जिले के बनावली से मिट्टी के हल का एक अच्छी तरह से संरक्षित मॉडल मिला है।",
    "Which major Harappan industrial center shows a complete absence of a fortified administrative citadel?": "कौन सा प्रमुख हड़प्पा औद्योगिक केंद्र एक किलेबंद प्रशासनिक दुर्ग के पूर्ण अभाव को दर्शाता है?",
    "Chanhudaro": "चन्हुदड़ो",
    "Chanhudaro in Sindh was a dedicated industrial town famous for craft and bead factories, and lacks a citadel.": "सिंध का चन्हुदड़ो मनके और शिल्प के कारखानों के लिए प्रसिद्ध एक समर्पित औद्योगिक नगर था, जहाँ दुर्ग नहीं मिला है।",
    "Rakhigarhi, currently recognized as the largest geographic site of the Indus Valley Civilisation, is located in which state?": "वर्तमान में सिंधु घाटी सभ्यता का सबसे बड़ा भौगोलिक स्थल माना जाने वाला राखीगढ़ी किस राज्य में स्थित है?",
    "Haryana": "हरियाणा",
    "Rakhigarhi is in Hisar district, Haryana, and covers over 350 hectares.": "राखीगढ़ी हरियाणा के हिसार जिले में स्थित है और यह 350 हेक्टेयर से अधिक में फैला है।",

    # S2 Multi-Correct
    "Identify the architectural and archaeological discoveries associated with Dholavira: (Select all that apply)": "धोलावीरा से जुड़ी वास्तुकला और पुरातात्विक खोजों की पहचान करें: (लागू होने वाले सभी विकल्प चुनें)",
    "Massive stone water reservoirs": "विशाल पत्थर के जलाशय", "A signboard with ten large Indus script characters": "दस बड़े सिंधु लिपि अक्षरों वाला जिप्सम साइनबोर्ड", "A three-tier town layout": "त्रि-स्तरीय नगर नियोजन", "An artificial brick dockyard": "एक कृत्रिम ईंट का गोदीवाड़ा",
    "Dholavira has stone reservoirs, a ten-character signboard, and a three-tier layout. Lothal contains the dockyard.": "धोलावीरा में पत्थर के जलाशय, दस अक्षरों वाला साइनबोर्ड और त्रि-स्तरीय नगर नियोजन है। लोथल में गोदीवाड़ा है।",
    "Which of the following sites contain evidence of fire altars, indicating ritual activity? (Select all that apply)": "निम्नलिखित में से किन स्थलों पर अग्निवेदियों (fire altars) के साक्ष्य मिले हैं, जो धार्मिक अनुष्ठान के संकेत हैं? (लागू होने वाले सभी विकल्प चुनें)",
    "Fire altars have been found at Kalibangan, Lothal, and Banawali. They are absent at Mohenjo-daro.": "कालीबंगन, लोथल और बनावली से अग्निवेदियाँ मिली हैं। ये मोहनजोदड़ो में अनुपस्थित हैं।",
    "Select the coastal ports and maritime centers of the Harappan civilization: (Select all that apply)": "हड़प्पा सभ्यता के तटीय बंदरगाहों और समुद्री केंद्रों का चयन करें: (लागू होने वाले सभी विकल्प चुनें)",
    "Lothal, Kuntasi, and Sutkagendor are coastal ports. Chanhudaro is an inland industrial site.": "लोथल, कुंतासी और सुतकागेंडोर तटीय बंदरगाह हैं। चन्हुदड़ो एक अंतर्देशीय औद्योगिक स्थल है।",
    "Which sites show evidence of pre-mature (Early Harappan) agricultural activities? (Select all that apply)": "किन स्थलों पर पूर्व-परिपक्व (प्रारंभिक हड़प्पा) कृषि गतिविधियों के साक्ष्य मिले हैं? (लागू होने वाले सभी विकल्प चुनें)",
    "Kalibangan (ploughed field)": "कालीबंगन (जुता हुआ खेत)", "Bhirrana (Hakra levels)": "भिरड़ाना (हाकड़ा स्तर)", "Mehrgarh (Neolithic farming)": "मेहरगढ़ (नवपाषाण कालीन कृषि)", "Lothal (dockyard)": "लोथल (गोदीवाड़ा)",
    "Kalibangan, Bhirrana, and Mehrgarh have early farming levels. Lothal is a Mature/Late phase port city.": "कालीबंगन, भिरड़ाना और मेहरगढ़ में प्रारंभिक कृषि स्तर हैं। लोथल एक परिपक्व/उत्तर चरण का बंदरगाह शहर है।",
    "Identify the major public structures excavated at Mohenjo-daro: (Select all that apply)": "मोहनजोदड़ो में उत्खनित प्रमुख सार्वजनिक संरचनाओं की पहचान करें: (लागू होने वाले सभी विकल्प चुनें)",
    "The Great Bath": "विशाल स्नानागार", "The Great Granary": "विशाल अन्नागार", "Assembly Hall of columns": "खंभों वाला विशाल सभा भवन", "A stone dockyard": "पत्थर का गोदीवाड़ा",
    "Mohenjo-daro contains the Great Bath, Great Granary, and Assembly Hall. Lothal contains the dockyard.": "मोहनजोदड़ो में विशाल स्नानागार, विशाल अन्नागार और स्तंभों वाला सभा भवन है। लोथल में गोदीवाड़ा है।",

    # S2 True/False
    "Mohenjo-daro literally means 'Mound of the Dead' in the Sindhi language.": "सिंधी भाषा में मोहनजोदड़ो का शाब्दिक अर्थ 'मृतकों का टीला' है।",
    "True. R.D. Banerji discovered the site under this local name.": "सत्य। आर.डी. बनर्जी ने इस स्थानीय नाम के तहत स्थल की खोज की थी।",
    "Lothal's dockyard basin was constructed using sun-dried mud-bricks.": "लोथल के गोदी बाड़े का निर्माण धूप में सुखाए गए कच्चे कीचड़ की ईंटों से किया गया था।",
    "False. It was built using high-quality baked bricks to withstand tidal water pressure.": "असत्य। ज्वारीय पानी के दबाव को झेलने के लिए इसका निर्माण उच्च गुणवत्ता वाली पकी ईंटों से किया गया था।",
    "Chanhudaro was a major administrative capital containing a large royal palace.": "चन्हुदड़ो एक प्रमुख प्रशासनिक राजधानी थी जिसमें एक बड़ा शाही महल स्थित था।",
    "False. It was a craft center with no citadel or palace structures.": "असत्य। यह बिना प्रशासनिक दुर्ग या महल संरचनाओं वाला एक शिल्प/औद्योगिक केंद्र था।",
    "Kalibangan is famous for yielding the earliest ploughed field in the subcontinent.": "कालीबंगन उपमहाद्वीप में सबसे पुराना जुता हुआ खेत देने के लिए प्रसिद्ध है।",
    "True. The criss-cross ploughed field belongs to the pre-mature Early Harappan phase.": "सत्य। आड़े-तिरछे जुते हुए खेत का साक्ष्य पूर्व-परिपक्व प्रारंभिक हड़प्पा चरण से संबंधित है।",
    "Banawali yielded a terracotta toy model of a plow.": "बनावली से मिट्टी का बना हल का खिलौना प्राप्त हुआ था।",
    "True. This discovery confirms that wooden plows were used for farming.": "सत्य। यह खोज पुष्टि करती है कि खेती के लिए लकड़ी के हलों का उपयोग किया जाता था।",
    "Dholavira's city walls were made entirely of mud-bricks without stone.": "धोलावीरा के शहर की दीवारें बिना पत्थर के पूरी तरह से मिट्टी की ईंटों से बनी थीं।",
    "False. Dholavira is famous for its extensive use of local stone in fortifications.": "असत्य। धोलावीरा किलेबंदी में स्थानीय पत्थर के व्यापक उपयोग के लिए प्रसिद्ध है।",
    "Rakhigarhi in Haryana has been declared the largest site of the Indus Valley Civilisation by area.": "हरियाणा के राखीगढ़ी को क्षेत्रफल की दृष्टि से सिंधु घाटी सभ्यता का सबसे बड़ा स्थल घोषित किया गया है।",
    "True. Recent excavations show it is larger than Mohenjo-daro and Harappa.": "सत्य। हाल के उत्खननों से पता चलता है कि यह मोहनजोदड़ो और हड़प्पा से भी बड़ा है।",
    "All Harappan towns were divided into exactly two fortified sections.": "सभी हड़प्पा शहर बिल्कुल दो किलेबंद भागों में विभाजित थे।",
    "False. Dholavira is divided into three sections: Citadel, Middle Town, and Lower Town.": "असत्य। धोलावीरा तीन भागों में विभाजित है: दुर्ग (Citadel), मध्य नगर (Middle Town) और निचला नगर (Lower Town)।",

    # S2 Fill Blank
    "Mohenjo-daro is situated on the banks of the __________ River.": "मोहनजोदड़ो __________ नदी के किनारे स्थित है।",
    "Mohenjo-daro lies in Sindh along the Indus River.": "मोहनजोदड़ो सिंध में सिंधु नदी के किनारे स्थित है।",
    "The largest site of the Indus Valley Civilisation by geographic area is __________.": "भौगोलिक क्षेत्र की दृष्टि से सिंधु घाटी सभ्यता का सबसे बड़ा स्थल __________ है।",
    "Rakhigarhi in Haryana is the largest site.": "हरियाणा का राखीगढ़ी सबसे बड़ा स्थल है।",
    "The Harappan city uniquely divided into three parts is __________.": "अद्वितीय रूप से तीन भागों में विभाजित हड़प्पा का शहर __________ है।",
    "Dholavira in Gujarat features three divisions.": "गुजरात के धोलावीरा में तीन विभाजन हैं।",
    "A terracotta model of an agricultural plow was excavated at __________.": "कृषि में प्रयुक्त हल का मिट्टी का खिलौना __________ पर उत्खनित किया गया था।",
    "Banawali yielded the clay plow model.": "बनावली से मिट्टी का हल प्राप्त हुआ था।",
    "The port site of Lothal was excavated by the archaeologist __________.": "लोथल बंदरगाह स्थल का उत्खनन पुरातत्वविद् __________ द्वारा किया गया था।",
    "S.R. Rao excavated Lothal in 1954.": "एस.आर. राव ने 1954 में लोथल का उत्खनन किया था।",
    "Fire altars indicating ritual sacrifices have been found at Lothal and __________.": "धार्मिक अनुष्ठानों को दर्शाने वाली अग्निवेदियाँ लोथल और __________ में पाई गई हैं।",
    "Kalibangan has a row of seven fire altars.": "कालीबंगन में सात अग्निवेदियों की एक पंक्ति मिली है।",
    "Chanhudaro was a major manufacturing center for __________ beads.": "चन्हुदड़ो __________ के मनके (beads) बनाने का एक प्रमुख केंद्र था।",
    "Carnelian beads were made in craft factories at Chanhudaro.": "चन्हुदड़ो के शिल्प कारखानों में अकीक (carnelian) के मनके बनाए जाते थे।",
    "The city of Harappa is located on the banks of the __________ River.": "हड़प्पा शहर __________ नदी के किनारे स्थित है।",
    "Harappa lies along the Ravi River in Punjab, Pakistan.": "हड़प्पा पंजाब, पाकिस्तान में रावी नदी के किनारे स्थित है।",

    # S2 Matching
    "Match the Indus Valley sites with their pioneer archaeological excavators:": "सिंधु घाटी के स्थलों को उनके अग्रणी पुरातात्विक उत्खननकर्ताओं से सुमेलित करें:",
    "A. Daya Ram Sahni": "A. दयाराम साहनी", "B. R.D. Banerji": "B. आर.डी. बनर्जी", "C. S.R. Rao": "C. एस.आर. राव",
    "Harappa was excavated by Sahni, Mohenjo-daro by Banerji, and Lothal by Rao.": "हड़प्पा का उत्खनन साहनी द्वारा, मोहनजोदड़ो का बनर्जी द्वारा और लोथल का राव द्वारा किया गया था।",
    "Match the major Harappan towns with their unique architectural features/discoveries:": "प्रमुख हड़प्पा शहरों को उनकी अनूठी वास्तुकला विशेषताओं/खोजों से सुमेलित करें:",
    "A. The Great Bath": "A. विशाल स्नानागार", "B. Giant stone reservoirs and signboard": "B. विशाल पत्थर के जलाशय और साइनबोर्ड", "C. Baked-brick dockyard": "C. पकी ईंटों का गोदीवाड़ा",
    "Mohenjo-daro has the Great Bath, Dholavira has stone reservoirs, and Lothal has the dockyard.": "मोहनजोदड़ो में विशाल स्नानागार, धोलावीरा में पत्थर के जलाशय और लोथल में गोदीवाड़ा है।",
    "Match the Harappan settlements with the rivers they are situated along:": "हड़प्पा बस्तियों को उन नदियों से सुमेलित करें जिनके किनारे वे स्थित हैं:",
    "A. Ravi River": "A. रावी नदी", "B. Indus River": "B. सिंधु नदी", "C. Bhogavo River": "C. भोगवो नदी",
    "Harappa is on the Ravi, Mohenjo-daro on the Indus, and Lothal on the Bhogavo.": "हड़प्पा रावी पर, मोहनजोदड़ो सिंधु पर और लोथल भोगवो के किनारे है।",

    # S2 One-Liners
    "Which site is known as the industrial craft suburb of Mohenjo-daro due to its bead factories?": "मनके के कारखानों के कारण किस स्थल को मोहनजोदड़ो का औद्योगिक शिल्प उपनगर कहा जाता है?",
    "Chanhudaro in Sindh.": "सिंध में चन्हुदड़ो।",
    "Name the Harappan site where a wooden coffin burial (indicating international contacts) was found.": "उस हड़प्पा स्थल का नाम बताइए जहाँ लकड़ी के ताबूत में शवाधान (अंतरराष्ट्रीय संपर्कों का संकेत) पाया गया था।",
    "Harappa (Cemetery R-37).": "हड़प्पा (कब्रिस्तान R-37)।",
    "Which site contains the earliest direct evidence of cotton cultivation in the ancient world?": "प्राचीन विश्व में कपास की खेती का सबसे पहला प्रत्यक्ष प्रमाण किस स्थल से मिला है?",
    "Mohenjo-daro (woven cotton scrap on a silver jar).": "मोहनजोदड़ो (एक चांदी के बर्तन पर बुने हुए कपास का टुकड़ा)।",
    "In which modern Indian state is the massive site of Rakhigarhi located?": "हरियाणा के किस जिले में विशाल राखीगढ़ी स्थल स्थित है?",
    "Haryana (Hisar district).": "हरियाणा (हिसार जिला)।",
    "Name the port site that yielded copper oxhide ingots, showing trade connections with the Persian Gulf.": "उस बंदरगाह स्थल का नाम बताइए जिससे तांबे की सिल्लियाँ मिली थीं, जो फ़ारस की खाड़ी के साथ व्यापारिक संबंधों को दर्शाती हैं।",
    "Lothal.": "लोथल।",
    "Which site uniquely showed that almost every house had its own brick-lined water well?": "किस स्थल ने विशिष्ट रूप से दिखाया कि लगभग हर घर में ईंटों से बना अपना कुआँ था?",
    "Mohenjo-daro.": "मोहनजोदड़ो।",
    "What is the name of the river tributary along which Lothal is situated?": "उस नदी की सहायक नदी का क्या नाम है जिसके किनारे लोथल स्थित है?",
    "The Bhogavo River (tributary of the Sabarmati).": "भोगवो नदी (साबरमती की सहायक नदी)।",
    "At which site in Gujarat were bones and skeletal remains of a horse reported?": "गुजरात के किस स्थल पर घोड़े की हड्डियों और कंकाल के अवशेष मिलने की सूचना मिली थी?",
    "Surkotada.": "सुरकोटदा।",

    # S2 Assertion-Reason
    "Assertion (A): Mohenjo-daro was rebuilt at least seven times on top of older ruins.\\nReason (R): The city was situated on the Indus floodplain and was repeatedly devastated by massive river floods.": "कथन (A): मोहनजोदड़ो को पुरानी खंडहरों के ऊपर कम से कम सात बार पुनर्निर्मित किया गया था।\nकारण (R): यह शहर सिंधु के बाढ़ के मैदान में स्थित था और बार-बार भीषण बाढ़ से तबाह होता था।",
    "Both A and R are true and R explains A. Silt deposits show repeated flood rebuilding cycles.": "दोनों कथन सत्य हैं और कारण कथन की सही व्याख्या है। गाद के जमाव बार-बार बाढ़ आने के चक्र को दर्शाते हैं।",
    "Assertion (A): Chanhudaro was a heavily fortified administrative city housing elite rulers.\\nReason (R): The site lacks a defensive wall or citadel and is packed with bead workshops and metal smelters.": "कथन (A): चन्हुदड़ो कुलीन शासकों का निवास स्थान, एक अत्यधिक किलेबंद प्रशासनिक शहर था।\nकारण (R): इस स्थल पर किसी रक्षात्मक दीवार या दुर्ग का अभाव है और यह मनके की कार्यशालाओं तथा धातु भट्टी से भरा है।",
    "A is false because Chanhudaro was an unfortified industrial suburb. R is true.": "कथन असत्य है क्योंकि चन्हुदड़ो बिना किले वाला एक औद्योगिक उपनगर था। कारण सत्य है।",
    "Assertion (A): Dholavira utilized massive stone masonry for its fortification walls.\\nReason (R): Local sandstone quarries in Kutch provided abundant stone, whereas brick-clay was scarce.": "कथन (A): धोलावीरा ने अपनी किलेबंदी की दीवारों के लिए विशाल पत्थर की चिनाई का उपयोग किया।\nकारण (R): कच्छ में स्थानीय बलुआ पत्थर की खदानों ने प्रचुर मात्रा में पत्थर प्रदान किए, जबकि ईंट बनाने की मिट्टी दुर्लभ थी।",
    "Both A and R are true and R explains A. Geography influenced Dholavira's stone architecture.": "दोनों कथन सत्य हैं और कारण कथन की सही व्याख्या है। भूगोल ने धोलावीरा की पत्थर की वास्तुकला को प्रभावित किया।",
    "Assertion (A): Lothal served as a major maritime trading hub for the Harappan empire.\\nReason (R): Archaeologists excavated a massive baked-brick basin linked to a river channel and Persian Gulf button seals at Lothal.": "कथन (A): लोथल ने हड़प्पा साम्राज्य के लिए एक प्रमुख समुद्री व्यापारिक केंद्र के रूप में कार्य किया।\nकारण (R): पुरातत्वविदों ने लोथल से नदी मार्ग से जुड़ा एक विशाल पकी ईंटों का बेसिन और फ़ारस की खाड़ी की बटन मुहरें खोजीं।",
    "Both are true and R explains A. The dockyard and seals prove its international port status.": "दोनों सत्य हैं और कारण कथन की सही व्याख्या है। गोदीवाड़ा और मुहरें इसके अंतरराष्ट्रीय बंदरगाह होने को प्रमाणित करते हैं।",
    "Assertion (A): Kalibangan houses were constructed using sun-dried mud bricks instead of baked bricks.\\nReason (R): Kalibangan lacked easy access to dense forests to bake bricks, relying on sun-drying.": "कथन (A): कालीबंगन के घरों का निर्माण पकी ईंटों के बजाय धूप में सुखाई गई मिट्टी की ईंटों से किया गया था।\nकारण (R): कालीबंगन के पास ईंटों को पकाने के लिए घने जंगलों की कमी थी, जिससे वे धूप में सुखाने पर निर्भर थे।",
    "Both are true and R explains why mud-bricks dominated at Kalibangan.": "दोनों सत्य हैं और कारण सही व्याख्या करता है कि क्यों कालीबंगन में मिट्टी की ईंटों का प्रभुत्व था।",
    "Assertion (A): Banawali represents a degenerate phase of mature town planning.\\nReason (R): Streets at Banawali did not follow a strict grid pattern and radial lanes were present.": "कथन (A): बनावली परिपक्व नगर नियोजन के पतन के चरण का प्रतिनिधित्व करता है।\nकारण (R): बनावली में सड़कों ने कड़े ग्रिड पैटर्न का पालन नहीं किया और वहाँ त्रिज्यीय (radial) गलियाँ मौजूद थीं।",
    "Both are true and R explains why Banawali is considered an exception to the grid layout.": "दोनों सत्य हैं और कारण व्याख्या करता है कि क्यों बनावली को ग्रिड पैटर्न का अपवाद माना जाता है।",
    "Assertion (A): Rakhigarhi is recognized as the largest Indus Valley site.\\nReason (R): Excavations revealed a cemetery and nine massive mounds covering over 350 hectares.": "कथन (A): राखीगढ़ी को सबसे बड़े सिंधु घाटी स्थल के रूप में मान्यता प्राप्त है।\nकारण (R): उत्खनन से एक कब्रिस्तान और नौ विशाल टीले मिले हैं जो 350 हेक्टेयर से अधिक क्षेत्र को कवर करते हैं।",
    "Both are true and R explains why Rakhigarhi is the largest site.": "दोनों सत्य हैं और कारण स्पष्ट करता है कि क्यों राखीगढ़ी सबसे बड़ा भौगोलिक स्थल है।",
    "Assertion (A): Surkotada was fortified with a stone-reinforced gateway.\\nReason (R): The gateway and stone walls provided security against cattle raids and external attacks in peripheral Gujarat.": "कथन (A): सुरकोटदा पत्थर से सुदृढ़ किए गए एक प्रवेश द्वार से सुरक्षित था।\nकारण (R): इस प्रवेश द्वार और पत्थर की दीवारों ने गुजरात के बाहरी क्षेत्र में मवेशी चोरी और बाहरी हमलों से सुरक्षा प्रदान की।",
    "Both are true and R explains the function of Surkotada's stone gateway.": "दोनों सत्य हैं और कारण सुरकोटदा के पत्थर के प्रवेश द्वार के कार्य की सही व्याख्या करता है।",

    # S2 Statement-Based
    "Consider the following statements regarding the Lothal dockyard:\\n1. It was constructed of high-quality baked bricks to resist water pressure.\\n2. It was connected to the Bhogavo River, which allowed ships to enter at high tide.\\nWhich of the statements given above is/are correct?": "लोथल गोदी बाड़े (dockyard) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. पानी के दबाव को झेलने के लिए इसका निर्माण उच्च गुणवत्ता वाली पकी ईंटों से किया गया था।\n2. यह भोगवो नदी से जुड़ा था, जिसने जहाजों को उच्च ज्वार पर प्रवेश करने की अनुमति दी।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
    "Consider the following statements regarding Dholavira:\\n1. The city is divided into three sections: Citadel, Middle Town, and Lower Town.\\n2. It has yielded a signboard containing ten large gypsum characters in the Indus script.\\nWhich of the statements given above is/are correct?": "धोलावीरा के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. शहर तीन भागों में विभाजित है: दुर्ग, मध्य नगर और निचला नगर।\n2. यहाँ से सिंधु लिपि में दस बड़े जिप्सम अक्षरों वाला एक साइनबोर्ड मिला है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
    "Consider the following statements regarding Mohenjo-daro:\\n1. The Great Bath was lined with a layer of natural tar (bitumen) to prevent leakage.\\n2. The Great Granary was built on a high brick platform to protect grain from dampness and floods.\\nWhich of the statements given above is/are correct?": "मोहनजोदड़ो के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. पानी के रिसाव को रोकने के लिए विशाल स्नानागार पर प्राकृतिक तारकोल (bitumen) की परत लगाई गई थी।\n2. अनाज को सीलन और बाढ़ से बचाने के लिए विशाल अन्नागार को एक ऊंचे ईंट के चबूतरे पर बनाया गया था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
    "Consider the following statements regarding Kalibangan:\\n1. A row of seven fire altars was found on a platform in the citadel.\\n2. Skeletons of a male and female buried together (double burial) were excavated here.\\nWhich of the statements given above is/are correct?": "कालीबंगन के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. दुर्ग में एक चबूतरे पर सात अग्निवेदियों की एक पंक्ति पाई गई थी।\n2. यहाँ एक ही कब्र में पुरुष और महिला के कंकालों के युगल शवाधान का उत्खनन किया गया था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
    "Statement 1 is correct. Statement 2 is incorrect because the double burial was found at Lothal, not Kalibangan.": "कथन 1 सही है। कथन 2 गलत है क्योंकि युगल शवाधान लोथल से मिला था, कालीबंगन से नहीं।",
    "Consider the following statements regarding Chanhudaro:\\n1. It was a major industrial center specializing in bead-making, seal-cutting, and shell-working.\\n2. It is the only Harappan city that has yielded a brick with the paw print of a dog chasing a cat.\\nWhich of the statements given above is/are correct?": "चन्हुदड़ो के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. यह मनके बनाने, मुहर तराशने और शंख-शिल्प में विशेषज्ञता रखने वाला एक प्रमुख औद्योगिक केंद्र था।\n2. यह एकमात्र ऐसा शहर है जहाँ से बिल्ली का पीछा करते हुए कुत्ते के पंजों के निशान वाली ईंट मिली है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
    "Both statements are correct. The paw print brick is a famous discovery from Chanhudaro.": "दोनों कथन सही हैं। पंजों के निशान वाली ईंट चन्हुदड़ो की एक प्रसिद्ध खोज है।",

    # S2 Conceptual
    "Why did Mohenjo-daro houses feature an abundance of water wells?": "मोहनजोदड़ो के घरों में इतनी अधिक संख्या में पानी के कुएँ क्यों थे?",
    "Almost every house had its own brick well, providing fresh water and maintaining high sanitation standards, which was unique in the ancient world.": "लगभग हर घर का अपना ईंटों का कुआँ था, जो ताज़ा पानी प्रदान करता था और स्वच्छता के उच्च मानकों को बनाए रखता था, जो प्राचीन विश्व में अद्वितीय था।",
    "Why did Chanhudaro lack defensive fortifications or a citadel structure?": "चन्हुदड़ो में रक्षात्मक किलेबंदी या प्रशासनिक दुर्ग की कमी क्यों थी?",
    "Because it was a dedicated industrial and craft center, not an administrative or political seat, focusing entirely on manufacture.": "क्योंकि यह एक समर्पित औद्योगिक और शिल्प केंद्र था, न कि प्रशासनिक या राजनीतिक मुख्यालय, और इसका ध्यान पूरी तरह से उत्पादन पर था।",
    "Why did Dholavira implement a three-tier town layout?": "धोलावीरा ने त्रि-स्तरीय नगर नियोजन क्यों लागू किया था?",
    "It represents a stratified social hierarchy: the elite rulers in the Citadel, merchants/middle class in the Middle Town, and artisans/laborers in the Lower Town.": "यह एक स्तरीकृत सामाजिक पदानुक्रम को दर्शाता है: दुर्ग में विशिष्ट शासक, मध्य नगर में व्यापारी/मध्यम वर्ग, और निचले नगर में शिल्पकार/मजदूर रहते थे।",
    "How did Lothal's dockyard operate with tidal water flows?": "लोथल का गोदी बाड़ा ज्वारीय जल प्रवाह के साथ कैसे संचालित होता था?",
    "It used a sluice gate mechanism to trap water in the basin at high tide, allowing ships to float and remain stable for loading/unloading even during low tide.": "इसने उच्च ज्वार पर बेसिन में पानी को रोकने के लिए एक स्लूइस गेट (sluice gate) तंत्र का उपयोग किया, जिससे निम्न ज्वार के दौरान भी जहाजों को तैरते रहने और स्थिर रहने में मदद मिलती थी।",
    "How did the Great Granary at Mohenjo-daro keep stored grain fresh?": "मोहनजोदड़ो का विशाल अन्नागार संग्रहित अनाज को कैसे ताजा रखता था?",
    "Built on a high platform to prevent flood damage, it featured air channels (ducts) that allowed cool air to circulate, keeping the grain dry and preventing rot.": "बाढ़ से नुकसान को रोकने के लिए इसे एक ऊंचे चबूतरे पर बनाया गया था, और इसमें वायु मार्ग थे जो ठंडी हवा को प्रसारित होने देते थे, जिससे अनाज सूखा रहता था और सड़ता नहीं था।",
    "How did Kalibangan's pre-mature agricultural layout optimize double-cropping?": "कालीबंगन के पूर्व-परिपक्व कृषि क्षेत्र ने दोहरी फसल पद्धति को कैसे सुगम बनाया?",
    "The furrows ran in two perpendicular directions: one set spaced closely (30cm) for small crops (mustard) and another spaced widely (1.9m) for taller crops (chickpeas), preventing shadow competition.": "जुताई की रेखाएँ दो लंबवत दिशाओं में थीं: एक कम दूरी पर (30 सेमी) छोटी फसलों (सरसों) के लिए और दूसरी अधिक दूरी पर (1.9 मीटर) लंबी फसलों (चने) के लिए, जिससे धूप के लिए प्रतिस्पर्धा नहीं होती थी।",
    "Case Study: The Lothal Dockyard": "केस स्टडी: लोथल गोदी बाड़ा",
    "A baked-brick basin measuring 218m x 37m. It shows advanced understanding of tidal hydrodynamics, enabling ships to dock from the Gulf of Khambhat via a river channel.": "पकी ईंटों से बना 218 मीटर x 37 मीटर का बेसिन। यह ज्वारीय जलगतिकी (hydrodynamics) की उन्नत समझ दिखाता है, जिसने जहाजों को नदी मार्ग के माध्यम से खंभात की खाड़ी से प्रवेश करने में सक्षम बनाया।",
    "Case Study: Dholavira's Reservoir Network": "केस स्टडी: धोलावीरा का जलाशय नेटवर्क",
    "Dholavira constructed 16 stone-cut reservoirs that collected rainwater from seasonal streams. This system sustained a large population in an arid region with no perennial rivers.": "धोलावीरा ने पत्थर काटकर 16 जलाशय बनाए जो मौसमी नालों से बारिश का पानी इकट्ठा करते थे। इस प्रणाली ने बारहमासी नदियों के बिना शुष्क क्षेत्र में एक बड़ी आबादी का जीवन संभव बनाया।",
    "Case Study: The Craft Workshops of Chanhudaro": "केस स्टडी: चन्हुदड़ो की शिल्प कार्यशालाएं",
    "Excavations revealed bead-making factories with drills, furnaces, and raw materials (carnelian, jasper). It confirms Chanhudaro was a highly specialized manufacturing hub.": "उत्खनन से मनके बनाने के कारखाने मिले हैं जिनमें बरमे (drills), भट्टियां और कच्चा माल (अकीक, जैस्पर) शामिल हैं। यह पुष्टि करता है कि चन्हुदड़ो एक अत्यधिक विशिष्ट विनिर्माण केंद्र था।",
    "Teach the Concept: The Citadel vs Lower Town": "अवधारणा को समझें: दुर्ग बनाम निचला नगर",
    "Explain that most Harappan cities had a dual layout: the western, raised Citadel (administrative offices and public halls) and the eastern, larger Lower Town (residential houses for the public).": "समझाएं कि अधिकांश शहरों का दोहरा लेआउट था: पश्चिम में स्थित ऊंचा दुर्ग (प्रशासनिक कार्यालय और सार्वजनिक भवन) और पूर्व में स्थित बड़ा निचला नगर (आम जनता के रहने के लिए घर)।",
    "Teach the Concept: The Granary and Food Security": "अवधारणा को समझें: अन्नागार और खाद्य सुरक्षा",
    "Explain how the state controlled food security by storing surplus grain in large public granaries (like those at Harappa and Mohenjo-daro) to survive famines and floods.": "समझाएं कि कैसे राज्य ने अकाल और बाढ़ से बचने के लिए बड़े सार्वजनिक अन्नागारों (जैसे हड़प्पा और मोहनजोदड़ो में) में अतिरिक्त अनाज का भंडारण करके खाद्य सुरक्षा को नियंत्रित किया।",
    "Teach the Concept: The Three-Tier Town Layout of Dholavira": "अवधारणा को समझें: धोलावीरा का त्रि-स्तरीय नगर नियोजन",
    "Highlight how Dholavira broke the standard dual layout by adding a 'Middle Town' between the Citadel and Lower Town, representing a unique social structure and civic complexity.": "बताएं कि कैसे धोलावीरा ने दुर्ग और निचले नगर के बीच एक 'मध्य नगर' जोड़कर मानक दोहरे लेआउट को बदल दिया, जो एक अनूठी सामाजिक संरचना और जटिलता को दर्शाता है।",

    # Section 3 Qs
    "What soft soapstone material was primarily used to manufacture Harappan seals?": "हड़प्पा की मुहरों के निर्माण में मुख्य रूप से किस नरम सोपस्टोन (साबुन का पत्थर) सामग्री का उपयोग किया जाता था?",
    "Chert": "चर्ट", "Steatite": "सेलखड़ी (Steatite)", "Faience": "फेयॉन्स", "Copper": "तांबा",
    "Most Harappan seals were carved from steatite (soapstone), which was easy to engrave and then baked to harden.": "हड़प्पा की अधिकांश मुहरें सेलखड़ी से बनाई गई थीं, जिसे तराशना आसान था और फिर भट्टी में गर्म करके उसे सख्त कर दिया जाता था।",
    "The famous bronze Dancing Girl statue was cast using which technical metallurgical process?": "प्रसिद्ध कांस्य नर्तकी (Dancing Girl) की मूर्ति किस धातु कर्म प्रक्रिया का उपयोग करके ढाली गई थी?",
    "Sand casting": "रेत ढलाई", "Lost-wax casting (Cire Perdue)": "लुप्त-मोम विधि (Lost-wax/Cire Perdue)", "Cold hammering": "ठंडा ठोकना", "Sheet metal joining": "धातु की चादरें जोड़ना",
    "The Dancing Girl was made using the lost-wax casting technique, showing advanced metallurgy.": "नर्तकी की मूर्ति का निर्माण लुप्त-मोम (lost-wax) विधि से किया गया था, जो उन्नत धातु कर्म को दर्शाता है।",
    "Which of the following materials was primarily used to make the highly standardized Harappan cubical weights?": "अत्यधिक मानकीकृत घनाकार हड़प्पा बाटों को बनाने के लिए मुख्य रूप से किस सामग्री का उपयोग किया जाता था?",
    "Lapis Lazuli": "लाजवर्त", "Alabaster": "सफेद संगमरमर",
    "Standardized cubical weights were made from a hard, fine-grained stone called chert.": "मानकीकृत घनाकार बाट चर्ट (chert) नामक एक कठोर, बारीक दाने वाले पत्थर से बनाए जाते थे।",
    "The famous bearded 'Priest-King' stone statue was excavated at which Mature Harappan site?": "प्रसिद्ध दाढ़ी वाले 'पुरोहित-राजा' (Priest-King) की पत्थर की मूर्ति किस परिपक्व हड़प्पा स्थल से मिली थी?",
    "The steatite Priest-King statue was discovered at Mohenjo-daro.": "सेलखड़ी से बनी पुरोहित-राजा की मूर्ति मोहनजोदड़ो से मिली थी।",
    "Which site yielded a unique clay pot featuring a painting of a crow and a fox, resembling the Panchatantra fable?": "किस स्थल से मिट्टी का एक अनूठा बर्तन मिला है जिस पर कौवे और लोमड़ी का चित्र बना है, जो पंचतंत्र की कहानी जैसा दिखता है?",
    "Lothal yielded a painted jar showing a crow with a fish and a fox, often compared to the 'Cunning Crow' fable.": "लोथल से एक चित्रित जार मिला है जिस पर मछली दबाए एक कौवा और एक लोमड़ी दिखाई गई है, जो पंचतंत्र की कहानी से मेल खाता है।",

    # S3 Multi-Correct
    "Identify the animals depicted around the central yogic figure on the Pashupati Seal: (Select all that apply)": "पशुपति मुहर पर केंद्रीय योगिक आकृति के आसपास चित्रित जानवरों की पहचान करें: (लागू होने वाले सभी विकल्प चुनें)",
    "Elephant and Tiger": "हाथी और बाघ", "Rhinoceros and Buffalo": "गेंदा और भैंसा", "Two Deer (at the feet)": "दो हिरण (पैरों के पास)", "Horse and Lion": "घोड़ा और शेर",
    "The Pashupati seal depicts an elephant, tiger, rhino, buffalo, and two deer. The horse and lion are absent.": "पशुपति मुहर पर हाथी, बाघ, गेंडा, भैंसा और दो हिरण चित्रित हैं। घोड़ा और शेर अनुपस्थित हैं।",
    "Which metals were known and used by Indus Valley metalworkers? (Select all that apply)": "सिंधु घाटी के धातु-कर्मियों को किन धातुओं का ज्ञान था और वे उनका उपयोग करते थे? (लागू होने वाले सभी विकल्प चुनें)",
    "Copper": "तांबा", "Bronze": "कांस्य", "Gold": "सोना", "Iron": "लोहा",
    "Copper, bronze, gold, and silver were used. Iron was completely unknown to the Harappans.": "तांबा, कांस्य, सोना और चांदी का उपयोग किया जाता था। हड़प्पावासियों के लिए लोहा पूरी तरह से अज्ञात था।",
    "Select the burial types identified in Mature Harappan cemeteries: (Select all that apply)": "परिपक्व हड़प्पा कब्रिस्तानों में पहचाने गए शवाधान के प्रकारों का चयन करें: (लागू होने वाले सभी विकल्प चुनें)",
    "Wooden coffin burials": "लकड़ी के ताबूत वाले शवाधान", "Pot/Urn burials": "घड़े (कलश) शवाधान", "Brick-chambered burials": "ईंटों के कक्ष वाले शवाधान", "Mummified burials": "ममी वाले शवाधान",
    "Harappans used coffin, pot, and brick-chamber burials. Mummification was not practiced.": "हड़प्पावासी ताबूत, घड़े और ईंट-कक्ष शवाधान का उपयोग करते थे। ममी बनाने की प्रथा नहीं थी।",
    "Which of the following items are associated with Mohenjo-daro? (Select all that apply)": "निम्नलिखित में से कौन सी वस्तुएं मोहनजोदड़ो से संबंधित हैं? (लागू होने वाले सभी विकल्प चुनें)",
    "The Bronze Dancing Girl": "कांस्य की नर्तकी", "The Steatite Priest-King": "सेलखड़ी के पुरोहित-राजा", "Woven cotton fragments": "बुने हुए कपास के टुकड़े", "A red sandstone torso of a male dancer": "पुरुष नर्तक का लाल बलुआ पत्थर का धड़",
    "Dancing Girl, Priest-King, and cotton are from Mohenjo-daro. The red sandstone male torso is from Harappa.": "नर्तकी, पुरोहित-राजा और कपास मोहनजोदड़ो से मिले हैं। पुरुष नर्तक का लाल बलुआ पत्थर का धड़ हड़प्पा से मिला है।",
    "Identify the primary raw materials imported for craft production: (Select all that apply)": "शिल्प उत्पादन के लिए आयात किए जाने वाले मुख्य कच्चे माल की पहचान करें: (लागू होने वाले सभी विकल्प चुनें)",
    "Lapis Lazuli from Badakhshan": "बदख्शां से लाजवर्त (Lapis Lazuli)", "Copper from Khetri mines": "खेतड़ी खदानों से तांबा", "Carnelian from Gujarat": "गुजरात से अकीक (Carnelian)", "Iron from Central India": "मध्य भारत से लोहा",
    "Lapis Lazuli, Copper, and Carnelian were imported/mined. Iron was unknown.": "लाजवर्त, तांबा और अकीक का आयात/उत्खनन किया जाता था। लोहा अज्ञात था।",

    # S3 True/False
    "The Pashupati seal depicts a three-faced seated deity wearing a horned headdress.": "पशुपति मुहर पर एक सींग वाले मुकुट पहने तीन मुख वाले बैठे हुए देवता को दिखाया गया है।",
    "True. The figure sits in a yogic yogasana posture with arms covered in bangles.": "सत्य। यह आकृति एक योगासन मुद्रा में बैठी है और इसकी भुजाएं चूड़ियों से ढकी हैं।",
    "The bronze Dancing Girl is depicted wearing a large number of bangles on her left arm.": "कांस्य नर्तकी को उसकी बाईं भुजा पर बड़ी संख्या में चूड़ियाँ पहने हुए चित्रित किया गया है।",
    "True. She wears 24 to 25 bangles on her left arm, holding it on her thigh.": "सत्य। वह अपने बाएं हाथ में 24 से 25 चूड़ियां पहने हुए है, और हाथ को अपनी जांघ पर रखे है।",
    "Harappan pottery was mostly plain, handmade grey ware with no paint.": "हड़प्पा के मिट्टी के बर्तन ज्यादातर बिना रंग के हाथ से बने सादे धूसर मृदभांड थे।",
    "False. Most pottery was wheel-made Red and Black ware, painted with black designs on red slips.": "असत्य। अधिकांश मिट्टी के बर्तन चाक पर बने लाल और काले मृदभांड थे, जिन पर लाल रंग की सतह पर काले रंग से डिज़ाइन बनाए गए थे।",
    "Traces of woven cotton cloth were discovered wrapped around a silver jar at Mohenjo-daro.": "मोहनजोदड़ो में एक चांदी के बर्तन के चारों ओर बुने हुए सूती कपड़े के लपेटे जाने के अवशेष मिले थे।",
    "True. This provides the oldest evidence of cotton use in the ancient world.": "सत्य। यह प्राचीन विश्व में कपास के उपयोग का सबसे पुराना प्रमाण प्रदान करता है।",
    "Harappan weights were spherical stone balls with no uniform values.": "हड़प्पा के बाट गोल पत्थर की गेंदें थीं जिनका कोई निश्चित या मानकीकृत वजन नहीं था।",
    "False. They were highly standardized cubical chert blocks following binary and decimal systems.": "असत्य। वे अत्यधिक मानकीकृत चर्ट पत्थर के घनाकार टुकड़े थे जो द्वि-आधारी और दशमलव प्रणालियों का पालन करते थे।",
    "The Priest-King statue is made of steatite and wears a shawl decorated with trefoil patterns.": "पुरोहित-राजा की मूर्ति सेलखड़ी से बनी है और वह तिपतिया पैटर्न से सजी शॉल ओढ़े हुए है।",
    "True. The trefoil patterns indicate contacts with Mesopotamian royal symbols.": "सत्य। तिपतिया पैटर्न मेसोपोटामिया के शाही प्रतीकों के साथ संपर्कों को दर्शाता है।",
    "Iron weapons and tools were excavated from the Cemetery R-37 at Harappa.": "हड़प्पा के कब्रिस्तान R-37 से लोहे के हथियार और उपकरण उत्खनित किए गए थे।",
    "False. Harappans were in the Bronze Age and had no knowledge of iron.": "असत्य। हड़प्पावासी कांस्य युग में थे और उन्हें लोहे का कोई ज्ञान नहीं था।",
    "The double burial at Lothal contains the skeletons of a male and female buried in the same grave.": "लोथल में युगल शवाधान में एक ही कब्र में दफनाए गए एक पुरुष और एक महिला के कंकाल मिले हैं।",
    "True. This unique joint burial is found only at Lothal in Gujarat.": "सत्य। यह अनूठा संयुक्त शवाधान केवल गुजरात के लोथल से प्राप्त हुआ है।",

    # S3 Fill Blank
    "The bearded Priest-King stone statue was discovered at the site of __________.": "दाढ़ी वाले पुरोहित-राजा की पत्थर की मूर्ति __________ स्थल पर खोजी गई थी।",
    "Mohenjo-daro yielded this steatite sculpture.": "मोहनजोदड़ो से यह सेलखड़ी की मूर्ति मिली थी।",
    "The metallurgical process used to cast the bronze Dancing Girl is called __________ casting.": "कांस्य नर्तकी की मूर्ति को ढालने के लिए उपयोग की जाने वाली धातु कर्म प्रक्रिया को __________ ढलाई कहा जाता है।",
    "lost-wax": "लुप्त-मोम (lost-wax)",
    "Lost-wax casting (cire perdue) was used.": "लुप्त-मोम ढलाई (cire perdue) का उपयोग किया गया था।",
    "Most Harappan seals feature an engraving of a mythical one-horned beast called the __________.": "अधिकांश हड़प्पा मुहरों पर एक काल्पनिक एक सींग वाले जानवर का अंकन है जिसे __________ कहा जाता है।",
    "unicorn": "एकश्रृंगी (unicorn)",
    "The unicorn is the most common animal on seals.": "मुहरों पर एकश्रृंगी सबसे आम जानवर है।",
    "The primary hard stone used to make Harappan cubical weights is __________.": "हड़प्पा के घनाकार बाट बनाने के लिए उपयोग किया जाने वाला मुख्य कठोर पत्थर __________ है।",
    "chert": "चर्ट (chert)",
    "Chert was used for its durability and consistency.": "चर्ट का उपयोग इसके स्थायित्व और मजबूती के लिए किया जाता था।",
    "Harappan painted pottery is scientifically classified as __________ and Black Ware.": "हड़प्पा के चित्रित मिट्टी के बर्तनों को वैज्ञानिक रूप से __________ और काले मृदभांड (Black Ware) के रूप में वर्गीकृत किया गया है।",
    "Red": "लाल (Red)",
    "Red and Black Ware is the characteristic style.": "लाल और काले मृदभांड हड़प्पा की विशिष्ट शैली हैं।",
    "A joint grave containing a double burial was discovered at the port site of __________.": "एक संयुक्त कब्र जिसमें युगल शवाधान था, __________ बंदरगाह स्थल पर खोजी गई थी।",
    "Lothal has double burials in its cemetery.": "लोथल के कब्रिस्तान से युगल शवाधान मिले हैं।",
    "The Priest-King shawl features a repeating decorative motif known as the __________ pattern.": "पुरोहित-राजा की शॉल पर एक दोहरावदार सजावटी पैटर्न है जिसे __________ पैटर्न कहा जाता है।",
    "trefoil": "तिपतिया (trefoil)",
    "The trefoil pattern resembles clover leaves.": "तिपतिया पैटर्न तीन पत्तियों वाले फूल जैसा दिखता है।",
    "Engraved seals were made of a soft soapstone called __________.": "उत्कीर्ण मुहरें एक नरम पत्थर से बनाई गई थीं जिसे __________ कहा जाता है।",
    "steatite": "सेलखड़ी (steatite)",
    "Steatite was carved and heated to form durable seals.": "सेलखड़ी को तराशा जाता था और फिर गर्म करके मजबूत मुहरें बनाई जाती थीं।",

    # S3 Matching
    "Match the famous archaeological artifacts with their primary manufacturing materials:": "प्रसिद्ध पुरातात्विक कलाकृतियों को उनकी मुख्य निर्माण सामग्री से सुमेलित करें:",
    "I. Dancing Girl": "I. नर्तकी", "II. Priest-King": "II. पुरोहित-राजा", "III. Cubical Weights": "III. घनाकार बाट",
    "A. Bronze (Metal Alloy)": "A. कांस्य (धातु मिश्र धातु)", "B. Steatite (Soapstone)": "B. सेलखड़ी (साबुन का पत्थर)", "C. Chert (Hard Stone)": "C. चर्ट (कठोर पत्थर)",
    "Dancing Girl is bronze, Priest-King is steatite, and weights are chert.": "नर्तकी कांस्य की है, पुरोहित-राजा सेलखड़ी के हैं, और बाट चर्ट पत्थर के हैं।",
    "Match the unique burial types with their corresponding Harappan sites:": "विशिष्ट शवाधान प्रकारों को उनके संबंधित हड़प्पा स्थलों से सुमेलित करें:",
    "I. Double Burial": "I. युगल शवाधान", "II. Wooden Coffin Burial": "II. ताबूत शवाधान", "III. Pot Burial": "III. घड़ा शवाधान",
    "A. Lothal": "A. लोथल", "B. Harappa (Cemetery R-37)": "B. हड़प्पा (कब्रुस्तान R-37)", "C. Kalibangan": "C. कालीबंगन",
    "Double burial is from Lothal, coffin burial from Harappa, and pot burial from Kalibangan.": "युगल शवाधान लोथल से, ताबूत शवाधान हड़प्पा से और घड़ा शवाधान कालीबंगन से मिला है।",
    "Match the animals depicted on Harappan seals with their academic interpretations:": "हड़प्पा मुहरों पर चित्रित जानवरों को उनकी शैक्षणिक व्याख्याओं से सुमेलित करें:",
    "I. Pashupati figure": "I. पशुपति की आकृति", "II. Unicorn figure": "II. एकश्रृंगी की आकृति", "III. Humped Bull": "III. कूबड़ वाला बैल",
    "A. Proto-Shiva / Lord of Animals": "A. आदि-शिव / पशुपतिनाथ", "B. Mythical merchant clan symbol": "B. काल्पनिक व्यापारी कबीले का प्रतीक", "C. Sacred zebu / strength symbol": "C. पवित्र सांड / शक्ति का प्रतीक",
    "Pashupati is Proto-Shiva, unicorn is merchant symbol, and bull represents strength.": "पशुपति आदि-शिव हैं, एकश्रृंगी व्यापारियों का प्रतीक है, और बैल शक्ति का प्रतिनिधित्व करता है।",

    # S3 One-Liners
    "What is the exact height of the famous bronze Dancing Girl statue?": "प्रसिद्ध कांस्य नर्तकी की मूर्ति की सही ऊँचाई क्या है?",
    "10.5 centimeters.": "10.5 सेंटीमीटर।",
    "Which site yielded a red sandstone sculpture of a male dancer with twisting torso?": "किस स्थल से घूमते हुए धड़ वाले पुरुष नर्तक की लाल बलुआ पत्थर की मूर्ति मिली थी?",
    "Harappa.": "हड़प्पा।",
    "What characteristic color is the glazed surface of Harappan faience ornaments?": "हड़प्पा के फेयॉन्स (faience) के गहनों की चमकदार सतह का विशिष्ट रंग कौन सा है?",
    "Greenish-blue or turquoise.": "हरा-नीला या फ़िरोज़ा (turquoise)।",
    "Name the animal painted on a Lothal pot that resembles the Panchatantra fox fable.": "लोथल के एक बर्तन पर चित्रित उस जानवर का नाम बताइए जो पंचतंत्र की लोमड़ी की कहानी जैसा दिखता है।",
    "A crow and a fox.": "एक कौआ और एक लोमड़ी।",
    "What term is used to describe the yet-undeciphered script carved on Harappan seals?": "हड़प्पा की मुहरों पर उत्कीर्ण अभी तक न पढ़ी गई लिपि को क्या कहा जाता है?",
    "Indus Script (written in Boustrophedon style).": "सिंधु लिपि (बूस्ट्रोफेडन शैली में लिखी गई)।",
    "What type of drills were used in bead-making workshops at Chanhudaro and Lothal?": "चन्हुदड़ो और लोथल में मनके बनाने की कार्यशालाओं में किस प्रकार के बरमों (drills) का उपयोग किया जाता था?",
    "Specialized chert or bronze drills.": "विशेष प्रकार के चर्ट या कांस्य के बरमे।",
    "Which site in Maharashtra yielded a hoard of solid copper figures of animals?": "महाराष्ट्र के किस स्थल से जानवरों की तांबे की ठोस मूर्तियों का खजाना मिला था?",
    "Daimabad.": "दैमाबाद।",
    "What are the clay toys and mother goddess figures found at Harappan sites called?": "हड़प्पा स्थलों पर पाए जाने वाले मिट्टी के खिलौनों और मातृदेवी की मूर्तियों को क्या कहा जाता है?",
    "Terracotta figurines.": "टेराकोटा मूर्तियाँ (terracotta figurines)।",

    # S3 Assertion-Reason
    "Assertion (A): Steatite was the most popular material for seal carving.\\nReason (R): Steatite is a soft soapstone that allows fine engraving and hardens when fired.": "कथन (A): मुहरों को तराशने के लिए सेलखड़ी सबसे लोकप्रिय सामग्री थी।\nकारण (R): सेलखड़ी एक नरम पत्थर है जो बारीक नक्काशी की अनुमति देता है और गर्म करने पर कठोर हो जाता है।",
    "Both A and R are true and R explains A. Steatite's properties made it ideal for seal production.": "दोनों कथन सत्य हैं और कारण कथन की सही व्याख्या है। सेलखड़ी के गुणों ने इसे मुहरों के लिए आदर्श बनाया।",
    "Assertion (A): The Dancing Girl is depicted as an active cultural figure.\\nReason (R): She stands in the tribhanga dance pose with her hand on her hip and wear bangles.": "कथन (A): कांस्य नर्तकी को एक सक्रिय सांस्कृतिक व्यक्ति के रूप में चित्रित किया गया है।\nकारण (R): वह अपने हाथ को कूल्हे पर रखकर और चूड़ियाँ पहनकर त्रिभंग नृत्य मुद्रा में खड़ी है।",
    "Both A and R are true and R explains her representation as a dancer.": "दोनों कथन सत्य हैं और कारण नृत्य मुद्रा में उसके चित्रण की सही व्याख्या करता है।",
    "Assertion (A): The Harappans traded extensively for lapis lazuli beads.\\nReason (R): Lapis lazuli was imported from Badakhshan to manufacture luxury items for elites.": "कथन (A): हड़प्पावासियों ने लाजवर्त (lapis lazuli) के मनकों के लिए व्यापक व्यापार किया।\nकारण (R): अभिजात वर्ग के लिए विलासिता की वस्तुएं बनाने के लिए बदख्शां से लाजवर्त का आयात किया जाता था।",
    "Both are true and R explains the trade dynamics of lapis lazuli.": "दोनों सत्य हैं और कारण लाजवर्त के व्यापारिक महत्व की सही व्याख्या करता है।",
    "Assertion (A): Cotton textiles were exported to Sumerian markets.\\nReason (R): Woven cotton fragments were found preserved on a silver jar at Mohenjo-daro.": "कथन (A): सूती कपड़ों का निर्यात सुमेर के बाजारों में किया जाता था।\nकारण (R): मोहनजोदड़ो में एक चांदी के बर्तन पर बुने हुए कपास के अवशेष संरक्षित मिले थे।",
    "Both statements are true but R does not explain why it was exported; it only proves preservation.": "दोनों कथन सत्य हैं लेकिन कारण कथन की सही व्याख्या नहीं है; यह केवल संरक्षण की पुष्टि करता है।",
    "Assertion (A): Iron implements were placed in Cemetery R-37 burials.\\nReason (R): The Harappan culture was a Bronze Age society that had no knowledge of iron metallurgy.": "कथन (A): कब्रिस्तान R-37 के शवाधानों में लोहे के औजार रखे गए थे।\nकारण (R): हड़प्पा संस्कृति एक कांस्य युगीन समाज था जिसे लोहे के धातु कर्म का कोई ज्ञान नहीं था।",
    "Assertion is false: iron was absent. Reason is true.": "कथन असत्य है: लोहा अनुपस्थित था। कारण सत्य है।",
    "Assertion (A): Faience ornaments were considered high-status items.\\nReason (R): Faience was made of ground sand and glaze, requiring complex kiln firing that was difficult to master.": "कथन (A): फेयॉन्स के आभूषणों को उच्च सामाजिक स्थिति का प्रतीक माना जाता था।\nकारण (R): फेयॉन्स पीसे हुए रेत और गोंद के मिश्रण से बनता था, जिसके लिए जटिल भट्टी में पकाने की आवश्यकता होती थी।",
    "Both are true and R explains why faience was considered a luxury ornament.": "दोनों सत्य हैं और कारण स्पष्ट करता है कि क्यों फेयॉन्स को एक विलासिता का आभूषण माना जाता था।",
    "Assertion (A): The Pashupati seal is often linked to the origins of Shiva worship.\\nReason (R): The seated figure wears a horned crown, sits in a yogic posture, and is surrounded by wild animals.": "कथन (A): पशुपति मुहर को अक्सर शिव पूजा की उत्पत्ति से जोड़ा जाता है।\nकारण (R): बैठी हुई आकृति ने सींगों वाला मुकुट पहना है, वह योग मुद्रा में है, और जंगली जानवरों से घिरी है।",
    "Both are true and R explains the Pashupati-Shiva connection.": "दोनों सत्य हैं और कारण पशुपति-शिव के संबंध की सही व्याख्या करता है।",
    "Assertion (A): The double burial at Lothal indicates Sati practice.\\nReason (R): Joint burials can occur due to epidemics or natural deaths, and there is no proof of immolation.": "कथन (A): लोथल में मिला युगल शवाधान सती प्रथा को दर्शाता है।\nकारण (R): संयुक्त कब्रें महामारी या प्राकृतिक मृत्यु के कारण भी हो सकती हैं, और आत्मदाह (सती) का कोई प्रमाण नहीं है।",
    "A is false because Sati is not proven. R is true.": "कथन असत्य है क्योंकि सती सिद्ध नहीं हुई है। कारण सत्य है।",

    # S3 Statement-Based
    "Consider the following statements regarding Harappan seals:\\n1. Most seals are square and contain short inscriptions alongside animal carvings.\\n2. Seals were made of steatite, terracotta, and sometimes copper.\\nWhich of the statements given above is/are correct?": "हड़प्पा मुहरों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. अधिकांश मुहरें चौकोर हैं और उनमें जानवरों के चित्रों के साथ संक्षिप्त लेख हैं।\n2. मुहरें सेलखड़ी, टेराकोटा और कभी-कभी तांबे से बनी थीं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
    "Consider the following statements regarding the Dancing Girl:\\n1. It is a solid bronze casting made using the lost-wax process.\\n2. She is shown completely naked except for a necklace and bangles.\\nWhich of the statements given above is/are correct?": "कांस्य नर्तकी (Dancing Girl) के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. यह लुप्त-मोम विधि द्वारा ढली हुई ठोस कांसे की मूर्ति है।\n2. वह गले में एक हार और हाथों में चूड़ियों के अलावा पूरी तरह नग्न दिखाई गई है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
    "Consider the following statements regarding Harappan pottery:\\n1. The pottery was primarily black-on-red painted ware.\\n2. The designs painted on the pottery include geometric circles, pipal leaves, and fish scales.\\nWhich of the statements given above is/are correct?": "हड़प्पा के बर्तनों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. मृदभांड मुख्य रूप से लाल और काले चित्रित मृदभांड थे।\n2. बर्तनों पर बने चित्रों में ज्यामितीय वृत्त, पीपल की पत्तियां और मछली के शल्क शामिल हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
    "Both statements are correct. These motifs are characteristic of Harappan ceramics.": "दोनों कथन सही हैं। ये रूपांकन हड़प्पा कालीन मृदभांडों की प्रमुख विशेषता हैं।",
    "Consider the following statements regarding burials:\\n1. Cemetery R-37 at Harappa contains burials where bodies were placed inside wooden coffins.\\n2. Skeletons were buried with pottery and personal ornaments, indicating a belief in life after death.\\nWhich of the statements given above is/are correct?": "शवाधान (burials) के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. हड़प्पा के कब्रिस्तान R-37 में ऐसे शवाधान मिले हैं जहाँ शवों को लकड़ी के ताबूतों में रखा गया था।\n2. शवों को मिट्टी के बर्तनों और व्यक्तिगत आभूषणों के साथ दफनाया जाता था, जो मृत्यु के बाद जीवन में विश्वास को दर्शाता है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
    "Consider the following statements regarding the Priest-King:\\n1. The statue is made of steatite and shows a draped shawl with trefoil patterns.\\n2. The eyes are elongated and were originally inlaid with shell or stone.\\nWhich of the statements given above is/are correct?": "पुरोहित-राजा के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. यह मूर्ति सेलखड़ी से बनी है और इस पर तिपतिया पैटर्न वाली शॉल ओढ़ी हुई दिखाई गई है।\n2. आँखें लंबी हैं और मूल रूप से शंख या पत्थर से जड़ी हुई थीं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
    "Both statements are correct. Trefoil pattern shawl and shell-inlaid eyes are key features of this statue.": "दोनों कथन सही हैं। तिपतिया पैटर्न वाली शॉल और शंख-जड़ी आँखें इस मूर्ति की प्रमुख विशेषताएं हैं।",

    # S3 Conceptual
    "Why did the Harappans paint animal and floral motifs on their pottery?": "हड़प्पावासी अपने मिट्टी के बर्तनों पर पशु और वनस्पति के रूपांकन क्यों बनाते थे?",
    "To express their naturalistic religious beliefs, utilizing symbols like the pipal leaf, zebu bull, and fish scales for ritual and domestic purposes.": "अपने प्रकृतिवादी धार्मिक विश्वासों को व्यक्त करने के लिए, अनुष्ठानिक और घरेलू उद्देश्यों के लिए पीपल के पत्ते, ज़ेबू बैल और मछली के शल्क जैसे प्रतीकों का उपयोग करते थे।",
    "Why was steatite the preferred material for seal manufacturing?": "मुहरों के निर्माण के लिए सेलखड़ी (steatite) को प्राथमिकता क्यों दी जाती थी?",
    "Because it is soft soapstone that can be easily carved with fine steel-like tools and then baked to trigger a phase change into hard steatite.": "क्योंकि यह एक नरम पत्थर है जिसे बारीक औजारों से आसानी से तराशा जा सकता था और फिर गर्म करने पर यह अत्यधिक कठोर हो जाता था।",
    "Why did Cemetery R-37 burials contain extensive pottery vessels?": "कब्रिस्तान R-37 के शवाधानों में मिट्टी के बर्तनों के इतने व्यापक अवशेष क्यों मिले हैं?",
    "They placed vessels containing food and water with the deceased, showing their belief in an afterlife where the soul needed nourishment.": "वे मृतक के साथ भोजन और पानी से भरे बर्तन रखते थे, जो परलोक में उनके विश्वास को दर्शाता है जहाँ आत्मा को पोषण की आवश्यकता होती थी।",
    "How did lost-wax casting work in the Harappan bronze industry?": "हड़प्पा के कांस्य उद्योग में लुप्त-मोम (lost-wax) ढलाई विधि कैसे काम करती थी?",
    "Artisans modeled a figure in wax, coated it in clay, baked it to melt and drain the wax out, and poured molten bronze into the hollow clay mold.": "कारीगर पहले मोम से एक मूर्ति बनाते थे, उसे मिट्टी से ढकते थे, फिर गर्म करके मोम को पिघलाकर बाहर निकाल देते थे, और खाली मिट्टी के सांचे में पिघला हुआ कांसा डालते थे।",
    "How did the cubical chert weights facilitate commercial integration?": "चर्ट पत्थर के घनाकार बाटों ने व्यापारिक एकीकरण को कैसे सुगम बनाया?",
    "By providing highly standardized, fraud-resistant measures across all cities, supporting trade trust from Gujarat to Punjab.": "सभी शहरों में अत्यधिक मानकीकृत और धोखाधड़ी-मुक्त माप प्रदान करके, जिसने गुजरात से पंजाब तक व्यापारिक विश्वास का समर्थन किया।",
    "How does the Priest-King's trefoil shawl pattern indicate international connections?": "पुरोहित-राजा की शॉल पर बना तिपतिया पैटर्न अंतरराष्ट्रीय संपर्कों को कैसे दर्शाता है?",
    "The trefoil pattern is also found in Mesopotamian and Egyptian royal art, representing a shared elite ideological symbol of the Bronze Age.": "तिपतिया पैटर्न मेसोपोटामिया और मिस्र की शाही कला में भी पाया जाता है, जो कांस्य युग के कुलीन वर्ग के साझा वैचारिक प्रतीक का प्रतिनिधित्व करता है।",
    "Case Study: The Pashupati Seal Iconography": "केस स्टडी: पशुपति मुहर का अंकन",
    "A steatite seal from Mohenjo-daro depicting a seated deity in yogic pose. It is surrounded by an elephant, tiger, rhino, buffalo, and two deer, representing Lord of Animals.": "मोहनजोदड़ो से प्राप्त सेलखड़ी की मुहर जिस पर योग मुद्रा में बैठे देवता दिखाए गए हैं। वह एक हाथी, बाघ, गेंडा, भैंसा और दो हिरणों से घिरे हैं, जो पशुओं के स्वामी (पशुपति) को दर्शाते हैं।",
    "Case Study: The Daimabad Copper Hoard": "केस स्टडी: दैमाबाद का तांबे का भंडार",
    "A cache of solid copper sculptures (chariot, bull, elephant, rhino) weighing over 60 kg, showing that metallurgy survived into the peripheral Late phase.": "60 किलोग्राम से अधिक वजन वाली तांबे की ठोस मूर्तियों (रथ, बैल, हाथी, गेंडा) का एक भंडार, जो दर्शाता है कि बाहरी उत्तर चरण में भी धातु कर्म जीवित रहा।",
    "Case Study: Cemetery R-37 Burials at Harappa": "केस स्टडी: हड़प्पा में कब्रिस्तान R-37 शवाधान",
    "Excavations revealed bodies laid in north-south orientation with pottery. One burial had a wooden coffin of cedar, showing trade links with the Himalayas.": "उत्खनन से उत्तर-दक्षिण दिशा में दफनाए गए शव मिले हैं जिनके साथ मिट्टी के बर्तन रखे थे। एक कब्र से देवदार की लकड़ी का ताबूत मिला है, जो हिमालय क्षेत्र के साथ व्यापारिक संबंधों को दर्शाता है।",
    "Teach the Concept: The Lost-Wax Method": "अवधारणा को समझें: लुप्त-मोम विधि",
    "Explain the step-by-step process of lost-wax casting (wax model, clay layer, heating, draining, metal pouring, breaking clay mold) used to make the Dancing Girl.": "नर्तकी की मूर्ति बनाने के लिए उपयोग की जाने वाली लुप्त-मोम ढलाई की चरण-दर-चरण प्रक्रिया (मोम का मॉडल, मिट्टी की परत लगाना, गर्म करना, मोम बाहर निकालना, धातु डालना, मिट्टी का सांचा तोड़ना) समझाएं।",
    "Teach the Concept: Harappan Faience Production": "अवधारणा को समझें: हड़प्पा फेयॉन्स का उत्पादन",
    "Explain how faience was made from crushed quartz/sand mixed with color glaze, then fired to create glassy, turquoise beads, representing a luxury industry.": "समझाएं कि कैसे पिसे हुए क्वार्ट्ज/रेत को रंगीन गोंद के साथ मिलाकर, और फिर गर्म करके कांच जैसी चमकदार, फ़िरोज़ा मोतियों का निर्माण किया जाता था, जो एक विलासितापूर्ण उद्योग का प्रतिनिधित्व करता था।",
    "Teach the Concept: The Cubical Chert Weights System": "अवधारणा को समझें: घनाकार चर्ट बाट प्रणाली",
    "Highlight how Harappan weights followed a binary system (1, 2, 4, 8, 16, 32...) for lighter weights and a decimal system for higher weights, indicating strict trade standards.": "बताएं कि कैसे हड़प्पा के बाट कम वजन के लिए द्वि-आधारी प्रणाली (1, 2, 4, 8, 16, 32...) और उच्च वजन के लिए दशमलव प्रणाली का पालन करते थे, जो कड़े व्यापारिक मानकों को दर्शाता है।"
}

def translate_to_hindi(eng_item):
    hin_item = {
        "type": eng_item["type"],
        "q": TRANS_MAP.get(eng_item["q"], eng_item["q"]),
        "sol": TRANS_MAP.get(eng_item["sol"], eng_item["sol"])
    }
    
    if "opts" in eng_item:
        hin_item["opts"] = [TRANS_MAP.get(o, o) for o in eng_item["opts"]]
        hin_item["ans"] = eng_item["ans"]
        
    if "ans" in eng_item and "opts" not in eng_item:
        if isinstance(eng_item["ans"], bool):
            hin_item["ans"] = eng_item["ans"]
        elif isinstance(eng_item["ans"], str):
            hin_item["ans"] = TRANS_MAP.get(eng_item["ans"], eng_item["ans"])
            
    if "items" in eng_item:
        hin_item["items"] = [{"left": TRANS_MAP.get(it["left"], it["left"]), "key": it["key"]} for it in eng_item["items"]]
        hin_item["options"] = [{"val": opt["val"], "text": TRANS_MAP.get(opt["text"], opt["text"])} for opt in eng_item["options"]]
        
    return hin_item

# Populate masteryZone arrays
for item in s1_mastery_eng:
    eng_data["deepDive"]["sections"][0]["masteryZone"].append(item)
    hin_data["deepDive"]["sections"][0]["masteryZone"].append(translate_to_hindi(item))

for item in s2_mastery_eng:
    eng_data["deepDive"]["sections"][1]["masteryZone"].append(item)
    hin_data["deepDive"]["sections"][1]["masteryZone"].append(translate_to_hindi(item))

for item in s3_mastery_eng:
    eng_data["deepDive"]["sections"][2]["masteryZone"].append(item)
    hin_data["deepDive"]["sections"][2]["masteryZone"].append(translate_to_hindi(item))

mock_data_eng = [
    (
        "Match the boundary sites of the Indus Civilisation with their respective rivers:\n1. Manda - Chenab\n2. Daimabad - Pravara\n3. Sutkagendor - Dasht\n4. Alamgirpur - Hindon\nWhich of the pairs given above are correct?",
        ["1, 2, 3 and 4", "1 and 2 only", "2, 3 and 4 only", "1, 3 and 4 only"],
        0,
        "All boundary sites are correctly matched to their rivers."
    ),
    (
        "Consider the following statements regarding Dholavira:\n1. It is divided into three sections: Citadel, Middle Town, and Lower Town.\n2. It contains spectacular stone water reservoirs and dams.\n3. It yielded a signboard with ten large Indus script characters.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All three statements represent unique characteristics of Dholavira."
    ),
    (
        "Which of the following statements is/are correct regarding Chanhudaro?\n1. It was a craft center specializing in bead-making, seal-cutting, and shell-working.\n2. It is the only major Harappan city that completely lacks a fortified citadel.\nSelect the correct answer:",
        ["Both 1 and 2", "1 only", "2 only", "Neither 1 nor 2"],
        0,
        "Chanhudaro was an unfortified craft and bead-making center."
    ),
    (
        "Mesopotamian cuneiform tablets from the Akkadian period mention trade with Meluhha. Meluhha refers to which region?",
        ["The Indus Valley region", "Ancient Bahrain", "Ancient Oman", "The Egyptian Delta"],
        0,
        "Meluhha was the Mesopotamian term for the Indus Civilisation."
    ),
    (
        "The Great Bath of Mohenjo-daro was made water-tight by applying a layer of:",
        ["Natural bitumen (tar)", "Lime mortar", "Glazed tiles", "Gypsum plaster"],
        0,
        "A layer of natural bitumen (tar) was applied to prevent leaks."
    ),
    (
        "Consider the following statements regarding Harappan burials:\n1. Cemetery R-37 at Harappa contains burials where bodies were placed in cedar wooden coffins.\n2. Lothal has yielded joint burials containing skeletons of a male and a female.\nWhich of the statements given above is/are correct?",
        ["Both 1 and 2", "1 only", "2 only", "Neither 1 nor 2"],
        0,
        "Both statements represent verified archaeological discoveries."
    ),
    (
        "Rakhigarhi in Haryana is significant in Indus Valley studies because it is:",
        ["The largest Harappan site by area, containing nine mounds", "The oldest site containing Hakra Ware", "The only port city in northern India", "The site showing the earliest ploughed field"],
        0,
        "Rakhigarhi is the largest Harappan site, covering over 350 hectares."
    ),
    (
        "Surkotada is a key archaeological site in Gujarat famous for:",
        ["The reported skeletal remains of a horse", "A massive brick-built dockyard", "A trefoil shawl wearing stone statue", "Woven cotton cloth fragments"],
        0,
        "Surkotada reported horse bones, though horse presence is debated."
    ),
    (
        "The Harappan commercial system relied on weights made of chert. What was the base unit of the binary system?",
        ["13.63 grams (equivalent to ratio 16)", "5.5 grams", "25.0 grams", "1.0 gram"],
        0,
        "The base weight was 13.63 grams, representing the unit ratio 16."
    ),
    (
        "The Dancing Girl bronze statue shows advanced metallurgy. Which process was used for its manufacture?",
        ["Lost-wax casting (cire perdue)", "Direct iron smelting", "Sheet copper riveting", "Cold metal chiseling"],
        0,
        "Lost-wax casting was used for the bronze Dancing Girl."
    )
]

mock_data_hin = [
    (
        "सिंधु सभ्यता के सीमा स्थलों को उनकी संबंधित नदियों से सुमेलित करें:\n1. मांडा - चिनाब\n2. दैमाबाद - प्रवर\n3. सुतकागेंडोर - दश्त\n4. आलमगीरपुर - हिंडन\nउपरोक्त में से कौन से जोड़े सही हैं?",
        ["1, 2, 3 और 4", "केवल 1 और 2", "केवल 2, 3 और 4", "केवल 1, 3 और 4"],
        0,
        "सभी सीमा स्थल अपनी नदियों से सही सुमेलित हैं।"
    ),
    (
        "धोलावीरा के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. यह तीन भागों में विभाजित है: किला (Citadel), मध्य नगर (Middle Town), और निचला नगर (Lower Town)।\n2. इसमें पत्थर के शानदार जलाशय और बांध मिले हैं।\n3. यहाँ से सिंधु लिपि के दस बड़े अक्षरों वाला एक साइनबोर्ड प्राप्त हुआ है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन धोलावीरा की अनूठी विशेषताओं को दर्शाते हैं।"
    ),
    (
        "चन्हुदड़ो के संबंध में निम्नलिखित में से कौन सा/से कथन सही है/हैं?\n1. यह मनके बनाने, मुहर काटने और शंख के काम में विशेषज्ञता रखने वाला एक शिल्प केंद्र था।\n2. यह एकमात्र प्रमुख हड़प्पा शहर है जिसमें कोई भी किला (Citadel) नहीं है।\nसही उत्तर चुनें:",
        ["1 और 2 दोनों", "केवल 1", "केवल 2", "न तो 1 न ही 2"],
        0,
        "चन्हुदड़ो बिना किलेबंदी वाला एक औद्योगिक शिल्प केंद्र था।"
    ),
    (
        "अक्कड़ काल की मेसोपोटामिया की कीलाक्षर (cuneiform) पट्टियों में मेलुहा के साथ व्यापार का उल्लेख है। मेलुहा किस क्षेत्र को संदर्भित करता है?",
        ["सिंधु घाटी क्षेत्र", "प्राचीन बहरीन", "प्राचीन ओमान", "मिस्र का डेल्टा"],
        0,
        "मेलुहा सिंधु सभ्यता के लिए प्रयुक्त मेसोपोटामियाई शब्द था।"
    ),
    (
        "मोहनजोदड़ो के विशाल स्नानागार (Great Bath) को पानी के रिसाव से सुरक्षित करने के लिए किसकी परत लगाई गई थी?",
        ["प्राकृतिक डामर (तारकोल/bitumen)", "चूने का गारा", "कांच की टाइलें", "जिप्सम का प्लास्टर"],
        0,
        "पानी का रिसाव रोकने के लिए ईंटों पर तारकोल (बिटुमेन) की परत लगाई गई थी।"
    ),
    (
        "हड़प्पा के शवाधानों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. हड़प्पा के सिमेट्री R-37 में शवों को देवदार की लकड़ी के ताबूत में दफनाने के प्रमाण मिले हैं।\n2. लोथल से एक ही कब्र में पुरुष और महिला के संयुक्त शवाधान के प्रमाण मिले हैं।\nसही कथन चुनें:",
        ["1 और 2 दोनों", "केवल 1", "केवल 2", "न तो 1 न ही 2"],
        0,
        "दोनों कथन प्रमाणित पुरातत्वीय खोजों को दर्शाते हैं।"
    ),
    (
        "हरियाणा का राखीगढ़ी स्थल सिंधु घाटी के अध्ययन में महत्वपूर्ण है क्योंकि यह:",
        ["नौ टीलों वाला सबसे बड़ा भौगोलिक हड़प्पा स्थल है", "हाकड़ा बर्तन दर्शाने वाला सबसे पुराना स्थल है", "उत्तर भारत का एकमात्र बंदरगाह है", "सबसे पुराना जुता हुआ खेत दर्शाने वाला स्थल है"],
        0,
        "राखीगढ़ी वर्तमान में सबसे बड़ा भौगोलिक हड़प्पा स्थल है, जो 350 हेक्टेयर से अधिक में फैला है।"
    ),
    (
        "गुजरात का सुरकोटदा स्थल मुख्य रूप से किसके लिए प्रसिद्ध है?",
        ["घोड़े के अस्थि अवशेषों की खोज के लिए", "baked-brick गोदी बाड़े के लिए", "तिपतिया शॉल ओढ़े पत्थर की मूर्ति के लिए", "बुने हुए सूती कपड़े के अवशेष के लिए"],
        0,
        "सुरकोटदा से घोड़े के अवशेषों की रिपोर्ट की गई है, जो विद्वानों में बहस का विषय है।"
    ),
    (
        "हड़प्पा की वजन प्रणाली चर्ट के बाटों पर निर्भर थी। द्वि-आधारी (binary) बाटों की आधार इकाई का मान क्या था?",
        ["13.63 ग्राम (अनुपात 16)", "5.5 ग्राम", "25.0 ग्राम", "1.0 ग्राम"],
        0,
        "आधार बाट 13.63 ग्राम का था, जो अनुपात 16 का प्रतिनिधित्व करता था।"
    ),
    (
        "कांस्य की नर्तकी की मूर्ति धातु कर्म की उन्नत अवस्था को दर्शाती है। इसके निर्माण में किस विधि का उपयोग किया गया था?",
        ["लुप्त-मोम विधि (lost-wax/cire perdue)", "सीधे लोहे को पिघलाना", "तांबे की चादरें जोड़ना", "ठंडी नक्काशी करना"],
        0,
        "नर्तकी की मूर्ति को खोया-मोम (lost-wax) विधि से ढाला गया था।"
    )
]

# Process and Append English Practice and Mock Test
for item in practice_data_eng:
    eng_data["practiceQuestions"].append({
        "q": item[0],
        "opts": item[1],
        "ans": item[2],
        "sol": item[3]
    })

for item in mock_data_eng:
    eng_data["mockTestQuestions"].append({
        "q": item[0],
        "opts": item[1],
        "ans": item[2],
        "sol": item[3]
    })

# Process and Append Hindi Practice and Mock Test
for item in practice_data_hin:
    hin_data["practiceQuestions"].append({
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

# Write JSON Files
with open(os.path.join(ENG_DIR, "content.json"), "w", encoding="utf-8") as f:
    json.dump(eng_data, f, ensure_ascii=False, indent=2)

with open(os.path.join(HIN_DIR, "content.json"), "w", encoding="utf-8") as f:
    json.dump(hin_data, f, ensure_ascii=False, indent=2)

print("JSON files built successfully with UPSC-style practice questions!")
print(f"English: Sections: {len(eng_data['deepDive']['sections'])} | S1 Mastery: {len(eng_data['deepDive']['sections'][0]['masteryZone'])} | Practice: {len(eng_data['practiceQuestions'])} | Mock: {len(eng_data['mockTestQuestions'])}")
print(f"Hindi: Sections: {len(hin_data['deepDive']['sections'])} | S1 Mastery: {len(hin_data['deepDive']['sections'][0]['masteryZone'])} | Practice: {len(hin_data['practiceQuestions'])} | Mock: {len(hin_data['mockTestQuestions'])}")
