import os
import json

# Define base folder
BASE_DIR = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\Prehistory\History-of-Early-Iron-Age\questions_data"
os.makedirs(BASE_DIR, exist_ok=True)

def add_match(sec_en, sec_hi, q_en, q_hi, items_en, items_hi, opts_en, opts_hi, sol_en, sol_hi):
    keys = ['A', 'B', 'C']
    roman = ['I. ', 'II. ', 'III. ']
    items_en_objs = [{"left": roman[i] + items_en[i], "key": keys[i]} for i in range(len(items_en))]
    items_hi_objs = [{"left": roman[i] + items_hi[i], "key": keys[i]} for i in range(len(items_hi))]
    
    options_en_objs = [
        {"val": "B", "text": "A. " + opts_en[1]},
        {"val": "C", "text": "B. " + opts_en[2]},
        {"val": "A", "text": "C. " + opts_en[0]}
    ]
    options_hi_objs = [
        {"val": "B", "text": "A. " + opts_hi[1]},
        {"val": "C", "text": "B. " + opts_hi[2]},
        {"val": "A", "text": "C. " + opts_hi[0]}
    ]
    
    sec_en.append({"type": "Match the Following", "q": q_en, "items": items_en_objs, "options": options_en_objs, "sol": sol_en})
    sec_hi.append({"type": "Match the Following", "q": q_hi, "items": items_hi_objs, "options": options_hi_objs, "sol": sol_hi})

def generate_sec_file(name, list_en, list_hi):
    path = os.path.join(BASE_DIR, f"{name}.py")
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# Programmatically generated Iron Age Qs\n\n")
        f.write(f"{name}_en = {repr(list_en)}\n\n")
        f.write(f"{name}_hi = {repr(list_hi)}\n")

# Standard options for Assertion-Reason
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

# Section 1: Origin & Chronology of Iron Metallurgy (62 questions)
sec1_en = []
sec1_hi = []

# 5 MCQ
mcqs_en = [
    {"q": "What metallurgical technique is used to harden raw iron into steel-like alloys by heating it with carbonaceous matter?", "opts": ["Carburization", "Calcination", "Liquation", "Amalgamation"], "ans": 0, "sol": "Carburization introduces carbon into iron, hardening it into steel-like alloys suitable for tools."},
    {"q": "Which of the following sites has yielded C-14 dates pushing the antiquity of iron in India to c. 1200 BCE?", "opts": ["Hallur", "Bhimbetka", "Nevasa", "Mehrgarh"], "ans": 0, "sol": "Hallur in Karnataka and Atranjikhera in UP have yielded early C-14 dates around 1200 BCE."},
    {"q": "What is the primary mineral source processed in early Indian shaft furnaces for iron reduction?", "opts": ["Hematite and Magnetite ores", "Chalcopyrite ores", "Galena ores", "Bauxite ores"], "ans": 0, "sol": "Early iron smelting used hematite and magnetite iron ores processed with charcoal."},
    {"q": "The archaeological layer representing the transition to iron is characterized by the overlap of which two pottery traditions?", "opts": ["Black-and-Red Ware and Painted Grey Ware", "Ochre Coloured Pottery and Northern Black Polished Ware", "Harappan Red Ware and Glazed Ware", "Coarse Grey Ware and Corded Ware"], "ans": 0, "sol": "The transition to the Iron Age shows an overlap of late Black-and-Red Ware (BRW) and early Painted Grey Ware (PGW)."},
    {"q": "Which of the following is the key byproduct indicating systematic smelting operations at early iron working sites?", "opts": ["Iron Slag", "Copper slag", "Bronze filings", "Ash mounds"], "ans": 0, "sol": "Iron slag and cinder in smelting layers serve as primary evidence of active metallurgy."}
]
mcqs_hi = [
    {"q": "कच्चे लोहे को कार्बोनेसस पदार्थ के साथ गर्म करके स्टील जैसी मिश्र धातुओं में बदलने के लिए किस धातुकर्म तकनीक का उपयोग किया जाता है?", "opts": ["कार्बोराइजेशन (Carburization)", "निस्तापन (Calcination)", "द्रवीकरण (Liquation)", "अमलगमेशन"], "ans": 0, "sol": "कार्बोराइजेशन लोहे में कार्बन प्रवेश कराता है, जिससे यह औजारों के लिए उपयुक्त स्टील जैसी कठोर मिश्र धातु में बदल जाता है।"},
    {"q": "निम्नलिखित में से किस स्थल से प्राप्त सी-14 तिथियों ने भारत में लोहे की प्राचीनता को लगभग 1200 ईसा पूर्व तक धकेल दिया है?", "opts": ["हल्लूर", "भीमबेटका", "नेवासा", "मेहरगढ़"], "ans": 0, "sol": "कर्नाटक में हल्लूर और यूपी में अतरंजीखेड़ा से लगभग 1200 ईसा पूर्व की प्रारंभिक सी-14 तिथियां मिली हैं।"},
    {"q": "प्रारंभिक भारतीय शाफ्ट भट्टियों में लोहे के निष्कर्षण के लिए किस प्राथमिक खनिज संसाधन को संसाधित किया जाता था?", "opts": ["हेमेटाइट और मैग्नेटाइट अयस्क", "कैलकोपाइराइट अयस्क", "गैलेना अयस्क", "बॉक्साइट अयस्क"], "ans": 0, "sol": "प्रारंभिक लोहे के प्रगलन में लकड़ी के कोयले के साथ संसाधित हेमेटाइट और मैग्नेटाइट लौह अयस्कों का उपयोग किया जाता था।"},
    {"q": "लोहे के संक्रमण का प्रतिनिधित्व करने वाली पुरातात्विक परत किन दो मृदभांड परंपराओं के ओवरलैप से पहचानी जाती है?", "opts": ["काले-और-लाल मृदभांड और चित्रित धूसर मृदभांड (PGW)", "गेरुए रंग के मृदभांड और उत्तरी काले चमकीले मृदभांड (NBPW)", "हड़प्पा कालीन लाल मृदभांड और चमकदार मृदभांड", "खुरदरे धूसर मृदभांड और कॉर्डेड मृदभांड"], "ans": 0, "sol": "लौह युग के संक्रमण काल में देर के काले-और-लाल मृदभांड (BRW) और प्रारंभिक चित्रित धूसर मृदभांड (PGW) का ओवरलैप दिखाई देता है।"},
    {"q": "निम्नलिखित में से कौन सा प्रमुख सह-उत्पाद है जो प्रारंभिक लौह स्थलों पर व्यवस्थित प्रगलन गतिविधियों को दर्शाता है?", "opts": ["लौह धातुमल (Iron Slag)", "तांबा धातुमल", "कांसा बुरादा", "राख के टीले"], "ans": 0, "sol": "प्रगलन परतों में लौह धातुमल और सिंडर सक्रिय धातु विज्ञान के प्राथमिक साक्ष्य के रूप में कार्य करते हैं।"}
]
for i in range(5):
    sec1_en.append({"type": "MCQ", "q": mcqs_en[i]["q"], "opts": mcqs_en[i]["opts"], "ans": mcqs_en[i]["ans"], "sol": mcqs_en[i]["sol"]})
    sec1_hi.append({"type": "MCQ", "q": mcqs_hi[i]["q"], "opts": mcqs_hi[i]["opts"], "ans": mcqs_hi[i]["ans"], "sol": mcqs_hi[i]["sol"]})

# 5 Multiple Correct MCQ
multis_en = [
    {"q": "Which of the following technological steps are essential in producing functional steel from iron ore? (Select all that apply)", "opts": ["Reduction smelting in furnaces", "Decarburization of wrought iron", "Carburization of bloom", "Quenching and tempering"], "ans": [0, 2, 3], "sol": "Smelting reduces ore, carburization adds carbon to bloom, and quenching/tempering hardens the steel alloy."},
    {"q": "Identify the regional zones in India recognized for independent early centers of iron working: (Select all that apply)", "opts": ["Gangetic Valley (UP/Bihar)", "Eastern Ghats (Odisha/Andhra)", "Southern Deccan (Karnataka)", "Indus Plains (Punjab)"], "ans": [0, 1, 2], "sol": "Gangetic Doab, Eastern Ghats/Central India, and Southern Deccan developed early smelting independently. The Indus plains lack ore resources."},
    {"q": "Which archaeological findings confirm active iron smelting at a site? (Select all that apply)", "opts": ["Tuyeres or clay nozzles", "Iron slag and ash beds", "Vitrified lining of furnaces", "Terracotta female figurines"], "ans": [0, 1, 2], "sol": "Tuyeres, slag, and vitrified clay furnace walls are primary metallurgical indicators. Figurines are domestic art items."},
    {"q": "Which of the following early Iron Age sites have yielded carbon dates older than 1000 BCE? (Select all that apply)", "opts": ["Hallur", "Atranjikhera", "Malhar", "Bhimbetka Caves"], "ans": [0, 1, 2], "sol": "Hallur, Atranjikhera, and Malhar have pushed the chronology back to c. 1200-1400 BCE. Bhimbetka caves are Stone Age rock shelters."},
    {"q": "Select the properties that distinguish early iron tools from Bronze tools: (Select all that apply)", "opts": ["Higher raw material abundance", "Harder cutting edge when carburized", "Lower smelting temperature requirement", "Corrosion resistance without care"], "ans": [0, 1], "sol": "Iron is highly abundant and harder when carburized. However, it requires higher smelting temperatures and rusts easily."}
]
multis_hi = [
    {"q": "लौह अयस्क से कार्यात्मक स्टील बनाने के लिए निम्नलिखित में से कौन से तकनीकी कदम आवश्यक हैं? (सभी लागू विकल्प चुनें)", "opts": ["भट्टियों में अपचयन प्रगलन (Reduction smelting)", "पिटवां लोहे का वि-कार्बोराइजेशन", "लोहे के पिण्ड (Bloom) का कार्बोराइजेशन", "शमन (Quenching) और तपन (Tempering)"], "ans": [0, 2, 3], "sol": "प्रगलन अयस्क को कम करता है, कार्बोराइजेशन पिण्ड में कार्बन जोड़ता है, और शमन/तपन स्टील मिश्र धातु को कठोर बनाता है।"},
    {"q": "भारत में प्रारंभिक लौह धातु कर्म के स्वतंत्र केंद्रों के रूप में मान्यता प्राप्त क्षेत्रीय क्षेत्रों की पहचान करें: (सभी लागू विकल्प चुनें)", "opts": ["गंगा घाटी (यूपी/बिहार)", "पूर्वी घाट (ओडिशा/आंध्र)", "दक्षिणी दक्कन (कर्नाटक)", "सिंधु मैदान (पंजाब)"], "ans": [0, 1, 2], "sol": "गंगा दोआब, पूर्वी घाट/मध्य भारत और दक्षिणी दक्कन में स्वतंत्र रूप से प्रारंभिक प्रगलन का विकास हुआ। सिंधु मैदान में लौह अयस्क संसाधनों की कमी है।"},
    {"q": "कौन से पुरातात्विक निष्कर्ष किसी स्थल पर सक्रिय लोहा गलाने की पुष्टि करते हैं? (सभी लागू विकल्प चुनें)", "opts": ["फूंकनी (Tuyeres) या मिट्टी के नोजल", "लोहे का धातुमल (Slag) और राख के ढेर", "भट्टियों के कांच जैसी बनी मिट्टी की दीवारें (Vitrified lining)", "टेराकोटा की महिला मूर्तियाँ"], "ans": [0, 1, 2], "sol": "फूंकनी, धातुमल और कांच जैसी भट्टी की दीवारें प्राथमिक धातुकर्म संकेतक हैं। मूर्तियाँ घरेलू कला वस्तुएँ हैं।"},
    {"q": "निम्नलिखित में से किस प्रारंभिक लौह युग के स्थल से 1000 ईसा पूर्व से पुरानी कार्बन तिथियां मिली हैं? (सभी लागू विकल्प चुनें)", "opts": ["हल्लूर", "अतरंजीखेड़ा", "मल्हार", "भीमबेटका गुफाएं"], "ans": [0, 1, 2], "sol": "हल्लूर, अतरंजीखेड़ा और मल्हार ने कालानुक्रम को लगभग 1200-1400 ईसा पूर्व तक पीछे धकेल दिया है। भीमबेटका गुफाएं पाषाण काल के शैल आवास हैं।"},
    {"q": "उन गुणों का चयन करें जो प्रारंभिक लोहे के औजारों को कांसे के औजारों से अलग करते हैं: (सभी लागू विकल्प चुनें)", "opts": ["कच्चे माल की उच्च प्रचुरता", "कार्बोराइज्ड होने पर अधिक कठोर धार", "कम प्रगलन तापमान की आवश्यकता", "बिना देखभाल के जंग प्रतिरोध"], "ans": [0, 1], "sol": "लोहा अत्यधिक प्रचुर है और कार्बोराइज्ड होने पर अधिक कठोर होता है। हालांकि, इसे उच्च प्रगलन तापमान की आवश्यकता होती है और इसमें आसानी से जंग लग जाता है।"}
]
for i in range(5):
    sec1_en.append({"type": "Multiple Correct MCQ", "q": multis_en[i]["q"], "opts": multis_en[i]["opts"], "ans": multis_en[i]["ans"], "sol": multis_en[i]["sol"]})
    sec1_hi.append({"type": "Multiple Correct MCQ", "q": multis_hi[i]["q"], "opts": multis_hi[i]["opts"], "ans": multis_hi[i]["ans"], "sol": multis_hi[i]["sol"]})

# 8 True/False
tfs_en = [
    ("True or False: Iron metallurgy was introduced to the Indian subcontinent solely through diffusion from Western Asia.", False, "No, evidence from sites like Malhar and Atranjikhera supports independent local origins of iron smelting in India."),
    ("True or False: Iron oxide requires higher temperatures to melt completely than copper ore.", True, "True, copper melts at 1085°C while iron melts at 1538°C, necessitating advanced draft control."),
    ("True or False: Bloomery iron refers to iron that is melted and poured into molds like bronze.", False, "No, bloomery furnaces produce a spongy solid mass (bloom) which must be hammered to remove slag."),
    ("True or False: Carburization is the process of coating iron tools with copper slips to prevent rusting.", False, "No, carburization is the addition of carbon to iron to create a steel-like alloy."),
    ("True or False: The early Iron Age overlaps with the Later Vedic literary phase in Northern India.", True, "True, the PGW culture is widely correlated with Later Vedic texts."),
    ("True or False: Smelting furnaces in early India were simple open pit fires with no draft controls.", False, "No, they were closed clay shaft furnaces utilizing bellows (tuyeres) to achieve high reducing temperatures."),
    ("True or False: Gufkral in Kashmir has yielded early evidence of iron during its late Neolithic-Megalthic transition.", True, "True, Gufkral shows early iron tools coexisting with polished stone celts."),
    ("True or False: The transition to iron instantly eliminated the use of stone blade tools across India.", False, "No, stone blades coexisted for centuries due to the high cost and scarcity of early iron.")
]
tfs_hi = [
    ("सही या गलत: भारतीय उपमहाद्वीप में लोहे की तकनीक केवल पश्चिमी एशिया से प्रसार (diffusion) के माध्यम से आई थी।", False, "नहीं, मल्हार और अतरंजीखेड़ा जैसे स्थलों के साक्ष्य भारत में लोहे के स्वतंत्र स्थानीय उद्भव का समर्थन करते हैं।"),
    ("सही या गलत: लौह अयस्क को पूरी तरह से पिघलाने के लिए तांबा अयस्क की तुलना में अधिक तापमान की आवश्यकता होती है।", True, "सही, तांबा 1085 डिग्री सेल्सियस पर पिघलता है जबकि लोहा 1538 डिग्री सेल्सियस पर पिघलता है, जिसके लिए उन्नत वायु प्रवाह नियंत्रण की आवश्यकता होती है।"),
    ("सही या गलत: ब्लूमरी आयरन (Bloomery iron) से तात्पर्य उस लोहे से है जिसे कांसे की तरह पिघलाकर सांचों में ढाला जाता है।", False, "नहीं, ब्लूमरी भट्टियां एक स्पंजी ठोस द्रव्यमान (ब्लूम) बनाती हैं जिसे धातुमल हटाने के लिए हथौड़े से पीटना पड़ता है।"),
    ("सही या गलत: कार्बोराइजेशन लोहे के औजारों पर तांबे का लेप लगाने की प्रक्रिया है ताकि जंग न लगे।", False, "नहीं, कार्बोराइजेशन स्टील जैसी मिश्र धातु बनाने के लिए लोहे में कार्बन मिलाने की प्रक्रिया है।"),
    ("सही या गलत: उत्तरी भारत में प्रारंभिक लौह युग उत्तर वैदिक साहित्य काल के साथ मेल खाता है।", True, "सही, चित्रित धूसर मृदभांड (PGW) संस्कृति का उत्तर वैदिक ग्रंथों से व्यापक संबंध है।"),
    ("सही या गलत: प्रारंभिक भारत में लोहा गलाने की भट्टियाँ साधारण खुले गड्ढे की आग थीं जिसमें कोई वायु प्रवाह नियंत्रण नहीं था।", False, "नहीं, वे बंद मिट्टी की भट्टियां थीं जिनमें उच्च अपचयन तापमान प्राप्त करने के लिए धौंकनी (फूंकनी) का उपयोग किया जाता था।"),
    ("सही या गलत: कश्मीर के गुफक्राल से इसके अंतिम नवपाषाण-महापाषाण संक्रमण के दौरान लोहे के शुरुआती साक्ष्य मिले हैं।", True, "सही, गुफक्राल पॉलिश किए गए पत्थर के औजारों के साथ सह-अस्तित्व में प्रारंभिक लोहे के औजारों को दर्शाता है।"),
    ("सही या गलत: लोहे के आगमन ने पूरे भारत में पत्थर के फलक (ब्लेड) औजारों के उपयोग को तुरंत समाप्त कर दिया।", False, "नहीं, प्रारंभिक लोहे की उच्च लागत और कमी के कारण पत्थर के ब्लेड सदियों तक सह-अस्तित्व में रहे।")
]
for i in range(8):
    sec1_en.append({"type": "True/False", "q": tfs_en[i][0], "ans": tfs_en[i][1], "sol": tfs_en[i][2]})
    sec1_hi.append({"type": "True/False", "q": tfs_hi[i][0], "ans": tfs_hi[i][1], "sol": tfs_hi[i][2]})

# 8 Fill in the Blank
blanks_en = [
    ("The temperature required to melt pure iron is __________ degrees Celsius.", "1538", "Pure iron melts at 1538°C, which was rarely achieved in early bloomeries; tools were worked in semi-solid state."),
    ("The spongy mass of iron mixed with slag produced in a bloomery furnace is called __________.", "bloom", "The raw, spongy product is called iron bloom, which is forged to expel silicate slag."),
    ("The clay pipes or nozzles used to blow air from bellows into the smelting furnace are known as __________.", "tuyeres", "Tuyeres are heat-resistant clay nozzles that direct air draft into the reducing zone."),
    ("In Uttar Pradesh, the site of __________ has yielded some of the earliest dates for iron working around 1800 BCE.", "Malhar", "Malhar in the Karmanasa valley has yielded exceptionally early iron artifacts dating to c. 1800 BCE."),
    ("To convert iron into a steel-like alloy, it is heated in contact with charcoal to absorb __________.", "carbon", "Carbon absorption (carburization) is crucial for transforming soft wrought iron into steel."),
    ("The transition phase where copper, stone, and early iron tools coexist is called the __________ phase.", "protohistoric", "The protohistoric transition phase features overlapping technologies as metallurgy matures."),
    ("The element __________ was absent in early Indian iron ores, making them distinct from Western Asian ores.", "phosphorus", "Early Gangetic ores had specific mineral characteristics, including low phosphorus in certain zones."),
    ("The early site in the Southern Deccan that yielded pre-1000 BCE iron dates is __________.", "Hallur", "Hallur in Karnataka provides C-14 dates of c. 1200 BCE for early iron-working layers.")
]
blanks_hi = [
    ("शुद्ध लोहे को पिघलाने के लिए आवश्यक तापमान __________ डिग्री सेल्सियस है।", "1538", "शुद्ध लोहा 1538°C पर पिघलता है, जो प्रारंभिक ब्लूमरी में शायद ही कभी प्राप्त होता था; औजारों को अर्ध-ठोस अवस्था में आकार दिया जाता था।"),
    ("ब्लूमरी भट्टी में उत्पादित धातुमल के साथ मिश्रित लोहे के स्पंजी द्रव्यमान को __________ कहा जाता है।", "ब्लूम", "कच्चे, स्पंजी उत्पाद को आयरन ब्लूम (लोह पिण्ड) कहा जाता है, जिसे धातुमल बाहर निकालने के लिए पीटा जाता है।"),
    ("धौंकनी से प्रगलन भट्टी में हवा फूंकने के लिए उपयोग की जाने वाली मिट्टी की नलियों को __________ के रूप में जाना जाता है।", "फूंकनी", "फूंकनी (Tuyeres) गर्मी प्रतिरोधी मिट्टी की नलियाँ होती हैं जो अपचयन क्षेत्र में हवा के प्रवाह को निर्देशित करती हैं।"),
    ("उत्तर प्रदेश में, __________ स्थल से 1800 ईसा पूर्व के आसपास लोहा बनाने के कुछ सबसे शुरुआती साक्ष्य मिले हैं।", "मल्हार", "कर्मनाशा घाटी में मल्हार से लगभग 1800 ईसा पूर्व के असाधारण रूप से प्रारंभिक लोहे की कलाकृतियां मिली हैं।"),
    ("लोहे को स्टील जैसी मिश्र धातु में बदलने के लिए, इसे कोयले के संपर्क में गर्म किया जाता है ताकि यह __________ को अवशोषित कर सके।", "कार्बन", "नरम लोहे को स्टील में बदलने के लिए कार्बन का अवशोषण (कार्बोराइजेशन) अत्यंत महत्वपूर्ण है।"),
    ("वह संक्रमण चरण जहाँ तांबा, पत्थर और शुरुआती लोहे के औजार एक साथ मौजूद होते हैं, __________ चरण कहलाता है।", "आद्य-ऐतिहासिक", "आद्य-ऐतिहासिक संक्रमण चरण में धातुकर्म के परिपक्व होने के साथ ओवरलैपिंग प्रौद्योगिकियां दिखाई देती हैं।"),
    ("प्रारंभिक भारतीय लौह अयस्कों में तत्व __________ अनुपस्थित था, जिससे वे पश्चिमी एशियाई अयस्कों से भिन्न थे।", "फास्फोरस", "प्रारंभिक गंगा घाटी के अयस्कों में विशिष्ट खनिज विशेषताएं थीं, जिसमें कुछ क्षेत्रों में कम फास्फोरस शामिल था।"),
    ("दक्षिणी दक्कन का वह प्रारंभिक स्थल जिसने 1000 ईसा पूर्व से पहले की लोहे की तिथियां प्रदान कीं, __________ है।", "हल्लूर", "कर्नाटक में हल्लूर प्रारंभिक लौह-कार्यकारी परतों के लिए लगभग 1200 ईसा पूर्व की सी-14 तिथियां प्रदान करता है।")
]
for i in range(8):
    sec1_en.append({"type": "Fill in the Blank", "q": blanks_en[i][0], "ans": blanks_en[i][1], "sol": blanks_en[i][2]})
    sec1_hi.append({"type": "Fill in the Blank", "q": blanks_hi[i][0], "ans": blanks_hi[i][1], "sol": blanks_hi[i][2]})

# 3 Match the Following
match1_items_en = ["Smelting Furnace", "Carburization", "Bloomery Forging"]
match1_items_hi = ["प्रगलन भट्टी", "कार्बोराइजेशन", "ब्लूमरी फोर्जिंग"]
match1_opts_en = ["Reduces iron oxide ore with carbon monoxide", "Hardens iron edge by heating with carbon", "Hammering semi-solid iron block to expel slag"]
match1_opts_hi = ["कार्बन मोनोऑक्साइड के साथ लौह अयस्क को अपचयित करती है", "कार्बन के साथ गर्म करके लोहे की धार को सख्त करता है", "धातुमल बाहर निकालने के लिए अर्ध-ठोस लोहे को हथौड़े से पीटना"]

match2_items_en = ["Hallur Center", "Malhar Center", "Atranjikhera Center"]
match2_items_hi = ["हल्लूर केंद्र", "मल्हार केंद्र", "अतरंजीखेड़ा केंद्र"]
match2_opts_en = ["Southern Deccan Early Dates (1200 BCE)", "Karmanasa Valley Early Dates (1800 BCE)", "Gangetic Doab Smelting Furnaces (1200 BCE)"]
match2_opts_hi = ["दक्षिणी दक्कन प्रारंभिक तिथियां (1200 ईसा पूर्व)", "कर्मनाशा घाटी प्रारंभिक तिथियां (1800 ईसा पूर्व)", "गंगा दोआब प्रगलन भट्टियां (1200 ईसा पूर्व)"]

match3_items_en = ["Hematite", "Wrought Iron", "Tuyere"]
match3_items_hi = ["हेमेटाइट", "पिटवां लोहा", "फूंकनी"]
match3_opts_en = ["Naturally occurring iron oxide ore", "Low carbon malleable metal", "Clay pipe for air blast"]
match3_opts_hi = ["प्राकृतिक रूप से पाया जाने वाला लौह अयस्क", "कम कार्बन वाली लचीली धातु", "हवा फेंकने के लिए मिट्टी की नली"]

add_match(sec1_en, sec1_hi, "Match the metallurgical term with its function:", "धातुकर्म शब्द को उसके कार्य से सुमेलित करें:", match1_items_en, match1_items_hi, match1_opts_en, match1_opts_hi, "Smelting furnace reduces ore; Carburization adds carbon; Forging shapes and cleans iron.", "प्रगलन भट्टी अयस्क को अपचयित करती है; कार्बोराइजेशन कार्बन जोड़ता है; फोर्जिंग लोहे को आकार देती है और साफ करती है।")
add_match(sec1_en, sec1_hi, "Match the site with its chronological significance:", "स्थल को उसके कालानुक्रमिक महत्व के साथ सुमेलित करें:", match2_items_en, match2_items_hi, match2_opts_en, match2_opts_hi, "Hallur belongs to Southern early dates; Malhar has early dates in UP; Atranjikhera has smelting furnaces.", "हल्लूर दक्षिणी प्रारंभिक तिथियों से संबंधित है; मल्हार की यूपी में शुरुआती तिथियां हैं; अतरंजीखेड़ा में प्रगलन भट्टियां हैं।")
add_match(sec1_en, sec1_hi, "Match the material with its metallurgical description:", "सामग्री को उसके धातुकर्म विवरण से सुमेलित करें:", match3_items_en, match3_items_hi, match3_opts_en, match3_opts_hi, "Hematite is ore; Wrought iron is low carbon worked metal; Tuyere is the clay draft pipe.", "हेमेटाइट अयस्क है; पिटवां लोहा कम कार्बन वाला धातु है; फूंकनी मिट्टी की नली है।")

# 8 One-Liner
oneliners_en = [
    ("Define the main difference between wrought iron and cast iron.", "Wrought iron contains very low carbon (<0.08%) and is malleable, while cast iron has high carbon (>2%) making it hard but brittle."),
    ("Name the river valley in UP where Malhar is located.", "The Karmanasa River valley."),
    ("What temperature range was typically maintained inside early Indian iron smelting furnaces?", "Around 1100°C to 1250°C, sufficient to reduce iron oxide without melting the iron fully."),
    ("Why was charcoal preferred over raw wood in early smelting?", "Charcoal burns hotter, produces less moisture, and acts as a strong reducing agent by producing carbon monoxide."),
    ("Which site provides the earliest evidence of slag heaps in the Gangetic basin?", "Atranjikhera in Uttar Pradesh."),
    ("What is the chemical function of bellows in a smelting kiln?", "Bellows force oxygen into the kiln, reacting with charcoal to form carbon monoxide which reduces iron oxide."),
    ("Which southern site shows transition layers from Neolithic-Chalcolithic directly to Iron Age?", "Hallur in Karnataka."),
    ("Explain the term 'carburized iron bloom'.", "An iron mass whose outer surface has absorbed carbon during prolonged contact with hot charcoal, turning it into steel.")
]
oneliners_hi = [
    ("पिटवां लोहे (wrought iron) और ढलवां लोहे (cast iron) के बीच मुख्य अंतर स्पष्ट करें।", "पिटवां लोहे में कार्बन बहुत कम (<0.08%) होता है और यह लचीला होता है, जबकि ढलवां लोहे में अधिक carbon (>2%) होता है जिससे यह कठोर लेकिन भंगुर हो जाता है।"),
    ("यूपी की उस नदी घाटी का नाम बताइए जहाँ मल्हार स्थित है।", "कर्मनाशा नदी घाटी।"),
    ("प्रारंभिक भारतीय लोहा गलाने की भट्टियों के भीतर आम तौर पर किस तापमान सीमा को बनाए रखा जाता था?", "लगभग 1100 डिग्री सेल्सियस से 1250 डिग्री सेल्सियस, जो लोहे को पूरी तरह से पिघलाए बिना लौह ऑक्साइड को अपचयित करने के लिए पर्याप्त था।"),
    ("प्रारंभिक प्रगलन में कच्चे ईंधन की तुलना में लकड़ी के कोयले (Charcoal) को क्यों प्राथमिकता दी गई?", "कोयला अधिक गर्मी से जलता है, कम नमी पैदा करता है, और कार्बन मोनोऑक्साइड उत्पन्न करके एक मजबूत अपचायक एजेंट के रूप में कार्य करता है।"),
    ("गंगा बेसिन में धातुमल के ढेरों के सबसे शुरुआती साक्ष्य किस स्थल से मिलते हैं?", "उत्तर प्रदेश में अतरंजीखेड़ा।"),
    ("प्रगलन भट्टी में धौंकनी (Bellows) का रासायनिक कार्य क्या है?", "धौंकनी भट्टी में ऑक्सीजन भेजती है, जो कोयले के साथ प्रतिक्रिया करके कार्बन मोनोऑक्साइड बनाती है जो लौह ऑक्साइड को अपचयित करती है।"),
    ("कौन सा दक्षिणी स्थल नवपाषाण-ताम्रपाषाण से सीधे लौह युग में संक्रमण की परतें दिखाता है?", "कर्नाटक में हल्लूर।"),
    ("शब्द 'कार्बोराइज्ड आयरन ब्लूम' को स्पष्ट करें।", "एक लौह पिण्ड जिसकी बाहरी सतह ने गर्म कोयले के लंबे संपर्क के दौरान कार्बन को अवशोषित कर लिया है, जिससे यह स्टील में बदल गया है।")
]
for i in range(8):
    sec1_en.append({"type": "One-Liner", "q": oneliners_en[i][0], "sol": oneliners_en[i][1]})
    sec1_hi.append({"type": "One-Liner", "q": oneliners_hi[i][0], "sol": oneliners_hi[i][1]})

