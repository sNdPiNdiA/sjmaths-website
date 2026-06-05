from .helpers import add_mcq, add_multi_mcq, add_tf, add_blank, add_match, add_oneliner, add_ar, add_stmt, add_open

sec2_en = []
sec2_hi = []

# --- 1. MCQ (5 Questions) ---
add_mcq(sec2_en, sec2_hi,
    "The Middle Paleolithic culture in India is formally named the 'Nevasan' tradition after the site Nevasa. On the banks of which river is Nevasa situated?",
    "भारत में मध्य पुरापाषाणकालीन संस्कृति को औपचारिक रूप से नेवासा स्थल के नाम पर 'नेवासियाई' परंपरा नाम दिया गया है। नेवासा किस नदी के तट पर स्थित है?",
    ["Narmada River", "Pravara River", "Luni River", "Ghod River"],
    ["नर्मदा नदी", "प्रवरा नदी", "लूनी नदी", "घोड़ नदी"],
    1,
    "Nevasa is the type site of the Middle Paleolithic flake industry, excavated by H.D. Sankalia on the banks of the Pravara River, a major tributary of the Godavari in Maharashtra.",
    "नेवासा मध्य पुरापाषाणकालीन शल्क उद्योग का प्रमुख स्थल है, जिसका उत्खनन एच.डी. संकलिया द्वारा महाराष्ट्र में गोदावरी की एक प्रमुख सहायक नदी प्रवरा के तट पर किया गया था।"
)

add_mcq(sec2_en, sec2_hi,
    "What technological transition marks the boundary between the Lower Paleolithic and Middle Paleolithic in India?",
    "भारत में निम्न पुरापाषाण और मध्य पुरापाषाण काल के बीच की सीमा को कौन सा तकनीकी बदलाव चिह्नित करता है?",
    ["Shift from chert to iron tools", "Shift from large core tools to smaller flake tools made on prepared cores", "Emergence of bone tools and microliths", "First creation of painted rock art shelters"],
    ["चर्ट से लोहे के औजारों में बदलाव", "बड़े कोर उपकरणों से तैयार कोर पर बने छोटे शल्क उपकरणों (flake tools) में बदलाव", "हड्डी के औजारों और सूक्ष्म-पाषाणों (microliths) का उदय", "चित्रित शैल कला गुफाओं का पहला निर्माण"],
    1,
    "The Middle Paleolithic is characterized by flake tools (scrapers, borers, points) struck from prepared cores (Levallois technique), replacing large bifaces like handaxes.",
    "मध्य पुरापाषाण काल की विशेषता तैयार कोर (लेवालोइस तकनीक) से तोड़े गए शल्क उपकरण (खुरचनी, वेधक, शूल) हैं, जिन्होंने हस्तकुठार जैसे बड़े उपकरणों का स्थान लिया।"
)

add_mcq(sec2_en, sec2_hi,
    "Which of the following raw materials represents the dominant shift in lithic technology during the Middle Paleolithic phase in India?",
    "भारत में मध्य पुरापाषाण चरण के दौरान पाषाण तकनीक में मुख्य बदलाव को निम्नलिखित में से कौन सा कच्चा माल दर्शाता है?",
    ["Basalt", "Quartzite", "Chert and Jasper", "Limestone"],
    ["बेसाल्ट", "क्वार्ट्जाइट", "चर्ट और जैस्पर (Chert and Jasper)", "चूना पत्थर"],
    2,
    "Hominins shifted from coarse-grained quartzite to fine-grained cryptocrystalline silica stones like chert, jasper, chalcedony, and agate for smaller tools.",
    "छोटे उपकरणों के निर्माण के लिए आदिम मानवों ने मोटे क्वार्ट्जाइट से महीन सिलिका पत्थरों जैसे चर्ट, जैस्पर, चाल्सीडोनी और अगेट की ओर रुख किया।"
)

add_mcq(sec2_en, sec2_hi,
    "The préparateur-core flake tools of the Middle Paleolithic were first systematically categorized in India by which archaeologist?",
    "मध्य पुरापाषाण काल के तैयार-कोर शल्क उपकरणों को भारत में सबसे पहले किस पुरातत्वविद द्वारा व्यवस्थित रूप से वर्गीकृत किया गया था?",
    ["V.S. Wakankar", "Robert Bruce Foote", "H.D. Sankalia", "Mortimer Wheeler"],
    ["वी.एस. वाकणकर", "रॉबर्ट ब्रूस फुट", "एच.डी. सांकलिया", "मॉर्टिमर व्हीलर"],
    2,
    "Dr. H.D. Sankalia defined and categorized the Middle Paleolithic stone tool industry based on his excavations at Nevasa (Maharashtra).",
    "डॉ. एच.डी. सांकलिया ने नेवासा (महाराष्ट्र) में अपने उत्खनन के आधार पर मध्य पुरापाषाणकालीन पत्थर के उपकरणों के उद्योगों को परिभाषित और वर्गीकृत किया।"
)

add_mcq(sec2_en, sec2_hi,
    "Which specific flake tool type was primarily designed for cleaning animal skins or shaping wooden shafts during the Middle Paleolithic?",
    "मध्य पुरापाषाण काल के दौरान जानवरों की खाल साफ करने या लकड़ी के डंडों को आकार देने के लिए मुख्य रूप से किस विशिष्ट शल्क उपकरण प्रकार का उपयोग किया जाता था?",
    ["Borer", "Point", "Scraper", "Cleaver"],
    ["वेधक", "शूल (Point)", "खुरचनी (Scraper)", "विदारक"],
    2,
    "Scrapers feature retouched sharp edges designed for scraping meat from hides, smoothing wooden shafts, or cutting plant tissues.",
    "खुरचनी (scrapers) में तीखे किनारे होते हैं जिन्हें जानवरों की खाल से मांस साफ करने, लकड़ी को चिकना करने या पौधों के रेशों को काटने के लिए बनाया जाता था।"
)

# --- 2. Multiple Correct MCQ (5 Questions) ---
add_multi_mcq(sec2_en, sec2_hi,
    "Which of the following stone tool types are diagnostic of the Indian Middle Paleolithic flake tool assemblage? (Select all that apply)",
    "निम्नलिखित में से कौन से पाषाण उपकरण प्रकार भारतीय मध्य पुरापाषाणकालीन शल्क उपकरण समूह की पहचान हैं? (सभी सही विकल्प चुनें)",
    ["Scrapers (side, end, and round)", "Borers or piercing tools", "Point tools", "Large cleavers and handaxes"],
    ["खुरचनी (पार्श्व, छोर और गोल खुरचनी)", "वेधक (Borer) या चुभने वाले उपकरण", "शूल (Point) उपकरण", "बड़े विदारक (cleavers) और हस्तकुठार"],
    [0, 1, 2],
    "Middle Paleolithic assemblages are dominated by scrapers, borers, and points made on flakes. Large handaxes and cleavers disappear or become extremely rare.",
    "मध्य पुरापाषाणकालीन उपकरण समूहों में शल्क पर बनी खुरचनी, वेधक और शूल (points) की प्रधानता होती है। बड़े हस्तकुठार और विदारक गायब हो जाते हैं या अत्यंत दुर्लभ हो जाते हैं।"
)

