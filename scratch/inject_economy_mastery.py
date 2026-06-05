import json
import os

ENG_PATH = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\HarappanIndus-Valley-Civilisation\Economic-Aspects-of-Indus-Valley-Civilisation\content.json"
HIN_PATH = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\HarappanIndus-Valley-Civilisation\Economic-Aspects-of-Indus-Valley-Civilisation\hi\content.json"

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
# SECTION 1: AGRICULTURE AND ANIMAL HUSBANDRY
# =========================================================================
s1_mastery_eng = []
s1_mastery_hin = []

# MCQ (5)
for q, opts, ans, sol in [
    ("Which of the following Mature Harappan sites has yielded the most direct evidence of a ploughed field showing grid furrows?", ["Banawali", "Kalibangan", "Lothal", "Surkotada"], 1, "Kalibangan in Rajasthan has yielded a ploughed field with grid-patterned furrows."),
    ("Direct traces of Harappan canals used for irrigation have been discovered at which site?", ["Shortughai", "Lothal", "Kalibangan", "Mohenjo-daro"], 0, "Direct traces of canals are found at Shortughai in northern Afghanistan."),
    ("The terracotta model of a plough was discovered at which of the following sites?", ["Kalibangan", "Lothal", "Banawali", "Surkotada"], 2, "Terracotta models of ploughs have been recovered from Banawali (Haryana)."),
    ("The Greek term 'Sindon' refers to which crop cultivated by the Harappans?", ["Wheat", "Barley", "Mustard", "Cotton"], 3, "The Greeks called cotton 'Sindon', derived from 'Sindhu' (Indus)."),
    ("Bones of horses have been reported at which of the following Gujarat sites?", ["Surkotada", "Dholavira", "Lothal", "Rangpur"], 0, "Skeletal remains of a horse have been identified at Surkotada in Gujarat.")
]:
    s1_mastery_eng.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("निम्नलिखित में से किस हड़प्पा स्थल से ग्रिड पैटर्न में जुते हुए खेत के साक्ष्य मिले हैं?", ["बनावली", "कालीबंगन", "लोथल", "सुरकोटदा"], 1, "राजस्थान के कालीबंगन से ग्रिड पैटर्न में जुते हुए खेत के साक्ष्य मिले हैं।"),
    ("सिंचाई के लिए उपयोग की जाने वाली हड़प्पा कालीन नहरों के सीधे साक्ष्य किस स्थल पर खोजे गए हैं?", ["शोर्तुघई", "लोथल", "कालीबंगन", "मोहनजोदड़ो"], 0, "नहरों के सीधे अवशेष उत्तरी अफगानिस्तान के शोर्तुघई में मिले हैं।"),
    ("मिट्टी के हल (Terracotta plough) का मॉडल निम्नलिखित में से किस स्थल पर मिला था?", ["कालीबंगन", "लोथल", "बनावली", "सुरकोटदा"], 2, "मिट्टी के हल का मॉडल हरियाणा के बनावली से मिला था।"),
    ("यूनानी शब्द 'सिंडन' (Sindon) हड़प्पा सभ्यता द्वारा उगाई जाने वाली किस फसल को दर्शाता है?", ["गेहूँ", "जौ", "सरसों", "कपास"], 3, "यूनानी लोग कपास को 'सिंडन' कहते थे, जो 'सिंधु' (Sindhu) शब्द से बना है।"),
    ("घोड़े की हड्डियाँ गुजरात के निम्नलिखित में से किस स्थल से प्राप्त हुई हैं?", ["सुरकोटदा", "धोलावीरा", "लोथल", "रंगपुर"], 0, "घोड़े के कंकाल के अवशेष गुजरात के सुरकोटदा से मिले हैं।")
]:
    s1_mastery_hin.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# Multi-Correct MCQ (5)
for q, opts, ans, sol in [
    ("Which of the following crops were cultivated by the Harappans? (Select all that apply)", ["Wheat and Barley", "Peas and Mustard", "Sesame and Lentils", "Sugar cane"], [0, 1, 2], "Wheat, barley, peas, mustard, sesame, and lentils were cultivated. Sugar cane was not cultivated."),
    ("Select the animals domesticated by the Harappans: (Select all that apply)", ["Humped cattle", "Water buffalo", "Camels and Asses", "African elephants"], [0, 1, 2], "Humped cattle, buffaloes, camels, and asses were domesticated. They knew Indian elephants, not African ones."),
    ("Identify the water management structures used in Harappan agriculture: (Select all that apply)", ["Stone-cut reservoirs at Dholavira", "Gabarbands (dams) in Baluchistan", "Brick-lined public wells", "Iron sprinkler systems"], [0, 1, 2], "Reservoirs at Dholavira, Gabarbands in Baluchistan, and wells were used. Iron was unknown."),
    ("Which of the following sites in Gujarat have yielded evidence of rice cultivation? (Select all that apply)", ["Lothal", "Rangpur", "Surkotada", "Dholavira"], [0, 1], "Lothal and Rangpur have yielded rice husks embedded in pottery clay."),
    ("Which wild animals are represented in Harappan bone assemblages and seals? (Select all that apply)", ["Deer and Wild Boar", "Rhinoceros", "Elephant", "Leopard"], [0, 1, 2, 3], "Deer, boar, rhino, elephant, and leopard are all represented in Harappan art and bone remains.")
]:
    s1_mastery_eng.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("निम्नलिखित में से कौन सी फसलें हड़प्पा वासियों द्वारा उगाई जाती थीं? (सभी लागू विकल्प चुनें)", ["गेहूँ और जौ", "मटर और सरसों", "तिल और मसूर", "गन्ना"], [0, 1, 2], "गेहूँ, जौ, मटर, सरसों, तिल और मसूर की खेती की जाती थी। गन्ने की खेती के साक्ष्य नहीं हैं।"),
    ("हड़प्पा वासियों द्वारा पाले जाने वाले जानवरों का चयन करें: (सभी लागू विकल्प चुनें)", ["कूबड़ वाले बैल", "भैंस", "ऊंट और गधा", "अफ्रीकी हाथी"], [0, 1, 2], "कूबड़ वाले बैल, भैंस, ऊंट और गधे पाले जाते थे। वे भारतीय हाथियों से परिचित थे, अफ्रीकी नहीं।"),
    ("हड़प्पा कृषि में प्रयुक्त जल प्रबंधन संरचनाओं की पहचान करें: (सभी लागू विकल्प चुनें)", ["धोलावीरा के पत्थर-कट जलाशय", "बलूचिस्तान में गबरबंद (बांध)", "ईंटों से बने कुएं", "लोहे के स्प्रिंकलर"], [0, 1, 2], "धोलावीरा के जलाशय, बलूचिस्तान के गबरबंद और कुओं का उपयोग होता था। लोहे का ज्ञान नहीं था।"),
    ("गुजरात के निम्नलिखित में से किन स्थलों से धान (चावल) की खेती के साक्ष्य मिले हैं? (सभी लागू विकल्प चुनें)", ["लोथल", "रंगपुर", "सुरकोटदा", "धोलावीरा"], [0, 1], "लोथल और रंगपुर से बर्तनों की मिट्टी में धान की भूसी मिली है।"),
    ("हड़प्पा स्थलों की हड्डियों और मुहरों में किन जंगली जानवरों का अंकन/अवशेष मिलता है? (सभी लागू विकल्प चुनें)", ["हिरण और जंगली सूअर", "गैंडा", "हाथी", "तेंदुआ"], [0, 1, 2, 3], "हिरण, सूअर, गैंडा, हाथी और तेंदुए सभी के साक्ष्य हड़प्पा कला और अवशेषों में मिलते हैं।")
]:
    s1_mastery_hin.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# True/False (8)
for q, ans, sol in [
    ("The Harappans were the first in the world to cultivate cotton.", True, "True. Cotton traces are found at Mohenjo-daro, dating back to 3000 BCE."),
    ("Canal irrigation was widespread throughout the alluvial plains of Sindh.", False, "False. Traces of canals are absent in the main Indus plain; only found at Shortughai."),
    ("A double-ploughed agricultural field has been excavated at Kalibangan.", True, "True. The field features two sets of furrows at right angles to each other."),
    ("Humped cattle (zebu) were highly revered and frequently depicted on seals.", True, "True. The humped bull is one of the most majestic motifs on Harappan seals."),
    ("The Harappans used heavy iron ploughshares to till the black soil.", False, "False. Iron was unknown to the Harappans; they likely used wooden ploughs."),
    ("Rice was the primary staple crop in all northern Harappan cities.", False, "False. Wheat and barley were the main staples; rice was rare and localized in Gujarat."),
    ("Surkotada has yielded controversial skeletal remains of horses.", True, "True. Surkotada yielded horse bones, though horse representations are absent on seals."),
    ("The stone dams called Gabarbands are located in the plains of Punjab.", False, "False. They are found in the hilly tracts of Baluchistan.")
]:
    s1_mastery_eng.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("हड़प्पा वासी विश्व में सबसे पहले कपास उगाने वाले लोग थे।", True, "सत्य। मोहनजोदड़ो से सूती कपड़े के अवशेष मिले हैं जो लगभग 3000 ईसा पूर्व के हैं।"),
    ("सिंध के जलोढ़ मैदानों में नहर सिंचाई प्रणाली का व्यापक प्रसार था।", False, "असत्य। मुख्य सिंधु घाटी में नहरों के अवशेष नहीं मिले हैं; केवल शोर्तुघई में मिले हैं।"),
    ("कालीबंगन से दोहरे जुते हुए खेत के साक्ष्य मिले हैं।", True, "सत्य। यह खेत ग्रिड पैटर्न में समकोण पर काटती हल-रेखाओं को दर्शाता है।"),
    ("कूबड़ वाले बैल (Zebu) का अत्यधिक महत्व था और मुहरों पर इनका अक्सर अंकन मिलता था।", True, "सत्य। कूबड़ वाला बैल हड़प्पा मुहरों पर बने प्रमुख सुंदर रूपांकनों में से एक है।"),
    ("हड़प्पा वासी काली मिट्टी जोतने के लिए लोहे के भारी हलों का प्रयोग करते थे।", False, "असत्य। हड़प्पा वासियों को लोहे का ज्ञान नहीं था; वे लकड़ी के हल का प्रयोग करते थे।"),
    ("उत्तरी हड़प्पा शहरों में चावल मुख्य भोजन था।", False, "असत्य। गेहूँ और जौ मुख्य भोजन थे; चावल गुजरात में स्थानीय स्तर पर उगाया जाता था।"),
    ("सुरकोटदा से घोड़े के विवादास्पद अस्थि अवशेष मिले हैं।", True, "सत्य। सुरकोटदा से घोड़े की हड्डियाँ मिली हैं, यद्यपि मुहरों पर इनका अंकन नहीं है।"),
    ("गबरबंद नामक पत्थर के बांध पंजाब के मैदानी भागों में स्थित हैं।", False, "असत्य। ये बांध बलूचिस्तान के पहाड़ी इलाकों में पाए जाते हैं।")
]:
    s1_mastery_hin.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

# Fill Blanks (8)
for q, ans, sol in [
    ("The ploughed field excavated at Kalibangan belongs to the ___________ Harappan phase.", "Early", "The ploughed field belongs to the Early Harappan/Pre-Mature phase of Kalibangan."),
    ("Terracotta models of ploughs have been discovered at ___________ in Haryana.", "Banawali", "Banawali has yielded terracotta plough models."),
    ("The Greek term for cotton is ___________, derived from the word Sindhu.", "sindon", "Greeks called cotton 'sindon' due to its Indus Valley origins."),
    ("Direct canal irrigation traces are found at ___________ in northern Afghanistan.", "Shortughai", "Shortughai has clear traces of canal systems."),
    ("Stone dams built across streams to check water run-off in Baluchistan are called ___________.", "gabarbands", "They are known as gabarbands."),
    ("Massive stone-cut reservoirs to store rainwater are characteristic of ___________.", "Dholavira", "Dholavira is famous for its reservoirs."),
    ("The most commonly depicted animal on Harappan seals is the ___________.", "unicorn", "The unicorn is the most frequent motif on seals."),
    ("Bones of horses have been identified at the site of ___________ in Gujarat.", "Surkotada", "Surkotada has yielded horse bones.")
]:
    s1_mastery_eng.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("कालीबंगन में खोजा गया जुता हुआ खेत ___________ हड़प्पा काल का है।", "प्रारंभिक", "जुता हुआ खेत कालीबंगन के प्रारंभिक हड़प्पा स्तर से संबंधित है।"),
    ("हरियाणा के ___________ नामक स्थल से मिट्टी के हल का मॉडल मिला है।", "बनावली", "बनावली से मिट्टी का हल मिला है।"),
    ("कपास के लिए यूनानी शब्द ___________ है, जो सिंधु शब्द से बना है।", "सिंडन", "यूनानी लोग कपास को सिंडन कहते थे।"),
    ("उत्तरी अफगानिस्तान में नहर सिंचाई के साक्ष्य ___________ से मिले हैं।", "शोर्तुघई", "शोर्तुघई में नहरों के साक्ष्य पाए गए हैं।"),
    ("बलूचिस्तान में पानी रोकने के लिए बनाए गए पत्थरों के बांधों को ___________ कहा जाता है।", "गबरबंद", "इन्हें गबरबंद कहा जाता है।"),
    ("वर्षा जल संचयन के लिए विशाल प्रस्तर जलाशयों का निर्माण ___________ में किया गया था।", "धोलावीरा", "धोलावीरा जलाशयों के लिए प्रसिद्ध है।"),
    ("हड़प्पा की मुहरों पर सबसे अधिक अंकन वाला पशु ___________ है।", "एक सींग वाला", "एक सींग वाला जानवर (unicorn) मुहरों पर सर्वाधिक मिलता है।"),
    ("घोड़े की हड्डियों के अवशेष गुजरात के ___________ नामक स्थल से मिले हैं।", "सुरकोटदा", "सुरकोटदा से घोड़े की हड्डियां प्राप्त हुई हैं।")
]:
    s1_mastery_hin.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

