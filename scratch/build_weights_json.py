import json
import os

ENG_DIR = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\HarappanIndus-Valley-Civilisation\Weights-and-Measures"
HIN_DIR = os.path.join(ENG_DIR, "hi")
os.makedirs(HIN_DIR, exist_ok=True)

# English base structure
eng_data = {
    "breadcrumbs": {
        "parent": "UPSC Syllabus",
        "parentUrl": "/upsc/",
        "current": "Weights & Measures"
    },
    "hero": {
        "title": "Harappan Weights, Measures & Metrological Standardization",
        "description": "Analyse the highly standardized weight systems, binary and decimal ratios, linear scales (ivory, shell, bronze), brick proportions (4:2:1), and trade metrology of the Indus Valley Civilisation for UPSC GS-1."
    },
    "labels": {
        "clickToExpand": "Click to expand details",
        "mockIntro": {
            "title": "Interactive UPSC Mock Test",
            "description": "Test your knowledge on Harappan weights, binary-decimal ratios, linear scales, and metrological standardization. This timed mock test contains 10 high-yield, exam-standard questions with negative marking.",
            "startBtn": "Start Mock Test"
        },
        "mockPlay": {
            "prevBtn": "Previous Question",
            "nextBtn": "Next Question",
            "submitBtn": "Submit Test"
        }
    },
    "timeline": {
        "title": "Evolution of Harappan Metrology",
        "description": "Chronological development of standardization and weight-measure integration in the Indus Valley Civilisation.",
        "cards": [
            {
                "period": "Early Harappan Regionalism",
                "date": "c. 3300 BCE - 2600 BCE",
                "details": "Development of localized weight standards at regional centers (e.g., Kot Diji, Amri). Initial experimentation with binary weighing for local trade."
            },
            {
                "period": "Mature Harappan Uniformity",
                "date": "c. 2600 BCE - 1900 BCE",
                "details": "Establishment of the highly standardized, pan-Harappan weight system based on chert cubical weights. Deployment of linear scales at Mohenjo-daro (shell), Lothal (ivory), and Harappa (bronze). Strict enforcement of the 4:2:1 brick ratio across all urban settlements."
            },
            {
                "period": "Late Harappan Decentralization",
                "date": "c. 1900 BCE - 1300 BCE",
                "details": "Gradual fragmentation of standardized weight ratios. Return to local, regional measurement practices and decline of precise ivory and shell scales as long-distance trade faded."
            }
        ]
    },
    "mnemonics": {
        "title": "Mnemonics & Memory Hacks",
        "description": "Visual triggers to memorize key metrological facts, ratios, and findings for UPSC.",
        "items": [
            {
                "title": "Mnemonic 1: Base Scale Materials",
                "phrase": "\"I-L / S-M / C-H (Ivory-Lothal, Shell-Mohenjo, Copper-Harappa)\"",
                "decryption": "Scale materials at major sites: **I**vory at **L**othal, **S**hell at **M**ohenjo-daro, and **C**opper/Bronze at **H**arappa."
            },
            {
                "title": "Mnemonic 2: Standard Unit Value",
                "phrase": "\"Lucky Sixteen - 13.6 (Base 16 is 13.6g)\"",
                "decryption": "The standard unit of weight was based on the binary ratio of **16**, which corresponds to approximately **13.63 grams**."
            },
            {
                "title": "Mnemonic 3: Brick Dimension Ratio",
                "phrase": "\"T-W-L = 1-2-4 (Thickness:Width:Length)\"",
                "decryption": "Harappan bricks show a strict ratio: **1** (Thickness) : **2** (Width) : **4** (Length)."
            }
        ]
    },
    "flashcards": {
        "title": "Active Recall Flashcards",
        "description": "Test your memory on critical Harappan weights, measures, and scales.",
        "items": [
            {
                "question": "What is the primary material used to manufacture Harappan weights?",
                "answer": "<strong>Chert</strong>, a microcrystalline quartz, was the most common. Agate, jasper, chalcedony, and slate were also used.",
                "icon": "fa-cube"
            },
            {
                "question": "Explain the dual mathematical system of Harappan weights.",
                "answer": "Lower values followed a <strong>binary system</strong> (1, 2, 4, 8, 16, 32, 64), while higher values transitioned into a <strong>decimal system</strong> (160, 200, 320, 640, 1600, etc.).",
                "icon": "fa-calculator"
            },
            {
                "question": "Where was the famous ivory scale found, and what is its division size?",
                "answer": "Found at <strong>Lothal</strong>. It has the smallest division ever recorded on a Bronze Age scale, measuring just <strong>1.7 mm</strong> (0.067 inches).",
                "icon": "fa-ruler"
            },
            {
                "question": "What is the standard ratio of Harappan building bricks?",
                "answer": "A strict ratio of <strong>1:2:4</strong> (thickness to width to length), which holds true for both sun-dried and kiln-baked bricks across almost all cities.",
                "icon": "fa-shapes"
            },
            {
                "question": "How did the Harappan weight system survive into later Indian history?",
                "answer": "The binary base unit ratio of 16 survived until 1957 in the traditional currency/weight system, where <strong>1 Rupee = 16 Annas</strong>.",
                "icon": "fa-hourglass-start"
            }
        ]
    },
    "deepDive": {
        "title": "Syllabus Core Study Notes (Deep-Dive)",
        "description": "Master the weights, measures, scales, and construction standards of the Indus valley.",
        "sections": [
            {
                "title": "1. The Standardized Weight System (Binary vs Decimal)",
                "content": """<p>The Harappan civilization achieved an unprecedented level of standardization in its weight system, which was vital for regulating its extensive internal and external trade networks.</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-cubes"></i> Material and Morphology of Weights</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>Chert Dominance:</strong> The vast majority of weights were carved out of high-quality chert (mostly sourced from the Rohri hills of Sindh). They are characterized by smooth, polished cubical (cubic) shapes.</li>
      <li><strong>Alternative Materials:</strong> Other stones like agate, chalcedony, jasper, limestone, slate, and alabaster were occasionally used, especially for very small or very large denominations.</li>
      <li><strong>Undecorated Nature:</strong> Unlike Harappan seals, the weights are completely plain, bearing no artistic representations, markings, or inscriptions.</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-superscript"></i> Mathematical Structure (Binary & Decimal)</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>Binary Lower Range:</strong> For small-scale measurements (e.g., weighing precious metals, gems, and spices), the weights followed a strict binary system: ratios of 1, 2, 4, 8, 16, 32, 64.</li>
      <li><strong>Standard Base Unit:</strong> The weight unit of ratio 16 was the most common base unit. It corresponds to an absolute weight of approximately 13.63 grams.</li>
      <li><strong>Decimal Upper Range:</strong> For large-scale bulk commodities, the system shifted to a decimal pattern: ratios of 160, 200, 320, 640, 1600, 3200, 6400, 8000, 12800, up to 12,800.</li>
    </ul>
  </div>
</div>""",
                "masteryZone": []
            },
            {
                "title": "2. Linear Measurements & Scales",
                "content": """<p>Linear measurement in the Indus Valley was highly precise, as evidenced by archaeological discoveries of calibrated scales made of various materials.</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-ruler-combined"></i> Calibrated Scales of the Indus Valley</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>Lothal Ivory Scale:</strong> Discovered at the port town of Lothal, this scale features the smallest division ever recorded on a Bronze Age ruler: 1.7 mm (0.067 inches), indicating extreme accuracy in maritime craftwork.</li>
      <li><strong>Mohenjo-daro Shell Scale:</strong> Made of marine shell, this scale features a division marking of 6.7 mm (0.264 inches). A sequence of these divisions defines the 'Indus inch' (approx. 33.5 mm or 1.32 inches).</li>
      <li><strong>Harappa Bronze Scale:</strong> A copper-alloy/bronze bar scale found at Harappa indicates that linear measures were also cast in metal.</li>
      <li><strong>Kalibangan Terracotta Scale:</strong> A broken clay ruler found in Rajasthan confirms that measurement tools were also manufactured for local brick-masons.</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-border-all"></i> Modular Brick Standardization (4:2:1)</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>Strict Dimension Ratio:</strong> Across the entire Harappan territory, building bricks (both sun-dried for ordinary houses and kiln-fired for drains/fortifications) adhere to a rigid ratio: Thickness : Width : Length = 1 : 2 : 4.</li>
      <li><strong>Common Brick Size:</strong> The standard size for domestic dwellings was 7 x 15 x 31 cm, while larger bricks (e.g., 10 x 20 x 40 cm) were used for monumental city walls and gateways.</li>
      <li><strong>Interlocking Masonry:</strong> The 1:2:4 proportion allowed masons to lay bricks in an interlocking header-and-stretcher pattern (English bond), providing structural stability to multi-story buildings and massive dockyards.</li>
    </ul>
  </div>
</div>""",
                "masteryZone": []
            },
            {
                "title": "3. Practical Application: Construction, Taxation, and Trade Rationale",
                "content": """<p>The standardization of weights and measures in Harappan society suggests a highly organized administrative and economic framework, though the nature of enforcement remains debated.</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-coins"></i> Metrological Utility in Trade and Taxation</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>Barter Regulation:</strong> Standardized weights allowed merchants to conduct barter trade with absolute consistency, preventing disputes over grain quantities, metals, or cotton bundles.</li>
      <li><strong>Tribute and Taxation:</strong> Standard weights enabled centralized authorities (or merchant guilds) to collect taxes or tributes in grain, which were stored in state granaries at Mohenjo-daro and Harappa.</li>
      <li><strong>Micro-measurements for Luxury:</strong> Tiny, precise weights found at bead workshops (Lothal, Chanhudaro) suggest that gold dust, carnelian beads, lapis lazuli, and silver were weighed with scientific accuracy.</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-scale-balanced"></i> Rationale of Administration and Heritage</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>The Authority Debate:</strong> The uniform distribution of Rohri chert weights across a million square kilometers implies a highly centralized administrative authority (a 'state' or a powerful merchant coalition) that controlled manufacturing standards.</li>
      <li><strong>Balance Scales:</strong> Archaeological excavations have yielded numerous balance scale sets, consisting of copper/bronze pans and suspension strings.</li>
      <li><strong>Historical Continuity:</strong> The binary base of 16 survived as a cultural legacy in India for millennia. Up until decimalization in 1957, the Indian currency followed the ratio where 1 Rupee was divided into 16 Annas.</li>
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
            "<strong>Trap 1:</strong> Avoid statements claiming that Harappan weights were decorated with animal engravings or seals script. Unlike seals, weights are completely plain and undecorated.",
            "<strong>Trap 2:</strong> Watch out for statements asserting that the weight system was exclusively binary. It was binary for lower denominations but transitioned to a decimal system for higher denominations.",
            "<strong>Trap 3:</strong> Do not assume that scales from Lothal, Mohenjo-daro, and Harappa indicate a single, unified linear standard. The three scales show slightly different base units, indicating possible regional subsystems or multiple standards.",
            "<strong>Trap 4:</strong> Avoid options claiming that bricks in rural areas did not follow the standard ratio. The 1:2:4 ratio was strictly followed in both major cities and small rural outposts.",
            "<strong>Trap 5:</strong> Watch out for questions claiming that weights were made of iron. Iron was completely unknown in the Bronze Age Harappan Civilisation; weights were always carved from stone (like chert) or occasionally cast in copper."
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
        "current": "बाट और माप"
    },
    "hero": {
        "title": "हड़प्पा बाट, माप और मापन प्रणाली का मानकीकरण",
        "description": "यूपीएससी जीएस-1 परीक्षा के लिए सिंधु घाटी सभ्यता के बाटों, बाइनरी और दशमलव अनुपातों, रैखिक पैमानों (हाथीदांत, शंख, कांसा), ईंटों के अनुपात (4:2:1) और व्यापार मापन प्रणालियों का विश्लेषण।"
    },
    "labels": {
        "clickToExpand": "विवरण देखने के लिए क्लिक करें",
        "mockIntro": {
            "title": "इंटरैक्टिव यूपीएससी मॉक टेस्ट",
            "description": "हड़प्पा बाट, बाइनरी-दशमलव अनुपात, रैखिक पैमानों और मापन प्रणालियों पर अपने ज्ञान का परीक्षण करें। इस समयबद्ध मॉक टेस्ट में नकारात्मक अंकन के साथ परीक्षा स्तर के 10 महत्वपूर्ण प्रश्न शामिल हैं।",
            "startBtn": "मॉक टेस्ट शुरू करें"
        },
        "mockPlay": {
            "prevBtn": "पिछला प्रश्न",
            "nextBtn": "अगला प्रश्न",
            "submitBtn": "परीक्षण जमा करें"
        }
    },
    "timeline": {
        "title": "हड़प्पा मापन प्रणाली का विकास",
        "description": "सिंधु घाटी सभ्यता में मानकीकरण और बाट-माप एकीकरण का कालानुक्रमिक विकास।",
        "cards": [
            {
                "period": "प्रारंभिक हड़प्पा क्षेत्रीय प्रवृत्तियां",
                "date": "लगभग 3300 ईसा पूर्व - 2600 ईसा पूर्व",
                "details": "क्षेत्रीय केंद्रों (जैसे कोट दीजी, आमरी) पर स्थानीय बाट मानकों का विकास। स्थानीय व्यापार के लिए बाइनरी (द्विआधारी) तौल प्रणालियों का शुरुआती उपयोग।"
            },
            {
                "period": "परिपक्व हड़प्पा मानकीकरण",
                "date": "लगभग 2600 ईसा पूर्व - 1900 ईसा पूर्व",
                "details": "चर्ट के घनाकार बाटों पर आधारित अत्यधिक मानकीकृत, अखिल-हड़प्पा बाट प्रणाली की स्थापना। मोहनजोदड़ो (शंख), लोथल (हाथीदांत) और हड़प्पा (कांसा) में रैखिक पैमानों का उपयोग। सभी शहरी बस्तियों में ईंटों के 4:2:1 अनुपात का कड़ाई से पालन।"
            },
            {
                "period": "उत्तर हड़प्पा विकेंद्रीकरण",
                "date": "लगभग 1900 ईसा पूर्व - 1300 ईसा पूर्व",
                "details": "मानकीकृत बाट अनुपातों का क्रमिक पतन। स्थानीय और क्षेत्रीय मापन प्रणालियों की वापसी तथा दीर्घकालिक विदेशी व्यापार के समाप्त होने पर सटीक पैमानों का ह्रास।"
            }
        ]
    },
    "mnemonics": {
        "title": "याद रखने के सूत्र और ट्रिक्स",
        "description": "यूपीएससी परीक्षा के लिए महत्वपूर्ण मापन तथ्यों, अनुपातों और निष्कर्षों को याद रखने के सूत्र।",
        "items": [
            {
                "title": "याद रखने का सूत्र 1: पैमानों (Scales) की निर्माण सामग्री",
                "phrase": "\"हा-लो / शं-मो / ता-ह (हाथीदांत-लोथल, शंख-मोहनजोदड़ो, तांबा-हड़प्पा)\"",
                "decryption": "प्रमुख स्थलों पर पैमाने: **हा**थीदांत का पैमाना **लो**थल से, **शं**ख का पैमाना **मो**हनजोदड़ो से, और **ता**ंबे का पैमाना **ह**ड़प्पा से मिला है।"
            },
            {
                "title": "याद रखने का सूत्र 2: मानक बाट इकाई मान",
                "phrase": "\"लकी सोलह - 13.6 (16 इकाई का मान 13.6 ग्राम है)\"",
                "decryption": "तौल की मुख्य मानक इकाई अनुपात **16** पर आधारित थी, जिसका वास्तविक वजन लगभग **13.63 ग्राम** था।"
            },
            {
                "title": "याद रखने का सूत्र 3: ईंटों का आयाम अनुपात",
                "phrase": "\"मो-चौ-लं = 1-2-4 (मोटाई:चौड़ाई:लंबाई)\"",
                "decryption": "हड़प्पाकालीन ईंटों का एक निश्चित आयाम अनुपात था: **1** (मोटाई) : **2** (चौड़ाई) : **4** (लंबाई)।"
            }
        ]
    },
    "flashcards": {
        "title": "सक्रिय स्मरण फ्लैशकार्ड (Active Recall)",
        "description": "हड़प्पा बाट, माप और पैमानों पर अपने ज्ञान का परीक्षण करें।",
        "items": [
            {
                "question": "हड़प्पा के बाटों के निर्माण में मुख्य रूप से किस सामग्री का उपयोग किया जाता था?",
                "answer": "मुख्य रूप से <strong>चर्ट (Chert)</strong> पत्थर का। इसके अतिरिक्त अगेट, जैस्पर, कैल्सेडोनी और स्लेट का भी उपयोग किया जाता था।",
                "icon": "fa-cube"
            },
            {
                "question": "हड़प्पा बाटों की दोहरी गणितीय प्रणाली क्या थी?",
                "answer": "निचले मूल्य <strong>बाइनरी सिस्टम</strong> (1, 2, 4, 8, 16, 32, 64) का पालन करते थे, जबकि उच्च मूल्य <strong>दशमलव (decimal) सिस्टम</strong> (160, 200, 320, 640, 1600 आदि) में बदल जाते थे।",
                "icon": "fa-calculator"
            },
            {
                "question": "प्रसिद्ध हाथीदांत का पैमाना कहाँ मिला था और इसकी विभाजन इकाई क्या है?",
                "answer": "यह <strong>लोथल</strong> से प्राप्त हुआ था। इसका सबसे छोटा दर्ज विभाजन केवल <strong>1.7 मिमी</strong> है, जो कांस्य युग में सबसे सटीक है।",
                "icon": "fa-ruler"
            },
            {
                "question": "हड़प्पा की इमारती ईंटों का मानक अनुपात क्या था?",
                "answer": "लगभग सभी शहरों में धूप में सुखाई गई और भट्टी में पकाई गई ईंटों के लिए <strong>1:2:4</strong> (मोटाई : चौड़ाई : लंबाई) का सख्त अनुपात था।",
                "icon": "fa-shapes"
            },
            {
                "question": "हड़प्पा की बाट प्रणाली बाद के भारतीय इतिहास में कैसे जीवित रही?",
                "answer": "बाइनरी 16 का अनुपात 1957 तक पारंपरिक भारतीय मुद्रा और तौल प्रणालियों में जीवित रहा, जहाँ <strong>1 रुपया = 16 आने</strong> के बराबर होता था।",
                "icon": "fa-hourglass-start"
            }
        ]
    },
    "deepDive": {
        "title": "पाठ्यक्रम मुख्य अध्ययन नोट्स (विस्तृत)",
        "description": "सिंधु घाटी के बाटों, पैमानों और निर्माण मानकों का अध्ययन करें।",
        "sections": [
            {
                "title": "1. मानक बाट प्रणाली (द्विआधारी बनाम दशमलव)",
                "content": """<p>हड़प्पा सभ्यता ने अपनी बाट प्रणाली में अभूतपूर्व मानकीकरण हासिल किया, जो इसके व्यापक आंतरिक और बाह्य व्यापार नेटवर्क को विनियमित करने के लिए अत्यंत महत्वपूर्ण था।</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-cubes"></i> बाटों की निर्माण सामग्री और आकार</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>चर्ट पत्थर की प्रधानता:</strong> अधिकांश बाट उच्च गुणवत्ता वाले चर्ट (Rohri chert) से तराशे गए थे। ये सुचारू, पॉलिशदार घनाकार (cubic) आकार के होते थे।</li>
      <li><strong>अन्य सामग्रियां:</strong> अगेट, कैल्सेडोनी, जैस्पर, चूना पत्थर और स्लेट का भी उपयोग किया जाता था, विशेष रूप से बहुत छोटे या बड़े बाट बनाने में।</li>
      <li><strong>सजावट रहित प्रकृति:</strong> मुहरों के विपरीत, बाट पूरी तरह से सादे थे, जिन पर कोई चित्र, निशान या लेख नहीं होते थे।</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-superscript"></i> गणितीय संरचना (बाइनरी और दशमलव)</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>निचला बाइनरी वर्ग:</strong> कीमती धातुओं, मोतियों और मसालों के लिए बाइनरी अनुपात: 1, 2, 4, 8, 16, 32, 64 का उपयोग होता था।</li>
      <li><strong>मानक आधार इकाई:</strong> 16 अनुपात का बाट सर्वाधिक लोकप्रिय था, जिसका वास्तविक वजन लगभग 13.63 ग्राम था।</li>
      <li><strong>उच्च दशमलव वर्ग:</strong> बड़ी वस्तुओं और अनाज के लिए दशमलव प्रणाली: 160, 200, 320, 640, 1600, 3200, 6400, 8000, 12800 का उपयोग होता था।</li>
    </ul>
  </div>
</div>""",
                "masteryZone": []
            },
            {
                "title": "2. रैखिक माप और पैमाना (Scales)",
                "content": """<p>सिंधु घाटी में रैखिक माप प्रणाली अत्यधिक सटीक थी, जैसा कि विभिन्न स्थलों से प्राप्त पैमानों (rulers) से स्पष्ट होता है।</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-ruler-combined"></i> सिंधु घाटी के कैलिब्रेटेड पैमाने</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>लोथल का हाथीदांत पैमाना:</strong> लोथल से प्राप्त इस पैमाने पर कांस्य युग का सबसे छोटा दर्ज विभाजन 1.7 मिमी है, जो शिल्प कौशल की सटीकता को दर्शाता है।</li>
      <li><strong>मोहनजोदड़ो का शंख पैमाना:</strong> समुद्री शंख से बने इस पैमाने का विभाजन मान 6.7 मिमी है। इन विभाजनों की एक श्रृंखला 'सिंधु इंच' (लगभग 33.5 मिमी या 1.32 इंच) को परिभाषित करती थी।</li>
      <li><strong>हड़प्पा का तांबा/कांसा पैमाना:</strong> हड़प्पा से मिली कांसे की छड़ दर्शाती है कि रैखिक पैमाने धातु में भी ढाले जाते थे।</li>
      <li><strong>कालीबंगन का मिट्टी पैमाना:</strong> मिट्टी की टूटी हुई पट्टी स्थानीय ईंट बनाने वालों के पास मापन साधनों की उपस्थिति दर्शाती है।</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-border-all"></i> ईंटों का मानकीकरण (4:2:1)</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>निश्चित अनुपात:</strong> पूरे हड़प्पा क्षेत्र में घरों (धूप में सूखी) और नालियों/किलेबंदी (भट्टी में पकी) की ईंटों के आयाम का अनुपात हमेशा 1 : 2 : 4 (मोटाई : चौड़ाई : लंबाई) होता था।</li>
      <li><strong>सामान्य आकार:</strong> घरेलू उपयोग की ईंटें 7x15x31 सेमी की थीं, जबकि विशाल सुरक्षा प्राचीरों के लिए 10x20x40 सेमी की बड़ी ईंटें प्रयुक्त होती थीं।</li>
      <li><strong>इंटरलॉकिंग चिनाई:</strong> 1:2:4 अनुपात के कारण दीवार निर्माण में इंटरलॉकिंग पैटर्न (English bond) आसान हुआ, जिससे बहुमंजिला इमारतों को मजबूती मिली।</li>
    </ul>
  </div>
</div>""",
                "masteryZone": []
            },
            {
                "title": "3. व्यावहारिक अनुप्रयोग: निर्माण, कराधान और व्यापारिक तर्क",
                "content": """<p>हड़प्पा समाज में बाट-माप का यह स्तर प्रशासनिक और आर्थिक संगठन को दर्शाता है, हालांकि इसे लागू करने वाली सत्ता को लेकर विद्वानों में मतभेद हैं।</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-coins"></i> व्यापार और करों में उपयोगिता</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>वस्तु विनिमय (Barter) का नियमन:</strong> बाटों की निश्चितता से अनाज, सूत और धातुओं के विनिमय में धोखाधड़ी से बचा जा सकता था।</li>
      <li><strong>कर और राजस्व संग्रह:</strong> मानकीकृत बाटों की मदद से शासक वर्ग या व्यापारिक गिल्ड अनाज के रूप में कर एकत्र करते थे, जिसे राजकीय अन्नागारों में संग्रहित किया जाता था।</li>
      <li><strong>विलासिता की वस्तुओं के सूक्ष्म माप:</strong> मनकों के कारखानों (लोथल, चन्हुदड़ो) से अत्यंत छोटे बाट मिले हैं, जो सोने की धूल और कीमती पत्थरों को तोलने के काम आते थे।</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-scale-balanced"></i> प्रशासन का स्वरूप और हमारी विरासत</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>केंद्रीय सत्ता का विवाद:</strong> पूरे हड़प्पा क्षेत्र (लगभग 10 लाख वर्ग किमी) में रोहरी चर्ट के बाटों की एकरूपता किसी केंद्रीय सत्ता या शक्तिशाली व्यापारी संघ के नियंत्रण को दर्शाती है।</li>
      <li><strong>तराजू के पलड़े:</strong> उत्खनन में तांबे/कांसे के गोल पलड़े मिले हैं, जिन्हें रस्सी से लटकाकर संतुलन तराजू (balance scales) की तरह उपयोग किया जाता था।</li>
      <li><strong>ऐतिहासिक निरंतरता:</strong> बाइनरी 16 का आधार भारत के पारंपरिक मापन में हजारों वर्षों तक बना रहा। वर्ष 1957 तक भारत में 1 रुपया = 16 आने की प्रणाली लागू थी।</li>
    </ul>
  </div>
</div>""",
                "masteryZone": []
            }
        ]
    },
    "traps": {
        "title": "यूपीएससी परीक्षा के लिए चेतावनी अलर्ट (भ्रम से बचें)",
        "items": [
            "<strong>चेतावनी 1:</strong> परीक्षा में ऐसे कथनों से बचें जो यह दावा करते हैं कि बाटों पर जानवरों के चित्र या लिपि खुदी होती थी। बाट पूरी तरह से सादे और बिना किसी नक्काशी के होते थे।",
            "<strong>चेतावनी 2:</strong> उन विकल्पों से बचें जो यह कहते हैं कि हड़प्पा काल में केवल बाइनरी प्रणाली प्रयुक्त होती थी। छोटे मापों के लिए बाइनरी तथा बड़े मापों के लिए दशमलव प्रणाली लागू थी।",
            "<strong>चेतावनी 3:</strong> इस बात पर ध्यान दें कि लोथल, मोहनजोदड़ो और हड़प्पा के पैमाने पूरी तरह से समान लंबाई की इकाई पर आधारित नहीं थे। वे तीन अलग-अलग उप-इकाइयों को दर्शाते हैं।",
            "<strong>चेतावनी 4:</strong> उन विकल्पों से बचें जो यह दावा करते हैं कि देहाती क्षेत्रों में ईंटों का आयाम अनुपात अलग था। 1:2:4 का अनुपात शहरों और छोटे गांवों दोनों में एक समान था।",
            "<strong>चेतावनी 5:</strong> इस बात पर विशेष ध्यान दें कि धातु के बाट लोहे के नहीं बने थे। हड़प्पा काल में लोहे का ज्ञान नहीं था; बाट हमेशा पत्थरों (जैसे चर्ट) या कभी-कभी तांबे के होते थे।"
        ]
    },
    "practiceQuestions": [],
    "mockTestQuestions": []
}

# 50 English Practice Questions (Multi-statement, UPSC standard)
raw_practice_eng = [
    # 1. Chert dominance
    ("With reference to the weights and measures of the Indus Valley Civilisation, consider the following statements:\n1. The vast majority of Harappan weights were made of Rohri chert.\n2. Standard weights were cubical in shape and completely plain without markings.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 2, "Both statements are correct. The weights were made of high-quality Rohri chert and were plain, polished cubical stones with no markings."),
    # 2. Binary vs Decimal
    ("Consider the following statements regarding the mathematical structure of Harappan weights:\n1. The lower denominations followed a binary system of doubling.\n2. The higher denominations transitioned into a decimal system.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 2, "Both statements are correct. Lower values were binary (1, 2, 4, 8, 16, 32, 64) and higher values were decimal (160, 200, 320, 640, 1600, etc.)."),
    # 3. Base unit
    ("With reference to the standard weight unit of the Harappans, consider the following statements:\n1. The unit ratio of 16 was the most common standard weight.\n2. The absolute value of this base unit was approximately 13.63 grams.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 2, "Both statements are correct. The base unit of 16 was the most popular standard, corresponding to about 13.63 grams."),
    # 4. Brick proportions
    ("Consider the following statements regarding the construction materials of the Harappan civilization:\n1. Sun-dried and kiln-baked bricks adhered to a strict ratio of 1:2:4 for thickness, width, and length.\n2. Rural settlements did not follow this brick ratio and used irregular stones.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 0, "Statement 1 is correct. Statement 2 is incorrect: the 1:2:4 brick ratio was uniformly maintained in both major cities and small villages."),
    # 5. Lothal ivory scale
    ("With reference to linear measurement devices in the Indus Valley Civilisation, consider the following statements:\n1. An ivory scale featuring the smallest division ever recorded on a Bronze Age scale was found at Lothal.\n2. The smallest division on the Lothal ivory scale measures approximately 1.7 mm.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 2, "Both statements are correct. Lothal yielded an ivory scale with a remarkably precise division of 1.7 mm."),
    # 6. Mohenjo-daro shell scale
    ("Consider the following statements regarding the shell scale found at Mohenjo-daro:\n1. It was made of marine shell and featured markings representing a division of 6.7 mm.\n2. A sequence of these divisions defines the 'Indus inch' equivalent to 33.5 mm.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 2, "Both statements are correct. The Mohenjo-daro shell scale has divisions of 6.7 mm, forming a unit system of 33.5 mm (the Indus inch)."),
    # 7. Harappa bronze scale
    ("With reference to linear scales found in the Harappan civilization, consider the following statements:\n1. A bronze/copper bar with calibration marks was excavated at Harappa.\n2. Calibration marks are absent on all metal tools discovered in the Indus Valley.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 0, "Statement 1 is correct. Statement 2 is incorrect: the bronze bar scale from Harappa clearly proves that metal scales with calibration marks existed."),
    # 8. Scale materials
    ("Which of the following materials were utilized by the Harappans to manufacture linear scales?\n1. Ivory\n2. Shell\n3. Terracotta\n4. Bronze\nSelect the correct answer using the code given below:", ["1, 2 and 3 only", "1, 2 and 4 only", "2, 3 and 4 only", "1, 2, 3 and 4"], 3, "All four materials were used: ivory (Lothal), shell (Mohenjo-daro), terracotta (Kalibangan), and bronze (Harappa)."),
    # 9. Weight materials
    ("Consider the following statements regarding the raw materials of Harappan weights:\n1. Weights were carved exclusively out of chert.\n2. Agate, chalcedony, and jasper were also used for manufacturing smaller, precise weights.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 1, "Statement 2 is correct. Statement 1 is incorrect: while chert was dominant, other stones like agate, chalcedony, and jasper were also used."),
    # 10. plain weights
    ("With reference to the aesthetic features of Harappan weights, consider the following statements:\n1. Most weights bear short pictographic inscriptions in the Harappan script.\n2. Some weights show detailed relief carvings of the humped bull.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 3, "Neither 1 nor 2 is correct. Harappan weights are completely plain, without any script inscriptions or animal carvings."),
    # 11. Balance pans
    ("Consider the following statements regarding weighing technology in the Indus Valley Civilisation:\n1. Balance scale pans made of copper, bronze, and terracotta have been excavated.\n2. Standardized weights were suspended using animal hide straps from wooden beams.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 0, "Statement 1 is correct. Statement 2 is incorrect: balance pans were suspended using woven cords or strings, not animal hide straps."),
    # 12. Micro-weights
    ("With reference to small-scale weights in Harappan cities, consider the following statements:\n1. Tiny weights weighing less than 1 gram have been found at bead-making centers.\n2. These micro-weights were used to weigh gold, silver, and precious stone beads.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 2, "Both statements are correct. Mini and micro-weights have been excavated at Chanhudaro and Lothal workshops for weighing precious stones and metals."),
    # 13. Currency link
    ("Consider the following statements regarding the cultural continuity of Harappan weights in India:\n1. The binary unit base of 16 survived in the traditional Indian system where 1 Rupee equaled 16 Annas.\n2. The metric decimalization of 1957 completely replaced the traditional base-16 currency division.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 2, "Both statements are correct. The traditional division of 1 Rupee into 16 Annas was a direct cultural legacy of the Harappan base-16 system, which ended with metric decimalization in 1957."),
    # 14. Rohri chert source
    ("With reference to the trade of raw materials for weights, consider the following statements:\n1. Rohri in Sindh was the primary source of chert for manufacturing weights.\n2. Finished weights were manufactured at Rohri and distributed throughout the civilization.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 2, "Both statements are correct. Rohri hills served as the major quarrying and manufacturing hub for chert weights, which were exported across the entire region."),
    # 15. Standard unit weight values
    ("Consider the following statements regarding the actual values of Harappan weights:\n1. The smallest unit of weight was approximately 0.86 grams.\n2. The largest weights exceeded 10 kilograms, representing bulk trade measurements.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 2, "Both statements are correct. The weight denominations ranged from very tiny units (approx. 0.86g) up to massive stones weighing over 10kg."),
    # 16. Mesopotamian trade weights
    ("With reference to Harappan overseas trade, consider the following statements:\n1. Harappan-standard weights have been excavated in Mesopotamian cities like Ur.\n2. Harappan merchants adjusted their weights to match the local Mesopotamian shekel system.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 0, "Statement 1 is correct. Statement 2 is incorrect: Harappan weights found at Ur show that Harappan merchants maintained their own weight standards for international transactions in Dilmun and Mesopotamia."),
    # 17. Spherical weights
    ("Consider the following statements regarding weight shapes in the Indus Valley:\n1. Cubical weights represent the dominant shape category across all sites.\n2. Spherical, cylindrical, and barrel-shaped weights are completely absent from the archaeological record.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 0, "Statement 1 is correct. Statement 2 is incorrect: while cubical shapes dominate, other shapes like spherical and barrel-shaped weights have been excavated in small numbers."),
    # 18. Brick bonding
    ("With reference to Harappan architecture, consider the following statements:\n1. The 1:2:4 brick ratio enabled the construction of stable walls using the interlocking 'English bond' method.\n2. Brick sizes were completely random and varied from house to house within the same city blocks.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 0, "Statement 1 is correct. Statement 2 is incorrect: brick dimensions were highly standardized, with uniform sizes (e.g. 7x15x31 cm) used throughout city blocks."),
    # 19. Kalibangan clay scale
    ("Consider the following statements regarding the terracotta scale found at Kalibangan:\n1. It represents a tool used primarily by ordinary builders and brick masons.\n2. It has no calibration marks, suggesting it was used as a simple decorative object.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 0, "Statement 1 is correct. Statement 2 is incorrect: it features clear calibration markings, indicating its practical use as a local measurement ruler."),
    # 20. Imperial control
    ("With reference to the administration of Harappan weights, consider the following statements:\n1. The uniformity of weights indicates a strict central authority enforcing standardized metrology.\n2. Metrological standardization could also be maintained by self-regulating merchant guilds without a centralized political state.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 2, "Both statements are correct. The uniformity points to a central authority, but modern historians also suggest that merchant guilds could have self-enforced standards to facilitate trade."),
    # 21. Brick size fortification
    ("Consider the following statements regarding Harappan building bricks:\n1. Fortifications and public structures used larger brick sizes than domestic dwellings.\n2. Both large and small bricks maintained the identical 1:2:4 ratio.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 2, "Both statements are correct. Fortification walls used larger bricks (e.g., 10x20x40 cm) than houses (e.g., 7x15x31 cm), but both types adhered strictly to the 1:2:4 proportion."),
    # 22. Domestic weights
    ("With reference to the distribution of weights within Harappan cities, consider the following statements:\n1. Weights are found only in large public buildings like the Great Granary.\n2. Weights are commonly excavated in ordinary houses, indicating domestic trade or tax assessment.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 1, "Statement 2 is correct. Statement 1 is incorrect: weights are commonly found in residential blocks, proving trade transactions occurred at the household level."),
    # 23. Balance pans materials
    ("Consider the following statements regarding balance scales in Harappan sites:\n1. Balance pans were made of thin sheets of copper or bronze.\n2. Clay pans have also been found, indicating they were accessible to poorer merchants.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 2, "Both statements are correct. Balance pans were made of metal (copper/bronze) for premium scales, and terracotta/clay for ordinary scales."),
    # 24. Linear scale units comparison
    ("With reference to linear scales of the Indus Valley, consider the following statements:\n1. The base units on the Mohenjo-daro shell scale and the Lothal ivory scale are exactly identical.\n2. The slight differences in scale calibrations indicate regional metrological variations.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 1, "Statement 2 is correct. Statement 1 is incorrect: the scales show slightly different unit systems, suggesting regional variations or distinct standards for different crafts."),
    # 25. Late Harappan weight collapse
    ("Consider the following statements regarding the Late Harappan phase:\n1. The standardization of weights collapsed, and regional weight systems re-emerged.\n2. Precise scales of ivory and shell disappeared from archaeological layers.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 2, "Both statements are correct. The collapse of long-distance trade and cities led to the fragmentation of standardized weights and the disappearance of luxury scales."),
    # 26. Rohri chert export
    ("With reference to Rohri chert quarries, consider the following statements:\n1. Chert blocks were quarried and rough-shaped at Rohri before being transported to cities for final polishing.\n2. Specialized weight manufacturing workshops have been identified at Mohenjo-daro.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 2, "Both statements are correct. Core preparation occurred at the quarries, and fine shaping was done at urban craft workshops like Mohenjo-daro."),
    # 27. Gold weighing
    ("Consider the following statements regarding the weighing of precious metals in Harappa:\n1. The binary weight system allowed for the measurement of fractions of a gram.\n2. Balance scales were sensitive enough to measure small amounts of gold dust.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 2, "Both statements are correct. The binary division reached very small units, and balance pans were designed for precise measurements of precious metals."),
    # 28. Standardized street widths
    ("With reference to Harappan town planning, consider the following statements:\n1. Street widths were designed in standardized multiples of a base measurement.\n2. The width ratios of roads and lanes followed a 1:2:3:4 grid system.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 2, "Both statements are correct. Harappan streets show standard dimensions (e.g., lanes of 1.8m, streets of 3.6m, avenues of 7.2m), matching a 1:2:3:4 layout."),
    # 29. Weight markings
    ("Consider the following statements:\n1. None of the excavated Harappan weights show any signs of numeric values written on them.\n2. Harappan merchants identified weight denominations by their size and standard dimensions.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 2, "Both statements are correct. Weights carried no numeric markings; their values were recognized solely by size, material, and standard shape."),
    # 30. Agate weights
    ("With reference to premium materials used for weights, consider the following statements:\n1. Banded agate was carved into beautiful, precise weights for high-value trade.\n2. Agate weights have been found primarily in public treasury structures.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 0, "Statement 1 is correct. Statement 2 is incorrect: agate weights were used in craft workshops and residential quarters for trade, not just treasury structures."),
    # 31. Harappan scale precision
    ("Consider the following statements regarding Bronze Age measurement systems:\n1. The Lothal ivory scale has the smallest division of any known Bronze Age scale in the world.\n2. The precision of Harappan scales matches or exceeds contemporary scales in Mesopotamia and Egypt.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 2, "Both statements are correct. The Lothal ivory scale (1.7 mm divisions) represents the pinnacle of Bronze Age metrology, surpassing contemporary systems."),
    # 32. Dilmun weight standard
    ("With reference to Persian Gulf trade, consider the following statements:\n1. The weight system of the island of Dilmun (modern Bahrain) was identical to the Harappan standard.\n2. Dilmun acted as a transit port where Harappan weights were used for trade with Mesopotamia.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 2, "Both statements are correct. Dilmun adopted the Harappan weight standard, confirming the dominance of Harappan trade in the Persian Gulf."),
    # 33. Limestone weights
    ("Consider the following statements regarding large weights:\n1. Large weights used for weighing heavy agricultural bags were made of limestone or slate.\n2. These large weights were shaped into conical or ring-like stones with suspension holes.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 2, "Both statements are correct. Large weights were made of limestone/slate and were often ring-shaped or conical to allow ropes to pass through."),
    # 34. Decimal division higher values
    ("With reference to mathematical calculations in Harappa, consider the following statements:\n1. The binary system was used up to a ratio of 64.\n2. Ratios above 64 shifted to decimal values like 160, 320, and 6400 to ease bulk calculations.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 2, "Both statements are correct. The dual binary-decimal system optimized precision for small goods and simplified bulk trade bookkeeping."),
    # 35. Indus inch value
    ("Consider the following statements regarding the shell scale units:\n1. The 'Indus inch' is calculated to be approximately 1.32 inches.\n2. This unit of measurement corresponds closely to linear dimensions used in brick manufacturing.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 2, "Both statements are correct. The 'Indus inch' (33.5 mm) fits perfectly with the modular dimensions of building structures and brick sizes."),
    # 36. Weight system uniformity
    ("With reference to the geographical extent of the weight system, consider the following statements:\n1. The same weight standards were used at sites in Gujarat, Punjab, Sindh, and Haryana.\n2. Short-distance trade between villages did not utilize these weights and relied on arbitrary heap sizes.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 0, "Statement 1 is correct. Statement 2 is incorrect: standardized weights are found even in small rural Harappan sites, proving deep economic integration."),
    # 37. Agate vs Chert
    ("Consider the following statements regarding weight materials:\n1. Agate weights are usually smaller than chert weights, reflecting their use in weighing gold.\n2. Chert is a harder stone than agate and was preferred for large-scale warehouse weights.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 2, "Both statements are correct. Agate was used for delicate micro-weights, while tough Rohri chert was selected for larger cubical weights."),
    # 38. Terracotta balance pans
    ("With reference to archaeological finds at Mohenjo-daro, consider the following statements:\n1. Small clay pans with three or four holes on the edges represent balance pans.\n2. Thread fragments have been found preserved inside these holes due to contact with copper salts.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 2, "Both statements are correct. Terracotta pans with suspension holes are common, and mineralized thread remnants confirm they were suspended on scales."),
    # 39. Metric transition India
    ("Consider the following statements regarding traditional Indian weights:\n1. The traditional base weight unit of 'Tola' (11.66g) was derived from the Harappan base unit.\n2. The system of dividing 1 seer into 16 chhataks represents the survival of Harappan binary ratios.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 1, "Statement 2 is correct. Statement 1 is incorrect: the British Indian Tola (11.66g) was based on the silver rupee weight, whereas the 16-based division (seer to chhatak) represents the ancient binary legacy."),
    # 40. Conical weights
    ("With reference to non-cubical weights, consider the following statements:\n1. Conical weights with pierced tops were used as plumb-bobs to ensure vertical walls.\n2. Plumb-bobs show that Harappan architects had advanced knowledge of geometry and masonry alignment.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 2, "Both statements are correct. Conical weights with holes served a dual purpose, acting as heavy weights or as plumb-bobs to align walls vertically."),
    # 41. Bronze bar scale Harappa
    ("Consider the following statements regarding metal measurement scales:\n1. The bronze bar found at Harappa has a broken end, indicating it was once part of a larger ruler.\n2. Calibration lines on the bronze bar are spaced at intervals of 9.3 mm.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 2, "Both statements are correct. The bronze bar from Harappa is broken and calibrated at 9.3 mm intervals, showing a distinct metal ruler standard."),
    # 42. Interlocking bricks masonry
    ("With reference to Harappan construction techniques, consider the following statements:\n1. The standard brick ratio of 1:2:4 allows the length of a brick to equal twice its width, plus the mortar thickness.\n2. This exact mathematical relationship was essential for constructing water-tight reservoirs like the Great Bath.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 2, "Both statements are correct. The 1:2:4 ratio is mathematically optimized for interlocking layout and structural integrity in hydraulic projects like the Great Bath."),
    # 43. Agate weight manufacturing
    ("Consider the following statements regarding weight manufacturing:\n1. The manufacturing of weights required high skill, involving sawing, grinding, and polishing hard stones.\n2. Chert weights were polished using fine sand and water to achieve smooth faces.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 2, "Both statements are correct. Stone carving and polishing using sand abrasives was a specialized urban industry."),
    # 44. Shell scales Mohenjo-daro construction
    ("With reference to Mohenjo-daro, consider the following statements:\n1. The layout of streets and building blocks aligns with multiples of the shell scale unit.\n2. This alignment proves that municipal authorities mapped out the city grid using standardized rulers.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 2, "Both statements are correct. Spatial analysis of Mohenjo-daro's street grids matches the shell scale divisions, confirming structural pre-planning."),
    # 45. Mesopotamia weight difference
    ("Consider the following statements:\n1. The Mesopotamian weight system was sexagesimal (base-60), whereas the Harappan system was binary-decimal.\n2. Despite mathematical differences, the two systems interacted through commercial exchanges in the Persian Gulf.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 2, "Both statements are correct. The Mesopotamian base-60 system and Harappan binary-decimal metrology were bridged by international merchants at Gulf trade hubs."),
    # 46. Agate weights luxury
    ("With reference to high-value transactions, consider the following statements:\n1. Tiny agate and jasper weights are typically found in association with kiln workshops and furnace sites.\n2. They were used to measure copper and bronze scrap metal for melting.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 3, "Neither 1 nor 2 is correct. Tiny agate weights are found in gold-working and bead-making residential zones, not smelting furnace sites, as they were meant for precious luxury items."),
    # 47. Slate weights
    ("Consider the following statements regarding weight materials:\n1. Slate and limestone weights were used for heavier, bulk goods due to the abundance of these stones.\n2. Chert was reserved exclusively for weights weighing under 100 grams.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 0, "Statement 1 is correct. Statement 2 is incorrect: large chert cubical weights weighing several kilograms have also been excavated."),
    # 48. Brick sizes consistency
    ("With reference to regional brick sizes, consider the following statements:\n1. The actual physical dimensions of bricks were identical at Mohenjo-daro and Lothal.\n2. Minor variations in actual brick sizes existed, but the 1:2:4 ratio was strictly maintained.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 2, "Both statements are correct. Bricks varied slightly in physical dimensions (7x15x31 cm vs 7.5x15x30 cm), but the 1:2:4 ratio remained constant."),
    # 49. Public granaries weights
    ("Consider the following statements regarding public warehouses:\n1. Standardized weights were kept at the entrance of public granaries to verify tribute collection.\n2. Large ring-stones found near granaries likely served as heavy anchors for scales.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 2, "Both statements are correct. Large weights and scales were used at public facilities to verify grain and tribute inflows."),
    # 50. Metrological decay
    ("With reference to the collapse of the Harappan system, consider the following statements:\n1. The standardized weight system vanished along with the urban phase around 1900 BCE.\n2. The binary ratio of 16 was completely forgotten and had no influence on later historical Indian metrology.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 1, "Statement 1 is correct. Statement 2 is incorrect: the base-16 binary division survived for centuries as a traditional weight and coin ratio in historical India.")
]

# 50 Hindi Practice Questions (Multi-statement, UPSC standard)
raw_practice_hin = [
    # 1. Chert dominance
    ("सिंधु घाटी सभ्यता के बाट और माप के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. अधिकांश हड़प्पा कालीन बाट रोहरी चर्ट (Chert) पत्थर से बनाए जाते थे।\n2. मानक बाट घनाकार (cubical) होते थे और उन पर कोई निशान या सजावट नहीं होती थी।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 2, "दोनों कथन सही हैं। हड़प्पा के बाट मुख्य रूप से उच्च गुणवत्ता वाले चर्ट से बनते थे और वे पूरी तरह से सादे घनाकार पत्थर थे।"),
    # 2. Binary vs Decimal
    ("हड़प्पा बाटों की गणितीय संरचना के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. निचले मूल्य के बाट द्विआधारी (बाइनरी) प्रणाली पर आधारित थे, जो प्रत्येक चरण में दुगने होते थे।\n2. उच्च मूल्य के बाट दशमलव प्रणाली में बदल जाते थे।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 2, "दोनों कथन सही हैं। निम्न मान बाइनरी (1, 2, 4, 8, 16, 32, 64) और उच्च मान दशमलव (160, 200, 320, 640 आदि) थे।"),
    # 3. Base unit
    ("हड़प्पा वासियों के मानक बाट इकाई के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. बाटों में '16' अनुपात की इकाई सबसे आम और लोकप्रिय मानक थी।\n2. इस मूल इकाई का वास्तविक वजन लगभग 13.63 ग्राम था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 2, "दोनों कथन सही हैं। 16 अनुपात का बाट मुख्य मानक था जिसका वजन लगभग 13.63 ग्राम था।"),
    # 4. Brick proportions
    ("हड़प्पा सभ्यता के निर्माण सामग्री के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. धूप में सूखी और भट्टी में पकी ईंटों की मोटाई, चौड़ाई और लंबाई का एक निश्चित अनुपात 1:2:4 था।\n2. देहाती बस्तियों में इस अनुपात का पालन नहीं किया जाता था और वे अनियमित पत्थरों का उपयोग करते थे।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि 1:2:4 का अनुपात शहरों और छोटे देहाती गांवों दोनों में समान रूप से लागू था।"),
    # 5. Lothal ivory scale
    ("सिंधु घाटी सभ्यता में रैखिक मापन उपकरणों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. लोथल से हाथीदांत का एक पैमाना मिला है, जिस पर कांस्य युग का सबसे छोटा विभाजन दर्ज है।\n2. इस लोथल हाथीदांत पैमाने पर सबसे छोटा विभाजन लगभग 1.7 मिमी है।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 2, "दोनों कथन सही हैं। लोथल से प्राप्त हाथीदांत का पैमाना अत्यंत सटीक था और इस पर 1.7 मिमी का विभाजन अंकित था।"),
    # 6. Mohenjo-daro shell scale
    ("मोहनजोदड़ो से प्राप्त शंख के पैमाने के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. यह समुद्री शंख से बना था और इस पर 6.7 मिमी की विभाजन इकाइयां अंकित थीं।\n2. इन विभाजनों की एक श्रृंखला 'सिंधु इंच' (Indus inch) को परिभाषित करती थी, जो 33.5 मिमी के बराबर था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 2, "दोनों कथन सही हैं। मोहनजोदड़ो का शंख पैमाना 6.7 मिमी के अंतरालों पर विभाजित था, जो 33.5 मिमी के सिंधु इंच को दर्शाता है।"),
    # 7. Harappa bronze scale
    ("हड़प्पा सभ्यता से प्राप्त रैखिक पैमानों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. हड़प्पा की खुदाई से तांबे या कांसे की एक छड़ मिली है जिस पर मापन के निशान अंकित हैं।\n2. सिंधु घाटी से मिले धातु के किसी भी उपकरण पर कैलिब्रेशन (मापन) के निशान नहीं मिले हैं।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि हड़प्पा से प्राप्त धातु का पैमाना यह सिद्ध करता है कि धातु पर भी मापन निशान होते थे।"),
    # 8. Scale materials
    ("हड़प्पा वासियों द्वारा रैखिक पैमाने बनाने के लिए निम्नलिखित में से किस सामग्री का उपयोग किया जाता था?\n1. हाथीदांत\n2. शंख\n3. पकी मिट्टी (Terracotta)\n4. कांसा\nनीचे दिए गए कूट का प्रयोग कर सही उत्तर चुनिए:", ["1, 2 और 3 केवल", "1, 2 और 4 केवल", "2, 3 और 4 केवल", "1, 2, 3 और 4"], 3, "चारों सामग्रियां प्रयुक्त होती थीं: हाथीदांत (लोथल), शंख (मोहनजोदड़ो), मिट्टी (कालीबंगन) और कांसा (हड़प्पा)।"),
    # 9. Weight materials
    ("हड़प्पा कालीन बाटों के कच्चे माल के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. बाट केवल चर्ट पत्थर से बनाए जाते थे।\n2. कीमती मोतियों और सोने को तोलने के लिए अगेट, जैस्पर और कैल्सेडोनी के छोटे सटीक बाट भी बनाए जाते थे।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 1, "कथन 2 सही है। कथन 1 गलत है क्योंकि चर्ट मुख्य था, लेकिन अन्य कीमती पत्थरों का उपयोग भी छोटे बाटों में होता था।"),
    # 10. plain weights
    ("हड़प्पा बाटों की सौंदर्य विशेषताओं के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. अधिकांश बाटों पर हड़प्पा लिपि में संक्षिप्त चित्रलेख खुदे हुए मिले हैं।\n2. कुछ बाटों पर कूबड़ वाले बैल का सजीव नक्काशीदार चित्रण मिलता है।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 3, "दोनों कथन गलत हैं। हड़प्पा के बाट पूरी तरह से सादे थे और उन पर कोई लिपि या सजावट नहीं होती थी।"),
    # 11. Balance pans
    ("सिंधु घाटी सभ्यता में तौल तकनीक के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. खुदाई से तांबे, कांसे और मिट्टी के बने तराजू के पलड़े (balance pans) प्राप्त हुए हैं।\n2. मानक बाटों को लकड़ी की छड़ों से लटकाने के लिए जानवरों के चमड़े के पट्टों का उपयोग होता था।\nउपर्युक्त कथनों में से कौन-sa/se सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि पलड़ों को लटकाने के लिए सूती धागों या रस्सियों का उपयोग किया जाता था।"),
    # 12. Micro-weights
    ("हड़प्पा शहरों में छोटे पैमाने के तौल के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. मनके बनाने वाले कार्यशाला केंद्रों से 1 ग्राम से भी कम वजन के अत्यंत छोटे बाट मिले हैं।\n2. इन सूक्ष्म बाटों का उपयोग सोने की धूल, चांदी और कीमती पत्थरों को तोलने के लिए किया जाता था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 2, "दोनों कथन सही हैं। चन्हुदड़ो और लोथल के कारखानों से सोने और रत्नों को तोलने के लिए प्रयुक्त माइक्रो-बाट मिले हैं।"),
    # 13. Currency link
    ("भारत में हड़प्पा बाट प्रणाली की सांस्कृतिक निरंतरता के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. बाइनरी 16 का आधार भारत की पारंपरिक प्रणाली में जीवित रहा, जहाँ 1 रुपया = 16 आने होता था।\n2. वर्ष 1957 के दशमलवकरण कानून ने इस पारंपरिक व्यवस्था को पूरी तरह से प्रतिस्थापित कर दिया।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 2, "दोनों कथन सही हैं। 1 रुपया = 16 आने का ढांचा हड़प्पा काल की बाइनरी 16 की इकाई का प्राचीन सांस्कृतिक प्रभाव था।"),
    # 14. Rohri chert source
    ("हड़प्पा बाट निर्माण के कच्चे माल के व्यापार के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. सिंध में रोहरी की पहाड़ियाँ चर्ट पत्थर के खनन का मुख्य स्रोत थीं।\n2. तैयार बाटों का निर्माण सीधे रोहरी खदानों पर होता था और वहाँ से इन्हें पूरे क्षेत्र में भेजा जाता था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 2, "दोनों कथन सही हैं। रोहरी की पहाड़ियों में चर्ट के खदान और शिल्प कार्यशालाएँ थीं, जहाँ से बाटों को पूरे साम्राज्य में वितरित किया जाता था।"),
    # 15. Standard unit weight values
    ("हड़प्पा कालीन बाटों के वास्तविक वजनों के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. सबसे छोटी बाट इकाई का वजन लगभग 0.86 ग्राम था।\n2. सबसे भारी बाटों का वजन 10 किलोग्राम से अधिक था, जो थोक व्यापार के लिए प्रयुक्त होते थे।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 2, "दोनों कथन सही हैं। हड़प्पा बाटों की सीमा अत्यंत सूक्ष्म स्तर (0.86 ग्राम) से लेकर बड़े थोक मापों (10 किलोग्राम से अधिक) तक फैली थी।"),
    # 16. Mesopotamian trade weights
    ("हड़प्पा कालीन विदेशी व्यापार के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. मेसोपोटामिया के शहरों (जैसे उर) से हड़प्पा मानक के बाट प्राप्त हुए हैं।\n2. मेसोपोटामिया में व्यापार के लिए हड़प्पा के व्यापारियों ने मेसोपोटामिया की शेकेल (shekel) प्रणाली को अपना लिया था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि व्यापारियों ने अपने स्वतंत्र हड़प्पा मानक को विदेशी बंदरगाहों पर भी बनाए रखा।"),
    # 17. Spherical weights
    ("हड़प्पा स्थलों से प्राप्त बाटों के आकारों के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. सभी स्थलों पर घनाकार (cubical) बाट सबसे प्रमुख आकार श्रेणी का प्रतिनिधित्व करते हैं।\n2. पुरातात्विक साक्ष्यों में गोलाकार या बेलनाकार बाट पूरी तरह से अनुपस्थित हैं।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि मुख्य रूप से घनाकार आकार थे, लेकिन अल्प मात्रा में गोलाकार और शंक्वाकार बाट भी मिले हैं।"),
    # 18. Brick bonding
    ("हड़प्पा वास्तुकला के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. ईंटों के 1:2:4 अनुपात के कारण दीवारों में 'इंग्लिश बॉन्ड' की इंटरलॉकिंग चिनाई आसान हुई।\n2. एक ही शहर के विभिन्न घरों में ईंटों के आकार मनमाने ढंग से भिन्न होते थे।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि ईंटों के आकार अत्यधिक मानकीकृत और समान थे।"),
    # 19. Kalibangan clay scale
    ("कालीबंगन से प्राप्त मिट्टी के पैमाने के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. यह पैमाना मुख्य रूप से साधारण राजमिस्त्रियों और मकान निर्माताओं द्वारा उपयोग किया जाता था।\n2. इस पर कोई मापन अंकन नहीं है, जो दर्शाता है कि यह केवल सजावटी वस्तु थी।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि इस पर सटीक मापन के विभाजन चिह्न स्पष्ट रूप से खुदे हुए हैं।"),
    # 20. Imperial control
    ("हड़प्पा बाटों के प्रशासनिक नियंत्रण के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. बाटों की सार्वभौमिक एकरूपता मापन के नियमों को लागू करने वाली एक मजबूत केंद्रीय प्रशासनिक सत्ता को दर्शाती है।\n2. यह मानकीकरण बिना किसी केंद्रीय राज्य के, केवल व्यापारियों के स्व-नियमन (self-regulating guilds) द्वारा भी संभव था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 2, "दोनों कथन सही हैं। मानकीकरण केंद्रीय सत्ता या सुसंगठित व्यापारिक संघों द्वारा व्यापारिक सुगमता के लिए लागू किया जा सकता था।"),
    # 21. Brick size fortification
    ("हड़प्पा की इमारती ईंटों के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. रक्षा प्राचीरों और सार्वजनिक इमारतों के निर्माण में साधारण घरों की तुलना में बड़ी ईंटों का उपयोग होता था।\n2. बड़ी और छोटी दोनों प्रकार की ईंटों का आयाम अनुपात समान रूप से 1:2:4 था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 2, "दोनों कथन सही हैं। यद्यपि रक्षा प्राचीरों की ईंटें (10x20x40 सेमी) घरों की ईंटों (7x15x31 सेमी) से बड़ी थीं, लेकिन अनुपात 1:2:4 ही था।"),
    # 22. Domestic weights
    ("हड़प्पा शहरों में बाटों के वितरण के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. बाट केवल बड़े सार्वजनिक भवनों (जैसे अन्न भंडार) में ही पाए गए हैं।\n2. बाट साधारण घरों की खुदाई से भी मिले हैं, जो दर्शाता है कि घरेलू स्तर पर भी क्रय-विक्रय होता था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 1, "कथन 2 सही है। कथन 1 गलत है क्योंकि बाट साधारण घरों से भी प्रचुर मात्रा में मिले हैं।"),
    # 23. Balance pans materials
    ("हड़प्पा स्थलों से प्राप्त तराजू के पलड़ों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. कुछ तराजू के पलड़े तांबे या कांसे की पतली चादरों से बनाए गए थे।\n2. साधारण व्यापारियों के लिए पकी हुई मिट्टी (terracotta) के पलड़े भी मिले हैं।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 2, "दोनों कथन सही हैं। कीमती धातुओं के लिए धातु के तथा साधारण वस्तुओं के लिए मिट्टी के तराजू पलड़ों का उपयोग होता था।"),
    # 24. Linear scale units comparison
    ("सिंधु घाटी के रैखिक पैमानों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. मोहनजोदड़ो के शंख पैमाने और लोथल के हाथीदांत पैमाने की मूल मापन इकाई पूर्णतः एक समान थी।\n2. पैमानों के अंशांकन में मामूली अंतर स्थानीय शिल्प कलाओं में अलग-अलग उप-इकाइयों के उपयोग को दर्शाता है।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 1, "कथन 2 सही है। कथन 1 गलत है क्योंकि पैमानों की मूल इकाइयां मामूली रूप से भिन्न थीं।"),
    # 25. Late Harappan weight collapse
    ("उत्तर हड़प्पा काल के मापन बदलावों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. बाटों की मानकीकृत अखिल-हड़प्पा प्रणाली का पतन हो गया और स्थानीय मापन तरीके फिर से उभरे।\n2. हाथीदांत और शंख जैसे कीमती पदार्थों से बने सटीक पैमाने मिलना पूरी तरह से बंद हो गए।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 2, "दोनों कथन सही हैं। शहरी पतन और दूरस्थ व्यापार समाप्त होने से मानकीकृत बाट-माप प्रणाली का विघटन हो गया।"),
    # 26. Rohri chert export
    ("रोहरी चर्ट खदानों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. चर्ट पत्थरों को रोहरी खदान पर तराशकर बुनियादी आकार दिया जाता था और अंतिम पॉलिश शहरों में की जाती थी।\n2. मोहनजोदड़ो में बाटों के निर्माण की विशिष्ट कार्यशालाओं के साक्ष्य मिले हैं।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 2, "दोनों कथन सही हैं। कच्चे कोर को खदान स्थल पर तैयार किया जाता था और बारीक नक्काशी मोहनजोदड़ो जैसे शिल्प केंद्रों पर की जाती थी।"),
    # 27. Gold weighing
    ("हड़प्पा में कीमती धातुओं के तौल के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. बाइनरी प्रणाली के कारण 1 ग्राम से भी कम के अंशों का सटीक तौल संभव था।\n2. तराजू के पलड़े इतने संवेदनशील थे कि वे सोने की महीन धूल को भी तोल सकते थे।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 2, "दोनों कथन सही हैं। सूक्ष्म बाट और संवेदनशील तराजू सोने-चांदी के तौल के लिए अत्यधिक उपयुक्त थे।"),
    # 28. Standardized street widths
    ("हड़प्पा नगर नियोजन के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. सड़कों और गलियों की चौड़ाई एक निश्चित बुनियादी मापन इकाई के गुणकों में निर्धारित थी।\n2. सड़कों की चौड़ाई का अनुपात 1:2:3:4 के ग्रिड पैटर्न पर आधारित था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 2, "दोनों कथन सही हैं। सड़कें मानकीकृत चौड़ाई (1.8 मीटर, 3.6 मीटर, 7.2 मीटर) की ग्रिड व्यवस्था में विभाजित थीं।"),
    # 29. Weight markings
    ("हड़प्पा बाटों की विशेषताओं के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:\n1. किसी भी हड़प्पा बाट पर उनका मान दर्शाने वाला कोई संख्यात्मक अंकन नहीं मिला है।\n2. व्यापारी बाट के आकार, वजन और उसकी निश्चित चौड़ाई को देखकर ही उसका मान पहचानते थे।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 2, "दोनों कथन सही हैं। बाटों पर अंक या मूल्य अंकित नहीं थे; वे केवल आकार और मानक भार से ही पहचाने जाते थे।"),
    # 30. Agate weights
    ("बाटों के लिए प्रयुक्त होने वाले कीमती पत्थरों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. चित्तीदार या धारीदार अगेट को कीमती सामानों के व्यापार के लिए सुंदर छोटे बाटों में बदला जाता था।\n2. अगेट के बाट केवल राजकीय राजकोषीय भवनों से ही मिले हैं।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि अगेट के बाट घरों और साधारण दुकानों से भी मिले हैं।"),
    # 31. Harappan scale precision
    ("कांस्य युगीन मापन प्रणालियों के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. लोथल का हाथीदांत पैमाना कांस्य युग में विश्व की सबसे बारीक मापन विभाजन प्रणाली को दर्शाता है।\n2. हड़प्पा पैमानों की सटीकता मेसोपोटामिया और मिस्र के पैमानों के बराबर या उससे अधिक थी।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 2, "दोनों कथन सही हैं। लोथल का हाथीदांत पैमाना अत्यंत बारीक (1.7 मिमी) था, जो इसे समकालीन सभ्यताओं से अधिक उन्नत बनाता है।"),
    # 32. Dilmun weight standard
    ("फारस की खाड़ी के व्यापार के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. दिलमुन (आधुनिक बहरीन) की बाट प्रणाली हड़प्पा मानक के बिल्कुल अनुरूप थी।\n2. दिलमुन एक पारगमन बंदरगाह था जहाँ हड़प्पा के बाटों का उपयोग मेसोपोटामिया से विनिमय के लिए होता था।\nउपर्युक्त कथनों में से कौन-sa/se सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 2, "दोनों कथन सही हैं। खाड़ी व्यापार में हड़प्पा मापन प्रणाली इतनी प्रभावी थी कि दिलमुन ने भी इसी मानक को अपनाया था।"),
    # 33. Limestone weights
    ("बड़े बाटों के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. अनाज के भारी बोरों को तोलने के लिए चूना पत्थर या स्लेट के बड़े बाटों का उपयोग होता था।\n2. इन बड़े बाटों को शंक्वाकार या अंगूठी (ring-stone) के आकार में बनाया जाता था ताकि रस्सियाँ बांधी जा सकें।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 2, "दोनों कथन सही हैं। बड़े बाटों का आकार रिंग-स्टोन या शंक्वाकार था ताकि उन्हें रस्सियों की मदद से आसानी से उठाया जा सके।"),
    # 34. Decimal division higher values
    ("हड़प्पा में गणितीय गणनाओं के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. 64 अनुपात तक केवल बाइनरी मापों का उपयोग किया जाता था।\n2. थोक व्यापार की गणना आसान करने के लिए 64 से ऊपर 160, 320 और 6400 जैसी दशमलव इकाइयों का उपयोग होता था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 2, "दोनों कथन सही हैं। बाइनरी और दशमलव की यह दोहरी प्रणाली सूक्ष्म रत्नों और बड़े अनाज दोनों के बहीखाते के लिए बहुत अनुकूल थी।"),
    # 35. Indus inch value
    ("शंख पैमाने की इकाइयों के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. 'सिंधु इंच' (Indus inch) की लंबाई लगभग 1.32 इंच आंकी गई है।\n2. यह मापन इकाई हड़प्पा ईंटों के निर्माण और आयामों से पूरी तरह मेल खाती है।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 2, "दोनों कथन सही हैं। सिंधु इंच का मान इमारतों और ईंटों के मानकीकृत आयामों के साथ सटीक रूप से मेल खाता है।"),
    # 36. Weight system uniformity
    ("बाट प्रणाली के भौगोलिक विस्तार के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. गुजरात, पंजाब, सिंध और हरियाणा के सभी प्रमुख स्थलों पर एक ही बाट मानक लागू थे।\n2. गाँवों के भीतर होने वाले स्थानीय व्यापार में इन बाटों का उपयोग नहीं होता था और वे ढेरों के अनुमान पर निर्भर थे।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि छोटे ग्रामीण स्थलों से भी मानक बाट मिले हैं, जो व्यापक आर्थिक एकीकरण दर्शाते हैं।"),
    # 37. Agate vs Chert
    ("बाटों की सामग्री के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:\n1. अगेट (Agate) के बाट आकार में चर्ट के बाटों से छोटे होते थे, जो सोने के तौल में उनके उपयोग को दर्शाते हैं।\n2. चर्ट पत्थर अगेट की तुलना में अधिक कठोर होता था, इसलिए बड़े गोदामों के बाटों में इसे प्राथमिकता दी जाती थी।\nउपर्युक्त कथनों में से कौन-sa/se सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 2, "दोनों कथन सही हैं। सोने के लिए अगेट तथा अनाज आदि थोक तौल के लिए मजबूत रोहरी चर्ट के बाट बनाए जाते थे।"),
    # 38. Terracotta balance pans
    ("मोहनजोदड़ो से प्राप्त पुरातात्विक साक्ष्यों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. किनारों पर तीन या चार छेदों वाले मिट्टी के छोटे बर्तन तराजू के पलड़ों का प्रतिनिधित्व करते हैं।\n2. तांबे के लवणों के संपर्क के कारण इन छेदों के भीतर धागे के अवशेष सुरक्षित मिले हैं।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 2, "दोनों कथन सही हैं। मिट्टी के पलड़ों में धागे के अवशेष मिलना यह प्रमाणित करता है कि धागे की रस्सी से पलड़े लटके होते थे।"),
    # 39. Metric transition India
    ("पारंपरिक भारतीय बाटों के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:\n1. प्राचीन भारतीय तौल इकाई 'टोला' (11.66 ग्राम) सीधे हड़प्पा काल की मुख्य मानक इकाई से ली गई थी।\n2. 1 सेर को 16 छटाक में विभाजित करने की पारंपरिक प्रणाली हड़प्पा कालीन बाइनरी 16 के अनुपात की उत्तरजीविता है।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 1, "कथन 2 सही है। कथन 1 गलत है क्योंकि टोला ब्रिटिश काल के चांदी के रुपये के वजन पर आधारित था, जबकि 16 का विभाजन हड़प्पा विरासत है।"),
    # 40. Conical weights
    ("गैर-घनाकार बाटों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. शीर्ष पर छेद वाले शंक्वाकार पत्थरों का उपयोग राजमिस्त्री साहुल (plumb-bob) के रूप में करते थे।\n2. साहुल का उपयोग दर्शाता है कि हड़प्पा के निर्माताओं को ज्यामिति और दीवारों को सीधा खड़ा करने का उन्नत ज्ञान था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 2, "दोनों कथन सही हैं। साहुल का उपयोग दीवारों की सीध और निर्माण की ज्यामितीय सटीकता सुनिश्चित करने के लिए होता था।"),
    # 41. Bronze bar scale Harappa
    ("हड़प्पा से प्राप्त धातु के पैमाने के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:\n1. हड़प्पा से मिली कांसे की पट्टी का सिरा टूटा हुआ है, जो दर्शाता है कि यह मूल रूप से बड़ी पट्टी थी।\n2. इस कांसे की पट्टी पर मापन के निशान 9.3 मिमी के अंतरालों पर अंकित हैं।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 2, "दोनों कथन सही हैं। टूटी कांसे की पट्टी पर 9.3 मिमी के विभाजन चिह्न एक अलग मापन मानक की पुष्टि करते हैं।"),
    # 42. Interlocking bricks masonry
    ("हड़प्पा निर्माण तकनीकों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. ईंटों का 1:2:4 अनुपात यह सुनिश्चित करता था कि दो ईंटों की चौड़ाई एक ईंट की लंबाई के बराबर हो।\n2. यह गणितीय संबंध विशाल स्नानागार (Great Bath) जैसे जलाशयों को जल-रोधी (water-tight) बनाने के लिए आवश्यक था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 2, "दोनों कथन सही हैं। 1:2:4 अनुपात चिनाई की मजबूती और संरचनात्मक जल-रोधी क्षमता बढ़ाने के लिए गणितीय रूप से अनुकूल था।"),
    # 43. Agate weight manufacturing
    ("बाट निर्माण प्रक्रिया के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. पत्थरों को काटकर बाट बनाने के लिए आरी चलाने, घिसने और चमकाने के उच्च कौशल की आवश्यकता होती थी।\n2. चर्ट के बाटों को चिकना बनाने के लिए बारीक रेत और पानी से घिसा जाता था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 2, "दोनों कथन सही हैं। पत्थरों को आरी से काटना और रेत अपघर्षक (abrasive) से चमकाना एक विशेष शहरी उद्योग था।"),
    # 44. Shell scales Mohenjo-daro construction
    ("मोहनजोदड़ो के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. सड़कों और घरों के ब्लॉकों का खाका शंख पैमाने की इकाइयों के गुणकों में व्यवस्थित था।\n2. यह संरेखण साबित करता है कि नगर अधिकारियों ने मानकों पैमानों की मदद से पूरे शहर का लेआउट तैयार किया था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 2, "दोनों कथन सही हैं। शहर के निर्माण का ग्रिड पैटर्न मापन इकाइयों से मेल खाता है, जो नगर नियोजन की पूर्व-योजना को सिद्ध करता है।"),
    # 45. Mesopotamia weight difference
    ("मेसोपोटामिया और हड़प्पा मापन के अंतर के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. मेसोपोटामिया की बाट प्रणाली षष्ठदशमलव (base-60) थी, जबकि हड़प्पा प्रणाली बाइनरी-दशमलव थी।\n2. गणितीय अंतर के बावजूद, फारस की खाड़ी के व्यापार में दोनों प्रणालियों का सहज आदान-प्रदान होता था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 2, "दोनों कथन सही हैं। व्यापारिक केंद्रों पर दोनों मापन प्रणालियों के बीच व्यापारिक विनिमय दरें निर्धारित की गई थीं।"),
    # 46. Agate weights luxury
    ("कीमती धातुओं के विनिमय के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. अगेट और जैस्पर के छोटे बाट आमतौर पर तांबा गलाने की भट्टियों और धातु कारखानों से मिले हैं।\n2. इनका उपयोग पिघलाने के लिए तांबे और कांसे के टुकड़ों को तोलने के लिए किया जाता था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 3, "दोनों कथन गलत हैं। छोटे बाट सोने-चांदी और कीमती मनकों के घरों से मिले हैं, न कि धातु गलाने वाले भट्टी क्षेत्रों से।"),
    # 47. Slate weights
    ("बाटों के पत्थरों के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. चूना पत्थर और स्लेट के बड़े बाटों का उपयोग भारी सामानों के लिए प्रयुक्त होता था क्योंकि ये पत्थर आसानी से उपलब्ध थे।\n2. चर्ट पत्थर को केवल 100 ग्राम से कम वजन के बाट बनाने के लिए आरक्षित रखा जाता था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि चर्ट के बड़े-बड़े बाट भी मिले हैं जो कई किलोग्राम के होते थे।"),
    # 48. Brick sizes consistency
    ("क्षेत्रीय ईंटों के आकारों के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. मोहनजोदड़ो और लोथल से मिली ईंटों के भौतिक आकार पूरी तरह से एक समान मिलीमीटर में थे।\n2. ईंटों के वास्तविक आकारों में मामूली अंतर था, लेकिन 1:2:4 का अनुपात पूरी तरह से स्थिर बना रहा।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 2, "दोनों कथन सही हैं। यद्यपि ईंटों का भौतिक आकार मामूली रूप से भिन्न था (जैसे 7x15x31 सेमी या 7.5x15x30 सेमी), लेकिन 1:2:4 का अनुपात स्थिर था।"),
    # 49. Public granaries weights
    ("सार्वजनिक मापन के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:\n1. अन्नागारों के प्रवेश द्वारों पर कर के रूप में अनाज की आवक मापने के लिए राजकीय तराजू-बाट रखे जाते थे।\n2. अन्नागारों के समीप मिले बड़े रिंग-स्टोन्स भारी तराजू के आधार के रूप में कार्य करते थे।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 2, "दोनों कथन सही हैं। सार्वजनिक केंद्रों पर कर की वसूली की सटीकता सुनिश्चित करने के लिए बड़े बाटों और पलड़ों का उपयोग होता था।"),
    # 50. Metrological decay
    ("हड़प्पा बाट मानकीकरण के अंत के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. 1900 ईसा पूर्व के बाद नगरीय जीवन के पतन के साथ ही मानकीकृत बाट प्रणाली समाप्त हो गई।\n2. बाइनरी 16 का मान पूरी तरह से भुला दिया गया और बाद के भारतीय इतिहास के मापन पर इसका कोई प्रभाव नहीं पड़ा।\nउपर्युक्त कथनों में से कौन-sa/se सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 1, "कथन 1 सही है। कथन 2 गलत है क्योंकि बाइनरी 16 की यह इकाई ऐतिहासिक काल में भी सिक्कों और बाटों के अनुपात में जीवित रही।")
]

# 10 English Mock Questions (Multi-statement, UPSC standard)
mock_raw_eng = [
    ("With reference to the weight system of the Harappan Civilisation, consider the following statements:\n1. Standard weights were made of Rohri chert and were plain cubic structures.\n2. The system followed binary divisions in the lower ranges and decimal divisions in the higher ranges.\n3. None of the excavated weights bear script inscriptions or animal carvings.\nWhich of the statements given above are correct?", ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"], 3, "All three statements are correct. Weights were made of chert, were plain cubical stones, and followed a dual binary-decimal system with no carvings or script."),
    ("Consider the following statements regarding linear measurement tools in the Indus Valley:\n1. The Lothal scale was made of ivory and had the smallest division of 1.7 mm.\n2. The Mohenjo-daro scale was made of shell and defined the 'Indus inch' as 33.5 mm.\n3. Harappa yielded a bronze bar scale with clear calibrated divisions.\nWhich of the statements given above are correct?", ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"], 3, "All three statements are correct. Lothal had an ivory scale, Mohenjo-daro a shell scale, and Harappa had a bronze bar scale."),
    ("Which of the following pairs is/are correctly matched?\nArchaeological Site - Metrological Finding\n1. Lothal - Ivory scale with 1.7 mm divisions\n2. Mohenjo-daro - Marine shell scale defining the Indus inch\n3. Kalibangan - Broken terracotta scale with calibration lines\nSelect the correct answer using the code given below:", ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"], 3, "All three pairs are correctly matched. Lothal, Mohenjo-daro, and Kalibangan have yielded these respective measurement instruments."),
    ("With reference to construction standards in Harappan cities, consider the following statements:\n1. Both sun-dried and kiln-baked bricks adhered to a strict 1:2:4 ratio for thickness, width, and length.\n2. Standard sizes of bricks differed between domestic houses and public fortification walls.\n3. The 1:2:4 brick ratio enabled the interlocking header-and-stretcher English bond pattern.\nWhich of the statements given above are correct?", ["1 and 3 only", "2 and 3 only", "1 and 2 only", "1, 2 and 3"], 3, "All statements are correct. The ratio was always 1:2:4, domestic and fortification brick sizes differed, and they allowed interlocking construction."),
    ("Consider the following statements regarding the economic application of weights:\n1. Tiny agate and jasper weights weighing under 1 gram were used for gold and silver beads.\n2. Large ring-stones made of limestone were used as bulk weights at public granaries.\n3. Standard weights are found only in large municipal warehouses and not in domestic houses.\nWhich of the statements given above is/are correct?", ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"], 0, "Statements 1 and 2 are correct. Statement 3 is incorrect: weights are commonly found in ordinary domestic houses, showing decentralized retail trade."),
    ("With reference to international trade metrology, consider the following statements:\n1. Harappan-standard chert weights have been excavated in Mesopotamian cities like Ur.\n2. The island of Dilmun (Bahrain) adopted the Harappan weight standard for Gulf commerce.\nWhich of the statements given above is/are correct?", ["Both 1 and 2", "1 only", "2 only", "Neither 1 nor 2"], 0, "Both statements are correct. Harappan weights are found at Ur, and Dilmun adopted the Harappan weight standard, showing its trade dominance."),
    ("Consider the following statements:\n1. Balance scales consisted of thin copper/bronze pans suspended by cords from wooden beams.\n2. Terracotta balance pans have been found, representing low-cost scales used by small traders.\nWhich of the statements given above is/are correct?", ["Both 1 and 2", "1 only", "2 only", "Neither 1 nor 2"], 0, "Both statements are correct. Copper/bronze pans represent premium balances, while clay/terracotta pans show scales were accessible to smaller traders."),
    ("Which of the following materials were utilized for making weight standards in the Indus Valley Civilisation?\n1. Chert\n2. Agate\n3. Limestone\n4. Iron\nSelect the correct answer using the code given below:", ["1, 2 and 3 only", "1, 2 and 4 only", "2, 3 and 4 only", "1, 2, 3 and 4"], 0, "Chert, agate, and limestone were used. Iron (4) was completely unknown to the Bronze Age Harappans."),
    ("With reference to the historical legacy of Harappan metrology, consider the following statements:\n1. The binary base ratio of 16 survived as a currency and weight division (1 Rupee = 16 Annas) until 1957.\n2. The British Indian weight unit of Tola was mathematically identical to the Harappan base unit.\nWhich of the statements given above is/are correct?", ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], 0, "Statement 1 is correct. Statement 2 is incorrect: the Tola (11.66g) was based on the silver rupee weight, whereas the 16-based division (seer/chhatak or rupee/anna) represents the binary legacy."),
    ("Consider the following statements:\nStatement 1: The uniform distribution of Rohri chert weights across a million square kilometers suggests a highly organized administration or guild system.\nStatement 2: In the Late Harappan phase, this metrological uniformity dissolved into localized, regional standards.\nWhich of the statements given above is/are correct?", ["Both 1 and 2", "1 only", "2 only", "Neither 1 nor 2"], 0, "Both statements are correct. The vast standardization points to centralized administration or guilds, and this broke down into regional standards in the Late Harappan phase.")
]

# 10 Hindi Mock Questions
mock_raw_hin = [
    ("हड़प्पा सभ्यता की बाट प्रणाली के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. मानक बाट रोहरी चर्ट के बने सादे घनाकार पत्थर होते थे।\n2. यह प्रणाली निचले मूल्य में बाइनरी विभाजन और उच्च मूल्य में दशमलव विभाजन का पालन करती थी।\n3. खुदाई से प्राप्त किसी भी बाट पर कोई चित्रलेख लिपि या पशु चित्रण नहीं मिला है।\nउपर्युक्त कथनों में से कौन-से सही हैं?", ["1 और 2 केवल", "2 और 3 केवल", "1 और 3 केवल", "1, 2 और 3"], 3, "तीनों कथन सही हैं। बाट चर्ट पत्थर के, सादे घनाकार और दोहरी बाइनरी-दशमलव प्रणाली पर आधारित थे, जिन पर कोई सजावट नहीं थी।"),
    ("सिंधु घाटी में रैखिक मापन उपकरणों के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. लोथल का पैमाना हाथीदांत का था जिसका सबसे छोटा विभाजन 1.7 मिमी था।\n2. मोहनजोदड़ो का पैमाना शंख का था जो 33.5 मिमी के 'सिंधु इंच' को परिभाषित करता था।\n3. हड़प्पा से कांसे की मापन छड़ (bronze bar scale) मिली है जिस पर स्पष्ट विभाजन चिह्न हैं।\nउपर्युक्त कथनों में से कौन-से सही हैं?", ["1 और 2 केवल", "2 और 3 केवल", "1 और 3 केवल", "1, 2 और 3"], 3, "तीनों कथन सही हैं। लोथल से हाथीदांत, मोहनजोदड़ो से शंख और हड़प्पा से कांसे के पैमाने मिले हैं।"),
    ("निम्नलिखित में से कौन सा/से युग्म सही सुमेलित है/हैं?\nपुरातात्विक स्थल - मापन निष्कर्ष\n1. लोथल - 1.7 मिमी विभाजनों वाला हाथीदांत का पैमाना\n2. मोहनजोदड़ो - सिंधु इंच को परिभाषित करने वाला शंख का पैमाना\n3. कालीबंगन - मापन रेखाओं वाली मिट्टी की टूटी पट्टी (Terracotta scale)\nनीचे दिए गए कूट का प्रयोग कर सही उत्तर चुनिए:", ["1 और 2 केवल", "2 और 3 केवल", "1 और 3 केवल", "1, 2 और 3"], 3, "तीनों युग्म सही सुमेलित हैं। ये तीनों स्थलों से प्राप्त विशिष्ट रैखिक पैमाने हैं।"),
    ("हड़प्पा शहरों में निर्माण मानकों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. धूप में सूखी और भट्टी में पकी ईंटें मोटाई, चौड़ाई और लंबाई के लिए 1:2:4 के अनुपात का कड़ाई से पालन करती थीं।\n2. घरेलू मकानों और सुरक्षा प्राचीरों के लिए प्रयुक्त ईंटों के वास्तविक आकार भिन्न-भिन्न होते थे।\n3. ईंटों का 1:2:4 अनुपात दीवार चिनाई में इंटरलॉकिंग 'इंग्लिश बॉन्ड' पैटर्न की अनुमति देता था।\nउपर्युक्त कथनों में से कौन-से सही हैं?", ["1 और 3 केवल", "2 और 3 केवल", "1 और 2 केवल", "1, 2 और 3"], 3, "तीनों कथन सही हैं। अनुपात हमेशा 1:2:4 था, मकानों और किलेबंदी की ईंटों के आकार अलग थे, और इससे इंटरलॉकिंग संभव हुई।"),
    ("बाटों के आर्थिक अनुप्रयोग के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. 1 ग्राम से कम वजन के अगेट और जैस्पर के छोटे बाटों का उपयोग सोने-चांदी के मनकों को तोलने के लिए किया जाता था।\n2. चूना पत्थर के बड़े रिंग-स्टोन्स का उपयोग अन्नागारों में अनाज तोलने के लिए बड़े बाटों के रूप में होता था।\n3. मानक बाट केवल सार्वजनिक नगर गोदामों में ही पाए गए हैं, साधारण घरों में नहीं।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 और 2 केवल", "2 और 3 केवल", "1 और 3 केवल", "1, 2 और 3"], 0, "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि बाट साधारण घरों से भी मिले हैं, जो फुटकर व्यापार को दर्शाते हैं।"),
    ("अंतरराष्ट्रीय व्यापार मापन के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. मेसोपोटामिया के शहरों (जैसे उर) से हड़प्पा मानक के चर्ट बाट प्राप्त हुए हैं।\n2. फारस की खाड़ी के व्यापार के लिए दिलमुन (बहरीन) द्वीप ने हड़प्पा बाट मानक को अपनाया था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 और 2 दोनों", "1 केवल", "2 केवल", "न तो 1 न ही 2"], 0, "दोनों कथन सही हैं। हड़प्पा के बाट उर से मिले हैं और दिलमुन ने खाड़ी व्यापार के लिए इसी मानक को अपनाया था।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\n1. तराजू में लकड़ी की छड़ से लटके तांबे या कांसे के पलड़े शामिल होते थे।\n2. मिट्टी (terracotta) के पलड़े भी मिले हैं, जो छोटे खुदरा व्यापारियों द्वारा कम लागत वाले तराजू के रूप में प्रयुक्त होते थे।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 और 2 दोनों", "1 केवल", "2 केवल", "न तो 1 न ही 2"], 0, "दोनों कथन सही हैं। धातु के पलड़े प्रीमियम वर्ग के लिए और मिट्टी के पलड़े छोटे व्यापारियों के लिए थे।"),
    ("सिंधु घाटी सभ्यता में बाट बनाने के लिए निम्नलिखित में से किन सामग्रियों का उपयोग किया जाता था?\n1. चर्ट\n2. अगेट\n3. चूना पत्थर (Limestone)\n4. लोहा\nनीचे दिए गए कूट का प्रयोग कर सही उत्तर चुनिए:", ["1, 2 और 3 केवल", "1, 2 और 4 केवल", "2, 3 और 4 केवल", "1, 2, 3 और 4"], 0, "चर्ट, अगेट और चूना पत्थर प्रयुक्त होते थे। लोहा (4) कांस्य युग में अज्ञात था।"),
    ("हड़प्पा मापन प्रणाली की ऐतिहासिक विरासत के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. बाइनरी 16 का आधार भारत में 1957 तक सिक्कों और बाटों के विभाजन (1 रुपया = 16 आने) में जीवित रहा।\n2. ब्रिटिश भारत की वजन इकाई 'टोला' गणितीय रूप से हड़प्पा की मूल इकाई के बिल्कुल समान थी।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 न ही 2"], 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि टोला चांदी के सिक्के के वजन पर आधारित था, जबकि 16 का गुणात्मक विभाजन हड़प्पा विरासत है।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: 10 लाख वर्ग किमी क्षेत्र में रोहरी चर्ट बाटों का एक समान वितरण एक अत्यंत संगठित प्रशासन या गिल्ड प्रणाली की ओर संकेत करता है।\nकथन 2: उत्तर हड़प्पा काल में, यह मापन एकरूपता समाप्त हो गई और स्थानीय क्षेत्रीय मानकों का उदय हुआ।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 और 2 दोनों", "1 केवल", "2 केवल", "न तो 1 न ही 2"], 0, "दोनों कथन सही हैं। व्यापक मानकीकरण गिल्ड या प्रशासन को दर्शाता है और उत्तर हड़प्पा काल में इसका पतन हो गया।")
]

# Process and format the lists
practice_list_eng = []
for q, opts, ans, sol in raw_practice_eng:
    practice_list_eng.append({"q": q, "opts": opts, "ans": ans, "sol": sol})

practice_list_hin = []
for q, opts, ans, sol in raw_practice_hin:
    practice_list_hin.append({"q": q, "opts": opts, "ans": ans, "sol": sol})

mock_list_eng = []
for q, opts, ans, sol in mock_raw_eng:
    mock_list_eng.append({"q": q, "opts": opts, "ans": ans, "sol": sol})

mock_list_hin = []
for q, opts, ans, sol in mock_raw_hin:
    mock_list_hin.append({"q": q, "opts": opts, "ans": ans, "sol": sol})

eng_data["practiceQuestions"] = practice_list_eng
eng_data["mockTestQuestions"] = mock_list_eng

hin_data["practiceQuestions"] = practice_list_hin
hin_data["mockTestQuestions"] = mock_list_hin

# Write files
print(f"Writing English base content to {os.path.join(ENG_DIR, 'content.json')}")
with open(os.path.join(ENG_DIR, "content.json"), "w", encoding="utf-8") as f:
    json.dump(eng_data, f, ensure_ascii=False, indent=2)

print(f"Writing Hindi base content to {os.path.join(HIN_DIR, 'content.json')}")
with open(os.path.join(HIN_DIR, "content.json"), "w", encoding="utf-8") as f:
    json.dump(hin_data, f, ensure_ascii=False, indent=2)

print("Base build script executed successfully!")
