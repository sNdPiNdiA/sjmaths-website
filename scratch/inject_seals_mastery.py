import json
import os

ENG_PATH = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\HarappanIndus-Valley-Civilisation\Seals-and-Images\content.json"
HIN_PATH = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\HarappanIndus-Valley-Civilisation\Seals-and-Images\hi\content.json"

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
# SECTION 1: HARAPPAN SEALS & COPPER TABLETS
# =========================================================================
s1_mastery_eng = []
s1_mastery_hin = []

# MCQ (5)
for q, opts, ans, sol in [
    ("Which of the following minerals was primarily used to manufacture standard Harappan seals?", ["Steatite", "Chert", "Lapis Lazuli", "Carnelian"], 0, "Steatite (talcose soapstone) was the primary raw material for Harappan seals."),
    ("The chemical transformation of steatite into enstatite during kiln firing achieved which of the following results?", ["Hardened the seal and created a glazed white surface", "Turned the soft stone into metallic copper", "Dissolved the seal to create clay castings", "Prevented the seal from being stamped on wet clay"], 0, "Firing steatite above 900°C converts it to enstatite, hardening the stone and creating a glazed white surface."),
    ("What physical feature is typically found on the reverse side of square Harappan seals?", ["A raised boss (button) pierced with a suspension hole", "A secondary script inscription representing the price", "A flat surface with copper-inlaid frames", "Nothing, it was completely smooth"], 0, "The reverse of square seals features a raised boss (button) with a hole for a suspension cord."),
    ("Which of the following materials was NOT used to manufacture seals in the Indus Valley?", ["Iron", "Terracotta", "Agate", "Copper"], 0, "Iron was completely unknown to the Harappans."),
    ("The copper tablets found in large quantities at Mohenjo-daro are characterized by which of the following?", ["An animal or deity on one side and a script inscription on the other", "Perforated bosses on the reverse for suspension", "Cylindrical forms rolled over clay taggings", "Stamping representing standard monetary value"], 0, "Copper tablets show an animal/deity on one side and script on the other. They have no reverse boss.")
]:
    s1_mastery_eng.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("मानक हड़प्पा मुहरों के निर्माण में मुख्य रूप से किस खनिज का उपयोग किया जाता था?", ["सेलखड़ी (Steatite)", "चर्ट (Chert)", "लाजवर्त (Lapis Lazuli)", "कार्नेलियन (Carnelian)"], 0, "सेलखड़ी (सोपस्टोन) हड़प्पा मुहरों के लिए प्राथमिक कच्चा माल था।"),
    ("भट्टी में पकाने के दौरान सेलखड़ी का एन्सटाइट में रासायनिक परिवर्तन निम्नलिखित में से क्या परिणाम देता था?", ["मुहर को कठोर करता था और एक चमकदार सफेद सतह बनाता था", "नरम पत्थर को तांबे में बदल देता था", "मिट्टी के सांचे बनाने के लिए पत्थर को पिघलाता था", "गीली मिट्टी पर मुहर लगाने से रोकता था"], 0, "सेलखड़ी को 900 डिग्री सेल्सियस से ऊपर पकाने से यह कठोर एन्सटाइट में बदल जाती थी और चमकदार सफेद सतह बनती थी।"),
    ("चौकोर हड़प्पा मुहरों के पीछे आमतौर पर कौन सी विशेषता पाई जाती है?", ["छेद वाला एक उभरा हुआ बटन (boss)", "मूल्य दर्शाने वाला एक दूसरा शिलालेख", "तांबे के फ्रेम वाली एक सपाट सतह", "कुछ नहीं, यह पूरी तरह से चिकनी होती थी"], 0, "चौकोर मुहरों के पीछे एक छेद वाला उभरा हुआ बटन होता था जिसमें लटकने के लिए धागा डाला जाता था।"),
    ("सिंधु घाटी में मुहरों के निर्माण के लिए निम्नलिखित में से किस सामग्री का उपयोग नहीं किया जाता था?", ["लोहा", "पकी मिट्टी (Terracotta)", "अगेट (Agate)", "तांबा"], 0, "हड़प्पा वासियों को लोहे का कोई ज्ञान नहीं था।"),
    ("मोहनजोदड़ो से प्रचुर मात्रा में प्राप्त तांबे की पट्टियों की क्या विशेषता है?", ["एक तरफ पशु या देवता और दूसरी तरफ लिपि का अंकन", "लटकने के लिए छेददार बटन", "मिट्टी पर घुमाए जाने वाले बेलनाकार आकार", "मानक मौद्रिक मूल्य को दर्शाने वाली छाप"], 0, "तांबे की पट्टियों पर एक तरफ पशु/देवता और दूसरी तरफ लेख होता है। इनके पीछे कोई उभार नहीं होता।")
]:
    s1_mastery_hin.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# Multiple Correct MCQ (5)
for q, opts, ans, sol in [
    ("Select the materials used in manufacturing Indus Valley seals: (Select all that apply)", ["Steatite", "Faience", "Copper", "Iron"], [0, 1, 2], "Steatite, faience, and copper were used. Iron was unknown."),
    ("Which of the following are functions of Harappan seals? (Select all that apply)", ["Securing goods in transit via clay sealings", "Serving as personal identification and status markers", "Functioning as protective amulets worn on the body", "Serving as currency for daily market purchases"], [0, 1, 2], "Seals were commercial tags, identity markers, and amulets, not currency."),
    ("Identify the characteristic features of square Harappan seals: (Select all that apply)", ["Carved in intaglio (sunken relief)", "Feature animal motifs along with script", "Possess a pierced boss on the reverse", "Carved exclusively in raised cameo relief"], [0, 1, 2], "Square seals are intaglio, feature animals and text, and have a pierced boss."),
    ("Which of the following animals are commonly depicted on Harappan seals? (Select all that apply)", ["Unicorn", "Humped Bull (Zebu)", "Elephant", "Lion"], [0, 1, 2], "Unicorn, humped bull, and elephant are common. Lions are never depicted."),
    ("Select correct statements regarding Harappan copper tablets: (Select all that apply)", ["They were found primarily at Mohenjo-daro and Harappa", "They are thin, rectangular plates with shallow engraving", "They lack a pierced boss on the reverse", "They were used as coins for international trade"], [0, 1, 2], "Copper tablets are concentrated at Mohenjo-daro/Harappa, are thin and boss-less, and were likely amulets rather than coins.")
]:
    s1_mastery_eng.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("सिंधु घाटी की मुहरों के निर्माण में प्रयुक्त सामग्रियों का चयन करें: (सभी लागू विकल्प चुनें)", ["सेलखड़ी (Steatite)", "फेयॉन्स (Faience)", "तांबा", "लोहा"], [0, 1, 2], "सेलखड़ी, फेयॉन्स और तांबे का उपयोग होता था। लोहा अज्ञात था।"),
    ("निम्नलिखित में से कौन से हड़प्पा मुहरों के कार्य थे? (सभी लागू विकल्प चुनें)", ["मिट्टी की छापों के माध्यम से पारगमन में माल सुरक्षित करना", "व्यक्तिगत पहचान और सामाजिक प्रतिष्ठा के रूप में कार्य करना", "सुरक्षात्मक ताबीज के रूप में शरीर पर पहना जाना", "बाजार में दैनिक खरीद के लिए मुद्रा के रूप में कार्य करना"], [0, 1, 2], "मुहरें वाणिज्यिक टैग, पहचान पत्र और ताबीज थीं, मुद्रा नहीं।"),
    ("वर्गाकार हड़प्पा मुहरों की विशिष्ट विशेषताओं की पहचान करें: (सभी लागू विकल्प चुनें)", ["अंतर्गठित नक्काशी (intaglio) में उत्कीर्ण", "पशु आकृतियों के साथ लिपि का अंकन", "पीछे की तरफ छेददार उभार (boss) होना", "केवल उभरी हुई नक्काशी (cameo) में निर्मित"], [0, 1, 2], "चौकोर मुहरें अंतर्गठित होती हैं, उन पर पशु व लेख होते हैं और पीछे बटन होता है।"),
    ("हड़प्पा मुहरों पर आमतौर पर निम्नलिखित में से किन पशुओं का अंकन मिलता है? (सभी लागू विकल्प चुनें)", ["एक सींग वाला पशु (Unicorn)", "कूबड़ वाला सांड", "हाथी", "शेर"], [0, 1, 2], "यूनिकॉर्न, सांड और हाथी आम हैं। शेर का अंकन कभी नहीं मिलता।"),
    ("हड़प्पा की तांबे की पट्टिकाओं के संबंध में सही कथनों का चयन करें: (सभी लागू विकल्प चुनें)", ["ये मुख्य रूप से मोहनजोदड़ो और हड़प्पा से मिली हैं", "ये उथली नक्काशी वाली पतली, आयताकार प्लेटें हैं", "इनके पीछे छेददार बटन का अभाव होता है", "इनका उपयोग अंतरराष्ट्रीय व्यापार में सिक्कों के रूप में होता था"], [0, 1, 2], "तांबे की पट्टियां मोहनजोदड़ो/हड़प्पा से मिली हैं, पतली और बटन-रहित हैं और संभवतः ताबीज थीं।")
]:
    s1_mastery_hin.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# True/False (8)
for q, ans, sol in [
    ("All Harappan seals discovered were made of bronze using lost-wax casting.", False, "False. Most seals were made of steatite (stone), not bronze."),
    ("The Unicorn motif is depicted in front of a double-tiered censer or standard on Harappan seals.", True, "True. The Unicorn stands before a censer standard, interpreted as a cult object."),
    ("The Indus script characters on seals were engraved in intaglio so that they left a raised positive print on clay.", True, "True. Sunken intaglio engravings produce raised impressions on clay."),
    ("Iron-backed seals were discovered at Lothal, proving that Harappans used iron for reinforcement.", False, "False. Iron was unknown to the Harappan civilization."),
    ("Copper tablets have a raised perforated boss on their reverse for suspension cords.", False, "False. Copper tablets are flat and lack a reverse boss."),
    ("Lions are prominently depicted on at least 10% of Mature Harappan seals.", False, "False. Lions are completely absent from Harappan seal iconography."),
    ("Some clay sealings found at Lothal show impressions of packing cords on their reverse, verifying packaging security.", True, "True. Cord impressions on the reverse of sealings verify they were tied to trade packages."),
    ("Rectangular seals usually carry only script inscriptions and lack animal motifs.", True, "True. Rectangular/bar seals typically feature only script.")
]:
    s1_mastery_eng.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("खोजी गई सभी हड़प्पा मुहरें लुप्त मोम ढलाई का उपयोग करके कांसे से बनाई गई थीं।", False, "असत्य। अधिकांश मुहरें सेलखड़ी पत्थर की थीं, कांसे की नहीं।"),
    ("हड़प्पा मुहरों पर एक सींग वाला पशु (Unicorn) एक दो-स्तरीय धूपदान या पात्र के सामने खड़ा दिखाया गया है।", True, "सत्य। यूनिकॉर्न एक धूप पात्र के सामने खड़ा दिखाया गया है।"),
    ("मुहरों पर सिंधु लिपि के अक्षर अंतर्गठित उत्कीर्ण थे ताकि वे मिट्टी पर उभरी हुई छाप छोड़ सकें।", True, "सत्य। अंतर्गठित उत्कीर्णन मिट्टी पर उभरी हुई छाप बनाता है।"),
    ("लोथल से लोहे के आधार वाली मुहरें खोजी गई हैं, जो साबित करती हैं कि हड़प्पा वासी लोहे का उपयोग करते थे।", False, "असत्य। हड़प्पा सभ्यता में लोहे का ज्ञान नहीं था।"),
    ("तांबे की पट्टिकाओं के पीछे धागा पिरोने के लिए एक उभरा हुआ छेददार बटन होता था।", False, "असत्य। तांबे की पट्टियां चपटी होती हैं और उनके पीछे कोई उभार नहीं होता।"),
    ("परिपक्व हड़प्पा मुहरों में से कम से कम 10% पर शेर का प्रमुखता से चित्रण किया गया है।", False, "असत्य। हड़प्पा मुहरों पर शेर का अंकन पूरी तरह अनुपस्थित है।"),
    ("लोथल से प्राप्त कुछ मिट्टी की सील पर पीछे पैकिंग रस्सियों के निशान मिले हैं, जो पैकिंग सुरक्षा की पुष्टि करते हैं।", True, "सत्य। सील के पीछे रस्सियों के निशान दर्शाते हैं कि वे बोरियों पर बांधी जाती थीं।"),
    ("आयताकार मुहरों पर आमतौर पर केवल लिपि के अक्षर होते हैं और पशु आकृतियों का अभाव होता है।", True, "सत्य। आयताकार/छड़ मुहरों पर केवल लिपि का अंकन होता है।")
]:
    s1_mastery_hin.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

# Fill in the Blank (8)
for q, ans, sol in [
    ("The soft talcose mineral used to carve the vast majority of Harappan seals is ___________.", "steatite", "Steatite was the primary soft soapstone mineral used."),
    ("Firing a steatite seal in a kiln converts the talc into a harder mineral called ___________.", "enstatite", "Firing talc at high temperatures converts it to enstatite."),
    ("Square seals feature a raised, perforated button on the reverse called a ___________.", "boss", "The raised projection on the reverse is called a boss."),
    ("Engraving carved into the surface of a seal is known as ___________ relief.", "intaglio", "Intaglio refers to sunken/incised relief carving."),
    ("The most commonly depicted mythical animal on Harappan seals is the ___________.", "unicorn", "The Unicorn is the most common motif, depicted in profile with one horn."),
    ("Unlike square seals, rectangular bar seals contain only ___________.", "script", "Rectangular seals contain script characters and lack animals."),
    ("Thin, flat metal plates with text on one side and an animal on the reverse are called ___________ tablets.", "copper", "These are known as copper tablets, found mostly at Mohenjo-daro."),
    ("The chemical glaze on fired seals was created by applying a slip made of water and ___________.", "talc", "A fine talc-based slip was applied prior to firing to create the glazed white finish.")
]:
    s1_mastery_eng.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("अधिकांश हड़प्पा मुहरों को तराशने के लिए प्रयुक्त नरम साबुन पत्थर (सोपस्टोन) खनिज को ___________ कहा जाता है।", "सेलखड़ी", "सेलखड़ी (steatite) प्राथमिक मुलायम पत्थर था।"),
    ("सेलखड़ी की मुहर को भट्टी में पकाने पर यह एक कठोर खनिज में बदल जाती है जिसे ___________ कहा जाता है।", "एन्सटाइट", "उच्च तापमान पर पकाने से सेलखड़ी एन्सटाइट (enstatite) में बदलती है।"),
    ("चौकोर मुहरों के पीछे एक उभरा हुआ गोल छेददार बटन होता है जिसे ___________ कहा जाता है।", "बॉस", "पीछे के उभार को बॉस (boss) या बटन कहा जाता है।"),
    ("मुहर की सतह के भीतर उकेरी गई नक्काशी को ___________ नक्काशी कहा जाता है।", "अंतर्गठित", "सतह के अंदर उकेरी गई नक्काशी को अंतर्गठित (intaglio) नक्काशी कहते हैं।"),
    ("हड़प्पा मुहरों पर सबसे अधिक चित्रित होने वाला काल्पनिक पशु ___________ है।", "यूनिकॉर्न", "एक सींग वाला यूनिकॉर्न (unicorn) सबसे आम पशु प्रतीक है।"),
    ("चौकोर मुहरों के विपरीत, आयताकार मुहरों पर केवल ___________ उत्कीर्ण होती है।", "लिपि", "आयताकार मुहरों पर केवल लिपि होती है, पशु नहीं।"),
    ("एक तरफ लेख और दूसरी तरफ पशु चित्रण वाली पतली सपाट धातु की पट्टियों को ___________ पट्टिकाएं कहा जाता है।", "तांबे", "इन्हें तांबे की पट्टिकाएं (copper tablets) कहा जाता है।"),
    ("मुहरों पर पकाने के बाद सफेद चमकदार परत बनाने के लिए पानी और ___________ का लेप लगाया जाता था।", "टैल्क", "पकाने से पहले बारीक पिसे हुए टैल्क (talc) का लेप लगाया जाता था।")
]:
    s1_mastery_hin.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

# Match the Following (3)
for q, items, opts, sol in [
    (
        "Match the seal types with their typical attributes:",
        [{"left": "I. Square Steatite Seals", "key": "A"}, {"left": "II. Rectangular Steatite Seals", "key": "B"}, {"left": "III. Rectangular Copper Tablets", "key": "C"}],
        [{"val": "A", "text": "A. Feature animal motifs + script, with a reverse boss"}, {"val": "B", "text": "B. Feature script only, with a flat or convex reverse (no boss)"}, {"val": "C", "text": "C. Two-sided flat metal tokens, shallow engraving"}],
        "Square seals have animal+script and a boss; rectangular seals have script only; copper tablets are flat two-sided metal tokens."
    ),
    (
        "Match the animal motifs on seals with their symbolic interpretations:",
        [{"left": "I. Unicorn", "key": "A"}, {"left": "II. Humped Bull (Zebu)", "key": "B"}, {"left": "III. Composite beast (three heads)", "key": "C"}],
        [{"val": "A", "text": "A. Mythical emblem associated with a ritual censer/standard"}, {"val": "B", "text": "B. Real animal representing strength, virility, and fertility"}, {"val": "C", "text": "C. Rich mythological lore combining bull, unicorn, and ibex"}],
        "Unicorn is a mythical emblem with a censer; Humped bull represents virility/fertility; Composite beasts show complex mythology."
    ),
    (
        "Match the materials with their manufacturing traits in seal production:",
        [{"left": "I. Steatite", "key": "A"}, {"left": "II. Faience", "key": "B"}, {"left": "III. Terracotta", "key": "C"}],
        [{"val": "A", "text": "A. Soft stone carved in intaglio and hardened by kiln firing"}, {"val": "B", "text": "B. Synthetic glazed silica paste pressed into clay molds"}, {"val": "C", "text": "C. Baked clay modeled by hand or stamp-impressed"}],
        "Steatite is soft stone hardened by firing; Faience is pressed silica paste; Terracotta is baked clay."
    )
]:
    s1_mastery_eng.append({"type": "Match the Following", "q": q, "items": items, "options": opts, "sol": sol})

