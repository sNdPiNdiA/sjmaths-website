from .helpers import add_mcq, add_multi_mcq, add_tf, add_blank, add_match, add_oneliner, add_ar, add_stmt, add_open

sec4_en = []
sec4_hi = []

# --- 1. MCQ (5 Questions) ---
add_mcq(sec4_en, sec4_hi,
    "Which two sites provide the earliest evidence of animal domestication in India, dating to approximately 5000 BCE?",
    "कौन से दो स्थल भारत में पशुपालन का सबसे पहला प्रमाण देते हैं, जो लगभग 5000 ईसा पूर्व के हैं?",
    ["Sarai Nahar Rai and Damdama", "Bagor and Adamgarh", "Langhnaj and Mahadaha", "Bhimbetka and Nevasa"],
    ["सराय नाहर राय और दमदमा", "बागोर और आदमगढ़", "लांघनाज और महदहा", "भीमबेटका और नेवासा"],
    1,
    "Bagor (Rajasthan) and Adamgarh (MP) yield the earliest evidence of domesticated cattle, sheep, and goats in India, dating to c. 5000 BCE.",
    "बागोर (राजस्थान) और आदमगढ़ (मध्य प्रदेश) भारत में पालतू मवेशियों, भेड़ों और बकरियों का सबसे पहला प्रमाण देते हैं, जो लगभग 5000 ईसा पूर्व के हैं।"
)

add_mcq(sec4_en, sec4_hi,
    "Which economic strategy is best described as 'utilizing a wide variety of food sources including plants, small animals, fish, and mollusks rather than specializing in one prey type'?",
    "किस आर्थिक रणनीति को 'एक शिकार प्रकार में विशेषज्ञता के बजाय पौधों, छोटे जानवरों, मछलियों और घोंघों सहित खाद्य स्रोतों की एक विस्तृत विविधता का उपयोग करना' के रूप में सबसे अच्छी तरह वर्णित किया जा सकता है?",
    ["Intensive agriculture", "Broad-spectrum foraging", "Pastoral nomadism", "Sedentary horticulture"],
    ["गहन कृषि", "व्यापक-स्पेक्ट्रम भोजन संग्रह", "पशुचारण खानाबदोशी", "स्थायी बागवानी"],
    1,
    "Broad-spectrum foraging describes the diversified food-collection strategy characteristic of the Mesolithic period.",
    "व्यापक-स्पेक्ट्रम भोजन संग्रह मध्यपाषाण काल की विविधीकृत खाद्य-संग्रहण रणनीति का वर्णन करता है।"
)

add_mcq(sec4_en, sec4_hi,
    "Which animal species were first domesticated at Bagor, as shown by its bone assemblages?",
    "बागोर में पहली बार कौन सी पशु प्रजातियाँ पालतू बनाई गई थीं, जैसा कि उसके हड्डी के समूह से पता चलता है?",
    ["Horse and camel", "Humped cattle, sheep, and goats", "Elephant and rhinoceros", "Tiger and wolf"],
    ["घोड़ा और ऊंट", "कूबड़ वाले मवेशी, भेड़ और बकरी", "हाथी और गैंडा", "बाघ और भेड़िया"],
    1,
    "Zooarchaeological analysis of Bagor Phase I shows humped cattle (zebu), sheep, and goats being domesticated — earliest such evidence in India.",
    "बागोर प्रथम चरण के पशु-पुरातात्विक विश्लेषण से पता चलता है कि कूबड़ वाले मवेशी (zebu), भेड़ और बकरियाँ पालतू बनाई जा रही थीं — यह भारत में ऐसा सबसे पहला साक्ष्य है।"
)

add_mcq(sec4_en, sec4_hi,
    "Which site yielded double burials with bone ornaments (necklaces) as grave goods?",
    "किस स्थल से कब्र के सामान के रूप में हड्डी के आभूषणों (हार) के साथ दोहरी कब्रें मिली हैं?",
    ["Damdama", "Langhnaj", "Mahadaha", "Bagor"],
    ["दमदमा", "लांघनाज", "महदहा", "बागोर"],
    2,
    "Mahadaha yielded double burials where the dead were placed together with bone necklaces and earrings, and fire pits were associated nearby.",
    "महदहा से दोहरी कब्रें मिली हैं जहाँ मृतकों को हड्डी के हारों और झुमकों के साथ एक साथ रखा गया था और पास में चूल्हे थे।"
)

add_mcq(sec4_en, sec4_hi,
    "The practice of placing food, tools, and ornaments with the dead in a grave is archaeologically interpreted as evidence of:",
    "मृतकों के साथ कब्र में भोजन, उपकरण और आभूषण रखने की प्रथा को पुरातात्विक रूप से किसके साक्ष्य के रूप में व्याख्यायित किया जाता है:",
    ["Lack of food resources", "Belief in an afterlife and social differentiation", "Agricultural grain storage", "Democratic social structure"],
    ["खाद्य संसाधनों की कमी", "परलोक में विश्वास और सामाजिक भेद", "कृषि अनाज भंडारण", "लोकतांत्रिक सामाजिक संरचना"],
    1,
    "Grave goods universally indicate beliefs in post-mortem life and also reveal social stratification when some graves are richer than others.",
    "कब्र के सामान सार्वभौमिक रूप से मृत्यु के बाद के जीवन में विश्वास को इंगित करते हैं और सामाजिक स्तरीकरण को भी प्रकट करते हैं जब कुछ कब्रें अन्य की तुलना में समृद्ध होती हैं।"
)

# --- 2. Multiple Correct MCQ (5 Questions) ---
add_multi_mcq(sec4_en, sec4_hi,
    "Which of the following correctly describe the subsistence economy of Mesolithic communities? (Select all that apply)",
    "निम्नलिखित में से कौन से मध्यपाषाणकालीन समुदायों की जीवन निर्वाह अर्थव्यवस्था का सही वर्णन करते हैं? (सभी सही विकल्प चुनें)",
    ["Hunting small to medium-sized game", "Fishing and collecting mollusks", "Gathering wild plant foods", "Full-scale irrigated grain farming"],
    ["छोटे से मध्यम आकार के शिकार", "मछली पकड़ना और घोंघे इकट्ठा करना", "जंगली पौधों का भोजन इकट्ठा करना", "पूर्ण पैमाने पर सिंचित अनाज की खेती"],
    [0, 1, 2],
    "Mesolithic economy was broad-spectrum foraging including hunting, fishing, and plant gathering. Full-scale irrigated farming belongs to the Neolithic phase.",
    "मध्यपाषाणकालीन अर्थव्यवस्था व्यापक-स्पेक्ट्रम भोजन संग्रह थी जिसमें शिकार, मछली पकड़ना और पौधों का संग्रह शामिल था।"
)

add_multi_mcq(sec4_en, sec4_hi,
    "Which of the following demonstrate early animal domestication in the Indian Mesolithic? (Select all that apply)",
    "निम्नलिखित में से कौन से भारतीय मध्यपाषाण काल में प्रारंभिक पशुपालन को प्रदर्शित करते हैं? (सभी सही विकल्प चुनें)",
    ["Selective culling patterns in animal bone age profiles at Bagor", "Presence of domesticated cattle bones at Adamgarh rock shelters", "Discovery of plough marks in soil", "Small body size of bones compared to wild species"],
    ["बागोर में पशु हड्डी आयु प्रोफाइल में चयनात्मक वध पैटर्न", "आदमगढ़ शैल आश्रयों में पालतू मवेशियों की हड्डियों की उपस्थिति", "मिट्टी में हल के निशानों की खोज", "जंगली प्रजातियों की तुलना में हड्डियों का छोटा आकार"],
    [0, 1, 3],
    "Selective culling, presence of domesticated animal bones, and smaller bone size all indicate domestication. Plough marks belong to the agricultural Neolithic.",
    "चयनात्मक वध, पालतू पशुओं की हड्डियों की उपस्थिति और छोटे हड्डी के आकार सभी पालतूपन को इंगित करते हैं। हल के निशान कृषि नवपाषाण के हैं।"
)

