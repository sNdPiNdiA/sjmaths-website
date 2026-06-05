from .helpers import add_mcq, add_multi_mcq, add_tf, add_blank, add_match, add_oneliner, add_ar, add_stmt, add_open

sec1_en = []
sec1_hi = []

# --- 1. MCQ (5 Questions) ---
add_mcq(sec1_en, sec1_hi,
    "The Lower Paleolithic site of Attirampakkam in Tamil Nadu was dated to c. 1.5 million years ago using which absolute dating method?",
    "तमिलनाडु में स्थित निम्न पुरापाषाणकालीन स्थल अतिरामपक्कम को लगभग 15 लाख वर्ष पुराना किस निरपेक्ष काल-निर्धारण विधि द्वारा आंका गया था?",
    ["Radiocarbon Dating", "Thermoluminescence", "Cosmogenic Nuclide Burial Dating", "Potassium-Argon Dating"],
    ["रेडियोकार्बन डेटिंग", "थर्मोलुमिनेसेंस", "कॉस्मोजेनिक न्यूक्लाइड दफन डेटिंग", "पोटेशियम-आर्गन डेटिंग"],
    2,
    "Shanti Pappu and her team dated the Acheulian tools at Attirampakkam using cosmogenic nuclide burial dating, measuring the isotopes Be-10 and Al-26 in quartz sand.",
    "शांति पप्पू और उनकी टीम ने क्वार्ट्ज रेत में बेरेलियम-10 और एल्युमिनियम-26 समस्थानिकों (isotopes) को मापकर कॉस्मोजेनिक न्यूक्लाइड दफन डेटिंग विधि से अतिरामपक्कम के एशुलेयिन उपकरणों का काल-निर्धारण किया।"
)

add_mcq(sec1_en, sec1_hi,
    "In the Hunsgi-Baichbal valley of Karnataka, which raw material was uniquely quarried for manufacturing Acheulian handaxes?",
    "कर्नाटक की हुन्सगी-बैचबल घाटी में, एशुलेयिन हस्तकुठार (handaxes) बनाने के लिए किस कच्चे माल का विशिष्ट रूप से उत्खनन किया गया था?",
    ["Quartzite", "Limestone", "Chert", "Basalt"],
    ["क्वार्ट्जाइट", "चूना पत्थर (Limestone)", "चर्ट", "बेसाल्ट"],
    1,
    "Unlike most Indian sites where quartzite was the main raw material, Hunsgi stands out because limestone was quarried to manufacture Acheulian tools.",
    "अधिकांश भारतीय स्थलों के विपरीत जहां क्वार्ट्जाइट मुख्य कच्चा माल था, हुन्सगी अद्वितीय है क्योंकि यहां एशुलेयिन उपकरणों के निर्माण के लिए चूना पत्थर का उत्खनन किया गया था।"
)

add_mcq(sec1_en, sec1_hi,
    "The first Paleolithic handaxe in India was discovered in 1863 by Robert Bruce Foote at which gravel pit site?",
    "रॉबर्ट ब्रूस फुट द्वारा 1863 में भारत में खोजा गया पहला पुरापाषाणकालीन हस्तकुठार किस बजरी गड्ढे वाले स्थल से प्राप्त हुआ था?",
    ["Pallavaram near Chennai", "Attirampakkam", "Hunsgi", "Didwana"],
    ["चेन्नई के निकट पल्लवरम", "अतिरामपक्कम", "हुन्सगी", "डीडवाना"],
    0,
    "Robert Bruce Foote discovered the first Paleolithic tool in a gravel pit at Pallavaram near Chennai on May 30, 1863.",
    "रॉबर्ट ब्रूस फुट ने 30 मई, 1863 को चेन्नई के पास पल्लवरम में एक बजरी गड्ढे से भारत का पहला पुरापाषाणकालीन उपकरण हस्तकुठार खोजा था।"
)

add_mcq(sec1_en, sec1_hi,
    "The Lower Paleolithic site of Didwana is located in which semi-arid margin of India?",
    "निम्न पुरापाषाणकालीन स्थल डीडवाना भारत के किस अर्ध-शुष्क किनारे पर स्थित है?",
    ["Thar Desert, Rajasthan", "Deccan Plateau, Maharashtra", "Vindhyas, Madhya Pradesh", "Rann of Kutch, Gujarat"],
    ["थार मरुस्थल, राजस्थान", "दक्कन का पठार, महाराष्ट्र", "विंध्य, मध्य प्रदेश", "कच्छ का रन, गुजरात"],
    0,
    "Didwana is located in Nagaur district of Rajasthan, showcasing shifting dune stratigraphy and Paleolithic occupations in the Thar margins.",
    "डीडवाना राजस्थान के नागौर जिले में स्थित है, जो थार मरुस्थल के किनारों पर बदलते रेत के टीलों और पुरापाषाणकालीन बस्तियों को दर्शाता है।"
)

add_mcq(sec1_en, sec1_hi,
    "The Soanian pebble chopper-chopping tradition is centered on which major river valley in the Potwar Plateau?",
    "सोअन बटिकाश्म (pebble) चॉपर-चॉपिंग परंपरा पोटवार पठार की किस मुख्य नदी घाटी में केंद्रित है?",
    ["Indus River Valley", "Soan River Valley", "Pravara River Valley", "Luni River Valley"],
    ["सिंधु नदी घाटी", "सोअन नदी घाटी", "प्रवरा नदी घाटी", "लूनी नदी घाटी"],
    1,
    "The Soanian tradition is named after the Soan River (a tributary of the Indus) flowing through Punjab and Potwar Plateau in Pakistan.",
    "सोअन परंपरा का नाम पाकिस्तान के पंजाब और पोटवार पठार से बहने वाली सोअन नदी (सिंधु की सहायक नदी) के नाम पर रखा गया है।"
)

# --- 2. Multiple Correct MCQ (5 Questions) ---
add_multi_mcq(sec1_en, sec1_hi,
    "Which of the following characteristics distinguish the Soanian tradition from the Acheulian tradition? (Select all that apply)",
    "निम्नलिखित में से कौन सी विशेषताएं सोअन परंपरा को एशुलेयिन परंपरा से अलग करती हैं? (सभी सही विकल्प चुनें)",
    ["Use of river pebbles as cores", "Dominance of chopper-chopping tools", "Abundance of bifacial cleavers", "Association with the Potwar Plateau"],
    ["नदी के पत्थरों (पेबल्स) का कोर के रूप में उपयोग", "चॉपर-चॉपिंग उपकरणों की प्रधानता", "द्वि-मुखी विदारकों (cleavers) की प्रचुरता", "पोटवार पठार से जुड़ाव"],
    [0, 1, 3],
    "The Soanian tradition is characterized by pebble-based chopper-chopping tools centered on the Soan River in Potwar (Pakistan). Handaxes and cleavers are diagnostic of the Acheulian tradition.",
    "सोअन परंपरा की विशेषता पोटवार (पाकिस्तान) में सोअन नदी पर केंद्रित बटिकाश्म (pebble) आधारित चॉपर-चॉपिंग उपकरण हैं। हस्तकुठार और विदारक एशुलेयिन परंपरा के पहचानकर्ता हैं।"
)

