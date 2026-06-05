from .helpers import add_mcq, add_multi_mcq, add_tf, add_blank, add_match, add_oneliner, add_ar, add_stmt, add_open

sec5_en = []
sec5_hi = []

# --- 1. MCQ (5 Questions) ---
add_mcq(sec5_en, sec5_hi,
    "The Upper Paleolithic site of Baghor I in the Son Valley (Madhya Pradesh) is famous for yielding which unique symbolic structure?",
    "सोन घाटी (मध्य प्रदेश) में स्थित उच्च पुरापाषाणकालीन स्थल बाघोर I किस अद्वितीय प्रतीकात्मक संरचना को प्रदान करने के लिए प्रसिद्ध है?",
    ["A stone platform with a triangular laminated sandstone representing a shrine", "A circular stone burial mound containing iron weapons", "A massive rock temple carved into the sandstone cliff", "A wooden totem pole depicting animal spirits"],
    ["एक पत्थर का चबूतरा जिस पर एक त्रिकोणीय स्तरित बलुआ पत्थर है जो एक मंदिर का प्रतिनिधित्व करता है", "एक विशाल पत्थर का मकबरा जिसमें लोहे के हथियार हैं", "बलुआ पत्थर की चट्टान में खुदा हुआ एक विशाल चट्टानी मंदिर", "पशु आत्माओं को दर्शाने वाला एक लकड़ी का कुलचिह्न (totem pole)"],
    0,
    "Baghor I, excavated by Kenoyer, Clark, Sharma, and Pappu, revealed a rubble-built stone platform with a natural triangular laminated sandstone at its center, interpreted as the earliest known Mother Goddess shrine in India.",
    "केनॉयर, क्लार्क, शर्मा और पप्पू द्वारा उत्खनित बाघोर I से एक पत्थर का चबूतरा मिला जिसके केंद्र में एक प्राकृतिक त्रिकोणीय स्तरित बलुआ पत्थर था, जिसे भारत में सबसे पुराना ज्ञात मातृ देवी मंदिर माना गया है।"
)

add_mcq(sec5_en, sec5_hi,
    "The famous rock shelters of Bhimbetka, which house a massive collection of prehistoric cave paintings, were discovered by V.S. Wakankar in which year?",
    "भीमबेटका के प्रसिद्ध रॉक शेल्टर, जिनमें प्रागैतिहासिक गुफा चित्रों का एक विशाल संग्रह है, की खोज वी.एस. वाकणकर ने किस वर्ष की थी?",
    ["1957", "1963", "1863", "1982"],
    ["1957", "1963", "1863", "1982"],
    0,
    "Dr. V.S. Wakankar discovered the Bhimbetka rock shelters in 1957 while travelling by train to Itarsi and noticing the unique Vindhyan sandstone formations.",
    "डॉ. वी.एस. वाकणकर ने 1957 में इटारसी की रेल यात्रा के दौरान विंध्य बलुआ पत्थर की अनूठी संरचनाओं को देखकर भीमबेटका रॉक शेल्टर की खोज की थी।"
)

add_mcq(sec5_en, sec5_hi,
    "What is the oldest pigment color layer identified in the rock paintings of Bhimbetka, representing the Upper Paleolithic phase?",
    "भीमबेटका के रॉक चित्रों में पहचानी गई सबसे पुरानी वर्णक (pigment) रंग की परत कौन सी है, जो उच्च पुरापाषाण चरण का प्रतिनिधित्व करती है?",
    ["Green, depicting dynamic dancing and hunting figures", "Red, depicting humped bulls and agricultural scenes", "White, depicting horse riders and shields", "Yellow, depicting metal smelting ovens"],
    ["हरा रंग, जो गतिशील नृत्य और शिकार के दृश्यों को दर्शाता है", "लाल रंग, जो कूबड़ वाले बैल और कृषि दृश्यों को दर्शाता है", "सफेद रंग, जो घुड़सवारों और ढालों को दर्शाता है", "पीला रंग, जो धातु पिघलाने वाली भट्टियों को दर्शाता है"],
    0,
    "The earliest paintings at Bhimbetka are green figures made of green chalcedony/chlorite, depicting dynamic stick-like human dancing figures and large animal silhouettes.",
    "भीमबेटका में सबसे पुराने चित्र हरे रंग के हैं जो हरी चाल्सीडोनी/क्लोराइट से बने हैं, जिनमें गतिशील छड़ी जैसे मानव नृत्य के दृश्य और बड़े जानवरों की रूपरेखा दर्शाई गई है।"
)

add_mcq(sec5_en, sec5_hi,
    "Decorated ostrich eggshell fragments with cross-hatched geometric engravings, dated to the late Pleistocene, were first discovered in India at which site?",
    "लेट प्लीस्टोसीन काल के जालीदार ज्यामितीय नक्काशी वाले अलंकृत शुतुरमुर्ग के अंडे के छिलके के टुकड़े भारत में पहली बार किस स्थल पर खोजे गए थे?",
    ["Patne in Maharashtra", "Bhimbetka in Madhya Pradesh", "Chandresal in Rajasthan", "Renigunta in Andhra Pradesh"],
    ["महाराष्ट्र में पाटणे", "मध्य प्रदेश में भीमबेटका", "राजस्थान में चंद्रसाल", "आंध्र प्रदेश में रेनिगुंटा"],
    0,
    "S.A. Sali discovered the first decorated ostrich eggshells in the Upper Paleolithic layers of Patne, Maharashtra, dating back to c. 25,000 BCE.",
    "एस.ए. साली ने महाराष्ट्र के पाटणे के उच्च पुरापाषाणकालीन परतों में लगभग 25,000 ईसा पूर्व के पहले अलंकृत शुतुरमुर्ग के अंडे के छिलके खोजे थे।"
)

add_mcq(sec5_en, sec5_hi,
    "How did Upper Paleolithic artists prepare durable mineral paints to ensure their drawings survived on cave walls for thousands of years?",
    "उच्च पुरापाषाणकालीन कलाकारों ने टिकाऊ खनिज पेंट कैसे तैयार किए ताकि यह सुनिश्चित हो सके कि उनके चित्र हजारों वर्षों तक गुफाओं की दीवारों पर टिके रहें?",
    ["By grinding mineral oxides and mixing them with organic binders like plant sap or fat", "By boiling coal tar and mixing it with river water", "By importing readymade vegetable dyes from Mesopotamia", "By using natural volcanic lava directly from active eruptions"],
    ["खनिज ऑक्साइडों को पीसकर और उन्हें पौधों के रस या चर्बी जैसे कार्बनिक बाइंडरों के साथ मिलाकर", "कोलतार को उबालकर और उसे नदी के पानी में मिलाकर", "मेसोपोटामिया से आयातित प्राकृतिक वनस्पति रंजक का उपयोग करके", "सक्रिय ज्वालामुखी विस्फोटों से सीधे प्राकृतिक लावा का उपयोग करके"],
    0,
    "Artists ground minerals like hematite (red) and chlorite (green) into powder, mixing them with animal fat, bone marrow, or plant sap, which chemically bonded with the silica in cave sandstone.",
    "कलाकारों ने हेमेटाइट (लाल) और क्लोराइट (हरे) जैसे खनिजों को पीसकर पाउडर बनाया, उन्हें जानवरों की चर्बी, हड्डी की मज्जा या पौधों के रस के साथ मिलाया, जिसने गुफा बलुआ पत्थर में सिलिका के साथ रासायनिक रूप से संबंध बनाया।"
)

# --- 2. Multiple Correct MCQ (5 Questions) ---
add_multi_mcq(sec5_en, sec5_hi,
    "Which of the following elements characterize the prehistoric rock art at Bhimbetka? (Select all that apply)",
    "निम्नलिखित में से कौन से तत्व भीमबेटका की प्रागैतिहासिक शैल कला की विशेषताएं हैं? (सभी सही विकल्प चुनें)",
    ["Use of natural mineral pigments like hematite and chlorite", "Depiction of dynamic human dancing figures in stick form", "Superposition of multiple layers of paintings spanning different eras", "Exquisite representations of metal weapons and chariots"],
    ["हेमेटाइट और क्लोराइट जैसे प्राकृतिक खनिज रंगों का उपयोग", "छड़ी के आकार में गतिशील मानव नृत्य के दृश्यों का चित्रण", "विभिन्न युगों के चित्रों की कई परतों का सुपरपोजिशन", "धातु के हथियारों और रथों का उत्कृष्ट चित्रण"],
    [0, 1, 2],
    "Bhimbetka art uses mineral pigments, shows stick-figure dancers, and has stratified layers. Chariots and metal weapons are historical/Bronze Age depictions, not part of the early Paleolithic paintings.",
    "भीमबेटका कला खनिज रंगों का उपयोग करती है, नृत्य दृश्यों को दर्शाती है और इसमें स्तरबद्ध परतें मिलती हैं। रथ और धातु के हथियार ऐतिहासिक/कांस्य युग के चित्रण हैं, न कि प्रारंभिक पुरापाषाण चित्र।"
)

add_multi_mcq(sec5_en, sec5_hi,
    "Which of the following details support the interpretation of the Baghor I stone platform as a prehistoric shrine? (Select all that apply)",
    "निम्नलिखित में से कौन से विवरण बाघोर I के पत्थर के चबूतरे को एक प्रागैतिहासिक मंदिर के रूप में मानने का समर्थन करते हैं? (सभी सही विकल्प चुनें)",
    ["A triangular laminated sandstone placed at the center of the platform", "The stone was sourced from the nearby Kaimur hills, selected for its natural aesthetic beauty", "Local tribal communities (Kols and Gonds) still worship similar triangular stones as 'Mai' in the region", "The presence of a written Sanskrit inscription on the stone platform"],
    ["चबूतरे के केंद्र में रखा गया एक त्रिकोणीय स्तरित बलुआ पत्थर", "यह पत्थर पास की कैमूर पहाड़ियों से लाया गया था, जिसे इसकी प्राकृतिक सुंदरता के कारण चुना गया था", "स्थानीय आदिवासी समुदाय (कोल और गोंड) आज भी इसी क्षेत्र में त्रिकोणीय पत्थरों की पूजा 'माई' के रूप में करते हैं", "पत्थर के चबूतरे पर संस्कृत में लिखे गए शिलालेख की उपस्थिति"],
    [0, 1, 2],
    "The Baghor I shrine is interpreted via ethnographic analogy (Kols and Gonds worshipping 'Mai') and its unique geological placement of laminated sandstone. Written scripts did not exist in the Paleolithic.",
    "बाघोर I मंदिर की व्याख्या नृवंशविज्ञान सादृश्य (कोल और गोंड आदिवासियों द्वारा 'माई' की पूजा) और इसके स्तरित बलुआ पत्थर के अद्वितीय स्थान से की जाती है। पुरापाषाण काल में लिखित भाषाएँ नहीं थीं।"
)

