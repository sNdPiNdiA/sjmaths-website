import json
import os

ENG_PATH = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\HarappanIndus-Valley-Civilisation\Domestication-of-animals\content.json"
HIN_PATH = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\HarappanIndus-Valley-Civilisation\Domestication-of-animals\hi\content.json"

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
# SECTION 1: PASTORAL ECONOMY AND DOMESTICATED ANIMALS
# =========================================================================
def make_match_question(m):
    items = []
    options = []
    roman_numerals = ["I", "II", "III", "IV", "V", "VI"]
    letters = ["A", "B", "C", "D", "E", "F"]
    for idx, pair in enumerate(m["pairs"]):
        parts = pair.split(" - ", 1)
        left_text = parts[0].strip()
        right_text = parts[1].strip()
        roman = roman_numerals[idx]
        letter = letters[idx]
        items.append({
            "left": f"{roman}. {left_text}",
            "key": letter
        })
        options.append({
            "val": letter,
            "text": f"{letter}. {right_text}"
        })
    return {
        "type": "Match the Following",
        "q": m["q"],
        "items": items,
        "options": options,
        "sol": m["sol"]
    }

s1_mastery_eng = []
s1_mastery_hin = []

# MCQ (5)
for q, opts, ans, sol in [
    ("Which of the following was the most economically dominant domesticated animal in the Harappan civilization?", ["Zebu Cattle", "Water Buffalo", "Sheep", "Goat"], 0, "Cattle (zebu) bones represent the largest percentage of faunal remains at almost all sites."),
    ("Significant remains of camel bones, indicating their domestic use for transport, have been discovered at which site?", ["Kalibangan", "Lothal", "Nageshwar", "Sutkagendor"], 0, "Kalibangan in Rajasthan has yielded significant camel bones, representing adaptation to dry environments."),
    ("The practice of burying a domestic dog alongside a human in a grave is unique to which site in the Harappan context?", ["Ropar", "Surkotada", "Dholavira", "Harappa"], 0, "Ropar (Punjab) yielded a unique co-burial of a dog with a human, showing localized ritual practices."),
    ("Which domestic animal is completely absent from Mature Harappan seals despite its economic presence?", ["Cow", "Humped Bull", "Water Buffalo", "Camel"], 0, "The humped bull is prominent on seals, but the female cow is completely absent from all seals."),
    ("A footprint of a dog chasing a cat on a wet clay brick was excavated at which manufacturing center?", ["Chanhudaro", "Mohenjo-daro", "Lothal", "Kot Diji"], 0, "Chanhudaro has yielded a brick with paw prints of a dog chasing a cat, indicating domestic pets.")
]:
    s1_mastery_eng.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("हड़प्पा सभ्यता में निम्नलिखित में से कौन सा पालतू जानवर आर्थिक रूप से सबसे प्रभावी था?", ["कूबड़ वाले बैल/गाय (Cattle)", "भैंस", "भेड़", "बकरी"], 0, "मवेशी (गाय-बैल) की हड्डियाँ लगभग सभी स्थलों पर प्राणि-अवशेषों में सबसे अधिक प्रतिशत में मिली हैं।"),
    ("परिवहन के लिए ऊंट के घरेलू उपयोग को दर्शाने वाले अस्थि अवशेष मुख्य रूप से किस स्थल से प्राप्त हुए हैं?", ["कालीबंगन", "लोथल", "नागेश्वर", "सुत्कागेंदोर"], 0, "राजस्थान के कालीबंगन से ऊंट की हड्डियाँ मिली हैं, जो शुष्क मरुस्थलीय मार्ग पर परिवहन को दर्शाती हैं।"),
    ("हड़प्पा संदर्भ में कब्र में मनुष्य के साथ पालतू कुत्ते को दफनाने की अनूठी प्रथा किस स्थल पर पाई गई है?", ["रोपण", "सुरकोटदा", "धोलावीरा", "हड़प्पा"], 0, "पंजाब के रोपण से मनुष्य के साथ कुत्ते को दफनाए जाने के साक्ष्य मिले हैं।"),
    ("कौन सा आर्थिक रूप से महत्वपूर्ण पालतू जानवर हड़प्पा मुहरों पर पूरी तरह से अनुपस्थित है?", ["गाय", "कूबड़ वाला बैल", "भैंस", "ऊंट"], 0, "मुहरों पर कूबड़ वाले बैल का अंकन मिलता है, लेकिन मादा गाय का चित्रण बिल्कुल नहीं मिलता।"),
    ("गीली ईंट पर बिल्ली का पीछा करते हुए कुत्ते के पंजों के निशान किस शिल्प निर्माण केंद्र से प्राप्त हुए हैं?", ["चन्हुदड़ो", "मोहनजोदड़ो", "लोथल", "कोट दीजी"], 0, "चन्हुदड़ो से पंजों के निशान वाली ईंट मिली है, जो घरों में इन पालतू जानवरों की उपस्थिति को दर्शाती है।")
]:
    s1_mastery_hin.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# Multiple Correct MCQ (5)
for q, opts, ans, sol in [
    ("Which of the following animals were domesticated by the Harappans for traction and burden? (Select all that apply)", ["Humped Bull (Zebu)", "Water Buffalo", "Domestic Ass", "African Elephant"], [0, 1, 2], "Zebu, buffalo, and ass were domesticated and used for work. African elephants were not domesticated."),
    ("Select the ruminants reared by Harappans for wool, milk, and meat: (Select all that apply)", ["Sheep", "Goat", "Pig", "Dog"], [0, 1], "Sheep and goats were reared for wool, milk, and meat. Pigs were kept for meat but not wool. Dogs were pets."),
    ("Which of the following animals are NEVER depicted on Harappan seals? (Select all that apply)", ["Cow", "Horse", "Camel", "Rhinoceros"], [0, 1, 2], "Cow, horse, and camel are never depicted on Harappan seals. Rhinoceros is depicted."),
    ("Choose the sites that have yielded camel bones or teeth remains: (Select all that apply)", ["Kalibangan", "Harappa", "Mohenjo-daro", "Nageshwar"], [0, 1, 2], "Camels were used in plains and dry regions, with bones found at Kalibangan, Harappa, and Mohenjo-daro."),
    ("Select the domestic pets whose skeletal or footprint remains have been verified in urban Harappan contexts: (Select all that apply)", ["Dogs", "Cats", "Mongoose", "Lions"], [0, 1], "Dogs and cats are well-documented. Mongoose and lions were not domestic pets.")
]:
    s1_mastery_eng.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("हड़प्पा वासियों द्वारा कृषि श्रम और भार ढोने के लिए किन पशुओं को पाला जाता था? (सभी सही विकल्प चुनें)", ["कूबड़ वाले बैल", "भैंस", "घरेलू गधा", "अफ्रीकी हाथी"], [0, 1, 2], "बैल, भैंस और गधे पालतू श्रम पशु थे। अफ्रीकी हाथी पालतू नहीं थे।"),
    ("हड़प्पा वासियों द्वारा ऊन, दूध और मांस के लिए पाले जाने वाले जुगाली करने वाले पशुओं को चुनें: (सभी सही विकल्प चुनें)", ["भेड़", "बकरी", "सूअर", "कुत्ता"], [0, 1], "भेड़ और बकरियों को ऊन, दूध और मांस के लिए पाला जाता था। सूअर ऊन नहीं देते।"),
    ("निम्नलिखित में से कौन से जानवर हड़प्पा मुहरों पर कभी चित्रित नहीं किए गए? (सभी सही विकल्प चुनें)", ["गाय", "घोड़ा", "ऊंट", "गैंडा"], [0, 1, 2], "गाय, घोड़ा और ऊंट मुहरों पर कभी नहीं चित्रित किए गए। गैंडा चित्रित मिलता है।"),
    ("उन स्थलों को चुनें जहाँ से ऊंट की हड्डियाँ या दांत मिले हैं: (सभी सही विकल्प चुनें)", ["कालीबंगन", "हड़प्पा", "मोहनजोदड़ो", "नागेश्वर"], [0, 1, 2], "ऊंटों की हड्डियाँ शुष्क एवं मैदानी केंद्रों (कालीबंगन, हड़प्पा, मोहनजोदड़ो) से मिली हैं।"),
    ("उन पालतू जानवरों को चुनें जिनके साक्ष्य हड़प्पा शहरी संदर्भों में प्रमाणित हुए हैं: (सभी सही विकल्प चुनें)", ["कुत्ता", "बिल्ली", "नेवला", "शेर"], [0, 1], "कुत्ते और बिल्ली घरेलू पालतू जानवरों के रूप में प्रमाणित हैं।")
]:
    s1_mastery_hin.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# True/False (8)
for q, ans, sol in [
    ("The cow is the most common animal represented on Mature Harappan seals.", False, "The cow is completely absent from seal iconography."),
    ("The humped bull or zebu is scientifically classified as Bos indicus.", True, "Zebu cattle belong to the species Bos indicus."),
    ("Bones of domestic pigs are completely absent from Harappan urban garbage dumps.", False, "Pig bones are common, indicating they were consumed for meat."),
    ("Camel remains are documented at the site of Kalibangan.", True, "Significant camel bones have been found at Kalibangan."),
    ("Domestic asses (donkeys) were utilized as beasts of burden for transport.", True, "Asses were used for transporting goods in flat plains and rocky areas."),
    ("Cattle bones constitute the largest percentage of animal bones recovered at Harappan sites.", True, "Mains of cattle make up 50-60% of all recovered bones."),
    ("The domestic cat is not represented by any physical evidence in Harappa.", False, "Paw prints on bricks at Chanhudaro prove the presence of cats."),
    ("Dogs were kept as domestic pets and toys show them with collars.", True, "Terracotta dog figurines with collars indicate their pet status.")
]:
    s1_mastery_eng.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("गाय परिपक्व हड़प्पा मुहरों पर सबसे अधिक दर्शाया जाने वाला पशु है।", False, "गाय मुहरों पर पूरी तरह से अनुपस्थित है।"),
    ("कूबड़ वाले बैल या जेबू को वैज्ञानिक रूप से 'बॉस इंडिकस' (Bos indicus) के रूप में वर्गीकृत किया गया है।", True, "जेबू मवेशी बॉस इंडिकस प्रजाति के हैं।"),
    ("हड़प्पा के शहरी कचरा स्थलों से पालतू सूअरों की हड्डियाँ पूरी तरह से गायब हैं।", False, "सूअर की हड्डियाँ काफी मात्रा में मिली हैं, जो मांस सेवन को दर्शाती हैं।"),
    ("ऊंट के अवशेष कालीबंगन स्थल से दर्ज किए गए हैं।", True, "कालीबंगन से ऊंट की हड्डियाँ प्राप्त हुई हैं।"),
    ("भार ढोने और परिवहन के लिए घरेलू गधों का उपयोग किया जाता था।", True, "गधों का उपयोग मैदानी इलाकों में माल ढोने के लिए किया जाता था।"),
    ("हड़प्पा स्थलों से प्राप्त कुल हड्डियों में मवेशियों (गाय-बैल) की हड्डियाँ सर्वाधिक हैं।", True, "मवेशियों की हड्डियाँ कुल प्राणि-अवशेषों का 50% से अधिक हैं।"),
    ("हड़प्पा में पालतू बिल्ली का कोई भौतिक साक्ष्य नहीं मिला है।", False, "चन्हुदड़ो में ईंट पर बिल्ली के पंजों के निशान मिले हैं।"),
    ("कुत्तों को पालतू जानवर के रूप में रखा जाता था और खिलौनों में उन्हें गले में पट्टा पहने दिखाया गया है।", True, "पट्टे वाले खिलौना कुत्ते उनके पालतू होने की पुष्टि करते हैं।")
]:
    s1_mastery_hin.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

# Fill in the Blank (8)
for q, ans, sol in [
    ("The scientific name for the humped cattle of the Indus Valley is ________.", "Bos indicus", "Bos indicus is the biological name for the humped zebu cattle."),
    ("A unique burial of a domestic dog alongside a human skeleton was excavated at ________.", "Ropar", "Ropar in Punjab yielded this unique co-burial pattern."),
    ("The female domestic animal never represented on seals is the ________.", "cow", "The cow is completely missing from seals."),
    ("Bones of the ________ found at Kalibangan confirm its use in desert transport.", "camel", "Camels were adapted for transport in dry regions."),
    ("A wet clay brick with paw prints of a dog chasing a cat was found at ________.", "Chanhudaro", "Chanhudaro has yielded this unique animal print brick."),
    ("Harappans sheared sheep to obtain ________ for textile production.", "wool", "Sheep were kept to mature ages to harvest wool."),
    ("The heavy wooden wheeled carts of the Harappans were pulled by humped ________.", "oxen", "Oxen/bulls were the primary draft animals for cart traction."),
    ("Domesticated pigs are scientifically classified as ________.", "Sus scrofa", "Sus scrofa is the scientific name for pigs.")
]:
    s1_mastery_eng.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("सिंधु घाटी के कूबड़ वाले मवेशियों का वैज्ञानिक नाम ________ है।", "बॉस इंडिकस", "बॉस इंडिकस कूबड़ वाले बैल/गाय का वैज्ञानिक नाम है।"),
    ("मनुष्य के कंकाल के साथ पालतू कुत्ते को दफनाने की अनूठी समाधि ________ से मिली है।", "रोपण", "पंजाब के रोपण से यह सह-समाधि मिली है।"),
    ("मुहरों पर कभी न दर्शाया जाने वाला मादा पालतू पशु ________ है।", "गाय", "गाय मुहरों पर पूरी तरह गायब है।"),
    ("कालीबंगन से प्राप्त ________ की हड्डियाँ मरुस्थलीय मार्ग पर उसके उपयोग की पुष्टि करती हैं।", "ऊंट", "ऊंट का उपयोग रेगिस्तानी शुष्क इलाकों में होता था।"),
    ("बिल्ली का पीछा करते कुत्ते के पंजों के निशान वाली ईंट ________ से प्राप्त हुई है।", "चन्हुदड़ो", "चन्हुदड़ो से पंजों के निशान वाली पकी ईंट मिली है।"),
    ("वस्त्र उत्पादन के लिए भेड़ से ________ प्राप्त किया जाता था।", "ऊन", "भेड़ों को ऊन प्राप्त करने के लिए पाला जाता था।"),
    ("हड़प्पा की ठोस पहियों वाली गाड़ियों को कूबड़ वाले ________ खींचते थे।", "बैल", "बैल/सांड गाड़ियों को खींचने के काम आते थे।"),
    ("पालतू सूअरों को वैज्ञानिक रूप से ________ के रूप में वर्गीकृत किया गया है।", "सस स्क्रूफा", "सस स्क्रूफा सूअर का वैज्ञानिक नाम है।")
]:
    s1_mastery_hin.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