add_multi_mcq(sec4_en, sec4_hi,
    "Which of the following are grave goods associated with Mesolithic burials in the Ganga Valley? (Select all that apply)",
    "निम्नलिखित में से कौन से गंगा घाटी में मध्यपाषाणकालीन कब्रों से जुड़े कब्र के सामान हैं? (सभी सही विकल्प चुनें)",
    ["Bone bead necklaces", "Microliths placed near the skeleton", "Animal joint bones (food offerings)", "Gold and silver jewellery"],
    ["हड्डी के मोतियों के हार", "कंकाल के पास रखे सूक्ष्म पाषाण", "जानवरों के जोड़ों की हड्डियाँ (भोजन चढ़ावा)", "सोने और चाँदी के गहने"],
    [0, 1, 2],
    "Bone beads, microliths, and food offerings are documented grave goods. Gold/silver jewellery belongs to much later historical periods.",
    "हड्डी के मोती, सूक्ष्म पाषाण और भोजन चढ़ावा दस्तावेजीकृत कब्र के सामान हैं। सोने/चाँदी के गहने बहुत बाद के ऐतिहासिक काल के हैं।"
)

add_multi_mcq(sec4_en, sec4_hi,
    "Which features of Mesolithic burials indicate the development of organised social life? (Select all that apply)",
    "मध्यपाषाणकालीन कब्रों की कौन सी विशेषताएं संगठित सामाजिक जीवन के विकास को इंगित करती हैं? (सभी सही विकल्प चुनें)",
    ["Consistent east-west orientation of bodies", "Placement of personal ornaments with the dead", "Evidence of ceremonial food offerings at gravesides", "Complete absence of any communal burial rituals"],
    ["शवों का लगातार पूर्व-पश्चिम अभिविन्यास", "मृतकों के साथ व्यक्तिगत आभूषण रखना", "कब्रों पर धार्मिक भोजन चढ़ावे का साक्ष्य", "किसी भी सामुदायिक शवाधान अनुष्ठान का पूर्ण अभाव"],
    [0, 1, 2],
    "Systematic orientation, ornaments, and food offerings all indicate organised social and ritual life. The absence of rituals would be the opposite evidence.",
    "व्यवस्थित अभिविन्यास, आभूषण और भोजन चढ़ावे सभी संगठित सामाजिक और अनुष्ठान जीवन को इंगित करते हैं।"
)

add_multi_mcq(sec4_en, sec4_hi,
    "Which species were part of the 'broad-spectrum foraging' diet of Indian Mesolithic communities? (Select all that apply)",
    "भारतीय मध्यपाषाणकालीन समुदायों के 'व्यापक-स्पेक्ट्रम भोजन संग्रह' आहार में कौन सी प्रजातियाँ शामिल थीं? (सभी सही विकल्प चुनें)",
    ["Freshwater fish and turtles", "Wild rice and honey", "Spotted deer (chital)", "Domesticated wheat from settled farms"],
    ["मीठे पानी की मछली और कछुए", "जंगली चावल और शहद", "चित्तीदार हिरण (चीतल)", "बसे हुए खेतों से पालतू गेहूँ"],
    [0, 1, 2],
    "Fish, turtles, wild rice, honey, and deer were all part of broad-spectrum foraging. Domesticated wheat belongs to the Neolithic agricultural phase.",
    "मछली, कछुए, जंगली चावल, शहद और हिरण सभी व्यापक-स्पेक्ट्रम भोजन संग्रह का हिस्सा थे।"
)

# --- 3. True/False (8 Questions) ---
add_tf(sec4_en, sec4_hi,
    "Animal domestication in India began exclusively in the Neolithic period.",
    "भारत में पशुपालन की शुरुआत विशेष रूप से नवपाषाण काल में हुई थी।",
    False,
    "The earliest evidence of animal domestication in India dates to the Mesolithic phase (c. 5000 BCE) at Bagor and Adamgarh.",
    "भारत में पशुपालन का सबसे पहला प्रमाण मध्यपाषाण काल (लगभग 5000 ईसा पूर्व) में बागोर और आदमगढ़ में मिलता है।"
)

add_tf(sec4_en, sec4_hi,
    "The dead in Mesolithic communities were often buried within the habitation site itself.",
    "मध्यपाषाणकालीन समुदायों में मृतकों को अक्सर बस्ती स्थल के भीतर ही दफनाया जाता था।",
    True,
    "Intra-settlement burials (burying the dead within the living area) are a documented feature of Ganga valley Mesolithic communities.",
    "बस्ती के भीतर शवाधान (रहने के क्षेत्र के भीतर मृतकों को दफनाना) गंगा घाटी मध्यपाषाणकालीन समुदायों की एक दस्तावेजीकृत विशेषता है।"
)

add_tf(sec4_en, sec4_hi,
    "Bagor Phase I yielded humped cattle, sheep, and goat bones showing selective culling — proving controlled domestication.",
    "बागोर प्रथम चरण से कूबड़ वाले मवेशियों, भेड़ों और बकरियों की हड्डियाँ मिली हैं जो चयनात्मक वध दिखाती हैं — यह नियंत्रित पशुपालन को साबित करती हैं।",
    True,
    "The selective culling of young males for meat while preserving breeding females is a key marker of deliberate pastoralism.",
    "प्रजनन करने वाली मादाओं को संरक्षित करते हुए मांस के लिए युवा नरों का चयनात्मक वध जानबूझकर पशुपालन का एक प्रमुख संकेतक है।"
)

add_tf(sec4_en, sec4_hi,
    "Mesolithic burials at Mahadaha show cremation of bodies in fire pits.",
    "महदहा में मध्यपाषाणकालीन कब्रें चूल्हों में शवों के दाह-संस्कार को दर्शाती हैं।",
    False,
    "Bodies at Mahadaha were directly inhumed (buried in the ground). Fire pits are associated with cooking, not cremation.",
    "महदहा में शवों को सीधे दफनाया (जमीन में) जाता था। चूल्हे खाना पकाने से जुड़े हैं, दाह-संस्कार से नहीं।"
)

add_tf(sec4_en, sec4_hi,
    "Wild honey gathering was a part of the broad-spectrum foraging strategy in Mesolithic India.",
    "मध्यपाषाणकालीन भारत में जंगली शहद इकट्ठा करना व्यापक-स्पेक्ट्रम भोजन संग्रह रणनीति का एक हिस्सा था।",
    True,
    "Wild honey is depicted in Mesolithic rock art and was certainly a high-energy food supplement.",
    "जंगली शहद को मध्यपाषाणकालीन शैल कला में दर्शाया गया है और यह निश्चित रूप से एक उच्च-ऊर्जा खाद्य पूरक था।"
)