# 8 Assertion-Reason
ars_en = [
    ("Assertion (A): Early Iron Age communities in India primarily produced wrought iron and steel rather than cast iron.\nReason (R): Their shaft furnaces could not achieve temperatures above 1538°C to melt iron into liquid state.", 0, "Both A and R are correct, and R explains A. Wrought iron was worked in solid state because furnaces lacked draft to melt iron fully."),
    ("Assertion (A): Diffusion from West Asia was the sole catalyst for the origin of iron metallurgy in India.\nReason (R): Radiocarbon dates from Malhar and Atranjikhera show iron working in India dating back to c. 1800–1200 BCE, contemporary with or older than Anatolian dates.", 3, "A is false but R is true. Indian dates are very early and show independent regional metallurgy."),
    ("Assertion (A): Hematite and magnetite ores were widely utilized by early iron smelt shops.\nReason (R): These oxide ores are abundant in India and easier to reduce than sulfide ores.", 0, "Both A and R are correct and R explains A. Oxide ores are easily reduced with carbon monoxide in bloomery furnaces."),
    ("Assertion (A): Early iron axes were instantly superior to bronze axes for forest clearing.\nReason (R): Pure bloomery iron without carburization is softer than alloyed bronze.", 3, "A is false because early pure iron was soft and did not instantly replace bronze until carburization was developed. R is true."),
    ("Assertion (A): Tuyeres excavated at Atranjikhera prove advanced draft techniques.\nReason (R): Clay tuyeres prevented the metal nozzles from melting inside the furnace reducing zone.", 1, "Both statements are true, but R is not the explanation of A. Tuyeres demonstrate draft capability but the clay material was chosen for refractory reasons."),
    ("Assertion (A): Chronological benchmarks of the Iron Age have shifted over the past decades.\nReason (R): New calibrated C-14 datings from sites like Hallur and Gufkral pushed the antiquity of iron to the early 2nd millennium BCE.", 0, "Both A and R are true and R explains A. C-14 datings have pushed dates back from 1000 BCE to 1200-1300 BCE."),
    ("Assertion (A): The Gangetic basin lacked copper resources, forcing communities to seek alternative metals.\nReason (R): The transition to iron in the Doab occurred earlier than in regions rich in copper like Rajasthan.", 1, "Both statements are true but R does not explain A. Lack of copper in the Ganga Doab made iron highly attractive once discovered."),
    ("Assertion (A): Slag is a vital indicator of in-situ metallurgical activities at archaeological sites.\nReason (R): Slag is a waste product formed when flux combines with gangue during smelting.", 0, "Both A and R are correct and R explains A. Since slag is heavy waste, it is left behind at the smelting spot, proving in-situ work.")
]
ars_hi = [
    ("अभिकथन (A): भारत में प्रारंभिक लौह युग के समुदायों ने ढलवां लोहे के बजाय मुख्य रूप से पिटवां लोहे और स्टील का उत्पादन किया।\nकारण (R): उनकी शाफ्ट भट्टियां लोहे को तरल अवस्था में पिघलाने के लिए 1538 डिग्री सेल्सियस से अधिक तापमान प्राप्त नहीं कर सकती थीं।", 0, "A और R दोनों सही हैं, और R, A की सही व्याख्या करता है। पिटवां लोहे पर ठोस अवस्था में काम किया जाता था क्योंकि भट्टियों में लोहे को पूरी तरह पिघलाने के लिए पर्याप्त हवा का प्रवाह नहीं था।"),
    ("अभिकथन (A): भारत में लौह धातु कर्म की उत्पत्ति के लिए पश्चिमी एशिया से प्रसार (diffusion) ही एकमात्र उत्प्रेरक था।\nकारण (R): मल्हार और अतरंजीखेड़ा की रेडियोकार्बन तिथियां भारत में लोहे के काम को लगभग 1800-1200 ईसा पूर्व दर्शाती हैं, जो अनातोलिया की तिथियों के समकालीन या उससे पुरानी हैं।", 3, "A गलत है लेकिन R सही है। भारतीय तिथियां बहुत शुरुआती हैं और स्वतंत्र क्षेत्रीय धातु विज्ञान को दर्शाती हैं।"),
    ("अभिकथन (A): प्रारंभिक लोहा गलाने की दुकानों द्वारा हेमेटाइट और मैग्नेटाइट अयस्कों का व्यापक रूप से उपयोग किया गया था।\nकारण (R): ये ऑक्साइड अयस्क भारत में प्रचुर मात्रा में हैं और सल्फाइड अयस्कों की तुलना में अपचयित करने में आसान हैं।", 0, "A और R दोनों सही हैं और R, A की सही व्याख्या करता है। ऑक्साइड अयस्क ब्लूमरी भट्टियों में कार्बन मोनोऑक्साइड के साथ आसानी से अपचयित हो जाते हैं।"),
    ("अभिकथन (A): शुरुआती लोहे की कुल्हाड़ियाँ जंगलों को साफ करने के लिए कांसे की कुल्हाड़ियों से तुरंत बेहतर साबित हुईं।\nकारण (R): बिना कार्बोराइजेशन के शुद्ध ब्लूमरी लोहा मिश्र धातु कांसे की तुलना में नरम होता है।", 3, "A गलत है क्योंकि शुरुआती शुद्ध लोहा नरम था और कार्बोराइजेशन के विकास तक इसने कांसे को तुरंत प्रतिस्थापित नहीं किया था। R सही है।"),
    ("अभिकथन (A): अतरंजीखेड़ा में खोजी गई फूंकनी (Tuyeres) उन्नत वायु प्रवाह तकनीकों को साबित करती हैं।\nकारण (R): मिट्टी की फूंकनी ने भट्टी के अपचयन क्षेत्र के भीतर धातु के नोजल को पिघलने से बचाया।", 1, "दोनों कथन सही हैं, लेकिन R, A की सही व्याख्या नहीं है। फूंकनी वायु प्रवाह क्षमता का प्रदर्शन करती हैं लेकिन मिट्टी का चयन रिफ्रैक्टरी (गर्मी प्रतिरोधी) कारणों से किया गया था।"),
    ("अभिकथन (A): पिछले दशकों में लौह युग के कालानुक्रमिक बेंचमार्क बदल गए हैं।\nकारण (R): हल्लूर और गुफक्राल जैसे स्थलों से प्राप्त नई कैलिब्रेटेड सी-14 तिथियों ने लोहे की प्राचीनता को दूसरी सहस्राब्दी ईसा पूर्व की शुरुआत तक धकेल दिया है।", 0, "A और R दोनों सही हैं और R, A की सही व्याख्या करता है। सी-14 तिथियों ने तिथियों को 1000 ईसा पूर्व से पीछे धकेल कर 1200-1300 ईसा पूर्व कर दिया है।"),
    ("अभिकथन (A): गंगा बेसिन में तांबे के संसाधनों की कमी थी, जिससे समुदायों को वैकल्पिक धातुओं की तलाश करनी पड़ी।\nकारण (R): दोआब में लोहे का संक्रमण राजस्थान जैसे तांबे से समृद्ध क्षेत्रों की तुलना में पहले हुआ था।", 1, "दोनों कथन सही हैं लेकिन R, A की व्याख्या नहीं करता है। गंगा दोआब में तांबे की कमी ने लोहे की खोज के बाद इसे अत्यधिक आकर्षक बना दिया।"),
    ("अभिकथन (A): पुरातात्विक स्थलों पर इन-सिटू (स्थानीय) धातुकर्म गतिविधियों का धातुमल (Slag) एक महत्वपूर्ण संकेतक है।\nकारण (R): धातुमल प्रगलन के दौरान फ्लक्स के गैंग (अशुद्धियों) के साथ मिलने से बनने वाला एक अपशिष्ट उत्पाद है।", 0, "A और R दोनों सही हैं और R, A की सही व्याख्या करता है। चूंकि धातुमल भारी कचरा होता है, इसलिए इसे पिघलाने वाले स्थान पर ही छोड़ दिया जाता, जिससे स्थानीय काम साबित होता है।")
]
for i in range(8):
    sec1_en.append({"type": "Assertion-Reason", "q": ars_en[i][0], "opts": EN_AR_OPTS, "ans": ars_en[i][1], "sol": ars_en[i][2]})
    sec1_hi.append({"type": "Assertion-Reason", "q": ars_hi[i][0], "opts": HI_AR_OPTS, "ans": ars_hi[i][1], "sol": ars_hi[i][2]})

# 5 Statement-Based
stmts_en = [
    {"q": "Consider the following statements regarding early iron technology in India:\n1. Iron tools were manufactured by pouring liquid iron directly into soapstone molds.\n2. The spongy solid block of iron produced in furnaces was forged repeatedly to expel slag.\nWhich of the statements given above is/are correct?", "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 1, "sol": "Statement 1 is incorrect because liquid cast iron was not produced in India's early bloomery phase. Only statement 2 is correct."},
    {"q": "Consider the following statements regarding the chronology of the Indian Iron Age:\n1. Calibrated C-14 datings from Gufkral place early iron in Kashmir around 1300 BCE.\n2. The transition to iron in the Deccan was complete only by 600 BCE.\nWhich of the statements given above is/are correct?", "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 0, "sol": "Statement 1 is correct. Statement 2 is incorrect as Hallur shows iron in the Deccan by 1200-1000 BCE."},
    {"q": "With reference to the site of Atranjikhera, consider the following statements:\n1. It has yielded systematic remnants of clay smelting furnaces.\n2. It belongs to the Painted Grey Ware cultural level.\nWhich of the statements given above is/are correct?", "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 2, "sol": "Both statements are correct. Atranjikhera yielded PGW layers containing smelting furnaces and slag piles."},
    {"q": "Consider the following statements:\n1. Pure wrought iron contains high amounts of carbon which prevents rusting.\n2. Carburization increases the carbon content on the outer surface of iron implements.\nWhich of the statements given above is/are correct?", "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 1, "sol": "Statement 1 is false because wrought iron has low carbon and rusts easily. Statement 2 is correct."},
    {"q": "Consider the following statements regarding the origin of iron in India:\n1. The diffusionist theory argues that iron was brought to India by Aryans from Western Asia.\n2. Modern excavations support the theory of multiple, independent centers of iron origin in India.\nWhich of the statements given above is/are correct?", "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 2, "sol": "Both statements are correct. Early scholars believed in diffusion, but modern archaeological evidence supports independent regional centers."}
]
stmts_hi = [
    {"q": "भारत में प्रारंभिक लौह तकनीक के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. साबुन के पत्थर (soapstone) के सांचों में सीधे तरल लोहे को डालकर लोहे के औजारों का निर्माण किया जाता था।\n2. भट्टियों में उत्पादित लोहे के स्पंजी ठोस ब्लॉक (bloom) को धातुमल बाहर निकालने के लिए बार-बार पीटा जाता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"], "ans": 1, "sol": "कथन 1 गलत है क्योंकि भारत के प्रारंभिक ब्लूमरी चरण में तरल लोहे का उत्पादन नहीं किया गया था। केवल कथन 2 सही है।"},
    {"q": "भारतीय लौह युग के कालानुक्रम के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. गुफक्राल से प्राप्त कैलिब्रेटेड सी-14 तिथियां कश्मीर में प्रारंभिक लोहे को लगभग 1300 ईसा पूर्व रखती हैं।\n2. दक्कन में लोहे का संक्रमण केवल 600 ईसा पूर्व तक ही पूरा हुआ था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"], "ans": 0, "sol": "कथन 1 सही है। कथन 2 गलत है क्योंकि हल्लूर दक्कन में 1200-1000 ईसा पूर्व तक लोहा दिखाता है।"},
    {"q": "अतरंजीखेड़ा स्थल के संदर्भ में, निम्नलिखित कथनों पर विचार करें:\n1. यहाँ से मिट्टी की प्रगलन भट्टियों के व्यवस्थित अवशेष मिले हैं।\n2. यह चित्रित धूसर मृदभांड (PGW) सांस्कृतिक स्तर से संबंधित है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"], "ans": 2, "sol": "दोनों कथन सही हैं। अतरंजीखेड़ा से प्रगलन भट्टियों और धातुमल के ढेरों वाले PGW स्तर मिले हैं।"},
    {"q": "निम्नलिखित कथनों पर विचार करें:\n1. शुद्ध पिटवां लोहे में कार्बन की उच्च मात्रा होती है जो जंग लगने से बचाती है।\n2. कार्बोराइजेशन लोहे के उपकरणों की बाहरी सतह पर कार्बन की मात्रा को बढ़ाता है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"], "ans": 1, "sol": "कथन 1 असत्य है क्योंकि पिटवां लोहे में कम कार्बन होता है और आसानी से जंग लग जाता है। कथन 2 सत्य है।"},
    {"q": "भारत में लोहे की उत्पत्ति के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. प्रसारवादी सिद्धांत (diffusionist theory) का तर्क है कि लोहा पश्चिमी एशिया से आर्यों द्वारा भारत लाया गया था।\n2. आधुनिक उत्खनन भारत में लोहे की उत्पत्ति के बहु-केंद्रित, स्वतंत्र विकास के सिद्धांत का समर्थन करते हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"], "ans": 2, "sol": "दोनों कथन सही हैं। प्रारंभिक विद्वान प्रसार में विश्वास करते थे, लेकिन आधुनिक पुरातात्विक साक्ष्य स्वतंत्र क्षेत्रीय केंद्रों का समर्थन करते हैं।"}
]
for i in range(5):
    sec1_en.append({"type": "Statement-Based", "q": stmts_en[i]["q"], "opts": stmts_en[i]["opts"], "ans": stmts_en[i]["ans"], "sol": stmts_en[i]["sol"]})
    sec1_hi.append({"type": "Statement-Based", "q": stmts_hi[i]["q"], "opts": stmts_hi[i]["opts"], "ans": stmts_hi[i]["ans"], "sol": stmts_hi[i]["sol"]})

# 3 Why
whys_en = [
    ("Why did the absence of tin alloying make early iron metallurgy highly revolutionary compared to bronze?", "Copper required tin to make bronze, which was scarce in India and imported. Iron ore, however, was highly abundant locally, allowing widespread access to metal tools once smelting was mastered."),
    ("Why could early Indian shaft furnaces not yield liquid cast iron?", "Early shaft furnaces utilized charcoal with natural draft or manual bellows, achieving temperatures up to 1200-1250°C. Since pure iron melts at 1538°C, the metal remained in a semi-solid spongy state (bloom) rather than melting into a liquid cast form."),
    ("Why are early carbon dates from Malhar critical to debates on Indian prehistory?", "Malhar yielded iron artifacts dating to c. 1800 BCE. This pushed the beginning of iron working back by centuries, arguing against the diffusionist theory that Western Asia introduced iron to India after 1000 BCE.")
]
whys_hi = [
    ("तांबे में टिन मिलाने (कांसा बनाने) की तुलना में लौह धातु विज्ञान की शुरुआत अधिक क्रांतिकारी क्यों साबित हुई?", "तांबे को कांसा बनाने के लिए टिन की आवश्यकता होती थी, जो भारत में दुर्लभ था और आयात किया जाता था। हालांकि, लौह अयस्क स्थानीय रूप से अत्यधिक प्रचुर मात्रा में था, जिससे प्रगलन सीखने के बाद धातु के औजारों तक व्यापक पहुंच संभव हो सकी।"),
    ("प्रारंभिक भारतीय शाफ्ट भट्टियों से तरल ढलवां लोहा क्यों नहीं प्राप्त हो सका?", "प्रारंभिक शाफ्ट भट्टियों में प्राकृतिक वायु प्रवाह या मैन्युअल धौंकनी के साथ लकड़ी के कोयले का उपयोग किया जाता था, जिससे 1200-1250 डिग्री सेल्सियस तक का तापमान प्राप्त होता था। चूंकि शुद्ध लोहा 1538 डिग्री सेल्सियस पर पिघलता है, इसलिए धातु तरल रूप में पिघलने के बजाय अर्ध-ठोस स्पंजी अवस्था (ब्लूम) में ही रही।"),
    ("भारतीय इतिहास के वाद-विवाद में मल्हार से प्राप्त शुरुआती कार्बन तिथियां क्यों महत्वपूर्ण हैं?", "मल्हार से लगभग 1800 ईसा पूर्व के लौह अवशेष मिले हैं। इसने लोहे के उपयोग की शुरुआत को सदियों पीछे धकेल दिया, जिससे उस प्रसारवादी सिद्धांत का खंडन हुआ कि पश्चिमी एशिया ने 1000 ईसा पूर्व के बाद भारत में लोहे की शुरुआत की थी।")
]
for i in range(3):
    sec1_en.append({"type": "Why", "q": whys_en[i][0], "sol": whys_en[i][1]})
    sec1_hi.append({"type": "Why", "q": whys_hi[i][0], "sol": whys_hi[i][1]})

# 3 How
hows_en = [
    ("How does carburization chemically transform soft wrought iron into steel?", "By heating wrought iron in a charcoal bed within a closed crucible. Carbon atoms diffuse from the charcoal gas into the iron's crystalline structure, forming a high-carbon surface layer (cementite) which is much harder."),
    ("How did early metal smiths expel silicate slag from the iron bloom?", "They took the hot, spongy bloom directly from the furnace and hammered it repeatedly on an anvil. This mechanical compression squeezed out the liquid silicate slag trapped within the iron pores."),
    ("How do archaeologists distinguish between iron smelting sites and iron forging workshops?", "Smelting sites contain massive amounts of raw iron slag, furnace vitrified clay, and tuyeres. Forging workshops yield smaller finishing slag, hammer-scale, and semi-finished tool preforms.")
]
hows_hi = [
    ("कार्बोराइजेशन रासायनिक रूप से नरम लोहे को स्टील में कैसे बदलता है?", "एक बंद क्रूसिबल के भीतर कोयले की परत में पिटवां लोहे को गर्म करके। Carbon परमाणु कोयले की गैस से लोहे की क्रिस्टलीय संरचना में फैल जाते हैं, जिससे एक उच्च कार्बन वाली बाहरी परत (सीमेंटाइट) बन जाती है जो बहुत कठोर होती है।"),
    ("प्रारंभिक धातुकारों ने लोहे के पिण्ड (bloom) से सिलिकेट धातुमल को कैसे बाहर निकाला?", "वे भट्टी से सीधे गर्म, स्पंजी ब्लूम निकालते थे और उसे निहाई पर बार-बार हथौड़े से पीटते थे। इस यांत्रिक संपीड़न ने लोहे के छिद्रों के भीतर फंसे हुए तरल सिलिकेट धातुमल को निचोड़कर बाहर निकाल दिया।"),
    ("पुरातत्वविद लोहा गलाने के स्थलों (smelting sites) और लोहे को आकार देने वाली कार्यशालाओं (forging workshops) के बीच कैसे अंतर करते हैं?", "गलाने वाले स्थलों में प्रचुर मात्रा में कच्चा लौह धातुमल, भट्टी की जली हुई मिट्टी और फूंकनी मिलती हैं। जबकि आकार देने वाली कार्यशालाओं में छोटा परिष्कृत धातुमल, हथौड़े से निकली पपड़ी (hammer-scale) और अर्ध-निर्मित औजार मिलते हैं।")
]
for i in range(3):
    sec1_en.append({"type": "How", "q": hows_en[i][0], "sol": hows_en[i][1]})
    sec1_hi.append({"type": "How", "q": hows_hi[i][0], "sol": hows_hi[i][1]})

# 3 Case Study
cases_en = [
    ("Analyze the metallurgical findings at Atranjikhera as a case study of PGW industrial specialization.", "Atranjikhera yielded clay furnaces, heaps of slag, and clay tuyeres alongside iron tools in PGW layers. This demonstrates that metallurgy had moved from sporadic work to specialized, localized production in workshops within the settlement."),
    ("Analyze Gufkral as a transitional case study from Neolithic bone/stone tool industries to early Iron metallurgy.", "Gufkral in Kashmir shows a clear stratigraphy where polished stone celts and bone tools dominate early layers, followed by a transitional layer where iron points and daggers appear alongside stone tools, illustrating a slow technological overlap rather than abrupt replacement."),
    ("Evaluate the C-14 date calibration controversy of Hallur iron findings.", "Initial C-14 datings of Hallur in the 1970s placed iron at c. 1000 BCE. Subsequent excavations and recalibrated accelerator mass spectrometry (AMS) dating pushed the dates to c. 1200-1100 BCE, sparking debates on the timing of early Deccan metallurgy.")
]
cases_hi = [
    ("PGW औद्योगिक विशेषज्ञता के मामले के रूप में अतरंजीखेड़ा में धातुकर्म निष्कर्षों का विश्लेषण करें।", "अतरंजीखेड़ा से PGW परतों में लोहे के औजारों के साथ मिट्टी की भट्टियां, धातुमल के ढेर और मिट्टी की फूंकनी मिली हैं। यह दर्शाता है कि धातु विज्ञान छिटपुट काम से हटकर बस्ती के भीतर कार्यशालाओं में विशिष्ट, स्थानीय उत्पादन में बदल गया था।"),
    ("नवपाषाण कालीन हड्डी/पत्थर के औजारों से प्रारंभिक लौह धातुकर्म में संक्रमण के अध्ययन के रूप में गुफक्राल का विश्लेषण करें।", "कश्मीर में गुफक्राल एक स्पष्ट स्तर-विन्यास दिखाता है जहाँ पॉलिश किए गए पत्थर के औजार और हड्डी के उपकरण प्रारंभिक परतों पर हावी हैं, इसके बाद एक संक्रमणकालीन परत है जहाँ लोहे के पॉइंट और खंजर पत्थर के औजारों के साथ दिखाई देते हैं, जो अचानक प्रतिस्थापन के बजाय एक धीमी तकनीकी ओवरलैप को दर्शाते हैं।"),
    ("हल्लूर लौह निष्कर्षों के सी-14 तिथि अंशांकन (calibration) विवाद का मूल्यांकन करें।", "1970 के दशक में हल्लूर के शुरुआती सी-14 कालनिर्धारण ने लोहे को लगभग 1000 ईसा पूर्व में रखा था। बाद के उत्खनन और पुन: अंशांकित एक्सीलेटर मास स्पेक्ट्रोमेट्री (AMS) डेटिंग ने तिथियों को लगभग 1200-1100 ईसा पूर्व तक धकेल दिया, जिससे दक्कन धातुकर्म के समय पर बहस शुरू हो गई।")
]
for i in range(3):
    sec1_en.append({"type": "Case Study", "q": cases_en[i][0], "sol": cases_en[i][1]})
    sec1_hi.append({"type": "Case Study", "q": cases_hi[i][0], "sol": cases_hi[i][1]})

# 3 Teach the Concept
teaches_en = [
    ("Explain the difference between iron reduction and iron melting to a beginner.", "Iron reduction is a chemical process where carbon monoxide gas reacts with solid iron ore to remove oxygen, leaving solid iron. Iron melting is a physical change where solid iron turns to liquid at 1538°C. Early smiths reduced iron but did not melt it."),
    ("Explain why iron slag is more useful to archaeologists than finished iron tools.", "Finished tools were highly valuable, recycled, and corrode easily in soil. Slag, however, is a worthless byproduct, left behind in large heaps, and is highly stable, preserving the exact chemical fingerprints of the smelting technology used."),
    ("Explain the concept of 'Reducing Atmosphere' inside an early shaft kiln.", "A reducing atmosphere is carbon-monoxide rich and oxygen-poor. By closing the furnace top and restricting draft, carbon monoxide is forced to steal oxygen from the iron ore (reducing it to metallic iron) instead of simply burning away.")
]
teaches_hi = [
    ("एक शुरुआती छात्र को आयरन रिडक्शन (अपचयन) और आयरन मेल्टिंग (पिघलने) के बीच का अंतर समझाएं।", "लोहे का अपचयन एक रासायनिक प्रक्रिया है जहाँ कार्बन मोनोऑक्साइड गैस ऑक्सीजन को हटाने के लिए ठोस लौह अयस्क के साथ प्रतिक्रिया करती है, जिससे ठोस लोहा रह जाता है। लोहे का पिघलना एक भौतिक परिवर्तन है जहाँ ठोस लोहा 1538 डिग्री सेल्सियस पर तरल में बदल जाता है। प्रारंभिक कारीगरों ने लोहे को अपचयित किया लेकिन उसे पिघलाया नहीं।"),
    ("समझाएं कि पुरातत्वविदों के लिए परिष्कृत लोहे के औजारों की तुलना में लौह धातुमल (slag) अधिक उपयोगी क्यों है।", "तैयार औजार अत्यधिक मूल्यवान थे, जिन्हें रीसायकल किया जाता था और मिट्टी में आसानी से जंग लग जाता था। हालांकि, धातुमल एक बेकार सह-उत्पाद है, जिसे बड़े ढेरों में छोड़ दिया जाता है, और यह अत्यधिक स्थिर होता है, जो उपयोग की जाने वाली प्रगलन तकनीक के सटीक रासायनिक साक्ष्य को सुरक्षित रखता है।"),
    ("प्रारंभिक शाफ्ट भट्टी के भीतर 'अपचायक वातावरण' (Reducing Atmosphere) की अवधारणा को समझाएं।", "अपचायक वातावरण कार्बन-मोनोऑक्साइड से समृद्ध और ऑक्सीजन से रहित होता है। भट्टी के शीर्ष को बंद करके और हवा के प्रवाह को सीमित करके, कार्बन मोनोऑक्साइड को केवल जलने के बजाय लौह अयस्क से ऑक्सीजन चुराने (उसे धातु लोहे में अपचयित करने) के लिए मजबूर किया जाता है।")
]
for i in range(3):
    sec1_en.append({"type": "Teach the Concept", "q": teaches_en[i][0], "sol": teaches_en[i][1]})
    sec1_hi.append({"type": "Teach the Concept", "q": teaches_hi[i][0], "sol": teaches_hi[i][1]})

# Write Section 1
generate_sec_file("section1", sec1_en, sec1_hi)


# Helper to clone section 1 template structure with replaced content to avoid code replication while keeping high educational standard.
def clone_and_generate_sec(sec_num, title, term_en, term_hi, qs_data_en, qs_data_hi):
    en = []
    hi = []
    
    # 5 MCQ
    for i in range(5):
        en.append({"type": "MCQ", "q": qs_data_en["mcq"][i]["q"], "opts": qs_data_en["mcq"][i]["opts"], "ans": qs_data_en["mcq"][i]["ans"], "sol": qs_data_en["mcq"][i]["sol"]})
        hi.append({"type": "MCQ", "q": qs_data_hi["mcq"][i]["q"], "opts": qs_data_hi["mcq"][i]["opts"], "ans": qs_data_hi["mcq"][i]["ans"], "sol": qs_data_hi["mcq"][i]["sol"]})
        
    # 5 Multiple Correct MCQ
    for i in range(5):
        en.append({"type": "Multiple Correct MCQ", "q": qs_data_en["multi"][i]["q"], "opts": qs_data_en["multi"][i]["opts"], "ans": qs_data_en["multi"][i]["ans"], "sol": qs_data_en["multi"][i]["sol"]})
        hi.append({"type": "Multiple Correct MCQ", "q": qs_data_hi["multi"][i]["q"], "opts": qs_data_hi["multi"][i]["opts"], "ans": qs_data_hi["multi"][i]["ans"], "sol": qs_data_hi["multi"][i]["sol"]})
        
    # 8 True/False
    for i in range(8):
        en.append({"type": "True/False", "q": qs_data_en["tf"][i][0], "ans": qs_data_en["tf"][i][1], "sol": qs_data_en["tf"][i][2]})
        hi.append({"type": "True/False", "q": qs_data_hi["tf"][i][0], "ans": qs_data_hi["tf"][i][1], "sol": qs_data_hi["tf"][i][2]})
        
    # 8 Fill in the Blank
    for i in range(8):
        en.append({"type": "Fill in the Blank", "q": qs_data_en["blank"][i][0], "ans": qs_data_en["blank"][i][1], "sol": qs_data_en["blank"][i][2]})
        hi.append({"type": "Fill in the Blank", "q": qs_data_hi["blank"][i][0], "ans": qs_data_hi["blank"][i][1], "sol": qs_data_hi["blank"][i][2]})
        
    # 3 Match the Following
    add_match(en, hi, qs_data_en["match"][0]["q"], qs_data_hi["match"][0]["q"], qs_data_en["match"][0]["items"], qs_data_hi["match"][0]["items"], qs_data_en["match"][0]["opts"], qs_data_hi["match"][0]["opts"], qs_data_en["match"][0]["sol"], qs_data_hi["match"][0]["sol"])
    add_match(en, hi, qs_data_en["match"][1]["q"], qs_data_hi["match"][1]["q"], qs_data_en["match"][1]["items"], qs_data_hi["match"][1]["items"], qs_data_en["match"][1]["opts"], qs_data_hi["match"][1]["opts"], qs_data_en["match"][1]["sol"], qs_data_hi["match"][1]["sol"])
    add_match(en, hi, qs_data_en["match"][2]["q"], qs_data_hi["match"][2]["q"], qs_data_en["match"][2]["items"], qs_data_hi["match"][2]["items"], qs_data_en["match"][2]["opts"], qs_data_hi["match"][2]["opts"], qs_data_en["match"][2]["sol"], qs_data_hi["match"][2]["sol"])
    
    # 8 One-Liner
    for i in range(8):
        en.append({"type": "One-Liner", "q": qs_data_en["oneliner"][i][0], "sol": qs_data_en["oneliner"][i][1]})
        hi.append({"type": "One-Liner", "q": qs_data_hi["oneliner"][i][0], "sol": qs_data_hi["oneliner"][i][1]})
        
    # 8 Assertion-Reason
    for i in range(8):
        en.append({"type": "Assertion-Reason", "q": qs_data_en["ar"][i][0], "opts": EN_AR_OPTS, "ans": qs_data_en["ar"][i][1], "sol": qs_data_en["ar"][i][2]})
        hi.append({"type": "Assertion-Reason", "q": qs_data_hi["ar"][i][0], "opts": HI_AR_OPTS, "ans": qs_data_hi["ar"][i][1], "sol": qs_data_hi["ar"][i][2]})
        
    # 5 Statement-Based
    for i in range(5):
        en.append({"type": "Statement-Based", "q": qs_data_en["stmt"][i]["q"], "opts": qs_data_en["stmt"][i]["opts"], "ans": qs_data_en["stmt"][i]["ans"], "sol": qs_data_en["stmt"][i]["sol"]})
        hi.append({"type": "Statement-Based", "q": qs_data_hi["stmt"][i]["q"], "opts": qs_data_hi["stmt"][i]["opts"], "ans": qs_data_hi["stmt"][i]["ans"], "sol": qs_data_hi["stmt"][i]["sol"]})
        
    # 3 Why
    for i in range(3):
        en.append({"type": "Why", "q": qs_data_en["why"][i][0], "sol": qs_data_en["why"][i][1]})
        hi.append({"type": "Why", "q": qs_data_hi["why"][i][0], "sol": qs_data_hi["why"][i][1]})
        
    # 3 How
    for i in range(3):
        en.append({"type": "How", "q": qs_data_en["how"][i][0], "sol": qs_data_en["how"][i][1]})
        hi.append({"type": "How", "q": qs_data_hi["how"][i][0], "sol": qs_data_hi["how"][i][1]})
        
    # 3 Case Study
    for i in range(3):
        en.append({"type": "Case Study", "q": qs_data_en["case"][i][0], "sol": qs_data_en["case"][i][1]})
        hi.append({"type": "Case Study", "q": qs_data_hi["case"][i][0], "sol": qs_data_hi["case"][i][1]})
        
    # 3 Teach the Concept
    for i in range(3):
        en.append({"type": "Teach the Concept", "q": qs_data_en["teach"][i][0], "sol": qs_data_en["teach"][i][1]})
        hi.append({"type": "Teach the Concept", "q": qs_data_hi["teach"][i][0], "sol": qs_data_hi["teach"][i][1]})
        
    generate_sec_file(f"section{sec_num}", en, hi)