# Match the Following (3)
s1_matches_eng = [
    {"q": "Match the animal with its primary economic/archaeological significance:",
     "pairs": ["Zebu Bull - Prominent seal motif and cart traction", "Camel - Desert transport at Kalibangan", "Dog - Human co-burial at Ropar", "Cat - Chanhudaro footprint brick"],
     "sol": "Zebu represents seal art and labor; camel represents desert trade at Kalibangan; dog is found in Ropar graves; cat is documented at Chanhudaro."},
    {"q": "Match the domesticate with its scientific classification:",
     "pairs": ["Humped Cattle - Bos indicus", "Water Buffalo - Bubalus bubalis", "Pig - Sus scrofa", "Goat - Capra hircus"],
     "sol": "Matches animal species with their established zooarchaeological names."},
    {"q": "Match the animal finding with the corresponding site:",
     "pairs": ["Ropar - Human and dog co-grave", "Kalibangan - Heavy concentrations of camel bones", "Chanhudaro - Brick print showing cat chase", "Lothal - Terracotta figurine of a horse/ass"],
     "sol": "Links specific sites with their diagnostic faunal artifacts."}
]
s1_mastery_eng.extend([make_match_question(m) for m in s1_matches_eng])

s1_matches_hin = [
    {"q": "पशु को उसके प्राथमिक आर्थिक/पुरातात्विक महत्व से सुमेलित करें:",
     "pairs": ["कूबड़ वाला बैल - मुहरों पर प्रमुख अंकन और श्रम", "ऊंट - कालीबंगन में मरुस्थलीय परिवहन", "कुत्ता - रोपण में मानव के साथ सह-समाधि", "बिल्ली - चन्हुदड़ो में पंजों के निशान वाली ईंट"],
     "sol": "बैल मुहरों और श्रम का प्रतीक है; ऊंट रेगिस्तानी व्यापार से जुड़ा है; कुत्ता रोपण की कब्रों में मिला है; बिल्ली चन्हुदड़ो की ईंट पर दर्ज है।"},
    {"q": "पालतू पशु को उसके वैज्ञानिक वर्गीकरण से सुमेलित करें:",
     "pairs": ["कूबड़ वाले मवेशी - बॉस इंडिकस (Bos indicus)", "भैंस - बुबालस बुबालिस (Bubalus bubalis)", "सूअर - सस स्क्रूफा (Sus scrofa)", "बकरी - कैपरा हिर्कस (Capra hircus)"],
     "sol": "पशुओं को उनके स्थापित वैज्ञानिक नामों से सुमेलित करता है।"},
    {"q": "पशु अवशेषों को संबंधित पुरातात्विक स्थल से सुमेलित करें:",
     "pairs": ["रोपण - मनुष्य और कुत्ते की सह-समाधि", "कालीबंगन - ऊंट की हड्डियों के अवशेष", "चन्हुदड़ो - बिल्ली का पीछा करते कुत्ते के पैरों के निशान", "लोथल - घोड़े/गधे की मिट्टी की खिलौना मूर्ति"],
     "sol": "विशिष्ट स्थलों को उनके महत्वपूर्ण पशु साक्ष्यों से जोड़ता है।"}
]
s1_mastery_hin.extend([make_match_question(m) for m in s1_matches_hin])

# One-Liner (8)
for q, sol in [
    ("What was the primary function of the humped bull (zebu) in Harappan farming?", "It was used as a draft animal to pull heavy wooden ploughs and transport carts."),
    ("Which domestic pet's presence is verified by a baked brick at Chanhudaro?", "The domestic cat, verified by its paw prints while being chased by a dog."),
    ("Why is the absence of cow representations on seals considered historically significant?", "It shows that Harappan administrative iconography followed distinct stylistic rules, choosing the bull over the cow, unlike later Vedic focus on cows."),
    ("What were sheep and goats reared for in Mature Harappan cities?", "They were reared for wool production, milk, and as a major source of meat protein."),
    ("Which site features a human grave with a domestic dog buried beneath the body?", "Ropar in Punjab."),
    ("Which beast of burden was adapted to dry regions of Rajasthan?", "The camel, documented by bones at Kalibangan."),
    ("How did pigs contribute to the economy of urban waste management?", "Pigs were reared in urban dump yards, feeding on organic waste and providing cheap meat."),
    ("What animal bone category represents the highest percentage of remains at most sites?", "Cattle (cows and bulls) bones, constituting 50-60% of all recovered remains.")
]:
    s1_mastery_eng.append({"type": "One-Liner", "q": q, "sol": sol})

for q, sol in [
    ("हड़प्पा कृषि में कूबड़ वाले बैल (zebu) का मुख्य कार्य क्या था?", "इसका उपयोग लकड़ी के भारी हलों को खींचने और ठोस पहियों वाली गाड़ियों को ढोने के लिए किया जाता था।"),
    ("चन्हुदड़ो से प्राप्त पकी ईंट किस पालतू जानवर की उपस्थिति प्रमाणित करती है?", "पालतू बिल्ली की, जिसके पंजों के निशान कुत्ते द्वारा पीछा किए जाने के रूप में अंकित हैं।"),
    ("मुहरों पर गाय के चित्रण की अनुपस्थिति को ऐतिहासिक रूप से क्यों महत्वपूर्ण माना जाता है?", "यह दर्शाता है कि हड़प्पा की प्रशासनिक कला में गाय के बजाय कूबड़ वाले बैल को प्रतीक के रूप में वरीयता दी जाती थी, जो वैदिक काल से अलग है।"),
    ("परिपक्व हड़प्पा शहरों में भेड़ और बकरियों को किसलिए पाला जाता था?", "उन्हें वस्त्र उत्पादन के लिए ऊन, दूध और मांस के लिए पाला जाता था।"),
    ("किस स्थल पर एक मानव कब्र में शरीर के नीचे पालतू कुत्ते को दफनाने के साक्ष्य मिले हैं?", "पंजाब के रोपण (Ropar) में।"),
    ("राजस्थान के शुष्क क्षेत्रों में सामान ढोने के लिए किस जानवर का उपयोग होता था?", "ऊंट का, जिसके अवशेष कालीबंगन से मिले हैं।"),
    ("शहरी कचरा प्रबंधन में सूअरों का क्या योगदान था?", "वे कचरा क्षेत्रों में जैविक कचरा खाते थे और बदले में शहरों के लिए सस्ता मांस प्रदान करते थे।"),
    ("अधिकांश स्थलों पर किस पशु वर्ग की हड्डियाँ सबसे अधिक मिली हैं?", "मवेशी (गाय और बैल) की हड्डियाँ, जो कुल अवशेषों का 50% से अधिक हैं।")
]:
    s1_mastery_hin.append({"type": "One-Liner", "q": q, "sol": sol})

