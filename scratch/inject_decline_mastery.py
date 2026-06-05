import json
import os

ENG_PATH = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\HarappanIndus-Valley-Civilisation\Decline-of-Harappan-Civilisation\content.json"
HIN_PATH = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\HarappanIndus-Valley-Civilisation\Decline-of-Harappan-Civilisation\hi\content.json"

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
# SECTION 1: CLIMATIC, ECOLOGICAL, AND ENVIRONMENTAL THEORIES
# =========================================================================
s1_mastery_eng = []
s1_mastery_hin = []

# MCQ (5)
for q, opts, ans, sol in [
    ("Who proposed the theory of Ecological Imbalance for the decline of the Harappan Civilisation?", ["Walter Fairservis", "Gurdip Singh", "Mortimer Wheeler", "John Marshall"], 0, "Walter Fairservis proposed the Ecological Imbalance theory, stating that human over-exploitation led to resources depletion."),
    ("Gurdip Singh linked the decline of the Harappan Civilisation to aridity (climate drying) based on his study of pollen from lakes in which state?", ["Gujarat", "Rajasthan", "Punjab", "Haryana"], 1, "Gurdip Singh conducted pollen analysis of salt lakes in Rajasthan (Sambhar, Didwana, Lunkaransar)."),
    ("According to the environmental desiccation theory, which river system's drying caused the abandonment of Kalibangan?", ["Indus", "Ravi", "Ghaggar-Hakra", "Luni"], 2, "The drying up of the Ghaggar-Hakra (Saraswati) river system caused Kalibangan's abandonment."),
    ("Walter Fairservis calculated that the massive requirements of firewood in Harappan cities was primarily for:", ["Cooking food", "Baking mud bricks", "Cremating the dead", "Smelting iron"], 1, "Fuel was extensively needed for baking millions of clay bricks used in municipal structures."),
    ("Tectonic changes diverted which glacial river away from the Ghaggar-Hakra, contributing to its drying up?", ["Indus", "Sutlej", "Chenab", "Jhelum"], 1, "Tectonic uplifts diverted the Sutlej west to join the Indus, and the Yamuna east to the Ganga, depriving the Ghaggar of water.")
]:
    s1_mastery_eng.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("हड़प्पा सभ्यता के पतन के लिए 'पारिस्थितिक असंतुलन' का सिद्धांत किसने दिया था?", ["वाल्टर फेयरसर्विस", "गुरदीप सिंह", "मोंटीमर व्हीलर", "जॉन मार्शल"], 0, "वाल्टर फेयरसर्विस ने पारिस्थितिक असंतुलन का सिद्धांत दिया था।"),
    ("गुरदीप सिंह ने किस राज्य की झीलों के पराग (pollen) विश्लेषण के आधार पर पतन को शुष्कता (सूखे) से जोड़ा?", ["गुजरात", "राजस्थान", "पंजाब", "हरियाणा"], 1, "गुरदीप सिंह ने राजस्थान की सांभर, डीडवाना और लूणकरणसर झीलों का अध्ययन किया था।"),
    ("पर्यावरणीय शुष्कता सिद्धांत के अनुसार, किस नदी प्रणाली के सूखने से कालीबंगा का परित्याग हुआ?", ["सिंधु", "रावी", "घग्गर-हकरा", "लूनी"], 2, "घग्गर-हकरा (सरस्वती) नदी मार्ग के सूखने से कालीबंगा का विनाश हुआ।"),
    ("वाल्टर फेयरसर्विस के अनुसार, हड़प्पा के शहरों में जलाऊ लकड़ी की अत्यधिक मांग मुख्य रूप से किस काम के लिए थी?", ["भोजन पकाने", "ईंटें पकाने", "दाह संस्कार", "लोहा पिघलाने"], 1, "लाखों मिट्टी की ईंटों को पकाने के लिए बड़े पैमाने पर लकड़ी की आवश्यकता थी।"),
    ("विवर्तनिक हलचलों के कारण किस हिमनदी (glacial river) को घग्गर-हकरा से दूर विस्थापित कर दिया गया?", ["सिंधु", "सतलुज", "चिनाब", "झेलम"], 1, "सतलुज नदी के मार्ग बदलकर सिंधु में मिलने और यमुना के गंगा में मिलने से घग्गर सूख गई।")
]:
    s1_mastery_hin.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# Multiple Correct MCQ (5)
for q, opts, ans, sol in [
    ("Which of the following factors are key components of Fairservis's Ecological Imbalance Theory? (Select all that apply)", ["Over-grazing by large cattle herds", "Deforestation due to brick baking", "Exhaustion of soil fertility", "Introduction of iron tools"], [0, 1, 2], "Over-grazing, deforestation for bricks, and soil exhaustion are components. Iron was unknown."),
    ("Select the Rajasthan salt lakes studied by Gurdip Singh for pollen analysis: (Select all that apply)", ["Sambhar", "Didwana", "Lunkaransar", "Chilika"], [0, 1, 2], "Singh studied Sambhar, Didwana, and Lunkaransar lakes. Chilika is in Odisha."),
    ("Which of the following changes are associated with the drying of the Ghaggar-Hakra river? (Select all that apply)", ["Sutlej shifting to join the Indus", "Yamuna shifting to join the Ganga", "Decline of agricultural yields in Cholistan", "Flooding of Mohenjo-daro"], [0, 1, 2], "Drying was caused by Sutlej and Yamuna shifts, ruining Cholistan agriculture. Mohenjo-daro floods were on the Indus, not Ghaggar."),
    ("Select the indicators of environmental stress during the Late Harappan phase: (Select all that apply)", ["Loss of urban planning and drainage", "Abandonment of large city centers", "Migration towards Gujarat and UP", "Introduction of canal networks"], [0, 1, 2], "Environmental stress is indicated by de-urbanisation, city abandonment, and migrations. Canal networks did not expand."),
    ("Which of the following activities contributed to the depletion of Harappan forest cover? (Select all that apply)", ["Firing millions of terracotta pots", "Baking bricks for housing and drains", "Clearing land for agriculture", "Building large wooden ships"], [0, 1, 2], "Pottery firing, brick baking, and agricultural clearing caused deforestation. Ship building was minor.")
]:
    s1_mastery_eng.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("फेयरसर्विस के पारिस्थितिक असंतुलन सिद्धांत के मुख्य घटक कौन से हैं? (सभी सही विकल्प चुनें)", ["पशुओं द्वारा अत्यधिक चराई", "ईंटें पकाने के लिए वनों की कटाई", "मिट्टी की उपजाऊ शक्ति का ह्रास", "लोहे के उपकरणों का आगमन"], [0, 1, 2], "पशु चराई, वनों की कटाई और मिट्टी का ह्रास इसके मुख्य घटक हैं। लोहे का ज्ञान नहीं था।"),
    ("पराग विश्लेषण के लिए गुरदीप सिंह द्वारा अध्ययन की गई राजस्थान की झीलें कौन सी हैं? (सभी सही विकल्प चुनें)", ["सांभर", "डीडवाना", "लूणकरणसर", "चिल्का"], [0, 1, 2], "उन्होंने सांभर, डीडवाना और लूणकरणसर का अध्ययन किया। चिल्का ओडिशा में है।"),
    ("घग्गर-हकरा नदी के सूखने से जुड़े परिवर्तन कौन से हैं? (सभी सही विकल्प चुनें)", ["सतलुज का सिंधु नदी में मिल जाना", "यमुना का गंगा नदी में मिल जाना", "चोलिस्तान क्षेत्र में कृषि उपज का गिरना", "मोहनजोदड़ो में बाढ़ आना"], [0, 1, 2], "सतलुज-यमुना का मार्ग बदलना और चोलिस्तान में सूखा इसके कारण थे। मोहनजोदड़ो की बाढ़ सिंधु से संबंधित थी।"),
    ("उत्तर हड़प्पा काल में पर्यावरणीय तनाव के पुरातात्विक सूचक कौन से हैं? (सभी सही विकल्प चुनें)", ["नगर नियोजन और जल निकासी का लोप", "बड़े शहरी केंद्रों का परित्याग", "गुजरात और उत्तर प्रदेश की ओर पलायन", "नहरों के नेटवर्क का विस्तार"], [0, 1, 2], "नियोजन का अंत, शहरों का परित्याग और पलायन पर्यावरणीय तनाव को दर्शाते हैं।"),
    ("हड़प्पा काल में जंगलों के विनाश में किन गतिविधियों ने योगदान दिया? (सभी सही विकल्प चुनें)", ["लाखों मिट्टी के बर्तनों को पकाना", "मकानों और नालियों के लिए ईंटें पकाना", "खेती के लिए भूमि साफ़ करना", "लकड़ी के बड़े जहाज बनाना"], [0, 1, 2], "बर्तन पकाना, ईंटें पकाना और कृषि विस्तार इसके कारण थे। जहाज निर्माण बहुत सीमित था।")
]:
    s1_mastery_hin.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# True/False (8)
for q, ans, sol in [
    ("Walter Fairservis proposed the Ecological Imbalance Theory of Harappan decline.", True, "Fairservis argued that the population outstripped environmental carrying capacity."),
    ("Gurdip Singh studied pollen profiles from lakes in Madhya Pradesh.", False, "He studied salt lakes in Rajasthan (Sambhar, Didwana, Lunkaransar)."),
    ("The Ghaggar-Hakra river system was fed by glacial waters of the Sutlej and Yamuna rivers.", True, "Tectonic uplifts diverted these rivers, leaving Ghaggar dry."),
    ("According to Gurdip Singh, aridity and drought began around 1800 BCE.", True, "His pollen analysis indicates a major drop in rainfall around 1800 BCE."),
    ("Ecological depletion resulted in a sudden destruction of all cities within a single decade.", False, "It was a slow, gradual process of ruralisation spanning centuries."),
    ("Late Harappan cultures in Punjab show a shift towards smaller, agricultural settlements.", True, "The post-urban phase is characterized by rural agricultural villages."),
    ("The Harappans successfully developed iron axes to clear forests, leading to soil erosion.", False, "The Harappans were in the Bronze Age and did not possess iron tools."),
    ("Kalibangan was abandoned due to the drying up of the Ghaggar-Hakra river bed.", True, "Kalibangan relied entirely on this system and was abandoned when it dried.")
]:
    s1_mastery_eng.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("वाल्टर फेयरसर्विस ने हड़प्पा पतन के लिए पारिस्थितिक असंतुलन का सिद्धांत दिया था।", True, "फेयरसर्विस ने जनसंख्या और पर्यावरण के असंतुलन का तर्क दिया था।"),
    ("गुरदीप सिंह ने मध्य प्रदेश की झीलों के पराग कणों का अध्ययन किया था।", False, "उन्होंने राजस्थान की लवणीय झीलों का अध्ययन किया था।"),
    ("घग्गर-हकरा नदी प्रणाली को सतलुज और यमुना नदियों के हिमनद जल से पानी मिलता था।", True, "भू-गर्भीय हलचलों ने इन नदियों का मार्ग बदल दिया, जिससे घग्गर सूख गई।"),
    ("गुरदीप सिंह के अनुसार, शुष्कता और सूखा लगभग 1800 ईसा पूर्व में शुरू हुआ था।", True, "पराग विश्लेषण 1800 ई.पू. के आसपास शुष्क जलवायु की शुरुआत दर्शाता है।"),
    ("पारिस्थितिक क्षरण के कारण केवल एक दशक के भीतर सभी शहर अचानक नष्ट हो गए थे।", False, "यह एक अत्यंत धीमी और क्रमिक प्रक्रिया थी जो सदियों में पूरी हुई।"),
    ("पंजाब की उत्तर हड़प्पा संस्कृतियों में छोटे और कृषि प्रधान गाँवों की ओर झुकाव दिखता है।", True, "शहरी पतन के बाद लोग ग्रामीण कृषि संस्कृतियों में रहने लगे।"),
    ("हड़प्पा वासियों ने जंगलों को साफ करने के लिए लोहे की कुल्हाड़ियों का विकास किया था।", False, "हड़प्पा वासी कांस्य युगीन थे; लोहे का ज्ञान उन्हें नहीं था।"),
    ("घग्गर-हकरा नदी मार्ग के सूखने के कारण ही कालीबंगा का परित्याग किया गया था।", True, "कालीबंगा इसी नदी तट पर था और पानी सूखने पर उजाड़ हो गया।")
]:
    s1_mastery_hin.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

# Fill in the Blank (8)
for q, ans, sol in [
    ("The Ecological Imbalance Theory of Harappan decline was proposed by ________.", "Walter Fairservis", "Fairservis argued environmental depletion caused the collapse."),
    ("Gurdip Singh conducted pollen analysis on Rajasthan salt lakes to reconstruct ancient ________.", "rainfall", "He reconstructed rainfall patterns showing a drop around 1800 BCE."),
    ("Tectonic uplifts diverted the river ________ westwards to join the Indus system.", "Sutlej", "Sutlej was diverted, cutting off the Ghaggar-Hakra."),
    ("The drying up of the Ghaggar-Hakra river led to the abandonment of the town ________.", "Kalibangan", "Kalibangan dried up and was abandoned (also Banawali)."),
    ("Millions of wood logs were consumed to bake clay ________ for city construction.", "bricks", "Baked bricks required massive firewood, driving deforestation."),
    ("Pollen analysis showed that a phase of climate ________ started around 1800 BCE.", "aridity", "Dry aridity replaced the wet monsoon phase."),
    ("The Ghaggar-Hakra river system is identified with the Rigvedic river ________.", "Saraswati", "Saraswati is modern Ghaggar-Hakra."),
    ("Over-grazing by large herds of ________ depleted grasslands in the Indus valley.", "cattle", "Cattle over-grazing stripped the protective grass layer.")
]:
    s1_mastery_eng.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("हड़प्पा पतन का पारिस्थितिक असंतुलन सिद्धांत ________ द्वारा दिया गया था।", "वाल्टर फेयरसर्विस", "फेयरसर्विस ने पर्यावरणीय दोहन को जिम्मेदार ठहराया।"),
    ("गुरदीप सिंह ने प्राचीन ________ का पुनर्निर्माण करने के लिए राजस्थान की झीलों का अध्ययन किया।", "वर्षा", "उन्होंने वर्षा के चक्र में कमी (शुष्कता) का विश्लेषण किया।"),
    ("विवर्तनिक हलचलों के कारण ________ नदी सिंधु नदी प्रणाली में मिल गई।", "सतलुज", "सतलुज का मार्ग बदला और वह घग्गर से अलग हो गई।"),
    ("घग्गर-हकरा नदी के सूखने से राजस्थान के प्रसिद्ध स्थल ________ का परित्याग हुआ।", "कालीबंगा", "कालीबंगा नदी सूखने पर वीरान हो गया।"),
    ("मकानों के निर्माण हेतु मिट्टी की ________ पकाने के लिए भारी मात्रा में लकड़ी जलाई गई।", "ईंटें", "पकी ईंटों के निर्माण ने वनों के विनाश को तीव्र किया।"),
    ("पराग विश्लेषण से पता चला कि 1800 ई.पू. के आसपास जलवायु ________ का चरण शुरू हुआ।", "शुष्कता", "सूखा और शुष्कता का काल शुरू हुआ था।"),
    ("घग्गर-हकरा नदी प्रणाली को प्राचीन वैदिक नदी ________ के रूप में पहचाना जाता है।", "सरस्वती", "सरस्वती ही घग्गर-हकरा का पुराना नाम है।"),
    ("पशुओं में मुख्य रूप से ________ की चराई ने घास के मैदानों को नष्ट कर दिया।", "गायों", "गाय-भैंसों (मवेशियों) की चराई से घास की परतें नष्ट हो गईं।")
]:
    s1_mastery_hin.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

# Match the Following (3)
s1_matches_eng = [
    {"q": "Match the environmental decline theory with its primary proponent:",
     "pairs": ["Ecological Imbalance Theory - Walter Fairservis", "Climate Aridity Theory - Gurdip Singh", "Drying of Ghaggar-Hakra - Aurel Stein and A.N. Ghosh", "Decline of Mesopotamian trade - Shereen Ratnagar"],
     "sol": "Fairservis proposed Ecological Imbalance; Singh studied aridity; Stein/Ghosh identified Ghaggar desiccation; Ratnagar proposed trade collapse."},
    {"q": "Match the archaeological site with the environmental cause of its decline:",
     "pairs": ["Kalibangan - Drying of the Ghaggar-Hakra river", "Lothal - Siltation of the port basin", "Mohenjo-daro - Repeated flooding by the Indus", "Rakhigarhi - Gradual lowering of groundwater tables"],
     "sol": "Kalibangan suffered from Ghaggar desiccation; Lothal ports silted up; Mohenjo-daro flooded; Rakhigarhi had dropping water tables."},
    {"q": "Match the environmental indicator with its corresponding research source:",
     "pairs": ["Pollen analysis - Rajasthan salt lakes (Sambhar)", "Clay bricks - Deforestation for fuel wood", "Late Harappan rural sites - Population migration eastwards", "Sutlej diversion - Tectonic uplift in Himalayas"],
     "sol": "Pollen was studied in Rajasthan lakes; clay bricks indicated deforestation; rural sites indicated migrations; Sutlej diversion was tectonic."}
]
s1_mastery_eng.extend([make_match_question(m) for m in s1_matches_eng])

