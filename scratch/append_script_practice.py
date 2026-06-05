import json
import os

ENG_PATH = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\HarappanIndus-Valley-Civilisation\Script-and-Language\content.json"
HIN_PATH = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\HarappanIndus-Valley-Civilisation\Script-and-Language\hi\content.json"

additional_eng = [
    (
        "Consider the following statements regarding the geographical distribution of Harappan writing:\n1. Script symbols are discovered as far as Shortughai in Badakhshan, Afghanistan.\n2. Inscribed pottery fragments have also been recovered from Ras al-Jinz in Oman, proving maritime trade links.\n3. No Harappan script has ever been found outside the geographical borders of modern India and Pakistan.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: Harappan inscriptions have been found in Afghanistan (Shortughai), Oman (Ras al-Jinz), and Mesopotamia (Ur, Kish)."
    ),
    (
        "With reference to the relationship between the Indus script and administrative control, consider the following statements:\n1. The standardization of sign shapes across distant cities indicates central administrative oversight.\n2. The disappearance of writing coincides precisely with the collapse of mature urban municipal bodies.\n3. Writing was utilized to record detailed treaties between the Citadel elites and rural chieftains.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "2 only", "1 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: because the script is undeciphered, we have no evidence of written treaties or political documents."
    ),
    (
        "Consider the following statements regarding the rebus writing technique:\n1. Rebus writing uses pictographic representations of concrete objects to denote homophones with abstract meanings.\n2. This technique was also a key step in the development of ancient Egyptian and Sumerian scripts.\n3. Rebus writing has been completely ruled out by all scholars analyzing the Harappan script.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: rebus writing is the primary method used by scholars like Asko Parpola to propose readings for the script."
    ),
    (
        "With reference to the language family of the Harappan Civilisation, consider the following statements:\n1. The Austroasiatic (Munda) family is connected to the Indus Valley through prehistoric substrate influences.\n2. The Indo-Aryan Sanskrit model requires reading the signs alphabetically from left to right.\n3. The Proto-Dravidian hypothesis remains the most archaeologically and geographically plausible theory.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All three statements are correct, describing the key arguments and structures of the Munda, Indo-Aryan, and Dravidian linguistic models."
    ),
    (
        "Consider the following statements regarding the Dholavira Signboard's physical construction:\n1. Each of the ten symbols was carved from natural white gypsum paste.\n2. The gypsum symbols were inlaid into a large wooden board that hung over the Citadel gate.\n3. The letters were coated with gold leaf to make them shine under sunlight.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: there is no archaeological evidence of gold leaf coatings on the Dholavira signboard letters."
    ),
    (
        "With reference to the script symbols representing numbers, consider the following statements:\n1. Scribes represented numbers using simple vertical strokes or bars.\n2. The number strokes are often grouped together to represent units and tens.\n3. Number signs are frequently placed before U-shaped or jar-shaped symbols.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, describing number representation, grouping of strokes, and placement before jar symbols."
    ),
    (
        "Consider the following statements regarding the Boustrophedon writing layout:\n1. It allowed the reader to read continuously without moving their eyes back to the start margin.\n2. Scribes curved the shapes of the boundary signs to transition between lines.\n3. It was exclusively reserved for public signboards and was never used on seals.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: Boustrophedon is found on longer inscriptions on seals and potsherds, while the Dholavira signboard is a single line."
    ),
    (
        "With reference to the decipherment attempts of John Marshall, consider the following statements:\n1. John Marshall officially declared the script undeciphered during his excavations in the 1920s.\n2. He suggested a tentative connection to early Dravidian language families.\n3. Marshall argued that the script was imported directly from Egypt during the Old Kingdom.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "2 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: John Marshall did not suggest the script was imported from Egypt; he recognized its indigenous origin."
    ),
    (
        "Consider the following statements regarding the fish symbol reading in astronomic calendars:\n1. Parpola interpreted the fish sign with a roof as Venus, associated with the Dravidian word for white.\n2. Scribes placed the fish symbol adjacent to deity figures on seals to denote astral protection.\n3. The fish symbol is completely absent on copper tablets found at Harappa.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: the fish symbol is present on various copper tablets from both Harappa and Mohenjo-daro."
    ),
    (
        "With reference to the post-urban script usage (Late Harappan phase), consider the following statements:\n1. Inscriptions became rare and signs simplified, losing their pictorial clarity.\n2. The use of elaborate steatite seals with animal reliefs ceased entirely.\n3. Graffiti on pottery survived as the last remnants of the writing system before its demise.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, describing the simplification of signs, cessation of steatite seals, and survival of pottery graffiti in the Late Harappan phase."
    )
]

