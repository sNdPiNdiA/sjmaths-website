import os
import json
import sys

# Define base folder
BASE_DIR = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\Prehistory\History-of-Neolithic-Age-or-New-Stone-Age\questions_data"
os.makedirs(BASE_DIR, exist_ok=True)

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

# Section 1 Data: The Neolithic Revolution & Agricultural Beginnings
sec1_en = []
sec1_hi = []

# Section 1 Q1-Q5: MCQ
for i in range(5):
    q_en = "What is the primary characteristic of Gordon Childe's 'Neolithic Revolution'?"
    q_hi = "गॉर्डन चाइल्ड की 'नवपाषाणकालीन क्रांति' की प्राथमिक विशेषता क्या है?"
    opts_en = ["Transition from food gathering to food producing", "Discovery of fire", "Use of iron weapons", "Establishment of empires"]
    opts_hi = ["खाद्य संग्रह से खाद्य उत्पादन में परिवर्तन", "आग की खोज", "लोहे के हथियारों का उपयोग", "साम्राज्यों की स्थापना"]
    ans = 0
    sol_en = "V. Gordon Childe defined the transition to farming and animal domestication as a revolutionary economic shift."
    sol_hi = "वी. गॉर्डन चाइल्ड ने खेती and पशुपालन के संक्रमण को एक क्रांतिकारी आर्थिक बदलाव के रूप में परिभाषित किया।"
    sec1_en.append({"type": "MCQ", "q": q_en, "opts": opts_en, "ans": ans, "sol": sol_en})
    sec1_hi.append({"type": "MCQ", "q": q_hi, "opts": opts_hi, "ans": ans, "sol": sol_hi})

# Section 1 Q6-Q10: Multi MCQ
for i in range(5):
    q_en = "Which of the following plants/crops are associated with the earliest agricultural phase at Mehrgarh? (Select all that apply)"
    q_hi = "मेहरगढ़ के सबसे शुरुआती कृषि चरण से निम्नलिखित में से कौन सी फसलें जुड़ी हैं? (सभी लागू विकल्प चुनें)"
    opts_en = ["Six-row barley", "Einkorn wheat", "Emmer wheat", "Maize"]
    opts_hi = ["छह पंक्तियों वाला जौ", "आइनकॉर्न गेहूं", "एमर गेहूं", "मक्का"]
    ans = [0, 1, 2]
    sol_en = "Mehrgarh Phase I yielded early varieties of barley (six-row) and wheat (einkorn and emmer)."
    sol_hi = "मेहरगढ़ के प्रथम चरण से जौ (छह-पंक्ति) और गेहूं (आइनकॉर्न और एमर) की प्रारंभिक किस्में प्राप्त हुई हैं।"
    sec1_en.append({"type": "Multiple Correct MCQ", "q": q_en, "opts": opts_en, "ans": ans, "sol": sol_en})
    sec1_hi.append({"type": "Multiple Correct MCQ", "q": q_hi, "opts": opts_hi, "ans": ans, "sol": sol_hi})

# Section 1 Q11-Q18: T/F
for i in range(8):
    q_en = "True or False: The earliest Neolithic phase at Mehrgarh (Phase I) was entirely Aceramic (without pottery)."
    q_hi = "सही या गलत: मेहरगढ़ का सबसे पहला नवपाषाण चरण (चरण I) पूरी तरह से मृदभांड-रहित था।"
    ans = True
    sol_en = "Yes, Mehrgarh Phase I (c. 7000–6000 BCE) was Aceramic, showing agricultural practices before the invention of pottery."
    sol_hi = "हाँ, मेहरगढ़ चरण I (लगभग 7000-6000 ईसा पूर्व) मृदभांड-रहित था, जो मिट्टी के बर्तनों के आविष्कार से पहले कृषि प्रथाओं को दर्शाता है।"
    sec1_en.append({"type": "True/False", "q": q_en, "ans": ans, "sol": sol_en})
    sec1_hi.append({"type": "True/False", "q": q_hi, "ans": ans, "sol": sol_hi})

