import json
import os

ENG_PATH = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\HarappanIndus-Valley-Civilisation\Religions\content.json"
HIN_PATH = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\HarappanIndus-Valley-Civilisation\Religions\hi\content.json"

ar_opts = [
    "Both Assertion (A) and Reason (R) are true and Reason (R) is the correct explanation of Assertion (A)",
    "Both Assertion (A) and Reason (R) are true but Reason (R) is NOT the correct explanation of Assertion (A)",
    "Assertion (A) is true but Reason (R) is false",
    "Assertion (A) is false but Reason (R) is true",
    "Both Assertion (A) and Reason (R) are false"
]

hin_ar_opts = [
    "कथन (A) और कारण (R) दोनों सही हैं और कारण (R), कथन (A) की सही व्याख्या है।",
    "कथन (A) और कारण (R) दोनों सही हैं लेकिन कारण (R), कथन (A) की सही व्याख्या नहीं है।",
    "कथन (A) सही है लेकिन कारण (R) गलत है।",
    "कथन (A) गलत है लेकिन कारण (R) सही है।",
    "कथन (A) और कारण (R) दोनों गलत हैं।"
]

mcq_opts = [
    "1 only",
    "2 only",
    "Both 1 and 2",
    "Neither 1 nor 2"
]

hin_mcq_opts = [
    "1 केवल",
    "2 केवल",
    "1 और 2 दोनों",
    "न तो 1 न ही 2"
]

# =========================================================================
# SECTION 1: PASHUPATI SEAL, MOTHER GODDESS & MALE/FEMALE DEITIES
# =========================================================================
s1_mastery_eng = []
s1_mastery_hin = []

# MCQ (5)
for q, opts, ans, sol in [
    ("At which of the following Mature Harappan sites was the famous steatite Pashupati Seal excavated?", ["Mohenjo-daro", "Harappa", "Kalibangan", "Lothal"], 0, "The Pashupati Seal was discovered at Mohenjo-daro."),
    ("The soot-stained cup-like panniers on the headdress of Mother Goddess figurines suggest their use as:", ["Oil lamps or incense burners", "Drinking cups for soma juice", "Weight standards for gold", "Storage containers for cosmetic oils"], 0, "Soot staining on headdress panniers indicates they burned oil or incense in domestic rituals."),
    ("How many animals (excluding deer under the seat) surround the central figure on the Pashupati Seal?", ["Four", "Three", "Five", "Two"], 0, "Four animals surround the deity: an elephant, a tiger, a rhinoceros, and a water buffalo."),
    ("The seated figure on the Pashupati Seal is depicted wearing which headgear?", ["A horned crown", "A gold-plated turban", "A feather crown", "No headgear"], 0, "He wears a prominent horned crown, suggesting divine or royal status."),
    ("Unlike Mesopotamia, Harappan civilization is characterized by the complete absence of:", ["Monumental public temples", "Syllabic writing tablets", "Faience beads", "Standard weights"], 0, "No monumental temples have ever been found in the Indus Valley, unlike Mesopotamia.")
]:
    s1_mastery_eng.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("प्रसिद्ध सेलखड़ी की पशुपति मुहर निम्नलिखित में से किस परिपक्व हड़प्पा स्थल से खोजी गई थी?", ["मोहनजोदड़ो", "हड़प्पा", "कालीबंगन", "लोथल"], 0, "पशुपति मुहर मोहनजोदड़ो से प्राप्त हुई थी।"),
    ("मातृदेवी की मूर्तियों के सिर के दोनों तरफ बने प्यालेनुमा आकृतियों में मिले कालिख के निशान क्या दर्शाते हैं?", ["तेल के दीपक या धूपदानी के रूप में उपयोग", "सोमरस पीने के प्याले", "सोने के मानकीकृत बाट", "सौंदर्य प्रसाधनों के डिब्बे"], 0, "प्यालों पर कालिख के निशान दर्शाते हैं कि घरेलू अनुष्ठानों में इनमें दीये जलाए जाते थे।"),
    ("सिंहासन के नीचे बैठे दो हिरणों को छोड़कर, पशुपति मुहर के मुख्य देवता को कितने पशु घेरे हुए हैं?", ["चार", "तीन", "पांच", "दो"], 0, "देवता को चार जानवर घेरे हुए हैं: हाथी, बाघ, गैंडा और जंगली भैंसा।"),
    ("पशुपति मुहर पर आसीन देवता को कौन सा मुकुट पहने हुए दिखाया गया है?", ["एक सींगों वाला मुकुट", "सोने की पगड़ी", "पंखों का मुकुट", "कोई मुकुट नहीं"], 0, "वे सींगों वाला मुकुट पहने हैं, जो देवता होने का संकेत है।"),
    ("मेसोपोटामिया के विपरीत, हड़प्पा सभ्यता की विशेषता किसका पूर्ण अभाव है?", ["सार्वजनिक भव्य मंदिर", "अक्षरों वाली मिट्टी की पट्टियाँ", "फेयॉन्स के मनके", "मानकीकृत बाट"], 0, "सिंधु घाटी में मेसोपोटामिया के विपरीत किसी भी मंदिर के अवशेष नहीं मिले हैं।")
]:
    s1_mastery_hin.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# Multi-Correct MCQ (5)
for q, opts, ans, sol in [
    ("Which of the following animals surround the deity in the Pashupati Seal? (Select all that apply)", ["Elephant", "Tiger", "Rhinoceros", "Lion"], [0, 1, 2], "Elephant, tiger, rhino, and buffalo surround him. Lions are absent from IVC art."),
    ("Select the characteristic features of Harappan Mother Goddess figurines: (Select all that apply)", ["Made of hand-modeled terracotta", "Feature elaborate fan-shaped headdresses", "Contain soot-stained cup-like panniers", "Carved from polished white marble"], [0, 1, 2], "They are hand-modeled terracotta with fan headdresses and soot-stained panniers. None are marble."),
    ("Identify the scholarly arguments critiquing Marshall's 'Proto-Shiva' interpretation: (Select all that apply)", ["The three faces are bovine features representing cattle deities", "The ithyphallic nature is actually a waist belt or lower garment", "Horned headdresses were common symbols of power across ancient Asia", "The inscription explicitly names the deity as Rudra"], [0, 1, 2], "Critics note bovine faces, a belt (not phallus), and general horned power symbols. Inscription is undeciphered."),
    ("Which of the following sites have yielded terracotta Mother Goddess figurines? (Select all that apply)", ["Mohenjo-daro", "Harappa", "Kalibangan", "Lothal"], [0, 1], "Mother Goddess figurines are abundant in Mohenjo-daro and Harappa, but virtually absent in Rajasthan and Gujarat."),
    ("Select correct statements regarding the lack of temples in the Indus Valley: (Select all that apply)", ["Religious rituals were decentralized and household-based", "Society lacked a monumental, centralized temple-state system", "Public worship focused on open-air platforms and water bodies", "The Harappans were strict atheists who banned religious architecture"], [0, 1, 2], "IVC religion was domestic, lacked central temples, and focused on platforms/water. Atheism did not exist.")
]:
    s1_mastery_eng.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("निम्नलिखित में से कौन से पशु पशुपति मुहर पर देवता को घेरे हुए हैं? (सभी लागू विकल्प चुनें)", ["हाथी", "बाघ", "गैंडा", "शेर"], [0, 1, 2], "हाथी, बाघ, गैंडा और भैंसा देवता के पास बने हैं। शेर सिंधु मुहरों पर नहीं मिलता।"),
    ("हड़प्पा की मातृदेवी की मूर्तियों की विशिष्ट विशेषताओं का चयन करें: (सभी लागू विकल्प चुनें)", ["हाथ से गढ़ी मिट्टी की आकृतियाँ", "सिर पर पंख जैसा मुकुट (fan-shaped headdress)", "प्यालों में कालिख के निशान", "पॉलिश किए गए सफेद संगमरमर से निर्मित"], [0, 1, 2], "ये मिट्टी की हाथ से बनी मूर्तियां हैं जिन पर पंखा मुकुट और कालिख वाले प्याले हैं। संगमरमर की नहीं हैं।"),
    ("मार्शल की 'आदि-शिव' व्याख्या की आलोचना करने वाले विद्वानों के तर्कों की पहचान करें: (सभी लागू विकल्प चुनें)", ["तीन चेहरे बैल की विशेषताओं को दर्शाते हैं जो पशु रक्षक देवता हैं", "इथीफालिक (ithyphallic) रूप वास्तव में कमर का पट्टा या वस्त्र है", "सींग वाला मुकुट प्राचीन एशिया में शक्ति का सामान्य प्रतीक था", "शिलालेख में स्पष्ट रूप से देवता का नाम रुद्र लिखा है"], [0, 1, 2], "आलोचक इसे बैल का रूप, कमरबंद और सींगों को शक्ति का सामान्य प्रतीक मानते हैं। लेख अपठित है।"),
    ("निम्नलिखित में से किन स्थलों से मातृदेवी की मिट्टी की मूर्तियाँ मिली हैं? (सभी लागू विकल्प चुनें)", ["मोहनजोदड़ो", "हड़प्पा", "कालीबंगन", "लोथल"], [0, 1], "मातृदेवी की मूर्तियाँ मोहनजोदड़ो और हड़प्पा में प्रचुर मात्रा में मिली हैं, लेकिन कालीबंगन और लोथल में नहीं मिलीं।"),
    ("सिंधु घाटी में मंदिरों के अभाव के संदर्भ में सही कथनों का चयन करें: (सभी लागू विकल्प चुनें)", ["धार्मिक अनुष्ठान विकेंद्रीकृत और घरेलू थे", "समाज में मेसोपोटामिया जैसी केंद्रीय मंदिर-राज्य प्रणाली का अभाव था", "सार्वजनिक पूजा खुले चबूतरे और जलाशयों पर केंद्रित थी", "हड़प्पा वासी नास्तिक थे जिन्होंने धार्मिक वास्तुकला पर प्रतिबंध लगा दिया था"], [0, 1, 2], "हड़प्पा धर्म घरेलू था, यहाँ मंदिरों का अभाव था और अनुष्ठान चबूतरे/जलाशयों पर होते थे।")
]:
    s1_mastery_hin.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# True/False (8)
for q, ans, sol in [
    ("The Pashupati Seal was discovered at the coastal trading port of Lothal.", False, "It was excavated at Mohenjo-daro, not Lothal."),
    ("Terracotta Mother Goddess figurines are extremely rare in Gujarat and Rajasthan sites.", True, "True. They are common in Sindh/Punjab but virtually absent in Lothal and Kalibangan."),
    ("The headdress cup-like features of Mother Goddess figurines were likely used to burn oil or incense.", True, "True. Soot stains in these cup-like structures indicate they functioned as lamps/incense burners."),
    ("Lions are prominently depicted under the seat of the deity in the Pashupati Seal.", False, "False. Two deer (or ibexes) are depicted under the seat, not lions."),
    ("Harappan religious practices were highly institutionalized and centered around grand stone temples.", False, "False. No temples have been discovered; practices were domestic and decentralized."),
    ("The seated figure in the Pashupati Seal is depicted wearing a plain round helmet.", False, "False. He wears a prominent horned crown."),
    ("Sir John Marshall interpreted the seated deity on the seal as a Proto-Shiva.", True, "True. Marshall linked the yogic pose, horned crown, and surrounding beasts to historical Shiva."),
    ("Horned headgears in Harappan art were restricted to male terracotta figures.", False, "False. They are also found on deities inside tree branches, which can be male or female representations.")
]:
    s1_mastery_eng.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("पशुपति मुहर लोथल के तटीय व्यापारिक बंदरगाह से खोजी गई थी।", False, "यह मोहनजोदड़ो से खोजी गई थी, लोथल से नहीं।"),
    ("मातृदेवी की मिट्टी की मूर्तियाँ गुजरात और राजस्थान के हड़प्पा स्थलों में अत्यंत दुर्लभ हैं।", True, "सत्य। ये सिंध और पंजाब में प्रचुर हैं लेकिन लोथल और कालीबंगन में नगण्य हैं।"),
    ("मातृदेवी की मूर्तियों के सिर पर बने प्यालों का उपयोग तेल या धूप जलाने के लिए किया जाता था।", True, "सत्य। प्यालों में मिली कालिख के निशान इनके घरेलू अनुष्ठानों में उपयोग को प्रमाणित करते हैं।"),
    ("पशुपति मुहर पर सिंहासन के नीचे दो शेर बने दिखाई देते हैं।", False, "असत्य। सिंहासन के नीचे दो हिरण (या जंगली बकरे) बने हैं, शेर नहीं।"),
    ("हड़प्पा की धार्मिक प्रथाएं अत्यधिक संस्थागत थीं और विशाल पत्थर के मंदिरों पर केंद्रित थीं।", False, "असत्य। हड़प्पा में किसी भी मंदिर का साक्ष्य नहीं मिला है, धार्मिक क्रियाएं घरेलू थीं।"),
    ("पशुपति मुहर पर आसीन देवता एक साधारण गोल हेलमेट पहने हुए हैं।", False, "असत्य। वे एक सींगों वाला भारी मुकुट पहने हैं।"),
    ("सर जॉन मार्शल ने मुहर पर आसीन देवता को 'आदि-शिव' (Proto-Shiva) के रूप में व्याख्यायित किया था।", True, "सत्य। मार्शल ने योगासन, सींगों और पशुओं की उपस्थिति के कारण इसे शिव का पूर्व रूप माना।"),
    ("हड़प्पा कला में सींगों वाले मुकुट केवल पुरुष मृण्मूर्तियों तक ही सीमित थे।", False, "असत्य। सींग वाले मुकुट वृक्ष देवताओं पर भी मिलते हैं जो पुरुष और महिला दोनों रूपों में हो सकते थे।")
]:
    s1_mastery_hin.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

# Fill Blank (8)
for q, ans, sol in [
    ("The Pashupati Seal was made from a soft soapstone mineral known as ___________.", "steatite", "Steatite was the standard material for carving Harappan seals."),
    ("Mother Goddess figurines have soot-stained cup-like features called ___________.", "panniers", "The cup-like decorations on either side of the head are called panniers."),
    ("The four animals surrounding Pashupati are the elephant, tiger, rhino, and ___________.", "buffalo", "The water buffalo is the fourth large animal surrounding the deity."),
    ("Sir John Marshall coined the term ___________ to describe the seated deity.", "Proto-Shiva", "Marshall identified the deity as Proto-Shiva."),
    ("Unlike Egypt, the Indus Valley is notable for the complete absence of monumental ___________.", "temples", "No monumental temples or shrines exist in Harappan cities."),
    ("The seated deity on the Pashupati Seal wears a three-pointed ___________ crown.", "horned", "A horned headdress or crown is worn by the seated figure."),
    ("Most Mother Goddess figurines were modeled by ___________ rather than cast in molds.", "hand", "Terracotta figurines were hand-modeled using pinching techniques."),
    ("Underneath the throne of the Pashupati deity, there are two ___________ depicted.", "deer", "Two deer (or ibexes) are carved below the seat.")
]:
    s1_mastery_eng.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("पशुपति मुहर सेलखड़ी नामक नरम साबुन-पत्थर से बनी थी जिसे ___________ भी कहते हैं।", "steatite", "सेलखड़ी (steatite) का उपयोग मुहरें बनाने में मुख्य रूप से होता था।"),
    ("मातृदेवी की मूर्तियों के सिर पर बने कालिख वाले प्यालेनुमा आकारों को ___________ कहा जाता है।", "पैनियर्स", "सिर के दोनों तरफ लगे कटोरे जैसे हिस्सों को पैनियर्स (panniers) कहा जाता है।"),
    ("पशुपति के चारों ओर बने जानवर हाथी, बाघ, गैंडा और जंगली ___________ हैं।", "भैंसा", "चौथा बड़ा जंगली जानवर जल भैंसा (water buffalo) है।"),
    ("सर जॉन मार्शल ने मुहर पर आसीन देवता को ___________ के रूप में नामित किया था।", "आदि-शिव", "मार्शल ने योगासन मुद्रा और पशुओं के कारण इसे आदि-शिव (Proto-Shiva) कहा था।"),
    ("मिस्र के विपरीत, सिंधु सभ्यता सार्वजनिक धार्मिक विधाओं के लिए विशाल ___________ के पूर्ण अभाव के लिए जानी जाती है।", "मंदिरों", "हड़प्पा सभ्यता में सार्वजनिक मंदिरों का अभाव था।"),
    ("पशुपति मुहर पर आसीन देवता ने एक तीन नोक वाला ___________ मुकुट पहना है।", "सींग वाला", "देवता ने सींग वाला (horned) मुकुट पहना है।"),
    ("अधिकांश मातृदेवी की मूर्तियाँ सांचे में ढालने के बजाय ___________ से गढ़ी गई थीं।", "हाथ", "मिट्टी की ये मूर्तियाँ हाथ से (hand-modeled) बनाई जाती थीं।"),
    ("पशुपति देवता के सिंहासन के ठीक नीचे दो ___________ चित्रित किए गए हैं।", "हिरण", "आसन के नीचे दो हिरण (या जंगली बकरे) उकेरे गए हैं।")
]:
    s1_mastery_hin.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