add_multi_mcq(sec1_en, sec1_hi,
    "Which of the following geographical regions in India show prominent sequences of Lower Paleolithic occupation? (Select all that apply)",
    "भारत के निम्नलिखित भौगोलिक क्षेत्रों में से कौन से क्षेत्र निम्न पुरापाषाणकालीन बस्तियों के प्रमुख अनुक्रम प्रदर्शित करते हैं? (सभी सही विकल्प चुनें)",
    ["Didwana in Rajasthan", "Belan Valley in Uttar Pradesh", "Kortallayar basin in Tamil Nadu", "Ganga-Yamuna Alluvial Plains"],
    ["राजस्थान में डीडवाना", "उत्तर प्रदेश में बेलन घाटी", "तमिलनाडु में कोर्तलैयार बेसिन", "गंगा-यमुना का जलोढ़ मैदानी भाग"],
    [0, 1, 2],
    "Didwana, Belan Valley, and Kortallayar basin contain rich Lower Paleolithic sequences. The Ganga-Yamuna alluvial plains lack stone raw materials and thus show no prehistoric stone age sites.",
    "डीडवाना, बेलन घाटी और कोर्तलैयार बेसिन में समृद्ध निम्न पुरापाषाणकालीन अनुक्रम मिलते हैं। गंगा-यमुना के जलोढ़ मैदानों में पत्थरों के कच्चे माल की कमी थी, इसलिए यहां कोई प्रागैतिहासिक पाषाण युग के स्थल नहीं हैं।"
)

add_multi_mcq(sec1_en, sec1_hi,
    "Which of the following stone raw materials were utilized for making tools during the Lower Paleolithic phase in India? (Select all that apply)",
    "भारत में निम्न पुरापाषाण चरण के दौरान उपकरण बनाने के लिए निम्नलिखित में से किन पत्थरों का उपयोग किया गया था? (सभी सही विकल्प चुनें)",
    ["Quartzite", "Limestone at Hunsgi", "Dolerite and Basalt in Deccan", "Obsidian"],
    ["क्वार्ट्जाइट", "हुन्सगी में चूना पत्थर", "दक्कन में डोलेराइट और बेसाल्ट", "ओब्सीडियन"],
    [0, 1, 2],
    "Quartzite was the most common rock. Limestone was used in Hunsgi. Basalt and dolerite were used in the Deccan (e.g. at Chirki-Nevasa). Obsidian was not used in the Indian Paleolithic.",
    "क्वार्ट्जाइट सबसे आम पत्थर था। हुन्सगी में चूना पत्थर का उपयोग किया गया था। दक्कन (जैसे चिरकी-नेवासा) में बेसाल्ट और डोलेराइट का उपयोग किया गया था। भारतीय पुरापाषाण में ओब्सीडियन का उपयोग नहीं हुआ।"
)

add_multi_mcq(sec1_en, sec1_hi,
    "Which of the following features are characteristic of Lower Paleolithic open-air habitation sites? (Select all that apply)",
    "निम्न पुरापाषाणकालीन खुले बस्तियों वाले स्थलों (open-air habitation sites) की निम्नलिखित में से कौन सी विशेषताएं हैं? (सभी सही विकल्प चुनें)",
    ["Located near perennial water springs or river channels", "Show accumulation of tool debitage and raw cores", "Feature permanent mud brick walls", "Located near stone outcrops for raw materials"],
    ["बारहमासी पानी के स्रोतों या नदी चैनलों के पास होना", "उपकरणों के कचरे (debitage) और कच्चे कोर के संचय को दिखाना", "स्थायी मिट्टी की ईंट की दीवारें प्रदर्शित करना", "कच्चे माल के लिए पत्थरों के स्रोतों के निकट होना"],
    [0, 1, 3],
    "Open-air sites are found near water and raw materials, displaying tool waste. Mud brick walls are not found in the Paleolithic; they appear in the Neolithic.",
    "खुले स्थल पानी और कच्चे माल के स्रोतों के पास मिलते हैं, और यहाँ उपकरण निर्माण का कचरा दिखता है। मिट्टी की ईंट की दीवारें पुरापाषाण काल में नहीं मिलतीं; वे नवपाषाण काल में शुरू होती हैं।"
)

add_multi_mcq(sec1_en, sec1_hi,
    "Which of the following fauna are reconstructed as existing in India during the Pleistocene epoch when Lower Paleolithic humans lived? (Select all that apply)",
    "प्लीस्टोसीन युग (जिसमें निम्न पुरापाषाणकालीन मनुष्य रहते थे) के दौरान भारत में निम्नलिखित में से किन वन्य जीवों की उपस्थिति का पुनर्निर्माण किया गया है? (सभी सही विकल्प चुनें)",
    ["Equus (wild horse)", "Elephas (wild elephant)", "Bos (wild cattle)", "Domesticated Sheep"],
    ["इक्वस (जंगली घोड़ा)", "एलीफस (जंगली हाथी)", "बोस (जंगली मवेशी)", "पालतू भेड़"],
    [0, 1, 2],
    "Pleistocene fauna in India included wild ancestors of horses, elephants, cattle, hippopotamus, and rhinoceros. Sheep domestication is a Neolithic phenomenon.",
    "भारत में प्लीस्टोसीन काल के जीवों में घोड़ों, हाथियों, मवेशियों, दरियाई घोड़ों और गैंडों के जंगली पूर्वज शामिल थे। भेड़ का घरेलूकरण नवपाषाण काल की घटना है।"
)

# --- 3. True/False (8 Questions) ---
add_tf(sec1_en, sec1_hi,
    "Is it true that coarse quartzite was the only raw material used for making handaxes across all Lower Paleolithic sites in the Indian subcontinent?",
    "क्या यह सत्य है कि भारतीय उपमहाद्वीप के सभी निम्न पुरापाषाण स्थलों पर हस्तकुठार बनाने के लिए केवल मोटे क्वार्ट्जाइट का ही उपयोग किया गया था?",
    False,
    "False. While quartzite was the most widely used material, limestone was utilized at Hunsgi, and basalt/dolerite was used in parts of the Deccan.",
    "गलत। यद्यपि क्वार्ट्जाइट सबसे व्यापक रूप से उपयोग की जाने वाली सामग्री थी, हुन्सगी में चूना पत्थर और दक्कन के कुछ हिस्सों में बेसाल्ट/डोलेराइट का उपयोग किया गया था।"
)

add_tf(sec1_en, sec1_hi,
    "The Hunsgi-Baichbal valley displays intensive tool-making workshop camps next to active groundwater springs.",
    "हुन्सगी-बैचबल घाटी सक्रिय भूजल स्रोतों के ठीक बगल में सघन उपकरण निर्माण कार्यशाला शिविरों को प्रदर्शित करती है।",
    True,
    "True. Springs provided a reliable water supply, attracting hunter-gatherers to set up factory-cum-habitation workshops nearby.",
    "सत्य। भूजल के झरने विश्वसनीय पानी की आपूर्ति प्रदान करते थे, जिससे शिकारी-संग्रहकर्ता वहाँ अपने कार्यशाला-सह-निवास स्थापित करते थे।"
)

add_tf(sec1_en, sec1_hi,
    "The fossil cranium of Narmada Man was found associated with late Acheulian handaxes in the gravel layers of Hathnora.",
    "नर्मदा मानव की जीवाश्मीकृत खोपड़ी हथनोरा की बजरी की परतों में उत्तर-एशुलेयिन हस्तकुठारों के साथ पाई गई थी।",
    True,
    "True. The Hathnora hominin skull was recovered from a basal conglomerate gravel layer containing late Acheulian handaxes and cleavers.",
    "सत्य। हथनोरा की मानव खोपड़ी एक कंकड़ बजरी की परत से मिली थी जिसमें उत्तर-एशुलेयिन हस्तकुठार और विदारक शामिल थे।"
)

add_tf(sec1_en, sec1_hi,
    "Soanian pebble tool tradition completely dominated Southern India, with a complete absence of any Acheulian bifaces.",
    "सोअन बटिकाश्म (pebble) उपकरण परंपरा पूरी तरह से दक्षिण भारत पर हावी थी, और वहाँ एशुलेयिन द्वि-मुखी उपकरणों का पूर्ण अभाव था।",
    False,
    "False. Soanian tools are centered in Northern India (Pakistan/Himachal), and Southern India is dominated by the Acheulian tradition (Madrasian tradition).",
    "गलत। सोअन उपकरण उत्तरी भारत (पाकिस्तान/हिमाचल) में केंद्रित हैं, और दक्षिण भारत में एशुलेयिन परंपरा (मद्रासियन परंपरा) का वर्चस्व है।"
)