add_multi_mcq(sec2_en, sec2_hi,
    "Which of the following fine-grained materials replaced coarse quartzite during the Middle Paleolithic tool-making phase? (Select all that apply)",
    "मध्य पुरापाषाणकालीन उपकरण निर्माण चरण के दौरान निम्नलिखित में से किन महीन कणों वाले पदार्थों ने मोटे क्वार्ट्जाइट का स्थान लिया? (सभी सही विकल्प चुनें)",
    ["Chert", "Jasper", "Chalcedony", "Sandstone"],
    ["चर्ट (Chert)", "जैस्पर (Jasper)", "चाल्सीडोनी (Chalcedony)", "बलुआ पत्थर (Sandstone)"],
    [0, 1, 2],
    "Middle Paleolithic toolmakers preferred cryptocrystalline silica rocks such as chert, jasper, chalcedony, and agate because they fracture more cleanly and allow sharper edges on smaller tools.",
    "मध्य पुरापाषाणकालीन शिल्पकार चर्ट, जैस्पर, चाल्सीडोनी और अगेट जैसे महीन पत्थरों को प्राथमिकता देते थे क्योंकि वे अधिक सफाई से टूटते हैं और छोटे उपकरणों पर अधिक धारदार किनारे देते हैं।"
)

add_multi_mcq(sec2_en, sec2_hi,
    "Which of the following archaeological sites contain stratified Middle Paleolithic sequences in India? (Select all that apply)",
    "भारत में निम्नलिखित में से किन पुरातात्विक स्थलों में स्तरबद्ध मध्य पुरापाषाणकालीन अनुक्रम मिलते हैं? (सभी सही विकल्प चुनें)",
    ["Nevasa in Maharashtra", "Bhimbetka in Madhya Pradesh", "Didwana in Rajasthan", "Mehrgarh in Balochistan"],
    ["महाराष्ट्र में नेवासा", "मध्य प्रदेश में भीमबेटका", "राजस्थान में डीडवाना", "बलूचिस्तान में मेहरगढ़"],
    [0, 1, 2],
    "Nevasa, Bhimbetka, and Didwana show rich Middle Paleolithic tool layers. Mehrgarh is a Neolithic farming village with no Paleolithic sequence.",
    "नेवासा, भीमबेटका और डीडवाना में समृद्ध मध्य पुरापाषाणकालीन उपकरण परतें मिलती हैं। मेहरगढ़ एक नवपाषाण गाँव है जहाँ पुरापाषाण अनुक्रम नहीं है।"
)

add_multi_mcq(sec2_en, sec2_hi,
    "Which of the following techniques were associated with prepared-core flake detachment in the Middle Paleolithic? (Select all that apply)",
    "मध्य पुरापाषाण काल में तैयार-कोर शल्क पृथक्करण (prepared-core flake detachment) से निम्नलिखित में से कौन सी तकनीकें जुड़ी थीं? (सभी सही विकल्प चुनें)",
    ["Levallois technique", "Prepared core shaping", "Direct percussion with hard hammers", "Polishing and grinding on sandstone"],
    ["लेवालोइस (Levallois) तकनीक", "तैयार कोर को आकार देना", "कठोर हथौड़े से सीधा प्रहार", "बलुआ पत्थर पर पॉलिश और घिसाई"],
    [0, 1, 2],
    "Prepared cores and Levallois techniques involve hard hammer percussion to detach planned flakes. Polishing and grinding are Neolithic tool technologies.",
    "तैयार कोर और लेवालोइस तकनीकों में शल्क निकालने के लिए हथौड़े से सीधे प्रहार किया जाता था। पॉलिश और घिसाई नवपाषाण काल की तकनीकें हैं।"
)

add_multi_mcq(sec2_en, sec2_hi,
    "Which of the following river basins show significant clusters of Middle Paleolithic sites in Peninsular India? (Select all that apply)",
    "प्रायद्वीपीय भारत में निम्नलिखित में से किस नदी बेसिन में मध्य पुरापाषाणकालीन स्थलों के महत्वपूर्ण समूह मिलते हैं? (सभी सही विकल्प चुनें)",
    ["Godavari-Pravara basin", "Krishna River basin", "Narmada River basin", "Ganga-Yamuna Alluvium"],
    ["गोदावरी-प्रवरा बेसिन", "कृष्णा नदी बेसिन", "नर्मदा नदी बेसिन", "गंगा-यमुना जलोढ़"],
    [0, 1, 2],
    "Godavari-Pravara (Nevasa), Krishna, and Narmada river basins are rich in Middle Paleolithic sites. Ganga-Yamuna lacks stone outcrops and Paleolithic occupations.",
    "गोदावरी-प्रवरा (नेवासा), कृष्णा और नर्मदा नदी घाटियाँ मध्य पुरापाषाण स्थलों से समृद्ध हैं। गंगा-यमुना जलोढ़ मैदानों में पत्थरों के अभाव के कारण यहाँ बस्तियाँ नहीं थीं।"
)

# --- 3. True/False (8 Questions) ---
add_tf(sec2_en, sec2_hi,
    "Did the prepared core technique (resembling the Levallois method of Europe) exist in the Middle Paleolithic cultures of the Luni Valley in Rajasthan?",
    "क्या राजस्थान की लूनी घाटी की मध्य पुरापाषाणकालीन संस्कृतियों में तैयार कोर तकनीक (जो यूरोप की लेवालोइस पद्धति जैसी है) मौजूद थी?",
    True,
    "True. Excavations in the Luni Valley and Didwana have recovered prepared cores and Levallois flakes, showing advanced planning techniques.",
    "सत्य। लूनी घाटी और डीडवाना में उत्खनन से तैयार कोर और लेवालोइस शल्क बरामद हुए हैं, जो उन्नत नियोजन तकनीकों को प्रदर्शित करते हैं।"
)

add_tf(sec2_en, sec2_hi,
    "Hominins completely abandoned quartzite in all Indian Middle Paleolithic sites without exception.",
    "आदिम मानवों ने बिना किसी अपवाद के भारत के सभी मध्य पुरापाषाण स्थलों पर क्वार्ट्जाइट का उपयोग पूरी तरह से बंद कर दिया था।",
    False,
    "False. While most sites shifted to chert, local fine-grained quartzite was still utilized at sites like Bhimbetka due to local abundance.",
    "गलत। अधिकांश स्थलों पर चर्ट का उपयोग शुरू हो गया था, लेकिन भीमबेटका जैसे स्थलों पर स्थानीय प्रचुरता के कारण स्थानीय महीन क्वार्ट्जाइट का उपयोग जारी रहा।"
)

add_tf(sec2_en, sec2_hi,
    "Scrapers are the dominant flake tool types in Middle Paleolithic toolkits, showing various retouched edges.",
    "मध्य पुरापाषाणकालीन उपकरण किटों में खुरचनी (scrapers) सबसे प्रमुख शल्क उपकरण प्रकार हैं, जो विभिन्न प्रकार के धारदार किनारों को दर्शाते हैं।",
    True,
    "True. Scrapers (side, end, round) dominate the Nevasan assemblages and were used for scraping hides, plant matter, and wood.",
    "सत्य। नेवासियाई उपकरण समूहों में खुरचनी (पार्श्व, छोर, गोल) की प्रधानता है, इनका उपयोग खाल, पौधों और लकड़ी को खुरचने के लिए किया जाता था।"
)

add_tf(sec2_en, sec2_hi,
    "The Middle Paleolithic occupations at Didwana occur in the same sandy horizons as the earliest Lower Paleolithic tools.",
    "डीडवाना में मध्य पुरापाषाणकालीन मानव बस्तियाँ उन्हीं रेतीले क्षेत्रों में मिलती हैं जहाँ सबसे शुरुआती निम्न पुरापाषाणकालीन उपकरण मिले थे।",
    False,
    "False. Middle Paleolithic tools occur in younger stratigraphic layers (stabilized soil horizons) higher up in the Didwana sequence compared to Lower Paleolithic tools.",
    "गलत। डीडवाना के स्तरविन्यास में निम्न पुरापाषाणकालीन उपकरणों की तुलना में मध्य पुरापाषाणकालीन उपकरण ऊपर की नई परतों में मिलते हैं।"
)