for q, items, opts, sol in [
    (
        "मुहर के प्रकारों को उनकी विशिष्ट विशेषताओं से सुमेलित करें:",
        [{"left": "I. चौकोर सेलखड़ी मुहरें", "key": "A"}, {"left": "II. आयताकार सेलखड़ी मुहरें", "key": "B"}, {"left": "III. आयताकार तांबे की पट्टिकाएं", "key": "C"}],
        [{"val": "A", "text": "A. पशु आकृति + लिपि, पीछे छेददार उभार (boss) होना"}, {"val": "B", "text": "B. केवल लिपि का अंकन, पीछे सपाट या उत्तल सतह (उभार रहित)"}, {"val": "C", "text": "C. दोनों तरफ खुदे हुए चपटे धातु के टोकन, उथली नक्काशी"}],
        "चौकोर मुहरों पर पशु+लिपि और पीछे बटन होता है; आयताकार मुहरों पर केवल लेख होता है; तांबे की पट्टिकाएं चपटी द्वि-पक्षीय होती हैं।"
    ),
    (
        "मुहरों पर अंकित पशु रूपांकनों को उनकी व्याख्याओं से सुमेलित करें:",
        [{"left": "I. एक सींग वाला पशु (Unicorn)", "key": "A"}, {"left": "II. कूबड़ वाला बैल (Zebu)", "key": "B"}, {"left": "III. तीन सिरों वाला मिश्रित जीव", "key": "C"}],
        [{"val": "A", "text": "A. धूप पात्र/मानक के साथ जुड़ा काल्पनिक धार्मिक प्रतीक"}, {"val": "B", "text": "B. शक्ति और जनन क्षमता का प्रतिनिधित्व करने वाला वास्तविक पशु"}, {"val": "C", "text": "C. सांड, यूनिकॉर्न और बकरे के अंगों को जोड़ने वाला पौराणिक जीव"}],
        "यूनिकॉर्न धूप पात्र के साथ काल्पनिक प्रतीक है; सांड शक्ति/उर्वरता का प्रतीक है; मिश्रित जीव पौराणिक कहानियों को दर्शाता है।"
    ),
    (
        "सामग्रियों को मुहर निर्माण में उनकी विशेषताओं से सुमेलित करें:",
        [{"left": "I. सेलखड़ी (Steatite)", "key": "A"}, {"left": "II. फेयॉन्स (Faience)", "key": "B"}, {"left": "III. मिट्टी (Terracotta)", "key": "C"}],
        [{"val": "A", "text": "A. मुलायम पत्थर जिसे तराशने के बाद भट्टी में पकाकर कड़ा किया जाता था"}, {"val": "B", "text": "B. सिलिका पेस्ट जिसे सांचों में दबाकर चमकीला बनाया जाता था"}, {"val": "C", "text": "C. पकाई गई मिट्टी जिसे हाथ से गढ़ा या ठप्पा दबाकर बनाया जाता था"}],
        "सेलखड़ी पकाया जाने वाला मुलायम पत्थर है; फेयॉन्स सांचे में दबाया गया सिलिका पेस्ट है; टेराकोटा पकी मिट्टी है।"
    )
]:
    s1_mastery_hin.append({"type": "Match the Following", "q": q, "items": items, "options": opts, "sol": sol})

# One-Liner (8)
for q, sol in [
    ("Name the primary soapstone mineral used to make Harappan seals.", "Steatite (talc)."),
    ("Into which mineral does steatite convert when fired in a kiln?", "Enstatite."),
    ("Why do square seals have a raised boss with a hole on their reverse?", "To pass a cord through it for suspension or carrying."),
    ("What are the flat copper plates with text and animals called?", "Copper tablets."),
    ("Name the most common mythical animal carved on Harappan seals.", "The Unicorn."),
    ("What style of carving (relief) is used on Harappan seals?", "Intaglio (sunken relief)."),
    ("Name one non-Indus region where Harappan seals have been excavated.", "Mesopotamia (or Persian Gulf sites like Bahrain)."),
    ("True or False: Harappan seals were used as metal coins.", "False (they were commercial tags, identity tokens, and amulets).")
]:
    s1_mastery_eng.append({"type": "One-Liner", "q": q, "sol": sol})

for q, sol in [
    ("हड़प्पा मुहरों को बनाने के लिए प्रयुक्त प्राथमिक सोपस्टोन खनिज का नाम बताएं।", "सेलखड़ी (Steatite/Talc)।"),
    ("भट्टी में पकाने पर सेलखड़ी किस खनिज में परिवर्तित हो जाती है?", "एन्सटाइट (Enstatite)।"),
    ("चौकोर मुहरों के पीछे छेद वाले उभार (boss) का क्या उद्देश्य था?", "लटकाने या ले जाने के लिए उसमें से धागा पिरोना।"),
    ("एक तरफ लेख और दूसरी तरफ पशु आकृतियों वाली तांबे की चपटी प्लेटों को क्या कहते हैं?", "तांबे की पट्टिकाएं (Copper tablets)।"),
    ("हड़प्पा मुहरों पर अंकित सबसे आम काल्पनिक जीव का नाम बताएं।", "एक सींग वाला पशु (Unicorn)।"),
    ("हड़प्पा मुहरों पर नक्काशी की कौन सी शैली (राहत) उपयोग की जाती है?", "अंतर्गठित नक्काशी (Intaglio/धँसी हुई नक्काशी)।"),
    ("सिंधु क्षेत्र के बाहर के एक क्षेत्र का नाम बताएं जहां हड़प्पा मुहरें मिली हैं।", "मेसोपोटामिया (या फारस की खाड़ी के स्थल जैसे बहरीन)।"),
    ("सत्य या असत्य: हड़प्पा मुहरों का उपयोग धातु के सिक्कों के रूप में होता था।", "असत्य (वे व्यापारिक टैग, पहचान पत्र और ताबीज थे)।")
]:
    s1_mastery_hin.append({"type": "One-Liner", "q": q, "sol": sol})