add_tf(sec1_en, sec1_hi,
    "The stratigraphic sequence at Didwana, Rajasthan, contains deep deposits of sand dunes and playa lake sediments indicating wet/dry climatic cycles.",
    "राजस्थान के डीडवाना में रेत के टीलों और प्लाया झील के तलछटों के गहरे निक्षेप मिलते हैं जो आर्द्र/शुष्क जलवायु चक्रों को दर्शाते हैं।",
    True,
    "True. The Didwana trench (specifically at 16R dune) shows alternating layers of calcium carbonate calcrete and windblown sand, indicating Pleistocene wet and dry phases.",
    "सत्य। डीडवाना की खुदाई (विशेष रूप से 16R टीले पर) में कैल्शियम कार्बोनेट की परतें और हवा से उड़कर आई रेत की परतें मिलती हैं, जो प्लीस्टोसीन काल के आर्द्र और शुष्क चरणों को दर्शाती हैं।"
)

add_tf(sec1_en, sec1_hi,
    "The term 'Acheulian' is named after the prehistoric site of St. Acheul located in Germany.",
    "एशुलेयिन (Acheulian) शब्द का नाम जर्मनी में स्थित सेंट एशुल के प्रागैतिहासिक स्थल के नाम पर रखा गया है।",
    False,
    "False. The Acheulian tradition is named after the site of St. Acheul located near Amiens in northern France.",
    "गलत। एशुलेयिन परंपरा का नाम उत्तरी फ्रांस में अमियंस के पास स्थित सेंट एशुल (St. Acheul) नामक स्थल के नाम पर रखा गया है।"
)

add_tf(sec1_en, sec1_hi,
    "Mortimer Wheeler introduced the systematic grid system of excavation in India to maintain stratigraphical control.",
    "मॉर्टिमर व्हीलर ने स्तरविन्यास नियंत्रण बनाए रखने के लिए भारत में उत्खनन की व्यवस्थित ग्रिड प्रणाली की शुरुआत की।",
    True,
    "True. Wheeler introduced grid-based excavations with earth baulks in the 1940s while serving as Director General of the ASI.",
    "सत्य। व्हीलर ने 1940 के दशक में एएसआई के महानिदेशक के रूप में कार्य करते समय मिट्टी के बाल्क वाली ग्रिड-आधारित उत्खनन प्रणाली की शुरुआत की थी।"
)

add_tf(sec1_en, sec1_hi,
    "The Law of Superposition states that in an undisturbed stratigraphic sequence, the lowest layers are the youngest.",
    "सुपरपोजिशन का नियम (Law of Superposition) यह बताता है कि एक अबाधित स्तरविन्यास अनुक्रम में, सबसे निचली परतें सबसे नई होती हैं।",
    False,
    "False. The Law of Superposition states that the lowest layers are the oldest, and successive layers above are progressively younger.",
    "गलत। सुपरपोजिशन का नियम बताता है कि सबसे निचली परतें सबसे पुरानी होती हैं, और ऊपर की परतें क्रमशः नई होती हैं।"
)

# --- 4. Fill in the Blank (8 Questions) ---
add_blank(sec1_en, sec1_hi,
    "The first Paleolithic handaxe in India was found at Pallavaram in 1863 by ________.",
    "भारत में पहला पुरापाषाणकालीन हस्तकुठार 1863 में पल्लवरम में ________ द्वारा खोजा गया था।",
    "Robert Bruce Foote", "रॉबर्ट ब्रूस फुट",
    "Robert Bruce Foote discovered the first Paleolithic tool in India on May 30, 1863.",
    "रॉबर्ट ब्रूस फुट ने 30 मई, 1863 को भारत में पहले पुरापाषाणकालीन हस्तकुठार की खोज की थी।"
)

add_blank(sec1_en, sec1_hi,
    "At the Lower Paleolithic workshop site of Hunsgi in Karnataka, the primary raw material used was ________.",
    "कर्नाटक में निम्न पुरापाषाणकालीन कार्यशाला स्थल हुन्सगी में प्रयुक्त प्राथमिक कच्चा माल ________ था।",
    "limestone", "चूना पत्थर",
    "Hunsgi is unique because it utilized local limestone instead of quartzite for tool manufacture.",
    "हुन्सगी अद्वितीय है क्योंकि यहाँ हस्तकुठार बनाने के लिए क्वार्ट्जाइट के स्थान पर स्थानीय चूना पत्थर का उपयोग किया गया था।"
)

add_blank(sec1_en, sec1_hi,
    "Cosmogenic nuclide burial dating dated the Acheulian layers of Attirampakkam to approximately ________ million years ago.",
    "कॉस्मोजेनिक न्यूक्लाइड दफन डेटिंग ने अतिरामपक्कम के एशुलेयिन जमावों को लगभग ________ मिलियन वर्ष पुराना आंका।",
    "1.5", "1.5",
    "The Be-10 and Al-26 isotope ratio in quartz sand dated the tools to c. 1.5 million years ago.",
    "क्वार्ट्ज रेत में बेरेलियम-10 और एल्युमिनियम-26 समस्थानिक अनुपात से इन उपकरणों को लगभग 1.5 मिलियन वर्ष पुराना आंका गया।"
)

add_blank(sec1_en, sec1_hi,
    "Didwana, which shows deep Lower Paleolithic dune stratigraphy, is located in the state of ________.",
    "डीडवाना, जो गहरे निम्न पुरापाषाणकालीन टीले के स्तरविन्यास को दर्शाता है, ________ राज्य में स्थित है।",
    "Rajasthan", "राजस्थान",
    "Didwana is a key prehistoric site in Nagaur district of Rajasthan.",
    "डीडवाना राजस्थान के नागौर जिले में स्थित एक प्रमुख प्रागैतिहासिक स्थल है।"
)

add_blank(sec1_en, sec1_hi,
    "The Soanian pebble chopper-chopping tradition is named after the Soan River, which is a tributary of the ________ River.",
    "सोअन बटिकाश्म (pebble) चॉपर-चॉपिंग परंपरा का नाम सोअन नदी के नाम पर रखा गया है, जो ________ नदी की सहायक नदी है।",
    "Indus", "सिंधु",
    "The Soan River is a tributary of the Indus flowing through Potwar in Pakistan.",
    "सोअन नदी पाकिस्तान के पोटवार पठार से होकर बहने वाली सिंधु नदी की एक सहायक नदी है।"
)

add_blank(sec1_en, sec1_hi,
    "The type-site St. Acheul, which gave its name to the Acheulian tradition, is located in the country of ________.",
    "प्रकार-स्थल सेंट एशुल (St. Acheul), जिससे एशुलेयिन परंपरा का नाम पड़ा, ________ देश में स्थित है।",
    "France", "फ्रांस",
    "St. Acheul is a suburb of Amiens in northern France.",
    "सेंट एशुल उत्तरी फ्रांस में अमियंस का एक उपनगर है।"
)

add_blank(sec1_en, sec1_hi,
    "In Wheeler's grid method of excavation, the unexcavated earth walls left between trenches are called ________.",
    "व्हीलर की उत्खनन की ग्रिड पद्धति में, खाइयों के बीच छोड़े गए मिट्टी के बिना खोदे गए हिस्सों को ________ कहा जाता है।",
    "baulks", "बाल्क",
    "Baulks are narrow dirt walls left between trenches to record stratigraphic profiles.",
    "बाल्क खाइयों के बीच छोड़ी गई पतली दीवारें होती हैं जिनका उपयोग स्तरविन्यास आरेखों को रिकॉर्ड करने के लिए किया जाता है।"
)

