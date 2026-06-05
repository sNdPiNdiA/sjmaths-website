import json
import os

ENG_PATH = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\HarappanIndus-Valley-Civilisation\Socio-Cultural-Aspects-of-Indus-Valley-Civilisation\content.json"
HIN_PATH = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\HarappanIndus-Valley-Civilisation\Socio-Cultural-Aspects-of-Indus-Valley-Civilisation\hi\content.json"

mcq_opts = ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"]
ar_opts = [
    "Both A and R are true and R is the correct explanation of A",
    "Both A and R are true but R is not the correct explanation of A",
    "A is true but R is false",
    "A is false but R is true"
]

hin_mcq_opts = ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"]
hin_ar_opts = [
    "A और R दोनों सत्य हैं और R, A की सही व्याख्या है",
    "A और R दोनों सत्य हैं लेकिन R, A की सही व्याख्या नहीं है",
    "A सत्य है लेकिन R असत्य है",
    "A असत्य है लेकिन R सत्य है"
]

# =========================================================================
# SECTION 1: SOCIAL STRUCTURE, DRESS, ORNAMENTS & DIET
# =========================================================================
s1_mastery_eng = []
s1_mastery_hin = []

# MCQ (5)
for q, opts, ans, sol in [
    ("Which Harappan site has yielded direct evidence of cosmetic items like cinnabar lipsticks?", ["Chanhudaro", "Mohenjo-daro", "Harappa", "Lothal"], 0, "Chanhudaro in Sindh, Pakistan, is famous for yielding cosmetic containers and lipsticks made from cinnabar."),
    ("The abundant terracotta Mother Goddess figurines have led many historians to suggest that Harappan society was:", ["Matriarchal or matrilineal", "Patriarchal and militaristic", "Exclusively ruled by a single king", "Divided into birth-based caste guilds"], 0, "The high veneration of female deities and fertility figurines points towards a matriarchal or matrilineal social focus."),
    ("Both men and women in Harappan cities wore garments primarily manufactured from which fibers?", ["Cotton and wool", "Silk and flax", "Hemp and jute", "Linen and leather"], 0, "Harappans were pioneers in cotton cultivation and also used wool for winter clothing."),
    ("Which dietary grain was NOT commonly cultivated in the northern metropolitan centers like Harappa and Kalibangan?", ["Rice", "Wheat", "Barley", "Sesame"], 0, "While wheat and barley were staples in the north, rice grains have only been recovered from southern sites like Lothal and Rangpur in Gujarat."),
    ("Grave findings containing necklaces, armlets, and rings buried with both male and female skeletons indicate that:", ["Ornaments were worn by both genders", "Men were forbidden from wearing jewelry", "Only the ruling priest class wore metal", "Jewelry was strictly used as currency"], 0, "The presence of jewelry in both male and female graves confirms ornaments were fashionable for both genders.")
]:
    s1_mastery_eng.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("किस हड़प्पा स्थल से लिपस्टिक (हिंगुल/cinnabar) जैसे सौंदर्य प्रसाधनों के अवशेष मिले हैं?", ["चन्हुदड़ो", "मोहनजोदड़ो", "हड़प्पा", "लोथल"], 0, "सिंध में स्थित चन्हुदड़ो से सौंदर्य प्रसाधनों के डिब्बे और लिपस्टिक के अवशेष मिले हैं।"),
    ("मिट्टी की प्रचुर मात्रा में मिली मातृदेवी की मूर्तियों से इतिहासकारों ने हड़प्पा समाज के बारे में क्या अनुमान लगाया है?", ["मातृसत्तात्मक या मातृवंशीय समाज", "पितृसत्तात्मक और सैन्यवादी समाज", "एकल राजा का निरंकुश शासन", "जन्म-आधारित जाति व्यवस्था"], 0, "मातृदेवियों और स्त्री उर्वरता की अत्यधिक पूजा समाज में महिलाओं के उच्च स्थान और मातृसत्तात्मक स्वरूप को दर्शाती है।"),
    ("हड़प्पा शहरों में स्त्री और पुरुष दोनों मुख्य रूप से किन धागों से बने वस्त्र पहनते थे?", ["सूती और ऊनी", "रेशमी और सन (flax)", "भांग (hemp) और जूट", "लिनन और चमड़ा"], 0, "हड़प्पा वासी कपास उगाने के अग्रदूत थे और सर्दियों के कपड़ों के लिए ऊन का उपयोग भी करते थे।"),
    ("हड़प्पा और कालीबंगन जैसे उत्तरी महानगरों में कौन सा अनाज सामान्य रूप से नहीं उगाया जाता था?", ["चावल", "गेहूं", "जौ", "तिल"], 0, "गेहूं और जौ उत्तर के मुख्य भोजन थे, जबकि चावल के अवशेष केवल लोथल और रंगपुर (गुजरात) जैसे दक्षिणी स्थलों से मिले हैं।"),
    ("कब्रों में स्त्री और पुरुष दोनों के कंकालों के साथ हार, बाजूबंद और अंगूठियाँ मिलने से क्या प्रमाणित होता है?", ["आभूषण स्त्री और पुरुष दोनों पहनते थे", "पुरुषों को आभूषण पहनना वर्जित था", "केवल पुरोहित वर्ग ही धातु पहनता था", "आभूषणों का उपयोग केवल मुद्रा के रूप में होता था"], 0, "दोनों लिंगों की कब्रों से आभूषणों की प्राप्ति यह सिद्ध करती है कि गहने पहनना स्त्री और पुरुष दोनों में प्रचलित था।")
]:
    s1_mastery_hin.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# Multi-Correct MCQ (5)
for q, opts, ans, sol in [
    ("Identify the social groups that populated Harappan cities: (Select all that apply)", ["The ruling administrative elite", "Wealthy merchants and scribes", "Artisans, craftsmen, and laborers", "Monastic orders of Buddhist monks"], [0, 1, 2], "The society was divided into administrators, merchants/scribes, and artisans/laborers. Buddhism arose much later."),
    ("Which cosmetic and grooming items have been discovered at Indus sites? (Select all that apply)", ["Ivory hair combs and hairpins", "Bronze mirrors with detailed handles", "Cinnabar lipsticks and collyrium eyeliner", "Silver-backed glass pocket mirrors"], [0, 1, 2], "Combs, bronze mirrors, and cinnabar lipsticks were common. Glass mirrors did not exist in the Bronze Age."),
    ("Select the cereal crops cultivated by Harappan agriculturalists: (Select all that apply)", ["Wheat", "Barley", "Millets (in Gujarat)", "Maize"], [0, 1, 2], "Wheat, barley, and millets were cultivated. Maize is a New World crop introduced much later."),
    ("Which features characterize the status of women in Harappan society? (Select all that apply)", ["Abundant representations as Mother Goddesses", "Involvement in textile spinning and weaving", "Depictions with elaborate hairstyles and ornaments", "Exclusion from public festivals and assemblies"], [0, 1, 2], "Women were worshipped as goddesses, worked in weaving, and wore complex hairstyles. There is no evidence of exclusion."),
    ("What findings indicate class differences in Harappan society? (Select all that apply)", ["Varying sizes of residential houses (large multi-room vs. barracks)", "Varying quantity and quality of pottery in graves", "Presence of imported luxury items in wealthy quarters", "Distinct legal codes inscribed on city walls"], [0, 1, 2], "Housing variations, grave goods, and imported luxuries show class differences. No written legal codes have been found.")
]:
    s1_mastery_eng.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("हड़प्पा शहरों में रहने वाले सामाजिक समूहों की पहचान करें: (सभी लागू विकल्प चुनें)", ["प्रशासक और शासक वर्ग", "धनी व्यापारी और लिपिक", "शिल्पी, कारीगर और मजदूर", "बौद्ध भिक्षुओं के संघ"], [0, 1, 2], "समाज प्रशासकों, व्यापारियों और कारीगरों/मजदूरों में बंटा था। बौद्ध धर्म का उदय बहुत बाद में हुआ था।"),
    ("सिंधु स्थलों से कौन से सौंदर्य प्रसाधन और श्रृंगार के सामान मिले हैं? (सभी लागू विकल्प चुनें)", ["हाथीदांत की कंघियाँ और केश सूइयाँ", "हैंडल वाले कांसे के दर्पण", "लिपस्टिक (हिंगुल) और आँखों का काजल", "कांच के बने आधुनिक शीशे"], [0, 1, 2], "कंघियाँ, कांसे के दर्पण और लिपस्टिक/काजल आम थे। कांस्य युग में कांच के शीशे नहीं बनते थे।"),
    ("हड़प्पा के किसानों द्वारा उगाई जाने वाली फसलों का चयन करें: (सभी लागू विकल्प चुनें)", ["गेहूं", "जौ", "बाजरा (गुजरात में)", "मक्का"], [0, 1, 2], "गेहूं, जौ और बाजरा उगाए जाते थे। मक्का अमेरिका की फसल है जो भारत में बहुत बाद में आई।"),
    ("हड़प्पा समाज में महिलाओं की स्थिति को कौन से लक्षण दर्शाते हैं? (सभी लागू विकल्प चुनें)", ["मातृदेवी के रूप में अत्यधिक मूर्तियाँ मिलना", "सूत कातने और बुनाई के काम में भागीदारी", "जटिल केशविन्यास और आभूषणों के चित्र मिलना", "सार्वजनिक उत्सवों और सभाओं से पूर्ण प्रतिबंध"], [0, 1, 2], "महिलाएं देवियों के रूप में पूज्य थीं, बुनाई करती थीं और जटिल हेयर स्टाइल रखती थीं। अलगाव का कोई साक्ष्य नहीं है।"),
    ("हड़प्पा समाज में वर्ग भेद का संकेत किन पुरातात्विक साक्ष्यों से मिलता है? (सभी लागू विकल्प चुनें)", ["आवासीय घरों के आकार में भिन्नता (बड़े मकान बनाम बैरक)", "कब्रों में रखे बर्तनों की गुणवत्ता और संख्या में अंतर", "धनी बस्तियों में आयातित विलासिता की वस्तुओं की प्राप्ति", "शहर की दीवारों पर खोदे गए अलग-अलग कानून"], [0, 1, 2], "मकानों का आकार, कब्र के बर्तन और विलासिता का सामान वर्ग भेद दर्शाते हैं। दीवारों पर कोई कानून नहीं लिखे मिले हैं।")
]:
    s1_mastery_hin.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# True/False (8)
for q, ans, sol in [
    ("Harappans cultivated cotton and wore cotton clothing.", True, "True. They were pioneers in cotton cultivation and wore light cotton garments."),
    ("Only women wore ornaments in Harappan society.", False, "False. Men also wore necklaces, armlets, and rings, as confirmed by grave findings."),
    ("Direct evidence of lipstick made from cinnabar was found at Chanhudaro.", True, "True. Cinnabar lipsticks have been recovered from Chanhudaro."),
    ("A hereditary, rigid caste system was established during the Mature Harappan phase.", False, "False. Social stratification existed but there is no evidence of a birth-based caste system."),
    ("Rice was the primary staple crop consumed in all northern Harappan cities.", False, "False. Wheat and barley were the northern staples; rice was limited to Gujarat."),
    ("Bronze mirrors with polished surfaces were used for personal grooming.", True, "True. Polished bronze plates served as mirrors for the wealthy."),
    ("The Priest-King statue is shown wearing a shawl with trefoil decorations.", True, "True. The bust features a patterned shawl draped over the left shoulder."),
    ("Harappans were entirely vegetarian and did not consume fish or poultry.", False, "False. Animal bones show they consumed fish, mutton, beef, and poultry.")
]:
    s1_mastery_eng.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("हड़प्पा वासी कपास उगाते थे और सूती कपड़े पहनते थे।", True, "सत्य। वे कपास की खेती के अग्रदूत थे और सूती कपड़ों का प्रयोग करते थे।"),
    ("हड़प्पा समाज में केवल महिलाएं ही आभूषण पहनती थीं।", False, "असत्य। पुरुष भी हार, बाजूबंद और अंगूठियां पहनते थे, जैसा कब्रों से पता चलता है।"),
    ("लिपस्टिक के प्रत्यक्ष साक्ष्य चन्हुदड़ो से मिले हैं।", True, "सत्य। चन्हुदड़ो से हिंगुल आधारित लिपस्टिक प्राप्त हुई है।"),
    ("परिपक्व हड़प्पा काल में जन्म-आधारित कठोर जाति व्यवस्था स्थापित हो चुकी थी।", False, "असत्य। वर्ग विभाजन था लेकिन जन्म-आधारित जाति व्यवस्था का कोई साक्ष्य नहीं है।"),
    ("उत्तरी हड़प्पा के सभी शहरों में चावल मुख्य खाद्य फसल थी।", False, "असत्य। उत्तर में गेहूं और जौ मुख्य अनाज थे; चावल केवल गुजरात तक सीमित था।"),
    ("श्रृंगार के लिए कांसे के चमकदार दर्पणों का उपयोग किया जाता था।", True, "सत्य। धातु के पॉलिश किए गए दर्पण विलासिता के साधन थे।"),
    ("पुरोहित-राजा की मूर्ति को तिपतिया पैटर्न वाले शॉल ओढ़े दिखाया गया है।", True, "सत्य। पुरोहित-राजा के बाएं कंधे पर तिपतिया सज्जा वाला शॉल है।"),
    ("हड़प्पा वासी पूरी तरह शाकाहारी थे और मछली या मांस नहीं खाते थे।", False, "असत्य। हड्डियों के अवशेष प्रमाणित करते हैं कि वे मछली, भेड़ और मवेशियों का मांस खाते थे।")
]:
    s1_mastery_hin.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

# Fill Blank (8)
for q, ans, sol in [
    ("Direct evidence of lipsticks made from cinnabar has been found at __________.", "Chanhudaro", "Chanhudaro yielded cosmetic items including lipsticks."),
    ("The primary plant fibers used for spinning and weaving garments were __________.", "cotton", "Cotton was spun and woven extensively by Harappan weavers."),
    ("The trefoil-decorated shawl is worn by the steatite sculpture called the __________.", "Priest-King", "The Priest-King bust features the trefoil shawl drape."),
    ("Women kept their eyeliner, known as __________, in small bronze or clay pots.", "collyrium", "Collyrium (kajal) was stored in small cosmetics pots."),
    ("At Lothal and Rangpur, agriculturalists cultivated __________ instead of northern wheat.", "rice", "Rice husks and grains were recovered in Gujarat sites."),
    ("The high status of women is inferred from abundant terracotta __________ figurines.", "Mother Goddess", "Mother Goddess figurines indicate female reverence."),
    ("Harappans styled their hair using ornamental pins made of __________.", "ivory", "Ivory and bone hairpins were used to secure hairstyles."),
    ("Common laborers lived in small row quarters or __________ near industrial zones.", "barracks", "Balked quarters or barracks housed laborers at Harappa.")
]:
    s1_mastery_eng.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("हिंगुल से बनी लिपस्टिक के अवशेष प्रसिद्ध हड़प्पा स्थल __________ से मिले हैं।", "चन्हुदड़ो", "चन्हुदड़ो से सौंदर्य प्रसाधन सामग्री और लिपस्टिक मिली है।"),
    ("कपड़े बुनने और सूत कातने के लिए प्रयुक्त होने वाला मुख्य पादप रेशा __________ था।", "कपास", "कपास (cotton) की खेती और बुनाई बड़े पैमाने पर की जाती थी।"),
    ("तिपतिया डिजाइनों से सजा शॉल ओढ़े पुरुष की मूर्ति को __________ कहा जाता है।", "पुरोहित-राजा", "पुरोहित-राजा (Priest-King) की मूर्ति शॉल ओढ़े दर्शाई गई है।"),
    ("महिलाएं आँखों का काजल, जिसे __________ कहते थे, छोटी डिब्बियों में रखती थीं।", "काजल", "काजल (collyrium) को मिट्टी या कांसे की डिब्बियों में रखा जाता था।"),
    ("लोथल और रंगपुर में उत्तर के गेहूं के स्थान पर __________ की खेती के साक्ष्य मिले हैं।", "चावल", "गुजरात के स्थलों से चावल की भूसी और दाने प्राप्त हुए हैं।"),
    ("महिलाओं की उच्च स्थिति का अनुमान मिट्टी की प्रचुर मात्रा में मिली __________ की मूर्तियों से लगाया जाता है।", "मातृदेवी", "मातृदेवी (Mother Goddess) की मूर्तियाँ समाज में नारी के सम्मान को दर्शाती हैं।"),
    ("हड़प्पा वासी अपने बालों को संवारने के लिए __________ से बनी केश सूइयों का प्रयोग करते थे।", "हाथीदांत", "हाथीदांत (ivory) और हड्डियों की बनी हेयरपिन का उपयोग किया जाता था।"),
    ("औद्योगिक क्षेत्रों के पास सामान्य मजदूर छोटी कतारों वाले मकानों या __________ में रहते थे।", "बैरकों", "हड़प्पा और अन्य शहरों में मजदूरों के रहने के लिए छोटे कमरे या बैरक मिले हैं।")
]:
    s1_mastery_hin.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

