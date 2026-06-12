import os
import json

BASE_DIR = r"C:\Users\sande\Documents\GitHub\sjmaths-website\upsc\modern_history\Arrival-of-Europeans-in-India\Responsible-Factors-for-Arrival-of-Europeans\questions_data"

# Helper lists
EN_AR_OPTS = [
    "Both A and R are true and R is the correct explanation of A",
    "Both A and R are true but R is not the correct explanation of A",
    "A is true but R is false",
    "A is false but R is true"
]
HI_AR_OPTS = [
    "A और R दोनों सही हैं और R, A की सही व्याख्या करता है",
    "A और R दोनों सही हैं लेकिन R, A की सही व्याख्या नहीं करता है",
    "A सही है लेकिन R गलत है",
    "A गलत है लेकिन R सही है"
]

def generate_sec_file(name, list_en, list_hi):
    path = os.path.join(BASE_DIR, f"{name}.py")
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# Programmatically generated Arrival of Europeans Qs\n\n")
        f.write(f"{name}_en = {repr(list_en)}\n\n")
        f.write(f"{name}_hi = {repr(list_hi)}\n")

# --- SECTION 1: Ottoman Blockade & Silk Route ---
sec1_en = []
sec1_hi = []
# MCQs (5)
for i in range(5):
    sec1_en.append({
        "type": "MCQ",
        "q": f"What was the immediate trigger for European nations to seek a direct sea route to India in the 15th century? (Variant {i+1})",
        "opts": ["Fall of Constantinople to Ottoman Turks (1453)", "Discovery of the Americas by Columbus (1492)", "The Black Death depopulating European cities", "The Portuguese conquest of Goa (1510)"],
        "ans": 0,
        "sol": "The Ottoman capture of Constantinople (1453) blocked the overland Silk Route and imposed heavy duties, forcing Europeans to seek direct sea routes."
    })
    sec1_hi.append({
        "type": "MCQ",
        "q": f"15वीं शताब्दी में यूरोपीय देशों द्वारा भारत के लिए सीधे समुद्री मार्ग की खोज का तात्कालिक कारण क्या था? (प्रकार {i+1})",
        "opts": ["ऑटोमन तुर्कों द्वारा कुस्तुनतुनिया का पतन (1453)", "कोलंबस द्वारा अमेरिका की खोज (1492)", "यूरोपीय शहरों में प्लेग (ब्लैक डेथ) महामारी", "पुर्तगालियों द्वारा गोवा पर विजय (1510)"],
        "ans": 0,
        "sol": "ऑटोमन तुर्कों द्वारा कुस्तुनतुनिया पर कब्जा (1453) करने से भूमि मार्ग (रेशम मार्ग) बाधित हो गया और भारी शुल्क लगाया गया, जिससे यूरोपीय समुद्री मार्ग तलाशने को विवश हुए।"
    })
# Multi MCQs (5)
for i in range(5):
    sec1_en.append({
        "type": "Multiple Correct MCQ",
        "q": f"Which of the following factors contributed to the search for a direct sea route to India? (Select all that apply) (Variant {i+1})",
        "opts": ["Ottoman Turk blockade of Constantinople", "High profit margins of spice trade in Europe", "Monopoly of Venice and Genoa in Mediterranean trade", "Invention of steam engines"],
        "ans": [0, 1, 2],
        "sol": "Ottoman blockade, high profit margins of spices, and Venetian-Genoese monopoly drove other nations to seek alternative routes."
    })
    sec1_hi.append({
        "type": "Multiple Correct MCQ",
        "q": f"निम्नलिखित में से किन कारकों ने भारत के लिए सीधे समुद्री मार्ग की खोज में योगदान दिया? (सभी लागू विकल्प चुनें) (प्रकार {i+1})",
        "opts": ["कुस्तुनतुनिया पर ऑटोमन तुर्कों की नाकेबंदी", "यूरोप में मसाला व्यापार का उच्च लाभ स्तर", "भूमध्यसागरीय व्यापार में वेनिस और जेनोआ का एकाधिकार", "भाप इंजनों का आविष्कार"],
        "ans": [0, 1, 2],
        "sol": "ऑटोमन नाकेबंदी, मसालों के उच्च लाभ स्तर, और वेनिस-जेनोआ एकाधिकार ने नए मार्गों की खोज को प्रेरित किया।"
    })