add_tf(sec2_en, sec2_hi,
    "H.D. Sankalia discovered the Middle Paleolithic layers at Nevasa directly overlying Chalcolithic Jorwe culture layers.",
    "एच.डी. सांकलिया ने नेवासा में ताम्रपाषाण कालीन जोर्वे संस्कृति की परतों के ठीक ऊपर मध्य पुरापाषाण काल की परतों की खोज की थी।",
    False,
    "False. The Middle Paleolithic layers lie at the bottom in the gravel beds of the river, while Chalcolithic layers are situated far above in the upper mound levels.",
    "गलत। मध्य पुरापाषाणकालीन परतें नदी के निचले बजरी बेड में हैं, जबकि ताम्रपाषाण कालीन परतें टीले के ऊपरी हिस्से में बहुत ऊपर स्थित हैं।"
)

add_tf(sec2_en, sec2_hi,
    "The Luni River valley in western Rajasthan was a major locus of Middle Paleolithic tool manufacturing sites.",
    "पश्चिमी राजस्थान में लूनी नदी घाटी मध्य पुरापाषाणकालीन उपकरण निर्माण स्थलों का एक प्रमुख केंद्र थी।",
    True,
    "True. Extensive surveys by V.N. Misra revealed dense concentrations of Middle Paleolithic flake workshops in the Luni Valley.",
    "सत्य। वी.एन. मिश्रा द्वारा किए गए व्यापक सर्वेक्षणों से लूनी घाटी में मध्य पुरापाषाणकालीन शल्क कार्यशालाओं के सघन जमाव का पता चला है।"
)

add_tf(sec2_en, sec2_hi,
    "Cryptocrystalline silica rocks like chert show predictable conchoidal fractures, which made them ideal for producing smaller flakes.",
    "चर्ट जैसे सूक्ष्म-कण सिलिका पत्थरों में निश्चित कॉनकॉइडल दरारें (conchoidal fractures) होती हैं, जिसने उन्हें छोटे शल्क बनाने के लिए आदर्श बनाया।",
    True,
    "True. The fine-grained homogeneous structure of chert fractures cleanly, allowing precise tool knapping.",
    "सत्य। चर्ट की महीन कणों वाली समरूप संरचना बहुत सफाई से टूटती है, जिससे सटीक उपकरण बनाना आसान हो जाता है।"
)

add_tf(sec2_en, sec2_hi,
    "A prepared core is discarded immediately without striking off any flakes, representing a symbolic ritual object.",
    "एक तैयार कोर को बिना कोई शल्क निकाले तुरंत फेंक दिया जाता था, जो एक प्रतीकात्मक अनुष्ठानिक वस्तु का प्रतिनिधित्व करता था।",
    False,
    "False. A prepared core is carefully shaped specifically to strike off pre-planned flakes of controlled sizes for tool production.",
    "गलत। तैयार कोर को उपकरण बनाने के लिए पूर्व-नियोजित आकारों के शल्क निकालने के उद्देश्य से ही सावधानीपूर्वक आकार दिया जाता था।"
)

# --- 4. Fill in the Blank (8 Questions) ---
add_blank(sec2_en, sec2_hi,
    "The Middle Paleolithic type-site Nevasa is located on the banks of the ________ River, a tributary of the Godavari.",
    "मध्य पुरापाषाणकालीन प्रमुख स्थल नेवासा गोदावरी की सहायक नदी ________ नदी के तट पर स्थित है।",
    "Pravara", "प्रवरा",
    "Nevasa is located on the Pravara River in Ahmednagar district of Maharashtra.",
    "नेवासा महाराष्ट्र के अहमदनगर जिले में प्रवरा नदी के तट पर स्थित है।"
)

add_blank(sec2_en, sec2_hi,
    "The Middle Paleolithic tool industry in India was systematically excavated and defined by Professor ________.",
    "भारत में मध्य पुरापाषाणकालीन उपकरण उद्योग का व्यवस्थित रूप से उत्खनन और परिभाषा प्रोफेसर ________ द्वारा की गई थी।",
    "H.D. Sankalia", "एच.डी. सांकलिया",
    "H.D. Sankalia defined the Nevasan tradition of Middle Paleolithic flake industries.",
    "एच.डी. सांकलिया ने मध्य पुरापाषाणकालीन शल्क उद्योगों की नेवासियाई परंपरा को परिभाषित किया था।"
)

add_blank(sec2_en, sec2_hi,
    "Fine-grained rocks like ________ and jasper replaced quartzite as primary raw materials in the Middle Paleolithic.",
    "मध्य पुरापाषाण काल में प्राथमिक कच्चे माल के रूप में क्वार्ट्जाइट का स्थान ________ और जैस्पर जैसे महीन पत्थरों ने ले लिया।",
    "chert", "चर्ट",
    "Chert and jasper were the preferred cryptocrystalline silica stones for Middle Paleolithic tools.",
    "मध्य पुरापाषाणकालीन उपकरणों के लिए चर्ट और जैस्पर सबसे पसंदीदा सिलिका पत्थर थे।"
)

add_blank(sec2_en, sec2_hi,
    "A flake tool with a retouched pointed projection designed to drill holes is called a ________.",
    "छेद करने के लिए बनाई गई शल्क पर तराशी गई नुकीली नोक वाला उपकरण ________ कहलाता है।",
    "borer", "वेधक",
    "Borers (or drills) were used to pierce wood, bone, or leather skins.",
    "वेधकों (borers) का उपयोग लकड़ी, हड्डी या चमड़े की खाल में छेद करने के लिए किया जाता था।"
)

add_blank(sec2_en, sec2_hi,
    "The method where a stone core is shaped to control the size and form of the detached flake is called the ________ core technique.",
    "वह विधि जिसमें अलग किए जाने वाले शल्क के आकार और रूप को नियंत्रित करने के लिए पत्थर के कोर को पहले आकार दिया जाता है, ________ कोर तकनीक कहलाती है।",
    "prepared", "तैयार",
    "Prepared core techniques (such as Levallois) represent advanced pre-planning in tool manufacture.",
    "तैयार कोर तकनीक (जैसे लेवालोइस) उपकरण निर्माण में उन्नत योजना का प्रतिनिधित्व करती है।"
)

add_blank(sec2_en, sec2_hi,
    "At Bhimbetka, Middle Paleolithic tool layers occur directly above the Lower Paleolithic ________ layers.",
    "भीमबेटका में, मध्य पुरापाषाणकालीन उपकरण परतें सीधे निम्न पुरापाषाणकालीन ________ परतों के ऊपर मिलती हैं।",
    "Acheulian", "एशुलेयिन",
    "The stratigraphic sequence shows Middle Paleolithic flake tools overlying Acheulian handaxes.",
    "यहाँ का स्तरविन्यास अनुक्रम एशुलेयिन हस्तकुठारों के ऊपर मध्य पुरापाषाणकालीन शल्क उपकरणों को दर्शाता है।"
)

add_blank(sec2_en, sec2_hi,
    "The Luni Valley, rich in Middle Paleolithic open-air sites, is located in the state of ________.",
    "मध्य पुरापाषाणकालीन खुले स्थलों से समृद्ध लूनी घाटी ________ राज्य में स्थित है।",
    "Rajasthan", "राजस्थान",
    "The Luni Valley is located in western Rajasthan, displaying extensive Middle Paleolithic workshop concentrations.",
    "लूनी घाटी पश्चिमी राजस्थान में स्थित है, जहाँ मध्य पुरापाषाणकालीन कार्यशालाओं के सघन जमाव मिलते हैं।"
)

