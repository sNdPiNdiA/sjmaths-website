from .helpers import add_mcq, add_multi_mcq, add_stmt, add_ar

mock_en = []
mock_hi = []

# 10 UPSC-level mock questions — high difficulty, varied types

add_stmt(mock_en, mock_hi,
    "Consider the following statements about the Mesolithic period in India:\n1. It is characterised by the use of geometric microliths made primarily from chert and chalcedony.\n2. The Mesolithic commenced with the onset of the Last Glacial Maximum (LGM) approximately 25,000 years ago.\n3. Sites like Bagor and Adamgarh provide the earliest evidence of animal domestication in South Asia.\nWhich of the statements given above is/are correct?",
    "भारत में मध्यपाषाण काल के बारे में निम्नलिखित कथनों पर विचार करें:\n1. यह मुख्य रूप से चर्ट और चाल्सीडोनी से बने ज्यामितीय सूक्ष्म पाषाणों के उपयोग द्वारा चित्रित है।\n2. मध्यपाषाण काल लगभग 25,000 वर्ष पहले अंतिम हिमाच्छादन अधिकतम (LGM) की शुरुआत के साथ शुरू हुआ।\n3. बागोर और आदमगढ़ जैसे स्थल दक्षिण एशिया में पशुपालन का सबसे पहला साक्ष्य प्रदान करते हैं।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 and 3 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"],
    ["केवल 1 और 3", "केवल 1 और 2", "केवल 2 और 3", "1, 2 और 3"],
    0,
    "Statements 1 and 3 are correct. Statement 2 is incorrect — the Mesolithic began with the END of the LGM (warming post-LGM), not its onset. The LGM was c. 26,500 years ago; the Mesolithic started c. 12,000 BCE.",
    "कथन 1 और 3 सही हैं। कथन 2 गलत है — मध्यपाषाण काल LGM की शुरुआत के साथ नहीं, बल्कि LGM के अंत (LGM के बाद ताप) के साथ शुरू हुआ।"
)

add_stmt(mock_en, mock_hi,
    "Consider the following pairs:\nSite : Key characteristic\n1. Bagor (Rajasthan) : Largest Mesolithic site in India; three-phase stratigraphy showing Mesolithic to early historical transition\n2. Damdama (Uttar Pradesh) : 41 human burials including triple burials; oxbow lake setting\n3. Bhimbetka (Madhya Pradesh) : Largest Mesolithic burial ground in India\n4. Langhnaj (Gujarat) : Sand-dune site excavated by H.D. Sankalia in Sabarmati basin\nHow many of the above pairs are correctly matched?",
    "निम्नलिखित युग्मों पर विचार करें:\nस्थल : मुख्य विशेषता\n1. बागोर (राजस्थान) : भारत का सबसे बड़ा मध्यपाषाणकालीन स्थल; मध्यपाषाण से प्रारंभिक ऐतिहासिक संक्रमण दिखाने वाला तीन-चरण स्तरविन्यास\n2. दमदमा (उत्तर प्रदेश) : तिहरी कब्रों सहित 41 मानव कब्रें; गोखुर झील स्थापना\n3. भीमबेटका (मध्य प्रदेश) : भारत का सबसे बड़ा मध्यपाषाणकालीन शवाधान स्थल\n4. लांघनाज (गुजरात) : साबरमती बेसिन में एच.डी. सांकलिया द्वारा उत्खनित रेत-टीला स्थल\nऊपर के कितने युग्म सही सुमेलित हैं?",
    ["Only one", "Only two", "Only three", "All four"],
    ["केवल एक", "केवल दो", "केवल तीन", "सभी चार"],
    2,
    "Pairs 1, 2, and 4 are correctly matched. Pair 3 is incorrect — Bhimbetka is a UNESCO rock art site, not a burial ground. The largest burial count is at Damdama.",
    "युग्म 1, 2 और 4 सही सुमेलित हैं। युग्म 3 गलत है — भीमबेटका एक UNESCO शैल कला स्थल है, शवाधान स्थल नहीं। सबसे अधिक शवाधान संख्या दमदमा में है।"
)