# Matchings (3)
s1_mastery_eng.extend([
    {
        "type": "Match the Following",
        "q": "Match the agricultural evidence with the sites where they were excavated:",
        "items": [{"left": "I. Ploughed Field Grid", "key": "A"}, {"left": "II. Terracotta Plough Model", "key": "B"}, {"left": "III. Stone Water Reservoirs", "key": "C"}],
        "options": [{"val": "A", "text": "A. Kalibangan (Rajasthan)"}, {"val": "B", "text": "B. Banawali (Haryana)"}, {"val": "C", "text": "C. Dholavira (Gujarat)"}],
        "sol": "Ploughed field is at Kalibangan; plough model at Banawali; reservoirs at Dholavira."
    },
    {
        "type": "Match the Following",
        "q": "Match the animals with their archaeological characteristics in Harappan sites:",
        "items": [{"left": "I. Unicorn", "key": "A"}, {"left": "II. Horse", "key": "B"}, {"left": "III. Humped Bull", "key": "C"}],
        "options": [{"val": "A", "text": "A. Most frequent motif on seals, likely mythological"}, {"val": "B", "text": "B. Bones found at Surkotada, absent on seal iconography"}, {"val": "C", "text": "C. Heavily revered, depicted with realistic fatty humps"}],
        "sol": "Unicorn is most common; horse bones at Surkotada (no seals); humped bull is revered."
    },
    {
        "type": "Match the Following",
        "q": "Match the crops with their socio-economic context:",
        "items": [{"left": "I. Rice", "key": "A"}, {"left": "II. Cotton", "key": "B"}, {"left": "III. Wheat/Barley", "key": "C"}],
        "options": [{"val": "A", "text": "A. Rare, husks found in Gujarat (Lothal, Rangpur)"}, {"val": "B", "text": "B. Known as Sindon, exported to Mesopotamians"}, {"val": "C", "text": "C. Primary staple crops grown in alluvial plains"}],
        "sol": "Rice husks are at Lothal/Rangpur; Cotton is Sindon; Wheat/Barley are main staples."
    }
])

s1_mastery_hin.extend([
    {
        "type": "Match the Following",
        "q": "कृषि साक्ष्यों को उनके संबंधित स्थलों से सुमेलित करें:",
        "items": [{"left": "I. जुते हुए खेत का ग्रिड", "key": "A"}, {"left": "II. मिट्टी के हल का मॉडल", "key": "B"}, {"left": "III. पत्थर के जलाशय", "key": "C"}],
        "options": [{"val": "A", "text": "A. कालीबंगन (राजस्थान)"}, {"val": "B", "text": "B. बनावली (हरियाणा)"}, {"val": "C", "text": "C. धोलावीरा (गुजरात)"}],
        "sol": "जुता हुआ खेत कालीबंगन में; हल का मॉडल बनावली में; जलाशय धोलावीरा में हैं।"
    },
    {
        "type": "Match the Following",
        "q": "जानवरों को उनके पुरातात्विक संदर्भों से सुमेलित करें:",
        "items": [{"left": "I. एक सींग वाला पशु (Unicorn)", "key": "A"}, {"left": "II. घोड़ा", "key": "B"}, {"left": "III. कूबड़ वाला बैल", "key": "C"}],
        "options": [{"val": "A", "text": "A. मुहरों पर सबसे अधिक रूपांकन, शायद काल्पनिक"}, {"val": "B", "text": "B. सुरकोटदा से हड्डियाँ मिलीं, मुहरों पर अंकन नहीं"}, {"val": "C", "text": "C. अत्यधिक श्रद्धेय, कूबड़ के साथ सजीव चित्रण"}],
        "sol": "एक सींग वाला सर्वाधिक सामान्य है; घोड़े की हड्डियाँ सुरकोटदा में मिलीं; कूबड़ वाले बैल का सजीव चित्रण है।"
    },
    {
        "type": "Match the Following",
        "q": "फसलों को उनके आर्थिक संदर्भ से सुमेलित करें:",
        "items": [{"left": "I. धान (चावल)", "key": "A"}, {"left": "II. कपास", "key": "B"}, {"left": "III. गेहूँ/जौ", "key": "C"}],
        "options": [{"val": "A", "text": "A. दुर्लभ, गुजरात के लोथल और रंगपुर से भूसी मिली"}, {"val": "B", "text": "B. 'सिंडन' नाम से प्रसिद्ध, पश्चिम में निर्यातित"}, {"val": "C", "text": "C. मैदानी भागों में उगाई जाने वाली प्राथमिक फसलें"}],
        "sol": "चावल लोथल/रंगपुर में; कपास सिंडन है; गेहूँ/जौ मुख्य खाद्य फसलें हैं।"
    }
])

# One-Liner (8)
for q, sol in [
    ("Which site provides evidence of a ploughed agricultural field?", "Kalibangan."),
    ("Name the site that yielded a terracotta model of a plough in Haryana.", "Banawali."),
    ("What was the Greek name for cotton derived from the Indus River?", "Sindon."),
    ("Which site in northern Afghanistan has traces of canals?", "Shortughai."),
    ("What are the stone-walled check dams in Baluchistan called?", "Gabarbands."),
    ("Where are the stone rainwater reservoirs of the Harappans located?", "Dholavira."),
    ("Which metal was completely absent from Harappan agrarian tools?", "Iron."),
    ("Where in Gujarat were horse bones found?", "Surkotada.")
]:
    s1_mastery_eng.append({"type": "One-Liner", "q": q, "sol": sol})

for q, sol in [
    ("किस हड़प्पा स्थल से जुते हुए कृषि खेत के साक्ष्य मिले हैं?", "कालीबंगन।"),
    ("हरियाणा के उस स्थल का नाम बताइए जहाँ मिट्टी के हल का मॉडल मिला था।", "बनावली।"),
    ("सिंधु नदी से व्युत्पन्न कपास का यूनानी नाम क्या था?", "सिंडन।"),
    ("उत्तरी अफगानिस्तान के किस स्थल पर नहरों के साक्ष्य मिले हैं?", "शोर्तुघई।"),
    ("बलूचिस्तान में ढलान वाले पानी को रोकने वाले पत्थर के बांधों को क्या कहा जाता है?", "गबरबंद।"),
    ("हड़प्पा वासियों के वर्षा जल संचयन के जलाशय कहाँ स्थित हैं?", "धोलावीरा।"),
    ("हड़प्पा के कृषि उपकरणों में किस धातु का पूर्ण अभाव था?", "लोहा।"),
    ("गुजरात में घोड़े की हड्डियाँ कहाँ पाई गईं?", "सुरकोटदा।")
]:
    s1_mastery_hin.append({"type": "One-Liner", "q": q, "sol": sol})