add_tf(sec4_en, sec4_hi,
    "The grave orientation (direction of body placement) was completely random and shows no cultural pattern at Ganga valley sites.",
    "गंगा घाटी के स्थलों पर कब्र का अभिविन्यास (शव रखने की दिशा) पूरी तरह से यादृच्छिक था और कोई सांस्कृतिक पैटर्न नहीं दिखाता था।",
    False,
    "A consistent east-west or west-east orientation at Ganga valley sites suggests shared spiritual beliefs regarding death and rebirth cycles.",
    "गंगा घाटी के स्थलों पर लगातार पूर्व-पश्चिम या पश्चिम-पूर्व अभिविन्यास मृत्यु और पुनर्जन्म चक्रों के बारे में साझा आध्यात्मिक विश्वासों का सुझाव देता है।"
)

add_tf(sec4_en, sec4_hi,
    "The introduction of pastoralism during the Mesolithic eventually facilitated the transition to sedentary farming in the Neolithic.",
    "मध्यपाषाण काल के दौरान पशुपालन की शुरुआत ने अंततः नवपाषाण काल में स्थायी खेती में संक्रमण को सुगम बनाया।",
    True,
    "Pastoralism is a critical intermediate step: controlling animal movements and managing herds eventually led to settling near seasonal pastures and cultivating food crops.",
    "पशुपालन एक महत्वपूर्ण मध्यवर्ती कदम है: पशुओं की गतिविधियों को नियंत्रित करना और झुंडों का प्रबंधन करना अंततः मौसमी चरागाहों के पास बसने और खाद्य फसलों की खेती करने की ओर ले जाता है।"
)

add_tf(sec4_en, sec4_hi,
    "Wild rice was first domesticated and cultivated during the Mesolithic period in the Ganga Valley.",
    "गंगा घाटी में मध्यपाषाण काल के दौरान जंगली चावल को पहली बार पालतू बनाया और उगाया गया था।",
    False,
    "Mesolithic groups only gathered wild rice. Intentional cultivation of rice began later during the early Neolithic (e.g., Lahuradewa, c. 7000 BCE).",
    "मध्यपाषाणकालीन समूह केवल जंगली चावल इकट्ठा करते थे। चावल की जानबूझकर खेती बाद में प्रारंभिक नवपाषाण काल में शुरू हुई (जैसे लहुरादेवा, लगभग 7000 ईसा पूर्व)।"
)

# --- 4. Fill in the Blank (8 Questions) ---
add_blank(sec4_en, sec4_hi,
    "The earliest evidence of animal domestication in India comes from Bagor and ________.",
    "भारत में पशुपालन का सबसे पहला प्रमाण बागोर और ________ से आता है।",
    "Adamgarh", "आदमगढ़",
    "Both Bagor and Adamgarh independently show domesticated cattle, sheep, and goats by c. 5000 BCE.",
    "बागोर और आदमगढ़ दोनों स्वतंत्र रूप से लगभग 5000 ईसा पूर्व तक पालतू मवेशियों, भेड़ों और बकरियों को दिखाते हैं।"
)

add_blank(sec4_en, sec4_hi,
    "The diversified food-collecting strategy of Mesolithic groups is called the ________ economy.",
    "मध्यपाषाणकालीन समूहों की विविधीकृत भोजन-संग्रह रणनीति को ________ अर्थव्यवस्था कहा जाता है।",
    "broad-spectrum", "व्यापक-स्पेक्ट्रम",
    "The broad-spectrum economy reflects diversification away from sole reliance on large game.",
    "व्यापक-स्पेक्ट्रम अर्थव्यवस्था केवल बड़े शिकार पर निर्भरता से विविधता को दर्शाती है।"
)

add_blank(sec4_en, sec4_hi,
    "Double burials with bone necklaces as grave goods were found at the Ganga valley site of ________.",
    "कब्र के सामान के रूप में हड्डी के हार के साथ दोहरी कब्रें गंगा घाटी के ________ स्थल पर मिली थीं।",
    "Mahadaha", "महदहा",
    "Mahadaha is famous for double burials accompanied by bone ornaments and fire pits.",
    "महदहा हड्डी के आभूषणों और चूल्हों के साथ दोहरी कब्रों के लिए प्रसिद्ध है।"
)

add_blank(sec4_en, sec4_hi,
    "Burial offerings (food, tools, ornaments) placed with the dead indicate a belief in a/an ________.",
    "मृतकों के साथ रखे गए शवाधान चढ़ावे (भोजन, उपकरण, आभूषण) एक ________ में विश्वास को इंगित करते हैं।",
    "afterlife", "परलोक",
    "The universal anthropological interpretation is that grave goods reflect beliefs in post-death existence.",
    "सार्वभौमिक मानवशास्त्रीय व्याख्या यह है कि कब्र के सामान मृत्यु के बाद के अस्तित्व में विश्वास को दर्शाते हैं।"
)

add_blank(sec4_en, sec4_hi,
    "Deliberate killing of young male animals for meat while preserving breeding females is called the ________ culling pattern.",
    "प्रजनन करने वाली मादाओं को संरक्षित करते हुए मांस के लिए युवा नर जानवरों की जानबूझकर हत्या को ________ वध पैटर्न कहा जाता है।",
    "selective", "चयनात्मक",
    "Selective culling is the zooarchaeological signature of deliberate animal husbandry.",
    "चयनात्मक वध जानबूझकर पशुपालन का पशु-पुरातात्विक हस्ताक्षर है।"
)

add_blank(sec4_en, sec4_hi,
    "The practice of gathering wild plant roots, tubers, and seeds is called plant ________.",
    "जंगली पौधों की जड़ें, कंद और बीज इकट्ठा करने की प्रथा को पौधों का ________ कहा जाता है।",
    "foraging", "संग्रहण",
    "Plant foraging was a key supplement to hunting and fishing in the Mesolithic economy.",
    "पौधों का संग्रहण मध्यपाषाणकालीन अर्थव्यवस्था में शिकार और मछली पकड़ने का एक प्रमुख पूरक था।"
)

add_blank(sec4_en, sec4_hi,
    "The zebu (humped cattle) belongs to the species ________, and was among the first domesticated animals at Bagor.",
    "ज़ेबू (कूबड़ वाले मवेशी) प्रजाति ________ से संबंधित है, और बागोर में पहले पालतू बनाए गए जानवरों में से एक था।",
    "Bos indicus", "बॉस इंडिकस",
    "Bos indicus (zebu/humped cattle) is the South Asian domesticated cattle species, evidence of which appears at Bagor.",
    "बॉस इंडिकस (ज़ेबू/कूबड़ वाले मवेशी) दक्षिण एशियाई पालतू मवेशी प्रजाति है, जिसके साक्ष्य बागोर में मिलते हैं।"
)

add_blank(sec4_en, sec4_hi,
    "Burials situated within the boundaries of a habitation area are called ________ burials.",
    "एक बस्ती क्षेत्र की सीमाओं के भीतर स्थित शवाधान को ________ शवाधान कहा जाता है।",
    "intra-settlement", "बस्ती-अंतर्गत",
    "Intra-settlement burials are a defining feature of Mesolithic social life in the Ganga plains.",
    "बस्ती-अंतर्गत शवाधान गंगा के मैदानों में मध्यपाषाणकालीन सामाजिक जीवन की एक परिभाषित विशेषता है।"
)