add_ar(mock_en, mock_hi,
    "Assertion (A): The Mesolithic period is considered the cultural bridge between the Paleolithic and Neolithic phases.\nReason (R): It combines microlithic hunting tools (Paleolithic tradition) with the beginnings of pastoralism and art (anticipating Neolithic developments).",
    "कथन (A): मध्यपाषाण काल को पुरापाषाण और नवपाषाण चरणों के बीच सांस्कृतिक पुल माना जाता है।\nकारण (R): यह सूक्ष्म पाषाण शिकार उपकरणों (पुरापाषाण परंपरा) को पशुपालन और कला की शुरुआत (नवपाषाण विकास की आशंका) के साथ जोड़ता है।",
    0,
    "Both A and R are true, and R correctly explains why the Mesolithic serves as a transitional cultural bridge.",
    "A और R दोनों सही हैं, और R सही ढंग से बताता है कि मध्यपाषाण काल एक संक्रमणकालीन सांस्कृतिक पुल के रूप में क्यों काम करता है।"
)

add_multi_mcq(mock_en, mock_hi,
    "Which of the following statements correctly describe the ecological drivers of the Mesolithic cultural transition? (Select all that apply)",
    "निम्नलिखित में से कौन से कथन मध्यपाषाणकालीन सांस्कृतिक संक्रमण के पारिस्थितिक चालकों का सही वर्णन करते हैं? (सभी सही विकल्प चुनें)",
    ["Post-glacial warming led to the extinction of large Pleistocene megafauna", "Rising sea levels submerged coastal habitats, forcing inland migrations", "The spread of forests required smaller, faster tools to hunt forest-adapted prey", "Onset of a new glaciation created new tundra environments favourable for megahunting"],
    ["हिमयुगोत्तर ताप ने बड़े प्लीस्टोसीन विशाल जीवों के विलोपन की ओर ले जाया", "बढ़ते समुद्र के स्तर ने तटीय आवासों को डुबो दिया, अंदरूनी इलाकों में प्रवासन को मजबूर किया", "जंगलों के फैलाव के लिए जंगल-अनुकूलित शिकार को पकड़ने के लिए छोटे, तेज उपकरणों की आवश्यकता थी", "नई हिमाच्छादन की शुरुआत ने विशाल-शिकार के लिए अनुकूल नए टुंड्रा वातावरण बनाए"],
    [0, 1, 2],
    "The first three correctly describe post-glacial ecological drivers. A new glaciation did not occur — the planet warmed during the Holocene, creating forests and shrinking grasslands.",
    "पहले तीन सही ढंग से हिमयुगोत्तर पारिस्थितिक चालकों का वर्णन करते हैं। कोई नई हिमाच्छादन नहीं हुई — होलोसीन के दौरान ग्रह गर्म हुआ।"
)

add_stmt(mock_en, mock_hi,
    "Consider the following statements about the significance of Bhimbetka:\n1. Its paintings span multiple prehistoric periods from Paleolithic to early historical times.\n2. It was discovered by V.S. Wakankar and inscribed as a UNESCO World Heritage Site in 2003.\n3. The dominant pigment used is red haematite, which is chemically stable and durable.\nWhich of the statements given above are correct?",
    "भीमबेटका के महत्व के बारे में निम्नलिखित कथनों पर विचार करें:\n1. इसकी चित्रकारी पुरापाषाण से प्रारंभिक ऐतिहासिक काल तक कई प्रागैतिहासिक कालों में फैली हुई है।\n2. इसकी खोज वी.एस. वाकणकर ने की थी और 2003 में UNESCO विश्व धरोहर स्थल के रूप में नामांकित किया गया था।\n3. उपयोग किया जाने वाला प्रमुख रंगद्रव्य लाल हेमेटाइट है, जो रासायनिक रूप से स्थिर और टिकाऊ है।\nऊपर दिए गए कौन से कथन सही हैं?",
    ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
    ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
    3,
    "All three statements are correct — Bhimbetka's multi-period art sequence, Wakankar's discovery, UNESCO inscription (2003), and haematite's chemical stability are all verified facts.",
    "तीनों कथन सही हैं — भीमबेटका का बहु-काल कला अनुक्रम, वाकणकर की खोज, UNESCO नामांकन (2003) और हेमेटाइट की रासायनिक स्थिरता सभी सत्यापित तथ्य हैं।"
)