add_multi_mcq(sec5_en, sec5_hi,
    "Which of the following sites in India have yielded fragments of Upper Paleolithic ostrich eggshells? (Select all that apply)",
    "भारत में निम्नलिखित में से किन स्थलों से उच्च पुरापाषाणकालीन शुतुरमुर्ग के अंडे के छिलके प्राप्त हुए हैं? (सभी सही विकल्प चुनें)",
    ["Patne in Maharashtra", "Chandresal in Rajasthan", "Bhimbetka in Madhya Pradesh", "Harappa in Punjab"],
    ["महाराष्ट्र में पाटणे", "राजस्थान में चंद्रसाल", "मध्य प्रदेश में भीमबेटका", "पंजाब में हड़प्पा"],
    [0, 1, 2],
    "Ostrich eggshells have been found at Patne, Chandresal, Bhimbetka, and Ramnagar. Harappa is a Bronze Age site and lacks Upper Paleolithic deposits.",
    "शुतुरमुर्ग के अंडों के छिलके पाटणे, चंद्रसाल, भीमबेटका और रामनगर से मिले हैं। हड़प्पा एक कांस्य युग का स्थल है और वहाँ उच्च पुरापाषाणकालीन जमाव नहीं हैं।"
)

add_multi_mcq(sec5_en, sec5_hi,
    "What technologies and methods were utilized by Upper Paleolithic humans to manufacture beads? (Select all that apply)",
    "उच्च पुरापाषाणकालीन मनुष्यों द्वारा मनके (beads) बनाने के लिए किन तकनीकों और विधियों का उपयोग किया गया था? (सभी सही विकल्प चुनें)",
    ["Drilling a central hole in shell blanks using tiny chert borers", "Grinding the outer edges smooth on grooved sandstone slabs", "Melting the shell fragments and casting them in clay molds", "Threading completed beads on sinew or plant fibers"],
    ["छोटे चर्ट वेधकों (borers) का उपयोग करके शेल ब्लैंक के केंद्र में छेद करना", "नालीदार बलुआ पत्थर के स्लैब पर बाहरी किनारों को घिसकर चिकना करना", "शेल के टुकड़ों को पिघलाकर मिट्टी के सांचों में ढालना", "तैयार मनकों को तांत या पौधों के रेशों में पिरोना"],
    [0, 1, 3],
    "Beads were manufactured by drilling holes, grinding edges, and threading. Melting shells is chemically impossible and was not a prehistoric technology.",
    "मनकों का निर्माण छिद्र करके, किनारों को घिसकर और पिरोकर किया जाता था। शेल को पिघलाना रासायनिक रूप से असंभव है और यह कोई प्रागैतिहासिक तकनीक नहीं थी।"
)

add_multi_mcq(sec5_en, sec5_hi,
    "Which of the following features are characteristic of the Upper Paleolithic art style at Bhimbetka? (Select all that apply)",
    "भीमबेटका में उच्च पुरापाषाण कला शैली की निम्नलिखित में से कौन सी विशेषताएं हैं? (सभी सही विकल्प चुनें)",
    ["Large, life-size linear outlines of wild animals", "Stick-like dynamic human figures executing dancing postures", "Depictions of heavy carts with spokes and wheels", "Total absence of domestic animals or pastoral scenes"],
    ["जंगली जानवरों की बड़ी, आदमकद रेखाकृतियाँ (outlines)", "नृत्य मुद्राओं में गतिशील छड़ी जैसे मानव चित्र", "प्रवक्ता (spokes) और पहियों वाली भारी गाड़ियों का चित्रण", "पालतू जानवरों या देहाती (pastoral) दृश्यों का पूर्ण अभाव"],
    [0, 1, 3],
    "Upper Paleolithic Bhimbetka art features large linear animal profiles, stick dancers, and contains no domestic animals. Carts with spokes and wheels belong to Chalcolithic and historic phases.",
    "उच्च पुरापाषाण भीमबेटका कला की विशेषताओं में बड़ी जानवरों की आकृतियाँ, छड़ी जैसे नर्तक शामिल हैं और इसमें पालतू जानवरों का अभाव है। पहियों और पहिए की तीलियों वाली गाड़ियां ताम्रपाषाण और ऐतिहासिक चरणों की हैं।"
)

# --- 3. True/False (8 Questions) ---
add_tf(sec5_en, sec5_hi,
    "Is it true that the triangular laminated stone at the Baghor I shrine was hand-carved into a triangle shape by Paleolithic hominins?",
    "क्या यह सच है कि बाघोर I मंदिर में त्रिकोणीय स्तरित पत्थर को पुरापाषाणकालीन होमिनिन द्वारा हाथ से त्रिकोण आकार में तराशा गया था?",
    False,
    "False. Hominins did not carve the stone; it was a natural geological piece weathered into a triangle by wind and water, selected and brought to the shrine because of its unique natural shape.",
    "गलत। होमिनिन ने पत्थर को नहीं तराशा था; यह एक प्राकृतिक भूवैज्ञानिक टुकड़ा था जो हवा और पानी से घिसकर त्रिकोण बन गया था, जिसे इसके अनोखे प्राकृतिक आकार के कारण चुनकर मंदिर में लाया गया था।"
)

add_tf(sec5_en, sec5_hi,
    "V.S. Wakankar discovered the Bhimbetka rock shelters while systematically studying geological maps and searching for limestone formations.",
    "वी.एस. वाकणकर ने भीमबेटका रॉक शेल्टर की खोज तब की थी जब वे व्यवस्थित रूप से भूवैज्ञानिक मानचित्रों का अध्ययन कर रहे थे और चूना पत्थर की चट्टानों की तलाश कर रहे थे।",
    False,
    "False. He noticed the sandstone rock outcrops from a train window while traveling, which prompted him to disembark and explore the forest nearby, leading to the discovery in 1957.",
    "गलत। उन्होंने यात्रा के दौरान ट्रेन की खिड़की से बलुआ पत्थर की चट्टानें देखी थीं, जिससे प्रेरित होकर वे उतरे और पास के जंगल की खोज की, जिसके परिणामस्वरूप 1957 में यह खोज हुई।"
)

add_tf(sec5_en, sec5_hi,
    "Ostrich eggshell fragments in India have been radiocarbon-dated to the late Pleistocene epoch, around 25,000 BCE.",
    "भारत में शुतुरमुर्ग के अंडे के छिलके के टुकड़ों का समय रेडियोकार्बन-निर्धारण से लेट प्लीस्टोसीन युग, लगभग 25,000 ईसा पूर्व का आंका गया है।",
    True,
    "True. Radiocarbon dating of ostrich shell fragments at Patne and Chandresal yielded ages clustered around 25,000 to 39,000 years ago.",
    "सत्य। पाटणे और चंद्रसाल में शुतुरमुर्ग के अंडे के छिलकों के रेडियोकार्बन काल-निर्धारण से पता चला कि इनकी आयु लगभग 25,000 से 39,000 वर्ष पुरानी है।"
)

add_tf(sec5_en, sec5_hi,
    "The green paintings at Bhimbetka are younger and sit on top of the red and white historic painting layers.",
    "भीमबेटका में हरे रंग के चित्र अपेक्षाकृत नए हैं और वे लाल व सफेद ऐतिहासिक चित्रों की परतों के ऊपर बने हुए हैं।",
    False,
    "False. The green paintings are the oldest layer, found at the very bottom (superposition), overlain by Mesolithic red and historical white/yellow layers.",
    "गलत। हरे रंग के चित्र सबसे पुरानी परत हैं, जो सबसे नीचे पाए जाते हैं (superposition), जिनके ऊपर मध्यपाषाणकालीन लाल और ऐतिहासिक सफेद/पीली परतें बनी हैं।"
)

add_tf(sec5_en, sec5_hi,
    "Chlorite minerals ground with water and organic sap produced the green pigment used in Upper Paleolithic rock art.",
    "पानी और जैविक रस के साथ पीसे गए क्लोराइट खनिजों ने हरे रंग का उत्पादन किया जिसका उपयोग उच्च पुरापाषाणकालीन शैल कला में किया गया था।",
    True,
    "True. Green chlorite or green chalcedony was pulverized and mixed with binders to create the green paint used for the earliest dancing stick figures.",
    "सत्य। हरी क्लोराइट या हरी चाल्सीडोनी को पीसकर पाउडर बनाया जाता था और बाइंडरों के साथ मिलाकर नृत्य आकृतियों के लिए हरे रंग का निर्माण किया जाता था।"
)

add_tf(sec5_en, sec5_hi,
    "The local Gond and Kol tribes in the Son Valley worship a triangular stone called 'Mai' (Mother Goddess) today, mirroring the prehistoric Baghor I assembly.",
    "सोन घाटी में स्थानीय गोंड और कोल जनजातियां आज भी 'माई' (मातृ देवी) नामक एक त्रिकोणीय पत्थर की पूजा करती हैं, जो प्रागैतिहासिक बाघोर I असेंबली के समान है।",
    True,
    "True. This ethnographic parallel helped archaeologists interpret the Baghor I platform as a prehistoric Mother Goddess shrine.",
    "सत्य। इस नृवंशविज्ञान समानांतर (ethnographic parallel) ने पुरातत्वविदों को बाघोर I चबूतरे को एक प्रागैतिहासिक मातृ देवी मंदिर के रूप में मानने में मदद की।"
)