add_blank(sec1_en, sec1_hi,
    "According to the Law of Superposition, in an undisturbed soil sequence, the oldest layers are located at the ________.",
    "सुपरपोजिशन के नियम के अनुसार, एक अबाधित मिट्टी के अनुक्रम में, सबसे पुरानी परतें ________ पर स्थित होती हैं।",
    "bottom", "नीचे",
    "The oldest layers are deposited first at the bottom, with younger layers forming sequentially above them.",
    "सबसे पुरानी परतें सबसे नीचे जमा होती हैं, और उनके ऊपर क्रमिक रूप से नई परतें बनती हैं।"
)

# --- 5. Match the Following (3 Questions) ---
add_match(sec1_en, sec1_hi,
    "Match the Lower Paleolithic site with its diagnostic raw material:",
    "निम्न पुरापाषाणकालीन स्थल को उसके विशिष्ट कच्चे माल से सुमेलित करें:",
    ["1. Hunsgi", "2. Attirampakkam", "3. Chirki-Nevasa"],
    ["1. हुन्सगी", "2. अतिरामपक्कम", "3. चिरकी-नेवासा"],
    ["A. Basalt / Dolerite", "B. Limestone", "C. Quartzite"],
    ["A. बेसाल्ट / डोलेराइट", "B. चूना पत्थर", "C. क्वार्ट्जाइट"],
    "1-B, 2-C, 3-A", "1-B, 2-C, 3-A"
)

add_match(sec1_en, sec1_hi,
    "Match the archaeological terminology with its definition:",
    "पुरातात्विक शब्दावली को उसकी परिभाषा से सुमेलित करें:",
    ["1. Debitage", "2. Core", "3. Flake"],
    ["1. डेबिटेज (Debitage)", "2. कोर (Core)", "3. शल्क (Flake)"],
    ["A. The parent block of stone from which fragments are struck", "B. The sharp fragment detached from a parent stone during knapping", "C. The waste lithic debris produced during stone tool manufacture"],
    ["A. पत्थर का मूल खंड जिससे टुकड़े तोड़े जाते हैं", "B. उपकरण बनाने के दौरान मूल पत्थर से निकाला गया धारदार टुकड़ा", "C. पत्थर के औजार बनाने के दौरान पैदा हुआ अपशिष्ट कचरा"],
    "1-C, 2-A, 3-B", "1-C, 2-A, 3-B"
)

add_match(sec1_en, sec1_hi,
    "Match the archaeologist with their landmark Lower Paleolithic discovery:",
    "पुरातत्वविद को उनकी ऐतिहासिक निम्न पुरापाषाण खोज से सुमेलित करें:",
    ["1. Robert Bruce Foote", "2. Shanti Pappu", "3. Arun Sonakia"],
    ["1. रॉबर्ट ब्रूस फुट", "2. शांति पप्पू", "3. अरुण सोनकिया"],
    ["A. Hathnora cranium (Narmada Man)", "B. Pallavaram handaxe (1863)", "C. Cosmic ray dating of Attirampakkam"],
    ["A. हथनोरा खोपड़ी (नर्मदा मानव)", "B. पल्लवरम हस्तकुठार (1863)", "C. अतिरामपक्कम का कॉस्मिक किरण काल-निर्धारण"],
    "1-B, 2-C, 3-A", "1-B, 2-C, 3-A"
)

# --- 6. One-Liner (8 Questions) ---
add_oneliner(sec1_en, sec1_hi,
    "Define a 'core tool' in Stone Age archaeology.",
    "पाषाण काल के पुरातत्व में 'कोर उपकरण' (core tool) को परिभाषित करें।",
    "A stone tool manufactured by chipping off waste flakes from a larger rock block to leave a shaped central tool core, such as a handaxe.",
    "एक बड़े पत्थर के खंड से टुकड़ों को तोड़कर केंद्रीय भाग को एक विशेष आकार देकर बनाया गया उपकरण, जैसे कि हस्तकुठार।"
)

add_oneliner(sec1_en, sec1_hi,
    "What is the primary function of a Lower Paleolithic 'handaxe'?",
    "निम्न पुरापाषाणकालीन 'हस्तकुठार' (handaxe) का प्राथमिक कार्य क्या था?",
    "A multi-purpose bifacial tool used for heavy-duty activities like digging, chopping wood, and butchering animal carcasses.",
    "खोदने, लकड़ी काटने और मवेशियों को काटने जैसी भारी गतिविधियों के लिए उपयोग किया जाने वाला एक बहुउद्देशीय द्वि-मुखी उपकरण।"
)

add_oneliner(sec1_en, sec1_hi,
    "Describe the characteristic shape of a Lower Paleolithic 'cleaver'.",
    "निम्न पुरापाषाणकालीन 'विदारक' (cleaver) के विशिष्ट आकार का वर्णन करें।",
    "A tool featuring a broad, straight transverse cutting edge at the front, shaped like a modern guillotine or axe blade.",
    "सामने की ओर एक चौड़ी, सीधी काटने वाली धार वाला उपकरण, जो आधुनिक छेनी या कुल्हाड़ी के ब्लेड के आकार का होता है।"
)

add_oneliner(sec1_en, sec1_hi,
    "What is a 'polyhedron' in Acheulian tool typology?",
    "एशुलेयिन उपकरण वर्गीकरण में 'बहुफलक' (polyhedron) क्या है?",
    "A heavily flaked, multi-faceted stone tool shaped roughly like a sphere or polygon, used as a missile or hammerstone.",
    "एक बहु-फलकीय पाषाण उपकरण जो लगभग गोलाकार या बहुभुज आकार का होता है, इसका उपयोग हथौड़े या प्रक्षेप्य के रूप में किया जाता था।"
)

add_oneliner(sec1_en, sec1_hi,
    "What does 'bifacial symmetry' refer to in Acheulian handaxes?",
    "एशुलेयिन हस्तकुठारों में 'द्वि-मुखी सममिति' (bifacial symmetry) से क्या तात्पर्य है?",
    "It refers to the deliberate symmetry in design along both faces and longitudinal axes, reflecting advanced cognitive planning by hominins.",
    "यह दोनों चेहरों और अनुदैर्ध्य अक्षों के साथ डिजाइन में सचेत समरूपता को संदर्भित करता है, जो होमिनिन की उन्नत संज्ञानात्मक योजना को दर्शाता है।"
)

add_oneliner(sec1_en, sec1_hi,
    "Where is the Potwar Plateau located in South Asian geography?",
    "दक्षिण एशियाई भूगोल में पोटवार पठार कहाँ स्थित है?",
    "It is located in northern Punjab, Pakistan, bordered by the Indus River and Jhelum River, housing key Soanian sites.",
    "यह उत्तरी पंजाब, पाकिस्तान में स्थित है, जो सिंधु और झेलम नदी से घिरा है, यहाँ प्रमुख सोअन स्थल स्थित हैं।"
)

add_oneliner(sec1_en, sec1_hi,
    "In which year did Shanti Pappu begin her systematic excavations at Attirampakkam?",
    "शांति पप्पू ने अतिरामपक्कम में अपना व्यवस्थित उत्खनन किस वर्ष शुरू किया था?",
    "Shanti Pappu initiated her landmark excavations at Attirampakkam in 1999 under the aegis of the Sharma Centre for Heritage Education.",
    "शांति पप्पू ने 1999 में शर्मा सेंटर फॉर हेरिटेज एजुकेशन के तत्वावधान में अतिरामपक्कम में अपना ऐतिहासिक उत्खनन शुरू किया था।"
)

add_oneliner(sec1_en, sec1_hi,
    "Did bifacial handaxes exist in the classic Soanian pebble-tool assemblages?",
    "क्या शास्त्रीय सोअन बटिकाश्म-उपकरण (pebble-tool) समूहों में द्वि-मुखी हस्तकुठार मौजूद थे?",
    "No, the classic Soanian tradition is characterized by unifacial or bifacial chopper-chopping tools on pebbles; handaxes are virtually absent.",
    "नहीं, शास्त्रीय सोअन परंपरा की विशेषता बटिकाश्म पर बने चॉपर-चॉपिंग उपकरण हैं; यहाँ हस्तकुठार पूरी तरह से अनुपस्थित हैं।"
)