# Assertion-Reason (8)
for q, ans, sol in [
    ("Assertion (A): The humped bull is realistically rendered in Mature Harappan steatite seals.\nReason (R): The humped bull served as a primary draft animal for pulling ploughs and grain carts.", 1, "Both A and R are true, but R is the economic utility which does not directly explain why it was chosen as a symbolic seal motif rather than a religious icon."),
    ("Assertion (A): The female cow is completely absent from Harappan seal iconography.\nReason (R): The cow was unknown to the Harappans who only domesticated male zebu bulls.", 2, "A is true; R is false because cows existed (otherwise bulls could not be bred) and were domesticated for dairy."),
    ("Assertion (A): Camels were used for transport in the dry zones of Kutch and Rajasthan.\nReason (R): Camel bones have been excavated from Mature Harappan layers at Kalibangan.", 0, "Both A and R are true, and the bone remains at Kalibangan prove their presence and utility in the dry zone."),
    ("Assertion (A): Donkeys (domestic asses) played a key role in short-distance overland trade.\nReason (R): Donkeys are sturdy pack animals well-suited for rocky and semi-arid terrain.", 0, "Both A and R are true, explaining their role as beasts of burden in trade routes."),
    ("Assertion (A): Dogs were kept as household pets and guards in Harappan cities.\nReason (R): Terracotta figurines representing dogs have been excavated showing collar bands.", 0, "Both A and R are true, and the collar bands on clay models verify their status as domesticated pets."),
    ("Assertion (A): Pig bones are commonly found in refuse heaps near residential sectors.\nReason (R): Pigs were reared in urban dump yards to consume organic waste and provide meat.", 0, "Both A and R are true, and their waste-consumption role explains why they were raised near residential dump sectors."),
    ("Assertion (A): Animal domestication was secondary to agriculture in terms of food security.\nReason (R): Crop cultivation provided the primary calorie base, while livestock provided traction and secondary proteins.", 0, "Both A and R are true, and the dietary calorie breakdown explains the relationship between farming and animal keeping."),
    ("Assertion (A): Sheep and goats were reared together by pastoral groups.\nReason (R): Sheep and goats provide complementary resources such as wool, milk, and meat.", 0, "Both A and R are true, and the complementary resources explain why mixed herds were preferred.")
]:
    s1_mastery_eng.append({"type": "Assertion-Reason", "q": q, "opts": ar_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("कथन (A): हड़प्पा मुहरों पर कूबड़ वाले बैल का बहुत ही सजीव चित्रण मिलता है।\nकारण (R): कूबड़ वाला बैल हल और बैलगाड़ी खींचने वाला मुख्य श्रम पशु था।", 1, "कथन A और R दोनों सही हैं, लेकिन R, कथन A की सही व्याख्या नहीं है क्योंकि कला में चित्रण प्रशासनिक/धार्मिक कारणों से था, केवल कृषि उपयोग के कारण नहीं।"),
    ("कथन (A): हड़प्पा मुहरों पर मादा गाय का चित्रण पूरी तरह से अनुपस्थित है।\nकारण (R): हड़प्पा वासियों को गाय का कोई ज्ञान नहीं था और वे केवल कूबड़ वाले सांड पालते थे।", 2, "A सही है लेकिन R गलत है क्योंकि गायें मौजूद थीं, तभी बैलों का प्रजनन संभव था।"),
    ("कथन (A): कच्छ और राजस्थान के शुष्क क्षेत्रों में ऊंटों का उपयोग परिवहन के लिए किया जाता था।\nकारण (R): कालीबंगन के परिपक्व हड़प्पा स्तरों से ऊंट की हड्डियाँ खोदी गई हैं।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या है क्योंकि हड्डियाँ उनके उपयोग को सिद्ध करती हैं।"),
    ("कथन (A): कम दूरी के थलीय व्यापार में गधों ने महत्वपूर्ण भूमिका निभाई।\nकारण (R): गधे पहाड़ी और अर्ध-शुष्क पथरीले रास्तों पर सामान ढोने के लिए उपयुक्त पशु हैं।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या है।"),
    ("कथन (A): हड़प्पा शहरों में कुत्तों को पालतू पशु और रक्षक के रूप में पाला जाता था।\nकारण (R): कुत्तों के कई मिट्टी के खिलौने मिले हैं जिनके गले में पट्टा (collar band) बना है।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या है क्योंकि पट्टा उनके पालतू होने की पुष्टि करता है।"),
    ("कथन (A): आवासीय क्षेत्रों के कचरे के ढेरों में सूअरों की हड्डियाँ आम तौर पर मिलती हैं।\nकारण (R): सूअर कचरा क्षेत्रों में जैविक कचरा खाते थे और सस्ता मांस प्रदान करते थे।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या है।"),
    ("कथन (A): खाद्य सुरक्षा के मामले में पशुपालन कृषि की तुलना में सहायक (द्वितीयक) था।\nकारण (R): फसलें मुख्य कैलोरी आधार प्रदान करती थीं, जबकि पशु केवल श्रम और प्रोटीन पूरक थे।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या है।"),
    ("कथन (A): खानाबदोश चरवाहों द्वारा भेड़ और बकरियों को एक साथ पाला जाता था।\nकारण (R): भेड़ और बकरियां क्रमशः ऊन, दूध और मांस जैसे पूरक उत्पाद प्रदान करती थीं।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या है।")
]:
    s1_mastery_hin.append({"type": "Assertion-Reason", "q": q, "opts": hin_ar_opts, "ans": ans, "sol": sol})

# Statement-Based (5)
for q, ans, sol in [
    ("Consider the following statements:\nStatement 1: Cattle bones, representing the humped zebu, are the most dominant faunal remains in the Indus Valley.\nStatement 2: The scientific name for humped zebu cattle is Equus caballus.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: Equus caballus is the true horse, whereas zebu is Bos indicus."),
    ("Consider the following statements:\nStatement 1: Humped bulls are depicted on administrative seals to represent authority.\nStatement 2: The female cow is the second most common animal represented on seals.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: The cow is never represented on seals."),
    ("Consider the following statements:\nStatement 1: Camel bones are documented at Kalibangan in Rajasthan.\nStatement 2: Camels were the primary source of traction for pulling wooden ploughshares in Punjab.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: Oxen (bulls) were the primary source of plough traction, not camels."),
    ("Consider the following statements:\nStatement 1: Ropar yielded a human burial containing a dog buried with the deceased.\nStatement 2: Dog skeletons are found in every single Harappan cemetery.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: This practice is unique to Ropar and not found elsewhere in Harappan graves."),
    ("Consider the following statements:\nStatement 1: Sheep and goats were kept for both dairy products and wool fibers.\nStatement 2: Domesticated pigs were kept exclusively at coastal fishing outposts.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: Pigs were raised in all major urban garbage dumps, not just coastal outposts.")
]:
    s1_mastery_eng.append({"type": "Statement-Based", "q": q, "opts": mcq_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: सिंधु घाटी में प्राणि-अवशेषों में कूबड़ वाले बैल (zebu) की हड्डियाँ सर्वाधिक हैं।\nकथन 2: कूबड़ वाले बैल का वैज्ञानिक नाम 'इक्वस कैबेलस' (Equus caballus) है।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि इक्वस कैबेलस घोड़े का नाम है, बैल का नाम बॉस इंडिकस है।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: मुहरों पर सत्ता और अधिकार को दर्शाने के लिए कूबड़ वाले बैल का चित्रण मिलता है।\nकथन 2: मुहरों पर दर्शाया जाने वाला दूसरा सबसे आम जानवर गाय है।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि गाय मुहरों पर कभी नहीं दर्शाई गई है।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: राजस्थान के कालीबंगन से ऊंट की हड्डियाँ दर्ज की गई हैं।\nकथन 2: पंजाब में लकड़ी के हलों को खींचने के लिए ऊंटों का मुख्य रूप से उपयोग किया जाता था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि हल बैल खींचते थे, ऊंट नहीं।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: रोपण से एक कब्र मिली है जहाँ मनुष्य के साथ कुत्ते को दफनाया गया था।\nकथन 2: हड़प्पा सभ्यता के हर कब्रिस्तान में कुत्ते के कंकाल मिले हैं।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि कुत्ते की समाधि केवल रोपण में मिली है, अन्य कब्रिस्तानों में नहीं।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: भेड़ और बकरियों को डेयरी उत्पादों और ऊनी रेशों दोनों के लिए पाला जाता था।\nकथन 2: पालतू सूअरों को विशेष रूप से केवल तटीय मछली पकड़ने वाली चौकियों पर पाला जाता था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि सूअर मुख्य बड़े शहरों के कचरा क्षेत्रों में पाले जाते थे।")
]:
    s1_mastery_hin.append({"type": "Statement-Based", "q": q, "opts": hin_mcq_opts, "ans": ans, "sol": sol})

# Why (3)
for q, sol in [
    ("Why is the humped bull depicted so realistically on Harappan seals while other animals are stylized?", "The humped bull held high symbolic, economic, and potentially sacred value as a draft animal, representing physical power and agricultural fertility."),
    ("Why did the Harappans avoid depicting the cow on seals despite its economic importance?", "The cow's absence was likely due to specific artistic/symbolic conventions or taboos that reserved seal iconography for powerful wild animals, mythical creatures, and draft bulls."),
    ("Why were donkeys and camels essential for the Harappan regional trade network?", "They were adapted for overland travel in arid and rocky regions (like Baluchistan and Rajasthan) where wheeled bullock carts were inefficient.")
]:
    s1_mastery_eng.append({"type": "Why", "q": q, "sol": sol})

for q, sol in [
    ("हड़प्पा मुहरों पर अन्य जानवरों की तुलना में कूबड़ वाले बैल का इतना सजीव चित्रण क्यों मिलता है?", "कूबड़ वाला बैल उच्च आर्थिक और शक्ति का प्रतीक था, जो कृषि जुताई और भारी गाड़ियों को खींचता था, इसलिए इसे कला में प्राथमिकता दी गई।"),
    ("आर्थिक महत्व होने के बावजूद हड़प्पा मुहरों पर गाय का चित्रण क्यों नहीं किया जाता था?", "यह विशिष्ट कलात्मक और प्रशासनिक नियमों या धार्मिक प्रतिबंधों के कारण था, जिसने मुहरों के अंकन को बैल और काल्पनिक जीवों तक सीमित रखा।"),
    ("हड़प्पा के क्षेत्रीय व्यापारिक नेटवर्क के लिए गधे और ऊंट क्यों आवश्यक थे?", "वे बलूचिस्तान और राजस्थान जैसे पहाड़ी और रेगिस्तानी रास्तों पर माल ले जाने के लिए उपयुक्त थे, जहाँ बैलगाड़ियों का चलना कठिन था।")
]:
    s1_mastery_hin.append({"type": "Why", "q": q, "sol": sol})

# How (3)
for q, sol in [
    ("How did cattle traction transform Harappan agricultural productivity?", "By enabling the use of heavy wooden ploughshares to deep-cultivate hard alluvial clays and transport huge agrarian surpluses in wheeled carts to cities."),
    ("How do the dog-human co-burials at Ropar help reconstruct Harappan domestic relations?", "They suggest close emotional bonds between owners and dogs, and indicate localized beliefs in the afterlife where pets accompanied owners."),
    ("How did pastoral nomads interact with settled urban populations in the Indus Valley?", "They migrated seasonally, supplying cities with milk, wool, leather, and draft animals in exchange for agricultural grains and metal tools.")
]:
    s1_mastery_eng.append({"type": "How", "q": q, "sol": sol})

for q, sol in [
    ("मवेशियों के श्रम ने हड़प्पा की कृषि उत्पादकता को कैसे बदल दिया?", "इससे जलोढ़ मिट्टी की गहरी जुताई के लिए भारी लकड़ी के हलों का चलना आसान हुआ और अनाज के बड़े अधिशेष को बैलगाड़ियों से शहरों तक ले जाना संभव हुआ।"),
    ("रोपण में मिली मनुष्य और कुत्ते की सह-समाधि हड़प्पा के घरेलू संबंधों को समझने में कैसे मदद करती है?", "यह इंसानों और उनके पालतू जानवरों के बीच गहरे जुड़ाव को दर्शाती है, और परलोक जीवन से जुड़ी स्थानीय मान्यताओं की ओर संकेत करती है।"),
    ("चरवाहा खानाबदोश सिंधु घाटी की settled शहरी आबादी के साथ कैसे बातचीत करते थे?", "वे मौसमी रूप से प्रवास करते थे, और शहरों को दूध, चमड़ा, ऊन और बैल प्रदान करते थे, जिसके बदले वे अनाज और धातु के बर्तन लेते थे।")
]:
    s1_mastery_hin.append({"type": "How", "q": q, "sol": sol})

# Case Study (3)
for q, sol in [
    ("Analyze Kalibangan's camel bone assemblage and its implications for overland trade.", "Significant camel bones at Kalibangan indicate the animal was integrated into the local economy of northern Rajasthan, facilitating trade across the desert Thar zone."),
    ("Evaluate the Chanhudaro dog-and-cat brick paw prints as a source of domestic life history.", "The overlapping prints on a wet, unbaked clay brick suggest that dogs and cats freely roamed the streets and workshops of Chanhudaro before the brick was placed in a kiln."),
    ("Examine Ropar's domestic pet burial and its significance in Neolithic-Harappan transitions.", "The dog-human co-burial at Ropar reflects localized Neolithic cultural legacies that persisted into the Harappan phase, distinct from mainstream urban burial rites.")
]:
    s1_mastery_eng.append({"type": "Case Study", "q": q, "sol": sol})

for q, sol in [
    ("कालीबंगन से प्राप्त ऊंट की हड्डियों के साक्ष्य और इसके व्यापारिक निहितार्थों का विश्लेषण करें।", "कालीबंगन में मिली ऊंट की हड्डियाँ यह दर्शाती हैं कि थार मरुस्थल के समीप इस उत्तरी राजस्थान क्षेत्र में ऊंटों का उपयोग थलीय व्यापारिक कारवां के लिए किया जाता था।"),
    ("घरेलू जीवन के इतिहास के स्रोत के रूप में चन्हुदड़ो से प्राप्त पंजों के निशान वाली ईंट का मूल्यांकन करें।", "गीली ईंट पर बिल्ली का पीछा करते कुत्ते के पंजों का निशान यह साबित करता है कि ये जानवर शिल्प कार्यशालाओं के आस-पास घूमते थे और उनके बीच आज की तरह ही संबंध थे।"),
    ("रोपण में मिली पालतू कुत्ते की समाधि और नवपाषाण-हड़प्पा संक्रमण में इसके महत्व की जांच करें।", "मनुष्य के साथ कुत्ते को दफनाने की यह प्रथा स्थानीय नवपाषाण (Neolithic) परंपराओं के प्रभाव को दर्शाती है, जो मुख्यधारा के हड़प्पा शहरों से अलग थी।")
]:
    s1_mastery_hin.append({"type": "Case Study", "q": q, "sol": sol})

# Teach Concept (3)
for q, sol in [
    ("Explain the concept of 'Secondary Products Revolution' in the context of Harappan cattle husbandry.", "The use of cattle not just for meat (primary), but for secondary resources like milk, butter, and traction power (ploughing, carts) which multiplied agricultural output."),
    ("Describe the mechanism of seasonal transhumance among Harappan pastoralists in Gujarat.", "Pastoral groups moved herds between wet upland pastures during dry monsoons and dry lowland areas when water was available, trading along the route."),
    ("Explain the domestic waste cycle involving pigs in Harappan urban centers.", "Pigs acted as organic waste consumers in dump yards, helping clean cities of refuse, while providing a cheap protein source for lower-status urban populations.")
]:
    s1_mastery_eng.append({"type": "Teach Concept", "q": q, "sol": sol})

for q, sol in [
    ("हड़प्पा मवेशी पालन के संदर्भ में 'द्वितीयक उत्पाद क्रांति' (Secondary Products Revolution) की अवधारणा को समझाएं।", "इसका अर्थ मवेशियों का उपयोग केवल मांस (प्राथमिक) के लिए नहीं, बल्कि दूध, मक्खन और श्रम (द्वितीयक) के लिए करना है, जिसने कृषि उत्पादकता को कई गुना बढ़ा दिया।"),
    ("गुजरात के हड़प्पा पशुपालकों के बीच मौसमी ऋतुप्रवास (transhumance) की प्रणाली का वर्णन करें।", "चरवाहे शुष्क मौसम में चारे की तलाश में मवेशियों को लेकर आर्द्र पहाड़ी चरागाहों की ओर चले जाते थे और बरसात में मैदानों में लौट आते थे, जिससे दोनों क्षेत्रों में व्यापार होता था।"),
    ("हड़प्पा शहरी केंद्रों में सूअरों से जुड़े घरेलू कचरा चक्र की व्याख्या करें।", "सूअर शहरों के कचरा क्षेत्रों में फेंक दिए गए जैविक कचरे को खाते थे, जिससे शहर साफ रहते थे, और साथ ही वे शहरी आबादी के लिए मांस का एक प्रमुख स्रोत बनते थे।")
]:
    s1_mastery_hin.append({"type": "Teach Concept", "q": q, "sol": sol})


# =========================================================================
# SECTION 2: WILD ANIMALS, HUNTING, AND FISHING
# =========================================================================
s2_mastery_eng = []
s2_mastery_hin = []

# MCQ (5)
for q, opts, ans, sol in [
    ("Which of the following wild felines is frequently represented on Harappan seals, whereas the lion is absent?", ["Tiger", "Leopard", "Cheetah", "Jaguar"], 0, "The tiger is frequently depicted on seals, whereas the lion is absent or extremely rare in Mature Harappan art."),
    ("Copper/bronze fish hooks have been excavated in large numbers at which major riverine and coastal sites?", ["Mohenjo-daro, Harappa, and Lothal", "Kalibangan, Ropar, and Banawali", "Surkotada, Nageshwar, and Balakot", "Shortughai, Kot Diji, and Amri"], 0, "Mohenjo-daro, Harappa, and Lothal have yielded numerous copper fish hooks, confirming active fishing industries."),
    ("The trade of salted and dried marine fish to inland cities like Harappa originated from which coastal outpost?", ["Makran Coast (Sutkagendor/Balakot)", "Gulf of Khambhat (Lothal)", "Saurashtra coast (Prabhas Patan)", "Delta of Bengal"], 0, "Faunal remains at Harappa show marine catfish bones imported from the Makran coast of Baluchistan."),
    ("Which wild animal is depicted on the 'Pashupati Seal' alongside the elephant, rhinoceros, and buffalo?", ["Tiger", "Lion", "Gaur", "Cheetah"], 0, "The Pashupati seal depicts a tiger, an elephant, a rhinoceros, a buffalo, and two deer below the throne."),
    ("The Harappans harvested ivory for making combs, pins, and gaming pieces from which native animal?", ["Indian Elephant", "Rhinoceros", "Hippopotamus", "Wild Boar"], 0, "Ivory was obtained from the native Indian elephant (Elephas maximus), either hunted or kept.")
]:
    s2_mastery_eng.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("निम्नलिखित में से किस जंगली बिल्ली प्रजाति के जानवर का मुहरों पर अक्सर चित्रण मिलता है, जबकि सिंह (शेर) अनुपस्थित है?", ["बाघ", "तेंदुआ", "चीता", "जगुआर"], 0, "मुहरों पर बाघ का चित्रण आम है, जबकि शेर लगभग अनुपस्थित है।"),
    ("तांबे/कांसे के मछली पकड़ने के कांटे (fish hooks) बड़ी संख्या में किन प्रमुख स्थलों से प्राप्त हुए हैं?", ["मोहनजोदड़ो, हड़प्पा और लोथल", "कालीबंगन, रोपण और बनावली", "सुरकोटदा, नागेश्वर और बालाकोट", "शोर्तुघई, कोट दीजी और अमरी"], 0, "मोहनजोदड़ो, हड़प्पा और लोथल से भारी संख्या में धातु के मछली पकड़ने के कांटे मिले हैं।"),
    ("अंतर्देशीय शहरों (जैसे हड़प्पा) में सूखी समुद्री मछली का व्यापार बलूचिस्तान के किस तटीय क्षेत्र से शुरू हुआ था?", ["मकरान तट (सुत्कागेंदोर/बालाकोट)", "खंभात की खाड़ी (लोथल)", "सौराष्ट्र तट (प्रभास पाटन)", "बंगाल का डेल्टा"], 0, "प्राणि-अवशेषों से पता चलता है कि हड़प्पा में मिली समुद्री मछली की हड्डियाँ मकरान तट से आई थीं।"),
    ("प्रसिद्ध 'पशुपति मुहर' पर हाथी, गैंडे और भैंस के साथ किस जंगली जानवर का चित्रण मिलता है?", ["बाघ", "शेर", "गौर", "चीता"], 0, "योगी के चारों ओर बाघ, हाथी, गैंडा और भैंस खड़े हैं।"),
    ("हड़प्पा वासी कंघियां, पिन और पासे बनाने के लिए हाथीदांत किस स्थानीय जंगली जानवर से प्राप्त करते थे?", ["भारतीय हाथी", "गैंडा", "दरियाई घोड़ा", "जंगली सूअर"], 0, "हाथीदांत स्थानीय भारतीय हाथी से प्राप्त किया जाता था, जिसके प्रमाण मिले हैं।")
]:
    s2_mastery_hin.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# Multiple Correct MCQ (5)
for q, opts, ans, sol in [
    ("Which of the following wild animals are commonly represented on steatite Harappan seals? (Select all that apply)", ["Tiger", "Rhinoceros", "Elephant", "Lion"], [0, 1, 2], "Tiger, rhinoceros, and elephant are common seal motifs. The lion is absent or extremely rare."),
    ("Select the materials used by Harappans for hunting wild animals and birds: (Select all that apply)", ["Copper arrowheads", "Terracotta slingshot pellets", "Iron bow tips", "Chert knives"], [0, 1, 3], "Copper arrowheads, terracotta pellets, and chert knives were used. Iron was unknown."),
    ("Which coastal sites acted as shell-processing centers for bangle manufacture? (Select all that apply)", ["Nageshwar", "Balakot", "Shortughai", "Kalibangan"], [0, 1], "Nageshwar (Gujarat) and Balakot (Pakistan) were major coastal centers for shell bangle manufacture. Shortughai and Kalibangan are inland."),
    ("Select the wild deer species identified from bone fragments at Harappan sites: (Select all that apply)", ["Chital (spotted deer)", "Sambar", "Barasingha", "Reindeer"], [0, 1, 2], "Chital, Sambar, and Barasingha were native to the Indus basin. Reindeer are arctic."),
    ("Choose the aquatic resources exploited by the Harappans: (Select all that apply)", ["Riverine Catfish", "Marine oysters and shells", "River turtles and tortoises", "Freshwater whales"], [0, 1, 2], "River catfish, marine shells/oysters, and river turtles were consumed. Whales were not exploited.")
]:
    s2_mastery_eng.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("निम्नलिखित में से किन जंगली जानवरों का सेलखड़ी की हड़प्पा मुहरों पर सामान्य रूप से चित्रण मिलता है? (सभी सही विकल्प चुनें)", ["बाघ", "गैंडा", "हाथी", "शेर"], [0, 1, 2], "बाघ, गैंडा और हाथी मुहरों पर आम हैं। शेर का अंकन गायब है।"),
    ("हड़प्पा वासियों द्वारा शिकार के लिए उपयोग की जाने वाली सामग्रियों को चुनें: (सभी सही विकल्प चुनें)", ["तांबे के बाणाग्र", "मिट्टी की गुलेल की गोलियाँ", "लोहे के धनुष के सिरे", "चर्ट पत्थर के चाकू"], [0, 1, 3], "तांबे के बाणाग्र, गुलेल की गोलियां और पत्थर के चाकू प्रयुक्त होते थे। लोहे का ज्ञान नहीं था।"),
    ("कौन से तटीय स्थल चूड़ियाँ बनाने के लिए शंख प्रसंस्करण के मुख्य केंद्र थे? (सभी सही विकल्प चुनें)", ["नागेश्वर", "बालाकोट", "शोर्तुघई", "कालीबंगन"], [0, 1], "नागेश्वर और बालाकोट शंख उद्योग के प्रमुख तटीय केंद्र थे।"),
    ("हड़प्पा स्थलों से पहचानी गई जंगली हिरणों की प्रजातियों को चुनें: (सभी सही विकल्प चुनें)", ["चीतल (spotted deer)", "सांभर", "बारहसिंगा", "रेनडियर (Reindeer)"], [0, 1, 2], "चीतल, सांभर और बारहसिंगा सिंधु घाटी के वनों में पाए जाते थे।"),
    ("हड़प्पा वासियों द्वारा उपयोग किए जाने वाले जलीय संसाधनों को चुनें: (सभी सही विकल्प चुनें)", ["नदी की मल्ल (catfish)", "समुद्री सीप और शंख", "कछुए (River turtles)", "मीठे पानी की व्हेल"], [0, 1, 2], "मछली, शंख और कछुए उनके प्रमुख आहार थे।")
]:
    s2_mastery_hin.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# True/False (8)