s1_matches_hin = [
    {"q": "पर्यावरणीय पतन के सिद्धांतों को उनके प्रतिपादक विद्वानों से सुमेलित करें:",
     "pairs": ["पारिस्थितिक असंतुलन सिद्धांत - वाल्टर फेयरसर्विस", "जलवायु शुष्कता सिद्धांत - गुरदीप सिंह", "घग्गर-हकरा का सूखना - ऑरेल स्टीन और ए.एन. घोष", "मेसोपोटामियाई व्यापार पतन - शीरीन रत्नागर"],
     "sol": "फेयरसर्विस ने पारिस्थितिक असंतुलन; सिंह ने शुष्कता; स्टीन/घोष ने घग्गर का सूखना; रत्नागर ने व्यापार पतन सिद्धांत दिया।"},
    {"q": "पुरातात्विक स्थल को उनके पतन के पर्यावरणीय कारणों से सुमेलित करें:",
     "pairs": ["कालीबंगा - घग्गर-हकरा नदी का सूखना", "लोथल - बंदरगाह गोदी में गाद जमा होना", "मोहनजोदड़ो - सिंधु नदी द्वारा बार-बार जलभराव", "राखीगढ़ी - भूजल स्तर में क्रमिक गिरावट"],
     "sol": "कालीबंगा घग्गर के सूखने से; लोथल गोदी की गाद से; मोहनजोदड़ो सिंधु की बाढ़ से और राखीगढ़ी जल स्तर गिरने से वीरान हुए।"},
    {"q": "पर्यावरणीय संकेतक को उसके संबंधित शोध स्रोत से सुमेलित करें:",
     "pairs": ["पराग विश्लेषण - राजस्थान की खारे पानी की झीलें", "पकी ईंटें - ईंधन के लिए वनों की अंधाधुंध कटाई", "उत्तर हड़प्पा ग्रामीण स्थल - पूर्व की ओर जनसंख्या का पलायन", "सतलुज का मार्ग बदलना - हिमालय क्षेत्र में विवर्तनिक हलचल"],
     "sol": "पराग विश्लेषण झीलों से; ईंट निर्माण वनों की कटाई से; ग्रामीण बस्तियाँ पलायन से और सतलुज का विस्थापन विवर्तनिक हलचल से जुड़ा है।"}
]
s1_mastery_hin.extend([make_match_question(m) for m in s1_matches_hin])

# One-Liner (8)
for q, sol in [
    ("What was the core argument of Walter Fairservis's Ecological Imbalance theory?", "The growing population consumed resources faster than the semi-arid environment could regenerate them."),
    ("Which lakes were selected by Gurdip Singh for pollen analysis?", "Sambhar, Didwana, and Lunkaransar salt lakes in Rajasthan."),
    ("What did the presence of cereal pollen in Rajasthan lakes indicate before 1800 BCE?", "It indicated a wet climate with abundant rainfall supporting agriculture."),
    ("How did tectonic activity affect the Ghaggar-Hakra river system?", "It diverted its glacial tributaries, the Sutlej and Yamuna, leaving the main bed to dry up."),
    ("Why did the production of baked bricks contribute to environmental decline?", "Baking clay bricks required immense amounts of timber, leading to widespread deforestation."),
    ("Where did the residents of abandoned desert sites migrate to?", "They migrated eastwards towards Punjab, western Uttar Pradesh, and southwards to Gujarat."),
    ("What mathematical ratio did Harappans abandon when municipal planning collapsed?", "The standardized 4:2:1 ratio for mud and baked bricks."),
    ("What does the lack of forest-loving animal depictions on Late Harappan seals represent?", "It reflects the loss of forest habitat and transition to a drier climate.")
]:
    s1_mastery_eng.append({"type": "One-Liner", "q": q, "sol": sol})

for q, sol in [
    ("वाल्टर फेयरसर्विस के पारिस्थितिक असंतुलन सिद्धांत का मूल तर्क क्या था?", "बढ़ती आबादी ने पर्यावरण की पुनः उत्पन्न होने की क्षमता से अधिक संसाधनों का उपभोग किया।"),
    ("गुरदीप सिंह ने पराग विश्लेषण के लिए किन झीलों का चयन किया था?", "राजस्थान की सांभर, डीडवाना और लूणकरणसर जैसी लवण झीलों का।"),
    ("1800 ई.पू. से पहले राजस्थान की झीलों में अनाज के परागकणों का मिलना क्या दर्शाता था?", "यह कृषि का समर्थन करने वाली अच्छी वर्षा और आर्द्र जलवायु को दर्शाता था।"),
    ("विवर्तनिक हलचलों ने घग्गर-हकरा नदी प्रणाली को कैसे प्रभावित किया?", "विवर्तनिक हलचलों ने इसकी सहायक नदियों सतलुज और यमुना को दूर धकेल दिया, जिससे घग्गर सूख गई।"),
    ("पकी ईंटों के निर्माण ने पर्यावरणीय पतन में कैसे योगदान दिया?", "ईंटों को पकाने के लिए भारी मात्रा में ईंधन की आवश्यकता थी, जिससे वनों का अंधाधुंध विनाश हुआ।"),
    ("मरुस्थलीय क्षेत्रों के वीरान होने पर वहां की आबादी कहाँ चली गई?", "वह पूर्व में पंजाब, पश्चिमी उत्तर प्रदेश और दक्षिण में गुजरात के ग्रामीण इलाकों में पलायन कर गई।"),
    ("नगरपालिका नियोजन के पतन पर हड़प्पा वासियों ने किस ईंट अनुपात का परित्याग कर दिया?", "मानक 4:2:1 अनुपात वाली ईंटों का परित्याग कर दिया गया।"),
    ("उत्तर हड़प्पा काल की मुहरों पर वन में रहने वाले जानवरों के चित्रों का न मिलना क्या दर्शाता है?", "यह वनों के विनाश और शुष्क जलवायु की शुरुआत को दर्शाता है।")
]:
    s1_mastery_hin.append({"type": "One-Liner", "q": q, "sol": sol})