# Assertion-Reason (8)
for q, ans, sol in [
    ("Assertion (A): Double-cropping was practiced by the Harappans at Kalibangan.\nReason (R): The ploughed field at Kalibangan features grid furrows intersecting at right angles.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Canal irrigation was not heavily practiced within the alluvial plains of Sindh.\nReason (R): The plains relied on seasonal floodwater inundation and irrigation from wells.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): The Harappans exported cotton textiles to Mesopotamia.\nReason (R): Cotton fragments are found at Mohenjo-daro and Greeks called cotton 'Sindon'.", 1, "Both A and R are true but R is NOT the correct explanation of A. The export is proved by Mesopotamian text entries and sealings."),
    ("Assertion (A): The horse was the primary draft animal used to pull Harappan bullock carts.\nReason (R): Horse representations are completely absent from Harappan seals and pottery.", 3, "A is false but R is true. Bullock carts were pulled by humped bulls/oxen."),
    ("Assertion (A): Water management was highly sophisticated at Dholavira.\nReason (R): Dholavira is located in a semi-arid zone that lacks perennial rivers, necessitating rain harvesting.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Humped bulls were revered animals in Harappan society.\nReason (R): The humped bull is frequently depicted on seals with realistic anatomical details.", 0, "Both A and R are true and R explains the artistic evidence of reverence."),
    ("Assertion (A): Harappans did not use iron ploughshares for tilling.\nReason (R): Iron technology was only introduced in India during the Later Vedic period.", 0, "Both A and R are true and R explains the absence of iron."),
    ("Assertion (A): Rice husks are found embedded in pottery clay at Lothal.\nReason (R): Wheat and barley could not be grown anywhere in the Gujarat region.", 2, "A is true but R is false. Wheat and barley were grown in Gujarat, though rice was a localized crop.")
]:
    s1_mastery_eng.append({"type": "Assertion-Reason", "q": q, "opts": ar_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("कथन (A): कालीबंगन में हड़प्पा वासियों द्वारा दोहरी फसल उगाई जाती थी।\nकारण (R): कालीबंगन के जुते हुए खेत में हल-रेखाएं एक-दूसरे को समकोण पर काटती हैं।", 0, "A और R दोनों सही हैं और R, A की सही व्याख्या करता है।"),
    ("कथन (A): सिंध के जलोढ़ मैदानों में नहर सिंचाई का सघन विकास नहीं हुआ था।\nकारण (R): मैदानी भाग मौसमी बाढ़ के पानी और कुओं से सिंचाई पर निर्भर थे।", 0, "A और R दोनों सही हैं और R, A की सही व्याख्या करता है।"),
    ("कथन (A): हड़प्पा वासी मेसोपोटामिया को सूती वस्त्रों का निर्यात करते थे।\nकारण (R): मोहनजोदड़ो से सूती कपड़े के टुकड़े मिले हैं और यूनानी कपास को 'सिंडन' कहते थे।", 1, "A और R दोनों सही हैं लेकिन R, A की सही व्याख्या नहीं करता। निर्यात की पुष्टि मेसोपोटामिया के ग्रंथों से होती है।"),
    ("कथन (A): हड़प्पा की बैलगाड़ियों को खींचने के लिए मुख्य रूप से घोड़ों का उपयोग किया जाता था।\nकारण (R): हड़प्पा की मुहरों और बर्तनों पर घोड़े का अंकन पूरी तरह से अनुपस्थित है।", 3, "A गलत है लेकिन R सही है। गाड़ियाँ खींचने के लिए बैलों का प्रयोग होता था।"),
    ("कथन (A): धोलावीरा में जल प्रबंधन प्रणाली अत्यंत विकसित थी।\nकारण (R): धोलावीरा एक अर्ध-शुष्क क्षेत्र में स्थित है जहाँ बारहमासी नदियों का अभाव था, जिससे वर्षा जल संचयन आवश्यक था।", 0, "A और R दोनों सही हैं और R, A की सही व्याख्या करता है।"),
    ("कथन (A): हड़प्पा समाज में कूबड़ वाले बैल को एक पवित्र पशु माना जाता था।\nकारण (R): मुहरों पर कूबड़ वाले बैल का अंकन शारीरिक विवरणों के साथ अक्सर मिलता है।", 0, "A और R दोनों सही हैं और R, A की सही व्याख्या करता है।"),
    ("कथन (A): हड़प्पा वासियों ने जुताई के लिए लोहे के फाल का प्रयोग नहीं किया।\nकारण (R): भारत में लोहे की तकनीक केवल उत्तर वैदिक काल में शुरू हुई थी।", 0, "A और R दोनों सही हैं और R, A की सही व्याख्या करता है।"),
    ("कथन (A): लोथल में बर्तनों की मिट्टी में धान की भूसी धँसी हुई मिली है।\nकारण (R): गुजरात क्षेत्र में कहीं भी गेहूँ और जौ की खेती नहीं की जा सकती थी।", 2, "A सही है लेकिन R गलत है। गुजरात में गेहूँ और जौ भी उगाए जाते थे।")
]:
    s1_mastery_hin.append({"type": "Assertion-Reason", "q": q, "opts": hin_ar_opts, "ans": ans, "sol": sol})

# Statement-Based (5)
for q, ans, sol in [
    ("Consider the following statements:\nStatement 1: The earliest ploughed field was discovered at Banawali.\nStatement 2: Terracotta models of ploughs have been excavated at Kalibangan.\nWhich of the statements given above is/are correct?", 3, "Both statements are reversed. Ploughed field is at Kalibangan; terracotta models are at Banawali."),
    ("Consider the following statements:\nStatement 1: Direct traces of canals are found at Shortughai in northern Afghanistan.\nStatement 2: Shortughai was located in Gujarat near the Gulf of Khambhat.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect; Shortughai is in Afghanistan."),
    ("Consider the following statements:\nStatement 1: Skeletal remains of horse bones are reported from Surkotada.\nStatement 2: The horse is frequently depicted on Mature Harappan seals.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: the horse is never depicted on seals."),
    ("Consider the following statements:\nStatement 1: The Harappans were the first to cultivate cotton in the ancient world.\nStatement 2: Vegetable root dyes like madder were used for coloring textiles.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct."),
    ("Consider the following statements:\nStatement 1: Gabarbands were stone dams built to store seasonal agricultural water.\nStatement 2: Gabarbands are primarily found in the hilly regions of Baluchistan.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct.")
]:
    s1_mastery_eng.append({"type": "Statement-Based", "q": q, "opts": mcq_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: सबसे प्रारंभिक जुता हुआ खेत बनावली में खोजा गया था।\nकथन 2: मिट्टी के हल के मॉडल कालीबंगन से प्राप्त हुए हैं।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 3, "दोनों कथन विपरीत लिखे गए हैं। जुता हुआ खेत कालीबंगन में और हल का मॉडल बनावली में मिला था।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: नहरों के सीधे अवशेष उत्तरी अफगानिस्तान के शोर्तुघई से मिले हैं।\nकथन 2: शोर्तुघई गुजरात में खंभात की खाड़ी के पास स्थित था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि शोर्तुघई अफगानिस्तान में है।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: सुरकोटदा से घोड़े के कंकाल के अवशेष प्राप्त हुए हैं।\nकथन 2: परिपक्व हड़प्पा मुहरों पर घोड़े का अंकन अक्सर मिलता है।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि मुहरों पर घोड़े का अंकन कभी नहीं मिलता।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: प्राचीन विश्व में कपास उगाने वाले हड़प्पा वासी सबसे पहले लोग थे।\nकथन 2: कपड़ों को रंगने के लिए मजीठ जैसी वनस्पति जड़ों के रंगों का उपयोग किया जाता था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 2, "दोनों कथन सही हैं।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: गबरबंद मौसमी कृषि जल को संचित करने के लिए बने पत्थरों के बांध थे।\nकथन 2: गबरबंद मुख्य रूप से बलूचिस्तान के पहाड़ी इलाकों में पाए जाते हैं।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 2, "दोनों कथन सही हैं।")
]:
    s1_mastery_hin.append({"type": "Statement-Based", "q": q, "opts": hin_mcq_opts, "ans": ans, "sol": sol})

# Why (3)
for q, sol in [
    ("Why is the Kalibangan ploughed field highly significant for agricultural history?", "It shows grid furrows cutting at right angles, providing the earliest evidence of double-cropping (growing mustard and chickpea simultaneously) in antiquity."),
    ("Why did the Harappans establish reservoirs at Dholavira?", "Dholavira in the Rann of Kutch has a semi-arid climate with scarce perennial water sources. Massive stone reservoirs collected rainwater run-off to sustain the city and agriculture."),
    ("Why is the presence of the horse in the Indus Valley Civilisation controversial?", "Skeletal bones matching the horse are found at Surkotada, but horse representations are completely absent on seals and painted pottery. This suggests it was not integral to Harappan economy/culture.")
]:
    s1_mastery_eng.append({"type": "Why", "q": q, "sol": sol})

for q, sol in [
    ("कालीबंगन का जुता हुआ खेत कृषि इतिहास के लिए क्यों महत्वपूर्ण है?", "यह समकोण पर काटती हल-रेखाओं को दर्शाता है, जो प्राचीन काल में दोहरी फसल (एक साथ सरसों और चना उगाने) का सबसे पहला पुरातात्विक प्रमाण है।"),
    ("हड़प्पा वासियों ने धोलावीरा में जलाशयों का निर्माण क्यों किया?", "कच्छ के रन में स्थित धोलावीरा एक अर्ध-शुष्क क्षेत्र है जहाँ पानी की कमी थी। विशाल जलाशय वर्षा जल को संचित कर कृषि और नगर की जलापूर्ति सुनिश्चित करते थे।"),
    ("सिंधु घाटी सभ्यता में घोड़े की उपस्थिति विवादास्पद क्यों है?", "सुरकोटदा से घोड़े की हड्डियाँ तो मिली हैं, लेकिन मुहरों और बर्तनों पर इसका कोई चित्रण नहीं है। यह दर्शाता है कि घोड़ा हड़प्पा संस्कृति और अर्थव्यवस्था का हिस्सा नहीं था।")
]:
    s1_mastery_hin.append({"type": "Why", "q": q, "sol": sol})

# How (3)
for q, sol in [
    ("How did the Harappans practice agriculture without iron tools?", "They used wooden ploughshares (indicated by terracotta models) and harvested crops using stone blades (chert) mounted on curved wooden handles or bronze sickles."),
    ("How did the Gabarbands of Baluchistan benefit dryland agriculture?", "These stone check-dams slowed down seasonal stream water, letting silt settle to create fertile soil beds and retaining water table levels for crop cultivation."),
    ("How was the grid-furrow system in Kalibangan organized to crop twice?", "The furrows ran in two directions: one set spaced closely (approx. 30 cm) for smaller crops like chickpea, and another spaced wider (approx. 1.9 m) at right angles for taller mustard plants.")
]:
    s1_mastery_eng.append({"type": "How", "q": q, "sol": sol})

for q, sol in [
    ("लोहे के औजारों के बिना हड़प्पा वासी कृषि कैसे करते थे?", "वे लकड़ी के हल का प्रयोग करते थे (मिट्टी के हल इसके प्रमाण हैं) और फसल काटने के लिए लकड़ी के हत्थों में लगे पत्थर (chert) के फलकों या कांसे की हंसिया का उपयोग करते थे।"),
    ("बलूचिस्तान के गबरबंदों ने शुष्क कृषि में कैसे मदद की?", "ये पत्थर के बांध मौसमी नदी नालों के पानी को धीमा करते थे, जिससे गाद जमा होकर उपजाऊ मिट्टी बनती थी और खेतों में नमी बनी रहती थी।"),
    ("कालीबंगन में दोहरी फसल के लिए ग्रिड हल-रेखाओं को कैसे व्यवस्थित किया गया था?", "रेखाएँ दो दिशाओं में थीं: एक पास-पास (लगभग 30 सेमी) छोटी फसलों (जैसे चना) के लिए, और दूसरी समकोण पर दूर-दूर (लगभग 1.9 मीटर) लंबी सरसों की फसल के लिए।")
]:
    s1_mastery_hin.append({"type": "How", "q": q, "sol": sol})

# Case Study (3)
for q, sol in [
    ("Case Study: Water Scarcity and Harvesting at Dholavira. Explain its design.", "Dholavira is located on Khadir Bet island. The Harappans diverted water from two seasonal channels (Manhar and Mandsar) into a series of interconnected stone-cut reservoirs, utilizing bunds and stone masonry, creating a model for dryland urban survival."),
    ("Case Study: The Agrarian Implements of Banawali. Analyze the significance of terracotta models.", "In alluvial plains, organic wooden ploughs decay, leaving no direct trace. The recovery of baked clay models of ploughs at Banawali provided crucial proof of the shape and function of Harappan tillage tools."),
    ("Case Study: Horse Bones at Surkotada. Analyze the debates on horse domestication.", "Excavator J.P. Joshi identified horse bones in Late Mature levels. However, archaeozoologist Richard Meadow argues they might belong to the half-ass (onager) wild in Kutch. The lack of horse images on seals supports Meadow's view that the horse was not domesticated or central to IVC.")
]:
    s1_mastery_eng.append({"type": "Case Study", "q": q, "sol": sol})

for q, sol in [
    ("केस स्टडी: धोलावीरा में जल की कमी और संचयन। इसकी रूपरेखा स्पष्ट करें।", "धोलावीरा खदिर बेट द्वीप पर है। हड़प्पा वासियों ने मनहर और मनसर नामक मौसमी नालों के पानी को बांधों के माध्यम से पत्थर काट कर बनाए गए जलाशयों में मोड़ा, जो शुष्क क्षेत्रों में जल संरक्षण का एक बेजोड़ मॉडल है।"),
    ("केस स्टडी: बनावली के कृषि उपकरण। मिट्टी के मॉडलों के महत्व का विश्लेषण करें।", "जलोढ़ मैदानों में लकड़ी के हल गल जाते हैं, जिससे कोई निशान नहीं बचता। बनावली से पकी मिट्टी के हल के मॉडल मिलने से यह साबित हुआ कि हड़प्पा के हल का स्वरूप और कार्य प्रणाली क्या थी।"),
    ("केस स्टडी: सुरकोटदा में घोड़े की हड्डियाँ। घोड़े के पालतूकरण के विवादों का विश्लेषण करें।", "उत्खननकर्ता जे.पी. जोशी ने सुरकोटदा में घोड़े की हड्डियां खोजीं। हालांकि, रिचर्ड मीडो का तर्क है कि ये जंगली गधे (गोरखर) की हो सकती हैं। मुहरों पर घोड़े के चित्रों का न होना मीडो के मत का समर्थन करता है।")
]:
    s1_mastery_hin.append({"type": "Case Study", "q": q, "sol": sol})

# Teach Concept (3)
for q, sol in [
    ("Teach the Concept: Double-Cropping Systems of the Harappans.", "Explain how the Kalibangan grid furrow pattern allowed planting two crops (mustard and chickpea) together. The crops were placed so they didn't block each other's sunlight, maximizing output in dry, rain-fed zones."),
    ("Teach the Concept: SINDON - The Origin of Cotton Cultivation.", "Explain to students that cotton was first grown and spun by Harappans around 3000 BCE. When exported to the West, Greeks named it 'Sindon', directly preserving the memory of the 'Sindhu' (Indus) River where it originated."),
    ("Teach the Concept: Inundation vs. Canal Irrigation in the Indus Plains.", "Teach the difference between Shortughai (dry region with direct canals) and the main Indus plain (which flooded annually, leaving rich silt). In the main plains, natural floods and wells were preferred over canals to prevent waterlogging.")
]:
    s1_mastery_eng.append({"type": "Teach Concept", "q": q, "sol": sol})

for q, sol in [
    ("अवधारणा सिखाएं: हड़प्पा वासियों की दोहरी फसल प्रणाली (Double-Cropping)।", "समझाएं कि कैसे कालीबंगन में समकोण पर जुती हुई रेखाओं ने एक साथ सरसों और चना उगाने में मदद की। फसलों को इस तरह लगाया जाता था कि वे एक-दूसरे की धूप न रोकें, जिससे उत्पादन अधिकतम हो सके।"),
    ("अवधारणा सिखाएं: सिंडन (SINDON) - कपास की खेती का इतिहास।", "विद्यार्थियों को बताएं कि हड़प्पा वासियों ने 3000 ईसा पूर्व में कपास उगाने और सूत कातने की शुरुआत की थी। पश्चिम में निर्यात किए जाने पर यूनानियों ने इसे 'सिंडन' कहा, जो 'सिंधु' (Sindhu) नदी की याद दिलाता है।"),
    ("अवधारणा सिखाएं: सिंधु मैदानों में बाढ़ बनाम नहर सिंचाई।", "शोर्तुघई (शुष्क क्षेत्र जहाँ नहरें थीं) और मुख्य सिंधु मैदान (जहाँ हर साल बाढ़ आती थी) के बीच अंतर समझाएं। मैदानी इलाकों में नहरों के बजाय वार्षिक बाढ़ और कुओं को प्राथमिकता दी जाती थी।")
]:
    s1_mastery_hin.append({"type": "Teach Concept", "q": q, "sol": sol})


# =========================================================================
# SECTION 2: CRAFT PRODUCTION, METALLURGY, AND WEIGHT SYSTEMS
# =========================================================================
s2_mastery_eng = []
s2_mastery_hin = []

# MCQ (5)
for q, opts, ans, sol in [
    ("Which of the following sites had specialized factories for bead-making, complete with drills and kilns?", ["Chanhudaro and Lothal", "Balakot and Nageshwar", "Kalibangan and Harappa", "Banawali and Dholavira"], 0, "Chanhudaro and Lothal were major bead-making industrial hubs with excavated workshops."),
    ("Which of the following coastal sites specialized in manufacturing shell objects?", ["Balakot and Nageshwar", "Chanhudaro and Amri", "Kalibangan and Lothal", "Harappa and Mohenjo-daro"], 0, "Balakot and Nageshwar were coastal centers specializing in shell bangles, ladles, and inlay pieces."),
    ("What stone was primarily used to make the highly standardized Harappan cubical weights?", ["Steatite", "Chert", "Carnelian", "Faience"], 1, "Standard cubical weights were carved from chert, a fine-grained silica stone."),
    ("From which region did the Harappans procure copper to alloy with tin for bronze?", ["Oman and Rajasthan (Khetri)", "Afghanistan and Badakhshan", "Karnataka (Kolar)", "Mesopotamia"], 0, "Copper came from the Khetri mines of Rajasthan and was imported from Oman."),
    ("In the Harappan weight system, what was the approximate value of the standard unit weight (16th multiple)?", ["5.5 grams", "13.63 grams", "28.4 grams", "64.0 grams"], 1, "The key unit standard weight (binary unit 16) was equivalent to approximately 13.63 grams.")
]:
    s2_mastery_eng.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("निम्नलिखित में से किन स्थलों पर मनके बनाने के कारखाने मिले हैं, जहाँ से बर्मा (Drills) और भट्टियाँ भी मिली हैं?", ["चन्हुदड़ो और लोथल", "बालाकोट और नागेश्वर", "कालीबंगन और हड़प्पा", "बनावली और धोलावीरा"], 0, "चन्हुदड़ो और लोथल मनके बनाने के प्रमुख कारखाने वाले स्थल थे।"),
    ("शंख (Shell) की वस्तुएं बनाने में महारत रखने वाले तटीय विशिष्ट स्थल कौन से थे?", ["बालाकोट और नागेश्वर", "चन्हुदड़ो और आमरी", "कालीबंगन और लोथल", "हड़प्पा और मोहनजोदड़ो"], 0, "बालाकोट और नागेश्वर शंख की चूड़ियाँ और पच्चीकारी के काम के तटीय केंद्र थे।"),
    ("मानकीकृत हड़प्पा घनाकार बाट बनाने के लिए मुख्यतः किस पत्थर का उपयोग किया जाता था?", ["सेलखड़ी (Steatite)", "चर्ट (Chert)", "अकीक (Carnelian)", "फेयॉन्स (Faience)"], 1, "मानक बाटों का निर्माण चर्ट नामक महीन पत्थर से किया जाता था।"),
    ("कांसा बनाने के लिए तांबा हड़प्पा वासियों को किस क्षेत्र से प्राप्त होता था?", ["ओमान और राजस्थान (खेत्री)", "अफगानिस्तान और बदख्शां", "कर्नाटक (कोलार)", "मेसोपोटामिया"], 0, "तांबा राजस्थान की खेत्री खदानों और ओमान से प्राप्त होता था।"),
    ("हड़प्पा की भार प्रणाली में मुख्य मानक बाट (16वीं इकाई) का वजन लगभग कितना था?", ["5.5 ग्राम", "13.63 ग्राम", "28.4 ग्राम", "64.0 ग्राम"], 1, "16वीं इकाई के रूप में प्रयुक्त होने वाला मानक बाट लगभग 13.63 ग्राम का था।")
]:
    s2_mastery_hin.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# Multi-Correct MCQ (5)
for q, opts, ans, sol in [
    ("Select the coastal specialized shell-working hubs of the Harappans: (Select all that apply)", ["Nageshwar", "Balakot", "Chanhudaro", "Surkotada"], [0, 1], "Nageshwar and Balakot are coastal sites specializing in shell objects."),
    ("Which of the following materials were utilized to manufacture Harappan weights? (Select all that apply)", ["Chert", "Alabaster / Agate", "Jasper", "Iron"], [0, 1, 2], "Chert, alabaster, agate, and jasper were used. Iron was unknown."),
    ("Identify the metals alloyed by Harappan smiths to produce bronze objects: (Select all that apply)", ["Copper", "Tin", "Lead", "Zinc"], [0, 1, 2], "Copper, tin, and sometimes lead were alloyed to make bronze. Zinc was not alloyed."),
    ("Which sites have yielded standardized measuring scales? (Select all that apply)", ["Mohenjo-daro (Ivory scale)", "Lothal (Shell scale)", "Harappa (Bronze scale)", "Kalibangan (Iron scale)"], [0, 1, 2], "Mohenjo-daro, Lothal, and Harappa have yielded scales of ivory, shell, and bronze respectively. No iron existed."),
    ("Select correct statements about bead-making processes: (Select all that apply)", ["Carnelian was heated to obtain its red color", "Nodules were chipped to form rough shapes", "Drilling was done with specialized bronze/stone drills", "Beads were cast in iron molds"], [0, 1, 2], "Bead-making involved heating carnelian, chipping, and drilling. No iron molds existed.")
]:
    s2_mastery_eng.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("हड़प्पा सभ्यता के तटीय शंख-उद्योग केंद्रों का चयन करें: (सभी लागू विकल्प चुनें)", ["नागेश्वर", "बालाकोट", "चन्हुदड़ो", "सुरकोटदा"], [0, 1], "नागेश्वर और बालाकोट तटीय शंख-उद्योग के प्रमुख केंद्र थे।"),
    ("हड़प्पा के बाट बनाने के लिए निम्नलिखित में से किस सामग्री का उपयोग किया जाता था? (सभी लागू विकल्प चुनें)", ["चर्ट (Chert)", "एलाबस्टर / अकीक", "जैस्पर", "लोहा"], [0, 1, 2], "बाट चर्ट, एलाबस्टर, अकीक और जैस्पर से बनते थे। लोहे का प्रयोग नहीं होता था।"),
    ("कांसे की वस्तुएं बनाने के लिए हड़प्पा के कारीगर किन धातुओं को मिलाते थे? (सभी लागू विकल्प चुनें)", ["तांबा", "टिन", "शीशा (Lead)", "जस्ता (Zinc)"], [0, 1, 2], "तांबा, टिन और कुछ मात्रा में शीशा मिलाकर कांसा तैयार किया जाता था।"),
    ("किन स्थलों से मानकीकृत मापक पैमाने प्राप्त हुए हैं? (सभी लागू विकल्प चुनें)", ["मोहनजोदड़ो (हाथीदांत पैमाना)", "लोथल (शंख पैमाना)", "हड़प्पा (कांसे का पैमाना)", "कालीबंगन (लोहे का पैमाना)"], [0, 1, 2], "मोहनजोदड़ो, लोथल और हड़प्पा से क्रमशः हाथीदांत, शंख और कांसे के पैमाने मिले हैं।"),
    ("मनके बनाने की प्रक्रिया के बारे में सही कथनों का चयन करें: (सभी लागू विकल्प चुनें)", ["अकीक (carnelian) को गर्म करके लाल रंग दिया जाता था", "पत्थरों को तोड़कर खुरदरा आकार दिया जाता था", "छेद करने के लिए विशिष्ट बर्मा का प्रयोग होता था", "मनकों को लोहे के सांचे में ढाला जाता था"], [0, 1, 2], "मनके बनाने में गर्म करना, तराशना और छेद करना शामिल था। लोहे का उपयोग नहीं होता था।")
]:
    s2_mastery_hin.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# True/False (8)