# Match the Following (3)
s1_mastery_eng.extend([
    {
        "type": "Match the Following",
        "q": "Match the sites with their representative socio-dietary findings:",
        "items": [{"left": "I. Chanhudaro", "key": "A"}, {"left": "II. Lothal", "key": "B"}, {"left": "III. Harappa", "key": "C"}],
        "options": [{"val": "A", "text": "A. Cinnabar lipsticks and cosmetic jars"}, {"val": "B", "text": "B. Rice husks and double burial graves"}, {"val": "C", "text": "C. Row-quarters (barracks) for manual laborers"}],
        "sol": "Chanhudaro has cosmetics, Lothal has rice husks, and Harappa has laborer barracks."
    },
    {
        "type": "Match the Following",
        "q": "Match the social status with their housing quarters:",
        "items": [{"left": "I. Administrative Elites", "key": "A"}, {"left": "II. Rich Merchants", "key": "B"}, {"left": "III. Working Laborers", "key": "C"}],
        "options": [{"val": "A", "text": "A. Fortified high Citadel buildings"}, {"val": "B", "text": "B. Large multi-room brick houses in Lower Town"}, {"val": "C", "text": "C. Small two-room row barracks near factories"}],
        "sol": "Elites lived on Citadels, merchants in large Lower Town houses, and laborers in barracks."
    },
    {
        "type": "Match the Following",
        "q": "Match the grooming items with their materials:",
        "items": [{"left": "I. Mirrors", "key": "A"}, {"left": "II. Hair Combs", "key": "B"}, {"left": "III. Lipsticks", "key": "C"}],
        "options": [{"val": "A", "text": "A. Polished cast bronze plate"}, {"val": "B", "text": "B. Carved elephant ivory"}, {"val": "C", "text": "C. Cinnabar mineral powder"}],
        "sol": "Mirrors were bronze, combs were ivory, and lipsticks were cinnabar."
    }
])

s1_mastery_hin.extend([
    {
        "type": "Match the Following",
        "q": "हड़प्पा स्थलों को उनके प्रतिनिधि सामाजिक-आहार साक्ष्यों से सुमेलित करें:",
        "items": [{"left": "I. चन्हुदड़ो", "key": "A"}, {"left": "II. लोथल", "key": "B"}, {"left": "III. हड़प्पा", "key": "C"}],
        "options": [{"val": "A", "text": "A. हिंगुल (cinnabar) आधारित लिपस्टिक और प्रसाधन डिब्बे"}, {"val": "B", "text": "B. चावल के दाने और युगल शवाधान कब्रें"}, {"val": "C", "text": "C. शारीरिक श्रमिकों के लिए बनाई गई बैरकें"}],
        "sol": "चन्हुदड़ो में लिपस्टिक, लोथल में चावल और युगल कब्र, तथा हड़प्पा में मजदूरों की बैरकें मिली हैं।"
    },
    {
        "type": "Match the Following",
        "q": "सामाजिक वर्गों को उनके रहने के क्षेत्रों से सुमेलित करें:",
        "items": [{"left": "I. प्रशासनिक अधिकारी", "key": "A"}, {"left": "II. धनी व्यापारी", "key": "B"}, {"left": "III. सामान्य मजदूर", "key": "C"}],
        "options": [{"val": "A", "text": "A. सुरक्षा प्राचीर से घिरे ऊंचे किले के भवन"}, {"val": "B", "text": "B. निचले नगर में बने बड़े बहु-कक्षीय पक्के मकान"}, {"val": "C", "text": "C. कारखानों के समीप बने दो कमरों के छोटे आवास (बैरक)"}],
        "sol": "अधिकारी किले पर रहते थे, व्यापारी निचले नगर के बड़े घरों में और मजदूर बैरकों में रहते थे।"
    },
    {
        "type": "Match the Following",
        "q": "श्रृंगार सामग्रियों को उनके निर्माण घटकों से सुमेलित करें:",
        "items": [{"left": "I. दर्पण (Mirrors)", "key": "A"}, {"left": "II. कंघियाँ", "key": "B"}, {"left": "III. लिपस्टिक", "key": "C"}],
        "options": [{"val": "A", "text": "A. पॉलिश की गई कांसे की प्लेट"}, {"val": "B", "text": "B. नक्काशीदार हाथीदांत (ivory)"}, {"val": "C", "text": "C. हिंगुल (cinnabar) खनिज का चूर्ण"}],
        "sol": "दर्पण कांसे से, कंघियाँ हाथीदांत से, और लिपस्टिक हिंगुल से बनती थी।"
    }
])

# One-Liner (8)
for q, sol in [
    ("Which site provides direct evidence of lipsticks in the Indus Civilisation?", "Chanhudaro in Sindh."),
    ("What was the primary plant fiber used for clothing?", "Cotton."),
    ("Name the animal whose bones show it was a source of wool.", "Sheep."),
    ("What was the estimated status of women based on terracotta artifacts?", "Highly revered, with many suggesting a matriarchal or matrilineal system."),
    ("Which site shows evidence of rice cultivation in Gujarat?", "Lothal (and Rangpur)."),
    ("What material was used to make the luxury pocket combs found in cities?", "Ivory (elephant tusk)."),
    ("Did Harappans consume beef and mutton?", "Yes, animal remains confirm the consumption of beef, mutton, and fish."),
    ("How did housing indicate social stratification in cities like Harappa?", "By the contrast between large multi-room courtyard houses and small two-room barracks.")
]:
    s1_mastery_eng.append({"type": "One-Liner", "q": q, "sol": sol})

for q, sol in [
    ("सिंधु सभ्यता में लिपस्टिक के प्रत्यक्ष साक्ष्य किस स्थल से मिले हैं?", "सिंध में स्थित चन्हुदड़ो से।"),
    ("वस्त्रों के निर्माण के लिए प्रयुक्त होने वाला मुख्य पादप रेशा कौन सा था?", "कपास (कपास की खेती का साक्ष्य)।"),
    ("किस पशु की हड्डियों से पता चलता है कि वह ऊन का स्रोत था?", "भेड़ (wool source)।"),
    ("मिट्टी की आकृतियों के आधार पर महिलाओं की सामाजिक स्थिति क्या थी?", "अत्यंत सम्मानित, कई इतिहासकार मातृसत्तात्मक समाज का अनुमान लगाते हैं।"),
    ("गुजरात में चावल की खेती का साक्ष्य कहाँ से मिला है?", "लोथल (और रंगपुर) से।"),
    ("अमीर बस्तियों से मिली विलासिता की कंघियाँ किस धातु/सामग्री से बनी थीं?", "हाथीदांत (ivory) से।"),
    ("क्या हड़प्पा वासी मवेशी (beef) और भेड़ (mutton) का मांस खाते थे?", "हाँ, पशुओं की हड्डियों के साक्ष्य मांस और मछली के सेवन की पुष्टि करते हैं।"),
    ("हड़प्पा जैसे शहरों में मकानों का ढांचा सामाजिक विभाजन कैसे दर्शाता है?", "बड़े बहु-कक्षीय आंगनों वाले घरों और छोटे मजदूरों के बैरकों के बीच का अंतर वर्ग भेद दर्शाता है।")
]:
    s1_mastery_hin.append({"type": "One-Liner", "q": q, "sol": sol})