add_tf(sec5_en, sec5_hi,
    "Geometric cross-hatched patterns engraved on ostrich eggshells are proof of early abstract cognitive planning and symbolic behavior.",
    "शुतुरमुर्ग के अंडे के छिलके पर उकेरे गए ज्यामितीय जालीदार पैटर्न (cross-hatched patterns) शुरुआती अमूर्त संज्ञानात्मक योजना और प्रतीकात्मक व्यवहार का प्रमाण हैं।",
    True,
    "True. Non-representational geometric engravings show that humans were beginning to express abstract mental concepts through material culture.",
    "सत्य। गैर-प्रतिनिधित्ववादी ज्यामितीय नक्काशी दर्शाती है कि मनुष्य भौतिक संस्कृति के माध्यम से अमूर्त मानसिक विचारों को व्यक्त करने लगे थे।"
)

add_tf(sec5_en, sec5_hi,
    "Upper Paleolithic humans used polished iron needles to engrave drawings onto the hard surfaces of ostrich eggshells.",
    "उच्च पुरापाषाणकालीन मनुष्यों ने शुतुरमुर्ग के अंडे के छिलके की कठोर सतहों पर नक्काशी करने के लिए पॉलिश की हुई लोहे की सुइयों का उपयोग किया था।",
    False,
    "False. Iron was completely unknown in the Paleolithic; engravings were done using sharp micro-burins or flint points made of chert.",
    "गलत। पुरापाषाण काल में लोहा पूरी तरह से अज्ञात था; नक्काशी तीखे चर्ट माइक्रो-ब्यूरिन या फ्लिंट पॉइंट द्वारा की जाती थी।"
)

# --- 4. Fill in the Blank (8 Questions) ---
add_blank(sec5_en, sec5_hi,
    "The archaeologist who discovered the Bhimbetka rock shelters in 1957 was ________.",
    "1957 में भीमबेटका रॉक शेल्टर की खोज करने वाले पुरातत्वविद ________ थे।",
    "V.S. Wakankar", "वी.एस. वाकणकर",
    "Dr. Vishnu Shridhar Wakankar discovered the site and spent years documenting its paintings.",
    "डॉ. विष्णु श्रीधर वाकणकर ने इस स्थल की खोज की और इसके चित्रों का दस्तावेजीकरण करने में वर्ष बिताए।"
)

add_blank(sec5_en, sec5_hi,
    "The prehistoric shrine containing the triangular sandstone was excavated at ________ I in Son Valley.",
    "त्रिकोणीय बलुआ पत्थर वाला प्रागैतिहासिक मंदिर सोन घाटी में ________ I में खोदा गया था।",
    "Baghor", "बाघोर",
    "Baghor I is a key Upper Paleolithic site in Madhya Pradesh.",
    "बाघोर I मध्य प्रदेश का एक महत्वपूर्ण उच्च पुरापाषाणकालीन स्थल है।"
)

add_blank(sec5_en, sec5_hi,
    "The oldest paintings at Bhimbetka, showing stick dancers, are colored ________.",
    "भीमबेटका में सबसे पुराने चित्र, जिनमें छड़ी जैसे नर्तक दिखाए गए हैं, ________ रंग के हैं।",
    "green", "हरे",
    "Green paintings made from chlorite represent the earliest Upper Paleolithic artistic layer.",
    "क्लोराइट से बने हरे चित्र सबसे पुराने उच्च पुरापाषाणकालीन कलात्मक चरण का प्रतिनिधित्व करते हैं।"
)

add_blank(sec5_en, sec5_hi,
    "Ostrich eggshells with cross-hatched engravings were first discovered in the Upper Paleolithic layers of ________, Maharashtra.",
    "जालीदार नक्काशी वाले शुतुरमुर्ग के अंडे के छिलके सबसे पहले महाराष्ट्र के ________ के उच्च पुरापाषाणकालीन परतों में खोजे गए थे।",
    "Patne", "पाटणे",
    "Patne, excavated by S.A. Sali, yielded the first engraved ostrich shell fragments in India.",
    "एस.ए. साली द्वारा उत्खनित पाटणे से भारत में पहले नक्काशीदार शुतुरमुर्ग के अंडे के छिलके मिले थे।"
)

add_blank(sec5_en, sec5_hi,
    "The red paint used in Bhimbetka cave paintings was made from the mineral ________.",
    "भीमबेटका गुफा चित्रों में प्रयुक्त लाल रंग ________ खनिज से बनाया गया था।",
    "hematite", "हेमेटाइट",
    "Hematite (iron oxide, local geru) was ground and mixed with animal fat to produce red paint.",
    "हेमेटाइट (आयरन ऑक्साइड, स्थानीय गेरू) को पीसकर और जानवरों की चर्बी के साथ मिलाकर लाल रंग तैयार किया जाता था।"
)

add_blank(sec5_en, sec5_hi,
    "The triangular stone at the Baghor shrine is made of ________, containing concentric colored bands.",
    "बाघोर मंदिर का त्रिकोणीय पत्थर ________ का बना है, जिसमें संकेंद्रित रंगीन धारियां हैं।",
    "sandstone", "बलुआ पत्थर",
    "It is a natural, ferruginous laminated sandstone fragment showing concentric rings.",
    "यह एक प्राकृतिक, आयरन युक्त स्तरित बलुआ पत्थर (ferruginous laminated sandstone) का टुकड़ा है जिसमें संकेंद्रित छल्ले हैं।"
)

add_blank(sec5_en, sec5_hi,
    "Bhimbetka is located in the ________ district of Madhya Pradesh.",
    "भीमबेटका मध्य प्रदेश के ________ जिले में स्थित है।",
    "Raisen", "रायसेन",
    "Bhimbetka is located in Raisen district, in the Vindhyan mountain range.",
    "भीमबेटका विंध्याचल पर्वत श्रृंखला में, रायसेन जिले में स्थित है।"
)

add_blank(sec5_en, sec5_hi,
    "Archaeologists use ________ analogy to explain prehistoric symbols by comparing them with modern tribal traditions.",
    "पुरातत्वविद प्रागैतिहासिक प्रतीकों की व्याख्या करने के लिए आधुनिक जनजातीय परंपराओं के साथ उनकी तुलना करके ________ सादृश्य का उपयोग करते हैं।",
    "ethnographic", "नृवंशविज्ञान",
    "Ethnographic analogy compares archaeological remains with living societies, like comparing Baghor shrine with Kol rituals.",
    "नृवंशविज्ञान सादृश्य (ethnographic analogy) पुरातात्विक अवशेषों की तुलना जीवित समाजों से करता है, जैसे बाघोर मंदिर की तुलना कोल अनुष्ठानों से करना।"
)

# --- 5. Match the Following (3 Questions) ---
add_match(sec5_en, sec5_hi,
    "Match the archaeological site with its diagnostic symbolic discovery:",
    "पुरातात्विक स्थल को उसकी विशिष्ट प्रतीकात्मक खोज से सुमेलित करें:",
    ["1. Baghor I", "2. Patne", "3. Bhimbetka"],
    ["1. बाघोर I", "2. पाटणे", "3. भीमबेटका"],
    ["A. Ostrich eggshell beads and geometric engravings", "B. Rubble-built platform with a triangular sandstone", "C. Green stick-figure dancing cave paintings"],
    ["A. शुतुरमुर्ग के अंडे के छिलके के मनके और ज्यामितीय नक्काशी", "B. एक त्रिकोणीय बलुआ पत्थर के साथ मलबे से बना चबूतरा", "C. हरे रंग के छड़ी जैसे नृत्य करने वाले गुफा चित्र"],
    "1-B, 2-A, 3-C", "1-B, 2-A, 3-C"
)

add_match(sec5_en, sec5_hi,
    "Match the color pigment with its mineral source:",
    "रंग पिगमेंट को उसके खनिज स्रोत से सुमेलित करें:",
    ["1. Red paint", "2. Green paint", "3. Dark Black paint"],
    ["1. लाल पेंट", "2. हरा पेंट", "3. गहरा काला पेंट"],
    ["A. Chlorite or green chalcedony", "B. Manganese oxides or charcoal", "C. Hematite or iron oxide (geru)"],
    ["A. क्लोराइट या हरी चाल्सीडोनी", "B. मैंगनीज ऑक्साइड या चारकोल", "C. हेमेटाइट या आयरन ऑक्साइड (गेरू)"],
    "1-C, 2-A, 3-B", "1-C, 2-A, 3-B"
)

add_match(sec5_en, sec5_hi,
    "Match the scholar with their specific contribution to Paleolithic art studies:",
    "विद्वान को पुरापाषाण कला अध्ययनों में उनके विशिष्ट योगदान से सुमेलित करें:",
    ["1. V.S. Wakankar", "2. S.A. Sali", "3. J.M. Kenoyer"],
    ["1. वी.एस. वाकणकर", "2. एस.ए. साली", "3. जे.एम. केनॉर्क"],
    ["A. Excavated and published Baghor I shrine details", "B. Excavated Patne ostrich shell beads", "C. Discovered and documented Bhimbetka rock shelters"],
    ["A. बाघोर I मंदिर के विवरण का उत्खनन और प्रकाशन किया", "B. पाटणे के शुतुरमुर्ग शेल मनकों का उत्खनन किया", "C. भीमबेटका रॉक शेल्टरों की खोज और दस्तावेजीकरण किया"],
    "1-C, 2-B, 3-A", "1-C, 2-B, 3-A"
)

# --- 6. One-Liner (8 Questions) ---
add_oneliner(sec5_en, sec5_hi,
    "What is the oldest known rock art site in India?",
    "भारत में सबसे पुराना ज्ञात शैल कला (rock art) स्थल कौन सा है?",
    "Bhimbetka in Madhya Pradesh, containing Upper Paleolithic paintings.",
    "मध्य प्रदेश में भीमबेटका, जिसमें उच्च पुरापाषाणकालीन चित्र मिलते हैं।"
)

