import json
import os

ENG_DIR = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\HarappanIndus-Valley-Civilisation\Socio-Cultural-Aspects-of-Indus-Valley-Civilisation"
HIN_DIR = os.path.join(ENG_DIR, "hi")
os.makedirs(HIN_DIR, exist_ok=True)

# English base structure
eng_data = {
    "breadcrumbs": {
        "parent": "UPSC Syllabus",
        "parentUrl": "/upsc/",
        "current": "Socio-Cultural Aspects"
    },
    "hero": {
        "title": "Socio-Cultural Aspects of IVC",
        "description": "Master the class structure, gender status, cosmetics, religious practices, Pashupati seal, burial rituals, undeciphered script, and arts of the Indus Valley Civilisation for UPSC GS-1."
    },
    "labels": {
        "clickToExpand": "Click to expand details",
        "mockIntro": {
            "title": "Interactive UPSC Mock Test",
            "description": "Evaluate your understanding of Harappan society and culture. This timed test contains 10 high-quality, exam-standard questions with negative marking.",
            "startBtn": "Start Mock Test"
        },
        "mockPlay": {
            "prevBtn": "Previous Question",
            "nextBtn": "Next Question",
            "submitBtn": "Submit Test"
        }
    },
    "timeline": {
        "title": "Social & Cultural Evolution",
        "description": "Explore the structural facets of Harappan daily life, spiritual practices, and artistic representations.",
        "cards": [
            {
                "period": "Daily Life",
                "date": "Society, Dress & Cosmetics",
                "details": "Class divisions without evidence of a rigid caste system. Use of cotton and wool, elaborate hairstyles, and cosmetic items like lipsticks (Chanhudaro) and bronze mirrors."
            },
            {
                "period": "Spiritual Realm",
                "date": "Religion & Burial Customs",
                "details": "Worship of Mother Goddess, Pashupati (Proto-Shiva), trees (pipal), and animals (bull). Funerary practices include complete burials (Cemetery R-37) and double burials (Lothal)."
            },
            {
                "period": "Creative Expression",
                "date": "Script, Crafts & Arts",
                "details": "Pictographic undeciphered script written in Boustrophedon. Masterful bronze lost-wax casting (Dancing Girl), steatite seal carving, and terracotta toy manufacturing."
            }
        ]
    },
    "mnemonics": {
        "title": "Mnemonics & Memory Hacks",
        "description": "Use these visual memory hooks to retain critical facts about Harappan society, religion, and art for the UPSC Civil Services Examination.",
        "items": [
            {
                "title": "Mnemonic 1: Animals on the Pashupati Seal",
                "phrase": "\"T-E-R-B + Deer (Tiger, Elephant, Rhino, Buffalo + 2 Deer)\"",
                "decryption": "The Pashupati seal deity is surrounded by **T**iger, **E**lephant, **R**hinoceros, and **B**uffalo, with **two deer** depicted under his throne."
            },
            {
                "title": "Mnemonic 2: Writing Style Direction",
                "phrase": "\"Boustrophedon - Bull plowing the field (Right to Left, then Left to Right)\"",
                "decryption": "The Harappan script direction alternates lines like an ox plowing: first line **Right to Left**, second line **Left to Right**."
            },
            {
                "title": "Mnemonic 3: Joint Burial Site Location",
                "phrase": "\"Lo-Double (Lothal double burial)\"",
                "decryption": "Joint burials of male and female in a single grave are found at **Lothal**."
            }
        ]
    },
    "flashcards": {
        "title": "Active Recall Flashcards",
        "description": "Flashcards are key to mastering fact-dense UPSC questions. Click on any card below to flip it and reveal the answer.",
        "items": [
            {
                "question": "Which site has yielded direct evidence of cosmetics like lipsticks?",
                "answer": "<strong>Chanhudaro</strong> in Sindh, Pakistan.",
                "icon": "fa-paint-brush"
            },
            {
                "question": "Name the four animals surrounding the central figure of the Pashupati seal.",
                "answer": "<strong>Tiger, Elephant, Rhinoceros, and Buffalo</strong> (plus two deer at the feet).",
                "icon": "fa-paw"
            },
            {
                "question": "What is the writing style of the Harappan pictographic script?",
                "answer": "<strong>Boustrophedon</strong> (alternating from right-to-left and left-to-right).",
                "icon": "fa-pen-fancy"
            },
            {
                "question": "Where was the famous bronze 'Dancing Girl' figurine discovered?",
                "answer": "<strong>Mohenjo-daro</strong>, using the lost-wax casting technique.",
                "icon": "fa-female"
            },
            {
                "question": "Which Harappan site yielded evidence of fire altars indicating ritual worship?",
                "answer": "<strong>Kalibangan</strong> and <strong>Lothal</strong>.",
                "icon": "fa-fire"
            }
        ]
    },
    "deepDive": {
        "title": "Syllabus Core Study Notes (Deep-Dive)",
        "description": "Master the class divisions, gender dynamics, spiritual rituals, burial styles, writing systems, and visual arts of the Harappan Civilisation.",
        "sections": [
            {
                "title": "1. Social Structure, Dress, Ornaments & Diet",
                "content": """<p>The Harappan society was highly stratified yet cohesive. While no evidence of a rigid hereditary caste system exists, class divisions based on occupation are clearly visible in the housing sizes and burial wealth.</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-users-viewfinder"></i> Social Stratification & Women Status</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>Class Divisions:</strong> Three primary social groups populated cities: the ruling administrative elite, wealthy merchants/scribes, and common artisans, farmers, and laborers.</li>
      <li><strong>Matriarchal Theories:</strong> The abundance of terracotta Mother Goddess figurines suggests that women held high status, and the society was potentially matriarchal or matrilineal in its spiritual focus.</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-shirt"></i> Dress, Cosmetics & Food Habits</div>
    <p style="font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;">
      Both men and women wore two-piece garments of cotton and wool. Men wore a shawl-like wrap (as seen on the Priest-King), and women wore short skirts held by girdles. Hair was styled elaborately, secured with ivory pins. Cosmetics were highly advanced: cinnabar lipsticks are found at Chanhudaro, collyrium (eyeliner) was kept in small pots, and bronze mirrors were common. Diet consisted of wheat, barley, rice (Lothal), fish, mutton, cattle, and poultry, indicating a rich agricultural surplus.
    </p>
  </div>
</div>""",
                "masteryZone": []
            },
            {
                "title": "2. Religious Beliefs, Burial Customs & Script",
                "content": """<p>Harappan religion did not center around massive temples but was deeply tied to nature, animism, and ritual purification. Their undeciphered script represents a highly standardized literacy system.</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-om"></i> Deities & Ritual Worship</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>Pantheon:</strong> Spiritual life was dominated by the worship of the Mother Goddess (Earth deity) and Pashupati Proto-Shiva (depicted on steatite seals sitting yogic, surrounded by wild beasts).</li>
      <li><strong>Animism:</strong> Nature worship of pipal trees, humped bulls, and water purification (ritual bathing at Mohenjo-daro). Fire altars found at Kalibangan and Lothal show sacrificial rituals.</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-box-archive"></i> Burial Types & Boustrophedon Script</div>
    <p style="font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;">
      The standard funerary method was complete inhumation (burial) in Cemetery R-37 (Harappa), with bodies placed head north. Fractional burials (bones gathered after exposure) and urn cremations were also practiced. Lothal is famous for double burials (male and female in a single grave). The script is pictographic and logo-syllabic (approx. 400 signs) and remains undeciphered. It was written in <strong>Boustrophedon</strong> format (alternating directions). The Dholavira signboard displays ten large script signs.
    </p>
  </div>
</div>""",
                "masteryZone": []
            },
            {
                "title": "3. Art, Crafts, Amusements & Toys",
                "content": """<p>Harappan artistic legacy demonstrates outstanding mastery over metallurgy, stone carving, and clay molding, combining aesthetic skill with functional play.</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-gem"></i> Metallurgical & Sculptural Masterpieces</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>Dancing Girl:</strong> A 10cm bronze figurine from Mohenjo-daro created using the solid <strong>lost-wax (cire perdue)</strong> casting method. She wears arm-covering bangles in a relaxed posture.</li>
      <li><strong>Stone Carving:</strong> The bearded Steatite Priest-King and the red sandstone athletic torso from Harappa exhibit highly realistic anatomy.</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-puzzle-piece"></i> Toys, Pastimes & Bead Industry</div>
    <p style="font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;">
      Terracotta was the medium of the masses, used to build toy carts with movable wheels, whistles shaped like birds, climbing monkeys, and cattle figurines with nodding heads. Pastimes included playing dice (cubical chert/terracotta dice), board games, cockfighting, and hunting. Bead manufacturing was a major industry at Chanhudaro and Lothal, utilizing carnelian, lapis lazuli, and steatite to make export-grade jewelry.
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
        "current": "सामाजिक-सांस्कृतिक पहलू"
    },
    "hero": {
        "title": "सिंधु सभ्यता के सामाजिक-सांस्कृतिक पहलू",
        "description": "यूपीएससी परीक्षा (GS-1) के लिए हड़प्पा सभ्यता के सामाजिक वर्गों, महिलाओं की स्थिति, सौंदर्य प्रसाधनों, धार्मिक विश्वासों, पशुपति मुहर, शवाधान विधियों, अपठित लिपि और कला रूपों का अध्ययन करें।"
    },
    "labels": {
        "clickToExpand": "विवरण देखने के लिए क्लिक करें",
        "mockIntro": {
            "title": "इंटरैक्टिव परीक्षा मॉक टेस्ट",
            "description": "हड़प्पा समाज और संस्कृति के संबंध में अपनी तैयारी का मूल्यांकन करें। इस समयबद्ध परीक्षण में नकारात्मक अंकन के साथ 10 उच्च-स्तरीय यूपीएससी मानक के प्रश्न शामिल हैं।",
            "startBtn": "मॉक टेस्ट शुरू करें"
        },
        "mockPlay": {
            "prevBtn": "Previous Question",
            "nextBtn": "Next Question",
            "submitBtn": "Submit Test"
        }
    },
    "timeline": {
        "title": "सामाजिक और सांस्कृतिक विकास",
        "description": "हड़प्पा वासियों के दैनिक जीवन, धार्मिक विश्वासों और रचनात्मक कलात्मक अभिव्यक्तियों का अध्ययन करें।",
        "cards": [
            {
                "period": "दैनिक जीवन",
                "date": "समाज, वेशभूषा और सौंदर्य प्रसाधन",
                "details": "जन्म-आधारित जाति व्यवस्था के बिना व्यावसायिक सामाजिक वर्ग। सूती और ऊनी कपड़ों का उपयोग, जटिल केशविन्यास और चन्हुदड़ो से मिले लिपस्टिक जैसे प्रसाधन।"
            },
            {
                "period": "आध्यात्मिक क्षेत्र",
                "date": "धर्म और शवाधान प्रथाएं",
                "details": "मातृदेवी, पशुपति (आद्य-शिव), पीपल और सांड की पूजा। शवाधान में सामान्य दफ़नाने (कब्रिस्तान R-37) और लोथल से युगल दफ़नाने (double burials) के साक्ष्य।"
            },
            {
                "period": "रचनात्मक अभिव्यक्ति",
                "date": "लिपि, हस्तशिल्प और कलाकृतियाँ",
                "details": "चित्रलेखीय अपठित लिपि जिसे बोउस्ट्रोफेडन (दाएं से बाएं और बाएं से दाएं) लिखा जाता था। कांस्य ढलाई की लुप्त-मोम विधि (नर्तकी), मुहर नक्काशी और खिलौना उद्योग।"
            }
        ]
    },
    "mnemonics": {
        "title": "याद रखने के सूत्र (Mnemonics)",
        "description": "यूपीएससी परीक्षा के लिए हड़प्पा समाज, धर्म और कला से संबंधित तथ्यों को आसानी से याद रखने के लिए इन दृश्य सूत्रों का उपयोग करें।",
        "items": [
            {
                "title": "याद रखने का सूत्र 1: पशुपति मुहर के पशु",
                "phrase": "\"T-E-R-B + हिरण (बाघ, हाथी, गैंडा, भैंसा + 2 हिरण)\"",
                "decryption": "पशुपति शिव के चारों ओर **T**iger (बाघ), **E**lephant (हाथी), **R**hinoceros (गैंडा), और **B**uffalo (भैंसा) हैं, और उनके पैरों के पास **दो हिरण** बने हैं।"
            },
            {
                "title": "याद रखने का सूत्र 2: लिपि की लेखन दिशा",
                "phrase": "\"बोउस्ट्रोफेडन - खेत जोतते हुए बैल की दिशा (दाएं से बाएं, फिर बाएं से दाएं)\"",
                "decryption": "हड़प्पा लिपि की पंक्तियाँ बारी-बारी से लिखी जाती थीं: पहली पंक्ति **दाएं से बाएं** और दूसरी पंक्ति **बाएं से दाएं**।"
            },
            {
                "title": "याद रखने का सूत्र 3: युगल शवाधान का स्थल",
                "phrase": "\"लो-युगल (लोथल युगल कब्र)\"",
                "decryption": "पुरुष और महिला को एक साथ एक ही कब्र में दफनाने (Double burial) के साक्ष्य **लोथल** से मिले हैं।"
            }
        ]
    },
    "flashcards": {
        "title": "सक्रिय स्मरण फ्लैशकार्ड (Active Recall)",
        "description": "फ्लैशकार्ड्स तथ्य-प्रधान यूपीएससी प्रश्नों को याद रखने का सर्वोत्तम साधन हैं। उत्तर देखने के लिए नीचे दिए गए कार्ड्स पर क्लिक करें।",
        "items": [
            {
                "question": "किस हड़प्पा स्थल से लिपस्टिक और काजल जैसे सौंदर्य प्रसाधनों के प्रत्यक्ष साक्ष्य मिले हैं?",
                "answer": "पाकिस्तान के सिंध प्रांत में स्थित <strong>चन्हुदड़ो</strong> से।",
                "icon": "fa-paint-brush"
            },
            {
                "question": "पशुपति मुहर की केंद्रीय आकृति को घेरने वाले चार पशुओं के नाम क्या हैं?",
                "answer": "<strong>बाघ, हाथी, गैंडा और भैंसा</strong> (और चरणों में दो हिरण)।",
                "icon": "fa-paw"
            },
            {
                "question": "हड़प्पा सभ्यता की चित्रात्मक लिपि की लेखन शैली क्या कहलाती है?",
                "answer": "<strong>बोउस्ट्रोफेडन (Boustrophedon)</strong> (बारी-बारी से दाएं से बाएं और बाएं से दाएं)।",
                "icon": "fa-pen-fancy"
            },
            {
                "question": "कांस्य से बनी प्रसिद्ध 'नर्तकी' (Dancing Girl) की मूर्ति कहाँ से खोजी गई थी?",
                "answer": "मोहनजोदड़ो से, इसे <strong>लुप्त-मोम (lost-wax)</strong> विधि द्वारा ढाला गया था।",
                "icon": "fa-female"
            },
            {
                "question": "किस हड़प्पा स्थल से अनुष्ठानिक पूजा का संकेत देने वाले अग्निकुंडों के साक्ष्य मिले हैं?",
                "answer": "<strong>कालीबंगन</strong> और <strong>लोथल</strong> से।",
                "icon": "fa-fire"
            }
        ]
    },
    "deepDive": {
        "title": "पाठ्यक्रम मुख्य नोट्स (गहन अध्ययन)",
        "description": "हड़प्पा समाज के वर्गों, महिलाओं की स्थिति, धार्मिक अनुष्ठानों, शवाधान शैलियों, लेखन प्रणालियों और कलाकृतियों का गहन अध्ययन करें।",
        "sections": [
            {
                "title": "1. सामाजिक संरचना, वेशभूषा, आभूषण और खान-पान",
                "content": """<p>हड़प्पा समाज स्तरीकृत था लेकिन अत्यधिक एकीकृत था। यद्यपि जन्म-आधारित कठोर जाति व्यवस्था के साक्ष्य नहीं हैं, लेकिन आवासों के आकार और कब्रों के सामान से सामाजिक विभाजन स्पष्ट दिखाई देता है।</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-users-viewfinder"></i> सामाजिक स्तरीकरण और महिलाओं की स्थिति</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>वर्ग विभाजन:</strong> समाज मुख्य रूप से तीन वर्गों में विभाजित था: शासक/प्रशासनिक वर्ग, व्यापारी और लिपिक वर्ग, तथा सामान्य कारीगर, किसान और मजदूर।</li>
      <li><strong>मातृसत्तात्मक सिद्धांत:</strong> भारी संख्या में मिली मिट्टी की मातृदेवी की मूर्तियाँ दर्शाती हैं कि महिलाओं का समाज में उच्च स्थान था, और समाज आध्यात्मिक रूप से मातृसत्तात्मक था।</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-shirt"></i> वेशभूषा, सौंदर्य प्रसाधन और खान-पान</div>
    <p style="font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;">
      स्त्री और पुरुष दोनों सूती और ऊनी कपड़े पहनते थे। पुरुष शॉल जैसा वस्त्र लपेटते थे (जैसे पुरोहित-राजा की मूर्ति में दिखता है), और स्त्रियाँ घुटनों तक स्कर्ट पहनती थीं। बालों को सजाने के लिए हाथीदांत की सूइयों का उपयोग होता था। चन्हुदड़ो से लिपस्टिक (cinnabar) के साक्ष्य मिले हैं, आँखों में लगाने के लिए काजल (collyrium) डिब्बियों में रखा जाता था और कांसे के दर्पण आम थे। खान-पान में गेहूं, जौ, चावल (लोथल), मछली, भेड़ और मवेशियों का मांस शामिल था।
    </p>
  </div>
</div>""",
                "masteryZone": []
            },
            {
                "title": "2. धार्मिक विश्वास, शवाधान प्रथाएं और लिपि",
                "content": """<p>हड़प्पा वासियों का धर्म बड़े मंदिरों के इर्द-गिर्द केंद्रित नहीं था, बल्कि प्रकृति, पशुओं और अनुष्ठानिक शुद्धता से जुड़ा हुआ था। उनकी अपठित लिपि एक व्यवस्थित साक्षरता प्रणाली को दर्शाती है।</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-om"></i> देव-पूजा और धार्मिक अनुष्ठान</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>देवता:</strong> आध्यात्मिक जीवन में मातृदेवी (पृथ्वी की उर्वरता देवी) और पशुपति शिव (मुहर पर योगासन में बैठे और जंगली जानवरों से घिरे देव) की पूजा प्रमुख थी।</li>
      <li><strong>प्रकृति पूजा:</strong> पीपल के पेड़, एक सींग वाले पशु और कूबड़ वाले सांड की पूजा की जाती थी। मोहनजोदड़ो में विशाल स्नानागार पवित्र स्नान के लिए था। कालीबंगन और लोथल में अग्निकुंडों से यज्ञीय प्रथाओं की पुष्टि होती है।</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-box-archive"></i> शवाधान के प्रकार और बोउस्ट्रोफेडन लिपि</div>
    <p style="font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;">
      सबसे आम प्रथा पूर्ण शवाधान (दफनाना) थी, जैसा हड़प्पा के कब्रिस्तान R-37 में मिला है, जहाँ शव का सिर उत्तर की ओर रखा जाता था। इसके अतिरिक्त आंशिक शवाधान (हड्डियों को धूप में छोड़ने के बाद दबाना) और दाह संस्कार के बाद अस्थियों को कलश में रखना भी प्रचलित था। लोथल से पुरुष और महिला को एक साथ दफनाने (युगल कब्र) के साक्ष्य मिले हैं। हड़प्पा लिपि चित्रात्मक और लोगो-सिलेबिक (लगभग 400 चिन्ह) है जो अभी तक पढ़ी नहीं जा सकी है। इसे <strong>बोउस्ट्रोफेडन</strong> (पहली पंक्ति दाएं से बाएं, दूसरी बाएं से दाएं) शैली में लिखा जाता था। धोलावीरा से 10 अक्षरों वाला एक बड़ा सूचना-पट्ट (signboard) मिला है।
    </p>
  </div>
</div>""",
                "masteryZone": []
            },
            {
                "title": "3. कला, शिल्प, खेल-मनोरंजन और खिलौने",
                "content": """<p>हड़प्पा की कला धातु विज्ञान, पत्थर की नक्काशी और मिट्टी की ढलाई में उनके असाधारण कौशल को दर्शाती है, जहाँ उपयोगिता और सौंदर्य का संगम था।</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-gem"></i> धातुकर्म और मूर्तिकला के उत्कृष्ट नमूने</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>कांस्य नर्तकी:</strong> मोहनजोदड़ो से प्राप्त 10 सेमी की कांस्य मूर्ति जिसे ठोस <strong>लुप्त-मोम (lost-wax/cire perdue)</strong> विधि से ढाला गया है। वह एक हाथ में चूड़ियां पहने हुए विश्राम की मुद्रा में खड़ी है।</li>
      <li><strong>पाषाण मूर्तियाँ:</strong> सेलखड़ी से बनी पुरोहित-राजा (Priest-King) की मूर्ति और हड़प्पा से प्राप्त लाल बलुआ पत्थर का मानव धड़ (torso) शारीरिक रचना के यथार्थवाद को दर्शाते हैं।</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-puzzle-piece"></i> खिलौने, मनोरंजन और मनका उद्योग</div>
    <p style="font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;">
      मिट्टी (terracotta) का उपयोग आम लोगों के खिलौने बनाने में होता था, जैसे चलने वाले पहियों वाली गाड़ियाँ, पक्षियों के आकार की सीटियाँ, रस्सी पर चढ़ने वाले बंदर और हिलने वाले सिर वाले मवेशी। मनोरंजन के लिए घनाकार चर्ट और मिट्टी के पासे (dice), शतरंज जैसे बोर्ड गेम, मुर्गों की लड़ाई और शिकार प्रमुख थे। मनका बनाने के बड़े कारखाने चन्हुदड़ो और लोथल में मिले हैं, जहाँ अकीक (carnelian), लाजवर्त (lapis lazuli) और सेलखड़ी का उपयोग आभूषणों के निर्यात के लिए होता था।
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
        "Consider the following statements regarding the social structure of the Harappan Civilisation:\n1. The layout of housing in cities suggests a clear distinction between different occupational classes.\n2. Archaeological evidence confirms the existence of a highly rigid, birth-based caste system similar to the later Vedic period.\n3. The abundance of terracotta female figurines has led many historians to suggest the possibility of a matriarchal or matrilineal society.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        2,
        "Statements 1 and 3 are correct. Statement 2 is incorrect: there is no archaeological evidence of a rigid birth-based caste system in the Indus Valley Civilisation; social divisions were occupational and wealth-based."
    ),
    (
        "With reference to the dress and ornaments of the Harappans, consider the following statements:\n1. Garments made of both cotton and wool were widely used by the population.\n2. Ornaments like necklaces, armlets, and finger rings were worn exclusively by women.\n3. Dressed stone sculptures, such as the Priest-King, show the use of patterned shawls draped over the shoulder.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        2,
        "Statements 1 and 3 are correct. Statement 2 is incorrect: ornaments like necklaces, armlets, and rings were worn by both men and women, as verified from grave findings."
    ),
    (
        "Consider the following statements regarding the cosmetic and grooming habits of the Harappans:\n1. Chanhudaro has yielded direct evidence of cosmetic items, including a substance identified as lipsticks.\n2. Small terracotta and bronze pots were used to store collyrium (eyeliner) and hair oils.\n3. Bronze mirrors with detailed handles were common items of personal grooming in wealthy households.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All three statements are correct, outlining the advanced cosmetics, pots for collyrium, and bronze mirrors utilized in Harappan grooming."
    ),
    (
        "With reference to the dietary habits of the Indus Valley people, consider the following statements:\n1. The primary cereal crops consumed were wheat and barley, which were stored in large public granaries.\n2. Rice was a staple food consumed daily across all major northern sites like Harappa and Kalibangan.\n3. Animal remains indicate a diet rich in mutton, beef, pork, poultry, and fish.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        2,
        "Statements 1 and 3 are correct. Statement 2 is incorrect: rice was not a staple food across northern sites; rice grains have been recovered only from Lothal and Rangpur in Gujarat, and it was not a common northern staple."
    ),
    (
        "Consider the following statements regarding the status of women in Harappan society:\n1. The worship of the Mother Goddess indicates that female fertility and nature were highly revered.\n2. Women were excluded from participating in craft production, which was a monopoly of male guilds.\n3. Elaborate hairstyles and ornaments depicted on female figurines suggest that personal grooming and high social representation were accessible to women.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "1 and 3 only", "2 and 3 only", "1, 2 and 3"],
        1,
        "Statements 1 and 3 are correct. Statement 2 is incorrect: women likely participated actively in textile spinning, weaving, bead sorting, and clay molding, and there is no evidence of male-only guilds."
    ),
    (
        "With reference to the religious beliefs of the Harappans, consider the following statements:\n1. The Pashupati seal from Mohenjo-daro depicts a three-faced seated deity surrounded by animals, identified as Proto-Shiva.\n2. The Harappans constructed large stone temples with central sanctum sanctorums to worship their main deities.\n3. Animistic worship of trees, particularly the pipal tree, and animals like the humped bull was highly prevalent.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        2,
        "Statements 1 and 3 are correct. Statement 2 is incorrect: the Harappans did not build temples or monumental places of public worship; their religion was domestic and nature-based."
    ),
    (
        "Consider the following statements regarding the fire altars found in Harappan settlements:\n1. Fire altars built on brick platforms have been excavated at Kalibangan and Lothal.\n2. These altars contain ashes, charcoal, and clay cakes, implying rituals involving animal sacrifice or fire worship.\n3. No fire altars have been reported from the metropolitan sites of Harappa or Mohenjo-daro.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All three statements are correct. Fire altars are prominent at Kalibangan and Lothal, but completely absent at Mohenjo-daro and Harappa."
    ),
    (
        "With reference to the burial customs of the Indus Valley Civilisation, consider the following statements:\n1. The most dominant method of disposing of the dead was complete inhumation in brick-lined graves.\n2. Bodies were typically placed in an East-West direction, with the head pointing east.\n3. Grave goods, including earthenware pottery, mirrors, and beads, were buried with the dead, indicating belief in an afterlife.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 and 3 only", "3 only", "1, 2 and 3"],
        1,
        "Statements 1 and 3 are correct. Statement 2 is incorrect: bodies were typically aligned North-South, with the head pointing north."
    ),
    (
        "Consider the following statements regarding the unique burials discovered at Lothal:\n1. Lothal has yielded evidence of double burials, where two individuals (typically male and female) were buried in a single grave.\n2. The double burials have been interpreted by some scholars as the earliest precursor to the practice of Sati.\n3. Double burials are found in almost 90% of the graves excavated across Lothal.\nWhich of the statements given above is/are correct?",
        ["1 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"],
        1,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: double burials are extremely rare, with only three such graves out of over twenty graves excavated at Lothal."
    ),
    (
        "With reference to the script of the Indus Valley Civilisation, consider the following statements:\n1. The script is pictographic and logo-syllabic, containing around 375 to 400 distinct signs.\n2. The writing style follows a system called Boustrophedon, where consecutive lines are written in alternating directions.\n3. The script was successfully deciphered by Iravatham Mahadevan using a bilingual inscription.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: the Harappan script remains undeciphered to this day; Mahadevan compiled a concordance but did not decipher the signs."
    ),
    (
        "Consider the following statements regarding the Dholavira Signboard:\n1. It consists of ten large, high-resolution signs made of white gypsum paste.\n2. The signboard was found fallen near one of the major defensive gateways of the Citadel.\n3. It represents one of the longest single inscriptions discovered in the Indus Valley Civilisation.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All three statements are correct, describing the gypsum letters, gateway location, and length significance of the Dholavira signboard."
    ),
    (
        "With reference to the famous bronze 'Dancing Girl' figurine, consider the following statements:\n1. She was discovered in the Lower Town of Mohenjo-daro.\n2. The figurine is cast in solid bronze using the lost-wax (cire perdue) technique.\n3. She is depicted standing in a dynamic dance posture with a drum in her hand.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "2 only", "2 and 3 only", "1, 2 and 3"],
        1,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: she is depicted standing in a relaxed pose with one hand on her hip (tribhanga posture) and the other holding bangles, not holding a drum."
    ),
    (
        "Consider the following statements regarding the Steatite 'Priest-King' bust:\n1. It was excavated at Harappa near the grain threshing platforms.\n2. The figure wears an armband, a headband with a circular buckle, and a shawl decorated with trefoil motifs.\n3. The eyes are elongated, half-closed, suggesting a state of meditation or concentration.\nWhich of the statements given above are correct?",
        ["2 and 3 only", "1 and 2 only", "1 and 3 only", "1, 2 and 3"],
        0,
        "Statements 2 and 3 are correct. Statement 1 is incorrect: the Priest-King bust was discovered at Mohenjo-daro, not Harappa."
    ),
    (
        "With reference to the terracotta art of the Harappans, consider the following statements:\n1. Terracotta figurines were hand-modeled and baked in kilns, representing the popular art of the masses.\n2. Toy carts with rotating wheels, hollow clay whistles shaped like birds, and climbing monkeys were common toys.\n3. Clay masks and animal figurines with movable limbs indicate highly creative toy engineering.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, describing the hand-molded terracotta items, bird whistles, and kinetic toy features."
    ),
    (
        "Consider the following statements regarding the Harappan bead manufacturing industry:\n1. Chanhudaro and Lothal were major industrial hubs dedicated to bead production.\n2. Raw materials used for beads included semi-precious stones like carnelian, jasper, agate, and lapis lazuli.\n3. Beads were finished by drilling holes using highly specialized bronze or chert micro-drills.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All three statements are correct and define the bead industry sites, materials, and drilling tools."
    ),
    (
        "With reference to the seals of the Indus Valley Civilisation, consider the following statements:\n1. Most seals were square or rectangular, carved from soft steatite soapstone.\n2. Seals predominantly depicted animals (unicorn, humped bull, elephant) accompanied by short inscriptions.\n3. The primary function of seals was religious worship, as they were worn as amulets around the neck.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "2 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: the primary function of seals was commercial (stamping cargo to verify ownership and integrity); though some were worn as amulets, religious worship was not their primary function."
    ),
    (
        "Consider the following statements regarding the amusements and pastimes of the Harappans:\n1. Cubical chert and terracotta dice with markings similar to modern dice have been excavated.\n2. Board games involving grid patterns and clay game-pieces suggest a precursor to chess.\n3. Cockfighting, animal hunting, and bull-leaping were common sports depicted in art.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct and detail the various board games, dice, and animal sports of Harappan daily life."
    ),
    (
        "With reference to the stone sculptures of the Harappans, consider the following statements:\n1. The red sandstone torso from Harappa displays highly realistic human musculature and organic detail.\n2. Stone sculpture was extremely rare compared to bronze and terracotta art.\n3. Stone carvings were primarily made of hard granite imported from South India.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: stone carvings were made of soft stones like steatite, sandstone, and alabaster, which were locally available or sourced nearby, not hard granite from South India."
    ),
    (
        "Consider the following statements regarding the 'Mother Goddess' terracotta figurines:\n1. They are typically depicted wearing a fan-shaped headdress and multiple necklaces.\n2. Many figurines show soot marks, indicating they were used as oil lamps during rituals.\n3. A unique figurine from Harappa depicts a plant growing out of a woman's womb, symbolizing the Earth Goddess.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All three statements are correct, describing the standard headdress, soot lamps, and the womb-plant Earth Goddess icon."
    ),
    (
        "With reference to the shell and ivory industries of the Harappans, consider the following statements:\n1. Balakot and Lothal were major coastal hubs specializing in shell working and bangle manufacturing.\n2. Ivory combs, dice, and rulers have been discovered in wealthy residential sectors.\n3. Shell ornaments were exported to Mesopotamia, as recorded in Sumerian texts.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All three statements are correct, detailing the coastal shell centers, ivory luxury items, and trade exports."
    ),
    # Additional 30 questions to make a total of 50. Let's write them cleanly.
    (
        "Consider the following statements regarding the status of the ruling class in Harappan society:\n1. There is a complete absence of monarchial palaces, royal tombs, or military armories in Harappan archaeology.\n2. The state was likely ruled by a council of wealthy merchants, priests, or municipal administrators.\n3. The uniformity of weights, measures, and city layouts indicates a highly centralized coordination.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, outlining the lack of standard monarchial markers and theories of merchant/priestly rule."
    ),
    (
        "With reference to the writing script, consider the following statements:\n1. The script is written starting from right to left in the first line, then left to right in the second line.\n2. The signboards at Dholavira show that writing was used for public display on gates.\n3. The total number of signs exceeds 5,000, showing a highly advanced alphabet.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: the number of signs is about 375 to 400, which is logo-syllabic, not an alphabet of 5,000 signs."
    ),
    (
        "Consider the following statements regarding the animal representations on Harappan seals:\n1. The most frequently depicted animal is the mythical 'one-horned unicorn'.\n2. The humped Zebu bull is depicted with high anatomical realism on major trade seals.\n3. Lions and horses are represented as dominant motifs on over 50% of all seals.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: lions are extremely rare, and horses are not depicted on Harappan seals at all."
    ),
    (
        "With reference to the Harappan terracotta toys, consider the following statements:\n1. A clay toy depicting a monkey sliding down a rope has been excavated.\n2. Bull figurines with movable heads operated by string mechanisms have been found.\n3. All toys were coated with a highly glazed glass-like layer called faience.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: most toys were simple unglazed baked clay (terracotta); faience was used for luxury beads and small pots, not common toys."
    ),
    (
        "Consider the following statements regarding the burials at Cemetery H in Harappa:\n1. Cemetery H belongs to the late Harappan phase, showing distinct cultural changes.\n2. The graves contain decorated pottery urns featuring depictions of stars, birds, and peacock motifs.\n3. Urn burials in Cemetery H indicate a shift towards fractional burials and cremation.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, describing the Late Harappan Cemetery H phase, decorative urns, and urn burial shift."
    ),
    (
        "With reference to the religious significance of water in Harappan culture, consider the following statements:\n1. The Great Bath of Mohenjo-daro was used for daily municipal cleaning and swimming competitions.\n2. The placement of the Great Bath on the Citadel suggests it was used for collective ritual purification.\n3. Standardized domestic bathrooms and private wells reflect a high spiritual value placed on cleanliness.\nWhich of the statements given above are correct?",
        ["2 and 3 only", "1 and 2 only", "1 and 3 only", "1, 2 and 3"],
        0,
        "Statements 2 and 3 are correct. Statement 1 is incorrect: the Great Bath was for ritual purification and collective bathing, not swimming competitions or municipal cleaning."
    ),
    (
        "Consider the following statements regarding the Priest-King statue:\n1. The material used is steatite, which was heated after carving to harden it.\n2. The trefoil motif on the shawl is similar to designs found in contemporary Mesopotamian and Egyptian royal art.\n3. The figure is shown wearing a crown decorated with gold foil.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "2 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: the Priest-King wears a simple woven headband with a circular buckle, not a gold foil crown."
    ),
    (
        "With reference to the status of merchants in Harappan society, consider the following statements:\n1. Merchants likely formed a highly influential group that coordinated long-distance trade with Mesopotamia.\n2. The standardization of weights, measures, and raw material distribution suggests state backing of merchant activities.\n3. Merchant residences were restricted to unfortified agricultural suburbs outside the city walls.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: merchant houses were located in the fortified Lower Towns, which were central urban residential sectors."
    ),
    (
        "Consider the following statements regarding the representation of trees in Harappan art:\n1. The pipal tree (Ficus religiosa) is frequently depicted on seals, often with deities emerging from its branches.\n2. The tree representations suggest that animism and forest worship were central to Harappan faith.\n3. Banyan and mango trees are the only trees carved on trade seals.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: the pipal tree is the dominant tree motif; other trees are rarely depicted, and mango trees are absent on seals."
    ),
    (
        "With reference to the manufacture of seals, consider the following statements:\n1. Seals were cut from block steatite, carved in relief, and coated with a glaze before baking.\n2. Baked steatite seals became highly durable and heat-resistant.\n3. Copper and bronze seals were manufactured in much larger numbers than steatite seals.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "2 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: steatite seals make up over 90% of all discovered seals; copper/bronze seals are rare anomalies."
    ),
    (
        "Consider the following statements regarding the Harappan diet in Gujarat:\n1. Millet seeds, including ragi and jowar, have been recovered from sites in Gujarat.\n2. Rice cultivation was practiced at Lothal and Rangpur.\n3. Sugarcane was the primary sweetener used in Harappan desserts.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: there is no archaeological evidence of sugarcane cultivation; honey was likely the primary sweetener."
    ),
    (
        "With reference to the terracotta 'Mother Goddess' figurines, consider the following statements:\n1. They have been found in almost every house at all mature sites, indicating domestic worship.\n2. Soot marks on the fan-shaped headdresses suggest they functioned as oil lamps.\n3. Some figurines show mothers holding infants, reflecting maternal themes.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, describing the domestic occurrence, soot lamps, and maternal representations."
    ),
    (
        "Consider the following statements regarding the Harappan script signs:\n1. Signs are often combined to form compound logograms.\n2. The fish symbol is one of the most frequently occurring signs in the script.\n3. The signs show a clear evolution from early Dravidian or Indo-Aryan alphabets.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: the script remains undeciphered, and its relation to Dravidian or Indo-Aryan languages is a matter of intense academic debate, not a proven fact."
    ),
    (
        "With reference to the layout of Harappan cemeteries, consider the following statements:\n1. Cemeteries were located outside the city fortification walls, away from residential areas.\n2. Graves were arranged in neat rows, reflecting municipal organization in death.\n3. High-status graves featured brick-lined walls, plastering, and hundreds of pottery vessels.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct and define the extramural location, neat rows, and brick lining of high-yield graves."
    ),
    (
        "Consider the following statements regarding the red sandstone human torso from Harappa:\n1. It features sockets in the neck and shoulders for attaching movable limbs.\n2. The anatomical realism of the abdomen and chest is comparable to classical Greek sculpture.\n3. It is carved from a single block of black basalt.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: the torso is made of red sandstone, not black basalt."
    ),
    (
        "With reference to the copper and bronze metallurgy of the Harappans, consider the following statements:\n1. Bronze was manufactured by alloying copper with tin sourced from Afghanistan or Rajasthan.\n2. Utensils like knives, axes, and fish-hooks were made of bronze for domestic work.\n3. Weapons of war, such as swords and shields, were produced in massive quantities.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "2 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: weapons like swords and shields are absent in Harappan tool assemblies; they mostly made domestic tools and simple arrows/spears."
    ),
    (
        "Consider the following statements regarding the status of artisans in Harappan towns:\n1. Potters, metal casters, and beadmakers lived in dedicated residential quarters within the Lower Town.\n2. The proximity of bead factories to administrative quarters suggests state control of high-value craft production.\n3. Artisans did not utilize standardized weights, which were reserved for international merchants.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: artisans used standard small weights (binary scales) to measure precious stones, metals, and shell materials."
    ),
    (
        "With reference to the pictographic signs on Harappan seals, consider the following statements:\n1. A rectangular seal from Harappa depicts a deity fighting two tigers, resembling the Mesopotamian Gilgamesh motif.\n2. Seals frequently depict cross-legged figures sitting in yogic postures.\n3. Many seals show ships with sails, confirming maritime contacts.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, describing the Gilgamesh tiger motif, yogic seating, and sailboat representations."
    ),
    (
        "Consider the following statements regarding Harappan religious structures:\n1. Public temples with pillars and altars have been discovered at Mohenjo-daro.\n2. Great platforms built of mud-brick at Kalibangan housed fire altars for public rituals.\n3. The Great Bath functioned as a public, ritualistic space for water purification.",
        ["2 and 3 only", "1 and 2 only", "1 and 3 only", "1, 2 and 3"],
        0,
        "Statements 2 and 3 are correct. Statement 1 is incorrect: no public temple structures have been discovered anywhere in the Indus Valley Civilisation."
    ),
    (
        "With reference to the fractional burials in Harappan sites, consider the following statements:\n1. Fractional burials involve burying only selected bones after exposing the body to elements.\n2. Urn burials containing bone fragments and ashes are typical of fractional burials.\n3. Fractional burials were the only method of disposal used at Mohenjo-daro.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: complete inhumation was also practiced at Mohenjo-daro, and fractional burials were not the sole method."
    ),
    (
        "Consider the following statements regarding the stone lingas and yonis found in Indus sites:\n1. Small stone cylinders and rings have been interpreted by archaeologists as symbols of phallic (linga) and vulva (yoni) worship.\n2. These stone objects suggest the origin of sectarian Shaivism and fertility rituals.\n3. Some historians argue these objects were simply weight units or structural components.",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements represent current historiographical arguments and interpretations regarding stone lingas and yonis."
    ),
    (
        "With reference to the children's toys of the Harappans, consider the following statements:\n1. Terracotta toy carts were miniature replicas of actual wooden bullock carts used for transport.\n2. Clay bird whistles are hollow structures that produce whistling sounds when blown.\n3. Toys were made exclusively for children of the ruling elite on the Citadel.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "2 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: toys have been found in abundance throughout the Lower Town houses, indicating they were common for all children."
    ),
    (
        "Consider the following statements regarding the Priest-King shawls:\n1. The shawl is decorated with a trefoil pattern that was painted with red cinnabar dye.\n2. The trefoil motif represents a solar or astral symbol in Bronze Age iconography.\n3. The Priest-King statue is depicted with his beard shaved completely.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "2 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: the Priest-King is depicted with a neatly trimmed and detailed beard, and only the upper lip is shaved."
    ),
    (
        "With reference to the Harappan script writing direction, consider the following statements:\n1. The writing direction is indicated by the cramping of characters on the left side of seals.\n2. Scribes started writing from the right and ran out of space on the left, proving right-to-left direction.\n3. Boustrophedon writing style is also found in early Greek inscriptions.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, describing the script compression on the left, right-to-left start, and Boustrophedon parallels."
    ),
    (
        "Consider the following statements regarding the status of artisans at Chanhudaro:\n1. Excavations revealed beadmaker shops with furnaces and stone drill bits.\n2. Metal workers at Chanhudaro manufactured bronze toys and copper knives.\n3. Artisans formed a separate lower caste that was excluded from the main town quarters.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: Chanhudaro was an unfortified suburb dedicated to craft production, and there is no evidence of caste exclusion."
    ),
    (
        "With reference to the pipal tree in Harappan religion, consider the following statements:\n1. It is depicted on seals with leaves showing three distinct lobes.\n2. Deities are shown standing inside a cleft of the tree branches, receiving worshippers.\n3. The pipal tree continues to hold sacred status in modern Indian religions, showing cultural continuity.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, outlining the seal depiction, deities in branches, and religious continuity."
    ),
    (
        "Consider the following statements regarding the Zebu humped bull representations:\n1. The humped bull was a sacred animal and a symbol of power or fertility.\n2. Humped bull figurines were carved primarily from ivory for international trade.\n3. It is depicted with a large hump and curved horns on major steatite seals.\nWhich of the statements given above is/are correct?",
        ["1 and 3 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 3 are correct. Statement 2 is incorrect: humped bulls were carved from steatite (seals) and molded in clay (terracotta), not primarily ivory."
    ),
    (
        "With reference to the board games played by the Harappans, consider the following statements:\n1. Terracotta and stone game boards with grids of squares have been excavated.\n2. Clay and shell casting counters have been found alongside game boards.\n3. Board games were used exclusively for astronomical calculations by priests.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "2 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: board games were recreational amusements played by the public, not exclusive priestly calculators."
    ),
    (
        "Consider the following statements regarding the double burials at Lothal:\n1. They represent three distinct graves, each containing a male and a female skeleton.\n2. The skeletons were buried with clay pots containing food offerings.\n3. Skeletons show clear evidence of violent trauma, indicating forced sacrifice.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: the skeletons do not show clear signs of violent trauma or forced sacrifice; their death remains unexplained."
    ),
    (
        "With reference to the script signs on the Dholavira signboard, consider the following statements:\n1. The signs are about 37 cm tall, carved in wooden boards that decayed over time.\n2. The letters were filled with white crystalline gypsum paste to stand out against the wood.\n3. The inscription remains undeciphered, similar to other Harappan script texts.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, describing the signboard height, gypsum filling, and undeciphered status."
    )
]

practice_data_hin = [
    (
        "हड़प्पा सभ्यता की सामाजिक संरचना के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. शहरों में आवासों का लेआउट विभिन्न व्यावसायिक वर्गों के बीच स्पष्ट विभाजन का संकेत देता है।\n2. पुरातात्विक साक्ष्य उत्तर वैदिक काल की तरह एक अत्यधिक कठोर, जन्म-आधारित जाति व्यवस्था के अस्तित्व की पुष्टि करते हैं।\n3. मिट्टी की नारी आकृतियों की प्रचुरता के कारण कई इतिहासकारों ने मातृसत्तात्मक या मातृवंशीय समाज की संभावना का सुझाव दिया है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        2,
        "कथन 1 और 3 सही हैं। कथन 2 गलत है: सिंधु घाटी सभ्यता में जन्म आधारित कठोर जाति व्यवस्था का कोई पुरातात्विक साक्ष्य नहीं मिला है; सामाजिक विभाजन व्यावसायिक और धन-आधारित थे।"
    ),
    (
        "हड़प्पा वासियों के पहनावे और आभूषणों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. आबादी द्वारा सूती और ऊनी दोनों प्रकार के वस्त्रों का व्यापक रूप से उपयोग किया जाता था।\n2. हार, बाजूबंद और अंगूठियां जैसे आभूषण विशेष रूप से केवल महिलाओं द्वारा पहने जाते थे।\n3. तराशी गई पत्थर की मूर्तियाँ, जैसे कि पुरोहित-राजा (Priest-King), कंधे पर लिपटे हुए अलंकृत शॉल को दर्शाती हैं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "Clean 1 और 3", "1, 2 और 3"],
        2,
        "कथन 1 और 3 सही हैं। कथन 2 गलत है: कब्रों की खोजों से प्रमाणित होता है कि आभूषण पुरुष और महिला दोनों द्वारा पहने जाते थे।"
    ),
    (
        "हड़प्पा वासियों की सौंदर्य प्रसाधन और श्रृंगार संबंधी आदतों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. चन्हुदड़ो से सौंदर्य प्रसाधन सामग्री के सीधे साक्ष्य मिले हैं, जिसमें लिपस्टिक के रूप में पहचानी गई वस्तु शामिल है।\n2. आँखों का काजल और बालों के तेल रखने के लिए मिट्टी और कांसे की छोटी डिब्बियों का उपयोग किया जाता था।\n3. समृद्ध परिवारों में व्यक्तिगत श्रृंगार के लिए सुंदर हैंडल वाले कांसे के दर्पण आम थे।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        3,
        "तीनों कथन सही हैं, जो हड़प्पा वासियों के उन्नत सौंदर्य प्रसाधनों, काजल डिब्बियों और कांसे के दर्पणों का वर्णन करते हैं।"
    ),
    (
        "सिंधु घाटी के लोगों के खान-पान के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. खाए जाने वाले मुख्य अनाज गेहूं और जौ थे, जिन्हें बड़े सार्वजनिक अन्नागारों में संग्रहित किया जाता था।\n2. हड़प्पा और कालीबंगन जैसे सभी प्रमुख उत्तरी स्थलों पर चावल मुख्य भोजन के रूप में दैनिक रूप से खाया जाता था।\n3. पशु अवशेषों से पता चलता है कि उनके भोजन में भेड़, सूअर, मवेशियों का मांस, मुर्गा और मछली शामिल थे।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        2,
        "कथन 1 और 3 सही हैं। कथन 2 गलत है: चावल उत्तरी स्थलों पर मुख्य भोजन नहीं था; चावल के दाने केवल गुजरात के लोथल और रंगपुर से मिले हैं।"
    ),
    (
        "हड़प्पा समाज में महिलाओं की स्थिति के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मातृदेवी की पूजा से संकेत मिलता है कि नारी की उर्वरता और प्रकृति का अत्यधिक सम्मान किया जाता था।\n2. महिलाओं को शिल्प उत्पादन में भाग लेने से बाहर रखा गया था, जिस पर केवल पुरुषों का एकाधिकार था।\n3. नारी मूर्तियों पर दर्शाए गए जटिल केशविन्यास और आभूषण बताते हैं कि महिलाओं को सौंदर्य प्रसाधन और सामाजिक प्रतिनिधित्व की स्वतंत्रता थी।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 1 और 3", "केवल 2 और 3", "1, 2 और 3"],
        1,
        "कथन 1 और 3 सही हैं। कथन 2 गलत है: सूत कातने, बुनाई, मनका छांटने और मिट्टी ढालने में महिलाएं सक्रिय थीं, और पुरुष-मात्र संघों का कोई प्रमाण नहीं है।"
    ),
    (
        "हड़प्पा वासियों के धार्मिक विश्वासों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मोहनजोदड़ो से प्राप्त पशुपति मुहर में तीन मुख वाले देव को योगासन में बैठे और जंगली जानवरों से घिरे दिखाया गया है, जिन्हें आद्य-शिव माना जाता है।\n2. हड़प्पा वासियों ने अपने मुख्य देवताओं की पूजा के लिए केंद्रीय गर्भगृह वाले बड़े पत्थर के मंदिरों का निर्माण किया था।\n3. पीपल के पेड़ और कूबड़ वाले सांड जैसे पशुओं की प्रकृति पूजा अत्यधिक प्रचलित थी।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        2,
        "कथन 1 and 3 सही हैं। कथन 2 गलत है: हड़प्पा सभ्यता में कोई मंदिर या सार्वजनिक पूजा स्थल नहीं मिले हैं; धर्म व्यक्तिगत और प्रकृति-केंद्रित था।"
    ),
    (
        "हड़प्पा बस्तियों में पाए गए अग्निकुंडों (fire altars) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. कालीबंगन और लोथल में ईंटों के चबूतरों पर बने अग्निकुंड उत्खनन में मिले हैं।\n2. इन अग्निकुंडों में राख, कोयला और मिट्टी के पिंड मिले हैं, जो अग्नि पूजा या बलि प्रथा का संकेत देते हैं।\n3. महानगरों जैसे हड़प्पा और मोहनजोदड़ो से कोई भी अग्निकुंड रिपोर्ट नहीं किया गया है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं। कालीबंगन और लोथल में अग्निकुंड मिले हैं, लेकिन वे मोहनजोदड़ो और हड़प्पा में पूरी तरह अनुपस्थित हैं।"
    ),
    (
        "सिंधु घाटी सभ्यता की शवाधान प्रथाओं के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मृतकों के निपटान की सबसे प्रमुख विधि पक्की ईंटों की कब्रों में पूर्ण शवाधान (दफनाना) थी।\n2. शवों को आमतौर पर पूर्व-पश्चिम दिशा में लिटाया जाता था, जिसका सिर पूर्व की ओर होता था।\n3. कब्रों में मिट्टी के बर्तन, दर्पण और मनके रखे जाते थे, जो पारलौकिक जीवन (afterlife) में विश्वास को दर्शाते हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1 और 3", "केवल 3", "1, 2 और 3"],
        1,
        "कथन 1 और 3 सही हैं। कथन 2 गलत है: शवों को आमतौर पर उत्तर-दक्षिण दिशा में दफनाया जाता था, जिसमें सिर उत्तर की ओर होता था।"
    ),
    (
        "लोथल से प्राप्त विशिष्ट कब्रों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. लोथल से युगल शवाधान (double burials) के साक्ष्य मिले हैं, जहाँ दो व्यक्तियों (पुरुष और महिला) को एक साथ एक ही कब्र में दफनाया गया था।\n2. इन युगल कब्रों को कुछ विद्वानों द्वारा सती प्रथा का सबसे प्राचीन पूर्ववर्ती रूप माना गया है।\n3. लोथल में खोजे गए लगभग 90% कब्रों में युगल शवाधान पाया गया है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1", "केवल 1 और 2", "केवल 2 और 3", "1, 2 और 3"],
        1,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: युगल शवाधान अत्यंत दुर्लभ हैं, लोथल से खोजे गए 20 से अधिक कब्रों में केवल तीन ऐसी कब्रें मिली हैं।"
    ),
    (
        "सिंधु घाटी सभ्यता की लिपि के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह लिपि चित्रात्मक (pictographic) और लोगो-सिलेबिक है, जिसमें लगभग 375 से 400 तक विशिष्ट चिन्ह हैं।\n2. इसकी लेखन शैली को बोउस्ट्रोफेडन (Boustrophedon) कहा जाता है, जहाँ क्रमिक पंक्तियाँ बारी-बारी से विपरीत दिशा में लिखी जाती हैं।\n3. इस लिपि को इरावथम महादेवन द्वारा एक द्विभाषी शिलालेख की सहायता से सफलतापूर्वक पढ़ा जा चुका है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: हड़प्पा लिपि आज तक पढ़ी नहीं जा सकी है; महादेवन ने केवल चिन्हों का संकलन किया था।"
    ),
    (
        "धोलावीरा के सूचना-पट्ट (Signboard) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इसमें सफेद जिप्सम लेप से बने दस बड़े अक्षर शामिल हैं।\n2. यह सूचना-पट्ट किले (Citadel) के एक मुख्य द्वार के पास गिरा हुआ मिला था।\n3. यह सिंधु घाटी सभ्यता में खोजे गए सबसे लंबे एकल अभिलेखों में से एक का प्रतिनिधित्व करता है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        3,
        "तीनों कथन सही हैं, जो सफेद अक्षरों, किले के द्वार और धोलावीरा सूचना-पट्ट की विशिष्टता को दर्शाते हैं।"
    ),
    (
        "कांस्य की प्रसिद्ध 'नर्तकी' (Dancing Girl) की मूर्ति के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इसे मोहनजोदड़ो के निचले नगर (Lower Town) से खोजा गया था।\n2. यह मूर्ति ठोस कांसे से लुप्त-मोम (lost-wax/cire perdue) तकनीक द्वारा बनाई गई है।\n3. उसे हाथ में ढोलक लिए नृत्य की एक गतिशील मुद्रा में दर्शाया गया है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 2", "केवल 2 और 3", "1, 2 और 3"],
        1,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: उसे कूल्हे पर एक हाथ रखे हुए त्रिभंग मुद्रा में खड़े दर्शाया गया है, न कि ढोलक बजाते हुए।"
    ),
    (
        "सेलखड़ी (Steatite) से बनी पुरोहित-राजा (Priest-King) की मूर्ति के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इसे हड़प्पा में अनाज कूटने वाले गोलाकार चबूतरों के पास खोजा गया था।\n2. इस मूर्ति ने बाजूबंद, माथे पर गोल बटन वाला पट्टा और तिपतिया (trefoil) डिजाइनों से सजा शॉल पहना हुआ है।\n3. इसकी आँखें लंबी और आधी खुली हुई हैं, जो ध्यान या एकाग्रता की स्थिति को दर्शाती हैं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 2 और 3", "केवल 1 और 2", "केवल 1 और 3", "1, 2 और 3"],
        0,
        "कथन 2 और 3 सही हैं। कथन 1 गलत है क्योंकि पुरोहित-राजा की मूर्ति मोहनजोदड़ो से मिली थी, हड़प्पा से नहीं।"
    ),
    (
        "हड़प्पा वासियों की मिट्टी की कला (terracotta art) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मिट्टी की मूर्तियाँ हाथ से बनाई जाती थीं और भट्टियों में पकाई जाती थीं, जो आम लोगों की कला को दर्शाती हैं।\n2. घूमने वाले पहियों वाली खिलौना गाड़ियाँ, पक्षियों के आकार की सीटी और रस्सी पर चढ़ने वाले बंदर आम खिलौने थे।\n3. मिट्टी के मुखौटे और हिलने वाले अंगों वाले खिलौने उनकी रचनात्मक खिलौना इंजीनियरिंग को दर्शाते हैं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "Clean 1 और 3"],
        0,
        "तीनों कथन सही हैं और हाथ से बने खिलौनों, सीटी और खिलौनों की बनावट का विवरण देते हैं।"
    ),
    (
        "हड़प्पा की मनका निर्माण (bead manufacturing) उद्योग के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. चन्हुदड़ो और लोथल मनका उत्पादन के प्रमुख औद्योगिक केंद्र थे।\n2. मनके बनाने के लिए अकीक (carnelian), यशब (jasper) और लाजवर्त (lapis lazuli) जैसे पत्थरों का उपयोग होता था।\n3. मनकों में छेद करने के लिए कांसे या चर्ट से बने विशेष सूक्ष्म-ड्रिल (micro-drills) का उपयोग किया जाता था।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        3,
        "तीनों कथन सही हैं, जो मनका उद्योग के स्थलों, कच्चे माल और छिद्रण उपकरणों को स्पष्ट करते हैं।"
    ),
    (
        "सिंधु घाटी सभ्यता की मुहरों (seals) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. अधिकांश मुहरें चौकोर या आयताकार थीं, जिन्हें नरम सेलखड़ी पत्थर से बनाया जाता था।\n2. मुहरों पर मुख्य रूप से जानवरों (एक सींग वाला बैल, कूबड़ वाला सांड, हाथी) और छोटे लेख अंकित थे।\n3. मुहरों का प्राथमिक कार्य धार्मिक पूजा था और इन्हें ताबीज के रूप में गले में पहना जाता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 2", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: मुहरों का मुख्य कार्य व्यावसायिक था (सामान की सुरक्षा के लिए गीली मिट्टी पर छाप लगाना); यद्यपि कुछ ताबीज के रूप में भी प्रयुक्त होती थीं, पर मुख्य कार्य पूजा नहीं था।"
    ),
    (
        "हड़प्पा वासियों के खेलों और मनोरंजन के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. घनाकार चर्ट और मिट्टी के पासे (dice), जिन पर आधुनिक पासों की तरह निशान थे, उत्खनित किए गए हैं।\n2. ग्रिड पैटर्न वाले बोर्ड और मिट्टी की गोटियाँ शतरंज के शुरुआती रूप की ओर इशारा करती हैं।\n3. तीतर-मुर्गों की लड़ाई, जानवरों का शिकार और सांडों से लड़ना कला में दर्शाए गए आम खेल थे।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो पासों, शतरंज जैसे खेलों और मनोरंजन का सटीक विवरण देते हैं।"
    ),
    (
        "हड़प्पा की पाषाण मूर्तियों (stone sculptures) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. हड़प्पा से प्राप्त लाल बलुआ पत्थर का मानव धड़ (torso) अत्यंत यथार्थवादी शारीरिक विवरण दर्शाता है।\n2. कांस्य और मिट्टी की कला की तुलना में पत्थर की मूर्तियाँ बहुत दुर्लभ थीं।\n3. पत्थर की अधिकांश मूर्तियाँ दक्षिण भारत से आयातित कठोर ग्रेनाइट से बनाई जाती थीं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि पत्थर की मूर्तियाँ सेलखड़ी और बलुआ पत्थर जैसे स्थानीय नरम पत्थरों से बनती थीं, दक्षिण भारत के ग्रेनाइट से नहीं।"
    ),
    (
        "मिट्टी की 'मातृदेवी' (Mother Goddess) की मूर्तियों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इन्हें आमतौर पर पंखे के आकार के मुकुट और कई हार पहने हुए दर्शाया जाता था।\n2. कई मूर्तियों पर काजल या कालिख के निशान मिले हैं, जिससे पता चलता है कि वे दीये की तरह प्रयुक्त होती थीं।\n3. हड़प्पा से प्राप्त एक विशिष्ट मूर्ति में एक महिला के गर्भ से पौधा निकलता दिखाया गया है, जो पृथ्वी देवी का प्रतीक है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो मुकुट, कालिख के चिह्नों और पृथ्वी देवी की अनूठी मूर्ति का विवरण देते हैं।"
    ),
    (
        "हड़प्पा के शंख और हाथीदांत उद्योगों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. बालाकोट और लोथल शंख के काम और चूड़ियाँ बनाने में विशेषज्ञता रखने वाले तटीय केंद्र थे।\n2. समृद्ध आवासीय क्षेत्रों से हाथीदांत की कंघियां, पासे और पैमाने मिले हैं।\n3. शंख के आभूषणों का निर्यात मेसोपोटामिया में किया जाता था, जिसके प्रमाण सुमेरियन ग्रंथों में मिलते हैं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        3,
        "तीनों कथन सही हैं और शंख उद्योग, हाथीदांत विलासिता और समुद्री निर्यात को स्पष्ट करते हैं।"
    ),
    # Additional 30 questions
    (
        "हड़प्पा समाज में शासक वर्ग की स्थिति के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. हड़प्पा पुरातत्व में किसी भी राजसी महल, शाही कब्रों या सैन्य शस्त्रागारों का पूर्ण अभाव है।\n2. राज्य संभवतः धनी व्यापारियों, पुरोहितों या नागरिक प्रशासकों की एक परिषद द्वारा चलाया जाता था।\n3. बाट-माप और नगर नियोजन की व्यापक एकरूपता एक मजबूत केंद्रीय समन्वय का संकेत देती है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं और राजशाही के प्रतीकों की कमी तथा व्यापारियों/प्रशासकों के शासन के सिद्धांतों को स्पष्ट करते हैं।"
    ),
    (
        "लेखन लिपि के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह लिपि पहली पंक्ति में दाएं से बाएं और दूसरी पंक्ति में बाएं से दाएं लिखी जाती थी।\n2. धोलावीरा का सूचना-पट्ट दर्शाता है कि लेखन का उपयोग प्रवेश द्वारों पर सार्वजनिक प्रदर्शन के लिए होता था।\n3. लिपि में चिन्हों की कुल संख्या 5,000 से अधिक है, जो एक बहुत बड़ी वर्णमाला दर्शाती है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि लिपि में चिन्हों की संख्या 375 से 400 है, जो वर्णमाला नहीं बल्कि लोगो-सिलेबिक प्रणाली है।"
    ),
    (
        "हड़प्पा मुहरों पर पशुओं के चित्रण के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. सबसे अधिक चित्रित किया जाने वाला पशु काल्पनिक 'एक सींग वाला सिंह' (unicorn) है।\n2. कूबड़ वाले सांड (Zebu) को व्यापारिक मुहरों पर अत्यधिक शारीरिक यथार्थवाद के साथ चित्रित किया गया है।\n3. शेर और घोड़े मुहरों पर चित्रित होने वाले सबसे प्रमुख जीव हैं जो 50% से अधिक मुहरों पर मिलते हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: शेर अत्यंत दुर्लभ हैं, और घोड़े मुहरों पर बिल्कुल नहीं दर्शाए गए हैं।"
    ),
    (
        "हड़प्पा की मिट्टी के खिलौनों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. रस्सी पर नीचे सरकने वाले बंदर का खिलौना उत्खनन में मिला है।\n2. धागे से कूबड़ वाले सांड के हिलने वाले सिर को नियंत्रित करने वाले खिलौने मिले हैं।\n3. सभी खिलौनों पर काँच जैसा चमकदार लेप चढ़ाया जाता था जिसे फेयॉन्स (faience) कहते थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "Clean 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि खिलौने साधारण पकी मिट्टी के होते थे, फेयॉन्स का उपयोग केवल कीमती मोतियों और डिब्बियों के लिए होता था।"
    ),
    (
        "हड़प्पा में कब्रिस्तान H (Cemetery H) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. कब्रिस्तान H उत्तर हड़प्पा काल (late Harappan phase) से संबंधित है, जो सांस्कृतिक बदलाव दर्शाता है।\n2. इन कब्रों से प्राप्त कलशों पर तारों, पक्षियों और मोरों के सुंदर चित्र बने हुए हैं।\n3. कब्रिस्तान H में कलश शवाधान (urn burial) आंशिक शवाधान और दाह संस्कार की ओर झुकाव दर्शाते हैं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं और कब्रिस्तान H के अवशेषों, कलशों और दाह संस्कार पद्धतियों का विवरण देते हैं।"
    ),
    (
        "हड़प्पा संस्कृति में पानी के धार्मिक महत्व के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मोहनजोदड़ो के विशाल स्नानागार का उपयोग दैनिक सफाई और तैराकी प्रतियोगिताओं के लिए होता था।\n2. किले (Citadel) पर विशाल स्नानागार की स्थिति बताती है कि यह अनुष्ठानिक शुद्धि के लिए था।\n3. घरों में पक्के स्नानघर और निजी कुएँ स्वच्छता को पवित्र मानने के आध्यात्मिक महत्व को दर्शाते हैं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 2 और 3", "केवल 1 और 2", "केवल 1 और 3", "1, 2 और 3"],
        0,
        "कथन 2 और 3 सही हैं। कथन 1 गलत है क्योंकि स्नानागार अनुष्ठानिक शुद्धि के लिए था, न कि खेलकूद या दैनिक तैराकी के लिए।"
    ),
    (
        "पुरोहित-राजा (Priest-King) की मूर्ति के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इसे सेलखड़ी पत्थर से तराश कर भट्टी में पकाया गया था ताकि यह मजबूत हो सके।\n2. शॉल पर बना तिपतिया (trefoil) डिजाइन मेसोपोटामिया और मिस्र के शाही कला प्रतिरूपों के समान है।\n3. इस मूर्ति के सिर पर सोने की पन्नी से मढ़ा हुआ मुकुट दर्शाया गया है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 2", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि पुरोहित-राजा ने सोने के मुकुट के बजाय गोल बटन वाला एक सामान्य सिरबंद पहना हुआ है।"
    ),
    (
        "हड़प्पा समाज में व्यापारियों की स्थिति के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. व्यापारियों का एक अत्यधिक प्रभावशाली वर्ग था जो मेसोपोटामिया के साथ लंबी दूरी के व्यापार को नियंत्रित करता था।\n2. बाटों, मापों और कच्चे माल के वितरण का मानकीकरण व्यापारी गतिविधियों को राजकीय समर्थन की ओर इशारा करता है।\n3. व्यापारियों के आवास शहर के बाहर बिना किलेबंदी वाले कृषि उपनगरों तक सीमित थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि व्यापारियों के बड़े घर किलेबंद निचले नगर के मुख्य आवासीय क्षेत्रों में थे।"
    ),
    (
        "हड़प्पा कला में पेड़ों के चित्रण के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. पीपल के पेड़ (Ficus religiosa) को अक्सर मुहरों पर चित्रित किया गया है, जिसमें देवों को उसकी टहनियों से निकलते दर्शाया गया है।\n2. पेड़ों के चित्रण से पता चलता है कि उनके धर्म में वन पूजा और प्रकृति का गहरा स्थान था।\n3. बरगद और आम के पेड़ ही मुहरों पर चित्रित होने वाले एकमात्र पेड़ हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["Clean 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि पीपल का पेड़ सबसे प्रमुख है, आम का चित्रण नहीं मिला है।"
    ),
    (
        "मुहरों के निर्माण के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मुहरों को सेलखड़ी के चौकोर टुकड़ों से काट कर उभरे हुए रूप में तराशा जाता था और पकाने से पहले चमकीला लेप लगाया जाता था।\n2. पकाने के बाद सेलखड़ी की मुहरें अत्यधिक टिकाऊ और घिसावट रोधी बन जाती थीं।\n3. तांबे और कांसे की मुहरों का उत्पादन सेलखड़ी की मुहरों से बहुत अधिक मात्रा में किया जाता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 2", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि सेलखड़ी की मुहरें कुल खोजों का 90% से अधिक हैं, धातु की मुहरें दुर्लभ अपवाद हैं।"
    ),
    (
        "गुजरात में हड़प्पा वासियों के खान-पान के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. गुजरात के स्थलों से बाजरा, रागी और ज्वार के दाने बरामद किए गए हैं।\n2. लोथल और रंगपुर में चावल की खेती की जाती थी।\n3. गन्ने का रस हड़प्पा के मीठे व्यंजनों का प्राथमिक आधार था।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि गन्ने की खेती के कोई पुरातात्विक साक्ष्य नहीं मिले हैं; मिठास के लिए शहद का उपयोग होता था।"
    ),
    (
        "मिट्टी की 'मातृदेवी' मूर्तियों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. ये मूर्तियाँ लगभग हर घर से घरेलू पूजा के साक्ष्य के रूप में प्राप्त हुई हैं।\n2. पंखे के आकार के मुकुटों पर मिले कालिख के निशान उनके दीये के रूप में प्रयोग का संकेत देते हैं।\n3. कुछ मूर्तियों में माँ को शिशु को गोद में लिए हुए वात्सल्य भाव में दिखाया गया है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो घरेलू उपलब्धता, कालिख लैंप और मातृत्व रूपों का विवरण देते हैं।"
    ),
    (
        "हड़प्पा लिपि के चिन्हों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. विभिन्न चिन्हों को मिलाकर संयुक्त चित्रलेख (compound logograms) बनाए जाते थे।\n2. मछली (fish) का चिन्ह लिपि में सबसे अधिक बार दोहराया जाने वाला प्रतीक है।\n3. ये चिन्ह स्पष्ट रूप से प्रारंभिक द्रविड़ या इंडो-आर्यन वर्णमाला के विकास को दर्शाते हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि लिपि अभी तक अपठित है और द्रविड़ या इंडो-आर्यन से इसका सीधा जुड़ाव सिद्ध नहीं हुआ है।"
    ),
    (
        "हड़प्पा के कब्रिस्तानों के नियोजन के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. कब्रिस्तान शहर की मुख्य सुरक्षा दीवार के बाहर रिहायशी इलाकों से दूर बनाए जाते थे।\n2. कब्रों को साफ कतारों में व्यवस्थित किया जाता था, जो मृत्यु में भी नागरिक अनुशासन दर्शाती हैं।\n3. उच्च वर्ग के लोगों की कब्रें ईंटों से पक्की की जाती थीं और उनमें सैकड़ों बर्तन रखे जाते थे।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं और कब्रों के बाहरी नियोजन, कतारबद्धता और पक्की कब्रों का विवरण देते हैं।"
    ),
    (
        "हड़प्पा से प्राप्त लाल बलुआ पत्थर के मानव धड़ (torso) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इसमें सिर और कंधे को जोड़ने के लिए छेद बने हैं जिससे घूमने वाले अंग लगाए जा सकें।\n2. इस धड़ की शारीरिक रचना और मांसपेशियों की गोलाई प्राचीन ग्रीक मूर्तिकला के समान यथार्थवादी है।\n3. इसे काले बेसाल्ट के एक ही खंड से तराशा गया है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि यह लाल बलुआ पत्थर से बना है, बेसाल्ट से नहीं।"
    ),
    (
        "हड़प्पा वासियों के तांबे और कांसे के धातुकर्म के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. कांसे का निर्माण तांबे में टिन मिलाकर किया जाता था, जिसे अफगानिस्तान या राजस्थान से मंगाया जाता था।\n2. घरेलू कार्यों के लिए कांसे की चाकुओं, कुल्हाड़ियों और मछली पकड़ने के कांटों का निर्माण होता था।\n3. युद्ध के हथियार जैसे तलवारें और ढालें बहुत बड़ी मात्रा में उत्पादित की जाती थीं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 2", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि तलवारें और सुरक्षा कवच जैसे युद्ध के हथियार हड़प्पा संस्कृति में अनुपस्थित हैं।"
    ),
    (
        "हड़प्पा शहरों में कारीगरों की स्थिति के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. कुम्हार, धातु ढालने वाले और मनका बनाने वाले निचले नगर के भीतर समर्पित बस्तियों में रहते थे।\n2. प्रशासनिक भवनों के समीप मनके के कारखानों की स्थिति कीमती शिल्पों पर नियंत्रण दर्शाती है।\n3. कारीगर मानकीकृत बाटों का उपयोग नहीं करते थे, वे केवल अंतरराष्ट्रीय व्यापारियों के लिए आरक्षित थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि कीमती पत्थरों और धातु को मापने के लिए कारीगर छोटे द्वि-आधारी बाटों का उपयोग करते थे।"
    ),
    (
        "हड़प्पा मुहरों पर चित्रात्मक प्रतीकों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. हड़प्पा से प्राप्त एक आयताकार मुहर पर एक देव को दो बाघों से लड़ते दिखाया गया है, जो मेसोपोटामिया के गिलगामेश प्रतिरूप के समान है।\n2. मुहरों पर अक्सर पालथी मारकर बैठे देवताओं को योगासन मुद्रा में दर्शाया गया है।\n3. कई मुहरों पर मस्तूल और पाल वाली नावों के चित्र बने हैं, जो समुद्री व्यापार की पुष्टि करते हैं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं और गिलगामेश बाघ प्रतिरूप, योगासन और जहाजों के चित्रण का विवरण देते हैं।"
    ),
    (
        "हड़प्पा के धार्मिक स्थलों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मोहनजोदड़ो से खंभों और वेदियों वाले बड़े सार्वजनिक मंदिर खोजे गए हैं।\n2. कालीबंगन में मिट्टी की ईंटों के बड़े चबूतरों पर सार्वजनिक अनुष्ठानों के लिए अग्निकुंड बने थे।\n3. विशाल स्नानागार पवित्र स्नान और अनुष्ठानिक शुद्धि के लिए एक सामूहिक धार्मिक स्थल था।",
        ["केवल 2 और 3", "केवल 1 और 2", "केवल 1 और 3", "1, 2 और 3"],
        0,
        "कथन 2 और 3 सही हैं। कथन 1 गलत है क्योंकि पूरी सिंधु घाटी सभ्यता में कोई भी मंदिर संरचना नहीं मिली है।"
    ),
    (
        "हड़प्पा स्थलों में आंशिक शवाधान (fractional burial) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. आंशिक शवाधान में शव को खुले में छोड़ने के बाद बची हुई चुनिंदा हड्डियों को दफनाया जाता था।\n2. हड्डियों और राख को कलश में रखकर दफनाना आंशिक शवाधान की ही एक विधि थी।\n3. आंशिक शवाधान मोहनजोदड़ो में शव निपटान की एकमात्र विधि थी।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि मोहनजोदड़ो में पूर्ण शवाधान भी किया जाता था, आंशिक एकमात्र विधि नहीं थी।"
    ),
    (
        "सिंधु स्थलों से प्राप्त पत्थर के लिंग और योनि के टुकड़ों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. छोटे पत्थर के बेलनों और छल्लों को पुराविदों द्वारा लिंग और योनि पूजा का प्रतीक माना गया है।\n2. ये वस्तुएं बाद के शैव संप्रदाय और उर्वरता पूजा के उद्भव की ओर इशारा करती हैं।\n3. कुछ इतिहासकारों का तर्क है कि ये पत्थर के टुकड़े वास्तव में संरचनात्मक भाग या बाट थे।",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन लिंग-योनि टुकड़ों के संबंध में इतिहासकारों के विभिन्न तर्कों और व्याख्याओं को दर्शाते हैं।"
    ),
    (
        "हड़प्पा वासियों के बच्चों के खिलौनों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मिट्टी की खिलौना गाड़ियाँ परिवहन के लिए प्रयुक्त होने वाली वास्तविक बैलगाड़ियों की हुबहू छोटी नकल थीं।\n2. मिट्टी की चिड़िया के आकार की सीटी एक खोखली संरचना है जिसे फूंकने पर सीटी बजती है।\n3. खिलौने केवल किले (Citadel) पर रहने वाले शासक वर्ग के बच्चों के लिए ही बनाए जाते थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 2", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि खिलौने निचले नगर के घरों से भी भारी मात्रा में मिले हैं, जिससे पता चलता है कि ये आम बच्चों के लिए भी थे।"
    ),
    (
        "पुरोहित-राजा के शॉल के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. शॉल पर बना तिपतिया (trefoil) डिजाइन लाल हिंगुल (cinnabar) रंग से रंगा गया था।\n2. तिपतिया प्रतिरूप कांस्य युग के प्रतीकों में सौर या खगोलीय महत्व रखता है।\n3. पुरोहित-राजा की मूर्ति में उसकी दाढ़ी को पूरी तरह मुड़ा हुआ दिखाया गया है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 2", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि पुरोहित-राजा की घनी और सजी हुई दाढ़ी है, केवल ऊपरी होंठ को साफ किया गया है।"
    ),
    (
        "लेखन की दिशा के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मुहरों के बाईं ओर अक्षरों के सिकुड़ने (cramping) से पता चलता है कि वे दाएं से बाएं लिखते थे।\n2. लेखक ने लिखना दाईं तरफ से शुरू किया और बाईं ओर जगह कम रहने से अक्षर छोटे कर दिए, जो दिशा सिद्ध करता है।\n3. बोउस्ट्रोफेडन लेखन शैली प्राचीन ग्रीक अभिलेखों में भी देखने को मिलती है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं और मुहरों पर अक्षर संकुचन, दाएं से बाएं लेखन और बोउस्ट्रोफेडन के ग्रीक समानांतर को दर्शाते हैं।"
    ),
    (
        "चन्हुदड़ो के कारीगरों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. उत्खनन में यहाँ भट्टियों और छिद्रण उपकरणों (drills) से युक्त मनका निर्माताओं की दुकानें मिली हैं।\n2. चन्हुदड़ो के धातु शिल्पियों ने कांसे के खिलौने और तांबे के चाकुओं का निर्माण किया।\n3. कारीगर एक अलग निचली जाति के थे जिन्हें मुख्य नगर से बाहर रखा गया था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि चन्हुदड़ो एक औद्योगिक शिल्प उपनगर था जहाँ कोई जातिगत बहिष्कार का प्रमाण नहीं है।"
    ),
    (
        "हड़प्पा धर्म में पीपल के पेड़ के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मुहरों पर इसे तीन पत्तों वाली टहनियों के रूप में चित्रित किया गया है।\n2. देवों को पेड़ की दो शाखाओं के बीच खड़े होकर पूजा स्वीकार करते हुए दिखाया गया है।\n3. पीपल का पेड़ आज भी भारतीय धर्मों में पूजनीय है, जो सांस्कृतिक निरंतरता को दर्शाता है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो पीपल के चित्रण, शाखाओं में देव और सांस्कृतिक निरंतरता का विवरण देते हैं।"
    ),
    (
        "कूबड़ वाले सांड (Zebu) के चित्रण के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. कूबड़ वाला सांड एक पवित्र पशु और शक्ति या उर्वरता का प्रतीक था।\n2. सांड की मूर्तियों को मुख्य रूप से अंतरराष्ट्रीय व्यापार के लिए हाथीदांत से बनाया जाता था।\n3. बड़ी सेलखड़ी की मुहरों पर इसे एक विशाल कूबड़ और मुड़े हुए सींगों के साथ दर्शाया गया है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 3", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 3 सही हैं। कथन 2 गलत है क्योंकि सांडों को सेलखड़ी मुहरों या मिट्टी (terracotta) से बनाया जाता था, हाथीदांत से नहीं।"
    ),
    (
        "हड़प्पा वासियों द्वारा खेले जाने वाले बोर्ड गेम के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. चौकोर खानों (grids) से युक्त मिट्टी और पत्थर के गेम बोर्ड उत्खनित किए गए हैं।\n2. गेम बोर्ड के साथ फेंकने के लिए शंख और मिट्टी की गोटियाँ मिली हैं।\n3. बोर्ड गेम का उपयोग विशेष रूप से पुरोहितों द्वारा खगोलीय गणनाओं के लिए किया जाता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 2", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि बोर्ड गेम आम लोगों के मनोरंजन के साधन थे, न कि खगोलीय यंत्र।"
    ),
    (
        "लोथल से प्राप्त युगल शवाधान (double burials) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. ये तीन अलग-अलग कब्रों का प्रतिनिधित्व करते हैं, जिनमें से प्रत्येक में एक पुरुष और एक महिला का कंकाल है।\n2. कंकालों को मिट्टी के बर्तनों (भोजन की थालियों) के साथ दफनाया गया था।\n3. कंकालों पर गंभीर हिंसा के निशान मिले हैं, जो जबरन बलि देने को प्रमाणित करते हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["Clean 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि कंकालों पर किसी प्रकार की चोट या बलि के निशान नहीं मिले हैं; उनकी मृत्यु का कारण अज्ञात है।"
    ),
    (
        "धोलावीरा के सूचना-पट्ट (signboard) के अक्षरों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. ये अक्षर लगभग 37 सेमी लंबे हैं, जिन्हें लकड़ी के बोर्ड पर लगाया गया था जो बाद में नष्ट हो गया।\n2. अक्षरों को लकड़ी की पृष्ठभूमि में चमकाने के लिए सफेद क्रिस्टलीय जिप्सम लेप से भरा गया था।\n3. यह अभिलेख आज तक अपठित है, जैसा कि अन्य हड़प्पा अभिलेखों के साथ है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं और धोलावीरा सूचना-पट्ट की ऊंचाई, जिप्सम भराव और अपठित स्थिति को स्पष्ट करते हैं।"
    )
]