for q, ans, sol in [
    ("Iron drills were used for perforating hard stones like carnelian.", False, "False. Iron was unknown. They used specialized bronze or stone (chert) drills."),
    ("Chert weights were cubical and generally lacked markings of denominations.", True, "True. They were polished, cubical blocks without numbers or symbols."),
    ("Tin was imported from Afghanistan and Iran to alloy copper into bronze.", True, "True. Tin was scarce locally and was imported from the Northwest."),
    ("The shell scale for linear measurement was discovered at Mohenjo-daro.", False, "False. The shell scale was found at Lothal; Mohenjo-daro yielded an ivory scale."),
    ("Copper was procured from Khetri mines of Rajasthan and also from Oman.", True, "True. Rajasthan and Oman were the two primary copper sources."),
    ("The Harappan weight system followed a purely binary scale for all values.", False, "False. Lower values were binary (up to 64), but higher values were decimal (160, 200, 320, etc.)."),
    ("Chanhudaro was a major specialized craft town in Sindh.", True, "True. Chanhudaro was dedicated almost entirely to bead, shell, and seal craft production."),
    ("The standard unit weight of the binary system was equivalent to 13.63g.", True, "True. The 16th multiple weight (approx 13.63g) was the primary standard.")
]:
    s2_mastery_eng.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("कठिन पत्थरों में छेद करने के लिए लोहे के बर्मा (drills) का प्रयोग किया जाता था।", False, "असत्य। लोहे का ज्ञान नहीं था; वे कांसे या चर्ट के विशिष्ट बर्मा का प्रयोग करते थे।"),
    ("चर्ट बाट घनाकार होते थे और उन पर आमतौर पर कोई संख्या अंकित नहीं होती थी।", True, "सत्य। बाटों पर कोई अंक नहीं खुदे होते थे, वे केवल चिकने घनाकार पत्थर थे।"),
    ("कांसा बनाने के लिए तांबे में मिलाने हेतु टिन का आयात अफगानिस्तान और ईरान से किया जाता था।", True, "सत्य। टिन की उपलब्धता कम थी और इसे उत्तर-पश्चिम से आयात किया जाता था।"),
    ("रैखिक माप का शंख पैमाना मोहनजोदड़ो से खोजा गया था।", False, "असत्य। शंख पैमाना लोथल से मिला था; मोहनजोदड़ो से हाथीदांत का पैमाना मिला था।"),
    ("तांबा राजस्थान की खेत्री खदानों और ओमान से प्राप्त किया जाता था।", True, "सत्य। राजस्थान और ओमान तांबे के दो मुख्य स्रोत थे।"),
    ("हड़प्पा की बाट प्रणाली सभी मूल्यों के लिए विशुद्ध रूप से द्वि-आधारी (binary) थी।", False, "असत्य। छोटे बाटों के लिए द्वि-आधारी (64 तक) और बड़े बाटों के लिए दशमलव प्रणाली थी।"),
    ("चन्हुदड़ो सिंध में एक प्रमुख विशिष्ट शिल्प नगर था।", True, "सत्य। चन्हुदड़ो लगभग पूरी तरह से मनके, शंख और मुहर बनाने के कार्यों में संलग्न था।"),
    ("द्वि-आधारी प्रणाली के मानक बाट का मूल्य 13.63 ग्राम के बराबर था।", True, "सत्य। 16वीं इकाई का बाट (लगभग 13.63 ग्राम) मुख्य मानक बाट था।")
]:
    s2_mastery_hin.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

# Fill Blanks (8)
for q, ans, sol in [
    ("The stone primarily used to make standardized Harappan weights was ___________.", "chert", "Standard cubical weights were made of chert."),
    ("Coastal centers like Nageshwar and Balakot specialized in the manufacture of ___________ items.", "shell", "They specialized in shell bangles, ladles, and inlay pieces."),
    ("Bead-making factories with drills and kilns were excavated at Lothal and ___________.", "Chanhudaro", "Lothal and Chanhudaro are the two premier bead hubs."),
    ("Copper was alloyed with ___________ to produce bronze.", "tin", "Copper + tin yields bronze."),
    ("An ivory scale showing standardized linear units was discovered at ___________.", "Mohenjo-daro", "The ivory scale was found at Mohenjo-daro."),
    ("For lower values, the weight system followed a ___________ scale.", "binary", "Lower weights followed the binary scale (1, 2, 4, 8, 16, 32, 64)."),
    ("For higher values, the weight system transitioned into a ___________ scale.", "decimal", "Higher weights followed the decimal scale (160, 200, 320, 640...)."),
    ("Chemical analyses show that Harappan copper matched the nickel impurities of copper from ___________.", "Oman", "The nickel traces match copper from Oman (Makan).")
]:
    s2_mastery_eng.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("मानकीकृत हड़प्पा बाट बनाने के लिए मुख्यतः ___________ पत्थर का उपयोग किया जाता था।", "चर्ट", "बाट बनाने के लिए चर्ट (Chert) का उपयोग होता था।"),
    ("नागेश्वर और बालाकोट जैसे तटीय स्थल ___________ की वस्तुएं बनाने में माहिर थे।", "शंख", "ये स्थल शंख की चूड़ियाँ व पच्चीकारी के काम के केंद्र थे।"),
    ("मनके बनाने के कारखाने लोथल और ___________ से प्राप्त हुए हैं।", "चन्हुदड़ो", "लोथल और चन्हुदड़ो से कारखाने मिले हैं।"),
    ("कांसा बनाने के लिए तांबे में ___________ धातु मिलाई जाती थी।", "टिन", "तांबे और टिन को मिलाकर कांसा बनाया जाता था।"),
    ("हाथीदांत का मानकीकृत पैमाना ___________ से प्राप्त हुआ था।", "मोहनजोदड़ो", "मोहनजोदड़ो से हाथीदांत का पैमाना मिला था।"),
    ("छोटे भारों के लिए बाट प्रणाली ___________ प्रणाली का पालन करती थी।", "द्वि-आधारी", "छोटे बाट द्वि-आधारी (binary) अनुपात में थे।"),
    ("बड़े भारों के लिए बाट प्रणाली ___________ प्रणाली में बदल जाती थी।", "दशमलव", "बड़े बाट दशमलव (decimal) गुणांकों में थे।"),
    ("रासायनिक विश्लेषण से सिद्ध होता है कि हड़प्पा का तांबा ___________ के तांबे के निकल अंश से मेल खाता है।", "ओमान", "हड़प्पा तांबे में निकल के निशान ओमान (माकन) के तांबे से मिलते हैं।")
]:
    s2_mastery_hin.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

# Matchings (3)
s2_mastery_eng.extend([
    {
        "type": "Match the Following",
        "q": "Match the materials used in craft production with their typical products:",
        "items": [{"left": "I. Chert", "key": "A"}, {"left": "II. Steatite", "key": "B"}, {"left": "III. Shell", "key": "C"}],
        "options": [{"val": "A", "text": "A. Cubical weights and drill bits"}, {"val": "B", "text": "B. Microscopic beads and seals"}, {"val": "C", "text": "C. Bangles, ladles, and decorative inlay work"}],
        "sol": "Chert is for weights; steatite for micro beads/seals; shell for bangles/inlay."
    },
    {
        "type": "Match the Following",
        "q": "Match the measuring scales with the materials and sites where they were found:",
        "items": [{"left": "I. Ivory Scale", "key": "A"}, {"left": "II. Shell Scale", "key": "B"}, {"left": "III. Bronze Scale", "key": "C"}],
        "options": [{"val": "A", "text": "A. Mohenjo-daro scale"}, {"val": "B", "text": "B. Lothal scale"}, {"val": "C", "text": "C. Harappa scale"}],
        "sol": "Ivory scale at Mohenjo-daro; shell scale at Lothal; bronze scale at Harappa."
    },
    {
        "type": "Match the Following",
        "q": "Match the metal inputs and outputs with their sources/sites:",
        "items": [{"left": "I. Copper Source", "key": "A"}, {"left": "II. Tin Source", "key": "B"}, {"left": "III. Bronze Casting Site", "key": "C"}],
        "options": [{"val": "A", "text": "A. Khetri mines (Rajasthan) & Oman"}, {"val": "B", "text": "B. Afghanistan & Central Asia"}, {"val": "C", "text": "C. Mohenjo-daro (Dancing Girl)"}],
        "sol": "Copper came from Khetri/Oman; tin from Afghanistan; bronze casting at Mohenjo-daro."
    }
])

s2_mastery_hin.extend([
    {
        "type": "Match the Following",
        "q": "शिल्प कला में प्रयुक्त सामग्रियों को उनके संबंधित उत्पादों से सुमेलित करें:",
        "items": [{"left": "I. चर्ट (Chert)", "key": "A"}, {"left": "II. सेलखड़ी (Steatite)", "key": "B"}, {"left": "III. शंख (Shell)", "key": "C"}],
        "options": [{"val": "A", "text": "A. घनाकार बाट और बर्मा के फलक"}, {"val": "B", "text": "B. अति-सूक्ष्म मनके और मुहरें"}, {"val": "C", "text": "C. चूड़ियाँ, करछुल और पच्चीकारी का सामान"}],
        "sol": "चर्ट बाटों के लिए है; सेलखड़ी मनकों के लिए; शंख चूड़ियों के लिए है।"
    },
    {
        "type": "Match the Following",
        "q": "मापक पैमानों को उनके निर्माण सामग्री और खोजे गए स्थलों से सुमेलित करें:",
        "items": [{"left": "I. हाथीदांत का पैमाना", "key": "A"}, {"left": "II. शंख का पैमाना", "key": "B"}, {"left": "III. कांसे का पैमाना", "key": "C"}],
        "options": [{"val": "A", "text": "A. मोहनजोदड़ो से प्राप्त"}, {"val": "B", "text": "B. लोथल से प्राप्त"}, {"val": "C", "text": "C. हड़प्पा से प्राप्त"}],
        "sol": "हाथीदांत पैमाना मोहनजोदड़ो में; शंख पैमाना लोथल में; कांस्य पैमाना हड़प्पा में है।"
    },
    {
        "type": "Match the Following",
        "q": "धातु इनपुट और स्थलों को उनके स्रोतों से सुमेलित करें:",
        "items": [{"left": "I. तांबे का स्रोत", "key": "A"}, {"left": "II. टिन का स्रोत", "key": "B"}, {"left": "III. कांस्य ढलाई स्थल", "key": "C"}],
        "options": [{"val": "A", "text": "A. खेत्री खदानें (राजस्थान) और ओमान"}, {"val": "B", "text": "B. अफगानिस्तान और मध्य एशिया"}, {"val": "C", "text": "C. मोहनजोदड़ो (नर्तकी की मूर्ति)"}],
        "sol": "तांबा खेत्री/ओमान से; टिन अफगानिस्तान से; कांस्य ढलाई मोहनजोदड़ो में हुई।"
    }
])

# One-Liner (8)
for q, sol in [
    ("What rock was standard for making weights?", "Chert."),
    ("Name the premier craft site in Sindh.", "Chanhudaro."),
    ("Which metal was completely absent from Harappan metallurgical repertoire?", "Iron."),
    ("Where was the ivory linear measurement scale found?", "Mohenjo-daro."),
    ("Where was the shell linear measurement scale found?", "Lothal."),
    ("From which country did the Harappans import tin?", "Afghanistan (and Iran)."),
    ("What is the weight in grams of the key standard weight unit?", "13.63 grams."),
    ("Name one coastal site specializing in shell crafts.", "Nageshwar (or Balakot).")
]:
    s2_mastery_eng.append({"type": "One-Liner", "q": q, "sol": sol})

for q, sol in [
    ("बाट बनाने के लिए किस पत्थर का उपयोग होता था?", "चर्ट।"),
    ("सिंध में स्थित प्रमुख शिल्प केंद्र का नाम बताइए।", "चन्हुदड़ो।"),
    ("हड़प्पा धातु विज्ञान में किस धातु का पूर्ण अभाव था?", "लोहा।"),
    ("हाथीदांत का बना हुआ मापक पैमाना कहाँ पाया गया था?", "मोहनजोदड़ो।"),
    ("शंख का बना हुआ मापक पैमाना कहाँ पाया गया था?", "लोथल।"),
    ("हड़प्पा वासी टिन का आयात किस देश से करते थे?", "अफगानिस्तान (और ईरान)।"),
    ("मुख्य मानक बाट इकाई का भार ग्राम में कितना था?", "13.63 ग्राम।"),
    ("शंख उद्योग में विशिष्टता रखने वाले एक तटीय स्थल का नाम बताइए।", "नागेश्वर (या बालाकोट)।")
]:
    s2_mastery_hin.append({"type": "One-Liner", "q": q, "sol": sol})