add_oneliner(sec5_en, sec5_hi,
    "What does a 'rubble-built platform' refer to in the context of Baghor I?",
    "बाघोर I के संदर्भ में 'मलबे से बने चबूतरे' (rubble-built platform) से क्या तात्पर्य है?",
    "A low platform built by arranging sandstone rubble rocks, creating a circular altar for the triangular stone.",
    "बलुआ पत्थर के मलबे के पत्थरों को व्यवस्थित करके बनाया गया एक छोटा चबूतरा, जो त्रिकोणीय पत्थर के लिए एक वेदी बनाता है।"
)

add_oneliner(sec5_en, sec5_hi,
    "State the significance of the green chalcedony stick figures at Bhimbetka.",
    "भीमबेटका में हरी चाल्सीडोनी से बनी छड़ी जैसी आकृतियों का महत्व बताएं।",
    "They represent the oldest layer of rock art in India, dating to the Upper Paleolithic, depicting group dancing and hunting.",
    "वे भारत में शैल कला की सबसे पुरानी परत का प्रतिनिधित्व करते हैं, जो उच्च पुरापाषाण काल की है और सामूहिक नृत्य व शिकार को दर्शाती है।"
)

add_oneliner(sec5_en, sec5_hi,
    "What is the primary function of a chert 'micro-borer' in bead manufacturing?",
    "मनका निर्माण में चर्ट 'माइक्रो-वेधक' (micro-borer) का प्राथमिक कार्य क्या है?",
    "A small pointed stone tool used to drill clean central holes in ostrich eggshell blanks.",
    "एक छोटा नुकीला पत्थर का उपकरण जिसका उपयोग शुतुरमुर्ग के अंडे के छिलके के ब्लैंक्स में साफ केंद्रीय छेद करने के लिए किया जाता था।"
)

add_oneliner(sec5_en, sec5_hi,
    "How does the law of superposition help date cave paintings?",
    "सुपरपोजिशन का नियम गुफा चित्रों के काल-निर्धारण में कैसे मदद करता है?",
    "By analyzing which layers of paint sit on top of others, allowing relative chronology (older paintings are beneath newer ones).",
    "यह विश्लेषण करके कि पेंट की कौन सी परतें दूसरों के ऊपर हैं, जिससे सापेक्ष कालक्रम का पता चलता है (पुराने चित्र नए चित्रों के नीचे होते हैं)।"
)

add_oneliner(sec5_en, sec5_hi,
    "State the geographic source of the Baghor I triangular laminated stone.",
    "बाघोर I के त्रिकोणीय स्तरित पत्थर के भौगोलिक स्रोत का उल्लेख करें।",
    "It was sourced from the Kaimur range sandstone beds, located c. 3 km away from the Baghor site.",
    "यह बाघोर स्थल से लगभग 3 किमी दूर स्थित कैमूर श्रृंखला के बलुआ पत्थर के बिस्तरों से लाया गया था।"
)

add_oneliner(sec5_en, sec5_hi,
    "Explain the term 'concentric laminations' on the Baghor triangular stone.",
    "बाघोर त्रिकोणीय पत्थर पर 'संकेंद्रित स्तरण' (concentric laminations) शब्द की व्याख्या करें।",
    "Natural concentric rings of yellow, red, and brown iron-rich bands created by geological layering in sandstone.",
    "बलुआ पत्थर में भूवैज्ञानिक परतों द्वारा निर्मित पीले, लाल और भूरे रंग के लौह-समृद्ध बैंड के प्राकृतिक संकेंद्रित छल्ले।"
)

add_oneliner(sec5_en, sec5_hi,
    "What does 'symbolic material culture' mean in prehistoric archaeology?",
    "प्रागैतिहासिक पुरातत्व में 'प्रतीकात्मक भौतिक संस्कृति' (symbolic material culture) का क्या अर्थ है?",
    "Physical artifacts (like beads, art, shrines) created not just for physical survival, but to communicate abstract meanings, beliefs, or identity.",
    "भौतिक उपकरण (जैसे मनके, कला, मंदिर) जो न केवल जीवित रहने के लिए बल्कि अमूर्त अर्थों, विश्वासों या पहचान को संप्रेषित करने के लिए बनाए गए थे।"
)

# --- 7. Assertion-Reason (8 Questions) ---
add_ar(sec5_en, sec5_hi,
    "Assertion (A): The Baghor I assembly is widely accepted as a prehistoric ritual shrine.\nReason (R): The central placement of a natural triangular laminated sandstone on a sandstone platform mirrors modern tribal shrines dedicated to 'Mai' in the same valley.",
    "कथन (A): बाघोर I असेंबली को व्यापक रूप से एक प्रागैतिहासिक अनुष्ठान स्थल (ritual shrine) के रूप में स्वीकार किया जाता है।\nकारण (R): एक बलुआ पत्थर के चबूतरे पर एक प्राकृतिक त्रिकोणीय स्तरित बलुआ पत्थर की केंद्रीय स्थिति इसी घाटी में 'माई' को समर्पित आधुनिक आदिवासी मंदिरों के समान है।",
    0,
    "Both A and R are true and R is the correct explanation of A. The ethnographic parallel directly explains the archaeological interpretation of a shrine.",
    "A और R दोनों सही हैं और R, A की सही व्याख्या करता है। नृवंशविज्ञान सादृश्य सीधे तौर पर एक मंदिर की पुरातात्विक व्याख्या को समझाता है।"
)

add_ar(sec5_en, sec5_hi,
    "Assertion (A): Upper Paleolithic humans painted only green figures and never used red pigments.\nReason (R): Hematite minerals were abundant in the Vindhyas, providing a natural source of iron oxide red paint.",
    "कथन (A): उच्च पुरापाषाणकालीन मनुष्यों ने केवल हरे रंग के चित्र बनाए और कभी भी लाल रंगों का उपयोग नहीं किया।\nकारण (R): विंध्य में हेमेटाइट खनिज प्रचुर मात्रा में थे, जो आयरन ऑक्साइड लाल पेंट का एक प्राकृतिक स्रोत प्रदान करते थे।",
    3,
    "A is false but R is true. Hominins used both green and red, though green is the oldest layer. Hematite was abundant in the Vindhyas.",
    "A गलत है लेकिन R सही है। होमिनिन ने हरे और लाल दोनों रंगों का उपयोग किया, हालांकि हरे रंग की परत सबसे पुरानी है। विंध्य में हेमेटाइट प्रचुर मात्रा में था।"
)

add_ar(sec5_en, sec5_hi,
    "Assertion (A): The discovery of decorated ostrich eggshells in India proves that ostriches co-existed with prehistoric humans in the late Pleistocene.\nReason (R): Radiocarbon dating of these organic eggshells yields ages of c. 25,000 BCE, matching the Upper Paleolithic tool layers.",
    "कथन (A): भारत में अलंकृत शुतुरमुर्ग के अंडे के छिलके की खोज साबित करती है कि शुतुरमुर्ग लेट प्लीस्टोसीन काल में प्रागैतिहासिक मनुष्यों के साथ रहते थे।\nकारण (R): इन जैविक अंडों के छिलकों का रेडियोकार्बन काल-निर्धारण लगभग 25,000 ईसा पूर्व की आयु देता है, जो उच्च पुरापाषाणकालीन उपकरण परतों से मेल खाता है।",
    0,
    "Both A and R are true and R is the correct explanation of A. Direct C-14 dating of the shell bones confirms their Pleistocene antiquity.",
    "A और R दोनों सही हैं और R, A की सही व्याख्या करता है। शेल के जैविक टुकड़ों की सीधी C-14 डेटिंग उनके प्लीस्टोसीन काल की होने की पुष्टि करती है।"
)

add_ar(sec5_en, sec5_hi,
    "Assertion (A): V.S. Wakankar's discovery of Bhimbetka in 1957 was a major breakthrough in South Asian prehistory.\nReason (R): Before Bhimbetka, South Asia was believed to have no prehistoric rock paintings at all.",
    "कथन (A): 1957 में वी.एस. वाकणकर द्वारा भीमबेटका की खोज दक्षिण एशियाई प्रागैतिहास में एक बड़ी सफलता थी।\nकारण (R): भीमबेटका से पहले, यह माना जाता था कि दक्षिण एशिया में कोई प्रागैतिहासिक शैल चित्र थे ही नहीं।",
    0,
    "Both A and R are true and R is the correct explanation of A. The discovery completely reshaped the understanding of prehistoric art in the subcontinent.",
    "A और R दोनों सही हैं और R, A की सही व्याख्या करता है। इस खोज ने उपमहाद्वीप में प्रागैतिहासिक कला की समझ को पूरी तरह से बदल दिया।"
)

add_ar(sec5_en, sec5_hi,
    "Assertion (A): Prehistoric rock paintings survive on cave sandstone walls because of chemical integration.\nReason (R): Iron and copper oxides in mineral pigments reacted with the silica in the sandstone, fusing the drawing into the rock matrix.",
    "कथन (A): प्रागैतिहासिक शैल चित्र गुफा बलुआ पत्थर की दीवारों पर जीवित रहे क्योंकि उनमें रासायनिक एकीकरण हुआ था।\nकारण (R): खनिज पिगमेंट में आयरन और कॉपर ऑक्साइड ने बलुआ पत्थर में सिलिका के साथ प्रतिक्रिया की, जिससे चित्र चट्टान की संरचना में समा गया।",
    0,
    "Both A and R are true and R is the correct explanation of A. Chemical bonding between oxides and silica explains paint preservation.",
    "A और R दोनों सही हैं और R, A की सही व्याख्या करता है। ऑक्साइड और सिलिका के बीच रासायनिक बंधन पेंट के संरक्षण की व्याख्या करता है।"
)

add_ar(sec5_en, sec5_hi,
    "Assertion (A): Paleolithic bead-makers utilized advanced automated industrial drills to punch holes in ostrich eggshells.\nReason (R): Ostrich eggshells are hard and require high friction to drill without breaking.",
    "कथन (A): पुरापाषाणकालीन मनका बनाने वालों ने शुतुरमुर्ग के अंडे के छिलके में छेद करने के लिए उन्नत स्वचालित औद्योगिक ड्रिल का उपयोग किया था।\nकारण (R): शुतुरमुर्ग के अंडे के छिलके कठोर होते हैं और बिना टूटे छेद करने के लिए उच्च घर्षण की आवश्यकता होती है।",
    3,
    "A is false but R is true. They used hand-held chert micro-borers, not automated industrial drills.",
    "A गलत है लेकिन R सही है। उन्होंने हाथ से चलने वाले चर्ट माइक्रो-वेधकों का उपयोग किया, न कि स्वचालित औद्योगिक ड्रिल का।"
)

