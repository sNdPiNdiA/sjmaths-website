import json
import os

ENG_PATH = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\HarappanIndus-Valley-Civilisation\Weights-and-Measures\content.json"
HIN_PATH = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\HarappanIndus-Valley-Civilisation\Weights-and-Measures\hi\content.json"

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

# =========================================================================
# SECTION 1: THE STANDARDIZED WEIGHT SYSTEM (BINARY VS DECIMAL)
# =========================================================================
s1_mastery_eng = []
s1_mastery_hin = []

# MCQ (5)
for q, opts, ans, sol in [
    ("Which material was most extensively utilized for manufacturing standard Harappan weights?", ["Rohri Chert", "Banded Agate", "Steatite", "Lapis Lazuli"], 0, "Chert (Rohri chert) was the primary raw material used for standard cubical weights."),
    ("The base unit ratio of 16 in the Harappan binary weight system corresponds to which absolute weight?", ["13.63 grams", "27.26 grams", "8.60 grams", "2.80 grams"], 0, "The base standard unit of 16 corresponds to approximately 13.63 grams."),
    ("Which of the following statements is true regarding the design of standard Harappan chert weights?", ["They are plain and bear no inscriptions", "They feature animal relief carvings", "They are inscribed with names of traders", "They have numerical values carved on them"], 0, "Harappan weights are completely plain and undecorated, bearing no carvings or script."),
    ("The lower values in the Harappan weight system followed which mathematical ratio pattern?", ["Binary system of doubling", "Sexagesimal system", "Pure decimal system", "Duodecimal system"], 0, "Lower denominations followed a binary system (1, 2, 4, 8, 16, 32, 64)."),
    ("At which workshops were tiny agate and jasper weights primarily excavated?", ["Bead-making workshops", "Bronze smelting furnaces", "Pottery kiln sites", "Brick-making pits"], 0, "Tiny agate and jasper weights were used in bead-making and gold workshops (Lothal, Chanhudaro) to measure luxury materials.")
]:
    s1_mastery_eng.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("हड़प्पा के मानक बाटों के निर्माण के लिए किस सामग्री का सर्वाधिक उपयोग किया जाता था?", ["रोहरी चर्ट", "धारीदार अगेट", "सेलखड़ी", "लाजवर्त"], 0, "चर्ट (रोहरी चर्ट) मानक घनाकार बाटों के लिए मुख्य रूप से उपयोग किया जाता था।"),
    ("हड़प्पा की बाइनरी बाट प्रणाली में 16 अनुपात की मूल इकाई का वास्तविक वजन कितना था?", ["13.63 ग्राम", "27.26 ग्राम", "8.60 ग्राम", "2.80 ग्राम"], 0, "तौल की मुख्य मानक इकाई 16 का वजन लगभग 13.63 ग्राम था।"),
    ("हड़प्पा के चर्ट बाटों के डिजाइन के संबंध में निम्नलिखित में से कौन सा कथन सही है?", ["वे सादे हैं और उन पर कोई लेख नहीं है", "उन पर जानवरों की आकृतियां खुदी हैं", "उन पर व्यापारियों के नाम अंकित हैं", "उन पर संख्यात्मक मूल्य खुदे हैं"], 0, "हड़प्पा के बाट पूरी तरह से सादे और बिना किसी लिपि या चित्र के होते थे।"),
    ("हड़प्पा बाट प्रणाली के निचले मान किस गणितीय अनुपात का पालन करते थे?", ["द्विआधारी (बाइनरी) प्रणाली", "षष्ठदशमलव प्रणाली", "दशमलव प्रणाली", "द्वादशमलव प्रणाली"], 0, "निचले मान बाइनरी प्रणाली (1, 2, 4, 8, 16, 32, 64) का पालन करते थे।"),
    ("अगेट और जैस्पर के अत्यंत सूक्ष्म बाट मुख्य रूप से कहाँ से खोदे गए हैं?", ["मनके बनाने की कार्यशालाओं से", "कांसा गलाने की भट्टियों से", "मिट्टी के बर्तनों के भट्ठों से", "ईंट बनाने वाले गड्डों से"], 0, "मनके बनाने और सोने के कारखानों (लोथल, चन्हुदड़ो) से सूक्ष्म बाट रत्नों को तोलने के लिए मिले हैं।")
]:
    s1_mastery_hin.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# Multiple Correct MCQ (5)
for q, opts, ans, sol in [
    ("Select the raw materials documented as being used to manufacture Harappan weights: (Select all that apply)", ["Chert", "Agate", "Jasper", "Iron"], [0, 1, 2], "Chert, agate, and jasper were used. Iron was unknown in the Bronze Age."),
    ("Which of the following denominations belong to the binary range of the weight system? (Select all that apply)", ["1", "8", "32", "160"], [0, 1, 2], "The binary values are 1, 2, 4, 8, 16, 32, 64. 160 is decimal."),
    ("Choose the correct characteristics of standard Harappan weights: (Select all that apply)", ["Cubical shape", "Rohri chert material", "Plain, un-engraved surfaces", "Short script labels"], [0, 1, 2], "Weights were cubical, Rohri chert, and plain without any script."),
    ("Select the sites where tiny micro-weights (under 1g) have been excavated: (Select all that apply)", ["Lothal", "Chanhudaro", "Mohenjo-daro", "Sutkagendor"], [0, 1, 2], "Micro-weights are documented at major urban and craft hubs (Lothal, Chanhudaro, Mohenjo-daro)."),
    ("Which mathematical systems were integrated within the Harappan weight system? (Select all that apply)", ["Binary", "Decimal", "Vigesimal", "Duodecimal"], [0, 1], "The Harappans integrated a dual binary and decimal weight system.")
]:
    s1_mastery_eng.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("हड़प्पा बाटों के निर्माण में प्रयुक्त होने वाली सामग्रियों को चुनें: (सभी सही विकल्प चुनें)", ["चर्ट", "अगेट", "जैस्पर", "लोहा"], [0, 1, 2], "चर्ट, अगेट और जैस्पर का उपयोग होता था। लोहे का ज्ञान हड़प्पा वासियों को नहीं था।"),
    ("निम्नलिखित में से कौन से मान बाट प्रणाली के बाइनरी (द्विआधारी) वर्ग में आते हैं? (सभी सही विकल्प चुनें)", ["1", "8", "32", "160"], [0, 1, 2], "बाइनरी मान 1, 2, 4, 8, 16, 32, 64 हैं। 160 दशमलव मान है।"),
    ("हड़प्पा बाटों की सही विशेषताओं का चयन करें: (सभी सही विकल्प चुनें)", ["घनाकार आकृति", "रोहरी चर्ट पत्थर", "सादी, बिना नक्काशीदार सतह", "लघु लिपि संकेत"], [0, 1, 2], "हड़प्पा के बाट घनाकार, चर्ट पत्थर के और बिना किसी लिपि के सादे होते थे।"),
    ("उन स्थलों को चुनें जहाँ से 1 ग्राम से कम वजन के सूक्ष्म बाट मिले हैं: (सभी सही विकल्प चुनें)", ["लोथल", "चन्हुदड़ो", "मोहनजोदड़ो", "सुत्कागेंदोर"], [0, 1, 2], "सूक्ष्म बाट प्रमुख शिल्प केंद्रों (लोथल, चन्हुदड़ो, मोहनजोदड़ो) से प्राप्त हुए हैं।"),
    ("हड़प्पा बाट प्रणाली में किन गणितीय प्रणालियों का समन्वय किया गया था? (सभी सही विकल्प चुनें)", ["द्विआधारी (बाइनरी)", "दशमलव (Decimal)", "विंशतीय (Vigesimal)", "द्वादशमलव (Duodecimal)"], [0, 1], "हड़प्पा बाट प्रणाली में बाइनरी और दशमलव दोनों प्रणालियों का समन्वय किया गया था।")
]:
    s1_mastery_hin.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# True/False (8)
for q, ans, sol in [
    ("The Rohri hills in Sindh were a major quarrying center for chert weights.", True, "Rohri hills provided the primary high-grade chert source."),
    ("Every single Harappan weight is inscribed with its numeric denomination.", False, "Weights carry no script or numbers; they are completely plain."),
    ("The base weight ratio of 16 corresponds to 28.6 grams.", False, "It corresponds to approximately 13.63 grams."),
    ("Banded agate was preferred for large bulk weights in state granaries.", False, "Agate was used for tiny, precise weights; large ones were limestone/slate."),
    ("The higher ranges of Harappan weights followed a decimal system.", True, "Higher values shifted to decimal patterns (160, 200, 320, 640, etc.)."),
    ("Copper and bronze balance pans with suspension holes have been found.", True, "Excavations have yielded copper-alloy pans from balance scales."),
    ("Standard chert weights are found only in the citadel area of cities.", False, "Weights are found in both citadels and lower town residential houses."),
    ("The Harappan weight standard was completely forgotten after 1900 BCE.", False, "The base-16 binary ratio survived in historical Indian systems (Annas).")
]:
    s1_mastery_eng.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("सिंध में रोहरी की पहाड़ियाँ चर्ट बाटों के लिए मुख्य खनन केंद्र थीं।", True, "रोहरी की पहाड़ियाँ उच्च श्रेणी के चर्ट पत्थर का मुख्य स्रोत थीं।"),
    ("प्रत्येक हड़प्पा बाट पर उसका संख्यात्मक मूल्य अंकित होता था।", False, "बाट पूरी तरह से सादे थे, उन पर कोई मूल्य अंकित नहीं था।"),
    ("बाट अनुपात 16 की मूल इकाई 28.6 ग्राम के बराबर थी।", False, "यह लगभग 13.63 ग्राम के बराबर थी।"),
    ("अनाज गोदामों के बड़े बाटों के लिए धारीदार अगेट को प्राथमिकता दी जाती थी।", False, "अगेट का उपयोग छोटे बाटों में होता था; बड़े बाट चूना पत्थर के थे।"),
    ("हड़प्पा बाटों की उच्च श्रृंखलाएँ दशमलव प्रणाली का पालन करती थीं।", True, "उच्च मान दशमलव प्रणाली (160, 200, 320, 640 आदि) का पालन करते थे।"),
    ("लटकाने के छेदों वाले तांबे और कांसे के तराजू के पलड़े मिले हैं।", True, "उत्खनन से तांबे और कांसे के गोल तराजू पलड़े मिले हैं।"),
    ("मानक चर्ट बाट केवल शहरों के दुर्ग (citadel) क्षेत्र से मिले हैं।", False, "बाट निचले शहर और दुर्ग दोनों क्षेत्रों से प्राप्त हुए हैं।"),
    ("हड़प्पा बाट प्रणाली 1900 ईसा पूर्व के बाद पूरी तरह से लुप्त हो गई थी।", False, "बाइनरी 16 का आधार बाद में पारंपरिक 'आने' प्रणाली में जीवित रहा।")
]:
    s1_mastery_hin.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

# Fill in the Blank (8)
for q, ans, sol in [
    ("The primary stone used to manufacture Harappan weights was ________.", "chert", "Rohri chert was the dominant material for cubical weights."),
    ("The base weight of 13.63 grams corresponds to the binary ratio of ________.", "16", "The ratio of 16 is the standard base unit of about 13.63 grams."),
    ("Higher denominations of weights followed a ________ mathematical system.", "decimal", "Values above ratio 64 shifted to the decimal system."),
    ("Tiny agate weights were used to weigh gold, silver, and ________.", "beads", "Micro-weights measured precious metals and stone beads."),
    ("The Rohri quarries that supplied weight materials are located in ________.", "Sindh", "Rohri hills are a key geological feature in Sindh."),
    ("Harappan weights are characterized by a complete absence of ________ or script.", "carvings", "Weights are plain without carvings or markings."),
    ("Copper and bronze pans were suspended by strings to form ________ scales.", "balance", "Suspended pans formed classic balance weighing scales."),
    ("The binary ratio of 16 survived until 1957 in the division of the ________.", "Rupee", "1 Rupee was divided into 16 Annas until decimalization in 1957.")
]:
    s1_mastery_eng.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("हड़प्पा बाटों के निर्माण के लिए प्रयुक्त होने वाला प्राथमिक पत्थर ________ था।", "चर्ट", "रोहरी चर्ट घनाकार बाटों का मुख्य पत्थर था।"),
    ("13.63 ग्राम का वास्तविक भार बाइनरी अनुपात ________ के बराबर होता था।", "16", "16 अनुपात की इकाई 13.63 ग्राम के बराबर होती थी।"),
    ("बाटों के उच्च मानों में ________ गणितीय प्रणाली का अनुसरण किया जाता था।", "दशमलव", "64 से ऊपर के बाट दशमलव प्रणाली के अंतर्गत आते थे।"),
    ("अगेट के छोटे बाटों का उपयोग सोना, चांदी और ________ तोलने के लिए होता था।", "मनके", "सूक्ष्म बाटों का उपयोग कीमती धातुओं और मनकों के लिए होता था।"),
    ("चर्ट प्रदान करने वाली प्रसिद्ध रोहरी खदानें ________ प्रांत में स्थित हैं।", "सिंध", "रोहरी पहाड़ियाँ सिंध (पाकिस्तान) में स्थित हैं।"),
    ("हड़प्पा बाटों पर किसी भी प्रकार के ________ या चित्र का पूर्ण अभाव होता था।", "अंकन", "बाटों पर कोई अंकन, नक्काशी या लिपि नहीं होती थी।"),
    ("रस्सियों की सहायता से लटकाए गए पलड़े मिलकर ________ तराजू बनाते थे।", "संतुलन", "धागे से लटके धातु के पलड़े संतुलन तराजू बनाते थे।"),
    ("बाइनरी 16 का अनुपात 1957 तक ________ के 16 आने के विभाजन में जीवित रहा।", "रुपये", "1 रुपया = 16 आने की प्रणाली 1957 तक भारत में लागू थी।")
]:
    s1_mastery_hin.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

# Match the Following (3)
s1_matches_eng = [
    {"q": "Match the weight denomination ratios with their mathematical classification:",
     "pairs": ["Ratio 1 - Binary range", "Ratio 16 - Base standard unit", "Ratio 160 - Decimal range", "Ratio 12800 - Maximum decimal limit"],
     "sol": "Ratios 1 and 16 belong to the binary range; 16 is the base standard unit; 160 and 12800 represent the decimal range."},
    {"q": "Match the material with the category of weights manufactured:",
     "pairs": ["Rohri Chert - Standard cubical weights", "Banded Agate - Micro-weights for gold and beads", "Limestone - Heavy bulk-cargo weights", "Steatite - Rare experimental weights"],
     "sol": "Standard weights were chert; agate was used for micro-weights; limestone for large heavy cargo weights; steatite for rare specimens."},
    {"q": "Match the weight value characteristics with their absolute measures:",
     "pairs": ["Base standard unit ratio - 13.63 grams", "Smallest binary unit ratio - 0.86 grams", "Large warehouse weight - 10+ kilograms", "Mesopotamian trade equivalent - Dilmun standard"],
     "sol": "Base standard unit is 13.63g; smallest unit is 0.86g; bulk weights exceed 10kg; Dilmun standard adopted Harappan standards."}
]
s1_mastery_eng.extend([make_match_question(m) for m in s1_matches_eng])