# Assertion-Reason (8)
for q, ans, sol in [
    ("Assertion (A): Chert was the preferred material for making Harappan weights.\nReason (R): Chert is a dense, hard stone resistant to chipping and chemical weathering, ensuring weight accuracy.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Iron drills were used by Chanhudaro artisans to drill tiny holes in carnelian beads.\nReason (R): Iron was completely unknown to the people of the Indus Valley Civilisation.", 3, "A is false but R is true. They used bronze or chert drills."),
    ("Assertion (A): Tin was imported from Afghanistan and Iran to make bronze.\nReason (R): Tin deposits are extremely scarce in the alluvial plains of the Indus River.", 0, "Both A and R are true and R explains why tin had to be imported from the Northwest."),
    ("Assertion (A): Chanhudaro was a specialized industrial town of the Harappans.\nReason (R): A bead-making factory, bead drills, and shell workshops were excavated there.", 0, "Both A and R are true and R explains why it is called a specialized craft town."),
    ("Assertion (A): Nageshwar was a coastal shell-working center.\nReason (R): Coastal areas provided easy access to marine mollusk shells, the raw material for shell objects.", 0, "Both A and R are true and R explains the location choice."),
    ("Assertion (A): The Harappan weight system shows a remarkable unity across thousands of kilometers.\nReason (R): Cubical chert weights of identical binary-decimal ratios are found in Harappa, Mohenjo-daro, and Lothal.", 0, "Both A and R are true and R provides the physical evidence for the unity."),
    ("Assertion (A): The Harappans imported copper from Oman.\nReason (R): Chemical tests show that both Omani copper and Harappan copper contain trace amounts of nickel, proving a common source.", 0, "Both A and R are true and R is the scientific proof of the import."),
    ("Assertion (A): Bronze was widely used to make heavy structural girders in Harappan houses.\nReason (R): Tin was a scarce import, so bronze was reserved for tools, weapons, and artistic figurines.", 3, "A is false but R is true. Girders were made of wood/bricks, not bronze.")
]:
    s2_mastery_eng.append({"type": "Assertion-Reason", "q": q, "opts": ar_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("कथन (A): हड़प्पा के बाटों के निर्माण के लिए चर्ट एक पसंदीदा पत्थर था।\nकारण (R): चर्ट एक कठोर पत्थर है जिसमें टूट-फूट और घिसावट कम होती है, जो बाट की सटीकता बनाए रखता था।", 0, "A और R दोनों सही हैं और R, A की सही व्याख्या करता है।"),
    ("कथन (A): चन्हुदड़ो के कारीगर मनकों में बारीक छेद करने के लिए लोहे के बर्मा (drills) का प्रयोग करते थे।\nकारण (R): सिंधु घाटी सभ्यता के लोगों को लोहे का कोई ज्ञान नहीं था।", 3, "A गलत है लेकिन R सही है। वे कांसे या पत्थर के बर्मा का प्रयोग करते थे।"),
    ("कथन (A): कांसा बनाने के लिए टिन को अफगानिस्तान और ईरान से आयात किया जाता था।\nकारण (R): सिंधु नदी के मैदानी इलाकों में टिन के प्राकृतिक भंडार अत्यंत दुर्लभ हैं।", 0, "A और R दोनों सही हैं और R, A की सही व्याख्या करता है।"),
    ("कथन (A): चन्हुदड़ो हड़प्पा सभ्यता का एक औद्योगिक नगर था।\nकारण (R): चन्हुदड़ो से मनके बनाने का कारखाना, बर्मा और शंख उद्योग के साक्ष्य मिले हैं।", 0, "A और R दोनों सही हैं और R, A की सही व्याख्या करता है।"),
    ("कथन (A): नागेश्वर शंख उद्योग का एक प्रमुख तटीय केंद्र था।\nकारण (R): तटीय क्षेत्रों में समुद्री शंख प्रचुर मात्रा में उपलब्ध थे जो शंख की वस्तुओं के लिए कच्चा माल थे।", 0, "A और R दोनों सही हैं और R, A की सही व्याख्या करता है।"),
    ("कथन (A): हड़प्पा की बाट प्रणाली में हजारों किलोमीटर की दूरी के बाद भी एकरूपता थी।\nकारण (R): हड़प्पा, मोहनजोदड़ो और लोथल से एक समान द्वि-आधारी-दशमलव अनुपात के बाट मिले हैं।", 0, "A और R दोनों सही हैं और R, A की सही व्याख्या करता है।"),
    ("कथन (A): हड़प्पा वासी ओमान से तांबे का आयात करते थे।\nकारण (R): रासायनिक विश्लेषण से सिद्ध हुआ है कि हड़प्पा और ओमान दोनों के तांबे में निकल के निशान हैं।", 0, "A और R दोनों सही हैं और R, A की सही व्याख्या करता है।"),
    ("कथन (A): हड़प्पा घरों में भारी संरचनात्मक शहतीर (Girders) बनाने के लिए कांसे का उपयोग होता था।\nकारण (R): टिन एक दुर्लभ आयात था, इसलिए कांसे को औजारों, हथियारों और कलाकृतियों तक सीमित रखा गया।", 3, "A गलत है लेकिन R सही है। घर लकड़ी और ईंटों से बनते थे।")
]:
    s2_mastery_hin.append({"type": "Assertion-Reason", "q": q, "opts": hin_ar_opts, "ans": ans, "sol": sol})

# Statement-Based (5)
for q, ans, sol in [
    ("Consider the following statements:\nStatement 1: Cubical weights of the Harappans were made of soft steatite.\nStatement 2: All weights were clearly marked with their values in numerals.\nWhich of the statements given above is/are correct?", 3, "Both statements are incorrect: weights were made of chert and were completely unmarked."),
    ("Consider the following statements:\nStatement 1: An ivory scale was discovered at Mohenjo-daro.\nStatement 2: A shell scale was found at Lothal.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct."),
    ("Consider the following statements:\nStatement 1: Copper was obtained from the Khetri mines of Rajasthan.\nStatement 2: Tin was obtained from Southern India.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: tin came from Afghanistan/Iran."),
    ("Consider the following statements:\nStatement 1: Bead factories have been excavated at Chanhudaro and Lothal.\nStatement 2: Harappan beads were strictly made of metals like gold and silver.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: beads were made of carnelian, jasper, steatite, shell, etc."),
    ("Consider the following statements:\nStatement 1: The lower denominations of weights followed a binary system (1, 2, 4, 8, 16, 32, 64).\nStatement 2: The higher denominations transitioned into a decimal system.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct.")
]:
    s2_mastery_eng.append({"type": "Statement-Based", "q": q, "opts": mcq_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: हड़प्पा के घनाकार बाट मुलायम सेलखड़ी पत्थर से बनते थे।\nकथन 2: सभी बाटों पर उनकी तौल का मूल्य स्पष्ट रूप से खुदा होता था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 3, "दोनों कथन गलत हैं: बाट चर्ट पत्थर से बनते थे और उन पर कोई मूल्य अंकित नहीं था।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: मोहनजोदड़ो से हाथीदांत का पैमाना मिला था।\nकथन 2: लोथल से शंख का पैमाना मिला था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 2, "दोनों कथन सही हैं।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: तांबा राजस्थान की खेत्री खदानों से प्राप्त होता था।\nकथन 2: टिन दक्षिण भारत से प्राप्त होता था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि टिन अफगानिस्तान/ईरान से आता था।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: चन्हुदड़ो और लोथल से मनके बनाने के कारखाने मिले हैं।\nकथन 2: हड़प्पा के मनके केवल सोने और चांदी जैसी धातुओं से ही बनते थे।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि मनके अकीक, जैस्पर, सेलखड़ी आदि से भी बनते थे।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: बाटों की छोटी श्रेणियां द्वि-आधारी प्रणाली (1, 2, 4, 8, 16, 32, 64) का पालन करती थीं।\nकथन 2: बड़ी श्रेणियां दशमलव प्रणाली का पालन करती थीं।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 2, "दोनों कथन सही हैं।")
]:
    s2_mastery_hin.append({"type": "Statement-Based", "q": q, "opts": hin_mcq_opts, "ans": ans, "sol": sol})

# Why (3)
for q, sol in [
    ("Why was chert preferred over other stones for crafting Harappan weights?", "Chert is a very hard cryptocrystalline quartz. It is highly resistant to abrasion, chipping, and weathering, ensuring that the weights maintained their standardized masses over long periods of usage."),
    ("Why did the Harappan smiths alloy copper with tin to make bronze?", "Pure copper is relatively soft and dulls quickly when used for cutting. Alloying copper with 10-12% tin creates bronze, which is much harder, allows for a sharper cutting edge on tools, and flows better during casting."),
    ("Why did coastal Balakot and Nageshwar specialize in shell-craft instead of bead-making?", "These sites are located on the Arabian Sea coast, rich in marine shell beds. Proximity to raw materials made it economically efficient to specialize in shell processing and export finished shell goods inland.")
]:
    s2_mastery_eng.append({"type": "Why", "q": q, "sol": sol})

for q, sol in [
    ("हड़प्पा के बाट बनाने के लिए अन्य पत्थरों की तुलना में चर्ट को क्यों प्राथमिकता दी गई?", "चर्ट अत्यंत कठोर पत्थर होता है। इसमें घिसावट, दरारें और क्षरण नगण्य होता है, जिससे बाटों का वजन लंबे समय तक उपयोग के बाद भी बिल्कुल सटीक बना रहता था।"),
    ("हड़प्पा के धातुकारों ने तांबे में टिन मिलाकर कांसा क्यों बनाया?", "शुद्ध तांबा अपेक्षाकृत नरम होता है और काम करने पर इसके औजार जल्दी मुड़ जाते हैं। तांबे में टिन मिलाने से धातु कठोर हो जाती है, जिससे औजारों की धार तेज और टिकाऊ बनती है।"),
    ("नागेश्वर और बालाकोट जैसे तटीय स्थलों ने मनके बनाने के बजाय शंख उद्योग में विशिष्टता क्यों हासिल की?", "ये स्थल अरब सागर के तट पर स्थित थे जहाँ समुद्री शंख प्रचुर मात्रा में उपलब्ध थे। कच्चे माल की निकटता के कारण शंख उद्योग का विकास यहाँ अधिक व्यावहारिक था।")
]:
    s2_mastery_hin.append({"type": "Why", "q": q, "sol": sol})

# How (3)
for q, sol in [
    ("How were etched carnelian beads manufactured by Harappan craftsmen?", "Raw chalcedony was heated in kilns to turn it red (converting iron to hematite). It was chipped into shape, drilled with specialized drills, etched with an alkaline paste of washing soda, and fired again to fix the white design."),
    ("How did the weight system transition mathematically from low to high denominations?", "It began with a binary scale doubling from 1 to 64. At the 16th multiple (~13.63g), it bridged into a decimal system, with higher weights being multiples like 160, 200, 320, 640, 1600, etc., up to 10,800 units."),
    ("How did scientists prove the import of Omani copper into the Indus Valley?", "Through chemical composition analysis (mass spectrometry). Both Indus copper artifacts and Omani copper ore show distinct trace levels of nickel impurities, separating them from other regional copper ores.")
]:
    s2_mastery_eng.append({"type": "How", "q": q, "sol": sol})

for q, sol in [
    ("हड़प्पा कारीगरों द्वारा नक्काशीदार लाल अकीक (etched carnelian) के मनके कैसे बनाए जाते थे?", "अकीक के पत्थरों को भट्टी में गर्म कर लाल रंग दिया जाता था। फिर इन्हें तराशकर बर्मा से छेद किया जाता था और सोडा के घोल से सफेद चित्रकारी करके पुनः पकाया जाता था।"),
    ("बाटों की माप प्रणाली गणितीय रूप से छोटी से बड़ी इकाइयों में कैसे बदलती थी?", "यह 1 से 64 तक द्वि-आधारी (binary) रूप से दोगुनी होती थी। 16वीं इकाई (लगभग 13.63 ग्राम) से यह दशमलव प्रणाली में परिवर्तित होकर 160, 200, 320, 640 आदि के गुणांकों में बदल जाती थी।"),
    ("वैज्ञानिकों ने सिंधु घाटी में ओमानी तांबे के आयात को कैसे प्रमाणित किया?", "रासायनिक विश्लेषण द्वारा। सिंधु घाटी से मिले तांबे के औजारों और ओमान के तांबे के अयस्क दोनों में निकल (Nickel) के समान रासायनिक अंश मिले हैं, जो उनके एक ही स्रोत का होने का प्रमाण है।")
]:
    s2_mastery_hin.append({"type": "How", "q": q, "sol": sol})

# Case Study (3)
for q, sol in [
    ("Case Study: Chanhudaro Craft Workshop. Describe its industrial nature.", "Chanhudaro was a tiny site (under 5 hectares) but was almost entirely devoted to craft production. Excavations revealed bead-making tools, unfinished beads, shell fragments, and seal-cutting workshops, proving it was a dedicated industrial town."),
    ("Case Study: Lothal Shell Industry. Discuss the division of labor.", "Lothal had a specialized shell workshop near the residential sectors. Raw turbinella pyrum shells were cut into bangles, and waste flakes were recycled into inlay pieces, showing structured recycling and resource efficiency."),
    ("Case Study: Weight Uniformity Across the Civilisation. Discuss its administrative implications.", "Despite covering over 1 million square kilometers, weights at Harappa, Mohenjo-daro, and Chanhu-daro conform to the exact same standard. This implies a powerful central regulatory authority enforcing commerce laws.")
]:
    s2_mastery_eng.append({"type": "Case Study", "q": q, "sol": sol})

for q, sol in [
    ("केस स्टडी: चन्हुदड़ो शिल्प कार्यशाला। इसकी औद्योगिक प्रकृति का वर्णन करें।", "चन्हुदड़ो एक छोटा स्थल था (5 हेक्टेयर से कम) लेकिन यह पूरी तरह से शिल्प उत्पादन को समर्पित था। यहाँ से मनके बनाने के उपकरण, अधबने मनके, शंख के टुकड़े और मुहर बनाने की कार्यशालाएं मिली हैं।"),
    ("केस स्टडी: लोथल का शंख उद्योग। श्रम विभाजन और अपशिष्ट प्रबंधन पर चर्चा करें।", "लोथल में आवासीय क्षेत्र के पास शंख कार्यशाला थी। शंखों को काटकर चूड़ियाँ बनाई जाती थीं और बचे हुए टुकड़ों से पच्चीकारी का सामान बनाया जाता था, जो कुशल कारीगरी को दर्शाता है।"),
    ("केस स्टडी: सभ्यता में भार की एकरूपता। इसके प्रशासनिक निहितार्थों पर चर्चा करें।", "10 लाख वर्ग किलोमीटर से अधिक क्षेत्र में फैले होने के बावजूद हड़प्पा, मोहनजोदड़ो और लोथल के बाटों का वजन बिल्कुल समान था। यह एक शक्तिशाली प्रशासनिक नियंत्रण की ओर इशारा करता है।")
]:
    s2_mastery_hin.append({"type": "Case Study", "q": q, "sol": sol})

# Teach Concept (3)
for q, sol in [
    ("Teach the Concept: Bronze Smelting and Alloying Ratios in IVC.", "Teach how copper was melted and tin was added to create bronze. Highlight that the tin content in Harappan bronze tools was strictly regulated (often around 8-12%) to optimize hardness without making the metal too brittle."),
    ("Teach the Concept: The Binary-Decimal Weight System.", "Explain the mathematics of the weight system. Show how 1, 2, 4, 8, 16, 32, 64 is binary (doubling), and explain why transitioning to a decimal system (multiples of 10) was necessary for weighing large bulk merchandise."),
    ("Teach the Concept: Linear Measurement Standardization.", "Teach how the ivory scale from Mohenjo-daro features divisions equal to 1.704 mm, the smallest division recorded in the Bronze Age. Explain how this precision was used in town planning and brick manufacturing.")
]:
    s2_mastery_eng.append({"type": "Teach Concept", "q": q, "sol": sol})

for q, sol in [
    ("अवधारणा सिखाएं: सिंधु घाटी में कांस्य निर्माण और धातु अनुपात।", "समझाएं कि कैसे तांबे को पिघलाकर उसमें टिन मिलाकर कांसा बनाया जाता था। रेखांकित करें कि कांसे में टिन का अनुपात (8-12%) नियंत्रित रखा जाता था ताकि औजार अधिक कठोर बनें और टूटे नहीं।"),
    ("अवधारणा सिखाएं: द्वि-आधारी-दशमलव भार प्रणाली (Binary-Decimal System)।", "भार प्रणाली के गणित को समझाएं। दिखाएं कि कैसे 1, 2, 4, 8, 16, 32, 64 द्वि-आधारी है, और बड़े सामानों को तौलने के लिए दशमलव प्रणाली (10 के गुणांकों) में बदलाव क्यों आवश्यक था।"),
    ("अवधारणा सिखाएं: रैखिक माप का मानकीकरण।", "समझाएं कि मोहनजोदड़ो से मिले हाथीदांत के पैमाने पर न्यूनतम विभाजन 1.704 मिमी है, जो कांस्य युग का सबसे छोटा मापक विभाजन है। यह यथार्थता नगर नियोजन और ईंट निर्माण में सहायक थी।")
]:
    s2_mastery_hin.append({"type": "Teach Concept", "q": q, "sol": sol})


# =========================================================================
# SECTION 3: TRADE NETWORKS, TRANSPORT, AND MARITIME COMMUNICATIONS
# =========================================================================
s3_mastery_eng = []
s3_mastery_hin = []

# MCQ (5)
for q, opts, ans, sol in [
    ("Which of the following is the Mesopotamian name for the Indus Valley region found in Akkadian cuneiform inscriptions?", ["Dilmun", "Makan", "Meluhha", "Sumer"], 2, "Mesopotamian inscriptions refer to the Indus region as Meluhha."),
    ("Dilmun, a key transit port in the Persian Gulf mentioned in cuneiform texts, is identified with which modern region?", ["Oman", "Bahrain", "Kuwait", "Iran"], 1, "Dilmun is identified with modern Bahrain in the Persian Gulf."),
    ("Which Harappan site features a massive baked-brick rectangular basin identified as a tidal dockyard?", ["Lothal", "Sutkagendor", "Balakot", "Dholavira"], 0, "Lothal features a massive tidal dockyard built of fired bricks."),
    ("Who was the famous Akkadian ruler whose cuneiform inscriptions record ships of Meluhha docking at his port?", ["Sargon of Akkad", "Hammurabi", "Gilgamesh", "Ashurbanipal"], 0, "Sargon of Akkad (c. 2350 BCE) recorded that ships of Meluhha, Makan, and Dilmun docked at Akkad."),
    ("Which fortified Harappan trade post on the Makran coast near the Iran border monitored maritime traffic?", ["Sutkagendor", "Sotka Koh", "Balakot", "Lothal"], 0, "Sutkagendor was the westernmost fortified trading post on the Makran coast.")
]:
    s3_mastery_eng.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("मेसोपोटामिया के अक्कड़ अभिलेखों में सिंधु घाटी क्षेत्र के लिए किस नाम का उपयोग किया गया है?", ["दिलमुन", "माकन", "मेलुहा", "सुमेर"], 2, "मेसोपोटामिया के अभिलेखों में सिंधु क्षेत्र को मेलुहा (Meluhha) कहा गया है।"),
    ("फारस की खाड़ी में स्थित प्रमुख व्यापारिक बंदरगाह 'दिलमुन' (Dilmun) की पहचान किस आधुनिक क्षेत्र से की जाती है?", ["ओमान", "बहरीन", "कुवैत", "ईरान"], 1, "दिलमुन की पहचान फारस की खाड़ी के आधुनिक बहरीन द्वीप से की जाती है।"),
    ("किस हड़प्पा स्थल पर पकी ईंटों से बना एक विशाल आयताकार ढांचा मिला है जिसे गोदीवाड़ा (Dockyard) माना गया है?", ["लोथल", "सुत्कागेंदोर", "बालाकोट", "धोलावीरा"], 0, "लोथल से पकी ईंटों का बना एक ज्वारीय गोदीवाड़ा प्राप्त हुआ है।"),
    ("मेसोपोटामिया के उस प्रसिद्ध शासक का नाम क्या है जिसके अभिलेखों में मेलुहा के जहाजों के लंगर डालने का उल्लेख है?", ["सारगोन (Sargon of Akkad)", "हम्मुराबी", "गिलगामेश", "अशुरबनिपाल"], 0, "अक्कड़ के शासक सारगोन (लगभग 2350 ईसा पूर्व) के लेखों में मेलुहा के जहाजों का उल्लेख है।"),
    ("मकरान तट पर ईरान सीमा के पास स्थित कौन सा हड़प्पा दुर्ग समुद्री व्यापार की निगरानी करने वाली व्यापारिक चौकी था?", ["सुत्कागेंदोर", "सोत्का कोह", "बालाकोट", "लोथल"], 0, "सुत्कागेंदोर मकरान तट पर स्थित सबसे पश्चिमी हड़प्पा व्यापारिक चौकी थी।")
]:
    s3_mastery_hin.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# Multi-Correct MCQ (5)
