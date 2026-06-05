import json
import os

ENG_PATH = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\HarappanIndus-Valley-Civilisation\Agriculture\content.json"
HIN_PATH = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\HarappanIndus-Valley-Civilisation\Agriculture\hi\content.json"

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
# SECTION 1: CROPS AND ANIMAL DOMESTICATION
# =========================================================================
s1_mastery_eng = []
s1_mastery_hin = []

# MCQ (5)
for q, opts, ans, sol in [
    ("Which of the following was the primary fiber crop cultivated by the Harappans, later exported to the West?", ["Cotton", "Jute", "Flax", "Hemp"], 0, "The Harappans were pioneers in cultivating cotton, which was a major export commodity."),
    ("Wheat and barley cultivated by the Harappans were predominantly grown as which crop type?", ["Rabi (winter) crops", "Kharif (summer) crops", "Zaid (seasonal) crops", "Plantation crops"], 0, "Wheat and barley were winter (Rabi) crops planted after floods receded."),
    ("At which site in Saurashtra did archaeologists discover direct evidence of rice husks embedded in pottery?", ["Lothal", "Surkotada", "Dholavira", "Nageshwar"], 0, "Lothal (and Rangpur) yielded evidence of rice husks, indicating localized rice growing."),
    ("Which domesticated animal, represented as the humped bull in Harappan art, was highly revered?", ["Zebu cattle", "Water buffalo", "Bactrian camel", "African elephant"], 0, "The humped bull or zebu cattle (Bos indicus) was highly revered and common."),
    ("The controversial skeletal remains of a horse, highly debated in Aryan migration theories, were found at which site?", ["Surkotada", "Kalibangan", "Mohenjo-daro", "Banawali"], 0, "Surkotada in Gujarat yielded horse bones, though horse domestication in Harappa remains highly debated.")
]:
    s1_mastery_eng.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("निम्नलिखित में से कौन सी हड़प्पा वासियों द्वारा उगाई जाने वाली प्राथमिक रेशा (fiber) फसल थी, जिसका बाद में पश्चिम में निर्यात किया गया?", ["कपास", "जूट", "सन (Flax)", "भांग"], 0, "हड़प्पा वासी कपास उगाने के अग्रदूत थे, जो एक प्रमुख निर्यात वस्तु थी।"),
    ("हड़प्पा वासियों द्वारा उगाई जाने वाली गेहूँ और जौ मुख्य रूप से किस प्रकार की फसलें थीं?", ["रबी (शीतकालीन) फसलें", "खरीफ (ग्रीष्मकालीन) फसलें", "जायद (मौसमी) फसलें", "रोपण फसलें"], 0, "गेहूँ और जौ रबी (शीतकालीन) फसलें थीं जो बाढ़ उतरने के बाद बोई जाती थीं।"),
    ("सौराष्ट्र के किस स्थल पर पुरातत्वविदों को मिट्टी के बर्तनों में धान (चावल) की भूसी के सीधे साक्ष्य मिले हैं?", ["लोथल", "सुरकोटदा", "धोलावीरा", "नागेश्वर"], 0, "लोथल (और रंगपुर) से चावल की भूसी मिली है, जो स्थानीय धान की खेती को दर्शाती है।"),
    ("हड़प्पा कला में कूबड़ वाले बैल के रूप में दर्शाए गए किस पालतू जानवर को अत्यधिक पूजनीय माना जाता था?", ["कूबड़ वाले बैल (Zebu)", "भैंस", "ऊँट", "अफ्रीकी हाथी"], 0, "कूबड़ वाले बैल (zebu/Bos indicus) को मुहरों पर सजीवता से उकेरा गया है और इसका बड़ा महत्व था।"),
    ("आर्यन प्रवास सिद्धांतों में अत्यधिक चर्चित घोड़े के विवादास्पद अस्थि अवशेष किस स्थल पर पाए गए थे?", ["सुरकोटदा", "कालीबंगन", "मोहनजोदड़ो", "बनावली"], 0, "गुजरात के सुरकोटदा से घोड़े की हड्डियां मिली हैं, हालांकि इसका पालतू होना अत्यधिक विवादास्पद है।")
]:
    s1_mastery_hin.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# Multiple Correct MCQ (5)
for q, opts, ans, sol in [
    ("Which of the following animals were domesticated by the Harappans for agricultural or transport draft work? (Select all that apply)", ["Humped cattle (oxen)", "Water buffaloes", "Bactrian camels", "African elephants"], [0, 1, 2], "Humped cattle, buffaloes, and camels were domesticated. African elephants were not known."),
    ("Select the winter crops (Rabi suite) that were cultivated in the Indus plains: (Select all that apply)", ["Wheat and Barley", "Peas and Lentils", "Mustard and Sesame", "Sugarcane"], [0, 1, 2], "Wheat, barley, peas, lentils, mustard, and sesame were grown. Sugarcane was unknown."),
    ("Which dry-crop millets were cultivated by the Harappans in the semi-arid Saurashtra/Gujarat region? (Select all that apply)", ["Ragi", "Jowar", "Bajra", "Oats"], [0, 1, 2], "Ragi, jowar, and bajra were millets grown in Gujarat. Oats were not cultivated."),
    ("Which of the following physical features characterize the Zebu cattle depicted on Harappan seals? (Select all that apply)", ["A large fatty hump", "Long, prominent curved horns", "A heavy dewlap under the neck", "A flat, humpless back"], [0, 1, 2], "Zebu cattle seals show a large fatty hump, long curved horns, and heavy dewlaps, not a flat back."),
    ("Identify the wild animal remains found in Harappan kitchen refuse or bone assemblages: (Select all that apply)", ["Rhinoceros", "Elephants", "Deer and Wild Boar", "Kangaroos"], [0, 1, 2], "Rhino, elephant, deer, and wild boar bones are found in refuse. Kangaroos are native to Australia.")
]:
    s1_mastery_eng.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("हड़प्पा वासियों द्वारा कृषि या परिवहन के लिए किन जानवरों को पालतू बनाया गया था? (सभी लागू विकल्प चुनें)", ["कूबड़ वाले बैल", "भैंस", "ऊँट", "अफ्रीकी हाथी"], [0, 1, 2], "बैल, भैंस और ऊँट पालतू थे। वे अफ्रीकी हाथी से परिचित नहीं थे।"),
    ("सिंधु मैदानों में उगाई जाने वाली रबी (शीतकालीन) फसलों का चयन करें: (सभी लागू विकल्प चुनें)", ["गेहूँ और जौ", "मटर और मसूर", "सरसों और तिल", "गन्ना"], [0, 1, 2], "गेहूँ, जौ, मटर, मसूर, सरसों और तिल रबी फसलें थीं। गन्ने की खेती नहीं की जाती थी।"),
    ("सौराष्ट्र/गुजरात के शुष्क क्षेत्र में हड़प्पा वासियों द्वारा किन मोटे अनाजों (बाजरा) की खेती की जाती थी? (सभी लागू विकल्प चुनें)", ["रागी", "ज्वार", "बाजरा", "जई (Oats)"], [0, 1, 2], "गुजरात में रागी, ज्वार और बाजरे की खेती होती थी। जई (oats) नहीं उगाई जाती थी।"),
    ("हड़प्पा मुहरों पर चित्रित कूबड़ वाले बैल (Zebu) की शारीरिक विशेषताएं क्या थीं? (सभी लागू विकल्प चुनें)", ["एक बड़ा कूबड़", "लंबे और घुमावदार सींग", "गर्दन के नीचे भारी गलकंबल (dewlap)", "एक सपाट कूबड़-रहित पीठ"], [0, 1, 2], "कूबड़ वाले बैल का अंकन बड़ा कूबड़, लंबे सींग और गलकंबल दिखाता है, सपाट पीठ नहीं।"),
    ("हड़प्पा के कचरे के ढेरों या हड्डियों के अवशेषों में किन जंगली जानवरों की पहचान की गई है? (सभी लागू विकल्प चुनें)", ["गैंडा", "हाथी", "हिरण और जंगली सूअर", "कंगारू"], [0, 1, 2], "गैंडे, हाथी, हिरण और जंगली सूअर के अवशेष मिले हैं। कंगारू ऑस्ट्रेलिया में पाए जाते हैं।")
]:
    s1_mastery_hin.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# True/False (8)
for q, ans, sol in [
    ("Sugarcane was a major staple food crop cultivated by the Harappans in Punjab.", False, "False. Sugarcane was completely unknown to the Harappans."),
    ("The humped bull (zebu) was highly valued and realistically depicted on Harappan seals.", True, "True. The humped bull is one of the most common and artistically rendered animal motifs on seals."),
    ("The Harappans were the first civilization in the world to cultivate cotton.", True, "True. Cotton traces found at Mohenjo-daro date back to c. 3000 BCE, confirming early cultivation."),
    ("Camel bones have been recovered from the site of Kalibangan in Rajasthan.", True, "True. Camel bones show that camels were used for desert transport in Rajasthan."),
    ("Rice was the primary staple crop consumed in all major northern cities of Sindh and Punjab.", False, "False. Rice was rare and localized to Gujarat; wheat and barley were the staples in the north."),
    ("Pig bones found in urban refuse indicate they were domesticated and consumed for meat.", True, "True. Pig bones are common in kitchen middens, reflecting dietary habits."),
    ("The horse was the most common animal depicted on Harappan administrative seals.", False, "False. The horse is completely absent from Harappan seal iconography."),
    ("Millets were widely grown by Harappan communities in the semi-arid areas of Gujarat.", True, "True. Millets like ragi and bajra were adapted to the drier Gujarat soils.")
]:
    s1_mastery_eng.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("गन्ना पंजाब में हड़प्पा वासियों द्वारा उगाई जाने वाली एक प्रमुख खाद्य फसल थी।", False, "असत्य। हड़प्पा वासी गन्ने की खेती से पूरी तरह अपरिचित थे।"),
    ("कूबड़ वाले बैल (zebu) का अत्यधिक महत्व था और मुहरों पर इसका सजीव चित्रण किया गया था।", True, "सत्य। कूबड़ वाला बैल मुहरों पर सबसे सुंदर और सामान्य रूप से चित्रित पशुओं में से एक है।"),
    ("हड़प्पा वासी विश्व में कपास की खेती करने वाले सबसे पहले लोग थे।", True, "सत्य। मोहनजोदड़ो से सूती कपड़े के अवशेष मिले हैं जो लगभग 3000 ईसा पूर्व के हैं।"),
    ("राजस्थान के कालीबंगन स्थल से ऊँट की हड्डियाँ प्राप्त हुई हैं।", True, "सत्य। कालीबंगन से ऊँट की हड्डियाँ मिली हैं, जिससे मरुस्थल में ऊँटों के उपयोग की पुष्टि होती है।"),
    ("सिंध और पंजाब के सभी प्रमुख उत्तरी शहरों में चावल मुख्य खाद्य फसल थी।", False, "असत्य। चावल गुजरात में स्थानीय स्तर पर उगाया जाता था; उत्तर में मुख्य भोजन गेहूँ और जौ थे।"),
    ("शहरी कचरे में सूअर की हड्डियों का मिलना यह दर्शाता है कि उन्हें मांस के लिए पाला जाता था।", True, "सत्य। सूअर की हड्डियाँ कचरे के ढेरों में आम हैं, जो भोजन आदतों को दर्शाती हैं।"),
    ("हड़प्पा की प्रशासनिक मुहरों पर घोड़ा सबसे आम चित्रित जानवर था।", False, "असत्य। मुहरों की नक्काशी में घोड़े का चित्रण पूरी तरह से अनुपस्थित है।"),
    ("गुजरात के शुष्क क्षेत्रों में हड़प्पा समुदायों द्वारा बाजरा (मोटा अनाज) व्यापक रूप से उगाया जाता था।", True, "सत्य। रागी और बाजरा जैसी फसलें गुजरात की शुष्क मिट्टी के अनुकूल थीं।")
]:
    s1_mastery_hin.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

# Fill Blanks (8)
for q, ans, sol in [
    ("The Greek term for cotton is ________, derived from the word Sindhu.", "Sindon", "Greeks called cotton 'sindon' due to its Indus Valley origins."),
    ("Rice husks have been discovered in Gujarat at Lothal and ________.", "Rangpur", "Lothal and Rangpur yielded rice husks embedded in pottery clay."),
    ("Humped cattle, depicted frequently on seals, are scientifically known as ________.", "zebu", "Humped cattle are known as zebu (Bos indicus)."),
    ("The two primary winter staple crops of the Harappans were wheat and ________.", "barley", "Wheat and barley were the winter (Rabi) staples."),
    ("Bones of camels used as beasts of burden have been reported from ________ in Rajasthan.", "Kalibangan", "Kalibangan has yielded camel bones."),
    ("Skeletal remains of a horse were excavated at the site of ________ in Gujarat.", "Surkotada", "Surkotada has yielded debated horse bones."),
    ("Drought-resistant millets like jowar and bajra were cultivated in ________.", "Gujarat", "Gujarat sites yielded millet remains adapted to dry farming."),
    ("Faunal remains show domesticates included cattle, sheep, goats, and ________.", "pigs", "Pigs, camels, and asses were also part of the domestic animal suite.")
]:
    s1_mastery_eng.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("कपास के लिए यूनानी शब्द ________ है, जो सिंधु शब्द से बना है।", "सिंडन", "यूनानी लोग कपास को सिंडन (Sindon) कहते थे।"),
    ("गुजरात के लोथल और ________ से धान (चावल) की भूसी खोजी गई है।", "रंगपुर", "लोथल और रंगपुर से बर्तनों के गारे में दबी धान की भूसी मिली है।"),
    ("मुहरों पर अक्सर चित्रित होने वाले कूबड़ वाले बैलों को वैज्ञानिक रूप से ________ कहा जाता है।", "जेबू", "कूबड़ वाले बैल जेबू (zebu) कहलाते हैं।"),
    ("हड़प्पा वासियों की दो प्राथमिक शीतकालीन फसलें गेहूँ और ________ थीं।", "जौ", "गेहूँ और जौ मुख्य शीतकालीन (रबी) फसलें थीं।"),
    ("भार ढोने के लिए प्रयुक्त ऊँटों की हड्डियाँ राजस्थान के ________ से प्राप्त हुई हैं।", "कालीबंगन", "कालीबंगन से ऊँट के अस्थि अवशेष मिले हैं।"),
    ("गुजरात के ________ नामक स्थल से घोड़े के अस्थि अवशेष खोजे गए थे।", "सुरकोटदा", "सुरकोटदा से घोड़े की हड्डियाँ मिली हैं।"),
    ("ज्वार और बाजरा जैसे शुष्क-अनुकूल मोटे अनाजों की खेती ________ में की जाती थी।", "गुजरात", "गुजरात के शुष्क क्षेत्रों में बाजरे की खेती व्यापक थी।"),
    ("पशु अवशेष दर्शाते हैं कि पालतू पशुओं में गाय, भेड़, बकरी और ________ शामिल थे।", "सूअर", "सूअर, ऊँट और गधे भी पालतू जानवरों की सूची में थे।")
]:
    s1_mastery_hin.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