# --- 7. Assertion-Reason (8 Questions) ---
add_ar(sec1_en, sec1_hi,
    "Assertion (A): Lower Paleolithic communities in Peninsular India preferred open-air habitats near river basins.\nReason (R): River basins provided a perennial water supply, rich animal resources, and abundant quartzite gravels for stone tool production.",
    "कथन (A): प्रायद्वीपीय भारत में निम्न पुरापाषाणकालीन समुदायों ने नदी घाटियों के पास खुले मैदानों में रहना पसंद किया।\nकारण (R): नदी घाटियां बारहमासी जल आपूर्ति, प्रचुर पशु संसाधन और पत्थर के उपकरण बनाने के लिए व्यापक क्वार्ट्जाइट बजरी प्रदान करती थीं।",
    0,
    "Both A and R are true and R is the correct explanation of A. River valleys provided all critical subsistence resources and tool raw materials.",
    "A और R दोनों सही हैं और R, A की सही व्याख्या करता है। नदी घाटियां भोजन, पानी और कच्चे माल के रूप में संसाधन प्रदान करती थीं।"
)

add_ar(sec1_en, sec1_hi,
    "Assertion (A): Quartzite was the exclusive material used for tool manufacturing at all Lower Paleolithic sites in India.\nReason (R): Hominins at Hunsgi in Karnataka utilized local limestone to manufacture Acheulian handaxes.",
    "कथन (A): भारत के सभी निम्न पुरापाषाण स्थलों पर उपकरण निर्माण के लिए केवल क्वार्ट्जाइट का उपयोग किया गया था।\nकारण (R): कर्नाटक के हुन्सगी में आदिम मानवों ने एशुलेयिन हस्तकुठार बनाने के लिए स्थानीय चूना पत्थर का उपयोग किया।",
    3,
    "A is false but R is true. Quartzite was dominant but not exclusive, as limestone was used at Hunsgi.",
    "A गलत है लेकिन R सही है। क्वार्ट्जाइट सबसे प्रमुख था लेकिन एकमात्र नहीं, क्योंकि हुन्सगी में चूना पत्थर का उपयोग किया गया था।"
)

add_ar(sec1_en, sec1_hi,
    "Assertion (A): The cosmic nuclide burial dating method was crucial for dating the Acheulian layers at Attirampakkam.\nReason (R): Radiocarbon dating cannot be used for sites older than approximately 50,000 years due to the rapid decay of carbon-14 isotopes.",
    "कथन (A): अतिरामपक्कम में एशुलेयिन परतों के काल-निर्धारण के लिए कॉस्मोजेनिक न्यूक्लाइड दफन डेटिंग विधि अत्यंत महत्वपूर्ण थी।\nकारण (R): कार्बन-14 समस्थानिकों (isotopes) के तेजी से क्षय के कारण लगभग 50,000 वर्ष से अधिक पुराने स्थलों के लिए रेडियोकार्बन डेटिंग का उपयोग नहीं किया जा सकता है।",
    1,
    "Both A and R are true but R is not the direct explanation of A (R explains why C-14 is limited, but not how cosmogenic dating works on quartz sand).",
    "A और R दोनों सही हैं लेकिन R, A की सही व्याख्या नहीं करता है (R बताता है कि C-14 क्यों सीमित है, लेकिन यह नहीं समझाता कि क्वार्ट्ज पर कॉस्मोजेनिक डेटिंग कैसे काम करती है)।"
)

add_ar(sec1_en, sec1_hi,
    "Assertion (A): The Soanian and Acheulian traditions represent two completely isolated populations that never met in India.\nReason (R): Soanian pebble tools are found in the Punjab region, while Acheulian tools are distributed extensively throughout Peninsular India.",
    "कथन (A): सोअन और एशुलेयिन परंपराएं दो पूरी तरह से पृथक आबादी का प्रतिनिधित्व करती हैं जो भारत में कभी नहीं मिलीं।\nकारण (R): सोअन बटिकाश्म उपकरण पंजाब क्षेत्र में पाए जाते हैं, जबकि एशुलेयिन उपकरण पूरे प्रायद्वीपीय भारत में व्यापक रूप से वितरित हैं।",
    3,
    "A is false but R is true. While the geographic cores differed, there are sites in northern/western India (like Didwana) where both traditions overlap, proving they were not completely isolated.",
    "A गलत है लेकिन R सही है। भौगोलिक केंद्र अलग थे, लेकिन उत्तर-पश्चिमी भारत (जैसे डीडवाना) में दोनों परंपराएं ओवरलैप होती हैं, जो साबित करती हैं कि वे पूरी तरह अलग नहीं थीं।"
)

add_ar(sec1_en, sec1_hi,
    "Assertion (A): Deep stratigraphic excavations at Didwana provide a valuable record of paleoclimatic changes in the Thar Desert.\nReason (R): The alternating layers of sand dunes and saline lake sediments capture dry and wet cycles of the Pleistocene epoch.",
    "कथन (A): डीडवाना में गहरे स्तरविन्यास उत्खनन थार मरुस्थल में पुरा-जलवायु (paleoclimatic) परिवर्तनों का एक मूल्यवान रिकॉर्ड प्रदान करते हैं।\nकारण (R): रेत के टीलों और खारे पानी के झील के तलछटों की वैकल्पिक परतें प्लीस्टोसीन युग के शुष्क और आर्द्र चक्रों को दर्शाती हैं।",
    0,
    "Both A and R are true and R is the correct explanation of A. The geological layers directly record desert wet/dry cycles.",
    "A और R दोनों सही हैं और R, A की सही व्याख्या करता है। भूवैज्ञानिक परतें मरुस्थल के आर्द्र/शुष्क चक्रों को सीधे रिकॉर्ड करती हैं।"
)

add_ar(sec1_en, sec1_hi,
    "Assertion (A): The Lower Paleolithic site of Pallavaram is historically significant in Indian prehistory.\nReason (R): It was the site where Arun Sonakia discovered the first fossilized Homo erectus skull in 1982.",
    "कथन (A): निम्न पुरापाषाणकालीन स्थल पल्लवरम भारतीय प्रागैतिहासिक काल में ऐतिहासिक रूप से महत्वपूर्ण है।\nकारण (R): यह वह स्थल था जहाँ अरुण सोनकिया ने 1982 में पहला जीवाश्मीकृत होमो इरेक्टस खोपड़ी की खोज की थी।",
    2,
    "A is true but R is false. Pallavaram is famous for Robert Bruce Foote's 1863 handaxe discovery; the Hathnora cranium was discovered by Arun Sonakia.",
    "A सही है लेकिन R गलत है। पल्लवरम 1863 में रॉबर्ट ब्रूस फुट की हस्तकुठार की खोज के लिए प्रसिद्ध है; हथनोरा खोपड़ी की खोज अरुण सोनकिया ने की थी।"
)

add_ar(sec1_en, sec1_hi,
    "Assertion (A): Hunsgi valley was a major habitation-cum-factory workshop for Acheulian communities.\nReason (R): Hunsgi lacked any local stone raw materials, forcing hominins to import quartzite boulders from the Vindhyas.",
    "कथन (A): हुन्सगी घाटी एशुलेयिन समुदायों के लिए एक प्रमुख निवास-सह-कार्यशाला स्थल थी।\nकारण (R): हुन्सगी में स्थानीय पत्थर के कच्चे माल की कमी थी, जिससे होमिनिन को विंध्य से क्वार्ट्जाइट पत्थरों का आयात करना पड़ा।",
    2,
    "A is true but R is false. Hunsgi was a factory workshop because it had abundant local limestone raw materials, not because it lacked stone.",
    "A सही है लेकिन R गलत है। हुन्सगी एक कारखाना स्थल था क्योंकि यहाँ स्थानीय चूना पत्थर प्रचुर मात्रा में उपलब्ध था, न कि पत्थरों की कमी के कारण।"
)

