from .helpers import add_mcq, add_multi_mcq, add_tf, add_blank, add_match, add_oneliner, add_ar, add_stmt, add_open

sec1_en = []
sec1_hi = []

# --- 1. MCQ (5 Questions) ---
add_mcq(sec1_en, sec1_hi,
    "The geological epoch that corresponds to the beginning and development of the Mesolithic period is the:",
    "वह भूवैज्ञानिक युग जो मध्यपाषाण काल की शुरुआत और विकास से मेल खाता है, वह है:",
    ["Pleistocene Epoch", "Holocene Epoch", "Pliocene Epoch", "Miocene Epoch"],
    ["प्लीस्टोसीन युग", "होलोसीन युग", "प्लायोसीन युग", "मायोसीन युग"],
    1,
    "The Mesolithic period in India begins with the transition from the Pleistocene to the Holocene epoch, around 10,000 BCE, characterized by global warming.",
    "भारत में मध्यपाषाण काल की शुरुआत लगभग 10,000 ईसा पूर्व में प्लीस्टोसीन से होलोसीन युग में संक्रमण के साथ होती है, जो वैश्विक वार्मिंग (तापमान वृद्धि) द्वारा चिह्नित है।"
)

add_mcq(sec1_en, sec1_hi,
    "Which of the following primary climatic changes occurred in India during the Pleistocene-Holocene transition?",
    "प्लीस्टोसीन-होलोसीन संक्रमण के दौरान भारत में निम्नलिखित में से कौन सा प्राथमिक जलवायु परिवर्तन हुआ?",
    ["From warm-humid to cold-dry", "From cold-dry to warm-humid", "Consistent extreme glaciation", "Severe desertification across the peninsula"],
    ["गर्म-आर्द्र से ठंडे-शुष्क में", "ठंडे-शुष्क से गर्म-आर्द्र में", "निरंतर अत्यधिक हिमीकरण", "पूरे प्रायद्वीप में गंभीर मरुस्थलीकरण"],
    1,
    "The transition to the Holocene brought a shift from a cold, arid climate to a warmer, more humid climate with increased monsoonal rainfall.",
    "होलोसीन में संक्रमण ने ठंडी, शुष्क जलवायु से गर्म, अधिक आर्द्र जलवायु और बढ़ी हुई मानसूनी वर्षा की ओर बदलाव लाया।"
)

add_mcq(sec1_en, sec1_hi,
    "How did the faunal composition change in the early Holocene, affecting Mesolithic hunting strategies?",
    "प्रारंभिक होलोसीन में जीवों की संरचना कैसे बदली, जिसने मध्यपाषाणकालीन शिकार रणनीतियों को प्रभावित किया?",
    ["Megafauna multiplied rapidly", "Large mammals declined and small, agile animals expanded", "All land animals went extinct, forcing marine dependence", "Domestication of large carnivores became dominant"],
    ["विशालकाय जीव तेजी से बढ़े", "बड़े स्तनधारियों में कमी आई और छोटे, फुर्तीले जानवरों का विस्तार हुआ", "सभी भूमि के जानवर विलुप्त हो गए, जिससे समुद्री निर्भरता बढ़ी", "बड़े मांसाहारी जानवरों का घरेलूकरण प्रमुख हो गया"],
    1,
    "Pleistocene megafauna declined, and small, agile game (deer, boar, birds) along with fish and mollusks expanded, prompting the need for smaller projectile weapons.",
    "प्लीस्टोसीन विशालकाय जीवों में कमी आई, और छोटे, फुर्तीले शिकार (हिरण, सूअर, पक्षी) के साथ-साथ मछली और घोंघे का विस्तार हुआ, जिससे छोटे प्रक्षेपास्त्र हथियारों की आवश्यकता महसूस हुई।"
)

add_mcq(sec1_en, sec1_hi,
    "Which of the following geographical regions was colonized for the first time by humans during the Mesolithic due to climatic stabilization?",
    "जलवायु स्थिरता के कारण मध्यपाषाण काल के दौरान मनुष्यों द्वारा पहली बार निम्नलिखित में से किस भौगोलिक क्षेत्र में बस्ती बसाई गई थी?",
    ["High-altitude Himalayan glaciers", "The alluvial plains of the Ganga River Basin", "Deep underwater marine trenches", "Extremely arid core areas of the Thar Desert"],
    ["उच्च ऊंचाई वाले हिमालयी हिमनद", "गंगा नदी बेसिन के जलोढ़ मैदान", "गहरे पानी के भीतर समुद्री खाइयाँ", "थार मरुस्थल के अत्यधिक शुष्क मुख्य क्षेत्र"],
    1,
    "The warming of the Holocene stabilized the Ganga River plain, forming oxbow lakes and fertile margins that attracted Mesolithic hunter-gatherers.",
    "होलोसीन के गर्म होने से गंगा नदी के मैदान में स्थिरता आई, जिससे गोखुर झीलें (oxbow lakes) और उपजाऊ किनारे बने जिन्होंने मध्यपाषाणकालीन शिकारी-संग्रहकर्ताओं को आकर्षित किया।"
)

add_mcq(sec1_en, sec1_hi,
    "Which environmental feature in Western India (Gujarat/Rajasthan) became stabilized and vegetated, supporting Mesolithic settlements?",
    "पश्चिमी भारत (गुजरात/राजस्थान) में कौन सी पर्यावरणीय विशेषता स्थिर और वनस्पति-युक्त हो गई, जिसने मध्यपाषाणकालीन बस्तियों को सहारा दिया?",
    ["Active volcanic craters", "Saline sand dunes", "Glacial moraines", "Sub-humid sand dunes"],
    ["सक्रिय ज्वालामुखी क्रेटर", "लवणीय रेत के टीले", "हिमनद हिमोढ़", "उपोष्णकटिबंधीय/स्थिर रेत के टीले"],
    3,
    "Increased rainfall during the early Holocene stabilized sand dunes in Gujarat and Rajasthan, allowing grass to grow and forming seasonal freshwater playas nearby.",
    "प्रारंभिक होलोसीन के दौरान बढ़ी हुई वर्षा ने गुजरात और राजस्थान में रेत के टीलों को स्थिर कर दिया, जिससे वहां घास उग आई और पास में मौसमी मीठे पानी की झीलें बन गईं।"
)

# --- 2. Multiple Correct MCQ (5 Questions) ---
add_multi_mcq(sec1_en, sec1_hi,
    "Which of the following environmental and climatic characteristics define the Holocene transition in India? (Select all that apply)",
    "निम्नलिखित में से कौन सी पर्यावरणीय और जलवायु संबंधी विशेषताएं भारत में होलोसीन संक्रमण को परिभाषित करती हैं? (सभी सही विकल्प चुनें)",
    ["Rise in global temperatures", "Increase in monsoonal precipitation", "Expansion of deciduous forests in Central India", "Advance of continental glaciers in Peninsular India"],
    ["वैश्विक तापमान में वृद्धि", "मानसूनी वर्षा में वृद्धि", "मध्य भारत में पर्णपाती (deciduous) वनों का विस्तार", "प्रायद्वीपीय भारत में महाद्वीपीय हिमनदों का आगे बढ़ना"],
    [0, 1, 2],
    "The Holocene transition is marked by global warming, enhanced monsoon rainfall, and forest expansion. Glacial advances did not occur in Peninsular India during this epoch.",
    "होलोसीन संक्रमण वैश्विक तापमान में वृद्धि, उन्नत मानसूनी वर्षा और वनों के विस्तार द्वारा चिह्नित है। इस युग में प्रायद्वीपीय भारत में हिमनदों का आगे बढ़ना नहीं हुआ था।"
)