add_blank(sec2_en, sec2_hi,
    "A flake tool with a sharp pointed tip, likely hafted to a wooden shaft to serve as a spearhead, is called a ________.",
    "एक नुकीली नोक वाला शल्क उपकरण, जिसे भाले की नोक के रूप में लकड़ी के डंडे पर लगाया जाता था, ________ कहलाता है।",
    "point", "शूल",
    "Points were triangular flakes retouched to form sharp tips for hunting projectiles.",
    "शूल (points) त्रिकोणीय शल्क होते थे जिन्हें शिकार के लिए तीखे सिरे प्रदान करने हेतु तराशा जाता था।"
)

# --- 5. Match the Following (4 Questions) ---
add_match(sec2_en, sec2_hi,
    "Match the Middle Paleolithic site with its diagnostic geographical location:",
    "मध्य पुरापाषाणकालीन स्थल को उसके विशिष्ट भौगोलिक स्थान से सुमेलित करें:",
    ["1. Nevasa", "2. Didwana", "3. Bhimbetka", "4. Luni Valley"],
    ["1. नेवासा", "2. डीडवाना", "3. भीमबेटका", "4. लूनी घाटी"],
    ["A. Raisen District, MP", "B. Ahmednagar District, Maharashtra", "C. Nagaur District, Rajasthan", "D. Western Rajasthan Desert Margin"],
    ["A. रायसेन जिला, मध्य प्रदेश", "B. अहमदनगर जिला, महाराष्ट्र", "C. नागौर जिला, राजस्थान", "D. पश्चिमी राजस्थान मरुस्थल का किनारा"],
    "1-B, 2-C, 3-A, 4-D", "1-B, 2-C, 3-A, 4-D"
)

add_match(sec2_en, sec2_hi,
    "Match the stone tool type with its primary archaeological function:",
    "पत्थर के उपकरण के प्रकार को उसके प्राथमिक पुरातात्विक कार्य से सुमेलित करें:",
    ["1. Scraper", "2. Borer", "3. Point", "4. Handaxe"],
    ["1. खुरचनी (Scraper)", "2. वेधक (Borer)", "3. शूल (Point)", "4. हस्तकुठार (Handaxe)"],
    ["A. Drilling holes in hides or wood", "B. Scraping animal skins and plant fibers", "C. Multi-purpose heavy chopping/digging", "D. Hunting projectile tip (spearhead)"],
    ["A. खाल या लकड़ी में छेद करना", "B. जानवरों की खाल और पौधों के रेशों को खुरचना", "C. बहुउद्देशीय भारी काटना/खोदना", "D. शिकार के लिए प्रक्षेप्य नोक (भाले का सिरा)"],
    "1-B, 2-A, 3-D, 4-C", "1-B, 2-A, 3-D, 4-C"
)

add_match(sec2_en, sec2_hi,
    "Match the River with the associated Middle Paleolithic site situated in its basin:",
    "नदी को उसके बेसिन में स्थित संबंधित मध्य पुरापाषाणकालीन स्थल से सुमेलित करें:",
    ["1. Pravara River", "2. Narmada River", "3. Luni River", "4. Belan River"],
    ["1. प्रवरा नदी", "2. नर्मदा नदी", "3. लूनी नदी", "4. बेलन नदी"],
    ["A. Hathnora", "B. Nevasa", "C. Chopani Mando", "D. Samnapur"],
    ["A. हथनोरा", "B. नेवासा", "C. चोपानी मांडो", "D. समनापुर"],
    "1-B, 2-A, 3-D, 4-C", "1-B, 2-A, 3-D, 4-C"
)

add_match(sec2_en, sec2_hi,
    "Match the archaeologist with their key contribution to Middle Paleolithic studies:",
    "पुरातत्वविद को मध्य पुरापाषाणकालीन अध्ययनों में उनके प्रमुख योगदान से सुमेलित करें:",
    ["1. H.D. Sankalia", "2. V.N. Misra", "3. V.S. Wakankar", "4. G.R. Sharma"],
    ["1. एच.डी. सांकलिया", "2. वी.एन. मिश्रा", "3. वी.एस. वाकणकर", "4. जी.आर. शर्मा"],
    ["A. Reconstructed Vindhyan cave sequences", "B. Excavated Belan Valley sequences", "C. Defined the Nevasan tradition", "D. Surveyed Luni Valley flake industries"],
    ["A. विंध्यन गुफा अनुक्रमों का पुनर्निर्माण किया", "B. बेलन घाटी अनुक्रमों का उत्खनन किया", "C. नेवासियाई परंपरा को परिभाषित किया", "D. लूनी घाटी शल्क उद्योगों का सर्वेक्षण किया"],
    "1-C, 2-D, 3-A, 4-B", "1-C, 2-D, 3-A, 4-B"
)

# --- 6. One-Liner (8 Questions) ---
add_oneliner(sec2_en, sec2_hi,
    "Define a 'scraper' in Middle Paleolithic tool technology.",
    "मध्य पुरापाषाणकालीन उपकरण तकनीक में 'खुरचनी' (scraper) को परिभाषित करें।",
    "A flake tool featuring retouched, sharp working edges along its sides or ends, used for cleaning hides or shaving wood.",
    "शल्क पर बना एक उपकरण जिसके किनारों या छोरों पर धारदार काम करने वाले किनारे तराशे गए होते हैं, इसका उपयोग खाल साफ करने या लकड़ी छीलने के लिए किया जाता था।"
)

add_oneliner(sec2_en, sec2_hi,
    "What is a 'prepared core' in lithic technology?",
    "पाषाण तकनीक में 'तैयार कोर' (prepared core) क्या है?",
    "A stone block carefully shaped by removing flakes from its face to control the form of the final flake tool detached from it.",
    "पत्थर का एक खंड जिसे उसकी सतह से शल्क निकालकर सावधानीपूर्वक आकार दिया जाता है ताकि उससे निकाले जाने वाले अंतिम उपकरण का आकार नियंत्रित किया जा सके।"
)

add_oneliner(sec2_en, sec2_hi,
    "What is the function of a prehistoric 'awl'?",
    "प्रागैतिहासिक 'आरी' (awl) का कार्य क्या है?",
    "A pointed tool used to pierce tiny holes in leather skins or sew together plant fibers and animal hides.",
    "एक नुकीला उपकरण जिसका उपयोग चमड़े की खाल में छोटे छेद करने या पौधों के रेशों और जानवरों की खाल को सिलने के लिए किया जाता था।"
)

add_oneliner(sec2_en, sec2_hi,
    "Where is the type-site St. Acheul located, which defined the Lower Paleolithic, and where is the Levallois type-site located?",
    "निम्न पुरापाषाण काल को परिभाषित करने वाला प्रकार-स्थल सेंट एशुल कहाँ स्थित है, और लेवालोइस प्रकार-स्थल कहाँ स्थित है?",
    "Both St. Acheul and Levallois-Perret are located in France; the latter defined the prepared-core technique.",
    "सेंट एशुल और लेवालोइस-पेरेट दोनों फ्रांस में स्थित हैं; लेवालोइस ने तैयार-कोर तकनीक को परिभाषित किया था।"
)

add_oneliner(sec2_en, sec2_hi,
    "What is meant by the 'Nevasan tradition' in Indian prehistory?",
    "भारतीय प्रागैतिहास में 'नेवासियाई परंपरा' से क्या तात्पर्य है?",
    "It refers to the Middle Paleolithic flake tool tradition named after the type-site Nevasa, dominated by scrapers and points.",
    "यह नेवासा प्रमुख स्थल के नाम पर रखी गई मध्य पुरापाषाणकालीन शल्क उपकरण परंपरा को संदर्भित करता है, जिसमें खुरचनी और शूल की प्रधानता है।"
)