# Matchings (3)
s1_mastery_eng.extend([
    {
        "type": "Match the Following",
        "q": "Match the crops with their primary archaeological sourcing contexts:",
        "items": [{"left": "I. Rice Husks", "key": "A"}, {"left": "II. Millets", "key": "B"}, {"left": "III. Wheat/Barley", "key": "C"}],
        "options": [{"val": "A", "text": "A. Lothal and Rangpur (Gujarat)"}, {"val": "B", "text": "B. Arid Saurashtra settlements"}, {"val": "C", "text": "C. Northern plains staple suite"}],
        "sol": "Rice husks are at Lothal/Rangpur, millets in dry Saurashtra, and wheat/barley in the northern plains."
    },
    {
        "type": "Match the Following",
        "q": "Match the animals with their specific archaeological significance:",
        "items": [{"left": "I. Unicorn", "key": "A"}, {"left": "II. Horse", "key": "B"}, {"left": "III. Humped Bull", "key": "C"}],
        "options": [{"val": "A", "text": "A. Mythological, most common motif on seals"}, {"val": "B", "text": "B. Debated bones at Surkotada, absent on seals"}, {"val": "C", "text": "C. Revered domestic draft animal (Zebu)"}],
        "sol": "Unicorn is mythological, horse bones are at Surkotada, and humped bull is the zebu."
    },
    {
        "type": "Match the Following",
        "q": "Match the terminology with their agricultural decryption:",
        "items": [{"left": "I. Sindon", "key": "A"}, {"left": "II. Rabi suite", "key": "B"}, {"left": "III. Kharif/Dry suite", "key": "C"}],
        "options": [{"val": "A", "text": "A. Greek word for cotton, derived from Sindhu"}, {"val": "B", "text": "B. Winter crops like wheat and barley"}, {"val": "C", "text": "C. Summer/dry crops like millets"}],
        "sol": "Sindon is cotton, Rabi winter crops, and Kharif dry crops like millets."
    }
])

s1_mastery_hin.extend([
    {
        "type": "Match the Following",
        "q": "फसलों को उनके पुरातात्विक साक्ष्यों से सुमेलित करें:",
        "items": [{"left": "I. धान की भूसी", "key": "A"}, {"left": "II. बाजरा/मोटा अनाज", "key": "B"}, {"left": "III. गेहूँ/जौ", "key": "C"}],
        "options": [{"val": "A", "text": "A. लोथल और रंगपुर (गुजरात)"}, {"val": "B", "text": "B. सौराष्ट्र की शुष्क बस्तियाँ"}, {"val": "C", "text": "C. उत्तरी मैदानों की मुख्य फसलें"}],
        "sol": "धान की भूसी लोथल/रंगपुर में, बाजरा सौराष्ट्र में और गेहूँ/जौ उत्तर में मिलते थे।"
    },
    {
        "type": "Match the Following",
        "q": "जानवरों को उनके पुरातात्विक महत्व से सुमेलित करें:",
        "items": [{"left": "I. एक सींग वाला पशु (Unicorn)", "key": "A"}, {"left": "II. घोड़ा", "key": "B"}, {"left": "III. कूबड़ वाला बैल", "key": "C"}],
        "options": [{"val": "A", "text": "A. काल्पनिक, मुहरों पर सबसे आम रूपांकन"}, {"val": "B", "text": "B. सुरकोटदा से विवादास्पद हड्डियाँ, मुहरों पर अनुपस्थित"}, {"val": "C", "text": "C. पूजनीय पालतू भारवाहक पशु (जेबू)"}],
        "sol": "एक सींग वाला काल्पनिक है, घोड़े की हड्डियाँ सुरकोटदा में मिलीं, और कूबड़ वाला बैल जेबू है।"
    },
    {
        "type": "Match the Following",
        "q": "शब्दावली को उनके कृषि अर्थों से सुमेलित करें:",
        "items": [{"left": "I. सिंडन (Sindon)", "key": "A"}, {"left": "II. रबी फसलें", "key": "B"}, {"left": "III. खरीफ/शुष्क फसलें", "key": "C"}],
        "options": [{"val": "A", "text": "A. कपास के लिए यूनानी शब्द, सिंधु से व्युत्पन्न"}, {"val": "B", "text": "B. गेहूँ और जौ जैसी शीतकालीन फसलें"}, {"val": "C", "text": "C. बाजरा जैसी शुष्क/ग्रीष्मकालीन फसलें"}],
        "sol": "सिंडन कपास है, रबी शीतकालीन फसलें हैं, और खरीफ शुष्क फसलें हैं।"
    }
])

# One-Liner (8)
for q, sol in [
    ("What was the Greek name for cotton derived from the Indus river?", "Sindon."),
    ("Which site yielded controversial skeletal remains of horses?", "Surkotada."),
    ("Name one dry-crop millet grown in Saurashtra.", "Ragi (or Bajra / Jowar)."),
    ("What is the most frequently depicted animal on Harappan seals?", "The unicorn."),
    ("Which two sites in Gujarat provided evidence of rice husks?", "Lothal and Rangpur."),
    ("What was the primary winter staple crop of the northern plains?", "Wheat (or Barley)."),
    ("Did the Harappans cultivate tea, coffee, or sugarcane?", "No."),
    ("Which draft animal was primarily used to pull heavy ploughs?", "Oxen (bulls).")
]:
    s1_mastery_eng.append({"type": "One-Liner", "q": q, "sol": sol})

for q, sol in [
    ("सिंधु नदी से व्युत्पन्न कपास का यूनानी नाम क्या था?", "सिंडन (Sindon)।"),
    ("किस स्थल से घोड़े के विवादास्पद अस्थि अवशेष प्राप्त हुए हैं?", "सुरकोटदा।"),
    ("सौराष्ट्र में उगाए जाने वाले एक मोटे अनाज (बाजरे) का नाम बताएं।", "रागी (या ज्वार / बाजरा)।"),
    ("हड़प्पा की मुहरों पर सबसे अधिक चित्रित किया जाने वाला पशु कौन सा है?", "एक सींग वाला गेंडा (Unicorn)।"),
    ("गुजरात के किन दो स्थलों से धान की भूसी के साक्ष्य मिले हैं?", "लोथल और रंगपुर।"),
    ("उत्तरी मैदानों की प्राथमिक शीतकालीन खाद्य फसल क्या थी?", "गेहूँ (या जौ)।"),
    ("क्या हड़प्पा वासी चाय, कॉफी या गन्ने की खेती करते थे?", "नहीं।"),
    ("भारी हलों को खींचने के लिए मुख्य रूप से किस पालतू पशु का उपयोग किया जाता था?", "बैल।")
]:
    s1_mastery_hin.append({"type": "One-Liner", "q": q, "sol": sol})