additional_hin = [
    (
        "हड़प्पा लेखन के भौगोलिक वितरण के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. लिपि के प्रतीक अफगानिस्तान के बदख्शां में स्थित शोर्तुघई तक खोजे गए हैं।\n2. ओमान के रास अल-जिंज से भी उत्कीर्ण बर्तनों के टुकड़े मिले हैं, जो समुद्री व्यापारिक संबंधों को सिद्ध करते हैं।\n3. आधुनिक भारत और पाकिस्तान की भौगोलिक सीमाओं के बाहर कभी कोई हड़प्पा लिपि नहीं पाई गई है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: हड़प्पा के अभिलेख अफगानिस्तान (शोरतूघई), ओमान (रास अल-जिंज) और मेसोपोटामिया (उर, किश) में मिले हैं।"
    ),
    (
        "सिंधु लिपि और प्रशासनिक नियंत्रण के बीच संबंध के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. दूरदराज के शहरों में अक्षरों के आकारों का मानकीकरण केंद्रीय प्रशासनिक नियंत्रण की ओर इशारा करता है।\n2. लेखन का लुप्त होना परिपक्व शहरी नागरिक निकायों के पतन के साथ ठीक मेल खाता है।\n3. किले के शासकों और ग्रामीण सरदारों के बीच विस्तृत संधियों को रिकॉर्ड करने के लिए लेखन का उपयोग किया जाता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 2", "केवल 1 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: चूंकि लिपि अपठित है, इसलिए हमारे पास लिखित संधियों या राजनीतिक दस्तावेजों का कोई साक्ष्य नहीं है।"
    ),
    (
        "रीबस (rebus) लेखन तकनीक के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. रीबस लेखन अमूर्त अर्थों वाले समध्वनि शब्दों को दर्शाने के लिए ठोस वस्तुओं के चित्रों का उपयोग करता है।\n2. यह तकनीक प्राचीन मिस्र और सुमेरियन लिपियों के विकास में भी एक महत्वपूर्ण चरण थी।\n3. हड़प्पा लिपि का विश्लेषण करने वाले सभी विद्वानों द्वारा रीबस लेखन को पूरी तरह से खारिज कर दिया गया है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: रीबस पद्धति आस्को पारपोला जैसे विद्वानों द्वारा लिपि के अनुवाद का मुख्य आधार है।"
    ),
    (
        "हड़प्पा सभ्यता के भाषा परिवार के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. ऑस्ट्रो-एशियाई (मुंडा) परिवार प्रागैतिहासिक सबस्ट्रेट प्रभावों के माध्यम से सिंधु घाटी से जुड़ा हुआ है।\n2. भारत-आर्य संस्कृत मॉडल के तहत चिन्हों को बाएं से दाएं वर्णमाला के रूप में पढ़ना आवश्यक होता है।\n3. आदि-द्रविड़ परिकल्पना पुरातात्विक और भौगोलिक रूप से सबसे प्रशंसनीय सिद्धांत बनी हुई है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो मुंडा, भारत-आर्य और द्रविड़ भाषाई सिद्धांतों के मूल तर्कों का वर्णन करते हैं।"
    ),
    (
        "धोलावीरा सूचना-पट्ट की भौतिक बनावट के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. दस प्रतीकों में से प्रत्येक को प्राकृतिक सफेद जिप्सम लेप से तराशा गया था।\n2. जिप्सम प्रतीकों को एक बड़े लकड़ी के बोर्ड में जड़ा गया था जो किले के गेट के ऊपर लटका हुआ था।\n3. धूप में चमकाने के लिए अक्षरों पर सोने की पत्ती (gold leaf) की परत चढ़ाई गई थी।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: धोलावीरा सूचना-पट्ट के अक्षरों पर सोने की परत होने का कोई पुरातात्विक साक्ष्य नहीं मिला है।"
    ),
    (
        "संख्याओं को दर्शाने वाले लिपि प्रतीकों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. लेखक संख्याओं को सरल लंबवत रेखाओं (strokes) या छड़ों से प्रदर्शित करते थे।\n2. इकाई और दहाई को दर्शाने के लिए इन रेखाओं को अक्सर एक साथ समूहीकृत किया जाता था।\n3. संख्या चिन्हों को अक्सर यू-आकार (U-shaped) या जार के आकार के प्रतीकों से पहले रखा जाता था।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "Clean 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो संख्या प्रदर्शन, स्ट्रोक के समूह और जार प्रतीकों से पहले उनकी स्थिति का वर्णन करते हैं।"
    ),
    (
        "बोउस्ट्रोफेडन लेखन लेआउट के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. इसने पाठक को लगातार पढ़ने की सुविधा दी, बिना उसकी आँखों को वापस शुरुआत के किनारे पर ले जाए।\n2. पंक्तियों के बीच परिवर्तन करने के लिए लेखक सीमा चिन्हों के आकारों को मोड़ देते थे।\n3. यह विशेष रूप से सार्वजनिक सूचना-पट्टों के लिए आरक्षित था और मुहरों पर इसका कभी उपयोग नहीं किया गया।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["Clean 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: बोउस्ट्रोफेडन मुहरों और बर्तनों के लंबे लेखों में मिलता है, जबकि धोलावीरा बोर्ड केवल एक पंक्ति का लेख है।"
    ),
    (
        "जॉन मार्शल के लिपि को पढ़ने के प्रयासों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. जॉन मार्शल ने 1920 के दशक में अपने उत्खनन के दौरान लिपि को आधिकारिक रूप से अपठित घोषित किया था।\n2. उन्होंने प्रारंभिक द्रविड़ भाषा परिवारों के साथ एक संभावित संबंध का सुझाव दिया था।\n3. मार्शल ने तर्क दिया कि यह लिपि पुरानी साम्राज्य (Old Kingdom) के दौरान सीधे मिस्र से आयात की गई थी।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 2", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: जॉन मार्शल ने लिपि को मिस्र से आयातित नहीं माना; उन्होंने इसकी स्थानीय उत्पत्ति को स्वीकार किया था।"
    ),
    (
        "खगोलीय पंचांगों में मछली के चिन्ह के अनुवाद के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. पारपोला ने ऊपर छत वाले मछली के चिन्ह को शुक्र (Venus) के रूप में पढ़ा, जो द्रविड़ में सफेद शब्द से जुड़ा है।\n2. खगोलीय सुरक्षा दर्शाने के लिए लेखकों ने मुहरों पर देवताओं के चित्रों के बगल में मछली का प्रतीक रखा।\n3. हड़प्पा से प्राप्त तांबे की पट्टियों पर मछली का प्रतीक पूरी तरह से अनुपस्थित है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: मछली का प्रतीक हड़प्पा और मोहनजोदड़ो दोनों से प्राप्त तांबे की पट्टियों पर मिलता है।"
    ),
    (
        "शहरीकरण के बाद के चरण (उत्तर-हड़प्पा काल) में लिपि के उपयोग के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. अभिलेख दुर्लभ हो गए और चिन्ह सरल हो गए, जिससे उनकी चित्रात्मक स्पष्टता खो गई।\n2. जानवरों के चित्रों वाली अलंकृत सेलखड़ी मुहरों का उपयोग पूरी तरह से बंद हो गया।\n3. लिपि के पूरी तरह लुप्त होने से पहले बर्तनों पर भित्तिचित्र (graffiti) इसके अंतिम अवशेष के रूप में बचे रहे।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो उत्तर-हड़प्पा काल में चिन्हों के सरलीकरण, मुहरों के बंद होने और बर्तनों पर भित्तिचित्रों के बचने का वर्णन करते हैं।"
    )
]