s1_matches_hin = [
    {"q": "बाट के अनुपात मूल्यों को उनके गणितीय वर्गीकरण से सुमेलित करें:",
     "pairs": ["अनुपात 1 - बाइनरी सीमा", "अनुपात 16 - मानक आधार इकाई", "अनुपात 160 - दशमलव सीमा", "अनुपात 12800 - अधिकतम दशमलव सीमा"],
     "sol": "अनुपात 1 और 16 बाइनरी सीमा में हैं, 16 मुख्य आधार इकाई है; 160 और 12800 दशमलव सीमा में हैं।"},
    {"q": "निर्माण सामग्री को बाटों की श्रेणियों से सुमेलित करें:",
     "pairs": ["रोहरी चर्ट - मानक घनाकार बाट", "धारीदार अगेट - सोने-मनकों के सूक्ष्म बाट", "चूना पत्थर - भारी थोक बाट", "सेलखड़ी - दुर्लभ प्रयोगात्मक बाट"],
     "sol": "मानक बाट चर्ट के; सूक्ष्म बाट अगेट के; थोक बाट चूना पत्थर के और प्रयोगात्मक बाट सेलखड़ी के बनते थे।"},
    {"q": "वजन मान की विशेषताओं को उनके वास्तविक वजनों से सुमेलित करें:",
     "pairs": ["आधार मानक अनुपात - 13.63 ग्राम", "न्यूनतम बाइनरी अनुपात - 0.86 ग्राम", "गोदामों के बड़े बाट - 10 किलोग्राम से अधिक", "खाड़ी व्यापारिक समकक्ष - दिलमुन मानक"],
     "sol": "आधार मानक 13.63 ग्राम है; न्यूनतम बाट 0.86 ग्राम का था; बड़े बाट 10 किलोग्राम से अधिक के थे; खाड़ी व्यापार में दिलमुन मानक हड़प्पा के समान था।"}
]
s1_mastery_hin.extend([make_match_question(m) for m in s1_matches_hin])

# One-Liner (8)
for q, sol in [
    ("What geological site was the primary quarrying source for Harappan chert weights?", "The Rohri hills in Sindh, Pakistan."),
    ("Why did the Harappans avoid carving script on their weights?", "Weights required absolute standardization in mass; carving script or relief details would alter the physical weight of the stones."),
    ("What was the absolute weight in grams of the binary unit '1' in the Harappan system?", "Approximately 0.86 grams (representing 1/16th of the base unit of 13.63g)."),
    ("Which trade items required the use of small agate weights?", "Precious metals (gold, silver) and beads made of carnelian, jasper, and lapis lazuli."),
    ("How many Annas made up 1 Rupee in the pre-1957 traditional Indian currency system?", "16 Annas."),
    ("Which mathematical system regulated the weighing of bulk agricultural grain?", "The decimal system (ratios of 160, 200, 320, 640, etc.)."),
    ("What is the general shape of standard Rohri chert weights?", "Cubical or cubic shape."),
    ("What tool was used along with weights to determine trade value?", "A balance scale consisting of copper-alloy or clay pans suspended by cords.")
]:
    s1_mastery_eng.append({"type": "One-Liner", "q": q, "sol": sol})

for q, sol in [
    ("हड़प्पा चर्ट बाटों के लिए मुख्य खनन स्रोत कौन सा भूवैज्ञानिक स्थल था?", "पाकिस्तान के सिंध प्रांत में स्थित रोहरी की पहाड़ियाँ।"),
    ("हड़प्पा वासियों ने अपने बाटों पर लिपि या नक्काशी करने से क्यों परहेज किया?", "द्रव्यमान की पूर्ण सटीकता बनाए रखने के लिए; नक्काशी करने से पत्थर का वास्तविक वजन बदल सकता था।"),
    ("हड़प्पा प्रणाली में बाइनरी इकाई '1' का वास्तविक वजन ग्राम में कितना था?", "लगभग 0.86 ग्राम (जो कि 13.63 ग्राम की आधार इकाई का 1/16वां हिस्सा था)।"),
    ("किन व्यापारिक वस्तुओं के लिए अगेट के छोटे बाटों का उपयोग किया जाता था?", "कीमती धातुओं (सोने-चांदी) तथा कार्नेलियन, लाजवर्त और जैस्पर के मनकों के लिए।"),
    ("1957 से पहले की पारंपरिक भारतीय मुद्रा प्रणाली में 1 रुपये में कितने आने होते थे?", "16 आने।"),
    ("थोक कृषि अनाज को तोलने के लिए किस गणितीय प्रणाली का उपयोग किया जाता था?", "दशमलव प्रणाली (160, 200, 320, 640 आदि अनुपात)।"),
    ("मानक रोहरी चर्ट बाटों का सामान्य आकार क्या था?", "घनाकार (cubic) आकार।"),
    ("व्यापारिक मूल्य निर्धारित करने के लिए बाटों के साथ किस उपकरण का उपयोग होता था?", "संतुलन तराजू (balance scale) का, जिसमें धातु या मिट्टी के पलड़े धागे से बंधे होते थे।")
]:
    s1_mastery_hin.append({"type": "One-Liner", "q": q, "sol": sol})