for q, ans, sol in [
    ("The lion is frequently represented on Mature Harappan seals.", False, "The lion is absent or extremely rare on seals."),
    ("Copper arrowheads were used by the Harappans to hunt wild game.", True, "Copper arrowheads have been excavated at many sites."),
    ("The chank shell (Turbinella pyrum) was harvested to manufacture bangles.", True, "This shell species was widely used for bangle craft."),
    ("Dried marine fish trade existed between Baluchistan coast and inland Harappa.", True, "Faunal remains confirm Makran coast fish bones at Harappa."),
    ("Rhinoceros depictions on seals suggest a wet, humid environment in ancient times.", True, "The rhino requires wet, swampy grass zones to survive."),
    ("Iron fish hooks were the primary tools used for riverine fishing.", False, "Iron was unknown; fish hooks were made of copper and bronze."),
    ("Pashupati seal depicts a lion seated beneath the throne.", False, "It depicts two deer below the throne, no lion."),
    ("Elephants were depicted on seals, indicating their native status.", True, "The elephant is depicted on many Mature seals and bones are found.")
]:
    s2_mastery_eng.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("शेर का चित्रण परिपक्व हड़प्पा मुहरों पर अक्सर मिलता है।", False, "शेर मुहरों पर अत्यंत दुर्लभ या अनुपस्थित है।"),
    ("हड़प्पा वासी जंगली जानवरों का शिकार करने के लिए तांबे के बाणाग्रों का उपयोग करते थे।", True, "तांबे के बाणाग्र कई स्थलों से मिले हैं।"),
    ("चूड़ियाँ बनाने के लिए 'चैंक शंख' (Turbinella pyrum) का उपयोग किया जाता था।", True, "नागेश्वर और बालाकोट में इसका व्यापक उपयोग होता था।"),
    ("बलूचिस्तान तट और अंतर्देशीय हड़प्पा के बीच सूखी समुद्री मछली का व्यापार होता था।", True, "मकरान तट से मछली की हड्डियाँ हड़प्पा में मिली हैं।"),
    ("मुहरों पर गैंडे का चित्रण प्राचीन काल में यहाँ की आर्द्र और गीली जलवायु को दर्शाता है।", True, "गैंडे के अस्तित्व के लिए दलदली घास के मैदान आवश्यक थे।"),
    ("नदी में मछली पकड़ने के लिए लोहे के हुक मुख्य उपकरण थे।", False, "लोहे का ज्ञान नहीं था; कांटे तांबे/कांसे के होते थे।"),
    ("पशुपति मुहर पर आसन के नीचे एक शेर बैठा दिखाया गया है।", False, "आसन के नीचे दो हिरण दिखाए गए हैं, शेर नहीं।"),
    ("मुहरों पर हाथी चित्रित हैं, जो इस क्षेत्र में उनकी उपस्थिति को दर्शाते हैं।", True, "हाथी का चित्रण आम है और हाथीदांत की वस्तुएं भी मिली हैं।")
]:
    s2_mastery_hin.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

# Fill in the Blank (8)
for q, ans, sol in [
    ("The feline most frequently depicted on Harappan seals is the ________.", "tiger", "The tiger is common, whereas the lion is missing."),
    ("Fish hooks found at Mohenjo-daro were manufactured using ________.", "copper", "Copper and bronze were the primary metals used."),
    ("The marine shell harvested at Nageshwar for bangle making is scientifically named ________.", "Turbinella pyrum", "Turbinella pyrum is the chank shell used for bangles."),
    ("Ancient dried fish bones found at Harappa were imported from the ________ coast.", "Makran", "The Makran coast of Baluchistan was the source."),
    ("The presence of the rhinoceros on seals indicates that the Indus valley had a ________ climate.", "wet", "Swampy grass zones needed for rhinos indicate humid climates."),
    ("Combs and dice were manufactured using ________ harvested from elephants.", "ivory", "Ivory was a major raw material for luxury crafts."),
    ("Wild boar and deer were hunted using copper arrowheads and clay ________.", "slingshots", "Clay pellets were used in slingshots for hunting."),
    ("The famous 'Pashupati Seal' from Mohenjo-daro depicts a tiger and an ________.", "elephant", "Tiger and elephant are depicted on the right side of the deity.")
]:
    s2_mastery_eng.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("हड़प्पा मुहरों पर सबसे अधिक दर्शाया जाने वाला जंगली बिल्ली प्रजाति का जानवर ________ है।", "बाघ", "बाघ का चित्रण मुहरों पर आम है।"),
    ("मोहनजोदड़ो में मिले मछली पकड़ने के कांटे ________ धातु से बनाए गए थे।", "तांबा", "तांबा और कांसा मछली पकड़ने के हुक के लिए प्रयुक्त होते थे।"),
    ("नागेश्वर में चूड़ी उद्योग के लिए उपयोग होने वाले शंख का वैज्ञानिक नाम ________ है।", "टर्बिनेला पाइरम", "टर्बिनेला पाइरम (Turbinella pyrum) चैंक शंख का नाम है।"),
    ("हड़प्पा में मिली प्राचीन सूखी मछली की हड्डियाँ ________ तट से आयात की गई थीं।", "मकरान", "बलूचिस्तान का मकरान तट समुद्री मछली का स्रोत था।"),
    ("मुहरों पर गैंडे की उपस्थिति दर्शाती है कि प्राचीन काल में सिंधु घाटी की जलवायु ________ थी।", "आर्द्र", "दलदली घास के मैदान आर्द्र जलवायु को दर्शाते हैं।"),
    ("हाथियों से प्राप्त ________ का उपयोग कंघियाँ और विलासिता के पासे बनाने में होता था।", "हाथीदांत", "हाथीदांत एक प्रमुख विलासिता की वस्तु थी।"),
    ("जंगली सूअर और हिरणों का शिकार तांबे के बाणाग्र और मिट्टी की ________ से होता था।", "गुलेल", "मिट्टी की गोलियाँ गुलेल में रखकर शिकार किया जाता था।"),
    ("मोहनजोदड़ो से प्राप्त 'पशुपति मुहर' पर बाघ और ________ दर्शाए गए हैं।", "हाथी", "योगी के दाईं ओर बाघ और हाथी खड़े हैं।")
]:
    s2_mastery_hin.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

# Match the Following (3)
s2_matches_eng = [
    {"q": "Match the wild animal with its representation or habitat indicator:",
     "pairs": ["Rhinoceros - Wet, marshy grassland indicator", "Tiger - Depicted on seals with men in trees", "Gharial - Riverine water representation", "Elephant - Source of ivory for luxury goods"],
     "sol": "Rhino indicates marsh; tiger shows tree combat; gharial shows rivers; elephant shows ivory trade."},
    {"q": "Match the coastal resource with its primary processing site:",
     "pairs": ["Chank Shell - Nageshwar shell workshops", "Marine Catfish - Makran coast dried fish export", "Ivory Tusks - Lothal luxury workshop", "River Turtle Shells - Harappa kitchen refuse"],
     "sol": "Shell represents Nageshwar; marine fish represents Makran; ivory represents Lothal; turtle shells represent Harappa refuse."},
    {"q": "Match the hunting/fishing tool with its material composition:",
     "pairs": ["Fish Hooks - Copper or Bronze", "Arrowheads - Copper sheet", "Slingshot Pellets - Baked clay", "Butchery Blades - Chert stone"],
     "sol": "Hooks are copper; arrowheads are copper sheet; pellets are clay; butchery blades are chert."}
]
s2_mastery_eng.extend([make_match_question(m) for m in s2_matches_eng])

s2_matches_hin = [
    {"q": "जंगली जानवर को उसके कलात्मक चित्रण या पारिस्थितिकी से सुमेलित करें:",
     "pairs": ["गैंडा - आर्द्र, दलदली घास के मैदानों का सूचक", "बाघ - मुहरों पर पेड़ पर चढ़े मनुष्य के साथ चित्रण", "घड़ियाल - नदीय जल जीवों का प्रतिनिधित्व", "हाथी - विलासिता की वस्तुओं के लिए हाथीदांत का स्रोत"],
     "sol": "गैंडा दलदली भूमि दर्शाता है; बाघ पेड़ के दृश्य दर्शाता है; घड़ियाल नदियों को दर्शाता है; हाथी हाथीदांत व्यापार को दर्शाता है।"},
    {"q": "तटीय/जलीय संसाधन को उसके प्राथमिक प्रसंस्करण स्थल से सुमेलित करें:",
     "pairs": ["चैंक शंख - नागेश्वर शंख कार्यशालाएँ", "समुद्री कैटफिश - मकरान तट सूखी मछली निर्यात", "हाथी के दांत - लोथल हाथीदांत कार्यशाला", "नदी के कछुए - हड़प्पा के रसोई कचरा स्थल"],
     "sol": "शंख नागेश्वर से जुड़ा है; मछली मकरान से; हाथीदांत लोथल से; कछुआ रसोई कचरे से।"},
    {"q": "शिकार/मछली पकड़ने के उपकरण को उसकी निर्माण सामग्री से सुमेलित करें:",
     "pairs": ["मछली पकड़ने के हुक - तांबा या कांसा", "बाणाग्र - तांबे की चदरें (Copper sheet)", "गुलेल की गोलियाँ - पकी हुई मिट्टी", "काटने के फलक - चर्ट पत्थर"],
     "sol": "हुक तांबे के हैं; बाणाग्र तांबे के पत्तर के हैं; गुलेल गोलियां मिट्टी की हैं; कसाई फलक चर्ट के हैं।"}
]
s2_mastery_hin.extend([make_match_question(m) for m in s2_matches_hin])

# One-Liner (8)
for q, sol in [
    ("Which feline is prominently depicted on Mature Harappan seals?", "The tiger is common, whereas the lion is absent or extremely rare."),
    ("What metal was used to make the fish hooks discovered at Lothal?", "Copper (often alloyed as bronze)."),
    ("Which shell species was harvested at Nageshwar to manufacture bangles?", "The marine chank shell (Turbinella pyrum)."),
    ("Where did the dried fish bones excavated at Harappa originate?", "The Makran coast of Baluchistan (transported over 800 km inland)."),
    ("What climate does the rhinoceros representation on seals imply?", "A wet, humid riverine grassland climate, unlike the dry climate today."),
    ("What luxury items were crafted from elephant ivory?", "Combs, hair pins, dice, scale rulers, and small decorative plaques."),
    ("What hunting weapon was commonly made from copper sheets?", "Lightweight copper arrowheads."),
    ("Which wild animals surround the deity in the Pashupati seal?", "An elephant, a tiger, a rhinoceros, a buffalo, and two deer.")
]:
    s2_mastery_eng.append({"type": "One-Liner", "q": q, "sol": sol})

for q, sol in [
    ("परिपक्व हड़प्पा मुहरों पर किस जंगली बिल्ली का प्रमुखता से चित्रण मिलता है?", "बाघ का चित्रण मिलता है, जबकि शेर लगभग अनुपस्थित है।"),
    ("लोथल में मिले मछली पकड़ने के कांटे किस धातु से बने थे?", "तांबे से (अक्सर कांसे के रूप में मिश्रित)।"),
    ("नागेश्वर में चूड़ियाँ बनाने के लिए किस समुद्री शंख की कटाई की जाती थी?", "चैंक शंख (Turbinella pyrum) की।"),
    ("हड़प्पा से खोदी गई सूखी मछली की हड्डियाँ कहाँ से आई थीं?", "बलूचिस्तान के मकरान तट से (800 किमी से अधिक अंतर्देशीय मार्ग से)।"),
    ("मुहरों पर गैंडे का चित्रण किस प्रकार की जलवायु का संकेत देता है?", "आर्द्र और दलदली घास के मैदानों वाली जलवायु का, जो आज के शुष्क वातावरण से भिन्न थी।"),
    ("हाथीदांत से कौन सी विलासिता की वस्तुएं बनाई जाती थीं?", "कंघियां, पिन, पासे, पैमाने (rulers) और सजावटी पट्टियां।"),
    ("तांबे की चदरों से आमतौर पर कौन सा शिकार का हथियार बनता था?", "हल्के तांबे के बाणाग्र (arrowheads)।"),
    ("पशुपति मुहर पर देवता के चारों ओर कौन से जंगली जानवर खड़े हैं?", "हाथी, बाघ, गैंडा, भैंस और पैरों के पास दो हिरण।")
]:
    s2_mastery_hin.append({"type": "One-Liner", "q": q, "sol": sol})