# Assertion-Reason (8)
for q, ans, sol in [
    ("Assertion (A): Firing steatite seals was a key technological step in their manufacture.\nReason (R): Kiln firing chemically converted the soft talc into hard enstatite, rendering the seals durable.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Harappan seals were used as metallic coins in market exchange.\nReason (R): Seals are made of highly standardized weights of silver and gold.", 4, "Both A and R are false. Seals were stone/clay trade tags and amulets, and contain no precious metal weights."),
    ("Assertion (A): Square seals are carved in intaglio.\nReason (R): Intaglio carving allowed the seals to leave a raised positive impression when stamped on wet clay.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Copper tablets served as administrative credentials for foreign trade.\nReason (R): Copper tablets contain a raised pierced boss on the reverse for suspension cords.", 2, "A is true but R is false. Copper tablets lack a reverse boss entirely."),
    ("Assertion (A): The Unicorn motif represents a real animal that went extinct in the Indus Valley.\nReason (R): It is always shown with a double-tiered censer standard in front of it.", 3, "A is false but R is true. The Unicorn is a mythical composite animal, not a real extinct species."),
    ("Assertion (A): Harappan merchants stamped wet clay tags on trade packages.\nReason (R): A sealing proved that the cargo arrived intact and verified the merchant's identity.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Rectangular seals are characterized by their elaborate animal depictions.\nReason (R): Rectangular seals carry script characters but almost completely lack animal motifs.", 3, "A is false but R is true. Rectangular seals carry script only and lack animals."),
    ("Assertion (A): Faience seals were produced through lost-wax metal casting.\nReason (R): Faience is a glazed ceramic material made of silica, clay, and gum, pressed into molds.", 3, "A is false but R is true. Faience is a ceramic material pressed in clay molds, not a metal cast.")
]:
    s1_mastery_eng.append({"type": "Assertion-Reason", "q": q, "opts": ar_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("कथन (A): सेलखड़ी की मुहरों को भट्टी में पकाना उनके निर्माण में एक महत्वपूर्ण तकनीकी कदम था।\nकारण (R): भट्टी में पकाने से नरम सोपस्टोन रासायनिक रूप से कठोर एन्सटाइट में बदल जाता था, जिससे मुहरें टिकाऊ हो जाती थीं।", 0, "कथन (A) और कारण (R) दोनों सही हैं और कारण (R), कथन (A) की सही व्याख्या है।"),
    ("कथन (A): हड़प्पा मुहरों का उपयोग बाजार विनिमय में धातु के सिक्कों के रूप में किया जाता था।\nकारण (R): मुहरें चांदी और सोने के अत्यधिक मानकीकृत भार से बनी थीं।", 4, "कथन (A) और कारण (R) दोनों गलत हैं। मुहरें सिक्के नहीं थीं, और वे पत्थर/मिट्टी की थीं, सोने-चांदी की नहीं।"),
    ("कथन (A): चौकोर मुहरें अंतर्गठित (intaglio) नक्काशी में उकेरी जाती थीं।\nकारण (R): अंतर्गठित नक्काशी मुहरों को गीली मिट्टी पर दबाने पर एक उभरी हुई छाप छोड़ने में मदद करती थी।", 0, "कथन (A) और कारण (R) दोनों सही हैं और कारण (R), कथन (A) की सही व्याख्या है।"),
    ("कथन (A): तांबे की पट्टिकाएं विदेशी व्यापार के लिए प्रशासनिक प्रमाण पत्र का कार्य करती थीं।\nकारण (R): तांबे की पट्टिकाओं के पीछे लटकने वाले धागे के लिए एक उभरा हुआ छेददार बटन होता था।", 2, "कथन (A) सही है लेकिन कारण (R) गलत है। तांबे की पट्टिकाओं पर पीछे कोई बटन नहीं होता।"),
    ("कथन (A): एक सींग वाला यूनिकॉर्न एक वास्तविक पशु का प्रतिनिधित्व करता है जो सिंधु घाटी में विलुप्त हो गया था।\nकारण (R): इसे हमेशा इसके सामने रखे एक दो-स्तरीय धूप पात्र के साथ दिखाया गया है।", 3, "कथन (A) गलत है लेकिन कारण (R) सही है। यूनिकॉर्न एक काल्पनिक मिश्रित पशु है, कोई वास्तविक विलुप्त प्रजाति नहीं।"),
    ("कथन (A): हड़प्पा के व्यापारी व्यापारिक पैकेटों पर गीली मिट्टी की छाप (सील) लगाते थे।\nकारण (R): सील यह साबित करती थी कि माल बिना छेड़छाड़ के पहुंचा है और व्यापारी की पहचान की पुष्टि करती थी।", 0, "कथन (A) और कारण (R) दोनों सही हैं और कारण (R), कथन (A) की सही व्याख्या है।"),
    ("कथन (A): आयताकार मुहरें अपने जटिल पशु चित्रणों के लिए जानी जाती हैं।\nकारण (R): आयताकार मुहरों पर लिपि के अक्षर होते हैं लेकिन पशु आकृतियों का लगभग पूर्ण अभाव होता है।", 3, "कथन (A) गलत है लेकिन कारण (R) सही है। आयताकार मुहरों पर केवल लिपि होती है, पशु नहीं।"),
    ("कथन (A): फेयॉन्स (faience) की मुहरें लुप्त मोम धातु ढलाई द्वारा बनाई जाती थीं।\nकारण (R): फेयॉन्स सिलिका, मिट्टी और गोंद से बना एक चमकीला सिरेमिक पदार्थ है जिसे सांचों में दबाकर बनाया जाता था।", 3, "कथन (A) गलत है लेकिन कारण (R) सही है। फेयॉन्स एक सिरेमिक है, धातु ढलाई नहीं।")
]:
    s1_mastery_hin.append({"type": "Assertion-Reason", "q": q, "opts": hin_ar_opts, "ans": ans, "sol": sol})

# Statement-Based (5)
for q, ans, sol in [
    ("Consider the following statements regarding Harappan seals:\n1. Steatite was the primary raw material, but terracotta, copper, and agate seals were also made.\n2. Inscriptions on seals were painted using black manganese-based pigment.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: inscriptions were carved into the stone (intaglio), not painted."),
    ("Consider the following statements regarding seal functions:\n1. Impressions of seals on clay were used to secure containers of trade goods.\n2. Seals were used as standardized coins to pay wages to state construction laborers.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: seals were not currency or coins."),
    ("Consider the following statements regarding copper tablets:\n1. They show a high degree of standardization in shape and size compared to steatite seals.\n2. They were recovered primarily at Kalibangan and Lothal but are rare at Mohenjo-daro.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: copper tablets are highly concentrated at Mohenjo-daro and Harappa, not Kalibangan/Lothal."),
    ("Consider the following statements regarding seal iconography:\n1. The Unicorn is depicted in profile with a single horn and a censer standard in front of it.\n2. Real animals like tigers, elephants, and lions are depicted in equal quantities on seals.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: lions are completely absent from Harappan seals."),
    ("Consider the following statements regarding rectangular seals:\n1. They are generally flat and lack a pierced boss on their reverse.\n2. They depict complex narrative scenes of deities emerging from Pipal trees.\nWhich of the statements given above is/are correct?", 3, "Neither statement is correct. Rectangular seals carry script only (no narratives) and have a convex reverse with a hole or are flat.")
]:
    s1_mastery_eng.append({"type": "Statement-Based", "q": q, "opts": mcq_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("हड़प्पा मुहरों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. सेलखड़ी प्राथमिक कच्चा माल थी, लेकिन मिट्टी, तांबे और अगेट की मुहरें भी बनाई जाती थीं।\n2. मुहरों पर लेख काले मैंगनीज आधारित पिगमेंट का उपयोग करके रंगे जाते थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि लेख उकेरे जाते थे, रंगे नहीं।"),
    ("मुहरों के कार्यों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. मिट्टी पर मुहरों की छाप का उपयोग व्यापारिक वस्तुओं के पैकेटों को सुरक्षित करने के लिए किया जाता था।\n2. मुहरों का उपयोग निर्माण श्रमिकों को वेतन देने के लिए मानक सिक्कों के रूप में किया जाता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि मुहरें सिक्के नहीं थीं।"),
    ("तांबे की पट्टिकाओं के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. सेलखड़ी की मुहरों की तुलना में इनके आकार और माप में बहुत अधिक मानकीकरण पाया जाता है।\n2. ये मुख्य रूप से कालीबंगन और लोथल से मिली हैं लेकिन मोहनजोदड़ो में दुर्लभ हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि तांबे की पट्टिकाएं मोहनजोदड़ो और हड़प्पा में केंद्रित हैं।"),
    ("मुहरों के रूपांकनों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. यूनिकॉर्न को एक सींग के साथ पार्श्व चित्र में धूप पात्र के सामने खड़ा दिखाया गया है।\n2. बाघ, हाथी और शेर जैसे वास्तविक पशु मुहरों पर समान मात्रा में अंकित हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि शेर मुहरों पर नहीं मिलता।"),
    ("आयताकार मुहरों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. ये आम तौर पर चपटी होती हैं और इनके पीछे छेददार उभार (boss) नहीं होता है।\n2. इन पर पीपल के पेड़ से निकलते देवताओं के जटिल कथात्मक दृश्य बने होते हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 3, "दोनों कथन गलत हैं। आयताकार मुहरों पर केवल लिपि होती है (कोई कहानी नहीं) और पीछे उभार होता है।")
]:
    s1_mastery_hin.append({"type": "Statement-Based", "q": q, "opts": hin_mcq_opts, "ans": ans, "sol": sol})

# Why (3)
for q, sol in [
    ("Why did the Harappan artisans fire their steatite seals in kilns?", "Firing talc-based steatite above 900°C induced a chemical phase change, converting the soft talc mineral into hard enstatite. This significantly increased the durability and hardness of the seals, preventing wear during stamping, and produced a white glazed aesthetic finish."),
    ("Why is the presence of clay sealings at Lothal significant for reconstructing trade practices?", "Lothal sealings retain impressions of packing materials like cords, reeds, and woven mats on their reverse, proving that the stamped clay was applied directly to real merchant bundles. The presence of multiple seal impressions on single sealings suggests administrative check-points or joint trade agreements between different merchants."),
    ("Why did the Harappans carve seal designs in intaglio rather than cameo relief?", "Carving in intaglio (sunken relief) was functionally necessary for stamp seals. When the seal was pressed into wet clay taggings of cargo, the sunken areas produced a raised (positive) relief impression of the animal and script, which was much easier to read and inspect for tampering.")
]:
    s1_mastery_eng.append({"type": "Why", "q": q, "sol": sol})

for q, sol in [
    ("हड़प्पा के शिल्पकार सेलखड़ी की मुहरों को भट्टी में क्यों पकाते थे?", "900 डिग्री सेल्सियस से ऊपर पकाने से सेलखड़ी (talc) में रासायनिक परिवर्तन होता था और यह कठोर एन्सटाइट (enstatite) खनिज में बदल जाती थी। इससे मुहरों की कठोरता और स्थायित्व बढ़ जाता था जिससे वे बार-बार छापने पर घिसती नहीं थीं, साथ ही मुहर को चमकीली सफेद ग्लाइलेज सतह मिलती थी।"),
    ("लोथल में मिट्टी की सील (sealings) की खोज व्यापारिक पद्धतियों के पुनर्निर्माण के लिए क्यों महत्वपूर्ण है?", "लोथल की सील के पीछे की तरफ रस्सियों, चटाइयों और नरकट के निशान मिले हैं, जो साबित करते हैं कि यह गीली मिट्टी सीधे व्यापारियों के पैकेजों की गांठों पर लगाई जाती थी। एक ही सील पर कई मुहरों की छाप मिलना यह दर्शाता है कि सामान को कई अधिकारियों या व्यापारिक गिल्डों द्वारा जांचा जाता था।"),
    ("हड़प्पा वासी मुहर के डिज़ाइनों को उभरी हुई नक्काशी (cameo) के बजाय अंतर्गठित (intaglio) नक्काशी में क्यों तराशते थे?", "मुहर लगाने के उद्देश्य के लिए अंतर्गठित (धँसी हुई) नक्काशी तकनीकी रूप से आवश्यक थी। जब मुहर को गीली मिट्टी पर दबाया जाता था, तो धँसे हुए हिस्सों से मिट्टी ऊपर उठ जाती थी और पशु व लिपि की एक उभरी हुई (सकारात्मक) आकृति बन जाती थी, जिसे पढ़ना और छेड़छाड़ के लिए जांचना आसान होता था।")
]:
    s1_mastery_hin.append({"type": "Why", "q": q, "sol": sol})

# How (3)
for q, sol in [
    ("How did Harappan artisans manufacture a standard square steatite seal?", "Artisans carved the block of soft steatite into a square tab, shaped the raised boss on the reverse, and drilled a suspension hole. Next, they engraved the animal motif and script characters in intaglio on the face using copper chisels or drills. Finally, they coated the seal with a fine talc-based chemical slip and fired it in a high-temperature kiln to harden and glaze it."),
    ("How did the sealings on trade goods protect cargo from tampering?", "Merchants tied their goods with cords, placed a piece of wet clay over the knots, and stamped the clay with their personal seals. Once dried, the clay sealing formed a hard shell over the knot. If anyone tried to open the package, the clay shell would break. Upon arrival at the port (like Lothal), officials inspected the sealings; an intact sealing proved the cargo had not been tampered with in transit."),
    ("How do copper tablets differ from steatite seals in terms of physical construction and engraving?", "Steatite seals were carved out of stone blocks, have a raised boss with a hole on the reverse, and feature deep intaglio engraving. In contrast, copper tablets are thin, flat rectangular metal plates. They have no reverse boss or suspension hole, and their designs/scripts were shallowly engraved or chased into the metal surface, often with text and motifs split between the front and back faces.")
]:
    s1_mastery_eng.append({"type": "How", "q": q, "sol": sol})

for q, sol in [
    ("हड़प्पा के शिल्पकार एक मानक वर्गाकार सेलखड़ी की मुहर का निर्माण कैसे करते थे?", "शिल्पकार पहले सेलखड़ी के चौकोर टुकड़े काटते थे, पीछे छेददार बटन (boss) बनाते थे। फिर तांबे की छेनी या बरमे से मुहर के मुख भाग पर पशु और लिपि को धँसी हुई नक्काशी (intaglio) में उकेरते थे। इसके बाद मुहर पर पानी व पिसे हुए टैल्क का घोल लगाते थे और अंत में इसे उच्च तापमान की भट्टी में पकाकर चमकीला व अत्यंत कठोर बनाते थे।"),
    ("व्यापारिक वस्तुओं पर लगी मिट्टी की मुहरें माल को छेड़छाड़ से कैसे बचाती थीं?", "व्यापारी सामान को रस्सियों से बांधते थे, गांठ पर गीली मिट्टी का लेप लगाते थे और उस पर अपनी व्यक्तिगत मुहर दबा देते थे। सूखने पर मिट्टी एक सख्त खोल बन जाती थी। यदि कोई पैकेट खोलने का प्रयास करता तो वह मिट्टी का खोल टूट जाता। गंतव्य पर अधिकारी सील की जांच करते थे; साबुत सील यह प्रमाणित करती थी कि मार्ग में माल सुरक्षित रहा है।"),
    ("शारीरिक बनावट और नक्काशी के मामले में तांबे की पट्टिकाएं सेलखड़ी की मुहरों से कैसे भिन्न थीं?", "सेलखड़ी की मुहरें पत्थर से बनती थीं, उनके पीछे छेददार गोल बटन होता था और उन पर गहरी अंतर्गठित नक्काशी होती थी। इसके विपरीत, तांबे की पट्टिकाएं धातु की पतली और चपटी आयताकार प्लेटें थीं। इनके पीछे कोई बटन या छेद नहीं होता था और इन पर आकृतियां/लेख धातु की सतह पर बहुत उथली नक्काशी द्वारा बनाए जाते थे, जो अक्सर दोनों तरफ फैले होते थे।")
]:
    s1_mastery_hin.append({"type": "How", "q": q, "sol": sol})

# Case Study (3)
for q, sol in [
    ("Case Study: Excavations at Lothal revealed a warehouse containing over 90 clay sealings, many showing impressions of cords and packing mats, but only a few steatite seals were found in the same structure. Analyze what this distribution indicates about Lothal's economic activities.", "This indicates that Lothal was primarily an active packaging, shipping, and receiving depot rather than a center of seal production. The abundance of sealings on packing materials proves goods were imported, inspected, and repackaged there, while the scarcity of seals shows that merchants did not leave their stamp tools behind, carrying them as personal administrative credentials."),
    ("Case Study: Mesopotamian clay tablets record trade transactions with a land called 'Meluhha' (generally identified as the Indus Valley), and Harappan square seals have been found in Ur and Susa. Contrast the sealing systems of the two civilisations to show how this trade was managed.", "Mesopotamia used cylinder seals rolled over clay tablets to sign contracts, while the Indus used square stamp seals pressed into clay taggings of packages. The discovery of Harappan-style square seals in Mesopotamian cities proves that Harappan merchants lived or traded directly in Mesopotamia, maintaining their local stamp-marking system to authenticate cargo and verify ownership in foreign ports."),
    ("Case Study: Copper tablets have been found in large quantities at Mohenjo-daro and Harappa, but are virtually absent at small rural settlements like Allahdino or Chanhu-daro. What does this spatial distribution suggest about their function?", "This suggest that copper tablets were linked to complex administrative, elite, or urban functions restricted to the primary capitals. If they were simple amulets worn by everyone, they would be distributed evenly. Their concentration in the major cities suggests they were tokens of citizenship, official guild passes, or administrative credentials used by the urban trade bureaucracy.")
]:
    s1_mastery_eng.append({"type": "Case Study", "q": q, "sol": sol})

for q, sol in [
    ("केस स्टडी: लोथल के एक गोदाम से 90 से अधिक मिट्टी की सीलें (sealings) मिली हैं, जिनमें से कई पर रस्सी और चटाई के निशान हैं, लेकिन उसी गोदाम से सेलखड़ी की मुहरें बहुत कम मिली हैं। यह वितरण लोथल की आर्थिक गतिविधियों के बारे में क्या दर्शाता है?", "यह दर्शाता है कि लोथल मुख्य रूप से माल पैक करने, भेजने और प्राप्त करने का एक सक्रिय डिपो था, न कि मुहर निर्माण का केंद्र। पैकिंग सामग्री पर लगी इतनी सीलें साबित करती हैं कि यहाँ माल आयात किया जाता था, गोदाम में स्टोर होता था और उसकी जांच की जाती थी। मुहरों की कमी दर्शाती है कि व्यापारी मुहरों को व्यक्तिगत पहचान पत्र के रूप में अपने पास रखते थे और उन्हें छोड़कर नहीं जाते थे।"),
    ("केस स्टडी: मेसोपोटामिया की मिट्टी की पट्टिकाएं 'मेलुहा' (सिंधु घाटी) के साथ व्यापारिक लेन-देन दर्ज करती हैं, और उर व सूसा से हड़प्पा शैली की वर्गाकार मुहरें मिली हैं। दोनों सभ्यताओं की मुहर प्रणालियों की तुलना करके बताएं कि यह व्यापार कैसे प्रबंधित होता था।", "मेसोपोटामिया में समझौतों पर हस्ताक्षर करने के लिए मिट्टी पर बेलनाकार मुहरें घुमाई (roll) जाती थीं, जबकि सिंधु घाटी में पैकेटों पर वर्गाकार मुहरें दबाई (stamp) जाती थीं। मेसोपोटामिया में हड़प्पा मुहरों का मिलना प्रमाणित करता है कि हड़प्पा के व्यापारी वहां रहते थे या सीधे व्यापार करते थे, और विदेशी बंदरगाहों में सामान की प्रामाणिकता साबित करने के लिए अपनी वर्गाकार मुहर प्रणाली का उपयोग करते थे।"),
    ("केस स्टडी: मोहनजोदड़ो और हड़प्पा से भारी मात्रा में तांबे की पट्टिकाएं मिली हैं, लेकिन अल्लादीनो या चन्हुदड़ो जैसे छोटे ग्रामीण या अर्ध-शहरी स्थलों पर ये लगभग पूरी तरह अनुपस्थित हैं। यह स्थानिक वितरण उनके कार्य के बारे में क्या संकेत देता है?", "यह संकेत देता है कि तांबे की पट्टिकाएं जटिल प्रशासनिक, शहरी या संभ्रांत वर्ग की गतिविधियों से जुड़ी थीं जो केवल मुख्य राजधानियों तक सीमित थीं। यदि ये आम जनता के पहनने के साधारण ताबीज होते, तो ग्रामीण क्षेत्रों में भी मिलते। बड़े शहरों में इनकी सघनता दर्शाती है कि ये नागरिकता के टोकन, व्यापारिक गिल्ड के पास या शहरी प्रशासनिक अधिकारियों के पहचान पत्र थे।")
]:
    s1_mastery_hin.append({"type": "Case Study", "q": q, "sol": sol})

# Teach Concept (3)
for q, sol in [
    ("Teach the concept of 'enstatite transformation' in Harappan seal manufacturing, explaining why it was a technological milestone.", "Enstatite transformation refers to the process of heating soft steatite (talc, which is a hydrous magnesium silicate) above 900°C. Heating drives out water, recrystallizing the talc into enstatite (anhydrous magnesium silicate), which is much harder and more durable. This allowed Harappan craftsmen to easily carve intricate scripts and animals on the soft stone first, and then bake it to become hard enough to stamp thousands of clay packages without wearing down. This represents a sophisticated milestone in pyro-technology and material science."),
    ("Explain the difference between a 'seal' and a 'sealing' to a student, using examples from Lothal's archaeology.", "A 'seal' is the active carving tool, usually made of hard fired steatite, featuring designs in reverse (intaglio). A 'sealing' is the passive clay impression left when the seal is pressed onto wet clay. For example, at Lothal, only a few steatite 'seals' (the tools) were found, but over 90 clay 'sealings' (the cargo stamps with rope marks on the back) were recovered from the burnt warehouse, showing that sealings are the physical proof of commercial shipments."),
    ("Teach the administrative and commercial role of the 'Unicorn Seal with standard' in the Harappan trade guild system.", "The Unicorn seal depicts a mythical animal and a censer/standard, which is the most common motif (found on ~60-70% of seals). This high standardization suggests that the Unicorn was the official emblem of the dominant trade guild, state bureaucracy, or ruling merchant class. The censer standard represents a religious or state cult object. When stamped on goods, it verified that the cargo conformed to official weights and municipal trade regulations, acting as a mark of quality control and administrative authority.")
]:
    s1_mastery_eng.append({"type": "Teach Concept", "q": q, "sol": sol})

for q, sol in [
    ("हड़प्पा मुहर निर्माण में 'एन्सटाइट परिवर्तन' की अवधारणा को समझाएं और बताएं कि यह एक तकनीकी मील का पत्थर क्यों था।", "एन्सटाइट परिवर्तन का तात्पर्य सेलखड़ी (जो एक नरम जलयोजित मैग्नीशियम सिलिकेट है) को 900 डिग्री सेल्सियस से ऊपर गर्म करने की प्रक्रिया से है। गर्म करने से इसका जल बाहर निकल जाता है और यह निर्जल मैग्नीशियम सिलिकेट यानी एन्सटाइट (enstatite) में बदल जाता है, जो अत्यंत कठोर होता है। इससे शिल्पकारों को पहले नरम पत्थर पर बारीक आकृतियां उकेरने की सुविधा मिलती थी और फिर पकाने के बाद वह मुहर इतनी सख्त हो जाती थी कि हजारों बार मिट्टी पर दबाने पर भी घिसती नहीं थी। यह पदार्थ विज्ञान का एक अद्भुत ऐतिहासिक उदाहरण है।"),
    ("एक छात्र को 'मुहर' (seal) और 'सील/मिट्टी की छाप' (sealing) के बीच का अंतर लोथल के पुरातात्विक साक्ष्यों का उदाहरण देकर समझाएं।", "मुहर (seal) वह सक्रिय नक्काशीदार उपकरण (जैसे सेलखड़ी का ठप्पा) है जिसका उपयोग छाप लगाने के लिए किया जाता था, और इस पर उल्टे अक्षर खुदे होते थे। सील (sealing) वह गीली मिट्टी पर बनी छाप है जो मुहर को दबाने से बनती है। उदाहरण के लिए, लोथल से केवल कुछ सेलखड़ी की 'मुहरें' (उपकरण) मिली हैं, लेकिन जले हुए गोदाम से 90 से अधिक मिट्टी की 'सीलें' (पीछे रस्सी के निशान वाली छापें) प्राप्त हुई हैं, जो व्यापारिक पारगमन का प्रमाण हैं।"),
    ("हड़प्पा व्यापार संघ प्रणाली में 'धूप पात्र के साथ एक सींग वाले पशु (Unicorn) की मुहर' की प्रशासनिक और व्यावसायिक भूमिका को स्पष्ट करें।", "यूनिकॉर्न मुहर सबसे आम है जो लगभग 60-70% मुहरों पर मिलती है। यह अत्यधिक मानकीकरण दर्शाता है कि यूनिकॉर्न सिंधु घाटी के सबसे शक्तिशाली व्यापारी संघ, राज्य प्रशासन या शासक वर्ग का आधिकारिक प्रतीक चिन्ह (emblem) था। सामने रखा धूप पात्र एक धार्मिक या राजकीय शुद्धि का प्रतीक है। जब इसे माल पर लगाया जाता था, तो यह प्रमाणित करता था कि माल आधिकारिक बाटों और सरकारी नियमों के अनुकूल है, जो गुणवत्ता नियंत्रण और प्रशासनिक स्वीकृति का सूचक था।")
]:
    s1_mastery_hin.append({"type": "Teach Concept", "q": q, "sol": sol})


# =========================================================================
# SECTION 2: STONE AND BRONZE SCULPTURES
# =========================================================================
s2_mastery_eng = []
s2_mastery_hin = []

# MCQ (5)
for q, opts, ans, sol in [
    ("The bronze 'Dancing Girl' sculpture from Mohenjo-daro is depicted in which of the following body postures?", ["Tribhanga (triple-bend)", "Samabhanga (straight standing)", "Padmasana (seated yogic pose)", "Alidhasana (warrior stance)"], 0, "The Dancing Girl stands in the relaxed Tribhanga (triple-bend) posture."),
    ("The metallurgical process of 'cire perdue' used to cast the Dancing Girl is commonly known as:", ["Lost-wax casting", "Cold hammering", "Sand casting", "Electroplating"], 0, "Cire perdue is the French term for lost-wax casting."),
    ("Which of the following decorative patterns is carved on the shawl of the steatite 'Priest-King' bust?", ["Trefoil", "Chevron", "Rosette", "Palmette"], 0, "The Priest-King's shawl features a trefoil (three-lobed clover) pattern."),
    ("At which Harappan site was the naturalistic red sandstone male torso with socket holes excavated?", ["Harappa", "Mohenjo-daro", "Dholavira", "Lothal"], 0, "The red sandstone male torso was discovered at Harappa."),
    ("The socket holes at the neck and shoulders of the Harappan red sandstone male torso indicate which technical achievement?", ["Use of detachable, modular limbs and head", "Attachment of iron reinforcement bars", "Infiltration of Mesopotamian bronze pins", "Marks left by core vents during casting"], 0, "The socket holes allowed the head and arms to be made separately and attached as detachable parts.")
]:
    s2_mastery_eng.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("मोहनजोदड़ो से प्राप्त कांस्य की 'नर्तकी' (Dancing Girl) को निम्नलिखित में से किस शारीरिक मुद्रा में दर्शाया गया है?", ["त्रिभंग मुद्रा (Tribhanga)", "समभंग मुद्रा (Samabhanga)", "पद्मासन (Padmasana)", "आलीढ़ासन (Alidhasana)"], 0, "कांस्य नर्तकी शिथिल त्रिभंग (शरीर में तीन झुकाव) मुद्रा में खड़ी है।"),
    ("नर्तकी को ढालने के लिए प्रयुक्त धातु कर्म की 'cire perdue' प्रक्रिया को आमतौर पर किस नाम से जाना जाता है?", ["लुप्त मोम ढलाई (Lost-wax casting)", "शीत हथौड़ा प्रहार (Cold hammering)", "रेत ढलाई (Sand casting)", "विद्युत लेपन (Electroplating)"], 0, "Cire perdue लुप्त मोम ढलाई (lost-wax casting) का फ्रांसीसी नाम है।"),
    ("सेलखड़ी के 'पुरोहित राजा' (Priest-King) की शाल पर निम्नलिखित में से कौन सा सजावटी पैटर्न खुदा हुआ है?", ["तिपतिया (Trefoil)", "शेवरॉन (Chevron)", "गुलाब (Rosette)", "ताड़-पत्ता (Palmette)"], 0, "पुरोहित राजा की शाल पर तिपतिया (तीन पत्तियों वाला) डिज़ाइन बना हुआ है।"),
    ("जोड़दार सॉकेट छेद वाला अत्यंत प्राकृतिक लाल बलुआ पत्थर का पुरुष धड़ किस हड़प्पा स्थल से मिला था?", ["हड़प्पा", "मोहनजोदड़ो", "धोलावीरा", "लोथल"], 0, "लाल बलुआ पत्थर का धड़ हड़प्पा से प्राप्त हुआ था।"),
    ("हड़प्पा के लाल बलुआ पत्थर के पुरुष धड़ के गर्दन और कंधों पर बने सॉकेट छेद किस तकनीकी उपलब्धि को दर्शाते हैं?", ["अलग होने वाले जोड़दार अंगों (detachable limbs) का उपयोग", "लोहे की छड़ें जोड़ने की व्यवस्था", "मेसोपोटामिया के पीतल के पिन लगाने के निशान", "ढलाई के दौरान हवा निकलने के छेद"], 0, "सॉकेट छेद दर्शाते हैं कि सिर और हाथ अलग से बनाकर जोड़े जा सकते थे।")
]:
    s2_mastery_hin.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# Multiple Correct MCQ (5)
for q, opts, ans, sol in [
    ("Select the features of the bronze 'Dancing Girl' from Mohenjo-daro: (Select all that apply)", ["Cast using lost-wax technique", "Stands in Tribhanga pose", "Left arm loaded with 24-25 bangles", "Found inside the Citadel granary"], [0, 1, 2], "The Dancing Girl is a lost-wax bronze in tribhanga with 24-25 left-arm bangles. It was found in a residential area, not the granary."),
    ("Which of the following are details carved on the Priest-King bust? (Select all that apply)", ["Trefoil pattern on the shawl", "Fillet headband with a central disc", "Right armlet matching the fillet", "Stitched tunic with buttons"], [0, 1, 2], "The Priest-King has a trefoil shawl, fillet headband, and armlet. No stitched buttoned tunic is depicted."),
    ("Identify stone sculptures excavated at Harappa: (Select all that apply)", ["Red sandstone male torso", "Grey steatite male dancer figurine", "Steatite Priest-King bust", "Bronze Dancing Girl"], [0, 1], "The red sandstone torso and grey dancer are from Harappa. The Priest-King and Dancing Girl are from Mohenjo-daro."),
    ("Select the technical details of lost-wax casting in the Indus Valley: (Select all that apply)", ["Wax model is melted and drained out of a heated clay shell", "Molten metal is poured into the hollow clay mold", "Clay mold is broken after the metal cools", "Iron wires were used as core pins in all castings"], [0, 1, 2], "Lost-wax involves melting wax, pouring metal into the hollow clay, and breaking it. Iron was unknown."),
    ("Which of the following details support the meditative interpretation of the Priest-King? (Select all that apply)", ["Eyes are half-closed, looking at the tip of the nose", "Hands are folded in an attitude of prayer", "Facial expression shows complete serenity", "Wearing a sacred thread over his right shoulder"], [0, 2], "Meditative interpretation is based on half-closed eyes looking down and serene expression. No hands or sacred thread are depicted on the bust.")
]:
    s2_mastery_eng.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("मोहनजोदड़ो की कांस्य 'नर्तकी' की विशेषताओं का चयन करें: (सभी लागू विकल्प चुनें)", ["लुप्त मोम तकनीक से निर्मित", "त्रिभंग मुद्रा में खड़ी", "बाईं बांह चूड़ियों (24-25) से पूरी तरह ढकी", "दुर्ग के अन्नागार के भीतर से प्राप्त"], [0, 1, 2], "नर्तकी कांस्य की लघु मूर्ति है, त्रिभंग मुद्रा में है और उसकी बाईं बांह चूड़ियों से भरी है। यह आवासीय क्षेत्र से मिली थी।"),
    ("पुरोहित राजा की मूर्ति पर उकेरे गए विवरणों में कौन से शामिल हैं? (सभी लागू विकल्प चुनें)", ["शाल पर तिपतिया डिज़ाइन", "सिर पर चक्रदार पट्टी (fillet)", "दाहिनी बांह पर गोल बाजूबंद", "बटन वाला सिला हुआ कुर्ता"], [0, 1, 2], "पुरोहित राजा पर तिपतिया शाल, सिर की पट्टी और बाजूबंद बने हैं। बटन वाला कुर्ता नहीं है।"),
    ("हड़प्पा से प्राप्त प्रस्तर मूर्तियों की पहचान करें: (सभी लागू विकल्प चुनें)", ["लाल बलुआ पत्थर का पुरुष धड़", "धूसर पत्थर का पुरुष नर्तक", "सेलखड़ी का पुरोहित राजा", "कांस्य नर्तकी"], [0, 1], "लाल बलुआ पत्थर का धड़ और धूसर नर्तक हड़प्पा से मिले हैं। पुरोहित राजा और नर्तकी मोहनजोदड़ो से मिले हैं।"),
    ("सिंधु घाटी की लुप्त मोम ढलाई तकनीक के चरणों का चयन करें: (सभी लागू विकल्प चुनें)", ["मिट्टी के सांचे को गर्म करके मोम पिघलाकर बाहर निकाला जाता था", "खाली मिट्टी के सांचे में पिघला हुआ कांसा भरा जाता था", "धातु ठंडी होने पर मिट्टी का सांचा तोड़ दिया जाता था", "सभी ढलाइयों में लोहे के तारों का उपयोग किया जाता था"], [0, 1, 2], "लुप्त मोम तकनीक में मोम पिघलाया जाता था, धातु भरी जाती थी और फिर सांचा तोड़ा जाता था। लोहे का ज्ञान नहीं था।"),
    ("कौन से विवरण पुरोहित राजा के ध्यानमग्न होने की व्याख्या का समर्थन करते हैं? (सभी लागू विकल्प चुनें)", ["आंखें आधी बंद हैं, जो नाक के अग्रभाग पर केंद्रित दिखती हैं", "हाथ प्रार्थना की मुद्रा में जुड़े हैं", "चेहरे का भाव पूर्ण शांति दर्शाता है", "दाहिने कंधे पर जनेऊ पहना हुआ है"], [0, 2], "ध्यानमग्न व्याख्या उनके अधखुले नेत्रों और शांत चेहरे के भाव पर आधारित है। मूर्ति में हाथ नहीं हैं।")
]:
    s2_mastery_hin.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# True/False (8)
for q, ans, sol in [
    ("The bronze Dancing Girl wears a total of 24 to 25 bangles on her right arm.", False, "False. She wears them on her left arm; her right arm has only 4 bangles."),
    ("The Lost-Wax technique was only used to cast copper weapons and never used for art objects.", False, "False. It was used extensively for artistic bronze figures like the Dancing Girl and animals."),
    ("The Priest-King shawl was originally inlaid with red pigment in the trefoil patterns.", True, "True. Red clay or paste was used to fill the trefoil carvings."),
    ("The red sandstone male torso has socket holes, suggesting it had detachable arms and head.", True, "True. Socket holes at neck and shoulders show it was modular."),
    ("Both the Dancing Girl and the Priest-King were discovered at Harappa.", False, "False. Both were discovered at Mohenjo-daro."),
    ("The bronze charging bull from Kalibangan is characterized by its dynamic, realistic posture.", True, "True. The Kalibangan bull is known for its highly expressive charging stance."),
    ("The Priest-King bust depicts a figure with a thick mustache and clean-shaven beard.", False, "False. He has a neatly trimmed beard and a shaved upper lip (no mustache)."),
    ("Harappan stone sculptures are very large, monumental statues measuring over two meters tall.", False, "False. They are tiny; the Priest-King is 17.5 cm and the male torso is 9.5 cm.")
]:
    s2_mastery_eng.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("कांस्य नर्तकी अपने दाहिने हाथ में कुल 24 से 25 चूड़ियाँ पहनती है।", False, "असत्य। वह अपनी बाईं बांह में चूड़ियाँ पहनती है; दाहिनी बांह पर केवल 4 चूड़ियाँ/बाजूबंद हैं।"),
    ("लुप्त मोम तकनीक का उपयोग केवल तांबे के हथियार ढालने के लिए होता था, कलाकृतियों के लिए कभी नहीं।", False, "असत्य। इसका उपयोग नर्तकी और पशुओं जैसी कलात्मक मूर्तियों के लिए होता था।"),
    ("पुरोहित राजा की शाल के तिपतिया डिज़ाइनों में मूल रूप से लाल रंग भरा गया था।", True, "सत्य। तिपतिया नक्काशी में लाल रंग का पेस्ट भरा गया था।"),
    ("लाल बलुआ पत्थर के पुरुष धड़ में सॉकेट छेद हैं, जो दर्शाता है कि उसके हाथ और सिर अलग हो सकते थे।", True, "सत्य। गर्दन और कंधों पर बने सॉकेट छेद जोड़दार अंगों को दर्शाते हैं।"),
    ("नर्तकी और पुरोहित राजा दोनों की मूर्तियाँ हड़प्पा से खोजी गई थीं।", False, "असत्य। दोनों मोहनजोदड़ो से खोजी गई थीं।"),
    ("कालीबंगन से प्राप्त कांस्य का आक्रामक सांड अपनी गतिशील और यथार्थवादी मुद्रा के लिए जाना जाता है।", True, "सत्य। कालीबंगन का सांड अत्यंत सजीव आक्रामक मुद्रा में है।"),
    ("पुरोहित राजा की मूर्ति में घनी मूंछें और साफ-सुथरी दाढ़ी दिखाई गई है।", False, "असत्य। इसमें दाढ़ी करीने से संवारी हुई है और ऊपरी होंठ साफ (मूंछ रहित) है।"),
    ("हड़प्पा की प्रस्तर मूर्तियाँ बहुत बड़ी हैं, जिनकी ऊँचाई दो मीटर से अधिक है।", False, "असत्य। ये अत्यंत लघु मूर्तियाँ हैं; पुरोहित राजा 17.5 सेमी और धड़ 9.5 सेमी का है।")
]:
    s2_mastery_hin.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