# Assertion-Reason (8)
for q, ans, sol in [
    ("Assertion (A): Harappan weights are plain and lack any script or artistic carvings.\nReason (R): Carving script would remove stone material and alter the calibrated weight standards.", 0, "Both A and R are true, and R is the correct explanation. Calibrated weights required strict consistency, which engraving would compromise."),
    ("Assertion (A): The Harappan weight system was purely binary.\nReason (R): Ratios of 1, 2, 4, 8, 16, 32, and 64 were used for smaller weight measurements.", 3, "A is false because the system was dual (binary for lower, decimal for higher ranges); R is true."),
    ("Assertion (A): Chert sourced from the Rohri hills was highly prized for weights.\nReason (R): Rohri chert is dense, uniform, and resistant to wear, ensuring long-term weight accuracy.", 0, "Both A and R are true, and Rohri chert's durability explains why it was chosen for weight standards."),
    ("Assertion (A): Micro-weights are found in domestic craft blocks at Chanhudaro.\nReason (R): Chanhudaro was a major center for manufacturing carnelian beads and gold ornaments.", 0, "Both A and R are true, and the presence of luxury craft workshops explains the find of micro-weights."),
    ("Assertion (A): The binary base of 16 represents a structural legacy in Indian history.\nReason (R): Traditional Indian currency retained a 16-based division (1 Rupee = 16 Annas) until the metric shift in 1957.", 0, "Both A and R are true, and the anna division directly illustrates the survival of the binary base."),
    ("Assertion (A): Bulk warehouses at Mohenjo-daro utilized conical limestone weights.\nReason (R): Conical weights with pierced holes allowed ropes to be threaded for hoisting heavy loads.", 0, "Both A and R are true, and the hoisting capability explains why large warehouse weights were conical."),
    ("Assertion (A): Agate weights were reserved for local village markets.\nReason (R): Agate is a common, inexpensive river pebble found throughout the Indus plains.", 4, "Both A and R are false. Agate was a premium material used for luxury micro-weights in urban craft zones."),
    ("Assertion (A): Balance scale pans were made of terracotta as well as copper.\nReason (R): Clay pans provided a cheap and accessible weighing option for smaller retail merchants.", 0, "Both A and R are true, and the accessibility of clay explains why terracotta pans were manufactured.")
]:
    s1_mastery_eng.append({"type": "Assertion-Reason", "q": q, "opts": ar_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("कथन (A): हड़प्पा के बाट पूरी तरह से सादे हैं और उन पर कोई लिपि या नक्काशी नहीं मिलती।\nकारण (R): बाट पर नक्काशी करने से पत्थर घिस जाता, जिससे मापन का मानक द्रव्यमान बदल सकता था।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या है। नक्काशी से बाट का सटीक वजन प्रभावित हो सकता था।"),
    ("कथन (A): हड़प्पा की बाट प्रणाली पूरी तरह से द्विआधारी (बाइनरी) थी।\nकारण (R): छोटे मापों के लिए 1, 2, 4, 8, 16, 32 और 64 के अनुपातों का उपयोग किया जाता था।", 3, "A गलत है क्योंकि प्रणाली बाइनरी और दशमलव का मिश्रण थी; R सही है।"),
    ("कथन (A): रोहरी की पहाड़ियों से प्राप्त चर्ट पत्थर को बाटों के लिए बहुत पसंद किया जाता था।\nकारण (R): रोहरी चर्ट सघन, एकसमान और घिसावट प्रतिरोधी होता है, जिससे बाटों की दीर्घकालिक सटीकता बनी रहती थी।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या है।"),
    ("कथन (A): चन्हुदड़ो के घरेलू शिल्प खंडों से सूक्ष्म बाट (micro-weights) प्राप्त हुए हैं।\nकारण (R): चन्हुदड़ो कार्नेलियन मनकों और सोने के आभूषणों के निर्माण का एक प्रमुख केंद्र था।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या है।"),
    ("कथन (A): बाइनरी 16 का आधार भारतीय इतिहास में एक महत्वपूर्ण संरचनात्मक विरासत है।\nकारण (R): पारंपरिक भारतीय मुद्रा में 1957 में दशमलव प्रणाली अपनाने तक 1 रुपये को 16 आने में विभाजित किया जाता था।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या है।"),
    ("कथन (A): मोहनजोदड़ो के थोक गोदामों में चूना पत्थर के बड़े शंक्वाकार बाटों का उपयोग होता था।\nकारण (R): छेद वाले शंक्वाकार बाटों में रस्सियाँ पिरोकर भारी भार को आसानी से उठाया जा सकता था।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या है।"),
    ("कथन (A): अगेट (अकीक) के बाट ग्रामीण स्थानीय बाजारों के लिए आरक्षित होते थे।\nकारण (R): अगेट सिंधु के मैदानों में मिलने वाला एक बहुत ही सामान्य और सस्ता पत्थर है।", 4, "A और R दोनों गलत हैं। अगेट एक कीमती पत्थर था जिसके सूक्ष्म बाट शहरी विलासिता व्यापार के लिए बनते थे।"),
    ("कथन (A): तराजू के पलड़े तांबे के साथ-साथ पकी मिट्टी (terracotta) के भी बनाए जाते थे।\nकारण (R): मिट्टी के पलड़े छोटे खुदरा व्यापारियों के लिए एक सस्ता और सुलभ तौल साधन प्रदान करते थे।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या है।")
]:
    s1_mastery_hin.append({"type": "Assertion-Reason", "q": q, "opts": hin_ar_opts, "ans": ans, "sol": sol})

# Statement-Based (5)
for q, ans, sol in [
    ("Consider the following statements:\nStatement 1: Lower value Harappan weights followed a binary system based on the doubling ratio.\nStatement 2: The base unit value corresponding to ratio 16 was approximately 28.6 grams.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: the base unit was 13.63 grams, not 28.6 grams."),
    ("Consider the following statements:\nStatement 1: Chert weights were polished and left completely undecorated without markings.\nStatement 2: Conical weights often featured relief carvings of the Pashupati deity.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: weights had no carvings of deities or animals."),
    ("Consider the following statements:\nStatement 1: Agate was utilized to produce tiny weights used in bead and ornament trade.\nStatement 2: Agate is a microcrystalline quartz similar to Rohri chert.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct. Agate was used for micro-weights, and it is a type of chalcedony/quartz like chert."),
    ("Consider the following statements:\nStatement 1: Balance scale pans were made exclusively of copper.\nStatement 2: Excavated pans have holes showing they were hung using strings.\nWhich of the statements given above is/are correct?", 1, "Statement 2 is correct. Statement 1 is incorrect: pans were also made of terracotta."),
    ("Consider the following statements:\nStatement 1: The standard weights found at Lothal and Harappa share the exact same weight ratios.\nStatement 2: Small rural Harappan settlements did not have access to these standardized weights.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: standard weights are found in small rural villages too, showing wide integration.")
]:
    s1_mastery_eng.append({"type": "Statement-Based", "q": q, "opts": mcq_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: कम मूल्य वाले हड़प्पा बाट द्विआधारी (बाइनरी) प्रणाली पर आधारित थे।\nकथन 2: अनुपात 16 से संबंधित मूल वजन इकाई लगभग 28.6 ग्राम के बराबर थी।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि मानक आधार वजन 13.63 ग्राम था।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: चर्ट बाटों को चिकना चमकाया जाता था और उन पर कोई सजावट नहीं होती थी।\nकथन 2: शंक्वाकार बाटों पर अक्सर पशुपति देवता की आकृतियाँ खुदी होती थीं।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि बाटों पर देवताओं की कोई मूर्तियां नहीं होती थीं।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: विलासिता के सामानों के व्यापार में प्रयुक्त छोटे बाट अगेट (Agate) पत्थर से बनाए जाते थे।\nकथन 2: अगेट एक सूक्ष्म क्रिस्टलीय क्वार्ट्ज पत्थर है जो चर्ट के समान होता है।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 2, "दोनों कथन सही हैं। अगेट रत्नों के तौल के लिए होता था और यह भी एक प्रकार का सिलिका क्वार्ट्ज है।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: तराजू के पलड़े केवल तांबे की धातु से ही बनाए जाते थे।\nकथन 2: खुदाई से मिले पलड़ों में छेद बने हैं, जो दर्शाते हैं कि उन्हें धागे से लटकाया जाता था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 1, "कथन 2 सही है। कथन 1 गलत है क्योंकि पलड़े मिट्टी (terracotta) के भी बनते थे।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: लोथल और हड़प्पा से प्राप्त मानक बाटों का अनुपात भार बिल्कुल समान था।\nकथन 2: हड़प्पा की छोटी ग्रामीण बस्तियों में इन मानकीकृत बाटों की पहुँच नहीं थी।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि छोटे गाँवों से भी मानक बाट मिले हैं।")
]:
    s1_mastery_hin.append({"type": "Statement-Based", "q": q, "opts": hin_mcq_opts, "ans": ans, "sol": sol})

# Why (3)
for q, sol in [
    ("Why did the Harappans use Rohri chert as the primary material for standard weights?", "Rohri chert is highly durable, dense, and resistant to chipping and weathering, which ensured that weights retained their calibrated values over long periods of usage."),
    ("Why is the absence of carvings on Harappan weights considered a deliberate choice?", "Because any engraving or surface relief carving would remove stone material or create uneven wear, altering the absolute mass and compromising the strict standardization of the weight system."),
    ("Why did the weight system transition from binary to decimal in the higher denominations?", "The binary system was ideal for high-precision, small-scale weighing of precious commodities, while the decimal system simplified calculations for bulk commodities like grain and timber during trade bookkeeping.")
]:
    s1_mastery_eng.append({"type": "Why", "q": q, "sol": sol})

for q, sol in [
    ("हड़प्पा वासियों ने मानक बाटों के निर्माण के लिए रोहरी चर्ट को प्राथमिक सामग्री के रूप में क्यों चुना?", "रोहरी चर्ट अत्यंत कठोर, सघन और मौसमी बदलावों के प्रति प्रतिरोधी होता है, जिससे लंबे समय तक उपयोग के बाद भी बाटों का सटीक वजन नहीं बदलता था।"),
    ("हड़प्पा बाटों पर नक्काशी न होना एक जानबूझकर किया गया नीतिगत निर्णय क्यों माना जाता है?", "क्योंकि पत्थर पर कोई भी उत्कीर्णन या चित्रकारी करने से उसका पत्थर घिस जाता, जिससे बाट के वजन की सार्वभौमिक सटीकता प्रभावित हो सकती थी।"),
    ("उच्च मानों में तौल प्रणाली बाइनरी से दशमलव में क्यों बदल जाती थी?", "बाइनरी प्रणाली सोने-चांदी के सटीक माप के लिए सर्वोत्तम थी, जबकि दशमलव प्रणाली थोक अनाज और भारी वस्तुओं के व्यापारिक बहीखाते को सरल बनाती थी।")
]:
    s1_mastery_hin.append({"type": "Why", "q": q, "sol": sol})

# How (3)
for q, sol in [
    ("How did the Rohri quarry network support the pan-regional standardization of weights?", "By acting as a centralized extraction and primary shaping hub from which standardized chert cores were exported to urban centers like Mohenjo-daro for final finishing under municipal guidelines."),
    ("How did the binary weight system survive as a cultural legacy in historical India?", "It persisted in commercial calculations, notably through the division of the silver Rupee into 16 Annas and the weight measurement where 1 Seer equaled 16 Chhataks, which survived until 1957."),
    ("How did small bead workshops at Chanhudaro maintain high precision in weighing precious ornaments?", "By using specialized micro-weights made of agate or jasper (weighing down to 0.86g) combined with highly sensitive copper balance pans suspended by thin cords.")
]:
    s1_mastery_eng.append({"type": "How", "q": q, "sol": sol})

for q, sol in [
    ("रोहरी खदान नेटवर्क ने बाटों के अखिल-हड़प्पा मानकीकरण को कैसे सहयोग दिया?", "यह खनन और प्राथमिक छंटाई का केंद्रीय केंद्र था जहाँ से चर्ट कोर को मोहनजोदड़ो जैसे शहरों में भेजा जाता था, जहाँ नगर पालिकाओं के मानकों के तहत अंतिम पॉलिश की जाती थी।"),
    ("बाइनरी बाट प्रणाली भारतीय इतिहास में एक सांस्कृतिक विरासत के रूप में कैसे जीवित रही?", "यह व्यावसायिक लेन-देन में बनी रही, विशेष रूप से 1 रुपये को 16 आने में विभाजित करने और 1 सेर को 16 छटाक में तोलने की पारंपरिक प्रणाली के रूप में, जो 1957 तक चली।"),
    ("चन्हुदड़ो में मनकों की छोटी कार्यशालाएँ कीमती आभूषणों को तोलने में उच्च सटीकता कैसे बनाए रखती थीं?", "अगेट और जैस्पर के विशेष सूक्ष्म बाटों (0.86 ग्राम तक) तथा पतले धागों से लटके अत्यंत संवेदनशील तांबे के तराजू के पलड़ों का उपयोग करके।")
]:
    s1_mastery_hin.append({"type": "How", "q": q, "sol": sol})

# Case Study (3)
for q, sol in [
    ("Analyze a case study of chert weights excavated from a domestic residence at Harappa. What does it reveal about trade?", "Excavations of a cluster of standard cubical chert weights (ratios 1, 2, 8, 16) in a house block shows that retail trading and tax assessment occurred at the household level, rather than being restricted to state citadels."),
    ("A workshop site at Lothal has yielded half-finished agate weights and waste flakes. Reconstruct the manufacturing process.", "The find proves that weights were manufactured locally from imported agate nodules. Masons first sawed the stones, ground them into cuboid shapes, polished them using fine sand abrasives, and verified their weight against standard units before distribution."),
    ("Evaluate the metrological findings from Mesopotamian excavations at Ur. How does this prove Harappan overseas trade?", "Excavations at Ur yielded cubical chert weights matching the Harappan standard of 13.63g. This proves that Harappan merchants in Mesopotamia used their own weight standards for transactions, confirming active maritime trade networks.")
]:
    s1_mastery_eng.append({"type": "Case Study", "q": q, "sol": sol})

for q, sol in [
    ("हड़प्पा में एक साधारण घरेलू निवास से उत्खनित चर्ट बाटों के केस स्टडी का विश्लेषण करें। यह व्यापार के बारे में क्या दर्शाता है?", "एक घर से 1, 2, 8, 16 अनुपात वाले मानक बाटों के समूह का मिलना यह दर्शाता है कि खुदरा व्यापार और कर का निर्धारण घरों के स्तर पर भी होता था, न कि केवल दुर्गों में।"),
    ("लोथल में एक कार्यशाला स्थल से आधे बने अगेट बाट और वेस्ट चिप्स मिले हैं। निर्माण प्रक्रिया का पुनर्निर्माण करें।", "यह सिद्ध करता है कि बाटों का स्थानीय स्तर पर निर्माण आयातित अगेट पत्थरों से होता था। पहले पत्थरों को काटा जाता था, फिर घिसकर चौकोर आकार दिया जाता था, और फिर बारीक बालू से चमकाकर भार मापा जाता था।"),
    ("मेसोपोटामिया के उर (Ur) में हुए उत्खनन के बाटों का मूल्यांकन करें। यह हड़प्पा के विदेशी व्यापार को कैसे सिद्ध करता है?", "उर से हड़प्पा मानक (13.63 ग्राम) के घनाकार चर्ट बाट मिले हैं, जो यह सिद्ध करते हैं कि हड़प्पा के व्यापारी मेसोपोटामिया में भी अपने बाट मानकों का उपयोग करते थे।")
]:
    s1_mastery_hin.append({"type": "Case Study", "q": q, "sol": sol})

# Teach Concept (3)
for q, sol in [
    ("Explain the concept of 'Metrological Standardization' in the context of the Indus Valley Civilisation.", "It is the uniform system of weights and linear measures maintained across a vast territory. In the Indus Valley, this was achieved via Rohri chert weights, standard scales, and the 1:2:4 brick ratio, facilitating integrated trade and administration."),
    ("Contrast the binary and decimal subsystems of Harappan weights, explaining the economic purpose of each.", "The binary subsystem (ratios 1 to 64) was used for small, precise trade (gold, gemstones) where accuracy prevented fraud. The decimal subsystem (ratios 160 to 12800) was used for bulk, heavy cargo (grains, firewood) to ease calculation in large volumes."),
    ("Describe the quarrying and manufacturing network that linked the Rohri Hills to urban centers.", "Rohri hills served as the quarrying zone where raw chert was extracted and rough-shaped into blanks. These blanks were traded to urban workshops in Mohenjo-daro and Harappa, where craftsmen performed precision grinding and polishing to meet strict metrological standards.")
]:
    s1_mastery_eng.append({"type": "Teach Concept", "q": q, "sol": sol})

for q, sol in [
    ("सिंधु घाटी सभ्यता के संदर्भ में 'मापन मानकीकरण' (Metrological Standardization) की अवधारणा को स्पष्ट करें।", "यह एक विशाल क्षेत्र में बाट और माप की एकरूपता की प्रणाली है। हड़प्पा में यह चर्ट बाटों, मानक पैमानों और ईंटों के 1:2:4 अनुपात के माध्यम से प्राप्त किया गया था, जो एकीकृत व्यापार को दर्शाता है।"),
    ("हड़प्पा बाटों के बाइनरी और दशमलव उप-प्रणालियों की तुलना करें और दोनों के आर्थिक उद्देश्यों को स्पष्ट करें।", "बाइनरी उप-प्रणाली (1 से 64) कीमती वस्तुओं (सोना, रत्न) के तौल के लिए थी जहाँ उच्च सटीकता आवश्यक थी। दशमलव उप-प्रणाली (160 से 12800) थोक अनाज और भारी माल के तौल के लिए थी ताकि बड़ी मात्रा में गणना आसान हो सके।"),
    ("रोहरी की पहाड़ियों को शहरी केंद्रों से जोड़ने वाले खनन और विनिर्माण नेटवर्क का वर्णन करें।", "रोहरी की पहाड़ियाँ कच्चा चर्ट निकालने का मुख्य क्षेत्र थीं जहाँ बाटों के प्राथमिक ब्लॉक तैयार होते थे। इन ब्लॉकों को शहरों (मोहनजोदड़ो, हड़प्पा) की कार्यशालाओं में भेजा जाता था जहाँ घिसाई और पॉलिश की जाती थी।")
]:
    s1_mastery_hin.append({"type": "Teach Concept", "q": q, "sol": sol})


# =========================================================================
# SECTION 2: LINEAR MEASUREMENTS & SCALES
# =========================================================================
s2_mastery_eng = []
s2_mastery_hin = []

# MCQ (5)
for q, opts, ans, sol in [
    ("The famous ivory scale, featuring the smallest division of 1.7 mm, was excavated at which port town?", ["Lothal", "Dholavira", "Nageshwar", "Sutkagendor"], 0, "The ivory scale was discovered at Lothal, which was a major maritime port and bead-craft center."),
    ("The Mohenjo-daro shell scale defines a linear unit known as the 'Indus inch' which is equal to:", ["33.5 mm", "13.6 mm", "6.7 mm", "1.7 mm"], 0, "The 'Indus inch' derived from the shell scale is approximately 33.5 mm (1.32 inches)."),
    ("The standard building bricks of the Harappan civilization adhere to which dimension ratio?", ["1:2:4", "1:3:9", "1:2:3", "2:3:4"], 0, "Harappan building bricks adhered strictly to the ratio of 1:2:4 (thickness to width to length)."),
    ("A broken terracotta scale featuring precise calibration markings was discovered at which Rajasthan site?", ["Kalibangan", "Banawali", "Rakhigarhi", "Ropar"], 0, "Kalibangan in Rajasthan yielded a broken terracotta scale used by local builders."),
    ("The bronze scale bar found at Harappa has calibration marks spaced at which intervals?", ["9.3 mm", "1.7 mm", "6.7 mm", "13.6 mm"], 0, "The bronze scale from Harappa features calibrated markings spaced at 9.3 mm intervals.")
]:
    s2_mastery_eng.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("1.7 मिमी के सबसे बारीक मापन विभाजन वाला प्रसिद्ध हाथीदांत का पैमाना किस बंदरगाह शहर से मिला है?", ["लोथल", "धोलावीरा", "नागेश्वर", "सुत्कागेंदोर"], 0, "हाथीदांत का पैमाना गुजरात के प्रसिद्ध बंदरगाह लोथल से प्राप्त हुआ है।"),
    ("मोहनजोदड़ो का शंख पैमाना एक रैखिक इकाई को परिभाषित करता है जिसे 'सिंधु इंच' कहा जाता है, इसका मान क्या है?", ["33.5 मिमी", "13.6 मिमी", "6.7 मिमी", "1.7 मिमी"], 0, "शंख पैमाने से प्राप्त सिंधु इंच का मान लगभग 33.5 मिमी था।"),
    ("हड़प्पा सभ्यता की मानक इमारती ईंटों का आयाम अनुपात क्या था?", ["1:2:4", "1:3:9", "1:2:3", "2:3:4"], 0, "हड़प्पा ईंटों का अनुपात हमेशा 1:2:4 (मोटाई : चौड़ाई : लंबाई) होता था।"),
    ("मापन के निशानों वाली मिट्टी की एक टूटी पट्टी (Terracotta scale) राजस्थान के किस स्थल से मिली है?", ["कालीबंगन", "बनावली", "राखीगढ़ी", "रोपण"], 0, "राजस्थान के कालीबंगन से पकी मिट्टी का बना मापन पैमाना मिला है।"),
    ("हड़प्पा से प्राप्त कांसे की मापन पट्टी (bronze scale bar) पर निशान कितने अंतरालों पर अंकित हैं?", ["9.3 मिमी", "1.7 मिमी", "6.7 मिमी", "13.6 मिमी"], 0, "हड़प्पा के कांसे के पैमाने पर मापन विभाजन 9.3 मिमी के अंतराल पर हैं।")
]:
    s2_mastery_hin.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# Multiple Correct MCQ (5)
for q, opts, ans, sol in [
    ("Which of the following linear scales have been discovered in the Indus Valley Civilisation? (Select all that apply)", ["Lothal Ivory Scale", "Mohenjo-daro Shell Scale", "Harappa Bronze Scale", "Dholavira Wooden Scale"], [0, 1, 2], "Lothal (ivory), Mohenjo-daro (shell), and Harappa (bronze) are documented. No wooden scale survived at Dholavira."),
    ("Select the correct statements regarding Harappan brick standardization: (Select all that apply)", ["The dimension ratio was always 1:2:4", "Standard house bricks were 7x15x31 cm", "Fortification bricks were larger, like 10x20x40 cm", "Bricks in rural villages had random proportions"], [0, 1, 2], "The ratio was 1:2:4 everywhere; physical sizes differed between houses and fort walls; rural bricks also followed the ratio."),
    ("Which materials were used to construct calibrated rulers in the Indus Valley? (Select all that apply)", ["Ivory", "Marine Shell", "Bronze", "Iron"], [0, 1, 2], "Rulers were made of ivory, shell, and bronze. Iron was unknown."),
    ("Select the structural features enabled by the 1:2:4 brick ratio: (Select all that apply)", ["Interlocking header-and-stretcher masonry", "Construction of multi-story houses", "Water-tight layouts in public baths", "Circular dome roofing"], [0, 1, 2], "The ratio allowed interlocking joints, multi-story load bearing, and watertight bath masonry. Domes were not built."),
    ("Choose the correct linear unit measurements calculated from Harappan rulers: (Select all that apply)", ["Lothal division of 1.7 mm", "Mohenjo-daro division of 6.7 mm", "Harappa division of 9.3 mm", "Kalibangan division of 25.4 mm"], [0, 1, 2], "The rulers show divisions of 1.7mm (Lothal), 6.7mm (Mohenjo-daro), and 9.3mm (Harappa).")
]:
    s2_mastery_eng.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("सिंधु घाटी सभ्यता में निम्नलिखित में से कौन से रैखिक पैमाने खोजे गए हैं? (सभी सही विकल्प चुनें)", ["लोथल हाथीदांत पैमाना", "मोहनजोदड़ो शंख पैमाना", "हड़प्पा कांस्य पैमाना", "धोलावीरा लकड़ी का पैमाना"], [0, 1, 2], "लोथल (हाथीदांत), मोहनजोदड़ो (शंख) और हड़प्पा (कांसा) पैमाने मिले हैं। कोई लकड़ी का पैमाना नहीं मिला।"),
    ("हड़प्पा ईंट मानकीकरण के संबंध में सही कथनों का चयन करें: (सभी सही विकल्प चुनें)", ["आयाम अनुपात हमेशा 1:2:4 था", "साधारण घरों की ईंटें 7x15x31 सेमी की थीं", "किलेबंदी की ईंटें 10x20x40 सेमी जैसी बड़ी थीं", "ग्रामीण गाँवों की ईंटें अनियमित आकार की थीं"], [0, 1, 2], "ईंटों का अनुपात हमेशा 1:2:4 था; भौतिक आकार भिन्न थे; गाँवों में भी इसी अनुपात का पालन होता था।"),
    ("सिंधु घाटी में कैलिब्रेटेड पैमाने बनाने के लिए किन सामग्रियों का उपयोग होता था? (सभी सही विकल्प चुनें)", ["हाथीदांत", "समुद्री शंख", "कांसा", "लोहा"], [0, 1, 2], "हाथीदांत, शंख और कांसे का उपयोग होता था। लोहे का ज्ञान नहीं था।"),
    ("ईंटों के 1:2:4 अनुपात से वास्तुकला में क्या सुविधा प्राप्त हुई? (सभी सही विकल्प चुनें)", ["इंटरलॉकिंग चिनाई (English bond)", "बहुमंजिला मकानों का निर्माण", "विशाल स्नानागार की जल-रोधी चिनाई", "गोलाकार गुंबददार छतें"], [0, 1, 2], "इंटरलॉकिंग, बहुमंजिला संरचना और जल-रोधी चिनाई संभव हुई। गुंबद नहीं बनाए जाते थे।"),
    ("हड़प्पा पैमानों से गणना की गई सही रैखिक विभाजनों को चुनें: (सभी सही विकल्प चुनें)", ["लोथल विभाजन - 1.7 मिमी", "मोहनजोदड़ो विभाजन - 6.7 मिमी", "हड़प्पा विभाजन - 9.3 मिमी", "कालीबंगन विभाजन - 25.4 मिमी"], [0, 1, 2], "लोथल (1.7 मिमी), मोहनजोदड़ो (6.7 मिमी) और हड़प्पा (9.3 मिमी) के विभाजन दर्ज हैं।")
]:
    s2_mastery_hin.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# True/False (8)