add_ar(sec1_en, sec1_hi,
    "Assertion (A): The grid method of excavation is superior to simple trenching for complex stratigraphic sites.\nReason (R): The grid method uses unexcavated earth walls called baulks, which preserve a vertical record of soil layers in all directions.",
    "कथन (A): जटिल स्तरविन्यास वाले स्थलों के लिए ग्रिड पद्धति साधारण खाई खोदने की तुलना में बेहतर है।\nकारण (R): ग्रिड पद्धति में 'बाल्क' नामक बिना खोदी गई मिट्टी की दीवारें छोड़ी जाती हैं, जो सभी दिशाओं में मिट्टी की परतों का ऊर्ध्वाधर रिकॉर्ड सुरक्षित रखती हैं।",
    0,
    "Both A and R are true and R is the correct explanation of A. Grid baulks allow direct stratigraphic tracking during horizontal excavations.",
    "A और R दोनों सही हैं और R, A की सही व्याख्या करता है। ग्रिड बाल्क क्षैतिज उत्खनन के दौरान स्तरविन्यास को प्रत्यक्ष ट्रैक करने की अनुमति देते हैं।"
)

# --- 8. Statement-Based (5 Questions) ---
add_stmt(sec1_en, sec1_hi,
    "Consider the following statements regarding the Lower Paleolithic Acheulian tradition:\n1. Acheulian tools display high symmetrical planning, including ovate and pear-shaped handaxes.\n2. The Soanian pebble tool tradition represents an evolutionary stage that occurred after the Acheulian tradition had completely disappeared.\nWhich of the statements given above is/are correct?",
    "निम्न पुरापाषाणकालीन एशुलेयिन परंपरा के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. एशुलेयिन उपकरण उच्च सममित योजना प्रदर्शित करते हैं, जिसमें अंडाकार और नाशपाती के आकार के हस्तकुठार शामिल हैं।\n2. सोअन बटिकाश्म (pebble) उपकरण परंपरा एक विकासात्मक चरण का प्रतिनिधित्व करती है जो एशुलेयिन परंपरा के पूरी तरह से समाप्त होने के बाद आई थी।\nकौन सा/से कथन सही है/हैं?",
    ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
    0,
    "Statement 1 is correct. Statement 2 is incorrect because the Acheulian and Soanian traditions were roughly contemporary and co-existed in some northern regions.",
    "कथन 1 सही है। कथन 2 गलत है क्योंकि एशुलेयिन और सोअन परंपराएं समकालीन थीं और कुछ उत्तरी क्षेत्रों में एक साथ मौजूद थीं।"
)

add_stmt(sec1_en, sec1_hi,
    "Consider the following statements regarding the dating of prehistoric sites:\n1. Cosmic ray exposure dating measures the duration that minerals in quartz sand have been buried away from cosmic rays.\n2. Radiocarbon dating is the primary method used to date Lower Paleolithic sites older than 1 million years in India.\nWhich of the statements given above is/are correct?",
    "प्रागैतिहासिक स्थलों के काल-निर्धारण के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. कॉस्मोजेनिक किरण दफन डेटिंग उस अवधि को मापती है जिसके दौरान क्वार्ट्ज रेत में खनिज ब्रह्मांडीय किरणों से दूर दफन रहे हैं।\n2. रेडियोकार्बन डेटिंग भारत में 10 लाख वर्ष से अधिक पुराने निम्न पुरापाषाणकालीन स्थलों के निर्धारण की प्राथमिक विधि है।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
    0,
    "Statement 1 is correct. Statement 2 is incorrect because Radiocarbon dating is limited to c. 50,000 years; Lower Paleolithic sites require methods like cosmogenic nuclide dating, Potassium-Argon, or OSL.",
    "कथन 1 सही है। कथन 2 गलत है क्योंकि रेडियोकार्बन डेटिंग लगभग 50,000 वर्षों तक सीमित है; निम्न पुरापाषाण स्थलों के लिए कॉस्मोजेनिक न्यूक्लाइड या OSL की आवश्यकता होती है।"
)

add_stmt(sec1_en, sec1_hi,
    "With reference to the Lower Paleolithic site of Hunsgi, consider the following statements:\n1. Limestone was quarried systematically to manufacture Acheulian handaxes.\n2. Hunsgi valley represents an arid scrubland completely devoid of any perennial water sources.\nWhich of the statements given above is/are correct?",
    "निम्न पुरापाषाणकालीन स्थल हुन्सगी के संदर्भ में, निम्नलिखित कथनों पर विचार करें:\n1. एशुलेयिन हस्तकुठार बनाने के लिए चूना पत्थर का व्यवस्थित रूप से उत्खनन किया गया था।\n2. हुन्सगी घाटी एक शुष्क झाड़ीदार मैदान का प्रतिनिधित्व करती है जहां बारहमासी पानी के स्रोतों का पूर्ण अभाव है।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
    0,
    "Statement 1 is correct. Statement 2 is incorrect because Hunsgi basin was rich in perennial artesian springs that attracted prehistoric hunter-gatherers.",
    "कथन 1 सही है। कथन 2 गलत है क्योंकि हुन्सगी बेसिन बारहमासी भूजल झरनों से समृद्ध था जिसने प्रागैतिहासिक शिकारियों को आकर्षित किया।"
)

add_stmt(sec1_en, sec1_hi,
    "Consider the following statements regarding the Didwana prehistoric site in Rajasthan:\n1. It displays a long stratigraphic sequence of Paleolithic occupations directly associated with dune movements.\n2. The excavations proved that the Thar Desert did not experience any humid or wet phases during the Pleistocene.\nWhich of the statements given above is/are correct?",
    "राजस्थान के डीडवाना प्रागैतिहासिक स्थल के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. यह रेत के टीलों के उतार-चढ़ाव से सीधे जुड़े पुरापाषाणकालीन मानव बस्तियों का एक लंबा स्तरविन्यास अनुक्रम प्रदर्शित करता है।\n2. यहाँ के उत्खनन ने साबित किया कि थार मरुस्थल में प्लीस्टोसीन काल के दौरान कभी भी कोई आर्द्र या गीला चरण नहीं आया।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
    0,
    "Statement 1 is correct. Statement 2 is incorrect because the alternating dune and saline lake sediments proved the Thar Desert experienced alternating wet and dry climate cycles during the Pleistocene.",
    "कथन 1 सही है। कथन 2 गलत है क्योंकि स्तरविन्यास ने साबित किया कि थार मरुस्थल में प्लीस्टोसीन के दौरान गीले और सूखे जलवायु चक्रों का क्रम चलता रहा।"
)

add_stmt(sec1_en, sec1_hi,
    "Consider the following statements regarding the discovery of prehistoric tools in India:\n1. The Pallavaram handaxe was discovered in 1863 inside a river gravel bed.\n2. Attirampakkam was excavated in the late 19th century and yielded the oldest modern human skeleton.\nWhich of the statements given above is/are correct?",
    "भारत में प्रागैतिहासिक उपकरणों की खोज के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. पल्लवरम हस्तकुठार की खोज 1863 में एक नदी बजरी के बिस्तर में की गई थी।\n2. अतिरामपक्कम का उत्खनन 19वीं सदी के अंत में किया गया था और वहाँ से सबसे पुराना आधुनिक मानव कंकाल मिला था।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
    0,
    "Statement 1 is correct (discovered in a gravel pit). Statement 2 is incorrect because Attirampakkam did not yield any human skeletal remains, only stone tools.",
    "कथन 1 सही है (एक बजरी गड्ढे में खोजा गया)। कथन 2 गलत है क्योंकि अतिरामपक्कम से कोई मानव कंकाल अवशेष नहीं मिला है, केवल पत्थर के औजार मिले हैं।"
)