add_oneliner(sec2_en, sec2_hi,
    "Why did Middle Paleolithic artisans prefer fine-grained chert over coarse quartzite?",
    "मध्य पुरापाषाणकालीन कारीगरों ने मोटे क्वार्ट्जाइट की तुलना में महीन चर्ट को क्यों प्राथमिकता दी?",
    "Because chert's microcrystalline structure allowed predictable, clean fracturing, yielding sharper and more standardized edges on smaller tools.",
    "क्योंकि चर्ट की महीन कणों वाली संरचना अधिक निश्चित और साफ टूटती थी, जिससे छोटे उपकरणों पर अधिक धारदार और मानकीकृत किनारे बनाना संभव था।"
)

add_oneliner(sec2_en, sec2_hi,
    "State the significance of the Luni Valley for Middle Paleolithic research in India.",
    "भारत में मध्य पुरापाषाणकालीन अनुसंधान के लिए लूनी घाटी के महत्व को बताएं।",
    "It represents a major concentration of open-air habitation-cum-factory sites showing adaptation to desert margins in western India.",
    "यह पश्चिमी भारत में मरुस्थलीय किनारों के प्रति अनुकूलन को दर्शाने वाले खुले निवास-सह-कारखाना स्थलों के बड़े जमाव का प्रतिनिधित्व करता है।"
)

add_oneliner(sec2_en, sec2_hi,
    "Define a 'point tool' in the context of Middle Paleolithic hunting technology.",
    "मध्य पुरापाषाणकालीन शिकार तकनीक के संदर्भ में 'शूल उपकरण' (point tool) को परिभाषित करें।",
    "A triangular flake tool retouched to form a sharp tip, likely attached to a wooden shaft to serve as a spearhead.",
    "एक त्रिकोणीय शल्क उपकरण जिसे एक तेज सिरा देने के लिए तराशा जाता था, इसे भाले की नोक के रूप में लकड़ी के डंडे से जोड़ा जाता था।"
)

# --- 7. Assertion-Reason (8 Questions) ---
add_ar(sec2_en, sec2_hi,
    "Assertion (A): Hominins in the Middle Paleolithic shifted from coarse quartzite to cryptocrystalline rocks like chert.\nReason (R): Cryptocrystalline stones fracture cleanly, enabling the manufacture of smaller, thinner, and highly retouched flake tools.",
    "कथन (A): मध्य पुरापाषाण काल में आदिम मानवों ने मोटे क्वार्ट्जाइट से चर्ट जैसे महीन पत्थरों की ओर रुख किया।\nकारण (R): महीन सिलिका पत्थर साफ टूटते हैं, जिससे छोटे, पतले और अत्यधिक तराशे गए शल्क उपकरण बनाना संभव हो जाता है।",
    0,
    "Both A and R are true and R is the correct explanation of A. Material shift was driven by technological needs for small flake tools.",
    "A और R दोनों सही हैं और R, A की सही व्याख्या करता है। कच्चे माल का बदलाव छोटे शल्क उपकरणों के निर्माण की तकनीकी आवश्यकताओं से प्रेरित था।"
)

add_ar(sec2_en, sec2_hi,
    "Assertion (A): Scrapers are the most abundant and diagnostic tool type of the Indian Middle Paleolithic.\nReason (R): Middle Paleolithic economies relied heavily on processing animal skins, wood, and plant fibers using scraping tools.",
    "कथन (A): खुरचनी (scrapers) भारतीय मध्य पुरापाषाण काल के सबसे प्रचुर और विशिष्ट उपकरण प्रकार हैं।\nकारण (R): मध्य पुरापाषाणकालीन अर्थव्यवस्थाएं खुरचने वाले उपकरणों का उपयोग करके जानवरों की खाल, लकड़ी और पौधों के रेशों को संसाधित करने पर अत्यधिक निर्भर थीं।",
    0,
    "Both A and R are true and R is the correct explanation of A. The tool frequency directly reflects the economic activities of hominins.",
    "A और R दोनों सही हैं और R, A की सही व्याख्या करता है। उपकरणों की प्रचुरता सीधे आदिम मानवों की आर्थिक गतिविधियों को दर्शाती है।"
)

add_ar(sec2_en, sec2_hi,
    "Assertion (A): The prepared core (Levallois) technique represents a major cognitive development in tool manufacture.\nReason (R): Hominins had to visualize the final shape and size of the flake before striking it off from the parent block of stone.",
    "कथन (A): तैयार कोर (लेवालोइस) तकनीक उपकरण निर्माण में एक बड़े संज्ञानात्मक विकास का प्रतिनिधित्व करती है।\nकारण (R): आदिम मानवों को मूल पत्थर के खंड से शल्क निकालने से पहले उसके अंतिम आकार और रूप की कल्पना करनी पड़ती थी।",
    0,
    "Both A and R are true and R is the correct explanation of A. Pre-planning is the core cognitive element of the Levallois technique.",
    "A और R दोनों सही हैं और R, A की सही व्याख्या करता है। पूर्व-नियोजन लेवालोइस तकनीक का मुख्य संज्ञानात्मक तत्व है।"
)

add_ar(sec2_en, sec2_hi,
    "Assertion (A): The stratigraphic profile at Nevasa shows an unbroken sequence from the Lower Paleolithic to the Chalcolithic Jorwe period.\nReason (R): Nevasa river terraces represent a geological catchment area that accumulated deposits over hundreds of thousands of years.",
    "कथन (A): नेवासा में स्तरविन्यास प्रोफाइल निम्न पुरापाषाण से लेकर ताम्रपाषाण जोर्वे काल तक का एक अटूट क्रम दिखाता है।\nकारण (R): नेवासा नदी की घाटियाँ एक भूवैज्ञानिक जलग्रहण क्षेत्र का प्रतिनिधित्व करती हैं जिसने लाखों वर्षों में जमाव संचित किया।",
    0,
    "Both A and R are true and R is the correct explanation of A. The river gravels capture continuous cultural evolution in the Deccan.",
    "A और R दोनों सही हैं और R, A की सही व्याख्या करता है। नदी की बजरी दक्कन में निरंतर सांस्कृतिक विकास को संजोए हुए है।"
)

add_ar(sec2_en, sec2_hi,
    "Assertion (A): Middle Paleolithic sites are completely absent from western Rajasthan.\nReason (R): The Luni Valley displays dense concentrations of Middle Paleolithic workshops made on chert and jasper.",
    "कथन (A): पश्चिमी राजस्थान में मध्य पुरापाषाणकालीन स्थल पूरी तरह से अनुपस्थित हैं।\nकारण (R): लूनी घाटी चर्ट और जैस्पर से बनी मध्य पुरापाषाणकालीन कार्यशालाओं के सघन जमाव को प्रदर्शित करती है।",
    3,
    "A is false but R is true. Western Rajasthan contains many sites, specifically along the Luni River basin.",
    "A गलत है लेकिन R सही है। पश्चिमी राजस्थान में कई स्थल मिलते हैं, विशेष रूप से लूनी नदी बेसिन के किनारे।"
)

add_ar(sec2_en, sec2_hi,
    "Assertion (A): Chert tool edges could easily be retouched to renew their sharpness.\nReason (R): Quartzite is a metamorphic rock that cannot be retouched under any circumstances.",
    "कथन (A): चर्ट के उपकरणों के किनारों को उनकी धार तेज करने के लिए आसानी से सुधारा (retouch) जा सकता था।\nकारण (R): क्वार्ट्जाइट एक कायांतरित (metamorphic) पत्थर है जिसे किसी भी स्थिति में सुधारा नहीं जा सकता।",
    2,
    "A is true but R is false. Quartzite can be and was retouched, as seen in Lower Paleolithic Acheulian tools; chert is just easier to retouch precisely.",
    "A सही है लेकिन R गलत है। क्वार्ट्जाइट को भी सुधारा जा सकता था, जैसा कि निम्न पुरापाषाणकालीन उपकरणों में देखा जाता है; चर्ट को केवल अधिक सटीकता से सुधारा जा सकता था।"
)