# Assertion-Reason (8)
for q, ans, sol in [
    ("Assertion (A): Cotton was exported to the West under the name 'Sindon'.\nReason (R): The Harappans were the first in the world to cultivate cotton.", 0, "Both A and R are true and R explains why cotton was named Sindon after the Indus valley."),
    ("Assertion (A): The horse was the central animal in Harappan economy and farming.\nReason (R): The horse is completely absent from seals and is not depicted in terracotta art.", 3, "A is false since the horse was not central or widely used; R is true."),
    ("Assertion (A): Rice was a rare and localized luxury crop in the Indus Civilisation.\nReason (R): Evidence of rice is absent in Sindh/Punjab and restricted to husks at Lothal and Rangpur.", 0, "Both A and R are true and the lack of rice in the north shows it was a localized Gujarat crop."),
    ("Assertion (A): Humped cattle (zebu) were highly revered and frequently depicted.\nReason (R): The humped bull is carved with great detail and artistic realism on administrative seals.", 0, "Both A and R are true and the realistic carvings highlight the reverence for humped cattle."),
    ("Assertion (A): Sugarcane was the most important cash crop grown in Sindh.\nReason (R): The main staple crops were wheat and barley, while sugarcane was completely unknown.", 3, "A is false because sugarcane was unknown; R is true."),
    ("Assertion (A): Millets were cultivated in the Saurashtra region of Gujarat.\nReason (R): Millets are drought-resistant crops well-suited to the semi-arid climate of Gujarat.", 0, "Both A and R are true and millets represent an adaptation to Saurashtra's dry climate."),
    ("Assertion (A): Domesticated pigs were kept by Harappan communities.\nReason (R): Pig bones showing cut marks are frequently found in urban kitchen refuse.", 0, "Both A and R are true and cut marks on bones prove they were slaughtered for meat consumption."),
    ("Assertion (A): Camels were the main draft animals in the wet delta of Bengal.\nReason (R): Camel bones are reported at Kalibangan, indicating their use in the arid tracts of Rajasthan.", 3, "A is false as Bengal was not part of the Harappan area and camels are dry-land animals; R is true.")
]:
    s1_mastery_eng.append({"type": "Assertion-Reason", "q": q, "opts": ar_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("कथन (A): कपास को पश्चिम में 'सिंडन' नाम से निर्यात किया जाता था।\nकारण (R): हड़प्पा वासी विश्व में कपास की खेती करने वाले सबसे पहले लोग थे।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या करता है क्योंकि सिंधु (Sindhu) क्षेत्र के नाम पर इसे सिंडन कहा गया।"),
    ("कथन (A): हड़प्पा की अर्थव्यवस्था और कृषि में घोड़ा सबसे केंद्रीय पशु था।\nकारण (R): मुहरों पर घोड़ा पूरी तरह से अनुपस्थित है और मृण्मूर्तियों में इसका अंकन नहीं मिलता है।", 3, "A गलत है क्योंकि घोड़ा केंद्रीय या सामान्य पशु नहीं था; R सही है।"),
    ("कथन (A): सिंधु सभ्यता में चावल एक दुर्लभ और स्थानीय स्तर पर उगाई जाने वाली फसल थी।\nकारण (R): सिंध/पंजाब में चावल के साक्ष्य अनुपस्थित हैं और ये केवल लोथल और रंगपुर में भूसी के रूप में मिले हैं।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या करता है।"),
    ("कथन (A): कूबड़ वाले बैल (zebu) का अत्यधिक महत्व था और मुहरों पर इसका बार-बार अंकन मिलता है।\nकारण (R): प्रशासनिक मुहरों पर कूबड़ वाले बैल को अत्यधिक कलात्मक और यथार्थवादी रूप से उकेरा गया है।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या है।"),
    ("कथन (A): गन्ना सिंध में उगाई जाने वाली सबसे महत्वपूर्ण नकदी फसल थी।\nकारण (R): मुख्य खाद्य फसलें गेहूँ और जौ थीं, जबकि गन्ना पूरी तरह से अज्ञात था।", 3, "A गलत है क्योंकि गन्ना अज्ञात था, और R सही है।"),
    ("कथन (A): गुजरात के सौराष्ट्र क्षेत्र में बाजरे (मोटे अनाजों) की खेती की जाती थी।\nकारण (R): बाजरा सूखा-प्रतिरोधी फसलें हैं जो गुजरात की अर्ध-शुष्क जलवायु के लिए उपयुक्त हैं।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या करता है।"),
    ("कथन (A): हड़प्पा समुदायों द्वारा सूअर पाले जाते थे।\nकारण (R): शहरी रसोई के कचरे में अक्सर सूअर की हड्डियाँ मिलती हैं जिन पर कटने के निशान हैं।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या करता है।"),
    ("कथन (A): बंगाल के आर्द्र डेल्टा क्षेत्र में ऊँट मुख्य भारवाहक पशु थे।\nकारण (R): कालीबंगन से ऊँट की हड्डियाँ मिली हैं, जो राजस्थान के शुष्क क्षेत्रों में इनके उपयोग को दर्शाती हैं।", 3, "A गलत है क्योंकि बंगाल हड़प्पा क्षेत्र में नहीं था; R सही है।")
]:
    s1_mastery_hin.append({"type": "Assertion-Reason", "q": q, "opts": hin_ar_opts, "ans": ans, "sol": sol})

# Statement-Based (5)
for q, ans, sol in [
    ("Consider the following statements:\nStatement 1: The Harappans cultivated sugarcane as a sweetening crop.\nStatement 2: The Harappans were pioneers in cotton cultivation.\nWhich of the statements given above is/are correct?", 1, "Statement 1 is incorrect: sugarcane was unknown. Statement 2 is correct."),
    ("Consider the following statements:\nStatement 1: Skeletal remains of a horse were excavated at Surkotada in Gujarat.\nStatement 2: The horse is depicted on several Mature Harappan seals alongside the bull.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: the horse is completely absent from seal art."),
    ("Consider the following statements:\nStatement 1: Rice husks were found mixed with pottery clay at Lothal.\nStatement 2: Rice husks were also found at the Saurashtra site of Rangpur.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct. Both sites yielded rice remains in Saurashtra."),
    ("Consider the following statements:\nStatement 1: The humped zebu cattle was domesticated and used for pulling agricultural ploughs.\nStatement 2: The mythical one-horned unicorn was the primary beast of burden in the fields.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: the unicorn is a mythical creature, not a real draft animal."),
    ("Consider the following statements:\nStatement 1: Wheat was cultivated as a winter crop in the alluvial plains.\nStatement 2: Barley was cultivated as a summer crop in the dry regions of Baluchistan.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: barley, like wheat, was part of the Rabi (winter) crop suite.")
]:
    s1_mastery_eng.append({"type": "Statement-Based", "q": q, "opts": mcq_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: हड़प्पा वासी मीठे के स्रोत के रूप में गन्ने की खेती करते थे।\nकथन 2: हड़प्पा वासी कपास की खेती करने वाले दुनिया के पहले लोग थे।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 1, "कथन 1 गलत है क्योंकि गन्ना अज्ञात था। कथन 2 सही है।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: गुजरात के सुरकोटदा से घोड़े के अस्थि अवशेष मिले हैं।\nकथन 2: बैल के साथ घोड़े का भी कई परिपक्व हड़प्पा मुहरों पर चित्रण मिलता है।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि मुहरों पर घोड़ा कभी नहीं दर्शाया गया।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: लोथल में मिट्टी के बर्तनों के गारे में धान की भूसी मिली है।\nकथन 2: सौराष्ट्र के रंगपुर स्थल से भी धान की भूसी खोजी गई है।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 2, "दोनों कथन सही हैं। गुजरात के इन दोनों स्थलों से चावल के प्रमाण मिले हैं।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: कूबड़ वाले बैल (जेबू) को पालतू बनाया गया था और खेत में हल खींचने के लिए उपयोग किया जाता था।\nकथन 2: काल्पनिक एक सींग वाला पशु खेतों में मुख्य भार ढोने का काम करता था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि एक सींग वाला गेंडा काल्पनिक था, वास्तविक काम करने वाला पशु नहीं।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: जलोढ़ मैदानों में गेहूँ की खेती शीतकालीन फसल के रूप में की जाती थी।\nकथन 2: बलूचिस्तान के शुष्क क्षेत्रों में जौ की खेती ग्रीष्मकालीन फसल के रूप में की जाती थी।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि जौ भी गेहूँ की तरह रबी (शीतकालीन) फसल थी।")
]:
    s1_mastery_hin.append({"type": "Statement-Based", "q": q, "opts": hin_mcq_opts, "ans": ans, "sol": sol})

# Why (3)
for q, sol in [
    ("Why did the ancient Greeks use the term 'Sindon' to describe cotton textile products?", "The word 'Sindon' is etymologically derived from 'Sindhu', the Sanskrit name for the Indus River. Since the Indus Valley Civilisation was the pioneer and main exporter of cotton textiles to the West, the Greeks named the fabric after the river valley of its origin."),
    ("Why is the presence and role of the horse in Harappan society highly debated among historians?", "While horse bones are reported at Surkotada, the horse is completely absent from the hundreds of seals and terracotta figurines. This mismatch suggests that even if horses existed, they were not integrated into the economic or religious life of Harappan cities, unlike in the later Vedic period."),
    ("Why did the Harappans in Gujarat focus heavily on millet cultivation (ragi, jowar) rather than wheat?", "Gujarat has a semi-arid, dry climate with lower rainfall and lacks the massive perennial river floods of the Indus. Millets are highly drought-resistant and require less water, making them the ideal crop adaptation for Saurashtra's soils.")
]:
    s1_mastery_eng.append({"type": "Why", "q": q, "sol": sol})

for q, sol in [
    ("प्राचीन यूनानियों ने सूती कपड़ों का वर्णन करने के लिए 'सिंडन' (Sindon) शब्द का उपयोग क्यों किया?", "यूनानी शब्द 'सिंडन' वास्तव में 'सिंधु' (Sindhu/Indus) शब्द का अपभ्रंश है। चूंकि सिंधु सभ्यता कपास उगाने और कपड़े निर्यात करने वाली पहली सभ्यता थी, इसलिए यूनानियों ने इसके उत्पत्ति क्षेत्र (सिंधु घाटी) के नाम पर कपड़े का नाम सिंडन रखा।"),
    ("हड़प्पा समाज में घोड़े के अस्तित्व और उसकी भूमिका पर इतिहासकारों के बीच इतना विवाद क्यों है?", "सुरकोटदा से घोड़े की हड्डियां मिलने का दावा तो किया गया है, लेकिन सैकड़ों मुहरों और खिलौनों पर घोड़ा कभी नहीं दिखाया गया। यह विरोधाभास दर्शाता है कि यदि घोड़ा था भी, तो वह शहरी आर्थिक या धार्मिक जीवन का हिस्सा नहीं था, जैसा कि बाद के वैदिक काल में था।"),
    ("गुजरात के हड़प्पा वासियों ने गेहूँ के बजाय मोटे अनाज (रागी, ज्वार, बाजरा) की खेती पर अधिक ध्यान क्यों दिया?", "गुजरात की जलवायु अर्ध-शुष्क और कम वर्षा वाली है, और वहां सिंधु नदी जैसी बारहमासी बाढ़ नहीं आती। बाजरा सूखा-रोधी फसलें हैं जिन्हें बहुत कम पानी की आवश्यकता होती है, जो सौराष्ट्र की मिट्टी के अनुकूल थी।")
]:
    s1_mastery_hin.append({"type": "Why", "q": q, "sol": sol})

# How (3)
for q, sol in [
    ("How do zooarchaeologists determine that animal bones found at Harappan sites represent human diet?", "They analyze faunal assemblages for diagnostic taphonomic markers. The presence of sharp cut marks on bones (indicating butchery), charring or burning (indicating cooking), and the concentration of these bones in household refuse dumps show they were consumed for food."),
    ("How was the international trade of cotton textiles managed from fields to foreign markets?", "Raw cotton was spun and woven locally. The finished textiles were folded, wrapped in bundles, secured with ropes, and covered with wet clay tags stamped with merchant seals (sealings) to prevent tampering before shipping to Mesopotamian ports."),
    ("How did humped cattle (zebu) assist the Harappan agrarian economy?", "Oxen served as the primary draft animals. They pulled heavy wooden ploughs to till the dense alluvial soils and were harnessed to solid-wheeled carts to transport bulk grains from farming villages to city granaries.")
]:
    s1_mastery_eng.append({"type": "How", "q": q, "sol": sol})

for q, sol in [
    ("पशु-पुरातत्वविद (zooarchaeologists) यह कैसे निर्धारित करते हैं कि हड़प्पा स्थलों पर मिली जानवरों की हड्डियां मानवीय आहार का हिस्सा थीं?", "वे हड्डियों पर कसाई के काम के निशान (cut marks) और आग में पकने के निशान (charring) का विश्लेषण करते हैं। इन हड्डियों का घरों के कचरे के ढेरों में मिलना यह साबित करता है कि इनका उपयोग भोजन के लिए किया गया था।"),
    ("खेतों से लेकर विदेशी बाजारों तक सूती कपड़ों के अंतर्राष्ट्रीय व्यापार का प्रबंधन कैसे किया जाता था?", "कपास की कताई और बुनाई स्थानीय स्तर पर की जाती थी। बने हुए कपड़ों को मोड़ा जाता था, बंडलों में बांधा जाता था और गांठ पर गीली मिट्टी लगाकर उस पर व्यापारियों की मुहर दबाई जाती थी (sealings), ताकि सुरक्षित निर्यात सुनिश्चित हो सके।"),
    ("कूबड़ वाले बैल (zebu) ने हड़प्पा की कृषि अर्थव्यवस्था को कैसे सहयोग दिया?", "बैल खेतों में मुख्य काम करते थे। वे जलोढ़ मिट्टी जोतने के लिए लकड़ी के भारी हलों को खींचते थे और कटी हुई फसलों को बैलगाड़ियों में भरकर गांवों से शहरों के अन्नागारों तक पहुँचाने का काम करते थे।")
]:
    s1_mastery_hin.append({"type": "How", "q": q, "sol": sol})

# Case Study (3)
for q, sol in [
    ("Case Study: The Surkotada Horse Bone Controversy. Discuss the debate.", "Excavations at Surkotada in 1974 yielded horse teeth and bones identified by AK Sharma as Equus caballus. However, critics like Richard Meadow argue the bones belong to the wild ass (khur) native to Kutch. The complete absence of horses on seals supports the view that the horse was not culturally integrated."),
    ("Case Study: Pioneers of Cotton. Analyze the textile discoveries at Mohenjo-daro.", "Mohenjo-daro yielded fragments of woven cotton cloth dyed with madder, preserved on the lid of a silver vase. This shows that by 3000 BCE, Harappans possessed advanced spinning, weaving, and dyeing technologies, making cotton a major industrial commodity."),
    ("Case Study: Gujarat Millet Adaptation. Discuss the late rural survival.", "As the Mature Harappan cities declined around 1900 BCE, rural sites in Gujarat (like Rojdi) survived and flourished. They adapted by shifting entirely to dry farming of millets (ragi, bajra), which allowed them to survive without river inundation, illustrating agricultural resilience.")
]:
    s1_mastery_eng.append({"type": "Case Study", "q": q, "sol": sol})

for q, sol in [
    ("केस स्टडी: सुरकोटदा में घोड़े की हड्डियों का विवाद। इसके पक्षों पर चर्चा करें।", "1974 में सुरकोटदा की खुदाई में घोड़े के दांत और हड्डियाँ मिली थीं जिन्हें ए.के. शर्मा ने वास्तविक घोड़े (Equus caballus) का बताया था। हालांकि, रिचर्ड मीडो जैसे आलोचकों का मानना है कि ये जंगली गधे (खुर) की हड्डियाँ हैं। मुहरों पर घोड़े का न मिलना इस संशय को बढ़ाता है।"),
    ("केस स्टडी: कपास के अग्रदूत। मोहनजोदड़ो में मिले वस्त्रों के साक्ष्यों का विश्लेषण करें।", "मोहनजोदड़ो में एक चांदी के बर्तन के ढक्कन पर चिपका हुआ सूती कपड़े का टुकड़ा मिला है जो मजीठ (madder) से रंगा हुआ था। यह दर्शाता है कि 3000 ईसा पूर्व तक हड़प्पा वासियों के पास कताई, बुनाई और रंगाई की उन्नत तकनीक थी।"),
    ("केस स्टडी: गुजरात में मोटे अनाज (Millet) का अनुकूलन। ग्रामीण उत्तरजीविता पर चर्चा करें।", "1900 ईसा पूर्व के आसपास जब हड़प्पा के बड़े शहर ढह गए, तब गुजरात के ग्रामीण स्थल (जैसे रोजदी) फलते-फूलते रहे। उन्होंने सिंचाई विफलता से बचने के लिए बाजरे की सूखी खेती को पूरी तरह अपना लिया, जो उनकी कृषि लचीलेपन को दर्शाता है।")
]:
    s1_mastery_hin.append({"type": "Case Study", "q": q, "sol": sol})

# Teach Concept (3)
for q, sol in [
    ("Teach the Concept: Subsistence Strategy vs. Commercial Crop Production.", "Explain to students that Harappan farming had a dual character: (1) subsistence production of staple crops (wheat, barley) to feed local cities, and (2) industrial crop production (cotton) designed specifically for textile manufacturing and long-distance export trade."),
    ("Teach the Concept: Diagnostic Methods for Domestic Faunal Assemblages.", "Teach students how archaeologists identify domesticated animals from bones. Domesticated animals have thinner, less dense bones due to controlled diets and confinement, and their bones show cut marks at joints, unlike wild bones which are thicker and show fractures from hunting."),
    ("Teach the Concept: Double-Cropping and Agrarian Risk Mitigation.", "Explain to students that planting Rabi crops (winter wheat) and Kharif crops (summer millets) allowed the Harappans to hedge against weather failures. If winter rains failed, summer floods or monsoon crops secured the food supply, preventing total famine.")
]:
    s1_mastery_eng.append({"type": "Teach Concept", "q": q, "sol": sol})

for q, sol in [
    ("अवधारणा सिखाएं: निर्वाह कृषि (Subsistence Strategy) बनाम व्यावसायिक फसल उत्पादन।", "छात्रों को समझाएं कि हड़प्पा कृषि का दोहरा स्वरूप था: (1) शहरों का पेट भरने के लिए गेहूं और जौ जैसी बुनियादी फसलों का निर्वाह उत्पादन, और (2) कपड़ा उद्योग और लंबी दूरी के निर्यात व्यापार के लिए कपास जैसी नकदी फसलों का औद्योगिक उत्पादन।"),
    ("अवधारणा सिखाएं: पालतू पशुओं की हड्डियों की पहचान करने के वैज्ञानिक तरीके।", "छात्रों को समझाएं कि पुरातत्वविद पालतू जानवरों की हड्डियों को कैसे पहचानते हैं। पालतू बनाए गए जानवरों की हड्डियां भोजन नियंत्रण और बंधक जीवन के कारण पतली और कम सघन होती हैं, और उनके जोड़ों पर कतरने के निशान मिलते हैं, जबकि जंगली जानवरों की हड्डियां मजबूत होती हैं।"),
    ("अवधारणा सिखाएं: दोहरी फसल प्रणाली और कृषि जोखिम प्रबंधन।", "समझाएं कि शीतकालीन रबी फसलों और ग्रीष्मकालीन खरीफ फसलों को साथ में उगाने से हड़प्पा वासियों को मौसम के जोखिमों से सुरक्षा मिलती थी। यदि शीतकालीन वर्षा विफल होती थी, तो ग्रीष्मकालीन बाढ़ या मानसूनी फसलें भोजन की सुरक्षा सुनिश्चित करती थीं।")
]:
    s1_mastery_hin.append({"type": "Teach Concept", "q": q, "sol": sol})


# =========================================================================
# SECTION 2: AGRICULTURAL TECHNOLOGY AND IRRIGATION
# =========================================================================
s2_mastery_eng = []
s2_mastery_hin = []

# MCQ (5)
for q, opts, ans, sol in [
    ("Direct evidence of a ploughed agricultural field with grid furrows was excavated at which site?", ["Kalibangan", "Banawali", "Lothal", "Surkotada"], 0, "Kalibangan in Rajasthan has yielded a ploughed field from the Early Harappan phase."),
    ("A complete terracotta model of a plough showing the curved share was discovered at which site?", ["Banawali", "Kalibangan", "Mohenjo-daro", "Harappa"], 0, "Banawali in Haryana yielded a famous complete terracotta model of a plough."),
    ("The stone-walled check dams constructed in Baluchistan to block water run-off are called:", ["Gabarbands", "Dockyards", "Sluice-gates", "Aqueducts"], 0, "They are known as Gabarbands, constructed across streams to collect water and fertile silt."),
    ("Canal irrigation traces are rare in the alluvial plains of Sindh primarily because:", ["Heavy flood siltation buried them over time", "The Harappans did not know how to dig canals", "Canals were forbidden by religious elites", "They relied entirely on drip irrigation"], 0, "The heavy silt carried by river floods buried ancient canals in the main plains, making them invisible today."),
    ("Which remote Harappan trading colony on the Oxus River features stone-lined canals for irrigation?", ["Shortughai", "Mundigak", "Sutkagendor", "Altyn-Depe"], 0, "Shortughai in northern Afghanistan features direct, stone-lined irrigation canals.")
]:
    s2_mastery_eng.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("ग्रिड पैटर्न की हल-रेखाओं वाले जुते हुए खेत का प्रत्यक्ष साक्ष्य किस स्थल पर खोजा गया था?", ["कालीबंगन", "बनावली", "लोथल", "सुरकोटदा"], 0, "राजस्थान के कालीबंगन से प्रारंभिक हड़प्पा स्तर का जुता हुआ खेत मिला है।"),
    ("घुमावदार फलक (share) दर्शाने वाले मिट्टी के हल का एक पूरा खिलौना मॉडल किस स्थल से मिला था?", ["बनावली", "कालीबंगन", "मोहनजोदड़ो", "हड़प्पा"], 0, "हरियाणा के बनावली से मिट्टी के हल का प्रसिद्ध मॉडल प्राप्त हुआ था।"),
    ("बलूचिस्तान में पानी के बहाव को रोकने के लिए बनाई गई पत्थरों की दीवारों (बांधों) को क्या कहा जाता है?", ["गबरबंद", "गोदीवाड़ा", "लॉक-गेट", "नहर"], 0, "इन्हें गबरबंद कहा जाता है, जो मौसमी नालों पर पानी और उपजाऊ गाद जमा करने के लिए बनाए जाते थे।"),
    ("सिंध के जलोढ़ मैदानों में नहर सिंचाई के अवशेष दुर्लभ होने का मुख्य कारण क्या है?", ["बाढ़ की गाद ने समय के साथ उन्हें ढक दिया", "हड़प्पा वासी नहर बनाना नहीं जानते थे", "धार्मिक गुरुओं द्वारा नहरों का निर्माण वर्जित था", "वे पूरी तरह से ड्रिप सिंचाई पर निर्भर थे"], 0, "नदियों की बाढ़ से बहने वाली गाद ने मैदानों में नहरों के प्राचीन अवशेषों को गहरे दफन कर दिया।"),
    ("आक्सस नदी के किनारे स्थित किस सुदूर हड़प्पा बस्ती से पत्थर की सिंचाई नहरों के अवशेष मिले हैं?", ["शोर्तुघई", "मुंडीगाक", "सुत्कागेंदोर", "अल्टिन-देपे"], 0, "उत्तरी अफगानिस्तान के शोर्तुघई से सिंचाई के लिए प्रयुक्त नहरों के अवशेष मिले हैं।")
]:
    s2_mastery_hin.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# Multiple Correct MCQ (5)
for q, opts, ans, sol in [
    ("Which of the following irrigation sources were used by the Harappans? (Select all that apply)", ["Brick-lined wells", "Masonry reservoirs at Dholavira", "Gabarbands in Baluchistan", "Diesel water pumps"], [0, 1, 2], "Wells, reservoirs, and Gabarbands were used. Diesel pumps are modern technology."),
    ("What features characterize the ploughed field discovered at Kalibangan? (Select all that apply)", ["It belongs to the Early Harappan phase", "It features two sets of furrows crossing at right angles", "It indicates the practice of double-cropping", "It was ploughed using iron shares"], [0, 1, 2], "The field is Early Harappan, grid-furrowed, and shows double-cropping. Iron was unknown."),
    ("Select the materials and designs used for Harappan harvesting tools: (Select all that apply)", ["Chert blades set in wooden slots", "Natural bitumen used as adhesive glue", "Iron sickles with wooden handles", "Bronze sickles in common use"], [0, 1], "Harvesting sickles were made of chert blades hafted with bitumen in wood. Iron was unknown, and bronze sickles were rare."),
    ("At which of the following regions or sites have terracotta models of ploughshares been excavated? (Select all that apply)", ["Banawali in Haryana", "Cholistan in Pakistan", "Lothal in Gujarat", "Shortughai in Afghanistan"], [0, 1], "Plough models came from Banawali and Cholistan. Lothal and Shortughai did not yield plough models."),
    ("Identify the elements of Dholavira's advanced rainwater harvesting system: (Select all that apply)", ["Massive stone-cut reservoirs", "Check dams across seasonal streams (Manhar/Mandsar)", "Feeder channels linking dams to basins", "Lead-lined copper pipes"], [0, 1, 2], "Dholavira used stone reservoirs, dams, and feeder channels. Lead-lined copper pipes are inaccurate.")
]:
    s2_mastery_eng.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("हड़प्पा वासियों द्वारा सिंचाई के किन स्रोतों का उपयोग किया जाता था? (सभी लागू विकल्प चुनें)", ["ईंटों से बने कुएं", "धोलावीरा के पत्थर-कट जलाशय", "बलूचिस्तान में गबरबंद", "डीजल पंप"], [0, 1, 2], "कुएं, जलाशय और गबरबंद प्राचीन सिंचाई माध्यम थे। डीजल पंप आधुनिक उपकरण हैं।"),
    ("कालीबंगन में खोजे गए जुते हुए खेत की क्या विशेषताएं हैं? (सभी लागू विकल्प चुनें)", ["यह प्रारंभिक हड़प्पा काल का है", "इसमें समकोण पर काटती हल की रेखाएं हैं", "यह दोहरी फसल प्रणाली का संकेत देता है", "इसे लोहे के हलों से जोता गया था"], [0, 1, 2], "खेत प्रारंभिक हड़प्पा काल का है, ग्रिड पैटर्न दिखाता है और दोहरी फसल का साक्ष्य है। लोहे का ज्ञान नहीं था।"),
    ("हड़प्पा कालीन कटाई उपकरणों के निर्माण और डिजाइन का चयन करें: (सभी लागू विकल्प चुनें)", ["लकड़ी के खांचे में लगे चर्ट के फलक", "चिपकाने के लिए प्राकृतिक राल/बिटुमेन का उपयोग", "लोहे के हँसिए", "कांस्य के हँसिए"], [0, 1], "हँसिए लकड़ी के खांचे में फिट चर्ट ब्लेड और राल से बनते थे। लोहे का ज्ञान नहीं था, कांस्य हँसिए दुर्लभ थे।"),
    ("निम्नलिखित में से किन क्षेत्रों या स्थलों से मिट्टी के हलों के मॉडल खोजे गए हैं? (सभी लागू विकल्प चुनें)", ["हरियाणा में बनावली", "पाकिस्तान में चोलिस्तान", "गुजरात में लोथल", "अफगानिस्तान में शोर्तुघई"], [0, 1], "बनावली और चोलिस्तान से हलों के मॉडल मिले हैं। लोथल या शोर्तुघई से नहीं मिले हैं।"),
    ("धोलावीरा की उन्नत वर्षा जल संचयन प्रणाली के तत्वों की पहचान करें: (सभी लागू विकल्प चुनें)", ["विशाल पत्थर-कट जलाशय", "मनहर और मंदसर नदियों पर बने बांध", "बांधों को जलाशयों से जोड़ने वाली नहरें", "तांबे के पाइप"], [0, 1, 2], "धोलावीरा में पत्थर के जलाशय, बांध और जोड़ने वाली नहरें थीं। तांबे के पाइप अनुपस्थित थे।")
]:
    s2_mastery_hin.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# True/False (8)