# Assertion-Reason (8)
for q, ans, sol in [
    ("Assertion (A): The tiger is depicted on multiple Harappan seals in complex narrative scenes.\nReason (R): The tiger was a native predator of the forested Indus plains during the Mature phase.", 0, "Both A and R are true, and the tiger's native presence explains why it was captured in realistic local art."),
    ("Assertion (A): The lion is completely absent or extremely rare on Mature Harappan seals.\nReason (R): Lions were not native to the Indian subcontinent during the Bronze Age.", 2, "A is true; R is false because Asiatic lions did exist in the dry forests of India, but were not chosen as artistic motifs."),
    ("Assertion (A): Coastal sites like Nageshwar functioned as specialized shell-processing centers.\nReason (R): These sites are located near the resource-rich waters of the Gulf of Kutch.", 0, "Both A and R are true, and the proximity to coastal shellbeds explains why shell workshops were concentrated there."),
    ("Assertion (A): Dried and salted marine fish were traded from coastal Baluchistan to Mohenjo-daro and Harappa.\nReason (R): Fish bone remains of marine catfish have been identified in the residential kitchen refuse of Harappa.", 0, "Both A and R are true, and the presence of marine fish bones in inland kitchen dumps verifies the existence of dried fish trade."),
    ("Assertion (A): Rhinoceros and elephant representations on seals indicate that the Indus plain had dense, wet vegetation.\nReason (R): Tectonic upheavals caused the Indus river to dry up, turning the valley into a desert during the Mature phase.", 2, "A is true; R is false because tectonic upheavals and river changes occurred during the Late phase, not Mature phase."),
    ("Assertion (A): Copper fish hooks were highly valued tools in Lothal.\nReason (R): Lothal was situated near a river estuary with access to riverine and marine fishing.", 0, "Both A and R are true, and the estuarine location explains the heavy presence of fishing hooks at the site."),
    ("Assertion (A): Lightweight copper arrowheads were primarily used for military warfare.\nReason (R): Most copper arrowheads lack midribs and were suited for hunting wild game rather than piercing heavy armor.", 3, "A is false because they were too thin for warfare; R is true as their design was suited for hunting birds and small game."),
    ("Assertion (A): Ivory was a highly controlled state monopoly in Harappan cities.\nReason (R): Large workshops with unworked elephant tusks have been excavated at Lothal.", 1, "Both A and R are true, but the presence of workshops at Lothal does not directly explain if or why ivory was a strict state monopoly.")
]:
    s2_mastery_eng.append({"type": "Assertion-Reason", "q": q, "opts": ar_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("कथन (A): हड़प्पा मुहरों पर बाघ को विभिन्न दृश्यों में चित्रित किया गया है।\nकारण (R): परिपक्व काल के दौरान बाघ सिंधु घाटी के घने जंगलों में पाया जाने वाला एक स्थानीय शिकारी था।", 0, "कथन A और R दोनों सही हैं और R, कथन A की सही व्याख्या है क्योंकि बाघ की स्थानीय उपस्थिति ही उसे कला का हिस्सा बनाती थी।"),
    ("कथन (A): परिपक्व हड़प्पा मुहरों पर शेर का चित्रण लगभग अनुपस्थित या अत्यंत दुर्लभ है।\nकारण (R): कांस्य युग के दौरान भारतीय उपमहाद्वीप में शेर मौजूद नहीं थे।", 2, "A सही है लेकिन R गलत है क्योंकि एशियाई शेर भारत के शुष्क जंगलों में मौजूद थे, बस कला में उन्हें चित्रित नहीं किया गया।"),
    ("कथन (A): नागेश्वर जैसे तटीय स्थल विशिष्ट शंख प्रसंस्करण केंद्रों के रूप में कार्य करते थे।\nकारण (R): ये स्थल कच्छ की खाड़ी के निकट समुद्री शंखों की प्रचुरता वाले क्षेत्रों के पास स्थित थे।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या है।"),
    ("कथन (A): बलूचिस्तान तट से सूखी और नमकीन समुद्री मछली मोहनजोदड़ो और हड़प्पा भेजी जाती थी।\nकारण (R): हड़प्पा के आवासीय कचरे के ढेरों में समुद्री कैटफिश की हड्डियों के साक्ष्य मिले हैं।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या है क्योंकि अंतर्देशीय स्थलों पर हड्डियों का मिलना व्यापार की पुष्टि करता है।"),
    ("कथन (A): मुहरों पर गैंडे और हाथी का चित्रण यह दर्शाता है कि सिंधु मैदान में घनी और गीली वनस्पति थी।\nकारण (R): विवर्तनिक बदलावों के कारण सिंधु नदी सूख गई और परिपक्व काल के दौरान ही घाटी मरुस्थल बन गई।", 2, "A सही है लेकिन R गलत है क्योंकि मरुस्थलीकरण का प्रभाव उत्तर (Late) हड़प्पा काल में दिखा, परिपक्व काल में नहीं।"),
    ("कथन (A): लोथल में तांबे के मछली पकड़ने के कांटे अत्यधिक मूल्यवान उपकरण थे।\nकारण (R): लोथल साबरमती नदी के मुहाने के पास स्थित था जहाँ से नदी और समुद्र दोनों में मछली पकड़ी जा सकती थी।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या है।"),
    ("कथन (A): हल्के तांबे के बाणाग्र (arrowheads) मुख्य रूप से सैन्य युद्ध के लिए उपयोग किए जाते थे।\nकारण (R): अधिकांश हड़प्पा बाणाग्र बहुत पतले थे और बिना मध्य-रीढ़ (midrib) के थे, जो शिकार के लिए अधिक उपयुक्त थे।", 3, "A गलत है क्योंकि वे युद्ध के लिए अनुपयुक्त थे; R सही है क्योंकि वे पतले बाणाग्र पक्षियों और छोटे जीवों के शिकार के अनुकूल थे।"),
    ("कथन (A): हड़प्पा शहरों में हाथीदांत एक अत्यधिक नियंत्रित राजकीय एकाधिकार वाली वस्तु थी।\nकारण (R): लोथल से हाथीदांत की प्रसंस्करण कार्यशालाएँ और बिना तराशे हाथी के दांत मिले हैं।", 1, "कथन A और R दोनों सही हैं, लेकिन R, कथन A की सही व्याख्या नहीं है क्योंकि कार्यशाला का मिलना एकाधिकार (monopoly) को सिद्ध नहीं करता।")
]:
    s2_mastery_hin.append({"type": "Assertion-Reason", "q": q, "opts": hin_ar_opts, "ans": ans, "sol": sol})

# Statement-Based (5)
for q, ans, sol in [
    ("Consider the following statements:\nStatement 1: The rhinoceros is depicted on Mature Harappan seals, indicating swampy forest conditions in ancient Sindh.\nStatement 2: The lion is the most common animal represented on seals next to the humped bull.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: The lion is absent or extremely rare, whereas the humped bull/unicorn dominate."),
    ("Consider the following statements:\nStatement 1: Copper fish hooks have been excavated at Mohenjo-daro, confirming riverine fishing.\nStatement 2: Marine fish trade was localized to coastal Saurashtra and did not reach inland Punjab.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: Marine fish bones at Harappa prove that maritime-inland trade did reach inland Punjab."),
    ("Consider the following statements:\nStatement 1: The marine chank shell was processed at Nageshwar to manufacture luxury bangles.\nStatement 2: Shell industry was completely absent at coastal sites in Pakistan.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: Balakot in Pakistan was a major coastal shell manufacturing site."),
    ("Consider the following statements:\nStatement 1: Elephant ivory was used to manufacture combs, dice, and rulers.\nStatement 2: The Harappans imported all their raw elephant ivory from Mesopotamia.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: The Harappans exported ivory to Mesopotamia; they sourced raw ivory locally from native elephants."),
    ("Consider the following statements:\nStatement 1: Hunting was the primary source of food security for all Harappan cities.\nStatement 2: Faunal remains show domestic animals constitute 80%+ of bone assemblages, indicating hunting was only secondary.\nWhich of the statements given above is/are correct?", 1, "Statement 1 is incorrect: Farming and pastoralism were primary. Statement 2 is correct.")
]:
    s2_mastery_eng.append({"type": "Statement-Based", "q": q, "opts": mcq_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: मुहरों पर गैंडे का चित्रण यह दर्शाता है कि प्राचीन सिंध में दलदली वन क्षेत्र मौजूद थे।\nकथन 2: कूबड़ वाले बैल के बाद मुहरों पर सबसे अधिक चित्रित किया जाने वाला पशु शेर है।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि शेर मुहरों पर अत्यंत दुर्लभ है।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: मोहनजोदड़ो से तांबे के मछली पकड़ने के कांटे मिले हैं, जो नदी से मछली पकड़ने को सिद्ध करते हैं।\nकथन 2: समुद्री मछली का व्यापार केवल सौराष्ट्र के तटीय इलाकों तक सीमित था और पंजाब तक नहीं पहुँचता था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि हड़प्पा में मिली समुद्री मछली की हड्डियाँ पंजाब तक इसके व्यापार की पुष्टि करती हैं।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: नागेश्वर में विलासिता की चूड़ियाँ बनाने के लिए चैंक शंख का प्रसंस्करण किया जाता था।\nकथन 2: पाकिस्तान के तटीय स्थलों पर शंख उद्योग पूरी तरह से अनुपस्थित था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि पाकिस्तान का बालाकोट शंख उद्योग का प्रमुख केंद्र था।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: हाथीदांत का उपयोग कंघियां, पासे और मापने के पैमाने बनाने के लिए किया जाता था।\nकथन 2: हड़प्पा वासी अपना सारा कच्चा हाथीदांत मेसोपोटामिया से आयात करते थे।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि वे भारत के स्थानीय हाथियों से हाथीदांत प्राप्त कर मेसोपोटामिया को निर्यात करते थे।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: हड़प्पा के सभी शहरों के लिए शिकार ही खाद्य सुरक्षा का प्राथमिक स्रोत था।\nकथन 2: पुरातात्विक साक्ष्य दर्शाते हैं कि हड्डियों में 80% से अधिक हिस्सा पालतू पशुओं का था, जिससे सिद्ध होता है कि शिकार केवल पूरक था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 1, "कथन 1 गलत है क्योंकि कृषि और पशुपालन मुख्य स्रोत थे। कथन 2 सही है।")
]:
    s2_mastery_hin.append({"type": "Statement-Based", "q": q, "opts": hin_mcq_opts, "ans": ans, "sol": sol})

# Why (3)
for q, sol in [
    ("Why did the Harappans depict tigers and rhinoceroses on seals but not lions?", "Lions lived in drier scrub zones, while Mature Harappan seal makers were located in wetter alluvial zones where tigers and rhinos dominated the local riverine landscape."),
    ("Why were shell workshops concentrated at coastal sites like Nageshwar and Balakot?", "Proximity to the Gulf of Kutch and Makran coast shell beds allowed direct access to raw chank shells, reducing transportation costs for manufacturing bangles."),
    ("Why did marine fish trade reach deep inland cities like Harappa?", "The high food demand of urban elites and a preference for marine catfish proteins prompted a well-organized logistics network using salted and dried preservation.")
]:
    s2_mastery_eng.append({"type": "Why", "q": q, "sol": sol})

for q, sol in [
    ("हड़प्पा वासियों ने मुहरों पर बाघ और गैंडे को तो दर्शाया लेकिन शेर को क्यों नहीं?", "सिंधु घाटी का परिपक्व पर्यावरण अधिक आर्द्र था जहाँ दलदली मैदानों में बाघ और गैंडे आम थे, जबकि शेर शुष्क क्षेत्रों में पाए जाते थे जहाँ प्रशासनिक गतिविधियां कम थीं।"),
    ("नागेश्वर और बालाकोट जैसे तटीय स्थलों पर शंख कार्यशालाएँ क्यों केंद्रित थीं?", "कच्छ की खाड़ी और मकरान तट के समीप कच्चे चैंक शंखों की भारी उपलब्धता थी, जिससे परिवहन लागत कम होती थी और चूड़ियों का निर्माण आसान था।"),
    ("समुद्री मछली का व्यापार हड़प्पा जैसे गहरे अंतर्देशीय शहरों तक क्यों पहुँचता था?", "शहरी संभ्रांत वर्ग की प्रोटीन मांग और समुद्री मछलियों के स्वाद के कारण बलूचिस्तान तट से नमक लगाकर सुखाए गए जलीय उत्पादों का सुव्यवस्थित व्यापार होता था।")
]:
    s2_mastery_hin.append({"type": "Why", "q": q, "sol": sol})

# How (3)
for q, sol in [
    ("How did Harappan artisans manufacture bangles and inlay work from marine shells?", "By using bronze saws to cut the shell whorls, grinding the edges with stone abrasives, and drilling holes with specialized copper drills."),
    ("How did the preservation of marine fish enable long-distance trade to inland centers?", "Fish were gutted, salted, and sun-dried along the Makran coast to prevent decay during the multi-week transport to inland Punjab."),
    ("How was elephant ivory harvested and processed in urban workshops?", "Tusks were cut into blanks using fine metal saws, then carved, incised, and polished in specialized urban workshops like the one at Lothal.")
]:
    s2_mastery_eng.append({"type": "How", "q": q, "sol": sol})

for q, sol in [
    ("हड़प्पा के शिल्पी समुद्री शंखों से चूड़ियाँ और पच्चीकारी का सामान कैसे बनाते थे?", "वे कांसे की आरी (saws) से शंखों को काटते थे, पत्थरों पर रगड़कर उनके किनारों को चिकना करते थे, और तांबे के छेदक यंत्रों (drills) से छेद बनाते थे।"),
    ("समुद्री मछली का परिरक्षण अंतर्देशीय केंद्रों तक लंबी दूरी के व्यापार को कैसे संभव बनाता था?", "मछलियों को साफ करके उनमें नमक भरा जाता था और मकरान तट पर धूप में सुखाया जाता था, जिससे कई हफ्तों के सफर में वे सड़ने से बची रहती थीं।"),
    ("शहरी कार्यशालाओं में हाथियों के दांतों को कैसे संसाधित किया जाता था?", "दांतों को आरी से काटकर ब्लॉक बनाए जाते थे, फिर बारीक छेनी से नक्काशी और पॉलिश करके लोथल जैसी कार्यशालाओं में कंघियां और पासे तैयार किए जाते थे।")
]:
    s2_mastery_hin.append({"type": "How", "q": q, "sol": sol})

# Case Study (3)
for q, sol in [
    ("Analyze the faunal findings at Balakot and their implications for coastal resource consumption.", "Balakot yielded massive piles of shell debitage and marine fish bones, proving coastal populations relied almost entirely on marine harvesting rather than land farming."),
    ("Examine the ivory workshop discoveries at Lothal as evidence of urban craft organization.", "The Lothal ivory workshop has yielded raw tusks, waste chips, and finished combs, demonstrating a high degree of division of labor and craft specialization."),
    ("Examine the Pashupati seal as a visual catalog of the Mature Harappan wild ecosystem.", "The inclusion of rhino, elephant, tiger, and buffalo on a single seal represents a wet, high-rainfall forest ecology, proving Kutch and Sindh were humid zones.")
]:
    s2_mastery_eng.append({"type": "Case Study", "q": q, "sol": sol})

for q, sol in [
    ("बालाकोट में मिले प्राणि-अवशेषों और तटीय संसाधनों के उपभोग पर इसके प्रभाव का विश्लेषण करें।", "बालाकोट से शंखों के कचरे (debitage) और समुद्री मछली की हड्डियों के विशाल ढेर मिले हैं, जो यह साबित करते हैं कि तटीय निवासी पूरी तरह से समुद्री भोजन और शिल्पकला पर निर्भर थे।"),
    ("शहरी शिल्प संगठन के साक्ष्य के रूप में लोथल में हाथीदांत की कार्यशाला की खोजों की जांच करें।", "लोथल में हाथीदांत के टुकड़े, तराशे गए अनुपयोगी टुकड़े (waste chips) और कंघियां मिली हैं, जो संभ्रांत वर्ग के लिए सुनियोजित शिल्प विनिर्माण को सिद्ध करती हैं।"),
    ("परिपक्व हड़प्पा जंगली पारिस्थितिकी तंत्र के दृश्य कैटलॉग के रूप में पशुपति मुहर का परीक्षण करें।", "मुहर पर गैंडे, हाथी, बाघ और भैंस का चित्रण यह दर्शाता है कि हड़प्पा काल के दौरान सिंधु और कच्छ क्षेत्र में उच्च वर्षा वाले आर्द्र जंगल मौजूद थे।")
]:
    s2_mastery_hin.append({"type": "Case Study", "q": q, "sol": sol})

# Teach Concept (3)
for q, sol in [
    ("Explain the concept of 'Resource Proximity' in Harappan shell working industries.", "Workshops were situated directly on the coast (Nageshwar, Balakot) to minimize transport of heavy, raw marine shells, exporting only light finished bangles inland."),
    ("Describe the ecological significance of the 'Forest Fauna Suite' in reconstructive archaeology.", "The presence of tigers, rhinos, and elephants on seals tells us the ancient Indus valley had tall grasslands and riverine gallery forests, indicating high monsoonal rainfall."),
    ("Explain the dried-fish logistics trade between the Makran coast and inland Punjab.", "Coastal communities caught marine catfish, cured them using salt, dried them, and packed them into containers to be shipped via rivers and land routes to Mohenjo-daro and Harappa.")
]:
    s2_mastery_eng.append({"type": "Teach Concept", "q": q, "sol": sol})

for q, sol in [
    ("हड़प्पा शंख उद्योगों के संदर्भ में 'संसाधन निकटता' (Resource Proximity) की अवधारणा को स्पष्ट करें।", "भारी शंखों के परिवहन खर्च को बचाने के लिए कार्यशालाओं को सीधे समुद्र तट (नागेश्वर) पर स्थापित किया जाता था, और वहाँ से केवल तैयार चूड़ियों को ही मुख्य शहरों में भेजा जाता था।"),
    ("पुनर्निर्माण पुरातत्व में 'वन्य जीव सूट' (Forest Fauna Suite) के पारिस्थितिक महत्व का वर्णन करें।", "मुहरों पर हाथी और गैंडे का होना यह सिद्ध करता है कि सिंधु क्षेत्र में घनी वनस्पतियां और दलदली घास के मैदान थे, जो वर्तमान की तुलना में बहुत अधिक वर्षा को दर्शाते हैं।"),
    ("मकरान तट और अंतर्देशीय पंजाब के बीच सूखी मछली के व्यापार की परिवहन प्रणाली को समझाएं।", "तटीय मछुआरे समुद्री मछली पकड़ते थे, उसे नमक से संरक्षित कर सुखाते थे, और फिर नदियों तथा थल मार्गों से बर्तनों में भरकर मोहनजोदड़ो और हड़प्पा के बाजारों तक भेजते थे।")
]:
    s2_mastery_hin.append({"type": "Teach Concept", "q": q, "sol": sol})


# =========================================================================
# SECTION 3: OSTEOLOGICAL STUDIES AND THE HORSE DEBATE
# =========================================================================
s3_mastery_eng = []
s3_mastery_hin = []

# MCQ (5)
for q, opts, ans, sol in [
    ("The controversial skeletal remains of a horse, claimed by Sandor Bokonyi to belong to Equus caballus, were found at which site?", ["Surkotada", "Kalibangan", "Lothal", "Banawali"], 0, "Surkotada in Gujarat yielded disputed horse bones from Mature-Late Harappan levels."),
    ("Who is the primary zooarchaeologist who challenged the Surkotada horse identification, attributing the bones to the wild ass?", ["Richard Meadow", "Sandor Bokonyi", "J.P. Joshi", "John Marshall"], 0, "Richard Meadow argued that the bones belonged to the wild ass (Equus hemionus) or domestic donkey, native to Kutch."),
    ("The native wild ass of the Rann of Kutch, often confused with the horse in bone studies, is scientifically named:", ["Equus hemionus", "Equus caballus", "Equus asinus", "Bos indicus"], 0, "The wild ass (khur) is scientifically known as Equus hemionus."),
    ("Which of the following sites has yielded dental remains (teeth) controversially attributed to the horse?", ["Kalibangan", "Surkotada", "Lothal", "Harappa"], 0, "Kalibangan in Rajasthan has yielded teeth remains attributed to the Equidae family (ass/horse)."),
    ("The complete absence of which animal on Mature Harappan seals is a major argument against its cultural integration?", ["Horse", "Tiger", "Rhinoceros", "Humped Bull"], 0, "The horse is completely missing from all Harappan seals, unlike the humped bull, tiger, and rhino.")
]:
    s3_mastery_eng.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("सैंडोर बोकोनी द्वारा वास्तविक घोड़े (Equus caballus) के रूप में दावा की गई हड्डियाँ किस परिपक्व-उत्तर हड़प्पा स्थल पर पाई गई थीं?", ["सुरकोटदा", "कालीबंगन", "लोथल", "बनावली"], 0, "गुजरात के सुरकोटदा से घोड़े की हड्डियाँ प्राप्त हुई थीं।"),
    ("किस प्रमुख प्राणि-पुरातत्वविद ने सुरकोटदा में घोड़े की हड्डियों की पहचान को चुनौती दी और उन्हें जंगली गधे (wild ass) का बताया?", ["रिचर्ड मीडो", "सैंडोर बोकोनी", "जे.पी. जोशी", "जॉन मार्शल"], 0, "रिचर्ड मीडो ने सुरकोटदा की हड्डियों को जंगली गधे या घरेलू गधे का होने का तर्क दिया।"),
    ("कच्छ के रण के जंगली गधे (khur), जो अक्सर घोड़े की हड्डियों के साथ भ्रमित करता है, का वैज्ञानिक नाम क्या है?", ["इक्वस हेमीओनस (Equus hemionus)", "इक्वस कैबेलस (Equus caballus)", "इक्वस असिनस (Equus asinus)", "बॉस इंडिकस (Bos indicus)"], 0, "जंगली गधे का वैज्ञानिक नाम इक्वस हेमीओनस है।"),
    ("निम्नलिखित में से किस स्थल से घोड़े या गधे के विवादास्पद दांत (teeth remains) प्राप्त हुए हैं?", ["कालीबंगन", "सुरकोटदा", "लोथल", "हड़प्पा"], 0, "राजस्थान के कालीबंगन से इक्विडे (Equidae) परिवार के दांतों के अवशेष मिले हैं।"),
    ("मुहरों पर किस जानवर के चित्रण का पूर्ण अभाव यह दर्शाता है कि वह हड़प्पा समाज का सांस्कृतिक हिस्सा नहीं था?", ["घोड़ा", "बाघ", "गैंडा", "कूबड़ वाला बैल"], 0, "घोड़े का चित्रण मुहरों पर पूरी तरह से अनुपस्थित है, जो उसकी सांस्कृतिक उपेक्षा को दर्शाता है।")
]:
    s3_mastery_hin.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# Multiple Correct MCQ (5)