add_ar(sec2_en, sec2_hi,
    "Assertion (A): Awls and borers were vital for Middle Paleolithic adaptation to cold and dry environments.\nReason (R): Piercing tools allowed hominins to make holes in animal hides to tie them together as protective body coverings.",
    "कथन (A): मध्य पुरापाषाण काल में ठंडे और शुष्क वातावरण के अनुकूल ढलने के लिए आरी (awls) और वेधक (borers) अत्यंत महत्वपूर्ण थे।\nकारण (R): चुभने वाले उपकरणों ने आदिम मानवों को शरीर को ढकने वाले सुरक्षात्मक आवरण के रूप में जोड़ने के लिए जानवरों की खाल में छेद करने की अनुमति दी।",
    0,
    "Both A and R are true and R is the correct explanation of A. Clothing manufacture was enabled by piercing tools.",
    "A और R दोनों सही हैं और R, A की सही व्याख्या करता है। शरीर को ढकने वाले सुरक्षात्मक आवरण का निर्माण चुभने वाले उपकरणों द्वारा संभव हुआ था।"
)

add_ar(sec2_en, sec2_hi,
    "Assertion (A): Prepared cores were exported over hundreds of miles by Middle Paleolithic trade networks.\nReason (R): Raw chert was highly abundant in the Deccan volcanic plateau, making transport unnecessary.",
    "कथन (A): मध्य पुरापाषाणकालीन व्यापारिक नेटवर्कों द्वारा तैयार कोर का सैकड़ों मील दूर तक निर्यात किया जाता था।\nकारण (R): दक्कन के ज्वालामुखी पठार में कच्चा चर्ट अत्यधिक प्रचुरता में उपलब्ध था, जिससे परिवहन की आवश्यकता नहीं थी।",
    3,
    "A is false but R is true. There is no evidence of trade networks in the Middle Paleolithic; hominins utilized local resources directly.",
    "A गलत है लेकिन R सही है। मध्य पुरापाषाण काल में व्यापारिक नेटवर्कों के कोई साक्ष्य नहीं मिले हैं; आदिम मानव सीधे स्थानीय संसाधनों का उपयोग करते थे।"
)

# --- 8. Statement-Based (5 Questions) ---
add_stmt(sec2_en, sec2_hi,
    "Consider the following statements regarding Middle Paleolithic flake tool technology:\n1. Flake tools are smaller and thinner than Lower Paleolithic core tools.\n2. The prepared core technique allows for the production of multiple predictable tools from a single core block.\nWhich of the statements given above is/are correct?",
    "मध्य पुरापाषाणकालीन शल्क उपकरण तकनीक के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. शल्क उपकरण निम्न पुरापाषाणकालीन कोर उपकरणों की तुलना में छोटे और पतले होते हैं।\n2. तैयार कोर तकनीक एक ही मूल ब्लॉक से कई निश्चित आकार के उपकरण बनाने की अनुमति देती है।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
    2,
    "Both statements are correct. These capture the core advantages of the prepared core flake tool industry.",
    "दोनों कथन सही हैं। ये तैयार कोर शल्क उपकरण उद्योग के मुख्य लाभों को दर्शाते हैं।"
)

add_stmt(sec2_en, sec2_hi,
    "Consider the following statements regarding the Nevasan tradition:\n1. It was defined based on excavations at Nevasa in the Pravara River basin.\n2. It represents a transition where flake tools completely replaced bone tools in the Deccan.\nWhich of the statements given above is/are correct?",
    "नेवासियाई परंपरा के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. इसे प्रवरा नदी बेसिन में नेवासा में हुए उत्खनन के आधार पर परिभाषित किया गया था।\n2. यह एक ऐसे संक्रमण का प्रतिनिधित्व करता है जहां शल्क उपकरणों ने दक्कन में हड्डी के उपकरणों को पूरी तरह से प्रतिस्थापित कर दिया।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
    0,
    "Statement 1 is correct. Statement 2 is incorrect because bone tools were not present in the Deccan Lower Paleolithic to be replaced; they only emerge significantly later in the Upper Paleolithic.",
    "कथन 1 सही है। कथन 2 गलत है क्योंकि दक्कन के निम्न पुरापाषाण काल में हड्डी के उपकरण मौजूद नहीं थे; वे बहुत बाद में उच्च पुरापाषाण काल में दिखाई देते हैं।"
)

add_stmt(sec2_en, sec2_hi,
    "With reference to the prepared core technique, consider the following statements:\n1. Hominins shaped the top and sides of the stone core before striking off the final flake.\n2. The technique resulted in a complete waste of the parent block of stone after one strike.\nWhich of the statements given above is/are correct?",
    "तैयार कोर तकनीक के संदर्भ में, निम्नलिखित कथनों पर विचार करें:\n1. आदिम मानवों ने अंतिम शल्क निकालने से पहले पत्थर के कोर के ऊपरी हिस्से और किनारों को आकार दिया।\n2. इस तकनीक के कारण एक प्रहार के बाद मूल पत्थर का खंड पूरी तरह से बेकार हो जाता था।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
    0,
    "Statement 1 is correct. Statement 2 is incorrect because prepared cores were often reused to detach several flakes before being discarded.",
    "कथन 1 सही है। कथन 2 गलत है क्योंकि तैयार कोर का अक्सर कई शल्क निकालने के लिए पुन: उपयोग किया जाता था।"
)

add_stmt(sec2_en, sec2_hi,
    "Consider the following statements regarding the Luni Valley Middle Paleolithic sites:\n1. The sites are mostly open-air workshop stations rich in chert flakes.\n2. The Luni Valley represents a dense forest ecosystem during the Middle Paleolithic.\nWhich of the statements given above is/are correct?",
    "लूनी घाटी के मध्य पुरापाषाण स्थलों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. ये स्थल ज्यादातर चर्ट शल्कों से समृद्ध खुले मैदानों में स्थित कार्यशाला स्टेशन हैं।\n2. लूनी घाटी मध्य पुरापाषाण काल के दौरान एक सघन वन पारिस्थितिकी तंत्र का प्रतिनिधित्व करती थी।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
    0,
    "Statement 1 is correct. Statement 2 is incorrect because the region was a semi-arid desert margin, not a dense forest ecosystem.",
    "कथन 1 सही है। कथन 2 गलत है क्योंकि यह क्षेत्र एक अर्ध-शुष्क मरुस्थलीय किनारा था, न कि सघन वन क्षेत्र।"
)

add_stmt(sec2_en, sec2_hi,
    "Consider the following statements regarding the site of Bhimbetka during the Middle Paleolithic:\n1. Hominins completely stopped using local Vindhyan quartzite, shifting entirely to imported chert.\n2. Cave deposits display thick layers of flake tools overlying Lower Paleolithic layers.\nWhich of the statements given above is/are correct?",
    "मध्य पुरापाषाण काल के दौरान भीमबेटका स्थल के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. आदिम मानवों ने स्थानीय विंध्यन क्वार्ट्जाइट का उपयोग पूरी तरह से बंद कर दिया और पूरी तरह से आयातित चर्ट का उपयोग करने लगे।\n2. गुफाओं के जमाव निम्न पुरापाषाण काल की परतों के ऊपर शल्क उपकरणों की मोटी परतें प्रदर्शित करते हैं।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
    1,
    "Statement 1 is incorrect because locally available fine-grained quartzite was still utilized due to its abundance. Statement 2 is correct.",
    "कथन 1 गलत है क्योंकि भीमबेटका में स्थानीय महीन क्वार्ट्जाइट का उपयोग जारी रहा। कथन 2 सही है।"
)