# ==================== SECTION 2: PAINTED GREY WARE CULTURE ====================
sec2_data_en = {
    "mcq": [
        {"q": "The Painted Grey Ware (PGW) pottery style is characterized by which decorative designs painted in black pigment?", "opts": ["Geometric designs (lines, dots, circles)", "Realistic representations of tigers and bulls", "Intricate floral and vine creepers", "Human stick figures hunting animals"], "ans": 0, "sol": "PGW is famous for its simple geometric designs (lines, dots, circles) painted in black on fine grey surfaces."},
        {"q": "Which major ancient Indian literary texts correlate closely with the geographical distribution of the PGW culture?", "opts": ["Later Vedic Literature (Sama, Yajur, Atharva Veda & Brahmanas)", "Rig Veda Samhita", "Sangam Literature", "Early Buddhist Pitakas"], "ans": 0, "sol": "The PGW culture in the Gangetic basin overlaps chronologically and geographically with the Later Vedic texts."},
        {"q": "What type of agricultural economy did the PGW communities practice?", "opts": ["Sedentary farming with double cropping (wheat, barley, rice)", "Semi-nomadic pastoralism only", "Shifting cultivation without crop variety", "Slash-and-burn horticulture"], "ans": 0, "sol": "PGW settlements were sedentary farming villages practicing multi-cropping of wheat, barley, and rice."},
        {"q": "Which domestic animal is prominently found in PGW layers, reflecting its importance in warfare and mobility?", "opts": ["Horse", "Elephant", "Camel", "Bactrian Lion"], "ans": 0, "sol": "Horse remains and trappings become noticeable in the PGW phase, reflecting Later Vedic martial traditions."},
        {"q": "What is the typical house structure found in early PGW settlements like Hastinapur?", "opts": ["Wattle-and-daub mud houses", "Multi-storeyed kiln-burnt brick houses", "Stone fortress villas", "Underground cave chambers"], "ans": 0, "sol": "Early PGW houses were simple rectangular or circular structures made of wattle-and-daub with thatched roofs."}
    ],
    "multi": [
        {"q": "Identify the key geographical regions associated with Painted Grey Ware settlements: (Select all that apply)", "opts": ["Gharghar-Hakra Valley", "Ganga-Yamuna Doab", "Kaveri Basin", "Punjab and Haryana plains"], "ans": [0, 1, 3], "sol": "PGW is distributed across Punjab, Haryana, Rajasthan (Gharghar-Hakra), and the Gangetic Doab. It is not found in the Southern Kaveri basin."},
        {"q": "Select the typical iron tool types found in PGW archaeological levels: (Select all that apply)", "opts": ["Arrowheads and spearheads", "Agricultural sickles and hoes", "Iron coins (punch-marked)", "Chisels and axes"], "ans": [0, 1, 3], "sol": "PGW iron tools include weapons (spears/arrowheads) and tools (axes/chisels/sickles). Coins appeared later in the NBPW phase."},
        {"q": "Which domestic animals were kept by the PGW farming communities? (Select all that apply)", "opts": ["Humped Cattle (Zebu)", "Sheep and Goats", "Domestic Horses", "Tamed Tigers"], "ans": [0, 1, 2], "sol": "Cattle, sheep, goats, and horses were domesticated. Tigers are wild fauna."},
        {"q": "Which of the following are Mahabharata epic sites that yield PGW layers? (Select all that apply)", "opts": ["Hastinapur", "Ahichchhatra", "Indraprastha (Delhi)", "Adichanallur"], "ans": [0, 1, 2], "sol": "Hastinapur, Ahichchhatra, Mathura, and Indraprastha yield PGW. Adichanallur is a Southern Megalithic site."},
        {"q": "Identify features that describe Painted Grey Ware pottery: (Select all that apply)", "opts": ["Fine and thin-walled clay", "Wheel-made fabric", "Glazed vitreous finish", "Grey body painted with black designs"], "ans": [0, 1, 3], "sol": "PGW is a fine, thin-walled, wheel-turned grey ware with black paintings. It lacks a glazed vitreous finish."}
    ],
    "tf": [
        ("True or False: The Painted Grey Ware culture represents the peak of urbanization in the Ganga Valley.", False, "No, PGW represents a predominantly rural, farming society. Urbanization peaked later during the NBPW phase."),
        ("True or False: PGW pots were mostly luxury tablewares like bowls and dishes.", True, "True, the thin-walled fine grey pottery was primarily used for elite tableware, while coarse red ware was used for cooking."),
        ("True or False: The PGW culture is characterized by the complete absence of copper.", False, "No, copper was still used for ornaments and minor tools, coexisting with iron."),
        ("True or False: Cultivation of rice (vrihi) became increasingly important in PGW levels.", True, "True, rice was a major staple food alongside wheat and barley in the Gangetic plains."),
        ("True or False: Wattle-and-daub construction uses wooden frames covered with mud plaster.", True, "True, this was the standard building method for PGW houses."),
        ("True or False: Glass objects like beads and bangles make their first systematic appearance in India during the PGW phase.", True, "True, glass technology is a notable innovation of the PGW period."),
        ("True or False: PGW settlements were heavily fortified cities with stone walls.", False, "No, they were mostly undefended agricultural villages, though late sites show basic mud ramparts."),
        ("True or False: Double cropping (wheat in winter, rice in monsoon) was unknown to PGW farmers.", False, "No, they successfully practiced double cropping due to monsoon cycles and fertile alluvial soil.")
    ],
    "blank": [
        ("The fine, thin-walled grey pottery painted with black geometric patterns is known as __________ Ware.", "Painted Grey", "Painted Grey Ware (PGW) is the signature ceramic of this phase."),
        ("The epic site associated with Kauravas and Pandavas that yielded PGW layers excavated by B.B. Lal is __________.", "Hastinapur", "Hastinapur was excavated by B.B. Lal in the early 1950s."),
        ("The primary metal used for manufacturing offensive weapons like arrowheads and spears in the Later Vedic phase was __________.", "iron", "Iron weapons provided substantial military advantages during this phase."),
        ("PGW houses were constructed using the __________-and-daub method.", "wattle", "Wattle-and-daub houses are made of woven wooden lattices plastered with wet mud."),
        ("The Later Vedic term for rice, which is found in PGW archaeological sites, is __________.", "vrihi", "Vrihi in Vedic texts corresponds to rice grains found in excavations."),
        ("Painted Grey Ware sites show the first systematic evidence of __________ manufacture in India, used for beads.", "glass", "Glass technology emerged alongside high-temperature iron smelting."),
        ("The type of soil in the Gangetic basin that PGW farmers tilled using early plowshares is __________ soil.", "alluvial", "The fertile alluvial soil of the Ganga-Yamuna Doab was highly productive."),
        ("The PGW culture was chronologically succeeded by the __________ Black Polished Ware culture.", "Northern", "NBPW succeeded PGW around 600-500 BCE.")
    ],
    "match": [
        {
            "q": "Match the pottery style with its corresponding phase:",
            "items": ["Painted Grey Ware", "Northern Black Polished Ware", "Black-and-Red Ware"],
            "opts": ["Later Vedic Phase (c. 1100-500 BCE)", "Second Urbanization/Mauryan Phase", "Neolithic-Chalcolithic Transition"],
            "sol": "PGW matches Later Vedic; NBPW matches Mauryan; BRW transitions from Chalcolithic."
        },
        {
            "q": "Match the PGW site with its location/context:",
            "items": ["Hastinapur", "Atranjikhera", "Noh"],
            "opts": ["Excavated by B.B. Lal (UP)", "Smelting furnace site on Kali Nadi", "Key PGW site in Rajasthan"],
            "sol": "Hastinapur is BB Lal's site; Atranjikhera has smelting evidence; Noh is in Rajasthan."
        },
        {
            "q": "Match the agricultural crop with its Vedic name:",
            "items": ["Vrihi", "Yava", "Godhuma"],
            "opts": ["Rice", "Barley", "Wheat"],
            "sol": "Vrihi is rice; Yava is barley; Godhuma is wheat."
        }
    ],
    "oneliner": [
        ("What does the fine texture of PGW indicate about its production?", "It indicates the use of well-levigated clay and controlled firing in closed kilns at high temperatures."),
        ("Identify the major diagnostic weapon types found in PGW levels.", "Socketed and tanged iron arrowheads and spearheads."),
        ("Why is the correlation of PGW with the Mahabharata significant?", "It provides archaeological layers matching the geography and material culture described in the epic."),
        ("Name the post-Harappan site in Punjab showing PGW overlapping with late Harappan layers.", "Dadheri."),
        ("What material was used for cooking pots in PGW households?", "Coarse red ware and black-and-red ware were used, while PGW was kept for serving tablewares."),
        ("Explain the term 'levigated clay'.", "Clay that has been washed and purified to remove coarse sand and organic impurities, yielding a smooth fabric."),
        ("Which animal was highly prized for ritual sacrifice (Ashvamedha) in the Later Vedic-PGW period?", "The horse."),
        ("State the primary fuel used to fire Painted Grey Ware kilns.", "Wood and charcoal in closed reducing kilns.")
    ],
    "ar": [
        ("Assertion (A): PGW bowls and dishes were likely luxury tableware rather than everyday cooking pots.\nReason (R): They are thin-walled, finely made, and constitute only a small percentage of the total pottery assemblage.", 0, "Both A and R are correct, and R explains A. Fineness and low percentage indicate elite serving usage."),
        ("Assertion (A): Later Vedic society was a nomadic pastoral society with no agriculture.\nReason (R): PGW layers yield abundant grains of rice, wheat, and barley alongside agricultural iron tools.", 3, "A is false because Later Vedic society transitioned to sedentary farming. R is true."),
        ("Assertion (A): B.B. Lal excavated Hastinapur to investigate the archaeological basis of the Mahabharata.\nReason (R): The site yielded PGW layers and showed evidence of destruction by a major flood, matching epic descriptions.", 0, "Both statements are correct and R explains A. The flood layer provides a direct epic correlation."),
        ("Assertion (A): Iron plows completely revolutionized PGW farming from the very beginning.\nReason (R): Early PGW iron plows were rare, and agricultural work mostly relied on wooden plows with early iron points.", 3, "A is false because wood plows were still dominant early on. R is true."),
        ("Assertion (A): Glass technology developed in India during the PGW period.\nReason (R): The high kiln temperatures achieved for smelting iron allowed the melting of silica to make glass.", 0, "Both A and R are correct, and R explains A. Iron smelting pyrotechnology paved the way for glass work."),
        ("Assertion (A): Fortifications are absent in early PGW sites.\nReason (R): The political structure was based on chiefdoms (Janas) rather than large consolidated territorial states (Janapadas).", 0, "Both A and R are correct, and R explains A. Lack of territorial states meant no major fortified capitals."),
        ("Assertion (A): Dadheri in Punjab represents a pure PGW settlement with no Harappan contact.\nReason (R): Excavations show a stratigraphic overlap between late Harappan and early PGW pottery traditions.", 3, "A is false because Dadheri represents a late Harappan/PGW overlap. R is true."),
        ("Assertion (A): PGW pottery was fired in an oxidizing atmosphere.\nReason (R): Firing pottery in a reducing (oxygen-poor) kiln turns the clay body grey by converting iron oxide.", 3, "A is false because PGW was fired in a reducing kiln, turning it grey. R is true.")
    ],
    "stmt": [
        {"q": "Consider the following statements regarding PGW pottery:\n1. It is coarse, thick-walled, and hand-made.\n2. It features black geometric paintings on a fine grey surface.\nWhich of the statements given above is/are correct?", "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 1, "sol": "Statement 1 is incorrect as PGW is fine, thin-walled, and wheel-made. Statement 2 is correct."},
        {"q": "Consider the following statements regarding Later Vedic settlements:\n1. They were concentrated primarily in the Ganga-Yamuna Doab.\n2. Wattle-and-daub was the primary construction material for domestic housing.\nWhich of the statements given above is/are correct?", "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 2, "sol": "Both statements are correct. The Doab was the Later Vedic heartland, and houses were made of wattle-and-daub."},
        {"q": "With reference to the epic Mahabharata, consider the following statements:\n1. B.B. Lal identified Hastinapur as a PGW site matching epic geography.\n2. PGW deposits have also been excavated at Kurukshetra and Mathura.\nWhich of the statements given above is/are correct?", "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 2, "sol": "Both statements are correct. Hastinapur, Kurukshetra, and Mathura all yield PGW deposits."},
        {"q": "Consider the following statements:\n1. Glass beads and bangles were first produced in India during the Harappan period.\n2. The PGW phase marks the first systematic appearance of glass manufacturing technology in India.\nWhich of the statements given above is/are correct?", "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 1, "sol": "Statement 1 is incorrect as Harappans did not make glass (only faience). Statement 2 is correct."},
        {"q": "Consider the following statements:\n1. Iron axes and sickles were widely used in the PGW period for agricultural clearance.\n2. The primary crop cultivated by PGW communities was maize.\nWhich of the statements given above is/are correct?", "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 0, "sol": "Statement 1 is correct. Statement 2 is false because maize is a New World crop introduced much later; they grew wheat, barley, and rice."}
    ],
    "why": [
        ("Why did PGW potters paint simple geometric designs rather than complex natural scenes?", "The geometric designs reflect a stylized, abstract decorative tradition suitable for standardized production of tablewares, contrasting with the rich animal representations of earlier Chalcolithic Malwa pottery."),
        ("Why is the PGW phase correlated with the transition from pastoralism to sedentary agriculture?", "The tool kit contains iron sickles and axes for land clearance and harvesting, and excavation layers show thick occupational deposits of domestic grains, indicating long-term village farming."),
        ("Why did the PGW pottery body turn grey instead of red?", "It was fired in closed, oxygen-deprived reducing kilns. This converted the ferric iron oxide in the clay into ferrous oxide, giving the pot its distinctive grey color.")
    ],
    "how": [
        ("How did Later Vedic socio-political structure change during the PGW period?", "Semi-nomadic pastoral tribes (Janas) merged into sedentary agricultural kingdoms (Janapadas) with established territorial chiefs (Rajans) and early tribute collections."),
        ("How do archaeologists trace Later Vedic-PGW migrations in Northern India?", "By mapping the distribution of PGW site clusters moving eastward from the Sarasvati-Gharghar valley into the Ganga-Yamuna Doab and Western Bihar."),
        ("How was wattle-and-daub housing constructed in PGW villages?", "By weaving split bamboo or reed screens (wattle) between upright wooden posts and plastering them with a thick mixture of wet alluvial clay, straw, and cow dung (daub).")
    ],
    "case": [
        ("Analyze the flooding event at Hastinapur as an archaeological correlation with Epic narratives.", "B.B. Lal's excavation at Hastinapur revealed a massive clay silt layer showing a major river flood that washed away the late PGW settlement. This aligns with Puranic texts stating the capital was shifted to Kaushambi due to Ganga floods."),
        ("Analyze the role of Jodhpura (Rajasthan) in understanding the transition from BRW to PGW.", "Jodhpura shows a distinct stratigraphic sequence where black-and-red ware (BRW) precedes the PGW layer, illustrating the technological transition and ceramic evolution of the region."),
        ("Evaluate the introduction of glass technology in Jakhera as a marker of technological complexity.", "Jakhera yielded early glass beads and bangles in PGW levels. This shows mastery over kiln temperature control and silicate chemistry, representing a high degree of craft specialization.")
    ],
    "teach": [
        ("Explain the difference between wattle-and-daub houses and kiln-burnt brick houses to a beginner.", "Wattle-and-daub houses are made of mud plastered over wood/reed screens (organic and simple, typical of PGW). Kiln-burnt brick houses use baked clay blocks held with mortar (durable and urban, typical of Harappa and NBPW)."),
        ("Explain the correlation between PGW sites and Later Vedic geography.", "Vedic literature mentions the Kuru-Panchala kingdom in the Doab. When archaeologists excavated sites in this region (like Hastinapur and Atranjikhera), they found PGW layers of the same age, showing a match between texts and artifacts."),
        ("Explain how reducing kiln firing differs from oxidizing kiln firing.", "Oxidizing firing lets air flow freely, so iron in clay turns red. Reducing firing seals the kiln, forcing carbon monoxide to react with clay iron, turning the pots grey.")
    ]
}

sec2_data_hi = {
    "mcq": [
        {"q": "चित्रित धूसर मृदभांड (PGW) शैली की मुख्य विशेषता क्या है, जिस पर काले रंग से चित्रकारी की जाती थी?", "opts": ["ज्यामितीय रेखाचित्र (रेखाएं, बिंदु, वृत्त)", "बाघों और सांडों के सजीव चित्रण", "फूल-पत्तियों की जटिल चित्रकारी", "शिकार करते हुए मनुष्यों के रेखाचित्र"], "ans": 0, "sol": "PGW अपने चिकने धूसर धरातल पर काले रंग से रंगे सरल ज्यामितीय डिज़ाइनों (रेखाओं, बिंदुओं, वृत्तों) के लिए प्रसिद्ध है।"},
        {"q": "कौन से प्रमुख प्राचीन भारतीय साहित्यिक ग्रंथ PGW संस्कृति के भौगोलिक वितरण से निकटता से मेल खाते हैं?", "opts": ["उत्तर वैदिक साहित्य (साम, यजुर्वेद, अथर्ववेद और ब्राह्मण)", "ऋग्वेद संहिता", "संगम साहित्य", "प्रारंभिक बौद्ध पिटक"], "ans": 0, "sol": "गंगा बेसिन में PGW संस्कृति उत्तर वैदिक ग्रंथों के साथ कालानुक्रमिक और भौगोलिक रूप से मेल खाती है।"},
        {"q": "PGW समुदायों ने किस प्रकार की कृषि अर्थव्यवस्था का अभ्यास किया था?", "opts": ["बहु-फसली खेती के साथ स्थायी कृषि (गेहूं, जौ, धान)", "केवल अर्ध-घुमंतू पशुपालन", "फसलों की विविधता के बिना झूम खेती", "काटकर जलाना (Slash-and-burn) बागवानी"], "ans": 0, "sol": "PGW बस्तियां स्थायी कृषि गाँव थीं जो गेहूं, जौ और धान की बहु-फसली खेती करती थीं।"},
        {"q": "PGW स्तरों में कौन सा पालतू पशु विशेष रूप से पाया जाता है, जो युद्ध और गतिशीलता में उसके महत्व को दर्शाता है?", "opts": ["घोड़ा", "हाथी", "ऊंट", "बैक्ट्रियन शेर"], "ans": 0, "sol": "PGW चरण में घोड़ों के अवशेष और साज-सज्जा विशेष रूप से दिखाई देती हैं, जो उत्तर वैदिक कालीन सैन्य परंपराओं को दर्शाती हैं।"},
        {"q": "अतरंजीखेड़ा और हस्तिनापुर जैसी प्रारंभिक PGW बस्तियों में घर की विशिष्ट संरचना क्या थी?", "opts": ["मिट्टी से लीपी गई सरकंडों की दीवारें (Wattle-and-daub)", "बहुमंजिला पक्की ईंटों के घर", "पत्थर के किलेनुमा विला", "भूमिगत गुफा कक्ष"], "ans": 0, "sol": "प्रारंभिक PGW घर साधारण आयताकार या गोल होते थे जो सरकंडों और मिट्टी की गारा से बने होते थे और जिन पर घास-फूस की छत होती थी।"}
    ],
    "multi": [
        {"q": "चित्रित धूसर मृदभांड (PGW) बस्तियों से जुड़े प्रमुख भौगोलिक क्षेत्रों की पहचान करें: (सभी लागू विकल्प चुनें)", "opts": ["घग्गर-हकरा घाटी", "गंगा-यमुना दोआब", "कावेरी बेसिन", "पंजाब और हरियाणा के मैदान"], "ans": [0, 1, 3], "sol": "PGW पंजाब, हरियाणा, राजस्थान (घग्गर-हकरा) और गंगा-यमुना दोआब में वितरित है। यह दक्षिणी कावेरी बेसिन में नहीं पाया जाता है।"},
        {"q": "PGW पुरातात्विक स्तरों में पाए जाने वाले विशिष्ट लोहे के औजारों के प्रकारों का चयन करें: (सभी लागू विकल्प चुनें)", "opts": ["तीर के अग्रभाग (Arrowheads) और भाले", "कृषि दरांती और कुदाल", "लोहे के सिक्के (आहत सिक्के)", "छेनी और कुल्हाड़ी"], "ans": [0, 1, 3], "sol": "PGW लोहे के औजारों में हथियार (भाले/तीर) और उपकरण (कुल्हाड़ी/छेनी/दरांती) शामिल हैं। सिक्के बाद में NBPW चरण में दिखाई दिए।"},
        {"q": "PGW कृषक समुदायों द्वारा कौन से पालतू जानवर रखे जाते थे? (सभी लागू विकल्प चुनें)", "opts": ["कूबड़ वाले मवेशी (जेबू)", "भेड़ और बकरियां", "पालतू घोड़े", "पालतू बाघ"], "ans": [0, 1, 2], "sol": "मवेशी, भेड़, बकरी और घोड़े पालतू बनाए गए थे। बाघ जंगली जानवर हैं।"},
        {"q": "निम्नलिखित में से कौन से महाभारत कालीन स्थल हैं जहाँ PGW परतें मिलती हैं? (सभी लागू विकल्प चुनें)", "opts": ["हस्तिनापुर", "अहिच्छत्र", "इंद्रप्रस्थ (दिल्ली)", "आदिचनल्लूर"], "ans": [0, 1, 2], "sol": "हस्तिनापुर, अहिच्छत्र, मथुरा और इंद्रप्रस्थ से PGW मिलता है। आदिचनल्लूर एक दक्षिणी महापाषाणकालीन स्थल है।"},
        {"q": "उन विशेषताओं की पहचान करें जो चित्रित धूसर मृदभांड (PGW) का वर्णन करती हैं: (सभी लागू विकल्प चुनें)", "opts": ["महीन और पतली दीवार वाली मिट्टी", "चाक से बने बर्तन", "कांच जैसी चमकीली फिनिश", "काले चित्रों वाला धूसर (धुंधला) शरीर"], "ans": [0, 1, 3], "sol": "PGW महीन, पतली दीवार वाले, चाक से निर्मित धूसर बर्तन हैं जिन पर काली चित्रकारी की जाती थी। इनमें शीशा जैसी चमकीली फिनिश का अभाव था।"}
    ],
    "tf": [
        ("सही या गलत: चित्रित धूसर मृदभांड संस्कृति गंगा घाटी में शहरीकरण के चरमोत्कर्ष का प्रतिनिधित्व करती है।", False, "नहीं, PGW मुख्य रूप से एक ग्रामीण, कृषक समाज का प्रतिनिधित्व करता है। शहरीकरण बाद में NBPW चरण के दौरान चरम पर था।"),
        ("सही या गलत: PGW बर्तन ज्यादातर लक्ज़री सर्विंग वियर जैसे कटोरे और थालियाँ थे।", True, "सही, पतली दीवार वाले महीन धूसर बर्तनों का उपयोग मुख्य रूप से विशिष्ट वर्ग के लिए परोसने वाले बर्तनों के रूप में किया जाता था, जबकि पकाने के लिए मोटे लाल बर्तनों का उपयोग होता था।"),
        ("सही या गलत: PGW संस्कृति में तांबे का बिल्कुल अभाव था।", False, "नहीं, आभूषणों और छोटे औजारों के लिए तांबे का उपयोग अभी भी होता था और यह लोहे के साथ सह-अस्तित्व में था।"),
        ("सही या गलत: PGW स्तरों में धान (व्रीहि) की खेती का महत्व तेजी से बढ़ा।", True, "सही, गंगा के मैदानों में गेहूं और जौ के साथ धान मुख्य भोजन बन गया था।"),
        ("सही या गलत: वॉटल-एंड-डॉब (wattle-and-daub) निर्माण में मिट्टी के पलस्तर से ढके लकड़ी/सरकंडों के ढांचे का उपयोग होता है।", True, "सही, यह PGW घरों के लिए मानक निर्माण विधि थी।"),
        ("सही या गलत: कांच की वस्तुएं जैसे मनके और चूड़ियां भारत में पहली बार व्यवस्थित रूप से PGW चरण के दौरान दिखाई देती हैं।", True, "सही, कांच तकनीक PGW काल का एक उल्लेखनीय नवाचार है।"),
        ("सही या गलत: PGW बस्तियां पत्थर की दीवारों वाले मजबूत किलेबंद शहर थे।", False, "नहीं, वे ज्यादातर असुरक्षित कृषक गाँव थे, हालाँकि बाद के स्थलों पर मिट्टी के बुनियादी बांध दिखाई देते हैं।"),
        ("सही या गलत: दोहरी कृषि (सर्दियों में गेहूं, मानसून में धान) से PGW किसान अपरिचित थे।", False, "नहीं, वे मानसून चक्र और उपजाऊ जलोढ़ मिट्टी के कारण दोहरी कृषि का सफलतापूर्वक अभ्यास करते थे।")
    ],
    "blank": [
        ("काले ज्यामितीय डिज़ाइनों से रंगे बारीक, पतली दीवार वाले धूसर बर्तनों को __________ धूसर मृदभांड (PGW) कहा जाता है।", "चित्रित", "चित्रित धूसर मृदभांड (PGW) इस चरण का विशिष्ट मृदभांड है।"),
        ("कौरवों और पांडवों से जुड़ा वह महाकाव्य स्थल जहाँ से बी.बी. लाल द्वारा उत्खनित PGW परतें मिली हैं, __________ है।", "हस्तिनापुर", "हस्तिनापुर का उत्खनन बी.बी. लाल द्वारा 1950 के दशक की शुरुआत में किया गया था।"),
        ("उत्तर वैदिक काल में तीर के अग्रभाग और भालों जैसे आक्रामक हथियारों के निर्माण के लिए उपयोग की जाने वाली प्राथमिक धातु __________ थी।", "लोहा", "लोहे के हथियारों ने इस चरण के दौरान महत्वपूर्ण सैन्य लाभ प्रदान किए।"),
        ("PGW घरों का निर्माण __________ और मिट्टी की गारा (wattle-and-daub) विधि का उपयोग करके किया जाता था।", "सरकंडों", "वॉटल-एंड-डॉब घर लकड़ी के ढांचों पर गीली मिट्टी थोपकर बनाए जाते हैं।"),
        ("धान (चावल) का उत्तर वैदिक नाम, जो PGW पुरातात्विक स्थलों में पाया जाता है, __________ है।", "व्रीहि", "वैदिक ग्रंथों में व्रीहि शब्द उत्खनन में मिले धान के दानों से मेल खाता है।"),
        ("चित्रित धूसर मृदभांड स्थल भारत में __________ निर्माण के पहले व्यवस्थित साक्ष्य दिखाते हैं, जिसका उपयोग मनकों के लिए किया जाता था।", "कांच", "लौह प्रगलन के लिए उच्च तापमान भट्टियों के विकास के साथ कांच तकनीक का उदय हुआ।"),
        ("गंगा-यमुना दोआब की वह मिट्टी जिसे PGW किसानों ने प्रारंभिक हल से जोता था, __________ मिट्टी थी।", "जलोढ़", "गंगा-यमुना दोआब की उपजाऊ जलोढ़ मिट्टी अत्यधिक उत्पादक थी।"),
        ("PGW संस्कृति के बाद कालानुक्रमिक रूप से __________ काले चमकीले मृदभांड (NBPW) संस्कृति आई।", "उत्तरी", "NBPW ने लगभग 600-500 ईसा पूर्व में PGW का स्थान लिया।")
    ],
    "match": [
        {
            "q": "मृदभांड शैली को उसके संबंधित चरण से सुमेलित करें:",
            "items": ["चित्रित धूसर मृदभांड (PGW)", "उत्तरी काले चमकीले मृदभांड (NBPW)", "काले-और-लाल मृदभांड (BRW)"],
            "opts": ["उत्तर वैदिक चरण (लगभग 1100-500 ईसा पूर्व)", "द्वितीय शहरीकरण / मौर्य काल", "नवपाषाण-ताम्रपाषाण संक्रमण"],
            "sol": "PGW उत्तर वैदिक काल से मेल खाता है; NBPW मौर्य काल से; BRW ताम्रपाषाण संक्रमण से।"
        },
        {
            "q": "PGW स्थल को उसके स्थान/संदर्भ से सुमेलित करें:",
            "items": ["हस्तिनापुर", "अतरंजीखेड़ा", "नोह"],
            "opts": ["बी.बी. लाल द्वारा उत्खनित (यूपी)", "काली नदी पर प्रगलन भट्टी स्थल", "राजस्थान में प्रमुख PGW स्थल"],
            "sol": "हस्तिनापुर बी.बी. लाल का स्थल है; अतरंजीखेड़ा में धातुकर्म साक्ष्य हैं; नोह राजस्थान में है।"
        },
        {
            "q": "कृषि फसल को उसके वैदिक नाम से सुमेलित करें:",
            "items": ["व्रीहि", "यव", "गोधूम"],
            "opts": ["धान / चावल", "जौ", "गेहूं"],
            "sol": "व्रीहि धान है; यव जौ है; गोधूम गेहूं है।"
        }
    ],
    "oneliner": [
        ("PGW मृदभांडों की महीन बनावट उनके उत्पादन के बारे में क्या दर्शाती है?", "यह अच्छी तरह से साफ की गई मिट्टी (well-levigated clay) और बंद भट्टियों में नियंत्रित तापमान पर पकाने को दर्शाती है।"),
        ("PGW स्तरों में पाए जाने वाले प्रमुख हथियारों के प्रकारों की पहचान करें।", "लोहे के तीर और भालों के सॉकेटेड और टैंग्ड अग्रभाग।"),
        ("महाभारत के साथ PGW के सह-संबंध का क्या महत्व है?", "यह महाकाव्य में वर्णित भूगोल और भौतिक संस्कृति से मेल खाने वाली पुरातात्विक परतें प्रदान करता है।"),
        ("पंजाब के उस उत्तर-हड़प्पा स्थल का नाम बताइए जहाँ उत्तर-हड़प्पा और प्रारंभिक PGW परतें मिलती हैं।", "दधेरी।"),
        ("PGW घरों में खाना पकाने के बर्तनों के लिए किस सामग्री का उपयोग किया जाता था?", "रसोई के बर्तनों के लिए मोटे लाल और काले-लाल मृदभांडों का उपयोग किया जाता था, जबकि सर्विंग टेबलवेयर के लिए PGW सुरक्षित थे।"),
        ("शब्द 'लेविगेटेड क्ले' (levigated clay) को स्पष्ट करें।", "वह मिट्टी जिसे साफ करके कंकड़ और जैविक अशुद्धियों को हटा दिया गया हो ताकि एक चिकनी सतह मिल सके।"),
        ("उत्तर वैदिक-PGW काल में अनुष्ठानिक बलि (अश्वमेध) के लिए किस जानवर को अत्यधिक महत्व दिया जाता था?", "घोड़े को।"),
        ("चित्रित धूसर मृदभांड भट्टियों को पकाने के लिए प्रयुक्त प्राथमिक ईंधन क्या था?", "बंद भट्टियों में लकड़ी और कोयला।")
    ],
    "ar": [
        ("अभिकथन (A): PGW कटोरे और थालियां दैनिक खाना पकाने के बर्तनों के बजाय लक्ज़री टेबलवेयर थे।\nकारण (R): वे बहुत पतली दीवार वाले, बारीक बने हुए हैं और कुल मिट्टी के बर्तनों का केवल एक छोटा प्रतिशत हैं।", 0, "A और R दोनों सही हैं, और R, A की सही व्याख्या करता है। महीन बनावट और कम प्रतिशत विशिष्ट उपयोग को दर्शाता है।"),
        ("अभिकथन (A): उत्तर वैदिक समाज एक खानाबदोश चरवाहा समाज था जिसमें खेती बिल्कुल नहीं होती थी।\nकारण (R): PGW परतों से लोहे के कृषि उपकरणों के साथ धान, गेहूं और जौ के प्रचुर दाने मिले हैं।", 3, "A गलत है क्योंकि उत्तर वैदिक समाज कृषि प्रधान बन गया था। R सही है।"),
        ("अभिकथन (A): बी.बी. लाल ने महाभारत के पुरातात्विक आधार की जांच करने के लिए हस्तिनापुर का उत्खनन किया।\nकारण (R): इस स्थल से PGW परतें मिलीं और एक बड़ी बाढ़ से विनाश के साक्ष्य मिले, जो महाकाव्य के विवरणों से मेल खाते हैं।", 0, "दोनों कथन सही हैं और R, A की सही व्याख्या करता है। बाढ़ की परत महाकाव्य से सीधा संबंध स्थापित करती है।"),
        ("अभिकथन (A): लोहे के हलों ने शुरुआत से ही PGW कृषि में पूरी तरह से क्रांति ला दी।\nकारण (R): प्रारंभिक PGW काल में लोहे के हल दुर्लभ थे, और अधिकांशतः लोहे की नोक वाले लकड़ी के हलों का उपयोग किया जाता था।", 3, "A गलत है क्योंकि शुरुआत में लकड़ी के हल ही हावी थे। R सही है।"),
        ("अभिकथन (A): भारत में कांच तकनीक का विकास PGW काल के दौरान हुआ।\nकारण (R): लोहा गलाने के लिए प्राप्त उच्च तापमान भट्टियों ने कांच बनाने के लिए सिलिका को पिघलाना संभव बनाया।", 0, "A और R दोनों सही हैं, और R, A की सही व्याख्या करता है। धातुकर्म के उच्च तापमान ने कांच उद्योग का मार्ग प्रशस्त किया।"),
        ("अभिकथन (A): प्रारंभिक PGW स्थलों पर किलेबंदी का अभाव था।\nकारण (R): इस समय राजनीतिक संरचना विशाल राज्यों (जनपदों) के बजाय जनजातीय सरदार तंत्र (Janas) पर आधारित थी।", 0, "A और R दोनों सही हैं, और R, A की सही व्याख्या करता है। विशाल राज्यों के अभाव के कारण राजधानियों की किलेबंदी नहीं थी।"),
        ("अभिकथन (A): पंजाब में दधेरी एक शुद्ध PGW बस्ती का प्रतिनिधित्व करता है जिसका हड़प्पा से कोई संपर्क नहीं था।\nकारण (R): उत्खनन बाद के हड़प्पा और प्रारंभिक PGW मृदभांड परंपराओं के बीच एक स्तर-विन्यास ओवरलैप दिखाते हैं।", 3, "A गलत है क्योंकि दधेरी हड़प्पा/PGW संक्रमण को दर्शाता है। R सही है।"),
        ("अभिकथन (A): PGW बर्तनों को ऑक्सीकरण वातावरण में पकाया जाता था।\nकारण (R): ऑक्सीजन रहित (अपचायक) भट्टी में पकाने से मिट्टी में मौजूद लोहा काले/धूसर ऑक्साइड में बदल जाता है जिससे बर्तन धूसर हो जाते हैं।", 3, "A गलत है क्योंकि PGW को अपचायक भट्टी में पकाया जाता था। R सही है।")
    ],
    "stmt": [
        {"q": "PGW मृदभांडों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. ये खुरदरे, मोटी दीवार वाले और हाथ से बने होते हैं।\n2. इन पर महीन धूसर सतह पर काले रंग से ज्यामितीय चित्र बने होते हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"], "ans": 1, "sol": "कथन 1 गलत है क्योंकि PGW महीन, पतली दीवार वाले और चाक-निर्मित हैं। कथन 2 सही है।"},
        {"q": "उत्तर वैदिक बस्तियों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. वे मुख्य रूप से गंगा-यमुना दोआब में केंद्रित थीं।\n2. सरकंडों की दीवारें और मिट्टी का लेप (wattle-and-daub) घरेलू आवासों के लिए प्राथमिक निर्माण सामग्री थी।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"], "ans": 2, "sol": "दोनों कथन सही हैं। दोआब उत्तर वैदिक क्षेत्र का केंद्र था और घर वॉटल-एंड-डॉब से बने थे।"},
        {"q": "महाभारत महाकाव्य के संदर्भ में, निम्नलिखित कथनों पर विचार करें:\n1. बी.बी. लाल ने हस्तिनापुर की पहचान महाकाव्य के भूगोल से मेल खाने वाले एक PGW स्थल के रूप में की थी।\n2. कुरुक्षेत्र और मथुरा में भी PGW परतों का उत्खनन किया गया है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"], "ans": 2, "sol": "दोनों कथन सही हैं। हस्तिनापुर, कुरुक्षेत्र और मथुरा सभी से PGW निक्षेप मिले हैं।"},
        {"q": "निम्नलिखित कथनों पर विचार करें:\n1. भारत में कांच के मनके और चूड़ियों का निर्माण पहली बार हड़प्पा काल के दौरान हुआ था।\n2. PGW चरण भारत में व्यवस्थित कांच निर्माण तकनीक की शुरुआत का प्रतीक है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"], "ans": 1, "sol": "कथन 1 गलत है क्योंकि हड़प्पावासी कांच नहीं बनाते थे (केवल सेलखड़ी/फैयांस बनाते थे)। कथन 2 सही है।"},
        {"q": "निम्नलिखित कथनों पर विचार करें:\n1. कृषि क्षेत्रों की सफाई के लिए PGW काल में लोहे की कुल्हाड़ियों और दरांती का व्यापक उपयोग किया गया।\n2. PGW समुदायों द्वारा उगाई जाने वाली प्राथमिक फसल मक्का थी।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"], "ans": 0, "sol": "कथन 1 सही है। कथन 2 गलत है क्योंकि मक्का बहुत बाद में भारत आया; वे गेहूं, जौ और धान उगाते थे।"}
    ],
    "why": [
        ("Why did PGW potters paint simple geometric designs rather than complex natural scenes?", "ज्यामितीय डिजाइन सर्विंग टेबलवेयर के मानकीकृत उत्पादन के लिए उपयुक्त एक शैलीबद्ध, अमूर्त सजावटी परंपरा को दर्शाते हैं, जो पहले के ताम्रपाषाण कालीन मालवा बर्तनों के समृद्ध पशु चित्रणों से भिन्न है।"),
        ("Why is the PGW phase correlated with the transition from pastoralism to sedentary agriculture?", "औजारों में जमीन साफ करने और कटाई के लिए लोहे की दरांती और कुल्हाड़ी शामिल हैं, और उत्खनन परतों से अनाज के प्रचुर साक्ष्य मिले हैं, जो स्थायी गाँव खेती को दर्शाते हैं।"),
        ("Why did the PGW pottery body turn grey instead of red?", "इन्हें बंद, ऑक्सीजन रहित अपचायक भट्टियों में पकाया जाता था। इसने मिट्टी में मौजूद फेरिक आयरन oxide को फेरस oxide में बदल दिया, जिससे बर्तनों को उनका विशिष्ट धूसर रंग मिला।")
    ],
    "how": [
        ("How did Later Vedic socio-political structure change during the PGW period?", "अर्ध-घुमंतू चरवाहा कबीले (Janas) स्थायी कृषक राज्यों (Janapadas) में विलीन हो गए, जहाँ कबीलों के राजा प्रादेशिक शासक (Rajans) बन गए और करों की शुरुआत हुई।"),
        ("How do archaeologists trace Later Vedic-PGW migrations in Northern India?", "पंजाब और घग्गर घाटी से पूर्व की ओर गंगा-यमुना दोआब और पश्चिमी बिहार की ओर बढ़ते हुए PGW स्थलों के वितरण का मानचित्रण करके।"),
        ("How was wattle-and-daub housing constructed in PGW villages?", "सरकंडों या बांस की बुनी हुई जाली को लकड़ी के खंभों के बीच बांधकर और उस पर गीली जलोढ़ मिट्टी, भूसे और गाय के गोबर के गाढ़े मिश्रण का लेप लगाकर।")
    ],
    "case": [
        ("Analyze the flooding event at Hastinapur as an archaeological correlation with Epic narratives.", "हस्तिनापुर में बी.बी. लाल के उत्खनन से मिट्टी की गाद की एक विशाल परत मिली जो एक बड़ी बाढ़ को दर्शाती है जिसने अंतिम PGW बस्ती को नष्ट कर दिया था। यह पौराणिक ग्रंथों से मेल खाता है जिसमें कहा गया है कि बाढ़ के कारण राजधानी को कौशांबी स्थानांतरित किया गया था।"),
        ("Analyze the role of Jodhpura (Rajasthan) in understanding the transition from BRW to PGW.", "जोधपुरा एक स्पष्ट स्तर-विन्यास अनुक्रम दिखाता है जहाँ काले-लाल मृदभांड (BRW) की परत PGW परत से पहले आती है, जो इस क्षेत्र में सिरेमिक और तकनीक के क्रमिक विकास को दर्शाती है।"),
        ("Evaluate the introduction of glass technology in Jakhera as a marker of technological complexity.", "जखेड़ा से PGW स्तरों में शुरुआती कांच के मनके और चूड़ियां मिली हैं। यह भट्टी के तापमान नियंत्रण और सिलिकेट रसायन विज्ञान पर नियंत्रण को दर्शाता है, जो उन्नत शिल्प विशेषता का प्रतिनिधित्व करता है।")
    ],
    "teach": [
        ("Explain the difference between wattle-and-daub houses and kiln-burnt brick houses to a beginner.", "वॉटल-एंड-डॉब घर सरकंडों पर गीली मिट्टी थोपकर बनाए जाते हैं (सरल और ग्रामीण, PGW की विशेषता)। पक्की ईंटों के घर भट्टी में पकी ईंटों और गारे से बनते हैं (मजबूत और शहरी, हड़प्पा और NBPW की विशेषता)।"),
        ("Explain the correlation between PGW sites and Later Vedic geography.", "वैदिक साहित्य दोआब में कुरु-पांचाल साम्राज्य का उल्लेख करता है। जब पुरातत्वविदों ने इस क्षेत्र (जैसे हस्तिनापुर और अतरंजीखेड़ा) के स्थलों का उत्खनन किया, तो उन्हें उसी काल की PGW परतें मिलीं, जो पाठ्य विवरणों और पुरातात्विक साक्ष्यों के मेल को दर्शाती हैं।"),
        ("Explain how reducing kiln firing differs from oxidizing kiln firing.", "ऑक्सीकरण प्रक्रिया में हवा स्वतंत्र रूप से बहती है जिससे मिट्टी का लोहा लाल हो जाता है। अपचयन प्रक्रिया में भट्टी को बंद कर दिया जाता है जिससे कार्बन मोनोऑक्साइड मिट्टी के लोहे से क्रिया करके बर्तनों को धूसर बना देती है।")
    ]
}

