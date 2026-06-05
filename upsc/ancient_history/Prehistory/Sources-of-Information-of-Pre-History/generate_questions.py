import json
import os

# Standard Option Templates
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

# Section 1: Archaeological Excavations & Major Sites (58 Questions)
sec1_en = []
sec1_hi = []

# Section 2: Epigraphy & Numismatics (58 Questions)
sec2_en = []
sec2_hi = []

# Section 3: Literary Sources (58 Questions)
sec3_en = []
sec3_hi = []

# Section 4: Foreign Accounts (58 Questions)
sec4_en = []
sec4_hi = []

# Section 5: Scientific Dating & Palaeo-environment (58 Questions)
sec5_en = []
sec5_hi = []

# Root practice questions (50 Questions)
practice_en = []
practice_hi = []

# Root mock test questions (10 Questions)
mock_en = []
mock_hi = []

# Helper to add standard MCQ
def add_mcq(sec_en, sec_hi, q_en, q_hi, opts_en, opts_hi, ans, sol_en, sol_hi):
    sec_en.append({"type": "MCQ", "q": q_en, "opts": opts_en, "ans": ans, "sol": sol_en})
    sec_hi.append({"type": "MCQ", "q": q_hi, "opts": opts_hi, "ans": ans, "sol": sol_hi})

# Helper to add Multiple Correct MCQ
def add_multi_mcq(sec_en, sec_hi, q_en, q_hi, opts_en, opts_hi, ans_list, sol_en, sol_hi):
    sec_en.append({"type": "Multiple Correct MCQ", "q": q_en, "opts": opts_en, "ans": ans_list, "sol": sol_en})
    sec_hi.append({"type": "Multiple Correct MCQ", "q": q_hi, "opts": opts_hi, "ans": ans_list, "sol": sol_hi})

# Helper to add True/False
def add_tf(sec_en, sec_hi, q_en, q_hi, ans, sol_en, sol_hi):
    sec_en.append({"type": "True/False", "q": q_en, "ans": ans, "sol": sol_en})
    sec_hi.append({"type": "True/False", "q": q_hi, "ans": ans, "sol": sol_hi})

# Helper to add Fill in the Blank
def add_blank(sec_en, sec_hi, q_en, q_hi, ans_en, ans_hi, sol_en, sol_hi):
    sec_en.append({"type": "Fill in the Blank", "q": q_en, "ans": ans_en, "sol": sol_en})
    sec_hi.append({"type": "Fill in the Blank", "q": q_hi, "ans": ans_hi, "sol": sol_hi})

# Helper to add Match the Following
def add_match(sec_en, sec_hi, q_en, q_hi, items_en, items_hi, opts_en, opts_hi, sol_en, sol_hi):
    sec_en.append({"type": "Match the Following", "q": q_en, "items": items_en, "options": opts_en, "sol": sol_en})
    sec_hi.append({"type": "Match the Following", "q": q_hi, "items": items_hi, "options": opts_hi, "sol": sol_hi})

# Helper to add One-Liner
def add_oneliner(sec_en, sec_hi, q_en, q_hi, sol_en, sol_hi):
    sec_en.append({"type": "One-Liner", "q": q_en, "sol": sol_en})
    sec_hi.append({"type": "One-Liner", "q": q_hi, "sol": sol_hi})

# Helper to add Assertion-Reason
def add_ar(sec_en, sec_hi, q_en, q_hi, ans, sol_en, sol_hi):
    sec_en.append({"type": "Assertion-Reason", "q": q_en, "opts": EN_AR_OPTS, "ans": ans, "sol": sol_en})
    sec_hi.append({"type": "Assertion-Reason", "q": q_hi, "opts": HI_AR_OPTS, "ans": ans, "sol": sol_hi})

# Helper to add Statement-Based
def add_stmt(sec_en, sec_hi, q_en, q_hi, opts_en, opts_hi, ans, sol_en, sol_hi):
    sec_en.append({"type": "Statement-Based", "q": q_en, "opts": opts_en, "ans": ans, "sol": sol_en})
    sec_hi.append({"type": "Statement-Based", "q": q_hi, "opts": opts_hi, "ans": ans, "sol": sol_hi})

# Helper to add Open Ended (Why/How/Case/Teach)
def add_open(sec_en, sec_hi, qtype, q_en, q_hi, sol_en, sol_hi):
    sec_en.append({"type": qtype, "q": q_en, "sol": sol_en})
    sec_hi.append({"type": qtype, "q": q_hi, "sol": sol_hi})

# ==========================================
# SECTION 1: ARCHAEOLOGICAL EXCAVATIONS & SITES
# ==========================================

# 1. MCQ (5 Qs)
add_mcq(sec1_en, sec1_hi,
    "Who introduced the systematic grid method of excavation in India to maintain stratigraphical control?",
    "भारत में स्तरविन्यास नियंत्रण बनाए रखने के लिए उत्खनन की व्यवस्थित ग्रिड पद्धति की शुरुआत किसने की?",
    ["Robert Bruce Foote", "Mortimer Wheeler", "John Marshall", "Alexander Cunningham"],
    ["रॉबर्ट ब्रूस फुट", "मॉर्टिमर व्हीलर", "जॉन मार्शल", "अलेक्जेंडर कनिंघम"],
    1,
    "Mortimer Wheeler introduced the grid method of excavation, which used unexcavated 'baulks' between square trenches to preserve vertical stratigraphy.",
    "मॉर्टिमर व्हीलर ने उत्खनन की ग्रिड पद्धति की शुरुआत की, जिसमें ऊर्ध्वाधर स्तरविन्यास को संरक्षित करने के लिए वर्गाकार खाइयों के बीच बिना खोदे गए हिस्से (बाल्क) छोड़े जाते थे।"
)
add_mcq(sec1_en, sec1_hi,
    "In which year were the famous prehistoric rock shelters of Bhimbetka discovered by Dr. V.S. Wakankar?",
    "डॉ. वी.एस. वाकणकर द्वारा भीमबेटका के प्रसिद्ध प्रागैतिहासिक शैल आश्रयों की खोज किस वर्ष की गई थी?",
    ["1863", "1921", "1957", "1974"],
    ["1863", "1921", "1957", "1974"],
    2,
    "Dr. V.S. Wakankar discovered the Bhimbetka rock shelters in 1957 while traveling by train and noticing the sandstone rock formations.",
    "डॉ. वी.एस. वाकणकर ने 1957 में ट्रेन से यात्रा करते समय बलुआ पत्थर की चट्टानों को देखकर भीमबेटका शैल आश्रयों की खोज की थी।"
)
add_mcq(sec1_en, sec1_hi,
    "Which archaeological site has yielded the earliest evidence of a Neolithic village settlement in South Asia?",
    "किस पुरातात्विक स्थल से दक्षिण एशिया में नवपाषाणकालीन ग्रामीण बस्ती का सबसे पहला साक्ष्य मिला है?",
    ["Mehrgarh", "Lahuradewa", "Burzahom", "Koldihwa"],
    ["मेहरगढ़", "लहुरादेवा", "बुर्जहोम", "कोलडिहवा"],
    0,
    "Mehrgarh in Balochistan, Pakistan, represents the earliest Neolithic village in South Asia, dating back to c. 7000 BCE.",
    "पाकिस्तान के बलूचिस्तान में स्थित मेहरगढ़ दक्षिण एशिया में सबसे प्रारंभिक नवपाषाणकालीन गाँव का प्रतिनिधित्व करता है, जो लगभग 7000 ईसा पूर्व का है।"
)
add_mcq(sec1_en, sec1_hi,
    "The Lower Paleolithic site of Attirampakkam, which established a 1.5-million-year-old Acheulian history, is located near which city?",
    "निम्न पुरापाषाणकालीन स्थल अतिरम्पक्कम, जिसने 1.5 मिलियन वर्ष पुराने अशुली इतिहास को स्थापित किया, किस शहर के निकट स्थित है?",
    ["Madurai", "Chennai", "Bengaluru", "Hyderabad"],
    ["मदुरै", "चेन्नई", "बेंगलुरु", "हैदराबाद"],
    1,
    "Attirampakkam is located in the Kortallayar River basin near Chennai, Tamil Nadu. Excavated by Shanti Pappu, it is dated to c. 1.5 MYA.",
    "अतिरम्पक्कम तमिलनाडु में चेन्नई के निकट कोर्तलैयार नदी बेसिन में स्थित है। शांति पप्पू द्वारा उत्खनित यह स्थल लगभग 1.5 मिलियन वर्ष पुराना माना गया है।"
)
add_mcq(sec1_en, sec1_hi,
    "The major Chalcolithic site of Inamgaon, which features a fortified settlement and mud houses, is located on which river?",
    "इनामगांव का प्रमुख ताम्रपाषाण कालीन स्थल, जिसमें एक किलेबंद बस्ती और मिट्टी के घर मिलते हैं, किस नदी पर स्थित है?",
    ["Narmada", "Ghod", "Pravara", "Kothari"],
    ["नर्मदा", "घोड़", "प्रवरा", "कोठारी"],
    1,
    "Inamgaon is a large Chalcolithic settlement of the Jorwe culture located on the banks of the Ghod River, a tributary of the Bhima River in Maharashtra.",
    "इनामगांव महाराष्ट्र में भीमा नदी की सहायक नदी घोड़ नदी के किनारे स्थित जोर्वे संस्कृति की एक बड़ी ताम्रपाषाण कालीन बस्ती है।"
)

# 2. Multiple Correct MCQ (5 Qs)
add_multi_mcq(sec1_en, sec1_hi,
    "Which of the following sites are classified as Paleolithic in the Indian subcontinent? (Select all that apply)",
    "भारतीय उपमहाद्वीप में निम्नलिखित में से किन स्थलों को पुरापाषाण कालीन वर्गीकृत किया गया है? (सभी लागू विकल्प चुनें)",
    ["Attirampakkam", "Hunsgi", "Mehrgarh", "Bhimbetka"],
    ["अतिरम्पक्कम", "हुंसगी", "मेहरगढ़", "भीमबेटका"],
    [0, 1, 3],
    "Attirampakkam, Hunsgi, and Bhimbetka are Paleolithic sites, while Mehrgarh is a Neolithic site.",
    "अतिरम्पक्कम, हुंसगी और भीमबेटका पुरापाषाण कालीन स्थल हैं, जबकि मेहरगढ़ एक नवपाषाण कालीन स्थल है।"
)
add_multi_mcq(sec1_en, sec1_hi,
    "Which excavations were directed or co-directed by French archaeologist Jean-François Jarrige? (Select all that apply)",
    "फ्रांसीसी पुरातत्वविद् ज्यां-फ्रांस्वा जारिज द्वारा किस उत्खनन का निर्देशन या सह-निर्देशन किया गया था? (सभी लागू विकल्प चुनें)",
    ["Mehrgarh", "Nausharo", "Pirak", "Attirampakkam"],
    ["मेहरगढ़", "नौशारो", "पीरक", "अतिरम्पक्कम"],
    [0, 1, 2],
    "Jean-François Jarrige directed the excavations at Mehrgarh, Nausharo, and Pirak in Balochistan. Attirampakkam was excavated by Shanti Pappu.",
    "ज्यां-फ्रांस्वा जारिज ने बलूचिस्तान में मेहरगढ़, नौशारो और पीरक के उत्खनन का निर्देशन किया था। अतिरम्पक्कम का उत्खनन शांति पप्पू द्वारा किया गया था।"
)
add_multi_mcq(sec1_en, sec1_hi,
    "Which of the following features are characteristic of horizontal excavations? (Select all that apply)",
    "निम्नलिखित में से कौन सी विशेषताएं क्षैतिज (horizontal) उत्खनन की लाक्षणिक हैं? (सभी लागू विकल्प चुनें)",
    ["Exposes structural layouts of a single period", "Acts as a quick chronological probe", "Covers a wide spatial area", "Minimizes damage to upper strata"],
    ["एक ही काल के संरचनात्मक लेआउट को उजागर करता है", "एक त्वरित कालानुक्रमिक जांच के रूप में कार्य करता है", "एक विस्तृत स्थानिक क्षेत्र को कवर करता है", "ऊपरी परतों को होने वाले नुकसान को कम करता है"],
    [0, 2],
    "Horizontal excavations expose wide spatial layouts of a single period to understand settlement patterns. Vertical excavations serve as chronological probes.",
    "क्षैतिज उत्खनन बस्ती के पैटर्न को समझने के लिए एक ही काल के व्यापक स्थानिक लेआउट को उजागर करता है। लंबवत उत्खनन कालानुक्रमिक जांच के रूप में कार्य करता है।"
)
add_multi_mcq(sec1_en, sec1_hi,
    "Which of the following sites represent the Mesolithic phase in India? (Select all that apply)",
    "निम्नलिखित में से कौन से स्थल भारत में मध्यपाषाण काल का प्रतिनिधित्व करते हैं? (सभी लागू विकल्प चुनें)",
    ["Bagor", "Adamgarh", "Langhnaj", "Inamgaon"],
    ["बागोर", "आदमगढ़", "लंगनाज", "इनामगांव"],
    [0, 1, 2],
    "Bagor, Adamgarh, and Langhnaj are famous Mesolithic sites. Inamgaon is a Chalcolithic settlement.",
    "बागोर, आदमगढ़ और लंगनाज प्रसिद्ध मध्यपाषाण कालीन स्थल हैं। इनामगांव एक ताम्रपाषाण कालीन बस्ती है।"
)
add_multi_mcq(sec1_en, sec1_hi,
    "Which of the following elements did Mortimer Wheeler introduce to Indian archaeology? (Select all that apply)",
    "मॉर्टिमर व्हीलर ने भारतीय पुरातत्व में निम्नलिखित में से किन तत्वों की शुरुआत की? (सभी लागू विकल्प चुनें)",
    ["Stratigraphical grid system", "Scientific staff training at Taxila", "Use of Carbon-14 dating", "Focus on the Harappan citadel layouts"],
    ["स्तरविन्यास ग्रिड प्रणाली", "तक्षशिला में वैज्ञानिक स्टाफ प्रशिक्षण", "कार्बन-14 तिथि निर्धारण का उपयोग", "हड़प्पा के दुर्ग (citadel) के लेआउट पर ध्यान"],
    [0, 1, 3],
    "Mortimer Wheeler introduced the grid system, structured training at Taxila, and focused on Harappan citadel fortifications. C-14 was introduced in India after his tenure.",
    "मॉर्टिमर व्हीलर ने ग्रिड प्रणाली, तक्षशिला में संरचित प्रशिक्षण की शुरुआत की और हड़प्पा के दुर्ग किलेबंदी पर ध्यान केंद्रित किया। भारत में सी-14 उनके कार्यकाल के बाद शुरू हुआ था।"
)

# 3. True/False (8 Qs)
add_tf(sec1_en, sec1_hi,
    "Vertical excavation is primarily designed to establish a detailed site timeline rather than uncover structural layouts.",
    "लंबवत (vertical) उत्खनन मुख्य रूप से संरचनात्मक लेआउट को उजागर करने के बजाय एक विस्तृत स्थल समयरेखा स्थापित करने के लिए डिज़ाइन किया गया है।",
    True,
    "Vertical excavation cuts deep through layers to serve as a chronological probe to build a historical sequence.",
    "लंबवत उत्खनन ऐतिहासिक अनुक्रम बनाने के लिए कालानुक्रमिक जांच के रूप में परतों में गहराई तक जाता है।"
)
add_tf(sec1_en, sec1_hi,
    "Robert Bruce Foote discovered the first Indian Paleolithic tool at Bhimbetka in 1863.",
    "रॉबर्ट ब्रूस फुट ने 1863 में भीमबेटका में पहले भारतीय पुरापाषाणकालीन उपकरण की खोज की थी।",
    False,
    "Robert Bruce Foote discovered the first Paleolithic tool (a handaxe) at Pallavaram near Chennai, not Bhimbetka.",
    "रॉबर्ट ब्रूस फुट ने पहले पुरापाषाणकालीन उपकरण (हस्त-कुठार) की खोज चेन्नई के पास पल्लवरम में की थी, भीमबेटका में नहीं।"
)
add_tf(sec1_en, sec1_hi,
    "The archaeological site of Hunsgi utilized limestone instead of quartzite for tool manufacture.",
    "हुंसगी के पुरातात्विक स्थल ने उपकरण निर्माण के लिए क्वार्टजाइट के स्थान पर चूना पत्थर (limestone) का उपयोग किया था।",
    True,
    "The Hunsgi-Baichbal valley is unique because Lower Paleolithic hominins utilized locally available limestone for their Acheulian tools.",
    "हुंसगी-बैचबल घाटी अद्वितीय है क्योंकि निम्न पुरापाषाणकालीन मानवों ने अपने अशुली उपकरणों के लिए स्थानीय स्तर पर उपलब्ध चूना पत्थर का उपयोग किया था।"
)
add_tf(sec1_en, sec1_hi,
    "The grid method leaves unexcavated earth walls called 'baulks' to show soil stratigraphy.",
    "ग्रिड विधि मिट्टी के स्तरविन्यास को दिखाने के लिए 'बाल्क' (baulks) नामक बिना खोदे गए हिस्से को छोड़ देती है।",
    True,
    "Baulks are vertical dirt walls left between grids to allow continuous recording and observation of soil layers.",
    "बाल्क ग्रिडों के बीच छोड़ी गई खड़ी दीवारें हैं ताकि मिट्टी की परतों की लगातार रिकॉर्डिंग और अवलोकन किया जा सके।"
)
add_tf(sec1_en, sec1_hi,
    "Lahuradewa is located in the Indus valley and is known for early wheat cultivation.",
    "लहुरादेवा सिंधु घाटी में स्थित है और गेहूं की प्रारंभिक खेती के लिए जाना जाता है।",
    False,
    "Lahuradewa is located in Sant Kabir Nagar, Uttar Pradesh (Ganga Valley), and is famous for early domestic rice evidence, not Indus valley wheat.",
    "लहुरादेवा संत कबीर नगर, उत्तर प्रदेश (गंगा घाटी) में स्थित है और यह शुरुआती धान की खेती के लिए प्रसिद्ध है, न कि सिंधु घाटी के गेहूं के लिए।"
)
add_tf(sec1_en, sec1_hi,
    "Stratigraphy is based on the principle that the lowest layer of undisturbed soil is the oldest.",
    "स्तरविन्यास इस सिद्धांत पर आधारित है कि बिना किसी छेड़छाड़ के मिट्टी की सबसे निचली परत सबसे पुरानी होती है।",
    True,
    "The Law of Superposition states that in an undisturbed stratigraphic sequence, the oldest layers lie at the bottom.",
    "अध्यारोपण का नियम (Law of Superposition) बताता है कि एक अबाधित स्तरविन्यास अनुक्रम में, सबसे पुरानी परतें सबसे नीचे होती हैं।"
)
add_tf(sec1_en, sec1_hi,
    "All Chalcolithic cultures in India are contemporary with the early Harappan civilization.",
    "भारत की सभी ताम्रपाषाण कालीन संस्कृतियाँ प्रारंभिक हड़प्पा सभ्यता के समकालीन हैं।",
    False,
    "Most Chalcolithic cultures (like Jorwe, Malwa, Banas) were post-Harappan or late Harappan rural farming communities existing after 2000 BCE.",
    "अधिकांश ताम्रपाषाण कालीन संस्कृतियाँ (जैसे जोर्वे, मालवा, बनास) उत्तर-हड़प्पा या उत्तरवर्ती हड़प्पा ग्रामीण कृषि समुदाय थीं जो 2000 ईसा पूर्व के बाद अस्तित्व में आईं।"
)
add_tf(sec1_en, sec1_hi,
    "Dr. Shanti Pappu's excavations at Attirampakkam pushed the history of Indian Acheulian tools back to c. 1.5 million years ago.",
    "अतिरम्पक्कम में डॉ. शांति पप्पू के उत्खनन ने भारतीय अशुली उपकरणों के इतिहास को लगभग 1.5 मिलियन वर्ष पीछे धकेल दिया।",
    True,
    "Excavations by the Sharma Centre for Heritage Education, led by Shanti Pappu, established a date of c. 1.5 MYA using cosmogenic nuclide burial dating.",
    "शांति पप्पू के नेतृत्व में शर्मा सेंटर फॉर हेरिटेज एजुकेशन द्वारा किए गए उत्खनन ने कॉस्मोजेनिक न्यूक्लाइड दफन तिथि निर्धारण का उपयोग करके लगभग 1.5 मिलियन वर्ष पुरानी तारीख स्थापित की।"
)

# 4. Fill in the Blank (8 Qs)
add_blank(sec1_en, sec1_hi,
    "The first Paleolithic tool in India was discovered by Robert Bruce Foote at ________ in 1863.",
    "भारत में पहला पुरापाषाणकालीन उपकरण रॉबर्ट ब्रूस फुट द्वारा 1863 में ________ में खोजा गया था।",
    "Pallavaram", "पल्लवरम",
    "Robert Bruce Foote discovered a handaxe at Pallavaram near Madras on May 30, 1863.",
    "रॉबर्ट ब्रूस फुट ने 30 मई, 1863 को मद्रास के पास पल्लवरम में एक हस्त-कुठार (handaxe) की खोज की थी।"
)
add_blank(sec1_en, sec1_hi,
    "The Bhimbetka rock shelters are situated in the Vindhyan range of the state of ________.",
    "भीमबेटका शैल आश्रय ________ राज्य की विंध्य श्रेणी में स्थित हैं।",
    "Madhya Pradesh", "मध्य प्रदेश",
    "Bhimbetka rock shelters are situated in the Raisen District of Madhya Pradesh.",
    "भीमबेटका शैल आश्रय मध्य प्रदेश के रायसेन जिले में स्थित हैं।"
)
add_blank(sec1_en, sec1_hi,
    "The excavation method that exposes large horizontal layouts of settlements is known as ________ excavation.",
    "बस्तियों के बड़े क्षैतिज लेआउट को उजागर करने वाली उत्खनन पद्धति को ________ उत्खनन के रूप में जाना जाता है।",
    "horizontal", "क्षैतिज",
    "Horizontal (or area) excavations are used to expose the spatial structure of a site during a single occupational phase.",
    "क्षैतिज (या क्षेत्र) उत्खनन का उपयोग एक ही निवास चरण के दौरान स्थल की स्थानिक संरचना को उजागर करने के लिए किया जाता है।"
)
add_blank(sec1_en, sec1_hi,
    "The earliest Neolithic village in South Asia, Mehrgarh, is situated in the modern province of ________.",
    "दक्षिण एशिया का सबसे पहला नवपाषाण गाँव, मेहरगढ़, ________ के आधुनिक प्रांत में स्थित है।",
    "Balochistan", "बलूचिस्तान",
    "Mehrgarh is located in Balochistan, Pakistan, near the Bolan Pass.",
    "मेहरगढ़ पाकिस्तान के बलूचिस्तान में बोलन दर्रे के पास स्थित है।"
)
add_blank(sec1_en, sec1_hi,
    "The excavator of the crucial Neolithic site of Mehrgarh was French archaeologist ________.",
    "महत्वपूर्ण नवपाषाण कालीन स्थल मेहरगढ़ के उत्खननकर्ता फ्रांसीसी पुरातत्वविद् ________ थे।",
    "Jean-Francois Jarrige", "ज्यां-फ्रांस्वा जारिज",
    "Jean-François Jarrige excavated Mehrgarh from 1974 to 1986.",
    "ज्यां-फ्रांस्वा जारिज ने 1974 से 1986 तक मेहरगढ़ का उत्खनन किया।"
)
add_blank(sec1_en, sec1_hi,
    "The Lower Paleolithic workshops in the Hunsgi-Baichbal valley are located in the state of ________.",
    "हुंसगी-बैचबल घाटी में निम्न पुरापाषाणकालीन कार्यशालाएँ ________ राज्य में स्थित हैं।",
    "Karnataka", "कर्नाटक",
    "Hunsgi is located in the Yadgir district of Karnataka.",
    "हुंसगी कर्नाटक के यादगीर जिले में स्थित है।"
)
add_blank(sec1_en, sec1_hi,
    "The unexcavated walls of earth left between grid trenches to monitor layers are called ________.",
    "परतों की निगरानी के लिए ग्रिड खाइयों के बीच छोड़ी गई मिट्टी की बिना खुदाई वाली दीवारों को ________ कहा जाता है।",
    "baulks", "बाल्क",
    "Baulks are narrow vertical partitions of soil left between excavation squares.",
    "बाल्क उत्खनन वर्गों के बीच छोड़े गए संकीर्ण मिट्टी के विभाजन हैं।"
)
add_blank(sec1_en, sec1_hi,
    "The site of Koldihwa, which yielded early corded pottery and rice husks, is located in the ________ river valley.",
    "कोलडिहवा स्थल, जहाँ से प्रारंभिक रज्जु-चिह्नित मिट्टी के बर्तन और धान की भूसी मिली है, ________ नदी घाटी में स्थित है।",
    "Belan", "बेलन",
    "Koldihwa is located in the Belan river valley in Uttar Pradesh.",
    "कोलडिहवा उत्तर प्रदेश में बेलन नदी घाटी में स्थित है।"
)

# 5. Match the Following (3 Qs)
add_match(sec1_en, sec1_hi,
    "Match the prehistoric excavations with their lead scholars:",
    "प्रागैतिहासिक उत्खनन को उनके प्रमुख विद्वानों के साथ सुमेलित करें:",
    [{"left": "Bhimbetka", "key": "wakankar"}, {"left": "Attirampakkam", "key": "pappu"}, {"left": "Mehrgarh", "key": "jarrige"}],
    [{"left": "भीमबेटका", "key": "wakankar"}, {"left": "अतिरम्पक्कम", "key": "pappu"}, {"left": "मेहरगढ़", "key": "jarrige"}],
    [{"val": "wakankar", "text": "V.S. Wakankar"}, {"val": "pappu", "text": "Shanti Pappu"}, {"val": "jarrige", "text": "J.F. Jarrige"}],
    [{"val": "wakankar", "text": "वी.एस. वाकणकर"}, {"val": "pappu", "text": "शांति पप्पू"}, {"val": "jarrige", "text": "जे.एफ. जारिज"}],
    "Bhimbetka was discovered by V.S. Wakankar; Attirampakkam was excavated by Shanti Pappu; Mehrgarh was excavated by Jean-François Jarrige.",
    "भीमबेटका की खोज वी.एस. वाकणकर ने की थी; अतिरम्पक्कम का उत्खनन शांति पप्पू द्वारा किया गया था; मेहरगढ़ का उत्खनन जे.एफ. जारिज द्वारा किया गया था।"
)
add_match(sec1_en, sec1_hi,
    "Match the prehistoric site with its key geographic river basin:",
    "प्रागैतिहासिक स्थल को उसके प्रमुख भौगोलिक नदी बेसिन के साथ सुमेलित करें:",
    [{"left": "Inamgaon", "key": "ghod"}, {"left": "Koldihwa", "key": "belan"}, {"left": "Bagor", "key": "kothari"}],
    [{"left": "इनामगांव", "key": "ghod"}, {"left": "कोलडिहवा", "key": "belan"}, {"left": "बागोर", "key": "kothari"}],
    [{"val": "ghod", "text": "Ghod Valley"}, {"val": "belan", "text": "Belan Valley"}, {"val": "kothari", "text": "Kothari Valley"}],
    [{"val": "ghod", "text": "घोड़ घाटी"}, {"val": "belan", "text": "बेलन घाटी"}, {"val": "kothari", "text": "कोठारी घाटी"}],
    "Inamgaon is on the Ghod, Koldihwa is in the Belan valley, and Bagor is on the Kothari River.",
    "इनामगांव घोड़ नदी पर, कोलडिहवा बेलन घाटी में, और बागोर कोठारी नदी पर स्थित है।"
)
add_match(sec1_en, sec1_hi,
    "Match the excavation methodology term with its description:",
    "उत्खनन पद्धति के शब्दों को उनके विवरण के साथ सुमेलित करें:",
    [{"left": "Baulks", "key": "walls"}, {"left": "Vertical Excavation", "key": "probe"}, {"left": "Horizontal Excavation", "key": "layout"}],
    [{"left": "बाल्क", "key": "walls"}, {"left": "लंबवत उत्खनन", "key": "probe"}, {"left": "क्षैतिज उत्खनन", "key": "layout"}],
    [{"val": "walls", "text": "Dirt partitions showing stratigraphy"}, {"val": "probe", "text": "Chronological deep probe"}, {"val": "layout", "text": "Exposing spatial town planning"}],
    [{"val": "walls", "text": "स्तरविन्यास दिखाने वाली मिट्टी की दीवारें"}, {"val": "probe", "text": "कालानुक्रमिक गहरी जांच"}, {"val": "layout", "text": "स्थानिक नगर योजना को उजागर करना"}],
    "Baulks are soil walls showing stratigraphy, vertical excavation is a chronological probe, and horizontal excavation exposes spatial layouts.",
    "बाल्क मिट्टी की दीवारें हैं जो स्तरविन्यास दिखाती हैं, लंबवत उत्खनन कालानुक्रमिक जांच है, और क्षैतिज उत्खनन स्थानिक संरचना को उजागर करता है।"
)

# 6. One-Liner (8 Qs)
add_oneliner(sec1_en, sec1_hi,
    "Who is known as the 'Father of Indian Prehistory'?",
    "किसे 'भारतीय प्रागैतिहास के जनक' के रूप में जाना जाता है?",
    "Robert Bruce Foote, a British geologist who discovered the first Paleolithic handaxe in 1863.",
    "रॉबर्ट ब्रूस फुट, एक ब्रिटिश भूविज्ञानी जिन्होंने 1863 में पहले पुरापाषाणकालीन हस्त-कुठार की खोज की थी।"
)
add_oneliner(sec1_en, sec1_hi,
    "Which excavation method is preferred to understand the horizontal layout and spatial planning of a prehistoric village?",
    "प्रागैतिहासिक गाँव के क्षैतिज लेआउट और स्थानिक योजना को समझने के लिए किस उत्खनन पद्धति को प्राथमिकता दी जाती है?",
    "Horizontal (or area) excavation method.",
    "क्षैतिज (या क्षेत्र) उत्खनन पद्धति।"
)
add_oneliner(sec1_en, sec1_hi,
    "Name the site that has yielded the earliest evidence of agricultural domestication in the Ganga Valley.",
    "गंगा घाटी में कृषि पालतू बनाने का सबसे पहला साक्ष्य देने वाले स्थल का नाम बताइए।",
    "Lahuradewa, located in Sant Kabir Nagar, Uttar Pradesh.",
    "लहुरादेवा, जो उत्तर प्रदेश के संत कबीर नगर में स्थित है।"
)
add_oneliner(sec1_en, sec1_hi,
    "Why are the rock shelters of Bhimbetka globally significant?",
    "भीमबेटका के शैल आश्रय वैश्विक स्तर पर क्यों महत्वपूर्ण हैं?",
    "They preserve a continuous sequence of rock art paintings spanning from the Upper Paleolithic to the Medieval period.",
    "वे पुरापाषाण काल से मध्यकाल तक फैले शैल चित्रों के निरंतर अनुक्रम को संरक्षित करते हैं।"
)
add_oneliner(sec1_en, sec1_hi,
    "What raw stone material was primarily used by Paleolithic toolmakers at Hunsgi?",
    "हुंसगी में पुरापाषाणकालीन उपकरण निर्माताओं द्वारा मुख्य रूप से किस कच्चे पत्थर का उपयोग किया गया था?",
    "Limestone, which was locally abundant in the Hunsgi-Baichbal valley.",
    "चूना पत्थर (limestone), जो हुंसगी-बैचबल घाटी में स्थानीय स्तर पर प्रचुर मात्रा में उपलब्ध था।"
)
add_oneliner(sec1_en, sec1_hi,
    "Which major site in Maharashtra belongs to the post-Harappan Jorwe Chalcolithic culture?",
    "महाराष्ट्र का कौन सा प्रमुख स्थल उत्तर-हड़प्पा कालीन जोर्वे ताम्रपाषाण संस्कृति से संबंधित है?",
    "Inamgaon (or Daimabad).",
    "इनामगांव (या दैमाबाद)।"
)
add_oneliner(sec1_en, sec1_hi,
    "What is the function of a 'baulk' in archaeological grid excavations?",
    "पुरातात्विक ग्रिड उत्खनन में 'बाल्क' (baulk) का क्या कार्य है?",
    "It acts as a physical wall showing the vertical stratigraphy and soil layers of the site.",
    "यह स्थल के ऊर्ध्वाधर स्तरविन्यास और मिट्टी की परतों को दिखाने वाली एक भौतिक दीवार के रूप में कार्य करता है।"
)
add_oneliner(sec1_en, sec1_hi,
    "Which Paleolithic excavation in India has been dated to c. 1.5 million years ago using cosmogenic nuclides?",
    "कॉस्मोजेनिक न्यूक्लाइड्स का उपयोग करके भारत में किस पुरापाषाणकालीन उत्खनन को लगभग 1.5 मिलियन वर्ष पुराना आंका गया है?",
    "Attirampakkam in Tamil Nadu.",
    "तमिलनाडु में अतिरम्पक्कम।"
)

# 7. Assertion-Reason (8 Qs)
add_ar(sec1_en, sec1_hi,
    "Assertion (A): Vertical excavations are referred to as chronological probes.\nReason (R): They cut deep into occupational layers to reveal historical sequences and timelines rather than wide spatial structures.",
    "कथन (A): लंबवत उत्खनन को कालानुक्रमिक जांच (chronological probes) कहा जाता है।\nकारण (R): वे व्यापक स्थानिक संरचनाओं के बजाय ऐतिहासिक अनुक्रमों और समयसीमाओं को प्रकट करने के लिए व्यावसायिक परतों में गहराई तक जाते हैं।",
    0,
    "Both A and R are true, and R is the correct explanation of A. Vertical excavations cut deep through levels specifically to build a chronology.",
    "A और R दोनों सही हैं और R, A की सही व्याख्या करता है। लंबवत उत्खनन विशेष रूप से कालक्रम बनाने के लिए परतों में गहराई तक जाता है।"
)
add_ar(sec1_en, sec1_hi,
    "Assertion (A): The Soan Valley represents a purely handaxe-dominated Acheulian culture.\nReason (R): River terraces in the northwest yielded Pebble tools (choppers) distinct from the southern bifacial traditions.",
    "कथन (A): सोहन घाटी विशुद्ध रूप से हस्त-कुठार (handaxe) प्रधान अशुली संस्कृति का प्रतिनिधित्व करती है।\nकारण (R): उत्तर-पश्चिम में नदी के छज्जों (terraces) से पत्थर के उपकरण (choppers) मिले हैं जो दक्षिणी द्विमुख परंपराओं से भिन्न हैं।",
    3,
    "A is false but R is true. The Soan valley is characterized by Soanian pebble-chopper tool traditions, not handaxe-dominated Acheulian (though some overlap occurs).",
    "A गलत है लेकिन R सही है। सोहन घाटी सोहन पेबल-चॉपर उपकरण परंपराओं की लाक्षणिक विशेषता है, न कि हस्त-कुठार प्रधान अशुली संस्कृति की।"
)
add_ar(sec1_en, sec1_hi,
    "Assertion (A): Bhimbetka shelters were selected for continuous occupation from the Paleolithic to Medieval times.\nReason (R): The site offered natural sandstones, permanent water sources, and abundant forest resources.",
    "कथन (A): भीमबेटका आश्रयों को पुरापाषाण काल से मध्यकाल तक निरंतर अधिवास के लिए चुना गया था।\nकारण (R): इस स्थल पर प्राकृतिक बलुआ पत्थर, स्थायी जल स्रोत और प्रचुर मात्रा में वन संसाधन उपलब्ध थे।",
    0,
    "Both A and R are true, and R explains why early humans continuously inhabited Bhimbetka.",
    "A और R दोनों सही हैं और R बताता है कि क्यों शुरुआती मनुष्यों ने भीमबेटका में निरंतर निवास किया।"
)
add_ar(sec1_en, sec1_hi,
    "Assertion (A): Mehrgarh is known as the breadbasket of early Balochistan.\nReason (R): It has yielded the earliest evidence of cultivated wheat and barley alongside domesticated sheep and goats in South Asia.",
    "कथन (A): मेहरगढ़ को प्रारंभिक बलूचिस्तान की अन्न-पेटी (breadbasket) के रूप में जाना जाता है।\nकारण (R): यहाँ से दक्षिण एशिया में पालतू भेड़ और बकरियों के साथ-साथ खेती की जाने वाली गेहूं और जौ के सबसे पुराने साक्ष्य मिले हैं।",
    0,
    "Both statements are true and R explains why it is called the breadbasket.",
    "दोनों कथन सही हैं और R व्याख्या करता है कि इसे अन्न-पेटी क्यों कहा जाता है।"
)
add_ar(sec1_en, sec1_hi,
    "Assertion (A): Shanti Pappu's excavations at Attirampakkam utilized vertical grid methodology.\nReason (R): Grid excavations allow precise vertical mapping of soil layers and artifact positioning.",
    "कथन (A): अतिरम्पक्कम में शांति पप्पू के उत्खनन में लंबवत ग्रिड पद्धति का उपयोग किया गया था।\nकारण (R): ग्रिड उत्खनन मिट्टी की परतों और कलाकृतियों की स्थिति का सटीक लंबवत मानचित्रण करने की अनुमति देता है।",
    1,
    "Both A and R are true but R is not the direct, unique explanation of A (it defines grid excavation generally).",
    "A और R दोनों सही हैं लेकिन R, A की सीधी व्याख्या नहीं करता है (यह ग्रिड उत्खनन को सामान्य रूप से परिभाषित करता है)।"
)
add_ar(sec1_en, sec1_hi,
    "Assertion (A): Lower Paleolithic humans are often called 'Quartzite Men' in India.\nReason (R): Quartzite was the exclusive material used throughout the Mesolithic and Neolithic periods.",
    "कथन (A): भारत में निम्न पुरापाषाणकालीन मनुष्यों को अक्सर 'क्वार्टजाइट मैन' कहा जाता है।\nकारण (R): मध्यपाषाण और नवपाषाण काल में भी विशेष रूप से क्वार्टजाइट का ही उपयोग किया गया था।",
    2,
    "A is true but R is false. Mesolithic and Neolithic tools utilized chert, chalcedony, and polished stones, not crude quartzite.",
    "A सही है लेकिन R गलत है। मध्यपाषाण और नवपाषाण कालीन उपकरणों में चर्ट, चाल्सीडोनी और पॉलिश किए गए पत्थरों का उपयोग किया गया था, न कि खुरदरे क्वार्टजाइट का।"
)
add_ar(sec1_en, sec1_hi,
    "Assertion (A): The grid method of excavation is highly superior to trial trenches.\nReason (R): It maintains unexcavated baulks that serve as permanent stratigraphical references.",
    "कथन (A): उत्खनन की ग्रिड पद्धति परीक्षण खाइयों (trial trenches) की तुलना में अत्यधिक श्रेष्ठ है।\nकारण (R): यह बिना खोदे गए बाल्क को बनाए रखती है जो स्थायी स्तरविन्यास संदर्भों के रूप में कार्य करते हैं।",
    0,
    "Both A and R are true, and R correctly explains the superiority of the grid method.",
    "A और R दोनों सही हैं और R ग्रिड पद्धति की श्रेष्ठता की सही व्याख्या करता है।"
)
add_ar(sec1_en, sec1_hi,
    "Assertion (A): Lahuradewa has disputed Mehrgarh's status as the sole earliest agricultural origin point in South Asia.\nReason (R): Domesticated rice grains at Lahuradewa date back to c. 9000-8000 BCE, indicating independent development in the Ganga basin.",
    "कथन (A): लहुरादेवा ने दक्षिण एशिया में एकमात्र सबसे पुराने कृषि मूल बिंदु के रूप में मेहरगढ़ की स्थिति को चुनौती दी है।\nकारण (R): लहुरादेवा में पालतू धान के दाने लगभग 9000-8000 ईसा पूर्व के हैं, जो गंगा बेसिन में स्वतंत्र विकास को दर्शाते हैं।",
    0,
    "Both A and R are true, and R explains why Lahuradewa challenged Mehrgarh's primacy.",
    "A और R दोनों सही हैं और R व्याख्या करता है कि क्यों लहुरादेवा ने मेहरगढ़ की प्रधानता को चुनौती दी।"
)

# 8. Statement-Based (5 Qs)
add_stmt(sec1_en, sec1_hi,
    "Consider the following statements regarding the site of Bhimbetka:\n1. It was discovered by Dr. V.S. Wakankar in 1957.\n2. It has yielded uninterrupted cultural deposits from the Lower Paleolithic to the historic period.\n3. It is situated on the Vindhyan range in Madhya Pradesh.\nWhich of the statements given above are correct?",
    "भीमबेटका स्थल के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. इसकी खोज 1957 में डॉ. वी.एस. वाकणकर ने की थी।\n2. यहाँ से निम्न पुरापाषाण काल से लेकर ऐतिहासिक काल तक के निरंतर सांस्कृतिक निक्षेप मिले हैं।\n3. यह मध्य प्रदेश में विंध्य श्रेणी पर स्थित है।\nऊपर दिए गए कथनों में से कौन से सही हैं?",
    ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
    ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
    3,
    "All three statements are correct. Bhimbetka exhibits long-term continuous human occupation and stratigraphy.",
    "तीनों कथन सही हैं। भीमबेटका दीर्घकालिक निरंतर मानव अधिवास और स्तरविन्यास प्रदर्शित करता है।"
)
add_stmt(sec1_en, sec1_hi,
    "Consider the following statements regarding excavation methodologies:\n1. Vertical excavations expose a broad spatial layout of buildings.\n2. Horizontal excavations act as deep chronological probes.\n3. The grid method was introduced in India by Mortimer Wheeler.\nWhich of the statements given above is/are correct?",
    "उत्खनन पद्धतियों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. लंबवत उत्खनन भवनों के व्यापक स्थानिक लेआउट को उजागर करता है।\n2. क्षैतिज उत्खनन गहरी कालानुक्रमिक जांच के रूप में कार्य करता है।\n3. भारत में ग्रिड पद्धति की शुरुआत मॉर्टिमर व्हीलर ने की थी।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["3 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"],
    ["केवल 3", "केवल 1 और 2", "केवल 2 और 3", "1, 2 और 3"],
    0,
    "Only statement 3 is correct. Vertical excavations are chronological probes, and horizontal excavations expose broad layouts.",
    "केवल कथन 3 सही है। लंबवत उत्खनन कालानुक्रमिक जांच है और क्षैतिज उत्खनन व्यापक लेआउट को उजागर करता है।"
)
add_stmt(sec1_en, sec1_hi,
    "Regarding the site of Mehrgarh, which of the following statements are correct?\n1. It is a Neolithic site located near the Bolan Pass.\n2. It has yielded the earliest evidence of pottery in South Asia prior to farming.\n3. Excavations show a transition from mud brick shelters to circular huts.\nWhich of the statements given above is/are correct?",
    "मेहरगढ़ स्थल के संबंध में, निम्नलिखित में से कौन से कथन सही हैं?\n1. यह बोलन दर्रे के पास स्थित एक नवपाषाण कालीन स्थल है।\n2. यहाँ से खेती से पहले दक्षिण एशिया में मिट्टी के बर्तनों के सबसे पुराने साक्ष्य मिले हैं।\n3. उत्खनन मिट्टी की ईंटों के आश्रयों से गोलाकार झोपड़ियों में संक्रमण को दर्शाता है।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 only", "1 and 3 only", "2 and 3 only", "1, 2 and 3"],
    ["केवल 1", "केवल 1 और 3", "केवल 2 और 3", "1, 2 और 3"],
    0,
    "Only statement 1 is correct. Mehrgarh did not yield pottery *prior* to farming (pottery appeared in Phase II, after farming started). shelter transition was from circular/irregular to rectangular mud-brick structures.",
    "केवल कथन 1 सही है। मेहरगढ़ में खेती से *पहले* मिट्टी के बर्तन नहीं मिले (मिट्टी के बर्तन खेती शुरू होने के बाद चरण II में दिखाई दिए)। मकानों का संक्रमण गोलाकार से आयताकार मिट्टी की ईंटों की संरचनाओं में था।"
)
add_stmt(sec1_en, sec1_hi,
    "Consider the following statements regarding the site of Attirampakkam:\n1. It has yielded evidence of Acheulian tool technology.\n2. It was excavated extensively by Robert Bruce Foote in 1863.\n3. The antiquity of the site has been dated using cosmogenic nuclide burial dating.\nWhich of the statements given above are correct?",
    "अतिरम्पक्कम स्थल के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. यहाँ से अशुली उपकरण तकनीक के साक्ष्य मिले हैं।\n2. इसका व्यापक उत्खनन 1863 में रॉबर्ट ब्रूस फुट ने किया था।\n3. इस स्थल की प्राचीनता को कॉस्मोजेनिक न्यूक्लाइड दफन तिथि निर्धारण से आंका गया है।\nऊपर दिए गए कथनों में से कौन से सही हैं?",
    ["1 and 3 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"],
    ["केवल 1 और 3", "केवल 1 और 2", "केवल 2 और 3", "1, 2 और 3"],
    0,
    "Statements 1 and 3 are correct. While Foote discovered tools near Madras in 1863, Attirampakkam's modern excavations establishing the 1.5 MYA date were directed by Shanti Pappu.",
    "कथन 1 और 3 सही हैं। हालांकि फुट ने 1863 में मद्रास के पास उपकरणों की खोज की थी, लेकिन 1.5 मिलियन वर्ष पूर्व की तारीख स्थापित करने वाले अतिरम्पक्कम के आधुनिक उत्खनन का निर्देशन शांति पप्पू ने किया था।"
)
add_stmt(sec1_en, sec1_hi,
    "With reference to the site of Inamgaon, consider the following statements:\n1. It is a large Chalcolithic settlement belonging to the Malwa culture.\n2. It has yielded evidence of a fortified wall and moat.\n3. Specialized burials of children in jars have been excavated here.\nWhich of the statements given above are correct?",
    "इनामगांव स्थल के संदर्भ में, निम्नलिखित कथनों पर विचार करें:\n1. यह मालवा संस्कृति से संबंधित एक बड़ी ताम्रपाषाण कालीन बस्ती है।\n2. यहाँ से एक किलेबंद दीवार और खाई के साक्ष्य मिले हैं।\n3. यहाँ बच्चों के घड़े में दफन (jar burials) के विशेष साक्ष्य मिले हैं।\nऊपर दिए गए कथनों में से कौन से सही हैं?",
    ["2 and 3 only", "1 and 2 only", "1 and 3 only", "1, 2 and 3"],
    ["केवल 2 और 3", "केवल 1 और 2", "केवल 1 और 3", "1, 2 और 3"],
    0,
    "Statements 2 and 3 are correct. Inamgaon belongs primarily to the Jorwe culture (c. 1400-700 BCE), not the Malwa culture.",
    "कथन 2 और 3 सही हैं। इनामगांव मुख्य रूप से जोर्वे संस्कृति (लगभग 1400-700 ईसा पूर्व) से संबंधित है, न कि मालवा संस्कृति से।"
)

# 9. Why (3 Qs)
add_open(sec1_en, sec1_hi, "Why",
    "Why are unexcavated dirt walls (baulks) left between grid trenches during archaeological excavations?",
    "पुरातात्विक उत्खनन के दौरान ग्रिड खाइयों के बीच बिना खोदे गए मिट्टी के हिस्से (बाल्क) क्यों छोड़े जाते हैं?",
    "Baulks are left as vertical dirt walls between grids to show the stratigraphy (soil layers) of the site. They allow archaeologists to draw and monitor cross-sections of soil profiles to understand the depositional history and sequence of layers.",
    "बाल्क को ग्रिडों के बीच खड़ी मिट्टी की दीवारों के रूप में छोड़ दिया जाता है ताकि स्थल के स्तरविन्यास (मिट्टी की परतों) को दिखाया जा सके। वे पुरातत्वविदों को मिट्टी के प्रोफाइल के क्रॉस-सेक्शन बनाने और परतों के जमाव के इतिहास और अनुक्रम को समझने की अनुमति देते हैं।"
)
add_open(sec1_en, sec1_hi, "Why",
    "Why is the Hathnora fossil (found in Madhya Pradesh) crucial to the study of early humans in India?",
    "मध्य प्रदेश में मिला हथनोरा जीवाश्म भारत में शुरुआती मनुष्यों के अध्ययन के लिए क्यों महत्वपूर्ण है?",
    "Hathnora yielded a skull cap (Homo erectus narmadensis) which represents the first and only human fossil of the Middle Pleistocene epoch found in the entire Indian subcontinent, confirming early hominin presence parallel to Neanderthals or Denisovans.",
    "हथनोरा से एक मानव कपाल (Homo erectus narmadensis) मिला है जो पूरे भारतीय उपद्वीप में पाया गया मध्य प्लीस्टोसीन काल का पहला और एकमात्र मानव जीवाश्म है, जो निएंडरथल या डेनिसोवन के समानांतर शुरुआती मानवों की उपस्थिति की पुष्टि करता है।"
)
add_open(sec1_en, sec1_hi, "Why",
    "Why is Lahuradewa considered a revolutionary excavation for South Asian agricultural history?",
    "लहुरादेवा को दक्षिण एशियाई कृषि इतिहास के लिए एक क्रांतिकारी उत्खनन क्यों माना जाता है?",
    "Lahuradewa pushed back the antiquity of agriculture in South Asia to c. 9000-8000 BCE by yielding domesticated rice grains. It proved that agricultural origins were not restricted to Mehrgarh (wheat/barley) but developed independently in the Ganga valley.",
    "लहुरादेवा ने पालतू धान के दानों के माध्यम से दक्षिण एशिया में कृषि की प्राचीनता को लगभग 9000-8000 ईसा पूर्व तक पीछे धकेल दिया। इसने सिद्ध किया कि कृषि की उत्पत्ति केवल मेहरगढ़ (गेहूं/जौ) तक सीमित नहीं थी, बल्कि गंगा घाटी में स्वतंत्र रूप से विकसित हुई थी।"
)

# 10. How (3 Qs)
add_open(sec1_en, sec1_hi, "How",
    "How does vertical excavation differ from horizontal excavation in its archaeological objective?",
    "पुरातात्विक उद्देश्य में लंबवत उत्खनन क्षैतिज उत्खनन से किस प्रकार भिन्न है?",
    "Vertical excavation cuts deep down in a narrow area to establish a chronological sequence of cultures (stratigraphic probe). Horizontal excavation clears a wide area of a single phase to expose structural layouts, trade patterns, and town planning.",
    "लंबवत उत्खनन संस्कृतियों के कालानुक्रमिक अनुक्रम को स्थापित करने के लिए एक संकीर्ण क्षेत्र में गहराई तक खुदाई करता है। क्षैतिज उत्खनन संरचनात्मक लेआउट, व्यापारिक पैटर्न और नगर नियोजन को उजागर करने के लिए एक ही चरण के व्यापक क्षेत्र को साफ करता है।"
)
add_open(sec1_en, sec1_hi, "How",
    "How did archaeologists date the Acheulian tools at Attirampakkam when organic remains were absent?",
    "जैविक अवशेषों की अनुपस्थिति में पुरातत्वविदों ने अतिरम्पक्कम में अशुली उपकरणों की तिथि कैसे निर्धारित की?",
    "Archaeologists used cosmogenic nuclide burial dating on the soil/sediment layers containing the stone tools. This method measures the decay of radioactive isotopes (like Beryllium-10 and Aluminum-26) in quartz grains since they were buried.",
    "पुरातत्वविदों ने पत्थर के उपकरणों से युक्त मिट्टी/तलछट की परतों पर कॉस्मोजेनिक न्यूक्लाइड दफन तिथि निर्धारण (cosmogenic nuclide burial dating) का उपयोग किया। यह विधि क्वार्ट्ज कणों के दबे होने के समय से उनमें रेडियोधर्मी समस्थानिकों (जैसे बेरिलियम-10 और एल्युमिनियम-26) के क्षय को मापती है।"
)
add_open(sec1_en, sec1_hi, "How",
    "How does the site of Hunsgi illustrate Lower Paleolithic spatial organization?",
    "हुंसगी स्थल निम्न पुरापाषाणकालीन स्थानिक संगठन को कैसे प्रदर्शित करता है?",
    "Hunsgi features distinct concentrations of limestone artifacts, tools, and debitage scattered across a valley. This shows a settlement-subsistence pattern where hominins used tool factory/workshop sites alongside springs for manufacturing, returning repeatedly.",
    "हुंसगी में एक घाटी में बिखरे हुए चूना पत्थर की कलाकृतियों, उपकरणों और मलबे (debitage) का विशिष्ट संकेंद्रण मिलता है। यह एक बस्ती-निर्वाह प्रतिरूप को दर्शाता है जहाँ मानवों ने विनिर्माण के लिए झरनों के पास उपकरण कारखानों/कार्यशालाओं का उपयोग किया।"
)

# 11. Case Study (3 Qs)
add_open(sec1_en, sec1_hi, "Case Study",
    "An archaeologist finds a site with stratified layers: Layer 1 (top) has iron sickles and black-and-red pottery; Layer 2 has tiny geometric blades (microliths) with no metals; Layer 3 has crude handaxes. Reconstruct the chronological transition of this site.",
    "एक पुरातत्वविद् को एक स्थल मिलता है जिसमें कई परतें हैं: परत 1 (शीर्ष) में लोहे की हंसिया और काले-लाल मिट्टी के बर्तन हैं; परत 2 में बिना धातुओं के छोटे ज्यामितीय ब्लेड (microliths) हैं; परत 3 में खुरदरे हस्त-कुठार हैं। इस स्थल के कालानुक्रमिक संक्रमण का पुनर्निर्माण करें।",
    "This site represents a classic evolutionary sequence of prehistory and protohistory: Layer 3 represents the Paleolithic period (crude handaxes), Layer 2 represents a transition to the Mesolithic period (microliths), and Layer 1 represents the transition to the Iron Age (iron sickles and specialized pottery).",
    "यह स्थल प्रागैतिहास और आदि-इतिहास के एक उत्कृष्ट विकासात्मक अनुक्रम का प्रतिनिधित्व करता है: परत 3 पुरापाषाण काल (खुरदरे हस्त-कुठार) का प्रतिनिधित्व करती है, परत 2 मध्यपाषाण काल (microliths) में संक्रमण को दर्शाती है, और परत 1 लौह युग (लोहे की हंसिया और विशेष मिट्टी के बर्तन) में संक्रमण को प्रदर्शित करती है।"
)
add_open(sec1_en, sec1_hi, "Case Study",
    "During excavations in a valley, a team uncovers an area filled with stone chips and half-finished tools, but no domestic pottery, hearths, or animal bones. Reconstruct the function of this site.",
    "एक घाटी में उत्खनन के दौरान, एक टीम को पत्थर के टुकड़ों और आधे-अधूरे उपकरणों से भरा क्षेत्र मिलता है, लेकिन वहाँ कोई घरेलू मिट्टी के बर्तन, चूल्हे या जानवरों की हड्डियाँ नहीं हैं। इस स्थल के कार्य का पुनर्निर्माण करें।",
    "The absence of hearths, bones, and domestic wares combined with massive debitage (chips) and unfinished tools indicates this was a specialized factory or workshop site. Hominins came here to exploit local stone resources to manufacture tools and carried finished tools to their habitation areas.",
    "चूल्हों, हड्डियों और घरेलू बर्तनों की अनुपस्थिति के साथ-साथ बड़े पैमाने पर मलबे (पत्थर के टुकड़े) और अधूरे उपकरणों की उपस्थिति यह दर्शाती है कि यह एक विशेष कार्यशाला या उपकरण निर्माण स्थल था। मानव यहाँ स्थानीय पत्थर संसाधनों का उपयोग करके उपकरण बनाने आते थे और तैयार उपकरणों को अपने निवास स्थानों पर ले जाते थे।"
)
add_open(sec1_en, sec1_hi, "Case Study",
    "At a river basin site, early layers show animal bones that are 80% wild species (deer, rhinos). Later strata show bones that are 70% domestic species (cattle, sheep). Reconstruct the socio-economic change that occurred.",
    "एक नदी बेसिन स्थल पर, प्रारंभिक परतों में जानवरों की हड्डियाँ दिखाई देती हैं जो 80% जंगली प्रजातियाँ (हिरण, गैंडे) हैं। बाद की परतों में ऐसी हड्डियाँ मिलती हैं जो 70% पालतू प्रजातियाँ (मवेशी, भेड़) हैं। यहाँ हुए सामाजिक-आर्थिक बदलाव का पुनर्निर्माण करें।",
    "This sequence reflects a clear transition from a hunter-gatherer economy (dependent on wild game) to a pastoralist/domesticated economy (animal husbandry). This represents the transitional Mesolithic phase or early Neolithic revolution where animal taming replaced wild hunting.",
    "यह अनुक्रम एक शिकारी-संग्रहकर्ता अर्थव्यवस्था (जंगली जानवरों पर निर्भर) से एक चरवाहा/पालतू अर्थव्यवस्था (पशुपालन) में स्पष्ट संक्रमण को दर्शाता है। यह मध्यपाषाण काल के संक्रमणकालीन चरण या प्रारंभिक नवपाषाण क्रांति का प्रतिनिधित्व करता है जहाँ जानवरों को पालतू बनाने ने जंगली शिकार का स्थान ले लिया।"
)

# 12. Teach the Concept (3 Qs)
add_open(sec1_en, sec1_hi, "Teach the Concept",
    "Explain the concept of stratigraphic superposition to a beginner. Use a common daily-life analogy.",
    "शुरुआती शिक्षार्थी को स्तरविन्यास सुपरपोजिशन (stratigraphic superposition) की अवधारणा समझाएं। दैनिक जीवन के एक सामान्य उदाहरण का उपयोग करें।",
    "Stratigraphic superposition is the rule that older things lie at the bottom, and newer things lie on top. A great analogy is a laundry basket: the clothes you wore on Monday are at the absolute bottom, while the clothes you wore on Friday are on the top. Similarly, in soil, older historical layers are buried deepest, while newer layers sit closest to the surface.",
    "स्तरविन्यास सुपरपोजिशन (stratigraphic superposition) का नियम यह है कि पुरानी चीजें नीचे होती हैं और नई चीजें ऊपर होती हैं। इसका एक बेहतरीन उदाहरण कपड़ों की टोकरी (laundry basket) है: जो कपड़े आपने सोमवार को पहने थे वे सबसे नीचे होंगे, जबकि जो कपड़े आपने शुक्रवार को पहने थे वे सबसे ऊपर होंगे। इसी तरह, मिट्टी में भी, पुरानी ऐतिहासिक परतें सबसे गहराई में दबी होती हैं, जबकि नई परतें सतह के सबसे करीब होती हैं।"
)
add_open(sec1_en, sec1_hi, "Teach the Concept",
    "How would you explain the difference between vertical and horizontal excavations? Create a mnemonic or visual trick.",
    "आप लंबवत और क्षैतिज उत्खनन के बीच के अंतर को कैसे समझाएंगे? कोई स्मृति सूत्र या दृश्य युक्ति बनाएं।",
    "Think of a cake: Vertical excavation is like cutting a single, deep slice of cake to see all the colorful layers inside (the chronological timeline). Horizontal excavation is like peeling off the entire top layer of frosting to see the design spread across the cake (the settlement layout). Vertical is a 'Time Probe', Horizontal is a 'Space Map'.",
    "एक केक के बारे में सोचें: लंबवत (vertical) उत्खनन केक के एक संकीर्ण लेकिन गहरे टुकड़े को काटने जैसा है ताकि अंदर की सभी रंगीन परतें (कालानुक्रमिक समयरेखा) देखी जा सकें। क्षैतिज (horizontal) उत्खनन केक के ऊपर की पूरी परत को हटाने जैसा है ताकि केक पर फैले डिजाइन (बस्ती का लेआउट) को देखा जा सके। लंबवत एक 'टाइम प्रोब' है, क्षैतिज एक 'स्पेस मैप' है।"
)
add_open(sec1_en, sec1_hi, "Teach the Concept",
    "Explain why Mehrgarh is called the 'cradle of agriculture' in the Indian subcontinent.",
    "समझाइए कि मेहरगढ़ को भारतीय उपमहाद्वीप में 'कृषि का पालना' (cradle of agriculture) क्यों कहा जाता है।",
    "Mehrgarh is called the cradle of agriculture because it shows the transition from hunting-gathering to settled farming (c. 7000 BCE). It is the earliest site in South Asia with mud-brick granaries, domesticated sheep/goats, and cultivated barley/wheat, marking the dawn of the Neolithic revolution in the subcontinent.",
    "मेहरगढ़ को कृषि का पालना कहा जाता है क्योंकि यह शिकार-संग्रहण से व्यवस्थित कृषि (लगभग 7000 ईसा पूर्व) में संक्रमण को दर्शाता है। यह दक्षिण एशिया का सबसे पुराना स्थल है जहाँ मिट्टी की ईंटों के अन्नभंडार, पालतू भेड़/बकरियाँ और खेती किए जाने वाले जौ/गेहूं के साक्ष्य मिले हैं, जो उपमहाद्वीप में नवपाषाण काल की शुरुआत का प्रतीक है।"
)

# ==========================================
# SECTION 2: EPIGRAPHY & NUMISMATICS
# ==========================================

# 1. MCQ (5 Qs)
add_mcq(sec2_en, sec2_hi,
    "The study of inscriptions is known as ________, while the study of historical handwriting style is called ________.",
    "शिलालेखों के अध्ययन को ________ के रूप में जाना जाता है, जबकि ऐतिहासिक हस्तलेखन शैली के अध्ययन को ________ कहा जाता है।",
    ["Palaeography, Epigraphy", "Epigraphy, Palaeography", "Numismatics, Epigraphy", "Archaeology, Palaeography"],
    ["पुरालिपि शास्त्र, पुरालेख शास्त्र", "पुरालेख शास्त्र, पुरालिपि शास्त्र", "मुद्राशास्त्र, पुरालेख शास्त्र", "पुरातत्व, पुरालिपि शास्त्र"],
    1,
    "Epigraphy is the study of inscriptions. Palaeography is the study of ancient writing styles and handwriting scripts.",
    "पुरालेखशास्त्र (Epigraphy) शिलालेखों का अध्ययन है। पुरालिपिशास्त्र (Palaeography) प्राचीन लेखन शैलियों और लिपियों का अध्ययन है।"
)
add_mcq(sec2_en, sec2_hi,
    "Which British scholar deciphered the Brahmi script on Ashokan inscriptions in the year 1837?",
    "किस ब्रिटिश विद्वान ने वर्ष 1837 में अशोक के शिलालेखों पर अंकित ब्राह्मी लिपि को पढ़ा था?",
    ["Alexander Cunningham", "John Marshall", "James Prinsep", "Mortimer Wheeler"],
    ["अलेक्जेंडर कनिंघम", "जॉन मार्शल", "जेम्स प्रिंसेप", "मॉर्टिमर व्हीलर"],
    2,
    "James Prinsep, the founding editor of the Journal of the Asiatic Society of Bengal, deciphered Brahmi in 1837.",
    "बंगाल की एशियाटिक सोसाइटी के जर्नल के संस्थापक संपादक जेम्स प्रिंसेप ने 1837 में ब्राह्मी लिपि को पढ़ा था।"
)
add_mcq(sec2_en, sec2_hi,
    "Which is the earliest copper-plate inscription in India that mentions famine relief measures, believed to be Mauryan?",
    "भारत का सबसे पहला ताम्रपत्र शिलालेख कौन सा है जिसमें अकाल राहत उपायों का उल्लेख है और जिसे मौर्यकालीन माना जाता है?",
    ["Junagadh Plate", "Sohgaura Plate", "Aihole Plate", "Allahabad Prasasti"],
    ["जूनागढ़ पत्र", "सोहगौरा पत्र", "ऐहोल पत्र", "इलाहाबाद प्रशस्ति"],
    1,
    "The Sohgaura copper plate (Gorakhpur, UP) is the earliest known copper plate in India, written in Brahmi, detailing state storehouse famine distribution.",
    "सोहगौरा ताम्रपत्र (गोरखपुर, उत्तर प्रदेश) भारत में पहला ज्ञात ताम्रपत्र है, जो ब्राह्मी में लिखा गया है और जिसमें राजकीय अन्नागारों से अकाल वितरण का विवरण है।"
)
add_mcq(sec2_en, sec2_hi,
    "Which dynasty introduced the first gold coins in India with portraits of kings and bilingual legends?",
    "किस राजवंश ने राजाओं के चित्रों और द्विभाषी लेखों के साथ भारत में पहले सोने के सिक्के जारी किए थे?",
    ["Kushanas", "Guptas", "Indo-Greeks", "Mauryas"],
    ["कुषाण", "गुप्त", "हिंद-यूनानी (Indo-Greeks)", "मौर्य"],
    2,
    "Indo-Greek rulers (c. 2nd century BCE) were the first to issue coins with portraits and bilingual (Greek/Kharoshthi) legends in India.",
    "हिंद-यूनानी शासकों (लगभग दूसरी शताब्दी ईसा पूर्व) ने भारत में सबसे पहले चित्रों और द्विभाषी (यूनानी/खरोष्ठी) लेखों वाले सिक्के जारी किए थे।"
)
add_mcq(sec2_en, sec2_hi,
    "The study of coins, which includes their composition, weight standards, and minting techniques, is called:",
    "सिक्कों का अध्ययन, जिसमें उनकी संरचना, वजन मानकों और ढलाई की तकनीकों का अध्ययन शामिल है, क्या कहलाता है?",
    ["Epigraphy", "Numismatics", "Palaeography", "Sigillography"],
    ["पुरालेखशास्त्र", "मुद्राशास्त्र (Numismatics)", "पुरालिपिशास्त्र", "मुहरशास्त्र"],
    1,
    "Numismatics is the scientific study of coins, tokens, paper money, and related objects.",
    "मुद्राशास्त्र (Numismatics) सिक्कों, टोकनों, कागजी मुद्रा और संबंधित वस्तुओं का वैज्ञानिक अध्ययन है।"
)

# 2. Multiple Correct MCQ (5 Qs)
add_multi_mcq(sec2_en, sec2_hi,
    "Which of the following scripts were used in the inscriptions of Ashoka? (Select all that apply)",
    "अशोक के शिलालेखों में निम्नलिखित में से किन लिपियों का उपयोग किया गया था? (सभी लागू विकल्प चुनें)",
    ["Brahmi", "Kharoshthi", "Aramaic", "Harappan Pictographic"],
    ["ब्राह्मी", "खरोष्ठी", "अरामी", "हड़प्पा चित्रलिपि"],
    [0, 1, 2],
    "Ashokan inscriptions used Brahmi (major), Kharoshthi (northwest), Aramaic, and Greek scripts.",
    "अशोक के शिलालेखों में ब्राह्मी (मुख्य), खरोष्ठी (उत्तर-पश्चिम), अरामी और यूनानी लिपियों का उपयोग किया गया था।"
)
add_multi_mcq(sec2_en, sec2_hi,
    "Which metals were primarily used to manufacture the earliest Punch-Marked Coins (c. 6th cent. BCE)? (Select all that apply)",
    "लगभग छठी शताब्दी ईसा पूर्व के सबसे पुराने आहत (पंच-मार्क) सिक्कों के निर्माण में मुख्य रूप से किन धातुओं का उपयोग किया गया था? (सभी लागू विकल्प चुनें)",
    ["Silver", "Copper", "Gold", "Lead"],
    ["चांदी", "तांबा", "सोना", "सीसा"],
    [0, 1],
    "The earliest punch-marked coins (c. 6th century BCE) were minted in silver and copper. Gold coins appeared much later.",
    "सबसे पुराने आहत सिक्के (लगभग छठी शताब्दी ईसा पूर्व) चांदी और तांबे में ढाले गए थे। सोने के सिक्के बहुत बाद में आए।"
)
add_multi_mcq(sec2_en, sec2_hi,
    "Which of the following descriptions accurately characterize Kharoshthi script? (Select all that apply)",
    "निम्नलिखित में से कौन से विवरण खरोष्ठी लिपि को सटीक रूप से चित्रित करते हैं? (सभी लागू विकल्प चुनें)",
    ["Written from right to left", "Used in northwestern India", "Derived from Aramaic influence", "Deciphered by James Prinsep in 1837"],
    ["दाएं से बाएं लिखी जाती थी", "उत्तर-पश्चिमी भारत में उपयोग की जाती थी", "अरामी प्रभाव से विकसित हुई थी", "1837 में जेम्स प्रिंसेप द्वारा पढ़ी गई थी"],
    [0, 1, 2],
    "Kharoshthi script is written right to left, used in the northwest under Aramaic influence, and deciphered primarily by James Prinsep, Lassen, and Norris in the 1830s.",
    "खरोष्ठी लिपि दाएं से बाएं लिखी जाती थी, अरामी प्रभाव के तहत उत्तर-पश्चिम में उपयोग की जाती थी, और मुख्य रूप से 1830 के दशक में जेम्स प्रिंसेप, लासेन और नोरिस द्वारा पढ़ी गई थी।"
)
add_multi_mcq(sec2_en, sec2_hi,
    "Which of the following inscriptions contain records of the Saka ruler Rudradaman I? (Select all that apply)",
    "निम्नलिखित में से किस शिलालेख में शक शासक रुद्रदामन प्रथम का रिकॉर्ड है? (सभी लागू विकल्प चुनें)",
    ["Junagadh Rock Inscription", "Allahabad Prasasti", "Sohgaura Copper Plate", "Aihole Inscription"],
    ["जूनागढ़ शैल शिलालेख", "इलाहाबाद प्रशस्ति", "सोहगौरा ताम्रपत्र", "ऐहोल शिलालेख"],
    [0],
    "Rudradaman I's famous Sanskrit inscription is located on the rock at Junagadh (Gujarat).",
    "रुद्रदामन प्रथम का प्रसिद्ध संस्कृत शिलालेख जूनागढ़ (गुजरात) की चट्टान पर स्थित है।"
)
add_multi_mcq(sec2_en, sec2_hi,
    "Which elements can be analyzed using Numismatics to reconstruct historical realities? (Select all that apply)",
    "ऐतिहासिक वास्तविकताओं के पुनर्निर्माण के लिए मुद्राशास्त्र (Numismatics) का उपयोग करके निम्नलिखित में से किन तत्वों का विश्लेषण किया जा सकता है? (सभी लागू विकल्प चुनें)",
    ["Trade and economic networks", "Territorial extent of kingdoms", "Metallurgical progress", "Decipherment of spoken languages"],
    ["व्यापार और आर्थिक नेटवर्क", "राज्यों की क्षेत्रीय सीमा", "धातुकर्म की प्रगति", "बोली जाने वाली भाषाओं का अनुवाद"],
    [0, 1, 2],
    "Coins indicate economy, territory, and metallurgy. They represent written scripts but do not directly record spoken languages.",
    "सिक्के अर्थव्यवस्था, क्षेत्र और धातुकर्म को दर्शाते हैं। वे लिखित लिपियों का प्रतिनिधित्व करते हैं लेकिन सीधे बोली जाने वाली भाषाओं को रिकॉर्ड नहीं करते हैं।"
)

# 3. True/False (8 Qs)
add_tf(sec2_en, sec2_hi,
    "The Kharoshthi script was written from left to right, similar to Brahmi.",
    "खरोष्ठी लिपि ब्राह्मी की तरह ही बाएं से दाएं लिखी जाती थी।",
    False,
    "Kharoshthi was written from right to left, while Brahmi was written from left to right.",
    "खरोष्ठी दाएं से बाएं लिखी जाती थी, जबकि ब्राह्मी बाएं से दाएं लिखी जाती थी।"
)
add_tf(sec2_en, sec2_hi,
    "Punch-marked coins bear legends of kings detailing their dates of coronation.",
    "आहत (पंच-मार्क) सिक्कों पर राजाओं के लेख मिलते हैं जिनमें उनके राज्याभिषेक की तिथियों का विवरण होता है।",
    False,
    "Punch-marked coins contain only symbols (hills, tree, sun) punched onto metal blanks; they do not contain written legends of kings.",
    "आहत सिक्कों पर धातु के टुकड़ों पर केवल प्रतीक (पहाड़, पेड़, सूर्य) अंकित होते थे; इनमें राजाओं के लिखे हुए लेख नहीं होते थे।"
)
add_tf(sec2_en, sec2_hi,
    "The earliest deciphered inscriptions in India are written in the Brahmi script.",
    "भारत में सबसे पहले पढ़े गए शिलालेख ब्राह्मी लिपि में लिखे गए हैं।",
    True,
    "The Ashokan edicts (3rd century BCE) in Brahmi are the earliest deciphered written records in India.",
    "ब्राह्मी में लिखे अशोक के शिलालेख (तीसरी शताब्दी ईसा पूर्व) भारत में सबसे पुराने पढ़े गए लिखित रिकॉर्ड हैं।"
)
add_tf(sec2_en, sec2_hi,
    "Palaeography is the science of reconstructing ancient languages from written inscriptions.",
    "पुरालिपिशास्त्र (Palaeography) लिखित शिलालेखों से प्राचीन भाषाओं के पुनर्निर्माण का विज्ञान है।",
    False,
    "Palaeography is the study of ancient writing styles and evolution of scripts, not languages.",
    "पुरालिपिशास्त्र प्राचीन लेखन शैलियों और लिपियों के विकास का अध्ययन है, न कि भाषाओं का।"
)
add_tf(sec2_en, sec2_hi,
    "The Sohgaura copper plate inscription is written in Prakrit and Brahmi script.",
    "सोहगौरा ताम्रपत्र शिलालेख प्राकृत भाषा और ब्राह्मी लिपि में लिखा गया है।",
    True,
    "The Sohgaura plate is written in the Prakrit language using Ashokan Brahmi characters.",
    "सोहगौरा पत्र प्राकृत भाषा में अशोक कालीन ब्राह्मी अक्षरों का उपयोग करके लिखा गया है।"
)
add_tf(sec2_en, sec2_hi,
    "Indian gold coins were minted in the largest quantities during the Gupta Empire.",
    "भारतीय सोने के सिक्के गुप्त साम्राज्य के दौरान सबसे बड़ी मात्रा में ढाले गए थे।",
    True,
    "Guptas issued the largest number of gold coins (known as dinars), depicting rich artistic variants, though Kushanas issued gold coins with higher purity.",
    "गुप्तों ने सबसे बड़ी संख्या में सोने के सिक्के जारी किए (जिन्हें दीनार कहा जाता था), जिनमें समृद्ध कलात्मक विविधताएँ थीं, हालांकि कुषाणों ने उच्च शुद्धता वाले सोने के सिक्के जारी किए थे।"
)
add_tf(sec2_en, sec2_hi,
    "Punch-marked coins were manufactured by casting molten metal in pre-designed clay molds.",
    "आहत सिक्कों का निर्माण पिघली हुई धातु को पूर्व-निर्मित मिट्टी के सांचों में ढालकर किया जाता था।",
    False,
    "Punch-marked coins were made by cutting metal sheets into shapes and then punching symbols onto them, not by casting in molds.",
    "आहत सिक्के धातु की चादरों को आकृतियों में काटकर और फिर उन पर प्रतीकों को हथौड़े से अंकित करके बनाए जाते थे, न कि सांचों में ढालकर।"
)
add_tf(sec2_en, sec2_hi,
    "James Prinsep deciphered the Brahmi script while serving as an officer in the Mint of Calcutta.",
    "जेम्स प्रिंसेप ने कलकत्ता के टकसाल (Mint) में एक अधिकारी के रूप में कार्य करते हुए ब्राह्मी लिपि को पढ़ा था।",
    True,
    "James Prinsep was an assay master in the Calcutta Mint, which gave him deep experience in coin metals and scripts.",
    "जेम्स प्रिंसेप कलकत्ता टकसाल में एसे मास्टर (परखकर्ता) थे, जिससे उन्हें सिक्कों की धातुओं और लिपियों में गहरा अनुभव मिला।"
)

# 4. Fill in the Blank (8 Qs)
add_blank(sec2_en, sec2_hi,
    "The science of studying inscriptions engraved on stone, clay, or copper is called ________.",
    "पत्थर, मिट्टी या तांबे पर खुदे हुए शिलालेखों के अध्ययन के विज्ञान को ________ कहा जाता है।",
    "epigraphy", "पुरालेखशास्त्र",
    "Epigraphy is the branch of science dedicated to deciphering and reading inscriptions.",
    "पुरालेखशास्त्र शिलालेखों को पढ़ने और उनका अर्थ निकालने के लिए समर्पित विज्ञान की शाखा है।"
)
add_blank(sec2_en, sec2_hi,
    "The Brahmi script on Ashokan edicts was deciphered in the year ________.",
    "अशोक के शिलालेखों पर ब्राह्मी लिपि को वर्ष ________ में पढ़ा गया था।",
    "1837", "1837",
    "James Prinsep successfully deciphered the script in 1837.",
    "जेम्स प्रिंसेप ने 1837 में सफलतापूर्वक लिपि को पढ़ा था।"
)
add_blank(sec2_en, sec2_hi,
    "The earliest coins of India, which lacked inscriptions and had only symbols, are called ________ coins.",
    "भारत के सबसे पुराने सिक्के, जिनमें लेख नहीं थे और केवल प्रतीक थे, ________ सिक्के कहलाते हैं।",
    "punch-marked", "आहत",
    "These are called punch-marked coins (or Aahat coins in Hindi) due to symbols being punched individually onto sheets.",
    "इन्हें धातु की चादरों पर अलग-अलग प्रतीकों को अंकित किए जाने के कारण आहत (या पंच-मार्क) सिक्के कहा जाता है।"
)
add_blank(sec2_en, sec2_hi,
    "The famous Junagadh Rock Inscription of Rudradaman I is the first major inscription written in ________ language.",
    "रुद्रदामन प्रथम का प्रसिद्ध जूनागढ़ शैल शिलालेख ________ भाषा में लिखा गया पहला प्रमुख शिलालेख है।",
    "Sanskrit", "संस्कृत",
    "The Junagadh inscription (c. 150 CE) is the first major long inscription written in classical Sanskrit.",
    "जूनागढ़ शिलालेख (लगभग 150 ईस्वी) शास्त्रीय संस्कृत में लिखा गया पहला प्रमुख लंबा शिलालेख है।"
)
add_blank(sec2_en, sec2_hi,
    "Gupta gold coins are officially designated in contemporary inscriptions as ________.",
    "गुप्तकालीन सोने के सिक्कों को समकालीन शिलालेखों में आधिकारिक तौर पर ________ के रूप में नामित किया गया है।",
    "dinars", "दीनार",
    "Contemporary Gupta inscriptions refer to gold coins as 'dinars', derived from the Roman denarius.",
    "समकालीन गुप्त शिलालेख सोने के सिक्कों को 'दीनार' कहते हैं, जो रोमन डेनारियस से लिया गया है।"
)
add_blank(sec2_en, sec2_hi,
    "The ancient writing style found in northwestern Ashokan edicts, written from right to left, is ________.",
    "उत्तर-पश्चिमी अशोक के शिलालेखों में पाई जाने वाली प्राचीन लेखन शैली, जो दाएं से बाएं लिखी जाती थी, ________ है।",
    "Kharoshthi", "खरोष्ठी",
    "Kharoshthi script was used primarily in the Gandhara region.",
    "खरोष्ठी लिपि का उपयोग मुख्य रूप से गांधार क्षेत्र में किया जाता था।"
)
add_blank(sec2_en, sec2_hi,
    "The study of seals and clay stampings used to authenticate ancient trade packages is called ________.",
    "प्राचीन व्यापारिक पैकेजों को प्रमाणित करने के लिए उपयोग की जाने वाली मुहरों और मिट्टी के छापों के अध्ययन को ________ कहा जाता है।",
    "sigillography", "मुहरशास्त्र",
    "Sigillography (or sphragistics) is the study of wax, clay, or lead seals.",
    "मुहरशास्त्र (Sigillography) मोम, मिट्टी या सीसे की मुहरों का अध्ययन है।"
)
add_blank(sec2_en, sec2_hi,
    "The earliest written records of India, still undeciphered, belong to the ________ Civilization.",
    "भारत के सबसे प्राचीन लिखित रिकॉर्ड, जो अभी भी पढ़े नहीं जा सके हैं, ________ सभ्यता के हैं।",
    "Harappan", "हड़प्पा",
    "Harappan pictographic seals represent the earliest writing in South Asia but remain undeciphered.",
    "हड़प्पा की मुहरें दक्षिण एशिया में सबसे प्राचीन लेखन का प्रतिनिधित्व करती हैं लेकिन अभी तक अपठित हैं।"
)

# 5. Match the Following (3 Qs)
add_match(sec2_en, sec2_hi,
    "Match the ancient inscriptions with their associated rulers:",
    "प्राचीन शिलालेखों को उनके संबद्ध शासकों के साथ सुमेलित करें:",
    [{"left": "Allahabad Prasasti", "key": "samudragupta"}, {"left": "Junagadh Rock Inscription", "key": "rudradaman"}, {"left": "Aihole Inscription", "key": "pulakeshin"}],
    [{"left": "इलाहाबाद प्रशस्ति", "key": "samudragupta"}, {"left": "जूनागढ़ शैल शिलालेख", "key": "rudradaman"}, {"left": "ऐहोल शिलालेख", "key": "pulakeshin"}],
    [{"val": "samudragupta", "text": "Samudragupta"}, {"val": "rudradaman", "text": "Rudradaman I"}, {"val": "pulakeshin", "text": "Pulakeshin II"}],
    [{"val": "samudragupta", "text": "समुद्रगुप्त"}, {"val": "rudradaman", "text": "रुद्रदामन प्रथम"}, {"val": "pulakeshin", "text": "पुलकेशिन द्वितीय"}],
    "Allahabad Prasasti belongs to Samudragupta; Junagadh is of Rudradaman I; Aihole belongs to Chalukya ruler Pulakeshin II.",
    "इलाहाबाद प्रशस्ति समुद्रगुप्त की है; जूनागढ़ रुद्रदामन प्रथम का है; ऐहोल चालुक्य शासक पुलकेशिन द्वितीय से संबंधित है।"
)
add_match(sec2_en, sec2_hi,
    "Match the script with its writing direction:",
    "लिपि को उसकी लेखन दिशा के साथ सुमेलित करें:",
    [{"left": "Brahmi", "key": "left-to-right"}, {"left": "Kharoshthi", "key": "right-to-left"}, {"left": "Boustrophedon", "key": "alternate"}],
    [{"left": "ब्राह्मी", "key": "left-to-right"}, {"left": "खरोष्ठी", "key": "right-to-left"}, {"left": "बूस्ट्रोफेडन", "key": "alternate"}],
    [{"val": "left-to-right", "text": "Left to Right"}, {"val": "right-to-left", "text": "Right to Left"}, {"val": "alternate", "text": "Alternate lines left/right"}],
    [{"val": "left-to-right", "text": "बाएं से दाएं"}, {"val": "right-to-left", "text": "दाएं से बाएं"}, {"val": "alternate", "text": "एक रेखा बाएं से दाएं, अगली दाएं से बाएं"}],
    "Brahmi is left to right, Kharoshthi is right to left, and Boustrophedon alternates directions.",
    "ब्राह्मी बाएं से दाएं लिखी जाती है, खरोष्ठी दाएं से बाएं लिखी जाती है, और बूस्ट्रोफेडन बारी-बारी से दिशा बदलती है।"
)
add_match(sec2_en, sec2_hi,
    "Match the coin type with its historical significance:",
    "सिक्कों के प्रकार को उनके ऐतिहासिक महत्व के साथ सुमेलित करें:",
    [{"left": "Punch-Marked Coins", "key": "earliest"}, {"left": "Indo-Greek Coins", "key": "portraits"}, {"left": "Gupta Dinars", "key": "largest-gold"}],
    [{"left": "आहत सिक्के", "key": "earliest"}, {"left": "हिंद-यूनानी सिक्के", "key": "portraits"}, {"left": "गुप्त दीनार", "key": "largest-gold"}],
    [{"val": "earliest", "text": "Earliest Indian metallic currency"}, {"val": "portraits", "text": "Introduced portraits & legends"}, {"val": "largest-gold", "text": "Minted largest numbers of gold coins"}],
    [{"val": "earliest", "text": "सबसे पुरानी भारतीय धातु मुद्रा"}, {"val": "portraits", "text": "चित्र और लेखों की शुरुआत की"}, {"val": "largest-gold", "text": "सबसे बड़ी संख्या में सोने के सिक्के ढाले"}],
    "Punch-marked coins are the earliest currency, Indo-Greeks introduced portraits, and Guptas minted the largest number of gold coins.",
    "आहत सिक्के सबसे पुरानी मुद्रा हैं, हिंद-यूनानियों ने चित्रों की शुरुआत की, और गुप्तों ने सबसे बड़ी संख्या में सोने के सिक्के ढाले।"
)

# 6. One-Liner (8 Qs)
add_oneliner(sec2_en, sec2_hi,
    "What is the term for the study of seals and sealings?",
    "मुहरों और उनके छापों के अध्ययन के लिए क्या शब्द है?",
    "Sigillography (or Sphragistics).",
    "मुहरशास्त्र (Sigillography या Sphragistics)।"
)
add_oneliner(sec2_en, sec2_hi,
    "Which script did James Prinsep decipher to read Mauryan records in 1837?",
    "1837 में मौर्यकालीन रिकॉर्ड को पढ़ने के लिए जेम्स प्रिंसेप ने किस लिपि को पढ़ा था?",
    "Brahmi script.",
    "ब्राह्मी लिपि।"
)
add_oneliner(sec2_en, sec2_hi,
    "Why are punch-marked coins called 'punch-marked'?",
    "आहत (punch-marked) सिक्कों को 'आहत' क्यों कहा जाता है?",
    "Because symbols were punched individually onto ready-cut sheets of metal, rather than cast from molds.",
    "क्योंकि मिट्टी के सांचों में ढालने के बजाय तैयार धातु की चादरों पर अलग-अलग प्रतीकों को आहत (punch) किया जाता था।"
)
add_oneliner(sec2_en, sec2_hi,
    "What language was used in the earliest deciphered inscriptions of India?",
    "भारत के सबसे पहले पढ़े गए शिलालेखों में किस भाषा का उपयोग किया गया था?",
    "Prakrit language (written in Brahmi script).",
    "प्राकृत भाषा (ब्राह्मी लिपि में लिखित)।"
)
add_oneliner(sec2_en, sec2_hi,
    "Which Gupta ruler is depicted on coins playing the lute (veena)?",
    "सिक्कों पर किस गुप्त शासक को वीणा बजाते हुए दिखाया गया है?",
    "Samudragupta.",
    "समुद्रगुप्त।"
)
add_oneliner(sec2_en, sec2_hi,
    "Name the oldest deciphered Sanskrit inscription found in western India.",
    "पश्चिमी भारत में पाए गए सबसे पुराने पढ़े गए संस्कृत शिलालेख का नाम बताइए।",
    "Junagadh Rock Inscription of Rudradaman I (c. 150 CE).",
    "रुद्रदामन प्रथम का जूनागढ़ शैल शिलालेख (लगभग 150 ईस्वी)।"
)
add_oneliner(sec2_en, sec2_hi,
    "Why did the Indo-Greeks coin system represent a major technological advance over punch-marked coins?",
    "हिंद-यूनानी सिक्का प्रणाली आहत सिक्कों की तुलना में एक बड़ा तकनीकी सुधार क्यों थी?",
    "They introduced die-striking methods that allowed portraiture and bilingual legends, rather than irregular stamps.",
    "उन्होंने डाई-स्ट्राइकिंग (ठप्पा लगाने की) पद्धति की शुरुआत की जिसने अनियमित छापों के स्थान पर चित्रों और द्विभाषी लेखों को छापने की अनुमति दी।"
)
add_oneliner(sec2_en, sec2_hi,
    "Which script was written from right to left under Aramaic influence in the northwestern edicts of Ashoka?",
    "अशोक के उत्तर-पश्चिमी शिलालेखों में अरामी प्रभाव के तहत कौन सी लिपि दाएं से बाएं लिखी गई थी?",
    "Kharoshthi script.",
    "खरोष्ठी लिपि।"
)

# 7. Assertion-Reason (8 Qs)
add_ar(sec2_en, sec2_hi,
    "Assertion (A): Mauryan punch-marked coins are dated based on stratigraphic layer association rather than inscriptions.\nReason (R): They do not contain any written legends, king names, or date markings.",
    "कथन (A): मौर्यकालीन आहत सिक्कों की तिथि उनके शिलालेखों के बजाय स्तरविन्यास परत संघ (stratigraphic layer association) के आधार पर तय की जाती है।\nकारण (R): उन पर राजाओं के नाम, कोई लिखित लेख या तिथि अंकित नहीं होती है।",
    0,
    "Both A and R are true, and R explains why stratigraphic dating is required for punch-marked coins.",
    "A और R दोनों सही हैं और R व्याख्या करता है कि आहत सिक्कों के लिए स्तरविन्यास तिथि निर्धारण की आवश्यकता क्यों होती है।"
)
add_ar(sec2_en, sec2_hi,
    "Assertion (A): Classical Sanskrit emerged as the primary epigraphical language of royal orders starting in the 3rd century BCE.\nReason (R): The earliest inscriptions, like the edicts of Ashoka, were written exclusively in Sanskrit.",
    "कथन (A): तीसरी शताब्दी ईसा पूर्व से शास्त्रीय संस्कृत शाही आदेशों की प्राथमिक पुरालेखीय भाषा के रूप में उभरी।\nकारण (R): अशोक के शिलालेखों जैसे सबसे प्रारंभिक शिलालेख विशेष रूप से संस्कृत में लिखे गए थे।",
    3,
    "A is false but R is false. Ashokan inscriptions were written in Prakrit (using Brahmi/Kharoshthi), not Sanskrit. Classical Sanskrit emerged later in inscriptions around 150 CE.",
    "A गलत है लेकिन R गलत है। अशोक के शिलालेख प्राकृत में लिखे गए थे, संस्कृत में नहीं। शास्त्रीय संस्कृत शिलालेखों में लगभग 150 ईस्वी के आसपास उभरी थी।"
)
add_ar(sec2_en, sec2_hi,
    "Assertion (A): Indo-Greek coinages are highly valued for reconstructing historical chronologies.\nReason (R): They introduced die-struck portraits of kings, helping researchers identify reigns and genealogical orders.",
    "कथन (A): ऐतिहासिक कालक्रम के पुनर्निर्माण के लिए हिंद-यूनानी सिक्कों को अत्यधिक मूल्यवान माना जाता है।\nकारण (R): उन्होंने राजाओं के चित्र वाले पासे से ढले (die-struck) सिक्कों की शुरुआत की, जिससे शोधकर्ताओं को शासनकाल और वंशावली के क्रम की पहचान करने में मदद मिली।",
    0,
    "Both A and R are true, and R explain how Indo-Greek coins assist in establishing chronology.",
    "A और R दोनों सही हैं और R व्याख्या करता है कि कैसे हिंद-यूनानी सिक्के कालक्रम स्थापित करने में सहायता करते हैं।"
)
add_ar(sec2_en, sec2_hi,
    "Assertion (A): Guptas issued coins with high artistic quality but varying gold purity.\nReason (R): Gold coins served as dynastic symbols and ritual currency rather than standard daily-life commercial exchange tokens.",
    "कथन (A): गुप्तों ने उच्च कलात्मक गुणवत्ता लेकिन भिन्न स्वर्ण शुद्धता वाले सिक्के जारी किए।\nकारण (R): सोने के सिक्कों ने दैनिक जीवन के वाणिज्यिक विनिमय के बजाय वंशवादी प्रतीकों और अनुष्ठानिक मुद्रा के रूप में कार्य किया।",
    1,
    "Both statements are true but R is not the direct cause of varying purity (which was linked to late Gupta economic decline and Roman trade shift).",
    "दोनों कथन सही हैं लेकिन R सोने की शुद्धता में बदलाव का प्रत्यक्ष कारण नहीं है (जो गुप्त काल के अंतिम समय की आर्थिक गिरावट से जुड़ा था)।"
)
add_ar(sec2_en, sec2_hi,
    "Assertion (A): The Kharoshthi script was deciphered through bilingual coins.\nReason (R): Indo-Greek coins bore names in both Greek and Kharoshthi characters, allowing scholars to translate the symbols.",
    "कथन (A): खरोष्ठी लिपि का अनुवाद द्विभाषी सिक्कों के माध्यम से किया गया था।\nकारण (R): हिंद-यूनानी सिक्कों पर यूनानी और खरोष्ठी दोनों लिपियों में नाम लिखे होते थे, जिससे विद्वानों को प्रतीकों का अनुवाद करने में मदद मिली।",
    0,
    "Both A and R are true, and R explains the exact mechanism of Kharoshthi's decipherment.",
    "A और R दोनों सही हैं और R खरोष्ठी लिपि के पढ़े जाने की सटीक प्रक्रिया की व्याख्या करता है।"
)
add_ar(sec2_en, sec2_hi,
    "Assertion (A): Numismatics is a secondary source for political history but primary for economic history.\nReason (R): Coins reveal metal purity, minting volumes, and trade networks directly reflecting fiscal state capacity.",
    "कथन (A): मुद्राशास्त्र राजनीतिक इतिहास के लिए एक द्वितीयक स्रोत है लेकिन आर्थिक इतिहास के लिए प्राथमिक है।\nकारण (R): सिक्के धातु की शुद्धता, ढलाई की मात्रा और व्यापार नेटवर्क को प्रकट करते हैं जो सीधे राज्य की राजकोषीय क्षमता को दर्शाते हैं।",
    0,
    "Both statements are true and R explains why coins represent primary sources for economic histories.",
    "दोनों कथन सही हैं और R व्याख्या करता है कि सिक्के क्यों आर्थिक इतिहास के लिए प्राथमिक स्रोत हैं।"
)
add_ar(sec2_en, sec2_hi,
    "Assertion (A): Inscriptions are considered more reliable than literary sources.\nReason (R): They are generally engraved on permanent materials, making them less prone to interpolation and copyist errors over centuries.",
    "कथन (A): शिलालेखों को साहित्यिक स्रोतों की तुलना में अधिक विश्वसनीय माना जाता है।\nकारण (R): वे आम तौर पर स्थायी सामग्रियों पर उकेरे जाते हैं, जिससे सदियों से होने वाले संशोधनों (interpolations) और प्रतिलिपिकारों की त्रुटियों की संभावना कम हो जाती है।",
    0,
    "Both A and R are true, and R is the correct explanation of A.",
    "A और R दोनों सही हैं और R, A की सही व्याख्या करता है।"
)
add_ar(sec2_en, sec2_hi,
    "Assertion (A): Mauryan state authority exercised monopolistic control over coin minting.\nReason (R): Inscriptions like Ashokan Edicts detail the punishments for individuals caught fabricating local punch-marked coins.",
    "कथन (A): मौर्य राज्य सत्ता ने सिक्कों की ढलाई पर एकाधिकार नियंत्रण का प्रयोग किया।\nकारण (R): अशोक के शिलालेखों में स्थानीय आहत सिक्कों का निर्माण करते हुए पकड़े गए लोगों के लिए दंड का विस्तृत विवरण है।",
    2,
    "A is true but R is false. While the Arthashastra lists metal regulations, Ashokan Edicts do not contain any references to coins, minting, or coin counterfeiting punishments.",
    "A सही है लेकिन R गलत है। यद्यपि अर्थशास्त्र में धातु नियमों की सूची है, लेकिन अशोक के शिलालेखों में सिक्कों, ढलाई या नकली सिक्के बनाने के दंड का कोई उल्लेख नहीं है।"
)

# 8. Statement-Based (5 Qs)
add_stmt(sec2_en, sec2_hi,
    "Consider the following statements regarding the decipherment of ancient Indian scripts:\n1. James Prinsep deciphered the Brahmi script in 1837.\n2. In Mauryan inscriptions, Brahmi script was written from right to left.\n3. The earliest bilingual coins that helped decipher Kharoshthi script were issued by Kushana rulers.\nWhich of the statements given above is/are correct?",
    "प्राचीन भारतीय लिपियों को पढ़े जाने के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. जेम्स प्रिंसेप ने 1837 में ब्राह्मी लिपि को पढ़ा था।\n2. मौर्यकालीन शिलालेखों में ब्राह्मी लिपि दाएं से बाएं लिखी जाती थी।\n3. खरोष्ठी लिपि को पढ़ने में मदद करने वाले सबसे पहले द्विभाषी सिक्के कुषाण शासकों द्वारा जारी किए गए थे।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"],
    ["केवल 1", "केवल 1 और 2", "केवल 2 और 3", "1, 2 और 3"],
    0,
    "Only statement 1 is correct. Brahmi was written left to right. Bilingual coins utilized for Kharoshthi decipherment were Indo-Greek, not Kushan.",
    "केवल कथन 1 सही है। ब्राह्मी बाएं से दाएं लिखी जाती थी। खरोष्ठी को पढ़ने के लिए प्रयुक्त द्विभाषी सिक्के हिंद-यूनानियों के थे, न कि कुषाणों के।"
)
add_stmt(sec2_en, sec2_hi,
    "Consider the following statements regarding ancient Indian coinages:\n1. Punch-marked coins lack any dates or names of kings.\n2. Indo-Greeks introduced bilingual gold coins depicting portraitures.\n3. Kushanas were the first dynasty in India to issue gold coins in large quantities.\nWhich of the statements given above are correct?",
    "प्राचीन भारतीय सिक्कों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. आहत सिक्कों पर राजाओं के नाम या कोई तिथि अंकित नहीं होती है।\n2. हिंद-यूनानियों ने चित्र दर्शाने वाले द्विभाषी सोने के सिक्के पेश किए।\n3. कुषाण भारत में बड़ी मात्रा में सोने के सिक्के जारी करने वाला पहला राजवंश था।\nऊपर दिए गए कथनों में से कौन से सही हैं?",
    ["1 and 3 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"],
    ["केवल 1 और 3", "केवल 1 और 2", "केवल 2 और 3", "1, 2 और 3"],
    3,
    "All three statements are correct. Kushanas standardized gold coinage in India following Indo-Greek styles.",
    "तीनों कथन सही हैं। कुषाणों ने हिंद-यूनानी शैली के बाद भारत में सोने के सिक्कों को मानकीकृत किया।"
)
add_stmt(sec2_en, sec2_hi,
    "With reference to Ashokan Edicts, which of the following statements are correct?\n1. Most edicts in the Gangetic plains are written in Prakrit and Brahmi script.\n2. Northwestern edicts near Kandahar are written in Greek and Aramaic.\n3. Kharoshthi script was used exclusively in his eastern Indian edicts.\nSelect the correct answer using the code given below:",
    "अशोक के शिलालेखों के संदर्भ में, निम्नलिखित में से कौन से कथन सही हैं?\n1. गंगा के मैदानों में अधिकांश शिलालेख प्राकृत भाषा और ब्राह्मी लिपि में लिखे गए हैं।\n2. कंधार के निकट उत्तर-पश्चिमी शिलालेख यूनानी और अरामी भाषा में लिखे गए हैं।\n3. खरोष्ठी लिपि का उपयोग विशेष रूप से उनके पूर्वी भारतीय शिलालेखों में किया गया था।\nनीचे दिए गए कोड का उपयोग करके सही उत्तर चुनें:",
    ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
    ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
    0,
    "Statements 1 and 2 are correct. Kharoshthi was used exclusively in northwestern edicts (like Shahbazgarhi and Mansehra), not eastern India.",
    "कथन 1 और 2 सही हैं। खरोष्ठी का उपयोग विशेष रूप से उत्तर-पश्चिमी शिलालेखों (जैसे शाहबाजगढ़ी और मनसेहरा) में किया गया था, न कि पूर्वी भारत में।"
)
add_stmt(sec2_en, sec2_hi,
    "Regarding epigraphical history, consider the following statements:\n1. The Sohgaura copper plate is the earliest deciphered copper plate in India.\n2. The Junagadh inscription of Rudradaman I represents the first long Sanskrit inscription.\n3. Allahabad Prasasti of Samudragupta was composed in Prakrit by Harishena.\nWhich of the statements given above is/are correct?",
    "पुरालेखीय इतिहास के संबंध में, निम्नलिखित कथनों पर विचार करें:\n1. सोहगौरा ताम्रपत्र भारत में सबसे पहला पढ़ा गया ताम्रपत्र है।\n2. रुद्रदामन प्रथम का जूनागढ़ शिलालेख पहला लंबा संस्कृत शिलालेख है।\n3. समुद्रगुप्त की इलाहाबाद प्रशस्ति की रचना हरिषेण द्वारा प्राकृत में की गई थी।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 and 2 only", "3 only", "2 and 3 only", "1, 2 and 3"],
    ["केवल 1 और 2", "केवल 3", "केवल 2 और 3", "1, 2 और 3"],
    0,
    "Statements 1 and 2 are correct. Allahabad Prasasti was composed in classical Sanskrit using Champu kavya style by Harishena, not Prakrit.",
    "कथन 1 और 2 सही हैं। इलाहाबाद प्रशस्ति की रचना हरिषेण द्वारा शास्त्रीय संस्कृत (चंपू काव्य शैली) में की गई थी, प्राकृत में नहीं।"
)
add_stmt(sec2_en, sec2_hi,
    "Consider the following statements regarding the study of coins (Numismatics):\n1. The presence of Roman gold coins in South India indicates a high trade surplus in favor of India.\n2. A decline in gold purity during late Gupta reigns is interpreted as a sign of economic crisis.\n3. The symbols on punch-marked coins have been fully deciphered as representing the names of Maurya ministers.\nWhich of the statements given above are correct?",
    "सिक्कों के अध्ययन (मुद्राशास्त्र) के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. दक्षिण भारत में रोमन सोने के सिक्कों की उपस्थिति भारत के पक्ष में एक उच्च व्यापार अधिशेष (trade surplus) को दर्शाती है।\n2. उत्तरवर्ती गुप्त शासकों के दौरान सोने की शुद्धता में गिरावट को आर्थिक संकट के संकेत के रूप में व्याख्यायित किया जाता है।\n3. आहत सिक्कों पर अंकित प्रतीकों को मौर्य मंत्रियों के नामों के प्रतिनिधित्व के रूप में पूरी तरह से पढ़ लिया गया है।\nऊपर दिए गए कथनों में से कौन से सही हैं?",
    ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
    ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
    0,
    "Statements 1 and 2 are correct. The symbols on punch-marked coins are not deciphered as minister names; they remain symbolic representations.",
    "कथन 1 और 2 सही हैं। आहत सिक्कों पर अंकित प्रतीकों को मंत्रियों के नामों के रूप में नहीं पढ़ा गया है; वे केवल प्रतीकात्मक प्रतिनिधित्व हैं।"
)

# 9. Why (3 Qs)
add_open(sec2_en, sec2_hi, "Why",
    "Why are inscriptions considered more reliable historical sources than literary texts?",
    "साहित्यिक ग्रंथों की तुलना में शिलालेखों को अधिक विश्वसनीय ऐतिहासिक स्रोत क्यों माना जाता है?",
    "Inscriptions are engraved on stone or metal, making them durable and highly resistant to changes over time. Unlike literary texts, which were manually copied over generations (introducing errors, additions, and interpolations), inscriptions remain original, unaltered documents of their specific period.",
    "शिलालेख पत्थर या धातु पर उकेरे जाते हैं, जिससे वे टिकाऊ होते हैं और समय के साथ होने वाले परिवर्तनों के प्रति अत्यधिक प्रतिरोधी होते हैं। साहित्यिक ग्रंथों के विपरीत, जिन्हें पीढ़ियों से हाथ से कॉपी किया गया था (जिससे त्रुटियां, नई बातें और संशोधन जुड़ गए), शिलालेख अपने विशिष्ट काल के मूल, अपरिवर्तित दस्तावेज बने रहते हैं।"
)
add_open(sec2_en, sec2_hi, "Why",
    "Why did the discovery of bilingual coins in Afghanistan and northwest India solve the mystery of the Kharoshthi script?",
    "अफगानिस्तान और उत्तर-पश्चिम भारत में द्विभाषी सिक्कों की खोज ने खरोष्ठी लिपि के रहस्य को कैसे सुलझाया?",
    "Scholars like James Prinsep could read the Greek legends on one side of Indo-Greek coins, which contained known royal names. By comparing these known Greek names with the unknown Kharoshthi characters on the reverse side, they matched sounds to symbols, unlocking the key to reading Kharoshthi.",
    "जेम्स प्रिंसेप जैसे विद्वान हिंद-यूनानी सिक्कों के एक तरफ यूनानी लेखों को पढ़ सकते थे, जिनमें ज्ञात राजाओं के नाम थे। इन ज्ञात यूनानी नामों की तुलना दूसरी तरफ के अज्ञात खरोष्ठी अक्षरों से करके, उन्होंने ध्वनियों का प्रतीकों से मिलान किया, जिससे खरोष्ठी को पढ़ने की कुंजी मिल गई।"
)
add_open(sec2_en, sec2_hi, "Why",
    "Why does a sudden change in coin metals or purity at a site indicate economic shifts?",
    "किसी स्थल पर सिक्कों की धातुओं या शुद्धता में अचानक बदलाव आर्थिक बदलाव को क्यों दर्शाता है?",
    "Coins reflect the fiscal strength of a state. A shift from pure gold to alloyed gold or copper, or a decrease in coin size and volume, shows that the treasury was facing deficits, trade networks were declining, or raw metal access was lost, reflecting economic distress.",
    "सिक्के किसी राज्य की राजकोषीय ताकत को दर्शाते हैं। शुद्ध सोने से मिश्रित सोने या तांबे में परिवर्तन, या सिक्के के आकार और मात्रा में कमी यह दर्शाती है कि खजाना घाटे का सामना कर रहा था, व्यापार नेटवर्क कम हो रहा था, या कच्ची धातु तक पहुंच समाप्त हो गई थी, जो आर्थिक संकट को दर्शाती है।"
)

# 10. How (3 Qs)
add_open(sec2_en, sec2_hi, "How",
    "How does the study of coins (Numismatics) help archaeologists map the territorial boundaries of ancient dynasties?",
    "सिक्कों का अध्ययन (मुद्राशास्त्र) पुरातत्वविदों को प्राचीन राजवंशों की क्षेत्रीय सीमाओं का मानचित्रण करने में कैसे मदद करता है?",
    "The spatial distribution of coin hoards indicates a dynasty's political control or trade domain. While a single stray coin could represent trade, finding multiple clusters and hoards of a specific dynasty's currency in a geographic region strongly suggests administrative control and taxation over that area.",
    "सिक्कों के ढेरों (hoards) का स्थानिक वितरण एक राजवंश के राजनीतिक नियंत्रण या व्यापार क्षेत्र को दर्शाता है। हालांकि एक अकेला भटका हुआ सिक्का व्यापार का प्रतिनिधित्व कर सकता है, लेकिन किसी भौगोलिक क्षेत्र में एक विशिष्ट राजवंश की मुद्रा के कई संकेंद्रण और ढेर मिलना उस क्षेत्र पर प्रशासनिक नियंत्रण और कराधान का दृढ़ संकेत देता है।"
)
add_open(sec2_en, sec2_hi, "How",
    "How did James Prinsep decipher the Brahmi script? Reconstruct the process.",
    "जेम्स प्रिंसेप ने ब्राह्मी लिपि को कैसे पढ़ा? इस प्रक्रिया का पुनर्निर्माण करें।",
    "Prinsep studied multiple rock and pillar edicts, matching recurring symbols at the end of statements. He realized that a common set of characters represented the word 'danam' (gift) and linked it to the donor. Using this linguistic key, he reconstructed the Brahmi alphabet step-by-step to read the complete Prakrit statements.",
    "प्रिंसेप ने कथनों के अंत में बार-बार आने वाले प्रतीकों का मिलान करते हुए कई शैल और स्तंभ शिलालेखों का अध्ययन किया। उन्होंने महसूस किया कि अक्षरों का एक सामान्य समूह 'दानम' (उपहार) शब्द का प्रतिनिधित्व करता है और इसे दाता से जोड़ा। इस भाषाई कुंजी का उपयोग करके, उन्होंने पूर्ण प्राकृत कथनों को पढ़ने के लिए चरण-दर-चरण ब्राह्मी वर्णमाला का पुनर्निर्माण किया।"
)
add_open(sec2_en, sec2_hi, "How",
    "How does the Sohgaura copper plate demonstrate early state administrative mechanisms?",
    "सोहगौरा ताम्रपत्र प्रारंभिक राज्य प्रशासनिक तंत्र को कैसे प्रदर्शित करता है?",
    "The Sohgaura plate lists royal orders detailing storehouses equipped with grain, fodder, and tools to be distributed during emergencies. This proves the existence of a structured famine-relief administrative policy and state grain storage infrastructure in the pre-Christian era.",
    "सोहगौरा पत्र में शाही आदेशों की सूची है जिसमें आपातकाल के दौरान वितरित किए जाने वाले अनाज, चारे और उपकरणों से सुसज्जित अन्नागारों का विवरण है। यह ईसा पूर्व युग में एक संरचित अकाल-राहत प्रशासनिक नीति और राजकीय अनाज भंडारण बुनियादी ढांचे के अस्तित्व को सिद्ध करता है।"
)

# 11. Case Study (3 Qs)
add_open(sec2_en, sec2_hi, "Case Study",
    "An excavation of a historic layer in South India uncovers hundreds of gold coins bearing the head of Roman Emperor Augustus, alongside a few local Satavahana copper coins. Reconstruct the trade dynamics of this site.",
    "दक्षिण भारत में एक ऐतिहासिक परत के उत्खनन से स्थानीय सातवाहन तांबे के सिक्कों के साथ-साथ रोमन सम्राट ऑगस्टस के सिर वाले सैकड़ों सोने के सिक्के मिलते हैं। इस स्थल की व्यापारिक गतिशीलता का पुनर्निर्माण करें।",
    "The presence of Roman gold coins indicates highly profitable maritime trade links with Rome. India exported luxury goods like pepper, silk, and spices and imported Roman gold and wine. The foreign coins were used as bullion for high-value transactions, while local copper coins served for daily domestic trade.",
    "रोमन सोने के सिक्कों की उपस्थिति रोम के साथ अत्यधिक लाभदायक समुद्री व्यापारिक संबंधों को दर्शाती है। भारत काली मिर्च, रेशम और मसालों जैसे विलासिता के सामानों का निर्यात करता था और रोमन सोना और शराब का आयात करता था। विदेशी सिक्कों का उपयोग उच्च मूल्य के लेन-देन के लिए बुलियन (सोने के रूप में) के रूप में किया जाता था, जबकि स्थानीय तांबे के सिक्के दैनिक घरेलू व्यापार के लिए काम आते थे।"
)
add_open(sec2_en, sec2_hi, "Case Study",
    "In a single field in Uttar Pradesh, a farmer uncovers a clay pot containing 500 gold coins. The coins of early layers are 98% pure gold; the coins of late layers are 70% pure gold. What socio-political process does this hoard record?",
    "उत्तर प्रदेश के एक खेत में, एक किसान को मिट्टी का घड़ा मिलता है जिसमें 500 सोने के सिक्के हैं। प्रारंभिक परतों के सिक्के 98% शुद्ध सोने के हैं; बाद की परतों के सिक्के 70% शुद्ध सोने के हैं। यह संचय (hoard) किस सामाजिक-राजनीतिक प्रक्रिया को दर्ज करता है?",
    "This hoard records a period of dynastic and economic decline (debasement of currency). The transition from high purity to alloyed gold shows a fiscal crisis, likely due to war, loss of trade routes, or treasury exhaustion, leading the state to mix gold with silver or copper to sustain coin volumes.",
    "यह संचय (hoard) वंशवादी और आर्थिक गिरावट (मुद्रा के अवमूल्यन) की अवधि को दर्ज करता है। उच्च शुद्धता से मिश्रित सोने में संक्रमण एक वित्तीय संकट को दर्शाता है, जो शायद युद्ध, व्यापारिक मार्गों की हानि, या खजाने के खाली होने के कारण था, जिसने राज्य को सिक्कों की मात्रा बनाए रखने के लिए सोने में चांदी या तांबे को मिलाने के लिए मजबूर किया।"
)
add_open(sec2_en, sec2_hi, "Case Study",
    "An inscription found on a temple wall details a land grant to a Brahmin community, listing the fields, tax exemptions, and punishments for violators. Analyze its historical value.",
    "एक मंदिर की दीवार पर मिले शिलालेख में ब्राह्मण समुदाय को भूमि अनुदान का विस्तृत विवरण दिया गया है, जिसमें खेतों, कर छूटों और उल्लंघनकर्ताओं के लिए दंड की सूची है। इसके ऐतिहासिक मूल्य का विश्लेषण करें।",
    "This inscription is a primary legal record of land tenure and feudal relations. It reveals the agricultural economy (fields), the state's fiscal structure (tax exemptions), the social hierarchy (patronage of Brahmins), and the judicial capacity of the rulers (punishments).",
    "यह शिलालेख भूमि कार्यकाल और सामंती संबंधों का एक प्राथमिक कानूनी रिकॉर्ड है। यह कृषि अर्थव्यवस्था (खेत), राज्य की राजकोषीय संरचना (कर छूट), सामाजिक पदानुक्रम (ब्राह्मणों को संरक्षण), और शासकों की न्यायिक क्षमता (दंड) को प्रकट करता है।"
)

# 12. Teach the Concept (3 Qs)
add_open(sec2_en, sec2_hi, "Teach the Concept",
    "Explain the difference between Epigraphy and Palaeography to a student. Use a simple visual comparison.",
    "एक छात्र को पुरालेखशास्त्र (Epigraphy) और पुरालिपिशास्त्र (Palaeography) के बीच का अंतर समझाएं। एक सरल दृश्य तुलना का उपयोग करें।",
    "Think of a historic signpost: **Epigraphy** is studying *what* is written on the signpost (the message, the historical events, the ruler's name). **Palaeography** is studying *how* it is written (the shape of the letters, the script style, the slant of the handwriting, and how it evolved over centuries).",
    "एक ऐतिहासिक संकेतक (signpost) के बारे में सोचें: **पुरालेखशास्त्र (Epigraphy)** यह अध्ययन करना है कि उस संकेतक पर *क्या* लिखा है (संदेश, ऐतिहासिक घटनाएं, शासक का नाम)। **पुरालिपिशास्त्र (Palaeography)** यह अध्ययन करना है कि वह *कैसे* लिखा गया है (अक्षरों का आकार, लिपि की शैली, लिखावट का झुकाव, और सदियों से इसका विकास कैसे हुआ)।"
)
add_open(sec2_en, sec2_hi, "Teach the Concept",
    "How do punch-marked coins differ from modern coins? Explain key manufacturing differences.",
    "आहत (punch-marked) सिक्के आधुनिक सिक्कों से किस प्रकार भिन्न हैं? मुख्य निर्माण अंतर समझाएं।",
    "1. **Legends**: Modern coins have printed words (denominations, dates). Punch-marked coins had no text, only symbols.\n2. **Shape**: Modern coins are perfectly round and uniform. Punch-marked coins were irregular sheets cut with shears.\n3. **Method**: Modern coins are struck in precise hydraulic press dies. Punch-marked coins had symbols hammered onto cold metal piece-by-piece using separate punches.",
    "1. **लेख (Legends)**: आधुनिक सिक्कों पर शब्द (मूल्यवर्ग, वर्ष) छपे होते हैं। आहत सिक्कों पर कोई पाठ नहीं होता था, केवल प्रतीक होते थे।\n2. **आकार**: आधुनिक सिक्के पूरी तरह से गोल और एक समान होते हैं। आहत सिक्के कैंची से काटे गए अनियमित धातु के टुकड़े होते थे।\n3. **विधि**: आधुनिक सिक्के सटीक प्रेस डाई में ढाले जाते हैं। आहत सिक्कों पर अलग-अलग पंचों का उपयोग करके धातु के टुकड़े पर एक-एक करके प्रतीकों को हथौड़े से अंकित किया जाता था।"
)
add_open(sec2_en, sec2_hi, "Teach the Concept",
    "Explain the historical significance of the Junagadh inscription of Rudradaman I.",
    "रुद्रदामन प्रथम के जूनागढ़ शिलालेख के ऐतिहासिक महत्व को समझाइए।",
    "The Junagadh inscription is significant because:\n1. **Language**: It is the first major long inscription written in classical, poetic Sanskrit, showing the rise of royal Sanskrit patronage.\n2. **Engineering**: It records the history of the Sudarshana Lake dam, built during Chandragupta Maurya's reign and repaired by Rudradaman without taxing his subjects, showcasing early water management and state welfare policies.",
    "जूनागढ़ शिलालेख महत्वपूर्ण है क्योंकि:\n1. **भाषा**: यह शास्त्रीय, काव्यात्मक संस्कृत में लिखा गया पहला प्रमुख लंबा शिलालेख है, जो शाही संस्कृत संरक्षण के उदय को दर्शाता है।\n2. **इंजीनियरिंग**: यह सुदर्शन झील के बांध का इतिहास दर्ज करता है, जिसे चंद्रगुप्त मौर्य के शासनकाल के दौरान बनाया गया था और रुद्रदामन द्वारा अपनी प्रजा पर कर लगाए बिना इसकी मरम्मत की गई थी, जो प्रारंभिक जल प्रबंधन और राज्य कल्याण नीतियों को प्रदर्शित करता है।"
)

# ==========================================
# SECTION 3: LITERARY SOURCES
# ==========================================

# 1. MCQ (5 Qs)
add_mcq(sec3_en, sec3_hi,
    "The oldest Indo-European literary text, which provides geographical details of the Sapta Sindhu (land of seven rivers) region, is:",
    "सबसे पुराना भारत-यूरोपीय साहित्यिक पाठ, जो सप्त सिंधु (सात नदियों की भूमि) क्षेत्र का भौगोलिक विवरण प्रदान करता है, कौन सा है?",
    ["Rigveda", "Atharvaveda", "Shatapatha Brahmana", "Sama Veda"],
    ["ऋग्वेद", "अथर्ववेद", "शतपथ ब्राह्मण", "सामवेद"],
    0,
    "The Rigveda (c. 1500-1200 BCE) is the oldest Veda and details the pastoral Vedic tribes living in the Sapta Sindhu region.",
    "ऋग्वेद (लगभग 1500-1200 ईसा पूर्व) सबसे पुराना वेद है और सप्त सिंधु क्षेत्र में रहने वाले पशुपालक वैदिक कबीलों का विवरण देता है।"
)
add_mcq(sec3_en, sec3_hi,
    "Which category of Vedic literature explains the ritualistic meaning and execution of sacrifices?",
    "वैदिक साहित्य की कौन सी श्रेणी यज्ञों के अनुष्ठानिक अर्थ और निष्पादन की व्याख्या करती है?",
    ["Upanishads", "Brahmanas", "Aranyakas", "Vedangas"],
    ["उपनिषद", "ब्राह्मण (Brahmanas)", "आरण्यक", "वेदांग"],
    1,
    "Brahmanas are prose texts appended to the Vedas that explain the ritualistic application, rules, and meaning of sacrifices.",
    "ब्राह्मण गद्य ग्रंथ हैं जो वेदों के साथ जुड़े हुए हैं और यज्ञों के अनुष्ठानिक अनुप्रयोग, नियमों और अर्थों की व्याख्या करते हैं।"
)
add_mcq(sec3_en, sec3_hi,
    "The philosophical treatises of ancient India that reflect late Vedic intellectual shifts and focus on Brahman/Atman are:",
    "प्राचीन भारत के दार्शनिक ग्रंथ जो उत्तर वैदिक बौद्धिक परिवर्तनों को दर्शाते हैं और ब्रह्म/आत्मन पर ध्यान केंद्रित करते हैं, कौन से हैं?",
    ["Puranas", "Upanishads", "Dharmasutras", "Vedangas"],
    ["पुराण", "उपनिषद (Upanishads)", "धर्मसूत्र", "वेदांग"],
    1,
    "The Upanishads (c. 800-500 BCE) are philosophical works focusing on the nature of reality, soul (Atman), and absolute truth (Brahman).",
    "उपनिषद (लगभग 800-500 ईसा पूर्व) दार्शनिक रचनाएँ हैं जो वास्तविकता की प्रकृति, आत्मा (आत्मन) और पूर्ण सत्य (ब्रह्म) पर ध्यान केंद्रित करती हैं।"
)
add_mcq(sec3_en, sec3_hi,
    "In which language was the Buddhist canonical literature (Tripitakas) written?",
    "बौद्ध विहित (canonical) साहित्य (त्रिपिटक) किस भाषा में लिखा गया था?",
    ["Sanskrit", "Pali", "Ardhamagadhi", "Tamil"],
    ["संस्कृत", "पालि (Pali)", "अर्धमागधी", "तमिल"],
    1,
    "The Tripitakas (Sutta, Vinaya, Abhidhamma) were compiled in the Pali language, reflecting the vernacular tongue of the masses in North India.",
    "त्रिपिटक (सुत्त, विनय, अभिधम्म) पालि भाषा में संकलित किए गए थे, जो उत्तर भारत में आम लोगों की लोकभाषा को दर्शाती थी।"
)
add_mcq(sec3_en, sec3_hi,
    "The Jain canonical texts (Angas) were primarily written and codified in which ancient language?",
    "जैन विहित ग्रंथों (अंग) को मुख्य रूप से किस प्राचीन भाषा में लिखा और संहिताबद्ध किया गया था?",
    ["Classical Sanskrit", "Pali", "Ardhamagadhi Prakrit", "Apabhramsha"],
    ["शास्त्रीय संस्कृत", "पालि", "अर्धमागधी प्राकृत (Ardhamagadhi Prakrit)", "अपभ्रंश"],
    2,
    "Jain canonical literature was composed in Ardhamagadhi Prakrit and codified at the Council of Valabhi in the 5th/6th century CE.",
    "जैन विहित साहित्य अर्धमागधी प्राकृत में रचा गया था और 5वीं/छठी शताब्दी ईस्वी में वलभी की परिषद में इसे संहिताबद्ध किया गया था।"
)

# 2. Multiple Correct MCQ (5 Qs)
add_multi_mcq(sec3_en, sec3_hi,
    "Which of the following texts belong to the Buddhist Pali Canon (Tripitakas)? (Select all that apply)",
    "निम्नलिखित में से कौन से ग्रंथ बौद्ध पालि विहित ग्रंथों (त्रिपिटक) के अंतर्गत आते हैं? (सभी लागू विकल्प चुनें)",
    ["Sutta Pitaka", "Vinaya Pitaka", "Abhidhamma Pitaka", "Kalpasutra"],
    ["सुत्त पिटक", "विनय पिटक", "अभिधम्म पिटक", "कल्पसूत्र"],
    [0, 1, 2],
    "Sutta, Vinaya, and Abhidhamma are the three baskets (Tripitakas) of Pali Buddhism. Kalpasutra is a Jain text composed by Bhadrabahu.",
    "सुत्त, विनय और अभिधम्म पालि बौद्ध धर्म की तीन टोकरियाँ (त्रिपिटक) हैं। कल्पसूत्र भद्रबाहु द्वारा रचित एक जैन ग्रंथ है।"
)
add_multi_mcq(sec3_en, sec3_hi,
    "Which of the following statements are correct regarding the Jataka stories? (Select all that apply)",
    "जातक कथाओं के संबंध में निम्नलिखित में से कौन से कथन सही हैं? (सभी लागू विकल्प चुनें)",
    ["Depict previous births of the Buddha", "Contain 547 folklore tales", "Written in Ardhamagadhi Prakrit", "Provide descriptions of guilds and trade routes"],
    ["बुद्ध के पूर्व जन्मों को दर्शाती हैं", "इसमें 547 लोककथाएँ शामिल हैं", "अर्धमागधी प्राकृत में लिखी गई हैं", "श्रेणियों (guilds) और व्यापारिक मार्गों का विवरण देती हैं"],
    [0, 1, 3],
    "Jatakas are written in Pali, depict prior births of the Buddha, consist of 547 tales, and offer valuable social, guild, and trade route data.",
    "जातक पालि में लिखे गए हैं, बुद्ध के पूर्व जन्मों को दर्शाते हैं, इनमें 547 कथाएँ हैं, और सामाजिक, श्रेणी तथा व्यापार मार्ग के मूल्यवान डेटा प्रदान करते हैं।"
)
add_multi_mcq(sec3_en, sec3_hi,
    "Which rivers are explicitly mentioned in the Rigvedic Nadistuti (river hymn)? (Select all that apply)",
    "ऋग्वैदिक नदीस्तुति (नदी भजन) में किन नदियों का स्पष्ट उल्लेख मिलता है? (सभी लागू विकल्प चुनें)",
    ["Sindhu (Indus)", "Sarasvati", "Ganga", "Narmada"],
    ["सिंधु (Sindhu)", "सरस्वती", "गंगा", "नर्मदा"],
    [0, 1, 2],
    "The Rigvedic Nadistuti lists rivers including Sindhu, Sarasvati, Ganga, and Yamuna. Narmada is not mentioned in the early Rigveda.",
    "ऋग्वैदिक नदीस्तुति में सिंधु, सरस्वती, गंगा और यमुना सहित नदियों की सूची है। प्रारंभिक ऋग्वेद में नर्मदा का उल्लेख नहीं है।"
)
add_multi_mcq(sec3_en, sec3_hi,
    "Which of the following are parts of the historical Puranas' five characteristics (Pancha Lakshana)? (Select all that apply)",
    "निम्नलिखित में से कौन से ऐतिहासिक पुराणों के पांच लक्षणों (पंच लक्षण) के अंग हैं? (सभी लागू विकल्प चुनें)",
    ["Sarga (Creation)", "Pratisarga (Recreation)", "Vamsha (Genealogies of gods/sages)", "Dharma (Legal statutes)"],
    ["सर्ग (सृष्टि)", "प्रतिसर्ग (पुनः सृष्टि)", "वंश (देवताओं/ऋषियों की वंशावली)", "धर्म (कानूनी नियम)"],
    [0, 1, 2],
    "The Pancha Lakshana of Puranas are: Sarga, Pratisarga, Vamsha, Manvantara, and Vamshanucharita. Dharma is not one of the five core literary classifications.",
    "पुराणों के पंच लक्षण हैं: सर्ग, प्रतिसर्ग, वंश, मन्वंतर और वंशानुचरित। धर्म इन पांच मूल साहित्यिक वर्गीकरणों में से नहीं है।"
)
add_multi_mcq(sec3_en, sec3_hi,
    "Which of the following texts contain detailed rules of conduct for Buddhist monks? (Select all that apply)",
    "निम्नलिखित में से किस ग्रंथ में बौद्ध भिक्षुओं के लिए आचरण के विस्तृत नियम शामिल हैं? (सभी लागू विकल्प चुनें)",
    ["Vinaya Pitaka", "Sutta Pitaka", "Pratimoksha", "Angas"],
    ["विनय पिटक", "सुत्त पिटक", "प्रतिमोक्ष", "अंग"],
    [0, 2],
    "The Vinaya Pitaka and its core section, the Pratimoksha, contain code of conduct rules for monks. Sutta Pitaka lists Buddha's sermons; Angas are Jain texts.",
    "विनय पिटक और इसके मूल भाग, प्रतिमोक्ष में भिक्षुओं के आचरण के नियम शामिल हैं। सुत्त पिटक में बुद्ध के उपदेश हैं; अंग जैन ग्रंथ हैं।"
)

# 3. True/False (8 Qs)
add_tf(sec3_en, sec3_hi,
    "The Rigveda is composed in classical Sanskrit, identical to the language used by Kalidasa.",
    "ऋग्वेद की रचना शास्त्रीय संस्कृत में की गई है, जो कालिदास द्वारा प्रयुक्त भाषा के समान है।",
    False,
    "The Rigveda is written in Vedic Sanskrit, which differs significantly in grammar and vocabulary from classical Sanskrit used by Kalidasa.",
    "ऋग्वेद की रचना वैदिक संस्कृत में की गई है, जो व्याकरण और शब्दावली में कालिदास द्वारा प्रयुक्त शास्त्रीय संस्कृत से काफी भिन्न है।"
)
add_tf(sec3_en, sec3_hi,
    "Later Vedic texts describe the expansion of settled agricultural communities eastward into the Ganga valley.",
    "उत्तर वैदिक ग्रंथ गंगा घाटी में पूर्व की ओर व्यवस्थित कृषि समुदायों के विस्तार का वर्णन करते हैं।",
    True,
    "Later Vedic works like the Shatapatha Brahmana detail the clearing of forests using fire and iron axes to settle the Ganga valley.",
    "शतपथ ब्राह्मण जैसे उत्तर वैदिक ग्रंथ गंगा घाटी में बसने के लिए आग और लोहे की कुल्हाड़ियों का उपयोग करके जंगलों को साफ करने का विवरण देते हैं।"
)
add_tf(sec3_en, sec3_hi,
    "The Upanishads reject ritualism and focus primarily on metaphysical theories of Atman and Karma.",
    "उपनिषद कर्मकांड को खारिज करते हैं और मुख्य रूप से आत्मन और कर्म के आध्यात्मिक सिद्धांतों पर ध्यान केंद्रित करते हैं।",
    True,
    "The Upanishads represent a major intellectual revolt against the ritual-heavy Brahmanical practices, shifting focus to spiritual self-knowledge.",
    "उपनिषद कर्मकांड प्रधान ब्राह्मणवादी प्रथाओं के खिलाफ एक बड़े बौद्धिक विद्रोह का प्रतिनिधित्व करते हैं, जिसमें ध्यान आध्यात्मिक आत्म-ज्ञान पर स्थानांतरित किया गया।"
)
add_tf(sec3_en, sec3_hi,
    "The Puranas contain valuable genealogical tables of ancient historical dynasties.",
    "पुराणों में प्राचीन ऐतिहासिक राजवंशों की मूल्यवान वंशावली तालिकाएँ मिलती हैं।",
    True,
    "The Puranas list dynasties of the historic period (Haryanka, Shishunaga, Nanda, Maurya, Shunga, Kanva, Satavahana, Gupta) in their Vamshanucharita sections.",
    "पुराण अपने वंशानुचरित खंडों में ऐतिहासिक काल के राजवंशों (हर्यक, शिशुनाग, नंद, मौर्य, शुंग, कण्व, सातवाहन, गुप्त) की सूची देते हैं।"
)
add_tf(sec3_en, sec3_hi,
    "Jataka stories contain valuable socio-economic information regarding craft guilds and ancient trade guilds.",
    "जातक कथाओं में शिल्प श्रेणियों (craft guilds) और प्राचीन व्यापार श्रेणियों के संबंध में मूल्यवान सामाजिक-आर्थिक जानकारी मिलती है।",
    True,
    "Jatakas frequently mention caravan merchants (sarthavaha), routes, and specific craft guilds (seni) operating in urban centers.",
    "जातक अक्सर शहरी केंद्रों में काम करने वाले कारवां व्यापारियों (सार्थवाह), मार्गों और विशिष्ट शिल्प श्रेणियों (श्रेणी) का उल्लेख करते हैं।"
)
add_tf(sec3_en, sec3_hi,
    "The Ramayana is older than the Rigveda and describes pre-metallic Paleolithic cultures.",
    "रामायण ऋग्वेद से भी पुरानी है और धातु-पूर्व पुरापाषाणकालीन संस्कृतियों का वर्णन करती है।",
    False,
    "The Ramayana is much younger than the Rigveda (core composed c. 500-300 BCE) and describes an advanced Iron Age urban society, not Paleolithic.",
    "रामायण ऋग्वेद से बहुत बाद की है (मूल रचना लगभग 500-300 ईसा पूर्व की) और यह एक उन्नत लौह युग के शहरी समाज का वर्णन करती है, न कि पुरापाषाण काल का।"
)
add_tf(sec3_en, sec3_hi,
    "Buddhist texts were written in Prakrit to ensure Brahmin scholars could read them easily.",
    "बौद्ध ग्रंथ प्राकृत में लिखे गए थे ताकि ब्राह्मण विद्वान उन्हें आसानी से पढ़ सकें।",
    False,
    "Buddhist texts were written in Pali (a vernacular tongue) to bypass Sanskrit and allow ordinary people, rather than just elite Brahmins, to understand them.",
    "बौद्ध ग्रंथ संस्कृत को दरकिनार करने और केवल कुलीन ब्राह्मणों के बजाय आम लोगों को उन्हें समझाने के लिए पालि (एक लोकभाषा) में लिखे गए थे।"
)
add_tf(sec3_en, sec3_hi,
    "The Shatapatha Brahmana describes the famous legend of Videgha Mathava carrying sacrificial fire east to the Sadaneera (Gandak) river.",
    "शतपथ ब्राह्मण में विदेघ माथव द्वारा यज्ञ की अग्नि को पूर्व में सदानीरा (गंडक) नदी तक ले जाने की प्रसिद्ध कथा का वर्णन है।",
    True,
    "This legend symbolizes the eastward expansion of Vedic Aryan culture and agriculture from the Sarasvati region into North Bihar.",
    "यह कथा सरस्वती क्षेत्र से उत्तरी बिहार में वैदिक आर्य संस्कृति और कृषि के पूर्व की ओर विस्तार का प्रतीक है।"
)

# 4. Fill in the Blank (8 Qs)
add_blank(sec3_en, sec3_hi,
    "The oldest of the four Vedas, containing hymns dedicated to natural deities, is the ________.",
    "चार वेदों में सबसे पुराना वेद, जिसमें प्राकृतिक देवताओं को समर्पित भजन हैं, ________ है।",
    "Rigveda", "ऋग्वेद",
    "The Rigveda has 1,028 hymns divided into 10 Mandalas.",
    "ऋग्वेद में 10 मंडलों में विभाजित 1,028 सूक्त हैं।"
)
add_blank(sec3_en, sec3_hi,
    "The prose texts appended to Vedas explaining the science and rules of sacrificial rituals are called ________.",
    "यज्ञ अनुष्ठानों के विज्ञान और नियमों की व्याख्या करने वाले वेदों से जुड़े गद्य ग्रंथ ________ कहलाते हैं।",
    "Brahmanas", "ब्राह्मण",
    "Each Veda has specific Brahmanas associated with it (e.g. Shatapatha Brahmana of Yajur Veda).",
    "प्रत्येक वेद से जुड़े विशिष्ट ब्राह्मण ग्रंथ हैं (जैसे यजुर्वेद का शतपथ ब्राह्मण)।"
)
add_blank(sec3_en, sec3_hi,
    "The philosophical ending sections of the Vedic corpus are called Upanishads or ________.",
    "वैदिक साहित्य के दार्शनिक अंतिम भागों को उपनिषद या ________ कहा जाता है।",
    "Vedanta", "वेदांत",
    "Vedanta literally means 'the end of the Vedas', indicating both position and ultimate knowledge.",
    "वेदांत का शाब्दिक अर्थ है 'वेदों का अंत', जो स्थिति और परम ज्ञान दोनों को दर्शाता है।"
)
add_blank(sec3_en, sec3_hi,
    "The 547 tales detailing prior lives of Gautama Buddha before his final enlightenment are the ________.",
    "अंतिम ज्ञान प्राप्ति से पहले गौतम बुद्ध के पिछले जन्मों का विवरण देने वाली 547 कहानियों का समूह ________ है।",
    "Jatakas", "जातक",
    "Jatakas form a key part of the Sutta Pitaka's Khuddaka Nikaya.",
    "जातक कथाएँ सुत्त पिटक के खुद्दक निकाय का एक महत्वपूर्ण हिस्सा हैं।"
)
add_blank(sec3_en, sec3_hi,
    "The Jain canonical texts compiled at the Valabhi Council are known as the twelve ________.",
    "वलभी परिषद में संकलित किए गए जैन विहित ग्रंथों को बारह ________ के रूप में जाना जाता है।",
    "Angas", "अंग",
    "The Jain canon is based on the 12 Angas, written in Prakrit.",
    "जैन विहित ग्रंथ प्राकृत में लिखे गए 12 अंगों पर आधारित हैं।"
)
add_blank(sec3_en, sec3_hi,
    "The famous Rigvedic geographical term 'Sapta Sindhu' refers to the Land of ________ Rivers.",
    "प्रसिद्ध ऋग्वैदिक भौगोलिक शब्द 'सप्त सिंधु' ________ नदियों की भूमि को संदर्भित करता है।",
    "Seven", "सात",
    "It refers to the Indus River and its five Punjab tributaries plus the Sarasvati River.",
    "यह सिंधु नदी और उसकी पंजाब की पांच सहायक नदियों तथा सरस्वती नदी को संदर्भित करता है।"
)
add_blank(sec3_en, sec3_hi,
    "The epic Mahabharata is historically attributed to the compilation by the sage ________.",
    "महाभारत महाकाव्य को ऐतिहासिक रूप से ऋषि ________ द्वारा संकलित माना जाता है।",
    "Vyasa", "व्यास",
    "Sage Krishna Dvaipayana Vyasa is credited with compiling the Mahabharata.",
    "ऋषि कृष्ण द्वैपायन व्यास को महाभारत के संकलन का श्रेय दिया जाता है।"
)
add_blank(sec3_en, sec3_hi,
    "The legendary river Sadaneera, mentioned in later Vedic texts as the eastern boundary of Aryan culture, is modern ________.",
    "उत्तर वैदिक ग्रंथों में आर्य संस्कृति की पूर्वी सीमा के रूप में उल्लिखित प्रसिद्ध नदी सदानीरा आधुनिक ________ नदी है।",
    "Gandak", "गंडक",
    "Sadaneera corresponds to the modern Gandak River flowing through Bihar.",
    "सदानीरा बिहार से बहने वाली आधुनिक गंडक नदी से मेल खाती है।"
)

# 5. Match the Following (3 Qs)
add_match(sec3_en, sec3_hi,
    "Match the Vedic texts with their literary category:",
    "वैदिक ग्रंथों को उनकी साहित्यिक श्रेणी के साथ सुमेलित करें:",
    [{"left": "Rigveda Samhita", "key": "hymns"}, {"left": "Shatapatha Brahmana", "key": "rituals"}, {"left": "Brihadaranyaka", "key": "philosophy"}],
    [{"left": "ऋग्वेद संहिता", "key": "hymns"}, {"left": "शतपथ ब्राह्मण", "key": "rituals"}, {"left": "बृहदारण्यक", "key": "philosophy"}],
    [{"val": "hymns", "text": "Hymns to natural deities"}, {"val": "rituals", "text": "Prose explanations of rituals"}, {"val": "philosophy", "text": "Upanishad/philosophical discourse"}],
    [{"val": "hymns", "text": "प्राकृतिक देवताओं के लिए भजन"}, {"val": "rituals", "text": "अनुष्ठानों की गद्य व्याख्या"}, {"val": "philosophy", "text": "उपनिषद/दार्शनिक प्रवचन"}],
    "Rigveda contains hymns; Shatapatha Brahmana details rituals; Brihadaranyaka is an Upanishad/philosophical discourse.",
    "ऋग्वेद में भजन हैं; शतपथ ब्राह्मण में अनुष्ठानों का विवरण है; बृहदारण्यक एक उपनिषद/दार्शनिक प्रवचन है।"
)
add_match(sec3_en, sec3_hi,
    "Match the heterodox texts with their religious tradition:",
    "नास्तिक (heterodox) ग्रंथों को उनकी धार्मिक परंपरा के साथ सुमेलित करें:",
    [{"left": "Vinaya Pitaka", "key": "buddhist"}, {"left": "Acharanga Sutra", "key": "jain"}, {"left": "Bhagavad Gita", "key": "hindu"}],
    [{"left": "विनय पिटक", "key": "buddhist"}, {"left": "आचारांग सूत्र", "key": "jain"}, {"left": "भगवद्गीता", "key": "hindu"}],
    [{"val": "buddhist", "text": "Buddhist Pali Canon"}, {"val": "jain", "text": "Jain Monastic Rules"}, {"val": "hindu", "text": "Brahmanical/Hindu Epic chapter"}],
    [{"val": "buddhist", "text": "बौद्ध पालि विहित ग्रंथ"}, {"val": "jain", "text": "जैन मठवासी नियम"}, {"val": "hindu", "text": "ब्राह्मणवादी/हिंदू महाकाव्य अध्याय"}],
    "Vinaya Pitaka is Buddhist; Acharanga Sutra is Jain; Bhagavad Gita is Hindu.",
    "विनय पिटक बौद्ध ग्रंथ है; आचारांग सूत्र जैन ग्रंथ है; भगवद्गीता हिंदू ग्रंथ है।"
)
add_match(sec3_en, sec3_hi,
    "Match the ancient terms with their historical meaning:",
    "प्राचीन शब्दों को उनके ऐतिहासिक अर्थ के साथ सुमेलित करें:",
    [{"left": "Sapta Sindhu", "key": "seven-rivers"}, {"left": "Seni", "key": "guild"}, {"left": "Sarthavaha", "key": "merchant"}],
    [{"left": "सप्त सिंधु", "key": "seven-rivers"}, {"left": "श्रेणी (Seni)", "key": "guild"}, {"left": "सार्थवाह", "key": "merchant"}],
    [{"val": "seven-rivers", "text": "Land of seven rivers"}, {"val": "guild", "text": "Craft guild"}, {"val": "merchant", "text": "Caravan merchant leader"}],
    [{"val": "seven-rivers", "text": "सात नदियों की भूमि"}, {"val": "guild", "text": "शिल्प संघ (श्रेणी)"}, {"val": "merchant", "text": "कारवां व्यापारी नेता"}],
    "Sapta Sindhu is the seven rivers region, seni is a craft guild, and sarthavaha is a caravan merchant leader.",
    "सप्त सिंधु सात नदियों का क्षेत्र है, श्रेणी शिल्प संघ है, और सार्थवाह कारवां व्यापारी नेता है।"
)

# 6. One-Liner (8 Qs)
add_oneliner(sec3_en, sec3_hi,
    "Which is the oldest of the four Vedas?",
    "चारों वेदों में सबसे पुराना वेद कौन सा है?",
    "Rigveda.",
    "ऋग्वेद।"
)
add_oneliner(sec3_en, sec3_hi,
    "What language was primarily used to compose early Buddhist literature?",
    "प्रारंभिक बौद्ध साहित्य की रचना के लिए मुख्य रूप से किस भाषा का उपयोग किया गया था?",
    "Pali language.",
    "पालि भाषा।"
)
add_oneliner(sec3_en, sec3_hi,
    "Which text describes the legendary Aryan expansion eastward to the Sadaneera River?",
    "कौन सा ग्रंथ सदाबहार गंडक नदी (सदानीरा) के पूर्व की ओर पौराणिक आर्यों के विस्तार का वर्णन करता है?",
    "Shatapatha Brahmana.",
    "शतपथ ब्राह्मण।"
)
add_oneliner(sec3_en, sec3_hi,
    "What is the literal meaning of the word 'Upanishad'?",
    "शब्द 'उपनिषद' का शाब्दिक अर्थ क्या है?",
    "To sit down near (a teacher to receive secret instruction).",
    "समीप बैठना (रहस्यमयी उपदेश प्राप्त करने के लिए गुरु के पास बैठना)।"
)
add_oneliner(sec3_en, sec3_hi,
    "Name the division of the Buddhist Pali canon that contains the moral discourses and sermons of Buddha.",
    "बौद्ध पालि विहित ग्रंथ के उस भाग का नाम बताइए जिसमें बुद्ध के नैतिक प्रवचन और उपदेश शामिल हैं।",
    "Sutta Pitaka.",
    "सुत्त पिटक।"
)
add_oneliner(sec3_en, sec3_hi,
    "In which ancient language were early Jain texts like the Angas written?",
    "प्रारंभिक जैन ग्रंथ जैसे अंग किस प्राचीन भाषा में लिखे गए थे?",
    "Ardhamagadhi Prakrit.",
    "अर्धमागधी प्राकृत।"
)
add_oneliner(sec3_en, sec3_hi,
    "Which Sanskrit term refers to the five core characteristics of Puranas?",
    "कौन सा संस्कृत शब्द पुराणों की पांच मूल विशेषताओं को संदर्भित करता है?",
    "Pancha Lakshana.",
    "पंच लक्षण।"
)
add_oneliner(sec3_en, sec3_hi,
    "Explain the historical utility of the Jataka tales.",
    "जातक कथाओं की ऐतिहासिक उपयोगिता स्पष्ट करें।",
    "They provide descriptions of social life, guilds, crafts, and trade routes of early historic India (c. 6th-5th century BCE).",
    "वे प्रारंभिक ऐतिहासिक भारत (लगभग छठी-पांचवीं शताब्दी ईसा पूर्व) के सामाजिक जीवन, श्रेणियों, शिल्पों और व्यापारिक मार्गों का विवरण प्रदान करते हैं।"
)

# 7. Assertion-Reason (8 Qs)
add_ar(sec3_en, sec3_hi,
    "Assertion (A): Rigvedic society was primarily pastoral and nomadic.\nReason (R): The text contains numerous hymns honoring cows and horses, and lacks description of major brick cities or canal networks.",
    "कथन (A): ऋग्वैदिक समाज मुख्य रूप से पशुपालक और खानाबदोश था।\nकारण (R): इस ग्रंथ में गायों और घोड़ों के सम्मान में कई भजन शामिल हैं और इसमें बड़े ईंटों के शहरों या नहर नेटवर्क का कोई विवरण नहीं मिलता है।",
    0,
    "Both A and R are true, and R correctly explains the pastoral/nomadic nature of Rigvedic society based on text markers.",
    "A और R दोनों सही हैं और R ऋग्वैदिक समाज की पशुपालक/खानाबदोश प्रकृति की सही व्याख्या करता है।"
)
add_ar(sec3_en, sec3_hi,
    "Assertion (A): Later Vedic texts represent a shift toward settled agriculture in the Gangetic basin.\nReason (R): Iron tools (krishna-ayas) are mentioned in later Vedic works, facilitating the clearing of heavy soils.",
    "कथन (A): उत्तर वैदिक ग्रंथ गंगा बेसिन में व्यवस्थित कृषि की ओर संक्रमण का प्रतिनिधित्व करते हैं।\nकारण (R): उत्तर वैदिक रचनाओं में लोहे के उपकरणों (कृष्ण-अयस) का उल्लेख है, जिसने भारी मिट्टी को साफ करने में मदद की।",
    0,
    "Both statements are true and R explains how iron enabled Gangetic agriculture and settled life.",
    "दोनों कथन सही हैं और R व्याख्या करता है कि कैसे लोहे ने गंगा बेसिन में कृषि और व्यवस्थित जीवन को संभव बनाया।"
)
add_ar(sec3_en, sec3_hi,
    "Assertion (A): Upanishads represent the zenith of ritual-sacrifice descriptions.\nReason (R): Upanishadic thinkers sought to establish the absolute authority of Vedic sacrificial priests.",
    "कथन (A): उपनिषद यज्ञ-अनुष्ठान के विवरणों के चरम का प्रतिनिधित्व करते हैं।\nकारण (R): उपनिषद विचारकों ने वैदिक बलि पुरोहितों के पूर्ण अधिकार को स्थापित करने की कोशिश की थी।",
    3,
    "A is false and R is false. Upanishads criticized ritualism, shifting the focus to internal philosophy (Atman/Brahman) and self-realization.",
    "A गलत है और R गलत है। उपनिषदों ने कर्मकांड की आलोचना की, ध्यान को आंतरिक दर्शन (आत्मन/ब्रह्म) और आत्म-साक्षात्कार पर केंद्रित किया।"
)
add_ar(sec3_en, sec3_hi,
    "Assertion (A): Pali was chosen as the medium of early Buddhist texts.\nReason (R): Buddha rejected elite Sanskrit and wanted his teachings accessible to the common masses in their local dialect.",
    "कथन (A): प्रारंभिक बौद्ध ग्रंथों के माध्यम के रूप में पालि को चुना गया था।\nकारण (R): बुद्ध ने कुलीन वर्ग की संस्कृत को खारिज कर दिया और चाहते थे कि उनकी शिक्षाएं स्थानीय बोली में आम जनता के लिए सुलभ हों।",
    0,
    "Both A and R are true, and R explains why Pali was used.",
    "A और R दोनों सही हैं और R व्याख्या करता है कि पालि का उपयोग क्यों किया गया था।"
)
add_ar(sec3_en, sec3_hi,
    "Assertion (A): Puranic genealogies (Vamshanucharita) are ignored by modern historians.\nReason (R): Puranic records contain dynastic lines mixed with mythological timelines, making them completely unreliable.",
    "कथन (A): आधुनिक इतिहासकार पौराणिक वंशावलियों (वंशानुचरित) की अनदेखी करते हैं।\nकारण (R): पौराणिक रिकॉर्ड में पौराणिक समयसीमाओं के साथ मिश्रित राजवंशों के नाम शामिल हैं, जिससे वे पूरी तरह से अविश्वसनीय हो जाते हैं।",
    3,
    "A is false but R is true. While Puranas mix mythology, modern historians do NOT ignore them; they are carefully cross-referenced with inscriptions to reconstruct Maurya, Satavahana, and Gupta chronologies.",
    "A गलत है लेकिन R सही है। हालांकि पुराणों में पौराणिक कथाओं का मिश्रण है, लेकिन आधुनिक इतिहासकार उनकी अनदेखी नहीं करते हैं; मौर्य, सातवाहन और गुप्त कालक्रम के पुनर्निर्माण के लिए शिलालेखों के साथ उनका सावधानीपूर्वक मिलान किया जाता है।"
)
add_ar(sec3_en, sec3_hi,
    "Assertion (A): Jataka stories are excellent sources for reconstruction of Iron Age trade networks.\nReason (R): They contain descriptions of merchants traveling to Suvarnabhumi (Southeast Asia) and utilizing specialized guilds.",
    "कथन (A): लौह युग के व्यापारिक नेटवर्क के पुनर्निर्माण के लिए जातक कथाएँ उत्कृष्ट स्रोत हैं।\nकारण (R): इनमें सुवर्णभूमि (दक्षिण-पूर्व एशिया) की यात्रा करने वाले व्यापारियों और विशिष्ट श्रेणियों (guilds) के उपयोग का विवरण है।",
    0,
    "Both statements are true and R provides the reasoning for Jatakas' value in trade studies.",
    "दोनों कथन सही हैं और R व्यापारिक अध्ययनों में जातक कथाओं के महत्व का कारण बताता है।"
)
add_ar(sec3_en, sec3_hi,
    "Assertion (A): Jain canonical literature (Angas) was codified during the Valabhi council.\nReason (R): The text was written in Ardhamagadhi Prakrit to prevent common masses from accessing monastic secrets.",
    "कथन (A): जैन विहित साहित्य (अंग) को वलभी परिषद के दौरान संहिताबद्ध किया गया था।\nकारण (R): इस ग्रंथ को आम जनता को मठवासी रहस्यों तक पहुँचने से रोकने के लिए अर्धमागधी प्राकृत में लिखा गया था।",
    2,
    "A is true but R is false. Prakrit was chosen specifically because it was a vernacular language of the common people, not to hide secrets.",
    "A सही है लेकिन R गलत है। प्राकृत को विशेष रूप से इसलिए चुना गया था क्योंकि यह आम लोगों की लोकभाषा थी, रहस्यों को छिपाने के लिए नहीं।"
)
add_ar(sec3_en, sec3_hi,
    "Assertion (A): Epics like Ramayana and Mahabharata are used carefully as historical records.\nReason (R): They underwent multiple revisions and expansions over centuries, introducing younger Iron Age features into older narratives.",
    "कथन (A): रामायण और महाभारत जैसे महाकाव्यों का उपयोग ऐतिहासिक रिकॉर्ड के रूप में सावधानीपूर्वक किया जाता है।\nकारण (R): सदियों से उनके कई संस्करण और विस्तार हुए हैं, जिससे पुरानी कहानियों में बाद के लौह युग के तत्व शामिल हो गए हैं।",
    0,
    "Both A and R are true, and R explains why historians exercise caution when using epics for dating.",
    "A और R दोनों सही हैं और R व्याख्या करता है कि इतिहासकार महाकाव्यों का उपयोग करते समय सावधानी क्यों बरतते हैं।"
)

# 8. Statement-Based (5 Qs)
add_stmt(sec3_en, sec3_hi,
    "Consider the following statements regarding Rigvedic literature:\n1. It contains 1,028 hymns organized into 10 Mandalas.\n2. The Nadistuti hymn honors the Indus (Sindhu) river as the most prominent river.\n3. The tenth Mandala contains the Purusha Sukta, which introduces the four Varnas.\nWhich of the statements given above are correct?",
    "ऋग्वैदिक साहित्य के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. इसमें 10 मंडलों में संगठित 1,028 सूक्त शामिल हैं।\n2. नदीस्तुति सूक्त सिंधु नदी को सबसे प्रमुख नदी के रूप में सम्मानित करता है।\n3. दसवें मंडल में पुरुष सूक्त शामिल है, जो चार वर्णों की शुरुआत करता है।\nऊपर दिए गए कथनों में से कौन से सही हैं?",
    ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
    ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
    3,
    "All three statements are correct and define key historical data extracted from the Rigvedic Samhita.",
    "तीनों कथन सही हैं और ऋग्वेद संहिता से निकाले गए प्रमुख ऐतिहासिक डेटा को परिभाषित करते हैं।"
)
add_stmt(sec3_en, sec3_hi,
    "Consider the following statements regarding the Buddhist canon:\n1. The Vinaya Pitaka deals with rules of discipline for monks.\n2. The Sutta Pitaka contains the philosophical analysis of Buddhist psychology.\n3. The Abhidhamma Pitaka contains the moral sermons of the Buddha.\nWhich of the statements given above is/are correct?",
    "बौद्ध विहित ग्रंथों (canon) के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. विनय पिटक में भिक्षुओं के लिए अनुशासन के नियमों का वर्णन है।\n2. सुत्त पिटक में बौद्ध मनोविज्ञान का दार्शनिक विश्लेषण है।\n3. अभिधम्म पिटक में बुद्ध के नैतिक उपदेश शामिल हैं।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"],
    ["केवल 1", "केवल 1 और 2", "केवल 2 और 3", "1, 2 और 3"],
    0,
    "Only statement 1 is correct. Sutta Pitaka contains sermons; Abhidhamma Pitaka contains the philosophical and psychological analysis.",
    "केवल कथन 1 सही है। सुत्त पिटक में उपदेश हैं; अभिधम्म पिटक में दार्शनिक और मनोवैज्ञानिक विश्लेषण है।"
)
add_stmt(sec3_en, sec3_hi,
    "With reference to Jain canonical literature, which of the following statements are correct?\n1. It was codified at the Valabhi Council in Gujarat.\n2. The texts are written in Sanskrit, the language of royal courts.\n3. The Acharanga Sutra details the rules of conduct for Jain monks.\nWhich of the statements given above are correct?",
    "जैन विहित साहित्य के संदर्भ में, निम्नलिखित में से कौन से कथन सही हैं?\n1. इसे गुजरात में वलभी परिषद में संहितबद्ध किया गया था।\n2. ये ग्रंथ संस्कृत में लिखे गए हैं, जो शाही दरबारों की भाषा थी।\n3. आचारांग सूत्र में जैन भिक्षुओं के आचरण के नियमों का विवरण है।\nऊपर दिए गए कथनों में से कौन से सही हैं?",
    ["1 and 3 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"],
    ["केवल 1 और 3", "केवल 1 और 2", "केवल 2 और 3", "1, 2 और 3"],
    0,
    "Statements 1 and 3 are correct. Jain canon was composed in Prakrit, not Sanskrit.",
    "कथन 1 और 3 सही हैं। जैन विहित ग्रंथ प्राकृत में लिखे गए थे, संस्कृत में नहीं।"
)
add_stmt(sec3_en, sec3_hi,
    "Regarding later Vedic geography, consider the following statements:\n1. Shatapatha Brahmana describes the myth of Videgha Mathava clearing forests with fire.\n2. Later Vedic literature indicates the center of Aryan culture shifted from Indus to Ganga-Yamuna Doab.\n3. The river Sarasvati is praised as the ultimate boundary in later Vedic texts.\nWhich of the statements given above are correct?",
    "उत्तर वैदिक भूगोल के संबंध में, निम्नलिखित कथनों पर विचार करें:\n1. शतपथ ब्राह्मण में विदेघ माथव द्वारा आग से जंगलों को साफ करने के मिथक का वर्णन है।\n2. उत्तर वैदिक साहित्य इंगित करता है कि आर्य संस्कृति का केंद्र सिंधु से गंगा-यमुना दोआब में स्थानांतरित हो गया था।\n3. उत्तर वैदिक ग्रंथों में सरस्वती नदी को अंतिम सीमा के रूप में सराहा गया है।\nऊपर दिए गए कथनों में से कौन से सही हैं?",
    ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
    ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
    0,
    "Statements 1 and 2 are correct. In later Vedic times, Sarasvati was drying up and Ganga-Yamuna became the core area, with Sadaneera (Gandak) as the eastern limit.",
    "कथन 1 और 2 सही हैं। उत्तर वैदिक काल में, सरस्वती सूख रही थी और गंगा-यमुना मुख्य क्षेत्र बन गई थी, जिसकी पूर्वी सीमा सदानीरा (गंडक) थी।"
)
add_stmt(sec3_en, sec3_hi,
    "Consider the following statements regarding the Puranas as historical sources:\n1. The genealogies of kings are preserved in the Vamshanucharita section.\n2. Puranas list historical dynasties like Nandas and Mauryas in future tense format.\n3. The Vishnu Purana provides crucial information regarding the Satavahana dynasty.\nWhich of the statements given above is/are correct?",
    "ऐतिहासिक स्रोतों के रूप में पुराणों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. राजाओं की वंशावलियाँ वंशानुचरित खंड में सुरक्षित हैं।\n2. पुराण नंद और मौर्य जैसे ऐतिहासिक राजवंशों को भविष्य काल (future tense) के प्रारूप में सूचीबद्ध करते हैं।\n3. विष्णु पुराण सातवाहन राजवंश के बारे में महत्वपूर्ण जानकारी प्रदान करता है।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 and 2 only", "3 only", "2 and 3 only", "1, 2 and 3"],
    ["केवल 1 और 2", "केवल 3", "केवल 2 और 3", "1, 2 और 3"],
    0,
    "Statements 1 and 2 are correct. Vishnu Purana details Mauryan dynasty; Matsya Purana details Satavahanas.",
    "कथन 1 and 2 सही हैं। विष्णु पुराण में मौर्य राजवंश का विवरण है; मत्स्य पुराण में सातवाहनों का विवरण है।"
)

# 9. Why (3 Qs)
add_open(sec3_en, sec3_hi, "Why",
    "Why does later Vedic literature show a major transition in agricultural techniques compared to early Rigvedic hymns?",
    "प्रारंभिक ऋग्वैदिक भजनों की तुलना में उत्तर वैदिक साहित्य कृषि तकनीकों में बड़ा बदलाव क्यों दिखाता है?",
    "Rigvedic society was pastoralist, utilizing light wooden plows (langala). In the later Vedic period, Aryans expanded into the Gangetic valley where they encountered hard alluvial clay. They adapted by utilizing heavy iron-shod plows and iron axes (krishna-ayas) to clear dense monsoon forests, shifting to intensive rice cultivation.",
    "ऋग्वैदिक समाज पशुपालक था, जो हल्के लकड़ी के हलों (लांगला) का उपयोग करता था। उत्तर वैदिक काल में, आर्य गंगा घाटी में फैल गए जहाँ उनका सामना कठोर जलोढ़ मिट्टी से हुआ। उन्होंने भारी लोहे के हलों और लोहे की कुल्हाड़ियों (कृष्ण-अयस) का उपयोग करके घने मानसूनी जंगलों को साफ किया, जिससे धान की सघन खेती शुरू हुई।"
)
add_open(sec3_en, sec3_hi, "Why",
    "Why are Upanishads considered a philosophical reaction against Brahmanas?",
    "उपनिषदों को ब्राह्मण ग्रंथों के खिलाफ एक दार्शनिक प्रतिक्रिया क्यों माना जाता है?",
    "Brahmanas focused heavily on the mechanics, costs, and execution of animal sacrifices and priest-led rituals. Upanishads represented a spiritual reaction, declaring rituals to be 'frail boats' and shifting focus to philosophical questions of self-realization, absolute truth (Brahman), and the inner soul (Atman).",
    "ब्राह्मण ग्रंथों में पशु बलि और पुजारियों के नेतृत्व में होने वाले अनुष्ठानों की प्रक्रिया, लागत और निष्पादन पर बहुत अधिक ध्यान केंद्रित किया गया था। उपनिषद इसके खिलाफ आध्यात्मिक प्रतिक्रिया थे, जिन्होंने अनुष्ठानों को 'कमजोर नावें' घोषित किया और ध्यान को आत्म-साक्षात्कार, परम सत्य (ब्रह्म) और आंतरिक आत्मा (आत्मन) के दार्शनिक प्रश्नों पर केंद्रित किया।"
)
add_open(sec3_en, sec3_hi, "Why",
    "Why do Buddhist Jataka stories represent reliable sources for early historic trade geography?",
    "बौद्ध जातक कथाएँ प्रारंभिक ऐतिहासिक व्यापार भूगोल के लिए विश्वसनीय स्रोत क्यों मानी जाती हैं?",
    "Although Jatakas are moral fables, they reflect the contemporary world of the compilers. They describe caravan traders (sarthavaha) traveling along specific highways (Uttarapatha and Dakshinapatha), naming rivers, ports, and cities, providing historians with realistic geographic maps of trade networks.",
    "हालांकि जातक नैतिक लोककथाएँ हैं, लेकिन वे संकलनकर्ताओं के समकालीन विश्व को दर्शाती हैं। वे विशिष्ट राजमार्गों (उत्तरापथ और दक्षिणापथ) पर यात्रा करने वाले कारवां व्यापारियों (सार्थवाह) का वर्णन करती हैं, जिसमें नदियों, बंदरगाहों और शहरों के नाम हैं, जिससे इतिहासकारों को व्यापार नेटवर्क के यथार्थवादी भौगोलिक मानचित्र मिलते हैं।"
)

# 10. How (3 Qs)
add_open(sec3_en, sec3_hi, "How",
    "How does the myth of Videgha Mathava in Shatapatha Brahmana explain historical geography?",
    "शतपथ ब्राह्मण में विदेघ माथव का मिथक ऐतिहासिक भूगोल को कैसे समझाता है?",
    "The myth describes Videgha Mathava carrying Agni (sacrificial fire) eastward from the Sarasvati, burning forests along the way, until reaching the Sadaneera River (modern Gandak). This explains the historical process of Aryan migration, clearing Gangetic forests using fire, and establishing agriculture in Bihar.",
    "यह मिथक विदेघ माथव द्वारा सरस्वती नदी से पूर्व की ओर अग्नि (यज्ञीय अग्नि) ले जाने का वर्णन करता है, जिसने रास्ते में जंगलों को जलाया, जब तक कि वे सदानीरा नदी (आधुनिक गंडक) तक नहीं पहुँच गए। यह आर्यों के प्रवास, आग का उपयोग करके गंगा के जंगलों को साफ करने और बिहार में कृषि स्थापित करने की ऐतिहासिक प्रक्रिया को समझाता है।"
)
add_open(sec3_en, sec3_hi, "How",
    "How did the compilation of Jain Angas at Valabhi shape early medieval Western Indian history?",
    "वलभी में जैन अंगों के संकलन ने प्रारंभिक मध्यकालीन पश्चिमी भारतीय इतिहास को कैसे आकार दिया?",
    "By compiling and writing down oral traditions at Valabhi (Gujarat, c. 5th-6th cent. CE), Jain scholars preserved rules, geography, and genealogies. This codified canon stimulated Jain temple networks, mercantile writing, and Prakrit literature in Western India, linking merchant wealth to Jain institutions.",
    "वलभी (गुजरात, लगभग 5वीं-छठी शताब्दी ईस्वी) में मौखिक परंपराओं को संकलित और लिखकर, जैन विद्वानों ने नियमों, भूगोल और वंशावलियों को सुरक्षित रखा। इस संहिताबद्ध धर्मग्रंथ ने पश्चिमी भारत में जैन मंदिर नेटवर्क, व्यापारिक लेखन और प्राकृत साहित्य को बढ़ावा दिया, जिससे व्यापारियों के धन को जैन संस्थानों से जोड़ा गया।"
)
add_open(sec3_en, sec3_hi, "How",
    "How do Puranas help reconstruct dynastic chronologies when epigraphic evidence is missing?",
    "पुरालेखीय साक्ष्य गायब होने पर पुराण राजवंशों के कालक्रम के पुनर्निर्माण में कैसे मदद करते हैं?",
    "Puranas record dynastic lists, listing the number of kings in a dynasty and their total reign years (e.g. Satavahanas or Mauryas). Historians cross-reference these lists with sporadic coins and foreign accounts to build structural timelines for periods lacking extensive royal inscriptions.",
    "पुराण राजवंशों की सूचियाँ दर्ज करते हैं, जिनमें एक राजवंश में राजाओं की संख्या और उनके कुल शासनकाल के वर्ष (जैसे सातवाहन या मौर्य) सूचीबद्ध होते हैं। इतिहासकार इन सूचियों का मिलान छिटपुट सिक्कों और विदेशी विवरणों से करते हैं ताकि उन अवधियों के लिए कालक्रम बनाया जा सके जहाँ बड़े शाही शिलालेख नहीं मिलते हैं।"
)

# 11. Case Study (3 Qs)
add_open(sec3_en, sec3_hi, "Case Study",
    "A researcher attempts to date a text describing a rich capital city with brick gates, stone towers, and gold coins. The text is claimed to be Rigvedic. Analyze this claim.",
    "एक शोधकर्ता ईंटों के दरवाजों, पत्थर के टावरों और सोने के सिक्कों वाले एक समृद्ध राजधानी शहर का वर्णन करने वाले पाठ की तिथि निर्धारित करने का प्रयास करता है। दावा किया जाता है कि यह पाठ ऋग्वैदिक है। इस दावे का विश्लेषण करें।",
    "The claim is historically invalid. Rigvedic society (c. 1500–1200 BCE) was a pastoral, non-urban culture that did not construct brick cities or stone fortifications. Gold currency (coins) did not exist in India until the Indo-Greek/Kushan period. The text must belong to a late historical period (c. 4th century BCE or later).",
    "यह दावा ऐतिहासिक रूप से अमान्य है। ऋग्वैदिक समाज (लगभग 1500-1200 ईसा पूर्व) एक पशुपालक, गैर-शहरी संस्कृति थी जिसने ईंटों के शहर या पत्थर के किले नहीं बनाए थे। भारत में इंडो-ग्रीक/कुषाण काल से पहले सोने की मुद्रा (सिक्के) का अस्तित्व नहीं था। यह पाठ निश्चित रूप से बाद के ऐतिहासिक काल (लगभग चौथी शताब्दी ईसा पूर्व या उसके बाद) का होना चाहिए।"
)
add_open(sec3_en, sec3_hi, "Case Study",
    "An economist studies ancient Indian interest rates and guild rules. Which literary sources (Buddhist, Jain, Brahmanical) should they select, and why?",
    "एक अर्थशास्त्री प्राचीन भारतीय ब्याज दरों और श्रेणी (guild) के नियमों का अध्ययन करता है। उन्हें कौन से साहित्यिक स्रोत (बौद्ध, जैन, ब्राह्मणवादी) चुनने चाहिए और क्यों?",
    "They should select: 1. Dharmasutras/Manusmriti (Brahmanical) for legal limits on interest rates.\n2. Jatakas (Buddhist) for realistic case studies of merchant credit, caravan financing, and guild disputes.\n3. Angas (Jain) for merchant routes, proving how different traditions recorded economic laws and practices.",
    "उन्हें निम्नलिखित का चयन करना चाहिए: 1. ब्याज दरों पर कानूनी सीमा के लिए धर्मसूत्र/मनुस्मृति (ब्राह्मणवादी)।\n2. व्यापारियों के ऋण, कारवां वित्तपोषण और श्रेणी विवादों के यथार्थवादी उदाहरणों के लिए जातक (बौद्ध)।\n3. व्यापारिक मार्गों के लिए अंग (जैन), जिससे यह सिद्ध होता है कि विभिन्न परंपराओं ने आर्थिक कानूनों और प्रथाओं को कैसे दर्ज किया था।"
)
add_open(sec3_en, sec3_hi, "Case Study",
    "During excavation of a site in Bihar, archaeologists find iron tools associated with charred rice grains in a layer dated to c. 800 BCE. Which later Vedic literary texts corroborate this archaeological phase?",
    "बिहार में एक स्थल के उत्खनन के दौरान, पुरातत्वविदों को लगभग 800 ईसा पूर्व की परत में जले हुए धान के दानों के साथ लोहे के उपकरण मिलते हैं। कौन से उत्तर वैदिक साहित्यिक ग्रंथ इस पुरातात्विक चरण की पुष्टि करते हैं?",
    "This archaeological phase is corroborated by later Vedic texts, particularly the Shatapatha Brahmana (which details the expansion into Bihar/Sadaneera and iron tool use) and the Atharvaveda (which mentions iron plowshares, indicating settled rice farming in the Ganga valley).",
    "इस पुरातात्विक चरण की पुष्टि उत्तर वैदिक ग्रंथों द्वारा होती है, विशेष रूप से शतपथ ब्राह्मण (जो बिहार/सदानीरा में विस्तार और लोहे के उपकरणों के उपयोग का विवरण देता है) और अथर्ववेद (जो लोहे के फाल का उल्लेख करता है, जो गंगा घाटी में धान की खेती की ओर संक्रमण को दर्शाता है)।"
)

# 12. Teach the Concept (3 Qs)
add_open(sec3_en, sec3_hi, "Teach the Concept",
    "Explain the concept of 'Sruthi' versus 'Smriti' in ancient Indian literature to a student. Use a modern legal analogy.",
    "एक छात्र को प्राचीन भारतीय साहित्य में 'श्रुति' बनाम 'स्मृति' की अवधारणा समझाएं। एक आधुनिक कानूनी सादृश्य का उपयोग करें।",
    "1. **Shruti** (Hearing): Believed to be direct cosmic truth heard by sages. It is eternal and unchangeable. Analogy: The Constitution (supreme, permanent law).\n2. **Smriti** (Memory): Human recollections and compilations of traditions. They adapt to changing social eras. Analogy: Bylaws or amendments (created by humans, open to revision).",
    "1. **श्रुति** (सुना हुआ): माना जाता है कि यह ऋषियों द्वारा सुनी गई सीधी ब्रह्मांडीय सच्चाई है। यह शाश्वत और अपरिवर्तनीय है। सादृश्य: संविधान (सर्वोच्च, स्थायी कानून)।\n2. **स्मृति** (याद रखा हुआ): मानवीय संस्मरण और परंपराओं का संकलन। वे बदलते सामाजिक युगों के अनुकूल होते हैं। सादृश्य: उप-नियम (bylaws) या संशोधन (मनुष्यों द्वारा बनाए गए, संशोधन के लिए खुले)।"
)
add_open(sec3_en, sec3_hi, "Teach the Concept",
    "How would you teach a student the historical value of the Puranas? Outline three warning traps.",
    "आप किसी छात्र को पुराणों का ऐतिहासिक मूल्य कैसे सिखाएंगे? तीन चेतावनी जाल (warning traps) की रूपरेखा तैयार करें।",
    "1. **Pancha Lakshana**: Teach that Puranas contain genealogies (Vamsha) essential for timelines.\n2. **Trap 1 (Future Tense)**: Explain that dynastic histories are written in a 'prophecy' format, but record past facts.\n3. **Trap 2 (Mythology)**: Warn that gods and sages are mixed with human kings; mythological years must be filtered out.\n4. **Trap 3 (Varying Editions)**: Emphasize that different Puranas must be cross-checked, as they contain sectarian biases.",
    "1. **पंच लक्षण**: सिखाएं कि पुराणों में कालक्रम के लिए आवश्यक वंशावली (वंश) शामिल हैं।\n2. **जाल 1 (भविष्य काल)**: समझाएं कि राजवंशों का इतिहास 'भविष्यवाणी' प्रारूप में लिखा गया है, लेकिन वे पिछले तथ्यों को दर्ज करते हैं।\n3. **जाल 2 (पौराणिक कथाएं)**: चेतावनी दें कि देवताओं और ऋषियों को मानव राजाओं के साथ मिलाया गया है; पौराणिक वर्षों को छानना आवश्यक है।\n4. **जाल 3 (बदलते संस्करण)**: जोर दें कि विभिन्न पुराणों की आपस में जांच की जानी चाहिए, क्योंकि उनमें सांप्रदायिक पूर्वाग्रह होते हैं।"
)
add_open(sec3_en, sec3_hi, "Teach the Concept",
    "Explain why the transition from Sanskrit in Vedas to Pali in Buddhism was a socio-political revolution.",
    "समझाइए कि वेदों में संस्कृत से बौद्ध धर्म में पालि में संक्रमण एक सामाजिक-राजनीतिक क्रांति क्यों थी।",
    "Sanskrit was the language of the elite Brahmins, who claimed exclusive rights to read and execute Vedic rituals, creating a social monopoly. By preaching and writing in Pali, the language of ordinary merchants, farmers, and women, Buddhism demystified spiritual knowledge, bypassing Brahmin authority and creating a democratic literary culture.",
    "संस्कृत कुलीन ब्राह्मणों की भाषा थी, जिन्होंने वैदिक अनुष्ठानों को पढ़ने और निष्पादन पर विशेष अधिकार का दावा किया, जिससे एक सामाजिक एकाधिकार बन गया। पालि (जो साधारण व्यापारियों, किसानों और महिलाओं की भाषा थी) में उपदेश देकर और लिखकर, बौद्ध धर्म ने आध्यात्मिक ज्ञान को आम जनता के लिए सुलभ बना दिया, ब्राह्मणवादी अधिकार को दरकिनार किया और एक लोकतांत्रिक साहित्यिक संस्कृति का निर्माण किया।"
)

# ==========================================
# SECTION 4: FOREIGN ACCOUNTS
# ==========================================

# 1. MCQ (5 Qs)
add_mcq(sec4_en, sec4_hi,
    "Which Greek ambassador visited the Mauryan court of Chandragupta Maurya and wrote the famous text 'Indica'?",
    "किस यूनानी राजदूत ने चंद्रगुप्त मौर्य के मौर्य दरबार का दौरा किया और प्रसिद्ध ग्रंथ 'इण्डिका' लिखा था?",
    ["Deimachus", "Megasthenes", "Herodotus", "Ptolemy"],
    ["डेइमेकस", "मेगास्थनीज", "हेरोडोटस", "टॉलेमी"],
    1,
    "Megasthenes served as the Seleucid ambassador to Chandragupta Maurya's court and compiled 'Indica', which survives only in fragments.",
    "मेगास्थनीज ने चंद्रगुप्त मौर्य के दरबार में सेल्यूसिड राजदूत के रूप में कार्य किया और 'इण्डिका' का संकलन किया, जो केवल अंशों (fragments) में जीवित है।"
)
add_mcq(sec4_en, sec4_hi,
    "Which Roman writer wrote the 'Naturalis Historia' (Natural History) in Latin and lamented the drain of Roman gold to India?",
    "किस रोमन लेखक ने लैटिन में 'नेचुरलिस हिस्टोरिया' (प्राकृतिक इतिहास) लिखा था और भारत में रोमन सोने के निकास पर खेद व्यक्त किया था?",
    ["Ptolemy", "Pliny the Elder", "Arrian", "Strabo"],
    ["टॉलेमी", "प्लिनी द एल्डर (Pliny the Elder)", "एरियन", "स्ट्रैबो"],
    1,
    "Pliny the Elder wrote Natural History in Latin (1st century CE), noting that Rome drained 55 million sesterces annually to India for luxury goods.",
    "प्लिनी द एल्डर ने पहली शताब्दी ईस्वी में लैटिन में नेचुरल हिस्ट्री लिखी थी, जिसमें उल्लेख था कि रोम विलासिता के सामानों के लिए भारत में सालाना 55 मिलियन सेस्टरस का निकास करता था।"
)
add_mcq(sec4_en, sec4_hi,
    "The anonymous 1st-century CE sailor's guidebook that provides detailed descriptions of ports, trade routes, and exports along the Indian Ocean is:",
    "पहली शताब्दी ईस्वी के अज्ञात नाविक की वह गाइडबुक कौन सी है जो हिंद महासागर के बंदरगाहों, व्यापारिक मार्गों और निर्यात का विस्तृत विवरण प्रदान करती है?",
    ["Geography of Ptolemy", "Indica of Megasthenes", "Periplus of the Erythraean Sea", "Kitab-ul-Hind"],
    ["टॉलेमी का भूगोल", "मेगास्थनीज की इण्डिका", "पेरिप्लस ऑफ द एरीथ्रियन सी (Periplus of the Erythraean Sea)", "किताब-उल-हिंद"],
    2,
    "The Periplus of the Erythraean Sea is an anonymous Greek logbook documenting Indian ports like Barygaza (Bharuch), Muziris, and Arikamedu.",
    "पेरिप्लस ऑफ द एरीथ्रियन सी एक अज्ञात यूनानी लॉगबुक है जो भड़ौच (Barygaza), मुज़िरिस और अरिकामेडु जैसे भारतीय बंदरगाहों का दस्तावेजीकरण करती है।"
)
add_mcq(sec4_en, sec4_hi,
    "Which Chinese Buddhist pilgrim visited India during the reign of Chandragupta II (Gupta dynasty) and wrote 'Fo-Kwo-Ki'?",
    "किस चीनी बौद्ध तीर्थयात्री ने चंद्रगुप्त द्वितीय (गुप्त राजवंश) के शासनकाल के दौरान भारत का दौरा किया और 'फो-कुओ-की' लिखा था?",
    ["Hiuen Tsang", "Fa-Hien", "I-Tsing", "Song Yun"],
    ["ह्वेनसांग", "फाह्यान (Fa-Hien)", "इत्सिंग", "सोंग युन"],
    1,
    "Fa-Hien (399-414 CE) visited India during the Gupta reign of Chandragupta II to collect Buddhist scriptures.",
    "फाह्यान (399-414 ईस्वी) ने बौद्ध ग्रंथों को एकत्र करने के लिए चंद्रगुप्त द्वितीय के गुप्त शासनकाल के दौरान भारत का दौरा किया था।"
)
add_mcq(sec4_en, sec4_hi,
    "The 11th-century Central Asian polymath who accompanied Mahmud of Ghazni and wrote 'Kitab-ul-Hind' was:",
    "महमूद गजनवी के साथ आने वाले और 'किताब-उल-हिंद' लिखने वाले 11वीं शताब्दी के मध्य एशियाई बहुश्रुत कौन थे?",
    ["Al-Masudi", "Al-Biruni", "Ibn Battuta", "Firdausi"],
    ["अल-मसूदी", "अल-बिरूनी (Al-Biruni)", "इब्न बतूता", "फिरदौसी"],
    1,
    "Al-Biruni wrote Tarikh-al-Hind (Kitab-ul-Hind) in Arabic, providing an objective study of Indian culture, astronomy, mathematics, and caste system.",
    "अल-बिरूनी ने अरबी में तारीख-अल-हिंद (किताब-उल-हिंद) लिखी थी, जो भारतीय संस्कृति, खगोल विज्ञान, गणित और जाति व्यवस्था का एक निष्पक्ष अध्ययन प्रदान करती है।"
)

# 2. Multiple Correct MCQ (5 Qs)
add_multi_mcq(sec4_en, sec4_hi,
    "Which of the following Chinese travellers visited India during the post-Gupta/Harsha and early medieval periods? (Select all that apply)",
    "निम्नलिखित में से किस चीनी यात्री ने उत्तर-गुप्त/हर्ष और प्रारंभिक मध्यकाल के दौरान भारत का दौरा किया था? (सभी लागू विकल्प चुनें)",
    ["Fa-Hien", "Hiuen Tsang (Xuanzang)", "I-Tsing (Yijing)", "Megasthenes"],
    ["फाह्यान", "ह्वेनसांग (Xuanzang)", "इत्सिंग (Yijing)", "मेगास्थनीज"],
    [1, 2],
    "Hiuen Tsang (7th century, Harsha) and I-Tsing (late 7th century) visited in the post-Gupta era. Fa-Hien visited in the Gupta era. Megasthenes was Greek.",
    "ह्वेनसांग (7वीं शताब्दी, हर्ष) और इत्सिंग (7वीं शताब्दी के अंत में) उत्तर-गुप्त काल में आए थे। फाह्यान गुप्त काल में आए थे। मेगास्थनीज यूनानी थे।"
)
add_multi_mcq(sec4_en, sec4_hi,
    "Which of the following Indian ports are explicitly documented in the 'Periplus of the Erythraean Sea'? (Select all that apply)",
    "निम्नलिखित में से कौन से भारतीय बंदरगाह 'पेरिप्लस ऑफ द एरीथ्रियन सी' में स्पष्ट रूप से प्रलेखित हैं? (सभी लागू विकल्प चुनें)",
    ["Barygaza (Bharuch)", "Muziris", "Arikamedu (Poduke)", "Pataliputra"],
    ["भड़ौच (Barygaza)", "मुज़िरिस (Muziris)", "अरिकामेडु (Poduke)", "पाटलिपुत्र"],
    [0, 1, 2],
    "Barygaza, Muziris, and Poduke (Arikamedu) are ports documented in the Periplus. Pataliputra is an inland capital city.",
    "भड़ौच, मुज़िरिस और पोडुके (अरिकामेडु) पेरिप्लस में प्रलेखित बंदरगाह हैं। पाटलिपुत्र एक अंतर्देशीय राजधानी शहर है।"
)
add_multi_mcq(sec4_en, sec4_hi,
    "Which of the following descriptions represent Megasthenes' observations in 'Indica'? (Select all that apply)",
    "निम्नलिखित में से कौन से विवरण मेगास्थनीज की 'इण्डिका' में उनके अवलोकनों को दर्शाते हैं? (सभी लागू विकल्प चुनें)",
    ["Divided Indian society into seven castes", "Stated that slavery was absent in India", "Described the administrative board of Pataliputra", "Recorded the rise of Buddhism under Ashoka"],
    ["भारतीय समाज को सात जातियों में विभाजित किया", "कहा कि भारत में गुलामी अनुपस्थित थी", "पाटलिपुत्र के प्रशासनिक बोर्ड का वर्णन किया", "अशोक के अधीन बौद्ध धर्म के उदय को रिकॉर्ड किया"],
    [0, 1, 2],
    "Megasthenes described 7 castes, noted no slavery, and detailed Pataliputra administration. Ashoka reigned after Megasthenes' visit.",
    "मेगास्थनीज ने 7 जातियों का वर्णन किया, उल्लेख किया कि दासता नहीं थी, और पाटलिपुत्र प्रशासन का विवरण दिया। अशोक मेगास्थनीज के आगमन के बाद शासक बने थे।"
)
add_multi_mcq(sec4_en, sec4_hi,
    "Which of the following fields of study did Al-Biruni analyze in 'Kitab-ul-Hind'? (Select all that apply)",
    "निम्नलिखित में से किस अध्ययन क्षेत्र का अल-बिरूनी ने 'किताब-उल-हिंद' में विश्लेषण किया था? (सभी लागू विकल्प चुनें)",
    ["Sanskrit grammar and literature", "Hindu religious philosophy", "Indian astronomy and mathematics", "Detailed dynastic genealogies of Cholas"],
    ["संस्कृत व्याकरण और साहित्य", "हिंदू धार्मिक दर्शन", "भारतीय खगोल विज्ञान और गणित", "चोलों की विस्तृत राजवंश वंशावली"],
    [0, 1, 2],
    "Al-Biruni studied Sanskrit, Hindu philosophy, astronomy, and math. He did not analyze Chola genealogies, as he was based in northwestern India.",
    "अल-बिरूनी ने संस्कृत, हिंदू दर्शन, खगोल विज्ञान और गणित का अध्ययन किया। उन्होंने चोलों की वंशावली का विश्लेषण नहीं किया, क्योंकि वे उत्तर-पश्चिमी भारत में केंद्रित थे।"
)
add_multi_mcq(sec4_en, sec4_hi,
    "Which Roman or Greek writers cite fragments of Megasthenes' lost 'Indica' in their own works? (Select all that apply)",
    "कौन से रोमन या यूनानी लेखक अपने स्वयं के कार्यों में मेगास्थनीज की खोई हुई 'इण्डिका' के अंशों को उद्धृत करते हैं? (सभी लागू विकल्प चुनें)",
    ["Arrian", "Strabo", "Pliny", "Al-Biruni"],
    ["एरियन", "स्ट्रैबो", "प्लिनी", "अल-बिरूनी"],
    [0, 1, 2],
    "Arrian, Strabo, Diodorus, and Pliny cite Megasthenes' Indica. Al-Biruni was an 11th-century Arabic-writing Persian scholar.",
    "एरियन, स्ट्रैबो, डियोडोरस और प्लिनी मेगास्थनीज की इण्डिका को उद्धृत करते हैं। अल-बिरूनी 11वीं शताब्दी के अरबी-लेखक फारसी विद्वान थे।"
)

# 3. True/False (8 Qs)
add_tf(sec4_en, sec4_hi,
    "Herodotus, the 'Father of History', visited the Gangetic plains and described the Mauryan administration.",
    "इतिहास के जनक हेरोडोटस ने गंगा के मैदानों का दौरा किया और मौर्य प्रशासन का वर्णन किया।",
    False,
    "Herodotus never visited India; he wrote about the Persian Satrapy of Gandhara based on secondary Persian accounts.",
    "हेरोडोटस कभी भारत नहीं आए; उन्होंने माध्यमिक फारसी विवरणों के आधार पर गांधार की फारसी क्षत्रप प्रणाली के बारे में लिखा था।"
)
add_tf(sec4_en, sec4_hi,
    "Megasthenes' original manuscript of 'Indica' is preserved in the British Museum.",
    "मेगास्थनीज की 'इण्डिका' की मूल पांडुलिपि ब्रिटिश संग्रहालय में सुरक्षित है।",
    False,
    "Megasthenes' original 'Indica' is completely lost. Its contents are known only through citations in later Greek and Roman texts.",
    "मेगास्थनीज की मूल 'इण्डिका' पूरी तरह से खो चुकी है। इसकी सामग्री केवल बाद के यूनानी और रोमन ग्रंथों में उद्धरणों के माध्यम से जानी जाती है।"
)
add_tf(sec4_en, sec4_hi,
    "The anonymous work 'Periplus of the Erythraean Sea' was written by a Roman emperor.",
    "अनाम कृति 'पेरिप्लस ऑफ द एरीथ्रियन सी' एक रोमन सम्राट द्वारा लिखी गई थी।",
    False,
    "It was written by an anonymous Greek-speaking merchant-sailor based in Alexandria, Egypt, not an emperor.",
    "यह अलेक्जेंड्रिया, मिस्र में रहने वाले एक अज्ञात यूनानी भाषी व्यापारी-नाविक द्वारा लिखी गई थी, न कि किसी सम्राट द्वारा।"
)
add_tf(sec4_en, sec4_hi,
    "Fa-Hien visited India during the reign of Harsha and studied at Nalanda University.",
    "फाह्यान ने हर्ष के शासनकाल के दौरान भारत का दौरा किया और नालंदा विश्वविद्यालय में अध्ययन किया।",
    False,
    "Hiuen Tsang studied at Nalanda during Harsha's reign. Fa-Hien visited during the Gupta period (Chandragupta II) when Nalanda was not yet a major center.",
    "ह्वेनसांग ने हर्ष के शासनकाल के दौरान नालंदा में अध्ययन किया था। फाह्यान ने गुप्त काल (चंद्रगुप्त द्वितीय) के दौरान दौरा किया था जब नालंदा अभी बड़ा केंद्र नहीं था।"
)
add_tf(sec4_en, sec4_hi,
    "Hiuen Tsang (Xuanzang) attended the great religious assembly at Kanauj organized by King Harsha.",
    "ह्वेनसांग (Xuanzang) राजा हर्ष द्वारा आयोजित कन्नौज की महान धार्मिक सभा में शामिल हुए थे।",
    True,
    "Hiuen Tsang was the guest of honor at Harsha's Kanauj assembly in 643 CE.",
    "ह्वेनसांग 643 ईस्वी में हर्ष की कन्नौज सभा में सम्मानित अतिथि थे।"
)
add_tf(sec4_en, sec4_hi,
    "Al-Biruni translated Sanskrit works, including Patanjali's Yoga Sutras, into Arabic.",
    "अल-बिरूनी ने पतंजलि के योग सूत्रों सहित संस्कृत कृतियों का अरबी में अनुवाद किया था।",
    True,
    "Al-Biruni translated Sanskrit mathematical, astronomical, and philosophical texts (like Yoga Sutras) into Arabic.",
    "अल-बिरूनी ने संस्कृत गणितीय, खगोलीय और दार्शनिक ग्रंथों (जैसे योग सूत्र) का अरबी में अनुवाद किया था।"
)
add_tf(sec4_en, sec4_hi,
    "Ptolemy's Geography (2nd century CE) contains the first detailed map of India with river courses.",
    "टॉलेमी के भूगोल (दूसरी शताब्दी ईस्वी) में नदी मार्गों के साथ भारत का पहला विस्तृत मानचित्र शामिल है।",
    True,
    "Ptolemy mapped India's rivers and ports, which, despite structural distortions, served as primary cartographic data.",
    "टॉलेमी ने भारत की नदियों और बंदरगाहों का मानचित्र बनाया, जिसने संरचनात्मक विकृतियों के बावजूद प्राथमिक मानचित्र डेटा के रूप में कार्य किया।"
)
add_tf(sec4_en, sec4_hi,
    "Fa-Hien described the Gupta administration as extremely harsh, with frequent executions and heavy taxes.",
    "फाह्यान ने गुप्त प्रशासन को अत्यंत कठोर बताया, जिसमें बार-बार मृत्युदंड और भारी कर लगाए जाते थे।",
    False,
    "Fa-Hien described Gupta administration as mild, noting that capital punishment was rare, travel was safe, and taxes were light.",
    "फाह्यान ने गुप्त प्रशासन को सौम्य बताया, यह उल्लेख करते हुए कि मृत्युदंड दुर्लभ था, यात्रा सुरक्षित थी, और कर हल्के थे।"
)

# 4. Fill in the Blank (8 Qs)
add_blank(sec4_en, sec4_hi,
    "The Seleucid ambassador who wrote 'Indica' was ________.",
    "सेल्यूसिड राजदूत जिसने 'इण्डिका' लिखी थी, ________ था।",
    "Megasthenes", "मेगास्थनीज",
    "Megasthenes stayed in Pataliputra as the envoy of Seleucus I Nicator.",
    "मेगास्थनीज सेल्यूकस प्रथम निकेटर के दूत के रूप में पाटलिपुत्र में रहे थे।"
)
add_blank(sec4_en, sec4_hi,
    "The 1st-century CE Roman author who lamented the drainage of Roman gold to India in 'Natural History' was ________.",
    "पहली शताब्दी ईस्वी के रोमन लेखक जिन्होंने 'नेचुरल हिस्ट्री' में भारत को होने वाले रोमन सोने के नुकसान पर खेद व्यक्त किया था, ________ थे।",
    "Pliny the Elder", "प्लिनी द एल्डर",
    "Pliny lamented the economic drain caused by Rome's import of Indian luxuries.",
    "प्लिनी ने भारतीय विलासिता की वस्तुओं के आयात के कारण होने वाले आर्थिक नुकसान पर खेद व्यक्त किया।"
)
add_blank(sec4_en, sec4_hi,
    "The anonymous Greek guidebook describing Indian ports and Ocean trade routes is the ________.",
    "भारतीय बंदरगाहों और समुद्री व्यापार मार्गों का वर्णन करने वाली अनाम यूनानी गाइडबुक ________ है।",
    "Periplus of the Erythraean Sea", "पेरिप्लस ऑफ द एरीथ्रियन सी",
    "Written in Greek by an Egyptian Greek sailor in the 1st century CE.",
    "पहली शताब्दी ईस्वी में मिस्र के एक यूनानी नाविक द्वारा यूनानी भाषा में लिखा गया था।"
)
add_blank(sec4_en, sec4_hi,
    "The Chinese pilgrim who visited India during the reign of King Harsha was ________.",
    "राजा हर्ष के शासनकाल के दौरान भारत का दौरा करने वाले चीनी तीर्थयात्री ________ थे।",
    "Hiuen Tsang", "ह्वेनसांग",
    "Xuanzang (Hiuen Tsang) traveled to India between 630 and 645 CE.",
    "शुआनजांग (ह्वेनसांग) ने 630 और 645 ईस्वी के बीच भारत की यात्रा की थी।"
)
add_blank(sec4_en, sec4_hi,
    "Al-Biruni's famous Arabic treatise on Indian sciences, customs, and philosophy is titled ________.",
    "भारतीय विज्ञान, रीति-रिवाजों और दर्शन पर अल-बिरूनी के प्रसिद्ध अरबी ग्रंथ का शीर्षक ________ है।",
    "Kitab-ul-Hind", "किताब-उल-हिंद",
    "Also known as Tarikh-al-Hind or Tahqiq-ma-lil-Hind.",
    "इसे तारीख-अल-हिंद या तहकीक-मा-लिल-हिंद भी कहा जाता है।"
)
add_blank(sec4_en, sec4_hi,
    "The Greek writer known as the 'Father of History' who first mentioned 'Indica' was ________.",
    "यूनानी लेखक जिन्हें 'इतिहास का जनक' कहा जाता है, जिन्होंने सबसे पहले 'इण्डिका' का उल्लेख किया था, ________ थे।",
    "Herodotus", "हेरोडोटस",
    "Herodotus wrote about the Persian-Indian borderlands in the 5th century BCE.",
    "हेरोडोटस ने 5वीं शताब्दी ईसा पूर्व में फारसी-भारतीय सीमावर्ती क्षेत्रों के बारे में लिखा था।"
)
add_blank(sec4_en, sec4_hi,
    "The 2nd-century CE geographer who drew a famous map locating Indian rivers and ports was ________.",
    "दूसरी शताब्दी ईस्वी के भूगोलवेत्ता जिन्होंने भारतीय नदियों और बंदरगाहों को दर्शाने वाला एक प्रसिद्ध मानचित्र बनाया था, ________ थे।",
    "Ptolemy", "टॉलेमी",
    "Claudius Ptolemy wrote the 'Geographia' in Alexandria.",
    "क्लॉडियस टॉलेमी ने अलेक्जेंड्रिया में 'जियोग्राफिया' लिखी थी।"
)
add_blank(sec4_en, sec4_hi,
    "The 7th-century CE Chinese Buddhist pilgrim who recorded Nalanda's monastic rules after Xuanzang was ________.",
    "7वीं शताब्दी ईस्वी के चीनी बौद्ध तीर्थयात्री जिन्होंने शुआनजांग के बाद नालंदा के मठवासी नियमों को रिकॉर्ड किया था, वो ________ थे।",
    "I-Tsing", "इत्सिंग",
    "I-Tsing (Yijing) stayed at Nalanda for ten years translating texts.",
    "इत्सिंग (Yijing) ने ग्रंथों का अनुवाद करते हुए दस साल नालंदा में बिताए थे।"
)

# 5. Match the Following (3 Qs)
add_match(sec4_en, sec4_hi,
    "Match the travellers with their country of origin:",
    "यात्रियों को उनके मूल देश के साथ सुमेलित करें:",
    [{"left": "Megasthenes", "key": "greece"}, {"left": "Fa-Hien", "key": "china"}, {"left": "Al-Biruni", "key": "persia"}],
    [{"left": "मेगास्थनीज", "key": "greece"}, {"left": "फाह्यान", "key": "china"}, {"left": "अल-बिरूनी", "key": "persia"}],
    [{"val": "greece", "text": "Greek/Macedonian Empire"}, {"val": "china", "text": "China (Imperial Dynasty)"}, {"val": "persia", "text": "Persia/Central Asia"}],
    [{"val": "greece", "text": "यूनानी/मकदूनियाई साम्राज्य"}, {"val": "china", "text": "चीन (शाही राजवंश)"}, {"val": "persia", "text": "फारस/मध्य एशिया"}],
    "Megasthenes is Greek; Fa-Hien is Chinese; Al-Biruni is Persian/Khwarazmian.",
    "मेगास्थनीज यूनानी हैं; फाह्यान चीनी हैं; अल-बिरूनी फारसी/ख्वारिज्मी हैं।"
)
add_match(sec4_en, sec4_hi,
    "Match the foreign accounts with their primary language:",
    "विदेशी विवरणों को उनकी प्राथमिक भाषा के साथ सुमेलित करें:",
    [{"left": "Indica of Megasthenes", "key": "greek"}, {"left": "Natural History of Pliny", "key": "latin"}, {"left": "Kitab-ul-Hind", "key": "arabic"}],
    [{"left": "मेगास्थनीज की इण्डिका", "key": "greek"}, {"left": "प्लिनी की नेचुरल हिस्ट्री", "key": "latin"}, {"left": "किताब-उल-हिंद", "key": "arabic"}],
    [{"val": "greek", "text": "Ancient Greek"}, {"val": "latin", "text": "Classical Latin"}, {"val": "arabic", "text": "Classical Arabic"}],
    [{"val": "greek", "text": "प्राचीन यूनानी"}, {"val": "latin", "text": "शास्त्रीय लैटिन"}, {"val": "arabic", "text": "शास्त्रीय अरबी"}],
    "Indica was written in Greek, Pliny wrote in Latin, and Al-Biruni wrote in Arabic.",
    "इण्डिका यूनानी में लिखी गई थी, प्लिनी ने लैटिन में लिखा था, और अल-बिरूनी ने अरबी में लिखा था।"
)
add_match(sec4_en, sec4_hi,
    "Match the travellers with the rulers they visited:",
    "यात्रियों को उनके द्वारा यात्रा किए गए शासकों के साथ सुमेलित करें:",
    [{"left": "Megasthenes", "key": "chandragupta-m"}, {"left": "Fa-Hien", "key": "chandragupta-ii"}, {"left": "Hiuen Tsang", "key": "harsha"}],
    [{"left": "मेगास्थनीज", "key": "chandragupta-m"}, {"left": "फाह्यान", "key": "chandragupta-ii"}, {"left": "ह्वेनसांग", "key": "harsha"}],
    [{"val": "chandragupta-m", "text": "Chandragupta Maurya"}, {"val": "chandragupta-ii", "text": "Chandragupta II (Gupta)"}, {"val": "harsha", "text": "Harsha Vardhana"}],
    [{"val": "chandragupta-m", "text": "चंद्रगुप्त मौर्य"}, {"val": "chandragupta-ii", "text": "चंद्रगुप्त द्वितीय (गुप्त)"}, {"val": "harsha", "text": "हर्षवर्धन"}],
    "Megasthenes visited Chandragupta Maurya; Fa-Hien visited Chandragupta II; Hiuen Tsang visited Harsha.",
    "मेगास्थनीज चंद्रगुप्त मौर्य के पास गए; फाह्यान चंद्रगुप्त द्वितीय के पास गए; ह्वेनसांग हर्ष के पास गए।"
)

# 6. One-Liner (8 Qs)
add_oneliner(sec4_en, sec4_hi,
    "What is the name of the lost book written by Megasthenes?",
    "मेगास्थनीज द्वारा लिखित खोई हुई पुस्तक का नाम क्या है?",
    "Indica.",
    "इण्डिका।"
)
add_oneliner(sec4_en, sec4_hi,
    "Which Roman writer lamented that Rome's wealth was drained to India?",
    "किस रोमन लेखक ने खेद व्यक्त किया था कि रोम का धन भारत की ओर बह रहा था?",
    "Pliny the Elder in his work 'Natural History'.",
    "प्लिनी द एल्डर ने अपनी रचना 'नेचुरल हिस्ट्री' में।"
)
add_oneliner(sec4_en, sec4_hi,
    "Who is the author of 'Periplus of the Erythraean Sea'?",
    "'पेरिप्लस ऑफ द एरीथ्रियन सी' का लेखक कौन है?",
    "The author is anonymous (an unnamed Greek-speaking merchant-sailor).",
    "लेखक अज्ञात है (एक अनाम यूनानी भाषी व्यापारी-नाविक)।"
)
add_oneliner(sec4_en, sec4_hi,
    "Name the Chinese traveller who visited India during the Gupta period.",
    "गुप्त काल के दौरान भारत का दौरा करने वाले चीनी यात्री का नाम बताइए।",
    "Fa-Hien.",
    "फाह्यान।"
)
add_oneliner(sec4_en, sec4_hi,
    "At which ancient university did Hiuen Tsang study Buddhist philosophy?",
    "ह्वेनसांग ने किस प्राचीन विश्वविद्यालय में बौद्ध दर्शन का अध्ययन किया था?",
    "Nalanda University in Bihar.",
    "बिहार में नालंदा विश्वविद्यालय।"
)
add_oneliner(sec4_en, sec4_hi,
    "Which Persian scholar wrote the 'Kitab-ul-Hind'?",
    "किस फारसी विद्वान ने 'किताब-उल-हिंद' लिखी थी?",
    "Al-Biruni.",
    "अल-बिरूनी।"
)
add_oneliner(sec4_en, sec4_hi,
    "Why did Fa-Hien visit India?",
    "फाह्यान ने भारत का दौरा क्यों किया?",
    "To collect authentic Buddhist Vinaya (monastic) scriptures.",
    "प्रामाणिक बौद्ध विनय (मठवासी) ग्रंथों को एकत्र करने के लिए।"
)
add_oneliner(sec4_en, sec4_hi,
    "Which Chinese pilgrim visited India after Xuanzang and documented the rules of Nalanda monks?",
    "शुआनजांग के बाद किस चीनी तीर्थयात्री ने भारत का दौरा किया और नालंदा के भिक्षुओं के नियमों का दस्तावेजीकरण किया?",
    "I-Tsing.",
    "इत्सिंग।"
)

# 7. Assertion-Reason (8 Qs)
add_ar(sec4_en, sec4_hi,
    "Assertion (A): Megasthenes stated that famine was unknown in India and slavery was absent.\nReason (R): He interpreted Indian social relations using Greek categories, failing to recognize local forms of debt-bondage (dasas).",
    "कथन (A): मेगास्थनीज ने कहा कि भारत में अकाल अज्ञात था और गुलामी अनुपस्थित थी।\nकारण (R): उन्होंने यूनानी श्रेणियों का उपयोग करके भारतीय सामाजिक संबंधों की व्याख्या की, जिससे वे ऋण-बंधन (दासों) के स्थानीय रूपों को पहचानने में विफल रहे।",
    0,
    "Both A and R are true, and R correctly explains the cognitive bias that led Megasthenes to claim slavery did not exist.",
    "A और R दोनों सही हैं और R उस संज्ञानात्मक पूर्वाग्रह (cognitive bias) की सही व्याख्या करता है जिसके कारण मेगास्थनीज ने दावा किया था कि गुलामी नहीं थी।"
)
add_ar(sec4_en, sec4_hi,
    "Assertion (A): The 'Periplus of the Erythraean Sea' is highly valued for compiling Mauryan genealogies.\nReason (R): It was written during the reign of Chandragupta Maurya and lists his council ministers.",
    "कथन (A): 'पेरिप्लस ऑफ द एरीथ्रियन सी' को मौर्य वंशावलियों के संकलन के लिए अत्यधिक महत्व दिया जाता है।\nकारण (R): यह चंद्रगुप्त मौर्य के शासनकाल के दौरान लिखा गया था और इसमें उनके परिषद मंत्रियों की सूची है।",
    3,
    "A is false but R is false. The Periplus is a 1st-century CE trade logbook focused on ports and commercial exports, containing no Mauryan dynastic information.",
    "A गलत है और R गलत है। पेरिप्लस पहली शताब्दी ईस्वी की व्यापारिक लॉगबुक है जो बंदरगाहों और वाणिज्यिक निर्यात पर केंद्रित है, इसमें कोई मौर्यकालीन वंशावली की जानकारी नहीं है।"
)
add_ar(sec4_en, sec4_hi,
    "Assertion (A): Hiuen Tsang spent several years at Nalanda University.\nReason (R): He wanted to study Mahayana Buddhist philosophy under the guidance of the venerable teacher Shilabhadra.",
    "कथन (A): ह्वेनसांग ने नालंदा विश्वविद्यालय में कई वर्ष बिताए।\nकारण (R): वे आदरणीय शिक्षक शीलभद्र के मार्गदर्शन में महायान बौद्ध दर्शन का अध्ययन करना चाहते थे।",
    0,
    "Both A and R are true, and R is the correct explanation of A.",
    "A और R दोनों सही हैं और R, A की सही व्याख्या करता है।"
)
add_ar(sec4_en, sec4_hi,
    "Assertion (A): Fa-Hien provides a detailed account of the military achievements of Chandragupta II.\nReason (R): He was appointed as a court historian by the Gupta emperor.",
    "कथन (A): फाह्यान चंद्रगुप्त द्वितीय की सैन्य उपलब्धियों का विस्तृत विवरण प्रदान करते हैं।\nकारण (R): उन्हें गुप्त सम्राट द्वारा दरबारी इतिहासकार के रूप में नियुक्त किया गया था।",
    3,
    "Both statements are false. Fa-Hien was a religious pilgrim who focused purely on Buddhist sites; he does not even mention the name of Chandragupta II in his memoir, and was never a court employee.",
    "दोनों कथन गलत हैं। फाह्यान एक धार्मिक तीर्थयात्री थे जिन्होंने विशुद्ध रूप से बौद्ध स्थलों पर ध्यान केंद्रित किया; उन्होंने अपने संस्मरण में चंद्रगुप्त द्वितीय के नाम तक का उल्लेख नहीं किया है और वे कभी भी दरबारी कर्मचारी नहीं थे।"
)
add_ar(sec4_en, sec4_hi,
    "Assertion (A): Al-Biruni's Kitab-ul-Hind is noted for its rigorous scientific methodology.\nReason (R): He begins each chapter with a structured question, followed by Sanskrit definitions, and ends with a comparative analysis of Greek/Persian culture.",
    "कथन (A): अल-बिरूनी की किताब-उल-हिंद अपनी कठोर वैज्ञानिक पद्धति के लिए प्रसिद्ध है।\nकारण (R): वे प्रत्येक अध्याय की शुरुआत एक संरचित प्रश्न से करते हैं, जिसके बाद संस्कृत परिभाषाएँ देते हैं और अंत में यूनानी/फारसी संस्कृति के तुलनात्मक विश्लेषण के साथ समाप्त करते हैं।",
    0,
    "Both A and R are true, and R explains the specific structural scientific methodology used by Al-Biruni.",
    "A और R दोनों सही हैं और R अल-बिरूनी द्वारा उपयोग की जाने वाली विशिष्ट संरचित वैज्ञानिक पद्धति की व्याख्या करता है।"
)
add_ar(sec2_en, sec2_hi,
    "Assertion (A): Ptolemy's Geography was highly accurate in mapping the peninsular shape of India.\nReason (R): He utilized advanced GPS satellites to record the coordinates of Barygaza and Arikamedu.",
    "कथन (A): टॉलेमी का भूगोल भारत के प्रायद्वीपीय आकार के मानचित्रण में अत्यधिक सटीक था।\nकारण (R): उन्होंने भड़ौच और अरिकामेडु के निर्देशांक रिकॉर्ड करने के लिए उन्नत जीपीएस उपग्रहों का उपयोग किया था।",
    3,
    "Both A and R are false. Ptolemy's map suffered from severe distortions, squeezing the peninsular shape of India, and GPS satellites did not exist.",
    "A और R दोनों गलत हैं। टॉलेमी के मानचित्र में गंभीर विकृतियां थीं, जिससे भारत का प्रायद्वीपीय आकार सिकुड़ गया था, और जीपीएस उपग्रहों का अस्तित्व नहीं था।"
)
add_ar(sec4_en, sec4_hi,
    "Assertion (A): Chinese pilgrim accounts are critical for establishing historic timelines of India.\nReason (R): They record dates of Indian kings relative to Chinese dynastic calendars, which were precisely maintained.",
    "कथन (A): चीनी तीर्थयात्रियों के विवरण भारत की ऐतिहासिक समयसीमा स्थापित करने के लिए महत्वपूर्ण हैं।\nकारण (R): वे चीनी शाही कैलेंडरों के सापेक्ष भारतीय राजाओं की तिथियों को दर्ज करते हैं, जिन्हें सटीक रूप से बनाए रखा गया था।",
    0,
    "Both A and R are true, and R explains why Chinese traveler logs serve as absolute chronological anchors.",
    "A और R दोनों सही हैं और R व्याख्या करता है कि क्यों चीनी यात्रियों के रिकॉर्ड निरपेक्ष कालानुक्रमिक एंकर के रूप में कार्य करते हैं।"
)
add_ar(sec4_en, sec4_hi,
    "Assertion (A): Al-Biruni accompanied Mahmud of Ghazni primarily to praise his military raids in India.\nReason (R): He served as the official court chronicler of the Ghaznavid military empire.",
    "कथन (A): अल-बिरूनी मुख्य रूप से भारत में महमूद गजनवी के सैन्य छापों की प्रशंसा करने के लिए उनके साथ आए थे।\nकारण (R): उन्होंने गजनवी सैन्य साम्राज्य के आधिकारिक दरबारी इतिहासकार के रूप में कार्य किया था।",
    3,
    "Both A and R are false. Al-Biruni was a hostage scholar brought from Khwarazm; he did not praise Mahmud's raids and instead wrote an objective, academic study of Indian culture, showing no interest in military flatteries.",
    "A और R दोनों गलत हैं। अल-बिरूनी ख्वारिज्म से लाए गए बंधक विद्वान थे; उन्होंने महमूद के छापों की प्रशंसा नहीं की, बल्कि भारतीय संस्कृति का एक निष्पक्ष, शैक्षणिक अध्ययन लिखा।"
)

# 8. Statement-Based (5 Qs)
add_stmt(sec4_en, sec4_hi,
    "Consider the following statements regarding Megasthenes' Indica:\n1. The original book is completely lost to history.\n2. He described the Maurya capital Pataliputra as surrounded by a wooden wall and ditch.\n3. He identified seven castes in Indian society, including philosophers and artisans.\nWhich of the statements given above are correct?",
    "मेगास्थनीज की इण्डिका के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. मूल पुस्तक इतिहास में पूरी तरह से खो चुकी है।\n2. उन्होंने मौर्य राजधानी पाटलिपुत्र का वर्णन लकड़ी की दीवार और खाई से घिरे शहर के रूप में किया।\n3. उन्होंने भारतीय समाज में सात जातियों की पहचान की, जिनमें दार्शनिक और कारीगर शामिल थे।\nऊपर दिए गए कथनों में से कौन से सही हैं?",
    ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
    ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
    3,
    "All three statements are correct and define the core surviving details of Megasthenes' Indica.",
    "तीनों कथन सही हैं और मेगास्थनीज की इण्डिका के जीवित बचे मुख्य विवरणों को परिभाषित करते हैं।"
)
add_stmt(sec4_en, sec4_hi,
    "Consider the following statements regarding Chinese pilgrims in India:\n1. Fa-Hien traveled to India by land and returned by sea.\n2. Hiuen Tsang studied at Nalanda under the chancellor Shilabhadra.\n3. Both pilgrims visited during the reign of Chandragupta Maurya.\nWhich of the statements given above is/are correct?",
    "भारत में चीनी तीर्थयात्रियों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. फाह्यान ने भूमि मार्ग से भारत की यात्रा की और समुद्री मार्ग से लौटे।\n2. ह्वेनसांग ने नालंदा में कुलपति शीलभद्र के अधीन अध्ययन किया।\n3. दोनों तीर्थयात्रियों ने चंद्रगुप्त मौर्य के शासनकाल के दौरान दौरा किया था।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 and 2 only", "2 and 3 only", "3 only", "1, 2 and 3"],
    ["केवल 1 और 2", "केवल 2 और 3", "केवल 3", "1, 2 और 3"],
    0,
    "Statements 1 and 2 are correct. Neither visited during Chandragupta Maurya's reign (Fa-Hien visited Chandragupta II; Hiuen Tsang visited Harsha).",
    "कथन 1 और 2 सही हैं। दोनों में से किसी ने भी चंद्रगुप्त मौर्य के शासनकाल में दौरा नहीं किया (फाह्यान चंद्रगुप्त द्वितीय के समय आए; ह्वेनसांग हर्ष के समय आए)।"
)
add_stmt(sec4_en, sec4_hi,
    "With reference to the 'Periplus of the Erythraean Sea', which of the following statements are correct?\n1. It was written in Greek during the 1st century CE.\n2. It documents trade transactions at ports like Arikamedu.\n3. It lists the names of Indian rulers of the Kushan and Satavahana dynasties.\nSelect the correct answer using the code given below:",
    "'पेरिप्लस ऑफ द एरीथ्रियन सी' के संदर्भ में, निम्नलिखित में से कौन से कथन सही हैं?\n1. यह पहली शताब्दी ईस्वी के दौरान यूनानी भाषा में लिखा गया था।\n2. यह अरिकामेडु जैसे बंदरगाहों पर व्यापारिक लेनदेन का दस्तावेजीकरण करता है।\n3. यह कुषाण और सातवाहन राजवंशों के भारतीय शासकों के नामों को सूचीबद्ध करता है।\nनीचे दिए गए कोड का उपयोग करके सही उत्तर चुनें:",
    ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
    ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
    0,
    "Statements 1 and 2 are correct. The Periplus contains trade names and geographical guides, but it does not list dynastic king lists or histories.",
    "कथन 1 और 2 सही हैं। पेरिप्लस में व्यापारिक नाम और भौगोलिक गाइड हैं, लेकिन यह राजवंशों के राजाओं की सूची या इतिहास नहीं देता है।"
)
add_stmt(sec4_en, sec4_hi,
    "Regarding Al-Biruni's Kitab-ul-Hind, consider the following statements:\n1. It was written in Arabic.\n2. It analyzes the caste system, comparing it with Persian classes.\n3. It praises Mahmud of Ghazni's military destruction of Hindu temples.\nWhich of the statements given above is/are correct?",
    "अल-बिरूनी की किताब-उल-हिंद के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. यह अरिक भाषा में लिखी गई थी।\n2. यह फारसी वर्गों के साथ तुलना करते हुए जाति व्यवस्था का विश्लेषण करती है।\n3. यह हिंदू मंदिरों के महमूद गजनवी द्वारा किए गए विनाश की प्रशंसा करती है।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 and 2 only", "3 only", "2 and 3 only", "1, 2 and 3"],
    ["केवल 1 और 2", "केवल 3", "केवल 2 और 3", "1, 2 और 3"],
    0,
    "Statements 1 and 2 are correct. Al-Biruni did not praise Mahmud's temple destructions; he noted that they caused deep resentment and ruined Indian science academies.",
    "कथन 1 और 2 सही हैं। अल-बिरूनी ने महमूद द्वारा मंदिरों के विनाश की प्रशंसा नहीं की; उन्होंने उल्लेख किया कि इससे गहरा असंतोष पैदा हुआ और भारतीय विज्ञान अकादमियाँ नष्ट हो गईं।"
)
add_stmt(sec4_en, sec4_hi,
    "Consider the following statements regarding Roman accounts of Indian trade:\n1. Pliny's Natural History is a primary source for Indo-Roman maritime trade.\n2. Rome imported pepper, pearls, and textiles from South Indian ports.\n3. Roman gold coins were found in large hoards in North India only.\nWhich of the statements given above are correct?",
    "भारतीय व्यापार के रोमन विवरणों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. प्लिनी की नेचुरल हिस्ट्री भारत-रोम समुद्री व्यापार के लिए एक प्राथमिक स्रोत है।\n2. रोम ने दक्षिण भारतीय बंदरगाहों से काली मिर्च, मोती और वस्त्रों का आयात किया।\n3. रोमन सोने के सिक्के केवल उत्तर भारत में बड़े संचय (hoards) में पाए गए।\nऊपर दिए गए कथनों में से कौन से सही हैं?",
    ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
    ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
    0,
    "Statements 1 and 2 are correct. Large Roman gold hoards were found primarily in South India (coinciding with ports and pepper areas), not North India only.",
    "कथन 1 और 2 सही हैं। बड़े रोमन सोने के सिक्कों के संचय मुख्य रूप से दक्षिण भारत (बंदरगाहों और काली मिर्च उत्पादक क्षेत्रों) में पाए गए, न कि केवल उत्तर भारत में।"
)

# 9. Why (3 Qs)
add_open(sec4_en, sec4_hi, "Why",
    "Why is Megasthenes' description of 'no slavery in India' considered incorrect by modern historians?",
    "मेगास्थनीज के 'भारत में कोई दासता नहीं थी' के विवरण को आधुनिक इतिहासकारों द्वारा गलत क्यों माना जाता है?",
    "Megasthenes compared Indian society with Greece, where slaves had no legal rights and were treated as chattel. In India, domestic servants and debt-bonded laborers (dasas) had legal protections under texts like Arthashastra. Because they were not treated as brutally as Greek slaves, Megasthenes failed to recognize them as enslaved.",
    "मेगास्थनीज ने भारतीय समाज की तुलना यूनान से की, जहाँ दासों के पास कोई कानूनी अधिकार नहीं थे और उन्हें संपत्ति की तरह माना जाता था। भारत में, घरेलू सेवकों और ऋण-बंधित श्रमिकों (दासों) को अर्थशास्त्र जैसे ग्रंथों के तहत कानूनी सुरक्षा प्राप्त थी। क्योंकि उनके साथ यूनानी दासों जैसा क्रूर व्यवहार नहीं किया जाता था, इसलिए मेगास्थनीज उन्हें दास के रूप में पहचानने में विफल रहे।"
)
add_open(sec4_en, sec4_hi, "Why",
    "Why are the accounts of Chinese pilgrims Fa-Hien and Hiuen Tsang considered chronologically reliable?",
    "चीनी तीर्थयात्री फाह्यान और ह्वेनसांग के विवरणों को कालानुक्रमिक रूप से विश्वसनीय क्यों माना जाता है?",
    "Chinese pilgrims recorded their journeys with precise dates linked to Chinese imperial calendars. Because China kept continuous, structured historic records, matching their arrival dates to Indian reigns provides absolute, verified dates for rulers like Chandragupta II and Harsha.",
    "चीनी तीर्थयात्रियों ने अपनी यात्राओं को चीनी शाही कैलेंडरों से जुड़ी सटीक तिथियों के साथ दर्ज किया। क्योंकि चीन के पास निरंतर, संरचित ऐतिहासिक रिकॉर्ड थे, इसलिए उनके आगमन की तिथियों का भारतीय राजाओं के शासनकाल से मिलान करने पर चंद्रगुप्त द्वितीय और हर्ष जैसे शासकों के लिए सटीक तिथियां प्राप्त होती हैं।"
)
add_open(sec4_en, sec4_hi, "Why",
    "Why did Pliny the Elder criticize the Roman import of Indian luxuries?",
    "प्लिनी द एल्डर ने भारतीय विलासिता की वस्तुओं के रोमन आयात की आलोचना क्यों की थी?",
    "Pliny lamented the economic drain. Roman citizens bought luxury Indian goods like pepper, silk, and gems, paying in gold and silver coins. Pliny calculated that Rome lost millions of sesterces annually to India, weakening the Roman treasury to feed elite vanity.",
    "प्लिनी ने आर्थिक नुकसान पर खेद व्यक्त किया था। रोमन नागरिक काली मिर्च, रेशम और रत्नों जैसी विलासिता की भारतीय वस्तुएं खरीदते थे, जिसका भुगतान वे सोने और चांदी के सिक्कों में करते थे। प्लिनी ने गणना की कि रोम ने कुलीन वर्ग के घमंड को संतुष्ट करने के लिए सालाना लाखों सेस्टरस भारत को गंवा दिए, जिससे रोमन खजाना कमजोर हो गया।"
)

# 10. How (3 Qs)
add_open(sec4_en, sec4_hi, "How",
    "How do foreign accounts serve as chronological anchors for Indian history?",
    "विदेशी विवरण भारतीय इतिहास के लिए कालानुक्रमिक एंकर के रूप में कैसे कार्य करते हैं?",
    "Many ancient Indian texts lack dates or dynastic lists. Foreign visitors record encounters with specific kings whose dates are known in their home empires (e.g. Megasthenes meeting 'Sandrokottos' / Chandragupta Maurya). By matching these external names and dates, historians anchor local dynasties to absolute calendars.",
    "कई प्राचीन भारतीय ग्रंथों में तिथियों या राजवंशों की सूची का अभाव है। विदेशी आगंतुक उन राजाओं के साथ मुलाकातों को दर्ज करते हैं जिनकी तिथियां उनके गृह साम्राज्यों में ज्ञात होती हैं (जैसे मेगास्थनीज की 'सैंड्रोकोट्टोस' / चंद्रगुप्त मौर्य से मुलाकात)। इन बाहरी नामों और तिथियों का मिलान करके, इतिहासकार स्थानीय राजवंशों को निरपेक्ष कैलेंडरों से जोड़ते हैं।"
)
add_open(sec4_en, sec4_hi, "How",
    "How did Al-Biruni bypass local language barriers to write the Kitab-ul-Hind?",
    "अल-बिरूनी ने किताब-उल-हिंद लिखने के लिए स्थानीय भाषा की बाधाओं को कैसे पार किया?",
    "Al-Biruni spent several years in northwestern India studying Sanskrit under local Brahmin scholars. He translated Sanskrit texts into Arabic and mastered local dialects, enabling him to read primary manuscripts on astronomy, math, and philosophy directly.",
    "अल-बिरूनी ने स्थानीय ब्राह्मण विद्वानों के अधीन संस्कृत का अध्ययन करने में उत्तर-पश्चिमी भारत में कई वर्ष बिताए। उन्होंने संस्कृत ग्रंथों का अरबी में अनुवाद किया और स्थानीय बोलियों पर महारत हासिल की, जिससे वे खगोल विज्ञान, गणित और दर्शन पर मूल पांडुलिपियों को सीधे पढ़ने में सक्षम हुए।"
)
add_open(sec4_en, sec4_hi, "How",
    "How does the 'Periplus of the Erythraean Sea' help reconstruct the maritime geography of India?",
    "पेरिप्लस ऑफ द एरीथ्रियन सी' भारत के समुद्री भूगोल के पुनर्निर्माण में कैसे मदद करता है?",
    "The Periplus acts as a coastal navigation log, listing ports from Karachi to Bengal in geographical order. It details wind directions, navigation hazards, local rulers, and the specific items bought and sold at each port, allowing historians to map the trade map of c. 1st century CE.",
    "पेरिप्लस एक तटीय नेविगेशन लॉग के रूप में कार्य करता है, जो कराची से बंगाल तक के बंदरगाहों को भौगोलिक क्रम में सूचीबद्ध करता है। यह हवा की दिशाओं, नौवहन के खतरों, स्थानीय शासकों और प्रत्येक बंदरगाह पर खरीदी और बेची जाने वाली विशिष्ट वस्तुओं का विवरण देता है, जिससे इतिहासकार पहली शताब्दी ईस्वी के व्यापारिक मानचित्र का पुनर्निर्माण कर पाते हैं।"
)

# 11. Case Study (3 Qs)
add_open(sec4_en, sec4_hi, "Case Study",
    "A historian reads a text claiming that in c. 300 BCE, Indian cities were built exclusively of polished stone and marble, similar to Rome. The text is attributed to Megasthenes. Verify this using archaeological findings.",
    "एक इतिहासकार एक पाठ पढ़ता है जिसमें दावा किया गया है कि लगभग 300 ईसा पूर्व में, भारतीय शहर पूरी तरह से पॉलिश किए गए पत्थर और संगमरमर से बने थे, ठीक रोम की तरह। यह पाठ मेगास्थनीज का बताया जाता है। पुरातात्विक खोजों का उपयोग करके इसकी पुष्टि करें।",
    "The claim is incorrect. Excavations of Mauryan Pataliputra (like Kumrahar) show that buildings and city walls were constructed primarily of wood and clay brick, not stone or marble. Stone was introduced for pillars and art only under Ashoka. Megasthenes' original lost descriptions actually noted wooden fortifications, which fits the archaeology.",
    "यह दावा गलत है। मौर्यकालीन पाटलिपुत्र (जैसे कुम्रहार) के उत्खनन से पता चलता है कि इमारतें और शहर की दीवारें मुख्य रूप से लकड़ी और मिट्टी की ईंटों से बनी थीं, न कि पत्थर या संगमरमर से। स्तंभों और कला के लिए पत्थर की शुरुआत केवल अशोक के अधीन हुई थी। मेगास्थनीज के मूल खोए हुए विवरणों में वास्तव में लकड़ी की किलेबंदी का उल्लेख था, जो पुरातत्व के अनुकूल है।"
)
add_open(sec4_en, sec4_hi, "Case Study",
    "An excavation of a Buddhist site in North India uncovers a Chinese copper coin alongside a set of silk banners bearing Chinese writing. Reconstruct the historical context using Chinese pilgrim accounts.",
    "उत्तर भारत में एक बौद्ध स्थल के उत्खनन से चीनी लेखन वाले रेशम के बैनरों के साथ एक चीनी तांबे का सिक्का मिलता है। चीनी तीर्थयात्रियों के विवरण का उपयोग करके ऐतिहासिक संदर्भ का पुनर्निर्माण करें।",
    "This find represents pilgrim activity (like Fa-Hien or Hiuen Tsang). Chinese pilgrims traveled to Buddhist holy sites in India, carrying Chinese coins as offerings or souvenirs, alongside silk banners to dedicate to monasteries. It proves active religious and intellectual traffic between China and India.",
    "यह खोज चीनी तीर्थयात्रियों (जैसे फाह्यान या ह्वेनसांग) की गतिविधियों को दर्शाती है। चीनी तीर्थयात्री भारत में बौद्ध पवित्र स्थलों की यात्रा करते थे, चीनी सिक्कों को चढ़ावे या स्मृति चिन्ह के रूप में लाते थे, साथ ही मठों को समर्पित करने के लिए रेशमी बैनर भी लाते थे। यह चीन और भारत के बीच सक्रिय धार्मिक और बौद्धिक आवागमन को सिद्ध करता है।"
)
add_open(sec4_en, sec4_hi, "Case Study",
    "A researcher reads an 11th-century Arabic text describing the division of Indian society into multiple occupational castes who do not intermarry. Cross-check this with Al-Biruni's observations.",
    "एक शोधकर्ता 11वीं शताब्दी के अरबी पाठ को पढ़ता है जिसमें भारतीय समाज के कई व्यावसायिक जातियों में विभाजन का वर्णन है जो आपस में विवाह नहीं करते हैं। अल-बिरूनी के अवलोकनों के साथ इसका मिलान करें।",
    "This matches Al-Biruni's Kitab-ul-Hind. He documented the rigid structure of the Hindu caste system (chaturvarnya) and the existence of outcaste groups (Antyajas), noting rules against intermarriage, shared dining, and the strict hereditary transmission of crafts.",
    "यह अल-बिरूनी की किताब-उल-हिंद से मेल खाता है। उन्होंने हिंदू जाति व्यवस्था (चातुर्वर्ण्य) की कठोर संरचना और अछूत समूहों (अंत्यजों) के अस्तित्व का दस्तावेजीकरण किया, जिसमें अंतर्विवाह, साझा भोजन और शिल्पों के कड़े आनुवंशिक हस्तांतरण के खिलाफ नियमों का उल्लेख था।"
)

# 12. Teach the Concept (3 Qs)
add_open(sec4_en, sec4_hi, "Teach the Concept",
    "Explain the concept of 'historical chronologue anchoring' to a student. Use the example of Megasthenes and Chandragupta Maurya.",
    "एक छात्र को 'ऐतिहासिक कालक्रम एंकरिंग' की अवधारणा समझाएं। मेगास्थनीज और चंद्रगुप्त मौर्य का उदाहरण दें।",
    "Imagine trying to build a puzzle with no picture. Anchor dating is finding a puzzle piece that links to a known map. Indian sources name Chandragupta Maurya but provide conflicting timelines. Megasthenes was sent by Seleucus I Nicator, whose reign is precisely dated in Greek history. Matching Megasthenes' visit anchors Chandragupta's reign to c. 322–298 BCE.",
    "बिना चित्र के एक पहेली (puzzle) बनाने की कल्पना करें। एंकर तिथि निर्धारण एक ऐसे टुकड़े को खोजना है जो एक ज्ञात मानचित्र से जुड़ता है। भारतीय स्रोत चंद्रगुप्त मौर्य का नाम तो देते हैं लेकिन विरोधाभासी समयसीमा प्रदान करते हैं। मेगास्थनीज को सेल्यूकस प्रथम निकेटर द्वारा भेजा गया था, जिनका शासनकाल ग्रीक इतिहास में सटीक रूप से निर्धारित है। मेगास्थनीज की यात्रा का मिलान चंद्रगुप्त के शासनकाल को लगभग 322-298 ईसा पूर्व पर एंकर करता है।"
)
add_open(sec4_en, sec4_hi, "Teach the Concept",
    "How would you explain the value of Pliny's Natural History to a student? Create a simple economic visualization.",
    "आप किसी छात्र को प्लिनी की नेचुरल हिस्ट्री का महत्व कैसे समझाएंगे? एक सरल आर्थिक चित्रण बनाएं।",
    "Think of a giant scale: on one side is Roman gold coins, on the other side is Indian black pepper, silk, and spices. Pliny's text shows this scale tipping heavily in India's favor. It represents a trade surplus for India and a massive cash drain for Rome, serving as the earliest evidence of global mercantilism.",
    "एक विशाल तराजू की कल्पना करें: एक तरफ रोमन सोने के सिक्के हैं, दूसरी तरफ भारतीय काली मिर्च, रेशम और मसाले हैं। प्लिनी का पाठ दिखाता है कि यह तराजू भारत के पक्ष में भारी रूप से झुक रहा था। यह भारत के लिए व्यापार अधिशेष (trade surplus) और रोम के लिए भारी नकदी नुकसान का प्रतिनिधित्व करता है, जो वैश्विक व्यापारवाद का सबसे पहला साक्ष्य है।"
)
add_open(sec4_en, sec4_hi, "Teach the Concept",
    "Explain the difference in focus between the memoirs of Fa-Hien and Hiuen Tsang.",
    "फाह्यान और ह्वेनसांग के संस्मरणों के बीच ध्यान (focus) के अंतर को समझाइए।",
    "1. **Fa-Hien**: Focused purely on Buddhist monastic rules (Vinaya) and pilgrimage. He paid little attention to secular politics and did not even name the reigning Gupta king.\n2. **Hiuen Tsang**: Had a broader interest, recording detailed observations of Harsha's administration, the university of Nalanda, local geography, and social classes, offering a rich secular and religious description.",
    "1. **फाह्यान**: उनका ध्यान विशुद्ध रूप से बौद्ध मठवासी नियमों (विनय) और तीर्थयात्रा पर था। उन्होंने धर्मनिरपेक्ष राजनीति पर बहुत कम ध्यान दिया और यहाँ तक कि तत्कालीन गुप्त राजा का नाम भी नहीं लिखा।\n2. **ह्वेनसांग**: उनकी व्यापक रुचि थी, उन्होंने हर्ष के प्रशासन, नालंदा विश्वविद्यालय, स्थानीय भूगोल और सामाजिक वर्गों के विस्तृत विवरणों को रिकॉर्ड किया, जिससे एक समृद्ध धर्मनिरपेक्ष और धार्मिक विवरण मिलता है।"
)

# ==========================================
# SECTION 5: SCIENTIFIC DATING & PALAEO-ENVIRONMENT
# ==========================================

# 1. MCQ (5 Qs)
add_mcq(sec5_en, sec5_hi,
    "Which radioactive isotope is measured in organic materials to establish dates up to approximately 50,000 years ago?",
    "लगभग 50,000 वर्ष पूर्व तक की तिथियाँ स्थापित करने के लिए जैविक सामग्रियों में किस रेडियोधर्मी समस्थानिक (isotope) को मापा जाता है?",
    ["Uranium-235", "Carbon-14", "Potassium-40", "Argon-39"],
    ["यूरेनियम-235", "कार्बन-14 (Carbon-14)", "पोटेशियम-40", "आर्गन-39"],
    1,
    "Radiocarbon (¹⁴C) dating measures the decay of carbon-14 in organic materials, with a half-life of c. 5,730 years, effective up to 50,000 years.",
    "रेडियोकार्बन (¹⁴C) तिथि निर्धारण जैविक सामग्रियों में कार्बन-14 के क्षय को मापता है, जिसकी अर्ध-आयु लगभग 5,730 वर्ष होती है और यह 50,000 वर्ष तक प्रभावी होता है।"
)
add_mcq(sec5_en, sec5_hi,
    "Which dating method measures the light emitted when crystalline minerals are heated to determine the time since they were last fired?",
    "कौन सी तिथि निर्धारण विधि क्रिस्टलीय खनिजों को गर्म करने पर उत्सर्जित प्रकाश को मापती है ताकि यह निर्धारित किया जा सके कि उन्हें अंतिम बार कब पकाया गया था?",
    ["Potassium-Argon", "Thermoluminescence (TL)", "Dendrochronology", "Stratigraphy"],
    ["पोटेशियम-आर्गन", "थर्मोलुमिनेसेंस (TL)", "वृक्षवलय कालानुक्रम", "स्तरविन्यास"],
    1,
    "Thermoluminescence (TL) is used to date pottery and burnt clay by measuring the trapped electrons released as light when heated.",
    "थर्मोलुमिनेसेंस (TL) का उपयोग मिट्टी के बर्तनों और पकी मिट्टी को गर्म करने पर प्रकाश के रूप में निकलने वाले फंसे हुए इलेक्ट्रॉनों को मापकर उनकी तिथि निर्धारित करने के लिए किया जाता है।"
)
add_mcq(sec5_en, sec5_hi,
    "Which absolute dating technique is ideal for establishing the chronology of volcanic rock layers older than 100,000 years?",
    "100,000 वर्ष से अधिक पुरानी ज्वालामुखी चट्टान की परतों के कालक्रम को स्थापित करने के लिए कौन सी निरपेक्ष तिथि निर्धारण तकनीक आदर्श है?",
    ["Radiocarbon Dating", "Potassium-Argon (K-Ar) Dating", "Dendrochronology", "Palynology"],
    ["रेडियोकार्बन डेटिंग", "पोटेशियम-आर्गन (K-Ar) डेटिंग", "वृक्षवलय कालानुक्रम", "परागकण विश्लेषण"],
    1,
    "Potassium-Argon dating measures the decay of potassium-40 into argon-40 in volcanic minerals, ideal for early hominin dating (e.g. volcanic beds).",
    "पोटेशियम-आर्गन डेटिंग ज्वालामुखी खनिजों में पोटेशियम-40 के आर्गन-40 में क्षय को मापती है, जो प्रारंभिक मानव जीवाश्मों की तिथि निर्धारण के लिए आदर्श है।"
)
add_mcq(sec5_en, sec5_hi,
    "The scientific study of fossil pollen grains to reconstruct ancient climate shifts, vegetation, and monsoonal rainfall is called:",
    "प्राचीन जलवायु परिवर्तनों, वनस्पति और मानसूनी वर्षा के पुनर्निर्माण के लिए जीवाश्म परागकणों के वैज्ञानिक अध्ययन को क्या कहा जाता है?",
    ["Palaeozoology", "Palynology", "Palaeobotany", "Dendrochronology"],
    ["पुरा-प्राणीशास्त्र", "परागकण विश्लेषण (Palynology)", "पुरा-वनस्पतिशास्त्र", "वृक्षवलय कालानुक्रम"],
    1,
    "Palynology is the study of pollen grains and spores extracted from soil cores, lake sediments, or peat beds to track environmental changes.",
    "परागकण विश्लेषण (Palynology) मिट्टी के कोर, झील के तलछटों या पीट बेड से निकाले गए परागकणों और बीजाणुओं का अध्ययन है ताकि पर्यावरणीय बदलावों को ट्रैक किया जा सके।"
)
add_mcq(sec5_en, sec5_hi,
    "Optically Stimulated Luminescence (OSL) dating is primarily used to determine:",
    "ऑप्टिकली स्टिमुलेटेड ल्यूमिनसेंस (OSL) डेटिंग का उपयोग मुख्य रूप से क्या निर्धारित करने के लिए किया जाता है?",
    ["The age of organic bones", "The last time sediment/sand was exposed to sunlight", "The tree-ring growth cycles", "The iron composition of coins"],
    ["जैविक हड्डियों की आयु", "तलछट/रेत आखिरी बार कब सूर्य के प्रकाश के संपर्क में आई थी", "वृक्ष के छल्लों के विकास चक्र", "सिक्कों की लौह संरचना"],
    1,
    "OSL dates the last time quartz or feldspar grains were exposed to sunlight prior to burial. It was used to date Attirampakkam tool sediments.",
    "OSL यह मापता है कि दफनाने से पहले क्वार्ट्ज या फेल्डस्पार कण आखिरी बार सूर्य के प्रकाश के संपर्क में कब आए थे। इसका उपयोग अतिरम्पक्कम उपकरण तलछट की तिथि निर्धारण के लिए किया गया था।"
)

# 2. Multiple Correct MCQ (5 Qs)
add_multi_mcq(sec5_en, sec5_hi,
    "Which of the following are classified as absolute dating methods? (Select all that apply)",
    "निम्नलिखित में से किन्हें निरपेक्ष तिथि निर्धारण (absolute dating) विधियों के रूप में वर्गीकृत किया गया है? (सभी लागू विकल्प चुनें)",
    ["Radiocarbon (C-14) dating", "Stratigraphy", "Thermoluminescence (TL)", "Seriation"],
    ["रेडियोकार्बन (C-14) डेटिंग", "स्तरविन्यास", "थर्मोलुमिनेसेंस (TL)", "श्रेणीकरण"],
    [0, 2],
    "Radiocarbon and Thermoluminescence are absolute methods. Stratigraphy and seriation are relative dating methods.",
    "रेडियोकार्बन और थर्मोलुमिनेसेंस निरपेक्ष विधियाँ हैं। स्तरविन्यास और श्रेणीकरण सापेक्ष तिथि निर्धारण विधियाँ हैं।"
)
add_multi_mcq(sec5_en, sec5_hi,
    "Which of the following materials can be dated using Radiocarbon (C-14) dating? (Select all that apply)",
    "निम्नलिखित में से किन सामग्रियों की तिथि रेडियोकार्बन (C-14) डेटिंग का उपयोग करके निर्धारित की जा सकती है? (सभी लागू विकल्प चुनें)",
    ["Charred grain", "Animal bone", "Quartzite handaxe", "Wood charcoal"],
    ["जला हुआ अनाज", "जानवर की हड्डी", "क्वार्टजाइट हस्त-कुठार", "लकड़ी का कोयला"],
    [0, 1, 3],
    "C-14 can only date organic carbon-bearing materials (charcoal, bone, grain). Stone handaxes contain no organic carbon.",
    "C-14 केवल जैविक कार्बन युक्त सामग्रियों (कोयला, हड्डी, अनाज) की तिथि निर्धारित कर सकता है। पत्थर के हस्त-कुठार में कोई जैविक कार्बन नहीं होता है।"
)
add_multi_mcq(sec5_en, sec5_hi,
    "Which of the following studies are branch disciplines of Palaeo-environmental reconstruction? (Select all that apply)",
    "निम्नलिखित में से कौन से अध्ययन पुरा-पर्यावरण पुनर्निर्माण की शाखाएँ हैं? (सभी लागू विकल्प चुनें)",
    ["Palynology (pollen studies)", "Palaeozoology (animal remains)", "Palaeobotany (plant remains)", "Epigraphy (inscriptions)"],
    ["परागकण विश्लेषण (Palynology)", "पुरा-प्राणीशास्त्र (Palaeozoology)", "पुरा-वनस्पतिशास्त्र (Palaeobotany)", "पुरालेखशास्त्र (Epigraphy)"],
    [0, 1, 2],
    "Palynology, Palaeozoology, and Palaeobotany are environmental/scientific fields. Epigraphy is a historical/linguistic discipline.",
    "परागकण विश्लेषण, पुरा-प्राणीशास्त्र और पुरा-वनस्पतिशास्त्र पर्यावरणीय/वैज्ञानिक क्षेत्र हैं। पुरालेखशास्त्र एक ऐतिहासिक/भाषाई विषय है।"
)
add_multi_mcq(sec5_en, sec5_hi,
    "Which of the following conditions can affect the accuracy of Radiocarbon (¹⁴C) dating? (Select all that apply)",
    "निम्नलिखित में से कौन सी परिस्थितियाँ रेडियोकार्बन (¹⁴C) डेटिंग की सटीकता को प्रभावित कर सकती हैं? (सभी लागू विकल्प चुनें)",
    ["Sample contamination with modern organic carbon", "Fluctuations in atmospheric ¹⁴C levels over millennia", "The weight of the surrounding stone layers", "The temperature of the kiln during firing"],
    ["आधुनिक जैविक कार्बन के साथ नमूना संदूषण (contamination)", "सहस्राब्दियों से वायुमंडलीय ¹⁴C स्तरों में उतार-चढ़ाव", "आसपास की पत्थर की परतों का वजन", "पकाने के दौरान भट्टी का तापमान"],
    [0, 1],
    "Contamination and atmospheric ¹⁴C fluctuations affect carbon dating. Calibration curves are used to adjust for fluctuations. Stone weight and firing temperatures do not affect ¹⁴C decay rates.",
    "संदूषण और वायुमंडलीय ¹⁴C के उतार-चढ़ाव कार्बन डेटिंग को प्रभावित करते हैं। इन बदलावों को समायोजित करने के लिए कैलिब्रेशन वक्रों का उपयोग किया जाता है। पत्थर का वजन और पकाने का तापमान ¹⁴C क्षय दर को प्रभावित नहीं करते हैं।"
)
add_multi_mcq(sec5_en, sec5_hi,
    "Which of the following sites in India have yielded early domestic crop botanical evidence validated by scientific floatation? (Select all that apply)",
    "भारत में निम्नलिखित में से किन स्थलों से वैज्ञानिक फ्लोटेशन (floatation) द्वारा सत्यापित प्रारंभिक घरेलू फसलों के वानस्पतिक साक्ष्य मिले हैं? (सभी लागू विकल्प चुनें)",
    ["Lahuradewa (Rice)", "Koldihwa (Rice)", "Mehrgarh (Wheat/Barley)", "Attirampakkam (Maize)"],
    ["लहुरादेवा (धान)", "कोलडिहवा (धान)", "मेहरगढ़ (गेहूं/जौ)", "अतिरम्पक्कम (मक्का)"],
    [0, 1, 2],
    "Lahuradewa, Koldihwa, and Mehrgarh yielded crops validated by botany. Attirampakkam is a Paleolithic site with no domestic crop records.",
    "लहुरादेवा, कोलडिहवा और मेहरगढ़ से वनस्पति विज्ञान द्वारा सत्यापित फसलों के साक्ष्य मिले हैं। अतिरम्पक्कम एक पुरापाषाण कालीन स्थल है जहाँ घरेलू फसलों का कोई रिकॉर्ड नहीं है।"
)

# 3. True/False (8 Qs)
add_tf(sec5_en, sec5_hi,
    "Dendrochronology is the study of tree-growth rings to establish absolute calendar dates.",
    "वृक्षवलय कालानुक्रम (Dendrochronology) निरपेक्ष कैलेंडर तिथियां स्थापित करने के लिए वृक्षों के छल्लों के विकास का अध्ययन है।",
    True,
    "Each year, trees produce a growth ring. Counting and matching ring patterns allows absolute dating of wood artifacts.",
    "हर साल, पेड़ एक विकास छल्ला (ring) बनाते हैं। छल्लों के पैटर्न की गिनती और मिलान करने से लकड़ी की कलाकृतियों की निरपेक्ष तिथि ज्ञात होती है।"
)
add_tf(sec5_en, sec5_hi,
    "Carbon-14 has an infinite half-life, making it suitable for dating dinosaur fossils millions of years old.",
    "कार्बन-14 की अर्ध-आयु अनंत होती है, जिससे यह लाखों साल पुराने डायनासोर के जीवाश्मों की तिथि निर्धारण के लिए उपयुक्त है।",
    False,
    "Carbon-14 has a half-life of c. 5,730 years and decays completely after ~50,000 years, making it useless for dinosaur fossils (which require K-Ar or Uranium dating).",
    "कार्बन-14 की अर्ध-आयु लगभग 5,730 वर्ष होती है और यह ~50,000 वर्षों के बाद पूरी तरह से क्षय हो जाता है, जिससे यह डायनासोर के जीवाश्मों के लिए अनुपयुक्त है।"
)
add_tf(sec5_en, sec5_hi,
    "Thermoluminescence (TL) dating measures the time that has elapsed since a pottery vessel was fired.",
    "थर्मोलुमिनेसेंस (TL) डेटिंग उस समय को मापती है जो मिट्टी के बर्तन को पकाने के बाद से बीत चुका है।",
    True,
    "TL measures the accumulated trapped electrons in minerals since the last heating event (kiln firing), which resets the clock to zero.",
    "TL अंतिम तापन घटना (भट्टी में पकाना) के बाद से खनिजों में संचित फंसे हुए इलेक्ट्रॉनों को मापता है, जो घड़ी को शून्य पर सेट कर देता है।"
)
add_tf(sec5_en, sec5_hi,
    "Palynology allows archaeologists to reconstruct ancient vegetation and monsoon cycles.",
    "परागकण विश्लेषण (Palynology) पुरातत्वविदों को प्राचीन वनस्पति और मानसून चक्रों के पुनर्निर्माण की अनुमति देता है।",
    True,
    "Fossil pollen grains are highly resistant to decay and reflect the species of plants growing in the region, indicating wet or dry climates.",
    "जीवाश्म परागकण क्षय के प्रति अत्यधिक प्रतिरोधी होते हैं और क्षेत्र में उगने वाले पौधों की प्रजातियों को दर्शाते हैं, जो गीली या शुष्क जलवायु का संकेत देते हैं।"
)
add_tf(sec5_en, sec5_hi,
    "Potassium-Argon dating is a relative dating method based on the sequence of soil layers.",
    "पोटेशियम-आर्गन डेटिंग मिट्टी की परतों के अनुक्रम पर आधारित एक सापेक्ष तिथि निर्धारण विधि है।",
    False,
    "Potassium-Argon dating is an absolute scientific dating method based on the radioactive decay of Potassium-40.",
    "पोटेशियम-आर्गन डेटिंग पोटेशियम-40 के रेडियोधर्मी क्षय पर आधारित एक निरपेक्ष वैज्ञानिक तिथि निर्धारण विधि है।"
)
add_tf(sec5_en, sec5_hi,
    "OSL dating determines the last time quartz sand was exposed to heat in a pottery kiln.",
    "OSL डेटिंग यह निर्धारित करती है कि क्वार्ट्ज रेत आखिरी बार मिट्टी के बर्तन पकाने वाली भट्टी में कब गर्मी के संपर्क में आई थी।",
    False,
    "OSL measures the last exposure to sunlight (burial date), whereas TL measures the last exposure to heat (firing date).",
    "OSL सूर्य के प्रकाश के अंतिम संपर्क (दफन की तिथि) को मापता है, जबकि TL गर्मी के अंतिम संपर्क (पकाने की तिथि) को मापता है।"
)
add_tf(sec5_en, sec5_hi,
    "The law of superposition states that soil layers are deposited horizontally, and the oldest layer is at the bottom.",
    "अध्यारोपण का नियम बताता है कि मिट्टी की परतें क्षैतिज रूप से जमा होती हैं, और सबसे पुरानी परत सबसे नीचे होती है।",
    True,
    "This is the foundation of stratigraphical relative dating.",
    "यह स्तरविन्यास सापेक्ष तिथि निर्धारण का आधार है।"
)
add_tf(sec5_en, sec5_hi,
    "Floatation is a technique used to recover microscopic plant remains and charred seeds from excavated soil.",
    "फ्लोटेशन (Floatation) उत्खनन की गई मिट्टी से सूक्ष्म पौधों के अवशेषों और जले हुए बीजों को प्राप्त करने के लिए उपयोग की जाने वाली तकनीक है।",
    True,
    "Soil is mixed with water; the organic seeds float to the surface (light fraction) and are collected for botanical analysis.",
    "मिट्टी को पानी के साथ मिलाया जाता है; जैविक बीज सतह पर तैरते हैं (हल्का अंश) और वानस्पतिक विश्लेषण के लिए एकत्र किए जाते हैं।"
)

# 4. Fill in the Blank (8 Qs)
add_blank(sec5_en, sec5_hi,
    "The scientist who discovered the Radiocarbon (C-14) dating method was ________.",
    "रेडियोकार्बन (C-14) डेटिंग पद्धति की खोज करने वाले वैज्ञानिक ________ थे।",
    "Willard Libby", "विलार्ड लिब्बी",
    "Willard Libby won the Nobel Prize in Chemistry in 1960 for developing C-14 dating.",
    "विलार्ड लिब्बी को C-14 डेटिंग विकसित करने के लिए 1960 में रसायन विज्ञान में नोबेल पुरस्कार मिला था।"
)
add_blank(sec5_en, sec5_hi,
    "Thermoluminescence (TL) dating resets its clock to zero when the mineral is exposed to ________.",
    "थर्मोलुमिनेसेंस (TL) डेटिंग खनिज के ________ के संपर्क में आने पर अपनी घड़ी को शून्य पर रीसेट करती है।",
    "heat", "गर्मी",
    "TL clocks are reset to zero by heating (firing), which releases all previously trapped electrons.",
    "टीएल घड़ियाँ गर्म करने (पकाने) से शून्य पर रीसेट हो जाती हैं, जिससे पहले से फंसे सभी इलेक्ट्रॉन निकल जाते हैं।"
)
add_blank(sec5_en, sec5_hi,
    "The dating method that relies on counting annual growth rings of trees is called ________.",
    "पेड़ों के वार्षिक विकास छल्लों को गिनने पर आधारित तिथि निर्धारण विधि को ________ कहा जाता है।",
    "Dendrochronology", "वृक्षवलय कालानुक्रम",
    "Dendrochronology is also used to calibrate radiocarbon dates.",
    "रेडियोकार्बन तिथियों को कैलिब्रेट करने के लिए भी वृक्षवलय कालानुक्रम का उपयोग किया जाता है।"
)
add_blank(sec5_en, sec5_hi,
    "Palynology is the scientific study of fossil ________ extracted from soil layers.",
    "परागकण विश्लेषण (Palynology) मिट्टी की परतों से निकाले गए जीवाश्म ________ का वैज्ञानिक अध्ययन है।",
    "pollen", "परागकणों",
    "Fossil pollen grains are used to reconstruct paleo-environments.",
    "जीवाश्म परागकणों का उपयोग पुरा-पर्यावरण के पुनर्निर्माण के लिए किया जाता है।"
)
add_blank(sec5_en, sec5_hi,
    "Potassium-40 decays into the stable gas ________, which is measured in volcanic rocks.",
    "पोटेशियम-40 स्थिर गैस ________ में क्षय हो जाता है, जिसे ज्वालामुखी चट्टानों में मापा जाता है।",
    "Argon", "आर्गन",
    "Potassium-Argon (K-Ar) dating measures the accumulation of Argon-40 gas.",
    "पोटेशियम-आर्गन (K-Ar) डेटिंग आर्गन-40 गैस के संचय को मापती है।"
)
add_blank(sec5_en, sec5_hi,
    "OSL dating determines the last time quartz sediment was exposed to ________ before burial.",
    "OSL डेटिंग यह निर्धारित करती है कि दफनाने से पहले क्वार्ट्ज तलछट आखिरी बार कब ________ के संपर्क में आई थी।",
    "sunlight", "सूर्य के प्रकाश",
    "Exposure to sunlight (bleaching) resets the OSL clock to zero.",
    "सूर्य के प्रकाश के संपर्क में आने (bleaching) से OSL घड़ी शून्य पर रीसेट हो जाती है।"
)
add_blank(sec5_en, sec5_hi,
    "The relative dating method that arranges artifacts in a chronological series based on style evolution is ________.",
    "शैली के विकास के आधार पर कलाकृतियों को कालानुक्रमिक श्रृंखला में व्यवस्थित करने वाली सापेक्ष तिथि निर्धारण विधि ________ है।",
    "seriation", "श्रेणीकरण",
    "Seriation arranges assemblages based on stylistic popularity curves.",
    "श्रेणीकरण शैलीगत लोकप्रियता वक्रों के आधार पर संग्रहों को व्यवस्थित करता है।"
)
add_blank(sec5_en, sec5_hi,
    "The technique of using water flow to separate carbonized seeds from soil is called ________.",
    "मिट्टी से कार्बनिक बीजों को अलग करने के लिए पानी के प्रवाह का उपयोग करने की तकनीक को ________ कहा जाता है।",
    "floatation", "फ्लोटेशन",
    "Water floatation is the standard method to recover botanical seeds.",
    "मिट्टी से वानस्पतिक बीजों को प्राप्त करने के लिए वाटर फ्लोटेशन मानक विधि है।"
)

# 5. Match the Following (3 Qs)
add_match(sec5_en, sec5_hi,
    "Match the scientific dating methods with their target materials:",
    "वैज्ञानिक तिथि निर्धारण विधियों को उनकी लक्षित सामग्रियों के साथ सुमेलित करें:",
    [{"left": "Carbon-14", "key": "organic"}, {"left": "Thermoluminescence", "key": "pottery"}, {"left": "Potassium-Argon", "key": "volcanic"}],
    [{"left": "कार्बन-14", "key": "organic"}, {"left": "थर्मोलुमिनेसेंस", "key": "pottery"}, {"left": "पोटेशियम-आर्गन", "key": "volcanic"}],
    [{"val": "organic", "text": "Organic bones and charcoal"}, {"val": "pottery", "text": "Burnt clay and pottery"}, {"val": "volcanic", "text": "Volcanic rocks and ash"}],
    [{"val": "organic", "text": "जैविक हड्डियां और लकड़ी का कोयला"}, {"val": "pottery", "text": "पकी हुई मिट्टी और मिट्टी के बर्तन"}, {"val": "volcanic", "text": "ज्वालामुखी चट्टानें और राख"}],
    "C-14 targets organic materials, TL targets pottery/burnt clay, and K-Ar targets volcanic minerals.",
    "C-14 जैविक सामग्रियों को लक्षित करता है, TL मिट्टी के बर्तनों/पकी मिट्टी को, और K-Ar ज्वालामुखी खनिजों को लक्षित करता है।"
)
add_match(sec5_en, sec5_hi,
    "Match the environmental disciplines with their studied remains:",
    "पर्यावरणीय विषयों को उनके द्वारा अध्ययन किए जाने वाले अवशेषों के साथ सुमेलित करें:",
    [{"left": "Palynology", "key": "pollen"}, {"left": "Palaeozoology", "key": "bones"}, {"left": "Palaeobotany", "key": "seeds"}],
    [{"left": "परागकण विश्लेषण", "key": "pollen"}, {"left": "पुरा-प्राणीशास्त्र", "key": "bones"}, {"left": "पुरा-वनस्पतिशास्त्र", "key": "seeds"}],
    [{"val": "pollen", "text": "Fossil pollen grains"}, {"val": "bones", "text": "Animal skeletal bones"}, {"val": "seeds", "text": "Charred plant seeds"}],
    [{"val": "pollen", "text": "जीवाश्म परागकण"}, {"val": "bones", "text": "जानवरों की हड्डियों के ढांचे"}, {"val": "seeds", "text": "जले हुए पौधों के बीज"}],
    "Palynology studies pollen, Palaeozoology studies bones, and Palaeobotany studies plant seeds.",
    "परागकण विश्लेषण पराग का अध्ययन करता है, पुरा-प्राणीशास्त्र हड्डियों का, और पुरा-वनस्पतिशास्त्र पौधों के बीजों का अध्ययन करता है।"
)
add_match(sec5_en, sec5_hi,
    "Match the dating clocks with their reset actions:",
    "तिथि निर्धारण घड़ियों को उनकी रीसेट क्रियाओं (reset actions) के साथ सुमेलित करें:",
    [{"left": "Radiocarbon clock", "key": "death"}, {"left": "OSL clock", "key": "sunlight"}, {"left": "TL clock", "key": "heating"}],
    [{"left": "रेडियोकार्बन घड़ी", "key": "death"}, {"left": "OSL घड़ी", "key": "sunlight"}, {"left": "TL घड़ी", "key": "heating"}],
    [{"val": "death", "text": "Death of the organic organism"}, {"val": "sunlight", "text": "Last exposure to sunlight"}, {"val": "heating", "text": "Last exposure to high heat"}],
    [{"val": "death", "text": "जैविक जीव की मृत्यु"}, {"val": "sunlight", "text": "सूर्य के प्रकाश से अंतिम संपर्क"}, {"val": "heating", "text": "उच्च गर्मी से अंतिम संपर्क"}],
    "C-14 clock starts at death, OSL resets with sunlight, and TL resets with heat.",
    "C-14 घड़ी मृत्यु पर शुरू होती है, OSL सूर्य के प्रकाश से रीसेट होती है, और TL गर्मी से रीसेट होती है।"
)

# 6. One-Liner (8 Qs)
add_oneliner(sec5_en, sec5_hi,
    "What is the half-life of Carbon-14?",
    "कार्बन-14 की अर्ध-आयु (half-life) क्या है?",
    "Approximately 5,730 years.",
    "लगभग 5,730 वर्ष।"
)
add_oneliner(sec5_en, sec5_hi,
    "Which absolute dating method is used to determine the age of pottery vessels?",
    "मिट्टी के बर्तनों की आयु निर्धारित करने के लिए किस निरपेक्ष तिथि निर्धारण विधि का उपयोग किया जाता है?",
    "Thermoluminescence (TL) dating.",
    "थर्मोलुमिनेसेंस (TL) डेटिंग।"
)
add_oneliner(sec5_en, sec5_hi,
    "What does Palynology study to reconstruct ancient environments?",
    "प्राचीन वातावरण के पुनर्निर्माण के लिए परागकण विश्लेषण (Palynology) किसका अध्ययन करता है?",
    "Fossil pollen grains extracted from geological deposits.",
    "भूवैज्ञानिक निक्षेपों से निकाले गए जीवाश्म परागकणों का।"
)
add_oneliner(sec5_en, sec5_hi,
    "Why can stone tools like quartzite handaxes not be dated using Carbon-14 directly?",
    "क्वार्टजाइट हस्त-कुठार जैसे पत्थर के उपकरणों की तिथि सीधे कार्बन-14 से क्यों नहीं निर्धारित की जा सकती?",
    "Because they do not contain organic carbon; C-14 requires organic matter to measure decay.",
    "क्योंकि वे जैविक कार्बन नहीं रखते हैं; सी-14 को क्षय मापने के लिए जैविक पदार्थ की आवश्यकता होती है।"
)
add_oneliner(sec5_en, sec5_hi,
    "Which dating method is used to establish the age of earliest hominid volcanic layers?",
    "सबसे प्रारंभिक मानव ज्वालामुखी परतों की आयु स्थापित करने के लिए किस तिथि निर्धारण विधि का उपयोग किया जाता है?",
    "Potassium-Argon (K-Ar) dating.",
    "पोटेशियम-आर्गन (K-Ar) डेटिंग।"
)
add_oneliner(sec5_en, sec5_hi,
    "What event resets the OSL dating clock in sand grains?",
    "रेत के कणों में OSL डेटिंग घड़ी को कौन सी घटना शून्य पर रीसेट करती है?",
    "Exposure of the sand grains to direct sunlight.",
    "रेत के कणों का सीधे सूर्य के प्रकाश के संपर्क में आना।"
)
add_oneliner(sec5_en, sec5_hi,
    "How does floatation help palaeobotanists recover ancient seeds?",
    "फ्लोटेशन (Floatation) तकनीक पुरा-वनस्पतिविदों को प्राचीन बीज प्राप्त करने में कैसे मदद करती है?",
    "By mixing soil with water, causing light carbonized seeds to float to the top for easy collection.",
    "मिट्टी को पानी के साथ मिलाकर, जिससे हल्के कार्बनयुक्त बीज आसान संग्रह के लिए ऊपर तैरने लगते हैं।"
)
add_oneliner(sec5_en, sec5_hi,
    "Name a relative dating method based on stylistic popularity curves.",
    "शैलीगत लोकप्रियता वक्रों पर आधारित एक सापेक्ष तिथि निर्धारण विधि का नाम बताइए।",
    "Seriation.",
    "श्रेणीकरण (Seriation)।"
)

# 7. Assertion-Reason (8 Qs)
add_ar(sec5_en, sec5_hi,
    "Assertion (A): Radiocarbon dating is ineffective for materials older than 50,000 years.\nReason (R): The half-life of Carbon-14 is c. 5,730 years, and after 50,000 years, the remaining ¹⁴C quantity becomes too small to measure.",
    "कथन (A): 50,000 वर्ष से अधिक पुरानी सामग्रियों के लिए रेडियोकार्बन डेटिंग अप्रभावी है।\nकारण (R): कार्बन-14 की अर्ध-आयु लगभग 5,730 वर्ष है और 50,000 वर्षों के बाद, शेष ¹⁴C की मात्रा इतनी कम हो जाती है कि उसे मापना असंभव हो जाता है।",
    0,
    "Both A and R are true, and R correctly explains the dating limit of C-14.",
    "A और R दोनों सही हैं और R, C-14 की तिथि निर्धारण सीमा की सही व्याख्या करता है।"
)
add_ar(sec5_en, sec5_hi,
    "Assertion (A): Thermoluminescence (TL) is ideal for dating stone tools made of flint or quartzite.\nReason (R): Stone tools do not release any light when heated, preventing any electron measurement.",
    "कथन (A): थर्मोलुमिनेसेंस (TL) चकमक पत्थर (flint) या क्वार्टजाइट से बने पत्थर के उपकरणों की तिथि निर्धारण के लिए आदर्श है।\nकारण (R): पत्थर के उपकरणों को गर्म करने पर कोई प्रकाश नहीं निकलता है, जिससे इलेक्ट्रॉनों का मापन नहीं हो पाता है।",
    3,
    "A is false but R is true. TL is used for fired pottery and clay, not raw stone tools like handaxes, as stones do not store kiln-reset thermal charges.",
    "A गलत है लेकिन R सही है। TL का उपयोग पके हुए मिट्टी के बर्तनों के लिए किया जाता है, हस्त-कुठार जैसे कच्चे पत्थर के उपकरणों के लिए नहीं।"
)
add_ar(sec5_en, sec5_hi,
    "Assertion (A): Dendrochronology can calibrate radiocarbon dates.\nReason (R): Tree rings record annual calendar growth, allowing scholars to check ¹⁴C levels in wood of verified calendar ages.",
    "कथन (A): वृक्षवलय कालानुक्रम (Dendrochronology) रेडियोकार्बन तिथियों को कैलिब्रेट कर सकता है।\nकारण (R): पेड़ के छल्ले वार्षिक विकास को दर्ज करते हैं, जिससे विद्वान सत्यापित कैलेंडर आयु की लकड़ी में ¹⁴C स्तरों की जांच कर पाते हैं।",
    0,
    "Both A and R are true, and R explains how tree rings serve as a calibration standard for C-14 curves.",
    "A और R दोनों सही हैं और R व्याख्या करता है कि कैसे पेड़ के छल्ले C-14 वक्रों के लिए एक अंशांकन (calibration) मानक के रूप में कार्य करते हैं।"
)
add_ar(sec5_en, sec5_hi,
    "Assertion (A): Palynology is a relative dating method based on bone size.\nReason (R): Fossil bones dry up over time, allowing species identification under microscopes.",
    "कथन (A): परागकण विश्लेषण (Palynology) हड्डियों के आकार पर आधारित एक सापेक्ष तिथि निर्धारण विधि है।\nकारण (R): जीवाश्म हड्डियां समय के साथ सूख जाती हैं, जिससे सूक्ष्मदर्शी के नीचे प्रजातियों की पहचान की अनुमति मिलती है।",
    3,
    "Both A and R are false. Palynology is the study of pollen grains for environmental reconstruction, not bone measurements.",
    "A और R दोनों गलत हैं। परागकण विश्लेषण (Palynology) पुरा-पर्यावरण के पुनर्निर्माण के लिए परागकणों का अध्ययन है, न कि हड्डियों का।"
)
add_ar(sec5_en, sec5_hi,
    "Assertion (A): OSL dating was used to establish the antiquity of Attirampakkam tools.\nReason (R): Attirampakkam lacked organic materials for C-14, requiring sand burial dating of the layers surrounding the artifacts.",
    "कथन (A): अतिरम्पक्कम उपकरणों की प्राचीनता को स्थापित करने के लिए OSL डेटिंग का उपयोग किया गया था।\nकारण (R): अतिरम्पक्कम में C-14 के लिए जैविक सामग्री का अभाव था, जिसके कारण कलाकृतियों के आसपास की परतों की रेत दफन तिथि निर्धारण (sand burial dating) की आवश्यकता थी।",
    0,
    "Both A and R are true, and R explains why OSL was utilized instead of C-14.",
    "A और R दोनों सही हैं और R व्याख्या करता है कि C-14 के स्थान पर OSL का उपयोग क्यों किया गया था।"
)
add_ar(sec5_en, sec5_hi,
    "Assertion (A): Potassium-Argon dating is suitable for organic skeletons of the Holocene epoch.\nReason (R): Potassium decays extremely fast, with a half-life of only 200 years.",
    "कथन (A): पोटेशियम-आर्गन डेटिंग होलोसीन काल के जैविक कंकालों के लिए उपयुक्त है।\nकारण (R): पोटेशियम बहुत तेजी से क्षय होता है, जिसकी अर्ध-आयु केवल 200 वर्ष होती है।",
    3,
    "Both A and R are false. K-Ar is for volcanic rocks older than 100,000 years, and Potassium-40 has a half-life of 1.25 billion years.",
    "A और R दोनों गलत हैं। K-Ar डेटिंग 100,000 वर्ष से अधिक पुरानी ज्वालामुखी चट्टानों के लिए है, और पोटेशियम-40 की अर्ध-आयु 1.25 बिलियन वर्ष होती है।"
)
add_ar(sec5_en, sec5_hi,
    "Assertion (A): Stratigraphy provides relative chronology, not absolute calendar dates.\nReason (R): It determines whether a layer is older or younger relative to other layers based on position, but does not measure atomic decay rates.",
    "कथन (A): स्तरविन्यास (Stratigraphy) सापेक्ष कालक्रम प्रदान करता है, न कि निरपेक्ष कैलेंडर तिथियां।\nकारण (R): यह स्थिति के आधार पर निर्धारित करता है कि कोई परत अन्य परतों के सापेक्ष पुरानी है या नई, लेकिन यह परमाणु क्षय दरों को नहीं मापता है।",
    0,
    "Both A and R are true, and R is the correct explanation of A.",
    "A और R दोनों सही हैं और R, A की सही व्याख्या करता है।"
)
add_ar(sec5_en, sec5_hi,
    "Assertion (A): Palynology is critical for reconstructing agricultural history.\nReason (R): The sudden appearance of cereal pollen grains in lake deposits indicates the transition to crop cultivation.",
    "कथन (A): कृषि इतिहास के पुनर्निर्माण के लिए परागकण विश्लेषण (Palynology) महत्वपूर्ण है।\nकारण (R): झील के निक्षेपों में अनाज के परागकणों का अचानक प्रकट होना फसल की खेती में संक्रमण को दर्शाता है।",
    0,
    "Both statements are true and R explains how pollen records agricultural transitions.",
    "दोनों कथन सही हैं और R व्याख्या करता है कि कैसे परागकण कृषि संक्रमणों को दर्ज करते हैं।"
)

# 8. Statement-Based (5 Qs)
add_stmt(sec5_en, sec5_hi,
    "Consider the following statements regarding Radiocarbon (C-14) dating:\n1. It measures the decay of carbon-14 relative to stable carbon-12.\n2. It can date any organic material, including fossilized dinosaur bones.\n3. The half-life of carbon-14 is approximately 5,730 years.\nWhich of the statements given above are correct?",
    "रेडियोकार्बन (C-14) डेटिंग के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. यह स्थिर कार्बन-12 के सापेक्ष कार्बन-14 के क्षय को मापता है।\n2. यह डायनासोर की जीवाश्म हड्डियों सहित किसी भी जैविक सामग्री की तिथि निर्धारित कर सकता है।\n3. कार्बन-14 की अर्ध-आयु लगभग 5,730 वर्ष है।\nऊपर दिए गए कथनों में से कौन से सही हैं?",
    ["1 and 3 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"],
    ["केवल 1 और 3", "केवल 1 और 2", "केवल 2 और 3", "1, 2 और 3"],
    0,
    "Statements 1 and 3 are correct. C-14 is ineffective for dinosaur fossils because they are millions of years old, far exceeding C-14's 50,000-year limit.",
    "कथन 1 और 3 सही हैं। डायनासोर के जीवाश्मों के लिए C-14 अप्रभावी है क्योंकि वे लाखों साल पुराने हैं, जो C-14 की 50,000 वर्ष की सीमा से कहीं अधिक है।"
)
add_stmt(sec5_en, sec5_hi,
    "Consider the following statements regarding Luminescence dating methods:\n1. Thermoluminescence (TL) is used to date pottery and burnt clay.\n2. OSL dating measures the last exposure of sediment grains to heat.\n3. OSL was used to date Acheulian levels at Attirampakkam.\nWhich of the statements given above are correct?",
    "ल्यूमिनेसेंस (Luminescence) डेटिंग विधियों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. थर्मोलुमिनेसेंस (TL) का उपयोग मिट्टी के बर्तनों और पकी मिट्टी की तिथि निर्धारित करने के लिए किया जाता है।\n2. OSL डेटिंग तलछट के कणों के गर्मी के अंतिम संपर्क को मापती है।\n3. OSL का उपयोग अतिरम्पक्कम में अशुली स्तरों की तिथि निर्धारित करने के लिए किया गया था।\nऊपर दिए गए कथनों में से कौन से सही हैं?",
    ["1 and 3 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"],
    ["केवल 1 और 3", "केवल 1 और 2", "केवल 2 और 3", "1, 2 और 3"],
    0,
    "Statements 1 and 3 are correct. OSL measures the last exposure to sunlight (not heat).",
    "कथन 1 और 3 सही हैं। OSL सूर्य के प्रकाश (गर्मी नहीं) के अंतिम संपर्क को मापता है।"
)
add_stmt(sec5_en, sec5_hi,
    "With reference to absolute dating of early hominin sites, which of the following statements are correct?\n1. Potassium-Argon (K-Ar) dating is ideal for volcanic rock layers.\n2. C-14 dating can establish absolute dates for lower Paleolithic tools.\n3. Dendrochronology cannot be used for hominin sites due to lack of preserved tree specimens.\nSelect the correct answer using the code given below:",
    "प्रारंभिक मानव स्थलों की निरपेक्ष डेटिंग के संदर्भ में, निम्नलिखित में से कौन से कथन सही हैं?\n1. पोटेशियम-आर्गन (K-Ar) डेटिंग ज्वालामुखी चट्टान की परतों के लिए आदर्श है।\n2. C-14 डेटिंग निम्न पुरापाषाणकालीन उपकरणों के लिए निरपेक्ष तिथियां स्थापित कर सकती है।\n3. संरक्षित वृक्ष नमूनों की कमी के कारण मानव स्थलों के लिए वृक्षवलय कालानुक्रम का उपयोग नहीं किया जा सकता है।\nनीचे दिए गए कोड का उपयोग करके सही उत्तर चुनें:",
    ["1 and 3 only", "2 and 3 only", "1 and 2 only", "1, 2 and 3"],
    ["केवल 1 और 3", "केवल 2 और 3", "केवल 1 और 2", "1, 2 और 3"],
    0,
    "Statements 1 and 3 are correct. C-14 cannot date lower Paleolithic tools because they are older than 100,000 years, exceeding C-14's limit.",
    "कथन 1 और 3 सही हैं। C-14 निम्न पुरापाषाणकालीन उपकरणों की तिथि निर्धारित नहीं कर सकता क्योंकि वे 100,000 वर्ष से अधिक पुराने हैं, जो सी-14 की सीमा से अधिक है।"
)
add_stmt(sec5_en, sec5_hi,
    "Regarding environmental reconstruction methods, consider the following statements:\n1. Palynology reconstructs ancient flora shifts by analyzing fossil pollen.\n2. Palaeozoology tracks animal domestication by analyzing skeletal age/sex patterns.\n3. Stratigraphy uses pollen data to calibrate radiocarbon curves.\nWhich of the statements given above are correct?",
    "पर्यावरण पुनर्निर्माण विधियों के संबंध में, निम्नलिखित कथनों पर विचार करें:\n1. परागकण विश्लेषण जीवाश्म पराग का विश्लेषण करके प्राचीन वनस्पतियों के बदलावों का पुनर्निर्माण करता है।\n2. पुरा-प्राणीशास्त्र कंकाल की आयु/लिंग पैटर्न का विश्लेषण करके पशुओं को पालतू बनाने की प्रक्रिया को ट्रैक करता है।\n3. स्तरविन्यास (Stratigraphy) रेडियोकार्बन वक्रों को कैलिब्रेट करने के लिए पराग डेटा का उपयोग करता है।\nऊपर दिए गए कथनों में से कौन से सही हैं?",
    ["1 and 2 only", "3 only", "2 and 3 only", "1, 2 and 3"],
    ["केवल 1 और 2", "केवल 3", "केवल 2 और 3", "1, 2 और 3"],
    0,
    "Statements 1 and 2 are correct. Stratigraphy does not calibrate radiocarbon curves (which is done by Dendrochronology).",
    "कथन 1 और 2 सही हैं। स्तरविन्यास रेडियोकार्बन वक्रों को कैलिब्रेट नहीं करता (यह वृक्षवलय कालानुक्रम द्वारा किया जाता है)।"
)
add_stmt(sec5_en, sec5_hi,
    "Consider the following statements regarding relative versus absolute dating:\n1. Seriation is an absolute dating method based on stylistic changes.\n2. Potassium-Argon dating establishes absolute dates for organic remains.\n3. Relative dating methods only establish sequence, not calendar years.\nWhich of the statements given above is/are correct?",
    "सापेक्ष बनाम निरपेक्ष तिथि निर्धारण के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. श्रेणीकरण (Seriation) शैलीगत परिवर्तनों पर आधारित एक निरपेक्ष तिथि निर्धारण विधि है।\n2. पोटेशियम-आर्गन डेटिंग जैविक अवशेषों के लिए निरपेक्ष तिथियां स्थापित करती है।\n3. सापेक्ष तिथि निर्धारण विधियां केवल अनुक्रम स्थापित करती हैं, न कि कैलेंडर वर्ष।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["3 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"],
    ["केवल 3", "केवल 1 और 2", "केवल 2 और 3", "1, 2 और 3"],
    0,
    "Only statement 3 is correct. Seriation is relative, and K-Ar dates volcanic rocks (inorganic), not organic remains.",
    "केवल कथन 3 सही है। श्रेणीकरण सापेक्ष है, और K-Ar ज्वालामुखी चट्टानों (अकार्बनिक) की तिथि निर्धारित करता है, न कि जैविक अवशेषों की।"
)

# 9. Why (3 Qs)
add_open(sec5_en, sec5_hi, "Why",
    "Why is C-14 dating ineffective for establishing the antiquity of Lower Paleolithic stone tools?",
    "निम्न पुरापाषाणकालीन पत्थर के उपकरणों की प्राचीनता स्थापित करने के लिए C-14 डेटिंग अप्रभावी क्यों है?",
    "First, stone tools do not contain organic carbon, which is required for C-14 decay measurement. Second, Lower Paleolithic tools in India are older than 100,000 years (up to 1.5 MYA), far exceeding C-14's limit of approximately 50,000 years.",
    "पहला, पत्थर के उपकरणों में जैविक कार्बन नहीं होता है, जो C-14 क्षय माप के लिए आवश्यक है। दूसरा, भारत में निम्न पुरापाषाणकालीन उपकरण 100,000 वर्ष से अधिक पुराने (1.5 मिलियन वर्ष तक) हैं, जो C-14 की लगभग 50,000 वर्ष की सीमा से कहीं अधिक है।"
)
add_open(sec5_en, sec5_hi, "Why",
    "Why does the reset mechanism of Thermoluminescence (TL) make it ideal for dating pottery?",
    "थर्मोलुमिनेसेंस (TL) की रीसेट प्रणाली इसे मिट्टी के बर्तनों की तिथि निर्धारित करने के लिए आदर्श क्यों बनाती है?",
    "Pottery contains quartz and feldspar minerals that trap electrons over geological time. When clay is fired in a kiln, the high heat releases all trapped electrons as light, resetting the mineral 'clock' to zero. Once cooled, it accumulates electrons again, allowing scientists to measure the time elapsed since the firing event.",
    "मिट्टी के बर्तनों में क्वार्ट्ज और फेल्डस्पार खनिज होते हैं जो भूवैज्ञानिक समय में इलेक्ट्रॉनों को फंसाते हैं। जब मिट्टी को भट्टी में पकाया जाता है, तो उच्च गर्मी सभी फंसे हुए इलेक्ट्रॉनों को प्रकाश के रूप में छोड़ देती है, जिससे खनिज 'घड़ी' शून्य पर रीसेट हो जाती है। ठंडा होने के बाद, यह फिर से इलेक्ट्रॉनों को जमा करता है, जिससे वैज्ञानिक पकाने की घटना के बाद से बीते समय को माप पाते हैं।"
)
add_open(sec5_en, sec5_hi, "Why",
    "Why are fossil pollen grains (palynology) highly valued for reconstructing climate cycles?",
    "प्राचीन जलवायु चक्रों के पुनर्निर्माण के लिए जीवाश्म परागकणों (palynology) को अत्यधिक मूल्यवान क्यों माना जाता है?",
    "Pollen grains have a highly durable outer wall (sporopollenin) that resists chemical decay. When deposited in lake beds, they are preserved for millennia. By analyzing the species of plants represented in different sediment layers, scientists track shifts in vegetation indicating cycles of wet monsoons or dry ice age aridity.",
    "परागकणों में एक अत्यधिक टिकाऊ बाहरी दीवार (sporopollenin) होती है जो रासायनिक क्षय का विरोध करती है। जब वे झील के तल में जमा होते हैं, तो वे सहस्राब्दियों तक सुरक्षित रहते हैं। विभिन्न तलछट परतों में पौधों की प्रजातियों का विश्लेषण करके, वैज्ञानिक वनस्पतियों में बदलाव को ट्रैक करते हैं जो गीले मानसून या शुष्क हिमयुग की शुष्कता के चक्रों को दर्शाते हैं।"
)

# 10. How (3 Qs)
add_open(sec5_en, sec5_hi, "How",
    "How does Dendrochronology establish absolute calendar dates for archaeological wood remains?",
    "वृक्षवलय कालानुक्रम (Dendrochronology) पुरातात्विक लकड़ी के अवशेषों के लिए निरपेक्ष कैलेंडर तिथियां कैसे स्थापित करता है?",
    "Trees produce annual rings whose width varies based on climate. By matching overlapping patterns of wide and narrow rings from living trees to older structural timbers, scientists build a continuous master chronology database. Matching an archaeological wood sample's ring pattern to this database yields its exact calendar year.",
    "पेड़ वार्षिक छल्ले बनाते हैं जिनकी चौड़ाई जलवायु के आधार पर बदलती है। जीवित पेड़ों से लेकर पुराने इमारती लकड़ी के छल्लों के व्यापक और संकीर्ण पैटर्न का मिलान करके, वैज्ञानिक एक निरंतर मास्टर कालक्रम डेटाबेस बनाते हैं। इस डेटाबेस से पुरातात्विक लकड़ी के नमूने के छल्ले के पैटर्न का मिलान करने पर उसका सटीक कैलेंडर वर्ष प्राप्त होता है।"
)
add_open(sec5_en, sec5_hi, "How",
    "How does OSL dating determine the burial age of sediment layers?",
    "OSL डेटिंग तलछट की परतों की दफन आयु (burial age) कैसे निर्धारित करती है?",
    "OSL measures the energy trapped in quartz grains since they were buried. Exposure to sunlight releases this energy, resetting the clock to zero. Once buried and shielded from light, grains absorb background radiation. In the lab, exposing the grains to blue or green light releases this stored energy as luminescence, indicating burial time.",
    "OSL रेत के दबे होने के बाद से क्वार्ट्ज कणों में फंसी ऊर्जा को मापता है। सूर्य के प्रकाश के संपर्क में आने से यह ऊर्जा निकल जाती है, जिससे घड़ी शून्य पर रीसेट हो जाती है। दबने और प्रकाश से सुरक्षित होने पर, कण पृष्ठभूमि विकिरण को अवशोषित करते हैं। प्रयोगशाला में, कणों को नीले या हरे रंग के प्रकाश के संपर्क में लाने पर यह संचित ऊर्जा ल्यूमिनेसेंस के रूप में निकलती है, जो दफन समय को दर्शाती है।"
)
add_open(sec5_en, sec5_hi, "How",
    "How does Palaeozoology distinguish between wild hunting and early animal domestication in the archaeological record?",
    "पुरा-प्राणीशास्त्र (Palaeozoology) पुरातात्विक रिकॉर्ड में जंगली शिकार और प्रारंभिक पशुपालन के बीच अंतर कैसे करता है?",
    "By analyzing the age and sex profile of animal bones. In wild hunting, bones show a natural mix of old, young, male, and female animals. In domesticated contexts, there is a high concentration of bones from young males (culled for meat) and adult females (kept for breeding/milk), reflecting controlled herd management.",
    "जानवरों की हड्डियों की आयु और लिंग प्रोफाइल का विश्लेषण करके। जंगली शिकार में, हड्डियां बूढ़े, युवा, नर और मादा जानवरों का एक प्राकृतिक मिश्रण दिखाती हैं। पालतू संदर्भों में, युवा नरों (मांस के लिए मारे गए) और वयस्क मादाओं (प्रजनन/दूध के लिए रखी गई) की हड्डियों का उच्च संकेंद्रण होता है, जो नियंत्रित झुंड प्रबंधन को दर्शाता है।"
)

# 11. Case Study (3 Qs)
add_open(sec5_en, sec5_hi, "Case Study",
    "An excavation of a Neolithic mound in South India uncovers a thick layer of ash and vitrified dung, but no organic charcoal or wood. Select a scientific dating method to date this phase, and explain why.",
    "दक्षिण भारत में एक नवपाषाण टीले के उत्खनन से राख और पके हुए गोबर (vitrified dung) की एक मोटी परत मिलती है, लेकिन वहाँ कोई जैविक कोयला या लकड़ी नहीं है। इस चरण की तिथि निर्धारित करने के लिए एक वैज्ञानिक पद्धति चुनें और समझाएं कि क्यों।",
    "The researcher should select **Thermoluminescence (TL) dating** or **OSL dating** on the vitrified dung and ash minerals. Since the dung was burned at high temperatures, the heat reset the TL clock of quartz grains inside. TL will measure the time elapsed since this burning event (associated with Neolithic Ash Mounds).",
    "शोधकर्ता को राख के खनिजों पर **थर्मोलुमिनेसेंस (TL) डेटिंग** या **OSL डेटिंग** चुननी चाहिए। चूंकि गोबर को उच्च तापमान पर जलाया गया था, इसलिए गर्मी ने भीतर के क्वार्ट्ज कणों की टीएल घड़ी को शून्य कर दिया। TL इस जलने की घटना (नवपाषाणकालीन राख के टीलों से जुड़ी) के बाद से बीते समय को मापेगा।"
)
add_open(sec5_en, sec5_hi, "Case Study",
    "At a site in the Rajasthan desert, archaeologists discover Paleolithic tool layers buried 10 meters deep in sand dunes. Organic material is absent. Reconstruct the age of the dunes and tools using OSL.",
    "राजस्थान के मरुस्थल में एक स्थल पर, पुरातत्वविदों को रेत के टीलों में 10 मीटर गहराई में दबे हुए पुरापाषाणकालीन उपकरण मिलते हैं। जैविक सामग्री अनुपस्थित है। OSL का उपयोग करके टीलों और उपकरणों की आयु का पुनर्निर्माण करें।",
    "The team should collect sand samples from the layer surrounding the tools without exposing them to light. **OSL dating** will measure the last time these quartz sand grains were exposed to sunlight (bleached) before being buried by the dune. This date will define the exact geological epoch when the tools were discarded and covered by sand.",
    "टीम को उपकरणों के आसपास की परत से रेत के नमूने प्रकाश के संपर्क में लाए बिना एकत्र करने चाहिए। **OSL डेटिंग** यह मापेगी कि इन क्वार्ट्ज रेत के कणों को टीले द्वारा दबाए जाने से पहले आखिरी बार कब सूर्य के प्रकाश के संपर्क में लाया गया था। यह तिथि उस भूवैज्ञानिक काल को परिभाषित करेगी जब उपकरणों को रेत द्वारा कवर किया गया था।"
)
add_open(sec5_en, sec5_hi, "Case Study",
    "A soil core extracted from an ancient lake bed in Haryana reveals a layer dated to c. 2000 BCE. Palynological analysis shows a sudden decline in tree pollen and a massive rise in weed and cereal pollen. Reconstruct the environmental change.",
    "हरियाणा में एक प्राचीन झील के तल से निकाले गए मिट्टी के कोर से लगभग 2000 ईसा पूर्व की एक परत का पता चलता है। परागकण विश्लेषण से पेड़ के पराग में अचानक गिरावट और खरपतवार तथा अनाज के पराग में भारी वृद्धि दिखाई देती है। पर्यावरणीय बदलाव का पुनर्निर्माण करें।",
    "This palynological shift indicates deforestation and the onset of intensive agriculture. The decrease in tree pollen shows that forests were cleared (likely using fire and tools), while the rise in cereal and weed pollen proves the cleared land was used for crop cultivation and farming, changing the local ecological landscape.",
    "यह परागकण बदलाव वनों की कटाई और गहन कृषि की शुरुआत का संकेत देता है। पेड़ के पराग में कमी यह दर्शाती है कि जंगलों को साफ किया गया था (संभवतः आग और उपकरणों का उपयोग करके), जबकि अनाज और खरपतवार के पराग में वृद्धि यह सिद्ध करती है कि साफ की गई भूमि का उपयोग फसल की खेती के लिए किया गया था, जिससे स्थानीय पारिस्थितिकी बदल गई थी।"
)

# 12. Teach the Concept (3 Qs)
add_open(sec5_en, sec5_hi, "Teach the Concept",
    "Explain the concept of 'Half-Life' in radioactive dating to a student. Use a simple pile of coins analogy.",
    "एक छात्र को रेडियोधर्मी तिथि निर्धारण में 'अर्ध-आयु' (Half-Life) की अवधारणा समझाएं। सिक्कों के ढेर के एक सरल उदाहरण का उपयोग करें।",
    "Imagine you start with a pile of 100 coins. Every hour, you flip all of them, and remove any coins that land on tails. After the first hour, about 50 coins will remain (half). After the second hour, about 25 will remain. The 'half-life' is that fixed time (one hour) it takes for half of the pile to decay. Similarly, in Carbon-14, it takes 5,730 years for half of the C-14 atoms to decay into nitrogen.",
    "कल्पना कीजिए कि आप 100 सिक्कों के ढेर से शुरू करते हैं। हर घंटे, आप उन सभी को उछालते हैं और उन सिक्कों को हटा देते हैं जिन पर पट (tails) आता है। पहले घंटे के बाद, लगभग 50 सिक्के बचेंगे (आधे)। दूसरे घंटे के बाद, लगभग 25 बचेंगे। 'अर्ध-आयु' वह निश्चित समय (एक घंटा) है जो ढेर के आधा होने में लगता है। इसी तरह, कार्बन-14 में, आधे C-14 परमाणुओं को नाइट्रोजन में क्षय होने में 5,730 वर्ष लगते हैं।"
)
add_open(sec5_en, sec5_hi, "Teach the Concept",
    "Explain how Thermoluminescence (TL) works. Create a visual trick involving a rechargeable battery.",
    "थर्मोलुमिनेसेंस (TL) कैसे काम करता है, समझाएं। रिचार्जेबल बैटरी से जुड़ा एक दृश्य उदाहरण बनाएं।",
    "Think of a mineral grain as a **rechargeable battery**. Over thousands of years under the ground, it slowly absorbs background radiation (charging the battery with trapped electrons). Firing the clay in a kiln is like **unplugging and short-circuiting** the battery (all stored energy is released instantly as light, resetting it to zero). The battery starts recharging again. In the lab, we heat it to measure how much charge (trapped light) it accumulated since it was fired.",
    "एक खनिज कण को एक **रिचार्जेबल बैटरी** के रूप में सोचें। जमीन के नीचे हजारों वर्षों में, यह धीरे-धीरे पृष्ठभूमि विकिरण को अवशोषित करता है (फंसे हुए इलेक्ट्रॉनों के साथ बैटरी को चार्ज करता है)। भट्टी में मिट्टी को पकाना बैटरी को **शॉर्ट-सर्किट** करने जैसा है (सभी संचित ऊर्जा तुरंत प्रकाश के रूप में निकल जाती है और शून्य पर आ जाती है)। बैटरी फिर से चार्ज होने लगती है। प्रयोगशाला में, हम इसे गर्म करके मापते हैं कि इसके पकने के बाद से इसमें कितना चार्ज (फंसा हुआ प्रकाश) संचित हुआ है।"
)
add_open(sec5_en, sec5_hi, "Teach the Concept",
    "How does palynology reconstruct the ancient environment? Explain using the concept of plant fingerprints.",
    "परागकण विश्लेषण (palynology) प्राचीन पर्यावरण का पुनर्निर्माण कैसे करता है? पौधों के उंगलियों के निशान (fingerprints) की अवधारणा का उपयोग करके समझाएं।",
    "Pollen grains act as **individual fingerprints** for plant species; oak pollen looks completely different from wheat or grass pollen. Because these fingerprints are made of tough shell material, they remain preserved in soil layers. By counting these fingerprints under a microscope, scientists reconstruct the exact vegetation layout of the past, showing whether a site was a wet forest or a dry desert.",
    "परागकण पौधों की प्रजातियों के लिए **व्यक्तिगत उंगलियों के निशान (fingerprints)** के रूप में कार्य करते हैं; बांज (oak) का पराग गेहूं या घास के पराग से पूरी तरह से अलग दिखता है। क्योंकि ये निशान सख्त सामग्री से बने होते हैं, वे मिट्टी की परतों में सुरक्षित रहते हैं। सूक्ष्मदर्शी के नीचे इन निशानों की गिनती करके, वैज्ञानिक अतीत के वनस्पतियों के लेआउट का पुनर्निर्माण करते हैं, जिससे पता चलता है कि कोई स्थल गीला जंगल था या सूखा रेगिस्तान।"
)


# ==========================================
# HELPERS FOR ROOT PRACTICE & MOCK QUESTIONS
# ==========================================

def add_root_mcq(q_en, q_hi, opts_en, opts_hi, ans, sol_en, sol_hi):
    practice_en.append({"q": q_en, "opts": opts_en, "ans": ans, "sol": sol_en})
    practice_hi.append({"q": q_hi, "opts": opts_hi, "ans": ans, "sol": sol_hi})

def add_mock_mcq(q_en, q_hi, opts_en, opts_hi, ans, sol_en, sol_hi):
    mock_en.append({"q": q_en, "opts": opts_en, "ans": ans, "sol": sol_en})
    mock_hi.append({"q": q_hi, "opts": opts_hi, "ans": ans, "sol": sol_hi})

# ==========================================
# 50 PRACTICE QUESTIONS (MCQs)
# ==========================================

# 1
add_root_mcq(
    "Who is designated as the 'Father of Indian Prehistory'?",
    "किसे 'भारतीय प्रागैतिहास का जनक' कहा जाता है?",
    ["Robert Bruce Foote", "Mortimer Wheeler", "John Marshall", "Alexander Cunningham"],
    ["रॉबर्ट ब्रूस फुट", "मॉर्टिमर व्हीलर", "जॉन मार्शल", "अलेक्जेंडर कनिंघम"],
    0,
    "Robert Bruce Foote was a British geologist who discovered the first Palaeolithic tool (a handaxe) at Pallavaram, near Madras, in 1863, earning him this title.",
    "रॉबर्ट ब्रूस फुट एक ब्रिटिश भूवैज्ञानिक थे जिन्होंने 1863 में मद्रास के निकट पल्लवरम में पहले पुरापाषाणकालीन उपकरण (एक हस्तकुठार) की खोज की थी, जिसके कारण उन्हें यह उपाधि मिली।"
)

# 2
add_root_mcq(
    "In which year did James Prinsep decipher the Brahmi script, unlocking the historical Ashokan inscriptions?",
    "जेम्स प्रिंसेप ने किस वर्ष ब्राह्मी लिपि को पढ़ा था, जिससे अशोक के ऐतिहासिक अभिलेखों का अर्थ स्पष्ट हुआ?",
    ["1827", "1837", "1847", "1857"],
    ["1827", "1837", "1847", "1857"],
    1,
    "James Prinsep deciphered the Brahmi script in 1837, which allowed historians to read the rock and pillar edicts of Emperor Ashoka.",
    "जेम्स प्रिंसेप ने 1837 में ब्राह्मी लिपि को पढ़ा था, जिससे इतिहासकारों को सम्राट अशोक के शिलालेखों और स्तंभ लेखों को पढ़ने में मदद मिली।"
)

# 3
add_root_mcq(
    "Which scientific dating method is ideal for volcanic rocks associated with early hominin fossil sites like those in the Soan valley?",
    "पोटवार/सोअन घाटी जैसे शुरुआती मानव जीवाश्म स्थलों से जुड़ी ज्वालामुखी चट्टानों के लिए कौन सी वैज्ञानिक काल-निर्धारण पद्धति आदर्श है?",
    ["Radiocarbon (C-14) Dating", "Thermoluminescence (TL)", "Potassium-Argon (K-Ar) Dating", "Dendrochronology"],
    ["रेडियोकार्बन (C-14) डेटिंग", "थर्मोलुमिनेसेंस (TL)", "पोटेशियम-आर्गन (K-Ar) डेटिंग", "वृक्षवलय कालानुक्रम (Dendrochronology)"],
    2,
    "Potassium-Argon (K-Ar) dating measures the decay of Potassium-40 to Argon-40 in volcanic ash and rocks, suitable for dating sites older than 100,000 years.",
    "पोटेशियम-आर्गन (K-Ar) डेटिंग ज्वालामुखी राख और चट्टानों में पोटेशियम-40 के आर्गन-40 में क्षय को मापती है, जो 100,000 वर्ष से अधिक पुराने स्थलों के काल-निर्धारण के लिए उपयुक्त है।"
)

# 4
add_root_mcq(
    "The systematic study of ancient inscriptions and written records engraved on hard surfaces is known as:",
    "कठोर सतहों पर उत्कीर्ण प्राचीन अभिलेखों और लिखित अभिलेखों के व्यवस्थित अध्ययन को क्या कहा जाता है?",
    ["Numismatics", "Epigraphy", "Palynology", "Stratigraphy"],
    ["मुद्राशास्त्र (Numismatics)", "अभिलेखशास्त्र (Epigraphy)", "परागकण विश्लेषण (Palynology)", "स्तरविन्यास (Stratigraphy)"],
    1,
    "Epigraphy is the study of inscriptions engraved on stone, metal, clay, or other hard surfaces.",
    "अभिलेखशास्त्र (Epigraphy) पत्थर, धातु, मिट्टी या अन्य कठोर सतहों पर उत्कीर्ण अभिलेखों का अध्ययन है।"
)

# 5
add_root_mcq(
    "The systematic study of coins, which provides key insights into ancient economy, metallurgy, and trade routes, is termed:",
    "सिक्कों का व्यवस्थित अध्ययन, जो प्राचीन अर्थव्यवस्था, धातु कर्म और व्यापार मार्गों के बारे में महत्वपूर्ण जानकारी प्रदान करता है, क्या कहलाता है?",
    ["Palaeography", "Epigraphy", "Numismatics", "Seriation"],
    ["पुरालेखशास्त्र (Palaeography)", "अभिलेखशास्त्र (Epigraphy)", "मुद्राशास्त्र (Numismatics)", "श्रेणीकरण (Seriation)"],
    2,
    "Numismatics is the study of coins, tokens, paper money, and related monetary instruments.",
    "मुद्राशास्त्र (Numismatics) सिक्कों, टोकनों, कागजी मुद्रा और संबंधित मौद्रिक साधनों का अध्ययन है।"
)

# 6
add_root_mcq(
    "Which Chinese traveller visited India during the Gupta reign of Chandragupta II to collect Buddhist scriptures?",
    "बौद्ध धर्मग्रंथों को एकत्र करने के लिए चंद्रगुप्त द्वितीय के गुप्त शासनकाल के दौरान किस चीनी यात्री ने भारत का दौरा किया था?",
    ["Hiuen Tsang (Xuanzang)", "Fa-Hien", "I-Tsing", "Song Yun"],
    ["ह्वेनसांग (Xuanzang)", "फाहियान (Fa-Hien)", "इत्सिंग (I-Tsing)", "सोंग युन"],
    1,
    "Fa-Hien visited India between 399 and 414 CE, during the reign of Chandragupta II, primarily focusing on visiting Buddhist pilgrimage sites.",
    "फाहियान ने चंद्रगुप्त द्वितीय के शासनकाल के दौरान 399 और 414 ईस्वी के बीच भारत का दौरा किया, मुख्य रूप से बौद्ध तीर्थस्थलों के दर्शन पर ध्यान केंद्रित किया।"
)

# 7
add_root_mcq(
    "Who authored the academic study 'Kitab-ul-Hind', providing an objective account of Indian society, mathematics, and philosophy in the 11th century?",
    "11वीं शताब्दी में भारतीय समाज, गणित और दर्शन का निष्पक्ष विवरण प्रदान करने वाले शैक्षणिक ग्रंथ 'किताब-उल-हिंद' के लेखक कौन थे?",
    ["Al-Masudi", "Al-Biruni", "Ibn Battuta", "Firdausi"],
    ["अल-मसूदी", "अल-बिरूनी", "इब्न बतूता", "फिरदौसी"],
    1,
    "Al-Biruni, a Persian polymath who accompanied Mahmud of Ghazni to India, authored the detailed study Kitab-ul-Hind.",
    "महमूद गजनवी के साथ भारत आए फारसी विद्वान अल-बिरूनी ने विस्तृत अध्ययन किताब-उल-हिंद की रचना की थी।"
)

# 8
add_root_mcq(
    "Which prehistoric site in India has yielded the oldest Acheulian stone tools, dated to c. 1.5 million years ago?",
    "भारत के किस प्रागैतिहासिक स्थल से लगभग 15 लाख वर्ष पुराने सबसे पुराने एशुलेयिन (Acheulian) पाषाण उपकरण मिले हैं?",
    ["Bhimbetka", "Mehrgarh", "Attirampakkam", "Hunsgi"],
    ["भीमबेटका", "मेहरगढ़", "अतिरामपक्कम", "हुन्सगी"],
    2,
    "Attirampakkam in Tamil Nadu, excavated by Shanti Pappu and her team, has been dated to c. 1.5 million years ago using cosmogenic nuclide burial dating.",
    "तमिलनाडु में अतिरामपक्कम, जिसका उत्खनन शांति पप्पू और उनकी टीम द्वारा किया गया था, को कॉस्मोजेनिक न्यूक्लाइड दफन डेटिंग का उपयोग करके लगभग 1.5 मिलियन वर्ष पुराना आंका गया है।"
)

# 9
add_root_mcq(
    "The earliest Neolithic agricultural settlement in the northwestern Indian subcontinent, dated to c. 7000 BCE, is:",
    "उत्तर-पश्चिमी भारतीय उपमहाद्वीप में सबसे प्रारंभिक नवपाषाण कृषि बस्ती, जो लगभग 7000 ईसा पूर्व की है, कौन सी है?",
    ["Koldihwa", "Mehrgarh", "Burzahom", "Lahuradewa"],
    ["कोल्डिहवा", "मेहरगढ़", "बुर्जहोम", "लहुरादेवा"],
    1,
    "Mehrgarh in Balochistan (Pakistan), excavated by Jean-Francois Jarrige, is the earliest Neolithic village showing transition to barley-wheat farming and sheep-goat pastoralism.",
    "बलूचिस्तान (पाकिस्तान) में मेहरगढ़, जीन-फ्रांस्वा जारिज द्वारा उत्खनित, सबसे प्रारंभिक नवपाषाण गाँव है जो जौ-गेहूं की खेती और भेड़-बकरी पालन के संक्रमण को दर्शाता है।"
)

# 10
add_root_mcq(
    "With which prehistoric phase are the 'Ash Mounds' of Southern India associated?",
    "दक्षिण भारत के 'राख के टीले' (Ash Mounds) किस प्रागैतिहासिक चरण से जुड़े हैं?",
    ["Lower Palaeolithic Hunter-Gatherers", "Neolithic Pastoralists", "Mesolithic Nomadic Camps", "Harappan Urban Centers"],
    ["निम्न पुरापाषाण शिकारी-संग्रहकर्ता", "नवपाषाणकालीन चरवाहे/पशुपालक", "मध्यपाषाण घुमंतू शिविर", "हड़प्पा शहरी केंद्र"],
    1,
    "Ash mounds (found at sites like Utnur, Kupgal, Piklihal, and Palavoy) represent vitrified cattle dung heaps burned at Neolithic pastoral sites.",
    "राख के टीले (उतनूर, कुपगल, पिकलिखल और पालवॉय जैसे स्थलों पर पाए गए) नवपाषाणकालीन चरवाहों की बस्तियों में संचित गोबर के जलने से बने थे।"
)

# 11
add_root_mcq(
    "Consider the following statements regarding relative vs. absolute dating methods:\\n1. Stratigraphy is an absolute dating method because it provides specific dates in calendar years.\\n2. Radiocarbon dating (C-14) is a relative dating method because it only establishes a sequence of events.\\n3. Stratigraphy is relative, whereas Carbon-14 is absolute.\\nWhich of the statements given above is/are correct?",
    "सापेक्ष बनाम निरपेक्ष काल-निर्धारण विधियों के संबंध में निम्नलिखित कथनों पर विचार करें:\\n1. स्तरविन्यास (Stratigraphy) एक निरपेक्ष तिथि निर्धारण विधि है क्योंकि यह कैलेंडर वर्षों में विशिष्ट तिथियां प्रदान करती है।\\n2. रेडियोकार्बन डेटिंग (C-14) एक सापेक्ष तिथि निर्धारण विधि है क्योंकि यह केवल घटनाओं का एक क्रम स्थापित करती है।\\n3. स्तरविन्यास सापेक्ष है, जबकि कार्बन -14 निरपेक्ष है।\\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 only", "2 only", "3 only", "1 and 2 only"],
    ["केवल 1", "केवल 2", "केवल 3", "केवल 1 और 2"],
    2,
    "Stratigraphy is a relative dating method based on geological layers (deep is older). Radiocarbon dating is an absolute dating method that calculates actual age range in calendar years based on C-14 decay.",
    "स्तरविन्यास भूवैज्ञानिक परतों पर आधारित एक सापेक्ष तिथि निर्धारण विधि है। रेडियोकार्बन डेटिंग एक निरपेक्ष तिथि निर्धारण विधि है जो C-14 क्षय के आधार पर कैलेंडर वर्षों में वास्तविक आयु सीमा की गणना करती है।"
)

# 12
add_root_mcq(
    "The first deciphered written records in India are the edicts of Emperor Ashoka. Which script was primarily used for these inscriptions in northern India?",
    "भारत में सबसे पहले पढ़े गए लिखित अभिलेख सम्राट अशोक के शिलालेख हैं। उत्तरी भारत में इन अभिलेखों के लिए मुख्य रूप से किस लिपि का उपयोग किया गया था?",
    ["Kharoshthi", "Brahmi", "Aramaic", "Devanagari"],
    ["खरोष्ठी", "ब्राह्मी", "अरामी", "देवनागरी"],
    1,
    "The Ashokan edicts in northern and central India were primarily written in the Brahmi script, which is the parent of most modern Indian scripts.",
    "उत्तरी और मध्य भारत में अशोक के शिलालेख मुख्य रूप से ब्राह्मी लिपि में लिखे गए थे, जो अधिकांश आधुनिक भारतीय लिपियों की जननी है।"
)

# 13
add_root_mcq(
    "Why are the accounts of Megasthenes, who visited Pataliputra as a Greek ambassador, considered problematic by modern historians?",
    "यूनानी राजदूत के रूप में पाटलिपुत्र का दौरा करने वाले मेगस्थनीज के विवरण को आधुनिक इतिहासकारों द्वारा समस्याग्रस्त क्यों माना जाता है?",
    ["His original book 'Indica' is lost and survives only as fragments in later Greek-Roman texts.", "He never visited India and compiled his book based on hearsay.", "He wrote his account in classical Sanskrit which was poorly translated.", "He was banished from India before he could finish his writing."],
    ["उनकी मूल पुस्तक 'इंडिका' खो गई है और बाद के ग्रीक-रोमन ग्रंथों में केवल उद्धरणों के रूप में बची है।", "उन्होंने कभी भारत का दौरा नहीं किया और केवल सुनी-सुनाई बातों के आधार पर अपनी पुस्तक तैयार की।", "उन्होंने अपना विवरण शास्त्रीय संस्कृत में लिखा था जिसका अनुवाद खराब था।", "अपना लेखन पूरा करने से पहले ही उन्हें भारत से निर्वाह कर दिया गया था।"],
    0,
    "Megasthenes' original 'Indica' is lost. Modern reconstructions are based on fragments quoted by later classical writers like Arrian, Strabo, Diodorus, and Pliny.",
    "मेगस्थनीज की मूल 'इंडिका' खो गई है। आधुनिक पुनर्निर्माण एरियन, स्ट्रैबो, डियोडोरस और प्लिनी जैसे बाद के शास्त्रीय लेखकों द्वारा उद्धृत अंशों पर आधारित हैं।"
)

# 14
add_root_mcq(
    "Which Chinese traveller visited Nalanda University during the reign of Harshavardhana and recorded detailed administrative and socio-economic accounts?",
    "हर्षवर्धन के शासनकाल में किस चीनी यात्री ने नालंदा विश्वविद्यालय का दौरा किया और विस्तृत प्रशासनिक और सामाजिक-आर्थिक विवरण दर्ज किए?",
    ["Fa-Hien", "I-Tsing", "Hiuen Tsang (Xuanzang)", "Song Yun"],
    ["फाहियान", "इत्सिंग", "ह्वेनसांग (Xuanzang)", "सोंग युन"],
    2,
    "Hiuen Tsang (Xuanzang) spent several years studying at Nalanda and travelling across Harshavardhana's empire in the 7th century CE.",
    "ह्वेनसांग (Xuanzang) ने 7वीं शताब्दी ईस्वी में नालंदा में अध्ययन किया और हर्षवर्धन के साम्राज्य में यात्रा करते हुए कई वर्ष बिताए।"
)

# 15
add_root_mcq(
    "Which scientific method is used to reconstruct prehistoric vegetation patterns and changes in monsoonal precipitation by studying fossil spores and pollen grains?",
    "जीवाश्म बीजाणुओं और परागकणों का अध्ययन करके प्रागैतिहासिक वनस्पति पैटर्न और मानसूनी वर्षा में बदलाव का पुनर्निर्माण करने के लिए किस वैज्ञानिक पद्धति का उपयोग किया जाता है?",
    ["Palaeobotany", "Palynology", "OSL Dating", "Palaeozoology"],
    ["पुरावनस्पतिशास्त्र", "परागकण विश्लेषण (Palynology)", "OSL डेटिंग", "पुराप्राणीशास्त्र"],
    1,
    "Palynology is the study of organic microfossils like pollen and spores, which have durable outer shells and reflect regional vegetational history.",
    "परागकण विश्लेषण (Palynology) पराग और बीजाणुओं जैसे कार्बनिक सूक्ष्मजीवाश्मों का अध्ययन है, जिनमें टिकाऊ बाहरी आवरण होते हैं और जो क्षेत्रीय वनस्पति इतिहास को दर्शाते हैं।"
)

# 16
add_root_mcq(
    "The ancient site of Bhimbetka, famous for its prehistoric rock art, was discovered in 1957 by which prominent Indian archaeologist?",
    "प्रागैतिहासिक शैल कला के लिए प्रसिद्ध भीमबेटका के प्राचीन स्थल की खोज 1957 में किस प्रमुख भारतीय पुरातत्वविद् ने की थी?",
    ["H. D. Sankalia", "V. S. Wakankar", "B. B. Lal", "D. N. Wadia"],
    ["एच. डी. संकलिया", "वी. एस. वाकणकर", "बी. बी. लाल", "डी. एन. वाडिया"],
    1,
    "Dr. Vishnu Shridhar Wakankar discovered the Bhimbetka rock shelters in 1957, revealing one of the largest concentrations of prehistoric rock art in the world.",
    "डॉ. विष्णु श्रीधर वाकणकर ने 1957 में भीमबेटका शैल आश्रयों की खोज की थी, जिससे दुनिया में प्रागैतिहासिक शैल कला के सबसे बड़े संकेंद्रणों में से एक का पता चला।"
)

# 17
add_root_mcq(
    "Which of the following books is a Greek sailor's anonymous logbook from the 1st century CE detailing Roman trade routes, ports, and items traded with India?",
    "निम्नलिखित में से कौन सी पुस्तक पहली शताब्दी ईस्वी की एक अज्ञात ग्रीक नाविक की लॉगबुक है जिसमें रोमन व्यापार मार्गों, बंदरगाहों और भारत के साथ व्यापार की जाने वाली वस्तुओं का विवरण है?",
    ["Indica", "Natural History", "Periplus of the Erythraean Sea", "Geography of India"],
    ["इंडिका", "प्राकृतिक इतिहास (Natural History)", "पेरिप्लस ऑफ द एरिथ्रियन सी", "भारत का भूगोल (Geography)"],
    2,
    "The Periplus of the Erythraean Sea, written by an anonymous Greek-speaking merchant/sailor, is an invaluable guide to Indo-Roman trade in the 1st century CE.",
    "पेरिप्लस ऑफ द एरिथ्रियन सी, एक अज्ञात ग्रीक भाषी व्यापारी/नाविक द्वारा लिखित, पहली शताब्दी ईस्वी में भारत-रोमन व्यापार के लिए एक अमूल्य मार्गदर्शिका है।"
)

# 18
add_root_mcq(
    "What is the primary material component measured during Thermoluminescence (TL) dating of archaeological pottery?",
    "पुरातात्विक मिट्टी के बर्तनों के थर्मोलुमिनेसेंस (TL) काल-निर्धारण के दौरान मापी जाने वाली प्राथमिक सामग्री घटक क्या है?",
    ["Organic carbon content in clay", "Trapped electrons in mineral grains like quartz and feldspar", "Decay of uranium isotopes in the clay matrix", "Tree-ring growth rings in the surrounding layer"],
    ["मिट्टी में कार्बनिक कार्बन की मात्रा", "क्वार्ट्ज और फेल्डस्पार जैसे खनिज कणों में फंसे हुए इलेक्ट्रॉन", "मिट्टी में यूरेनियम समस्थानिकों (isotopes) का क्षय", "आसपास की परत में पेड़ के छल्ले"],
    1,
    "TL dating measures the accumulated radiation dose in quartz and feldspar minerals since they were last fired (which released all previous trapped electrons).",
    "TL डेटिंग क्वार्ट्ज और फेल्डस्पार खनिजों में संचित विकिरण खुराक को मापती है जब से उन्हें आखिरी बार पकाया गया था (जिसने पिछले सभी फंसे हुए इलेक्ट्रॉनों को मुक्त कर दिया था)।"
)

# 19
add_root_mcq(
    "The oldest deciphered writing system in India, Brahmi, is read from:",
    "भारत की सबसे पुरानी पढ़ी गई लेखन प्रणाली, ब्राह्मी, किस दिशा से पढ़ी जाती है?",
    ["Right to Left", "Left to Right", "Boustrophedon (alternate directions)", "Top to Bottom"],
    ["दाएं से बाएं", "बाएं से दाएं", "बूस्ट्रोफेडन (बारी-बारी से दिशा बदलना)", "ऊपर से नीचे"],
    1,
    "Unlike the Kharoshthi script (which was read from right to left), Brahmi script was written and read from left to right, similar to Devanagari.",
    "खरोष्ठी लिपि (जो दाएं से बाएं पढ़ी जाती थी) के विपरीत, ब्राह्मी लिपि बाएं से दाएं लिखी और पढ़ी जाती थी, जो देवनागरी के समान है।"
)

# 20
add_root_mcq(
    "Which Vedic text represents the oldest literary source in India, offering geographical references to the 'Sapta Sindhu' (Seven Rivers) region?",
    "कौन सा वैदिक ग्रंथ भारत में सबसे पुराना साहित्यिक स्रोत है, जो 'सप्त सिंधु' (सात नदियों) क्षेत्र के भौगोलिक संदर्भ प्रदान करता है?",
    ["Sama Veda", "Yajur Veda", "Rig Veda", "Atharva Veda"],
    ["सामवेद", "यजुर्वेद", "ऋग्वेद", "अथर्ववेद"],
    2,
    "The Rig Veda (composed c. 1500–1200 BCE) is the oldest literary work in India. It contains hymns describing the geography, rivers, and tribes of the Indus region.",
    "ऋग्वेद (लगभग 1500-1200 ईसा पूर्व रचित) भारत का सबसे पुराना साहित्यिक ग्रंथ है। इसमें सिंधु क्षेत्र के भूगोल, नदियों और जनजातियों का वर्णन करने वाले भजन शामिल हैं।"
)

# 21
add_root_mcq(
    "Why is Radiocarbon (C-14) dating ineffective for dating Palaeolithic stone tools directly?",
    "पुरापाषाणकालीन पाषाण उपकरणों का सीधे तौर पर रेडियोकार्बन (C-14) काल-निर्धारण करने के लिए यह विधि अप्रभावी क्यों है?",
    ["Stone tools do not contain organic carbon required for C-14 decay measurement.", "Palaeolithic tool layers are always contaminated by ground water.", "C-14 has a half-life of only 100 years, making it too short.", "Quartzite stones absorb radiocarbon and distort the results."],
    ["पत्थर के औजारों में C-14 क्षय माप के लिए आवश्यक जैविक कार्बन नहीं होता है।", "पुरापाषाणकालीन उपकरण परतें हमेशा भूजल से दूषित होती हैं।", "C-14 की अर्ध-आयु केवल 100 वर्ष है, जो बहुत कम है।", "क्वार्ट्जाइट पत्थर रेडियोकार्बन को अवशोषित करते हैं और परिणामों को विकृत करते हैं।"],
    0,
    "Radiocarbon dating only works on organic remains (charcoal, wood, bone, shell). Stone tools do not contain organic carbon, so the surrounding organic layers must be dated instead.",
    "रेडियोकार्बन डेटिंग केवल जैविक अवशेषों (कोयला, लकड़ी, हड्डी, शंख) पर काम करती है। पत्थर के औजारों में कार्बनिक कार्बन नहीं होता है, इसलिए आसपास की जैविक परतों की तिथि निर्धारित की जानी चाहिए।"
)

# 22
add_root_mcq(
    "Which archaeological excavation technique cuts deep vertical trenches into the soil to establish a chronological sequence of cultures?",
    "संस्कृतियों के कालानुक्रमिक अनुक्रम को स्थापित करने के लिए कौन सी पुरातात्विक उत्खनन तकनीक मिट्टी में गहरे ऊर्ध्वाधर गड्ढे खोदती है?",
    ["Horizontal Excavation", "Vertical Excavation", "Grid-system Excavation", "Open-cast Excavation"],
    ["क्षैतिज उत्खनन (Horizontal Excavation)", "ऊर्ध्वाधर उत्खनन (Vertical Excavation)", "ग्रिड-प्रणाली उत्खनन", "ओपन-कास्ट उत्खनन"],
    1,
    "Vertical excavation cuts through layers vertically to reveal a succession of cultural phases over time, acting as a chronological probe.",
    "ऊर्ध्वाधर उत्खनन समय के साथ सांस्कृतिक चरणों के अनुक्रम को प्रकट करने के लिए लंबवत परतों को काटता है, जो एक कालानुक्रमिक जांच के रूप में कार्य करता है।"
)

# 23
add_root_mcq(
    "The earliest Indian coins, known as Punch-Marked Coins (c. 6th century BCE), were primarily made of which metal?",
    "प्रारंभिक भारतीय सिक्के, जिन्हें आहत सिक्के या पंच-चिह्नित सिक्के (लगभग 6ठी शताब्दी ईसा पूर्व) कहा जाता है, मुख्य रूप से किस धातु के बने थे?",
    ["Gold", "Lead", "Silver", "Iron"],
    ["सोना", "सीसा", "चांदी", "लोहा"],
    2,
    "The earliest punch-marked coins (associated with Mahajanapadas and Mauryas) were primarily made of silver, though some copper coins also existed.",
    "शुरुआती आहत सिक्के (महाजनपदों और मौर्यों से जुड़े) मुख्य रूप से चांदी के बने थे, हालांकि कुछ तांबे के सिक्के भी मौजूद थे।"
)

# 24
add_root_mcq(
    "Which external source mentions the existence of a highly organized Mauryan city administration and seven distinct castes in Indian society during 300 BCE?",
    "कौन सा बाहरी स्रोत 300 ईसा पूर्व के दौरान भारतीय समाज में एक अत्यधिक संगठित मौर्य नगर प्रशासन और सात अलग-अलग जातियों के अस्तित्व का उल्लेख करता है?",
    ["Xuanzang's travelogue", "Al-Biruni's Kitab-ul-Hind", "Megasthenes' Indica", "Pliny's Natural History"],
    ["ह्वेनसांग का यात्रा वृत्तांत", "अल-बिरूनी की किताब-उल-हिंद", "मेगस्थनीज की 'इंडिका'", "प्लिनी का 'प्राकृतिक इतिहास'"],
    2,
    "Megasthenes, the Greek ambassador to the court of Chandragupta Maurya, described Pataliputra's administration and the seven-caste system in his book Indica.",
    "चंद्रगुप्त मौर्य के दरबार में यूनानी राजदूत मेगस्थनीज ने अपनी पुस्तक इंडिका में पाटलिपुत्र के प्रशासन और सात-जाति व्यवस्था का वर्णन किया था।"
)

# 25
add_root_mcq(
    "In the context of prehistoric archaeological records, what are 'Phytoliths'?",
    "प्रागैतिहासिक पुरातात्विक अभिलेखों के संदर्भ में 'फाइटोलिथ' (Phytoliths) क्या हैं?",
    ["Petrified wooden handles of prehistoric stone axes.", "Microscopic silica structures formed within plant tissues that survive after decay.", "Fossilized animal droppings used to determine diet.", "Engraved rock surfaces found in Neolithic caves."],
    ["प्रागैतिहासिक पाषाण कुल्हाड़ियों के जीवाश्मीकृत लकड़ी के हत्थे।", "पौधों के ऊतकों के भीतर बनने वाली सूक्ष्म सिलिका संरचनाएं जो सड़ने के बाद भी बची रहती हैं।", "आहार का निर्धारण करने के लिए उपयोग किए जाने वाले जीवाश्मीकृत जानवरों के गोबर।", "नवपाषाणकालीन गुफाओं में पाई जाने वाली उत्कीर्ण चट्टानी सतहें।"],
    1,
    "Phytoliths are microscopic silica bodies deposited in plant cells. Because they are inorganic, they survive decay and help identify ancient crops and vegetation.",
    "फाइटोलिथ पौधों की कोशिकाओं में जमा सूक्ष्म सिलिका पिंड होते हैं। चूंकि वे अकार्बनिक होते हैं, वे क्षय से बच जाते हैं और प्राचीन फसलों तथा वनस्पतियों की पहचान करने में मदद करते हैं।"
)

# 26
add_root_mcq(
    "Which archaeological site in India provides the earliest evidence of cultivated rice in the Ganga Valley, dated to c. 9000-8000 BCE?",
    "भारत का कौन सा पुरातात्विक स्थल गंगा घाटी में खेती किए जाने वाले चावल का सबसे पुराना साक्ष्य प्रदान करता है, जो लगभग 9000-8000 ईसा पूर्व का है?",
    ["Koldihwa", "Mehrgarh", "Lahuradewa", "Chirand"],
    ["कोल्डिहवा", "मेहरगढ़", "लहुरादेवा", "चिरांद"],
    2,
    "Lahuradewa in Sant Kabir Nagar district, UP, has pushed back the antiquity of rice cultivation in South Asia to around 9000-8000 BCE.",
    "उत्तर प्रदेश के संत कबीर नगर जिले में लहुरादेवा ने दक्षिण एशिया में चावल की खेती की प्राचीनता को लगभग 9000-8000 ईसा पूर्व तक पीछे धकेल दिया है।"
)

# 27
add_root_mcq(
    "The study of ancient handwriting, scripts, and their historical development over time is called:",
    "प्राचीन हस्तलेखन, लिपियों और समय के साथ उनके ऐतिहासिक विकास के अध्ययन को क्या कहा जाता है?",
    ["Epigraphy", "Numismatics", "Palaeography", "Palaeozoology"],
    ["अभिलेखशास्त्र", "मुद्राशास्त्र", "पुरालेखशास्त्र (Palaeography)", "पुराप्राणीशास्त्र"],
    2,
    "Palaeography is the study of ancient writing systems, decipherment, and the evolution of historical scripts over time.",
    "पुरालेखशास्त्र (Palaeography) प्राचीन लेखन प्रणालियों, उनके पढ़ने की विधि और समय के साथ ऐतिहासिक लिपियों के विकास का अध्ययन है।"
)

# 28
add_root_mcq(
    "Which Roman writer, in his book 'Naturalis Historia', famously lamented the massive drain of gold from the Roman Empire to India due to luxury trade?",
    "किस रोमन लेखक ने अपनी पुस्तक 'नेचुरलिस हिस्टोरिया' में विलासिता के व्यापार के कारण रोमन साम्राज्य से भारत में सोने के भारी बहाव पर गहरा दुख व्यक्त किया था?",
    ["Ptolemy", "Megasthenes", "Pliny the Elder", "Arrian"],
    ["टॉलेमी", "मेगस्थनीज", "प्लिनी द एल्डर (Pliny)", "एरियन"],
    2,
    "Pliny the Elder, writing in the 1st century CE, complained about the trade deficit, stating that India drained Rome of 50 million sesterces annually.",
    "पहली शताब्दी ईस्वी में लिखते हुए प्लिनी द एल्डर ने व्यापार घाटे के बारे में शिकायत की थी, जिसमें कहा गया था कि भारत ने प्रतिवर्ष रोम से 5 करोड़ सेस्टर्स (मुद्रा) खींचे।"
)

# 29
add_root_mcq(
    "The earliest deciphered bilingual and biscriptual inscription found in South Asia is the Kandahar Inscription of which ruler?",
    "दक्षिण एशिया में पाया गया सबसे पहला पढ़ा गया द्विभाषी और द्विलिपि अभिलेख किस शासक का कंधार अभिलेख है?",
    ["Kanishka", "Rudradaman", "Ashoka", "Samudragupta"],
    ["कनिष्क", "रुद्रदामन", "अशोक", "समुद्रगुप्त"],
    2,
    "Emperor Ashoka's Kandahar inscription was written in Greek and Aramaic languages, reflecting his policy of Dhamma to western frontiers.",
    "सम्राट अशोक का कंधार अभिलेख ग्रीक और अरामी भाषाओं में लिखा गया था, जो पश्चिमी सीमाओं पर उनकी धम्म की नीति को दर्शाता है।"
)

# 30
add_root_mcq(
    "Which archaeological excavation methodology, using baulks between trench squares to keep stratigraphic profiles visible, was introduced to India by Mortimer Wheeler?",
    "पुरातात्विक उत्खनन की किस पद्धति को मॉर्टिमर व्हीलर द्वारा भारत में पेश किया गया था, जिसमें स्तरविन्यास प्रोफाइल को दृश्यमान रखने के लिए खाइयों के बीच 'बाल्क' (मिट्टी की दीवारें) का उपयोग किया जाता है?",
    ["Grid-System Excavation", "Open-Area Horizontal Excavation", "Deep Vertical Shafting", "Step Trenching"],
    ["ग्रिड-सिस्टम उत्खनन", "ओपन-एरिया क्षैतिज उत्खनन", "गहरी ऊर्ध्वाधर शाफ्टिंग", "स्टेप ट्रेंचिंग"],
    0,
    "Mortimer Wheeler introduced the Grid-System method in 1944 to ensure stratigraphical control and preserve vertical earth walls for analysis.",
    "मॉर्टिमर व्हीलर ने स्तरविन्यास नियंत्रण सुनिश्चित करने और विश्लेषण के लिए ऊर्ध्वाधर मिट्टी की दीवारों को सुरक्षित रखने के लिए 1944 में ग्रिड-सिस्टम विधि की शुरुआत की थी।"
)

# 31
add_root_mcq(
    "Which classical text, compiled by Claudius Ptolemy in the 2nd century CE, contains a detailed geographic catalog and early map of India's rivers and ports?",
    "दूसरी शताब्दी ईस्वी में क्लॉडियस टॉलेमी द्वारा संकलित किस शास्त्रीय ग्रंथ में भारत की नदियों और बंदरगाहों का विस्तृत भौगोलिक विवरण और प्रारंभिक मानचित्र शामिल है?",
    ["Periplus of the Erythraean Sea", "Geographike Hyphegesis (Geography)", "Indica", "Naturalis Historia"],
    ["पेरिप्लस ऑफ द एरिथ्रियन सी", "ज्योग्राफी (Geographike Hyphegesis)", "इंडिका", "नेचुरलिस हिस्टोरिया"],
    1,
    "Ptolemy's Geography (2nd century CE) provided coordinates and geographical details of Indian coastal ports and inland rivers.",
    "टॉलेमी की ज्योग्राफी (दूसरी शताब्दी ईस्वी) ने भारतीय तटीय बंदरगाहों और अंतर्देशीय नदियों के निर्देशांक और भौगोलिक विवरण प्रदान किए थे।"
)

# 32
add_root_mcq(
    "The Buddhist Jataka tales (part of Sutta Pitaka) are historically valuable because they provide detailed descriptions of:",
    "बौद्ध जातक कथाएँ (सुत्त पिटक का हिस्सा) ऐतिहासिक रूप से मूल्यवान हैं क्योंकि वे किसका विस्तृत विवरण प्रदान करती हैं?",
    ["Pre-historic stone tool manufacturing methods.", "Early trade guilds, caravan routes, and craft specializations in 6th century BCE.", "Ashokan administrative codes and pillar inscriptions.", "Rigvedic tribal wars and rituals."],
    ["प्रागैतिहासिक पाषाण उपकरण निर्माण विधियों का।", "6ठी शताब्दी ईसा पूर्व में शुरुआती व्यापारिक संघों, कारवां मार्गों और शिल्प विशेषज्ञता का।", "अशोक के प्रशासनिक कोड और स्तंभ लेखों का।", "ऋग्वैदिक जनजातीय युद्धों और अनुष्ठानों का।"],
    1,
    "The 547 Jataka tales describe the former births of Buddha, reflecting contemporary urban and rural socio-economic life, trade, and guilds.",
    "547 जातक कथाएँ बुद्ध के पूर्व जन्मों का वर्णन करती हैं, जो समकालीन शहरी और ग्रामीण सामाजिक-आर्थिक जीवन, व्यापार और शिल्प श्रेणियों को दर्शाती हैं।"
)

# 33
add_root_mcq(
    "What kind of environmental information is primary reconstructed using Palynological analysis in Indian prehistoric archaeology?",
    "भारतीय प्रागैतिहासिक पुरातत्व में परागकण विश्लेषण (Palynological analysis) का उपयोग करके किस प्रकार की पर्यावरणीय जानकारी का मुख्य रूप से पुनर्निर्माण किया जाता है?",
    ["Changes in prehistoric forest density and precipitation cycles over time.", "The domestication history of local cattle varieties.", "The absolute age of pottery fragments.", "The speed of river siltation in alluvial basins."],
    ["समय के साथ प्रागैतिहासिक वन घनत्व और वर्षा चक्र में परिवर्तन।", "स्थानीय मवेशियों की किस्मों के पालतू बनाने का इतिहास।", "मिट्टी के बर्तनों के टुकड़ों की निरपेक्ष आयु।", "जलोढ़ घाटियों में नदी के गाद जमा होने की गति।"],
    0,
    "Palynology reconstructs past climate and vegetation patterns by isolating ancient pollen grains preserved in lake beds or soil horizons.",
    "परागकण विश्लेषण झील के तलवों या मिट्टी में सुरक्षित प्राचीन परागकणों को अलग करके अतीत की जलवायु और वनस्पति पैटर्न का पुनर्निर्माण करता है।"
)

# 34
add_root_mcq(
    "Which archaeological site in Gujarat, excavated by H. D. Sankalia, yielded Mesolithic burials and human skeletons showing physical traits linked to Northeast Africa?",
    "गुजरात का कौन सा पुरातात्विक स्थल, जिसका उत्खनन एच. डी. संकलिया द्वारा किया गया था, से मध्यपाषाणकालीन कब्रें और मानव कंकाल मिले हैं जो उत्तर-पूर्वी अफ्रीका से जुड़े शारीरिक लक्षणों को दर्शाते हैं?",
    ["Bagor", "Langhnaj", "Lothal", "Rojdi"],
    ["बागोर", "लघनाज", "लोथल", "रोजड़ी"],
    1,
    "Langhnaj in Gujarat yielded microlithic tools, animal bones, and 14 human skeletons showing physical affinities to Hamitic populations of Africa.",
    "गुजरात में लघनाज से माइक्रोलिथिक उपकरण, जानवरों की हड्डियां और 14 मानव कंकाल मिले हैं जो अफ्रीका की हेमिटिक आबादी के साथ शारीरिक समानताएं दिखाते हैं।"
)

# 35
add_root_mcq(
    "Who is credited with the systematic discovery and recording of the first prehistoric site in India at Lingsugur, Karnataka in 1842?",
    "1842 में कर्नाटक के लिंगसुगुर में भारत के पहले प्रागैतिहासिक स्थल की व्यवस्थित खोज और रिकॉर्डिंग का श्रेय किसे दिया जाता है?",
    ["Robert Bruce Foote", "Dr. Primrose", "Mortimer Wheeler", "John Marshall"],
    ["रॉबर्ट ब्रूस फुट", "डॉ. प्राइमरोज़ (Dr. Primrose)", "मॉर्टिमर व्हीलर", "जॉन मार्शल"],
    1,
    "In 1842, Dr. Primrose discovered Palaeolithic stone implements (knives and arrowheads) at Lingsugur in Raichur district of Karnataka.",
    "1842 में, डॉ. प्राइमरोज़ ने कर्नाटक के रायचूर जिले के लिंगसुगुर में पुरापाषाणकालीन पाषाण उपकरणों (चाकू और तीरों) की खोज की थी।"
)

# 36
add_root_mcq(
    "In which of the following regions are Lower Palaeolithic stone tools completely absent due to lack of raw stone materials and heavy deposition of river silt?",
    "निम्नलिखित में से किस क्षेत्र में कच्चे पत्थर की कमी और नदी के गाद के भारी जमाव के कारण निम्न पुरापाषाण काल के उपकरण पूरी तरह से अनुपस्थित हैं?",
    ["Belan Valley", "Indo-Gangetic Plains", "Hunsgi Valley", "Deccan Plateau"],
    ["बेलन घाटी", "गंगा-यमुना के मैदानी भाग", "हुन्सगी घाटी", "दक्कन का पठार"],
    1,
    "The Indo-Gangetic plains are rich in soft silt and sand, lacking quartzite gravels required for tool making, hence Lower Palaeolithic sites are absent there.",
    "गंगा-यमुना के मैदान कोमल जलोढ़ मिट्टी और रेत से समृद्ध हैं, वहाँ उपकरण बनाने के लिए आवश्यक क्वार्ट्जाइट पत्थरों की कमी है, इसलिए वहां निम्न पुरापाषाण स्थल अनुपस्थित हैं।"
)

# 37
add_root_mcq(
    "Which literary genre contains historical genealogies of early dynasties and descriptions of traditional ancient geography in post-Vedic India?",
    "उत्तर-वैदिक भारत में प्रारंभिक राजवंशों की ऐतिहासिक वंशावली और पारंपरिक प्राचीन भूगोल का विवरण किस साहित्यिक विधा में मिलता है?",
    ["Upanishads", "Aranyakas", "Puranas", "Brahmanas"],
    ["उपनिषद", "आरण्यक", "पुराण", "ब्राह्मण"],
    2,
    "The 18 Mahapuranas contain dynastic lineages, mythological history, and geography, serving as important source materials for early history.",
    "18 महापुराणों में राजवंशों की वंशावली, पौराणिक इतिहास और भूगोल शामिल हैं, जो प्रारंभिक इतिहास के लिए महत्वपूर्ण स्रोत सामग्री के रूप में कार्य करते हैं।"
)

# 38
add_root_mcq(
    "What is the effective absolute dating limit of the Radiocarbon (C-14) method for organic materials?",
    "जैविक सामग्रियों के लिए रेडियोकार्बन (C-14) पद्धति की प्रभावी निरपेक्ष काल-निर्धारण सीमा क्या है?",
    ["Approximately 5,000 years", "Approximately 50,000 years", "Approximately 500,000 years", "Approximately 5,000,000 years"],
    ["लगभग 5,000 वर्ष", "लगभग 50,000 वर्ष", "लगभग 5,00,000 वर्ष", "लगभग 50,00,000 वर्ष"],
    1,
    "Due to the relatively short half-life of Carbon-14 (5,730 years), active C-14 levels become too low to measure accurately after approximately 50,000 years.",
    "कार्बन-14 की अपेक्षाकृत कम अर्ध-आयु (5,730 वर्ष) के कारण, लगभग 50,000 वर्षों के बाद C-14 का स्तर सटीक रूप से मापने के लिए बहुत कम हो जाता है।"
)

# 39
add_root_mcq(
    "Which archaeological site in South Asia represents the earliest transition from foraging to pastoralism, containing animal bones of domesticated sheep and goats around 7000 BCE?",
    "दक्षिण एशिया का कौन सा पुरातात्विक स्थल शिकार से पशुपालन में संक्रमण का सबसे पहला प्रतिनिधित्व करता है, जिसमें 7000 ईसा पूर्व के आसपास पालतू भेड़ों और बकरियों की हड्डियाँ मिली हैं?",
    ["Adamgarh", "Bagor", "Mehrgarh", "Lahuradewa"],
    ["आदमगढ़", "बागोर", "मेहरगढ़", "लहुरादेवा"],
    2,
    "Mehrgarh Period I (Neolithic) shows a gradual shift from hunting wild gazelles to raising domesticated humped cattle (zebu), sheep, and goats.",
    "मेहरगढ़ काल I (नवपाषाण) जंगली गज़लों के शिकार से पालतू कूबड़ वाले मवेशियों (जेबू), भेड़ों और बकरियों के पालन की ओर एक क्रमिक बदलाव दिखाता है।"
)

# 40
add_root_mcq(
    "The scientific study of ancient animal bones excavated from archaeological sites to understand hunting habits and domestication is called:",
    "शिकार की आदतों और पशुपालन को समझने के लिए पुरातात्विक स्थलों से खोदी गई प्राचीन जानवरों की हड्डियों के वैज्ञानिक अध्ययन को क्या कहा जाता है?",
    ["Palaeobotany", "Palaeozoology (Zooarchaeology)", "Palynology", "Palaeography"],
    ["पुरावनस्पतिशास्त्र", "पुराप्राणीशास्त्र (Zooarchaeology)", "परागकण विश्लेषण", "पुरालेखशास्त्र"],
    1,
    "Palaeozoology or Zooarchaeology is the study of animal remains from archaeological sites, helping reconstruct human-animal relationships in the past.",
    "पुराप्राणीशास्त्र या चिड़ियाघर-पुरातत्व (Zooarchaeology) पुरातात्विक स्थलों से जानवरों के अवशेषों का अध्ययन है, जो अतीत में मानव-पशु संबंधों के पुनर्निर्माण में मदद करता है।"
)

# 41
add_root_mcq(
    "Which of the following early coins bear the portraits and names of specific rulers, representing a massive shift from punch-marked designs?",
    "निम्नलिखित में से किस प्रारंभिक सिक्के पर विशिष्ट शासकों के चित्र और नाम अंकित हैं, जो आहत सिक्कों (punch-marked) के डिजाइनों से एक बड़ा बदलाव प्रदर्शित करते हैं?",
    ["Punch-marked coins", "Indo-Greek coins", "Gupta gold coins", "Cast copper coins"],
    ["आहत सिक्के (Punch-marked)", "हिंद-यवन सिक्के (Indo-Greek)", "गुप्त स्वर्ण सिक्के", "तांबे के ढाले हुए सिक्के"],
    1,
    "The Indo-Greeks introduced bilingual, bi-scriptural, and portrait coins in India (2nd Century BCE), allowing precise identification of kings.",
    "हिंद-यवन (Indo-Greeks) शासकों ने भारत में (दूसरी शताब्दी ईसा पूर्व) द्विभाषी, द्विलिपि और चित्र वाले सिक्कों की शुरुआत की, जिससे राजाओं की सटीक पहचान संभव हुई।"
)

# 42
add_root_mcq(
    "Which ancient Greek historian, known as the 'Father of History', wrote about India in his work 'Histories' during the 5th century BCE?",
    "किस प्राचीन यूनानी इतिहासकार ने, जिसे 'इतिहास का जनक' कहा जाता है, 5वीं शताब्दी ईसा पूर्व के दौरान अपने ग्रंथ 'इतिहास' (Histories) में भारत के बारे में लिखा था?",
    ["Arrian", "Herodotus", "Ctesias", "Strabo"],
    ["एरियन", "हेरोडोटस", "क्टेसियस", "स्ट्रैबो"],
    1,
    "Herodotus mentioned that India was the 20th satrapy (province) of the Persian Achaemenid Empire in his book Histories.",
    "हेरोडोटस ने अपनी पुस्तक हिस्टोरीज़ में उल्लेख किया है कि भारत फारसी हखामनी (Achaemenid) साम्राज्य का 20वां क्षत्रप (प्रांत) था।"
)

# 43
add_root_mcq(
    "In archaeological investigations, what is 'Seriation'?",
    "पुरातात्विक अन्वेषणों में 'श्रेणीकरण' (Seriation) क्या है?",
    ["An absolute dating method using radioactive carbon decay.", "A relative dating technique where artifacts from numerous sites of the same culture are placed in chronological order based on style shifts.", "The process of sieving soil to find micro-artifacts.", "The chemical cleaning of metal coins to read inscriptions."],
    ["रेडियोधर्मी कार्बन क्षय का उपयोग करने वाली एक निरपेक्ष तिथि निर्धारण विधि।", "एक सापेक्ष काल-निर्धारण तकनीक जहां एक ही संस्कृति के कई स्थलों की कलाकृतियों को शैलीगत बदलावों के आधार पर कालानुक्रमिक क्रम में रखा जाता है।", "सूक्ष्म-कलाकृतियों को खोजने के लिए मिट्टी को छानने की प्रक्रिया।", "अभिलेखों को पढ़ने के लिए धातु के सिक्कों की रासायनिक सफाई।"],
    1,
    "Seriation is a relative dating technique that sequences assemblies of artifacts (usually pottery) based on the assumption that stylistic trends rise, peak, and fall over time.",
    "श्रेणीकरण (Seriation) एक सापेक्ष तिथि निर्धारण technique है जो कलाकृतियों (आमतौर पर मिट्टी के बर्तनों) के समूहों को इस धारणा के आधार पर क्रमबद्ध करती है कि शैलीगत रुझान समय के साथ बढ़ते हैं, चरम पर पहुंचते हैं और फिर घटते हैं।"
)

# 44
add_root_mcq(
    "Which scientific method is utilized to determine the exact calendar dates of wooden structures by measuring the variations in tree growth rings?",
    "पेड़ के विकास के छल्लों (tree-rings) में भिन्नता को मापकर लकड़ी की संरचनाओं की सटीक कैलेंडर तिथियां निर्धारित करने के लिए किस वैज्ञानिक पद्धति का उपयोग किया जाता है?",
    ["OSL Dating", "Dendrochronology", "Thermoluminescence", "Uranium-Series"],
    ["OSL डेटिंग", "वृक्षवलय कालानुक्रम (Dendrochronology)", "थर्मोलुमिनेसेंस", "यूरेनियम-श्रृंखला"],
    1,
    "Dendrochronology is the scientific study of dating tree-rings, reflecting past climate variations and providing absolute dates for wooden remains.",
    "वृक्षवलय कालानुक्रम (Dendrochronology) पेड़ के छल्लों के काल-निर्धारण का वैज्ञानिक अध्ययन है, जो अतीत की जलवायु विविधताओं को दर्शाता है और लकड़ी के अवशेषों के लिए निरपेक्ष तिथियां प्रदान करता है।"
)

# 45
add_root_mcq(
    "The famous 'Junagadh Rock Inscription' of Rudradaman (c. 150 CE) is historically significant because it is the first major long inscription written in:",
    "रुद्रदामन का प्रसिद्ध 'जूनागढ़ शिलालेख' (लगभग 150 ईस्वी) ऐतिहासिक रूप से महत्वपूर्ण है क्योंकि यह निम्नलिखित में लिखा गया पहला बड़ा लंबा अभिलेख है:",
    ["Prakrit language", "Sanskrit language", "Pali language", "Greek language"],
    ["प्राकृत भाषा", "संस्कृत भाषा", "पालि भाषा", "ग्रीक भाषा"],
    1,
    "The Junagadh Inscription of Saka ruler Rudradaman is the earliest major public royal inscription written in chaste classical Sanskrit language.",
    "शक शासक रुद्रदामन का जूनागढ़ अभिलेख शुद्ध शास्त्रीय संस्कृत भाषा में लिखा गया सबसे पहला बड़ा सार्वजनिक शाही अभिलेख है।"
)

# 46
add_root_mcq(
    "Which archaeological site in Madhya Pradesh represents a continuous sequence of human occupation from the Upper Palaeolithic to the Historic periods, preserved in limestone shelters?",
    "मध्य प्रदेश का कौन सा पुरातात्विक स्थल चूना पत्थर के आश्रयों में सुरक्षित उच्च पुरापाषाण काल से ऐतिहासिक काल तक मानव निवास के एक निरंतर अनुक्रम का प्रतिनिधित्व करता है?",
    ["Adamgarh", "Bhimbetka", "Bagor", "Mehrgarh"],
    ["आदमगढ़", "भीमबेटका", "बागोर", "मेहरगढ़"],
    1,
    "Bhimbetka shelters in MP show a continuous archaeological sequence from the Acheulian/Palaeolithic period up to the historical era.",
    "मध्य प्रदेश में भीमबेटका आश्रय स्थल एशुलेयिन/पुरापाषाण काल से लेकर ऐतिहासिक युग तक का एक निरंतर पुरातात्विक अनुक्रम दिखाते हैं।"
)

# 47
add_root_mcq(
    "The gold coins issued by the Gupta emperors, characterized by high artistic quality and representations of sacrifices or musical acts, were known in contemporary records as:",
    "गुप्त सम्राटों द्वारा जारी किए गए सोने के सिक्के, जो उच्च कलात्मक गुणवत्ता और यज्ञों या संगीत गतिविधियों के प्रदर्शन की विशेषता रखते थे, समकालीन अभिलेखों में किस नाम से जाने जाते थे?",
    ["Rupaka", "Karshapana", "Dinara", "Jital"],
    ["रूपक", "कार्षापण", "दीनार (Dinara)", "जीतल"],
    2,
    "Gupta gold coins were referred to as Dinaras (derived from Roman Denarius) in contemporary inscriptions. Gupta silver coins were called Rupakas.",
    "गुप्त काल के सोने के सिक्कों को समकालीन अभिलेखों में दीनार (रोमन डेनारियस से लिया गया) कहा जाता था। गुप्तकालीन चांदी के सिक्कों को रूपक कहा जाता था।"
)

# 48
add_root_mcq(
    "The non-destructive absolute dating method Optically Stimulated Luminescence (OSL) is primarily used in Indian prehistoric contexts to date:",
    "गैर-विनाशकारी निरपेक्ष काल-निर्धारण पद्धति ऑप्टिकली स्टिम्युलेटेड ल्यूमिनेसेंस (OSL) का उपयोग मुख्य रूप से भारतीय प्रागैतिहासिक संदर्भों में किसके काल-निर्धारण के लिए किया जाता है?",
    ["Organic bone collagen", "Sediment layers of sand or silt enclosing stone tools", "Copper slag residues from kilns", "Volcanic basalt boulders"],
    ["जैविक हड्डी कोलेजन", "पत्थर के औजारों को घेरने वाली रेत या गाद की तलछट परतें", "भट्टियों से निकले तांबे के धातुमल (slag) के अवशेष", "ज्वालामुखी बेसाल्ट चट्टानें"],
    1,
    "OSL dating determines the last time mineral sediment grains (like quartz sand) were exposed to sunlight before burial, dating the soil layer enclosing tools.",
    "OSL डेटिंग यह निर्धारित करती है कि दफन होने से पहले खनिज तलछट के कणों (जैसे क्वार्ट्ज रेत) को आखिरी बार कब सूर्य के प्रकाश के संपर्क में लाया गया था, जिससे उपकरणों को घेरने वाली मिट्टी की परत की तिथि निर्धारित होती है।"
)

# 49
add_root_mcq(
    "Which Buddhist Pali canon text contains detailed historical listings of major ancient Indian geography, clans, and kingdoms (Mahajanapadas)?",
    "किस बौद्ध पाली ग्रंथ में प्रमुख प्राचीन भारतीय भूगोल, कुलों और साम्राज्यों (महाजनपदों) की विस्तृत ऐतिहासिक सूची शामिल है?",
    ["Vinaya Pitaka", "Anguttara Nikaya", "Abhidhamma Pitaka", "Mahavamsa"],
    ["विनय पिटक", "अंगुत्तर निकाय (Anguttara Nikaya)", "अभिधम्म पिटक", "महावंश"],
    1,
    "The Anguttara Nikaya (a branch of Sutta Pitaka) contains the famous list of the sixteen great kingdoms (Sodasa Mahajanapadas) of the 6th century BCE.",
    "अंगुत्तर निकाय (सुत्त पिटक की एक शाखा) में 6ठी शताब्दी ईसा पूर्व के सोलह महान साम्राज्यों (षोडश महाजनपद) की प्रसिद्ध सूची शामिल है।"
)

# 50
add_root_mcq(
    "The first major archaeological excavation of a Neolithic site in Kashmir, revealing pit-dwellings and unique animal burials, was conducted at which site?",
    "कश्मीर में नवपाषाणकालीन स्थल का पहला बड़ा पुरातात्विक उत्खनन किस स्थल पर किया गया था, जिसमें गर्त-निवास (pit-dwellings) और अद्वितीय पशु दफन का पता चला था?",
    ["Gufkral", "Burzahom", "Martand", "Harwan"],
    ["गुफकराल", "बुर्जहोम (Burzahom)", "मार्तंड", "हरवन"],
    1,
    "Burzahom near Srinagar was excavated by De Terra and Paterson in 1935, revealing semi-subterranean pits built to survive cold winters and dog burials.",
    "श्रीनगर के निकट बुर्जहोम का उत्खनन 1935 में डी टेरा और पीटरसन द्वारा किया गया था, जिसमें ठंडी सर्दियों से बचने के लिए बनाए गए अर्ध-भूमिगत गड्ढों और कुत्तों को दफनाने के साक्ष्य मिले थे।"
)

# ==========================================
# 10 MOCK QUESTIONS (INTEGRATED & MULTI-STATEMENT)
# ==========================================

# Mock 1
add_mock_mcq(
    "Consider the following statements regarding early archaeological excavation methodologies in India:\\n1. John Marshall advocated horizontal excavation, which exposed structural plans but mixed up stratigraphical layers.\\n2. Mortimer Wheeler introduced the grid system of vertical trenches to maintain stratigraphical control.\\n3. The grid method uses 'baulks' of earth between trenches to serve as visible stratigraphic control walls.\\nWhich of the statements given above are correct?",
    "भारत में प्रारंभिक पुरातात्विक उत्खनन पद्धतियों के संबंध में निम्नलिखित कथनों पर विचार करें:\\n1. जॉन मार्शल ने क्षैतिज उत्खनन (horizontal excavation) की वकालत की, जिसने संरचनात्मक योजनाओं को उजागर किया लेकिन स्तरविन्यास परतों को मिला दिया।\\n2. मॉर्टिमर व्हीलर ने स्तरविन्यास नियंत्रण बनाए रखने के लिए ऊर्ध्वाधर खाइयों की ग्रिड प्रणाली की शुरुआत की।\\n3. ग्रिड पद्धति खाइयों के बीच मिट्टी की दीवारों ('baulks') का उपयोग करती है जो दृश्य स्तरविन्यास नियंत्रण दीवारों के रूप में कार्य करती हैं।\\nऊपर दिए गए कथनों में से कौन से सही हैं?",
    ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
    ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
    3,
    "All statements are correct. John Marshall dug horizontally without keeping stratigraphy separate, which Mortimer Wheeler corrected in 1944 by introducing the grid system with earth baulks to track geological strata.",
    "सभी कथन सही हैं। जॉन मार्शल ने स्तरविन्यास को अलग रखे बिना क्षैतिज रूप से खुदाई की, जिसे मॉर्टिमर व्हीलर ने 1944 में भूवैज्ञानिक स्तरों को ट्रैक करने के लिए मिट्टी के बाल्क (baulks) के साथ ग्रिड प्रणाली की शुरुआत करके सुधारा था।"
)

# Mock 2
add_mock_mcq(
    "In the context of reconstructing prehistoric palaeo-environments and human adaptation, consider the following matches:\\n1. Palynology : Study of fossil pollen to reconstruct climatic forest shifts.\\n2. Palaeozoology : Study of animal bones to determine herd mortality profiles and domestication.\\n3. Phytolith analysis : Study of microscopic mineral particles in plant cells to identify crop domestication.\\nWhich of the pairs given above are correctly matched?",
    "प्रागैतिहासिक पुरा-पर्यावरण और मानव अनुकूलन के पुनर्निर्माण के संदर्भ में, निम्नलिखित मिलानों पर विचार करें:\\n1. परागकण विश्लेषण (Palynology) : जलवायु वन बदलावों के पुनर्निर्माण के लिए जीवाश्म पराग का अध्ययन।\\n2. पुराप्राणीशास्त्र (Palaeozoology) : झुंड की मृत्यु दर प्रोफाइल और पालतू बनाने की स्थिति का निर्धारण करने के लिए जानवरों की हड्डियों का अध्ययन।\\n3. फाइटोलिथ विश्लेषण (Phytolith analysis) : फसल के घरेलूकरण की पहचान करने के लिए पौधों की कोशिकाओं में सूक्ष्म खनिज कणों का अध्ययन।\\nऊपर दिए गए युग्मों में से कौन से सही सुमेलित हैं?",
    ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
    ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
    3,
    "All three matches are correct scientific techniques used in modern environmental archaeology to reconstruct prehistoric climates, animal husbandry, and agricultural practices.",
    "आधुनिक पर्यावरणीय पुरातत्व में प्रागैतिहासिक जलवायु, पशुपालन और कृषि प्रथाओं के पुनर्निर्माण के लिए उपयोग की जाने वाली तीनों वैज्ञानिक तकनीकें सही सुमेलित हैं।"
)

# Mock 3
add_mock_mcq(
    "Consider the following statements regarding the decipherment and historical utility of Indian scripts:\\n1. The Harappan script is written in boustrophedon style and represents the earliest deciphered script of India.\\n2. James Prinsep deciphered Brahmi script by comparing bilingual Indo-Greek coins bearing Greek and Brahmi legends.\\n3. Ashoka's inscriptions in northwestern India (Shahbazgarhi and Mansehra) were written in the Kharoshthi script.\\nWhich of the statements given above are correct?",
    "भारतीय लिपियों को पढ़ने और उनकी ऐतिहासिक उपयोगिता के संबंध में निम्नलिखित कथनों पर विचार करें:\\n1. हड़प्पा लिपि बूस्ट्रोफेडन (boustrophedon) शैली में लिखी गई है और यह भारत की सबसे पुरानी पढ़ी गई लिपि का प्रतिनिधित्व करती है।\\n2. जेम्स प्रिंसेप ने ग्रीक और ब्राह्मी लेखों वाले द्विभाषी हिंद-यवन सिक्कों की तुलना करके ब्राह्मी लिपि को पढ़ा था।\\n3. उत्तर-पश्चिमी भारत (शाहबाजगढ़ी और मनसेहरा) में अशोक के अभिलेख खरोष्ठी लिपि में लिखे गए थे।\\nऊपर दिए गए कथनों में से कौन से सही हैं?",
    ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
    ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
    1,
    "Statement 1 is incorrect because Harappan script is undeciphered. Statement 2 is correct (Prinsep compared names on Indo-Greek coins to learn the script values). Statement 3 is correct (Kharoshthi was used in the northwest frontiers).",
    "कथन 1 गलत है क्योंकि हड़प्पा लिपि अभी तक पढ़ी नहीं जा सकी है। कथन 2 सही है (प्रिंसेप ने लिपि के अक्षरों को सीखने के लिए हिंद-यवन सिक्कों पर नामों की तुलना की)। कथन 3 सही है (उत्तर-पश्चिमी सीमाओं में खरोष्ठी का उपयोग किया गया था)।"
)

# Mock 4
add_mock_mcq(
    "With reference to the chronological accounts left by early foreign visitors, consider the following statements:\\n1. Megasthenes claims that Indian society did not experience slavery or famine, which contradicts local Buddhist sources.\\n2. The anonymous author of the 'Periplus of the Erythraean Sea' details trade ports along both the western and eastern coasts of India.\\n3. Fa-Hien travelled to India during Harsha's reign and left a detailed account of the administrative structure of the empire.\\nWhich of the statements given above is/are correct?",
    "प्रारंभिक विदेशी आगंतुकों द्वारा छोड़े गए कालानुक्रमिक विवरणों के संदर्भ में, निम्नलिखित कथनों पर विचार करें:\\n1. मेगस्थनीज का दावा है कि भारतीय समाज में गुलामी या अकाल का अनुभव नहीं हुआ, जो स्थानीय बौद्ध स्रोतों का खंडन करता है।\\n2. 'पेरिप्लस ऑफ द एरिथ्रियन सी' के अज्ञात लेखक ने भारत के पश्चिमी और पूर्वी दोनों तटों के व्यापारिक बंदरगाहों का विस्तृत विवरण दिया है।\\n3. फाहियान ने हर्ष के शासनकाल के दौरान भारत की यात्रा की और साम्राज्य की प्रशासनिक संरचना का विस्तृत विवरण दिया।\\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 and 2 only", "2 and 3 only", "1 and 3 only", "2 only"],
    ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "केवल 2"],
    0,
    "Statements 1 and 2 are correct. Statement 3 is incorrect because Fa-Hien visited during Chandragupta II's Gupta reign, not Harsha's reign (which was visited by Hiuen Tsang).",
    "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि फाहियान ने चंद्रगुप्त द्वितीय के गुप्त शासनकाल के दौरान यात्रा की थी, न कि हर्ष के शासनकाल में (जिसमें ह्वेनसांग ने यात्रा की थी)।"
)

# Mock 5
add_mock_mcq(
    "Regarding the scientific dating of prehistoric and early historical sites, which of the following matches is/are correct?\\n1. Cosmogenic Nuclide Dating : Attirampakkam Acheulian tools (c. 1.5 MYA)\\n2. Thermoluminescence (TL) : Harappan pottery sequences\\n3. Radiocarbon (C-14) Dating : Neolithic Lahuradewa rice remains (c. 8000 BCE)\\nSelect the correct answer using the code given below:",
    "प्रागैतिहासिक और प्रारंभिक ऐतिहासिक स्थलों के वैज्ञानिक काल-निर्धारण के संबंध में, निम्नलिखित में से कौन सा/से मिलान सही है/हैं?\\n1. कॉस्मोजेनिक न्यूक्लाइड डेटिंग : अतिरामपक्कम एशुलेयिन उपकरण (लगभग 1.5 मिलियन वर्ष पूर्व)\\n2. थर्मोलुमिनेसेंस (TL) : हड़प्पा मिट्टी के बर्तनों के अनुक्रम\\n3. रेडियोकार्बन (C-14) डेटिंग : नवपाषाणकालीन लहुरादेवा चावल के अवशेष (लगभग 8000 ईसा पूर्व)\\nनीचे दिए गए कूट का उपयोग करके सही उत्तर चुनें:",
    ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
    ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
    3,
    "All three matches are correct. Cosmogenic nuclide burial dating was used for Attirampakkam tools. TL is standard for pottery. Radiocarbon was used on carbonized organic grains at Lahuradewa.",
    "तीनों मिलान सही हैं। अतिरामपक्कम उपकरणों के लिए कॉस्मोजेनिक न्यूक्लाइड दफन डेटिंग का उपयोग किया गया था। मिट्टी के बर्तनों के लिए TL मानक विधि है। लहुरादेवा में कोयलाकृत जैविक दानों पर रेडियोकार्बन का उपयोग किया गया था।"
)

# Mock 6
add_mock_mcq(
    "Consider the following statements regarding the evolution of coinage in ancient India:\\n1. Punch-marked coins carried no royal names or portraits, using only geometric and natural symbols.\\n2. Indo-Greeks introduced bilingual inscriptions containing Greek and Prakrit languages on coins.\\n3. The Kushana dynasty issued the largest number of copper coins and the first large-scale gold coinage in India.\\nWhich of the statements given above are correct?",
    "प्राचीन भारत में सिक्कों के विकास के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. आहत सिक्कों पर कोई शाही नाम या चित्र नहीं होते थे, केवल ज्यामितीय और प्राकृतिक प्रतीकों का उपयोग किया जाता था।\\n2. हिंद-यवन (Indo-Greeks) शासकों ने सिक्कों पर ग्रीक और प्राकृत भाषाओं वाले द्विभाषी अभिलेखों की शुरुआत की।\\n3. कुषाण राजवंश ने भारत में तांबे के सिक्कों की सबसे बड़ी संख्या और पहला बड़े पैमाने पर सोने का सिक्का जारी किया।\\nऊपर दिए गए कथनों में से कौन से सही हैं?",
    ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
    ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
    3,
    "All statements are correct. Punch-marked coins represent the earliest trade coins with symbolic markings. Indo-Greeks introduced bilingual portrait coins. Kushanas minted extensive gold coins for international trade and large amounts of copper for local trade.",
    "सभी कथन सही हैं। आहत सिक्के प्रतीकात्मक चिह्नों वाले सबसे शुरुआती व्यापारिक सिक्कों का प्रतिनिधित्व करते हैं। हिंद-यवनों ने द्विभाषी चित्र वाले सिक्कों की शुरुआत की। कुषाणों ने अंतर्राष्ट्रीय व्यापार के लिए बड़े पैमाने पर सोने के सिक्के और स्थानीय व्यापार के लिए बड़ी मात्रा में तांबे के सिक्के ढाले।"
)

# Mock 7
add_mock_mcq(
    "Consider the following statements regarding literary sources and their historical reliability for reconstructing proto-history:\\n1. Rigvedic hymns describe a purely nomadic pastoral society residing primarily in the Ganga-Yamuna Doab.\\n2. The Later Vedic texts describe iron tools and expansion of settlements into the dense forests of the middle Ganga valley.\\n3. Ancient Puranic texts contain lists of historical kings and lineages that have been verified using epigraphical records.\\nWhich of the statements given above are correct?",
    "आदि-इतिहास (proto-history) के पुनर्निर्माण के लिए साहित्यिक स्रोतों और उनकी ऐतिहासिक विश्वसनीयता के संबंध में निम्नलिखित कथनों पर विचार करें:\\n1. ऋग्वैदिक भजनों में मुख्य रूप से गंगा-यमुना दोआब में रहने वाले एक शुद्ध रूप से खानाबदोश समाज का वर्णन है।\\n2. उत्तर-वैदिक ग्रंथ लोहे के उपकरणों और मध्य गंगा घाटी के घने जंगलों में बस्तियों के विस्तार का वर्णन करते हैं।\\n3. प्राचीन पौराणिक ग्रंथों में ऐतिहासिक राजाओं और वंशावलियों की सूचियाँ शामिल हैं जिन्हें अभिलेखीय अभिलेखों का उपयोग करके सत्यापित किया गया है।\\nऊपर दिए गए कथनों में से कौन से सही हैं?",
    ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
    ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
    1,
    "Statement 1 is incorrect because the Rig Veda describes the Sapta Sindhu (Punjab/Indus) region, not the Ganga-Yamuna Doab. Statements 2 and 3 are correct.",
    "कथन 1 गलत है क्योंकि ऋग्वेद सप्त सिंधु (पंजाब/सिंधु) क्षेत्र का वर्णन करता है, न कि गंगा-यमुना दोआब का। कथन 2 और 3 सही हैं।"
)

# Mock 8
add_mock_mcq(
    "With reference to the epigraphical evidence in India, which of the following is/are correct limitation(s) of inscriptions as absolute historical sources?\\n1. Inscriptions can be damaged, erased, or undergo natural weathering over centuries.\\n2. Royal prasastis (eulogies) often exaggerate achievements of patrons and ignore defeats.\\n3. Inscriptions only reflect the perspectives of the literate ruling elite, neglecting the lives of common masses.\\nSelect the correct answer using the code given below:",
    "भारत में अभिलेखीय साक्ष्यों के संदर्भ में, निम्नलिखित में से कौन सी अभिलेखों की पूर्ण ऐतिहासिक स्रोतों के रूप में सही सीमा/सीमाएं हैं?\\n1. सदियों से अभिलेख क्षतिग्रस्त हो सकते हैं, मिटाए जा सकते हैं या प्राकृतिक क्षरण का शिकार हो सकते हैं।\\n2. शाही प्रशस्तियाँ अक्सर संरक्षकों की उपलब्धियों को बढ़ा-चढ़ाकर पेश करती हैं और पराजयों को नजरअंदाज करती हैं।\\n3. अभिलेख केवल साक्षर शासक वर्ग के दृष्टिकोण को दर्शाते हैं, सामान्य जनता के जीवन की उपेक्षा करते हैं।\\nनीचे दिए गए कूट का उपयोग करके सही उत्तर चुनें:",
    ["1 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"],
    ["केवल 1", "केवल 1 और 2", "केवल 2 और 3", "1, 2 और 3"],
    3,
    "All three points represent major limitations of epigraphical sources highlighted by historians like Romila Thapar and D.D. Kosambi.",
    "तीनों बिंदु इतिहासकारों (जैसे रोमिला थापर और डी.डी. कोसांबी) द्वारा रेखांकित किए गए अभिलेखीय स्रोतों की प्रमुख सीमाओं का प्रतिनिधित्व करते हैं।"
)

# Mock 9
add_mock_mcq(
    "Consider the following statements regarding Neolithic transitions in different regions of India:\\n1. The Kashmiri Neolithic site of Gufkral shows pit-dwellings in its earliest phase but shifts to mud-brick structures later.\\n2. Domestication of rice at Lahuradewa developed independently and was not introduced by Central Asian migrants.\\n3. Chirand in Bihar is unique because it yielded a massive assemblage of bone tools alongside stone celts.\\nWhich of the statements given above are correct?",
    "भारत के विभिन्न क्षेत्रों में नवपाषाणकालीन परिवर्तनों के संबंध में निम्नलिखित कथनों पर विचार करें:\\n1. कश्मीर के नवपाषाणकालीन स्थल गुफकराल के शुरुआती चरण में गर्त-निवास (pit-dwellings) दिखाई देते हैं लेकिन बाद में यह मिट्टी की ईंटों की संरचनाओं में स्थानांतरित हो जाता है।\\n2. लहुरादेवा में चावल का घरेलूकरण स्वतंत्र रूप से विकसित हुआ और इसे मध्य एशियाई प्रवासियों द्वारा नहीं लाया गया था।\\n3. बिहार में चिरांद अद्वितीय है क्योंकि वहाँ पत्थर के औजारों (celts) के साथ-साथ बड़ी संख्या में हड्डी के उपकरण मिले हैं।\\nऊपर दिए गए कथनों में से कौन से सही हैं?",
    ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
    ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
    3,
    "All three statements are correct. Gufkral shows pit dwellings in Phase IA. Lahuradewa shows indigenous rice domestication c. 9000-8000 BCE. Chirand is famous for its extensive antler/bone tool collection.",
    "तीनों कथन सही हैं। गुफकराल के IA चरण में गर्त निवास दिखते हैं। लहुरादेवा में लगभग 9000-8000 ईसा पूर्व के स्थानीय स्तर पर विकसित चावल के साक्ष्य मिले हैं। चिरांद हिरण के सींगों और हड्डियों के उपकरणों के व्यापक संग्रह के लिए प्रसिद्ध है।"
)

# Mock 10
add_mock_mcq(
    "Consider the following archaeological scholars and their key fields of contribution:\\n1. Robert Bruce Foote : Discovered first Palaeolithic tool in India at Pallavaram (1863)\\n2. Jean-Francois Jarrige : Excavated the early Neolithic settlement of Mehrgarh\\n3. Vishnu Shridhar Wakankar : Discovered the prehistoric rock shelters of Bhimbetka (1957)\\n4. Shanti Pappu : Conducted cosmic nuclide dating and excavations at Attirampakkam\\nWhich of the pairs given above are correctly matched?",
    "निम्नलिखित पुरातात्विक विद्वानों और उनके योगदान के प्रमुख क्षेत्रों पर विचार करें:\\n1. रॉबर्ट ब्रूस फुट : पल्लवरम में भारत में पहला पुरापाषाणकालीन उपकरण खोजा (1863)\\n2. जीन-फ्रांस्वा जारिज : मेहरगढ़ की प्रारंभिक नवपाषाण बस्ती का उत्खनन किया\\n3. विष्णु श्रीधर वाकणकर : भीमबेटका के प्रागैतिहासिक शैल आश्रयों की खोज की (1957)\\n4. शांति पप्पू : अतिरामपक्कम में कॉस्मिक न्यूक्लाइड काल-निर्धारण और उत्खनन का नेतृत्व किया\\nऊपर दिए गए युग्मों में से कौन से सही सुमेलित हैं?",
    ["1, 2 and 3 only", "2, 3 and 4 only", "1, 3 and 4 only", "1, 2, 3 and 4"],
    ["केवल 1, 2 और 3", "केवल 2, 3 और 4", "केवल 1, 3 और 4", "1, 2, 3 और 4"],
    3,
    "All four pairs are correct matches of major archaeological figures in Indian prehistory and their landmark achievements.",
    "भारतीय प्रागैतिहास के चारों प्रमुख पुरातात्विक व्यक्तित्व और उनकी ऐतिहासिक उपलब्धियां सही सुमेलित हैं।"
)

# ==========================================
# MERGE LOGIC (READ, INJECT, WRITE JSON FILES)
# ==========================================

import json

# EN content.json
print("Merging English content.json...")
with open('content.json', 'r', encoding='utf-8') as f:
    en_data = json.load(f)

en_data['deepDive']['sections'][0]['masteryZone'] = sec1_en
en_data['deepDive']['sections'][1]['masteryZone'] = sec2_en
en_data['deepDive']['sections'][2]['masteryZone'] = sec3_en
en_data['deepDive']['sections'][3]['masteryZone'] = sec4_en
en_data['deepDive']['sections'][4]['masteryZone'] = sec5_en

en_data['practiceQuestions'] = practice_en
en_data['mockTestQuestions'] = mock_en

en_data['labels']['tabs']['practice'] = "2. Practice Zone (50 Qs)"
en_data['labels']['practiceZoneHeader']['title'] = "Practice Zone: 50 Questions"
en_data['labels']['mockIntro']['description'] = "Contains 10 multi-statement questions testing conceptual understanding and site locations. 1/3 negative marking applies."

with open('content.json', 'w', encoding='utf-8') as f:
    json.dump(en_data, f, ensure_ascii=False, indent=2)

# HI content.json
print("Merging Hindi hi/content.json...")
with open('hi/content.json', 'r', encoding='utf-8') as f:
    hi_data = json.load(f)

hi_data['deepDive']['sections'][0]['masteryZone'] = sec1_hi
hi_data['deepDive']['sections'][1]['masteryZone'] = sec2_hi
hi_data['deepDive']['sections'][2]['masteryZone'] = sec3_hi
hi_data['deepDive']['sections'][3]['masteryZone'] = sec4_hi
hi_data['deepDive']['sections'][4]['masteryZone'] = sec5_hi

hi_data['practiceQuestions'] = practice_hi
hi_data['mockTestQuestions'] = mock_hi

hi_data['labels']['tabs']['practice'] = "2. अभ्यास क्षेत्र (50 प्रश्न)"
hi_data['labels']['practiceZoneHeader']['title'] = "अभ्यास क्षेत्र: 50 प्रश्न"
hi_data['labels']['mockIntro']['description'] = "अवधारणात्मक समझ और स्थलों की स्थिति का परीक्षण करने वाले 10 बहु-कथनीय प्रश्न शामिल हैं। 1/3 नकारात्मक अंकन प्रणाली लागू है।"

with open('hi/content.json', 'w', encoding='utf-8') as f:
    json.dump(hi_data, f, ensure_ascii=False, indent=2)

print("SUCCESS: Merged all sections, practice questions, and mock questions into English and Hindi content.json.")