for q, ans, sol in [
    ("The Lothal ivory scale division of 1.7 mm is the smallest recorded Bronze Age measurement unit.", True, "It represents the most precise linear calibration of the Bronze Age globally."),
    ("The brick ratio of 1:2:4 applied only to baked bricks, while sun-dried bricks had irregular ratios.", False, "Both baked and sun-dried bricks adhered strictly to the 1:2:4 ratio."),
    ("The Mohenjo-daro scale was made of animal bone.", False, "The Mohenjo-daro scale was made of marine shell."),
    ("The 'Indus inch' represents a value of approximately 33.5 mm.", True, "A sequence of shell scale markings defines this unit as 33.5 mm."),
    ("The Harappa scale bar was manufactured out of copper-alloy or bronze.", True, "It is a copper-alloy bar calibrated with markings."),
    ("The Kalibangan terracotta scale has no markings and was a decorative toy.", False, "It has clear calibration markings and was a builder's tool."),
    ("Bricks used for building city fortification walls were larger than those for ordinary houses.", True, "Fort walls used large bricks (10x20x40 cm), while houses used smaller ones (7x15x31 cm)."),
    ("The interlocking English bond masonry was unknown to Harappan architects.", False, "The 1:2:4 brick ratio was specifically used to lay walls in the interlocking English bond pattern.")
]:
    s2_mastery_eng.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("लोथल के हाथीदांत पैमाने का 1.7 मिमी का विभाजन कांस्य युग का सबसे सूक्ष्म मापन मान है।", True, "यह वैश्विक स्तर पर कांस्य युग का सबसे सटीक रैखिक कैलिब्रेशन दर्शाता है।"),
    ("1:2:4 का ईंट अनुपात केवल पकी ईंटों पर लागू था, जबकि कच्ची ईंटें अनियमित आकार की थीं।", False, "कच्ची (धूप में सूखी) और पकी दोनों प्रकार की ईंटें 1:2:4 अनुपात की थीं।"),
    ("मोहनजोदड़ो का पैमाना जानवर की हड्डी से बनाया गया था।", False, "मोहनजोदड़ो का पैमाना समुद्री शंख से बनाया गया था।"),
    ("सिंधु इंच का मान लगभग 33.5 मिमी के बराबर आंका गया है।", True, "शंख पैमाने के विभाजनों की श्रृंखला इस इकाई को 33.5 मिमी बताती है।"),
    ("हड़प्पा का पैमाना तांबे की मिश्र धातु या कांसे से बनाया गया था।", True, "हड़प्पा से मापन निशानों वाली कांसे की पट्टी मिली है।"),
    ("कालीबंगन का मिट्टी पैमाना बिना किसी निशान का एक साधारण खिलौना था।", False, "इस मिट्टी की पट्टी पर मापन के स्पष्ट निशान अंकित हैं।"),
    ("शहर की सुरक्षा प्राचीर की ईंटें साधारण घरों की ईंटों से बड़ी होती थीं।", True, "किलेबंदी की ईंटें (10x20x40 सेमी) घरों की ईंटों (7x15x31 सेमी) से बड़ी थीं।"),
    ("हड़प्पा के शिल्पकार दीवारों की इंटरलॉकिंग चिनाई (English bond) से परिचित नहीं थे।", False, "ईंटों का 1:2:4 अनुपात चिनाई में इंटरलॉकिंग पैटर्न बनाने के लिए ही डिज़ाइन था।")
]:
    s2_mastery_hin.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

# Fill in the Blank (8)
for q, ans, sol in [
    ("The Lothal scale was made of ________.", "ivory", "Ivory was carved into a precise ruler at Lothal."),
    ("The Mohenjo-daro scale was made of ________.", "shell", "Marine shell was used for the Mohenjo-daro ruler."),
    ("The standard building brick ratio is ________.", "1:2:4", "Bricks followed the thickness:width:length ratio of 1:2:4."),
    ("The smallest division on the Lothal ivory scale is ________ mm.", "1.7", "The division was extremely precise at 1.7 mm."),
    ("The 'Indus inch' equals approximately ________ mm.", "33.5", "The shell scale unit of Mohenjo-daro equals 33.5 mm."),
    ("The Harappa scale bar was made of ________.", "bronze", "Harappa yielded a bronze/copper bar ruler."),
    ("The terracotta scale was discovered at the site of ________.", "Kalibangan", "Kalibangan in Rajasthan has yielded a clay ruler."),
    ("The interlocking brick laying pattern used by Harappans is called the ________ bond.", "English", "Masons laid bricks in the interlocking English bond pattern.")
]:
    s2_mastery_eng.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("लोथल का मापन पैमाना ________ से बनाया गया था।", "हाथीदांत", "लोथल से हाथीदांत का बना सटीक पैमाना मिला है।"),
    ("मोहनजोदड़ो का मापन पैमाना ________ से बनाया गया था।", "शंख", "समुद्री शंख से मोहनजोदड़ो का पैमाना बनाया गया था।"),
    ("मानक इमारती ईंटों का आयाम अनुपात ________ था।", "1:2:4", "ईंटों का मोटाई:चौड़ाई:लंबाई का अनुपात 1:2:4 था।"),
    ("लोथल हाथीदांत पैमाने का सबसे छोटा मापन विभाजन ________ मिमी है।", "1.7", "लोथल पैमाने पर न्यूनतम विभाजन 1.7 मिमी अंकित है।"),
    ("सिंधु इंच का मान लगभग ________ मिमी के बराबर था।", "33.5", "शंख पैमाने से प्राप्त सिंधु इंच 33.5 मिमी के बराबर था।"),
    ("हड़प्पा का पैमाना छड़ ________ धातु से बना था।", "कांसा", "हड़प्पा से कांसे/तांबे का पैमाना मिला है।"),
    ("पकी मिट्टी (terracotta) का पैमाना ________ नामक स्थल से प्राप्त हुआ है।", "कालीबंगन", "राजस्थान के कालीबंगन से मिट्टी की मापन पट्टी मिली है।"),
    ("हड़प्पा वासियों द्वारा ईंट जोड़ने के लिए प्रयुक्त इंटरलॉकिंग पैटर्न को ________ बांड कहते हैं।", "इंग्लिश", "दीवारों की मजबूती के लिए वे इंग्लिश बांड चिनाई करते थे।")
]:
    s2_mastery_hin.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

# Match the Following (3)
s2_matches_eng = [
    {"q": "Match the scale material with the site of discovery:",
     "pairs": ["Ivory - Lothal", "Marine Shell - Mohenjo-daro", "Bronze - Harappa", "Terracotta - Kalibangan"],
     "sol": "Rulers were made of ivory (Lothal), shell (Mohenjo-daro), bronze (Harappa), and clay (Kalibangan)."},
    {"q": "Match the linear measurement values with their corresponding scale units:",
     "pairs": ["1.7 mm - Smallest Lothal division", "6.7 mm - Mohenjo-daro shell scale division", "9.3 mm - Harappa bronze scale calibration", "33.5 mm - Indus inch unit value"],
     "sol": "Links the calibrated linear values to their respective scale instruments and units."},
    {"q": "Match the building brick sizes with their architectural use:",
     "pairs": ["7 x 15 x 31 cm - Standard domestic houses", "10 x 20 x 40 cm - Public fortification walls", "1:2:4 - Fixed dimension ratio", "English Bond - Interlocking joint method"],
     "sol": "Integrates structural brick dimensions with their specific construction purposes."}
]
s2_mastery_eng.extend([make_match_question(m) for m in s2_matches_eng])

s2_matches_hin = [
    {"q": "पैमाने की निर्माण सामग्री को प्राप्ति स्थल से सुमेलित करें:",
     "pairs": ["हाथीदांत - लोथल", "समुद्री शंख - मोहनजोदड़ो", "कांसा - हड़प्पा", "पकी मिट्टी - कालीबंगन"],
     "sol": "हाथीदांत का पैमाना लोथल से; शंख का मोहनजोदड़ो से; कांसे का हड़प्पा से; और मिट्टी का कालीबंगन से मिला है।"},
    {"q": "रैखिक माप के मानों को उनके संबंधित पैमानों से सुमेलित करें:",
     "pairs": ["1.7 मिमी - लोथल हाथीदांत पैमाने का न्यूनतम विभाजन", "6.7 मिमी - मोहनजोदड़ो शंख पैमाने का विभाजन", "9.3 मिमी - हड़प्पा कांस्य पैमाने का विभाजन", "33.5 मिमी - सिंधु इंच का इकाई मान"],
     "sol": "मापन मानों को उनके विशिष्ट पैमानों और मापन इकाइयों से जोड़ता है।"},
    {"q": "इमारती ईंटों के आकारों को उनके स्थापत्य उपयोग से सुमेलित करें:",
     "pairs": ["7 x 15 x 31 सेमी - साधारण घरेलू मकान", "10 x 20 x 40 सेमी - सार्वजनिक सुरक्षा प्राचीर", "1:2:4 - निश्चित आयाम अनुपात", "इंग्लिश बांड - इंटरलॉकिंग चिनाई विधि"],
     "sol": "ईंटों के आयामों को नगर निर्माण के विशिष्ट उद्देश्यों से सुमेलित करता है।"}
]
s2_mastery_hin.extend([make_match_question(m) for m in s2_matches_hin])

# One-Liner (8)
for q, sol in [
    ("Where was the ivory linear scale found in the Indus Valley?", "Lothal in Gujarat."),
    ("What is the smallest division on the Lothal ivory ruler?", "1.7 millimeters."),
    ("What material was used for the Mohenjo-daro ruler?", "Marine shell."),
    ("What is the name of the linear unit equal to 33.5 mm?", "The Indus inch."),
    ("What is the exact ratio of standard Harappan bricks?", "Thickness : Width : Length = 1 : 2 : 4."),
    ("Which site yielded a builder's clay scale?", "Kalibangan in Rajasthan."),
    ("Why was the 1:2:4 brick ratio structurally important?", "It allowed bricks to be laid in an interlocking header-and-stretcher pattern, providing maximum stability."),
    ("What metal was used to make the Harappan scale bar?", "Bronze (or copper-alloy).")
]:
    s2_mastery_eng.append({"type": "One-Liner", "q": q, "sol": sol})

for q, sol in [
    ("सिंधु घाटी में हाथीदांत का रैखिक पैमाना कहाँ से प्राप्त हुआ है?", "गुजरात के लोथल से।"),
    ("लोथल के हाथीदांत पैमाने पर सबसे छोटा विभाजन कितना है?", "1.7 मिलीमीटर।"),
    ("मोहनजोदड़ो के मापन पैमाने के निर्माण में किस सामग्री का उपयोग हुआ था?", "समुद्री शंख का।"),
    ("33.5 मिमी के बराबर की हड़प्पा रैखिक मापन इकाई को क्या कहते हैं?", "सिंधु इंच (Indus inch)।"),
    ("हड़प्पा की मानक ईंटों का निश्चित आयाम अनुपात क्या है?", "मोटाई : चौड़ाई : लंबाई = 1 : 2 : 4।"),
    ("किस स्थल से राजमिस्त्रियों का मिट्टी का पैमाना प्राप्त हुआ है?", "राजस्थान के कालीबंगन से।"),
    ("ईंटों का 1:2:4 अनुपात संरचनात्मक दृष्टि से क्यों महत्वपूर्ण था?", "इससे दीवारों में इंग्लिश बांड इंटरलॉकिंग चिनाई संभव हुई जिससे बहुमंजिला ढांचे स्थिर रहे।"),
    ("हड़प्पा से मिली मापन छड़ किस धातु से बनाई गई थी?", "कांसे (या तांबे की मिश्र धातु) से।")
]:
    s2_mastery_hin.append({"type": "One-Liner", "q": q, "sol": sol})