add_ar(sec5_en, sec5_hi,
    "Assertion (A): The engravings on ostrich eggshells are representational depictions of domestic crops.\nReason (R): Agriculture did not exist during the Late Pleistocene Upper Paleolithic phase, and artistic expression was limited to abstract geometric lines.",
    "कथन (A): शुतुरमुर्ग के अंडे के छिलके पर नक्काशी घरेलू फसलों के प्रतिनिधिक चित्रण हैं।\nकारण (R): लेट प्लीस्टोसीन उच्च पुरापाषाण चरण के दौरान कृषि अस्तित्व में नहीं थी, और कलात्मक अभिव्यक्ति अमूर्त ज्यामितीय रेखाओं तक सीमित थी।",
    3,
    "A is false but R is true. The engravings are abstract geometric cross-hatches, not crops. Agriculture arose in the Neolithic.",
    "A गलत है लेकिन R सही है। नक्काशी अमूर्त ज्यामितीय रेखाएं हैं, फसलें नहीं। कृषि का उदय नवपाषाण काल में हुआ था।"
)

add_ar(sec5_en, sec5_hi,
    "Assertion (A): Ostrich eggshell fragments have been found in Harappan Indus Valley seals.\nReason (R): Ostriches became extinct in India by the start of the Holocene epoch, long before the Harappan civilization emerged.",
    "कथन (A): हड़प्पाकालीन सिंधु घाटी की मुहरों में शुतुरमुर्ग के अंडे के छिलके के टुकड़े पाए गए हैं।\nकारण (R): हड़प्पा सभ्यता के उदय से बहुत पहले, होलोसीन युग की शुरुआत तक भारत में शुतुरमुर्ग विलुप्त हो गए थे।",
    3,
    "A is false but R is true. Ostrich fragments are not found in Harappan seals; ostriches were extinct by the Holocene in India.",
    "A गलत है लेकिन R सही है। हड़प्पा की मुहरों में शुतुरमुर्ग के टुकड़े नहीं मिले हैं; होलोसीन की शुरुआत तक भारत में शुतुरमुर्ग विलुप्त हो चुके थे।"
)

# --- 8. Statement-Based (5 Questions) ---
add_stmt(sec5_en, sec5_hi,
    "Consider the following statements regarding the Bhimbetka cave paintings:\n1. The green paintings showing stick dancers represent the earliest Upper Paleolithic layer.\n2. The red paintings depicting heavy metal carts represent the subsequent Mesolithic layer.\nWhich of the statements given above is/are correct?",
    "भीमबेटका गुफा चित्रों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. छड़ी जैसे नर्तकों को दर्शाने वाले हरे रंग के चित्र सबसे पुराने उच्च पुरापाषाणकालीन चरण का प्रतिनिधित्व करते हैं।\n2. भारी धातु की गाड़ियों को दर्शाने वाले लाल चित्र उसके बाद के मध्यपाषाणकालीन चरण का प्रतिनिधित्व करते हैं।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
    0,
    "Statement 1 is correct. Statement 2 is incorrect because metal carts belong to the Chalcolithic and historical phases, not the Mesolithic.",
    "कथन 1 सही है। कथन 2 गलत है क्योंकि धातु की गाड़ियां ताम्रपाषाण और ऐतिहासिक चरणों की हैं, न कि मध्यपाषाण काल की।"
)

add_stmt(sec5_en, sec5_hi,
    "Consider the following statements regarding the Baghor I prehistoric site:\n1. A rubble platform containing a natural triangular laminated stone was discovered in the Son Valley.\n2. Archaeologists used ethnographic analogy with local tribal 'Mai' shrines to interpret this site as a mother goddess altar.\nWhich of the statements given above is/are correct?",
    "बाघोर I प्रागैतिहासिक स्थल के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. सोन घाटी में एक प्राकृतिक त्रिकोणीय स्तरित पत्थर वाला मलबे का चबूतरा खोजा गया था।\n2. पुरातत्वविदों ने इस स्थल को मातृ देवी की वेदी के रूप में व्याख्यायित करने के लिए स्थानीय आदिवासी 'माई' मंदिरों के साथ नृवंशविज्ञान सादृश्य का उपयोग किया।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
    2,
    "Both Statement 1 and Statement 2 are true. The platform with the triangular stone is interpreted as a shrine using Kol/Gond ethnographic parallels.",
    "कथन 1 और कथन 2 दोनों सही हैं। त्रिकोणीय पत्थर वाले चबूतरे को कोल/गोंड नृवंशविज्ञान समानांतरों का उपयोग करके एक मंदिर के रूप में माना गया है।"
)

add_stmt(sec5_en, sec5_hi,
    "Consider the following statements regarding ostrich eggshell art in India:\n1. Engraved ostrich eggshell fragments were discovered at Patne and Chandresal.\n2. The eggshells were dated using Uranium-series and Radiocarbon dating to approximately 25,000 BCE.\nWhich of the statements given above is/are correct?",
    "भारत में शुतुरमुर्ग के अंडे के छिलके की कला के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. महाराष्ट्र के पाटणे और राजस्थान के चंद्रसाल से अलंकृत शुतुरमुर्ग के अंडे के छिलके के टुकड़े प्राप्त हुए थे।\n2. यूरेनियम-श्रृंखला और रेडियोकार्बन डेटिंग का उपयोग करके इन अंडों के छिलकों की आयु लगभग 25,000 ईसा पूर्व आंकी गई थी।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
    2,
    "Both Statement 1 and Statement 2 are true. Ostrich shells are key indicators of late Pleistocene art and aridity in India.",
    "कथन 1 और कथन 2 दोनों सही हैं। शुतुरमुर्ग के छिलके भारत में लेट प्लीस्टोसीन काल की कला और शुष्कता के प्रमुख संकेतक हैं।"
)

add_stmt(sec5_en, sec5_hi,
    "With reference to colors in prehistoric art, consider the following statements:\n1. Chlorite minerals were pulverized to create green pigment.\n2. Hematite iron oxides were pulverized to produce red pigment.\nWhich of the statements given above is/are correct?",
    "प्रागैतिहासिक कला में रंगों के संदर्भ में, निम्नलिखित कथनों पर विचार करें:\n1. हरे रंग के पिगमेंट के निर्माण के लिए क्लोराइट खनिजों को पीसा जाता था।\n2. लाल पिगमेंट के उत्पादन के लिए हेमेटाइट आयरन ऑक्साइड को पीसा जाता था।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
    2,
    "Both Statement 1 and Statement 2 are true. Pulverized chlorite and hematite mixed with organic binders were the key pigments of the Upper Paleolithic.",
    "कथन 1 और कथन 2 दोनों सही हैं। जैविक बाइंडरों के साथ मिश्रित पीसा हुआ क्लोराइट और हेमेटाइट उच्च पुरापाषाण काल के प्रमुख रंग थे।"
)

add_stmt(sec5_en, sec5_hi,
    "Consider the following statements regarding Paleolithic self-ornamentation in India:\n1. Patne excavations yielded complete ostrich eggshell beads alongside unfinished blanks.\n2. The beads were manufactured using iron needles imported from Central Asia.\nWhich of the statements given above is/are correct?",
    "भारत में पुरापाषाणकालीन आत्म-श्रृंगार के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. पाटणे उत्खनन से अधूरे ब्लैंक्स के साथ-साथ तैयार शुतुरमुर्ग के अंडे के छिलके के मनके भी प्राप्त हुए।\n2. इन मनकों का निर्माण मध्य एशिया से आयातित लोहे की सुइयों का उपयोग करके किया गया था।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
    0,
    "Statement 1 is true but Statement 2 is false. Iron was unknown in the Paleolithic; beads were drilled using chert micro-borers.",
    "कथन 1 सही है लेकिन कथन 2 गलत है। पुरापाषाण काल में लोहा अज्ञात था; मनकों में छेद चर्ट माइक्रो-वेधकों से किया जाता था।"
)

# --- 9. Why (3 Questions) ---
add_open(sec5_en, sec5_hi, "Why",
    "Why is the Baghor I platform assembly in the Son Valley interpreted as a ritual shrine dedicated to a Mother Goddess rather than a simple domestic hearth or tool workshop?",
    "सोन घाटी में बाघोर I चबूतरे को एक साधारण चूल्हे या उपकरण कार्यशाला के बजाय मातृ देवी को समर्पित एक धार्मिक मंदिर के रूप में क्यों व्याख्यायित किया गया है?",
    "The Baghor I platform is interpreted as a ritual shrine based on key archaeological and ethnographic features:\n1. Non-Functional Nature: The platform contains no bone remnants, charcoal, or tool debitage, ruling out a cooking hearth or tool workshop.\n2. Central Symbolic Object: A natural triangular sandstone displaying concentric colored rings was placed at the very center of a raised platform. This rock was sourced from the distant Kaimur hills, selected for its unique natural design.\n3. Ethnographic Analogy: Local Gond and Kol tribes in the same valley currently build identical rubble platforms containing similar natural triangular laminated stones to worship 'Mai' (Mother Goddess) for protection and fertility.\nThis direct ethnographic link strongly supports its identification as a prehistoric mother goddess shrine.",
    "बाघोर I चबूतरे को निम्नलिखित पुरातात्विक और नृवंशविज्ञान विशेषताओं के आधार पर एक मंदिर के रूप में माना गया है:\n1. गैर-कार्यात्मक प्रकृति: चबूतरे पर कोई हड्डी के अवशेष, चारकोल या उपकरण कचरा नहीं है, जिससे यह रसोईघर या उपकरण कार्यशाला नहीं हो सकता।\n2. केंद्रीय प्रतीकात्मक वस्तु: चबूतरे के ठीक केंद्र में संकेंद्रित रंगीन छल्लों वाला एक प्राकृतिक त्रिकोणीय बलुआ पत्थर रखा गया था। यह पत्थर दूर की कैमूर पहाड़ियों से लाया गया था, जिसे इसके अनोखे आकार के कारण चुना गया था।\n3. नृवंशविज्ञान सादृश्य: इसी घाटी में स्थानीय गोंड और कोल जनजातियां आज भी सुरक्षा और उर्वरता के लिए 'माई' (मातृ देवी) की पूजा करने के लिए समान प्राकृतिक त्रिकोणीय पत्थरों वाले चबूतरे बनाती हैं।\nयह सीधा जनजातीय संबंध इसे प्रागैतिहासिक मातृ देवी मंदिर के रूप में मानने का दृढ़ता से समर्थन करता है।"
)