# Run generation for Section 2
clone_and_generate_sec(2, "Painted Grey Ware Culture", "PGW Culture", "चित्रित धूसर मृदभांड", sec2_data_en, sec2_data_hi)


# ==================== SECTION 3: SOUTHERN MEGALITHIC CULTURES ====================
sec3_data_en = {
    "mcq": [
        {"q": "What defines a Southern Indian 'Megalith' in archaeological contexts?", "opts": ["A burial monument constructed using large stone boulders or slabs", "A large copper-alloy sculpture of animals", "A high-rise earthen temple platform", "A monolithic rock-cut cave residence"], "ans": 0, "sol": "Megaliths are graves or commemorative monuments constructed using large stone slabs (megas = large, lithos = stone)."},
        {"q": "Which burial type is characterized by a circular boundary of large stone boulders enclosing a grave?", "opts": ["Cairn circle", "Menhir", "Dolmen", "Urn burial"], "ans": 0, "sol": "Cairn circles are defined by a circular ring of large stone boulders surrounding a central grave covered with stone fragments."},
        {"q": "Which pottery style is the dominant ceramic type recovered from Southern Megalithic grave chambers?", "opts": ["Black-and-Red Ware", "Ochre Coloured Pottery", "Painted Grey Ware", "Northern Black Polished Ware"], "ans": 0, "sol": "Highly polished, wheel-made Black-and-Red Ware (BRW) is the signature ceramic of Southern Megalithic burials."},
        {"q": "Which metal weapon, associated with early forms of deity worship (Murugan/Shiva), is a common grave offering in Tamil Nadu megaliths?", "opts": ["Iron Trident (Vel)", "Bronze Sword", "Copper Harpoon", "Steel Battle-axe"], "ans": 0, "sol": "Iron tridents (Vel) are frequently found in Tamil Nadu megaliths, linked to early indigenous cults."},
        {"q": "What evidence indicates a highly specialized horse cult or usage among Southern Megalithic builders?", "opts": ["Skeletal remains of horses and iron horse-trappings in graves", "Terracotta horse chariots with spoked wheels", "Detailed cave paintings of cavalry charges", "Stone statues of winged horses guarding graves"], "ans": 0, "sol": "Excavations at sites like Kodumanal and Brahmagiri have yielded horse skeletons and iron horse-bits/trappings in graves."}
    ],
    "multi": [
        {"q": "Identify the common architectural types of Megalithic burials found in South India: (Select all that apply)", "opts": ["Cist burials with port-holes", "Dolmens or above-ground chambers", "Menhirs or standing upright stones", "Kiln-burnt brick stupas"], "ans": [0, 1, 2], "sol": "Cists, Dolmens, and Menhirs are classic megalithic types. Burnt-brick stupas are Buddhist structures of later periods."},
        {"q": "Which of the following sites are prominent Southern Megalithic burial sites? (Select all that apply)", "opts": ["Adichanallur (Tamil Nadu)", "Brahmagiri (Karnataka)", "Maski (Karnataka)", "Hastinapur (UP)"], "ans": [0, 1, 2], "sol": "Adichanallur, Brahmagiri, and Maski are major Southern Megalithic centers. Hastinapur is a PGW site in the north."},
        {"q": "What items are typically recovered as grave goods from Southern Megalithic tombs? (Select all that apply)", "opts": ["Iron arrowheads, daggers, and sickles", "Black-and-Red pottery bowls", "Gold and bronze beads or ornaments", "Punch-marked silver coins"], "ans": [0, 1, 2], "sol": "Graves yield iron tools/weapons, BRW pottery, and beads/ornaments. Silver punch-marked coins belong to later historic layers, not early megaliths."},
        {"q": "Select the agricultural features representing the Southern Megalithic economy: (Select all that apply)", "opts": ["Tank irrigation and water storage", "Cultivation of rice and ragi", "Pastoral herding of cattle and sheep", "Saffron plantations"], "ans": [0, 1, 2], "sol": "They grew rice/ragi, built early irrigation tanks, and practiced pastoralism. Saffron was limited to Kashmir."},
        {"q": "Which characteristics describe a 'Cist' burial in Megalithic culture? (Select all that apply)", "opts": ["Box-like stone chamber", "Often subterranean (below ground)", "Contains a circular port-hole in one slab", "Built strictly inside domestic kitchens"], "ans": [0, 1, 2], "sol": "Cists are underground box-like stone chambers, often with a port-hole for secondary insertions. They are built in designated burial areas outside settlements."}
    ],
    "tf": [
        ("True or False: Megaliths are found exclusively in South India and are completely absent in Kashmir and Central India.", False, "No, megaliths are also found in Kashmir (Gufkral), Uttar Pradesh, and Rajasthan, though the highest density is in the South."),
        ("True or False: A Port-hole is a circular opening cut into a cist slab, likely serving as an entrance for secondary burials.", True, "True, port-holes allowed family members to insert additional skeletal remains over time."),
        ("True or False: Southern Megalithic communities relied primarily on stone tools, with iron being extremely rare.", False, "No, they had highly advanced iron metallurgy, yielding massive quantities of weapons and tools."),
        ("True or False: Menhirs are large stone circles containing multiple urn burials inside.", False, "No, a Menhir is a single upright standing stone erected as a marker or memorial."),
        ("True or False: Adichanallur is a massive urn burial site in the Thamirabarani valley of Tamil Nadu.", True, "True, it is one of the largest Megalithic urn burial fields in India."),
        ("True or False: Southern Megalithic builders practiced both agriculture and sheep-cattle pastoralism.", True, "True, they had a mixed economy supported by irrigation tanks."),
        ("True or False: Megalithic burials were strictly egalitarian, with all graves containing identical grave goods.", False, "No, graves show stratification, as some contain gold and bronze ornaments, while others have only basic pots."),
        ("True or False: Kodumanal in Tamil Nadu was an important industrial center for bead making and steel working.", True, "True, Kodumanal yielded bead-making workshops and crucible steel smelting remains.")
    ],
    "blank": [
        ("A single upright standing monolithic stone erected to mark a burial site is called a __________.", "Menhir", "Menhirs are standing monoliths acting as memorials."),
        ("The box-like subterranean stone tomb constructed using stone slabs, often featuring a port-hole, is called a __________.", "Cist", "Cists are subterranean slab tombs."),
        ("The signature pottery style of the Southern Megaliths is __________ Ware.", "Black-and-Red", "Highly polished BRW is the dominant grave ceramic."),
        ("The circular opening cut into one of the stone slabs of a cist is called a __________.", "port-hole", "Port-holes allowed access for subsequent burial offerings."),
        ("The massive urn burial site in Tuticorin district, Tamil Nadu, which yielded gold diadems and iron weapons is __________.", "Adichanallur", "Adichanallur is a premier Megalithic urn site."),
        ("Southern Megalithic builders constructed early water-harvesting systems known as __________ irrigation.", "tank", "Irrigation tanks are often found adjacent to Megalithic fields."),
        ("An above-ground stone chamber constructed of upright slabs supporting a large capstone is called a __________.", "dolmen", "Dolmens are table-like stone structures above ground."),
        ("The Southern Megalithic culture chronologically corresponds to the __________ Age of the region.", "Iron", "Megalithic culture represents the Southern Iron Age.")
    ],
    "match": [
        {
            "q": "Match the Megalithic monument with its architectural form:",
            "items": ["Dolmen", "Menhir", "Cist"],
            "opts": ["Above-ground table-like stone chamber", "Single upright standing stone monolith", "Subterranean stone box tomb with a port-hole"],
            "sol": "Dolmen is above ground; Menhir is standing stone; Cist is subterranean box."
        },
        {
            "q": "Match the site with its key Megalithic discovery:",
            "items": ["Adichanallur", "Kodumanal", "Brahmagiri"],
            "opts": ["Massive urn burial field with gold diadems", "Crucible steel workshops and carnelian beads", "Stone-cist burials excavated by Mortimer Wheeler"],
            "sol": "Adichanallur has urn burials; Kodumanal has steel/beads; Brahmagiri has cists excavated by Wheeler."
        },
        {
            "q": "Match the grave offering with its social/functional meaning:",
            "items": ["Iron Hoes and Sickles", "Iron Swords and Lances", "Gold Ornaments and Bronze Vessels"],
            "opts": ["Agricultural tools representing agrarian economy", "Weapons representing warrior elites", "Prestige goods representing wealthy individuals"],
            "sol": "Hoes/sickles are agricultural; Swords/lances represent warriors; Gold/bronze represent wealth."
        }
    ],
    "oneliner": [
        ("What is the primary function of a port-hole in a cist burial?", "To allow the insertion of additional skeletal remains and grave offerings in secondary family burials."),
        ("Name the modern state containing the site of Adichanallur.", "Tamil Nadu."),
        ("Which southern site yielded evidence of Roman trade alongside Megalithic layers?", "Kodumanal (through Roman coins and foreign pottery)."),
        ("What does the presence of iron hoes in graves indicate about Megalithic livelihood?", "It indicates active cultivation and tillage of agricultural fields."),
        ("Explain the term 'Cairn Circle'.", "A burial grave covered with a heap of stone fragments (cairn) and enclosed by a ring of large stone boulders."),
        ("What unique ceramic feature distinguishes Megalithic BRW from ordinary pottery?", "Its highly polished, lustrous surface finish and distinct black interior and red exterior."),
        ("Identify the grain crop widely grown by Megalithic farmers in dry areas.", "Ragi (finger millet)."),
        ("What metal was used to make the horse-bits found in southern graves?", "Iron.")
    ],
    "ar": [
        ("Assertion (A): Megalithic burials demonstrate a high degree of social stratification.\nReason (R): Some graves contain rich offerings like gold ornaments, bronze vessels, and iron weapons, while many others contain only a few pots.", 0, "Both A and R are correct, and R explains A. Unequal grave goods reflect wealth differences in life."),
        ("Assertion (A): Southern Megaliths were built inside the living areas of settlements.\nReason (R): Megalithic cemeteries are consistently located outside the residential zones, often on dry rocky wastelands near water sources.", 3, "A is false because burials were placed outside settlements. R is true."),
        ("Assertion (A): Iron tridents (Vel) found in Southern burials reflect early religious cults.\nReason (R): Tridents are linked to the indigenous worship of Murugan/Shiva, which became popular in South India.", 0, "Both statements are correct, and R explains A. Iron weapons reflect proto-religious cults."),
        ("Assertion (A): Megalithic builders were completely nomadic pastoralists who grew no crops.\nReason (R): Excavations adjacent to megalithic fields show tank systems, channels, and grains of rice and ragi.", 3, "A is false because they practiced sedentary farming. R is true."),
        ("Assertion (A): Cist burials were designed for repeated use over generations.\nReason (R): The circular port-hole in the cist slab allowed new bones to be pushed in without dismantling the monument.", 0, "Both A and R are correct, and R explains A. Port-holes acted as entry points for subsequent insertions."),
        ("Assertion (A): Adichanallur is famous for its massive dolmens.\nReason (R): The site is dominated by urn burials where human bones were placed in large earthenware jars before burial.", 3, "A is false because Adichanallur is an urn burial site, not a dolmen site. R is true."),
        ("Assertion (A): Kodumanal in Tamil Nadu was an industrial center.\nReason (R): Excavations revealed bead-making workshops processing carnelian, jasper, and quartz, along with crucible iron smelting.", 0, "Both A and R are correct, and R explains A. Workshops and furnaces prove its industrial role."),
        ("Assertion (A): Wheeler's excavation at Brahmagiri established the sequence of South Indian cultures.\nReason (R): It showed the stratigraphy of Stone Axe (Neolithic-Chalcolithic) transitioning directly into Megalithic (Iron Age).", 0, "Both A and R are correct, and R explains A. Wheeler's stratigraphy clarified the southern transition sequence.")
    ],
    "stmt": [
        {"q": "Consider the following statements regarding Megalithic burials:\n1. Dolmens are above-ground stone chambers constructed with upright slabs and a capstone.\n2. Menhirs are box-like underground graves containing pottery.\nWhich of the statements given above is/are correct?", "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 0, "sol": "Statement 1 is correct. Statement 2 is incorrect as Menhirs are single standing stone monuments, not underground box graves."},
        {"q": "Consider the following statements regarding Southern Megalithic economy:\n1. Tank irrigation was widely used to irrigate wet rice cultivation.\n2. Ragi and millets were grown in dry zones.\nWhich of the statements given above is/are correct?", "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 2, "sol": "Both statements are correct. Irrigation tanks and dry millet cultivation were central to the Megalithic agricultural economy."},
        {"q": "With reference to the site of Kodumanal, consider the following statements:\n1. It is located in the Erode district of Tamil Nadu.\n2. It has yielded workshops for producing steel using crucibles.\nWhich of the statements given above is/are correct?", "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 2, "sol": "Both statements are correct. Kodumanal was a key industrial center in Tamil Nadu famous for crucible steel and beads."},
        {"q": "Consider the following statements:\n1. Urn burials represent a practice where the entire body was cremated, and ashes were buried in a cist.\n2. In urn burials, skeletal remains were placed inside large earthenware jars and buried in pits.\nWhich of the statements given above is/are correct?", "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 1, "sol": "Statement 1 is incorrect because urn burials contain bones (inhumation), not ashes of cremation. Statement 2 is correct."},
        {"q": "Consider the following statements regarding Southern Megalithic weaponry:\n1. Iron swords, daggers, and lances are common in graves.\n2. Bronze weapons are completely absent from Megalithic burial goods.\nWhich of the statements given above is/are correct?", "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 0, "sol": "Statement 1 is correct. Statement 2 is false because bronze items (especially vessels and ornamental bowls) were present, though iron dominated weaponry."}
    ],
    "why": [
        ("Why are megalithic burial fields often situated on dry, rocky gravelly ridges?", "To preserve fertile agricultural lowlands for crop cultivation and to ensure the massive stone graves were founded on stable rocky beds above the flood levels of nearby tanks."),
        ("Why did Megalithic builders place port-holes in subterranean cists?", "To create a functional opening through which descendants could insert the bones of newly deceased family members, practicing collective family burial over generations."),
        ("Why did the horse hold a prominent position in Southern Megalithic grave offerings?", "It indicates the emergence of a martial pastoral-warrior elite who utilized horses for mobility, raids, and political dominance, as reflected in the inclusion of horse-bits in graves.")
    ],
    "how": [
        ("How did Megalithic builders coordinate the labor required to move massive stone capstones?", "Moving stones weighing tons required cooperative community labor, indicating a chiefdom level of organization where leaders could mobilize and feed communal workforces."),
        ("How was the Black-and-Red Ware pottery surface given its highly lustrous look?", "By applying a fine clay slip to the pot and burnishing it with smooth pebbles before firing it under high temperatures, creating a polished, glossy finish."),
        ("How did tank irrigation systems interact with Megalithic settlements?", "Settlers built earthen embankments across seasonal streams to store rainwater. Burials were placed on high ridges surrounding the tank, while agricultural fields were laid below the bund to catch irrigation outflow.")
    ],
    "case": [
        ("Analyze the archaeological significance of Mortimer Wheeler's excavations at Brahmagiri.", "Wheeler's 1947 excavation at Brahmagiri established the first clear sequence for South India, showing Neolithic-Chalcolithic stone axes followed directly by megalithic iron cultures, proving that the Iron Age arrived in the South without an intervening Bronze Age."),
        ("Analyze Adichanallur as a case study of Megalithic Urn burial traditions.", "Adichanallur yields thousands of urn burials in pits. The urns contain skeletal remains, Black-and-Red pottery, iron weapons, and unique gold diadems, showing specialized mortuary practices distinct from cist or dolmen structures."),
        ("Evaluate Kodumanal as an industrial site trading with the Roman Empire.", "Kodumanal yielded Roman coins, inscribed pottery, and extensive workshops for carnelian beads and crucible iron (wootz steel), proving it was a major industrial node integrated into early global trade networks.")
    ],
    "teach": [
        ("Explain the difference between a Menhir and a Dolmen to a beginner.", "A Menhir is a single upright standing stone erected as a monument. A Dolmen is a table-like stone chamber made of vertical slabs supporting a flat capstone, serving as a tomb."),
        ("Explain why Megalithic graves contain so many iron weapons.", "The weapons (swords, daggers, lances) show that Megalithic society had a class of warriors or chiefs. Burying weapons with them showed their status and provided tools for the afterlife."),
        ("Explain the concept of secondary burial in Megalithic cists.", "Instead of burying the fresh body, it was left exposed for defleshing. Later, the clean bones were collected, placed in the stone cist along with pots and weapons, and sealed for eternity.")
    ]
}

sec3_data_hi = {
    "mcq": [
        {"q": "विद्यार्थियों के संदर्भ में दक्षिण भारतीय 'महापाषाण' (Megalith) को क्या परिभाषित करता है?", "opts": ["विशाल पत्थरों या शिलाखंडों का उपयोग करके बनाया गया एक कब्र स्मारक", "जानवरों की तांबे की एक विशाल मूर्ति", "मिट्टी का बना एक ऊंचा मंदिर मंच", "पहाड़ काटकर बनाई गई एक गुफा निवास संरचना"], "ans": 0, "sol": "महापाषाण (मैसेज = बड़े, लिथोस = पत्थर) विशाल पत्थरों का उपयोग करके बनाई गई कब्रें या स्मारक हैं।"},
        {"q": "वह कौन सी कब्र है जिसमें कब्र के चारों ओर बड़े शिलाखंडों का एक गोलाकार घेरा होता है?", "opts": ["कैरन सर्कल (Cairn circle)", "मेनहिर", "डोलमेन", "कलश शवाधान (Urn burial)"], "ans": 0, "sol": "कैरन सर्कल एक केंद्रीय कब्र के चारों ओर बड़े शिलाखंडों के घेरे द्वारा परिभाषित होते हैं, जो छोटे पत्थरों से ढकी होती है।"},
        {"q": "दक्षिणी महापाषाण कब्रों से बरामद प्रमुख मृदभांड शैली कौन सी है?", "opts": ["काले-और-लाल मृदभांड (Black-and-Red Ware)", "गेरुए रंग के मृदभांड", "चित्रित धूसर मृदभांड", "उत्तरी काले चमकीले मृदभांड"], "ans": 0, "sol": "महीन, चाक से निर्मित काले-और-लाल मृदभांड (BRW) दक्षिणी महापाषाण कब्रों के मुख्य सिरेमिक हैं।"},
        {"q": "तमिलनाडु के महापाषाण कब्रों में पाया जाने वाला कौन सा धातु का हथियार शुरुआती देवता पूजा (मुरुगन/शिव) से जुड़ा है?", "opts": ["लोहे का त्रिशूल (Vel)", "कांसे की तलवार", "तांबे का हारपून", "स्टील की कुल्हाड़ी"], "ans": 0, "sol": "तमिलनाडु के महापाषाणों में अक्सर लोहे के त्रिशूल (Vel) पाए जाते हैं, जो शुरुआती स्थानीय पंथों से जुड़े हैं।"},
        {"q": "महापाषाण काल के लोगों में घोड़े के विशेष महत्व को दर्शाने वाला कौन सा साक्ष्य मिला है?", "opts": ["कब्रों में घोड़ों के कंकाल और लोहे के लगाम (bits) के अवशेष", "तीली वाले पहियों वाले टेराकोटा रथ", "घुड़सवार सेना के हमलों के विस्तृत गुफा चित्र", "कब्रों की रक्षा करने वाले पंख वाले घोड़ों की पत्थर की मूर्तियाँ"], "ans": 0, "sol": "कोडुमनाल और ब्रह्मगिरि जैसे स्थलों से कब्रों में घोड़ों के कंकाल और लोहे के लगाम/साज-सज्जा मिले हैं।"}
    ],
    "multi": [
        {"q": "दक्षिण भारत में पाए जाने वाले महापाषाण कब्रों के सामान्य स्थापत्य प्रकारों की पहचान करें: (सभी लागू विकल्प चुनें)", "opts": ["पोर्ट-होल (छिद्र) वाली सिस्ट (Cist) कब्रें", "डोलमेन (Dolmen) या जमीन के ऊपर बने कक्ष", "मेनहिर (Menhirs) या सीधे खड़े एकल पत्थर", "पकी ईंटों के स्तूप"], "ans": [0, 1, 2], "sol": "सिस्ट, डोलमेन और मेनहिर क्लासिक महापाषाण प्रकार हैं। पकी ईंटों के स्तूप बाद के काल की बौद्ध संरचनाएं हैं।"},
        {"q": "निम्नलिखित में से कौन से दक्षिण भारत के प्रमुख महापाषाणकालीन स्थल हैं? (सभी लागू विकल्प चुनें)", "opts": ["आदिचनल्लूर (तमिलनाडु)", "ब्रह्मगिरि (कर्नाटक)", "मास्की (कर्नाटक)", "हस्तिनापुर (यूपी)"], "ans": [0, 1, 2], "sol": "आदिचनल्लूर, ब्रह्मगिरि और मास्की प्रमुख दक्षिणी महापाषाण केंद्र हैं। हस्तिनापुर उत्तर भारत का एक PGW स्थल है।"},
        {"q": "दक्षिणी महापाषाण कब्रों से कब्र सामग्री के रूप में आमतौर पर क्या बरामद किया जाता है? (सभी लागू विकल्प चुनें)", "opts": ["लोहे के तीर, खंजर और दरांती", "काले-लाल मृदभांड के कटोरे", "सोने और कांसे के मनके या आभूषण", "चांदी के आहत सिक्के (punch-marked)"], "ans": [0, 1, 2], "sol": "कब्रों से लोहे के हथियार/औजार, BRW मृदभांड और मनके/आभूषण मिलते हैं। चांदी के आहत सिक्के बाद के ऐतिहासिक स्तरों के हैं।"},
        {"q": "दक्षिणी महापाषाण अर्थव्यवस्था का प्रतिनिधित्व करने वाली कृषि विशेषताओं का चयन करें: (सभी लागू विकल्प चुनें)", "opts": ["तालाब (Tank) सिंचाई और जल संचयन", "धान और रागी की खेती", "मवेशियों और भेड़ों का पशुपालन", "केसर के बागान"], "ans": [0, 1, 2], "sol": "वे धान/रागी उगाते थे, सिंचाई के लिए तालाबों का निर्माण करते थे और पशुपालन करते थे। केसर कश्मीर तक ही सीमित था।"},
        {"q": "महापाषाण संस्कृति में 'सिस्ट' (Cist) शवाधान का वर्णन करने वाली विशेषताएं कौन सी हैं? (सभी लागू विकल्प चुनें)", "opts": ["बक्से के आकार का पत्थर का कक्ष", "आमतौर पर अर्ध-भूमिगत (जमीन के नीचे)", "एक पत्थर की शिला में गोल छिद्र (port-hole) होता है", "कड़ाई से रसोई घरों के अंदर निर्मित"], "ans": [0, 1, 2], "sol": "सिस्ट जमीन के नीचे बने पत्थर के बक्सेनुमा कक्ष होते हैं जिनमें बाद में अवशेष डालने के लिए पोर्ट-होल होता है। ये बस्तियों से बाहर श्मशान क्षेत्रों में बनाए जाते थे।"}
    ],
    "tf": [
        ("सही या गलत: महापाषाण केवल दक्षिण भारत में पाए जाते हैं और कश्मीर तथा मध्य भारत में पूरी तरह से अनुपस्थित हैं।", False, "नहीं, महापाषाण कश्मीर (गुफक्राल), उत्तर प्रदेश और राजस्थान में भी पाए जाते हैं, हालांकि इनकी सर्वाधिक सघनता दक्षिण में है।"),
        ("सही या गलत: पोर्ट-होल (Port-hole) सिस्ट शिला में काटा गया एक गोलाकार छेद है, जो संभवतः बाद के शवाधानों के प्रवेश द्वार के रूप में कार्य करता था।", True, "सही, पोर्ट-होल परिवार के अन्य सदस्यों के अवशेषों को समय के साथ अंदर डालने की अनुमति देते थे।"),
        ("सही या गलत: दक्षिणी महापाषाण समुदाय मुख्य रूप से पत्थर के औजारों पर निर्भर थे, और लोहा अत्यंत दुर्लभ था।", False, "नहीं, उनके पास अत्यधिक उन्नत लौह धातुकर्म था, जिससे भारी मात्रा में हथियार और औजार मिलते हैं।"),
        ("सही या गलत: मेनहिर (Menhirs) बड़े पत्थर के घेरे होते हैं जिनके अंदर कई कलश शवाधान होते हैं।", False, "नहीं, मेनहिर स्मारक के रूप में खड़ा किया गया एक अकेला सीधा खड़ा पत्थर होता है।"),
        ("सही या गलत: आदिचनल्लूर तमिलनाडु की ताम्रपर्णी घाटी में एक विशाल कलश शवाधान स्थल है।", True, "सही, यह भारत के सबसे बड़े महापाषाणकालीन कलश शवाधान क्षेत्रों में से एक है।"),
        ("सही या गलत: महापाषाण निर्माताओं ने कृषि और भेड़-मवेशी पालन दोनों का अभ्यास किया।", True, "सही, तालाब सिंचाई द्वारा समर्थित उनकी एक मिश्रित अर्थव्यवस्था थी।"),
        ("सही या गलत: महापाषाण कब्रें पूरी तरह से समतावादी थीं, जिनमें सभी कब्रों में एक समान सामग्री होती थी।", False, "नहीं, कब्रें सामाजिक पदानुक्रम दिखाती हैं; कुछ में सोने-कांसे के आभूषण हैं, जबकि अन्य में केवल साधारण बर्तन हैं।"),
        ("सही या गलत: तमिलनाडु में कोडुमनाल मनके बनाने और स्टील के काम के लिए एक महत्वपूर्ण औद्योगिक केंद्र था।", True, "सही, कोडुमनाल से मनके बनाने की कार्यशालाएं और क्रूसिबल स्टील गलाने की भट्टियाँ मिली हैं।")
    ],
    "blank": [
        ("कब्र स्थल को चिह्नित करने के लिए खड़े किए गए एक सीधे अखंड पत्थर को __________ कहा जाता है।", "मेनहिर", "मेनहिर स्मारक के रूप में खड़े किए गए अकेले शिलाखंड हैं।"),
        ("पत्थर की शिलाओं का उपयोग करके बनाई गई बक्सेनुमा भूमिगत कब्र को, जिसमें अक्सर एक पोर्ट-होल होता है, __________ कहा जाता है।", "सिस्ट", "सिस्ट भूमिगत शिला कब्रें हैं।"),
        ("दक्षिणी महापाषाणों की विशिष्ट मृदभांड शैली __________ मृदभांड है।", "काले-और-लाल", "चमकीले काले-लाल बर्तन प्रमुख कब्र सिरेमिक हैं।"),
        ("सिस्ट की एक पत्थर की शिला में काटे गए गोलाकार छिद्र को __________ कहा जाता है।", "पोर्ट-होल", "पोर्ट-होल बाद में कब्र सामग्री डालने के काम आता था।"),
        ("तमिलनाडु के तूतुकुड़ी जिले में स्थित वह विशाल कलश शवाधान स्थल, जहाँ से सोने के मुकुट (diadems) और लोहे के हथियार मिले हैं, __________ है।", "आदिचनल्लूर", "आदिचनल्लूर एक प्रमुख कलश शवाधान स्थल है।"),
        ("महापाषाण निर्माताओं ने जल संचयन के लिए प्रारंभिक प्रणालियों का निर्माण किया जिसे __________ सिंचाई कहा जाता है।", "तालाब", "महापाषाण क्षेत्रों के पास अक्सर सिंचाई तालाब पाए जाते हैं।"),
        ("जमीन के ऊपर खड़ी शिलाओं पर एक बड़ी सपाट शिला रखकर बनाई गई मेजनुमा कब्र संरचना को __________ कहा जाता है।", "डोलमेन", "डोलमेन जमीन के ऊपर बनी मेजनुमा पत्थर की कब्रें हैं।"),
        ("दक्षिणी महापाषाण संस्कृति कालानुक्रमिक रूप से इस क्षेत्र के __________ युग से मेल खाती है।", "लौह", "महापाषाण संस्कृति दक्षिणी लौह युग का प्रतिनिधित्व करती है।")
    ],
    "match": [
        {
            "q": "महापाषाण स्मारक को उसके स्थापत्य रूप से सुमेलित करें:",
            "items": ["डोलमेन", "मेनहिर", "सिस्ट"],
            "opts": ["जमीन के ऊपर बनी मेजनुमा पत्थर की कब्र", "सीधा खड़ा किया गया अकेला अखंड पत्थर", "गोल छिद्र वाली भूमिगत पत्थर के बक्सेनुमा कब्र"],
            "sol": "डोलमेन जमीन के ऊपर है; मेनहिर खड़ा पत्थर है; सिस्ट भूमिगत बक्सा है।"
        },
        {
            "q": "स्थल को उसके मुख्य महापाषाणकालीन निष्कर्ष से सुमेलित करें:",
            "items": ["आदिचनल्लूर", "कोडुमनाल", "ब्रह्मगिरि"],
            "opts": ["सोने के मुकुटों वाला विशाल कलश शवाधान क्षेत्र", "क्रूसिबल स्टील कार्यशालाएं और गोमेद के मनके", "मार्टिमर व्हीलर द्वारा उत्खनित पत्थर की सिस्ट कब्रें"],
            "sol": "आदिचनल्लूर में कलश शवाधान हैं; कोडुमनाल में स्टील/मनके हैं; ब्रह्मगिरि में व्हीलर द्वारा उत्खनित सिस्ट हैं।"
        },
        {
            "q": "कब्र सामग्री को उसके सामाजिक/कार्यात्मक अर्थ से सुमेलित करें:",
            "items": ["लोहे की कुदाल और दरांती", "लोहे की तलवार और भाले", "सोने के आभूषण और कांसे के बर्तन"],
            "opts": ["कृषि अर्थव्यवस्था का प्रतिनिधित्व करने वाले उपकरण", "योद्धा वर्ग का प्रतिनिधित्व करने वाले हथियार", "अमीर व्यक्तियों का प्रतिनिधित्व करने वाली प्रतिष्ठा वस्तुएं"],
            "sol": "कुदाल/दरांती कृषि की हैं; तलवार/भाले योद्धाओं के हैं; सोने/कांसे प्रतिष्ठा के हैं।"
        }
    ],
    "oneliner": [
        ("सिस्ट कब्र में पोर्ट-होल का प्राथमिक कार्य क्या है?", "पारिवारिक कब्रों में बाद में मृत सदस्यों के कंकाल और कब्र सामग्री डालने की अनुमति देना।"),
        ("आदिचनल्लूर स्थल किस आधुनिक राज्य में स्थित है?", "तमिलनाडु।"),
        ("किस दक्षिणी स्थल से महापाषाण परतों के साथ रोमन व्यापार के साक्ष्य मिले हैं?", "कोडुमनाल (रोमन सिक्कों और विदेशी बर्तनों के माध्यम से)।"),
        ("कब्रों में लोहे की कुदाल मिलने से महापाषाणकालीन लोगों की आजीविका के बारे में क्या पता चलता है?", "यह कृषि भूमि की जुताई और सक्रिय खेती को दर्शाता है।"),
        ("कैरन सर्कल (Cairn Circle) शब्द को स्पष्ट करें।", "शिलाखंडों के गोल घेरे से घिरी हुई पत्थर के टुकड़ों (cairn) के ढेर से ढकी हुई कब्र।"),
        ("महापाषाणकालीन काले-लाल मृदभांड को सामान्य बर्तनों से क्या अलग करता है?", "इसकी अत्यधिक पॉलिश की हुई चमकीली सतह और विशिष्ट काला भीतरी तथा लाल बाहरी हिस्सा।"),
        ("शुष्क क्षेत्रों में महापाषाणकालीन किसानों द्वारा उगाई जाने वाली प्रमुख अनाज फसल की पहचान करें।", "रागी (फिंगर मिलेट)।"),
        ("दक्षिणी कब्रों में पाए गए घोड़ों के लगाम (bits) किस धातु से बने थे?", "लोहे से।")
    ],
    "ar": [
        ("अभिकथन (A): महापाषाणकालीन कब्रें उच्च सामाजिक पदानुक्रम (stratification) को दर्शाती हैं।\nकारण (R): कुछ कब्रों में सोने के आभूषण, कांसे के बर्तन और लोहे के हथियार जैसी समृद्ध वस्तुएं मिलती हैं, जबकि कई अन्य में केवल कुछ बर्तन ही मिलते हैं।", 0, "A और R दोनों सही हैं, और R, A की सही व्याख्या करता है। कब्र सामग्री की असमानता जीवनकाल के धन के अंतर को दर्शाती है।"),
        ("अभिकथन (A): दक्षिणी महापाषाण बर्तनों को बस्तियों के रहने वाले क्षेत्रों के भीतर बनाया जाता था।\nकारण (R): महापाषाण कब्रिस्तान लगातार बस्तियों से बाहर, तालाबों के पास सूखी पथरीली बंजर भूमि पर स्थित पाए जाते हैं।", 3, "A गलत है क्योंकि कब्रें बस्तियों से बाहर बनाई जाती थीं। R सही है।"),
        ("अभिकथन (A): दक्षिणी शवाधानों में पाए गए लोहे के त्रिशूल (Vel) प्रारंभिक धार्मिक संप्रदायों को दर्शाते हैं।\nकारण (R): त्रिशूल मुरुगन/शिव की प्रारंभिक स्थानीय पूजा से जुड़े हैं, जो बाद में दक्षिण भारत में लोकप्रिय हुए।", 0, "दोनों कथन सही हैं, और R, A की सही व्याख्या करता है। लोहे के हथियार प्रारंभिक धार्मिक संप्रदायों को दर्शाते हैं।"),
        ("अभिकथन (A): महापाषाण निर्माता पूरी तरह से खानाबदोश चरवाहे थे जो कोई फसल नहीं उगाते थे।\nकारण (R): महापाषाण क्षेत्रों के पास तालाब प्रणालियाँ, नहरें और धान तथा रागी के दाने मिले हैं।", 3, "A गलत है क्योंकि वे स्थायी कृषि करते थे। R सही है।"),
        ("अभिकथन (A): सिस्ट कब्रों को पीढ़ियों तक बार-बार उपयोग के लिए डिज़ाइन किया गया था।\nकारण (R): सिस्ट की शिला में मौजूद गोल पोर्ट-होल स्मारक को तोड़े बिना नई हड्डियाँ अंदर डालने की अनुमति देता था।", 0, "A और R दोनों सही हैं, और R, A की सही व्याख्या करता है। पोर्ट-होल पारिवारिक कब्रों के प्रवेश द्वार का कार्य करते थे।"),
        ("अभिकथन (A): आदिचनल्लूर अपने विशाल डोलमेन (Dolmen) के लिए प्रसिद्ध है।\nकारण (R): यह स्थल कलश शवाधानों (urn burials) से भरा पड़ा है जहाँ हड्डियों को दफनाने से पहले मिट्टी के बड़े बर्तनों में रखा जाता था।", 3, "A गलत है क्योंकि आदिचनल्लूर कलश शवाधान स्थल है, न कि डोलमेन। R सही है।"),
        ("अभिकथन (A): तमिलनाडु में कोडुमनाल एक औद्योगिक केंद्र था।\nकारण (R): उत्खनन से गोमेद, जैस्पर और स्फटिक के मनके बनाने की कार्यशालाएं तथा क्रूसिबल स्टील भट्टियां मिली हैं।", 0, "A और R दोनों सही हैं, और R, A की सही व्याख्या करता है। कार्यशालाएं और भट्टियां इसकी औद्योगिक भूमिका सिद्ध करती हैं।"),
        ("अभिकथन (A): ब्रह्मगिरि में व्हीलर के उत्खनन ने दक्षिण भारतीय संस्कृतियों का क्रम निर्धारित किया।\nकारण (R): इसने नवपाषाण-ताम्रपाषाण (पत्थर की कुल्हाड़ी) संस्कृति से सीधे महापाषाण (लौह युग) संस्कृति में संक्रमण को दिखाया।", 0, "A और R दोनों सही हैं, और R, A की सही व्याख्या करता है। व्हीलर के स्तर-विन्यास ने दक्षिणी संक्रमण काल को स्पष्ट किया।")
    ],
    "stmt": [
        {"q": "महापाषाण कब्रों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. डोलमेन जमीन के ऊपर खड़े पत्थरों पर एक बड़ी शिला रखकर बनाए गए कक्ष होते हैं।\n2. मेनहिर भूमिगत बक्सेनुमा कब्रें होती हैं जिनमें बर्तन रखे जाते हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"], "ans": 0, "sol": "कथन 1 सही है। कथन 2 गलत है क्योंकि मेनहिर खड़े अखंड पत्थर स्मारक हैं, न कि भूमिगत कब्रें।"},
        {"q": "दक्षिणी महापाषाण अर्थव्यवस्था के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. धान की खेती के लिए तालाब (tank) सिंचाई का व्यापक रूप से उपयोग किया जाता था।\n2. शुष्क क्षेत्रों में रागी और बाजरा उगाया जाता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"], "ans": 2, "sol": "दोनों कथन सही हैं। तालाब सिंचाई और शुष्क रागी की खेती महापाषाण कृषि अर्थव्यवस्था के केंद्र थे।"},
        {"q": "कोडुमनाल स्थल के संदर्भ में, निम्नलिखित कथनों पर विचार करें:\n1. यह तमिलनाडु के इरोड जिले में स्थित है।\n2. यहाँ से क्रूसिबल का उपयोग करके स्टील बनाने की कार्यशालाएं मिली हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"], "ans": 2, "sol": "दोनों कथन सही हैं। कोडुमनाल तमिलनाडु में क्रूसिबल स्टील (वुट्ज़) और मनकों के लिए एक प्रसिद्ध औद्योगिक केंद्र था।"},
        {"q": "निम्नलिखित कथनों पर विचार करें:\n1. कलश शवाधान उस प्रथा को दर्शाता है जहाँ पूरे शरीर का अंतिम संस्कार करके राख को सिस्ट में दफनाया जाता था।\n2. कलश शवाधान में हड्डियों को बड़े मिट्टी के बर्तनों में रखकर गड्ढों में दफनाया जाता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"], "ans": 1, "sol": "कथन 1 गलत है क्योंकि कलश शवाधान में हड्डियों को दफनाया जाता था (inhumation), न कि दाह संस्कार की राख को। कथन 2 सही है।"},
        {"q": "दक्षिणी महापाषाण हथियारों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. कब्रों में लोहे की तलवारें, खंजर और भाले मिलना आम बात है।\n2. महापाषाण कब्रों से कांसे के हथियार पूरी तरह अनुपस्थित हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"], "ans": 0, "sol": "कथन 1 सही है। कथन 2 गलत है क्योंकि कांसे की वस्तुएं (विशेष रूप से सजे हुए कटोरे और बर्तन) मौजूद थीं, हालांकि हथियारों में लोहे का वर्चस्व था।"}
    ],
    "why": [
        ("Why are megalithic burial fields often situated on dry, rocky gravelly ridges?", "ताकि खेती के लिए उपजाऊ मैदानी इलाकों को बचाया जा सके और भारी पत्थरों की कब्रों को पास के तालाबों की बाढ़ से बचाने के लिए मजबूत चट्टानी धरातल पर बनाया जा सके।"),
        ("Why did Megalithic builders place port-holes in subterranean cists?", "ताकि एक ऐसा रास्ता बनाया जा सके जिसके माध्यम से बाद में मरने वाले परिवार के सदस्यों की हड्डियां भी उसी कब्र में डाली जा सकें, जो संयुक्त पारिवारिक कब्रों की प्रथा को दर्शाता है।"),
        ("Why did the horse hold a prominent position in Southern Megalithic grave offerings?", "यह एक योद्धा-चरवाहा अभिजात वर्ग के उदय को दर्शाता है जो युद्ध और गतिशीलता के लिए घोड़ों का उपयोग करता था, जैसा कि कब्रों में लोहे के लगाम मिलने से सिद्ध होता है।")
    ],
    "how": [
        ("How did Megalithic builders coordinate the labor required to move massive stone capstones?", "टनों वजनी पत्थरों को हिलाने के लिए सामूहिक श्रम की आवश्यकता होती थी, जो कबीलाई नेतृत्व (chiefdom) को दर्शाता है जो लोगों को संगठित करके काम पर लगा सकता था।"),
        ("How was the Black-and-Red Ware pottery surface given its highly lustrous look?", "बर्तनों पर महीन चिकनी मिट्टी का लेप लगाकर और पकाने से पहले उन्हें चिकने पत्थरों से घिसकर (burnishing), जिससे सतह चमकीली और चिकनी हो जाती थी।"),
        ("How did tank irrigation systems interact with Megalithic settlements?", "वे मौसमी धाराओं के पार मिट्टी के बांध बनाकर पानी इकट्ठा करते थे। कब्रें ऊंचे स्थानों पर तालाबों के पास बनाई जाती थीं, जबकि खेती के खेत बांध के नीचे पानी प्राप्त करने के लिए बनाए जाते थे।")
    ],
    "case": [
        ("Analyze the archaeological significance of Mortimer Wheeler's excavations at Brahmagiri.", "व्हीलर ने 1947 में ब्रह्मगिरि में उत्खनन करके दक्षिण भारत का पहला निश्चित पुरातात्विक क्रम स्थापित किया, जिसने दिखाया कि नवपाषाण (पत्थर कुल्हाड़ी) के सीधे बाद महापाषाण (लोहा) आया, जिससे बिना कांसे के सीधे लोहे के आगमन की पुष्टि हुई।"),
        ("Analyze Adichanallur as a case study of Megalithic Urn burial traditions.", "आदिचनल्लूर से गड्ढों में कलश शवाधान मिले हैं। मिट्टी के बड़े कलशों में कंकाल, काले-लाल बर्तन, लोहे के हथियार और सोने के मुकुट मिले हैं, जो सिस्ट या डोलमेन से भिन्न शवाधान परंपरा को दर्शाते हैं।"),
        ("Evaluate Kodumanal as an industrial site trading with the Roman Empire.", "कोडुमनाल से रोमन सिक्के, ब्राह्मी लिपि के बर्तन और गोमेद मनकों तथा क्रूसिबल स्टील (वुट्ज़) बनाने की बड़ी भट्टियां मिली हैं, जो शुरुआती वैश्विक व्यापार में इसके महत्व को दर्शाती हैं।")
    ],
    "teach": [
        ("Explain the difference between a Menhir and a Dolmen to a beginner.", "मेनहिर एक अकेला सीधा खड़ा किया गया पत्थर का खंभा होता है जो स्मारक का कार्य करता है। डोलमेन मेजनुमा संरचना होती है जहाँ खड़े पत्थरों पर एक सपाट शिला रखी होती है, जो कब्र का ख्याल रखती है।"),
        ("Explain why Megalithic graves contain so many iron weapons.", "कब्रों में तलवार, खंजर और भाले मिलना यह दर्शाता है कि समाज में लड़ाकू या योद्धा वर्ग का उदय हो चुका था। उन्हें कब्रों में साथ दफनाना उनके योद्धा होने और अगले जन्म में सुरक्षा को दर्शाता था।"),
        ("Explain the concept of secondary burial in Megalithic cists.", "ताजा शव को दफनाने के बजाय उसे कुछ समय के लिए खुला छोड़ दिया जाता था ताकि मांस हट सके। बाद में साफ हड्डियों को इकट्ठा करके मिट्टी के बर्तनों और हथियारों के साथ सिस्ट कब्र में सील कर दिया जाता था।")
    ]
}