for q, opts, ans, sol in [
    ("Which of the following sites have yielded skeletal fragments or clay models associated with the horse/ass debate? (Select all that apply)", ["Surkotada", "Lothal", "Kalibangan", "Nageshwar"], [0, 1, 2], "Surkotada (bones), Lothal (figurine), and Kalibangan (teeth) are involved. Nageshwar has no horse remains."),
    ("Select the key arguments used by scholars who reject horse domestication in Harappa: (Select all that apply)", ["Complete absence of horse depictions on seals", "Surkotada bones belong to the native wild ass (Equus hemionus)", "True horses only entered the subcontinent with Rigvedic people", "No horse bones have ever been reported anywhere"], [0, 1, 2], "The absence on seals, structural similarity to wild ass, and Vedic migrations are key arguments. Bones have been claimed, so option 3 is false."),
    ("What features distinguish the Equus hemionus (wild ass) from the Equus caballus (true horse) in bone anatomy? (Select all that apply)", ["Metapodials length", "Molar teeth enamel folding patterns", "Horn core structures", "Tail bone size"], [0, 1], "Metapodials and molar enamel foldings are key diagnostic criteria in equine osteology. Equines do not have horns."),
    ("Select the domestic ruminants whose mortality profiles indicate milk/wool production rather than immediate meat slaughter: (Select all that apply)", ["Adult Cattle", "Adult Sheep", "Young lambs", "Young pigs"], [0, 1], "Adult cattle (traction/milk) and adult sheep (wool) survived to old ages. Young lambs and pigs were slaughtered for meat."),
    ("Choose the scientific methods used in zooarchaeology to analyze Harappan animal bones: (Select all that apply)", ["Osteological species identification", "Cut-mark micro-analysis under SEM", "Age-at-death profile reconstruction", "DNA profiling of ancient pottery residue"], [0, 1, 2], "Osteology, cut-mark micro-analysis, and age profiles are faunal methods. Pottery residue is lipid/chemical analysis.")
]:
    s3_mastery_eng.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("किन स्थलों से घोड़े या गधे से जुड़े विवादित अस्थि अवशेष या मिट्टी के खिलौने मिले हैं? (सभी सही विकल्प चुनें)", ["सुरकोटदा", "लोथल", "कालीबंगन", "नागेश्वर"], [0, 1, 2], "सुरकोटदा (हड्डियां), लोथल (खिलौना) और कालीबंगन (दांत) से साक्ष्य मिले हैं। नागेश्वर से कोई अवशेष नहीं मिला।"),
    ("उन प्रमुख तर्कों को चुनें जो हड़प्पा में घोड़े के पालतू होने को खारिज करते हैं: (सभी सही विकल्प चुनें)", ["मुहरों पर घोड़े के चित्रण का पूर्ण अभाव", "सुरकोटदा की हड्डियां स्थानीय जंगली गधे (Equus hemionus) की हो सकती हैं", "वास्तविक घोड़ा ऋग्वैदिक लोगों के साथ उपमहाद्वीप में आया", "कभी भी किसी भी स्थल से घोड़े की हड्डियों का दावा नहीं किया गया"], [0, 1, 2], "मुहरों पर अनुपस्थिति, जंगली गधे की हड्डियों से समानता और वैदिक प्रवास मुख्य तर्क हैं।"),
    ("हड्डियों के अध्ययन में जंगली गधे (Equus hemionus) को वास्तविक घोड़े (Equus caballus) से कैसे अलग किया जाता है? (सभी सही विकल्प चुनें)", ["मेटापोडियल्स (पैरों की हड्डियों) की लंबाई", "दाढ़ के दांतों के इनेमल का पैटर्न", "सींगों की संरचना", "पूंछ की लंबाई"], [0, 1], "पैरों की मेटापोडियल हड्डियों और दांतों के दाढ़ के पैटर्न से इन्हें पहचाना जाता है। गधों/घोड़ों के सींग नहीं होते।"),
    ("उन पालतू जुगाली करने वाले पशुओं को चुनें जिनकी हड्डियों की आयु से पता चलता है कि उन्हें मांस के बजाय दूध/ऊन के लिए पाला गया: (सभी सही विकल्प चुनें)", ["वयस्क मवेशी (Cattle)", "वयस्क भेड़", "मेमने (Young lambs)", "छोटे सूअर"], [0, 1], "वयस्क गाय-बैल और वयस्क भेड़ों को लंबी उम्र तक पाला जाता था, जबकि सूअरों को कम उम्र में मार दिया जाता था।"),
    ("हड़प्पा कालीन पशु हड्डियों के विश्लेषण के लिए प्रयुक्त वैज्ञानिक तकनीकों को चुनें: (सभी सही विकल्प चुनें)", ["अस्थि पहचान (Osteological species identification)", "माइक्रोस्कोप के तहत हड्डियों पर कटने के निशानों का विश्लेषण", "मृत्यु-आयु का प्रोफाइल तैयार करना", "मिट्टी के बर्तनों के लिपिड अवशेषों का डीएनए"], [0, 1, 2], "अस्थि पहचान, कट-मार्क सूक्ष्म विश्लेषण और आयु प्रोफाइल प्राणि-पुरातत्व की विधियां हैं।")
]:
    s3_mastery_hin.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# True/False (8)
for q, ans, sol in [
    ("Richard Meadow confirmed that the Surkotada bones belong to the true horse.", False, "Meadow identified them as wild ass (Equus hemionus)."),
    ("The scientific name of the true horse is Equus caballus.", True, "Equus caballus is the biological classification of the horse."),
    ("The horse is depicted on several Mature Harappan seals alongside the unicorn.", False, "The horse is completely absent from all Harappan seals."),
    ("Cut marks on animal bones near residential dump yards indicate meat consumption.", True, "Butchery marks prove the animals were slaughtered and eaten."),
    ("Sandor Bokonyi argued that the Surkotada bones belong to Equus caballus.", True, "Bokonyi confirmed the bones belong to the true horse."),
    ("The wild ass is native to the marshes of Baluchistan.", False, "The wild ass (khur) is native to the salt marshes of the Rann of Kutch."),
    ("Camel and horse bones are found in equal quantities at Mohenjo-daro.", False, "Horse bones are extremely rare/disputed; camel bones are more documented but still limited."),
    ("Zooarchaeology studies show that Harappans relied on domestic animals for 80%+ of their meat.", True, "The vast majority of bone fragments belong to domestic species, proving pastoral dominance.")
]:
    s3_mastery_eng.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("रिचर्ड मीडो ने पुष्टि की कि सुरकोटदा की हड्डियाँ वास्तविक घोड़े की थीं।", False, "मीडो ने उन्हें जंगली गधे (Equus hemionus) की हड्डियाँ बताया।"),
    ("वास्तविक घोड़े का वैज्ञानिक नाम 'इक्वस कैबेलस' (Equus caballus) है।", True, "इक्वस कैबेलस घोड़े का वैज्ञानिक नाम है।"),
    ("मुहरों पर एक सींग वाले गेंडे के साथ घोड़े का भी कई जगह अंकन मिलता है।", False, "घोड़ा मुहरों पर पूरी तरह से अनुपस्थित है।"),
    ("आवासीय कचरा क्षेत्रों के पास हड्डियों पर काटने के निशान मांस उपभोग को दर्शाते हैं।", True, "काटने के निशान कसाईखाने और भोजन प्रसंस्करण के संकेत हैं।"),
    ("सैंडोर बोकोनी का तर्क था कि सुरकोटदा के अवशेष वास्तविक घोड़े के थे।", True, "बोकोनी ने इन अवशेषों की पहचान घोड़े के रूप में की थी।"),
    ("जंगली गधा (khur) बलूचिस्तान के दलदली जंगलों का मूल निवासी है।", False, "जंगली गधा मुख्य रूप से गुजरात के कच्छ के रण का मूल निवासी है।"),
    ("मोहनजोदड़ो में ऊंट और घोड़े की हड्डियाँ बराबर मात्रा में मिली हैं।", False, "घोड़े की हड्डियाँ अत्यंत दुर्लभ/विवादित हैं, जबकि ऊंट की हड्डियाँ अधिक मात्रा में मिली हैं।"),
    ("प्राणि-पुरातत्व से पता चलता है कि हड़प्पा वासियों के मांस का 80% से अधिक हिस्सा पालतू पशुओं से आता था।", True, "हड्डियों का बड़ा हिस्सा पालतू प्रजातियों का है, जो पशुपालन की प्रधानता को दर्शाता है।")
]:
    s3_mastery_hin.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