for q, ans, sol in [
    ("Iron ploughshares were widely used to till the hard soil of Rakhigarhi.", False, "False. Iron was unknown; Harappans used wooden ploughshares."),
    ("The remote outpost of Shortughai has yielded clear ruins of stone-lined canals.", True, "True. Shortughai's canals redirected Oxus waters to nearby fields."),
    ("The ploughed field at Kalibangan belongs to the Late Harappan period.", False, "False. The field belongs to the Pre-Mature/Early Harappan level."),
    ("Gabarbands are stone check dams built by Harappans in the hilly regions of Baluchistan.", True, "True. They helped store seasonal stream water and trap fertile silt."),
    ("Harvesting blades used by Harappans were primarily made of chert stones.", True, "True. Fine chert blades set in wooden handles served as crop-cutting sickles."),
    ("Wells were utilized for gardening and small-plot cultivation in major cities.", True, "True. Brick-lined wells supplied water to plots inside Mohenjo-daro."),
    ("Every Harappan farming field was irrigated by a network of canals.", False, "False. Canals were rare; most plains farming relied on annual floods and wells."),
    ("Dholavira's water reservoirs were carved directly out of the local bedrock.", True, "True. Dholavira's reservoirs are magnificent stone-cut basins lining the citadel.")
]:
    s2_mastery_eng.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("राखीगढ़ी की कठोर मिट्टी को जोतने के लिए लोहे के हलों का व्यापक उपयोग किया जाता था।", False, "असत्य। लोहे का ज्ञान नहीं था; लकड़ी के हलों का उपयोग किया जाता था।"),
    ("सुदूर चौकी शोर्तुघई से पत्थर की नहरों के स्पष्ट अवशेष मिले हैं।", True, "सत्य। शोर्तुघई की नहरें आक्सस नदी के पानी को खेतों की ओर मोड़ती थीं।"),
    ("कालीबंगन का जुता हुआ खेत उत्तर-हड़प्पा काल का है।", False, "असत्य। यह खेत प्रारंभिक हड़प्पा स्तर से संबंधित है।"),
    ("गबरबंद बलूचिस्तान के पहाड़ी इलाकों में हड़प्पा वासियों द्वारा बनाए गए पत्थर के बांध हैं।", True, "सत्य। ये बांध मौसमी पानी को रोकते थे और उपजाऊ गाद जमा करते थे।"),
    ("हड़प्पा वासियों द्वारा प्रयुक्त कटाई के फलक मुख्य रूप से चर्ट (पत्थर) से बने थे।", True, "सत्य। बारीक चर्ट पत्थरों को लकड़ी के हत्थों में लगाकर हँसिए बनाए जाते थे।"),
    ("बड़े शहरों में कुओं का उपयोग बागवानी और छोटी कृषि भूमियों की सिंचाई के लिए होता था।", True, "सत्य। मोहनजोदड़ो के कुएं खेतों और बगीचों में पानी देने के काम आते थे।"),
    ("हड़प्पा के प्रत्येक कृषि क्षेत्र की सिंचाई नहरों के जाल द्वारा की जाती थी।", False, "असत्य। नहरें दुर्लभ थीं; मैदानी खेती मुख्य रूप से बाढ़ के पानी और कुओं पर निर्भर थी।"),
    ("धोलावीरा के जल जलाशय वहाँ की स्थानीय चट्टानों को काटकर बनाए गए थे।", True, "सत्य। धोलावीरा के जलाशय चट्टानों को काटकर बनाए गए थे जो किले के किनारे स्थित थे।")
]:
    s2_mastery_hin.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

# Fill Blanks (8)
for q, ans, sol in [
    ("The ploughed field excavated at Kalibangan belongs to the ________ Harappan phase.", "Early", "The field belongs to the Early/Pre-Mature phase of Kalibangan."),
    ("Terracotta plough models were recovered at Banawali and ________.", "Cholistan", "Cholistan (Jawariwala) has also yielded terracotta ploughs."),
    ("Stone check dams built to collect water and silt in Baluchistan are called ________.", "Gabarbands", "They are known as Gabarbands in Baluchistan."),
    ("Magnificent stone-cut reservoirs to store rainwater are found at ________.", "Dholavira", "Dholavira is famous for stone-cut reservoirs."),
    ("The primary material used to make sickle blades for harvesting was ________.", "chert", "Banded chert blades were used for sickles."),
    ("Canal ruins have been excavated in northern Afghanistan at the site of ________.", "Shortughai", "Shortughai has canal ruins on the Oxus River."),
    ("High siltation from river floods buried canals in the ________ plains.", "alluvial", "The alluvial plains of the Indus lack canal remains due to heavy silting."),
    ("Brick-lined ________ dug inside Mohenjo-daro were used for domestic irrigation.", "wells", "Wells supplied water for garden plots inside Mohenjo-daro.")
]:
    s2_mastery_eng.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("कालीबंगन में खोजा गया जुता हुआ खेत ________ हड़प्पा काल का है।", "प्रारंभिक", "कालीबंगन का जुता हुआ खेत प्रारंभिक/पूर्व-परिपक्व स्तर का है।"),
    ("मिट्टी के हल के मॉडल बनावली और ________ से प्राप्त हुए हैं।", "चोलिस्तान", "चोलिस्तान (जवारीवाला) से भी हल के मॉडल मिले हैं।"),
    ("बलूचिस्तान में पानी और गाद रोकने के लिए पत्थरों के बांधों को ________ कहा जाता है।", "गबरबंद", "बलूचिस्तान में इन्हें गबरबंद (Gabarbands) कहा जाता है।"),
    ("वर्षा जल संचयन के लिए चट्टानों को काटकर बनाए गए शानदार जलाशय ________ में मिले हैं।", "धोलावीरा", "धोलावीरा अपने प्रस्तर जलाशयों के लिए प्रसिद्ध है।"),
    ("फसल कटाई के लिए हँसिए के फलक बनाने के लिए प्रयुक्त मुख्य पदार्थ ________ था।", "चर्ट", "चर्ट (chert) पत्थर के फलक हँसिए में लगाए जाते थे।"),
    ("उत्तरी अफगानिस्तान में ________ नामक स्थल से नहरों के अवशेष मिले हैं।", "शोर्तुघई", "शोर्तुघई में आक्सस नदी के पानी को मोड़ने वाली नहरें मिली हैं।"),
    ("नदियों की बाढ़ से आने वाली गाद ने ________ मैदानों में नहरों के अवशेषों को ढक दिया।", "जलोढ़", "जलोढ़ मैदानों में बाढ़ के साथ आने वाली मिट्टी ने नहरों को दफन कर दिया।"),
    ("मोहनजोदड़ो के भीतर खोदे गए ईंटों के ________ सिंचाई और घरेलू उपयोग में आते थे।", "कुएं", "कुओं का उपयोग घरेलू बाड़ी और खेतों में पानी देने के लिए भी होता था।")
]:
    s2_mastery_hin.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

# Matchings (3)
s2_mastery_eng.extend([
    {
        "type": "Match the Following",
        "q": "Match the farming technologies with their primary discovery sites:",
        "items": [{"left": "I. Ploughed Field", "key": "A"}, {"left": "II. Terracotta Plough", "key": "B"}, {"left": "III. Stone Reservoirs", "key": "C"}],
        "options": [{"val": "A", "text": "A. Kalibangan (Rajasthan)"}, {"val": "B", "text": "B. Banawali (Haryana)"}, {"val": "C", "text": "C. Dholavira (Gujarat)"}],
        "sol": "Ploughed field is at Kalibangan, plough model at Banawali, and reservoirs at Dholavira."
    },
    {
        "type": "Match the Following",
        "q": "Match the water systems with their geographic settings:",
        "items": [{"left": "I. Gabarband check-dams", "key": "A"}, {"left": "II. Irrigation canals", "key": "B"}, {"left": "III. Standardized wells", "key": "C"}],
        "options": [{"val": "A", "text": "A. Baluchistan hilly valleys"}, {"val": "B", "text": "B. Shortughai (Afghanistan)"}, {"val": "C", "text": "C. Mohenjo-daro urban sectors"}],
        "sol": "Gabarbands are in Baluchistan hills, canals in Shortughai, and wells in Mohenjo-daro."
    },
    {
        "type": "Match the Following",
        "q": "Match the agricultural materials with their tools:",
        "items": [{"left": "I. Chert", "key": "A"}, {"left": "II. Wood", "key": "B"}, {"left": "III. Bitumen", "key": "C"}],
        "options": [{"val": "A", "text": "A. Sickle cutting blades"}, {"val": "B", "text": "B. Ploughshare and shaft"}, {"val": "C", "text": "C. Hafting adhesive glue"}],
        "sol": "Chert was for sickle blades, wood for ploughs, and bitumen acted as the hafting adhesive."
    }
])

s2_mastery_hin.extend([
    {
        "type": "Match the Following",
        "q": "कृषि तकनीकों को उनके मुख्य खोज स्थलों से सुमेलित करें:",
        "items": [{"left": "I. जुता हुआ खेत", "key": "A"}, {"left": "II. मिट्टी के हल का मॉडल", "key": "B"}, {"left": "III. पत्थर के जलाशय", "key": "C"}],
        "options": [{"val": "A", "text": "A. कालीबंगन (राजस्थान)"}, {"val": "B", "text": "B. बनावली (हरियाणा)"}, {"val": "C", "text": "C. धोलावीरा (गुजरात)"}],
        "sol": "जुता खेत कालीबंगन में, हल मॉडल बनावली में और जलाशय धोलावीरा में मिले।"
    },
    {
        "type": "Match the Following",
        "q": "जल प्रणालियों को उनके भौगोलिक संदर्भों से सुमेलित करें:",
        "items": [{"left": "I. गबरबंद (Gabarband)", "key": "A"}, {"left": "II. सिंचाई नहरें", "key": "B"}, {"left": "III. मानकीकृत कुएं", "key": "C"}],
        "options": [{"val": "A", "text": "A. बलूचिस्तान की पर्वतीय घाटियाँ"}, {"val": "B", "text": "B. शोर्तुघई (अफगानिस्तान)"}, {"val": "C", "text": "C. मोहनजोदड़ो के शहरी क्षेत्र"}],
        "sol": "गबरबंद बलूचिस्तान में, नहरें शोर्तुघई में और कुएं मोहनजोदड़ो में थे।"
    },
    {
        "type": "Match the Following",
        "q": "कृषि सामग्रियों को उनके संबंधित उपकरणों से सुमेलित करें:",
        "items": [{"left": "I. चर्ट (Chert)", "key": "A"}, {"left": "II. लकड़ी", "key": "B"}, {"left": "III. बिटुमेन (कोलतार)", "key": "C"}],
        "options": [{"val": "A", "text": "A. हँसिए (sickle) के फलक"}, {"val": "B", "text": "B. हल का फलक और शाफ्ट"}, {"val": "C", "text": "C. चिपकाने वाला गोंद/राल"}],
        "sol": "चर्ट से हँसिए के फलक, लकड़ी से हल और बिटुमेन से उन्हें जोड़ा जाता था।"
    }
])

# One-Liner (8)
for q, sol in [
    ("Where was the direct evidence of a ploughed field found?", "Kalibangan."),
    ("Name the hilly stone check dams used in Baluchistan.", "Gabarbands."),
    ("Which site yielded a terracotta model of a plough in Haryana?", "Banawali."),
    ("Which stone was primarily used to make harvesting blades?", "Chert."),
    ("Where are the massive stone rainwater reservoirs located?", "Dholavira."),
    ("Which river valley is Shortughai located in?", "Oxus River valley (Amu Darya)."),
    ("Did the Harappans use iron tools for tilling?", "No."),
    ("Why did Indus floods prevent canal visibility today?", "Heavy silt deposits buried them.")
]:
    s2_mastery_eng.append({"type": "One-Liner", "q": q, "sol": sol})

for q, sol in [
    ("जुते हुए खेत का प्रत्यक्ष पुरातात्विक साक्ष्य कहाँ मिला था?", "कालीबंगन।"),
    ("बलूचिस्तान में प्रयुक्त होने वाले पत्थर के बांधों को क्या कहा जाता है?", "गबरबंद।"),
    ("हरियाणा के किस स्थल से मिट्टी के हल का मॉडल मिला है?", "बनावली।"),
    ("कटाई के फलक बनाने के लिए किस पत्थर का मुख्य रूप से उपयोग किया जाता था?", "चर्ट।"),
    ("चट्टानों को काटकर बनाए गए विशाल जलाशय कहाँ स्थित हैं?", "धोलावीरा।"),
    ("शोर्तुघई किस नदी घाटी में स्थित है?", "आक्सस नदी घाटी (अमु दरिया)।"),
    ("क्या हड़प्पा वासी जोतने के लिए लोहे के उपकरणों का उपयोग करते थे?", "नहीं।"),
    ("सिंधु की बाढ़ ने नहरों को आज अदृश्य क्यों बना दिया?", "भारी गाद (silt) के जमाव ने उन्हें पाट दिया।")
]:
    s2_mastery_hin.append({"type": "One-Liner", "q": q, "sol": sol})