add_multi_mcq(sec1_en, sec1_hi,
    "Which of the following resources became central to the 'broad-spectrum' diet of Mesolithic humans in the early Holocene plains? (Select all that apply)",
    "प्रारंभिक होलोसीन मैदानों में मध्यपाषाणकालीन मनुष्यों के 'व्यापक-स्पेक्ट्रम' (broad-spectrum) आहार में निम्नलिखित में से कौन से संसाधन केंद्रीय बन गए? (सभी सही विकल्प चुनें)",
    ["Freshwater mollusks (snails)", "Migratory and water birds", "Turtles and fish", "Domesticated wheat and barley crops"],
    ["मीठे पानी के घोंघे (mollusks)", "प्रवासी और जलीय पक्षी", "कछुए और मछली", "पालतू गेहूँ और जौ की फसलें"],
    [0, 1, 2],
    "Mesolithic diet expanded to include aquatic resources (snails, turtles, fish) and birds. Crop cultivation of wheat and barley is characteristic of the later Neolithic period, not the early Mesolithic.",
    "मध्यपाषाणकालीन आहार का विस्तार जलीय संसाधनों (घोंघे, कछुए, मछली) और पक्षियों को शामिल करने के लिए हुआ। गेहूँ और जौ की खेती बाद के नवपाषाण काल की विशेषता है, न कि प्रारंभिक मध्यपाषाण काल की।"
)

add_multi_mcq(sec1_en, sec1_hi,
    "Which geographical features provided favorable conditions for the Mesolithic colonization of the Ganga Valley? (Select all that apply)",
    "किन भौगोलिक विशेषताओं ने गंगा घाटी में मध्यपाषाणकालीन मानव बस्तियों के बसने के लिए अनुकूल परिस्थितियां प्रदान कीं? (सभी सही विकल्प चुनें)",
    ["Oxbow lakes formed by shifting river courses", "Rich alluvial soils supporting wild grasslands", "Abundant herds of small to medium swamp deer", "Arid sand dunes completely devoid of water sources"],
    ["नदियों के मार्ग बदलने से बनी गोखुर झीलें", "जंगली घास के मैदानों को सहारा देने वाली समृद्ध जलोढ़ मिट्टी", "छोटे से मध्यम दलदली हिरणों के प्रचुर झुंड", "पानी के स्रोतों से पूरी तरह से रहित शुष्क रेत के टीले"],
    [0, 1, 2],
    "Oxbow lakes, wild grasslands, and medium deer provided rich game and aquatic resources in the Ganga plains. Arid waterless dunes did not attract colonization.",
    "गंगा के मैदानों में गोखुर झीलों, जंगली घास के मैदानों और मध्यम आकार के हिरणों ने समृद्ध शिकार और जलीय संसाधन प्रदान किए। जलविहीन शुष्क टीलों ने बस्तियों को आकर्षित नहीं किया।"
)

add_multi_mcq(sec1_en, sec1_hi,
    "In Western India, how did environmental shifts impact Mesolithic site placement? (Select all that apply)",
    "पश्चिमी भारत में, पर्यावरणीय बदलावों ने मध्यपाषाणकालीन स्थलों की स्थिति को कैसे प्रभावित किया? (सभी सही विकल्प चुनें)",
    ["Sites were located on top of stabilized sand dunes", "Settlements clustered around seasonal rainwater pans (playas)", "Sites were established near high-altitude mountain peaks", "Occupations focused on dense evergreen rainforest niches"],
    ["बस्तियाँ स्थिर रेत के टीलों के शीर्ष पर स्थित थीं", "बस्तियाँ मौसमी वर्षा के गड्ढों (playas) के आसपास केंद्रित थीं", "बस्तियाँ ऊँची पर्वतीय चोटियों के पास स्थापित की गई थीं", "बस्तियाँ सघन सदाबहार वर्षावनों के अनुकूल स्थानों पर केंद्रित थीं"],
    [0, 1],
    "Western Indian Mesolithic sites like Langhnaj are situated on top of stabilized sand dunes, clustered near seasonal water bodies that provided freshwater in semi-arid zones.",
    "पश्चिमी भारतीय मध्यपाषाणकालीन स्थल जैसे लांघनाज स्थिर रेत के टीलों के ऊपर स्थित हैं, जो मौसमी जल निकायों के पास केंद्रित हैं जो अर्ध-शुष्क क्षेत्रों में मीठा पानी प्रदान करते थे।"
)

add_multi_mcq(sec1_en, sec1_hi,
    "Which of the following factors indicate a demographic expansion during the Indian Mesolithic? (Select all that apply)",
    "निम्नलिखित में से कौन से कारक भारतीय मध्यपाषाण काल के दौरान जनसांख्यिकीय विस्तार (demographic expansion) को दर्शाते हैं? (सभी सही विकल्प चुनें)",
    ["A major increase in the total number of documented archaeological sites", "Colonization of diverse ecological zones previously uninhabited by humans", "Widespread evidence of large permanent brick cities", "Deep stratigraphic occupational layers in shelters"],
    ["दस्तावेजीकृत पुरातात्विक स्थलों की कुल संख्या में बड़ी वृद्धि", "पहले से निर्जन विविध पारिस्थितिक क्षेत्रों में मानव बस्तियों का बसना", "बड़े स्थायी ईंटों के शहरों के व्यापक साक्ष्य", "शैल आश्रयों में गहरी स्तरविन्यासात्मक आवासीय परतें"],
    [0, 1, 3],
    "Demographic expansion is shown by more sites, new ecological zones, and deep occupation layers. Permanent brick cities belong to the Bronze Age Harappan civilization, not the Mesolithic.",
    "जनसांख्यिकीय विस्तार को अधिक स्थलों, नए पारिस्थितिक क्षेत्रों और गहरी परतों द्वारा दर्शाया गया है। स्थायी ईंटों के शहर कांस्य युग की हड़प्पा सभ्यता के हैं, न कि मध्यपाषाण काल के।"
)

# --- 3. True/False (8 Questions) ---
add_tf(sec1_en, sec1_hi,
    "The Holocene transition led to colder and drier conditions across the Indian subcontinent.",
    "होलोसीन संक्रमण के कारण भारतीय उपमहाद्वीप में ठंड और शुष्क परिस्थितियां पैदा हुईं।",
    False,
    "The Holocene transition brought warmer temperatures and higher humidity with increased precipitation.",
    "होलोसीन संक्रमण गर्म तापमान और बढ़ी हुई वर्षा के साथ उच्च आर्द्र परिस्थितियाँ लाया।"
)

add_tf(sec1_en, sec1_hi,
    "The Mesolithic period is geologically situated within the Pleistocene epoch.",
    "मध्यपाषाण काल भूवैज्ञानिक रूप से प्लीस्टोसीन युग के भीतर स्थित है।",
    False,
    "The Mesolithic is situated within the early Holocene epoch, which succeeded the Pleistocene.",
    "मध्यपाषाण काल प्रारंभिक होलोसीन युग के भीतर स्थित है, जो प्लीस्टोसीन के बाद आया था।"
)

add_tf(sec1_en, sec1_hi,
    "Large Pleistocene megafauna like the giant elephant and hippopotamus became extinct or highly reduced in India during the Holocene transition.",
    "प्लीस्टोसीन काल के विशालकाय जीव जैसे विशाल हाथी और दरियाई घोड़ा होलोसीन संक्रमण के दौरान भारत में विलुप्त हो गए या अत्यधिक कम हो गए।",
    True,
    "The environmental changes of the early Holocene caused a decline and extinction of several Pleistocene megafaunal species in India.",
    "प्रारंभिक होलोसीन के पर्यावरणीय परिवर्तनों के कारण भारत में कई प्लीस्टोसीन विशालकाय प्रजातियों में गिरावट और विलुप्ति हुई।"
)