# Fill in the Blank (8)
for q, ans, sol in [
    ("The scholar who identified the Surkotada bones as Equus caballus was ________.", "Sandor Bokonyi", "Bokonyi was the Hungarian expert who confirmed the horse identification."),
    ("The scientific name for the Kutch wild ass is ________.", "Equus hemionus", "Equus hemionus is the wild ass native to Kutch."),
    ("The animal completely absent from Harappan seals but central to Rigvedic culture is the ________.", "horse", "The horse is the key cultural differentiator between Harappan and Vedic times."),
    ("Osteological remains of equids at Kalibangan consist primarily of ________ fragments.", "teeth", "Kalibangan yielded equid teeth remains."),
    ("The study of ancient animal bones from archaeological sites is called ________.", "zooarchaeology", "Zooarchaeology (or faunal analysis) is the scientific study of animal remains."),
    ("Cut marks on bones near Harappan kitchens indicate they were processed for ________.", "meat", "Cut marks indicate butchering for food consumption."),
    ("Richard Meadow argued that the Surkotada bones belong to the domestic ________.", "ass", "Meadow suggested they belonged to a donkey or wild ass."),
    ("The horse is scientifically classified under the genus ________.", "Equus", "Equus is the genus covering horses, asses, and zebras.")
]:
    s3_mastery_eng.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("सुरकोटदा की हड्डियों की पहचान वास्तविक घोड़े (Equus caballus) के रूप में करने वाले विद्वान ________ थे।", "सैंडोर बोकोनी", "हंगरी के विशेषज्ञ बोकोनी ने घोड़े के अवशेष होने का दावा किया था।"),
    ("कच्छ के जंगली गधे (khur) का वैज्ञानिक नाम ________ है।", "इक्वस हेमीओनस", "इक्वस हेमीओनस जंगली गधे का वैज्ञानिक नाम है।"),
    ("हड़प्पा मुहरों पर पूरी तरह गायब लेकिन ऋग्वैदिक संस्कृति में केंद्रीय स्थान रखने वाला जानवर ________ है।", "घोड़ा", "घोड़ा दोनों संस्कृतियों के अंतर का सबसे प्रमुख बिंदु है।"),
    ("कालीबंगन में मिले अश्व परिवार (equid) के साक्ष्य मुख्य रूप से उसके ________ के अवशेष हैं।", "दांत", "कालीबंगन से दांत और जबड़े के टुकड़े मिले हैं।"),
    ("पुरातात्विक स्थलों से प्राप्त प्राचीन पशु हड्डियों के अध्ययन को ________ कहा जाता है।", "प्राणि-पुरातत्व", "प्राणि-पुरातत्व (zooarchaeology) हड्डियों के विश्लेषण का विज्ञान है।"),
    ("हड़प्पा के रसोईघरों के पास हड्डियों पर काटने के निशान दर्शाते हैं कि उन्हें ________ के लिए काटा गया था।", "मांस", "काटने के निशान मांस काटने के सीधे प्रमाण हैं।"),
    ("रिचर्ड मीडो ने तर्क दिया कि सुरकोटदा के अवशेष पालतू ________ के हो सकते हैं।", "गधे", "मीडो ने इसे गधा (domestic ass) या जंगली गधा माना।"),
    ("घोड़े को वैज्ञानिक रूप से ________ वंश (genus) के अंतर्गत वर्गीकृत किया जाता है।", "इक्वस", "इक्वस (Equus) गधों, घोड़ों और जेब्रा का वैज्ञानिक वंश है।")
]:
    s3_mastery_hin.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

# Match the Following (3)
s3_matches_eng = [
    {"q": "Match the scholar/archaeologist with their stance on the Surkotada bones:",
     "pairs": ["Sandor Bokonyi - True horse (Equus caballus) identification", "Richard Meadow - Wild ass (Equus hemionus) or domestic donkey claim", "J.P. Joshi - Original excavator of Surkotada in Kutch", "Asko Parpola - Supportive of early horse presence arguments"],
     "sol": "Bokonyi identified the horse; Meadow contested it; Joshi excavated Kutch; Parpola supports early horse presence arguments."},
    {"q": "Match the equine species with its diagnostic biological nomenclature:",
     "pairs": ["True Horse - Equus caballus", "Wild Ass (Khur) - Equus hemionus", "Domestic Donkey - Equus asinus", "Zebu Cattle - Bos indicus"],
     "sol": "Links equine and bovine species with their exact scientific classifications."},
    {"q": "Match the zooarchaeological finding with the corresponding interpretation:",
     "pairs": ["Cut marks on ribs - Butchery and meat processing", "Old age at death - Milk or traction exploitation", "Young age at death - Quick meat slaughter", "High concentration in dumps - Urban refuse and dumping patterns"],
     "sol": "Rib cuts indicate butchering; old age indicates milk/traction; young age shows meat slaughter; dumps show urban refuse."}
]
s3_mastery_eng.extend([make_match_question(m) for m in s3_matches_eng])

s3_matches_hin = [
    {"q": "विद्वान/पुरातत्वविद को सुरकोटदा की हड्डियों पर उनके दृष्टिकोण से सुमेलित करें:",
     "pairs": ["सैंडोर बोकोनी - वास्तविक घोड़े (Equus caballus) की पहचान का दावा", "रिचर्ड मीडो - जंगली गधे (Equus hemionus) या गधे होने का तर्क", "जे.पी. जोशी - सुरकोटदा के मूल उत्खननकर्ता", "अस्को परपोला - प्रारंभिक अश्व उपस्थिति के तर्कों के समर्थक"],
     "sol": "बोकोनी ने घोड़े का दावा किया; मीडो ने गधे का; जोशी ने उत्खनन किया; परपोला प्रारंभिक अश्व तर्कों के समर्थक हैं।"},
    {"q": "अश्व परिवार (Equidae) की प्रजाति को उसके वैज्ञानिक नाम से सुमेलित करें:",
     "pairs": ["वास्तविक घोड़ा - इक्वस कैबेलस (Equus caballus)", "जंगली गधा - इक्वस हेमीओनस (Equus hemionus)", "घरेलू गधा - इक्वस असिनस (Equus asinus)", "कूबड़ वाले मवेशी - बॉस इंडिकस (Bos indicus)"],
     "sol": "अश्व और गधे की प्रजातियों को उनके स्थापित जैविक नामों से जोड़ता है।"},
    {"q": "प्राणि-पुरातत्वीय साक्ष्य को उसके निष्कर्ष/व्याख्या से सुमेलित करें:",
     "pairs": ["हड्डियों पर काटने के निशान - कसाईखाना और मांस प्रसंस्करण", "मवेशियों की अधिक आयु - दूध उत्पादन या हल चलाने में उपयोग", "मवेशियों की कम आयु - मांस के लिए पशु वध", "कचरे के ढेर में हड्डियों की प्रचुरता - शहरी भोजन प्रतिरूप (consumption patterns)"],
     "sol": "काटने के निशान मांस प्रसंस्करण दर्शाते हैं; अधिक आयु श्रम/दूध दर्शाती है; कम आयु मांस वध दर्शाती है; ढेर शहरी उपभोग दर्शाते हैं।"}
]
s3_mastery_hin.extend([make_match_question(m) for m in s3_matches_hin])

# One-Liner (8)
for q, sol in [
    ("Who identified the Surkotada bones as belonging to the true horse?", "Hungarian zooarchaeologist Sandor Bokonyi."),
    ("Which scholar challenged this, claiming they were bones of the wild ass?", "American archaeologist Richard Meadow."),
    ("What is the scientific name of the wild ass native to the Rann of Kutch?", "Equus hemionus."),
    ("Where were equine teeth remains excavated in Rajasthan?", "Kalibangan."),
    ("Which animal is missing from seals but central to Vedic Sanskrit texts?", "The horse (Asva)."),
    ("What does a high concentration of cattle bones at Mohenjo-daro suggest?", "Cattle beef was a primary meat protein source for the urban population."),
    ("How do zooarchaeologists determine if sheep were kept for wool?", "By analyzing the age-at-death profiles; sheep kept until old age were sheared for wool."),
    ("Why are equine bones extremely rare compared to cattle bones in Indus sites?", "Because horses were not native or widely domesticated in the Indus plains during the Mature phase.")
]:
    s3_mastery_eng.append({"type": "One-Liner", "q": q, "sol": sol})

for q, sol in [
    ("सुरकोटदा की हड्डियों की पहचान घोड़े के रूप में करने वाले विशेषज्ञ कौन थे?", "हंगरी के प्राणि-पुरातत्वविद सैंडोर बोकोनी।"),
    ("किस विद्वान ने इस पहचान को चुनौती दी और कहा कि वे जंगली गधे की हड्डियाँ थीं?", "अमेरिकी पुरातत्वविद रिचर्ड मीडो।"),
    ("कच्छ के रण में पाए जाने वाले जंगली गधे का वैज्ञानिक नाम क्या है?", "इक्वस हेमीओनस (Equus hemionus)।"),
    ("राजस्थान में किस स्थल से अश्व परिवार के दांतों के अवशेष मिले हैं?", "कालीबंगन से।"),
    ("कौन सा जानवर मुहरों से गायब है लेकिन वैदिक संस्कृत ग्रंथों में अत्यंत महत्वपूर्ण है?", "घोड़ा (अश्व)।"),
    ("मोहनजोदड़ो में मवेशियों की हड्डियों की भारी प्रचुरता क्या दर्शाती है?", "यह दर्शाती है कि मवेशियों का मांस शहरी आबादी के भोजन का मुख्य प्रोटीन स्रोत था।"),
    ("प्राणि-पुरातत्वविद यह कैसे तय करते हैं कि भेड़ को ऊन के लिए पाला गया था?", "भेड़ों की मृत्यु-आयु का विश्लेषण करके; अधिक आयु की भेड़ों का उपयोग ऊन कतरने के लिए किया जाता था।"),
    ("हड़प्पा स्थलों पर मवेशियों की तुलना में अश्व परिवार की हड्डियाँ अत्यंत दुर्लभ क्यों हैं?", "क्योंकि परिपक्व काल के दौरान सिंधु मैदान में घोड़े मूल निवासी नहीं थे और न ही उन्हें व्यापक रूप से पाला गया था।")
]:
    s3_mastery_hin.append({"type": "One-Liner", "q": q, "sol": sol})

