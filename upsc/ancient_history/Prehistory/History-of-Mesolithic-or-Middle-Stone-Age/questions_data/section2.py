from .helpers import add_mcq, add_multi_mcq, add_tf, add_blank, add_match, add_oneliner, add_ar, add_stmt, add_open

sec2_en = []
sec2_hi = []

# --- 1. MCQ (5 Questions) ---
add_mcq(sec2_en, sec2_hi,
    "What is the typical length range of a diagnostic Mesolithic stone tool (microlith)?",
    "मध्यपाषाण काल के नैदानिक पत्थर के उपकरण (सूक्ष्म पाषाण) की विशिष्ट लंबाई सीमा क्या है?",
    ["10 to 20 cm", "1 to 8 cm", "0.1 to 0.5 cm", "25 to 50 cm"],
    ["10 से 20 सेमी", "1 से 8 सेमी", "0.1 से 0.5 सेमी", "25 से 50 सेमी"],
    1,
    "Microliths are defined by their tiny size, typically ranging between 1 cm and 8 cm in length, designed for composite hafting.",
    "सूक्ष्म पाषाणों को उनके छोटे आकार से परिभाषित किया जाता है, जो आमतौर पर लंबाई में 1 सेमी और 8 सेमी के बीच होते हैं, जिन्हें संयुक्त हत्था लगाने (composite hafting) के लिए डिज़ाइन किया गया था।"
)

add_mcq(sec2_en, sec2_hi,
    "The specialized method of notch-chipping used to break small blades cleanly into geometric segments is called the:",
    "छोटे ब्लेडों को ज्यामितीय खंडों में सफाई से तोड़ने के लिए उपयोग की जाने वाली विशेष नॉच-चिपिंग विधि को कहा जाता है:",
    ["Acheulian handaxe flaking", "Nevasan retouching", "Micro-burin technique", "Levallois core preparation"],
    ["एशुलेयिन हस्तकुठार शल्कन", "नेवासन घिसाई (retouching)", "माइक्रो-ब्यूरिन तकनीक", "लेवालोइस कोर तैयारी"],
    2,
    "The micro-burin technique is a specialized archaeological diagnostic method used to section micro-blades cleanly into triangles or lunates.",
    "माइक्रो-ब्यूरिन तकनीक एक विशेष पुरातात्विक विधि है जिसका उपयोग माइक्रो-ब्लेड को त्रिकोण या चंद्राकार में सफाई से काटने के लिए किया जाता था।"
)

add_mcq(sec2_en, sec2_hi,
    "Which of the following is classified as a geometric microlith shape?",
    "निम्नलिखित में से किसे ज्यामितीय सूक्ष्म पाषाण आकार के रूप में वर्गीकृत किया गया है?",
    ["Backed blade", "Scraper-flake", "Lunate (crescent)", "Bifacial handaxe"],
    ["बैक्ड ब्लेड", "खुरचनी-शल्क", "चंद्राकार (lunate)", "द्वि-मुखी हस्तकुठार"],
    2,
    "Geometric microliths include specific shapes like lunates (crescents), triangles, and trapezes. Backed blades are non-geometric.",
    "ज्यामितीय सूक्ष्म पाषाणों में चंद्राकार (lunates), त्रिकोण और समलंब (trapezes) जैसे विशिष्ट आकार शामिल हैं। बैक्ड ब्लेड गैर-ज्यामितीय हैं।"
)

add_mcq(sec2_en, sec2_hi,
    "Which raw material family became dominant in the Mesolithic period, replacing coarse quartzite?",
    "मध्यपाषाण काल में मोटे क्वार्ट्जाइट का स्थान लेकर कौन सा कच्चा माल परिवार हावी हो गया?",
    ["Fine-grained cryptocrystalline silica (chert, chalcedony, jasper)", "Coarse Vindhyan sandstones", "Limestone outcrops", "Deccan basalt sheets"],
    ["महीन सिलिका पत्थर (चर्ट, चाल्सीडोनी, जैस्पर)", "मोटे विंध्यन बलुआ पत्थर", "चूना पत्थर", "दक्कन बेसाल्ट परतें"],
    0,
    "Mesolithic toolmakers shifted to fine-grained silica stones like chert, chalcedony, jasper, and agate, which fractured predictably to produce razor-sharp edges.",
    "मध्यपाषाणकालीन उपकरण निर्माताओं ने चर्ट, चाल्सीडोनी, जैस्पर और अगेट जैसे महीन सिलिका पत्थरों को चुना, जो अत्यधिक तीखे किनारे बनाने के लिए आसानी से टूटते थे।"
)

add_mcq(sec2_en, sec2_hi,
    "The archaeological term for securing stone microliths into slots of wooden or bone handles using natural resins is:",
    "प्राकृतिक राल का उपयोग करके लकड़ी या हड्डी के हैंडल के खांचों में पत्थर के सूक्ष्म पाषाणों को सुरक्षित करने का पुरातात्विक शब्द है:",
    ["Hafting", "Knapping", "Levallois flaking", "Retouching"],
    ["हत्था लगाना (Hafting)", "नैपिंग (Knapping)", "लेवालोइस शल्कन", "घिसाई (Retouching)"],
    0,
    "Hafting refers to attaching a stone point or blade to a wooden/bone shaft or handle to form a composite tool.",
    "हत्था लगाने (Hafting) से तात्पर्य एक संयुक्त उपकरण बनाने के लिए लकड़ी/हड्डी के हैंडल में एक पत्थर की नोक या ब्लेड को जोड़ने से है।"
)

# --- 2. Multiple Correct MCQ (5 Questions) ---
add_multi_mcq(sec2_en, sec2_hi,
    "Which of the following are classified as geometric shapes of microliths? (Select all that apply)",
    "निम्नलिखित में से किसे सूक्ष्म पाषाणों के ज्यामितीय आकार के रूप में वर्गीकृत किया गया है? (सभी सही विकल्प चुनें)",
    ["Lunates (crescents)", "Triangles", "Trapezes", "Backed blades"],
    ["चंद्राकार (lunates)", "त्रिकोण", "समलंब (trapezes)", "बैक्ड ब्लेड (backed blades)"],
    [0, 1, 2],
    "Geometric shapes have specific geometric symmetry like lunates, triangles, and trapezes. Backed blades are straight and non-geometric.",
    "ज्यामितीय आकारों में चंद्राकार, त्रिकोण और समलंब जैसी विशिष्ट ज्यामितीय समरूपता होती है। बैक्ड ब्लेड सीधे और गैर-ज्यामितीय होते हैं।"
)

add_multi_mcq(sec2_en, sec2_hi,
    "Which raw materials were widely preferred by Mesolithic toolmakers for making micro-blades? (Select all that apply)",
    "सूक्ष्म ब्लेड बनाने के लिए मध्यपाषाणकालीन उपकरण निर्माताओं द्वारा किन कच्चे मालों को व्यापक रूप से पसंद किया गया था? (सभी सही विकल्प चुनें)",
    ["Chert", "Chalcedony", "Agate", "Coarse sandstone"],
    ["चर्ट", "चाल्सीडोनी", "अगेट", "मोटा बलुआ पत्थर"],
    [0, 1, 2],
    "Chert, chalcedony, and agate are crypto-crystalline silica rocks preferred for microliths. Coarse sandstone is too granular and unsuitable for micro-blades.",
    "चर्ट, चाल्सीडोनी और अगेट सूक्ष्म पाषाणों के लिए पसंद किए जाने वाले सिलिका पत्थर हैं। मोटा बलुआ पत्थर बहुत दानेदार होता है और सूक्ष्म ब्लेड के लिए अनुपयुक्त है।"
)