add_tf(sec1_en, sec1_hi,
    "The Ganga Valley contains extensive archaeological evidence of Lower Paleolithic occupations.",
    "गंगा घाटी में निम्न पुरापाषाणकालीन बस्तियों के व्यापक पुरातात्विक साक्ष्य मिलते हैं।",
    False,
    "The Ganga Valley shows a complete absence of Paleolithic occupations; it was only colonized systematically during the Mesolithic due to Holocene stabilization.",
    "गंगा घाटी में पुरापाषाणकालीन बस्तियों का पूर्ण अभाव है; होलोसीन स्थिरता के कारण केवल मध्यपाषाण काल के दौरान ही वहां व्यवस्थित रूप से बसावट शुरू हुई थी।"
)

add_tf(sec1_en, sec1_hi,
    "Rise in monsoonal rains led to the expansion of vegetation and deciduous forests in Central India during the Mesolithic.",
    "मध्यपाषाण काल के दौरान मानसूनी बारिश में वृद्धि से मध्य भारत में वनस्पतियों और पर्णपाती वनों का विस्तार हुआ।",
    True,
    "Increased precipitation stimulated forest growth in Central India, creating a rich ecosystem for Mesolithic foragers.",
    "बढ़ी हुई वर्षा ने मध्य भारत में वनों के विकास को बढ़ावा दिया, जिससे मध्यपाषाणकालीन शिकारियों के लिए एक समृद्ध पारिस्थितिकी तंत्र का निर्माण हुआ।"
)

add_tf(sec1_en, sec1_hi,
    "Freshwater snail shells found at Ganga valley Mesolithic sites indicate the active exploitation of aquatic resources.",
    "गंगा घाटी के मध्यपाषाणकालीन स्थलों से मिले मीठे पानी के घोंघे के छिलके जलीय संसाधनों के सक्रिय दोहन को दर्शाते हैं।",
    True,
    "Freshwater mollusk shells indicate that aquatic resources were a crucial element of the broad-spectrum Mesolithic diet in the plains.",
    "मीठे पानी के घोंघों के छिलके दर्शाते हैं कि जलीय संसाधन मैदानों में व्यापक-स्पेक्ट्रम मध्यपाषाणकालीन आहार के एक महत्वपूर्ण तत्व थे।"
)

add_tf(sec1_en, sec1_hi,
    "The Holocene epoch began approximately 100,000 years ago.",
    "होलोसीन युग की शुरुआत लगभग 1,00,000 वर्ष पहले हुई थी।",
    False,
    "The Holocene epoch began around 11,700 years ago (c. 10,000 BCE).",
    "होलोसीन युग की शुरुआत लगभग 11,700 वर्ष पहले (लगभग 10,000 ईसा पूर्व) हुई थी।"
)

add_tf(sec1_en, sec1_hi,
    "The change in climate and prey types during the Holocene transition necessitated the invention of smaller, composite projectile tools.",
    "होलोसीन संक्रमण के दौरान जलवायु और शिकार के प्रकारों में बदलाव के कारण छोटे, संयुक्त प्रक्षेपास्त्र उपकरणों के आविष्कार की आवश्यकता हुई।",
    True,
    "Small, fast-moving game (like birds and deer) required lighter and faster projectile weapons, leading directly to microlithic technology.",
    "छोटे, तेज-तर्रार शिकार (जैसे पक्षी और हिरण) के लिए हल्के और तेज प्रक्षेपास्त्र हथियारों की आवश्यकता थी, जिससे सीधे सूक्ष्म पाषाण (microlithic) तकनीक का विकास हुआ।"
)

# --- 4. Fill in the Blank (8 Questions) ---
add_blank(sec1_en, sec1_hi,
    "The geological epoch that marks the beginning of the Mesolithic period is the ________.",
    "वह भूवैज्ञानिक युग जो मध्यपाषाण काल की शुरुआत को चिह्नित करता है, वह ________ है।",
    "Holocene", "होलोसीन",
    "The Holocene epoch succeeded the Pleistocene and represents the current warm post-glacial period.",
    "होलोसीन युग प्लीस्टोसीन के बाद आया और वर्तमान गर्म हिमनद-पश्चात (post-glacial) काल का प्रतिनिधित्व करता है।"
)

add_blank(sec1_en, sec1_hi,
    "During the early Holocene, the climate of India shifted from cold-arid to ________.",
    "प्रारंभिक होलोसीन के दौरान, भारत की जलवायु ठंडी-शुष्क से ________ में स्थानांतरित हो गई।",
    "warm-humid", "गर्म-आर्द्र",
    "The post-glacial warming cycle shifted climates to warm and humid across the subcontinent.",
    "हिमनद-पश्चात तापमान वृद्धि चक्र ने उपमहाद्वीप में जलवायु को गर्म और आर्द्र बना दिया।"
)

add_blank(sec1_en, sec1_hi,
    "The expansion of ________ forests in Central India provided rich plant and animal food resources for Mesolithic bands.",
    "मध्य भारत में ________ वनों के विस्तार ने मध्यपाषाणकालीन समूहों के लिए समृद्ध पौधों और जानवरों के खाद्य संसाधन प्रदान किए।",
    "deciduous", "पर्णपाती",
    "Deciduous forests flourished under higher monsoonal rainfall, replacing Pleistocene scrubland.",
    "उच्च मानसूनी वर्षा के कारण पर्णपाती वनों का विकास हुआ, जिसने प्लीस्टोसीन झाड़ियों का स्थान लिया।"
)

add_blank(sec1_en, sec1_hi,
    "In Western India, the increase in rainfall led to the stabilization of sub-humid ________ dunes.",
    "पश्चिमी भारत में, वर्षा में वृद्धि के कारण उप-आर्द्र ________ टीले स्थिर हो गए।",
    "sand", "रेत के",
    "Increased precipitation allowed vegetation to bind sand dunes, preventing wind erosion and creating habitable surfaces.",
    "बढ़ी हुई वर्षा ने वनस्पतियों को रेत के टीलों को बांधने में मदद की, जिससे हवा से होने वाला क्षरण रुका और रहने योग्य सतहों का निर्माण हुआ।"
)

add_blank(sec1_en, sec1_hi,
    "The systematic exploitation of rivers, oxbow lakes, and ponds for fish and turtles is termed ________ foraging.",
    "मछली और कछुओं के लिए नदियों, गोखुर झीलों और तालाबों का व्यवस्थित दोहन ________ भोजन जुटाने की विधि कहलाता है।",
    "aquatic", "जलीय",
    "Aquatic foraging became a major component of the broad-spectrum food economy in the Ganga valley.",
    "गंगा घाटी में व्यापक-स्पेक्ट्रम खाद्य अर्थव्यवस्था का एक प्रमुख हिस्सा जलीय भोजन जुटाना बन गया।"
)

add_blank(sec1_en, sec1_hi,
    "The earliest Mesolithic human occupations in the Ganga plain are located in the ________ district of Uttar Pradesh.",
    "गंगा के मैदान में सबसे प्रारंभिक मध्यपाषाणकालीन मानव बस्तियाँ उत्तर प्रदेश के ________ जिले में स्थित हैं।",
    "Pratapgarh", "प्रतापगढ़",
    "Pratapgarh district contains the landmark sites of Sarai Nahar Rai, Mahadaha, and Damdama.",
    "प्रतापगढ़ जिले में सराय नाहर राय, महदहा और दमदमा जैसे ऐतिहासिक स्थल स्थित हैं।"
)

add_blank(sec1_en, sec1_hi,
    "The Holocene epoch began around ________ BCE, marking the end of the Last Glacial Maximum.",
    "होलोसीन युग की शुरुआत लगभग ________ ईसा पूर्व हुई थी, जो अंतिम हिमनद काल के अंत का प्रतीक है।",
    "10000", "10000",
    "The geological boundary between Pleistocene and Holocene is placed at approximately 10,000 BCE.",
    "प्लीस्टोसीन और होलोसीन के बीच की भूवैज्ञानिक सीमा लगभग 10,000 ईसा पूर्व मानी जाती है।"
)

