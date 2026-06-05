import json
import os

ENG_DIR = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\HarappanIndus-Valley-Civilisation\Domestication-of-animals"
HIN_DIR = os.path.join(ENG_DIR, "hi")
os.makedirs(HIN_DIR, exist_ok=True)

# English base structure
eng_data = {
    "breadcrumbs": {
        "parent": "UPSC Syllabus",
        "parentUrl": "/upsc/",
        "current": "Animal Domestication"
    },
    "hero": {
        "title": "Harappan Domestication of Animals & Wild Fauna",
        "description": "Analyse the pastoral economy, animal husbandry, wild fauna assemblages, hunting-fishing networks, and the horse remains debate of the Indus Valley Civilisation for UPSC GS-1."
    },
    "labels": {
        "clickToExpand": "Click to expand details",
        "mockIntro": {
            "title": "Interactive UPSC Mock Test",
            "description": "Test your knowledge on Harappan pastoralism, wild fauna hunting, and the horse remains debate at Surkotada. This timed mock test contains 10 high-yield, exam-standard questions with negative marking.",
            "startBtn": "Start Mock Test"
        },
        "mockPlay": {
            "prevBtn": "Previous Question",
            "nextBtn": "Next Question",
            "submitBtn": "Submit Test"
        }
    },
    "timeline": {
        "title": "Evolution of Harappan Faunal Interaction",
        "description": "Chronological development of pastoralism, hunting practices, and animal integration in Indus Valley society.",
        "cards": [
            {
                "period": "Early Harappan Pastoralism",
                "date": "c. 3300 BCE - 2600 BCE",
                "details": "Establishment of village-based animal husbandry (cattle, sheep, goat) alongside early agricultural expansion. Development of pastoral-nomadic seasonal networks in Gujarat and Baluchistan."
            },
            {
                "period": "Mature Harappan Exploitation",
                "date": "c. 2600 BCE - 1900 BCE",
                "details": "Intensive cattle breeding for urban traction (carts) and dairy. Advanced riverine and marine fishing networks (Makran coast dried fish trade). Prolific animal representation in seals, copper plates, and terracotta art."
            },
            {
                "period": "Late Harappan Shifts",
                "date": "c. 1900 BCE - 1300 BCE",
                "details": "Weakening monsoons and desiccation of pastures lead to ruralization. Increased reliance on local cattle and sheep breeding, and shift towards localized, opportunistic hunting/fishing."
            }
        ]
    },
    "mnemonics": {
        "title": "Mnemonics & Memory Hacks",
        "description": "Visual triggers to memorize key animals, sites, and debates for UPSC.",
        "items": [
            {
                "title": "Mnemonic 1: Domesticated Animal Suite",
                "phrase": "\"C-B-S-G-P-A-C (Cattle, Buffalo, Sheep, Goat, Pig, Ass, Camel)\"",
                "decryption": "Remember the primary domesticated suite: **C**attle, **B**uffalo, **S**heep, **G**oat, **P**ig, **A**ss, **C**amel."
            },
            {
                "title": "Mnemonic 2: The Horse Skeletal Remains Sites",
                "phrase": "\"Sur-Horse-Loth-Clay-Kali-Teeth (Surkotada, Lothal, Kalibangan)\"",
                "decryption": "Skeletal/clay evidence for horses: **Sur**kotada (bones/skeletons), **Loth**al (terracotta figurine), and **Kali**bangan (teeth remains)."
            },
            {
                "title": "Mnemonic 3: Non-depicted Animals on Seals",
                "phrase": "\"Cow-Horse-Camel (Never on Seals)\"",
                "decryption": "Despite their economic presence, the **Cow**, **Horse**, and **Camel** are NEVER depicted on Harappan seals."
            }
        ]
    },
    "flashcards": {
        "title": "Active Recall Flashcards",
        "description": "Test your memory on critical Harappan faunal discoveries and debates.",
        "items": [
            {
                "question": "Which animal is most frequently depicted on Mature Harappan seals?",
                "answer": "The mythical <strong>Unicorn</strong> (one-horned creature), followed by the humped bull (zebu), elephant, rhinoceros, tiger, and water buffalo.",
                "icon": "fa-stamp"
            },
            {
                "question": "Which major domesticate is economically vital but completely absent from seal iconography?",
                "answer": "The <strong>Cow</strong>. Humped bulls are highly prominent, but the female cow is never depicted on seals, possibly due to taboos or specific symbolic conventions.",
                "icon": "fa-cow"
            },
            {
                "question": "Where is the site of Surkotada located, and what is its faunal significance?",
                "answer": "Located in <strong>Gujarat</strong>. It has yielded disputed bone remains of the true horse (<em>Equus caballus</em>) from Mature-Late Harappan levels.",
                "icon": "fa-map-location-dot"
            },
            {
                "question": "What evidence exists for the domestic cat in the Indus Valley?",
                "answer": "At <strong>Chanhudaro</strong>, a baked brick was found with paw prints of a dog chasing a cat, confirming their presence in urban households.",
                "icon": "fa-cat"
            },
            {
                "question": "How did coastal Harappans utilize marine resources?",
                "answer": "They engaged in extensive sea fishing. Salted and dried marine fish were traded from coastal outposts in Baluchistan (Makran coast) to inland cities like Harappa.",
                "icon": "fa-fish"
            }
        ]
    },
    "deepDive": {
        "title": "Syllabus Core Study Notes (Deep-Dive)",
        "description": "Master the pastoral economy, wild fauna, and zooarchaeological debates of the Indus valley.",
        "sections": [
            {
                "title": "1. Pastoral Economy and Domesticated Animals",
                "content": """<p>Animal husbandry was a cornerstone of the Harappan subsistence economy, complementing agriculture and providing vital secondary products.</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-cow"></i> Core Domesticates & Economic Roles</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>Cattle (Bos indicus):</strong> The humped bull (zebu) was highly prized for pulling solid-wheeled carts and heavy wooden ploughshares. Cattle also provided milk, butter, and beef.</li>
      <li><strong>Small Ruminants:</strong> Sheep and goats were kept in large numbers for meat, milk, and wool. Pigs (Sus scrofa) were reared in urban dump yards for meat.</li>
      <li><strong>Beasts of Burden:</strong> Domestic asses (donkeys) and camels (bones found at Kalibangan) served as beasts of burden for overland desert trade routes.</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-cubes-stacked"></i> Symbolic Representations & Taboos</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>Bull Cult:</strong> The humped bull is realistically rendered in masterfully carved steatite seals and clay figurines, indicating its status as a symbol of power or fertility.</li>
      <li><strong>The Missing Cow:</strong> Intriguingly, the female cow is completely absent from seals, copper tablets, and terracotta art. This suggests the cow was not a central ritual icon, unlike in the Rigvedic period.</li>
      <li><strong>Domestic Pets:</strong> Dogs and cats were kept. Dogs are represented in terracotta toys (some with collars), and cat footprints are recorded.</li>
    </ul>
  </div>
</div>""",
                "masteryZone": []
            },
            {
                "title": "2. Wild Animals, Hunting, and Fishing",
                "content": """<p>Harappan society interacted extensively with wild fauna for supplementary nutrition, bone/ivory raw materials, and symbolic art.</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-paw"></i> Wild Fauna & Artistic Depictions</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>Rainforest Fauna:</strong> Tigers, elephants, rhinoceroses, and gaur (bison) are frequently depicted on seals, indicating that the Indus plain was wetter and more heavily forested than it is today.</li>
      <li><strong>The Missing Lion:</strong> The lion is extremely rare on seals (only depicted as a combat motif under Western Asian influence), whereas the tiger is a common motif, highlighting differences from Mesopotamian art.</li>
      <li><strong>Deer & Gharial:</strong> Various deer (sambar, chital, barasingha) and gharials (crocodiles) are depicted, showing familiarity with riverine and forest ecology.</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-hook"></i> Hunting, Fishing & Marine Trade</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>Hunting:</strong> Copper arrowheads and clay slingshots were used to hunt wild boar, deer, and birds. Ivory was harvested from elephants for crafting luxury pins, combs, and dice.</li>
      <li><strong>Fishing:</strong> Copper/bronze fish hooks have been excavated in large numbers at Mohenjo-daro, Harappa, and Lothal. Riverine catfish and marine fish were caught.</li>
      <li><strong>Makran Coast Fish Trade:</strong> Zooarchaeological studies of dried fish bones at Harappa show they were imported from the Makran coast, proving a structured inland-maritime trade network.</li>
    </ul>
  </div>
</div>""",
                "masteryZone": []
            },
            {
                "title": "3. Zooarchaeology and The Horse Controversy",
                "content": """<p>Scientific analysis of bone remains (osteology) helps reconstruct dietary habits, pastoral management, and long-standing historical debates.</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-dna"></i> Zooarchaeological Methods & Bone Data</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>Cut Marks:</strong> High concentrations of bones with cut marks near urban residential sectors prove meat processing and butchery.</li>
      <li><strong>Mortality Profiles:</strong> The slaughter of sheep/goats at young ages indicates meat production, whereas keeping cattle to old age indicates they were used for milk and traction.</li>
      <li><strong>Wild vs Domestic:</strong> Domesticated cattle, buffalo, sheep, and goat bones make up over 70% to 80% of faunal assemblages at most sites, proving that hunting was secondary.</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-horse-head"></i> The Surkotada Horse Controversy</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>Surkotada Bones:</strong> Excavated by J.P. Joshi, Mature-Late Harappan layers yielded bones claimed to be the true horse (<em>Equus caballus</em>). Archaeologist Sandor Bokonyi confirmed this identification.</li>
      <li><strong>The Counter-Argument:</strong> Other scholars, including Richard Meadow, argue these bones belong to the wild ass (khur/<em>Equus hemionus</em>) or domestic ass, which are native to Kutch.</li>
      <li><strong>Vedic Shift:</strong> The horse is central to Rigvedic culture but completely absent from Harappan seals and terracotta art (unlike the bull/unicorn). Therefore, it was not culturally integrated into Harappan society.</li>
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
            "<strong>Trap 1:</strong> Do not choose statements claiming that the cow was the most common animal depicted on seals. Humped bulls are common, but the cow is NEVER depicted on seals.",
            "<strong>Trap 2:</strong> Avoid options asserting that the horse was a central draft animal in Mature Harappan chariot warfare. Light-spoked wheeled chariots and horse-drawn warfare only appear in the Vedic/Post-Vedic period.",
            "<strong>Trap 3:</strong> Do not assume the lion was a popular icon. The lion is absent/rare on seals; the tiger is the dominant feline motif.",
            "<strong>Trap 4:</strong> Watch out for questions claiming camels were absent. Camel bones are documented at Kalibangan and were used for desert transport.",
            "<strong>Trap 5:</strong> Do not confuse domestic dog burials. Human burials with dogs are found at <strong>Ropar</strong> (Punjab), which is a key Neolithic-Harappan transition site."
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
        "current": "पशुओं का घरेलूकरण"
    },
    "hero": {
        "title": "हड़प्पा पशुओं का घरेलूकरण और जंगली जीव",
        "description": "यूपीएससी परीक्षा के लिए सिंधु घाटी सभ्यता की पशुपालन अर्थव्यवस्था, पशुपालन, जंगली जीवों, शिकार-मछली पकड़ने के जाल और सुरकोटदा में घोड़े के साक्ष्यों के विवाद का विश्लेषण।"
    },
    "labels": {
        "clickToExpand": "विवरण देखने के लिए क्लिक करें",
        "mockIntro": {
            "title": "इंटरैक्टिव यूपीएससी मॉक टेस्ट",
            "description": "हड़प्पा पशुपालन, जंगली जीवों के शिकार, और सुरकोटदा में घोड़े के अवशेषों के विवाद पर अपने ज्ञान का परीक्षण करें। इस समयबद्ध मॉक टेस्ट में नकारात्मक अंकन के साथ परीक्षा स्तर के 10 महत्वपूर्ण प्रश्न शामिल हैं।",
            "startBtn": "मॉक टेस्ट शुरू करें"
        },
        "mockPlay": {
            "prevBtn": "पिछला प्रश्न",
            "nextBtn": "अगला प्रश्न",
            "submitBtn": "परीक्षण जमा करें"
        }
    },
    "timeline": {
        "title": "हड़प्पा मानव-पशु संबंधों का विकास",
        "description": "सिंधु घाटी समाज में पशुपालन, शिकार प्रथाओं और अर्थव्यवस्था में पशुओं के जुड़ाव का कालानुक्रमिक विकास।",
        "cards": [
            {
                "period": "प्रारंभिक हड़प्पा पशुपालन",
                "date": "लगभग 3300 ईसा पूर्व - 2600 ईसा पूर्व",
                "details": "कृषि विस्तार के साथ ग्रामीण स्तर पर पशुपालन (बैल, भेड़, बकरी) की स्थापना। गुजरात और बलूचिस्तान में खानाबदोश-पशुपालकों के मौसमी प्रवास मार्गों का विकास।"
            },
            {
                "period": "परिपक्व हड़प्पा काल में पशु उपयोग",
                "date": "लगभग 2600 ईसा पूर्व - 1900 ईसा पूर्व",
                "details": "शहरी परिवहन (बैलगाड़ी) और डेयरी के लिए बैलों का बड़े पैमाने पर प्रजनन। मकरान तट से अंतर्देशीय शहरों तक सूखी मछली के व्यापार जैसी उन्नत मछली पकड़ने की प्रणालियों का विकास। मुहरों और मिट्टी के खिलौनों में पशुओं का प्रचुर चित्रण।"
            },
            {
                "period": "उत्तर हड़प्पा कालीन बदलाव",
                "date": "लगभग 1900 ईसा पूर्व - 1300 ईसा पूर्व",
                "details": "कमजोर मानसून और चरागाहों के सूखने के कारण शहरी व्यवस्था का ग्रामीणकरण। भेड़/बकरी पालन पर निर्भरता में वृद्धि और स्थानीय शिकार तथा मछली पकड़ने पर बल।"
            }
        ]
    },
    "mnemonics": {
        "title": "याद रखने के सूत्र और ट्रिक्स",
        "description": "परीक्षा के लिए महत्वपूर्ण पशुओं, स्थलों और बहसों को याद रखने के सूत्र।",
        "items": [
            {
                "title": "याद रखने का सूत्र 1: पालतू पशुओं की सूची",
                "phrase": "\"ब-भैं-भे-ब-सू-ग-ऊँ (बैल, भैंस, भेड़, बकरी, सूअर, गधा, ऊंट)\"",
                "decryption": "मुख्य पालतू पशु: **ब**ैल, **भैं**स, **भे**ड़, **ब**करी, **सू**अर, **ग**धा, **ऊँ**ट।"
            },
            {
                "title": "याद रखने का सूत्र 2: घोड़े के अस्थि अवशेष वाले स्थल",
                "phrase": "\"सुर-घोड़ा-लो-मिट्टी-काली-दांत (सुरकोटदा, लोथल, कालीबंगन)\"",
                "decryption": "घोड़े के प्रमाण: **सुर**कोटदा (हड्डियाँ/कंकाल), **लो**थल (मिट्टी की मूर्ति), **काली**बंगन (दांत के अवशेष)।"
            },
            {
                "title": "याद रखने का सूत्र 3: मुहरों पर अनुपस्थित पशु",
                "phrase": "\"गाय-घोड़ा-ऊंट (मुहरों पर कभी नहीं)\"",
                "decryption": "हड़प्पा मुहरों पर **गाय**, **घोड़ा** और **ऊंट** का चित्रण कभी नहीं किया गया है, हालांकि वे आर्थिक रूप से उपस्थित थे।"
            }
        ]
    },
    "flashcards": {
        "title": "सक्रिय स्मरण फ्लैशकार्ड (Active Recall)",
        "description": "हड़प्पा सभ्यता के पशु साक्ष्यों और ऐतिहासिक बहसों पर अपने ज्ञान का परीक्षण करें।",
        "items": [
            {
                "question": "हड़प्पा मुहरों पर सबसे अधिक चित्रित किया जाने वाला पशु कौन सा है?",
                "answer": "काल्पनिक जीव <strong>एक सींग वाला गेंडा (Unicorn)</strong>, इसके बाद कूबड़ वाला बैल (Zebu), हाथी, गैंडा, बाघ और भैंस का स्थान आता है।",
                "icon": "fa-stamp"
            },
            {
                "question": "वह कौन सा महत्वपूर्ण पालतू पशु है जो मुहरों पर बिल्कुल नहीं दर्शाया गया है?",
                "answer": "<strong>गाय</strong>। कूबड़ वाले बैल का अत्यधिक चित्रण मिलता है, लेकिन गाय का अंकन मुहरों पर पूर्णतः अनुपस्थित है, संभवतः किसी धार्मिक निषेध के कारण।",
                "icon": "fa-cow"
            },
            {
                "question": "सुरकोटदा कहाँ स्थित है और इसका पशु अवशेषों के मामले में क्या महत्व है?",
                "answer": "यह <strong>गुजरात</strong> में स्थित है। यहाँ परिपक्व-उत्तर हड़प्पा स्तरों से वास्तविक घोड़े (<em>Equus caballus</em>) की विवादास्पद हड्डियाँ मिली हैं।",
                "icon": "fa-map-location-dot"
            },
            {
                "question": "सिंधु घाटी में पालतू बिल्ली के क्या प्रमाण मिले हैं?",
                "answer": "<strong>चन्हुदड़ो</strong> से एक पकी ईंट मिली है जिस पर बिल्ली का पीछा करते हुए कुत्ते के पैरों के निशान अंकित हैं, जो घरों में इनके पालतू होने की पुष्टि करता है।",
                "icon": "fa-cat"
            },
            {
                "question": "तटीय हड़प्पा निवासियों ने समुद्री संसाधनों का उपयोग कैसे किया?",
                "answer": "उन्होंने बड़े पैमाने पर मछली पकड़ने का काम किया। बलूचिस्तान के मकरान तट से सूखी और नमकीन मछलियों को अंतर्देशीय शहरों (जैसे हड़प्पा) में व्यापार के लिए भेजा जाता था।",
                "icon": "fa-fish"
            }
        ]
    },
    "deepDive": {
        "title": "पाठ्यक्रम मुख्य अध्ययन नोट्स (विस्तृत)",
        "description": "सिंधु घाटी की पशुपालन अर्थव्यवस्था, जंगली जीवों और पुरातात्विक बहसों का अध्ययन करें।",
        "sections": [
            {
                "title": "1. पशुपालन अर्थव्यवस्था और पालतू जानवर",
                "content": """<p>पशुपालन हड़प्पा की निर्वाह अर्थव्यवस्था का एक महत्वपूर्ण स्तंभ था, जो कृषि का पूरक था और मूल्यवान द्वितीयक उत्पाद प्रदान करता था।</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-cow"></i> मुख्य पालतू पशु और आर्थिक भूमिका</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>मवेशी (Bos indicus):</strong> कूबड़ वाले बैल (zebu) को ठोस पहियों वाली गाड़ियों और लकड़ी के भारी हलों को खींचने के लिए पाला जाता था। मवेशियों से दूध, मक्खन और मांस भी मिलता था।</li>
      <li><strong>छोटे जुगाली करने वाले पशु:</strong> भेड़ और बकरियों को मांस, दूध और ऊन के लिए बड़ी संख्या में पाला जाता था। शहरों के कचरा क्षेत्रों में मांस के लिए सूअर (Sus scrofa) पाले जाते थे।</li>
      <li><strong>भार ढोने वाले पशु:</strong> घरेलू गधे और ऊंट (जिसके साक्ष्य कालीबंगन में मिले हैं) मरुस्थलीय व्यापारिक मार्गों पर सामान ढोने के काम आते थे।</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-cubes-stacked"></i> कलात्मक चित्रण और धार्मिक मान्यताएं</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>बैल की महत्ता:</strong> सेलखड़ी की मुहरों और मिट्टी की मूर्तियों में कूबड़ वाले बैल का सजीव चित्रण मिलता है, जो शक्ति या उर्वरता के प्रतीक के रूप में पूजनीय था।</li>
      <li><strong>गाय की अनुपस्थिति:</strong> आश्चर्यजनक रूप से, मुहरों, तांबे की पट्टियों और मिट्टी की कलाकृतियों पर मादा गाय का कोई चित्रण नहीं मिलता है। इससे पता चलता है कि वैदिक काल की तरह गाय यहाँ केंद्रीय धार्मिक प्रतीक नहीं थी।</li>
      <li><strong>पालतू कुत्ते-बिल्लियां:</strong> कुत्ते और बिल्लियां पाले जाते थे। कुत्तों को खिलौनों में गले में पट्टे के साथ दर्शाया गया है, और बिल्लियों के पंजों के निशान मिले हैं।</li>
    </ul>
  </div>
</div>""",
                "masteryZone": []
            },
            {
                "title": "2. जंगली जानवर, शिकार और मछली पकड़ना",
                "content": """<p>हड़प्पा समाज अतिरिक्त पोषण, हड्डियों/हाथीदांत की कच्चे माल के रूप में प्राप्ति और कलात्मक प्रेरणा के लिए जंगली जीवों से जुड़ा हुआ था।</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-paw"></i> जंगली जीव और उनका कलात्मक चित्रण</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>वर्षावन के जीव:</strong> मुहरों पर बाघ, हाथी, गैंडे और गौर (बाइसन) का बार-बार चित्रण यह दर्शाता है कि सिंधु क्षेत्र आज की तुलना में अधिक नम और सघन वनों से ढका था।</li>
      <li><strong>शेर की अनुपस्थिति:</strong> मुहरों पर शेर का चित्रण अत्यंत दुर्लभ है (केवल पश्चिमी एशियाई प्रभाव में ही लड़ाई के दृश्यों में मिलता है), जबकि बाघ का चित्रण आम है, जो मेसोपोटामिया की कला से भिन्न है।</li>
      <li><strong>हिरण और घड़ियाल:</strong> विभिन्न प्रकार के हिरण (सांभर, चीतल, बारहसिंगा) और घड़ियाल मुहरों पर अंकित हैं, जो नदीय और वन पारिस्थितिकी से उनकी पहचान दर्शाते हैं।</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-hook"></i> शिकार, मछली पकड़ना और समुद्री व्यापार</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>शिकार:</strong> जंगली सूअर, हिरण और पक्षियों का शिकार करने के लिए तांबे के बाणाग्र (arrowheads) और मिट्टी की गुलेल की गोलियों का उपयोग किया जाता था। हाथीदांत से विलासिता की वस्तुएं, कंघियां और पासे बनाए जाते थे।</li>
      <li><strong>मछली पकड़ना:</strong> मोहनजोदड़ो, हड़प्पा और लोथल से तांबे/कांसे के मछली पकड़ने के कांटे बड़ी संख्या में मिले हैं। नदियों की मल्ल (catfish) और समुद्री मछलियां पकड़ी जाती थीं।</li>
      <li><strong>मकरान तट से मछली का व्यापार:</strong> हड़प्पा में मिली समुद्री मछली की हड्डियों के विश्लेषण से पता चलता है कि उन्हें मकरान तट से सुखाकर आयात किया गया था, जो तटीय-अंतर्देशीय व्यापारिक नेटवर्क को सिद्ध करता है।</li>
    </ul>
  </div>
</div>""",
                "masteryZone": []
            },
            {
                "title": "3. प्राणि-पुरातत्व (Zooarchaeology) और घोड़े का विवाद",
                "content": """<p>पशुओं की हड्डियों के वैज्ञानिक विश्लेषण से भोजन की आदतों, चरागाह प्रबंधन और लंबे समय से चले आ रहे ऐतिहासिक विवादों को सुलझाने में मदद मिलती है।</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-dna"></i> वैज्ञानिक पद्धतियां और हड्डियों के साक्ष्य</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>काटने के निशान:</strong> आवासीय क्षेत्रों के पास मिली हड्डियों पर काटने (cut marks) के निशान मांस के प्रसंस्करण और कसाईखाने की उपस्थिति को सिद्ध करते हैं।</li>
      <li><strong>मृत्यु-आयु का प्रोफाइल:</strong> भेड़-बकरियों को कम उम्र में मारना मांस उत्पादन को दर्शाता है, जबकि मवेशियों को बुढ़ापे तक जीवित रखना दूध और गाड़ियां खींचने में उनके उपयोग की पुष्टि करता है।</li>
      <li><strong>पालतू बनाम जंगली:</strong> अधिकांश स्थलों पर 70% से 80% हड्डियाँ पालतू बैल, भैंस, भेड़ और बकरियों की हैं, जो दर्शाती हैं कि शिकार केवल एक सहायक गतिविधि थी।</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-horse-head"></i> सुरकोटदा में घोड़े का विवाद</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>सुरकोटदा के अवशेष:</strong> जे.पी. जोशी द्वारा उत्खनित गुजरात के सुरकोटदा स्थल के परिपक्व-उत्तर हड़प्पा स्तरों से घोड़े (<em>Equus caballus</em>) की हड्डियाँ मिलने का दावा किया गया, जिसे हंगरी के विशेषज्ञ सैंडोर बोकोनी ने सही ठहराया।</li>
      <li><strong>विपक्षी तर्क:</strong> रिचर्ड मीडो जैसे विद्वानों का तर्क है कि ये हड्डियाँ जंगली गधे (khur) या पालतू गधे की हैं, जो कच्छ के रण में आम हैं।</li>
      <li><strong>सांस्कृतिक अंतर:</strong> घोड़ा वैदिक संस्कृति का मुख्य हिस्सा था, लेकिन हड़प्पा की मुहरों और कलाकृतियों पर यह पूर्णतः गायब है, जिससे सिद्ध होता है कि यह हड़प्पा समाज का हिस्सा नहीं था।</li>
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
            "<strong>चेतावनी 1:</strong> परीक्षा में ऐसे कथनों से बचें जो यह दावा करते हैं कि मुहरों पर सबसे आम जानवर गाय थी। मुहरों पर बैल आम हैं, लेकिन गाय मुहरों पर कभी नहीं दर्शाई गई है।",
            "<strong>चेतावनी 2:</strong> उन विकल्पों से बचें जो यह कहते हैं कि हड़प्पा काल में रथ युद्ध के लिए घोड़े का व्यापक उपयोग होता था। पहियों वाले रथ और घोड़े से लड़े जाने वाले युद्ध वैदिक काल में ही दिखाई देते हैं।",
            "<strong>चेतावनी 3:</strong> सिंह (शेर) को एक लोकप्रिय हड़प्पा प्रतीक न समझें। मुहरों पर शेर अनुपस्थित या अत्यंत दुर्लभ है; बाघ ही मुख्य बिल्ली प्रजाति का जानवर है।",
            "<strong>चेतावनी 4:</strong> इस बात पर ध्यान दें कि हड़प्पा काल में ऊंट मौजूद थे। कालीबंगन से ऊंट की हड्डियाँ मिली हैं, और वे मरुस्थलीय परिवहन के काम आते थे।",
            "<strong>चेतावनी 5:</strong> मनुष्य के साथ कुत्ते को दफनाने के साक्ष्य पंजाब के <strong>रोपण</strong> (Ropar) से मिले हैं, जो नवपाषाण-हड़प्पा संक्रमण का एक प्रमुख स्थल है।"
        ]
    },
    "practiceQuestions": [],
    "mockTestQuestions": []
}

# 50 English Practice Questions
raw_practice_eng = [
    ('With reference to the pastoral economy of the Indus Valley Civilisation, consider the following statements:\n1. Cattle (zebu) bones represent the largest percentage of faunal remains at almost all sites.\n2. Sheep and goats were reared together primarily for milk and wool.\nWhich of the statements given above is/are correct?', ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 2, 'Both statements are correct. Cattle (zebu) bones are the most dominant faunal remains (50-60%), and sheep and goats were reared in mixed herds for milk, meat, and wool.'),
    ('Consider the following statements regarding the cow in Harappan culture:\n1. Humped bulls are highly prominent on steatite administrative seals.\n2. The female cow is depicted alongside the humped bull on several seals from Mohenjo-daro.\nWhich of the statements given above is/are correct?', ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 0, 'Statement 1 is correct. Statement 2 is incorrect: the female cow is completely absent from all known Harappan seals and iconography, which is a major contrast to the Rigvedic period.'),
    ('With reference to the beasts of burden in the Harappan civilization, consider the following statements:\n1. Camel bones showing adaptation to dry climates have been excavated in significant quantities at Kalibangan.\n2. Camels were the primary source of traction for ploughing agricultural fields in Punjab.\nWhich of the statements given above is/are correct?', ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 0, 'Statement 1 is correct. Statement 2 is incorrect: humped oxen (bulls) were the primary draft animals used for agricultural plough traction, not camels.'),
    ('Consider the following statements regarding burial practices in Harappan cities:\n1. A human burial containing a domestic dog buried alongside the deceased was excavated at Ropar.\n2. The practice of burying domestic pets with their owners was common across all major Harappan cemeteries.\nWhich of the statements given above is/are correct?', ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 0, 'Statement 1 is correct. Statement 2 is incorrect: the dog-human co-burial is unique to Ropar in Punjab and not found in other Harappan cemeteries.'),
    ('With reference to domestic pets in the Indus Valley Civilisation, consider the following statements:\n1. A wet clay brick with paw prints of a dog chasing a cat was discovered at Chanhudaro.\n2. Terracotta toys of dogs showing collar bands suggest they were kept as domestic pets.\nWhich of the statements given above is/are correct?', ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 2, 'Both statements are correct. Chanhudaro yielded a brick with paw prints showing a dog chasing a cat, and terracotta dog toys from Harappa show collars, proving their pet status.'),
    ('Consider the following statements regarding the humped cattle of the Indus Valley Civilisation:\n1. Humped cattle are scientifically classified as Bos indicus.\n2. The humped bull or zebu is carved with great detail and artistic realism on administrative seals.\nWhich of the statements given above is/are correct?', ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 2, 'Both statements are correct. Humped cattle are Bos indicus and were carved with extreme realism on steatite seals.'),
    ('With reference to overland trade networks of the Harappans, consider the following statements:\n1. Domestic asses (donkeys) were used as beasts of burden for transport across rocky terrains.\n2. Camel remains at Kalibangan suggest camels were utilized for desert trade routes.\nWhich of the statements given above is/are correct?', ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 2, 'Both statements are correct. Donkeys and camels served as pack animals for overland trade in arid and rocky regions (Baluchistan/Rajasthan).'),
    ('Consider the following statements regarding Harappan diets and zooarchaeological remains:\n1. High concentrations of domestic pig (Sus scrofa) bones are found in refuse heaps near urban residential sectors.\n2. Pigs were kept in urban dump yards, feeding on organic waste and providing a source of meat.\nWhich of the statements given above is/are correct?', ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 2, 'Both statements are correct. Pig bones are common in urban refuse middens, indicating pigs consumed organic waste and were slaughtered for meat.'),
    ('With reference to Harappan sheep and goat herding, consider the following statements:\n1. Pastoral groups reared sheep and goats together in mixed herds to exploit complementary resources.\n2. Sheep were sheared for wool, whereas goats were primarily kept for milk and meat.\nWhich of the statements given above is/are correct?', ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 2, 'Both statements are correct. Sheep and goats were kept together; sheep provided wool, and both provided milk and meat.'),
    ('Consider the following statements regarding terracotta figurines in Harappan sites:\n1. Toy figurines representing dogs have been excavated showing collar bands.\n2. Terracotta models of horses showing spoked-wheeled chariots have been found at Mohenjo-daro.\nWhich of the statements given above is/are correct?', ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 0, 'Statement 1 is correct. Statement 2 is incorrect: horses and spoked-wheeled chariots are completely absent from Harappan terracotta art.'),
    ('With reference to felines depicted in Mature Harappan art, consider the following statements:\n1. The tiger is a common motif on seals, often shown in scenes with men in trees.\n2. The Asiatic lion is frequently depicted on seals as a symbol of royal power.\nWhich of the statements given above is/are correct?', ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 0, 'Statement 1 is correct. Statement 2 is incorrect: the lion is absent or extremely rare on seals, unlike the tiger which is highly common.'),
    ("Which of the following wild animals are depicted on the famous 'Pashupati Seal' of Mohenjo-daro?\n1. Tiger\n2. Elephant\n3. Rhinoceros\n4. Lion\nSelect the correct answer using the code given below:", ['1, 2 and 3 only', '1, 2 and 4 only', '2, 3 and 4 only', '1, 2, 3 and 4'], 0, 'The Pashupati seal depicts a tiger, an elephant, a rhinoceros, and a buffalo surrounding the deity, with two deer below the throne. The lion is absent.'),
    ('Consider the following statements regarding the representation of aquatic fauna in Harappan art:\n1. The gharial or fish-eating crocodile is commonly depicted on pottery, amulets, and seals.\n2. Marine fish and tortoises are depicted on painted pottery at coastal sites like Lothal.\nWhich of the statements given above is/are correct?', ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 2, 'Both statements are correct. Gharials represent riverine fauna on seals/pottery, and marine species are common in coastal Lothal art.'),
    ('With reference to the maritime trade of the Harappans, consider the following statements:\n1. Dried and salted marine fish were traded from coastal outposts on the Makran coast to inland cities like Harappa.\n2. Fish bone assemblages at Harappa include species native only to the Arabian Sea.\nWhich of the statements given above is/are correct?', ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 2, 'Both statements are correct. Zooarchaeological analysis of fish bones at Harappa shows they include marine species traded from the Makran coast (800 km away).'),
    ('Consider the following statements regarding fishing technology in Harappan sites:\n1. Large numbers of copper and bronze fish hooks have been excavated at Mohenjo-daro and Lothal.\n2. The Harappans relied exclusively on bone hooks due to the scarcity of metals.\nWhich of the statements given above is/are correct?', ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 0, 'Statement 1 is correct. Statement 2 is incorrect: metal hooks of copper and bronze were widely used for fishing in both rivers and seas.'),
    ('With reference to the manufacturing of shell objects, consider the following statements:\n1. Coastal sites like Nageshwar and Balakot specialized in the procurement and carving of marine chank shells.\n2. Marine shell bangles, ladles, and inlay work were traded from coastal workshops to inland cities.\nWhich of the statements given above is/are correct?', ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 2, 'Both statements are correct. Nageshwar and Balakot were dedicated shell-craft centers that traded finished goods (bangles, ladles) inland.'),
    ('Consider the following statements regarding ivory utilization in the Indus Valley Civilisation:\n1. Lothal has yielded ivory workshop remains, including unworked elephant tusks and waste flakes.\n2. Ivory was exported from the Indus Valley (Meluhha) to Mesopotamia as a luxury trade commodity.\nWhich of the statements given above is/are correct?', ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 2, 'Both statements are correct. Lothal has an ivory workshop, and Akkadian texts list ivory from Meluhha (Indus valley) as a premium import.'),
    ('With reference to Harappan hunting practices, consider the following statements:\n1. Copper arrowheads and clay slingshots were used to hunt wild boar, deer, and birds.\n2. Wild animal bones represent the main source of daily protein in large urban centers.\nWhich of the statements given above is/are correct?', ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 0, 'Statement 1 is correct. Statement 2 is incorrect: domesticated livestock bones make up over 80% of urban assemblages; hunting wild game was secondary.'),
    ('Consider the following statements regarding zooarchaeological analysis of animal bones:\n1. Sharp cut marks and scrapes at joints indicate butchery and meat processing for human consumption.\n2. Charring or burning of bones shows they were roasted or cooked.\nWhich of the statements given above is/are correct?', ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 2, 'Both statements are correct. Cut marks and charring are direct osteological evidence of slaughtering and cooking animals for food.'),
    ('With reference to the economic use of cattle, consider the following statements:\n1. Zooarchaeological mortality profiles showing cattle living to old age suggest they were used for milk and agricultural traction.\n2. Cattle were slaughtered uniformly at very young ages, indicating they were raised exclusively for beef.\nWhich of the statements given above is/are correct?', ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 0, 'Statement 1 is correct. Keeping cattle until old age proves they were valued for their milk and labor (pulling carts/ploughs) rather than quick meat.'),
    ('Consider the following statements regarding the herding of sheep in Harappan cities:\n1. Sheep were kept to mature ages to harvest maximum wool yields over several years.\n2. Woven wool and cotton textiles were primary industrial exports of the Harappans.\nWhich of the statements given above is/are correct?', ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 2, 'Both statements are correct. Zooarchaeological age profiles confirm sheep were kept to mature ages to shear wool, which was woven into textiles for trade.'),
    ('With reference to the site of Surkotada in Gujarat, consider the following statements:\n1. J.P. Joshi excavated Mature-Late Harappan layers that yielded bones claimed to be the true horse.\n2. Hungarian zooarchaeologist Sandor Bokonyi confirmed the identification of these bones as Equus caballus.\nWhich of the statements given above is/are correct?', ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 2, 'Both statements are correct. J.P. Joshi excavated horse bones at Surkotada, and Bokonyi verified them as belonging to the true horse (Equus caballus).'),
    ('Consider the following statements regarding the counter-arguments in the horse controversy:\n1. Scholar Richard Meadow argues that the Surkotada bones belong to the wild ass (khur) or domestic donkey.\n2. The wild ass (Equus hemionus) is native to the Rann of Kutch and shares skeletal similarities with the horse.\nWhich of the statements given above is/are correct?', ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 2, 'Both statements are correct. Meadow contested the horse claim, asserting the bones belong to the native wild ass (khur), which looks similar osteologically.'),
    ('With reference to the cultural role of the horse, consider the following statements:\n1. The horse is completely absent from all Mature Harappan seals and terracotta art.\n2. The horse holds a central religious and economic place in Rigvedic culture, unlike in Harappan iconography.\nWhich of the statements given above is/are correct?', ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 2, "Both statements are correct. The horse's absence on seals shows it was not culturally integrated in Harappa, representing a sharp shift from Vedic culture."),
    ('Consider the following statements regarding the environmental changes in the Late Harappan phase:\n1. Disappearance of water-loving fauna like rhinoceros and elephant bones from refuse dumps indicates climatic drying.\n2. Late Harappan assemblages show an increase in dry-adapted sheep and goat remains.\nWhich of the statements given above is/are correct?', ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 2, 'Both statements are correct. The shift in bone assemblages from wet-climate species to dry-adapted ruminants confirms environmental desiccation around 1900 BCE.'),
    ('With reference to pastoral nomadic groups in Gujarat, consider the following statements:\n1. They engaged in seasonal migrations (transhumance) between dry plains and wet hills to secure pastures.\n2. They supplied urban Harappan centers with milk, wool, hides, and draft animals in exchange for grains and metal tools.\nWhich of the statements given above is/are correct?', ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 2, 'Both statements are correct. Seasonal pastoral migration (transhumance) was vital for herd survival and maintained symbiotic trade with cities.'),
    ('Consider the following statements regarding zooarchaeological statistics at Harappan sites:\n1. Domesticated cattle, buffalo, sheep, and goat bones constitute over 70% to 80% of faunal remains at most urban sites.\n2. Bones of wild deer and antelope are completely absent from all urban kitchen middens.\nWhich of the statements given above is/are correct?', ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 1, 'Statement 1 is correct. Statement 2 is incorrect: wild deer bones are present, indicating supplementary hunting, though it was minor.'),
    ('With reference to coastal subsistence strategies at Balakot, consider the following statements:\n1. Excavations show high consumption of marine fish and sea turtles, indicating a marine-dominant diet.\n2. The site was a major center for herding humped camels for maritime shipment.\nWhich of the statements given above is/are correct?', ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 1, 'Statement 1 is correct. Statement 2 is incorrect: Balakot was a coastal shell-craft and sea-fishing center, not a camel herding outpost.'),
    ('Consider the following statements regarding transportation in the Indus Valley Civilisation:\n1. Terracotta toy models of carts show they were designed to be pulled by humped oxen.\n2. These toy models feature solid, spoke-less clay wheels matching track ruts found in streets.\nWhich of the statements given above is/are correct?', ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 2, 'Both statements are correct. Bullock carts with solid hubless wheels were the primary bulk overland transport system, as confirmed by toys and ruts.'),
    ('With reference to Harappan glyptic art, consider the following statements:\n1. Seals were carved out of soft talcose rock called steatite and then fired to glaze them.\n2. The humped bull or zebu was the single most common animal depicted on seals.\nWhich of the statements given above is/are correct?', ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 1, 'Statement 1 is correct. Statement 2 is incorrect: the mythological one-horned unicorn was the most common motif, not the humped bull.'),
    ('Consider the following statements regarding wild fauna remains in Harappan refuse heaps:\n1. Bones of rhinoceros, wild boar, and various deer species indicate supplementary hunting.\n2. Wild birds like peacocks, jungle fowl, and ducks were also hunted for food.\nWhich of the statements given above is/are correct?', ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 2, 'Both statements are correct. Refuse piles yield bones of wild boar, deer, and birds, proving that hunting supplemented agricultural diets.'),
    ('With reference to Harappan seal iconography, consider the following statements:\n1. Seals sometimes depict composite creatures, such as a three-headed beast combining a bull, unicorn, and ibex.\n2. Human-faced quadrupeds with unicorn horns suggest complex mythological and religious beliefs.\nWhich of the statements given above is/are correct?', ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 2, 'Both statements are correct. Composite and chimerical creatures are highly common on seals, indicating administrative or mythological icons.'),
    ('Consider the following statements regarding kitchen refuse at Harappa:\n1. Heavy concentrations of river turtle shells with burn marks indicate they were boiled and consumed.\n2. Turtles were kept in domestic ponds as sacred household guardians and never eaten.\nWhich of the statements given above is/are correct?', ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 1, 'Statement 1 is correct. Statement 2 is incorrect: burned shell fragments prove turtles were harvested from rivers and cooked for food.'),
    ('With reference to dental remains at Kalibangan, consider the following statements:\n1. Excavations yielded jaw fragments and teeth belonging to the Equidae (horse/ass) family.\n2. These dental remains conclusively prove that the true domestic horse was used for agriculture in Rajasthan.\nWhich of the statements given above is/are correct?', ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 1, 'Statement 1 is correct. Statement 2 is incorrect: these teeth are highly debated and cannot conclusively differentiate between horses and asses.'),
    ('Consider the following statements regarding household pets in Harappan cities:\n1. Terracotta figurines show dogs with collars, proving they were domesticated for guarding and companionship.\n2. Domestic cats are represented by terracotta figurines showing cats catching mice.\nWhich of the statements given above is/are correct?', ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 1, 'Statement 1 is correct. Statement 2 is incorrect: cats are proven by brick paw prints (Chanhudaro), but cat toy figurines are extremely rare or absent.'),
    ('With reference to harvesting tools in Harappan fields, consider the following statements:\n1. Chert blades set in wooden handles were the primary tools used as sickles to harvest grains.\n2. Bronze and copper sickles were mass-produced in urban factories to harvest rabi crops.\nWhich of the statements given above is/are correct?', ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 1, 'Statement 1 is correct. Statement 2 is incorrect: metal sickles were extremely rare, as chert (stone) was the primary material for sickles.'),
    ('Consider the following statements regarding the water buffalo (Bubalus bubalis) in Harappa:\n1. Buffaloes were domesticated and used for milk, meat, and traction in wet alluvial soils.\n2. Buffalo bones show high concentrations in water-logged coastal outposts of Gujarat.\nWhich of the statements given above is/are correct?', ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 2, 'Both statements are correct. The water buffalo was domesticated and exploited for dairy, meat, and traction in wet fields.'),
    ('With reference to wild birds in Harappan art, consider the following statements:\n1. The peacock is frequently painted on pottery and modeled as terracotta figurines, showing its symbolic value.\n2. Peacocks are depicted on seals as draft birds pulling the chariots of deities.\nWhich of the statements given above is/are correct?', ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 1, 'Statement 1 is correct. Statement 2 is incorrect: peacocks were never depicted as draft birds pulling chariots (chariots themselves were unknown).'),
    ("Consider the following statements regarding cuneiform inscriptions of Mesopotamia:\n1. Tablets list ivory items imported from the land of 'Meluhha', which is identified as the Indus Valley.\n2. Raw elephant tusks were shipped via Persian Gulf transit ports to Mesopotamian workshops.\nWhich of the statements given above is/are correct?", ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 2, 'Both statements are correct. Mesopotamian records list ivory objects and tusks imported from Meluhha (the Indus valley) via the Gulf.'),
    ('With reference to livestock management in rural Gujarat, consider the following statements:\n1. Circular stone and brick enclosures found at rural sites functioned as corrals to pen sheep, goats, or cattle at night.\n2. These enclosures were built to protect domesticated herds from wild predators like tigers and leopards.\nWhich of the statements given above is/are correct?', ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 2, 'Both statements are correct. Circular corrals protect livestock from nocturnal predators, representing structured rural pastoral management.'),
    ('Consider the following statements regarding Harappan fishing gear:\n1. Fish hooks excavated at riverine and coastal sites were made of copper and bronze.\n2. Iron fish hooks were widely traded from Gangetic sites during the Mature Harappan phase.\nWhich of the statements given above is/are correct?', ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 1, 'Statement 1 is correct. Statement 2 is incorrect: iron was completely unknown to the Harappans, who relied on copper/bronze for metal hooks.'),
    ("With reference to ritual evidence at Harappan sites, consider the following statements:\n1. Clay altars at Kalibangan containing animal bones and ash suggest cattle sacrifices.\n2. The 'Pashupati Seal' depicts a deity performing a horse sacrifice.\nWhich of the statements given above is/are correct?", ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 1, 'Statement 1 is correct. Statement 2 is incorrect: the Pashupati seal shows a seated yogic figure surrounded by wild animals, not a sacrifice scene.'),
    ('Consider the following statements regarding the contrast between Harappan and Rigvedic societies:\n1. Harappan seals are dominated by bulls and unicorns, while Rigvedic culture is highly horse-centric.\n2. Harappan civilization was urban and commercial, while Rigvedic society was pastoral and rural.\nWhich of the statements given above is/are correct?', ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 2, 'Both statements are correct. These represent key differences in economy, settlement types, and faunal focus between the two periods.'),
    ('With reference to the wild ass (khur) of Kutch, consider the following statements:\n1. The scientific name of the wild ass is Equus hemionus.\n2. Its bones are osteologically very similar to the true horse, causing identification controversies.\nWhich of the statements given above is/are correct?', ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 2, 'Both statements are correct. The wild ass (Equus hemionus) is native to Kutch and its skeletal similarity to the horse fuels the Surkotada debate.'),
    ("Consider the following statements regarding burial offerings in Harappan graves:\n1. Skeletons of domestic dogs are found in almost every single excavated Harappan grave.\n2. Ropar is the only site where a dog was found buried directly beneath the owner's body.\nWhich of the statements given above is/are correct?", ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 2, 'Statement 2 is correct. Statement 1 is incorrect: dog co-burials are extremely rare, with Ropar being the only verified site.'),
    ('With reference to the ancient environment of the Indus Valley, consider the following statements:\n1. The frequent depiction of swampy species like rhinoceros and tigers on seals indicates a humid, wet climate.\n2. The complete absence of desert animals like camels on seals shows the valley was completely forested.\nWhich of the statements given above is/are correct?', ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 2, 'Statement 1 is correct. Statement 2 is incorrect: camels existed (proven by bones at Kalibangan) but were simply not chosen as seal motifs.'),
    ('Consider the following statements regarding manufacturing from wild animal remains:\n1. Antlers of wild deer (sambar/chital) were collected from forests to manufacture needles, awls, and pins.\n2. Antlers show signs of sawing and carving in workshops at Harappa and Mohenjo-daro.\nWhich of the statements given above is/are correct?', ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 2, 'Both statements are correct. Deer antlers were collected and processed in urban workshops to make bone implements and tools.'),
    ('With reference to the late Harappan pastoral shifts, consider the following statements:\n1. The decline of urban granaries led to a decentralization of herding and local dairy production.\n2. Late Harappan populations in Gujarat focused heavily on herding goats and sheep rather than large cattle.\nWhich of the statements given above is/are correct?', ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 2, 'Both statements are correct. The transition to rural settings was accompanied by herding smaller, drought-adapted sheep and goats.'),
    ('Consider the following statements regarding buffalo representations on seals:\n1. Seals sometimes depict a water buffalo in combat with a tiger, representing nature myths.\n2. Buffalo horn motifs are depicted on the headgear of deities, indicating sacred value.\nWhich of the statements given above is/are correct?', ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 2, 'Both statements are correct. Buffaloes are shown in combat scenes, and horned headgear is a diagnostic feature of Harappan deities on seals.'),
    ('With reference to exchange systems in Harappan trade, consider the following statements:\n1. Standardized chert weights, mostly cubic, were used to weigh commodities during barter transactions.\n2. Trade of pastoral items like wool and hides relied on metallic coins with animal engravings.\nWhich of the statements given above is/are correct?', ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 1, 'Statement 1 is correct. Statement 2 is incorrect: coins did not exist; barter backed by standardized chert weights was the system.'),
]

raw_practice_hin = [
    ('सिंधु घाटी सभ्यता की पशुपालन अर्थव्यवस्था के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. मवेशियों (जेबू) की हड्डियाँ लगभग सभी स्थलों पर प्राणि-अवशेषों में सबसे अधिक प्रतिशत में मिली हैं।\n2. भेड़ और बकरियों को मुख्य रूप से दूध और ऊन के लिए एक साथ पाला जाता था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?', ['1 केवल', '2 केवल', '1 और 2 दोनों', 'न तो 1 न ही 2'], 2, 'दोनों कथन सही हैं। मवेशियों (जेबू) की हड्डियाँ सबसे अधिक मिली हैं (50-60%), और भेड़-बकरियों को दूध, मांस तथा ऊन के लिए पाला जाता था।'),
    ('हड़प्पा संस्कृति में गाय के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. सेलखड़ी की प्रशासनिक मुहरों पर कूबड़ वाले बैल का अंकन अत्यधिक मिलता है।\n2. मोहनजोदड़ो की कई मुहरों पर कूबड़ वाले बैल के साथ मादा गाय का भी अंकन किया गया है।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?', ['1 केवल', '2 केवल', '1 और 2 दोनों', 'न तो 1 न ही 2'], 0, 'कथन 1 सही है। कथन 2 गलत है क्योंकि मुहरों और कलाकृतियों पर गाय का चित्रण पूरी तरह से अनुपस्थित है, जो ऋग्वैदिक काल से अलग है।'),
    ('हड़प्पा सभ्यता में भारवाहक पशुओं के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. कालीबंगन से शुष्क जलवायु के अनुकूल ऊंट की हड्डियाँ महत्वपूर्ण मात्रा में मिली हैं।\n2. पंजाब में कृषि खेतों की जुताई के लिए ऊंट ही मुख्य श्रम पशु थे।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?', ['1 केवल', '2 केवल', '1 और 2 दोनों', 'न तो 1 न ही 2'], 0, 'कथन 1 सही है। कथन 2 गलत है क्योंकि जुताई के लिए मुख्य रूप से कूबड़ वाले बैलों का उपयोग किया जाता था, ऊंटों का नहीं।'),
    ('हड़प्पा शहरों में शवाधान प्रथाओं के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. पंजाब के रोपण से एक कब्र मिली है जहाँ मनुष्य के कंकाल के साथ पालतू कुत्ते को दफनाया गया था।\n2. पालतू जानवरों को उनके मालिकों के साथ दफनाने की यह प्रथा सभी हड़प्पा कब्रिस्तानों में आम थी।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?', ['1 केवल', '2 केवल', '1 और 2 दोनों', 'न तो 1 न ही 2'], 0, 'कथन 1 सही है। कथन 2 गलत है क्योंकि मनुष्य के साथ कुत्ते को दफनाने की यह प्रथा केवल रोपण में मिली है, अन्य कब्रिस्तानों में नहीं।'),
    ('सिंधु घाटी सभ्यता में पालतू जानवरों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. चन्हुदड़ो से गीली मिट्टी की एक ईंट मिली है जिस पर बिल्ली का पीछा करते कुत्ते के पैरों के निशान अंकित हैं।\n2. मिट्टी के खिलौना कुत्तों पर गले में पट्टा दिखाना यह दर्शाता है कि उन्हें पालतू बनाया गया था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?', ['1 केवल', '2 केवल', '1 और 2 दोनों', 'न तो 1 न ही 2'], 2, 'दोनों कथन सही हैं। चन्हुदड़ो की ईंट पर पंजों के निशान और खिलौना कुत्तों के गले में पट्टा पालतू पेट्स होने की पुष्टि करते हैं।'),
    ("सिंधु घाटी सभ्यता के कूबड़ वाले मवेशियों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. कूबड़ वाले मवेशियों को वैज्ञानिक रूप से 'बॉस इंडिकस' (Bos indicus) के रूप में वर्गीकृत किया गया है।\n2. मुहरों पर कूबड़ वाले बैल का चित्रण बहुत ही सजीव और कलात्मक बारीकी से किया गया है।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ['1 केवल', '2 केवल', '1 और 2 दोनों', 'न तो 1 न ही 2'], 2, 'दोनों कथन सही हैं। कूबड़ वाले बैल (जेबू) का वैज्ञानिक नाम बॉस इंडिकस है और मुहरों पर इनका अत्यधिक कलात्मक चित्रण मिलता है।'),
    ('हड़प्पा वासियों के थलीय व्यापारिक नेटवर्क के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. पथरीले रास्तों पर सामान ढोने के लिए घरेलू गधों का उपयोग भारवाहक पशुओं के रूप में किया जाता था।\n2. कालीबंगन से प्राप्त ऊंट की हड्डियाँ दर्शाती हैं कि ऊंटों का उपयोग मरुस्थलीय व्यापार मार्गों पर होता था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?', ['1 केवल', '2 केवल', '1 और 2 दोनों', 'न तो 1 न ही 2'], 2, 'दोनों कथन सही हैं। गधे और ऊंट शुष्क एवं पहाड़ी क्षेत्रों में मालवाहक पशुओं के रूप में व्यापारिक नेटवर्क के मुख्य हिस्से थे।'),
    ('हड़प्पा कालीन आहार और प्राणि-अवशेषों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. आवासीय कचरे के ढेरों में पालतू सूअर (Sus scrofa) की हड्डियाँ प्रचुर मात्रा में मिली हैं।\n2. सूअर शहरों के कचरा क्षेत्रों में जैविक कचरा खाते थे और सस्ता मांस प्रदान करते थे।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?', ['1 केवल', '2 केवल', '1 और 2 दोनों', 'न तो 1 न ही 2'], 2, 'दोनों कथन सही हैं। सूअर की हड्डियाँ कचरे के ढेरों से मिली हैं, जो मांस उपभोग और अपशिष्ट खाने वाले पशु के रूप में उनकी भूमिका को दर्शाती हैं।'),
    ('हड़प्पा भेड़ और बकरियों के पालन के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. खानाबदोश चरवाहे पूरक संसाधनों के उपयोग के लिए भेड़ और बकरियों को एक साथ मिश्रित झुंडों में पालते थे।\n2. भेड़ों से मुख्यतः ऊन प्राप्त किया जाता था, जबकि बकरियों को मांस और दूध के लिए पाला जाता था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?', ['1 केवल', '2 केवल', '1 और 2 दोनों', 'न तो 1 न ही 2'], 2, 'दोनों कथन सही हैं। मिश्रित झुंडों में दोनों को पाला जाता था; भेड़ों से ऊन तथा दोनों से दूध और मांस प्राप्त होता था।'),
    ('हड़प्पा स्थलों से प्राप्त मिट्टी के खिलौनों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. कुत्तों की मिट्टी की आकृतियों में उनके गले में पट्टा (collar band) बना हुआ मिला है।\n2. मोहनजोदड़ो से रथ खींचते हुए घोड़ों के मिट्टी के मॉडल भी प्रचुर मात्रा में मिले हैं।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?', ['1 केवल', '2 केवल', '1 और 2 दोनों', 'न तो 1 न ही 2'], 0, 'कथन 1 सही है। कथन 2 गलत है क्योंकि हड़प्पा कला में घोड़े और रथ खींचते घोड़ों के चित्र पूर्णतः अनुपस्थित हैं।'),
    ('परिपक्व हड़प्पा कला में चित्रित हिंसक बिल्ली प्रजातियों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. मुहरों पर बाघ एक आम प्रतीक है, जिसे अक्सर पेड़ पर बैठे मनुष्य के साथ दिखाया गया है।\n2. शेर हड़प्पा प्रशासनिक मुहरों पर सबसे आम प्रतीक था जो राजकीय सत्ता को दर्शाता था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?', ['1 केवल', '2 केवल', '1 और 2 दोनों', 'न तो 1 न ही 2'], 0, 'कथन 1 सही है। कथन 2 गलत है क्योंकि मुहरों पर शेर का चित्रण अत्यंत दुर्लभ/अनुपस्थित है, जबकि बाघ बहुत आम है।'),
    ("मोहनजोदड़ो की प्रसिद्ध 'पशुपति मुहर' पर निम्नलिखित में से किन जंगली जानवरों का चित्रण मिलता है?\n1. बाघ\n2. हाथी\n3. गैंडा\n4. शेर\nनीचे दिए गए कूट का प्रयोग कर सही उत्तर चुनिए:", ['1, 2 और 3 केवल', '1, 2 और 4 केवल', '2, 3 और 4 केवल', '1, 2, 3 और 4'], 0, 'पशुपति मुहर पर केंद्रीय आकृति के चारों ओर बाघ, हाथी, गैंडा और भैंस खड़े हैं। शेर इस पर अनुपस्थित है।'),
    ('हड़प्पा कला में जलीय जीवों के चित्रण के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. बर्तनों, ताबीजों और मुहरों पर घड़ियाल (मछली खाने वाले मगरमच्छ) का चित्रण बहुत आम है।\n2. तटीय स्थलों जैसे लोथल के बर्तनों पर समुद्री मछलियों और कछुओं के सुंदर चित्र मिलते हैं।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?', ['1 केवल', '2 केवल', '1 और 2 दोनों', 'न तो 1 न ही 2'], 2, 'दोनों कथन सही हैं। घड़ियाल नदी पारिस्थितिकी का और समुद्री मछलियां/कछुए लोथल की तटीय कला का प्रतीक हैं।'),
    ('हड़प्पा सभ्यता के समुद्री व्यापार के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. बलूचिस्तान के मकरान तट से सूखी और नमकीन समुद्री मछली अंतर्देशीय शहरों (जैसे हड़प्पा) में व्यापार के लिए भेजी जाती थी।\n2. हड़प्पा से मिली मछलियों की हड्डियों में ऐसी प्रजातियाँ शामिल हैं जो केवल अरब सागर में पाई जाती हैं।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?', ['1 केवल', '2 केवल', '1 और 2 दोनों', 'न तो 1 न ही 2'], 2, 'दोनों कथन सही हैं। वैज्ञानिक विश्लेषण पुष्टि करता है कि अंतर्देशीय हड़प्पा में समुद्री मछली मकरान तट (800 किमी दूर) से आयात की जाती थी।'),
    ('हड़प्पा स्थलों से मिले मछली पकड़ने के उपकरणों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. मोहनजोदड़ो और लोथल से तांबे और कांसे के मछली पकड़ने के हुक (hooks) बड़ी संख्या में मिले हैं।\n2. धातु की कमी के कारण हड़प्पा वासी मछली पकड़ने के लिए केवल हड्डियों के हुक पर निर्भर थे।\nउपर्युक्त कथनों में से कौन-sa/se सही है/हैं?', ['1 केवल', '2 केवल', '1 और 2 दोनों', 'न तो 1 न ही 2'], 0, 'कथन 1 सही है। कथन 2 गलत है क्योंकि मछली पकड़ने के लिए तांबे और कांसे के कांटे (hooks) व्यापक रूप से उपयोग होते थे।'),
    ('शंख की वस्तुओं के निर्माण के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. नागेश्वर और बालाकोट जैसी तटीय बस्तियाँ समुद्री शंख (Turbinella pyrum) एकत्र करने और तराशने में माहिर थीं।\n2. तटीय कार्यशालाओं से बनी शंख की चूड़ियाँ, चमचे और पच्चीकारी की वस्तुएं अंतर्देशीय शहरों में व्यापार के लिए भेजी जाती थीं।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?', ['1 केवल', '2 केवल', '1 और 2 दोनों', 'न तो 1 न ही 2'], 2, 'दोनों कथन सही हैं। नागेश्वर और बालाकोट विशेष शंख शिल्प केंद्र थे जो अपनी निर्मित वस्तुओं का व्यापार अंतर्देशीय शहरों में करते थे।'),
    ('सिंधु घाटी सभ्यता में हाथीदांत के उपयोग के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. लोथल से हाथीदांत की कार्यशाला के अवशेष मिले हैं, जिसमें बिना काम किए दांत और कचरा टुकड़े शामिल हैं।\n2. मेसोपोटामिया को विलासिता की वस्तु के रूप में सिंधु घाटी (मेलुहा) से हाथीदांत का निर्यात किया जाता था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?', ['1 केवल', '2 केवल', '1 और 2 दोनों', 'न तो 1 न ही 2'], 2, 'दोनों कथन सही हैं। लोथल में हाथीदांत कारखाना था और मेसोपोटामियाई स्रोतों में मेलुहा से हाथीदांत के आयात के स्पष्ट संदर्भ हैं।'),
    ('हड़प्पा वासियों के शिकार प्रथाओं के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. जंगली सूअर, हिरण और पक्षियों का शिकार करने के लिए तांबे के बाणाग्र और मिट्टी की गुलेल की गोलियों का उपयोग होता था।\n2. बड़े शहरी केंद्रों में दैनिक प्रोटीन आहार का मुख्य स्रोत जंगली जानवरों का शिकार ही था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?', ['1 केवल', '2 केवल', '1 और 2 दोनों', 'न तो 1 न ही 2'], 0, 'कथन 1 सही है। कथन 2 गलत है क्योंकि प्रोटीन का मुख्य स्रोत पालतू पशु (मवेशी, भेड़-बकरी) थे, जंगली शिकार केवल सहायक था।'),
    ('पशु हड्डियों के पुरातात्विक विश्लेषण के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. हड्डियों के जोड़ों पर तेज काटने और खरोंच के निशान मानव उपभोग के लिए मांस प्रसंस्करण (butchery) को दर्शाते हैं।\n2. हड्डियों का झुलसा या जला होना यह दिखाता है कि मांस को भूनकर या पकाकर खाया जाता था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?', ['1 केवल', '2 केवल', '1 और 2 दोनों', 'न तो 1 न ही 2'], 2, 'दोनों कथन सही हैं। हड्डियों पर काटने और जलने के निशान कसाईखाना प्रसंस्करण तथा पकाने की प्रत्यक्ष पुष्टि करते हैं।'),
    ('मवेशियों के आर्थिक उपयोग के संबंध में, निम्नलिखित कथनों पर विचार कीजिए:\n1. मवेशियों की मृत्यु-आयु का प्रोफाइल यह दर्शाता है कि उन्हें बुढ़ापे तक पाला जाता था, जो दूध और श्रम उपयोग को सिद्ध करता है।\n2. मवेशियों को बहुत कम उम्र में मार दिया जाता था, जिससे पता चलता है कि उन्हें केवल गोमांस के लिए पाला जाता था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?', ['1 केवल', '2 केवल', '1 और 2 दोनों', 'न तो 1 न ही 2'], 0, 'कथन 1 सही है। मवेशियों को अधिक उम्र तक जीवित रखना कृषि श्रम (हल/गाड़ी) और दूध उत्पादन के लिए उनके उपयोग को सिद्ध करता है।'),
    ('हड़प्पा शहरों में भेड़ों के पालन के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. भेड़ों को वयस्क/वृद्ध होने तक पाला जाता था ताकि कई वर्षों तक उनसे अधिकतम ऊन प्राप्त किया जा सके।\n2. बुने हुए ऊनी और सूती कपड़े हड़प्पा वासियों के प्रमुख औद्योगिक निर्यात उत्पाद थे।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?', ['1 केवल', '2 केवल', '1 और 2 दोनों', 'न तो 1 न ही 2'], 2, 'दोनों कथन सही हैं। भेड़ों की अधिक उम्र की हड्डियां ऊन की कतरन का साक्ष्य हैं, जो कपड़ा उद्योग को सहारा देती थीं।'),
    ('गुजरात के सुरकोटदा स्थल के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. जे.पी. जोशी ने सुरकोटदा के परिपक्व-उत्तर हड़प्पा स्तरों से ऐसी हड्डियां खोदीं जिन्हें घोड़े की हड्डियां कहा गया।\n2. हंगरी के प्राणि-विज्ञानी सैंडोर बोकोनी ने इन हड्डियों को वास्तविक घोड़े (Equus caballus) के रूप में पहचाना।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?', ['1 केवल', '2 केवल', '1 और 2 दोनों', 'न तो 1 न ही 2'], 2, 'दोनों कथन सही हैं। जे.पी. जोशी ने सुरकोटदा से हड्डियां प्राप्त की थीं और बोकोनी ने उन्हें घोड़े (Equus caballus) के अवशेष माना था।'),
    ('घोड़े के विवाद में विपक्षी तर्कों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. रिचर्ड मीडो का तर्क है कि सुरकोटदा की हड्डियां वास्तव में जंगली गधे (khur) या पालतू गधे की हैं।\n2. जंगली गधा (Equus hemionus) कच्छ के रण का मूल निवासी है और इसकी हड्डियां घोड़े से बहुत मिलती हैं।\nउपर्युक्त कथनों में से कौन-sa/se सही है/हैं?', ['1 केवल', '2 केवल', '1 और 2 दोनों', 'न तो 1 न ही 2'], 2, 'दोनों कथन सही हैं। मीडो ने इन साक्ष्यों को खारिज कर इन्हें स्थानीय जंगली गधे (khur) की हड्डियां माना था।'),
    ('हड़प्पा संस्कृति में घोड़े की सांस्कृतिक भूमिका के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. परिपक्व हड़प्पा मुहरों और टेराकोटा कला पर घोड़े का चित्रण पूर्णतः अनुपस्थित है।\n2. ऋग्वैदिक संस्कृति में घोड़े को केंद्रीय आर्थिक और धार्मिक महत्व प्राप्त था, जो हड़प्पा मुहर कला से भिन्न है।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?', ['1 केवल', '2 केवल', '1 और 2 दोनों', 'न तो 1 न ही 2'], 2, 'दोनों कथन सही हैं। मुहरों पर घोड़े का चित्रण न मिलना यह दर्शाता है कि हड़प्पा समाज में इसका महत्व नहीं था, जो वैदिक काल से अलग है।'),
    ('उत्तर हड़प्पा काल में पर्यावरणीय बदलावों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. कचरे के ढेरों में गैंडे और हाथी जैसे आर्द्र जलवायु के जीवों की हड्डियों का गायब होना शुष्क जलवायु को दर्शाता है।\n2. उत्तर हड़प्पा स्तरों में शुष्क परिस्थितियों में जीवित रहने वाली भेड़ और बकरियों की हड्डियों का अनुपात बढ़ गया।\nउपर्युक्त कथनों में से कौन-sa/se सही है/हैं?', ['1 केवल', '2 केवल', '1 और 2 दोनों', 'न तो 1 न ही 2'], 2, 'दोनों कथन सही हैं। हड्डियों के प्रकार में यह बदलाव 1900 ईसा पूर्व के आसपास मानसून के कमजोर होने और शुष्कीकरण की पुष्टि करता है।'),
    ('गुजरात के खानाबदोश चरवाहा समूहों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. वे चारे की तलाश में मैदानों और पहाड़ियों के बीच मौसमी प्रवास (transhumance) करते थे।\n2. वे शहरी केंद्रों को दूध, ऊन, चमड़ा और श्रम पशु देते थे और बदले में अनाज तथा धातु के उपकरण लेते थे।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?', ['1 केवल', '2 केवल', '1 और 2 दोनों', 'न तो 1 न ही 2'], 2, 'दोनों कथन सही हैं। पशुओं को बचाने के लिए ऋतुप्रवास (transhumance) होता था और वे शहरों के साथ परस्पर व्यापारिक विनिमय करते थे।'),
    ('हड़प्पा स्थलों पर प्राणि-पुरातत्वीय सांख्यिकी के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. अधिकांश शहरी स्थलों पर कुल हड्डियों में पालतू बैल, भैंस, भेड़ और बकरियों की हड्डियां 70% से 80% से अधिक हैं।\n2. हड़प्पा के आवासीय कचरे के ढेरों में जंगली हिरण और बारहसिंगा की हड्डियाँ पूरी तरह से अनुपस्थित हैं।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?', ['1 केवल', '2 केवल', '1 और 2 दोनों', 'न तो 1 न ही 2'], 1, 'कथन 1 सही है। कथन 2 गलत है क्योंकि पूरक आहार के रूप में जंगली हिरणों की हड्डियां कुछ मात्रा में मिलती हैं।'),
    ('बालाकोट की तटीय निर्वाह रणनीतियों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. बालाकोट में खुदाई से समुद्री मछली और समुद्री कछुओं के अवशेष भारी मात्रा में मिले हैं, जो जलीय आहार को सिद्ध करते हैं।\n2. यह स्थल समुद्री जहाजों के लिए कूबड़ वाले ऊंटों के पालन-पोषण का एक प्रमुख केंद्र था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?', ['1 केवल', '2 केवल', '1 और 2 दोनों', 'न तो 1 न ही 2'], 1, 'कथन 1 सही है। कथन 2 गलत है क्योंकि बालाकोट मछली पकड़ने और शंख कटाई का केंद्र था, ऊंटों का नहीं।'),
    ('सिंधु घाटी सभ्यता में परिवहन प्रणालियों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. मिट्टी के खिलौना गाड़ियों के मॉडल दिखाते हैं कि गाड़ियों को खींचने के लिए कूबड़ वाले बैलों का उपयोग होता था।\n2. खिलौना बैलगाड़ियों में ठोस (तिल्ली-रहित) पहिये होते थे, जो सड़कों पर मिले पहियों के निशानों से मेल खाते हैं।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?', ['1 केवल', '2 केवल', '1 और 2 दोनों', 'न तो 1 न ही 2'], 2, 'दोनों कथन सही हैं। ठोस पहियों वाली बैलगाड़ी ही माल ढोने का मुख्य माध्यम थी, जिसकी पुष्टि खिलौने और पहियों के निशान करते हैं।'),
    ('हड़प्पा मुहर कला के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. मुहरों को सेलखड़ी (steatite) नामक एक नरम पत्थर पर तराशा जाता था और फिर उन्हें गर्म कर पकाया जाता था।\n2. मुहरों पर चित्रित सबसे आम जानवर कूबड़ वाला बैल (zebu) था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?', ['1 केवल', '2 केवल', '1 और 2 दोनों', 'न तो 1 न ही 2'], 1, 'कथन 1 सही है। कथन 2 गलत है क्योंकि मुहरों पर एक सींग वाला गेंडा (unicorn) सबसे आम था, बैल नहीं।'),
    ('कचरे के ढेरों में मिले जंगली जानवरों के अवशेषों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. जंगली सूअर, गैंडे और हिरणों की हड्डियां दर्शाती हैं कि शहरी लोग कभी-कभी पूरक शिकार भी करते थे।\n2. भोजन के रूप में जंगली पक्षियों जैसे मोर, जंगली मुर्गियों और बत्तखों का भी सेवन किया जाता था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?', ['1 केवल', '2 केवल', '1 और 2 दोनों', 'न तो 1 न ही 2'], 2, 'दोनों कथन सही हैं। कचरे से मिले विविध अवशेष यह सिद्ध करते हैं कि पूरक आहार के रूप में जंगली पशु-पक्षियों का सेवन होता था।'),
    ('हड़प्पा मुहरों के अंकन के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. मुहरों पर कभी-कभी मिश्रित पशु (composite creatures) मिलते हैं, जैसे बैल, गेंडा और बकरे के सिरों को मिलाना।\n2. मानव चेहरे और गेंडे के सींग वाले चौपायों का चित्रण हड़प्पा की समृद्ध धार्मिक कल्पनाओं को दर्शाता है।\nउपर्युक्त कथनों में से कौन-sa/se सही है/हैं?', ['1 केवल', '2 केवल', '1 और 2 दोनों', 'न तो 1 न ही 2'], 2, 'दोनों कथन सही हैं। काल्पनिक और मिश्रित जानवरों का मुहरों पर चित्रण हड़प्पा संस्कृति की एक विशेष शैली थी।'),
    ('हड़प्पा में रसोई कचरे के अवशेषों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. नदियों से पकड़े गए कछुओं के खोल (shells) जिन पर जलने के निशान हैं, आहार के रूप में उनके सेवन को दर्शाते हैं।\n2. कछुओं को घरों में पालतू पशु के रूप में पाला जाता था और उन्हें मारना धार्मिक रूप से वर्जित था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?', ['1 केवल', '2 केवल', '1 और 2 दोनों', 'न तो 1 न ही 2'], 1, 'कथन 1 सही है। कथन 2 गलत है क्योंकि जले हुए खोल भोजन के हिस्से के रूप में कछुए के सेवन की पुष्टि करते हैं।'),
    ('कालीबंगन से प्राप्त दांतों के अवशेषों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. खुदाई से अश्व परिवार (Equidae) के जबड़े और दांतों के अवशेष प्राप्त हुए हैं।\n2. ये दंत अवशेष निश्चित रूप से यह प्रमाणित करते हैं कि राजस्थान में कृषि के लिए घरेलू घोड़ों का उपयोग होता था।\nउपर्युक्त कथनों में से कौन-sa/se सही है/हैं?', ['1 केवल', '2 केवल', '1 और 2 दोनों', 'न तो 1 न ही 2'], 1, 'कथन 1 सही है। कथन 2 गलत है क्योंकि इन दांतों के आधार पर घोड़े और गधे के बीच स्पष्ट अंतर करना संभव नहीं हो सका है।'),
    ('हड़प्पा शहरों में पालतू पेट्स के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. कुत्तों के खिलौनों में उनके गले में पट्टा दिखाना सुरक्षा और पालतू होने की प्रथा को दर्शाता है।\n2. बिल्लियों के चूहे पकड़ते हुए मिट्टी के खिलौने भी प्रचुर मात्रा में खोजे गए हैं।\nउपर्युक्त कथनों में से कौन-sa/se सही है/हैं?', ['1 केवल', '2 केवल', '1 और 2 दोनों', 'न तो 1 न ही 2'], 1, 'कथन 1 सही है। कथन 2 गलत है क्योंकि बिल्लियों के अवशेष (पंजों के निशान) ईंट पर मिले हैं, लेकिन उनके मिट्टी के खिलौने नहीं मिले हैं।'),
    ('हड़प्पा कृषि में फसल काटने के उपकरणों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. लकड़ी के हत्थों में चर्ट (पत्थर) के फलक लगाकर बनाई गई हँसियाँ ही फसल काटने का मुख्य साधन थीं।\n2. रबी फसलों की कटाई के लिए तांबे और कांसे की हँसियों का बड़े पैमाने पर निर्माण किया जाता था।\nउपर्युक्त कथनों में से कौन-sa/se सही है/हैं?', ['1 केवल', '2 केवल', '1 और 2 दोनों', 'न तो 1 न ही 2'], 1, 'कथन 1 सही है। कथन 2 गलत है क्योंकि धातु की हँसियाँ अत्यंत दुर्लभ थीं, चर्ट (पत्थर) का ही उपयोग फसल कटाई में अधिक होता था।'),
    ('हड़प्पा में जल भैंस (Bubalus bubalis) के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. भैंसों का घरेलूकरण किया गया था और उनका उपयोग दूध, मांस तथा गीली मिट्टी में भारी श्रम के लिए होता था।\n2. गुजरात के शुष्क क्षेत्रों में भैंसों की हड्डियाँ कूबड़ वाले बैलों से अधिक संख्या में मिली हैं।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?', ['1 केवल', '2 केवल', '1 और 2 दोनों', 'न तो 1 न ही 2'], 1, 'कथन 1 सही है। कथन 2 गलत है क्योंकि गुजरात के शुष्क क्षेत्रों में कूबड़ वाले बैल ही मुख्य थे, भैंसें जलीय या नम मैदानों में अधिक थीं।'),
    ('हड़प्पा कला में जंगली पक्षियों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. मोर का चित्रण बर्तनों पर पेंटिंग और खिलौना मूर्तियों में बहुत अधिक मिलता है, जो उसके महत्व को दर्शाता है।\n2. मुहरों पर मोरों को देवताओं के रथ खींचते हुए चित्रित किया गया है।\nउपर्युक्त कथनों में से कौन-sa/se सही है/हैं?', ['1 केवल', '2 केवल', '1 और 2 दोनों', 'न तो 1 न ही 2'], 1, 'कथन 1 सही है। कथन 2 गलत है क्योंकि रथ का उपयोग ही अनुपस्थित था, और मोर का मुहरों पर रथ खींचने का कोई चित्रण नहीं है।'),
    ("मेसोपोटामिया के क्यूनिफॉर्म अभिलेखों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. अभिलेखों में 'मेलुहा' (सिंधु घाटी) से हाथीदांत की बनी विलासिता की वस्तुओं के आयात की सूची मिलती है।\n2. बिना तराशे हाथीदांत के बड़े दांत खाड़ी के बंदरगाहों के माध्यम से मेसोपोटामिया की कार्यशालाओं में भेजे जाते थे।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ['1 केवल', '2 केवल', '1 और 2 दोनों', 'न तो 1 न ही 2'], 2, 'दोनों कथन सही हैं। सिंधु घाटी से निर्मित हाथीदांत की कंघियां, पिन और कच्चे दांत मेसोपोटामिया निर्यात किए जाते थे।'),
    ('गुजरात के ग्रामीण क्षेत्रों में पशुधन प्रबंधन के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. ग्रामीण स्थलों पर पत्थर और ईंटों के वृत्ताकार बाड़े मिले हैं जो रात में भेड़-बकरियों को बांधने (corrals) के काम आते थे।\n2. ये बाड़े पालतू पशुओं को रात में बाघ और तेंदुओं जैसे हिंसक जंगली जानवरों से बचाने के लिए बनाए जाते थे।\nउपर्युक्त कथनों में से कौन-sa/se सही है/हैं?', ['1 केवल', '2 केवल', '1 और 2 दोनों', 'न तो 1 न ही 2'], 2, 'दोनों कथन सही हैं। ये वृत्ताकार घेरे ग्रामीण क्षेत्रों में रात में चरवाहों द्वारा पशुओं को जंगली जानवरों से सुरक्षित रखने के लिए बनाए जाते थे।'),
    ('हड़प्पा सभ्यता में मछली पकड़ने के कांटों (hooks) के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. खुदाई से मिले मछली पकड़ने के कांटे तांबे और कांसे जैसी धातुओं से बने हैं।\n2. परिपक्व हड़प्पा काल में गंगा घाटी के स्थलों से लोहे के मछली कांटों का आयात किया जाता था।\nउपर्युक्त कथनों में से कौन-sa/se सही है/हैं?', ['1 केवल', '2 केवल', '1 और 2 दोनों', 'न तो 1 न ही 2'], 1, 'कथन 1 सही है। कथन 2 गलत है क्योंकि हड़प्पा वासियों को लोहे का कोई ज्ञान नहीं था।'),
    ("हड़प्पा स्थलों पर धार्मिक अनुष्ठानों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. कालीबंगन की मिट्टी की वेदिकाओं से राख और पशुओं की हड्डियाँ मिली हैं, जो पशु बलि की ओर संकेत करती हैं।\n2. मोहनजोदड़ो की 'पशुपति मुहर' पर एक योगी को अश्वमेध (घोड़े की बलि) अनुष्ठान करते दिखाया गया है।\nउपर्युक्त कथनों में से कौन-sa/se सही है/हैं?", ['1 केवल', '2 केवल', '1 और 2 दोनों', 'न तो 1 न ही 2'], 1, 'कथन 1 सही है। कथन 2 गलत है क्योंकि पशुपति मुहर पर कोई बलि दृश्य नहीं है, यह ध्यानमग्न योगी और जानवरों का दृश्य है।'),
    ('हड़प्पा और ऋग्वैदिक समाजों के बीच अंतर के संबंध में, निम्नलिखित कथनों पर विचार कीजिए:\n1. हड़प्पा मुहरों पर बैल और एकसिंगी का दबदबा है, जबकि ऋग्वैदिक संस्कृति पूरी तरह से अश्व-केंद्रित (horse-centric) है।\n2. हड़प्पा सभ्यता मुख्य रूप से शहरी और व्यावसायिक थी, जबकि ऋग्वैदिक समाज मुख्य रूप से चरवाहा और ग्रामीण था।\nउपर्युक्त कथनों में से कौन-sa/se सही है/हैं?', ['1 केवल', '2 केवल', '1 और 2 दोनों', 'न तो 1 न ही 2'], 2, 'दोनों कथन सही हैं। ये दोनों कालों के बीच अर्थव्यवस्था और पशु प्राथमिकताओं में बड़े सांस्कृतिक अंतर को दर्शाते हैं।'),
    ("कच्छ के रण के जंगली गधे (खुर) के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. जंगली गधे का वैज्ञानिक नाम 'इक्वस हेमीओनस' (Equus hemionus) है।\n2. इसकी हड्डियों की बनावट घोड़े से इतनी मिलती है कि प्राणि-पुरातत्वीय पहचान में अक्सर विवाद खड़ा होता है।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ['1 केवल', '2 केवल', '1 और 2 दोनों', 'न तो 1 न ही 2'], 2, 'दोनों कथन सही हैं। जंगली गधे (खुर/Equus hemionus) की हड्डियों की बनावट घोड़े से बहुत अधिक मिलती है, जो सुरकोटदा विवाद का कारण है।'),
    ('हड़प्पा कब्रों में शवाधान सामग्री के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. सिंधु घाटी में मिले लगभग हर एक मानव कंकाल के पास पालतू कुत्ते का कंकाल दफन मिला है।\n2. रोपण एकमात्र ऐसा स्थल है जहाँ मालिक के शव के ठीक नीचे कुत्ते को दफनाने के साक्ष्य मिले हैं।\nउपर्युक्त कथनों में से कौन-sa/se सही है/हैं?', ['1 केवल', '2 केवल', '1 और 2 दोनों', 'न तो 1 न ही 2'], 2, 'कथन 2 सही है। कथन 1 गलत है क्योंकि मनुष्य के साथ कुत्ते को दफनाने की प्रथा अत्यंत दुर्लभ थी और केवल रोपण से प्रमाणित है।'),
    ('सिंधु घाटी के प्राचीन पर्यावरण के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. मुहरों पर गैंडे और बाघ जैसे आर्द्र-भूमि के जीवों का अंकन यहाँ प्राचीन काल में नम एवं सघन वन जलवायु को दर्शाता है।\n2. मुहरों पर ऊंटों का चित्रण न होना यह प्रमाणित करता है कि सिंधु घाटी में ऊंट पूरी तरह से अनुपस्थित थे।\nउपर्युक्त कथनों में से कौन-sa/se सही है/हैं?', ['1 केवल', '2 केवल', '1 और 2 दोनों', 'न तो 1 न ही 2'], 1, 'कथन 1 सही है। कथन 2 गलत है क्योंकि कालीबंगन से ऊंट की हड्डियाँ मिली हैं, मुहरों पर न होना केवल शैलीगत चयन था।'),
    ('जंगली जानवरों के अवशेषों से शिल्प निर्माण के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. जंगली हिरणों (सांभर/चीतल) के सींगों (antlers) को जंगलों से एकत्र कर सुइयां, आरी और पिन बनाए जाते थे।\n2. हड़प्पा और मोहनजोदड़ो की कार्यशालाओं में सींगों को काटने और छीलने के निशान वाले साक्ष्य मिले हैं।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?', ['1 केवल', '2 केवल', '1 और 2 दोनों', 'न तो 1 न ही 2'], 2, 'दोनों कथन सही हैं। हिरण के सींगों को ग्रामीण चरवाहे एकत्र कर शहरों में भेजते थे जहाँ उनसे हड्डियाँ के उपकरण बनते थे।'),
    ('उत्तर हड़प्पा कालीन चरवाहा बदलावों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. बड़े शहरों के पतन के बाद पशुपालन का विकेंद्रीकरण हुआ और स्थानीय स्तर पर डेयरी का महत्व बढ़ा।\n2. गुजरात के उत्तर हड़प्पा समुदायों ने बड़े मवेशियों के बजाय भेड़ और बकरियों के पालन पर अधिक ध्यान दिया।\nउपर्युक्त कथनों में से कौन-sa/se सही है/हैं?', ['1 केवल', '2 केवल', '1 और 2 दोनों', 'न तो 1 न ही 2'], 2, 'दोनों कथन सही हैं। शहरों के पतन और शुष्क जलवायु के कारण चरवाहों ने छोटे तथा कम पानी में जीवित रहने वाले भेड़-बकरियों को पालना शुरू किया।'),
    ('मुहरों पर भैंस के चित्रण के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. मुहरों पर भैंस को बाघ से मुकाबला करते हुए या किसी मानव नायक द्वारा नियंत्रित करते हुए दिखाया गया है।\n2. हड़प्पा देवताओं के मुकुटों पर भैंस के सींगों का अंकन उनके धार्मिक महत्व को दर्शाता है।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?', ['1 केवल', '2 केवल', '1 और 2 दोनों', 'न तो 1 न ही 2'], 2, 'दोनों कथन सही हैं। भैंस मुहरों पर द्वंद्व दृश्यों में मिलती है और इसके सींगों का उपयोग देवताओं के सींगदार मुकुट में किया जाता था।'),
    ('हड़प्पा व्यापार में विनिमय प्रणालियों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. वस्तुओं के तौल और विनिमय के लिए सेलखड़ी या चर्ट के अत्यंत सटीक घनाकार (cubic) बाटों का उपयोग होता था।\n2. ऊन और चमड़े जैसी वस्तुओं के व्यापार में पशुओं के चित्र अंकित धातु के सिक्कों का उपयोग किया जाता था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?', ['1 केवल', '2 केवल', '1 और 2 दोनों', 'न तो 1 न ही 2'], 1, 'कथन 1 सही है। कथन 2 गलत है क्योंकि हड़प्पा अर्थव्यवस्था में धातु के सिक्के नहीं थे; व्यापार वस्तु-विनिमय (barter) पर आधारित था।'),
]

# 10 English Mock Questions (Multi-statement, UPSC standard)
mock_raw_eng = [
    ("With reference to the pastoral economy of the Mature Harappan Civilisation, consider the following statements:\n1. Humped cattle (zebu) were the most economically dominant domesticated animals.\n2. The cow is frequently depicted alongside the zebu bull on steatite administrative seals.\n3. Bone cuts and scrape marks suggest that cattle were slaughtered for meat in urban centers.\nWhich of the statements given above is/are correct?", ["1 and 3 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"], 0, "Statement 1 is correct: Cattle bones dominate faunal assemblages. Statement 2 is incorrect: The cow is completely absent from seals. Statement 3 is correct: Cut marks on cattle bones near residential sectors show meat processing and slaughter."),
    ("Consider the following statements regarding the wild fauna of the Indus Valley:\n1. The tiger and rhinoceros are frequently depicted on seals, indicating a wet, swampy climate.\n2. The lion is the most common feline depicted on Mature Harappan seals.\n3. Elephant remains and ivory items indicate that elephants were native to the region.\nWhich of the statements given above are correct?", ["1 and 3 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"], 0, "Statements 1 and 3 are correct. Statement 2 is incorrect: The lion is absent or extremely rare on seals; the tiger is the dominant feline represented."),
    ("Which of the following pairs is/are correctly matched?\nArchaeological Site - Faunal Finding\n1. Surkotada - Disputed skeletal remains of the true horse\n2. Chanhudaro - Paw prints of a dog chasing a cat on a baked brick\n3. Kalibangan - Significant remains of camel bones\nSelect the correct answer using the code given below:", ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"], 3, "All three pairs are correctly matched. Surkotada has disputed horse bones, Chanhudaro the brick print, and Kalibangan has camel bones."),
    ("With reference to zooarchaeological studies in the Indus Valley Civilisation, consider the following statements:\n1. Reconstructed age-at-death profiles of cattle show they were kept until old age, indicating dairy and traction use.\n2. Sheep and goats were slaughtered at young ages, indicating meat production.\n3. Wild animals represent more than 50% of the total bone assemblages at all major urban sites.\nWhich of the statements given above is/are correct?", ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"], 0, "Statements 1 and 2 are correct. Statement 3 is incorrect: Domesticated animal bones constitute over 70% to 80% of assemblages at major sites; wild game represents a minor portion of the diet."),
    ("Consider the following statements regarding the horse remains debate in Harappan archaeology:\n1. Sandor Bokonyi identified horse bones at Surkotada as belonging to Equus caballus.\n2. Richard Meadow argued that the Surkotada bones belong to the wild ass (Equus hemionus) or domestic donkey.\n3. The horse is a central motif on the seals of Mohenjo-daro, representing ruling class power.\nWhich of the statements given above is/are correct?", ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"], 0, "Statements 1 and 2 are correct. Statement 3 is incorrect: The horse is completely absent from seals and terracotta art, which is a major contrast to Vedic culture."),
    ("With reference to hunting and fishing in Harappan society, consider the following statements:\n1. Copper fish hooks have been excavated at Mohenjo-daro and Lothal, proving active fishing.\n2. Salted and dried marine fish were transported from the Makran coast of Baluchistan to inland cities.\n3. Harappans used iron arrowheads to hunt wild boar and deer.\nWhich of the statements given above is/are correct?", ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"], 0, "Statements 1 and 2 are correct. Statement 3 is incorrect: Iron was unknown to the Harappans (Bronze Age); they used copper or chert arrowheads."),
    ("Consider the following statements:\n1. Domestic dog burials alongside humans have been excavated at Ropar in Punjab.\n2. Terracotta figurines from Harappa show dogs wearing collars, suggesting they were domesticated pets.\nWhich of the statements given above is/are correct?", ["Both 1 and 2", "1 only", "2 only", "Neither 1 nor 2"], 0, "Both statements are correct. Dog-human co-burial is a unique finding at Ropar, and toy dogs show collars at Harappa and Mohenjo-daro."),
    ("Which of the following wild animals are depicted on the famous 'Pashupati Seal' of Mohenjo-daro?\n1. Tiger\n2. Elephant\n3. Rhinoceros\n4. Lion\nSelect the correct answer using the code given below:", ["1, 2 and 3 only", "1, 2 and 4 only", "2, 3 and 4 only", "1, 2, 3 and 4"], 0, "The Pashupati seal depicts a tiger, an elephant, a rhinoceros, and a buffalo surrounding the central deity. The lion is not depicted on the seal."),
    ("With reference to shell and ivory processing in Harappan coastal settlements, consider the following statements:\n1. Chank shell (Turbinella pyrum) was harvested at Balakot and Nageshwar to manufacture bangles.\n2. Ivory workshops containing unworked elephant tusks have been excavated at Lothal.\nWhich of the statements given above is/are correct?", ["Both 1 and 2", "1 only", "2 only", "Neither 1 nor 2"], 0, "Both statements are correct. Coastal shell workshops and Lothal's ivory factory are well-documented archaeological findings."),
    ("Consider the following statements:\nStatement 1: The transition from humped cattle representations on seals to horse representations represents the transition from Harappan to Vedic culture.\nStatement 2: The Rigvedic economy was primarily pastoral and horse-centric, whereas the Mature Harappan economy was agricultural, urban, and bull-centric.\nWhich of the statements given above is/are correct?", ["Both 1 and 2", "1 only", "2 only", "Neither 1 nor 2"], 0, "Both statements are correct. The horse-centric Rigveda is culturally distinct from the bull/unicorn-dominated iconography of the Harappan civilization.")
]

# 10 Hindi Mock Questions
mock_raw_hin = [
    ("परिपक्व हड़प्पा सभ्यता की पशुपालन अर्थव्यवस्था के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. मवेशी (गाय-बैल) सबसे अधिक आर्थिक रूप से प्रभावी पालतू पशु थे।\n2. सेलखड़ी की प्रशासनिक मुहरों पर कूबड़ वाले बैल के साथ गाय का भी अक्सर चित्रण मिलता है।\n3. हड्डियों पर काटने के निशान दर्शाते हैं कि शहरी केंद्रों में मांस के लिए मवेशियों को काटा जाता था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 और 3 केवल", "1 और 2 केवल", "2 और 3 केवल", "1, 2 और 3"], 0, "कथन 1 सही है क्योंकि मवेशी सबसे आम पशुधन थे। कथन 2 गलत है क्योंकि मुहरों पर गाय का चित्रण अनुपस्थित है। कथन 3 सही है क्योंकि काटने के निशान मांस प्रसंस्करण को दर्शाते हैं।"),
    ("सिंधु घाटी के जंगली जीवों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. मुहरों पर बाघ और गैंडे का चित्रण मिलता है, जो एक नम और दलदली जलवायु का संकेत है।\n2. परिपक्व हड़प्पा मुहरों पर शेर सबसे आम बिल्ली प्रजाति का जानवर है।\n3. हाथी के अवशेष और हाथीदांत की वस्तुएं दर्शाती हैं कि हाथी इस क्षेत्र के मूल निवासी थे।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 और 3 केवल", "1 और 2 केवल", "2 और 3 केवल", "1, 2 और 3"], 0, "कथन 1 और 3 सही हैं। कथन 2 गलत है क्योंकि मुहरों पर शेर अनुपस्थित या बहुत दुर्लभ है; बाघ का चित्रण आम है।"),
    ("निम्नलिखित में से कौन सा/से युग्म सही सुमेलित है/हैं?\nपुरातात्विक स्थल - पशु साक्ष्य\n1. सुरकोटदा - वास्तविक घोड़े के विवादास्पद अस्थि अवशेष\n2. चन्हुदड़ो - ईंट पर बिल्ली का पीछा करते कुत्ते के पंजों के निशान\n3. कालीबंगन - ऊंट की हड्डियों के महत्वपूर्ण अवशेष\nनीचे दिए गए कूट का प्रयोग कर सही उत्तर चुनिए:", ["1 और 2 केवल", "2 और 3 केवल", "1 और 3 केवल", "1, 2 और 3"], 3, "तीनों युग्म सही सुमेलित हैं। सुरकोटदा से घोड़े की हड्डियां, चन्हुदड़ो से पंजों के निशान वाली ईंट, और कालीबंगन से ऊंट की हड्डियां मिली हैं।"),
    ("सिंधु घाटी सभ्यता में प्राणि-पुरातत्व (zooarchaeological) अध्ययनों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. मवेशियों की मृत्यु-आयु से पता चलता है कि उन्हें बुढ़ापे तक पाला जाता था, जो डेयरी और श्रम के उपयोग को दर्शाता है।\n2. भेड़ और बकरियों को कम उम्र में काटा जाता था, जो मांस उत्पादन को दर्शाता है।\n3. सभी प्रमुख शहरी स्थलों पर कुल हड्डियों के ढेर में जंगली जानवरों की हड्डियाँ 50% से अधिक हैं।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 और 2 केवल", "2 और 3 केवल", "1 और 3 केवल", "1, 2 और 3"], 0, "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि अधिकांश स्थलों पर 80% से अधिक हड्डियां पालतू पशुओं की हैं, जंगली जानवरों की हिस्सेदारी बहुत कम थी।"),
    ("हड़प्पा पुरातत्व में घोड़े के अवशेषों के विवाद के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. सैंडोर बोकोनी ने सुरकोटदा की हड्डियों को वास्तविक घोड़े (Equus caballus) के रूप में पहचाना।\n2. रिचर्ड मीडो का तर्क है कि ये हड्डियाँ जंगली गधे (Equus hemionus) या पालतू गधे की हैं।\n3. मोहनजोदड़ो की मुहरों पर घोड़ा एक मुख्य प्रतीक है जो शासक वर्ग की शक्ति को दर्शाता है।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 और 2 केवल", "2 और 3 केवल", "1 और 3 केवल", "1, 2 और 3"], 0, "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि मुहरों और टेराकोटा कला पर घोड़ा पूरी तरह से अनुपस्थित है, जो इसे वैदिक संस्कृति से अलग करता है।"),
    ("हड़प्पा समाज में शिकार और मछली पकड़ने के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. मोहनजोदड़ो और लोथल से तांबे के मछली पकड़ने के कांटे मिले हैं, जो मछली पकड़ने को सिद्ध करते हैं।\n2. बलूचिस्तान के मकरान तट से नमकीन और सूखी मछली अंतर्देशीय शहरों में भेजी जाती थी।\n3. हड़प्पा वासी जंगली सूअर और हिरण का शिकार करने के लिए लोहे के बाणाग्र का उपयोग करते थे।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 और 2 केवल", "2 और 3 केवल", "1 और 3 केवल", "1, 2 और 3"], 0, "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि हड़प्पा वासियों को लोहे का ज्ञान नहीं था; वे तांबे या पत्थर के बाणाग्र का उपयोग करते थे।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\n1. पंजाब के रोपण में मानव के साथ पालतू कुत्ते को दफनाने के साक्ष्य मिले हैं।\n2. हड़प्पा से प्राप्त मिट्टी के खिलौनों में कुत्तों को गले में पट्टे पहने हुए दिखाया गया है, जो पालतू होने को दर्शाता है।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 और 2 दोनों", "1 केवल", "2 केवल", "न तो 1 न ही 2"], 0, "दोनों कथन सही हैं। रोपण से मनुष्य और कुत्ते की कब्र मिली है और खिलौना कुत्तों में गले में पट्टे दिखाए गए हैं।"),
    ("मोहनजोदड़ो की प्रसिद्ध 'पशुपति मुहर' पर निम्नलिखित में से किन जंगली जानवरों का चित्रण मिलता है?\n1. बाघ\n2. हाथी\n3. गैंडा\n4. शेर\nनीचे दिए गए कूट का प्रयोग कर सही उत्तर चुनिए:", ["1, 2 and 3 केवल", "1, 2 and 4 केवल", "2, 3 and 4 केवल", "1, 2, 3 and 4"], 0, "पशुपति मुहर पर बाघ, हाथी, गैंडा और भैंस का चित्रण मिलता है। शेर का चित्रण इस पर नहीं है।"),
    ("हड़प्पा की तटीय बस्तियों में शंख और हाथीदांत प्रसंस्करण के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. चूड़ियाँ बनाने के लिए बालाकोट और नागेश्वर में समुद्री शंख (Turbinella pyrum) एकत्र किए जाते थे।\n2. लोथल से हाथीदांत के कारखाने के अवशेष मिले हैं जिनमें बिना काम किए हाथीदांत के दांत भी शामिल हैं।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 और 2 दोनों", "1 केवल", "2 केवल", "न तो 1 न ही 2"], 0, "दोनों कथन सही हैं। शंख कार्यशालाओं और लोथल के हाथीदांत कारखाने के पुरातात्विक साक्ष्य स्पष्ट रूप से मिले हैं।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: मुहरों पर कूबड़ वाले बैल के चित्रण से लेकर वैदिक काल में घोड़े के चित्रण तक का बदलाव हड़प्पा से वैदिक संस्कृति के परिवर्तन को दर्शाता है।\nकथन 2: ऋग्वैदिक अर्थव्यवस्था मुख्य रूप से पशुपालन और घोड़ा-केंद्रित थी, जबकि परिपक्व हड़प्पा अर्थव्यवस्था कृषि, शहरी और बैल-केंद्रित थी।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", ["1 और 2 दोनों", "1 केवल", "2 केवल", "न तो 1 न ही 2"], 0, "दोनों कथन सही हैं। घोड़ा-केंद्रित ऋग्वेद और बैल/एकसिंगी (unicorn) हावी हड़प्पा कला के बीच का सांस्कृतिक अंतर स्पष्ट है।")
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