# Assertion-Reason (8)
for q, ans, sol in [
    ("Assertion (A): Terracotta plough models help reconstruct Harappan tillage practices.\nReason (R): Being made of organic wood, actual Harappan ploughs have rotted away and left no physical traces.", 0, "Both A and R are true and R explains why terracotta replicas are crucial to prove wood plough use."),
    ("Assertion (A): Canals are absent from the main alluvial plains of Sindh and Punjab.\nReason (R): The high-silt annual floods of the Indus buried ancient shallow channels under thick layers of mud.", 0, "Both A and R are true and heavy flood siltation is the reason plains canals are invisible today."),
    ("Assertion (A): Dholavira constructed large reservoirs inside its stone-wall fortifications.\nReason (R): Located in dry Kutch, Dholavira received low rainfall and required rainwater storage to secure survival.", 0, "Both A and R are true and geographic dry conditions made rainwater harvesting vital."),
    ("Assertion (A): Iron tools were widely used to cut forest timber for farming space.\nReason (R): The Harappans lived in the Bronze Age and had no knowledge of iron metallurgy.", 3, "A is false because iron was unknown; R is true."),
    ("Assertion (A): The Kalibangan ploughed field shows that they practiced double-cropping.\nReason (R): The grid pattern of furrows shows lines running at right angles to each other, allowing two crop rows.", 0, "Both A and R are true and the perpendicular grid allowed two crops to grow together."),
    ("Assertion (A): Canals were dug at the trading outpost of Shortughai in Afghanistan.\nReason (R): Shortughai lies in a semi-arid zone where agriculture was impossible without diverting river water.", 0, "Both A and R are true and dry local conditions necessitated canal irrigation at Shortughai."),
    ("Assertion (A): Wells were used only to wash clothes in cities.\nReason (R): Brick-lined wells provided water for drinking, household needs, and small-plot garden farming.", 3, "A is false since wells had agrarian uses; R is true."),
    ("Assertion (A): Gabarbands were stone check dams constructed in the delta of Bengal.\nReason (R): They are located in the arid, hilly valleys of Baluchistan to check rainwater run-off.", 3, "A is false since they are in Baluchistan, not Bengal; R is true.")
]:
    s2_mastery_eng.append({"type": "Assertion-Reason", "q": q, "opts": ar_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("कथन (A): मिट्टी के हल के मॉडल हड़प्पा की जुताई पद्धतियों को समझने में मदद करते हैं।\nकारण (R): लकड़ी से बने होने के कारण वास्तविक हड़प्पा हल सड़ गए हैं और उनके भौतिक अवशेष नहीं बचे हैं।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या करता है क्योंकि लकड़ी के सड़ने से खिलौने ही मुख्य साक्ष्य बचे।"),
    ("कथन (A): सिंध और पंजाब के जलोढ़ मैदानों में नहरों के अवशेष दिखाई नहीं देते हैं।\nकारण (R): सिंधु नदी की गाद से भरी वार्षिक बाढ़ ने प्राचीन उथली नहरों को मिट्टी की मोटी परतों के नीचे दबा दिया।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या करता है क्योंकि बाढ़ की सिल्ट ही नहरों के लुप्त होने का कारण है।"),
    ("कथन (A): धोलावीरा ने अपनी मजबूत पत्थरों की दीवारों के भीतर विशाल जलाशयों का निर्माण किया था।\nकारण (R): शुष्क कच्छ में स्थित होने के कारण धोलावीरा में वर्षा कम होती थी, जिससे अस्तित्व के लिए जल भंडारण आवश्यक था।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या है।"),
    ("कथन (A): कृषि योग्य भूमि साफ करने के लिए लोहे के उपकरणों का व्यापक उपयोग किया जाता था।\nकारण (R): हड़प्पा वासी कांस्य युग में रहते थे और उन्हें लोहे के धातु विज्ञान का कोई ज्ञान नहीं था।", 3, "A गलत है क्योंकि लोहे का ज्ञान नहीं था; R सही है।"),
    ("कथन (A): कालीबंगन के जुते हुए खेत से पता चलता है कि वे दोहरी फसल प्रणाली अपनाते थे।\nकारण (R): खेत में हल की रेखाएं एक-दूसरे को समकोण पर काटती हैं, जिससे दो फसलें साथ उगाई जा सकती थीं।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या है।"),
    ("कथन (A): अफगानिस्तान में शोर्तुघई व्यापारिक चौकी पर नहरें खोदी गई थीं।\nकारण (R): शोर्तुघई एक अर्ध-शुष्क क्षेत्र में स्थित है जहाँ आक्सस नदी के जल के बिना खेती असंभव थी।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या करता है।"),
    ("कथन (A): शहरों में कुओं का उपयोग केवल कपड़े धोने के लिए किया जाता था।\nकारण (R): ईंटों से बने कुओं ने पीने, घरेलू आवश्यकताओं और बगीचे की सिंचाई के लिए पानी की आपूर्ति की।", 3, "A गलत है क्योंकि कुओं के कई उपयोग थे, R सही है।"),
    ("कथन (A): गबरबंद बंगाल के डेल्टा क्षेत्र में बने पत्थर के बांध थे।\nकारण (R): वे बलूचिस्तान की पहाड़ी घाटियों में बारिश का पानी रोकने के लिए बनाए गए थे।", 3, "A गलत है क्योंकि वे बलूचिस्तान में थे, R सही है।")
]:
    s2_mastery_hin.append({"type": "Assertion-Reason", "q": q, "opts": hin_ar_opts, "ans": ans, "sol": sol})

# Statement-Based (5)
for q, ans, sol in [
    ("Consider the following statements:\nStatement 1: The ploughed field discovered at Kalibangan shows a grid pattern of furrows.\nStatement 2: The Banawali terracotta model shows that ploughshares were curved.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct, verifying tillage technology."),
    ("Consider the following statements:\nStatement 1: Canals were the primary source of irrigation throughout the alluvial plains of Sindh.\nStatement 2: Water reservoirs carved from stone bedrock were excavated at Dholavira.\nWhich of the statements given above is/are correct?", 1, "Statement 1 is incorrect: canals are absent in Sindh plains due to siltation. Statement 2 is correct."),
    ("Consider the following statements:\nStatement 1: Sickles used for harvesting wheat were made of polished iron blades.\nStatement 2: Copper and bronze sickles were rare compared to chert stone blades.\nWhich of the statements given above is/are correct?", 1, "Statement 1 is incorrect: iron was unknown. Statement 2 is correct."),
    ("Consider the following statements:\nStatement 1: Shortughai was situated on the banks of the Oxus River in northern Afghanistan.\nStatement 2: Shortughai features ruins of ancient stone-lined canals.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct."),
    ("Consider the following statements:\nStatement 1: Gabarbands are check dams constructed of stone rubble across dry streams.\nStatement 2: Gabarbands are found predominantly in the flat plains of Punjab.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: they are found in hilly Baluchistan, not flat Punjab.")
]:
    s2_mastery_eng.append({"type": "Statement-Based", "q": q, "opts": mcq_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: कालीबंगन में खोजा गया जुता हुआ खेत हल की रेखाओं का ग्रिड पैटर्न दिखाता है।\nकथन 2: बनावली से मिला मिट्टी का हल दर्शाता है कि हल का फलक मुड़ा हुआ था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 2, "दोनों कथन सही हैं, जो हड़प्पा की जुताई तकनीक को सिद्ध करते हैं।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: सिंध के जलोढ़ मैदानों में नहरें ही सिंचाई का प्राथमिक स्रोत थीं।\nकथन 2: धोलावीरा में चट्टानों को काटकर बनाए गए जलाशय खोजे गए हैं।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 1, "कथन 1 गलत है क्योंकि मैदानों में नहरें नहीं थीं। कथन 2 सही है।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: गेहूँ की कटाई के लिए प्रयुक्त हँसिए चमकीले लोहे के फलकों से बने थे।\nकथन 2: चर्ट पत्थर के फलकों की तुलना में तांबे और कांसे के हँसिए दुर्लभ थे।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 1, "कथन 1 गलत है क्योंकि लोहे का ज्ञान नहीं था। कथन 2 सही है।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: शोर्तुघई उत्तरी अफगानिस्तान में आक्सस नदी के किनारे स्थित था।\nकथन 2: शोर्तुघई में प्राचीन पत्थर की नहरों के अवशेष मिले हैं।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 2, "दोनों कथन सही हैं।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: गबरबंद सूखी मौसमी नदियों पर पत्थरों से बनाए गए बांध थे।\nकथन 2: गबरबंद मुख्य रूप से पंजाब के समतल मैदानों में पाए जाते हैं।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि ये पहाड़ी बलूचिस्तान में थे, पंजाब में नहीं।")
]:
    s2_mastery_hin.append({"type": "Statement-Based", "q": q, "opts": hin_mcq_opts, "ans": ans, "sol": sol})

# Why (3)
for q, sol in [
    ("Why did the Harappans manufacture composite harvesting sickles using chert blades rather than metal sickles?", "Copper and bronze were rare and valuable metals, mostly reserved for weapons, specialized tools, and elite ornaments. Chert was abundant, hard, and could be easily knapped into razor-sharp blades, making it the most cost-effective material for harvesting sickles."),
    ("Why was rainwater harvesting and storage developed to such a high degree at Dholavira?", "Dholavira is located on Khadir Bet island in the Rann of Kutch, an arid region surrounded by salt flats with no perennial rivers. Rain was seasonal and scarce, making rainwater harvesting via check dams and massive reservoirs critical for the city's survival."),
    ("Why do we find ancient canals at Shortughai but not in the main Indus Valley plains?", "Shortughai was located in northern Afghanistan where rainfall was extremely low, requiring river water to be diverted to sustain crops. In the main Indus basin, the silt load of river floods buried shallow canals, while well irrigation and natural flood basins made canals less essential.")
]:
    s2_mastery_eng.append({"type": "Why", "q": q, "sol": sol})

for q, sol in [
    ("हड़प्पा वासियों ने धातु के हँसियों के बजाय चर्ट के फलक (blades) वाले संयुक्त हँसियों का निर्माण क्यों किया?", "तांबा और कांसा दुर्लभ और कीमती धातुएं थीं, जिन्हें हथियारों, विशिष्ट उपकरणों और गहनों के लिए सुरक्षित रखा जाता था। चर्ट आसानी से उपलब्ध था और इसके फलक बेहद तेज होते थे, जिससे यह फसल कटाई के लिए सबसे किफायती माध्यम था।"),
    ("धोलावीरा में वर्षा जल संचयन और भंडारण का इतना उन्नत विकास क्यों किया गया था?", "धोलावीरा कच्छ के रन में खादिर बेट द्वीप पर स्थित है, जो एक शुष्क क्षेत्र है और जहां कोई बारहमासी नदियां नहीं हैं। वर्षा बहुत कम और मौसमी होती थी, इसलिए जलाशयों में बारिश का पानी रोकना ही नगर के जीवित रहने का एकमात्र उपाय था।"),
    ("हमें शोर्तुघई में प्राचीन नहरें मिलती हैं लेकिन मुख्य सिंधु घाटी के मैदानों में क्यों नहीं मिलतीं?", "शोर्तुघई उत्तरी अफगानिस्तान में स्थित था जहाँ वर्षा बहुत कम थी, जिससे फसलों के लिए नदी का पानी मोड़ना जरूरी था। सिंधु मैदानों में भारी गाद के कारण नहरें दब गईं और बाढ़ के पानी से प्राकृतिक सिंचाई हो जाती थी।")
]:
    s2_mastery_hin.append({"type": "Why", "q": q, "sol": sol})

# How (3)
for q, sol in [
    ("How did Baluchistan's Gabarbands function to support agriculture in arid valleys?", "Gabarbands were stone check dams built across dry stream beds. During seasonal rains, they slowed down water run-off, allowing water to saturate the soil and forcing the silt to settle. This created small patches of flat, highly fertile damp soil behind the dams for cultivation."),
    ("How did Dholavira's hydraulic engineers divert water from seasonal streams into the city reservoirs?", "They constructed stone masonry dams across the seasonal Manhar and Mandsar torrents. Inlet channels and stone drains connected these dams to the network of reservoirs, allowing stormwater run-off to flow directly into the massive storage tanks."),
    ("How were Harappan chert sickles constructed and assembled by artisans?", "Artisans chipped fine chert nodules into thin, razor-like blades. They carved a curved slot into a wooden or bone handle, inserted the chert blades in a row, and secured them using natural bitumen (asphalt) or tree resin as an adhesive glue.")
]:
    s2_mastery_eng.append({"type": "How", "q": q, "sol": sol})

for q, sol in [
    ("बलूचिस्तान के गबरबंदों ने शुष्क घाटियों में कृषि का समर्थन करने के लिए कैसे काम किया?", "गबरबंद मौसमी नालों पर बने बांध थे। जब बारिश होती थी, तो ये पानी के तेज बहाव को रोकते थे, जिससे पानी मिट्टी में रिस जाता था और मिट्टी की गाद बांध के पीछे जमा हो जाती थी। इससे खेती के लिए उपजाऊ और नमी युक्त समतल भूमि तैयार होती थी।"),
    ("धोलावीरा के जल इंजीनियरों ने मौसमी नदियों से पानी शहर के जलाशयों में कैसे मोड़ा था?", "उन्होंने मनहर और मंदसर नदियों पर पत्थरों के बांध बनाए। इन बांधों से नहरें और नालियां बनाई गईं जो जलाशयों से जुड़ी थीं, जिससे बारिश का पानी बहकर सीधे शहर के बड़े टैंकों में जमा हो जाता था।"),
    ("हड़प्पा के कारीगरों द्वारा चर्ट के हँसियों का निर्माण और संयोजन कैसे किया जाता था?", "कारीगर चर्ट पत्थरों को तोड़कर पतले और तेज फलक बनाते थे। वे लकड़ी या हड्डी के घुमावदार हत्थे में एक खांचा बनाते थे, उसमें चर्ट फलकों को कतार में रखकर प्राकृतिक राल या कोलतार (bitumen) से चिपका देते थे।")
]:
    s2_mastery_hin.append({"type": "How", "q": q, "sol": sol})

# Case Study (3)
for q, sol in [
    ("Case Study: The Kalibangan Pre-Mature Field. Discuss the tillage pattern.", "Excavated in the 1960s, the field at Kalibangan shows grid furrows in two directions: one set spaced 30 cm apart running north-south, and another spaced 1.9 m apart running east-west. This matches modern Rajasthani grid-ploughing where mustard is grown in wide furrows and chickpeas in narrow ones, showing ancient continuity."),
    ("Case Study: Shortughai Canal Irrigation. Analyze the hydraulic ruins.", "Shortughai on the Oxus River features clear traces of canals. The longest channel runs over 10 km, diverting river water to the dry plains. The presence of these canals alongside typical Indus weights and seals shows that Harappan colonists brought their advanced water diversion technology to Central Asia."),
    ("Case Study: Dholavira's Rainwater Harvesting. Analyze the scale of engineering.", "Dholavira's citadel was surrounded by 16 massive reservoirs, the largest measuring 73 x 29 x 10 m, capable of holding millions of liters of water. The reservoirs were cut into solid rock and lined with clay plaster to prevent seepage, illustrating advanced hydraulic knowledge.")
]:
    s2_mastery_eng.append({"type": "Case Study", "q": q, "sol": sol})

for q, sol in [
    ("केस स्टडी: कालीबंगन का पूर्व-परिपक्व खेत। जुताई के पैटर्न का विश्लेषण करें।", "1960 के दशक में खोजे गए इस खेत में दो दिशाओं में हल की रेखाएं मिली हैं: एक उत्तर-दक्षिण (30 सेमी दूरी) और दूसरी पूर्व-पश्चिम (1.9 मीटर दूरी)। यह आधुनिक राजस्थान के बुवाई पैटर्न से मेल खाता है जहाँ चौड़ी रेखाओं में सरसों और तंग रेखाओं में चना बोया जाता है।"),
    ("केस स्टडी: शोर्तुघई नहर सिंचाई। इसके पुरातात्विक अवशेषों का विश्लेषण करें।", "आक्सस नदी पर शोर्तुघई से नहरों के अवशेष मिले हैं, जिनमें से सबसे लंबी नहर 10 किमी लंबी थी। यह दर्शाती है कि हड़प्पा वासियों ने सुदूर बदख्शां में खेती को जीवित रखने के लिए अपनी जल मोड़ने (water diversion) की उन्नत तकनीक का सफलतापूर्वक उपयोग किया।"),
    ("केस स्टडी: धोलावीरा का वर्षा जल संचयन। इंजीनियरिंग के पैमाने का विश्लेषण करें।", "धोलावीरा का नगर दुर्ग 16 जलाशयों से घिरा था, जिनमें सबसे बड़ा 73 x 29 x 10 मीटर का था जो लाखों लीटर पानी रोक सकता था। चट्टानों को काटने के बाद दीवारों पर मिट्टी का लेप किया गया था ताकि पानी का रिसाव न हो, जो जल प्रबंधन का अद्भुत उदाहरण है।")
]:
    s2_mastery_hin.append({"type": "Case Study", "q": q, "sol": sol})

# Teach Concept (3)
for q, sol in [
    ("Teach the Concept: Siltation and the Invisibility of Ancient Canals.", "Explain to students that the Indus River carries massive silt loads. In flat plains, floodwaters deposit silt, raising the ground level by several meters over millennia. This process buries shallow dirt canals, explaining why plains canals are invisible, while wells (which are deep vertical structures) survive."),
    ("Teach the Concept: Sluice-Gate Control in Estuary and Inundation Systems.", "Explain how Harappan engineers used wooden barrier gates to block or open canals during flood surges. By opening the gate during high floods, they allowed water to fill reservoirs and basins, and by closing it, they trapped the water for dry-season crop cultivation."),
    ("Teach the Concept: The Grid Furrow System of Double-Cropping.", "Teach how grid-ploughing works: the crossing lines create square cells. Tall crops like mustard are planted in the widely spaced furrows, while short crops like chickpeas are grown in the closely spaced ones. This ensures both crops get sunlight and nutrients without crowding.")
]:
    s2_mastery_eng.append({"type": "Teach Concept", "q": q, "sol": sol})

for q, sol in [
    ("अवधारणा सिखाएं: गाद जमाव (Siltation) और प्राचीन नहरों का लुप्त होना।", "छात्रों को समझाएं कि सिंधु नदी भारी मात्रा में गाद (silt) बहाकर लाती है। वार्षिक बाढ़ के साथ गाद जमा होने से मैदानी भूमि का स्तर सदियों में कई मीटर बढ़ गया। इससे खेतों की उथली नहरें मिट्टी में दब गईं, जबकि कुएं अपनी गहराई के कारण आज भी मिलते हैं।"),
    ("अवधारणा सिखाएं: बाढ़ सिंचाई प्रणालियों में लॉक-गेट (Sluice-gate) का नियंत्रण।", "समझाएं कि कैसे बाढ़ के समय पानी मोड़ने के लिए लकड़ी के फाटकों का उपयोग किया जाता था। बाढ़ के समय द्वार खोलकर जलाशयों को भरा जाता था, और बाढ़ उतरने के बाद द्वार बंद कर पानी को रोक लिया जाता था ताकि शुष्क महीनों में खेती की जा सके।"),
    ("अवधारणा सिखाएं: दोहरी फसल बुवाई की ग्रिड प्रणाली।", "ग्रिड जुताई की बुवाई तकनीक समझाएं: एक-दूसरे को काटती रेखाएं चौकोर खाने बनाती हैं। चौड़ी रेखाओं में सरसों जैसी लंबी फसलें और संकरी रेखाओं में चने जैसी छोटी फसलें बोई जाती हैं ताकि दोनों फसलों को बिना रुकावट के सूर्य का प्रकाश और पोषण मिल सके।")
]:
    s2_mastery_hin.append({"type": "Teach Concept", "q": q, "sol": sol})


# =========================================================================
# SECTION 3: FOOD STORAGE, GRANARIES AND DECLINE
# =========================================================================
s3_mastery_eng = []
s3_mastery_hin = []

# MCQ (5)
for q, opts, ans, sol in [
    ("The Great Granary, a massive brick structure with sockets for timber columns, is located at which site?", ["Mohenjo-daro", "Harappa", "Kalibangan", "Lothal"], 0, "The Great Granary is located on the citadel mound of Mohenjo-daro."),
    ("Which site features a series of six granaries arranged in two rows of three near circular threshing platforms?", ["Harappa", "Mohenjo-daro", "Rakhigarhi", "Dholavira"], 0, "Harappa features six granaries near circular brick threshing floors."),
    ("Circular brick platforms excavated next to the granaries at Harappa served which agricultural function?", ["Threshing floors for grain processing", "Cattle pens for draft oxen", "Storage silos for crop husks", "Ritual fire altars"], 0, "Traces of wheat and barley chaff found in these platforms confirm they were threshing floors."),
    ("Which river system dried up around 1900 BCE due to tectonic shifts, leading to agrarian collapse in Cholistan?", ["Ghaggar-Hakra River system", "Indus River system", "Sabarmati River system", "Ganges River system"], 0, "The drying up of the Ghaggar-Hakra river system starved settlements of agricultural water, causing collapse."),
    ("The decline of agricultural surplus during the Late Harappan phase caused populations to migrate where?", ["Eastward and southward (Ganga Doab and Gujarat)", "Westward to Mesopotamia", "Northward to the Hindu Kush mountains", "Southward to Sri Lanka"], 0, "Populations migrated east into the Ganga-Yamuna Doab and south into Gujarat as the core agricultural lands desiccated.")
]:
    s3_mastery_eng.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("पकी ईंटों से बना 'विशाल अन्नागार', जिसमें लकड़ी के खंभों के लिए खांचे बने थे, किस स्थल पर स्थित है?", ["मोहनजोदड़ो", "हड़प्पा", "कालीबंगन", "लोथल"], 0, "विशाल अन्नागार मोहनजोदड़ो के नगर दुर्ग (citadel) पर स्थित है।"),
    ("किस स्थल पर वृत्ताकार खलिहानों के पास तीन-तीन की दो कतारों में व्यवस्थित छह अन्नागार मिले हैं?", ["हड़प्पा", "मोहनजोदड़ो", "राखीगढ़ी", "धोलावीरा"], 0, "हड़प्पा से कतारबद्ध छह अन्नागार मिले हैं जो वृत्ताकार चबूतरों के निकट थे।"),
    ("हड़प्पा में अन्नागारों के पास मिले ईंटों के वृत्ताकार चबूतरे किस कृषि कार्य के काम आते थे?", ["अनाज की गहाई (Threshing) के लिए", "बैलों को बांधने के लिए", "भूसे के भंडारण के लिए", "हवन कुंड के रूप में"], 0, "वृत्ताकार चबूतरों में मिले गेहूँ और जौ के अवशेषों से सिद्ध होता है कि ये खलिहान (threshing floors) थे।"),
    ("विवर्तनिक हलचलों के कारण 1900 ईसा पूर्व के आसपास कौन सी नदी प्रणाली सूख गई, जिससे चोलिस्तान में कृषि संकट पैदा हुआ?", ["घग्गर-हकरा नदी प्रणाली", "सिंधु नदी प्रणाली", "साबरमती नदी प्रणाली", "गंगा नदी प्रणाली"], 0, "घग्गर-हकरा नदी के सूखने से चोलिस्तान क्षेत्र की कृषि बस्तियां उजड़ गईं।"),
    ("उत्तर-हड़प्पा काल में कृषि अधिशेष समाप्त होने के कारण शहरी आबादी ने किस ओर पलायन किया?", ["पूर्व और दक्षिण की ओर (गंगा दोआब और गुजरात)", "पश्चिम में मेसोपोटामिया की ओर", "उत्तर में हिंदूकुश पहाड़ों की ओर", "दक्षिण में श्रीलंका की ओर"], 0, "कृषि भूमि सूखने के कारण आबादी पूर्व में गंगा-यमुना दोआब और दक्षिण में गुजरात की ओर विस्थापित हो गई।")
]:
    s3_mastery_hin.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# Multiple Correct MCQ (5)
for q, opts, ans, sol in [
    ("Which of the following structures were used for storing agricultural surplus in Indus cities? (Select all that apply)", ["The Great Granary at Mohenjo-daro", "Six granaries in a row at Harappa", "Brick platforms at Kalibangan", "Hollow stone pyramids"], [0, 1, 2], "Great Granary, Harappa granaries, and Kalibangan brick platforms were storage units. Pyramids are Egyptian."),
    ("Select the plant remains discovered in the brick crevasses of Harappa's circular platforms: (Select all that apply)", ["Wheat grains", "Barley grains", "Straw/chaff remains", "Rice grains in bulk"], [0, 1, 2], "Wheat, barley, and straw remains were found on Harappa's circular platforms. Rice was absent in the north."),
    ("Which environmental factors contributed to the decline of Harappan agricultural productivity around 1900 BCE? (Select all that apply)", ["Weakening of the summer monsoon", "Tectonic shifts drying up the Ghaggar-Hakra", "Soil salinization from over-irrigation", "Sudden volcanic eruptions in Sindh"], [0, 1, 2], "Monsoon failures, drying of rivers, and salinization were key factors. There were no volcanic eruptions in Sindh."),
    ("How did Harappans transport crop surplus from rural hinterlands to the urban granaries? (Select all that apply)", ["Solid-wheeled wooden bullock carts", "Flat-bottomed river cargo boats", "Caravans of pack-oxen", "Horse-drawn grain chariots"], [0, 1, 2], "Bullock carts, river boats, and pack animal caravans were used. Horse chariots did not exist."),
    ("Which of the following functions did the public granaries serve in the Harappan state? (Select all that apply)", ["A food security reserve against crop failures", "A central storehouse for trade and export", "A tax collection depot for agrarian tribute", "Barracks for housing municipal armies"], [0, 1, 2], "Granaries served as food reserves, trade depots, and tax collection points. There were no municipal armies."),
]:
    s3_mastery_eng.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("हड़प्पा शहरों में कृषि अधिशेष के भंडारण के लिए किन संरचनाओं का उपयोग किया जाता था? (सभी लागू विकल्प चुनें)", ["मोहनजोदड़ो का विशाल अन्नागार", "हड़प्पा के छह कतारबद्ध अन्नागार", "कालीबंगन के ईंटों के चबूतरे", "खोखले प्रस्तर पिरामिड"], [0, 1, 2], "मोहनजोदड़ो का अन्नागार, हड़प्पा के अन्नागार और कालीबंगन के चबूतरे भंडारण स्थल थे। पिरामिड मिस्र के थे।"),
    ("हड़प्पा के वृत्ताकार चबूतरों की दरारों से कौन से पादप अवशेष खोजे गए हैं? (सभी लागू विकल्प चुनें)", ["गेहूँ के दाने", "जौ के दाने", "भूसी/पुआल के अवशेष", "चावल के दानों के विशाल ढेर"], [0, 1, 2], "चबूतरों से गेहूँ, जौ और भूसी के अवशेष मिले हैं। चावल उत्तर में अनुपस्थित था।"),
    ("1900 ईसा पूर्व के आसपास किन पर्यावरणीय कारकों ने हड़प्पा कृषि उत्पादकता के पतन में योगदान दिया? (सभी लागू विकल्प चुनें)", ["ग्रीष्मकालीन मानसून का कमजोर होना", "विवर्तनिक बदलावों से घग्गर-हकरा का सूखना", "अत्यधिक सिंचाई से मिट्टी का लवणीकरण", "सिंध में अचानक ज्वालामुखी विस्फोट"], [0, 1, 2], "मानसून विफलता, नदियों का सूखना और लवणीकरण मुख्य कारक थे। सिंध में कोई ज्वालामुखी विस्फोट नहीं हुआ।"),
    ("हड़प्पा वासी ग्रामीण इलाकों से शहरी अन्नागारों तक अनाज अधिशेष का परिवहन कैसे करते थे? (सभी लागू विकल्प चुनें)", ["ठोस पहियों वाली लकड़ी की बैलगाड़ियाँ", "चपटी तली वाली मालवाहक नावें", "बैलों के कारवां", "घोड़ों से चलने वाले रथ"], [0, 1, 2], "परिवहन बैलगाड़ियों, नावों और बैलों के कारवां से होता था। घोड़ों के रथ नहीं थे।"),
    ("सार्वजनिक अन्नागारों ने हड़प्पा राज्य में किन कार्यों को पूरा किया? (सभी लागू विकल्प चुनें)", ["फसल विफलता के खिलाफ खाद्य सुरक्षा का बफर स्टॉक", "व्यापार और निर्यात के लिए केंद्रीय भंडारण", "अनाज के रूप में कर संग्रह का डिपो", "सैन्य बलों के लिए बैरक"], [0, 1, 2], "अन्नागार बफर स्टॉक, व्यापार डिपो और कर संग्रह स्थल थे। वहां सेना के बैरक नहीं थे।")
]:
    s3_mastery_hin.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# True/False (8)