add_blank(sec1_en, sec1_hi,
    "Mesolithic sites in the Thar desert margins indicate that dunes became covered in grass due to increased ________.",
    "थार मरुस्थल के किनारों पर स्थित मध्यपाषाणकालीन स्थल यह दर्शाते हैं कि टीले बढ़ी हुई ________ के कारण घास से ढक गए थे।",
    "rainfall", "वर्षा",
    "Increased monsoonal rainfall stabilized Thar margins, allowing seasonal grasslands to develop.",
    "बढ़ी हुई मानसूनी वर्षा ने थार के किनारों को स्थिर कर दिया, जिससे मौसमी घास के मैदान विकसित हो सके।"
)

# --- 5. Match the Following (3 Questions) ---
add_match(sec1_en, sec1_hi,
    "Match the geological epoch and climatic phase with its characteristics:",
    "भूवैज्ञानिक युग और जलवायु चरण को उसकी विशेषताओं से सुमेलित करें:",
    ["1. Pleistocene Epoch", "2. Holocene Epoch", "3. Mesolithic Phase"],
    ["1. प्लीस्टोसीन युग", "2. होलोसीन युग", "3. मध्यपाषाण चरण"],
    ["A. Glacial cycles & extreme aridity", "B. Post-glacial warming & monsoons", "C. Transitional microlithic adaptation"],
    ["A. हिमनद चक्र और अत्यधिक शुष्कता", "B. हिमनद-पश्चात तापमान वृद्धि और मानसून", "C. संक्रमणकालीन सूक्ष्म पाषाण अनुकूलन"],
    "1-A, 2-B, 3-C. The Pleistocene was cold-arid; the Holocene is warm-humid; the Mesolithic represents the human cultural adaptation during this transition.",
    "1-A, 2-B, 3-C. प्लीस्टोसीन ठंडा-शुष्क था; होलोसीन गर्म-आर्द्र है; मध्यपाषाण काल इस संक्रमण के दौरान मानव सांस्कृतिक अनुकूलन का प्रतिनिधित्व करता है।"
)

add_match(sec1_en, sec1_hi,
    "Match the Indian region with its Holocene environmental adaptation:",
    "भारतीय क्षेत्र को उसके होलोसीन पर्यावरणीय अनुकूलन से सुमेलित करें:",
    ["1. Ganga Plain", "2. Thar Desert Margins", "3. Central Indian Hills"],
    ["1. गंगा का मैदान", "2. थार मरुस्थल के किनारे", "3. मध्य भारतीय पहाड़ियाँ"],
    ["A. Oxbow lake settlements & aquatic foraging", "B. Sand dune stabilization & seasonal playas", "C. Deciduous forest expansion & rock shelter occupation"],
    ["A. गोखुर झील बस्तियाँ और जलीय भोजन संग्रह", "B. रेत के टीलों का स्थिरीकरण और मौसमी झीलें", "C. पर्णपाती वनों का विस्तार और शैल आश्रय बस्तियाँ"],
    "1-A, 2-B, 3-C. The Ganga plain was rich in oxbow lakes; Western dunes stabilized with playas; Central hills developed rich deciduous forests and shelters.",
    "1-A, 2-B, 3-C. गंगा के मैदान गोखुर झीलों से समृद्ध थे; पश्चिमी रेत के टीले झीलों के साथ स्थिर हुए; मध्य पहाड़ियों में समृद्ध पर्णपाती वन और शैल आश्रय विकसित हुए।"
)

add_match(sec1_en, sec1_hi,
    "Match the faunal size categories with their archaeological context:",
    "जीवों के आकार की श्रेणियों को उनके पुरातात्विक संदर्भ से सुमेलित करें:",
    ["1. Megafauna (Elephants, Hippopotamus)", "2. Medium/Small Game (Deer, Boars)", "3. Microfauna (Snails, Fish)"],
    ["1. विशालकाय जीव (हाथी, दरियाई घोड़ा)", "2. मध्यम/छोटे जीव (हिरण, जंगली सूअर)", "3. सूक्ष्म जीव (घोंघे, मछली)"],
    ["A. Pleistocence dominance, declining in Holocene", "B. Holocene expansion, targeted by microlith arrows", "C. Exploded in lakes, base of broad-spectrum diet"],
    ["A. प्लीस्टोसीन में प्रभुत्व, होलोसीन में गिरावट", "B. होलोसीन में विस्तार, सूक्ष्म पाषाण तीरों का शिकार", "C. झीलों में प्रचुरता, व्यापक-स्पेक्ट्रम आहार का आधार"],
    "1-A, 2-B, 3-C. Megafauna declined with the Pleistocene end; medium game became the primary land target; microfauna supported broad-spectrum diet expansion.",
    "1-A, 2-B, 3-C. प्लीस्टोसीन की समाप्ति के साथ विशालकाय जीवों में कमी आई; मध्यम आकार के जीव मुख्य भूमि शिकार बन गए; सूक्ष्म जीवों ने व्यापक-स्पेक्ट्रम आहार विस्तार का समर्थन किया।"
)

# --- 6. One-Liner (8 Questions) ---
add_oneliner(sec1_en, sec1_hi,
    "What is the key defining feature of the Holocene epoch in the context of global climate?",
    "वैश्विक जलवायु के संदर्भ में होलोसीन युग की प्रमुख परिभाषित विशेषता क्या है?",
    "Global warming and transition to post-glacial humid conditions.",
    "वैश्विक तापमान में वृद्धि और हिमनद-पश्चात (post-glacial) आर्द्र परिस्थितियों में संक्रमण।"
)

add_oneliner(sec1_en, sec1_hi,
    "Why did the diversity of human diet expand during the Mesolithic?",
    "मध्यपाषाण काल के दौरान मानव आहार की विविधता का विस्तार क्यों हुआ?",
    "Warming expanded floral and faunal resources, leading to broad-spectrum foraging of plants, birds, and aquatic life.",
    "तापमान में वृद्धि से वनस्पतियों और जीवों का विस्तार हुआ, जिससे पौधों, पक्षियों और जलीय जीवों के व्यापक-स्पेक्ट्रम संग्रह को बढ़ावा मिला।"
)

add_oneliner(sec1_en, sec1_hi,
    "What geological transition corresponds directly to the start of the Indian Mesolithic?",
    "कौन सा भूवैज्ञानिक संक्रमण सीधे तौर पर भारतीय मध्यपाषाण काल की शुरुआत से मेल खाता है?",
    "The transition from the Pleistocene to the Holocene epoch.",
    "प्लीस्टोसीन युग से होलोसीन युग में होने वाला संक्रमण।"
)

add_oneliner(sec1_en, sec1_hi,
    "Why did the Ganga Plain remain uninhabited by Paleolithic humans?",
    "गंगा का मैदान पुरापाषाणकालीन मनुष्यों द्वारा निर्जन क्यों रहा?",
    "Due to extreme cold-arid conditions and high marshy, unstable river channels during the Pleistocene.",
    "प्लीस्टोसीन के दौरान अत्यधिक ठंडी-शुष्क परिस्थितियों और दलदली, अस्थिर नदी मार्गों के कारण।"
)

add_oneliner(sec1_en, sec1_hi,
    "How did the shrinkage of tool size relate to faunal changes in the Holocene?",
    "होलोसीन में औजारों के आकार का छोटा होना जीवों में आए परिवर्तनों से कैसे संबंधित था?",
    "Smaller, faster prey (deer, birds) required lightweight projectile tools like microlithic arrowheads.",
    "छोटे और तेज जीवों (हिरण, पक्षी) के शिकार के लिए हल्के प्रक्षेपास्त्र उपकरणों जैसे सूक्ष्म पाषाण वाले तीरों की आवश्यकता थी।"
)