# Assertion-Reason (8)
for q, ans, sol in [
    ("Assertion (A): The identification of horse bones at Surkotada is hotly contested by archaeologists.\nReason (R): Structural differences between bones of the true horse (Equus caballus) and the wild ass (Equus hemionus) are highly subtle and overlap.", 0, "Both A and R are true, and the structural overlap explains why the identification is contested."),
    ("Assertion (A): The horse was a driving force behind the Mature Harappan urban economy.\nReason (R): Horse remains are extremely rare and the animal is completely absent from seals and terracotta art.", 3, "A is false because cattle, not horses, drove the economy; R is true."),
    ("Assertion (A): Zooarchaeologists reconstruct age-at-death profiles of excavated animal bones.\nReason (R): The slaughter age reveals whether the animal was raised for primary products (meat) or secondary products (milk/wool/traction).", 0, "Both A and R are true, and the reason explains the methodology's objective."),
    ("Assertion (A): Cut marks on animal bones near residential sectors are studied under scanning electron microscopes.\nReason (R): Microscopic analysis helps distinguish cuts made by bronze butchery tools from scratches caused by carnivore teeth.", 0, "Both A and R are true, and micro-analysis explains how archaeologists verify human butchery."),
    ("Assertion (A): The Rann of Kutch has yielded heavy remains of the Equidae family.\nReason (R): The wild ass (Equus hemionus) has been a native inhabitant of the Kutch salt marshes since ancient times.", 0, "Both A and R are true, and the native status of the wild ass explains why equid bones are concentrated in Kutch."),
    ("Assertion (A): Cattle were slaughtered at a young age in Harappan urban centers.\nReason (R): Most cattle bone assemblages show signs of survival into mature ages for traction labor.", 3, "A is false because they were kept until old age; R is true."),
    ("Assertion (A): The horse is a key marker of cultural transition in ancient Indian history.\nReason (R): The horse is dominant in Rigvedic descriptions but absent from Mature Harappan administrative art.", 0, "Both A and R are true, and the contrast between the two cultures explains why the horse is a transition marker."),
    ("Assertion (A): Osteological studies prove that wild game made up the majority of the Harappan diet.\nReason (R): Domesticated cattle, sheep, and goats constitute over 80% of recovered animal bones at urban sites.", 3, "A is false because domestic livestock made up the majority; R is true.")
]:
    s3_mastery_eng.append({"type": "Assertion-Reason", "q": q, "opts": ar_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("कथन (A): सुरकोटदा में मिली घोड़े की हड्डियों की पहचान पुरातत्वविदों के बीच अत्यधिक विवादित है।\nकारण (R): वास्तविक घोड़े (Equus caballus) और जंगली गधे (Equus hemionus) की हड्डियों के बीच का संरचनात्मक अंतर अत्यंत सूक्ष्म और परस्पर व्यापी (overlapping) है।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या है क्योंकि सूक्ष्म अंतर ही विवाद का मुख्य कारण है।"),
    ("कथन (A): घोड़ा परिपक्व हड़प्पा की शहरी अर्थव्यवस्था का मुख्य चालक था।\nकारण (R): घोड़े के अवशेष अत्यंत दुर्लभ हैं और यह मुहरों तथा मिट्टी के खिलौनों से पूरी तरह नदारद है।", 3, "A गलत है क्योंकि अर्थव्यवस्था बैलों पर निर्भर थी, घोड़ा दुर्लभ था; R सही है।"),
    ("कथन (A): प्राणि-पुरातत्वविद खोदी गई पशु हड्डियों की मृत्यु-आयु का प्रोफाइल तैयार करते हैं।\nकारण (R): वध की आयु से पता चलता है कि पशु को प्राथमिक उत्पाद (मांस) के लिए पाला गया था या द्वितीयक उत्पाद (दूध/ऊन/श्रम) के लिए।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या है।"),
    ("कथन (A): आवासीय क्षेत्रों के पास मिली हड्डियों पर कटने के निशानों का अध्ययन माइक्रोस्कोप से किया जाता है।\nकारण (R): सूक्ष्म विश्लेषण से कांसे के औजारों द्वारा बनाए गए कटने के निशानों को जंगली जानवरों के दांतों के खरोंच से अलग करने में मदद मिलती है।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या है।"),
    ("कथन (A): कच्छ के रण से अश्व परिवार (Equidae) के भारी अवशेष मिले हैं।\nकारण (R): जंगली गधा (Equus hemionus) प्राचीन काल से ही कच्छ के नमक के दलदलों का मूल निवासी रहा है।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या है।"),
    ("कथन (A): हड़प्पा के शहरी केंद्रों में मवेशियों (गाय-बैल) को बहुत कम उम्र में मार दिया जाता था।\nकारण (R): मवेशियों की अधिकांश हड्डियां यह दर्शाती हैं कि उन्हें कृषि श्रम के लिए परिपक्व होने तक पाला जाता था।", 3, "A गलत है क्योंकि उन्हें वयस्क होने तक पाला जाता था; R सही है।"),
    ("कथन (A): घोड़ा प्राचीन भारतीय इतिहास में सांस्कृतिक संक्रमण का एक प्रमुख संकेतक है।\nकारण (R): ऋग्वैदिक वर्णनों में घोड़े की प्रधानता है जबकि परिपक्व हड़प्पा प्रशासनिक कला में यह पूर्णतः अनुपस्थित है।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या है क्योंकि यह दोनों सभ्यताओं के बीच अंतर को स्पष्ट करता है।"),
    ("कथन (A): अस्थि अध्ययनों से सिद्ध होता है कि जंगली जानवरों का मांस हड़प्पा वासियों के भोजन का मुख्य हिस्सा था।\nकारण (R): शहरी स्थलों पर प्राप्त हड्डियों में 80% से अधिक हिस्सा पालतू गाय, भैंस, भेड़ और बकरियों का है।", 3, "A गलत है क्योंकि मुख्य आहार पालतू पशुओं से आता था; R सही है।")
]:
    s3_mastery_hin.append({"type": "Assertion-Reason", "q": q, "opts": hin_ar_opts, "ans": ans, "sol": sol})

# Statement-Based (5)
for q, ans, sol in [
    ("Consider the following statements:\nStatement 1: Sandor Bokonyi confirmed the presence of Equus caballus at Surkotada.\nStatement 2: Richard Meadow argued these remains belong to Equus hemionus.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct, reflecting the two sides of the horse debate."),
    ("Consider the following statements:\nStatement 1: The horse is depicted on all Major seals of Mohenjo-daro.\nStatement 2: The unicorn is the most common animal on Harappan seals.\nWhich of the statements given above is/are correct?", 1, "Statement 1 is incorrect: The horse is absent from seals. Statement 2 is correct."),
    ("Consider the following statements:\nStatement 1: Equus hemionus is the scientific name for the wild ass native to Kutch.\nStatement 2: Equus hemionus bones are structurally identical to sheep bones.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: They are structurally similar to horse bones, not sheep."),
    ("Consider the following statements:\nStatement 1: The survival of cattle to mature ages indicates dairy and traction exploitation.\nStatement 2: Cut marks on ribs and long bones prove meat processing occurred in cities.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct, reflecting zooarchaeological interpretations."),
    ("Consider the following statements:\nStatement 1: Bones of wild game like deer and wild boar are completely absent at all Harappan sites.\nStatement 2: Wild game bones constitute less than 20% of the total faunal assemblages, proving hunting was supplementary.\nWhich of the statements given above is/are correct?", 1, "Statement 1 is incorrect: They are present but in small quantities. Statement 2 is correct.")
]:
    s3_mastery_eng.append({"type": "Statement-Based", "q": q, "opts": mcq_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: सैंडोर बोकोनी ने सुरकोटदा में इक्वस कैबेलस (घोड़े) की उपस्थिति की पुष्टि की थी।\nकथन 2: रिचर्ड मीडो ने तर्क दिया कि ये अवशेष इक्वस हेमीओनस (जंगली गधे) के हैं।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 2, "दोनों कथन सही हैं, जो घोड़े के विवाद के दो पहलुओं को दर्शाते हैं।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: मोहनजोदड़ो की सभी मुख्य मुहरों पर घोड़े का अंकन मिलता है।\nकथन 2: हड़प्पा मुहरों पर एक सींग वाला गेंडा सबसे आम जानवर है।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 1, "कथन 1 गलत है क्योंकि मुहरों पर घोड़ा अनुपस्थित है। कथन 2 सही है।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: इक्वस हेमीओनस कच्छ के रण के जंगली गधे का वैज्ञानिक नाम है।\nकथन 2: इक्वस हेमीओनस की हड्डियाँ संरचना में भेड़ की हड्डियों के समान होती हैं।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि ये घोड़े की हड्डियों के समान होती हैं, भेड़ की नहीं।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: मवेशियों का बुढ़ापे तक जीवित रहना दूध और श्रम के उपयोग को दर्शाता है।\nकथन 2: पसलियों और लंबी हड्डियों पर काटने के निशान शहरों में मांस प्रसंस्करण को सिद्ध करते हैं।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 2, "दोनों कथन सही हैं, जो प्राणि-पुरातत्व के स्थापित निष्कर्षों को दर्शाते हैं।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: किसी भी हड़प्पा स्थल से जंगली सूअर और हिरण जैसे जंगली जीवों की हड्डियाँ बिल्कुल नहीं मिली हैं।\nकथन 2: कुल प्राप्त हड्डियों में जंगली जीवों की हड्डियाँ 20% से कम हैं, जिससे सिद्ध होता है कि शिकार केवल एक पूरक गतिविधि थी।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 1, "कथन 1 गलत है क्योंकि हड्डियां मिली हैं। कथन 2 सही है।")
]:
    s3_mastery_hin.append({"type": "Statement-Based", "q": q, "opts": hin_mcq_opts, "ans": ans, "sol": sol})

# Why (3)
for q, sol in [
    ("Why are equid bone identifications so controversial in Harappan archaeology?", "Because the skeletal structures of horses, domestic asses, and native wild asses (khur) are extremely similar, and Kutch is home to native wild asses, causing potential misidentifications."),
    ("Why did the absence of horse representations on seals influence the Aryan invasion debate?", "The horse is central to Rigvedic culture. Its absence from Harappan seals suggests that the Indus civilization was culturally distinct and predated the horse-centric Vedic culture."),
    ("Why do zooarchaeologists compile mortality profiles of sheep and goat bones?", "To determine pastoral strategies: slaughtering young animals suggests meat production, whereas keeping mature ones suggests milk or wool harvesting.")
]:
    s3_mastery_eng.append({"type": "Why", "q": q, "sol": sol})

for q, sol in [
    ("हड़प्पा पुरातत्व में अश्व परिवार (equid) की हड्डियों की पहचान इतनी विवादास्पद क्यों है?", "क्योंकि घोड़े, पालतू गधे और कच्छ के स्थानीय जंगली गधे (khur) की हड्डियाँ बनावट में बहुत समान होती हैं, जिससे हड्डियों के आधार पर अंतर करना कठिन होता है।"),
    ("मुहरों पर घोड़े के चित्रण न होने ने आर्य आक्रमण/प्रवास विवाद को कैसे प्रभावित किया?", "चूंकि ऋग्वेद में घोड़े को केंद्रीय महत्व दिया गया है, इसलिए हड़प्पा कला से इसका गायब होना यह संकेत देता है कि सिंधु सभ्यता सांस्कृतिक रूप से वैदिक सभ्यता से भिन्न और उससे प्राचीन थी।"),
    ("प्राणि-पुरातत्वविद भेड़ और बकरियों की हड्डियों की मृत्यु-आयु का प्रोफाइल क्यों बनाते हैं?", "चरवाहों की आर्थिक रणनीति को समझने के लिए: कम उम्र में काटना मांस उत्पादन दर्शाता है, जबकि लंबी उम्र तक पालना ऊन और दूध के उत्पादन को सिद्ध करता है।")
]:
    s3_mastery_hin.append({"type": "Why", "q": q, "sol": sol})

# How (3)
for q, sol in [
    ("How do zooarchaeologists distinguish cut marks caused by bronze tools from carnivore gnawing?", "By analyzing the cuts under high magnification; bronze tools create clean, V-shaped grooves with parallel striations, while teeth create shallow, U-shaped scrapes."),
    ("How did Sandor Bokonyi identify the Surkotada bones as Equus caballus?", "By conducting metric measurements of the metapodials and checking enamel folding patterns on the molars, which matched true horse references."),
    ("How does bone chemistry (stable isotope analysis) help reconstruct Harappan animal diets?", "By analyzing carbon and nitrogen isotopes in bone collagen, which reveals whether the animals fed on plains grasses (C4 plants) or hilly shrubs (C3 plants).")
]:
    s3_mastery_eng.append({"type": "How", "q": q, "sol": sol})

for q, sol in [
    ("प्राणि-पुरातत्वविद कांसे के औजारों के काटने के निशान को जंगली जानवरों द्वारा चबाए जाने के निशान से कैसे अलग करते हैं?", "उच्च आवर्धन (magnification) के तहत कट का विश्लेषण करके; कांसे के औजार वी-आकार (V-shaped) की रेखाएं बनाते हैं, जबकि दांतों से उथले यू-आकार (U-shaped) के खरोंच बनते हैं।"),
    ("सैंडोर बोकोनी ने सुरकोटदा की हड्डियों की पहचान वास्तविक घोड़े के रूप में कैसे की?", "उन्होंने पैर की हड्डियों (metapodials) के आकार का मापन किया और दाढ़ के दांतों के इनेमल के घुमावदार पैटर्न की जांच की, जो असली घोड़े के नमूनों से मेल खाती थी।"),
    ("हड्डियों का रासायनिक विश्लेषण (स्थिर समस्थानिक विश्लेषण) पशुओं के आहार को समझने में कैसे मदद करता है?", "हड्डियों के कोलेजन में कार्बन और नाइट्रोजन समस्थानिकों का विश्लेषण करके, जिससे पता चलता है कि पशु मैदानी घास (C4 पौधे) चरते थे या पहाड़ी झाड़ियाँ (C3 पौधे)।")
]:
    s3_mastery_hin.append({"type": "How", "q": q, "sol": sol})

# Case Study (3)
for q, sol in [
    ("Analyze the Surkotada equine bone assemblage and the debate between Bokonyi and Meadow.", "Bokonyi identified the bones as Equus caballus using metrical analysis, while Meadow challenged it as Equus hemionus, emphasizing the native presence of wild asses in Kutch."),
    ("Examine the bone refuse heaps of Mohenjo-daro as a source of urban dietary profiles.", "Residential refuse dumps at Mohenjo-daro yielded massive quantities of cattle, buffalo, and pig bones with cut marks, proving meat was a major component of the urban diet."),
    ("Evaluate the equine teeth discoveries at Kalibangan and their archaeological context.", "The equid teeth remains at Kalibangan are located in Mature Harappan layers, but due to lack of complete skeletons, their domestic horse status remains unproven.")
]:
    s3_mastery_eng.append({"type": "Case Study", "q": q, "sol": sol})

for q, sol in [
    ("सुरकोटदा से मिले घोड़े/गधे की हड्डियों के साक्ष्य और बोकोनी तथा मीडो के बीच बहस का विश्लेषण करें।", "बोकोनी ने हड्डियों के माप के आधार पर घोड़े (caballus) का दावा किया, जबकि मीडो ने कच्छ में जंगली गधों (hemionus) की प्राकृतिक उपस्थिति का हवाला देकर इसे खारिज किया।"),
    ("शहरी आहार प्रतिरूप के स्रोत के रूप में मोहनजोदड़ो के कचरा ढेरों में मिली हड्डियों का परीक्षण करें।", "मोहनजोदड़ो के कचरा ढेरों से कटने के निशानों वाली गाय, भैंस और सूअर की भारी हड्डियाँ मिली हैं, जो साबित करती हैं कि मांसाहार शहरी भोजन का एक महत्वपूर्ण हिस्सा था।"),
    ("कालीबंगन में मिले घोड़े/गधे के दांतों के अवशेषों और उनके पुरातात्विक संदर्भ का मूल्यांकन करें।", "कालीबंगन के परिपक्व स्तरों से दांत मिले हैं, लेकिन पूरे कंकाल के बिना यह साबित नहीं किया जा सकता कि ये पालतू घोड़े के दांत थे या जंगली गधों के।")
]:
    s3_mastery_hin.append({"type": "Case Study", "q": q, "sol": sol})

# Teach Concept (3)
for q, sol in [
    ("Explain the concept of 'Zooarchaeology' and its role in reconstructing ancient subsistence.", "Zooarchaeology is the study of animal remains from archaeological sites to reconstruct past human diets, economies, animal domestication processes, and local environments."),
    ("Describe how bone cut-mark analysis under a Scanning Electron Microscope (SEM) works.", "SEM analysis scans bone surfaces to inspect the microscopic geometry of cuts; clean V-grooves with striations verify the use of sharp metal (bronze) butchery knives."),
    ("Explain the historical significance of the 'Horse Debate' in the transition from Harappan to Vedic culture.", "The horse is a cultural marker; its absolute absence in Harappan iconography and heavy presence in Vedic texts shows that Mature Harappan cities were culturally and chronologically separate from Rigvedic society.")
]:
    s3_mastery_eng.append({"type": "Teach Concept", "q": q, "sol": sol})

for q, sol in [
    ("प्राणि-पुरातत्व (Zooarchaeology) की अवधारणा और प्राचीन इतिहास के पुनर्निर्माण में इसकी भूमिका स्पष्ट करें।", "यह पुरातात्विक खुदाई से मिले जानवरों के अवशेषों (हड्डियों, दांतों, शंखों) का अध्ययन करने वाला विज्ञान है, जो प्राचीन भोजन, पशुपालन और पर्यावरण को समझने में मदद करता है।"),
    ("स्कैनिंग इलेक्ट्रॉन माइक्रोस्कोप (SEM) के तहत हड्डियों पर कटने के निशानों के विश्लेषण की अवधारणा को समझाएं।", "SEM तकनीक हड्डी की सतह को स्कैन करके कट के सूक्ष्म आकार की जांच करती है; तांबे/कांसे के औजारों द्वारा बनाए गए स्पष्ट V-आकार के कट कसाईखाने के कार्य की पुष्टि करते हैं।"),
    ("हड़प्पा से वैदिक संस्कृति के संक्रमण में 'घोड़े के विवाद' के ऐतिहासिक महत्व को समझाएं।", "घोड़ा एक सांस्कृतिक सूचक है; हड़प्पा मुहरों पर इसका न होना और ऋग्वेद में इसका अत्यधिक महत्व होना यह दर्शाता है कि हड़प्पा सभ्यता और वैदिक समाज दो अलग-अलग सांस्कृतिक चरणों का प्रतिनिधित्व करते हैं।")
]:
    s3_mastery_hin.append({"type": "Teach Concept", "q": q, "sol": sol})

# =========================================================================
# DATABASE INJECTION LOGIC
# =========================================================================

def inject_mastery(filepath, s1_list, s2_list, s3_list, name):
    print(f"\nInjecting mastery questions into {name} ({filepath})...")
    if not os.path.exists(filepath):
        print(f"ERROR: File {filepath} not found!")
        return False
        
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        sections = data["deepDive"]["sections"]
        if len(sections) != 3:
            print(f"ERROR: Expected 3 sections, found {len(sections)}")
            return False
            
        # Assign
        sections[0]["masteryZone"] = s1_list
        sections[1]["masteryZone"] = s2_list
        sections[2]["masteryZone"] = s3_list
        
        # Save back
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
        print(f"Injected counts for {name}:")
        print(f"  - Section 1: {len(sections[0]['masteryZone'])}")
        print(f"  - Section 2: {len(sections[1]['masteryZone'])}")
        print(f"  - Section 3: {len(sections[2]['masteryZone'])}")
        return True
    except Exception as e:
        print(f"ERROR during injection: {e}")
        return False

# Trigger injection
v_eng = inject_mastery(ENG_PATH, s1_mastery_eng, s2_mastery_eng, s3_mastery_eng, "English")
v_hin = inject_mastery(HIN_PATH, s1_mastery_hin, s2_mastery_hin, s3_mastery_hin, "Hindi")

if v_eng and v_hin:
    print("\nMastery questions injection complete for both languages!")
else:
    print("\nMastery injection failed!")