# Assertion-Reason (8)
for q, ans, sol in [
    ("Assertion (A): Harappans are credited as the world's earliest producers of cotton textiles.\nReason (R): Spindle whorls of terracotta and faience have been excavated from domestic quarters.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Harappan society had a rigid, hereditary caste system based on Later Vedic laws.\nReason (R): Archaeological finds show social differentiation in terms of house size and grave goods.", 3, "A is false because there is no evidence of later Vedic caste laws in the IVC. R is true."),
    ("Assertion (A): The status of women in Harappan society was likely highly respected.\nReason (R): A massive number of Mother Goddess clay figurines have been found in residential sites.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Rice was the primary staple crop consumed daily in northern cities like Kalibangan.\nReason (R): Northern sites relied on wheat and barley, while rice was cultivated primarily in Gujarat.", 3, "A is false because wheat/barley were northern staples. R is true."),
    ("Assertion (A): Grooming and cosmetics were highly advanced in Harappan urban centers.\nReason (R): Archaeologists recovered cinnabar lipsticks, ivory combs, and polished bronze mirrors.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Ornaments were worn exclusively by Harappan women to display wealth.\nReason (R): Skeletons of both men and women have been excavated wearing necklaces, armlets, and rings.", 3, "A is false because men also wore jewelry. R is true."),
    ("Assertion (A): Spun wool was used for winter clothing alongside light summer cotton.\nReason (R): Large herds of domesticated sheep were reared in the semiarid zones of Punjab and Sindh.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): The ruling elites lived in the eastern Lower Town for proximity to markets.\nReason (R): The western Citadel mound was built on raised brick platforms and housed public and elite buildings.", 3, "A is false because elites lived on the Citadel, not the Lower Town. R is true.")
]:
    s1_mastery_eng.append({"type": "Assertion-Reason", "q": q, "opts": ar_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("कथन (A): हड़प्पा वासियों को विश्व में सूती वस्त्रों के सबसे प्राचीन उत्पादकों के रूप में श्रेय दिया जाता है।\nकारण (R): घरों के उत्खनन में मिट्टी और फेयॉन्स से बने कताई चक्र (spindle whorls) प्रचुर मात्रा में मिले हैं।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): हड़प्पा समाज में उत्तर वैदिक कालीन व्यवस्था की तरह एक जन्म-आधारित कठोर जाति व्यवस्था थी।\nकारण (R): उत्खनन में मकानों के आकार और कब्रों के सामान में स्पष्ट सामाजिक अंतर दिखाई देता है।", 3, "A असत्य है क्योंकि उत्तर वैदिक कालीन व्यवस्था का साक्ष्य यहाँ नहीं है। R सत्य है।"),
    ("कथन (A): हड़प्पा समाज में महिलाओं की स्थिति अत्यंत सम्मानित और प्रभावशाली रही होगी।\nकारण (R): आवासीय क्षेत्रों से भारी संख्या में पकी मिट्टी की मातृदेवी की मूर्तियां प्राप्त हुई हैं।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): कालीबंगन जैसे उत्तरी शहरों में चावल दैनिक भोजन की मुख्य फसल थी।\nकारण (R): उत्तरी क्षेत्रों में मुख्य भोजन गेहूं और जौ था, जबकि चावल की खेती गुजरात के तटीय क्षेत्रों में होती थी।", 3, "A असत्य है क्योंकि उत्तर का मुख्य भोजन गेहूं/जौ था। R सत्य है।"),
    ("कथन (A): हड़प्पा के शहरी केंद्रों में सौंदर्य प्रसाधन और व्यक्तिगत श्रृंगार अत्यंत विकसित अवस्था में थे।\nकारण (R): उत्खनन में हिंगुल की लिपस्टिक, हाथीदांत की कंघियाँ और कांसे के चमकदार दर्पण प्राप्त हुए हैं।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): हड़प्पा समाज में संपत्ति के प्रदर्शन के लिए आभूषण केवल महिलाओं द्वारा ही पहने जाते थे।\nकारण (R): उत्खनन में स्त्री और पुरुष दोनों के कंकालों के साथ हार, बाजूबंद और अंगूठियां दबी हुई मिली हैं।", 3, "A असत्य है क्योंकि आभूषण दोनों पहनते थे। R सत्य है।"),
    ("कथन (A): गर्मियों के कपास के साथ-साथ सर्दियों में ऊनी धागों का उपयोग भी किया जाता था।\nकारण (R): पंजाब और सिंध के अर्ध-शुष्क क्षेत्रों में भेड़-बकरियों को बड़े पैमाने पर पाला जाता था।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): प्रशासनिक शासक वर्ग बाजार के समीप रहने के लिए पूर्वी निचले नगर में रहता था।\nकारण (R): पश्चिमी किला चबूतरे पर ऊँचा बनाया गया था और उसमें प्रशासनिक तथा सार्वजनिक भवन स्थित थे।", 3, "A असत्य है क्योंकि शासक वर्ग किले पर रहता था, निचले नगर में नहीं। R सत्य है।")
]:
    s1_mastery_hin.append({"type": "Assertion-Reason", "q": q, "opts": hin_ar_opts, "ans": ans, "sol": sol})

# Statement-Based (5)
for q, ans, sol in [
    ("Consider the following statements regarding Harappan cotton:\n1. The Indus region is recognized as the earliest home of cotton cultivation in the Old World.\n2. In Mesopotamia, cotton textiles were called 'Sindon', originating from the word 'Sindh'.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct and verify the early history of cotton and its trade name Sindon."),
    ("Consider the following statements regarding social hierarchy:\n1. The ruling elites held monopoly over steatite seal carvings and brick kilns.\n2. The barracks at Harappa suggest that manual laborers lived in standardized housing.\nWhich of the statements given above is/are correct?", 1, "Statement 2 is correct. Statement 1 is incorrect: seals and bricks were made by professional artisan guilds, not as an elite monopoly."),
    ("Consider the following statements regarding cosmetic artifacts:\n1. Small pots of ivory were used to store collyrium eyeliner.\n2. Bronze mirrors featured highly reflective glass lenses imported from Mesopotamia.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: Bronze Age mirrors were made of polished metal plates, not reflective glass."),
    ("Consider the following statements regarding the status of women:\n1. The prevalence of female terracotta figurines suggests matrilineal social indicators.\n2. Women were buried with less pottery, proving they had lower status in death.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: female graves contain equal quantities of pottery and ornaments as male graves."),
    ("Consider the following statements regarding diet:\n1. Animal remains include bones of sheep, goats, humped bulls, and pigs.\n2. Wheat was the only cereal crop cultivated in northern India.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: barley and sesame were also cultivated in the north.")
]:
    s1_mastery_eng.append({"type": "Statement-Based", "q": q, "opts": mcq_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("हड़प्पा के कपास के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. सिंधु क्षेत्र को पुरानी दुनिया में कपास की खेती के सबसे प्राचीन घर के रूप में मान्यता प्राप्त है।\n2. मेसोपोटामिया में सूती कपड़ों को 'सिन्डोन' (Sindon) कहा जाता था, जो 'सिंध' शब्द से उत्पन्न हुआ था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 2, "दोनों कथन सही हैं, जो कपास के प्राचीनतम साक्ष्य और मेसोपोटामियाई नाम 'सिन्डोन' को स्पष्ट करते हैं।"),
    ("सामाजिक स्तरीकरण के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. शासक वर्ग के पास सेलखड़ी की मुहरों और ईंट के भट्टों पर पूर्ण एकाधिकार था।\n2. हड़प्पा की बैरकें दर्शाती हैं कि शारीरिक श्रम करने वाले मजदूर एक समान सरकारी आवासों में रहते थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 1, "कथन 2 सही है। कथन 1 गलत है क्योंकि मुहरें और ईंटें पेशेवर कारीगरों द्वारा बनाई जाती थीं, कोई राजकीय एकाधिकार प्रमाणित नहीं है।"),
    ("श्रृंगार सामग्री के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. हाथीदांत की छोटी डिब्बियों का उपयोग आँखों का काजल रखने के लिए किया जाता था।\n2. कांसे के दर्पणों में मेसोपोटामिया से आयातित कांच के शीशे लगे होते थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि दर्पण पॉलिश किए धातु के होते थे, कांच का आविष्कार तब नहीं हुआ था।"),
    ("महिलाओं की स्थिति के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मिट्टी की स्त्री मूर्तियों की बहुलता मातृवंशीय सामाजिक संकेतकों की ओर इशारा करती है।\n2. महिलाओं को कम बर्तनों के साथ दफनाया जाता था, जो मृत्यु में उनकी निम्न स्थिति दर्शाता है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि महिला कब्रों में पुरुषों के बराबर ही आभूषण और बर्तन मिले हैं।"),
    ("खान-पान के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. पशु अवशेषों में भेड़, बकरी, कूबड़ वाले सांड और सूअरों की हड्डियां मिली हैं।\n2. उत्तरी भारत में उगाई जाने वाली एकमात्र खाद्य फसल गेहूं थी।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि जौ और तिल भी उत्तर में उगाए जाते थे।")
]:
    s1_mastery_hin.append({"type": "Statement-Based", "q": q, "opts": hin_mcq_opts, "ans": ans, "sol": sol})

# Why (3)
for q, sol in [
    ("Why did the Mesopotamians refer to cotton textiles as 'Sindon'?", "Because the textiles originated from the 'Sindh' (Indus River) valley, where cotton cultivation was pioneered."),
    ("Why do historians suggest that Harappan society may have been matriarchal?", "Due to the overwhelming discovery of female clay figurines, Mother Goddess cult icons, and the absence of militaristic male-king representations."),
    ("Why was jewelry buried with the dead in Harappan cemeteries?", "It reflected their belief in an afterlife, where the deceased would require personal items, grooming tools, and ornaments in their next journey.")
]:
    s1_mastery_eng.append({"type": "Why", "q": q, "sol": sol})

for q, sol in [
    ("मेसोपोटामिया के लोग सूती वस्त्रों को 'सिन्डोन' (Sindon) क्यों कहते थे?", "क्योंकि ये वस्त्र 'सिंध' (सिंधु घाटी) क्षेत्र से आते थे, जहाँ कपास की खेती की शुरुआत हुई थी।"),
    ("इतिहासकार ऐसा क्यों मानते हैं कि हड़प्पा समाज मातृसत्तात्मक रहा होगा?", "मिट्टी की स्त्री मूर्तियों की भारी संख्या, मातृदेवी पूजा के प्रतीकों और किसी भी सैन्यवादी पुरुष-सम्राट के साक्ष्यों के अभाव के कारण।"),
    ("हड़प्पा के कब्रिस्तानों में शवों के साथ गहने और बर्तन क्यों दफनाए जाते थे?", "यह पारलौकिक जीवन (afterlife) में उनके विश्वास को दर्शाता है, जहाँ माना जाता था कि मृतक को अगली यात्रा में इन वस्तुओं की आवश्यकता होगी।")
]:
    s1_mastery_hin.append({"type": "Why", "q": q, "sol": sol})

# How (3)
for q, sol in [
    ("How did social divisions manifest in the architecture of Harappan towns?", "Through housing hierarchy: administrative elites lived in fortified, elevated Citadels; merchants lived in large Lower Town houses; and laborers lived in tiny, two-room quarters near factories."),
    ("How were cosmetics stored and utilized by Harappan women?", "Collyrium and facial powders were stored in small glazed terracotta or ivory pots and applied using small copper sticks, while lipsticks were prepared from mineral cinnabar blocks."),
    ("How did Harappan diets differ between the northern dry zones and southern coastal zones?", "Northern zones relied heavily on wheat and barley alongside mutton and beef, while southern zones in Gujarat incorporated millets, rice, and a high proportion of marine fish and shells.")
]:
    s1_mastery_eng.append({"type": "How", "q": q, "sol": sol})

for q, sol in [
    ("हड़प्पा शहरों की वास्तुकला में सामाजिक विभाजन किस प्रकार दिखाई देता था?", "आवासों के स्तरीकरण से: शासक वर्ग किले के ऊंचे प्राचीरयुक्त भवनों में रहते थे, धनी व्यापारी निचले नगर के बड़े घरों में, और श्रमिक कारखानों के समीप बैरकों में रहते थे।"),
    ("हड़प्पा की महिलाओं द्वारा सौंदर्य प्रसाधनों का भंडारण और उपयोग कैसे किया जाता था?", "काजल और उबटन को हाथीदांत या मिट्टी की छोटी चमकीली डिब्बियों में रखकर तांबे की शलाकाओं से लगाया जाता था, और लिपस्टिक हिंगुल खनिज से बनाई जाती थी।"),
    ("उत्तरी शुष्क क्षेत्रों और दक्षिणी तटीय क्षेत्रों में हड़प्पा वासियों के भोजन में क्या अंतर था?", "उत्तरी क्षेत्रों के लोग गेहूं, जौ, भेड़ और सूअर के मांस पर निर्भर थे, जबकि गुजरात के तटीय क्षेत्रों के लोग बाजरा, चावल और समुद्री मछलियों व केकड़ों का अधिक सेवन करते थे।")
]:
    s1_mastery_hin.append({"type": "How", "q": q, "sol": sol})

# Case Study (3)
for q, sol in [
    ("Case Study: Chanhudaro Cosmetic Workshops", "Excavations at Chanhudaro yielded cosmetic boxes, copper eyeliner rods, and small cakes of cinnabar (lipstick). This indicates that cosmetic manufacturing was a specialized craft sector, and grooming held high value in Harappan urban culture."),
    ("Case Study: Class Zoning at Harappa", "Harappa's Mound E displays clear socio-economic segregation. Near the circular threshing platforms sat rows of identical two-room barracks for laborers, contrasting with the spacious merchant houses in the center of the Lower Town, proving institutionalized class divisions."),
    ("Case Study: Grave Wealth and Stratification", "Archaeological study of Cemetery R-37 graves reveals that while most individuals were buried with simple pottery, a few graves were brick-lined and contained jade beads, gold rings, and bronze mirrors, demonstrating wealth inequality in death.")
]:
    s1_mastery_eng.append({"type": "Case Study", "q": q, "sol": sol})

for q, sol in [
    ("केस स्टडी: चन्हुदड़ो की सौंदर्य प्रसाधन कार्यशालाएँ", "चन्हुदड़ो में प्रसाधन बक्से, आँखों में काजल लगाने वाली तांबे की सलाइयाँ और हिंगुल (लिपस्टिक) के टुकड़े मिले हैं। यह सिद्ध करता है कि प्रसाधन सामग्री का निर्माण एक व्यावसायिक शिल्प था और शहरी संस्कृति में श्रृंगार का महत्व था।"),
    ("केस स्टडी: हड़प्पा में सामाजिक क्षेत्रों का विभाजन", "हड़प्पा के टीले E पर सामाजिक-आर्थिक अलगाव स्पष्ट है। अनाज कूटने के गोलाकार चबूतरों के पास मजदूरों के लिए दो-कमरे वाले एक समान बैरक बने थे, जो निचले नगर के बीच बने बड़े घरों से काफी अलग थे, जो वर्ग भेद को दर्शाते हैं।"),
    ("केस स्टडी: कब्रों की सामग्री और सामाजिक विभाजन", "कब्रिस्तान R-37 की कब्रों के अध्ययन से पता चलता है कि जहाँ अधिकांश सामान्य लोगों को मिट्टी के साधारण बर्तनों के साथ दफनाया गया था, वहीं कुछ विशेष कब्रें ईंटों से पक्की की गई थीं जिनमें सोने की अंगूठियां, जेड के मनके और कांसे के दर्पण रखे थे।")
]:
    s1_mastery_hin.append({"type": "Case Study", "q": q, "sol": sol})

# Teach Concept (3)
for q, sol in [
    ("Teach Concept: Matriarchal Social Indicators", "Explain how historians use archaeological weight of evidence. By showing the high ratio of female-to-male clay figures (Mother Goddesses), representations of pregnant deities, and the absolute lack of glorifying military male kings, scholars infer a matrilineal focus."),
    ("Teach Concept: Textual Traces of Harappan Cotton", "Describe the trade link. Harappans cultivated cotton first. Mesopotamian clay tablets refer to imports of 'Sindon' or 'Sinnu' from the Indus (Meluhha). Explain how cotton became an international trade commodity that defined early Indian exports."),
    ("Teach Concept: Material Analysis of Social Class", "Explain how historians deduce class structures without texts. They study the architecture ( Citadel vs. Lower Town), housing size, raw material access (rich quarters have lapis and gold, poor have clay), and burial wealth to map out class stratification.")
]:
    s1_mastery_eng.append({"type": "Teach Concept", "q": q, "sol": sol})

for q, sol in [
    ("अवधारणा समझाएं (Teach Concept): मातृसत्तात्मक समाज के पुरातात्विक संकेतक", "समझाएं कि इतिहासकार पुरातात्विक साक्ष्यों का विश्लेषण कैसे करते हैं। पुरुषों की तुलना में मिट्टी की नारी आकृतियों (मातृदेवियों) की अत्यधिक संख्या, गर्भवती देवियों के चित्रण और किसी भी पुरुष योद्धा-सम्राट के महिमामंडन के अभाव से वे मातृसत्तात्मक व्यवस्था का निष्कर्ष निकालते हैं।"),
    ("अवधारणा समझाएं (Teach Concept): हड़प्पा के सूती वस्त्रों के व्यापारिक प्रमाण", "व्यापारिक संबंधों को स्पष्ट करें। हड़प्पा वासियों ने सबसे पहले कपास उगाया। मेसोपोटामिया की मिट्टी की पट्टियों पर सिंधु (मेलुहा) से आने वाले सूती कपड़ों को 'सिन्डोन' या 'सिन्नू' कहा गया है। समझाएं कि यह वस्त्र शुरुआती भारतीय अंतरराष्ट्रीय निर्यात का आधार बना।"),
    ("अवधारणा समझाएं (Teach Concept): भौतिक साक्ष्यों से सामाजिक वर्ग का विश्लेषण", "बिना लिखित साक्ष्यों के वर्ग विभाजन को समझने की विधि बताएं। इतिहासकार आवासीय वास्तुकला (किला बनाम निचला नगर), मकानों के आकार, कच्चे माल तक पहुंच (अमीरों के यहाँ लाजवर्त और सोना, गरीबों के यहाँ मिट्टी) और कब्रों की संपत्ति का अध्ययन कर वर्ग विभाजन का खाका खींचते हैं।")
]:
    s1_mastery_hin.append({"type": "Teach Concept", "q": q, "sol": sol})


# =========================================================================
# SECTION 2: RELIGIOUS BELIEFS, BURIAL CUSTOMS & SCRIPT
# =========================================================================
s2_mastery_eng = []
s2_mastery_hin = []

# MCQ (5)
for q, opts, ans, sol in [
    ("Which tree species is most frequently represented on Harappan seals, often associated with emerging deities?", ["Pipal (Ficus religiosa)", "Banyan (Ficus benghalensis)", "Mango (Mangifera indica)", "Neem (Azadirachta indica)"], 0, "The pipal tree is the most dominant botanical motif, depicted as sacred and associated with deities."),
    ("At which Harappan site were male and female skeletons discovered buried together in a single grave?", ["Lothal", "Harappa", "Mohenjo-daro", "Kalibangan"], 0, "Lothal in Gujarat is famous for its three double burial graves, suggesting joint burials."),
    ("The writing direction of the undeciphered Harappan script, alternating right-to-left and left-to-right, is called:", ["Boustrophedon", "Cuneiform", "Hieroglyphic", "Kharosthi"], 0, "Boustrophedon is the style where writing alternates directions in consecutive lines."),
    ("The famous Pashupati seal depicts a deity seated in a yogic posture surrounded by which four animals?", ["Elephant, Tiger, Rhinoceros, Buffalo", "Lion, Horse, Bull, Leopard", "Elephant, Lion, Horse, Deer", "Tiger, Leopard, Zebu, Rhino"], 0, "The Pashupati figure is surrounded by an elephant, a tiger, a rhinoceros, and a buffalo, with two deer at the feet."),
    ("Where was the famous signboard inscription containing ten large pictographic signs discovered?", ["Dholavira", "Rakhigarhi", "Lothal", "Surkotada"], 0, "The Dholavira signboard, containing 10 large white gypsum characters, was found near a Citadel gate.")
]:
    s2_mastery_eng.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("हड़प्पा की मुहरों पर किस पेड़ का सबसे अधिक बार चित्रण मिला है, जो अक्सर देवताओं से जुड़ा रहता था?", ["पीपल (Ficus religiosa)", "बरगद (Banyan)", "आम (Mango)", "नीम (Neem)"], 0, "पीपल का पेड़ सबसे प्रमुख वनस्पति प्रतीक है जिसे मुहरों पर देवताओं के निवास के रूप में पवित्र दिखाया गया है।"),
    ("किस हड़प्पा स्थल पर पुरुष और महिला के कंकालों को एक ही कब्र में एक साथ दफनाया गया पाया गया है?", ["लोथल", "हड़प्पा", "मोहनजोदड़ो", "कालीबंगन"], 0, "गुजरात के लोथल से तीन युगल शवाधान (double burials) के साक्ष्य मिले हैं जहाँ एक ही कब्र में दो कंकाल मिले हैं।"),
    ("हड़प्पा की अपठित लिपि की लेखन दिशा, जिसमें पहली पंक्ति दाएं से बाएं और दूसरी बाएं से दाएं लिखी जाती थी, कहलाती है:", ["बोउस्ट्रोफेडन (Boustrophedon)", "कीलकाक्षर (Cuneiform)", "चित्रलिपि (Hieroglyphic)", "खरोष्ठी (Kharosthi)"], 0, "बोउस्ट्रोफेडन वह शैली है जिसमें लेखन की दिशा क्रमिक पंक्तियों में बारी-बारी से बदलती थी।"),
    ("प्रसिद्ध पशुपति मुहर में एक योगासन में बैठे देव को किन चार जंगली पशुओं से घिरा दिखाया गया है?", ["हाथी, बाघ, गैंडा, भैंसा", "शेर, घोड़ा, बैल, तेंदुआ", "हाथी, शेर, घोड़ा, हिरण", "बाघ, तेंदुआ, कूबड़ वाला बैल, गैंडा"], 0, "पशुपति शिव की आकृति के चारों ओर हाथी, बाघ, गैंडा और भैंसा बने हैं, और नीचे चरणों में दो हिरण हैं।"),
    ("दस बड़े चित्रलेखीय चिन्हों वाला प्रसिद्ध सूचना-पट्ट (Signboard) कहाँ से प्राप्त हुआ है?", ["धोलावीरा", "राखीगढ़ी", "लोथल", "सुरकोटदा"], 0, "धोलावीरा के किले के द्वार के पास से सफेद जिप्सम से बने 10 बड़े अक्षरों वाला सूचना-पट्ट मिला है।")
]:
    s2_mastery_hin.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# Multi-Correct MCQ (5)
for q, opts, ans, sol in [
    ("Which animals are depicted surrounding the central deity on the Pashupati seal? (Select all that apply)", ["Elephant", "Tiger", "Rhinoceros", "Lion"], [0, 1, 2], "Elephant, tiger, rhinoceros, and buffalo surround the deity. Lions are not depicted on seals."),
    ("Select the burial methods practiced by the Harappan people: (Select all that apply)", ["Complete inhumation (body head north)", "Fractional burials (post-exposure bones)", "Urn burials after cremation", "Mummification using resin-soaked linens"], [0, 1, 2], "Inhumation, fractional, and urn burials were practiced. Mummification was Egyptian, not Harappan."),
    ("What are the characteristics of the Harappan writing script? (Select all that apply)", ["Written in Boustrophedon style", "Pictographic and logo-syllabic", "Deciphered successfully by modern linguists", "Contains approximately 375 to 400 signs"], [0, 1, 3], "The script is Boustrophedon, pictographic, and has 375-400 signs. It remains undeciphered."),
    ("Identify the sites where evidence of ritual fire altars has been excavated: (Select all that apply)", ["Kalibangan", "Lothal", "Mohenjo-daro", "Banawali"], [0, 1], "Fire altars are found at Kalibangan and Lothal. None exist at Mohenjo-daro or Banawali."),
    ("Which deities or objects were worshiped by the Harappans? (Select all that apply)", ["Mother Goddess (Earth deity)", "Pashupati (Proto-Shiva)", "Phallic stones and yoni symbols", "Bronze idols of Vedic solar deities"], [0, 1, 2], "Mother Goddess, Pashupati, and phallic/yoni stones were worshiped. Vedic bronze sun idols did not exist yet.")
]:
    s2_mastery_eng.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("पशुपति मुहर पर केंद्रीय देव को घेरने वाले जंगली जानवरों का चयन करें: (सभी लागू विकल्प चुनें)", ["हाथी", "बाघ", "गैंडा", "शेर"], [0, 1, 2], "हाथी, बाघ, गैंडा और भैंसा घिरे हुए हैं। शेर मुहरों पर चित्रित नहीं हैं।"),
    ("हड़प्पा वासियों द्वारा अपनाई जाने वाली शवाधान विधियों का चयन करें: (सभी लागू विकल्प चुनें)", ["पूर्ण शवाधान (उत्तर की ओर सिर करके दफनाना)", "आंशिक शवाधान (हड्डियों का संचयन)", "दाह संस्कार के बाद अस्थि कलश दफनाना", "राल लगे कपड़ों में लपेटकर ममी बनाना"], [0, 1, 2], "पूर्ण, आंशिक और कलश शवाधान प्रचलित थे। ममी बनाने का काम मिस्र में होता था, यहाँ नहीं।"),
    ("हड़प्पा लेखन लिपि की क्या विशेषताएं हैं? (सभी लागू विकल्प चुनें)", ["बोउस्ट्रोफेडन शैली में लिखी जाना", "चित्रात्मक और लोगो-सिलेबिक होना", "आधुनिक भाषाविदों द्वारा सफलतापूर्वक पढ़ा जाना", "लगभग 375 से 400 चिन्हों का होना"], [0, 1, 3], "लिपि बोउस्ट्रोफेडन, चित्रात्मक और 375-400 चिन्हों वाली थी। यह अभी तक अपठित है।"),
    ("उन स्थलों की पहचान करें जहाँ से अनुष्ठानिक अग्निकुंडों के साक्ष्य मिले हैं: (सभी लागू विकल्प चुनें)", ["कालीबंगन", "लोथल", "मोहनजोदड़ो", "बनावली"], [0, 1], "अग्निकुंड कालीबंगन और लोथल में मिले हैं। मोहनजोदड़ो या बनावली में ये नहीं मिले।"),
    ("हड़प्पा वासी किन देवताओं या प्रतीकों की पूजा करते थे? (सभी लागू विकल्प चुनें)", ["मातृदेवी (उर्वरता की देवी)", "पशुपति (आद्य-शिव)", "लिंग और योनि के पाषाण प्रतीक", "वैदिक सौर देवताओं की कांस्य मूर्तियां"], [0, 1, 2], "मातृदेवी, पशुपति और लिंग-योनि प्रतीकों की पूजा होती थी। वैदिक कांस्य मूर्तियां बहुत बाद की हैं।")
]:
    s2_mastery_hin.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# True/False (8)
for q, ans, sol in [
    ("The Harappan script has been successfully translated by linguists.", False, "False. Despite many claims, the Harappan script remains undeciphered."),
    ("The standard head direction in Harappan burials was North.", True, "True. Skeletons were typically aligned North-South with the head to the north."),
    ("Fire altars indicate that animal sacrifices were performed at Mohenjo-daro.", False, "False. Fire altars were absent at Mohenjo-daro; they are found only at Kalibangan and Lothal."),
    ("Boustrophedon is a writing style where lines alternate directions.", True, "True. Scribes wrote from right-to-left, then left-to-right in the next line."),
    ("The Pashupati seal depicts a lion seated at the feet of the deity.", False, "False. The animal at the feet is a deer (two deer are depicted)."),
    ("Lothal has yielded graves containing double burials of male and female skeletons.", True, "True. Three double graves were found at Lothal."),
    ("Cemetery R-37 is a major burial site located at Mohenjo-daro.", False, "False. Cemetery R-37 is located at Harappa."),
    ("The pipal tree was worshiped as a sacred botanical deity.", True, "True. Depictions on seals show pipal trees as holy and linked to deities.")
]:
    s2_mastery_eng.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("हड़प्पा की लिपि को भाषाविदों द्वारा सफलतापूर्वक पढ़ा जा चुका है।", False, "असत्य। कई दावों के बावजूद हड़प्पा लिपि आज भी अपठित है।"),
    ("हड़प्पा शवाधान में शव के सिर की मानक दिशा उत्तर की ओर होती थी।", True, "सत्य। कब्रों में शवों को उत्तर-दक्षिण दिशा में लिटाया जाता था और सिर उत्तर में होता था।"),
    ("अग्निकुंडों से पता चलता है कि मोहनजोदड़ो में पशु बलि दी जाती थी।", False, "असत्य। मोहनजोदड़ो में अग्निकुंड नहीं मिले हैं; वे केवल कालीबंगन और लोथल में मिले हैं।"),
    ("बोउस्ट्रोफेडन लेखन की वह शैली है जहाँ पंक्तियों की दिशा वैकल्पिक रूप से बदलती है।", True, "सत्य। इसमें पहली पंक्ति दाएं से बाएं और अगली पंक्ति बाएं से दाएं लिखी जाती थी।"),
    ("पशुपति मुहर पर देव के चरणों में एक शेर बैठा दर्शाया गया है।", False, "असत्य। चरणों में दो हिरण बने हैं, शेर मुहरों पर नहीं मिलता।"),
    ("लोथल से पुरुष और महिला के कंकालों वाली युगल कब्रें मिली हैं।", True, "सत्य। लोथल से तीन ऐसी युगल कब्रें खोजी गई हैं।"),
    ("कब्रिस्तान R-37 मोहनजोदड़ो में स्थित एक प्रमुख शवाधान स्थल है।", False, "असत्य। कब्रिस्तान R-37 हड़प्पा में स्थित है।"),
    ("पीपल के पेड़ की पूजा एक पवित्र वनस्पति देवता के रूप में की जाती थी।", True, "सत्य। मुहरों पर पीपल को देवताओं के निवास के रूप में दर्शाया गया है।")
]:
    s2_mastery_hin.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

# Fill Blank (8)
for q, ans, sol in [
    ("The writing direction that alternates from right-to-left and left-to-right is __________.", "Boustrophedon", "Boustrophedon writing alternates directions like plowing fields."),
    ("The most frequently represented sacred tree on seals is the __________.", "pipal", "The pipal tree is the primary sacred plant representation."),
    ("Male and female double burials in a single grave were excavated at __________.", "Lothal", "Lothal has yielded three double burials."),
    ("The primary burial ground excavated at Harappa is designated as Cemetery __________.", "R-37", "Cemetery R-37 is the mature Harappan cemetery at Harappa."),
    ("The Pashupati seal deity wears a crown made of __________ horns.", "bull", "The deity wears a three-horned bull head-dress."),
    ("Fire altars built on brick platforms are found at Lothal and __________.", "Kalibangan", "Kalibangan in Rajasthan is famous for its line of fire altars."),
    ("The Dholavira signboard features __________ large symbols made of gypsum.", "ten", "Ten large signs were recovered at Dholavira."),
    ("Stone rings representing female fertility are interpreted as __________ symbols.", "yoni", "Yoni stones represent female fertility worship.")
]:
    s2_mastery_eng.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("दाएं से बाएं और फिर बाएं से दाएं लिखने की वैकल्पिक शैली को __________ कहते हैं।", "बोउस्ट्रोफेडन", "बारी-बारी से दिशा बदलने की लेखन शैली बोउस्ट्रोफेडन कहलाती है।"),
    ("मुहरों पर चित्रित सबसे प्रमुख पवित्र वृक्ष __________ है।", "पीपल", "पीपल का पेड़ धार्मिक महत्व का मुख्य वनस्पति प्रतीक था।"),
    ("एक ही कब्र में पुरुष और महिला के युगल शवाधान के अवशेष __________ से मिले हैं।", "लोथल", "लोथल से तीन युगल कब्रों के अवशेष मिले हैं।"),
    ("हड़प्पा में खोजे गए मुख्य परिपक्व कब्रिस्तान को कब्रिस्तान __________ नाम दिया गया है।", "R-37", "कब्रिस्तान R-37 हड़प्पा का मुख्य शवाधान स्थल है।"),
    ("पशुपति मुहर के देव ने माथे पर __________ के सींगों वाला मुकुट पहना है।", "सांड", "देव ने कूबड़ वाले सांड/बैल के सींगों वाला मुकुट पहना हुआ है।"),
    ("लोथल के अतिरिक्त चबूतरों पर बने अग्निकुंड __________ नामक स्थल से मिले हैं।", "कालीबंगन", "राजस्थान के कालीबंगन से अग्निकुंडों की कतारें मिली हैं।"),
    ("धोलावीरा के सूचना-पट्ट पर जिप्सम से बने __________ बड़े अक्षर मिले हैं।", "दस", "धोलावीरा सूचना-पट्ट पर 10 बड़े चिन्ह अंकित थे।"),
    ("नारी की उर्वरता और जनन शक्ति के रूप में पूजे जाने वाले पत्थर के छल्लों को __________ कहते हैं।", "योनि", "पत्थर के छल्लों को योनि (yoni) प्रतीक माना गया है।")
]:
    s2_mastery_hin.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