add_open(sec5_en, sec5_hi, "Why",
    "Why are the green drawings of dancers at Bhimbetka attributed to the Upper Paleolithic phase, while the red paintings are attributed to later Mesolithic and historical phases?",
    "भीमबेटका में नर्तकों के हरे रंग के चित्रों को उच्च पुरापाषाण चरण का क्यों माना जाता है, जबकि लाल चित्रों को बाद के मध्यपाषाण और ऐतिहासिक चरणों का माना जाता है?",
    "The chronological assignment of Bhimbetka rock paintings is established through three criteria:\n1. Stratigraphic Superposition: In shelters where paintings overlap, the green paintings are consistently found at the lowest level, directly on the sandstone face, with red and white layers painted on top of them. This proves the green layer is oldest.\n2. Subject Matter and Style: Green paintings depict dynamic stick figures dancing or carrying bows, alongside large wild animal silhouettes (bisons, boars). They contain no domesticated animals, metal weapons, or carts.\n3. Relative Dating: The stylized linear animal silhouettes match the Upper Paleolithic art tradition seen on portable dated media (like Patne shell engravings), whereas red drawings depict microliths (Mesolithic) or horses/swords (historical).",
    "भीमबेटका शैल चित्रों का कालक्रम निर्धारण तीन मानदंडों के माध्यम से किया गया है:\n1. स्तरविन्यास सुपरपोजिशन (Superposition): जिन आश्रयों में चित्र एक-दूसरे के ऊपर बने हैं, उनमें हरे रंग के चित्र हमेशा सबसे निचले स्तर पर (बलुआ पत्थर की सतह पर) पाए जाते हैं, और उनके ऊपर लाल व सफेद परतें बनी हैं। यह साबित करता है कि हरी परत सबसे पुरानी है।\n2. विषय वस्तु और शैली: हरे चित्र छड़ी जैसी गतिशील आकृतियों को नृत्य करते या धनुष ले जाते हुए दिखाते हैं, साथ ही बड़े जंगली जानवरों (बैल, जंगली सूअर) को भी दर्शाते हैं। इनमें पालतू जानवरों, धातु के हथियारों या रथों का अभाव है।\n3. सापेक्ष काल-निर्धारण: शैलियों का मिलान उच्च पुरापाषाणकालीन शैलियों से होता है, जबकि लाल चित्र सूक्ष्म-पाषाणों (मध्यपाषाण) या घोड़ों/तलवारों (ऐतिहासिक) को दर्शाते हैं।"
)

add_open(sec5_en, sec5_hi, "Why",
    "Why is the emergence of personal ornamentation, such as the ostrich eggshell beads at Patne, considered a major cognitive milestone in human evolution?",
    "पाटणे में शुतुरमुर्ग के अंडे के छिलके के मनके जैसे व्यक्तिगत अलंकरण के उदय को मानव विकास में एक बड़ा संज्ञानात्मक मील का पत्थर क्यों माना जाता है?",
    "The manufacture and wearing of beads represent a major cognitive leap due to three factors:\n1. Abstract Symbolic Thought: Beads serve no physical survival function. They are symbols used to communicate abstract concepts, such as personal identity, social status, group affiliation, and gender role within a mobile band.\n2. Technology of Micro-Manufacturing: Making tiny, uniform beads from hard ostrich shells requires advanced motor control and planning, including cutting blanks, drilling central holes using chert micro-borers, and smoothing edges.\n3. Shared Social Codes: For a bead to convey meaning, the entire band must agree on its social significance, proving the existence of complex language and shared social beliefs.",
    "मनके बनाने और पहनने को निम्नलिखित तीन कारणों से एक बड़ा संज्ञानात्मक विकास माना जाता है:\n1. अमूर्त प्रतीकात्मक विचार: मनके जीवित रहने के लिए किसी भौतिक कार्य में मदद नहीं करते। वे व्यक्तिगत पहचान, सामाजिक स्थिति, समूह संबद्धता और समूह के भीतर भूमिका जैसी अमूर्त अवधारणाओं को संप्रेषित करने के साधन हैं।\n2. सूक्ष्म-निर्माण की तकनीक: कठोर शुतुरमुर्ग के छिलकों से छोटे, एक समान मनके बनाने के लिए उन्नत योजना और नियंत्रण की आवश्यकता होती है, जिसमें शेल काटना, छिद्र करना और किनारों को चिकना करना शामिल है।\n3. साझा सामाजिक कोड: मनके द्वारा अर्थ संप्रेषित करने के लिए, पूरे समूह को इसके सामाजिक महत्व पर सहमत होना पड़ता है, जो जटिल भाषा और साझा सामाजिक विश्वासों के अस्तित्व को साबित करता है।"
)

# --- 10. How (3 Questions) ---
add_open(sec5_en, sec5_hi, "How",
    "How did Dr. V.S. Wakankar locate and discover the Bhimbetka rock shelters in 1957? Describe his journey and observations.",
    "1957 में डॉ. वी.एस. वाकणकर ने भीमबेटका रॉक शेल्टर की खोज कैसे की थी? उनकी यात्रा और टिप्पणियों का वर्णन करें।",
    "Dr. V.S. Wakankar discovered Bhimbetka in 1957 through keen geological observation and exploration:\n1. Visual Observation: While travelling by train towards Itarsi, Wakankar looked out the window and noticed massive, unique Vindhyan sandstone formations jutting out above the forest canopy near Obaydullaganj.\n2. Geological Insight: Recognizing that these natural rocks were identical to shelters containing rock art in France and Spain, he decided to investigate.\n3. Exploration: Wakankar disembarked, entered the dense forest with a local guide, and discovered hundreds of rock shelters containing prehistoric paintings, bringing the site to global archaeological prominence.",
    "डॉ. वी.एस. वाकणकर ने 1957 में भूवैज्ञानिक टिप्पणियों और अन्वेषण के माध्यम से भीमबेटका की खोज की:\n1. दृश्य अवलोकन: इटारसी की ओर ट्रेन से यात्रा करते समय, वाकणकर ने खिड़की से बाहर देखा और ओबैदुल्लागंज के पास जंगल के ऊपर विशाल, अनोखी विंध्य बलुआ पत्थर की चट्टानें देखीं।\n2. भूवैज्ञानिक अंतर्दृष्टि: यह पहचानते हुए कि ये प्राकृतिक चट्टानें फ्रांस और स्पेन में शैल कला वाले गुफा आश्रयों के समान थीं, उन्होंने जांच करने का फैसला किया।\n3. अन्वेषण: वाकणकर ट्रेन से उतरे, एक स्थानीय गाइड के साथ घने जंगल में गए, और प्रागैतिहासिक चित्रों से युक्त सैकड़ों रॉक शेल्टरों की खोज की, जिससे यह स्थल वैश्विक पुरातात्विक मानचित्र पर आया।"
)

add_open(sec5_en, sec5_hi, "How",
    "How did Upper Paleolithic humans manufacture uniform circular beads from raw ostrich eggshells? Detail the manufacturing sequence.",
    "उच्च पुरापाषाणकालीन मनुष्यों ने शुतुरमुर्ग के अंडे के कच्चे छिलकों से एक समान गोलाकार मनके (beads) कैसे बनाए? निर्माण अनुक्रम का विवरण दें।",
    "Upper Paleolithic artisans manufactured beads through a systematic, multi-step sequence:\n1. Blank Selection: Raw ostrich eggshell fragments were broken into small polygonal pieces (blanks) using stone hammerstones.\n2. Drilling: A central hole was drilled into each blank from both sides using a sharp, hand-rotated chert micro-borer or drill point.\n3. Rough Shaping: The drilled blanks were roughly chipped around the edges to form a crude circular shape.\n4. Edge Smoothing: The blanks were threaded together onto a tight cord of animal sinew. The entire string of beads was then rubbed back and forth inside a groove cut into a sandstone slab, grinding the outer edges simultaneously to produce perfectly uniform, polished circular beads.",
    "उच्च पुरापाषाणकालीन कारीगरों ने एक व्यवस्थित, बहु-चरण अनुक्रम के माध्यम से मनकों का निर्माण किया:\n1. ब्लैंक का चयन: शुतुरमुर्ग के अंडे के कच्चे छिलके के टुकड़ों को पत्थर के हथौड़ों का उपयोग करके छोटे बहुभुज टुकड़ों (blanks) में तोड़ा गया। \n2. छिद्र करना: एक तेज, हाथ से घुमाए जाने वाले चर्ट माइक्रो-वेधक (borer) का उपयोग करके प्रत्येक टुकड़े के केंद्र में दोनों तरफ से एक छेद किया गया।\n3. खुरदरा आकार देना: छिद्रित टुकड़ों के किनारों को एक कच्चा गोलाकार आकार देने के लिए तोड़ा गया।\n4. किनारों को चिकना करना: टुकड़ों को तांत की एक तंग रस्सी पर एक साथ पिरोया गया। इसके बाद बलुआ पत्थर के स्लैब में बने एक खांचे के भीतर पूरी माला को आगे-पीछे रगड़ा गया, जिससे बाहरी किनारे चिकने हो गए और एक समान, पॉलिश किए गए गोलाकार मनके तैयार हो गए।"
)