# --- 5. Match the Following (3 Questions) ---
add_match(sec4_en, sec4_hi,
    "Match the Mesolithic economic activity with its archaeological evidence:",
    "मध्यपाषाणकालीन आर्थिक गतिविधि को उसके पुरातात्विक साक्ष्य से सुमेलित करें:",
    ["1. Animal domestication", "2. Aquatic foraging", "3. Plant gathering"],
    ["1. पशुपालन", "2. जलीय भोजन संग्रह", "3. पौधों का संग्रह"],
    ["A. Selective bone culling profiles at Bagor", "B. Freshwater snail shell mounds at Ganga valley sites", "C. Carbonized wild seeds in hearth ash"],
    ["A. बागोर में चयनात्मक हड्डी वध प्रोफाइल", "B. गंगा घाटी स्थलों पर मीठे पानी के घोंघों के छिलकों के ढेर", "C. चूल्हे की राख में जले हुए जंगली बीज"],
    "1-A, 2-B, 3-C.",
    "1-A, 2-B, 3-C."
)

add_match(sec4_en, sec4_hi,
    "Match the grave good type with its archaeological significance:",
    "कब्र के सामान के प्रकार को उसके पुरातात्विक महत्व से सुमेलित करें:",
    ["1. Bone necklaces in grave", "2. Microliths placed near skeleton", "3. Animal joint bones in grave"],
    ["1. कब्र में हड्डी के हार", "2. कंकाल के पास रखे सूक्ष्म पाषाण", "3. कब्र में जानवरों के जोड़ों की हड्डियाँ"],
    ["A. Indicates personal adornment and social identity", "B. Tool kits provided for use in afterlife", "C. Food offering for nourishment in afterlife"],
    ["A. व्यक्तिगत श्रृंगार और सामाजिक पहचान को इंगित करता है", "B. परलोक में उपयोग के लिए प्रदान किए गए उपकरण", "C. परलोक में पोषण के लिए भोजन चढ़ावा"],
    "1-A, 2-B, 3-C. Each grave good type reveals a different aspect of Mesolithic spiritual belief.",
    "1-A, 2-B, 3-C. प्रत्येक कब्र के सामान का प्रकार मध्यपाषाणकालीन आध्यात्मिक विश्वास के एक अलग पहलू को प्रकट करता है।"
)

add_match(sec4_en, sec4_hi,
    "Match the domesticated animal with their earliest Indian Mesolithic site of identification:",
    "पालतू जानवर को उनके सबसे पहले भारतीय मध्यपाषाणकालीन पहचान स्थल से सुमेलित करें:",
    ["1. Humped cattle (zebu)", "2. Sheep and goat", "3. Wild pig"],
    ["1. कूबड़ वाले मवेशी (ज़ेबू)", "2. भेड़ और बकरी", "3. जंगली सूअर"],
    ["A. Bagor (Rajasthan)", "B. Bagor and Adamgarh (Rajasthan/MP)", "C. Adamgarh (MP)"],
    ["A. बागोर (राजस्थान)", "B. बागोर और आदमगढ़ (राजस्थान/मध्य प्रदेश)", "C. आदमगढ़ (मध्य प्रदेश)"],
    "1-A, 2-B, 3-C. Zebu evidence comes most clearly from Bagor; sheep/goats appear at both sites; wild pigs at Adamgarh.",
    "1-A, 2-B, 3-C. ज़ेबू साक्ष्य सबसे स्पष्ट रूप से बागोर से है; भेड़/बकरियाँ दोनों स्थलों पर हैं; जंगली सूअर आदमगढ़ में।"
)

# --- 6. One-Liner (8 Questions) ---
add_oneliner(sec4_en, sec4_hi,
    "Which two Indian Mesolithic sites provide the earliest evidence of animal domestication?",
    "कौन से दो भारतीय मध्यपाषाणकालीन स्थल पशुपालन का सबसे पहला साक्ष्य प्रदान करते हैं?",
    "Bagor (Rajasthan) and Adamgarh (Madhya Pradesh).",
    "बागोर (राजस्थान) और आदमगढ़ (मध्य प्रदेश)।"
)

add_oneliner(sec4_en, sec4_hi,
    "What is the zooarchaeological indicator of pastoralism (animal domestication) in bone assemblages?",
    "हड्डी के समूह में पशुपालन (पशुपालन) का पशु-पुरातात्विक संकेतक क्या है?",
    "Selective culling patterns — young males slaughtered for meat while females preserved for breeding.",
    "चयनात्मक वध पैटर्न — मांस के लिए युवा नरों को मारा जाता है जबकि प्रजनन के लिए मादाओं को संरक्षित किया जाता है।"
)

add_oneliner(sec4_en, sec4_hi,
    "What does the term 'broad-spectrum economy' mean in Mesolithic archaeology?",
    "मध्यपाषाण पुरातत्व में 'व्यापक-स्पेक्ट्रम अर्थव्यवस्था' का क्या अर्थ है?",
    "A diversified food strategy using multiple sources: hunting, fishing, plant gathering, and gathering mollusks.",
    "शिकार, मछली पकड़ने, पौधों के संग्रह और घोंघे इकट्ठा करने जैसे कई स्रोतों का उपयोग करने वाली विविधीकृत खाद्य रणनीति।"
)

add_oneliner(sec4_en, sec4_hi,
    "What do grave goods in Mesolithic burials indicate?",
    "मध्यपाषाणकालीन कब्रों में कब्र के सामान क्या इंगित करते हैं?",
    "Belief in an afterlife and emergence of social differentiation/status.",
    "परलोक में विश्वास और सामाजिक भेद/स्थिति का उदय।"
)

add_oneliner(sec4_en, sec4_hi,
    "Which animals were domesticated earliest at Bagor?",
    "बागोर में सबसे पहले कौन से जानवर पालतू बनाए गए थे?",
    "Humped cattle (zebu), sheep, and goats.",
    "कूबड़ वाले मवेशी (ज़ेबू), भेड़ और बकरियाँ।"
)

add_oneliner(sec4_en, sec4_hi,
    "Were Mesolithic communities fully settled farmers or nomadic?",
    "क्या मध्यपाषाणकालीन समुदाय पूरी तरह से बसे हुए किसान थे या खानाबदोश?",
    "Semi-nomadic hunter-gatherers with early pastoralism — not fully settled farmers.",
    "प्रारंभिक पशुपालन के साथ अर्ध-घुमंतू शिकारी-संग्रहकर्ता — पूरी तरह से बसे हुए किसान नहीं।"
)

add_oneliner(sec4_en, sec4_hi,
    "What is the significance of intra-settlement burials?",
    "बस्ती-अंतर्गत शवाधान का क्या महत्व है?",
    "It shows strong social cohesion — the dead were kept within the community's living space.",
    "यह मजबूत सामाजिक एकजुटता दर्शाता है — मृतकों को समुदाय के रहने की जगह के भीतर रखा जाता था।"
)

add_oneliner(sec4_en, sec4_hi,
    "Which domesticated animal provides the earliest evidence of controlled herding in the Deccan/Central India?",
    "कौन सा पालतू जानवर दक्कन/मध्य भारत में नियंत्रित पशुपालन का सबसे पहला साक्ष्य प्रदान करता है?",
    "Humped cattle (Bos indicus/zebu) at Adamgarh rock shelters.",
    "आदमगढ़ शैल आश्रयों में कूबड़ वाले मवेशी (बॉस इंडिकस/ज़ेबू)।"
)

