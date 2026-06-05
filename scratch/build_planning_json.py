import json
import os

ENG_DIR = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\HarappanIndus-Valley-Civilisation\Town-Planning"
HIN_DIR = os.path.join(ENG_DIR, "hi")
os.makedirs(HIN_DIR, exist_ok=True)

# English base structure
eng_data = {
    "breadcrumbs": {
        "parent": "UPSC Syllabus",
        "parentUrl": "/upsc/",
        "current": "Town Planning"
    },
    "hero": {
        "title": "Harappan Town Planning",
        "description": "Master the grid system, citadels, sanitation engineering, metrology, and public civic architecture of the Indus Valley Civilisation for UPSC GS-1."
    },
    "labels": {
        "clickToExpand": "Click to expand details",
        "mockIntro": {
            "title": "Interactive UPSC Mock Test",
            "description": "Test your knowledge on Harappan Town Planning. This timed test contains 10 high-quality, exam-standard questions with negative marking. Perfect for self-evaluation.",
            "startBtn": "Start Mock Test"
        },
        "mockPlay": {
            "prevBtn": "Previous Question",
            "nextBtn": "Next Question",
            "submitBtn": "Submit Test"
        }
    },
    "timeline": {
        "title": "Urban Development and Metrology",
        "description": "Explore the structural components, drainage layouts, and civic systems of Harappan town planning.",
        "cards": [
            {
                "period": "Grid Planning",
                "date": "Citadel & Residential Grids",
                "details": "Establishment of western fortified citadels and eastern lower towns. Avenues crossing at right angles along cardinal wind directions for natural street cleaning."
            },
            {
                "period": "Sanitation Layout",
                "date": "Drainage & Sewerage Networks",
                "details": "Development of brick-lined house drains connecting to covered street conduits, equipped with soak pits (cesspits) and cleanup manholes."
            },
            {
                "period": "Civic Standards",
                "date": "Metrology & Brick Ratios",
                "details": "Introduction of highly standardized weights (binary chert blocks) and a uniform brick ratio of 4:2:1 for burnt and mud bricks."
            }
        ]
    },
    "mnemonics": {
        "title": "Mnemonics & Memory Hacks",
        "description": "Use these visual memory hooks to retain critical facts about Harappan town planning and civic systems for the UPSC Civil Services Examination.",
        "items": [
            {
                "title": "Mnemonic 1: Standard Brick Dimensions",
                "phrase": "\"4-2-1 (Four-To-One) - Wall Builders\"",
                "decryption": "Harappan brick dimensions followed the strict ratio **4:2:1** (Length = 4 units, Width = 2 units, Thickness = 1 unit)."
            },
            {
                "title": "Mnemonic 2: Street Layout Cardinal Directions",
                "phrase": "\"N-S-E-W (Wind Swept Streets) - Grid Plan\"",
                "decryption": "Streets aligned to **North-South** and **East-West** so winds could blow through and clean them naturally."
            },
            {
                "title": "Mnemonic 3: Dual Sector City Division",
                "phrase": "\"C-L (Citadel Left, Lower right) - Class Division\"",
                "decryption": "**Citadel** (West/Left - raised, administrative), **Lower Town** (East/Right - residential, artisans) (**CL**)."
            }
        ]
    },
    "flashcards": {
        "title": "Active Recall Flashcards",
        "description": "Flashcards are key to mastering fact-dense UPSC questions. Click on any card below to flip it and reveal the answer.",
        "items": [
            {
                "question": "What is the standard ratio of Harappan bricks (length:width:thickness)?",
                "answer": "<strong>4:2:1</strong>. (For example: 28cm x 14cm x 7cm in standard houses).",
                "icon": "fa-cubes"
            },
            {
                "question": "Which site shows a radial layout of streets rather than the standard grid system?",
                "answer": "<strong>Banawali</strong> in Haryana, where streets radiate from the fortified citadel mound.",
                "icon": "fa-dharmachakra"
            },
            {
                "question": "How did Harappans manage wastewater sanitation inside houses?",
                "answer": "House drains emptied into brick-lined <strong>soak pits (cesspools)</strong> beneath the street surface, filtering solid waste before water entered main drains.",
                "icon": "fa-faucet-drip"
            },
            {
                "question": "Name the materials used to waterproofing the Great Bath of Mohenjo-daro.",
                "answer": "<strong>Gypsum mortar</strong> for binding bricks and a layer of <strong>natural bitumen (tar)</strong> to prevent leakage.",
                "icon": "fa-water"
            },
            {
                "question": "Which site utilized dressed limestone instead of baked bricks for town walls?",
                "answer": "<strong>Dholavira</strong> in Kutch, which also featured massive stone check dams and reservoirs.",
                "icon": "fa-hill-rockslide"
            }
        ]
    },
    "deepDive": {
        "title": "Syllabus Core Study Notes (Deep-Dive)",
        "description": "Master the grid system, Citadel-Lower Town structures, sanitation networks, and civic engineering of the Harappan Civilisation.",
        "sections": [
            {
                "title": "1. Grid Iron Streets, Citadels & Lower Towns",
                "content": """<p>The hallmark of Harappan urbanism is its grid iron planning. Avenues crossed at right angles, dividing the city into rectangular sectors. Most cities had a dual-sector division.</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-grid-3"></i> Street Layout & Cardinal Alignment</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>Wind-Swept Cleansing:</strong> Streets were aligned strictly along North-South and East-West directions. This utilized prevailing winds to sweep dust away naturally.</li>
      <li><strong>Grid Pattern:</strong> Streets crossed at right angles, creating a grid plan (e.g. at Mohenjo-daro). Radial street layouts (non-grid) are found at Banawali.</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-fort-awesome"></i> Citadel vs. Lower Town Dichotomy</div>
    <p style="font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;">
      Cities were typically split into a western raised <strong>Citadel</strong> (built on mud-brick platforms for public assembly, administrative staff, and granaries) and an eastern <strong>Lower Town</strong> (larger, residential, for artisans and merchants). Fortification walls surrounded both sections. Dholavira represents a unique three-tier division (Citadel, Middle Town, Lower Town), while Chanhudaro is the only major town lacking a citadel.
    </p>
  </div>
</div>""",
                "masteryZone": []
            },
            {
                "title": "2. Sanitation, Public Drainage & Private Drains",
                "content": """<p>No contemporary civilization, including Egypt and Mesopotamia, matched the sanitation standards of the Indus Valley. Civic management prioritized waste management and clean water supply.</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-sink"></i> House Drains & Covered Channels</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>House Drains:</strong> Bathrooms and kitchens had brick-paved floors sloping toward a corner wall inlet, leading water out via terracotta pipe sleeves.</li>
      <li><strong>Covered Sewers:</strong> Main street drains were covered with brick slabs or stone blocks. They had regular inspection chambers (manholes) for cleanup.</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-trash-can"></i> Soak Pits & Water Supply</div>
    <p style="font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;">
      House drains emptied into brick-lined <strong>soak pits (cesspools)</strong> where solid debris settled. Only the liquid runoff entered the public street drains. Water supply was secured by private house wells. Mohenjo-daro had over 700 brick-lined public and private wells. Kalibangan is unique for its use of wooden drainage conduits instead of baked bricks.
    </p>
  </div>
</div>""",
                "masteryZone": []
            },
            {
                "title": "3. Brick Technology, Metrology & Civic Architecture",
                "content": """<p>Standardisation proves a highly organized administrative authority, visible in brick dimensions, trade weight systems, and massive monuments.</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-scale-balanced"></i> Brick Ratios & Standard Weights</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>Brick Ratio:</strong> Burnt (baked) and sun-dried bricks followed a strict ratio of <strong>4:2:1</strong> (Length:Width:Thickness) across all sites.</li>
      <li><strong>Standardized Metrology:</strong> Cubical weights made of hard chert followed a binary system (1, 2, 4, 8, 16, 32, 64) for lower weights and decimal for higher weights. The basic unit was 13.63g.</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-monument"></i> Monumental Civic Structures</div>
    <p style="font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;">
      <strong>The Great Bath</strong> (Mohenjo-daro) features brick-paved walls sealed with natural bitumen. <strong>The Great Granaries</strong> at Harappa and Mohenjo-daro were raised on brick platforms with ventilation ducts to keep grain dry. <strong>Assembly Halls</strong> with pillars indicate spaces for municipal council and collective decisions.
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
        "current": "नगर नियोजन"
    },
    "hero": {
        "title": "हड़प्पा नगर नियोजन",
        "description": "यूपीएससी परीक्षा (GS-1) के लिए सिंधु घाटी सभ्यता की ग्रिड प्रणाली, किलों, जल निकासी व्यवस्था, ईंटों की वास्तुकला और नागरिक स्मारकों का अध्ययन करें।"
    },
    "labels": {
        "clickToExpand": "विवरण देखने के लिए क्लिक करें",
        "mockIntro": {
            "title": "इंटरैक्टिव परीक्षा मॉक टेस्ट",
            "description": "हड़प्पा नगर नियोजन के संबंध में अपनी तैयारी का मूल्यांकन करें। इस समयबद्ध परीक्षण में नकारात्मक अंकन के साथ 10 उच्च-स्तरीय यूपीएससी मानक के प्रश्न शामिल हैं।",
            "startBtn": "मॉक टेस्ट शुरू करें"
        },
        "mockPlay": {
            "prevBtn": "पिछला प्रश्न",
            "nextBtn": "अगला प्रश्न",
            "submitBtn": "परीक्षण जमा करें"
        }
    },
    "timeline": {
        "title": "शहरी विकास और नागरिक मानक",
        "description": "हड़प्पा नगर नियोजन के प्रमुख घटकों, संरचनात्मक प्रतिरूपों और नागरिक व्यवस्थाओं का कालानुक्रमिक अध्ययन करें।",
        "cards": [
            {
                "period": "ग्रिड नियोजन",
                "date": "किला और आवासीय क्षेत्र",
                "details": "पश्चिमी किलेबंद किलों और पूर्वी निचले शहरों की स्थापना। हवा की दिशा में समकोण पर काटती सड़कों का जाल, जिससे स्वतः सफाई होती थी।"
            },
            {
                "period": "स्वच्छता व्यवस्था",
                "date": "नाली और सीवरेज नेटवर्क",
                "details": "घरों की नालियों का सड़कों के ढके हुए सीवरों से जुड़ाव। ठोस कचरे के निपटान के लिए शोषक गड्ढों और नालियों की सफाई के लिए मैनहोल का उपयोग।"
            },
            {
                "period": "नागरिक मानक",
                "date": "बाट-माप और ईंट अनुपात",
                "details": "चर्ट पत्थर के मानकीकृत द्वि-आधारी बाटों का उपयोग। पकी और कच्ची ईंटों के लिए 4:2:1 के एक समान अनुपात का पालन।"
            }
        ]
    },
    "mnemonics": {
        "title": "याद रखने के सूत्र (Mnemonics)",
        "description": "यूपीएससी परीक्षा के लिए हड़प्पा नगर नियोजन से संबंधित तथ्यों को आसानी से याद रखने के लिए इन दृश्य सूत्रों का उपयोग करें।",
        "items": [
            {
                "title": "याद रखने का सूत्र 1: मानक ईंटों का अनुपात",
                "phrase": "\"4-2-1 (चार-दो-एक) - दीवार निर्माण\"",
                "decryption": "हड़प्पा की ईंटों के आकार का अनुपात हमेशा **4:2:1** (लंबाई:चौड़ाई:मोटाई) होता था।"
            },
            {
                "title": "याद रखने का सूत्र 2: सड़कों का नियोजन",
                "phrase": "\"N-S-E-W (हवा और सड़क) - ग्रिड पैटर्न\"",
                "decryption": "सड़कें **उत्तर-दक्षिण** और **पूर्व-पश्चिम** दिशा में सीधी होती थीं ताकि हवा से स्वतः सफाई हो सके।"
            },
            {
                "title": "याद रखने का सूत्र 3: दोहरे नगर क्षेत्र",
                "phrase": "\"C-L (किला और निचला नगर) - सामाजिक विभाजन\"",
                "decryption": "**Citadel** (पश्चिम/किला - प्रशासनिक), **Lower Town** (पूर्व/निचला नगर - रिहायशी, कारीगर) (**CL**)।"
            }
        ]
    },
    "flashcards": {
        "title": "सक्रिय स्मरण फ्लैशकार्ड (Active Recall)",
        "description": "फ्लैशकार्ड्स तथ्य-प्रधान यूपीएससी प्रश्नों को याद रखने का सर्वोत्तम साधन हैं। उत्तर देखने के लिए नीचे दिए गए कार्ड्स पर क्लिक करें।",
        "items": [
            {
                "question": "हड़प्पा की ईंटों (लंबाई:चौड़ाई:मोटाई) का मानक अनुपात क्या है?",
                "answer": "<strong>4:2:1</strong>. (जैसे घरों में सामान्यतः 28 सेमी x 14 सेमी x 7 सेमी की ईंटें प्रयुक्त होती थीं)।",
                "icon": "fa-cubes"
            },
            {
                "question": "किस हड़प्पा स्थल पर सड़कों का ग्रिड प्रणाली के बजाय अरीय (radial) प्रतिरूप मिला है?",
                "answer": "हरियाणा के <strong>बनावली</strong> में, जहाँ सड़कें किले के टीले से बाहर की ओर अरीय रूप में व्यवस्थित थीं।",
                "icon": "fa-dharmachakra"
            },
            {
                "question": "हड़प्पावासी घरों के गंदे पानी का प्रबंधन कैसे करते थे?",
                "answer": "घर की नालियों का पानी सड़कों के नीचे बने <strong>शोषक गड्ढों (soak pits)</strong> में जाता था, जहाँ ठोस कचरा नीचे बैठ जाता था और केवल तरल पानी मुख्य नाली में जाता था।",
                "icon": "fa-faucet-drip"
            },
            {
                "question": "मोहनजोदड़ो के विशाल स्नानागार को जल-रोधी बनाने के लिए किन सामग्रियों का उपयोग किया गया था?",
                "answer": "ईंटों को जोड़ने के लिए <strong>जिप्सम गारे</strong> का और पानी का रिसाव रोकने के लिए <strong>प्राकृतिक डामर (बिटुमेन)</strong> की परत का उपयोग किया गया था।",
                "icon": "fa-water"
            },
            {
                "question": "किस स्थल पर किले की दीवारों के लिए पकी ईंटों के बजाय स्थानीय तराशे गए पत्थरों का उपयोग किया गया था?",
                "answer": "गुजरात के <strong>धोलावीरा</strong> में, जहाँ पानी संचित करने के लिए विशाल जलाशय भी मिले हैं।",
                "icon": "fa-hill-rockslide"
            }
        ]
    },
    "deepDive": {
        "title": "पाठ्यक्रम मुख्य नोट्स (गहन अध्ययन)",
        "description": "हड़प्पा सभ्यता की ग्रिड सड़कों, किला-निचले नगर के विभाजन, नालियों की स्वच्छता और वास्तुकला का गहन अध्ययन करें।",
        "sections": [
            {
                "title": "1. ग्रिड सड़कें, किला और निचला नगर",
                "content": """<p>हड़प्पा शहरीकरण की मुख्य विशेषता इसकी ग्रिड सड़कों का नियोजन है। सड़कें समकोण पर काटती थीं, जिससे पूरा शहर चौकोर खंडों में विभाजित हो जाता था। अधिकांश शहरों में दोहरा विभाजन था।</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-grid-3"></i> सड़कों का लेआउट और दिशा संरेखण</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>प्राकृतिक सफाई:</strong> सड़कें हमेशा उत्तर-दक्षिण और पूर्व-पश्चिम दिशा में सीधी बनाई जाती थीं। हवा चलने पर सड़कों की धूल स्वतः साफ हो जाती थी।</li>
      <li><strong>ग्रिड पैटर्न:</strong> सड़कें एक-दूसरे को समकोण पर काटती थीं (जैसे मोहनजोदड़ो में)। अरीय सड़कें (radial/non-grid) बनावली में पाई गई हैं।</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-fort-awesome"></i> किला बनाम निचला नगर</div>
    <p style="font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;">
      शहर सामान्यतः एक पश्चिमी ऊंचे <strong>किले (Citadel)</strong> (जो कच्चे चबूतरों पर प्रशासनिक भवनों, अन्नागारों और सार्वजनिक स्थलों के लिए बना था) और एक पूर्वी <strong>निचले नगर (Lower Town)</strong> (बड़ा, आवासीय और व्यापारियों के लिए) में विभाजित थे। धोलावीरा में त्रि-स्तरीय विभाजन (किला, मध्य नगर, निचला नगर) मिला है, जबकि चन्हुदड़ो में कोई किला नहीं था।
    </p>
  </div>
</div>""",
                "masteryZone": []
            },
            {
                "title": "2. स्वच्छता, सार्वजनिक नालियां और निजी जल निकासी",
                "content": """<p>मिस्र और मेसोपोटामिया जैसी समकालीन सभ्यताओं में जल निकासी और सार्वजनिक स्वच्छता की ऐसी उत्कृष्ट व्यवस्था कहीं नहीं थी। नागरिक प्रशासन में स्वच्छता को सर्वोच्च प्राथमिकता दी गई थी।</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-sink"></i> घरों की नालियां और ढके हुए मार्ग</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>घरों से जल निकासी:</strong> स्नानघरों में ढलान वाले फर्श होते थे, जहाँ कोने से पाइप निकाल कर बाहर गली की नाली से जोड़ा जाता था।</li>
      <li><strong>ढके हुए नाले:</strong> सड़क की मुख्य नालियों को ईंटों की शिलाओं या पत्थरों से ढका जाता था। नालियों की सफाई के लिए नियमित स्थानों पर मैनहोल बने थे।</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-trash-can"></i> शोषक गड्ढे और कुएं</div>
    <p style="font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;">
      घरों की नालियाँ पहले सड़क पर बने <strong>शोषक गड्ढों (soak pits)</strong> में गिरती थीं, जहाँ ठोस कचरा जमा हो जाता था और केवल तरल गंदा पानी मुख्य नाली में जाता था। घरों में पानी की आपूर्ति के लिए कुएं होते थे। मोहनजोदड़ो में 700 से अधिक कुएँ मिले हैं। कालीबंगन में नालियों के लिए पकी ईंटों के बजाय खोखली लकड़ी के पाइपों का उपयोग किया गया था।
    </p>
  </div>
</div>""",
                "masteryZone": []
            },
            {
                "title": "3. ईंट प्रौद्योगिकी, बाट-माप और नागरिक वास्तुकला",
                "content": """<p>एक समान बाट-माप, ईंटों का अनुपात और बड़े सार्वजनिक भवन एक सुगठित प्रशासनिक सत्ता की पुष्टि करते हैं।</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-scale-balanced"></i> ईंटों का अनुपात और बाट-माप</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>ईंटों का मानक:</strong> सभी स्थलों पर कच्ची और पकी ईंटें <strong>4:2:1</strong> (लंबाई:चौड़ाई:मोटाई) के निश्चित अनुपात में बनाई जाती थीं।</li>
      <li><strong>मानकीकृत बाट:</strong> चर्ट पत्थर के घनाकार बाट कम वजन के लिए द्वि-आधारी (binary - 1, 2, 4, 8, 16, 32...) और अधिक वजन के लिए दशमलव (decimal) प्रणाली पर आधारित थे। आधार इकाई 13.63 ग्राम थी।</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-monument"></i> सार्वजनिक स्मारक भवन</div>
    <p style="font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;">
      <strong>विशाल स्नानागार (Great Bath)</strong> पकी ईंटों और डामर की सील से बना था। <strong>विशाल अन्नागार (Granaries)</strong> ईंटों के ऊंचे चबूतरे पर हवा आने-जाने के रास्तों सहित बनाए जाते थे ताकि अनाज में सीलन न लगे। स्तंभों वाले <strong>सभा भवन (Assembly Halls)</strong> नागरिक परिषद या सामूहिक निर्णयों के स्थलों को दर्शाते हैं।
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
        "Consider the following statements regarding the layout of streets in Harappan cities:\n1. Main streets were aligned strictly along North-South and East-West directions to allow prevailing winds to clean them naturally.\n2. Streets crossed at right angles, forming a highly organized grid iron pattern in all major settlements.\n3. The street layout at Banawali deviated from the grid pattern, displaying a radial layout of roads radiating from the citadel.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All three statements are correct, explaining the cardinal alignments, grid system, and Banawali's radial street planning."
    ),
    (
        "With reference to the division of Harappan cities, consider the following statements:\n1. Most settlements were divided into a western raised Citadel on a mud-brick platform and an eastern Lower Town.\n2. The Citadel housed public, administrative, and religious monuments while the Lower Town was primarily residential.\n3. Dholavira is uniquely divided into three fortified sections: Citadel, Middle Town, and Lower Town.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All statements are correct, illustrating the standard two-tier city division and Dholavira's unique three-tier planning."
    ),
    (
        "Consider the following statements regarding the Citadel-free settlements of the Indus Civilisation:\n1. Chanhudaro in Sindh was a major craft suburb that completely lacked a fortified citadel mound.\n2. In the absence of a citadel, Chanhudaro did not display standard Harappan weights or drainage systems.\n3. Lothal had no physical wall separating its Citadel from its residential sectors.\nWhich of the statements given above is/are correct?",
        ["1 only", "1 and 2 only", "1 and 3 only", "1, 2 and 3"],
        0,
        "Statement 1 is correct. Statement 2 is incorrect: Chanhudaro utilized standard Harappan weights, measures, and drainage systems despite lacking a citadel. Statement 3 is incorrect: Lothal's Citadel was separated from the Lower Town by a mud-brick wall."
    ),
    (
        "With reference to the drainage systems of the Indus Valley Civilisation, consider the following statements:\n1. Main street drains were built of baked bricks and remained completely uncovered for air ventilation.\n2. Inspection chambers or cleanup manholes were provided at regular intervals along the street drains.\n3. Drains were constructed with a slight gradient or slope to ensure smooth water flow.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        1,
        "Statements 2 and 3 are correct. Statement 1 is incorrect: Main street drains were covered with brick slabs or stone blocks to ensure public health and sanitation."
    ),
    (
        "Consider the following statements regarding the domestic drainage inside Harappan houses:\n1. Bathrooms and kitchens had brick-paved floors sloping towards a corner outlet.\n2. Wastewater entered a brick-lined soak pit (cesspit) beneath the street to trap solid waste before entering public drains.\n3. House drains were constructed using wooden pipes wrapped in leather at all major sites.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "2 and 3 only", "1 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: House drains were constructed of baked bricks and terracotta pipes; only Kalibangan used wooden conduits, which was a regional anomaly."
    ),
    (
        "With reference to the water supply in Harappan towns, consider the following statements:\n1. Almost every house at Mohenjo-daro featured a private brick-lined water well.\n2. Over 700 wells have been excavated at Mohenjo-daro alone.\n3. Dholavira relied entirely on private household wells because surface water was absent in Kutch.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: Dholavira relied on massive stone-cut reservoirs to harvest rainwater runoff because groundwater wells in Kutch were brackish and scarce."
    ),
    (
        "Consider the following statements regarding the bricks used by Harappan builders:\n1. The dimensions of both burnt and sun-dried bricks followed a strict ratio of 4:2:1 (length:width:thickness).\n2. Standard brick sizes for houses were typically 28cm x 14cm x 7cm.\n3. Mud-brick structures were reserved exclusively for Citadel fortifications, while private houses used burnt bricks.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: Mud bricks were widely used for house platforms, lower town houses, and courtyard walls, while burnt bricks were preferred where water contact was high (drains, wells, baths)."
    ),
    (
        "With reference to the metrological systems of the Harappans, consider the following statements:\n1. Weights were standardized cubical blocks typically carved from hard chert.\n2. The binary system of weights (1, 2, 4, 8, 16, 32, 64) was used for lower weights.\n3. Decimal progressions were used for higher values, indicating a highly advanced mathematical scale.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All three statements are correct and define the standardized metrology of the Harappan trade system."
    ),
    (
        "Consider the following statements regarding the Great Bath of Mohenjo-daro:\n1. It is a rectangular basin lined with tightly fitted baked bricks and bound with gypsum mortar.\n2. Waterproofing was achieved by applying a thick layer of natural bitumen (asphalt) over the brickwork.\n3. It was located in the Lower Town and was used for municipal swimming and domestic washing.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "2 and 3 only", "1 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: The Great Bath was located on the Citadel and was used for collective ritual bathing and purification, not municipal washing."
    ),
    (
        "With reference to the granaries in Harappan town planning, consider the following statements:\n1. The Great Granary at Mohenjo-daro featured a grid of brick podiums raised to support a massive wooden superstructure.\n2. Parallel rows of smaller granaries at Harappa were constructed outside the citadel near the river bank.\n3. Granaries were equipped with under-floor air ventilation ducts to prevent moisture accumulation.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All three statements are correct, describing the design, location, and structural ventilation of Harappan granaries."
    ),
    (
        "Consider the following statements regarding Dholavira's water management system:\n1. It featured check dams built across seasonal streams to channel water into massive stone reservoirs.\n2. The reservoirs surrounding the Citadel were cut directly into local limestone rocks.\n3. Dholavira relied on a system of pottery pipelines to bring freshwater from rivers located 50 miles away.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: Water was harvested locally via check dams and channels diverting seasonal runoff from Kutch's hills, not from distant rivers."
    ),
    (
        "With reference to the fortifications of Harappan towns, consider the following statements:\n1. Fortifications were built primarily of mud-brick, faced with burnt brick or rubble stone in peripheral areas.\n2. Fortification walls featured rectangular bastions, defensive gateways, and watchtowers.\n3. Sites like Chanhudaro and Balakot were enclosed by massive stone ramparts over 10 meters thick.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "2 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: Chanhudaro completely lacked fortification walls, and Balakot had mud-brick defensive walls, not 10-meter stone ramparts."
    ),
    (
        "Consider the following statements regarding the residential houses of the Harappans:\n1. Houses were built facing the main avenues to facilitate commercial displays.\n2. Entrance doors typically opened into side lanes rather than main streets, ensuring privacy.\n3. Most houses featured a central courtyard surrounded by rooms, bathrooms, and staircases indicating double-story structures.\nWhich of the statements given above are correct?",
        ["2 and 3 only", "1 and 2 only", "1 and 3 only", "1, 2 and 3"],
        0,
        "Statements 2 and 3 are correct. Statement 1 is incorrect: Harappan house entrances opened into side alleys, and main walls facing the streets lacked windows to maintain privacy and reduce dust entry."
    ),
    (
        "With reference to the site of Kalibangan, consider the following statements:\n1. The town featured separate fortifications for its Citadel and residential Lower Town.\n2. The city completely lacked a public baked-brick drainage system, utilizing wooden drain pipes instead.\n3. Pre-Harappan levels showed grid plowing, which aligns with the grid pattern of the mature town planning.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, describing Kalibangan's fortifications, unique wooden drains, and early agricultural grid lines."
    ),
    (
        "Consider the following statements regarding the site of Banawali:\n1. The streets did not follow a grid pattern, resulting in irregular radial layouts.\n2. A fortified wall separated the Citadel from the Lower Town, yet both were built on a single mound.\n3. Its drainage system was poor, using earthenware jars placed at street corners to collect waste.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All three statements are correct and define the regional town planning characteristics of Banawali."
    ),
    (
        "With reference to the metrological standardisation, consider the following statements:\n1. Weights made of chert were used primarily in Gujarat, while steatite weights were used in Punjab.\n2. The standard unit of weight ratio 16 was equivalent to 13.63 grams.\n3. Linear measurement systems used bronze scales and ivory rulers divided into precise units.\nWhich of the statements given above are correct?",
        ["2 and 3 only", "1 and 2 only", "1 and 3 only", "1, 2 and 3"],
        0,
        "Statements 2 and 3 are correct. Statement 1 is incorrect: Standardized chert weights were used uniformly across the entire Harappan territory, proving a centralized economic system."
    ),
    (
        "Consider the following statements regarding the Assembly Hall at Mohenjo-daro:\n1. It is a large square hall containing twenty brick pillars arranged in rows.\n2. It is located on the Citadel and is believed to have functioned as a municipal council hall.\n3. It was decorated with relief sculptures of Harappan rulers and deities.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "2 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: No relief sculptures or representations of rulers or deities have been found inside any Harappan public buildings."
    ),
    (
        "With reference to Harappan sanitary engineering, consider the following statements:\n1. Wastewater from bathrooms was discharged directly onto streets to be swept away.\n2. Vertical terracotta pipes embedded inside house walls channeled waste from upper floors to street drains.\n3. Street drains were built below road level and paved with flat bricks.\nWhich of the statements given above are correct?",
        ["2 and 3 only", "1 and 2 only", "1 and 3 only", "1, 2 and 3"],
        0,
        "Statements 2 and 3 are correct. Statement 1 is incorrect: House waste did not run onto streets; it was channeled via wall pipes into brick-lined pits or street drains to maintain cleanliness."
    ),
    (
        "Consider the following statements regarding Dholavira's stone masonry:\n1. Local dressed limestone was used for defensive gates and Citadel bastions.\n2. The stone walls were coated with white gypsum plaster to prevent weathering.\n3. Baked bricks were completely absent at Dholavira, even in private structures.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: While stone was the primary building material for public fortifications, baked and mud bricks were still used for private residential buildings."
    ),
    (
        "With reference to the site of Surkotada in Gujarat, consider the following statements:\n1. It featured a unified fortification wall enclosing both the citadel and lower town.\n2. Gateway structures constructed with stone rubble and mud-brick have been excavated.\n3. The site had no drainage systems or sanitation planning.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: Surkotada had standard Harappan drainage planning, with gutters and sewers, consistent with other sites in Gujarat."
    ),
    (
        "Consider the following statements regarding the socio-political implications of Harappan planning:\n1. Standardized weights, measures, and brick ratios across 1,000 miles imply central coordination.\n2. The distinction between raised Citadels and Lower Towns suggests social stratification.\n3. Temples and palaces are absent, indicating that civic organization did not rely on standard monarchial structures.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All three statements are correct and represent current scholarly interpretations of Harappan socio-political structures."
    ),
    (
        "With reference to the site of Mohenjo-daro, consider the following statements:\n1. The layout is divided into a Citadel and a residential Lower Town.\n2. It has yielded the famous Great Bath, pillared Assembly Hall, and Collegiate Building.\n3. The site featured over 700 wells, proving highly developed groundwater management.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct and define the urban planning and monuments of Mohenjo-daro."
    ),
    (
        "Consider the following statements regarding the site of Harappa:\n1. It featured a Citadel fortified by a massive mud-brick wall faced with burnt bricks.\n2. Parallel rows of circular brick threshing platforms were placed outside the Citadel near granaries.\n3. Charles Masson was the first modern traveler to describe Harappa in 1826.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All three statements are correct, describing Harappa's walls, threshing platforms, and early discovery history."
    ),
    (
        "With reference to the site of Rakhigarhi, consider the following statements:\n1. It is the largest Harappan site by area, covering over nine mounds in Haryana.\n2. Standardized brick planning and grid iron streets have been excavated across its mounds.\n3. The site completely lacks Citadels or fortifications, showing it was a peaceful agricultural town.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: Rakhigarhi has fortified mounds and citadel platforms, conforming to standard metropolitan planning."
    ),
    (
        "Consider the following statements regarding the site of Kalibangan:\n1. It is situated along the Ghaggar River channel in Rajasthan.\n2. The site features a Citadel and Lower Town fortified separately.\n3. Clay fire altars built on brick platforms suggest ritual fire worship.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, describing Kalibangan's geography, fortification walls, and ritual fire pits."
    ),
    (
        "With reference to the site of Dholavira, consider the following statements:\n1. The city is uniquely divided into three fortified sections: Citadel, Middle Town, and Lower Town.\n2. The city was surrounded by massive stone reservoirs to harvest seasonal rainwater runoff.\n3. A unique 10-character gypsum signboard was found at its gateway.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All three statements are correct, illustrating the unique urban zoning, hydraulic engineering, and script discoveries at Dholavira."
    ),
    (
        "Consider the following statements regarding the site of Lothal:\n1. It was a southern port city featuring a baked-brick tidal dockyard.\n2. A mud-brick wall separated the Citadel from the Lower Town.\n3. Joint double burials containing skeletons of male-female pairs were found here.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, describing Lothal's port, fortification layout, and burial findings."
    ),
    (
        "With reference to the site of Banawali, consider the following statements:\n1. Streets follow a radial layout rather than a grid pattern.\n2. Excavations yielded a terracotta model of an agricultural plow.\n3. The drainage system was poor, using soak jars at street corners.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All three statements are correct, describing the layout, plowing model, and drainage at Banawali."
    ),
    (
        "Consider the following statements regarding the site of Surkotada:\n1. Both the citadel and lower town are enclosed by a common stone fortification wall.\n2. Skeletal remains of horses were reported in its upper layers.\n3. The site is located in the Kutch district of Gujarat.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, defining Surkotada's walls, horse bone findings, and geographic location."
    ),
    (
        "With reference to the site of Chanhudaro, consider the following statements:\n1. It is the only major Harappan city that completely lacks a Citadel.\n2. It was a craft suburb specializing in bead-making, seal-cutting, and shell-working.\n3. It yielded a brick with the paw print of a dog chasing a cat.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All three statements are correct, detailing Chanhudaro's unique layout, crafts, and animal print findings."
    ),
    (
        "Consider the following statements regarding the decline of the Harappan Civilisation:\n1. R.E.M. Wheeler proposed the Aryan invasion theory based on cemetery skeletons showing trauma.\n2. Modern studies link the decline to the drying up of the Ghaggar-Hakra river system due to tectonic diversions.\n3. Severe, repeated floods caused by shifts in the Indus river course devastated Mohenjo-daro multiple times.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, summarizing key theories of Harappan decline."
    ),
    (
        "With reference to the site of Balakot in Balochistan, consider the following statements:\n1. It was a major coastal site specializing in the shell-working industry.\n2. It was fortified with mud-brick walls and watchtowers.\n3. Marine shells were processed to make bangles and beads for export.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, defining Balakot's coastal geography, defenses, and shell industry."
    ),
    (
        "Consider the following statements regarding the site of Kuntasi:\n1. It functioned as a small port-cum-industrial center in Gujarat.\n2. Copper metallurgy and bead manufacturing were the main economic activities.\n3. The site had a small jetty for loading trade vessels.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, outlining Kuntasi's port facilities and industrial functions."
    ),
    (
        "With reference to the site of Shortughai, consider the following statements:\n1. It was a mature Harappan trading enclave established in northern Afghanistan.\n2. It is situated along the Amu Darya (Oxus) River.\n3. It directly controlled the trade of lapis lazuli from Badakhshan.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, describing Shortughai's trading function and location."
    ),
    (
        "Consider the following statements regarding the weight system of the Harappan Civilisation:\n1. Weights were standardized cubical blocks typically carved from chert.\n2. The binary system was used for lower weights (up to ratio 64) and decimal for higher weights.\n3. The weights were highly precise and standardized across all sites.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All three statements are correct, describing the material, math, and standardization of weights."
    ),
    (
        "With reference to Harappan pottery, consider the following statements:\n1. The pottery was predominantly wheel-made, painted in Red and Black style.\n2. Common decorative motifs included geometric patterns, pipal leaves, and animal drawings like fish scales.\n3. Painted pottery was highly standardized in both design and size across all sites.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, explaining the technology and standard designs of Harappan pottery."
    ),
    (
        "Consider the following statements regarding the seals of the Indus Civilisation:\n1. Seals were primarily square or rectangular blocks made of soft steatite soapstone.\n2. Most seals contained short inscriptions along with animal motifs like the unicorn, zebu bull, or elephant.\n3. Seals served as security tags stamped on clay sealings for commercial shipments.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, outlining the materials, designs, and functions of seals."
    ),
    (
        "With reference to the terracotta figurines of the Harappan Civilisation, consider the following statements:\n1. Terracotta figurines were hand-modeled and baked in kilns, representing animals, toys, and human forms.\n2. The 'Mother Goddess' figurines are characterized by elaborate fan-shaped headdresses.\n3. Figured toys like clay carts and whistles were common in residential sectors.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, describing terracotta human and toy figures."
    ),
    (
        "Consider the following statements regarding fire altars in the Harappan Civilisation:\n1. Brick-lined ritual pits identified as fire altars have been found at Kalibangan and Lothal.\n2. These altars often contain ash, charcoal, and clay cakes, suggesting fire worship.\n3. Altars are completely absent at Mohenjo-daro and Harappa.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, outlining the fire altar findings and distributions."
    ),
    (
        "With reference to Harappan linear measurements, consider the following statements:\n1. Bronze scales and ivory rulers divided into precise units have been excavated.\n2. Linear standards were uniform across Punjab, Sindh, and Gujarat.\n3. A standard Harappan foot was equivalent to approximately 37.6 cm.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, describing linear measurement devices and standards."
    ),
    (
        "Consider the following statements regarding Harappan construction techniques:\n1. Bricks were laid in an interlocking pattern, often called the English bond.\n2. Gypsum-lime mortar was used to seal brick joins in drains and baths.\n3. Pillars of stone or wood were used to support roofs in large assembly halls.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, summarizing building patterns and mortars."
    ),
    (
        "With reference to the site of Lothal's dockyard, consider the following statements:\n1. The dockyard basin measured approximately 217 meters in length and 37 meters in width.\n2. Sluice gates were built to trap water in the basin during low tides to float ships.\n3. It was constructed using high-quality baked bricks bound with gypsum.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, describing the dimensions, gates, and bricks of the Lothal dockyard."
    ),
    (
        "Consider the following statements regarding the site of Mohenjo-daro's Great Bath:\n1. The bath is a rectangular pool measuring 12m x 7m with a depth of 2.4m.\n2. North and south flights of steps led down into the water.\n3. Surrounding corridors led to small rooms, one of which housed a large brick well.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, outlining the physical and architectural layout of the Great Bath."
    ),
    (
        "With reference to Harappan residential wells, consider the following statements:\n1. Public and private wells were lined with wedge-shaped radial bricks to resist soil pressure.\n2. Wells were placed near the outer door of houses so that travelers could use them.\n3. Over 700 wells have been excavated at Mohenjo-daro.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, describing the engineering, location, and numbers of wells."
    ),
    (
        "Consider the following statements regarding Harappan sanitary engineering:\n1. Street drains were paved with flat bricks and run below the road level.\n2. Houses had pottery drain conduits embedded inside the brick walls to carry waste from roofs.\n3. Drains were equipped with silt traps and soak jars at junctions.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, outlining sewer paving, conduits, and silt traps."
    ),
    (
        "With reference to the site of Kalibangan's wooden drainage, consider the following statements:\n1. Sal or teak logs were hollowed out to form drainage conduits.\n2. These wooden drains were utilized primarily in the Citadel area.\n3. Kalibangan completely lacked the standard brick-lined public street sewers.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, detailing the materials, locations, and unique status of Kalibangan's wooden drains."
    ),
    (
        "Consider the following statements regarding Dholavira's check dams:\n1. Stone check dams were built across the seasonal Manhar and Mansar streams.\n2. Dammed water was diverted into a series of 16 interconnected reservoirs.\n3. The reservoirs were cut into solid limestone and lined with stone blocks.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, detailing Dholavira's damming, reservoir count, and stone masonry."
    ),
    (
        "With reference to the site of Surkotada's citadel gateway, consider the following statements:\n1. The gateway featured a ramp built of rubble stone leading to the main citadel entrance.\n2. Guard rooms were built flanking the gateway to monitor entry.\n3. It displays a sophisticated stone arch construction representing the earliest true arch in India.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: Harappans did not build true arches; they utilized corbelled lintels and flat stone gateways."
    ),
    (
        "Consider the following statements regarding the site of Banawali's fortifications:\n1. It featured a mud-brick wall enclosing both the Citadel and Lower Town.\n2. A deep moat filled with water surrounded the outer walls of the town.\n3. The Citadel was separated from the Lower Town by a fortified wall.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, outlining Banawali's wall, moat, and internal division."
    ),
    (
        "With reference to the site of Rakhigarhi's town plan, consider the following statements:\n1. The settlement is divided into a Citadel and Lower Town spread over nine mounds.\n2. Standardized brick platforms raisedCitadels to protect them from seasonal floods.\n3. Covered brick drains with manholes are present across all mounds.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, detailing Rakhigarhi's mounds, citadels, and drains."
    )
]

# Hindi translation of the 50 practice questions
practice_data_hin = [
    (
        "हड़प्पा नगरों में सड़कों के नियोजन के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. धूल और कचरे को प्राकृतिक रूप से साफ करने के लिए मुख्य सड़कें उत्तर-दक्षिण और पूर्व-पश्चिम दिशाओं में संरेखित थीं।\n2. सड़कें एक-दूसरे को समकोण पर काटती थीं, जिससे सभी प्रमुख शहरों में ग्रिड पैटर्न (grid iron system) बनता था।\n3. बनावली में सड़कों का लेआउट ग्रिड प्रणाली से भिन्न था, यहाँ सड़कें किले के टीले से बाहर की ओर अरीय (radial) रूप में जाती थीं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        3,
        "तीनों कथन सही हैं, जो दिशा संरेखण, ग्रिड प्रणाली और बनावली की अरीय सड़कों का सटीक विवरण देते हैं।"
    ),
    (
        "हड़प्पा शहरों के दोहरे विभाजन के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. अधिकांश बस्तियां कच्चे ईंट के चबूतरे पर बने पश्चिमी ऊंचे किले (Citadel) और एक पूर्वी निचले नगर (Lower Town) में विभाजित थीं।\n2. किले में प्रशासनिक और धार्मिक स्मारक होते थे, जबकि निचला नगर मुख्य रूप से आवासीय था।\n3. धोलावीरा विशिष्ट रूप से तीन भागों: किला, मध्य नगर और निचले नगर में विभाजित है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        3,
        "तीनों कथन सही हैं, जो मानक विभाजन और धोलावीरा के तीन भागों के विभाजन को दर्शाते हैं।"
    ),
    (
        "किले (Citadel) के बिना बनी सिंधु बस्तियों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. सिंध में स्थित चन्हुदड़ो एक बड़ा शिल्प उपनगर था जिसमें किले का पूर्ण अभाव था।\n2. किले के अभाव के कारण, चन्हुदड़ो में मानक हड़प्पा बाटों या जल निकासी प्रणाली का उपयोग नहीं होता था।\n3. लोथल में किले और निचले नगर के बीच कोई भौतिक दीवार नहीं थी।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1", "केवल 1 और 2", "केवल 1 और 3", "1, 2 और 3"],
        0,
        "कथन 1 सही है। कथन 2 गलत है: चन्हुदड़ो में बिना किले के भी मानक हड़प्पा बाटों और जल निकासी प्रणालियों का पूरा उपयोग होता था। कथन 3 गलत है: लोथल में किले और निचले नगर के बीच एक कच्ची ईंट की दीवार बनी थी।"
    ),
    (
        "सिंधु घाटी की जल निकासी प्रणालियों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मुख्य सड़कें की नालियां पकी ईंटों से बनी थीं और हवा आने-जाने के लिए पूरी तरह खुली रहती थीं।\n2. सड़कों की नालियों के साथ नियमित अंतराल पर मैनहोल (inspection chambers) बनाए गए थे।\n3. गंदे पानी का सुचारू प्रवाह सुनिश्चित करने के लिए नालियों को एक हल्के ढलान के साथ बनाया गया था।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        1,
        "कथन 2 और 3 सही हैं। कथन 1 गलत है: स्वच्छता और सार्वजनिक स्वास्थ्य सुनिश्चित करने के लिए नालियों को ईंटों या पत्थरों की शिलाओं से ढका जाता था।"
    ),
    (
        "हड़प्पा घरों के भीतर जल निकासी के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. स्नानघरों और रसोइयों में फर्श ढलानदार होते थे जो एक कोने की नाली की ओर जाते थे।\n2. घरों का पानी सड़कों पर बने शोषक गड्ढे (soak pit) में गिरता था, जहाँ ठोस कचरा नीचे बैठ जाता था और तरल पानी मुख्य नाली में जाता था।\n3. सभी प्रमुख स्थलों पर घरों की नालियाँ चमड़े में लपेटे गए लकड़ी के पाइपों से बनाई जाती थीं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: घरों की नालियां पकी ईंटों और मिट्टी के पाइपों से बनती थीं; केवल कालीबंगन में लकड़ी की नाली मिली है जो एक अपवाद है।"
    ),
    (
        "हड़प्पा शहरों में पानी की आपूर्ति के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मोहनजोदड़ो के लगभग हर घर में पकी ईंटों से बना एक निजी कुआँ होता था।\n2. अकेले मोहनजोदड़ो से 700 से अधिक कुएँ खोजे गए हैं।\n3. धोलावीरा पूरी तरह से निजी घरों के कुओं पर निर्भर था क्योंकि कच्छ में सतह पर पानी नहीं था।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: धोलावीरा मुख्य रूप से विशाल जलाशयों पर निर्भर था क्योंकि कच्छ का भूजल खारा था और कुएं दुर्लभ थे।"
    ),
    (
        "हड़प्पा वासियों द्वारा प्रयुक्त ईंटों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. पकी और कच्ची दोनों ईंटों के आकार का अनुपात हमेशा 4:2:1 (लंबाई:चौड़ाई:मोटाई) होता था।\n2. घरों के निर्माण के लिए प्रयुक्त ईंटों का आकार सामान्यतः 28 सेमी x 14 सेमी x 7 सेमी होता था।\n3. कच्ची ईंटों का उपयोग केवल किले की सुरक्षा दीवारों के लिए होता था, जबकि निजी घर केवल पकी ईंटों से बनते थे।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: चबूतरे और निजी घरों के निर्माण में कच्ची ईंटों का व्यापक उपयोग होता था, जबकि पकी ईंटें मुख्य रूप से नालियों और कुओं में लगाई जाती थीं।"
    ),
    (
        "हड़प्पावासियों की बाट-माप प्रणाली के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. बाट मानकीकृत घनाकार पत्थर के होते थे जो कठोर चर्ट पत्थर से बनाए जाते थे।\n2. कम वजन मापने के लिए द्वि-आधारी प्रणाली (1, 2, 4, 8, 16, 32, 64) का उपयोग होता था।\n3. उच्च मानों के लिए दशमलव प्रणाली का उपयोग किया जाता था, जो एक उन्नत गणितीय ज्ञान दर्शाता है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        3,
        "तीनों कथन सही हैं और हड़प्पा की मानकीकृत मापन व्यवस्था का वर्णन करते हैं।"
    ),
    (
        "मोहनजोदड़ो के विशाल स्नानागार (Great Bath) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह पकी ईंटों और जिप्सम गारे से बना एक आयताकार कुंड है।\n2. कुंड को जल-रोधी बनाने के लिए ईंटों पर प्राकृतिक डामर (बिटुमेन) की एक परत लगाई गई थी।\n3. यह निचले नगर में स्थित था और इसका उपयोग नागरिक रोजमर्रा के स्नान और कपड़े धोने के लिए करते थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: विशाल स्नानागार किले पर स्थित था और इसका उपयोग सार्वजनिक अनुष्ठानिक स्नान के लिए होता था।"
    ),
    (
        "हड़प्पा नगर नियोजन में अन्नागारों (Granaries) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मोहनजोदड़ो के विशाल अन्नागार में ऊंचे ईंट के चबूतरे थे जिन पर लकड़ी की विशाल संरचना बनी थी।\n2. हड़प्पा में छोटी अन्नागारों की दो कतारें किले के बाहर नदी तट के करीब स्थित थीं।\n3. अन्नागारों में नमी से बचाने के लिए फर्श के नीचे हवा आने-जाने के मार्ग (ventilation ducts) बने थे।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        3,
        "तीनों कथन सही हैं, जो अन्नागारों के स्थान, संरचना और जल निकासी/हवा निकासी के प्रतिरूप को दर्शाते हैं।"
    ),
    (
        "धोलावीरा की जल प्रबंधन प्रणाली के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यहाँ मौसमी नदियों पर बांध बनाकर पानी को मोड़ने और जलाशयों में संचित करने की व्यवस्था थी।\n2. किले के चारों ओर बने ये जलाशय सीधे स्थानीय चूना पत्थर की चट्टानों को काटकर बनाए गए थे।\n3. धोलावीरा 50 मील दूर स्थित नदियों से पानी लाने के लिए मिट्टी की पाइपलाइनों पर निर्भर था।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: वर्षा जल को स्थानीय बांधों और जलाशयों द्वारा सहेजा जाता था, न कि दूर की नदियों से पाइपलाइन द्वारा।"
    ),
    (
        "हड़प्पा शहरों की किलेबंदी (fortifications) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. सुरक्षा दीवारें मुख्य रूप से कच्ची ईंटों से बनती थीं और बाहरी क्षेत्रों में पत्थर या पकी ईंटों की परत चढ़ाई जाती थी।\n2. सुरक्षा दीवारों में बुर्ज, किलेबंद प्रवेश द्वार और निगरानी चौकियां शामिल होती थीं।\n3. चन्हुदड़ो और बालाकोट जैसे स्थल 10 मीटर से अधिक मोटी पत्थर की सुरक्षा दीवारों से घिरे थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 2", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: चन्हुदड़ो में कोई सुरक्षा दीवार नहीं थी, और बालाकोट में कच्ची ईंटों की दीवारें थीं, न कि 10 मीटर की पत्थर की दीवारें।"
    ),
    (
        "हड़प्पावासियों के आवासीय घरों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. व्यावसायिक प्रदर्शन को बढ़ावा देने के लिए घरों के दरवाजे मुख्य सड़कों की ओर खुलते थे।\n2. गोपनीयता बनाए रखने के लिए घर के प्रवेश द्वार मुख्य सड़क के बजाय पतली गलियों की ओर खुलते थे।\n3. अधिकांश घरों में एक केंद्रीय आंगन होता था जिसके चारों ओर कमरे, स्नानघर और दूसरी मंजिल पर जाने के लिए सीढ़ियाँ होती थीं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 2 और 3", "केवल 1 और 2", "केवल 1 और 3", "1, 2 और 3"],
        0,
        "कथन 2 और 3 सही हैं। कथन 1 गलत है: दरवाजे और खिड़कियां सड़कों की ओर नहीं खुलती थीं ताकि शोर, धूल और बाहरी झांकने से बचा जा सके।"
    ),
    (
        "कालीबंगन स्थल के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इस शहर में किले और निचले नगर दोनों के लिए अलग-अलग सुरक्षा दीवारें बनी थीं।\n2. यहाँ पकी ईंटों की सार्वजनिक नाली प्रणाली का अभाव था, और नालियों के लिए खोखली लकड़ी का उपयोग होता था।\n3. पूर्व-हड़प्पा स्तरों में जुते हुए खेत के साक्ष्य मिले हैं, जो नगर के ग्रिड नियोजन के समरूप हैं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं और कालीबंगन के नियोजन, नालियों और कृषि साक्ष्यों का विवरण देते हैं।"
    ),
    (
        "बनावली स्थल के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. सड़कों का नियोजन ग्रिड पैटर्न पर न होकर अनियमित अरीय (radial) था।\n2. किले और निचले नगर के बीच एक सुरक्षित दीवार थी, हालांकि दोनों एक ही टीले पर बने थे।\n3. जल निकासी व्यवस्था कमजोर थी और सड़कों पर गंदा पानी जमा करने के लिए मटके रखे जाते थे।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं और बनावली के स्थानीय नियोजन और जल निकासी का सटीक विवरण देते हैं।"
    ),
    (
        "बाट-माप के मानकीकरण के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. चर्ट पत्थर के बाट मुख्य रूप से गुजरात में और सेलखड़ी के बाट पंजाब में प्रयुक्त होते थे।\n2. अनुपात 16 के आधार वजन का मान लगभग 13.63 ग्राम था।\n3. रैखिक माप प्रणालियों में कांसे के स्केल और हाथीदांत के पैमाने मिले हैं जिन पर सटीक विभाजन के निशान हैं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 2 और 3", "केवल 1 और 2", "केवल 1 और 3", "1, 2 और 3"],
        0,
        "कथन 2 और 3 सही हैं। कथन 1 गलत है: पूरे हड़प्पा क्षेत्र में समान चर्ट के बाटों का उपयोग होता था, जो व्यापारिक मानकीकरण को दर्शाता है।"
    ),
    (
        "मोहनजोदड़ो के सभा भवन (Assembly Hall) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह एक विशाल चौकोर भवन है जिसमें बीस ईंटों के स्तंभ कतारों में बने हैं।\n2. यह किले पर स्थित है और माना जाता है कि इसका उपयोग नगर परिषद की बैठकों के लिए होता था।\n3. इसे हड़प्पा के देवताओं और राजाओं की ठोस मूर्तियों से सजाया गया था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 2", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: हड़प्पा के किसी भी सार्वजनिक भवन से राजाओं या देवताओं की चित्रकारी या मूर्तियां दीवारों पर नहीं मिली हैं।"
    ),
    (
        "हड़प्पा स्वच्छता इंजीनियरिंग के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. स्नानघरों का गंदा पानी सीधे गलियों में बहने दिया जाता था ताकि वह स्वतः साफ हो सके।\n2. घरों की दीवारों के भीतर से मिट्टी के पाइप (terracotta pipes) नीचे आते थे जो ऊपरी मंजिलों का कचरा गली की नाली तक लाते थे।\n3. गली के नाले सड़कों के स्तर से नीचे बनाए जाते थे और उन्हें समतल ईंटों से पक्का किया जाता था।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 2 और 3", "केवल 1 और 2", "केवल 1 और 3", "1, 2 और 3"],
        0,
        "कथन 2 और 3 सही हैं। कथन 1 गलत है: घरों का गंदा पानी सड़क पर नहीं बहता था, बल्कि नालियों या शोषक गड्ढों में जाता था।"
    ),
    (
        "धोलावीरा की पत्थर की वास्तुकला के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. किले के प्रवेश द्वारों और बुर्जों के लिए स्थानीय तराशे गए चूना पत्थरों का उपयोग किया गया था।\n2. मौसम के प्रभाव से बचाने के लिए पत्थर की दीवारों पर सफेद जिप्सम प्लास्टर का लेप लगाया जाता था।\n3. धोलावीरा में पकी हुई ईंटें पूरी तरह से अनुपस्थित थीं, यहाँ तक कि निजी घरों में भी।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: यद्यपि पत्थर मुख्य सामग्री थी, निजी रिहायशी घरों के लिए पकी और कच्ची ईंटों का उपयोग किया जाता था।"
    ),
    (
        "गुजरात के सुरकोटदा स्थल के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इसमें एक किला और निचला नगर था जो एक ही सामान्य सुरक्षा दीवार से घिरे थे।\n2. यहाँ से पत्थरों और कच्ची ईंटों से बने सुरक्षित प्रवेश द्वार मिले हैं।\n3. इस स्थल पर स्वच्छता या नालियों की कोई व्यवस्था नहीं थी।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: सुरकोटदा में भी अन्य स्थलों की तरह जल निकासी और स्वच्छता के समान मानक थे।"
    ),
    (
        "हड़प्पा नियोजन के सामाजिक-राजनीतिक प्रभावों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. 1,000 मील के क्षेत्र में बाट-माप और ईंटों का समान अनुपात एक मजबूत केंद्रीय समन्वय को दर्शाता है।\n2. ऊंचे किलों और निचले नगरों का विभाजन समाज में स्तरीकरण (class structure) का संकेत देता है।\n3. मंदिरों और महलों की अनुपस्थिति दर्शाती है कि यहाँ का सामाजिक संगठन सामान्य राजशाही जैसा नहीं था।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं और हड़प्पा समाज के राजनीतिक और सामाजिक सिद्धांतों को स्पष्ट करते हैं।"
    ),
    (
        "मोहनजोदड़ो स्थल के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इसका नगर नियोजन एक किला और निचले आवासीय नगर में विभाजित है।\n2. यहाँ से विशाल स्नानागार, सभा भवन और कॉलेज भवन मिले हैं।\n3. इस शहर में 700 से अधिक कुएं मिले हैं, जो भूजल प्रबंधन की उत्कृष्ट व्यवस्था दर्शाते हैं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं और मोहनजोदड़ो की विशेषताओं को दर्शाते हैं।"
    ),
    (
        "हड़प्पा स्थल के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इसका किला कच्ची ईंटों की एक विशाल दीवार से घिरा था जिस पर पकी ईंटों की परत चढ़ी थी।\n2. किले के बाहर अन्नागारों के पास अनाज गाहने के गोलाकार ईंटों के चबूतरे मिले हैं।\n3. चार्ल्स मैसन 1826 में हड़प्पा की यात्रा करने वाले पहले आधुनिक यात्री थे।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो हड़प्पा की किलेबंदी, चबूतरों और खोज के इतिहास को दर्शाते हैं।"
    ),
    (
        "राखीगढ़ी स्थल के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह क्षेत्रफल की दृष्टि से सबसे बड़ा हड़प्पा स्थल है, जो हरियाणा में नौ टीलों में फैला है।\n2. इसके विभिन्न टीलों में ग्रिड सड़कों और मानक ईंटों के नियोजन के साक्ष्य मिले हैं।\n3. इस स्थल पर कोई किला या सुरक्षा दीवार नहीं मिली है, जो दर्शाता है कि यह एक शांत कृषि नगर था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: राखीगढ़ी में किलेबंदी वाले टीले और चबूतरे मिले हैं जो इसके महानगर होने की पुष्टि करते हैं।"
    ),
    (
        "कालीबंगन स्थल के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह राजस्थान में घग्गर नदी के शुष्क मार्ग पर स्थित है।\n2. यहाँ किला और निचला नगर दोनों अलग-अलग दीवारों से सुरक्षित किए गए थे।\n3. यहाँ ईंटों के चबूतरे पर बने अग्निकुंड अग्नि पूजा की ओर संकेत करते हैं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो कालीबंगन के भूगोल, सुरक्षात्मक दीवारों और अग्निकुंडों का सटीक विवरण देते हैं।"
    ),
    (
        "धोलावीरा स्थल के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह शहर विशिष्ट रूप से तीन किलेबंद भागों: किला, मध्य नगर और निचले नगर में विभाजित है।\n2. शहर के चारों ओर वर्षा जल को संचित करने के लिए विशाल जलाशय बनाए गए थे।\n3. यहाँ के मुख्य प्रवेश द्वार से जिप्सम के दस अक्षरों वाला एक अनोखा साइनबोर्ड मिला है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं और धोलावीरा के विभाजन, जलाशयों और साइनबोर्ड की खोज का विवरण देते हैं।"
    ),
    (
        "लोथल स्थल के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह एक दक्षिणी बंदरगाह शहर था जिसमें पकी ईंटों से बना गोदी बाड़ा (dockyard) मिला है।\n2. यहाँ किला और निचला नगर एक मिट्टी की ईंटों की दीवार से अलग किए गए थे।\n3. यहाँ से पुरुष-महिला के युगल शवाधान (double burials) के साक्ष्य मिले हैं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो लोथल के बंदरगाह, आंतरिक दीवारों और युगल कब्रों को दर्शाते हैं।"
    ),
    (
        "बनावली के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यहाँ की सड़कें ग्रिड के बजाय अरीय (radial) प्रतिरूप का पालन करती थीं।\n2. यहाँ से मिट्टी का बना खिलौना हल मिला है।\n3. जल निकासी व्यवस्था कमजोर थी और सड़कों के कोनों पर शोषक मटके रखे जाते थे।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो बनावली के अनियमित नियोजन, हल और जल निकासी का विवरण देते हैं।"
    ),
    (
        "सुरकोटदा स्थल के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इसमें किला और निचला नगर दोनों एक साझी पत्थर की सुरक्षा दीवार से घिरे हैं।\n2. यहाँ ऊपरी स्तरों से घोड़े की हड्डियों के साक्ष्य मिलने की रिपोर्ट की गई है।\n3. यह गुजरात के कच्छ जिले में स्थित है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं और सुरकोटदा की दीवार, घोड़े के अवशेषों और कच्छ में इसकी स्थिति को दर्शाते हैं।"
    ),
    (
        "चन्हुदड़ो स्थल के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह एकमात्र प्रमुख हड़प्पा शहर है जिसमें कोई सुरक्षात्मक किला (citadel) नहीं था।\n2. यह मनके बनाने, मुहर तराशने और शंख उद्योग के लिए प्रसिद्ध था।\n3. यहाँ से एक ईंट पर बिल्ली का पीछा करते हुए कुत्ते के पंजों के निशान मिले हैं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं और चन्हुदड़ो के नियोजन, उद्योगों और पंजों के साक्ष्य को दर्शाते हैं।"
    ),
    (
        "हड़प्पा सभ्यता के पतन के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. आर.ई.एम. व्हीलर ने कंकालों के आघात के आधार पर आर्य आक्रमण का सिद्धांत दिया था।\n2. आधुनिक शोध पतन को भू-विवर्तनिक हलचलों के कारण घग्गर-हाकड़ा नदी के सूखने से जोड़ते हैं।\n3. सिंधु नदी के मार्ग परिवर्तन से आने वाली भीषण बाढ़ों ने मोहनजोदड़ो को कई बार तबाह किया।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं और पतन के प्रमुख पुरातात्विक सिद्धांतों को स्पष्ट करते हैं।"
    ),
    (
        "बलूचिस्तान के बालाकोट स्थल के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह शंख उद्योग (shell-working) में विशेषज्ञता रखने वाला एक तटीय बंदरगाह था।\n2. यह कच्ची ईंटों की सुरक्षा दीवारों और बुर्जों से घिरा हुआ था।\n3. निर्यात के लिए शंख की चूड़ियाँ और आभूषण यहाँ बनाए जाते थे।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं और बालाकोट की तटीय स्थिति, सुरक्षा और उद्योगों को दर्शाते हैं।"
    ),
    (
        "कुंतासी स्थल के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह गुजरात में स्थित एक छोटा बंदरगाह और औद्योगिक केंद्र था।\n2. तांबा गलाने और मनके बनाने का काम यहाँ की मुख्य आर्थिक गतिविधियाँ थीं।\n3. व्यापारिक जहाजों के लंगर डालने के लिए यहाँ एक छोटी जेट्टी (jetty) मिली है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो कुंतासी के बंदरगाह और शिल्प उद्योगों का विवरण देते हैं।"
    ),
    (
        "शॉर्टुघई के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. यह उत्तरी अफगानिस्तान में स्थित एक परिपक्व हड़प्पा व्यापारिक चौकी थी।\n2. यह अमू दरिया (ऑक्सस) नदी के किनारे स्थित है।\n3. यह सीधे बदख्शां के लाजवर्त (lapis lazuli) व्यापार को नियंत्रित करती थी।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो शॉर्टुघई की भौगोलिक स्थिति और व्यापारिक भूमिका को स्पष्ट करते हैं।"
    ),
    (
        "हड़प्पा सभ्यता की वजन प्रणाली के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. बाट मानकीकृत घनाकार पत्थर के होते थे जो चर्ट से बनाए जाते थे।\n2. कम वजन के लिए द्वि-आधारी प्रणाली (64 तक) और उच्च वजन के लिए दशमलव प्रणाली का उपयोग होता था।\n3. बाटों के मान अत्यधिक सटीक थे और सभी स्थलों पर एक समान थे।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो बाटों की सामग्री, गणितीय अनुपात और मानकीकरण को स्पष्ट करते हैं।"
    ),
    (
        "हड़प्पा के मिट्टी के बर्तनों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. बर्तन मुख्य रूप से चाक पर बने लाल और काले (Red and Black) रंग के होते थे।\n2. प्रमुख डिजाइनों में ज्यामितीय प्रतिरूप, पीपल के पत्ते और मछली के शल्क शामिल थे।\n3. सभी स्थलों पर बर्तनों के आकार और उनकी चित्रकारी अत्यधिक मानकीकृत थीं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो मिट्टी के बर्तनों की तकनीक और डिजाइनों का विवरण देते हैं।"
    ),
    (
        "सिंधु सभ्यता की मुहरों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मुहरें मुख्य रूप से चौकोर या आयताकार होती थीं और मुलायम सेलखड़ी से बनती थीं।\n2. अधिकांश मुहरों पर एक सींग वाले पशु, सांड या हाथी के साथ एक छोटा लेख होता था।\n3. व्यापारिक सामानों की सुरक्षा के लिए गीली मिट्टी पर मुहरों की छाप लगाई जाती थी।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो मुहरों की सामग्री, चित्र और कार्यों को दर्शाते हैं।"
    ),
    (
        "हड़प्पा की मिट्टी की मूर्तियों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मिट्टी की मूर्तियाँ हाथ से बनाई जाती थीं और भट्टी में पकाई जाती थीं, जिनमें पशु, खिलौने और मानव रूप शामिल थे।\n2. मातृदेवी की मूर्तियों की मुख्य विशेषता उनका पंखे जैसा बड़ा मुकुट (headdress) है।\n3. रिहायशी इलाकों में मिट्टी के खिलौने जैसे गाड़ियाँ और सीटियाँ आम तौर पर मिलती हैं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो मिट्टी की मूर्तियों, मातृदेवी और खिलौनों का विवरण देते हैं।"
    ),
    (
        "हड़प्पा सभ्यता में अग्निकुंडों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. ईंटों से बने अग्निकुंड कालीबंगन और लोथल स्थलों से मिले हैं।\n2. इन अग्निकुंडों में राख, कोयला और मिट्टी के पिंड मिले हैं, जो अग्नि पूजा का संकेत देते हैं।\n3. मोहनजोदड़ो और हड़प्पा से कोई भी अग्निकुंड नहीं मिले हैं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो अग्निकुंडों की उपस्थिति, सामग्री और उनके वितरण को स्पष्ट करते हैं।"
    ),
    (
        "हड़प्पा की रैखिक माप प्रणालियों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यहाँ से उत्खनन में कांसे और हाथीदांत के पैमाने (rulers) मिले हैं जिन पर सटीक विभाजन हैं।\n2. पंजाब, सिंध और गुजरात सभी क्षेत्रों में रैखिक माप समान थे।\n3. हड़प्पा की एक मानक फुट इकाई का मान लगभग 37.6 सेमी था।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो मापन उपकरणों और उनके मानों का विवरण देते हैं।"
    ),
    (
        "हड़प्पा निर्माण तकनीकों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. ईंटों को एक-दूसरे से जोड़कर दीवार मजबूत करने के लिए इंग्लिश बांड (interlocking pattern) का उपयोग होता था।\n2. नालियों और स्नानागारों में ईंटें जोड़ने के लिए चूने और जिप्सम के गारे का उपयोग होता था।\n3. बड़े सभा भवनों की छतों को सहारा देने के लिए पत्थर या लकड़ी के स्तंभों का उपयोग किया जाता था।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        3,
        "तीनों कथन सही हैं, जो हड़प्पा की निर्माण तकनीक, गारे और स्तंभों का सटीक विवरण देते हैं।"
    ),
    (
        "लोथल के गोदी बाड़े (dockyard) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. गोदी बाड़े के कुंड का आकार लगभग 217 मीटर लंबा और 37 मीटर चौड़ा है।\n2. भाटे के दौरान पानी रोकने और जहाजों को तैरते रखने के लिए स्लूस गेट बनाए गए थे।\n3. इसका निर्माण जिप्सम से जोड़ी गई पकी ईंटों से किया गया था।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो गोदी बाड़े के आकार, द्वारों और ईंटों का विवरण देते हैं।"
    ),
    (
        "मोहनजोदड़ो के विशाल स्नानागार (Great Bath) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह 12 मीटर लंबा, 7 मीटर चौड़ा और 2.4 मीटर गहरा एक आयताकार कुंड है।\n2. इसमें उतरने के लिए उत्तर और दक्षिण दिशा से सीढ़ियाँ बनी हैं।\n3. कुंड के चारों ओर गलियारे थे जो कमरों से जुड़े थे, जिनमें से एक में विशाल कुआँ था।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो विशाल स्नानागार की माप, सीढ़ियों और कमरों का विवरण देते हैं।"
    ),
    (
        "घरों के कुओं के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. मिट्टी के दबाव को सहने के लिए कुओं में त्रिकोणीय/फानाकार (wedge-shaped) ईंटें लगाई जाती थीं।\n2. कुएँ अक्सर घर के बाहरी दरवाजे के पास होते थे ताकि राहगीर भी उनका उपयोग कर सकें।\n3. अकेले मोहनजोदड़ो से 700 से अधिक कुएँ मिले हैं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो कुओं की बनावट, स्थान और संख्या को दर्शाते हैं।"
    ),
    (
        "हड़प्पा स्वच्छता इंजीनियरिंग के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. सड़कों की नालियाँ ढकी हुई थीं और वे सड़क के स्तर से नीचे बनाई जाती थीं।\n2. घरों की दीवारों के भीतर मिट्टी के पाइप लगे थे जो छतों का गंदा पानी नीचे लाते थे।\n3. नालियों के मिलन स्थलों पर कचरा इकट्ठा करने के लिए सिल्ट ट्रैप (शोषक गड्ढे) लगे थे।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो नालियों, मिट्टी के पाइपों और सिल्ट ट्रैप का विवरण देते हैं।"
    ),
    (
        "कालीबंगन में लकड़ी की नाली प्रणाली के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. साल या सागौन की लकड़ी के तनों को खोखला करके नालियां बनाई गई थीं।\n2. इन लकड़ी की नालियों का उपयोग मुख्य रूप से किले (citadel) क्षेत्र में किया गया था।\n3. कालीबंगन में पकी ईंटों की बनी सड़कों की नालियों का पूर्ण अभाव था।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो कालीबंगन की लकड़ी की नालियों की सामग्री, स्थिति और इसके अनोखे स्वरूप को स्पष्ट करते हैं।"
    ),
    (
        "धोलावीरा के बांधों और जलाशयों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. मौसमी मनहर और मनसर नदियों पर पत्थर के बांध बनाए गए थे।\n2. बांध के पानी को मोड़कर 16 आपस में जुड़े जलाशयों में संचित किया जाता था।\n3. ये जलाशय ठोस चूना पत्थर को काटकर बनाए गए थे और उनकी दीवारें पत्थरों से पक्की की गई थीं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो धोलावीरा के बांधों, जलाशयों की संख्या और उनकी बनावट का विवरण देते हैं।"
    ),
    (
        "सुरकोटदा के प्रवेश द्वार के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. प्रवेश द्वार में किले तक जाने के लिए पत्थर के मलबे से बना एक रैंप था।\n2. प्रवेश द्वार के दोनों ओर सुरक्षा कक्ष (guard rooms) बने थे।\n3. यहाँ से पत्थर की मेहराब (arch) मिली है जो भारत में मेहराब का सबसे प्राचीन साक्ष्य है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: हड़प्पावासी मेसोपोटामिया की तरह सच्ची मेहराब (true arch) नहीं बनाते थे; वे सपाट या शहतीर (corbelled lintels) वाले प्रवेश द्वार बनाते थे।"
    ),
    (
        "बनावली की किलेबंदी के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इसमें एक मिट्टी की ईंटों की सुरक्षा दीवार थी जो किले और निचले नगर दोनों को घेरती थी।\n2. नगर की सुरक्षा दीवार के चारों ओर पानी से भरी एक गहरी खाई (moat) बनी थी।\n3. किला और निचला नगर एक सुरक्षा दीवार से आपस में विभाजित थे।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो बनावली की सुरक्षा दीवार, खाई और टीलों के विभाजन को स्पष्ट करते हैं।"
    ),
    (
        "राखीगढ़ी के नगर नियोजन के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. यह शहर नौ टीलों में फैला है और किला तथा निचले नगर में विभाजित है।\n2. अन्नागारों और सार्वजनिक स्थलों को मौसमी बाढ़ से बचाने के लिए ईंटों के ऊंचे चबूतरे बनाए गए थे।\n3. नालियाँ सड़कों के नीचे बनी थीं और उन पर मैनहोल ढक्कन लगे थे।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो राखीगढ़ी के टीलों, चबूतरों और जल निकासी को स्पष्ट करते हैं।"
    )
]

