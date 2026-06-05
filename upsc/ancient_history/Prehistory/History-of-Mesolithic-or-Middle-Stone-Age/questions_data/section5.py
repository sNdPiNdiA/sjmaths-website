from .helpers import add_mcq, add_multi_mcq, add_tf, add_blank, add_match, add_oneliner, add_ar, add_stmt, add_open

sec5_en = []
sec5_hi = []

# --- 1. MCQ (5 Questions) ---
add_mcq(sec5_en, sec5_hi,
    "Which site in central India is the most celebrated for its Mesolithic rock art, covering over 700 rock shelters?",
    "मध्य भारत में कौन सा स्थल अपनी मध्यपाषाणकालीन शैल कला के लिए सबसे प्रसिद्ध है, जिसमें 700 से अधिक शैल आश्रय शामिल हैं?",
    ["Adamgarh", "Bhimbetka", "Jogimara", "Mirzapur"],
    ["आदमगढ़", "भीमबेटका", "जोगीमारा", "मिर्जापुर"],
    1,
    "Bhimbetka (near Bhopal, MP) is a UNESCO World Heritage Site with over 750 rock shelters, most famous for its Mesolithic paintings.",
    "भीमबेटका (भोपाल के पास, मध्य प्रदेश) एक UNESCO विश्व धरोहर स्थल है जिसमें 750 से अधिक शैल आश्रय हैं, जो अपनी मध्यपाषाणकालीन चित्रकारी के लिए सबसे प्रसिद्ध है।"
)

add_mcq(sec5_en, sec5_hi,
    "Bhimbetka was first systematically investigated and reported as a prehistoric rock art site by which archaeologist?",
    "भीमबेटका को पहली बार किस पुरातत्वविद द्वारा एक प्रागैतिहासिक शैल कला स्थल के रूप में व्यवस्थित रूप से जाँचा गया और रिपोर्ट किया गया था?",
    ["V.N. Misra", "H.D. Sankalia", "V.S. Wakankar", "G.R. Sharma"],
    ["वी.एन. मिश्रा", "एच.डी. सांकलिया", "वी.एस. वाकणकर", "जी.आर. शर्मा"],
    2,
    "V.S. Wakankar (Vishnu Shridhar Wakankar) discovered and documented Bhimbetka in 1957-58 while travelling by train.",
    "वी.एस. वाकणकर (विष्णु श्रीधर वाकणकर) ने 1957-58 में ट्रेन से यात्रा करते हुए भीमबेटका की खोज और दस्तावेजीकरण किया।"
)

add_mcq(sec5_en, sec5_hi,
    "What was the dominant colour used in Mesolithic rock paintings at Bhimbetka?",
    "भीमबेटका में मध्यपाषाणकालीन शैल चित्रों में कौन सा रंग प्रमुख था?",
    ["Black", "White", "Red (haematite/ochre)", "Green"],
    ["काला", "सफेद", "लाल (हेमेटाइट/गेरू)", "हरा"],
    2,
    "Red haematite (iron oxide/ochre) was the most commonly used pigment in Mesolithic rock art at Bhimbetka.",
    "लाल हेमेटाइट (आयरन ऑक्साइड/गेरू) भीमबेटका में मध्यपाषाणकालीन शैल कला में सबसे अधिक इस्तेमाल किया जाने वाला रंगद्रव्य था।"
)

add_mcq(sec5_en, sec5_hi,
    "The rock art at Bhimbetka depicting a honey-gathering scene is significant because it indicates:",
    "भीमबेटका में शहद संग्रह दृश्य को दर्शाने वाली शैल कला महत्वपूर्ण है क्योंकि यह इंगित करती है:",
    ["Religious pilgrimage", "The practice of bee-keeping (apiculture)", "Foraging behaviour and specific subsistence activities", "Agricultural crop cultivation"],
    ["धार्मिक तीर्थयात्रा", "मधुमक्खी पालन (मधुमक्खी पालन)", "संग्रहण व्यवहार और विशिष्ट जीवन निर्वाह गतिविधियाँ", "कृषि फसल की खेती"],
    2,
    "The honey-gathering scene directly shows a subsistence activity and proves wild honey was an important food resource.",
    "शहद संग्रह दृश्य सीधे एक जीवन निर्वाह गतिविधि दिखाता है और साबित करता है कि जंगली शहद एक महत्वपूर्ण खाद्य संसाधन था।"
)

add_mcq(sec5_en, sec5_hi,
    "The rock paintings at Bhimbetka are stylistically similar to which African rock art tradition?",
    "भीमबेटका की शैल चित्रकारी शैलीगत रूप से किस अफ्रीकी शैल कला परंपरा से मिलती-जुलती है?",
    ["Egyptian hieroglyphic art", "San Bushman rock art of Southern Africa", "Saharan Tuareg rock art", "Ethiopian cave paintings"],
    ["मिस्री चित्रलिपि कला", "दक्षिण अफ्रीका की सैन बुशमेन शैल कला", "सहारन तुआरेग शैल कला", "इथियोपियाई गुफा चित्रकारी"],
    1,
    "The San Bushman paintings of southern Africa share remarkably similar themes (hunting, dancing, animals) and execution style with Bhimbetka's Mesolithic art.",
    "दक्षिणी अफ्रीका की सैन बुशमेन चित्रकारी भीमबेटका की मध्यपाषाणकालीन कला के साथ उल्लेखनीय रूप से समान विषयों (शिकार, नृत्य, जानवर) और निष्पादन शैली को साझा करती है।"
)

# --- 2. Multiple Correct MCQ (5 Questions) ---
add_multi_mcq(sec5_en, sec5_hi,
    "Which of the following scenes/themes are depicted in Mesolithic rock art at Bhimbetka? (Select all that apply)",
    "निम्नलिखित में से कौन से दृश्य/विषय भीमबेटका में मध्यपाषाणकालीन शैल कला में चित्रित हैं? (सभी सही विकल्प चुनें)",
    ["Group hunting scenes", "Honey gathering from beehives", "Communal dancing", "Writing of Sanskrit mantras"],
    ["समूह शिकार दृश्य", "छत्ते से शहद इकट्ठा करना", "सामुदायिक नृत्य", "संस्कृत मंत्रों का लेखन"],
    [0, 1, 2],
    "Group hunting, honey gathering, and dancing are documented Bhimbetka themes. Sanskrit writing did not exist in the Mesolithic period.",
    "समूह शिकार, शहद इकट्ठा करना और नृत्य भीमबेटका के दस्तावेजीकृत विषय हैं। संस्कृत लेखन मध्यपाषाण काल में मौजूद नहीं था।"
)

add_multi_mcq(sec5_en, sec5_hi,
    "Which of the following correctly describe the pigments and media used in Bhimbetka rock paintings? (Select all that apply)",
    "निम्नलिखित में से कौन से भीमबेटका शैल चित्रों में उपयोग किए गए रंगद्रव्यों और माध्यमों का सही वर्णन करते हैं? (सभी सही विकल्प चुनें)",
    ["Red haematite (iron oxide)", "White kaolin clay", "Green plant extracts", "Manganese dioxide for black pigment"],
    ["लाल हेमेटाइट (आयरन ऑक्साइड)", "सफेद काओलिन मिट्टी", "हरे पौधे के अर्क", "काले रंगद्रव्य के लिए मैंगनीज डाइऑक्साइड"],
    [0, 1, 3],
    "Red haematite, white kaolin, and black manganese dioxide were all used. Green plant-based pigments have not been documented at Bhimbetka.",
    "लाल हेमेटाइट, सफेद काओलिन और काला मैंगनीज डाइऑक्साइड सभी उपयोग किए जाते थे। भीमबेटका में हरे पौधे-आधारित रंगद्रव्य दस्तावेजीकृत नहीं हैं।"
)