# --- 9. Why (3 Questions) ---
add_open(sec2_en, sec2_hi, "Why",
    "Why did Middle Paleolithic hominins shift from quartzite to chert and jasper?",
    "मध्य पुरापाषाणकालीन आदिम मानवों ने क्वार्ट्जाइट से चर्ट और जैस्पर की ओर रुख क्यों किया?",
    "Fine-grained chert and jasper possess microcrystalline structure and fracture more predictably than coarse quartzite. This allowed hominins to manufacture much smaller, thinner, and more specialized tools with extremely sharp and retouched edges.",
    "महीन चर्ट और जैस्पर में सूक्ष्म-कण संरचना होती है और ये मोटे क्वार्ट्जाइट की तुलना में अधिक निश्चितता से टूटते हैं। इसने आदिम मानवों को बहुत छोटे, पतले और अधिक विशिष्ट उपकरण बनाने में सक्षम बनाया जिनके किनारे अत्यंत तीखे होते थे।"
)

add_open(sec2_en, sec2_hi, "Why",
    "Why did scrapers become the dominant tool type in Middle Paleolithic toolkits?",
    "मध्य पुरापाषाणकालीन उपकरण किटों में खुरचनी (scrapers) सबसे प्रमुख उपकरण प्रकार क्यों बन गए?",
    "The Middle Paleolithic coincided with changing climatic niches where hominins engaged in processing animal hides for clothing/coverings and shaving wood for hafting spears. Scrapers, with their retouched sharp working edges, were ideal for these intensive scraping activities.",
    "मध्य पुरापाषाण काल बदलती जलवायु परिस्थितियों के साथ मेल खाता था जहाँ आदिम मानवों को शरीर ढकने के लिए जानवरों की खाल साफ करने और भालों को जोड़ने के लिए लकड़ी को तराशने की आवश्यकता थी। खुरचनी (scrapers) अपने तीखे किनारों के साथ इन गतिविधियों के लिए आदर्श उपकरण थे।"
)

add_open(sec2_en, sec2_hi, "Why",
    "Why is the prepared core technique considered technologically superior to direct handaxe knapping?",
    "तैयार कोर तकनीक को सीधे हस्तकुठार तराशने की तुलना में तकनीकी रूप से श्रेष्ठ क्यों माना जाता है?",
    "Direct knapping of core tools is wasteful and yields only one general-purpose tool per block. The prepared core technique allow hominins to pre-shape the core to extract multiple standardized, sharp flakes of pre-planned sizes, maximizing the utility of a single rock block.",
    "मूल पत्थरों को सीधे तराशना कचरा बढ़ाता है और इससे प्रति ब्लॉक केवल एक ही उपकरण बनता है। तैयार कोर तकनीक आदिम मानवों को कोर को पूर्व-आकार देने और उससे पूर्व-नियोजित आकारों के कई मानकीकृत शल्क निकालने की अनुमति देती थी, जिससे एक ही पत्थर की उपयोगिता अधिकतम हो जाती थी।"
)

# --- 10. How (3 Questions) ---
add_open(sec2_en, sec2_hi, "How",
    "How does a knapper manufacture a tool using the prepared core Levallois method?",
    "एक कारीगर लेवालोइस तैयार कोर विधि का उपयोग करके उपकरण का निर्माण कैसे करता है?",
    "The knapper first trims the edges of a stone block to create a dome-like core. Next, they prepare a flat striking platform at one end. Finally, a single directed blow on this platform detaches a pre-shaped, sharp flake that requires minimal retouching to become a functional tool.",
    "कारीगर सबसे पहले पत्थर के एक खंड के किनारों को तराशकर गुंबद जैसा कोर बनाता है। इसके बाद, वे एक सिरे पर एक समतल प्रहार मंच (striking platform) तैयार करते हैं। अंत में, इस मंच पर एक सटीक प्रहार से पहले से नियोजित आकार का एक तेज शल्क अलग हो जाता है जिसे सीधे उपयोग किया जा सकता है।"
)

add_open(sec2_en, sec2_hi, "How",
    "How did archaeologists identify the Middle Paleolithic flake tradition at Nevasa?",
    "पुरातत्वविदों ने नेवासा में मध्य पुरापाषाणकालीन शल्क (flake) परंपरा की पहचान कैसे की?",
    "Archaeologists led by H.D. Sankalia excavated the Pravara gravel beds at Nevasa. They found layers containing almost no large handaxes or cleavers, but a massive accumulation of small scrapers, points, and prepared cores made on chert and jasper. This distinct stratigraphic tool shift established the Middle Paleolithic as an independent phase in India.",
    "एच.डी. सांकलिया के नेतृत्व में पुरातत्वविदों ने नेवासा में प्रवरा नदी की बजरी की परतों का उत्खनन किया। उन्होंने पाया कि यहाँ बड़े हस्तकुठार लगभग गायब थे, और चर्ट व जैस्पर से बनी छोटी खुरचनी, शूल और तैयार कोर का सघन संचय था। उपकरणों के इस बदलाव ने मध्य पुरापाषाण काल को भारत में एक स्वतंत्र चरण के रूप में स्थापित किया।"
)

add_open(sec2_en, sec2_hi, "How",
    "How does 'retouching' alter the functionality of a stone flake?",
    "सुधार करना या तराशना (retouching) एक पाषाण शल्क (flake) की कार्यक्षमता को कैसे बदलता है?",
    "Retouching involves pressing off tiny flakes along the sharp edge of a detached flake using a bone or wood tool. This strengthens the edge, prevents it from dulling quickly, shapes it into specific working profiles (such as side scrapers or piercing borers), and makes it safer to hold in the hand.",
    "रिटचिंग में हड्डी या लकड़ी के उपकरण का उपयोग करके निकाले गए शल्क के तीखे किनारे से छोटे-छोटे टुकड़े दबाकर तोड़े जाते हैं। यह किनारे को मजबूत करता है, उसे जल्दी कुंद होने से बचाता है, उसे विशिष्ट कार्यों के लिए आकार देता है (जैसे खुरचनी या वेधक), और हाथ में पकड़ना आसान बनाता है।"
)

# --- 11. Case Study (3 Questions) ---
add_open(sec2_en, sec2_hi, "Case Study",
    "Case Study: H.D. Sankalia's excavations at Nevasa (1950s).\nExplain how Nevasa established the Middle Paleolithic as an independent cultural horizon in India.",
    "मामला अध्ययन: 1950 के दशक में एच.डी. सांकलिया द्वारा नेवासा का उत्खनन।\nस्पष्ट करें कि नेवासा ने भारत में एक स्वतंत्र सांस्कृतिक क्षितिज के रूप में मध्य पुरापाषाण काल को कैसे स्थापित किया।",
    "Before Nevasa, it was assumed that India transitioned directly from the Lower Paleolithic to the Mesolithic. Sankalia's excavation of the gravel terraces at Nevasa exposed a distinct stratigraphic layer between the Acheulian and later microliths. This layer contained a specialized flake-tool industry (scrapers, borers) made on silica rocks, proving the existence of a separate Middle Paleolithic phase, which he named the Nevasan tradition.",
    "नेवासा से पहले, यह माना जाता था कि भारत निम्न पुरापाषाण से सीधे मध्यपाषाण काल में चला गया था। सांकलिया ने नेवासा में नदी के बजरी बेड के उत्खनन से एशुलेयिन और बाद के सूक्ष्म-पाषाणों के बीच एक स्पष्ट परत खोजी। इस परत में सिलिका पत्थरों से बने शल्क उपकरण मिले, जो एक स्वतंत्र मध्य पुरापाषाण चरण को साबित करते हैं, जिसे उन्होंने नेवासियाई परंपरा नाम दिया।"
)