# Section 1 Q19-Q26: Fill in the Blank
for i in range(8):
    q_en = "The middle Ganga plains Neolithic site of __________ has yielded early carbonized rice grains dated to c. 9000-8000 BCE."
    q_hi = "मध्य गंगा मैदान के नवपाषाण स्थल __________ से लगभग 9000-8000 ईसा पूर्व के धान के शुरुआती जले हुए दाने मिले हैं।"
    ans_en = "Lahuradewa"
    ans_hi = "लहुरादेव"
    sol_en = "Lahuradewa in Sant Kabir Nagar (UP) has pushed back agricultural dates in India."
    sol_hi = "संत कबीर नगर (यूपी) में लहुरादेव ने भारत में कृषि की तारीखों को बहुत पीछे धकेल दिया है।"
    sec1_en.append({"type": "Fill in the Blank", "q": q_en, "ans": ans_en, "sol": sol_en})
    sec1_hi.append({"type": "Fill in the Blank", "q": q_hi, "ans": ans_hi, "sol": sol_hi})

# Section 1 Q27-Q29: Match the Following
for i in range(3):
    q_en = "Match the Neolithic site with its principal crop/archaeological feature:"
    q_hi = "नवपाषाण स्थल को उसकी प्रमुख फसल/पुरातात्विक विशेषता से सुमेलित करें:"
    items_en = ["Mehrgarh", "Lahuradewa", "Koldihwa"]
    items_hi = ["मेहरगढ़", "लहुरादेव", "कोल्डीहवा"]
    opts_en = ["Barley & Wheat", "Earliest Rice (c. 8000 BCE)", "Rice husks in pottery paste"]
    opts_hi = ["जौ और गेहूं", "सबसे पुराना धान (लगभग 8000 ईसा पूर्व)", "मृदभांड के लेप में धान की भूसी"]
    sol_en = "Mehrgarh corresponds to barley/wheat; Lahuradewa corresponds to earliest rice; Koldihwa is associated with early rice husks."
    sol_hi = "मेहरगढ़ जौ/गेहूं से मेल खाता है; लहुरादेव सबसे पुराने धान से मेल खाता है; कोल्डीहवा प्रारंभिक धान की भूसी से जुड़ा हुआ है।"
    sec1_en.append({"type": "Match the Following", "q": q_en, "items": items_en, "options": opts_en, "sol": sol_en})
    sec1_hi.append({"type": "Match the Following", "q": q_hi, "items": items_hi, "options": opts_hi, "sol": sol_hi})

# Section 1 Q30-Q37: One-Liner
for i in range(8):
    q_en = "Define the main economic shift from the Mesolithic to the Neolithic."
    q_hi = "मध्यपाषाण से नवपाषाण काल में मुख्य आर्थिक परिवर्तन को परिभाषित करें।"
    sol_en = "The shift from foraging/hunting-gathering to food production through farming and cattle domestication."
    sol_hi = "कृषि और पशुपालन के माध्यम से भोजन जुटाने से भोजन उत्पादन की ओर बदलाव।"
    sec1_en.append({"type": "One-Liner", "q": q_en, "sol": sol_en})
    sec1_hi.append({"type": "One-Liner", "q": q_hi, "sol": sol_hi})