for q, opts, ans, sol in [
    ("Select the three lands mentioned in Akkadian trade records: (Select all that apply)", ["Meluhha", "Dilmun", "Makan", "Egypt"], [0, 1, 2], "Meluhha, Dilmun, and Makan are the three trade lands mentioned. Egypt was not mentioned in this context."),
    ("Which of the following commodities were exported from Meluhha to Mesopotamia? (Select all that apply)", ["Carnelian beads", "Lapis Lazuli", "Ivory products", "Gold and Copper"], [0, 1, 2, 3], "All of these (carnelian, lapis, ivory, gold, copper, wood) were exports from Meluhha."),
    ("Identify the structural components of the Lothal dockyard: (Select all that apply)", ["Kiln-burnt brick walls", "Sluice/lock-gate spillway", "Inlet canal from the Bhogavo River", "Iron anchoring posts"], [0, 1, 2], "Kiln brick walls, lock-gate spillway, and inlet canal are parts of the dockyard. No iron existed."),
    ("Select correct statements about Harappan trade transport: (Select all that apply)", ["Land transport used solid-wheeled wooden bullock carts", "River trade was carried out in flat-bottomed boats", "Maritime trade used masted wooden ships", "Horse-drawn chariots were the primary commercial transport"], [0, 1, 2], "Land transport relied on bullock carts, and river/sea on boats. No horse-drawn chariots existed."),
    ("Which of the following raw materials were obtained from external locations? (Select all that apply)", ["Lapis Lazuli from Badakhshan (Shortughai)", "Copper from Oman", "Tin from Afghanistan", "Gold from Karnataka"], [0, 1, 2, 3], "All these pairs correctly represent raw material sources for the Harappan economy.")
]:
    s3_mastery_eng.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("मेसोपोटामिया के व्यापारिक लेखों में उल्लिखित तीन देशों का चयन करें: (सभी लागू विकल्प चुनें)", ["मेलुहा", "दिलमुन", "माकन", "मिस्र"], [0, 1, 2], "मेलुहा, दिलमुन और माकन तीन व्यापारिक देश थे जिनका उल्लेख मिलता है।"),
    ("मेलुहा से मेसोपोटामिया को कौन सी वस्तुएं निर्यात की जाती थीं? (सभी लागू विकल्प चुनें)", ["अकीक (Carnelian) के मनके", "लाजवर्त (Lapis Lazuli)", "हाथीदांत की वस्तुएं", "सोना और तांबा"], [0, 1, 2, 3], "ये सभी (अकीक, लाजवर्त, हाथीदांत, सोना, तांबा) मेलुहा से निर्यात होते थे।"),
    ("लोथल के गोदीवाड़ा (Dockyard) के संरचनात्मक घटकों की पहचान करें: (सभी लागू विकल्प चुनें)", ["पकी ईंटों की दीवारें", "लकड़ी के लॉक-गेट वाला स्पिलवे", "भोगावो नदी से जुड़ी प्रवेश नहर", "लोहे के लंगर खंभे"], [0, 1, 2], "पकी ईंटें, लॉक-गेट स्पिलवे और फीडर नहर गोदीवाड़ा के हिस्से थे। लोहे का अस्तित्व नहीं था।"),
    ("हड़प्पा व्यापार परिवहन के बारे में सही कथनों का चयन करें: (सभी लागू विकल्प चुनें)", ["स्थल परिवहन में ठोस पहियों वाली लकड़ी की बैलगाड़ियाँ प्रयुक्त होती थीं", "नदी व्यापार चपटे तल वाली नावों से होता था", "समुद्री व्यापार पाल वाले लकड़ी के जहाजों से होता था", "घोड़े वाले रथ वाणिज्यिक परिवहन का मुख्य साधन थे"], [0, 1, 2], "गाड़ियाँ बैलों द्वारा और नावें/जहाज जल परिवहन के साधन थे। घोड़े वाले रथ नहीं थे।"),
    ("निम्नलिखित में से कौन से कच्चे माल बाहरी स्थानों से प्राप्त किए जाते थे? (सभी लागू विकल्प चुनें)", ["बदख्शां (शोर्तुघई) से लाजवर्त", "ओमान से तांबा", "अफगानिस्तान से टिन", "कर्नाटक से सोना"], [0, 1, 2, 3], "ये सभी कच्चे माल के स्रोत हड़प्पा अर्थव्यवस्था के अंतर्गत बिल्कुल सही हैं।")
]:
    s3_mastery_hin.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# True/False (8)
for q, ans, sol in [
    ("Mesopotamian cuneiform texts describe Meluhha as a land of peacocks.", True, "True. The texts mention the 'Haja-bird' of Meluhha, identified as the peacock."),
    ("Standard silver coins were used to settle import balances with Mesopotamia.", False, "False. No coins existed; trade was settled via barter of goods."),
    ("Dilmun (Bahrain) served as a major commercial transit point in the Persian Gulf.", True, "True. Dilmun was a transit center linking Akkad to Meluhha."),
    ("Sutkagendor, the westernmost trade post, was located in inland Punjab.", False, "False. Sutkagendor was located on the Makran coast near Iran."),
    ("Clay sealings were pressed onto cargo bags to ensure they arrived untampered.", True, "True. The sealing served as a tamper-evident security seal."),
    ("Sargon of Akkad boasted that ships from Sumer docked at Meluhha's ports.", False, "False. He recorded that ships of Meluhha docked at the port of Akkad."),
    ("An overland trade route linked the lapis lazuli outpost of Shortughai to the Indus plain.", True, "True. Shortughai traded with the Indus plains via land routes through Afghanistan."),
    ("The Lothal dockyard was constructed using unburnt, sun-dried mud bricks.", False, "False. It was built using high-quality kiln-burnt bricks to resist water erosion.")
]:
    s3_mastery_eng.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("मेसोपोटामिया के ग्रंथों में मेलुहा को मोरों (peacocks) का देश कहा गया है।", True, "सत्य। ग्रंथों में मेलुहा के 'हाजा-पक्षी' का उल्लेख है जिसकी पहचान मोर से की गई है।"),
    ("मेसोपोटामिया के साथ व्यापारिक भुगतान के लिए चांदी के सिक्कों का उपयोग होता था।", False, "असत्य। कोई सिक्के नहीं थे; व्यापार वस्तु विनिमय पर आधारित था।"),
    ("दिलमुन (बहरीन) फारस की खाड़ी में एक प्रमुख व्यापारिक पारगमन (transit) केंद्र था।", True, "सत्य। दिलमुन मेसोपोटामिया और सिंधु क्षेत्र को जोड़ने वाला पारगमन बंदरगाह था।"),
    ("सबसे पश्चिमी व्यापारिक चौकी सुत्कागेंदोर पंजाब के आंतरिक भाग में स्थित थी।", False, "असत्य। सुत्कागेंदोर ईरान सीमा के पास मकरान तट पर स्थित था।"),
    ("सामान के बोरों पर गीली मिट्टी लगाकर मुहर दबाई जाती थी ताकि सामान सुरक्षित रहे।", True, "सत्य। यह सील पैकेट से छेड़छाड़ रोकने के लिए सुरक्षा टैग का काम करती थी।"),
    ("अक्कड़ के सारगोन ने दावा किया था कि सुमेर के जहाज मेलुहा के बंदरगाह पर आते थे।", False, "असत्य। उसने लिखा था कि मेलुहा के जहाज उसके राजधानी शहर अक्कड़ में लंगर डालते थे।"),
    ("लाजवर्त की व्यापारिक चौकी शोर्तुघई थल मार्ग द्वारा सिंधु मैदानों से जुड़ी हुई थी।", True, "सत्य। शोर्तुघई से थल मार्ग द्वारा लाजवर्त सिंधु घाटी भेजा जाता था।"),
    ("लोथल के गोदीवाड़ा का निर्माण धूप में सुखाई गई कच्ची ईंटों से किया गया था।", False, "असत्य। पानी के कटाव को रोकने के लिए इसका निर्माण पक्की ईंटों (kiln-burnt bricks) से किया गया था।")
]:
    s3_mastery_hin.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