# Mock Test Questions (10 Qs)
mock_data_eng = [
    (
        "Consider the following statements regarding the metrology of the Harappan Civilisation:\n1. Standardized weights were cubical blocks typically carved from chert.\n2. The binary scale of weights was used for lower weights (up to ratio 64), while decimal scales were used for higher values.\n3. The base unit weight ratio 16 was equivalent to 13.63 grams.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All three statements are correct, describing the standard materials, scales, and base weights of the Harappan metrology system."
    ),
    (
        "With reference to the division of Harappan cities, consider the following statements:\n1. Citadels were typically located in the west and built on mud-brick platforms, housing public monuments.\n2. Lower Towns were positioned to the east, acting as larger residential areas for merchants and artisans.\n3. Dholavira in Kutch is divided into three fortified sections: Citadel, Middle Town, and Lower Town.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All three statements are correct, describing the Citadel-Lower Town dichotomy and Dholavira's three-tier layout."
    ),
    (
        "Consider the following statements regarding Harappan sanitation and sewage system:\n1. Main drains running along streets were paved with flat bricks and covered with brick slabs or stone blocks.\n2. Earthenware soak jars were placed at street corners and junctions to collect solid waste before water entered public drains.\n3. Drains were equipped with inspection chambers or manholes for cleaning.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All three statements are correct, outlining the paving, soak jars, and cleanup manholes of the municipal sewage network."
    ),
    (
        "With reference to the site of Kalibangan, consider the following statements:\n1. The Citadel and the Lower Town were fortified separately.\n2. It lacked standard public baked-brick sewers, using hollowed-out wooden logs for drainage conduits.\n3. Pre-Harappan layers yielded furrow marks showing a grid of crop plowing.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All three statements are correct, describing the fortifications, wooden drains, and early ploughed field of Kalibangan."
    ),
    (
        "Consider the following statements regarding the site of Banawali:\n1. Streets follow a radial layout radiating from the citadel mound instead of a grid pattern.\n2. Earthenware jars were placed at street corners to collect household wastewater.\n3. Excavations yielded a well-preserved terracotta model of an agricultural plow.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, describing the radial plan, drainage, and plowing toy finding of Banawali."
    ),
    (
        "With reference to the Great Bath of Mohenjo-daro, consider the following statements:\n1. The rectangular pool is located on the Citadel and lined with tightly fitted baked bricks.\n2. Natural bitumen (asphalt) was applied over the brickwork to ensure waterproofing.\n3. It was filled using a large brick-lined well located in an adjacent room.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All three statements represent verified archaeological facts about the construction, sealing, and water source of the Great Bath."
    ),
    (
        "Consider the following statements regarding the bricks used in Harappan construction:\n1. Both mud and burnt bricks followed a strict ratio of 4:2:1 (length:width:thickness).\n2. Standard brick dimensions for private houses were 28cm x 14cm x 7cm.\n3. Interlocking patterns, known as the English bond, were used to lay bricks for walls.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, outlining the brick ratios, house brick sizes, and interlocking English bond technique."
    ),
    (
        "With reference to Dholavira's water engineering, consider the following statements:\n1. Check dams were constructed across seasonal streams like the Manhar and Mansar.\n2. Dammed runoff water was diverted into a series of 16 stone-cut reservoirs.\n3. Dholavira's fortifications and reservoir walls were constructed using dressed local limestone blocks.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, describing the stream damming, reservoir count, and stone masonry at Dholavira."
    ),
    (
        "Consider the following statements regarding the site of Surkotada:\n1. Both the citadel and residential lower town are enclosed by a common stone fortification wall.\n2. Gateway structures built of rubble stone masonry have been excavated.\n3. Debated skeletal remains of horses have been reported in its upper layers.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, detailing Surkotada's stone walls, stone gateway, and horse bone reports."
    ),
    (
        "With reference to the site of Chanhudaro, consider the following statements:\n1. It is the only major Harappan city that completely lacks a Citadel mound.\n2. It functioned as an unfortified craft suburb specializing in bead-making and shell-cutting.\n3. A brick showing the paw print of a dog chasing a cat was excavated here.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct and define the unique unfortified craft planning and animal footprint brick of Chanhudaro."
    )
]