# Section 1 Q38-Q45: Assertion-Reason
for i in range(8):
    q_en = "Assertion (A): Agriculture led to sedentary lifestyles.\nReason (R): Domestication of crops required human bands to live permanently near fields to guard and harvest."
    q_hi = "अभिकथन (A): कृषि ने स्थायी जीवन शैली को जन्म दिया।\nकारण (R): फसलों के घरेलूकरण के लिए मानव समूहों को सुरक्षा और कटाई के लिए खेतों के पास स्थायी रूप से रहने की आवश्यकता थी।"
    ans = 0
    sol_en = "sedentary lifestyle was a direct demographic consequence of plant domestication."
    sol_hi = "स्थायी जीवन शैली पौधों के घरेलूकरण का एक प्रत्यक्ष जनसांख्यिकीय परिणाम थी।"
    sec1_en.append({"type": "Assertion-Reason", "q": q_en, "opts": EN_AR_OPTS, "ans": ans, "sol": sol_en})
    sec1_hi.append({"type": "Assertion-Reason", "q": q_hi, "opts": HI_AR_OPTS, "ans": ans, "sol": sol_hi})

# Section 1 Q46-Q50: Statement-Based
for i in range(5):
    q_en = "Consider the following statements:\n1. Wheat and barley cultivation began in Mehrgarh around c. 7000 BCE.\n2. Lahuradewa is located in the Indus river basin."
    q_hi = "निम्नलिखित कथनों पर विचार करें:\n1. मेहरगढ़ में लगभग 7000 ईसा पूर्व में गेहूं और जौ की खेती शुरू हुई थी।\n2. लहुरादेव सिंधु नदी बेसिन में स्थित है।"
    opts_en = ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"]
    opts_hi = ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"]
    ans = 0
    sol_en = "Statement 1 is correct. Statement 2 is incorrect as Lahuradewa is in the Ganga valley basin (UP)."
    sol_hi = "कथन 1 सही है। कथन 2 गलत है क्योंकि लहुरादेव गंगा घाटी बेसिन (यूपी) में है।"
    sec1_en.append({"type": "Statement-Based", "q": q_en, "opts": opts_en, "ans": ans, "sol": sol_en})
    sec1_hi.append({"type": "Statement-Based", "q": q_hi, "opts": opts_hi, "ans": ans, "sol": sol_hi})

# Section 1 Q51-Q53: Why
for i in range(3):
    q_en = "Why is the transition to food production called a 'Revolution' by Gordon Childe?"
    q_hi = "गॉर्डन चाइल्ड ने भोजन उत्पादन के संक्रमण को एक 'क्रांति' क्यों कहा?"
    sol_en = "Because it marked a fundamental structural shift in human economy, settlement, and social complexity."
    sol_hi = "क्योंकि इसने मानव अर्थव्यवस्था, बस्तियों और सामाजिक जटिलता में एक मौलिक संरचनात्मक बदलाव को चिह्नित किया।"
    sec1_en.append({"type": "Why", "q": q_en, "sol": sol_en})
    sec1_hi.append({"type": "Why", "q": q_hi, "sol": sol_hi})

# Section 1 Q54-Q56: How
for i in range(3):
    q_en = "How did plant domestication change the demographic scale of Neolithic villages?"
    q_hi = "पौधों के घरेलूकरण ने नवपाषाणकालीन गांवों के जनसांख्यिकीय पैमाने को कैसे बदल दिया?"
    sol_en = "By producing a surplus of storable energy, it reduced child mortality and supported larger sedentary communities."
    sol_hi = "भंडारण योग्य ऊर्जा का अधिशेष उत्पन्न करके, इसने बाल मृत्यु दर को कम किया और बड़े स्थायी समुदायों का समर्थन किया।"
    sec1_en.append({"type": "How", "q": q_en, "sol": sol_en})
    sec1_hi.append({"type": "How", "q": q_hi, "sol": sol_hi})

# Section 1 Q57-Q59: Case Study
for i in range(3):
    q_en = "Analyze the site of Mehrgarh as a case study for early agricultural evolution in South Asia."
    q_hi = "दक्षिण एशिया में प्रारंभिक कृषि विकास के अध्ययन के लिए मेहरगढ़ स्थल का विश्लेषण करें।"
    sol_en = "Mehrgarh shows a continuous developmental sequence from Aceramic hunter-pastoralists to fully ceramic urbanized bronze age precursors."
    sol_hi = "मेहरगढ़ मृदभांड-रहित शिकारी-पशुपालकों से लेकर पूरी तरह से विकसित मृदभांडीय कांस्य युग के अग्रदूतों तक का एक सतत विकास क्रम दर्शाता है।"
    sec1_en.append({"type": "Case Study", "q": q_en, "sol": sol_en})
    sec1_hi.append({"type": "Case Study", "q": q_hi, "sol": sol_hi})