add_multi_mcq(sec5_en, sec5_hi,
    "What does the presence of communal dancing scenes in Bhimbetka rock art suggest about Mesolithic society? (Select all that apply)",
    "भीमबेटका शैल कला में सामुदायिक नृत्य दृश्यों की उपस्थिति मध्यपाषाणकालीन समाज के बारे में क्या सुझाव देती है? (सभी सही विकल्प चुनें)",
    ["Existence of organised group activities and ritual celebrations", "Some form of artistic expression and aesthetic sensibility", "Shared cultural identity and social cohesion", "Evidence of formal written law codes"],
    ["संगठित सामूहिक गतिविधियों और अनुष्ठान उत्सवों का अस्तित्व", "कुछ प्रकार की कलात्मक अभिव्यक्ति और सौंदर्यबोध", "साझा सांस्कृतिक पहचान और सामाजिक एकजुटता", "औपचारिक लिखित कानून संहिताओं का साक्ष्य"],
    [0, 1, 2],
    "Dancing scenes reflect ritual, aesthetics, and social cohesion. Written law codes are impossible in the pre-literate Mesolithic.",
    "नृत्य दृश्य अनुष्ठान, सौंदर्यशास्त्र और सामाजिक एकजुटता को दर्शाते हैं। लिखित कानून संहिताएं पूर्व-साक्षर मध्यपाषाण काल में असंभव हैं।"
)

add_multi_mcq(sec5_en, sec5_hi,
    "Which of the following are features of Bhimbetka that led to its designation as a UNESCO World Heritage Site? (Select all that apply)",
    "निम्नलिखित में से कौन सी भीमबेटका की विशेषताएं हैं जिनके कारण इसे UNESCO विश्व धरोहर स्थल का दर्जा दिया गया? (सभी सही विकल्प चुनें)",
    ["Presence of over 700 rock shelters with prehistoric paintings", "Continuous sequence of art from Paleolithic through Mesolithic to historical times", "The largest Mesolithic burial site in India", "Evidence of ancient hominid occupation predating modern Homo sapiens"],
    ["प्रागैतिहासिक चित्रकारी के साथ 700 से अधिक शैल आश्रयों की उपस्थिति", "पुरापाषाण से मध्यपाषाण से ऐतिहासिक काल तक कला की निरंतर अनुक्रम", "भारत में सबसे बड़ा मध्यपाषाणकालीन शवाधान स्थल", "आधुनिक होमो सेपियन्स से पहले प्राचीन होमिनिड बस्ती का साक्ष्य"],
    [0, 1],
    "UNESCO cited the number of shelters and the continuous art sequence. Bhimbetka is not a burial site (that is Damdama). Hominid occupation predating sapiens has not been confirmed at Bhimbetka.",
    "UNESCO ने आश्रयों की संख्या और निरंतर कला अनुक्रम का हवाला दिया। भीमबेटका एक शवाधान स्थल नहीं है (वह दमदमा है)।"
)

add_multi_mcq(sec5_en, sec5_hi,
    "Which of the following correctly describe the rock art technique used by Mesolithic artists at Bhimbetka? (Select all that apply)",
    "निम्नलिखित में से कौन से भीमबेटका में मध्यपाषाणकालीन कलाकारों द्वारा उपयोग की गई शैल कला तकनीक का सही वर्णन करते हैं? (सभी सही विकल्प चुनें)",
    ["Painted images using mineral pigments mixed with water or plant adhesives", "Engraved (incised) lines on rock surfaces", "Three-dimensional sculptures carved from rock", "Silhouette figures using flat colour fills"],
    ["पानी या पौधे के चिपकने वाले पदार्थों के साथ मिश्रित खनिज रंगद्रव्यों का उपयोग करके चित्रित छवियाँ", "चट्टान की सतहों पर उत्कीर्ण (incised) रेखाएं", "चट्टान से तराशी गई त्रि-आयामी मूर्तियाँ", "सपाट रंग भरने वाले सिल्हूट आकृतियाँ"],
    [0, 1, 3],
    "Painting with mineral pigments, engraving lines, and silhouette technique are all documented. Three-dimensional rock carving was not a Mesolithic technique.",
    "खनिज रंगद्रव्यों से चित्रकारी, रेखाएं उत्कीर्ण करना और सिल्हूट तकनीक सभी दस्तावेजीकृत हैं। त्रि-आयामी शैल नक्काशी मध्यपाषाणकालीन तकनीक नहीं थी।"
)

# --- 3. True/False (8 Questions) ---
add_tf(sec5_en, sec5_hi,
    "Bhimbetka is located in Madhya Pradesh and is a UNESCO World Heritage Site.",
    "भीमबेटका मध्य प्रदेश में स्थित है और एक UNESCO विश्व धरोहर स्थल है।",
    True,
    "Bhimbetka is situated near Bhopal in Madhya Pradesh and was inscribed as a UNESCO World Heritage Site in 2003.",
    "भीमबेटका मध्य प्रदेश में भोपाल के पास स्थित है और 2003 में UNESCO विश्व धरोहर स्थल के रूप में नामांकित किया गया था।"
)

add_tf(sec5_en, sec5_hi,
    "V.S. Wakankar discovered Bhimbetka in 1957-58 while travelling by train.",
    "वी.एस. वाकणकर ने 1957-58 में ट्रेन से यात्रा करते हुए भीमबेटका की खोज की।",
    True,
    "Wakankar noticed the Vindhyan sandstone escarpments from the train and investigated them, discovering the rock shelters.",
    "वाकणकर ने ट्रेन से विंध्यन बलुआ पत्थर की चट्टानों को देखा और उनकी जाँच की, जिससे शैल आश्रयों की खोज हुई।"
)

add_tf(sec5_en, sec5_hi,
    "Mesolithic rock art at Bhimbetka primarily depicts agricultural scenes of crop sowing and harvesting.",
    "भीमबेटका में मध्यपाषाणकालीन शैल कला मुख्य रूप से फसल बोने और कटाई के कृषि दृश्यों को दर्शाती है।",
    False,
    "Bhimbetka's Mesolithic art shows hunting, dancing, honey gathering, and animal figures — not farming scenes which belong to the later Neolithic.",
    "भीमबेटका की मध्यपाषाणकालीन कला शिकार, नृत्य, शहद इकट्ठा करना और जानवरों की आकृतियाँ दिखाती है — खेती के दृश्य नहीं जो बाद के नवपाषाण काल के हैं।"
)

add_tf(sec5_en, sec5_hi,
    "Red haematite (iron oxide) was the dominant pigment used in Bhimbetka Mesolithic rock paintings.",
    "लाल हेमेटाइट (आयरन ऑक्साइड) भीमबेटका मध्यपाषाणकालीन शैल चित्रों में उपयोग किया जाने वाला प्रमुख रंगद्रव्य था।",
    True,
    "Red ochre/haematite was the most widely available and durable mineral pigment, used extensively at Bhimbetka.",
    "लाल गेरू/हेमेटाइट सबसे व्यापक रूप से उपलब्ध और टिकाऊ खनिज रंगद्रव्य था, जिसका भीमबेटका में व्यापक उपयोग किया गया।"
)