mock_data_hin = [
    (
        "हड़प्पा सभ्यता की वजन और माप प्रणालियों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मानकीकृत बाट मुख्य रूप से चर्ट पत्थर से तराशे गए घनाकार खंड होते थे।\n2. कम वजन के लिए द्वि-आधारी (binary) पैमाने (64 तक) और उच्च वजन के लिए दशमलव (decimal) पैमाने का उपयोग होता था।\n3. अनुपात 16 के आधार वजन का मान लगभग 13.63 ग्राम था।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं और हड़प्पा मापन प्रणाली की सामग्री, बाटों के अनुपात और मूल वजन का सटीक वर्णन करते हैं।"
    ),
    (
        "हड़प्पा शहरों के भौगोलिक विभाजन के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. किला (Citadel) आमतौर पर पश्चिम में स्थित होता था और कच्चे चबूतरे पर बना होता था जहाँ सार्वजनिक भवन होते थे।\n2. निचला नगर (Lower Town) पूर्व में स्थित था जो व्यापारियों और कारीगरों का रिहायशी इलाका था।\n3. गुजरात का धोलावीरा तीन भागों: किला, मध्य नगर और निचले नगर में विभाजित है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं और किला-निचले नगर के मानक प्रतिरूप तथा धोलावीरा के त्रि-स्तरीय विभाजन को स्पष्ट करते हैं।"
    ),
    (
        "हड़प्पा जल निकासी और सीवरेज प्रणाली के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. सड़कों के नाले पकी ईंटों से पक्के किए जाते थे और उन्हें पत्थरों या ईंटों की शिलाओं से ढका जाता था।\n2. सार्वजनिक नालियों में जाने से पहले ठोस कचरा जमा करने के लिए सड़क के कोनों पर मिट्टी के शोषक मटके रखे जाते थे।\n3. नालियों की सफाई के लिए नियमित स्थानों पर निरीक्षण कक्ष (manholes) बने थे।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो मुख्य सीवरों, कचरा मटकों और निरीक्षण मैनहोल के नियोजन का विवरण देते हैं।"
    ),
    (
        "कालीबंगन स्थल के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. किला (Citadel) और निचला नगर (Lower Town) दोनों अलग-अलग दीवारों से सुरक्षित किए गए थे।\n2. यहाँ पकी ईंटों के सीवरों के बजाय नालियों के लिए खोखले लकड़ी के तनों का उपयोग किया गया था।\n3. पूर्व-हड़प्पा स्तरों से जुते हुए खेत के साक्ष्य मिले हैं जो ग्रिड पैटर्न पर जुताई दर्शाते हैं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो कालीबंगन की सुरक्षात्मक दीवारों, लकड़ी की नालियों और जुते हुए खेत के साक्ष्यों का विवरण देते हैं।"
    ),
    (
        "बनावली स्थल के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. सड़कें ग्रिड पैटर्न के बजाय किले के टीले से बाहर की ओर अरीय (radial) रूप में व्यवस्थित थीं।\n2. रिहायशी पानी को सड़कों पर जमा करने के लिए सड़कों के कोनों पर मटके रखे जाते थे।\n3. यहाँ से मिट्टी का एक अच्छी स्थिति में बना हल का खिलौना मिला है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो बनावली के अरीय सड़कों, जल निकासी और खिलौने हल की खोज का विवरण देते हैं।"
    ),
    (
        "मोहनजोदड़ो के विशाल स्नानागार (Great Bath) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह आयताकार कुंड किले (Citadel) पर स्थित है और पकी ईंटों को बारीक रूप से जोड़कर बनाया गया है।\n2. पानी का रिसाव रोकने के लिए ईंटों पर प्राकृतिक डामर (बिटुमेन) की एक परत लगाई गई थी।\n3. इसे भरने के लिए पास के कमरे में बने ईंटों के एक बड़े कुएं से पानी लाया जाता था।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं और विशाल स्नानागार के निर्माण, जल-रोधी परत और पानी के स्रोत की जानकारी देते हैं।"
    ),
    (
        "हड़प्पा निर्माण में प्रयुक्त ईंटों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. कच्ची और पकी दोनों ईंटों का अनुपात हमेशा 4:2:1 (लंबाई:चौड़ाई:मोटाई) होता था।\n2. निजी घरों के लिए प्रयुक्त ईंटों का आकार 28 सेमी x 14 सेमी x 7 सेमी होता था।\n3. दीवारें मजबूत करने के लिए ईंटों को एक-दूसरे में फंसाकर (English bond/interlocking pattern) बिछाया जाता था।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो ईंटों के अनुपात, घर की ईंटों के आकार और इंग्लिश बांड दीवार तकनीक को दर्शाते हैं।"
    ),
    (
        "धोलावीरा के जल प्रबंधन के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मनहर और मनसर जैसी मौसमी नदियों पर पानी मोड़ने के लिए बांध बनाए गए थे।\n2. बाँध का पानी मोड़कर 16 आपस में जुड़े जलाशयों में संचित किया जाता था।\n3. धोलावीरा के जलाशयों की दीवारें स्थानीय तराशे गए चूना पत्थरों के खंडों से बनाई गई थीं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो धोलावीरा के बांधों, जलाशयों और पत्थर की वास्तुकला को स्पष्ट करते हैं।"
    ),
    (
        "सुरकोटदा स्थल के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इसमें किला और निचला नगर दोनों एक साझी पत्थर की सुरक्षा दीवार से घिरे थे।\n2. पत्थरों से बना एक प्रवेश द्वार और रक्षक कक्ष उत्खनित किए गए हैं।\n3. इसके ऊपरी स्तरों से घोड़े की हड्डियों के विवादास्पद साक्ष्य मिले हैं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं और सुरकोटदा की दीवारों, प्रवेश द्वार और घोड़े की हड्डियों की रिपोर्ट को दर्शाते हैं।"
    ),
    (
        "चन्हुदड़ो के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह एकमात्र प्रमुख हड़प्पा शहर है जिसमें कोई किला (citadel) नहीं था।\n2. यह एक बिना किलेबंदी वाला शिल्प नगर था जो मनके और शंख बनाने में विशेषज्ञता रखता था।\n3. यहाँ से बिल्ली का पीछा करते हुए कुत्ते के पंजों के निशान वाली ईंट मिली है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो चन्हुदड़ो के बिना किले वाले नियोजन, उद्योगों और पशु पंजों के निशान वाली ईंट को दर्शाते हैं।"
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