add_oneliner(sec1_en, sec1_hi,
    "Which mineral group replaced quartzite as the primary raw material during the Mesolithic?",
    "मध्यपाषाण काल के दौरान प्राथमिक कच्चे माल के रूप में किस खनिज समूह ने क्वार्ट्जाइट का स्थान लिया?",
    "Fine-grained cryptocrystalline silica minerals (chert, chalcedony, jasper, agate).",
    "महीन सिलिका खनिजों (चर्ट, चाल्सीडोनी, जैस्पर, अगेट) के समूह ने।"
)

add_oneliner(sec1_en, sec1_hi,
    "What is the archaeological term for a diet utilizing wild grains, small game, fish, and mollusks?",
    "जंगली अनाज, छोटे शिकार, मछली और घोंघों का उपयोग करने वाले आहार का पुरातात्विक नाम क्या है?",
    "Broad-Spectrum Economy / Foraging.",
    "व्यापक-स्पेक्ट्रम अर्थव्यवस्था (Broad-Spectrum Economy) या व्यापक भोजन संग्रह।"
)

add_oneliner(sec1_en, sec1_hi,
    "How did sand dunes in Gujarat support Mesolithic camps?",
    "गुजरात में रेत के टीलों ने मध्यपाषाणकालीन शिविरों को कैसे सहारा दिया?",
    "Stabilized dunes provided elevated dry land to camp on near seasonal freshwater lakes.",
    "स्थिर टीलों ने मौसमी मीठे पानी की झीलों के पास शिविर लगाने के लिए ऊंचे सूखे स्थान प्रदान किए।"
)

# --- 7. Assertion-Reason (8 Questions) ---
add_ar(sec1_en, sec1_hi,
    "Assertion (A): The density of human population in India was significantly higher during the Mesolithic than the Paleolithic.\nReason (R): The warm-humid Holocene climate expanded the carry capacity of the ecosystem, increasing edible biomass.",
    "कथन (A): पुरापाषाण काल की तुलना में मध्यपाषाण काल के दौरान भारत में मानव जनसंख्या का घनत्व काफी अधिक था।\nकारण (R): गर्म-आर्द्र होलोसीन जलवायु ने पारिस्थितिकी तंत्र की वहन क्षमता (carrying capacity) का विस्तार किया, जिससे खाद्य बायोमास में वृद्धि हुई।",
    0,
    "Both A and R are true, and R is the correct explanation. Edible biomass expansion directly allowed higher population density.",
    "A और R दोनों सही हैं, और R सही व्याख्या करता है। खाद्य बायोमास के विस्तार ने सीधे तौर पर उच्च जनसंख्या घनत्व को संभव बनाया।"
)

add_ar(sec1_en, sec1_hi,
    "Assertion (A): Ganga Valley Mesolithic sites yield thick layers of freshwater mollusk shells.\nReason (R): Mesolithic groups relied heavily on aquatic foraging to supplement their diet in the river plains.",
    "कथन (A): गंगा घाटी के मध्यपाषाणकालीन स्थलों से मीठे पानी के घोंघों के छिलकों की मोटी परतें मिलती हैं।\nकारण (R): मैदानी इलाकों में अपने आहार की पूर्ति के लिए मध्यपाषाणकालीन समूह जलीय भोजन जुटाने पर बहुत अधिक निर्भर थे।",
    0,
    "Both A and R are true, and R explains the presence of snail shells as dietary remnants of aquatic foraging.",
    "A और R दोनों सही हैं, और R जलीय खोज को घोंघे के छिलकों की उपस्थिति के रूप में समझाता है।"
)

add_ar(sec1_en, sec1_hi,
    "Assertion (A): The transition to the Holocene caused Pleistocene megafauna to expand in number across the Indian peninsula.\nReason (R): Post-glacial warming brought extreme glacial conditions that favored massive cold-adapted mammals.",
    "कथन (A): होलोसीन संक्रमण के कारण भारतीय उपमहाद्वीप में प्लीस्टोसीन विशालकाय जीवों की संख्या में वृद्धि हुई।\nकारण (R): हिमनद-पश्चात वार्मिंग से अत्यधिक हिमनद स्थितियां पैदा हुईं जो बड़े ठंड-अनुकूल स्तनधारियों के अनुकूल थीं।",
    3,
    "A is false because megafauna declined; R is false because post-glacial warming reduced glacial conditions.",
    "A गलत है क्योंकि विशालकाय जीवों में कमी आई; R गलत है क्योंकि हिमनद-पश्चात वार्मिंग ने हिमनद स्थितियों को कम किया।"
)

add_ar(sec1_en, sec1_hi,
    "Assertion (A): Stabilized sand dunes in Western India were favored locations for Mesolithic camps.\nReason (R): Dunes provided elevated, dry ground that remained safe from seasonal flooding of adjacent lakes (playas).",
    "कथन (A): पश्चिमी भारत में स्थिर रेत के टीले मध्यपाषाणकालीन शिविरों के लिए पसंदीदा स्थान थे।\nकारण (R): टीलों ने ऊंचे, सूखे स्थान प्रदान किए जो पास की झीलों (playas) में आने वाली मौसमी बाढ़ से सुरक्षित रहते थे।",
    0,
    "Both statements are true, and dune heights provided dry refuge near water sources, which explains their occupational density.",
    "दोनों कथन सही हैं, और टीले की ऊंचाई ने जल स्रोतों के पास सूखा आश्रय प्रदान किया, जो उनके आवासीय घनत्व को समझाता है।"
)

add_ar(sec1_en, sec1_hi,
    "Assertion (A): Microlithic projectile technology emerged as a critical adaptation in the early Holocene.\nReason (R): Heavy Acheulian handaxes were highly inefficient for hunting small, fast-moving game like deer and birds.",
    "कथन (A): प्रारंभिक होलोसीन में सूक्ष्म पाषाण प्रक्षेपास्त्र तकनीक एक महत्वपूर्ण अनुकूलन के रूप में उभरी।\nकारण (R): हिरण और पक्षियों जैसे छोटे, तेज-तर्रार जीवों के शिकार के लिए भारी एशुलेयिन हस्तकुठार अत्यधिक अप्रभावी थे।",
    0,
    "Both statements are true. The shift in game size made large tools obsolete and drove the invention of microliths.",
    "दोनों कथन सही हैं। शिकार के आकार में बदलाव ने बड़े उपकरणों को अप्रचलित बना दिया और सूक्ष्म पाषाणों के आविष्कार को प्रेरित किया।"
)

add_ar(sec1_en, sec1_hi,
    "Assertion (A): The end of the Pleistocene epoch around 10,000 BCE led directly to the establishment of brick-built farming towns in the Ganga valley.\nReason (R): Agriculture cannot exist in any form during glacial epochs.",
    "कथन (A): लगभग 10,000 ईसा पूर्व में प्लीस्टोसीन युग की समाप्ति से सीधे गंगा घाटी में ईंटों से बने कृषि कस्बों की स्थापना हुई।\nकारण (R): हिमनद युग के दौरान कृषि किसी भी रूप में अस्तित्व में नहीं रह सकती है।",
    3,
    "A is false because brick-built towns belong to much later historical phases; Mesolithic was non-agricultural. R is true as cold-arid glaciers prevent systematic farming.",
    "A गलत है क्योंकि ईंटों से बने कस्बे बहुत बाद के ऐतिहासिक चरणों के हैं; मध्यपाषाण काल गैर-कृषि प्रधान था। R सही है क्योंकि ठंडा-शुष्क हिमनद वातावरण कृषि को रोकता है।"
)