# Match the Following (3)
s2_mastery_eng.extend([
    {
        "type": "Match the Following",
        "q": "Match the burial landmarks with their respective sites:",
        "items": [{"left": "I. Cemetery R-37 (Head North)", "key": "A"}, {"left": "II. Three Double Burial Graves", "key": "B"}, {"left": "III. Late Urn Cremations (Peacock drawings)", "key": "C"}],
        "options": [{"val": "A", "text": "A. Harappa (Mature Phase)"}, {"val": "B", "text": "B. Lothal (Gujarat)"}, {"val": "C", "text": "C. Cemetery H (Late Harappa)"}],
        "sol": "Cemetery R-37 is Harappa, double burials Lothal, and Cemetery H is Late Harappa."
    },
    {
        "type": "Match the Following",
        "q": "Match the religious symbols with their modern academic interpretations:",
        "items": [{"left": "I. Pashupati Seal", "key": "A"}, {"left": "II. Large Mud Platforms with Altars", "key": "B"}, {"left": "III. Stone Rings and Cylinders", "key": "C"}],
        "options": [{"val": "A", "text": "A. Proto-Shiva yoga deity"}, {"val": "B", "text": "B. Public fire sacrifice rituals"}, {"val": "C", "text": "C. Linga and Yoni fertility worship"}],
        "sol": "Pashupati is Proto-Shiva, mud platforms are fire sacrifices, and rings are linga/yoni fertility worship."
    },
    {
        "type": "Match the Following",
        "q": "Match the script artifacts with their descriptions:",
        "items": [{"left": "I. Dholavira Signboard", "key": "A"}, {"left": "II. Standard Steatite Seals", "key": "B"}, {"left": "III. Copper Tablets", "key": "C"}],
        "options": [{"val": "A", "text": "A. 10 large gypsum symbols once mounted on wood"}, {"val": "B", "text": "B. 2-5 character short names with animal reliefs"}, {"val": "C", "text": "C. Minor script tablets with repeating signs"}],
        "sol": "Dholavira signboard has 10 large symbols, seals have short name/animal reliefs, and copper tablets have repeating signs."
    }
])

s2_mastery_hin.extend([
    {
        "type": "Match the Following",
        "q": "शवाधान स्थलों को उनके विशिष्ट सांस्कृतिक साक्ष्यों से सुमेलित करें:",
        "items": [{"left": "I. कब्रिस्तान R-37 (सिर उत्तर)", "key": "A"}, {"left": "II. तीन युगल कब्रें (Double graves)", "key": "B"}, {"left": "III. कलश शवाधान (मोर के चित्र)", "key": "C"}],
        "options": [{"val": "A", "text": "A. हड़प्पा (परिपक्व चरण)"}, {"val": "B", "text": "B. लोथल (गुजरात)"}, {"val": "C", "text": "C. कब्रिस्तान H (उत्तर हड़प्पा चरण)"}],
        "sol": "कब्रिस्तान R-37 हड़प्पा में है, युगल कब्र लोथल में, और कब्रिस्तान H उत्तर हड़प्पा का है।"
    },
    {
        "type": "Match the Following",
        "q": "धार्मिक प्रतीकों को उनकी आधुनिक व्याख्याओं से सुमेलित करें:",
        "items": [{"left": "I. पशुपति मुहर", "key": "A"}, {"left": "II. चबूतरों पर बने अग्निकुंड", "key": "B"}, {"left": "III. पत्थर के छल्ले और बेलन", "key": "C"}],
        "options": [{"val": "A", "text": "A. आद्य-शिव योगासन देवता"}, {"val": "B", "text": "B. सार्वजनिक यज्ञीय अनुष्ठान"}, {"val": "C", "text": "C. लिंग और योनि उर्वरता पूजा"}],
        "sol": "पशुपति आद्य-शिव हैं, अग्निकुंड यज्ञ अनुष्ठान हैं, और पत्थर लिंग-योनि उर्वरता पूजा के प्रतीक हैं।"
    },
    {
        "type": "Match the Following",
        "q": "लिपि के अवशेषों को उनके भौतिक विवरणों से सुमेलित करें:",
        "items": [{"left": "I. धोलावीरा सूचना-पट्ट", "key": "A"}, {"left": "II. मानक सेलखड़ी मुहरें", "key": "B"}, {"left": "III. तांबे की पट्टियाँ (tablets)", "key": "C"}],
        "options": [{"val": "A", "text": "A. जिप्सम से बने 10 बड़े अक्षर जो कभी लकड़ी पर मढ़े थे"}, {"val": "B", "text": "B. पशु चित्र के साथ 2-5 अक्षरों के संक्षिप्त लेख"}, {"val": "C", "text": "C. दोहराव वाले चिन्हों से युक्त लघु धातु फलक"}],
        "sol": "धोलावीरा सूचना-पट्ट में 10 जिप्सम अक्षर हैं, मुहरों पर पशु और संक्षिप्त लेख हैं, और तांबे की पट्टियों पर दोहराव चिन्ह हैं।"
    }
])

# One-Liner (8)
for q, sol in [
    ("What is the writing style of the Harappan script?", "Boustrophedon (alternating from right-to-left and left-to-right)."),
    ("Which tree was considered highly sacred and carved on seals?", "The pipal tree."),
    ("Where was the unique double burial of male and female excavated?", "Lothal in Gujarat."),
    ("Name the major cemetery excavated at mature Harappa.", "Cemetery R-37."),
    ("What four animals surround the deity on the Pashupati seal?", "Tiger, Elephant, Rhinoceros, and Buffalo."),
    ("Which sites feature brick fire altars showing fire worship?", "Kalibangan and Lothal."),
    ("How many signs are estimated to exist in the logo-syllabic script?", "Between 375 and 400 signs."),
    ("What material was used to make the letters of the Dholavira signboard?", "White crystalline gypsum paste.")
]:
    s2_mastery_eng.append({"type": "One-Liner", "q": q, "sol": sol})