# Assertion-Reason (8)
for q, ans, sol in [
    ("Assertion (A): Gurdip Singh proposed that aridity caused the decline of Harappan cities.\nReason (R): Pollen samples from Sambhar lake showed a decline in vegetation indicating rainfall reduction around 1800 BCE.", 0, "Both are true, and R explains A. Pollen analysis verified aridity."),
    ("Assertion (A): Kalibangan was abandoned during the Late Harappan phase.\nReason (R): Tectonic uplifts diverted the waters of the Yamuna and Sutlej, causing the Ghaggar-Hakra river to dry up.", 0, "Both are true, and R explain why Kalibangan on the Ghaggar was abandoned."),
    ("Assertion (A): Walter Fairservis argued that the Harappan economy was destroyed by floods.\nReason (R): The intensive cattle grazing denuded vegetation cover, accelerating soil erosion.", 3, "Assertion is false. Fairservis argued ecological imbalance/resource depletion, not floods. Reason is true."),
    ("Assertion (A): Late Harappan settlements shifted towards the Gangetic Doab and Gujarat.\nReason (R): The drying of the Saraswati river system compelled population dispersal towards wetter river basins.", 0, "Both are true, and R is the correct explanation for the eastward migration."),
    ("Assertion (A): The Harappans extensively manufactured baked bricks using iron smelting techniques.\nReason (R): Iron tools were absent during the Mature Harappan period.", 3, "A is false. Harappans were in Bronze Age, no iron was used. R is true."),
    ("Assertion (A): Soil salinization increased in the Indus plain over centuries of intensive farming.\nReason (R): Over-cultivation and continuous irrigation under semi-arid conditions bring salts to the surface.", 0, "Both are true, and R explains A. Continuous farming led to salinization."),
    ("Assertion (A): Gurdip Singh's aridity theory has been accepted by all archaeologists without doubt.\nReason (R): Pollen profiles from salt lakes provide indirect evidence of weather cycles but cannot confirm regional social collapse.", 3, "A is false because many scholars debate if aridity alone could destroy the entire civilization. R is true."),
    ("Assertion (A): Standardized municipal architecture collapsed in the Late Harappan period.\nReason (R): Deforestation created a severe shortage of firewood, leading to a decline in baked brick manufacturing.", 1, "Both statements are true. Deforestation reduced baked bricks, and municipal standards collapsed, but R is not the direct causal explanation for the loss of administrative control.")
]:
    s1_mastery_eng.append({"type": "Assertion-Reason", "q": q, "opts": ar_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("कथन (A): गुरदीप सिंह ने प्रस्ताव दिया कि शुष्कता ने हड़प्पा के शहरों का पतन किया।\nकारण (R): सांभर झील के पराग नमूनों में 1800 ई.पू. के आसपास वर्षा में भारी कमी और वनस्पति ह्रास दिखा।", 0, "दोनों सत्य हैं और R, A की सही व्याख्या करता है।"),
    ("कथन (A): उत्तर हड़प्पा काल में कालीबंगा को छोड़ दिया गया था।\nकारण (R): विवर्तनिक उत्थान ने सतलुज और यमुना का मार्ग बदल दिया, जिससे घग्गर-हकरा नदी सूख गई।", 0, "दोनों सत्य हैं और R, A की सही व्याख्या करता है क्योंकि कालीबंगा घग्गर के किनारे था।"),
    ("कथन (A): वाल्टर फेयरसर्विस ने तर्क दिया कि हड़प्पा की अर्थव्यवस्था को भीषण बाढ़ ने नष्ट किया।\nकारण (R): पशुओं की अत्यधिक चराई से घास के मैदान नष्ट हो गए, जिससे मिट्टी का क्षरण तीव्र हुआ।", 3, "कथन गलत है। फेयरसर्विस ने बाढ़ नहीं बल्कि पारिस्थितिक असंतुलन का तर्क दिया था। कारण सही है।"),
    ("कथन (A): उत्तर हड़प्पा बस्तियाँ गंगा के दोआब और गुजरात की ओर स्थानांतरित हो गईं।\nकारण (R): सरस्वती नदी प्रणाली के सूखने से लोगों को अधिक आर्द्र नदी घाटियों की ओर जाने के लिए मजबूर होना पड़ा।", 0, "दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): हड़प्पा वासियों ने लोहे के उपकरणों का उपयोग करके बड़े पैमाने पर पकी ईंटें बनाईं।\nकारण (R): परिपक्व हड़प्पा काल में लोहे के उपकरण अनुपस्थित थे।", 3, "कथन (A) गलत है। हड़प्पा वासियों के पास लोहा नहीं था। कारण (R) सत्य है।"),
    ("कथन (A): सदियों की सघन खेती के कारण सिंधु के मैदानों में मिट्टी की लवणता बढ़ गई थी।\nकारण (R): अर्द्ध-शुष्क क्षेत्रों में अत्यधिक सिंचाई और खेती से लवण भूमि की सतह पर आ जाते हैं।", 0, "दोनों सत्य हैं और R, A की सही व्याख्या करता है।"),
    ("कथन (A): गुरदीप सिंह के शुष्कता सिद्धांत को सभी पुरातत्वविदों ने बिना किसी संदेह के स्वीकार कर लिया है।\nकारण (R): खारे पानी की झीलों का पराग विश्लेषण मौसम चक्र का अप्रत्यक्ष प्रमाण देता है पर सामाजिक पतन की पुष्टि नहीं करता।", 3, "कथन (A) गलत है क्योंकि इस पर विवाद है। कारण (R) सही है।"),
    ("कथन (A): उत्तर हड़प्पा काल में मानकीकृत नगरपालिका वास्तुकला ध्वस्त हो गई।\nकारण (R): वनों की कटाई से ईंधन की कमी हो गई, जिससे पकी ईंटों के निर्माण में भारी गिरावट आई।", 1, "दोनों सत्य हैं लेकिन R, A की सही व्याख्या नहीं है (प्रशासनिक पतन केवल ईंटों की कमी से नहीं हुआ था)।")
]:
    s1_mastery_hin.append({"type": "Assertion-Reason", "q": q, "opts": hin_ar_opts, "ans": ans, "sol": sol})

# Statement-Based (5)
for q, ans, sol in [
    ("Consider the following statements regarding the Ecological Imbalance Theory:\n1. It calculates that the domestic and municipal needs of Mohenjo-daro exceeded the ecological capacity of its immediate surroundings.\n2. It assumes that the Harappans possessed advanced canal irrigation networks that caused water-logging.\nWhich of the statement(s) is/are correct?", 0, "Statement 1 is correct. Fairservis's calculations showed carrying capacity was breached. Statement 2 is incorrect; advanced state-sponsored canal networks are not documented in the mature phase."),
    ("Consider the following statements regarding the climatic transition in the Indus valley:\n1. The Mature Harappan phase flourished during a period of high rainfall and moisture.\n2. The Late Harappan phase corresponds to a global drying event around 2200-1800 BCE.\nWhich of the statement(s) is/are correct?", 2, "Both statements are correct. Mature phase aligned with wet weather, while the decline aligned with global Holocene aridity."),
    ("Consider the following statements regarding Ghaggar-Hakra river system:\n1. Archaeological surveys by Aurel Stein and A.N. Ghosh documented numerous Harappan sites along its dry bed.\n2. It dried up because its headwaters were captured by tectonic movements.\nWhich of the statement(s) is/are correct?", 2, "Both statements are correct. Stein and Ghosh surveyed the Ghaggar-Hakra bed. Tectonic activity diverted its glacial tributaries, drying it up."),
    ("Consider the following statements regarding Late Harappan pottery:\n1. The fine, painted red-and-black pottery was replaced by coarser, less decorated red wares.\n2. Late Harappan pottery is characterized by complex geometric designs and foreign motifs.\nWhich of the statement(s) is/are correct?", 0, "Statement 1 is correct. Pottery deteriorated in quality and decoration. Statement 2 is incorrect; painted motifs became extremely simple, not complex."),
    ("Consider the following statements regarding Gurdip Singh's rainfall theory:\n1. His pollen analysis demonstrated that high rainfall supported the urban phase of the Indus Valley.\n2. His research proved that the drying of lakes was caused by manual canal diversion by Harappans.\nWhich of the statement(s) is/are correct?", 0, "Statement 1 is correct. High rainfall was shown in pollen levels. Statement 2 is incorrect; drying was climatic, not due to canal diversion.")
]:
    s1_mastery_eng.append({"type": "Statement-Based", "q": q, "opts": mcq_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("पारिस्थितिक असंतुलन सिद्धांत के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. इसके अनुसार मोहनजोदड़ो की घरेलू और नागरिक जरूरतें उसके आसपास के पर्यावरण की क्षमता से अधिक हो गई थीं।\n2. यह मानता है कि हड़प्पा वासियों के पास विकसित नहर सिंचाई प्रणाली थी जिसने जलभराव पैदा किया।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 0, "कथन 1 सही है। फेयरसर्विस ने दर्शाया कि वहन क्षमता समाप्त हो गई थी। कथन 2 गलत है क्योंकि नहरों के व्यापक प्रमाण नहीं हैं।"),
    ("सिंधु घाटी में जलवायु परिवर्तन के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. परिपक्व हड़प्पा काल भारी वर्षा और आर्द्र जलवायु के दौरान फला-फूला।\n2. उत्तर हड़प्पा काल 2200-1800 ई.पू. के आसपास के वैश्विक शुष्कता चरण से मेल खाता है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 2, "दोनों कथन सही हैं। परिपक्व चरण आर्द्र जलवायु में विकसित हुआ और पतन वैश्विक सूखे के काल में हुआ।"),
    ("घग्गर-हकरा नदी प्रणाली के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. ऑरेल स्टीन और ए.एन. घोष ने इसके सूखे मार्ग के किनारे अनेक हड़प्पा स्थलों का दस्तावेजीकरण किया।\n2. विवर्तनिक हलचलों के कारण इसकी मुख्य नदियों का जल मार्ग बदलने से यह सूख गई।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 2, "दोनों कथन सही हैं। स्टीन और घोष ने शुष्क घग्गर का सर्वेक्षण किया था और विवर्तनिक हलचल से नदियाँ दूर चली गई थीं।"),
    ("उत्तर हड़प्पा मृदभांडों (pottery) के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. उत्कृष्ट चित्रित लाल-और-काले बर्तनों का स्थान मोटे और कम नक्काशीदार लाल बर्तनों ने ले लिया।\n2. उत्तर हड़प्पा बर्तनों की विशेषता जटिल ज्यामितीय डिजाइन और विदेशी रूपांकन हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 0, "कथन 1 सही है। बर्तनों की गुणवत्ता में गिरावट आई। कथन 2 गलत है क्योंकि रूपांकन जटिल के बजाय अत्यधिक सरल हो गए थे।"),
    ("गुरदीप सिंह के वर्षा सिद्धांत के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. उनके पराग विश्लेषण ने दर्शाया कि उच्च वर्षा ने सिंधु घाटी के शहरी चरण को सहारा दिया।\n2. उनके शोध ने साबित किया कि झीलों का सूखना हड़प्पा वासियों द्वारा नहरों के मार्ग बदलने से हुआ था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि झीलों का सूखना प्राकृतिक जलवायु परिवर्तन (शुष्कता) का परिणाम था।")
]:
    s1_mastery_hin.append({"type": "Statement-Based", "q": q, "opts": hin_mcq_opts, "ans": ans, "sol": sol})

# Why (3)
for q, sol in [
    ("Why did the shift of the Sutlej River cause the desiccation of the Ghaggar-Hakra channel?", "The Ghaggar-Hakra was not a glacier-fed river by itself; it depended on glacier-fed tributaries like the Sutlej. Tectonic changes diverted the Sutlej westwards, cutting off this water source and causing the channel to dry up."),
    ("Why did Walter Fairservis believe that the Harappans brought about their own ecological ruin?", "He argued that the Harappans over-exploited their fragile semi-arid environment through deforestation (for baking millions of bricks and firing pottery) and intensive livestock grazing, which destroyed the forest cover and depleted soil nutrients."),
    ("Why are pollen profiles from salt lakes in Rajasthan used as evidence for climatic change?", "Pollen grains from different depths reflect the vegetation types of past eras. A high concentration of cereal pollen indicates wet conditions, while a sudden drop and rise in xerophytic (desert-loving) plant pollen around 1800 BCE indicates aridity.")
]:
    s1_mastery_eng.append({"type": "Why", "q": q, "sol": sol})

for q, sol in [
    ("सतलुज नदी के मार्ग बदलने से घग्गर-हकरा नदी मार्ग क्यों सूख गया?", "घग्गर-हकरा स्वयं ग्लेशियर से निकलने वाली नदी नहीं थी; यह सतलुज जैसी ग्लेशियर से निकलने वाली सहायक नदियों पर निर्भर थी। सतलुज के पश्चिम की ओर मुड़ जाने से इसका पानी बंद हो गया और घग्गर सूख गई।"),
    ("वाल्टर फेयरसर्विस का ऐसा क्यों मानना था कि हड़प्पा वासियों ने स्वयं अपना पारिस्थितिक विनाश किया?", "उनका तर्क था कि हड़प्पा वासियों ने ईंटें पकाने और मिट्टी के बर्तन बनाने के लिए वनों की अत्यधिक कटाई की और भारी मात्रा में मवेशी चराई की, जिससे पर्यावरण की वहन क्षमता समाप्त हो गई।"),
    ("जलवायु परिवर्तन के प्रमाण के रूप में राजस्थान की खारे पानी की झीलों के पराग (pollen) प्रोफाइल का उपयोग क्यों किया जाता है?", "मिट्टी की विभिन्न परतों में मिलने वाले परागकण प्राचीन वनस्पतियों को दर्शाते हैं। अनाजों के पराग आर्द्र जलवायु को दर्शाते हैं, जबकि 1800 ई.पू. के बाद शुष्क-कटिले पौधों के पराग शुष्कता की शुरुआत की पुष्टि करते हैं।")
]:
    s1_mastery_hin.append({"type": "Why", "q": q, "sol": sol})

# How (3)
for q, sol in [
    ("How did deforestation accelerate the agricultural decline in the Indus basin?", "Deforestation removed the root systems holding the soil, causing topsoil erosion during rains. With no trees to regulate moisture, groundwater levels dropped, and fields lost their fertility, causing agricultural failure."),
    ("How did tectonic movements in the sub-Himalayan region affect Harappan settlements?", "Tectonic uplifts tilted the gradient of the plains, causing rivers like the Sutlej and Yamuna to change courses. Settlements in Cholistan and eastern Rajasthan lost their primary water source, causing mass desertion."),
    ("How does the material culture of the Late Harappan phase reflect environmental stress?", "The decline of resources is shown in degraded materials: baked bricks were replaced by mud bricks and reused old bricks, fine painted pottery became crude and unpainted, and standardized weight systems vanished due to the collapse of state resources.")
]:
    s1_mastery_eng.append({"type": "How", "q": q, "sol": sol})

for q, sol in [
    ("वनों की कटाई ने सिंधु बेसिन में कृषि पतन को कैसे गति दी?", "पेड़ों के हटने से मिट्टी की ऊपरी उपजाऊ परत का क्षरण हुआ। हवा और बाढ़ से उपजाऊ मिट्टी बह गई, भूजल स्तर गिर गया, जिससे खेतों की उत्पादकता समाप्त हो गई और कृषि संकट गहरा गया।"),
    ("उप-हिमालयी क्षेत्र में विवर्तनिक हलचलों ने हड़प्पा बस्तियों को कैसे प्रभावित किया?", "विवर्तनिक हलचलों ने मैदानों के ढाल को बदल दिया, जिससे सतलुज और यमुना जैसी नदियाँ मार्ग बदलने पर मजबूर हो गईं। चोलिस्तान और पूर्वी राजस्थान की बस्तियों का पानी बंद हो गया, जिससे लोगों को पलायन करना पड़ा।"),
    ("उत्तर हड़प्पा काल की भौतिक संस्कृति पर्यावरणीय तनाव को कैसे दर्शाती है?", "यह भौतिक अवशेषों में दिखता है: पकी ईंटों के स्थान पर कच्ची ईंटों और पुरानी ईंटों का पुनः उपयोग होने लगा, उत्कृष्ट बर्तनों का स्थान खुरदरे बर्तनों ने ले लिया, और बाट-माप प्रणाली गायब हो गई।")
]:
    s1_mastery_hin.append({"type": "How", "q": q, "sol": sol})

# Case Study (3)
for q, sol in [
    ("Analyze Kalibangan as a case study for the desiccation of the Ghaggar-Hakra river system.", "Kalibangan (Rajasthan) was a major urban site of the mature phase situated on the Ghaggar. Excavations show that the site was abandoned without signs of massacre or floods. The dry riverbed and the sudden lack of river silts in the late levels prove that the drying of the river forced the inhabitants to abandon the city."),
    ("Evaluate the Sambhar Lake pollen core study as a case study for aridity in ancient India.", "Gurdip Singh studied core sediments from Sambhar Lake. The core showed high percentages of arboreal (forest) and cereal pollen from 3000 to 1800 BCE, indicating heavy monsoons. Around 1800 BCE, these pollen types decreased sharply, replaced by desert shrubs, proving that regional aridity led to agricultural collapse."),
    ("Examine the Cholistan region surveys as a case study for river migration.", "M.R. Mughal surveyed Cholistan (Pakistan) along the dry bed of the Hakra. He found over 170 Mature Harappan sites but only a few Late Harappan ones. This drastic reduction shows that the migration of the rivers away from the Hakra channel left Cholistan barren, causing a massive population shift towards the east.")
]:
    s1_mastery_eng.append({"type": "Case Study", "q": q, "sol": sol})

for q, sol in [
    ("घग्गर-हकरा नदी मार्ग के सूखने के संदर्भ में कालीबंगा का एक केस स्टडी के रूप में विश्लेषण करें।", "कालीबंगा (राजस्थान) घग्गर के किनारे स्थित था। खुदाई में पता चला कि यहाँ बिना किसी आक्रमण या बाढ़ के शांतिपूर्वक परित्याग किया गया। सूखी नदी घाटी और मिट्टी की परतों में गाद का अभाव साबित करता है कि पानी सूखने पर लोग शहर छोड़कर चले गए।"),
    ("प्राचीन भारत में शुष्कता (aridity) के संदर्भ में सांभर झील के पराग कोर अध्ययन का मूल्यांकन करें।", "गुरदीप सिंह ने सांभर झील की गाद का विश्लेषण किया। 3000 से 1800 ई.पू. तक यहाँ पेड़-पौधों और अनाजों के पराग मिले जो भारी मानसून दर्शाते हैं। 1800 ई.पू. में परागों में भारी गिरावट आई और मरुस्थलीय वनस्पति बढ़ी, जो शुष्कता की पुष्टि करती है।"),
    ("नदी विस्थापन के संदर्भ में चोलिस्तान क्षेत्र के पुरातात्विक सर्वेक्षणों का परीक्षण करें।", "एम.आर. मुगल ने हकरा के सूखे मार्ग के किनारे चोलिस्तान का सर्वेक्षण किया। उन्हें परिपक्व काल के 170 स्थल मिले, पर उत्तर काल के बहुत कम। इससे सिद्ध होता है कि हकरा के सूखने पर चोलिस्तान बंजर हो गया और आबादी पूर्व की ओर चली गई।")
]:
    s1_mastery_hin.append({"type": "Case Study", "q": q, "sol": sol})

# Teach Concept (3)
for q, sol in [
    ("Explain the concept of 'Ecological Carrying Capacity' in the context of Fairservis's theory of Harappan decline.", "Ecological Carrying Capacity refers to the maximum population size that an environment can sustain indefinitely without degradation. Fairservis argued that the dense population and urban demands of Harappan cities exceeded the carrying capacity of the semi-arid Indus valley, causing irreversible environmental degradation and civil collapse."),
    ("Describe the process of 'Pollen Analysis' (Palynology) and how it reconstructs ancient rainfall patterns.", "Pollen grains have tough outer walls and preserve well in lake sediments. By extracting core samples and counting pollen types, researchers identify past vegetation. High crop pollen indicates wet rainfall periods; desert shrub pollen indicates dry, arid periods. This reconstructs historical climate shifts."),
    ("Reconstruct the hydrological shift that occurred when glacier-fed rivers were captured by other river systems.", "Glacier-fed rivers have high, perennial water volumes. Tectonic uplifts tilt the land gradient. When Sutlej was captured by the Indus system and Yamuna by the Ganga, the Ghaggar-Hakra became a rain-fed river. Without glacial melt, it was reduced to a seasonal stream and eventually dried up entirely.")
]:
    s1_mastery_eng.append({"type": "Teach Concept", "q": q, "sol": sol})

for q, sol in [
    ("फेयरसर्विस के सिद्धांत के संदर्भ में 'पारिस्थितिक वहन क्षमता' (Ecological Carrying Capacity) की अवधारणा को स्पष्ट करें।", "वहन क्षमता वह अधिकतम जनसंख्या है जिसे पर्यावरण बिना नुकसान के सहारा दे सकता है। फेयरसर्विस के अनुसार, हड़प्पा शहरों की जनसंख्या उनकी वहन क्षमता से अधिक हो गई थी, जिससे पर्यावरण को स्थायी नुकसान हुआ और नगर बिखर गए।"),
    ("पराग विश्लेषण (Palynology) की प्रक्रिया और इसके द्वारा प्राचीन वर्षा चक्रों के पुनर्निर्माण की विधि को समझाएं।", "झीलों की तलछट में परागकण सुरक्षित रहते हैं। गाद के नमूने निकालकर पराग के प्रकार गिने जाते हैं। वृक्षों और अनाजों के पराग प्रचुर वर्षा दर्शाते हैं; कंटीली झाड़ियों के पराग सूखे के काल को प्रकट करते हैं।"),
    ("हिमनद-पोषित (glacier-fed) नदियों के अन्य प्रणालियों द्वारा ग्रहण (capture) किए जाने पर होने वाले जल-वैज्ञानिक परिवर्तन का वर्णन करें।", "विवर्तनिक हलचलों से भूमि का ढाल बदल जाता है। जब सतलुज को सिंधु ने और यमुना को गंगा ने अपनी ओर खींच लिया, तो घग्गर-हकरा नदी हिमनद जल से वंचित हो गई। बिना ग्लेशियर के पानी के यह मौसमी धारा बनकर रह गई और सूख गई।")
]:
    s1_mastery_hin.append({"type": "Teach Concept", "q": q, "sol": sol})


# =========================================================================
# SECTION 2: HYDROLOGICAL, TECTONIC, AND PATHOLOGICAL THEORIES
# =========================================================================
s2_mastery_eng = []
s2_mastery_hin = []

# MCQ (5)
for q, opts, ans, sol in [
    ("Which scholar proposed that tectonic uplifts near Sehwan created a natural dam on the Indus River, flooding Mohenjo-daro?", ["Robert Raikes", "H.T. Lambrick", "Gurdip Singh", "Mortimer Wheeler"], 0, "Robert Raikes (along with M.R. Sahni and George Dales) proposed the Tectonic Damming theory."),
    ("Who argued that the decline of Mohenjo-daro was due to the Indus River migrating away from the city?", ["H.T. Lambrick", "Robert Raikes", "Walter Fairservis", "John Marshall"], 0, "H.T. Lambrick proposed that river migration left Mohenjo-daro dry and without agricultural water."),
    ("Silt layers containing water-worn pottery deep within Mohenjo-daro are used as evidence for which theory?", ["Aryan invasion", "Tectonic damming and floods", "Ecological imbalance", "Foreign trade collapse"], 1, "Deep silt deposits indicate repeated, prolonged submergence under lake-like conditions caused by natural damming."),
    ("K.V.R. Kennedy's pathological study of Mohenjo-daro skeletons revealed a high incidence of which disease?", ["Plague", "Malaria", "Smallpox", "Cholera"], 1, "Kennedy identified endemic malaria, anemia, and osteoarthritis, pointing to biological factors for population decline."),
    ("The absence of silty clay deposits at Harappa proves that which theory of decline is not applicable to it?", ["River migration", "Tectonic flooding", "Ecological imbalance", "Trade collapse"], 1, "The tectonic flooding and damming theory applies specifically to Mohenjo-daro and lower Indus sites, not to Harappa in Punjab.")
]:
    s2_mastery_eng.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("किस विद्वान ने यह सिद्धांत दिया कि सेहवान के पास विवर्तनिक उत्थान से सिंधु नदी पर प्राकृतिक बांध बन गया और मोहनजोदड़ो डूब गया?", ["रॉबर्ट रैक्स", "एच.टी. लैम्ब्रिक", "गुरदीप सिंह", "मोंटीमर व्हीलर"], 0, "रॉबर्ट रैक्स (सहयोगियों साहनी और डेल्स के साथ) ने प्राकृतिक बांध और बाढ़ का सिद्धांत दिया था।"),
    ("किसने तर्क दिया कि मोहनजोदड़ो का पतन सिंधु नदी के शहर से दूर चले जाने (मार्ग बदलने) के कारण हुआ था?", ["एच.टी. लैम्ब्रिक", "रॉबर्ट रैक्स", "वाल्टर फेयरसर्विस", "जॉन मार्शल"], 0, "एच.टी. लैम्ब्रिक ने तर्क दिया कि नदी विस्थापन से पानी और खेती ठप हो गई।"),
    ("मोहनजोदड़ो के गहरे स्तरों में पानी से घिसी हुई मिट्टी की गाद की परतें किस सिद्धांत का प्रमाण मानी जाती हैं?", ["आर्य आक्रमण", "विवर्तनिक अवरोध और बाढ़", "पारिस्थितिक असंतुलन", "विदेशी व्यापार का पतन"], 1, "गाद की मोटी परतें लंबे समय तक पानी जमा होने (बाढ़) को दर्शाती हैं।"),
    ("के.वी.आर. कैनेडी द्वारा मोहनजोदड़ो के कंकालों के पैथोलॉजिकल अध्ययन में किस बीमारी का अधिक प्रसार पाया गया?", ["प्लेग", "मलेरिया", "चेचक", "हैजा"], 1, "कैनेडी ने कंकालों में मलेरिया और एनीमिया के प्रमाण पाए।"),
    ("हड़प्पा स्थल से गाद (clay silt) की परतों का न मिलना पतन के किस सिद्धांत को वहाँ के लिए अप्रासंगिक बनाता है?", ["नदी विस्थापन", "विवर्तनिक बाढ़", "पारिस्थितिक असंतुलन", "व्यापारिक पतन"], 1, "विवर्तनिक बाढ़ का सिद्धांत मुख्य रूप से मोहनजोदड़ो और निचले सिंधु क्षेत्र पर लागू होता है, हड़प्पा पर नहीं।")
]:
    s2_mastery_hin.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# Multiple Correct MCQ (5)
for q, opts, ans, sol in [
    ("Which of the following scholars supported the tectonic dam and flood theory for Mohenjo-daro? (Select all that apply)", ["M.R. Sahni", "Robert Raikes", "George Dales", "H.T. Lambrick"], [0, 1, 2], "Sahni, Raikes, and Dales supported the tectonic dam theory. Lambrick opposed it."),
    ("Select the pathological conditions identified by K.V.R. Kennedy in Mohenjo-daro skeletons: (Select all that apply)", ["Porotic hyperostosis (anemia)", "Endemic malaria traces", "Osteoarthritis", "Weapon-induced skull fractures"], [0, 1, 2], "Anemia, malaria, and osteoarthritis were identified. Weapon trauma was absent."),
    ("Which arguments support H.T. Lambrick's river migration theory? (Select all that apply)", ["Abandoned silt channels near Mohenjo-daro", "Absence of deep-lake silts in surrounding regions", "Wind-blown sand deposits in late phases", "Rigvedic descriptions of dried-up oceans"], [0, 1, 2], "Abandoned channels, lack of regional lake silts, and wind-blown sand support migration and desiccation. Rigvedic texts do not relate."),
    ("Select the geological/tectonic features of the lower Indus valley associated with Raikes's theory: (Select all that apply)", ["Sehwan tectonic fault line", "Natural rock barriers across the Indus", "Deep silty clay layers inside houses", "Glacial moraines in Sindh"], [0, 1, 2], "Tectonic faults, natural barriers, and silty deposits inside houses support the damming. Glacial moraines are in high mountains, not Sindh."),
    ("Which biological pathogens are linked to the demographic stress in late Indus urban centers? (Select all that apply)", ["Plasmodium falciparum (Malaria)", "Water-borne pathogens from clogged drains", "Nutritional iron-deficiency anemia", "Yersinia pestis (Plague)"], [0, 1, 2], "Malaria, sanitation-induced water pathogens, and nutritional anemia caused stress. Plague is not archaeologically confirmed.")
]:
    s2_mastery_eng.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("मोहनजोदड़ो के लिए विवर्तनिक बांध और बाढ़ सिद्धांत का समर्थन किन विद्वानों ने किया? (सभी सही विकल्प चुनें)", ["एम.आर. साहनी", "रॉबर्ट रैक्स", "जॉर्ज डेल्स", "एच.टी. लैम्ब्रिक"], [0, 1, 2], "साहनी, रैक्स और डेल्स ने इसका समर्थन किया। लैम्ब्रिक ने इसका विरोध किया था।"),
    ("के.वी.आर. कैनेडी द्वारा मोहनजोदड़ो के कंकालों में पहचानी गई बीमारियां कौन सी थीं? (सभी सही विकल्प चुनें)", ["पोरोटिक हाइपरोस्टोसिस (एनीमिया)", "स्थानिक मलेरिया के लक्षण", "ऑस्टियोआर्थराइटिस", "हथियारों से खोपड़ी पर लगे घाव"], [0, 1, 2], "एनीमिया, मलेरिया और जोड़ों की बीमारी (आर्थराइटिस) मिलीं। हथियारों के ताज़ा घाव नहीं थे।"),
    ("एच.टी. लैम्ब्रिक के नदी विस्थापन सिद्धांत का समर्थन करने वाले तर्क कौन से हैं? (सभी सही विकल्प चुनें)", ["मोहनजोदड़ो के पास छोड़े गए नदी मार्ग (silt channels)", "आसपास के क्षेत्रों में गहरी झील जैसी गाद का न मिलना", "अंतिम चरणों में हवा से उड़कर आई रेत की परतें", "ऋग्वेद में सूखे महासागरों का वर्णन"], [0, 1, 2], "छोड़े गए नदी मार्ग, झील गाद का अभाव और रेत की परतें इसका समर्थन करती हैं। ऋग्वेद इससे संबंधित नहीं है।"),
    ("रैक्स के सिद्धांत से जुड़े निचले सिंधु क्षेत्र की भौगोलिक विशेषताएं कौन सी हैं? (सभी सही विकल्प चुनें)", ["सेहवान विवर्तनिक फॉल्ट लाइन", "सिंधु नदी पर प्राकृतिक चट्टानी बाधाएं", "घरों के भीतर गाद की गहरी परतें", "सिंध में हिमनद हिमोढ़ (moraines)"], [0, 1, 2], "सेहवान फॉल्ट लाइन, प्राकृतिक बाधाएं और गाद की परतें विवर्तनिक बांध का समर्थन करती हैं। हिमोढ़ पर्वतीय क्षेत्रों में होते हैं।"),
    ("सिंधु शहरी केंद्रों में जनसंख्या पतन से जुड़े जैविक कारक कौन से हैं? (सभी सही विकल्प चुनें)", ["प्लाज्मोडियम फाल्सीपेरम (मलेरिया)", "रुके हुए नालियों के जलजनित रोग", "पोषण संबंधी आयरन-कमी एनीमिया", "येर्सिनिया पेस्टिस (प्लेग)"], [0, 1, 2], "मलेरिया, जलजनित रोग और एनीमिया इसके प्रमुख कारण थे। प्लेग का कोई साक्ष्य नहीं मिला है।")
]:
    s2_mastery_hin.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# True/False (8)
for q, ans, sol in [
    ("Robert Raikes proposed the tectonic damming theory to explain Mohenjo-daro's decline.", True, "Raikes argued that a tectonic uplift blocked the Indus river flow."),
    ("H.T. Lambrick agreed with Raikes's lake flooding theory.", False, "Lambrick refuted it, proposing river migration away from the city instead."),
    ("Silt deposits at Mohenjo-daro are found at different heights, indicating multiple flood cycles.", True, "Silt layers alternate with occupational levels, proving recurrent flooding."),
    ("Skeletal remains from Mohenjo-daro show clear evidence of battle injuries in 90% of cases.", False, "Pathological studies by KVR Kennedy showed only a few healed fractures, not battle injuries."),
    ("The tectonic dam theory explains the decline of all Harappan sites, including Ropar and Lothal.", False, "The theory is geographically limited to Mohenjo-daro and lower Indus basin sites."),
    ("Endemic malaria would have severely weakened the city's labor force and trade economy.", True, "Widespread disease leads to demographic decay and loss of municipal efficiency."),
    ("Tectonic activity near Sehwan is impossible because the region has no geological faults.", False, "Sehwan lies near a major active seismic fault line."),
    ("Mohenjo-daro residents abandoned the city because the Indus river completely dried up.", False, "The river shifted its channel; it did not dry up entirely, but left the city dry.")
]:
    s2_mastery_eng.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("रॉबर्ट रैक्स ने मोहनजोदड़ो के पतन की व्याख्या के लिए विवर्तनिक बांध सिद्धांत दिया था।", True, "रैक्स ने तर्क दिया कि विवर्तनिक उत्थान ने सिंधु नदी को अवरुद्ध किया था।"),
    ("एच.टी. लैम्ब्रिक रैक्स के झील बाढ़ सिद्धांत से सहमत थे।", False, "लैम्ब्रिक ने इसका खंडन कर नदी विस्थापन (migration) का सिद्धांत दिया।"),
    ("मोहनजोदड़ो में गाद की परतें अलग-अलग ऊंचाइयों पर मिली हैं जो बार-बार बाढ़ आने की पुष्टि करती हैं।", True, "गाद की परतें विभिन्न स्तरों पर वैकल्पिक रूप से मिलती हैं।"),
    ("मोहनजोदड़ो के 90% कंकालों पर युद्ध के घावों के स्पष्ट प्रमाण मिले हैं।", False, "के.वी.आर. कैनेडी के शोध में केवल कुछ ही कंकालों पर पुरानी ठीक हो चुकी चोटें मिलीं।"),
    ("विवर्तनिक बांध सिद्धांत रोपण और लोथल सहित सभी स्थलों के पतन की व्याख्या करता है।", False, "यह भौगोलिक रूप से केवल निचले सिंधु क्षेत्र के लिए प्रासंगिक है।"),
    ("स्थानिक मलेरिया ने शहर की श्रम शक्ति और व्यापारिक दक्षता को गंभीर रूप से कमजोर किया होगा।", True, "बीमारी से श्रम शक्ति और नागरिक व्यवस्था बिखर गई।"),
    ("सेहवान के पास विवर्तनिक हलचल असंभव है क्योंकि वहां कोई फॉल्ट लाइन नहीं है।", False, "सेहवान क्षेत्र एक सक्रिय भूकंपीय फॉल्ट लाइन पर स्थित है।"),
    ("सिंधु नदी पूरी तरह से सूख जाने के कारण मोहनजोदड़ो के लोगों ने शहर छोड़ दिया था।", False, "नदी ने अपना मार्ग बदला था, वह पूरी तरह सूखी नहीं थी।")
]:
    s2_mastery_hin.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

# Fill in the Blank (8)
for q, ans, sol in [
    ("The tectonic uplift that dammed the Indus River occurred near the town of ________.", "Sehwan", "Tectonic activity near Sehwan created the natural Indus dam."),
    ("Deep layers of silty ________ found inside houses indicate prolonged water submergence.", "clay", "Silty clay deposits indicate still-water flooding inside residential areas."),
    ("The theory of river migration away from Mohenjo-daro was proposed by ________.", "H.T. Lambrick", "Lambrick proposed that the Indus shifted its course away from the city."),
    ("K.V.R. Kennedy utilized the science of ________ to study human skeletal remains.", "paleopathology", "Paleopathology is the study of ancient diseases in skeletons."),
    ("Malaria traces in skeletons are indicated by bone modifications like porotic ________.", "hyperostosis", "Porotic hyperostosis is an indicator of severe anemia, linked to malaria."),
    ("Unlike Mohenjo-daro, the city of ________ in Punjab shows no water silt layers.", "Harappa", "Harappa, located on the Ravi, does not show Indus silt flood layers."),
    ("Tectonic earthquakes disrupted the city's brick-lined municipal ________ system.", "drainage", "Drainage structures collapsed, creating stagnancy and disease."),
    ("The natural damming of the Indus created a giant temporary ________.", "lake", "The dam blocked river flow, forming a huge lake that submerged Mohenjo-daro.")
]:
    s2_mastery_eng.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("सिंधु नदी को बाधित करने वाला विवर्तनिक उत्थान ________ नामक कस्बे के पास हुआ था।", "सेहवान", "सेहवान के पास भू-गर्भीय हलचल से प्राकृतिक बांध बना था।"),
    ("घरों के अंदर पाई जाने वाली ________ मिट्टी की गहरी परतें लंबे समय तक जलभराव दर्शाती हैं।", "गाद", "गाद (silt clay) की परतें स्थिर जल ठहराव का संकेत हैं।"),
    ("सिंधु नदी के मोहनजोदड़ो से दूर खिसकने का मार्ग परिवर्तन सिद्धांत ________ ने दिया था।", "एच.टी. लैम्ब्रिक", "लैम्ब्रिक ने मार्ग परिवर्तन का सिद्धांत दिया।"),
    ("के.वी.आर. कैनेडी ने कंकालों के अध्ययन के लिए ________ विज्ञान का उपयोग किया।", "पुरा-रोगविज्ञान", "पुरा-रोगविज्ञान (paleopathology) प्राचीन रोगों का अध्ययन है।"),
    ("कंकालों में मलेरिया के प्रभाव को हड्डी में होने वाले पोरोटिक ________ से आंका गया।", "हाइपरोस्टोसिस", "पोरोटिक हाइपरोस्टोसिस गंभीर एनीमिया और मलेरिया का सूचक है।"),
    ("मोहनजोदड़ो के विपरीत, पंजाब के प्रसिद्ध स्थल ________ में बाढ़ की गाद नहीं मिलती।", "हड़प्पा", "हड़प्पा रावी नदी तट पर था, अतः वहाँ सिंधु की बाढ़ के साक्ष्य नहीं हैं।"),
    ("भूकंपीय झटकों ने शहर की ईंटों से बनी नगरपालिका की ________ व्यवस्था को नष्ट कर दिया।", "जल निकासी", "जल निकासी व्यवस्था टूटने से बीमारियाँ फैलीं।"),
    ("विवर्तनिक बांध बनने से सिंधु नदी का पानी रुक गया और एक विशाल ________ बन गई।", "झील", "नदी का पानी रुकने से एक बड़ी कृत्रिम झील बन गई थी।")
]:
    s2_mastery_hin.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

# Match the Following (3)
s2_matches_eng = [
    {"q": "Match the hydrological theory with its diagnostic geological evidence:",
     "pairs": ["Tectonic Damming - Silty clay layers containing water-worn pottery", "River Migration - Relic channels and wind-blown sands near Mohenjo-daro", "Saraswati Desiccation - Dry Ghaggar channel surveyed by Stein", "Monsoon Failure - Pollen sequence showing drop in grass pollen"],
     "sol": "Tectonic damming is proved by silty clay; river migration by relic channels; Saraswati by Stein's surveys; monsoon failure by pollen."},
    {"q": "Match the pathological indicator with its biological cause:",
     "pairs": ["Porotic hyperostosis - Chronic iron-deficiency anemia", "Enlarged bone vascularity - Endemic malaria infection", "Degenerative joint disease - Severe physical labor and arthritis", "Unhealed skeletal trauma - Actual violence or burial disturbance"],
     "sol": "Porotic hyperostosis indicates anemia; bone vascularity indicates malaria; joint disease indicates labor; unhealed trauma indicates violence."},
    {"q": "Match the scholar with their critique of alternative decline theories:",
     "pairs": ["George Dales - Refuted Wheeler's massacre theory using stratigraphy", "H.T. Lambrick - Refuted Raikes's lake flooding theory using local hydrology", "K.V.R. Kennedy - Refuted military invasion by documenting skeletal diseases", "Walter Fairservis - Refuted external trade collapse as the sole reason"],
     "sol": "Dales refuted Wheeler; Lambrick refuted Raikes; Kennedy refuted invasion; Fairservis highlighted ecological limits."}
]
s2_mastery_eng.extend([make_match_question(m) for m in s2_matches_eng])

s2_matches_hin = [
    {"q": "जल-वैज्ञानिक सिद्धांत को उसके पुरातात्विक साक्ष्यों से सुमेलित करें:",
     "pairs": ["विवर्तनिक अवरोध - पानी से घिसी गाद और बर्तनों की परतें", "नदी विस्थापन - छोड़े गए मार्ग और उड़कर आई रेत के टीले", "सरस्वती का सूखना - स्टीन द्वारा खोजा गया सूखा घग्गर मार्ग", "मानसून की कमी - घास के परागकणों में तीव्र गिरावट"],
     "sol": "विवर्तनिक अवरोध गाद से; नदी विस्थापन रेत और छोड़े मार्गों से; सरस्वती सूखना घग्गर मार्ग से और मानसून कमी पराग से सिद्ध होता है।"},
    {"q": "शारीरिक संकेतक को उसके जैविक कारण से सुमेलित करें:",
     "pairs": ["पोरोटिक हाइपरोस्टोसिस - गंभीर आयरन-कमी एनीमिया", "अस्थि वाहिकाओं का बढ़ना - स्थानिक मलेरिया संक्रमण", "जोड़ों का ह्रास - कठिन शारीरिक श्रम और आर्थराइटिस", "कंकाल पर चोट - वास्तविक हिंसा या दफन के समय की टूट-फूट"],
     "sol": "हाइपरोस्टोसिस एनीमिया से; अस्थि वाहिकाएँ मलेरिया से; जोड़ों का ह्रास श्रम से और चोट नरसंहार या दफन बाधा से संबंधित हैं।"},
    {"q": "विद्वान को अन्य पतन सिद्धांतों की उनके द्वारा की गई आलोचना से सुमेलित करें:",
     "pairs": ["जॉर्ज डेल्स - स्तरिकी का उपयोग कर व्हीलर के नरसंहार सिद्धांत को खारिज किया", "एच.टी. लैम्ब्रिक - स्थानीय जल-प्रवाह से रैक्स के झील बाढ़ सिद्धांत को खारिज किया", "के.वी.आर. कैनेडी - रोगों का दस्तावेजीकरण कर बाहरी सैन्य आक्रमण को खारिज किया", "वाल्टर फेयरसर्विस - बाहरी व्यापार पतन को एकमात्र कारण मानने से इनकार किया"],
     "sol": "डेल्स ने व्हीलर को खारिज किया; लैम्ब्रिक ने रैक्स को; कैनेडी ने आक्रमण को; फेयरसर्विस ने केवल व्यापार पतन को नाकाफी बताया।"}
]
s2_mastery_hin.extend([make_match_question(m) for m in s2_matches_hin])

# One-Liner (8)
for q, sol in [
    ("What geological feature near Sehwan was responsible for Raikes's tectonic dam?", "A seismic fault zone that underwent tectonic uplift, raising a barrier across the Indus River."),
    ("Why did Lambrick reject the idea of a giant lake flooding Mohenjo-daro?", "He argued that the Indus silt deposits were riverine silts, not the deep lacustrine silts characteristic of a lake."),
    ("What does 'porotic hyperostosis' in skeletons indicate?", "It indicates severe anemia, which is a common physiological response to chronic malaria."),
    ("How did stagnant water in clogged drains impact Harappan health?", "It created breeding grounds for mosquitoes and water-borne pathogens, causing epidemics."),
    ("Why did the Indus River change its course away from Mohenjo-daro?", "Tectonic tilt of the Indus alluvial plain caused the river to seek a lower gradient channel."),
    ("What evidence did K.V.R. Kennedy use to show that Mohenjo-daro was not destroyed by a war?", "The lack of cut marks, weapon injuries, and battle trauma on the excavated skeletons."),
    ("How many flood levels were identified at Mohenjo-daro by archaeologists?", "At least seven distinct occupational levels separated by thick layers of silt."),
    ("What was the demographic consequence of malaria in the Late Harappan cities?", "A significant drop in population density, leading to the abandonment of urban maintenance.")
]:
    s2_mastery_eng.append({"type": "One-Liner", "q": q, "sol": sol})

for q, sol in [
    ("सेहवान के पास कौन सी भौगोलिक विशेषता रैक्स के विवर्तनिक बांध के लिए जिम्मेदार थी?", "एक सक्रिय भूकंपीय फॉल्ट जोन जिसने विवर्तनिक उत्थान के कारण सिंधु नदी पर एक प्राकृतिक दीवार खड़ी कर दी।"),
    ("लैम्ब्रिक ने मोहनजोदड़ो में विशाल झील बनने के सिद्धांत को क्यों खारिज किया?", "उनका तर्क था कि सिंधु की गाद नदी द्वारा बहाकर लाई गई मिट्टी थी, न कि किसी स्थिर झील की गहरी गाद।"),
    ("कंकालों में 'पोरोटिक हाइपरोस्टोसिस' क्या दर्शाता है?", "यह गंभीर एनीमिया को दर्शाता है, जो मलेरिया महामारी का एक आम शारीरिक प्रभाव है।"),
    ("रुके हुए नालियों के पानी ने हड़प्पा वासियों के स्वास्थ्य पर क्या प्रभाव डाला?", "इससे मच्छरों और जलजनित रोगाणुओं को पनपने का मौका मिला, जिससे महामारियां फैलीं।"),
    ("सिंधु नदी मोहनजोदड़ो से दूर क्यों खिसक गई?", "मैदानी ढाल में भूकंपीय या विवर्तनिक झुकाव होने से नदी ने ढलान की ओर नया मार्ग खोज लिया।"),
    ("के.वी.आर. कैनेडी ने यह साबित करने के लिए क्या सबूत दिया कि मोहनजोदड़ो युद्ध में नष्ट नहीं हुआ था?", "खुदाई में मिले कंकालों पर तलवारों के कट, हथियारों के गहरे घाव या युद्ध आघात का अभाव।"),
    ("पुरातत्वविदों ने मोहनजोदड़ो में बाढ़ के कितने स्तरों की पहचान की है?", "गाद की मोटी परतों द्वारा अलग किए गए कम से कम सात अलग-अलग आवासीय स्तर।"),
    ("उत्तर हड़प्पा शहरों में मलेरिया का जनसांख्यिकीय परिणाम क्या हुआ?", "जनसंख्या घनत्व में भारी गिरावट आई, जिससे नागरिक रख-रखाव और नगर पालिका पतन हुआ।")
]:
    s2_mastery_hin.append({"type": "One-Liner", "q": q, "sol": sol})

# Assertion-Reason (8)
for q, ans, sol in [
    ("Assertion (A): Tectonic uplift near Sehwan caused Mohenjo-daro to be submerged under water.\nReason (R): Layers of silty clay containing pottery are found at high levels within the city's residential quarters.", 0, "Both are true, and R is the direct physical evidence of flooding caused by damming (A)."),
    ("Assertion (A): H.T. Lambrick proposed that the Indus River shifted its course away from Mohenjo-daro.\nReason (R): A shift in the river channel deprived the city of the water required for domestic and agricultural sustenance.", 0, "Both are true, and R is the correct explanation for the city's abandonment proposed by Lambrick (A)."),
    ("Assertion (A): K.V.R. Kennedy confirmed that Mortimer Wheeler's invasion theory was correct.\nReason (R): Kennedy's studies showed that the skeletons of Mohenjo-daro had healed fractures and suffered from malaria.", 3, "Assertion is false. Kennedy refuted Wheeler's theory. Reason is true."),
    ("Assertion (A): Recurrent flooding forced the citizens of Mohenjo-daro to rebuild their houses on top of older silted structures.\nReason (R): The municipal authority maintained strict grid control and drainage levels even in the latest phases.", 2, "A is true. Citizens rebuilt on silt. R is false; municipal planning collapsed completely in the late phase."),
    ("Assertion (A): Tectonic disturbances in the Indus plain occurred during the Bronze Age.\nReason (R): Seismic faults in Sindh have been historically active, causing shifts in alluvial gradients.", 0, "Both are true, and R explains why tectonic shifts occurred in the Indus plain during that time."),
    ("Assertion (A): Skeletal pathology demonstrates that Mohenjo-daro's population declined due to an invasion of horse-riders.\nReason (R): No horse remains or military weapons of Central Asian type are found in the Mature Harappan layers.", 3, "A is false. Skeletal pathology indicates malaria/anemia, not invasion. R is true."),
    ("Assertion (A): The tectonic damming theory explains the lack of agricultural water at Kalibangan.\nReason (R): Kalibangan was situated on the Ghaggar river, which was independent of the Indus river system.", 3, "A is false because tectonic damming applies only to Mohenjo-daro on the Indus. R is true."),
    ("Assertion (A): Water-logging and poor sanitation became severe in the final phase of Mohenjo-daro.\nReason (R): Drains were clogged, kilns were built in the middle of streets, and houses were divided into small tenements.", 0, "Both are true, and R is the direct evidence of the breakdown of sanitation and water-logging (A).")
]:
    s2_mastery_eng.append({"type": "Assertion-Reason", "q": q, "opts": ar_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("कथन (A): सेहवान के पास विवर्तनिक उत्थान ने मोहनजोदड़ो को जलमग्न कर दिया।\nकारण (R): शहर के आवासीय क्षेत्रों में ऊंचाई पर मिट्टी के बर्तनों वाली गाद की परतें मिली हैं।", 0, "दोनों सत्य हैं और R, A की सही व्याख्या करता है।"),
    ("कथन (A): एच.टी. लैम्ब्रिक ने प्रस्ताव दिया कि सिंधु नदी मोहनजोदड़ो से दूर खिसक गई थी।\nकारण (R): नदी के विस्थापन ने शहर को घरेलू और कृषि उपयोग के लिए आवश्यक पानी से वंचित कर दिया।", 0, "दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): के.वी.आर. कैनेडी ने पुष्टि की कि मोंटीमर व्हीलर का आक्रमण सिद्धांत सही था।\nकारण (R): कैनेडी के शोध ने दिखाया कि मोहनजोदड़ो के कंकाल मलेरिया से पीड़ित थे और उन पर पुरानी ठीक हो चुकी चोटें थीं।", 3, "कथन (A) गलत है। कैनेडी ने व्हीलर का खंडन किया था। कारण (R) सही है।"),
    ("कथन (A): बार-बार आने वाली बाढ़ ने मोहनजोदड़ो के नागरिकों को पुरानी गाद वाली संरचनाओं के ऊपर घर बनाने को मजबूर किया।\nकारण (R): नगरपालिका प्राधिकार ने अंतिम चरणों में भी जल निकासी और ग्रिड नियोजन पर कड़ा नियंत्रण बनाए रखा।", 2, "A सत्य है पर R गलत है क्योंकि अंतिम चरण में नियोजन और जल निकासी पूरी तरह ध्वस्त हो चुकी थी।"),
    ("कथन (A): कांस्य युग के दौरान सिंधु के मैदान में विवर्तनिक हलचलें हुई थीं।\nकारण (R): सिंध में भूकंपीय फॉल्ट ऐतिहासिक रूप से सक्रिय रहे हैं, जिससे नदी ढलान में बदलाव हुए हैं।", 0, "दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): कंकाल रोगविज्ञान (skeletal pathology) दर्शाता है कि मोहनजोदड़ो की आबादी का ह्रास घुड़सवार आक्रमणकारियों के कारण हुआ।\nकारण (R): परिपक्व हड़प्पा स्तरों से मध्य एशियाई प्रकार के घोड़े के अवशेष या सैन्य हथियार नहीं मिले हैं।", 3, "A गलत है क्योंकि रोगविज्ञान मलेरिया दर्शाता है, आक्रमण नहीं। R सही है।"),
    ("कथन (A): विवर्तनिक बांध सिद्धांत कालीबंगा में कृषि जल की कमी की व्याख्या करता है।\nकारण (R): कालीबंगा घग्गर नदी के किनारे स्थित था, जो सिंधु नदी प्रणाली से स्वतंत्र थी।", 3, "A गलत है क्योंकि बांध सिद्धांत केवल मोहनजोदड़ो के लिए है। R सही है।"),
    ("कथन (A): मोहनजोदड़ो के अंतिम चरण में जलभराव और खराब स्वच्छता की स्थिति गंभीर हो गई थी।\nकारण (R): नालियाँ बंद थीं, सड़कों के बीच भट्टियाँ बनाई गईं और घरों को छोटे-छोटे कमरों में विभाजित कर दिया गया।", 0, "दोनों सत्य हैं और R, A की सही व्याख्या है।")
]:
    s2_mastery_hin.append({"type": "Assertion-Reason", "q": q, "opts": hin_ar_opts, "ans": ans, "sol": sol})

# Statement-Based (5)
for q, ans, sol in [
    ("Consider the following statements regarding the tectonic dam theory:\n1. It states that an earthquake created a rocky dam near Sehwan, blocking the Indus flow.\n2. Silt deposits at Mohenjo-daro show that the city was submerged under still, lake-like waters.\nWhich of the statement(s) is/are correct?", 2, "Both statements are correct. Raikes proposed that tectonic blockages formed a lake, and silt clay shows still-water flooding."),
    ("Consider the following statements regarding the river migration theory:\n1. It was proposed by H.T. Lambrick as an alternative to the tectonic dam theory.\n2. It explains that the Indus shifted its course eastwards, causing massive erosion of Mohenjo-daro's citadel.\nWhich of the statement(s) is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect; the shift left the city dry and desiccated, it did not wash away the citadel."),
    ("Consider the following statements regarding paleopathological findings:\n1. Skeletons from Mohenjo-daro show a high percentage of deaths caused by iron arrowheads.\n2. Osteological analysis reveals that malaria was endemic in the late stages of Mohenjo-daro.\nWhich of the statement(s) is/are correct?", 1, "Statement 1 is incorrect; no iron arrowheads or weapon injuries were found. Statement 2 is correct; malaria was indeed endemic."),
    ("Consider the following statements regarding the geological fault lines of Sindh:\n1. The lower Indus valley is situated near the junction of tectonic plates, making it prone to earthquakes.\n2. Tectonic uplifts could easily block flat alluvial plains like that of the Indus.\nWhich of the statement(s) is/are correct?", 2, "Both statements are correct. Plate boundaries make Sindh seismically active, and flat plains are easily dammed by minor uplifts."),
    ("Consider the following statements regarding sanitation and health in Late Mohenjo-daro:\n1. Municipal administration completely collapsed, leading to clogged drains and stagnant water.\n2. Stagnant water is archaeologically linked to the spread of malaria vector mosquitoes.\nWhich of the statement(s) is/are correct?", 2, "Both statements are correct. Loss of drain maintenance and stagnation facilitated malaria vector breeding, contributing to decline.")
]:
    s2_mastery_eng.append({"type": "Statement-Based", "q": q, "opts": mcq_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("विवर्तनिक बांध सिद्धांत के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. इसके अनुसार सेहवान के पास आए भूकंप ने सिंधु के मार्ग को अवरुद्ध कर एक प्राकृतिक बांध बना दिया था।\n2. मोहनजोदड़ो में मिले गाद के अवशेष दर्शाते हैं कि शहर लंबे समय तक शांत झील जैसे पानी में डूबा रहा था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 2, "दोनों कथन सही हैं। रैक्स के अनुसार भूकंपीय हलचल से पानी रुका और गाद से जलभराव सिद्ध होता है।"),
    ("नदी विस्थापन सिद्धांत के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. यह सिद्धांत एच.टी. लैम्ब्रिक द्वारा विवर्तनिक बांध सिद्धांत के विकल्प के रूप में दिया गया था।\n2. इसके अनुसार सिंधु नदी ने पूर्व की ओर रुख किया जिससे मोहनजोदड़ो के दुर्ग का भारी कटाव हुआ।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि विस्थापन से शहर सूखा पड़ गया था, दुर्ग का कटाव नहीं हुआ था।"),
    ("पुरा-रोगविज्ञान (paleopathology) के निष्कर्षों के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. मोहनजोदड़ो के कंकालों में लोहे के तीरों से होने वाली मौतों का उच्च प्रतिशत मिला है।\n2. अस्थि विश्लेषण से पता चलता है कि मोहनजोदड़ो के अंतिम चरणों में मलेरिया महामारी के रूप में फैला था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 1, "कथन 1 गलत है। लोहे के तीर नहीं मिले। कथन 2 सही है क्योंकि मलेरिया के अकाट्य प्रमाण मिले हैं।"),
    ("सिंध की भू-गर्भीय फॉल्ट लाइनों के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. निचली सिंधु घाटी टेक्टोनिक प्लेटों के जंक्शन के पास स्थित है, जिससे यहाँ भूकंप का खतरा बना रहता है।\n2. थोड़े से विवर्तनिक उत्थान भी सिंधु जैसे समतल जलोढ़ मैदानों के मार्ग को आसानी से अवरुद्ध कर सकते हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 2, "दोनों कथन सही हैं। यह क्षेत्र भूकंपीय रूप से सक्रिय है और समतल मैदान आसानी से बाधित हो जाते हैं।"),
    ("उत्तर कालीन मोहनजोदड़ो में स्वच्छता और स्वास्थ्य के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. नगरपालिका प्रशासन पूरी तरह चरमरा गया था, जिससे नालियाँ अवरुद्ध हो गईं और पानी जमा हो गया।\n2. रुके हुए पानी को पुरातात्विक रूप से मलेरिया फैलाने वाले मच्छरों के पनपने से जोड़ा गया है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 2, "दोनों कथन सही हैं। स्वच्छता खत्म होने और नालियों के अवरुद्ध होने से मच्छरों को पनपने का मौका मिला।")
]:
    s2_mastery_hin.append({"type": "Statement-Based", "q": q, "opts": hin_mcq_opts, "ans": ans, "sol": sol})

# Why (3)
for q, sol in [
    ("Why did K.V.R. Kennedy reject the theory of a violent massacre at Mohenjo-daro?", "He analyzed the skeletons and found that the wounds were either healed fractures (incurred years before death) or post-depositional damages caused by soil pressure. The lack of weapon trauma and presence of bone lesions from malaria and anemia proved that they died of disease, not violence."),
    ("Why does tectonic damming lead to silty clay layers inside urban houses?", "When a river is dammed, its flow stops and it forms a lake. The mud and silt carried by the river settle to the bottom in still-water conditions, depositing a layer of fine silty clay. Recurrent damming creates alternating layers of occupational debris and silt."),
    ("Why did the migration of the Indus River away from Mohenjo-daro ruin its economy?", "The city relied entirely on the Indus for water supply and agricultural irrigation in its floodplains. When the river shifted its course miles away, the irrigation channels dried up, agricultural yields collapsed, and domestic water became scarce, forcing abandonment.")
]:
    s2_mastery_eng.append({"type": "Why", "q": q, "sol": sol})

for q, sol in [
    ("के.वी.आर. कैनेडी ने मोहनजोदड़ो में हिंसक नरसंहार के सिद्धांत को क्यों खारिज कर दिया?", "उन्होंने कंकालों का विश्लेषण कर पाया कि चोटें या तो बहुत पुरानी और ठीक हो चुकी थीं या मिट्टी के दबाव से बाद में हुई टूट-फूट थीं। कंकालों पर हथियारों के ताज़ा घाव नहीं मिले, जबकि मलेरिया और एनीमिया के निशान मिले।"),
    ("विवर्तनिक बांध बनने से मोहनजोदड़ो के घरों के भीतर गाद की परतें क्यों जमा हो गईं?", "नदी का मार्ग रुकने पर वह झील बन जाती है। शांत पानी में नदी द्वारा बहाकर लाई गई महीन गाद और मिट्टी नीचे बैठ जाती है, जिससे गाद (silt clay) की मोटी परतें जमा हो गईं।"),
    ("सिंधु नदी के मोहनजोदड़ो से दूर खिसकने से वहाँ की अर्थव्यवस्था क्यों नष्ट हो गई?", "शहर पानी और कृषि सिंचाई के लिए सिंधु नदी पर निर्भर था। नदी के मीलों दूर खिसक जाने से नहरें सूख गईं, फसलें नष्ट हो गईं और दैनिक उपयोग के पानी की किल्लत से लोग पलायन कर गए।")
]:
    s2_mastery_hin.append({"type": "Why", "q": q, "sol": sol})

# How (3)
for q, sol in [
    ("How did Robert Raikes explain the accumulation of silt at Mohenjo-daro?", "He proposed that tectonic uplifts near Sehwan formed natural dams. The Indus River backed up, forming a temporary lake. As Mohenjo-daro was flooded under this lake, silt settled inside the buildings. When the dam breached, the lake drained, and the process repeated over centuries."),
    ("How did H.T. Lambrick use local geomorphology to argue against the flood theory?", "He observed that the silty clay was river-silt deposited during normal annual floods, not lake-silt. He pointed to dry riverbeds near Mohenjo-daro as evidence that the river shifted its channel, depriving the area of water rather than drowning it."),
    ("How did the collapse of civic drainage under tectonic stress create a pathological crisis?", "Tectonic earthquakes damaged the brick sewers, halting the flow of waste. The municipal authority failed to clear the blockages. Stagnant water accumulated in streets and houses, leading to an explosion of malaria-carrying mosquitoes and water-borne pathogens.")
]:
    s2_mastery_eng.append({"type": "How", "q": q, "sol": sol})

for q, sol in [
    ("रॉबर्ट रैक्स ने मोहनजोदड़ो में गाद (silt) के जमाव की व्याख्या कैसे की?", "उन्होंने तर्क दिया कि सेहवान के पास विवर्तनिक हलचल से प्राकृतिक बांध बन गया। सिंधु का पानी वापस लौट आया और एक झील बन गई। जलमग्न शहर के घरों में गाद बैठ गई। बांध टूटने पर पानी निकला और यह चक्र बार-बार दोहराया गया।"),
    ("एच.टी. लैम्ब्रिक ने बाढ़ सिद्धांत के विरोध में स्थानीय भू-आकृति विज्ञान का उपयोग कैसे किया?", "उन्होंने पाया कि गाद नदी की सामान्य वार्षिक बाढ़ की मिट्टी थी, न कि किसी झील की शांत गाद। उन्होंने मोहनजोदड़ो के पास सूखे नदी मार्गों को दिखाकर मार्ग परिवर्तन (river migration) का तर्क दिया।"),
    ("विवर्तनिक तनाव के तहत नगरपालिका जल निकासी के पतन ने स्वास्थ्य संकट कैसे खड़ा किया?", "भूकंपीय झटकों से नालियाँ टूट गईं जिससे कचरे का निकास बंद हो गया। नालियों में जमा रुके हुए पानी में मलेरिया के मच्छर और बैक्टीरिया पनपे जिससे स्वास्थ्य संकट और महामारियाँ फैलीं।")
]:
    s2_mastery_hin.append({"type": "How", "q": q, "sol": sol})

# Case Study (3)
for q, sol in [
    ("Evaluate the 'HR Area Skeletons' of Mohenjo-daro as a case study for Wheeler's massacre theory.", "Wheeler cited 14 skeletons found in a room in the HR area of Mohenjo-daro as victims of an Aryan massacre. A detailed case study showed they were buried or lay in different strata, and KVR Kennedy's osteological examination showed no weapon cuts but clear signs of malaria and anemia, proving they did not die in a single battle."),
    ("Analyze the Sehwan Fault Line uplift as a case study for tectonic damming.", "The Sehwan region is geologically active. Tectonic shifts along the fault line raised the rock bed, acting as a natural dam. This case study shows how a flat alluvial plain like Sindh is highly sensitive to tectonic changes, which can completely alter river networks and submerge nearby settlements."),
    ("Examine the paleopathological study of Mohenjo-daro skeletal series as a case study for disease-driven decline.", "Kennedy examined a series of skeletons from Mohenjo-daro and found porotic hyperostosis in the skulls and abnormal bone growth. This case study proved that malaria was endemic, causing chronic health deterioration, reducing birth rates, and leading to demographic collapse without military action.")
]:
    s2_mastery_eng.append({"type": "Case Study", "q": q, "sol": sol})

for q, sol in [
    ("व्हीलर के नरसंहार सिद्धांत के संदर्भ में मोहनजोदड़ो के 'HR क्षेत्र के कंकालों' का केस स्टडी के रूप में मूल्यांकन करें।", "व्हीलर ने HR क्षेत्र के एक कमरे से मिले 14 कंकालों को नरसंहार का शिकार बताया था। विस्तृत अध्ययन से पता चला कि ये अलग-अलग स्तरों के थे और कैनेडी ने दर्शाया कि उन पर युद्ध के घाव नहीं थे बल्कि मलेरिया के लक्षण थे।"),
    ("विवर्तनिक बांध के संदर्भ में सेहवान फॉल्ट लाइन के उत्थान का केस स्टडी के रूप में विश्लेषण करें।", "सेहवान क्षेत्र भूकंपीय रूप से सक्रिय है। फॉल्ट लाइन के पास भूमि उठने से प्राकृतिक बांध बना। यह केस स्टडी दर्शाती है कि सिंध जैसे जलोढ़ मैदान भूकंपीय हलचलों के प्रति कितने संवेदनशील हैं जिससे नदियाँ मार्ग बदल लेती हैं।"),
    ("बीमारी से होने वाले पतन के केस स्टडी के रूप में मोहनजोदड़ो के मानव अवशेषों के पुरा-रोगवैज्ञानिक अध्ययन का परीक्षण करें।", "कैनेडी ने मोहनजोदड़ो के कंकालों की खोपड़ियों में पोरोटिक हाइपरोस्टोसिस पाया। इस केस स्टडी ने साबित किया कि मलेरिया महामारी के रूप में फैला था जिससे जनसंख्या में भारी गिरावट आई और शहर उजड़ गया।")
]:
    s2_mastery_hin.append({"type": "Case Study", "q": q, "sol": sol})

# Teach Concept (3)
for q, sol in [
    ("Explain the concept of 'Lacustrine vs. Alluvial Siltation' in geological studies of river basins.", "Alluvial siltation is deposited by flowing river water during seasonal floods and contains coarse grains. Lacustrine siltation is deposited at the bottom of still lakes and contains extremely fine silty clay. Identifying the type of silt helps determine whether a city was flooded by a river shift or a tectonic dam lake."),
    ("Describe the concept of 'Epidemiological Transition' in ancient urban centers.", "Epidemiological Transition refers to the shift in disease patterns as populations grow and densify. In early cities like Mohenjo-daro, crowded housing, poor sanitation, and stagnant water facilitated a transition from occasional infections to endemic epidemics like malaria, leading to demographic collapse."),
    ("Reconstruct the physical process of 'River Avulsion' and its impact on flat floodplains.", "River Avulsion is the rapid abandonment of an old river channel and the adoption of a new one. In flat plains, silt buildup raises the riverbed above the plain. During a flood or tectonic tilt, the river breaks its banks and shifts to a lower area miles away, leaving the original urban settlements dry.")
]:
    s2_mastery_eng.append({"type": "Teach Concept", "q": q, "sol": sol})

for q, sol in [
    ("नदी घाटियों के भू-वैज्ञानिक अध्ययन में 'सरोवरीय गाद' (Lacustrine) बनाम 'जलोढ़ गाद' (Alluvial) के अंतर को स्पष्ट करें।", "जलोढ़ गाद बहते पानी द्वारा लाई जाती है और खुरदरी होती है। सरोवरीय गाद शांत झीलों के नीचे जमा होती है और बहुत बारीक होती है। गाद का प्रकार पहचानने से बाढ़ के कारण (नदी बाढ़ या प्राकृतिक बांध झील) का पता चलता है।"),
    ("प्राचीन शहरी केंद्रों में 'महामारी संक्रमण' (Epidemiological Transition) की अवधारणा को समझाएं।", "आबादी बढ़ने और सघन होने पर बीमारियों के पैटर्न में होने वाले बदलाव को महामारी संक्रमण कहते हैं। मोहनजोदड़ो में खराब स्वच्छता और रुके पानी से मलेरिया जैसी बीमारियाँ महामारी बन गईं जिससे पूरी जनसंख्या समाप्त हो गई।"),
    ("नदी विवर्तन/विस्थापन (River Avulsion) की भौतिक प्रक्रिया और समतल मैदानों पर इसके प्रभाव का पुनर्निर्माण करें।", "नदी विवर्तन पुरानी धारा को छोड़कर नई धारा अपनाने की तीव्र प्रक्रिया है। समतल मैदानों में गाद जमने से नदी तल मैदान से ऊपर उठ जाता है। बाढ़ या भूकंप आने पर नदी तटबंध तोड़कर दूर चली जाती है, जिससे पुराने शहर सूखे पड़ जाते हैं।")
]:
    s2_mastery_hin.append({"type": "Teach Concept", "q": q, "sol": sol})


# =========================================================================
# SECTION 3: ARYAN INVASION, TRADE COLLAPSE, AND DECENTRALISATION THEORIES
# =========================================================================
s3_mastery_eng = []
s3_mastery_hin = []

# MCQ (5)
for q, opts, ans, sol in [
    ("Who popularized the Aryan Invasion Theory of Harappan decline in 1947?", ["Mortimer Wheeler", "John Marshall", "George Dales", "Shereen Ratnagar"], 0, "Mortimer Wheeler popularized the Aryan Invasion Theory in 1947, citing Rigvedic texts and skeletal remains."),
    ("Which Rigvedic term meaning 'destroyer of forts' was used by Wheeler to identify Indra as the destroyer of Harappan cities?", ["Purandara", "Gapati", "Vispati", "Rajanya"], 0, "Wheeler cited the epithet Purandara (destroyer of forts/pur) to argue that Vedic Aryans destroyed Harappan cities."),
    ("Shereen Ratnagar linked the decline of the Harappan Civilisation to the collapse of trade with which ancient region?", ["Mesopotamia", "Egypt", "China", "Central Asia"], 0, "Ratnagar argued that the collapse of long-distance trade with Mesopotamia (Meluhha) caused political and administrative decay."),
    ("What archeological culture succeeded the Mature Harappan culture in Sindh, representing urban decay?", ["Jhukar Culture", "Cemetery H Culture", "Ochre Coloured Pottery", "Malwa Culture"], 0, "The Jhukar culture succeeded the Mature Harappan phase in Sindh, characterized by crude pottery and loss of urban planning."),
    ("Which of the following is a key feature of the Late Harappan Cemetery H culture in Punjab?", ["Fractional burial in painted urns", "Standardized grid town planning", "Use of Rohri chert weights", "Inscribed steatite seals"], 0, "Cemetery H is characterized by fractional burials in painted urns, reflecting changed religious and material traits.")
]:
    s3_mastery_eng.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("1947 में हड़प्पा पतन के 'आर्य आक्रमण सिद्धांत' को किसने लोकप्रिय बनाया था?", ["मोंटीमर व्हीलर", "जॉन मार्शल", "जॉर्ज डेल्स", "शीरीन रत्नागर"], 0, "मोंटीमर व्हीलर ने 1947 में आर्य आक्रमण के सिद्धांत को लोकप्रिय बनाया था।"),
    ("व्हीलर ने इंद्र को हड़प्पा शहरों का विनाशक बताने के लिए किस ऋग्वैदिक शब्द (जिसका अर्थ 'किलों का नाशक' है) का उपयोग किया?", ["पुरंदर", "गपति", "विस्पति", "राजन्य"], 0, "व्हीलर ने इंद्र के विशेषण 'पुरंदर' का उल्लेख किया था।"),
    ("शीरीन रत्नागर ने हड़प्पा सभ्यता के पतन को किस प्राचीन क्षेत्र के साथ व्यापार बंद होने से जोड़ा?", ["मेसोपोटामिया", "मिस्र", "चीन", "मध्य एशिया"], 0, "रत्नागर ने मेसोपोटामिया (मेलुहा) के साथ होने वाले व्यापार के पतन को पतन का मुख्य कारण माना।"),
    ("सिंध में परिपक्व हड़प्पा संस्कृति के बाद कौन सी उत्तर हड़प्पा संस्कृति आई जो शहरी ह्रास को दर्शाती है?", ["झुकर संस्कृति", "सिमेट्री एच संस्कृति", "गेरूए रंग के मृदभांड", "मालवा संस्कृति"], 0, "सिंध में झुकर संस्कृति परिपक्व हड़प्पा के बाद आई जो पतन के पुरातात्विक साक्ष्य प्रस्तुत करती है।"),
    ("पंजाब में उत्तर हड़प्पा 'सिमेट्री एच' (Cemetery H) संस्कृति की प्रमुख विशेषता क्या है?", ["चित्रित कलशों में आंशिक शवाधान", "मानकीकृत ग्रिड नगर नियोजन", "रोहरी चर्ट के बाटों का उपयोग", "उत्कीर्ण सेलखड़ी की मुहरें"], 0, "सिमेट्री एच चित्रित कलशों में आंशिक शवाधान (fractional burial) के लिए जानी जाती है।")
]:
    s3_mastery_hin.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# Multiple Correct MCQ (5)
for q, opts, ans, sol in [
    ("Which of the following archaeological findings refute Wheeler's Aryan Invasion Theory? (Select all that apply)", ["Skeletons belonging to different stratigraphic layers", "Absence of weapon trauma or injuries on bone remains", "Total lack of horses and weapons of war in mature levels", "Complete burning of Mohenjo-daro citadel"], [0, 1, 2], "Skeletal layers, lack of trauma, and lack of horses/war weapons refute Wheeler. There was no burning of the citadel."),
    ("Select the Late Harappan regional cultures that emerged after the Mature phase: (Select all that apply)", ["Jhukar culture in Sindh", "Cemetery H culture in Punjab", "Late Harappan Gujarat (Rojdi/Rangpur)", "Jorwe culture in Maharashtra"], [0, 1, 2], "Jhukar, Cemetery H, and Gujarat Late Harappan are regional successors. Jorwe is a separate Chalcolithic culture of Deccan."),
    ("Which features characterize the de-urbanisation of the Late Harappan phase? (Select all that apply)", ["Disappearance of the script and writing system", "Abandonment of standardized Rohri chert weights", "Loss of uniform 4:2:1 brick proportions", "Increase in international trade contracts"], [0, 1, 2], "De-urbanisation is marked by loss of script, weights, and brick proportions. Trade decreased, not increased."),
    ("Select the Mesopotamian texts/records linked to Harappan trade: (Select all that apply)", ["Cuneiform tablets referencing Meluhha", "Sargon of Akkad's inscriptions on shipping", "Mentions of ivory and carnelian imports", "Hieroglyphic records of the Nile"], [0, 1, 2], "Cuneiform tablets, Sargon's inscriptions, and ivory/carnelian references link to Indus trade. Hieroglyphs are Egyptian."),
    ("Which of the following factors contributed to the collapse of administrative control according to Ratnagar? (Select all that apply)", ["Loss of procurement networks for raw materials", "Breakdown of the prestige-goods economy with Mesopotamia", "Loss of elite legitimacy and authority", "Adoption of Mesopotamian cuneiform script"], [0, 1, 2], "Loss of raw materials, prestige goods trade, and elite legitimacy led to administrative collapse. Cuneiform was never adopted.")
]:
    s3_mastery_eng.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("निम्नलिखित में से कौन से पुरातात्विक निष्कर्ष व्हीलर के आर्य आक्रमण सिद्धांत का खंडन करते हैं? (सभी सही विकल्प चुनें)", ["कंकालों का अलग-अलग ऐतिहासिक स्तरों से मिलना", "कंकाल अवशेषों पर हथियारों के घाव या आघात का अभाव", "परिपक्व स्तरों में घोड़ों और युद्ध के हथियारों का पूर्ण अभाव", "मोहनजोदड़ो के दुर्ग का पूरी तरह से जलाया जाना"], [0, 1, 2], "कंकाल के स्तर, घावों की कमी और घोड़ों/हथियारों की कमी व्हीलर का खंडन करते हैं। दुर्ग को जलाया नहीं गया था।"),
    ("परिपक्व चरण के बाद उभरने वाली उत्तर हड़प्पा क्षेत्रीय संस्कृतियों का चयन करें: (सभी सही विकल्प चुनें)", ["सिंध में झुकर संस्कृति", "पंजाब में सिमेट्री एच संस्कृति", "उत्तर हड़प्पा गुजरात (रोजदी/रंगपुर)", "महाराष्ट्र में जोर्वे संस्कृति"], [0, 1, 2], "झुकर, सिमेट्री एच और गुजरात उत्तर हड़प्पा संस्कृतियां हैं। जोर्वे दक्कन की ताम्रपाषाण संस्कृति थी।"),
    ("उत्तर हड़प्पा काल के वि-शहरीकरण (de-urbanisation) की विशेषताएं क्या हैं? (सभी सही विकल्प चुनें)", ["लिपि और लेखन प्रणाली का गायब होना", "मानकीकृत रोहरी चर्ट के बाटों का परित्याग", "समान 4:2:1 ईंट अनुपातों का लोप", "अंतरराष्ट्रीय व्यापार समझौतों में वृद्धि"], [0, 1, 2], "लिपि, बाट और ईंट अनुपात का अंत वि-शहरीकरण की पहचान हैं। व्यापार घटा था, बढ़ा नहीं।"),
    ("हड़प्पा व्यापार से जुड़े मेसोपोटामिया के अभिलेख/दस्तावेज कौन से हैं? (सभी सही विकल्प चुनें)", ["कीलाक्षर (cuneiform) लेख जिनमें 'मेलुहा' का जिक्र है", "अक्कड़ के सारगॉन के जहाजों से संबंधित शिलालेख", "हाथीदांत और अगेट के आयात का उल्लेख", "नील नदी के चित्रलिपि (hieroglyph) लेख"], [0, 1, 2], "कीलाक्षर, सारगॉन के लेख और आयात के संदर्भ सिंधु व्यापार से जुड़े हैं। चित्रलिपि मिस्र की है।"),
    ("रत्नागर के अनुसार प्रशासनिक नियंत्रण के पतन में किन कारकों ने योगदान दिया? (सभी सही विकल्प चुनें)", ["कच्चे माल के खरीद नेटवर्क का नष्ट होना", "मेसोपोटामिया के साथ विलासिता-वस्तु व्यापार का बंद होना", "शासक वर्ग की विश्वसनीयता और सत्ता का कमजोर होना", "मेसोपोटामिया की कीलाक्षर लिपि को अपनाना"], [0, 1, 2], "खरीद नेटवर्क का अंत, विलासिता व्यापार का पतन और सत्ता का कमजोर होना इसके कारण थे। कीलाक्षर को अपनाया नहीं गया था।")
]:
    s3_mastery_hin.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# True/False (8)
for q, ans, sol in [
    ("Mortimer Wheeler proposed the Aryan Invasion Theory based on skeletons found at Harappa.", False, "He based his massacre theory on skeletons found in the streets of Mohenjo-daro."),
    ("The Jhukar culture represents the transition to a ruralised chalcolithic economy.", True, "Jhukar represents a localized post-urban chalcolithic phase in Sindh."),
    ("Cuneiform tablets show that trade with Meluhha flourished up to 1500 BCE.", False, "Mentions of Meluhha ceased around 1900 BCE, indicating trade collapse."),
    ("George Dales proved that the Mohenjo-daro skeletons showed signs of healed wounds.", True, "Dales pointed out that some skeletons showed healed injuries, proving they did not die in a final war."),
    ("The Late Harappan phase saw an increase in the size and layout of planned cities.", False, "Cities were abandoned, and populations dispersed into small, unplanned rural villages."),
    ("The Cemetery H culture is named after a cemetery excavated at Harappa.", True, "Cemetery H is a Late Harappan burial ground excavated at the site of Harappa."),
    ("Iron weapons were found alongside skeletons, proving they were killed in battle.", False, "No iron was present; the Harappan Civilisation ended before the Iron Age began."),
    ("The loss of centralized authority led to a variation in local brick dimensions.", True, "With no central inspection, brick ratios drifted away from the standard 4:2:1.")
]:
    s3_mastery_eng.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("मोंटीमर व्हीलर ने हड़प्पा से मिले कंकालों के आधार पर आर्य आक्रमण सिद्धांत दिया था।", False, "उन्होंने अपना सिद्धांत मोहनजोदड़ो की सड़कों पर मिले कंकालों के आधार पर दिया था।"),
    ("झुकर संस्कृति एक ग्रामीण ताम्रपाषाण कालीन अर्थव्यवस्था के संक्रमण का प्रतिनिधित्व करती है।", True, "झुकर संस्कृति सिंध में उत्तर-शहरी ताम्रपाषाण चरण को दर्शाती है।"),
    ("मेसोपोटामिया के कीलाक्षर लेख दर्शाते हैं कि मेलुहा व्यापार 1500 ई.पू. तक समृद्ध था।", False, "1900 ई.पू. के बाद मेलुहा का उल्लेख समाप्त हो गया जो व्यापार पतन का सूचक है।"),
    ("जॉर्ज डेल्स ने सिद्ध किया कि मोहनजोदड़ो के कंकालों पर ठीक हो चुके घावों के निशान थे।", True, "डेल्स ने दर्शाया कि चोटें पुरानी थीं, जिससे साबित होता है कि वे युद्ध में नहीं मरे थे।"),
    ("उत्तर हड़प्पा काल में नियोजित शहरों के आकार और विन्यास में भारी वृद्धि हुई।", False, "शहरों का परित्याग कर लोग छोटी ग्रामीण बस्तियों में फैल गए।"),
    ("सिमेट्री एच संस्कृति का नाम हड़प्पा में खोदे गए एक कब्रिस्तान के नाम पर रखा गया है।", True, "सिमेट्री एच हड़प्पा स्थल पर खोजा गया उत्तर हड़प्पा कालीन कब्रिस्तान है।"),
    ("कंकालों के पास लोहे के हथियार मिले, जो साबित करते हैं कि वे युद्ध में मारे गए थे।", False, "लोहे का अस्तित्व नहीं था; हड़प्पा काल लोह युग से काफी पहले समाप्त हो गया था।"),
    ("केंद्रीय नियंत्रण समाप्त होने से स्थानीय स्तर पर ईंटों के आकारों में भिन्नता आने लगी।", True, "निरीक्षण के अभाव में मानक 4:2:1 अनुपात वाली ईंटों का उपयोग बंद हो गया।")
]:
    s3_mastery_hin.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

# Fill in the Blank (8)
for q, ans, sol in [
    ("Mortimer Wheeler popularized the theory of an invasion of Indus cities by the ________.", "Aryans", "Wheeler blamed the Aryans for destroying Indus cities."),
    ("The Rigvedic god Indra is referred to as ________, meaning destroyer of forts.", "Purandara", "Purandara was the Rigvedic epithet used for Indra."),
    ("Shereen Ratnagar linked administrative decay to the collapse of trade with ________.", "Mesopotamia", "The collapse of Mesopotamian trade undermined elite authority."),
    ("The regional successor culture that appeared in Sindh was the ________ culture.", "Jhukar", "Jhukar culture succeeded the mature phase in Sindh."),
    ("The Cemetery H culture is located at the site of ________.", "Harappa", "Cemetery H was excavated at Harappa in Punjab."),
    ("The Late Harappan phase is marked by the complete absence of the Indus ________.", "script", "Writing and the script completely disappeared in the post-urban phase."),
    ("Skeletons found at Mohenjo-daro belonged to different ________ layers, refuting a single massacre.", "stratigraphic", "Stratigraphic levels show they did not die in a single event."),
    ("In Late Harappan Gujarat, planned town layouts were replaced by ________ villages.", "unplanned", "Urban planning collapsed, replaced by unplanned agrarian settlements.")
]:
    s3_mastery_eng.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("मोंटीमर व्हीलर ने सिंधु शहरों पर ________ द्वारा किए गए आक्रमण के सिद्धांत को लोकप्रिय बनाया।", "आर्यों", "व्हीलर ने आर्यों को हड़प्पा विनाश के लिए उत्तरदायी माना था।"),
    ("ऋग्वैदिक देवता इंद्र को ________ कहा गया है, जिसका अर्थ है किलों का नाशक।", "पुरंदर", "इंद्र का ऋग्वैदिक विशेषण पुरंदर (किलों का नाशक) था।"),
    ("शीरीन रत्नागर ने प्रशासनिक पतन को ________ के साथ व्यापार टूटने से जोड़ा।", "मेसोपोटामिया", "मेसोपोटामियाई व्यापार बंद होने से शासकों का नियंत्रण टूट गया।"),
    ("सिंध क्षेत्र में विकसित होने वाली उत्तर हड़प्पा संस्कृति ________ संस्कृति थी।", "झुकर", "झुकर संस्कृति सिंध में परिपक्व चरण के बाद आई थी।"),
    ("सिमेट्री एच (Cemetery H) नामक उत्तर हड़प्पा कब्रिस्तान ________ स्थल पर मिला है।", "हड़प्पा", "सिमेट्री एच कब्रिस्तान पंजाब के हड़प्पा स्थल पर स्थित है।"),
    ("उत्तर हड़प्पा काल की सबसे बड़ी विशेषता सिंधु ________ का पूर्ण लोप होना है।", "लिपि", "उत्तर शहरी चरण में लिपि और लेखन का पूर्ण लोप हो गया था।"),
    ("मोहनजोदड़ो के कंकाल अलग-अलग ________ स्तरों में दबे मिले, जो एक ही नरसंहार का खंडन करता है।", "ऐतिहासिक", "स्तरिकी (stratigraphy) दर्शाती है कि मौतें अलग-अलग समय पर हुई थीं।"),
    ("उत्तर हड़प्पा गुजरात में नियोजित नगरों के स्थान पर ________ बस्तियों का उदय हुआ।", "अनियोजित", "नियोजित नगरों के स्थान पर अनियोजित ग्रामीण गाँवों का उदय हुआ।")
]:
    s3_mastery_hin.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

# Match the Following (3)
s3_matches_eng = [
    {"q": "Match the Late Harappan regional culture with its geographic location:",
     "pairs": ["Jhukar Culture - Sindh province", "Cemetery H Culture - Punjab (Harappa)", "OCP (Ochre Coloured Pottery) - Gangetic Doab", "Lustrous Red Ware Culture - Gujarat (Rangpur)"],
     "sol": "Jhukar is in Sindh; Cemetery H in Punjab; OCP in Gangetic Doab; Lustrous Red Ware in Gujarat."},
    {"q": "Match the historical scholar with their critical hypothesis:",
     "pairs": ["Mortimer Wheeler - Blamed Rigvedic Aryans for destroying Indus citadels", "George Dales - Refuted massacre by proving skeletons were proper burials", "Shereen Ratnagar - Argued that loss of luxury prestige trade ruined central control", "John Marshall - Attributed decline to environmental changes and flooding"],
     "sol": "Wheeler proposed Aryans; Dales refuted massacre; Ratnagar proposed trade collapse; Marshall proposed floods/environment."},
    {"q": "Match the material trait with its transitional phase status:",
     "pairs": ["Standardized Chert Weights - Mature Harappan urban standard", "Localized Stone Weights - Late Harappan decentralized standard", "Inscribed Steatite Seals - Mature Harappan administrative seal", "Geometric Clay Seals - Late Harappan Jhukar culture seal"],
     "sol": "Chert weights were Mature; local weights were Late; steatite seals were Mature; clay seals were Jhukar."}
]
s3_mastery_eng.extend([make_match_question(m) for m in s3_matches_eng])

s3_matches_hin = [
    {"q": "उत्तर हड़प्पा क्षेत्रीय संस्कृतियों को उनके भौगोलिक क्षेत्रों से सुमेलित करें:",
     "pairs": ["झुकर संस्कृति - सिंध प्रांत", "सिमेट्री एच संस्कृति - पंजाब (हड़प्पा)", "गेरूए रंग के मृदभांड (OCP) - गंगा दोआब", "चमकीले लाल मृदभांड (Lustrous) - गुजरात (रंगपुर)"],
     "sol": "झुकर सिंध में; सिमेट्री एच पंजाब में; OCP गंगा दोआब में; चमकीले लाल मृदभांड गुजरात में विकसित हुए।"},
    {"q": "ऐतिहासिक विद्वानों को उनकी आलोचनात्मक परिकल्पनाओं से सुमेलित करें:",
     "pairs": ["मोंटीमर व्हीलर - हड़प्पा दुर्गों के विनाश का दोष ऋग्वैदिक आर्यों पर मढ़ा", "जॉर्ज डेल्स - साबित किया कि कंकाल नरसंहार नहीं बल्कि शवाधान का हिस्सा थे", "शीरीन रत्नागर - विलासिता व्यापार बंद होने से केंद्रीय नियंत्रण टूटने का तर्क दिया", "जॉन मार्शल - पतन का कारण पर्यावरणीय परिवर्तनों और बाढ़ को माना"],
     "sol": "व्हीलर ने आर्य आक्रमण; डेल्स ने शवाधान दफन; रत्नागर ने व्यापार पतन; मार्शल ने बाढ़/पर्यावरण का तर्क दिया।"},
    {"q": "पुरातात्विक सामग्री को उसकी संक्रमणकालीन स्थिति से सुमेलित करें:",
     "pairs": ["मानकीकृत चर्ट बाट - परिपक्व हड़प्पा शहरी मानक", "स्थानीय पत्थर के बाट - उत्तर हड़प्पा विकेंद्रीकृत मानक", "उत्कीर्ण सेलखड़ी मुहरें - परिपक्व हड़प्पा प्रशासनिक मुहर", "ज्यामितीय मिट्टी की मुहरें - उत्तर हड़प्पा झुकर संस्कृति मुहर"],
     "sol": "चर्ट बाट परिपक्व काल के; स्थानीय बाट उत्तर काल के; सेलखड़ी मुहर परिपक्व काल की; मिट्टी की मुहर झुकर काल की है।"}
]
s3_mastery_hin.extend([make_match_question(m) for m in s3_matches_hin])

# One-Liner (8)
for q, sol in [
    ("Why did Wheeler call Indra the destroyer of Harappan cities?", "Indra is called Purandara (destroyer of pur/forts) in the Rigveda, which Wheeler equated with Harappan citadels."),
    ("What stratigraphic error did Wheeler make at Mohenjo-daro?", "He grouped skeletons from different stratigraphic levels together as if they died in a single massacre."),
    ("Why did the Mesopotamian trade collapse hurt the Harappan elites?", "Elites maintained power by distributing imported prestige luxury goods; when trade stopped, their political authority collapsed."),
    ("What does the Jhukar culture pottery look like compared to Mature Harappan pottery?", "It is coarser, wheel-turned red ware with simple black geometric paintings, lacking the sophisticated animal designs."),
    ("What is fractional burial, as seen in the Cemetery H culture?", "It is the burial of bones after the body has been exposed to nature, placed inside large urns painted with peacocks and stars."),
    ("Why did the centralized inspection of weight standards cease in 1900 BCE?", "The municipal governments collapsed, removing the administrative inspectors who verified weights."),
    ("Where did the copper hoards of the Gangetic valley originate from in terms of culture?", "They are associated with the Ochre Coloured Pottery (OCP) culture, which has Late Harappan influences."),
    ("What happened to the layout of houses in the late phases of Mohenjo-daro?", "Large courtyards were subdivided into tiny slums, and streets were blocked by kilns, indicating urban decay.")
]:
    s3_mastery_eng.append({"type": "One-Liner", "q": q, "sol": sol})

for q, sol in [
    ("व्हीलर ने इंद्र को हड़प्पा के शहरों का विनाशक क्यों कहा था?", "ऋग्वेद में इंद्र को पुरंदर (किलों का नाशक) कहा गया है, जिसे व्हीलर ने हड़प्पा के दुर्गों (citadels) से जोड़ दिया।"),
    ("व्हीलर ने मोहनजोदड़ो में क्या स्तरिकी (stratigraphic) त्रुटि की थी?", "उन्होंने अलग-अलग ऐतिहासिक स्तरों पर मिले कंकालों को एक साथ जोड़कर एक ही बड़े नरसंहार का दावा कर दिया।"),
    ("मेसोपोटामियाई व्यापार के पतन ने हड़प्पा के शासक वर्ग को कैसे चोट पहुंचाई?", "शासक विलासिता की वस्तुओं के वितरण से अपनी सत्ता बनाए रखते थे; व्यापार बंद होने पर उनका नियंत्रण समाप्त हो गया।"),
    ("परिपक्व हड़प्पा बर्तनों की तुलना में झुकर संस्कृति के बर्तन कैसे दिखते हैं?", "वे अधिक खुरदरे हैं, जिन पर जटिल पशु चित्रों के स्थान पर केवल सरल ज्यामितीय आकृतियाँ चित्रित हैं।"),
    ("सिमेट्री एच संस्कृति में देखे जाने वाले आंशिक शवाधान (fractional burial) का क्या अर्थ है?", "खुले में शरीर सड़ने के बाद बची हड्डियों को एकत्रित कर मोर और तारों से चित्रित कलशों में भरकर दफनाना।"),
    ("1900 ई.पू. में बाट मानकों का केंद्रीय निरीक्षण क्यों बंद हो गया था?", "नगरपालिका सरकारें नष्ट हो गईं, जिससे बाटों का सत्यापन करने वाले सरकारी निरीक्षकों का अस्तित्व समाप्त हो गया।"),
    ("संस्कृति के संदर्भ में गंगा घाटी के ताम्र निधियों (copper hoards) का उद्गम कहाँ से माना जाता है?", "वे गेरूए रंग के मृदभांड (OCP) संस्कृति से संबंधित हैं, जिस पर उत्तर हड़प्पा का प्रभाव था।"),
    ("मोहनजोदड़ो के अंतिम चरणों में मकानों के विन्यास में क्या बदलाव आया?", "बड़े आँगनों को छोटी झुग्गियों में बाँट दिया गया और सड़कों पर ईंट भट्ठियाँ बना दी गईं जो शहरी पतन को दर्शाती हैं।")
]:
    s3_mastery_hin.append({"type": "One-Liner", "q": q, "sol": sol})

# Assertion-Reason (8)
for q, ans, sol in [
    ("Assertion (A): Mortimer Wheeler declared Indra as the destroyer of Harappan cities.\nReason (R): Rigvedic texts frequently describe Indra destroying 'pur' or fortified settlements.", 0, "Both are true, and R is the reason Wheeler (A) accused Indra and the Aryans."),
    ("Assertion (A): The Aryan invasion theory is rejected by modern historians.\nReason (R): Stratigraphic analysis shows that skeletons found at Mohenjo-daro did not die at the same time and show no trauma from weapons.", 0, "Both are true, and R is the direct scientific reason why A is rejected."),
    ("Assertion (A): Shereen Ratnagar proposed that a decline in rainfall destroyed Harappan cities.\nReason (R): Mentions of Meluhha cease in Mesopotamian records around 1900 BCE.", 3, "A is false. Ratnagar proposed Trade Collapse, not aridity/rainfall. R is true."),
    ("Assertion (A): The Late Harappan period is marked by the disintegration of a pan-regional material uniformity.\nReason (R): Successor regional cultures like Jhukar and Cemetery H show localized pottery, burial, and architectural patterns.", 0, "Both are true, and R explains why there was a loss of pan-regional uniformity (A)."),
    ("Assertion (A): Iron swords and chariots were used by the defenders of Mohenjo-daro against invaders.\nReason (R): The Harappan civilization belonged to the Bronze Age and did not use iron tools.", 3, "A is false. No iron or war chariots existed in Harappa. R is true."),
    ("Assertion (A): The distinctive Harappan script ceased to be used after 1900 BCE.\nReason (R): The collapse of long-distance trade and centralized state administrations removed the administrative utility of writing.", 0, "Both are true, and R explaining why the script fell out of use (A)."),
    ("Assertion (A): Late Harappan Cemetery H culture is characterized by fractional burials in painted urns.\nReason (R): Harappa was completely abandoned and no burials occurred after 1900 BCE.", 2, "A is true. R is false because Cemetery H represents the post-urban phase at Harappa."),
    ("Assertion (A): The civic standards of Mohenjo-daro deteriorated in the Late Harappan phase.\nReason (R): Kilns were constructed in the middle of streets, and domestic waste choked the main channels.", 0, "Both are true, and R is the physical evidence showing the civic deterioration (A).")
]:
    s3_mastery_eng.append({"type": "Assertion-Reason", "q": q, "opts": ar_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("कथन (A): मोंटीमर व्हीलर ने इंद्र को हड़प्पा के शहरों का विनाशक घोषित किया।\nकारण (R): ऋग्वैदिक ग्रंथ अक्सर इंद्र को 'पुर' या किलाबंद बस्तियों को नष्ट करने वाले के रूप में वर्णित करते हैं।", 0, "दोनों सत्य हैं और R, A की सही व्याख्या करता है।"),
    ("कथन (A): आधुनिक इतिहासकारों द्वारा आर्य आक्रमण सिद्धांत को खारिज कर दिया गया है।\nकारण (R): स्तरिकी विश्लेषण दर्शाता है कि मोहनजोदड़ो के कंकाल एक ही समय के नहीं हैं और उन पर हथियारों की चोटें नहीं हैं।", 0, "दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): शीरीन रत्नागर ने प्रस्ताव दिया कि वर्षा में गिरावट ने हड़प्पा के शहरों को नष्ट कर दिया।\nकारण (R): मेसोपोटामिया के अभिलेखों में 1900 ई.पू. के आसपास मेलुहा का उल्लेख समाप्त हो जाता है।", 3, "A गलत है। रत्नागर ने व्यापार पतन का सिद्धांत दिया था, शुष्कता का नहीं। R सही है।"),
    ("कथन (A): उत्तर हड़प्पा काल अखिल-क्षेत्रीय (pan-regional) भौतिक एकरूपता के टूटने से चिह्नित है।\nकारण (R): झुकर और सिमेट्री एच जैसी उत्तराधिकारी क्षेत्रीय संस्कृतियां स्थानीय मृदभांड और वास्तुकला पैटर्न प्रदर्शित करती हैं।", 0, "दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): मोहनजोदड़ो के रक्षकों ने आक्रमणकारियों के खिलाफ लोहे की तलवारों और रथों का इस्तेमाल किया था।\nकारण (R): हड़प्पा सभ्यता कांस्य युग से संबंधित थी और उसे लोहे का ज्ञान नहीं था।", 3, "A गलत है। लोहा और रथ नहीं थे। R सही है।"),
    ("कथन (A): 1900 ई.पू. के बाद विशिष्ट हड़प्पा लिपि का उपयोग बंद हो गया।\nकारण (R): दीर्घकालिक व्यापार और केंद्रीकृत राज्यों के पतन ने लेखन की प्रशासनिक उपयोगिता को समाप्त कर दिया।", 0, "दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): उत्तर हड़प्पा सिमेट्री एच संस्कृति की विशेषता चित्रित कलशों में आंशिक शवाधान है।\nकारण (R): 1900 ई.पू. के बाद हड़प्पा को पूरी तरह से छोड़ दिया गया था और वहां कोई शवाधान नहीं हुआ।", 2, "A सत्य है पर R गलत है क्योंकि सिमेट्री एच हड़प्पा में ही उत्तर शहरी बस्तियों को दर्शाती है।"),
    ("कथन (A): उत्तर हड़प्पा काल में मोहनजोदड़ो के नागरिक मानकों में भारी गिरावट आई।\nकारण (R): सड़कों के बीचों-बीच भट्टियाँ बनाई गईं और घरेलू कचरे से मुख्य नालियाँ बंद हो गईं।", 0, "दोनों सत्य हैं और R, A की सही व्याख्या है।")
]:
    s3_mastery_hin.append({"type": "Assertion-Reason", "q": q, "opts": hin_ar_opts, "ans": ans, "sol": sol})

# Statement-Based (5)
for q, ans, sol in [
    ("Consider the following statements regarding the Aryan Invasion Theory:\n1. It was first suggested by R.P. Chanda in 1926 and later popularized by Wheeler in 1947.\n2. Skeletons lying in the streets of Mohenjo-daro were found with iron weapons, confirming battle.\nWhich of the statement(s) is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect; no weapons of war or iron were found alongside the skeletons."),
    ("Consider the following statements regarding trade collapse theory:\n1. Shereen Ratnagar argued that the termination of maritime trade with Ur and Kish ruined Harappan state control.\n2. Mentions of Meluhha continue in Mesopotamian texts up to the Persian period.\nWhich of the statement(s) is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect; mentions of Meluhha ceased around 1900 BCE."),
    ("Consider the following statements regarding Late Harappan regional cultures:\n1. Jhukar culture is characterized by circular copper stamp seals and geometric designs.\n2. Cemetery H culture represents the ruralised chalcolithic phase in Sindh.\nWhich of the statement(s) is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect; Cemetery H represents the phase in Punjab (Harappa), while Jhukar represents Sindh."),
    ("Consider the following statements regarding the transition to Chalcolithic phase:\n1. The de-urbanisation of Harappa led to the return of localized barter systems.\n2. Large granaries disappeared, replaced by household grain storage pits.\nWhich of the statement(s) is/are correct?", 2, "Both statements are correct. Standardized state storage (granaries) vanished, and trade returned to local barter levels."),
    ("Consider the following statements regarding Rigvedic terms:\n1. Indra's epithet 'Purandara' refers specifically to the destruction of stone temples.\n2. Skeletons at Mohenjo-daro showed healed fractures, proving they lived after receiving injuries.\nWhich of the statement(s) is/are correct?", 1, "Statement 1 is incorrect; Purandara refers to the destroyer of forts (pur), not stone temples. Statement 2 is correct; paleopathological analysis proved injuries were healed.")
]:
    s3_mastery_eng.append({"type": "Statement-Based", "q": q, "opts": mcq_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("आर्य आक्रमण सिद्धांत के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. यह सबसे पहले 1926 में आर.पी. चंदा द्वारा सुझाया गया था और बाद में 1947 में व्हीलर द्वारा लोकप्रिय बनाया गया।\n2. मोहनजोदड़ो की सड़कों पर मिले कंकालों के पास लोहे के हथियार मिले जो युद्ध की पुष्टि करते हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि लोहे के हथियार नहीं मिले थे।"),
    ("व्यापारिक पतन के सिद्धांत के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. शीरीन रत्नागर ने तर्क दिया कि उर और किश के साथ व्यापार बंद होने से हड़प्पा राज्य का नियंत्रण टूट गया।\n2. मेसोपोटामिया के ग्रंथों में फारसी काल तक मेलुहा का उल्लेख मिलता रहा।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि 1900 ई.पू. के बाद मेलुहा का उल्लेख बंद हो गया था।"),
    ("उत्तर हड़प्पा क्षेत्रीय संस्कृतियों के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. झुकर संस्कृति की विशेषता गोलाकार तांबे की मुहरें और ज्यामितीय डिजाइन हैं।\n2. सिमेट्री एच संस्कृति सिंध में ग्रामीण ताम्रपाषाण चरण का प्रतिनिधित्व करती है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि सिमेट्री एच पंजाब (हड़प्पा) में थी, सिंध में झुकर थी।"),
    ("ताम्रपाषाण काल में संक्रमण के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. हड़प्पा के वि-शहरीकरण से स्थानीय वस्तु विनिमय प्रणालियाँ पुनः प्रभावी हो गईं।\n2. विशाल राजकीय अन्नागार समाप्त हो गए और उनकी जगह घरेलू अनाज गड्ढों ने ले ली।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 2, "दोनों कथन सही हैं। अन्नागार समाप्त हुए और व्यापार स्थानीय वस्तु विनिमय में बदल गया।"),
    ("ऋग्वैदिक पदों के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. इंद्र का विशेषण 'पुरंदर' विशेष रूप से पत्थर के मंदिरों के विनाश को संदर्भित करता है।\n2. मोहनजोदड़ो के कंकालों पर चोटें ठीक होने के निशान थे, जिससे सिद्ध होता है कि वे चोट लगने के बाद जीवित रहे थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 1, "कथन 1 गलत है क्योंकि पुरंदर का अर्थ किलों का नाशक है, पत्थर के मंदिरों का नहीं। कथन 2 सही है।")
]:
    s3_mastery_hin.append({"type": "Statement-Based", "q": q, "opts": hin_mcq_opts, "ans": ans, "sol": sol})

# Why (3)
for q, sol in [
    ("Why did Shereen Ratnagar argue that the collapse of Mesopotamian trade caused systemic collapse?", "She argued that Harappan rulers depended on imported luxury prestige goods to maintain social status and administrative control. When Mesopotamian trade collapsed, the ruling elites lost the ability to distribute prestige goods, leading to the decay of the state machinery."),
    ("Why was Mortimer Wheeler's skeletal evidence for an invasion criticized by modern archeologists?", "Modern stratigraphic analysis proved that the 37 skeletons did not belong to a single event or layer. They were scattered across different occupational periods. Furthermore, there was an absence of weapon trauma and no horse remains or foreign weapons nearby."),
    ("Why did the Harappan script and writing system disappear during the Late Harappan phase?", "Writing is a tool used by centralized administrations for tax records, trade accounting, and official seals. When the cities collapsed and trade became localized and agrarian, the state machinery disappeared, removing the practical utility of writing.")
]:
    s3_mastery_eng.append({"type": "Why", "q": q, "sol": sol})

for q, sol in [
    ("शीरीन रत्नागर ने यह क्यों तर्क दिया कि मेसोपोटामियाई व्यापार बंद होने से व्यवस्था ढह गई?", "उनका तर्क था कि हड़प्पा के शासक विलासिता के आयातित सामानों के वितरण से अपनी सामाजिक स्थिति और सत्ता बनाए रखते थे। व्यापार बंद होने पर उनकी शक्ति समाप्त हो गई जिससे प्रशासनिक व्यवस्था चरमरा गई।"),
    ("आक्रमण के साक्ष्य के रूप में व्हीलर द्वारा प्रस्तुत कंकाल साक्ष्यों की आधुनिक पुरातत्वविदों ने आलोचना क्यों की?", "आधुनिक स्तरिकी विश्लेषण ने साबित किया कि वे 37 कंकाल एक ही समय के नहीं थे बल्कि अलग-अलग कालों के थे। उन पर हथियारों की चोटें नहीं थीं और युद्ध के कोई भी उपकरण आसपास नहीं मिले।"),
    ("उत्तर हड़प्पा काल के दौरान सिंधु लिपि और लेखन प्रणाली क्यों गायब हो गई?", "लेखन का उपयोग केंद्रीकृत प्रशासन द्वारा करों, व्यापार खातों और सरकारी मुहरों के लिए किया जाता था। शहरों के ढहने और व्यापार के स्थानीय कृषि स्तर पर लौटने से लेखन की आवश्यकता समाप्त हो गई।")
]:
    s3_mastery_hin.append({"type": "Why", "q": q, "sol": sol})

# How (3)
for q, sol in [
    ("How does the Jhukar culture demonstrate a decline in craftsmanship compared to the Mature Harappan phase?", "Jhukar pottery is coarser, wheel-made but poorly fired, and lacks the smooth slip and intricate designs of the Mature phase. The seals changed from carved steatite squares with scripts and animals to crude circular clay stamps with simple geometric markings."),
    ("How did de-urbanisation lead to the regionalisation of cultures in Western India?", "When central cities collapsed, regional communities lost contact with the pan-regional standards. They developed local styles of pottery, burial, and craft, breaking the uniformity and creating regional cultures like Jhukar in Sindh and Cemetery H in Punjab."),
    ("How did the abandonment of weight standards impact internal trade during the Late Harappan phase?", "Without centralized inspection and uniform chert weights, traders had to rely on local stone and clay weights. This increased transaction costs, limited trade to localized areas, and dismantled the standardized inter-regional commercial network.")
]:
    s3_mastery_eng.append({"type": "How", "q": q, "sol": sol})

for q, sol in [
    ("झुकर संस्कृति परिपक्व हड़प्पा की तुलना में शिल्पकला में गिरावट को कैसे प्रदर्शित करती है?", "झुकर के बर्तन मोटे, कम पके और साधारण चित्रों वाले थे। परिपक्व काल की सुंदर चौकोर सेलखड़ी की मुहरों के स्थान पर झुकर काल में मिट्टी की खुरदरी गोल मुहरें मिलीं जिन पर केवल ज्यामितीय रेखाएं खुदी थीं।"),
    ("वि-शहरीकरण (de-urbanisation) के कारण पश्चिमी भारत में संस्कृतियों का क्षेत्रीयकरण कैसे हुआ?", "केंद्रीय शहरों के नष्ट होने पर विभिन्न क्षेत्र अखिल-भारतीय मानकों से कट गए। उन्होंने मिट्टी के बर्तनों और कलाकृतियों की अपनी स्थानीय शैलियाँ विकसित कीं, जिससे सिंध में झुकर और पंजाब में सिमेट्री एच जैसी क्षेत्रीय संस्कृतियां उभरीं।"),
    ("बाट मानकों के परित्याग ने उत्तर हड़प्पा काल में आंतरिक व्यापार को कैसे प्रभावित किया?", "केंद्रीय नियंत्रण और चर्ट के बाटों के गायब होने से व्यापारियों को स्थानीय पत्थरों और मिट्टी के मनमाने बाटों पर निर्भर रहना पड़ा, जिससे व्यापार स्थानीय स्तर पर सिमट गया और अंत-क्षेत्रीय व्यापार नष्ट हो गया।")
]:
    s3_mastery_hin.append({"type": "How", "q": q, "sol": sol})

# Case Study (3)
for q, sol in [
    ("Examine the 'Jhukar Phase at Chanhudaro' as a case study for urban decay.", "Chanhudaro (Sindh) shows a clear transition from Mature Harappan to the Jhukar phase. Excavations show that the planned drainage system was abandoned. Houses were built on top of old debris without grid alignment, using reused bricks, and kilns blocked streets, presenting a classic case study of urban decay."),
    ("Analyze Sargon of Akkad's inscriptions as a case study for Mesopotamian trade collapse.", "Inscriptions of Sargon of Akkad (c. 2350 BCE) brag about ships from Meluhha, Magan, and Dilmun docking at Akkad's ports. In contrast, post-1900 BCE Mesopotamian texts lack any reference to Meluhha. This case study confirms that maritime trade with the Indus Valley collapsed, directly impacting the Harappan economy."),
    ("Examine Harappa's 'Cemetery HUrn Burials' as a case study of cultural transformation.", "Cemetery H represents the successor culture at Harappa. In contrast to mature extended burials, Cemetery H features fractional burials in large urns painted with complex stars, flying peacocks, and human figures, showing a case study of changed religious and funerary ideas.")
]:
    s3_mastery_eng.append({"type": "Case Study", "q": q, "sol": sol})

for q, sol in [
    ("शहरी पतन के केस स्टडी के रूप में चन्हुदड़ो में 'झुकर चरण' का परीक्षण करें।", "चन्हुदड़ो (सिंध) परिपक्व हड़प्पा से झुकर काल के बदलाव को दर्शाता है। यहाँ नियोजित जल निकासी व्यवस्था बंद कर दी गई थी। मकान ग्रिड योजना के बिना पुरानी ईंटों को जोड़कर बनाए गए थे और सड़कों पर भट्टियां बनी थीं जो शहरी पतन का प्रमाण हैं।"),
    ("मेसोपोटामियाई व्यापार पतन के केस स्टडी के रूप में अक्कड़ के सारगॉन (Sargon of Akkad) के शिलालेखों का विश्लेषण करें।", "सारगॉन के अभिलेखों (2350 ई.पू.) में अक्कड़ बंदरगाहों पर मेलुहा के जहाजों के रुकने का गर्व से उल्लेख है। पर 1900 ई.पू. के बाद के ग्रंथों में मेलुहा का कोई उल्लेख नहीं मिलता, जो समुद्री व्यापार के पूर्ण पतन की पुष्टि करता है।"),
    ("सांस्कृतिक परिवर्तन के केस स्टडी के रूप में हड़प्पा के 'सिमेट्री एच कलश शवाधान' (Urn Burials) का परीक्षण करें।", "सिमेट्री एच हड़प्पा की उत्तराधिकारी संस्कृति है। यहाँ परिपक्व काल के सीधे दफनाने के स्थान पर कलशों में आंशिक हड्डियाँ भरकर दफनाने की प्रथा मिली है, जिन पर मोर और तारों के चित्र बने हैं जो धार्मिक बदलाव को दर्शाते हैं।")
]:
    s3_mastery_hin.append({"type": "Case Study", "q": q, "sol": sol})

# Teach Concept (3)
for q, sol in [
    ("Explain the concept of 'Systemic State Collapse' as applied to Bronze Age civilisations.", "Systemic State Collapse is the complete breakdown of central administrative, political, and economic control. In Harappa, it is marked by the simultaneous disappearance of the script, municipal drainage, standardised weights, and brick ratios across 1 million sq km, leaving local communities to adapt independently."),
    ("Describe the process of 'Ruralisation' (De-urbanisation) in archaeological terms.", "Ruralisation is the shift of a society's baseline from city-dwelling and craft-specialisation to village-based farming and animal husbandry. In archaeology, it is documented by the abandonment of planned cities, a decrease in site size, loss of luxury crafts, and emergence of agrarian villages."),
    ("Reconstruct the economic dynamics of 'Prestige-Goods Economy' and its vulnerability to trade disruption.", "In a Prestige-Goods Economy, rulers maintain status by controlling and distributing rare, imported luxury items (like lapis lazuli or carnelian). If trade routes are disrupted, the rulers lose access to these items. They can no longer reward subordinates or show status, causing the administrative structure to fall apart.")
]:
    s3_mastery_eng.append({"type": "Teach Concept", "q": q, "sol": sol})

for q, sol in [
    ("कांस्य युगीन सभ्यताओं के संदर्भ में 'व्यवस्थागत राज्य पतन' (Systemic State Collapse) की अवधारणा को स्पष्ट करें।", "यह केंद्रीय प्रशासनिक, राजनीतिक और आर्थिक नियंत्रण के पूरी तरह बिखरने की स्थिति है। हड़प्पा में 10 लाख वर्ग किमी में एक साथ लिपि, बाट प्रणाली, ईंट अनुपात और नालियों का बंद होना व्यवस्थागत पतन को दर्शाता है।"),
    ("पुरातात्विक शब्दावली में 'ग्रामीणकरण' (De-urbanisation/Ruralisation) की प्रक्रिया का वर्णन करें।", "यह शहरों को छोड़कर कृषि प्रधान ग्रामीण बस्तियों में बसने की प्रक्रिया है। पुरातत्व में इसे नियोजित नगरों के परित्याग, बस्तियों के छोटे आकार, विलासिता शिल्पों के अंत और कृषि आधारित गाँवों के उदय से मापा जाता है।"),
    ("विलासिता-वस्तु आधारित अर्थव्यवस्था ('Prestige-Goods Economy') के आर्थिक चक्र और व्यापार व्यवधान के प्रति इसकी संवेदनशीलता को समझाएं।", "इस अर्थव्यवस्था में शासक आयातित विलासिता वस्तुओं के वितरण से अपनी सत्ता बनाए रखते हैं। जब बाहरी व्यापार बंद हो जाता है, तो वे अधीनस्थों को खुश करने में असमर्थ हो जाते हैं, जिससे प्रशासनिक पकड़ ढीली हो जाती है।")
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