# --- 7. Assertion-Reason (8 Questions) ---
add_ar(sec4_en, sec4_hi,
    "Assertion (A): Animal domestication in India predates the Neolithic period at certain sites.\nReason (R): Evidence from Bagor and Adamgarh shows controlled herding of cattle, sheep, and goats by c. 5000 BCE.",
    "कथन (A): भारत में कुछ स्थलों पर पशुपालन नवपाषाण काल से पहले हुआ।\nकारण (R): बागोर और आदमगढ़ के साक्ष्य दिखाते हैं कि लगभग 5000 ईसा पूर्व तक मवेशियों, भेड़ों और बकरियों का नियंत्रित पालन-पोषण किया जा रहा था।",
    0,
    "Both are true, and R proves the Mesolithic origin of pastoralism in India.",
    "दोनों सही हैं, और R भारत में पशुपालन की मध्यपाषाणकालीन उत्पत्ति को साबित करता है।"
)

add_ar(sec4_en, sec4_hi,
    "Assertion (A): Grave goods at Mahadaha indicate individual social identities.\nReason (R): Placement of personal bone ornaments with specific individuals shows some burials were richer than others.",
    "कथन (A): महदहा में कब्र के सामान व्यक्तिगत सामाजिक पहचान को इंगित करते हैं।\nकारण (R): विशिष्ट व्यक्तियों के साथ व्यक्तिगत हड्डी के आभूषण रखना दर्शाता है कि कुछ कब्रें दूसरों की तुलना में अधिक समृद्ध थीं।",
    0,
    "Both are true. Differential burial wealth is a global indicator of emerging social hierarchies.",
    "दोनों सही हैं। अलग-अलग शवाधान संपदा उभरती सामाजिक श्रेणियों का एक वैश्विक संकेतक है।"
)

add_ar(sec4_en, sec4_hi,
    "Assertion (A): The Mesolithic broad-spectrum economy showed greater food security than the Paleolithic focus on large game.\nReason (R): Diversification reduces the risk of starvation if one food source fails.",
    "कथन (A): मध्यपाषाणकालीन व्यापक-स्पेक्ट्रम अर्थव्यवस्था ने बड़े शिकार पर पुरापाषाणकालीन ध्यान केंद्रित करने की तुलना में अधिक खाद्य सुरक्षा दिखाई।\nकारण (R): विविधीकरण भुखमरी के जोखिम को कम करता है यदि एक खाद्य स्रोत विफल हो जाए।",
    0,
    "Both A and R are true, and R explains the survival advantage of the broad-spectrum strategy.",
    "A और R दोनों सही हैं, और R व्यापक-स्पेक्ट्रम रणनीति के जीवित रहने के लाभ को समझाता है।"
)

add_ar(sec4_en, sec4_hi,
    "Assertion (A): The Mesolithic period marks the complete transition to sedentary farming in the Ganga valley.\nReason (R): Large granaries and permanent houses were built at Ganga plain Mesolithic sites.",
    "कथन (A): मध्यपाषाण काल गंगा घाटी में स्थायी खेती में पूर्ण संक्रमण को चिह्नित करता है।\nकारण (R): गंगा के मैदान के मध्यपाषाणकालीन स्थलों पर बड़े अनाज भंडार और स्थायी घर बनाए गए थे।",
    3,
    "A is false — the Mesolithic was NOT a farming phase. R is false — no granaries or permanent buildings exist at these sites.",
    "A गलत है — मध्यपाषाण काल कृषि चरण नहीं था। R गलत है — इन स्थलों पर कोई अनाज भंडार या स्थायी इमारतें नहीं हैं।"
)

add_ar(sec4_en, sec4_hi,
    "Assertion (A): Wild rice gathering was part of Mesolithic broad-spectrum foraging in the Ganga plains.\nReason (R): The intentional cultivation of rice was first practiced during the Mesolithic to ensure a stable grain supply.",
    "कथन (A): जंगली चावल इकट्ठा करना गंगा के मैदानों में मध्यपाषाणकालीन व्यापक-स्पेक्ट्रम भोजन संग्रह का हिस्सा था।\nकारण (R): स्थिर अनाज आपूर्ति सुनिश्चित करने के लिए पहली बार मध्यपाषाण काल के दौरान चावल की जानबूझकर खेती की गई थी।",
    2,
    "A is true — wild rice was gathered. R is false — intentional rice cultivation began in the Neolithic period (e.g., Lahuradewa c. 7000 BCE).",
    "A सही है — जंगली चावल इकट्ठा किया जाता था। R गलत है — जानबूझकर चावल की खेती नवपाषाण काल में शुरू हुई (जैसे लहुरादेवा लगभग 7000 ईसा पूर्व)।"
)

add_ar(sec4_en, sec4_hi,
    "Assertion (A): The development of pastoralism during the Mesolithic was a precursor to sedentary agriculture.\nReason (R): Managing herds required semi-permanent settlement, familiarity with seasonal pasture cycles, and knowledge of animal biology.",
    "कथन (A): मध्यपाषाण काल के दौरान पशुपालन का विकास स्थायी कृषि का अग्रगामी (precursor) था।\nकारण (R): झुंडों के प्रबंधन के लिए अर्ध-स्थायी बस्ती, मौसमी चरागाह चक्रों से परिचित होना और पशु जीव विज्ञान का ज्ञान आवश्यक था।",
    0,
    "Both A and R are true. Pastoralism laid the cognitive and social groundwork for the later Neolithic agricultural revolution.",
    "A और R दोनों सही हैं। पशुपालन ने बाद की नवपाषाण कृषि क्रांति के लिए संज्ञानात्मक और सामाजिक आधार तैयार किया।"
)

add_ar(sec4_en, sec4_hi,
    "Assertion (A): Organic remains like bone ornaments at Mahadaha survived because the site has highly acidic floodplain soil.\nReason (R): Acidic soils rapidly dissolve calcium phosphate in bones, destroying organic remains.",
    "कथन (A): महदहा में हड्डी के आभूषण जैसे जैविक अवशेष बचे रहे क्योंकि स्थल में अत्यधिक अम्लीय बाढ़ के मैदान की मिट्टी है।\nकारण (R): अम्लीय मिट्टी हड्डियों में कैल्शियम फॉस्फेट को तेजी से घोल देती है, जिससे जैविक अवशेष नष्ट हो जाते हैं।",
    3,
    "A is false — bones survived because the Ganga plains have relatively alkaline, calcium-carbonate-rich sediments. R is true (acidic soil does destroy bones), but it is not the reason for Mahadaha's preservation.",
    "A गलत है — हड्डियाँ बचीं क्योंकि गंगा के मैदानों में अपेक्षाकृत क्षारीय, कैल्शियम-कार्बोनेट युक्त तलछट है। R सही है (अम्लीय मिट्टी हड्डियों को नष्ट करती है), लेकिन यह महदहा के संरक्षण का कारण नहीं है।"
)

add_ar(sec4_en, sec4_hi,
    "Assertion (A): Triple burials at Damdama suggest that families or close kin were buried together.\nReason (R): Shared burial of multiple individuals simultaneously implies simultaneous death events, probably during conflict or epidemic.",
    "कथन (A): दमदमा में तिहरी कब्रें सुझाव देती हैं कि परिवारों या करीबी रिश्तेदारों को एक साथ दफनाया गया था।\nकारण (R): कई व्यक्तियों का एक साथ साझा शवाधान एक साथ मृत्यु की घटनाओं का संकेत देता है, शायद संघर्ष या महामारी के दौरान।",
    1,
    "Both A and R are true, but R is not the only explanation — triple burials can also represent family units buried at different times in the same grave, not necessarily simultaneous deaths.",
    "A और R दोनों सही हैं, लेकिन R एकमात्र व्याख्या नहीं है — तिहरी कब्रें उसी कब्र में अलग-अलग समय पर दफनाए गए परिवार के सदस्यों का प्रतिनिधित्व भी कर सकती हैं।"
)