add_ar(sec1_en, sec1_hi,
    "Assertion (A): Mesolithic hunter-gatherer bands colonised the Ganga Plain for the first time during the early Holocene.\nReason (R): Shifting monsoonal cycles stabilized river channels, creating rich resource margins around oxbow lakes.",
    "कथन (A): प्रारंभिक होलोसीन के दौरान मध्यपाषाणकालीन शिकारी-संग्रहकर्ता समूहों ने पहली बार गंगा के मैदान पर बस्तियां बसाईं।\nकारण (R): बदलते मानसूनी चक्रों ने नदी के मार्गों को स्थिर किया, जिससे गोखुर झीलों के पास समृद्ध संसाधन क्षेत्र बने।",
    0,
    "Both are true and R explains why the Ganga plain became habitable and attractive during the Mesolithic.",
    "दोनों सही हैं और R स्पष्ट करता है कि गंगा का मैदान मध्यपाषाण काल के दौरान रहने योग्य और आकर्षक क्यों बन गया।"
)

add_ar(sec1_en, sec1_hi,
    "Assertion (A): Quartzite remained the exclusive raw material for stone tools throughout all phases of prehistory.\nReason (R): Fine silica minerals like chert and chalcedony were too soft to be chipped into sharp points.",
    "कथन (A): प्रागैतिहास के सभी चरणों में क्वार्ट्जाइट पत्थर के औजारों के लिए एकमात्र कच्चा माल बना रहा।\nकारण (R): चर्ट और चाल्सीडोनी जैसे महीन सिलिका खनिज इतने नरम थे कि उन्हें तेज नोकदार औजारों में नहीं बदला जा सकता था।",
    3,
    "A is false as chert/chalcedony replaced quartzite in Mesolithic. R is false as chert/chalcedony fracture cleanly to produce extremely sharp edges.",
    "A गलत है क्योंकि मध्यपाषाण काल में चर्ट/चाल्सीडोनी ने क्वार्ट्जाइट का स्थान लिया। R गलत है क्योंकि चर्ट/चाल्सीडोनी अत्यंत तीखे किनारे बनाने के लिए आसानी से टूटते हैं।"
)

# --- 8. Statement-Based (5 Questions) ---
add_stmt(sec1_en, sec1_hi,
    "Consider the following statements regarding the Holocene climatic transition in India:\n1. The monsoon rains became stronger, leading to the expansion of vegetation.\n2. The arid scrub forests of Central India were replaced by tropical deciduous forests.\nWhich of the statements given above is/are correct?",
    "भारत में होलोसीन जलवायु संक्रमण के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. मानसूनी बारिश तेज हो गई, जिससे वनस्पतियों का विस्तार हुआ।\n2. मध्य भारत के शुष्क झाड़ीदार वनों का स्थान उष्णकटिबंधीय पर्णपाती वनों ने ले लिया।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
    2,
    "Both statements are correct. Enhanced monsoons promoted forest growth and shifted Central Indian scrub forests to deciduous vegetation.",
    "दोनों कथन सही हैं। उन्नत मानसून ने वनों के विकास को बढ़ावा दिया और मध्य भारतीय झाड़ीदार वनों को पर्णपाती वनस्पति में बदल दिया।"
)

add_stmt(sec1_en, sec1_hi,
    "With reference to the colonization of the Ganga Valley in the Mesolithic phase, consider the following statements:\n1. Sarai Nahar Rai and Mahadaha show the earliest human occupations in these alluvial plains.\n2. The sites were occupied year-round due to the development of intensive wheat farming.\nWhich of the statements given above is/are correct?",
    "मध्यपाषाण चरण में गंगा घाटी के बसने के संदर्भ में, निम्नलिखित कथनों पर विचार करें:\n1. सराय नाहर राय और महदहा इन जलोढ़ मैदानों में सबसे प्रारंभिक मानव बस्तियों को दर्शाते हैं।\n2. गहन गेहूं की खेती के विकास के कारण इन स्थलों पर पूरे वर्ष निवास किया जाता था।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
    0,
    "Statement 1 is correct. Statement 2 is incorrect because Mesolithic groups were hunter-gatherers and did not practice wheat farming.",
    "कथन 1 सही है। कथन 2 गलत है क्योंकि मध्यपाषाणकालीन समूह शिकारी-संग्रहकर्ता थे और वे गेहूं की खेती नहीं करते थे।"
)

add_stmt(sec1_en, sec1_hi,
    "Consider the following statements regarding the 'broad-spectrum revolution' in the Mesolithic diet:\n1. Diet became restricted exclusively to large game hunting.\n2. It involved the exploitation of aquatic fauna such as fish, turtles, and mollusks.\nWhich of the statements given above is/are correct?",
    "मध्यपाषाणकालीन आहार में 'व्यापक-स्पेक्ट्रम क्रांति' (broad-spectrum revolution) के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. आहार विशेष रूप से केवल बड़े जानवरों के शिकार तक सीमित हो गया था।\n2. इसमें जलीय जीवों जैसे मछली, कछुए और घोंघों का दोहन शामिल था।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
    1,
    "Statement 1 is incorrect as diet diversified. Statement 2 is correct, showing the expansion to aquatic food sources.",
    "कथन 1 गलत है क्योंकि आहार विविध हो गया था। कथन 2 सही है, जो जलीय खाद्य स्रोतों के विस्तार को दर्शाता है।"
)

add_stmt(sec1_en, sec1_hi,
    "Consider the following statements regarding Western Indian sand dunes in the Holocene:\n1. Increased precipitation stabilized the sand dunes with grass cover.\n2. Stabilized sand dunes provided elevated camping sites close to water bodies.\nWhich of the statements given above is/are correct?",
    "होलोसीन में पश्चिमी भारतीय रेत के टीलों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. बढ़ी हुई वर्षा ने रेत के टीलों को घास के आवरण से स्थिर कर दिया।\n2. स्थिर टीलों ने जल निकायों के करीब ऊंचे शिविर स्थल प्रदान किए।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
    2,
    "Both statements are correct. Holocene rains grassed the dunes, creating dry, safe camping mounds next to rainwater basins.",
    "दोनों कथन सही हैं। होलोसीन वर्षा ने टीलों पर घास उगाई, जिससे वर्षा के गड्ढों के बगल में सूखे, सुरक्षित शिविर टीले बने।"
)

add_stmt(sec1_en, sec1_hi,
    "Consider the following statements regarding demographic shifts in the Mesolithic phase:\n1. The geographical range of human settlements decreased significantly.\n2. The number of recorded archaeological sites is much higher than in the preceding Paleolithic phase.\nWhich of the statements given above is/are correct?",
    "मध्यपाषाण चरण में जनसांख्यिकीय बदलावों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. मानव बस्तियों का भौगोलिक दायरा काफी कम हो गया।\n2. दर्ज किए गए पुरातात्विक स्थलों की संख्या पूर्ववर्ती पुरापाषाण चरण की तुलना में बहुत अधिक है।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
    1,
    "Statement 1 is incorrect because the geographical range expanded to new areas like the Ganga plains. Statement 2 is correct, reflecting population growth.",
    "कथन 1 गलत है क्योंकि भौगोलिक दायरे का विस्तार गंगा के मैदानों जैसे नए क्षेत्रों में हुआ। कथन 2 सही है, जो जनसंख्या वृद्धि को दर्शाता है।"
)