add_multi_mcq(sec2_en, sec2_hi,
    "Which of the following composite tools were manufactured by hafting microliths? (Select all that apply)",
    "सूक्ष्म पाषाणों को हत्था लगाकर निम्नलिखित में से कौन से संयुक्त उपकरण बनाए गए थे? (सभी सही विकल्प चुनें)",
    ["Bows and arrows", "Harpoons for fishing", "Sickles for harvesting", "Acheulian cleavers"],
    ["तीर-कमान", "मछली पकड़ने के लिए हारपून", "फसल काटने के हंसिया", "एशुलेयिन विदारक"],
    [0, 1, 2],
    "Microliths were hafted into arrows, harpoons, and sickles. Acheulian cleavers are large, single core tools from the Lower Paleolithic.",
    "सूक्ष्म पाषाणों को तीर, हारपून और हंसिया में लगाया जाता था। एशुलेयिन विदारक निम्न पुरापाषाण काल के बड़े, एकल कोर उपकरण हैं।"
)

add_multi_mcq(sec2_en, sec2_hi,
    "Which manufacturing features are associated with the 'pressure flaking' technique? (Select all that apply)",
    "'दबाव शल्कन' (pressure flaking) तकनीक से कौन सी निर्माण विशेषताएं जुड़ी हुई हैं? (सभी सही विकल्प चुनें)",
    ["Using a pointed bone or wood tool to push off tiny flakes", "Striking the core directly with a massive stone hammer", "Producing highly standardized, uniform micro-blades", "Complete absence of prepared core methods"],
    ["छोटे शल्क निकालने के लिए एक नुकीले हड्डी या लकड़ी के उपकरण का उपयोग करना", "एक बड़े पत्थर के हथौड़े से सीधे कोर पर वार करना", "अत्यधिक मानकीकृत, समान सूक्ष्म ब्लेड का उत्पादन करना", "तैयार कोर विधियों का पूर्ण अभाव"],
    [0, 2],
    "Pressure flaking uses a wooden/bone pointer to press off flakes, producing standardized blades. Direct hard hammer blows are associated with earlier knapping styles.",
    "दबाव शल्कन में शल्क निकालने के लिए लकड़ी/हड्डी के नुकीले उपकरण का उपयोग किया जाता है, जिससे मानकीकृत ब्लेड बनते हैं। सीधे हथौड़े के प्रहार पहले की शैलियों से जुड़े हैं।"
)

add_multi_mcq(sec2_en, sec2_hi,
    "What advantages did composite microlithic tools have over Paleolithic handaxes? (Select all that apply)",
    "पुरापाषाणकालीन हस्तकुठार की तुलना में संयुक्त सूक्ष्म पाषाण उपकरणों के क्या लाभ थे? (सभी सही विकल्प चुनें)",
    ["Light weight, allowing projectile hunting from a safe distance", "Ease of repair by replacing individual broken inserts", "Maximum efficiency, yielding more cutting edge per kilogram of raw material", "Complete elimination of organic handles"],
    ["हल्का वजन, जो सुरक्षित दूरी से प्रक्षेपास्त्र शिकार की अनुमति देता था", "टूटने पर व्यक्तिगत पाषाणों को बदलकर मरम्मत करने में आसानी", "अधिकतम दक्षता, प्रति किलोग्राम कच्चे माल में अधिक धारदार किनारा प्राप्त होना", "जैविक हैंडल का पूर्ण उन्मूलन"],
    [0, 1, 2],
    "Composite tools were lightweight, easily repaired by replacing inserts, and highly resource-efficient. Organic handles were introduced, not eliminated.",
    "संयुक्त उपकरण हल्के थे, व्यक्तिगत पाषाणों को बदलकर आसानी से मरम्मत किए जा सकते थे और अत्यधिक संसाधन-कुशल थे। जैविक हैंडल को शामिल किया गया था, न कि समाप्त किया गया था।"
)

# --- 3. True/False (8 Questions) ---
add_tf(sec2_en, sec2_hi,
    "Geometric microliths include backed blades and micro-points.",
    "ज्यामितीय सूक्ष्म पाषाणों में बैक्ड ब्लेड और सूक्ष्म शूल (points) शामिल हैं।",
    False,
    "Backed blades and points are non-geometric microliths; geometric ones have specific geometric shapes like triangles or lunates.",
    "बैक्ड ब्लेड और शूल गैर-ज्यामितीय सूक्ष्म पाषाण हैं; ज्यामितीय पाषाणों के विशिष्ट आकार जैसे त्रिकोण या चंद्राकार होते हैं।"
)

add_tf(sec2_en, sec2_hi,
    "Pressure flaking involves hitting the stone core with a heavy quartzite hammerstone.",
    "दबाव शल्कन में भारी क्वार्ट्जाइट हथौड़े से पत्थर के कोर पर वार करना शामिल है।",
    False,
    "Pressure flaking involves applying steady, controlled pressure using an antler or wooden pointer to detach flakes.",
    "दबाव शल्कन में शल्क निकालने के लिए सींग या लकड़ी के उपकरण का उपयोग करके नियंत्रित दबाव डाला जाता है।"
)

add_tf(sec2_en, sec2_hi,
    "Microliths were rarely used individually; they were designed to be hafted as inserts in composite tools.",
    "सूक्ष्म पाषाणों का शायद ही कभी व्यक्तिगत रूप से उपयोग किया जाता था; उन्हें संयुक्त उपकरणों में फिट करने के लिए डिज़ाइन किया गया था।",
    True,
    "The true value of microliths was as components of composite tools like arrows, spears, or sickles.",
    "सूक्ष्म पाषाणों का वास्तविक मूल्य तीर, भाले या हंसिया जैसे संयुक्त उपकरणों के घटकों के रूप में था।"
)

add_tf(sec2_en, sec2_hi,
    "Quartzite remained the dominant material for making microliths during the Mesolithic.",
    "मध्यपाषाण काल के दौरान सूक्ष्म पाषाण बनाने के लिए क्वार्ट्जाइट प्रमुख सामग्री बना रहा।",
    False,
    "Quartzite was replaced by fine-grained silica stones like chert and chalcedony.",
    "क्वार्ट्जाइट का स्थान चर्ट और चाल्सीडोनी जैसे महीन सिलिका पत्थरों ने ले लिया था।"
)

add_tf(sec2_en, sec2_hi,
    "Prehistoric artisans used natural adhesives like plant resins and asphalt to stick microliths into wood or bone handles.",
    "प्रागैतिहासिक कारीगरों ने लकड़ी या हड्डी के हैंडल में सूक्ष्म पाषाणों को चिपकाने के लिए प्राकृतिक राल और डामर का उपयोग किया।",
    True,
    "Resins, tar, and gum were heated to serve as powerful adhesives for hafting microliths.",
    "हत्था लगाने के लिए राल, डामर और गोंद को गर्म करके शक्तिशाली चिपकने वाले पदार्थ के रूप में उपयोग किया जाता था।"
)