add_open(sec2_en, sec2_hi, "Case Study",
    "Case Study: V.N. Misra's surveys in the Luni Basin.\nDetail how the distribution of Middle Paleolithic sites in Rajasthan relates to Pleistocene hydrological networks.",
    "मामला अध्ययन: लूनी बेसिन में वी.एन. मिश्रा का सर्वेक्षण।\nविस्तार से बताएं कि राजस्थान में मध्य पुरापाषाणकालीन स्थलों का वितरण प्लीस्टोसीन काल के जल-स्रोतों (hydrological networks) से कैसे संबंधित है।",
    "V.N. Misra mapped Middle Paleolithic sites along the Luni River and its tributaries. His surveys showed that flake tool workshops clustered near paleo-channels and ancient lake beds (playas) like Didwana. This distribution proved that even during dry Pleistocene phases, these hydrological networks retained water, serving as migration corridors for animals and focus areas for human bands who relied on chert gravels exposed along river beds.",
    "वी.एन. मिश्रा ने लूनी नदी और उसकी सहायक नदियों के किनारे मध्य पुरापाषाण स्थलों का मानचित्रण किया। उनके सर्वेक्षणों ने दिखाया कि शल्क कार्यशालाएं पुराने चैनलों और प्राचीन झीलों (प्लेया) जैसे डीडवाना के आसपास केंद्रित थीं। इस वितरण ने साबित किया कि प्लीस्टोसीन के शुष्क चरणों के दौरान भी इन जल प्रणालियों में पानी रहता था, जो मानवों और वन्यजीवों को आकर्षित करता था।"
)

add_open(sec2_en, sec2_hi, "Case Study",
    "Case Study: Middle Paleolithic occupation inside Bhimbetka Caves (Shelter III F-23).\nExplain why Bhimbetka cave deposits show continuity of raw material usage unlike open-air sites.",
    "मामला अध्ययन: भीमबेटका गुफाओं (Shelter III F-23) के भीतर मध्य पुरापाषाणकालीन निवास।\nस्पष्ट करें कि खुले स्थलों के विपरीत भीमबेटका गुफा के जमाव कच्चे माल के उपयोग की निरंतरता को क्यों प्रदर्शित करते हैं।",
    "In Shelter III F-23, archaeologists excavated a thick deposit showing Middle Paleolithic layers directly overlying Acheulian deposits. Uniquely, the Middle Paleolithic tools at Bhimbetka were still made primarily of local fine-grained Vindhyan quartzite rather than chert. This was because the cave dwellers had access to massive quartzite outcrops right outside the shelter, making it unnecessary to search for silica rocks, demonstrating that local resource availability can override regional technological shifts.",
    "गुफा III F-23 में, पुरातत्वविदों ने एशुलेयिन जमावों के ठीक ऊपर मध्य पुरापाषाणकालीन परतों का उत्खनन किया। भीमबेटका में मध्य पुरापाषाणकालीन उपकरण चर्ट के बजाय स्थानीय महीन क्वार्ट्जाइट से ही बनाए जाते रहे। ऐसा इसलिए था क्योंकि गुफा के निवासियों के पास गुफा के ठीक बाहर क्वार्ट्जाइट के विशाल स्रोत थे, जिससे स्थानीय उपलब्धता ने क्षेत्रीय तकनीकी बदलाव को पीछे छोड़ दिया।"
)

# --- 12. Teach the Concept (3 Questions) ---
add_open(sec2_en, sec2_hi, "Teach the Concept",
    "Teach the Concept: Explain the prepared core (Levallois) technique to a student using the analogy of baking cookies.",
    "अवधारणा समझाएं: कुकीज़ बेक करने के सादृश्य (analogy) का उपयोग करके एक छात्र को तैयार कोर (लेवालोइस) तकनीक समझाएं।",
    "Imagine you want to bake a star-shaped cookie. If you just take a lump of dough and pull off a piece, it won't be symmetrical. Instead, you carefully roll out the dough, smooth the surface, and shape the edges first. Once the dough block is perfectly prepared, you press a cookie cutter once to get the perfect star. In the Levallois technique, the stoneworker shapes the core first (like the dough) so that when they strike it once at the end, they get a pre-shaped, sharp flake tool (the cookie) immediately.",
    "कल्पना कीजिए कि आप एक सितारे के आकार की कुकी बनाना चाहते हैं। यदि आप केवल आटे का एक लोटा लें और उसका टुकड़ा तोड़ें, तो वह सममित नहीं होगा। इसके बजाय, आप पहले आटे को बेलते हैं, उसकी सतह को चिकना करते हैं और किनारों को आकार देते हैं। एक बार जब आटा तैयार हो जाता है, तो आप एक सही सितारा प्राप्त करने के लिए सांचे को दबाते हैं। लेवालोइस तकनीक में, कारीगर पहले कोर को आकार देता है (आटे की तरह) ताकि अंत में एक प्रहार से एक पूर्वनिर्धारित शल्क उपकरण मिल सके।"
)

add_open(sec2_en, sec2_hi, "Teach the Concept",
    "Teach the Concept: Explain the differences between a Scraper and a Point tool, including how their designs reflect their functions.",
    "अवधारणा समझाएं: एक खुरचनी (Scraper) और एक शूल (Point) उपकरण के बीच के अंतर को समझाएं, जिसमें यह भी शामिल हो कि उनके डिजाइन उनके कार्यों को कैसे दर्शाते हैं।",
    "A scraper is designed with flat, broad working edges that are retouched to make them durable and slightly dull so they slide over animal hides to remove fat without tearing the skin. In contrast, a point tool is triangular and tapers to a sharp, narrow tip. It is designed to pierce flesh, meaning its edges converge to a single point, making it suitable to be tied to a wooden stick as a spearhead for hunting from a distance.",
    "खुरचनी (scraper) को चपटे, चौड़े किनारों के साथ बनाया जाता है जिन्हें थोड़ा मजबूत बनाया जाता है ताकि वे बिना फाड़े जानवरों की खाल से चर्बी हटाने के लिए उस पर फिसल सकें। इसके विपरीत, शूल (point) त्रिकोणीय होता है और एक नुकीली नोक पर समाप्त होता है। इसे मांस में छेद करने के लिए बनाया जाता है, जिससे इसके किनारे एक बिंदु पर मिलते हैं, जो इसे भाले की नोक के रूप में बांधने के लिए उपयुक्त बनाता है।"
)

add_open(sec2_en, sec2_hi, "Teach the Concept",
    "Teach the Concept: Explain why the transition from Lower to Middle Paleolithic represents a change from 'heavy-duty' to 'specialized' toolkits.",
    "अवधारणा समझाएं: समझाएं कि निम्न से मध्य पुरापाषाण काल का संक्रमण 'भारी कार्यों' से 'विशिष्ट' उपकरणों की ओर बदलाव का प्रतिनिधित्व क्यों करता है।",
    "In the Lower Paleolithic, hominins relied on large core handaxes and cleavers. These were heavy tools held directly in the hand, used for crushing bones, digging roots, or cutting heavy wood (heavy-duty). In the Middle Paleolithic, tools became much smaller and lighter (flake tools). Hominins created specialized toolkits containing scrapers for hides, borers for piercing holes, and points for spearheads. This allowed them to perform precise tasks and hunt more efficiently, shifting from brute force to specialized precision.",
    "निम्न पुरापाषाण काल में, आदिम मानव बड़े हस्तकुठार और विदारक पर निर्भर थे। ये भारी उपकरण थे जिनका उपयोग सीधे हाथ में पकड़कर हड्डियाँ तोड़ने, जड़ें खोदने या भारी लकड़ी काटने (भारी कार्य) के लिए किया जाता था। मध्य पुरापाषाण काल में, उपकरण बहुत छोटे और हल्के हो गए (flake tools)। आदिम मानवों ने विशिष्ट उपकरण किट बनाए जिनमें खाल के लिए खुरचनी, छेद करने के लिए वेधक और भालों के लिए शूल शामिल थे, जिससे वे सटीक कार्य कर सके।"
)