for q, ans, sol in [
    ("The Great Granary of Mohenjo-daro was located inside the lower town area.", False, "False. The Great Granary was located on the high citadel mound."),
    ("Wheat and barley residues have been discovered inside the brick platforms at Harappa.", True, "True. Grains of wheat and barley were trapped in circular threshing platforms."),
    ("Harappan granaries utilized elevated floors and air passages to prevent grain spoilage.", True, "True. Air ducts beneath the structures kept the grain dry and fresh."),
    ("The Ghaggar-Hakra river system is still a major perennial flowing river today.", False, "False. The river dried up in antiquity, leaving a dry channel valley."),
    ("A weakening of the summer monsoon around 1900 BCE triggered agricultural decline.", True, "True. Monsoon desiccation dried up water sources, lowering crop yields."),
    ("Bullock carts were the primary transport vehicle for carrying crop taxes.", True, "True. Oxen pulled cartloads of tax grain from villages to cities."),
    ("The collapse of farming surplus led directly to the abandonment of the cities.", True, "True. Without a crop surplus, the large urban population could not survive."),
    ("Rice was the main grain stored inside the Great Granary of Mohenjo-daro.", False, "False. Wheat and barley were the main grains stored; rice was rare.")
]:
    s3_mastery_eng.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("मोहनजोदड़ो का विशाल अन्नागार निचले नगर (lower town) के भीतर स्थित था।", False, "असत्य। विशाल अन्नागार नगर के उच्च दुर्ग (citadel) पर स्थित था।"),
    ("हड़प्पा के वृत्ताकार चबूतरों की दरारों से गेहूँ और जौ के अवशेष मिले हैं।", True, "सत्य। गहाई के इन चबूतरों की दरारों में अनाज के दाने फंसे हुए पाए गए।"),
    ("हड़प्पा के अन्नागारों में अनाज सड़ने से बचाने के लिए ऊंचे फर्श और हवा के मार्ग बने थे।", True, "सत्य। अन्नागार के नीचे बनी हवा की नालियाँ अनाज को नमी से दूर और ताजा रखती थीं।"),
    ("घग्गर-हकरा नदी प्रणाली आज भी एक प्रमुख बारहमासी बहती हुई नदी है।", False, "असत्य। यह नदी प्राचीन काल में ही सूख गई थी और आज केवल इसका सूखा मार्ग बचा है।"),
    ("1900 ईसा पूर्व के आसपास ग्रीष्मकालीन मानसून के कमजोर होने से कृषि का पतन हुआ।", True, "सत्य। मानसून कमजोर होने से जल संकट बढ़ा और फसल की पैदावार घट गई।"),
    ("फसल के रूप में कर एकत्र करने के लिए बैलगाड़ियाँ मुख्य परिवहन वाहन थीं।", True, "सत्य। गाँव के कर अनाज को शहरों तक पहुँचाने के लिए बैलगाड़ियों का ही उपयोग होता था।"),
    ("कृषि अधिशेष के पतन के कारण ही सिंधु शहरों का परित्याग करना पड़ा।", True, "सत्य। शहरों की गैर-कृषि आबादी पूरी तरह से ग्रामीण खाद्यान्न अधिशेष पर निर्भर थी, जिसके समाप्त होने से शहर उजड़ गए।"),
    ("मोहनजोदड़ो के विशाल अन्नागार में जमा किया जाने वाला मुख्य अनाज चावल था।", False, "असत्य। मुख्य रूप से गेहूँ और जौ जमा किए जाते थे; चावल दुर्लभ था।")
]:
    s3_mastery_hin.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