add_open(sec5_en, sec5_hi, "How",
    "How do archaeologists reconstruct the chronological sequence (relative dating) of cave paintings when organic binders are absent?",
    "जब जैविक बाइंडरों का अभाव हो, तो पुरातत्वविद गुफा चित्रों के कालानुक्रमिक अनुक्रम (सापेक्ष काल-निर्धारण) का पुनर्निर्माण कैसे करते हैं?",
    "When carbon-14 dating is impossible due to lack of organic binders, archaeologists reconstruct relative dates using three methods:\n1. Superposition Analysis: Examining overlapping layers of paint under magnifying lenses. The paint layer at the bottom is older, while the layer painted on top is younger.\n2. Stylistic and Subject Analysis: Comparing the artistic style (linear outlines vs. filled silhouettes) and subject matter (wild Pleistocene game vs. domestic cattle and horse riders) with dated portable art.\n3. Physical Weathering: Observing the degree of mineral mineralization and weathering of the paint. E.g., green paintings are often deeply integrated into the sandstone silica matrix, showing great antiquity.",
    "जब जैविक बाइंडरों की कमी के कारण कार्बन-14 डेटिंग असंभव होती है, तो पुरातत्वविद तीन तरीकों का उपयोग करके सापेक्ष तिथियों का पुनर्निर्माण करते हैं:\n1. सुपरपोजिशन (Superposition) विश्लेषण: आवर्धक लेंस के तहत पेंट की ओवरलैपिंग परतों की जांच करना। नीचे की पेंट की परत पुरानी है, जबकि ऊपर की परत नई है।\n2. शैली और विषय वस्तु का विश्लेषण: कलात्मक शैली (रेखाकृतियाँ बनाम भरी हुई आकृतियाँ) और विषय वस्तु (जंगली प्लीस्टोसीन जानवर बनाम पालतू मवेशी और घुड़सवार) की तुलना अन्य काल-निर्धारित कलाओं से करना।\n3. भौतिक अपक्षय: पेंट के खनिजकरण और अपक्षय की सीमा का अवलोकन करना। उदाहरण के लिए, हरे रंग के चित्र अक्सर बलुआ पत्थर की सिलिका संरचना में गहराई से एकीकृत होते हैं, जो उनकी प्राचीनता को दर्शाता है।"
)

# --- 11. Case Study (3 Questions) ---
add_open(sec5_en, sec5_hi, "Case Study",
    "Case Study: The Ritual Context of the Baghor I Prehistoric Platform\n\nAnalyze the Baghor I platform assembly. Examine the geological origin of the triangular stone and discuss why the site represents one of the earliest examples of continuity in Indian religious practices.",
    "केस स्टडी: बाघोर I प्रागैतिहासिक चबूतरे का धार्मिक संदर्भ\n\nबाघोर I चबूतरे की संरचना का विश्लेषण करें। त्रिकोणीय पत्थर की भूवैज्ञानिक उत्पत्ति का परीक्षण करें और चर्चा करें कि क्यों यह स्थल भारतीय धार्मिक प्रथाओं में निरंतरता के सबसे पुराने उदाहरणों में से एक का प्रतिनिधित्व करता है।",
    "The Baghor I platform assembly in the Son Valley displays remarkable symbolic complexity:\n1. Architectural Structure: A circular platform constructed of sandstone rubble stones, measuring c. 85 cm in diameter.\n2. The Laminated Stone: A natural triangular sandstone displaying yellow, red, and brown concentric rings. Geological analysis proved the stone was sourced from the Kaimur range, transported by humans to the site.\n3. Continuity: Local Kol and Gond tribal groups in the Son Valley still build identical rubble platforms under trees, placing similar natural triangular laminated sandstones to worship 'Mai' (Mother Goddess). The tribal priests identified the Baghor stone as Mai when excavated.\nThis represents an extraordinary 10,000+ year cultural continuity of goddess worship in Central India.",
    "सोन घाटी में बाघोर I चबूतरा उल्लेखनीय प्रतीकात्मक जटिलता प्रदर्शित करता है:\n1. स्थापत्य संरचना: बलुआ पत्थर के मलबे से बना एक गोलाकार चबूतरा, जिसका व्यास लगभग 85 सेमी है।\n2. स्तरित पत्थर: पीले, लाल और भूरे रंग के संकेंद्रित छल्लों वाला एक प्राकृतिक त्रिकोणीय बलुआ पत्थर। भूवैज्ञानिक विश्लेषण से साबित हुआ कि यह पत्थर कैमूर पर्वत श्रृंखला से लाया गया था।\n3. सांस्कृतिक निरंतरता: सोन घाटी में स्थानीय कोल और गोंड आदिवासी समूह आज भी पेड़ों के नीचे समान मलबे के चबूतरे बनाते हैं और 'माई' (मातृ देवी) की पूजा करने के लिए समान प्राकृतिक त्रिकोणीय स्तरित बलुआ पत्थर रखते हैं। उत्खनन के समय आदिवासी पुजारियों ने बाघोर पत्थर की पहचान 'माई' के रूप में की थी।\nयह मध्य भारत में मातृ देवी की पूजा की एक असाधारण 10,000 से अधिक वर्षों की सांस्कृतिक निरंतरता का प्रतिनिधित्व करता है।"
)

add_open(sec5_en, sec5_hi, "Case Study",
    "Case Study: Relative Chronology of Painting Styles at Bhimbetka Rock Shelters\n\nAnalyze how archaeologists established the sequence of art at Bhimbetka. Compare the styles, colors, and subjects of Upper Paleolithic and Mesolithic layers.",
    "केस स्टडी: भीमबेटका रॉक शेल्टर में चित्रकला शैलियों का सापेक्ष कालक्रम\n\nविश्लेषण करें कि पुरातत्वविदों ने भीमबेटका में कला के अनुक्रम को कैसे स्थापित किया। उच्च पुरापाषाण और मध्यपाषाण परतों की शैलियों, रंगों और विषयों की तुलना करें।",
    "Archaeologists established a relative chronology of Bhimbetka rock art through superposition and style analysis:\n1. Upper Paleolithic Layer (Oldest): Painted in green (chlorite) and dark red (hematite). The figures are large, life-size linear outlines of wild animals (bisons, tigers, elephants) and dynamic stick-like human dancing figures. There are no domestic animals or weapons.\n2. Mesolithic Layer (Succeeding): Painted in bright red. The figures are much smaller, showing filled-in silhouettes. The subject matter shifts to group hunting with bows and arrows, honey collection, family scenes, and community dances.\n3. Historical Layer (Youngest): Painted in white and yellow. It depicts horse riders with metal shields, swords, flags, and inscriptions in Brahmi script.\nThis sequence shows a clear transition from Pleistocene hunter-gatherers to Holocene societies.",
    "पुरातत्वविदों ने सुपरपोजिशन और शैली विश्लेषण के माध्यम से भीमबेटका शैल कला का एक सापेक्ष कालक्रम स्थापित किया:\n1. उच्च पुरापाषाण परत (सबसे पुरानी): हरे (क्लोराइट) और गहरे लाल (हेमेटाइट) रंग में चित्रित। आकृतियाँ जंगली जानवरों (जंगली भैंसे, बाघ, हाथी) की बड़ी रेखाकृतियाँ और गतिशील नर्तक हैं। यहाँ पालतू जानवरों का अभाव है।\n2. मध्यपाषाण परत (मध्यम): चमकीले लाल रंग में चित्रित। आकृतियाँ बहुत छोटी हैं, जिनमें भरी हुई आकृतियाँ (silhouettes) दिखाई गई हैं। विषय वस्तु धनुष-बाण से शिकार, शहद इकट्ठा करने और पारिवारिक दृश्यों में बदल जाती है।\n3. ऐतिहासिक परत (सबसे नई): सफेद और पीले रंग में चित्रित। इसमें ढाल, तलवार, झंडे वाले घुड़सवार और ब्राह्मी लिपि में लिखे शिलालेख दिखाए गए हैं।\nयह अनुक्रम प्लीस्टोसीन शिकारी-संग्रहकर्ताओं से होलोसीन समाजों में संक्रमण को दर्शाता है।"
)

add_open(sec5_en, sec5_hi, "Case Study",
    "Case Study: Ostrich Eggshell Beads as Markers of Late Pleistocene Symbolic Behavior\n\nAnalyze the distribution of ostrich eggshell art in India. Discuss the manufacturing workshop at Patne and how these ornaments serve as markers of social communication.",
    "केस स्टडी: लेट प्लीस्टोसीन प्रतीकात्मक व्यवहार के संकेतक के रूप में शुतुरमुर्ग के अंडे के छिलके के मनके\n\nभारत में शुतुरमुर्ग के अंडे के छिलके की कला के वितरण का विश्लेषण करें। पाटणे में निर्माण कार्यशाला पर चर्चा करें और बताएं कि कैसे ये आभूषण सामाजिक संचार के संकेतक के रूप में काम करते हैं।",
    "Ostrich eggshell fragments have been recovered from over 40 late Pleistocene sites in India, with Patne being the key workshop:\n1. Workshop Evidence at Patne: Excavations by S.A. Sali yielded shell fragments showing various manufacturing stages: raw shell pieces, drilled circular blanks, unfinished broken beads, and completed polished beads alongside sandstone grinding slabs.\n2. Aesthetic and Cognitive Aspects: Several shells show geometric cross-hatched engravings. This indicates that eggshells served as both raw material for beads and canvases for abstract art.\n3. Social Communication: Hunter-gatherers used these beads as body ornaments. In band societies, ornaments are 'visual shorthand' to communicate tribal identity, status, marital readiness, or ritual roles to other bands without verbal communication.\nConclusion: Beads prove that late Pleistocene humans in India possessed fully modern symbolic capacities.",
    "शुतुरमुर्ग के अंडे के छिलके के टुकड़े भारत में 40 से अधिक लेट प्लीस्टोसीन स्थलों से बरामद किए गए हैं, जिसमें पाटणे प्रमुख कार्यशाला है:\n1. पाटणे में कार्यशाला के साक्ष्य: एस.ए. साली द्वारा किए गए उत्खनन से शेल के ऐसे टुकड़े मिले जो निर्माण के विभिन्न चरणों को दिखाते हैं: कच्चे टुकड़े, छिद्रित गोलाकार ब्लैंक्स, अधूरे टूटे हुए मनके और तैयार पॉलिश किए गए मनके।\n2. सौंदर्यशास्त्र और संज्ञानात्मक पहलू: कई टुकड़ों पर ज्यामितीय नक्काशी मिलती है। यह दर्शाता है कि अंडे के छिलके कला के लिए कैनवास के रूप में भी काम करते थे।\n3. सामाजिक संचार: शिकारी-संग्रहकर्ता इन मनकों का उपयोग शरीर के आभूषणों के रूप में करते थे। टोलियों में, आभूषण सामाजिक पहचान, स्थिति या अनुष्ठानिक भूमिकाओं को संप्रेषित करने के साधन होते हैं।\nनिष्कर्ष: मनके साबित करते हैं कि भारत में लेट प्लीस्टोसीन मानव पूरी तरह से आधुनिक प्रतीकात्मक क्षमता रखता था।"
)