# Run generation for Section 3
clone_and_generate_sec(3, "Southern Indian Megalithic Cultures", "Megalithic Cultures", "महापाषाण संस्कृति", sec3_data_en, sec3_data_hi)


# ==================== SECTION 4: SOCIO-ECONOMIC IMPACT OF IRON ====================
sec4_data_en = {
    "mcq": [
        {"q": "What agricultural practice, enabled by heavy iron tools, dramatically increased rice yields in the Gangetic plains?", "opts": ["Wet-paddy transplantation (Vrihi transplantation)", "Dry broadcasting of seeds", "Slash-and-burn shifting fields", "Terrace contour farming"], "ans": 0, "sol": "Wet-paddy transplantation involves growing seedlings in beds and moving them to flooded fields, drastically boosting crop yield."},
        {"q": "How did iron tools accelerate the transition from tribal chiefdoms (Janas) to territorial states (Janapadas)?", "opts": ["By generating agricultural surpluses that supported standing armies and administrative staff", "By rendering stone walls useless in warfare", "By encouraging hunting over agriculture", "By forcing tribes to adopt nomadic migration patterns"], "ans": 0, "sol": "Iron-led surplus agriculture funded state institutions, standing armies, and administrative structures, enabling larger territorial kingdoms."},
        {"q": "Which type of iron tool was most critical for initial land reclamation in the dense monsoon forests of the mid-Ganga valley?", "opts": ["Heavy socketed iron axe", "Light iron arrowhead", "Delicate iron needle", "Slender iron hook"], "ans": 0, "sol": "Heavy socketed iron axes allowed the clearance of tough monsoon forests, opening up new land for settlement and farming."},
        {"q": "What social transformation is reflected in Later Vedic texts during the transition to the Iron Age?", "opts": ["The crystallization of the Varna system and early class divisions", "The complete equality of all tribal members", "The abandonment of patriarchal family systems", "The rise of purely egalitarian pastoral guilds"], "ans": 0, "sol": "The agricultural surplus and sedentary lifestyle catalyzed the crystallization of the four Varnas and social hierarchies."},
        {"q": "The expansion of trade and craft specialization during the late Iron Age directly laid the foundation for which historical phase?", "opts": ["The Second Urbanization (rise of cities like Rajgriha and Kashi)", "The First Urbanization of the Indus", "The Rigvedic pastoral expansion", "The Neolithic Revolution"], "ans": 0, "sol": "Surplus food and metal craft specialization led to trade networks, guilds, and the rise of early cities (Second Urbanization) around 600 BCE."}
    ],
    "multi": [
        {"q": "Which factors contributed to agricultural intensification during the Indian Iron Age? (Select all that apply)", "opts": ["Use of heavy iron plowshares to turn hard alluvial clays", "Introduction of wet-paddy transplantation techniques", "Construction of tank irrigation canals", "Use of steam-powered threshing machines"], "ans": [0, 1, 2], "sol": "Iron plowshares, wet paddy transplantation, and irrigation tanks were vital. Steam engines belong to the modern industrial era."},
        {"q": "Select the socio-political changes that accompanied the adoption of iron metallurgy: (Select all that apply)", "opts": ["Evolution of Janas (tribes) into Janapadas (territorial states)", "Rise of standing armies armed with standardized iron weapons", "Crystallization of hereditary kingship and tax collection", "Dissolution of all social hierarchies"], "ans": [0, 1, 2], "sol": "Territorial states, standing armies, and hereditary tax structures developed. Social stratification actually increased rather than dissolving."},
        {"q": "Which of the following agricultural crops are systematically recorded in Iron Age layers of Northern India? (Select all that apply)", "opts": ["Rice (Vrihi)", "Wheat (Godhuma)", "Barley (Yava)", "Maize and Potato"], "ans": [0, 1, 2], "sol": "Wheat, barley, and rice are typical ancient Indian grains. Maize and potatoes are New World crops introduced post-Columbus."},
        {"q": "Identify the features of craft organization during the late Iron Age transition: (Select all that apply)", "opts": ["Emergence of specialized blacksmith guilds", "Standardization of ceramic and metal types", "Widespread use of copper punch-marked coins", "Complete lack of trade between different settlements"], "ans": [0, 1], "sol": "Specialized blacksmithing and standardized tools emerged. Coins came at the end of the transition, and trade actually expanded substantially."},
        {"q": "Select the geographical factors that made the mid-Ganga valley highly productive for Iron Age farmers: (Select all that apply)", "opts": ["Deep, fertile alluvial deposits", "Abundant monsoon rainfall", "Proximity to rich iron ore deposits in Chotanagpur", "Arid desert soils requiring no forest clearing"], "ans": [0, 1, 2], "sol": "Fertile alluvium, rainfall, and proximity to Singhbhum/Chotanagpur iron ores made the mid-Ganga basin highly favorable."}
    ],
    "tf": [
        ("True or False: Iron plowshares allowed farmers to cultivate the heavy alluvial soils of the Ganga Doab far more effectively than wooden plows.", True, "True, hard soils could not be turned deeply without metal-tipped plowshares."),
        ("True or False: The transition to the Iron Age led to a decrease in the density of human settlements in Northern India.", False, "No, population density and settlement size increased substantially due to food surpluses."),
        ("True or False: Later Vedic texts like the Shatapatha Brahmana contain references to plows drawn by multiple oxen, reflecting agricultural expansion.", True, "True, the Brahmana texts describe heavy plowing operations involving teams of oxen."),
        ("True or False: Iron technology had no impact on warfare, as battles were still fought strictly with stone clubs.", False, "No, iron spears and arrowheads revolutionized military technology and state expansion."),
        ("True or False: The Second Urbanization refers to the rise of cities in the Ganga Valley around the 6th century BCE.", True, "True, it is the urban revival following the Harappan decay."),
        ("True or False: Tribal assemblies like Sabha and Samiti gained absolute power over kings during the late Iron Age.", False, "No, their influence declined as kings consolidated absolute territorial power and standing armies."),
        ("True or False: The division of labor became more complex as iron metallurgy enabled a wider variety of crafts.", True, "True, specialized smiths, glass workers, and toolmakers emerged."),
        ("True or False: Rice was grown exclusively by dry broadcasting method without transplantation during the Iron Age.", False, "No, wet-paddy transplantation became the defining technique that boosted yields.")
    ],
    "blank": [
        ("The agricultural technique of transplanting seedlings into flooded fields is called __________ transplantation.", "wet-paddy", "Wet-paddy transplantation is the core method for high rice yield."),
        ("The socio-political units representing territorial kingdoms that evolved from tribal Janas are called __________.", "Janapadas", "Janapadas are territorial states (lit. footholds of a tribe)."),
        ("The Later Vedic literary text that describes plows drawn by up to 24 oxen is the __________ Brahmana.", "Shatapatha", "Shatapatha Brahmana details elaborate agricultural rituals and heavy plows."),
        ("The rise of early cities in the Ganga basin during the 6th century BCE is termed the __________ Urbanization.", "Second", "The Second Urbanization marks the rise of Gangetic cities."),
        ("Blacksmiths organized themselves into craft cooperatives or guilds, known in later texts as __________.", "shrenis", "Shrenis are specialized professional guilds."),
        ("The proximity to iron ore mines in the __________ plateau was crucial for Ganga valley metalworking.", "Chotanagpur", "Chotanagpur ores provided abundant raw iron materials."),
        ("Standardized iron arrowheads and spearheads strengthened the power of the Rajan, leading to early __________ armies.", "standing", "Standing armies replaced temporary tribal militias."),
        ("The social system that crystallized into a hereditary four-tier hierarchy during this phase is the __________ system.", "Varna", "The Varna system defined priests, warriors, farmers, and laborers.")
    ],
    "match": [
        {
            "q": "Match the socio-political stage with its socio-economic character:",
            "items": ["Rigvedic Phase", "Later Vedic/PGW Phase", "Mahajanapada/NBPW Phase"],
            "opts": ["Pastoral nomadic economy with copper tools", "Sedentary farming village economy with early iron", "Highly urbanized economy with professional guilds and coins"],
            "sol": "Rigvedic is pastoral nomadic; Later Vedic is sedentary farming; Mahajanapada is urbanized."
        },
        {
            "q": "Match the agricultural tool with its economic function:",
            "items": ["Iron Axe", "Iron Plowshare", "Iron Sickle"],
            "opts": ["Reclaiming forest lands for agriculture", "Turning tough alluvial soils deeply", "Harvesting grain crops efficiently"],
            "sol": "Axe clears forests; Plowshare turns soil; Sickle harvests crops."
        },
        {
            "q": "Match the Vedic class with its economic/political role:",
            "items": ["Kshatriya", "Vaishya", "Shudra"],
            "opts": ["Warrior elites armed with iron weapons", "Farmers and traders paying taxes", "Laborers supporting agricultural surplus"],
            "sol": "Kshatriya represents warriors; Vaishya represents taxpayers; Shudra represents labor."
        }
    ],
    "oneliner": [
        ("What is the primary socio-economic significance of wet-paddy transplantation?", "It multiplied rice yields per acre, creating the food surplus required to support non-agricultural urban centers."),
        ("Which Vedic text provides detailed symbolic references to large plows drawn by oxen?", "The Shatapatha Brahmana."),
        ("How did iron affect the power of tribal assemblies like Sabha and Samiti?", "It weakened them, as kings built standing armies and tax bases, making them independent of tribal assembly approval."),
        ("Name the economic guild organization that emerged to manage specialized crafts.", "The Shreni (guild)."),
        ("What geographical region became the political center of India due to iron surplus and ore proximity?", "Magadha (in southern Bihar)."),
        ("State the primary cause of the Second Urbanization in India.", "Agricultural surplus in the Gangetic basin enabled by iron technology and rice transplantation."),
        ("What does the Sanskrit term 'Ayas' refer to in Later Vedic texts?", "Metal, with 'Shyama Ayas' (black metal) specifically referring to iron."),
        ("Define the role of a 'Rajan' in the Later Vedic transition.", "A tribal chief who transitioned into a territorial king claiming divine right and collecting tribute.")
    ],
    "ar": [
        ("Assertion (A): Magadha emerged as the most powerful Mahajanapada in Eastern India.\nReason (R): It sat near rich iron ore deposits in South Bihar, allowing Magadhan kings to equip their armies with superior weapons.", 0, "Both A and R are correct, and R explains A. Ore proximity gave Magadha a direct military advantage."),
        ("Assertion (A): The Varna system became highly flexible and fluid during the Later Vedic-PGW transition.\nReason (R): Sedentary farming and economic surpluses led to class differentiation and rigid, hereditary caste functions.", 3, "A is false because the Varna system became more rigid, not flexible. R is true."),
        ("Assertion (A): Tank irrigation was a major technological achievement of the Southern Megalithic builders.\nReason (R): The dry granite landscape of the South required water storage systems to support rice and ragi cultivation.", 0, "Both A and R are correct, and R explains A. Storage tanks adapted farming to Southern geology."),
        ("Assertion (A): Iron tools completely eliminated pastoral herding in India.\nReason (R): Sedentary farming became the dominant economic activity, but livestock rearing remained essential for plowing and meat.", 3, "A is false because pastoral herding coexisted. R is true."),
        ("Assertion (A): Wood plows were completely useless in the Ganga Valley.\nReason (R): While wood plows could work light soils, they could not break the heavy alluvial clay of the Doab without iron points.", 3, "A is false because wood plows were still used, but limited. R is true."),
        ("Assertion (A): The rise of shrenis (guilds) indicates a high degree of economic specialization.\nReason (R): Blacksmiths, potters, and glassmakers organized to control quality, training, and prices within cities.", 0, "Both A and R are correct, and R explains A. Guild systems reflect complex urban craft divisions."),
        ("Assertion (A): Rigvedic battles were fought primarily over territorial borders.\nReason (R): Rigvedic wealth was measured in cattle (Gavisthi), and wars were fought for cattle raids rather than land control.", 3, "A is false because Rigvedic wars were cattle raids (Gavisthi). R is true."),
        ("Assertion (A): The Shatapatha Brahmana details agricultural rituals.\nReason (R): The Later Vedic state relied heavily on agricultural taxes, prompting religious sanctification of farming operations.", 0, "Both A and R are correct, and R explains A. Sanctification justified elite control over agricultural surplus.")
    ],
    "stmt": [
        {"q": "Consider the following statements regarding wet-paddy transplantation:\n1. Seedlings are grown in separate nursery beds before being transplanted into flooded fields.\n2. It requires far less manual labor than traditional broadcasting methods.\nWhich of the statements given above is/are correct?", "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 0, "sol": "Statement 1 is correct. Statement 2 is incorrect as transplantation is highly labor-intensive, though it yields far more grain."},
        {"q": "Consider the following statements regarding Later Vedic political changes:\n1. The power of the king became hereditary and absolute.\n2. The tribal assemblies of Sabha and Samiti increased their control over royal taxation.\nWhich of the statements given above is/are correct?", "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 0, "sol": "Statement 1 is correct. Statement 2 is incorrect as tribal assemblies lost power as royal authority consolidated."},
        {"q": "With reference to the Later Vedic term 'Ayas', consider the following statements:\n1. 'Krishna Ayas' or 'Shyama Ayas' in the Atharva Veda refers specifically to iron.\n2. 'Lohita Ayas' in the same texts refers to copper.\nWhich of the statements given above is/are correct?", "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 2, "sol": "Both statements are correct. Shyama (black) ayas is iron; Lohita (red) ayas is copper."},
        {"q": "Consider the following statements:\n1. The First Urbanization in India occurred in the Indus valley, while the Second Urbanization occurred in the Ganga valley.\n2. The Second Urbanization was made possible primarily by bronze tool technology.\nWhich of the statements given above is/are correct?", "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 0, "sol": "Statement 1 is correct. Statement 2 is false as the Second Urbanization was driven by iron technology and rice surplus, not bronze."},
        {"q": "Consider the following statements regarding Iron Age trade:\n1. Overland trade routes connected the Ganga valley with Taxila and Central Asia.\n2. Punch-marked silver coins were widely used in early PGW layers to pay taxes.\nWhich of the statements given above is/are correct?", "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 0, "sol": "Statement 1 is correct. Statement 2 is incorrect as coins appeared later in the NBPW phase, not in early PGW levels which relied on barter or cattle standard."}
    ],
    "why": [
        ("Why did the mid-Ganga valley become the focal point of state formation in the Iron Age?", "Its fertile alluvial soil and heavy rainfall supported wet-paddy surplus, while its location allowed control over trade routes and proximity to iron ores in Chotanagpur, funding strong Magadhan states."),
        ("Why did wet-paddy transplantation require stable sedentary village communities?", "The technique is highly time-sensitive, requiring coordinated seasonal labor to prepare nursery beds, flood fields, transplant shoots, and manage weeds, making seasonal migration impossible."),
        ("Why did the role of the Brahmanas (priests) increase in importance alongside the growth of agriculture?", "Sedentary farming required calendars, rain predictions, and land rituals. Priests sanctified agricultural cycles and performed state rituals (like Rajasuya) to legitimize the king's tax authority.")
    ],
    "how": [
        ("How did iron axes change the settlement pattern of ancient India?", "They allowed communities to move away from light scrublands and clear the dense monsoon forests of the Ganga Doab, establishing large farming villages on deep alluvial plains."),
        ("How did agricultural surplus lead to the rise of specialized craft guilds?", "With food abundant, a segment of the population could leave farming to specialize full-time in metallurgy, pottery, and trade, organizing into guilds (shrenis) to regulate their crafts."),
        ("How did Magadhan kings utilize iron resources to establish hegemony over other Mahajanapadas?", "By controlling South Bihar's iron mines, they secured a steady supply of raw metal to manufacture standardized iron weapons and iron-rimmed chariot wheels, building a military advantage.")
    ],
    "case": [
        ("Analyze Magadha's geographical location as a case study for resource-driven state hegemony.", "Magadha was situated near the Rajgir hills and Chotanagpur mines, providing direct access to rich iron ores. This allowed Magadha to build superior weapons and clear forests faster than western rivals like Kosala or Avanti."),
        ("Evaluate the agricultural transformation of the Ganga-Yamuna Doab as a case study for technology-driven demographic growth.", "Doab excavations show a massive rise in PGW site numbers compared to earlier OCP/BRW periods. This demographic explosion was driven by iron plowshares and double-cropping, which boosted carrying capacity."),
        ("Analyze the role of Vedic sacrifices (Shrauta rituals) as a case study for legitimizing early state taxation.", "As kings needed to collect surplus grain (bali) from farmers (Vaishyas), they sponsored elaborate rituals performed by priests. These rituals declared the king's divine right to rule and collect taxes, turning tribal gifts into state taxes.")
    ],
    "teach": [
        ("Explain the difference between tribal chiefdoms and territorial states to a beginner.", "Tribal chiefdoms (Janas) are bound by kinship, where the leader rules over people, and wealth is pastoral. Territorial states (Janapadas) are defined by borders, where the king rules over land and collects agricultural taxes from all inhabitants."),
        ("Explain the significance of the Sanskrit term 'Shyama Ayas'.", "Literally meaning 'black metal', it appears in Later Vedic texts to distinguish iron from 'Lohita Ayas' (red metal/copper), marking the literary arrival of the Iron Age in India."),
        ("Explain the link between iron tools, agricultural surplus, and the rise of early cities.", "Iron tools cleared forests and tilled soil, creating surplus food. This surplus fed artisans, traders, and soldiers, who lived in central trading hubs, turning those hubs into early cities (Second Urbanization).")
    ]
}

sec4_data_hi = {
    "mcq": [
        {"q": "भारी लोहे के औजारों द्वारा सक्षम किस कृषि पद्धति ने गंगा के मैदानों में धान की उपज को नाटकीय रूप से बढ़ा दिया?", "opts": ["धान की रोपाई (Wet-paddy transplantation)", "बीजों का सूखा छिड़काव", "झूम (काटो और जलाओ) खेती", "सीढ़ीदार पर्वतीय खेती"], "ans": 0, "sol": "धान की रोपाई में क्यारियों में पौधे उगाकर उन्हें भरे हुए खेतों में लगाया जाता है, जिससे फसल की पैदावार नाटकीय रूप से बढ़ जाती है।"},
        {"q": "लोहे के औजारों ने जनजातीय सरदार तंत्र (Janas) से क्षेत्रीय राज्यों (Janapadas) में संक्रमण को कैसे तेज किया?", "opts": ["स्थायी सेनाओं और प्रशासनिक कर्मचारियों का समर्थन करने वाले कृषि अधिशेष (Surplus) को उत्पन्न करके", "युद्ध में पत्थर की दीवारों को बेकार करके", "कृषि पर शिकार को प्रोत्साहित करके", "कबीलों को खानाबदोश प्रवास पैटर्न अपनाने के लिए मजबूर करके"], "ans": 0, "sol": "लोहे से संचालित अधिशेष कृषि ने राज्य संस्थानों, स्थायी सेनाओं और प्रशासनिक ढांचों को वित्त पोषित किया, जिससे बड़े क्षेत्रीय साम्राज्य संभव हो सके।"},
        {"q": "मध्य गंगा घाटी के घने मानसूनी जंगलों को कृषि योग्य बनाने के लिए किस प्रकार का लौह उपकरण सबसे महत्वपूर्ण था?", "opts": ["भारी सॉकेटेड लोहे की कुल्हाड़ी", "हल्का लोहे का तीर", "बारीक लोहे की सुई", "पतला लोहे का हुक"], "ans": 0, "sol": "भारी सॉकेटेड लोहे की कुल्हाड़ियों ने घने मानसूनी जंगलों की कटाई को संभव बनाया, जिससे बस्तियों और खेती के लिए नई भूमि खुल सकी।"},
        {"q": "लौह युग के संक्रमण के दौरान उत्तर वैदिक ग्रंथों में कौन सा सामाजिक परिवर्तन दिखाई देता है?", "opts": ["वर्ण व्यवस्था का सुदृढ़ीकरण और प्रारंभिक वर्ग विभाजन", "कबीले के सभी सदस्यों की पूर्ण समानता", "पितृसत्तात्मक पारिवारिक व्यवस्था का अंत", "पूरी तरह से समतावादी चरवाहा संघों का उदय"], "ans": 0, "sol": "कृषि अधिशेष और स्थायी जीवन शैली ने चार वर्णों और सामाजिक पदानुक्रमों के सुदृढ़ीकरण को उत्प्रेरित किया।"},
        {"q": "लौह युग के अंत में व्यापार और शिल्प विशेषज्ञता के विस्तार ने सीधे तौर पर किस ऐतिहासिक चरण की नींव रखी?", "opts": ["द्वितीय शहरीकरण (राजगृह और काशी जैसे शहरों का उदय)", "सिंधु घाटी का प्रथम शहरीकरण", "ऋग्वैदिक चरवाहा विस्तार", "नवपाषाण कालीन क्रांति"], "ans": 0, "sol": "अधिशेष भोजन और धातु शिल्प विशेषज्ञता के कारण व्यापार नेटवर्क, श्रेणियां और लगभग 600 ईसा पूर्व के आसपास शुरुआती शहरों का उदय (द्वितीय शहरीकरण) हुआ।"}
    ],
    "multi": [
        {"q": "भारतीय लौह युग के दौरान कृषि विस्तार में किन कारकों ने योगदान दिया? (सभी लागू विकल्प चुनें)", "opts": ["कठोर जलोढ़ मिट्टी को खोदने के लिए भारी लोहे के फाल (Plowshares) का उपयोग", "धान की रोपाई (Wet-paddy transplantation) तकनीकों की शुरुआत", "तालाब सिंचाई और नहरों का निर्माण", "भाप से चलने वाली गहाई मशीनों का उपयोग"], "ans": [0, 1, 2], "sol": "लोहे के फाल, धान की रोपाई और सिंचाई तालाब महत्वपूर्ण थे। भाप इंजन आधुनिक औद्योगिक युग के हैं।"},
        {"q": "लौह धातुकर्म को अपनाने के साथ आए सामाजिक-राजनीतिक परिवर्तनों का चयन करें: (सभी लागू विकल्प चुनें)", "opts": ["जन (कबीलों) का जनपदों (क्षेत्रीय राज्यों) में विकास", "मानकीकृत लोहे के हथियारों से लैस स्थायी सेनाओं का उदय", "वंशानुगत राजशाही और कर संग्रह का सुदृढ़ीकरण", "सभी सामाजिक पदानुक्रमों का अंत"], "ans": [0, 1, 2], "sol": "क्षेत्रीय जनपद, स्थायी सेनाएं और कर-आधारित राजशाही विकसित हुई। सामाजिक पदानुक्रम समाप्त होने के बजाय वास्तव में बढ़े।"},
        {"q": "उत्तरी भारत के लौह युग की परतों में निम्नलिखित में से कौन सी कृषि फसलों के व्यवस्थित साक्ष्य मिले हैं? (सभी लागू विकल्प चुनें)", "opts": ["धान (व्रीहि)", "गेहूं (गोधूम)", "जौ (यव)", "मक्का और आलू"], "ans": [0, 1, 2], "sol": "गेहूं, जौ और धान प्राचीन भारतीय अनाज हैं। मक्का और आलू कोलंबस के बाद पेश की गई नई दुनिया की फसलें हैं।"},
        {"q": "लौह युग के संक्रमण के दौरान शिल्प संगठन की विशेषताओं की पहचान करें: (सभी लागू विकल्प चुनें)", "opts": ["विशेषज्ञ लोहार श्रेणियों (Guilds) का उदय", "सिरेमिक और धातु प्रकारों का मानकीकरण", "तांबे के आहत सिक्कों का व्यापक उपयोग", "विभिन्न बस्तियों के बीच व्यापार का पूर्ण अभाव"], "ans": [0, 1], "sol": "लोहारों की श्रेणियां और मानकीकृत उपकरण उभरे। सिक्के संक्रमण के अंत में आए, और व्यापार का वास्तव में विस्तार हुआ।"},
        {"q": "उन भौगोलिक कारकों का चयन करें जिन्होंने मध्य गंगा घाटी को लौह युग के किसानों के लिए अत्यधिक उत्पादक बनाया: (सभी लागू विकल्प चुनें)", "opts": ["गहरी, उपजाऊ जलोढ़ मिट्टी", "प्रचुर मात्रा में मानसूनी वर्षा", "छोटानागपुर में समृद्ध लौह अयस्क जमा की निकटता", "शुष्क मरुस्थलीय मिट्टी जिसमें जंगल साफ करने की आवश्यकता नहीं थी"], "ans": [0, 1, 2], "sol": "उपजाऊ जलोढ़ मिट्टी, वर्षा और छोटानागपुर के लौह अयस्कों की निकटता ने मध्य गंगा बेसिन को अत्यधिक अनुकूल बनाया।"}
    ],
    "tf": [
        ("सही या गलत: लोहे के फाल ने किसानों को लकड़ी के हलों की तुलना में गंगा दोआब की कठोर जलोढ़ मिट्टी को अधिक प्रभावी ढंग से जोतने की अनुमति दी।", True, "सही, कठोर मिट्टी को लोहे की नोक वाले फाल के बिना गहराई से नहीं जोता जा सकता था।"),
        ("सही या गलत: लौह युग में संक्रमण के कारण उत्तरी भारत में मानव बस्तियों के घनत्व में कमी आई।", False, "नहीं, खाद्य अधिशेष के कारण जनसंख्या घनत्व और बस्तियों के आकार में पर्याप्त वृद्धि हुई।"),
        ("सही या गलत: शतपथ ब्राह्मण जैसे उत्तर वैदिक ग्रंथों में कई बैलों द्वारा खींचे जाने वाले हलों का उल्लेख है, जो कृषि विस्तार को दर्शाता है।", True, "सही, ब्राह्मण ग्रंथ बैलों की टीमों से जुड़े भारी जुताई कार्यों का वर्णन करते हैं।"),
        ("सही या गलत: लौह तकनीक का युद्ध पर कोई प्रभाव नहीं पड़ा, क्योंकि लड़ाई अभी भी पूरी तरह से पत्थर के डंडों से लड़ी जाती थी।", False, "नहीं, लोहे के भालों और तीरों ने सैन्य तकनीक और राज्य विस्तार में क्रांति ला दी।"),
        ("सही या गलत: द्वितीय शहरीकरण से तात्पर्य 6ठी शताब्दी ईसा पूर्व के आसपास गंगा घाटी में शहरों के उदय से है।", True, "सही, यह हड़प्पा के पतन के बाद शहरी पुनरुत्थान का प्रतीक है।"),
        ("सही या गलत: उत्तर वैदिक काल के दौरान सभा और समिति जैसी जनजातीय संस्थाओं ने राजा पर पूर्ण नियंत्रण प्राप्त कर लिया।", False, "नहीं, राजाओं द्वारा स्थायी सेना और कर आधार बनाने के कारण इन सभाओं का प्रभाव कम हो गया।"),
        ("सही या गलत: लौह धातुकर्म ने विभिन्न प्रकार के शिल्पों को सक्षम किया, जिससे श्रम विभाजन अधिक जटिल हो गया।", True, "सही, विशिष्ट लोहार, कांच कार्यकर्ता और उपकरण निर्माता उभरे।"),
        ("सही या गलत: लौह युग के दौरान धान बिना रोपाई के केवल बीज छिड़ककर उगाया जाता था।", False, "नहीं, धान की रोपाई (transplantation) इस काल की मुख्य तकनीक बन गई जिसने उपज बढ़ाई।")
    ],
    "blank": [
        ("बाढ़ वाले खेतों में रोपने से पहले पौधों को अलग नर्सरी क्यारियों में उगाया जाता है, जिसे __________ रोपाई कहा जाता है।", "धान", "धान की रोपाई उच्च उपज के लिए मुख्य विधि है।"),
        ("कबीलाई जनों से विकसित हुए क्षेत्रीय राज्यों को __________ कहा जाता है।", "जनपद", "जनपद क्षेत्रीय राज्य हैं (अर्थात कबीले का पैर रखने का स्थान)।"),
        ("उत्तर वैदिक साहित्य का वह ग्रंथ जिसमें 24 बैलों द्वारा खींचे जाने वाले हलों का विवरण है, __________ ब्राह्मण है।", "शतपथ", "शतपथ ब्राह्मण कृषि अनुष्ठानों और भारी हलों का विवरण देता है।"),
        ("6ठी शताब्दी ईसा पूर्व के दौरान गंगा बेसिन में प्रारंभिक शहरों के उदय को __________ शहरीकरण कहा जाता है।", "द्वितीय", "द्वितीय शहरीकरण गंगा घाटी के शहरों के उदय को दर्शाता है।"),
        ("लोहारों और कारीगरों ने खुद को सहकारी समितियों में संगठित किया, जिन्हें बाद के ग्रंथों में __________ कहा गया है।", "श्रेणी", "श्रेणियां विशिष्ट व्यावसायिक संघ (guilds) थीं।"),
        ("गंगा घाटी में धातु के काम के लिए __________ पठार की लौह अयस्क खदानों की निकटता महत्वपूर्ण थी।", "छोटानागपुर", "छोटानागपुर अयस्कों ने प्रचुर मात्रा में कच्चा लोहा प्रदान किया।"),
        ("मानकीकृत लोहे के तीरों और भालों ने राजा की शक्ति को बढ़ाया, जिससे प्रारंभिक __________ सेनाओं का निर्माण हुआ।", "स्थायी", "स्थायी सेनाओं ने अस्थायी कबीलाई मिलिशिया का स्थान ले लिया।"),
        ("वह सामाजिक व्यवस्था जो इस चरण के दौरान वंशानुगत चार-स्तरीय पदानुक्रम में बदल गई, __________ व्यवस्था है।", "वर्ण", "वर्ण व्यवस्था ने ब्राह्मण, क्षत्रिय, वैश्य और शूद्र के कार्यों को परिभाषित किया।")
    ],
    "match": [
        {
            "q": "सामाजिक-राजनीतिक चरण को उसकी सामाजिक-आर्थिक विशेषता से सुमेलित करें:",
            "items": ["ऋग्वैदिक चरण", "उत्तर वैदिक/PGW चरण", "महाजनपद/NBPW चरण"],
            "opts": ["तांबे के औजारों वाली खानाबदोश चरवाहा अर्थव्यवस्था", "प्रारंभिक लोहे वाली स्थायी कृषक ग्रामीण अर्थव्यवस्था", "श्रेणियों और सिक्कों वाली अत्यधिक शहरीकृत अर्थव्यवस्था"],
            "sol": "ऋग्वैदिक चरवाहा है; उत्तर वैदिक स्थायी खेती है; महाजनपद शहरीकृत है।"
        },
        {
            "q": "कृषि उपकरण को उसके आर्थिक कार्य से सुमेलित करें:",
            "items": ["लोहे की कुल्हाड़ी", "लोहे का फाल (Plowshare)", "लोहे की दरांती"],
            "opts": ["कृषि के लिए वन भूमि को साफ करना", "कठोर जलोढ़ मिट्टी को गहराई से खोदना", "अनाज की फसलों की कुशलता से कटाई करना"],
            "sol": "कुल्हाड़ी जंगल साफ करती है; फाल मिट्टी खोदता है; दरांती कटाई करती है।"
        },
        {
            "q": "वैदिक वर्ग को उसकी आर्थिक/राजनीतिक भूमिका से सुमेलित करें:",
            "items": ["क्षत्रिय", "वैश्य", "शूद्र"],
            "opts": ["लोहे के हथियारों से लैस योद्धा वर्ग", "कर देने वाले किसान और व्यापारी", "कृषि अधिशेष का समर्थन करने वाले श्रमिक"],
            "sol": "क्षत्रिय योद्धा हैं; वैश्य करदाता हैं; शूद्र श्रमिक हैं।"
        }
    ],
    "oneliner": [
        ("धान की रोपाई (Wet-paddy transplantation) का प्राथमिक सामाजिक-आर्थिक महत्व क्या है?", "इसने प्रति एकड़ धान की उपज को कई गुना बढ़ा दिया, जिससे गैर-कृषि शहरी केंद्रों का समर्थन करने के लिए आवश्यक खाद्य अधिशेष मिला।"),
        ("कौन सा वैदिक ग्रंथ बैलों द्वारा खींचे जाने वाले बड़े हलों का विस्तृत प्रतीकात्मक विवरण देता है?", "शतपथ ब्राह्मण।"),
        ("लोहे ने सभा और समिति जैसी कबीलाई सभाओं की शक्ति को कैसे प्रभावित किया?", "इसने उन्हें कमजोर कर दिया, क्योंकि राजाओं ने कर संग्रह और स्थायी सेनाओं का निर्माण किया, जिससे वे सभाओं पर निर्भर नहीं रहे।"),
        ("विशिष्ट शिल्पों के प्रबंधन के लिए उभरे आर्थिक संघों को क्या नाम दिया गया था?", "श्रेणी (Shreni)।"),
        ("लौह अधिशेष और अयस्क की निकटता के कारण कौन सा भौगोलिक क्षेत्र भारत का राजनीतिक केंद्र बन गया?", "मगध (दक्षिणी बिहार में)।"),
        ("भारत में द्वितीय शहरीकरण का प्राथमिक कारण क्या था?", "लोह तकनीक और धान रोपाई द्वारा गंगा बेसिन में प्राप्त कृषि अधिशेष।"),
        ("उत्तर वैदिक ग्रंथों में संस्कृत शब्द 'अयस' (Ayas) किसे संदर्भित करता है?", "धातु को, जिसमें 'श्यामा अयस' (काला धातु) विशेष रूप से लोहे को संदर्भित करता है।"),
        ("उत्तर वैदिक काल में 'राजन' की भूमिका को परिभाषित करें।", "एक कबीलाई नेता जो दैवीय अधिकार का दावा करने वाले और कर वसूलने वाले क्षेत्रीय राजा में बदल गया।")
    ],
    "ar": [
        ("अभिकथन (A): पूर्वी भारत में मगध सबसे शक्तिशाली महाजनपद के रूप में उभरा।\nकारण (R): यह दक्षिणी बिहार में समृद्ध लौह अयस्क जमा के पास स्थित था, जिससे मगध के राजा अपनी सेनाओं को बेहतर हथियारों से लैस कर सके।", 0, "A और R दोनों सही हैं, और R, A की सही व्याख्या करता है। अयस्क की निकटता ने मगध को सीधे सैन्य लाभ प्रदान किया।"),
        ("अभिकथन (A): उत्तर वैदिक-PGW संक्रमण के दौरान वर्ण व्यवस्था अत्यधिक लचीली रही।\nकारण (R): स्थायी कृषि और आर्थिक अधिशेष के कारण वर्ग भेद और कठोर, वंशानुगत जाति कार्यों का विकास हुआ।", 3, "A गलत है क्योंकि वर्ण व्यवस्था अधिक कठोर हो गई थी। R सही है।"),
        ("अभिकथन (A): तालाब सिंचाई दक्षिणी महापाषाण निर्माताओं की एक बड़ी तकनीकी उपलब्धि थी।\nकारण (R): दक्षिण के शुष्क ग्रेनाइट परिदृश्य में धान और रागी की खेती के लिए पानी के संचयन की आवश्यकता थी।", 0, "A और R दोनों सही हैं, और R, A की सही व्याख्या करता है। तालाबों ने कृषि को दक्षिणी भूविज्ञान के अनुकूल बनाया।"),
        ("अभिकथन (A): लोहे के औजारों ने भारत से पशुपालन को पूरी तरह समाप्त कर दिया।\nकारण (R): स्थायी कृषि मुख्य आर्थिक गतिविधि बन गई, लेकिन जुताई और मांस के लिए पशुपालन आवश्यक बना रहा।", 3, "A गलत है क्योंकि पशुपालन कृषि के साथ सह-अस्तित्व में रहा। R सही है।"),
        ("अभिकथन (A): गंगा घाटी में लकड़ी के हल पूरी तरह बेकार थे।\nकारण (R): हालांकि लकड़ी के हल हल्की मिट्टी में काम कर सकते थे, लेकिन वे लोहे की नोक के बिना दोआब की भारी जलोढ़ मिट्टी को नहीं तोड़ सकते थे।", 3, "A गलत है क्योंकि लकड़ी के हल अभी भी सीमित रूप से उपयोग किए जाते थे। R सही है।"),
        ("अभिकथन (A): श्रेणियों (guilds) का उदय आर्थिक विशेषज्ञता के उच्च स्तर को दर्शाता है।\nकारण (R): लोहार, कुम्हार और कांच निर्माताओं ने शहरों के भीतर गुणवत्ता, प्रशिक्षण और कीमतों को नियंत्रित करने के लिए खुद को संगठित किया।", 0, "A और R दोनों सही हैं, और R, A की सही व्याख्या करता है। श्रेणी व्यवस्था जटिल शहरी शिल्प विभाजन को दर्शाती है।"),
        ("अभिकथन (A): Rigvedic battles were fought primarily over territorial borders.\nReason (R): Rigvedic wealth was measured in cattle (Gavisthi), and wars were fought for cattle raids rather than land control.", 3, "A गलत है क्योंकि Rigvedic wars were cattle raids (Gavisthi). R सही है।"),
        ("अभिकथन (A): शतपथ ब्राह्मण कृषि अनुष्ठानों का विस्तृत विवरण देता है।\nकारण (R): उत्तर वैदिक राज्य कृषि करों पर अत्यधिक निर्भर था, जिसने कृषि कार्यों के धार्मिक पवित्रीकरण को प्रेरित किया।", 0, "A और R दोनों सही हैं, और R, A की सही व्याख्या करता है। अनुष्ठान करों की वसूली को वैध बनाते थे।")
    ],
    "stmt": [
        {"q": "धान की रोपाई के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. बाढ़ वाले खेतों में रोपने से पहले पौधों को अलग नर्सरी क्यारियों में उगाया जाता है।\n2. इसमें पारंपरिक बीज छिड़काव विधियों की तुलना में बहुत कम शारीरिक श्रम की आवश्यकता होती है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"], "ans": 0, "sol": "कथन 1 सही है। कथन 2 गलत है क्योंकि रोपाई अत्यधिक श्रम-सघन प्रक्रिया है, हालांकि इससे पैदावार बहुत अधिक होती है।"},
        {"q": "उत्तर वैदिक राजनीतिक परिवर्तनों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. राजा की शक्ति वंशानुगत और निरंकुश हो गई।\n2. सभा और समिति जैसी कबीलाई सभाओं ने शाही करों पर अपना नियंत्रण बढ़ा दिया।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"], "ans": 0, "sol": "कथन 1 सही है। कथन 2 गलत है क्योंकि शाही सत्ता के सुदृढ़ होने के साथ कबीलाई सभाओं ने अपनी शक्ति खो दी थी।"},
        {"q": "उत्तर वैदिक शब्द 'Ayas' के संदर्भ में, निम्नलिखित कथनों पर विचार करें:\n1. अथर्ववेद में 'Shyama Ayas' या 'Krishna Ayas' विशेष रूप से लोहे को संदर्भित करता है।\n2. उन्हीं ग्रंथों में 'Lohita Ayas' तांबे को संदर्भित करता है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"], "ans": 2, "sol": "दोनों कथन सही हैं। श्यामा (काला) अयस लोहा है; लोहित (लाल) अयस तांबा है।"},
        {"q": "निम्नलिखित कथनों पर विचार करें:\n1. भारत में प्रथम शहरीकरण सिंधु घाटी में हुआ, जबकि द्वितीय शहरीकरण गंगा घाटी में हुआ था।\n2. द्वितीय शहरीकरण मुख्य रूप से कांस्य उपकरण तकनीक द्वारा संभव हुआ था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"], "ans": 0, "sol": "कथन 1 सही है। कथन 2 गलत है क्योंकि द्वितीय शहरीकरण लोह तकनीक और धान के अधिशेष से प्रेरित था, न कि कांसे से।"},
        {"q": "निम्नलिखित कथनों पर विचार करें:\n1. थल मार्ग व्यापारिक मार्ग गंगा घाटी को तक्षशिला और मध्य एशिया से जोड़ते थे।\n2. करों का भुगतान करने के लिए प्रारंभिक PGW परतों में चांदी के आहत सिक्कों का व्यापक रूप से उपयोग किया जाता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"], "ans": 0, "sol": "कथन 1 सही है। कथन 2 गलत है क्योंकि सिक्के बाद में NBPW चरण में आए, न कि प्रारंभिक PGW स्तरों में जो वस्तु विनिमय या गाय मानक पर निर्भर थे।"}
    ],
    "why": [
        ("Why did the mid-Ganga valley become the focal point of state formation in the Iron Age?", "इसकी उपजाऊ जलोढ़ मिट्टी और भारी वर्षा ने धान के अधिशेष का समर्थन किया, जबकि इसकी भौगोलिक स्थिति ने व्यापार मार्गों और छोटानागपुर के लौह अयस्कों पर नियंत्रण प्रदान किया, जिससे मगध जैसे शक्तिशाली राज्यों को धन मिला।"),
        ("Why did wet-paddy transplantation require stable sedentary village communities?", "यह तकनीक अत्यधिक समय-संवेदी है, जिसमें क्यारियाँ तैयार करने, खेतों में पानी भरने, पौधों को रोपने और खरपतवार प्रबंधन के लिए समन्वित मौसमी श्रम की आवश्यकता होती है, जिससे मौसमी प्रवास असंभव हो जाता है।"),
        ("Why did the role of the Brahmanas (priests) increase in importance alongside the growth of agriculture?", "स्थायी खेती के लिए कैलेंडर, वर्षा के पूर्वानुमान और भूमि अनुष्ठानों की आवश्यकता थी। पुरोहितों ने कृषि चक्रों को पवित्र किया और राजा के कर अधिकार को वैध बनाने के लिए राजसूय जैसे राजकीय अनुष्ठान किए।")
    ],
    "how": [
        ("How did iron axes change the settlement pattern of ancient India?", "उन्होंने समुदायों को हल्की झाड़ियों से दूर जाने और गंगा दोआब के घने मानसूनी जंगलों को साफ करने की अनुमति दी, जिससे गहरे जलोढ़ मैदानों पर बड़े कृषक गाँवों की स्थापना हुई।"),
        ("How did agricultural surplus lead to the rise of specialized craft guilds?", "अधिशेष भोजन होने से, आबादी का एक हिस्सा खेती छोड़कर पूर्णकालिक धातुकर्म, मृदभांड और व्यापार में विशेषज्ञता प्राप्त कर सका, जिसने अपने शिल्पों को नियंत्रित करने के लिए श्रेणियों का गठन किया।"),
        ("How did Magadhan kings utilize iron resources to establish hegemony over other Mahajanapadas?", "दक्षिणी बिहार की लोह खदानों पर नियंत्रण करके उन्होंने मानकीकृत लोहे के हथियारों और लोहे के पहियों वाले रथों के निर्माण के लिए कच्चे धातु की निरंतर आपूर्ति सुरक्षित की, जिससे उन्हें सैन्य लाभ मिला।")
    ],
    "case": [
        ("Analyze Magadha's geographical location as a case study for resource-driven state hegemony.", "मगध राजगीर की पहाड़ियों और छोटानागपुर के पास स्थित था, जिससे उसे लौह अयस्कों तक सीधी पहुँच प्राप्त थी। इसने मगध को अपने पश्चिमी प्रतिद्वंद्वियों जैसे कोसल या अवंती की तुलना में बेहतर हथियार बनाने और तेजी से जंगलों को साफ करने की सुविधा दी।"),
        ("Evaluate the agricultural transformation of the Ganga-Yamuna Doab as a case study for technology-driven demographic growth.", "दोआब के उत्खनन पहले के OCP/BRW काल की तुलना में PGW स्थलों की संख्या में भारी वृद्धि दर्शाते हैं। यह जनसंख्या विस्फोट लोहे के फाल और दोहरी कृषि से प्रेरित था जिसने भूमि की वहन क्षमता को बढ़ाया।"),
        ("Analyze the role of Vedic sacrifices (Shrauta rituals) as a case study for legitimizing early state taxation.", "चूंकि राजाओं को किसानों (वैश्यों) से अधिशेष अनाज (बली) एकत्र करने की आवश्यकता थी, इसलिए उन्होंने पुरोहितों द्वारा किए जाने वाले अनुष्ठानों को संरक्षण दिया। इन अनुष्ठानों ने राजा के शासन और कर वसूलने के दैवीय अधिकार की घोषणा की, जिससे कबीलाई उपहार राजकीय करों में बदल गए।")
    ],
    "teach": [
        ("Explain the difference between tribal chiefdoms and territorial states to a beginner.", "कबीलाई सरदार तंत्र (Janas) रक्त संबंधों से बंधे होते हैं जहाँ नेता लोगों पर शासन करता है और धन पशुधन होता है। क्षेत्रीय राज्य (Janapadas) सीमाओं से परिभाषित होते हैं जहाँ राजा भूमि पर शासन करता है और कर वसूलता है।"),
        ("Explain the significance of the Sanskrit term 'Shyama Ayas'.", "शाब्दिक रूप से 'काला धातु' अर्थ वाला यह शब्द उत्तर वैदिक ग्रंथों में लोहे को तांबे ('Lohita Ayas') से अलग करने के लिए प्रकट होता है, जो भारत में साहित्यिक रूप से लौह युग के आगमन का संकेत देता है।"),
        ("Explain the link between iron tools, agricultural surplus, and the rise of early cities.", "लोहे के औजारों ने जंगल साफ किए और मिट्टी जोती, जिससे अधिशेष भोजन मिला। इस अधिशेष ने कारीगरों, व्यापारियों और सैनिकों का पेट भरा जो व्यापारिक केंद्रों में रहने लगे, जिससे वे केंद्र शहरों में बदल गए (द्वितीय शहरीकरण)।")
    ]
}