add_tf(sec2_en, sec2_hi,
    "The micro-burin technique is a method of wood-carving rather than stone tool manufacturing.",
    "माइक्रो-ब्यूरिन तकनीक पत्थर के औजार निर्माण के बजाय लकड़ी की नक्काशी की एक विधि है।",
    False,
    "The micro-burin technique is a stone knapping method used to section micro-blades cleanly.",
    "माइक्रो-ब्यूरिन तकनीक पत्थर के ब्लेड को सफाई से काटने की एक निर्माण विधि है।"
)

add_tf(sec2_en, sec2_hi,
    "Non-geometric microliths generally appeared before geometric microliths in the stratigraphic sequences of India.",
    "भारत के स्तरविन्यासात्मक अनुक्रमों में गैर-ज्यामितीय सूक्ष्म पाषाण आमतौर पर ज्यामितीय सूक्ष्म पाषाणों से पहले दिखाई दिए।",
    True,
    "Stratigraphic sequences (e.g., at Bagor) prove non-geometric microliths preceded the development of geometric forms.",
    "स्तरविन्यासात्मक अनुक्रम (जैसे बागोर में) साबित करते हैं कि गैर-ज्यामितीय सूक्ष्म पाषाण ज्यामितीय रूपों से पहले विकसित हुए थे।"
)

add_tf(sec2_en, sec2_hi,
    "The introduction of bows and arrows occurred for the first time during the Mesolithic phase in India.",
    "भारत में मध्यपाषाण काल के दौरान पहली बार तीर-कमान की शुरुआत हुई थी।",
    True,
    "The lightweight microlith arrowheads enabled the development and widespread use of the bow and arrow.",
    "हल्के सूक्ष्म पाषाण अग्रभागों ने तीर-कमान के विकास और व्यापक उपयोग को संभव बनाया।"
)

# --- 4. Fill in the Blank (8 Questions) ---
add_blank(sec2_en, sec2_hi,
    "The typical length of a diagnostic microlith ranges from 1 to ________ centimeters.",
    "एक नैदानिक सूक्ष्म पाषाण की विशिष्ट लंबाई 1 से ________ सेंटीमीटर तक होती है।",
    "8", "8",
    "Microliths are defined as tiny tools between 1 and 8 cm in length.",
    "सूक्ष्म पाषाणों को 1 से 8 सेमी लंबाई के छोटे उपकरणों के रूप में परिभाषित किया जाता है।"
)

add_blank(sec2_en, sec2_hi,
    "Fine-grained silica stones like chert and ________ were preferred for microliths.",
    "सूक्ष्म पाषाणों के लिए चर्ट और ________ जैसे महीन सिलिका पत्थरों को प्राथमिकता दी जाती थी।",
    "chalcedony", "चाल्सीडोनी",
    "Chalcedony was highly favored for its clean conchoidal fracture and razor-sharp flakes.",
    "चाल्सीडोनी को उसके साफ फ्रैक्चर और तीखे शल्कों के कारण अत्यधिक पसंद किया जाता था।"
)

add_blank(sec2_en, sec2_hi,
    "The process of fixing stone inserts into wood or bone slots is called ________.",
    "लकड़ी या हड्डी के खांचों में पत्थर के पाषाणों को फिट करने की प्रक्रिया को ________ कहा जाता है।",
    "hafting", "हत्था लगाना",
    "Hafting attaches the blade or point to a handle or shaft to form a composite tool.",
    "हत्था लगाने से ब्लेड या नोक को एक हैंडल या शाफ्ट से जोड़ा जाता है जिससे संयुक्त उपकरण बनता है।"
)

add_blank(sec2_en, sec2_hi,
    "A crescent-shaped geometric microlith is technically termed a ________.",
    "एक अर्धचंद्राकार ज्यामितीय सूक्ष्म पाषाण को तकनीकी रूप से ________ कहा जाता है।",
    "lunate", "चंद्राकार",
    "Lunates have a curved backed edge and a straight cutting edge, resembling a crescent.",
    "चंद्राकारों में एक घुमावदार किनारा और एक सीधा काटने वाला किनारा होता है, जो अर्धचंद्र जैसा दिखता है।"
)

add_blank(sec2_en, sec2_hi,
    "The specialized method used to snap micro-blades cleanly is the ________-burin technique.",
    "सूक्ष्म ब्लेडों को सफाई से तोड़ने के लिए प्रयुक्त विशेष विधि को ________-ब्यूरिन तकनीक कहा जाता है।",
    "micro", "माइक्रो",
    "The micro-burin technique was used to section blades into geometric shapes.",
    "माइक्रो-ब्यूरिन तकनीक का उपयोग ब्लेड को ज्यामितीय आकारों में काटने के लिए किया जाता था।"
)

add_blank(sec2_en, sec2_hi,
    "Adhesive paste made of plant ________ was heated to secure microliths to shafts.",
    "सूक्ष्म पाषाणों को शाफ्ट से सुरक्षित करने के लिए पौधों की ________ से बने चिपकने वाले पेस्ट को गर्म किया जाता था।",
    "resin", "राल",
    "Natural plant resins or gums acted as strong adhesives for composite tools.",
    "प्राकृतिक पौधों की राल या गोंद संयुक्त उपकरणों के लिए मजबूत चिपकने वाले के रूप में कार्य करते थे।"
)

add_blank(sec2_en, sec2_hi,
    "Tools made of multiple stone parts fitted together are called ________ tools.",
    "एक साथ फिट किए गए कई पत्थरों के हिस्सों से बने औजारों को ________ उपकरण कहा जाता है।",
    "composite", "संयुक्त",
    "Composite tools (like sickles and harpoons) combine stone inserts with wooden/bone shafts.",
    "संयुक्त उपकरण (जैसे हंसिया और हारपून) लकड़ी/हड्डी के शाफ्ट के साथ पत्थर के पाषाणों को जोड़ते हैं।"
)

add_blank(sec2_en, sec2_hi,
    "Steady force applied to a core using a bone pointer defines the ________ flaking technique.",
    "हड्डी के नुकीले उपकरण का उपयोग करके कोर पर लगातार बल लगाना ________ शल्कन तकनीक को परिभाषित करता है।",
    "pressure", "दबाव",
    "Pressure flaking allows the systematic extraction of micro-blades from prepared cores.",
    "दबाव शल्कन तैयार कोर से सूक्ष्म ब्लेड के व्यवस्थित निष्कर्षण की अनुमति देता है।"
)

# --- 5. Match the Following (3 Questions) ---
add_match(sec2_en, sec2_hi,
    "Match the geometric microlith shapes with their geometric definitions:",
    "ज्यामितीय सूक्ष्म पाषाण आकारों को उनके ज्यामितीय विवरणों से सुमेलित करें:",
    ["1. Lunate", "2. Triangle", "3. Trapeze"],
    ["1. चंद्राकार (Lunate)", "2. त्रिकोण (Triangle)", "3. समलंब (Trapeze)"],
    ["A. Crescent shape with one curved backed edge", "B. Three-sided shape with retouched edges", "C. Four-sided quadrilateral with two parallel edges"],
    ["A. एक घुमावदार किनारे वाला अर्धचंद्राकार रूप", "B. घिसे हुए किनारों वाला तीन पक्षों का आकार", "C. दो समानांतर किनारों वाला चार पक्षों का चतुर्भुज"],
    "1-A, 2-B, 3-C. Lunates are crescents; triangles are 3-sided; trapezes are 4-sided quadrilaterals.",
    "1-A, 2-B, 3-C. चंद्राकार अर्धचंद्र हैं; त्रिकोण 3-पक्षीय हैं; समलंब 4-पक्षीय चतुर्भुज हैं।"
)