# Assertion-Reason (8)
for q, ans, sol in [
    ("Assertion (A): The Lothal ivory scale has the most precise division (1.7 mm) of the Bronze Age.\nReason (R): Lothal was a major manufacturing hub for beads and ornaments requiring micro-measurements.", 0, "Both A and R are true, and R explains why such a high-precision scale was needed at a craft town like Lothal."),
    ("Assertion (A): Sun-dried bricks used for building houses had random proportions.\nReason (R): Only kiln-fired bricks used in drainage networks required the standardized 1:2:4 ratio.", 4, "Both A and R are false. Both sun-dried and baked bricks followed the strict 1:2:4 ratio across all cities."),
    ("Assertion (A): Mohenjo-daro's shell scale is highly resistant to moisture.\nReason (R): Marine shell does not expand or warp in humid climates, preserving scale accuracy.", 0, "Both A and R are true, and the climatic stability of shell explains why it was chosen for scales in riverine climates."),
    ("Assertion (A): Harappan street layouts conform to standardized dimensions.\nReason (R): Street and lane widths align with mathematical multiples of the shell scale unit.", 0, "Both A and R are true, and the street layout dimensions prove that builders planned grids using scales."),
    ("Assertion (A): Fortification walls used much larger bricks than private dwellings.\nReason (R): Large bricks (10x20x40 cm) provided more structural mass for defense, while keeping the 1:2:4 ratio.", 0, "Both A and R are true, and the structural mass requirement explains why fortification bricks were larger."),
    ("Assertion (A): Terracotta scales were mass-produced for the elite ruling class.\nReason (R): Terracotta is a cheap material used to make everyday tools for ordinary masonry builders.", 3, "A is false; R is true. Clay scales were everyday tools for builders, not luxury items for the elite."),
    ("Assertion (A): Bronze rulers were preferred for measuring textiles.\nReason (R): Bronze bars do not bend, ensuring consistent cloth measurements without stretching.", 1, "Both A and R are true, but R does not explain why they were made of metal rather than bone or shell."),
    ("Assertion (A): Harappan walls were built without mortar using friction only.\nReason (R): The 1:2:4 brick ratio enabled walls to stand securely using interlocking patterns.", 3, "A is false because mud mortar or gypsum mortar was used; R is true as the ratio facilitated interlocking stability.")
]:
    s2_mastery_eng.append({"type": "Assertion-Reason", "q": q, "opts": ar_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("कथन (A): लोथल का हाथीदांत पैमाना कांस्य युग का सबसे सटीक रैखिक पैमाना (1.7 मिमी) है।\nकारण (R): लोथल मनकों और रत्नों का बड़ा केंद्र था जहाँ अत्यंत बारीक मापन की आवश्यकता थी।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या है। रत्नों के काम में अत्यधिक सटीकता की आवश्यकता हाथीदांत पैमाने की उत्पत्ति का कारण थी।"),
    ("कथन (A): मकान बनाने में प्रयुक्त धूप में सूखी ईंटें मनमाने आकार की होती थीं।\nकारण (R): केवल नालियों में प्रयुक्त भट्टी में पकी ईंटों को ही 1:2:4 के मानक अनुपात की आवश्यकता होती थी।", 4, "A और R दोनों गलत हैं। कच्ची और पकी दोनों ईंटें हमेशा 1:2:4 के निश्चित अनुपात में बनती थीं।"),
    ("कथन (A): मोहनजोदड़ो का शंख पैमाना नमी और आर्द्रता के प्रति प्रतिरोधी था।\nकारण (R): समुद्री शंख आर्द्र नदीय जलवायु में फैलता या सिकुड़ता नहीं था, जिससे मापन की शुद्धता बनी रहती थी।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या है।"),
    ("कथन (A): हड़प्पा की सड़कों का लेआउट मानकीकृत आयामों के अनुरूप था।\nकारण (R): गलियों और सड़कों की चौड़ाई शंख पैमाने की मापन इकाई के गणितीय गुणकों से मेल खाती है।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या है।"),
    ("कथन (A): नगर सुरक्षा प्राचीरों में घरेलू मकानों से कहीं बड़ी ईंटों का उपयोग होता था।\nकारण (R): बड़ी ईंटें (10x20x40 सेमी) सुरक्षा प्राचीरों को मजबूत आधार प्रदान करती थीं, जबकि अनुपात 1:2:4 ही रहता था।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या है।"),
    ("कथन (A): मिट्टी (terracotta) के पैमाने विशेष रूप से केवल शासक वर्ग के लिए बनाए जाते थे।\nकारण (R): मिट्टी एक सस्ती सामग्री थी जिससे राजमिस्त्रियों के उपयोग के लिए साधारण मापन पट्टियाँ बनाई जाती थीं।", 3, "A गलत है लेकिन R सही है। मिट्टी के पैमाने राजमिस्त्रियों के आम औजार थे, न कि शासकों की विलासिता।"),
    ("कथन (A): कपड़ा मापने के लिए कांसे के पैमानों को प्राथमिकता दी जाती थी।\nकारण (R): कांसे की छड़ें मुड़ती नहीं थीं, जिससे बिना खिंचाव के कपड़ों का एकसमान मापन सुनिश्चित होता था।", 1, "A और R दोनों सही हैं, लेकिन R, कथन A की सही व्याख्या नहीं है क्योंकि कांसे के पैमाने का उपयोग अन्य मापों में भी होता था।"),
    ("कथन (A): हड़प्पा की दीवारें बिना किसी गारे (mortar) के केवल घर्षण से खड़ी की जाती थीं।\nकारण (R): ईंटों का 1:2:4 अनुपात दीवारों को इंटरलॉकिंग पैटर्न में मजबूती से खड़े होने की अनुमति देता था।", 3, "A गलत है क्योंकि वे मिट्टी या जिप्सम के गारे का उपयोग करते थे; R सही है क्योंकि अनुपात इंटरलॉकिंग में सहायक था।")
]:
    s2_mastery_hin.append({"type": "Assertion-Reason", "q": q, "opts": hin_ar_opts, "ans": ans, "sol": sol})

# Statement-Based (5)
for q, ans, sol in [
    ("Consider the following statements:\nStatement 1: The Lothal ivory scale has a minimum division of 1.7 mm.\nStatement 2: The Mohenjo-daro shell scale defines a unit called the 'Indus inch' equal to 33.5 mm.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct. Lothal division is 1.7mm and Mohenjo-daro shell scale defines the Indus inch (33.5mm)."),
    ("Consider the following statements:\nStatement 1: Sun-dried and kiln-baked building bricks adhere to the 1:2:4 ratio.\nStatement 2: Harappan bricks were made using wooden molds of standard sizes.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct. Bricks followed the 1:2:4 ratio and were shaped using standardized wooden molds."),
    ("Consider the following statements:\nStatement 1: The Harappa scale was made of marine shell.\nStatement 2: The Kalibangan scale was made of terracotta.\nWhich of the statements given above is/are correct?", 1, "Statement 2 is correct. Statement 1 is incorrect: Harappa scale was bronze, Mohenjo-daro was shell."),
    ("Consider the following statements:\nStatement 1: The 1:2:4 brick ratio enabled walls to be built using interlocking English bond masonry.\nStatement 2: Harappan architects built massive circular arches using wedge-shaped bricks.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: Harappans did not build true circular arches; they built corbelled arches."),
    ("Consider the following statements:\nStatement 1: Fortification bricks were larger than domestic building bricks.\nStatement 2: Both house and fortification bricks followed different ratio structures.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: both types strictly followed the same 1:2:4 ratio.")
]:
    s2_mastery_eng.append({"type": "Statement-Based", "q": q, "opts": mcq_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: लोथल के हाथीदांत पैमाने पर न्यूनतम विभाजन 1.7 मिमी अंकित है।\nकथन 2: मोहनजोदड़ो का शंख पैमाना 33.5 मिमी के 'सिंधु इंच' को परिभाषित करता है।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 2, "दोनों कथन सही हैं। लोथल का विभाजन 1.7 मिमी है और सिंधु इंच 33.5 मिमी के बराबर आंका गया है।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: धूप में सूखी और भट्टी में पकी ईंटें 1:2:4 के निश्चित अनुपात का पालन करती थीं।\nकथन 2: हड़प्पा कालीन ईंटों को आकार देने के लिए मानक आकार के लकड़ी के सांचों का उपयोग होता था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 2, "दोनों कथन सही हैं। ईंटें 1:2:4 अनुपात की थीं और उन्हें लकड़ी के सांचों (molds) में ढाला जाता था।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: हड़प्पा से प्राप्त रैखिक पैमाना समुद्री शंख से बनाया गया था।\nकथन 2: कालीबंगन से प्राप्त पैमाना पकी मिट्टी (terracotta) से बनाया गया था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 1, "कथन 2 सही है। कथन 1 गलत है क्योंकि हड़प्पा का पैमाना कांसे का था, शंख का पैमाना मोहनजोदड़ो से मिला था।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: ईंटों के 1:2:4 अनुपात से दीवारों में इंग्लिश बांड की इंटरलॉकिंग चिनाई संभव हुई।\nकथन 2: हड़प्पा के इंजीनियरों ने त्रिकोणीय ईंटों की मदद से विशाल गोलाकार मेहराब (arches) बनाए।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि हड़प्पा वास्तुकला में असली गोलाकार मेहराब नहीं थे; वे केवल कोर्बल्ड मेहराब बनाते थे।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: किलेबंदी की प्राचीरों की ईंटें घरेलू मकानों की ईंटों से आकार में बड़ी थीं।\nकथन 2: घर और सुरक्षा प्राचीर की दोनों प्रकार की ईंटें अलग-अलग आयाम अनुपात का पालन करती थीं।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि दोनों ईंटों का अनुपात समान रूप से 1:2:4 ही होता था।")
]:
    s2_mastery_hin.append({"type": "Statement-Based", "q": q, "opts": hin_mcq_opts, "ans": ans, "sol": sol})

# Why (3)
for q, sol in [
    ("Why did the Harappans manufacture linear scales out of marine shell and ivory rather than wood?", "Wood warps, swells, and decays when exposed to water or high humidity. Ivory and marine shell are structurally stable, dense, and water-resistant materials, ensuring that calibration marks remained accurate over generations of use in a riverine climate."),
    ("Why did Harappan masons strictly enforce the 1:2:4 ratio for building bricks?", "Because a length that is exactly twice the width (plus mortar) allows bricks to be laid in an interlocking header-and-stretcher pattern (English bond), avoiding continuous vertical joints and distributing structural load evenly."),
    ("Why was the bronze scale bar at Harappa a significant technological achievement?", "It shows that linear measurement was integrated into metalworking. Cast bronze rulers required precise engraving tools and metallurgical control, proving that metrology was managed by highly skilled urban state institutions.")
]:
    s2_mastery_eng.append({"type": "Why", "q": q, "sol": sol})

for q, sol in [
    ("हड़प्पा वासियों ने मापन पैमाने लकड़ी के बजाय हाथीदांत और समुद्री शंख से क्यों बनाए?", "लकड़ी नमी या पानी के संपर्क में आने पर सड़ जाती है और टेढ़ी हो जाती है। हाथीदांत और समुद्री शंख नदीय आर्द्र जलवायु में भी फैलते या सिकुड़ते नहीं हैं, जिससे पैमाने की सटीकता बनी रहती थी।"),
    ("हड़प्पा के राजमिस्त्रियों ने ईंटों के लिए 1:2:4 का अनुपात इतनी सख्ती से क्यों लागू किया?", "क्योंकि चौड़ाई से दुगनी लंबाई होने पर ईंटों को एक-दूसरे के ऊपर लंबवत (English bond) जोड़ना आसान होता था, जिससे दीवारों में जोड़ एक सीध में नहीं आते थे और दीवारें अत्यधिक मजबूत बनती थीं।"),
    ("हड़प्पा से प्राप्त कांसे की मापन पट्टी एक महत्वपूर्ण तकनीकी उपलब्धि क्यों थी?", "यह सिद्ध करता है कि रैखिक मापन धातु विज्ञान का हिस्सा था। कांसे के पैमाने ढालने के लिए सटीक नक्काशी और धातु नियंत्रण की आवश्यकता होती थी, जो विकसित मापन नियमों को दर्शाता है।")
]:
    s2_mastery_hin.append({"type": "Why", "q": q, "sol": sol})

# How (3)
for q, sol in [
    ("How did the 1:2:4 brick ratio contribute to the construction of hydraulic works like the Great Bath and Lothal Dockyard?", "It allowed masons to build dense, thick walls using interlocking joints. These joints were filled with gypsum or bitumen mortar, creating watertight barriers capable of holding massive volumes of water without leaking."),
    ("How was the shell scale at Mohenjo-daro calibrated to establish the 'Indus inch'?", "Craftsmen engraved markings at intervals of 6.7 mm. A sequence of five divisions constituted the standard unit of 33.5 mm, which served as a modular unit for layout planning and architectural design."),
    ("How did the discovery of the Kalibangan terracotta scale change our understanding of rural builder networks?", "It proved that standard measurement tools were not limited to the administrative elites of Mohenjo-daro or Harappa, but were distributed to regional builders and brick-makers in peripheral zones like Rajasthan.")
]:
    s2_mastery_eng.append({"type": "How", "q": q, "sol": sol})

for q, sol in [
    ("ईंटों के 1:2:4 अनुपात ने विशाल स्नानागार और लोथल गोदी (dockyard) जैसे जलीय ढांचों के निर्माण में कैसे सहयोग दिया?", "इससे इंटरलॉकिंग जोड़ों की सहायता से अत्यंत सघन और मोटी दीवारें बनाना संभव हुआ। इन जोड़ों में जिप्सम या डामर (bitumen) का गारा भरा जाता था, जिससे पानी का रिसाव पूरी तरह से रुक जाता था।"),
    ("मोहनजोदड़ो में शंख पैमाने को 'सिंधु इंच' स्थापित करने के लिए कैसे अंशांकित (calibrate) किया गया था?", "शिल्पकारों ने शंख पट्टी पर 6.7 मिमी के अंतरालों पर विभाजन रेखाएं बनाईं। पांच अंतरालों की एक श्रृंखला से 33.5 मिमी की इकाई बनती थी, जिसका उपयोग नगर के लेआउट और भवनों के आयामों में होता था।"),
    ("कालीबंगन से प्राप्त मिट्टी के पैमाने ने क्षेत्रीय राजमिस्त्री नेटवर्क के बारे में हमारी समझ को कैसे बदला?", "यह सिद्ध करता है कि मानक मापन साधन केवल मोहनजोदड़ो या हड़प्पा के कुलीनों तक सीमित नहीं थे, बल्कि राजस्थान जैसे बाहरी क्षेत्रों के स्थानीय राजमिस्त्रियों और ईंट बनाने वालों तक भी वितरित थे।")
]:
    s2_mastery_hin.append({"type": "How", "q": q, "sol": sol})

# Case Study (3)
for q, sol in [
    ("Discuss a case study of the Lothal ivory scale. What does its precision indicate about maritime manufacturing?", "The Lothal ivory scale (1.7 mm divisions) was excavated near the bead factory. Its micro-calibrations were used by lapidaries to cut carnelian beads and calibrate marine shell items, showing that port towns required high metrological accuracy for export manufacturing."),
    ("Analyze the spatial dimensions of houses at Mohenjo-daro. How does it relate to the shell scale?", "Studies of room lengths, street widths, and courtyard sizes at Mohenjo-daro show they are exact mathematical multiples of the 33.5 mm 'Indus inch' unit, proving that municipal engineers used the shell scale for urban layout planning."),
    ("Evaluate the English bond masonry findings from the fortification walls of Harappa. Why was the brick ratio vital?", "fortification walls at Harappa were built with bricks measuring 10x20x40 cm. Masons laid them in alternating directions (headers and stretchers). The 1:2:4 ratio ensured that overlapping brick joints aligned perfectly, preventing cracks and giving walls strength to resist military siege.")
]:
    s2_mastery_eng.append({"type": "Case Study", "q": q, "sol": sol})

for q, sol in [
    ("लोथल के हाथीदांत पैमाने के केस स्टडी पर चर्चा करें। इसकी सूक्ष्मता बंदरगाह के विनिर्माण के बारे में क्या दर्शाती है?", "यह पैमाना (1.7 मिमी विभाजन) मनकों के कारखाने के समीप मिला था। इसके छोटे विभाजनों का उपयोग शिल्पकार मनके काटने और शंख की वस्तुओं को सटीक रूप देने के लिए करते थे, जो निर्यात व्यापार की सटीकता को दर्शाता है।"),
    ("मोहनजोदड़ो के घरों के स्थानिक आयामों (spatial dimensions) का विश्लेषण करें। यह शंख पैमाने से किस प्रकार संबंधित है?", "मोहनजोदड़ो में कमरों की लंबाई, गलियों की चौड़ाई और आँगनों के आकार का विश्लेषण यह दर्शाता है कि वे 33.5 मिमी के सिंधु इंच के गणितीय गुणक हैं, जिससे सिद्ध होता है कि नगर नियोजक पैमाने का उपयोग करते थे।"),
    ("हड़प्पा की सुरक्षा प्राचीर की इंग्लिश बांड चिनाई के साक्ष्यों का मूल्यांकन करें। ईंट का निश्चित अनुपात क्यों आवश्यक था?", "हड़प्पा की प्राचीर में 10x20x40 सेमी की ईंटें प्रयुक्त थीं। इन्हें एकांतर दिशाओं (headers and stretchers) में बिछाया गया था। 1:2:4 अनुपात के कारण जोड़ों का ओवरलैप एकदम सटीक रहा, जिसने प्राचीर को भारी मजबूती प्रदान की।")
]:
    s2_mastery_hin.append({"type": "Case Study", "q": q, "sol": sol})

# Teach Concept (3)
for q, sol in [
    ("Explain the concept of the 'Indus Inch' and how it was calculated from archaeological remains.", "The 'Indus inch' is a linear unit calculated from the Mohenjo-daro shell scale. Craftsmen marked divisions at 6.7 mm intervals. A set of five divisions equals 33.5 mm (1.32 inches). This unit served as the basis for standard brick lengths and room layout planning."),
    ("Compare the linear scale systems of Lothal, Mohenjo-daro, and Harappa, detailing their materials and divisions.", "The Lothal scale is ivory with 1.7 mm divisions, optimized for micro-crafts. The Mohenjo-daro scale is shell with 6.7 mm divisions (forming the 33.5 mm Indus inch), used for buildings. The Harappa scale is a bronze bar with 9.3 mm divisions, showing metallurgical calibration."),
    ("Explain the English Bond masonry system and how the 1:2:4 brick ratio is essential for its structural logic.", "The English Bond lays bricks in alternating courses of headers (width facing out) and stretchers (length facing out). The 1:2:4 ratio ensures that two headers laid side-by-side equal one stretcher length (plus mortar). This mathematical alignment eliminates continuous vertical joints, giving walls structural load-bearing capacity.")
]:
    s2_mastery_eng.append({"type": "Teach Concept", "q": q, "sol": sol})

for q, sol in [
    ("रैखिक इकाई 'सिंधु इंच' की अवधारणा और पुरातात्विक साक्ष्यों से इसकी गणना को स्पष्ट करें।", "सिंधु इंच मोहनजोदड़ो के शंख पैमाने से प्राप्त एक मापन इकाई है। शिल्पकारों ने 6.7 मिमी पर विभाजन बनाए थे। पांच विभाजनों का समूह 33.5 मिमी (1.32 इंच) के बराबर होता था, जिसका उपयोग नगर नियोजन और ईंटों के आकार में किया जाता था।"),
    ("लोथल, मोहनजोदड़ो और हड़प्पा की रैखिक मापन प्रणालियों की तुलना करें और उनकी सामग्री एवं विभाजनों का विवरण दें।", "लोथल का हाथीदांत का पैमाना 1.7 मिमी विभाजन वाला था (सूक्ष्म शिल्प के लिए); मोहनजोदड़ो का शंख पैमाना 6.7 मिमी विभाजन वाला था (सिंधु इंच के लिए); हड़प्पा का पैमाना कांसे की पट्टी था जिस पर 9.3 मिमी के निशान थे।"),
    ("दीवार निर्माण में इंग्लिश बांड (English Bond) चिनाई प्रणाली और इसमें ईंटों के 1:2:4 अनुपात की आवश्यकता को समझाएं।", "इंग्लिश बांड में ईंटों को बारी-बारी से लंबवत (headers) और समानांतर (stretchers) बिछाया जाता है। 1:2:4 अनुपात यह सुनिश्चित करता है कि दो लंबवत ईंटों की चौड़ाई एक समानांतर ईंट की लंबाई के बराबर हो, जिससे दीवार मजबूत बनती है।")
]:
    s2_mastery_hin.append({"type": "Teach Concept", "q": q, "sol": sol})


# =========================================================================
# SECTION 3: PRACTICAL APPLICATION: CONSTRUCTION, TAXATION, AND TRADE RATIONALE
# =========================================================================
s3_mastery_eng = []
s3_mastery_hin = []

# MCQ (5)
for q, opts, ans, sol in [
    ("Standardized Harappan chert weights have been excavated in which Persian Gulf trade transit port?", ["Dilmun (Bahrain)", "Magan (Oman)", "Susa", "Lagash"], 0, "Dilmun (modern Bahrain) adopted the Harappan weight standard for its Gulf trade."),
    ("The collection of state grain taxes or tributes was verified using weights at which public structures?", ["Granaries and Warehouses", "Great Baths", "Cemeteries", "Bead Factories"], 0, "State granaries and warehouses were the points where food tribute was weighed, verified, and stored."),
    ("Excavations of balance scales and weights in residential quarters of lower towns suggest:", ["Decentralized retail trade was common", "Only royal officials could weigh goods", "All trade was controlled by temple priests", "Barter did not exist in domestic areas"], 0, "Finding weights in residential quarters proves that retail trade occurred directly at the household level."),
    ("Mesopotamian cuneiform texts list imports of luxury commodities from which region, matching Harappan weights?", ["Meluhha", "Magan", "Dilmun", "Elam"], 0, "Meluhha (the Indus Valley) exported ivory, carnelian, and timber to Mesopotamia, using its standardized metrology."),
    ("During the Late Harappan phase, the breakdown of metrological standardization was accompanied by:", ["The disappearance of long-distance trade", "The invention of coinage", "The adoption of the Mesopotamian system", "The discovery of iron weights"], 0, "The collapse of urban centers and long-distance trade led to the fragmentation of standardized weights.")
]:
    s3_mastery_eng.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("फारस की खाड़ी के किस व्यापारिक पारगमन बंदरगाह (transit port) से हड़प्पा मानक के चर्ट बाट मिले हैं?", ["दिलमुन (बहरीन)", "मगन (ओमान)", "सूसा", "लगाश"], 0, "फारस की खाड़ी में स्थित दिलमुन (बहरीन) से हड़प्पा मानक के चर्ट बाट प्राप्त हुए हैं।"),
    ("राजकीय अनाज करों या उपहारों का सत्यापन और मापन किस सार्वजनिक संरचना पर किया जाता था?", ["अन्नागार और गोदाम", "विशाल स्नानागार", "कब्रिस्तान", "मनके बनाने के कारखाने"], 0, "अन्नागार और राजकीय गोदामों में कर संग्रह को बाटों की मदद से तोलकर भंडारित किया जाता था।"),
    ("निचले शहरों के साधारण आवासीय क्षेत्रों में तराजू के पलड़ों और बाटों का मिलना क्या दर्शाता है?", ["विकेंद्रीकृत खुदरा व्यापार आम था", "केवल शाही अधिकारी ही सामान तोल सकते थे", "संपूर्ण व्यापार पुरोहितों द्वारा नियंत्रित था", "घरेलू क्षेत्रों में वस्तु विनिमय नहीं होता था"], 0, "साधारण घरों से बाटों का मिलना खुदरा व्यापार और दैनिक लेन-देन में इनकी व्यापक पहुँच को दर्शाता है।"),
    ("मेसोपोटामिया के कीलाक्षर (cuneiform) लेखों में किस क्षेत्र से वस्तुओं के आयात का उल्लेख है जो हड़प्पा बाट मानकों से मेल खाता है?", ["मेलुहा (Meluhha)", "मगन", "दिलमुन", "एलाम"], 0, "मेलुहा (सिंधु घाटी) से हाथीदांत और कीमती पत्थरों का आयात होता था जो हड़प्पा मापन मानकों पर आधारित थे।"),
    ("उत्तर हड़प्पा काल में, बाट और माप के मानकीकरण के पतन के साथ और क्या बदलाव आया?", ["दीर्घकालिक विदेशी व्यापार का समाप्त होना", "धातु के सिक्कों का आविष्कार", "मेसोपोटामिया की मापन प्रणाली को अपनाना", "लोहे के बाटों की खोज"], 0, "शहरी केंद्रों के पतन और विदेशी व्यापार बंद होने से मानकीकृत बाट-माप प्रणाली बिखर गई।")
]:
    s3_mastery_hin.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# Multiple Correct MCQ (5)
