import json
import os

ENG_DIR = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\HarappanIndus-Valley-Civilisation\Religions"
HIN_DIR = os.path.join(ENG_DIR, "hi")
os.makedirs(HIN_DIR, exist_ok=True)

# English base structure
eng_data = {
    "breadcrumbs": {
        "parent": "UPSC Syllabus",
        "parentUrl": "/upsc/",
        "current": "Religions of IVC"
    },
    "hero": {
        "title": "Religions & Belief Systems of the Indus Valley Civilisation",
        "description": "Explore the deities, animistic traditions, sacred animals, purification rituals, and burial customs of the Harappan Civilisation for UPSC GS-1."
    },
    "labels": {
        "clickToExpand": "Click to expand details",
        "mockIntro": {
            "title": "Interactive UPSC Mock Test",
            "description": "Evaluate your understanding of Harappan religious beliefs and rituals. This timed test contains 10 high-yield, exam-standard questions with negative marking.",
            "startBtn": "Start Mock Test"
        },
        "mockPlay": {
            "prevBtn": "Previous Question",
            "nextBtn": "Next Question",
            "submitBtn": "Submit Test"
        }
    },
    "timeline": {
        "title": "Religious Beliefs & Ritual Archetypes",
        "description": "Track the religious practices, iconography, and funerary transitions across the Indus Civilisation.",
        "cards": [
            {
                "period": "Deities & Glyptic Art",
                "date": "Pashupati & Mother Goddess",
                "details": "Emergence of sophisticated iconographical archetypes such as the Pashupati Seal and terracotta Mother Goddess figurines with soot-stained headdresses."
            },
            {
                "period": "Animism & Purificatory Architecture",
                "date": "Great Bath & Sacred Animals",
                "details": "Development of monumental civic water structures for purificatory rituals, alongside widespread worship of the Pipal tree and mythical creatures like the Unicorn."
            },
            {
                "period": "Ritual Closures & Funerary Customs",
                "date": "Fire Altars & Standard Burials",
                "details": "Integration of fire worship in oval and rectangular altars (Kalibangan/Lothal) and standardized North-South extended inhumation with grave goods."
            }
        ]
    },
    "mnemonics": {
        "title": "Mnemonics & Memory Hacks",
        "description": "Use these visual memory hooks to retain critical facts about Harappan religious sites and archeological findings.",
        "items": [
            {
                "title": "Mnemonic 1: Pashupati Seal Surrounding Animals",
                "phrase": "\"TEB-R-D (Tiger, Elephant, Buffalo, Rhino + 2 Deer under the seat)\"",
                "decryption": "Remember the animal composition of the Pashupati Proto-Shiva seal: **T**iger, **E**lephant, **B**uffalo, **R**hinoceros surrounding the deity, and 2 **D**eer/ibexes beneath the seat."
            },
            {
                "title": "Mnemonic 2: Fire Altars Locations",
                "phrase": "\"Ka-Lo-Fire (Kalibangan and Lothal Fire Altars)\"",
                "decryption": "**Ka**libangan and **Lo**thal are the two primary Mature Harappan sites where clay-lined **Fire** Altars with ashes, charcoal, and animal bone fragments were discovered."
            },
            {
                "title": "Mnemonic 3: Regional Burial Oddities",
                "phrase": "\"Co-Ha-Do-Lo-Po-Ka (Coffin Harappa, Double Lothal, Pot Kalibangan)\"",
                "decryption": "Wood **Co**ffin burial is at **Ha**rappa, **Do**uble/twin burial is at **Lo**thal, and symbolic **Po**t/cenotaph burial is at **Ka**libangan."
            }
        ]
    },
    "flashcards": {
        "title": "Active Recall Flashcards",
        "description": "Use these active recall questions to reinforce fact-dense syllabus details on Harappan religions.",
        "items": [
            {
                "question": "Which animals surround the seated deity in the famous Pashupati Seal of Mohenjo-daro?",
                "answer": "An <strong>elephant</strong>, a <strong>tiger</strong>, a <strong>rhinoceros</strong>, and a <strong>water buffalo</strong>, with two deer (or ibexes) depicted under the seat.",
                "icon": "fa-paw"
            },
            {
                "question": "How did Sir John Marshall interpret the horned, three-faced deity on the Pashupati Seal?",
                "answer": "As a <strong>Proto-Shiva</strong> (an early historical form of Shiva as Mahadeva or Pashupati, the Lord of Animals), though this is debated by modern scholars.",
                "icon": "fa-yin-yang"
            },
            {
                "question": "What evidence suggests that the terracotta Mother Goddess figurines were used in household rituals?",
                "answer": "The presence of <strong>soot-stained cup-like panniers</strong> on the sides of their elaborate headdresses, likely used as oil lamps or for burning incense.",
                "icon": "fa-fire"
            },
            {
                "question": "Which tree was widely considered sacred and represented frequently on Harappan seals and pottery?",
                "answer": "The <strong>Pipal tree (Ficus religiosa)</strong>, often shown with a horned deity standing in its branches.",
                "icon": "fa-tree"
            },
            {
                "question": "What is the standard orientation of bodies in Mature Harappan graves?",
                "answer": "An <strong>extended position oriented North-South</strong>, with the head pointing toward the North and the feet toward the South.",
                "icon": "fa-compass"
            }
        ]
    },
    "deepDive": {
        "title": "Syllabus Core Study Notes (Deep-Dive)",
        "description": "Master the iconography, animistic elements, and funerary rites of the Indus Civilisation for the Civil Services Examination.",
        "sections": [
            {
                "title": "1. Pashupati Seal, Mother Goddess & Male/Female Deities",
                "content": """<p>Harappan religion is primarily reconstructed from glyptic arts (seals) and terracotta figurines, displaying a pantheon of male and female deities without any trace of public monumental temples.</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-ring"></i> The Pashupati Seal (Proto-Shiva)</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>Discovery & Iconography:</strong> Excavated at Mohenjo-daro, this steatite seal depicts a seated, three-faced male figure in a yogic posture (mulabandhasana), wearing a horned headdress.</li>
      <li><strong>Surrounding Animals:</strong> He is flanked by four animals: an **elephant** and **tiger** on his right, and a **rhinoceros** and **water buffalo** on his left. Two **deer** (or ibexes) sit beneath his low throne.</li>
      <li><strong>Interpretation:</strong> John Marshall termed him *Proto-Shiva*. Modern scholars (like Doris Srinivasan) suggest he represents a composite bovine deity or a pre-Vedic deity associated with fertility.</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-female"></i> Mother Goddess Cult & Temple Absence</div>
    <p style="font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;">
      **Mother Goddess:** Hand-modeled terracotta figurines of standing, heavily ornamented females with fan-shaped headdresses are common at Mohenjo-daro and Harappa. The soot-stained headdress cup/panniers indicate their use in household domestic rituals.
      <br>**Temple Absence:** Unlike Mesopotamia (Ziggurats) and Egypt (Karnak), the Harappan civilization has yielded no temples. Religious practices were decentralized, domestic, and civic.
    </p>
  </div>
</div>""",
                "masteryZone": []
            },
            {
                "title": "2. Animism, Tree & Animal Worship, and Therianthropic Beliefs",
                "content": """<p>The Harappans practiced a form of animism and nature worship, attributing spiritual qualities to trees, animals, and composite mythological creatures.</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-tree"></i> Sacred Trees & Therianthropes</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>Pipal Tree Worship:</strong> The *Pipal tree (Ficus religiosa)* is frequently represented on seals and pottery. Notable seals depict a horned deity emerging from a Pipal tree, with a worshipper kneeling in front and a line of seven figures below.</li>
      <li><strong>Composite Beasts:</strong> Therianthropic figures (part-human, part-animal), such as tiger-bodied men and three-headed monsters (unicorn-bull-ibex), highlight a rich mythological lore.</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-water"></i> Animal Cults & Purificatory Bathing</div>
    <p style="font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;">
      **Animal Worship:** The mythical **Unicorn** (one-horned animal with a sacred standard/censer) is the most common motif. The majestic **humped bull (Zebu)** is depicted realistically, suggesting strength and fertility worship.
      <br>**Great Bath:** Located on the Citadel of Mohenjo-daro, this waterproofed brick pool (using gypsum mortar and bitumen) was built for public, water-based purificatory bathing and civic rituals.
    </p>
  </div>
</div>""",
                "masteryZone": []
            },
            {
                "title": "3. Burial Practices, Fire Altars & Ritual Architecture",
                "content": """<p>Funerary practices and sacrificial altars show regional variations across the civilization, revealing concepts of afterlife and public rituals.</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-bed"></i> Standard & Variant Funerary Rites</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>Inhumation:</strong> Extended burial in simple rectangular pits oriented North-South (head to the North) was the standard practice. Grave goods included pottery, copper mirrors, beads, and food offerings.</li>
      <li><strong>Wooden Coffin:</strong> Harappa's R-37 cemetery revealed a rare wooden coffin burial.</li>
      <li><strong>Lothal Double Burial:</strong> Three graves at Lothal contained twin skeletons buried together, sparking debates on joint burials.</li>
      <li><strong>Kalibangan Pot Burials:</strong> Pits containing only pottery and grave goods but no skeletal remains (symbolic graves).</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-fire"></i> Fire Altars & Sacrificial Pits</div>
    <p style="font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;">
      **Fire Altars:** Rectangular or oval clay-lined pits dug into the floors have been found at **Kalibangan** and **Lothal**. These altars contained charcoal, ash, terracotta triangular cakes, and animal bones, suggesting public fire sacrifices or rituals.
      <br>**Amulets:** Numerous terracotta and steatite amulets indicate a belief in magical protection, evil spirits, and personal protective charms.
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
        "current": "हड़प्पा धर्म"
    },
    "hero": {
        "title": "हड़प्पा सभ्यता के धर्म और धार्मिक विश्वास",
        "description": "यूपीएससी परीक्षा (GS-1) के लिए सिंधु घाटी सभ्यता के देवताओं, प्रकृति पूजा, पवित्र पशुओं, धार्मिक स्नानागारों और शवाधान प्रथाओं का अध्ययन करें।"
    },
    "labels": {
        "clickToExpand": "विवरण देखने के लिए क्लिक करें",
        "mockIntro": {
            "title": "इंटरैक्टिव परीक्षा मॉक टेस्ट",
            "description": "हड़प्पा सभ्यता के धार्मिक विश्वासों और अनुष्ठानों के संबंध में अपनी तैयारी का मूल्यांकन करें। इस समयबद्ध परीक्षण में नकारात्मक अंकन के साथ 10 उच्च-स्तरीय यूपीएससी मानक के प्रश्न शामिल हैं।",
            "startBtn": "मॉक टेस्ट शुरू करें"
        },
        "mockPlay": {
            "prevBtn": "Previous Question",
            "nextBtn": "Next Question",
            "submitBtn": "Submit Test"
        }
    },
    "timeline": {
        "title": "धार्मिक विश्वास और अनुष्ठान के चरण",
        "description": "सिंधु सभ्यता में धार्मिक प्रथाओं, प्रतीकों और शवाधान संक्रमणों के पुरातात्विक साक्ष्यों का कालक्रम देखें।",
        "cards": [
            {
                "period": "देवता और मुहर कला",
                "date": "पशुपति और मातृदेवी",
                "details": "मोहनजोदड़ो से पशुपति मुहर और मिट्टी की मातृदेवी की मूर्तियों (जिनमें दीपक जलाने के कारण कालिख के निशान मिले हैं) का प्रादुर्भाव।"
            },
            {
                "period": "प्रकृति पूजा और शुद्धिकरण वास्तुकला",
                "date": "विशाल स्नानागार और पवित्र पशु",
                "details": "धार्मिक स्नान के लिए मोहनजोदड़ो में विशाल स्नानागार का निर्माण, और पीपल के वृक्ष व काल्पनिक 'एक सींग वाले पशु' (Unicorn) की पूजा का प्रसार।"
            },
            {
                "period": "अग्नि वेदी और शवाधान प्रथाएं",
                "date": "अग्नि वेदियाँ और मानक कब्रें",
                "details": "कालीबंगन और लोथल में यज्ञ कुंड (अग्नि वेदियों) की खोज और उत्तर-दक्षिण दिशा में शवों को दफनाने की मानक प्रथा का विकास।"
            }
        ]
    },
    "mnemonics": {
        "title": "याद रखने के सूत्र (Mnemonics)",
        "description": "यूपीएससी परीक्षा के लिए हड़प्पा के धार्मिक साक्ष्यों और पशुओं को आसानी से याद रखने के लिए इन सूत्रों का उपयोग करें।",
        "items": [
            {
                "title": "याद रखने का सूत्र 1: पशुपति मुहर के चारों ओर के पशु",
                "phrase": "\"बा-हा-गै-भै-दो-हिरण (बाघ, हाथी, गैंडा, भैंसा + दो हिरण नीचे)\"",
                "decryption": "पशुपति मुहर के चारों ओर घिरे पांच प्रमुख पशु: **बा**घ, **हा**थी, **गै**ंडा, **भै**ंसा और आसन के नीचे बैठे **दो** **हिरण**।"
            },
            {
                "title": "याद रखने का सूत्र 2: अग्नि वेदियों के प्राप्ति स्थल",
                "phrase": "\"का-लो-अग्नि (कालीबंगन और लोथल में अग्नि वेदियाँ)\"",
                "decryption": "**का**लीबंगन और **लो**थल दो प्रमुख परिपक्व हड़प्पा स्थल हैं जहाँ से मिट्टी के यज्ञ कुंड या **अग्नि** वेदियाँ प्राप्त हुई हैं।"
            },
            {
                "title": "याद रखने का सूत्र 3: विशिष्ट शवाधान प्रथाएं",
                "phrase": "\"कफ-हड़-डब-लो-पॉट-का (ताबूत हड़प्पा, जुड़वां लोथल, प्रतीकात्मक कालीबंगन)\"",
                "decryption": "लकड़ी का ताबूत (**कफ**िन) शवाधान **हड़**प्पा में, **डब**ल (जुड़वां) शवाधान **लो**थल में, और मिट्टी के बर्तन वाला प्रतीकात्मक (**पॉट**) शवाधान **का**लीबंगन में मिला है।"
            }
        ]
    },
    "flashcards": {
        "title": "सक्रिय स्मरण फ्लैशकार्ड (Active Recall)",
        "description": "तथ्य-प्रधान यूपीएससी प्रश्नों को याद रखने के लिए इन फ्लैशकार्ड्स का उपयोग करें। उत्तर देखने के लिए नीचे दिए गए कार्ड्स पर क्लिक करें।",
        "items": [
            {
                "question": "मोहनजोदड़ो से प्राप्त प्रसिद्ध पशुपति मुहर में बैठे देवता को कौन से पशु घेरे हुए हैं?",
                "answer": "उनके दाहिने ओर **हाथी** और **बाघ**, बाईं ओर **गैंडा** और **जंगली भैंसा**, तथा सिंहासन के नीचे **दो हिरण** (या बारहसिंगा) बैठे हैं।",
                "icon": "fa-paw"
            },
            {
                "question": "सर जॉन मार्शल ने पशुपति मुहर पर चित्रित सींग वाले देवता की व्याख्या किस रूप में की थी?",
                "answer": "उन्होंने इसे <strong>आदि-शिव (Proto-Shiva)</strong> कहा, जो ऐतिहासिक हिंदू धर्म के भगवान शिव का प्रारंभिक रूप था।",
                "icon": "fa-yin-yang"
            },
            {
                "question": "मिट्टी की मातृदेवी की मूर्तियों के सिर पर बने प्यालों में कालिख के निशान क्या दर्शाते हैं?",
                "answer": "यह दर्शाता है कि इन प्यालों का उपयोग घरेलू धार्मिक अनुष्ठानों में <strong>तेल का दीपक जलाने</strong> या धूप जलाने के लिए किया जाता था।",
                "icon": "fa-fire"
            },
            {
                "question": "हड़प्पा की मुहरों और बर्तनों पर सबसे अधिक किस वृक्ष का अंकन मिलता है जिसे पवित्र माना जाता था?",
                "answer": "<strong>पीपल का वृक्ष (Ficus religiosa)</strong>, जिस पर अक्सर सींग वाले देवता को शाखों के बीच खड़े दिखाया गया है।",
                "icon": "fa-tree"
            },
            {
                "question": "हड़प्पा सभ्यता में शवों को दफनाने की मानक दिशा क्या थी?",
                "answer": "शवों को सामान्यतः <strong>उत्तर-दक्षिण दिशा</strong> में लिटाया जाता था, जिसमें सिर उत्तर की ओर और पैर दक्षिण की ओर होते थे।",
                "icon": "fa-compass"
            }
        ]
    },
    "deepDive": {
        "title": "पाठ्यक्रम मुख्य नोट्स (गहन अध्ययन)",
        "description": "सिंधु घाटी सभ्यता की धार्मिक मूर्तिकला, जीववाद, अनुष्ठानों और शवाधान प्रथाओं का गहन अध्ययन करें।",
        "sections": [
            {
                "title": "1. पशुपति मुहर, मातृदेवी और पुरुष/स्त्री देवता",
                "content": """<p>हड़प्पा धर्म का पुनर्निर्माण मुख्य रूप से मुहरों और मिट्टी की मूर्तियों के आधार पर किया गया है, जो बिना किसी मंदिर वास्तुकला के घरेलू स्तर पर पूजे जाने वाले देवताओं को दर्शाते हैं।</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-ring"></i> पशुपति मुहर (आदि-शिव)</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>खोज और रूप:</strong> मोहनजोदड़ो से प्राप्त सेलखड़ी की इस मुहर में एक पुरुष देवता को योगासन मुद्रा (पद्मासन) में दिखाया गया है, जिन्होंने सींगों वाला मुकुट पहना है।</li>
      <li><strong>चारों ओर के जानवर:</strong> इनके दाहिनी ओर एक **हाथी** और **बाघ** है, तथा बाईं ओर एक **गैंडा** और **भैंसा** है। सिंहासन के नीचे **दो हिरण** बने हैं।</li>
      <li><strong>व्याख्या:</strong> जॉन मार्शल ने इसे *आदि-शिव (Proto-Shiva)* कहा। आधुनिक विद्वानों का मानना है कि यह कोई वैदिक देवता या वन्य पशुओं का स्वामी है।</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-female"></i> मातृदेवी की पूजा और मंदिरों का अभाव</div>
    <p style="font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;">
      **मातृदेवी:** मिट्टी से बनी नारी की खड़ी मूर्तियां मोहनजोदड़ो और हड़प्पा में प्रचुर मात्रा में मिली हैं। इनके सिर के दोनों ओर प्याले जैसे आकार बने हैं, जिन पर जमा कालिख यह दर्शाती है कि घरों में इनके समक्ष तेल के दीये जलाए जाते थे।
      <br>**मंदिरों का अभाव:** मिस्र और मेसोपोटामिया के विपरीत, हड़प्पा सभ्यता में किसी भी प्रकार के मंदिर या सार्वजनिक धार्मिक भवन का कोई पुरातात्विक साक्ष्य नहीं मिला है।
    </p>
  </div>
</div>""",
                "masteryZone": []
            },
            {
                "title": "2. जीववाद (Animism), वृक्ष व पशु पूजा और मिश्रित धार्मिक रूप",
                "content": """<p>हड़प्पा वासी प्रकृति की शक्तियों के आराधक थे। वे पेड़ों, पशुओं और मिश्रित काल्पनिक जीवों में दिव्य शक्तियों का वास मानते थे।</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-tree"></i> पीपल वृक्ष की पूजा और मिश्रित आकृतियां</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>पीपल वृक्ष पूजा:</strong> पीपल (Ficus religiosa) को अत्यंत पवित्र माना जाता था। एक मुहर पर पीपल की टहनियों के बीच एक देवता को खड़ा दिखाया गया है और एक उपासक घुटने टेके हुए है, जिसके नीचे सात आकृतियाँ खड़ी हैं।</li>
      <li><strong>मिश्रित जीव (Therianthropes):</strong> मुहरों पर बाघ के धड़ वाले मानव और तीन सिरों (एक सींग वाला सांड, बैल, हिरण) वाले काल्पनिक जीवों का अंकन उनके समृद्ध मिथकों को दर्शाता है।</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-water"></i> पशु पूजा और धार्मिक जल-स्नान</div>
    <p style="font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;">
      **पशु पूजा:** मुहरों पर सबसे अधिक अंकन काल्पनिक **'एक सींग वाले पशु' (Unicorn)** का है जिसके आगे एक पात्र (धूपदानी) रखा होता था। **कूबड़ वाला सांड (Zebu)** भी अत्यंत सजीव रूप में उकेरा गया है।
      <br>**विशाल स्नानागार:** मोहनजोदड़ो के दुर्ग पर बना यह जलाशय जिप्सम और तारकोल (bitumen) से जलरोधी बनाया गया था। इसका उपयोग अनुष्ठानिक एवं सामूहिक स्नान के लिए किया जाता था।
    </p>
  </div>
</div>""",
                "masteryZone": []
            },
            {
                "title": "3. शवाधान प्रथाएं, अग्नि वेदियाँ और अनुष्ठानिक वास्तुकला",
                "content": """<p>शवों को दफनाने और यज्ञ वेदियों की खोज से परलोक जीवन की अवधारणा और यज्ञीय अनुष्ठानों के क्षेत्रीय अंतर प्रकट होते हैं।</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-bed"></i> शवाधान प्रथाओं के प्रकार</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>पूर्ण समाधिकरण:</strong> शव को जमीन में बने आयताकार गड्ढे में उत्तर-दक्षिण (सिर उत्तर की ओर) लिटाकर दफनाना सबसे आम था। कब्रों में मिट्टी के बर्तन, तांबे के दर्पण और मालाएं रखी जाती थीं।</li>
      <li><strong>लकड़ी का ताबूत:</strong> हड़प्पा के कब्रिस्तान R-37 से देवदार की लकड़ी के ताबूत में बंद शव मिला है।</li>
      <li><strong>लोथल का जुड़वां शवाधान:</strong> लोथल की तीन कब्रों से दो-दो शवों को एक साथ दफनाने के साक्ष्य मिले हैं।</li>
      <li><strong>कालीबंगन के प्रतीकात्मक शवाधान:</strong> ऐसे गड्ढे मिले हैं जिनमें केवल बर्तन रखे हैं, मानव कंकाल नहीं।</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-fire"></i> अग्नि वेदियाँ और ताबीज</div>
    <p style="font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;">
      **अग्नि वेदियाँ:** **कालीबंगन** और **लोथल** से मिट्टी की ईंटों से बनी चौकोर और अंडाकार अग्नि वेदियाँ (यज्ञ कुंड) मिली हैं, जिनमें कोयला, राख और पालतू पशुओं की हड्डियों के टुकड़े मिले हैं, जो अग्नि बलि को दर्शाते हैं।
      <br>**ताबीज:** बड़ी संख्या में प्राप्त मिट्टी और सेलखड़ी के ताबीज (amulets) यह संकेत देते हैं कि हड़प्पा समाज में बुरी आत्माओं और जादू-टोने का डर व्याप्त था।
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
        "Consider the following statements regarding the Pashupati Seal of the Indus Valley Civilisation:\n1. It was excavated from the lower town area of Harappa.\n2. The seated deity is depicted wearing a horned headgear and is shown in a yogic posture.\n3. The four wild animals surrounding the deity are the elephant, tiger, rhinoceros, and buffalo.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        1,
        "Statement 1 is incorrect: the Pashupati Seal was excavated at Mohenjo-daro, not Harappa. Statements 2 and 3 are correct."
    ),
    (
        "With reference to the terracotta Mother Goddess figurines of the Harappan Civilisation, consider the following statements:\n1. They are highly standardized, manufactured in two-part clay molds to achieve identical features.\n2. The cup-like panniers on the sides of their headdresses often contain soot stains, indicating use as oil lamps.\n3. These figurines are found abundantly in both domestic dwellings and monumental public temples.\nWhich of the statements given above is/are correct?",
        ["2 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statement 2 is correct. Statement 1 is incorrect: they were modeled by hand, not in molds. Statement 3 is incorrect: no temples have ever been found in the Harappan civilization."
    ),
    (
        "Consider the following statements regarding the nature and tree worship practiced by the Harappans:\n1. The Pipal tree (Ficus religiosa) was considered sacred and is depicted with horned deities on seals.\n2. Neem and Banyan leaves were the exclusive motifs painted on Harappan black-on-red pottery.\n3. A unique seal depicts a line of seven figures wearing long tunics standing below a tree deity.\nWhich of the statements given above is/are correct?",
        ["1 and 3 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 3 are correct. Statement 2 is incorrect: Pipal and palm leaves were common, but not Neem/Banyan exclusively."
    ),
    (
        "With reference to the Great Bath of Mohenjo-daro, consider the following statements:\n1. It was constructed using burnt bricks, gypsum mortar, and sealed with a layer of bitumen to prevent leakage.\n2. The pool was filled with water supplied from a nearby large well, and drained via a vaulted brick conduit.\n3. It was situated in the Lower Town area to cater to the daily household washing needs of commoners.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: the Great Bath was located on the Citadel mound, implying it was used for special elite purificatory or public rituals."
    ),
    (
        "Consider the following statements regarding Harappan burial practices:\n1. Extended inhumation in a North-South direction, with the head to the North, was the most common burial method.\n2. Grave goods included painted pottery, copper mirrors, beads, and food vessels, indicating belief in life after death.\n3. Bodies of commoners were cremated in open brick kilns, while only elites were buried in pits.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: burial was widespread; there is no evidence of elite-only cremation in brick kilns."
    ),
    (
        "With reference to the fire altars discovered in the Indus Valley Civilisation, consider the following statements:\n1. Clay-lined fire pits have been excavated at Surkotada and Dholavira.\n2. The fire altars contain ash, charcoal, and terracotta triangular cakes, suggesting sacrificial or domestic rituals.\n3. Animal bone fragments found within some of these altars indicate the practice of animal sacrifice.\nWhich of the statements given above is/are correct?",
        ["2 and 3 only", "2 only", "1 and 3 only", "1, 2 and 3"],
        0,
        "Statements 2 and 3 are correct. Statement 1 is incorrect: fire altars have been found at Kalibangan and Lothal, not Surkotada or Dholavira."
    ),
    (
        "Consider the following statements regarding the Lothal double burials:\n1. Three grave pits were excavated at Lothal, each containing two skeletons buried together.\n2. The double burials have been confirmed by physical anthropologists to represent only male-female couples.\n3. The twin burials are widely cited as definitive, undisputed evidence of the practice of Sati in the Bronze Age.\nWhich of the statements given above is/are correct?",
        ["1 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statement 1 is correct. Statement 2 is incorrect: sex determination of the skeletons in some double burials is contested. Statement 3 is incorrect: they are not definitive evidence of Sati and other explanations exist."
    ),
    (
        "With reference to Surkotada and Kalibangan funerary variations, consider the following statements:\n1. Surkotada yielded evidence of pot/urn burials containing cremated bone fragments.\n2. Kalibangan has revealed symbolic burials containing rich offerings of pottery and beads but no human remains.\n3. Clay-brick lined graves, forming a small structural tomb, were discovered at Harappa.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All three statements are correct, describing Surkotada pot burials, Kalibangan symbolic graves, and Harappan brick tombs."
    ),
    (
        "Consider the following statements regarding the Unicorn motif on Harappan seals:\n1. It is the most common animal representation, depicted as a mythical one-horned animal in profile.\n2. The Unicorn is invariably placed in front of a standard or manger, interpreted as an incense burner or cult object.\n3. Modern DNA studies of seal residues show that the Unicorn was a real, domestic bovine species that went extinct.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: the Unicorn is a mythical, composite animal, and no DNA studies exist on seal stones."
    ),
    (
        "With reference to the therianthropic representations in Harappan art, consider the following statements:\n1. Therianthropes are hybrid composite creatures combining human and animal features.\n2. A famous seal depicts a horned human figure with the body of a tiger and hooves of a bull.\n3. These composite figures are believed to represent protective deities or mythological spirits.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, detailing hybrid therianthropic creatures on Harappan seals."
    ),
    (
        "Consider the following statements regarding the comparative religion of the ancient world:\n1. Like Mesopotamian temples (Ziggurats), Harappan cities had massive central structures for patron deities.\n2. Harappan religious practice appears to have been decentralized, focusing on domestic rituals and nature spirits.\n3. The civic administration of Harappa was led by a class of temple priests, similar to the Egyptian pharaohs.\nWhich of the statements given above is/are correct?",
        ["2 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statement 2 is correct. Statements 1 and 3 are incorrect: Harappa lacked temples and there is no evidence of a ruling priestly class similar to Egypt."
    ),
    (
        "With reference to Harappan amulets and magical beliefs, consider the following statements:\n1. Numerous small tablets made of terracotta and faience have been found, functioning as protective amulets.\n2. Some amulets depict deities fighting wild beasts, which scholars link to Mesopotamian Gilgamesh myths.\n3. The complete absence of weapons in graves proves that Harappans relied on magic to protect them from invaders.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        1,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: weapons were found in houses, but they were simple, and graves generally did not contain weapons."
    ),
    (
        "Consider the following statements regarding the historical debate over the Pashupati Seal:\n1. Sir John Marshall proposed that the seal depicts 'Proto-Shiva' because of the yogic pose, horns, and wild animals.\n2. Doris Srinivasan argued that the figure is a composite human-bovine deity representing Vedic Rudra.\n3. S.R. Rao deciphered the inscription on the seal as containing the name of 'Mahadeva'.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: the Indus script remains undeciphered, and no consensus exists on Rao's readings."
    ),
    (
        "With reference to the terracotta triangular cakes, consider the following statements:\n1. They are commonly found in domestic hearths and fire altars at Kalibangan and Lothal.\n2. They were likely used as heat-retaining devices for cooking or as symbolic offerings in rituals.\n3. All terracotta cakes were inscribed with pictographic prayers in the Indus script.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: the vast majority of terracotta cakes are uninscribed and plain."
    ),
    (
        "Consider the following statements regarding the Surkotada pot burials:\n1. They represent fractional burials, where human bones were collected after exposure and placed inside large pots.\n2. Pot burials were accompanied by grave goods like small pots, indicating they were part of regular funerary rites.\n3. Surkotada pot burials are unique because they were placed in circular stone-cairn circles.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, describing Surkotada's unique fractional pot burials and cairn stone markings."
    ),
    (
        "With reference to the animal symbols on Harappan seals, consider the following statements:\n1. The humped bull (Zebu) is rendered with great artistic realism and is associated with strength and fertility.\n2. Animals like tigers, elephants, and rhinos are depicted, showing familiarity with jungle fauna.\n3. Domestic dogs and horses are the most common animals depicted on Harappan square seals.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: dogs and horses are extremely rare on seals; the unicorn and humped bull are the most common."
    ),
    (
        "Consider the following statements regarding the source of water for the Great Bath of Mohenjo-daro:\n1. A large brick-lined double-ringed well in an adjacent room supplied water to the Bath.\n2. Water was drawn directly from the Indus River through an open stone canal.\n3. The pool was cleaned regularly by draining the water through a large corbelled arch drain.\nWhich of the statements given above is/are correct?",
        ["1 and 3 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 3 are correct. Statement 2 is incorrect: water was not drawn directly from the river, but from a nearby well to ensure clean water."
    ),
    (
        "With reference to the use of steatite in Harappan seals, consider the following statements:\n1. Steatite is a soft talcose soapstone that was easily carved with metal tools.\n2. After carving, seals were coated with a chemical slip and fired in a kiln to harden them.\n3. Firing converted the steatite into a white, durable, glazed surface.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, describing steatite carving, firing, and glazing process."
    ),
    (
        "Consider the following statements regarding the regional variations in Harappan funerary customs:\n1. Harappa has yielded wooden coffin burials in Cemetery R-37.\n2. Lothal is unique for its double burials in a single pit.\n3. Kalibangan is characterized by symbolic pot burials containing offering vessels but no skeletons.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, summarizing key regional funerary variations."
    ),
    (
        "With reference to the stone and clay 'ring stones' and phallic objects, consider the following statements:\n1. Large stone rings found at Mohenjo-daro are interpreted by some scholars as yoni symbols.\n2. Small terracotta cylindrical objects are believed by Marshall to represent phallic lingas.\n3. Modern scholars like George Dales argue that ring stones were architectural column bases, not ritual icons.\nWhich of the statements given above is/are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, outlining Marshall's ritual interpretation and Dales' architectural critique."
    ),
    (
        "Consider the following statements regarding Harappan religious beliefs in the afterlife:\n1. The presence of mirrors and cosmetic pots in graves suggests belief in the bodily resurrection of the deceased.\n2. Pots containing grain and food items were placed in graves to sustain the deceased in the journey beyond.\n3. Scribes recorded funerary prayers on the wooden coffins using a standard black paint.\nWhich of the statements given above is/are correct?",
        ["2 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statement 2 is correct. Statement 1 is incorrect: grave goods show belief in an afterlife, but not necessarily physical resurrection. Statement 3 is incorrect: no readable prayers or script have been found on coffins."
    ),
    (
        "With reference to the Horned Deity motif in Harappan iconography, consider the following statements:\n1. Horned deities are shown on seals wearing three-pointed or buffalo-horned headdresses.\n2. A terracotta tablet from Kalibangan depicts a horned deity on one side and a sacrificial scene on the other.\n3. Horned headgears were restricted to male figures and never worn by female figures.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: horned headdresses are also worn by female figures (like the deity inside the Pipal tree)."
    ),
    (
        "Consider the following statements regarding the Harappan Priest-King bust:\n1. It is carved from soft steatite and shows a stylized beard and a trefoil-patterned shawl.\n2. Some historians suggest the trefoil motif has a religious or astral significance, similar to Mesopotamian designs.\n3. The eyes are inlaid with shell and are half-closed, suggesting a meditative or trance-like state.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, detailing the Priest-King bust characteristics and comparative motifs."
    ),
    (
        "With reference to the sacrificial pit at Kalibangan, consider the following statements:\n1. It consists of a brick-lined pit containing animal bones, ash, and charcoal on a raised mud platform.\n2. Scribes recorded the names of the sacrificed animals on copper tablets found near the pit.\n3. The platform was surrounded by rooms, which were likely used by priests for preparation.\nWhich of the statements given above is/are correct?",
        ["1 and 3 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 3 are correct. Statement 2 is incorrect: there are no readable texts or tables describing sacrifices."
    ),
    (
        "Consider the following statements regarding Harappan religious continuity in later India:\n1. Tree worship, especially of the Pipal, continues as a sacred practice in Buddhism and Hinduism.\n2. The Pashupati seal is widely cited as the earliest representation of the yogic posture and Shiva.\n3. The double burial at Lothal is considered the direct antecedent of the medieval Sati practice.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: linking Lothal's double burial to the medieval Sati practice is highly speculative and lacks historical/stratigraphical continuity."
    ),
    (
        "With reference to the terracotta Mother Goddess figurines, consider the following statements:\n1. They are found in large numbers at Mohenjo-daro and Harappa.\n2. They are virtually absent at sites in Gujarat and Rajasthan, like Lothal and Kalibangan.\n3. This geographical variation suggests that religious cults differed across the Harappan civilization.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All three statements are correct, detailing the regional abundance of Mother Goddess figurines in the Indus valley and their absence in Gujarat/Rajasthan."
    ),
    (
        "Consider the following statements regarding the Harappan belief in malevolent spirits:\n1. Small clay tablets depicting protective animal figures were used as amulets to ward off evil.\n2. Scribes wore copper bracelets inscribed with protective mantras in the Indus script.\n3. The presence of bent copper rods in graves was a ritual practice to prevent the dead from rising.\nWhich of the statements given above is/are correct?",
        ["1 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statement 1 is correct. Statements 2 and 3 are incorrect: there are no bracelets with readable mantras or ritual bent copper rods to stop the dead from rising."
    ),
    (
        "With reference to the Great Bath as a ritual structure, consider the following statements:\n1. The Bath is surrounded by corridors on three sides and a row of changing rooms on the north.\n2. A staircase led down into the pool from the north and south ends.\n3. The water was kept clean by a continuous flow from the adjacent Indus River channel.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: water was not fed from the river channel directly, but from a large well inside the complex."
    ),
    (
        "Consider the following statements regarding Harappan funerary pottery:\n1. Pottery placed in graves was painted with black-on-red designs, often matching domestic ware.\n2. Offering jars were filled with food and water to sustain the deceased in the afterlife.\n3. Scribes broke the pottery ritually before placing it in the graves to release its spirit.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: pottery found in graves is intact and complete, not ritually broken."
    ),
    (
        "With reference to the clay-lined fire altars of Kalibangan, consider the following statements:\n1. A series of seven fire altars were found on a mud-brick platform inside the Citadel.\n2. The altars contained cylindrical clay pillars in the center, surrounded by ash and charcoal.\n3. These altars show that public sacrificial fire rituals were central to Kalibangan's civic life.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, describing Kalibangan's public fire altars, central clay pillars, and civic rituals."
    ),
    (
        "Consider the following statements regarding animal symbolism on seals:\n1. The Unicorn is the most frequently depicted animal, appearing on more than 60% of all seals.\n2. The humped bull is depicted with a highly pronounced hump, representing strength and agricultural power.\n3. Animals like the tiger and rhinoceros are rarely shown in realistic poses, showing they were mythical beasts.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: tigers and rhinos are depicted realistically, reflecting familiarity with the marshy jungle fauna of the Indus basin."
    ),
    (
        "With reference to the Harappan wooden coffin burial, consider the following statements:\n1. It was excavated in the R-37 cemetery at Harappa.\n2. The coffin was made of local rosewood, which is highly resistant to insects.\n3. The shroud of the deceased was made of cotton fabric, preserved by copper salts in the grave.\nWhich of the statements given above is/are correct?",
        ["1 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statement 1 is correct. Statement 2 is incorrect: the coffin was made of deodar wood. Statement 3 is incorrect: there is no cotton shroud preserved by copper salts in this specific grave."
    ),
    (
        "Consider the following statements regarding the Great Bath complex:\n1. The tank floor was made of flat-laid bricks set in gypsum mortar, backed by a thick layer of bitumen.\n2. Small rooms surrounding the Bath each contained a private brick-lined bathing platform.\n3. The entire complex was enclosed by massive fortifications to restrict entry to high priests.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: while it was on the fortified Citadel, there is no evidence that entry was restricted exclusively to 'high priests' by massive internal fortifications."
    ),
    (
        "With reference to the Kalibangan symbolic burials, consider the following statements:\n1. The graves are circular or rectangular pits containing only pottery, ornaments, and offerings.\n2. These symbolic burials have been interpreted as cenotaphs for individuals who died elsewhere.\n3. The offering pottery was painted with black geometric patterns on a red slip.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, outlining symbolic burials, their interpretation as cenotaphs, and the pottery style."
    ),
    (
        "Consider the following statements regarding the therianthropic tiger-man seal:\n1. It depicts a human head with horns, a tiger body, and a bovine tail.\n2. It represents a common mythological theme of shape-shifting or protective spirits in Harappan folklore.\n3. It was used exclusively by tiger hunters as a protective hunting charm.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: we do not know if it was used exclusively by tiger hunters; seals were general administrative/trade markers."
    ),
    (
        "With reference to the Pipal tree deity seal, consider the following statements:\n1. It depicts a figure standing inside a U-shaped branch of a Pipal tree, wearing a horned headdress.\n2. A worshipper is shown kneeling before the tree, with a human-headed goat behind them.\n3. Below the scene, a row of seven figures wearing tunics and feathers in their hair stand in a line.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, describing the iconic tree-worship seal components."
    ),
    (
        "Consider the following statements regarding the Surkotada cairn burials:\n1. Graves were covered with a low mound of stones (cairn) and marked by a large vertical stone block.\n2. This practice shows megalithic influence, suggesting contact with Southern Indian cultures.\n3. The graves contained urns filled with ashes and bone fragments, indicating fractional burial.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, detailing Surkotada's stone cairns, megalithic influence, and urn burials."
    ),
    (
        "With reference to Harappan clay tablets depicting mythological scenes, consider the following statements:\n1. A tablet from Mohenjo-daro depicts a figure seated on a tree holding back two tigers with his hands.\n2. This scene is structurally similar to the Mesopotamian Gilgamesh epic of subduing wild beasts.\n3. These tablets were used as currency to pay temple priests for performing rituals.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: there is no evidence of currency or temple priests in Harappa."
    ),
    (
        "Consider the following statements regarding Harappan funerary ornaments:\n1. Shell bangles, copper rings, and jasper beads are frequently found on the skeletons in graves.\n2. Skeletons are sometimes found wearing gold crowns and heavy silver armor.\n3. Funerary jewelry was generally simple, showing that the most valuable items were passed down to heirs.\nWhich of the statements given above is/are correct?",
        ["1 and 3 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 3 are correct. Statement 2 is incorrect: gold crowns and silver armor have never been found in Harappan graves."
    ),
    (
        "With reference to the Kalibangan fire altars in houses, consider the following statements:\n1. Many houses in the Lower Town contained private fire altars in their courtyards.\n2. The altars were rectangular clay-lined pits, containing a central clay column, ash, and charcoal.\n3. The presence of private altars shows that fire worship was practiced domestically, not just in public platforms.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, describing domestic fire altars in Kalibangan."
    ),
    (
        "Consider the following statements regarding animal cults on seals:\n1. The Unicorn is always depicted with a two-tiered standard or incense burner before it.\n2. The humped bull is never depicted with a standard, suggesting it had a different symbolic status.\n3. Tiger and elephant seals are often found with manger-like objects placed before them.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: tiger and elephant seals never feature standard/manger objects."
    ),
    (
        "With reference to the Harappan wooden coffin burial, consider the following statements:\n1. The coffin was wrapped in a reed shroud and placed in a grave pit surrounded by pottery.\n2. A copper mirror was found placed near the head of the female skeleton inside the coffin.\n3. Scribes inscribed the name of the deceased on the lid using a sharp bronze chisel.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: no inscription is present on the wooden lid."
    ),
    (
        "Consider the following statements regarding the purificatory platforms at Mohenjo-daro:\n1. A series of bathing platforms were situated near the Great Bath, each with its own drain.\n2. These platforms suggest that physical cleanliness was a prerequisite for participating in Citadel rituals.\n3. The platforms were made of wood coated with a water-resistant resin.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: platforms were made of fired bricks, not wood."
    ),
    (
        "With reference to the Kalibangan double burials, consider the following statements:\n1. Unlike Lothal, Kalibangan did not yield any double burials in its cemeteries.\n2. Kalibangan burials are characterized by distinct circular pits containing urns and offerings.\n3. Urn burials at Kalibangan represent fractional burials of bones gathered after exposure.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, summarizing Kalibangan's burial features."
    ),
    (
        "Consider the following statements regarding the multi-headed composite animals on seals:\n1. A seal from Mohenjo-daro depicts a beast with three heads: a unicorn, a humped bull, and a short-horned bull.\n2. Another seal shows a single body with three heads of a unicorn, a tiger, and a mountain goat.\n3. These seals were likely used by merchant guilds to represent a joint partnership of three traders.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: the guild partnership theory is speculative, and the primary interpretation is mythological."
    ),
    (
        "With reference to the tree deities of Harappa, consider the following statements:\n1. The deity inside the Pipal tree is depicted wearing a horned headgear, showing divine status.\n2. The seven figures below the tree deity are shown wearing long tunics, bangles, and a single feather in their hair.\n3. Tree worship was restricted to the Pipal, and no other tree species are depicted on seals.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: other trees, like acacia and palm trees, are occasionally depicted."
    ),
    (
        "Consider the following statements regarding the Surkotada funerary offerings:\n1. Large storage jars containing beads, shells, and pottery were placed next to the burial urns.\n2. Graves were covered with heavy stone slabs, mimicking the dolmens of the historical phase.\n3. Scribes buried copper weapons with the deceased to protect them in the afterlife.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: weapons were not buried with the deceased at Surkotada."
    ),
    (
        "With reference to the Mesopotamian comparative text references, consider the following statements:\n1. Cuneiform texts refer to trade with Meluhha, which is widely identified as the Indus Valley.\n2. The texts mention importing raw lapis lazuli, ivory, and exotic birds from Meluhha.\n3. The texts contain descriptions of the religious rituals performed by Indus priests in Meluhhan temples.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: Mesopotamian texts mention trade goods, but do not describe Harappan religious rituals or temples."
    ),
    (
        "Consider the following statements regarding the grave goods in Harappan burials:\n1. The number of pottery vessels placed in a grave could range from a few to over several dozen.\n2. Highly valuable items like gold necklaces and bronze vessels are extremely rare in graves.\n3. This pattern suggests that Harappan society did not practice excessive wealth display in burials.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All three statements are correct, detailing the quantity, rarity, and social implications of grave goods."
    ),
    (
        "With reference to the Kalibangan raised platform altars, consider the following statements:\n1. Clay-lined altars were built on top of mud-brick platforms inside the Citadel mound.\n2. The platform was accessed by a flight of brick stairs, suggesting a formal, public ritual space.\n3. Scribes carved geometric drawings on the platform floors to demarcate ritual seating.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: no drawings or inscriptions are carved on the floors."
    )
]

practice_data_hin = [
    (
        "सिंधु घाटी सभ्यता की पशुपति मुहर के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह हड़प्पा के निचले शहर (lower town) क्षेत्र से खोजी गई थी।\n2. आसीन देवता को सींग वाला मुकुट पहने हुए और योगासन मुद्रा में दिखाया गया है।\n3. देवता को घेरे हुए चार जंगली जानवर हाथी, बाघ, गैंडा और भैंसा हैं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1 और 2 केवल", "2 और 3 केवल", "1 और 3 केवल", "1, 2 और 3"],
        1,
        "कथन 1 गलत है: पशुपति मुहर मोहनजोदड़ो से मिली थी, हड़प्पा से नहीं। कथन 2 और 3 सही हैं।"
    ),
    (
        "हड़प्पा सभ्यता की मिट्टी की मातृदेवी की मूर्तियों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. ये अत्यधिक मानकीकृत हैं और समान आकृतियों को प्राप्त करने के लिए दो-भाग वाले सांचों में बनाई गई थीं।\n2. उनके मुकुट के दोनों ओर बने प्यालेनुमा आकारों में अक्सर कालिख के निशान मिले हैं, जो दीपक के रूप में उपयोग को दर्शाते हैं।\n3. ये मूर्तियाँ घरेलू आवासों और विशाल सार्वजनिक मंदिरों दोनों में प्रचुर मात्रा में मिली हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["2 केवल", "1 और 2 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 2 सही है। कथन 1 गलत है क्योंकि इन्हें हाथ से बनाया गया था, सांचे से नहीं। कथन 3 गलत है क्योंकि हड़प्पा सभ्यता में कोई मंदिर नहीं मिला है।"
    ),
    (
        "हड़प्पा वासियों द्वारा की जाने वाली प्रकृति और वृक्ष पूजा के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. पीपल के वृक्ष (Ficus religiosa) को पवित्र माना जाता था और मुहरों पर इसे सींग वाले देवताओं के साथ चित्रित किया गया है।\n2. नीम और बरगद के पत्ते हड़प्पा के लाल-काले बर्तनों पर चित्रित एकमात्र रूपांकन थे।\n3. एक विशिष्ट मुहर में पीपल वृक्ष के देवता के नीचे लंबे लबादे पहने सात आकृतियों को खड़ा दिखाया गया है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 3 केवल", "1 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 3 सही हैं। कथन 2 गलत है क्योंकि पीपल और ताड़ के पत्ते आम थे, नीम/बरगद नहीं।"
    ),
    (
        "मोहनजोदड़ो के विशाल स्नानागार (Great Bath) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इसका निर्माण पकी ईंटों, जिप्सम गारे से किया गया था और रिसाव रोकने के लिए कोलतार (bitumen) की परत चढ़ाई गई थी।\n2. जलाशय को पास के एक बड़े कुएं से पानी की आपूर्ति की जाती थी, और पानी की निकासी एक ढकी हुई नाली से होती थी।\n3. यह निचले शहर के क्षेत्र में स्थित था ताकि आम लोगों की दैनिक नहाने की ज़रूरतों को पूरा किया जा सके।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 2 केवल", "2 और 3 केवल", "1 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि विशाल स्नानागार दुर्ग (Citadel) पर स्थित था, जो इसके अनुष्ठानिक और विशेष उपयोग को दर्शाता है।"
    ),
    (
        "हड़प्पा की शवाधान प्रथाओं के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. उत्तर-दक्षिण दिशा में शव को सीधा लिटाकर दफनाना सबसे आम तरीका था, जिसमें सिर उत्तर की ओर होता था।\n2. कब्रों में चित्रित मृदभांड, तांबे के दर्पण, मनके और खाने के बर्तन रखे जाते थे, जो मरणोपरांत जीवन में विश्वास दर्शाते हैं।\n3. आम लोगों के शवों को ईंटों के भट्ठा में जलाया जाता था, जबकि केवल संभ्रांत लोगों को कब्रों में दफनाया जाता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 2 केवल", "1 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि शवाधान आम था; भट्ठों में जलाने के कोई साक्ष्य नहीं हैं।"
    ),
    (
        "सिंधु घाटी सभ्यता में खोजी गई अग्नि वेदियों (यज्ञ कुंडों) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. सुरकोटदा और धोलावीरा से मिट्टी की अग्नि वेदियाँ मिली हैं।\n2. इन अग्नि वेदियों में राख, कोयला और मिट्टी के त्रिकोणीय केक मिले हैं, जो यज्ञीय या घरेलू अनुष्ठानों का संकेत देते हैं।\n3. इन वेदियों में मिले पशुओं की हड्डियों के टुकड़े पशु बलि की प्रथा की ओर इशारा करते हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["2 और 3 केवल", "2 केवल", "1 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 2 और 3 सही हैं। कथन 1 गलत है क्योंकि अग्नि वेदियाँ कालीबंगन और लोथल से मिली हैं, सुरकोटदा या धोलावीरा से नहीं।"
    ),
    (
        "लोथल के जुड़वां/डबल शवाधान के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. लोथल से तीन कब्रें मिली हैं, जिनमें से प्रत्येक में दो शवों को एक साथ दफनाया गया था।\n2. शारीरिक मानवविज्ञानियों ने यह पुष्टि की है कि ये जुड़वां शवाधान केवल पुरुष-महिला जोड़ों के ही थे।\n3. इन जुड़वां कब्रों को कांस्य युग में सती प्रथा के अस्तित्व के अकाट्य और निर्विवाद साक्ष्य के रूप में उद्धृत किया जाता है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 केवल", "1 और 2 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 सही है। कथन 2 गलत है क्योंकि कुछ कंकालों का लिंग निर्धारण अभी भी विवादित है। कथन 3 गलत है क्योंकि इन्हें सती प्रथा का अकाट्य साक्ष्य नहीं माना जा सकता, इसके अन्य कारण भी हो सकते हैं।"
    ),
    (
        "सुरकोटदा और कालीबंगन की शवाधान विविधताओं के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. सुरकोटदा से कलश शवाधान (pot burials) के साक्ष्य मिले हैं जिनमें हड्डियों के अवशेष थे।\n2. कालीबंगन से प्रतीकात्मक कब्रें मिली हैं जिनमें बर्तन और आभूषण तो थे लेकिन कोई मानव कंकाल नहीं था।\n3. हड़प्पा से पकी ईंटों से बनी कब्र (ईंटों का ताबूत) मिली है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "1 और 2 केवल", "2 और 3 केवल", "1 और 3 केवल"],
        0,
        "तीनों कथन सही हैं, जो सुरकोटदा के कलश शवाधान, कालीबंगन की प्रतीकात्मक कब्रों और हड़प्पा की ईंटों वाली कब्रों का वर्णन करते हैं।"
    ),
    (
        "हड़प्पा की मुहरों पर एक सींग वाले पशु (Unicorn) के रूपांकन के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह सबसे आम पशु चित्रण है, जिसे एक काल्पनिक सींग वाले जानवर के रूप में दिखाया गया है।\n2. इस पशु के आगे हमेशा एक धूपदानी या पंखा जैसा पात्र रखा होता है, जिसे धार्मिक प्रतीक माना जाता है।\n3. आधुनिक अध्ययनों से सिद्ध हुआ है कि एक सींग वाला पशु एक वास्तविक बैल प्रजाति थी जो बाद में विलुप्त हो गई।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 2 केवल", "1 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि यह एक पौराणिक जीव है और इसके वास्तविक होने का कोई साक्ष्य नहीं है।"
    ),
    (
        "हड़प्पा कला में मिश्रित मानव-पशु (Therianthropic) आकृतियों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. ये मिश्रित आकृतियां मानव और पशु दोनों के शारीरिक लक्षणों को जोड़ती हैं।\n2. एक प्रसिद्ध मुहर में बाघ के शरीर, बैल के खुरों और सींग वाले मानव सिर वाली आकृति बनी है।\n3. माना जाता है कि ये मिश्रित आकृतियां रक्षक देवताओं या पौराणिक आत्माओं को दर्शाती थीं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "1 और 2 केवल", "2 और 3 केवल", "1 और 3 केवल"],
        0,
        "तीनों कथन सही हैं, जो हड़प्पा की मिश्रित मानव-पशु आकृतियों का विवरण देते हैं।"
    ),
    (
        "प्राचीन विश्व के तुलनात्मक धर्म के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मेसोपोटामिया के मंदिरों (जिग्गुरत) की तरह, हड़प्पा के शहरों में भी देवताओं के विशाल केंद्रीय मंदिर थे।\n2. हड़प्पा की धार्मिक प्रथाएं विकेंद्रीकृत प्रतीत होती हैं, जो घरेलू अनुष्ठानों और प्रकृति पूजा पर केंद्रित थीं।\n3. हड़प्पा का नागरिक प्रशासन मंदिर के पुजारियों के एक वर्ग द्वारा चलाया जाता था, जैसे मिस्र के फिरौन।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["2 केवल", "1 और 2 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 2 सही है। कथन 1 और 3 गलत हैं क्योंकि हड़प्पा में मंदिरों और शासक पुजारी वर्ग का पूर्ण अभाव था।"
    ),
    (
        "हड़प्पा के ताबीजों और जादुई विश्वासों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. पकी मिट्टी और फेयॉन्स से बने कई छोटे ताबीज मिले हैं, जो सुरक्षात्मक भूमिका निभाते थे।\n2. कुछ ताबीजों में देवताओं को जंगली जानवरों से लड़ते दिखाया गया है, जिसे गिल्गामेश मिथक से जोड़ा जाता है।\n3. कब्रों में हथियारों का न होना यह साबित करता है कि हड़प्पा वासी सुरक्षा के लिए केवल जादू-टोने पर निर्भर थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 2 केवल", "1 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि घरों में तांबे के साधारण हथियार मिले हैं, हालांकि वे कब्रों में नहीं रखे जाते थे।"
    ),
    (
        "पशुपति मुहर के ऐतिहासिक विवाद के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. सर जॉन मार्शल ने योगासन, सींगों और जंगली जानवरों के कारण इसे 'आदि-शिव' का नाम दिया था।\n2. डोरिस श्रीनिवासन ने तर्क दिया कि यह आकृति एक बैल-मानव मिश्रित देवता है जो वैदिक रुद्र को दर्शाता है।\n3. एस.आर. राव ने मुहर के शिलालेख को 'महादेव' के नाम के रूप में पढ़ा था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 2 केवल", "1 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि हड़प्पा लिपि अभी तक अपठित है और राव के वाचन पर कोई सहमति नहीं है।"
    ),
    (
        "मिट्टी के त्रिकोणीय केक (terracotta cakes) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. ये कालीबंगन और लोथल के घरेलू चूल्हों और अग्नि वेदियों में आम तौर पर पाए जाते हैं।\n2. इनका उपयोग खाना पकाने के लिए गर्मी बनाए रखने वाले उपकरणों या अनुष्ठानों में प्रतीकात्मक भेंट के रूप में किया जाता था।\n3. सभी पकी मिट्टी के केक पर सिंधु लिपि में प्रार्थनाएं खुदी हुई थीं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 2 केवल", "1 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि अधिकांश केक सादे हैं और उन पर कोई लेख नहीं है।"
    ),
    (
        "सुरकोटदा के कलश शवाधान (pot burials) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. ये आंशिक शवाधान को दर्शाते हैं, जहाँ हड्डियों को इकट्ठा करके बड़े बर्तनों में रखा जाता था।\n2. बर्तनों के साथ छोटे प्याले और तश्तरियाँ भी रखी जाती थीं, जो नियमित शवाधान अनुष्ठान का हिस्सा थीं।\n3. सुरकोटदा के कलश शवाधान पत्थरों के घेरे (cairns) से ढके पाए गए हैं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "1 और 2 केवल", "2 और 3 केवल", "1 और 3 केवल"],
        0,
        "तीनों कथन सही हैं, जो सुरकोटदा के कलश शवाधान की विशेषताओं को स्पष्ट करते हैं।"
    ),
    (
        "हड़प्पा की मुहरों पर पशु प्रतीकों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. कूबड़ वाले बैल (Zebu) का चित्रण बहुत सजीव है और यह शक्ति व उर्वरता से जुड़ा है।\n2. बाघ, हाथी और गैंडे जैसे जानवरों का चित्रण जंगली जीवों के साथ उनकी निकटता को दर्शाता है।\n3. पालतू कुत्ते और घोड़े हड़प्पा की चौकोर मुहरों पर सबसे अधिक चित्रित किए गए जानवर हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 2 केवल", "1 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि कुत्ते और घोड़े मुहरों पर अत्यंत दुर्लभ हैं; सांड और एक सींग वाला पशु सबसे आम हैं।"
    ),
    (
        "मोहनजोदड़ो के विशाल स्नानागार के पानी के स्रोत के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. स्नानागार के बगल के कमरे में स्थित एक दोहरे घेरे वाले ईंट के कुएं से पानी की आपूर्ति होती थी।\n2. पानी सीधे सिंधु नदी के एक खुले नाले से खींचा जाता था।\n3. एक बड़े मेहराबदार नाले के माध्यम से पानी बाहर निकालकर स्नानागार को नियमित साफ किया जाता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 3 केवल", "1 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 3 सही हैं। कथन 2 गलत है क्योंकि साफ पानी सुनिश्चित करने के लिए नदी के बजाय कुएं के पानी का उपयोग होता था।"
    ),
    (
        "मुहर निर्माण में सेलखड़ी (steatite) के उपयोग के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. सेलखड़ी एक नरम पत्थर है जिसे तांबे/कांस्य के उपकरणों से आसानी से तराशा जा सकता था।\n2. नक्काशी के बाद, मुहरों को भट्टी में पकाया जाता था ताकि वे कठोर हो जाएं।\n3. पकाने से सेलखड़ी की सतह सफेद, टिकाऊ और चमकीली हो जाती थी।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "1 और 2 केवल", "2 और 3 केवल", "1 और 3 केवल"],
        0,
        "तीनों कथन सही हैं, जो सेलखड़ी मुहरों के निर्माण और पकाने की प्रक्रिया का वर्णन करते हैं।"
    ),
    (
        "हड़प्पा की शवाधान प्रथाओं में क्षेत्रीय विविधताओं के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. हड़प्पा के कब्रिस्तान R-37 से देवदार की लकड़ी के ताबूत मिले हैं।\n2. लोथल एक ही गड्ढे में दो शवों को दफनाने (जुड़वां शवाधान) के लिए विशिष्ट है।\n3. कालीबंगन प्रतीकात्मक कब्रों के लिए जाना जाता है जहाँ कंकाल के बिना केवल बर्तन रखे गए थे।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "1 और 2 केवल", "2 और 3 केवल", "1 और 3 केवल"],
        0,
        "तीनों कथन सही हैं, जो क्षेत्रीय शवाधान विविधताओं को दर्शाते हैं।"
    ),
    (
        "पाषाण और मिट्टी के 'छल्लों' (ring stones) और लिंग आकारों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मोहनजोदड़ो से प्राप्त बड़े पत्थर के छल्लों को कुछ विद्वान योनी का प्रतीक मानते हैं।\n2. छोटे बेलनाकार पत्थरों को जॉन मार्शल ने लिंग पूजा का साक्ष्य माना था।\n3. जॉर्ज डेल्स जैसे आधुनिक विद्वानों का तर्क है कि ये छल्ले इमारतों के खंभों के आधार (column bases) थे, न कि धार्मिक प्रतीक।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1, 2 और 3", "1 और 2 केवल", "2 और 3 केवल", "1 और 3 केवल"],
        0,
        "तीनों कथन सही हैं, जो मार्शल की धार्मिक व्याख्या और डेल्स की वास्तुकला संबंधी आलोचना को स्पष्ट करते हैं।"
    ),
    (
        "मृत्यु के बाद के जीवन (afterlife) में हड़प्पा वासियों के विश्वास के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. कब्रों में दर्पणों और सौंदर्य प्रसाधनों का होना मृतकों के शारीरिक पुनरुत्थान (resurrection) में विश्वास दर्शाता है।\n2. कब्रों में अनाज और पानी से भरे बर्तन रखे जाते थे ताकि परलोक की यात्रा में मृत व्यक्ति को पोषण मिल सके।\n3. लेखक देवदार के ताबूतों पर काली स्याही से शवाधान की प्रार्थनाएँ लिखते थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["2 केवल", "1 और 2 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 2 सही है। कथन 1 गलत है क्योंकि सौंदर्य प्रसाधन परलोक जीवन का संकेत तो हैं, लेकिन शारीरिक पुनरुत्थान का निश्चित प्रमाण नहीं हैं। कथन 3 गलत है क्योंकि ताबूतों पर कोई लेख नहीं मिला है।"
    ),
    (
        "हड़प्पा कला में 'सींग वाले देवता' के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. सींग वाले देवताओं को मुहरों पर तीन नोक वाले या भैंसे के सींग वाले मुकुट पहने दिखाया गया है।\n2. कालीबंगन से प्राप्त एक मिट्टी की पट्टी (tablet) के एक तरफ सींग वाले देवता और दूसरी तरफ बलि का दृश्य है।\n3. सींग वाले मुकुट केवल पुरुष आकृतियों तक सीमित थे और महिलाओं द्वारा कभी नहीं पहने जाते थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 2 केवल", "1 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि पीपल वृक्ष की देवी जैसी स्त्री आकृतियों को भी सींग पहने दिखाया गया है।"
    ),
    (
        "हड़प्पा के पुरोहित-राजा (Priest-King) की अर्ध-मूर्ति के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह सेलखड़ी से बनी है और इसमें एक व्यवस्थित दाढ़ी व तिपतिया डिज़ाइन वाला शॉल दिखाया गया है।\n2. कुछ इतिहासकारों का सुझाव है कि तिपतिया डिज़ाइन का धार्मिक या खगोलीय महत्व था, जैसा मेसोपोटामिया में था।\n3. इसकी आँखें शंख की पच्चीकारी से बनी हैं और आधी बंद हैं, जो ध्यानमग्न मुद्रा को दर्शाती हैं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "1 और 2 केवल", "2 और 3 केवल", "1 और 3 केवल"],
        0,
        "तीनों कथन सही हैं, जो पुरोहित-राजा मूर्ति की शारीरिक और प्रतीकात्मक विशेषताओं को स्पष्ट करते हैं।"
    ),
    (
        "कालीबंगन में ऊंचे चबूतरे पर बनी यज्ञ वेदी के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इसमें एक ईंटों से बना गड्ढा है जिसमें मिट्टी के ऊंचे चबूतरे पर पशुओं की हड्डियाँ, राख और कोयला मिले हैं।\n2. लेखकों ने पास में मिली तांबे की पट्टियों पर बलि दिए गए जानवरों के नाम दर्ज किए थे।\n3. यह चबूतरा कुओं और स्नान करने के चबूतरे के पास था, जो अनुष्ठानिक स्नान के महत्व को दर्शाता है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 3 केवल", "1 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 3 सही हैं। कथन 2 गलत है क्योंकि कोई पठनीय तांबे की पट्टियाँ नहीं मिली हैं।"
    ),
    (
        "बाद के भारत में हड़प्पा के धार्मिक विश्वासों की निरंतरता के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. पीपल वृक्ष की पूजा बौद्ध और हिंदू धर्म में एक पवित्र प्रथा के रूप में आज भी जारी है।\n2. पशुपति मुहर को योगासन और शिव के प्रारंभिक चित्रण के रूप में व्यापक रूप से स्वीकार किया जाता है।\n3. लोथल के जुड़वां शवाधान को मध्यकालीन सती प्रथा का सीधा पूर्ववृत्त (antecedent) माना जाता है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 2 केवल", "1 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि लोथल के जुड़वां शवाधान को सती प्रथा से जोड़ना अत्यंत काल्पनिक है और इसका कोई ऐतिहासिक आधार नहीं है।"
    ),
    (
        "मिट्टी की मातृदेवी की मूर्तियों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. ये मोहनजोदड़ो और हड़प्पा में भारी संख्या में पाई गई हैं।\n2. ये गुजरात और राजस्थान के स्थलों जैसे लोथल और कालीबंगन में लगभग अनुपस्थित हैं।\n3. यह भौगोलिक भिन्नता दर्शाती है कि हड़प्पा सभ्यता के विभिन्न क्षेत्रों में धार्मिक पंथ अलग थे।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "1 और 2 केवल", "2 और 3 केवल", "1 और 3 केवल"],
        0,
        "तीनों कथन सही हैं, जो मातृदेवी की मूर्तियों के क्षेत्रीय वितरण और उनके धार्मिक निहितार्थों को दर्शाते हैं।"
    ),
    (
        "हड़प्पा वासियों के बुरी आत्माओं में विश्वास के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. सुरक्षात्मक पशु आकृतियों वाली मिट्टी की पट्टियों का उपयोग बुरी ताकतों से बचने के लिए ताबीज के रूप में किया जाता था।\n2. लेखक तांबे के कंगन पहनते थे जिन पर सुरक्षात्मक मंत्र खुदे होते थे।\n3. मृतकों को दोबारा जीवित होने से रोकने के लिए कब्रों में मुड़ी हुई तांबे की छड़ें दफनाई जाती थीं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 केवल", "1 और 2 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 सही है। कथन 2 और 3 गलत हैं क्योंकि कोई पठनीय सुरक्षात्मक मंत्र या कंकाल को रोकने वाली मुड़ी हुई छड़ें नहीं मिली हैं।"
    ),
    (
        "विशाल स्नानागार की अनुष्ठानिक वास्तुकला के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. जलाशय तीन ओर से गलियारों और उत्तर की ओर बदलने वाले कमरों की एक श्रृंखला से घिरा है।\n2. जलाशय में उतरने के लिए उत्तरी और दक्षिणी छोर पर सीढ़ियाँ बनी थीं।\n3. जलाशय में पानी पास की सिंधु नदी की नहर से लगातार बहकर आता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 2 केवल", "1 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि पानी नहर से नहीं बल्कि बगल के कमरे में स्थित कुएं से आता था।"
    ),
    (
        "कब्रों में रखे जाने वाले मिट्टी के बर्तनों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. कब्रों में रखे बर्तन लाल सतह पर काले रंग से रंगे होते थे, जो आम बर्तनों जैसे ही थे।\n2. परलोक की यात्रा में मृत व्यक्ति की सहायता के लिए इन बर्तनों में भोजन और पानी रखा जाता था।\n3. लेखक बर्तनों को कब्र में रखने से पहले उनकी आत्मा को मुक्त करने के लिए उन्हें तोड़ देते थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 2 केवल", "1 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि कब्रों में बर्तन साबुत मिले हैं, तोड़े हुए नहीं।"
    ),
    (
        "कालीबंगन की ईंटों से बनी सार्वजनिक अग्नि वेदियों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. दुर्ग (Citadel) के अंदर मिट्टी-ईंट के चबूतरे पर सात अग्नि वेदियों की एक श्रृंखला मिली है।\n2. इन वेदियों के बीच में एक मिट्टी का बेलनाकार खंभा बना था, जिसके चारों ओर राख और कोयला था।\n3. ये वेदियाँ दर्शाती हैं कि सार्वजनिक यज्ञीय अनुष्ठान कालीबंगन के नागरिक जीवन का हिस्सा थे।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "1 और 2 केवल", "2 और 3 केवल", "1 और 3 केवल"],
        0,
        "तीनों कथन सही हैं, जो कालीबंगन की सार्वजनिक वेदियों की बनावट और उनके महत्व को स्पष्ट करते हैं।"
    ),
    (
        "मुहरों पर पशु प्रतीकों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. एक सींग वाला पशु (Unicorn) सबसे अधिक चित्रित जानवर है, जो लगभग 60% मुहरों पर मिलता है।\n2. कूबड़ वाले बैल का चित्रण बड़े कूबड़ के साथ किया गया है, जो कृषि शक्ति का प्रतीक है।\n3. बाघ और गैंडे को मुहरों पर अवास्तविक रूप में दर्शाया गया है, जिससे पता चलता है कि ये काल्पनिक जीव थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 2 केवल", "1 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि बाघ और गैंडे का अंकन बहुत सजीव है, जो सिंधु बेसिन के दलदली जंगलों के जीवों से उनकी परिचितता को दर्शाता है।"
    ),
    (
        "हड़प्पा के देवदार की लकड़ी के ताबूत (wooden coffin) शवाधान के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इसे हड़प्पा के कब्रिस्तान R-37 से उत्खनित किया गया था।\n2. यह ताबूत स्थानीय देवदार (deodar) की लकड़ी से बना था।\n3. कब्र में तांबे के लवणों के कारण सूती कपड़े का कफ़न सुरक्षित बचा रहा।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 केवल", "1 और 2 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 सही है। कथन 2 भी सही है क्योंकि ताबूत देवदार का था। कथन 3 गलत है क्योंकि इस विशेष कब्र में कोई सूती कफ़न तांबे के लवणों से सुरक्षित नहीं पाया गया है।"
    ),
    (
        "विशाल स्नानागार परिसर के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. जलाशय का फर्श जिप्सम गारे में लगी चपटी ईंटों से बना था, जिसके पीछे तारकोल की मोटी परत थी।\n2. स्नानागार के पास बने छोटे कमरों में से प्रत्येक में स्नान करने का एक निजी चबूतरा बना था।\n3. प्रवेश को केवल उच्च पुजारियों तक सीमित करने के लिए पूरे परिसर को विशाल प्राचीर से घेरा गया था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 2 केवल", "1 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि स्नानागार यद्यपि दुर्ग पर था, लेकिन इसके प्रवेश पर ऐसे किसी प्रतिबंध का प्रमाण नहीं है।"
    ),
    (
        "कालीबंगन के प्रतीकात्मक शवाधान (symbolic burials) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. ये कब्रें गोल या चौकोर गड्ढे थे जिनमें केवल बर्तन, आभूषण और भेंट रखी गई थीं।\n2. इन प्रतीकात्मक कब्रों को उन लोगों के लिए बना स्मारक (cenotaphs) माना जाता है जिनकी मृत्यु कहीं और हुई थी।\n3. भेंट किए गए बर्तन लाल सतह पर काले रंग की ज्यामितीय आकृतियों से रंगे थे।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "1 और 2 केवल", "2 और 3 केवल", "1 और 3 केवल"],
        0,
        "तीनों कथन सही हैं, जो प्रतीकात्मक शवाधान, उनके महत्व और बर्तनों की शैली का वर्णन करते हैं।"
    ),
    (
        "बाघ-मानव मिश्रित मुहर (therianthropic tiger-man seal) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह सींग वाले मानव सिर, बाघ के शरीर और बैल की पूंछ वाली आकृति को दर्शाती है।\n2. यह हड़प्पा लोककथाओं में रूप बदलने वाली या रक्षक आत्माओं के पौराणिक विषय को दर्शाती है।\n3. इसका उपयोग विशेष रूप से बाघों का शिकार करने वाले शिकारी अपने ताबीज के रूप में करते थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 2 केवल", "1 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि इसका शिकारियों द्वारा विशेष उपयोग साबित नहीं है; मुहरें सामान्यतः व्यापारिक थीं।"
    ),
    (
        "पीपल वृक्ष के देवता की मुहर के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इसमें पीपल की द्विशाखित टहनी के बीच खड़े सींग वाले देवता को दिखाया गया है।\n2. देवता के सामने एक उपासक घुटने टेके हुए है, और उसके पीछे मानव सिर वाला बकरा खड़ा है।\n3. इस दृश्य के नीचे लंबे लबादे पहने और सिर पर पंख लगाए सात आकृतियां एक पंक्ति में खड़ी हैं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "1 और 2 केवल", "2 और 3 केवल", "1 और 3 केवल"],
        0,
        "तीनों कथन सही हैं, जो पीपल पूजा के इस प्रसिद्ध अंकन का विवरण देते हैं।"
    ),
    (
        "सुरकोटदा के पत्थर के घेरे (cairn) वाले शवाधान के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. कब्रों को पत्थरों के कम ऊंचे ढेर (cairn) से ढका जाता था और एक बड़े खड़े पत्थर से चिह्नित किया जाता था।\n2. यह प्रथा दक्षिण भारतीय महापाषाण (megalithic) प्रभाव की ओर इशारा करती है।\n3. इन कब्रों में राख और हड्डियों से भरे कलश दफनाए जाते थे।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "1 और 2 केवल", "2 और 3 केवल", "1 और 3 केवल"],
        0,
        "तीनों कथन सही हैं, जो सुरकोटदा के पत्थर के ढेरों, कलशों और महापाषाण संपर्कों का वर्णन करते हैं।"
    ),
    (
        "पौराणिक दृश्यों को दर्शाने वाली मिट्टी की पट्टियों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मोहनजोदड़ो से प्राप्त एक पट्टी में एक व्यक्ति को पेड़ पर बैठे और दोनों हाथों से दो बाघों को रोकते दिखाया गया है।\n2. यह दृश्य मेसोपोटामिया के गिल्गामेश महाकाव्य में जंगली जानवरों को वश में करने के दृश्य से मिलता-जुलता है।\n3. इन पट्टियों का उपयोग पुजारियों को अनुष्ठान करने के बदले मुद्रा (currency) के रूप में भुगतान करने के लिए होता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 2 केवल", "1 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि हड़प्पा में मंदिर पुजारियों या सिक्कों के साक्ष्य नहीं हैं।"
    ),
    (
        "कब्रों से प्राप्त आभूषणों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. कंकालों के हाथों में शंख की चूड़ियाँ, उंगलियों में तांबे की अंगूठियाँ और गले में जैस्पर के मनके अक्सर मिले हैं।\n2. कुछ कंकाल सोने के मुकुट और चांदी के भारी कवच पहने पाए गए हैं।\n3. कब्रों के आभूषण सामान्यतः सादे थे, जो दर्शाता है कि मूल्यवान आभूषण वारिसों को सौंप दिए जाते थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 3 केवल", "1 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 3 सही हैं। कथन 2 गलत है क्योंकि सोने के मुकुट या चांदी के कवच हड़प्पा की कब्रों से कभी नहीं मिले।"
    ),
    (
        "कालीबंगन के घरों में मिली अग्नि वेदियों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. निचले शहर के कई घरों के आंगनों में निजी अग्नि वेदियाँ मिली हैं।\n2. ये वेदियाँ मिट्टी के गड्ढे थीं जिनमें एक केंद्रीय बेलनाकार मिट्टी का खंभा और कोयला-राख था।\n3. घरों में वेदियों का होना दर्शाता है कि अग्नि पूजा केवल सार्वजनिक स्थानों पर नहीं बल्कि घरेलू स्तर पर भी होती थी।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "1 और 2 केवल", "2 और 3 केवल", "1 और 3 केवल"],
        0,
        "तीनों कथन सही हैं, जो कालीबंगन के घरों में निजी अनुष्ठानों के साक्ष्यों का विवरण देते हैं।"
    ),
    (
        "मुहरों पर पशु प्रतीकों और धूपदान के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. एक सींग वाले पशु (Unicorn) के आगे हमेशा दो-खंडों वाला धूपदान या पात्र बना होता है।\n2. कूबड़ वाले सांड के आगे कभी धूपदान नहीं बनाया गया, जिससे पता चलता है कि उसका दर्जा अलग था।\n3. बाघ और हाथी की मुहरों पर भी अक्सर उनके आगे धूपदान का चित्रण मिलता है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 2 केवल", "1 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि बाघ और हाथी के आगे कभी धूपदान नहीं बनाया गया था।"
    ),
    (
        "लकड़ी के ताबूत शवाधान के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. ताबूत को नरकट की चटाई में लपेटकर बर्तनों से घिरे गड्ढे में रखा जाता था।\n2. एक महिला के कंकाल के सिर के पास तांबे का दर्पण रखा मिला था।\n3. लेखक ताबूत के ढक्कन पर कांसे की छेनी से मृत व्यक्ति का नाम खोदते थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 2 केवल", "1 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि ढक्कन पर कोई नाम या लेख नहीं मिला है।"
    ),
    (
        "मोहनजोदड़ो के अनुष्ठानिक स्नान चबूतरे के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. विशाल स्नानागार के पास ईंटों से बने स्नान के कई चबूतरे मिले हैं, जिनमें ढलानदार नालियां थीं।\n2. ये चबूतरे दर्शाते हैं कि शारीरिक स्वच्छता दुर्ग के अनुष्ठानों में भाग लेने की पूर्व-शर्त थी।\n3. ये चबूतरे लकड़ी के बने थे जिन पर जलरोधी राल (resin) चढ़ाया गया था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 2 केवल", "1 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि ये चबूतरे पकी ईंटों के बने थे, लकड़ी के नहीं।"
    ),
    (
        "कालीबंगन की शवाधान प्रथाओं के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. लोथल के विपरीत, कालीबंगन के कब्रिस्तान से कोई भी जुड़वां शवाधान नहीं मिला।\n2. कालीबंगन की कब्रों में गोल गड्ढे मिले हैं जिनमें कलश और बर्तन दफनाए गए थे।\n3. कालीबंगन में कलश शवाधान हड्डियों को धूप में सुखाने के बाद उन्हें दफनाने को दर्शाते हैं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "1 और 2 केवल", "2 और 3 केवल", "1 और 3 केवल"],
        0,
        "तीनों कथन सही हैं, जो कालीबंगन के कब्रों की विशेषताओं का वर्णन करते हैं।"
    ),
    (
        "मुहरों पर बहु-सिर वाले मिश्रित पशुओं (multi-headed composite beasts) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मोहनजोदड़ो की एक मुहर में तीन सिरों वाला पशु है जिसमें एक सींग वाले पशु, कूबड़ वाले बैल और सींग वाले बकरे के सिर हैं।\n2. एक अन्य मुहर में एक शरीर के साथ एक सींग वाले पशु, बाघ और पहाड़ी बकरे के सिर जुड़े हैं।\n3. इन मुहरों का उपयोग व्यापारिक गिल्ड अपनी संयुक्त साझेदारी को दर्शाने के लिए करते थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 2 केवल", "1 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि गिल्ड साझेदारी का सिद्धांत पूरी तरह काल्पनिक है और इसकी व्याख्या मुख्य रूप से धार्मिक है।"
    ),
    (
        "हड़प्पा के वृक्ष देवताओं के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. पीपल वृक्ष के अंदर खड़े देवता को सींग वाला मुकुट पहने दिखाया गया है, जो उनके दिव्य होने का संकेत है।\n2. पीपल के नीचे खड़े सात उपासक लबादे पहने हैं, चूड़ियाँ पहने हैं और बालों में एक पंख लगाए हैं।\n3. वृक्ष पूजा केवल पीपल तक सीमित थी और मुहरों पर अन्य कोई पेड़ नहीं मिलता।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 2 केवल", "1 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि मुहरों पर बबूल और खजूर के पेड़ों का चित्रण भी कभी-कभी मिला है।"
    ),
    (
        "सुरकोटदा के शवाधान में दी जाने वाली भेंट के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. कलशों के ठीक पास बड़े मिट्टी के घड़े रखे जाते थे जिनमें मनके, शंख और अन्य बर्तन होते थे।\n2. कब्रों को भारी पत्थर की चट्टानों से ढका जाता था, जो ऐतिहासिक काल के डोलमेन (dolmens) की तरह दिखते हैं।\n3. लेखक परलोक में रक्षा के लिए मृतकों के साथ तांबे के हथियार दफनाते थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 2 केवल", "1 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि सुरकोटदा की कब्रों से तांबे के हथियार नहीं मिले हैं।"
    ),
    (
        "मेसोपोटामिया के तुलनात्मक संदर्भों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मेसोपोटामिया के कीलाक्षर (cuneiform) लेखों में 'मेलुहा' के साथ व्यापार का उल्लेख है, जिसे सिंधु क्षेत्र माना जाता है।\n2. लेखों में मेलुहा से लाजवर्द, हाथी दांत और विदेशी पक्षियों के आयात का उल्लेख है।\n3. लेखों में मेलुहा के मंदिरों में सिंधु वासियों द्वारा की जाने वाली पूजा पद्धतियों का विस्तृत वर्णन है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 2 केवल", "1 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि इन लेखों में केवल व्यापारिक माल का उल्लेख है, धार्मिक अनुष्ठानों या मंदिरों का नहीं।"
    ),
    (
        "कब्रों में मिलने वाले बर्तनों और सामानों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. एक कब्र में रखे जाने वाले बर्तनों की संख्या कुछ बर्तनों से लेकर दर्जनों तक हो सकती थी।\n2. सोने की माला और कांस्य के बर्तन जैसी बहुमूल्य वस्तुएं कब्रों में अत्यंत दुर्लभ हैं।\n3. यह दर्शाता है कि हड़प्पा समाज कब्रों में धन के अत्यधिक प्रदर्शन पर विश्वास नहीं करता था।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "1 और 2 केवल", "2 और 3 केवल", "1 और 3 केवल"],
        0,
        "तीनों कथन सही हैं, जो कब्रों के सामानों की मात्रा, दुर्लभता और उनके सामाजिक अर्थों को दर्शाते हैं।"
    ),
    (
        "कालीबंगन के ऊंचे चबूतरे पर बनी वेदियों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. दुर्ग (Citadel) के अंदर मिट्टी-ईंट के ऊंचे चबूतरों पर ईंटों से बनी वेदियाँ मिली हैं।\n2. चबूतरे पर जाने के लिए ईंटों की सीढ़ियाँ बनी थीं, जो एक औपचारिक सार्वजनिक अनुष्ठान स्थल का संकेत देती हैं।\n3. लेखक चबूतरे के फर्श पर पूजा में बैठने वालों के लिए ज्यामितीय आकृतियाँ बनाते थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 2 केवल", "1 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि फर्श पर ऐसी किसी नक्काशी का कोई साक्ष्य नहीं है।"
    )
]

# Mock Test Questions (10 Qs) - UPSC standard
mock_data_eng = [
    (
        "With reference to the interpretation of the 'Pashupati Seal' of Mohenjo-daro, which of the following statements is/are correct?\n1. Sir John Marshall identified the figure as 'Proto-Shiva' based on its three faces, horned headgear, and yogic posture.\n2. Doris Srinivasan argued that the figure is a composite bovine deity representing a protective lord of vegetation.\n3. Herbert Gillings proposed that the seal depicts a calendar showing six seasonal transitions represented by the animals.\nSelect the correct answer using the code given below:",
        ["1 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"],
        1,
        "Statements 1 and 2 are correct, reflecting Marshall's Proto-Shiva interpretation and Srinivasan's composite bovine critique. Statement 3 is incorrect: there is no historical or scholarly theory attributing a calendar seasonal transition model by Herbert Gillings to the seal."
    ),
    (
        "Consider the following pairs of Mature Harappan sites and their associated religious/funerary findings:\nI. Lothal : Double/Twin Burials in a single pit\nII. Harappa : Wooden Coffin burial in Cemetery R-37\nIII. Kalibangan : Raised platform with a row of seven fire altars\nWhich of the pairs given above are correctly matched?",
        ["I and II only", "II and III only", "I and III only", "I, II and III"],
        3,
        "All three pairs are correctly matched: Lothal double burial, Harappa wooden coffin, and Kalibangan row of seven fire altars."
    ),
    (
        "Which of the following statements best explains the complete absence of monumental temples in the Indus Valley Civilisation?\n1. The Harappans were strict materialists who did not practice any form of deity worship.\n2. Their religious practices were decentralised, focusing on domestic shrines, animism, and open-air natural rituals.\n3. The ruling elites suppressed institutional religion to prevent the emergence of a powerful priestly class.\nSelect the correct answer using the code given below:",
        ["2 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statement 2 is correct. The absence of temples indicates a decentralized, domestic, and civic nature of Harappan religion. Statements 1 and 3 are incorrect and speculative."
    ),
    (
        "With reference to tree worship in the Harappan Civilisation, consider the following statements:\n1. The Pipal tree (Ficus religiosa) is the most frequently depicted sacred plant in glyptic arts.\n2. Tree deities are shown on seals as standing inside the forks of Pipal branches, wearing horned headdresses.\n3. Acacias and wild palms are also occasionally represented on seals, suggesting a broad animistic reverence.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All three statements are correct, describing Pipal worship, horned tree deities, and other plant representations."
    ),
    (
        "Consider the following statements regarding the 'Unicorn' seal motif:\n1. It is the most common zoomorphic representation, appearing on square steatite seals used for administrative and trade purposes.\n2. The Unicorn is depicted with a single curved horn, a collar, and stands before a two-tiered 'manger' or 'standard'.\n3. Scholars generally interpret the standard as a sacred censer or incense burner, indicating the ritual status of the Unicorn.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All three statements are correct, detailing the Unicorn motif, its standard accessory, and its ritual significance."
    ),
    (
        "With reference to the Great Bath of Mohenjo-daro, which of the following statements are correct?\n1. It was waterproofed with a backing layer of bitumen (asphalt) behind the brick lining.\n2. It features two wide staircases on the north and south ends with wooden steps preserved in the clay.\n3. The complex includes private changing rooms and bathing platforms with independent drains.\nSelect the correct answer using the code given below:",
        ["1 and 3 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 3 are correct. Statement 2 is incorrect: while the staircases exist, they had brick steps, and there is no evidence of preserved wooden steps."
    ),
    (
        "Consider the following statements regarding Harappan funerary rites:\n1. North-South extended inhumation was the dominant form, with pots and personal ornaments placed around the head.\n2. Fractional or urn burials containing bone ashes were practiced as secondary burial rites.\n3. The graves of the Harappans show a high degree of social stratification, with rulers buried in monumental brick tombs.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: Harappan graves are generally simple and do not show extreme wealth differentiation or monumental brick tombs for rulers."
    ),
    (
        "With reference to the fire altars of Kalibangan and Lothal, consider the following statements:\n1. The altars consist of shallow clay-lined pits containing charcoal, ash, and animal bones.\n2. A central clay stele or column is found in the middle of these altars, interpreted as a sacrificial post.\n3. Fire altars are found in both public citadel platforms and private courtyards of the Lower Town.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All three statements are correct, detailing the composition, central clay column, and location of fire altars."
    ),
    (
        "Consider the following statements regarding Harappan amulets:\n1. Small tablets of terracotta, faience, and steatite are interpreted as protective amulets against evil forces.\n2. Many amulets depict scenes of heroes strangling tigers or mythical beasts, indicating a popular folklore.\n3. Amulets were inscribed with long texts containing the names of personal guardian deities.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: inscriptions are very short (usually 3-5 signs) and since the script is undeciphered, we do not know if they contain deity names."
    ),
    (
        "With reference to the phallic and vulva worship in the Indus Civilisation, consider the following statements:\n1. Sir John Marshall identified conical stones and terracotta cylinders as lingas representing phallic worship.\n2. Large stone rings were interpreted as yoni rings representing female fertility principles.\n3. Archaeologist George Dales challenged these interpretations, suggesting they were structural column bases.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All three statements are correct, describing Marshall's linga/yoni interpretations and Dales' architectural challenge."
    )
]

mock_data_hin = [
    (
        "मोहनजोदड़ो की 'पशुपति मुहर' की व्याख्या के संदर्भ में, निम्नलिखित कथनों में से कौन सा/से सही है/हैं?\n1. सर जॉन मार्शल ने तीन चेहरों, सींग वाले मुकुट और योगासन मुद्रा के आधार पर इसे 'आदि-शिव' के रूप में व्याख्यायित किया।\n2. डोरिस श्रीनिवासन ने तर्क दिया कि यह आकृति एक बैल-मानव मिश्रित देवता है जो वनस्पति के रक्षक का प्रतिनिधित्व करता है।\n3. हरबर्ट गिलिंग्स ने प्रस्तावित किया कि मुहर में जानवरों द्वारा दर्शाए गए छह मौसमी बदलावों को दर्शाने वाला कैलेंडर है।\nनीचे दिए गए कूट का उपयोग करके सही उत्तर चुनिए:",
        ["1 केवल", "1 और 2 केवल", "2 और 3 केवल", "1, 2 और 3"],
        1,
        "कथन 1 और 2 सही हैं, जो मार्शल की आदि-शिव व्याख्या और श्रीनिवासन की बैल-मानव आलोचना को दर्शाते हैं। कथन 3 गलत है क्योंकि हरबर्ट गिलिंग्स द्वारा दिया गया ऐसा कोई सिद्धांत मान्य नहीं है।"
    ),
    (
        "परिपक्व हड़प्पा स्थलों और उनसे जुड़े धार्मिक/शवाधान साक्ष्यों के निम्नलिखित युग्मों पर विचार करें:\nI. लोथल : एक ही गड्ढे में जुड़वां/डबल शवाधान\nII. हड़प्पा : कब्रिस्तान R-37 से देवदार की लकड़ी का ताबूत शवाधान\nIII. कालीबंगन : सात अग्नि वेदियों की पंक्ति वाला मिट्टी का चबूतरा\nउपरोक्त युग्मों में से कौन से सही सुमेलित हैं?",
        ["I और II केवल", "II और III केवल", "I और III केवल", "I, II और III"],
        3,
        "तीनों युग्म सही सुमेलित हैं: लोथल का जुड़वां शवाधान, हड़प्पा का ताबूत शवाधान और कालीबंगन की सात अग्नि वेदियाँ।"
    ),
    (
        "निम्नलिखित में से कौन सा कथन सिंधु घाटी सभ्यता में विशाल मंदिरों के पूर्ण अभाव की सबसे अच्छी व्याख्या करता है?\n1. हड़प्पा वासी सख्त भौतिकवादी थे जो किसी भी प्रकार की मूर्ति पूजा नहीं करते थे।\n2. उनकी धार्मिक प्रथाएं विकेंद्रीकृत थीं, जो घरेलू वेदिकाओं, जीववाद और खुले में प्राकृतिक अनुष्ठानों पर केंद्रित थीं।\n3. शासक वर्ग ने पुरोहित वर्ग के प्रभाव को दबाने के लिए संस्थागत मंदिरों के निर्माण पर प्रतिबंध लगा दिया था।\nनीचे दिए गए कूट का उपयोग करके सही उत्तर चुनिए:",
        ["2 केवल", "1 और 2 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 2 सही है। मंदिरों का न मिलना हड़प्पा धर्म के विकेंद्रीकृत, घरेलू और नागरिक स्वभाव को दर्शाता है। कथन 1 और 3 काल्पनिक हैं।"
    ),
    (
        "हड़प्पा सभ्यता में वृक्ष पूजा के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. पीपल का वृक्ष (Ficus religiosa) मुहरों पर सबसे अधिक चित्रित किया जाने वाला पवित्र पौधा है।\n2. पीपल की शाखाओं के बीच खड़े सींग वाले मुकुट पहने देवताओं को मुहरों पर दिखाया गया है।\n3. मुहरों पर बबूल और जंगली खजूर का भी अंकन मिलता है, जो प्रकृति के प्रति उनकी श्रद्धा को दर्शाता है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1 और 2 केवल", "2 और 3 केवल", "1 और 3 केवल", "1, 2 और 3"],
        3,
        "तीनों कथन सही हैं, जो पीपल पूजा, सींग वाले देवताओं और अन्य पौधों के चित्रण का वर्णन करते हैं।"
    ),
    (
        "मुहरों पर एक सींग वाले पशु (Unicorn) के रूपांकन के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह सबसे आम पशु चित्रण है, जो व्यापारिक और प्रशासनिक उपयोग के लिए बनी सेलखड़ी की मुहरों पर पाया जाता है।\n2. इस पशु के सिर पर एक सींग और गर्दन में पट्टा बना है, और यह दो-खंडों वाले धूपदान या पात्र के आगे खड़ा है।\n3. विद्वान इस पात्र को एक पवित्र धूपदानी मानते हैं, जो इस पशु की धार्मिक विशिष्टता को दर्शाता है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "1 और 2 केवल", "2 और 3 केवल", "1 और 3 केवल"],
        0,
        "तीनों कथन सही हैं, जो एक सींग वाले पशु के रूपांकन, उसके आगे रखे पात्र और उसके अनुष्ठानिक महत्व को स्पष्ट करते हैं।"
    ),
    (
        "मोहनजोदड़ो के विशाल स्नानागार के संदर्भ में निम्नलिखित में से कौन से कथन सही हैं?\n1. रिसाव रोकने के लिए ईंटों के पीछे तारकोल (bitumen) की एक मोटी परत बिछाई गई थी।\n2. जलाशय में उतरने के लिए उत्तर और दक्षिण में दो सीढ़ियाँ बनी थीं जिनमें लकड़ी के पायदान सुरक्षित बचे रहे।\n3. इस परिसर में स्नान के निजी चबूतरे और ढकी नालियाँ शामिल थीं।\nनीचे दिए गए कूट का उपयोग करके सही उत्तर चुनिए:",
        ["1 और 3 केवल", "1 और 2 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 3 सही हैं। कथन 2 गलत है क्योंकि सीढ़ियाँ ईंटों की थीं, लकड़ी के पायदान सुरक्षित बचने का कोई प्रमाण नहीं है।"
    ),
    (
        "हड़प्पा की शवाधान प्रथाओं के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. उत्तर-दक्षिण दिशा में शव को सीधा लिटाकर दफनाना प्रमुख था, जिसमें सिर के पास बर्तन और आभूषण रखे जाते थे।\n2. द्वितीयक शवाधान के रूप में कलशों में हड्डियों की राख को इकट्ठा करके दफनाने की प्रथा भी थी।\n3. हड़प्पा की कब्रें अत्यधिक सामाजिक असमानता दर्शाती हैं, जहाँ शासकों को बड़े मकबरों में दफनाया जाता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 2 केवल", "1 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि हड़प्पा की कब्रें बहुत सादा हैं और मिस्र या चीन की तरह शासकों के बड़े मकबरे नहीं मिले हैं।"
    ),
    (
        "कालीबंगन और लोथल की अग्नि वेदियों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. ये वेदियाँ मिट्टी के गड्ढे थीं जिनमें कोयला, राख और पालतू पशुओं की हड्डियाँ मिली हैं।\n2. वेदियों के बीच में एक बेलनाकार मिट्टी का खंभा खड़ा होता था, जिसे बलि का खंभा माना जाता है।\n3. अग्नि वेदियाँ दुर्ग के सार्वजनिक चबूतरे और निचले शहर के निजी आंगनों दोनों जगह मिली हैं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "1 और 2 केवल", "2 और 3 केवल", "1 और 3 केवल"],
        0,
        "तीनों कथन सही हैं, जो अग्नि वेदियों की बनावट, मध्य स्तंभ और प्राप्ति स्थानों का वर्णन करते हैं।"
    ),
    (
        "हड़प्पा के ताबीजों (amulets) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. पकी मिट्टी, फेयॉन्स और सेलखड़ी के छोटे ताबीजों को बुरी आत्माओं से बचने का साधन माना जाता था।\n2. कई ताबीजों में नायकों को बाघों को वश में करते दिखाया गया है, जो लोककथाओं को दर्शाता है।\n3. ताबीजों पर लंबे मंत्र लिखे होते थे जिनमें व्यक्तिगत रक्षक देवताओं के नाम लिखे होते थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 2 केवल", "1 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि लेख अत्यंत छोटे (3-5 वर्णों के) हैं और लिपि अपठित होने के कारण देवताओं के नाम की पुष्टि नहीं की जा सकती।"
    ),
    (
        "सिंधु सभ्यता में लिंग और योनि पूजा के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. सर जॉन मार्शल ने शंक्वाकार पत्थरों और बेलनाकार आकारों को लिंग पूजा का प्रतीक माना था।\n2. बड़े पत्थर के छल्लों को स्त्री उर्वरता के प्रतीक योनी छल्ले के रूप में व्याख्यायित किया गया था।\n3. पुरातत्वविद जॉर्ज डेल्स ने इन व्याख्याओं को चुनौती दी और इन्हें इमारतों के खंभों के आधार बताया।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "1 और 2 केवल", "2 और 3 केवल", "1 और 3 केवल"],
        0,
        "तीनों कथन सही हैं, जो मार्शल की लिंग/योनि व्याख्या और जॉर्ज डेल्स की वास्तुकला संबंधी चुनौती का वर्णन करते हैं।"
    )
]

for q, opts, ans, sol in practice_data_eng:
    eng_data["practiceQuestions"].append({
        "q": q,
        "opts": opts,
        "ans": ans,
        "sol": sol
    })

for q, opts, ans, sol in practice_data_hin:
    hin_data["practiceQuestions"].append({
        "q": q,
        "opts": opts,
        "ans": ans,
        "sol": sol
    })

for q, opts, ans, sol in mock_data_eng:
    eng_data["mockTestQuestions"].append({
        "q": q,
        "opts": opts,
        "ans": ans,
        "sol": sol
    })

for q, opts, ans, sol in mock_data_hin:
    hin_data["mockTestQuestions"].append({
        "q": q,
        "opts": opts,
        "ans": ans,
        "sol": sol
    })

# Write English base JSON
eng_file = os.path.join(ENG_DIR, "content.json")
with open(eng_file, "w", encoding="utf-8") as f:
    json.dump(eng_data, f, ensure_ascii=False, indent=2)

# Write Hindi base JSON
hin_file = os.path.join(HIN_DIR, "content.json")
with open(hin_file, "w", encoding="utf-8") as f:
    json.dump(hin_data, f, ensure_ascii=False, indent=2)

print("Religions Base JSON files built successfully!")