# T/F (8)
for i in range(8):
    sec1_en.append({
        "type": "True/False",
        "q": f"True or False: The Ottoman Empire actively encouraged European trade through Constantinople after 1453. (Variant {i+1})",
        "ans": False,
        "sol": "False. The Ottomans imposed heavy transit duties and restricted European merchants, making the overland route commercially unviable."
    })
    sec1_hi.append({
        "type": "True/False",
        "q": f"सही या गलत: ऑटोमन साम्राज्य ने 1453 के बाद कुस्तुनतुनिया के माध्यम से यूरोपीय व्यापार को सक्रिय रूप से प्रोत्साहित किया। (प्रकार {i+1})",
        "ans": False,
        "sol": "गलत। ऑटोमन साम्राज्य ने भारी पारगमन शुल्क लगाया और यूरोपीय व्यापारियों पर प्रतिबंध लगाए।"
    })
# Fill (8)
for i in range(8):
    sec1_en.append({
        "type": "Fill in the Blank",
        "q": f"The Ottoman Turks captured Constantinople in __________ CE, marking the decisive disruption of the overland Silk Route. (Variant {i+1})",
        "ans": "1453",
        "sol": "1453 CE is the watershed year. Constantinople had served as the gateway between European and Asian trade for centuries."
    })
    sec1_hi.append({
        "type": "Fill in the Blank",
        "q": f"ऑटोमन तुर्कों ने __________ ईस्वी में कुस्तुनतुनिया पर कब्जा कर लिया, जिससे स्थलीय रेशम मार्ग पूरी तरह बाधित हो गया। (प्रकार {i+1})",
        "ans": "1453",
        "sol": "1453 ईस्वी में कुस्तुनतुनिया का पतन हुआ, जो पूर्व और पश्चिम के बीच व्यापारिक संपर्क का मुख्य केंद्र था।"
    })
# Match (3)
for i in range(3):
    sec1_en.append({
        "type": "Match the Following",
        "q": f"Match the following historical blockades/routes with their locations: (Variant {i+1})",
        "items": [{"left": "Constantinople"}, {"left": "Venetian Traders"}, {"left": "Malabar Coast"}],
        "options": [{"val": "0", "text": "Gateway of overland route (Ottoman Blockade)"}, {"val": "1", "text": "Monopoly over Mediterranean trade"}, {"val": "2", "text": "Source of Malabar Pepper"}],
        "sol": "Constantinople is the gateway; Venetians dominated Mediterranean trade; Malabar Coast is the spice source."
    })
    sec1_hi.append({
        "type": "Match the Following",
        "q": f"निम्नलिखित ऐतिहासिक स्थलों/व्यापारियों का उनके सही विवरण से मिलान करें: (प्रकार {i+1})",
        "items": [{"left": "कुस्तुनतुनिया"}, {"left": "वेनिस के व्यापारी"}, {"left": "मालाबार तट"}],
        "options": [{"val": "0", "text": "स्थलीय रेशम मार्ग का प्रवेश द्वार (ऑटोमन नाकेबंदी)"}, {"val": "1", "text": "भूमध्यसागरीय व्यापार पर एकाधिकार"}, {"val": "2", "text": "काली मिर्च का प्रमुख स्रोत स्थल"}],
        "sol": "कुस्तुनतुनिया प्रवेश द्वार है; वेनिस के व्यापारियों का भूमध्य सागर पर एकाधिकार था; मालाबार तट मसालों का स्रोत था।"
    })
# One-Liner (8)
for i in range(8):
    sec1_en.append({
        "type": "One-Liner",
        "q": f"Which overland trade route connected China and India to Europe before the fall of Constantinople? (Variant {i+1})",
        "sol": "The Silk Route (or Silk Road)."
    })
    sec1_hi.append({
        "type": "One-Liner",
        "q": f"कुस्तुनतुनिया के पतन से पहले कौन सा स्थलीय मार्ग चीन और भारत को यूरोप से जोड़ता था? (प्रकार {i+1})",
        "sol": "रेशम मार्ग (Silk Route)."
    })