# --- 9. Why (3 Questions) ---
add_open(sec1_en, sec1_hi, "Why",
    "Why did the transition to the Holocene trigger a reduction in the size of prehistoric stone tools?",
    "होलोसीन में संक्रमण ने प्रागैतिहासिक पत्थर के औजारों के आकार में कमी को क्यों प्रेरित किया?",
    "The warming climate replaced Pleistocene megafauna with smaller, agile animals like deer and birds. Heavy Paleolithic handaxes were ineffective for hunting these fast creatures. Hominins created miniature, light microlithic arrowheads and spear points to hunt smaller game effectively.",
    "गर्म होती जलवायु ने प्लीस्टोसीन विशालकाय जीवों को हिरण और पक्षियों जैसे छोटे, फुर्तीले जानवरों से प्रतिस्थापित कर दिया। इन तेज जीवों के शिकार के लिए भारी पुरापाषाणकालीन हस्तकुठार अप्रभावी थे। आदिम मानवों ने छोटे शिकार को प्रभावी ढंग से मारने के लिए लघु, हल्के प्रक्षेपास्त्र औजार (microliths) बनाए।"
)

add_open(sec1_en, sec1_hi, "Why",
    "Why did the Ganga Plain witness human settlements only during the Holocene Mesolithic phase, not earlier?",
    "गंगा के मैदान में केवल होलोसीन मध्यपाषाण चरण के दौरान ही मानव बस्तियाँ क्यों देखी गईं, उससे पहले क्यों नहीं?",
    "During the Pleistocene, the Ganga basin was cold-arid with unstable, rapidly shifting torrents and dense marshes. The Holocene warming brought stable monsoonal rainfall, creating predictable river flows, fertile grass plains, and perennial oxbow lakes rich in aquatic life, making the plain habitable.",
    "प्लीस्टोसीन के दौरान, गंगा बेसिन अस्थिर, तेजी से बहने वाली धाराओं और घने दलदलों के साथ ठंडा-शुष्क था। होलोसीन वार्मिंग ने स्थिर मानसूनी वर्षा प्रदान की, जिससे नदी का बहाव नियंत्रित हुआ, उपजाऊ घास के मैदान बने और जलीय जीवन से समृद्ध गोखुर झीलें बनीं, जिससे मैदान रहने योग्य बन गया।"
)

add_open(sec1_en, sec1_hi, "Why",
    "Why is the Mesolithic period characterized as a 'transitional' economic phase?",
    "मध्यपाषाण काल को एक 'संक्रमणकालीन' आर्थिक चरण के रूप में क्यों वर्गीकृत किया जाता है?",
    "It bridges the gap between the nomadic, opportunistic hunting-gathering lifestyle of the Paleolithic and the sedentary, food-producing farming economy of the Neolithic. Mesolithic groups maintained hunting-gathering but introduced early animal husbandry and intensive foraging.",
    "यह पुरापाषाण काल की घुमंतू, शिकार-संग्रह जीवन शैली और नवपाषाण काल की स्थायी, भोजन उत्पादक कृषि अर्थव्यवस्था के बीच की खाई को पाटता है। मध्यपाषाणकालीन समूहों ने शिकार-संग्रह जारी रखा लेकिन प्रारंभिक पशुपालन और व्यापक खाद्य संग्रह की शुरुआत की।"
)

# --- 10. How (3 Questions) ---
add_open(sec1_en, sec1_hi, "How",
    "How did the stabilization of sand dunes in Western India assist Mesolithic settlement patterns?",
    "पश्चिमी भारत में रेत के टीलों के स्थिरीकरण ने मध्यपाषाणकालीन बस्ती प्रतिरूपों (settlement patterns) में कैसे मदद की?",
    "Increased Holocene rainfall stabilized dunes with vegetation cover, preventing erosion. These grass-covered dunes provided elevated dry land that served as safe camp mounds adjacent to seasonal rainwater ponds (playas), providing both shelter and fresh water.",
    "होलोसीन में बढ़ी हुई वर्षा ने वनस्पति आवरण के साथ टीलों को स्थिर किया, जिससे उनका क्षरण रुका। इन घास वाले टीलों ने ऊंचे सूखे स्थान प्रदान किए जो मौसमी मीठे पानी के गड्ढों (playas) के बगल में सुरक्षित शिविर टीलों के रूप में काम करते थे।"
)

add_open(sec1_en, sec1_hi, "How",
    "How do archaeologists identify the 'broad-spectrum revolution' from faunal remains at Mesolithic sites?",
    "पुरातत्वविद मध्यपाषाणकालीन स्थलों पर जीवों के अवशेषों (faunal remains) से 'व्यापक-स्पेक्ट्रम क्रांति' की पहचान कैसे करते हैं?",
    "Instead of finding only bones of large cattle and elephants (typical of Paleolithic layers), excavations show high percentages of small game bones (deer, boars, birds) along with large deposits of freshwater snail shells, fish bones, and turtle shells, indicating dietary diversification.",
    "केवल बड़े मवेशियों और हाथियों की हड्डियों (जो पुरापाषाणकालीन परतों की विशेषता हैं) को खोजने के बजाय, उत्खनन से छोटे जीवों (हिरण, जंगली सूअर, पक्षी) की हड्डियों के उच्च प्रतिशत के साथ-साथ मीठे पानी के घोंघों के छिलकों, मछली और कछुओं के अवशेष मिलते हैं।"
)

add_open(sec1_en, sec1_hi, "How",
    "How did monsoonal forest expansion influence the seasonal mobility of Mesolithic bands?",
    "मानसूनी वनों के विस्तार ने मध्यपाषाणकालीन समूहों की मौसमी गतिशीलता (seasonal mobility) को कैसे प्रभावित किया?",
    "Forest growth expanded plant foods like wild berries, tubers, and fruits. Bands developed seasonal migration paths, aggregating near permanent lakes during dry winters and dispersing into forest zones during monsoons to harvest shifting seasonal resources.",
    "वनों के विकास से जंगली कंद, फल और बेर जैसी खाद्य सामग्री का विस्तार हुआ। मानव समूहों ने मौसमी प्रवास मार्ग विकसित किए, शुष्क सर्दियों में स्थायी झीलों के पास इकट्ठा होते थे और मानसून के दौरान विभिन्न वन संसाधनों को इकट्ठा करने के लिए जंगलों में बिखर जाते थे।"
)

# --- 11. Case Study (3 Questions) ---
add_open(sec1_en, sec1_hi, "Case Study",
    "Case Study: Pratapgarh Ganga Plain Hydrology.\nExplain how Holocene hydrological changes allowed the earliest human settlements in Uttar Pradesh.",
    "मामला अध्ययन: प्रतापगढ़ गंगा मैदान जलविज्ञान (Hydrology)।\nस्पष्ट करें कि होलोसीन के जलविज्ञानी परिवर्तनों ने उत्तर प्रदेश में सबसे प्रारंभिक मानव बस्तियों को कैसे संभव बनाया।",
    "During the early Holocene, monsoon rains caused the Ganga tributaries to migrate across the plains. As river courses shifted, they left behind crescent-shaped oxbow lakes. These lakes stabilized as perennial water bodies. Sites like Sarai Nahar Rai and Mahadaha were established right along these oxbow margins, exploiting their abundant fish, turtles, waterbirds, and plant resources, anchoring human occupation in the plains for the first time.",
    "प्रारंभिक होलोसीन के दौरान, मानसूनी बारिश के कारण गंगा की सहायक नदियों ने अपना मार्ग बदला। जैसे ही नदियों के मार्ग बदले, वे पीछे अर्धचंद्राकार गोखुर झीलें (oxbow lakes) छोड़ गए। ये झीलें बारहमासी जल निकायों के रूप में स्थिर हो गईं। सराय नाहर राय और महदहा जैसे स्थल इन झीलों के किनारे स्थापित किए गए, जिससे उनके प्रचुर जलीय जीवन और पक्षियों का दोहन संभव हुआ और मैदानी इलाकों में पहली बार मानव बस्ती स्थापित हुई।"
)