for q, sol in [
    ("हड़प्पा लिपि की लेखन शैली क्या कहलाती है?", "बोउस्ट्रोफेडन (बारी-बारी से दिशा बदलना)।"),
    ("किस वृक्ष को अत्यंत पवित्र मानकर मुहरों पर चित्रित किया जाता था?", "पीपल का पेड़।"),
    ("पुरुष और महिला की युगल कब्र का साक्ष्य कहाँ से मिला है?", "गुजरात के लोथल से।"),
    ("हड़प्पा में परिपक्व चरण का मुख्य कब्रिस्तान कौन सा खोजा गया है?", "कलिब्रस्तान R-37।"),
    ("पशुपति मुहर पर देव को घेरने वाले चार पशु कौन से हैं?", "बाघ, हाथी, गैंडा और भैंसा।"),
    ("यज्ञ और अग्नि पूजा दर्शाने वाले अग्निकुंड किन स्थलों से मिले हैं?", "कालीबंगन और लोथल से।"),
    ("हड़प्पा की इस चित्रात्मक लिपि में कुल कितने चिन्ह होने का अनुमान है?", "375 से 400 चिन्ह।"),
    ("धोलावीरा सूचना-पट्ट के बड़े अक्षरों को बनाने में किस सामग्री का उपयोग हुआ था?", "सफेद क्रिस्टलीय जिप्सम लेप का।")
]:
    s2_mastery_hin.append({"type": "One-Liner", "q": q, "sol": sol})