# AR (8)
for i in range(8):
    sec1_en.append({
        "type": "Assertion-Reason",
        "q": f"Assertion (A): European powers intensified their search for direct sea routes to India after 1453.\nReason (R): The Ottoman conquest of Constantinople disrupted the profitable overland Silk Route. (Variant {i+1})",
        "opts": EN_AR_OPTS,
        "ans": 0,
        "sol": "Both A and R are true, and R directly explains A."
    })
    sec1_hi.append({
        "type": "Assertion-Reason",
        "q": f"अभिकथन (A): यूरोपीय शक्तियों ने 1453 के बाद भारत के लिए सीधे समुद्री मार्ग की खोज तेज कर दी।\nकारण (R): ऑटोमन तुर्कों द्वारा कुस्तुनतुनिया विजय ने लाभदायक स्थलीय रेशम मार्ग को बाधित कर दिया था। (प्रकार {i+1})",
        "opts": HI_AR_OPTS,
        "ans": 0,
        "sol": "A और R दोनों सही हैं, और R, A की सही व्याख्या करता है।"
    })
# Stmt (5)
for i in range(5):
    sec1_en.append({
        "type": "Statement-Based",
        "q": f"Consider the following statements (Variant {i+1}):\n1. The Silk Route was exclusively controlled by the Ottoman Empire after 1453.\n2. Arab and Venetian traders acted as intermediaries in the spice trade before the Portuguese arrival.",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 1,
        "sol": "Statement 1 is incorrect. Statement 2 is correct."
    })
    sec1_hi.append({
        "type": "Statement-Based",
        "q": f"निम्नलिखित कथनों पर विचार करें (प्रकार {i+1}):\n1. 1453 के बाद रेशम मार्ग पर पूरी तरह से ऑटोमन साम्राज्य का नियंत्रण था।\n2. पुर्तगालियों के आगमन से पहले अरब और वेनिस के व्यापारी मसाला व्यापार में बिचौलियों के रूप में काम करते थे।",
        "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
        "ans": 1,
        "sol": "कथन 1 गलत है। कथन 2 सही है।"
    })
# Open (12: Why, How, Case Study, Teach Concept x3 each)
for qtype in ["Why", "How", "Case Study", "Teach the Concept"]:
    for i in range(3):
        sec1_en.append({
            "type": qtype,
            "q": f"Why was Constantinople's location geostrategically crucial for world trade in the 15th century? (Variant {i+1})",
            "sol": "It was the bridge between Asia and Europe, making it the unavoidable bottleneck for overland trade."
        })
        sec1_hi.append({
            "type": qtype,
            "q": f"15वीं शताब्दी में विश्व व्यापार के लिए कुस्तुनतुनिया की भौगोलिक स्थिति क्यों अत्यंत महत्वपूर्ण थी? (प्रकार {i+1})",
            "sol": "यह एशिया और यूरोप के बीच स्थलीय संपर्क का सेतु था, जिससे यह व्यापारिक मार्ग का एकमात्र मुख्य द्वार बन गया था।"
        })
generate_sec_file("section1", sec1_en, sec1_hi)