# Fill Blanks (8)
for q, ans, sol in [
    ("In Mesopotamian cuneiform records, the Indus Valley region is named ___________.", "Meluhha", "Cuneiform texts refer to the Indus region as Meluhha."),
    ("The copper-producing region of Oman is referred to in texts as ___________.", "Makan", "Oman is referred to as Makan/Magan."),
    ("The famous brick-lined Harappan tidal dockyard was built at ___________.", "Lothal", "Lothal is the site of the dockyard."),
    ("The Mesopotamian king who recorded Meluhhan trade was ___________.", "Sargon", "Sargon of Akkad recorded Meluhha shipping."),
    ("A circular Persian Gulf button seal was excavated at the site of ___________.", "Lothal", "Lothal yielded the Persian Gulf seal."),
    ("The westernmost fortified trading outpost of the Harappans was ___________.", "Sutkagendor", "Sutkagendor is the westernmost site."),
    ("Merchant packages were verified for security using clay impressions called ___________.", "sealings", "The impressions are called sealings."),
    ("Land cargo was transported using wooden carts with ___________ wheels.", "solid", "Carts had solid, hubless wooden wheels (not spoked).")
]:
    s3_mastery_eng.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("मेसोपोटामिया के अभिलेखों में सिंधु घाटी क्षेत्र को ___________ कहा गया है।", "मेलुहा", "सिंधु घाटी को मेलुहा कहा गया है।"),
    ("तांबा उत्पादक ओमान क्षेत्र को मेसोपोटामिया के ग्रंथों में ___________ कहा गया है।", "माकन", "ओमान को माकन/मगान कहा गया है।"),
    ("पकी ईंटों से बना प्रसिद्ध हड़प्पा गोदीवाड़ा ___________ में खोजा गया था।", "लोथल", "गोदीवाड़ा लोथल में मिला था।"),
    ("मेलुहा के व्यापार को दर्ज करने वाला अक्कड़ का शासक ___________ था।", "सारगोन", "अक्कड़ के राजा सारगोन ने व्यापार दर्ज किया था।"),
    ("फारस की खाड़ी शैली की एक गोल बटन मुहर ___________ से प्राप्त हुई थी।", "लोथल", "लोथल से फारस की खाड़ी की मुहर मिली थी।"),
    ("हड़प्पा सभ्यता का सबसे पश्चिमी व्यापारिक दुर्ग ___________ था।", "सुत्कागेंदोर", "सुत्कागेंदोर सबसे पश्चिमी स्थल था।"),
    ("व्यापारिक पैकेटों की सुरक्षा प्रमाणित करने के लिए मिट्टी की छाप को ___________ कहते थे।", "सीलिंग्स", "मिट्टी की छापों को सीलिंग्स (sealings) कहा जाता था।"),
    ("अंतर्देशीय माल ढोने के लिए लकड़ी की बैलगाड़ियों में ___________ पहिये लगे होते थे।", "ठोस", "पहिये ठोस होते थे (आरा वाले पहिये नहीं थे)।")
]:
    s3_mastery_hin.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

# Matchings (3)
s3_mastery_eng.extend([
    {
        "type": "Match the Following",
        "q": "Match the ancient geographical names with their modern locations:",
        "items": [{"left": "I. Meluhha", "key": "A"}, {"left": "II. Dilmun", "key": "B"}, {"left": "III. Makan", "key": "C"}],
        "options": [{"val": "A", "text": "A. Indus Valley region"}, {"val": "B", "text": "B. Bahrain Island in Persian Gulf"}, {"val": "C", "text": "C. Oman Peninsula / Makran coast"}],
        "sol": "Meluhha is Indus; Dilmun is Bahrain; Makan is Oman."
    },
    {
        "type": "Match the Following",
        "q": "Match the trade outposts with their strategic economic roles:",
        "items": [{"left": "I. Shortughai", "key": "A"}, {"left": "II. Sutkagendor", "key": "B"}, {"left": "III. Lothal", "key": "C"}],
        "options": [{"val": "A", "text": "A. Lapis Lazuli colony in Afghanistan"}, {"val": "B", "text": "B. Fortified coastal post monitoring Makran traffic"}, {"val": "C", "text": "C. Port dockyard facilitating Gulf maritime shipping"}],
        "sol": "Shortughai is lapis colony; Sutkagendor monitors Makran coast; Lothal is port dockyard."
    },
    {
        "type": "Match the Following",
        "q": "Match the transportation items with their archeological traces:",
        "items": [{"left": "I. River Boats", "key": "A"}, {"left": "II. Land Carts", "key": "B"}, {"left": "III. Dockyard Basin", "key": "C"}],
        "options": [{"val": "A", "text": "A. Terracotta models and boat drawings on seals"}, {"val": "B", "text": "B. Fossilized clay wheel ruts and toy cart models"}, {"val": "C", "text": "C. Interconnected brick basin with lock-gate at Lothal"}],
        "sol": "Boats shown on seals; land carts indicated by wheel ruts/toys; dockyard is brick basin."
    }
])

s3_mastery_hin.extend([
    {
        "type": "Match the Following",
        "q": "प्राचीन व्यापारिक भौगोलिक नामों को उनके आधुनिक स्थलों से सुमेलित करें:",
        "items": [{"left": "I. मेलुहा", "key": "A"}, {"left": "II. दिलमुन", "key": "B"}, {"left": "III. माकन", "key": "C"}],
        "options": [{"val": "A", "text": "A. सिंधु घाटी क्षेत्र"}, {"val": "B", "text": "B. फारस की खाड़ी में बहरीन द्वीप"}, {"val": "C", "text": "C. ओमान प्रायद्वीप / मकरान तट"}],
        "sol": "मेलुहा सिंधु क्षेत्र है; दिलमुन बहरीन है; माकन ओमान है।"
    },
    {
        "type": "Match the Following",
        "q": "व्यापारिक चौकियों को उनके रणनीतिक आर्थिक कार्यों से सुमेलित करें:",
        "items": [{"left": "I. शोर्तुघई", "key": "A"}, {"left": "II. सुत्कागेंदोर", "key": "B"}, {"left": "III. लोथल", "key": "C"}],
        "options": [{"val": "A", "text": "A. अफगानिस्तान में लाजवर्त (Lapis) उपनिवेश"}, {"val": "B", "text": "B. मकरान तट के यातायात की निगरानी हेतु दुर्ग"}, {"val": "C", "text": "C. खाड़ी जहाजों के आवागमन हेतु बंदरगाह"}],
        "sol": "शोर्तुघई लाजवर्त के लिए था; सुत्कागेंदोर मकरान तट पर था; लोथल बंदरगाह था।"
    },
    {
        "type": "Match the Following",
        "q": "परिवहन के साधनों को उनके पुरातात्विक साक्ष्यों से सुमेलित करें:",
        "items": [{"left": "I. नदी नावें", "key": "A"}, {"left": "II. बैलगाड़ियाँ", "key": "B"}, {"left": "III. गोदीवाड़ा बेसिन", "key": "C"}],
        "options": [{"val": "A", "text": "A. मिट्टी के खिलौने और मुहरों पर नावों के चित्र"}, {"val": "B", "text": "B. पक्की मिट्टी के पहियों के निशान व गाड़ियाँ"}, {"val": "C", "text": "C. लोथल में लॉक-गेट युक्त पकी ईंटों का तालाब"}],
        "sol": "नावें मुहरों व खिलौनों से सिद्ध हैं; बैलगाड़ियाँ पहियों के निशानों से; गोदीवाड़ा लोथल का तालाब है।"
    }
])

# One-Liner (8)
for q, sol in [
    ("What does 'Meluhha' denote in Akkadian tablets?", "The Indus Valley region."),
    ("Name the island transit point identified with Dilmun.", "Bahrain."),
    ("Where is the ancient brick dockyard located?", "Lothal."),
    ("Which Akkadian king recorded trade with Meluhha?", "Sargon of Akkad."),
    ("What was the westernmost fortified Harappan site?", "Sutkagendor."),
    ("How did merchants secure trade package knots?", "By using clay sealings (imprinting seals on wet clay)."),
    ("What was the primary trade system without currency?", "Barter system."),
    ("Which site yielded a circular Gulf button seal?", "Lothal.")
]:
    s3_mastery_eng.append({"type": "One-Liner", "q": q, "sol": sol})

for q, sol in [
    ("अक्काद की पट्टिकाओं पर 'मेलुहा' शब्द किसे दर्शाता है?", "सिंधु घाटी क्षेत्र को।"),
    ("दिलमुन के रूप में पहचाने जाने वाले द्वीप का नाम बताइए।", "बहरीन।"),
    ("पकी ईंटों का प्राचीन गोदीवाड़ा कहाँ स्थित है?", "लोथल।"),
    ("किस अक्काद सम्राट ने मेलुहा के साथ व्यापार दर्ज किया था?", "सारगोन।"),
    ("हड़प्पा सभ्यता का सबसे पश्चिमी किला कौन सा था?", "सुत्कागेंदोर।"),
    ("व्यापारी माल के बोरों को कैसे सुरक्षित करते थे?", "गीली मिट्टी पर मुहर दबाकर (सीलिंग्स द्वारा)।"),
    ("मुद्रा के बिना व्यापार की प्राथमिक व्यवस्था क्या थी?", "वस्तु विनिमय (Barter) प्रणाली।"),
    ("किस स्थल से गोल खाड़ी बटन मुहर प्राप्त हुई थी?", "लोथल।")
]:
    s3_mastery_hin.append({"type": "One-Liner", "q": q, "sol": sol})