add_open(sec1_en, sec1_hi, "Case Study",
    "Case Study: Thar Desert Margins (16R Dune Profile).\nExplain how the stratigraphic sequence of Rajasthan dunes records the Pleistocene-Holocene climate transition.",
    "मामला अध्ययन: थार मरुस्थल के किनारे (16R टीला आरेख)।\nस्पष्ट करें कि राजस्थान के टीलों का स्तरविन्यासात्मक (stratigraphic) अनुक्रम कैसे प्लीस्टोसीन-होलोसीन जलवायु संक्रमण को रिकॉर्ड करता है।",
    "Excavations at the 16R dune near Didwana expose a deep stratigraphic column. The lower Pleistocene layers consist of thick wind-blown sand without soil structure, representing hyper-aridity. The transition to the Holocene is marked by fossilized root-casts, calcified soil layers, and rich microlithic horizons, proving that increased moisture and vegetation stabilized the sand, allowing humans to camp on the dune surfaces.",
    "डीडवाना के पास 16R टीले की खुदाई से एक गहरा स्तरविन्यासात्मक स्तंभ सामने आता है। निचली प्लीस्टोसीन परतों में मिट्टी की संरचना के बिना मोटी उड़ती हुई रेत शामिल है, जो अत्यधिक शुष्कता को दर्शाती है। होलोसीन के संक्रमण को जीवाश्मीकृत जड़ों के सांचे, कैल्शियम युक्त मिट्टी की परतों और समृद्ध सूक्ष्म पाषाण स्तरों द्वारा चिह्नित किया गया है, जो साबित करता है कि नमी और वनस्पति ने रेत को स्थिर किया, जिससे मनुष्यों को टीलों पर शिविर लगाने का अवसर मिला।"
)

add_open(sec1_en, sec1_hi, "Case Study",
    "Case Study: Sabarmati Basin Sand Dune Excavatons.\nDescribe how interdisciplinary research at Langhnaj established the relationship between dune soils and Mesolithic occupancy.",
    "मामला अध्ययन: साबरमती बेसिन रेत के टीले का उत्खनन।\nवर्णन करें कि लांघनाज में अंतःविषय अनुसंधान ने टीले की मिट्टी और मध्यपाषाणकालीन निवास के बीच संबंध को कैसे स्थापित किया।",
    "H.D. Sankalia analyzed the soil profiles of Langhnaj dunes. He found that the lower layers consisted of yellow wind-blown sand devoid of human activity. The middle layer showed soil weathering (humus development), animal bones, and dense microliths, proving that a wetter Holocene phase stabilized the dune, allowed vegetation growth, and created an attractive, stable campsite for Mesolithic hunter-gatherers.",
    "एच.डी. सांकलिया ने लांघनाज टीलों की मिट्टी के प्रोफाइल का विश्लेषण किया। उन्होंने पाया कि निचली परतें मानव गतिविधि से रहित पीली हवा से उड़ने वाली रेत की थीं। मध्यम परत में मिट्टी का अपक्षय (उर्वरक विकास), जानवरों की हड्डियाँ और सघन सूक्ष्म पाषाण दिखाई दिए, जो साबित करता है कि एक गीले होलोसीन चरण ने टीले को स्थिर किया, वनस्पति के विकास को बढ़ावा दिया, और मध्यपाषाणकालीन शिकारियों के लिए एक आकर्षक शिविर बनाया।"
)

# --- 12. Teach the Concept (3 Questions) ---
add_open(sec1_en, sec1_hi, "Teach the Concept",
    "Teach the Concept: Explain the differences between Pleistocene and Holocene climates in India using a simple comparison.",
    "अवधारणा समझाएं: एक सरल तुलना का उपयोग करके भारत में प्लीस्टोसीन और होलोसीन जलवायु के बीच अंतर को समझाएं।",
    "Imagine the Pleistocene as a long cold, dry winter where water is locked up, deserts are expanding, and vegetation is scarce. Handaxes were big and clumsy. The Holocene is like the arrival of a warm, rainy spring: monsoon rains arrive, rivers flow, grasslands stabilize, and forests bloom. The landscape comes alive with smaller animals, prompting humans to shrink their tools into microliths.",
    "प्लीस्टोसीन की कल्पना एक लंबी ठंडी, शुष्क सर्दियों के रूप में करें जहाँ पानी जमा हुआ है, मरुस्थल फैल रहे हैं, और वनस्पतियाँ दुर्लभ हैं। इस दौरान हस्तकुठार बड़े और भारी थे। होलोसीन एक गर्म, बरसाती वसंत के आगमन जैसा है: मानसूनी बारिश शुरू होती है, नदियाँ बहती हैं, घास के मैदान स्थिर होते हैं, और वन विकसित होते हैं। छोटे जानवरों की प्रचुरता के कारण इंसानों ने अपने औजारों को छोटा करके सूक्ष्म पाषाण बना लिया।"
)

add_open(sec1_en, sec1_hi, "Teach the Concept",
    "Teach the Concept: Explain the ecological concept of 'Carrying Capacity' and why it increased during the Mesolithic phase.",
    "अवधारणा समझाएं: 'वहन क्षमता' (Carrying Capacity) की पारिस्थितिक अवधारणा को समझाएं और यह भी बताएं कि मध्यपाषाण चरण के दौरान यह क्यों बढ़ गई।",
    "Carrying capacity is the maximum population size that an environment's resources can support without damage. During the dry Pleistocene, resources were scarce, keeping human populations small. The warm, wet Holocene increased carrying capacity by expanding forests and wetlands. This provided more wild grains, deer, fish, and birds, allowing the same territory to feed much larger bands, leading to the population boom of the Mesolithic.",
    "वहन क्षमता (Carrying capacity) किसी पर्यावरण के संसाधनों द्वारा बिना किसी नुकसान के समर्थित की जा सकने वाली अधिकतम जनसंख्या का आकार है। शुष्क प्लीस्टोसीन के दौरान संसाधन दुर्लभ थे, जिससे मानव आबादी कम रही। गर्म, आर्द्र होलोसीन ने जंगलों और आर्द्रभूमियों का विस्तार करके वहन क्षमता में वृद्धि की। इसने अधिक जंगली अनाज, हिरण, मछली और पक्षी प्रदान किए, जिससे एक ही क्षेत्र में बड़ी आबादी का भरण-पोषण संभव हुआ।"
)

add_open(sec1_en, sec1_hi, "Teach the Concept",
    "Teach the Concept: Explain the 'Broad-Spectrum Revolution' to a high school student.",
    "अवधारणा समझाएं: एक हाई स्कूल के छात्र को 'व्यापक-स्पेक्ट्रम क्रांति' (Broad-Spectrum Revolution) समझाएं।",
    "Imagine going to a restaurant where the menu only has one item: a giant steak. If the steak runs out, you starve. That was the Paleolithic hunter who focused only on large mammals. The Broad-Spectrum Revolution is when the restaurant updates its menu to include chicken, fish, salads, berries, and soup. Mesolithic humans shifted from hunting only big game to collecting wild seeds, birds, fish, and snails, securing their food supply.",
    "एक ऐसे रेस्तरां में जाने की कल्पना करें जहां मेनू में केवल एक ही चीज है: एक बड़ा स्टेक। यदि स्टेक समाप्त हो जाता है, तो आप भूखे रह जाएंगे। यह पुरापाषाणकालीन शिकारी था जो केवल बड़े स्तनधारियों पर ध्यान केंद्रित करता था। व्यापक-स्पेक्ट्रम क्रांति वह है जब रेस्तरां अपने मेनू को अपडेट करता है और उसमें चिकन, मछली, सलाद, जामुन और सूप शामिल करता है। मध्यपाषाणकालीन मनुष्यों ने केवल बड़े शिकार के बजाय जंगली बीज, पक्षी, मछली और घोंघे इकट्ठा करना शुरू किया, जिससे उनका भोजन सुरक्षित हुआ।"
)