for q, opts, ans, sol in [
    ("Select the trade routes where Harappan standardized weights or their influence have been discovered: (Select all that apply)", ["Persian Gulf (Dilmun/Bahrain)", "Mesopotamian cities (Ur)", "Makran Coast outposts", "Central Asian steppes"], [0, 1, 2], "Harappan metrological influence is found in the Persian Gulf, Ur, and Makran coast. Central Asian steppes show no such influence."),
    ("Which of the following functions did standard weights and measures serve in Harappan administration? (Select all that apply)", ["Standardizing taxation on agricultural surplus", "Regulating exchange values in barter trade", "Enforcing uniform brick sizes for municipal works", "Issuing stamped metallic coins"], [0, 1, 2], "Weights regulated tax, barter values, and brick/municipal sizes. Coins did not exist."),
    ("Choose the correct statements regarding trade metrology: (Select all that apply)", ["Mesopotamia followed a sexagesimal metrology", "Harappa followed a binary-decimal metrology", "Dilmun adopted the Harappan weight standard", "Egyptians used Rohri chert weights"], [0, 1, 2], "Mesopotamia used base-60, Harappa used binary-decimal, Dilmun adopted Harappan standards. Egypt did not use Rohri chert weights."),
    ("Select the indicators of administrative centralization in Harappan metrology: (Select all that apply)", ["Rohri chert sourced from a single region", "Exact weight ratios maintained over 1 million sq km", "Uniform 1:2:4 brick ratios in cities and villages", "Use of iron scales"], [0, 1, 2], "Centralization is indicated by Rohri chert quarrying, uniform weight ratios, and uniform brick ratios. Iron did not exist."),
    ("Which factors contributed to the decline of standardized weights in the Late Harappan phase? (Select all that apply)", ["Decline of long-distance Persian Gulf trade", "De-urbanization and collapse of municipal administrations", "Re-emergence of localized regional barter standards", "Introduction of Mesopotamian standardized rulers"], [0, 1, 2], "Decline was caused by Gulf trade collapse, de-urbanization, and regional fragmentation. Mesopotamian rulers were not introduced.")
]:
    s3_mastery_eng.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("उन व्यापार मार्गों को चुनें जहाँ हड़प्पा के मानक बाटों या उनके प्रभाव के साक्ष्य मिले हैं: (सभी सही विकल्प चुनें)", ["फारस की खाड़ी (दिलमुन/बहरीन)", "मेसोपोटामिया के शहर (उर)", "मकरान तट की चौकियां", "मध्य एशियाई स्टेपी क्षेत्र"], [0, 1, 2], "खाड़ी व्यापारिक बंदरगाहों, मेसोपोटामिया (उर) और मकरान तट से बाट मिले हैं। स्टेपी क्षेत्र से कोई साक्ष्य नहीं है।"),
    ("हड़प्पा प्रशासन में बाट और माप ने किन कार्यों में सहयोग दिया? (सभी सही विकल्प चुनें)", ["कृषि अधिशेष पर करों का निर्धारण", "वस्तु विनिमय में विनिमय मूल्यों का नियमन", "नगर पालिकाओं के लिए ईंटों के आकार का नियमन", "धातु के मुहरबंद सिक्कों का प्रचलन"], [0, 1, 2], "कर निर्धारण, वस्तु विनिमय नियमन और नगर वास्तुकला मानकीकरण में बाटों का उपयोग होता था। सिक्के नहीं थे।"),
    ("व्यापार मापन के संबंध में सही कथनों का चयन करें: (सभी सही विकल्प चुनें)", ["मेसोपोटामिया में षष्ठदशमलव (sexagesimal) प्रणाली थी", "हड़प्पा में बाइनरी-दशमलव प्रणाली थी", "दिलमुन ने हड़प्पा के बाट मानक को अपनाया था", "मिस्र वासी रोहरी चर्ट के बाटों का उपयोग करते थे"], [0, 1, 2], "मेसोपोटामिया में बेस-60, हड़प्पा में बाइनरी-दशमलव था, और दिलमुन ने हड़प्पा बाटों को अपनाया था। मिस्र चर्ट बाटों का प्रयोग नहीं करता था।"),
    ("हड़प्पा मापन प्रणाली में प्रशासनिक केंद्रीकरण के संकेत कौन से हैं? (सभी सही विकल्प चुनें)", ["एक ही क्षेत्र (रोहरी) से चर्ट पत्थर मंगाना", "10 लाख वर्ग किमी में बाटों का समान अनुपात होना", "शहरों और गाँवों में ईंटों का समान 1:2:4 अनुपात होना", "लोहे के पैमानों का उपयोग"], [0, 1, 2], "एक ही स्रोत से चर्ट मंगाना, समान बाट अनुपात और समान ईंट अनुपात प्रशासनिक एकता को दर्शाते हैं। लोहे का अस्तित्व नहीं था।"),
    ("उत्तर हड़प्पा काल में मापन प्रणालियों के बिखरने के कारण क्या थे? (सभी सही विकल्प चुनें)", ["खाड़ी व्यापार का समाप्त होना", "शहरीकरण का पतन और नगर पालिकाओं का कमजोर होना", "स्थानीय स्तर पर क्षेत्रीय मापों का उदय होना", "मेसोपोटामिया के मापन पैमानों का आगमन"], [0, 1, 2], "खाड़ी व्यापार का पतन, शहरों का ह्रास और स्थानीय मापों का पुनरुत्थान इसके कारण थे। मेसोपोटामिया के पैमाने नहीं आए थे।")
]:
    s3_mastery_hin.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# True/False (8)
for q, ans, sol in [
    ("Mesopotamian texts refer to the Indus region as Meluhha.", True, "Cuneiform tablets identify Meluhha as the Indus Valley Civilisation."),
    ("The island of Dilmun rejected Harappan weights and used Egyptian standards.", False, "Dilmun adopted the Harappan weight standard for Gulf trade."),
    ("Tax collection in Harappan cities was verified using standardized weights.", True, "Weights were used to measure grain taxes at public granaries."),
    ("The standardization of weights collapsed during the Late Harappan phase.", True, "De-urbanization led to the decay of metrological standards."),
    ("Barter trade did not require standardized weights as no money was involved.", False, "Barter required strict weights to establish uniform exchange ratios for grain, metal, and goods."),
    ("Balance scales were owned only by municipal inspectors, not ordinary citizens.", False, "Balance scales and weights are commonly found in ordinary domestic houses."),
    ("Harappan merchants traded directly with Mesopotamian markets using chert weights.", True, "Weights matching Harappan standards have been excavated at Ur in Mesopotamia."),
    ("Iron scales were introduced in the Late Harappan phase to weigh heavy cargo.", False, "Iron was completely unknown; scales were bronze or terracotta.")
]:
    s3_mastery_eng.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("मेसोपोटामिया के प्राचीन लेखों में सिंधु क्षेत्र को 'मेलुहा' कहा गया है।", True, "कीलाक्षर पट्टियों में मेलुहा नाम सिंधु घाटी सभ्यता के लिए प्रयुक्त हुआ है।"),
    ("दिलमुन द्वीप ने हड़प्पा बाटों को अस्वीकार कर मिस्र के मानकों को अपनाया था।", False, "दिलमुन ने फारस की खाड़ी के व्यापार में हड़प्पा के बाट मानकों को ही अपनाया था।"),
    ("हड़प्पा शहरों में करों की वसूली का सत्यापन मानक बाटों से किया जाता था।", True, "राजकीय अन्नागारों में बाटों की मदद से कर का अनाज तोलकर एकत्र किया जाता था।"),
    ("उत्तर हड़प्पा काल में बाटों के मानकीकरण की व्यवस्था बिखर गई थी।", True, "शहरी पतन के बाद मापन मानकों में विविधता और क्षेत्रीयता आ गई थी।"),
    ("वस्तु विनिमय (barter) में धन का उपयोग न होने के कारण बाटों की आवश्यकता नहीं थी।", False, "वस्तु विनिमय में अनाज और धातुओं की विनिमय दर तय करने के लिए बाट आवश्यक थे।"),
    ("तराजू केवल नगर पालिका निरीक्षकों के पास होते थे, साधारण नागरिकों के पास नहीं।", False, "साधारण घरों से भी तराजू और बाट मिले हैं जो खुदरा व्यापार को दर्शाते हैं।"),
    ("हड़प्पा के व्यापारी मेसोपोटामिया के बाजारों में सीधे चर्ट बाटों से व्यापार करते थे।", True, "मेसोपोटामिया के उर शहर से हड़प्पा मानक के चर्ट बाट मिले हैं।"),
    ("उत्तर हड़प्पा काल में भारी माल तोलने के लिए लोहे के पैमाने शुरू किए गए थे।", False, "लोहा अज्ञात था; तराजू पलड़े हमेशा कांसे या मिट्टी के ही रहे।")
]:
    s3_mastery_hin.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