# --- 9. Why (3 Questions) ---
add_open(sec1_en, sec1_hi, "Why",
    "Why was the discovery at Attirampakkam crucial for reconstructing global human migration theories?",
    "वैश्विक मानव प्रवास सिद्धांतों के पुनर्निर्माण के लिए अतिरामपक्कम की खोज क्यों महत्वपूर्ण थी?",
    "Before Attirampakkam, it was believed that the Acheulian tradition spread from Africa to India relatively late. The c. 1.5 MYA dating proved that hominins migrated out of Africa with advanced Acheulian technology much earlier, placing India as a key locus in early human evolution.",
    "अतिरामपक्कम से पहले यह माना जाता था कि एशुलेयिन परंपरा अफ्रीका से भारत में देर से फैली। लगभग 15 लाख वर्ष पुरानी खोज ने साबित कर दिया कि होमिनिन बहुत पहले ही उन्नत एशुलेयिन तकनीक के साथ अफ्रीका से बाहर चले गए थे, जिससे भारत शुरुआती मानव विकास का एक प्रमुख केंद्र बन गया।"
)

add_open(sec1_en, sec1_hi, "Why",
    "Why did Lower Paleolithic hominins prefer quartzite as a raw material for bifacial tools?",
    "निम्न पुरापाषाणकालीन आदिम मानवों ने द्वि-मुखी उपकरणों के निर्माण के लिए क्वार्ट्जाइट को कच्चे माल के रूप में क्यों प्राथमिकता दी?",
    "Quartzite is a tough metamorphic rock composed of recrystallized quartz. Unlike granite which crumbles, quartzite fractures predictably when hit (conchoidal fracture), producing sharp, durable edges that do not break easily under heavy forces like chopping and digging.",
    "क्वार्ट्जाइट एक कायांतरित (metamorphic) पत्थर है जो क्वार्ट्ज से बना होता है। ग्रेनाइट के विपरीत जो बिखर जाता है, क्वार्ट्जाइट चोट मारने पर एक निश्चित दरार में टूटता है, जिससे तेज और मजबूत किनारे बनते हैं जो खोदने और काटने के दौरान आसानी से नहीं टूटते।"
)

add_open(sec1_en, sec1_hi, "Why",
    "Why did Hunsgi valley witness intense tool manufacturing activity during dry seasonal phases?",
    "हुन्सगी घाटी में शुष्क मौसमी चरणों के दौरान सघन उपकरण निर्माण गतिविधियाँ क्यों देखी गईं?",
    "During dry seasons, surrounding scrub forest areas dried up. Hunsgi basin, rich in artesian springs, remained a reliable source of water and game animals. Hunter-gatherer bands aggregated here, taking advantage of the abundant local limestone outcrops to replenish their stone toolkits.",
    "शुष्क मौसम के दौरान, आसपास के जंगलों का पानी सूख जाता था। हुन्सगी बेसिन बारहमासी स्रोतों से समृद्ध था, जहाँ पानी और शिकार उपलब्ध रहता था। शिकारी-संग्रहकर्ता समूह यहाँ एकत्रित होते थे और स्थानीय चूना पत्थर के प्रचुर स्रोतों का उपयोग करके अपने उपकरण बनाते थे।"
)

# --- 10. How (3 Questions) ---
add_open(sec1_en, sec1_hi, "How",
    "How does the excavation layout of Hunsgi-Baichbal valley prove the existence of seasonal hunter-gatherer camps?",
    "हुन्सगी-बैचबल घाटी का उत्खनन लेआउट मौसमी शिकारी-संग्रहकर्ता शिविरों के अस्तित्व को कैसे साबित करता है?",
    "Excavations revealed clustering of finished tools, debitage (flakes), and animal bones around seasonal water springs. The presence of tool quarrying workshop sites next to small temporary camp clearings indicates bands gathered at Hunsgi during dry seasons and dispersed during monsoons.",
    "उत्खनन से मौसमी पानी के झरनों के आसपास तैयार औजारों, मलबे (शल्क) और जानवरों की हड्डियों के जमाव का पता चला। छोटे अस्थायी शिविरों के बगल में उपकरण बनाने वाली कार्यशालाओं की उपस्थिति इंगित करती है कि शुष्क मौसम में मानव समूह हुन्सगी में इकट्ठा होते थे और मानसून के दौरान बिखर जाते थे।"
)

add_open(sec1_en, sec1_hi, "How",
    "How do cosmogenic isotopes Be-10 and Al-26 accumulate to date buried stone tools?",
    "ब्रह्मांडीय किरण (cosmogenic) समस्थानिक Be-10 और Al-26 दबे हुए पाषाण उपकरणों का काल-निर्धारण करने के लिए कैसे संचित होते हैं?",
    "While quartz sand is on the surface, cosmic rays strike it, creating radioactive Beryllium-10 and Aluminum-26. Once tools are buried deep under sediment layers, cosmic rays can no longer reach them, and these isotopes decay at known rates. Measuring their ratio reveals the duration of burial.",
    "जब क्वार्ट्ज रेत सतह पर होती है, तो ब्रह्मांडीय किरणें उससे टकराकर बेरेलियम-10 और एल्युमिनियम-26 समस्थानिक बनाती हैं। एक बार जब उपकरण गाद के नीचे गहराई में दब जाते हैं, तो ब्रह्मांडीय किरणें उन तक नहीं पहुँच पातीं और इन समस्थानिकों का क्षय निश्चित दर पर होता है। उनके अनुपात को मापकर दफन की अवधि का पता लगाया जाता है।"
)

add_open(sec1_en, sec1_hi, "How",
    "How does stratigraphical analysis help determine the relative age of tools at a multi-occupational cave site like Bhimbetka?",
    "भीमबेटका जैसे बहु-आवासीय गुफा स्थल पर स्तरविन्यास (stratigraphical) विश्लेषण उपकरणों की सापेक्ष आयु निर्धारित करने में कैसे मदद करता है?",
    "According to the law of superposition, younger occupational debris accumulates on top of older deposits. By excavating vertically and recording the soil layers, archaeologists can prove that handaxes in the bottom layer are older than the flake scrapers found in the layer directly above.",
    "सुपरपोजिशन के नियम के अनुसार, पुराना कचरा नीचे और नया कचरा उसके ऊपर जमा होता है। लंबवत उत्खनन करके और मिट्टी की परतों को रिकॉर्ड करके, पुरातत्वविद यह साबित कर सकते हैं कि सबसे निचली परत के हस्तकुठार उसके ठीक ऊपर की परत में मिले शल्क खुरचनी से अधिक पुराने हैं।"
)

# --- 11. Case Study (3 Questions) ---
add_open(sec1_en, sec1_hi, "Case Study",
    "Case Study: Shanti Pappu's excavation of Attirampakkam Kortallayar Basin.\nExplain how modern interdisciplinary research methods altered the age estimates of the Indian Acheulian culture.",
    "मामला अध्ययन: Kortallayar बेसिन में शांति पप्पू द्वारा अतिरामपक्कम का उत्खनन।\nस्पष्ट करें कि आधुनिक अंतःविषय अनुसंधान विधियों ने भारतीय एशुलेयिन संस्कृति के आयु अनुमानों को कैसे बदल दिया।",
    "Earlier, Indian Acheulian tools were dated using relative river-terrace sequences, estimating them to be c. 700,000 years old. Shanti Pappu used cosmogenic nuclide burial dating on buried tools, establishing an absolute age of c. 1.5 MYA. Combined with micromorphology of soils, it proved that early hominins adapted to varying monsoon cycles much earlier than previously thought.",
    "पहले, भारतीय एशुलेयिन उपकरणों का काल-निर्धारण नदी-घाटियों के सापेक्ष अनुक्रमों के आधार पर किया जाता था, और उन्हें लगभग 7,00,000 वर्ष पुराना माना जाता था। शांति पप्पू ने उपकरणों पर कॉस्मोजेनिक न्यूक्लाइड दफन डेटिंग का उपयोग किया, जिससे लगभग 15 लाख वर्ष की आयु स्थापित हुई। मिट्टी के विश्लेषण के साथ मिलकर इसने साबित कर दिया कि प्रारंभिक मानव मानसून चक्रों के अनुकूल बहुत पहले ही ढल गए थे।"
)