# Fill Blanks (8)
for q, ans, sol in [
    ("The Great Granary was constructed on the citadel of ________.", "Mohenjo-daro", "Mohenjo-daro has the Great Granary on its citadel."),
    ("Harappa features a series of ________ granaries near circular brick platforms.", "six", "Harappa has six granaries arranged in two rows."),
    ("The circular platforms next to the granaries functioned as ________ floors.", "threshing", "They were used as threshing floors to process wheat and barley."),
    ("The dry river system that starved Cholistan settlements of water was the ________.", "Ghaggar-Hakra", "The drying of the Ghaggar-Hakra starved Cholistan sites."),
    ("The agricultural economy and urban cities collapsed around ________ BCE.", "1900", "1900 BCE marks the transition to the Late/Post-urban phase."),
    ("Food was carried to urban centers using solid-wheeled ________.", "bullock carts", "Oxen-driven bullock carts were the primary land transport."),
    ("To keep grain dry, granaries featured brick floors elevated over air ________.", "ducts", "Air ducts provided ventilation to prevent dampness and rot."),
    ("Agrarian collapse forced populations to migrate towards the ________ valley.", "Ganga", "Populations migrated east into the Ganga-Yamuna Doab.")
]:
    s3_mastery_eng.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("विशाल अन्नागार का निर्माण ________ के नगर दुर्ग (Citadel) पर किया गया था।", "मोहनजोदड़ो", "विशाल अन्नागार मोहनजोदड़ो के दुर्ग में स्थित था।"),
    ("हड़प्पा में वृत्ताकार चबूतरों के निकट ________ कतारबद्ध अन्नागार मिले हैं।", "छह", "हड़प्पा से छह अन्नागार मिले हैं जो दो कतारों में व्यवस्थित थे।"),
    ("अन्नागारों के निकट मिले ईंटों के वृत्ताकार चबूतरे ________ फर्श का काम करते थे।", "गहाई", "वे अनाज की गहाई (threshing) के चबूतरे थे।"),
    ("चोलिस्तान की बस्तियों को उजाड़ने वाली सूखी नदी प्रणाली का नाम ________ है।", "घग्गर-हकरा", "घग्गर-हकरा नदी सूखने से चोलिस्तान के स्थल उजड़ गए।"),
    ("सिंधु की कृषि अर्थव्यवस्था और बड़े शहरों का पतन लगभग ________ ईसा पूर्व हुआ था।", "1900", "1900 ईसा पूर्व परिपक्व हड़प्पा काल के अंत का समय है।"),
    ("अधिशेष खाद्यान्न को ग्रामीण क्षेत्रों से ठोस पहियों वाली ________ द्वारा लाया जाता था।", "बैलगाड़ियों", "बैलगाड़ियाँ थल परिवहन का मुख्य साधन थीं।"),
    ("अनाज को नमी से बचाने के लिए अन्नागारों के फर्श के नीचे हवा की ________ बनी थीं।", "नालियाँ", "हवा की नालियाँ (air ducts) फर्श को हवादार रखती थीं।"),
    ("कृषि संकट के कारण आबादी पूर्व की ओर विस्थापित होकर ________ घाटी की ओर गई।", "गंगा", "लोग पूर्व में गंगा-यमुना घाटी की ओर चले गए।")
]:
    s3_mastery_hin.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

# Matchings (3)
s3_mastery_eng.extend([
    {
        "type": "Match the Following",
        "q": "Match the storage structures with their discovery locations:",
        "items": [{"left": "I. Great Granary", "key": "A"}, {"left": "II. Six Granaries", "key": "B"}, {"left": "III. Platform storage", "key": "C"}],
        "options": [{"val": "A", "text": "A. Mohenjo-daro citadel"}, {"val": "B", "text": "B. Harappa riverside area"}, {"val": "C", "text": "C. Kalibangan platform mounds"}],
        "sol": "Great Granary is at Mohenjo-daro, six granaries at Harappa, and platform storage at Kalibangan."
    },
    {
        "type": "Match the Following",
        "q": "Match the environmental disasters with their agricultural impacts:",
        "items": [{"left": "I. Monsoon shift", "key": "A"}, {"left": "II. Tectonic shifts", "key": "B"}, {"left": "III. Land salinization", "key": "C"}],
        "options": [{"val": "A", "text": "A. Weakened winter/summer rains"}, {"val": "B", "text": "B. Dried up the Ghaggar-Hakra"}, {"val": "C", "text": "C. Spoiled fields with salt crusts"}],
        "sol": "Monsoon shift reduced rains, tectonic shifts dried rivers, and salinization ruined fields."
    },
    {
        "type": "Match the Following",
        "q": "Match the grain process stage with their architectural indicators:",
        "items": [{"left": "I. Grain Threshing", "key": "A"}, {"left": "II. Bulk Storage", "key": "B"}, {"left": "III. Inland Transport", "key": "C"}],
        "options": [{"val": "A", "text": "A. Circular brick platforms at Harappa"}, {"val": "B", "text": "B. Massive elevated brick platforms"}, {"val": "C", "text": "C. Terracotta model bullock carts"}],
        "sol": "Threshing was on circular platforms, storage in granary platforms, and transport via bullock carts."
    }
])

s3_mastery_hin.extend([
    {
        "type": "Match the Following",
        "q": "भंडारण संरचनाओं को उनके खोज स्थलों से सुमेलित करें:",
        "items": [{"left": "I. विशाल अन्नागार", "key": "A"}, {"left": "II. छह अन्नागार", "key": "B"}, {"left": "III. चबूतरा भंडारण", "key": "C"}],
        "options": [{"val": "A", "text": "A. मोहनजोदड़ो नगर दुर्ग"}, {"val": "B", "text": "B. हड़प्पा नदी तट क्षेत्र"}, {"val": "C", "text": "C. कालीबंगन चबूतरा टीले"}],
        "sol": "विशाल अन्नागार मोहनजोदड़ो में, छह अन्नागार हड़प्पा में और चबूतरा भंडारण कालीबंगन में थे।"
    },
    {
        "type": "Match the Following",
        "q": "पर्यावरणीय आपदाओं को उनके कृषि प्रभावों से सुमेलित करें:",
        "items": [{"left": "I. मानसून का बदलना", "key": "A"}, {"left": "II. विवर्तनिक बदलाव", "key": "B"}, {"left": "III. लवणीकरण", "key": "C"}],
        "options": [{"val": "A", "text": "A. शीत/ग्रीष्म वर्षा का कमजोर होना"}, {"val": "B", "text": "B. घग्गर-हकरा नदी का सूखना"}, {"val": "C", "text": "C. खेतों पर नमक की परत जमा होना"}],
        "sol": "मानसून बदलने से वर्षा कम हुई, विवर्तनिक बदलाव से नदी सूखी, और लवणीकरण से मिट्टी खराब हुई।"
    },
    {
        "type": "Match the Following",
        "q": "अनाज प्रसंस्करण के चरणों को उनके पुरातात्विक साक्ष्यों से सुमेलित करें:",
        "items": [{"left": "I. अनाज की गहाई", "key": "A"}, {"left": "II. थोक भंडारण", "key": "B"}, {"left": "III. अंतर्देशीय परिवहन", "key": "C"}],
        "options": [{"val": "A", "text": "A. हड़प्पा में ईंटों के वृत्ताकार चबूतरे"}, {"val": "B", "text": "B. अन्नागारों के विशाल मंच"}, {"val": "C", "text": "C. मिट्टी के खिलौना बैलगाड़ियाँ"}],
        "sol": "गहाई वृत्ताकार चबूतरों पर, थोक भंडारण अन्नागार मंच पर और परिवहन बैलगाड़ियों से होता था।"
    }
])

# One-Liner (8)
for q, sol in [
    ("Where was the Great Granary discovered?", "Mohenjo-daro."),
    ("How many granaries are located at Harappa?", "Six (in two rows of three)."),
    ("What function did the circular brick platforms at Harappa perform?", "Threshing floors."),
    ("Which river dried up, causing collapse in Cholistan?", "Ghaggar-Hakra."),
    ("When did the urban agricultural economy collapse?", "c. 1900 BCE."),
    ("What animal pulled grain carts to cities?", "Oxen (bullocks)."),
    ("Where did populations migrate after the agricultural collapse?", "East (Ganga valley) and South (Gujarat)."),
    ("What ventilated the floors of Harappan granaries?", "Air ducts (air passages).")
]:
    s3_mastery_eng.append({"type": "One-Liner", "q": q, "sol": sol})

for q, sol in [
    ("विशाल अन्नागार किस स्थल पर खोजा गया था?", "मोहनजोदड़ो।"),
    ("हड़प्पा में कितने अन्नागार मिले हैं?", "छह (तीन-तीन की दो पंक्तियों में)।"),
    ("हड़प्पा के वृत्ताकार चबूतरों का क्या कार्य था?", "अनाज की गहाई (threshing floors)।"),
    ("चोलिस्तान में सूखा लाने वाली नदी का नाम क्या था?", "घग्गर-हकरा।"),
    ("शहरी कृषि अर्थव्यवस्था किस वर्ष के आसपास समाप्त हो गई?", "लगभग 1900 ईसा पूर्व।"),
    ("शहरों तक अनाज ढोने वाली गाड़ियों को कौन खींचता था?", "बैल।"),
    ("कृषि पतन के बाद आबादी किस दिशा में विस्थापित हुई?", "पूर्व (गंगा घाटी) और दक्षिण (गुजरात) की ओर।"),
    ("अन्नागार के फर्श को सूखा रखने के लिए क्या बना हुआ था?", "हवा के मार्ग (Air ducts)।")
]:
    s3_mastery_hin.append({"type": "One-Liner", "q": q, "sol": sol})