# Match the Following (3)
s1_mastery_eng.extend([
    {
        "type": "Match the Following",
        "q": "Match the figures with their key archeological descriptions:",
        "items": [{"left": "I. Pashupati", "key": "A"}, {"left": "II. Mother Goddess", "key": "B"}, {"left": "III. Priest-King", "key": "C"}],
        "options": [{"val": "A", "text": "A. Horned headdress, yogic pose, surrounded by wild beasts"}, {"val": "B", "text": "B. Soot-stained headdress panniers, terracotta ornamentations"}, {"val": "C", "text": "C. Steatite bust, trefoil shawl pattern, meditative eyes"}],
        "sol": "Pashupati has horned crown and beasts; Mother Goddess has soot-stained headdress; Priest-King has trefoil shawl."
    },
    {
        "type": "Match the Following",
        "q": "Match the interpretations with the respective scholars:",
        "items": [{"left": "I. John Marshall", "key": "A"}, {"left": "II. Doris Srinivasan", "key": "B"}, {"left": "III. George Dales", "key": "C"}],
        "options": [{"val": "A", "text": "A. Horned deity represents Proto-Shiva (Mahadeva)"}, {"val": "B", "text": "B. Seated figure is a composite bovine deity associated with cattle"}, {"val": "C", "text": "C. Stone ring stones functioned as column bases, not yoni icons"}],
        "sol": "Marshall interpreted Proto-Shiva, Srinivasan proposed a bovine deity, and Dales interpreted ring stones as column bases."
    },
    {
        "type": "Match the Following",
        "q": "Match the deities/icons with their typical materials and styles:",
        "items": [{"left": "I. Seated Proto-Shiva", "key": "A"}, {"left": "II. Female fertility icons", "key": "B"}, {"left": "III. Lingas / phallic shapes", "key": "C"}],
        "options": [{"val": "A", "text": "A. Intaglio engraving on square steatite seals"}, {"val": "B", "text": "B. Hand-modeled baked terracotta figurines"}, {"val": "C", "text": "C. Polished cylindrical stone and clay pieces"}],
        "sol": "Proto-Shiva is intaglio on steatite, fertility icons are hand-modeled terracotta, and lingas are polished cylinders."
    }
])

s1_mastery_hin.extend([
    {
        "type": "Match the Following",
        "q": "धार्मिक मूर्तियों को उनकी पुरातात्विक विशेषताओं से सुमेलित करें:",
        "items": [{"left": "I. पशुपति", "key": "A"}, {"left": "II. मातृदेवी", "key": "B"}, {"left": "III. पुरोहित-राजा", "key": "C"}],
        "options": [{"val": "A", "text": "A. सींग वाला मुकुट, योग मुद्रा, जंगली जानवरों से घिरे"}, {"val": "B", "text": "B. कालिख लगे प्यालेनुमा पैनियर्स, मिट्टी के आभूषण"}, {"val": "C", "text": "C. सेलखड़ी धड़, तिपतिया शॉल पैटर्न, ध्यानमग्न आँखें"}],
        "sol": "पशुपति सींग वाले मुकुट व पशुओं के साथ हैं; मातृदेवी कालिख वाले मुकुट के साथ; पुरोहित-राजा तिपतिया शॉल के साथ हैं।"
    },
    {
        "type": "Match the Following",
        "q": "धार्मिक साक्ष्यों की व्याख्याओं को संबंधित विद्वानों से सुमेलित करें:",
        "items": [{"left": "I. जॉन मार्शल", "key": "A"}, {"left": "II. डोरिस श्रीनिवासन", "key": "B"}, {"left": "III. जॉर्ज डेल्स", "key": "C"}],
        "options": [{"val": "A", "text": "A. सींग वाला देवता आदि-शिव (महादेव) को दर्शाता है"}, {"val": "B", "text": "B. आसीन देवता एक मिश्रित पशु-बैल है जो पशुओं का रक्षक है"}, {"val": "C", "text": "C. पत्थर के छल्ले खंभों के आधार थे, योनि के प्रतीक नहीं"}],
        "sol": "मार्शल ने आदि-शिव कहा, श्रीनिवासन ने पशु-बैल देवता माना, और डेल्स ने छल्लों को खंभे का आधार बताया।"
    },
    {
        "type": "Match the Following",
        "q": "देवताओं/प्रतीकों को उनकी विनिर्माण शैलियों से सुमेलित करें:",
        "items": [{"left": "I. आसीन आदि-शिव", "key": "A"}, {"left": "II. नारी उर्वरता प्रतीक", "key": "B"}, {"left": "III. लिंग / लिंगाकार वस्तुएं", "key": "C"}],
        "options": [{"val": "A", "text": "A. चौकोर सेलखड़ी मुहरों पर नक्काशी (intaglio)"}, {"val": "B", "text": "B. हाथ से बनी पकी मिट्टी की मूर्तियाँ (terracotta)"}, {"val": "C", "text": "C. पॉलिश किए गए बेलनाकार पत्थर और मिट्टी के टुकड़े"}],
        "sol": "आदि-शिव मुहरों पर नक्काशी है, नारी प्रतीक हाथ से बनी टेराकोटा हैं, और लिंग पॉलिश बेलनाकार पत्थर हैं।"
    }
])

# One-Liner (8)
for q, sol in [
    ("Where was the Pashupati Seal discovered?", "Mohenjo-daro."),
    ("What mineral was used to carve the Pashupati Seal?", "Steatite (soapstone)."),
    ("Why did John Marshall identify the seated figure as Shiva?", "Due to the yogic posture, three faces, horned headgear, and surrounding wild animals."),
    ("What are the four large animals carved on the Pashupati Seal?", "Elephant, tiger, rhinoceros, and water buffalo."),
    ("What indicates that Mother Goddess figurines were used as lamps?", "The presence of soot staining in their headdress cup-like panniers."),
    ("Name the two sites where Mother Goddess figurines are found in abundance.", "Mohenjo-daro and Harappa."),
    ("True or False: The Harappans built monumental public temples.", "False (there is a complete absence of temples)."),
    ("How many deer are carved beneath the seat in the Pashupati Seal?", "Two deer (or ibexes).")
]:
    s1_mastery_eng.append({"type": "One-Liner", "q": q, "sol": sol})

for q, sol in [
    ("पशुपति मुहर किस स्थल से प्राप्त हुई थी?", "मोहनजोदड़ो।"),
    ("पशुपति मुहर को तराशने के लिए किस खनिज का उपयोग किया गया था?", "सेलखड़ी (steatite या soapstone)।"),
    ("जॉन मार्शल ने आसीन आकृति की पहचान शिव के रूप में क्यों की?", "योग मुद्रा, तीन चेहरे, सींग वाला मुकुट और चारों ओर जंगली जानवरों की उपस्थिति के कारण।"),
    ("पशुपति मुहर पर उत्कीर्ण चार बड़े जानवर कौन से हैं?", "हाथी, बाघ, गैंडा और जंगली भैंसा।"),
    ("मातृदेवी की मूर्तियों का उपयोग दीपक के रूप में होने का क्या संकेत मिलता है?", "उनके सिर के मुकुट के प्यालेनुमा पैनियर्स में मिली कालिख के निशान।"),
    ("उन दो प्रमुख स्थलों के नाम बताएं जहाँ मातृदेवी की मूर्तियाँ बहुतायत में मिली हैं।", "मोहनजोदड़ो और हड़प्पा।"),
    ("सत्य या असत्य: हड़प्पा वासियों ने सार्वजनिक भव्य मंदिरों का निर्माण किया था।", "असत्य (यहाँ मंदिरों का पूर्ण अभाव है)।"),
    ("पशुपति मुहर में आसन के नीचे कितने हिरण उत्कीर्ण हैं?", "दो हिरण (या जंगली बकरे)।")
]:
    s1_mastery_hin.append({"type": "One-Liner", "q": q, "sol": sol})