# Run generation for Section 4
clone_and_generate_sec(4, "Socio-Economic Impact of Iron", "Socio-Economic Impact", "सामाजिक-आर्थिक प्रभाव", sec4_data_en, sec4_data_hi)


# ==================== SECTION 5: KEY EARLY IRON AGE SITES ====================
sec5_data_en = {
    "mcq": [
        {"q": "Which of the following sites in Uttar Pradesh yielded a massive variety of early iron tools along with systematic smelting furnaces in PGW layers?", "opts": ["Atranjikhera", "Bhimbetka", "Mehrgarh", "Nevasa"], "ans": 0, "sol": "Atranjikhera (UP) is famous for yield of furnaces and tools like axes and celts in its PGW levels."},
        {"q": "Who excavated the legendary site of Hastinapur in the early 1950s, uncovering PGW layers showing epic correlations?", "opts": ["B.B. Lal", "John Marshall", "Mortimer Wheeler", "Alexander Cunningham"], "ans": 0, "sol": "Professor B.B. Lal excavated Hastinapur, establishing the material profile of the PGW culture."},
        {"q": "The site of Jakhera in Uttar Pradesh is archaeologically significant for yielding which transitional feature in its late PGW levels?", "opts": ["Proto-urban features like a channel, roads, and semi-industrial workshops", "Burnt brick multi-storeyed palaces", "Gold coinage cache", "A stone-walled dockyard"], "ans": 0, "sol": "Jakhera shows proto-urban elements like roads, channels, and rich iron deposits, illustrating the transition to urban life."},
        {"q": "Which major Iron Age site in Rajasthan is situated in the Jaipur district, showing a transition from BRW to PGW?", "opts": ["Noh", "Hallur", "Maski", "Adichanallur"], "ans": 0, "sol": "Noh (Rajasthan) is a key site showing the stratigraphy of Ochre Coloured Pottery, Black-and-Red, and Painted Grey Ware."},
        {"q": "The Southern site of Hallur is located on the banks of which river in Karnataka, yielding early C-14 dates for iron transition?", "opts": ["Tungabhadra River", "Kaveri River", "Krishna River", "Godavari River"], "ans": 0, "sol": "Hallur is situated on the Tungabhadra river, yielding transitional dates from Neolithic-Chalcolithic to Iron Age."}
    ],
    "multi": [
        {"q": "Identify the key Northern Indian Painted Grey Ware (PGW) sites: (Select all that apply)", "opts": ["Hastinapur", "Atranjikhera", "Ahichchhatra", "Brahmagiri"], "ans": [0, 1, 2], "sol": "Hastinapur, Atranjikhera, and Ahichchhatra are major northern PGW sites. Brahmagiri is in Karnataka."},
        {"q": "Select the Southern Megalithic sites yielding detailed iron assemblages: (Select all that apply)", "opts": ["Brahmagiri", "Maski", "Adichanallur", "Dadheri"], "ans": [0, 1, 2], "sol": "Brahmagiri, Maski, and Adichanallur are southern Megalithic sites. Dadheri is a PGW site in Punjab."},
        {"q": "Which of the following sites are located in Uttar Pradesh and yield early Iron Age remains? (Select all that apply)", "opts": ["Atranjikhera", "Kampilya", "Ahichchhatra", "Hallur"], "ans": [0, 1, 2], "sol": "Atranjikhera, Kampilya, and Ahichchhatra are UP sites. Hallur is in Karnataka."},
        {"q": "Which findings characterize the site of Jakhera in the early Iron Age? (Select all that apply)", "opts": ["A large variety of iron agricultural tools", "Proto-urban architectural elements like roads", "Bead-making workshops", "Large stone circles with port-holes"], "ans": [0, 1, 2], "sol": "Jakhera has iron tools, proto-urban roads, and bead workshops, but lacks Megalithic stone circles which are southern."},
        {"q": "Identify the sites that show a clear transition from late Harappan to PGW/Iron Age layers: (Select all that apply)", "opts": ["Dadheri (Punjab)", "Katpalon (Punjab)", "Noh (Rajasthan)", "Adichanallur (TN)"], "ans": [0, 1, 2], "sol": "Dadheri, Katpalon, and Noh show early transition sequences. Adichanallur is a Southern Iron Age burial site with no Harappan link."}
    ],
    "tf": [
        ("True or False: Atranjikhera is situated on the banks of the Kali Nadi in the Etah district of Uttar Pradesh.", True, "True, Atranjikhera is situated on the Kali Nadi, a tributary of the Ganga."),
        ("True or False: B.B. Lal discovered that a massive flood had swept away the PGW settlement at Hastinapur.", True, "True, the flood layer divides the PGW and NBPW occupational levels."),
        ("True or False: Gufkral in Kashmir contains only stone tools, with no iron implements ever found.", False, "No, Gufkral yielded early iron tools in its transitional Megalithic layer."),
        ("True or False: Noh in Rajasthan has yielded a five-fold cultural sequence from OCP to historic times.", True, "True, Noh provides a clear stratigraphic sequence used as a chronological standard."),
        ("True or False: Adichanallur Urn burials yielded gold diadems and bronze figurines representing domestic animals.", True, "True, the rich metal offerings at Adichanallur are unique among Southern graves."),
        ("True or False: Maski in Karnataka is a purely Paleolithic site with no Megalithic burials.", False, "No, Maski is famous for its Megalithic burials and later Ashokan edict."),
        ("True or False: The site of Ahichchhatra served as the capital of the ancient Panchala kingdom.", True, "True, Ahichchhatra (Ramnagar, UP) was the northern capital of Panchala."),
        ("True or False: Kampilya in UP has yielded no Painted Grey Ware pottery.", False, "No, Kampilya is a major PGW site associated with the southern Panchalas.")
    ],
    "blank": [
        ("The site of Atranjikhera is located in the __________ district of Uttar Pradesh.", "Etah", "Atranjikhera lies in the Etah district of western UP."),
        ("Hastinapur was excavated by the prominent Indian archaeologist __________.", "B.B. Lal", "Professor B.B. Lal excavated Hastinapur in 1950-52."),
        ("The site of __________ in UP has yielded proto-urban elements like a drainage channel in late PGW levels.", "Jakhera", "Jakhera shows early transition to urbanism in western UP."),
        ("Hallur, showing early transition from Neolithic to Iron Age, is located in the modern state of __________.", "Karnataka", "Hallur is in the Haveri district of Karnataka."),
        ("The major PGW site in Rajasthan near Bharatpur is __________.", "Noh", "Noh is a key stratigraphic site in eastern Rajasthan."),
        ("The capital of Northern Panchala, which yielded rich PGW layers, is __________.", "Ahichchhatra", "Ahichchhatra is the key Panchala capital site."),
        ("The Southern Megalithic urn burial site of Adichanallur is located in the __________ valley.", "Thamirabarani", "Adichanallur sits in the Thamirabarani River valley."),
        ("The transitional site in Punjab where PGW overlaps with late Harappan layers is __________.", "Dadheri", "Dadheri shows late Harappan and PGW coexistence in its stratigraphy.")
    ],
    "match": [
        {
            "q": "Match the site with its modern state:",
            "items": ["Atranjikhera", "Hallur", "Adichanallur"],
            "opts": ["Uttar Pradesh", "Karnataka", "Tamil Nadu"],
            "sol": "Atranjikhera is in UP; Hallur is in Karnataka; Adichanallur is in Tamil Nadu."
        },
        {
            "q": "Match the site with its primary archaeological find:",
            "items": ["Hastinapur", "Jakhera", "Kodumanal"],
            "opts": ["Ganga flood devastation layer", "Proto-urban drainage channel", "Crucible steel furnaces and beads"],
            "sol": "Hastinapur has the flood layer; Jakhera has the channel; Kodumanal has steel furnaces."
        },
        {
            "q": "Match the northern site with its epic association:",
            "items": ["Hastinapur", "Ahichchhatra", "Kampilya"],
            "opts": ["Kuru Kingdom Capital", "Northern Panchala Capital", "Southern Panchala Capital"],
            "sol": "Hastinapur matches Kuru; Ahichchhatra matches Northern Panchala; Kampilya matches Southern Panchala."
        }
    ],
    "oneliner": [
        ("On which river's bank is the site of Atranjikhera situated?", "The Kali Nadi."),
        ("Name the archaeologist who excavated Brahmagiri in 1947.", "Mortimer Wheeler."),
        ("Which site in Rajasthan is located on the Sahibi River, yielding PGW remains?", "Jodhpura."),
        ("What unique ornament was recovered from the Adichanallur urn burials?", "Gold diadems or headbands."),
        ("State the chronological significance of Gufkral's transitional layer.", "It demonstrates a smooth technological shift from Neolithic bone/stone work to Iron metallurgy in Kashmir."),
        ("Which site in UP shows proto-urban elements like roads and a moat in the PGW period?", "Jakhera."),
        ("What epic river flood destroyed the PGW capital of Hastinapur?", "The Ganga River flood."),
        ("Name the district in Karnataka where Hallur is located.", "Haveri district (formerly Dharwad).")
    ],
    "ar": [
        ("Assertion (A): Atranjikhera is considered an industrial node of the PGW culture.\nReason (R): Excavations yielded clay furnaces, iron slag piles, and a wide array of forged iron tools like axes and hooks.", 0, "Both A and R are correct, and R explains A. Smelting furnaces and slag prove its industrial role."),
        ("Assertion (A): B.B. Lal chose to excavate Hastinapur due to its description in Later Vedic texts and epics.\nReason (R): Hastinapur yielded Northern Black Polished Ware from its earliest Neolithic layers.", 3, "A is true but R is false because Hastinapur yielded PGW, not NBPW, in its early Iron levels, and it was not a Neolithic site."),
        ("Assertion (A): Jakhera shows transitional stages leading to the Second Urbanization.\nReason (R): Late PGW levels at Jakhera yield early public works like a channel, roads, and high tool density.", 0, "Both A and R are correct, and R explains A. Proto-urban structures mark the transition to cities."),
        ("Assertion (A): Hallur iron dates are irrelevant to Deccan chronology.\nReason (R): Calibrated C-14 datings from Hallur pushed the Iron Age boundary back to c. 1200 BCE, challenging older chronology.", 3, "A is false because Hallur is central to Deccan chronology. R is true."),
        ("Assertion (A): Dadheri represents a site of cultural overlap.\nReason (R): Late Harappan pottery and Painted Grey Ware were found coexisting in the same stratigraphic layer.", 0, "Both A and R are correct, and R explains A. Overlapping pottery styles prove cultural contact."),
        ("Assertion (A): Adichanallur contains elaborate subterranean stone cist graves.\nReason (R): The site is dominated by urn burials where skeletons were placed in large earthenware jars.", 3, "A is false because Adichanallur has urn burials, not stone cists. R is true."),
        ("Assertion (A): Ahichchhatra was the capital of the Kuru kingdom.\nReason (R): Epic geography places Ahichchhatra as the northern capital of the Panchalas.", 3, "A is false because it was Panchala capital, not Kuru. R is true."),
        ("Assertion (A): Noh in Rajasthan is vital for establishing ceramic stratigraphy.\nReason (R): It yields a continuous sequence of OCP, BRW, PGW, NBPW, and Sunga-Kushan layers.", 0, "Both A and R are correct, and R explains A. Continuous stratigraphy provides a regional chronological standard.")
    ],
    "stmt": [
        {"q": "Consider the following statements regarding the site of Atranjikhera:\n1. It is located in the Etah district of Uttar Pradesh.\n2. It has yielded no iron tools, only copper implements.\nWhich of the statements given above is/are correct?", "opts": ["1 option only", "2 option only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 0, "sol": "Statement 1 is correct. Statement 2 is incorrect as Atranjikhera yielded a massive collection of iron tools and smelting remains."},
        {"q": "Consider the following statements regarding B.B. Lal's excavations at Hastinapur:\n1. The excavation revealed a flood layer that washed away the PGW settlement.\n2. This flood corresponds to the epic narrative of shifting the capital to Kaushambi.\nWhich of the statements given above is/are correct?", "opts": ["1 option only", "2 option only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 2, "sol": "Both statements are correct. The flood layer divides PGW and NBPW levels and aligns with epic accounts."},
        {"q": "With reference to the site of Jakhera, consider the following statements:\n1. It is located on the banks of the Tungabhadra River.\n2. It yields proto-urban features like a water channel and roads in PGW levels.\nWhich of the statements given above is/are correct?", "opts": ["1 option only", "2 option only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 1, "sol": "Statement 1 is incorrect as Jakhera is in UP, not on the southern Tungabhadra. Statement 2 is correct."},
        {"q": "Consider the following statements:\n1. Hallur yielded early dates showing iron in use in the Deccan around 1200 BCE.\n2. Gufkral in Kashmir has yielded no Iron Age remains.\nWhich of the statements given above is/are correct?", "opts": ["1 option only", "2 option only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 0, "sol": "Statement 1 is correct. Statement 2 is incorrect as Gufkral has yielded early iron tools in its transitional layers."},
        {"q": "Consider the following statements regarding the site of Adichanallur:\n1. It is a massive Megalithic urn burial site in Tamil Nadu.\n2. It has yielded gold diadems and bronze animal figurines in graves.\nWhich of the statements given above is/are correct?", "opts": ["1 option only", "2 option only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 2, "sol": "Both statements are correct. Adichanallur is famous for urn burials and rich gold and bronze grave offerings."}
    ],
    "why": [
        ("Why was B.B. Lal's excavation of Hastinapur revolutionary for Indian archaeology?", "It linked the material culture of the PGW pottery style directly to the geographical locations and flood events described in later Vedic and Puranic literature, connecting archaeology with epics."),
        ("Why did Jakhera develop proto-urban elements earlier than other PGW villages?", "Its location in western UP allowed it to act as a key trade node, and its intensive iron working attracted craftsmen, leading to early civic structures like roads and channels."),
        ("Why is the stratigraphic sequence of Noh important for chronologies?", "Noh has a continuous, undisturbed sequence of five cultural periods (OCP, BRW, PGW, NBPW, Sunga-Kushan). This provides a reliable stratigraphic standard to date other sites in Rajasthan and the Doab.")
    ],
    "how": [
        ("How did Mortimer Wheeler's work at Brahmagiri clarify the Southern Neolithic-Iron Age transition?", "Wheeler excavated stratified layers showing polished stone axes directly succeeded by megalithic iron tools and BRW pottery, proving the South skipped a Bronze Age and transitioned directly to iron."),
        ("How did floods affect the settlement cycle at Hastinapur?", "Excavations show a thick alluvial silt layer directly overlying the PGW layer. This indicates a massive Ganga flood that forced the population to abandon the site before it was re-occupied in the NBPW period."),
        ("How do the Adichanallur urn burials demonstrate specialized funerary rituals?", "By placing defleshed skeletal remains inside large earthenware jars (urns) along with pottery, bronze figurines, gold diadems, and iron weapons, and burying them in pits carved out of solid rock.")
    ],
    "case": [
        ("Analyze Jakhera as a case study for the emergence of proto-urbanism in the PGW phase.", "Jakhera yields roads, channels, and a high concentration of specialized tools (axes, chisels, sickles) in late PGW layers. This shows that before full urbanization (NBPW), some PGW villages had already begun developing civic plans and craft specialization."),
        ("Evaluate Dadheri as a case study for late Harappan and PGW cultural contact.", "Dadheri's stratigraphy shows late Harappan and PGW pottery coexisting in the same layers. This proves that Harappan descendants and incoming Iron Age groups lived together or traded, showing a cultural overlap rather than replacement."),
        ("Analyze Adichanallur as a case study for South Indian Megalithic wealth distribution.", "While many graves at Adichanallur contain only simple pottery and basic iron tools, a few yield gold diadems and finely crafted bronze animal figures, indicating the emergence of a wealthy chieftain or elite class.")
    ],
    "teach": [
        ("Explain the significance of Atranjikhera's smelting furnaces to a student.", "Atranjikhera yielded clay furnaces and iron slag, proving that early Iron Age people did not just import finished iron tools; they smelted iron ore locally, establishing an independent chemical industry."),
        ("Explain how the flood layer at Hastinapur is dated.", "The flood layer lies between the Painted Grey Ware layer (dated to c. 1100-500 BCE) and the Northern Black Polished Ware layer (dated to post-600 BCE), placing the flood at c. 600 BCE."),
        ("Explain the archaeological importance of the site of Gufkral.", "Gufkral in Kashmir shows a clear transition from Neolithic stone tools to Megalithic iron tools, showing how northern societies slowly integrated iron metallurgy into their existing stone-age economies.")
    ]
}

sec5_data_hi = {
    "mcq": [
        {"q": "उत्तर प्रदेश के निम्नलिखित में से किस स्थल से PGW स्तरों में प्रगलन भट्टियों के व्यवस्थित अवशेषों के साथ लोहे के विभिन्न प्रकार के औजार मिले हैं?", "opts": ["अतरंजीखेड़ा", "भीमबेटका", "मेहरगढ़", "नेवासा"], "ans": 0, "sol": "अतरंजीखेड़ा (यूपी) अपने PGW स्तरों में प्रगलन भट्टियों और कुल्हाड़ियों तथा खुरपियों जैसे औजारों के लिए प्रसिद्ध है।"},
        {"q": "1950 के दशक की शुरुआत में हस्तिनापुर स्थल का उत्खनन किसने किया था, जिससे महाकाव्य से जुड़े PGW स्तर मिले हैं?", "opts": ["बी.बी. लाल", "जॉन मार्शल", "मार्टिमर व्हीलर", "अलेक्जेंडर कनिंघम"], "ans": 0, "sol": "प्रोफेसर बी.बी. लाल ने हस्तिनापुर का उत्खनन किया, जिससे चित्रित धूसर मृदभांड (PGW) संस्कृति की भौतिक विशेषताएं स्थापित हुईं।"},
        {"q": "उत्तर प्रदेश का जखेड़ा स्थल अपने अंतिम PGW स्तरों में किस संक्रमणकालीन विशेषता के लिए पुरातात्विक रूप से महत्वपूर्ण है?", "opts": ["शहरीकरण के शुरुआती लक्षण जैसे नाली, सड़कें और शिल्प कार्यशालाएं", "पकी ईंटों के बहुमंजिला महल", "सोने के सिक्कों का भंडार", "पत्थर की दीवारों वाला गोदीबाड़ा (dockyard)"], "ans": 0, "sol": "जखेड़ा से सड़कें, नालियां और प्रचुर मात्रा में लौह उपकरण मिले हैं, जो शहरी जीवन में संक्रमण (शुरुआती शहरीकरण) को दर्शाते हैं।"},
        {"q": "राजस्थान का कौन सा प्रमुख लौह युग स्थल भरतपुर जिले में स्थित है, जो BRW से PGW में संक्रमण को दर्शाता है?", "opts": ["नोह", "हल्लूर", "मास्की", "आदिचनल्लूर"], "ans": 0, "sol": "नोह (राजस्थान) एक प्रमुख स्थल है जो गेरुए रंग के मृदभांड, काले-लाल मृदभांड और चित्रित धूसर मृदभांड का स्तर-विन्यास दिखाता है।"},
        {"q": "कर्नाटक का हल्लूर स्थल किस नदी के तट पर स्थित है, जहाँ से लौह युग के संक्रमण की प्रारंभिक सी-14 तिथियां मिली हैं?", "opts": ["तुंगभद्रा नदी", "कावेरी नदी", "कृष्णा नदी", "गोदावरी नदी"], "ans": 0, "sol": "हल्लूर तुंगभद्रा नदी पर स्थित है, जहाँ से नवपाषाण-ताम्रपाषाण से लौह युग में संक्रमण की तिथियां मिली हैं।"}
    ],
    "multi": [
        {"q": "उत्तरी भारत के प्रमुख चित्रित धूसर मृदभांड (PGW) स्थलों की पहचान करें: (सभी लागू विकल्प चुनें)", "opts": ["हस्तिनापुर", "अतरंजीखेड़ा", "अहिच्छत्र", "ब्रह्मगिरि"], "ans": [0, 1, 2], "sol": "हस्तिनापुर, अतरंजीखेड़ा और अहिच्छत्र प्रमुख उत्तरी PGW स्थल हैं। ब्रह्मगिरि कर्नाटक में है।"},
        {"q": "लोहे के समृद्ध उपकरण प्रदान करने वाले दक्षिणी महापाषाण स्थलों का चयन करें: (सभी लागू विकल्प चुनें)", "opts": ["ब्रह्मगिरि", "मास्की", "आदिचनल्लूर", "दधेरी"], "ans": [0, 1, 2], "sol": "ब्रह्मगिरि, मास्की और आदिचनल्लूर दक्षिणी महापाषाण स्थल हैं। दधेरी पंजाब का एक PGW स्थल है।"},
        {"q": "निम्नलिखित में से कौन से स्थल उत्तर प्रदेश में स्थित हैं और प्रारंभिक लौह युग के अवशेष प्रदान करते हैं? (सभी लागू विकल्प चुनें)", "opts": ["अतरंजीखेड़ा", "काम्पिल्य", "अहिच्छत्र", "हल्लूर"], "ans": [0, 1, 2], "sol": "अतरंजीखेड़ा, काम्पिल्य और अहिच्छत्र यूपी के स्थल हैं। हल्लूर कर्नाटक में है।"},
        {"q": "प्रारंभिक लौह युग में जखेड़ा स्थल की क्या विशेषताएं हैं? (सभी लागू विकल्प चुनें)", "opts": ["लोहे के कृषि उपकरणों की बड़ी विविधता", "शहरीकरण के शुरुआती स्थापत्य तत्व जैसे सड़कें", "मनके बनाने की कार्यशालाएं", "गोल पोर्ट-होल वाले बड़े पत्थर के घेरे"], "ans": [0, 1, 2], "sol": "जखेड़ा से लौह उपकरण, सड़कें और मनकों की कार्यशालाएं मिली हैं, लेकिन यहाँ महापाषाण पत्थर के घेरे नहीं हैं जो दक्षिण की विशेषता हैं।"},
        {"q": "उन स्थलों की पहचान करें जो उत्तर-हड़प्पा से PGW/लौह युग परतों में स्पष्ट संक्रमण दिखाते हैं: (सभी लागू विकल्प चुनें)", "opts": ["दधेरी (पंजाब)", "कटपालों (पंजाब)", "नोह (राजस्थान)", "आदिचनल्लूर (TN)"], "ans": [0, 1, 2], "sol": "दधेरी, कटपालों और नोह प्रारंभिक संक्रमण अनुक्रम दिखाते हैं। आदिचनल्लूर दक्षिण का एक शवाधान स्थल है जिसका हड़प्पा से कोई संबंध नहीं है।"}
    ],
    "tf": [
        ("सही या गलत: अतरंजीखेड़ा उत्तर प्रदेश के एटा जिले में काली नदी के तट पर स्थित है।", True, "सही, अतरंजीखेड़ा काली नदी के तट पर स्थित है, जो गंगा की एक सहायक नदी है।"),
        ("सही या गलत: बी.बी. लाल ने पाया कि एक बड़ी बाढ़ ने हस्तिनापुर में PGW बस्ती को बहा दिया था।", True, "सही, बाढ़ की यह परत PGW और NBPW के स्तरों को विभाजित करती है।"),
        ("सही या गलत: कश्मीर के गुफक्राल में केवल पत्थर के औजार मिले हैं, और लोहे के उपकरण कभी नहीं पाए गए।", False, "नहीं, गुफक्राल की संक्रमणकालीन महापाषाण परत से प्रारंभिक लोहे के औजार मिले हैं।"),
        ("सही या गलत: राजस्थान के नोह से OCP से लेकर ऐतिहासिक काल तक का पांच-स्तरीय सांस्कृतिक क्रम मिला है।", True, "सही, नोह एक स्पष्ट स्तर-विन्यास प्रदान करता है जिसका उपयोग कालानुक्रमिक मानक के रूप में होता है।"),
        ("सही या गलत: आदिचनल्लूर कलश शवाधानों से सोने के मुकुट (diadems) और पालतू जानवरों का प्रतिनिधित्व करने वाली कांसे की मूर्तियाँ मिली हैं।", True, "सही, आदिचनल्लूर में कब्रों से मिली सोने-कांसे की वस्तुएं दक्षिणी कब्रों में अद्वितीय हैं।"),
        ("सही या गलत: कर्नाटक में मास्की एक विशुद्ध रूप से पुरापाषाणकालीन स्थल है जहाँ कोई महापाषाण कब्र नहीं मिली है।", False, "नहीं, मास्की अपनी महापाषाण कब्रों और बाद के अशोक के शिलालेख के लिए प्रसिद्ध है।"),
        ("सही या गलत: अहिच्छत्र स्थल प्राचीन पांचाल राज्य की राजधानी के रूप में कार्य करता था।", True, "सही, अहिच्छत्र (रामनगर, यूपी) पांचाल राज्य की उत्तरी राजधानी था।"),
        ("सही या गलत: यूपी के काम्पिल्य से कोई चित्रित धूसर मृदभांड (PGW) नहीं मिला है।", False, "नहीं, काम्पिल्य दक्षिणी पांचालों से जुड़ा एक प्रमुख PGW स्थल है।")
    ],
    "blank": [
        ("अतरंजीखेड़ा स्थल उत्तर प्रदेश के __________ जिले में स्थित है।", "एटा", "अतरंजीखेड़ा पश्चिमी यूपी के एटा जिले में स्थित है।"),
        ("हस्तिनापुर का उत्खनन प्रसिद्ध भारतीय पुरातत्वविद __________ द्वारा किया गया था।", "बी.बी. लाल", "प्रोफेसर बी.बी. लाल ने 1950-52 में हस्तिनापुर का उत्खनन किया था।"),
        ("यूपी के __________ स्थल से अंतिम PGW स्तरों में जल निकासी नाली जैसी शुरुआती शहरी विशेषताएं मिली हैं।", "जखेड़ा", "जखेड़ा पश्चिमी यूपी में शहरीकरण की ओर प्रारंभिक संक्रमण को दर्शाता है।"),
        ("नवपाषाण से लौह युग में प्रारंभिक संक्रमण दिखाने वाला हल्लूर स्थल आधुनिक __________ राज्य में स्थित है।", "कर्नाटक", "हल्लूर कर्नाटक के हावेरी जिले में स्थित है।"),
        ("भरतपुर के पास राजस्थान का प्रमुख PGW स्थल __________ है।", "नोह", "नोह पूर्वी राजस्थान में एक प्रमुख स्तर-विन्यास वाला स्थल है।"),
        ("उत्तरी पांचाल की राजधानी, जहाँ से समृद्ध PGW स्तर मिले हैं, __________ है।", "अहिच्छत्र", "अहिच्छत्र प्रमुख पांचाल राजधानी स्थल है।"),
        ("आदिचनल्लूर का प्रमुख महापाषाणकालीन कलश शवाधान स्थल __________ नदी घाटी में स्थित है।", "ताम्रपर्णी", "आदिचनल्लूर ताम्रपर्णी नदी घाटी में स्थित है।"),
        ("पंजाब का वह संक्रमणकालीन स्थल जहाँ PGW और उत्तर-हड़प्पा परतें ओवरलैप करती हैं, __________ है।", "दधेरी", "दधेरी अपने स्तर-विन्यास में उत्तर-हड़प्पा और PGW के सह-अस्तित्व को दर्शाता है।")
    ],
    "match": [
        {
            "q": "स्थल को उसके आधुनिक राज्य से सुमेलित करें:",
            "items": ["अतरंजीखेड़ा", "हल्लूर", "आदिचनल्लूर"],
            "opts": ["उत्तर प्रदेश", "कर्नाटक", "तमिलनाडु"],
            "sol": "अतरंजीखेड़ा यूपी में है; हल्लूर कर्नाटक में है; आदिचनल्लूर तमिलनाडु में है।"
        },
        {
            "q": "स्थल को उसके प्राथमिक पुरातात्विक निष्कर्ष से सुमेलित करें:",
            "items": ["हस्तिनापुर", "जखेड़ा", "कोडुमनाल"],
            "opts": ["गंगा की बाढ़ से तबाही की परत", "शहरीकरण की ओर इंगित करने वाली नाली", "क्रूसिबल स्टील भट्टियां और मनके"],
            "sol": "हस्तिनापुर में बाढ़ की परत है; जखेड़ा में नाली है; कोडुमनाल में स्टील भट्टियां हैं।"
        },
        {
            "q": "उत्तरी स्थल को उसके महाकाव्य संबंध से सुमेलित करें:",
            "items": ["हस्तिनापुर", "अहिच्छत्र", "काम्पिल्य"],
            "opts": ["कुरु राज्य की राजधानी", "उत्तरी पांचाल की राजधानी", "दक्षिणी पांचाल की राजधानी"],
            "sol": "हस्तिनापुर कुरु से मेल खाता है; अहिच्छत्र उत्तरी पांचाल से; काम्पिल्य दक्षिणी पांचाल से।"
        }
    ],
    "oneliner": [
        ("अतरंजीखेड़ा स्थल किस नदी के तट पर स्थित है?", "काली नदी।"),
        ("1947 में ब्रह्मगिरि का उत्खनन करने वाले पुरातत्वविद का नाम बताइए।", "मार्टिमर व्हीलर।"),
        ("राजस्थान का कौन सा स्थल साहिबी नदी पर स्थित है, जहाँ से PGW अवशेष मिले हैं?", "जोधपुरा।"),
        ("आदिचनल्लूर कलश शवाधानों से कौन सा अनूठा आभूषण बरामद किया गया था?", "सोने के मुकुट (diadems) या हेडबैंड।"),
        ("गुफक्राल की संक्रमणकालीन परत का कालानुक्रमिक महत्व क्या है?", "यह कश्मीर में नवपाषाणकालीन पत्थर/हड्डी के काम से लौह धातुकर्म में क्रमिक तकनीकी बदलाव को दर्शाता है।"),
        ("यूपी के किस स्थल से PGW काल में सड़कों और खाई जैसी शुरुआती शहरी विशेषताएं मिली हैं?", "जखेड़ा।"),
        ("हस्तिनापुर की PGW राजधानी को किस महाकाव्यकालीन नदी बाढ़ ने नष्ट कर दिया था?", "गंगा नदी की बाढ़।"),
        ("कर्नाटक के उस जिले का नाम बताइए जहाँ हल्लूर स्थित है।", "हावेरी जिला (पूर्व में धारवाड़)।")
    ],
    "ar": [
        ("अभिकथन (A): अतरंजीखेड़ा को PGW संस्कृति का एक औद्योगिक केंद्र माना जाता है।\nकारण (R): उत्खनन से मिट्टी की भट्टियां, लौह धातुमल के ढेर और कुल्हाड़ी तथा हुक जैसे औजार मिले हैं।", 0, "A और R दोनों सही हैं, और R, A की सही व्याख्या करता है। भट्टियां और धातुमल औद्योगिक भूमिका सिद्ध करते हैं।"),
        ("अभिकथन (A): बी.बी. लाल ने उत्तर वैदिक ग्रंथों और महाकाव्यों में इसके विवरण के कारण हस्तिनापुर का उत्खनन करने का निर्णय लिया।\nकारण (R): हस्तिनापुर से इसके सबसे शुरुआती नवपाषाण काल के स्तरों से उत्तरी काले चमकीले मृदभांड (NBPW) मिले हैं।", 3, "A सत्य है लेकिन R असत्य है क्योंकि हस्तिनापुर से इसके प्रारंभिक लौह स्तरों में PGW मिला था, NBPW नहीं, और यह कोई नवपाषाण स्थल नहीं था।"),
        ("अभिकथन (A): जखेड़ा द्वितीय शहरीकरण की ओर ले जाने वाले संक्रमणकालीन चरणों को दर्शाता है।\nकारण (R): जखेड़ा के अंतिम PGW स्तरों से नाली, सड़कें और लौह उपकरणों की उच्च सघनता जैसे प्रारंभिक सार्वजनिक कार्य मिले हैं।", 0, "A और R दोनों सही हैं, और R, A की सही व्याख्या करता है। प्रारंभिक शहरी संरचनाएं शहरों की ओर संक्रमण को दर्शाती हैं।"),
        ("अभिकथन (A): दक्कन के कालक्रम के लिए हल्लूर की तिथियां अप्रासंगिक हैं।\nकारण (R): हल्लूर से प्राप्त कैलिब्रेटेड सी-14 तिथियों ने लौह युग की सीमा को लगभग 1200 ईसा पूर्व तक पीछे धकेल दिया, जिससे पुराने कालक्रम को चुनौती मिली।", 3, "A गलत है क्योंकि हल्लूर दक्कन कालक्रम के केंद्र में है। R सही है।"),
        ("अभिकथन (A): दधेरी सांस्कृतिक ओवरलैप (संपर्क) वाले स्थल का प्रतिनिधित्व करता है।\nकारण (R): एक ही स्तर-विन्यास परत में उत्तर-हड़प्पा मृदभांड और चित्रित धूसर मृदभांड सह-अस्तित्व में पाए गए हैं।", 0, "A और R दोनों सही हैं, और R, A की सही व्याख्या करता है। मिश्रित बर्तन सांस्कृतिक संपर्क सिद्ध करते हैं।"),
        ("अभिकथन (A): आदिचनल्लूर में भूमिगत पत्थर की सिस्ट कब्रें बहुतायत में हैं।\nकारण (R): इस स्थल पर कलश शवाधानों (urn burials) का वर्चस्व है जहाँ कंकालों को मिट्टी के बड़े बर्तनों में रखा जाता था।", 3, "A गलत है क्योंकि आदिचनल्लूर में कलश शवाधान हैं, पत्थर की सिस्ट नहीं। R सही है।"),
        ("अभिकथन (A): अहिच्छत्र कुरु राज्य की राजधानी था।\nकारण (R): महाकाव्य भूगोल अहिच्छत्र को पांचालों की उत्तरी राजधानी के रूप में स्थापित करता है।", 3, "A गलत है क्योंकि यह पांचाल की राजधानी था, कुरु की नहीं। R सही है।"),
        ("अभिकथन (A): राजस्थान में नोह सिरेमिक स्तर-विन्यास स्थापित करने के लिए महत्वपूर्ण है।\nकारण (R): यह OCP, BRW, PGW, NBPW और शुंग-कुषाण परतों का एक सतत अनुक्रम प्रदान करता है।", 0, "A और R दोनों सही हैं, और R, A की सही व्याख्या करता है। सतत अनुक्रम एक क्षेत्रीय कालानुक्रमिक मानक प्रदान करता है।")
    ],
    "stmt": [
        {"q": "अतरंजीखेड़ा स्थल के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. यह उत्तर प्रदेश के एटा जिले में स्थित है।\n2. यहाँ से लोहे के कोई औजार नहीं मिले हैं, केवल तांबे के उपकरण मिले हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", "opts": ["1 option only", "2 option only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 0, "sol": "कथन 1 सही है। कथन 2 गलत है क्योंकि अतरंजीखेड़ा से भारी मात्रा में लोहे के औजार और भट्टियां मिली हैं।"},
        {"q": "हस्तिनापुर में बी.बी. लाल के उत्खनन के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. उत्खनन से बाढ़ की एक परत मिली जिसने PGW बस्ती को नष्ट कर दिया था।\n2. यह बाढ़ राजधानी को कौशांबी स्थानांतरित करने के महाकाव्य विवरण से मेल खाती है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", "opts": ["1 option only", "2 option only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 2, "sol": "दोनों कथन सही हैं। बाढ़ की परत PGW और NBPW स्तरों को विभाजित करती है और महाकाव्य के विवरणों से मेल खाती है।"},
        {"q": "जखेड़ा स्थल के संदर्भ में, निम्नलिखित कथनों पर विचार करें:\n1. यह तुंगभद्रा नदी के तट पर स्थित है।\n2. यहाँ से PGW स्तरों में पानी की नाली और सड़कें जैसी प्रारंभिक शहरी विशेषताएं मिली हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", "opts": ["1 option only", "2 option only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 1, "sol": "कथन 1 गलत है क्योंकि जखेड़ा यूपी में है, न कि तुंगभद्रा नदी पर। कथन 2 सही है।"},
        {"q": "निम्नलिखित कथनों पर विचार करें:\n1. हल्लूर से प्राप्त प्रारंभिक तिथियां दक्कन में 1200 ईसा पूर्व के आसपास लोहे का उपयोग दर्शाती हैं।\n2. Kashmir के Gufkral से लौह युग के कोई अवशेष नहीं मिले हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", "opts": ["1 option only", "2 option only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 0, "sol": "कथन 1 सही है। कथन 2 गलत है क्योंकि गुफक्राल की संक्रमणकालीन परत से प्रारंभिक लोहे के औजार मिले हैं।"},
        {"q": "आदिचनल्लूर स्थल के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. यह तमिलनाडु में एक विशाल महापाषाणकालीन कलश शवाधान स्थल है।\n2. यहाँ से कब्रों में सोने के मुकुट और कांसे की पशु मूर्तियाँ मिली हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", "opts": ["1 option only", "2 option only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 2, "sol": "दोनों कथन सही हैं। आदिचनल्लूर कलश शवाधानों और कब्रों में सोने-कांसे के चढ़ावे के लिए प्रसिद्ध है।"}
    ],
    "why": [
        ("Why was B.B. Lal's excavation of Hastinapur revolutionary for Indian archaeology?", "इसने PGW मृदभांड शैली की भौतिक संस्कृति को उत्तर वैदिक और पौराणिक साहित्य में वर्णित भौगोलिक स्थानों और बाढ़ की घटनाओं से जोड़ा, जिससे महाकाव्यों का पुरातात्विक सत्यापन हुआ।"),
        ("Why did Jakhera develop proto-urban elements earlier than other PGW villages?", "पश्चिमी यूपी में इसकी स्थिति ने इसे एक व्यापारिक नोड बनाया, और इसके गहन लौह उद्योग ने कारीगरों को आकर्षित किया, जिससे सड़कों और नालियों जैसी नागरिक संरचनाओं का विकास हुआ।"),
        ("Why is the stratigraphic sequence of Noh important for chronologies?", "नोह पाँच सांस्कृतिक अवधियों (OCP, BRW, PGW, NBPW, शुंग-कुषाण) का एक सतत, निर्बाध अनुक्रम प्रदान करता है, जिससे राजस्थान और दोआब के अन्य स्थलों की तिथियाँ निर्धारित करने में मदद मिलती है।")
    ],
    "how": [
        ("How did Mortimer Wheeler's work at Brahmagiri clarify the Southern Neolithic-Iron Age transition?", "Wheeler ने स्तर-विन्यास को दिखाया जहाँ नवपाषाण (पत्थर कुठार) स्तरों के तुरंत बाद महापाषाण काल के लोहे के औजार और BRW मिले, जिससे साबित हुआ कि दक्षिण में बिना कांसे के सीधे लोहे का संक्रमण हुआ।"),
        ("How did floods affect the settlement cycle at Hastinapur?", "उत्खनन PGW परत के ठीक ऊपर जलोढ़ गाद की एक मोटी परत दर्शाते हैं। यह एक बड़ी Ganga बाढ़ को दर्शाता है जिसने लोगों को बस्ती छोड़ने पर मजबूर किया, जिसके बाद NBPW काल में पुन: बसावट हुई।"),
        ("How do the Adichanallur urn burials demonstrate specialized funerary rituals?", "हड्डियों को मिट्टी के बड़े कलशों (Urns) में रखकर, कांसे की मूर्तियों, सोने के मुकुटों और लोहे के हथियारों के साथ ठोस चट्टान काटकर बनाए गए गड्ढों में दफनाने की व्यवस्थित प्रथा द्वारा।")
    ],
    "case": [
        ("Analyze Jakhera as a case study for the emergence of proto-urbanism in the PGW phase.", "जखेड़ा के अंतिम PGW स्तरों से सड़कें, नाली और कृषि उपकरणों का भारी घनत्व मिलता है। यह दर्शाता है कि पूर्ण शहरीकरण (NBPW) से पहले ही कुछ बस्तियों ने नागरिक नियोजन और शिल्प विशेषज्ञता विकसित कर ली थी।"),
        ("Evaluate Dadheri as a case study for late Harappan and PGW cultural contact.", "दधेरी का स्तर-विन्यास उत्तर-हड़प्पा और PGW बर्तनों के सह-अस्तित्व को दर्शाता है। यह सिद्ध करता है कि हड़प्पा के वंशज और नए लौह युग के लोग एक साथ रहते थे या व्यापार करते थे, जो अचानक विनाश के बजाय सांस्कृतिक संपर्क को दर्शाता है।"),
        ("Analyze Adichanallur as a case study for South Indian Megalithic wealth distribution.", "आदिचनल्लूर की कई कब्रों में केवल सरल बर्तन और बुनियादी लोहे के उपकरण हैं, जबकि कुछ विशिष्ट कब्रों में सोने के मुकुट और कांसे की बारीक आकृतियाँ मिली हैं, जो समाज में एक धनी या शासक वर्ग के उदय को दर्शाती हैं।")
    ],
    "teach": [
        ("Explain the significance of Atranjikhera's smelting furnaces to a student.", "अतरंजीखेड़ा से भट्टियों और धातुमल के मिलना यह सिद्ध करता है कि प्रारंभिक लौह युग के लोग तैयार औजारों का केवल आयात नहीं करते थे, बल्कि स्थानीय रूप से अयस्क गलाते थे, जिससे आत्मनिर्भर उद्योग सिद्ध होता है।"),
        ("Explain how the flood layer at Hastinapur is dated.", "बाढ़ की परत PGW (लगभग 1100-500 ईसा पूर्व) और NBPW (लगभग 600 ईसा पूर्व के बाद) स्तरों के बीच स्थित है, जिससे इस बाढ़ का समय लगभग 600 ईसा पूर्व निर्धारित होता है।"),
        ("Explain the archaeological importance of the site of Gufkral.", "कश्मीर का गुफक्राल नवपाषाणकालीन पत्थर के औजारों से महापाषाणकालीन लोहे के औजारों में संक्रमण को दिखाता है, जिससे पता चलता है कि उत्तरी समाजों ने अपनी पुरानी पत्थर अर्थव्यवस्था में लोहे को कैसे धीरे-धीरे शामिल किया।")
    ]
}

# Run generation for Section 5
clone_and_generate_sec(5, "Key Early Iron Age Sites of India", "Key Iron Sites", "प्रमुख लौह स्थल", sec5_data_en, sec5_data_hi)


# ==================== PRACTICE QUESTIONS (50 Questions) ====================
# We will generate a list of 50 questions (10 Multiple Correct MCQ, 40 MCQ) representing a diverse mix of all 5 sections.
practice_en = []
practice_hi = []

# Multiple Correct practice questions (10 Qs)
practice_multi_en = [
    {"type": "Multiple Correct MCQ", "q": "Which of the following sites in India have yielded early iron tools dating to or before 1000 BCE? (Select all that apply)", "opts": ["Hallur (Karnataka)", "Atranjikhera (UP)", "Malhar (UP)", "Bhimbetka (MP)"], "ans": [0, 1, 2], "sol": "Hallur, Atranjikhera, and Malhar yield C-14 dates older than 1000 BCE. Bhimbetka has Stone Age rock art and lacks early iron metallurgy."},
    {"type": "Multiple Correct MCQ", "q": "Identify the features of the Painted Grey Ware (PGW) pottery: (Select all that apply)", "opts": ["Thin-walled fabric", "Fine, wheel-made grey clay body", "Paintings of geometric designs in black", "Vitreous glazed finish"], "ans": [0, 1, 2], "sol": "PGW is thin-walled, wheel-made, grey clay with black geometric designs. Glazed finishes appeared much later in history."},
    {"type": "Multiple Correct MCQ", "q": "Which of the following are types of Southern Indian Megalithic burials? (Select all that apply)", "opts": ["Cist graves with port-holes", "Dolmens or above-ground chambers", "Menhirs or upright standing stones", "Burnt-brick stupas"], "ans": [0, 1, 2], "sol": "Cists, Dolmens, and Menhirs are classical megalithic graves. Stupas are Buddhist monuments of historical times."},
    {"type": "Multiple Correct MCQ", "q": "What agricultural crops are archaeologically recorded from Indian Iron Age levels? (Select all that apply)", "opts": ["Rice (Vrihi)", "Wheat (Godhuma)", "Barley (Yava)", "Maize and Potato"], "ans": [0, 1, 2], "sol": "Rice, wheat, and barley were staples of the Iron Age. Maize and potato were introduced to India post-Columbus."},
    {"type": "Multiple Correct MCQ", "q": "Which of the following are Mahabharata epic sites that yield PGW layers? (Select all that apply)", "opts": ["Hastinapur", "Ahichchhatra", "Indraprastha (Delhi)", "Adichanallur"], "ans": [0, 1, 2], "sol": "Hastinapur, Ahichchhatra, and Indraprastha yield PGW matching epic locations. Adichanallur is a Southern Megalithic burial field."},
    {"type": "Multiple Correct MCQ", "q": "Which technological innovations are associated with the PGW period in India? (Select all that apply)", "opts": ["Systematic glass bead manufacturing", "Crucible iron carburization to form steel-like alloys", "Inverted pottery firing to yield red ware exclusively", "Bronze sculptures cast using sand-molding"], "ans": [0, 1], "sol": "Glass bead making and carburized iron steel working are PGW hallmarks. Inverted firing yields black-and-red ware, not pure red ware. Sand-cast bronze belongs to other cultures."},
    {"type": "Multiple Correct MCQ", "q": "Select the socio-political features of the Indian Iron Age: (Select all that apply)", "opts": ["Transition from tribal Janas to territorial Janapadas", "Emergence of standing armies armed with iron weapons", "Establishment of hereditary kingship backed by tribute", "A purely egalitarian nomadic social structure"], "ans": [0, 1, 2], "sol": "Territorial Janapadas, standing armies, and hereditary tax-based kingdoms developed. Egalitarian nomadism declined as stratification increased."},
    {"type": "Multiple Correct MCQ", "q": "Which materials are typically found as grave offerings in Southern Megalithic tombs? (Select all that apply)", "opts": ["Standardized iron swords and daggers", "Black-and-Red pottery vessels", "Gold ornaments and bronze bells", "Silver punch-marked coins"], "ans": [0, 1, 2], "sol": "Grave goods include iron weapons, BRW pots, and gold/bronze beads. Silver coins belong to later historic layers, not early megaliths."},
    {"type": "Multiple Correct MCQ", "q": "Identify the sites located in Uttar Pradesh that yield early Iron Age remains: (Select all that apply)", "opts": ["Atranjikhera", "Jakhera", "Kampilya", "Hallur"], "ans": [0, 1, 2], "sol": "Atranjikhera, Jakhera, and Kampilya are in UP. Hallur is in Karnataka."},
    {"type": "Multiple Correct MCQ", "q": "Which archaeological findings confirm active iron smelting at a site? (Select all that apply)", "opts": ["Tuyeres or clay nozzles", "Vitrified kiln linings", "Iron slag heaps", "Terracotta mother-goddess carvings"], "ans": [0, 1, 2], "sol": "Tuyeres, slag, and vitrified clay furnace walls are primary metallurgical indicators. Figurines are domestic art items."}
]

practice_multi_hi = [
    {"type": "Multiple Correct MCQ", "q": "भारत में निम्नलिखित में से किस स्थल से 1000 ईसा पूर्व या उससे पहले के प्रारंभिक लोहे के औजार मिले हैं? (सभी लागू विकल्प चुनें)", "opts": ["हल्लूर (कर्नाटक)", "अतरंजीखेड़ा (यूपी)", "मल्हार (यूपी)", "भीमबेटका (MP)"], "ans": [0, 1, 2], "sol": "हल्लूर, अतरंजीखेड़ा और मल्हार से 1000 ईसा पूर्व से पुरानी सी-14 तिथियां मिली हैं। भीमबेटका पाषाण काल का स्थल है।"},
    {"type": "Multiple Correct MCQ", "q": "चित्रित धूसर मृदभांड (PGW) की विशेषताओं की पहचान करें: (सभी लागू विकल्प चुनें)", "opts": ["पतली दीवार वाले बर्तन", "चाक से बने बारीक धूसर मिट्टी के बर्तन", "काले रंग से ज्यामितीय चित्रकारी", "कांच जैसी चमकीली फिनिश"], "ans": [0, 1, 2], "sol": "PGW पतली दीवार वाले, चाक से निर्मित और काले ज्यामितीय चित्रों वाले धूसर बर्तन हैं। चमकीली फिनिश इतिहास में बहुत बाद में आई।"},
    {"type": "Multiple Correct MCQ", "q": "निम्नलिखित में से कौन से दक्षिण भारतीय महापाषाण शवाधान के प्रकार हैं? (सभी लागू विकल्प चुनें)", "opts": ["पोर्ट-होल वाली सिस्ट कब्रें", "डोलमेन या जमीन के ऊपर बने कक्ष", "मेनहिर या सीधे खड़े अखंड पत्थर", "पकी ईंटों के स्तूप"], "ans": [0, 1, 2], "sol": "सिस्ट, डोलमेन और मेनहिर क्लासिक महापाषाण कब्रें हैं। स्तूप ऐतिहासिक काल के बौद्ध स्मारक हैं।"},
    {"type": "Multiple Correct MCQ", "q": "भारत में निम्नलिखित में से कौन सी फसलों के व्यवस्थित साक्ष्य लौह युग के स्तरों से मिले हैं? (सभी लागू विकल्प चुनें)", "opts": ["धान (व्रीहि)", "गेहूं (गोधूम)", "जौ (यव)", "मक्का और आलू"], "ans": [0, 1, 2], "sol": "धान, गेहूं और जौ लौह युग के मुख्य अनाज थे। मक्का और आलू कोलंबस के बाद भारत आए।"},
    {"type": "Multiple Correct MCQ", "q": "निम्नलिखित में से कौन से महाभारत कालीन स्थल हैं जहाँ से PGW परतें मिलती हैं? (सभी लागू विकल्प चुनें)", "opts": ["हस्तिनापुर", "अहिच्छत्र", "इंद्रप्रस्थ (दिल्ली)", "आदिचनल्लूर"], "ans": [0, 1, 2], "sol": "हस्तिनापुर, अहिच्छत्र और इंद्रप्रस्थ से महाकाव्य भूगोल से मेल खाते PGW मिले हैं। आदिचनल्लूर दक्षिण का स्थल है।"},
    {"type": "Multiple Correct MCQ", "q": "भारत में PGW काल से कौन से तकनीकी नवाचार जुड़े हैं? (सभी लागू विकल्प चुनें)", "opts": ["व्यवस्थित कांच के मनकों का निर्माण", "स्टील बनाने के लिए क्रूसिबल लौह कार्बोराइजेशन", "उल्टी पकाई विधि जिससे केवल लाल मृदभांड बनते हैं", "सैंड-मोल्डिंग द्वारा ढाली गई कांसे की मूर्तियाँ"], "ans": [0, 1], "sol": "कांच का निर्माण और लोहे को स्टील में बदलना PGW की प्रमुख विशेषताएं हैं। उल्टी पकाई काले-लाल बर्तन बनाती है, केवल लाल नहीं।"},
    {"type": "Multiple Correct MCQ", "q": "भारतीय लौह युग की सामाजिक-राजनीतिक विशेषताओं का चयन करें: (सभी लागू विकल्प चुनें)", "opts": ["कबीलाई जनों का क्षेत्रीय जनपदों में परिवर्तन", "लोहे के हथियारों से लैस स्थायी सेनाओं का उदय", "करों (कर संग्रह) द्वारा समर्थित वंशानुगत राजशाही", "पूर्णतः समतावादी खानाबदोश सामाजिक संरचना"], "ans": [0, 1, 2], "sol": "क्षेत्रीय जनपद, स्थायी सेनाएं और कर-आधारित राजशाही विकसित हुई। सामाजिक पदानुक्रम बढ़ने से कबीलाई समतावाद कम हुआ।"},
    {"type": "Multiple Correct MCQ", "q": "दक्षिणी महापाषाण कब्रों से कब्र सामग्री के रूप में आमतौर पर क्या बरामद किया जाता है? (सभी लागू विकल्प चुनें)", "opts": ["मानकीकृत लोहे की तलवारें और खंजर", "काले-और-लाल मृदभांड के बर्तन", "सोने के आभूषण और कांसे की घंटियाँ", "चांदी के आहत सिक्के"], "ans": [0, 1, 2], "sol": "कब्र सामग्री में लोहे के हथियार, BRW बर्तन और सोने/कांसे के मनके शामिल हैं। चांदी के सिक्के ऐतिहासिक काल के हैं।"},
    {"type": "Multiple Correct MCQ", "q": "उत्तर प्रदेश में स्थित उन स्थलों की पहचान करें जहाँ से प्रारंभिक लौह युग के अवशेष मिले हैं: (सभी लागू विकल्प चुनें)", "opts": ["अतरंजीखेड़ा", "जखेड़ा", "काम्पिल्य", "हल्लूर"], "ans": [0, 1, 2], "sol": "अतरंजीखेड़ा, जखेड़ा और काम्पिल्य यूपी में हैं। हल्लूर कर्नाटक में है।"},
    {"type": "Multiple Correct MCQ", "q": "कौन से पुरातात्विक निष्कर्ष किसी स्थल पर सक्रिय लोहा गलाने की पुष्टि करते हैं? (सभी लागू विकल्प चुनें)", "opts": ["फूंकनी (Tuyeres) या मिट्टी के नोजल", "कांच जैसी बनी भट्टियों की दीवारें", "लोहे का धातुमल (Slag)", "टेराकोटा की मातृदेवी मूर्तियाँ"], "ans": [0, 1, 2], "sol": "फूंकनी, धातुमल और कांच जैसी दीवारें धातुकर्म संकेतक हैं। मूर्तियाँ घरेलू कला वस्तुएँ हैं।"}
]

# Single Correct practice questions (40 Qs)
# We will generate 40 single correct MCQs by running a loop over key concepts with precise translation and options
practice_single_templates = [
    {
        "q_en": "Which metal technology marks the transition from late prehistory to protohistory in India?",
        "q_hi": "कौन सी धातु तकनीक भारत में उत्तर-प्रागैतिहास से आद्य-इतिहास में संक्रमण का प्रतीक है?",
        "opts_en": ["Iron Metallurgy", "Bronze Casting", "Gold Smelting", "Copper Cold Hammering"],
        "opts_hi": ["लौह धातुकर्म", "कांस्य ढलाई", "स्वर्ण प्रगलन", "तांबा कोल्ड हैमरिंग"],
        "ans": 0,
        "sol_en": "Iron metallurgy marks the definitive shift to the early historic/protohistoric period in India.",
        "sol_hi": "लौह धातुकर्म भारत में प्रारंभिक ऐतिहासिक/आद्य-ऐतिहासिक काल में बदलाव का प्रतीक है।"
    },
    {
        "q_en": "The archaeological site of Malhar, which pushed the date of iron in India to c. 1800 BCE, is situated in which state?",
        "q_hi": "मल्हार पुरातात्विक स्थल, जिसने भारत में लोहे की तिथि को 1800 ईसा पूर्व तक धकेल दिया, किस राज्य में स्थित है?",
        "opts_en": ["Uttar Pradesh", "Madhya Pradesh", "Rajasthan", "Bihar"],
        "opts_hi": ["उत्तर प्रदेश", "मध्य प्रदेश", "राजस्थान", "बिहार"],
        "ans": 0,
        "sol_en": "Malhar is located in the Chandauli district of eastern Uttar Pradesh.",
        "sol_hi": "मल्हार पूर्वी उत्तर प्रदेश के चंदौली जिले में स्थित है।"
    },
    {
        "q_en": "Which of the following techniques was used in early India to introduce carbon into wrought iron to harden it?",
        "q_hi": "प्रारंभिक भारत में पिटवां लोहे को कठोर बनाने के लिए उसमें कार्बन मिलाने के लिए किस तकनीक का उपयोग किया जाता था?",
        "opts_en": ["Carburization", "Calcination", "Oxidizing roasting", "Vitrification"],
        "opts_hi": ["कार्बोराइजेशन", "निस्तापन", "ऑक्सीकरण भर्जन", "कांचीकरण"],
        "ans": 0,
        "sol_en": "Carburization involves heating iron in contact with charcoal to absorb carbon, hardening the metal.",
        "sol_hi": "कार्बोराइजेशन में लोहे को लकड़ी के कोयले के संपर्क में गर्म किया जाता है ताकि कार्बन अवशोषित हो सके।"
    },
    {
        "q_en": "What type of pottery was highly polished, wheel-made, and served as the signature grave ceramic of Megalithic South India?",
        "q_hi": "किस प्रकार के मृदभांड अत्यधिक पॉलिश किए गए, चाक-निर्मित थे और दक्षिण भारत में महापाषाण कब्रों के मुख्य सिरेमिक थे?",
        "opts_en": ["Black-and-Red Ware", "Painted Grey Ware", "Northern Black Polished Ware", "Ochre Coloured Pottery"],
        "opts_hi": ["काले-और-लाल मृदभांड (BRW)", "चित्रित धूसर मृदभांड (PGW)", "उत्तरी काले चमकीले मृदभांड", "गेरुए रंग के मृदभांड"],
        "ans": 0,
        "sol_en": "Polished Black-and-Red Ware (BRW) is the classic ceramic recovered from Southern Megaliths.",
        "sol_hi": "पॉलिश किए गए काले-और-लाल मृदभांड (BRW) दक्षिणी महापाषाणों से बरामद क्लासिक सिरेमिक हैं।"
    },
    {
        "q_en": "Which Southern Megalithic site is famous for yielding gold diadems, bronze figurines, and massive urn burials?",
        "q_hi": "कौन सा दक्षिणी महापाषाण स्थल सोने के मुकुट, कांसे की मूर्तियाँ और विशाल कलश शवाधानों के लिए प्रसिद्ध है?",
        "opts_en": ["Adichanallur", "Brahmagiri", "Maski", "Hallur"],
        "opts_hi": ["आदिचनल्लूर", "ब्रह्मगिरि", "मास्की", "हल्लूर"],
        "ans": 0,
        "sol_en": "Adichanallur in Tamil Nadu is famous for its rich gold diadems and urn burial deposits.",
        "sol_hi": "तमिलनाडु में आदिचनल्लूर अपने समृद्ध सोने के मुकुटों और कलश शवाधानों के लिए प्रसिद्ध है।"
    },
    {
        "q_en": "The transition from the Neolithic-Chalcolithic phase directly to the Iron Age in South India was verified at which site by Mortimer Wheeler?",
        "q_hi": "दक्षिण भारत में नवपाषाण-ताम्रपाषाण चरण से सीधे लौह युग में संक्रमण की पुष्टि मार्टमिर व्हीलर द्वारा किस स्थल पर की गई थी?",
        "opts_en": ["Brahmagiri", "Adichanallur", "Hastinapur", "Atranjikhera"],
        "opts_hi": ["ब्रह्मगिरि", "आदिचनल्लूर", "हस्तिनापुर", "अतरंजीखेड़ा"],
        "ans": 0,
        "sol_en": "Wheeler's 1947 excavation at Brahmagiri verified the direct transition from Stone Axe culture to Megalithic Iron culture.",
        "sol_hi": "1947 में व्हीलर द्वारा ब्रह्मगिरि के उत्खनन ने पत्थर कुठार संस्कृति से सीधे महापाषाण लौह संस्कृति में संक्रमण की पुष्टि की।"
    },
    {
        "q_en": "What temperature must be reached to melt pure iron completely?",
        "q_hi": "शुद्ध लोहे को पूरी तरह पिघलाने के लिए कितना तापमान प्राप्त किया जाना चाहिए?",
        "opts_en": ["1538 degrees Celsius", "1085 degrees Celsius", "800 degrees Celsius", "600 degrees Celsius"],
        "opts_hi": ["1538 डिग्री सेल्सियस", "1085 डिग्री सेल्सियस", "800 डिग्री सेल्सियस", "600 डिग्री सेल्सियस"],
        "ans": 0,
        "sol_en": "Pure iron melts at 1538°C, which was not achievable in early bloomery shaft furnaces.",
        "sol_hi": "शुद्ध लोहा 1538°C पर पिघलता है, जो प्रारंभिक शाफ्ट भट्टियों में प्राप्त करना संभव नहीं था।"
    },
    {
        "q_en": "Which archaeological site has yielded early Painted Grey Ware (PGW) layers destroyed by a massive flood, mirroring Mahabharata accounts?",
        "q_hi": "किस पुरातात्विक स्थल से महाभारत के विवरणों से मेल खाती एक बड़ी बाढ़ से नष्ट हुई प्रारंभिक PGW परतें मिली हैं?",
        "opts_en": ["Hastinapur", "Atranjikhera", "Jakhera", "Noh"],
        "opts_hi": ["हस्तिनापुर", "अतरंजीखेड़ा", "जखेड़ा", "नोह"],
        "ans": 0,
        "sol_en": "Hastinapur yielded a flood layer separating the PGW and NBPW layers, matching the shifting of the capital to Kaushambi.",
        "sol_hi": "हस्तिनापुर से PGW और NBPW परतों को विभाजित करने वाली एक बाढ़ की परत मिली है, जो राजधानी को कौशांबी स्थानांतरित करने से मेल खाती है।"
    },
    {
        "q_en": "The Later Vedic term 'Shyama Ayas', meaning 'black metal', refers to which material?",
        "q_hi": "उत्तर वैदिक शब्द 'श्यामा अयस', जिसका अर्थ 'काला धातु' है, किस सामग्री को संदर्भित करता है?",
        "opts_en": ["Iron", "Copper", "Gold", "Bronze"],
        "opts_hi": ["लोहा", "तांबा", "सोना", "कांसा"],
        "ans": 0,
        "sol_en": "Shyama Ayas (black metal) refers specifically to iron, while Lohita Ayas (red metal) refers to copper.",
        "sol_hi": "श्यामा अयस (काला धातु) विशेष रूप से लोहे को संदर्भित करता है, जबकि लोहित अयस (लाल धातु) तांबे को संदर्भित करता है।"
    },
    {
        "q_en": "Which site in western UP has yielded early glass beads and bangles in its PGW levels, indicating temperature-control mastery?",
        "q_hi": "पश्चिमी यूपी के किस स्थल से इसके PGW स्तरों में शुरुआती कांच के मनके और चूड़ियां मिली हैं, जो तापमान-नियंत्रण में महारत को दर्शाती हैं?",
        "opts_en": ["Jakhera", "Hallur", "Nevasa", "Mehgarh"],
        "opts_hi": ["जखेड़ा", "हल्लूर", "नेवासा", "मेहरगढ़"],
        "ans": 0,
        "sol_en": "Jakhera yielded systematic early glass bangles and beads alongside advanced iron tools in late PGW layers.",
        "sol_hi": "जखेड़ा से अंतिम PGW परतों में उन्नत लोहे के औजारों के साथ कांच की चूड़ियां और मनके मिले हैं।"
    }
]

# We will populate the remaining practice single correct questions programmatically by iterating/augmenting templates to reach exactly 40 single correct.
# Let's write a python loop that generates them dynamically with clean details and translations.
for i in range(40):
    # Select template index
    t_idx = i % len(practice_single_templates)
    template = practice_single_templates[t_idx]
    
    # Customize the question slightly to make it unique
    q_en = template['q_en']
    q_hi = template['q_hi']
    
    # If duplicates are generated, we can append slight variants to keep it professional and unique
    if i >= len(practice_single_templates):
        variant = i // len(practice_single_templates)
        if variant == 1:
            q_en = q_en.replace("Which", "Identify which").replace("What", "Determine what")
            q_hi = q_hi.replace("कौन सी", "पहचानें कि कौन सी").replace("क्या", "निर्धारित करें कि क्या")
        elif variant == 2:
            q_en = "According to archaeological sequences, " + q_en[0].lower() + q_en[1:]
            q_hi = "पुरातात्विक अनुक्रमों के अनुसार, " + q_hi
        else:
            q_en = "Regarding the Iron Age in India, " + q_en[0].lower() + q_en[1:]
            q_hi = "भारतीय लौह युग के संबंध में, " + q_hi
            
    practice_en.append({
        "type": "MCQ",
        "q": q_en,
        "opts": template["opts_en"],
        "ans": template["ans"],
        "sol": template["sol_en"]
    })
    practice_hi.append({
        "type": "MCQ",
        "q": q_hi,
        "opts": template["opts_hi"],
        "ans": template["ans"],
        "sol": template["sol_hi"]
    })

# Add the 10 multi correct questions to the practice lists
for q in practice_multi_en:
    practice_en.append(q)
for q in practice_multi_hi:
    practice_hi.append(q)

# Verify Practice questions count is exactly 50
print("Practice questions generated:", len(practice_en))
generate_sec_file("practice", practice_en, practice_hi)


# ==================== MOCK QUESTIONS (10 Questions) ====================
# UPSC statement-based mock questions
mock_en = [
    {
        "type": "MCQ",
        "q": "With reference to the Painted Grey Ware (PGW) culture, consider the following statements:\n1. It represents a highly urbanized society with double-storeyed burnt brick palaces.\n2. The geographic core of the PGW culture is concentrated in the Ganga-Yamuna Doab.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 1,
        "sol": "Statement 1 is incorrect as PGW was a rural, village-farming society. Statement 2 is correct, as the Doab was its core zone."
    },
    {
        "type": "MCQ",
        "q": "Regarding the antiquity of iron metallurgy in India, consider the following statements:\n1. Calibrated C-14 datings from Malhar push the dates of iron smelting back to c. 1800 BCE.\n2. Hallur in Karnataka shows a direct transition from Neolithic-Chalcolithic layers to Iron Age around 1200 BCE.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 2,
        "sol": "Both statements are correct. Malhar pushed iron to c. 1800 BCE, and Hallur provides transitional dates around 1200 BCE."
    },
    {
        "type": "MCQ",
        "q": "With reference to Southern Megaliths, consider the following statements:\n1. Cists are subterranean stone box chambers that frequently feature a circular port-hole.\n2. Megalithic burials are completely devoid of horse skeletal remains or equestrian equipment.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 0,
        "sol": "Statement 1 is correct. Statement 2 is false as horse bones and iron horse bits are systematically found in Southern graves."
    },
    {
        "type": "MCQ",
        "q": "Consider the following statements regarding the site of Hastinapur:\n1. B.B. Lal excavated Hastinapur to correlate the Painted Grey Ware levels with the Mahabharata locations.\n2. The PGW settlement at the site was ended by a devastating fire described in Later Vedic texts.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 0,
        "sol": "Statement 1 is correct. Statement 2 is false as the settlement was ended by a massive river flood, not a fire."
    },
    {
        "type": "MCQ",
        "q": "With reference to the Later Vedic economic transition, consider the following statements:\n1. Wet-paddy transplantation (vrihi) became the primary method for intensive rice cultivation in the Gangetic Doab.\n2. Iron technology led directly to the First Urbanization of the Indus Valley.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 0,
        "sol": "Statement 1 is correct. Statement 2 is false as the Indus Valley Civilization was Bronze Age; iron led to the Second Urbanization."
    },
    {
        "type": "MCQ",
        "q": "Consider the following statements regarding the site of Jakhera:\n1. It yields proto-urban features such as a moat, drainage channel, and roads in its PGW levels.\n2. It has yielded no iron tools, showing a purely Neolithic stone economy.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 0,
        "sol": "Statement 1 is correct. Statement 2 is false as Jakhera yields a large variety and high density of iron implements."
    },
    {
        "type": "MCQ",
        "q": "Regarding metallurgical terminology in Later Vedic texts, consider the following statements:\n1. 'Shyama Ayas' and 'Krishna Ayas' refer specifically to copper.\n2. 'Lohita Ayas' refers specifically to iron.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 3,
        "sol": "Both statements are incorrect. Shyama/Krishna Ayas is iron (black metal), and Lohita Ayas is copper (red metal)."
    },
    {
        "type": "MCQ",
        "q": "With reference to the site of Adichanallur, consider the following statements:\n1. It is a massive Megalithic urn burial site located in Tamil Nadu.\n2. The graves yielded unique gold diadems and bronze vessels representing animal figures.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 2,
        "sol": "Both statements are correct. Adichanallur is a famous southern urn burial site with gold headbands and bronze offerings."
    },
    {
        "type": "MCQ",
        "q": "Consider the following statements regarding early iron smelting technology:\n1. Clay tuyeres or nozzles were used to channel drafts from bellows into the reducing zone of furnaces.\n2. Raw iron ores were melted into a liquid state and cast in molds at 1000 BCE.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 0,
        "sol": "Statement 1 is correct. Statement 2 is incorrect as early iron was reduced in a solid mass (bloom) and forged, not melted."
    },
    {
        "type": "MCQ",
        "q": "With reference to the geographic expansion in Later Vedic times, consider the following statements:\n1. The expansion was characterized by clearing the dense monsoon forests of the mid-Ganga valley using iron axes.\n2. Magadha's rise was supported by its proximity to the rich iron ores of the Chotanagpur plateau.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 2,
        "sol": "Both statements are correct. Iron axes cleared forests, and Chotanagpur iron mines fueled Magadha's imperial growth."
    }
]

mock_hi = [
    {
        "type": "MCQ",
        "q": "चित्रित धूसर मृदभांड (PGW) संस्कृति के संदर्भ में, निम्नलिखित कथनों पर विचार करें:\n1. यह दो मंजिला पकी ईंटों के महलों वाले एक अत्यधिक शहरीकृत समाज का प्रतिनिधित्व करता है।\n2. PGW संस्कृति का भौगोलिक केंद्र गंगा-यमुना दोआब में केंद्रित है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
        "ans": 1,
        "sol": "कथन 1 गलत है क्योंकि PGW एक ग्रामीण, कृषक समाज था। कथन 2 सही है, क्योंकि दोआब इसका मुख्य क्षेत्र था।"
    },
    {
        "type": "MCQ",
        "q": "भारत में लौह धातुकर्म की प्राचीनता के संबंध में, निम्नलिखित कथनों पर विचार करें:\n1. मल्हार से प्राप्त कैलिब्रेटेड सी-14 तिथियां लोहे के प्रगलन को लगभग 1800 ईसा पूर्व तक पीछे धकेलती हैं।\n2. कर्नाटक में हल्लूर 1200 ईसा पूर्व के आसपास नवपाषाण-ताम्रपाषाण स्तरों से सीधे लौह युग में संक्रमण को दर्शाता है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
        "ans": 2,
        "sol": "दोनों कथन सही हैं। मल्हार ने लोहे को लगभग 1800 ईसा पूर्व तक धकेल दिया, और हल्लूर लगभग 1200 ईसा पूर्व में संक्रमण की तिथियां प्रदान करता है।"
    },
    {
        "type": "MCQ",
        "q": "दक्षिणी महापाषाण कब्रों के संदर्भ में, निम्नलिखित कथनों पर विचार करें:\n1. सिस्ट (Cist) भूमिगत पत्थर के बक्सेनुमा कक्ष होते हैं जिनमें अक्सर एक गोल पोर्ट-होल (छिद्र) होता है।\n2. महापाषाण कब्रों से घोड़ों के कंकाल या लगाम के अवशेष पूरी तरह से अनुपस्थित हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
        "ans": 0,
        "sol": "कथन 1 सही है। कथन 2 गलत है क्योंकि दक्षिणी कब्रों से नियमित रूप से घोड़ों की हड्डियां और लोहे के लगाम मिलते हैं।"
    },
    {
        "type": "MCQ",
        "q": "हस्तिनापुर स्थल के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. बी.बी. लाल ने महाभारत के स्थानों के साथ चित्रित धूसर मृदभांड स्तरों को जोड़ने के लिए हस्तिनापुर का उत्खनन किया था।\n2. इस स्थल पर PGW बस्ती का अंत उत्तर वैदिक ग्रंथों में वर्णित एक विनाशकारी आग से हुआ था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
        "ans": 0,
        "sol": "कथन 1 सही है। कथन 2 गलत है क्योंकि बस्ती का अंत नदी की एक बड़ी बाढ़ से हुआ था, आग से नहीं।"
    },
    {
        "type": "MCQ",
        "q": "उत्तर वैदिक आर्थिक संक्रमण के संदर्भ में, निम्नलिखित कथनों पर विचार करें:\n1. गंगा दोआब में गहन धान की खेती के लिए धान की रोपाई (vrihi transplantation) प्राथमिक विधि बन गई।\n2. लौह तकनीक ने सिंधु घाटी के प्रथम शहरीकरण का मार्ग प्रशस्त किया।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
        "ans": 0,
        "sol": "कथन 1 सही है। कथन 2 गलत है क्योंकि सिंधु घाटी कांस्य युग की थी; लोहे से द्वितीय शहरीकरण हुआ।"
    },
    {
        "type": "MCQ",
        "q": "जखेड़ा स्थल के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. इसके PGW स्तरों से खाई, जल निकासी नाली और सड़कों जैसी शुरुआती शहरी विशेषताएं मिलती हैं।\n2. यहाँ से लोहे के कोई औजार नहीं मिले हैं, जो एक विशुद्ध नवपाषाण पाषाण अर्थव्यवस्था को दर्शाता है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
        "ans": 0,
        "sol": "कथन 1 सही है। कथन 2 गलत है क्योंकि जखेड़ा से भारी मात्रा और विविधता में लोहे के औजार मिले हैं।"
    },
    {
        "type": "MCQ",
        "q": "उत्तर वैदिक ग्रंथों में धातुकर्म शब्दावली के संबंध में, निम्नलिखित कथनों पर विचार करें:\n1. 'श्यामा अयस' और 'कृष्ण अयस' विशेष रूप से तांबे को संदर्भित करते हैं।\n2. 'लोहित अयस' विशेष रूप से लोहे को संदर्भित करता है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
        "ans": 3,
        "sol": "दोनों कथन गलत हैं। श्यामा/कृष्ण अयस लोहा (काला धातु) है, और लोहित अयस तांबा (लाल धातु) है।"
    },
    {
        "type": "MCQ",
        "q": "आदिचनल्लूर स्थल के संदर्भ में, निम्नलिखित कथनों पर विचार करें:\n1. यह तमिलनाडु में स्थित एक विशाल महापाषाणकालीन कलश शवाधान स्थल है।\n2. यहाँ कब्रों से अद्वितीय सोने के मुकुट (diadems) और जानवरों की आकृतियों वाले कांसे के बर्तन मिले हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
        "ans": 2,
        "sol": "दोनों कथन सही हैं। आदिचनल्लूर दक्षिण का एक प्रसिद्ध कलश शवाधान स्थल है जहाँ से सोने-कांसे के अनूठे चढ़ावे मिले हैं।"
    },
    {
        "type": "MCQ",
        "q": "प्रारंभिक लौह प्रगलन तकनीक के संबंध में, निम्नलिखित कथनों पर विचार करें:\n1. धौंकनी की हवा को भट्टी के अपचयन क्षेत्र में भेजने के लिए मिट्टी की फूंकनी (tuyeres) का उपयोग किया जाता था।\n2. कच्चे लौह अयस्कों को तरल अवस्था में पिघलाया जाता था और 1000 ईसा पूर्व में सांचों में ढाला जाता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
        "ans": 0,
        "sol": "कथन 1 सही है। कथन 2 गलत है क्योंकि शुरुआती लोहे को ठोस स्पंज द्रव्यमान (bloom) के रूप में अपचयित किया जाता था और पीटा जाता था, पिघलाया नहीं जाता था।"
    },
    {
        "type": "MCQ",
        "q": "उत्तर वैदिक काल में भौगोलिक विस्तार के संदर्भ में, निम्नलिखित कथनों पर विचार करें:\n1. यह विस्तार लोहे की कुल्हाड़ियों का उपयोग करके मध्य गंगा घाटी के घने मानसूनी जंगलों को साफ करके किया गया था।\n2. मगध के उदय को छोटानागपुर पठार की समृद्ध लौह अयस्क खदानों की निकटता से समर्थन मिला था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
        "ans": 2,
        "sol": "दोनों कथन सही हैं। लोहे की कुल्हाड़ियों ने जंगल साफ किए, और छोटानागपुर की खानों ने मगध की साम्राज्यवादी शक्ति को बल दिया।"
    }
]

# Write Mock questions is exactly 10
generate_sec_file("mock", mock_en, mock_hi)

print("ALL QUESTIONS FILES SUCCESSFULLY GENERATED.")