add_stmt(mock_en, mock_hi,
    "Consider the following statements about the Mesolithic subsistence economy:\n1. The broad-spectrum foraging strategy replaced exclusive dependence on large-game hunting.\n2. Pastoralism (animal domestication) began during the Mesolithic at sites like Bagor, prior to the Neolithic.\n3. Intentional irrigated rice cultivation was first practised at Mesolithic sites in the Ganga Valley.\nWhich of the statements given above is/are correct?",
    "मध्यपाषाणकालीन जीवन निर्वाह अर्थव्यवस्था के बारे में निम्नलिखित कथनों पर विचार करें:\n1. व्यापक-स्पेक्ट्रम भोजन संग्रह रणनीति ने बड़े-शिकार शिकार पर विशेष निर्भरता को प्रतिस्थापित किया।\n2. पशुपालन (पशुपालन) मध्यपाषाण काल के दौरान बागोर जैसे स्थलों पर शुरू हुआ, नवपाषाण से पहले।\n3. गंगा घाटी के मध्यपाषाणकालीन स्थलों पर पहली बार जानबूझकर सिंचित चावल की खेती का अभ्यास किया गया था।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"],
    ["केवल 1", "केवल 1 और 2", "केवल 2 और 3", "1, 2 और 3"],
    1,
    "Statements 1 and 2 are correct. Statement 3 is incorrect — irrigated rice cultivation was a Neolithic achievement (e.g., Lahuradewa, c. 7000 BCE), not Mesolithic.",
    "कथन 1 और 2 सही हैं। कथन 3 गलत है — सिंचित चावल की खेती एक नवपाषाणकालीन उपलब्धि थी (जैसे लहुरादेवा, लगभग 7000 ईसा पूर्व), मध्यपाषाणकालीन नहीं।"
)

add_ar(mock_en, mock_hi,
    "Assertion (A): Organic remains such as bone ornaments survive at Ganga valley Mesolithic sites despite the typically destructive alluvial environment.\nReason (R): The Ganga valley sediments are relatively rich in calcium carbonate, creating alkaline conditions that retard bone dissolution.",
    "कथन (A): जैविक अवशेष जैसे हड्डी के आभूषण गंगा घाटी मध्यपाषाणकालीन स्थलों पर आम तौर पर विनाशकारी जलोढ़ वातावरण के बावजूद बचते हैं।\nकारण (R): गंगा घाटी की तलछट अपेक्षाकृत कैल्शियम कार्बोनेट से समृद्ध है, जो क्षारीय परिस्थितियाँ बनाती है जो हड्डी के विघटन को धीमा करती है।",
    0,
    "Both A and R are true, and R is the correct chemical explanation for bone preservation in Ganga valley alluvial sediments.",
    "A और R दोनों सही हैं, और R गंगा घाटी जलोढ़ तलछट में हड्डी संरक्षण की सही रासायनिक व्याख्या है।"
)