add_match(sec2_en, sec2_hi,
    "Match the stone age phases with their primary raw material categories:",
    "पाषाण युग के चरणों को उनके प्राथमिक कच्चे माल की श्रेणियों से सुमेलित करें:",
    ["1. Lower Paleolithic", "2. Mesolithic Phase", "3. Chalcolithic Transition"],
    ["1. निम्न पुरापाषाण", "2. मध्यपाषाण चरण", "3. ताम्रपाषाण संक्रमण"],
    ["A. Coarse quartzite blocks & limestone", "B. Cryptocrystalline silica (Chert & Chalcedony)", "C. Microliths alongside copper implements"],
    ["A. मोटे क्वार्ट्जाइट ब्लॉक और चूना पत्थर", "B. महीन सिलिका पत्थर (चर्ट और चाल्सीडोनी)", "C. तांबे के औजारों के साथ-साथ सूक्ष्म पाषाण"],
    "1-A, 2-B, 3-C. Lower Paleolithic used quartzite/limestone; Mesolithic shifted to chert/chalcedony; Chalcolithic integrated early copper tools.",
    "1-A, 2-B, 3-C. निम्न पुरापाषाण में क्वार्ट्जाइट/चूना पत्थर का उपयोग किया गया; मध्यपाषाण में चर्ट/चाल्सीडोनी का उपयोग हुआ; ताम्रपाषाण में प्रारंभिक तांबे के उपकरणों को शामिल किया गया।"
)

add_match(sec2_en, sec2_hi,
    "Match the composite tool component with its function:",
    "संयुक्त उपकरण के घटक को उसके कार्य से सुमेलित करें:",
    ["1. Microlith bladelets", "2. Wooden/bone shafts", "3. Organic resin/tar"],
    ["1. सूक्ष्म पाषाण ब्लेड", "2. लकड़ी/हड्डी के शाफ्ट", "3. कार्बनिक राल/डामर"],
    ["A. Served as cutting edges or barbs", "B. Formed the main handle or structural body", "C. Served as the binding adhesive"],
    ["A. काटने वाले किनारों या शूलों के रूप में कार्य करना", "B. मुख्य हैंडल या संरचनात्मक शरीर का निर्माण करना", "C. चिपकने वाले बंधन के रूप में कार्य करना"],
    "1-A, 2-B, 3-C. Microliths cut/barb; shafts provide structure; resins act as adhesive glue.",
    "1-A, 2-B, 3-C. सूक्ष्म पाषाण काटते/चुभते हैं; शाफ्ट संरचना प्रदान करते हैं; राल चिपकने वाले गोंद का काम करती है।"
)

# --- 6. One-Liner (8 Questions) ---
add_oneliner(sec2_en, sec2_hi,
    "Define a stone age microlith.",
    "पाषाण युग के सूक्ष्म पाषाण (microlith) को परिभाषित करें।",
    "A miniature stone tool measuring 1-8 cm, made on fine-grained silica stones.",
    "एक लघु पत्थर का उपकरण (1-8 सेमी) जो महीन सिलिका पत्थरों से बनाया जाता था।"
)

add_oneliner(sec2_en, sec2_hi,
    "What does the term 'hafting' mean in prehistoric technology?",
    "प्रागैतिहासिक तकनीक में 'हत्था लगाने' (hafting) का क्या अर्थ है?",
    "Securing a stone point, blade, or microlith into a wooden or bone shaft or handle.",
    "लकड़ी या हड्डी के शाफ्ट या हैंडल में पत्थर की नोक या सूक्ष्म पाषाण को सुरक्षित करना।"
)

add_oneliner(sec2_en, sec2_hi,
    "Name three standard geometric shapes of Indian microliths.",
    "भारतीय सूक्ष्म पाषाणों के तीन मानक ज्यामितीय आकारों के नाम बताएं।",
    "Lunate (crescent), triangle, and trapeze.",
    "चंद्राकार (lunate), त्रिकोण और समलंब (trapeze)।"
)

add_oneliner(sec2_en, sec2_hi,
    "What is a lunate in Mesolithic tool typology?",
    "मध्यपाषाण उपकरण वर्गीकरण में चंद्राकार (lunate) क्या है?",
    "A crescent-shaped stone tool with one straight cutting edge and one curved, backed edge.",
    "एक अर्धचंद्राकार पत्थर का उपकरण जिसमें एक सीधा काटने वाला किनारा और एक घुमावदार किनारा होता है।"
)

add_oneliner(sec2_en, sec2_hi,
    "Why did conchoidal fracture properties make chalcedony a preferred raw material?",
    "शंखाभ अपभ्रंश (conchoidal fracture) गुणों के कारण चाल्सीडोनी को एक पसंदीदा कच्चा माल क्यों बनाया गया?",
    "It fractures predictably to yield extremely thin, sharp-edged micro-blades.",
    "यह अनुमानित रूप से टूटता है जिससे अत्यधिक पतले, तेज धार वाले सूक्ष्म-ब्लेड प्राप्त होते हैं।"
)

add_oneliner(sec2_en, sec2_hi,
    "What are composite tools?",
    "संयुक्त (composite) उपकरण क्या हैं?",
    "Tools made by fitting multiple stone blades/points into organic shafts or handles.",
    "लकड़ी या हड्डी के शाफ्ट में पत्थर के कई हिस्सों को फिट करके बनाए गए उपकरण।"
)

add_oneliner(sec2_en, sec2_hi,
    "What is the function of the micro-burin technique?",
    "माइक्रो-ब्यूरिन तकनीक का क्या कार्य है?",
    "To snap micro-blades cleanly and systematically into geometric segments.",
    "सूक्ष्म ब्लेडों को ज्यामितीय खंडों में सफाई से और व्यवस्थित रूप से तोड़ना।"
)

add_oneliner(sec2_en, sec2_hi,
    "Name two natural adhesive substances used for hafting.",
    "हत्था लगाने के लिए उपयोग किए जाने वाले दो प्राकृतिक चिपकने वाले पदार्थों के नाम बताएं।",
    "Tree resin (gum) and natural asphalt (tar).",
    "वृक्षों की राल (गोंद) और प्राकृतिक डामर (राल)।"
)

# --- 7. Assertion-Reason (8 Questions) ---
add_ar(sec2_en, sec2_hi,
    "Assertion (A): Microlithic technology represents a dramatic increase in resource-use efficiency.\nReason (R): A single small chert core can yield dozens of sharp blades, generating more cutting edges per kilogram of stone than Paleolithic methods.",
    "कथन (A): सूक्ष्म पाषाण तकनीक संसाधन-उपयोग दक्षता में भारी वृद्धि का प्रतिनिधित्व करती है।\nकारण (R): एक छोटा चर्ट कोर दर्जनों तीखे ब्लेड प्रदान कर सकता है, जिससे पुरापाषाणकालीन तरीकों की तुलना में प्रति किलोग्राम पत्थर में अधिक धारदार किनारे प्राप्त होते हैं।",
    0,
    "Both A and R are true, and R explains why microliths represent a major increase in resource-use efficiency.",
    "A और R दोनों सही हैं, और R स्पष्ट करता है कि क्यों सूक्ष्म पाषाण संसाधन-उपयोग दक्षता में भारी वृद्धि दर्शाते हैं।"
)