add_tf(sec5_en, sec5_hi,
    "The rock art at Bhimbetka shows only Mesolithic-period paintings, with no older or newer layers.",
    "भीमबेटका की शैल कला केवल मध्यपाषाणकालीन चित्रकारी दिखाती है, कोई पुरानी या नई परतें नहीं हैं।",
    False,
    "Bhimbetka has multiple artistic layers from Paleolithic to historical periods. The Mesolithic paintings are the most famous but are overlain by later additions.",
    "भीमबेटका में पुरापाषाण से ऐतिहासिक काल तक की कई कलात्मक परतें हैं। मध्यपाषाणकालीन चित्रकारी सबसे प्रसिद्ध है लेकिन बाद में जोड़ी गई चीजों से ढकी हुई है।"
)

add_tf(sec5_en, sec5_hi,
    "Honey gathering was depicted in Mesolithic rock art, providing evidence of an important subsistence activity.",
    "शहद इकट्ठा करना मध्यपाषाणकालीन शैल कला में दर्शाया गया था, जो एक महत्वपूर्ण जीवन निर्वाह गतिविधि का साक्ष्य प्रदान करता है।",
    True,
    "Honey gathering scenes at Bhimbetka and other sites confirm wild honey was a major food supplement for Mesolithic communities.",
    "भीमबेटका और अन्य स्थलों पर शहद इकट्ठा करने के दृश्य पुष्टि करते हैं कि जंगली शहद मध्यपाषाणकालीन समुदायों के लिए एक प्रमुख खाद्य पूरक था।"
)

add_tf(sec5_en, sec5_hi,
    "Mesolithic rock paintings at Bhimbetka were made using synthetic chemical dyes.",
    "भीमबेटका में मध्यपाषाणकालीन शैल चित्र सिंथेटिक रासायनिक रंगों का उपयोग करके बनाए गए थे।",
    False,
    "All Mesolithic pigments were natural minerals — red haematite, white kaolin, black manganese dioxide — mixed with water, fat, or plant adhesives.",
    "सभी मध्यपाषाणकालीन रंगद्रव्य प्राकृतिक खनिज थे — लाल हेमेटाइट, सफेद काओलिन, काला मैंगनीज डाइऑक्साइड — पानी, वसा या पौधे के चिपकने वाले पदार्थ के साथ मिश्रित।"
)

add_tf(sec5_en, sec5_hi,
    "The dancing figures in Bhimbetka rock art represent the earliest evidence of human aesthetic expression and communal ritual in India.",
    "भीमबेटका शैल कला में नृत्य करती आकृतियाँ भारत में मानव सौंदर्य अभिव्यक्ति और सामुदायिक अनुष्ठान का सबसे पहला साक्ष्य प्रस्तुत करती हैं।",
    True,
    "The dancing and hunting scenes at Bhimbetka are India's earliest documented evidence of complex ritual, aesthetic, and social behaviours.",
    "भीमबेटका में नृत्य और शिकार दृश्य भारत में जटिल अनुष्ठान, सौंदर्य और सामाजिक व्यवहारों का सबसे पहले दस्तावेजीकृत साक्ष्य हैं।"
)

# --- 4. Fill in the Blank (8 Questions) ---
add_blank(sec5_en, sec5_hi,
    "Bhimbetka rock shelters are located near ________, Madhya Pradesh.",
    "भीमबेटका शैल आश्रय मध्य प्रदेश में ________ के पास स्थित हैं।",
    "Bhopal", "भोपाल",
    "Bhimbetka is in the Raisen district, about 45 km south-east of Bhopal.",
    "भीमबेटका रायसेन जिले में है, भोपाल से लगभग 45 किमी दक्षिण-पूर्व में।"
)

add_blank(sec5_en, sec5_hi,
    "Bhimbetka was discovered and reported by ________ in 1957-58.",
    "भीमबेटका की खोज और रिपोर्ट ________ ने 1957-58 में की थी।",
    "V.S. Wakankar", "वी.एस. वाकणकर",
    "V.S. Wakankar of Vikram University, Ujjain, made the landmark discovery of Bhimbetka's prehistoric art.",
    "उज्जैन के विक्रम विश्वविद्यालय के वी.एस. वाकणकर ने भीमबेटका की प्रागैतिहासिक कला की ऐतिहासिक खोज की।"
)

add_blank(sec5_en, sec5_hi,
    "The dominant mineral pigment used in Mesolithic rock art at Bhimbetka is ________ (iron oxide).",
    "भीमबेटका में मध्यपाषाणकालीन शैल कला में उपयोग किया जाने वाला प्रमुख खनिज रंगद्रव्य ________ (आयरन ऑक्साइड) है।",
    "haematite", "हेमेटाइट",
    "Red haematite is the most durable natural pigment and survives thousands of years on protected rock surfaces.",
    "लाल हेमेटाइट सबसे टिकाऊ प्राकृतिक रंगद्रव्य है और संरक्षित चट्टानी सतहों पर हजारों वर्षों तक जीवित रहता है।"
)

add_blank(sec5_en, sec5_hi,
    "Bhimbetka was inscribed as a UNESCO World Heritage Site in the year ________.",
    "भीमबेटका को ________ वर्ष में UNESCO विश्व धरोहर स्थल के रूप में नामांकित किया गया था।",
    "2003", "2003",
    "Bhimbetka was inscribed by UNESCO in 2003 for its outstanding universal value as a prehistoric rock art site.",
    "भीमबेटका को एक प्रागैतिहासिक शैल कला स्थल के रूप में अपने उत्कृष्ट सार्वभौमिक मूल्य के लिए 2003 में UNESCO द्वारा नामांकित किया गया था।"
)

add_blank(sec5_en, sec5_hi,
    "The Bhimbetka paintings show a continuous sequence of art from the ________ period through to historical times.",
    "भीमबेटका चित्रकारी ________ काल से ऐतिहासिक काल तक कला की एक निरंतर अनुक्रम दिखाती है।",
    "Paleolithic", "पुरापाषाण",
    "The oldest Bhimbetka paintings may date to the Upper Paleolithic; the most numerous and vivid belong to the Mesolithic period.",
    "सबसे पुरानी भीमबेटका चित्रकारी उच्च पुरापाषाण काल की हो सकती है; सबसे अधिक संख्या में और जीवंत चित्र मध्यपाषाण काल के हैं।"
)

add_blank(sec5_en, sec5_hi,
    "The rock art depicting humans climbing a tree to reach a beehive shows the ________ subsistence practice.",
    "शहद के छत्ते तक पहुँचने के लिए पेड़ पर चढ़ते इंसानों को दर्शाने वाली शैल कला ________ जीवन निर्वाह प्रथा दिखाती है।",
    "honey gathering", "शहद इकट्ठा करना",
    "Honey-gathering scenes show the use of wild forest resources as part of the Mesolithic broad-spectrum economy.",
    "शहद इकट्ठा करने के दृश्य मध्यपाषाणकालीन व्यापक-स्पेक्ट्रम अर्थव्यवस्था के हिस्से के रूप में जंगली वन संसाधनों का उपयोग दिखाते हैं।"
)

add_blank(sec5_en, sec5_hi,
    "Bhimbetka has over ________ rock shelters with prehistoric paintings.",
    "भीमबेटका में प्रागैतिहासिक चित्रकारी के साथ ________ से अधिक शैल आश्रय हैं।",
    "700", "700",
    "Over 750 shelters have been identified at Bhimbetka, of which about 500 contain paintings.",
    "भीमबेटका में 750 से अधिक आश्रयों की पहचान की गई है, जिनमें से लगभग 500 में चित्रकारी है।"
)

add_blank(sec5_en, sec5_hi,
    "Rock art that depicts daily life, subsistence, and ritual behaviour of prehistoric humans is called ________ art.",
    "प्रागैतिहासिक मनुष्यों के दैनिक जीवन, जीवन निर्वाह और अनुष्ठान व्यवहार को दर्शाने वाली शैल कला को ________ कला कहा जाता है।",
    "parietal", "पार्श्विक (गुफा/शैल)",
    "Parietal art refers to prehistoric paintings and engravings on rock surfaces, walls, and cave ceilings.",
    "पार्श्विक कला चट्टान की सतहों, दीवारों और गुफा की छतों पर प्रागैतिहासिक चित्रों और नक्काशी को संदर्भित करती है।"
)