add_open(sec1_en, sec1_hi, "Case Study",
    "Case Study: K. Paddayya's excavation of Hunsgi Valley.\nDetail how site catchment analysis was used to reconstruct the subsistence of Acheulian communities.",
    "मामला अध्ययन: के. पडय्या द्वारा हुन्सगी घाटी का उत्खनन।\nविस्तार से बताएं कि एशुलेयिन समुदायों के निर्वाह के पुनर्निर्माण के लिए 'साइट कैचमेंट विश्लेषण' (site catchment analysis) का उपयोग कैसे किया गया था।",
    "K. Paddayya analyzed resources within a 10 km radius of Hunsgi workshops. He identified local limestone outcrops as quarries, wild plant tubers, and small game habitats near artesian springs. This catchment analysis proved Hunsgi was a seasonal gathering point where bands manufactured tools, hunted migrating fauna, and foraged wild berries before dispersing during rains.",
    "के. पडय्या ने हुन्सगी कार्यशालाओं के 10 किमी के दायरे में संसाधनों का विश्लेषण किया। उन्होंने स्थानीय चूना पत्थर के स्रोतों, जंगली कंदों और झरनों के पास शिकार के आवासों की पहचान की। इस विश्लेषण ने साबित किया कि हुन्सगी एक मौसमी सभा स्थल था जहाँ उपकरण बनाए जाते थे, शिकार किया जाता था और बारिश के मौसम से पहले भोजन जुटाया जाता था।"
)

add_open(sec1_en, sec1_hi, "Case Study",
    "Case Study: V.N. Misra's excavations at Didwana (16R dune).\nExplain how the stratigraphic profile of a sand dune helps reconstruct Pleistocene climate changes.",
    "मामला अध्ययन: वी.एन. मिश्रा द्वारा डीडवाना (16R टीला) का उत्खनन।\nस्पष्ट करें कि रेत के टीले का स्तरविन्यास आरेख प्लीस्टोसीन जलवायु परिवर्तनों के पुनर्निर्माण में कैसे मदद करता है।",
    "At Didwana 16R, a 19-meter deep trench exposed alternating layers of wind-blown sand dunes and fossilized calcrete layers. The wind-blown sand represented arid phases (weak monsoon), while the calcrete layers (calcium carbonate deposits) represented soil stability during humid phases (wet monsoon). Lithic tools embedded in these layers anchored hominin presence to specific climate phases.",
    "डीडवाना 16R में, एक 19 मीटर गहरे गर्त ने उड़ती रेत के टीलों और जीवाश्मीकृत कैल्शियम कार्बोनेट (कैलक्रीट) की परतों को प्रदर्शित किया। उड़ती रेत शुष्क चरणों (कमजोर मानसून) का प्रतिनिधित्व करती थी, जबकि कैलक्रीट की परतें आर्द्र चरणों (मजबूत मानसून) को दर्शाती थीं। इन परतों में मिले पाषाण उपकरण विशिष्ट जलवायु चरणों में मानव उपस्थिति को साबित करते हैं।"
)

# --- 12. Teach the Concept (3 Questions) ---
add_open(sec1_en, sec1_hi, "Teach the Concept",
    "Teach the Concept: Explain the technological differences between the Soanian pebble-tool tradition and the Acheulian bifacial tradition to a beginner.",
    "अवधारणा समझाएं: सोअन बटिकाश्म-उपकरण (pebble-tool) परंपरा और एशुलेयिन द्वि-मुखी (bifacial) परंपरा के बीच तकनीकी अंतर को एक नौसिखिए को समझाएं।",
    "Think of Soanian tools as quick, simple tools made on river stones. Artisans took rounded river pebbles and struck flakes off only one side to create a sharp chopping edge (unifacial chopper). In contrast, Acheulian tools are highly planned. Artisans used quartzite blocks, chipping flakes off both sides of the stone symmetrically to produce flat, balanced handaxes and cleavers (bifaces) designed for heavy-duty tasks.",
    "सोअन उपकरणों को नदी के पत्थरों पर बने त्वरित, सरल उपकरणों के रूप में समझें। कारीगरों ने गोल पत्थरों को लिया और केवल एक तरफ से शल्क तोड़कर एक तेज धार बनाई (unifacial chopper)। इसके विपरीत, एशुलेयिन उपकरण अत्यधिक नियोजित हैं। कारीगरों ने दोनों तरफ से पत्थर के शल्क तोड़कर सममित हस्तकुठार और विदारक (bifaces) बनाए, जिन्हें भारी कार्यों के लिए उपयोग किया जाता था।"
)

add_open(sec1_en, sec1_hi, "Teach the Concept",
    "Teach the Concept: Explain the principles of Stratigraphy and the Law of Superposition using a simple household analogy.",
    "अवधारणा समझाएं: एक साधारण घरेलू सादृश्य का उपयोग करके स्तरविन्यास (Stratigraphy) और सुपरपोजिशन के नियम (Law of Superposition) के सिद्धांतों को समझाएं।",
    "Imagine a laundry basket. On Monday, you throw in dirty socks. On Wednesday, you throw in a t-shirt. On Friday, you throw in a jacket. If you don't disturb the basket, the socks from Monday are at the bottom (oldest), and the jacket from Friday is at the top (youngest). In archaeology, soil layers accumulate the same way. The oldest human tools are buried in the lowest layer, while newer tools lie in the layers above.",
    "कपड़ों की एक टोकरी की कल्पना करें। सोमवार को आप उसमें मोज़े डालते हैं। बुधवार को आप एक टी-शर्ट डालते हैं। शुक्रवार को आप एक जैकेट डालते हैं। यदि टोकरी को हिलाया न जाए, तो सोमवार के मोज़े सबसे नीचे (सबसे पुराने) होंगे, और शुक्रवार की जैकेट सबसे ऊपर (सबसे नई) होगी। पुरातत्व में भी मिट्टी की परतें इसी तरह जमा होती हैं। सबसे पुराने उपकरण सबसे निचली परत में दबे होते हैं, और नए उपकरण ऊपर की परतों में होते हैं।"
)

add_open(sec1_en, sec1_hi, "Teach the Concept",
    "Teach the Concept: Explain why Mortimer Wheeler's grid method of excavation is vital for preserving vertical soil profiles during horizontal excavations.",
    "अवधारणा समझाएं: समझाएं कि मॉर्टिमर व्हीलर की उत्खनन की ग्रिड पद्धति क्षैतिज उत्खनन के दौरान मिट्टी के ऊर्ध्वाधर प्रोफाइल को सुरक्षित रखने के लिए क्यों आवश्यक है।",
    "If you dig up a whole field flat, you lose the records of the soil walls that show the historical layers (stratigraphy). Wheeler's grid method digs in squares but leaves 1-meter thick dirt walls (baulks) between them. This creates a grid of trenches. The baulks act as standing cross-sections, allowing archaeologists to look at the soil walls in all directions and draw exactly which layer each tool came from before removing it.",
    "यदि आप पूरे मैदान को एक साथ समतल खोदते हैं, तो आप मिट्टी की परतों के आरेख खो देते हैं। व्हीलर की ग्रिड विधि वर्गाकार गड्ढे खोदती है लेकिन उनके बीच 1 मीटर चौड़ी मिट्टी की दीवारें (baulks) छोड़ देती है। ये बाल्क खड़े क्रॉस-सेक्शन के रूप में कार्य करते हैं, जिससे पुरातत्वविदों को सभी दिशाओं में मिट्टी की दीवारों को देखने और यह रिकॉर्ड करने में मदद मिलती है कि कौन सा उपकरण किस परत से निकला है।"
)