# Assertion-Reason (8)
for q, ans, sol in [
    ("Assertion (A): The Harappan script remains undeciphered despite extensive linguistic efforts.\nReason (R): No lengthy bilingual inscriptions, like the Rosetta Stone, have been discovered to provide translation keys.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): The Pashupati seal representation is widely identified as a precursor to Shiva.\nReason (R): The seated figure is depicted cross-legged in a yogic posture, wearing a horned headdress and surrounded by wild beasts.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Fire sacrifices were a major part of public religion at Mohenjo-daro.\nReason (R): Mohenjo-daro features the Great Bath but completely lacks the brick fire altars found in Rajasthan.", 3, "A is false because fire altars are absent at Mohenjo-daro. R is true."),
    ("Assertion (A): Double burials at Lothal indicate the widespread practice of ritual Sati.\nReason (R): There is no pathological evidence of forced trauma on the female skeletons to prove sacrifice.", 3, "A is false because Sati is not proven. R is true."),
    ("Assertion (A): The script was written in Boustrophedon style.\nReason (R): Consecutive lines alternate writing directions, preventing the scribe from having to lift the hand back to the right margin.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Cemetery H at Harappa belongs to the Early Harappan agrarian phase.\nReason (R): Cemetery H represents the Late Harappan culture and contains painted burial urns.", 3, "A is false because Cemetery H is Late Harappan. R is true."),
    ("Assertion (A): Stone cylinders and rings suggest fertility worship.\nReason (R): These objects resemble the lingas and yonis worshiped in historical Indian religions.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): The Dholavira signboard was used for international trade calculations.\nReason (R): The signboard was found near the Citadel gate and served as a public inscription.", 3, "A is false. R is true.")
]:
    s2_mastery_eng.append({"type": "Assertion-Reason", "q": q, "opts": ar_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("कथन (A): व्यापक प्रयासों के बावजूद हड़प्पा लिपि को आज तक पढ़ा नहीं जा सका है।\nकारण (R): रोसेटा स्टोन की तरह कोई भी बड़ा द्विभाषी अभिलेख नहीं मिला है जो अनुवाद की कुंजी प्रदान कर सके।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): पशुपति मुहर पर चित्रित आकृति को आद्य-शिव (Shiva) का अग्रदूत माना जाता है।\nकारण (R): यह आकृति योगासन में बैठी है, कूबड़ वाले बैल के सींगों का मुकुट पहने है और जंगली पशुओं से घिरी है।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): मोहनजोदड़ो में अग्नि यज्ञ सार्वजनिक धर्म का मुख्य हिस्सा थे।\nकारण (R): मोहनजोदड़ो में विशाल स्नानागार तो है लेकिन राजस्थान में मिलने वाले ईंटों के अग्निकुंड यहाँ पूर्णतः अनुपस्थित हैं।", 3, "A असत्य है क्योंकि मोहनजोदड़ो में अग्निकुंड नहीं मिले हैं। R सत्य है।"),
    ("कथन (A): लोथल में मिले युगल शवाधान बड़े पैमाने पर सती प्रथा के अस्तित्व को प्रमाणित करते हैं।\nकारण (R): महिला कंकालों पर किसी भी प्रकार के आघात या जबरन मारने के पुरातात्विक साक्ष्य नहीं मिले हैं।", 3, "A असत्य है क्योंकि सती प्रथा प्रमाणित नहीं है। R सत्य है।"),
    ("कथन (A): हड़प्पा की लिपि को बोउस्ट्रोफेडन शैली में लिखा जाता था।\nकारण (R): क्रमिक पंक्तियों में लेखन की दिशा बदलने से लेखक को प्रत्येक पंक्ति में हाथ दाईं सीमा पर वापस ले जाने की आवश्यकता नहीं होती थी।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): हड़प्पा में मिला कब्रिस्तान H (Cemetery H) प्रारंभिक हड़प्पा कृषि चरण से संबंधित है।\nकारण (R): कब्रिस्तान H उत्तर हड़प्पा संस्कृति का प्रतिनिधित्व करता है और इसमें चित्रित शवाधान कलश मिले हैं।", 3, "A असत्य है क्योंकि कब्रिस्तान H उत्तर हड़प्पा का है। R सत्य है।"),
    ("कथन (A): पत्थर के बेलन और छल्ले उर्वरता और जनन शक्ति की पूजा का संकेत देते हैं।\nकारण (R): ये पत्थर के टुकड़े बाद के ऐतिहासिक हिंदू धर्म में पूजे जाने वाले लिंग और योनि के समान दिखते हैं।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): धोलावीरा के सूचना-पट्ट का उपयोग अंतरराष्ट्रीय व्यापार के करों की गणना के लिए किया जाता था।\nकारण (R): यह सूचना-पट्ट किले के मुख्य द्वार के समीप गिरा हुआ मिला था और यह एक सार्वजनिक नाम-पट्ट था।", 3, "A असत्य है। R सत्य है।")
]:
    s2_mastery_hin.append({"type": "Assertion-Reason", "q": q, "opts": hin_ar_opts, "ans": ans, "sol": sol})

# Statement-Based (5)
for q, ans, sol in [
    ("Consider the following statements regarding the Pashupati Seal:\n1. The deity wears a three-horned headgear and sits in a yogic posture.\n2. The animals surrounding him include an elephant, a tiger, a rhinoceros, and a horse.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: the animals are elephant, tiger, rhino, and buffalo (no horse)."),
    ("Consider the following statements regarding Dholavira's script findings:\n1. Ten large signs of gypsum paste were found fallen near the Citadel gateway.\n2. This finding indicates that literacy was displayed for public notifications.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct and define the Dholavira signboard context."),
    ("Consider the following statements regarding fire altars:\n1. Altars were built of baked bricks at Kalibangan and Lothal.\n2. Fire altars have been excavated inside the Great Bath complex at Mohenjo-daro.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: fire altars are absent at Mohenjo-daro."),
    ("Consider the following statements regarding burial types:\n1. Complete inhumation aligned North-South was the most common burial type.\n2. Lothal has yielded double burials indicating joint interment.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct and define standard and double burial methods."),
    ("Consider the following statements regarding script undecipherability:\n1. The script is logo-syllabic, written in alternating Boustrophedon style.\n2. The undeciphered status leaves the language of the Indus Valley highly debated.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct, describing script properties and its undeciphered impact.")
]:
    s2_mastery_eng.append({"type": "Statement-Based", "q": q, "opts": mcq_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("पशुपति मुहर के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. देव तीन सींगों वाला मुकुट पहने हैं और योगासन मुद्रा में बैठे हैं।\n2. उन्हें घेरने वाले पशुओं में हाथी, बाघ, गैंडा और घोड़ा शामिल हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि जानवर हाथी, बाघ, गैंडा और भैंसा हैं (घोड़ा नहीं)।"),
    ("धोलावीरा के लिपि अवशेषों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. किले के प्रवेश द्वार के समीप जिप्सम लेप से बने दस बड़े अक्षर गिरे हुए मिले थे।\n2. यह खोज दर्शाती है कि साक्षरता का उपयोग सार्वजनिक सूचनाओं के प्रदर्शन के लिए किया जाता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 2, "दोनों कथन सही हैं और धोलावीरा सूचना-पट्ट की प्रासंगिकता को स्पष्ट करते हैं।"),
    ("अग्निकुंडों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. कालीबंगन और लोथल में पकी ईंटों से बने अग्निकुंड मिले हैं।\n2. मोहनजोदड़ो के विशाल स्नानागार परिसर के भीतर भी अग्निकुंड खोदे गए हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि मोहनजोदड़ो में अग्निकुंड नहीं मिले हैं।"),
    ("शवाधान विधियों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. उत्तर-दक्षिण संरेखण में दफनाना (पूर्ण शवाधान) सबसे आम प्रथा थी।\n2. लोथल से युगल शवाधान (double burials) के साक्ष्य मिले हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 2, "दोनों कथन सही हैं और सामान्य तथा युगल शवाधान विधियों का वर्णन करते हैं।"),
    ("अपठित लिपि के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह लिपि चित्रात्मक और लोगो-सिलेबिक है, जिसे बोउस्ट्रोफेडन शैली में लिखा जाता था।\n2. लिपि के न पढ़े जाने के कारण सिंधु घाटी के लोगों की मूल भाषा आज भी अत्यधिक विवादित है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 2, "दोनों कथन सही हैं, जो लिपि की प्रकृति और उसके अपठित होने के ऐतिहासिक प्रभावों को स्पष्ट करते हैं।")
]:
    s2_mastery_hin.append({"type": "Statement-Based", "q": q, "opts": hin_mcq_opts, "ans": ans, "sol": sol})

# Why (3)
for q, sol in [
    ("Why was the Harappan script written in Boustrophedon direction?", "To optimize continuous writing flow, preventing scribes from lifting their hands back to the right margin at the start of every new line."),
    ("Why did the Harappans align graves head pointing North?", "It reflected a standardized spiritual or cosmological belief regarding the transition of the soul aligned to the earth's primary axis."),
    ("Why are fire altars present at Kalibangan and Lothal but absent at Mohenjo-daro?", "It indicates regional variations in religious practices, showing that Vedic-like fire sacrifice was localized to Rajasthan and Gujarat rather than Sindh.")
]:
    s2_mastery_eng.append({"type": "Why", "q": q, "sol": sol})

for q, sol in [
    ("हड़प्पा की लिपि को बोउस्ट्रोफेडन (Boustrophedon) शैली में क्यों लिखा जाता था?", "लेखन प्रवाह को निरंतर बनाए रखने के लिए, ताकि प्रत्येक नई पंक्ति के प्रारंभ में लेखक को हाथ उठाकर पुनः दाईं ओर न ले जाना पड़े।"),
    ("हड़प्पा वासी शवों को हमेशा उत्तर दिशा में सिर करके ही क्यों दफनाते थे?", "यह पृथ्वी के ध्रुवीय अक्ष के संरेखण में आत्मा के गमन से संबंधित उनके किसी मानकीकृत आध्यात्मिक या ब्रह्मांडीय विश्वास को दर्शाता है।"),
    ("कालीबंगन और लोथल में अग्निकुंड क्यों मिले हैं, जबकि मोहनजोदड़ो में ये अनुपस्थित हैं?", "यह धार्मिक प्रथाओं में क्षेत्रीय भिन्नताओं को दर्शाता है, जिससे पता चलता है कि अग्नि यज्ञ की प्रथा केवल राजस्थान और गुजरात तक सीमित थी, सिंध में नहीं।")
]:
    s2_mastery_hin.append({"type": "Why", "q": q, "sol": sol})

# How (3)
for q, sol in [
    ("How did the Pashupati seal portray animistic power and deity authority?", "By placing the seated yogic deity in a central, dominant position surrounded by wild forest beasts, establishing him as lord of animals."),
    ("How did the Dholavira signboard letters withstand weathering before discovery?", "The letters were made of thick white gypsum paste inset into a wooden board, which fell face-down into the silt, protecting the gypsum shapes from erosion."),
    ("How did burial goods reflect the socio-economic status of the deceased?", "Common graves contained simple clay pots; high-status graves featured brick lining, copper mirrors, beads of semi-precious stones, and gold ornaments.")
]:
    s2_mastery_eng.append({"type": "How", "q": q, "sol": sol})

for q, sol in [
    ("पशुपति मुहर ने वन्य जीव शक्ति और देवता के अधिकार को कैसे प्रदर्शित किया?", "योगासन में बैठे देव को मुहर के केंद्र में रखकर और उनके चारों ओर विशाल जंगली जानवरों को चित्रित करके, उन्हें 'पशुओं का स्वामी' (पशुपति) सिद्ध किया गया।"),
    ("धोलावीरा सूचना-पट्ट के अक्षर खोज से पहले मौसम की मार से कैसे बचे रहे?", "अक्षर लकड़ी के तख्ते पर सफेद जिप्सम लेप से बने थे, जो तख्ता टूटकर मुंह के बल मिट्टी में गिर गया, जिससे अक्षरों की जिप्सम आकृतियाँ सुरक्षित रह सकीं।"),
    ("शवाधान की वस्तुएं मृतक की सामाजिक-आर्थिक स्थिति को किस प्रकार दर्शाती थीं?", "सामान्य कब्रों में केवल मिट्टी के बर्तन मिले हैं, जबकि समृद्ध लोगों की कब्रों में ईंटों की चिनाई, तांबे के दर्पण, अकीक व जेड के मनके और सोने के आभूषण मिले हैं।")
]:
    s2_mastery_hin.append({"type": "How", "q": q, "sol": sol})

# Case Study (3)
for q, sol in [
    ("Case Study: The Dholavira Signboard Gateway", "Found near the northern gate of Dholavira's Citadel, it consists of ten signs made of white gypsum paste. This indicates that the Harappan script was used for public civic notifications, displaying administrative authority to visitors entering the fort."),
    ("Case Study: Lothal's Double Burials", "Excavations yielded three graves containing skeletons of a male and female buried together. Some scholars theorized Sati, but the lack of trauma suggests simultaneous death by disease or a joint funerary custom unique to this coastal trading hub."),
    ("Case Study: Cemetery H Cult Transitions", "Located at Harappa, Cemetery H urns contain painted birds, peacocks carrying human forms, and stars. This late phase indicates a shift from ground burial to urn cremation, reflecting changing spiritual beliefs regarding the soul's journey after death.")
]:
    s2_mastery_eng.append({"type": "Case Study", "q": q, "sol": sol})

for q, sol in [
    ("केस स्टडी: धोलावीरा का प्रवेश द्वार सूचना-पट्ट", "धोलावीरा के किले के उत्तरी प्रवेश द्वार के समीप जिप्सम से बने 10 अक्षरों वाला सूचना-पट्ट मिला है। यह दर्शाता है कि हड़प्पा लिपि का उपयोग द्वारों पर सार्वजनिक सूचना देने और आने वाले अतिथियों को प्रशासनिक सत्ता दिखाने के लिए होता था।"),
    ("केस स्टडी: लोथल का युगल शवाधान (Double Burials)", "लोथल से तीन कब्रें मिली हैं जिनमें एक ही स्थान पर पुरुष और महिला के कंकाल दबे हैं। कुछ विद्वानों ने इसे सती प्रथा माना, लेकिन हड्डियों पर चोट की कमी यह बताती है कि यह बीमारी से मृत्यु या कोई विशिष्ट तटीय शवाधान प्रथा थी।"),
    ("केस स्टडी: कब्रिस्तान H में सांस्कृतिक संक्रमण", "हड़प्पा के कब्रिस्तान H से प्राप्त कलशों पर मोर, पक्षियों और मानव आकृतियों के चित्र मिले हैं। यह उत्तर-हड़प्पा काल में जमीन में दफनाने के स्थान पर कलश दाह संस्कार की ओर बदलाव को दर्शाता है, जो आत्मा के संबंध में बदलते विचारों को सिद्ध करता है।")
]:
    s2_mastery_hin.append({"type": "Case Study", "q": q, "sol": sol})

# Teach Concept (3)
for q, sol in [
    ("Teach Concept: The Mechanics of Boustrophedon Writing", "Explain the plowing metaphor. Boustrophedon comes from Greek meaning 'ox-turning'. Scribes write first line right-to-left. Instead of returning the pen, they drop to the next line and write left-to-right, creating a continuous snake-like reading flow."),
    ("Teach Concept: Animism and Nature Deities", "Teach how early religions deified environmental forces. Worship of the pipal tree, humped bull, and ritual baths shows that Harappan spirituality centered on ecological harmony, fertility of the soil, and cleansing, rather than temple priesthoods."),
    ("Teach Concept: Decipherment Challenges of Logo-Syllabic Scripts", "Explain why the script remains unread. Scribes used around 400 signs, meaning it is logo-syllabic (each sign represents a word or syllable, not an alphabet). Without a bilingual Rosetta stone key, decipherment relies on computer database models, causing major debates.")
]:
    s2_mastery_eng.append({"type": "Teach Concept", "q": q, "sol": sol})

for q, sol in [
    ("अवधारणा समझाएं (Teach Concept): बोउस्ट्रोफेडन लेखन की यांत्रिकी", "बैल जोतने के रूपक को समझाएं। बोउस्ट्रोफेडन ग्रीक शब्द है जिसका अर्थ है 'बैल का मुड़ना'। लेखक पहली पंक्ति दाएं से बाएं लिखता था, और फिर हाथ को वापस दाईं सीमा पर ले जाने के बजाय अगली पंक्ति को सीधे बाएं से दाएं लिखता था, जिससे सांप जैसा लेखन प्रवाह बनता था।"),
    ("अवधारणा समझाएं (Teach Concept): जीववाद (Animism) और प्रकृति पूजा", "समझाएं कि प्राचीन धर्मों में प्रकृति की शक्तियों को कैसे देवत्व दिया गया। पीपल, सांड और पवित्र स्नान का महत्व दिखाता है कि उनका धर्म मंदिर के पुरोहितों के स्थान पर पारिस्थितिक संतुलन, मिट्टी की उर्वरता और शुद्धि पर आधारित था।"),
    ("अवधारणा समझाएं (Teach Concept): लोगो-सिलेबिक लिपियों को पढ़ने की चुनौतियाँ", "समझाएं कि यह लिपि आज तक अपठित क्यों है। इसमें लगभग 400 चिन्ह मिले हैं, यानी यह वर्णमाला नहीं बल्कि लोगो-सिलेबिक (शब्द-अक्षर आधारित) है। रोसेटा स्टोन जैसी किसी द्विभाषी कुंजी के बिना इसे पढ़ना बहुत कठिन है और यह कंप्यूटर मॉडलों पर निर्भर है।")
]:
    s2_mastery_hin.append({"type": "Teach Concept", "q": q, "sol": sol})


# =========================================================================
# SECTION 3: ART, CRAFTS, AMUSEMENTS & TOYS
# =========================================================================
s3_mastery_eng = []
s3_mastery_hin = []

# MCQ (5)
for q, opts, ans, sol in [
    ("The 10cm bronze 'Dancing Girl' figurine from Mohenjo-daro was cast using which ancient metallurgical method?", ["Solid lost-wax casting (cire perdue)", "Sand mold casting", "Hollow sheet hammering", "Cold copper chiseling"], 0, "The Dancing Girl is a masterpiece of solid bronze lost-wax (cire perdue) casting."),
    ("Which soft soapstone was the primary medium for carving the iconic Priest-King bust?", ["Steatite", "Chert", "Carnelian", "Lapis Lazuli"], 0, "The Priest-King bust is carved from soft steatite soapstone, which hardens when baked."),
    ("At which industrial settlement was a massive bead manufacturing factory with furnaces discovered?", ["Chanhudaro", "Kalibangan", "Rakhigarhi", "Banawali"], 0, "Chanhudaro (and Lothal) had bead manufacturing workshops equipped with specialized furnaces and drills."),
    ("What unique anatomical feature characterizes the red sandstone human torso sculpture from Harappa?", ["Sockets in the neck and shoulders for attaching movable limbs", "Elongated half-closed eyes", "A patterned shawl draped over the left shoulder", "A fan-shaped headdress made of baked clay"], 0, "The red sandstone torso from Harappa features circular sockets in the neck and shoulders to attach movable limbs."),
    ("What amusement device, carved from chert or terracotta with dotted markings, is a common find in Harappan houses?", ["Cubical dice", "Circular checker pieces", "Iron playing cards", "Spinning metal roulette wheels"], 0, "Cubical dice with dotted numbers 1 to 6 made of chert or clay are common domestic findings.")
]:
    s3_mastery_eng.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("मोहनजोदड़ो से प्राप्त 10 सेमी की कांस्य 'नर्तकी' (Dancing Girl) को किस धातुकर्म विधि द्वारा ढाला गया था?", ["ठोस लुप्त-मोम ढलाई (lost-wax/cire perdue)", "रेत के सांचे में ढलाई", "खोखली धातु की चादर पीटना", "तांबे को ठंडी छेनी से काटना"], 0, "नर्तकी की मूर्ति ठोस कांस्य की लुप्त-मोम (lost-wax) ढलाई का सबसे प्राचीन और बेहतरीन नमूना है।"),
    ("पुरोहित-राजा (Priest-King) की प्रसिद्ध मूर्ति को तराशने के लिए किस नरम साबुन-पत्थर (soapstone) का उपयोग किया गया था?", ["सेलखड़ी (Steatite)", "चर्ट (Chert)", "अकीक (Carnelian)", "लाजवर्त (Lapis)"], 0, "पुरोहित-राजा की मूर्ति को सेलखड़ी से बनाया गया था, जो तराशने के बाद गर्म करने पर कड़ा हो जाता था।"),
    ("किस औद्योगिक हड़प्पा बस्ती से भट्टियों और सूक्ष्म उपकरणों से युक्त मनके बनाने का कारखाना मिला है?", ["चन्हुदड़ो", "कालीबंगन", "राखीगढ़ी", "बनावली"], 0, "चन्हुदड़ो (और लोथल) में मनके बनाने के कारखाने मिले हैं जहाँ भट्टियाँ और ड्रिल उपकरण प्रयुक्त होते थे।"),
    ("हड़प्पा से प्राप्त लाल बलुआ पत्थर के मानव धड़ (torso) की विशिष्ट शारीरिक विशेषता क्या है?", ["सिर और कंधे पर घूमने वाले अंग लगाने के लिए सॉकेट (छेद) होना", "लंबी और आधी बंद आँखें होना", "बाएं कंधे पर तिपतिया सज्जा वाला शॉल होना", "पकी मिट्टी का पंखे के आकार का मुकुट होना"], 0, "हड़प्पा के लाल बलुआ पत्थर के धड़ में गर्दन और कंधों पर घूमने वाले हाथ-पैर लगाने के लिए सॉकेट बने मिले हैं।"),
    ("घरों से प्राप्त मनोरंजक साधनों में किस बिंदु-चिह्नित उपकरण की बहुलता मिली है?", ["घनाकार पासे (cubical dice)", "गोलाकार गोटियां", "लोहे के ताश के पत्ते", "कांसे का पहिया"], 0, "चर्ट या मिट्टी के बने घनाकार पासे जिन पर 1 से 6 तक के बिंदु बने थे, घरों से आम तौर पर प्राप्त हुए हैं।")
]:
    s3_mastery_hin.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# Multi-Correct MCQ (5)
for q, opts, ans, sol in [
    ("Which materials were utilized by Harappan bead makers to manufacture export-grade ornaments? (Select all that apply)", ["Carnelian", "Lapis Lazuli", "Steatite", "Imported Platinum"], [0, 1, 2], "Beadmakers used carnelian, lapis lazuli, and steatite. Platinum was unknown in Bronze Age metallurgy."),
    ("Select the kinetic features observed in Harappan terracotta toys: (Select all that apply)", ["Toy carts with rotating wheels", "Humped bulls with nodding heads operated by string", "Monkeys that slide down ropes", "Clockwork wind-up gears"], [0, 1, 2], "Carts, nodding bulls, and sliding monkeys are verified kinetic toys. Clockwork gears did not exist."),
    ("Which characteristics define the bronze Dancing Girl figurine? (Select all that apply)", ["Stands in a relaxed tribhanga posture", "Left arm is covered with dozens of bangles", "Created using the lost-wax casting method", "Wears an elaborate fan-shaped clay crown"], [0, 1, 2], "The Dancing Girl is bronze (lost-wax), in tribhanga, with left arm bangles. The clay crown is found on terracotta Mother Goddesses."),
    ("Identify the stone sculptures recovered from mature Harappan sites: (Select all that apply)", ["Bearded Priest-King bust from Mohenjo-daro", "Red sandstone athletic human torso from Harappa", "Seated grey stone male figure with sockets", "Massive marble statue of a charioteer"], [0, 1, 2], "The Priest-King, red sandstone torso, and grey seated male are verified stone sculptures. Marble charioteers are absent."),
    ("What pastimes were popular in Harappan cities? (Select all that apply)", ["Board games resembling chess with clay checkers", "Dice rolling using cubical chert blocks", "Animal fighting (cockfighting and bull fights)", "Gladiator tournaments in open amphitheaters"], [0, 1, 2], "Board games, dice, and animal fights were popular. Gladiator tournaments were Roman, not Harappan.")
]:
    s3_mastery_eng.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("हड़प्पा के मनका निर्माताओं द्वारा निर्यात-योग्य आभूषण बनाने के लिए किन सामग्रियों का उपयोग किया जाता था? (सभी लागू विकल्प चुनें)", ["अकीक (Carnelian)", "लाजवर्त (Lapis)", "सेलखड़ी (Steatite)", "आयातित प्लेटिनम"], [0, 1, 2], "मनकों के लिए अकीक, लाजवर्त और सेलखड़ी प्रयुक्त होते थे। प्लेटिनम का ज्ञान कांस्य युग में नहीं था।"),
    ("हड़प्पा के मिट्टी के खिलौनों में पाए जाने वाले गतिज (kinetic) लक्षणों का चयन करें: (सभी लागू विकल्प चुनें)", ["घूमने वाले पहियों वाली खिलौना गाड़ियाँ", "धागे से नियंत्रित हिलने वाले सिर वाले सांड", "रस्सी पर सरकने वाले बंदर", "चाबी से चलने वाले गियर तंत्र"], [0, 1, 2], "गाड़ियाँ, हिलने वाले सिर वाले सांड और रस्सी पर सरकने वाले बंदर गतिज खिलौने हैं। चाबी वाले गियर नहीं थे।"),
    ("कांस्य की नर्तकी (Dancing Girl) की मूर्ति को कौन से लक्षण परिभाषित करते हैं? (सभी लागू विकल्प चुनें)", ["शिथिल त्रिभंग मुद्रा में खड़ी होना", "बायां हाथ दर्जनों चूड़ियों से ढका होना", "लुप्त-मोम ढलाई विधि से निर्मित होना", "मिट्टी का पंखे के आकार का भारी मुकुट पहना होना"], [0, 1, 2], "नर्तकी त्रिभंग में है, बायां हाथ चूड़ियों से ढका है और लुप्त-मोम से बनी है। मुकुट मिट्टी की मूर्तियों पर था, इस पर नहीं।"),
    ("परिपक्व हड़प्पा स्थलों से प्राप्त पाषाण मूर्तियों की पहचान करें: (सभी लागू विकल्प चुनें)", ["मोहनजोदड़ो से प्राप्त दाढ़ी वाले पुरोहित-राजा की मूर्ति", "हड़प्पा से प्राप्त लाल बलुआ पत्थर का मानव धड़", "सॉकेट युक्त धूसर (grey) पत्थर की पुरुष आकृति", "संगमरमर से बनी रथ चालक की विशाल मूर्ति"], [0, 1, 2], "पुरोहित-राजा, लाल बलुआ पत्थर धड़ और सॉकेट वाली धूसर मूर्ति प्रामाणिक पाषाण कला हैं। संगमरमर के रथ चालक नहीं मिले हैं।"),
    ("हड़प्पा शहरों में कौन से मनोरंजन लोकप्रिय थे? (सभी लागू विकल्प चुनें)", ["मिट्टी की गोटियों वाले शतरंज जैसे बोर्ड गेम", "घनाकार चर्ट के पासे फेंकना", "तीतर-मुर्गों की लड़ाई और सांडों से लड़ना", "खुले अखाड़ों में ग्लैडीएटरों की खूनी कुश्तियाँ"], [0, 1, 2], "बोर्ड गेम, पासे और मुर्गों की लड़ाई लोकप्रिय खेल थे। ग्लैडीएटर कुश्तियाँ रोम की विशेषता थीं, हड़प्पा की नहीं।")
]:
    s3_mastery_hin.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# True/False (8)
for q, ans, sol in [
    ("The bronze Dancing Girl was cast using the solid lost-wax process.", True, "True. She is a solid cast bronze figurine made using the lost-wax process."),
    ("The red sandstone torso from Harappa has sockets to attach limbs.", True, "True. The torso has circular socket holes in the neck and shoulders."),
    ("Bead factories with specialized micro-drills have been found at Kalibangan.", False, "False. Bead factories are located at Chanhudaro and Lothal, not Kalibangan."),
    ("Harappans used cubical chert dice with dots representing numbers.", True, "True. Cubical dice similar to modern dice have been recovered from domestic houses."),
    ("No metal tools or sculptures were produced; they were exclusively stone-age.", False, "False. They were in the Bronze Age, producing bronze tools and sculptures like the Dancing Girl."),
    ("Cockfighting was one of the popular pastimes depicted in Harappan art.", True, "True. Seals and clay models show bird/cockfighting representations."),
    ("The Priest-King statue is made of solid copper.", False, "False. The Priest-King is made of steatite (soapstone)."),
    ("Toy whistles shaped like birds were made of hollow terracotta.", True, "True. Hollow clay whistles shaped like sparrows are common children's toys.")
]:
    s3_mastery_eng.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("कांस्य की नर्तकी की मूर्ति ठोस लुप्त-मोम विधि द्वारा बनाई गई थी।", True, "सत्य। यह लुप्त-मोम ढलाई की ठोस मूर्ति है।"),
    ("हड़प्पा से प्राप्त लाल बलुआ पत्थर के धड़ में हाथ-पैर जोड़ने के लिए सॉकेट हैं।", True, "सत्य। गर्दन और कंधों पर घूमने वाले अंग लगाने के लिए सॉकेट छेद बने हैं।"),
    ("सूक्ष्म उपकरणों से युक्त मनके बनाने के कारखाने कालीबंगन में मिले हैं।", False, "असत्य। मनके बनाने के कारखाने चन्हुदड़ो और लोथल में मिले हैं, कालीबंगन में नहीं।"),
    ("हड़प्पा वासी बिंदु-अंकित घनाकार चर्ट के पासों का उपयोग करते थे।", True, "सत्य। आधुनिक पासों जैसे घनाकार पासे घरों से खोजे गए हैं।"),
    ("वहाँ कोई धातु के उपकरण या मूर्तियाँ नहीं बनती थीं; वे केवल पाषाण युगीन थे।", False, "असत्य। वे कांस्य युगीन थे और धातु उपकरण व कांस्य की मूर्तियाँ बनाते थे।"),
    ("तीतर-मुर्गों की लड़ाई हड़प्पा कला में दर्शाया गया एक लोकप्रिय मनोरंजन था।", True, "सत्य। मुहरों और मिट्टी के अवशेषों में पक्षियों की लड़ाई के चित्र मिले हैं।"),
    ("पुरोहित-राजा की मूर्ति ठोस तांबे से बनी है।", False, "असत्य। पुरोहित-राजा की मूर्ति सेलखड़ी (steatite) पत्थर से बनी है।"),
    ("पक्षियों के आकार की खिलौना सीटियाँ खोखली मिट्टी से बनाई जाती थीं।", True, "सत्य। गौरैया के आकार की खोखली मिट्टी की सीटियाँ आम बच्चों के खिलौने थे।")
]:
    s3_mastery_hin.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

# Fill Blank (8)
for q, ans, sol in [
    ("The solid lost-wax bronze casting method is also known as __________.", "cire perdue", "Cire perdue is the French term for lost-wax casting."),
    ("The Priest-King statue was carved from a soft stone called __________.", "steatite", "Steatite soapstone was used to carve the Priest-King bust."),
    ("A major bead manufacturing center in Gujarat was __________.", "Lothal", "Lothal had bead factories alongside Chanhudaro."),
    ("The red sandstone human torso with sockets was excavated at __________.", "Harappa", "The torso was discovered at Harappa."),
    ("Domestic games used cubical dice carved from clay or __________.", "chert", "Chert and clay were standard materials for dice."),
    ("Hollow sparrow-shaped clay toys that produce sound are __________.", "whistles", "Bird whistles are hollow terracotta toys."),
    ("Harappans alloying copper with __________ to produce durable bronze.", "tin", "Copper was alloyed with tin to manufacture bronze."),
    ("The jewelry makers used red __________ stone to carve long cylindrical beads.", "carnelian", "Red carnelian was prized for making long cylindrical beads.")
]:
    s3_mastery_eng.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("ठोस लुप्त-मोम कांस्य ढलाई पद्धति को __________ भी कहा जाता है।", "सिरे परड्यू", "सिरे परड्यू (cire perdue) लुप्त-मोम ढलाई का तकनीकी नाम है।"),
    ("पुरोहित-राजा की प्रतिमा को __________ नामक नरम पत्थर से तराशा गया था।", "सेलखड़ी", "यह मूर्ति सेलखड़ी (steatite/soapstone) से बनी थी।"),
    ("गुजरात में स्थित मनका निर्माण का प्रमुख औद्योगिक केंद्र __________ था।", "लोथल", "लोथल में मनके बनाने के बड़े कारखाने मिले हैं।"),
    ("हाथ-पैर जोड़ने के छेद (sockets) वाला लाल बलुआ पत्थर का मानव धड़ __________ से मिला है।", "हड़प्पा", "यह धड़ हड़प्पा नामक स्थल से उत्खनन में मिला था।"),
    ("घरेलू खेलों के पासे मिट्टी या __________ पत्थर से बनाए जाते थे।", "चर्ट", "बाट और पासे बनाने के लिए घनाकार चर्ट पत्थर का उपयोग होता था।"),
    ("चिड़िया के आकार के मिट्टी के खिलौने जो फूंकने पर आवाज करते थे, __________ कहलाते हैं।", "सीटियाँ", "गौरैया के आकार की खोखली मिट्टी की सीटियाँ खिलौने थीं।"),
    ("हड़प्पा वासी तांबे में __________ मिलाकर मजबूत कांसा तैयार करते थे।", "टिन", "कांसा (bronze) बनाने के लिए तांबे में टिन मिलाया जाता था।"),
    ("मनका बनाने के लिए प्रयुक्त लाल रंग का अर्द्ध-कीमती चमकीला पत्थर __________ था।", "अकीक", "लाल रंग के अकीक (carnelian) पत्थर से लंबे बेलनाकार मनके बनते थे।")
]:
    s3_mastery_hin.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

# Match the Following (3)
s3_mastery_eng.extend([
    {
        "type": "Match the Following",
        "q": "Match the art objects with their primary manufacturing materials:",
        "items": [{"left": "I. Dancing Girl Figurines", "key": "A"}, {"left": "II. Priest-King Bust", "key": "B"}, {"left": "III. Node-head Bull Toys", "key": "C"}],
        "options": [{"val": "A", "text": "A. Solid cast copper-tin bronze"}, {"val": "B", "text": "B. Baked block steatite soapstone"}, {"val": "C", "text": "C. Hand-modeled baked clay (terracotta)"}],
        "sol": "Dancing Girl is bronze, Priest-King is steatite, and bull toys are terracotta."
    },
    {
        "type": "Match the Following",
        "q": "Match the craft workshops with their industrial hubs:",
        "items": [{"left": "I. Bead Factory & Micro-drills", "key": "A"}, {"left": "II. Shell Working & Bangle Shops", "key": "B"}, {"left": "III. Bronze Melting Furnaces", "key": "C"}],
        "options": [{"val": "A", "text": "A. Chanhudaro and Lothal"}, {"val": "B", "text": "B. Balakot and Lothal"}, {"val": "C", "text": "C. Mohenjo-daro and Harappa"}],
        "sol": "Beads were made at Chanhudaro/Lothal, shell bangle shops at Balakot/Lothal, and bronze furnaces at Mohenjo-daro/Harappa."
    },
    {
        "type": "Match the Following",
        "q": "Match the toys with their kinetic or design features:",
        "items": [{"left": "I. Bullock Carts", "key": "A"}, {"left": "II. Sparrows", "key": "B"}, {"left": "III. Nodding Cattle", "key": "C"}],
        "options": [{"val": "A", "text": "A. Moving terracotta wheels on wooden axles"}, {"val": "B", "text": "B. Hollow body acting as a whistle when blown"}, {"val": "C", "text": "C. Head attached to a string passing through the neck"}],
        "sol": "Carts had moving wheels, sparrows were hollow whistles, and nodding cattle used neck strings."
    }
])

s3_mastery_hin.extend([
    {
        "type": "Match the Following",
        "q": "कलाकृतियों को उनकी निर्माण सामग्री से सुमेलित करें:",
        "items": [{"left": "I. नर्तकी की मूर्ति", "key": "A"}, {"left": "II. पुरोहित-राजा की मूर्ति", "key": "B"}, {"left": "III. हिलते सिर वाले सांड", "key": "C"}],
        "options": [{"val": "A", "text": "A. ठोस ढाला गया तांबा-टिन कांसा"}, {"val": "B", "text": "B. बेक की हुई सेलखड़ी (Steatite)"}, {"val": "C", "text": "C. हाथ से ढाली पकी मिट्टी (Terracotta)"}],
        "sol": "नर्तकी कांसे से, पुरोहित-राजा सेलखड़ी से, और सांड खिलौने मिट्टी से बने हैं।"
    },
    {
        "type": "Match the Following",
        "q": "शिल्प केंद्रों को उनके औद्योगिक स्थलों से सुमेलित करें:",
        "items": [{"left": "I. मनके का कारखाना और ड्रिल", "key": "A"}, {"left": "II. शंख उद्योग और चूड़ी की दुकानें", "key": "B"}, {"left": "III. तांबा गलाने की भट्टियाँ", "key": "C"}],
        "options": [{"val": "A", "text": "A. चन्हुदड़ो और लोथल"}, {"val": "B", "text": "B. बालाकोट और लोथल"}, {"val": "C", "text": "C. मोहनजोदड़ो और हड़प्पा"}],
        "sol": "मनके चन्हुदड़ो/लोथल में, शंख चूड़ियाँ बालाकोट/लोथल में, और तांबा भट्टी मोहनजोदड़ो/हड़प्पा में मिली हैं।"
    },
    {
        "type": "Match the Following",
        "q": "खिलौनों को उनके गतिज या डिजाइन लक्षणों से सुमेलित करें:",
        "items": [{"left": "I. बैलगाड़ियाँ", "key": "A"}, {"left": "II. गौरैया (Sparrows)", "key": "B"}, {"left": "III. हिलते सिर वाले मवेशी", "key": "C"}],
        "options": [{"val": "A", "text": "A. लकड़ी की धुरी पर घूमने वाले मिट्टी के पहिये"}, {"val": "B", "text": "B. फूंक मारने पर सीटी बजाने वाली खोखली संरचना"}, {"val": "C", "text": "C. गर्दन के रास्ते धागे से हिलने के लिए जुड़ा सिर"}],
        "sol": "बैलगाड़ी में घूमने वाले पहिए थे, गौरैया खोखली सीटी थी, और मवेशी धागे वाले हिलते सिर वाले थे।"
    }
])

# One-Liner (8)
for q, sol in [
    ("What metallurgic casting method was used to produce the Dancing Girl?", "Solid lost-wax casting (cire perdue)."),
    ("Which soft soapstone was preferred for carving high-value seals and busts?", "Steatite."),
    ("Name the industrial center in Sindh specializing in bead making.", "Chanhudaro."),
    ("What unique structural feature did the Harappan red sandstone torso have?", "Circular sockets in the neck and shoulders for attaching limbs."),
    ("What shape were the chert and clay dice found in Harappan homes?", "Cubical shape."),
    ("What bird species shaped the common terracotta toy whistles?", "Sparrow (bird whistle)."),
    ("Which two metals did Harappans alloy to make bronze?", "Copper and tin."),
    ("What red gemstone was highly prized for making cylindrical beads?", "Carnelian.")
]:
    s3_mastery_eng.append({"type": "One-Liner", "q": q, "sol": sol})

for q, sol in [
    ("नर्तकी की कांस्य मूर्ति को बनाने में किस धातुकर्म ढलाई विधि का उपयोग हुआ था?", "ठोस लुप्त-मोम (lost-wax/cire perdue) ढलाई विधि।"),
    ("मुहरों और मूर्तियों को तराशने के लिए किस नरम पत्थर को प्राथमिकता दी जाती थी?", "सेलखड़ी (steatite/soapstone) को।"),
    ("सिंध में स्थित मनके बनाने के लिए प्रसिद्ध औद्योगिक केंद्र का नाम क्या है?", "चन्हुदड़ो (Chanhudaro)।"),
    ("हड़प्पा के लाल बलुआ पत्थर के मानव धड़ में क्या विशिष्ट ढांचागत सुराख थे?", "गर्दन और कंधों पर हाथ-पैर जोड़ने वाले गोलाकार सॉकेट।"),
    ("घरों से प्राप्त मिट्टी और चर्ट के पासे किस ज्यामितीय आकार के होते थे?", "घनाकार (cubical) आकार के।"),
    ("गौरैया के आकार के मिट्टी के सीटी खिलौने किस सामग्री से बनते थे?", "खोखली पकी मिट्टी (terracotta) से।"),
    ("कांसा बनाने के लिए हड़प्पा वासी किन दो धातुओं को मिश्रित करते थे?", "तांबा और टिन।"),
    ("बेलनाकार मनके बनाने के लिए किस लाल रंग के चमकीले रत्न का उपयोग होता था?", "अकीक (carnelian)।")
]:
    s3_mastery_hin.append({"type": "One-Liner", "q": q, "sol": sol})

# Assertion-Reason (8)
for q, ans, sol in [
    ("Assertion (A): The bronze Dancing Girl represents the pinnacle of Bronze Age metal art.\nReason (R): She was cast using the solid lost-wax casting technique, indicating advanced metallurgical skills.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): The red sandstone human torso from Harappa displays outstanding anatomical realism.\nReason (R): The torso features circular sockets to attach movable stone limbs, a highly creative sculpture technique.", 1, "Both A and R are true but R is not the explanation of anatomical realism (realism is about muscle contours)."),
    ("Assertion (A): Chanhudaro was a dedicated industrial workshop for craft production.\nReason (R): Archaeologists recovered bead factories, micro-drills, metal furnaces, and shell bangles from the site.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Cubical dice found in Harappan houses prove they participated in domestic gambling.\nReason (R): The dice are made of chert or terracotta and feature dotted markings similar to modern dice.", 1, "Both A and R are true but R does not explain why they participated in gambling (it just describes the dice)."),
    ("Assertion (A): Harappans did not produce any metal tools and were stuck in the Neolithic era.\nReason (R): The Bronze Age Harappans alloyed copper and tin to produce axes, knives, and statues.", 3, "A is false. R is true."),
    ("Assertion (A): Sparrows shaped the hollow clay toy whistles found in residential sites.\nReason (R): Sparrows were highly common birds in the Indus valley and children used the whistles for play.", 1, "Both A and R are true but R does not explain why they are sparrow-shaped (it just describes the habitat)."),
    ("Assertion (A): The Priest-King statue is made of solid cast bronze.\nReason (R): The Priest-King was carved from soft steatite soapstone and baked to harden.", 3, "A is false because it is steatite, not bronze. R is true."),
    ("Assertion (A): Red carnelian was a highly prized export gemstone to Mesopotamia.\nReason (R): Carnelian beads were drilled using specialized micro-drills and polished to a high luster at Lothal.", 0, "Both A and R are true and R is the correct explanation of A.")
]:
    s3_mastery_eng.append({"type": "Assertion-Reason", "q": q, "opts": ar_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("कथन (A): कांस्य की नर्तकी (Dancing Girl) कांस्य युग की धातु कला के चरम शिखर का प्रतिनिधित्व करती है।\nकारण (R): इसे ठोस लुप्त-मोम (lost-wax) विधि से ढाला गया है, जो धातुकर्म के उन्नत ज्ञान को सिद्ध करता है।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): हड़प्पा से प्राप्त लाल बलुआ पत्थर का मानव धड़ उत्कृष्ट शारीरिक यथार्थवाद दर्शाता है।\nकारण (R): इस धड़ में घूमने वाले हाथ-पैर जोड़ने के लिए गोलाकार सॉकेट बने हैं जो अत्यंत रचनात्मक कला का प्रमाण है।", 1, "A और R दोनों सत्य हैं लेकिन R यथार्थवाद की व्याख्या नहीं करता (यथार्थवाद मांसपेशियों के गोलाई प्रतिरूप से संबंधित है)।"),
    ("कथन (A): चन्हुदड़ो शिल्प उत्पादन के लिए समर्पित एक प्रमुख औद्योगिक बस्ती थी।\nकारण (R): उत्खनन में यहाँ मनके के कारखाने, सूक्ष्म ड्रिल, तांबे की भट्टी और शंख के टुकड़े प्राप्त हुए हैं।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): घरों से प्राप्त घनाकार पासे यह प्रमाणित करते हैं कि वे जुए जैसे घरेलू खेलों में भाग लेते थे।\nकारण (R): ये पासे चर्ट और मिट्टी से बने हैं और इन पर आधुनिक पासों की तरह बिंदु-निशान बने हैं।", 1, "A और R दोनों सत्य हैं लेकिन R जुए की प्रवृत्ति की व्याख्या नहीं करता (यह केवल पासे का विवरण देता है)।"),
    ("कथन (A): हड़प्पा वासी कोई भी धातु उपकरण नहीं बनाते थे और वे नवपाषाण युग में ही अटके हुए थे।\nकारण (R): कांस्य युगीन हड़प्पा वासियों ने कुल्हाड़ियों, चाकुओं और मूर्तियों को बनाने के लिए तांबे और टिन का मिश्रण किया।", 3, "A असत्य है। R सत्य है।"),
    ("कथन (A): गौरैया के आकार की मिट्टी की खोखली सीटियाँ आवासीय क्षेत्रों से प्राप्त हुई हैं।\nकारण (R): गौरैया घाटी में पाई जाने वाली एक आम चिड़िया थी और बच्चे इन सीटियों का खेलने में उपयोग करते थे।", 1, "A और R दोनों सत्य हैं लेकिन R यह व्याख्या नहीं करता कि वे गौरैया के आकार की ही क्यों थीं।"),
    ("कथन (A): पुरोहित-राजा की मूर्ति को ठोस कांसे से ढाला गया था।\nकारण (R): पुरोहित-राजा की मूर्ति को सेलखड़ी पत्थर से तराश कर भट्टी में पकाया गया था।", 3, "A असत्य है क्योंकि यह सेलखड़ी से बनी थी, कांसे से नहीं। R सत्य है।"),
    ("कथन (A): लाल अकीक (carnelian) मेसोपोटामिया को निर्यात किया जाने वाला एक अत्यंत मूल्यवान रत्न था।\nकारण (R): अकीक के मनकों में लोथल में विशेष सूक्ष्म-ड्रिल से छेद किए जाते थे और उन्हें घिसकर चमकाया जाता था।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।")
]:
    s3_mastery_hin.append({"type": "Assertion-Reason", "q": q, "opts": hin_ar_opts, "ans": ans, "sol": sol})

# Statement-Based (5)
for q, ans, sol in [
    ("Consider the following statements regarding the lost-wax casting technique:\n1. The process involves creating a wax model, coating it with clay, melting the wax out, and pouring molten bronze inside.\n2. The bronze Dancing Girl is the earliest solid bronze casting discovered in the world.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct and define the lost-wax process and the significance of the Dancing Girl."),
    ("Consider the following statements regarding stone sculptures:\n1. The Priest-King has elongated eyes and trefoil shawl motifs.\n2. The red sandstone torso from Harappa features limb sockets.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct, describing the key features of the two iconic stone sculptures."),
    ("Consider the following statements regarding bead making:\n1. Carnelian was imported as a finished bead directly from Mesopotamia.\n2. Chanhudaro and Lothal had large workshops to drill, bake, and polish beads.\nWhich of the statements given above is/are correct?", 1, "Statement 2 is correct. Statement 1 is incorrect: carnelian was imported as raw nodules and worked locally before export."),
    ("Consider the following statements regarding toys:\n1. Terracotta toy carts were cheap replicas of wooden transportation carts.\n2. Whistles shaped like birds were made of gold and silver for elite children.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: bird whistles were made of cheap, hollow terracotta."),
    ("Consider the following statements regarding amusements:\n1. Board games resembling chess used clay game checkers.\n2. Cubical dice were carved primarily from steatite and decorated with lapis lazuli inlays.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: dice were made of simple chert or terracotta, not decorated with lapis.")
]:
    s3_mastery_eng.append({"type": "Statement-Based", "q": q, "opts": mcq_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("लुप्त-मोम (lost-wax) कांस्य ढलाई तकनीक के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इस प्रक्रिया में पहले मोम का मॉडल बनाकर उसे मिट्टी से लपेटा जाता था, फिर मोम पिघलाकर निकाल दिया जाता था और खाली जगह में पिघला कांसा भरा जाता था।\n2. कांस्य की नर्तकी विश्व में खोजी गई ठोस कांस्य ढलाई का सबसे प्राचीन उदाहरण है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 2, "दोनों कथन सही हैं, जो लुप्त-मोम ढलाई की विधि और नर्तकी के ऐतिहासिक महत्व को स्पष्ट करते हैं।"),
    ("पाषाण मूर्तियों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. पुरोहित-राजा की मूर्ति में आधी खुली आँखें और तिपतिया सज्जा वाला शॉल दर्शाया गया है।\n2. हड़प्पा से प्राप्त लाल बलुआ पत्थर के धड़ में हाथ-पैर लगाने के सॉकेट छेद बने हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 2, "दोनों कथन सही हैं और दोनों प्रसिद्ध पाषाण मूर्तियों के लक्षणों का सही विवरण देते हैं।"),
    ("मनका निर्माण के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. अकीक (carnelian) को तैयार मनके के रूप में सीधे मेसोपोटामिया से आयात किया जाता था।\n2. चन्हुदड़ो और लोथल में कच्चे पत्थर को काटने, पकाने और चमकाने की बड़ी कार्यशालाएँ थीं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 1, "कथन 2 सही है। कथन 1 गलत है क्योंकि अकीक को कच्चे पत्थर के रूप में मंगाकर यहीं मनके तैयार किए जाते थे।"),
    ("खिलौनों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मिट्टी की खिलौना गाड़ियाँ परिवहन के लिए प्रयुक्त होने वाली वास्तविक लकड़ी की गाड़ियों की सस्ती नकल थीं।\n2. पक्षियों के आकार की सीटियाँ धनी वर्ग के बच्चों के लिए सोने और चांदी से बनाई जाती थीं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि सीटी खिलौने साधारण खोखली मिट्टी से बनते थे।"),
    ("मनोरंजन के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. शतरंज जैसे बोर्ड गेम में खेलने के लिए मिट्टी की गोटियों का उपयोग किया जाता था।\n2. घनाकार पासे मुख्य रूप से सेलखड़ी से बनाए जाते थे और उन पर लाजवर्त (lapis) मढ़ा जाता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि पासे चर्ट या मिट्टी के होते थे, लाजवर्त का मढ़ाव नहीं होता था।")
]:
    s3_mastery_hin.append({"type": "Statement-Based", "q": q, "opts": hin_mcq_opts, "ans": ans, "sol": sol})

# Why (3)
for q, sol in [
    ("Why did the Harappan metallurgists utilize the lost-wax method for bronze statues?", "Because lost-wax casting allows for extremely detailed fluid curves and fine features (like the Dancing Girl's fingers and bangles) that are impossible with simple sand molds."),
    ("Why did the sculptor of the red sandstone torso carve sockets in the neck and shoulders?", "To enable movable stone head and arms to be attached, creating a kinetic sculpture that could be posed in different positions."),
    ("Why was steatite selected as the primary medium for carving seals and the Priest-King?", "Steatite (soapstone) is very soft when freshly quarried and easy to engrave with fine chert tools, but when baked at high temperatures, it undergoes a phase change and hardens into a durable stone.")
]:
    s3_mastery_eng.append({"type": "Why", "q": q, "sol": sol})

for q, sol in [
    ("हड़प्पा के धातु शिल्पियों ने कांस्य मूर्तियों के लिए लुप्त-मोम (lost-wax) विधि का उपयोग क्यों किया?", "क्योंकि लुप्त-मोम विधि से मूर्ति में बारीक विवरण (जैसे नर्तकी के हाथ की उँगलियाँ और चूड़ियाँ) को अत्यंत सटीकता से उभारा जा सकता था, जो साधारण रेत के सांचे से संभव नहीं था।"),
    ("लाल बलुआ पत्थर के धड़ के मूर्तिकार ने गर्दन और कंधों पर सॉकेट छेद क्यों बनाए थे?", "ताकि उसमें अलग से तराशे गए सिर और हाथ जोड़े जा सकें, जिससे एक गतिमान (kinetic) मूर्ति तैयार हो सके जिसे विभिन्न मुद्राओं में बदला जा सके।"),
    ("मुहरों और पुरोहित-राजा की मूर्ति के लिए सेलखड़ी (steatite) को ही क्यों चुना गया था?", "सेलखड़ी खदान से निकालते समय बहुत नरम होती है जिसे चर्ट के बारीक औजारों से उकेरा जा सकता था, लेकिन भट्टी में गर्म करने पर यह अत्यधिक कठोर और टिकाऊ बन जाती थी।")
]:
    s3_mastery_hin.append({"type": "Why", "q": q, "sol": sol})

# How (3)
for q, sol in [
    ("How was the lost-wax (cire perdue) process carried out by Harappan craftsmen?", "They sculpted a wax model, coated it in clay, baked it to melt the wax out via a small hole, poured molten bronze inside the hollow space, and broke the outer clay shell once cooled."),
    ("How did toys reflect the daily technological items of the Harappans?", "Terracotta toys replicated transport technology (solid-wheel bullock carts), agricultural technology (clay models of plows), and local fauna (humped bulls and monkeys)."),
    ("How was carnelian processed to turn into export-grade beads at Lothal?", "Raw greyish-yellow chalcedony nodules were baked in pottery kilns to turn them deep red, chipped and ground into cylinders, drilled with chert bits, and polished to a luster.")
]:
    s3_mastery_eng.append({"type": "How", "q": q, "sol": sol})

for q, sol in [
    ("हड़प्पा के कारीगरों द्वारा लुप्त-मोम (cire perdue) ढलाई की प्रक्रिया कैसे की जाती थी?", "पहले मोम की मूर्ति बनाकर उस पर मिट्टी का लेप लगाते थे, फिर उसे सुखाकर भट्टी में गर्म करते थे ताकि मोम पिघलकर छोटे छेद से निकल जाए, फिर खाली स्थान में पिघला कांसा भरकर ठंडा होने पर मिट्टी को तोड़ दिया जाता था।"),
    ("खिलौने हड़प्पा वासियों के दैनिक तकनीकी साधनों को किस प्रकार प्रतिबिंबित करते थे?", "मिट्टी के खिलौने उनके परिवहन तंत्र (ठोस पहियों वाली बैलगाड़ी), कृषि तकनीक (मिट्टी के हल) और स्थानीय जीव-जंतुओं (कूबड़ वाले सांड और बंदरों) के लघु रूप थे।"),
    ("लोथल में कच्चे अकीक पत्थर को निर्यात-योग्य मोतियों में कैसे बदला जाता था?", "कच्चे पीले-धूसर पत्थर को भट्टी में गर्म करके गहरे लाल रंग में बदला जाता था, फिर उसे तोड़कर बेलनाकार घिसा जाता था, चर्ट के बारीक औजारों से छेद करके चमकाया जाता था।")
]:
    s3_mastery_hin.append({"type": "How", "q": q, "sol": sol})

# Case Study (3)
for q, sol in [
    ("Case Study: The Bronze Dancing Girl's Metallurgy", "Found at Mohenjo-daro, this 10cm figure showcases mastery of bronze metallurgy. The alloy of copper and tin was melted at 1085°C. Cast solid using lost-wax, she has elongated arms covered in bangles, a unique pose demonstrating high artistic confidence in Bronze Age art."),
    ("Case Study: Chanhudaro Bead Factory Finds", "Archaeologists excavated a bead factory at Chanhudaro containing raw carnelian blocks, copper drills, polishing stones, and finished cylindrical beads. This shows bead making was a factory-scale export industry coordinating with Mesopotamian trade demands."),
    ("Case Study: Node-head nodding bull toy", "Excavations yielded terracotta bull figurines with hollow necks and separate heads. A string running through the hump to the chin let children make the head nod. This reflects high ingenuity in kinetic toy design for common household children.")
]:
    s3_mastery_eng.append({"type": "Case Study", "q": q, "sol": sol})

for q, sol in [
    ("केस स्टडी: कांस्य नर्तकी की धातुकर्म इंजीनियरिंग", "मोहनजोदड़ो से प्राप्त 10 सेमी की यह मूर्ति कांसे की ढलाई पर उनके प्रभुत्व को दर्शाती है। तांबे और टिन के मिश्र धातु को 1085 डिग्री सेल्सियस पर पिघलाया गया था। लुप्त-मोम विधि से ठोस रूप में ढाली गई यह मूर्ति चूड़ियों से ढकी लंबी बाहों के साथ त्रिभंग मुद्रा में है, जो बेजोड़ आत्मविश्वास को दर्शाती है।"),
    ("केस स्टडी: चन्हुदड़ो मनका कारखाने की खोजें", "चन्हुदड़ो में मनका बनाने का एक बड़ा कारखाना मिला है जिसमें अकीक के बड़े पत्थर, तांबे की ड्रिल, पॉलिश करने वाले सिल और तैयार बेलनाकार मनके मिले हैं। यह दर्शाता है कि मनका निर्माण कारखाने के स्तर पर चलने वाला एक बड़ा निर्यात उद्योग था।"),
    ("केस स्टडी: हिलते सिर वाला मिट्टी का बैल", "उत्खनन में खोखली गर्दन और अलग सिर वाले मिट्टी के सांड मिले हैं। कूबड़ से होकर ठोड़ी तक जाने वाले धागे को खींचने पर सांड का सिर हिलता था। यह आम घरों के बच्चों के लिए खिलौना बनाने की उन्नत गतिज कला (kinetic design) को दर्शाता है।")
]:
    s3_mastery_hin.append({"type": "Case Study", "q": q, "sol": sol})

# Teach Concept (3)
for q, sol in [
    ("Teach Concept: Solid Lost-Wax (Cire Perdue) Casting Method", "Describe the step-by-step casting process. Create a detailed wax sculpture. Wrap it tightly in porous clay, leaving a small hole at the bottom. Heat the mold so the wax melts and drains out. Pour molten bronze (copper + tin) into the hollow space. Let cool, then crack open the clay shroud to reveal a solid metal masterpiece."),
    ("Teach Concept: Sockets and Kinetic Joints in Stone Carving", "Explain the concept of interlocking sculpture components. By carving circular hollow sockets in the neck and shoulders of the red sandstone torso, the artist allowed separate stone arms and heads to be inserted. This created a modular, posable artwork that represents an early step in kinetic joint engineering."),
    ("Teach Concept: The Chemistry of Steatite Baking", "Explain how soapstone undergoes a chemical transformation. Raw steatite is a talc-rich metamorphic rock that is extremely soft (1 on Mohs scale), easily carved with bronze tools. Baking it in a kiln at over 900°C changes its mineral structure, transforming talc into enstatite, hardening it to a 5-6 Mohs rating, ensuring durability.")
]:
    s3_mastery_eng.append({"type": "Teach Concept", "q": q, "sol": sol})

for q, sol in [
    ("अवधारणा समझाएं (Teach Concept): ठोस लुप्त-मोम (lost-wax) ढलाई की विधि", "इस ढलाई की चरणबद्ध प्रक्रिया बताएं। पहले मोम की एक विस्तृत मूर्ति बनाएं। उसे मिट्टी से लपेट दें और नीचे एक छोटा छेद छोड़ दें। सांचे को गर्म करें ताकि मोम पिघलकर बाहर निकल जाए। फिर उस खाली स्थान में पिघला कांसा भरें। ठंडा होने पर बाहरी मिट्टी के आवरण को तोड़कर धातु की ठोस मूर्ति प्राप्त कर लें।"),
    ("अवधारणा समझाएं (Teach Concept): पाषाण कला में गतिज सॉकेट जोड़", "मूर्तिकला के घटकों को आपस में जोड़ने की विधि समझाएं। लाल बलुआ पत्थर के धड़ के गर्दन और कंधों पर गोलाकार सॉकेट (छेद) बनाकर, मूर्तिकार ने अलग से बने सिर और हाथों को इसमें जोड़ने की व्यवस्था की। यह एक परिवर्तनीय, गतिशील कला का प्रारंभिक उदाहरण है।"),
    ("अवधारणा समझाएं (Teach Concept): सेलखड़ी को पकाने की रसायन शास्त्र", "समझाएं कि साबुन-पत्थर कैसे रासायनिक रूप से बदलता था। कच्ची सेलखड़ी बहुत नरम रूपांतरित चट्टान है (मोह स्केल पर 1), जिसे कांसे के औजारों से आसानी से तराशा जा सकता था। भट्टी में 900 डिग्री सेल्सियस से ऊपर पकाने पर इसका खनिज ढांचा बदल जाता है और यह अत्यधिक कठोर व चमकीला पत्थर बन जाता है।")
]:
    s3_mastery_hin.append({"type": "Teach Concept", "q": q, "sol": sol})


# Load content files and inject
with open(ENG_PATH, "r", encoding="utf-8") as f:
    eng_data = json.load(f)

with open(HIN_PATH, "r", encoding="utf-8") as f:
    hin_data = json.load(f)

# Inject Section 1
eng_data["deepDive"]["sections"][0]["masteryZone"] = s1_mastery_eng
hin_data["deepDive"]["sections"][0]["masteryZone"] = s1_mastery_hin

# Inject Section 2
eng_data["deepDive"]["sections"][1]["masteryZone"] = s2_mastery_eng
hin_data["deepDive"]["sections"][1]["masteryZone"] = s2_mastery_hin

# Inject Section 3
eng_data["deepDive"]["sections"][2]["masteryZone"] = s3_mastery_eng
hin_data["deepDive"]["sections"][2]["masteryZone"] = s3_mastery_hin

# Save files
with open(ENG_PATH, "w", encoding="utf-8") as f:
    json.dump(eng_data, f, ensure_ascii=False, indent=2)

with open(HIN_PATH, "w", encoding="utf-8") as f:
    json.dump(hin_data, f, ensure_ascii=False, indent=2)

print("Socio-Cultural Mastery Zone questions injected successfully!")