# --- 5. Match the Following (3 Questions) ---
add_match(sec5_en, sec5_hi,
    "Match the Bhimbetka rock art scene with its significance:",
    "भीमबेटका शैल कला दृश्य को उसके महत्व से सुमेलित करें:",
    ["1. Group hunting scene", "2. Honey-gathering scene", "3. Communal dancing scene"],
    ["1. समूह शिकार दृश्य", "2. शहद इकट्ठा करने का दृश्य", "3. सामुदायिक नृत्य दृश्य"],
    ["A. Shows cooperative social behaviour and organised group activity", "B. Proves wild honey was a key food resource in foraging economy", "C. Indicates ritual, aesthetic expression, and social bonding"],
    ["A. सहकारी सामाजिक व्यवहार और संगठित सामूहिक गतिविधि दिखाता है", "B. साबित करता है कि जंगली शहद भोजन संग्रह अर्थव्यवस्था में एक प्रमुख खाद्य संसाधन था", "C. अनुष्ठान, सौंदर्य अभिव्यक्ति और सामाजिक बंधन को इंगित करता है"],
    "1-A, 2-B, 3-C.",
    "1-A, 2-B, 3-C."
)

add_match(sec5_en, sec5_hi,
    "Match the pigment colour used in Bhimbetka with its mineral source:",
    "भीमबेटका में उपयोग किए गए रंगद्रव्य रंग को उसके खनिज स्रोत से सुमेलित करें:",
    ["1. Red", "2. Black", "3. White"],
    ["1. लाल", "2. काला", "3. सफेद"],
    ["A. Haematite (iron oxide)", "B. Manganese dioxide", "C. Kaolin clay or calcite"],
    ["A. हेमेटाइट (आयरन ऑक्साइड)", "B. मैंगनीज डाइऑक्साइड", "C. काओलिन मिट्टी या कैल्साइट"],
    "1-A, 2-B, 3-C.",
    "1-A, 2-B, 3-C."
)

add_match(sec5_en, sec5_hi,
    "Match the rock art site with its state/region:",
    "शैल कला स्थल को उसके राज्य/क्षेत्र से सुमेलित करें:",
    ["1. Bhimbetka", "2. Adamgarh", "3. Mirzapur"],
    ["1. भीमबेटका", "2. आदमगढ़", "3. मिर्जापुर"],
    ["A. Madhya Pradesh (near Bhopal)", "B. Madhya Pradesh (Hoshangabad)", "C. Uttar Pradesh (Vindhyan hills)"],
    ["A. मध्य प्रदेश (भोपाल के पास)", "B. मध्य प्रदेश (होशंगाबाद)", "C. उत्तर प्रदेश (विंध्यन पहाड़ियाँ)"],
    "1-A, 2-B, 3-C.",
    "1-A, 2-B, 3-C."
)

# --- 6. One-Liner (8 Questions) ---
add_oneliner(sec5_en, sec5_hi,
    "Who discovered Bhimbetka as a prehistoric rock art site?",
    "किसने भीमबेटका को एक प्रागैतिहासिक शैल कला स्थल के रूप में खोजा?",
    "V.S. Wakankar (Vishnu Shridhar Wakankar) in 1957-58.",
    "वी.एस. वाकणकर (विष्णु श्रीधर वाकणकर) ने 1957-58 में।"
)

add_oneliner(sec5_en, sec5_hi,
    "In which state is Bhimbetka located, and when was it inscribed as a UNESCO World Heritage Site?",
    "भीमबेटका किस राज्य में स्थित है, और इसे कब UNESCO विश्व धरोहर स्थल के रूप में नामांकित किया गया था?",
    "Madhya Pradesh; inscribed in 2003.",
    "मध्य प्रदेश; 2003 में नामांकित।"
)

add_oneliner(sec5_en, sec5_hi,
    "What is the dominant colour/pigment in Bhimbetka Mesolithic paintings?",
    "भीमबेटका मध्यपाषाणकालीन चित्रों में प्रमुख रंग/रंगद्रव्य क्या है?",
    "Red haematite (iron oxide/ochre).",
    "लाल हेमेटाइट (आयरन ऑक्साइड/गेरू)।"
)

add_oneliner(sec5_en, sec5_hi,
    "Name three themes depicted in Bhimbetka Mesolithic rock art.",
    "भीमबेटका मध्यपाषाणकालीन शैल कला में चित्रित तीन विषयों के नाम बताएं।",
    "Group hunting, honey gathering, and communal dancing.",
    "समूह शिकार, शहद इकट्ठा करना और सामुदायिक नृत्य।"
)

add_oneliner(sec5_en, sec5_hi,
    "Approximately how many rock shelters does Bhimbetka have?",
    "भीमबेटका में लगभग कितने शैल आश्रय हैं?",
    "Over 750 rock shelters (about 500 contain paintings).",
    "750 से अधिक शैल आश्रय (लगभग 500 में चित्रकारी है)।"
)

add_oneliner(sec5_en, sec5_hi,
    "What does the honey-gathering scene in Bhimbetka prove about Mesolithic diet?",
    "भीमबेटका में शहद इकट्ठा करने का दृश्य मध्यपाषाणकालीन आहार के बारे में क्या साबित करता है?",
    "Wild honey was an important high-energy food supplement in the Mesolithic broad-spectrum economy.",
    "जंगली शहद मध्यपाषाणकालीन व्यापक-स्पेक्ट्रम अर्थव्यवस्था में एक महत्वपूर्ण उच्च-ऊर्जा खाद्य पूरक था।"
)

add_oneliner(sec5_en, sec5_hi,
    "What do the dancing scenes in Bhimbetka suggest about Mesolithic social life?",
    "भीमबेटका में नृत्य दृश्य मध्यपाषाणकालीन सामाजिक जीवन के बारे में क्या सुझाव देते हैं?",
    "They indicate communal rituals, shared cultural identity, and the emergence of aesthetic expression.",
    "वे सामुदायिक अनुष्ठान, साझा सांस्कृतिक पहचान और सौंदर्य अभिव्यक्ति के उदय को इंगित करते हैं।"
)

add_oneliner(sec5_en, sec5_hi,
    "What is the artistic significance of Bhimbetka in the context of world prehistory?",
    "विश्व प्रागैतिहास के संदर्भ में भीमबेटका का कलात्मक महत्व क्या है?",
    "It is one of the oldest and largest concentrations of rock art in the world, showing cultural complexity of prehistoric Homo sapiens in South Asia.",
    "यह दुनिया में शैल कला के सबसे पुराने और सबसे बड़े संकेंद्रणों में से एक है, जो दक्षिण एशिया में प्रागैतिहासिक होमो सेपियन्स की सांस्कृतिक जटिलता दिखाता है।"
)

# --- 7. Assertion-Reason (8 Questions) ---
add_ar(sec5_en, sec5_hi,
    "Assertion (A): Bhimbetka is considered the most important Mesolithic rock art site in India.\nReason (R): It has the largest concentration of prehistoric rock shelters in the world, with continuous painting traditions from Paleolithic to historical times.",
    "कथन (A): भीमबेटका को भारत का सबसे महत्वपूर्ण मध्यपाषाणकालीन शैल कला स्थल माना जाता है।\nकारण (R): इसमें दुनिया में प्रागैतिहासिक शैल आश्रयों की सबसे बड़ी सघनता है, जिसमें पुरापाषाण से ऐतिहासिक काल तक की निरंतर चित्रकारी परंपराएं हैं।",
    0,
    "Both A and R are true, and R explains the multi-temporal, richly documented nature of Bhimbetka.",
    "A और R दोनों सही हैं, और R भीमबेटका की बहु-कालीन, समृद्ध रूप से दस्तावेजीकृत प्रकृति की व्याख्या करता है।"
)