add_ar(sec2_en, sec2_hi,
    "Assertion (A): Non-geometric backed blades are classified as Acheulian handaxes.\nReason (R): Both tools were designed to be held directly in the hand without any handles or shafts.",
    "कथन (A): गैर-ज्यामितीय बैक्ड ब्लेड को एशुलेयिन हस्तकुठार के रूप में वर्गीकृत किया गया है।\nकारण (R): दोनों उपकरणों को बिना किसी हैंडल या शाफ्ट के सीधे हाथ में पकड़ने के लिए डिज़ाइन किया गया था।",
    3,
    "A is false as backed blades are microliths, not handaxes; R is false as microliths were hafted, and handaxes were held directly.",
    "A गलत है क्योंकि बैक्ड ब्लेड सूक्ष्म पाषाण हैं, हस्तकुठार नहीं; R गलत है क्योंकि सूक्ष्म पाषाणों में हत्था लगाया जाता था और हस्तकुठार सीधे पकड़े जाते थे।"
)

add_ar(sec2_en, sec2_hi,
    "Assertion (A): The invention of the bow and arrow occurred alongside microlithic development during the Mesolithic.\nReason (R): Light, small microlithic points were aerodynamically suitable to serve as arrowheads.",
    "कथन (A): मध्यपाषाण काल के दौरान सूक्ष्म पाषाण विकास के साथ-साथ तीर-कमान का आविष्कार हुआ।\nकारण (R): हल्के, छोटे सूक्ष्म पाषाण अग्रभाग वायुगतिकी रूप से तीर के अग्रभाग (arrowheads) के रूप में कार्य करने के लिए उपयुक्त थे।",
    0,
    "Both A and R are true, and R explains why microliths enabled bow and arrow technology.",
    "A और R दोनों सही हैं, और R स्पष्ट करता है कि क्यों सूक्ष्म पाषाणों ने तीर-कमान तकनीक को संभव बनाया।"
)

add_ar(sec2_en, sec2_hi,
    "Assertion (A): Heated tree resin was used as a binding glue in composite tools.\nReason (R): Resins melt when heated and solidify upon cooling, creating a tight lock around stone inserts.",
    "कथन (A): संयुक्त उपकरणों में बंधन गोंद के रूप में गर्म राल का उपयोग किया जाता था।\nकारण (R): राल गर्म करने पर पिघलती है और ठंडा होने पर जम जाती है, जिससे पत्थर के औजारों के चारों ओर एक मजबूत पकड़ बन जाती है।",
    0,
    "Both are true, and R explains the chemical property that made resin a perfect prehistoric adhesive glue.",
    "दोनों सही हैं, और R उस रासायनिक गुण को समझाता है जिसने राल को एक आदर्श प्रागैतिहासिक चिपकने वाला गोंद बना दिया।"
)

add_ar(sec2_en, sec2_hi,
    "Assertion (A): Quartzite was completely abandoned at all Mesolithic sites in India.\nReason (R): Quartzite lacks the structural composition to be retouched or backed into geometric shapes.",
    "कथन (A): भारत के सभी मध्यपाषाणकालीन स्थलों पर क्वार्ट्जाइट को पूरी तरह से त्याग दिया गया था।\nकारण (R): क्वार्ट्जाइट में ज्यामितीय आकृतियों में बदलने या घिसने के लिए आवश्यक संरचनात्मक संरचना का अभाव होता है।",
    3,
    "A is false as some sites still used quartzite occasionally; R is false because quartzite can be retouched, though fine silica is preferred.",
    "A गलत है क्योंकि कुछ स्थलों पर अभी भी कभी-कभी क्वार्ट्जाइट का उपयोग किया जाता था; R गलत है क्योंकि क्वार्ट्जाइट को घिसा जा सकता है, हालांकि महीन सिलिका को प्राथमिकता दी जाती है।"
)

add_ar(sec2_en, sec2_hi,
    "Assertion (A): Geometric microliths like trapezes were utilized as barbs on harpoons.\nReason (R): Their straight margins and flat shapes allowed multiple pieces to be fitted flush into narrow bone grooves.",
    "कथन (A): समलंब (trapezes) जैसे ज्यामितीय सूक्ष्म पाषाणों का उपयोग हारपून पर शूल (barbs) के रूप में किया जाता था।\nकारण (R): उनके सीधे किनारों और चपटे आकार ने कई टुकड़ों को हड्डी के संकीर्ण खांचों में एक साथ फिट करने की अनुमति दी।",
    0,
    "Both are true, and R explains why the geometric shape of trapezes was selected for composite harpoons.",
    "दोनों सही हैं, और R समझाता है कि संयुक्त हारपून के लिए समलंब के ज्यामितीय आकार को क्यों चुना गया था।"
)

add_ar(sec2_en, sec2_hi,
    "Assertion (A): Micro-burin flakes are classified as tool production waste, not tools.\nReason (R): The micro-burin technique snaps a blade, leaving a waste remnant showing a clean diagonal fracture.",
    "कथन (A): माइक्रो-ब्यूरिन शल्क को उपकरण निर्माण का कचरा माना जाता है, उपकरण नहीं।\nकारण (R): माइक्रो-ब्यूरिन तकनीक ब्लेड को तोड़ती है, जिससे एक अपशिष्ट अवशेष बचता है जो एक साफ तिरछा फ्रैक्चर दिखाता है।",
    0,
    "Both are true, and R explains why micro-burins are waste debitage generated during geometric blade snapping.",
    "दोनों सही हैं, और R स्पष्ट करता है कि क्यों माइक्रो-ब्यूरिन ब्लेड को तोड़ने के दौरान उत्पन्न होने वाला अपशिष्ट मलबे (debitage) हैं।"
)

add_ar(sec2_en, sec2_hi,
    "Assertion (A): Microliths allowed the utilization of lightweight organic handles.\nReason (R): Organic materials like wood and bone provide excellent structural handles that increase leverage and throwing distance.",
    "कथन (A): सूक्ष्म पाषाणों ने हल्के जैविक हैंडल (हत्था) के उपयोग की अनुमति दी।\nकारण (R): लकड़ी और हड्डी जैसी जैविक सामग्रियां उत्कृष्ट संरचनात्मक हैंडल प्रदान करती हैं जो लीवर प्रभाव और फेंकने की दूरी को बढ़ाती हैं।",
    0,
    "Both are true, and R explains why the use of organic shafts and handles was technologically advantageous.",
    "दोनों सही हैं, और R समझाता है कि क्यों जैविक शाफ्ट और हैंडल का उपयोग तकनीकी रूप से फायदेमंद था।"
)