# Fill in the Blank (8)
for q, ans, sol in [
    ("Mesopotamian cuneiform tablets refer to the Indus valley as ________.", "Meluhha", "Meluhha was the Akkadian name for the Indus region."),
    ("The Persian Gulf trading port of ________ adopted the Harappan weight standard.", "Dilmun", "Dilmun (modern Bahrain) was a major trade partner that used Harappan weights."),
    ("Public storage facilities where grain taxes were weighed are called ________.", "granaries", "Granaries at Harappa and Mohenjo-daro stored grain tribute."),
    ("The breakdown of municipal authority in the Late Harappan phase led to the decay of ________.", "standardization", "Without municipal enforcement, metrological standardization faded."),
    ("Standard weights found in ordinary houses suggest active ________ trade.", "retail", "Finding weights in residential zones indicates domestic buying and selling."),
    ("Mesopotamian trade was based on a sexagesimal system, while Harappa used a ________-decimal system.", "binary", "Harappa used a dual binary and decimal mathematical metrology."),
    ("Balance scale pans were made of terracotta or ________ sheets.", "copper", "Copper/bronze sheet metal was beaten into scale pans."),
    ("The trade transition port of Dilmun is located in the modern country of ________.", "Bahrain", "Bahrain corresponds to the ancient island of Dilmun.")
]:
    s3_mastery_eng.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("मेसोपोटामिया की पट्टियों में सिंधु घाटी को ________ के रूप में संदर्भित किया गया है।", "मेलुहा", "मेलुहा सिंधु घाटी सभ्यता का मेसोपोटामियाई नाम था।"),
    ("फारस की खाड़ी के व्यापारिक बंदरगाह ________ ने हड़प्पा के बाट मानक को अपनाया था।", "दिलमुन", "दिलमुन (बहरीन) खाड़ी व्यापार में हड़प्पा मानकों का उपयोग करता था।"),
    ("कर के अनाज को तोलकर जमा करने वाले सार्वजनिक भवनों को ________ कहा जाता था।", "अन्नागार", "हड़प्पा और मोहनजोदड़ो के राजकीय अन्नागारों (granaries) में अनाज सुरक्षित रखा जाता था।"),
    ("उत्तर हड़प्पा काल में नगरीय प्रशासन के कमजोर होने से मापन व्यवस्था का ________ हो गया।", "पतन", "नगरपालिका नियंत्रण समाप्त होने से बाटों का मानकीकरण बिखर गया।"),
    ("साधारण घरों से बाटों का मिलना दर्शाता है कि वहाँ स्थानीय स्तर पर ________ व्यापार होता था।", "खुदरा", "घरों से बाटों का मिलना खुदरा व्यापार और रोजमर्रा के लेन-देन को दर्शाता है।"),
    ("मेसोपोटामिया का व्यापार षष्ठदशमलव था, जबकि हड़प्पा का व्यापार ________-दशमलव प्रणाली पर था।", "बाइनरी", "हड़प्पा वासी बाइनरी और दशमलव की दोहरी प्रणाली का उपयोग करते थे।"),
    ("तराजू के पलड़े पकी मिट्टी या ________ की पतली चादरों से बनते थे।", "तांबे", "तांबे और कांसे के पलड़े हथौड़े से ठोककर बनाए जाते थे।"),
    ("फारस की खाड़ी का प्राचीन व्यापारिक केंद्र दिलमुन आज के ________ देश में स्थित है।", "बहरीन", "आधुनिक बहरीन देश ही प्राचीन काल का दिलमुन था।")
]:
    s3_mastery_hin.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

# Match the Following (3)
s3_matches_eng = [
    {"q": "Match the trade entity with its corresponding metrological role:",
     "pairs": ["Meluhha - Source of standardized chert weights", "Dilmun - Port adopting the Harappan standard", "Mesopotamia - Destination using sexagesimal base-60", "Ur - Site yielding Harappan weights"],
     "sol": "Meluhha represents the Indus region; Dilmun adopted Harappan weights; Mesopotamia used base-60; Ur yielded chert weights."},
    {"q": "Match the archaeological context with the administrative function:",
     "pairs": ["Citadel Granary - Collection and weighing of grain taxes", "Lower Town House - Local retail transactions and barter", "Rohri Quarry - Sourcing and rough-shaping chert", "Chanhudaro workshop - Precision weighing of gold beads"],
     "sol": "Links the physical findspots with their specific socio-economic uses."},
    {"q": "Match the metrological phase with its historical description:",
     "pairs": ["Mature Harappan - Peak of pan-regional standardization", "Late Harappan - Fragmentation into localized regional units", "Early Harappan - Initial experimentation with local ratios", "British Indian - Retention of the base-16 binary anna system"],
     "sol": "Integrates the evolutionary phases of Indian metrology with their core characteristics."}
]
s3_mastery_eng.extend([make_match_question(m) for m in s3_matches_eng])

s3_matches_hin = [
    {"q": "व्यापारिक क्षेत्रों को उनकी मापन भूमिकाओं से सुमेलित करें:",
     "pairs": ["मेलुहा - मानक चर्ट बाटों का स्रोत क्षेत्र", "दिलमुन - हड़प्पा बाटों को अपनाने वाला खाड़ी बंदरगाह", "मेसोपोटामिया - षष्ठदशमलव (base-60) का उपयोग करने वाला क्षेत्र", "उर - हड़प्पा बाटों की प्राप्ति वाला शहर"],
     "sol": "मेलुहा सिंधु क्षेत्र है; दिलमुन ने हड़प्पा बाटों को अपनाया; मेसोपोटामिया में बेस-60 था; उर से चर्ट बाट मिले हैं।"},
    {"q": "पुरातात्विक खोज के संदर्भ को प्रशासनिक कार्यों से सुमेलित करें:",
     "pairs": ["दुर्ग का अन्नागार - अनाज करों का तौल और संग्रहण", "निचले शहर का मकान - स्थानीय खुदरा वस्तु विनिमय", "रोहरी की खदान - चर्ट पत्थरों का खनन और कट्स", "चन्हुदड़ो की कार्यशाला - सोने के आभूषणों का सूक्ष्म मापन"],
     "sol": "प्राप्ति स्थानों को उनके व्यावहारिक आर्थिक उपयोगों से सुमेलित करता है।"},
    {"q": "मापन प्रणालियों के ऐतिहासिक चरणों को उनके विवरण से सुमेलित करें:",
     "pairs": ["परिपक्व हड़प्पा - अखिल-क्षेत्रीय मानकीकरण का चरम काल", "उत्तर हड़प्पा - स्थानीय क्षेत्रीय मापों में विभाजन का काल", "प्रारंभिक हड़प्पा - स्थानीय मानकों के प्रयोग का काल", "ब्रिटिश भारत - बाइनरी 16 पर आधारित आने (anna) प्रणाली का बने रहना"],
     "sol": "भारतीय मापन प्रणालियों के क्रमिक ऐतिहासिक विकास को उनके मुख्य लक्षणों से जोड़ता है।"}
]
s3_mastery_hin.extend([make_match_question(m) for m in s3_matches_hin])

# One-Liner (8)
for q, sol in [
    ("What ancient Akkadian name corresponds to the Indus Valley Civilisation?", "Meluhha."),
    ("Which Persian Gulf island served as a key transit port and adopted Harappan weights?", "Dilmun (Bahrain)."),
    ("Where were grain taxes collected and measured in Mature Harappan cities?", "In the public granaries and warehouses located in Citadels."),
    ("What does the presence of weights in lower town houses reveal about retail trade?", "It reveals that trade was decentralized, allowing ordinary households to conduct retail barter transactions directly."),
    ("What was the mathematical base of the Mesopotamian weight system?", "Sexagesimal (base-60) system."),
    ("What caused the disintegration of standardized weights in the Late Harappan phase?", "The collapse of urban centers, municipal administrations, and long-distance trade routes."),
    ("What metal was beaten into sheets to manufacture weighing pans?", "Copper or bronze."),
    ("Which trade commodity from Meluhha was highly prized in Mesopotamian palaces?", "Ivory objects (carved combs, luxury items) and carnelian beads.")
]:
    s3_mastery_eng.append({"type": "One-Liner", "q": q, "sol": sol})

for q, sol in [
    ("मेसोपोटामिया के प्राचीन कीलाक्षर ग्रंथों में सिंधु सभ्यता के लिए क्या नाम आया है?", "मेलुहा (Meluhha)।"),
    ("हड़प्पा बाटों को अपनाने वाला फारस की खाड़ी का प्रमुख पारगमन बंदरगाह कौन सा था?", "दिलमुन (आधुनिक बहरीन)।"),
    ("परिपक्व हड़प्पा शहरों में कर के रूप में लिए जाने वाले अनाज को कहाँ तोलकर जमा किया जाता था?", "दुर्गों में स्थित सार्वजनिक अन्नागारों (granaries) और गोदामों में।"),
    ("निचले शहरों के घरों में बाटों का पाया जाना खुदरा व्यापार के बारे में क्या दर्शाता है?", "यह दर्शाता है कि व्यापार विकेंद्रीकृत था, और साधारण लोग भी घरों के स्तर पर दैनिक क्रय-विक्रय करते थे।"),
    ("मेसोपोटामिया की बाट प्रणाली का गणितीय आधार क्या था?", "षष्ठदशमलव (sexagesimal - base-60) प्रणाली।"),
    ("उत्तर हड़प्पा काल में मापन प्रणालियों के विखंडन का मुख्य कारण क्या था?", "शहरी पतन, नगरपालिकाओं के नियंत्रण की समाप्ति और दूरगामी व्यापार मार्गों का बंद होना।"),
    ("तराजू के पलड़े बनाने के लिए किस धातु की चादरों को ठोककर आकार दिया जाता था?", "तांबे या कांसे की।"),
    ("मेसोपोटामिया के राजमहलों में मेलुहा से आयातित किस विलासिता की वस्तु की भारी मांग थी?", "हाथीदांत की वस्तुओं (तराशी हुई कंघियों आदि) तथा कार्नेलियन के लाल मनकों की।")
]:
    s3_mastery_hin.append({"type": "One-Liner", "q": q, "sol": sol})