# --- 12. Teach the Concept (3 Questions) ---
add_open(sec5_en, sec5_hi, "Teach the Concept",
    "Teach the Concept: Prehistoric Cave Art in India\n\nExplain the history, discovery, pigments, styles, and significance of prehistoric rock art in India, using Bhimbetka as the primary model. Discuss the transition across eras.",
    "अवधारणा सिखाएं: भारत में प्रागैतिहासिक गुफा कला (Prehistoric Cave Art)\n\nभीमबेटका को प्राथमिक मॉडल के रूप में उपयोग करते हुए भारत में प्रागैतिहासिक शैल कला के इतिहास, खोज, रंगों, शैलियों और महत्व की व्याख्या करें। युगों के बीच संक्रमण पर चर्चा करें।",
    "Prehistoric cave art represents the earliest creative expression of humans in India. Key concepts include:\n1. Discovery: Dr. V.S. Wakankar discovered Bhimbetka in 1957. Located in the Vindhyas, it contains over 700 rock shelters.\n2. Pigments and Binders: Made from ground local minerals. Red paint was made from hematite (geru), green from chlorite/chalcedony, and black from manganese. Pigments were mixed with animal fat or plant sap to bind with sandstone silica.\n3. Styles and Evolution:\n   - Upper Paleolithic (Earliest): Green stick-figure dancers and massive linear wild animal outlines. Represents a pure hunter-gatherer phase.\n   - Mesolithic: Bright red, small, filled-in silhouettes depicting group hunting, family life, honey gathering, and rituals.\n   - Historic: White and yellow drawings of horse riders, soldiers with metal armor, swords, and scripts.\nKey Takeaway: Cave art serves as a visual record of human cognitive, social, and technological evolution in India.",
    "प्रागैतिहासिक गुफा कला भारत में मनुष्यों की सबसे पुरानी रचनात्मक अभिव्यक्ति का प्रतिनिधित्व करती है। मुख्य अवधारणाओं में शामिल हैं:\n1. खोज: डॉ. वी.एस. वाकणकर ने 1957 में भीमबेटका की खोज की। विंध्य पर्वत श्रृंखला में स्थित इस स्थल में 700 से अधिक रॉक शेल्टर हैं।\n2. पिगमेंट और बाइंडर्स: ये स्थानीय खनिजों को पीसकर बनाए जाते थे। लाल रंग हेमेटाइट (गेरू) से, हरा क्लोराइट से और काला मैंगनीज से बनता था। पिगमेंट को जानवरों की चर्बी या पौधों के रस के साथ मिलाया जाता था। \n3. शैलियाँ और विकास:\n   - उच्च पुरापाषाण (सबसे पुराना): हरे रंग की छड़ी जैसी नृत्य आकृतियाँ और जंगली जानवरों की बड़ी रेखाकृतियाँ।\n   - मध्यपाषाण: चमकीले लाल रंग के छोटे, भरे हुए चित्र जो समूह शिकार, पारिवारिक जीवन, शहद इकट्ठा करने को दर्शाते हैं।\n   - ऐतिहासिक: सफेद और पीले रंग के चित्र जिनमें घुड़सवार, सैनिक और शिलालेख दिखाए गए हैं।\nमुख्य सीख: गुफा कला भारत में मानव संज्ञानात्मक, सामाजिक और तकनीकी विकास का एक दृश्य रिकॉर्ड प्रदान करती है।"
)

add_open(sec5_en, sec5_hi, "Teach the Concept",
    "Teach the Concept: Symbolic Behavior and Ornamentation in the Paleolithic\n\nExplain how archaeologists study symbolic behavior through prehistoric personal ornaments, focusing on the ostrich eggshell beads and engravings discovered at Patne.",
    "अवधारणा सिखाएं: पुरापाषाण काल में प्रतीकात्मक व्यवहार और अलंकरण\n\nसमझाएं कि पुरातत्वविद प्रागैतिहासिक व्यक्तिगत आभूषणों के माध्यम से प्रतीकात्मक व्यवहार का अध्ययन कैसे करते हैं, जिसमें पाटणे में खोजे गए शुतुरमुर्ग के अंडे के छिलके के मनकों और नक्काशी पर ध्यान केंद्रित किया गया हो।",
    "Symbolic behavior is the capacity to create physical objects to communicate abstract meanings. In prehistory, this is studied through personal ornamentation:\n1. The Ostrich Shell beads of Patne (c. 25,000 BCE): Making a bead is a multi-step technology. Eggshells are broken, drilled centrally with stone drills, threaded, and ground smooth on grooved sandstone. This proves early planning and technology.\n2. Symbolic Function: Unlike stone axes, beads do not cut meat. They communicate social identity. In mobile bands, beads are visual markers worn to convey group membership, marital readiness, or status without verbal communication.\n3. Abstract Engravings: Geometric lines on shells at Patne represent early abstract art, showing that humans were beginning to express patterns and ideas not found in nature.\nKey Takeaway: Ornaments prove that late Pleistocene humans had developed modern language, social codes, and aesthetic appreciation.",
    "प्रतीकात्मक व्यवहार अमूर्त अर्थों को संप्रेषित करने के लिए भौतिक वस्तुओं के निर्माण की क्षमता है। प्रागैतिहासिक काल में, इसका अध्ययन व्यक्तिगत आभूषणों के माध्यम से किया जाता है:\n1. पाटणे के शुतुरमुर्ग शेल मनके (लगभग 25,000 ईसा पूर्व): मनके बनाना एक बहु-चरणीय तकनीक है। अंडे के छिलकों को तोड़ना, पत्थर की ड्रिल से छेद करना, पिरोना और चिकना करना इसमें शामिल है। यह प्रारंभिक योजना और तकनीक को साबित करता है।\n2. प्रतीकात्मक कार्य: कुल्हाड़ियों के विपरीत, मनके मांस नहीं काटते। वे सामाजिक पहचान को संप्रेषित करते हैं। टोलियों में, मनके दृश्य संकेतक होते हैं जो समूह की सदस्यता या स्थिति को दर्शाते हैं।\n3. अमूर्त नक्काशी: पाटणे में छिलकों पर उकेरी गई ज्यामितीय रेखाएं प्रारंभिक अमूर्त कला का प्रतिनिधित्व करती हैं।\nमुख्य सीख: आभूषण साबित करते हैं कि लेट प्लीस्टोसीन काल में मनुष्यों ने आधुनिक भाषा, सामाजिक कोड और सौंदर्यबोध विकसित कर लिया था।"
)

add_open(sec5_en, sec5_hi, "Teach the Concept",
    "Teach the Concept: The Baghor I Prehistoric Shrine\n\nExplain the architecture, findings, and ethnographic significance of the Baghor I site in the Son Valley. Address why it represents an exceptional example of cultural continuity in Indian history.",
    "अवधारणा सिखाएं: बाघोर I प्रागैतिहासिक मंदिर (Prehistoric Shrine)\n\nसोन घाटी में बाघोर I स्थल की वास्तुकला, खोजों और नृवंशविज्ञान संबंधी महत्व की व्याख्या करें। इस बात पर चर्चा करें कि क्यों यह भारतीय इतिहास में सांस्कृतिक निरंतरता का एक असाधारण उदाहरण है।",
    "The Baghor I site represents the earliest known structural shrine in India. Key components include:\n1. Architecture: A low circular stone platform built of sandstone rubble, c. 85 cm in diameter, dating to the late Upper Paleolithic (c. 9000-8000 BCE).\n2. The Altar Stone: At the center of the platform was a natural triangular sandstone fragment displaying concentric rings of yellow, red, and brown colors. The stone was sourced from the Kaimur range, carried to the site.\n3. Ethnographic Continuity: Today, the local Gond and Kol tribal communities in the Son Valley build identical circular rubble platforms under trees, placing similar natural triangular laminated stones to worship 'Mai' (Mother Goddess) for fertility and protection.\nKey Takeaway: The Baghor I shrine is a classic model of using ethnographic analogy in archaeology, showing a religious practice that has survived with minimal change for over 10,000 years.",
    "बाघोर I स्थल भारत में सबसे पुराना ज्ञात मंदिर माना जाता है। मुख्य घटकों में शामिल हैं:\n1. वास्तुकला: बलुआ पत्थर के मलबे से बना एक गोलाकार चबूतरा, लगभग 85 सेमी व्यास का, जो उच्च पुरापाषाण काल (लगभग 9000-8000 ईसा पूर्व) का है।\n2. वेदी का पत्थर: चबूतरे के केंद्र में पीले, लाल और भूरे रंग के संकेंद्रित छल्लों वाला एक प्राकृतिक त्रिकोणीय बलुआ पत्थर का टुकड़ा था, जिसे कैमूर पहाड़ियों से लाया गया था।\n3. नृवंशविज्ञान निरंतरता: आज, सोन घाटी में स्थानीय गोंड और कोल आदिवासी समुदाय आज भी 'माई' (मातृ देवी) की पूजा करने के लिए इसी तरह के त्रिकोणीय पत्थरों वाले चबूतरे बनाते हैं।\nमुख्य सीख: बाघोर I मंदिर पुरातत्व में नृवंशविज्ञान सादृश्य के उपयोग का एक उत्कृष्ट मॉडल है, जो एक ऐसी धार्मिक प्रथा को दर्शाता है जो 10,000 से अधिक वर्षों से जीवित है।"
)