# --- 8. Statement-Based (5 Questions) ---
add_stmt(sec2_en, sec2_hi,
    "Consider the following statements regarding microlithic shapes:\n1. Lunates are geometric microliths characterized by a curved backed edge and a straight cutting edge.\n2. Triangles have three retouched margins and were used primarily as projectile points.\nWhich of the statements given above is/are correct?",
    "सूक्ष्म पाषाण आकृतियों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. चंद्राकार (lunates) ज्यामितीय सूक्ष्म पाषाण हैं जो एक घुमावदार किनारे और एक सीधे काटने वाले किनारे द्वारा पहचाने जाते हैं।\n2. त्रिकोणों में तीन घिसे हुए किनारे होते हैं और इनका उपयोग मुख्य रूप से प्रक्षेपास्त्र नोक के रूप में किया जाता था।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
    2,
    "Both statements are correct. Lunates are crescent-shaped with curved backs, and triangles were used as arrowheads or spear tips.",
    "दोनों कथन सही हैं। चंद्राकार घुमावदार पीठ के साथ अर्धचंद्राकार होते हैं, और त्रिकोणों का उपयोग तीर या भाले की नोक के रूप में किया जाता था।"
)

add_stmt(sec2_en, sec2_hi,
    "With reference to the raw materials of the Mesolithic tools, consider the following statements:\n1. The transition is marked by a shift from coarse quartzite to cryptocrystalline silica like chalcedony and chert.\n2. Chalcedony was preferred because it fractures along cleavage planes, not conchoidal fractures.\nWhich of the statements given above is/are correct?",
    "मध्यपाषाणकालीन उपकरणों के कच्चे माल के संदर्भ में, निम्नलिखित कथनों पर विचार करें:\n1. यह संक्रमण मोटे क्वार्ट्जाइट से चाल्सीडोनी और चर्ट जैसे सिलिका पत्थरों की ओर झुकाव द्वारा चिह्नित है।\n2. चाल्सीडोनी को इसलिए पसंद किया गया क्योंकि यह क्लीवेज प्लेन के अनुदिश टूटता है, शंखाभ अपभ्रंश (conchoidal fracture) से नहीं।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
    0,
    "Statement 1 is correct. Statement 2 is incorrect because chalcedony and chert fracture conchoidally (not along cleavage planes), which creates extremely sharp edges.",
    "कथन 1 सही है। कथन 2 गलत है क्योंकि चाल्सीडोनी और चर्ट शंखाभ अपभ्रंश (conchoidally) में टूटते हैं (क्लीवेज प्लेन के अनुदिश नहीं), जिससे बेहद तीखे किनारे बनते हैं।"
)

add_stmt(sec2_en, sec2_hi,
    "Consider the following statements regarding the prepared core pressure flaking technique:\n1. Flakes were struck off using direct heavy stone-on-stone blows.\n2. It utilized a bone pointer pressed steadily against the core edge to pop off uniform blades.\nWhich of the statements given above is/are correct?",
    "तैयार कोर दबाव शल्कन (pressure flaking) तकनीक के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. सीधे भारी पत्थर से पत्थर पर चोट करके शल्क निकाले जाते थे।\n2. इसमें एक समान ब्लेड निकालने के लिए कोर के किनारे पर हड्डी के नुकीले उपकरण से लगातार दबाव डाला जाता था।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
    1,
    "Statement 1 is incorrect as pressure flaking does not involve striking. Statement 2 is correct, detailing the pressure knapping method.",
    "कथन 1 गलत है क्योंकि दबाव शल्कन में प्रहार शामिल नहीं होता है। कथन 2 सही है, जो दबाव शल्कन विधि का विवरण देता है।"
)

add_stmt(sec2_en, sec2_hi,
    "Consider the following statements regarding composite tools in the Mesolithic:\n1. Sickles were manufactured by hafting a row of overlapping microliths into a wooden groove.\n2. Harpoons used for fishing were made by hafting geometric trapezes as side-pointing barbs on bone shafts.\nWhich of the statements given above is/are correct?",
    "मध्यपाषाण काल में संयुक्त उपकरणों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. एक लकड़ी के खांचे में ओवरलैपिंग सूक्ष्म पाषाणों की एक पंक्ति को हत्था लगाकर हंसिया बनाया जाता था।\n2. मछली पकड़ने के लिए उपयोग किए जाने वाले हारपून हड्डी के शाफ्ट पर बगल की ओर नुकीले शूलों के रूप में समलंब (trapezes) लगाकर बनाए जाते थे।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
    2,
    "Both statements are correct, showing the complex composite designs developed for agriculture/foraging and fishing.",
    "दोनों कथन सही हैं, जो कृषि/संग्रहण और मछली पकड़ने के लिए विकसित जटिल संयुक्त डिजाइनों को दर्शाते हैं।"
)

add_stmt(sec2_en, sec2_hi,
    "Consider the following statements regarding geometric vs. non-geometric microliths:\n1. Non-geometric backed blades and scrapers preceded geometric shapes in the archaeological layers.\n2. Geometric microliths represent a higher level of standardization and hunting efficiency.\nWhich of the statements given above is/are correct?",
    "ज्यामितीय बनाम गैर-ज्यामितीय सूक्ष्म पाषाणों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. पुरातात्विक परतों में गैर-ज्यामितीय बैक्ड ब्लेड और खुरचनी ज्यामितीय आकारों से पहले आए थे।\n2. ज्यामितीय सूक्ष्म पाषाण मानकीकरण और शिकार दक्षता के उच्च स्तर का प्रतिनिधित्व करते हैं।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
    2,
    "Both statements are correct. Non-geometric types represent the early phase, while geometric shapes show advanced standardization in the late Mesolithic.",
    "दोनों कथन सही हैं। गैर-ज्यामितीय प्रकार प्रारंभिक चरण का प्रतिनिधित्व करते हैं, जबकि ज्यामितीय आकार उत्तर मध्यपाषाण काल में उन्नत मानकीकरण दिखाते हैं।"
)

# --- 9. Why (3 Questions) ---
add_open(sec2_en, sec2_hi, "Why",
    "Why was the prepared-core pressure flaking technique a major advance in stone tool manufacture?",
    "तैयार-कोर दबाव शल्कन तकनीक पत्थर के औजार निर्माण में एक प्रमुख प्रगति क्यों थी?",
    "It allowed toolmakers to extract dozens of uniform, thin, and standardized micro-blades from a single stone core. It reduced waste, maximized the utilization of precious raw materials (chert/chalcedony), and ensured that replacement blades fitted perfectly into pre-carved wooden or bone handles.",
    "इसने निर्माताओं को एक ही पत्थर के कोर से दर्जनों समान, पतले और मानकीकृत सूक्ष्म-ब्लेड निकालने की अनुमति दी। इसने कचरे को कम किया, मूल्यवान कच्चे माल (चर्ट/चाल्सीडोनी) के उपयोग को अधिकतम किया, और यह सुनिश्चित किया कि बदले जाने वाले ब्लेड पहले से बने लकड़ी या हड्डी के हैंडल में बिल्कुल फिट बैठें।"
)

add_open(sec2_en, sec2_hi, "Why",
    "Why did composite microlithic tools increase hunting efficiency compared to Paleolithic weapons?",
    "पुरापाषाणकालीन हथियारों की तुलना में संयुक्त सूक्ष्म पाषाण उपकरणों ने शिकार की दक्षता को क्यों बढ़ाया?",
    "Composite weapons like arrows and light spears were lightweight, allowing throwing/shooting from safe distances. If a stone tip broke, the hunter could quickly glue a replacement microlith into the handle rather than manufacturing a whole new tool, making the toolkit highly maintainable and fatal.",
    "तीर और हल्के भाले जैसे संयुक्त हथियार हल्के होते थे, जिससे सुरक्षित दूरी से फेंकने/मारने की अनुमति मिलती थी। यदि पत्थर की नोक टूट जाती थी, तो शिकारी पूरे नए उपकरण का निर्माण करने के बजाय हैंडल में एक नया सूक्ष्म पाषाण चिपका सकता था, जिससे उपकरण अत्यधिक उपयोगी और घातक बन गए।"
)