# --- 8. Statement-Based (5 Questions) ---
add_stmt(sec4_en, sec4_hi,
    "Consider the following statements regarding the origin of animal domestication in India:\n1. The earliest evidence comes from Bagor (Rajasthan) and Adamgarh (MP), dating to c. 5000 BCE.\n2. These sites predate the Neolithic phase, proving that pastoralism began in the Mesolithic.\nWhich of the statements given above is/are correct?",
    "भारत में पशुपालन की उत्पत्ति के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. सबसे पहला साक्ष्य बागोर (राजस्थान) और आदमगढ़ (मध्य प्रदेश) से आता है, जो लगभग 5000 ईसा पूर्व के हैं।\n2. ये स्थल नवपाषाण चरण से पहले हैं, जो साबित करता है कि पशुपालन मध्यपाषाण काल में शुरू हुआ था।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
    2,
    "Both statements are correct. India's earliest animal domestication is Mesolithic, predating the Neolithic agricultural revolution.",
    "दोनों कथन सही हैं। भारत का सबसे पहला पशुपालन मध्यपाषाणकालीन है, जो नवपाषाण कृषि क्रांति से पहले है।"
)

add_stmt(sec4_en, sec4_hi,
    "Consider the following statements regarding grave goods at Mesolithic burials:\n1. Grave goods like bone ornaments indicate a belief in life after death.\n2. All Mesolithic graves contained identical grave goods, showing an egalitarian society.\nWhich of the statements given above is/are correct?",
    "मध्यपाषाणकालीन शवाधान में कब्र के सामान के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. हड्डी के आभूषण जैसे कब्र के सामान मृत्यु के बाद के जीवन में विश्वास को इंगित करते हैं।\n2. सभी मध्यपाषाणकालीन कब्रों में समान कब्र के सामान थे, जो एक समतावादी समाज दर्शाता है।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
    0,
    "Statement 1 is correct. Statement 2 is incorrect — graves varied in richness, suggesting social differentiation, not egalitarianism.",
    "कथन 1 सही है। कथन 2 गलत है — कब्रें समृद्धि में भिन्न थीं, जो समतावादिता नहीं बल्कि सामाजिक भेद का सुझाव देती हैं।"
)

add_stmt(sec4_en, sec4_hi,
    "With reference to the Mesolithic subsistence economy, consider the following statements:\n1. Aquatic resources like fish and mollusks supplemented the main diet of large mammal hunting.\n2. Wild plant foods were an integral part of the broad-spectrum diet.\nWhich of the statements given above is/are correct?",
    "मध्यपाषाणकालीन जीवन निर्वाह अर्थव्यवस्था के संदर्भ में, निम्नलिखित कथनों पर विचार करें:\n1. मछली और घोंघे जैसे जलीय संसाधनों ने बड़े स्तनधारियों के शिकार के मुख्य आहार की पूर्ति की।\n2. जंगली पौधों का भोजन व्यापक-स्पेक्ट्रम आहार का एक अभिन्न हिस्सा था।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
    2,
    "Both statements are correct, describing the balanced and diversified nature of the Mesolithic broad-spectrum economy.",
    "दोनों कथन सही हैं, जो मध्यपाषाणकालीन व्यापक-स्पेक्ट्रम अर्थव्यवस्था की संतुलित और विविध प्रकृति का वर्णन करते हैं।"
)

add_stmt(sec4_en, sec4_hi,
    "Consider the following pairs:\nSite : Key burial/domestication feature\n1. Bagor : Earliest evidence of animal domestication\n2. Mahadaha : 41 human burials including triple burials\n3. Sarai Nahar Rai : Skeleton with embedded arrowhead\nHow many pairs are correctly matched?",
    "निम्नलिखित युग्मों पर विचार करें:\nस्थल : मुख्य शवाधान/पशुपालन विशेषता\n1. बागोर : पशुपालन का सबसे पहला साक्ष्य\n2. महदहा : तिहरी कब्रों सहित 41 मानव कब्रें\n3. सराय नाहर राय : धँसी तीर नोक वाला कंकाल\nकितने युग्म सही सुमेलित हैं?",
    ["Only one", "Only two", "All three", "None"],
    ["केवल एक", "केवल दो", "सभी तीन", "कोई नहीं"],
    1,
    "Pair 1 is correct (Bagor: animal domestication) and Pair 3 is correct (Sarai Nahar Rai: conflict skeleton). Pair 2 is incorrect — 41 burials including triple burials belong to Damdama, not Mahadaha.",
    "युग्म 1 सही है (बागोर: पशुपालन) और युग्म 3 सही है (सराय नाहर राय: संघर्ष कंकाल)। युग्म 2 गलत है — तिहरी कब्रों सहित 41 कब्रें दमदमा की हैं, महदहा की नहीं।"
)

add_stmt(sec4_en, sec4_hi,
    "Consider the following statements regarding the Mesolithic transition to food production:\n1. Mesolithic pastoralism at Bagor is considered a precursor to the Neolithic agricultural economy.\n2. Mesolithic communities in the Ganga plains cultivated irrigated rice fields alongside hunting.\nWhich of the statements given above is/are correct?",
    "खाद्य उत्पादन में मध्यपाषाणकालीन संक्रमण के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. बागोर में मध्यपाषाणकालीन पशुपालन को नवपाषाणकालीन कृषि अर्थव्यवस्था का पूर्ववर्ती माना जाता है।\n2. गंगा के मैदानों में मध्यपाषाणकालीन समुदायों ने शिकार के साथ-साथ सिंचित चावल के खेतों की खेती की।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
    0,
    "Statement 1 is correct. Statement 2 is incorrect — irrigated rice farming was not practiced in the Mesolithic; only wild rice was gathered.",
    "कथन 1 सही है। कथन 2 गलत है — मध्यपाषाण काल में सिंचित चावल की खेती नहीं की जाती थी; केवल जंगली चावल इकट्ठा किया जाता था।"
)

# --- 9. Why (3 Questions) ---
add_open(sec4_en, sec4_hi, "Why",
    "Why is the transition from hunting to pastoralism considered a critical step in human prehistory?",
    "शिकार से पशुपालन में संक्रमण को मानव प्रागैतिहास में एक महत्वपूर्ण कदम क्यों माना जाता है?",
    "Domesticating animals provided a reliable, on-demand protein source that could be bred, managed, and moved. Unlike wild game (unpredictable), herds could be managed to ensure meat supply even in lean seasons. This food security allowed bands to become semi-permanent, which eventually triggered the social and cognitive preconditions for full-scale agriculture.",
    "पशुओं को पालतू बनाने ने एक विश्वसनीय, मांग पर उपलब्ध प्रोटीन स्रोत प्रदान किया जिसे पाला, प्रबंधित और स्थानांतरित किया जा सकता था। जंगली शिकार (अनिश्चित) के विपरीत, झुंडों को दुबले मौसम में भी मांस आपूर्ति सुनिश्चित करने के लिए प्रबंधित किया जा सकता था। इस खाद्य सुरक्षा ने समूहों को अर्ध-स्थायी बनने की अनुमति दी, जिसने अंततः पूर्ण पैमाने पर कृषि के लिए सामाजिक और संज्ञानात्मक पूर्व शर्तों को प्रेरित किया।"
)