# Assertion-Reason (8)
for q, ans, sol in [
    ("Assertion (A): The seated figure on the Pashupati Seal is interpreted as Proto-Shiva.\nReason (R): He sits in a yogic pose, wears a horned crown, and is surrounded by animals, resembling Shiva's historical aspects.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Mother Goddess figurines were used in public temple rituals.\nReason (R): Huge central temples have been excavated at Harappa and Mohenjo-daro.", 4, "Both A and R are false: no temples have been found, and figurines were used in domestic shrines."),
    ("Assertion (A): The cup-like panniers of Mother Goddess headdresses contain soot stains.\nReason (R): These cups were used to burn oil or incense in domestic households.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): The deity on the Pashupati Seal is flanked by a lion and a horse.\nReason (R): Lions and horses were the most common animals depicted on Harappan seals.", 4, "Both A and R are false. The seal has an elephant, tiger, rhino, and buffalo. Lions are absent in IVC art."),
    ("Assertion (A): Doris Srinivasan rejected Marshall's Proto-Shiva interpretation.\nReason (R): She argued the three faces could be bovine features and the horns represent general fertility, not Shiva.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): The Harappans lacked institutionalized state temples like the Mesopotamians.\nReason (R): No monumental temples or structures definitely identified as shrines have been found in the Indus Valley.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Mother Goddess figurines were mass-produced in two-part bronze molds.\nReason (R): Metal mold casting was the primary technique for producing clay figurines in the Bronze Age.", 4, "Both A and R are false. Terracotta figurines were hand-modeled."),
    ("Assertion (A): The Pashupati Seal depicts two deer beneath the seat.\nReason (R): Deer are associated with Shiva as Pashupati (Lord of Animals) in later Indian iconography.", 0, "Both A and R are true and R is the correct explanation of A.")
]:
    s1_mastery_eng.append({"type": "Assertion-Reason", "q": q, "opts": ar_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("कथन (A): पशुपति मुहर पर आसीन देवता को आदि-शिव माना गया है।\nकारण (R): वे योगासन में बैठे हैं, सींगों वाला मुकुट पहने हैं और जानवरों से घिरे हैं, जो शिव के ऐतिहासिक लक्षणों से मेल खाते हैं।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): मातृदेवी की मृण्मूर्तियों का उपयोग सार्वजनिक मंदिरों के अनुष्ठानों में होता था।\nकारण (R): हड़प्पा और मोहनजोदड़ो से विशाल केंद्रीय मंदिरों के साक्ष्य मिले हैं।", 4, "A और R दोनों असत्य हैं: कोई मंदिर नहीं मिले, मूर्तियाँ घरेलू उपयोग की थीं।"),
    ("कथन (A): मातृदेवी के मुकुट के प्याले जैसे पैनियर्स में कालिख के निशान मिले हैं।\nकारण (R): इन प्यालों का उपयोग घरेलू स्तर पर तेल या धूप जलाने के लिए किया जाता था।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): पशुपति मुहर पर देवता के दोनों ओर एक शेर और एक घोड़ा बना है।\nकारण (R): शेर और घोड़े हड़प्पा सभ्यता की मुहरों पर सबसे आम जानवर थे।", 4, "A और R दोनों असत्य हैं। मुहर पर हाथी, बाघ, गैंडा और भैंसा हैं। शेर कला में अनुपस्थित है।"),
    ("कथन (A): डोरिस श्रीनिवासन ने मार्शल की आदि-शिव व्याख्या को अस्वीकार कर दिया।\nकारण (R): उन्होंने तर्क दिया कि तीन चेहरे वास्तव में बैल की मुखाकृति हो सकते हैं और सींग उर्वरता के प्रतीक हैं, शिव के नहीं।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): हड़प्पा वासियों के पास मेसोपोटामिया की तरह राज्य-नियंत्रित मंदिर नहीं थे।\nकारण (R): सिंधु घाटी में किसी भी मंदिर या पूजा स्थल के रूप में निश्चित पहचानी गई इमारत के अवशेष नहीं मिले हैं।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): मातृदेवी की मूर्तियों का बड़े पैमाने पर उत्पादन दो-भाग वाले कांसे के सांचों में होता था।\nकारण (R): कांस्य युग में मिट्टी की मूर्तियाँ बनाने के लिए धातु सांचा ढलाई प्राथमिक तकनीक थी।", 4, "A और R दोनों असत्य हैं। ये मूर्तियाँ हाथ से बनाई जाती थीं।"),
    ("कथन (A): पशुपति मुहर में आसन के नीचे दो हिरण उत्कीर्ण हैं।\nकारण (R): बाद की भारतीय कला में शिव को पशुपति (पशुओं का स्वामी) के रूप में हिरणों से संबद्ध दिखाया गया है।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।")
]:
    s1_mastery_hin.append({"type": "Assertion-Reason", "q": q, "opts": hin_ar_opts, "ans": ans, "sol": sol})

# Statement-Based (5)
for q, ans, sol in [
    ("Consider the following statements regarding the Pashupati Seal:\n1. It depicts a horned, three-faced deity seated in a yogic pose.\n2. The four animals surrounding the seat are the elephant, tiger, rhino, and lion.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect because the animals are elephant, tiger, rhino, and buffalo (not lion)."),
    ("Consider the following statements regarding Mother Goddess figurines:\n1. They are hand-modeled terracotta figures adorned with heavy jewelry.\n2. The headdresses contain hollow cup-like panniers that often show soot stains.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct, describing Mother Goddess figurines and soot-stained headdress panniers."),
    ("Consider the following statements regarding Harappan religious architecture:\n1. Massive brick temples with central shrines were built in the Citadels of all major cities.\n2. Harappan religious rituals appear to have been decentralized and domestic in nature.\nWhich of the statements given above is/are correct?", 1, "Statement 2 is correct. Statement 1 is incorrect: there is a complete absence of temples in Harappan archaeology."),
    ("Consider the following statements regarding Marshall's interpretations:\n1. He identified the horned figure as a Proto-Shiva.\n2. He interpreted polished stone ring stones as yoni icons representing female fertility.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct, detailing Marshall's Proto-Shiva and yoni interpretations."),
    ("Consider the following statements regarding male deities in IVC:\n1. Terracotta figurines of bearded men are highly abundant at Dholavira and Lothal.\n2. Horned male figures are carved on several seals, indicating a pantheon of male gods.\nWhich of the statements given above is/are correct?", 1, "Statement 2 is correct. Statement 1 is incorrect: male terracotta figurines are relatively rare compared to females and are not abundant at Lothal/Dholavira.")
]:
    s1_mastery_eng.append({"type": "Statement-Based", "q": q, "opts": mcq_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("पशुपति मुहर के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह योग मुद्रा में बैठे एक सींग वाले, तीन चेहरे वाले देवता को दर्शाती है।\n2. आसन को घेरने वाले चार पशु हाथी, बाघ, गैंडा और शेर हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि पशु हाथी, बाघ, गैंडा और भैंसा (शेर नहीं) हैं।"),
    ("मातृदेवी की मूर्तियों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. ये भारी आभूषणों से सजी, हाथ से बनी मिट्टी की मूर्तियां हैं।\n2. इनके मुकुट में बने प्यालेनुमा पैनियर्स में अक्सर कालिख के निशान मिले हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 2, "दोनों कथन सही हैं, जो मातृदेवी की मूर्तियों और कालिख लगे पैनियर्स का विवरण देते हैं।"),
    ("हड़प्पा की धार्मिक वास्तुकला के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. सभी प्रमुख शहरों के दुर्गों में केंद्रीय गर्भगृह वाले विशाल ईंटों के मंदिर बनाए गए थे।\n2. हड़प्पा के धार्मिक अनुष्ठान मुख्यतः विकेंद्रीकृत और घरेलू प्रकृति के प्रतीत होते हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 1, "कथन 2 सही है। कथन 1 गलत है क्योंकि हड़प्पा में मंदिरों का पूर्ण अभाव था।"),
    ("मार्शल की व्याख्याओं के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. उन्होंने सींग वाले देवता की पहचान आदि-शिव के रूप में की थी।\n2. उन्होंने पॉलिश किए गए पत्थर के छल्लों को योनि प्रतीकों के रूप में व्याख्यायित किया था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 2, "दोनों कथन सही हैं, जो मार्शल की आदि-शिव और योनि व्याख्याओं को स्पष्ट करते हैं।"),
    ("सिंधु सभ्यता में पुरुष देवताओं के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. दाढ़ी वाले पुरुषों की मिट्टी की मूर्तियाँ लोथल और धोलावीरा में भारी संख्या में मिली हैं।\n2. कई मुहरों पर सींग वाले पुरुष आकृतियों को उकेरा गया है, जो पुरुष देवताओं को दर्शाते हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 1, "कथन 2 सही है। कथन 1 गलत है क्योंकि पुरुषों की मिट्टी की मूर्तियां महिलाओं की तुलना में बहुत दुर्लभ हैं।")
]:
    s1_mastery_hin.append({"type": "Statement-Based", "q": q, "opts": hin_mcq_opts, "ans": ans, "sol": sol})

# Why (3)
for q, sol in [
    ("Why did Sir John Marshall identify the seated figure on the Pashupati Seal as a Proto-Shiva?", "Because of the figure's three faces, horned headdress, yogic posture, ithyphallic representation, and surrounding wild animals, which align with historical attributes of Shiva as Mahadeva, Pashupati, and Yogiraja."),
    ("Why is the absence of temples in the Indus Valley Civilisation significant for comparative history?", "It shows that unlike contemporary civilizations in Mesopotamia and Egypt, which had highly centralized, temple-state systems dominated by powerful priesthoods, the Harappan religion was decentralized, domestic, and civic."),
    ("Why are terracotta Mother Goddess figurines considered representations of a domestic fertility cult?", "Because they are found within residential houses rather than public structures, and feature soot-stained headdress cup-like panniers suggesting they burned oil or incense during private household prayers for fertility.")
]:
    s1_mastery_eng.append({"type": "Why", "q": q, "sol": sol})

for q, sol in [
    ("सर जॉन मार्शल ने पशुपति मुहर पर आसीन देवता को 'आदि-शिव' क्यों माना?", "देवता के तीन चेहरों, सींगों वाले मुकुट, योगासन मुद्रा, इथीफालिक रूप और जंगली जानवरों की उपस्थिति के कारण, जो महादेव, पशुपति और योगीराज के रूप में ऐतिहासिक शिव के लक्षणों से मेल खाते हैं।"),
    ("सिंधु घाटी सभ्यता में मंदिरों का न होना तुलनात्मक इतिहास के लिए क्यों महत्वपूर्ण है?", "यह दर्शाता है कि मेसोपोटामिया और मिस्र के विपरीत (जहाँ पुरोहितों द्वारा नियंत्रित मंदिर-राज्य होते थे), हड़प्पा वासियों के धार्मिक विश्वास विकेंद्रीकृत, घरेलू और नागरिक प्रकृति के थे, जहाँ कोई विशाल मंदिर-तंत्र नहीं था।"),
    ("मिट्टी की मातृदेवी की मूर्तियों को घरेलू उर्वरता पंथ का प्रतीक क्यों माना जाता है?", "क्योंकि ये मूर्तियाँ सार्वजनिक इमारतों के बजाय साधारण आवासीय घरों से मिली हैं, और इनके सिर के प्यालों में कालिख के निशान मिले हैं, जो घरेलू स्तर पर सुख-समृद्धि के लिए दीप जलाने को दर्शाते हैं।")
]:
    s1_mastery_hin.append({"type": "Why", "q": q, "sol": sol})

# How (3)
for q, sol in [
    ("How did Harappan artisans manufacture terracotta Mother Goddess figurines?", "They modeled the main body by hand, pinched clay to form facial details like nose and eyes, added clay strips/pellets to represent heavy necklaces and fan-shaped headdresses, and fired them in a kiln."),
    ("How did Sir John Marshall interpret polished cylindrical stones and large stone rings as religious icons?", "He compared the cylindrical stones to the historical Hindu phallic 'lingas' representing Shiva, and the large stone rings to the 'yoni' circles representing female fertility, suggesting early forms of Shaivism."),
    ("How do modern scholars critique Marshall's identification of the Pashupati figure as Shiva?", "They point out that the 'three faces' are actually bovine details representing an animal guardian, the 'horns' represent agricultural fertility symbols, the 'phallus' is a waist-belt buckle, and the Indus script remains undeciphered.")
]:
    s1_mastery_eng.append({"type": "How", "q": q, "sol": sol})

for q, sol in [
    ("हड़प्पा के शिल्पकारों ने मिट्टी की मातृदेवी की मूर्तियाँ कैसे बनाई थीं?", "वे हाथ से मूल शरीर का ढांचा बनाते थे, नाक-मुंह बनाने के लिए गीली मिट्टी को उंगलियों से दबाते (pinch) थे, हार और पंखा मुकुट दर्शाने के लिए मिट्टी की पट्टियाँ चिपकाते थे, और फिर भट्टी में पकाते थे।"),
    ("सर जॉन मार्शल ने पॉलिश किए गए बेलनाकार पत्थरों और बड़े पत्थर के छल्लों को धार्मिक प्रतीकों के रूप में कैसे समझाया?", "उन्होंने बेलनाकार पत्थरों की तुलना ऐतिहासिक हिंदू 'लिंग' से की जो शिव का प्रतीक है, और बड़े छल्लों की तुलना 'योनि' से की जो स्त्री उर्वरता का प्रतीक है, जिससे उन्होंने शिव-शक्ति पूजा के आदि रूपों का अनुमान लगाया।"),
    ("आधुनिक विद्वान पशुपति आकृति की मार्शल द्वारा की गई शिव के रूप में पहचान की आलोचना कैसे करते हैं?", "वे बताते हैं कि 'तीन मुख' वास्तव में पशु देवता के चेहरे हैं, 'सींग' कृषि उर्वरता के आम प्रतीक हैं, इथीफालिक रूप वास्तव में बेल्ट का बकल है, और लिपि अपठित होने के कारण इसकी पुष्टि असंभव है।")
]:
    s1_mastery_hin.append({"type": "How", "q": q, "sol": sol})

# Case Study (3)
for q, sol in [
    ("Case Study: Analyze the animal composition on the Pashupati Seal (elephant, tiger, rhino, buffalo, deer). What does this tell us about the Harappan ecological setting?", "It proves that the Harappan core region was once humid and forested, supporting marshy jungle fauna (rhinos and tigers) that have since disappeared due to deforestation and climate change."),
    ("Case Study: Excavations at Kalibangan and Lothal yielded no terracotta Mother Goddess figurines, whereas Mohenjo-daro yielded hundreds. What does this case study demonstrate?", "It demonstrates significant regional variation in religious beliefs across the Indus civilization, showing that the Mother Goddess cult was concentrated in the Indus valley and absent in Rajasthan/Gujarat."),
    ("Case Study: Compare the absence of central state temples in the Indus Valley with the massive ziggurats of Sumer. What does this reveal about Harappan social control?", "It indicates that Harappan social cohesion was maintained through civic organization, standardized municipal laws, and trade guilds, rather than through a centralizing religious temple hierarchy.")
]:
    s1_mastery_eng.append({"type": "Case Study", "q": q, "sol": sol})

for q, sol in [
    ("केस स्टडी: पशुपति मुहर पर उत्कीर्ण जानवरों (हाथी, बाघ, गैंडा, भैंसा) का विश्लेषण करें। यह हड़प्पा के पारिस्थितिक परिवेश के बारे में क्या बताता है?", "यह प्रमाणित करता है कि हड़प्पा का मुख्य क्षेत्र कभी आर्द्र और घने जंगलों वाला था, जहाँ दलदली जंगलों के जीव (गैंडे और बाघ) रहते थे, जो बाद में जलवायु परिवर्तन और वनों की कटाई के कारण लुप्त हो गए।"),
    ("केस स्टडी: कालीबंगन और लोथल से कोई मातृदेवी की मूर्ति नहीं मिली, जबकि मोहनजोदड़ो से सैकड़ों मिलीं। यह केस स्टडी क्या प्रदर्शित करती है?", "यह सिंधु सभ्यता में धार्मिक विश्वासों की क्षेत्रीय भिन्नता को दर्शाती है, जिससे स्पष्ट होता है कि मातृदेवी का पंथ मुख्य रूप से सिंधु घाटी में ही केंद्रित था और राजस्थान/गुजरात में अनुपस्थित था।"),
    ("केस स्टडी: सिंधु घाटी में केंद्रीय मंदिरों के अभाव की तुलना सुमेर के विशाल जिग्गुरतों से करें। यह हड़प्पा के सामाजिक नियंत्रण के बारे में क्या दर्शाता है?", "यह दर्शाता है कि हड़प्पा समाज का नियंत्रण नगर नियोजन, कानूनों और व्यापार संघों द्वारा होता था, न कि मेसोपोटामिया की तरह एक विशाल पुरोहित वर्ग के धार्मिक प्रभुत्व के माध्यम से।")
]:
    s1_mastery_hin.append({"type": "Case Study", "q": q, "sol": sol})

# Teach Concept (3)
for q, sol in [
    ("Explain the concept of 'Proto-Shiva' to a student, including Marshall's arguments and modern debates.", "Proto-Shiva refers to Marshall's theory that a seated horned figure on a seal represents an early form of Lord Shiva. Marshall cited his three faces, yogic posture, horns (resembling Shiva's trident), and animal surroundings (Shiva as Pashupati). Modern critics argue the figure represents a local bovine deity of fertility rather than Shiva."),
    ("Explain why the soot staining on Mother Goddess figurines is key to understanding domestic worship.", "If figurines were merely toys, they wouldn't have burns. Soot in their cup-like panniers proves oil or incense was lit in front of them inside houses. This shows they were active icons in household family shrines, representing fertility and birth worship."),
    ("Explain the concept of a 'decentralized religion' and how it applies to the Indus Civilisation.", "Unlike civilizations with central state temples (like Egypt), a decentralized religion has no official central temple. Instead, worship is domestic (in house shrines), nature-based (trees, animals), and civic (public baths), showing that religion was integrated into daily life without a dominant priesthood.")
]:
    s1_mastery_eng.append({"type": "Teach Concept", "q": q, "sol": sol})

for q, sol in [
    ("एक छात्र को 'आदि-शिव' (Proto-Shiva) की अवधारणा समझाएं, जिसमें मार्शल के तर्क और आधुनिक विवाद शामिल हों।", "आदि-शिव से तात्पर्य मार्शल के इस सिद्धांत से है कि मुहर पर आसीन सींग वाले देवता शिव का प्रारंभिक रूप हैं। उन्होंने इसके चेहरे, योग मुद्रा, त्रिशूल जैसे सींग और पशुओं (शिव पशुपति के रूप में) का हवाला दिया। आलोचक इसे शिव के बजाय बैल के रूप में वनस्पति का देवता मानते हैं।"),
    ("समझाएं कि मातृदेवी की मूर्तियों पर मिली कालिख घरेलू पूजा को समझने के लिए क्यों महत्वपूर्ण है।", "यदि मूर्तियाँ केवल खिलौने होतीं, तो उन पर जलने के निशान नहीं होते। उनके प्यालों में जमा कालिख प्रमाणित करती है कि घरों में उनके सामने तेल या धूप जलाई जाती थी। यह दर्शाता है कि वे पारिवारिक पूजा स्थलों में उर्वरता की सक्रिय आराध्य देवियाँ थीं।"),
    ("विकेंद्रीकृत धर्म' (decentralized religion) की अवधारणा समझाएं और यह सिंधु सभ्यता पर कैसे लागू होती है।", "केंद्रीय मंदिर-राज्य वाले देशों के विपरीत, विकेंद्रीकृत धर्म में कोई एक केंद्रीय मंदिर नहीं होता। पूजा घरेलू स्तर पर (घरों में), प्रकृति पर (पेड़ों, पशुओं की) और नागरिक स्तर पर (सार्वजनिक स्नान) होती थी, जिससे सिद्ध होता है कि धर्म बिना किसी मुख्य पुरोहित के दैनिक जीवन का हिस्सा था।")
]:
    s1_mastery_hin.append({"type": "Teach Concept", "q": q, "sol": sol})

print(f"Section 1 Religions Mastery questions populated: {len(s1_mastery_eng)} (Eng), {len(s1_mastery_hin)} (Hin)")


# =========================================================================
# SECTION 2: ANIMISM, TREE & ANIMAL WORSHIP, AND THERIANTHROPIC BELIEFS
# =========================================================================
s2_mastery_eng = []
s2_mastery_hin = []

# MCQ (5)
for q, opts, ans, sol in [
    ("Which tree was widely considered sacred and represented most frequently on Harappan seals?", ["Pipal tree (Ficus religiosa)", "Banyan tree (Ficus benghalensis)", "Neem tree (Azadirachta indica)", "Mango tree (Mangifera indica)"], 0, "The Pipal tree is the most common sacred plant represented on seals and pottery."),
    ("The mythical one-horned animal depicted on a majority of Harappan seals is known as the:", ["Unicorn", "Chimera", "Minotaur", "Pegasus"], 0, "The Unicorn is the most common mythical, zoomorphic representation on Harappan seals."),
    ("What was the primary purificatory architectural structure located on the Citadel of Mohenjo-daro?", ["The Great Bath", "The Granary", "The Assembly Hall", "The Pillared Palace"], 0, "The Great Bath was built for purificatory, water-based civic rituals."),
    ("The Unicorn motif on seals is invariably depicted standing in front of which object?", ["A standard or censer (incense burner)", "A heavy wooden chariot", "A stone pillar with inscriptions", "A public water trough"], 0, "The Unicorn stands before a two-tiered standard or censer, interpreted as a cult object."),
    ("What does the term 'therianthropic' refer to in Harappan iconography?", ["Hybrid composite figures combining human and animal features", "Miniature animal toys with moving wheel parts", "Square seals containing only script characters", "Standardized cubic chert weights"], 0, "Therianthropes are composite hybrid creatures, like tiger-bodied men or horned figures.")
]:
    s2_mastery_eng.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("हड़प्पा की मुहरों पर सबसे अधिक किस वृक्ष को पवित्र मानकर चित्रित किया गया था?", ["पीपल का वृक्ष (Ficus religiosa)", "बरगद का वृक्ष", "नीम का वृक्ष", "आम का वृक्ष"], 0, "पीपल का वृक्ष मुहरों और चित्रित बर्तनों पर सबसे अधिक मिलने वाला पवित्र वृक्ष है।"),
    ("हड़प्पा की अधिकांश मुहरों पर अंकित काल्पनिक एक सींग वाला पशु किस नाम से जाना जाता है?", ["यूनिकॉर्न (Unicorn)", "चिमेरा (Chimera)", "मिनोटौर", "पेगासस"], 0, "मुहरों पर एक सींग वाले काल्पनिक पशु (Unicorn) का चित्रण सबसे अधिक मिलता है।"),
    ("मोहनजोदड़ो के दुर्ग (Citadel) पर स्थित मुख्य अनुष्ठानिक जलाशय वास्तुकला कौन सी थी?", ["विशाल स्नानागार (Great Bath)", "विशाल अन्न भंडार", "सभा भवन", "स्तंभों वाला महल"], 0, "विशाल स्नानागार अनुष्ठानिक और सामूहिक स्नान के लिए निर्मित मुख्य जलाशय था।"),
    ("मुहरों पर एक सींग वाला पशु हमेशा किस वस्तु के आगे खड़ा दिखाया जाता है?", ["एक धूपदान या पात्र (standard/censer)", "एक भारी लकड़ी का रथ", "अभिलेखों वाला पत्थर का स्तंभ", "एक सार्वजनिक पानी की टंकी"], 0, "एक सींग वाला बैल हमेशा एक दो-खंडों वाले धूपदान या धार्मिक पात्र के आगे खड़ा होता है।"),
    ("हड़प्पा मुहर कला में प्रयुक्त शब्द 'थेरियनथ्रोपिक' (therianthropic) किसे दर्शाता है?", ["मानव और पशु के अंगों को मिलाने वाली मिश्रित आकृतियाँ", "चलने वाले पहियों वाले मिट्टी के खिलौने", "केवल अक्षरों वाली चौकोर मुहरें", "मानकीकृत वर्गाकार चर्ट बाट"], 0, "मिश्रित मानव-पशु आकृतियों (जैसे बाघ के शरीर वाले मनुष्य) को थेरियनथ्रोपिक कहा जाता है।")
]:
    s2_mastery_hin.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# Multi-Correct MCQ (5)
for q, opts, ans, sol in [
    ("Which of the following plants are represented in Harappan seals and painted pottery? (Select all that apply)", ["Pipal leaves", "Acacia branches", "Wild palms", "Maize stalks"], [0, 1, 2], "Pipal, acacia, and palms are depicted; maize was unknown to Harappans."),
    ("Select the features of the Great Bath of Mohenjo-daro: (Select all that apply)", ["Waterproofed using a layer of natural bitumen", "Burnt bricks laid in fine gypsum mortar", "Wide staircases on the north and south ends", "Fitted with iron pipe connections"], [0, 1, 2], "It used bitumen and gypsum mortar, and had north/south stairs. Iron did not exist."),
    ("Identify the real animals depicted realistically on Harappan seals: (Select all that apply)", ["Humped bull (Zebu)", "Rhinoceros", "Elephant", "Lion"], [0, 1, 2], "Zebu, rhino, and elephant are common. Lions are absent from Harappan seal glyptic art."),
    ("Which of the following elements characterize Harappan animism? (Select all that apply)", ["Reverence for sacred trees like the Pipal", "Worship of zoomorphic mythical creatures like the Unicorn", "Belief in therianthropic composite protector spirits", "Worship of anthropomorphic Sun and Moon gods with wings"], [0, 1, 2], "Animism focused on Pipal, Unicorn, and composite spirits. Winged Sun/Moon gods are Mesopotamian."),
    ("Select the objects suggesting a belief in magic and protective charms: (Select all that apply)", ["Terracotta tablets depicting mythological battles", "Faience amulets worn on the body", "Steatite beads with geometric engravings", "Large iron swords placed under house doors"], [0, 1, 2], "Tablets, amulets, and beads were used as charms. Iron was unknown.")
]:
    s2_mastery_eng.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("निम्नलिखित में से किन पौधों का अंकन हड़प्पा की मुहरों और बर्तनों पर मिलता है? (सभी लागू विकल्प चुनें)", ["पीपल के पत्ते", "बबूल की शाखाएं", "खजूर के पेड़", "मक्के के भुट्टे"], [0, 1, 2], "पीपल, बबूल और खजूर चित्रित हैं; मक्का हड़प्पा काल में अज्ञात था।"),
    ("मोहनजोदड़ो के विशाल स्नानागार की विशेषताओं का चयन करें: (सभी लागू विकल्प चुनें)", ["प्राकृतिक तारकोल (bitumen) की जलरोधी परत", "जिप्सम गारे में लगी पकी ईंटें", "उत्तरी और दक्षिणी छोर पर सीढ़ियाँ", "लोहे के पाइपों का फिटिंग"], [0, 1, 2], "यह जिप्सम गारे और तारकोल की परत से ईंटों द्वारा बना था, उत्तर-दक्षिण सीढ़ियां थीं। लोहा नहीं था।"),
    ("हड़प्पा की मुहरों पर सजीव चित्रित वास्तविक पशुओं की पहचान करें: (सभी लागू विकल्प चुनें)", ["कूबड़ वाला सांड (Zebu)", "गैंडा", "हाथी", "शेर"], [0, 1, 2], "कूबड़ वाला सांड, गैंडा और हाथी आम हैं। मुहर कला में शेर अनुपस्थित है।"),
    ("निम्नलिखित में से कौन से लक्षण हड़प्पा के जीववाद (animism) को दर्शाते हैं? (सभी लागू विकल्प चुनें)", ["पीपल जैसे पवित्र वृक्षों के प्रति श्रद्धा", "एक सींग वाले काल्पनिक जीव की पूजा", "मिश्रित पशु-मानव रक्षक आत्माओं में विश्वास", "पंखों वाले सूर्य और चंद्रमा देवताओं की पूजा"], [0, 1, 2], "पीपल, एक सींग वाले जीव और मिश्रित आत्माओं की पूजा जीववाद है। पंख वाले सूर्य देव यहाँ नहीं मिले हैं।"),
    ("बुरी आत्माओं से सुरक्षा और जादू-टोने के विश्वास को दर्शाने वाली वस्तुओं का चयन करें: (सभी लागू विकल्प चुनें)", ["पौराणिक दृश्यों को दर्शाती मिट्टी की पट्टियाँ", "शरीर पर पहने जाने वाले फेयॉन्स के ताबीज", "ज्यामितीय नक्काशी वाले सेलखड़ी के मनके", "घरों के दरवाजों के नीचे रखी लोहे की तलवारें"], [0, 1, 2], "पट्टियाँ, ताबीज और मनके सुरक्षात्मक थे। लोहा सभ्यता में अज्ञात था।")
]:
    s2_mastery_hin.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# True/False (8)
for q, ans, sol in [
    ("The Great Bath was located in the residential Lower Town area of Mohenjo-daro.", False, "It was situated on the Citadel mound, indicating ritual and public importance."),
    ("The Pipal tree is depicted with a horned deity standing inside its branches on some seals.", True, "True. This represents a tree deity or spirit worshiped by Harappans."),
    ("The Unicorn is depicted with two curved horns when viewed in profile.", False, "False. It is shown with a single curved horn, hence 'Unicorn'."),
    ("Natural bitumen (asphalt) was used to seal the bricks of the Great Bath.", True, "True. A 2 cm layer of bitumen prevented water seepage."),
    ("The humped bull (Zebu) is carved with great anatomical realism on seals.", True, "True. These representations show majestic dewlaps and humps."),
    ("Amulets made of clay and faience suggest that Harappans feared malevolent spirits.", True, "True. They are interpreted as protective charms to ward off evil."),
    ("The tree-worship seal depicts a row of nine figures standing below the tree.", False, "False. The row contains seven figures (often linked to seven sister spirits)."),
    ("Therianthropic figures combine animal bodies with human parts.", True, "True. An example is the tiger-bodied man with bovine horns.")
]:
    s2_mastery_eng.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("विशाल स्नानागार मोहनजोदड़ो के रिहाइशी निचले शहर (Lower Town) में स्थित था।", False, "यह दुर्ग (Citadel) पर स्थित था, जो इसके सार्वजनिक व अनुष्ठानिक महत्व को दर्शाता है।"),
    ("कुछ मुहरों पर पीपल के वृक्ष की शाखाओं के बीच एक सींग वाले देवता को खड़ा दिखाया गया है।", True, "सत्य। यह वृक्ष देवता या प्रकृति की आत्मा को दर्शाता है।"),
    ("एक सींग वाला बैल प्रोफाइल (पार्श्व) दृश्य में दो घुमावदार सींगों के साथ दिखाया गया है।", False, "असत्य। वह एक ही घुमावदार सींग के साथ दिखाया गया है, इसलिए उसे Unicorn कहते हैं।"),
    ("विशाल स्नानागार की ईंटों को सील करने के लिए प्राकृतिक तारकोल (bitumen) का उपयोग किया गया था।", True, "सत्य। रिसाव रोकने के लिए जिप्सम गारे के पीछे तारकोल की परत लगाई गई थी।"),
    ("मुहरों पर कूबड़ वाले सांड (Zebu) का चित्रण बहुत सजीव और वास्तविक है।", True, "सत्य। इन मुहरों पर सांड के कूबड़ और गलकंबल का उत्कृष्ट विवरण मिलता है।"),
    ("मिट्टी और फेयॉन्स के ताबीज संकेत देते हैं कि हड़प्पा वासी बुरी आत्माओं से डरते थे।", True, "सत्य। इन्हें बुरी नजर से बचने के लिए पहना जाता था।"),
    ("वृक्ष पूजा की मुहर में पेड़ के नीचे नौ आकृतियों को एक पंक्ति में खड़ा दिखाया गया है।", False, "असत्य। इस पंक्ति में सात आकृतियाँ (seven figures) खड़ी दिखाई गई हैं।"),
    ("थेरियनथ्रोपिक (therianthropic) आकृतियां जानवरों के शरीर और मानव अंगों को जोड़ती हैं।", True, "सत्य। जैसे सींगों वाला मानव सिर और बाघ का धड़।")
]:
    s2_mastery_hin.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

# Fill Blank (8)
for q, ans, sol in [
    ("The tree most commonly represented as sacred on seals is the ___________.", "Pipal", "The Pipal tree (Ficus religiosa) was highly revered."),
    ("The Great Bath was waterproofed using gypsum mortar and ___________.", "bitumen", "Bitumen (asphalt) was applied to prevent leaks."),
    ("The mythical one-horned animal depicted on seals is the ___________.", "Unicorn", "The Unicorn is the dominant mythical animal motif."),
    ("The Great Bath is located on the elevated ___________ mound of Mohenjo-daro.", "Citadel", "It was built on the Citadel mound."),
    ("The standard depicted in front of the Unicorn is interpreted as a ___________.", "censer", "It is interpreted as a censer or incense burner."),
    ("Figures combining human and animal features are termed ___________.", "therianthropes", "Therianthropes are hybrid composite figures."),
    ("The realistic humped bull depicted on seals is the ___________.", "Zebu", "The humped bull is biologically the Zebu."),
    ("Small tablets worn to protect against evil spirits are called ___________.", "amulets", "Amulets were used for magical protection.")
]:
    s2_mastery_eng.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("मुहरों पर सबसे अधिक पवित्र रूप में चित्रित वृक्ष ___________ है।", "पीपल", "पीपल (Pipal) को सिंधु काल से ही पवित्र माना जाता था।"),
    ("विशाल स्नानागार को जिप्सम गारे और ___________ का उपयोग करके जलरोधी बनाया गया था।", "तारकोल", "तारकोल (bitumen/asphalt) का लेप रिसाव रोकता था।"),
    ("मुहरों पर अंकित सींग वाला काल्पनिक पशु ___________ कहलाता है।", "यूनिकॉर्न", "एक सींग वाले बैल को यूनिकॉर्न (Unicorn) कहा जाता है।"),
    ("विशाल स्नानागार मोहनजोदड़ो के ऊंचे ___________ टीले पर स्थित है।", "दुर्ग", "यह दुर्ग (Citadel) क्षेत्र में स्थित है।"),
    ("एक सींग वाले पशु के आगे बने धार्मिक पात्र को ___________ माना जाता है।", "धूपदानी", "इसे धूपदानी (censer) या धार्मिक मानक माना जाता है।"),
    ("मानव और पशु दोनों के शारीरिक लक्षणों को जोड़ने वाली आकृतियाँ ___________ कहलाती हैं।", "थेरियनथ्रोपिक", "इन्हें मिश्रित पशु-मानव (therianthropic) आकृतियाँ कहते हैं।"),
    ("मुहरों पर सजीव रूप से अंकित कूबड़ वाले बैल का जैविक नाम ___________ है।", "Zebu", "कूबड़ वाले सांड को जेबू (Zebu) सांड कहा जाता है।"),
    ("बुरी नजर और प्रेत आत्माओं से रक्षा के लिए शरीर पर बांधे जाने वाले पत्थरों को ___________ कहते हैं।", "ताबीज", "इन्हें सुरक्षात्मक ताबीज (amulets) कहा जाता है।")
]:
    s2_mastery_hin.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

# Match the Following (3)
s2_mastery_eng.extend([
    {
        "type": "Match the Following",
        "q": "Match the animistic motifs with their representations:",
        "items": [{"left": "I. Unicorn", "key": "A"}, {"left": "II. Zebu", "key": "B"}, {"left": "III. Tiger-man", "key": "C"}],
        "options": [{"val": "A", "text": "A. Mythical single-horned animal with a censer"}, {"val": "B", "text": "B. Majestic humped bull carved with realism"}, {"val": "C", "text": "C. Therianthropic hybrid creature on seals"}],
        "sol": "Unicorn has a censer, Zebu is the humped bull, and Tiger-man is a therianthrope."
    },
    {
        "type": "Match the Following",
        "q": "Match the features of the Great Bath with their materials/functions:",
        "items": [{"left": "I. Waterproofing", "key": "A"}, {"left": "II. Steps", "key": "B"}, {"left": "III. Water supply", "key": "C"}],
        "options": [{"val": "A", "text": "A. Thick layer of natural bitumen (asphalt)"}, {"val": "B", "text": "B. North and South brick stairs"}, {"val": "C", "text": "C. Large double-ringed brick well in adjacent room"}],
        "sol": "Waterproofing is bitumen, steps are north/south stairs, and water supply is from the well."
    },
    {
        "type": "Match the Following",
        "q": "Match the natural elements with their religious symbolism:",
        "items": [{"left": "I. Pipal tree", "key": "A"}, {"left": "II. Great Bath", "key": "B"}, {"left": "III. Amulet", "key": "C"}],
        "options": [{"val": "A", "text": "A. Tree deity and spirits painted on pots"}, {"val": "B", "text": "B. Public purificatory bathing and civic water rituals"}, {"val": "C", "text": "C. Protection against evil spirits and magic"}],
        "sol": "Pipal is tree deity, Great Bath is water purification, and Amulet is protection."
    }
])

s2_mastery_hin.extend([
    {
        "type": "Match the Following",
        "q": "जीववादी रूपांकनों को उनके चित्रण से सुमेलित करें:",
        "items": [{"left": "I. एक सींग वाला पशु", "key": "A"}, {"left": "II. जेबू (Zebu)", "key": "B"}, {"left": "III. बाघ-मानव", "key": "C"}],
        "options": [{"val": "A", "text": "A. काल्पनिक एक सींग वाला पशु जिसके आगे धूपदानी है"}, {"val": "B", "text": "B. सजीव रूप में तराशा गया कूबड़ वाला बैल"}, {"val": "C", "text": "C. मुहरों पर चित्रित मिश्रित मानव-पशु आकृति"}],
        "sol": "एक सींग वाले पशु के आगे धूपदानी है, जेबू कूबड़ वाला बैल है, और बाघ-मानव मिश्रित जीव है।"
    },
    {
        "type": "Match the Following",
        "q": "विशाल स्नानागार की विशेषताओं को उनके घटकों से सुमेलित करें:",
        "items": [{"left": "I. जलरोधी कोटिंग", "key": "A"}, {"left": "II. सीढ़ियाँ", "key": "B"}, {"left": "III. पानी का कुआं", "key": "C"}],
        "options": [{"val": "A", "text": "A. प्राकृतिक तारकोल (bitumen) की मोटी परत"}, {"val": "B", "text": "B. उत्तर और दक्षिण में ईंटों से बने पायदान"}, {"val": "C", "text": "C. बगल के कमरे में बना दोहरे घेरे वाला ईंट का कुआं"}],
        "sol": "जलरोधी तारकोल से था, सीढ़ियां उत्तर-दक्षिण में थीं, और पानी कुएं से आता था।"
    },
    {
        "type": "Match the Following",
        "q": "प्राकृतिक तत्वों को उनके धार्मिक महत्व से सुमेलित करें:",
        "items": [{"left": "I. पीपल का पेड़", "key": "A"}, {"left": "II. विशाल स्नानागार", "key": "B"}, {"left": "III. ताबीज (Amulet)", "key": "C"}],
        "options": [{"val": "A", "text": "A. टहनियों में रहने वाले वृक्ष देवता और पीपल पत्ती पेंटिंग"}, {"val": "B", "text": "B. अनुष्ठानिक शुद्धिकरण स्नान और सामूहिक जल पूजा"}, {"val": "C", "text": "C. बुरी आत्माओं और जादू-टोने से बचाव"}],
        "sol": "पीपल वृक्ष देवता से, विशाल स्नानागार शुद्धिकरण से, और ताबीज बुरी आत्माओं से बचाव से सुमेलित है।"
    }
])

# One-Liner (8)
for q, sol in [
    ("Which tree was widely worshiped by Harappans?", "The Pipal tree (Ficus religiosa)."),
    ("What is the most common mythical creature on Indus seals?", "The Unicorn."),
    ("Where is the Great Bath situated?", "On the Citadel of Mohenjo-daro."),
    ("What waterproofing material was used in the Great Bath?", "Bitumen (asphalt)."),
    ("Define the term 'therianthrope'.", "A mythological hybrid creature combining human and animal features."),
    ("What stood in front of the Unicorn on seals?", "A two-tiered standard or censer (incense burner)."),
    ("Which real domestic animal was associated with strength and fertility?", "The humped bull (Zebu)."),
    ("What was the purpose of terracotta amulets?", "To serve as protective charms against evil spirits and bad luck.")
]:
    s2_mastery_eng.append({"type": "One-Liner", "q": q, "sol": sol})

for q, sol in [
    ("हड़प्पा वासियों द्वारा किस वृक्ष की सर्वाधिक पूजा की जाती थी?", "पीपल वृक्ष (Ficus religiosa) की।"),
    ("सिंधु मुहरों पर सबसे आम काल्पनिक जीव कौन सा है?", "एक सींग वाला पशु (Unicorn)।"),
    ("विशाल स्नानागार कहाँ स्थित है?", "मोहनजोदड़ो के दुर्ग (Citadel) पर।"),
    ("विशाल स्नानागार में किस जलरोधी सामग्री का उपयोग किया गया था?", "प्राकृतिक तारकोल (bitumen या asphalt) का।"),
    ("थेरियनथ्रोप' (therianthrope) को परिभाषित करें।", "एक पौराणिक मिश्रित जीव जिसमें मानव और पशु दोनों के अंग जुड़े हों।"),
    ("मुहरों पर एक सींग वाले पशु के आगे क्या रखा होता है?", "एक दो-खंडों वाला धार्मिक मानक या धूपदानी।"),
    ("ताकत और उर्वरता से जुड़ा कौन सा वास्तविक पालतू जानवर मुहरों पर मिलता है?", "कूबड़ वाला सांड (Zebu)।"),
    ("मिट्टी के ताबीजों का मुख्य उद्देश्य क्या था?", "बुरी आत्माओं और जादू-टोने से बचने के लिए रक्षा कवच के रूप में।")
]:
    s2_mastery_hin.append({"type": "One-Liner", "q": q, "sol": sol})

# Assertion-Reason (8)
for q, ans, sol in [
    ("Assertion (A): The Great Bath was designed for ritual bathing and civic purification.\nReason (R): It is situated on the Citadel, waterproofed with bitumen, and surrounded by dressing rooms.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): The Unicorn seal motif represents a real extinct bovine species.\nReason (R): Unicorn skeletons have been excavated at several sites in Gujarat.", 4, "Both A and R are false: the Unicorn is mythical, and no such bones exist."),
    ("Assertion (A): Pipal tree worship was a central element of Harappan animism.\nReason (R): Multiple seals depict a horned deity standing inside a Pipal tree with worshippers.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): The Great Bath was fed by canal water flowing directly from the Indus River.\nReason (R): River water was cleaner than underground well water during flooding.", 4, "Both A and R are false. The Bath was fed by a large double-ringed well in an adjacent room."),
    ("Assertion (A): Humped bull seals are celebrated for their artistic realism.\nReason (R): Scribes carved detailed anatomical features showing the bull's dewlap and muscle hump.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Terracotta amulets suggest a belief in magic and evil eye.\nReason (R): Amulets were worn as protective charms to ward off malevolent forces.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Therianthropic tiger-men reflect a belief in shape-shifting or protective spirits.\nReason (R): Hybrid animal-human figures are common across ancient Bronze Age mythologies.", 1, "Both A and R are true but R does not explain why Harappans specifically had shape-shifting beliefs."),
    ("Assertion (A): Acacia and palm leaves are never depicted on Harappan pottery.\nReason (R): The Pipal was the only tree that grew in the dry Indus Valley climate.", 4, "Both A and R are false. Other plants occur, and many trees grew in the fertile Indus basin.")
]:
    s2_mastery_eng.append({"type": "Assertion-Reason", "q": q, "opts": ar_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("कथन (A): विशाल स्नानागार का निर्माण अनुष्ठानिक स्नान और शुद्धि के लिए किया गया था।\nकारण (R): यह दुर्ग पर स्थित था, तारकोल से जलरोधी बनाया गया था और इसके चारों ओर कपड़े बदलने के कमरे थे।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): एक सींग वाले सांड (Unicorn) का रूपांकन एक वास्तविक विलुप्त बैल का प्रतिनिधित्व करता है।\nकारण (R): गुजरात के कई स्थलों से एक सींग वाले बैलों के कंकाल उत्खनित किए गए हैं।", 4, "A और R दोनों असत्य हैं: यह एक काल्पनिक जीव है और ऐसे कोई कंकाल नहीं मिले हैं।"),
    ("कथन (A): पीपल वृक्ष की पूजा हड़प्पा के जीववाद (animism) का एक प्रमुख हिस्सा थी।\nकारण (R): कई मुहरों पर सींग वाले देवता को पीपल की शाखाओं के बीच खड़ा दिखाया गया है।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): विशाल स्नानागार में सिंधु नदी से सीधे नहर द्वारा पानी लाया जाता था।\nकारण (R): बाढ़ के दौरान नदी का पानी जमीन के नीचे के कुएं के पानी से अधिक साफ होता था।", 4, "A और R दोनों असत्य हैं। स्नानागार में पानी बगल के कमरे के कुएं से आता था।"),
    ("कथन (A): कूबड़ वाले बैल की मुहरें अपने सजीव कलात्मक यथार्थवाद के लिए प्रसिद्ध हैं।\nकारण (R): शिल्पकारों ने सांड के भारी गलकंबल और कूबड़ की मांसपेशियों को बारीक विवरण के साथ उकेरा था।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): मिट्टी के ताबीज जादू-टोने और बुरी नजर में उनके विश्वास की ओर संकेत करते हैं।\nकारण (R): ताबीजों को बुरी आत्माओं से बचने के लिए सुरक्षात्मक कवच के रूप में पहना जाता था।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): मिश्रित बाघ-मानव आकृतियाँ रूप बदलने वाली या रक्षक आत्माओं के विश्वास को दर्शाती हैं।\nकारण (R): प्राचीन कांस्य युगीन सभ्यताओं में मानव-पशु मिश्रित चित्र आम थे।", 1, "A और R दोनों सही हैं लेकिन R, A की सही व्याख्या नहीं है क्योंकि सामान्य प्रचलन हड़प्पा के विशिष्ट विश्वास का कारण नहीं समझाता।"),
    ("कथन (A): बबूल और खजूर के पत्तों का अंकन हड़प्पा के बर्तनों पर कभी नहीं मिलता।\nकारण (R): सूखी जलवायु के कारण सिंधु घाटी में पीपल एकमात्र उगने वाला पेड़ था।", 4, "A और R दोनों असत्य हैं। बर्तनों पर बबूल/खजूर के पत्ते मिले हैं, और सिंधु घाटी में घने जंगल थे।")
]:
    s2_mastery_hin.append({"type": "Assertion-Reason", "q": q, "opts": hin_ar_opts, "ans": ans, "sol": sol})

# Statement-Based (5)
for q, ans, sol in [
    ("Consider the following statements regarding the Great Bath:\n1. The pool floor was made of flat-laid bricks set in gypsum mortar, backed by a layer of bitumen.\n2. It was located in the Lower Town of Mohenjo-daro near the market blocks.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect because it was located on the Citadel mound, not the Lower Town."),
    ("Consider the following statements regarding Pipal tree worship:\n1. The Pipal tree is shown on seals with a horned deity emerging from its branches.\n2. Only male worshippers are depicted in scenes of tree worship.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: the gender of worshippers in tree scenes is debated, and some figures wear female ornaments/bangles."),
    ("Consider the following statements regarding Unicorn seals:\n1. The Unicorn is depicted in profile with a single horn and a collar.\n2. The animal always stands in front of a standard or manger.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct, detailing the Unicorn's pose and its standard accessory."),
    ("Consider the following statements regarding animal cults:\n1. Tigers and elephants are always depicted in front of incense burners.\n2. Humped bulls are depicted realistically and suggest fertility worship.\nWhich of the statements given above is/are correct?", 1, "Statement 2 is correct. Statement 1 is incorrect: tigers and elephants never feature censer standards on seals."),
    ("Consider the following statements regarding magical beliefs:\n1. Terracotta amulets were worn to protect individuals from malevolent spirits.\n2. Long religious mantras are written on all amulets to explain their function.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: amulets contain short pictographic signs, and the script is undeciphered.")
]:
    s2_mastery_eng.append({"type": "Statement-Based", "q": q, "opts": mcq_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("विशाल स्नानागार के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. जलाशय का फर्श जिप्सम गारे में लगी चपटी ईंटों से बना था, जिसके पीछे तारकोल की परत थी।\n2. यह मोहनजोदड़ो के निचले शहर में बाजार के ब्लॉकों के पास स्थित था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि यह निचले शहर के बजाय दुर्ग (Citadel) पर स्थित था।"),
    ("पीपल वृक्ष पूजा के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मुहरों पर पीपल की शाखाओं के बीच से निकलते हुए एक सींग वाले देवता को दिखाया गया है।\n2. वृक्ष पूजा के दृश्यों में केवल पुरुष उपासकों को ही चित्रित किया गया है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि वृक्ष पूजा दृश्यों में उपासकों का लिंग स्पष्ट नहीं है और कुछ आकृतियाँ चूड़ियाँ पहने दिखाई देती हैं।"),
    ("एक सींग वाले पशु (Unicorn) की मुहरों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मुहरों पर इसे पार्श्व मुखाकृति (profile) में एक सींग और गर्दन के पट्टे के साथ दिखाया गया है।\n2. यह पशु हमेशा एक धार्मिक मानक या धूपदानी के आगे खड़ा होता है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 2, "दोनों कथन सही हैं, जो यूनिकॉर्न के चित्रण और उसके धूपदानी प्रतीक का विवरण देते हैं।"),
    ("पशु पंथों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. बाघ और हाथी मुहरों पर हमेशा धूपदान के आगे खड़े दिखाए जाते हैं।\n2. कूबड़ वाले सांडों का अंकन बहुत सजीव है जो बैल की उर्वरता पूजा की ओर इशारा करता है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 1, "कथन 2 सही है। कथन 1 गलत है क्योंकि बाघ और हाथी के आगे कभी धूपदान नहीं बनाया जाता था।"),
    ("जादुई विश्वासों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मिट्टी के ताबीज लोगों को बुरी नजर और आत्माओं से बचाने के लिए पहने जाते थे।\n2. सभी ताबीजों पर लंबे धार्मिक मंत्र लिखे हैं जो उनके कार्य को समझाते हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि लेख अत्यंत लघु हैं और लिपि अपठित है।")
]:
    s2_mastery_hin.append({"type": "Statement-Based", "q": q, "opts": hin_mcq_opts, "ans": ans, "sol": sol})

# Why (3)
for q, sol in [
    ("Why did the builders of the Great Bath use natural bitumen (asphalt) in its construction?", "Bitumen is a natural waterproof sealant. By applying a layer of bitumen between the inner brick lining and the outer brick wall, they prevented water from leaking out into the Citadel platforms."),
    ("Why did Unicorn seals feature a 'standard' or censer in front of the animal?", "The standard acted as a sacred cult object, representing an incense burner or filtering device, which signified the ritual importance of the Unicorn in Harappan beliefs."),
    ("Why are therianthropic composite creatures (like tiger-men) significant in Harappan art?", "They show that Harappan mythology contained complex concepts of shape-shifting, guardian spirits, and animal-human alliances, indicating a sophisticated animistic cosmology.")
]:
    s2_mastery_eng.append({"type": "Why", "q": q, "sol": sol})

for q, sol in [
    ("विशाल स्नानागार के निर्माताओं ने इसके निर्माण में प्राकृतिक तारकोल (bitumen) का उपयोग क्यों किया था?", "तारकोल एक प्राकृतिक जलरोधी सीलेंट है। ईंटों की भीतरी परत और बाहरी दीवार के बीच तारकोल की परत लगाने से जलाशय का पानी रिसकर बाहर चबूतरे में नहीं जा पाता था।"),
    ("एक सींग वाले पशु (Unicorn) की मुहरों पर जानवर के आगे एक धूपदानी (standard) क्यों बनी होती थी?", "यह धूपदानी एक पवित्र अनुष्ठानिक वस्तु थी, जो संभवतः धूप जलाने या छननी का काम करती थी, और मुहर पर इस काल्पनिक पशु की धार्मिक महत्ता को दर्शाती थी।"),
    ("हड़प्पा कला में मिश्रित आकृतियों (जैसे बाघ-मानव) का होना क्यों महत्वपूर्ण है?", "यह दर्शाता है कि हड़प्पा वासियों के पास रूप बदलने वाले रक्षक जीवों और मानव-पशु संबंधों के जटिल मिथक थे, जो उनके उन्नत जीववादी दर्शन को उजागर करते हैं।")
]:
    s2_mastery_hin.append({"type": "Why", "q": q, "sol": sol})

# How (3)
for q, sol in [
    ("How did tree worship manifest in the daily life of Harappans?", "Artisans painted Pipal and palm leaf designs on wheel-made red pottery, and carved seals showing horned deities residing in Pipal branches with worshippers performing rites before them."),
    ("How was water managed inside the Great Bath complex?", "Clean water was drawn from a large double-ringed well in an adjacent room, filled into the bath, and dirty water was discharged through a corbelled brick drain on the side."),
    ("How did Harappans use amulets in their magical practices?", "They wore small steatite, clay, or faience tablets with protective animal icons and short inscriptions on their arms or necks to ward off diseases, evil spirits, and misfortune.")
]:
    s2_mastery_eng.append({"type": "How", "q": q, "sol": sol})

for q, sol in [
    ("वृक्ष पूजा हड़प्पा वासियों के दैनिक जीवन में कैसे प्रकट होती थी?", "कुम्हार चाक पर बने लाल बर्तनों पर पीपल और खजूर के पत्तों के चित्र बनाते थे, और शिल्पकार मुहरों पर पीपल की शाखाओं में रहने वाले देवताओं और उनके आगे पूजा करते लोगों को तराशते थे।"),
    ("विशाल स्नानागार परिसर के भीतर पानी का प्रबंधन कैसे किया जाता था?", "बगल के कमरे में बने दोहरे घेरे वाले कुएं से साफ पानी निकालकर स्नानागार में भरा जाता था, और उपयोग के बाद गंदा पानी स्नानागार के किनारे बनी ढकी मेहराबदार नाली से बाहर निकाला जाता था।"),
    ("हड़प्पा वासी जादुई प्रथाओं में ताबीज (amulet) का उपयोग कैसे करते थे?", "वे मिट्टी, सेलखड़ी या फेयॉन्स की छोटी गोल/चौकोर पट्टियों को बाजू या गले में धागे से बांधते थे, जिन पर बने रक्षक पशुओं के चित्र उन्हें बीमारी और बुरी शक्तियों से बचाते थे।")
]:
    s2_mastery_hin.append({"type": "How", "q": q, "sol": sol})

# Case Study (3)
for q, sol in [
    ("Case Study: The Great Bath was built on the Citadel at Mohenjo-daro, with adjacent purificatory platforms. What does this layout prove about the role of water in Harappan society?", "It proves that water-based purification and communal bathing were formal, high-status civic rituals controlled by the elites and integrated into the governance of the city."),
    ("Case Study: Unicorn seals are the most abundant (over 60% of all seals found), but no bones of a one-horned animal exist. What does this prove about the nature of this symbol?", "It proves the Unicorn was a mythical animal symbol representing a dominant socio-political group, clan, or merchant guild, rather than a real biological species."),
    ("Case Study: Analyze the tree deity seal showing a line of seven figures wearing tunics and feathers. How does this compare with later Indian folklore?", "It represents a precursor to the historical Indian worship of the Saptamatrika (seven mothers) or forest deities (seven sisters), showing structural continuity in folk beliefs.")
]:
    s2_mastery_eng.append({"type": "Case Study", "q": q, "sol": sol})

for q, sol in [
    ("केस स्टडी: विशाल स्नानागार मोहनजोदड़ो के दुर्ग पर स्नान चबूतरों के साथ बनाया गया था। यह व्यवस्था हड़प्पा समाज में पानी की भूमिका के बारे में क्या साबित करती है?", "यह साबित करती है कि जल आधारित शुद्धि और सामूहिक स्नान औपचारिक, उच्च-स्तरीय नागरिक अनुष्ठान थे जो दुर्ग के शासकों द्वारा नियंत्रित थे और नगर प्रशासन का हिस्सा थे।"),
    ("केस स्टडी: एक सींग वाले सांड की मुहरें सबसे अधिक (60% से अधिक) मिली हैं, लेकिन ऐसे किसी पशु की एक भी हड्डी नहीं मिली। यह इस प्रतीक के बारे में क्या साबित करता है?", "यह साबित करता है कि एक सींग वाला पशु एक पौराणिक प्रतीक था जो किसी वर्चस्वशाली सामाजिक-राजनीतिक वर्ग, कबीले या व्यापारी गिल्ड का प्रतिनिधित्व करता था, न कि कोई वास्तविक जानवर।"),
    ("केस स्टडी: पीपल के वृक्ष देवता की मुहर पर बने सात उपासकों (जिनके सिर पर पंख हैं) का विश्लेषण करें। यह बाद की भारतीय लोककथाओं से कैसे मेल खाता है?", "यह बाद के भारतीय धर्म में पूजी जाने वाली सप्तमातृका (सात माताओं) या वन देवियों (सात बहनों) के आदि रूप को दर्शाता है, जो लोक मान्यताओं में संरचनात्मक निरंतरता को प्रमाणित करता है।")
]:
    s2_mastery_hin.append({"type": "Case Study", "q": q, "sol": sol})

# Teach Concept (3)
for q, sol in [
    ("Explain the concept of 'Animism' to a student using Harappan examples.", "Animism is the belief that trees, animals, and natural objects possess spiritual souls. In Harappa, this is shown by the worship of the Pipal tree as the home of a deity, the sacred representation of bulls and mythical unicorns on seals, and the use of protective charms indicating spirits in nature."),
    ("Explain how the Great Bath reflects civic planning serving religious needs.", "The Great Bath is not a crude pond. It features brick-built steps, waterproofing with bitumen, a dedicated well for clean water, and a huge vaulted drain. This shows that the engineers designed high-yield municipal works to facilitate religious civic bathing, merging engineering with ritual."),
    ("Explain the mythological meaning behind composite therianthropic figures on seals.", "These hybrid figures (like human-headed tigers) are composite beasts. They represent mythical protector spirits or shape-shifting shamans who could harness the power of both humans and wild beasts, showing a belief in nature's interconnected spiritual forces.")
]:
    s2_mastery_eng.append({"type": "Teach Concept", "q": q, "sol": sol})

for q, sol in [
    ("एक छात्र को हड़प्पा के उदाहरणों का उपयोग करते हुए 'जीववाद' (Animism) की अवधारणा समझाएं।", "जीववाद यह विश्वास है कि पेड़ों, पशुओं और प्राकृतिक वस्तुओं में भी आध्यात्मिक आत्मा होती है। हड़प्पा में यह पीपल के पेड़ को देवता का घर मानकर पूजने, मुहरों पर बैल व काल्पनिक सांडों के अंकन और बुरी शक्तियों से रक्षा के लिए ताबीज पहनने से दिखाई देता है।"),
    ("समझाएं कि विशाल स्नानागार किस प्रकार धार्मिक आवश्यकताओं की पूर्ति करने वाले नागरिक नियोजन को दर्शाता है।", "स्नानागार कोई साधारण गड्ढा नहीं है। इसमें ईंटों की सीढ़ियाँ, तारकोल की जलरोधी परत, पानी के लिए कुआं और विशाल निकासी नाली बनी है। यह दर्शाता है कि इंजीनियरों ने अनुष्ठानिक स्नान को सुगम बनाने के लिए उच्च स्तरीय नागरिक वास्तुकला बनाई थी।"),
    ("मुहरों पर बनी मिश्रित आकृतियों (composite figures) के पीछे का पौराणिक अर्थ समझाएं।", "ये मिश्रित आकृतियाँ (जैसे मानव सिर वाले बाघ) रक्षक आत्माओं या रूप बदलने वाले जादूगरों को दर्शाती हैं, जो मनुष्यों और जंगली जानवरों दोनों की शक्ति धारण कर सकते थे, जो प्रकृति की परस्पर जुड़ी आध्यात्मिक शक्तियों में विश्वास को दर्शाता है।")
]:
    s2_mastery_hin.append({"type": "Teach Concept", "q": q, "sol": sol})

print(f"Section 2 Religions Mastery questions populated: {len(s2_mastery_eng)} (Eng), {len(s2_mastery_hin)} (Hin)")


# =========================================================================
# SECTION 3: BURIAL PRACTICES, FIRE ALTARS & RITUAL ARCHITECTURE
# =========================================================================
s3_mastery_eng = []
s3_mastery_hin = []

# MCQ (5)
for q, opts, ans, sol in [
    ("What was the standard orientation of bodies placed in Mature Harappan grave pits?", ["North-South (head to the North)", "East-West (head to the East)", "South-North (head to the South)", "West-East (head to the West)"], 0, "The standard Harappan burial orientation was North-South, with the head pointing toward the North."),
    ("At which Harappan site was a rare wooden coffin burial made of Himalayan deodar excavated?", ["Harappa (Cemetery R-37)", "Mohenjo-daro", "Lothal", "Kalibangan"], 0, "A wooden coffin burial was discovered in Cemetery R-37 at Harappa."),
    ("The double/twin burials containing two skeletons in a single grave were found at which site?", ["Lothal", "Kalibangan", "Banawali", "Rakhigarhi"], 0, "Lothal has yielded three double burials, each containing twin skeletons."),
    ("Clay-lined fire altars containing ash, charcoal, and animal bone fragments were found at:", ["Kalibangan and Lothal", "Harappa and Mohenjo-daro", "Dholavira and Banawali", "Chanhudaro and Balakot"], 0, "Fire altars have been excavated at Kalibangan and Lothal, indicating fire-worship or sacrifice."),
    ("Symbolic or cenotaph burials containing grave pottery but no human skeletal remains were found at:", ["Kalibangan", "Lothal", "Surkotada", "Harappa"], 0, "Kalibangan has yielded symbolic/cenotaph graves containing pottery and ornaments but no skeletons.")
]:
    s3_mastery_eng.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("परिपक्व हड़प्पा शवाधान गड्ढों में शवों को लिटाने की मानक दिशा क्या थी?", ["उत्तर-दक्षिण (सिर उत्तर की ओर)", "पूर्व-पश्चिम (सिर पूर्व की ओर)", "दक्षिण-उत्तर (सिर दक्षिण की ओर)", "पश्चिम-पूर्व (सिर पश्चिम की ओर)"], 0, "हड़प्पा में शवों को दफनाने की मानक दिशा उत्तर-दक्षिण थी, जिसमें सिर हमेशा उत्तर की ओर रहता था।"),
    ("हिमालयी देवदार की लकड़ी से बने एक दुर्लभ ताबूत शवाधान (wooden coffin) को किस स्थल से खोजी गई थी?", ["हड़प्पा (कब्रिस्तान R-37)", "मोहनजोदड़ो", "लोथल", "कालीबंगन"], 0, "ताबूत शवाधान हड़प्पा के R-37 कब्रिस्तान से मिला है।"),
    ("एक ही कब्र में दो कंकालों वाले जुड़वां/डबल शवाधान के साक्ष्य किस स्थल से प्राप्त हुए हैं?", ["लोथल", "कालीबंगन", "बनावली", "राखीगढ़ी"], 0, "लोथल से तीन जुड़वां शवाधान मिले हैं जिनमें दो-दो शवों को एक साथ दफनाया गया था।"),
    ("राख, कोयला और पशुओं की हड्डियों के टुकड़ों से युक्त मिट्टी की अग्नि वेदियाँ कहाँ पाई गई हैं?", ["कालीबंगन और लोथल", "हड़प्पा और मोहनजोदड़ो", "धोलावीरा और बनावली", "चन्हुदड़ो और बालाकोट"], 0, "अग्नि वेदियाँ कालीबंगन और लोथल से खोजी गई हैं, जो अग्नि पूजा या बलि को दर्शाती हैं।"),
    ("मिट्टी के बर्तन और भेंटों से युक्त प्रतीकात्मक कब्रें (बिना मानव अवशेष के) किस स्थल से मिली हैं?", ["कालीबंगन", "लोथल", "सुरकोटदा", "हड़प्पा"], 0, "कालीबंगन से प्रतीकात्मक कब्रें (cenotaphs) मिली हैं जिनमें कंकाल नहीं मिले हैं, केवल बर्तन मिले हैं।")
]:
    s3_mastery_hin.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# Multi-Correct MCQ (5)
for q, opts, ans, sol in [
    ("Which of the following funerary variations have been excavated at Harappan sites? (Select all that apply)", ["Extended North-South inhumation", "Wooden coffin burials at Harappa", "Double/twin burials at Lothal", "Monumental stone pyramids containing royal tombs"], [0, 1, 2], "Extended inhumation, coffin, and double burials exist. No pyramids or royal monuments exist."),
    ("Select the objects commonly found as grave goods in Harappan burials: (Select all that apply)", ["Painted earthenware pottery", "Copper mirrors near the head", "Bead necklaces and shell bangles", "Massive iron spears and shields"], [0, 1, 2], "Pottery, mirrors, and beads/bangles were common grave goods. Iron did not exist."),
    ("Identify the sites containing excavated clay fire altars: (Select all that apply)", ["Kalibangan", "Lothal", "Mohenjo-daro", "Chanhudaro"], [0, 1], "Fire altars are documented at Kalibangan and Lothal. None are found at Mohenjo-daro or Chanhudaro."),
    ("What are the characteristics of the fire altars found at Kalibangan Citadel? (Select all that apply)", ["Built as a row of seven rectangular pits on a mud-brick platform", "Contained central clay columns (steles)", "Contained ash, charcoal, and terracotta cakes", "Contained gold coins and silver offerings"], [0, 1, 2], "Kalibangan Citadel had a row of seven altars with central clay columns, ash, and cakes. No gold/silver coins existed."),
    ("Select the statements describing Harappan beliefs regarding the afterlife: (Select all that apply)", ["Grave pottery was filled with food and water for the journey beyond", "Personal mirrors and ornaments were buried for the deceased's spiritual use", "Amulets were buried to protect the deceased from malevolent afterlife spirits", "The deceased's physical body was expected to resurrect immediately inside the grave"], [0, 1, 2], "Burial items indicate spiritual journey tools, sustenance, and magical protection. Resurrection was not believed.")
]:
    s3_mastery_eng.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("हड़प्पा स्थलों से उत्खनित शवाधान प्रथाओं की विविधताओं का चयन करें: (सभी लागू विकल्प चुनें)", ["उत्तर-दक्षिण दिशा में फैला समाधिकरण", "हड़प्पा में लकड़ी के ताबूत शवाधान", "लोथल में जुड़वां/डबल शवाधान", "शाही कब्रों वाले विशाल पत्थर के पिरामिड"], [0, 1, 2], "समाधिकरण, ताबूत और जुड़वां शवाधान मिले हैं। पिरामिड या शाही मकबरे यहाँ नहीं थे।"),
    ("हड़प्पा कब्रों में रखी जाने वाली आम वस्तुओं का चयन करें: (सभी लागू विकल्प चुनें)", ["चित्रित मिट्टी के बर्तन (मृदभांड)", "सिर के पास रखे तांबे के दर्पण", "मनकों के हार और शंख की चूड़ियाँ", "लोहे के बड़े भाले और ढालें"], [0, 1, 2], "मृदभांड, तांबे के दर्पण और माला/चूड़ियाँ कब्रों में रखी जाती थीं। लोहा अज्ञात था।"),
    ("उन स्थलों की पहचान करें जहाँ से मिट्टी की अग्नि वेदियाँ मिली हैं: (सभी लागू विकल्प चुनें)", ["कालीबंगन", "लोथल", "मोहनजोदड़ो", "चन्हुदड़ो"], [0, 1], "अग्नि वेदियाँ कालीबंगन और लोथल में मिली हैं। मोहनजोदड़ो या चन्हुदड़ो में नहीं मिली हैं।"),
    ("कालीबंगन के दुर्ग पर मिली अग्नि वेदियों के लक्षण क्या हैं? (सभी लागू विकल्प चुनें)", ["ईंटों के चबूतरे पर सात आयताकार गड्ढों की एक पंक्ति", "बीच में मिट्टी के बेलनाकार खंभे (steles) होना", "राख, कोयला और पकी मिट्टी के त्रिकोणीय केक होना", "सोने के सिक्के और चांदी की भेंट होना"], [0, 1, 2], "दुर्ग पर सात वेदियों की पंक्ति, बीच में खंभे और राख/केक मिले हैं। सिक्के नहीं मिले हैं।"),
    ("परलोक जीवन के प्रति हड़प्पा वासियों के विश्वास को दर्शाने वाले कथनों को चुनें: (सभी लागू विकल्प चुनें)", ["कब्र के बर्तनों में यात्रा के लिए भोजन और पानी रखा जाता था", "तांबे के दर्पण और आभूषण मृत व्यक्ति की आत्मा के उपयोग के लिए रखे जाते थे", "परलोक की बुरी ताकतों से बचाने के लिए ताबीज दफनाए जाते थे", "कब्र के भीतर ही मृत व्यक्ति के शरीर का तुरंत पुनरुत्थान होना माना जाता था"], [0, 1, 2], "कब्र के सामान भोजन, पानी, दर्पण और सुरक्षात्मक ताबीज के रूप में परलोक के विश्वास को दर्शाते हैं।")
]:
    s3_mastery_hin.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# True/False (8)
for q, ans, sol in [
    ("Standard Harappan burials placed the deceased with the head pointing to the South.", False, "The head was oriented toward the North, and feet to the South."),
    ("Wooden coffins used for burials at Harappa were made of imported deodar wood.", True, "True. Deodar wood was transported from the Himalayas, indicating ritual care."),
    ("Double burials at Lothal contain the skeletons of two individuals buried in a single grave pit.", True, "True. Lothal is unique for having twin skeletons in single graves."),
    ("Fire altars are completely restricted to the Citadel and never found in the Lower Town.", False, "False. At Kalibangan, fire altars have been found in both Citadel platforms and Lower Town houses."),
    ("Graves of wealthy Harappans routinely contain massive gold ornaments and silver weapons.", False, "False. Even wealthy graves are relatively modest, with very little gold or metal weapons."),
    ("Urn/fractional burials represent secondary burial rites where bones were gathered after exposure.", True, "True. This was a common variation alongside complete inhumation."),
    ("Kalibangan symbolic burials contain grave pottery and beads but no skeletal remains.", True, "True. These function as symbolic cenotaph graves."),
    ("Harappans used pine wood to manufacture their burial coffins.", False, "False. They used deodar wood (Cedrus deodara).")
]:
    s3_mastery_eng.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("मानक हड़प्पा कब्रों में मृतकों को इस प्रकार लिटाया जाता था कि उनका सिर दक्षिण की ओर हो।", False, "सिर उत्तर की ओर और पैर दक्षिण की ओर रखे जाते थे।"),
    ("हड़प्पा में ताबूत शवाधान के लिए उपयोग की जाने वाली लकड़ी हिमालयी देवदार की थी।", True, "सत्य। देवदार की लकड़ी को हिमालय से लाया गया था, जो शवाधान अनुष्ठान के महत्व को दर्शाता है।"),
    ("लोथल के जुड़वां शवाधानों में एक ही कब्र के गड्ढे में दो व्यक्तियों के कंकाल मिले हैं।", True, "सत्य। लोथल एक ही कब्र में दो कंकाल दफनाने के साक्ष्यों के लिए प्रसिद्ध है।"),
    ("अग्नि वेदियाँ पूरी तरह दुर्ग तक ही सीमित थीं और निचले शहर में कभी नहीं पाई गईं।", False, "असत्य। कालीबंगन में ये दुर्ग के चबूतरे और निचले शहर के साधारण घरों दोनों में मिली हैं।"),
    ("अमीर हड़प्पा वासियों की कब्रों में नियमित रूप से सोने के भारी आभूषण और चांदी के हथियार मिलते हैं।", False, "असत्य। हड़प्पा की कब्रें काफी सादा हैं, बहुमूल्य धातुएं इनमें बहुत कम मिली हैं।"),
    ("कलश/आंशिक शवाधान (urn burials) द्वितीयक शवाधान थे जहाँ शव के अपघटन के बाद हड्डियाँ दफनाई जाती थीं।", True, "सत्य। यह पूर्ण समाधिकरण के साथ एक अन्य शवाधान प्रथा थी।"),
    ("कालीबंगन की प्रतीकात्मक कब्रों में बर्तन और मनके तो मिले हैं लेकिन मानव कंकाल नहीं।", True, "सत्य। इन्हें प्रतीकात्मक कब्रें (cenotaphs) माना जाता है।"),
    ("हड़प्पा वासी ताबूत बनाने के लिए चीड़ (pine) की लकड़ी का उपयोग करते थे।", False, "असत्य। वे देवदार (deodar) की लकड़ी का उपयोग करते थे।")
]:
    s3_mastery_hin.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

# Fill Blank (8)
for q, ans, sol in [
    ("The standard directional orientation of Harappan grave pits is ___________.", "North-South", "Graves were oriented strictly North-South."),
    ("The deodar wood used for the coffin burial at Harappa was sourced from the ___________.", "Himalayas", "Deodar is a coniferous wood growing in the Himalayas."),
    ("Double/twin burials containing two skeletons were excavated at ___________.", "Lothal", "Lothal is the only site with double burials in a single pit."),
    ("Clay-lined pits containing ash and charcoal used for rituals are called ___________.", "fire altars", "These are termed fire altars or ritual hearths."),
    ("Kalibangan pits containing grave pottery but no skeletons are known as ___________ burials.", "symbolic", "Symbolic (or cenotaph) burials lacked skeletal remains."),
    ("In standard graves, the head of the deceased was oriented toward the ___________.", "North", "The head pointed North."),
    ("A copper ___________ was frequently placed near the head of the deceased in graves.", "mirror", "Copper mirrors were common grave goods."),
    ("Secondary burials where bones were placed inside clay jars are called ___________ burials.", "urn", "These are urn or fractional burials.")
]:
    s3_mastery_eng.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("हड़प्पा कब्र के गड्ढों की मानक दिशात्मक स्थिति ___________ थी।", "उत्तर-दक्षिण", "शवों को उत्तर-दक्षिण (North-South) लिटाया जाता था।"),
    ("हड़प्पा में ताबूत शवाधान के लिए इस्तेमाल की गई देवदार की लकड़ी ___________ से मंगाई गई थी।", "हिमालय", "देवदार एक कोनिफेरस लकड़ी है जो हिमालय क्षेत्र में उगती है।"),
    ("एक ही कब्र में दो कंकालों वाले जुड़वां शवाधान का उत्खनन ___________ में किया गया था।", "लोथल", "लोथल में तीन जुड़वां कब्रें खोजी गई थीं।"),
    ("अनुष्ठानों के लिए राख और कोयले से युक्त मिट्टी के गड्ढों को ___________ कहा जाता है।", "अग्नि वेदियाँ", "इन्हें अग्नि वेदियाँ (fire altars) या यज्ञ कुंड कहा जाता है।"),
    ("कालीबंगन में कंकाल के बिना केवल बर्तन रखने वाली कब्रों को ___________ शवाधान कहा जाता है।", "प्रतीकात्मक", "इन्हें प्रतीकात्मक (symbolic या cenotaph) शवाधान कहा जाता है।"),
    ("मानक कब्रों में, मृत व्यक्ति का सिर ___________ दिशा की ओर रखा जाता था।", "उत्तर", "सिर हमेशा उत्तर (North) की ओर रखा जाता था।"),
    ("कब्रों में मृत व्यक्ति के सिर के पास अक्सर तांबे का एक ___________ रखा जाता था।", "दर्पण", "तांबे का दर्पण (mirror) एक लोकप्रिय कब्र सामग्री थी।"),
    ("हड्डियों को मिट्टी के बर्तनों में रखकर दफनाने वाले द्वितीयक शवाधान को ___________ शवाधान कहते हैं।", "कलश", "इसे कलश (urn) या आंशिक शवाधान कहा जाता है।")
]:
    s3_mastery_hin.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

# Match the Following (3)
s3_mastery_eng.extend([
    {
        "type": "Match the Following",
        "q": "Match the sites with their representative funerary findings:",
        "items": [{"left": "I. Harappa", "key": "A"}, {"left": "II. Lothal", "key": "B"}, {"left": "III. Kalibangan", "key": "C"}],
        "options": [{"val": "A", "text": "A. Deodar wooden coffin burial in Cemetery R-37"}, {"val": "B", "text": "B. Twin skeletons buried together in double graves"}, {"val": "C", "text": "C. Symbolic graves containing offering pots but no bones"}],
        "sol": "Harappa has the wooden coffin, Lothal has double burials, and Kalibangan has symbolic graves."
    },
    {
        "type": "Match the Following",
        "q": "Match the ritual findings with their archaeological evidence:",
        "items": [{"left": "I. Fire Altars", "key": "A"}, {"left": "II. Grave Goods", "key": "B"}, {"left": "III. Surkotada Burials", "key": "C"}],
        "options": [{"val": "A", "text": "A. Charcoal, ash, and central clay columns in pits"}, {"val": "B", "text": "B. Earthenware pottery, copper mirrors, beads"}, {"val": "C", "text": "C. Pot burials covered with stone cairns and markers"}],
        "sol": "Fire altars have charcoal/ash; grave goods have pottery/mirrors; Surkotada has pot burials with cairns."
    },
    {
        "type": "Match the Following",
        "q": "Match the burial terms with their definitions:",
        "items": [{"left": "I. Inhumation", "key": "A"}, {"left": "II. Fractional Burial", "key": "B"}, {"left": "III. Cenotaph", "key": "C"}],
        "options": [{"val": "A", "text": "A. Complete body laid extended in a dirt grave pit"}, {"val": "B", "text": "B. Burial of bones collected after exposure in urns"}, {"val": "C", "text": "C. Memorial grave containing offerings but no skeleton"}],
        "sol": "Inhumation is complete body burial, fractional is urn burial of exposed bones, and cenotaph is symbolic grave."
    }
])

s3_mastery_hin.extend([
    {
        "type": "Match the Following",
        "q": "हड़प्पा स्थलों को उनके शवाधान साक्ष्यों से सुमेलित करें:",
        "items": [{"left": "I. हड़प्पा", "key": "A"}, {"left": "II. लोथल", "key": "B"}, {"left": "III. कालीबंगन", "key": "C"}],
        "options": [{"val": "A", "text": "A. R-37 कब्रिस्तान से देवदार की लकड़ी का ताबूत शवाधान"}, {"val": "B", "text": "B. एक ही कब्र में दो कंकालों वाले जुड़वां शवाधान"}, {"val": "C", "text": "C. कंकाल के बिना मिट्टी के बर्तनों वाली प्रतीकात्मक कब्रें"}],
        "sol": "हड़प्पा में देवदार का ताबूत था, लोथल में जुड़वां कब्र थी, और कालीबंगन में प्रतीकात्मक कब्रें थीं।"
    },
    {
        "type": "Match the Following",
        "q": "धार्मिक साक्ष्यों को उनके पुरातात्विक विवरणों से सुमेलित करें:",
        "items": [{"left": "I. अग्नि वेदियाँ", "key": "A"}, {"left": "II. कब्र सामग्री", "key": "B"}, {"left": "III. सुरकोटदा शवाधान", "key": "C"}],
        "options": [{"val": "A", "text": "A. गड्ढों में कोयला, राख और मिट्टी का मध्य खंभा होना"}, {"val": "B", "text": "B. मिट्टी के चित्रित बर्तन, तांबे के दर्पण, मनके"}, {"val": "C", "text": "C. कलश शवाधान जो पत्थर के ढेरों और खड़े पत्थर से चिह्नित हैं"}],
        "sol": "अग्नि वेदियों में कोयला/राख/खंभा था; कब्र सामग्री में बर्तन/दर्पण थे; सुरकोटदा में पत्थरों के ढेर वाले कलश शवाधान थे।"
    },
    {
        "type": "Match the Following",
        "q": "शवाधान शब्दावलियों को उनकी परिभाषाओं से सुमेलित करें:",
        "items": [{"left": "I. पूर्ण समाधिकरण", "key": "A"}, {"left": "II. आंशिक शवाधान", "key": "B"}, {"left": "III. प्रतीकात्मक कब्र", "key": "C"}],
        "options": [{"val": "A", "text": "A. पूरे शरीर को सीधा लिटाकर गड्ढे में दफनाना"}, {"val": "B", "text": "B. शव को खुला छोड़ने के बाद बची हड्डियों को कलश में दफनाना"}, {"val": "C", "text": "C. मृत व्यक्ति की स्मृति में बनी कब्र जिसमें हड्डियाँ नहीं होतीं"}],
        "sol": "पूर्ण समाधिकरण सीधा लिटाना है, आंशिक शवाधान कलश में हड्डियां दफनाना है, और प्रतीकात्मक कब्र बिना कंकाल की कब्र है।"
    }
])

# One-Liner (8)
for q, sol in [
    ("What was the standard directional orientation of Harappan graves?", "North-South, with the head to the North."),
    ("Where was the wooden coffin burial discovered?", "Harappa, Cemetery R-37."),
    ("Which site features double burials of twin skeletons?", "Lothal."),
    ("Name two sites where clay fire altars have been excavated.", "Kalibangan and Lothal."),
    ("What are symbolic burials?", "Grave pits containing offering vessels and ornaments but no human remains."),
    ("What wood was used to make the Harappan coffin?", "Deodar wood sourced from the Himalayas."),
    ("What copper object was commonly placed near the head of the dead?", "A copper mirror."),
    ("Define urn or fractional burials.", "Secondary burials where skeletal bones are collected after exposure and buried in clay jars.")
]:
    s3_mastery_eng.append({"type": "One-Liner", "q": q, "sol": sol})

for q, sol in [
    ("हड़प्पा कब्रों की मानक दिशात्मक स्थिति क्या थी?", "उत्तर-दक्षिण, जिसमें सिर उत्तर की ओर रहता था।"),
    ("ताबूत शवाधान कहाँ खोजा गया था?", "हड़प्पा के R-37 कब्रिस्तान में।"),
    ("किस स्थल पर दो कंकालों वाले जुड़वां शवाधान मिले हैं?", "लोथल में।"),
    ("उन दो स्थलों के नाम बताएं जहाँ से मिट्टी की अग्नि वेदियाँ मिली हैं।", "कालीबंगन और लोथल।"),
    ("प्रतीकात्मक शवाधान (symbolic burials) क्या हैं?", "ऐसे कब्र गड्ढे जिनमें केवल बर्तन और आभूषण रखे थे, मानव शरीर के अवशेष नहीं।"),
    ("हड़प्पा के ताबूत को बनाने के लिए किस लकड़ी का उपयोग किया गया था?", "हिमालय से मंगाई गई देवदार (deodar) की लकड़ी का।"),
    ("कब्रों में मृतकों के सिर के पास कौन सी तांबे की वस्तु रखी जाती थी?", "एक तांबे का दर्पण (mirror)।"),
    ("कलश या आंशिक शवाधान को परिभाषित करें।", "द्वितीयक शवाधान जहाँ शव के अपघटन के बाद बची हड्डियों को कलश में बंद करके दफनाया जाता था।")
]:
    s3_mastery_hin.append({"type": "One-Liner", "q": q, "sol": sol}) # Note: wait, let's keep q as question and sol as solution! Yes: "q": q, "sol": sol. Wait, look at line 836: `q` and `sol` were reversed! Let's check line 836:
# `s3_mastery_hin.append({"type": "One-Liner", "q": sol, "sol": q})` - wait! Yes, on line 836 it was `q: sol` and `sol: q`. Let's write it correctly as `q: q` and `sol: sol`. Let's fix that in our script template.

# One-Liner (8) Hindi (corrected)
# We will append properly below.

# Assertion-Reason (8)
for q, ans, sol in [
    ("Assertion (A): Harappan burials reflect a belief in life after death.\nReason (R): Graves are packed with earthenware pottery, copper mirrors, beads, and food vessels.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Lothal double burials represent the earliest mandatory practice of Sati.\nReason (R): Skeletons in double burials are always confirmed to be a married couple.", 4, "Both A and R are false: it is not confirmed to be Sati, and skeleton sexes are debated."),
    ("Assertion (A): Wooden coffin burial was a rare, non-standard practice at Harappa.\nReason (R): Only one wooden coffin made of Himalayan deodar has been excavated in Cemetery R-37.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Fire altars have been excavated at Mohenjo-daro.\nReason (R): The Great Bath was surrounded by a circle of public sacrificial pits.", 4, "Both A and R are false: no fire altars were found at Mohenjo-daro."),
    ("Assertion (A): Kalibangan symbolic burials were likely constructed for individuals who died elsewhere.\nReason (R): These graves contain no skeletal remains, only offering pottery and personal belongings.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Copper mirrors were buried near the head of the deceased.\nReason (R): Mirrors were highly valued personal items buried to accompany the owner's spirit.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Urn burials at Surkotada were covered by stone cairns.\nReason (R): Stone cairn markers indicate regional variety in Harappan funerary practices.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Standard Harappan graves were lined with high brick vaults.\nReason (R): Standard burials used simple, unlined rectangular dirt pits.", 3, "A is false because brick-lined graves are rare. R is true.")
]:
    s3_mastery_eng.append({"type": "Assertion-Reason", "q": q, "opts": ar_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("कथन (A): हड़प्पा के शवाधान मृत्यु के बाद जीवन (afterlife) में विश्वास को दर्शाते हैं।\nकारण (R): कब्रों में मिट्टी के बर्तन, तांबे के दर्पण, मनके और भोजन के पात्र रखे जाते थे।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): लोथल का जुड़वां शवाधान सती प्रथा के अनिवार्य प्रचलन का पहला उदाहरण है।\nकारण (R): जुड़वां कब्रों के कंकालों की पहचान हमेशा विवाहित दंपत्ति के रूप में की गई है।", 4, "A और R दोनों असत्य हैं: सती प्रथा का कोई स्पष्ट प्रमाण नहीं है और कंकालों का लिंग निर्धारण विवादित है।"),
    ("कथन (A): हड़प्पा में ताबूत शवाधान एक दुर्लभ और गैर-मानक प्रथा थी।\nकारण (R): R-37 कब्रिस्तान से केवल एक ही देवदार का ताबूत शवाधान मिला है।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): मोहनजोदड़ो से बड़े पैमाने पर अग्नि वेदियाँ खोजी गई हैं।\nकारण (R): विशाल स्नानागार के चारों ओर सार्वजनिक यज्ञ वेदियों के गड्ढे बने थे।", 4, "A और R दोनों असत्य हैं: मोहनजोदड़ो में अग्नि वेदियाँ नहीं मिली हैं।"),
    ("कथन (A): कालीबंगन की प्रतीकात्मक कब्रें उन लोगों के लिए बनी थीं जिनकी मृत्यु कहीं और हुई थी।\nकारण (R): इन कब्रों में मानव अवशेष नहीं मिले हैं, केवल बर्तन और व्यक्तिगत सामान मिले हैं।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): मृतकों के सिर के पास तांबे का दर्पण रखा जाता था।\nकारण (R): दर्पण मूल्यवान वस्तु थी जिसे मृत व्यक्ति की आत्मा के उपयोग के लिए साथ दफनाया जाता था।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): सुरकोटदा में कलश शवाधानों को पत्थरों के घेरे (cairns) से ढका जाता था।\nकारण (R): पत्थर के घेरे शवाधान प्रथाओं में क्षेत्रीय विविधताओं के पुरातात्विक संकेतक हैं।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): मानक हड़प्पा कब्रों को ईंटों की बड़ी गुंबददार मेहराबों से पक्का किया जाता था।\nकारण (R): मानक शवाधान के लिए साधारण, मिट्टी के आयताकार गड्ढों का उपयोग होता था।", 3, "A असत्य है क्योंकि ईंटों वाली कब्रें बहुत दुर्लभ थीं। R सत्य है।")
]:
    s3_mastery_hin.append({"type": "Assertion-Reason", "q": q, "opts": hin_ar_opts, "ans": ans, "sol": sol})

# Statement-Based (5)
for q, ans, sol in [
    ("Consider the following statements regarding extended inhumation:\n1. The body was laid straight in a rectangular pit oriented North-South.\n2. The head was pointed toward the South and the feet to the North.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect because the head pointed North (not South)."),
    ("Consider the following statements regarding coffin burials:\n1. They were common across all Mature Harappan sites, indicating a standard practice.\n2. The coffin found at Harappa was constructed from Himalayan deodar wood.\nWhich of the statements given above is/are correct?", 1, "Statement 2 is correct. Statement 1 is incorrect: coffin burials were rare and found only at Harappa R-37."),
    ("Consider the following statements regarding Lothal burials:\n1. Lothal cemeteries have yielded double burials containing two skeletons in one pit.\n2. Skeletons inside double burials are always accompanied by heavy bronze swords.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: double burials contain simple ornaments and pottery, not bronze swords."),
    ("Consider the following statements regarding fire altars:\n1. Fire altars consist of clay-lined pits containing ash, charcoal, and terracotta cakes.\n2. They have been excavated at Mohenjo-daro and Dholavira.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: fire altars have been found at Kalibangan and Lothal, not Mohenjo-daro/Dholavira."),
    ("Consider the following statements regarding symbolic burials:\n1. They contain offerings like pots and beads but completely lack human skeletons.\n2. They are widely interpreted as cenotaphs for individuals who died elsewhere.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct, describing symbolic burials and their cenotaph interpretation.")
]:
    s3_mastery_eng.append({"type": "Statement-Based", "q": q, "opts": mcq_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("पूर्ण समाधिकरण के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. शव को उत्तर-दक्षिण दिशा में उन्मुख आयताकार गड्ढे में सीधा लिटाया जाता था।\n2. सिर दक्षिण दिशा की ओर और पैर उत्तर की ओर होते थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि सिर उत्तर की ओर होता था (दक्षिण नहीं)।"),
    ("ताबूत शवाधान के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. ये सभी परिपक्व हड़प्पा स्थलों में आम थे, जो एक मानक प्रथा को दर्शाते हैं।\n2. हड़प्पा से प्राप्त ताबूत का निर्माण हिमालयी देवदार की लकड़ी से किया गया था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 1, "कथन 2 सही है। कथन 1 गलत है क्योंकि ताबूत शवाधान दुर्लभ था और केवल हड़प्पा में मिला।"),
    ("लोथल के शवाधान के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. लोथल के कब्रिस्तान से जुड़वां शवाधान मिले हैं जिनमें एक ही गड्ढे में दो कंकाल दफनाए गए थे।\n2. जुड़वां कब्रों के भीतर हमेशा भारी कांसे की तलवारें रखी होती थीं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि कब्रों में सामान्य आभूषण व बर्तन मिले हैं, तलवारें नहीं।"),
    ("अग्नि वेदियों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. अग्नि वेदियाँ मिट्टी के गड्ढे थीं जिनमें कोयला, राख और मिट्टी के केक मिले हैं।\n2. इनका उत्खनन मोहनजोदड़ो और धोलावीरा से किया गया है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि अग्नि वेदियाँ कालीबंगन और लोथल से मिली हैं, मोहनजोदड़ो/धोलावीरा से नहीं।"),
    ("प्रतीकात्मक शवाधान के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इनमें बर्तन और मनके जैसी भेंट तो होती थीं लेकिन मानव कंकाल पूरी तरह अनुपस्थित होता था।\n2. इन्हें उन लोगों का स्मारक माना जाता है जिनकी मृत्यु दूर किसी क्षेत्र में हुई थी।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 2, "दोनों कथन सही हैं, जो प्रतीकात्मक शवाधान और उनकी स्मारक व्याख्या का वर्णन करते हैं।")
]:
    s3_mastery_hin.append({"type": "Statement-Based", "q": q, "opts": hin_mcq_opts, "ans": ans, "sol": sol})

# Why (3)
for q, sol in [
    ("Why did Harappans bury pottery, mirrors, and beads with the deceased?", "To serve as grave goods that would sustain and accompany the spirit of the deceased in the afterlife, reflecting their belief in life after death."),
    ("Why was deodar wood chosen for the Harappan coffin burial in Cemetery R-37?", "Deodar is a highly durable coniferous wood resistant to decay. Sourcing it from the Himalayas shows trade networks and special ritual care given to the deceased."),
    ("Why are the fire altars of Kalibangan and Lothal interpreted as sacrificial or worship pits?", "Because they contain charcoal, ash, terracotta triangular cakes, and animal bone fragments centered around a clay column, indicating ritual fire offerings and sacrifices.")
]:
    s3_mastery_eng.append({"type": "Why", "q": q, "sol": sol})

for q, sol in [
    ("हड़प्पा वासी मृतकों के साथ बर्तन, दर्पण और मनके क्यों दफनाते थे?", "परलोक जीवन में मृत व्यक्ति की सहायता के लिए और उसकी आत्मा के उपयोग हेतु, जो मृत्यु के बाद के जीवन में उनके धार्मिक विश्वास को दर्शाता है।"),
    ("हड़प्पा के R-37 कब्रिस्तान में ताबूत बनाने के लिए देवदार की लकड़ी को क्यों चुना गया था?", "देवदार सड़न के प्रति अत्यधिक प्रतिरोधी और टिकाऊ लकड़ी होती है। इसे हिमालय से मंगाना दर्शाता है कि मृत व्यक्ति के लिए विशेष व्यापारिक और अनुष्ठानिक प्रयास किए गए थे।"),
    ("कालीबंगन और लोथल की अग्नि वेदियों को यज्ञ कुंड या बलि कुंड क्यों माना जाता है?", "क्योंकि इनमें मिट्टी के मध्य स्तंभ के चारों ओर कोयला, राख, त्रिकोणीय मिट्टी के केक और पालतू जानवरों की हड्डियों के अवशेष मिले हैं, जो अग्नि अनुष्ठान और बलि को दर्शाते हैं।")
]:
    s3_mastery_hin.append({"type": "Why", "q": q, "sol": sol})

# How (3)
for q, sol in [
    ("How was standard extended inhumation performed in Harappan cemeteries?", "Artisans dug a rectangular pit oriented North-South. The body was laid straight with the head to the North, dozens of offering pottery vessels were arranged around the head, and the grave was backfilled with soil."),
    ("How did domestic fire altars function in Kalibangan houses?", "They were clay-lined pits dug inside courtyards, centered around a clay stele, where firewood/charcoal was lit, and terracotta cakes/offerings were placed during family prayers."),
    ("How were secondary urn burials performed?", "The body was exposed to the elements, and later the remaining bones were collected and buried inside large earthenware jars along with offering bowls in circular cairn graves.")
]:
    s3_mastery_eng.append({"type": "How", "q": q, "sol": sol})

for q, sol in [
    ("हड़प्पा के कब्रिस्तानों में पूर्ण समाधिकरण की प्रक्रिया कैसे की जाती थी?", "एक आयताकार गड्ढा उत्तर-दक्षिण दिशा में खोदा जाता था। शव को सिर उत्तर की ओर करके सीधा लिटाया जाता था, सिर के पास दर्जनों मिट्टी के बर्तन रखे जाते थे, और फिर गड्ढे को मिट्टी से बंद कर दिया जाता था।"),
    ("कालीबंगन के घरों में घरेलू अग्नि वेदियाँ कैसे काम करती थीं?", "ये घर के आंगनों में बने मिट्टी के गड्ढे थे जिनमें एक केंद्रीय मिट्टी का खंभा होता था, जहाँ कोयला जलाया जाता था और पूजा के दौरान त्रिकोणीय मिट्टी के केक व भेंट चढ़ाई जाती थीं।"),
    ("द्वितीयक कलश शवाधान (urn burials) कैसे किया जाता था?", "शव को पहले खुले में छोड़ दिया जाता था, और बाद में अपघटन के बाद बची हड्डियों को इकट्ठा करके मिट्टी के कलशों में भरकर, भेंट के बर्तनों के साथ गोल पत्थरों के घेरे वाली कब्रों में दबा दिया जाता था।")
]:
    s3_mastery_hin.append({"type": "How", "q": q, "sol": sol})

# Case Study (3)
for q, sol in [
    ("Case Study: Excavations at Cemetery H and R-37 at Harappa revealed a coffin burial surrounded by standard pottery, but only one such grave was found among hundreds. What does this case study tell us about social structure?", "It tells us that while the standard burial was simple inhumation, rare high-status individuals or foreigners were given elaborate coffins, indicating social hierarchy or long-distance contact."),
    ("Case Study: Analyze the twin skeletons in Lothal's double burials. How does this case study impact the debate over Sati?", "Since the skeletons are not definitively sexed and show no signs of violent death, it remains highly contested, and most scholars interpret it as joint burials due to epidemic or family ties rather than Sati."),
    ("Case Study: A row of seven fire altars was found on a mud-brick platform in Kalibangan's Citadel. What does this setup show about the civic organization of religion?", "It shows that fire rituals were formal public ceremonies managed by the municipal authorities and performed on elevated platforms for the entire community to observe.")
]:
    s3_mastery_eng.append({"type": "Case Study", "q": q, "sol": sol})

for q, sol in [
    ("केस स्टडी: हड़प्पा के R-37 कब्रिस्तान में एक ताबूत शवाधान मिला, जो सैकड़ों कब्रों में से केवल एक था। यह सामाजिक संरचना के बारे में क्या बताता है?", "यह दर्शाता है कि यद्यपि सामान्य प्रथा साधारण समाधिकरण थी, लेकिन कुछ विशिष्ट उच्च पदस्थ व्यक्तियों या प्रवासियों को ताबूत में दफनाया गया, जो सामाजिक पदानुक्रम या बाहरी संपर्क को दर्शाता है।"),
    ("केस स्टडी: लोथल की जुड़वां कब्रों के कंकालों का विश्लेषण करें। यह सती प्रथा के विवाद को कैसे प्रभावित करता है?", "चूंकि कंकालों का लिंग निश्चित नहीं है और उन पर किसी हिंसा के निशान नहीं हैं, इसलिए सती प्रथा का दावा संदेहास्पद है; विद्वान इसे महामारी या पारिवारिक संबंधों के कारण साथ दफन मानते हैं।"),
    ("केस स्टडी: कालीबंगन के दुर्ग में मिट्टी की ईंटों के चबूतरे पर सात अग्नि वेदियों की पंक्ति मिली। यह धार्मिक नागरिक संगठन के बारे में क्या दर्शाता है?", "यह दर्शाता है कि अग्नि अनुष्ठान औपचारिक सार्वजनिक समारोह थे जो नगर अधिकारियों द्वारा आयोजित होते थे और पूरी जनता के देखने के लिए ऊंचे चबूतरों पर किए जाते थे।")
]:
    s3_mastery_hin.append({"type": "Case Study", "q": q, "sol": sol})

# Teach Concept (3)
for q, sol in [
    ("Explain the difference between primary inhumation and secondary/fractional burial to a student.", "Primary inhumation is burying the complete body immediately after death in a grave pit. Secondary or fractional burial involves exposing the body to nature first, then collecting the remaining skeletal bones and burying them inside an urn or clay jar along with offering pots."),
    ("Explain the archaeological evidence used to prove a belief in the afterlife.", "The presence of grave goods like painted pottery (for food/water), copper mirrors (personal grooming), beads, and amulets. Because these items have functional domestic uses, burying them shows the society believed the deceased's spirit would need them in the next world."),
    ("Explain the concept of regional variations in funerary customs across Harappa.", "Funerary practices were not identical: Harappa had wooden coffins, Lothal had double burials, Kalibangan had empty symbolic cenotaph graves, and Surkotada had stone-cairn pot burials. This shows that the Harappan civilization was a cultural union with diverse regional customs.")
]:
    s3_mastery_eng.append({"type": "Teach Concept", "q": q, "sol": sol})

for q, sol in [
    ("एक छात्र को पूर्ण समाधिकरण (primary) और आंशिक शवाधान (secondary) के बीच का अंतर समझाएं।", "पूर्ण समाधिकरण में मृत्यु के तुरंत बाद पूरे शरीर को कब्र में दफनाया जाता है। आंशिक शवाधान में शव को पहले खुला छोड़ दिया जाता है, और बाद में बची हुई हड्डियों को कलश में भरकर मिट्टी के बर्तनों के साथ दफनाया जाता है।"),
    ("परलोक जीवन (afterlife) में विश्वास को सिद्ध करने के लिए पुरातात्विक साक्ष्यों को समझाएं।", "कब्रों में बर्तनों (भोजन/पानी के लिए), तांबे के दर्पणों, मालाओं और ताबीजों की उपस्थिति। चूंकि ये वस्तुएं दैनिक उपयोग की हैं, इन्हें दफनाना यह दर्शाता है कि समाज का मानना था कि मृत व्यक्ति की आत्मा को अगले जन्म में इनकी आवश्यकता होगी।"),
    ("हड़प्पा में शवाधान प्रथाओं की क्षेत्रीय विविधताओं की अवधारणा को समझाएं।", "शवाधान की प्रथाएं हर जगह समान नहीं थीं: हड़प्पा में ताबूत मिले, लोथल में जुड़वां कब्रें मिलीं, कालीबंगन में बिना हड्डियों की प्रतीकात्मक कब्रें मिलीं, और सुरकोटदा में पत्थरों के ढेर वाली कब्रें। यह विविधता सांस्कृतिक संघ में क्षेत्रीय स्वायत्तता को दर्शाती है।")
]:
    s3_mastery_hin.append({"type": "Teach Concept", "q": q, "sol": sol})

print(f"Section 3 Religions Mastery questions populated: {len(s3_mastery_eng)} (Eng), {len(s3_mastery_hin)} (Hin)")


# =========================================================================
# WRITE BACK INJECTED DATA
# =========================================================================

# English injection
if os.path.exists(ENG_PATH):
    with open(ENG_PATH, "r", encoding="utf-8") as f:
        eng_data = json.load(f)
    
    eng_data["deepDive"]["sections"][0]["masteryZone"] = s1_mastery_eng
    eng_data["deepDive"]["sections"][1]["masteryZone"] = s2_mastery_eng
    eng_data["deepDive"]["sections"][2]["masteryZone"] = s3_mastery_eng
    
    with open(ENG_PATH, "w", encoding="utf-8") as f:
        json.dump(eng_data, f, ensure_ascii=False, indent=2)
    print("English mastery injected successfully!")
else:
    print(f"Error: English file not found at {ENG_PATH}")

# Hindi injection
if os.path.exists(HIN_PATH):
    with open(HIN_PATH, "r", encoding="utf-8") as f:
        hin_data = json.load(f)
    
    hin_data["deepDive"]["sections"][0]["masteryZone"] = s1_mastery_hin
    hin_data["deepDive"]["sections"][1]["masteryZone"] = s2_mastery_hin
    hin_data["deepDive"]["sections"][2]["masteryZone"] = s3_mastery_hin
    
    with open(HIN_PATH, "w", encoding="utf-8") as f:
        json.dump(hin_data, f, ensure_ascii=False, indent=2)
    print("Hindi mastery injected successfully!")
else:
    print(f"Error: Hindi file not found at {HIN_PATH}")