add_open(sec2_en, sec2_hi, "Why",
    "Why did Mesolithic knappers shift from coarse-grained quartzite to fine-grained crypto-crystalline silica?",
    "मध्यपाषाणकालीन उपकरण निर्माताओं ने मोटे क्वार्ट्जाइट के स्थान पर महीन सिलिका पत्थरों को क्यों चुना?",
    "Coarse quartzite fractures unevenly, preventing the extraction of uniform micro-blades under 5 cm. Crypto-crystalline silica (chert, chalcedony, jasper) fractures along predictable conchoidal paths, yielding razor-sharp, thin flakes that can be easily retouched into precise geometric shapes.",
    "मोटे क्वार्ट्जाइट असमान रूप से टूटते हैं, जिससे 5 सेमी से कम के समान सूक्ष्म-ब्लेड निकालना मुश्किल होता है। महीन सिलिका (चर्ट, चाल्सीडोनी, जैस्पर) अनुमानित शंखाभ रास्तों (conchoidal paths) के साथ टूटती है, जिससे तीखे, पतले शल्क प्राप्त होते हैं जिन्हें सटीक ज्यामितीय आकारों में बदलना आसान होता है।"
)

# --- 10. How (3 Questions) ---
add_open(sec2_en, sec2_hi, "How",
    "How was a composite sickle manufactured using Mesolithic microliths?",
    "मध्यपाषाणकालीन सूक्ष्म पाषाणों का उपयोग करके एक संयुक्त हंसिया (sickle) कैसे बनाया जाता था?",
    "Artisans carved a narrow groove along a curved bone or wooden shaft. They selected a series of overlapping geometric microliths (backed blades, lunates) and inserted them into the groove in a row. They then melted natural tree resin or tar, poured it into the slot, and let it cool to bind the inserts tightly.",
    "कारीगरों ने एक घुमावदार हड्डी या लकड़ी के शाफ्ट में एक संकीर्ण खांचा बनाया। उन्होंने ओवरलैपिंग ज्यामितीय सूक्ष्म पाषाणों (बैक्ड ब्लेड, चंद्राकार) की एक श्रृंखला चुनी और उन्हें एक पंक्ति में खांचे में डाल दिया। फिर उन्होंने प्राकृतिक राल या डामर को पिघलाया, उसे खांचे में डाला और ठंडा होने दिया ताकि वे मजबूती से बंध सकें।"
)

add_open(sec2_en, sec2_hi, "How",
    "How does the micro-burin technique work to section micro-blades cleanly?",
    "सूक्ष्म ब्लेडों को सफाई से विभाजित करने के लिए माइक्रो-ब्यूरिन तकनीक कैसे काम करती है?",
    "The knapper chips a small notch into the side of a micro-blade. The blade is then placed on a stone anvil, and a light tap with a hammerstone directly above the notch snaps the blade cleanly along a diagonal line, producing a geometric tool segment and a waste burin-like flake.",
    "उपकरण निर्माता एक सूक्ष्म ब्लेड के किनारे पर एक छोटा खांचा बनाता है। ब्लेड को फिर एक पत्थर की निहाई (anvil) पर रखा जाता है, और खांचे के ठीक ऊपर एक हल्के प्रहार से ब्लेड एक तिरछी रेखा के अनुदिश सफाई से टूट जाता है, जिससे एक ज्यामितीय उपकरण खंड और एक अपशिष्ट ब्यूरिन जैसा शल्क बनता है।"
)

add_open(sec2_en, sec2_hi, "How",
    "How did the invention of the bow and arrow alter human subsistence patterns in the Holocene?",
    "होलोसीन में तीर-कमान के आविष्कार ने मानव निर्वाह पैटर्न को कैसे बदल दिया?",
    "It allowed hunters to kill fast, small game (deer, boars, waterfowl) from a distance. Hunting became less dangerous, and success rates increased. It reduced dependence on trapping or direct combat, allowing families to secure animal proteins regularly and expand broad-spectrum diet options.",
    "इसने शिकारियों को दूरी से तेज, छोटे जीवों (हिरण, जंगली सूअर, जलीय पक्षी) को मारने की अनुमति दी। शिकार कम खतरनाक हो गया, और सफलता की दर बढ़ गई। इसने जाल में फंसाने या सीधे संघर्ष पर निर्भरता को कम किया, जिससे परिवारों को नियमित रूप से प्रोटीन प्राप्त करने और आहार का विस्तार करने में मदद मिली।"
)

# --- 11. Case Study (3 Questions) ---
add_open(sec2_en, sec2_hi, "Case Study",
    "Case Study: Langhnaj Microlith Assemblages.\nExplain how raw material transport distances at Langhnaj prove Mesolithic regional trade networks or mobility.",
    "मामला अध्ययन: लांघनाज सूक्ष्म पाषाण असेंब्लेज।\nस्पष्ट करें कि लांघनाज में कच्चे माल के परिवहन की दूरी कैसे मध्यपाषाणकालीन क्षेत्रीय व्यापार नेटवर्क या गतिशीलता को साबित करती है।",
    "Excavations at Langhnaj (Gujarat) revealed rich microliths made of chert and chalcedony. However, there are no natural stone outcrops near the Sabarmati sand dunes. The closest sources of chert and chalcedony are in the hills of Panchmahals or Rajasthan, over 100-150 km away. This transport proves that Langhnaj bands either engaged in long-distance seasonal migrations or established early trade networks with neighboring groups.",
    "लांघनाज (गुजरात) के उत्खनन से चर्ट और चाल्सीडोनी से बने समृद्ध सूक्ष्म पाषाण मिले हैं। हालाँकि, साबरमती रेत के टीलों के पास कोई प्राकृतिक पत्थर स्रोत नहीं हैं। चर्ट और चाल्सीडोनी के सबसे नजदीकी स्रोत पंचमहाल या राजस्थान की पहाड़ियों में हैं, जो 100-150 किमी से अधिक दूर हैं। यह परिवहन साबित करता है कि लांघनाज के समूह या तो लंबी दूरी के मौसमी प्रवास में संलग्न थे या उन्होंने पड़ोसी समूहों के साथ व्यापार संबंध स्थापित किए थे।"
)