add_open(sec4_en, sec4_hi, "Why",
    "Why do Mesolithic burial sites like Damdama show multiple bodies in the same pit?",
    "दमदमा जैसे मध्यपाषाणकालीन शवाधान स्थलों पर एक ही गड्ढे में कई शव क्यों दिखाई देते हैं?",
    "Multiple burials in a single pit suggest that families or close social groups were intentionally buried together. This could reflect a worldview where kin relationships extended beyond death. Alternatively, mass deaths from conflict (the Sarai Nahar Rai arrowhead) or epidemic episodes may have triggered simultaneous burials.",
    "एक ही गड्ढे में कई शवाधान सुझाव देते हैं कि परिवारों या करीबी सामाजिक समूहों को जानबूझकर एक साथ दफनाया गया था। यह एक ऐसी विश्व दृष्टि को प्रतिबिंबित कर सकता है जहाँ रिश्तेदारी मृत्यु के बाद भी जारी रहती थी। वैकल्पिक रूप से, संघर्ष या महामारी से सामूहिक मौतें एक साथ शवाधान को प्रेरित कर सकती थीं।"
)

add_open(sec4_en, sec4_hi, "Why",
    "Why was wild rice gathered but not cultivated during the Mesolithic phase?",
    "मध्यपाषाण चरण के दौरान जंगली चावल को क्यों इकट्ठा किया जाता था लेकिन उसकी खेती नहीं की जाती थी?",
    "Cultivation requires investment in land clearing, sowing, weeding, and harvesting — tasks incompatible with a mobile hunter-gatherer lifestyle. Mesolithic groups moved seasonally and could not commit to a fixed agricultural plot. They gathered wild rice opportunistically during their circuit of seasonal camps, but the cognitive and social shift to deliberate cultivation occurred only in the early Neolithic.",
    "खेती के लिए भूमि को साफ करने, बोने, निराई और कटाई में निवेश की आवश्यकता होती है — जो कार्य एक गतिशील शिकारी-संग्रहकर्ता जीवन शैली के साथ असंगत हैं। मध्यपाषाणकालीन समूह मौसमी रूप से आगे-पीछे होते रहते थे और एक निश्चित कृषि भूखंड के लिए प्रतिबद्ध नहीं हो सकते थे। उन्होंने मौसमी शिविरों में जंगली चावल इकट्ठा किया, लेकिन जानबूझकर खेती में बदलाव केवल प्रारंभिक नवपाषाण काल में हुआ।"
)

# --- 10. How (3 Questions) ---
add_open(sec4_en, sec4_hi, "How",
    "How do zooarchaeologists distinguish between wild-hunted and domesticated animal bones at a prehistoric site?",
    "पशु-पुरातत्वविद एक प्रागैतिहासिक स्थल पर जंगली-शिकार और पालतू जानवरों की हड्डियों के बीच अंतर कैसे करते हैं?",
    "Three main indicators: (1) Body size — domesticated animals show smaller body size over generations due to selective breeding; (2) Age profiles — domestic herds show selective culling of young males while females are preserved; (3) Species composition — finding high ratios of cattle, sheep, and goats (herding species) over wild deer/boar ratios signals controlled herding.",
    "तीन मुख्य संकेतक: (1) शरीर का आकार — पालतू जानवर चयनात्मक प्रजनन के कारण पीढ़ियों में छोटे शरीर का आकार दिखाते हैं; (2) आयु प्रोफाइल — घरेलू झुंड मादाओं को संरक्षित करते हुए युवा नरों का चयनात्मक वध दिखाते हैं; (3) प्रजाति संरचना — जंगली हिरण/सूअर के अनुपात पर मवेशियों, भेड़ों और बकरियों का उच्च अनुपात नियंत्रित पशुपालन का संकेत देता है।"
)

add_open(sec4_en, sec4_hi, "How",
    "How did the Mesolithic broad-spectrum economy reduce seasonal starvation risk?",
    "मध्यपाषाणकालीन व्यापक-स्पेक्ट्रम अर्थव्यवस्था ने मौसमी भुखमरी के जोखिम को कैसे कम किया?",
    "By diversifying food sources across multiple ecological niches, Mesolithic groups ensured that if one resource failed (e.g., deer migrated away), other resources (fish, mollusks, berries, tubers) were available. Seasonal fishing, root gathering, honey collection, and bird trapping created a year-round nutritional buffer against food shortfalls.",
    "कई पारिस्थितिक क्षेत्रों में खाद्य स्रोतों को विविधीकरण करके, मध्यपाषाणकालीन समूहों ने यह सुनिश्चित किया कि यदि एक संसाधन विफल हो जाए (जैसे हिरण चले जाएं), तो अन्य संसाधन (मछली, घोंघे, जामुन, कंद) उपलब्ध रहें। मौसमी मछली पकड़ना, जड़ें इकट्ठा करना, शहद संग्रह और पक्षियों को पकड़ना भोजन की कमी के खिलाफ साल भर का पोषण बफर बनाते थे।"
)

add_open(sec4_en, sec4_hi, "How",
    "How does intra-settlement burial practice reflect the social bonds of Mesolithic communities?",
    "बस्ती-अंतर्गत शवाधान प्रथा मध्यपाषाणकालीन समुदायों के सामाजिक बंधनों को कैसे दर्शाती है?",
    "Burying the dead within the habitation area — rather than outside it — shows that the community did not wish to separate from their deceased members. It suggests strong social attachment (kin loyalty) and possibly belief that the dead continued to protect the living. It also suggests recurring seasonal use of the same camp, where multiple generations were buried in the same spot over centuries.",
    "रहने के क्षेत्र के भीतर मृतकों को दफनाना — बाहर की बजाय — दर्शाता है कि समुदाय अपने मृत सदस्यों से अलग नहीं होना चाहता था। यह मजबूत सामाजिक लगाव (रिश्तेदारी की वफादारी) का सुझाव देता है और शायद यह विश्वास कि मृत जीवितों की रक्षा करते रहते हैं।"
)

# --- 11. Case Study (3 Questions) ---
add_open(sec4_en, sec4_hi, "Case Study",
    "Case Study: Animal Bone Analysis at Bagor Phase I.\nExplain how zooarchaeological evidence reconstructed the shift from hunting to pastoralism.",
    "मामला अध्ययन: बागोर प्रथम चरण में पशु हड्डी विश्लेषण।\nस्पष्ट करें कि पशु-पुरातात्विक साक्ष्य ने शिकार से पशुपालन में बदलाव को कैसे पुनर्निर्मित किया।",
    "Phase I bones show three key signals: (1) Cattle, sheep, and goat bones dominated over deer and wild boar — indicating active herding rather than opportunistic hunting. (2) The age profiles showed a high proportion of adult females and very young calves, with few prime-age males — indicating selective slaughter for milk and meat. (3) Bone measurements were slightly smaller than wild counterparts, indicating the morphological changes from selective breeding pressure.",
    "प्रथम चरण की हड्डियाँ तीन प्रमुख संकेत दिखाती हैं: (1) हिरण और जंगली सूअर पर मवेशियों, भेड़ों और बकरियों की हड्डियों का वर्चस्व था — जो सक्रिय पशुपालन को इंगित करता है। (2) आयु प्रोफाइल में वयस्क मादाओं और बहुत छोटे बछड़ों का उच्च अनुपात था — जो दूध और मांस के लिए चयनात्मक वध को इंगित करता है। (3) हड्डी के माप जंगली समकक्षों से थोड़े छोटे थे।"
)