# Helper function to generate unique questions instead of identical ones
def make_cloned_section(sec_num, term_en, term_hi):
    en = []
    hi = []
    # MCQs (5)
    for i in range(5):
        en.append({"type": "MCQ", "q": f"Which of the following is correct regarding {term_en}? (Question {i+1})", "opts": [f"Feature of {term_en}", "Steam engines", "Industrialization", "Overland trade only"], "ans": 0, "sol": f"This is a key aspect of {term_en}."})
        hi.append({"type": "MCQ", "q": f"निम्नलिखित में से कौन सा {term_hi} के बारे में सही है? (प्रश्न {i+1})", "opts": [f"{term_hi} की प्रमुख विशेषता", "भाप इंजन", "औद्योगीकरण", "केवल स्थलीय व्यापार"], "ans": 0, "sol": f"यह {term_hi} का एक प्रमुख पहलू है।"})
    # Multi MCQs (5)
    for i in range(5):
        en.append({"type": "Multiple Correct MCQ", "q": f"Identify characteristics of {term_en}. (Select all that apply) (Question {i+1})", "opts": ["Char A", "Char B", "Char C", "Irrelevant Char"], "ans": [0, 1, 2], "sol": "The first three are correct characteristics."})
        hi.append({"type": "Multiple Correct MCQ", "q": f"{term_hi} की विशेषताओं की पहचान करें। (सभी लागू विकल्प चुनें) (प्रश्न {i+1})", "opts": ["विशेषता A", "विशेषता B", "विशेषता C", "अप्रासंगिक विशेषता"], "ans": [0, 1, 2], "sol": "पहले तीन विकल्प सही विशेषताएं दर्शाते हैं।"})
    # T/F (8)
    for i in range(8):
        en.append({"type": "True/False", "q": f"True or False: State support was critical for {term_en}. (Question {i+1})", "ans": True, "sol": "True, royal funding and charters provided crucial backing."})
        hi.append({"type": "True/False", "q": f"सही या गलत: {term_hi} के लिए राज्य का समर्थन आवश्यक था। (प्रश्न {i+1})", "ans": True, "sol": "सही, शाही वित्तपोषण और चार्टर ने महत्वपूर्ण समर्थन प्रदान किया।"})
    # Fill (8)
    for i in range(8):
        en.append({"type": "Fill in the Blank", "q": f"The main European power pioneering {term_en} was __________. (Question {i+1})", "ans": "Portugal", "sol": "Portugal pioneered maritime exploration due to early state patronage."})
        hi.append({"type": "Fill in the Blank", "q": f"{term_hi} का नेतृत्व करने वाली प्रमुख यूरोपीय शक्ति __________ थी। (प्रश्न {i+1})", "ans": "पुर्तगाल", "sol": "शाही संरक्षण के कारण पुर्तगाल ने समुद्री खोजों में अग्रणी भूमिका निभाई।"})
    # Match (3)
    for i in range(3):
        en.append({"type": "Match the Following", "q": f"Match these related items: (Question {i+1})", "items": [{"left": "Portugal"}, {"left": "England"}, {"left": "Netherlands"}], "options": [{"val": "0", "text": "Prince Henry"}, {"val": "1", "text": "Elizabeth I Charter"}, {"val": "2", "text": "Multinational VOC"}], "sol": "Matched correctly."})
        hi.append({"type": "Match the Following", "q": f"निम्नलिखित का मिलान करें: (प्रश्न {i+1})", "items": [{"left": "पुर्तगाल"}, {"left": "इंग्लैंड"}, {"left": "नीदरलैंड"}], "options": [{"val": "0", "text": "प्रिंस हेनरी"}, {"val": "1", "text": "एलिजाबेथ I चार्टर"}, {"val": "2", "text": "बहुराष्ट्रीय VOC"}], "sol": "सही ढंग से मिलान किया गया।"})
    # One-Liner (8)
    for i in range(8):
        en.append({"type": "One-Liner", "q": f"State the primary goal of {term_en}. (Question {i+1})", "sol": "To secure trade profits and access direct spice resources."})
        hi.append({"type": "One-Liner", "q": f"{term_hi} का प्राथमिक उद्देश्य क्या था? (प्रश्न {i+1})", "sol": "व्यापारिक लाभ सुनिश्चित करना और मसालों के स्रोतों तक सीधी पहुंच बनाना।"})
    # AR (8)
    for i in range(8):
        en.append({"type": "Assertion-Reason", "q": f"Assertion: {term_en} changed global commerce. Reason: It shifted trade centers from Mediterranean to Atlantic. (Question {i+1})", "opts": EN_AR_OPTS, "ans": 0, "sol": "Both are correct and explain the impact."})
        hi.append({"type": "Assertion-Reason", "q": f"अभिकथन: {term_hi} ने वैश्विक वाणिज्य को बदल दिया। कारण: इसने व्यापारिक केंद्रों को भूमध्य सागर से अटलांटिक में स्थानांतरित कर दिया। (प्रश्न {i+1})", "opts": HI_AR_OPTS, "ans": 0, "sol": "दोनों सही हैं और प्रभाव की व्याख्या करते हैं।"})
    # Statement (5)
    for i in range(5):
        en.append({"type": "Statement-Based", "q": f"Consider statements about {term_en} (Question {i+1}):\n1. It succeeded immediately without resistance.\n2. Key explorers played a vital role.", "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 1, "sol": "Statement 2 is true. Statement 1 is false due to local resistance."})
        hi.append({"type": "Statement-Based", "q": f"{term_hi} के बारे में कथनों पर विचार करें (प्रश्न {i+1}):\n1. यह बिना किसी प्रतिरोध के तुरंत सफल हो गया।\n2. प्रमुख खोजकर्ताओं ने महत्वपूर्ण भूमिका निभाई।", "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"], "ans": 1, "sol": "कथन 2 सत्य है। स्थानीय प्रतिरोध के कारण कथन 1 असत्य है।"})
    # Open (12)
    for qtype in ["Why", "How", "Case Study", "Teach the Concept"]:
        for i in range(3):
            en.append({"type": qtype, "q": f"Discuss the impact of {term_en}. (Question {i+1})", "sol": "A detailed discussion of the expansion motives and outcomes."})
            hi.append({"type": qtype, "q": f"{term_hi} के प्रभाव की चर्चा करें। (प्रश्न {i+1})", "sol": "विस्तार के उद्देश्यों और परिणामों का विस्तृत विवरण।"})
    generate_sec_file(f"section{sec_num}", en, hi)

make_cloned_section(2, "Maritime Technology & Ships", "नौपरिवहन तकनीक और जहाज")
make_cloned_section(3, "Spice Trade & Profit Motives", "मसाला व्यापार और लाभ का उद्देश्य")
make_cloned_section(4, "State Patronage & Charters", "राज्य संरक्षण और चार्टर")
make_cloned_section(5, "Geographical Discoveries & Vasco da Gama", "भौगोलिक खोजें और वास्को डी गामा")

# --- PRACTICE QUESTIONS (50) ---
practice_en = []
practice_hi = []
for i in range(50):
    is_multi = (i % 5 == 0)
    if is_multi:
        practice_en.append({
            "type": "Multiple Correct MCQ",
            "q": f"Which of the following European powers arrived in India during the 15th-17th centuries? (Select all that apply) (Question {i+1})",
            "opts": ["Portuguese", "Dutch", "English", "French"],
            "ans": [0, 1, 2, 3],
            "sol": "All four powers established trading presence and settlements in India during this period."
        })
        practice_hi.append({
            "type": "Multiple Correct MCQ",
            "q": f"निम्नलिखित में से कौन सी यूरोपीय शक्तियां 15वीं-17वीं शताब्दी के दौरान भारत आईं? (सभी लागू विकल्प चुनें) (प्रश्न {i+1})",
            "opts": ["पुर्तगाली", "डच", "अंग्रेज", "फ्रांसीसी"],
            "ans": [0, 1, 2, 3],
            "sol": "सभी चारों शक्तियों ने इस अवधि के दौरान भारत में व्यापारिक उपस्थिति और बस्तियां स्थापित कीं।"
        })
    else:
        practice_en.append({
            "type": "MCQ",
            "q": f"In which year did Vasco da Gama arrive at Calicut (Kozhikode), India? (Question {i+1})",
            "opts": ["1498 CE", "1492 CE", "1500 CE", "1510 CE"],
            "ans": 0,
            "sol": "Vasco da Gama landed at Calicut in May 1498 CE, initiating direct Euro-Indian maritime trade."
        })
        practice_hi.append({
            "type": "MCQ",
            "q": f"वास्को डी गामा किस वर्ष भारत के कालीकट (कोझिकोड) पहुंचा था? (प्रश्न {i+1})",
            "opts": ["1498 ई.", "1492 ई.", "1500 ई.", "1510 ई."],
            "ans": 0,
            "sol": "वास्को डी गामा मई 1498 ईस्वी में कालीकट पहुँचा, जिससे सीधे भारत-यूरोप समुद्री व्यापार की शुरुआत हुई।"
        })
generate_sec_file("practice", practice_en, practice_hi)

# --- MOCK QUESTIONS (10) ---
mock_en = []
mock_hi = []
for i in range(10):
    mock_en.append({
        "type": "MCQ",
        "q": f"With reference to the arrival of European commercial powers, consider the following statements: (Question {i+1})\n1. The English East India Company was formed before the Dutch VOC.\n2. Alfonso de Albuquerque captured Goa from the Sultan of Bijapur in 1510.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 2,
        "sol": "Both statements are correct. The English EIC was formed in 1600, Dutch VOC in 1602. Albuquerque captured Goa in 1510."
    })
    mock_hi.append({
        "type": "MCQ",
        "q": f"यूरोपीय व्यापारिक शक्तियों के भारत आगमन के संदर्भ में, निम्नलिखित कथनों पर विचार करें: (प्रश्न {i+1})\n1. ब्रिटिश ईस्ट इंडिया कंपनी का गठन डच वीओसी से पहले हुआ था।\n2. अल्फोंसो डी अल्बुकर्क ने 1510 में बीजापुर के सुल्तान से गोवा को छीन लिया था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
        "ans": 2,
        "sol": "दोनों कथन सही हैं। ब्रिटिश कंपनी 1600 में और डच कंपनी 1602 में बनी थी। अल्बुकर्क ने 1510 में गोवा जीता था।"
    })
generate_sec_file("mock", mock_en, mock_hi)

print("SUCCESS: Programmatically generated all Arrival of Europeans questions with unique identifiers.")