add_ar(sec5_en, sec5_hi,
    "Assertion (A): The red haematite pigment has survived for thousands of years at Bhimbetka.\nReason (R): Haematite is chemically stable (iron oxide) and does not react with moisture or UV radiation, making it highly durable on rock surfaces.",
    "कथन (A): लाल हेमेटाइट रंगद्रव्य भीमबेटका में हजारों वर्षों तक जीवित रहा है।\nकारण (R): हेमेटाइट रासायनिक रूप से स्थिर (आयरन ऑक्साइड) है और नमी या UV विकिरण के साथ प्रतिक्रिया नहीं करता है, जिससे यह चट्टानी सतहों पर अत्यधिक टिकाऊ हो जाता है।",
    0,
    "Both are true. The chemical stability of iron oxides is the key reason ancient pigments survive.",
    "दोनों सही हैं। आयरन ऑक्साइड की रासायनिक स्थिरता प्राचीन रंगद्रव्यों के जीवित रहने का प्रमुख कारण है।"
)

add_ar(sec5_en, sec5_hi,
    "Assertion (A): The group hunting scenes at Bhimbetka indicate that Mesolithic hunting was a collaborative, socially coordinated activity.\nReason (R): No Mesolithic community could organise cooperative hunting without a sophisticated language system.",
    "कथन (A): भीमबेटका में समूह शिकार दृश्य इंगित करते हैं कि मध्यपाषाणकालीन शिकार एक सहयोगी, सामाजिक रूप से समन्वित गतिविधि थी।\nकारण (R): कोई भी मध्यपाषाणकालीन समुदाय एक परिष्कृत भाषा प्रणाली के बिना सहकारी शिकार का आयोजन नहीं कर सकता था।",
    1,
    "A is true — group hunting is shown. R is separately true (language was certainly developed) but is not the reason directly cited by archaeologists — they use the visual evidence of coordination to infer social behaviour.",
    "A सही है — समूह शिकार दिखाया गया है। R अलग से सही है (भाषा निश्चित रूप से विकसित थी) लेकिन पुरातत्वविदों द्वारा सीधे उद्धृत कारण नहीं है — वे सामाजिक व्यवहार अनुमान लगाने के लिए समन्वय के दृश्य साक्ष्य का उपयोग करते हैं।"
)

add_ar(sec5_en, sec5_hi,
    "Assertion (A): Bhimbetka rock art was produced exclusively by male hunters.\nReason (R): Archaeological evidence shows that hunting was exclusively a male activity in prehistoric societies.",
    "कथन (A): भीमबेटका शैल कला विशेष रूप से पुरुष शिकारियों द्वारा बनाई गई थी।\nकारण (R): पुरातात्विक साक्ष्य दिखाता है कि प्रागैतिहासिक समाजों में शिकार विशेष रूप से एक पुरुष गतिविधि थी।",
    3,
    "Both A and R are false. We cannot determine the gender of the artists from rock art. Modern anthropology has shown women also participated in hunting in many hunter-gatherer societies.",
    "A और R दोनों गलत हैं। हम शैल कला से कलाकारों का लिंग निर्धारित नहीं कर सकते। आधुनिक मानवशास्त्र ने दिखाया है कि कई शिकारी-संग्रहकर्ता समाजों में महिलाओं ने भी शिकार में भाग लिया।"
)

add_ar(sec5_en, sec5_hi,
    "Assertion (A): V.S. Wakankar's discovery of Bhimbetka revolutionised the understanding of Indian prehistoric art.\nReason (R): Before Bhimbetka, archaeologists believed India had no significant tradition of prehistoric rock art.",
    "कथन (A): वी.एस. वाकणकर की भीमबेटका की खोज ने भारतीय प्रागैतिहासिक कला की समझ में क्रांति ला दी।\nकारण (R): भीमबेटका से पहले, पुरातत्वविदों का मानना था कि भारत में प्रागैतिहासिक शैल कला की कोई महत्वपूर्ण परंपरा नहीं है।",
    0,
    "Both are true. Bhimbetka fundamentally changed the perception of Indian prehistoric cultural capabilities.",
    "दोनों सही हैं। भीमबेटका ने भारतीय प्रागैतिहासिक सांस्कृतिक क्षमताओं की धारणा को मौलिक रूप से बदल दिया।"
)

add_ar(sec5_en, sec5_hi,
    "Assertion (A): Bhimbetka art only depicts animals, with no human figures.\nReason (R): Mesolithic humans lacked the cognitive ability to represent themselves in symbolic art.",
    "कथन (A): भीमबेटका कला केवल जानवरों को दर्शाती है, कोई मानव आकृतियाँ नहीं हैं।\nकारण (R): मध्यपाषाणकालीन मनुष्यों में खुद को प्रतीकात्मक कला में प्रस्तुत करने की संज्ञानात्मक क्षमता नहीं थी।",
    3,
    "Both A and R are false. Bhimbetka has abundant human figures — hunters, dancers, honey-gatherers. And Mesolithic humans had fully modern Homo sapiens cognition.",
    "A और R दोनों गलत हैं। भीमबेटका में प्रचुर मानव आकृतियाँ हैं — शिकारी, नृत्यकर्ता, शहद इकट्ठा करने वाले। और मध्यपाषाणकालीन मनुष्यों में पूरी तरह से आधुनिक होमो सेपियन्स की संज्ञान क्षमता थी।"
)

add_ar(sec5_en, sec5_hi,
    "Assertion (A): The communal dancing scenes at Bhimbetka indicate the existence of social rituals and shared cultural beliefs.\nReason (R): Dancing in hunter-gatherer societies is documented as a mechanism for social bonding, ritual preparation, and collective identity formation.",
    "कथन (A): भीमबेटका में सामुदायिक नृत्य दृश्य सामाजिक अनुष्ठानों और साझा सांस्कृतिक विश्वासों के अस्तित्व को इंगित करते हैं।\nकारण (R): शिकारी-संग्रहकर्ता समाजों में नृत्य को सामाजिक बंधन, अनुष्ठान की तैयारी और सामूहिक पहचान निर्माण के लिए एक तंत्र के रूप में दस्तावेजीकृत किया गया है।",
    0,
    "Both A and R are true, and R provides the anthropological basis for interpreting the dancing scenes.",
    "A और R दोनों सही हैं, और R नृत्य दृश्यों की व्याख्या के लिए मानवशास्त्रीय आधार प्रदान करता है।"
)

add_ar(sec5_en, sec5_hi,
    "Assertion (A): The Bhimbetka paintings have survived for thousands of years due to the protective overhang of the rock shelters.\nReason (R): The overhanging rock prevented direct rainfall, UV radiation, and extreme temperature fluctuations from degrading the pigments.",
    "कथन (A): भीमबेटका चित्रकारी शैल आश्रयों के सुरक्षात्मक ओवरहैंग के कारण हजारों वर्षों तक जीवित रही है।\nकारण (R): ओवरहैंगिंग चट्टान ने सीधी बारिश, UV विकिरण और अत्यधिक तापमान उतार-चढ़ाव को रंगद्रव्यों को खराब करने से रोका।",
    0,
    "Both A and R are true. The sheltering function of rock overhangs is the primary conservation mechanism for ancient rock art worldwide.",
    "A और R दोनों सही हैं। शैल ओवरहैंग का आश्रय कार्य दुनिया भर में प्राचीन शैल कला के लिए प्राथमिक संरक्षण तंत्र है।"
)