add_open(sec4_en, sec4_hi, "Case Study",
    "Case Study: Mahadaha Double Burials.\nDescribe what the double burials with bone ornaments reveal about Mesolithic social organization.",
    "मामला अध्ययन: महदहा की दोहरी कब्रें।\nवर्णन करें कि हड्डी के आभूषणों के साथ दोहरी कब्रें मध्यपाषाणकालीन सामाजिक संगठन के बारे में क्या प्रकट करती हैं।",
    "Double burials with bone necklaces and earrings placed in the same pit suggests the couple or kin pair shared social identity. The bone ornaments are personal items — they belonged specifically to the dead individual, not to the community pool. Difference in ornament richness between graves suggests some community members had higher social status. The proximity of fire pits suggests funerary feasting, showing community cohesion during mourning.",
    "हड्डी के हारों और झुमकों के साथ एक ही गड्ढे में दोहरी कब्रें सुझाव देती हैं कि जोड़े या रिश्तेदार ने सामाजिक पहचान साझा की। हड्डी के आभूषण व्यक्तिगत वस्तुएं हैं — वे विशेष रूप से मृत व्यक्ति की थीं। कब्रों के बीच आभूषणों की समृद्धि में अंतर सुझाव देता है कि कुछ सदस्यों की उच्च सामाजिक स्थिति थी।"
)

add_open(sec4_en, sec4_hi, "Case Study",
    "Case Study: Wild versus Domesticated Species at Adamgarh Rock Shelters.\nExplain how rock shelter ecology supported the earliest pastoralism in Central India.",
    "मामला अध्ययन: आदमगढ़ शैल आश्रयों में जंगली बनाम पालतू प्रजातियाँ।\nस्पष्ट करें कि शैल आश्रय पारिस्थितिकी ने मध्य भारत में सबसे पहले पशुपालन का समर्थन कैसे किया।",
    "Adamgarh shelters provided a permanent, weatherproof base camp near the Narmada valley grasslands. Small herds of cattle, sheep, and goats could be grazed in the adjacent river meadows during the day and corralled near the shelter entrance at night for protection from predators. The shelter's proximity to fresh water, grasslands, and raw stone material made it an ideal semi-permanent pastoral base camp.",
    "आदमगढ़ के आश्रयों ने नर्मदा घाटी के घास के मैदानों के पास एक स्थायी, मौसम-रोधी आधार शिविर प्रदान किया। मवेशियों, भेड़ों और बकरियों के छोटे झुंडों को दिन में पास की नदी की घास में चराया जा सकता था और रात में शिकारियों से सुरक्षा के लिए आश्रय के प्रवेश द्वार के पास बाड़ में रखा जा सकता था।"
)

# --- 12. Teach the Concept (3 Questions) ---
add_open(sec4_en, sec4_hi, "Teach the Concept",
    "Teach the Concept: Explain why animal domestication is considered the most transformative development in human prehistory.",
    "अवधारणा समझाएं: समझाएं कि पशुपालन को मानव प्रागैतिहास में सबसे परिवर्तनकारी विकास क्यों माना जाता है?",
    "Think about what changes when you own a cow rather than chase deer in the forest. First, you have guaranteed milk, meat, and leather without daily hunting risk. Second, the cow does ploughing for you, reducing farming labour. Third, you produce surplus food — no longer just eating for survival. This surplus allowed trade, specialised crafts, towns, and eventually civilisation. Domestication didn't just change how people ate; it changed how people lived, governed, and thought.",
    "सोचें कि क्या होता है जब आपके पास एक गाय होती है जबकि दूसरी ओर आप जंगल में हिरण का पीछा करते हैं। पहला, आपके पास बिना दैनिक शिकार जोखिम के गारंटीकृत दूध, मांस और चमड़ा है। दूसरा, गाय आपके लिए जुताई करती है। तीसरा, आप अधिशेष भोजन उत्पादित करते हैं। इस अधिशेष ने व्यापार, विशेष शिल्प, शहरों और अंततः सभ्यता की अनुमति दी।"
)

add_open(sec4_en, sec4_hi, "Teach the Concept",
    "Teach the Concept: Explain the concept of 'grave goods' and what they tell archaeologists using a simple gift analogy.",
    "अवधारणा समझाएं: एक सरल उपहार सादृश्य का उपयोग करके 'कब्र के सामान' (grave goods) की अवधारणा और वे पुरातत्वविदों को क्या बताते हैं, इसे समझाएं।",
    "When you gift something precious to a dear friend who is moving far away, you believe it will make their journey better. That is exactly what grave goods represent. Mesolithic families placed necklaces, food, and tools with the dead because they believed those items would be needed in the afterlife, just as you pack a bag for a long trip. When some graves have expensive bone jewellery and others have nothing, it tells us the society was NOT equal — some people had more status or wealth.",
    "जब आप किसी प्रिय मित्र को कुछ कीमती तोहफा देते हैं जो दूर जा रहा हो, तो आप विश्वास करते हैं कि यह उनकी यात्रा को बेहतर बनाएगा। यही कब्र के सामान का प्रतिनिधित्व करता है। मध्यपाषाणकालीन परिवारों ने मृतकों के साथ हार, भोजन और उपकरण रखे क्योंकि उन्हें विश्वास था कि परलोक में उनकी जरूरत होगी। जब कुछ कब्रों में महंगे हड्डी के आभूषण होते हैं और कुछ में कुछ नहीं होता, तो यह हमें बताता है कि समाज असमान था।"
)

add_open(sec4_en, sec4_hi, "Teach the Concept",
    "Teach the Concept: Explain the 'Broad-Spectrum Revolution' in food strategy using the analogy of a restaurant pivot.",
    "अवधारणा समझाएं: रेस्तरां परिवर्तन के सादृश्य का उपयोग करके खाद्य रणनीति में 'व्यापक-स्पेक्ट्रम क्रांति' को समझाएं।",
    "Imagine a restaurant that only serves one dish — a giant steak. If beef prices rise, the restaurant goes bankrupt. But if it pivots to a diverse menu (pasta, salads, grilled chicken, seafood, soup), it survives any single supply disruption. Mesolithic groups did the same: instead of relying only on large deer or elephants, they added fishing, shell gathering, honey, wild seeds, and small game to their menu. This food diversification was their 'pivot strategy' for surviving environmental variability.",
    "एक ऐसे रेस्तरां की कल्पना करें जो केवल एक व्यंजन परोसता है — एक बड़ा स्टेक। यदि गोमांस की कीमतें बढ़ जाती हैं, तो रेस्तरां दिवालिया हो जाता है। लेकिन यदि यह एक विविध मेनू (पास्ता, सलाद, ग्रिल्ड चिकन, समुद्री भोजन, सूप) में बदल जाता है, तो यह किसी भी एकल आपूर्ति व्यवधान से बच जाता है। मध्यपाषाणकालीन समूहों ने भी यही किया: केवल बड़े हिरणों पर निर्भर रहने के बजाय, उन्होंने मछली पकड़ना, घोंघे इकट्ठा करना, शहद, जंगली बीज और छोटे शिकार को अपने मेनू में शामिल किया।"
)