# Append English
if os.path.exists(ENG_PATH):
    with open(ENG_PATH, "r", encoding="utf-8") as f:
        eng_data = json.load(f)
    
    # We append the 10 additional questions
    current_count = len(eng_data.get("practiceQuestions", []))
    print(f"Current English practice questions count: {current_count}")
    
    for q, opts, ans, sol in additional_eng:
        eng_data["practiceQuestions"].append({
            "q": q,
            "opts": opts,
            "ans": ans,
            "sol": sol
        })
    
    with open(ENG_PATH, "w", encoding="utf-8") as f:
        json.dump(eng_data, f, ensure_ascii=False, indent=2)
    print(f"New English practice questions count: {len(eng_data['practiceQuestions'])}")

# Append Hindi
if os.path.exists(HIN_PATH):
    with open(HIN_PATH, "r", encoding="utf-8") as f:
        hin_data = json.load(f)
    
    current_count = len(hin_data.get("practiceQuestions", []))
    print(f"Current Hindi practice questions count: {current_count}")
    
    for q, opts, ans, sol in additional_hin:
        hin_data["practiceQuestions"].append({
            "q": q,
            "opts": opts,
            "ans": ans,
            "sol": sol
        })
    
    with open(HIN_PATH, "w", encoding="utf-8") as f:
        json.dump(hin_data, f, ensure_ascii=False, indent=2)
    print(f"New Hindi practice questions count: {len(hin_data['practiceQuestions'])}")