# Assertion-Reason (8)
for q, ans, sol in [
    ("Assertion (A): Seals and clay sealings were critical tools for long-distance commerce.\nReason (R): Clay sealings over package knots served as tamper-evident locks and verified the sender's identity.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): The Harappans used silver punch-marked coins to settle trade deficits with Sumer.\nReason (R): The Harappan economy relied entirely on a barter system of exchange.", 3, "A is false but R is true. No coins existed in IVC trade."),
    ("Assertion (A): Lothal acted as an important maritime gateway for Harappan trade.\nReason (R): Lothal featured a large rectangular brick basin with inlet channels connected to a tidal river.", 0, "Both A and R are true and R explains the maritime gateway role of Lothal."),
    ("Assertion (A): Shortughai was established as a trading colony in northern Afghanistan.\nReason (R): Shortughai secured control over the procurement of highly valued Lapis Lazuli.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Akkadian cuneiform inscriptions describe Meluhha as a barren land of dust.\nReason (R): Meluhha exported precious timber, carnelian, lapis lazuli, gold, and ivory to Akkad.", 3, "A is false but R is true. Meluhha was described as a land of exotic birds and rich resources."),
    ("Assertion (A): Sutkagendor was a heavily fortified Harappan outpost on the Makran coast.\nReason (R): It was strategically positioned to monitor and control maritime shipping routes near Iran.", 0, "Both A and R are true and R explains the strategic fortification of Sutkagendor."),
    ("Assertion (A): Dilmun (Bahrain) was a crucial middleman in Mesopotamian-Indus trade.\nReason (R): Dilmun was located halfway along the Persian Gulf maritime route, acting as a transit port.", 0, "Both A and R are true and R explains the middleman status of Dilmun."),
    ("Assertion (A): Overland carriage of goods in the Indus plains was slow and laborious.\nReason (R): The Harappans lacked horse-drawn chariots and relied on slow humped oxen to pull solid-wheeled carts.", 0, "Both A and R are true and R explains why land carriage was slow.")
]:
    s3_mastery_eng.append({"type": "Assertion-Reason", "q": q, "opts": ar_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("कथन (A): लंबी दूरी के व्यापार में मुहरें और मिट्टी की छापें महत्वपूर्ण उपकरण थीं।\nकारण (R): गांठों पर लगी मिट्टी की छाप सुरक्षा सील का काम करती थी और प्रेषक की पहचान सुनिश्चित करती थी।", 0, "A और R दोनों सही हैं और R, A की सही व्याख्या करता है।"),
    ("कथन (A): सुमेर के साथ व्यापार घाटे को चुकाने के लिए हड़प्पा वासी चांदी के सिक्कों का उपयोग करते थे।\nकारण (R): हड़प्पा की संपूर्ण अर्थव्यवस्था विनिमय के लिए वस्तु विनिमय (Barter) प्रणाली पर निर्भर थी।", 3, "A गलत है लेकिन R सही है। हड़प्पा काल में सिक्कों का अस्तित्व नहीं था।"),
    ("कथन (A): लोथल हड़प्पा व्यापार का एक प्रमुख समुद्री प्रवेश द्वार था।\nकारण (R): लोथल में पकी ईंटों का एक विशाल बेसिन था जो ज्वारीय नदी से नहर द्वारा जुड़ा हुआ था।", 0, "A और R दोनों सही हैं और R, A की सही व्याख्या करता है।"),
    ("कथन (A): शोर्तुघई को उत्तरी अफगानिस्तान में एक व्यापारिक उपनिवेश के रूप में बसाया गया था।\nकारण (R): शोर्तुघई ने बहुमूल्य लाजवर्त (Lapis) पत्थर के व्यापार पर सीधे नियंत्रण की सुविधा प्रदान की।", 0, "A और R दोनों सही हैं और R, A की सही व्याख्या करता है।"),
    ("कथन (A): मेसोपोटामिया के ग्रंथों में मेलुहा को धूल से भरा बंजर देश बताया गया है।\nकारण (R): मेलुहा से अकीक, लाजवर्त, सोने, तांबे और मूल्यवान लकड़ी का निर्यात अक्कड़ को किया जाता था।", 3, "A गलत है लेकिन R सही है। मेलुहा को समृद्ध और पक्षियों का देश कहा गया था।"),
    ("कथन (A): सुत्कागेंदोर मकरान तट पर एक अत्यंत सुरक्षित हड़प्पा चौकी थी।\nकारण (R): यह ईरान के पास फारस की खाड़ी के समुद्री व्यापारिक मार्गों की निगरानी के लिए रणनीतिक रूप से स्थित था।", 0, "A और R दोनों सही हैं और R, A की सही व्याख्या करता है।"),
    ("कथन (A): मेसोपोटामिया-सिंधु व्यापार में दिलमुन (बहरीन) एक महत्वपूर्ण मध्यस्थ था।\nकारण (R): दिलमुन फारस की खाड़ी मार्ग के बीच में स्थित था, जो पारगमन बंदरगाह के रूप में उपयोगी था।", 0, "A और R दोनों सही हैं और R, A की सही व्याख्या करता है।"),
    ("कथन (A): सिंधु मैदानों में थल मार्ग से माल का परिवहन धीमा और कठिन था।\nकारण (R): हड़प्पा वासियों के पास घोड़े से चलने वाले रथ नहीं थे और वे ठोस पहियों वाली गाड़ियों के लिए बैलों पर निर्भर थे।", 0, "A और R दोनों सही हैं और R, A की सही व्याख्या करता है।")
]:
    s3_mastery_hin.append({"type": "Assertion-Reason", "q": q, "opts": hin_ar_opts, "ans": ans, "sol": sol})

# Statement-Based (5)
for q, ans, sol in [
    ("Consider the following statements:\nStatement 1: Meluhha is identified with the Oman region in cuneiform texts.\nStatement 2: Makan is identified with the Bahrain region.\nWhich of the statements given above is/are correct?", 3, "Both statements are incorrect. Meluhha is the Indus region; Makan is Oman; Dilmun is Bahrain."),
    ("Consider the following statements:\nStatement 1: The Lothal dockyard was constructed using high-quality kiln-burnt bricks.\nStatement 2: The dockyard basin was directly connected to a tributary of the Sabarmati River.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct."),
    ("Consider the following statements:\nStatement 1: The barter system was the primary exchange mechanism in Harappan commerce.\nStatement 2: Standardized seals functioned as money currency with fixed face values.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: seals were security tags, not money currency."),
    ("Consider the following statements:\nStatement 1: Sutkagendor was located on the northern borders of Afghanistan.\nStatement 2: Shortughai was situated on the Makran coast near Iran.\nWhich of the statements given above is/are correct?", 3, "Both statements are reversed: Sutkagendor is on the Makran coast, and Shortughai is in Afghanistan."),
    ("Consider the following statements:\nStatement 1: Sargon of Akkad bragged that ships of Meluhha docked at his capital city.\nStatement 2: Meluhha exported items like gold, carnelian, and ivory to Mesopotamia.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct.")
]:
    s3_mastery_eng.append({"type": "Statement-Based", "q": q, "opts": mcq_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: कीलाक्षर लेखों में मेलुहा की पहचान ओमान क्षेत्र से की जाती है।\nकथन 2: माकन की पहचान बहरीन क्षेत्र से की जाती है।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 3, "दोनों कथन गलत हैं। मेलुहा सिंधु क्षेत्र है, माकन ओमान है और दिलमुन बहरीन है।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: लोथल गोदीवाड़ा का निर्माण उच्च गुणवत्ता वाली पकी ईंटों से किया गया था।\nकथन 2: गोदीवाड़ा बेसिन सीधे साबरमती नदी की एक सहायक धारा से जुड़ा हुआ था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 2, "दोनों कथन सही हैं।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: हड़प्पा वाणिज्य में वस्तु विनिमय प्रणाली मुख्य विनिमय माध्यम थी।\nकथन 2: मानकीकृत मुहरें मौद्रिक मुद्रा का कार्य करती थीं जिन पर निश्चित मूल्य अंकित होता था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि मुहरें मुद्रा नहीं थीं।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: सुत्कागेंदोर अफगानिस्तान की उत्तरी सीमा पर स्थित था।\nकथन 2: शोर्तुघई ईरान सीमा के पास मकरान तट पर स्थित था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 3, "दोनों कथन आपस में बदल दिए गए हैं। सुत्कागेंदोर मकरान तट पर था और शोर्तुघई अफगानिस्तान में था।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: अक्कड़ के शासक सारगोन ने दावा किया था कि मेलुहा के जहाज उसकी राजधानी में लंगर डालते थे।\nकथन 2: मेलुहा मेसोपोटामिया को सोना, लाल अकीक और हाथीदांत निर्यात करता था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 2, "दोनों कथन सही हैं।")
]:
    s3_mastery_hin.append({"type": "Statement-Based", "q": q, "opts": hin_mcq_opts, "ans": ans, "sol": sol})

# Why (3)
for q, sol in [
    ("Why did the Mesopotamians refer to Dilmun (Bahrain) as a 'pure' or 'clean' land?", "Dilmun was a peaceful mercantile transit port where merchants from different civilizations met. It lacked monumental defensive fortifications or traces of military conflict, earning its name as a blessed neutral trading zone."),
    ("Why were clay sealings crucial for long-distance commerce?", "They acted as security seals. If the clay sealing remained unbroken upon delivery, it proved that the package had not been opened or tampered with, verifying the merchant's identity and protecting cargo integrity."),
    ("Why did the Harappans establish a fortified trade post at Sutkagendor on the Makran coast?", "Sutkagendor controlled the maritime entrance to the Persian Gulf. By placing a fortified post there, the Harappans secured their maritime trade route and monitored cargo ships heading towards Mesopotamia.")
]:
    s3_mastery_eng.append({"type": "Why", "q": q, "sol": sol})

for q, sol in [
    ("मेसोपोटामिया वासी दिलमुन (बहरीन) को 'पवित्र' या 'स्वच्छ' भूमि क्यों कहते थे?", "दिलमुन एक शांत व्यापारिक बंदरगाह था जहाँ विभिन्न सभ्यताओं के व्यापारी मिलते थे। यहाँ सैन्य संघर्ष या बड़े दुर्गों के निशान नहीं मिले हैं, जिससे इसे तटस्थ व्यापारिक क्षेत्र का दर्जा मिला।"),
    ("लंबी दूरी के व्यापार में मिट्टी की छापें (sealings) क्यों महत्वपूर्ण थीं?", "वे सुरक्षा सील का काम करती थीं। यदि माल पहुँचने पर मिट्टी की छाप साबुत रहती थी, तो यह साबित होता था कि पैकेट खोला नहीं गया है, जिससे प्रेषक की विश्वसनीयता और सामान की सुरक्षा सुनिश्चित होती थी।"),
    ("हड़प्पा वासियों ने मकरान तट पर सुत्कागेंदोर में एक मजबूत किला क्यों स्थापित किया?", "सुत्कागेंदोर फारस की खाड़ी के मुहाने पर नियंत्रण रखता था। यहाँ चौकी स्थापित करके हड़प्पा वासियों ने अपने समुद्री मार्गों को सुरक्षित किया और मेसोपोटामिया जाने वाले जहाजों पर नियंत्रण रखा।")
]:
    s3_mastery_hin.append({"type": "Why", "q": q, "sol": sol})

# How (3)
for q, sol in [
    ("How did the lock-gate system in the Lothal dockyard operate to facilitate shipping?", "During high tide, ships entered the dockyard through an inlet channel. At low tide, a wooden sluice-gate at the spillway was lowered to trap the water inside the basin, maintaining depth and keeping ships afloat for loading."),
    ("How do cuneiform inscriptions help reconstruct the trade relations of the Indus Valley?", "They list imports from Meluhha (timbers, gold, carnelian, lapis, ivory), mention transit points (Dilmun, Makan), and describe ships of Meluhha docking at Akkad, verifying direct trade contacts."),
    ("How did the Harappans transport heavy cargo inland across vast distances?", "They used solid-wheeled wooden bullock carts pulled by oxen. Fossilized clay wheel ruts matching modern track gauges suggest that these carts travelled along established, standardized land routes between cities.")
]:
    s3_mastery_eng.append({"type": "How", "q": q, "sol": sol})

for q, sol in [
    ("नौवहन को आसान बनाने के लिए लोहे के बिना लोथल गोदीवाड़ा का लॉक-गेट सिस्टम कैसे काम करता था?", "उच्च ज्वार के समय जहाज नहर के रास्ते गोदी में प्रवेश करते थे। निम्न ज्वार के समय अतिरिक्त पानी के निकास द्वार पर लकड़ी का एक फाटक गिरा दिया जाता था, जिससे पानी अंदर रुक जाता था और जहाज तैरते रहते थे।"),
    ("मेसोपोटामिया के कीलाक्षर अभिलेख सिंधु घाटी के व्यापारिक संबंधों को समझने में कैसे मदद करते हैं?", "वे मेलुहा से आने वाली वस्तुओं (लकड़ी, सोना, अकीक, लाजवर्त, हाथीदांत) की सूची देते हैं, बहरीन (दिलमुन) और ओमान (माकन) का उल्लेख करते हैं, जिससे सीधे व्यापारिक संपर्कों की पुष्टि होती है।"),
    ("हड़प्पा वासी लंबी दूरी तक भारी माल का अंतर्देशीय परिवहन कैसे करते थे?", "वे बैलों द्वारा खींची जाने वाली ठोस लकड़ी के पहियों वाली गाड़ियों का प्रयोग करते थे। सड़कों पर मिले पहियों के निशान यह दर्शाते हैं कि वे शहरों के बीच बने नियमित थल मार्गों पर यात्रा करते थे।")
]:
    s3_mastery_hin.append({"type": "How", "q": q, "sol": sol})

# Case Study (3)
for q, sol in [
    ("Case Study: The Lothal Dockyard and Tidal Engineering. Analyze its design.", "Constructed in the delta of the Sabarmati, the dockyard shows advanced knowledge of tides. The basin was lined with thick burnt bricks to resist water pressure, and a lock-gate regulated water levels, allowing year-round harbor operations in a tidal estuary."),
    ("Case Study: Mesopotamian Trade Tablets. Discuss the textual evidence of Meluhha.", "Mesopotamian tablets from the Akkadian and Ur III periods detail trading contracts. In one tablet, Sargon of Akkad boasts that ships of Meluhha, Makan, and Dilmun docked at his capital, proving the scale of Indus maritime reach."),
    ("Case Study: Shortughai Trading Colony. Discuss its strategic positioning.", "Located on the Oxus River in northern Afghanistan, Shortughai was isolated from the Indus plain. However, it was located near the richest lapis lazuli mines of Badakhshan and copper mines, serving as a dedicated resource extraction colony.")
]:
    s3_mastery_eng.append({"type": "Case Study", "q": q, "sol": sol})

for q, sol in [
    ("केस स्टडी: लोथल गोदीवाड़ा और ज्वारीय इंजीनियरिंग। इसके डिजाइन का विश्लेषण करें।", "साबरमती डेल्टा में बने इस गोदीवाड़ा में ज्वार-भाटे का गहरा ज्ञान दिखता है। पानी के दबाव को रोकने के लिए दीवारों को पकी ईंटों से जोड़ा गया था और लॉक-गेट द्वारा पानी का स्तर नियंत्रित किया जाता था ताकि नावें हमेशा तैरती रहें।"),
    ("केस स्टडी: मेसोपोटामिया की व्यापारिक पट्टिकाएँ। मेलुहा के लिखित साक्ष्यों पर चर्चा करें।", "अक्कड़ और उर काल की पट्टिकाएँ व्यापार सौदों का विवरण देती हैं। एक पट्टिका में राजा सारगोन ने गर्व से लिखा है कि मेलुहा के जहाजों ने उसकी राजधानी अक्कड़ में लंगर डाला, जो सिंधु सभ्यता के समुद्री प्रभाव को दर्शाता है।"),
    ("केस स्टडी: शोर्तुघई व्यापारिक उपनिवेश। इसकी रणनीतिक स्थिति पर चर्चा करें।", "उत्तरी अफगानिस्तान में आक्सस नदी पर स्थित शोर्तुघई सिंधु मैदानों से बहुत दूर था। लेकिन यह बदख्शां की लाजवर्त खदानों और तांबे के स्रोतों के निकट था, जो इसे एक महत्वपूर्ण संसाधन निष्कर्षण केंद्र बनाता था।")
]:
    s3_mastery_hin.append({"type": "Case Study", "q": q, "sol": sol})

# Teach Concept (3)
for q, sol in [
    ("Teach the Concept: Sluice-Gate Hydrology in Lothal Dockyard.", "Explain how Harappan engineers used the force of gravity and wooden gates to trap tidal water inside a brick basin. This ensured that despite 4-meter tide variations, ships remained stable and floating during loading."),
    ("Teach the Concept: Tamper-Evident Clay Sealings in Ancient Commerce.", "Explain to students that clay sealings acted as a physical security key. If a sealing arrived broken, it indicated theft or tampering, allowing ancient merchants to secure trade caravans without metal padlocks."),
    ("Teach the Concept: The Meluhha-Mesopotamia Maritime Trade Route.", "Teach the route taken by Harappan ships: coast-hugging from the Indus delta along the Makran coast (Makan/Oman), stopping at Bahrain (Dilmun), and entering the Euphrates-Tigris delta to reach Akkad in Mesopotamia.")
]:
    s3_mastery_eng.append({"type": "Teach Concept", "q": q, "sol": sol})

for q, sol in [
    ("अवधारणा सिखाएं: लोथल गोदीवाड़ा में लॉक-गेट (Sluice-gate) हाइड्रोलॉजी।", "समझाएं कि कैसे हड़प्पा के इंजीनियरों ने ज्वार के पानी को ईंटों के तालाब में रोकने के लिए गुरुत्वाकर्षण और लकड़ी के द्वारों का प्रयोग किया। इससे ज्वार के उतरने के बाद भी जहाज स्थिर बने रहते थे।"),
    ("अवधारणा सिखाएं: प्राचीन वाणिज्य में सुरक्षा मिट्टी की छाप (sealings)।", "छात्रों को समझाएं कि गीली मिट्टी की छाप सुरक्षा कुंजी थी। यदि छाप टूटी मिलती थी, तो यह चोरी या छेड़छाड़ का संकेत थी, जिससे बिना धातु के तालों के भी व्यापारिक माल को सुरक्षित रखा जाता था।"),
    ("अवधारणा सिखाएं: मेलुहा-मेसोपोटामिया समुद्री व्यापार मार्ग।", "हड़प्पा जहाजों के मार्ग को समझाएं: सिंधु मुहाने से मकरान तट (ओमान/माकन) के सहारे चलते हुए, बहरीन (दिलमुन) में रुकना और दजला-फरात डेल्टा से होते हुए मेसोपोटामिया के अक्कड़ शहर पहुँचना।")
]:
    s3_mastery_hin.append({"type": "Teach Concept", "q": q, "sol": sol})


# Wait, we need to make sure that the length of s1, s2, s3 is EXACTLY 62!
# Let's count them:
# MCQ: 5
# Multi-Correct: 5
# True/False: 8
# Fill in the Blank: 8 (Wait! For s3_mastery_eng, we appended Fill Blanks to s1_mastery_eng instead of s3_mastery_eng! Let's double check the variable names in the script.)
# Let's write the code clearly and verify variables.
# For s3_mastery_eng, we had:
# s1_mastery_eng.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})
# Ah! We must write it as s3_mastery_eng.append(...) inside the loop!
# Yes, let's fix that.
# Let's carefully write out the python script.

# Wait, let's verify if the lists have exactly 62 questions:
# MCQ: 5
# Multi-Correct: 5
# True/False: 8
# Fill Blanks: 8
# Matchings: 3
# One-Liner: 8
# Assertion-Reason: 8
# Statement-Based: 5
# Why: 3
# How: 3
# Case Studies: 3
# Teach Concept: 3
# Sum: 5 + 5 + 8 + 8 + 3 + 8 + 8 + 5 + 3 + 3 + 3 + 3 = 62.
# Yes! The count is exactly 62 questions per section.

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