add_stmt(mock_en, mock_hi,
    "Consider the following statements about Mesolithic burial practices:\n1. Intra-settlement burials at Ganga valley sites indicate strong social bonds within bands.\n2. Grave goods (ornaments, food, tools) placed with the dead indicate belief in an afterlife.\n3. All Ganga valley Mesolithic burials were individual, with no double or triple burials.\nWhich of the statements given above is/are correct?",
    "मध्यपाषाणकालीन शवाधान प्रथाओं के बारे में निम्नलिखित कथनों पर विचार करें:\n1. गंगा घाटी के स्थलों पर बस्ती-अंतर्गत शवाधान समूहों के भीतर मजबूत सामाजिक बंधनों को इंगित करते हैं।\n2. मृतकों के साथ रखे गए कब्र के सामान (आभूषण, भोजन, उपकरण) परलोक में विश्वास को इंगित करते हैं।\n3. सभी गंगा घाटी मध्यपाषाणकालीन शवाधान व्यक्तिगत थे, कोई दोहरे या तिहरे शवाधान नहीं थे।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 and 2 only", "2 and 3 only", "1 only", "1, 2 and 3"],
    ["केवल 1 और 2", "केवल 2 और 3", "केवल 1", "1, 2 और 3"],
    0,
    "Statements 1 and 2 are correct. Statement 3 is incorrect — Mahadaha shows double burials and Damdama shows triple burials.",
    "कथन 1 और 2 सही हैं। कथन 3 गलत है — महदहा दोहरी कब्रें दिखाता है और दमदमा तिहरी कब्रें दिखाता है।"
)

add_stmt(mock_en, mock_hi,
    "Which of the following statements about the Mesolithic tool technology are correct?\n1. Microliths were standardised, geometrically shaped tools made by the indirect percussion and pressure flaking technique.\n2. Composite tools that combined microliths with organic handles were a major Mesolithic innovation.\n3. The key raw materials were granite and basalt, selected for their weight and hardness.\nSelect the correct answer:",
    "मध्यपाषाणकालीन उपकरण प्रौद्योगिकी के बारे में निम्नलिखित कथनों में से कौन से सही हैं?\n1. सूक्ष्म पाषाण मानकीकृत, ज्यामितीय रूप से आकार के उपकरण थे जो अप्रत्यक्ष प्रहार और दबाव फ्लेकिंग तकनीक द्वारा बनाए गए थे।\n2. सूक्ष्म पाषाणों को जैविक हैंडल के साथ जोड़ने वाले संयुक्त उपकरण एक प्रमुख मध्यपाषाण नवाचार था।\n3. मुख्य कच्ची सामग्री ग्रेनाइट और बेसाल्ट थे, जो उनके वजन और कठोरता के लिए चुने गए थे।\nसही उत्तर चुनें:",
    ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
    ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
    0,
    "Statements 1 and 2 are correct. Statement 3 is incorrect — microliths used chert and chalcedony (silica-rich), not granite/basalt, because silica fractures conchoidally to give sharp edges.",
    "कथन 1 और 2 सही हैं। कथन 3 गलत है — सूक्ष्म पाषाणों ने चर्ट और चाल्सीडोनी (सिलिका-समृद्ध) का उपयोग किया, ग्रेनाइट/बेसाल्ट नहीं, क्योंकि सिलिका तेज किनारे देने के लिए शंखाभ फ्रैक्चर करता है।"
)

add_ar(mock_en, mock_hi,
    "Assertion (A): The sand dune site of Langhnaj in Gujarat provides evidence of a mixed subsistence economy combining foraging, fishing, and human burials.\nReason (R): Langhnaj's location in the Sabarmati river basin provided proximity to seasonal water bodies, fish, and animal resources, making it an ideal recurring camp site.",
    "कथन (A): गुजरात में लांघनाज का रेत टीला स्थल भोजन संग्रह, मछली पकड़ने और मानव शवाधान को मिलाकर एक मिश्रित जीवन निर्वाह अर्थव्यवस्था का साक्ष्य प्रदान करता है।\nकारण (R): साबरमती नदी बेसिन में लांघनाज का स्थान मौसमी जल निकायों, मछली और पशु संसाधनों से निकटता प्रदान करता था, जिससे यह एक आदर्श आवर्ती शिविर स्थल बन गया।",
    0,
    "Both A and R are true, and R correctly explains the ecological factors that made Langhnaj a repeated Mesolithic occupation site.",
    "A और R दोनों सही हैं, और R सही ढंग से उन पारिस्थितिक कारकों की व्याख्या करता है जिन्होंने लांघनाज को एक बार-बार मध्यपाषाणकालीन बस्ती स्थल बनाया।"
)