# Fill in the Blank (8)
for q, ans, sol in [
    ("The bronze Dancing Girl is depicted standing in the relaxed ___________ pose.", "tribhanga", "She stands in the triple-bend posture (tribhanga)."),
    ("The metallurgical lost-wax process is also known as ___________.", "cire perdue", "Cire perdue is the French term for lost-wax casting."),
    ("The Priest-King shawl is carved with a three-lobed pattern called ___________.", "trefoil", "The pattern is a trefoil clover shape."),
    ("The Priest-King bust is made of the soft stone mineral known as ___________.", "steatite", "It was carved from steatite (soapstone)."),
    ("The modular red sandstone male torso was excavated at the site of ___________.", "Harappa", "The red sandstone torso is from Harappa."),
    ("To attach modular head and arms, the sandstone torso features drilled ___________ holes.", "socket", "Socket holes were drilled at the neck and shoulders."),
    ("The Dancing Girl wears 24 to 25 bangles on her left arm and a triple-drop ___________ on her neck.", "pendant", "She wears a necklace with three drop-shaped pendants."),
    ("The metallic alloy bronze is produced by mixing copper with ___________.", "tin", "Tin is the primary alloying element with copper to make bronze.")
]:
    s2_mastery_eng.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("कांस्य नर्तकी को शिथिल खड़ी मुद्रा में दिखाया गया है जिसे ___________ कहा जाता है।", "त्रिभंग", "इसे त्रिभंग (tribhanga) मुद्रा कहा जाता है।"),
    ("लुप्त मोम ढलाई की धातु कर्म प्रक्रिया को फ्रांसीसी में ___________ भी कहा जाता है।", "cire perdue", "इसे cire perdue (लुप्त मोम) कहा जाता है।"),
    ("पुरोहित राजा की शाल पर बने तीन पत्तियों वाले डिज़ाइन को ___________ कहा जाता है।", "तिपतिया", "इसे तिपतिया (trefoil) डिज़ाइन कहा जाता है।"),
    ("पुरोहित राजा की मूर्ति ___________ नामक मुलायम पत्थर खनिज से बनाई गई है।", "सेलखड़ी", "यह सेलखड़ी (steatite) पत्थर से बनी है।"),
    ("अंग जोड़ने वाले सॉकेट छेद वाला लाल बलुआ पत्थर का पुरुष धड़ ___________ नामक स्थल से मिला था।", "हड़प्पा", "यह धड़ हड़प्पा से प्राप्त हुआ था।"),
    ("सिर और हाथ जोड़ने के लिए, लाल बलुआ पत्थर के धड़ में गोल ___________ छेद बनाए गए थे।", "सॉकेट", "कंधों और गर्दन पर सॉकेट (socket) छेद बने हैं।"),
    ("नर्तकी अपनी बाईं बांह में 24-25 चूड़ियां और गले में तीन लटकन वाला ___________ पहनती है।", "हार", "वह गले में तीन लटकन (pendant) वाला हार पहनती है।"),
    ("कांसा (bronze) बनाने के लिए तांबे के साथ मुख्य रूप से ___________ धातु को मिलाया जाता था।", "टिन", "तांबे और टिन (tin) के मिश्रण से कांसा बनता था।")
]:
    s2_mastery_hin.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

# Match the Following (3)
for q, items, opts, sol in [
    (
        "Match the sculptures with their discovery locations:",
        [{"left": "I. Priest-King Bust", "key": "A"}, {"left": "II. Red Sandstone Male Torso", "key": "B"}, {"left": "III. Bronze Charging Bull", "key": "C"}],
        [{"val": "A", "text": "A. Mohenjo-daro Citadel"}, {"val": "B", "text": "B. Harappa Mound"}, {"val": "C", "text": "C. Kalibangan residential area"}],
        "Priest-King is from Mohenjo-daro; Male Torso is from Harappa; Bronze Bull is from Kalibangan."
    ),
    (
        "Match the figures with their primary material composition:",
        [{"left": "I. Dancing Girl figurine", "key": "A"}, {"left": "II. Priest-King bust", "key": "B"}, {"left": "III. Anatomical Male Torso", "key": "C"}],
        [{"val": "A", "text": "A. Copper-tin bronze alloy"}, {"val": "B", "text": "B. Steatite (talcose soapstone)"}, {"val": "C", "text": "C. Red Sandstone"}],
        "Dancing girl is bronze; Priest-King is steatite; Male Torso is red sandstone."
    ),
    (
        "Match the stylistic postures with the respective sculptures:",
        [{"left": "I. Tribhanga pose", "key": "A"}, {"left": "II. Seated Yogic posture", "key": "B"}, {"left": "III. Formal static posture", "key": "C"}],
        [{"val": "A", "text": "A. Bronze Dancing Girl"}, {"val": "B", "text": "B. Pashupati Seal figure"}, {"val": "C", "text": "C. Steatite Priest-King bust"}],
        "Tribhanga is Dancing Girl; Yogic pose is Pashupati Seal; Formal static posture is Priest-King."
    )
]:
    s2_mastery_eng.append({"type": "Match the Following", "q": q, "items": items, "options": opts, "sol": sol})

for q, items, opts, sol in [
    (
        "मूर्तियों को उनके प्राप्ति स्थलों से सुमेलित करें:",
        [{"left": "I. पुरोहित राजा की प्रतिमा", "key": "A"}, {"left": "II. लाल बलुआ पत्थर का पुरुष धड़", "key": "B"}, {"left": "III. कांस्य आक्रामक सांड", "key": "C"}],
        [{"val": "A", "text": "A. मोहनजोदड़ो का दुर्ग"}, {"val": "B", "text": "B. हड़प्पा का टीला"}, {"val": "C", "text": "C. कालीबंगन का आवासीय क्षेत्र"}],
        "पुरोहित राजा मोहनजोदड़ो से मिले हैं; पुरुष धड़ हड़प्पा से मिला है; कांस्य सांड कालीबंगन से प्राप्त हुआ है।"
    ),
    (
        "आकृतियों को उनकी प्राथमिक पत्थर या धातु संरचना से सुमेलित करें:",
        [{"left": "I. नर्तकी की मूर्ति", "key": "A"}, {"left": "II. पुरोहित राजा की अर्ध-प्रतिमा", "key": "B"}, {"left": "III. मांसपेशियों वाला पुरुष धड़", "key": "C"}],
        [{"val": "A", "text": "A. तांबा-टिन कांस्य मिश्र धातु"}, {"val": "B", "text": "B. सेलखड़ी (Steatite)"}, {"val": "C", "text": "C. लाल बलुआ पत्थर (Red Sandstone)"}],
        "नर्तकी कांसे की है; पुरोहित राजा सेलखड़ी के हैं; पुरुष धड़ लाल बलुआ पत्थर का है।"
    ),
    (
        "शारीरिक मुद्राओं को संबंधित मूर्तियों से सुमेलित करें:",
        [{"left": "I. त्रिभंग मुद्रा", "key": "A"}, {"left": "II. योगासन ध्यान मुद्रा", "key": "B"}, {"left": "III. औपचारिक कठोर मुद्रा", "key": "C"}],
        [{"val": "A", "text": "A. कांस्य नर्तकी"}, {"val": "B", "text": "B. पशुपति मुहर की आकृति"}, {"val": "C", "text": "C. सेलखड़ी पुरोहित राजा प्रतिमा"}],
        "त्रिभंग नर्तकी की है; योगासन पशुपति मुहर का है; औपचारिक कठोर मुद्रा पुरोहित राजा की है।"
    )
]:
    s2_mastery_hin.append({"type": "Match the Following", "q": q, "items": items, "options": opts, "sol": sol})

# One-Liner (8)
for q, sol in [
    ("Where was the bronze Dancing Girl discovered?", "Mohenjo-daro."),
    ("Name the casting process used for Harappan bronzes.", "Lost-wax casting (cire perdue)."),
    ("Which posture is the Dancing Girl depicted in?", "Tribhanga (triple-bend) posture."),
    ("What stone is the Priest-King bust carved from?", "Steatite (soapstone)."),
    ("What pattern is carved on the Priest-King's shawl?", "Trefoil pattern."),
    ("Where was the red sandstone male torso discovered?", "Harappa."),
    ("What was the purpose of the socket holes in the red sandstone torso?", "To attach a detachable, modular head and arms."),
    ("True or False: The Priest-King has a long mustache and clean-shaven beard.", "False (he has a neatly groomed beard and a shaved upper lip/no mustache).")
]:
    s2_mastery_eng.append({"type": "One-Liner", "q": q, "sol": sol})

for q, sol in [
    ("कांस्य नर्तकी की मूर्ति कहाँ खोजी गई थी?", "मोहनजोदड़ो।"),
    ("हड़प्पा कांस्य मूर्तियों के निर्माण के लिए किस ढलाई प्रक्रिया का उपयोग किया जाता था?", "लुप्त मोम ढलाई (lost-wax casting / cire perdue)।"),
    ("कांस्य नर्तकी को किस शारीरिक मुद्रा में खड़ा दिखाया गया है?", "त्रिभंग (Tribhanga) मुद्रा में।"),
    ("पुरोहित राजा की प्रतिमा किस पत्थर से तराशी गई है?", "सेलखड़ी (steatite) पत्थर से।"),
    ("पुरोहित राजा की शाल पर कौन सा पैटर्न उकेरा गया है?", "तिपतिया (trefoil) पैटर्न।"),
    ("लाल बलुआ पत्थर का पुरुष धड़ कहाँ खोजा गया था?", "हड़प्पा।"),
    ("लाल बलुआ पत्थर के धड़ में सॉकेट छेदों का क्या उद्देश्य था?", "अलग होने वाले सिर और हाथों को जोड़ना।"),
    ("सत्य या असत्य: पुरोहित राजा की मूर्ति में लंबी मूंछें और साफ-सुथरी दाढ़ी दिखाई गई है।", "असत्य (उनकी दाढ़ी करीने से संवारी हुई है और ऊपरी होंठ साफ है)।")
]:
    s2_mastery_hin.append({"type": "One-Liner", "q": q, "sol": sol})