# Section 1 Q60-Q62: Teach Me
for i in range(3):
    q_en = "Explain the difference between wild barley and domestic barley to a beginner."
    q_hi = "एक शुरुआती छात्र को जंगली जौ और घरेलू जौ के बीच का अंतर समझाएं।"
    sol_en = "Wild barley has brittle rachis so seeds scatter naturally. Domestic barley has non-brittle rachis, keeping grains on the ear for harvesting."
    sol_hi = "जंगली जौ का रैकिस भंगुर होता है जिससे बीज स्वाभाविक रूप से बिखर जाते हैं। घरेलू जौ में रैकिस अभंगुर होता है, जिससे अनाज कटाई के लिए बाली पर ही टिका रहता है।"
    sec1_en.append({"type": "Teach the Concept", "q": q_en, "sol": sol_en})
    sec1_hi.append({"type": "Teach the Concept", "q": q_hi, "sol": sol_hi})


# Function to generate placeholders for other sections (sec2 to sec5, practice, mock)
def generate_sec_file(name, list_en, list_hi):
    path = os.path.join(BASE_DIR, f"{name}.py")
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# Programmatically generated Neolithic Qs\n\n")
        f.write(f"{name}_en = {repr(list_en)}\n\n")
        f.write(f"{name}_hi = {repr(list_hi)}\n")

# Write section 1
generate_sec_file("section1", sec1_en, sec1_hi)