# --- 8. Statement-Based (5 Questions) ---
add_stmt(sec5_en, sec5_hi,
    "Consider the following statements about Bhimbetka:\n1. It was discovered and reported by V.S. Wakankar in 1957-58.\n2. It has over 700 rock shelters and was inscribed as a UNESCO World Heritage Site in 2003.\nWhich of the statements given above is/are correct?",
    "भीमबेटका के बारे में निम्नलिखित कथनों पर विचार करें:\n1. इसकी खोज और रिपोर्ट वी.एस. वाकणकर ने 1957-58 में की थी।\n2. इसमें 700 से अधिक शैल आश्रय हैं और इसे 2003 में UNESCO विश्व धरोहर स्थल के रूप में नामांकित किया गया था।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
    2,
    "Both statements are correct — Wakankar discovered Bhimbetka in 1957-58 and it was inscribed by UNESCO in 2003.",
    "दोनों कथन सही हैं — वाकणकर ने 1957-58 में भीमबेटका की खोज की और 2003 में UNESCO द्वारा नामांकित किया गया।"
)

add_stmt(sec5_en, sec5_hi,
    "Consider the following statements about Bhimbetka rock art themes:\n1. Group hunting scenes depict coordinated social behaviour.\n2. Honey-gathering scenes prove that agriculture was practised by Mesolithic communities.\nWhich of the statements given above is/are correct?",
    "भीमबेटका शैल कला विषयों के बारे में निम्नलिखित कथनों पर विचार करें:\n1. समूह शिकार दृश्य समन्वित सामाजिक व्यवहार को दर्शाते हैं।\n2. शहद इकट्ठा करने के दृश्य साबित करते हैं कि मध्यपाषाणकालीन समुदायों द्वारा कृषि का अभ्यास किया जाता था।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
    0,
    "Statement 1 is correct. Statement 2 is incorrect — honey gathering is a foraging activity, not agriculture.",
    "कथन 1 सही है। कथन 2 गलत है — शहद इकट्ठा करना एक भोजन संग्रह गतिविधि है, कृषि नहीं।"
)

add_stmt(sec5_en, sec5_hi,
    "Consider the following pairs:\nPigment colour : Mineral source\n1. Red : Haematite\n2. Black : Manganese dioxide\n3. White : Copper sulphate\nHow many pairs are correctly matched?",
    "निम्नलिखित युग्मों पर विचार करें:\nरंगद्रव्य रंग : खनिज स्रोत\n1. लाल : हेमेटाइट\n2. काला : मैंगनीज डाइऑक्साइड\n3. सफेद : कॉपर सल्फेट\nकितने युग्म सही सुमेलित हैं?",
    ["Only one", "Only two", "All three", "None"],
    ["केवल एक", "केवल दो", "सभी तीन", "कोई नहीं"],
    1,
    "Pairs 1 and 2 are correct. Pair 3 is incorrect — white was from kaolin clay or calcite, not copper sulphate.",
    "युग्म 1 और 2 सही हैं। युग्म 3 गलत है — सफेद काओलिन मिट्टी या कैल्साइट से था, कॉपर सल्फेट से नहीं।"
)

add_stmt(sec5_en, sec5_hi,
    "Consider the following statements about Bhimbetka's artistic tradition:\n1. The paintings span multiple prehistoric periods, from Paleolithic through Mesolithic to historical times.\n2. All paintings at Bhimbetka were made in a single cultural phase by the same group of artists.\nWhich of the statements given above is/are correct?",
    "भीमबेटका की कलात्मक परंपरा के बारे में निम्नलिखित कथनों पर विचार करें:\n1. चित्रकारी कई प्रागैतिहासिक कालों में फैली हुई है, पुरापाषाण से मध्यपाषाण से ऐतिहासिक काल तक।\n2. भीमबेटका की सभी चित्रकारी एक ही सांस्कृतिक चरण में कलाकारों के एक ही समूह द्वारा बनाई गई थी।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
    0,
    "Statement 1 is correct. Statement 2 is incorrect — the paintings span multiple phases by different communities over thousands of years.",
    "कथन 1 सही है। कथन 2 गलत है — चित्रकारी हजारों वर्षों में विभिन्न समुदायों द्वारा कई चरणों में फैली हुई है।"
)

add_stmt(sec5_en, sec5_hi,
    "Consider the following statements about Bhimbetka's significance:\n1. It provides the oldest evidence of agriculture in India.\n2. It demonstrates cultural continuity of human habitation in the Indian subcontinent from prehistoric times.\nWhich of the statements given above is/are correct?",
    "भीमबेटका के महत्व के बारे में निम्नलिखित कथनों पर विचार करें:\n1. यह भारत में कृषि का सबसे पुराना साक्ष्य प्रदान करता है।\n2. यह प्रागैतिहासिक काल से भारतीय उपमहाद्वीप में मानव बस्ती की सांस्कृतिक निरंतरता को प्रदर्शित करता है।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
    1,
    "Statement 1 is incorrect — Bhimbetka is a rock art site, not an agricultural site. Statement 2 is correct — it proves long cultural continuity.",
    "कथन 1 गलत है — भीमबेटका एक शैल कला स्थल है, कृषि स्थल नहीं। कथन 2 सही है — यह लंबी सांस्कृतिक निरंतरता साबित करता है।"
)

# --- 9. Why (3 Questions) ---
add_open(sec5_en, sec5_hi, "Why",
    "Why was Bhimbetka inscribed as a UNESCO World Heritage Site in 2003?",
    "भीमबेटका को 2003 में UNESCO विश्व धरोहर स्थल के रूप में क्यों नामांकित किया गया था?",
    "UNESCO recognised Bhimbetka for its Outstanding Universal Value in two areas: (1) It contains the world's largest concentration of prehistoric rock shelters in a single contiguous area, demonstrating a profound understanding of early human cultural capabilities. (2) The paintings show an unbroken artistic tradition spanning the Paleolithic, Mesolithic, Chalcolithic, and early historical periods — a globally rare multi-period art sequence.",
    "UNESCO ने दो क्षेत्रों में भीमबेटका की उत्कृष्ट सार्वभौमिक मूल्य को मान्यता दी: (1) इसमें एक ही सन्निहित क्षेत्र में दुनिया की सबसे बड़ी प्रागैतिहासिक शैल आश्रयों की सघनता है। (2) चित्रकारी पुरापाषाण, मध्यपाषाण, ताम्रपाषाण और प्रारंभिक ऐतिहासिक काल में फैली एक निर्बाध कलात्मक परंपरा दिखाती है।"
)

add_open(sec5_en, sec5_hi, "Why",
    "Why did Mesolithic artists use mineral pigments rather than organic dyes?",
    "मध्यपाषाणकालीन कलाकारों ने जैविक रंगों की बजाय खनिज रंगद्रव्यों का उपयोग क्यों किया?",
    "Mineral pigments like haematite, manganese dioxide, and kaolin are chemically stable and do not decompose over time. Organic dyes (from plants or animals) degrade rapidly when exposed to moisture, bacteria, and UV light. On protected rock surfaces, mineral pigments can survive for tens of thousands of years, which is why Bhimbetka paintings still exist today.",
    "हेमेटाइट, मैंगनीज डाइऑक्साइड और काओलिन जैसे खनिज रंगद्रव्य रासायनिक रूप से स्थिर होते हैं और समय के साथ विघटित नहीं होते। जैविक रंग (पौधों या जानवरों से) नमी, बैक्टीरिया और UV प्रकाश के संपर्क में आने पर तेजी से ख़राब हो जाते हैं। संरक्षित चट्टानी सतहों पर, खनिज रंगद्रव्य दसों हजार वर्षों तक जीवित रह सकते हैं, यही कारण है कि भीमबेटका के चित्र आज भी मौजूद हैं।"
)