# Mock Test Questions (10 Qs)
mock_data_eng = [
    (
        "Consider the following statements regarding the Boustrophedon writing style of the Harappans:\n1. Consecutive lines alternate directions, typically starting from right-to-left, then left-to-right.\n2. This writing style was also used in early ancient Greek inscriptions.\n3. It remains undeciphered, though over 400 signs have been identified.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All three statements are correct and define the boustrophedon direction, Greek parallels, and undeciphered logo-syllabic status of the Harappan script."
    ),
    (
        "With reference to the Pashupati seal from Mohenjo-daro, consider the following statements:\n1. The seated figure is three-faced and wears a horned headdress in a yogic posture.\n2. He is surrounded by four wild animals: tiger, elephant, rhinoceros, and humped zebu bull.\n3. Two deer are depicted beneath his raised throne.\nWhich of the statements given above are correct?",
        ["1 and 3 only", "1, 2 and 3", "1 and 2 only", "2 and 3 only"],
        0,
        "Statements 1 and 3 are correct. Statement 2 is incorrect: the four animals are tiger, elephant, rhinoceros, and buffalo (not humped zebu bull)."
    ),
    (
        "Consider the following statements regarding Harappan funerary practices:\n1. Complete inhumation with the body aligned head pointing north was the standard method.\n2. Lothal is unique for yielding double burials (male and female in a single grave).\n3. Cemetery H at Harappa represents a late cultural phase with cremation urns decorated with star and bird motifs.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All three statements represent verified archaeological facts about Harappan burials, Lothal double graves, and late Cemetery H urns."
    ),
    (
        "With reference to the Dancing Girl bronze statue, consider the following statements:\n1. She is cast using the lost-wax (cire perdue) technique, demonstrating high metallurgy.\n2. She stands in a tribhanga posture, with one hand on her hip and the left arm covered in bangles.\n3. She was discovered in the Citadel mound of Harappa.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "2 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: she was discovered at Mohenjo-daro, not Harappa."
    ),
    (
        "Consider the following statements regarding Harappan cosmetic and personal grooming habits:\n1. Chanhudaro has yielded direct evidence of cinnabar-based lipsticks.\n2. Small pots of terracotta and bronze were used to store eyeliner (collyrium).\n3. Bronze mirrors with decorative handles were common luxury goods.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, describing the lipsticks at Chanhudaro, collyrium pots, and bronze mirrors."
    ),
    (
        "With reference to the terracotta 'Mother Goddess' figurines, consider the following statements:\n1. They feature elaborate fan-shaped headdresses, often showing soot marks from use as lamps.\n2. A famous figurine depicts a plant emerging from a woman's womb, representing fertility.\n3. They are completely absent in Gujarati sites like Lothal and Dholavira.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "1, 2 and 3", "2 and 3 only", "1 and 3 only"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: Mother Goddess figurines are rare in Gujarat compared to Sindh/Punjab, but they are not completely absent."
    ),
    (
        "Consider the following statements regarding the Priest-King sculpture:\n1. It is a bearded bust carved from soft steatite soapstone.\n2. The figure is draped in a shawl decorated with trefoil motifs, once filled with red pigment.\n3. The eyes are inlaid with shell and half-closed in a meditative state.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, detailing the Priest-King bust materials, shawl trefoils, and shell-inlaid eyes."
    ),
    (
        "With reference to the toys and amusements of the Harappans, consider the following statements:\n1. Moving carts with clay wheels and clay whistles shaped like birds were common toys.\n2. Board games and cubical chert dice with dotted numbers indicate precursors to chess and dice games.\n3. Animal fights, particularly cockfighting, are depicted in terracotta and seals.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, outlining the toy engineering, board games, dice, and animal-fighting pastimes."
    ),
    (
        "Consider the following statements regarding the shell and bead industries:\n1. Chanhudaro and Lothal featured dedicated bead manufacturing workshops with micro-drills.\n2. Balakot in Baluchistan was a coastal center specializing in shell bangle cutting.\n3. Steatite, carnelian, and lapis lazuli were the primary raw stones used in bead making.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, outlining the bead shops, shell centers, and minerals used in Harappan jewelry."
    ),
    (
        "With reference to the Dholavira Signboard inscription, consider the following statements:\n1. It features ten large symbols, each about 37 cm high, made of white gypsum paste.\n2. The symbols were mounted on a wooden board that once hung over a city gate.\n3. It has been successfully translated as a royal decree of the Harappan king.",
        ["1 and 2 only", "1, 2 and 3", "2 and 3 only", "1 and 3 only"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: the signboard inscription remains undeciphered, and no kings or decrees are verified."
    )
]

mock_data_hin = [
    (
        "हड़प्पा वासियों की बोउस्ट्रोफेडन (Boustrophedon) लेखन शैली के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. क्रमिक पंक्तियों में लेखन की दिशा बदलती थी, जो आमतौर पर दाएं से बाएं, फिर बाएं से दाएं होती थी।\n2. इस लेखन शैली का उपयोग प्रारंभिक प्राचीन यूनानी (Greek) शिलालेखों में भी किया गया था।\n3. यह लिपि आज तक अपठित है, यद्यपि 400 से अधिक विशिष्ट चिन्हों की पहचान की गई है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं और बोउस्ट्रोफेडन दिशा, यूनानी समानांतर और अपठित लोगो-सिलेबिक स्थिति को परिभाषित करते हैं।"
    ),
    (
        "मोहनजोदड़ो से प्राप्त पशुपति मुहर के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. बैठी हुई आकृति के तीन मुख हैं और वह सींगों वाला मुकुट पहने योगासन मुद्रा में है।\n2. वह चार जंगली जानवरों: बाघ, हाथी, गैंडा और कूबड़ वाले सांड से घिरा हुआ है।\n3. उनके उठे हुए सिंहासन के नीचे दो हिरण चित्रित हैं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 3", "1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3"],
        0,
        "कथन 1 और 3 सही हैं। कथन 2 गलत है: चार जानवर बाघ, हाथी, गैंडा और भैंसा हैं (कूबड़ वाला सांड नहीं)।"
    ),
    (
        "हड़प्पा की शवाधान प्रथाओं के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. शव को उत्तर की ओर सिर करके दफनाना (पूर्ण शवाधान) मुख्य विधि थी।\n2. लोथल युगल कब्रों (पुरुष और महिला एक ही कब्र में) के लिए प्रसिद्ध है।\n3. हड़प्पा में कब्रिस्तान H (Cemetery H) उत्तर हड़प्पा काल का प्रतिनिधित्व करता है जहाँ कलशों पर मोरों और तारों के चित्र हैं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो शव संरेखण, लोथल की युगल कब्रों और कब्रिस्तान H के चित्रित कलशों को स्पष्ट करते हैं।"
    ),
    (
        "कांस्य की नर्तकी (Dancing Girl) की मूर्ति के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इसे लुप्त-मोम (lost-wax) विधि से ढाला गया है, जो उच्च धातुकर्म कौशल को दर्शाता है।\n2. वह त्रिभंग मुद्रा में खड़ी है, जिसमें एक हाथ कूल्हे पर है और बायां हाथ चूड़ियों से ढका है।\n3. इसे हड़प्पा के किले (Citadel) के टीले से खोजा गया था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 2", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि नर्तकी मोहनजोदड़ो से मिली थी, हड़प्पा से नहीं।"
    ),
    (
        "हड़प्पा वासियों के सौंदर्य प्रसाधनों और श्रृंगार आदतों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. चन्हुदड़ो से हिंगुल (cinnabar) आधारित लिपस्टिक के प्रत्यक्ष साक्ष्य मिले हैं।\n2. मिट्टी और कांसे के छोटे पात्रों का उपयोग आँखों के काजल (collyrium) को रखने के लिए किया जाता था।\n3. सुंदर हैंडल वाले कांसे के दर्पण एक आम विलासिता वस्तु थे।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो चन्हुदड़ो की लिपस्टिक, काजल डिब्बियों और कांसे के दर्पणों का विवरण देते हैं।"
    ),
    (
        "मिट्टी की 'मातृदेवी' मूर्तियों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इनमें बड़े पंखे के आकार के मुकुट बने हैं, जिन पर दीये के रूप में प्रयोग से कालिख के निशान हैं।\n2. एक प्रसिद्ध मूर्ति में महिला के गर्भ से पौधा निकलता दिखाया गया है, जो उर्वरता का प्रतीक है।\n3. ये मूर्तियाँ गुजरात के लोथल और धोलावीरा जैसे स्थलों से पूरी तरह अनुपस्थित हैं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "1, 2 और 3", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि गुजरात में मातृदेवी मूर्तियाँ दुर्लभ हैं पर पूरी तरह अनुपस्थित नहीं हैं।"
    ),
    (
        "पुरोहित-राजा (Priest-King) की मूर्ति के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह सेलखड़ी पत्थर से तराशा गया दाढ़ी वाला एक मानव धड़ है।\n2. उसने तिपतिया (trefoil) डिजाइनों से सजा शॉल ओढ़ा है, जिसमें कभी लाल रंग भरा गया था।\n3. आँखें शंख से मढ़ी थीं और ध्यान की मुद्रा में आधी खुली हुई हैं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं और पुरोहित-राजा की मूर्ति के पत्थर, शॉल डिजाइन और आँखों की बनावट का विवरण देते हैं।"
    ),
    (
        "हड़प्पा वासियों के खिलौनों और मनोरंजन के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मिट्टी के पहियों वाली चलती गाड़ियाँ और चिड़िया के आकार की मिट्टी की सीटियाँ आम खिलौने थे।\n2. ग्रिड पैटर्न वाले बोर्ड और घनाकार चर्ट के पासे शतरंज और पासा खेलों के प्राचीन रूप को दर्शाते हैं।\n3. तीतर-मुर्गों की लड़ाई जैसे खेल कला और मुहरों पर चित्रित किए गए हैं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो खिलौनों, पासा-बोर्ड खेलों और मुर्गों की लड़ाई के साक्ष्यों को स्पष्ट करते हैं।"
    ),
    (
        "शंख और मनका उद्योगों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. चन्हुदड़ो और लोथल में सूक्ष्म-ड्रिल से युक्त मनका बनाने के समर्पित कारखाने मिले हैं।\n2. बलूचिस्तान का बालाकोट शंख की चूड़ियाँ काटने में विशेषज्ञता रखने वाला एक तटीय केंद्र था।\n3. सेलखड़ी, अकीक (carnelian) और लाजवर्त (lapis) मनके बनाने में प्रयुक्त प्रमुख पत्थर थे।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं और मनका कारखानों, शंख उद्योगों और प्रयुक्त खनिज पत्थरों का सटीक वर्णन करते हैं।"
    ),
    (
        "धोलावीरा के सूचना-पट्ट (Signboard) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इसमें सफेद जिप्सम से बने दस बड़े प्रतीक शामिल हैं, जिनमें से प्रत्येक की ऊंचाई लगभग 37 सेमी है।\n2. इन अक्षरों को एक लकड़ी के तख्ते पर लगाया गया था जो कभी शहर के द्वार पर लटका था।\n3. इसे हड़प्पा के राजा के एक शाही आदेश के रूप में सफलतापूर्वक अनुवादित किया जा चुका है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "1, 2 और 3", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि यह लिपि अपठित है और किसी राजा या आदेश की पुष्टि नहीं हुई है।"
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

print("Socio-Cultural Base JSON files built successfully!")