# Assertion-Reason (8)
for q, ans, sol in [
    ("Assertion (A): Cuneiform texts indicate active metrological contacts between Mesopotamia and Meluhha.\nReason (R): Standard Harappan chert weights have been excavated at Mesopotamian sites like Ur.", 0, "Both A and R are true, and the chert weights found at Ur verify the metrological contacts mentioned in cuneiform texts."),
    ("Assertion (A): Dilmun adopted the Harappan weight standard for Gulf trade.\nReason (R): Dilmun was a colony under direct military control of the Harappan priest-king.", 2, "A is true; R is false. Dilmun adopted the weights due to Harappan commercial dominance, not military colonisation."),
    ("Assertion (A): Granaries at Harappa served as trade tax verification hubs.\nReason (R): Standard weights and scale fragments are found in high concentrations near granary entrances.", 0, "Both A and R are true, and the find of metrological equipment near granary entrances verifies their tax role."),
    ("Assertion (A): Standardized weights disappeared in the Late Harappan phase.\nReason (R): The collapse of long-distance Gulf trade and de-urbanization removed the administrative need for standardized weights.", 0, "Both A and R are true, and the trade collapse explaining the decline of municipal standardization is correct."),
    ("Assertion (A): Barter trade was difficult to regulate in Harappan lower towns.\nReason (R): Standard weights in lower town houses show that citizens had uniform tools to calculate barter values.", 3, "A is false; R is true. Standard weights actually made barter regulation very efficient for ordinary citizens."),
    ("Assertion (A): Mesopotamian merchants easily converted weights during Gulf trade.\nReason (R): Dilmun acted as a metrological bridge, using the Harappan standard which had established exchange ratios with Mesopotamia.", 0, "Both A and R are true, and Dilmun's bridging role explains how merchants converted different systems."),
    ("Assertion (A): Weights found in houses were used only for weighing wedding dowries.\nReason (R): Dowries in Harappan culture were strictly regulated by municipal laws based on chert weights.", 4, "Both A and R are false. Weights in houses were used for retail trade, craft measurements, and general barter transactions."),
    ("Assertion (A): Iron weights were introduced in Mesopotamian trade routes during the Mature Harappan phase.\nReason (R): Iron was the most common metal traded from the Indus to Mesopotamia in the Bronze Age.", 4, "Both A and R are false. Iron was unknown to both Harappa and Mesopotamia during the Bronze Age; trade was in copper/bronze.")
]:
    s3_mastery_eng.append({"type": "Assertion-Reason", "q": q, "opts": ar_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("कथन (A): मेसोपोटामिया के कीलाक्षर लेख मेलुहा और उनके बीच सक्रिय व्यापारिक मापन संपर्कों को दर्शाते हैं।\nकारण (R): मेसोपोटामिया के उर जैसे स्थलों के उत्खनन से हड़प्पा मानक के चर्ट बाट मिले हैं।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या है। उर से मिले बाट ग्रंथों के व्यापार दावों की पुष्टि करते हैं।"),
    ("कथन (A): दिलमुन ने खाड़ी व्यापार के लिए हड़प्पा के बाट मानकों को अपनाया था।\nकारण (R): दिलमुन हड़प्पा के पुरोहित-राजा के सीधे सैन्य नियंत्रण में एक उपनिवेश था।", 2, "A सही है लेकिन R गलत है। दिलमुन ने व्यापारिक प्रभाव के कारण बाटों को अपनाया था, सैन्य कब्जे के कारण नहीं।"),
    ("कथन (A): हड़प्पा के अन्नागार व्यापार कर सत्यापन केंद्रों के रूप में कार्य करते थे।\nकारण (R): अन्नागारों के प्रवेश द्वारों के पास भारी संख्या में बाट और तराजू के टुकड़े मिले हैं।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या है।"),
    ("कथन (A): उत्तर हड़प्पा काल में मानकीकृत बाट प्रणालियाँ समाप्त हो गईं।\nकारण (R): खाड़ी व्यापार के पतन और शहरों के ह्रास ने बाटों को नियंत्रित करने वाली नगरपालिका नियंत्रण व्यवस्था को समाप्त कर दिया था।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या है।"),
    ("कथन (A): हड़प्पा के निचले शहरों में वस्तु विनिमय व्यापार का नियमन करना बहुत कठिन था।\nकारण (R): निचले शहरों के घरों से मिले बाट यह दर्शाते हैं कि नागरिकों के पास वस्तु विनिमय का मूल्य तोलने के समान साधन थे।", 3, "A गलत है लेकिन R सही है। बाटों की उपलब्धता ने वस्तु विनिमय के नियमन को अत्यधिक सुगम और विश्वसनीय बनाया था।"),
    ("कथन (A): मेसोपोटामिया के व्यापारियों को खाड़ी व्यापार में बाटों का परिवर्तन करने में कोई कठिनाई नहीं होती थी।\nकारण (R): दिलमुन एक मापन सेतु था जो हड़प्पा बाट मानकों का उपयोग करता था, जिनकी मेसोपोटामियाई मापों के साथ विनिमय दरें तय थीं।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या है।"),
    ("कथन (A): घरों से मिले बाटों का उपयोग केवल विवाह में दहेज के आभूषणों को तोलने के लिए होता था।\nकारण (R): हड़प्पा संस्कृति में दहेज का नियमन सख्त नगर पालिका कानूनों द्वारा चर्ट बाटों के आधार पर किया जाता था।", 4, "A और R दोनों गलत हैं। बाटों का उपयोग दैनिक फुटकर व्यापार और शिल्प कार्यों में किया जाता था।"),
    ("कथन (A): परिपक्व हड़प्पा काल में मेसोपोटामियाई व्यापारिक मार्गों पर लोहे के बाटों का प्रचलन शुरू हुआ था।\nकारण (R): कांस्य युग में सिंधु घाटी से मेसोपोटामिया को निर्यात की जाने वाली सबसे आम धातु लोहा थी।", 4, "A और R दोनों गलत हैं। कांस्य युग में लोहे का कोई अस्तित्व नहीं था; तांबे और कांसे का ही व्यापार होता था।")
]:
    s3_mastery_hin.append({"type": "Assertion-Reason", "q": q, "opts": hin_ar_opts, "ans": ans, "sol": sol})

# Statement-Based (5)
for q, ans, sol in [
    ("Consider the following statements:\nStatement 1: Cuneiform inscriptions mention imports of gold, ivory, and carnelian from Meluhha.\nStatement 2: Meluhha is the ancient Mesopotamian geographical term for Egypt.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: Meluhha is the term for the Indus Valley Civilisation."),
    ("Consider the following statements:\nStatement 1: The island of Dilmun functioned as a middleman port, adopting Harappan weights.\nStatement 2: Dilmun corresponds to modern-day Bahrain in the Persian Gulf.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct. Dilmun was a trade hub in Bahrain using Harappan weights."),
    ("Consider the following statements:\nStatement 1: Standardized weights are found only in royal palace zones.\nStatement 2: Ordinary homes yielded balance scales, showing household-level trade.\nWhich of the statements given above is/are correct?", 1, "Statement 2 is correct. Statement 1 is incorrect: weights are found throughout lower towns."),
    ("Consider the following statements:\nStatement 1: Mesopotamian trade relied on base-60 mathematics, while Harappan metrology used binary-decimal.\nStatement 2: Harappan merchants refused to trade with Mesopotamia due to these metrological differences.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: trade was highly active, with merchants converting weights at Gulf hubs."),
    ("Consider the following statements:\nStatement 1: The Late Harappan phase saw the breakdown of municipal weight systems.\nStatement 2: Late Harappans adopted the Mesopotamian weight system to revive trade.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: Late Harappans returned to localized, non-standardized systems; they did not adopt Mesopotamian standards.")
]:
    s3_mastery_eng.append({"type": "Statement-Based", "q": q, "opts": mcq_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: मेसोपोटामिया के कीलाक्षर ग्रंथों में मेलुहा से सोने, हाथीदांत और कार्नेलियन के आयात का उल्लेख है।\nकथन 2: मेलुहा प्राचीन मेसोपोटामियाई भूगोल में मिस्र देश का नाम था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि मेलुहा सिंधु घाटी सभ्यता का नाम था।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: दिलमुन द्वीप ने एक बिचौलिए बंदरगाह के रूप में कार्य किया जिसने हड़प्पा बाट मानकों को अपनाया।\nकथन 2: दिलमुन फारस की खाड़ी के आधुनिक बहरीन देश का प्राचीन नाम है।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 2, "दोनों कथन सही हैं। दिलमुन बहरीन में था और व्यापार के लिए हड़प्पा बाटों का उपयोग करता था।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: मानकीकृत बाट केवल राजमहलों और दुर्गों के क्षेत्रों से ही प्राप्त हुए हैं।\nकथन 2: साधारण घरों से तराजू के पलड़े मिले हैं, जो घरेलू खुदरा व्यापार की पुष्टि करते हैं।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 1, "कथन 2 सही है। कथन 1 गलत है क्योंकि बाट साधारण आवासीय बस्तियों से भी मिले हैं।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: मेसोपोटामिया का व्यापार आधार-60 (sexagesimal) पर तथा हड़प्पा का व्यापार बाइनरी-दशमलव पर आधारित था।\nकथन 2: मापन प्रणालियों में अंतर के कारण हड़प्पा के व्यापारियों ने मेसोपोटामिया से व्यापार बंद कर दिया था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि दोनों सभ्यताओं में खाड़ी बंदरगाहों के माध्यम से बहुत सक्रिय व्यापार होता था।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: उत्तर हड़प्पा काल में नगरपालिकाओं की बाट प्रणाली पूरी तरह बिखर गई थी।\nकथन 2: व्यापार को बचाने के लिए उत्तर हड़प्पा वासियों ने मेसोपोटामिया की बाट प्रणाली को अपना लिया था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि उन्होंने विदेशी प्रणाली नहीं अपनाई, बल्कि वे स्थानीय गैर-मानकीकृत मापों की ओर लौट गए।")
]:
    s3_mastery_hin.append({"type": "Statement-Based", "q": q, "opts": hin_mcq_opts, "ans": ans, "sol": sol})

# Why (3)
for q, sol in [
    ("Why did the island of Dilmun adopt the Harappan weight standard instead of the Mesopotamian one?", "Because Harappan merchants dominated the Persian Gulf trade routes, exporting massive quantities of luxury beads, textiles, and ivory. Dilmun adopted the standard to facilitate commerce with their most powerful trade partner."),
    ("Why did the standardization of weights collapse so rapidly during the Late Harappan transition?", "The decline of municipal governments in cities like Mohenjo-daro meant there was no administrative authority to inspect, calibrate, or enforce weight standards. Additionally, the decline of long-distance trade removed the need for uniform regional metrology."),
    ("Why was metrological standardization vital for collecting state tax in Harappan citadels?", "To ensure fairness and consistency. Grain stored in state granaries was collected as tribute or tax; standardized weights prevented tax evasion by taxpayers and corruption or double-dipping by state tax-collectors.")
]:
    s3_mastery_eng.append({"type": "Why", "q": q, "sol": sol})

for q, sol in [
    ("दिलमुन द्वीप ने मेसोपोटामिया के बजाय हड़प्पा के बाट मानकों को क्यों अपनाया था?", "क्योंकि खाड़ी के व्यापार मार्गों पर हड़प्पा के व्यापारियों का प्रभुत्व था। दिलमुन ने अपने सबसे बड़े व्यापारिक साझेदार (सिंधु सभ्यता) के साथ लेनदेन को सरल बनाने के लिए इन बाटों को अपनाया।"),
    ("उत्तर हड़प्पा संक्रमण काल के दौरान बाटों का मानकीकरण इतनी तेजी से क्यों समाप्त हो गया?", "क्योंकि मोहनजोदड़ो जैसे शहरों में नागरिक प्रशासनों के पतन के बाद बाटों की जांच और नियंत्रण करने वाली कोई सत्ता नहीं बची। साथ ही, विदेशी व्यापार बंद होने से एकसमान मापन की आवश्यकता भी समाप्त हो गई।"),
    ("हड़प्पा दुर्गों में राजकीय कर वसूलने के लिए मापन मानकीकरण क्यों आवश्यक था?", "कर संग्रहण में निष्पक्षता और एकरूपता बनाए रखने के लिए। राजकीय अन्नागारों में अनाज कर के रूप में एकत्र होता था; निश्चित बाटों ने कर चोरी तथा कर वसूलने वाले अधिकारियों के भ्रष्टाचार को रोकने में सहायता की।")
]:
    s3_mastery_hin.append({"type": "Why", "q": q, "sol": sol})

# How (3)
for q, sol in [
    ("How did Mesopotamian texts verify the imports of commodities measured by Harappan standards?", "Akkadian tablets list imports of ivory objects, carnelian beads, and royal timber from 'Meluhha'. The discovery of Harappan chert weights at Ur confirms these goods were weighed and traded under Meluhhan standards."),
    ("How did the presence of scales in lower towns prove the existence of a middle-class merchant network?", "By showing that weighing and trading were not state monopolies restricted to citadels. Ordinary lower-town citizens owned the tools to weigh and exchange goods, proving a thriving, decentralized retail economy."),
    ("How did Late Harappan populations adapt to the collapse of standardized weights?", "They returned to localized, regional barter networks. They abandoned precise chert cubical weights and ivory scales, relying instead on opportunistic heap measures and variable local stone weights, leading to economic fragmentation.")
]:
    s3_mastery_eng.append({"type": "How", "q": q, "sol": sol})

for q, sol in [
    ("मेसोपोटामिया के लेखों ने हड़प्पा मापन मानकों के अनुसार विनिमय की पुष्टि कैसे की?", "अक्कदी पट्टियों में मेलुहा से हाथीदांत की वस्तुओं और मनकों के आयात की सूची है। उर में हड़प्पा बाटों की खोज यह दर्शाती है कि इन वस्तुओं का तौल और मूल्यांकन हड़प्पा मानकों पर होता था।"),
    ("निचले शहरों में तराजू-बाटों की उपस्थिति ने एक मध्यवर्गीय व्यापारी नेटवर्क के अस्तित्व को कैसे सिद्ध किया?", "यह दर्शाता है कि तौलना और व्यापार करना केवल दुर्गों के शासकों का एकाधिकार नहीं था। निचले शहर के आम नागरिकों के पास स्वयं के तौल उपकरण थे, जो एक जीवंत, विकेंद्रीकृत खुदरा अर्थव्यवस्था को दर्शाते हैं।"),
    ("उत्तर हड़प्पा समुदायों ने मानकीकृत बाटों के पतन के बाद स्वयं को कैसे ढाला?", "वे स्थानीय और क्षेत्रीय व्यापार नेटवर्क की ओर लौट गए। उन्होंने चर्ट के बाटों और हाथीदांत पैमानों को छोड़कर साधारण पत्थरों और स्थानीय अनुमानों पर आधारित तौल प्रणालियों को अपना लिया, जिससे आर्थिक विकेंद्रीकरण हुआ।")
]:
    s3_mastery_hin.append({"type": "How", "q": q, "sol": sol})

# Case Study (3)
for q, sol in [
    ("Examine a case study of Harappan chert weights discovered in Mesopotamia (Ur). What does it prove about trade integration?", "The discovery of a set of polished chert cubical weights at Ur matching the Harappan unit of 13.63g indicates that Harappan merchants resided or traded directly in Sumerian cities, maintaining their own metrological standards to avoid trade disputes."),
    ("Evaluate the metrological findings at Dilmun (Bahrain). How does this support Gulf trade systems?", "Dilmun excavations yielded weights that follow the Harappan standard. Dilmun served as a gateway between Mesopotamia and Harappa. The adoption of Harappan weights shows that Dilmun integrated its economy with the Indus Valley to facilitate Gulf shipping."),
    ("Analyze the de-urbanization transition at Late Harappan sites in Gujarat. What happened to metrological artifacts?", "Excavations at Late Harappan levels in Gujarat show a decline in chert weights. Masons abandoned chert and made crude weights from local sandstone or terracotta, representing a loss of precision and the fragmentation of the pan-regional trade network.")
]:
    s3_mastery_eng.append({"type": "Case Study", "q": q, "sol": sol})

for q, sol in [
    ("मेसोपोटामिया (Ur) से प्राप्त हड़प्पा चर्ट बाटों के केस स्टडी का परीक्षण करें। यह व्यापारिक एकीकरण के बारे में क्या सिद्ध करता है?", "उर से हड़प्पा की 13.63 ग्राम की इकाई से मेल खाने वाले घनाकार चर्ट बाटों का मिलना यह दर्शाता है कि हड़प्पा के व्यापारी सुमेरियन शहरों में सीधे रहकर व्यापार करते थे और अपने स्वतंत्र बाट मानकों का उपयोग करते थे।"),
    ("दिलमुन (बहरीन) के मापन साक्ष्यों का मूल्यांकन करें। यह खाड़ी व्यापार प्रणालियों का किस प्रकार समर्थन करता है?", "दिलमुन की खुदाई से प्राप्त बाट हड़प्पा मानक का पालन करते हैं। दिलमुन मेसोपोटामिया और सिंधु सभ्यता के बीच का प्रवेश द्वार था। हड़प्पा बाटों को अपनाना यह दर्शाता है कि दिलमुन की अर्थव्यवस्था खाड़ी नौवहन के लिए सिंधु घाटी से जुड़ी थी।"),
    ("गुजरात के उत्तर हड़प्पा स्थलों पर शहरीकरण के अंत के काल का विश्लेषण करें। मापन कलाकृतियों का क्या हुआ?", "गुजरात के उत्तर हड़प्पा स्तरों में चर्ट के बाटों में भारी गिरावट देखी गई। शिल्पकारों ने चर्ट का उपयोग छोड़कर स्थानीय बलुआ पत्थर और मिट्टी से खुरदरे बाट बनाए, जो व्यापारिक नेटवर्क के विखंडन को दर्शाता है।")
]:
    s3_mastery_hin.append({"type": "Case Study", "q": q, "sol": sol})

# Teach Concept (3)
for q, sol in [
    ("Explain the concept of 'Metrological Hegemony' in ancient maritime trade, using Dilmun as an example.", "Metrological Hegemony occurs when a dominant trading power influences its partners to adopt its measurement standards. In the Bronze Age Gulf trade, Dilmun adopted the Harappan weight standard because Indus merchants controlled the flow of luxury goods, establishing the Harappan standard as the commercial currency of the Persian Gulf."),
    ("Describe how municipal tax collection was organized in Harappan citadels using standardized weights.", "Citadels housed central granaries and warehouses. Farmers and traders brought agricultural surplus as tax. Tax collectors verified these deposits using large ring-stones and limestone weights on suspended balance scales, ensuring accurate registry and preventing municipal fraud."),
    ("Reconstruct the economic transitions that occurred in weights and measures during the Late Harappan de-urbanization.", "With the collapse of municipal administrations around 1900 BCE, central inspection of weights ceased. Long-distance trade with Mesopotamia ended, removing the need for a pan-regional standard. Consequently, the uniform Rohri chert weights and precise ivory scales fell out of use, replaced by localized, variable stone and clay weights in fragmented rural economies.")
]:
    s3_mastery_eng.append({"type": "Teach Concept", "q": q, "sol": sol})

for q, sol in [
    ("दिलमुन का उदाहरण देते हुए, प्राचीन समुद्री व्यापार में 'मापन प्रभुत्व' (Metrological Hegemony) की अवधारणा को स्पष्ट करें।", "मापन प्रभुत्व तब होता है जब एक बड़ी व्यापारिक शक्ति अपने भागीदारों को अपने मापन मानकों को अपनाने के लिए प्रभावित करती है। खाड़ी व्यापार में दिलमुन ने हड़प्पा बाटों को इसलिए अपनाया क्योंकि सिंधु के व्यापारी विलासिता के सामानों के प्रवाह को नियंत्रित करते थे।"),
    ("मानकीकृत बाटों की मदद से हड़प्पा दुर्गों में नगरपालिका कर संग्रहण कैसे आयोजित किया जाता था, इसका वर्णन करें।", "दुर्गों में केंद्रीय अन्नागार होते थे। किसान और व्यापारी कर के रूप में अनाज लाते थे। कर संग्राहक बड़े चूना पत्थरों और लटके हुए तराजू की मदद से इन जमाओं का सत्यापन करते थे, जिससे कर धोखाधड़ी रुकती थी।"),
    ("उत्तर हड़प्पा वि-शहरीकरण (de-urbanization) के दौरान बाट और माप प्रणालियों में हुए आर्थिक परिवर्तनों का पुनर्निर्माण करें।", "1900 ईसा पूर्व के बाद नागरिक प्रशासनों के पतन से बाटों का केंद्रीय निरीक्षण बंद हो गया। मेसोपोटामिया से व्यापार बंद होने से साझा मानकों की आवश्यकता समाप्त हो गई। फलतः रोहरी चर्ट के बाटों का स्थान खुरदरे स्थानीय बाटों ने ले लिया।")
]:
    s3_mastery_hin.append({"type": "Teach Concept", "q": q, "sol": sol})


# Trigger injection logic
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