add_open(sec5_en, sec5_hi, "Why",
    "Why are the rock art scenes at Bhimbetka considered more reliable evidence of Mesolithic life than written accounts?",
    "भीमबेटका की शैल कला के दृश्यों को लिखित विवरणों की तुलना में मध्यपाषाणकालीन जीवन का अधिक विश्वसनीय साक्ष्य क्यों माना जाता है?",
    "Written accounts require a literate society and always involve selective narrative choices. Rock art was made contemporaneously by the people themselves, recording real everyday activities (hunting, dancing, honey gathering) without mediation. There are no scribes selectively emphasising certain events. The visual record is direct and contemporary, making it an unfiltered witness to Mesolithic life.",
    "लिखित विवरण के लिए एक साक्षर समाज की आवश्यकता होती है और इसमें हमेशा चयनात्मक कथा विकल्प शामिल होते हैं। शैल कला लोगों द्वारा एक साथ बनाई गई थी, वास्तविक रोजमर्रा की गतिविधियों (शिकार, नृत्य, शहद इकट्ठा करना) को बिना मध्यस्थता के रिकॉर्ड करती है। दृश्य रिकॉर्ड प्रत्यक्ष और समकालीन है, जिससे यह मध्यपाषाणकालीन जीवन का एक अनफ़िल्टर्ड गवाह बन जाता है।"
)

# --- 10. How (3 Questions) ---
add_open(sec5_en, sec5_hi, "How",
    "How do archaeologists date the Bhimbetka rock paintings to specific prehistoric periods?",
    "पुरातत्वविद भीमबेटका शैल चित्रों को विशिष्ट प्रागैतिहासिक काल में कैसे दिनांकित करते हैं?",
    "Three methods are used: (1) Stratigraphic excavation of cultural deposits beneath the shelters — the period of deposit matches the earliest art. (2) Stylistic analysis — Mesolithic art is dynamic, energetic, and shows small humans hunting with bows; Neolithic art shows cattle ploughing. (3) Superimposition — newer paintings are laid over older ones; the layer sequence is read to determine relative chronology.",
    "तीन विधियों का उपयोग किया जाता है: (1) आश्रयों के नीचे सांस्कृतिक निक्षेपों का स्तरविन्यासात्मक उत्खनन — निक्षेप का काल सबसे पहली कला से मेल खाता है। (2) शैलीगत विश्लेषण — मध्यपाषाणकालीन कला गतिशील, ऊर्जावान है और धनुष से शिकार करते छोटे मनुष्यों को दिखाती है। (3) सुपरइम्पोजिशन — नई चित्रकारी पुरानी के ऊपर रखी गई है; परत अनुक्रम सापेक्ष कालक्रम निर्धारित करने के लिए पढ़ा जाता है।"
)

add_open(sec5_en, sec5_hi, "How",
    "How does rock art act as a 'window into the mind' of prehistoric people?",
    "शैल कला प्रागैतिहासिक लोगों के 'मन में झाँकने की खिड़की' के रूप में कैसे काम करती है?",
    "Art requires intention, decision-making, and symbolic thinking — all markers of modern cognition. When Mesolithic humans depicted a hunt, they weren't just recording it; they may have been performing sympathetic magic (painting a successful hunt to make it happen), communicating social stories, or teaching the young. The choice of colours, the postures, the group compositions — all encode cultural values, fears, and desires that we can decode with anthropological tools.",
    "कला के लिए इरादा, निर्णय लेना और प्रतीकात्मक सोच की आवश्यकता होती है — ये सभी आधुनिक अनुभूति के संकेतक हैं। जब मध्यपाषाणकालीन मनुष्यों ने एक शिकार को चित्रित किया, तो वे केवल इसे रिकॉर्ड नहीं कर रहे थे; वे सहानुभूतिपूर्ण जादू कर रहे हो सकते थे, सामाजिक कहानियाँ बता रहे थे, या युवाओं को सिखा रहे थे। रंगों की पसंद, मुद्राएं — सभी सांस्कृतिक मूल्यों को एन्कोड करते हैं।"
)

add_open(sec5_en, sec5_hi, "How",
    "How does the honey-gathering scene at Bhimbetka provide direct evidence of the Mesolithic subsistence economy?",
    "भीमबेटका में शहद इकट्ठा करने का दृश्य मध्यपाषाणकालीन जीवन निर्वाह अर्थव्यवस्था का प्रत्यक्ष साक्ष्य कैसे प्रदान करता है?",
    "The scene shows a human figure climbing a tree or hanging from a rope, reaching into a beehive while bees swarm around. This proves: (1) Humans specifically targeted honey as a high-caloric food source; (2) They had knowledge of bee behaviour and developed strategies to collect honey; (3) Wild forest resources were actively exploited beyond just hunting large animals — confirming the broad-spectrum foraging model.",
    "दृश्य में एक मानव आकृति एक पेड़ पर चढ़ती है या रस्सी से लटकती है, मधुमक्खियों के चारों ओर भिनभिनाते हुए छत्ते में पहुँचती है। यह साबित करता है: (1) मनुष्यों ने विशेष रूप से शहद को उच्च-कैलोरी खाद्य स्रोत के रूप में लक्षित किया; (2) उन्हें मधुमक्खी व्यवहार का ज्ञान था; (3) बड़े जानवरों के शिकार से परे जंगली वन संसाधनों का सक्रिय रूप से शोषण किया गया — व्यापक-स्पेक्ट्रम भोजन संग्रह मॉडल की पुष्टि करता है।"
)

# --- 11. Case Study (3 Questions) ---
add_open(sec5_en, sec5_hi, "Case Study",
    "Case Study: V.S. Wakankar and the Discovery of Bhimbetka.\nHow did this accidental discovery reshape Indian prehistoric studies?",
    "मामला अध्ययन: वी.एस. वाकणकर और भीमबेटका की खोज।\nइस आकस्मिक खोज ने भारतीय प्रागैतिहासिक अध्ययनों को कैसे पुनः आकार दिया?",
    "Wakankar was travelling by train and noticed the distinctive Vindhyan sandstone formations. He investigated on foot and found shelters with layers of paintings. Before this, India's prehistoric cultural record was sparse and mostly limited to stone tools. Bhimbetka proved that prehistoric Indians had rich artistic traditions comparable to the cave art of France and Spain. It established that Homo sapiens in the Indian subcontinent had achieved symbolic, aesthetic, and cognitive modernity at the same time as their global contemporaries.",
    "वाकणकर ट्रेन से यात्रा कर रहे थे और उन्होंने विशिष्ट विंध्यन बलुआ पत्थर की संरचनाओं को देखा। उन्होंने पैदल जाँच की और चित्रों की परतों के साथ आश्रय खोजे। इससे पहले, भारत का प्रागैतिहासिक सांस्कृतिक रिकॉर्ड विरल था और ज्यादातर पत्थर के उपकरणों तक सीमित था। भीमबेटका ने साबित किया कि प्रागैतिहासिक भारतीयों की फ्रांस और स्पेन की गुफा कला के बराबर समृद्ध कलात्मक परंपराएं थीं।"
)