# Assertion-Reason (8)
for q, ans, sol in [
    ("Assertion (A): The Great Granary was constructed on the high Mohenjo-daro citadel.\nReason (R): Placing the granary on the citadel protected the state's vital food reserve from seasonal river floods and kept it secure.", 0, "Both A and R are true and R explains why the granary was built on the elevated citadel mound."),
    ("Assertion (A): Circular brick platforms at Harappa are identified as threshing floors.\nReason (R): Grains of wheat and barley were recovered from the cracks of these platforms during excavations.", 0, "Both A and R are true and recovering grain residues proves they were used for threshing."),
    ("Assertion (A): The drying of the Ghaggar-Hakra river system caused the abandonment of many Cholistan cities.\nReason (R): The dried river basin lost its water supply, making the agricultural surplus necessary to feed cities impossible to grow.", 0, "Both A and R are true and the dry-up directly destroyed the agrarian surplus economy of Cholistan."),
    ("Assertion (A): The agricultural collapse was caused by massive volcanic eruptions that flooded Sindh with lava.\nReason (R): Climate desiccation and changes in river courses starved the crop fields of crucial water.", 3, "A is false because there were no volcanic eruptions in Sindh; R is true."),
    ("Assertion (A): Granaries were located close to river channels or city gates.\nReason (R): This location allowed easy unloading of crop tribute from river boats and rural bullock carts.", 0, "Both A and R are true and proximity to rivers and roads facilitated transport efficiency."),
    ("Assertion (A): Late Harappan populations migrated entirely to Central Asia to escape drought.\nReason (R): They migrated east towards the Ganga-Yamuna Doab and south towards Gujarat where rainfall was higher.", 3, "A is false because they migrated east/south, not to Central Asia; R is true."),
    ("Assertion (A): The Harappan granaries were built with timber superstructures on brick bases.\nReason (R): The brick platforms contain square sockets where wooden columns stood to support roofs.", 0, "Both A and R are true and sockets prove timber pillars supported the granary roof."),
    ("Assertion (A): The agricultural surplus was unaffected by monsoon cycles.\nReason (R): Weakening summer monsoons around 1900 BCE lowered rainfall, reducing river volume and crop yields.", 3, "A is false because monsoon cycles shaped the surplus; R is true.")
]:
    s3_mastery_eng.append({"type": "Assertion-Reason", "q": q, "opts": ar_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("कथन (A): विशाल अन्नागार का निर्माण मोहनजोदड़ो के ऊंचे दुर्ग पर किया गया था।\nकारण (R): अन्नागार को दुर्ग पर बनाने से राज्य के आपातकालीन खाद्यान्न भंडार को बाढ़ से सुरक्षा मिलती थी और यह सुरक्षित रहता था।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या करता है क्योंकि ऊंचे चबूतरे बाढ़ से अनाज बचाते थे।"),
    ("कथन (A): हड़प्पा के वृत्ताकार चबूतरों की पहचान खलिहान (threshing floors) के रूप में की गई है।\nकारण (R): चबूतरों की दरारों से खुदाई के दौरान गेहूँ और जौ के दानों के अवशेष प्राप्त हुए हैं।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या करता है क्योंकि अनाज मिलना ही गहाई सिद्ध करता है।"),
    ("कथन (A): घग्गर-हकरा नदी प्रणाली के सूखने से चोलिस्तान के कई शहरों का परित्याग करना पड़ा।\nकारण (R): सूखी नदी घाटी ने अपना जल स्रोत खो दिया, जिससे शहरों का पेट भरने के लिए आवश्यक कृषि अधिशेष उगाना असंभव हो गया।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या है।"),
    ("कथन (A): कृषि संकट सिंध में आए भयानक ज्वालामुखी विस्फोटों के कारण हुआ जिसने खेतों को लावा से पाट दिया।\nकारण (R): शुष्क जलवायु और नदियों के मार्ग बदलने से खेतों को मिलने वाला सिंचाई का पानी समाप्त हो गया।", 3, "A गलत है क्योंकि ज्वालामुखी विस्फोट नहीं हुए थे, R सही है।"),
    ("कथन (A): अन्नागारों को नदी जलमार्गों या शहर के द्वारों के समीप बनाया जाता था।\nकारण (R): इस स्थिति से नावों और बैलगाड़ियों द्वारा लाए गए अनाज कर को उतारना और संग्रहित करना आसान होता था।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या करता है।"),
    ("कथन (A): उत्तर-हड़प्पा काल के लोग सूखे से बचने के लिए पूरी तरह से मध्य एशिया की ओर चले गए।\nकारण (R): वे पूर्व में गंगा-यमुना दोआब और दक्षिण में गुजरात की ओर चले गए जहाँ अधिक वर्षा होती थी।", 3, "A गलत है क्योंकि वे पूर्व/दक्षिण गए थे, R सही है।"),
    ("कथन (A): हड़प्पा के अन्नागारों का निर्माण ईंटों के चबूतरे पर लकड़ी के ऊंचे ढांचों के रूप में किया गया था।\nकारण (R): ईंटों के मंचों में चौकोर खांचे मिले हैं जिनमें छत को थामने वाले लकड़ी के खंभे खड़े किए जाते थे।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या है।"),
    ("कथन (A): सिंधु का कृषि अधिशेष मानसून चक्रों से पूरी तरह से अप्रभावित रहता था।\nकारण (R): 1900 ईसा पूर्व के आसपास मानसून के कमजोर होने से वर्षा कम हुई, जिससे नदियों का जल स्तर और फसल उत्पादन घट गया।", 3, "A गलत है क्योंकि मानसून फसल उत्पादन के लिए महत्वपूर्ण था, R सही है।")
]:
    s3_mastery_hin.append({"type": "Assertion-Reason", "q": q, "opts": hin_ar_opts, "ans": ans, "sol": sol})

# Statement-Based (5)
for q, ans, sol in [
    ("Consider the following statements:\nStatement 1: The Great Granary is located at Mohenjo-daro.\nStatement 2: The Great Granary was built on a massive stone platform.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: it was built on a brick-faced platform, not stone."),
    ("Consider the following statements:\nStatement 1: The circular platforms at Harappa are rectangular in shape.\nStatement 2: They are located in the southern parts of the lower town.\nWhich of the statements given above is/are correct?", 3, "Both statements are incorrect: they are circular and situated on the northern side of Harappa near the river bed."),
    ("Consider the following statements:\nStatement 1: The drying of the Ghaggar-Hakra river system was a key cause of agrarian decline.\nStatement 2: Post-urban Harappans migrated east into the Ganga-Yamuna valley.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct, describing Late Harappan transitions."),
    ("Consider the following statements:\nStatement 1: The agrarian surplus was collected as tax using coins.\nStatement 2: Public granaries acted as centralized food reserves under administrative control.\nWhich of the statements given above is/are correct?", 1, "Statement 1 is incorrect: they used barter, not coins. Statement 2 is correct."),
    ("Consider the following statements:\nStatement 1: Weakening summer monsoons around 1900 BCE caused environmental drying.\nStatement 2: Silt-heavy floods in Sindh led to abandonment of fields.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct, representing two environmental causes of agrarian collapse.")
]:
    s3_mastery_eng.append({"type": "Statement-Based", "q": q, "opts": mcq_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: विशाल अन्नागार मोहनजोदड़ो में स्थित है।\nकथन 2: विशाल अन्नागार का निर्माण एक बड़े पत्थर के मंच पर किया गया था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि यह पकी ईंटों के मंच पर था, पत्थर पर नहीं।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: हड़प्पा के वृत्ताकार चबूतरे आयताकार आकार के हैं।\nकथन 2: ये निचले नगर के दक्षिणी भाग में स्थित हैं।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 3, "दोनों कथन गलत हैं क्योंकि चबूतरे वृत्ताकार हैं और हड़प्पा के उत्तरी किनारे पर नदी तट के समीप थे।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: घग्गर-हकरा नदी प्रणाली का सूखना कृषि पतन का एक मुख्य कारण था।\nकथन 2: उत्तर-शहरी काल के लोग पूर्व में गंगा-यमुना घाटी की ओर चले गए।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 2, "दोनों कथन सही हैं।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: कृषि अधिशेष को सिक्कों के माध्यम से कर के रूप में एकत्र किया जाता था।\nकथन 2: सार्वजनिक अन्नागार प्रशासनिक नियंत्रण में केंद्रीय खाद्य भंडार के रूप में कार्य करते थे।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 1, "कथन 1 गलत है क्योंकि सिक्के नहीं थे, विनिमय वस्तु विनिमय पर आधारित था। कथन 2 सही है।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: 1900 ईसा पूर्व के आसपास कमजोर मानसून ने पर्यावरण को शुष्क बना दिया।\nकथन 2: सिंध में गाद-युक्त विनाशकारी बाढ़ के कारण खेतों का परित्याग करना पड़ा।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 2, "दोनों कथन सही हैं, जो कृषि पतन के दो मुख्य कारणों को दर्शाते हैं।")
]:
    s3_mastery_hin.append({"type": "Statement-Based", "q": q, "opts": hin_mcq_opts, "ans": ans, "sol": sol})

# Why (3)
for q, sol in [
    ("Why did the Harappans design granaries with raised brick foundations and under-floor air passages?", "Indus Valley plains were humid and flood-prone. Raising the granary floor kept the stored crops safe from groundwater dampness and seasonal floodwaters, while the air ducts allowed air to circulate below, preventing moisture build-up, mold, and rot."),
    ("Why did the drying up of the Ghaggar-Hakra river system lead to the collapse of urban centers in Cholistan?", "Cholistan settlements were located along the Ghaggar-Hakra course. Tectonic shifts diverted its main tributaries (Sutlej and Yamuna) into the Indus and Ganga respectively. Without a regular river water supply, local crops failed, ending the agrarian surplus needed to sustain urban populations."),
    ("Why were public granaries strategically located on citadel mounds or near river channels?", "Citadels were elevated and fortified, providing protection from floods and security from looting. Locating granaries near river channels allowed cargo boats to unload grain tribute directly, reducing handling costs for the state administration.")
]:
    s3_mastery_eng.append({"type": "Why", "q": q, "sol": sol})

for q, sol in [
    ("हड़प्पा वासियों ने अन्नागारों को ऊंचे ईंटों के मंचों और हवादार फर्शों के साथ क्यों डिजाइन किया था?", "मैदानी भाग आर्द्र और बाढ़-प्रवण थे। फर्श ऊंचा रखने से अनाज भूजल की नमी और मौसमी बाढ़ से सुरक्षित रहता था, जबकि हवा की नालियों (air ducts) से हवा का प्रवाह बना रहता था जो फफूंद और सड़न को रोकता था।"),
    ("घग्गर-हकरा नदी प्रणाली के सूखने से चोलिस्तान के शहरी केंद्रों का पतन क्यों हुआ?", "चोलिस्तान की बस्तियां घग्गर नदी के किनारे बसी थीं। विवर्तनिक बदलावों से इसकी सहायक नदियां (सतलुज और यमुना) क्रमशः सिंधु और गंगा में मिल गईं। नदी सूखने से फसलें नष्ट हो गईं और शहरों का भरण-पोषण करने वाला अनाज अधिशेष समाप्त हो गया।"),
    ("सार्वजनिक अन्नागारों को नगर दुर्ग (Citadel) या नदियों के निकट रणनीतिक रूप से क्यों बनाया जाता था?", "दुर्ग ऊंचे और सुरक्षित स्थान थे जो बाढ़ और लूटपाट से रक्षा करते थे। नदियों के निकट बनाने से मालवाहक नावों से अनाज उतारना और सीधे अन्नागारों में पहुँचाना आसान होता था, जिससे श्रम लागत कम होती थी।")
]:
    s3_mastery_hin.append({"type": "Why", "q": q, "sol": sol})

# How (3)
for q, sol in [
    ("How did Harappan rulers coordinate the food supply from rural zones to support urban specialization?", "They established a centralized distribution network. Bullock carts brought grain tribute from countryside farms to town gates. The state housed these grains in massive city granaries and redistributed them to non-farming specialists (artisans, scribes, administrative staff) as rations."),
    ("How did environmental climate shifts trigger the Late Harappan agrarian collapse?", "Weakening summer monsoons after 1900 BCE reduced river volumes. This decreased the area of fertile silty land flooded each year. The drop in soil fertility and water scarcity lowered crop yields, drying up the agricultural surplus that sustained large cities."),
    ("How were Harappa's circular brick platforms operated to process harvested grain?", "Artisans brought crop sheaves to these platforms. Grains were beaten against the circular bricks or stamped by oxen to separate the kernels from the stalks. The wind was then used for winnowing, leaving chaff residues in the central hollow of the platforms.")
]:
    s3_mastery_eng.append({"type": "How", "q": q, "sol": sol})

for q, sol in [
    ("हड़प्पा के शासकों ने शहरी कारीगरों को बनाए रखने के लिए ग्रामीण क्षेत्रों से अनाज आपूर्ति का प्रबंधन कैसे किया?", "उन्होंने एक प्रशासनिक वितरण प्रणाली बनाई। बैलगाड़ियों से अनाज को गांवों से लाकर शहरों के मुख्य द्वारों पर एकत्र किया जाता था। राज्य ने इसे बड़े अन्नागारों में जमा किया और फिर गैर-कृषि वर्ग (शिल्पियों, क्लर्कों, प्रशासनिक स्टाफ) में राशन के रूप में बांटा।"),
    ("पर्यावरणीय बदलावों ने उत्तर-हड़प्पा कृषि पतन को कैसे गति दी?", "1900 ईसा पूर्व के बाद मानसून कमजोर होने से नदियों में पानी कम हो गया। इससे वार्षिक बाढ़ का दायरा घट गया और उपजाऊ मिट्टी जमा होना कम हो गया। पानी की कमी और घटती उर्वरता ने फसलों के अधिशेष को समाप्त कर दिया जिससे शहर उजड़ गए।"),
    ("हड़प्पा के वृत्ताकार चबूतरों का उपयोग अनाज प्रसंस्करण (threshing) के लिए कैसे किया जाता था?", "फसल की बालियों को इन चबूतरों पर लाया जाता था। अनाज को अलग करने के लिए बालियों को चबूतरे की ईंटों पर पीटा जाता था या बैलों से कुचलवाया जाता था। हवा की मदद से ओसाने के बाद दाने अलग हो जाते थे और भूसा चबूतरे के केंद्रीय गड्ढे में जमा हो जाता था।")
]:
    s3_mastery_hin.append({"type": "How", "q": q, "sol": sol})

# Case Study (3)
for q, sol in [
    ("Case Study: The Great Granary Architecture. Analyze its layout and ventilation.", "Mohenjo-daro's Great Granary consists of a solid brick foundation measuring 45 x 15 m. It supported 27 wooden blocks that held the timber superstructure. The design left narrow air passages running beneath the wooden floors. This early ventilation system indicates a sophisticated state understanding of grain preservation under tropical climates."),
    ("Case Study: The Drying of the Sarasvati. Analyze river migrations in the Cholistan desert.", "The Ghaggar-Hakra dry channel in Bahawalpur (Pakistan) has over 170 sites. Tectonic shifts diverted the Sutlej into the Indus and the Yamuna into the Ganga. This starved the Sarasvati channel of its glacial waters, converting it into a seasonal dry track, demonstrating how geological shifts can destroy fertile agrarian basins."),
    ("Case Study: Harappa Threshing Floors. Analyze faunal and floral residues.", "Circular platforms excavated north of the Harappa granaries show rings of brick-on-edge masonry. In the center, excavators recovered carbonized seeds of wheat and barley, along with straw fragments. This direct botanical evidence confirms the platforms functioned as dedicated community threshing floors.")
]:
    s3_mastery_eng.append({"type": "Case Study", "q": q, "sol": sol})

for q, sol in [
    ("केस स्टडी: विशाल अन्नागार की वास्तुकला। इसके डिजाइन और वेंटिलेशन का विश्लेषण करें।", "मोहनजोदड़ो का विशाल अन्नागार 45 x 15 मीटर के ईंटों के मंच पर बना था। इसके ऊपर लकड़ी के ढाँचे को थामने वाले 27 ब्लॉक थे। फर्श के नीचे संकीर्ण हवादार नालियां छोड़ी गई थीं। यह डिज़ाइन यह दर्शाता है कि हड़प्पा वासियों के पास अनाज के संरक्षण की अत्याधुनिक तकनीक थी।"),
    ("केस स्टडी: सरस्वती (घग्गर) का सूखना। चोलिस्तान मरुस्थल में नदियों के विस्थापन का विश्लेषण करें।", "बहावलपुर (पाकिस्तान) में शुष्क घग्गर मार्ग के पास 170 से अधिक बस्तियाँ खोजी गई हैं। भू-वैज्ञानिक परिवर्तनों से सतलुज नदी सिंधु में और यमुना गंगा में मिल गई। इससे सरस्वती जलविहीन हो गई और चोलिस्तान की समृद्ध कृषि अर्थव्यवस्था तबाह हो गई।"),
    ("केस स्टडी: हड़प्पा के गहाई (Threshing) के चबूतरे। पादप अवशेषों का विश्लेषण करें।", "हड़प्पा अन्नागार के उत्तर में मिले वृत्ताकार चबूतरों की बनावट विशेष खड़ी ईंटों की कतारों से की गई थी। इसके केंद्र से गेहूँ, जौ और भूसे के जले हुए अंश मिले हैं। यह वानस्पतिक साक्ष्य यह साबित करता है कि ये खलिहानों के फर्श थे।")
]:
    s3_mastery_hin.append({"type": "Case Study", "q": q, "sol": sol})

# Teach Concept (3)
for q, sol in [
    ("Teach the Concept: Public Food Security Reservoirs in Ancient Cities.", "Teach students how public granaries acted as state buffer stocks. Similar to modern systems like FCI in India, the Harappan administration stored grains during high-yield seasons to redistribute during droughts, keeping cities stable and preventing famine."),
    ("Teach the Concept: Environmental Determinism and Civilizational Collapse.", "Explain how climate desiccation limits human society. As summer monsoons weakened, the reduced rainfall and dry river beds ended the agricultural surplus. This demonstrates that without a stable agrarian base, complex urban structures inevitably dissolve."),
    ("Teach the Concept: The Mechanics of Winnowing and Threshing in Bronze Age.", "Explain to students the mechanical process: (1) threshing (beating grain stalks against hard brick platforms to free kernels) and (2) winnowing (tossing the mixture in the wind so that the light chaff blows away while heavy wheat grains fall down).")
]:
    s3_mastery_eng.append({"type": "Teach Concept", "q": q, "sol": sol})

for q, sol in [
    ("अवधारणा सिखाएं: प्राचीन शहरों में सार्वजनिक खाद्य सुरक्षा और बफर स्टॉक।", "छात्रों को समझाएं कि कैसे सार्वजनिक अन्नागार राज्य के बफर स्टॉक का काम करते थे। आधुनिक भारतीय खाद्य निगम (FCI) की तरह ही हड़प्पा प्रशासन आपातकाल और सूखे के लिए अनाज जमा रखता था, जो शहरी समाज को स्थायित्व देता था।"),
    ("अवधारणा सिखाएं: पर्यावरणीय नियतिवाद (Environmental Determinism) और सभ्यता का पतन।", "समझाएं कि कैसे जलवायु परिवर्तन मानव समाज की सीमाओं को निर्धारित करता है। जब ग्रीष्मकालीन मानसून कमजोर हुआ, तो कृषि अधिशेष समाप्त हो गया। यह सिद्ध करता है कि एक मजबूत कृषि आधार के बिना जटिल शहरी सभ्यताएं अंततः समाप्त हो जाती हैं।"),
    ("अवधारणा सिखाएं: कांस्य युग में गहाई (Threshing) और ओसाई (Winnowing) के तरीके।", "छात्रों को समझाएं: (1) गहाई (बालियों को ईंटों के चबूतरे पर पीटकर दाना अलग करना) और (2) ओसाई (हवा के झोंके में दाने और भूसे के मिश्रण को ऊपर से गिराना ताकि भूसा उड़ जाए और भारी अनाज नीचे बैठ जाए)।")
]:
    s3_mastery_hin.append({"type": "Teach Concept", "q": q, "sol": sol})


# Write outputs
def inject_mastery(filepath, s1, s2, s3, name):
    if not os.path.exists(filepath):
        print(f"Error: {name} file not found at {filepath}")
        return False
    
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    data["deepDive"]["sections"][0]["masteryZone"] = s1
    data["deepDive"]["sections"][1]["masteryZone"] = s2
    data["deepDive"]["sections"][2]["masteryZone"] = s3
    
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"{name} mastery injected successfully!")
    return True

v_eng = inject_mastery(ENG_PATH, s1_mastery_eng, s2_mastery_eng, s3_mastery_eng, "English")
v_hin = inject_mastery(HIN_PATH, s1_mastery_hin, s2_mastery_hin, s3_mastery_hin, "Hindi")

if v_eng and v_hin:
    print("Mastery questions injection complete for both languages!")
else:
    print("Injection failed. Check paths or errors above.")