add_open(sec2_en, sec2_hi, "Case Study",
    "Case Study: Bagor Phase I Lithic Industry.\nDescribe how the stratigraphic record of Bagor reveals the transition from pure microliths to metal integration.",
    "मामला अध्ययन: बागोर प्रथम चरण पाषाण उद्योग।\nवर्णन करें कि बागोर का स्तरविन्यासात्मक रिकॉर्ड शुद्ध सूक्ष्म पाषाण से धातु एकीकरण के संक्रमण को कैसे प्रकट करता है।",
    "Bagor Phase I (c. 5000-2800 BCE) yielded purely stone microliths alongside bones of domesticated animals. In Phase II (c. 2800-1000 BCE), microliths continue to be manufactured but are found in the same layers as copper arrowheads, spearheads, and handmade pottery. This stratigraphy proves that microliths were not abandoned immediately upon metal contact, but co-existed and adapted to early metallurgy.",
    "बागोर प्रथम चरण (लगभग 5000-2800 ईसा पूर्व) से पालतू जानवरों की हड्डियों के साथ विशुद्ध रूप से पत्थर के सूक्ष्म पाषाण मिले हैं। द्वितीय चरण (लगभग 2800-1000 ईसा पूर्व) में सूक्ष्म पाषाणों का निर्माण जारी रहा, लेकिन वे तांबे के तीरों, भालों और हस्तनिर्मित बर्तनों के साथ एक ही परतों में मिले हैं। यह स्तरविन्यास साबित करता है कि धातु के संपर्क में आने के तुरंत बाद सूक्ष्म पाषाणों को त्यागा नहीं गया था, बल्कि वे प्रारंभिक धातु विज्ञान के साथ सह-अस्तित्व में रहे।"
)

add_open(sec2_en, sec2_hi, "Case Study",
    "Case Study: Ganga Plain Microlith Raw Materials.\nExplain how the lack of local stone outcrops in the Ganga plains proves trade/migration to the Vindhyan hills.",
    "मामला अध्ययन: गंगा मैदान सूक्ष्म पाषाण कच्चा माल।\nस्पष्ट करें कि गंगा के मैदानों में स्थानीय पत्थर के स्रोतों की कमी विंध्यन पहाड़ियों की ओर व्यापार/प्रवास को कैसे साबित करती है।",
    "Sites like Sarai Nahar Rai and Mahadaha are located deep in the alluvial Ganga plains, where no stone raw materials exist. However, excavations yielded thousands of microliths made of Vindhyan chert and chalcedony. The nearest stone sources are in the Vindhyan hills (Mirzapur, Sonbhadra), 80-100 km across the Ganga River. This proves Mesolithic groups either migrated seasonally between the hills and plains or traded systematically for raw stone material.",
    "सराय नाहर राय और महदहा जैसे स्थल गंगा के जलोढ़ मैदानों में स्थित हैं, जहाँ पत्थर का कोई कच्चा माल मौजूद नहीं है। हालाँकि, उत्खनन से विंध्यन चर्ट और चाल्सीडोनी से बने हजारों सूक्ष्म पाषाण मिले हैं। निकटतम पत्थर के स्रोत गंगा नदी के उस पार विंध्यन पहाड़ियों (मिर्जापुर, सोनभद्र) में हैं, जो 80-100 किमी दूर हैं। यह साबित करता है कि मध्यपाषाणकालीन समूह या तो पहाड़ियों और मैदानों के बीच मौसमी प्रवास करते थे या व्यवस्थित रूप से कच्चे पत्थर का व्यापार करते थे।"
)

# --- 12. Teach the Concept (3 Questions) ---
add_open(sec2_en, sec2_hi, "Teach the Concept",
    "Teach the Concept: Explain the difference between geometric and non-geometric microliths to a beginner.",
    "अवधारणा समझाएं: एक नौसिखिए को ज्यामितीय और गैर-ज्यामितीय सूक्ष्म पाषाणों के बीच का अंतर समझाएं।",
    "Think of non-geometric microliths as simple miniature knives—they are small, straight blades backed on one side to protect your finger when cutting. In contrast, geometric microliths are highly standardized shapes like triangles, crescents (lunates), and trapezoids. They were not held by hand; they were designed like puzzle pieces to fit flush into slots of wooden/bone arrows or harpoons, creating advanced composite weapons.",
    "गैर-ज्यामितीय सूक्ष्म पाषाणों को साधारण लघु चाकू के रूप में सोचें — वे छोटे, सीधे ब्लेड होते हैं जिनके एक तरफ घिसाई की जाती है ताकि काटते समय आपकी उंगली सुरक्षित रहे। इसके विपरीत, ज्यामितीय सूक्ष्म पाषाण त्रिकोण, चंद्राकार (lunates) और समलंब जैसे अत्यधिक मानकीकृत आकार हैं। इन्हें हाथ से नहीं पकड़ा जाता था; इन्हें पहेली के टुकड़ों की तरह डिजाइन किया गया था ताकि वे लकड़ी/हड्डी के तीरों या हारपून के खांचों में फिट बैठें।"
)

add_open(sec2_en, sec2_hi, "Teach the Concept",
    "Teach the Concept: Explain the process of 'Hafting' using a modern utility knife (like a box cutter) as an analogy.",
    "अवधारणा समझाएं: सादृश्य के रूप में एक आधुनिक उपयोगिता चाकू (जैसे बॉक्स कटर) का उपयोग करके 'हत्था लगाने' (Hafting) की प्रक्रिया को समझाएं।",
    "Imagine a modern box cutter: you have a plastic or metal handle, and you slide in a tiny, sharp steel blade. If the blade gets blunt, you pop it out and put a new one in. Prehistoric hafting worked the same way. The handle was carved out of wood or bone, and the 'blade' was a row of tiny stone microliths glued into a groove. Instead of throwing away a precious carved handle, hunters just replaced the tiny stone tips when they broke.",
    "एक आधुनिक बॉक्स कटर की कल्पना करें: आपके पास एक प्लास्टिक या धातु का हैंडल होता है, और आप उसमें एक छोटा, तेज स्टील का ब्लेड डालते हैं। यदि ब्लेड कुंद हो जाता है, तो आप उसे बाहर निकालते हैं और एक नया ब्लेड लगा देते हैं। प्रागैतिहासिक हत्था लगाने का काम भी इसी तरह होता था। हैंडल लकड़ी या हड्डी से बनाया जाता था, और 'ब्लेड' एक खांचे में चिपकाए गए छोटे सूक्ष्म पाषाणों की एक पंक्ति होती थी। पूरे हैंडल को फेंकने के बजाय, वे बस टूटे हुए छोटे पत्थर बदल देते थे।"
)

add_open(sec2_en, sec2_hi, "Teach the Concept",
    "Teach the Concept: Explain the micro-burin technique using the analogy of scoring and snapping glass.",
    "अवधारणा समझाएं: कांच को खरोंचने और तोड़ने (scoring and snapping) के सादृश्य का उपयोग करके माइक्रो-ब्यूरिन तकनीक को समझाएं।",
    "To cut a sheet of glass cleanly, a glazier doesn't smash it with a hammer. Instead, they make a thin scratch (score) along a line and apply gentle pressure to snap it cleanly. The micro-burin technique works the same way: a stone knapper chips a small notch into a blade, creating a weak point. When they strike the blade near the notch, it snaps perfectly along a straight diagonal line, creating a clean geometric stone point.",
    "कांच की एक शीट को साफ से काटने के लिए, एक कारीगर उस पर हथौड़े से वार नहीं करता। इसके बजाय, वे एक रेखा के अनुदिश एक पतली खरोंच (score) बनाते हैं और उसे साफ से तोड़ने के लिए हल्का दबाव डालते हैं। माइक्रो-ब्यूरिन तकनीक भी इसी तरह काम करती है: एक कारीगर ब्लेड में एक छोटा खांचा बनाता है, जिससे एक कमजोर बिंदु बनता है। जब वे खांचे के पास वार करते हैं, तो यह एक सीधी तिरछी रेखा के अनुदिश टूट जाता है, जिससे साफ ज्यामितीय पत्थर की नोक बनती है।"
)