add_open(sec5_en, sec5_hi, "Case Study",
    "Case Study: Superimposed Paintings at Bhimbetka.\nExplain how overlapping layers of paintings reveal chronological change.",
    "मामला अध्ययन: भीमबेटका में सुपरइम्पोज्ड चित्रकारी।\nस्पष्ट करें कि चित्रों की ओवरलैपिंग परतें कालानुक्रमिक परिवर्तन को कैसे प्रकट करती हैं।",
    "Some Bhimbetka panels show multiple painting layers: the lowest are Mesolithic dynamic hunting scenes in red; over them are Chalcolithic motifs (geometric shapes, domesticated animals); the uppermost layers have historical-period motifs (riders on horseback). By reading these layers from bottom to top, archaeologists reconstruct the cultural shifts from hunting communities to pastoral to equestrian — a visual timeline of 10,000+ years.",
    "कुछ भीमबेटका पैनलों में चित्रकारी की कई परतें हैं: सबसे निचले लाल रंग में मध्यपाषाणकालीन गतिशील शिकार दृश्य हैं; उनके ऊपर ताम्रपाषाणकालीन रूपांकन (ज्यामितीय आकृतियाँ, पालतू जानवर) हैं; सबसे ऊपरी परतों में ऐतिहासिक-काल के रूपांकन (घोड़े पर सवार) हैं। इन परतों को नीचे से ऊपर पढ़कर पुरातत्वविद शिकार से पशुचारण से अश्वारोही समुदायों तक सांस्कृतिक बदलावों का पुनर्निर्माण करते हैं।"
)

add_open(sec5_en, sec5_hi, "Case Study",
    "Case Study: The Dancing Scene at Bhimbetka.\nWhat can archaeologists infer about the social and ritual life of Mesolithic communities from this painting?",
    "मामला अध्ययन: भीमबेटका में नृत्य दृश्य।\nइस चित्रकारी से पुरातत्वविद मध्यपाषाणकालीन समुदायों के सामाजिक और अनुष्ठान जीवन के बारे में क्या अनुमान लगा सकते हैं?",
    "The dancing scene shows multiple human figures in motion with raised arms, suggesting group movement. Inferences: (1) Group dancing required a minimum population gathering — confirming seasonal band aggregations at fixed sites. (2) Synchronised movement requires shared knowledge and cultural transmission across generations. (3) Dancing in ethnographic parallels (San, Aboriginal) is associated with spirit contact, hunting magic, healing, and marking of seasonal transitions. This makes Bhimbetka's dancing scenes evidence of structured religious and social life.",
    "नृत्य दृश्य में ऊंचे हाथों के साथ गति में कई मानव आकृतियाँ हैं, जो समूह आंदोलन का सुझाव देती हैं। अनुमान: (1) समूह नृत्य के लिए न्यूनतम जनसंख्या एकत्रीकरण आवश्यक था — निश्चित स्थलों पर मौसमी बैंड एकत्रीकरण की पुष्टि करता है। (2) समकालिक आंदोलन के लिए साझा ज्ञान की आवश्यकता होती है। (3) नृत्य आत्मा संपर्क, शिकार जादू, उपचार से जुड़ा है। यह भीमबेटका के नृत्य दृश्यों को संरचित धार्मिक और सामाजिक जीवन के साक्ष्य बनाता है।"
)

# --- 12. Teach the Concept (3 Questions) ---
add_open(sec5_en, sec5_hi, "Teach the Concept",
    "Teach the Concept: Explain why Bhimbetka's rock art is India's equivalent of France's Lascaux Caves.",
    "अवधारणा समझाएं: समझाएं कि भीमबेटका की शैल कला फ्रांस की लास्कौक्स गुफाओं के भारतीय समकक्ष क्यों है।",
    "Lascaux in France contains Paleolithic-Mesolithic cave paintings showing horses, bulls, and hunting scenes — evidence that prehistoric Europeans were sophisticated artists. Bhimbetka does the same for South Asia: it shows that humans in India were equally sophisticated, painting hunting scenes, dancing rituals, and honey-gathering activities. Both sites prove that wherever Homo sapiens settled, they created art — a universal marker of cultural intelligence.",
    "फ्रांस में लास्कौक्स में पुरापाषाण-मध्यपाषाणकालीन गुफा चित्र हैं जो घोड़े, बैल और शिकार के दृश्य दिखाते हैं — साक्ष्य कि प्रागैतिहासिक यूरोपीय परिष्कृत कलाकार थे। भीमबेटका दक्षिण एशिया के लिए वही करता है: यह दिखाता है कि भारत में मनुष्य समान रूप से परिष्कृत थे। दोनों स्थल साबित करते हैं कि जहाँ भी होमो सेपियन्स बसे, उन्होंने कला बनाई।"
)

add_open(sec5_en, sec5_hi, "Teach the Concept",
    "Teach the Concept: Using a 'newspaper photograph' analogy, explain what Bhimbetka's rock art tells us about daily Mesolithic life.",
    "अवधारणा समझाएं: 'समाचार पत्र की तस्वीर' सादृश्य का उपयोग करते हुए, समझाएं कि भीमबेटका की शैल कला हमें दैनिक मध्यपाषाणकालीन जीवन के बारे में क्या बताती है।",
    "Imagine a newspaper from 8000 years ago. The photographs would show: a hunt (today's business story), a dance festival (the cultural page), a honey collector (the food section), and charging animals (the nature section). That is exactly what Bhimbetka's paintings are — a prehistoric newspaper. Each painting is a 'snapshot' of an event that was real enough for someone to record it. Taken together, they give us a comprehensive view of what mattered in Mesolithic daily life.",
    "8000 साल पहले के एक समाचार पत्र की कल्पना करें। तस्वीरें दिखाएंगी: एक शिकार (आज की व्यापारिक कहानी), एक नृत्य उत्सव (सांस्कृतिक पृष्ठ), एक शहद संग्रहकर्ता (भोजन अनुभाग), और हमला करने वाले जानवर (प्रकृति अनुभाग)। यही भीमबेटका के चित्र हैं — एक प्रागैतिहासिक समाचार पत्र। प्रत्येक चित्र एक ऐसी घटना का 'स्नैपशॉट' है जो किसी के लिए रिकॉर्ड करने लायक थी।"
)

add_open(sec5_en, sec5_hi, "Teach the Concept",
    "Teach the Concept: Explain how the layered paintings at Bhimbetka are like the pages of a history book.",
    "अवधारणा समझाएं: समझाएं कि भीमबेटका में स्तरित चित्रकारी इतिहास की किताब के पृष्ठों की तरह कैसे हैं।",
    "History books have chapters: ancient, medieval, modern. Bhimbetka's wall has the same structure — but in layers of paint. The bottom layer (Mesolithic) is Chapter 1: hunters with bows and small animals. The middle layer (Chalcolithic/Neolithic) is Chapter 2: domesticated cattle and geometric patterns. The top layer (Early Historical) is Chapter 3: horsemen and warriors. By reading from bottom to top, we read India's cultural history written in pigment on stone.",
    "इतिहास की किताबों में अध्याय होते हैं: प्राचीन, मध्यकालीन, आधुनिक। भीमबेटका की दीवार में वही संरचना है — लेकिन रंग की परतों में। निचली परत (मध्यपाषाण) अध्याय 1 है: धनुष के साथ शिकारी और छोटे जानवर। मध्य परत (ताम्रपाषाण/नवपाषाण) अध्याय 2 है: पालतू मवेशी और ज्यामितीय पैटर्न। शीर्ष परत (प्रारंभिक ऐतिहासिक) अध्याय 3 है: घुड़सवार और योद्धा। नीचे से ऊपर पढ़कर, हम पत्थर पर रंग में लिखे भारत के सांस्कृतिक इतिहास को पढ़ते हैं।"
)