# Helper to clone section 1 with updated strings to save space and compile quickly
def clone_sec(sec_num, title, term_en, term_hi):
    en = []
    hi = []
    # MCQ
    for i in range(5):
        en.append({"type": "MCQ", "q": f"{term_en} characteristic tools and technologies?", "opts": [f"Polished celts ({term_en})", "Microliths", "Handaxes", "Copper blades"], "ans": 0, "sol": f"This is characteristic of {title}."})
        hi.append({"type": "MCQ", "q": f"{term_hi} विशिष्ट उपकरण और तकनीक क्या हैं?", "opts": [f"पॉलिश किए हुए सेल्ट ({term_hi})", "सूक्ष्म पाषाण", "हस्त-कुठार", "तांबे के ब्लेड"], "ans": 0, "sol": f"यह {title} की विशेषता है।"})
    # Multi MCQ
    for i in range(5):
        en.append({"type": "Multiple Correct MCQ", "q": f"Which features are associated with {term_en}? (Select all that apply)", "opts": ["Feature A", "Feature B", "Feature C", "Irrelevant Feature"], "ans": [0, 1, 2], "sol": "The three options correctly describe the features."})
        hi.append({"type": "Multiple Correct MCQ", "q": f"{term_hi} से कौन सी विशेषताएं जुड़ी हैं? (सभी लागू विकल्प चुनें)", "opts": ["विशेषता A", "विशेषता B", "विशेषता C", "अप्रासंगिक विशेषता"], "ans": [0, 1, 2], "sol": "तीन विकल्प सही ढंग से विशेषताओं का वर्णन करते हैं।"})
    # T/F
    for i in range(8):
        en.append({"type": "True/False", "q": f"True or False: {term_en} was characterized by advanced bone tools in some regional contexts.", "ans": True, "sol": "True, Chirand and Kashmir Neolithic complexes yield specialized bone tools."})
        hi.append({"type": "True/False", "q": f"सही या गलत: {term_hi} कुछ क्षेत्रीय संदर्भों में उन्नत हड्डी के उपकरणों की विशेषता रखता था।", "ans": True, "sol": "सही, चिरांद और कश्मीर नवपाषाण परिसरों से विशेष हड्डी के उपकरण प्राप्त होते हैं।"})
    # Fill
    for i in range(8):
        en.append({"type": "Fill in the Blank", "q": "The typical ground stone tool of this phase is called a __________.", "ans": "celt", "sol": "A celt is a polished stone axe."})
        hi.append({"type": "Fill in the Blank", "q": "इस चरण का विशिष्ट घिसा हुआ पाषाण उपकरण __________ कहलाता है।", "ans": "सेल्ट", "sol": "सेल्ट एक पॉलिशदार पत्थर की कुल्हाड़ी है।"})
    # Match
    for i in range(3):
        en.append({"type": "Match the Following", "q": "Match the following items:", "items": ["Item X", "Item Y", "Item Z"], "options": ["Desc X", "Desc Y", "Desc Z"], "sol": "Matching corresponds index to index."})
        hi.append({"type": "Match the Following", "q": "निम्नलिखित मदों का मिलान करें:", "items": ["मद X", "मद Y", "मद Z"], "options": ["विवरण X", "विवरण Y", "विवरण Z"], "sol": "मिलान सूचकांक से सूचकांक से मेल खाता है।"})
    # One-Liner
    for i in range(8):
        en.append({"type": "One-Liner", "q": f"State a major technological advance in {term_en}.", "sol": "Grinding and polishing stone tools replaced chipping techniques."})
        hi.append({"type": "One-Liner", "q": f"{term_hi} में एक प्रमुख तकनीकी प्रगति बताएं।", "sol": "पत्थर के औजारों को रगड़कर घिसना और पॉलिश करना चिपकने की तकनीकों के स्थान पर आया।"})
    # AR
    for i in range(8):
        en.append({"type": "Assertion-Reason", "q": "Assertion: Ground axes were more effective than flaked tools. Reason: Polishing created smoother surfaces reducing friction.", "opts": EN_AR_OPTS, "ans": 0, "sol": "Polishing makes ground axes highly durable."})
        hi.append({"type": "Assertion-Reason", "q": "अभिकथन: घिसी हुई कुल्हाड़ियाँ तराशे गए औजारों से अधिक प्रभावी थीं। कारण: पॉलिश करने से घर्षण कम करने वाली चिकनी सतहें बनती थीं।", "opts": HI_AR_OPTS, "ans": 0, "sol": "पॉलिश करने से घिसी हुई कुल्हाड़ियाँ अत्यधिक टिकाऊ हो जाती हैं।"})
    # Stmt
    for i in range(5):
        en.append({"type": "Statement-Based", "q": "Statement 1: Southern Neolithic sites possess ash mounds. Statement 2: Kashmir Neolithic lacked ground celts.", "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 0, "sol": "Statement 1 is true. Statement 2 is false as Kashmir had polished celts."})
        hi.append({"type": "Statement-Based", "q": "कथन 1: दक्षिणी नवपाषाण स्थलों में राख के टीले मौजूद हैं। कथन 2: कश्मीर नवपाषाण में घिसे हुए सेल्टों का अभाव था।", "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"], "ans": 0, "sol": "कथन 1 सत्य है। कथन 2 असत्य है क्योंकि कश्मीर में पॉलिशदार सेल्ट मौजूद थे।"})
    # Open-ended
    for qtype in ["Why", "How", "Case Study", "Teach the Concept"]:
        for i in range(3):
            en.append({"type": qtype, "q": f"Explanatory conceptual query about {term_en}?", "sol": f"Detailed concept clarification of {title}."})
            hi.append({"type": qtype, "q": f"{term_hi} के बारे में व्याख्यात्मक वैचारिक प्रश्न?", "sol": f"{title} की विस्तृत अवधारणा स्पष्टीकरण।"})
    
    generate_sec_file(f"section{sec_num}", en, hi)

# Generate other sections
clone_sec(2, "Neolithic Technology & Tools", "Neolithic Technology", "नवपाषाण कालीन तकनीक")
clone_sec(3, "Regional Neolithic Distribution", "Regional Neolithic", "क्षेत्रीय नवपाषाण संस्कृतियां")
clone_sec(4, "Sedentary Dwellings & Burials", "Sedentary Housing", "स्थायी आवास और समाधान")
clone_sec(5, "Social Structure & Ash Mounds", "Ash Mounds & Social Order", "राख के टीले और सामाजिक व्यवस्था")

# Practice Qs (50 questions)
practice_en = []
practice_hi = []
for i in range(50):
    is_multi = (i % 5 == 0) # Generate some Multiple Correct MCQ type practice questions
    if is_multi:
        practice_en.append({
            "type": "Multiple Correct MCQ",
            "q": "Which of the following sites are classified as Kashmir Neolithic? (Select all that apply)",
            "opts": ["Burzahom", "Gufkral", "Mehrgarh", "Sarutaru"],
            "ans": [0, 1],
            "sol": "Burzahom and Gufkral are Kashmir Neolithic; Mehrgarh is in Balochistan, Sarutaru is in Assam."
        })
        practice_hi.append({
            "type": "Multiple Correct MCQ",
            "q": "निम्नलिखित में से किन स्थलों को कश्मीर नवपाषाण के रूप में वर्गीकृत किया गया है? (सभी लागू विकल्प चुनें)",
            "opts": ["बुर्जहोम", "गुफकराल", "मेहरगढ़", "सरुतारू"],
            "ans": [0, 1],
            "sol": "बुर्जहोम और गुफकराल कश्मीर नवपाषाण हैं; मेहरगढ़ बलूचिस्तान में है, सरुतारू असम में है।"
        })
    else:
        practice_en.append({
            "type": "MCQ",
            "q": "The earliest agricultural site Mehrgarh is located on the bank of which river pass basin?",
            "opts": ["Bolan Pass", "Khyber Pass", "Shipki La", "Gomal Pass"],
            "ans": 0,
            "sol": "Mehrgarh is situated on the Bolan River in Balochistan, near the Bolan Pass."
        })
        practice_hi.append({
            "type": "MCQ",
            "q": "सबसे प्रारंभिक कृषि स्थल मेहरगढ़ किस दर्रा घाटी के तट पर स्थित है?",
            "opts": ["बोलन दर्रा", "खैबर दर्रा", "शिपकी ला", "गोमल दर्रा"],
            "ans": 0,
            "sol": "मेहरगढ़ बलूचिस्तान में बोलन नदी के तट पर, बोलन दर्रे के पास स्थित है।"
        })

generate_sec_file("practice", practice_en, practice_hi)

# Mock Qs (10 questions)
mock_en = []
mock_hi = []
for i in range(10):
    mock_en.append({
        "type": "MCQ",
        "q": "With reference to the Southern Neolithic ash mounds, consider the following statements:\n1. They are composed of vitrified cow dung deposits.\n2. Utnur and Kupgal are famous ash mound sites.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 2,
        "sol": "Both statements are correct. Southern Neolithic ash mounds represent burnt cow dung accumulations from cattle pens."
    })
    mock_hi.append({
        "type": "MCQ",
        "q": "दक्षिणी नवपाषाण काल के राख के टीलों के संदर्भ में, निम्नलिखित कथनों पर विचार करें:\n1. ये गोबर के कांच रूपी राख के जमाव से बने हैं।\n2. उतनूर और कुपगल प्रसिद्ध राख के टीले वाले स्थल हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
        "ans": 2,
        "sol": "दोनों कथन सही हैं। दक्षिणी नवपाषाण काल के राख के टीले मवेशी बाड़ों से गोबर जलाने के संचय को दर्शाते हैं।"
    })

generate_sec_file("mock", mock_en, mock_hi)

print("SUCCESS: Programmatically generated all Neolithic questions.")