# Assertion-Reason (8)
for q, ans, sol in [
    ("Assertion (A): The bronze Dancing Girl represents a masterpiece of early metallurgy.\nReason (R): She was cast using the Lost-Wax technique, which requires heating a clay mold to drain melted wax.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): The Priest-King bust is carved from hard granite.\nReason (R): Granite was easily available in the alluvial plains of the Indus River.", 4, "Both A and R are false. The Priest-King is steatite (soft soapstone) and granite was not available locally in the plains."),
    ("Assertion (A): The red sandstone male torso shows a modular construction method.\nReason (R): It features drilled socket holes at the neck and shoulders for attaching detachable head and limbs.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): The Dancing Girl wears 24-25 bangles on her right arm.\nReason (R): Heavy arm jewelry was worn only by male priests in Harappan society.", 4, "Both A and R are false. She wears 24-25 bangles on her left arm, and arm jewelry was widely worn by women."),
    ("Assertion (A): Trefoil designs on the Priest-King's shawl indicate contact with West Asia.\nReason (R): Similar trefoil patterns are associated with royal and divine clothing in Mesopotamia and Egypt.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): The charging bull from Kalibangan is a terracotta toy.\nReason (R): Terracotta toys are modeled by hand and depict moving parts.", 3, "A is false but R is true. The Kalibangan charging bull is made of bronze, not terracotta."),
    ("Assertion (A): The grey stone dancer from Harappa has socket holes.\nReason (R): The socket holes allowed the attachable head and arms to rotate during religious plays.", 2, "A is true but R is false. While it has socket holes, there is no proof they were made to rotate during plays."),
    ("Assertion (A): Harappan stone sculptures were carved inside large temples.\nReason (R): Extensive stone quarries have been discovered in Mohenjo-daro's Citadel.", 4, "Both A and R are false. No temples have been found, and there are no stone quarries at Mohenjo-daro as the site is on alluvial clay.")
]:
    s2_mastery_eng.append({"type": "Assertion-Reason", "q": q, "opts": ar_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("कथन (A): कांस्य नर्तकी प्रारंभिक धातु कर्म का एक उत्कृष्ट नमूना है।\nकारण (R): इसे लुप्त मोम तकनीक से ढाला गया था, जिसमें मोम पिघलाकर बाहर निकालने के लिए मिट्टी के सांचे को गर्म करना पड़ता था।", 0, "कथन (A) और कारण (R) दोनों सही हैं और कारण (R), कथन (A) की सही व्याख्या है।"),
    ("कथन (A): पुरोहित राजा की प्रतिमा कठोर ग्रेनाइट से तराशी गई है।\nकारण (R): सिंधु नदी के मैदानी इलाकों में ग्रेनाइट आसानी से उपलब्ध था।", 4, "कथन (A) और कारण (R) दोनों गलत हैं। पुरोहित राजा सेलखड़ी के हैं, और मैदानी इलाकों में ग्रेनाइट नहीं मिलता।"),
    ("कथन (A): लाल बलुआ पत्थर का पुरुष धड़ एक जोड़दार (modular) निर्माण विधि को दर्शाता है।\nकारण (R): इसमें सिर और हाथ जोड़ने के लिए गर्दन और कंधों पर सॉकेट छेद बने हैं।", 0, "कथन (A) और कारण (R) दोनों सही हैं और कारण (R), कथन (A) की सही व्याख्या है।"),
    ("कथन (A): नर्तकी अपने दाहिने हाथ में 24-25 चूड़ियाँ पहनती है।\nकारण (R): हड़प्पा समाज में भारी बाजूबंद केवल पुरुष पुरोहितों द्वारा पहने जाते थे।", 4, "कथन (A) और कारण (R) दोनों गलत हैं। वह बाएं हाथ में 24-25 चूड़ियां पहनती है, और ये आभूषण महिलाओं के थे।"),
    ("कथन (A): पुरोहित राजा की शाल पर बने तिपतिया डिज़ाइन पश्चिमी एशिया के साथ संपर्कों का संकेत देते हैं।\nकारण (R): इसी तरह के तिपतिया डिज़ाइन मेसोपोटामिया और मिस्र में शाही वस्त्रों पर पाए जाते थे।", 0, "कथन (A) और कारण (R) दोनों सही हैं और कारण (R), कथन (A) की सही व्याख्या है।"),
    ("कथन (A): कालीबंगन से प्राप्त आक्रामक सांड मिट्टी का एक खिलौना है।\nकारण (R): मिट्टी के खिलौने हाथ से बनाए जाते थे और उनमें हिलने वाले अंग होते थे।", 3, "कथन (A) गलत है लेकिन कारण (R) सही है। कालीबंगन का सांड कांसे का है, मिट्टी का नहीं।"),
    ("कथन (A): हड़प्पा के धूसर पत्थर के नर्तक में सॉकेट छेद बने हैं।\nकारण (R): ये सॉकेट छेद धार्मिक नाटकों के दौरान सिर और हाथ घुमाने के लिए बनाए गए थे।", 2, "कथन (A) सही है लेकिन कारण (R) गलत है। सॉकेट छेद तो हैं, पर उनका उपयोग नाटकों में अंग घुमाने के लिए किया जाता था, इसका कोई प्रमाण नहीं है।"),
    ("कथन (A): हड़प्पा की प्रस्तर मूर्तियाँ बड़े मंदिरों के भीतर तराशी जाती थीं।\nकारण (R): मोहनजोदड़ो के दुर्ग के भीतर पत्थर की विशाल खदानें खोजी गई हैं।", 4, "कथन (A) और कारण (R) दोनों गलत हैं। हड़प्पा में न तो मंदिर मिले हैं और न ही मैदानी क्षेत्र में पत्थर की खदानें थीं।")
]:
    s2_mastery_hin.append({"type": "Assertion-Reason", "q": q, "opts": hin_ar_opts, "ans": ans, "sol": sol})

# Statement-Based (5)
for q, ans, sol in [
    ("Consider the following statements regarding the Priest-King bust:\n1. He wears a trefoil-patterned shawl draped over his left shoulder.\n2. He wears a circular headband (fillet) and a matching armband on his right arm.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct, describing the Priest-King's shawl, headband, and right armband."),
    ("Consider the following statements regarding the red sandstone male torso:\n1. It was excavated at Mohenjo-daro, close to the Great Bath.\n2. Its modular construction permitted attaching a separate stone head and limbs.\nWhich of the statements given above is/are correct?", 1, "Statement 2 is correct. Statement 1 is incorrect: it was excavated at Harappa, not Mohenjo-daro."),
    ("Consider the following statements regarding lost-wax casting:\n1. The mold was created using clay layers applied over a wax model.\n2. The technique was only used to cast animal figures and never human figures.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: it was used for human figures (Dancing Girl) as well as animal figures."),
    ("Consider the following statements regarding the Dancing Girl:\n1. She stands in the rigid, formal Samabhanga posture.\n2. She wears a total of four bangles on her right arm and holds a small bowl.\nWhich of the statements given above is/are correct?", 1, "Statement 2 is correct. Statement 1 is incorrect: she stands in the relaxed, fluid Tribhanga pose."),
    ("Consider the following statements regarding stone sculptures:\n1. They are abundant in the Indus Valley, with over five hundred stone statues recovered.\n2. They were carved from locally sourced granite and basalt blocks.\nWhich of the statements given above is/are correct?", 3, "Neither statement is correct. Stone statues are extremely rare (only about a dozen found) and were made of steatite, sandstone, and limestone, not granite or basalt.")
]:
    s2_mastery_eng.append({"type": "Statement-Based", "q": q, "opts": mcq_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("पुरोहित राजा की प्रतिमा के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. वे बाएं कंधे पर तिपतिया डिज़ाइन वाली शाल ओढ़े हुए हैं।\n2. वे सिर पर एक गोल पट्टी और दाहिनी बांह पर एक वैसा ही बाजूबंद पहने हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 2, "दोनों कथन सही हैं, जो पुरोहित राजा की शाल, पट्टी और बाजूबंद का वर्णन करते हैं।"),
    ("लाल बलुआ पत्थर के पुरुष धड़ के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. यह मोहनजोदड़ो में विशाल स्नानागार के पास से खोजा गया था।\n2. इसकी जोड़दार संरचना से अलग प्रस्तर सिर और हाथ जोड़े जा सकते थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 1, "कथन 2 सही है। कथन 1 गलत है क्योंकि यह हड़प्पा से मिला था।"),
    ("लुप्त मोम ढलाई तकनीक के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. मोम के मॉडल के ऊपर मिट्टी की परतें चढ़ाकर सांचा तैयार किया जाता था।\n2. इस तकनीक का उपयोग केवल पशु आकृतियों के लिए होता था, इंसानों के लिए कभी नहीं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि इसका उपयोग इंसानों (नर्तकी) के लिए भी होता था।"),
    ("कांस्य नर्तकी के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. वह सीधी, औपचारिक समभंग मुद्रा में खड़ी दिखाई गई है।\n2. वह अपने दाहिने हाथ में कुल चार चूड़ियाँ पहनती है और हाथ में एक छोटा कटोरा लिए हुए है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 1, "कथन 2 सही है। कथन 1 गलत है क्योंकि वह शिथिल त्रिभंग मुद्रा में खड़ी है।"),
    ("प्रस्तर मूर्तियों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. ये सिंधु घाटी में प्रचुर मात्रा में मिली हैं, कुल पांच सौ से अधिक प्रस्तर मूर्तियां प्राप्त हुई हैं।\n2. इन्हें स्थानीय रूप से मिलने वाले ग्रेनाइट और बेसाल्ट पत्थरों से तराशा गया था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 3, "दोनों कथन गलत हैं। पत्थर की मूर्तियाँ अत्यंत दुर्लभ हैं (केवल लगभग एक दर्जन प्राप्त) और ये सेलखड़ी व बलुआ पत्थर की थीं, ग्रेनाइट की नहीं।")
]:
    s2_mastery_hin.append({"type": "Statement-Based", "q": q, "opts": hin_mcq_opts, "ans": ans, "sol": sol})

# Why (3)
for q, sol in [
    ("Why did the sculptor of the red sandstone male torso drill socket holes in the neck and shoulders?", "The socket holes were drilled to allow a modular assembly of the sculpture. By carving the head and arms separately, the artist could achieve much finer detail and anatomical precision without the risk of breaking delicate projecting limbs from a single stone block, and it allowed attaching limbs made of different materials or in different postures."),
    ("Why is the bronze Dancing Girl considered a highly realistic, non-classical depiction of human form?", "Unlike the formal, rigid, and stylized statues of historical Indian art, the Dancing Girl is rendered with dynamic, natural posture. Her elongated limbs, relaxed tribhanga stance, right hand on hip, head tilted back, and proud expression capture a realistic, lively tribal or local girl. Her naturalistic modeling differs from the idealized, static figures of priests and kings."),
    ("Why is the Priest-King's shawl decoration significant for tracing cultural connections with Mesopotamia?", "The trefoil pattern carved on the Priest-King's shawl consists of three overlapping circles. In contemporary Mesopotamia and Egypt, this exact trefoil motif is associated with royal garments, astral deities, and divine symbols (like the bulls of heaven). This suggests that the Harappans shared common symbolic systems or had direct cultural and trade contacts with West Asian elite classes.")
]:
    s2_mastery_eng.append({"type": "Why", "q": q, "sol": sol})

for q, sol in [
    ("लाल बलुआ पत्थर के पुरुष धड़ के मूर्तिकार ने गर्दन और कंधों पर सॉकेट छेद क्यों बनाए थे?", "ये सॉकेट छेद मूर्ति के जोड़दार (modular) संयोजन के लिए बनाए गए थे। सिर और हाथों को अलग से तराशने से मूर्तिकार एक ही पत्थर से पूरी आकृति बनाने पर पतले अंगों के टूटने के जोखिम के बिना बहुत बारीक विवरण और शारीरिक शुद्धता प्राप्त कर सकता था। यह अलग-अलग मुद्राओं या विभिन्न सामग्रियों के अंगों को जोड़ने की सुविधा भी देता था।"),
    ("कांस्य नर्तकी को मानव रूप का अत्यंत यथार्थवादी और गैर-शास्त्रीय चित्रण क्यों माना जाता है?", "बाद के काल की आदर्श और कठोर मूर्तियों के विपरीत, नर्तकी को एक जीवंत और स्वाभाविक मुद्रा में दर्शाया गया है। उसके लंबे पतले हाथ-पैर, शिथिल त्रिभंग मुद्रा, कमर पर टिका हाथ, पीछे झुका सिर और गर्वित मुखाभिव्यक्ति एक वास्तविक स्थानीय लड़की के रूप को दर्शाती है। यह शैली पुरोहितों और राजाओं की औपचारिक मूर्तियों से बिल्कुल भिन्न है।"),
    ("पुरोहित राजा की शाल पर बना तिपतिया (trefoil) अलंकरण मेसोपोटामिया के साथ सांस्कृतिक संपर्कों का पता लगाने के लिए क्यों महत्वपूर्ण है?", "शाल पर खुदा तिपतिया डिज़ाइन तीन जुड़े हुए छल्लों का आकार है। समकालीन मेसोपोटामिया और मिस्र में इस तिपतिया डिज़ाइन का उपयोग दिव्य परिधानों, आकाशीय देवताओं और धार्मिक प्रतीकों (जैसे स्वर्ग के बैल) में होता था। यह दर्शाता है कि हड़प्पा वासियों के विचार और व्यापारिक संपर्क पश्चिमी एशिया के संभ्रांत वर्ग के साथ सीधे जुड़े हुए थे।")
]:
    s2_mastery_hin.append({"type": "Why", "q": q, "sol": sol})

# How (3)
for q, sol in [
    ("How did Harappan metalworkers execute the lost-wax casting of the Dancing Girl?", "First, they sculpted a detailed wax model of the girl. Then, they coated the wax model in layers of fine clay, leaving small openings at the bottom. Once dried, they heated the clay mold to melt and drain the wax out. After securing the hollow clay mold, they poured molten copper-tin bronze into the cavity. Once the metal cooled and solidified, they broke open the outer clay shell to reveal the finished bronze figurine, which was then polished."),
    ("How does the physical modeling of the red sandstone male torso achieve its lifelike realism?", "The sculptor carved the stone with soft contours, depicting the fleshy volumes of the abdomen, the natural depression of the navel, and the realistic alignment of the pelvic bone. The smooth finish and curved muscles mimic the soft quality of human flesh, showing a level of three-dimensional anatomical understanding that was millennia ahead of its time."),
    ("How is the Priest-King bust decorated, and what does it suggest about his social role?", "The Priest-King is decorated with a trefoil-patterned shawl over his left shoulder, a circular fillet headband with a central disc, and a matching armband on his right arm. His beard is groomed, and his ears are pierced. This elaborate ornamentation, combined with half-closed meditative eyes and a formal posture, suggests he was an elite religious leader, merchant guild chief, or administrator who wore indicators of high office.")
]:
    s2_mastery_eng.append({"type": "How", "q": q, "sol": sol})

for q, sol in [
    ("हड़प्पा के धातुकार नर्तकी की मूर्ति की लुप्त मोम ढलाई कैसे करते थे?", "सर्वप्रथम वे मोम की एक विस्तृत मूर्ति बनाते थे। फिर उस मोम की मूर्ति को बारीक मिट्टी की परतों से ढक देते थे और नीचे हवा/निकासी के लिए छेद छोड़ते थे। सूखने पर सांचे को गर्म किया जाता था जिससे मोम पिघलकर बाहर बह जाता था। फिर उस खाली मिट्टी के सांचे में पिघला हुआ तांबा-टिन का कांसा भर दिया जाता था। धातु के ठंडा होने पर बाहरी मिट्टी को तोड़ दिया जाता था और अंत में मूर्ति को पॉलिश किया जाता था।"),
    ("लाल बलुआ पत्थर के पुरुष धड़ की नक्काशी में सजीव यथार्थवाद कैसे प्राप्त किया गया है?", "मूर्तिकार ने पत्थर को बहुत कोमल गोलाइयों में तराशा है, जिसमें पेट की मांसपेशियों के उभार, नाभि के यथार्थवादी गड्ढे और कूल्हे की हड्डी के झुकाव को स्पष्ट दर्शाया गया है। इसकी चिकनी सतह और मांसपेशी वक्र मानव त्वचा की कोमलता की नकल करते हैं, जो उस समय के हिसाब से असाधारण शारीरिक समझ को प्रमाणित करता है।"),
    ("पुरोहित राजा की मूर्ति को कैसे सजाया गया है, और यह उनकी सामाजिक भूमिका के बारे में क्या संकेत देता है?", "पुरोहित राजा को बाएं कंधे पर तिपतिया शाल, सिर पर एक गोल चक्रदार पट्टी और दाहिने हाथ पर बाजूबंद पहने दिखाया गया है। उनकी दाढ़ी करीने से कटी है और कान छिदे हैं। यह आभूषण, शांत ध्यानमग्न नेत्र और औपचारिक बैठने की मुद्रा यह संकेत देती है कि वे कोई उच्च धार्मिक नेता, व्यापारी संघ के प्रमुख या शहर के मुख्य प्रशासक थे।")
]:
    s2_mastery_hin.append({"type": "How", "q": q, "sol": sol})

# Case Study (3)
for q, sol in [
    ("Case Study: Analyze the differences in material availability and artistic techniques between the steatite Priest-King bust from Mohenjo-daro and the red sandstone male torso from Harappa. What do these differences reveal about regional resources?", "Steatite is a magnesium silicate soapstone that was imported from Rajasthan or Gujarat, whereas red sandstone was quarried from the hills near Harappa. The Mohenjo-daro Priest-King reflects a formal, West-Asian influenced static style of carving on soft soapstone. The Harappan male torso reflects a naturalistic, highly detailed modeling of hard sandstone with a modular socket system. This shows that each city utilized its closest geological resources while sharing a common guild knowledge of stone-working techniques."),
    ("Case Study: The bronze Dancing Girl was discovered in a small, ordinary residential house in the HR area of Mohenjo-daro, rather than in a monumental temple or administrative palace. Evaluate what this context suggests about Harappan social hierarchy and art ownership.", "This indicates that art ownership in the Indus Valley was decentralized and domestic. In contemporary Egypt, metal sculptures were restricted to royal tombs or temple shrines. The discovery of a high-status bronze masterpiece in a regular commoner's house suggests that wealthy merchants, artisans, or private citizens could afford and own premium art. It reinforces the view of a society governed by municipal civic laws and trade wealth rather than a centralized divine king who monopolized artistic production."),
    ("Case Study: Chemical analysis of Harappan bronze objects shows varying tin concentrations (ranging from 1% to 12%), and tin is practically absent in the geology of the Indus plains. Discuss how these findings relate to the lost-wax casting of sculptures like the Dancing Girl.", "This shows that tin was a highly valued, imported raw material (sourced from Afghanistan or Central India) that had to be carefully managed. The high tin content (around 10-12%) in the Dancing Girl shows that for complex lost-wax casting, Harappan metalworkers deliberately used high-grade bronze alloys because tin lowers the melting point of copper and improves the fluidity of the molten metal, allowing it to fill the intricate details of the clay mold before solidifying.")
]:
    s2_mastery_eng.append({"type": "Case Study", "q": q, "sol": sol})

for q, sol in [
    ("केस स्टडी: मोहनजोदड़ो से प्राप्त सेलखड़ी के पुरोहित राजा और हड़प्पा से प्राप्त लाल बलुआ पत्थर के पुरुष धड़ की सामग्री व तकनीकों में अंतर का विश्लेषण करें। यह दोनों क्षेत्रों के संसाधनों के बारे में क्या दर्शाता है?", "सेलखड़ी एक मुलायम साबुन पत्थर है जिसे राजस्थान या गुजरात से लाया जाता था, जबकि लाल बलुआ पत्थर हड़प्पा के पास की पहाड़ियों से आता था। मोहनजोदड़ो का पुरोहित राजा मुलायम सोपस्टोन पर औपचारिक प्रस्तर शैली को दर्शाता है, जबकि हड़प्पा का पुरुष धड़ सॉकेट प्रणाली वाले कठोर बलुआ पत्थर पर बारीक यथार्थवादी कला को दिखाता है। यह सिद्ध करता है कि दोनों शहरों ने अपने निकटतम भूवैज्ञानिक संसाधनों का उपयोग किया, जबकि पत्थर के काम की गिल्ड तकनीकें दोनों जगह समान थीं।"),
    ("केस स्टडी: कांस्य नर्तकी मोहनजोदड़ो के HR क्षेत्र में एक साधारण रिहायशी घर से मिली थी, न कि किसी बड़े मंदिर या प्रशासनिक महल से। यह संदर्भ हड़प्पा की सामाजिक व्यवस्था और कला के स्वामित्व के बारे में क्या दर्शाता है?", "यह दर्शाता है कि सिंधु घाटी में कला का स्वामित्व विकेंद्रीकृत और व्यक्तिगत था। मिस्र के विपरीत, जहाँ धातु की मूर्तियाँ मंदिरों या राजा की कब्रों तक सीमित थीं, हड़प्पा में एक बहुमूल्य कांस्य कलाकृति का सामान्य घर में मिलना यह दर्शाता है कि धनी व्यापारी या आम नागरिक भी कला खरीद सकते थे। यह एक ऐसी सामाजिक व्यवस्था को रेखांकित करता है जो पुरोहितों के नियंत्रण के बजाय व्यापारिक संपदा पर आधारित थी।"),
    ("केस स्टडी: हड़प्पा के कांस्य बर्तनों के रासायनिक विश्लेषण से पता चलता है कि उनमें टिन की सांद्रता (1% से 12%) अलग-अलग है, और टिन सिंधु घाटी में नहीं मिलता था। यह खोज कांस्य नर्तकी जैसी मूर्तियों के निर्माण से कैसे संबंधित है?", "यह दर्शाता है कि टिन एक अत्यंत मूल्यवान आयातित कच्चा माल था (जो अफगानिस्तान या मध्य भारत से आता था) जिसे बहुत सोच-समझकर उपयोग किया जाता था। नर्तकी की मूर्ति में टिन की सांद्रता (लगभग 11-12%) अधिक होना यह प्रमाणित करता है कि शिल्पकार जानते थे कि टिन मिलाने से तांबे का गलनांक कम हो जाता है और पिघली धातु का प्रवाह सुगम होता है, जिससे मिट्टी के सांचे के बारीक कोनों में भी धातु ठीक से भर जाती थी।")
]:
    s2_mastery_hin.append({"type": "Case Study", "q": q, "sol": sol})

# Teach Concept (3)
for q, sol in [
    ("Teach the concept of the 'Tribhanga Posture' as demonstrated in the bronze Dancing Girl, explaining its significance in Indian art history.", "Tribhanga (literally 'three bends') is a traditional standing posture in Indian art where the body bends in three places: the neck tilts in one direction, the torso curves in the opposite direction, and the hips/legs shift back. In the bronze Dancing Girl, she stands with her head tilted slightly back, her right hip pushed out, and her knees slightly bent. This creates a highly dynamic, fluid, and rhythmic posture that captures the movement of a dance. It is the earliest known representation of Tribhanga in South Asian sculpture, a posture that later became a cornerstone of classical Indian dance (like Odissi) and Hindu temple sculpture."),
    ("Explain the modular design and technical assembly of the sandstone male torso to a class.", "The sandstone male torso is a tiny sculpture (9.5 cm) that demonstrates an advanced, modular assembly technique. Instead of carving the entire figure from a single block of stone, the artist carved the body torso, head, and arms separately. To join them, the artist drilled circular socket holes into the neck and shoulders. Detachable limbs (possibly made of different colored stones or materials) were inserted into these sockets. This modular design allowed the creator to focus on extreme detail in each piece without the risk of thin protruding arms snapping off during carving."),
    ("Teach the iconographic details of the Priest-King bust and discuss why his identification is contested.", "The Priest-King has specific details: a bearded face with a shaved upper lip, half-closed eyes, a fillet headband with a central disc, an armlet, and a shawl over his left shoulder with trefoil designs. Sir John Marshall termed him a 'Priest-King' based on Mesopotamian parallels where rulers were also high priests. However, this is contested because there is no evidence of temples, palaces, royal graves, or a ruling priesthood in the Indus Valley. He could simply be a wealthy merchant, a clan elder, or a civic administrator wearing indicators of status, rather than a divine king.")
]:
    s2_mastery_eng.append({"type": "Teach Concept", "q": q, "sol": sol})

for q, sol in [
    ("कांस्य नर्तकी में प्रदर्शित 'त्रिभंग मुद्रा' की अवधारणा को समझाएं और भारतीय कला इतिहास में इसके महत्व पर चर्चा करें।", "त्रिभंग (अर्थात तीन झुकाव) भारतीय कला की एक पारंपरिक खड़ी मुद्रा है जिसमें शरीर तीन स्थानों पर झुकता है: गर्दन एक तरफ झुकती है, धड़ विपरीत दिशा में वक्र बनाता है, और कूल्हे व पैर वापस सीधे होते हैं। कांस्य नर्तकी में उसका सिर पीछे झुका है, दाहिना कूल्हा बाहर की तरफ निकला है और घुटने थोड़े मुड़े हैं। यह एक अत्यंत गतिशील, लचीली और लयबद्ध मुद्रा बनाता है जो नृत्य की गति को दर्शाता है। यह दक्षिण एशियाई मूर्तिकला में त्रिभंग का सबसे पहला ज्ञात उदाहरण है, जो बाद में शास्त्रीय भारतीय नृत्य (जैसे ओडिसी) और मंदिर मूर्तिकला का मुख्य आधार बना।"),
    ("बलुआ पत्थर के पुरुष धड़ की जोड़दार (modular) संरचना और तकनीकी संयोजन को छात्रों को समझाएं।", "बलुआ पत्थर का पुरुष धड़ (9.5 सेमी) एक उन्नत जोड़दार असेंबली तकनीक को प्रदर्शित करता है। एक ही पत्थर से पूरी मूर्ति बनाने के बजाय मूर्तिकार ने धड़, सिर और हाथ अलग-अलग बनाए। इन्हें आपस में जोड़ने के लिए कंधे और गर्दन पर गोल सॉकेट (socket) छेद किए गए थे। अलग से बने अंगों (शायद भिन्न रंगों के पत्थरों के) को इन छेदों में फिट किया जाता था। यह जोड़दार डिजाइन मूर्तिकार को बारीक नक्काशी करने की सुविधा देता था और पतले अंगों के टूटने का डर नहीं रहता था।"),
    ("पुरोहित राजा की मूर्ति की रूपात्मक विशेषताओं को समझाएं और चर्चा करें कि उनकी पहचान क्यों विवादित है।", "पुरोहित राजा के चेहरे पर करीने से संवारी दाढ़ी, मूंछ रहित होंठ, अधखुले नेत्र, सिर पर पट्टी, बाजूबंद और बाएं कंधे पर तिपतिया शाल है। जॉन मार्शल ने मेसोपोटामिया की तर्ज पर उन्हें 'पुरोहित राजा' कहा था जहाँ शासक ही मुख्य पुरोहित होते थे। लेकिन यह विवादित है क्योंकि सिंधु घाटी में किसी मंदिर, महल, राजकीय कब्र या शासक पुरोहित वर्ग के होने का कोई प्रमाण नहीं मिला है। वे केवल एक अमीर व्यापारी, कबीले के मुखिया या शहर के प्रशासक भी हो सकते हैं जिन्होंने अपनी प्रतिष्ठा के प्रतीक पहने थे।")
]:
    s2_mastery_hin.append({"type": "Teach Concept", "q": q, "sol": sol})


# =========================================================================
# SECTION 3: TERRACOTTA FIGURINES & PAINTED POTTERY
# =========================================================================
s3_mastery_eng = []
s3_mastery_hin = []

# MCQ (5)
for q, opts, ans, sol in [
    ("Which technique was primarily used to manufacture Harappan terracotta figurines?", ["Hand-modeling by pinching and appliqué", "Mass production in metal molds", "Rotary carving from dried clay blocks", "Lost-wax casting in bronze shells"], 0, "Terracottas were entirely hand-modeled using pinching and appliqué techniques."),
    ("The headdress of the terracotta Mother Goddess figurines features which of the following details?", ["Fan-shaped headdresses with soot-stained cup-like panniers", "Plain rounded helmets made of copper wire", "Crowns made of inlaid lapis lazuli beads", "No headdress, she is depicted with loose hair"], 0, "Mother Goddess figurines wear fan headdresses with soot-stained cup panniers."),
    ("What does the presence of soot stains inside the headdress panniers of Mother Goddess figurines suggest?", ["They were used to burn oil or incense in domestic rituals", "They were used to store toxic cosmetic chemicals", "They were damaged by fires during the city's destruction", "They were used as weights for measuring gold beads"], 0, "Soot stains indicate they burned oil or incense during household rituals."),
    ("What are the primary colors used to decorate standard Harappan painted pottery?", ["Red background slip and black painted motifs", "Yellow background slip and blue painted motifs", "White background slip and red painted motifs", "Green background slip and gold painted motifs"], 0, "Harappan pottery is red-and-black ware, with black paint over a red slip."),
    ("Which of the following animal motifs is commonly painted on Harappan wheel-made pottery?", ["Fish scales and Pipal leaves", "Lions chasing horses", "Elephants fighting rhinos on chariots", "Mesopotamian mythical chimeras"], 0, "Fish-scale patterns, Pipal leaves, geometric circles, and birds are common pottery motifs.")
]:
    s3_mastery_eng.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("हड़प्पा कालीन मिट्टी की मूर्तियों (Terracotta) के निर्माण में मुख्य रूप से किस तकनीक का उपयोग किया जाता था?", ["उंगलियों से पिंच करने और आवरण (pinching & appliqué) द्वारा हाथ से बनाना", "धातु के सांचों में बड़े पैमाने पर ढलाई", "सूखे मिट्टी के ब्लॉकों से घुमाकर तराशना", "कांस्य के सांचों में लुप्त मोम ढलाई"], 0, "मिट्टी की मूर्तियां पूरी तरह से पिंचिंग और आवरण (appliqué) तकनीकों का उपयोग करके हाथ से बनाई जाती थीं।"),
    ("मिट्टी की मातृदेवी (Mother Goddess) की मूर्तियों के सिर पर निम्नलिखित में से कौन सा विवरण बना है?", ["प्यालेनुमा कालिखदार आकृतियों (panniers) से सजा पंख जैसा मुकुट", "तांबे के तारों से बना साधारण गोल हेलमेट", "लाजवर्त के मोतियों से जड़े हुए मुकुट", "कोई मुकुट नहीं, वे खुले बालों में दिखाई गई हैं"], 0, "मातृदेवी की मूर्तियों के सिर पर पंखे जैसा मुकुट और कालिख वाले प्याले (panniers) बने हैं।"),
    ("मातृदेवी की मूर्तियों के सिर पर बने प्यालों में कालिख के निशान क्या दर्शाते हैं?", ["घरेलू अनुष्ठानों में इनमें तेल का दीपक या धूप जलाया जाता था", "इनका उपयोग जहरीले सौंदर्य प्रसाधनों को रखने के लिए होता था", "शहरों के विनाश के समय लगी आग से ये झुलस गई थीं", "इनका उपयोग सोने के मोतियों को तोलने के लिए बाट के रूप में होता था"], 0, "कालिख के निशान दर्शाते हैं कि घरेलू पूजा में इनके समक्ष दीप या धूप जलाई जाती थी।"),
    ("मानक हड़प्पा चित्रित मृदभांडों को सजाने के लिए किन प्राथमिक रंगों का उपयोग किया जाता था?", ["लाल रंग की पृष्ठभूमि (slip) और काले रंग के रेखाचित्र", "पीले रंग की पृष्ठभूमि और नीले रंग के रेखाचित्र", "सफेद रंग की पृष्ठभूमि और लाल रंग के रेखाचित्र", "हरे रंग की पृष्ठभूमि और सुनहरे रंग के रेखाचित्र"], 0, "हड़प्पा के बर्तन लाल-काले मृदभांड हैं, जिन पर लाल लेप पर काले रंग से चित्रकारी की जाती थी।"),
    ("हड़प्पा के चाक-निर्मित बर्तनों पर निम्नलिखित में से कौन सा रूपांकन (motif) आमतौर पर रंगा जाता था?", ["मछली के शल्क (scales) और पीपल के पत्ते", "घोड़ों का पीछा करते शेर", "रथों पर लड़ते हाथी और गैंडे", "मेसोपोटामिया के काल्पनिक जीव"], 0, "मछली के शल्क, पीपल के पत्ते, ज्यामितीय वृत्त और पक्षी सामान्य बर्तन डिज़ाइन हैं।")
]:
    s3_mastery_hin.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# Multiple Correct MCQ (5)
for q, opts, ans, sol in [
    ("Select the features of Harappan terracotta Mother Goddess figurines: (Select all that apply)", ["Hand-modeled baked clay", "Fan-shaped headdress with cup-like panniers", "Adorned with heavy necklaces and grid-belts", "Carved from polished white limestone"], [0, 1, 2], "Mother Goddess figurines are hand-modeled clay with fan headdresses, panniers, and heavy necklaces. None are stone."),
    ("Which of the following terracotta toys have been excavated at Harappan sites? (Select all that apply)", ["Wheeled toy carts", "Bulls with movable heads controlled by strings", "Monkeys sliding down vertical cords", "Toy chariots made of cast iron"], [0, 1, 2], "Toy carts, movable bulls, and sliding monkeys are common. Iron did not exist."),
    ("Identify the design motifs commonly painted on Mature Harappan pottery: (Select all that apply)", ["Geometric intersecting circles", "Vegetal Pipal leaves and palm trees", "Fish-scale patterns", "Lions hunting horses"], [0, 1, 2], "Intersecting circles, Pipal leaves, palm trees, and fish scales are common. Lions and horses are not depicted."),
    ("Select correct statements regarding Harappan pottery manufacturing: (Select all that apply)", ["Pottery was made on a fast-spinning potter's wheel", "A red slip of iron oxide was applied before firing", "Black designs of manganese were painted on the slip", "Pottery was fired at low temperatures in open pits"], [0, 1, 2], "Harappan pottery was wheel-made, used red slip and black manganese paint, and was fired at high temperatures in updraft kilns."),
    ("Which of the following are functional shapes of Harappan pottery? (Select all that apply)", ["Tall storage jars with narrow bases", "Perforated cylindrical jars (beverage strainers)", "Dish-on-stand offering vessels", "Glazed porcelain teacups"], [0, 1, 2], "Storage jars, perforated strainers, and dish-on-stand are standard pottery shapes. Porcelain teacups were unknown.")
]:
    s3_mastery_eng.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("हड़प्पा की मिट्टी की मातृदेवी की मूर्तियों की विशिष्टताओं का चयन करें: (सभी लागू विकल्प चुनें)", ["हाथ से गढ़ी पकी मिट्टी", "प्यालेनुमा कालिखदार आकृतियों से सजा पंख जैसा मुकुट", "भारी हार और ग्रिड जैसी करधनी (belts) से सजी", "पॉलिश किए गए सफेद चूना पत्थर से निर्मित"], [0, 1, 2], "मातृदेवी की मूर्तियां हाथ से बनी मिट्टी की हैं, जिन पर मुकुट, प्याले और भारी आभूषण हैं। पत्थर की नहीं हैं।"),
    ("हड़प्पा स्थलों से निम्नलिखित में से कौन से मिट्टी के खिलौने प्राप्त हुए हैं? (सभी लागू विकल्प चुनें)", ["पहियों वाली खिलौना गाड़ियां", "धागे से हिलने वाले सिर वाले सांड", "रस्सी पर नीचे सरकने वाले बंदर", "ढले हुए लोहे से बने रथ"], [0, 1, 2], "खिलौना गाड़ियां, हिलने वाले सिर वाले सांड और सरकने वाले बंदर मिले हैं। लोहे का ज्ञान नहीं था।"),
    ("परिपक्व हड़प्पा मृदभांडों पर आमतौर पर चित्रित डिज़ाइनों की पहचान करें: (सभी लागू विकल्प चुनें)", ["ज्यामितीय एक-दूसरे को काटते वृत्त", "पीपल के पत्ते और ताड़ के पेड़", "मछली के शल्क (scales) का डिज़ाइन", "घोड़ों का शिकार करते शेर"], [0, 1, 2], "वृत्त, पीपल के पत्ते, ताड़ के पेड़ और मछली के शल्क आम हैं। शेर और घोड़े चित्रित नहीं हैं।"),
    ("हड़प्पा बर्तनों के निर्माण के संबंध में सही कथनों का चयन करें: (सभी लागू विकल्प चुनें)", ["बर्तन तेज गति से घूमने वाले चाक पर बनते थे", "पकाने से पहले लोहे के लाल लेप (गेरू) का लेप लगाया जाता था", "लेप के ऊपर मैंगनीज के काले रेखाचित्र बनाए जाते थे", "बर्तनों को खुले गड्ढों में बहुत कम तापमान पर पकाया जाता था"], [0, 1, 2], "बर्तन चाक पर बनते थे, लाल लेप और काले मैंगनीज पिगमेंट का उपयोग होता था और इन्हें भट्टियों में पकाया जाता था।"),
    ("निम्नलिखित में से कौन से हड़प्पा मृदभांडों के कार्यात्मक आकार हैं? (सभी लागू विकल्प चुनें)", ["संकड़े आधार वाले ऊंचे अनाज भंडारण जार", "छिद्रित बेलनाकार जार (पेय छानने के पात्र)", "थाली-युक्त स्टैंड (dish-on-stand) वाले प्रसाद पात्र", "चमकीली चीनी मिट्टी (porcelain) के चाय के प्याले"], [0, 1, 2], "भंडारण जार, छिद्रित जार और डिश-ऑन-स्टैंड सामान्य प्रकार हैं। चीनी मिट्टी की चाय की प्यालियां नहीं थीं।")
]:
    s3_mastery_hin.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# True/False (8)
for q, ans, sol in [
    ("Terracotta Mother Goddess figurines were mass-produced in two-part bronze molds.", False, "False. They were hand-modeled, not mold-cast."),
    ("The headdress panniers of Mother Goddess figurines often contain soot stains from incense burning.", True, "True. Soot stains suggest incense or oil was burned in them."),
    ("Lions and horses are the most common animals painted on Harappan red pottery.", False, "False. Lions and horses are completely absent from pottery paintings."),
    ("Harappan painted pottery was decorated using black manganese-rich pigment over a red slip.", True, "True. Red-and-black ware is the standard style."),
    ("The perforated pottery jars were likely used to strain beer or other fermented beverages.", True, "True. Drilled holes suggest they acted as strainers or filters."),
    ("Terracotta toys include carts with wheels, whistles, and movable-head bulls.", True, "True. These toys are common and reflect advanced clay-modeling skills."),
    ("Terracotta figurines are rare, with only a dozen specimens found across the entire civilization.", False, "False. Terracottas are extremely abundant, numbering in the thousands."),
    ("The black paint on Harappan pottery was applied after the pot was fully fired and cooled.", False, "False. Red slip and black paint were applied before firing, bonding them permanently.")
]:
    s3_mastery_eng.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("मिट्टी की मातृदेवी की मूर्तियों का निर्माण बड़े पैमाने पर कांसे के सांचों में किया जाता था।", False, "असत्य। वे पूरी तरह हाथ से गढ़ी जाती थीं, सांचे से नहीं।"),
    ("मातृदेवी की मूर्तियों के सिर पर बने प्यालों में धूप जलाने के कारण अक्सर कालिख के निशान मिलते हैं।", True, "सत्य। कालिख के निशान घरेलू पूजा में धूप या तेल दीया जलाने का संकेत हैं।"),
    ("हड़प्पा के लाल बर्तनों पर शेर और घोड़े सबसे आम चित्रित पशु हैं।", False, "असत्य। शेर और घोड़े बर्तनों के रेखाचित्रों में पूरी तरह अनुपस्थित हैं।"),
    ("हड़प्पा चित्रित मृदभांडों पर लाल लेप के ऊपर काले मैंगनीज पिगमेंट से चित्रकारी की जाती थी।", True, "सत्य। यह लाल और काले रंग के मृदभांड बनाने की मानक शैली थी।"),
    ("छिद्रित मिट्टी के बर्तनों (perforated jars) का उपयोग संभवतः शराब या अन्य पेय छानने के लिए किया जाता था।", True, "सत्य। इनमें बने छिद्र छानने या छानने की क्रिया का संकेत देते हैं।"),
    ("मिट्टी के खिलौनों में पहियेदार गाड़ियां, सीटियां और हिलने वाले सिर वाले सांड शामिल हैं।", True, "सत्य। ये खिलौने आम हैं और खिलौना निर्माताओं की कला को दर्शाते हैं।"),
    ("मिट्टी की मूर्तियाँ अत्यंत दुर्लभ हैं, पूरी सभ्यता में केवल एक दर्जन मूर्तियाँ ही मिली हैं।", False, "असत्य। ये अत्यंत प्रचुर मात्रा में मिली हैं, जिनकी संख्या हजारों में है।"),
    ("हड़प्पा बर्तनों पर काला रंग बर्तन के पूरी तरह पकने और ठंडा होने के बाद लगाया जाता था।", False, "असत्य। लाल लेप और काली चित्रकारी पकाने से पहले की जाती थी ताकि वे स्थायी रूप से जुड़ जाएं।")
]:
    s3_mastery_hin.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

# Fill in the Blank (8)
for q, ans, sol in [
    ("Terracotta figurines were modeled by hand, using the pinching and ___________ techniques.", "appliqué", "Appliqué involves attaching clay strips/pellets to represent details."),
    ("The headdress cup-like ornaments on Mother Goddess figurines are called ___________.", "panniers", "The cup-like headdress ornaments are called panniers."),
    ("The soot stains inside Mother Goddess panniers prove they were used in domestic ___________.", "rituals", "The soot shows they burned oil/incense during household rituals."),
    ("Standard Harappan painted pottery is known as red and ___________ ware.", "black", "It is known as red-and-black painted pottery."),
    ("The black painted designs on pottery were made using ___________-rich pigments.", "manganese", "Manganese dioxide was the mineral used for black paint."),
    ("Toy bulls had movable heads controlled by a thread passing through the ___________.", "neck", "A thread through the neck allowed the head to move."),
    ("The tall cylindrical vessels with numerous drilled holes are called ___________ jars.", "perforated", "These are perforated jars, likely used as strainers."),
    ("A unique terracotta model of a ship with a mast socket was discovered at the port of ___________.", "Lothal", "The clay ship model was found at Lothal.")
]:
    s3_mastery_eng.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("मिट्टी की मूर्तियां हाथ से पिंचिंग और आभूषण चिपकाने की ___________ तकनीक से बनाई जाती थीं।", "आवरण", "चिपकाने वाली इस विधि को आवरण (appliqué) तकनीक कहा जाता है।"),
    ("मातृदेवी की मूर्तियों के सिर पर मुकुट के दोनों तरफ बनी प्याले जैसी आकृतियों को ___________ कहा जाता है।", "पैनियर", "इन प्यालेनुमा आकृतियों को पैनियर (panniers) कहा जाता है।"),
    ("मातृदेवी के पैनियर में मिले कालिख के निशान प्रमाणित करते हैं कि इनका उपयोग घरेलू ___________ में होता था।", "अनुष्ठान", "कालिख दर्शाती है कि इनका उपयोग पूजा या अनुष्ठान (rituals) के दीपकों के रूप में होता था।"),
    ("मानक हड़प्पा चित्रित बर्तनों को लाल और ___________ मृदभांड कहा जाता है।", "काले", "इन्हें लाल और काले (red and black) मृदभांड कहा जाता है।"),
    ("बर्तनों पर काली चित्रकारी करने के लिए ___________ से भरपूर खनिज पिगमेंट का उपयोग किया जाता था।", "मैंगनीज", "काले रंग के लिए मैंगनीज (manganese) पिगमेंट का उपयोग होता था।"),
    ("खिलौना बैलों के सिर हिलाने के लिए गर्दन के ___________ से होकर एक धागा निकाला जाता था।", "छेद", "गर्दन के छेद (hole/neck) से धागा निकाला जाता था।"),
    ("पूरे शरीर पर कई छोटे छेदों वाले लंबे बेलनाकार बर्तनों को ___________ जार कहा जाता है।", "छिद्रित", "इन्हें छिद्रित जार (perforated jars) कहा जाता है।"),
    ("मस्तूल के सॉकेट वाले जहाज का एक अनूठा मिट्टी का खिलौना मॉडल ___________ बंदरगाह से मिला था।", "लोथल", "यह मॉडल लोथल (Lothal) बंदरगाह से मिला था।")
]:
    s3_mastery_hin.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

# Match the Following (3)
for q, items, opts, sol in [
    (
        "Match the terracotta artifacts with their socio-cultural descriptions:",
        [{"left": "I. Mother Goddess figurines", "key": "A"}, {"left": "II. Wheeled toy carts", "key": "B"}, {"left": "III. Terracotta animal whistles", "key": "C"}],
        [{"val": "A", "text": "A. Fan headdresses with soot panniers, linked to domestic fertility rituals"}, {"val": "B", "text": "B. Earliest model evidence of vehicular transport in South Asia"}, {"val": "C", "text": "C. Clay bird-shaped figures used for children's amusement"}],
        "Mother Goddess has soot panniers; Toy carts show wheeled transport; Whistles are bird-shaped toys for children."
    ),
    (
        "Match the pottery shapes with their potential uses:",
        [{"left": "I. Large storage jars", "key": "A"}, {"left": "II. Perforated cylindrical jars", "key": "B"}, {"left": "III. Dish-on-stand", "key": "C"}],
        [{"val": "A", "text": "A. Holding grains, oil, or water in domestic households"}, {"val": "B", "text": "B. Straining fermented beverages or burning incense"}, {"val": "C", "text": "C. Presenting food offerings during rituals or banquets"}],
        "Storage jars held grain/water; Perforated jars were strainers/censers; Dish-on-stand was for offerings."
    ),
    (
        "Match the decorative motifs with their geometric or nature categories:",
        [{"left": "I. Intersecting circles", "key": "A"}, {"left": "II. Pipal leaf", "key": "B"}, {"left": "III. Fish scales", "key": "C"}],
        [{"val": "A", "text": "A. Geometric pattern painted in black manganese paint"}, {"val": "B", "text": "B. Vegetal motif painted on red slips representing sacred trees"}, {"val": "C", "text": "C. Zoomorphic-overlapping pattern resembling riverine fauna skins"}],
        "Intersecting circles is geometric; Pipal leaf is vegetal/sacred; Fish scales is overlapping zoomorphic."
    )
]:
    s3_mastery_eng.append({"type": "Match the Following", "q": q, "items": items, "options": opts, "sol": sol})

for q, items, opts, sol in [
    (
        "मिट्टी की कलाकृतियों को उनके सामाजिक-सांस्कृतिक विवरणों से सुमेलित करें:",
        [{"left": "I. मातृदेवी की मूर्तियां", "key": "A"}, {"left": "II. पहियेदार खिलौना गाड़ियां", "key": "B"}, {"left": "III. मिट्टी की पशु सीटियां", "key": "C"}],
        [{"val": "A", "text": "A. कालिख वाले मुकुट, घरेलू उर्वरता अनुष्ठानों से संबंधित"}, {"val": "B", "text": "B. दक्षिण एशिया में पहिएदार परिवहन के प्राचीनतम मॉडल साक्ष्य"}, {"val": "C", "text": "C. बच्चों के मनोरंजन के लिए प्रयुक्त पक्षी के आकार के खिलौने"}],
        "मातृदेवी कालिख पैनियर से जुड़ी हैं; गाड़ियां पहिएदार परिवहन का साक्ष्य हैं; सीटियां पक्षी के आकार के खिलौने हैं।"
    ),
    (
        "मृदभांडों के आकारों को उनके संभावित उपयोगों से सुमेलित करें:",
        [{"left": "I. अनाज भंडारण के बड़े जार", "key": "A"}, {"left": "II. छिद्रित बेलनाकार जार", "key": "B"}, {"left": "III. थाली-युक्त स्टैंड (dish-on-stand)", "key": "C"}],
        [{"val": "A", "text": "A. घरों में अनाज, तेल या पानी का भंडारण करना"}, {"val": "B", "text": "B. किण्वित पेय पदार्थों को छानना या धूप जलाना"}, {"val": "C", "text": "C. अनुष्ठानों या भोजों में खाद्य प्रसाद अर्पित करना"}],
        "भंडारण जार अनाज/तेल के लिए हैं; छिद्रित जार पेय छानने/धूप जलाने के लिए हैं; डिश-ऑन-स्टैंड प्रसाद के लिए है।"
    ),
    (
        "बर्तनों पर चित्रित डिज़ाइनों को उनकी श्रेणियों से सुमेलित करें:",
        [{"left": "I. एक-दूसरे को काटते वृत्त", "key": "A"}, {"left": "II. पीपल का पत्ता", "key": "B"}, {"left": "III. मछली के शल्क (scales)", "key": "C"}],
        [{"val": "A", "text": "A. काले मैंगनीज रंग से चित्रित ज्यामितीय पैटर्न"}, {"val": "B", "text": "B. लाल लेप पर चित्रित पवित्र वृक्षों को दर्शाने वाला वनस्पति रूपांकन"}, {"val": "C", "text": "C. जलीय जीवों की त्वचा की नकल करने वाला एक-दूसरे को ढकता पैटर्न"}],
        "काटते वृत्त ज्यामितीय हैं; पीपल का पत्ता वनस्पति का है; मछली के शल्क जलीय जीवों से प्रेरित ओवरलैपिंग पैटर्न है।"
    )
]:
    s3_mastery_hin.append({"type": "Match the Following", "q": q, "items": items, "options": opts, "sol": sol})

# One-Liner (8)
for q, sol in [
    ("What technique was used to model clay terracottas by hand?", "Pinching (and appliqué for ornaments)."),
    ("Describe the headdress of Mother Goddess figurines.", "A fan-shaped headdress with cup-like panniers on either side."),
    ("Why do Mother Goddess cup headdresses have soot stains?", "Because they burned oil or incense in domestic household prayers."),
    ("Name one toy animal with moving parts found in Harappan sites.", "The toy bull with a movable head (controlled by a string)."),
    ("What is the standard name of Mature Harappan pottery?", "Red-and-black painted pottery (or red-and-black ware)."),
    ("What pigment was used to paint black designs on pottery?", "Manganese-based pigment."),
    ("Name one vegetal motif painted on Harappan pots.", "Pipal leaf (Ficus religiosa) or palm tree branches."),
    ("What shape of jar was likely used as a beverage strainer?", "The perforated cylindrical jar.")
]:
    s3_mastery_eng.append({"type": "One-Liner", "q": q, "sol": sol})

for q, sol in [
    ("हाथ से मिट्टी की मूर्तियां बनाने के लिए किस तकनीक का उपयोग किया जाता था?", "पिंचिंग (pinching) और विवरणों के लिए आवरण (appliqué) तकनीक।"),
    ("मातृदेवी की मूर्तियों के मुकुट की बनावट का वर्णन करें।", "पंखे जैसा बड़ा मुकुट जिसके दोनों तरफ प्यालेनुमा आकृतियां (panniers) बनी थीं।"),
    ("मातृदेवी के सिर के प्यालों में कालिख के निशान क्यों हैं?", "क्योंकि घरेलू पूजा के दौरान उनमें तेल का दीया या धूप जलाई जाती थी।"),
    ("हड़प्पा स्थलों से मिले हिलने वाले अंगों वाले एक खिलौना पशु का नाम बताएं।", "धागे से हिलने वाले सिर वाला मिट्टी का बैल।"),
    ("परिपक्व हड़प्पा मृदभांडों का मानक नाम क्या है?", "लाल और काले चित्रित मृदभांड (Red-and-black painted pottery)।"),
    ("बर्तनों पर काले रेखाचित्र बनाने के लिए किस पिगमेंट का उपयोग किया जाता था?", "मैंगनीज-आधारित (manganese) पिगमेंट का।"),
    ("हड़प्पा बर्तनों पर चित्रित एक वनस्पति रूपांकन का नाम बताएं।", "पीपल का पत्ता (Pipal leaf) या ताड़ की शाखाएं।"),
    ("पेय पदार्थों को छानने के लिए किस आकार के जार का उपयोग किया जाता था?", "छिद्रित बेलनाकार जार (Perforated cylindrical jar)।")
]:
    s3_mastery_hin.append({"type": "One-Liner", "q": q, "sol": sol})

# Assertion-Reason (8)
for q, ans, sol in [
    ("Assertion (A): Terracotta Mother Goddess figurines were used in household religious activities.\nReason (R): The headdress cup-like panniers contain soot stains, proving they burned incense or oil inside homes.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Harappan painted pottery is known as black-and-red ware.\nReason (R): The red background was applied as a slip, and black manganese designs were painted over it.", 0, "Both A and R are true and R is the correct explanation of A. (Note: standard UPSC terminology refers to this as red-and-black ware, which is built using red slip and black paint)."),
    ("Assertion (A): Terracotta toy carts provide direct evidence of vehicular transport.\nReason (R): Metal toy carts were cast in bronze using two-part iron molds in all major capitals.", 2, "A is true but R is false. Carts were made of terracotta (baked clay) by hand, not cast in bronze/iron molds."),
    ("Assertion (A): Perforated cylindrical jars were used to store grains.\nReason (R): The drilled holes allowed air to circulate, keeping the grain fresh.", 4, "Both A and R are false. Perforated jars were strainers for liquids or incense burners, not grain storage vessels (which were large solid jars)."),
    ("Assertion (A): Lions are the most common animals painted on Harappan pottery.\nReason (R): Lions were worshipped as symbols of royal power in the Harappan state.", 4, "Both A and R are false. Lions are completely absent from Harappan pottery and seal iconography."),
    ("Assertion (A): Terracotta figurines were hand-modeled using pinching and appliqué.\nReason (R): Harappans completely lacked mold technology for casting metals.", 2, "A is true but R is false. They hand-modeled clay, but they possessed advanced mold technology for lost-wax bronze casting."),
    ("Assertion (A): The black designs on Harappan pottery do not wash or fade away.\nReason (R): The manganese paint was fired together with the clay and red slip in high-temperature kilns, bonding them permanently.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Toy models of animals reflect a playful side of Harappan craftsmen.\nReason (R): Toys like sliding monkeys and movable-head bulls demonstrate advanced mechanical toys.", 0, "Both A and R are true and R is the correct explanation of A.")
]:
    s3_mastery_eng.append({"type": "Assertion-Reason", "q": q, "opts": ar_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("कथन (A): मिट्टी की मातृदेवी की मूर्तियों का उपयोग घरेलू धार्मिक गतिविधियों में किया जाता था।\nकारण (R): सिर के प्यालेनुमा पैनियर में कालिख के निशान मिले हैं, जो यह साबित करते हैं कि घरों के अंदर इनमें धूप या तेल जलाया जाता था।", 0, "कथन (A) और कारण (R) दोनों सही हैं और कारण (R), कथन (A) की सही व्याख्या है।"),
    ("कथन (A): हड़प्पा के चित्रित बर्तनों को लाल-काले मृदभांड के रूप में जाना जाता है।\nकारण (R): लाल पृष्ठभूमि को लेप (slip) के रूप में लगाया जाता था और उसके ऊपर काले मैंगनीज से चित्रकारी की जाती थी।", 0, "कथन (A) और कारण (R) दोनों सही हैं और कारण (R), कथन (A) की सही व्याख्या है।"),
    ("कथन (A): मिट्टी की खिलौना गाड़ियां पहिएदार परिवहन का प्रत्यक्ष प्रमाण प्रदान करती हैं।\nकारण (R): ये खिलौना गाड़ियां सभी बड़ी राजधानियों में दो-पक्षीय लोहे के सांचों में कांसे से ढाली जाती थीं।", 2, "कथन (A) सही है लेकिन कारण (R) गलत है। गाड़ियां मिट्टी (terracotta) की थीं, कांसे या लोहे के सांचे की नहीं।"),
    ("कथन (A): छिद्रित बेलनाकार बर्तनों का उपयोग अनाज के भंडारण के लिए किया जाता था।\nकारण (R): छोटे छेदों से हवा का प्रवाह बना रहता था जिससे अनाज ताज़ा रहता था।", 4, "कथन (A) और कारण (R) दोनों गलत हैं। छिद्रित बर्तन तरल छानने या धूप जलाने के लिए थे, अनाज भंडारण के लिए बड़े ठोस जार होते थे।"),
    ("कथन (A): हड़प्पा बर्तनों पर शेर सबसे अधिक चित्रित होने वाले पशु हैं।\nकारण (R): हड़प्पा राज्य में शेर को शाही शक्ति के प्रतीक के रूप में पूजा जाता था।", 4, "कथन (A) और कारण (R) दोनों गलत हैं। शेर का अंकन बर्तनों और मुहरों पर पूरी तरह अनुपस्थित है।"),
    ("कथन (A): मिट्टी की मानव आकृतियां हाथ से पिंचिंग और आवरण (appliqué) द्वारा बनाई जाती थीं।\nकारण (R): हड़प्पा वासियों के पास धातु ढलाई के लिए सांचा तकनीक का पूर्ण अभाव था।", 2, "कथन (A) सही है लेकिन कारण (R) गलत है। वे मिट्टी हाथ से बनाते थे, लेकिन धातु ढलाई के लिए उनके पास मोम ढलाई की सांचा तकनीक उपलब्ध थी।"),
    ("कथन (A): हड़प्पा बर्तनों पर बनी काली चित्रकारी धुलती या फीकी नहीं पड़ती है।\nकारण (R): मैंगनीज पेंट को मिट्टी और लाल लेप के साथ उच्च तापमान की भट्टियों में पकाया जाता था, जिससे वे स्थायी रूप से जुड़ जाते थे।", 0, "कथन (A) और कारण (R) दोनों सही हैं और कारण (R), कथन (A) की सही व्याख्या है।"),
    ("कथन (A): जानवरों के खिलौना मॉडल हड़प्पा शिल्पकारों के मनोरंजक स्वभाव को दर्शाते हैं।\nकारण (R): रस्सी पर सरकने वाले बंदर और हिलने वाले सिर वाले बैल जैसे खिलौने सरल यांत्रिकी का प्रदर्शन करते हैं।", 0, "कथन (A) और कारण (R) दोनों सही हैं और कारण (R), कथन (A) की सही व्याख्या है।")
]:
    s3_mastery_hin.append({"type": "Assertion-Reason", "q": q, "opts": hin_ar_opts, "ans": ans, "sol": sol})

# Statement-Based (5)
for q, ans, sol in [
    ("Consider the following statements regarding Mother Goddess figurines:\n1. They represent fertility and maternity worship, common in residential houses.\n2. They are found abundantly at Kalibangan and Lothal but are rare at Mohenjo-daro.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: they are virtually absent at Kalibangan/Lothal and concentrated in Sindh/Punjab."),
    ("Consider the following statements regarding Harappan pottery:\n1. Perforated cylindrical jars were likely used for liquid straining or beverage filtration.\n2. Standard painted designs include geometric, vegetal, and lion motifs.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: lion motifs are completely absent from Harappan pottery."),
    ("Consider the following statements regarding terracotta toys:\n1. Wheeled carts, movable bulls, and sliding monkeys show mechanical ingenuity.\n2. Toy carts were manufactured using lost-wax bronze casting to ensure durability.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: toy carts were made of hand-modeled terracotta, not bronze casting."),
    ("Consider the following statements regarding pottery painting:\n1. Red slip was applied to the vessel and fired before the black designs were painted.\n2. Black paint was made of manganese mineral and applied to the red slip before firing.\nWhich of the statements given above is/are correct?", 1, "Statement 2 is correct. Statement 1 is incorrect: slip and paint were both applied *before* firing to bond them together permanently."),
    ("Consider the following statements regarding terracotta production:\n1. Terracotta figurines were hand-modeled by pinching clay and applying details.\n2. Terracottas are extremely rare, representing less than 1% of recovered artifacts.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: terracottas are highly abundant, numbering in the thousands.")
]:
    s3_mastery_eng.append({"type": "Statement-Based", "q": q, "opts": mcq_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("मातृदेवी की मूर्तियों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. ये मातृत्व और उर्वरता पूजा का प्रतिनिधित्व करती हैं, जो घरों में आम थी।\n2. ये कालीबंगन और लोथल में प्रचुर मात्रा में मिली हैं लेकिन मोहनजोदड़ो में दुर्लभ हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि ये कालीबंगन/लोथल में लगभग अनुपस्थित हैं और सिंध/पंजाब में केंद्रित हैं।"),
    ("हड़प्पा मृदभांडों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. छिद्रित बेलनाकार जार का उपयोग संभवतः तरल पदार्थ या पेय को छानने के लिए किया जाता था।\n2. मानक चित्रित डिज़ाइनों में ज्यामितीय, वनस्पति और शेर के रूपांकन शामिल हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि बर्तनों पर शेर का अंकन नहीं मिलता।"),
    ("मिट्टी के खिलौनों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. पहियेदार गाड़ियां, हिलने वाले सिर वाले सांड और सरकने वाले बंदर सरल यांत्रिकी का प्रदर्शन करते हैं।\n2. खिलौना गाड़ियों का निर्माण टिकाऊपन सुनिश्चित करने के लिए लुप्त मोम कांस्य ढलाई से किया जाता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि गाड़ियां मिट्टी की थीं, कांस्य ढलाई की नहीं।"),
    ("बर्तनों पर चित्रकारी के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. बर्तन पर लाल लेप लगाकर पहले पकाया जाता था, फिर उसके ऊपर काले रेखाचित्र बनाए जाते थे।\n2. काला रंग मैंगनीज खनिज से बनता था और पकाने से पहले इसे लाल लेप के ऊपर लगाया जाता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 1, "कथन 2 सही है। कथन 1 गलत है क्योंकि दोनों लेप पकाने से पहले लगाए जाते थे।"),
    ("मिट्टी की मूर्तियों (Terracotta) के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. मिट्टी की मानव व पशु आकृतियां हाथ से पिंचिंग और आवरण (appliqué) द्वारा बनाई जाती थीं।\n2. मिट्टी की मूर्तियाँ अत्यंत दुर्लभ हैं, जो प्राप्त कलाकृतियों का 1% से भी कम हिस्सा हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि ये अत्यंत प्रचुर मात्रा में मिली हैं।")
]:
    s3_mastery_hin.append({"type": "Statement-Based", "q": q, "opts": hin_mcq_opts, "ans": ans, "sol": sol})

# Why (3)
for q, sol in [
    ("Why did the Mother Goddess cult focus on hand-modeled terracottas rather than stone or metal statues?", "Terracotta was a highly accessible, local domestic medium made from common alluvial clay, allowing every household to have a private ritual icon. Stone and metal were scarce, costly, and imported, reserved for elite administrative or symbolic markers. Hand-modeling allowed personal, decentralized production of household fertility charms."),
    ("Why was manganese used in the black pigment painted on Harappan pottery?", "Manganese dioxide is a mineral pigment that remains chemically stable and does not vaporize or burn off at the high firing temperatures (around 800°C to 1000°C) of Harappan updraft kilns. Firing fused the manganese permanently with the clay slip, creating a durable, non-fading black design that survived for millennia under the soil."),
    ("Why did Harappan toy makers develop mechanical joints in terracotta toys (like moving heads or sliding monkeys)?", "Developing mechanical joints shows a high level of child-centered leisure and creativity. By threading strings through hollow passages or utilizing sliding sleeves, craftsmen made interactive, kinetic toys that mimicked natural movements, reflecting both mechanical curiosity and a peaceful, settled urban society with resources for children's play.")
]:
    s3_mastery_eng.append({"type": "Why", "q": q, "sol": sol})

for q, sol in [
    ("मातृदेवी की पूजा पत्थर या धातु की मूर्तियों के बजाय हाथ से गढ़ी मिट्टी की मूर्तियों पर क्यों केंद्रित थी?", "मिट्टी (terracotta) एक अत्यंत सुलभ और स्थानीय माध्यम था जो मैदानी इलाकों की जलोढ़ मिट्टी से बनाया जा सकता था, जिससे प्रत्येक परिवार को अपना निजी घरेलू अनुष्ठानिक प्रतीक रखने की सुविधा मिलती थी। पत्थर और धातु दुर्लभ, महंगे और आयातित थे, जिन्हें प्रशासनिक प्रतीकों के लिए बचाकर रखा जाता था। हाथ से मूर्ति गढ़ना घरेलू स्तर पर विकेंद्रीकृत उत्पादन को बढ़ावा देता था।"),
    ("हड़प्पा बर्तनों पर चित्रकारी के लिए काले रंग में मैंगनीज का उपयोग क्यों किया जाता था?", "मैंगनीज डाइऑक्साइड एक ऐसा खनिज पिगमेंट है जो हड़प्पा की उच्च तापमान वाली भट्टियों (लगभग 800°C से 1000°C) में रासायनिक रूप से स्थिर रहता है और जलता या उड़ता नहीं है। भट्टी में पकने से मैंगनीज स्थायी रूप से मिट्टी के लेप के साथ मिलकर जुड़ जाता था, जिससे अत्यंत टिकाऊ काला रेखाचित्र बनता था जो हजारों वर्षों तक जमीन में रहने पर भी फीका नहीं पड़ा।"),
    ("हड़प्पा के खिलौना निर्माताओं ने मिट्टी के खिलौनों में यांत्रिक जोड़ (जैसे हिलने वाले सिर या सरकने वाले बंदर) क्यों विकसित किए?", "खिलौनों में यांत्रिक जोड़ बनाना बच्चों के मनोरंजन और रचनात्मकता के उच्च स्तर को दर्शाता है। खोखले हिस्सों में धागा पिरोकर या सरकने वाली आस्तीन बनाकर शिल्पकारों ने गतिशील खिलौने बनाए जो प्राकृतिक हरकतों की नकल करते थे। यह यांत्रिक जिज्ञासा और एक शांत, समृद्ध शहरी समाज को दर्शाता है जहाँ बच्चों के खेल के लिए पर्याप्त फुर्सत थी।")
]:
    s3_mastery_hin.append({"type": "Why", "q": q, "sol": sol})

# How (3)
for q, sol in [
    ("How did Harappan potters manufacture and paint a standard red-and-black storage jar?", "Potters shaped the storage jar on a fast-spinning wheel, dried it partially, and coated it with a red clay slip rich in iron oxide. Once the slip dried, they painted geometric or nature designs over it using a black pigment made of manganese dioxide. Finally, they stacked the painted vessel in an updraft kiln and fired it at high temperatures, permanently bonding the slip and black designs to the clay body."),
    ("How did the pinching and appliqué techniques work in creating a Mother Goddess figurine?", "Craftsmen pinched wet clay with their fingers to shape the nose, chest, and limbs from a single lump. They then made separate small coils, pellets, and flat clay strips. Using the appliqué method (pressing these clay pieces onto the main body), they attached the fan headdress, cup-like panniers, eyes, and layered necklaces. The entire hand-modeled figure was then baked in a kiln."),
    ("How does the perforated jar function as a strainer, and what does it suggest about Harappan lifestyle?", "Perforated jars are cylindrical clay vessels with numerous small holes drilled through the walls. To filter liquids, the jar was filled with a mixture (like fermented beer mash or curds) allowing the clear liquid to strain through the holes into a larger solid basin. This suggests that the Harappans brewed fermented beverages, strained dairy products (like cheese), or burned incense where holes allowed ventilation.")
]:
    s3_mastery_eng.append({"type": "How", "q": q, "sol": sol})

for q, sol in [
    ("हड़प्पा के कुम्हार एक मानक लाल और काले रंग के अनाज जार का निर्माण और चित्रकारी कैसे करते थे?", "कुम्हार पहले चाक पर बर्तन का आकार देते थे, उसे थोड़ा सुखाकर लोहे के ऑक्साइड से भरपूर लाल मिट्टी का लेप (slip) चढ़ाते थे। लेप सूखने पर मैंगनीज डाइऑक्साइड के काले रंग से उसके ऊपर ज्यामितीय या प्राकृतिक आकृतियां चित्रित करते थे। अंत में वे चित्रित बर्तन को भट्टी में रखकर उच्च तापमान पर पकाते थे जिससे लाल लेप और काले रंग के रेखाचित्र मिट्टी के साथ हमेशा के लिए बंध जाते थे।"),
    ("मातृदेवी की मूर्ति के निर्माण में पिंचिंग और आवरण (appliqué) तकनीकें कैसे काम करती थीं?", "शिल्पकार उंगलियों से गीली मिट्टी को दबाकर (पिंच करके) एक ही लोई से नाक, छाती और हाथ-पैर का मूल आकार बनाते थे। फिर वे अलग से मिट्टी की गोलियां, पट्टियां और पेंच बनाते थे। आवरण (appliqué) विधि द्वारा इन टुकड़ों को मुख्य शरीर पर दबाकर चिपकाया जाता था जिससे आंखें, पंखे जैसा मुकुट, प्याले और गले के हार बनाए जाते थे। अंत में इस हस्तनिर्मित आकृति को भट्टी में पकाया जाता था।"),
    ("छिद्रित जार एक छन्नी के रूप में कैसे काम करता था, और यह हड़प्पा की जीवनशैली के बारे में क्या संकेत देता है?", "छिद्रित जार बेलनाकार मिट्टी के बर्तन होते हैं जिनमें दीवारों पर कई छोटे-छोटे छेद होते थे। तरल छानने के लिए जार में मिश्रण (जैसे किण्वित अनाज का घोल या छाछ) भरा जाता था जिससे साफ तरल छेदों से रिसकर नीचे रखे बड़े ठोस बर्तन में जमा हो जाता था। यह दर्शाता है कि हड़प्पा वासी मादक पेय छानते थे, डेयरी उत्पाद (जैसे पनीर) बनाते थे, या धूप जलाते थे जहाँ छिद्रों से हवा का प्रवाह आवश्यक था।")
]:
    s3_mastery_hin.append({"type": "How", "q": q, "sol": sol})

# Case Study (3)
for q, sol in [
    ("Case Study: Excavations at Mohenjo-daro yielded hundreds of terracotta Mother Goddess figurines, whereas sites in Gujarat (like Lothal, Dholavira, and Surkotada) yielded virtually none. Discuss what this regional distribution demonstrates about Indus religious and social life.", "This demonstrates significant regional variation in religious beliefs and domestic cult practices within the Indus Valley Civilisation. While the civilization shared uniform weights, measures, and trade networks, the Mother Goddess cult was a regional tradition concentrated in the Indus plains of Sindh and Punjab, but not adopted in Gujarat or Rajasthan. This suggests that the Harappan empire was not a culturally homogeneous, monolithically ruled state, but a federation of regions with distinct local socio-religious identities."),
    ("Case Study: Large red-and-black painted jars containing black intersecting circles and peacock motifs have been found in Harappan graves at Harappa, and matching shards have been excavated in Oman (West Asia). Analyze what this tells us about the lifecycle of Harappan pottery.", "This shows that Harappan pottery was highly valued both as a prestigious grave offering and as a durable packaging container for international maritime trade. The jars found in Oman were used to transport surplus Harappan agricultural liquid goods (like oil or wine) across the Arabian Sea. Once empty, their artistic quality made them valuable items. Finding them in Harappan graves indicates that these standardized decorated jars were prized personal possessions placed with the dead for use in the afterlife."),
    ("Case Study: The toy carts found at Harappa are made of heavy baked terracotta, with solid clay wheels and holes for wooden axles, modeled realistically after actual working ox-carts. Compare these with the lack of military war-chariot representations in Harappan art. What does this reveal about their society?", "This reveals that Harappan vehicular technology was focused entirely on agriculture, bulk transport, and civic trade rather than warfare. In contemporary Egypt and Mesopotamia, art was dominated by military war-chariots crushing enemies. The Harappan toy carts represent slow, heavy agricultural transport used to carry grain from fields to city granaries. This reinforces the archaeological picture of a peaceful, commerce-oriented society that prioritized domestic transport over military conquests.")
]:
    s3_mastery_eng.append({"type": "Case Study", "q": q, "sol": sol})

for q, sol in [
    ("केस स्टडी: मोहनजोदड़ो से सैकड़ों मिट्टी की मातृदेवी की मूर्तियां मिली हैं, लेकिन गुजरात के स्थलों (जैसे लोथल, धोलावीरा और सुरकोटदा) से लगभग एक भी नहीं मिली है। चर्चा करें कि यह क्षेत्रीय वितरण हड़प्पा के धार्मिक और सामाजिक जीवन के बारे में क्या दर्शाता है।", "यह दर्शाता है कि सिंधु घाटी सभ्यता के भीतर धार्मिक विश्वासों और घरेलू पूजा पद्धतियों में महत्वपूर्ण क्षेत्रीय भिन्नताएं थीं। यद्यपि सभ्यता में समान बाट, माप और व्यापारिक नेटवर्क साझा थे, लेकिन मातृदेवी की पूजा सिंध और पंजाब के मैदानी क्षेत्रों तक सीमित एक क्षेत्रीय परंपरा थी, जिसे गुजरात या राजस्थान में नहीं अपनाया गया। यह इस विचार का समर्थन करता है कि हड़प्पा सभ्यता कोई सांस्कृतिक रूप से समरूप राज्य नहीं था, बल्कि विशिष्ट स्थानीय सामाजिक-धार्मिक पहचान वाले क्षेत्रों का एक संघ था।"),
    ("केस स्टडी: हड़प्पा की कब्रों से काले रंग से रंगे ज्यामितीय वृत्त और मयूर आकृतियों वाले बड़े लाल जार मिले हैं, और ओमान (पश्चिमी एशिया) से भी ऐसे ही बर्तनों के टुकड़े मिले हैं। यह हड़प्पा मृदभांडों के जीवन-चक्र के बारे में क्या बताता है?", "यह दर्शाता है कि हड़प्पा के बर्तनों का मूल्य कब्रों में दी जाने वाली भेंट और अंतर्राष्ट्रीय समुद्री व्यापार में टिकाऊ पैकेजिंग कंटेनर दोनों के रूप में था। ओमान में मिले जार का उपयोग अरब सागर के पार तेल या शराब जैसे तरल उत्पादों को ले जाने के लिए किया जाता था। खाली होने पर भी उनकी कलात्मक गुणवत्ता उन्हें मूल्यवान बनाती थी। कब्रों में इनका मिलना यह दर्शाता है कि ये शानदार सजे जार व्यक्तिगत प्रिय वस्तुएं थे जिन्हें परलोक में उपयोग के लिए मृत व्यक्ति के साथ दफनाया जाता था।"),
    ("केस स्टडी: हड़प्पा से मिली खिलौना गाड़ियां ठोस पहियों और धुरी के छेदों के साथ भारी पकी मिट्टी की बनी हैं, जो वास्तविक बैलगाड़ियों की सजीव नकल हैं। हड़प्पा कला में युद्ध रथों के चित्रण के अभाव से इसकी तुलना करें। यह उनके समाज के बारे में क्या दर्शाता है?", "यह दर्शाता है कि हड़प्पा की वाहन तकनीक युद्ध के बजाय पूरी तरह कृषि, माल परिवहन और नागरिक व्यापार पर केंद्रित थी। समकालीन मिस्र और मेसोपोटामिया की कला में शत्रुओं को कुचलते हुए युद्ध रथों का अंकन हावी था। हड़प्पा की खिलौना गाड़ियां अनाज को खेतों से शहर के अन्नागारों तक ले जाने वाले भारी कृषि परिवहन को दर्शाती हैं। यह एक शांतिप्रिय और वाणिज्य-उन्मुख समाज की पुष्टि करता है जो सैन्य विजय के स्थान पर घरेलू व्यापार को प्राथमिकता देता था।")
]:
    s3_mastery_hin.append({"type": "Case Study", "q": q, "sol": sol})

# Teach Concept (3)
for q, sol in [
    ("Teach the concept of the 'Applique Technique' in clay modeling, using the headdress of the Mother Goddess as an example.", "Applique is a sculpting technique in clay-working where decorative elements are shaped separately and then attached to the main body. First, the artist models the primary body shape. Then, they roll separate coils of clay for necklaces, pinch flat disc pellets for eyes, and press flat clay strips to form the fan-shaped headdress and cup-like panniers. Using water or thin clay slip as a binder, they press these pieces onto the wet body. When fired, the pieces fuse into a single decorated figurine. The elaborate Mother Goddess headdress is the classic example of applique, creating highly layered, 3D ornamentations on a simple hand-modeled figure."),
    ("Explain the chemistry and firing technology of Harappan 'Red-and-Black Painted Pottery' to a class.", "Red-and-Black painted pottery is a highly standardized wheel-made ceramic. The red color comes from iron oxide slip applied to the clay before firing. Firing the clay in an oxidizing atmosphere converts the iron to red hematite. The black designs were painted using manganese dioxide mineral pigment. During firing, the manganese bonds with the clay, creating a permanent black design that does not wash off. The vessels were baked in advanced updraft kilns where heat was circulated through holes under a chamber floor, ensuring even temperature distribution (around 800-900°C) and uniform firing of the slip and paint."),
    ("Teach the historical significance of Harappan terracotta toys as evidence of childhood, leisure, and social stability.", "Terracotta toys (wheeled carts, bird whistles, sliding monkeys, movable-head bulls, clay marbles) are rare and important evidence of childhood and family life in the ancient world. In many Bronze Age societies, children are archaeologically invisible, or only depicted as miniature laborers. The abundance of interactive, moving-part toys in the Indus Valley shows that Harappan society had a stable, prosperous economy that could allocate resource-surplus and craftsman labor to create items for children's amusement and cognitive play. The focus on peaceful toys (and the complete absence of toy weapons) suggests a stable, non-militaristic civic culture.")
]:
    s3_mastery_eng.append({"type": "Teach Concept", "q": q, "sol": sol})

for q, sol in [
    ("मिट्टी मॉडलिंग में 'आवरण (appliqué) तकनीक' की अवधारणा को मातृदेवी के मुकुट का उदाहरण देकर समझाएं।", "आवरण (appliqué) मिट्टी के काम में एक मूर्तिकला तकनीक है जहां सजावटी तत्वों को अलग से आकार दिया जाता है और फिर मुख्य शरीर पर चिपकाया जाता है। मूर्तिकार पहले शरीर का मूल ढांचा बनाता है। फिर वह हार के लिए अलग से मिट्टी की बत्तियां बनाता है, आंखों के लिए गोल मिट्टी की गोलियां बनाता है और पंखे जैसी शाल व प्याले बनाने के लिए मिट्टी की सपाट पट्टियां दबाता है। पानी या पतले गीले लेप का उपयोग करके इन हिस्सों को गीले शरीर पर दबाकर चिपका दिया जाता है। पकाने पर ये सभी अंग आपस में जुड़ जाते हैं। मातृदेवी का भारी मुकुट आवरण तकनीक का सबसे उत्कृष्ट उदाहरण है, जो साधारण हाथ से बनी मूर्ति पर अत्यधिक स्तरित, 3D आभूषण बनाता है।"),
    ("एक कक्षा को हड़प्पा के 'लाल और काले चित्रित मृदभांड' की रसायन विज्ञान और पकाने की तकनीक समझाएं।", "लाल-काले चित्रित मृदभांड चाक पर बने मानक मिट्टी के बर्तन हैं। बर्तनों का लाल रंग पकाने से पहले चढ़ाई गई लोहे के लाल ऑक्साइड (गेरू) की परत से आता है। भट्टी की ऑक्सीजन युक्त हवा में पकाने पर लोहा लाल हेमेटाइट में बदल जाता है। काले रेखाचित्र मैंगनीज डाइऑक्साइड खनिज पिगमेंट से रंगे जाते थे। पकाने के दौरान मैंगनीज मिट्टी के साथ स्थायी रूप से जुड़ जाता था जिससे काला रंग पक्का हो जाता था। इन बर्तनों को उन्नत भट्टियों में पकाया जाता था जहाँ छिद्रित फर्श के नीचे से आंच उठती थी जिससे समान तापमान (लगभग 800-900°C) प्राप्त होता था और लेप व चित्रकारी समान रूप से पकती थी।"),
    ("बचपन, फुर्सत और सामाजिक स्थिरता के साक्ष्य के रूप में हड़प्पा के मिट्टी के खिलौनों के ऐतिहासिक महत्व को समझाएं।", "मिट्टी के खिलौने (पहिएदार गाड़ियां, पक्षीनुमा सीटियां, सरकने वाले बंदर, हिलने वाले बैल, कंचे) प्राचीन दुनिया में बच्चों और पारिवारिक जीवन के दुर्लभ पुरातात्विक साक्ष्य हैं। कई कांस्य युगीन समाजों में बच्चों का कोई साक्ष्य नहीं मिलता या उन्हें केवल बाल श्रमिकों के रूप में दिखाया जाता था। सिंधु घाटी में गतिशील खिलौनों की प्रचुरता यह दर्शाती है कि समाज में एक स्थिर, समृद्ध अर्थव्यवस्था थी जो बच्चों के मनोरंजन और मानसिक विकास के लिए खिलौने बनाने में संसाधन लगा सकती थी। शांतिपूर्ण खिलौनों पर ध्यान (और खिलौना हथियारों का पूर्ण अभाव) एक स्थिर, गैर-सैन्य नागरिक संस्कृति का संकेत देता है।")
]:
    s3_mastery_hin.append({"type": "Teach Concept", "q": q, "sol": sol})


# Load content and inject questions
with open(ENG_PATH, "r", encoding="utf-8") as f:
    eng_data = json.load(f)

with open(HIN_PATH, "r", encoding="utf-8") as f:
    hin_data = json.load(f)

# Ensure sections exist
assert len(eng_data["deepDive"]["sections"]) == 3
assert len(hin_data["deepDive"]["sections"]) == 3

# Inject Section 1
eng_data["deepDive"]["sections"][0]["masteryZone"] = s1_mastery_eng
hin_data["deepDive"]["sections"][0]["masteryZone"] = s1_mastery_hin

# Inject Section 2
eng_data["deepDive"]["sections"][1]["masteryZone"] = s2_mastery_eng
hin_data["deepDive"]["sections"][1]["masteryZone"] = s2_mastery_hin

# Inject Section 3
eng_data["deepDive"]["sections"][2]["masteryZone"] = s3_mastery_eng
hin_data["deepDive"]["sections"][2]["masteryZone"] = s3_mastery_hin

# Write back files
print(f"Injecting mastery questions into {ENG_PATH}")
with open(ENG_PATH, "w", encoding="utf-8") as f:
    json.dump(eng_data, f, ensure_ascii=False, indent=2)

print(f"Injecting mastery questions into {HIN_PATH}")
with open(HIN_PATH, "w", encoding="utf-8") as f:
    json.dump(hin_data, f, ensure_ascii=False, indent=2)

print("Mastery questions injection complete!")
